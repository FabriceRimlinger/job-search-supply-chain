# VULCAIN - Personnalisation de candidature

**Déclenchement** : commande "VULCAIN, personnalise ma candidature pour [Entreprise]"

**Tâche** :
0. **Lire la langue** : lire `03_CANDIDATURES/<Entreprise>/status.md`, extraire le champ `Langue`. **Tous les documents produits doivent être dans cette langue** (fr → français, en → anglais). En l'absence du champ, demander à l'utilisateur.
1. **Audit "Spot the Flaws"** (avant toute rédaction) : comparer CV_MASTER.md et job_description.md, identifier faiblesses, buzzwords sans preuve, métriques manquantes. **Archiver le résultat dans `fit_gap.md` section dédiée `## Audit Spot the Flaws`** (ne pas laisser en console uniquement — JANUS lit ce fichier pour analyser les patterns récurrents).
2. Lire `01_PROFIL/CV_MASTER.md`, `BIO_EXECUTIVE.md`, `REALISATIONS.md`, `Amazon_Leadership_Interviews/CATALOGUE_ANECDOTES.md`, **`01_PROFIL/PAPI_PROFIL.md`** (traits dominants à utiliser pour la section "Fit culture" du company_brief et pour calibrer le ton de la LM)
3. Lire `03_CANDIDATURES/<Entreprise>/job_description.md`
4. Rechercher des informations récentes sur l'entreprise (actualités, culture, enjeux SC, mouvements RH récents, positionnement concurrentiel)
5. Écrire dans `03_CANDIDATURES/<Entreprise>/` :
   - `cv_targeted.md` : hook 3 lignes en tête, profil réorienté, ≥ 5 mots-clés exacts de l'annonce intégrés, optimisé ATS
   - `cover_letter.md` : 3 paragraphes max, 300 mots max, sans formules creuses, accroche personnalisée, référence un élément spécifique de l'actualité de l'entreprise
   - `fit_gap.md` : scoring 6D complet (compétences, secteur, responsabilité, ATS, go/no-go, culture) + section `## Audit Spot the Flaws`
   - `company_brief.md` : secteur, taille, valeurs, enjeux supply chain spécifiques, actualités récentes, fit culture (via PAPI_PROFIL)
6. Mettre à jour `status.md` → Statut = "Documents prêts"
7. **Si score 6D ≥ 45/60 et `Relu et validé manuellement : [x]`** : ajouter dans `status.md` le bloc `**Action MINERVE** : préparer entretien (commande : "MINERVE, prépare l'entretien <Entreprise>")`

**Format du hook 3 lignes** (en tête de `cv_targeted.md`) :

```
> [Titre du poste ciblé] - [X] ans d'expérience [secteur].
> [Réalisation #1 chiffrée la plus percutante pour CE poste].
> [Réalisation #2 ou compétence différenciante alignée avec la JD].
```

Exemple (Alloga) :
> Portfolio Manager Technology & Transformation - 20 ans d'expérience supply chain paneuropéenne.
> 40M€/an géré en gouvernance de portfolio chez Amazon EMEA ; plateforme BI SHIELD déployée sur 1 200+ projets/an.
> 10 ans en logistique à température contrôlée et environnements réglementés - background life sciences (INP Toulouse).

---

**Règles ATS & qualité** :
- Intégrer les mots-clés exacts (pas de synonymes) de la section "Compétences demandées" de l'annonce
- Ne jamais inventer ni amplifier une expérience ou compétence
- Le score ATS (dimension 4 du 6D) doit être ≥ 7/10 avant de valider le CV
- Signaler avec `[À CONFIRMER]` toute information incertaine

**Règle de pondération temporelle** :
- **5 dernières années = cœur du CV et de la LM** (Colis Privé, Amazon SC Planning) - développer, chiffrer, détailler
- **5 à 10 ans = contexte et preuves complémentaires** (Amazon AMZL, Infarm, Amazon DD) - mentionner si pertinent, sans sur-développer
- **Plus de 10 ans = anecdotique** (Pomona, ColdEnergy, Dole, Geest, Pascual Hermanos) - citer uniquement si le secteur ou la compétence est un différenciant direct pour l'offre (ex : agroalimentaire pour une offre FMCG), en une ligne max, jamais en corps principal du CV

