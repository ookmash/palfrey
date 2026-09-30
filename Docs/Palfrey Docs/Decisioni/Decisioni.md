---
tipo: Hub
data: 2026-09-30
---

Una nota per ogni requisito (**R**) o domanda di design (**D**) verificabile — non prosa libera, un record con lo stesso schema per tutti: `codice`, `tema`, `stato`, `data`, `proposto_da`, `verificato_su`.

## Stato

- **Deciso** — accettata, in vigore.
- **Proposto** — scritta, in attesa di una sessione di decisione dedicata (vedi [[Governance]]).
- **Da design** — il problema è chiaro, la soluzione no.
- **Da spike** — serve un esperimento tecnico prima di poter decidere: vedi [[Spikes]].
- **Aperto** — nemmeno il problema è chiuso.

## Formato

Ogni nota segue lo schema ADR (Architecture Decision Record): Contesto, Decisione, Stato, Conseguenze. Se una decisione ne supera un'altra, la vecchia resta e viene marcata superseded — non si cancella mai una decisione presa.

## Come guardarle tutte insieme

`Registro.base`, in questa cartella: tabella filtrabile e ordinabile per tema o stato, modificabile direttamente in cella.

Fa parte di [[Palfrey]].
