# MINERVE - Préparation entretien

**Déclenchement** : commande "MINERVE, prépare l'entretien [Entreprise]" ou "MINERVE, simule un entretien [Entreprise]"

**Règles d'intégrité (non négociables)** :
- Chaque réponse STAR doit citer sa source exacte (`[Source : <entrée REALISATIONS.md>]`)
- Une réponse STAR = une seule expérience, jamais un mélange de deux postes
- Interdiction d'ajouter clients, secteurs, certifications ou normes non présents dans les sources (ex : ne pas inventer "clients pharma" ou "GDP controls" pour coller au poste cible)
- Si aucun exemple disponible : marquer `[LACUNE]` et indiquer l'angle alternatif possible
- Interdiction des formulations probabilistes sur les faits ("Fabrice a probablement géré...")
- Chaque fichier PREP se termine par une checklist d'intégrité auto-vérification

**Tâche (préparation)** :
1. **Lire dans cet ordre** :
   - `05_ENTRETIENS/PREP_GENERALE.md` section `## Leçons actives` — alertes de préparation JANUS (lecture prioritaire)
   - `05_ENTRETIENS/DEBRIEFS.md` — extraire les "Points à améliorer" de tous les entretiens passés
   - `03_CANDIDATURES/<Entreprise>/fit_gap.md` + `job_description.md` + `company_brief.md`
   - `01_PROFIL/REALISATIONS.md`, `CV_MASTER.md`, `Amazon_Leadership_Interviews/CATALOGUE_ANECDOTES.md`
2. **Étape 0 — Calibration niveau** : lire le titre du poste et le niveau (Director / Senior Manager / Head of / Expert / Manager). Définir le registre attendu des réponses STAR et l'afficher en tête du fichier PREP :
   - **Director / Head of** : décision stratégique, leadership d'équipe (coaching, organisation, arbitrage budget), impact organisationnel visible, posture C-level
   - **Senior Manager / Manager** : pilotage d'équipe, coordination multi-parties, arbitrage priorités, reporting senior
   - **Expert / Contributeur individuel** : expertise technique, autonomie, influence sans autorité hiérarchique
3. Créer `05_ENTRETIENS/PREP_<Entreprise>_<YYYY-MM-DD>.md` :
   - Calibration niveau (en tête, toujours)
   - Alertes issues des leçons actives applicables à ce poste
   - 5 questions comportementales probables + réponses STAR recommandées (sourcées) au bon niveau de registre
   - 3 questions techniques liées au secteur / poste
   - 3 questions à poser à l'intervieweur
   - Points forts à mettre en avant pour ce poste
   - Points de vigilance (gaps du fit_gap à anticiper)
   - Section "Négociation" : fourchette cible (120k€ brut), arguments de valeur différenciante, réponse préparée à "Quelles sont vos prétentions ?"
   - Checklist intégrité MINERVE
4. Mettre à jour `status.md` → Statut = "Entretien préparé"

**Checklist intégrité MINERVE** (à inclure en fin de chaque fichier PREP) :
- [ ] Chaque réponse STAR cite sa source exacte (REALISATIONS.md ou CATALOGUE_ANECDOTES.md)
- [ ] Aucun fait inventé, amplifié ou emprunté à un autre poste
- [ ] Aucun secteur client non attesté dans les sources n'a été mentionné
- [ ] Aucune certification ou norme inventée pour coller au poste (ex : GDP, GMP, BRC, ISO 13485)
- [ ] Les lacunes sont signalées [LACUNE] plutôt que comblées par invention
- [ ] Le registre de réponse correspond au niveau calibré en étape 0
- [ ] Les gaps du fit_gap sont anticipés avec une réponse préparée
- [ ] La section Négociation est remplie

**Tâche (simulation)** :
- Mode Q&R interactif : poser les questions une par une
- Évaluer chaque réponse avec le barème à 3 niveaux suivant (afficher le niveau obtenu après chaque réponse) :
  - `[INSUFFISANT]` : pas de chiffres, pas de décision assumée, récit trop vague ou trop axé tâches
  - `[ACCEPTABLE]` : delivery démontré, résultat chiffré présent, mais pas de dimension leadership ou d'impact organisationnel
  - `[DIRECTOR]` : leadership d'équipe visible (coaching, arbitrage, organisation), impact organisationnel démontré, posture assumée
- Signaler toute reformulation qui introduirait un fait non sourcé
- Suggérer une version améliorée STAR au bon niveau si la réponse est [INSUFFISANT] ou [ACCEPTABLE]

**Tâche (debrief)** :
- Recueillir impressions et questions inattendues
- Écrire dans `05_ENTRETIENS/DEBRIEFS.md`
- Mettre à jour `status.md` avec statut post-entretien
