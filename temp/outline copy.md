# Building Guardrails for Enterprise AI
## Hardening Enterprise AI Against Hallucinations, Hacks, and Liability

---
## Potential alternative titles

- Permissions, Not Prompts: The Practical Handbook of Enterprise AI Security, Risk, and Governance
- Governing the Probabilistic Enterprise: Security, Compliance, and Trust in the Age of AI Agents
- Beyond the Prompt: Hardening AI Against Hallucinations, Hacks, and Liability

---

## Front Matter
- **Foreword:** Guardrails help you go faster, they don't slow you down
- **How to Use This Handbook:** reading paths by role (see table below) 
- **Executive Summary:** the top 10 enterprise AI risks on one page 
- **A Shared Vocabulary:** key terms everyone should know (full glossary in Appendix I) 

---

## Part I: Foundations 

### Chapter 1: Why AI Risk Is Different
- 1.1 Probabilistic systems in a deterministic enterprise
  - Six incidents that highlighted the AI Risk landscape - Next-token probability vs. deterministic software - temperature-zero variance in batched inference - why models bluff instead of abstaining - enterprise accountability for confident AI errors
- 1.2 When data becomes instructions: the root cause of prompt injection
  - Single token stream mixing system prompts and untrusted content - direct vs. indirect injection - why LLMs act as confusable deputies - designing beyond fragile filters
- 1.3 How fast things change: models, vendors, and regulations shifting every quarter
  - Silent vendor model updates and deprecations - shadow employee adoption outpacing policy - shifting legal deadlines like the EU Digital Omnibus - moving to continuous governance
- 1.4 From chatbots to agents: why the potential damage keeps growing
  - Five-level autonomy ladder from drafting to multi-agent execution - OWASP excessive agency and the lethal trifecta - why prompts are requests while permissions are enforceable controls
- 1.5 The Enterprise AI Risk Taxonomy: a one-page map of every risk in this handbook
  - Translating technical, legal, and risk vocabularies - seven accountability-based risk families - mapping chapters to NIST, OWASP, and MIT Risk Repository - causal analysis by intent

### Chapter 2: Reference Frameworks at a Glance
- 2.1 NIST AI Risk Management Framework & Generative AI Profile (NIST AI 600-1)
  - Govern, Map, Measure, and Manage functions - socio-technical framing of AI risk - twelve generative AI risk categories in AI 600-1 - practical action checklists for teams
- 2.2 ISO/IEC 42001 (AI Management System) and ISO/IEC 23894 (AI Risk Management)
  - Certifiable management system requirements under ISO 42001 - plan-do-check-act governance cycle - aligning AI risk management in ISO 23894 with existing ISO 27001 security programs
- 2.3 OWASP Top 10 for LLM Applications & OWASP Agentic AI guidance
  - Practitioner vulnerability list from prompt injection to unbounded consumption - RAG and vector weaknesses - emerging agentic threat patterns including tool misuse and identity spoofing
- 2.4 MITRE ATLAS (adversarial threat landscape for AI systems)
  - Adversarial tactics, techniques, and real-world attack case studies - mapping AI reconnaissance, poisoning, and exfiltration - integrating ATLAS matrices into enterprise threat modeling and SOC playbooks
- 2.5 How the frameworks fit together, and which one to start with
  - Comparing strategic governance, certifiable management, and engineering security frameworks - avoiding duplicate compliance work - choosing a starter stack based on company size and regulatory exposure

---

## Part II: Governance & Accountability 
*Moved up from the old closing chapter and expanded.*

### Chapter 3: Board & Executive Oversight
- 3.1 The board's duty of oversight for AI
  - Fiduciary care and Caremark-style oversight expectations - board committee allocation across audit, risk, and technology - avoiding rubber-stamping executive AI initiatives without independent challenge
- 3.2 Setting the enterprise AI risk appetite
  - Defining clear red lines for prohibited and high-risk use cases - linking autonomy thresholds to financial and reputational tolerance - documenting exceptions and executive sign-off authority
- 3.3 Board AI literacy: what directors need to understand
  - Core concepts directors must grasp without needing code - probabilistic failure modes, shadow AI, and vendor lock-in - structured briefing cadence and external expert advisory access
- 3.4 What the board should receive: AI risk reporting and dashboards
  - Quarterly board packet design - inventory coverage, high-risk system counts, incident trends, and shadow AI metrics - avoiding vanity adoption numbers that obscure operational risk
