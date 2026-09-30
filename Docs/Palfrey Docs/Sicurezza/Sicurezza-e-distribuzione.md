---
tipo: Riferimento
data: 2026-09-14
---

## Sblocco e dati a riposo

Tutto il database locale è cifrato con SQLCipher. La chiave del database è avvolta da:

| Piattaforma | Protezione della chiave del database |
|---|---|
| Android | Android Keystore (supporto hardware, per app, sblocco biometrico) |
| Linux | Secret Service **più** una chiave derivata con Argon2id dalla passphrase di sblocco: il Secret Service da solo è leggibile da ogni processo dell'utente. FIDO2 `hmac-secret` come opzione futura |
| Windows, macOS | se e quando |

Da verificare: plugin Tauri per il keystore di sistema, comportamento di SQLCipher su Android.

## Dati in chiaro fuori dal database

| Superficie | Regola |
|---|---|
| Storage e cache della webview | mai `localStorage`, IndexedDB o cache HTTP per i dati; tutto dal contratto |
| Log e tracing del core | mai contenuti né identificatori in chiaro |
| File temporanei | cartella dedicata, pulizia alla chiusura, avviso esplicito |
| Crash dump e swap | crash report senza memoria del processo; swap cifrato è responsabilità del SO |
| Appunti | pulizia a tempo per i contenuti copiati dal vault |
| Anteprime del sistema operativo | su Android `FLAG_SECURE` sulle schermate sensibili |

## Consegna del codice

Binari firmati su GitHub Releases; updater di Tauri con verifica della firma, aggiornamento con conferma esplicita. **La chiave di firma degli aggiornamenti è il segreto più critico del progetto**: custodita offline, firma delle release in locale. APK Android firmato, installato a mano, stessa custodia. Catena di fornitura: lockfile, versioni esatte, `cargo-deny` in CI, aggiornamenti di crate crittografici e di sync con gate manuale.

Vedi [[Roadmap]], punto aperto 5.
