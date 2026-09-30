---
tipo: Principio
data: 2026-09-14
---

Quattro minacce, tutte assunte come reali:

1. **Compromissione o furto del server**: accesso a macchina o dischi non rende leggibile nulla.
2. **Me stesso come operatore**: se ospito dati di altri, non devono dover dare fiducia a me. Niente scorciatoie amministrative, niente recupero lato server, niente escrow delle chiavi.
3. **Furto del dispositivo client**: database locale interamente cifrato, auto-lock applicativo, revoca del dispositivo.
4. **Richiesta legale o sequestro**: non essere tecnicamente in grado di consegnare i contenuti.

**Requisito trasversale**: resistenza post-quantum su ogni scambio o avvolgimento di chiavi (harvest-now-decrypt-later). Vedi [[R5|Resistenza post-quantum obbligatoria]] e [[D10|Costruzione post-quantum X-Wing in HPKE]].

## Limiti da non nascondere

- **Metadati**: l'E2EE protegge i contenuti, non chi/quando/quanto. Li tiene solo chi ospita il server — nessuna rete P2P, nessun relay.
- **Grafo della condivisione**: il server conosce i partecipanti di ogni space condiviso.
- **Passphrase sotto coercizione**: nessuna architettura aiuta.
- **Membro rimosso**: conserva i dati già sincronizzati. La rotazione protegge solo i dati successivi.
- **Consegna del codice**: chi controlla il codice eseguito controlla le chiavi — per questo client binario firmato, non servito dal server. Rischio spostato su catena di build e chiave di firma (vedi [[Mitigazioni-consegna-codice]]).
- **Codice crittografico nostro senza audit**: sync e portachiavi seguono design di riferimento pubblici ma non sono auditati; anche le librerie PQ adottate non lo sono. Nessun dato di altri prima di una revisione esterna.
- **XSS nella webview**: mitigazioni obbligatorie in [[Sicurezza-e-distribuzione]].
- **Server compromesso**: non legge, ma può trattenere o cancellare — risposta nel [[Backup-ed-export|backup]].