- 3.5 Investor disclosures and the risk of "AI-washing"
  - SEC and securities-regulator scrutiny of exaggerated AI claims - substantiating public capability statements - aligning earnings-call narratives with actual production controls and risk-factor filings
- 3.6 Risk transfer and AI insurance: auditing Cyber, E&O, and D&O coverage for silent AI exclusions
  - Auditing existing Cyber, E&O, and D&O policies for silent generative-AI exclusions - evaluating affirmative AI endorsements and performance warranties - aligning insurance limits with agentic blast radius

### Chapter 4: The AI Governance Operating Model
- 4.1 The cross-functional AI Governance Council ↪
  - Charter, membership, and decision rights across technology, security, data, legal, and business - escalation paths for disputed use cases - avoiding slow, bureaucratic review bottlenecks
- 4.2 Roles & accountability: CEO, CIO, CISO, CDO, CRO, General Counsel, DPO, AI leads, business owners
  - Clear ownership boundaries across executive and technical leaders - preventing diffusion of responsibility - assigning named business-owner accountability for every deployed AI system
- 4.3 Applying the Three Lines of Defense to AI
  - First-line engineering and product controls - second-line risk, compliance, and privacy oversight - third-line internal audit independence - adapting model-risk governance without paralyzing delivery
- 4.4 Centralized, federated, or hub-and-spoke: choosing a Center of Excellence model
  - Comparing centralized control, federated business-unit autonomy, and hub-and-spoke Centers of Excellence - staffing reusable guardrail platforms - evolving the operating model as AI maturity grows

### Chapter 5: Policies, Inventory & Risk Tiering
- 5.1 Turning Responsible AI principles into policies you can enforce 
  - Translating high-level fairness and transparency pledges into testable rules - writing clear policy owners, exceptions, and enforcement triggers - retiring vague aspirational AI ethics statements
- 5.2 The employee AI Acceptable Use Policy 
  - Defining approved tools, prohibited data types, and verification duties - clear rules on code, customer data, and personal accounts - communicating expectations without relying on fear
- 5.3 The central AI registry & AI Bill of Materials (AI-BOM) ↪
  - Single source of truth for all internal, vendor, and embedded AI systems - tracking models, datasets, prompts, and owners - maintaining a live AI-BOM for audits
- 5.4 Risk-tiering method: low, medium, high, prohibited ↪
  - Scoring use cases by data sensitivity, external exposure, autonomy, and legal impact - aligning internal tiers with regulatory classifications - triggering proportional review depth automatically
- 5.5 The Traffic Light intake process (Green / Yellow / Red lanes) ↪
  - Fast-tracking low-risk internal productivity tools in days - standard privacy and permission checks for yellow-lane workflows - deep red-teaming and executive sign-off for red-lane systems
- 5.6 Architectural risk selection: how governance duties shift across SaaS, RAG, fine-tuning, and custom models
  - Comparing compliance burdens across off-the-shelf SaaS, RAG, fine-tuning, and custom training - avoiding accidental deployer-to-provider shifts under EU AI Act Article 25

---

## Part III: Data Risk

### Chapter 6: Data Leakage & Shadow AI
- 6.1 External data leakage and model-training risk
  - How prompts, source code, and customer PII leave the perimeter - consumer vs. enterprise API retention defaults - why leaked trade secrets cannot be unlearned easily
- 6.2 The Shadow AI problem
  - Why employees use personal AI accounts after blanket bans - discovering unsanctioned tools via DNS, CASB, and browser telemetry - replacing prohibition with safe, sanctioned alternatives
- 6.3 "Embedded AI": when existing SaaS tools quietly add AI features 
  - Silent AI rollouts inside CRM, email, and office suites - default opt-in settings that bypass procurement review - auditing and disabling risky vendor features centrally
- 6.4 Sanctioned AI gateways and Zero Data Retention (ZDR)
  - Routing all model traffic through an internal proxy - enforcing Zero Data Retention contracts and technical opt-outs - centralizing rate limits, logging, and approved model access
- 6.5 Data Loss Prevention (DLP) and PII redaction pipelines
  - Detecting and masking secrets, API keys, and PII before prompts leave - tuning regex and NER classifiers for low latency - balancing false positives against productivity

