# Variazioni di quota: piano

Obiettivo: seguire le quote di Serie A, B, C, Premier League, Championship, League One e League Two su più
bookmaker e sull'exchange Betfair. Si studiano le variazioni in entrambi i versi, le loro cause, le proiezioni
della quota di chiusura e i bookmaker che reagiscono in ritardo. Solo se l'analisi lo giustifica si arriva a
giocate reali con il conto dell'utente, entro un budget fissato.

Risultati man mano in [`RISULTATI.md`](RISULTATI.md).

| Fase | Cosa | Stato |
|---|---|---|
| 1 | Analisi sui dati storici gratuiti | fatta |
| 2 | Verifica delle fonti dal vivo (API, Betfair.it, bookmaker italiani) | serve chiavi e conto dell'utente |
| 3 | Proposta di architettura | dopo la fase 2, da approvare |
| 4 | Raccolta e analisi: **solo osservazione, nessuna giocata** | vedi calendario |
| 5 | Giocate reali entro un budget | solo se la fase 4 dà esito positivo |

## Quanto deve durare l'analisi (fase 4)

Il giudizio si dà sul **CLV** (quanto la quota presa batte la quota giusta di chiusura), non sul guadagno.

- Sui dati storici il CLV di una giocata varia di circa ±12 punti. Per stimarlo con un margine di ±1 punto
  servono circa **600 giocate simulate**.
- Stimare il ROI con un margine di ±3 punti richiederebbe circa **19.000 giocate**: le occasioni trovate hanno
  quote medie alte (5-6), e con quote così il risultato è molto rumoroso. Anni di raccolta, quindi il ROI non
  può essere il criterio.

Le giocate simulate si contano solo dopo aver congelato le regole, così non si giudica una regola sugli stessi
dati con cui la si è costruita. Calendario, con raccolta a partire da metà dicembre:

1. **Settimane 1-8, metà dicembre-metà febbraio: misura e costruzione.**
   - ritardi dei bookmaker, durata delle finestre, frequenza delle occasioni;
   - movimenti in entrambi i versi, cause (volumi, formazioni);
   - si scrivono le regole: soglie e proiezioni.

   Il periodo comprende il calendario fitto di Natale in Inghilterra e il mercato di gennaio.
2. **Regole congelate.** Da qui il sistema registra le giocate che farebbe, senza giocare.
3. **Settimane 9-20 circa, metà febbraio-inizio maggio: verifica fuori campione.** Si va avanti finché ci sono
   almeno 600 giocate simulate. La data dipende da quante occasioni si trovano: con circa 100 partite a settimana
   nei 7 campionati, servono almeno 50 occasioni a settimana per chiudere a maggio.
4. **Verdetto.** Si passa alla fase 5 solo se:
   - il CLV è positivo in modo netto, cioè il margine d'errore non tocca lo zero;
   - è positivo in entrambe le metà del periodo di verifica;
   - l'occasione resta aperta abbastanza a lungo da poter essere presa davvero.

Le ultime giornate di campionato hanno dinamiche proprie (squadre senza obiettivi), quindi si leggono a parte.
Se il verdetto arriva a maggio, le giocate reali partono con la stagione 2027-28.

## Fase 5: giocate reali entro un budget (bozza)

**Dove si gioca in automatico.** Solo sull'**exchange Betfair.it**. L'API ufficiale permette di piazzare
scommesse con il proprio conto, per uso personale, e l'exchange non limita chi vince. È il canale adatto alle
proiezioni, cioè prendere la quota prima che si muova.

**Sui bookmaker italiani niente automatismi.** Bet365, Snai, Sisal e gli altri non offrono API per giocare.
Automatizzare le giocate dalle loro pagine viola i termini d'uso e porta alla chiusura del conto, anche con le
vincite dentro. Inoltre i bookmaker limitano rapidamente chi batte la chiusura. Per loro:
- il sistema manda un avviso con partita, esito, quota minima e importo;
- la giocata la fa l'utente.

**Budget e protezioni, scritti nel codice e non modificabili dall'automatismo:**
- conto dedicato con budget fissato; la cifra la decide l'utente;
- importo per giocata piccolo e fisso: 1-2% del budget, o una frazione di Kelly con un tetto;
- limite di perdita giornaliero e settimanale, superato il quale il sistema si ferma da solo;
- arresto automatico se il CLV reale delle ultime 100 giocate scende sotto zero;
- prime settimane in modalità prova, che calcola tutto ma non piazza nulla;
- registro di ogni giocata con motivo, quota presa, quota di chiusura ed esito;
- pulsante di arresto immediato;
- come rete di sicurezza esterna, i limiti di deposito del conto previsti dalle regole ADM.
