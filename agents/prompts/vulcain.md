# VULCAIN - Personnalisation de candidature

**Déclenchement** : commande "VULCAIN, personnalise ma candidature pour [Entreprise]"

**Tâche** :
0. **Lire la langue** : lire `03_CANDIDATURES/<Entreprise>/status.md`, extraire le champ `Langue`. **Tous les documents produits doivent être dans cette langue** (fr → français, en → anglais). En l'absence du champ, demander à l'utilisateur.
1. **Audit "Spot the Flaws"** (avant toute rédaction) : comparer CV_MASTER.md et job_description.md, identifier faiblesses, buzzwords sans preuve, métriques manquantes. Afficher le diagnostic en console.
2. Lire `01_PROFIL/CV_MASTER.md`, `BIO_EXECUTIVE.md`, `REALISATIONS.md`, `Amazon_Leadership_Interviews/CATALOGUE_ANECDOTES.md`
3. Lire `03_CANDIDATURES/<Entreprise>/job_description.md`
3. Rechercher des informations récentes sur l'entreprise (actualités, culture, enjeux SC)
4. Écrire dans `03_CANDIDATURES/<Entreprise>/` :
   - `cv_targeted.md` : hook 3 lignes en tête, profil réorienté, ≥ 5 mots-clés exacts de l'annonce intégrés, optimisé ATS
   - `cover_letter.md` : 3 paragraphes max, 300 mots max, sans formules creuses, accroche personnalisée
   - `fit_gap.md` : scoring 6D complet (compétences, secteur, responsabilité, ATS, go/no-go, culture)
   - `company_brief.md` : secteur, taille, valeurs, enjeux supply chain spécifiques, actualités récentes
5. Mettre à jour `status.md` → Statut = "Documents prêts"

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