### Chapter 7: Internal Over-Exposure & Permission-Aware AI
- 7.1 The "insider access" problem: AI as a super-search engine
  - How enterprise copilots surface forgotten HR, M&A, and salary files - turning dormant over-shared folders into instant data exposure - real-world internal leak scenarios
- 7.2 Fixing file permissions before rollout 
  - Auditing SharePoint, Google Drive, and Slack permissions prior to indexing - removing "anyone with the link" access - running permission-hygiene sprints before launching enterprise search
- 7.3 Data classification and sensitivity labels 
  - Tagging documents as public, internal, confidential, or restricted - blocking restricted labels from AI indexing pipelines - enforcing sensitivity inheritance when AI summarizes protected files
- 7.4 Permission-aware retrieval (RAG that respects access control)
  - Propagating user ACLs into vector database queries - post-retrieval filtering vs. index-time security trimming - preventing cross-tenant and cross-department leakage in shared embedding stores

### Chapter 8: Data Provenance, Consent & Sovereignty 
- 8.1 Lineage and provenance for training and grounding data
  - Tracking where documents, fine-tuning datasets, and embeddings originate - removing stale, contradictory, or unverified sources - maintaining audit-ready data lineage across RAG pipelines
- 8.2 Consent and purpose limitation: is this data allowed to be used for AI?
  - Checking customer contracts, privacy notices, and GDPR purpose-limitation rules - distinguishing service delivery from model training - securing valid opt-ins before reusing personal data
- 8.3 Data residency, sovereignty, and cross-border transfers
  - Keeping prompts, embeddings, and inference within regional boundaries - navigating Schrems II, localization mandates, and sovereign cloud options - verifying vendor sub-processor locations
- 8.4 The "right to be forgotten" in vector stores and model weights ↪
  - Propagating GDPR and CCPA deletion requests across chunked vector indexes - why erasing personal data from fine-tuned weights fails - preferring RAG over weight memorization
- 8.5 Synthetic data: benefits, limits, and re-identification risk
  - Generating privacy-preserving test and training datasets - testing for memorization and linkage attacks - avoiding model collapse and hidden bias amplification in synthetic corpora

---

## Part IV: Security

### Chapter 9: The AI Threat Landscape 
- 9.1 Mapping AI threats to OWASP LLM Top 10 and MITRE ATLAS
  - Connecting application vulnerabilities to adversarial tactics - prioritizing threats across chatbots, RAG, and autonomous agents - building a shared security baseline for engineering and SecOps
- 9.2 Threat modeling for AI systems and agents
  - Extending STRIDE to probabilistic components, retrieval stores, and tool connectors - mapping trust boundaries and blast radius - running lightweight threat models during design reviews
- 9.3 Who is attacking AI systems, and why
  - Profiling threat actors from financially motivated fraudsters to nation-state groups and curious insiders - common targets including IP theft, fraud, brand damage, and compute abuse

### Chapter 10: Prompt Injection & Manipulation
- 10.1 Direct prompt injection and jailbreaks
  - Role-play, encoding, and multi-turn techniques that bypass safety instructions - why system-prompt hardening alone fails - assessing real business impact beyond embarrassing chatbot replies
- 10.2 Indirect prompt injection: the Trojan Horse in documents, emails, and web pages
  - Hiding instructions inside emails, PDFs, tickets, and web pages - lessons from EchoLeak - defending against zero-click exfiltration when assistants read untrusted external content
- 10.3 System prompt leakage 
  - Extracting confidential instructions, business logic, and tool schemas via crafted queries - avoiding secrets in system prompts - treating prompt text as potentially public information
- 10.4 Input/output guardrail models, and what they can't catch 
  - Deploying classifier firewalls for toxicity, PII, and injection detection - latency and bypass trade-offs - why guardrails act as speed bumps rather than complete security boundaries

### Chapter 11: Securing AI Agents (expanded) 
- 11.1 Excessive agency and how much damage an agent can do
  - Over-broad tool permissions, destructive actions, and runaway loops - breaking Simon Willison's lethal trifecta - scoping agent capabilities strictly to minimum required business tasks
- 11.2 Non-human identities: how agents authenticate and what they're authorized to do 
  - Issuing distinct service identities instead of sharing user admin tokens - short-lived, task-scoped OAuth credentials - auditing delegated "on-behalf-of" actions across enterprise APIs
