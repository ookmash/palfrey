---
tipo: Fonte
per: D10
data: 2026-09-14
---

| Crate | Versione | Audit | Test vector |
|---|---|---|---|
| `ml-kem` (RustCrypto) | 0.3.2 | mai auditato (dichiarazione README) | ACVP FIPS203, Wycheproof |
| `x-wing` (RustCrypto) | 0.1.0 | mai auditato | coincidenti con XWING-10 App. C |
| `hpke` (rozbb) | 0.14.1 | nessun audit pagato; revisione interna Cloudflare sulla 0.8 | RFC 9180, test ibridi |
| `hpke-rs` (CE Labs) | 0.7.0 | pre-release dichiarata | non verificato; correzioni VT non confermate |
| `libcrux-ml-kem` | 0.0.10 | verifica formale parziale (hax/F*) | non verificato |

**Nessuna implementazione Rust auditata di X-Wing o HPKE-PQ esiste.** Scatta la regola di [[D10|Costruzione post-quantum X-Wing in HPKE]]: si accetta comunque, a condizioni. La sicurezza classica dell'ibrido richiede che ML-KEM sia C2PRI — non copre bug del combinatore, di X25519 o di HPKE.

Candidati per [[Spike-0c]], non una scelta: `hpke`+`x-wing`+`ml-kem` (X-Wing già integrato in HPKE), oppure `hpke-rs`+`libcrux-ml-kem` (verifica formale ma README fermo alla revisione -06).
