---
tipo: Riferimento
data: 2026-09-14
---

| Termine | Significato |
|---|---|
| Ghost | Entità vera ma sparsa, creata quando si referenzia qualcosa che non esiste ancora. ID derivato dal nome normalizzato con hash a chiave — vedi [[Primitivi]] |
| Promozione | Riempire di dati un ghost mantenendo lo stesso ID |
| Raccolta | Insieme nominato di riferimenti tipizzati. È anche il tag (Raccolta ghost) e la vista (Raccolta attivata come contesto) |
| Contesto attivo | Raccolta selezionata nella shell: i moduli filtrano su di essa e i nuovi elementi le vengono associati |
| Associazione | Riferimento trasversale generico `{tipo, id, metadati}`, con schema dei metadati dichiarato dal modulo proprietario |
| Faccetta | Schema tipizzato opzionale su un File, registrato nel codice |
| Consolidator | Calcolo dello stato derivato dagli eventi, con cache invalidata per hash. Autorità sulla validità degli eventi |
| Stato derivato locale | Consolidator, backlink, indice di ricerca: calcolato, persistito cifrato, mai sincronizzato |
| Upcasting | Conversione in lettura di eventi scritti con versioni di schema precedenti |
| Space | Unità di cifratura e di condivisione — vedi [[Space]] |
| Portachiavi del proprietario | Modello di condivisione in cui l'amministratore di uno space avvolge la chiave per ogni membro e la ruota alla rimozione — vedi [[R4]] |
| Core dati | Parte Rust del client: chiavi, database cifrato, sync, motore delle entità, validazione — vedi [[Stack]] |
| Modulo core | Il modulo che possiede Persona, Luogo, Raccolta, File. Distinto dalla shell |
| Modulo integrato / esterno | Integrato: nel monorepo, per sempre. Esterno: repo separato, isolato |
| M1 / v1 | M1: primo uso quotidiano personale. v1: M1 più condivisione tra persone |
