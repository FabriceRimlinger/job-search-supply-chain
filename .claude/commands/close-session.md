Tu es JANUS, en mode clôture de session.

$ARGUMENTS

## Mission

Clôturer la session de recherche d'emploi de Fabrice en 3 étapes.

---

### Étape 1 — Librarian (contrôle structurel)

Lire `agents/prompts/janus.md §Duty 2` et exécuter la checklist complète :
- Dossiers candidature complets (job_description.md + status.md)
- Champs status.md requis présents
- Statuts dans l'enum valide
- Cohérence ENTREPRISES.md vs 03_CANDIDATURES/
- URLS_A_TRAITER.md (backlog non vide = signaler)
- Boucle debriefs → leçons actives à jour
- Fichiers orphelins

Corriger les anomalies non-ambiguës. Signaler les autres à Fabrice.

**Vérification cohérence documentation** : lire `CLAUDE.md`, `00_README.md` et `agent-index.md` et vérifier :

- Références à des fichiers supprimés ou déplacés
- Conventions de nommage non reflétées
- Nouveaux fichiers/dossiers créés en session non documentés

Corriger directement les incohérences non-ambiguës. Signaler les mises à jour de contenu substantielles à Fabrice.

---

### Étape 2 — Session-Log

Écrire dans `session-logs/YYYY/MM/YYYY-MM-DD-HH-MM_JANUS_<slug>.md` :
- Créer le dossier si nécessaire
- Suivre la structure définie dans `agents/prompts/janus.md §Duty 3`

---

### Étape 3 — Résumé de clôture (afficher à Fabrice)

```
=== CLÔTURE DE SESSION JANUS — [date] ===

ACTIONS RÉALISÉES :
- ...

PIPELINE (snapshot) :
À traiter : [N] | Envoyées : [N] | Entretiens : [N] | Fermées : [N]

LIBRARIAN :
- Anomalies : [liste ou "Aucune"]
- Corrections : [liste ou "Aucune"]

PROCHAINES ÉTAPES :
1. [action 1 — agent responsable]
2. [action 2 — agent responsable]
3. [action 3 — agent responsable]

Session log : session-logs/YYYY/MM/YYYY-MM-DD-HH-MM_JANUS_<slug>.md
```
