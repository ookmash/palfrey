---
tipo: Storico
data: 2026-09-30
---

Log cronologico di cosa è cambiato, dal più recente. Una voce per sessione in cui è successo qualcosa di rilevante, non per ogni singola modifica — serve a ricostruire "cosa è successo dall'ultima volta" senza confrontare a memoria lo stato di ieri con quello di oggi.

Storia precedente al 30/9/2026: non conservata — i sei documenti originali del progetto sono stati rimossi il 30/9/2026, dopo la migrazione completa nel vault.

## 2026-09-30

- Migrata tutta la documentazione da sei file .md sparsi nella cartella del progetto a questo vault Obsidian, con linking e frontmatter strutturato.
- Prima struttura piatta rivelatasi poco navigabile (troppe note in root, nessun livello intermedio); riorganizzata in cartelle tematiche con nota-guida: Sicurezza, Architettura, Governance, Decisioni, Fonti.
- Le 24 decisioni riformattate nel formato ADR (Contesto/Decisione/Stato/Conseguenze).
- Rimosso Mappa.canvas: richiedeva risincronizzazione manuale a ogni cambio di stato, sostituito da `Registro.base` (auto-aggiornante) e dai backlink automatici già presenti nelle note ADR.
- Roadmap trasformata da nota cumulativa a cartella: 17 passi della sequenza come note atomiche in `Roadmap/Sequenza/`, con `Sequenza.base` come vista tracciabile. Spikes non più cartella root: sono passi della sequenza, non un dominio a sé.
- Dei 7 "punti aperti" originali di vision.md, 6 coincidevano già con un passo della sequenza o con una decisione (documento di design, post-quantum, i due spike Tauri, diario d'uso, v1) e non sono stati duplicati come note a sé; l'unico genuinamente nuovo è diventato [[Mitigazioni-consegna-codice]].
- Valutato il plugin community Kanban per una vista drag-and-drop: scartato perché salva la colonna nella board, non nel frontmatter della nota — avrebbe creato una seconda fonte di verità per lo stato. Le tabelle di `Registro.base`/`Sequenza.base` sono già modificabili cella per cella, senza quel rischio.
- `Registro.base` e `Sequenza.base` spostate dentro le cartelle che descrivono (`Decisioni/`, `Roadmap/Sequenza/`) invece che un livello sopra.
- Passo di deduplicazione: tolte o linkate le ripetizioni tra Architettura.md/Stack.md, Non-obiettivi.md/R2/R8/Shell-e-moduli.md, e nel Glossario; corretto un disallineamento reale tra Architettura.md e [[D6]] sullo stato di LWW/HLC — D6 (Aperto) era la versione corretta.
- Secondo passo di pulizia: tolti i cross-reference periferici o "nudi" a [[M1]]/[[v1]]/R8 dove non erano necessari a capire la nota che li conteneva.
- Criterio esteso a tutte le 24 decisioni e alle ~15 note che le citano; aggiunto un campo `titolo` semantico a ogni decisione e milestone, usato ovunque al posto della sigla nuda (`[[R8|Riferimento pubblico per ogni costrutto crittografico]]` invece di `[[R8]]`). Scritte le regole in [[Direttive-cognitive]].
- Creato `CLAUDE.md` alla radice del repo: punta al vault come guida primaria per chi lavora sul progetto via Claude Code, referenzia Direttive-AI e Direttive-cognitive senza ripeterle.
- Rimossi i sei documenti originali (erano in `archivio/`, fuori dal vault) e tutte le righe "Fonte: ..." che li citavano in fondo alle note — il vault è ora l'unica fonte, senza un livello di provenienza esterno a cui risalire.

### Sessione decisionale

- Sessione di decisione dedicata su [[D11|Modello dei dati tra space]] (passo [[Sessione-decisione-D11|Sessione di decisione dedicata su D11]] della sequenza): ratificate D11, D11.1, D11.2, D11.3; aggiunte [[D11.4|Il contesto attivo assegna lo space ai nuovi elementi]] e [[D11.5|Spazio di una Raccolta ghost]] per chiudere due domande rimaste aperte in [[Space]] senza una D-nota propria. Chiusa di conseguenza [[D8|Chiave di derivazione degli ID ghost]] (per account).
- [[D7|Visibilità lato server di ID e operazioni]]: chiusa la parte sul formato degli ID (UUIDv4, mai v7 — rif. RFC 9562, IETF, mag. 2024); resta da design la parte sulle operazioni visibili al server.
- [[R6|Blob indirizzati per hash del ciphertext]] chiusa: l'indirizzamento per hash del ciphertext è un dettaglio non crittografico, fuori dal perimetro di [[R8|Riferimento pubblico per ogni costrutto crittografico]]; il principio (mai chiave dal plaintext) è verificato su Signal e Tahoe-LAFS.
- [[R7|Cancellazione definitiva del ciphertext]] riqualificata come procedura operativa, non crittografica, e chiusa con il Purge History API di Synapse/Matrix come precedente diretto; sblocca parzialmente [[D9|Autorizzazione dello snapshot e compattazione]] (autorizza il proprietario dello space, meccanica di sync ancora da design).
- [[R3|Autorizzazione dispositivo dalla radice]]: aggiunta una terza pista (BIP-32/BIP-39) per la persistenza zero della radice; verificato e scartato il paper key di Keybase (stessa famiglia del cross-signing Matrix, non una radice privilegiata). Resta Da design, non decisa.
- Nuove note Fonti: [[R6 — indirizzamento del ciphertext]], [[R7 — precedente operativo per la cancellazione]].

### Bootstrap del repository

- Eseguito [[Bootstrap-repository|Bootstrap del repository]] (passo 8): [github.com/ookmash/palfrey](https://github.com/ookmash/palfrey), pubblico, non annunciato, branch di default `main`. Identità dei commit impostata a livello di repository (non globale): `ookmash <ookmash@users.noreply.github.com>`.
- Commit iniziale: vault più scaffold minimo — `LICENSE` (MPL-2.0, testo verificato da mozilla.org, corrispondenza byte-per-byte con la copia SPDX), `README.md`, `.gitignore`, due workflow CI. `.obsidian/` escluso dal repository: `mcp-tools-istefox/data.json` conteneva un bearer token live del transport MCP locale, mai arrivato al commit.
- CI: `vault-links.yml` (controllo link rotti nel vault via `scripts/check_vault_links.py`, testato in positivo e in negativo prima del commit) e `adr-code-separation.yml` (rifiuta una PR che tocca insieme `Decisioni/` e codice, come richiesto da [[Governance]]) — entrambe con `actions/checkout` pinnato al commit esatto, non a un tag mobile. Prima esecuzione reale su GitHub Actions dopo il push: verde.
- Nessun crate Rust o package TS ancora — arrivano con [[Piattaforma-e-primitivi]] insieme al primo codice reale con test, non come scaffolding vuoto anticipato.
