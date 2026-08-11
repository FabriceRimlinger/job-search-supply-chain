# Audit de vérification - REALISATIONS.md

> Passe menée le 2026-08-11 par JANUS, à la demande de Fabrice, après la découverte que "15 stations AMZL" était faux et s'était propagé dans 48 fichiers.
>
> **Méthode** : chaque affirmation est confrontée aux sources primaires disponibles dans `INPUT/processed/` - les six Forte reviews Amazon (2017, 2018, 2019, 2020, 2021, 2023), le rapport `WP DD 2020 wrap up.docx` et `DD survey results.docx`.
>
> **Principe de classement** : un chiffre n'est pas "vérifié" parce qu'un ancien CV le répète. Les anciens CV sont la source de la contamination, pas une preuve. Trois catégories seulement : confirmé par un document faisant autorité, attesté par Fabrice sans source indépendante, ou contredit.
>
> **Ce document ne modifie rien.** Les arbitrages appartiennent à Fabrice.

---

## Synthèse

| Catégorie | Nombre |
|---|---|
| Confirmé par source primaire | 9 |
| Contredit par source primaire | 7 |
| Attesté par Fabrice, aucune source dans le repo | 9 |
| Incohérence interne au repo | 3 |

**Le point le plus important de cet audit n'est pas un chiffre : c'est un titre.** Voir section dédiée.

---

## 1. Le titre Amazon officiel - problème transverse

Les **six** Forte reviews portent le même intitulé, sans exception :

> **Business title: Program Manager, Supply Chain**

2017 (finalisé par Bernard De Guillebon), 2018 (Helder Velho), 2019 (Steve Griffiths), 2020 (Steve Griffiths), 2021 (Chris Young-Wootton), 2023 (Jenny Schumacher).

Or `CV_MASTER.md` et tous les CV ciblés annoncent :
- "Head of Last Mile Delivery Expansion South EU" (2016-2018)
- "Head of Technical & Environmental Real Estate Due Diligence" (2018-2021)
- "Senior Manager - Supply Chain Long-term Planning & Risk Management" (2022-2023)

**Aucun de ces trois intitulés n'apparaît dans les documents RH Amazon.** Les fonctions décrites sont réelles - les verbatims des pairs confirment le périmètre, le leadership d'équipe et les lancements pays. Mais le grade officiel était Program Manager pendant toute la période.

**Pourquoi ça compte maintenant** : la candidature en cours est **chez Amazon**. Amazon vérifie l'historique interne d'un ancien salarié. Un écart entre le CV et le dossier RH interne est le type d'incohérence qui se détecte sans effort et qui coûte cher.

**Options, à trancher par Fabrice** :
1. Aligner les intitulés sur "Program Manager, Supply Chain" et décrire le périmètre réel en sous-titre (ex : "Program Manager, Supply Chain - Last Mile Expansion Lead, Italy & Spain"). Honnête, vérifiable, et le périmètre reste impressionnant.
2. Conserver les intitulés fonctionnels mais les présenter explicitement comme des descriptions de rôle et non des grades.

Option 1 recommandée pour la candidature Amazon au minimum.

*Nuance en faveur de Fabrice* : `WP DD 2020 wrap up` indique "Fabrice Rimlinger replaced Steve Griffiths in May 2020 as team leader", et l'équipe comptait alors un Sr manager. Le rôle de responsable d'équipe est donc documenté, même si le grade ne l'était pas.

---

## 2. Confirmé par source primaire

