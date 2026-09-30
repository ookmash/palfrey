---
tipo: Principio
data: 2026-09-14
---

Tre livelli, per evitare che la shell diventi un oggetto-dio:

- **Shell**: runtime e servizi, zero dominio. Sessione e sblocco, registro dei moduli, chrome condiviso (navigazione, selettore del contesto attivo, ingresso della ricerca), servizi di piattaforma.
- **Modulo core**: possiede Persona, Luogo, Raccolta, File. Esiste dal giorno uno.
- **Moduli funzionali**: note/task, calendario, contatti, drive, ledger, vault. Contatti e Drive sono viste ricche su entità del core, non proprietari.

**Moduli integrati** (nel monorepo, per sempre) e **moduli esterni** (repo separati, in futuro). Vincoli da subito: un modulo dipende solo dal contratto pubblico, mai da altri moduli; nessun accesso privilegiato anche per i moduli integrati; capability dichiarate e verificate a runtime dal core; il contratto ha forma di messaggio (asincrono, dati serializzabili, sottoscrizioni).

L'estensibilità verso i moduli esterni si progetta dopo il secondo modulo, estraendola dall'uso reale.

Dettaglio tecnico del contratto: [[Contratto-e-moduli]]. Ordine di costruzione dei moduli: [[App-e-moduli]].
