# Fase 1: tabelle generate

Generato da `fase1_storico.py` su 24105 partite. ROI con intervallo al 95% tra parentesi quadre. Le quote dell'exchange non tengono conto della commissione (5% sulle vincite nette).

## Riferimento: Pinnacle

20787 partite con Pinnacle e Bet365 in entrambe le fotografie, stagioni 19-20, 20-21, 21-22, 22-23, 23-24, 24-25, 25-26.

### 1-4. Mercato e movimenti

| Campionato | Partite | Margine Pinnacle (iniz./chius.) | Margine Bet365 (iniz./chius.) | Movimento mediano | Esiti mossi >5% | >10% | Informazione tardiva (‰ log-loss) | Max/media −1 (iniz./chius.) |
|---|---|---|---|---|---|---|---|---|
| **Tutti** | 20787 | 3.8% / 3.5% | 6.1% / 6.1% | 4.2% | 43% | 18% | 3.1 | 5.4% / 6.1% |
| Maggiori (A, Premier) | 4965 | 3.0% / 2.7% | 5.5% / 5.5% | 4.3% | 44% | 18% | 3.1 | 5.3% / 6.1% |
| Minori (le altre) | 15822 | 4.1% / 3.7% | 6.3% / 6.3% | 4.1% | 43% | 17% | 3.1 | 5.5% / 6.1% |
| Serie A | 2475 | 3.0% / 2.8% | 5.5% / 5.6% | 4.5% | 46% | 19% | 2.2 | 5.5% / 6.2% |
| Serie B | 2344 | 3.5% / 3.2% | 6.7% / 6.6% | 4.7% | 47% | 22% | 4.5 | 5.8% / 6.6% |
| Premier League | 2490 | 3.0% / 2.7% | 5.4% / 5.5% | 4.2% | 43% | 18% | 4.0 | 5.1% / 6.0% |
| Championship | 3567 | 3.4% / 3.1% | 5.6% / 5.7% | 3.7% | 38% | 13% | 1.4 | 4.7% / 5.4% |
| League One | 3308 | 4.1% / 3.6% | 5.6% / 5.6% | 4.1% | 42% | 16% | 3.2 | 5.6% / 6.2% |
| League Two | 3349 | 4.2% / 3.8% | 5.6% / 5.6% | 3.8% | 39% | 14% | 3.9 | 5.3% / 5.8% |
| National League | 3254 | 5.2% / 4.7% | 8.3% / 8.2% | 4.9% | 49% | 24% | 2.8 | 6.1% / 7.0% |

### 5-6. Quote iniziali sopra il prezzo giusto