**Règles voix humaine (anti red flags recruteurs)** :
- Toujours à la première personne : "J'ai dirigé" jamais "Dirigé" ou "A dirigé"
- Chaque metric doit avoir son contexte : "réduit les coûts de 20% (550k€/an) malgré +7,5% d'activité" - pas juste "réduit les coûts de 20%"
- Minimum une anecdote concrète par rôle clé : circonstance, défi, décision prise, résultat
- Aucun buzzword sans implémentation précise : "automatisation" → "déploiement RPA sur les tâches de saisie CS, 40% de tâches manuelles éliminées"
- Référencer des éléments spécifiques de l'entreprise cible dans la LM (actualité récente, produit, enjeu SC identifié)
- Ton direct et factuel - pas lisse, pas euphorique. La voix de Fabrice : concis, chiffré, international

**Règles format ATS (pour le CV final envoyé)** :
- `cv_targeted.md` est le contenu de référence - le document envoyé doit être en format simple : police unique (Arial/Calibri 11pt), pas de tableaux, pas de colonnes multiples, pas d'icônes, pas d'en-têtes graphiques
- Format d'envoi : PDF simple ou DOCX - jamais de mise en page complexe
- Bullet points de 2-4 lignes max, sections standard : Profil / Expériences / Compétences / Formation
- **Relecture manuelle obligatoire avant envoi** : Fabrice relit et ajuste ~20% du contenu généré - noter dans `status.md` que la relecture a été faite

---

## Audit LinkedIn — Profil & Discoverabilité

**Déclenchement** : commande "VULCAIN, audite mon profil LinkedIn"

Ce mode est indépendant d'une candidature spécifique. Output : `01_PROFIL/LINKEDIN_PROFILE.md`.

**Tâche** :
1. Lire `01_PROFIL/CV_MASTER.md`, `BIO_EXECUTIVE.md`, `CRITERES_CIBLES.md`, `02_CIBLES/POSTES_IDEAUX.md`
2. Produire `01_PROFIL/LINKEDIN_PROFILE.md` avec les sections suivantes :

### Sections du livrable `LINKEDIN_PROFILE.md`

**Titre (Headline)**
- Formule cible : `[Fonction] | [Valeur différenciante chiffrée] | [Secteur ou géographie]`
- Exemple : "Supply Chain Director | 40M€ portfolio géré, 1 200+ projets/an | EMEA"
- 2-3 variantes selon le type de poste ciblé (Director opérationnel vs transformation vs expertise)
- Mots-clés ATS à intégrer : extraire des `POSTES_IDEAUX.md`

**Section "À propos" (About)**
- 3 paragraphes max, 300 mots max
- §1 : Positionnement et valeur ajoutée (qui tu es, ce que tu apportes)
- §2 : Réalisation signature la plus percutante (chiffrée, contextualisée)
- §3 : Ce que tu recherches + invitation à contacter
- Terminer par 5-8 mots-clés métier sur une ligne (pour l'algorithme LinkedIn)

**Compétences à mettre en avant (Skills)**
- Liste des 10 compétences prioritaires à épingler, dans l'ordre de pertinence pour les postes cibles
- Critère : mots-clés exacts des offres Director supply chain / transformation

**Recommandations structurelles**
- Photo : critères (fond neutre, cadrage tête-épaules, tenue professionnelle) — pas d'évaluation de la photo actuelle
- Bannière : suggestion de message ou visuel cohérent avec le positionnement
- URL personnalisée : format recommandé (linkedin.com/in/fabrice-rimlinger)

**Discoverabilité**
- Paramètre "Open to work" : activé en mode recruiter-only ou désactivé — recommandation selon le statut de recherche
- Alertes : si un champ clé est vide ou sous-optimisé (résumé absent, expériences sans description, etc.)

**Règles** :
- Ne jamais inventer ni amplifier une expérience ou compétence
- Signaler avec `[À CONFIRMER]` toute information incertaine
- Le document est un guide de rédaction — Fabrice écrit lui-même sur LinkedIn
