# PREP - Alloga, Portfolio Manager Technology / Change & Transformation
**Date d'entretien** : 6 mai 2026, 11:30 CET (Teams)
**Interviewers** : Mamoudou Traore (Head of TSFM Delivery) + Mercedes Garcia (Senior Programme Manager)
**Durée** : 1 heure
**Contexte** : Portfolio management pan-European en environnement pharma régulé (GDP), expansion Cencora 2026

---

## 5 Questions Comportementales Probables + Réponses STAR

### 1. **"Tell us about a time when you had to manage a large, complex portfolio with competing priorities and stakeholders at executive level. How did you drive decisions?"**

**STAR** : Amazon SC Planning (2022-2023) - Expansion SOP 36 mois, 80+ bâtiments réaffectés EU-wide.

- **Situation** : Pilotage d'un programme de réaffectation supply chain pan-European sur 36 mois impliquant 25+ équipes transversales (Immobilier, Juridique, Finance, IT, Ops), avec C-level governance et rapports mensuels directement au VP Supply Chain.
- **Task** : Assurer alignment entre demandes des pays, constraints réglementaires et roadmap d'expansion, tout en maintenant business continuity.
- **Action** : Mis en place un SteerCo mensuel structuré (agenda, decision logs, escalation paths), created a BI dashboard (SHIELD) pour consolidate KPIs across countries. Used data-driven prioritisation to challenge scope creep et redirect resources vers high-impact projects.
- **Result** : 80+ bâtiments réaffectés on-track sans rupture opérationnelle. C-level visibility complète. Engagement du VP + Finance confiance renforcée.

---

### 2. **"Describe a situation where you had to deliver a major programme in a regulated or high-stakes environment. What compliance or quality controls did you implement?"**

**STAR** : Milee acquisition integration (2023-2024) - 300 employees, regulated logistics context.

- **Situation** : Intégration post-M&A de Milee (300 employees) dans Colis Privé. Environnement haute-stakes : négociations légales, P&L sensible, opérations 24/7, clients pharma existants (GDP-adjacent controls).
- **Task** : Assurer continuité opérationnelle complète, harmoniser processus sans disruption, achever intégration en 4 mois sous pressure.
- **Action** : Structuré un governance framework avec checkpoint hebdomadaires (legal compliance, ops readiness, staff engagement), mis en place un audit trail complet des décisions critiques, communiqué transparent aux 300 staff sur timelines et impacts. Used data to track integration KPIs (sickness absence, customer satisfaction, cost absorption).
- **Result** : Zéro incidents opérationnels post-acquisition. Intégration achevée 4 mois. Rétention staff >95%, clients pharma rassurés.

---

### 3. **"Can you give an example of a technical transformation programme you managed? What systems or integrations were involved, and how did you ensure benefits realisation?"**

**STAR** : SHIELD platform deployment (Amazon EMEA, 2019-2021) - pan-European BI rollout.

- **Situation** : 150+ Amazon EMEA stakeholders (Operations, Finance, Compliance, Regional MDs) utilisant des processes manuels et des data silos pour piloter Due Diligence decisions. Besoin : plateforme BI centralisée, audit trail, standardisation multi-pays.
- **Task** : Concevoir et déployer une solution BI (SHIELD) qui unifierait 15+ données sources (ERP, systems externes, spreadsheets legacy), en moins de 6 mois, sur 6 pays.
- **Action** : Led discovery sessions avec chaque stakeholder pour comprendre pain points. Built data model using SQL + PowerBI. Phased rollout avec training intensive (week 1-2), feedback loops (week 3-8), optimization. Tracked adoption (KPI: % de stakeholders actifs). Post-launch: 2-3 mois iterations basées sur usage réel.
- **Result** : Plateforme adoptée par 100% des stakeholders. Onboarding de nouveaux collaborateurs répassé de 4 semaines à 1 semaine. Décisions exécutives accélérées (audit trail auto-generated). Reconnu par les pairs : "revolutionised how the team operates".

---

### 4. **"Tell us about a time you had to communicate bad news or risks to executive leadership. How did you frame it and drive mitigation?"**

**STAR** : Amazon EMEA CapEx forecasting (2020) - ajustement de budget 40M€ mid-year.