| Campionato | Esiti con quota Bet365 iniziale sopra la chiusura giusta | Bet365 iniz. > giusta Pinnacle iniz. | … oltre 3% | … oltre 5% | Quota migliore iniz. oltre 5% |
|---|---|---|---|---|---|
| **Tutti** | 20.2% | n=3346 · -2.1% [-8.1; +4.4] · CLV +0.8% ±0.3 | n=910 · +6.0% [-7.2; +19.7] · CLV +2.8% ±0.8 | n=419 · +0.1% [-20.2; +23.1] · CLV +4.2% ±1.4 | n=1869 · -7.4% [-18.3; +4.4] |
| Maggiori (A, Premier) | 21.4% | n=519 · +13.7% [-7.2; +35.2] · CLV +1.0% ±1.0 | n=148 · +33.2% [-13.7; +85.1] · CLV +4.4% ±2.1 | n=69 · +25.7% [-42.4; +102.5] · CLV +4.8% ±3.6 | n=902 · -1.8% [-21.1; +19.4] |
| Minori (le altre) | 19.9% | n=2827 · -5.0% [-11.1; +1.4] · CLV +0.7% ±0.4 | n=762 · +0.7% [-12.5; +13.6] · CLV +2.5% ±0.8 | n=350 · -5.0% [-24.4; +15.0] · CLV +4.1% ±1.5 | n=967 · -12.6% [-24.6; -0.3] |
| Serie A | 22.1% | n=249 · +12.3% [-16.3; +43.9] · CLV +0.6% ±1.5 | n=64 · +37.4% [-25.8; +104.1] · CLV +3.7% ±3.4 | n=29 · -22.4% [-100.0; +69.0] · CLV +5.9% ±6.2 | n=440 · -9.3% [-33.5; +16.4] |
| Serie B | 22.4% | n=408 · +2.1% [-13.7; +18.0] · CLV +0.7% ±0.7 | n=75 · +23.2% [-16.3; +63.8] · CLV +2.3% ±1.8 | n=23 · +24.3% [-59.8; +122.2] · CLV +1.6% ±3.7 | n=166 · -2.3% [-26.6; +22.7] |
| Premier League | 20.6% | n=270 · +14.9% [-13.7; +47.8] · CLV +1.3% ±1.3 | n=84 · +30.0% [-33.1; +107.4] · CLV +4.9% ±2.7 | n=40 · +60.6% [-43.1; +176.2] · CLV +4.1% ±4.3 | n=462 · +5.3% [-23.6; +37.7] |
| Championship | 18.2% | n=413 · -2.7% [-19.5; +15.8] · CLV +1.1% ±0.9 | n=76 · +17.2% [-30.3; +67.9] · CLV +3.3% ±2.6 | n=37 · +24.1% [-45.1; +103.2] · CLV +4.1% ±4.6 | n=123 · -35.6% [-64.3; -4.3] |
| League One | 21.0% | n=641 · -11.5% [-23.9; +0.9] · CLV +0.5% ±0.7 | n=165 · +1.1% [-28.3; +30.7] · CLV +3.4% ±1.7 | n=64 · -15.2% [-60.4; +35.3] · CLV +4.0% ±3.7 | n=228 · -14.7% [-38.6; +12.4] |
| League Two | 21.1% | n=725 · -5.3% [-17.0; +7.0] · CLV +0.7% ±0.6 | n=172 · -6.6% [-30.0; +19.2] · CLV +1.7% ±1.5 | n=73 · -9.0% [-49.2; +29.5] · CLV +3.6% ±2.5 | n=170 · -16.6% [-39.7; +9.8] |
| National League | 17.4% | n=640 · -4.0% [-17.3; +10.2] · CLV +0.7% ±1.0 | n=274 · -5.8% [-26.4; +16.7] · CLV +2.4% ±1.7 | n=153 · -10.2% [-37.7; +20.4] · CLV +4.7% ±2.6 | n=280 · -4.5% [-27.0; +21.6] |

### 7. Lo scarto iniziale anticipa la direzione?

| Campionato | Correlazione scarto Bet365−Pinnacle / movimento successivo | Esiti con scarto >2 punti | … in cui Pinnacle si sposta verso Bet365 |
|---|---|---|---|
| **Tutti** | +0.04 | 3873 | 55% |
| Maggiori (A, Premier) | +0.04 | 246 | 59% |
| Minori (le altre) | +0.04 | 3627 | 54% |
| Serie A | +0.03 | 146 | 58% |
| Serie B | +0.03 | 661 | 59% |
| Premier League | +0.04 | 100 | 60% |
| Championship | +0.02 | 292 | 42% |
| League One | +0.07 | 441 | 59% |
| League Two | +0.06 | 524 | 58% |
| National League | +0.03 | 1709 | 52% |

### 8. Discese e salite a confronto

Tutti i campionati:

