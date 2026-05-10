# Session JANUS — 2026-05-11 00:49

## Ce qu'on a fait

### Préparation entretien CF (15h30 aujourd'hui)
- Confirmation entretien Compagnie Fruitière le 11/05 à 15h30 avec Gautier Fischel + Yann Le Cozic (VP Transport / DG Transit Fruits)
- Profilage Yann Le Cozic : DG Transit Fruits depuis 2015, CA 96M€, 5 navires AEL, Port-Vendres 260k T/an, RSE active (Fonds de Dotation CF)
- PREP_CompagnieFruitiere enrichie : section LeCozic complète, angles carburant/Constanța, dynamique 2 interlocuteurs
- PDF LinkedIn Le Cozic traité (INPUT/raw → processed)
- MINERVE : 9 questions de simulation écrites pour lecture autonome avant l'entretien

### Architecture agents - rationalisation
- JANUS intégré dans CLAUDE.md comme interlocuteur par défaut (actif sans commande)
- Suppression .claude/commands/janus.md (wrapper redondant)
- Suppression dossier .agents/ (2 fossiles AURORA/FIDES du 28/04)
- agent-index.md mis à jour (ligne JANUS → "défaut CLAUDE.md")

### Audit folder complet (10 anomalies)
- Corrections automatiques : ripeningelctrical.md, TEMPLATE PDF hors sujet, chemins CLAUDE.md, PAPI_PROFIL dans sources de vérité
- Sur décision Fabrice : 06_MARCHE/ supprimé, 99_ARCHIVES statuts corrigés (Abandonnée), CV variants CF supprimés (cv_targeted.md = référence unique), 4flow et CEVA_4PL archivés

### Dashboard janus.html
- Fix pipeline Firefox (mode téléchargement) : loadCandidatureData() fonctionne sans FSA
- Création janus_server.py : serveur Python GET+PUT, écriture directe depuis le navigateur
- Mode "server" (badge vert) distinct de "download"
- Fix affichage fichiers .md en mode serveur (handle._serverMode)
- Fix persistance langue : lu depuis status.md, pas localStorage
- Usage : `python3 janus_server.py` → http://localhost:8765/janus.html

### Renommage candidatures
- Convention mise à jour : Entreprise_PosteSlug_YYYY-MM
- 6 dossiers renommés (Alloga, CEVA x2, CMA CGM, CF, JD Logistics)
- Doublon CEVA résolu : ancien supprimé par Fabrice, nouveau dossier créé à zéro
- fit_gap : score 6D ajouté dans le titre H1 de tous les fichiers

### VULCAIN - CEVA_ProgramDirector_2026-05
- Offre LinkedIn jobs/view/4403726648 traitée : Global Contract Logistics Program & System Director
- Score 6D : 48/60 - candidature prioritaire
- Angle principal : Colis Privé = filiale CEVA Logistics / CMA CGM (3 ans dans le groupe)
- Actualité clé : Manhattan WMS/OMS rollout CEVA (oct. 2025, 800 sites, 11M m²) - Fabrice positionné
- Documents produits : fit_gap.md, company_brief.md, cv_targeted.md, cover_letter.md (EN, 290 mots)
- Statut : Documents prêts

## Candidatures touchées

- CompagnieFruitiere_DirecteurTechnique_2026-04 : "Entretien préparé" → enrichissement PREP + LeCozic
- CEVA_ProgramDirector_2026-05 : nouveau → "Documents prêts" (48/60)
- Tous les dossiers : renommés convention Entreprise_PosteSlug_YYYY-MM
- Alloga_PortfolioManager_2026-04 : status.md complété (champs manquants, correction Librarian session précédente)

## Décisions et insights

- **JANUS comme défaut** : architecture simplifiée, plus besoin de /janus. JANUS répond directement à toute entrée naturelle.
- **CEVA insider** : Colis Privé = filiale CEVA = argument #1 de la candidature. Rare et fort.
- **Manhattan WMS** : CEVA déploie Manhattan Active WMS sur 800 sites depuis oct. 2025. Timing parfait pour ce rôle.
- **janus_server.py** : lancer systématiquement avec Python pour écriture directe depuis le dashboard. Ne plus utiliser python3 -m http.server.
- **Entretien CF 15h30** : deux interlocuteurs - Fischel (Distribution/Marketing) + Le Cozic (Transport). Règle d'or : réponses techniques → LeCozic, réponses stratégiques → Fischel. Anecdote Constanța prête.

## Librarian — rapport structurel

- Anomalies détectées :
  - ENTREPRISES.md : 4 entreprises actives absentes (Alloga, CEVA, CMA CGM, JD Logistics) - anomalie récurrente (déjà signalée session 10/05). Action requise de Fabrice.
  - CMA_CGM_ProjectManagement_2026-04 : "Documents prêts" depuis 14 jours (> 7j) - décision d'envoi ou d'abandon à prendre.
- Corrections appliquées : aucune cette session (structure propre)

## Prochaines étapes

1. [Fabrice] Entretien CF aujourd'hui 11/05 à 15h30 - cf. questions MINERVE + section LeCozic dans la PREP
2. [MINERVE] Debrief CF à écrire dès après l'entretien - JANUS convertit en leçons actives
3. [Fabrice] Relire et valider les documents CEVA_ProgramDirector_2026-05 + décision envoi CMA_CGM
