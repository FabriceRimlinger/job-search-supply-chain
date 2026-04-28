# Catalogue d'anecdotes - Amazon Leadership Principles

> Sources : Writing Exercises Amazon (2014, 2022), Forte Reviews (2019-2023), CV.
> Format STAR : Situation → Task → Action → Result.
> Usage : réponses entretien comportemental, LM, pitch.

## Recherche rapide par tag

```bash
# Filtrer par LP
grep -A 20 "#bias-for-action" CATALOGUE_ANECDOTES.md

# Filtrer par secteur
grep -l "#pharma\|#cold-chain" CATALOGUE_ANECDOTES.md

# Filtrer par type de situation
grep -B 2 "#judgment-call\|#crisis" CATALOGUE_ANECDOTES.md

# Anecdotes avec chiffres forts
grep -B 2 "#budget-40m\|#savings-550k\|#100k-downloads" CATALOGUE_ANECDOTES.md
```

## Taxonomie des tags

| Catégorie | Tags disponibles |
|-----------|-----------------|
| **LP principal** | #invent-simplify #bias-for-action #deliver-results #ownership #earn-trust #have-backbone #dive-deep #learn-curious #insist-standards #frugality #think-big #are-right #customer-obsession #hire-develop |
| **Entreprise** | #amazon #colis-prive #dole #infarm #pomona #coldenergy |
| **Type** | #innovation #judgment-call #crisis #launch #m-and-a #restructuring #planning #tool-build #cost-reduction #compliance |
| **Compétences** | #data #bi #vba #automation #rpa #ai #escalation #negotiation #pm #change-management |
| **Périmètre** | #emea #eu #france #multi-country #team-25 #team-16 #team-10 #budget-40m |
| **Secteur** | #logistics #last-mile #pharma #supply-chain #real-estate #cold-chain #agri #e-commerce #regulated |
| **Impact** | #savings-550k #cost-20pct #tasks-40pct #100k-downloads #15-stations #2m-revenue |
| **Format entretien** | #polyvalent #amazon-only #non-amazon #chiffres-forts #leadership-solo |

---

## INVENT AND SIMPLIFY ⭐ (LP #1 - cité dans 100% des Forte reviews)

### Anecdote A - Sparklines for Excel (SfE)
**Tags** : #invent-simplify #dive-deep #learn-curious #deliver-results · #amazon #dole · #innovation #tool-build · #data #vba #bi · #emea · #logistics #supply-chain · #100k-downloads · #polyvalent #chiffres-forts
**Source** : Writing Exercises 2014 & 2022, Forte reviews

**S** : En 2007, Technical Projects Manager chez Dole Europe. Reporting intensif sur portefeuille de projets (KPIs, P&L). Problème récurrent : formatage des graphiques Excel = perte de temps massive avant même d'analyser les données.

**T** : Créer un outil qui simplifie et accélère le reporting sans dépendre d'un designer. Aucun outil du marché ne répondait au besoin.

**A** : Inspiré par Edward Tufte (*The Visual Display of Quantitative Information*), j'ai conçu de zéro une bibliothèque VBA de formules Excel générant des micro-graphiques directement dans une cellule. Apprentissage du VBA sur le tas, en testant chaque composant graphique ("est-ce que cette ligne est vraiment nécessaire ?"). 14 types de graphiques créés : LineChart, BulletChart, Pareto, BoxPlot, Gantt, TreeMap, BeanPlot...

**R** : "Sparklines for Excel" (SfE) est un projet open-source **téléchargé plus de 100 000 fois**, encore utilisé dans des PME et grandes entreprises. Utilisé quotidiennement chez Amazon pour les rapports AMZL (IT, ES) et pour wireframer les dashboards avant de passer à PowerBI.

**LP secondaires** : Dive Deep, Learn and Be Curious, Deliver Results

---

