---
tipo: Principio
data: 2026-09-14
---

- **Forge: GitHub**, con vincoli di portabilità: decisioni negli ADR, CI come script del repo, nessuna dipendenza da funzioni non esportabili.
- **Repository pubblico da subito, non annunciato**; README con uso personale, nessun supporto, nessuna PR esterna. Storia pubblicabile per costruzione: niente segreti né dati personali.
- **Account `ookmash`**, repo con prefisso:
  - `palfrey`: monorepo con core Rust, server, shell, moduli, documentazione, deploy;
  - `palfrey-spike-*`: un repo usa-e-getta per spike;
  - `palfrey-ops`: privato, quando esisterà un deploy.
- Organization quando i repo esterni saranno più d'uno (`palfrey` come nome è già occupato).
- **Licenza: MPL-2.0.**
- **`CLAUDE.md`** alla radice con le [[Direttive-AI]].