| Quota Pinnacle | Esiti | Frequenza reale | Prob. giusta iniziale | Prob. giusta chiusura | ROI Bet365 iniziale | ROI Bet365 chiusura | ROI quota migliore chiusura |
|---|---|---|---|---|---|---|---|
| scesa oltre 10% | 3917 | 34.3% | 28.8% | 33.7% | +8.3% [+3.0; +13.0] | -6.9% [-11.8; -2.1] | +2.1% [-3.1; +7.5] |
| scesa 3-10% | 13755 | 35.5% | 33.7% | 35.9% | -1.6% [-4.0; +1.0] | -6.5% [-9.0; -4.2] | -0.8% [-3.4; +1.6] |
| ferma (±3%) | 23927 | 35.3% | 34.6% | 34.8% | -3.7% [-5.6; -1.8] | -4.0% [-5.9; -2.4] | +0.5% [-1.4; +2.5] |
| salita 3-10% | 13681 | 31.8% | 33.9% | 32.2% | -12.0% [-14.6; -9.7] | -8.3% [-10.6; -5.7] | -3.0% [-5.6; -0.3] |
| salita oltre 10% | 7081 | 25.0% | 29.7% | 25.7% | -22.8% [-26.3; -19.2] | -11.9% [-15.9; -7.8] | -6.0% [-10.4; -1.5] |

Per campionato: frequenza reale meno probabilità giusta di chiusura (punti) e ROI di Bet365 alla chiusura.

| Campionato | scesa oltre 10% | scesa 3-10% | ferma (±3%) | salita 3-10% | salita oltre 10% |
|---|---|---|---|---|---|
| **Tutti** | +0.5 pt · ROI -7% (n=3917) | -0.3 pt · ROI -6% (n=13755) | +0.5 pt · ROI -4% (n=23927) | -0.4 pt · ROI -8% (n=13681) | -0.6 pt · ROI -12% (n=7081) |
| Maggiori (A, Premier) | -1.0 pt · ROI -14% (n=1014) | -0.5 pt · ROI -7% (n=3420) | +1.2 pt · ROI -1% (n=5583) | -0.4 pt · ROI -10% (n=3171) | -1.6 pt · ROI -17% (n=1707) |
| Minori (le altre) | +1.1 pt · ROI -4% (n=2903) | -0.3 pt · ROI -6% (n=10335) | +0.3 pt · ROI -5% (n=18344) | -0.4 pt · ROI -8% (n=10510) | -0.3 pt · ROI -10% (n=5374) |
| Serie A | -2.3 pt · ROI -17% (n=487) | -1.0 pt · ROI -10% (n=1741) | +0.8 pt · ROI -3% (n=2733) | +1.2 pt · ROI -5% (n=1539) | -1.1 pt · ROI -18% (n=925) |
| Serie B | +1.2 pt · ROI -6% (n=568) | -1.2 pt · ROI -8% (n=1607) | +1.9 pt · ROI +1% (n=2462) | -1.3 pt · ROI -12% (n=1441) | -1.8 pt · ROI -15% (n=954) |
| Premier League | +0.3 pt · ROI -12% (n=527) | +0.0 pt · ROI -4% (n=1679) | +1.6 pt · ROI +1% (n=2850) | -1.9 pt · ROI -14% (n=1632) | -2.1 pt · ROI -17% (n=782) |
| Championship | +0.8 pt · ROI -0% (n=476) | -0.3 pt · ROI -6% (n=2307) | -0.6 pt · ROI -7% (n=4551) | +1.4 pt · ROI -0% (n=2436) | -0.5 pt · ROI -11% (n=931) |
| League One | +0.4 pt · ROI -6% (n=549) | +0.5 pt · ROI -6% (n=2182) | -0.2 pt · ROI -7% (n=3910) | -0.0 pt · ROI -8% (n=2219) | -0.6 pt · ROI -10% (n=1064) |
| League Two | +3.4 pt · ROI -0% (n=479) | +0.2 pt · ROI -3% (n=2190) | +0.5 pt · ROI -4% (n=4178) | -1.1 pt · ROI -8% (n=2295) | -1.7 pt · ROI -13% (n=905) |
| National League | +0.2 pt · ROI -6% (n=831) | -1.0 pt · ROI -10% (n=2049) | +0.7 pt · ROI -5% (n=3243) | -1.4 pt · ROI -13% (n=2119) | +1.7 pt · ROI -5% (n=1520) |

