# Palfrey

Suite personale di applicazioni self-hosted, cifrata end-to-end. Dettagli, stato di avanzamento e decisioni tecniche non stanno in questo file: vivono nel vault Obsidian in `Docs/Palfrey Docs/`, che è l'unica fonte per il progetto.

## Prima di lavorare su questo progetto

Apri `Docs/Palfrey Docs/Palfrey.md` — punto di ingresso del vault, linka roadmap, decisioni, architettura, sicurezza, governance.

Leggi sempre, prima di proporre o costruire qualcosa:
- `Docs/Palfrey Docs/Governance/Direttive-AI.md` — le regole su cosa l'AI può decidere e cosa deve solo proporre.
- `Docs/Palfrey Docs/Governance/Direttive-cognitive.md` — come si scrive e si organizza il vault stesso (deduplicazione, quando linkare, nomi semantici, nota-guida per cartella). Vale anche per questo file: non ripetere qui quello che dicono loro, aggiornalo solo se cambia una regola.

## Come leggere e scrivere il vault

Il vault è raggiungibile via MCP (server `obsidian-mcp-connector`, richiede Obsidian Desktop avviato col plugin attivo). Preferiscilo quando disponibile: dà controllo automatico dei link (`find_broken_links`) e gestisce frontmatter/Base/Canvas nel formato giusto. Se Obsidian non è avviato, il vault è comunque solo markdown — leggerlo e modificarlo direttamente da filesystem funziona; dopo una modifica strutturale (rinomina, spostamento), riverifica i link col connettore alla prima occasione.
