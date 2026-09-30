---
tipo: Fonte
per: D13
data: 2026-09-14
---

| Sistema | Ruota? | Evidenza |
|---|---|---|
| 1Password | No | 1P Security Design §10, Story 7: policy di server e client, non crittografia |
| Bitwarden | No | `RemoveOrganizationUserCommand` cancella la membership, nessuna operazione sulla chiave (commit `ced49fb`) |
| Etebase | No | `remove` è una semplice DELETE HTTP; nessuna rotazione nei sorgenti di `etebase-rs` |
| Standard Notes (shared vault) | **Sì** | `RotateVaultKey.ts`: nuova radice, nuovo items key, distribuzione ai membri rimasti via messaggio asimmetrico firmato (commit `6fcb991`) |

Lettura per [[D13|Riferimento pubblico per la rotazione delle chiavi]]: 1Password e Bitwarden si affidano alla policy del server — non trasferibile nel threat model di Palfrey, dove il server non è fidato. La rotazione non è una preferenza, è imposta.

Riserve non coperte dal riferimento Standard Notes: rimozione e rotazione non atomiche, la nuova chiave si condivide solo se chi ruota è owner, l'uscita volontaria non ruota, il messaggio di cambio chiave può essere trattenuto dal server.
