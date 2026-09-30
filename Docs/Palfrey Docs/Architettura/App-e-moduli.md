---
tipo: Principio
data: 2026-09-14
---

## Ordine di costruzione

1. **Piattaforma e primitivi**: core dati, sync, portachiavi, entità, riferimenti, raccolte, file.
2. **Note e Task** (M1): un modulo con due viste, traiettoria di lungo periodo verso un'app note stile Obsidian.
3. **Condivisione tra persone** (chiude la v1).
4. **Calendario**: porta tempo e ricorrenza.
5. **Contatti**: app completa.
6. **Drive**: vista sui file.

Contatti e calendario prendono valore dall'integrazione col sistema operativo, rimandata.

## Moduli di dominio

- **ledger**, dopo le app core. Traguardo: parità con Oinkoin (conti, categorie, tag, ricorrenze, budget, multi-valuta, trasferimenti) più divisione spese stile Cospend. Migrazione da Oinkoin a mano. Il suo orizzonte si allontana — va riletto ogni volta che si valuta l'avanzamento.
- **vault**, dopo le app core. Tre avvertenze: postura di sicurezza propria (sblocco separato, timeout aggressivi, igiene della clipboard); utilità legata all'autofill di sistema (plugin nativo Android, iOS non coperto); alternativa matura da battere (Vaultwarden con i client Bitwarden).

Previste, senza ordine: diario, food log, tracker di abitudini.

## Confini noti e accettati

- **iOS non garantito**: l'uso da iPhone non è coperto.
- **WebKitGTK** su Linux è la webview più fragile, ed è il target primario.
- **Integrazioni di sistema** (autofill, rubrica, calendario, file provider): plugin nativi del client, fuori dalle priorità.
- Con l'E2EE il server non fa ricerca, thumbnail, dedup, transcodifica o antivirus: compromesso scelto.