- 11.3 Tool and connector security (MCP servers, plugins, APIs) 
  - Vetting third-party MCP servers and plugins for tool poisoning and rug pulls - validating schemas and parameter bounds - pinning trusted tool versions in production
- 11.4 Risks when multiple agents work together or talk to each other 
  - Cascading errors, conflicting goals, and cross-agent prompt propagation - enforcing message authentication between orchestrator and worker agents - preserving end-to-end trace IDs for accountability
- 11.5 Human approval gates and kill switches 
  - Designing step-up confirmation for payments, deletions, and external emails - enforcing hard financial and rate limits in code - testing global and per-agent emergency kill switches
- 11.6 Sandboxing code execution and browser agents 
  - Running agent-generated code and web browsing inside ephemeral, isolated containers - blocking lateral network movement and local filesystem access - enforcing strict CPU and memory quotas

### Chapter 12: Model & Supply Chain Security
- 12.1 Poisoning of training data, models, and knowledge bases
  - Sleeper backdoors in fine-tuning corpora and RAG poisoning via public wikis or tickets - verifying ingestion sources - detecting anomalous retrieval patterns and sudden behavioral shifts
- 12.2 Open-weight model provenance and scanning (malicious model files) 
  - Arbitrary code execution risks in pickle files vs. Safetensors - verifying cryptographic hashes and publisher signatures - scanning downloaded weights and tokenizers before internal hosting
- 12.3 Model theft, extraction, and inversion attacks 
  - Reconstructing proprietary models or sensitive features through repeated API queries - rate limiting, output perturbation, and watermarking - protecting high-value custom models from distillation theft
- 12.4 Membership inference and training-data extraction 
  - Detecting whether specific individuals' records appeared in training data - preventing verbatim memorization of secrets and PII - applying differential privacy and deduplication during fine-tuning
- 12.5 AI-BOM and SBOM for the AI supply chain
  - Cataloging base models, LoRA adapters, datasets, vector stores, and Python dependencies - tracking CVEs and license obligations - automating supply-chain checks inside CI/CD pipelines

### Chapter 13: Infrastructure & Operational Security 
- 13.1 Managing API keys and secrets for model providers
  - Eliminating hardcoded keys in notebooks and repositories - centralizing credentials in secrets vaults and AI gateways - automating key rotation and per-team spend alerts
- 13.2 Unbounded consumption and "denial-of-wallet" attacks
  - Preventing attackers or infinite agent loops from exhausting token budgets and GPU capacity - enforcing per-user quotas, context caps, and circuit breakers on API spend
- 13.3 Securing prompt and response logs (logs are sensitive data too)
  - Protecting observability traces that capture PII, credentials, and trade secrets - encrypting, masking, and setting strict retention windows - restricting developer access to production logs
- 13.4 Vector database security and tenant isolation
  - Securing unauthenticated vector endpoints and weak network rules - enforcing namespace or metadata-based tenant isolation - preventing embedding inversion and cross-customer data leakage

### Chapter 14: AI-Enabled External Threats 
- 14.1 Deepfakes and voice cloning used for executive fraud
  - Real-time audio and video impersonation in wire-transfer scams like Arup - establishing out-of-band callback verification and code words - training finance and executive-assistant teams
- 14.2 Phishing and social engineering at AI scale
  - Hyper-personalized spear-phishing in fluent local languages using scraped context - upgrading email security and MFA to phishing-resistant FIDO2 - running realistic AI-era phishing simulations
- 14.3 Synthetic identities and bypassing KYC checks
  - AI-generated IDs, deepfake liveness spoofing, and automated account creation - layering device intelligence, behavioral biometrics, and document forensics into onboarding and fraud workflows
- 14.4 Fighting back: using AI defensively in the Security Operations Center
  - Accelerating alert triage, log correlation, and threat hunting with governed SOC copilots - validating AI-generated detections against false positives - keeping analysts in command of containment actions

---

## Part V: Output, Trust & Liability

### Chapter 15: Hallucinations & Reliability
- 15.1 Confident hallucinations in high-stakes workflows
  - Why fluent fabrications slip past human reviewers - high-risk exposure in legal, medical, financial, and support settings - quantifying acceptable error tolerances by workflow
- 15.2 Grounding with citations and permission to say "I don't know"
  - Anchoring answers to retrieved source passages with clickable citations - prompting and scoring models to abstain on missing evidence - verifying citation faithfulness automatically
