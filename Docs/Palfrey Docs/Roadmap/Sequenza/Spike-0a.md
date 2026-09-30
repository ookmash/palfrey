---
tipo: Spike
codice: 0a
ordine: 0
stato: Fatto
data: 2026-09-14
esito: Superato
---

Triage a tavolino dei framework local-first E2EE. Nessun framework rispetta il threat model senza compromessi: Jazz v2 (permessi da server fidato), Classic Jazz (legacy), DXOS (non open source), any-sync (solo Go), p2panda (P2P, relay terzi, messaggi di gruppo in chiaro), Automerge+Keyhive (pre-alpha, senza audit), Evolu/Etebase/NextGraph/Peerbit/SecSync (licenza, servizi terzi, condivisione assente, sviluppo fermo).

Promossi allo spike 0b: prima p2panda poi Automerge+Keyhive; entrambi abbandonati al consolidamento. Riconferma a mano su p2panda con lettura diretta dei sorgenti (non solo riassunti): spazi cifrati non ancora rilasciati nell'API di alto livello, metadati dei gruppi in chiaro, blob non cifrati.

Esito: strada custom sottile in Rust, componenti crittografici adottati. Vedi [[Architettura]].
