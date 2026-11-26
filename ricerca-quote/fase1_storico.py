#!/usr/bin/env python3
"""Fase 1: verifica sui dati storici gratuiti di football-data.co.uk.

Per ogni partita ci sono due fotografie delle quote 1X2: una "iniziale" (presa il venerdì per le partite del
fine settimana, il martedì per quelle infrasettimanali) e una di chiusura. Il riferimento del mercato è
Pinnacle fino al 2025-26, quando le sue quote smettono di essere pubblicate, e l'exchange Betfair dal 2024-25.

Uso:
    python3 fase1_storico.py            # scarica i dati mancanti e scrive tabelle_fase1.md
    python3 fase1_storico.py --aggiorna # riscarica anche le stagioni già presenti
"""
import argparse
import os
import urllib.request

import numpy as np
import pandas as pd

QUI = os.path.dirname(os.path.abspath(__file__))
DATI = os.path.join(QUI, "dati")
USCITA = os.path.join(QUI, "tabelle_fase1.md")

LEGHE = {
    "I1": "Serie A", "I2": "Serie B",
    "E0": "Premier League", "E1": "Championship", "E2": "League One", "E3": "League Two",
    "EC": "National League",
}
MAGGIORI = {"I1", "E0"}
STAGIONI = ["1920", "2021", "2122", "2223", "2324", "2425", "2526", "2627"]
IN_CORSO = "2627"
ESITI = "HDA"
# Bookmaker tradizionali presenti almeno in alcune stagioni (prefisso delle colonne di football-data).
BOOK = {
    "B365": "Bet365", "BW": "bwin", "WH": "William Hill", "BF": "Betfair sportsbook", "1XB": "1xBet",
    "IW": "Interwetten", "VC": "VC Bet", "BFD": "Betfred", "BV": "BetVictor", "PP": "Paddy Power",
    "SKB": "Sky Bet",
}
RIFERIMENTI = {"PS": "Pinnacle", "BFE": "exchange Betfair"}
FASCE = [(-np.inf, -0.10, "scesa oltre 10%"), (-0.10, -0.03, "scesa 3-10%"), (-0.03, 0.03, "ferma (±3%)"),
         (0.03, 0.10, "salita 3-10%"), (0.10, np.inf, "salita oltre 10%")]
RNG = np.random.default_rng(20261126)


# ---------------------------------------------------------------- dati

def scarica(aggiorna=False):
    os.makedirs(DATI, exist_ok=True)
    for s in STAGIONI:
        for lega in LEGHE:
            f = os.path.join(DATI, f"{lega}_{s}.csv")
            if os.path.exists(f) and os.path.getsize(f) > 0 and not (aggiorna or s == IN_CORSO):
                continue
            url = f"https://www.football-data.co.uk/mmz4281/{s}/{lega}.csv"
            try:
                with urllib.request.urlopen(url, timeout=60) as r:
                    dati = r.read()
            except Exception as e:  # una stagione mancante non blocca le altre
                print(f"  impossibile scaricare {url}: {e}")
                continue
            with open(f, "wb") as out:
                out.write(dati)


def carica():
    parti = []
    for s in STAGIONI:
        for lega in LEGHE:
            f = os.path.join(DATI, f"{lega}_{s}.csv")
            if not os.path.exists(f) or os.path.getsize(f) == 0:
                continue
            x = pd.read_csv(f, encoding="latin1", on_bad_lines="skip")
            x = x.dropna(subset=["FTR"]).copy()
            x["lega"], x["stagione"] = lega, s
            parti.append(x)
    df = pd.concat(parti, ignore_index=True)
    return df[df.FTR.isin(list(ESITI))].reset_index(drop=True)


def tripla(df, prefisso, chiusura):
    """Quote 1X2 (n×3) di un bookmaker; NaN dove mancano o non sono plausibili."""
    c = "C" if chiusura else ""
    cols = [f"{prefisso}{c}{o}" for o in ESITI]
    if not all(col in df for col in cols):
        return np.full((len(df), 3), np.nan)
    q = df[cols].apply(pd.to_numeric, errors="coerce").to_numpy(float, copy=True)
    with np.errstate(divide="ignore"):
        somma = (1 / q).sum(1)
    ok = (q > 1.01).all(1) & (somma > 0.97) & (somma < 1.30)
    q[~ok] = np.nan
    return q


def equa(q):
    """Probabilità senza margine (normalizzazione proporzionale)."""
    inv = 1 / q
    return inv / inv.sum(1, keepdims=True)


# ---------------------------------------------------------------- statistica