- 15.3 Hand rules and math to deterministic code
  - Separating language understanding from calculations, pricing, and policy eligibility checks - using structured tool calls to deterministic engines - eliminating arithmetic and rule-lookup hallucinations
- 15.4 Legal liability for what your AI says (*Moffatt v. Air Canada*, corrected)
  - Examining the British Columbia Civil Resolution Tribunal ruling - why chatbots cannot be disclaimed as separate entities - contractual and consumer-protection exposure for automated promises
- 15.5 Sycophancy, anthropomorphism, and manipulative outputs: preventing false authority and emotional over-reliance
  - Mitigating model sycophancy that validates false user beliefs - curbing anthropomorphic persona design - preventing manipulative nudging and psychological harm in customer-facing assistants

### Chapter 16: Bias, Fairness & Discrimination
- 16.1 Where bias comes from: data, design, and deployment
  - Historical disparities in training data, proxy variables, and language-performance gaps - deployment drift when tools serve unintended populations - intersectional fairness challenges
- 16.2 High-risk use cases: hiring, credit, insurance, healthcare, education
  - Disparate-impact risks in automated screening, lending, pricing, and triage - real regulatory enforcement cases - why sensitive decisions demand stricter statistical validation and human recourse
- 16.3 Fairness testing and independent bias audits 
  - Measuring demographic parity, equalized odds, and error-rate gaps - designing pre-deployment bias evaluations - meeting NYC Local Law 144 and EU high-risk audit expectations

### Chapter 17: Human Oversight & Automation Bias 
- 17.1 Real human control vs. rubber-stamping
  - Why nominal "human-in-the-loop" reviewers miss errors under time pressure - cognitive fatigue and automation bias - designing interfaces that surface uncertainty and require active judgment
- 17.2 Choosing the design: human-in-the-loop, human-on-the-loop, or human-out-of-the-loop
  - Matching oversight patterns to decision speed, reversibility, and harm severity - when synchronous approval helps vs. when asynchronous monitoring and sampling work better
- 17.3 Calibrating trust: avoiding both over-reliance and outright rejection
  - Helping staff know when to trust, verify, or override AI outputs - showing confidence cues and source links - preventing deskilling and silent tool abandonment
- 17.4 Contestability and human redress: giving affected customers and employees a way to appeal AI decisions
  - Designing clear appeal channels for rejected applicants and customers - meeting EU AI Act right-to-explanation and complaint duties - empowering human reviewers to overturn automated outcomes

### Chapter 18: Transparency, Disclosure & Content Provenance 
- 18.1 Telling people when they're interacting with AI
  - Clear, timely disclosures for chatbots, voice agents, and automated decisions - meeting EU AI Act Article 50 and consumer-protection rules without degrading user experience
- 18.2 Labeling AI-generated content: watermarking and C2PA content credentials
  - Cryptographic provenance with C2PA metadata vs. imperceptible watermarks - resilience limits when images or text are cropped - practical enterprise rules for external marketing assets
- 18.3 Explainability: what LLMs can realistically explain
  - Distinguishing persuasive post-hoc rationalizations from true causal reasons - using retrieved evidence, rule traces, and feature attributions where explanations are legally required
- 18.4 Documentation: model cards, system cards, and datasheets
  - Standardizing intended use, known limitations, training data summaries, and evaluation results - keeping living documentation synchronized across model and prompt updates

### Chapter 19: Intellectual Property & Licensing
- 19.1 Inbound risk: generated output that infringes someone else's rights
  - Copyright, trademark, and trade-dress exposure from memorized training content - guarding against lookalike brand assets and verbatim text reproduction in external marketing and products
- 19.2 Outbound risk: who owns and can protect AI-generated work?
  - Human-authorship thresholds for copyright protection across major jurisdictions - documenting meaningful human creative control - protecting competitive advantage when AI outputs lack exclusivity
- 19.3 Open-weight model licenses and their usage restrictions 
  - Navigating custom commercial, revenue-cap, and acceptable-use clauses in Llama, Gemma, and Mistral licenses - avoiding distribution triggers and non-commercial traps in enterprise products
- 19.4 Open-source license contamination in AI-generated code 
  - Detecting copyleft snippets (GPL/AGPL) suggested by coding assistants - running automated code-provenance scanners in CI/CD - setting developer guidelines for generated code review