### 9. Bookmaker lenti

Casi in ritardo: la quota Pinnacle scende oltre il 5% e il bookmaker fa meno della metà del movimento.

| Bookmaker | Partite | Quanto segue Pinnacle (1 = tutto) | Casi in ritardo | Vantaggio medio sulla chiusura giusta Pinnacle | ROI alla sua quota di chiusura |
|---|---|---|---|---|---|
| Bet365 | 20787 | 0.87 | 2405 | -2.2% | -4.2% [-10.9; +2.7] |
| bwin | 18995 | 0.78 | 3104 | -2.9% | -4.6% [-10.4; +1.0] |
| William Hill | 18482 | 0.60 | 4368 | -0.2% | -7.2% [-11.6; -2.7] |
| Betfair sportsbook | 3340 | 0.80 | 258 | -1.0% | -3.5% [-19.9; +14.8] |
| 1xBet | 3289 | 0.85 | 289 | +0.3% | -8.9% [-26.4; +10.3] |
| Interwetten | 14555 | 0.79 | 1874 | -3.8% | -3.4% [-10.6; +4.1] |
| VC Bet | 16147 | 0.85 | 2542 | -2.4% | -5.7% [-12.3; +0.6] |
| Betfred | 1265 | 0.78 | 110 | -0.6% | +1.8% [-28.4; +33.1] |
| BetVictor | 1266 | 0.77 | 124 | -1.0% | -14.7% [-42.0; +14.6] |

| Campionato | Quanto seguono Pinnacle (media bookmaker) | Casi in ritardo | Vantaggio medio | ROI |
|---|---|---|---|---|
| Serie A | 0.80 | 1632 | -1.8% | -18.1% [-25.9; -10.1] |
| Serie B | 0.76 | 2277 | -0.6% | -4.4% [-9.8; +1.4] |
| Premier League | 0.79 | 1679 | -1.1% | +2.0% [-7.8; +13.3] |
| Championship | 0.82 | 1829 | -2.0% | -2.4% [-9.1; +4.8] |
| League One | 0.77 | 2118 | -3.0% | -8.5% [-14.8; -2.7] |
| League Two | 0.83 | 2058 | -2.7% | +0.4% [-6.1; +7.2] |
| National League | 0.74 | 3473 | -2.0% | -6.7% [-11.0; -2.0] |

## Riferimento: exchange Betfair

7407 partite con exchange Betfair e Bet365 in entrambe le fotografie, stagioni 24-25, 25-26, 26-27.

### 1-4. Mercato e movimenti

| Campionato | Partite | Margine exchange Betfair (iniz./chius.) | Margine Bet365 (iniz./chius.) | Movimento mediano | Esiti mossi >5% | >10% | Informazione tardiva (‰ log-loss) | Max/media −1 (iniz./chius.) |
|---|---|---|---|---|---|---|---|---|
| **Tutti** | 7407 | 2.8% / 0.9% | 7.3% / 7.4% | 4.5% | 46% | 21% | 3.3 | 4.6% / 5.1% |
| Maggiori (A, Premier) | 1707 | 0.7% / 0.5% | 5.5% / 5.6% | 4.1% | 42% | 17% | 1.0 | 4.6% / 4.8% |
| Minori (le altre) | 5700 | 3.4% / 1.1% | 7.9% / 7.9% | 4.6% | 47% | 22% | 4.0 | 4.6% / 5.2% |
| Serie A | 859 | 0.8% / 0.5% | 5.5% / 5.7% | 4.2% | 42% | 18% | -0.4 | 4.8% / 5.0% |
| Serie B | 799 | 4.8% / 0.9% | 7.3% / 7.3% | 5.6% | 53% | 30% | 6.9 | 5.1% / 5.8% |
| Premier League | 848 | 0.6% / 0.6% | 5.5% / 5.6% | 4.1% | 42% | 16% | 2.5 | 4.4% / 4.7% |
| Championship | 1266 | 1.0% / 0.7% | 7.1% / 7.1% | 3.6% | 38% | 14% | 0.6 | 4.2% / 4.6% |
| League One | 1234 | 2.3% / 0.9% | 7.9% / 8.0% | 4.6% | 47% | 20% | 3.4 | 4.7% / 5.1% |
| League Two | 1228 | 3.2% / 1.0% | 8.0% / 8.0% | 4.3% | 44% | 17% | 3.6 | 4.4% / 4.7% |
| National League | 1173 | 6.5% / 1.9% | 8.9% / 8.9% | 6.2% | 57% | 32% | 6.6 | 5.0% / 5.8% |