| Affirmation | Source | Verdict |
|---|---|---|
| Rating **"Exceeds" 2021** | Forte 2021, section Performance rating | ✅ **Exact.** "Exceeds" est bien le rating affiché. |
| **"Tech-Master par excellence"** | Forte **2019**, verbatim d'un pair | ✅ **Exact.** Citation complète : *"Fabrice is the Tech-Master par excellence, may it be EXCEL, may it be Wiki, whatever has any connection to a PC, I'd ask Fabrice."* À dater 2019 - `REALISATIONS.md` ne la date pas. |
| **"Multi-cultural and multi-lingual with excellent cross-cultural ability"** | Forte 2020, verbatim d'un pair | ✅ **Exact au mot près.** |
| **"Extraordinary experience - precious resource to understand and solve business critical situations"** | Forte 2020, verbatim d'un pair | ✅ **Fidèle.** Original : *"Fabrice is a colleague with extraordinary experience. He's a precious resources due to his well-recognized capacity to understand ans solve business critical sitations."* Compression fidèle. |
| **"Revolutionised how the team operates using data"** | Forte 2021 | ✅ **Fidèle** mais voir §3 pour l'attribution. Original : *"Fabrice has revolutionised how the team operates, using his knowledge to help the team leverage data to get to the right answer at pace, whilst exploring options for improvements to ways of working (eg Shield, DD Intake and DD Summary)."* |
| **"Guidé l'équipe dans la bonne direction dans de nombreuses instances"** | Forte 2023, verbatim d'un pair | ✅ **Traduction fidèle** de *"has guided the team in the right direction in numerous instances"*. |
| **Volume DD : 133 sites en 2018 → 686 en 2020** | `WP DD 2020 wrap up` | ✅ **Exact.** Le rapport donne 686 (2020), 312 (2019), 133 (2018). |
| **30+ consultants** | `WP DD 2020 wrap up` | ✅ **Confirmé.** "Out of 36 active DD consultants, 10 suppliers were onboarded in 2020." |
| **Verbatims enquête satisfaction DD** (3 citations) | `DD survey results` + `WP DD 2020 wrap up` | ✅ **Fidèles**, mais voir §3 sur leur qualification de "verbatims". |

---

## 3. Contredit par source primaire

### 3.1 Budget de 40M€/an - contredit

`REALISATIONS.md` item 4 : *"Gestion d'un budget de 40M€/an"*.

`WP DD 2020 wrap up`, section DD expenditure :
> *"In 2020, 2,548 PO lines were created (vs.1094 in 2019) for a FY total of approx. **13.3M€**."*

**Écart d'un facteur 3.** 2020 était l'année de pic documentée (686 sites). Le chiffre de 40M€ n'apparaît dans aucune source du repo.

Hypothèse à vérifier : 40M€ pourrait correspondre au cumul 2018-2021, ou à un périmètre plus large que la seule dépense DD. En l'état, **non soutenu**. Ce chiffre figure dans `CV_MASTER.md` et dans plusieurs CV ciblés.

### 3.2 Équipe de 10 risk managers - contredit

`WP DD 2020 wrap up` :
> *"In 2020, the DD team included **7 members**: 5 DD managers (DDM) (vs. 4 in 2019), 1 Testfit manager and 1 Sr manager."*

Le plan 2021 prévoyait 2 recrutements supplémentaires, soit 9 au maximum. **"10 risk managers" surestime**, et "risk managers" n'est pas l'intitulé employé (DD managers).

### 3.3 "Plus de 1200 Due Diligence par an" - non soutenu

Le volume documenté le plus élevé est **686 intakes en 2020**. Le rapport anticipe une hausse en 2021 sans la chiffrer. 1 200 n'apparaît nulle part.

Note : le rapport mentionne en plus ~200 "Quick Checks" et 157 testfits en S2 2020. Une agrégation large de tous les livrables 2020 approcherait le millier - mais ce ne sont pas 1 200 Due Diligence.

### 3.4 "Volume géré x5 en 3 ans" - imprécis

133 (2018) → 686 (2020) est un facteur **5,2 sur deux ans**, pas trois. Le multiplicateur est bon, la durée non.

### 3.5 "Due Diligence Environnementales" - imprécis

Le rapport indique que les Phase I environnementales ont porté sur **29% des sites** en 2020. Le périmètre réel est technique *et* environnemental. Qualifier les 686 de "Due Diligence Environnementales" surestime la part environnementale.

### 3.6 SHIELD et l'onboarding - mauvaise attribution

`REALISATIONS.md` item 3 attribue à SHIELD le fait d'avoir *"rendu l'onboarding des nouveaux collaborateurs considérablement plus facile"*.

