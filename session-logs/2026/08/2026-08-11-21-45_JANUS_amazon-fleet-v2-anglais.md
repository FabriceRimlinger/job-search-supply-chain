# Session-log - 2026-08-11 21:45 - Amazon Sr Fleet Manager v2

**Types d'entrée** : `realignment` + `mid-session-insight`
**Dossier impacté** : `03_CANDIDATURES/AmazonFrance_SrFleetManager_2026-08/`
**Agents mobilisés** : JANUS (enrichissement offre), VULCAIN (v2 des documents)

---

## Déclencheur

Fabrice dépose dans `INPUT/` une capture de la page officielle amazon.jobs de l'offre Sr Fleet Manager, déjà traitée le 2026-08-05 depuis une capture LinkedIn.

## Realignment - langue de correspondance

**Direction initiale** : dossier monté en français. L'offre était affichée en français sur amazon.jobs, `status.md` portait `Langue : fr`, et le CV comme la lettre étaient rédigés en français.

**Correction de Fabrice, en cours de session** : "for Amazon, all correspondance in english".

**Ce qui a été fait** : `cv_targeted.md` et `cover_letter.md` réécrits intégralement en anglais. `fit_gap.md` et `company_brief.md` laissés en français - ce sont des documents de travail internes, jamais envoyés. Ce découpage reprend le précédent du dossier `CEVA_GlobalBPExcellenceExpert_2026-08`, vérifié avant d'appliquer.

**Pourquoi ça compte au-delà de ce dossier** : la règle vaut pour Amazon en général, pas pour cette candidature seule. Toute future candidature ou relance Amazon doit partir en anglais par défaut. À appliquer sans redemander.

**Effet secondaire favorable** : l'annonce Amazon est rédigée en anglais puis traduite (sélecteur "Français" sur la page, termes anglais non traduits dans la capture LinkedIn comme "Single-Threaded Leader"). Le parsing ATS porte donc sur les termes canoniques anglais. Le pivot renforce le score ATS au lieu de l'affaiblir.

## Mid-session-insight - la localisation multi-sites est un risque, pas une opportunité

**Comment on y est arrivé** : la page officielle liste trois sites de rattachement - Longvic (21), Marseille (13), Lyon (69) - là où la capture LinkedIn n'affichait que Marseille. Premier réflexe, annoncé à Fabrice : "élargit le go/no-go localisation". Faux.

**L'insight** : sur une annonce Amazon, une liste de sites signifie que l'employeur affecte, pas que le candidat choisit. Vérification faite dans `01_PROFIL/CRITERES_CIBLES.md` : seul Marseille satisfait le critère dur "Marseille / Provence / Sud de France en priorité". Lyon et surtout Longvic (agglomération dijonnaise, ~500 km) tombent dans "autres villes françaises en secondaire uniquement si scope exceptionnel". Le multi-sites **dégrade** le go/no-go au lieu de l'améliorer : 7 → 6.

**Implication downstream** : le site de rattachement devient la question bloquante à poser dès le premier échange recruteur, avant tout investissement MINERVE en préparation d'entretien. Inscrite dans `status.md`, `fit_gap.md` et `company_brief.md`.

**Règle générale à retenir** : une annonce multi-sites se lit comme un risque de localisation tant que l'affectation n'est pas confirmée. Ne jamais la scorer comme un élargissement d'opportunité.

## Insight process - les justifications de score se périment

Deux fois dans la même session, un score 6D portait une justification devenue fausse :

1. ATS noté 6/10 sur "absence du terme fleet management au CV" alors que le `cv_targeted.md` contenait déjà un bloc "Fleet & asset management". Le protocole VULCAIN exige ATS ≥ 7 avant validation : le dossier était au statut "Documents prêts" sur un score qui aurait dû le bloquer.
2. Après correction, la nouvelle justification citait les termes français ajoutés au CV - puis le pivot linguistique les a fait disparaître du fichier. Rescorrigée.

**À retenir** : quand un document change, relire les justifications de score qui le décrivent. Le chiffre peut rester juste alors que la raison ne l'est plus.

## Décisions