def roi(quote, vinte):
    """ROI medio (puntata 1) e intervallo al 95% con bootstrap."""
    quote, vinte = np.asarray(quote), np.asarray(vinte, bool)
    n = len(quote)
    if n == 0:
        return 0, np.nan, np.nan, np.nan
    utile = np.where(vinte, quote - 1, -1.0)
    medie = utile[RNG.integers(0, n, size=(1000, n))].mean(1) if n > 1 else utile
    return n, utile.mean() * 100, np.percentile(medie, 2.5) * 100, np.percentile(medie, 97.5) * 100


def fmt_roi(r):
    n, m, lo, hi = r
    if n == 0:
        return "–"
    return f"{m:+.1f}% [{lo:+.1f}; {hi:+.1f}]"


def fmt_media(x):
    """Media in % con margine d'errore al 95% (approssimazione normale)."""
    x = np.asarray(x)
    if len(x) < 2:
        return "–"
    return f"{x.mean() * 100:+.1f}% ±{1.96 * x.std(ddof=1) / np.sqrt(len(x)) * 100:.1f}"


def tabella(intestazioni, righe):
    out = ["| " + " | ".join(intestazioni) + " |", "|" + "|".join("---" for _ in intestazioni) + "|"]
    out += ["| " + " | ".join(str(c) for c in r) + " |" for r in righe]
    return "\n".join(out)


# ---------------------------------------------------------------- analisi

class Campione:
    """Partite con riferimento e Bet365 validi in entrambe le fotografie, in formato per esito (n×3)."""

    def __init__(self, df, rif):
        re_, rc = tripla(df, rif, False), tripla(df, rif, True)
        be, bc = tripla(df, "B365", False), tripla(df, "B365", True)
        ok = ~(np.isnan(re_).any(1) | np.isnan(rc).any(1) | np.isnan(be).any(1) | np.isnan(bc).any(1))
        self.df = df[ok].reset_index(drop=True)
        self.re, self.rc, self.be, self.bc = re_[ok], rc[ok], be[ok], bc[ok]
        self.pre, self.prc = equa(self.re), equa(self.rc)
        self.pbe = equa(self.be)
        self.vinto = np.stack([(self.df.FTR == o).to_numpy() for o in ESITI], 1)
        self.maxe, self.maxc = tripla(self.df, "Max", False), tripla(self.df, "Max", True)
        self.avge, self.avgc = tripla(self.df, "Avg", False), tripla(self.df, "Avg", True)
        self.mov = self.rc / self.re - 1  # variazione % della quota di riferimento

    def sotto(self, maschera_partite):
        c = object.__new__(Campione)
        for k, v in self.__dict__.items():
            c.__dict__[k] = v[maschera_partite].reset_index(drop=True) if k == "df" else v[maschera_partite]
        return c


def gruppi(c):
    yield "**Tutti**", np.ones(len(c.df), bool)
    yield "Maggiori (A, Premier)", c.df.lega.isin(MAGGIORI).to_numpy()
    yield "Minori (le altre)", ~c.df.lega.isin(MAGGIORI).to_numpy()
    for lega, nome in LEGHE.items():
        yield nome, (c.df.lega == lega).to_numpy()


def logloss(p, vinto):
    return -np.log(p[vinto]).mean()


def sezione_mercato(c, nome_rif):
    righe = []
    for nome, m in gruppi(c):
        s = c.sotto(m)
        if len(s.df) < 50:
            continue
        mov = np.abs(s.mov).ravel()
        disp_e = np.nanmean(s.maxe / s.avge - 1) * 100
        disp_c = np.nanmean(s.maxc / s.avgc - 1) * 100
        guadagno = (logloss(s.pre, s.vinto) - logloss(s.prc, s.vinto)) * 1000
        righe.append([
            nome, len(s.df),
            f"{((1 / s.re).sum(1).mean() - 1) * 100:.1f}% / {((1 / s.rc).sum(1).mean() - 1) * 100:.1f}%",
            f"{((1 / s.be).sum(1).mean() - 1) * 100:.1f}% / {((1 / s.bc).sum(1).mean() - 1) * 100:.1f}%",
            f"{np.median(mov) * 100:.1f}%", f"{(mov > 0.05).mean() * 100:.0f}%", f"{(mov > 0.10).mean() * 100:.0f}%",
            f"{guadagno:.1f}", f"{disp_e:.1f}% / {disp_c:.1f}%",
        ])
    return tabella(
        ["Campionato", "Partite", f"Margine {nome_rif} (iniz./chius.)", "Margine Bet365 (iniz./chius.)",
         "Movimento mediano", "Esiti mossi >5%", ">10%", "Informazione tardiva (‰ log-loss)",
         "Max/media −1 (iniz./chius.)"], righe)


