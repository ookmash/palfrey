---
tipo: Fonte
per: R6
data: 2026-09-30
---

| Sistema | Chiave | Cosa verifica il digest | Indirizzo di storage |
|---|---|---|---|
| Signal (`Signal-Android`, commit `32f37f3`, 29/9/2026) | Random per allegato, mai dal plaintext (`AttachmentCipherOutputStream`) | SHA-256 sul ciphertext trasmesso (IV+ciphertext+MAC), verificato al download (`AttachmentCipherInputStream`, `MessageDigest.isEqual`) — integrità end-to-end | Assegnato dal server *prima* della cifratura (`AttachmentUploadForm.key`), non derivato dal digest |
| Tahoe-LAFS (`tahoe-lafs`, commit `f002fd0`, 21/1/2026) | Convergente di default (hash del plaintext + segreto locale); random possibile per non-convergenza | Merkle tree separato sui blocchi di ciphertext (`file-encoding.rst`) | Storage Index = hash(chiave), non hash(ciphertext) |
| Etebase (citato in [[R6|Blob indirizzati per hash del ciphertext]]) | — | Hash sul plaintext, con MAC | — |

Lettura per [[R6|Blob indirizzati per hash del ciphertext]]: nessuno dei due sistemi indirizza letteralmente per hash-del-ciphertext. Quello che è solidamente precedentato è il principio sostanziale — mai derivare dal plaintext nulla che il server possa vedere. Tahoe-LAFS nomina esplicitamente l'attacco che questo evita, il *Confirmation-of-a-File Attack* (`docs/convergence-secret.rst`, che rimanda a Drew Perttula's Hack Tahoe-LAFS Hall of Fame entry): chi conosce il segreto di derivazione e possiede una copia del file può verificare se anche tu la possiedi. Con chiave random per file (mai un segreto condiviso, mai il plaintext), questo attacco non si applica: due upload indipendenti dello stesso plaintext producono ciphertext diversi con probabilità schiacciante, quindi "indirizzare per hash del ciphertext" non rivela né abilita alcuna correlazione — è equivalente in sicurezza a un ID casuale, non un costrutto crittografico a sé.
