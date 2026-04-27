# Catalogue d'anecdotes — Amazon Leadership Principles

> Sources : Writing Exercises Amazon (2014, 2022), Forte Reviews (2019-2023), CV.
> Format STAR : Situation → Task → Action → Result.
> Usage : réponses entretien comportemental, LM, pitch. Choisir l'anecdote la plus alignée avec l'entreprise cible.

---

## INVENT AND SIMPLIFY ⭐ (LP #1 de Fabrice — cité dans 100% des Forte reviews)

### Anecdote A — Sparklines for Excel (SfE)
**Source** : Writing Exercises 2014 & 2022, Forte reviews

**S** : En 2007, Technical Projects Manager chez Dole Europe. Reporting intensif sur portefeuille de projets (KPIs, P&L). Problème récurrent : formatage des graphiques Excel = perte de temps massive (couleurs, axes, placement) avant même d'analyser les données.

**T** : Créer un outil qui simplifie et accélère le reporting sans dépendre d'un designer. Aucun outil du marché ne répondait au besoin — les add-ins existants (Peltier, Juice Analytics) ne convenaient pas.

**A** : Inspiré par Edward Tufte (*The Visual Display of Quantitative Information*), j'ai conçu de zéro une bibliothèque VBA de formules Excel générant des micro-graphiques directement dans une cellule. Apprentissage du VBA sur le tas, en testant chaque composant graphique ("est-ce que cette ligne est vraiment nécessaire ?"). 14 types de graphiques créés : LineChart, BulletChart, Pareto, BoxPlot, Gantt, TreeMap, BeanPlot...

**R** : "Sparklines for Excel" (SfE) est un projet open-source **téléchargé plus de 100 000 fois**, encore utilisé dans des PME et grandes entreprises. J'ai utilisé SfE quotidiennement chez Amazon pour les rapports AMZL (IT, ES) et pour wireframer les dashboards avant de passer à PowerBI.

**LP secondaires** : Dive Deep, Learn and Be Curious, Deliver Results

---

### Anecdote B — Plateforme SHIELD (Amazon Real Estate Due Diligence)
**Source** : CV, Forte 2020 & 2021

**S** : Head of Technical & Environmental Real Estate Due Diligence, Amazon (2018-2021). Gérer 1 200+ Due Diligence EMEA/an avec 10 risk managers et 30+ consultants, un budget de 40M€/an. Le reporting était fragmenté, chaque équipe utilisait ses propres outils — aucune vision consolidée en temps réel.

**T** : Concevoir une plateforme BI centralisée, adoptée par toutes les parties prenantes EMEA, sans imposer une formation lourde.

**A** : J'ai conçu SHIELD de A à Z — architecture des données, logique de reporting, UX. Déployé progressivement avec formation intégrée. Priorité à la simplicité d'usage : les users devaient pouvoir l'utiliser sans guide.

**R** : Adoption totale par toutes les parties prenantes Amazon EMEA. Feedback Forte 2021 : *"Fabrice has revolutionised how the team operates, using his knowledge to help the team leverage data to get to the right answer at pace."* Accélération significative des délais de DD et amélioration de la qualité des rapports.

**LP secondaires** : Customer Obsession, Insist on Highest Standards, Earn Trust

---

### Anecdote C — Dashboard SNN4 (Amazon SC Planning, 2023)
**Source** : Forte 2023

**S** : Program Manager Supply Chain, Amazon (2022-2023). Nouveaux dans le rôle (3-6 mois). Problème de drop-offs sur les sélections de sites — les compliance blockers EU n'étaient pas visibles en temps réel.

**T** : Créer un mécanisme qui permette de détecter et réduire les blocages compliance avant qu'ils ne dérèglent les sélections.

**A** : Guidé l'équipe dans la conception du dashboard SNN4. Facilité les conversations entre les équipes business EU et programme pour s'assurer que le mécanisme couvrait les bons cas d'usage.

