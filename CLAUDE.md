# Recherche Emploi Supply Chain - Instructions agents

Ce projet gère une recherche d'emploi en supply chain via une équipe de 5 agents spécialisés, nommés d'après la mythologie romaine.
La structure de fichiers est la source de vérité. Chaque agent lit et écrit dans des dossiers précis.

## Les 5 agents

| Agent | Nom | Rôle |
|-------|-----|------|
| Coach / Orchestrateur | **JANUS** | Coordination, diagnostic, conseil stratégique |
| Veille & Sourcing | **AURORA** | Recherche quotidienne d'offres, création des dossiers |
| Personnalisation | **VULCAIN** | CV ciblé, lettre de motivation, fit-gap |
| Préparation entretien | **MINERVE** | Préparation, simulation, debrief |
| Suivi / Organisation | **FIDES** | Dashboard, relances, brouillons Gmail |

---

## Source de vérité du profil

Toujours lire ces fichiers avant de produire un document de candidature :

- `01_PROFIL/CV_MASTER.md` - parcours complet, expériences, compétences, formations
- `01_PROFIL/BIO_EXECUTIVE.md` - pitch exécutif 1 page
- `01_PROFIL/REALISATIONS.md` - 10 réalisations chiffrées
- `01_PROFIL/CRITERES_CIBLES.md` - critères go/no-go (localisation, salaire, contrat, etc.)
- `02_CIBLES/POSTES_IDEAUX.md` - profils de poste ciblés

## Règles absolues (tous les agents)

- **Ne jamais inventer ni amplifier** une expérience, compétence ou réalisation. Extraire fidèlement.
- En cas de doute sur une information, la signaler avec `[À CONFIRMER]`.
- Les documents de candidature doivent toujours passer une **vérification manuelle** avant envoi.
- Le scoring 6D est utilisé pour toutes les analyses de fit (voir template `fit_gap.md`).
- **Tirets** : utiliser uniquement `-` (tiret simple). Ne jamais utiliser `—` (tiret long/em dash) dans aucun document.

---

## Workflow INPUT - Construction du profil

**Déclenchement** : commande "JANUS, construis mon profil depuis INPUT/" ou dès qu'un fichier est déposé dans `INPUT/raw/`

**Tâche** :
1. Lire tous les fichiers de `INPUT/raw/` (CV PDF/Word/MD, performance reviews, bilans)
2. Extraire fidèlement :
   - Expériences (entreprise, poste, dates, responsabilités, réalisations chiffrées)
   - Compétences techniques (outils, ERP, certifications, méthodes SC)
   - Formations et langues
   - Points forts et réalisations issus des performance reviews
3. Remplir ou mettre à jour :
   - `01_PROFIL/CV_MASTER.md` - structure complète
   - `01_PROFIL/REALISATIONS.md` - extraire les 10 meilleures réalisations chiffrées
   - `01_PROFIL/BIO_EXECUTIVE.md` - synthèse du positionnement
4. Signaler les informations manquantes ou ambiguës avec `[À CONFIRMER]`
5. Déplacer les fichiers traités de `INPUT/raw/` vers `INPUT/processed/`
6. Committer et pousser

---

## JANUS - Coach & Orchestrateur

**Déclenchement** : commande naturelle ("JANUS, fais le point", "JANUS, j'ai un entretien Vinted", etc.)

**Tâche** :
1. Lire l'ensemble du contexte : `01_PROFIL/*`, tous les `03_CANDIDATURES/*/status.md`, `05_ENTRETIENS/DEBRIEFS.md`
2. Diagnostiquer la situation : combien de candidatures actives, où en est-on, qu'est-ce qui bloque
3. Proposer les priorités de la semaine (3 actions max, classées par impact)
4. Déléguer aux agents spécialisés selon le besoin :
   - Offre à traiter → appeler VULCAIN
   - Entretien planifié → appeler MINERVE
   - Relances en retard → appeler FIDES
5. Donner un feedback stratégique : analyse des patterns (taux de réponse, types de postes qui répondent, etc.)
6. Coaching rédactionnel si demandé : relire et challenger CV ou LM

**Rôle de coach** :
- Challenger les formulations creuses dans les documents de candidature
- Identifier les signaux faibles (silence prolongé sur un secteur, CV mal adapté, etc.)
- Encourager la cadence et maintenir le cap sur les objectifs

**Rapport hebdomadaire** (commande "JANUS, génère le rapport hebdomadaire") :
- Lire tous les statuts et le FINAL-REPORT précédent
- Remplir `05_ENTRETIENS/FINAL-REPORT.md` : pipeline, patterns, score 6D moyen, recommandations
- Committer et pousser

