# Session-log - CV IT pour Astrulys, normalisations repo-wide

- **Date** : 2026-08-12, 18:01
- **Type** : close-session
- **Agent** : JANUS

---

## Actions réalisées

### 1. Production des CV IT / transformation digitale (FR + EN)

Objectif initial : un CV standard orienté IT pour Astrulys, cabinet de conseil en transformation digitale à Marseille.

Livrables dans `01_PROFIL/` : `CV_IT_TRANSFO_DIGITALE.{md,html,pdf}` (FR) et `CV_IT_DIGITAL_TRANSFORMATION_EN.{md,html,pdf}` (EN). HTML écrits à la main sur la charte du CV 2026, PDF A4 de 2 pages générés via wkhtmltopdf.

Contenu extrait de `CV_MASTER.md` sans invention, repositionné sur l'axe IT :
- Réalisations clés : Amazon WW Expansion platform, automatisation IA/RPA Colis Privé, WMS + TMS Pomona, PMO Alloga/Cencora
- Sparklines for Excel descendu des réalisations vers les compétences
- Ligne Leadership recentrée sur les budgets pilotés (72 M€ CAPEX, 40 M€/an) après suppression du doublon C-level avec le profil

Itérations sur retours de Fabrice, toutes appliquées aux 4 fichiers en parallèle :
- Alloga : implémentation IA dans les tâches quotidiennes, définition de processus, équipe IT Marseille de 80 personnes
- Pomona requalifié : WMS avec les équipes Méthodes et Process + TMS sur 600 camions (tournées, capteurs embarqués, gestion des véhicules), l'intégration ERP atténuée en "contribution"
- "SHIELD" remplacé par "Amazon WW Expansion platform" (SHIELD est un terme interne Amazon)
- Conseil et avant-vente technique retirés du profil - Fabrice n'a pas cette expérience
- Colis Privé : les deux postes regroupés en une seule expérience "Directeur Business Excellence et Transformation" (07/2023 - 02/2026), aligné aussi dans `CV_MASTER.md`

Intégration d'une relecture recruteur externe : titre recentré sur l'interface Métiers-IT, profil resserré, franglais réduit côté FR (suivi des jalons, reporting aux parties prenantes, gouvernance projet, responsabilisation, décision pilotée par la donnée).

### 2. Normalisations repo-wide

**Diplôme** : "Agricultural Engineer" et variantes remplacés par "Ingénieur Agronome (MSc)" dans 24 fichiers, dossiers envoyés et archives inclus. Redondances nettoyées ("Master of Science, Agronomy", doubles mentions MSc). Règle ajoutée dans `CLAUDE.md`.

**Orthographe US** : appliquée à 39 documents anglophones (`organization`, `optimization`, `standardization`, `customized`, `programs`, `artifacts`, `modeling`, `analyze`). Détection par densité de mots-outils pour épargner les documents français. Deux faux positifs rattrapés : `BIO_EXECUTIVE.md` (français, restauré) et `Licence Biochimie` devenu `License`. Règle ajoutée dans `CLAUDE.md`.

### 3. Dossier Astrulys

Création de `03_CANDIDATURES/Astrulys_CandidatureSpontanee_2026-08/` avec le PDF exact envoyé le 12/08 à Kaysser Agnouche, fondateur.

Requalification progressive au fil des informations de Fabrice :
- Contact 1er degré, introduction par **Benito Diz, DSI Colis Privé** - priorité passée de Moyenne à Haute
- Entretien de prise de contact **déjà passé, très positif** : ce n'est pas une candidature à un poste mais une entrée en vivier pour de futures missions de transformation sur Marseille
- Debrief renseigné : **TJM 700-900 €/j, pipeline de 3 clients**

### 4. Prolongation mission Alloga

Mission prolongée de 3 mois, échéance repoussée de ~09/09/2026 à ~09/12/2026. Session-log dédié écrit, `status.md` mis à jour.

---

## Candidatures touchées

| Dossier | Action |
|---|---|
| Astrulys_CandidatureSpontanee_2026-08 | Créé, statut "Entretien passé", debrief renseigné |
| Alloga_SeniorPMOChangeLead_2026-06 | Prolongation +3 mois enregistrée |
| Shiftmove_PlanningLogisticsOpsManager_2026-07 | Rejet confirmé (déjà enregistré au 05/08) |
| AmazonFrance_SrFleetManager_2026-08 | Statut remis dans l'enum (correction Librarian) |
| 21 autres dossiers | Normalisation diplôme et orthographe US |

---

## Décisions

1. **Astrulys est un vivier, pas une piste active.** Un TJM cabinet de 700-900 € face aux 850 € en direct chez Alloga, moins la marge du cabinet, et un pipeline de 3 clients : le déclenchement est peu probable à court terme et l'équation financière est défavorable. La relation se nourrit par la valeur, elle ne se relance pas comme une candidature.
2. **Regroupement Colis Privé assumé** sur tous les CV, y compris `CV_MASTER.md`. La progression interne (Director of Transformation puis Director Business Excellence) est conservée en note dans la source de vérité.
3. **Deux règles permanentes ajoutées à `CLAUDE.md`** : "Ingénieur Agronome (MSc)" et orthographe américaine pour les documents anglais.

---

## Résultat Librarian

**Corrections appliquées**
- `AmazonFrance_SrFleetManager_2026-08` : statut "Documents prêts (v2 anglaise, 2026-08-11)" hors enum, ramené à "Documents prêts", l'annotation déplacée en commentaires
- `Astrulys_CandidatureSpontanee_2026-08` : `job_description.md` créé, documentant l'absence d'offre publiée et le cadrage disponible
- `CLAUDE.md` : les CV IT génériques ajoutés à la section profil, distingués des sources de vérité

**Signalé à Fabrice**
- `FarmsDigital_Network_2026-05` : pas de `job_description.md`, alors que `fit_gap.md` et `company_brief.md` existent. Antérieur à cette session.
- `AmazonFrance_SrFleetManager_2026-08` : "À traiter" dans `ENTREPRISES.md` contre "Documents prêts" dans le dossier
- `05_ENTRETIENS/PREP_GENERALE.md` : les leçons actives datent toutes du 06/05 (Alloga). Ni le rejet Shiftmove ni l'entretien Astrulys n'ont alimenté la boucle.

**Conforme** : champs `status.md`, cohérence `ENTREPRISES.md`, `URLS_A_TRAITER.md` vide.

---

## Prochaines étapes

1. **Compléter le debrief Astrulys** - stade de maturité des 3 opportunités du pipeline (signées, en négociation, prospects). Sans cette information, impossible de trancher entre piste réelle et politesse. *(Fabrice, puis JANUS)*
2. **Remercier Benito Diz** et lui dire que l'échange avec Kaysser a été positif. C'est le seul DSI du réseau de Fabrice et le meilleur retour sur investissement disponible. *(Fabrice)*
3. **Alimenter les leçons actives** avec le rejet Shiftmove et l'entretien Astrulys. *(JANUS)*
4. **Préparer le discours sur les tenures courtes depuis 2021** - Infarm 1 an, Amazon planning 1 an, Colis Privé 2,5 ans, Alloga en mission. Seul angle mort identifié par la relecture recruteur. *(MINERVE)*
5. **Traiter les 3 dossiers "Documents prêts"** : CEVA Program Director, Meli Consulting, Amazon France Fleet Manager. *(FIDES pour l'envoi, VULCAIN si mise à jour des documents)*
6. **Point de contact léger Astrulys vers le 15/09**, sans posture de demandeur.