### Anecdote B - Plateforme SHIELD (Amazon Real Estate Due Diligence)
**Tags** : #invent-simplify #customer-obsession #insist-standards #earn-trust · #amazon · #innovation #tool-build #compliance · #data #bi #pm · #emea #budget-40m #team-10 · #real-estate #supply-chain #regulated · #polyvalent #chiffres-forts
**Source** : CV, Forte 2020 & 2021

**S** : Head of Technical & Environmental Real Estate Due Diligence, Amazon (2018-2021). 1 200+ Due Diligence EMEA/an, budget 40M€/an, 10 risk managers + 30+ consultants. Reporting fragmenté - aucune vision consolidée en temps réel.

**T** : Concevoir une plateforme BI centralisée, adoptée par toutes les parties prenantes EMEA, sans imposer une formation lourde.

**A** : Conçu SHIELD de A à Z - architecture des données, logique de reporting, UX. Déployé progressivement avec formation intégrée. Priorité à la simplicité d'usage.

**R** : Adoption totale par toutes les parties prenantes Amazon EMEA. *"Fabrice has revolutionised how the team operates, using his knowledge to help the team leverage data to get to the right answer at pace."* (Forte 2021). Accélération significative des délais de DD.

**LP secondaires** : Customer Obsession, Insist on Highest Standards, Earn Trust

---

### Anecdote C - Dashboard SNN4 (Amazon SC Planning, 2023)
**Tags** : #invent-simplify #customer-obsession · #amazon · #tool-build #compliance · #data #bi · #eu · #supply-chain #regulated · #non-amazon
**Source** : Forte 2023

**S** : Program Manager Supply Chain, Amazon (2022-2023). Problème de drop-offs sur les sélections de sites - les compliance blockers EU n'étaient pas visibles en temps réel.

**T** : Créer un mécanisme permettant de détecter et réduire les blocages compliance avant qu'ils ne dérèglent les sélections.

**A** : Guidé l'équipe dans la conception du dashboard SNN4. Facilité les échanges entre équipes business EU et programme pour s'assurer que le mécanisme couvrait les bons cas d'usage.

**R** : *"Guided the team... reducing EU compliance blockers and unblock selection for customers."* (Forte 2023)

---

## BIAS FOR ACTION ⭐

### Anecdote A - Andon Cord DCT1 Barcelona (AMZL Launch 2017)
**Tags** : #bias-for-action #have-backbone #ownership #deliver-results #are-right #customer-obsession · #amazon · #judgment-call #crisis #launch · #escalation #pm · #eu #multi-country · #logistics #last-mile #e-commerce · #polyvalent #chiffres-forts #leadership-solo
**Source** : Writing Exercise Amazon 2022 A

**S** : Sr Launch Manager, AMZL. Go/No Go call à 18h, 6h avant le lancement de la Delivery Station DCT1 à Barcelone. Signal 4G chute à quasi zéro la nuit - précisément pendant le tri (minuit-7h). 5 000 à 10 000 colis à risque. Pic 2017 compromis.

**T** : Décision sous pression, sans données complètes : lancer, adapter, ou retarder. Chaque option a des coûts importants (associates mobilisés, partenaires prêts).

**A** : Tiré l'Andon cord, repoussé le lancement de 24h. Simultanément : (1) retiré DCT1 d'ATROPS, (2) maintenu les associates en formation et "virtual deliveries", (3) pensé hors du cadre - le FC BCN2 était dans le même bâtiment. Escaladé de Madrid à Seattle en quelques heures pour partager une fibre optique BCN2. À 7h le lendemain : trou de 5cm percé dans un mur de 40cm, ethernet tiré.

**R** : À 12h, réseau AMZL opérationnel avec *"la meilleure connexion broadband jamais déployée pour un DS launch"*. Lancement J+1, zéro impact client. La fibre WiMAX est arrivée 1 mois plus tard - comme anticipé.

**LP secondaires** : Have Backbone, Ownership, Deliver Results, Are Right A Lot, Customer Obsession

---

### Anecdote B - Intégration Milee post-acquisition (Colis Privé, 2023)
**Tags** : #bias-for-action #ownership #deliver-results · #colis-prive · #m-and-a #change-management · #negotiation #pm · #france #team-25 · #logistics #last-mile · #polyvalent
**Source** : CV

