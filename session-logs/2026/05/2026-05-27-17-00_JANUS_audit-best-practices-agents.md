# Session JANUS - 2026-05-27 17:00

## Ce qu'on a fait
- Audit de conformité des 5 agents vs les best practices Anthropic Skills (https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- Enrichissement des descriptions des 5 commandes (.claude/commands/*.md) avec triggers d'utilisation
- Ajout de checklists de progression dans aurora.md et vulcain.md
- Réduction du CLAUDE.md (suppression des 4 sections agents dupliquées, -18% de tokens)
- Allégement des over-explanations dans aurora.md (format contenu collé) et vulcain.md (règles ATS)
- Annulation de la recommandation MCP tool names (format `mcp__claude_ai_Gmail__*` correct pour Claude Code)

## Candidatures touchées
- Aucune candidature directement modifiée (session infrastructure uniquement)
- ENTREPRISES.md : Farms Digital "Documents prêts" → "Entretien passé" (correction Librarian)

## Décisions et insights
- Les commandes Claude Code (`.claude/commands/*.md`) ne sont pas des Platform Skills : pas de YAML frontmatter, la première ligne "Tu es X" sert d'activation de persona (garder en 2ème personne)
- Les noms d'outils MCP dans Claude Code utilisent le format `mcp__claude_ai_Gmail__create_draft`, pas `Gmail:create_draft` (format Platform Skills)
- Le CLAUDE.md contient les instructions JANUS par défaut (session-log triggers, workflow INPUT) qui ne doivent pas migrer vers janus.md uniquement

## Librarian - rapport structurel
- Anomalies détectées : ENTREPRISES.md Farms Digital statut désynchronisé
- Corrections appliquées : statut Farms Digital mis à jour "Documents prêts" → "Entretien passé" + commentaires actualisés
- Note : FarmsDigital_Network company_brief.md sans job_description.md (attendu - pas d'offre formelle)
- Debrief Farms Digital : pas de nouvelle leçon active (points à améliorer = intel entreprise, pas technique d'entretien)

## Prochaines étapes
- Fabrice envoie le mail de suivi à Benoît Mauran (Farms Digital) - JANUS coaching
- Envoyer les candidatures CEVA (2 dossiers "Documents prêts" depuis 16j) - FIDES relance
- Décider HID + Leica (scores 6D < 35 - go/no-go à trancher) - JANUS diagnostic
