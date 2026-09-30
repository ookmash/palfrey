---
tipo: Principio
data: 2026-09-14
---

- **Client unico, moduli caricati on demand.** Un solo sblocco, una sola sessione: niente single sign-on, niente riferimenti tra domini di cifratura separati.
- **Client nativo firmato**, da verificare — vedi [[Spike-0b]] e [[Spike-1]]. Scelta tecnologica in [[Stack]]. Il browser è solo ambiente di sviluppo e test.
- **Separazione core/webview** (scelta tecnologica in [[Stack]]): la webview riceve dati decifrati solo su richiesta, entro le capability del modulo — le chiavi non entrano mai nella webview. Dettaglio: [[Topologia-client]].
- **Server che non capisce i dati.** Log append-only cifrato per space, blob cifrati, autenticazione a firma. Self-hosted, unico punto di contatto di rete — vedi [[R1|Server vede solo metadati]], [[R2|Nessun instradamento P2P o di terzi]].
- **Sync e crittografia: custom sottile, componenti adottati** (dettaglio in [[Stack]]) — sempre seguendo design di riferimento pubblici. Nessun framework esistente rispetta il threat model senza compromessi: vedi [[Spike-0a]].
- **Condivisione tra persone: portachiavi del proprietario** — vedi [[R4|Rotazione della chiave alla rimozione]], [[D13|Riferimento pubblico per la rotazione delle chiavi]], [[D4|Invito, ruoli e rimozione nella condivisione]].
- **I file sono un primitivo di piattaforma**, non una feature del modulo drive: blob cifrati con chiave per file, indirizzati per hash del ciphertext — vedi [[R6|Blob indirizzati per hash del ciphertext]].
- **Dati come log di eventi append-only, più consolidator.** I fatti sono eventi immutabili; una correzione è un nuovo evento. Come si risolvono le scritture concorrenti — LWW per campo? orologio logico ibrido? copie di conflitto sul corpo delle note? — non è ancora deciso: vedi [[D6|Risoluzione delle scritture concorrenti]].
- **Stato derivato locale** (consolidator, backlink, indice di ricerca): persistito cifrato, mai sincronizzato, invalidato per hash degli eventi.
- **Evoluzione dello schema**: ogni evento porta la propria versione, i lettori convertono al volo (upcasting). Nessuna riscrittura massiva.
- **Validazione**: il core applica sempre schema e permessi, i moduli le regole di dominio; il consolidator resta l'autorità e tollera eventi non validi. Dettaglio: [[Contratto-e-moduli]].
- **Notifiche**: schedulazione locale, nessun orario consegnato al server.
- **Ricerca**: per modulo finché non esiste il secondo modulo.
- **Primo avvio**: server richiesto, nessuna modalità solo-locale.

## In questa cartella

- [[Stack]] — le scelte tecnologiche concrete, cosa è deciso e cosa no.
- [[Topologia-client]] — cosa può fare la webview e cosa resta solo nel core Rust.
- [[Shell-e-moduli]] — i tre livelli (shell, modulo core, moduli funzionali) e i vincoli tra moduli.
- [[App-e-moduli]] — ordine di costruzione dei moduli e confini accettati.
- [[Primitivi]] — le entità (Persona, Task, Nota...) e i meccanismi trasversali (riferimento, raggruppamento, ghost).
- [[Space]] — l'unità di cifratura e condivisione, e le domande ancora aperte.
- [[Contratto-e-moduli]] — come scrivono i moduli, chi valida, cosa può rompersi.