**S** : Director of Transformation, Colis Privé (2023-2024). Acquisition de Milee (300 chauffeurs). Nécessité d'intégrer 300 personnes rapidement sans perturber 250 000 livraisons/jour.

**T** : Conduire l'intégration juridique, opérationnelle et humaine en quelques mois, sans interruption de service.

**A** : Mené les négociations juridiques, modélisé le P&L, aligné les équipes transversales, maintenu l'exécution opérationnelle pendant toute la transition.

**R** : 300 employés intégrés avec continuité opérationnelle totale.

---

## DELIVER RESULTS ⭐

### Anecdote A - 550k€ d'économies Service Client (Colis Privé, 2024)
**Tags** : #deliver-results #frugality #invent-simplify · #colis-prive · #cost-reduction #automation · #rpa #ai #data #team-25 · #france · #logistics #e-commerce · #savings-550k #cost-20pct #tasks-40pct · #polyvalent #chiffres-forts
**Source** : CV

**S** : Director Business Excellence, Colis Privé. Activité en hausse de +7,5%, pression sur les coûts.

**T** : Réduire le budget Service Client sans dégrader la qualité de service.

**A** : Déployé un programme d'automatisation (AI forecasting, RPA, call bots) sur les tâches manuelles répétitives. Piloté 25 personnes sur la performance opérationnelle et client.

**R** : Budget CS réduit de **20% = 550k€/an d'économies**. Tâches manuelles réduites de **40%**. Délai de traitement amélioré.

---

### Anecdote B - 15 stations AMZL en 2 ans (Italie et Espagne)
**Tags** : #deliver-results #ownership #think-big · #amazon · #launch #planning · #pm #escalation · #eu #multi-country · #logistics #last-mile · #15-stations · #polyvalent #chiffres-forts
**Source** : CV

**S** : Head of AMZL Expansion South EU, Amazon Logistics (2016-2018). Mission pionnière : déployer le réseau last mile Amazon en Italie et Espagne, marchés sans infrastructure AMZL.

**T** : Lancer 15 stations en 2 ans en coordonnant des équipes sans expérience AMZL dans 2 pays.

**A** : Coordonné 15+ équipes transversales. Standardisé les playbooks, outils et processus pour rendre le déploiement reproductible.

**R** : **15 stations livrées en 2 ans.** Playbooks déployés ensuite à l'échelle EMEA.

---

## OWNERSHIP ⭐

### Anecdote A - SOP expansion SC Amazon 36 mois
**Tags** : #ownership #think-big #deliver-results · #amazon · #planning · #pm · #eu #multi-country · #supply-chain · #non-amazon
**Source** : CV

**S** : Senior Manager SC Long-term Planning & Risk Management, Amazon (2022-2023). Aucun SOP formel pour piloter l'expansion SC EU à 3 ans.

**T** : Définir le cadre stratégique permettant à Amazon EU de prendre des décisions sur 80+ bâtiments avec rigueur.

**A** : Défini le SOP d'expansion SC 36 mois. Benchmarké et lancé des projets pilotes sur la réaffectation des bâtiments EU.

**R** : Cadre stratégique adopté pour les décisions d'expansion EU.

---

### Anecdote B - ColdEnergy France (entrepreneur, 2012-2014)
**Tags** : #ownership #deliver-results #frugality · #coldenergy · #planning · #pm #negotiation · #emea · #cold-chain #pharma #agri · #2m-revenue · #non-amazon
**Source** : CV

**S** : Création de ColdEnergy France, société de conseil et maintenance pour plateformes logistiques réfrigérées.

**T** : Gérer des projets de construction/maintenance pour des clients exigeants (Dole, Fruidor, Lidl Austria) sans les ressources d'un grand groupe.

**A** : Coordonné les prestataires (ingénierie, construction, SAV) en direct. Assumé la responsabilité commerciale et opérationnelle.

