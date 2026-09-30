---
tipo: Principio
data: 2026-09-14
---

- **Sessioni di decisione separate da sessioni di costruzione.** Un ADR nasce `Proposed` in una PR solo documentale e diventa `Accepted` in una sessione successiva; la CI rifiuta PR che toccano insieme ADR e codice.
- **Provenienza**: ogni decisione indica chi l'ha proposta (tu o l'AI) e su cosa è verificata (fonte primaria, codice, spike, nulla).
- **Contraddittorio**: prima di accettare una decisione irreversibile si chiede la migliore argomentazione per l'alternativa scartata.
- **Divisione per reversibilità**: all'AI il reversibile (scaffolding, test, refactor, documentazione, dipendenze, spike); a te l'irreversibile (modello dati, protocollo, crittografia, cosa non costruire).
- **Verifica eseguibile obbligatoria**: niente entra senza un test che fallisce se la cosa è rotta a runtime.
- **"Done" include cancellare**: ogni sessione finisce verde e integrata, oppure eliminata.
- **Flusso trunk-based**: l'AI apre PR; il merge lo fai tu, con CI verde.
- **Dipendenze**: lockfile, versioni esatte, aggiornamenti raggruppati; crittografia e sync con gate manuale.
- Tempi e ordine di costruzione li decidi tu, caso per caso.

**Nota di audit (2026-09-26)**: [[D10|Costruzione post-quantum X-Wing in HPKE]] e [[D13|Riferimento pubblico per la rotazione delle chiavi]] sono state proposte e accettate nella stessa sessione, contro la raccomandazione AI di un raffreddamento — l'unica deroga finora, capitata proprio sulle due decisioni crittografiche.

## In questa cartella

- [[Direttive-AI]] — le 8 regole che l'AI segue a ogni sessione, da rileggere spesso.
- [[Direttive-cognitive]] — come si scrive e organizza questo vault: dedup, link, nomi, nota-guida per cartella.
- [[Repository-e-forge]] — dove vive il codice, licenza, convenzioni dei repository.
- [[Non-obiettivi]] — cosa è deciso di *non* fare, da non riproporre senza un argomento nuovo.
