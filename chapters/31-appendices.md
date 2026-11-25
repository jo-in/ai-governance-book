# Appendices: Templates, Checklists & Reference Toolkit

*Practitioner Templates, Governance Checklists, Crosswalks & Reference Guides*

> **In these appendices**
> - **Appendix A: Role-Based Cheat Sheets** — Top 7 pre-approval questions for all eight governance stakeholder roles, plus Role Reading Paths.
> - **Appendix B: AI Governance RACI Matrix (Template)** — Copy-ready accountability assignment across 18 lifecycle governance activities.
> - **Appendix C: AI Use-Case Intake & Risk-Tiering Form (Template)** — Five-minute standardized intake, prohibited-practice screen, and Tier 1–3 scoring rubric.
> - **Appendix D: AI Vendor Due Diligence Questionnaire (Template)** — 32 procurement verification questions spanning IP, ZDR, security, fourth-party chains, resilience, and ESG telemetry.
> - **Appendix E: Employee AI Acceptable Use Policy (Template)** — Plain-English workforce policy with Traffic-Light data rules and explicit whistleblower carve-outs.
> - **Appendix F: Pre-Flight Production Checklist (Go/No-Go Rubric)** — Gate verification table and executive waiver sign-off template aligned to Chapter 26.
> - **Appendix G: Regulatory & Framework Crosswalk** — Unified 14-domain mapping across EU AI Act (`2024/1689` + Digital Omnibus `2026/1744`), NIST AI RMF, ISO/IEC 42001, and OWASP/MITRE ATLAS.
> - **Appendix H: AI Incident Response Playbook (Template)** — Severity tiers, out-of-band kill-switch directory, four technical containment cards, reporting clocks, and postmortem closure.
> - **Appendix I: Glossary of Terms** — Complete alphabetical reference consolidating enterprise AI governance, security, legal, and FinOps terminology.
> - **Appendix J: References & Further Reading** — Thematic guide connecting governance topics directly to the Annotated Bibliography.

---

## Appendix A: Role-Based Cheat Sheets

*Adapted from the core design principle of this handbook: different roles read the same risk landscape through distinct responsibilities. Bring these seven questions to your next intake gate, vendor review, or executive briefing before approving any AI initiative.*

### Board of Directors
1. How does this initiative align with our board-approved AI risk appetite, and what is our exposure if an error scales across customers (`Moffatt`-style commitments, systemic bias, or safety harm)?
2. Are all mission-critical AI dependencies—including underlying foundation-model and GPU concentration risks—mapped inside our quarterly Board Dashboard (**Chapter 28, Table 28.1**) and Business Continuity Impact Tolerances?
3. What proportion of active company AI spend is still operating off-inventory ("shadow AI"), and what did FinOps show regarding `>90-day` idle pilot spend?
4. Do we hold affirmative contractual assurances covering Zero Data Retention (`ZDR`), no-training guarantees, IP indemnification boundaries, and exit portability?
5. Has an independent second or third line (`IIA 2025` / Model Risk / External Assessor) tested high-risk deployments against blind golden datasets and adaptive red teams prior to launch?
6. How have we satisfied applicable statutory timelines (`EU AI Act Art. 4` literacy since February 2025; `Art. 50` transparency since August 2026; EU Digital Omnibus `2027/2028` readiness; `CSRD` Scope 2/3 compute energy)?
7. Do our confidentiality agreements, audit escalations, and ethics portals legally protect whistleblowers who surface AI safety or disclosure flaws early?

### Chief Executive Officer (CEO)
1. Which measurable customer or operating metric improves with this AI system—and would we still fund it if inference unit costs double or foundation pricing rises?
2. Are we making our governed internal AI portal effortless enough ("paved road") that staff naturally choose it over consumer tools?
3. Who owns single-point executive accountability (`Accountable` in **Appendix B**) if this workload misbehaves publicly on a Friday evening?
4. Do our promotion criteria and town-hall messages reward leaders for pulling the "Stop-the-Line" cord on unsafe launches, or only for hitting demo dates?
5. What is our competitive switching plan if our primary foundation vendor suffers a four-hour blackout, forces a 60-day deprecation, or raises rates materially?
6. Are external marketing statements about `"hallucination-free"` accuracy or `"ethical AI"` substantiated strictly by staged empirical test logs (avoiding SEC/FTC AI-washing exposure)?
7. How will front-line staff retain manual exception capability if AI tools drop offline during peak demand?

### Chief Information Officer (CIO) / CTO
1. Does all traffic route through one central enterprise AI gateway enforcing pinned snapshots (never `-latest` aliases), token budgets, jittered retries, and `OpenTelemetry gen_ai.*` logging?
2. Have we bundled prompts, model snapshots, retrieval chunks, tool schemas, and guardrail configs into one Git-tracked release manifest for point-in-time reproducibility?
3. If our primary cloud region or model provider vanishes for 24 hours, is our ZDR-equivalent secondary model or deterministic non-generative floor tested and warm?
4. Are we backing up raw ACL-tagged source corpora plus pinned embedding artifacts inside cross-cloud immutable vaults rather than relying solely on live vector snapshots?
5. Can a low-risk Tier 3 internal team clear intake automatically inside `<= 48 hours` without bogging down Tier 1 architectural review boards?
6. Are we cascading routine classification and extraction tasks down to compact Small Language Models (`SLMs`) or deterministic code rather than burning frontier reasoning tokens unnecessarily?
7. What automated 90-day sandbox expiry enforces cleanup of orphaned staging clusters and zombie pilot endpoints?

### Chief Information Security Officer (CISO)
1. Have we verified architectural blast-radius containment assuming prompt injection will bypass text classifiers (`confusable deputy` reality)—using strict RBAC/ReBAC, network egress allowlists, and runtime capability checks?
2. If this system uses RAG, does retrieval strictly enforce per-user document ACL permissions at query time, and is the vector database encrypted and tenant-isolated at plaintext security parity?
3. Can an autonomous agent mutate external systems (`write`, `delete`, `transfer`) without scoped short-lived Non-Human Identity (`NHI`) tokens, idempotency keys, and out-of-band human confirmation?
4. Do all PII scrubbers, prompt-injection sidecars, and authorization gates strictly **fail closed** on latency spikes or timeouts?
5. Are open-weights artifacts verified via `OpenSSF Model Signing`, `Safetensors` format enforcement, `CycloneDX ML-BOM` manifests, and isolated sandboxes prior to ingestion?
6. Have nightly `garak` probes and adaptive `PyRIT` multi-turn tests targeted indirect injections inside uploaded files, emails, and MCP tool descriptions?
7. Can SOC analysts pull an out-of-band IAM/gateway kill switch inside minutes and preserve immutable `gen_ai.*` telemetry before wiping volatile caches?

### Chief Data Officer (CDO) & Data Stewards
1. What legal basis, copyright provenance, license terms, and consent opt-out boundaries cover every corpus document or fine-tuning record entering this pipeline (`SPDX 3.0`)?
2. Has PII, PHI, PCI, or trade-secret data been stripped, masked, or tokenized at ingestion—and strictly restricted from crossing unauthorized jurisdictions?
3. Are retrieval collections versioned and sanitized cleanly when employee access changes, policies expire, or GDPR erasure requests (`Art. 17`) arrive?
4. Are AI-generated summaries and synthetic outputs tagged and quarantined before corpus re-ingestion to prevent recursive model collapse?
5. Do backup and retirement workflows verify cryptographic erasure (`NIST SP 800-88 Rev. 2`) across vector clones, caches, and checkpoints while respecting `FRCP 37(e)` legal-hold freezes?
6. Have evaluation slices verified output reliability and completeness across underrepresented customer dialects, languages, and edge-case populations?
7. Can engineering trace a specific answer generated six months ago cleanly back to the exact source document revision and metadata tags active at query time?

