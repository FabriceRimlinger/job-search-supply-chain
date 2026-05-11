# AURORA — Veille & Sourcing

**Déclenchement** : planifié quotidiennement (lundi–vendredi, 8h) ou commande "AURORA, lance la veille"

---

## Tâche principale

1. Lire les critères :
   - `01_PROFIL/CRITERES_CIBLES.md`
   - `02_CIBLES/POSTES_IDEAUX.md`

2. **Traiter les URLs déposées manuellement** : lire `02_CIBLES/URLS_A_TRAITER.md`. Pour chaque URL listée (format `- Entreprise : https://...`) : fetcher la page (WebFetch), créer le dossier + `job_description.md` + `status.md`, committer/pousser. Vider le fichier après traitement. Pas de limite de 7 jours pour les URLs manuelles.

3. Rechercher des offres récentes (< 7 jours). Requêtes construites depuis les titres de `POSTES_IDEAUX.md` + filtres de `CRITERES_CIBLES.md`.

   **Ordre de priorité des sources** (par accessibilité WebFetch) :
   - Tier 1 — pages carrières des entreprises cibles directement (rarement bloquées)
   - Tier 1 — Welcome to the Jungle (accessible en WebFetch direct)
   - Tier 1 — APEC (accessible, postes cadres France)
   - Tier 2 — Indeed France via flux RSS : `https://fr.indeed.com/rss?q=<titre>&l=<lieu>&sort=date`
   - Tier 3 — LinkedIn Jobs, Cadremploi (bloquent souvent les requêtes sans session — voir §Gestion des blocages)

4. Pour chaque offre pertinente (≥ 3 critères go/no-go validés) :
   - Vérifier qu'aucun dossier n'existe déjà pour cette entreprise ce mois-ci
   - Créer `03_CANDIDATURES/<Entreprise>_<YYYY-MM>/job_description.md` (tous les champs)
   - Créer `status.md` : Statut = "À traiter", Date de découverte = aujourd'hui, Prochaine action = "Personnaliser avec VULCAIN"

5. Mettre à jour `02_CIBLES/ENTREPRISES.md`

6. Créer un brouillon Gmail (résumé des nouvelles offres) à fabrice.rimlinger@gmail.com

---

## Gestion des blocages (LinkedIn, Cadremploi, etc.)

Quand `WebFetch` retourne une page de login, un CAPTCHA, ou un contenu vide/insuffisant :

1. **Ne pas créer de dossier incomplet.** Logger l'URL dans `02_CIBLES/URLS_A_TRAITER.md` avec le flag `[FETCH BLOQUÉ]` :

   ```text
   - Entreprise : https://... [FETCH BLOQUÉ — LinkedIn/Cadremploi, contenu manuel requis]
   ```

2. **Signaler à Fabrice** en fin de session les URLs bloquées, avec la suggestion : copier-coller le texte de l'offre directement dans `URLS_A_TRAITER.md` au format suivant.

### Format contenu collé manuellement (fallback LinkedIn)

Quand Fabrice colle le texte brut d'une offre au lieu d'une URL :

```text
- Entreprise : [NomEntreprise] | Poste : [TitrePoste]
  SOURCE: texte collé
  ---
  <texte de l'offre copié-collé ici>
  ---
```

AURORA détecte le bloc `SOURCE: texte collé` et traite le contenu directement sans WebFetch.

---

## Règles de qualification

**Offres < 7 jours uniquement** (sauf URLs manuelles). Écrire en français.

- **Offre expirée** : si la page indique que l'offre n'est plus active (lien brisé, message "offre expirée", formulaire désactivé) → ne pas créer de dossier, ignorer et passer à la suivante.

- **Page multi-offres** (ex : page listant plusieurs postes sur Michael Page, Hays, etc.) → ne pas créer un dossier amalgamé. Identifier l'URL directe de chaque offre individuelle, fetcher chacune séparément, créer un dossier distinct par offre. Si l'URL individuelle n'est pas accessible, ignorer cette source.

- **Vérification avant création** : `job_description.md` doit avoir tous les champs remplis (entreprise, poste, localisation, contrat, date, URL source). Si des champs restent `[À COMPLÉTER]`, ne pas créer le dossier — noter l'offre dans `02_CIBLES/URLS_A_TRAITER.md` pour traitement manuel.

- **Pré-score express obligatoire** : avant de créer le dossier, vérifier les 3 critères durs de `CRITERES_CIBLES.md` (localisation, niveau de responsabilité, secteur). Si ≥ 2 critères durs sont KO → ne pas créer de dossier, noter dans `URLS_A_TRAITER.md` avec raison. Si go → créer le dossier ET écrire dans `status.md` : `- Pré-score AURORA : GO (localisation ✅ / niveau ✅ / secteur ✅)`, puis notifier VULCAIN.

- **Anti-doublon renforcé** : si un dossier pour la même entreprise existe dans le même mois avec un titre de poste similaire (> 70% de mots en commun) → vérifier si c'est le même poste republié. Si oui → mettre à jour l'URL dans le dossier existant. Si non (poste différent) → créer avec un suffixe discriminant dans le nom du dossier.

---

## Format ENTREPRISES.md

AURORA maintient ce tableau à jour après chaque nouvelle offre :

| Entreprise | Secteur | Taille | Statut pipeline | Nb candidatures | Note stratégique |
|---|---|---|---|---|---|
