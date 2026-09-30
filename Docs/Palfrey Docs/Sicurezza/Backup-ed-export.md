---
tipo: Principio
data: 2026-09-14
---

- **Backup del server: nessun codice nostro.** Il server tiene già tutto cifrato: backuppare il server è backuppare i dati. Ricetta documentata (snapshot del volume, `restic` o `borg`), non codice. Segmentazione possibile solo per account — il server non vede i concetti applicativi.
- **Export in formati standard, on demand**: portabilità e via di fuga, va provato davvero ogni tanto. Lato client solo un promemoria quando non esporti da troppo tempo.
- Niente backup cifrato automatico dal client: sarebbe una seconda copia dello stesso ciphertext, e la cancellazione accidentale è coperta dal log con tombstone.
