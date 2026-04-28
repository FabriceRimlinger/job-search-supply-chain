# INPUT - Dossier d'alimentation du profil

Déposez ici vos documents sources. JANUS les lira et construira automatiquement les fichiers de profil dans `01_PROFIL/`.

## Documents acceptés

| Type | Format | Utilisation |
|------|--------|-------------|
| CV existant | PDF, Word (.docx), Markdown | Alimenter `CV_MASTER.md` |
| Performance review | PDF, Word | Alimenter `REALISATIONS.md` |
| LinkedIn export | PDF | Compléter `CV_MASTER.md` |
| Bilan de compétences | PDF | Alimenter `BIO_EXECUTIVE.md` |
| Lettre de référence | PDF | Extraire des réalisations chiffrées |

## Comment déposer

1. Glissez vos fichiers dans `INPUT/raw/`
2. Dites à JANUS : **"JANUS, construis mon profil depuis INPUT/"**
3. JANUS lit tous les documents, extrait les informations et remplit :
   - `01_PROFIL/CV_MASTER.md`
   - `01_PROFIL/REALISATIONS.md`
   - `01_PROFIL/BIO_EXECUTIVE.md`
4. Les fichiers traités sont déplacés dans `INPUT/processed/`
5. Relisez et complétez manuellement si nécessaire

## Ce que JANUS extrait

**Depuis un CV :**
- Expériences (entreprise, poste, durée, responsabilités)
- Compétences techniques et comportementales
- Formations et certifications
- Langues et outils

**Depuis une performance review :**
- Réalisations chiffrées ("réduit les délais de X%", "géré un budget de X€")
- Points forts identifiés par le manager
- Axes de développement (utiles pour fit_gap)

## Règles importantes

- JANUS ne **jamais invente ni amplifie** - il extrait fidèlement ce qui est écrit
- En cas de doute sur une information, il la signale avec `[À CONFIRMER]`
- Les documents restent dans `INPUT/processed/` à titre d'archive (ne pas supprimer)
- Après mise à jour du profil, faire un `git commit + push` pour synchroniser avec les agents distants
