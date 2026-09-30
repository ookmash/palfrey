---
tipo: Principio
data: 2026-09-30
---

Regole su *come* si scrive e organizza questo vault — non su cosa decidere per Palfrey (quello è [[Direttive-AI]]). Nascono da una serie di correzioni fatte insieme il 30/9/2026, dopo che la prima struttura si è rivelata poco sostenibile da seguire. Da rileggere prima di aggiungere o ristrutturare qualcosa qui dentro.

## Un fatto, un posto

Un fatto vive in una sola nota — quella più specifica che lo riguarda. Ovunque altro serva menzionarlo, si linka, non si riscrive. Se un fatto non ha ancora una casa più specifica, può stare temporaneamente in una nota-indice; nel momento in cui una casa più specifica esiste, il fatto si sposta lì e la nota-indice diventa un link.

Eccezione dichiarata: nel glossario e nelle note con decisione "Aperto" o "Non ancora presa", una definizione breve e autosufficiente è il punto della nota, non un difetto — ma deve comunque chiudere con un link alla versione completa.

## Link solo se necessario, mai a sigla nuda

Un cross-reference resta solo se la frase che lo contiene non si capisce senza — non per "a proposito, è collegato a...". Se il link non è necessario a capire la nota, si toglie, non si lascia come contesto periferico.

Quando un link resta, ci devono essere abbastanza parole intorno perché si capisca cosa significa senza cliccare. Mai un codice nudo tipo "vedi R8" — sempre col titolo: `[[R8|Riferimento pubblico per ogni costrutto crittografico]]`.

## Nomi semantici, non solo codici

Ogni decisione, milestone o passo tracciabile ha un campo frontmatter `titolo` in linguaggio semplice, oltre al codice tecnico (`R8`, `M1`...). Il codice resta per compatibilità con vision.md/tecnico.md e per restare corto nelle tabelle; il `titolo` è quello che compare nei link e nelle colonne delle Base — mai il codice nudo in prosa.

## Ogni cartella con più di 2-3 note ha una nota-guida

Stesso nome della cartella, dentro la cartella (`Decisioni/Decisioni.md`, `Sicurezza/Sicurezza.md`...). Spiega cosa rappresenta la cartella e in che ordine leggerla, prima di elencare cosa contiene — mai assumere che il nome della cartella si spieghi da solo.

## Vista live, non copia manuale

Per vedere più note insieme (stato, tema, ordine) si usa una Base — dentro la cartella che descrive, non un livello sopra — mai un Canvas o un plugin che salva uno stato proprio separato dal frontmatter. Una vista che richiede risincronizzazione manuale diventa fuorviante prima o poi; una Base letta dal frontmatter no. Verificato due volte, vedi [[Storico]] (voci su Mappa.canvas e sul plugin Kanban).

## Formato delle decisioni

Ogni nota in `Decisioni/` segue lo schema ADR: Contesto, Decisione, Stato, Conseguenze. Una decisione superata si marca "superseded", non si cancella.

Fa parte di [[Governance]].