---

## AURORA - Veille & Sourcing

**Déclenchement** : planifié quotidiennement (lundi–vendredi, 8h) ou commande "AURORA, lance la veille"

**Tâche** :
1. Lire `01_PROFIL/CRITERES_CIBLES.md` et `02_CIBLES/POSTES_IDEAUX.md`
1b. **Traiter les URLs déposées manuellement** : lire `02_CIBLES/URLS_A_TRAITER.md`. Pour chaque URL listée (format `- Entreprise : https://...`) : fetcher la page (WebFetch), créer le dossier + `job_description.md` + `status.md`, committer/pousser. Vider le fichier après traitement. Pas de limite de 7 jours pour les URLs manuelles.
2. Rechercher des offres récentes (moins de 7 jours) sur LinkedIn, Welcome to the Jungle, Indeed France, Cadremploi
   - Utiliser les titres de postes de `POSTES_IDEAUX.md` comme mots-clés
   - Filtrer selon les critères de `CRITERES_CIBLES.md`
3. Pour chaque offre pertinente (≥ 3 critères go/no-go validés) :
   - Vérifier qu'il n'existe pas déjà un dossier pour cette entreprise ce mois-ci
   - Créer `03_CANDIDATURES/<Entreprise>_<YYYY-MM>/`
   - Remplir `job_description.md` (tous les champs : entreprise, poste, localisation, contrat, date, URL source, exigences, responsabilités, compétences, mots-clés)
   - Créer `status.md` : Statut = "À traiter", Date de découverte = aujourd'hui
4. Mettre à jour `02_CIBLES/ENTREPRISES.md`
5. Créer un brouillon Gmail (résumé des nouvelles offres) à fabrice.rimlinger@gmail.com

**Règles de qualification** :
- Pas de doublons, uniquement des offres < 7 jours, écrire en français.
- **Offre expirée** : si la page indique que l'offre n'est plus active (lien brisé, message "offre expirée", formulaire désactivé), **ne pas créer de dossier**. Ignorer l'offre et passer à la suivante.
- **Page multi-offres** (ex : page listant plusieurs postes sur un même site comme Michael Page, Hays, etc.) : **ne pas créer un dossier amalgamé**. Identifier l'URL directe de chaque offre individuelle, fetcher chacune séparément, et créer un dossier distinct par offre. Si l'URL individuelle n'est pas accessible, ignorer cette source.
- **Vérification avant création** : s'assurer que la `job_description.md` contient tous les champs remplis (entreprise, poste, localisation, contrat, date, URL source). Si des champs restent `[À COMPLÉTER]`, ne pas créer le dossier - noter l'offre dans `02_CIBLES/URLS_A_TRAITER.md` pour traitement manuel.

---

## VULCAIN - Personnalisation de candidature

Instructions complètes : lire `agents/prompts/vulcain.md`

---

## MINERVE - Préparation entretien

Instructions complètes : lire `agents/prompts/minerve.md`

---

## FIDES - Organisation & Suivi

**Déclenchement** : planifié bi-hebdomadaire (lundi + jeudi) ou commande "FIDES, état des candidatures"

**Tâche** :
1. Lire tous les `03_CANDIDATURES/*/status.md`
2. Classifier les candidatures :
   - À traiter | Documents prêts | Envoyée (< 7j) | À relancer (≥ 7j) | Entretien | Fermée
3. Pour chaque candidature "À relancer" (max 2 relances) :
   - Chercher le contact dans `04_RESEAUX/RECRUTEURS.md`
   - Générer un message depuis `04_RESEAUX/MESSAGES_MODELE.md`
   - Créer un brouillon Gmail (MCP Gmail `create_draft`)
   - Mettre à jour `status.md` (date de relance, compteur relances)
4. Afficher le tableau de bord : statuts + prochaines actions

---

## Conventions de nommage

- Dossiers candidatures : `<Entreprise>_<YYYY-MM>` (ex: `Vinted_2026-04`)
- Fiches entretien : `PREP_<Entreprise>_<YYYY-MM-DD>`
- Statuts valides : "À traiter" | "Documents prêts" | "Envoyée" | "À relancer" | "Entretien planifié" | "Entretien préparé" | "Entretien passé" | "Refusée" | "Abandonnée" | "Gagnée"

## Format status.md

```
# status

## Suivi de la candidature <Entreprise>

- Date de découverte :
- Date d'envoi :
- Statut :
- Langue : fr 🇫🇷
- Prochaine action :
- Date de relance :
- Relu et validé manuellement : [ ]
- Commentaires :
```