### 5-6. Quote iniziali sopra il prezzo giusto

| Campionato | Esiti con quota Bet365 iniziale sopra la chiusura giusta | Bet365 iniz. > giusta exchange Betfair iniz. | … oltre 3% | … oltre 5% | Quota migliore iniz. oltre 5% |
|---|---|---|---|---|---|
| **Tutti** | 14.9% | n=562 · +8.7% [-4.7; +22.4] · CLV -2.3% ±0.7 | n=160 · -19.5% [-42.0; +3.4] · CLV -3.8% ±1.7 | n=85 · -24.5% [-56.0; +8.2] · CLV -3.9% ±2.5 | n=322 · +10.3% [-9.6; +30.6] |
| Maggiori (A, Premier) | 19.9% | n=50 · +56.5% [-2.6; +114.9] · CLV +1.1% ±2.6 | n=1 · -100.0% [-100.0; -100.0] · CLV – | n=0 · – · CLV – | n=53 · +15.3% [-36.5; +66.2] |
| Minori (le altre) | 13.4% | n=512 · +4.1% [-10.6; +17.7] · CLV -2.6% ±0.8 | n=159 · -19.0% [-43.7; +7.1] · CLV -3.5% ±1.6 | n=85 · -24.5% [-54.6; +9.5] · CLV -3.9% ±2.5 | n=269 · +9.3% [-12.6; +31.6] |
| Serie A | 21.3% | n=32 · +54.6% [-18.3; +132.6] · CLV +1.9% ±3.5 | n=1 · -100.0% [-100.0; -100.0] · CLV – | n=0 · – · CLV – | n=37 · -6.6% [-65.6; +62.7] |
| Serie B | 21.0% | n=124 · +5.9% [-23.3; +34.5] · CLV -2.0% ±1.6 | n=49 · -15.8% [-52.5; +25.0] · CLV -2.8% ±2.8 | n=25 · -39.6% [-86.0; +10.8] · CLV -4.8% ±3.6 | n=70 · +13.5% [-26.1; +56.4] |
| Premier League | 18.5% | n=18 · +59.7% [-34.7; +170.8] · CLV -0.4% ±3.7 | n=0 · – · CLV – | n=0 · – · CLV – | n=16 · +65.9% [-38.6; +180.8] |
| Championship | 12.4% | n=49 · +12.6% [-31.3; +59.1] · CLV +0.6% ±1.9 | n=3 · -100.0% [-100.0; -100.0] · CLV -14.5% ±22.9 | n=1 · -100.0% [-100.0; -100.0] · CLV – | n=11 · -37.3% [-100.0; +58.6] |
| League One | 12.8% | n=68 · +13.6% [-31.8; +61.0] · CLV -1.4% ±1.4 | n=14 · +31.8% [-53.9; +126.5] · CLV -0.8% ±2.4 | n=7 · +52.9% [-54.3; +195.7] · CLV -1.7% ±4.5 | n=38 · +46.6% [-16.8; +111.5] |
| League Two | 11.0% | n=89 · +4.6% [-31.3; +39.1] · CLV -1.8% ±1.3 | n=10 · -100.0% [-100.0; -100.0] · CLV -2.1% ±2.8 | n=3 · -100.0% [-100.0; -100.0] · CLV -3.6% ±3.8 | n=51 · -2.8% [-41.8; +42.8] |
| National League | 12.5% | n=182 · -3.2% [-28.2; +20.8] · CLV -4.8% ±1.5 | n=83 · -16.8% [-50.7; +20.4] · CLV -4.2% ±2.4 | n=49 · -21.6% [-64.5; +21.8] · CLV -3.1% ±3.6 | n=99 · +3.4% [-33.8; +38.9] |

