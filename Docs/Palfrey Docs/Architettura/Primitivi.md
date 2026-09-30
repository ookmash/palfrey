---
tipo: Principio
data: 2026-09-14
---

Due tipi di primitivo: entità e meccanismi trasversali.

## Entità

| Entità | A cosa serve | Forma di riferimento |
|---|---|---|
| Persona | referenziata da task, eventi, spese | JSContact, RFC 9553 |
| Evento | qualcosa collocato nel tempo | JSCalendar, RFC 8984 |
| Task | cosa da fare, con stato e scadenza | VTODO (RFC 5545) |
| Nota | testo, autonomo o attaccato a qualcosa | VJOURNAL come riferimento per il diario |
| File | allegabile a qualunque cosa | faccette tipizzate |
| Luogo | il dove, accanto al tempo | `Place` di ActivityStreams 2.0 |
| Raccolta | insieme curato di riferimenti | `Collection` di AS2 |

Si implementano solo i campi che servono ai moduli esistenti, mantenendo i nomi degli standard. Un'entità può esistere come primitivo molto prima di avere un'app che la gestisce. Criterio di inclusione nel core: un'entità è core se la usano almeno due app che non si conoscono.

## Meccanismi trasversali

- **Riferimento tipizzato**: il meccanismo più costoso da sbagliare. Due forme: relazioni strutturali (campo tipizzato nello schema) e associazioni trasversali (`{tipo, id, metadati opzionali}`, con metadati tipizzati dichiarati dal modulo proprietario).
- **Raggruppamento**: un solo concetto semantico, la Raccolta. Lo space non è un raggruppamento ma il confine di cifratura — vedi [[Space]].
- **Ghost**: referenziare qualcosa che non esiste crea un'entità vera ma sparsa. ID derivato dal nome normalizzato con hash a chiave, per far convergere le creazioni offline concorrenti senza rivelare i nomi al server. Promozione = riempirla mantenendo lo stesso ID. Serve un percorso di fusione per concetti uguali con nomi diversi.
- **Cancellazione**: il tombstone conserva il nome per default. "Cancella definitivamente" purga anche il nome, con compattazione sul server. "Rimuovi i riferimenti connessi" è best-effort, mai a cascata sulle entità.
- **File e faccette**: nucleo fisso (nome, MIME, dimensione, hash, riferimento al blob) + faccette tipizzate (immagine, audio, documento), schemi concreti nel codice. Nessuna entità Media.
- **Raccolta**: riferimento, non possesso — un'entità può stare in molte raccolte. Manuale per ora, a query in futuro. È anche il tag (Raccolta ghost) e la vista (contesto attivo). Annidamento sì, ereditarietà no — richiederebbe prevenire cicli, impossibile sotto merge offline.