Forte 2021, feedback du **manager** :
> *"His **due diligence wiki page** makes it far easier to onboard new starters, especially during Covid when working from home."*

Le mérite est attribué à la **page wiki DD**, pas à SHIELD. Ce sont deux artefacts distincts, tous deux réels. L'item mélange les deux.

**Deuxième erreur sur le même item** : la source est indiquée *"Forte 2021, peers feedback"*. Les deux citations proviennent du **manager** (Chris Young-Wootton) et d'un **direct report**, pas des pairs.

### 3.7 Dashboard SNN4 - propriété surestimée et résultat contredit

`REALISATIONS.md` item 9 : *"**Développement du dashboard SNN4** (réduction des blocages de conformité EU, **prévention des drop-offs**)"*.

Forte 2023, pair :
> *"Fabrice has been a **great support for developing** the SNN4 dashboard. **He guided the team**, but also believed in the team's inputs."*

Il a soutenu et guidé - il n'a pas développé. Nuance importante face à un Dive Deep Amazon.

Plus gênant, un autre pair, en growth idea :
> *"While the project started with solving the drop-off issue, **the dashboard was focused more towards capturing overall compliance blockers**. Fabrice could have provided more of a leadership view and also helped drive adoption of the dashboard for downstream implementation."*

La "prévention des drop-offs" est précisément l'objectif dont le projet s'est écarté. **L'affirmation retient comme résultat ce que la source décrit comme un manque.**

### 3.8 "Invent & Simplify cité dans 100% des reviews" - trompeur

La parenthèse énumère *(2019, 2020, 2021, 2023)*. Il existe **six** Forte dans `INPUT/processed/` : 2017 et 2018 sont omises. "100% des reviews" décrit en réalité 100% de quatre années choisies.

Invent & Simplify apparaît bien sous une forme ou une autre dans les six. Mais son **rang** varie fortement :

| Année | Rang d'Invent & Simplify | Détail |
|---|---|---|
| 2017 | Auto-évaluation + 1 pair | Format sans décompte |
| **2018** | **6ème** | 3 réponses, loin derrière Deliver Results (12) et Ownership (10) |
| 2019 | 1er ex aequo | 4 réponses, à égalité avec Earn Trust |
| 2020 | **1er** | 6 réponses |
| 2021 | **1er** | 7 réponses |
| 2023 | Faible, partiellement en growth idea | Forces dominantes : Dive Deep, Earn Trust, Ownership, Bias for Action |

Formulation défendable : *"Invent & Simplify identifié comme Leadership Principle dominant dans les reviews 2019, 2020 et 2021"*. C'est exact, vérifiable, et suffisant.

---

## 4. Attesté par Fabrice, aucune source primaire dans le repo

Ni confirmé ni contredit. Aucun document du repo ne les établit, et les anciens CV ne comptent pas comme preuve. À traiter comme déclaratif tant qu'une pièce ne remonte pas.

| Affirmation | Ce qui la trancherait |
|---|---|
| 550k€/an d'économies CS, -20% de budget, +7,5% d'activité (Colis Privé) | `KPI CP alloga.png` (présent dans `INPUT/processed/`, non exploité), un support de comité de direction CP |
| Réduction de 40% des tâches manuelles (Colis Privé) | Même source |
| 250-300k colis/jour, 300 chauffeurs propres + 4 000 tiers | Reporting opérationnel CP |
| Intégration de 300 employés (acquisition Milee) | Documentation projet ou accord d'entreprise |
| CAPEX de 72M€ et équipe de 16 (Infarm) | Budget ou organigramme Infarm |
| SOP d'expansion 36 mois, 80+ bâtiments EU | `amazon EU L&E Weekly Portfolio Flash Report Wk26` (présent, non exploité) |
| 10 stations AMZL et "75% des livraisons Amazon" en IT/ES | Corrigé de 15 à 10 le 2026-08-11 sur déclaration de Fabrice. Le 75% reste non sourcé. |
| Dole Romania : 5 sites, -50% d'effectifs | - |
| Geest/Primaflor : -50% de coûts logistiques | - |