- 19.5 Vendor IP indemnification: what it covers and what it doesn't
  - Examining defense caps, customer-prompt exclusions, and required guardrail settings in vendor indemnities - why indemnification supplements rather than replaces internal IP hygiene

---

## Part VI: Regulation & Compliance

### Chapter 20: The Global Regulatory Landscape
- 20.1 EU AI Act: risk tiers, deployer-to-provider shifts (Art. 25), GPAI obligations, timelines, penalties (corrected)
  - Risk classification, prohibited practices, Article 25 value-chain shifts, GPAI rules, and revised Digital Omnibus timelines - tiered penalty ceilings up to 7% - extraterritorial reach
- 20.2 United States: federal policy and the patchwork of state and local laws (e.g., Colorado, California, NYC Local Law 144, Illinois)
  - Navigating FTC, EEOC, and DOJ enforcement under existing laws alongside Colorado, California, Illinois, and NYC rules - managing conflicting state deadlines and exemptions
- 20.3 India: DPDP Act & Rules, MeitY AI Governance Guidelines, sector regulators (RBI, SEBI, IRDAI) 
  - Consent, notice, and breach duties under the DPDP framework - MeitY's risk-graded governance principles - RBI FREE-AI, SEBI, and IRDAI expectations for regulated Indian firms
- 20.4 Asia-Pacific & beyond: China, South Korea, Japan, Singapore (Model AI Governance Framework, AI Verify), UK, Canada 
  - Comparing Singapore's practical AI Verify toolkit and South Korea's Basic Act - China's algorithm filings - Japan's soft-law approach and UK sector-regulator guidance
- 20.5 Managing compliance across jurisdictions: build once, comply many times 
  - Designing a unified control baseline mapped to the strictest common requirements - isolating jurisdiction-specific add-ons like local disclosures and filings - avoiding fragmented compliance silos

### Chapter 21: Sector-Specific Requirements 
- 21.1 Financial services: model risk management (e.g., SR 11-7), EU DORA, RBI guidance
  - Adapting SR 11-7 validation to generative models - operational resilience and third-party oversight under DORA - fair-lending, credit explainability, and algorithmic trading controls
- 21.2 Healthcare & life sciences: HIPAA, AI-enabled medical devices
  - Protecting PHI under HIPAA and Business Associate Agreements - FDA and EU MDR boundaries for Software as a Medical Device - clinical safety validation
- 21.3 Employment & HR: works councils, employee monitoring, automated hiring decisions
  - High-risk classification of recruiting, screening, and performance-scoring AI - co-determination duties with European works councils - candidate notice, opt-outs, and bias-audit obligations
- 21.4 Public sector and critical infrastructure
  - Procurement transparency, algorithmic impact disclosures, and citizen due-process rights - heightened resilience and human-oversight rules for energy, transport, telecom, and public-safety systems

### Chapter 22: Auditability, Assessments & Evidence
- 22.1 The "black box" problem
  - Why auditors reject "the model decided" - reconstructing context when models, prompts, and knowledge bases evolve - bridging technical telemetry with legal defensibility
- 22.2 Tamper-proof logging and decision replay ↪
  - Capturing immutable records of prompts, retrieved chunks, model versions, parameters, tool calls, and outputs - balancing audit retention against privacy and storage cost
- 22.3 Impact assessments: DPIA, Fundamental Rights Impact Assessment (FRIA), algorithmic impact assessments 
  - When privacy, fundamental-rights, or algorithmic assessments are mandatory - integrating them into one unified intake workflow - documenting residual risk and stakeholder consultation
- 22.4 Conformity assessments and certification (e.g., ISO/IEC 42001) 
  - Preparing technical documentation and quality-management evidence for EU conformity assessments - navigating ISO/IEC 42001 external certification audits - closing common evidence gaps
- 22.5 Preparing for internal and external AI audits 
  - Organizing an audit-ready evidence binder - testing control effectiveness over sample transactions - coaching engineering, legal, and product teams for formal auditor walkthroughs
- 22.6 e-Discovery, legal hold, and retention governance for prompts, agent traces, and AI meeting transcripts
  - Managing litigation discovery risks for employee prompts, copilot histories, and AI meeting transcripts - suspending automated deletion during legal holds - setting defensible retention schedules

---

## Part VII: Third-Party & Lifecycle Risk 

### Chapter 23: Vendor & Third-Party AI Risk 
- 23.1 Due diligence for AI vendors and model providers
  - Evaluating security posture, training-data provenance, eval methodology, and financial stability - spotting vendor "AI-washing" claims - scoring third-party tools before pilot sign-off