def sezione_valore(c, nome_rif):
    """Quote iniziali sopra il prezzo giusto: rispetto alla chiusura (CLV) e allo stesso momento (realizzabile)."""
    righe = []
    for nome, m in gruppi(c):
        s = c.sotto(m)
        if len(s.df) < 50:
            continue
        clv = s.be * s.prc - 1
        riga = [nome, f"{(clv > 0).mean() * 100:.1f}%"]
        for soglia in (0.0, 0.03, 0.05):
            sel = s.be * s.pre > 1 + soglia
            r = roi(s.be[sel], s.vinto[sel])
            riga.append(f"n={r[0]} · {fmt_roi(r)} · CLV {fmt_media(clv[sel])}")
        sel = s.maxe * s.pre > 1.05
        sel &= ~np.isnan(s.maxe)
        r = roi(s.maxe[sel], s.vinto[sel])
        riga.append(f"n={r[0]} · {fmt_roi(r)}")
        righe.append(riga)
    return tabella(
        ["Campionato", "Esiti con quota Bet365 iniziale sopra la chiusura giusta",
         f"Bet365 iniz. > giusta {nome_rif} iniz.", "… oltre 3%", "… oltre 5%",
         "Quota migliore iniz. oltre 5%"], righe)


def sezione_direzione(c, nome_rif):
    righe = []
    for nome, m in gruppi(c):
        s = c.sotto(m)
        if len(s.df) < 50:
            continue
        scarto = (s.pbe - s.pre).ravel()  # Bet365 vede l'esito più probabile del riferimento
        passo = (s.prc - s.pre).ravel()   # come si muove poi il riferimento
        forte = np.abs(scarto) > 0.02
        concordi = (np.sign(passo[forte]) == np.sign(scarto[forte])).mean() * 100 if forte.any() else np.nan
        righe.append([nome, f"{np.corrcoef(scarto, passo)[0, 1]:+.2f}", int(forte.sum()), f"{concordi:.0f}%"])
    return tabella(
        ["Campionato", f"Correlazione scarto Bet365−{nome_rif} / movimento successivo",
         "Esiti con scarto >2 punti", f"… in cui {nome_rif} si sposta verso Bet365"], righe)


def sezione_fasce(c, nome_rif):
    righe = []
    for lo, hi, etichetta in FASCE:
        sel = (c.mov > lo) & (c.mov <= hi)
        if not sel.any():
            continue
        v = c.vinto[sel]
        righe.append([
            etichetta, int(sel.sum()), f"{v.mean() * 100:.1f}%", f"{c.pre[sel].mean() * 100:.1f}%",
            f"{c.prc[sel].mean() * 100:.1f}%", fmt_roi(roi(c.be[sel], v)), fmt_roi(roi(c.bc[sel], v)),
            fmt_roi(roi(c.maxc[sel & ~np.isnan(c.maxc)], c.vinto[sel & ~np.isnan(c.maxc)])),
        ])
    tab1 = tabella(
        [f"Quota {nome_rif}", "Esiti", "Frequenza reale", "Prob. giusta iniziale", "Prob. giusta chiusura",
         "ROI Bet365 iniziale", "ROI Bet365 chiusura", "ROI quota migliore chiusura"], righe)
    righe = []
    for nome, m in gruppi(c):
        s = c.sotto(m)
        if len(s.df) < 50:
            continue
        riga = [nome]
        for lo, hi, _ in FASCE:
            sel = (s.mov > lo) & (s.mov <= hi)
            if sel.sum() < 30:
                riga.append("–")
                continue
            scarto = (s.vinto[sel].mean() - s.prc[sel].mean()) * 100
            riga.append(f"{scarto:+.1f} pt · ROI {roi(s.bc[sel], s.vinto[sel])[1]:+.0f}% (n={int(sel.sum())})")
        righe.append(riga)
    tab2 = tabella(["Campionato"] + [f[2] for f in FASCE], righe)
    return tab1, tab2