**Deux sources présentes dans `INPUT/processed/` n'ont pas été exploitées** et pourraient trancher plusieurs lignes : `KPI CP alloga.png` et `amazon EU L&E Weekly Portfolio Flash Report Wk26 v2.0.pdf`. Dis-moi si tu veux que je les ouvre.

---

## 5. Incohérences internes

1. **Le titre annonce 10 réalisations, le fichier en contient 11.** Corrigé en "11 réalisations" - correction mécanique, sans arbitrage.
2. **Items 1 et 2 datés "2024-présent"** alors que Fabrice a quitté Colis Privé en 02/2026 et est chez Alloga depuis 06/2026. Corrigé en "2024-2026".
3. **Item 10, Dole Romania, daté 2009-2010.** `CV_MASTER.md` place la restructuration roumaine sous le poste *Supply-chain Manager - Dole Europe, 2011-2012, Bucarest*, et un poste *Corporate Operation Controller, 2007-2011, Paris* le précède. Par ailleurs le catalogue d'anecdotes évoque un "Technical Projects Manager chez Dole Europe" en 2007, intitulé absent de `CV_MASTER.md`. Trois intitulés pour un même employeur : à clarifier par Fabrice, **non modifié**.

---

## 6. Matériau solide et inexploité

L'audit fait aussi apparaître des preuves plus fortes que certaines de celles retenues.

- **Forte 2018 : Deliver Results, 12 réponses (1 manager, 11 pairs), et Ownership, 10 réponses.** Ce sont les scores de reconnaissance les plus élevés de toutes les reviews, sur l'année des lancements AMZL. Bien plus probant que l'argument "Invent & Simplify à 100%".
- **Verbatims AMZL Espagne, Forte 2018**, jamais utilisés : *"He has take over Spain launches in Spain making them all successful, with a new and short team delivering great stations to Spain for first."* et *"Hugely influencial in the launch of ES last year and his bias for action came out at its best when rescuing Catalonia'n peak by landing the first MDS."* Directement pertinents pour la candidature Amazon.
- **Forte 2021, un pair** : *"Fabrice has been instrumental in reshaping the DD team and how it interacts with its customers."*

## 7. Ce que l'enquête satisfaction dit vraiment

Les trois citations reprises dans `REALISATIONS.md` sont fidèles, mais deux réserves :

1. Ce ne sont pas des **verbatims de stakeholders**. Ce sont les phrases de synthèse du rapport, rédigé par l'équipe DD elle-même. La section s'intitule "Verbatims externes" - qualification inexacte.
2. L'enquête contenait **autant de critiques** : *"the DD reports appear to be sometimes unclear"*, *"the DD team could be more flexible and accommodating"*, *"perception that the DD team innovates, but not in the interest of customers"*, et *"very few answers despite of 3 reminders sent"*.

Un fichier de réalisations sélectionne évidemment le positif. Mais si ce document circule ou nourrit une préparation d'entretien, mieux vaut savoir que la source est équilibrée, pas élogieuse.

---

## Recommandations, par ordre de priorité

1. **Trancher la question du titre Amazon avant d'envoyer la candidature Sr Fleet Manager.** C'est le seul point de cet audit qui peut faire échouer une candidature en cours.
2. **Corriger le budget 40M€** dans `CV_MASTER.md`, `REALISATIONS.md` et les CV ciblés, ou retrouver la pièce qui le soutient. 13,3M€ documentés contre 40M€ affichés.
3. **Corriger "1 200 DD/an" en 686**, et "10 risk managers" en 7. Les chiffres réels restent remarquables : x5,2 de volume en deux ans à effectif quasi constant est une meilleure histoire que des chiffres ronds invérifiables.
4. **Reformuler SNN4** en "soutien et pilotage du développement", et retirer "prévention des drop-offs".
5. **Corriger l'attribution SHIELD/wiki** et "peers feedback" → "manager feedback".
6. **Remplacer "Invent & Simplify dans 100% des reviews"** par la formulation restreinte à 2019-2021.
7. Exploiter `KPI CP alloga.png` et le Flash Report Amazon pour trancher les lignes Colis Privé et SC Planning.