### 7. Lo scarto iniziale anticipa la direzione?

| Campionato | Correlazione scarto Bet365−exchange Betfair / movimento successivo | Esiti con scarto >2 punti | … in cui exchange Betfair si sposta verso Bet365 |
|---|---|---|---|
| **Tutti** | +0.11 | 1842 | 59% |
| Maggiori (A, Premier) | +0.04 | 316 | 52% |
| Minori (le altre) | +0.12 | 1526 | 61% |
| Serie A | +0.05 | 170 | 55% |
| Serie B | +0.17 | 257 | 63% |
| Premier League | +0.04 | 146 | 48% |
| Championship | +0.04 | 163 | 46% |
| League One | +0.08 | 240 | 60% |
| League Two | +0.12 | 256 | 66% |
| National League | +0.15 | 610 | 61% |

### 8. Discese e salite a confronto

Tutti i campionati:

| Quota exchange Betfair | Esiti | Frequenza reale | Prob. giusta iniziale | Prob. giusta chiusura | ROI Bet365 iniziale | ROI Bet365 chiusura | ROI quota migliore chiusura |
|---|---|---|---|---|---|---|---|
| scesa oltre 10% | 1048 | 33.2% | 27.9% | 32.8% | +4.0% [-5.9; +14.0] | -11.3% [-19.9; -3.1] | -5.2% [-14.4; +4.3] |
| scesa 3-10% | 3877 | 36.7% | 34.6% | 37.1% | -3.5% [-7.7; +0.9] | -9.1% [-13.3; -4.9] | -3.7% [-7.9; +0.8] |
| ferma (±3%) | 8243 | 36.2% | 35.3% | 35.7% | -3.5% [-6.6; -0.6] | -4.3% [-7.5; -1.2] | +0.1% [-2.9; +3.3] |
| salita 3-10% | 5508 | 32.0% | 33.3% | 32.1% | -11.3% [-15.1; -7.4] | -8.5% [-12.2; -4.5] | -3.9% [-7.9; +0.2] |
| salita oltre 10% | 3545 | 25.2% | 29.1% | 25.8% | -21.4% [-25.9; -16.6] | -13.7% [-19.1; -8.6] | -8.5% [-14.5; -3.0] |

Per campionato: frequenza reale meno probabilità giusta di chiusura (punti) e ROI di Bet365 alla chiusura.