**R** : *"Guided the team... reducing EU compliance blockers and unblock selection for customers"* (Forte 2023). *"Facilitated conversations with EU business and program teams to ensure that mechanism that has been built to prevent drop offs is effective."*

---

## BIAS FOR ACTION ⭐

### Anecdote A — Andon Cord DCT1 Barcelona (AMZL Launch 2017)
**Source** : Writing Exercise Amazon 2022 A

**S** : Sr Launch Manager, AMZL. Go/No Go call à 18h, 6h avant le lancement de la Delivery Station DCT1 à Barcelone. L'équipe IT remonte un problème critique : le signal 4G chute à quasi zéro la nuit — précisément quand les associates font le tri (minuit-7h). 5 000 à 10 000 colis pourraient ne pas être triés. Pic 2017 à risque.

**T** : Décision à prendre en quelques minutes, sans données complètes : lancer quand même, adapter le process, ou retarder. Chaque option a des coûts importants (associates mobilisés, partenaires prêts, pression deadline).

**A** : J'ai tiré l'Andon cord et repoussé le lancement de 24h. Simultanément : (1) retiré DCT1 d'ATROPS pour qu'aucun colis ne soit affecté, (2) maintenu les associates sur site pour de la formation et des "virtual deliveries", (3) investigué une solution alternative en pensant hors du cadre — le FC BCN2 était dans le même bâtiment, séparé par un mur de béton. J'ai escaladé de Madrid à Seattle en quelques heures pour obtenir le feu vert du partage d'une fibre optique de BCN2.

**R** : À 7h le lendemain, un trou de 5cm est percé dans le mur de 40cm, l'ethernet est tiré. À 12h, le réseau AMZL est opérationnel avec *"la meilleure connexion broadband jamais déployée pour un lancement de DS"*. Lancement effectif J+1 sans impact client. La fibre WiMAX commandée est arrivée 1 mois plus tard (comme anticipé).

**LP secondaires** : Have Backbone/Disagree and Commit, Ownership, Deliver Results, Are Right A Lot

---

### Anecdote B — Intégration Milee post-acquisition (Colis Privé, 2023)
**Source** : CV

**S** : Director of Transformation, Colis Privé (2023-2024). Acquisition de Milee (300 chauffeurs). Nécessité d'intégrer 300 personnes rapidement, sans perturber 250 000 livraisons/jour.

**T** : Conduire l'intégration juridique, opérationnelle et humaine en quelques mois, sans interruption de service.

**A** : Mené les négociations juridiques, modélisé le P&L, aligné les équipes transversales sur les processus communs, maintenu l'exécution opérationnelle pendant toute la transition.

**R** : 300 employés intégrés avec continuité opérationnelle totale.

---

## DELIVER RESULTS ⭐

### Anecdote A — 550k€ d'économies Service Client (Colis Privé, 2024)
**Source** : CV

**S** : Director Business Excellence, Colis Privé. Contexte : activité en hausse de +7,5%, pression sur les coûts.

**T** : Réduire le budget Service Client sans dégrader la qualité de service ni l'expérience client.

**A** : Déployé un programme d'automatisation (AI forecasting, RPA, call bots) sur les tâches manuelles répétitives. Piloté 25 personnes sur la performance opérationnelle et client.

**R** : Budget CS réduit de **20% = 550k€/an d'économies**. Tâches manuelles réduites de **40%**. Délai de traitement amélioré.

---

### Anecdote B — 15 stations AMZL en 2 ans (Italie et Espagne)
**Source** : CV

**S** : Head of AMZL Expansion South EU, Amazon Logistics (2016-2018). Mission pionnière : déployer le réseau de livraison last mile Amazon en Italie et Espagne, marchés sans infrastructure AMZL existante.

**T** : Lancer 15 stations de livraison en 2 ans, en coordonnant des équipes sans expérience AMZL dans 2 pays.