### General Counsel, Compliance & Data Protection Officer (GC / DPO)
1. Does the use case trigger any prohibited AI red line (`EU AI Act Art. 5`) or Annex III / sector high-risk classification, employment audit law (`NYC LL144` / `IL HB 3773`), or automated decision statute (`GDPR Art. 22` / `CCPA ADMT` / `CO SB 26-189`)?
2. Does the underlying vendor contract guarantee ZDR, no model training on company inputs/outputs, explicit sub-processor approval, audit rights, and `<= 24h` security incident notification?
3. Have we checked open-weight license caps (e.g., Meta `700M MAU` triggers or field-of-use caps) and excluded unlicensed scraped training inputs creating disgorgement risk?
4. Are mandatory AI disclosure labels, `C2PA` Content Credentials, and clear adverse-action explanations (`ECOA` / `AI Act Art. 86`) wired seamlessly into user interfaces?
5. Are `EU AI Act Art. 18` (`10-year` provider files), `Art. 26(6)` (`>=6-month` deployer logs), and instant `FRCP Rule 37(e)` litigation-hold locks separated cleanly from live data-minimization purges?
6. Are triage escalation timers calibrated to colliding statutory clocks (`DORA 4h/24h`, `NIS2 24h`, `AI Act 2d/10d/15d`, `GDPR 72h`, `SEC 4 business days`)?
7. Do all NDAs, severance terms, and DLP policies contain explicit whistleblower carve-outs satisfying `SEC Rule 21F-17`, `CA SB 53`, and `Directive (EU) 2019/1937`?

### AI Engineers & Architects
1. Are `dev-eval` tuning prompts strictly isolated from our frozen, quarantined `gate-eval` dataset containing calibrated abstention traps and past incident failures?
2. Are component RAG metrics (`RAGAS` context precision/recall vs. faithfulness) tracked separately from deterministic JSON schema assertions?
3. Are our LLM-as-a-Judge monitors bias-controlled (order-swapped `A/B` and `B/A`, length-normalized, cross-family judged) and recalibrated monthly against human experts?
4. Do mutating MCP/tool actions use strict type validation, bounded step/token ceilings, idempotency keys, and dead-letter queues against retry cascades?
5. If our upstream embedding model upgrades, is an atomic blue/green vector collection rebuild automated before swapping collection aliases?
6. Are non-human service tokens scoped to minimum task permissions with automatic expiration and zero hardcoded credentials in prompts or repos?
7. If an engineer notices a hidden fairness defect or missing safeguard on launch week, is there one unambiguous Stop-the-Line escalation path?

### Business & Product Owners
1. Exactly how can this AI fail gracefully—switching seamlessly to deterministic keyword search, static rules, or human queues—when inference slows or stalls?
2. What domain-specific edge cases, ambiguous conflicts, and regulatory exclusions did our subject-matter experts contribute to the blind evaluation set?
3. How do we present confidence boundaries, source links, and friction cues in the UI so users avoid passive automation bias and catch plausible hallucinations?
4. Have our human supervisors rehearsed manual "AI-off" shifts within the past quarter so manual proficiency does not erode (`Bainbridge`)?
5. Do we track customer human-override rates, complaint spikes, and re-ask friction weekly as early-warning KRIs?
6. What quantified unit outcome justifies this system's ongoing token and GPU run rate—and what triggers retirement on Day 90 if adoption or ROI lags?
7. Have all operational users and contractors using this feature completed practical, scenario-based role training (`Art. 4`) before go-live?

#### Reading Paths by Role

| Role | Core Chapters | Recommended Companion Sections |
| :--- | :--- | :--- |
| **Board Members / CEO** | Ch. 1, 3, 5, 14, 28, 30 | Ch. 20, 23, **App. A & B** |
| **CIO** | Ch. 1, 4, 5, 23, 24, 25, 30 | Ch. 11, 13, 26, **App. C & F** |
| **CISO / Security** | Ch. 9–14, 23, 27 | Ch. 6, 7, 26, **App. D & H** |
| **CDO / Data Stewards** | Ch. 6, 7, 8, 15, 16, 22 | Ch. 5, 19, 24, **App. C & G** |
| **General Counsel / Compliance / DPO** | Ch. 8, 18–22, 23 | Ch. 3, 16, 27, 29, **App. D, E & G** |
| **AI Engineers / Architects** | Ch. 1, 7, 10–13, 15, 26 | Ch. 17, 18, 24, 25, **App. F & H** |
| **Business & Product Owners** | Ch. 1, 5, 15, 16, 17 | Ch. 18, 28, 29, **App. C & E** |

---

## Appendix B: AI Governance RACI Matrix (Template)

**Legend:** **R** = Responsible (executes work) · **A** = Accountable (single final decision/risk owner; strictly one `A` per row) · **C** = Consulted (provides mandatory expert input before decision) · **I** = Informed (notified of outcome/status).

| # | Lifecycle Governance Activity | Board / Risk Comm. | CEO / Bus. Exec | CIO / MLOps Eng | CISO / AppSec | CDO / Stewards | GC / DPO / Comp. | Product Owner | Internal Audit |
| :-: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | Approve Enterprise AI Policy & Risk Appetite | **A** | C | C | C | C | **R** | I | I |
| 2 | Maintain Intake Gate & Assign Risk Tiers (1–3) | I | I | C | C | C | C | **R** | I |
| 3 | Approve Tier 1 High-Risk AI Business Sponsor Risk | I | **A** | C | C | C | C | **R** | I |
| 4 | Reconcile Enterprise AI Inventory vs. Cloud Billing | I | I | **A / R** | C | C | I | C | I |
| 5 | Clear Training/RAG Data Provenance & Consent | I | I | C | C | **A / R** | C | C | I |
| 6 | Enforce Permission-Aware RAG ACLs & Vector Isolation | I | I | **R** | **A** | C | I | I | I |
| 7 | Model Threat Scoping & Agent IAM Containment | I | I | R | **A** | I | I | C | I |
| 8 | Execute Vendor Due Diligence & ZDR Contracts | I | I | C | C | C | **A** | **R** | I |
| 9 | Run Blind `gate-eval` & Automated CI Security Scans | I | I | **A / R** | C | C | I | C | I |
| 10 | Lead Independent Tier 1 Red-Teaming & Release Gate | I | **A** | C | **R** | C | C | C | I |
| 11 | Authorize Time-Boxed `CONDITIONAL GO` Waivers | I | **A** | C | C | C | C | R | I |
| 12 | Govern Change-Materiality Matrix & Model Sunsets | I | I | **A / R** | C | C | C | C | I |
| 13 | Monitor Live KRIs, Drift & Trip Fallback Circuits | I | I | **R** | C | C | I | **A** | I |
| 14 | Enforce AI FinOps Unit Attribution & 90-Day Sunsets | I | **A** | **R** | I | I | I | C | I |
| 15 | Verify CSRD Scope 2/3 & Annex XI Energy Telemetry | I | **A** | **R** | I | I | C | I | I |
| 16 | Execute AI Incident Kill Switch & WORM Trace Capture | I | I | **R** | **A** | C | C | I | I |
| 17 | File Regulatory Incident Notices & Freeze Legal Holds | I | I | C | C | C | **A / R** | I | I |
| 18 | Deliver EU AI Act Art. 4 Role Literacy & Speak-Up | I | **A** | C | C | C | **R** | C | **C** |