- 23.2 Contract clauses that matter: ZDR, training opt-out, data location, sub-processors, audit rights, incident notification, indemnity
  - Essential redlines for AI MSAs and DPAs - securing Zero Data Retention, model-change notice, sub-processor transparency, breach SLAs, and meaningful IP indemnification
- 23.3 Concentration risk and provider lock-in
  - Managing dependence on a small number of frontier model providers and cloud GPUs - designing model-agnostic abstractions, portable prompts, and exit strategies
- 23.4 Fourth-party risk: the AI vendors your vendors rely on
  - Uncovering hidden foundation-model APIs inside SaaS suppliers - mapping downstream sub-processors - ensuring your security and residency commitments flow through to fourth parties
- 23.5 AI due diligence in M&A and investments: spotting algorithmic disgorgement, poisoned weights, and license traps
  - Assessing target companies for unconsented training data and FTC-style algorithmic disgorgement exposure - auditing open-source code contamination, undocumented models, and inherited regulatory liabilities

### Chapter 24: Model Lifecycle & Change Management 
- 24.1 Model versioning and vendor-forced deprecation
  - Pinning exact model snapshots in production - tracking vendor retirement calendars - running parallel shadow evaluations before migrating workflows to newer model releases
- 24.2 Re-validating when the underlying model changes
  - Defining materiality triggers for re-testing prompts, guardrails, and safety filters - automating regression gates in CI/CD before promoting model or retrieval updates
- 24.3 Drift, degradation, and continuous monitoring ↪
  - Detecting data drift, shifting user behavior, rising hallucination rates, and silent safety-refusal decay - combining automated LLM-as-judge checks with targeted human sampling
- 24.4 Decommissioning AI systems safely
  - Archiving audit logs and revoking agent credentials or API keys - purging vector indexes - notifying affected stakeholders and updating the central AI registry

### Chapter 25: Operational Resilience & Business Continuity 
- 25.1 Provider outages, rate limits, and routing to a fallback model
  - Architecting multi-region and multi-provider gateways - handling 429 throttling and latency spikes - validating fallback models so failover doesn't weaken safety guardrails
- 25.2 Graceful degradation: what happens when the AI is unavailable?
  - Designing deterministic fallbacks, queued processing, and manual backup workflows - preventing single-point AI outages from halting core customer service or business operations
- 25.3 Including AI in business continuity and disaster recovery plans
  - Setting RTO/RPO targets for vector stores, gateways, and model endpoints - running tabletop exercises for model-provider outages and corrupted knowledge bases

---

## Part VIII: Operationalizing the Guardrails

### Chapter 26: Testing, Evaluation & Red-Teaming 
- 26.1 Pre-deployment evals and golden datasets
  - Building domain-specific golden test sets with legal and business experts - measuring factual accuracy, groundedness, refusal quality, and latency before production launch
- 26.2 AI red-teaming: scope, methods, and who should do it
  - Combining automated attack probes with adversarial human testers - scoping jailbreaks, indirect injection, bias, and agent tool abuse - scheduling pre-launch and periodic exercises
- 26.3 Safety and security benchmarks
  - Understanding public safety benchmarks vs. enterprise-specific risk tests - avoiding benchmark gaming - calibrating pass thresholds to each system's assigned risk tier
- 26.4 Go/no-go criteria for production
  - Defining measurable release gates across accuracy, security, privacy, and fallback readiness - documenting formal executive risk acceptance when minor gaps remain

### Chapter 27: AI Incident Response 
- 27.1 What counts as an "AI incident"?
  - Classifying prompt-injection exploits, data leaks, severe hallucinations, biased decisions, and runaway agents - integrating AI severity tiers into existing SecOps incident taxonomies
- 27.2 Playbooks: prompt injection, data leak, harmful output, runaway agent
  - Step-by-step containment, credential revocation, kill-switch activation, and log preservation playbooks - rehearsing incident response roles across security, engineering, legal, and communications teams
- 27.3 Regulatory notification obligations (e.g., EU AI Act serious-incident reporting, data-breach laws)
  - Meeting tight statutory clocks under the EU AI Act, GDPR, DPDP, and sector regulators - coordinating legal privilege and customer notifications
