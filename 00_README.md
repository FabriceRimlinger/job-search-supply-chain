# Recherche Emploi Supply Chain

Projet de pilotage de la recherche d'emploi de Fabrice Rimlinger en supply chain, orchestré par une équipe de 5 agents IA spécialisés.

## Les 5 agents

| Agent | Rôle | Commande |
| --- | --- | --- |
| **JANUS** | Coach & Orchestrateur — actif par défaut | — |
| **AURORA** | Veille & Sourcing d'offres | `/aurora` |
| **VULCAIN** | Personnalisation CV / lettre / fit-gap | `/vulcain` |
| **MINERVE** | Préparation entretiens | `/minerve` |
| **FIDES** | Suivi pipeline & relances | `/fides` |

Protocoles complets : `agents/prompts/<agent>.md` — table de routage : `agent-index.md`

---

## Structure du projet

```
Recherche Emploi Supply Chain/
├── 00_README.md
├── CLAUDE.md                        # Instructions agents (source de vérité)
├── agent-index.md                   # Routing table + propriété des fichiers
├── janus.html                       # Dashboard web local (localhost:8765)
│
├── 01_PROFIL/
│   ├── CV_MASTER.md                 # CV source unique
│   ├── BIO_EXECUTIVE.md             # Pitch exécutif 1 page
│   ├── REALISATIONS.md              # 10 réalisations chiffrées
│   ├── CRITERES_CIBLES.md           # Critères go/no-go
│   └── PAPI_PROFIL.md               # Profil de personnalité PAPI-I
│
├── 02_CIBLES/
│   ├── ENTREPRISES.md               # Pipeline cibles entreprises
│   ├── POSTES_IDEAUX.md             # Profils de poste ciblés
│   └── URLS_A_TRAITER.md            # Backlog URLs AURORA
│
├── 03_CANDIDATURES/
│   ├── TEMPLATE/                    # Modèle dossier candidature
│   └── <Entreprise>_<Poste>_YYYY-MM/
│       ├── job_description.md
│       ├── company_brief.md
│       ├── fit_gap.md
│       ├── cv_targeted.md
│       ├── cover_letter.md
│       ├── status.md                # Statut + debrief entretien(s)
│       └── PREP_<Entreprise>_YYYY-MM-DD.md   # Fiche entretien (MINERVE)
│
├── 04_RESEAUX/
│   ├── RECRUTEURS.md                # Contacts recruteurs
│   ├── REFERENCES.md                # Références professionnelles
│   └── MESSAGES_MODELE.md           # Templates LinkedIn/email
│
├── 05_ENTRETIENS/
│   ├── PREP_GENERALE.md             # Leçons actives + questions types
│   └── FINAL-REPORT.md              # Rapport hebdomadaire pipeline
│
├── INPUT/
│   ├── raw/                         # Déposer CV/bilan à intégrer ici
│   └── processed/                   # Fichiers traités par JANUS
│
├── session-logs/YYYY/MM/            # Logs de session JANUS
└── 99_ARCHIVES/                     # Dossiers candidatures fermées
```

---

## Workflow

### 1. Profil central
`01_PROFIL/CV_MASTER.md` est la source unique. Tous les documents de candidature en sont extraits — jamais modifiés directement.

Pour intégrer un nouveau CV ou bilan : déposer dans `INPUT/raw/` puis demander à JANUS de construire le profil.

### 2. Sourcer les offres — AURORA

- Veille automatique lun-ven
- Dépôt manuel d'URLs dans `02_CIBLES/URLS_A_TRAITER.md`
- AURORA qualifie, crée le dossier dans `03_CANDIDATURES/`, met à jour `ENTREPRISES.md`

### 3. Personnaliser — VULCAIN

- Score fit 6D (score/60)
- Produit `cv_targeted.md`, `cover_letter.md`, `fit_gap.md`, `company_brief.md`
- Si score ≥ 45 + validé manuellement : notifie MINERVE

### 4. Suivre — FIDES

- Dashboard pipeline bi-hebdomadaire (lun + jeu)
- Relances automatiques (max 2)
- Brouillons Gmail
- Alimente `05_ENTRETIENS/FINAL-REPORT.md` (pipeline brut — JANUS complète l'analyse)

### 5. Préparer les entretiens — MINERVE

- Fiche `PREP_<Entreprise>_YYYY-MM-DD.md` dans le dossier candidature
- Simulation d'entretien
- Debrief → section `## Debrief entretien` dans `status.md` → JANUS met à jour `PREP_GENERALE.md §Leçons actives`

### 6. Orchestrer — JANUS

- Interlocuteur par défaut à chaque session
- Librarian : contrôle structurel à chaque clôture
- Session-log : `session-logs/YYYY/MM/YYYY-MM-DD-HH-MM_JANUS_<slug>.md`
- Commande `/close-session` pour clôturer

---

## Statuts valides

`À traiter` | `Documents prêts` | `Envoyée` | `À relancer` | `Entretien planifié` | `Entretien préparé` | `Entretien passé` | `Refusée` | `Abandonnée` | `Gagnée`
