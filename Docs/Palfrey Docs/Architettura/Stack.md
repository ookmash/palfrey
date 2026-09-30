---
tipo: Riferimento
data: 2026-09-14
---

| Ambito | Scelta | Stato |
|---|---|---|
| Core dati | Rust, nel processo del contenitore: storage, sync, crittografia, portachiavi, motore delle entità, schemi e capability | Deciso |
| Dominio e UI | TypeScript nella webview, in funzioni pure dove possibile | Deciso |
| Client | Tauri 2. Target: Linux, poi Android; iOS non garantito | Direzione decisa · Tauri da spike |
| Storage locale | SQLite con SQLCipher su tutto il database (`rusqlite`, feature `bundled-sqlcipher`) | Deciso · Android da spike |
| Primitive crittografiche | Adottate, mai scritte: AEAD, HPKE, firme, Argon2id da crate di riferimento | Principio deciso · scelta dei crate da design |
| Post-quantum | Requisito per ogni scambio o avvolgimento di chiavi | Vedi [[R5\|Resistenza post-quantum obbligatoria]], [[D10\|Costruzione post-quantum X-Wing in HPKE]] |
| Sync e server | Custom sottile: server che non capisce i dati | Deciso · da design |
| Condivisione tra persone | Portachiavi del proprietario con rotazione alla rimozione | Vedi [[R4\|Rotazione della chiave alla rimozione]], [[D13\|Riferimento pubblico per la rotazione delle chiavi]] |
| CRDT per il testo | Loro o Automerge, come migrazione additiva quando servirà | Aperto |
| Schema comune Rust/TS | formato dichiarativo leggibile da entrambi | Aperto |
| Toolchain TS | Node LTS, pnpm, Vite, React, Tailwind, Radix, i18next, Biome | Proposto |
| Toolchain Rust | stable, rustfmt, clippy, `cargo-deny` | Proposto |
| Test | Rust: `cargo test` e property test. TS: Vitest. End-to-end: `tauri-driver` | Proposto |