- 27.4 Post-incident review and feeding lessons back into guardrails
  - Conducting blameless root-cause analyses after failures - turning real production incidents into permanent regression evals, updated DLP rules, and tighter agent permissions

### Chapter 28: Metrics, KRIs & Reporting 
- 28.1 Key Risk Indicators (KRIs) for AI
  - Tracking shadow AI usage, unvetted high-risk tools, and policy violations - monitoring guardrail bypass rates and recurring incident counts with clear alert thresholds
- 28.2 Governance KPIs: time-to-approve, how much of your AI is in the inventory, eval pass rates
  - Measuring governance speed alongside safety - tracking intake turnaround time, registry completeness across business units, vendor-review SLAs, and automated eval coverage
- 28.3 Board-level AI risk dashboard template
  - Structuring a concise one-page executive scorecard - pairing risk posture, compliance readiness, and incident trends with clear red-amber-green actions and owners
- 28.4 AI FinOps, token economics, and environmental footprint: governing compute cost, zombie pilots, and ESG impact
  - Enforcing per-workflow token budgets, small-model routing, and business-unit chargebacks - sunsetting low-ROI zombie pilots - tracking inference energy and carbon metrics for ESG disclosures

### Chapter 29: Building a Risk-Aware AI Culture 
- 29.1 AI literacy programs (incl. EU AI Act Art. 4 obligations)
  - Designing practical, mandatory literacy programs that explain capabilities, hallucination limits, and data hygiene - evidencing compliance with EU AI Act Article 4
- 29.2 Role-based training paths
  - Tailored curricula for boards, procurement, legal, security analysts, engineers, and everyday staff - focusing on real workplace scenarios rather than abstract ethics
- 29.3 Make the safe path the easy path
  - Offering fast, approved enterprise AI workspaces and pre-vetted templates - maintaining responsive intake lanes so employees choose sanctioned tools over shadow workarounds
- 29.4 Speak-up culture and whistleblower protections for reporting unsafe AI
  - Establishing confidential channels for engineers and domain staff to report bypassed guardrails or biased outputs - aligning internal escalation with statutory AI whistleblower protections

### Chapter 30: Governance Maturity Model & Roadmap
- 30.1 The five-level AI governance maturity model 
  - Assessing current posture from ad-hoc experimentation through repeatable, managed, and continuously optimized governance - benchmarking gaps across people, process, and technology
- 30.2 A 30/60/90-day action plan 
  - Concrete first-quarter execution sequence - inventory and AUP in 30 days - traffic-light intake and gateway in 60 - evals and incident playbooks in 90
- 30.3 From point-in-time sign-off to continuous governance ↪
  - Connecting registries, automated evals, and runtime telemetry - integrating regulatory monitoring into a living governance loop that scales safely with enterprise AI adoption

---

## Appendices 
- **A. Role-Based Cheat Sheets:** the top questions each role should ask before approving an AI project (Board, CEO, CIO, CISO, CDO/Data Stewards, GC/DPO, AI Engineers, Business Owners)
- **B. AI Governance RACI Matrix** (template)
- **C. AI Use-Case Intake & Risk-Tiering Form** (template)
- **D. AI Vendor Due Diligence Questionnaire** (template)
- **E. Employee AI Acceptable Use Policy** (template)
- **F. Pre-Flight Production Checklist** (go/no-go rubric)
- **G. Regulatory & Framework Crosswalk** (EU AI Act ↔ NIST AI RMF ↔ ISO 42001 ↔ OWASP)
- **H. AI Incident Response Playbook** (template)
- **I. Glossary of Terms**
- **J. References & Further Reading**

---

## Reading Paths by Role

| Role | Core chapters | Recommended |
|:---|:---|:---|
| **Board Members / CEO** | 1, 3, 5, 14, 28, 30 | 20, 23, App. A |
| **CIO** | 1, 4, 5, 23, 24, 25, 30 | 11, 13, 26 |
| **CISO / Security** | 9–14, 23, 27 | 6, 7, 26 |
| **CDO / Data Stewards** | 6, 7, 8, 15, 16, 22 | 5, 19, 24 |
| **General Counsel / Compliance / DPO** | 8, 18–22, 23 | 3, 16, 27 |
| **AI Engineers / Architects** | 1, 7, 10–13, 15, 26 | 17, 18, 24 |
| **Business & Product Owners** | 1, 5, 15, 16, 17 | 18, 29 |