def sezione_lenti(df, rif, nome_rif):
    """Quanto ogni bookmaker segue il movimento del riferimento, e cosa rende quando resta indietro."""
    re_, rc = tripla(df, rif, False), tripla(df, rif, True)
    ok_rif = ~(np.isnan(re_).any(1) | np.isnan(rc).any(1))
    vinto = np.stack([(df.FTR == o).to_numpy() for o in ESITI], 1)
    prc = equa(np.where(ok_rif[:, None], rc, 1.5))
    lr = np.log(rc / re_)
    righe, per_lega = [], {}
    for b, nome_b in BOOK.items():
        be, bc = tripla(df, b, False), tripla(df, b, True)
        ok = ok_rif & ~(np.isnan(be).any(1) | np.isnan(bc).any(1))
        if ok.sum() < 300:
            continue
        lb = np.log(bc / be)
        x, y = lr[ok].ravel(), lb[ok].ravel()
        beta = np.polyfit(x, y, 1)[0]
        # il riferimento accorcia oltre il 5% e il bookmaker fa meno della metà del movimento
        lento = ok[:, None] & (lr < np.log(0.95)) & (lb > 0.5 * lr)
        r = roi(bc[lento], vinto[lento])
        vant = (bc * prc - 1)[lento].mean() * 100 if lento.any() else np.nan
        righe.append([nome_b, int(ok.sum()), f"{beta:.2f}", int(lento.sum()), f"{vant:+.1f}%", fmt_roi(r)])
        for lega in LEGHE:
            ml = (df.lega == lega).to_numpy()
            okl = ok & ml
            if okl.sum() < 150:
                continue
            bl = np.polyfit(lr[okl].ravel(), lb[okl].ravel(), 1)[0]
            ll = lento & ml[:, None]
            per_lega.setdefault(lega, []).append((bl, bc[ll], vinto[ll], (bc * prc - 1)[ll]))
    tab1 = tabella(
        ["Bookmaker", "Partite", f"Quanto segue {nome_rif} (1 = tutto)", "Casi in ritardo",
         f"Vantaggio medio sulla chiusura giusta {nome_rif}", "ROI alla sua quota di chiusura"], righe)
    righe = []
    for lega, nome in LEGHE.items():
        if lega not in per_lega:
            continue
        v = per_lega[lega]
        q = np.concatenate([t[1] for t in v])
        w = np.concatenate([t[2] for t in v])
        vant = np.concatenate([t[3] for t in v])
        righe.append([nome, f"{np.mean([t[0] for t in v]):.2f}", len(q),
                      f"{vant.mean() * 100:+.1f}%" if len(q) else "–", fmt_roi(roi(q, w))])
    tab2 = tabella(["Campionato", f"Quanto seguono {nome_rif} (media bookmaker)", "Casi in ritardo",
                    "Vantaggio medio", "ROI"], righe)
    return tab1, tab2


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--aggiorna", action="store_true", help="riscarica tutte le stagioni")
    args = ap.parse_args()
    scarica(args.aggiorna)
    df = carica()
    print(f"partite caricate: {len(df)}")

    testo = ["# Fase 1: tabelle generate", "",
             f"Generato da `fase1_storico.py` su {len(df)} partite. ROI con intervallo al 95% tra parentesi "
             "quadre. Le quote dell'exchange non tengono conto della commissione (5% sulle vincite nette).", ""]
    for rif, nome_rif in RIFERIMENTI.items():
        c = Campione(df, rif)
        stag = sorted(c.df.stagione.unique())
        print(f"{nome_rif}: {len(c.df)} partite, stagioni {stag[0]}-{stag[-1]}")
        testo += [f"## Riferimento: {nome_rif}", "",
                  f"{len(c.df)} partite con {nome_rif} e Bet365 in entrambe le fotografie, stagioni "
                  f"{', '.join(s[:2] + '-' + s[2:] for s in stag)}.", ""]
        testo += ["### 1-4. Mercato e movimenti", "", sezione_mercato(c, nome_rif), ""]
        testo += ["### 5-6. Quote iniziali sopra il prezzo giusto", "", sezione_valore(c, nome_rif), ""]
        testo += ["### 7. Lo scarto iniziale anticipa la direzione?", "", sezione_direzione(c, nome_rif), ""]
        t1, t2 = sezione_fasce(c, nome_rif)
        testo += ["### 8. Discese e salite a confronto", "", "Tutti i campionati:", "", t1, "",
                  "Per campionato: frequenza reale meno probabilità giusta di chiusura (punti) e ROI di Bet365 "
                  "alla chiusura.", "", t2, ""]
        t1, t2 = sezione_lenti(df, rif, nome_rif)
        testo += ["### 9. Bookmaker lenti", "",
                  f"Casi in ritardo: la quota {nome_rif} scende oltre il 5% e il bookmaker fa meno della metà "
                  "del movimento.", "", t1, "", t2, ""]
    with open(USCITA, "w", encoding="utf-8") as f:
        f.write("\n".join(testo))
    print(f"scritto {USCITA}")


if __name__ == "__main__":
    main()