**A** : Coordonné 15+ équipes transversales (Immobilier, Construction, Juridique, RH, IT, prestataires). Standardisé les playbooks, outils et processus pour rendre le déploiement reproductible.

**R** : **15 stations livrées en 2 ans.** Playbooks standardisés ensuite déployés à l'échelle EMEA.

---

## OWNERSHIP ⭐

### Anecdote A — SOP expansion SC Amazon 36 mois
**Source** : CV

**S** : Senior Manager SC Long-term Planning & Risk Management, Amazon (2022-2023). Aucun SOP formel n'existait pour piloter l'expansion du réseau supply chain EU à 3 ans.

**T** : Définir le cadre stratégique qui permettrait à Amazon EU de prendre des décisions d'affectation sur 80+ bâtiments avec rigueur et cohérence.

**A** : Défini le SOP d'expansion SC 36 mois. Benchmarké et lancé des projets pilotes sur la réaffectation des bâtiments EU.

**R** : Cadre stratégique adopté pour les décisions d'expansion EU.

---

### Anecdote B — ColdEnergy France (entrepreneur, 2012-2014)
**Source** : CV

**S** : Après des années de grands groupes (Amazon, Dole), j'ai créé ma propre société de conseil et maintenance pour plateformes logistiques réfrigérées.

**T** : Gérer des projets complexes de construction/maintenance pour des clients exigeants (Dole, Fruidor, Lidl Austria) sans les ressources d'un grand groupe.

**A** : Coordonné les prestataires (ingénierie, construction, SAV) en direct. Assumé la responsabilité commerciale et opérationnelle.

**R** : **2M€ de CA**, projets livrés dans les délais et budgets pour des clients EMEA.

---

## EARN TRUST ⭐

### Anecdote A — Collaboration multiculturelle EMEA
**Source** : Forte 2019, 2020

**S** : Chez Amazon, j'ai travaillé avec des équipes dans 10+ pays (FR, UK, DE, IT, ES, RO, LU, DK...).

**T** : Obtenir la coopération de parties prenantes sans lien hiérarchique direct, dans des contextes culturels très différents.

**A** : Approche systématique : comprendre le besoin de l'autre avant de proposer une solution, adapter le style de communication selon l'interlocuteur.

**R** : Feedback Forte 2020 : *"Amazing ability of consistently collaborating well with colleagues from diverse countries and backgrounds. His patience with his peers and clients allow him to provide clear assessments — no matter the audience."* Forte 2019 : *"Multi-cultural and multi-lingual with excellent cross-cultural ability."*

---

### Anecdote B — DD Intake process (Amazon Real Estate)
**Source** : Forte 2021

**S** : L'intake des demandes de Due Diligence était informel et chronophage — les équipes Real Estate ne savaient pas où en étaient leurs dossiers.

**T** : Créer un processus d'intake structuré, adopté par les équipes internes et les clients.

**A** : Conçu le DD Intake form, formalisé le processus, formé les équipes.

**R** : Forte 2021 peer feedback : *"The introduction and improvement of the DD intake progress is a good example [of customer focus]. He also listens to customers needs, working on solutions to prioritise critical path activity whilst maintaining workload churn."*

---

## HAVE BACKBONE; DISAGREE AND COMMIT

### Anecdote A — Andon Cord DCT1 Barcelona *(voir Bias for Action A)*
Même histoire — angle différent : j'ai contredit le consensus implicite du "Go" malgré la pression des délais et des coûts déjà engagés.

*"I made the decision to pull the Andon cord and delay the launch by at least 24h."* — Writing Exercise 2022

---

## DIVE DEEP ⭐

### Anecdote A — Sparklines for Excel : apprentissage VBA from scratch
**Source** : Writing Exercise 2014, 2022

*"After extensive research and despite of little experience in programming, I found out that the VBA 'shape' object actually offers plenty of properties..."*

J'ai appris le VBA sur le tas en décomposant un graphique composant par composant — chaque ligne, chaque rectangle, chaque point. Forte 2023 peer : *"inane ability to deed dive, manage complex data and define root cause."*

