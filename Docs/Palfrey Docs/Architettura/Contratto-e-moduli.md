---
tipo: Riferimento
data: 2026-09-14
---

## Contratto trasportabile

L'API dei moduli ha la forma di un messaggio, anche quando il trasporto è una chiamata diretta: asincrona, dati serializzabili, entità riferite per `{tipo, id}`, reattività via sottoscrizioni. Oggi il trasporto è comandi ed eventi Tauri; per i moduli esterni futuri sarà `postMessage` da un iframe sandboxed. La forma non cambia.

## Scritture e validazione

Ogni scrittura passa dal core Rust, che applica sempre schema dichiarativo e capability prima di toccare lo storage. Le regole di dominio non esprimibili in uno schema le applica il modulo prima di chiamare la scrittura — sono una guardia che dà feedback immediato, non un'autorità.

**Il consolidator è l'autorità** ed è tollerante per costruzione: un evento non valido arriva comunque in tre casi — invarianti tra entità violati dal merge di scritture offline concorrenti, eventi arrivati dalla sync scritti da versioni diverse del client, un client alterato che possiede le chiavi. La regola con cui si risolve un evento non valido dev'essere deterministica, altrimenti i dispositivi divergono.

## Capability e proprietà dei tipi

Ogni tipo ha il namespace del modulo proprietario (`core/Persona`, `notes/Task`). Un manifest minimo per modulo dichiara i tipi posseduti e le operazioni richieste. Le capability sono verificate a runtime dal core anche per i moduli integrati — ma senza isolamento dei moduli, questo verifica solo un'identità **dichiarata**: intercetta bug e collauda il contratto, non è una barriera di sicurezza né crittografica.

## Estensibilità

Congelata fino al secondo modulo, come da [[Non-obiettivi]]. Unica nota da non perdere: i moduli esterni gireranno in un iframe `sandbox` senza `allow-same-origin`.
