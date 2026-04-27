# Recherche Emploi Supply Chain

Ce projet est conçu pour piloter ta recherche d'emploi en supply chain avec une organisation claire, des agents dédiés et un workflow réutilisable.

## Objectif

Permettre la gestion complète du cycle de candidature :
- sourcing des offres
- qualification des cibles
- personnalisation des documents
- suivi des candidatures
- préparation des entretiens

## Structure du projet

```
Recherche Emploi Supply Chain/
├── 00_README.md                 # Index + workflow
├── 01_PROFIL/
│   ├── CV_MASTER.md             # CV source unique
│   ├── BIO_EXECUTIVE.md         # Pitch 1 page
│   ├── REALISATIONS.md          # 10 bullet points clés
│   └── CRITERES_CIBLES.md       # Go/no-go
├── 02_CIBLES/
│   ├── ENTREPRISES.md           # Tableau cibles
│   └── POSTES_IDEAUX.md         # Job descriptions types
├── 03_CANDIDATURES/
│   ├── TEMPLATE/                # Modèle pour nouvelles
│   │   ├── job_description.md
│   │   ├── cv_targeted.md
│   │   └── cover_letter.md
│   └── Vinted_2026-04/          # Exemple avec vos candidatures
│       ├── job_description.md
│       ├── company_brief.md
│       ├── fit_gap.md
│       ├── cv_vinted.md
│       ├── lm_vinted.md
│       └── status.md
├── 04_RESEAUX/
│   ├── RECRUTEURS.md            # Tableau contacts
│   └── MESSAGES_MODELE.md       # Templates LinkedIn/email
├── 05_ENTRETIENS/
│   ├── PREP_GENERALE.md         # Questions communes
│   └── DEBRIEFS.md              # Notes post-entretien
├── 06_MARCHE/
│   └── SYNTHESE_LOGISTIQUE.md   # Tendances, salaires
└── 99_ARCHIVES/
    └── README.md               # Archive des dossiers fermés
```

## Workflow agent

### 1. Préparer le profil central

Fais de `01_PROFIL/CV_MASTER.md` ton CV source unique. Ce document contient toutes tes expériences, compétences et réalisations.

- `BIO_EXECUTIVE.md` : présentation courte et percutante
- `REALISATIONS.md` : 10 réalisations impactantes en supply chain
- `CRITERES_CIBLES.md` : impératifs de recherche (localisation, type de contrat, salaire, culture d'entreprise, ...)

### 2. Qualifier le marché et les cibles

- `02_CIBLES/ENTREPRISES.md` : liste des entreprises prioritaires
- `02_CIBLES/POSTES_IDEAUX.md` : typologies de poste recherchées
- `06_MARCHE/SYNTHESE_LOGISTIQUE.md` : tendances du marché, attentes RH et fourchettes salariales

### 3. Sourcer les opportunités

Le rôle de l'agent veille est de collecter les annonces, d'identifier les cibles pertinentes et d'alimenter `03_CANDIDATURES/TEMPLATE/job_description.md`.

### 4. Personnaliser les candidatures

L'agent personnalisation prend en entrée la fiche poste, ton CV source et ton pitch exécutif pour produire :

- `cv_targeted.md`
- `cover_letter.md`
- `fit_gap.md`
- `company_brief.md`

Pour chaque nouvelle candidature, crée un dossier dédié sous `03_CANDIDATURES/`.

### 5. Suivre les candidatures

Crée un fichier `status.md` dans chaque dossier de candidature pour suivre :
- statut (envoyée, relancée, entretien, refusée, gagnée)
- prochains pas
- date de relance

Mets à jour `04_RESEAUX/RECRUTEURS.md` avec les contacts de recruteurs et `MESSAGES_MODELE.md` avec les messages de relance ou d'approche.

### 6. Préparer et capitaliser sur les entretiens

- `05_ENTRETIENS/PREP_GENERALE.md` : questions types, argumentaire, pitch
- `05_ENTRETIENS/DEBRIEFS.md` : retours après entretien et points d'amélioration

### 7. Archiver et optimiser

- `99_ARCHIVES/README.md` : conserver les candidatures closes et les versions historiques de documents
- Archive les dossiers de candidatures non retenues ou terminées pour garder le workspace propre

## Rôle des agents

### Agent veille & sourcing
Responsable de la recherche active d'offres, du filtrage selon tes critères et de la première qualification.

### Agent personnalisation
Responsable de l'adaptation du contenu de candidature aux attentes de chaque annonce.

### Agent préparation entretien
Responsable de la préparation spécifique au poste, des simulations d'entretien et de la capitalisation post-entretien.

### Agent organisation / suivi
Responsable de l'état des candidatures, du suivi des relances et de la mise à jour des contacts.

## Mode d'emploi rapide

1. Mets à jour `01_PROFIL/*`
2. Identifie les cibles dans `02_CIBLES/*`
3. Récupère une annonce et remplis `03_CANDIDATURES/TEMPLATE/job_description.md`
4. Génère un dossier de candidature ciblée
5. Note l'état dans `status.md`
6. Prépare l'entretien et écris le debrief

---

Ce README est ton guide central pour organiser une recherche d'emploi structurée en supply chain. Reviens-y à chaque étape pour garder le processus aligné et efficace.
