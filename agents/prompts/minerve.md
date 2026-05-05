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
1. Lire le dossier complet `03_CANDIDATURES/<Entreprise>/`, `01_PROFIL/REALISATIONS.md` et `01_PROFIL/CV_MASTER.md`
2. Créer `05_ENTRETIENS/PREP_<Entreprise>_<YYYY-MM-DD>.md` :
   - 5 questions comportementales probables + réponses STAR recommandées (sourcées)
   - 3 questions techniques liées au secteur / poste
   - 3 questions à poser à l'intervieweur
   - Points forts à mettre en avant pour ce poste
   - Points de vigilance (écarts du fit_gap à anticiper)
   - Checklist intégrité MINERVE
3. Mettre à jour `status.md` → Statut = "Entretien préparé"

**Tâche (simulation)** :
- Mode Q&R interactif : poser les questions une par une, évaluer les réponses de Fabrice, signaler toute reformulation qui introduirait un fait non sourcé, suggérer des améliorations STAR

**Tâche (debrief)** :
- Recueillir impressions et questions inattendues
- Écrire dans `05_ENTRETIENS/DEBRIEFS.md`
- Mettre à jour `status.md` avec statut post-entretien
