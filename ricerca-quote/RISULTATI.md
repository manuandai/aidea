# Variazioni di quota: risultati

## Fase 1: dati storici gratuiti

**Dati.** 24.105 partite di Serie A, Serie B, Premier League, Championship, League One, League Two e National
League, dalla stagione 2019-20 a quella in corso (football-data.co.uk). Per ogni partita ci sono due fotografie
delle quote 1X2: una "iniziale" (il venerdì per le partite del fine settimana, il martedì per quelle
infrasettimanali) e una di chiusura, per fino a 11 bookmaker.

**Riferimento del mercato.** Pinnacle su 20.787 partite. Le sue quote smettono di essere pubblicate a metà del
2025-26 e mancano nella stagione in corso. Per il periodo recente (dal 2024-25, 7.407 partite) si usa
l'exchange Betfair.

Le tabelle complete sono in [`tabelle_fase1.md`](tabelle_fase1.md) e si rigenerano con
`python3 fase1_storico.py`. Per leggerle: il ROI è il guadagno medio per euro puntato. Tra parentesi quadre
c'è l'intervallo al 95%: se comprende lo zero, il risultato non si distingue dal caso. Il CLV è di quanto la
quota presa batte la quota giusta di chiusura; è l'indicatore più affidabile, perché ha molto meno rumore del
ROI.

### In breve

