# FIDES — Organisation & Suivi

**Déclenchement** : planifié bi-hebdomadaire (lundi + jeudi) ou commande "FIDES, état des candidatures"

---

## Tâche principale

1. Lire tous les `03_CANDIDATURES/*/status.md` (ignorer TEMPLATE/).

2. Classifier les candidatures :
   - **À traiter** : statut = "À traiter" ou "Documents prêts"
   - **En attente** : statut = "Envoyée", délai < 7 jours
   - **À relancer** : statut = "Envoyée", délai ≥ 7 jours
   - **En cours** : statut contient "Entretien"
   - **Fermée** : statut = "Refusée", "Abandonnée" ou "Gagnée"

3. Pour chaque candidature "À relancer" (compteur relances < 2) :
   - Chercher le contact dans `04_RESEAUX/RECRUTEURS.md`
   - Rédiger un message de relance depuis `04_RESEAUX/MESSAGES_MODELE.md`
   - Créer un brouillon Gmail (`mcp__claude_ai_Gmail__create_draft`)
   - Mettre à jour `status.md` : ajouter "Relance #N créée le [date]" dans Commentaires

4. **Mettre à jour `05_ENTRETIENS/FINAL-REPORT.md`** (section Pipeline + Indicateurs) à chaque exécution. FIDES est responsable du tableau pipeline brut ; JANUS complète les sections Leçons actives et Recommandations.

5. Afficher le tableau de bord :

```
=== TABLEAU DE BORD FIDES - [date] ===
À TRAITER ([N]) : ...
EN ATTENTE ([N]) : ...
À RELANCER ([N]) : ...
EN COURS ([N]) : ...
FERMÉES ([N]) : ...
PROCHAINES ACTIONS : ...
```

**Règle** : ne jamais relancer plus de 2 fois sans mise à jour manuelle du statut.

---

## Règles de transition automatiques

- Statut "Envoyée" depuis > 7j sans relance programmée → écrire dans `status.md` : `- Prochaine action : Relancer avant [date J+3]` et créer brouillon Gmail
- Statut "Envoyée" depuis > 30j, 0 réponse, 2 relances faites → proposer archivage dans `99_ARCHIVES/` avec question explicite à Fabrice avant de déplacer
- Statut passe à "Entretien planifié" → écrire dans `status.md` un bloc `**Action MINERVE** : préparer entretien (commande : "MINERVE, prépare l'entretien [Entreprise]")`

---

## Escalade vers JANUS

Si l'une de ces conditions est détectée, ajouter une alerte dans le rapport FIDES ET signaler verbalement à Fabrice :
- Plus de 3 candidatures "Documents prêts" depuis > 7j sans être envoyées
- 0 entretien obtenu après 5 candidatures envoyées
- Relance en retard de > 3j

---

## Format RECRUTEURS.md

FIDES maintient ce fichier à jour. Colonnes obligatoires :

| Nom | Cabinet / Entreprise | Rôle | Email | LinkedIn | Candidatures liées | Dernier contact | Note |
|---|---|---|---|---|---|---|---|
