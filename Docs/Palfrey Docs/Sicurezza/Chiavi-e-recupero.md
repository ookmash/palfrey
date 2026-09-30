---
tipo: Principio
data: 2026-09-14
---

- **Radice**: una frase mnemonica generata sul client, mostrata una sola volta con conferma esplicita di averla salvata. Esportabile come testo o QR (QR opzionalmente protetto da passphrase).
- **Dispositivi**: ogni dispositivo genera le proprie chiavi, autorizzate dalla radice — vedi [[R3|Autorizzazione dispositivo dalla radice]]. La radice non resta in memoria nell'uso quotidiano.
- **Revoca** per singolo dispositivo, con rotazione delle chiavi degli space.
- **Device linking**: il nuovo dispositivo viene autorizzato da uno già autorizzato, ad esempio via QR — vedi [[D3|Canale di device linking]]. È il meccanismo quotidiano; la mnemonic è la rete di sicurezza ultima.
- **Nessun escrow, per costruzione.** Persi mnemonic e tutti i dispositivi, i dati sono irrecuperabili: conseguenza accettata.
- **Protezione locale**: auto-lock dopo inattività, riapertura con passphrase o biometria. Dettagli sulla chiave del database in [[Sicurezza-e-distribuzione]].
