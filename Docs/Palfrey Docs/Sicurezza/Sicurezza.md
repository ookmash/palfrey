---
tipo: Hub
data: 2026-09-30
---

Cosa deve reggere Palfrey se il server è compromesso, il dispositivo viene rubato, o arriva una richiesta legale — e cosa succede in pratica alle chiavi, ai backup e al codice distribuito. Quattro note, lette in quest'ordine se è la prima volta:

1. [[Threat-model]] — le minacce assunte come reali, e i limiti dichiarati apertamente: cosa la crittografia *non* risolve (metadati, grafo di condivisione, coercizione).
2. [[Chiavi-e-recupero]] — la mnemonic radice, le chiavi per dispositivo, cosa succede se perdi tutto (nessun recupero, per scelta).
3. [[Backup-ed-export]] — perché il backup del server non è codice nostro, e cosa esportare a mano per restare al sicuro da un fornitore che sparisce.
4. [[Sicurezza-e-distribuzione]] — come sono protetti i dati sul dispositivo (SQLCipher, keystore) e come viene firmato e distribuito il codice stesso.

Decisioni collegate: [[R3|Autorizzazione dispositivo dalla radice]] · [[D3|Canale di device linking]] · [[R5|Resistenza post-quantum obbligatoria]] · [[D10|Costruzione post-quantum X-Wing in HPKE]].

Fa parte di [[Palfrey]].