*(Note: On Line 2 above, assign single `A` for intake triage operations to Chief Risk Officer / Governance Chair if separate from Legal/Product; customize Role column headers to match your organization's Chief Risk Officer (`CRO`), Chief Human Resources Officer (`CHRO`), and Chief Financial Officer (`CFO`) seats.)*

---

## Appendix C: AI Use-Case Intake & Risk-Tiering Form (Template)

*Designed to take five minutes for initial submission. Complete prior to procurement signature, API-key provisioning, or staging deployment.*

### Section 1: Ownership & Business Context
- **Use-Case Name & Short ID:** `[ ]`
- **Accountable Executive Business Sponsor (Name / Title):** `[ ]`
- **Technical / Product Owner (Name / Team):** `[ ]`
- **System Type:** `[ ] Internal Copilot  [ ] Customer-Facing Assistant  [ ] Decision / Eligibility Support  [ ] Autonomous Agent  [ ] Embedded SaaS Feature`
- **Delivery Path:** `[ ] Vendor SaaS  [ ] Custom App via Foundation API  [ ] Fine-Tuned / Open-Weights Self-Hosted`
- **Expected Measurable Value / Unit Outcome Metric:** `[ ]`
- **Target Go-Live / 90-Day Pilot Sunset Date (if PoC):** `[ ]`

### Section 2: Technical, Data & Autonomy Profile
- **Model(s) & Pinned Snapshot / Weight Digest:** `[ ]` *(floating `-latest` aliases prohibited in Tier 1/2)*
- **Hosting Region & Contractual ZDR Status:** `[ ] Verified Enterprise ZDR + Region Pin  [ ] Standard Consumer / Non-ZDR (BLOCK)`
- **Highest Data Sensitivity Touched:** `[ ] Public Only  [ ] Internal Non-Sensitive  [ ] Confidential IP / Contracts  [ ] PII / HR / Customer Data  [ ] PHI / PCI / Biometric / Regulated Special Category`
- **Enterprise Knowledge Integration (RAG):** `[ ] None  [ ] Public Docs  [ ] Internal Corpus with Enforced Per-User ACL Filtering  [ ] Unfiltered Shared SharePoint/Drive (BLOCK UNTIL ACLs WIRED)`
- **External Tool / Action Permissions (`Agents / MCP`):** `[ ] Read-Only Text Output Only  [ ] Read-Only Internal Lookup  [ ] Mutating / Write / Financial / External Comms Tools`

### Section 3: Hard Red-Line Screening (`Prohibited` Automatic Reject)
Does this system involve any of the following practices? *(If YES to any item, halt immediately and escalate to General Counsel.)*
- `[ ]` Subliminal, manipulative, or deceptive techniques distorting human behavior causing significant harm (`EU AI Act Art. 5(1)(a)`)
- `[ ]` Exploitation of age, disability, or socio-economic vulnerability (`Art. 5(1)(b)`)
- `[ ]` Social scoring evaluating trustworthiness across unrelated social contexts
- `[ ]` Workplace or educational emotion inference (outside strictly bounded medical/safety exceptions)
- `[ ]` Untargeted scraping of facial images or biometric categorization by sensitive traits
- `[ ]` Direct autonomous execution of irreversible financial transfers, clinical interventions, or production `DROP/DELETE` operations without deterministic IAM limits and human approval

### Section 4: Automatic Risk-Tier Scoring Rubric
Select the highest matching criteria below—the **highest single answer** sets your system tier:

| Risk Dimension | Tier 1: Critical / High-Risk | Tier 2: Moderate Risk | Tier 3: Low Risk (Fast Lane) |
| :--- | :--- | :--- | :--- |
| **Impact on Individuals / Revenue** | Determines or materially influences credit, hiring, insurance, health, legal eligibility, safety, or direct financial commitments | Customer-facing support/knowledge Q&A, contract drafting, or external content generation with human review | Internal productivity drafting, summarization, or coding assistance on non-sensitive work |
| **Data Exposure** | Processes regulated PII, PHI, PCI, biometric, special-category, or crown-jewel source/M&A secrets | Processes general confidential internal business documents or non-sensitive business customer context | Public or generic non-confidential corporate information only |
| **Autonomy Level** | Autonomous agent calling external/internal mutating APIs (`write`/`transfer`/`provision`) | Recommends workflows or populates draft forms requiring explicit human submit confirmation | Strictly read-only conversational or formatting suggestions |
| **External Regulation** | Falls under EU AI Act Annex I/III, DORA ICT critical service, NYC LL144/IL HB 3773, HIPAA, FDA SaMD, or SR 26-2 material scope | Subject to AI disclosure/transparency rules (`Art. 50`, `CA SB 942`) or standard GDPR consumer processing | Outside high-risk statutory definitions; covered by standard AUP (**Appendix E**) |

### Section 5: Intake Disposition & Required Gates
- **Assigned Risk Tier:** `[ ] Tier 1 (Full Gate + Independent Validation)   [ ] Tier 2 (Standard Review + Golden Eval + AppSec)   [ ] Tier 3 (<=48h Paved-Road Self-Serve via SSO ZDR Gateway)`
- **Required Next Artifacts:** `[ ] Appendix D (if third-party)   [ ] DPIA / Impact Assessment   [ ] Blind gate-eval + RAG ACL check   [ ] Appendix F Pre-Flight Sign-Off`
- **Governance Reviewer Sign-Off & CMDB ID:** `[ ]`

---

## Appendix D: AI Vendor Due Diligence Questionnaire (Template)

*Issue to every prospective AI SaaS supplier, foundation-model provider, or embedded-AI incumbent before signature or feature toggle (Chapter 23). Mark any `Red-Flag` failure for mandatory escalation before contracting.*

| # | Diligence Question | Category | Required Evidence / Red-Flag Pass Criteria |
| :-: | :--- | :--- | :--- |
| **1** | Specify full legal entity, AI hosting jurisdictions, and corporate control over model operations. | Governance & Sovereignty | Entity matches MSA signatory; contractual residency pinning matches data boundary. |
| **2** | Are customer prompts, uploaded files, RAG chunks, telemetry logs, or generated outputs **ever** used to train, fine-tune, or evaluate foundation or safety models? | Data & Training | Written unconditional **no-training warranty** covering all enterprise tiers (`Red Flag` if opt-out only or ambiguous). |
| **3** | Do you provide contractual **Zero Data Retention (`ZDR`)** eliminating abuse/safety prompt storage on disk? | Privacy & Retention | Signed ZDR addendum (`0-day` retention) or explicit bounded exception approved by CISO/DPO. |
| **4** | Which third- and fourth-party sub-processors, inference providers, and upstream model APIs touch customer data? | Fourth-Party Risk | Complete sub-processor list + `>=30-day` advance notice + object/terminate right on new AI sub-processors. |
| **5** | Have training datasets been audited for copyright provenance, personal-data consent, and lawful text/data mining opt-outs? | IP & Provenance | Written transparency summary (`AB 2013` / EU GPAI Art. 53) and credible provenance hygiene. |
| **6** | Do you provide contractual uncapped (or heightened-cap) **IP copyright/trademark indemnification** covering enterprise AI outputs? | Legal Indemnity | Indemnification confirmed without impossible prompt-engineering carve-outs (`Ch. 19`). |
| **7** | Confirm all AI workflows honor enterprise SSO/SAML, MFA (`FIDO2`), RBAC/SCIM, and document-level retrieval permissions. | Access & Identity | No shared multi-tenant API keys; retrieval enforces source ACLs cleanly per user (`Red Flag` if global index). |
| **8** | How are tenant vector stores, fine-tuned adapters, and semantic caches isolated cryptographically (`customer-managed keys / KMS`)? | Multi-Tenancy | Per-tenant logical/cryptographic isolation verified; cache keys bound strictly to caller identity. |
| **9** | Describe defenses against indirect prompt injection, tool hijacking, and SSRF inside uploaded files or connectors. | AppSec Controls | Layered deterministic tool allowlists, egress restrictions, and human confirmation gates (`no prompt-only claims`). |
| **10** | Do you publish an `AI-BOM` (`CycloneDX 1.6` / `SPDX 3.0`), third-party model licenses, and cryptographic signatures (`OpenSSF OMS`)? | Supply Chain | Machine-readable component inventory + license disclosures (identifying any `700M MAU` or field caps). |
| **11** | Provide latest `SOC 2 Type II`, `ISO/IEC 27001`, and—where applicable—`ISO/IEC 42001` or independent AI assurance reports. | Third-Party Audit | Unqualified recent attestation covering production AI inference infrastructure (`<=12 months` old). |
| **12** | Detail automated and independent human red-teaming cadence, methodology (`MITRE ATLAS` / `NIST AI 100-2`), and remediation SLAs. | Red-Teaming | Written red-team summary report showing critical/high findings remediated cleanly prior to release. |
| **13** | Share empirical accuracy, hallucination/abstention calibration, and fairness disaggregation evaluations (no `"100% accurate"` marketing claims). | Reliability & Bias | Domain-relevant accuracy/precision benchmarks and subgroup error parity metrics provided cleanly. |
| **14** | Does the product support machine-readable output provenance (`C2PA` / watermarking) and configurable `Art. 50` AI disclosure labels? | Transparency | Configurable user-facing `"AI-generated"` labels and metadata intact on media/synthetic exports. |
| **15** | For high-risk use cases, will you supply full `EU AI Act Annex IV` technical files, `FRIA`/DPIA inputs, and adverse-action explanations? | Compliance Support | Written cooperation obligation supporting customer conformity, impact assessments, and bias audits (`NYC LL144` / `ECOA`). |
| **16** | Does the platform prohibit undocumented silent swaps of underlying model snapshots across active customer endpoints? | Change Control | Explicit model-pinning capability + advance written notice (`>=30–60 days`) before weight/router upgrades. |
| **17** | What guaranteed advance notice window applies before deprecating or retiring a supported model snapshot? | Lifecycle Notice | Minimum **`>= 60 days`** written deprecation notice alongside shadow-testing sandbox access (`Ch. 24`). |
| **18** | Describe your operational outage SLA, regional failover topology, and independent backup path if upstream GPU APIs fail. | Resilience | Documented `RTO`/`RPO`, multi-region failover honoring identical ZDR/residency pins, and `99.9%+` enterprise SLA. |
| **19** | Within how many hours do you notify customers of security breaches, cross-tenant data spills, or reportable AI safety incidents? | Incident Clocks | Binding notification **`<= 24 hours`** (enabling customer `DORA 4h/24h`, `NIS2 24h`, and `GDPR 72h` compliance) + full forensic log access. |
| **20** | Upon termination or vendor failure, how do we export fine-tuned weights, prompt configs, and raw corpora cleanly without egress penalties? | Exit & Portability | `30-day` structured migration window, documented export formats, and zero switching/egress fees matching **EU Data Act**. |
| **21** | How do you prove permanent deletion of tenant embeddings, caches, backups, and fine-tuned weights upon exit (`NIST SP 800-88r2`)? | Sanitization | Written **Certificate of Sanitization / Cryptographic Erase** within `30 days` post-exit (unless valid legal hold applies). |
| **22** | Do you expose OpenTelemetry (`gen_ai.*`) token telemetry, per-workspace cost limits, and automated rate-limit guardrails? | FinOps Controls | Exportable API/usage logs broken down by workspace, user/agent key, input tokens, and output tokens. |
| **23** | Can you supply vendor-verified Scope 3 energy (`kWh`), `PUE`, or computational energy estimates (`CSRD ESRS E1` / `EU AI Act Annex XI`)? | ESG Telemetry | Primary compute energy/carbon methodology or annual verified intensity disclosures committed in writing. |
| **24** | Confirm whether any FTC, SEC, state AG, EU supervisory order, or pending copyright/privacy injunction targets the product or weights. | Disgorgement Risk | Clean litigation & regulatory disclosure confirming zero algorithmic-deletion exposure (`FTC v. Rite Aid` / M&A check). |

*(Expand rows 25–32 dynamically per domain for Sector Addenda: HIPAA Business Associate Agreements & `§ 520(o)(1)(E)` / `PCCP` status for healthcare; Federal Reserve `SR 23-4` / `SR 26-2` fourth-party flow-downs & `DORA` Article 28 RoI fields for financial services; NYC Local Law 144 / `IL HB 3773` independent audit packets for employment tools; accessibility `WCAG` compliance for public portals; and FedRAMP/OMB `M-25-22` terms for public-sector contractors.)*

---

## Appendix E: Employee AI Acceptable Use Policy (Template)

**Policy Owner:** General Counsel & CISO · **Effective Date:** `[YYYY-MM-DD]` · **Applies To:** All employees, executives, contractors, temporary staff, and external service personnel operating AI systems on behalf of `[Company Name]`.

### 1. Purpose
`[Company Name]` encourages responsible use of approved AI tools to boost productivity, creativity, and customer service while protecting customer trust, intellectual property, fairness, and legal compliance. Guardrails exist to let you work faster safely—not to push AI underground.

### 2. Traffic-Light Tool & Data Classification Rules

| Tier | Approved Tools & Permissible Data | Mandatory Employee Actions |
| :--- | :--- | :--- |
| **GREEN: Always Approved** | `[Company SSO AI Portal / Approved IDE Copilot]` operating under verified Zero Data Retention (`ZDR`) contracts. Permissible for public, internal, and approved confidential business context matching your own access permissions. | Verify factual accuracy, citations, and code security before sharing externally; follow department prompt templates. |
| **AMBER: Restricted Approval Required** | Processing **Customer PII, Health Info (`PHI`), Financial Records, HR Evaluations, or Source Trade Secrets** inside Tier 1/2 approved enterprise tools (`CMDB`-registered). | Use **only** approved business-unit tools cleared under Risk Tier 1–2 (`Appendix C`); **never** bypass human review on eligibility, hiring, credit, or clinical actions. |
| **RED: Strictly Prohibited** | Entering *any* non-public company, customer, employee, or partner data into **personal or unapproved consumer AI tools** (`BYOAI`), free browser extensions, unapproved meeting-transcription bots, or personal API keys. | **Zero exceptions:** Never paste source code, credentials/API secrets, customer files, unannounced financials, legal privilege memos, or PII into unapproved tools. |

### 3. Mandatory Verification & Accountability ("Human-in-the-Loop")
- **You own what you ship:** AI systems hallucinate citations, legal rules, prices, and software libraries confidently. Never publish external emails, client deliverables, customer policy statements, or production code containing unverified AI claims or unreviewed dependencies.
- **Verify urgent payment/credential requests out of band:** Treat any unexpected voice call, video clip, or email from executives or vendors requesting wire transfers, MFA resets, or urgent policy overrides as a potential deepfake (`Chapter 14`); confirm independently using a pre-verified directory number before acting.
- **No false marketing or undisclosed commitments:** Never tell customers or regulators an AI output is infallible, and clearly label external synthetic media or customer-facing chatbot interactions per Company Disclosure Standards.

### 4. Requesting New Tools ("No Silent Shadow AI")
Need a specialized AI coding plug-in, vendor feature, or workflow tool missing from our portal? Submit the five-minute **Intake Form (Appendix C)**—Tier 3 low-risk requests clear inside `48 hours`, and Business Unit AI Champions help connect teams quickly without workarounds.

### 5. Protected Speak-Up Culture & Whistleblower Carve-Out
If you spot an unsafe AI model, biased decision pattern, undisclosed vendor sub-processor, falsified test metric, or potential legal violation:
- **Stop and report safely:** Escalate immediately to `[Ethics Hotline / Anonymous Portal URL]` or directly to Legal/Ethics. Company policy strictly prohibits retaliation of any form against employees or contractors raising good-faith safety or compliance concerns (`EU AI Act Art. 87` / `Directive (EU) 2019/1937` / `CA SB 53`).
- **Explicit Legal Disclosure Carve-Out:** *Nothing in this Policy, any confidentiality agreement, non-disclosure agreement, or handbook rule prevents or impedes any individual from communicating directly with, or making protected disclosures to, the U.S. Securities and Exchange Commission (`17 CFR § 240.21F-17`), EU supervisory authorities, law enforcement, or other applicable government regulators regarding potential legal, safety, or compliance violations without prior company notice or authorization.*

### 6. Consequences & Acknowledgment
Violating Red-line data rules or intentionally disabling approved AI security controls may lead to access revocation and disciplinary action consistent with HR policy.

**Acknowledgment:** I have completed my role-specific AI Literacy lab (`Appendix Table 29.1`) and agree to follow this Acceptable Use Policy.  
**Signature / SSO Stamp:** `[ ]` · **Date:** `[ ]`

---

## Appendix F: Pre-Flight Production Checklist (Go/No-Go Rubric)

*Mandatory release gate prior to initial Tier 1/2 launch and all Tier C/D changes (Chapter 24 & Chapter 26).*

| Gate # | Verification Control & Evidence Artifact Required | Tier 1 Req. | Tier 2 Req. | Tier 3 Req. | Status (`Pass / Fail / N/A`) |
| :-: | :--- | :---: | :---: | :---: | :---: |
| **1** | **Inventory & Ownership:** Registered CMDB Asset ID, named Business Risk Owner & Technical Owner (`App. C`). | Mandatory | Mandatory | Mandatory | `[ ]` |
| **2** | **Immutable Release Bundle:** Prompts, pinned model snapshot digest (no `-latest`), embedding ID, and tool schemas Git-tagged. | Mandatory | Mandatory | Auto-CI | `[ ]` |
| **3** | **Vendor & Data Clearance:** Signed ZDR, no-training, sub-processor & IP clauses (`App. D`); valid data provenance/consent & DPIA/FRIA. | Mandatory | Mandatory | Portal Default | `[ ]` |
| **4** | **RAG Permission Enforcement:** Document-level ACL filtering verified at query time; tenant isolation & KMS keys verified (`0` cross-tenant leaks). | Mandatory | Mandatory | N/A (No Restricted RAG) | `[ ]` |
| **5** | **Blind Golden Gate Evals:** Passed quarantined held-out `gate-eval` (`>=95%` Tier 1 critical accuracy/schema fidelity; `>=90%` Tier 2 RAGAS faithfulness; calibrated abstention scored). | Mandatory | Mandatory | Dev Smoke (`>=85%`) | `[ ]` |
| **6** | **Subgroup Fairness Disaggregation:** Adverse impact (`AIR`), false-positive/negative parity, and demographic/dialect checks pass tolerances (`Ch. 16`). | Mandatory | Key Slices | Baseline Check | `[ ]` |
| **7** | **CI & Adaptive Red-Teaming:** Nightly `garak` + adaptive multi-turn `PyRIT` passed; **Independent** human & domain red team resolved `0` Critical/High exploits (`App. D/Ch. 26`). | **Independent** + CI | Internal Peer + CI | CI Probe (`garak`) | `[ ]` |
| **8** | **Agent Containment (if tool-calling):** Read/write separated; short-lived scoped NHI tokens; runtime schema validation; idempotency keys + DLQs active. | Mandatory | Mandatory | Prohibited in Tier 3 | `[ ]` |
| **9** | **Fail-Closed Sidecars & Outage Fallback:** Verified PII/injection sidecars fail **closed** on timeout; deterministic BM25/rule/human fallback verified under fault injection. | Mandatory | Mandatory | Fail-Silent Banner | `[ ]` |
| **10** | **Telemetry, Kill Switch & Legal Hold:** `OTel gen_ai.*` tracing to WORM vault tested; `<5 min` IAM/gateway kill switch tested; `FRCP 37(e)` / `Art. 18` retention wired. | Mandatory | Mandatory | Gateway Default | `[ ]` |
| **11** | **Transparency, Literacy & FinOps:** User AI notices/C2PA active (`Art. 50`); staff & reviewers completed Table 29.1 role training (`Art. 4`); token budgets & 90-day sunset tagged. | Mandatory | Mandatory | Standard AUP | `[ ]` |

### Hard-Block (`NO-GO`) Conditions *(Override Strictly Prohibited)*
- `[ ]` Any unresolved Critical/High sandbox breach, cross-tenant RAG ACL leak, or uncontained destructive tool call
- `[ ]` Any safety/PII guardrail sidecar failing open on timeout
- `[ ]` Missing ZDR/no-training addendum for regulated or confidential enterprise data
- `[ ]` Missing blind `gate-eval` run or using unpinned floating model aliases in Tier 1/2 production

### Formal Release Verdict & Waiver Sign-Off
- **Verdict:** `[ ] GO (Staged Canary Rollout Approved)   [ ] CONDITIONAL GO (Bounded Cohort Only — Waiver Required)   [ ] NO-GO (Release Blocked)`
- **If CONDITIONAL GO — Exact Residual Limitation & Mitigation Control:** `[ ]`
- **Hard Expiry Date (Max `30–60` Calendar Days):** `[YYYY-MM-DD]` *(auto-halts pipeline deployment upon expiry)*
- **Business Risk Owner Approval Signature:** `[ ]` · **Independent Risk / CISO / Governance Approver:** `[ ]` · **Date:** `[ ]`

---

## Appendix G: Regulatory & Framework Crosswalk

*Unified enterprise control mapping allowing one engineering control library to satisfy global statutes and certifiable standards simultaneously.*

| Control Domain | EU AI Act (`2024/1689` + Digital Omnibus `2026/1744`) | NIST AI RMF 1.0 & GenAI Profile (`600-1`) | ISO/IEC 42001:2023 | OWASP (`LLM 2025` / `Agentic 2026` / `NHI`) & `MITRE ATLAS` | Handbook Chapters |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1. Governance & Accountability** | Art. 16–17 (Provider QMS), Art. 26 (Deployer duties), Art. 25 (Substantial mod) | `GOVERN 1–6` (Policies, roles, oversight, risk tolerances) | Clauses 4–5, Annex A.2–A.3 (AI Policy, Roles, Leadership) | Shared governance accountability across threat models | Ch. 3, 4, 30 |
| **2. Inventory & Risk Classification** | Art. 5 (Prohibited), Art. 6 & Annex I/III (High-Risk), Art. 49 EU Database registration | `MAP 1–5` (Intended context, impact categorization, risk framing) | Clause 6.1, Annex A.5 (System Inventory & Impact Assessment) | Component asset mapping across pipelines (`AI-BOM`) | Ch. 5, 20, 21 |
| **3. Data Provenance, Privacy & Erasure** | Art. 10 (Data governance, GDPR alignment), Art. 10(5) (Bias data safeguards) | `MAP 2`, `MEASURE 2`, `MANAGE 2` (Privacy & data quality) | Clause 7.5, Annex A.7 (Data Provenance, Quality & Privacy) | `LLM02` Sensitive Information Disclosure; `AML.T0057` | Ch. 6, 8, 24 |
| **4. RAG Access Control & Isolation** | Art. 15(5) (Cybersecurity & unauthorized third-party data alteration/access) | `GOVERN 6`, `MANAGE 2` (Access boundary enforcement) | Annex A.6 / A.7 (Lifecycle Access & Storage Isolation) | `LLM08` Vector & Embedding Weaknesses; `LLM02` Leak | Ch. 7, 13 |
| **5. Prompt Injection & Agent Security** | Art. 15(5) (Model manipulation & cyber robustness), Art. 55 (Systemic GPAI) | `MEASURE 2.7` / `600-1` Information Security Actions | Annex A.6.2 (System Design & Runtime Technical Safeguards) | `LLM01` Injection, `LLM05` Output, `LLM06`, `ASI01–ASI10`, `NHI1–2`; `AML.T0051/53` | Ch. 9–11, 14 |
| **6. Model Supply Chain & Integrity** | Art. 11 & Annex IV (Third-party weights & open-weight traceability), Art. 53 | `GOVERN 6` (Third-party software & model dependencies) | Annex A.10 (Third-Party & Supplier Relationships) | `LLM03` Supply Chain; `ASI04` Agent Supply Chain; `AML.T0010` | Ch. 12, 23 |
| **7. Hallucination & Reliability Testing** | Art. 9(6)–(8) (Pre-market threshold testing), Art. 15(1)/(4) (Accuracy & robustness) | `MEASURE 2.5` & `600-1` Confabulation Mitigation | Clauses 8–9, Annex A.6.2 (Verification & Validation) | `LLM09` Misinformation (`RAGAS` / blind `gate-eval`) | Ch. 15, 26 |
| **8. Bias & Fairness Disaggregation** | Art. 10(2)(f)–(g) (Bias detection/mitigation), Art. 27 (FRIA rights impact) | `MEASURE 2.11` (Fairness, bias & subgroup parity; `SP 1270`) | Annex A.5.4–A.5.5 (Individual & Societal Impact Assessment) | Algorithmic bias & demographic performance parity checks | Ch. 16, 21 |
| **9. Human Oversight & Contestability** | Art. 14 (Human-oversight UI & stop button), Art. 85–86 (Explanation & complaint) | `GOVERN 3`, `MANAGE 3` (Human-in-the-loop authority) | Annex A.9 (Responsible Use & Human Control Boundaries) | `ASI09` Human-Agent Trust Exploitation | Ch. 17, 29 |
| **10. Transparency & Provenance** | Art. 13 (Instructions), Art. 50 (Bot & synthetic content labels), Art. 53(1)(d) | `MAP 2`, `MEASURE 2.8` & `AI 100-4` (Provenance) | Annex A.8 (Information for Interested Parties & Users) | Trust transparency & deepfake provenance (`C2PA`) | Ch. 18, 19 |
| **11. Vendor Concentration & Resilience** | Art. 15(4) (Resilience against faults/inconsistencies), Art. 25 (Upstream provider) | `GOVERN 6`, `MANAGE 4` (Third-party & contingency plans) | Annex A.10 (Supplier Risk, Outage Continuity & Exit) | `LLM10` Unbounded Consumption; `ASI08` Cascading Failures (`DORA`/`SS1/21`) | Ch. 23, 25 |
| **12. Change Control & Decommissioning** | Art. 18 (`10-year` doc), Art. 26(6) (`>=6-mo` logs), Art. 61/72 (Post-market monitoring) | `MANAGE 4` (Continuous monitoring, updates & retirement) | Clause 8–10, Annex A.6 (Lifecycle Changes & Retirement) | `NHI1:2025` Improper Offboarding (`NIST SP 800-88r2`) | Ch. 22, 24 |
| **13. Incident Reporting & Legal Hold** | Art. 73 (`2d`/`10d`/`15d` serious incidents), Art. 26(5) (Deployer alert & suspend) | `MANAGE 4.3` (Incident escalation, reporting & recovery) | Clause 10.2, Annex A.6.2 (Incident Learning & Records) | Forensics trace capture (`DORA 4h`, `NIS2 24h`, `GDPR 72h`, `SEC 4d`) | Ch. 27, 28 |
| **14. Literacy, Speak-Up & ESG Watts** | Art. 4 (Literacy), Art. 87 (Whistleblowing), Art. 53 & Annex XI (GPAI energy) | `GOVERN 1–2` (Training culture & accountability) | Clause 7.2–7.3 (Competence & Awareness) | Cultural & economic defenses (`CSRD ESRS E1` / `SB 53` / `21F-17`) | Ch. 28, 29 |

#### Key Global Regulatory Milestones (2025–2028)
- **Jan 17, 2025:** EU DORA (`2022/2554`) enters application (`Art. 19` `4h/24h` reporting & `Art. 28` vendor registers).
- **Feb 2, 2025:** EU AI Act Prohibited Practices (`Art. 5`) and Workforce AI Literacy (`Art. 4`) enter application.
- **Mar 31, 2025:** UK PRA `SS1/21` & FCA `PS21/3` full Impact Tolerance compliance deadline.
- **Aug 2, 2025:** EU AI Act GPAI model rules (`Arts. 51–55`, `Annex XI` energy documentation) enter application.
- **Sep 12, 2025:** EU Data Act cloud-switching rights (`30-day` transition) enter application (`Art. 29(1)` zero switching fees eff. **Jan 12, 2027**).
- **Jan 1, 2026:** California `AB 2013` / `CCPA ADMT`, `SB 53` (*TFAIA* whistleblowing), Illinois `HB 3773`, Texas `HB 149` (*TRAIGA*), and **Jan 22, 2026** South Korea *AI Basic Act*.
- **Aug 2, 2026:** EU AI Act `Article 50` synthetic transparency & California `SB 942`/`AB 853`.
- **Dec 2, 2026 / Jan 1, 2027:** EU Platform Work Directive `2024/2831` transposition (`Dec 2, 2026`); Colorado `SB 26-189` ADMT statute (`Jan 1, 2027`).
- **Dec 2, 2027 / Aug 2, 2028:** Deferred high-risk compliance dates under EU Digital Omnibus `Regulation (EU) 2026/1744` for stand-alone Annex III systems (`Dec 2, 2027`) and Annex I embedded-product AI (`Aug 2, 2028`).

---

## Appendix H: AI Incident Response Playbook (Template)

*Print/host offline outside compromised AI clouds. Pull deterministic IAM/gateway switches BEFORE running cleanup.*

### 1. Severity Matrix & Escalation SLAs (OECD Taxonomy)

| Severity | Definition & Trigger Criteria | Initial Response SLA | Escalation Bridge |
| :---: | :--- | :---: | :--- |
| **Sev-1 (Critical)** | Actualized external data/PII/secret spill, runaway destructive/financial tool action, physical/critical-infrastructure threat, or active statutory clock | `< 15 min` | Incident Commander, CISO, GC/DPO, Exec Business Owner, MLOps |
| **Sev-2 (High)** | Active guardrail-bypassing jailbreak/indirect injection without confirmed external harm, `>5%` systemic hallucination/refusal regression, or fairness parity failure | `< 30 min` | SOC Lead, AI Eng Lead, AppSec, Product Risk, Model Risk |
| **Sev-3 (Moderate)** | Isolated customer misrepresentation (*Moffatt*), contained blocked probe ("AI hazard"), or non-critical copilot brownout | `< 4 hours` | Product Risk, Eng Lead, Support Operations |
| **Sev-4 (Low)** | Minor tone/formatting drift or harmless over-refusal with zero security, privacy, safety, or financial impact | `< 48 hours` | Eng Regression Backlog (`gate-eval` candidate) |

### 2. Out-of-Band Kill-Switch & Evidence Directory *(Fill Per Environment)*
- **Central AI Gateway Circuit-Breaker Endpoint / Console:** `[URL / CLI Runbook]`
- **IAM Service Principal & Agent NHI Emergency Revoke Script:** `[URL / KMS Break-Glass Procedure]`
- **Git / MLflow Release-Bundle Rollback Digest Target:** `[Registry URL]`
- **Forensic WORM Export Destination (`OTel gen_ai.*` + Vector Snapshot Archive):** `[Immutable S3/Blob Object-Lock URI]`
- **Legal Hold Freeze Lead (`FRCP Rule 37(e)` Purge Halt):** `[GC / e-Discovery On-Call Contact]`

### 3. Containment & Recovery Playbooks
- **Playbook H1 — Indirect / Direct Prompt Injection:** (1) Isolate tainted uploaded PDF/email/RAG chunk ID and block outbound markdown image/URL rendering; (2) Disable or downgrade vulnerable tool connectors; (3) Export raw `gen_ai.*` traces + retrieved document IDs to WORM archive; (4) Scrub poisoned records from active indices & backups (`NIST SP 800-88r2`); (5) Harden tool allowlists/input boundaries and commit payload to blind `gate-eval`.
- **Playbook H2 — AI Data Leak & Cross-Tenant Cache Spill:** (1) Trip egress filter or flush affected semantic caches / compromised vector partitions immediately; (2) Revoke exposed keys/NHIs; (3) Snapshot gateway logs, vector ACLs, and ZDR request IDs for DPO scope sizing; (4) Issue emergency vendor data-deletion demand if public or unauthorized endpoint touched; (5) Trigger `GDPR Art. 33/34` (`72h`) breach assessment.
- **Playbook H3 — Systemic Harmful Output, Misrepresentation, or Bias Surge:** (1) Roll back release bundle digest or divert gateway traffic to deterministic search/manual fallback; (2) Export all customer-facing outputs during impacted window under legal hold; (3) Coordinate customer remediation/corrections via Legal; (4) Diagnose weight/prompt/RAG drift before re-testing against full `Appendix F`.
- **Playbook H4 — Runaway Autonomous Agent:** (1) **Never prompt the agent via chat to stop**—revoke scoped NHI credentials and MCP sessions immediately via IAM kill switch; (2) Lock dead-letter queues and freeze downstream ERP/payment webhooks; (3) Trace all idempotency keys & executed tool calls via `gen_ai.*` trace IDs; (4) Restore transactional database backups cleanly; (5) Remove excessive privileges deterministically before restarting.

### 4. Statutory Notification Clocks & Blameless Postmortem Closure
- **Check Clocks Immediately at Sev-1/Sev-2 Classification:** **DORA (`<=4h` from major class / `<=24h` awareness -> `72h` -> `1m`)** · **NIS2 (`<=24h` -> `72h` -> `1m`)** · **EU AI Act Art. 73 (`<=2d` critical infra / `<=10d` death / `<=15d` general + `Art. 26(5)` deployer suspend/alert)** · **GDPR (`<=72h` authority)** · **SEC Form 8-K Item 1.05 (`<=4 business days` of materiality)**.
- **5-Day Postmortem Sign-Off Requires All Five Items:** `[ ] WORM Evidence & FRCP 37(e) Status Confirmed   [ ] Blameless Root Cause Documented   [ ] Poisoned/Failing Case Committed to Blind gate-eval   [ ] Deterministic IAM/Schema Fix Deployed (Not Prompt-Only)   [ ] App. H / KRI / MITRE ATLAS Updated`.

---

## Appendix I: Glossary of Terms

*Alphabetical reference consolidating foundational enterprise AI governance terminology across all 30 chapters.*

- **Adversarial Machine Learning:** Crafting inputs, poisoned training data, or manipulated environments to cause AI models to misclassify, reveal secrets, bypass safety gates, or exhaust compute (`NIST AI 100-2 E2025`).
- **Agentic AI:** AI architectures capable of multi-step planning, maintaining memory, and invoking external tools, APIs, or sub-agents (`MCP`/`A2A`) to execute tasks autonomously inside digital or physical environments.
- **AI Bill of Materials (`AI-BOM` / `ML-BOM`):** Machine-readable manifest (`CycloneDX 1.6` or `SPDX 3.0`) recording model weights, training datasets, cryptographic hashes, upstream parent models, licenses, and known vulnerabilities.
- **AI Gateway:** Centralized architectural proxy inspecting and routing all model traffic—enforcing authentication, rate limits, PII redaction, ZDR headers, schema validation, OpenTelemetry logging, and fallback circuits.
- **AI Hazard (Near-Miss):** Event or circumstance where AI development, use, or malfunction could *plausibly* lead to an actualized AI incident if left unaddressed (`OECD`, 2024).
- **AI Incident:** Event where AI development, use, or malfunction directly or indirectly causes actual injury, critical-infrastructure disruption, human/fundamental/IP rights violations, or property/environmental damage (`OECD`, 2024).
- **AI Literacy:** Practical skills, knowledge, and understanding enabling providers, deployers, and affected persons to deploy AI informedly and recognize opportunities, limitations, and harms (`EU AI Act Art. 3(56)` & `Art. 4`).
- **AI Red-Teaming:** Structured adversarial testing probing both security vulnerabilities (prompt injection, data/tool hijack) and socio-technical harms (bias, unsafe advice) beyond static unit tests.
- **AI-Washing:** Making unsubstantiated, exaggerated, or false public claims about AI capabilities, accuracy (`"hallucination-free"`), or governance maturity in marketing or securities filings (`SEC` / `FTC`).
- **Algorithmic Disgorgement:** Regulatory remedy ordering an organization to delete not only unlawfully collected training data, but also any trained models, weights, or algorithms built from it (`FTC v. Rite Aid` / `Kurbo`).
- **Alignment:** Training and steering AI behavior toward human-intended values, honesty, and policy boundaries—frequently strained by conflicting helpfulness vs. refusal objectives.
- **Automation Bias:** Human cognitive tendency to over-rely on automated recommendations—generating errors of omission (failing to act without alerts) or commission (rubber-stamping wrong AI advice).
- **Bring Your Own AI (`BYOAI`):** Employees adopting consumer or unvetted external AI applications via personal accounts to complete work tasks faster than official corporate tools allow (`78%` prevalence in `Microsoft 2024 Work Trend Index`).
- **Business Impact Analysis (`BIA`):** Foundational `ISO 22301` continuity assessment mapping critical services, upstream third/fourth-party AI dependencies, and acceptable disruption tolerances (`MTPD` / `RTO` / `RPO`).
- **C2PA / Content Credentials:** Open technical provenance standard (`Coalition for Content Provenance and Authenticity`) cryptographically binding creator, capture/generation tool, and edit history into digital media manifests.
- **Calibrated Abstention:** Scoring and designing models to respond `"I don't know"` or escalate honestly when evidence is weak rather than hallucinating plausible guesses (`Kalai et al.`).
- **Change Anything Changes Everything (`CACE`):** Machine-learning coupling principle coined by Sculley et al. (`2015`): modifying one prompt clause, chunk size, feature, or guardrail alters behavior across coupled components.
- **Circuit Breaker (AI Gateway):** Automated fault-isolation trigger cutting off traffic to an unhealthy, degraded, or drifting model/agent path and routing cleanly to pre-validated standby models or deterministic fallbacks.
- **Confusable Deputy:** Security condition where a model cannot reliably distinguish trusted system instructions from untrusted user data inside the same token stream (`UK NCSC`).
- **Continuous Controls Monitoring (`CCM`):** Ongoing automated telemetry verifying control effectiveness in production (`NIST SP 800-137`) rather than relying on annual static approvals.
- **Data Provenance:** Verifiable chain of custody documenting dataset origin, licensing, consent status, legal scraping/opt-out compliance, and transformations (`SPDX 3.0`).
- **Dead-Letter Queue (`DLQ`):** Durable buffer capturing failed or interrupted asynchronous AI/agent tool executions with idempotency keys for safe inspection and non-duplicate recovery.
- **Deepfake / Synthetic Media:** AI-generated or AI-altered audio, video, or imagery realistically impersonating real people or events (`FinCEN 2024` social-engineering alerts; `EU AI Act Art. 50`).
- **Denial-of-Wallet (`DoW`):** Financial availability attack driving extreme token consumption, verbose reasoning loops, or Sponge inputs to inflate metered cloud inference bills (`OWASP LLM10`).
- **Drift (Covariate / Concept / Behavioral):** Post-deployment shift in incoming prompt distributions, real-world facts/rules, or vendor model weights causing silent degradation despite green infrastructure telemetry.
- **Electronically Stored Information (`ESI`):** Discoverable digital records—now spanning saved AI prompts, agent execution traces, and meeting transcripts—subject to U.S. `FRCP 37(e)` legal holds.
- **Embedding Inversion:** Reconstruction attack recovering readable original text—including names and clinical/sensitive facts—directly from numeric vector embeddings (`vec2text`, `Morris et al.`).
- **Exaggerated Safety (Over-Refusal):** Brittle alignment or safety tuning causing models to block benign domain queries containing sensitive keywords (medical, security, historical).
- **Fail-Closed vs. Fail-Open:** Failure design rule requiring security/compliance sidecars to block execution or route to human review (`fail-closed`) rather than passing uninspected traffic through (`fail-open`) on timeout.
- **Fourth-Party Risk:** Indirect operational, legal, or security exposure created when your approved SaaS vendor embeds an unvetted external foundation-model provider beneath its product.
- **Golden Dataset (`dev-eval` vs. `gate-eval`):** Curated, versioned benchmark pairing developer iteration sets (`dev`) with a blind, quarantined release-gate set (`gate`) including abstention traps and prior production failures.
- **Goodhart's Law:** Principle that when a benchmark or KRI becomes a narrow optimization target, systems game the metric while degrading real-world reliability or safety.
- **Hallucination (Confabulation):** Statistically plausible but factually false, ungrounded, or fabricated output—including invented legal citations, prices, or policies—presented fluently by generative models.
- **Human-in-the-Loop (`HITL`) / Human-on-the-Loop (`HOTL`):** Oversight designs placing humans before execution (`HITL`) versus monitoring autonomous actions with interrupt/override control (`HOTL`).
- **Idempotency Key:** Unique operation token ensuring retries after network or API brownouts never execute duplicate financial transfers or database writes.
- **Impact Tolerance:** Board-approved maximum tolerable disruption duration or volume loss for customer-facing Important Business Services (`UK PRA SS1/21` / `FCA PS21/3`).
- **Jailbreak:** Adversarial prompt technique designed to bypass a foundation model's built-in safety alignment and elicit restricted instructions or content.
- **Jagged Technological Frontier:** Empirical finding (`Dell'Acqua et al.`) that AI excels dramatically on tasks inside its irregular capability boundary while sharply raising human error rates on deceptively similar outside-frontier tasks.
- **Key Risk Indicator (`KRI`):** Forward-looking early-warning risk metric (`COSO`) signaling rising exposure against risk appetite before a major incident erupts.
- **Lethal Trifecta:** High-danger agentic design combining `(1)` access to private enterprise data, `(2)` exposure to untrusted external content, and `(3)` external communication/exfiltration ability (`Willison`).
- **LLM-as-a-Judge:** Using calibrated language models to score outputs at scale against rubrics, requiring controls against position, verbosity, and self-enhancement biases (`Zheng et al.`).
- **Model Collapse:** Irreversible degradation of rare-event accuracy and diversity when models train or index recursively on uncurated AI-generated synthetic data (`Shumailov et al.`).
- **Model Context Protocol (`MCP`):** Open client-server protocol connecting AI models to external enterprise tools, data stores, and APIs—requiring strict server trust verification and least-privilege auth (`OAuth 2.0`).
- **Non-Human Identity (`NHI`):** Machine credentials—API keys, service principals, webhook secrets, and agent tokens—subject to credential sprawl and improper offboarding risks (`OWASP NHI Top 10`).
- **Paved Road:** Engineering platform design making the compliant, ZDR-backed internal workflow substantially faster and more capable than unvetted shadow AI alternatives.
- **Policy-as-Code:** Expressing risk, ZDR, schema, and evaluation release thresholds in deterministic CI/CD and gateway configuration files rather than static manuals.
- **Prompt Injection (Direct & Indirect):** Attack embedding hidden or adversarial instructions inside user prompts (`Direct`) or ingested external documents, emails, and webpages (`Indirect`, e.g., `EchoLeak`).
- **Provisioned Throughput Units (`PTUs`):** Dedicated reserved cloud inference capacity insulating critical workloads from shared pay-as-you-go queue throttling (`429`).
- **RAG (`Retrieval-Augmented Generation`):** Grounding LLM generation in retrieved enterprise documents via vector/keyword search—requiring query-time document ACL enforcement.
- **Shadow AI:** Uninventoried generative models, personal chatbot accounts, browser plug-ins, or embedded vendor AI features adopted outside organizational oversight.
- **Small Language Model (`SLM`):** Compact specialized or distilled model deployed efficiently inside VPCs or edge layers—reducing inference cost, latency, and carbon energy cleanly on narrow workflows.
- **Sponge Examples:** Adversarially crafted inputs maximizing activation density or output length to slow neural inference and degrade availability (`Shumailov et al.`).
- **Stop-the-Line Authority:** Formal cultural and governance power authorizing any engineer, QA analyst, or reviewer to halt deployment on safety or fairness concerns without penalty.
- **Sycophancy:** Model tendency learned from human preference rewards to validate flawed user premises, praise weak reasoning, or abandon accuracy to please users (`Sharma et al.`, GPT-4o 2025 rollback).
- **Vector Database:** Specialized store indexing high-dimensional semantic embeddings for similarity search—carrying plaintext-equivalent privacy sensitivity (`vec2text`) and `NIST SP 800-88r2` sanitization duties.
- **Zero Data Retention (`ZDR`):** Binding vendor commitment ensuring API prompts and model completions are processed ephemerally in memory and never stored persistently or reused for training.

---

## Appendix J: References & Further Reading

The full **Annotated Bibliography** immediately following this section catalogs all **234 verified primary sources** (standards, academic papers, incident postmortems, judicial decisions, and global statutes) cited across the handbook—each accompanied by direct URLs, DOIs, audience tags, and exact chapter links. Use the eight thematic clusters below to locate canonical primary readings quickly inside the Annotated Bibliography:

1. **Core Governance Frameworks & Standards:** Begin with **NIST** *AI Risk Management Framework (AI RMF 1.0)* (`NIST AI 100-1`) and *Generative AI Profile* (`NIST AI 600-1`), **ISO/IEC** *42001:2023*, *42005:2025*, *42006:2025*, and *23894:2023*, **NIST** *CSF 2.0* (`CSWP 29`), **COSO**'s *Developing Key Risk Indicators*, **IIA** *Global Internal Audit Standards (2025)*, and **Paulk et al.**'s *Capability Maturity Model (`CMM v1.1`)*.
2. **Adversarial Security, Agents & Threat Taxonomies:** Consult **MITRE ATLAS**, **NIST** *Adversarial Machine Learning Taxonomy* (`NIST AI 100-2 E2025`), **OWASP** *Top 10 for LLM Applications 2025*, *Top 10 for Agentic Applications for 2026*, and *Non-Human Identities Top 10: 2025*, **UK NCSC**'s *"confusable deputy"* guidance, **Debenedetti et al.** (*CaMeL*), **Nasr et al.** (*"The Attacker Moves Second"*), **Willison** (*Prompt Injection* & *Lethal Trifecta*), **Munoz et al.** (*PyRIT*), **Derczynski et al.** (*garak*), and **Mazeika et al.** (*HarmBench*).
3. **Data Protection, Privacy & Supply-Chain Integrity:** Reference **Microsoft Presidio**, **Pang et al.** (*Google Zanzibar*), **Morris et al.** (*`vec2text`*), **Lee et al.** (training deduplication), **NIST SP 800-88 Rev. 2** (*Media Sanitization*), **NIST SP 800-63B-4** (*Digital Identity*), **OpenSSF Model Signing (`OMS v1.0`)**, **OWASP/Ecma** *CycloneDX `ML-BOM`*, and **Linux Foundation** *SPDX v3.0 AI/Dataset Profiles*.
4. **Reliability, Evaluation, Fairness & Human Factors:** Examine **Es et al.** (*RAGAS*), **Zheng et al.** (*LLM-as-a-Judge*), **Kalai et al.** (*"Why Language Models Hallucinate"*), **Magesh et al.** (Stanford RegLab Legal RAG), **MLCommons** *AILuminate v1.0*, **NIST SP 1270** (*AI Bias*), **Kleinberg et al.** (fairness impossibility tradeoffs), **Sharma et al.** (sycophancy), **Bainbridge** (*Ironies of Automation*), **Goddard et al.** (automation bias), **Lee & See** (calibrated reliance), **Dell'Acqua et al.** (jagged frontier), and **Edmondson** (psychological safety).
5. **Global Horizontal & Sectoral AI Regulation:** Track binding obligations via the **EU AI Act (`Regulation (EU) 2024/1689`)** and **EU Digital Omnibus (`Regulation (EU) 2026/1744`)**, **GDPR**, **EU Whistleblowing Directive (`2019/1937`)**, **EU DORA (`2022/2554`)**, **NIS2 (`2022/2555`)**, **EU Data Act (`2023/2854`)**, **CSRD (`2022/2464`) / `ESRS E1`**, **UK PRA `SS1/21` / `PS21/3`**, **U.S. Federal Reserve `SR 26-2` / `SR 23-4`**, **FDA** *CDS & Predetermined Change Control Plans (`PCCP`)*, **HIPAA**, **SEC `Rule 21F-17` & Release `33-11216`**, **California** `AB 2013` / `SB 942` / `SB 53` / `CCPA ADMT`, **Colorado `SB 26-189`**, **Illinois `HB 3773`**, **India** `DPDP Act` & `RBI FREE-AI`, and **Singapore** `IMDA Agentic AI`.
6. **Landmark Court & Tribunal Rulings, Enforcement & Postmortems:** Study **Moffatt v. Air Canada** (`2024 BCCRT 149` tribunal decision), **Getty Images v. Stability AI**, **Thomson Reuters v. Ross Intelligence**, **Thaler v. Perlmutter**, **In re OpenAI** preservation orders, **FTC v. Rite Aid**, **SEC AI-Washing Releases**, **`EchoLeak` (`CVE-2025-32711`)**, **Arup HK\$200M deepfake**, **Samsung source leak**, **OpenAI** Redis cache spill (`Mar 2023`), K8s outage (`Dec 2024`), & GPT-4o sycophancy rollback (`Apr 2025`), and **Replit** production database deletion (`Jul 2025`).
7. **Operational Resilience, Lifecycle & Incident Response:** Pair **Chen et al.** (*ChatGPT Behavioral Drift*), **Sculley et al.** (*CACE Technical Debt*), **Shumailov et al.** (*Sponge Examples* & *Model Collapse*), and **He** (*LLM Nondeterminism*) with **NIST SP 800-160 Vol. 2 Rev. 1** (*Cyber-Resilient Systems*), **ISO 22301:2019 (+ Amd 1:2024)**, **NIST SP 800-61 Rev. 3** (*CSF 2.0 Incident Response*), **NIST SP 800-137** (*Continuous Monitoring — ISCM*), **OECD** *Defining AI Incidents*, and **OpenTelemetry** *GenAI Semantic Conventions*.
8. **AI Economics, FinOps & Environmental Sustainability:** Review **FinOps Foundation** *State of FinOps 2026*, **IEA** *Energy and AI (2025)*, **Luccioni et al.** (*Power Hungry Processing*), **IBM/Ponemon** *Cost of a Data Breach 2025*, **Gartner** *Agentic Cancellation Forecast*, **McKinsey** *State of AI 2025*, **Deloitte** *Governance of AI*, and **Microsoft & LinkedIn** *Work Trend Index*.

Continue directly to the **Annotated Bibliography** below for full citation details, DOIs, hyperlinks, and chapter cross-references.
