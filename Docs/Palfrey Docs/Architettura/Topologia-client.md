---
tipo: Riferimento
data: 2026-09-14
---

Webview (WebKitGTK / Android System WebView) parla col processo Rust (Tauri) tramite comandi ed eventi — contratto trasportabile, dettaglio in [[Contratto-e-moduli]].

Conseguenze:

- **Chiavi e chiave del database non entrano mai nella webview.** L'auto-lock chiude il database e azzera il materiale in memoria nel processo Rust.
- **La webview riceve dati decifrati** solo su richiesta o sottoscrizione, entro le capability del modulo. Un XSS nella webview può quindi leggere ciò che il contratto espone. Requisiti: CSP stretta, permessi Tauri ridotti ai soli comandi del contratto, rendering sanitizzato di markdown/SVG/file importati.
- **Finestra singola**: nessun problema di coordinamento tra più tab.
- **Lavoro pesante**: thumbnail, OCR, indice full-text (FTS5 dentro SQLCipher) nel core Rust; calcoli di dominio TS in un Web Worker, caso per caso.
- **Stato derivato del dominio TS** (consolidator, backlink): calcolato in TS, persistito tramite il contratto dentro SQLCipher, mai sincronizzato. Da misurare nello spike: il ricalcolo passa gli eventi dal core alla webview, e per il ledger con anni di dati il costo può pesare.
