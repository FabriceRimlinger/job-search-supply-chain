# Agent Index — Recherche Emploi Supply Chain

Table de routage des 5 agents. Toutes les définitions canoniques vivent dans `agents/prompts/<agent>.md`.

## Routing table

| Agent | Rôle | Déclenchement | Protocole | Commande |
|---|---|---|---|---|
| **JANUS** | Coach & Orchestrateur | Interlocuteur par défaut — actif sans commande (voir `CLAUDE.md`) | `agents/prompts/janus.md` | — (défaut) |
| **AURORA** | Veille & Sourcing | "AURORA, lance la veille" / planifié lun-ven 8h | `agents/prompts/aurora.md` | `/aurora` |
| **VULCAIN** | Personnalisation | "VULCAIN, personnalise ma candidature pour [Entreprise]" | `agents/prompts/vulcain.md` | `/vulcain [Entreprise]` |
| **MINERVE** | Préparation entretien | "MINERVE, prépare l'entretien [Entreprise]" / simulation / debrief | `agents/prompts/minerve.md` | `/minerve [Entreprise]` |
| **FIDES** | Organisation & Suivi | "FIDES, état des candidatures" / planifié lun+jeu | `agents/prompts/fides.md` | `/fides` |

---

## Chaîne de délégation

```
AURORA ──────→ crée dossier (pré-score GO) ──→ notifie VULCAIN
VULCAIN ─────→ score 6D ≥ 45 + relu validé ──→ notifie MINERVE via status.md
FIDES ───────→ statut "Entretien planifié" ───→ notifie MINERVE via status.md
MINERVE ─────→ debrief écrit ─────────────────→ JANUS (boucle feedback → PREP_GENERALE)
FIDES ───────→ pipeline brut ─────────────────→ JANUS (complète FINAL-REPORT)
JANUS ───────→ clôture session ───────────────→ Librarian + Session-Log
```

---

## Points de contact entre agents

| Source | Action | Cible | Fichier impacté |
|---|---|---|---|
| AURORA | Offre qualifiée créée | VULCAIN | `03_CANDIDATURES/*/status.md` (Pré-score AURORA : GO) |
| VULCAIN | Score 6D ≥ 45 + validé manuellement | MINERVE | `03_CANDIDATURES/*/status.md` (bloc Action MINERVE) |
| FIDES | Statut → "Entretien planifié" | MINERVE | `03_CANDIDATURES/*/status.md` (bloc Action MINERVE) |
| MINERVE | Debrief écrit | JANUS | `03_CANDIDATURES/*/status.md §Debrief` → `PREP_GENERALE.md §Leçons actives` |
| FIDES | Exécution bi-hebdo | JANUS | `05_ENTRETIENS/FINAL-REPORT.md` (pipeline brut) |
| JANUS | Clôture session | — | `session-logs/YYYY/MM/` |

---

## Propriété des fichiers

| Fichier | Propriétaire (écriture) | Lecteurs |
|---|---|---|
| `03_CANDIDATURES/*/job_description.md` | AURORA / JANUS (URL express) | VULCAIN, MINERVE |
| `03_CANDIDATURES/*/status.md` | AURORA (création), VULCAIN (docs prêts), FIDES (relances), MINERVE (entretien) | JANUS, tous |
| `03_CANDIDATURES/*/fit_gap.md` | VULCAIN | JANUS, MINERVE |
| `03_CANDIDATURES/*/cv_targeted.md`, `cover_letter.md`, `company_brief.md` | VULCAIN | MINERVE |
| `03_CANDIDATURES/*/PREP_*.md` | MINERVE | Fabrice |
| `05_ENTRETIENS/PREP_GENERALE.md §Leçons actives` | JANUS | MINERVE |
| `05_ENTRETIENS/FINAL-REPORT.md` | FIDES (pipeline) + JANUS (analyse) | Fabrice |
| `02_CIBLES/ENTREPRISES.md` | AURORA + FIDES | JANUS |
| `02_CIBLES/URLS_A_TRAITER.md` | Fabrice (dépôt) / AURORA (vidage) | JANUS (Librarian) |
| `04_RESEAUX/RECRUTEURS.md` | FIDES | FIDES |
| `04_RESEAUX/REFERENCES.md` | JANUS / Fabrice | MINERVE, FIDES |
| `session-logs/` | JANUS | — |