**R** : **2M€ de CA**, projets livrés dans les délais et budgets pour des clients EMEA.

---

## EARN TRUST ⭐

### Anecdote A - Collaboration multiculturelle EMEA
**Tags** : #earn-trust #hire-develop · #amazon · #change-management · #emea #multi-country · #logistics #supply-chain · #polyvalent #non-amazon
**Source** : Forte 2019, 2020

**S** : Chez Amazon, travail avec des équipes dans 10+ pays (FR, UK, DE, IT, ES, RO, LU, DK...).

**T** : Obtenir la coopération de parties prenantes sans lien hiérarchique direct, dans des contextes culturels très différents.

**A** : Approche systématique : comprendre le besoin de l'autre avant de proposer une solution, adapter le style de communication selon l'interlocuteur.

**R** : *"Amazing ability of consistently collaborating well with colleagues from diverse countries and backgrounds."* (Forte 2020). *"Multi-cultural and multi-lingual with excellent cross-cultural ability."* (Forte 2019)

---

### Anecdote B - DD Intake process (Amazon Real Estate)
**Tags** : #earn-trust #customer-obsession #invent-simplify · #amazon · #tool-build #compliance · #pm · #emea · #real-estate #regulated · #non-amazon
**Source** : Forte 2021

**S** : L'intake des demandes de Due Diligence était informel - les équipes Real Estate ne savaient pas où en étaient leurs dossiers.

**T** : Créer un processus d'intake structuré, adopté par les équipes internes et les clients.

**A** : Conçu le DD Intake form, formalisé le processus, formé les équipes.

**R** : *"The introduction and improvement of the DD intake progress is a good example [of customer focus]."* (Forte 2021)

---

## HAVE BACKBONE; DISAGREE AND COMMIT

### Anecdote A - Andon Cord DCT1 Barcelona *(voir Bias for Action A)*
**Tags** : #have-backbone #bias-for-action #ownership · #amazon · #judgment-call #crisis · #escalation · #eu · #logistics #last-mile · #leadership-solo
Même histoire - angle : contredire le consensus implicite "Go" malgré la pression des délais et coûts déjà engagés.

---

## DIVE DEEP ⭐

### Anecdote A - Sparklines for Excel : apprentissage VBA from scratch
**Tags** : #dive-deep #learn-curious #invent-simplify · #dole #amazon · #innovation #tool-build · #vba #data · #emea · #logistics · #100k-downloads · #amazon-only
**Source** : Writing Exercise 2014, 2022

*"After extensive research and despite of little experience in programming, I found out that the VBA 'shape' object actually offers plenty of properties..."*

J'ai appris le VBA sur le tas en décomposant un graphique composant par composant - chaque ligne, chaque rectangle, chaque point. Forte 2023 : *"inane ability to deed dive, manage complex data and define root cause."*

---

## LEARN AND BE CURIOUS

### Anecdote A - Sparklines for Excel + Edward Tufte
**Tags** : #learn-curious #dive-deep #invent-simplify · #dole · #innovation · #vba #data · #emea · #logistics · #non-amazon
Inspiré par *The Visual Display of Quantitative Information* de Tufte, j'ai appliqué ses principes de data viz minimaliste à un contexte opérationnel. Forte 2023 manager : *"right level of Learn & Be Curious as he demonstrated in all new areas he jumped in this year."*

---

## INSIST ON THE HIGHEST STANDARDS

### Anecdote A - SHIELD : chaque composant justifié
**Tags** : #insist-standards #dive-deep #invent-simplify · #amazon · #tool-build #compliance · #bi #data · #emea #budget-40m · #real-estate #regulated · #amazon-only
*"Every individual component of the graphic had to be carefully thought: Is this line absolutely necessary?"* - éthique de conception appliquée à SHIELD et SfE.

Forte 2021 : *"Fabrice dives deep on every process and every product he and his team delivers because he insists on higher standards."*

---

## FRUGALITY

