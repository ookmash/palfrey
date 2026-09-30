---
tipo: Fonte
per: R7
data: 2026-09-30
---

Precedente verificato per [[R7|Cancellazione definitiva del ciphertext]]: Synapse (`element-hq/synapse`, commit `81bc4c8`, 30/9/2026), l'homeserver di riferimento di Matrix.

**Purge History API** (`docs/admin_api/purge_history_api.md`): `POST /_synapse/admin/v1/purge_history/<room_id>[/<event_id>]`, autenticato come admin. Cancella fisicamente dal database gli eventi fino a un punto specificato (per `event_id` o `purge_up_to_ts`); lo stato della stanza (equivalente più vicino a un membership/keyring dello space) è sempre preservato; l'ultimo messaggio non viene mai cancellato. Operazione asincrona con polling dello stato (`purge_history_status`). Il recupero effettivo dello spazio su disco richiede `VACUUM` — la cancellazione logica e la deallocazione fisica sono due passi distinti.

**Message retention policies** (`docs/message_retention_policies.md`, MSC1763): purga automatica basata su `max_lifetime` per stanza, eseguita da job periodici in background — un modello di "snapshot implicito" (lo stato corrente resta, gli eventi scaduti no) analogo a quanto R7 propone per Palfrey.

Lettura per R7: nessun riferimento crittografico esiste perché non serve — cancellare ciphertext già scritto è una procedura operativa (chi autorizza, quando, cosa si preserva), non un costrutto crittografico o un protocollo di gruppo. Synapse mostra la stessa procedura (autorizzazione admin, cancellazione fisica, ricalcolo/preservazione dello stato derivato, deallocazione separata) applicata a un sistema reale con E2EE opzionale sui contenuti. Riserva onesta: Synapse è federato e la cancellazione vale solo sul proprio homeserver — irrilevante per Palfrey, che ha un solo server per definizione ([[R2|Nessun instradamento P2P o di terzi]]).