- **Situation** : En Q2, forecasting montrait que le budget annuel 40M€ serait exceeded de 8% (~3.2M€) du à une accélération des client onboarding. Risk : amorce de rupture avec budget governance.
- **Task** : Communiquer cette variance au VP Finance et au CFO, en proposant des options claires sans excuses.
- **Action** : Prépared un executive brief (1 page) montrant : (1) root cause analysis précise, (2) impact business (growth upside + compliance maintained), (3) trois options de mitigation avec trade-offs clairs, (4) recommandation avec timing d'exécution. Présenté en SteerCo meeting avec data visuelle.
- **Result** : CFO approuva l'ajustement 3.2M€ et demanda de reproduire cette gestion de variance pour d'autres portfolios. Culture de "bad news early, options always" établie.

---

### 5. **"Describe a time when you had to build trust with senior stakeholders from different functions or cultures across Europe. How did you approach cross-functional collaboration?"**

**STAR** : Infarm European expansion CAPEX (2021-2022) - €72M, 16 engineers, 4 pays (DE, UK, DK, FR).

- **Situation** : Pilotage d'un CAPEX 72M€ pour déployer infrastructure agriculture verticale dans 4 pays EU. Équipe hétérogène : ingénieurs allemands (Infarm HQ), engineers UK, Danish logistics partners, équipe finance FR. Langues : EN + DE requises. Timezones : 1h décalage, meetings late afternoon DE = early morning FR.
- **Task** : Assurer alignement technique ET financier malgré différences culturelles et opérationnelles.
- **Action** : Established bi-weekly syncs structure (tech + finance combined pour contexte). Translated key docs (budgets, risk registers) en EN + DE dès départ. Travelled en personne en DE + UK (weeks 1-2) pour rencontrer teams face-to-face, comprendre local constraints. Mis en place un RACI clair (German HQ drives tech decisions, French finance approves spend, UK logistics validates site readiness). Celebrated small wins (site preparation ahead of schedule) across all four countries pour build momentum.
- **Result** : €72M déployé on-track across 4 countries sans major delays. German HQ noted "exceptional ability to bridge tech and business language". Teams across countries reported high confidence in governance.

---

## 3 Questions Techniques (Portfolio + Pharma/Regulated Context)

### 1. **"Our portfolio currently runs ~30 projects across 6 European sites, with WMS/TMS/OMS/EDI integrations and GDP compliance constraints. How would you approach portfolio governance and risk management in this context? What tools or frameworks would you use?"**

**Recommended response structure**:
- Acknowledge the complexity : 30 projects, multi-site, regulated = high integration risk.
- Propose a **structured governance framework** :
  - **SteerCo governance** : monthly executive steering, clear decision logs, escalation paths for regulatory issues
  - **Portfolio layer** : dependency mapping (WMS↔TMS↔EDI), risk register specific to regulated integrations (GDP validation, audit trail, testing protocols)
  - **Reporting** : executive dashboard (% on-track, budget vs. forecast, regulatory readiness, benefits on-track)
- **Regulated specifics** : mention that WMS/TMS/EDI in pharma = validation requirements (IQ/OQ/PQ), so project phases must include GDP readiness gates, not just technical go-live
- **Tools** : mention you'd assess Alloga's current portfolio system (update the "system of record"), possibly recommend BI dashboard similar to SHIELD for cross-site visibility
- **Benefits realisation** : tie projects to revenue growth (new client onboarding) and margin protection (operational efficiency), not just cost
- **Your experience** : reference Amazon portfolio 40M€ (dependency management), Infarm CAPEX 72M€ (multi-country coordination), Colis Privé transformation (post-M&A integration under execution pressure)

---

### 2. **"GDP compliance in pharmaceutical logistics means strict audit trails, validation requirements, and no shortcuts. How have you ensured regulatory compliance in previous roles, and how would you embed this into portfolio delivery?"**

**Recommended response structure**:
- **Honest start** : "I don't have direct pharma/GDP experience, but I've operated in highly regulated environments with strict compliance frameworks—Amazon EMEA (EDD, regulatory audits), Dole (traceability in cold chain). Let me show you the bridge."
- **Bridge concept** :
  - **Cold chain background** : Dole post-acquisition (2009-2010), worked with frozen fruit logistics requiring traceability, temperature controls, documentation standards similar in spirit to GDP
  - **Amazon regulatory** : EDD (Environmental Due Diligence) compliance across EMEA sites = mandatory documentation, audit trails, no deviation tolerance. Learned that compliance ≠ slowing down — it's about building processes that embed controls upfront
