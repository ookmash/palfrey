---
tipo: Spike
codice: 0b
ordine: 5
stato: Da fare
data:
esito:
---

Prototipo custom, diviso in due timebox dopo revisione: **0b-1** (~12h, un client + server: B1 chiavi/dati a riposo, B2 WebKitGTK, B3 server che non legge — prerequisito [[D1|Formato della busta e versionamento]], [[D5|Autenticazione e log append-only del server]]) e **0b-2** (~12h, due client: B5 merge LWW concorrente, B6 dispositivi/revoca — prerequisito [[D2|Gerarchia delle chiavi L0–L4]], [[D3|Canale di device linking]], [[D6|Risoluzione delle scritture concorrenti]]).

Criteri di stop: serve una primitiva scritta a mano, oppure il timebox scade senza B1 e B3 verdi. Prerequisito generale: [[Documento-design-sync-v0|documento di design palfrey-sync v0]].