| Campionato | scesa oltre 10% | scesa 3-10% | ferma (±3%) | salita 3-10% | salita oltre 10% |
|---|---|---|---|---|---|
| **Tutti** | +0.4 pt · ROI -11% (n=1048) | -0.4 pt · ROI -9% (n=3877) | +0.5 pt · ROI -4% (n=8243) | -0.1 pt · ROI -8% (n=5508) | -0.7 pt · ROI -14% (n=3545) |
| Maggiori (A, Premier) | -1.7 pt · ROI -20% (n=354) | -1.4 pt · ROI -12% (n=1168) | +0.4 pt · ROI -2% (n=2028) | +2.0 pt · ROI -3% (n=1053) | -1.4 pt · ROI -18% (n=518) |
| Minori (le altre) | +1.5 pt · ROI -7% (n=694) | -0.0 pt · ROI -8% (n=2709) | +0.5 pt · ROI -5% (n=6215) | -0.5 pt · ROI -10% (n=4455) | -0.5 pt · ROI -13% (n=3027) |
| Serie A | -3.0 pt · ROI -24% (n=182) | -1.8 pt · ROI -16% (n=596) | +0.6 pt · ROI -4% (n=988) | +2.0 pt · ROI -2% (n=533) | -0.2 pt · ROI -21% (n=278) |
| Serie B | +5.2 pt · ROI +4% (n=87) | +0.8 pt · ROI -6% (n=415) | -0.5 pt · ROI -7% (n=739) | +1.9 pt · ROI -1% (n=524) | -2.2 pt · ROI -18% (n=632) |
| Premier League | -0.3 pt · ROI -16% (n=172) | -0.9 pt · ROI -9% (n=572) | +0.3 pt · ROI +1% (n=1040) | +2.0 pt · ROI -4% (n=520) | -2.9 pt · ROI -14% (n=240) |
| Championship | -1.8 pt · ROI -19% (n=168) | -1.3 pt · ROI -10% (n=756) | +0.1 pt · ROI -6% (n=1702) | +0.6 pt · ROI -6% (n=820) | +1.7 pt · ROI +1% (n=352) |
| League One | +4.1 pt · ROI +4% (n=194) | +1.8 pt · ROI -4% (n=627) | -1.0 pt · ROI -12% (n=1346) | -1.3 pt · ROI -12% (n=992) | +1.5 pt · ROI -7% (n=543) |
| League Two | +0.5 pt · ROI -12% (n=117) | -1.4 pt · ROI -13% (n=509) | +2.0 pt · ROI +2% (n=1423) | -0.9 pt · ROI -11% (n=1136) | -2.1 pt · ROI -18% (n=499) |
| National League | +0.4 pt · ROI -10% (n=128) | +0.5 pt · ROI -6% (n=402) | +1.9 pt · ROI -4% (n=1005) | -1.6 pt · ROI -15% (n=983) | -0.5 pt · ROI -16% (n=1001) |

### 9. Bookmaker lenti

Casi in ritardo: la quota exchange Betfair scende oltre il 5% e il bookmaker fa meno della metà del movimento.

| Bookmaker | Partite | Quanto segue exchange Betfair (1 = tutto) | Casi in ritardo | Vantaggio medio sulla chiusura giusta exchange Betfair | ROI alla sua quota di chiusura |
|---|---|---|---|---|---|
| Bet365 | 7407 | 0.71 | 388 | -5.0% | -17.9% [-31.8; -3.3] |
| bwin | 6210 | 0.64 | 538 | -5.0% | -13.9% [-25.6; -1.7] |
| William Hill | 2576 | 0.47 | 395 | -0.8% | -22.2% [-35.0; -8.6] |
| Betfair sportsbook | 3228 | 0.68 | 160 | -1.4% | -10.6% [-32.8; +11.0] |
| 1xBet | 3176 | 0.68 | 280 | -1.5% | -26.6% [-41.8; -10.3] |
| Betfred | 4166 | 0.64 | 325 | -3.2% | +0.3% [-15.4; +17.1] |
| BetVictor | 4150 | 0.70 | 267 | -3.2% | -3.2% [-20.6; +16.1] |
| Paddy Power | 1135 | 0.83 | 36 | -5.1% | +7.7% [-37.4; +54.2] |
| Sky Bet | 1135 | 0.80 | 82 | -5.4% | -25.7% [-55.6; +6.3] |

| Campionato | Quanto seguono exchange Betfair (media bookmaker) | Casi in ritardo | Vantaggio medio | ROI |
|---|---|---|---|---|
| Serie A | 0.83 | 296 | -4.0% | -29.8% [-45.3; -12.4] |
| Serie B | 0.58 | 219 | -0.4% | -43.4% [-58.5; -28.1] |
| Premier League | 0.85 | 339 | -3.4% | -14.6% [-31.4; +3.3] |
| Championship | 0.85 | 428 | -3.5% | -4.1% [-18.0; +10.2] |
| League One | 0.77 | 366 | -3.4% | -2.4% [-16.4; +12.2] |
| League Two | 0.71 | 372 | -3.8% | -9.9% [-23.4; +3.8] |
| National League | 0.52 | 417 | -3.2% | -10.1% [-23.1; +4.0] |