---

## LEARN AND BE CURIOUS

### Anecdote A — Sparklines for Excel + Edward Tufte
Inspiré par *The Visual Display of Quantitative Information* de Tufte, j'ai appliqué ses principes de data viz minimaliste à un contexte opérationnel inattendu. Forte 2023 manager : *"right level of Learn & Be Curious as he demonstrated in all new areas he jumped in this year."*

---

## INSIST ON THE HIGHEST STANDARDS

### Anecdote A — SHIELD : chaque composant justifié
*"Given the reduced size of the charts, every individual component of the graphic had to be carefully thought: Is this line absolutely necessary? What information does this line provide?"* — éthique de conception appliquée à SHIELD et à SfE.

Forte 2021 directs : *"Fabrice dives deep on every process and every product he and his team delivers because he insists on higher standards. He simplifies and expedites the processes while he increases the quality of final product."*

---

## FRUGALITY

### Anecdote A — 550k€ économies CS, Colis Privé
Réduction de 20% du budget CS sans réduction d'effectifs ni dégradation de service. Déployé des solutions IA/RPA plutôt que d'embaucher.

### Anecdote B — Dole Romania : restructuration 5 sites, -50% effectifs
Post-acquisition, réhabilitation de 2 sites tout en réduisant les coûts de personnel de moitié.

---

## THINK BIG

### Anecdote A — Amazon SC 36-month expansion SOP, 80+ bâtiments EU
Redéfinir la stratégie d'utilisation du réseau de bâtiments Amazon EU sur 3 ans. Pas un projet opérationnel — une réflexion stratégique sur la topologie du réseau SC à l'échelle continentale.

---

## ARE RIGHT, A LOT

### Anecdote A — Andon Cord DCT1 Barcelona
La décision de retarder le lancement a été prise sur jugement, sans certitude — et s'est avérée correcte. La fibre WiMAX commandée est arrivée 1 mois après le lancement (comme anticipé). La 4G aurait effectivement été insuffisante pendant le ramp-up.

---

## CUSTOMER OBSESSION

### Anecdote A — DCT1 : protéger l'expérience client et associate
*"I made the decision to pull the Andon cord... Impacting the customer delivery promise: 5 to 10k parcels might not be sorted."* La décision prioritaire était de ne pas exposer les clients à un risque de livraison, même au coût d'un retard.

### Anecdote B — Colis Privé : performance externe client
Accountable pour la performance client sur 90M colis/an. Réduction des coûts CS tout en maintenant la qualité de service.

---

## HIRE AND DEVELOP THE BEST

### Anecdote A — Équipe DD Amazon : montée en compétences
Formation et adoption de SHIELD par l'ensemble des parties prenantes. Forte 2021 : *"Fabrice has transformed and grown the due diligence team through 2020."* Forte 2019 : *"Considering his skills and experience accumulated in different roles, that Fabrice is a candidate for a position in which he can manage a team directly."*

### Anecdote B — Infarm : équipe de 16 ingénieurs
*"Conducted training and mentoring programs to elevate team capabilities and skills."* — équipe internationale sur 4 pays EU.

---

## Notes d'utilisation

**Pour les entretiens Amazon** : utiliser le format STAR strict. Avoir des chiffres précis en tête.

**Pour les entretiens non-Amazon** : adapter la terminologie (supprimer "Andon cord", "ATROPS", remplacer par des termes sectoriels).

**Anecdotes les plus polyvalentes** (couvrent plusieurs LPs simultanément) :
1. **DCT1 Barcelona** : Bias for Action + Have Backbone + Ownership + Deliver Results + Customer Obsession
2. **SfE / SHIELD** : Invent and Simplify + Dive Deep + Learn and Be Curious + Insist on Highest Standards
3. **550k€ Colis Privé** : Deliver Results + Frugality + Invent and Simplify (RPA/IA)