### Anecdote A - 550k€ économies CS, Colis Privé *(voir Deliver Results A)*
**Tags** : #frugality #deliver-results · #colis-prive · #cost-reduction #automation · #rpa #ai · #france · #logistics · #savings-550k #cost-20pct · #chiffres-forts

### Anecdote B - Dole Romania : restructuration 5 sites, -50% effectifs
**Tags** : #frugality #deliver-results #ownership · #dole · #restructuring #m-and-a · #pm · #multi-country · #agri #cold-chain · #non-amazon
Post-acquisition, réhabilitation de 2 sites (Constanța, Bucarest) tout en réduisant les coûts de personnel de 50%.

---

## THINK BIG

### Anecdote A - Amazon SC 36-month expansion SOP, 80+ bâtiments EU
**Tags** : #think-big #ownership #deliver-results · #amazon · #planning · #pm · #eu #multi-country · #supply-chain · #non-amazon
Redéfinir la stratégie d'utilisation du réseau de bâtiments Amazon EU sur 3 ans - réflexion sur la topologie du réseau SC à l'échelle continentale.

---

## ARE RIGHT, A LOT

### Anecdote A - Andon Cord DCT1 Barcelona *(voir Bias for Action A)*
**Tags** : #are-right #bias-for-action #have-backbone · #amazon · #judgment-call · #escalation · #eu · #logistics #last-mile · #leadership-solo
Décision prise sur jugement, sans certitude - la fibre WiMAX est arrivée 1 mois après le lancement, comme anticipé. La 4G aurait effectivement été insuffisante pendant le ramp-up.

---

## CUSTOMER OBSESSION

### Anecdote A - DCT1 : protéger l'expérience client *(voir Bias for Action A)*
**Tags** : #customer-obsession #bias-for-action · #amazon · #judgment-call #crisis · #escalation · #eu · #last-mile #logistics · #leadership-solo
*"Impacting the customer delivery promise: 5 to 10k parcels might not be sorted."* La priorité était de ne pas exposer les clients, même au coût d'un retard.

### Anecdote B - Colis Privé : performance externe client
**Tags** : #customer-obsession #deliver-results · #colis-prive · #cost-reduction · #team-25 · #france · #logistics #e-commerce · #savings-550k · #polyvalent
Accountable pour la performance client sur 90M colis/an. Réduction des coûts CS tout en maintenant la qualité de service.

---

## HIRE AND DEVELOP THE BEST

### Anecdote A - Équipe DD Amazon : montée en compétences
**Tags** : #hire-develop #earn-trust · #amazon · #change-management · #team-10 #emea · #real-estate #regulated · #non-amazon
Formation et adoption de SHIELD. *"Fabrice has transformed and grown the due diligence team through 2020."* (Forte 2021)

### Anecdote B - Infarm : équipe de 16 ingénieurs EU
**Tags** : #hire-develop #deliver-results · #infarm · #launch #change-management · #team-16 #eu #multi-country · #agri · #non-amazon
*"Conducted training and mentoring programs to elevate team capabilities and skills."* - équipe internationale sur 4 pays EU.

---

## Index rapide - Anecdotes polyvalentes

| Anecdote | LPs couverts | Impact chiffré | Idéal pour |
|----------|-------------|---------------|-----------|
| **DCT1 Barcelona** | Bias · Backbone · Ownership · Deliver · Customer | Lancement J+1, 0 impact | Tout entretien executive |
| **SfE / SHIELD** | Invent · Dive Deep · Learn · Standards | 100k downloads, 40M€ géré | Postes data/transformation |
| **550k€ Colis Privé** | Deliver · Frugality · Invent | 550k€/an, -40% tâches | Postes opérations/coûts |
| **15 stations AMZL** | Deliver · Ownership · Think Big | 15 sites, 2 pays, 2 ans | Postes expansion/programme |
| **Milee 300 employés** | Bias · Ownership · Deliver | 300p intégrés, 0 disruption | M&A, transformation |

**Pour entretiens non-Amazon** : remplacer "Andon cord" → "j'ai stoppé le lancement", "ATROPS" → "le système de routage des colis", "associates" → "équipes".