- Score 6D Amazon : 46/60 → **48/60**. Compétences 7→8 (qualif de base assouplie en "logistique **ou** rôle opérationnel", nouveau critère formation couvert par des preuves réelles), ATS 6→8 (justification corrigée, cible anglaise), go/no-go 7→6 (risque site de rattachement).
- Canal de candidature : amazon.jobs direct (Job ID 10492642), pas le apply LinkedIn.
- Nouvelle qualification de base "animer des sessions de formation et créer les supports" couverte sans invention, via Alloga (rituels de pilotage + supports de gouvernance), Infarm (programmes de formation et mentoring), Pomona (documentation et formation utilisateurs sur 600 camions GPS). SHIELD écarté volontairement - plateforme BI, pas de l'animation de formation, l'utiliser aurait été une amplification.

## Prochaines étapes

1. **Fabrice** : relecture manuelle du CV et de la lettre anglaise (`Relu et validé manuellement` toujours à `[ ]`).
2. **Fabrice** : ajouter si possible une actualité Amazon France Transport / flotte vérifiée dans la lettre - aucune source fiable disponible à la rédaction, rien n'a été inventé.
3. Poser la question du site de rattachement dès le premier contact recruteur.
4. **MINERVE** : préparation entretien à déclencher seulement après relecture validée (score 48/60 ≥ 45).

---

## Addendum - correction repo-wide du nombre de stations AMZL (2026-08-11, fin de session)

**Type d'entrée** : `realignment` (correction factuelle de portée repo)

**Le fait corrigé** : les stations AMZL lancées en Italie et Espagne sont au nombre de **10, dont 6 en Espagne et 4 en Italie**. Tous les fichiers du repo affirmaient 15 depuis l'origine.

**Comment c'est sorti** : Fabrice l'a signalé spontanément en commentant le dossier Amazon, pas à la suite d'une vérification. Sa première formulation ("Spain and Italy w/ respectively 4 and 6") a été comprise comme 4 Espagne / 6 Italie, puis inversée par sa demande suivante ("4 IT, 6 ES"). Répartition tranchée explicitement avant d'écrire : **6 Espagne, 4 Italie**. Le dossier Amazon, déjà rédigé sur 6 IT / 4 ES, a été inversé.

**Portée de la correction** : 48 fichiers - fichiers profil (`CV_MASTER.md`, `BIO_EXECUTIVE.md`, `REALISATIONS.md`, `LINKEDIN_PROFILE.md`, `CATALOGUE_ANECDOTES.md` dont le tag `#15-stations` devenu `#10-stations`), tous les dossiers de candidature actifs, `99_ARCHIVES/`, `05_ENTRETIENS/PREP_GENERALE.md`, les CV HTML, et le sous-projet `claude-linkedin-assistant/`.

**Ce qui n'a pas été touché, volontairement** :
- Les **session-logs** : archives historiques, on ne réécrit pas le passé.
- Les mentions de **"15+ équipes transversales"** : claim distinct (nombre d'équipes coordonnées, 19 au CV_MASTER), sans rapport avec le nombre de stations. Vérifié une par une, 9 occurrences préservées.
- Les affirmations **"2 centres au-delà des objectifs initiaux"** (JD Logistics `cover_letter.md` et `cv_targeted.md`, Compagnie Fruitière `cv_targeted.md` et fiche PREP). Ce récit supposait une cible de 13 pour 15 livrées. Avec 10 livrées, la cible deviendrait 8 - non vérifiable, donc laissé en l'état et signalé. **[À CONFIRMER] avec Fabrice.**

**Ce que ça coûte** : des candidatures déjà envoyées annonçaient 15 (Alloga Portfolio Manager, dont l'entretien est passé ; JD Logistics ; CEVA ; Compagnie Fruitière ; Shiftmove, refusée). Les fichiers sont désormais corrigés, mais **ce qui est parti est parti**. Si le sujet revient en entretien sur un de ces dossiers, la position honnête est de corriger de soi-même.

**Leçon de process** : un chiffre repris de fichier en fichier sans source primaire s'est propagé dans 48 fichiers et plusieurs candidatures envoyées avant d'être remis en cause - par Fabrice, pas par un contrôle. Les réalisations chiffrées de `REALISATIONS.md` mériteraient une passe de vérification à la source, indépendamment de toute candidature.

**Autres confirmations de Fabrice** enregistrées le même jour : pas de propriété de la flotte chez Colis Privé (directeur de la performance), aucune expérience d'achat ni de leasing de véhicules, Pomona trop ancien pour porter un argument. Score Amazon ramené de 48 à 47/60 en conséquence.