- **How you'd embed GDP into portfolio delivery** :
  - **Project charter includes GDP readiness gates** : not just tech go-live, but validation protocols (IQ/OQ/PQ), training sign-off, compliance evidence collected during build, not after
  - **Risk register specific to regulated integrations** : WMS/EDI API changes = validation scope, so project duration includes pre- and post-validation phases
  - **RAID management includes compliance dependencies** : if Supplier A (WMS vendor) delays validation, Project B (EDI go-live) is blocked — governance must surface this early
  - **Audit trail by design** : every decision logged (as in Amazon EDD), every deviation tracked, evidence collected in real-time
- **Your capability** : reference your BI + SQL skills (data governance, audit trails can be automated via dashboards), your ability to work with auditors / quality teams (proven at Amazon with compliance partners)

---

### 3. **"One of our key challenges is balancing revenue growth (new client onboarding, new services) with operational stability and compliance. How would you approach benefits realisation in this context?"**

**Recommended response structure**:
- **Acknowledge the tension** : yes, this is the core strategic challenge in 3PL — growth can destabilise operations if not managed.
- **Propose a dual-track benefits model** :
  - **Revenue growth track** : new client onboarding KPIs (# of clients, ramp-up timeline, revenue ramp), project to revenue contribution
  - **Stability/compliance track** : operational metrics (on-time delivery %, inventory accuracy, audit findings), compliance risk (zero non-conformances target)
- **Portfolio governance bridges them** :
  - **Portfolio prioritisation logic** : projects that drive growth AND maintain/improve stability rank highest (avoid false trade-off)
  - **Go/no-go gates** : a project only goes live if (a) revenue assumptions confirmed, (b) compliance validation complete, (c) operations signed off on readiness
  - **Post-implementation tracking** : benefits realisation doesn't end at go-live. Track revenue vs. plan for 3-6 months post-launch, track operational metrics for stability impact. If new client onboarding destabilises existing clients, red flag early
- **Your experience** :
  - **Colis Privé** : managed the balance between growth (+7.5% activity) and cost control (550k€ savings), via automation + process excellence
  - **Amazon SC Planning** : €40M portfolio = growth-focused (new sites, capabilities), but every project included post-implementation review to confirm benefits realisation (revenue contribution, margin protection)
- **Data approach** : reference your BI skills (SHIELD, PowerBI) — you'd establish a dashboard that tracks both revenue KPIs and operational stability KPIs in real-time, so gaps surface immediately

---

## 3 Questions à Poser aux Interviewers

### 1. **"You mentioned challenges in Europe around Alloga expansion. Can you give me a concrete example of a project or initiative that's on the portfolio now? What's the biggest risk or blocker you're seeing, and how are you currently managing it?"**

*Rationale* : Shows interest in their real problems, not just the job description. Gives you insight into their actual pain points and maturity of governance.

---

### 2. **"I see that Alloga is part of Cencora, a Fortune 50. How much autonomy does Alloga have in shaping its European portfolio strategy, versus taking direction from Cencora's global priorities? And how does the Portfolio Manager fit into that dynamic?"**

*Rationale* : Clarifies governance structure and your level of influence. Important to understand if you'd be driving strategy or executing someone else's.

---

### 3. **"On the GDP and regulated environment side — you mentioned compliance is non-negotiable. How do you see the Portfolio Manager role contributing to that? Are there specific regulatory or quality teams I'd be working closely with, and what's the relationship dynamic?"**

*Rationale* : Shows respect for regulated environment challenges. Demonstrates you'd partner with compliance, not work around it. Also uncovers if there are hidden friction points.

---

## Points Forts à Mettre en Avant (Ce Poste Précisément)

1. **Pan-European portfolio management at scale** : Amazon SC Planning (36-month SOP, 80+ sites, 6 countries), Infarm CAPEX (€72M, 4 countries, multi-cultural teams). You've proven you can coordinate complex, multi-country programmes with executive-level reporting.

2. **Financial governance + CapEx/OpEx ownership** : Amazon €40M/year budget (1200+ due diligence cases, 10 managers, 30+ consultants). Direct experience with large-scale financial forecast, variance management, business case oversight—exactly what the role requires.

3. **BI as a competitive advantage** : SHIELD platform (Amazon EMEA, 2019-2021) = you don't just manage portfolios, you revolutionise how teams see data. This is rare in Portfolio Managers. Mention SQL + PowerBI skills explicitly.

4. **Transformation programme delivery under pressure** : Colis Privé M&A integration (300 employees, 4 months, zero operational incidents), Infarm multi-country build, Amazon expansion SOP. You've delivered complex change without losing control or compliance.

5. **Regulated environment bridge** : Cold chain background (Dole, ColdEnergy ~10 years), Amazon EDD compliance (audit trails, regulatory audits), Milee integration (GDP-adjacent controls). Frame this as "I've built compliance into delivery, not bolted it on afterwards."

6. **Stakeholder management across cultures** : Infarm (DE/UK/DK/FR teams, budget discussions in German/English), Amazon EMEA (multi-regional C-level reporting), Colis Privé (legal, finance, operations, pharma clients). Proven ability to translate across functions and languages.

---

## Points de Vigilance (From Fit_gap)

### Critical Gap: Pharma/GDP Experience
**Watch point** : Recruiters may probe whether your non-pharma background is a deal-breaker.

**How to address** :
- **Own it upfront** : "I don't have direct pharma/GDP experience, AND here's why that's actually an asset..."
- **Bridge narrative** : cold chain (Dole), regulated compliance (Amazon EDD), post-M&A integration in logistics (Milee). These are adjacent regulated environments where you learned compliance-first thinking.
- **Speed of ramp** : "I'd need 2-3 months to get GDP-certified and understand Alloga's specific quality framework, but the portfolio governance principles I've mastered at scale transfer directly."
- **Who to learn from** : hint that you'd partner closely with Mamoudou (Head of TSFM Delivery) and quality teams—position this as collaborative, not a solo learning curve.

### Possible Questions to Trigger This
- "What's your experience with GDP?"
- "Have you worked in pharma before?"
- "Regulated environments can be very different—how quickly do you think you'd adapt?"

**Prepare a 30-second response** that shows respect for the gap, demonstrates adjacent experience, and signals confidence in your ability to learn the specific GDP framework.

---

### Potential Secondary Gaps
- **WMS/TMS/ERP direct experience** : you have *indirect* experience (Amazon, Colis Privé systems exposure). Don't claim expertise. Instead: "I've managed programmes that integrated WMS/TMS/EDI, working closely with IT and vendors. I don't code, but I understand the governance and validation requirements."
- **PMO certifications** : you don't have PMP/PRINCE2/MSP. **Do not mention**. Let your 40M€ + 72M€ + multi-year SOP speak for itself.

---

## Tone & Delivery Notes

- **Speak their language** : you're talking to TSFM Delivery (operations mindset) and a Senior Programme Manager (delivery mindset). Use concrete examples, metrics, timelines—not theory.
- **Show respect for constraints** : "Regulated environment, GDP, multi-site complexity" = they've likely been burned by portfolio chaos. Show you understand why governance matters.
- **Lead with data** : your superpower is turning data into decisions. Reference SHIELD, BI dashboards, KPI tracking. This will resonate with a growth-stage company in transformation.
- **Ask clarifying questions** : the three questions above are genuine discovery questions. Listen more than you talk.
- **Timeline expectation** : Amazon SC Planning + Infarm suggest you're comfortable with 36-month + programmes. Alloga expansion is likely similar scale.

---

## Dernière Vérification Avant l'Entretien

- [ ] Vérifier la date/heure (6 mai, 11:30 CET) dans ton calendrier
- [ ] Rejoindre Teams **5 min avant** (comme demandé par Matt Hancock)
- [ ] Vérifier micro + caméra (ils demanderont un tech check)
- [ ] Lire rapidement Cencora corporate (Fortune 50, logistics leader) sur leur site
- [ ] Relire les LinkedIn de Mamoudou Traore + Mercedes Garcia (2-3 min chacun pour trouver un point de connexion)
- [ ] Préparer une **anecdote courte** (< 2 min) sur ton moment le plus fier en portfolio management (ex: SHIELD impact)
- [ ] Anticiper la question "Why Alloga?" — réponse : growth-stage transformation company + proximity Marseille + pharma/regulated challenge you want to master
