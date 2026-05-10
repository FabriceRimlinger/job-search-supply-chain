# Agent Index — Recherche Emploi Supply Chain

Table de routage des 5 agents. Toutes les définitions canoniques vivent dans `agents/prompts/<agent>.md`.

## Routing table

| Agent | Rôle | Déclenchement | Protocole | Commande |
|---|---|---|---|---|
| **JANUS** | Coach & Orchestrateur | "JANUS, fais le point" / tout contexte de coordination | `agents/prompts/janus.md` | `/janus [args]` |
| **AURORA** | Veille & Sourcing | "AURORA, lance la veille" / planifié lun–ven 8h | `agents/prompts/aurora.md` | `/aurora` |
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
| MINERVE | Debrief écrit | JANUS | `05_ENTRETIENS/DEBRIEFS.md` → `PREP_GENERALE.md §Leçons actives` |
| FIDES | Exécution bi-hebdo | JANUS | `05_ENTRETIENS/FINAL-REPORT.md` (pipeline brut) |
| JANUS | Clôture session | — | `session-logs/YYYY/MM/` |

---

## État de cohérence post-consolidation (2026-05-10)

### Divergences détectées et corrigées

**VULCAIN** — deux définitions en conflit :
- `.claude/commands/vulcain.md` avait la "Checklist voix humaine" et le "Format du hook 3 lignes" avec exemple Alloga
- `agents/prompts/vulcain.md` avait la règle de pondération temporelle, les règles format ATS, et la logique PAPI_PROFIL — absentes des commandes
- Résolution : `agents/prompts/vulcain.md` = SSOT ; le hook 3 lignes + exemple Alloga y ont été ajoutés ; la commande est devenue un pointeur

**MINERVE** — deux checklists d'intégrité divergentes :
- Commande : 5 items axés sur l'intégrité factuelle (secteurs clients non attestés, certifications inventées, [LACUNE], mélange d'expériences)
- `agents/prompts/minerve.md` : 5 items axés sur la qualité de préparation (calibration niveau, fit_gap, négociation)
- Résolution : checklist fusionnée à 8 items dans `agents/prompts/minerve.md` — intégrité factuelle + qualité préparation

**AURORA** — règles dans `CLAUDE.md` absentes de la commande :
- Anti-doublon renforcé (> 70% mots en commun), pré-score express obligatoire, règle page multi-offres, URLs manuelles — présents dans `CLAUDE.md §AURORA`, absents de `.claude/commands/aurora.md`
- Résolution : `agents/prompts/aurora.md` créé avec l'ensemble des règles ; commande = pointeur

**FIDES** — règles dans `CLAUDE.md` absentes de la commande :
- Transitions automatiques (> 7j, > 30j, statut → "Entretien planifié"), escalade vers JANUS, responsabilité FINAL-REPORT — dans `CLAUDE.md §FIDES`, absents de `.claude/commands/fides.md`
- Résolution : `agents/prompts/fides.md` créé avec toutes les règles ; commande = pointeur

### Interactions inter-agents non documentées — maintenant formalisées

| Interaction | Était documentée | Maintenant dans |
|---|---|---|
| VULCAIN → MINERVE (score 6D ≥ 45 + validé) | Dans `agents/prompts/vulcain.md` step 7 uniquement | `agent-index.md §Chaîne`, `agents/prompts/vulcain.md` |
| FIDES → MINERVE (statut "Entretien planifié") | Dans `CLAUDE.md §FIDES` uniquement | `agent-index.md §Chaîne`, `agents/prompts/fides.md` |
| MINERVE → JANUS (boucle debrief → leçons actives) | Dans `CLAUDE.md §JANUS` uniquement | `agent-index.md §Chaîne`, `agents/prompts/janus.md §Boucle feedback` |
| FIDES → JANUS (pipeline brut → FINAL-REPORT) | Dans `CLAUDE.md §FIDES` uniquement | `agent-index.md §Points de contact`, `agents/prompts/fides.md` |
| JANUS Librarian (contrôle structurel) | Absent | `agents/prompts/janus.md §Duty 2` |
| JANUS Session-Log Author | Absent | `agents/prompts/janus.md §Duty 3`, `session-logs/` |

---

## Propriété des fichiers

| Fichier | Propriétaire (écriture) | Lecteurs |
|---|---|---|
| `03_CANDIDATURES/*/job_description.md` | AURORA / JANUS (URL express) | VULCAIN, MINERVE |
| `03_CANDIDATURES/*/status.md` | AURORA (création), VULCAIN (docs prêts), FIDES (relances), MINERVE (entretien) | JANUS, tous |
| `03_CANDIDATURES/*/fit_gap.md` | VULCAIN | JANUS, MINERVE |
| `03_CANDIDATURES/*/cv_targeted.md`, `cover_letter.md`, `company_brief.md` | VULCAIN | MINERVE |
| `05_ENTRETIENS/PREP_*.md` | MINERVE | Fabrice |
| `05_ENTRETIENS/DEBRIEFS.md` | MINERVE | JANUS |
| `05_ENTRETIENS/PREP_GENERALE.md §Leçons actives` | JANUS | MINERVE |
| `05_ENTRETIENS/FINAL-REPORT.md` | FIDES (pipeline) + JANUS (analyse) | Fabrice |
| `02_CIBLES/ENTREPRISES.md` | AURORA + FIDES | JANUS |
| `02_CIBLES/URLS_A_TRAITER.md` | Fabrice (dépôt) / AURORA (vidage) | JANUS (Librarian) |
| `04_RESEAUX/RECRUTEURS.md` | FIDES | FIDES |
| `session-logs/` | JANUS | — |
