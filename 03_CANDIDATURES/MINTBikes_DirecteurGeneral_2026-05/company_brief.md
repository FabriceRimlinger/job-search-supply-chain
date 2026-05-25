# Company Brief — MINT Bikes

## Secteur et positionnement

Spécialiste français du vélo reconditionné haut de gamme. Marché : mobilité douce + économie circulaire.
Modèle : sourcing vélos d'occasion via algorithme propriétaire → reconditionnement 100+ points de contrôle → revente B2C avec garantie 12 mois.
Prix moyen 1 500€ moins cher qu'un vélo neuf équivalent. 113 kg CO2 évité par vente.

## Chiffres clés (2026)

- ~40 collaborateurs (14 en oct. 2023 dont 4 mécaniciens)
- ~150 vélos achetés/revendus par mois en 2023 → cible 10 000/an (x5)
- CA estimé ~10M€ → objectif 20M€ en 18 mois
- 200 boutiques partenaires en France
- Levée de fonds : 3M€ (oct. 2023 | MTF, Blast, BPI France, CIC, BNP)
- Ambition : leader du vélo reconditionné en France (pas d'expansion internationale à court terme)

## Fondateurs et gouvernance

### Jules Thevenod — Co-fondateur & CEO (Président)
- linkedin.com/in/julesthevenod
- Né ~2000, ~25 ans en 2026 - fondateur à 21 ans
- **Formation** : EDHEC Business School, Finance / Commerce (2018-2023) - profil finance/business, pas opérationnel
- **Expériences avant MINT** : Kiss Studio, Planet Fitness Group, stages sportifs/multisports
- **Traits** : résilience assumée (podcast "La résilience pour réussir", 2024), esprit entrepreneurial précoce, face publique de MINT, levée 3M€ menée personnellement
- **Ce qu'il cherche dans le DG** : un exécutant opérationnel pour traduire la vision en machine industrielle. Son profil finance/commercial a besoin d'un ops partner, pas d'un concurrent.
- **Angle pour Fabrice** : Jules a ~30 ans de moins. Le respect mutuel se construit sur la complémentarité (vision Jules / exécution Fabrice), pas sur la hiérarchie d'âge. À adresser frontalement en entretien.

### Rodolphe Cadart — Co-fondateur
- linkedin.com/in/rodolphe-cadart-47445729
- Né le 8 août 1978, ~47 ans en 2026 - même génération que Fabrice (55 ans)
- **Parcours tennis professionnel** : classé ~150e ATP, quarts de finale Australian Open juniors 1995, quarts de finale Open 13 Marseille 2003 (ATP 250, battu Mirnyi classé 45e mondial), 15 titres ITF
- **Après le tennis** : Diplôme fédéral entraîneur de haut niveau (2010), fondateur de la **Cadart Country Tennis Academy** au Country Club d'Aix-en-Provence (2014 - activité en parallèle de MINT)
- **Rôle chez MINT** : co-fondateur historique, mais double activité (académie de tennis + MINT) = probablement moins présent dans les opérations quotidiennes. Rôle d'associé/mentor plus que de manager opérationnel.
- **Ce qu'il apporte** : réseau local Aix-en-Provence, crédibilité sport de haut niveau, posture entrepreneur-athlète cohérente avec la marque MINT
- **Angle pour Fabrice** : profil sportif de haut niveau, exigence de performance, culture du résultat - terrain commun avec Fabrice (alpinisme, cyclisme compétiteur). Pas de tension hiérarchique attendue.

### Seb et David — Associés
- Fondateurs de **Voyage Privé** (e-commerce voyage, scale-up française notable) et **Kiss Studio**
- Rôle : investisseurs opérationnels / board, apport d'expérience scale-up e-commerce française
- Voyage Privé = référence en e-commerce B2C à forte croissance - leur lecture du modèle MINT est experte

### Structure de gouvernance cible
- Binôme opérationnel : **Jules (Président/vision) + Fabrice (DG/exécution)**
- Rodolphe : associé fondateur, moins opérationnel
- Seb & David : board / conseil stratégique
- Décision finale sur le recrutement DG : Jules (confirmé dans l'annonce "binôme avec Jules")

## Modèle financier et risques structurels

MINT opère en **buy-recondition-sell** (achat ferme aux particuliers, pas de marketplace). Ce modèle crée des risques financiers significatifs à l'échelle cible :

- **Capital immobilisé** : à 833 vélos/mois, avec un cycle achat→vente de 3-6 semaines et un coût total par vélo (achat + reconditionnement) de ~800-1 300€, le WIP + stock représente potentiellement 1,5 à 3M€ de trésorerie immobilisée en permanence. Mise en tension forte avec une levée de 3M€ totale.
- **Risque saisonnier** : forte saisonnalité des ventes (mars-juillet vs nov-janv). Si le sourcing ne l'anticipe pas, le stock s'emballe en automne/hiver avec des vélos qui déprécient.
- **Risque de mix** : surachats d'un segment (ex. VTT) si la demande se déplace vers le gravel ou le VAE - stock bloqué, marge rongée.
- **Erreur de valorisation à l'achat** : l'algorithme de sourcing fixe le prix d'achat. S'il surestime la valeur de revente, la marge est négative. Risque d'autant plus fort à volume industriel.
- **Délai de paiement vendeur** : les avis TrustPilot signalent des retards de paiement aux vendeurs particuliers - symptôme d'un flux de trésorerie tendu ou d'un process de rachat non structuré.
- **Risque juridique vélos volés (recel)** : les CGR MINT reposent sur une déclaration sur l'honneur + copie d'identité. Or depuis juillet 2021 (Loi LOM), tout professionnel de la vente de vélos d'occasion a l'obligation légale de vérifier l'immatriculation BICYCODE/FNUCI avant achat. Absence de vérification systématique = risque de recel involontaire (Art. 321-1 Code pénal, 5 ans + 375 000€). À 150 vélos/mois c'est gérable manuellement ; à 833/mois, il faut une intégration API FNUCI dans le workflow d'achat. C'est un chantier compliance/IT prioritaire pour le DG entrant.

**Analogie pertinente dans le profil Fabrice** : Dole Europe - import de bananes à prix ferme, stockage en mûrisseries (cycle incompressible, comme le reconditionnement), revente à la GD avec contrainte de saisonnalité et de mix. Vessel scheduling = optimisation du flux d'approvisionnement pour éviter la saturation des entrepôts. Amazon SC Planning = gestion des actifs (80+ bâtiments) et scénarios d'expansion long terme.

---

## Enjeux opérationnels critiques (pour le futur DG)

1. **Industrialisation du flux vélos** : passer de ~150 à 833 vélos/mois sans dégrader la qualité de reconditionnement. Processus, WMS, gestion des stocks, capacité atelier.
2. **Dimensionnement du Customer Service** : à volume x5, les contacts acheteurs (SAV garantie, retours, questions pré-achat) et vendeurs (processus de reprise, valorisation, prise en charge) explosent. Sans outillage ni processus adaptés, c'est le premier poste qui déraille et le premier poste de coût qui s'emballe. Fabrice a réduit le CS de 20% (550k€/an) chez Colis Privé via RPA, call bots et IA forecasting - tout en améliorant le NPS de 30%.
3. **Recrutement et formation des mécaniciens** : passer de 4 à 20-30 mécaniciens certifiés est un vrai goulet d'étranglement. Compétence rare, formation longue, risque qualité fort si on brade l'onboarding. Fabrice a construit des programmes de formation et des playbooks de lancement (AMZL, Infarm) - structurer l'onboarding mécanicien est un chantier immédiat.
4. **Logistique livraison à l'échelle** : 833 vélos/mois livrés en 4-7 jours sur toute la France = carrier management, emballage spécifique (vélos), WMS, taux de casse en transit, gestion des retours. C'est le coeur de métier de Fabrice (20 ans, last mile, Amazon, Colis Privé). Différenciant direct.
5. **Structuration des équipes** : x3 en effectif prévu. Organisation à concevoir, recrutement, onboarding, délégation, autonomie des managers.
6. **Pilotage data et KPIs** : l'algorithme de sourcing est un actif. La culture data doit s'étendre à toutes les fonctions (opérations, commercial, SAV).
7. **Réseau partenaires** : 200 boutiques = un réseau à piloter, former, animer, mesurer.
8. **Atteinte budgets** : 20M€ CA en 18 mois = pression forte sur l'exécution commerciale et opérationnelle conjointe.

## Concurrents

- **Upway** : principal concurrent direct, spécialisé VAE uniquement - MINT se différencie par gamme complète (VTT, route, urbain, VAE)
- Marketplaces occasion (leboncoin, vinted) : différenciation par garantie, reconditionnement certifié, SAV professionnel
- Vélos neufs grande distribution : différenciation prix (-1 500€ en moyenne)

## Valeurs et culture

- Mission environnementale : substituer le neuf, réduire l'empreinte carbone
- Accessibilité au vélo de qualité (économie circulaire)
- Scale-up en croissance rapide : agilité, prise de décision terrain, tout-faire-avec-peu
- Fondateur jeune, esprit entrepreneurial, proximité des équipes

## Fit culture — Profil Fabrice (PAPI-I)

**Alignements forts :**
- Builder de processus et d'outils data (SHIELD Amazon, BI Colis Privé) = exactement ce qu'une scale-up passant à l'industrialisation doit construire
- Leadership par adhésion et co-construction (PAPI dim. 1) = adapté au binôme DG-fondateur, pas de hiérarchie lourde
- Innovation + exécution simultanée (PAPI dim. 3) = culture scale-up par excellence
- **Passion cyclisme authentique** : ancien compétiteur Elite, VTT, routier - crédibilité produit rare et différenciante pour MINT
- Autonomie forte + reporting proactif (Gantt, plans B) = fondateur rassuré sans être étouffé

**Points de vigilance à préparer en entretien :**
- Adaptation de la grande structure à la scale-up (tout est à construire, ressources limitées) : valoriser ColdEnergy France (Owner 2M€, seul avec ses mains) comme preuve d'agilité
- Jules ~25 ans + Fabrice 55 ans : dynamique fondateur/DG à adresser frontalement - pas une menace mais un apport de maturité opérationnelle
- Franco-français vs profil multiculturel : neutraliser en se concentrant sur le marché cible (France), pas un sujet MINT

---

## Questions stratégiques pour l'entretien (à poser à Jules)

Ces questions montrent que tu as fait le diagnostic avant d'entrer dans la salle. Ne pas toutes poser - choisir 2-3 selon le contexte.

1. **Sur le capital et la trésorerie** : "Quel est votre cycle moyen achat-vente aujourd'hui, et comment gérez-vous le pic de stock en dehors de la saison vélo ? Avez-vous des lignes de crédit court terme pour absorber le WIP à l'échelle cible ?"
2. **Sur l'algorithme de sourcing** : "Comment mesurez-vous la précision de valorisation à l'achat ? Quel est votre taux de vélos vendus en dessous du prix cible ?"
3. **Sur la formation mécaniciens** : "Quel est votre référentiel de reconditionnement aujourd'hui - checklist standardisée, certification interne ? Comment formez-vous un nouveau mécanicien avant qu'il touche un vélo seul ?"
4. **Sur le SAV** : "Quel est votre taux de contacts SAV par vélo vendu, et quelle est votre cible ? Avez-vous un process de résolution distinct pour les pannes sous garantie vs les insatisfactions ?"
5. **Sur le flux vendeur** : "Quel est votre délai moyen de paiement des particuliers qui vous vendent un vélo ? C'est un point de friction qui impacte votre réputation de sourcing."
6. **Sur la saisonnalité** : "Comment planifiez-vous vos achats en octobre-novembre pour ne pas saturer l'entrepôt pendant l'hiver ?"
7. **Sur la compliance anti-recel** : "Votre process d'achat inclut-il une vérification systématique BICYCODE/FNUCI avant chaque reprise ? À 800+ vélos par mois, une intégration API est indispensable - avez-vous déjà ce chantier en roadmap ?"