1. **Le variazioni hanno senso in entrambi i versi.** Quando una quota scende, l'esito esce più spesso; quando
   sale, esce meno. Alla chiusura la probabilità è giusta, entro un punto percentuale, in tutte le fasce. Il
   movimento non va oltre il dovuto (non c'è un rimbalzo da sfruttare andando contro) e non resta a metà (non
   c'è una scia da seguire dopo).
2. **Seguire il movimento a cose fatte fa perdere, in entrambi i versi.** Alla quota di chiusura di Bet365:
   −7% sugli esiti scesi oltre il 10%, −12% su quelli saliti oltre il 10%.
3. **Il guadagno sta nell'arrivare prima.** Chi avesse preso alla quota iniziale di Bet365 gli esiti poi scesi
   oltre il 10% avrebbe fatto **+8,3%** (intervallo +3,0 / +13,0). Non è realizzabile così com'è, perché bisogna
   sapere in anticipo che la quota scenderà: è esattamente ciò che le proiezioni devono stimare.
4. **C'è un segnale realizzabile.** Quando la quota iniziale di Bet365 supera di oltre il 3% la quota giusta di
   Pinnacle *nello stesso momento*, la giocata batte la chiusura in media del **+2,8% ±0,8** (910 casi). Oltre il
   5% il vantaggio sale a **+4,2% ±1,4** (419 casi). È un vantaggio vero, ma piccolo e raro: circa 130 casi
   all'anno con due sole fotografie per partita. Inoltre Bet365 limita in fretta i conti che vincono.
5. **I bookmaker lenti esistono, ma alla chiusura hanno già recuperato abbastanza.** William Hill segue solo il
   60% dei movimenti di Pinnacle, bwin il 78%, Bet365 l'87%. Quando restano indietro, alla chiusura la loro
   quota è comunque in media ancora sotto il prezzo giusto (da −0,2% a −3,8%), perché il margine assorbe il
   ritardo. Il ritardo si può sfruttare solo nei minuti dopo il movimento, che con due fotografie non si vedono.

### L'ipotesi sui campionati minori

**In parte confermata.** Nei campionati minori il mercato è meno efficiente, ma il margine del bookmaker lo
compensa.

| Indizio | Maggiori (A, Premier) | Minori | Verdetto |
|---|---|---|---|
| Margine Pinnacle a chiusura | 2,7% | 3,7% (National 4,7%) | prezzi meno affilati nei minori |
| Margine Bet365 a chiusura | 5,5% | 6,3% (National 8,2%) | ma il bookmaker si fa pagare di più |
| Partite con Bet365 iniziale oltre il 3% sopra Pinnacle | 3,0% | 4,8% | occasioni più frequenti nei minori |
| CLV di quelle giocate | +4,4% ±2,1 | +2,5% ±0,8 | ma non più grandi |
| Quanto i bookmaker seguono Pinnacle | 0,79-0,80 | 0,74-0,83 | Serie B e National reagiscono un po' meno |
| Margine dell'exchange Betfair alla quota iniziale | 0,7% | 3,4% (Serie B 4,8%, National 6,5%) | exchange poco liquido prima della partita |
| Lo scarto Bet365-exchange anticipa dove andrà l'exchange | 52% delle volte | 61% (Serie B 63%) | nei minori l'exchange "impara" dai bookmaker |

La Serie B è quella che si muove di più: il 22% degli esiti cambia oltre il 10% tra le due fotografie (30% con
il riferimento Betfair), contro il 13-19% degli altri campionati, ed è anche dove le quote iniziali sono meno
precise ("informazione tardiva" 4,5‰ contro 2,2‰ della Serie A).

### Cautele

- Con tante tabelle e celle, qualche ROI positivo esce per caso. Esempi: Serie B "scesa oltre 10%" +4%,
  League One +4%, Premier "bookmaker lenti" +2%. Nessuno di questi ha un intervallo che esclude lo zero; vanno
  trattati come rumore finché non si ripetono su dati nuovi.
- Le due fotografie non sono la vera apertura e non mostrano il percorso della quota durante la settimana.
- Non ci sono bookmaker italiani né la Serie C.
- Le quote dell'exchange qui sono solo quelle di "punta", senza "banca" né volumi, e non tengono conto della
  commissione del 5%. Nei campionati minori, prima della partita, sono un riferimento debole.

### Cosa cambia per la fase 2 e per l'architettura

- **Il riferimento deve essere l'exchange Betfair, e completo.** Pinnacle non è più disponibile da
  football-data e non ha più un'API pubblica. Dall'exchange servono la quota di punta e di banca (il prezzo
  giusto è a metà) e i volumi, altrimenti nei campionati minori il riferimento è troppo rumoroso. Questo
  conferma che serve l'API di Betfair.it, possibilmente con la chiave live, che restituisce i volumi.
- **Contano le fotografie simultanee e frequenti.** L'unico segnale realizzabile (punto 4) nasce dal
  confronto di più bookmaker nello stesso istante. Con fotografie ogni pochi minuti, le occasioni dovrebbero
  essere molte più di 130 all'anno, e si misura per quanto restano aperte.
- **Le proiezioni sono il cuore.** Il valore sta nel prevedere il movimento (punto 3). Lo scarto tra bookmaker
  ed exchange è già un primo indizio, più forte nei campionati minori. Le proiezioni della fase 4 partono da
  qui.
- **Serie B e bookmaker italiani sono il terreno più promettente** da verificare dal vivo: è il campionato che
  si muove di più, dove l'exchange è meno liquido e dove i bookmaker italiani, che football-data non copre,
  potrebbero essere i più lenti.

## Fase 2: primi controlli, senza account (26 novembre 2026)

Controllo di raggiungibilità dall'ambiente cloud in cui lavoro (server fuori dall'Italia):

| Fonte | Esito | Significato |
|---|---|---|
| The Odds API | risponde (chiede la chiave) | usabile dal cloud |
| OddsPapi | risponde | usabile dal cloud |
| API-Football | risponde (chiede la chiave) | usabile dal cloud |
| Betfair.it (login) | bloccato da Cloudflare | probabile blocco per paese o per server |
| Eurobet, Goldbet | pagina anti-bot di Cloudflare | lettura automatica bloccata dal cloud |
| Snai, Sisal | connessione chiusa | come sopra |

Conseguenza per l'architettura: Betfair.it e i bookmaker italiani vanno letti da una connessione italiana
domestica, cioè dal computer dell'utente o da un dispositivo a casa sua. Le API a pagamento o gratuite dei
fornitori possono invece girare nel cloud.
