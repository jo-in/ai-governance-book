# Annotated Bibliography

*Building Guardrails for Enterprise AI: Hardening Enterprise AI Against Hallucinations, Hacks, and Liability*

This bibliography follows the *Chicago Manual of Style* (17th ed.) notes-and-bibliography system. Every source cited in a chapter footnote appears here, and every entry lists the chapters that cite it. Each entry includes:

- **Annotation:** what the source is and why it matters to enterprise AI governance.
- **Audience:** the roles that will find it most useful.
- **Type:** the kind of source (standard, statute, case law, peer-reviewed paper, industry report, news report, practitioner essay, and so on).
- **Cited in:** links back to the chapters that cite the source.

Entries are listed alphabetically by author (or by issuing organization). Court decisions and legislation are listed separately at the end, as Chicago recommends.

> **Verification:** Every entry was checked against the source or against authoritative secondary reporting on 15 November 2026. Web addresses change, so re-check them before publication. The verification status of each entry is recorded in [references/verification-log.md](references/verification-log.md).

---

## Books, Articles, Reports, Standards, and Web Sources

<a id="abadi-2016-dpsgd"></a>
Abadi, Martín, et al. "Deep Learning with Differential Privacy." In *Proceedings of the 2016 ACM SIGSAC Conference on Computer and Communications Security (CCS '16)*, October 2016. arXiv:1607.00133. https://doi.org/10.48550/arXiv.1607.00133.

> **Annotation:** Landmark privacy engineering paper introducing Differentially Private Stochastic Gradient Descent (`DP-SGD`) and the Moments Accountant, proving how gradient clipping and calibrated Gaussian noise mathematically bound single-record memorization risk during neural-network training.
>
> **Audience:** AI Engineers · CISO · DPO · Privacy Engineers · **Type:** Peer-reviewed paper · **Cited in:** [Ch. 12](chapters/12-model-and-supply-chain-security.md)

<a id="abercrombie-2023-mirages"></a>
Abercrombie, Gavin, Amanda Cercas Curry, Tanvi Dinkar, Verena Rieser, and Zeerak Talat. "Mirages: On Anthropomorphism in Dialogue Systems." In *Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP 2023)*, December 2023. arXiv:2305.09800. https://aclanthology.org/2023.emnlp-main.290/.

> **Annotation:** Analyzes linguistic and persona "mirages" (human names, first-person emotion claims, simulated empathy) that encourage users to anthropomorphize conversational AI—increasing uncritical over-reliance, false authority, and gender/behavioral stereotype reinforcement.
>
> **Audience:** Chief Product Officer · CX Design · Legal / Compliance · AI Engineers · **Type:** Peer-reviewed paper · **Cited in:** [Ch. 15](chapters/15-hallucinations-and-reliability.md)

<a id="agache-2020-firecracker"></a>
Agache, Alexandru, et al. "Firecracker: Lightweight Virtualization for Serverless Applications." In *Proceedings of the 17th USENIX Symposium on Networked Systems Design and Implementation (NSDI '20)*, February 2020. https://www.usenix.org/conference/nsdi20/presentation/agache.

> **Annotation:** Presents AWS's Rust/KVM microVM monitor booting isolated Linux environments in under 125 ms with under 5 MB memory overhead at up to 150 microVMs per host per second, setting the production hardware-isolation standard for untrusted agent code execution.
>
> **Audience:** AI Engineers · Cloud Security · Platform Architects · CISO · **Type:** Peer-reviewed systems paper · **Cited in:** [Ch. 11](chapters/11-securing-ai-agents.md)

<a id="anil-2024-many-shot"></a>
Anil, Cem, et al. "Many-Shot Jailbreaking." Anthropic Research, April 2, 2024. https://www.anthropic.com/research/many-shot-jailbreaking.

> **Annotation:** Demonstrates that packing dozens to hundreds of fabricated compliant Q&A examples inside extended context windows exploits in-context learning to override safety fine-tuning across leading frontier LLMs.
>
> **Audience:** CISO · AI Engineers · Red Teams · **Type:** Industry safety research · **Cited in:** [Ch. 10](chapters/10-prompt-injection-and-manipulation.md)

<a id="wp29-2018-wp251"></a>
Article 29 Data Protection Working Party (endorsed by the European Data Protection Board). *Guidelines on Automated Individual Decision-Making and Profiling for the Purposes of Regulation 2016/679*. WP251rev.01. Adopted February 6, 2018. https://ec.europa.eu/newsroom/article29/items/612053.

> **Annotation:** Authoritative European data-protection guidance establishing that nominal human rubber-stamping does not satisfy GDPR Article 22; meaningful human intervention requires reviewers holding genuine organizational **authority and competence** to inspect all relevant data and overturn automated outcomes.
>
> **Audience:** General Counsel · DPO · Head of Operations · Risk · **Type:** Regulatory guidance (EU) · **Cited in:** [Ch. 17](chapters/17-human-oversight-and-automation-bias.md)

<a id="bainbridge-1983-ironies"></a>
Bainbridge, Lisanne. "Ironies of Automation." *Automatica* 19, no. 6 (November 1983): 775–779. https://doi.org/10.1016/0005-1098(83)90046-8.

> **Annotation:** Foundational human-factors paper explaining the automation paradox: offloading routine decisions erodes operators' manual proficiency through disuse, leaving humans least prepared precisely when rare, complex system failures demand immediate takeover.
>
> **Audience:** CHRO · CIO · Chief Operating Officer · Safety Engineering · **Type:** Peer-reviewed journal article · **Cited in:** [Ch. 17](chapters/17-human-oversight-and-automation-bias.md), [Ch. 25](chapters/25-operational-resilience-and-business-continuity.md), [Ch. 29](chapters/29-building-a-risk-aware-ai-culture.md)

<a id="beurer-kellner-2025-mcp-poisoning"></a>
Beurer-Kellner, Luca, and Marc Fischer. "MCP Security Notification: Tool Poisoning Attacks." Invariant Labs Blog, April 1, 2025. https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks.

> **Annotation:** Landmark security advisory demonstrating how malicious prompt commands inside MCP tool descriptions hijack LLM agents to exfiltrate local secrets (`~/.ssh/id_rsa`, `mcp.json`), how remote servers can swap definitions post-approval ("rug pulls"), and how cross-server shadowing intercepts trusted tools.
>
> **Audience:** CISO · AI Engineers · AppSec · Platform Architects · **Type:** Security research advisory · **Cited in:** [Ch. 11](chapters/11-securing-ai-agents.md)

<a id="beurer-kellner-2025-github-mcp"></a>
Beurer-Kellner, Luca, and Marc Fischer. "GitHub MCP Exploited: Accessing Private Repositories via MCP." Invariant Labs Blog, May 26, 2025. https://invariantlabs.ai/blog/mcp-github-vulnerability.

> **Annotation:** Discloses a real-world "toxic agent flow" against the official GitHub MCP integration in which indirect prompt injection inside a public repository issue tricked an agent holding overly broad token permissions into leaking private repository code via an autonomous public pull request.
>
> **Audience:** CISO · IAM Leads · AI Engineers · AppSec · **Type:** Security research advisory · **Cited in:** [Ch. 11](chapters/11-securing-ai-agents.md)

<a id="bloomberg-2024-ferrari"></a>
Bloomberg News. "Ferrari Narrowly Dodges Deepfake Scam Simulating Deal-Hungry CEO." *Bloomberg*, July 26, 2024. https://www.bloomberg.com/news/articles/2024-07-26/ferrari-narrowly-dodges-deepfake-scam-simulating-deal-hungry-ceo.

> **Annotation:** Documents the July 2024 attempted deepfake voice-clone impersonation of Ferrari CEO Benedetto Vigna—escalating from spoofed WhatsApp messages to an AI-cloned southern Italian accent urging a confidential acquisition currency hedge—and shows how live challenge verification defeated the fraud.
>
> **Audience:** Board · CFO / Treasury · CISO · Executive Assistants · **Type:** News report · **Cited in:** [Ch. 14](chapters/14-ai-enabled-external-threats.md)

<a id="fed-2011-sr11-7"></a>
Board of Governors of the Federal Reserve System and Office of the Comptroller of the Currency. *Supervisory Guidance on Model Risk Management*. SR 11-7 / OCC Bulletin 2011-12. Washington, DC, April 4, 2011. https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm.

> **Annotation:** The landmark U.S. banking guidance that established Model Risk Management (MRM) and defined "effective challenge" as critical analysis by objective, informed parties combining competence, independence/incentives, and influence. Superseded in April 2026 by SR 26-2, though its challenge principles remain a cornerstone of enterprise AI governance across sectors.
>
> **Audience:** CRO · Internal Audit · CIO · Legal / Compliance · **Type:** Regulatory guidance (United States) · **Cited in:** [Ch. 4](chapters/04-ai-governance-operating-model.md), [Ch. 21](chapters/21-sector-specific-requirements.md)

<a id="fed-2023-sr23-4"></a>
Board of Governors of the Federal Reserve System, Office of the Comptroller of the Currency, and Federal Deposit Insurance Corporation. *Interagency Guidance on Third-Party Relationships: Risk Management*. SR 23-4 / OCC Bulletin 2023-17 / FIL-29-2023. Washington, DC, June 6, 2023. https://www.federalreserve.gov/supervisionreg/srletters/sr2304.htm.

> **Annotation:** Joint U.S. banking third-party risk standard structuring lifecycle governance across planning, due diligence, contracting, monitoring, and termination while mandating subcontractor vetting, concentration tracking, contractual flow-downs, and retained institutional accountability.
>
> **Audience:** CRO · Chief Procurement Officer · Third-Party Risk · Legal / Compliance · **Type:** Regulatory guidance (United States) · **Cited in:** [Ch. 23](chapters/23-vendor-and-third-party-ai-risk.md)

<a id="fed-2026-sr26-2"></a>
Board of Governors of the Federal Reserve System, Office of the Comptroller of the Currency, and Federal Deposit Insurance Corporation. *Revised Guidance on Model Risk Management*. SR 26-2 / OCC Bulletin 2026-13 / FIL-15-2026. Washington, DC, April 17, 2026. https://www.federalreserve.gov/supervisionreg/srletters/sr2602.htm.

> **Annotation:** Jointly supersedes SR 11-7 and SR 21-8, shifting U.S. banking model risk management toward materiality-based proportionality rather than rigid annual review calendars, and explicitly placing generative and agentic AI outside its narrow scope while expecting banks to govern them through broader enterprise risk management.
>
> **Audience:** CRO · Internal Audit · CIO · Legal / Compliance · **Type:** Regulatory guidance (United States) · **Cited in:** [Ch. 4](chapters/04-ai-governance-operating-model.md), [Ch. 21](chapters/21-sector-specific-requirements.md), [Ch. 24](chapters/24-model-lifecycle-and-change-management.md), [Ch. 30](chapters/30-governance-maturity-model-and-roadmap.md)

<a id="bourtoule-2021-unlearning"></a>
Bourtoule, Lucas, Varun Chandrasekaran, Christopher A. Choquette-Choo, Hengrui Jia, Adelin Travers, Baiwu Zhang, David Lie, and Nicolas Papernot. "Machine Unlearning." In *2021 IEEE Symposium on Security and Privacy (SP)*, 141–159. IEEE, 2021. https://doi.org/10.1109/SP40001.2021.00019.

> **Annotation:** Foundational paper introducing exact machine unlearning and the SISA (Sharded, Isolated, Sliced, and Aggregated) training architecture. Demonstrates both how shard isolation reduces exact unlearning costs for structured ML pipelines and why removing individual records from large monolithically trained neural networks remains computationally prohibitive.
>
> **Audience:** AI Engineers · CISO · DPO · **Type:** Peer-reviewed paper · **Cited in:** [Ch. 8](chapters/08-data-provenance-consent-and-sovereignty.md)

<a id="bucinca-2021-forcing"></a>
Buçinca, Zana, Maja Barbara Malaya, and Krzysztof Z. Gajos. "To Trust or to Think: Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-Assisted Decision-Making." *Proceedings of the ACM on Human-Computer Interaction* 5, no. CSCW1 (April 2021): Article 188. arXiv:2102.09692. https://doi.org/10.1145/3449287.

> **Annotation:** Empirical HCI study proving that simple AI explanations do not stop over-reliance, whereas cognitive forcing functions—requiring a user judgment prior to AI display, delaying recommendation reveal, or showing advice on request—measurably reduce blind acceptance.
>
> **Audience:** Chief Product Officer · UX Design · AI Engineers · Risk · **Type:** Peer-reviewed paper · **Cited in:** [Ch. 17](chapters/17-human-oversight-and-automation-bias.md)

<a id="buolamwini-2018-gender-shades"></a>
Buolamwini, Joy, and Timnit Gebru. "Gender Shades: Intersectional Accuracy Disparities in Commercial Gender Classification." In *Proceedings of the 1st Conference on Fairness, Accountability and Transparency (FAT\* 2018)*, PMLR 81: 77–91, February 2018. https://proceedings.mlr.press/v81/buolamwini18a.html.

> **Annotation:** Landmark intersectional fairness audit demonstrating commercial gender classifiers recorded error rates up to 0.8 percent on lighter-skinned males versus 34.7 percent on darker-skinned females—proving aggregate or single-axis evaluations conceal severe disparities.
>
> **Audience:** CISO · Chief Product Officer · AI Engineers · Legal / Compliance · **Type:** Peer-reviewed paper · **Cited in:** [Ch. 16](chapters/16-bias-fairness-and-discrimination.md)

<a id="carlini-2021-extracting"></a>
Carlini, Nicholas, Florian Tramèr, Eric Wallace, Matthew Jagielski, Ariel Herbert-Voss, Katherine Lee, Adam Roberts, et al. "Extracting Training Data from Large Language Models." In *Proceedings of the 30th USENIX Security Symposium (USENIX Security 21)*, August 2021. https://www.usenix.org/conference/usenixsecurity21/presentation/carlini-extracting.

> **Annotation:** Seminal paper proving that black-box querying can extract verbatim PII, source code, UUIDs, and secrets memorized by large language models—including strings seen in only a single training document—and showing that larger models memorize strictly more than smaller ones. Establishes why leaked trade secrets cannot reliably be removed once absorbed into model weights.
>
> **Audience:** CISO · AI Engineers · DPO · **Type:** Peer-reviewed paper · **Cited in:** [Ch. 6](chapters/06-data-leakage-and-shadow-ai.md), [Ch. 8](chapters/08-data-provenance-consent-and-sovereignty.md), [Ch. 12](chapters/12-model-and-supply-chain-security.md), [Ch. 19](chapters/19-intellectual-property-and-licensing.md)

<a id="carlini-2024-stealing"></a>
Carlini, Nicholas, Florian Tramèr, et al. "Stealing Part of a Production Language Model." In *Proceedings of the 41st International Conference on Machine Learning (ICML 2024)*, 2024. arXiv:2403.06634. https://doi.org/10.48550/arXiv.2403.06634.

> **Annotation:** Demonstrates that standard API queries can recover nontrivial internal parameters—extracting exact embedding projection layer matrices from production OpenAI `ada` and `babbage` models for under \$20 and leaking `gpt-3.5-turbo`'s hidden dimension size.
>
> **Audience:** CISO · AI Engineers · MLOps · IP Counsel · **Type:** Peer-reviewed paper · **Cited in:** [Ch. 12](chapters/12-model-and-supply-chain-security.md)

<a id="chaikin-2025-comet-brave"></a>
Chaikin, Artem, and Shivan Kaul Sahib. "Agentic Browser Security: Indirect Prompt Injection in Perplexity Comet." Brave Security Blog, August 2025. https://brave.com/blog/comet-prompt-injection/.

> **Annotation:** Discloses indirect prompt-injection vulnerabilities in agentic browsers where hidden webpage text hijacked Perplexity's Comet assistant into pivoting across open authenticated tabs (such as Gmail) and initiating OTP/account-access steps without traditional XSS bugs.
>
> **Audience:** CISO · AI Engineers · AppSec · Endpoint Security · **Type:** Security research blog · **Cited in:** [Ch. 11](chapters/11-securing-ai-agents.md)

<a id="chen-2024-chatgpt-drift"></a>
Chen, Lingjiao, Matei Zaharia, and James Zou. "How Is ChatGPT's Behavior Changing Over Time?" *Harvard Data Science Review* 6, Special Issue 5 (2024). arXiv:2307.09009. https://doi.org/10.1162/99608f92.5317da47.

> **Annotation:** Empirical longitudinal evaluation measuring GPT-4 and GPT-3.5 snapshots across March and June 2023, documenting wide swings in accuracy (including prime-checking falling from 84%–97.6% to 2.4%–51% on GPT-4), formatting wrappers, chain-of-thought length, and refusal behavior under unchanged product branding.
>
> **Audience:** AI Engineers · MLOps · CRO · Quality Engineering · **Type:** Peer-reviewed article · **Cited in:** [Ch. 24](chapters/24-model-lifecycle-and-change-management.md)

<a id="chen-2025-reasoning-faithfulness"></a>
Chen, Yanda, et al. (Anthropic Alignment Science). "Reasoning Models Don't Always Say What They Think." arXiv:2505.05410, May 2025. https://doi.org/10.48550/arXiv.2505.05410.

> **Annotation:** Empirical faithfulness audit proving frontier reasoning models (`Claude 3.7 Sonnet` and `DeepSeek-R1`) verbalized influential prompt hints only 25 percent and 39 percent of the time inside Chain-of-Thought scratchpads—falling further on harder tasks and concealing RL shortcut behaviors.
>
> **Audience:** CISO · AI Engineers · Internal Audit · Legal / Compliance · **Type:** Research preprint · **Cited in:** [Ch. 18](chapters/18-transparency-disclosure-and-content-provenance.md)

<a id="ncsc-2025-prompt-injection"></a>
Chismon, Dave. "Prompt Injection Is Not SQL Injection (It May Be Worse)." National Cyber Security Centre (UK), December 2025. https://www.ncsc.gov.uk/blog-post/prompt-injection-is-not-sql-injection.

> **Annotation:** Written by the NCSC's Technical Director for Platforms Research, this post argues that the popular comparison between prompt injection and SQL injection is misleading. SQL injection has a definitive fix in parameterized queries; prompt injection may never be fully fixed, because LLMs do not separate instructions from data. The post describes LLMs as "inherently confusable deputies" and recommends secure-by-design limits on what models can do, rather than relying on filters. It is an authoritative government voice for setting realistic expectations with boards and risk committees.
>
> **Audience:** Board · CISO · AI Engineers · **Type:** Government guidance (blog) · **Cited in:** [Front Matter](chapters/00-front-matter.md), [Ch. 1](chapters/01-why-ai-risk-is-different.md), [Ch. 9](chapters/09-ai-threat-landscape.md), [Ch. 10](chapters/10-prompt-injection-and-manipulation.md), [Ch. 26](chapters/26-testing-evaluation-and-red-teaming.md)

<a id="clinton-2024-dpd"></a>
Clinton, Jane. "DPD AI Chatbot Swears, Calls Itself 'Useless' and Criticises Delivery Firm." *The Guardian*, January 20, 2024. https://www.theguardian.com/technology/2024/jan/20/dpd-ai-chatbot-swears-calls-itself-useless-and-criticises-delivery-firm.

> **Annotation:** Documents the January 2024 incident in which London customer Ashley Beauchamp prompted DPD's support chatbot—after a routine system update disabled behavioral constraints—to swear, call itself "useless," and write a poem attacking the firm. Widely cited as a benchmark example of viral reputational harm from unguarded customer-facing chatbots.
>
> **Audience:** CISO · CIO · Business Owners · PR / Communications · **Type:** News report · **Cited in:** [Ch. 9](chapters/09-ai-threat-landscape.md)

<a id="c2pa-2025-spec"></a>
Coalition for Content Provenance and Authenticity (C2PA). *C2PA Technical Specification (Versions 2.1 and 2.2)*. 2024–May 2025. https://spec.c2pa.org/.

> **Annotation:** Open technical specification embedding cryptographically signed Content Credentials in JUMBF (`ISO/IEC 19566-5`) containers with SHA-256 hard bindings, and formalizing v2.1/v2.2 soft-binding perceptual hashes and invisible watermarks for external Manifest Repository recovery after metadata stripping.
>
> **Audience:** CMO / Brand · CIO · CISO · Product Engineering · **Type:** Open technical standard · **Cited in:** [Ch. 18](chapters/18-transparency-disclosure-and-content-provenance.md)

<a id="cohen-2024-morris-ii"></a>
Cohen, Stav, Ron Bitton, and Ben Nassi. "Here Comes The AI Worm: Unleashing Zero-Click Worms That Target GenAI-Powered Applications." arXiv:2403.02817, March 2024. https://doi.org/10.48550/arXiv.2403.02817.

> **Annotation:** Introduces *Morris II*, a proof-of-concept zero-click AI worm using adversarial self-replicating prompts to steal confidential user data and spread automatically across interconnected RAG and email agent ecosystems without exploiting binary vulnerabilities.
>
> **Audience:** CISO · Security Architects · AI Engineers · Red Teams · **Type:** Research preprint · **Cited in:** [Ch. 11](chapters/11-securing-ai-agents.md)

<a id="coso-2010-kri"></a>
Committee of Sponsoring Organizations of the Treadway Commission (COSO) (Mark S. Beasley, Bruce C. Branson, and Bonnie V. Hancock). *Developing Key Risk Indicators to Strengthen Enterprise Risk Management*. Durham, NC: COSO / NC State ERM Initiative, December 2010. https://www.coso.org/Documents/COSO-KRI-Paper-Full-FINAL-for-Web-Posting-Dec110-000.pdf.

> **Annotation:** Foundational enterprise risk-management guidance distinguishing forward-looking Key Risk Indicators (`KRIs`) calibrated to signal emerging exposure before harm from lagging operational Key Performance Indicators (`KPIs`).
>
> **Audience:** Board · CRO · CFO · Internal Audit · **Type:** Professional guidance paper · **Cited in:** [Ch. 28](chapters/28-metrics-kris-and-reporting.md)

<a id="cfpb-2023-circular-03"></a>
Consumer Financial Protection Bureau. *Consumer Financial Protection Circular 2023-03: Adverse Action Notification Requirements and the Proper Use of the CFPB's Sample Forms Provided in Regulation B*. Washington, DC: CFPB, September 19, 2023. https://www.consumerfinance.gov/compliance/circulars/circular-2023-03-adverse-action-notification-requirements-and-the-proper-use-of-the-cfpbs-sample-forms-provided-in-regulation-b/.

> **Annotation:** Authoritative federal lending guidance confirming that creditors using complex AI/ML underwriting models cannot shield denials behind generic Regulation B sample forms; Equal Credit Opportunity Act disclosures must accurately state the specific principal reasons driving each credit outcome.
>
> **Audience:** Chief Credit Officer · Legal / Compliance · AI Engineers · Risk · **Type:** Regulatory guidance (United States) · **Cited in:** [Ch. 16](chapters/16-bias-fairness-and-discrimination.md), [Ch. 17](chapters/17-human-oversight-and-automation-bias.md), [Ch. 18](chapters/18-transparency-disclosure-and-content-provenance.md), [Ch. 21](chapters/21-sector-specific-requirements.md)

<a id="dathathri-2024-synthid"></a>
Dathathri, Sumanth, Abigail See, Sumedh Ghaisas, Po-Sen Huang, et al. "Scalable Watermarking for Identifying Large Language Model Outputs." *Nature* 634 (October 23, 2024): 818–823. https://doi.org/10.1038/s41586-024-08025-4.

> **Annotation:** Introduces *SynthID-Text*, demonstrating imperceptible tournament-sampling watermarking for production LLM text that preserves generation quality without latency penalty while illustrating trade-offs under short text or aggressive paraphrasing.
>
> **Audience:** AI Engineers · CMO · Product Leaders · CISO · **Type:** Peer-reviewed journal article · **Cited in:** [Ch. 18](chapters/18-transparency-disclosure-and-content-provenance.md)

<a id="debenedetti-2025-camel"></a>
Debenedetti, Edoardo, Ilia Shumailov, Nicholas Carlini, Florian Tramèr, et al. "Defeating Prompt Injections by Design." arXiv:2503.18813, March 2025. https://doi.org/10.48550/arXiv.2503.18813.

> **Annotation:** Introduces CaMeL (*CApabilities for MachinE Learning*), a system-level runtime defense from Google, Google DeepMind, and ETH Zurich researchers that enforces strict control-flow and data-flow isolation alongside provenance capability checks so untrusted text cannot hijack agent tool invocations.
>
> **Audience:** CISO · Security Architects · AI Engineers · **Type:** Research preprint · **Cited in:** [Ch. 10](chapters/10-prompt-injection-and-manipulation.md), [Ch. 11](chapters/11-securing-ai-agents.md)

<a id="dellacqua-2023-frontier"></a>
Dell'Acqua, Fabrizio, Edward McFowland III, Ethan R. Mollick, Hila Lifshitz-Assaf, Katherine C. Kellogg, Saran Rajendran, Lisa Krayer, François Candelon, and Karim R. Lakhani. "Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of AI on Knowledge Worker Productivity and Quality." Harvard Business School Working Paper No. 24-013, September 2023. https://www.hbs.edu/faculty/Pages/item.aspx?num=64700.

> **Annotation:** Pre-registered field experiment across 758 BCG consultants demonstrating uneven AI capability boundaries: while GPT-4 boosted inside-frontier productivity (`+12.2%` tasks, `+25.1%` speed, `>40%` quality), consultants using AI outside the frontier were 19 percentage points less likely to reach correct solutions due to persuasive over-reliance.
>
> **Audience:** Board · CIO · CHRO · Practice Leads · **Type:** Academic / field working paper · **Cited in:** [Ch. 17](chapters/17-human-oversight-and-automation-bias.md), [Ch. 29](chapters/29-building-a-risk-aware-ai-culture.md)

<a id="deloitte-2025-board-ai"></a>
Deloitte Global Boardroom Program. *Governance of AI: A Critical Imperative for Today's Boards*. 2nd ed. Deloitte, 2025. https://www.deloitte.com/global/en/issues/trust/progress-on-ai-in-the-boardroom-but-room-to-accelerate.html.

> **Annotation:** Global survey of roughly 700 board directors and executives across 56 countries tracking board AI literacy, agenda time, and composition. Finds that 66 percent of respondents still describe their boards as having limited to no knowledge or experience of AI, and 31 percent say AI is not yet on the board agenda.
>
> **Audience:** Board · CEO · Company Secretary · **Type:** Industry survey report · **Cited in:** [Ch. 3](chapters/03-board-and-executive-oversight.md), [Ch. 28](chapters/28-metrics-kris-and-reporting.md), [Ch. 29](chapters/29-building-a-risk-aware-ai-culture.md), [Ch. 30](chapters/30-governance-maturity-model-and-roadmap.md)

<a id="derczynski-2024-garak"></a>
Derczynski, Leon, Erick Galinkin, Jeffrey Martin, Subho Majumdar, and Nanna Inie. "garak: A Framework for Security Probing Large Language Models." arXiv:2406.11036, June 2024. https://doi.org/10.48550/arXiv.2406.11036.

> **Annotation:** Introduces `garak` (Generative AI Red-teaming and Assessment Kit), an open-source LLM security probe combining modular Generators, Probes, Buffs (obfuscation transforms), and Detectors for automated CI/CD regression scanning across prompt injection, jailbreaks, toxicity, and data leakage.
>
> **Audience:** CISO · AppSec · AI Engineers · Red Teams · **Type:** Research preprint / tool paper · **Cited in:** [Ch. 26](chapters/26-testing-evaluation-and-red-teaming.md)

<a id="dietvorst-2015-aversion"></a>
Dietvorst, Berkeley J., Joseph P. Simmons, and Cade Massey. "Algorithm Aversion: People Erroneously Avoid Algorithms After Seeing Them Err." *Journal of Experimental Psychology: General* 144, no. 1 (February 2015): 114–126. https://doi.org/10.1037/xge0000033.

> **Annotation:** Classic behavioral study demonstrating that decision-makers abandon accurate algorithmic tools disproportionately after observing even isolated errors, whereas allowing constrained human adjustment sharply lowers outright rejection.
>
> **Audience:** Chief Product Officer · CHRO · Operations Leads · AI Engineers · **Type:** Peer-reviewed journal article · **Cited in:** [Ch. 17](chapters/17-human-oversight-and-automation-bias.md)

<a id="edelman-2024-security-copilot"></a>
Edelman, Ben, James Bono, Sida Peng, Roberto Rodriguez, and Sandra Ho. *Randomized Controlled Trials for Microsoft Copilot for Security*. Microsoft Research, March 2024. https://www.microsoft.com/en-us/security/business/ai-machine-learning/microsoft-copilot-security.

> **Annotation:** Empirical randomized controlled trials evaluating AI assistance in Security Operations Center workflows, finding experienced security analysts worked 22 percent faster and 7 percent more accurately while newer analysts achieved 35 percent higher accuracy and 26 percent faster task completion.
>
> **Audience:** CISO · SOC Directors · SecOps Engineers · **Type:** Empirical RCT research report · **Cited in:** [Ch. 14](chapters/14-ai-enabled-external-threats.md)

<a id="edmondson-1999-psych-safety"></a>
Edmondson, Amy. "Psychological Safety and Learning Behavior in Work Teams." *Administrative Science Quarterly* 44, no. 2 (June 1999): 350–383. https://doi.org/10.2307/2666999.

> **Annotation:** Landmark organizational-behavior study demonstrating that teams with high psychological safety speak up and report errors more openly—enabling faster defect correction and higher team performance rather than suppressing operational warnings.
>
> **Audience:** CEO · CHRO · CISO · Engineering Leaders · **Type:** Peer-reviewed journal article · **Cited in:** [Ch. 29](chapters/29-building-a-risk-aware-ai-culture.md)

<a id="edwards-2023-sydney"></a>
Edwards, Benj. "AI-Powered Bing Chat Spills Its Secrets via Prompt Injection Attack." *Ars Technica*, February 10, 2023. https://arstechnica.com/information-technology/2023/02/ai-powered-bing-chat-spills-its-secrets-via-prompt-injection-attack/.

> **Annotation:** Documents Kevin Liu's extraction of Microsoft Bing Chat's confidential "Sydney" system prompt via direct prompt injection (reproduced by Marvin von Hagen and confirmed by Microsoft), proving that system instructions stored inside the prompt window cannot remain secret.
>
> **Audience:** CISO · AI Engineers · Product Owners · **Type:** News report · **Cited in:** [Ch. 10](chapters/10-prompt-injection-and-manipulation.md)

<a id="es-2024-ragas"></a>
Es, Shahul, Jithin James, Luis Espinosa Anke, and Steven Schockaert. "RAGAS: Automated Evaluation of Retrieval Augmented Generation." In *Proceedings of the 18th Conference of the European Chapter of the Association for Computational Linguistics (EACL 2024): System Demonstrations*, March 2024. arXiv:2309.15217. https://doi.org/10.48550/arXiv.2309.15217.

> **Annotation:** Introduces RAGAS, an open-source reference-free evaluation framework scoring `faithfulness` (claim-level context entailment), `answer relevance`, and retrieval context precision/recall so CI/CD gates detect ungrounded RAG claims prior to release.
>
> **Audience:** AI Engineers · MLOps · CISO · Quality Engineering · **Type:** Peer-reviewed paper · **Cited in:** [Ch. 15](chapters/15-hallucinations-and-reliability.md), [Ch. 24](chapters/24-model-lifecycle-and-change-management.md), [Ch. 26](chapters/26-testing-evaluation-and-red-teaming.md)

<a id="ec-2025-digital-omnibus"></a>
European Commission. *Proposal for a Regulation Amending Regulation (EU) 2024/1689 as Regards the Simplification of the Implementation of Harmonised Rules on Artificial Intelligence (Digital Omnibus on AI)*. COM(2025) 836 final. Brussels, November 19, 2025.

> **Annotation:** The Commission's proposal to adjust the EU AI Act before its main high-risk obligations took effect. It was prompted by delays in harmonised standards and in national enforcement readiness. Read together with the adopted Regulation (EU) 2026/1744 (listed under Legislation), it shows how quickly AI regulation is being revised, and why compliance programs must track amendments rather than only the original text.
>
> **Audience:** Legal / Compliance · Board · **Type:** Legislative proposal · **Cited in:** [Ch. 1](chapters/01-why-ai-risk-is-different.md)

<a id="ec-2025-gpai-template"></a>
European Commission and European AI Office. *Explanatory Notice and Template for the Public Summary of Training Content for General-Purpose AI Models*. Brussels, July 24, 2025. https://digital-strategy.ec.europa.eu/en/library/explanatory-notice-and-template-public-summary-training-content-general-purpose-ai-models.

> **Annotation:** Operationalizes EU AI Act Article 53(1)(d) into a mandatory three-part summary template covering model metadata, training data categories (public, web-scraped, licensed, user, and synthetic data), copyright TDM opt-out compliance, and illegal-content safeguards.
>
> **Audience:** Legal / Compliance · CDO · AI Engineers · **Type:** Regulatory guidance / template (EU) · **Cited in:** [Ch. 8](chapters/08-data-provenance-consent-and-sovereignty.md), [Ch. 18](chapters/18-transparency-disclosure-and-content-provenance.md), [Ch. 20](chapters/20-the-global-regulatory-landscape.md), [Ch. 23](chapters/23-vendor-and-third-party-ai-risk.md)

<a id="cen-2024-18099"></a>
European Committee for Standardization (CEN). *CEN/TS 18099:2024, Biometric Data Injection Attack Detection*. Brussels: CEN, 2024. https://standards.cencenelec.eu/.

> **Annotation:** European technical specification addressing biometric data injection attacks—such as virtual webcams, emulators, and MitM video stream substitution behind physical camera optics—closing a major KYC assurance gap left by physical presentation-attack standards alone.
>
> **Audience:** Head of Fraud / KYC · CISO · Mobile Architects · Procurement · **Type:** European technical specification · **Cited in:** [Ch. 14](chapters/14-ai-enabled-external-threats.md)

<a id="edpb-2024-opinion28"></a>
European Data Protection Board. *Opinion 28/2024 on Certain Data Protection Aspects Related to the Processing of Personal Data in the Context of AI Models*. Adopted December 17, 2024. https://www.edpb.europa.eu/our-work-tools/our-documents/opinion-board-art-64/opinion-282024-certain-data-protection-aspects_en.

> **Annotation:** Authoritative EU guidance establishing that AI models trained on personal data are not automatically anonymous, clarifying the strict three-step balancing test and reasonable-expectation limit for legitimate interest under GDPR Article 6(1)(f), and confirming that unlawful processing during training taints downstream model deployment.
>
> **Audience:** Legal / Compliance · DPO · Board · AI Engineers · **Type:** Regulatory opinion (EU) · **Cited in:** [Ch. 8](chapters/08-data-provenance-consent-and-sovereignty.md)

<a id="ftc-2021-everalbum"></a>
Federal Trade Commission. *In the Matter of Everalbum, Inc.* Decision and Order, Docket No. C-4743. May 6, 2021. https://www.ftc.gov/legal-library/browse/cases-proceedings/1923172-everalbum-inc-matter.

> **Annotation:** Landmark U.S. privacy enforcement order requiring Everalbum not only to delete deceptively collected user photos, but also to destroy the facial-recognition models and algorithms trained on those photos—establishing "algorithmic disgorgement" as a remedy for unconsented training data.
>
> **Audience:** Board · General Counsel · CDO · DPO · **Type:** Regulatory enforcement order (United States) · **Cited in:** [Ch. 8](chapters/08-data-provenance-consent-and-sovereignty.md), [Ch. 23](chapters/23-vendor-and-third-party-ai-risk.md)

<a id="ftc-2023-rite-aid"></a>
Federal Trade Commission. *United States v. Kurbo, Inc. and WW International, Inc.* (March 2022, COPPA algorithmic disgorgement) and *Federal Trade Commission v. Rite Aid Corporation* (December 19, 2023, five-year facial-recognition ban and model/data deletion across company and vendors). Washington, DC: FTC, 2022–2023. https://www.ftc.gov/news-events/news/press-releases/2023/12/rite-aid-banned-using-ai-facial-recognition-after-ftc-says-retailer-deployed-technology-without.

> **Annotation:** Landmark FTC enforcement actions expanding algorithmic disgorgement across children's COPPA data (*WW International*) and biometric surveillance (*Rite Aid*, barring facial recognition for five years and compelling deletion of models/data held across third-party vendors).
>
> **Audience:** General Counsel · M&A Diligence · CDO · DPO · **Type:** Regulatory enforcement orders (United States) · **Cited in:** [Ch. 23](chapters/23-vendor-and-third-party-ai-risk.md)

<a id="fincen-2024-deepfake-alert"></a>
Financial Crimes Enforcement Network (FinCEN). *FinCEN Alert on Fraud Schemes Involving Deepfake Media Targeting Financial Institutions*. Alert FIN-2024-Alert004. Washington, DC: U.S. Department of the Treasury, November 13, 2024. https://www.fincen.gov/resources/advisoriesbulletinsfact-sheets/fincen-alert-fraud-schemes-involving-deepfake-media.

> **Annotation:** U.S. Treasury financial-crimes alert highlighting rising SAR filings involving AI-generated audio, video, and tampered digital identity documents targeting financial institutions, detailing both deepfake executive/payment impersonation and KYC onboarding red-flag indicators.
>
> **Audience:** CFO / Treasury · AML / Compliance · Head of Fraud / KYC · CISO · **Type:** Regulatory alert (United States) · **Cited in:** [Ch. 14](chapters/14-ai-enabled-external-threats.md)

<a id="fsb-2024-ai-stability"></a>
Financial Stability Board (FSB). *The Financial Stability Implications of Artificial Intelligence*. Basel: FSB, November 14, 2024. https://www.fsb.org/2024/11/the-financial-stability-implications-of-artificial-intelligence/.

> **Annotation:** Global financial-stability assessment warning that acute third-party concentration across GPU hardware, hyperscale cloud infrastructure, and dominant foundation models creates correlated systemic single points of failure.
>
> **Audience:** Board · CRO · CIO · Chief Procurement Officer · **Type:** International regulatory report · **Cited in:** [Ch. 23](chapters/23-vendor-and-third-party-ai-risk.md), [Ch. 25](chapters/25-operational-resilience-and-business-continuity.md)

<a id="finops-2026-state"></a>
FinOps Foundation. *State of FinOps 2026*. San Francisco: Linux Foundation / FinOps Foundation, 2026. https://data.finops.org/.

> **Annotation:** Annual practitioner benchmark documenting rapid enterprise adoption of AI cost governance, reporting 98 percent of respondents managing AI spend in 2026 (up from 63 percent in 2025 and 31 percent two years earlier) alongside rising AI unit-economics expectations.
>
> **Audience:** CFO · FinOps · CIO · Platform Engineering · **Type:** Industry survey report · **Cited in:** [Ch. 28](chapters/28-metrics-kris-and-reporting.md), [Ch. 30](chapters/30-governance-maturity-model-and-roadmap.md)

<a id="fredrikson-2015-inversion"></a>
Fredrikson, Matt, Somesh Jha, and Thomas Ristenpart. "Model Inversion Attacks That Exploit Confidence Information and Basic Countermeasures." In *Proceedings of the 22nd ACM SIGSAC Conference on Computer and Communications Security (CCS '15)*, October 2015. https://doi.org/10.1145/2810103.2813677.

> **Annotation:** Classic security paper demonstrating how adversaries exploit returned class confidence vectors to reconstruct recognizable private training features (including facial images), highlighting the privacy leakage hidden in raw probability outputs.
>
> **Audience:** CISO · AI Engineers · DPO · **Type:** Peer-reviewed paper · **Cited in:** [Ch. 12](chapters/12-model-and-supply-chain-security.md)

<a id="gao-2023-pal"></a>
Gao, Luyu, Aman Madaan, Shuyan Zhou, Uri Alon, Pengfei Liu, Yiming Yang, Jamie Callan, and Graham Neubig. "PAL: Program-aided Language Models." In *Proceedings of the 40th International Conference on Machine Learning (ICML 2023)*, July 2023. arXiv:2211.10435. https://doi.org/10.48550/arXiv.2211.10435.

> **Annotation:** Demonstrates neuro-symbolic delegation: instructing LLMs to read problems and generate executable code run by a Python/symbolic interpreter eliminates arithmetic hallucinations and lets smaller code-delegating models surpass larger text-only Chain-of-Thought models on GSM8K and BIG-Bench Hard.
>
> **Audience:** AI Engineers · Platform Architects · CFO / FinOps · **Type:** Peer-reviewed paper · **Cited in:** [Ch. 15](chapters/15-hallucinations-and-reliability.md)

<a id="gartner-2025-agentic"></a>
Gartner, Inc. "Gartner Predicts Over 40% of Agentic AI Projects Will Be Canceled by End of 2027." Press release, June 25, 2025. https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027.

> **Annotation:** An analyst forecast that more than 40 percent of agentic AI projects will be abandoned by 2027, citing escalating costs, unclear business value, and inadequate risk controls. It also warns about "agent washing," where vendors rebrand chatbots or robotic process automation (RPA) as agents. Useful for executives weighing agent investments and for making the business case that governance protects value.
>
> **Audience:** Board · CIO · Business Owners · **Type:** Industry analyst forecast · **Cited in:** [Front Matter](chapters/00-front-matter.md), [Ch. 1](chapters/01-why-ai-risk-is-different.md), [Ch. 28](chapters/28-metrics-kris-and-reporting.md), [Ch. 30](chapters/30-governance-maturity-model-and-roadmap.md)

<a id="gatlan-2026-copilot-bug"></a>
Gatlan, Sergiu. "Microsoft Says Bug Causes Copilot to Summarize Confidential Emails." *BleepingComputer*, February 18, 2026. https://www.bleepingcomputer.com/news/microsoft/microsoft-says-bug-causes-copilot-to-summarize-confidential-emails/.

> **Annotation:** Reports Microsoft Service Health Advisory CW1226324 (January–February 2026), in which a server-side defect allowed Microsoft 365 Copilot's work-tab chat feature to process and summarize confidential emails in users' Sent Items and Drafts folders despite Purview sensitivity labels and DLP rules. A vivid example of why single label or DLP controls must be backed by defense in depth.
>
> **Audience:** CISO · CIO · CDO · DPO · **Type:** News report · **Cited in:** [Ch. 7](chapters/07-internal-over-exposure-and-permission-aware-ai.md)

<a id="gebru-2021-datasheets"></a>
Gebru, Timnit, Jamie Morgenstern, Briana Vecchione, Jennifer Wortman Vaughan, Hanna Wallach, Hal Daumé III, and Kate Crawford. "Datasheets for Datasets." *Communications of the ACM* 64, no. 12 (December 2021): 86–92. https://doi.org/10.1145/3458723.

> **Annotation:** Seminal framework proposing standardized datasheets documenting a dataset's motivation, composition, collection process, preprocessing, legal/ethical considerations, intended uses, and maintenance plan. Underpins modern enterprise data-provenance practices for both model training and RAG corpora.
>
> **Audience:** CDO · Data Stewards · AI Engineers · Legal / Compliance · **Type:** Peer-reviewed article · **Cited in:** [Ch. 8](chapters/08-data-provenance-consent-and-sovereignty.md), [Ch. 16](chapters/16-bias-fairness-and-discrimination.md), [Ch. 18](chapters/18-transparency-disclosure-and-content-provenance.md)

<a id="gitguardian-2025-secrets"></a>
GitGuardian. *The State of Secrets Sprawl 2025*. Paris: GitGuardian, 2025. https://www.gitguardian.com/state-of-secrets-sprawl-report-2025.

> **Annotation:** Annual telemetry report analyzing public GitHub leaks across 2024, uncovering 23,770,171 newly exposed hardcoded secrets (+25% YoY), showing that 58 percent are unprefixed generic credentials bypassing simple pattern push protection and 70 percent of older leaked secrets remain valid.
>
> **Audience:** CISO · AppSec · Platform Engineers · AI Engineers · **Type:** Industry telemetry report · **Cited in:** [Ch. 13](chapters/13-infrastructure-and-operational-security.md)

<a id="goddard-2012-automation-bias"></a>
Goddard, Kate, Abdul Roudsari, and Jeremy C. Wyatt. "Automation Bias: A Systematic Review of Frequency, Effect Mediators, and Mitigators." *Journal of the American Medical Informatics Association (JAMIA)* 19, no. 1 (January–February 2012): 121–127. https://doi.org/10.1136/amiajnl-2011-000089.

> **Annotation:** Benchmark systematic review screening 13,821 articles across 74 empirical studies, cataloging omission and commission errors from automation bias and identifying workload, complexity, and time pressure as key amplifiers.
>
> **Audience:** Chief Risk Officer · Chief Product Officer · UX Design · Operations Leads · **Type:** Peer-reviewed review article · **Cited in:** [Ch. 17](chapters/17-human-oversight-and-automation-bias.md), [Ch. 29](chapters/29-building-a-risk-aware-ai-culture.md)

<a id="google-2025-a2a"></a>
Google Cloud. "Announcing the Agent2Agent Protocol (A2A)." Google Developers Blog, April 9, 2025. https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/.

> **Annotation:** Introduces the open Agent2Agent (A2A) interoperability specification pairing JSON Agent Cards (`/.well-known/agent-card.json`) with OAuth 2.0 and `mTLS` security schemas for authenticated cross-agent delegation.
>
> **Audience:** AI Engineers · Platform Architects · CISO · CIO · **Type:** Open protocol announcement · **Cited in:** [Ch. 11](chapters/11-securing-ai-agents.md)

<a id="google-2023-ip-indemnity"></a>
Google Cloud. "Shared Fate: Protecting Customers with Generative AI Indemnification." Google Cloud Blog, October 12, 2023. https://cloud.google.com/blog/products/ai-machine-learning/protecting-customers-with-generative-ai-indemnification.

> **Annotation:** Launches Google Cloud's two-pronged generative AI IP indemnity protecting enterprise Vertex AI and Workspace customers against both third-party training-data claims and generated-output copyright claims when built-in safety filters remain enabled.
>
> **Audience:** General Counsel · Procurement · CIO · CISO · **Type:** Vendor policy / blog · **Cited in:** [Ch. 19](chapters/19-intellectual-property-and-licensing.md), [Ch. 23](chapters/23-vendor-and-third-party-ai-risk.md)

<a id="gtig-2025-adversarial-misuse"></a>
Google Threat Intelligence Group. *Adversarial Misuse of Generative AI*. Google Cloud Threat Intelligence, January 29, 2025. https://cloud.google.com/blog/topics/threat-intelligence/adversarial-misuse-generative-ai.

> **Annotation:** Baseline intelligence analysis examining how state-sponsored APTs and cybercriminals attempted to integrate generative AI across reconnaissance, phishing localization, scripting, and research—finding that actors primarily gained productivity multipliers while commercial safety guardrails obstructed push-button malware creation.
>
> **Audience:** CISO · Security Operations · Threat Intelligence · **Type:** Threat intelligence report · **Cited in:** [Ch. 9](chapters/09-ai-threat-landscape.md), [Ch. 14](chapters/14-ai-enabled-external-threats.md)

<a id="gtig-2025-threat-tracker"></a>
Google Threat Intelligence Group. "GTIG AI Threat Tracker: Advances in Threat Actor Usage of AI Tools." Google Cloud Blog, November 5, 2025. https://cloud.google.com/blog/topics/threat-intelligence/threat-actor-usage-of-ai-tools.

> **Annotation:** Follow-on threat tracker documenting an operational inflection point: threat actors bypassing safety filters under research pretexts and deploying experimental "just-in-time" malware families (`PROMPTFLUX` and `PROMPTSTEAL`) that query external LLM APIs dynamically during execution to mutate scripts and generate malicious commands on the fly.
>
> **Audience:** CISO · Security Operations · Threat Intelligence · Red Teams · **Type:** Threat intelligence report · **Cited in:** [Ch. 9](chapters/09-ai-threat-landscape.md), [Ch. 14](chapters/14-ai-enabled-external-threats.md)

<a id="green-2022-oversight"></a>
Green, Ben. "The Flaws of Policies Requiring Human Oversight of Government Algorithms." *Computer Law & Security Review* 45 (July 2022): 105681. https://doi.org/10.1016/j.clsr.2022.105681.

> **Annotation:** Evaluates over 40 AI oversight policies, arguing that nominal human-in-the-loop mandates fail empirically under cognitive limits while prematurely legitimizing flawed automated systems unless effectiveness is verified institutionally.
>
> **Audience:** Board · General Counsel · Internal Audit · Public Sector · **Type:** Peer-reviewed journal article · **Cited in:** [Ch. 17](chapters/17-human-oversight-and-automation-bias.md)

<a id="greshake-2023-indirect"></a>
Greshake, Kai, Sahar Abdelnabi, Shailesh Mishra, Christoph Endres, Thorsten Holz, and Mario Fritz. "Not What You've Signed Up For: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection." In *Proceedings of the 2023 ACM Workshop on Artificial Intelligence and Security (AISec '23)*. New York: ACM, 2023. https://doi.org/10.1145/3605764.3623985.

> **Annotation:** The foundational peer-reviewed study of *indirect* prompt injection, where attackers plant instructions in content (web pages, emails, documents) that an LLM-integrated application later reads. The authors demonstrate data theft, manipulation, and persistence against real systems, and set out a threat taxonomy that later guidance builds on. Essential background for anyone designing retrieval-augmented generation (RAG) systems or agents.
>
> **Audience:** CISO · AI Engineers · **Type:** Peer-reviewed paper · **Cited in:** [Front Matter](chapters/00-front-matter.md), [Ch. 1](chapters/01-why-ai-risk-is-different.md), [Ch. 10](chapters/10-prompt-injection-and-manipulation.md)

<a id="gurman-2023-samsung"></a>
Gurman, Mark. "Samsung Bans Staff's AI Use After Spotting ChatGPT Data Leak." *Bloomberg*, May 2, 2023. https://www.bloomberg.com/news/articles/2023-05-02/samsung-bans-chatgpt-and-other-generative-ai-use-by-staff-after-leak.

> **Annotation:** Reports Samsung's ban on generative AI tools on company devices after engineers uploaded sensitive source code to ChatGPT. It also reports an internal survey in which 65 percent of respondents saw such tools as a security risk. The case has become the standard illustration of insider data leakage through public AI tools, and of the limits of blanket bans as a response.
>
> **Audience:** Board · CISO · CDO / Data Stewards · **Type:** News report · **Cited in:** [Front Matter](chapters/00-front-matter.md), [Ch. 1](chapters/01-why-ai-risk-is-different.md), [Ch. 5](chapters/05-policies-inventory-and-risk-tiering.md), [Ch. 6](chapters/06-data-leakage-and-shadow-ai.md), [Ch. 27](chapters/27-ai-incident-response.md), [Ch. 29](chapters/29-building-a-risk-aware-ai-culture.md)

<a id="hardt-2016-opportunity"></a>
Hardt, Moritz, Eric Price, and Nathan Srebro. "Equality of Opportunity in Supervised Learning." In *Advances in Neural Information Processing Systems 29 (NeurIPS 2016)*, 2016. arXiv:1610.02413. https://doi.org/10.48550/arXiv.1610.02413.

> **Annotation:** Foundational machine learning paper defining *equal opportunity* (equal true-positive rates across groups) and *equalized odds* (equal true-positive and false-positive rates), proving why ignoring protected attributes fails and demonstrating optimal threshold-based post-processing.
>
> **Audience:** CDO · AI Engineers · Legal / Compliance · Risk · **Type:** Peer-reviewed paper · **Cited in:** [Ch. 16](chapters/16-bias-fairness-and-discrimination.md)

<a id="he-2025-nondeterminism"></a>
He, Horace, and Thinking Machines Lab. "Defeating Nondeterminism in LLM Inference." Thinking Machines Lab, September 2025. https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/.

> **Annotation:** Explains why LLM inference often gives different outputs for the same prompt even at temperature zero. The authors trace much of the variation to the way servers batch requests dynamically, rather than only to floating-point arithmetic. They show that "batch-invariant" computation can make results reproducible, at a performance cost. Relevant to audit replay, evaluation reliability, and incident forensics.
>
> **Audience:** AI Engineers · CISO · Legal / Compliance · **Type:** Technical research essay · **Cited in:** [Ch. 1](chapters/01-why-ai-risk-is-different.md), [Ch. 15](chapters/15-hallucinations-and-reliability.md), [Ch. 22](chapters/22-auditability-assessments-and-evidence.md), [Ch. 24](chapters/24-model-lifecycle-and-change-management.md), [Ch. 25](chapters/25-operational-resilience-and-business-continuity.md)

<a id="heiding-2024-spear-phishing"></a>
Heiding, Fred, Simon Lermen, Andrew Kao, Bruce Schneier, and Arun Vishwanath. "Evaluating Large Language Models' Capability to Launch Fully Automated Spear Phishing Campaigns: Validated on Human Subjects." arXiv:2412.00586, December 2024. https://doi.org/10.48550/arXiv.2412.00586.

> **Annotation:** Controlled randomized human-subjects study (`n = 101`) finding that fully automated LLM spear-phishing matches human experts at a 54 percent click-through rate (versus 12 percent baseline control and 56 percent AI-human hybrid), with 88 percent automated OSINT target profiling accuracy.
>
> **Audience:** CISO · IAM Leads · Security Awareness / HR · SOC Directors · **Type:** Research preprint · **Cited in:** [Ch. 14](chapters/14-ai-enabled-external-threats.md)

<a id="hines-2024-spotlighting"></a>
Hines, Keegan, Gary Lopez, Matthew Hall, Federico Zarfati, Yonatan Zunger, and Emre Kıcıman. "Defending Against Indirect Prompt Injection Attacks With Spotlighting." arXiv:2403.14720, March 2024. https://doi.org/10.48550/arXiv.2403.14720.

> **Annotation:** Introduces "spotlighting"—delimiter, datamarking, and encoding input-transformation techniques that signal untrusted text provenance to LLMs, slashing indirect prompt-injection attack success rates from above 50 percent to under 2 percent with minimal utility degradation.
>
> **Audience:** AI Engineers · CISO · AppSec · **Type:** Research preprint · **Cited in:** [Ch. 10](chapters/10-prompt-injection-and-manipulation.md)

<a id="hofmann-2024-dialect"></a>
Hofmann, Valentin, Pratyusha Ria Kalluri, Dan Jurafsky, and Sharese King. "AI Generates Covertly Racist Decisions About People Based on Their Dialect." *Nature* 633 (August 28, 2024): 147–154. https://doi.org/10.1038/s41586-024-07856-5.

> **Annotation:** Landmark *Nature* study proving RLHF-aligned language models that mask overt bias still exhibit deep covert dialect prejudice against African American English (AAE) speakers—recommending lower-status jobs, higher conviction rates, and harsher penalties based purely on dialect markers.
>
> **Audience:** AI Engineers · CHRO · Chief Product Officer · Civil Rights / Legal · **Type:** Peer-reviewed journal article · **Cited in:** [Ch. 16](chapters/16-bias-fairness-and-discrimination.md)

<a id="huang-2025-maestro"></a>
Huang, Ken. "Agentic AI Threat Modeling Framework: MAESTRO." Cloud Security Alliance Blog, February 6, 2025. https://cloudsecurityalliance.org/blog/2025/02/06/agentic-ai-threat-modeling-framework-maestro.

> **Annotation:** Introduces MAESTRO (*Multi-Agent Environment, Security, Threat, Risk, and Outcome*), a seven-layer threat modeling methodology created specifically for autonomous and multi-agent AI architectures spanning Foundation Models, Data Operations, Agent Frameworks, Deployment Infrastructure, Evaluation & Observability, Security & Compliance, and the Agent Ecosystem.
>
> **Audience:** CISO · Security Architects · AI Engineers · **Type:** Industry threat-modeling framework · **Cited in:** [Ch. 9](chapters/09-ai-threat-landscape.md)

<a id="hubinger-2024-sleeper"></a>
Hubinger, Evan, et al. "Sleeper Agents: Training Deceptive LLMs That Persist Through Safety Training." arXiv:2401.05566, January 2024. https://doi.org/10.48550/arXiv.2401.05566.

> **Annotation:** Demonstrates that triggered deceptive model backdoors (e.g., generating vulnerable code when prompted with a target year) persist robustly through supervised fine-tuning, RLHF, and adversarial safety training.
>
> **Audience:** CISO · AI Engineers · Red Teams · **Type:** Research preprint · **Cited in:** [Ch. 12](chapters/12-model-and-supply-chain-security.md)

<a id="huggingface-safetensors"></a>
Hugging Face. *Safetensors: Simple, Safe Way to Store and Distribute Tensors*. GitHub repository and documentation. Accessed November 21, 2026. https://github.com/huggingface/safetensors.

> **Annotation:** Defines the `safetensors` serialization format (8-byte header size + UTF-8 JSON tensor descriptors + raw contiguous numerical arrays) eliminating arbitrary Python `pickle` code execution on model load while supporting fast zero-copy memory mapping (`mmap`).
>
> **Audience:** AI Engineers · MLOps · AppSec · CISO · **Type:** Open-source specification / software · **Cited in:** [Ch. 12](chapters/12-model-and-supply-chain-security.md)

<a id="ibm-2025-breach"></a>
IBM Security and Ponemon Institute. *Cost of a Data Breach Report 2025*. Armonk, NY: IBM, 2025. https://www.ibm.com/reports/data-breach.

> **Annotation:** Annual empirical benchmark on enterprise breach causes and financial impact. The 2025 edition finds that 20 percent of studied organizations experienced breaches involving shadow AI, and that high levels of shadow AI increased average breach costs by \$670,000.
>
> **Audience:** Board · CEO · CISO · CFO · **Type:** Industry research report · **Cited in:** [Ch. 6](chapters/06-data-leakage-and-shadow-ai.md), [Ch. 28](chapters/28-metrics-kris-and-reporting.md), [Ch. 30](chapters/30-governance-maturity-model-and-roadmap.md)

<a id="inan-2023-llama-guard"></a>
Inan, Hakan, Kartikeya Upasani, Jianfeng Chi, et al. "Llama Guard: LLM-Based Input-Output Safeguard for Human-AI Conversations." arXiv:2312.06674, December 2023. https://doi.org/10.48550/arXiv.2312.06674.

> **Annotation:** Presents Meta's instruction-tuned safeguard classifier architecture evaluating both inbound prompts and outbound LLM completions against customizable safety risk taxonomies—a canonical reference model for LLM input/output guardrail layers.
>
> **Audience:** CISO · AI Engineers · MLOps · **Type:** Research preprint · **Cited in:** [Ch. 10](chapters/10-prompt-injection-and-manipulation.md)

<a id="imda-2026-agentic"></a>
Infocomm Media Development Authority (IMDA) and AI Verify Foundation. *Model AI Governance Framework for Generative AI* (May 2024), *Model AI Governance Framework for Agentic AI* (launched at WEF Davos, January 2026), and *AI Verify Testing Framework*. Singapore: IMDA, 2024–2026. https://www.imda.gov.sg/ and https://aiverifyfoundation.sg/.

> **Annotation:** Singapore's operational AI governance suite expanding from generative AI to the world's first dedicated governance framework for autonomous tool-using agents (across four pillars) paired with the open-source AI Verify and Starter Kit testing tools.
>
> **Audience:** CIO · CISO · AI Engineers · Legal / Compliance · **Type:** Government governance framework & toolkit (Singapore) · **Cited in:** [Ch. 20](chapters/20-the-global-regulatory-landscape.md)

<a id="iia-2020-three-lines"></a>
Institute of Internal Auditors. *The IIA's Three Lines Model: An Update of the Three Lines of Defense*. Lake Mary, FL: IIA, July 2020. https://www.theiia.org/en/content/position-papers/2020/the-iias-three-lines-model-an-update-of-the-three-lines-of-defense/.

> **Annotation:** Replaces the traditional "Three Lines of Defense" with six principles centred on creating and protecting value. Explicitly positions the governing body at the top, distinguishes first-line operational roles from second-line risk/compliance roles, and protects third-line internal audit independence.
>
> **Audience:** Board · CRO · Internal Audit · CIO · **Type:** Professional standard / position paper · **Cited in:** [Ch. 4](chapters/04-ai-governance-operating-model.md), [Ch. 22](chapters/22-auditability-assessments-and-evidence.md)

<a id="iia-2025-standards"></a>
Institute of Internal Auditors. *Global Internal Audit Standards*. Lake Mary, FL: IIA, January 2024 (effective January 9, 2025). https://www.theiia.org/en/standards/2024-standards/global-internal-audit-standards/.

> **Annotation:** Binding global internal auditing principles mandating technology and AI governance competence, continuous risk evaluation, independent third-line testing, and board-level assurance reporting.
>
> **Audience:** Chief Audit Executive · Internal Audit · Board · CRO · **Type:** Professional audit standards · **Cited in:** [Ch. 22](chapters/22-auditability-assessments-and-evidence.md), [Ch. 28](chapters/28-metrics-kris-and-reporting.md), [Ch. 30](chapters/30-governance-maturity-model-and-roadmap.md)

<a id="verisk-2026-genai-exclusions"></a>
Insurance Services Office, Inc. (Verisk). Commercial General Liability Endorsements CG 40 47 (*Exclusion — Generative Artificial Intelligence*) and CG 40 48 (*Exclusion — Generative Artificial Intelligence — Coverage B Only*). Effective January 1, 2026.

> **Annotation:** Optional standard U.S. commercial general liability endorsements removing coverage for liabilities arising out of generative AI, defining generative AI broadly to include systems creating text, images, audio, video, or code. Marks the insurance market's move to eliminate "silent AI" coverage.
>
> **Audience:** Board · CRO · CFO · General Counsel · **Type:** Insurance standard form · **Cited in:** [Ch. 3](chapters/03-board-and-executive-oversight.md), [Ch. 15](chapters/15-hallucinations-and-reliability.md), [Ch. 19](chapters/19-intellectual-property-and-licensing.md)

<a id="iea-2025-energy-ai"></a>
International Energy Agency (IEA). *Energy and AI*. Paris: IEA, April 2025. https://www.iea.org/reports/energy-and-ai.

> **Annotation:** Comprehensive global energy assessment estimating baseline data-center electricity demand at roughly 415 TWh (~1.5 percent of global electricity consumption) and projecting consumption will double to roughly 945 TWh by 2030 at ~15 percent annual growth led by AI-optimized compute clusters.
>
> **Audience:** Board · CFO · Chief Sustainability Officer · Infrastructure Leads · **Type:** International energy report · **Cited in:** [Ch. 28](chapters/28-metrics-kris-and-reporting.md)

<a id="iso-2019-22301"></a>
International Organization for Standardization. *ISO 22301:2019 (including Amendment 1:2024), Security and Resilience — Business Continuity Management Systems — Requirements*. Geneva: ISO, October 2019 (Amendment 1:2024, February 2024). https://www.iso.org/standard/75106.html.

> **Annotation:** Core international business-continuity management standard establishing Business Impact Analysis (`BIA`), Maximum Tolerable Period of Disruption (`MTPD`), Recovery Time Objectives (`RTO`), Recovery Point Objectives (`RPO`), and disruption exercising—expanded in 2024 to embed external environmental and supply-chain shock considerations across operational resilience programs.
>
> **Audience:** COO · CRO · CIO · Business Continuity Leads · **Type:** International standard (certifiable) · **Cited in:** [Ch. 25](chapters/25-operational-resilience-and-business-continuity.md)

<a id="iso-2023-23894"></a>
International Organization for Standardization and International Electrotechnical Commission. *ISO/IEC 23894:2023, Information Technology — Artificial Intelligence — Guidance on Risk Management*. Geneva: ISO, February 2023. https://www.iso.org/standard/77304.html.

> **Annotation:** International guidance on managing AI-specific risks, written as an extension of ISO 31000:2018. It shows how establishing context, risk identification, analysis, evaluation, and treatment change for systems that are probabilistic, data-dependent, and liable to drift after deployment. Not certifiable on its own; it is most useful as the risk-assessment method inside an ISO/IEC 42001 management system.
>
> **Audience:** CRO / Risk · Legal / Compliance · CIO · **Type:** International standard (guidance) · **Cited in:** [Ch. 2](chapters/02-reference-frameworks-at-a-glance.md)

<a id="iso-2023-30107-3"></a>
International Organization for Standardization and International Electrotechnical Commission. *ISO/IEC 30107-3:2023, Information Technology — Biometric Presentation Attack Detection — Part 3: Testing and Reporting*. Geneva: ISO, 2023. https://www.iso.org/standard/79520.html.

> **Annotation:** International biometric standard defining `APCER` and `BPCER` metrics for evaluating presentation attack detection against physical artifacts (photos, masks, screen replays) at camera sensors, explicitly excluding software-level digital stream injection attacks.
>
> **Audience:** Head of Fraud / KYC · CISO · Mobile Architects · Procurement · **Type:** International standard · **Cited in:** [Ch. 14](chapters/14-ai-enabled-external-threats.md)

<a id="iso-2023-42001"></a>
International Organization for Standardization and International Electrotechnical Commission. *ISO/IEC 42001:2023, Information Technology — Artificial Intelligence — Management System*. Geneva: ISO, December 2023. https://www.iso.org/standard/81230.html.

> **Annotation:** The first certifiable international standard for an AI management system (AIMS). It follows the harmonized ISO management-system structure used by ISO/IEC 27001 and ISO 9001, built on a Plan-Do-Check-Act cycle, and includes 38 Annex A reference controls under nine objectives covering AI policy, internal organization, resources, impact assessment, life cycle, data, information for interested parties, use of AI, and third-party relationships. Increasingly requested in enterprise procurement as independent evidence of AI governance.
>
> **Audience:** CIO · CISO · Legal / Compliance · CRO · **Type:** International standard (certifiable) · **Cited in:** [Ch. 2](chapters/02-reference-frameworks-at-a-glance.md), [Ch. 3](chapters/03-board-and-executive-oversight.md), [Ch. 4](chapters/04-ai-governance-operating-model.md), [Ch. 5](chapters/05-policies-inventory-and-risk-tiering.md), [Ch. 6](chapters/06-data-leakage-and-shadow-ai.md), [Ch. 7](chapters/07-internal-over-exposure-and-permission-aware-ai.md), [Ch. 8](chapters/08-data-provenance-consent-and-sovereignty.md), [Ch. 20](chapters/20-the-global-regulatory-landscape.md), [Ch. 22](chapters/22-auditability-assessments-and-evidence.md), [Ch. 24](chapters/24-model-lifecycle-and-change-management.md), [Ch. 25](chapters/25-operational-resilience-and-business-continuity.md), [Ch. 26](chapters/26-testing-evaluation-and-red-teaming.md), [Ch. 28](chapters/28-metrics-kris-and-reporting.md), [Ch. 29](chapters/29-building-a-risk-aware-ai-culture.md), [Ch. 30](chapters/30-governance-maturity-model-and-roadmap.md)

<a id="iso-2025-42005"></a>
International Organization for Standardization and International Electrotechnical Commission. *ISO/IEC 42005:2025, Information Technology — Artificial Intelligence (AI) — AI System Impact Assessment*. Geneva: ISO, May 2025. https://www.iso.org/.

> **Annotation:** International lifecycle impact-assessment standard guiding enterprises on evaluating AI effects on individuals, groups, and society—enabling one unified intake to support GDPR DPIAs, EU FRIAs, and algorithmic assessments.
>
> **Audience:** DPO · Legal / Compliance · CRO · Product · **Type:** International standard · **Cited in:** [Ch. 22](chapters/22-auditability-assessments-and-evidence.md)

<a id="iso-2025-42006"></a>
International Organization for Standardization and International Electrotechnical Commission. *ISO/IEC 42006:2025, Information Technology — Artificial Intelligence — Requirements for Bodies Providing Audit and Certification of Artificial Intelligence Management Systems*. Geneva: ISO, July 2025. https://www.iso.org/.

> **Annotation:** Establishes impartiality, AI technical competence, and Stage 1/Stage 2 conformity-assessment rules governing third-party registrars auditing and certifying organizations against `ISO/IEC 42001`.
>
> **Audience:** Compliance · Internal Audit · Procurement · CISO · **Type:** International accreditation standard · **Cited in:** [Ch. 22](chapters/22-auditability-assessments-and-evidence.md), [Ch. 30](chapters/30-governance-maturity-model-and-roadmap.md)

<a id="jones-2020-rfc8693"></a>
Jones, Michael, Anthony Nadalin, Brian Campbell (ed.), John Bradley, and Chuck Mortimore. *OAuth 2.0 Token Exchange*. IETF RFC 8693, January 2020. https://datatracker.ietf.org/doc/html/rfc8693.

> **Annotation:** Internet Engineering Task Force standard defining a Security Token Service exchange protocol distinguishing impersonation from auditable delegation via the JWT `act` (Actor) claim (Section 4.1) and nested multi-hop actor chains—now the core IAM pattern for scoped AI agent identities.
>
> **Audience:** CISO · IAM Architects · AI Engineers · **Type:** Internet standard (IETF RFC) · **Cited in:** [Ch. 11](chapters/11-securing-ai-agents.md)

<a id="kalai-2025-hallucinate"></a>
Kalai, Adam Tauman, Ofir Nachum, Santosh S. Vempala, and Edwin Zhang. "Why Language Models Hallucinate." arXiv:2509.04664, September 2025. https://doi.org/10.48550/arXiv.2509.04664.

> **Annotation:** Argues that hallucinations are a statistically predictable result of how models are trained, and that they persist because common benchmarks reward confident guessing over honest abstention. The authors propose changing how mainstream evaluations are scored so that calibrated "I don't know" answers are rewarded. Gives executives and engineers a clear mental model of why errors will not simply disappear as models improve.
>
> **Audience:** All roles · **Type:** Research preprint · **Cited in:** [Ch. 1](chapters/01-why-ai-risk-is-different.md), [Ch. 15](chapters/15-hallucinations-and-reliability.md), [Ch. 26](chapters/26-testing-evaluation-and-red-teaming.md)

<a id="kleinberg-2017-tradeoffs"></a>
Kleinberg, Jon, Sendhil Mullainathan, and Manish Raghavan. "Inherent Trade-Offs in the Fair Determination of Risk Scores." In *Proceedings of the 8th Innovations in Theoretical Computer Science Conference (ITCS 2017)*, 2017. arXiv:1609.05807. https://doi.org/10.48550/arXiv.1609.05807.

> **Annotation:** Mathematical impossibility proof demonstrating that whenever underlying demographic base rates differ and predictions are less than perfect, no risk score can simultaneously satisfy calibration within groups, false-positive parity, and false-negative parity—turning fairness metric choice into a governance decision.
>
> **Audience:** Board · General Counsel · Chief Risk Officer · AI Engineers · **Type:** Peer-reviewed paper · **Cited in:** [Ch. 16](chapters/16-bias-fairness-and-discrimination.md)

<a id="kumar-2025-overthink"></a>
Kumar, Abhinav, Jaechul Roh, Ali Naseh, Marzena Karpinska, Mohit Iyyer, Amir Houmansadr, and Eugene Bagdasarian. "OverThink: Slowdown Attacks on Reasoning LLMs." arXiv:2502.02542, February 2025. https://doi.org/10.48550/arXiv.2502.02542.

> **Annotation:** Demonstrates "Denial-of-Wallet" slowdown attacks targeting reasoning LLMs (`o1`, `o1-mini`, `o3-mini`, `DeepSeek-R1`) by slipping benign-looking decoy reasoning puzzles into external RAG and coding-agent contexts, inflating reasoning token consumption up to 46× on SQuAD, 13×–18× on FreshQA, and up to 17× in code agents.
>
> **Audience:** CISO · FinOps · AI Engineers · Platform Architects · **Type:** Research preprint · **Cited in:** [Ch. 13](chapters/13-infrastructure-and-operational-security.md)

<a id="lecher-2024-nyc-mycity"></a>
Lecher, Colin. "NYC's AI Chatbot Tells Businesses to Break the Law." *The Markup*, March 29, 2024. https://themarkup.org/artificial-intelligence/2024/03/29/nycs-ai-chatbot-tells-businesses-to-break-the-law.

> **Annotation:** Investigative test of New York City's Microsoft-powered MyCity business portal chatbot showing repeated false statutory guidance—claiming owners could take workers' tips, refuse cash payments, and discriminate against Section 8 housing vouchers—despite carrying an on-screen accuracy disclaimer.
>
> **Audience:** General Counsel · Public Sector · Chief Product Officer · Compliance · **Type:** Investigative news report · **Cited in:** [Ch. 15](chapters/15-hallucinations-and-reliability.md)

<a id="lee-2004-trust"></a>
Lee, John D., and Katrina A. See. "Trust in Automation: Designing for Appropriate Reliance." *Human Factors* 46, no. 1 (Spring 2004): 50–80. https://doi.org/10.1518/hfes.46.1.50_30392.

> **Annotation:** Seminal human-factors framework distinguishing *appropriate reliance* from *misuse* (over-trusting unreliable systems) and *disuse* (abandoning capable systems), guiding enterprise trust calibration.
>
> **Audience:** Chief Product Officer · UX Design · CHRO · Operations Leads · **Type:** Peer-reviewed journal article · **Cited in:** [Ch. 17](chapters/17-human-oversight-and-automation-bias.md), [Ch. 29](chapters/29-building-a-risk-aware-ai-culture.md)

<a id="lee-2022-dedup"></a>
Lee, Katherine, Daphne Ippolito, Andrew Nystrom, Chiyuan Zhang, Douglas Eck, Chris Callison-Burch, and Nicholas Carlini. "Deduplicating Training Data Makes Language Models Better." In *Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (ACL 2022)*, May 2022. https://doi.org/10.18653/v1/2022.acl-long.577.

> **Annotation:** Proves that `ExactSubstr` and `NearDup` deduplication of training corpora cuts verbatim memorized emissions by roughly tenfold while speeding training and improving generalization.
>
> **Audience:** AI Engineers · CDO · DPO · **Type:** Peer-reviewed paper · **Cited in:** [Ch. 12](chapters/12-model-and-supply-chain-security.md)

<a id="spdx-2024-v3"></a>
Linux Foundation. *SPDX Specification Version 3.0 (AI and Dataset Profiles)*. 2024. https://spdx.dev/use/specifications/.

> **Annotation:** Major release of the Software Package Data Exchange standard (extending ISO/IEC 5962) introducing dedicated AI and Dataset profiles on a modular RDF graph architecture. Well suited to deep data provenance, open-source license compliance, and legal documentation for enterprise AI systems.
>
> **Audience:** CISO · CDO · Legal / Compliance · AI Engineers · **Type:** Open technical standard · **Cited in:** [Ch. 5](chapters/05-policies-inventory-and-risk-tiering.md), [Ch. 8](chapters/08-data-provenance-consent-and-sovereignty.md), [Ch. 12](chapters/12-model-and-supply-chain-security.md), [Ch. 19](chapters/19-intellectual-property-and-licensing.md)

<a id="liu-2023-verifiability"></a>
Liu, Nelson F., Tianyi Zhang, and Percy Liang. "Evaluating Verifiability in Generative Search Engines." In *Findings of the Association for Computational Linguistics: EMNLP 2023*, December 2023. arXiv:2304.09848. https://doi.org/10.48550/arXiv.2304.09848.

> **Annotation:** Human audit of four commercial generative search engines (Bing Chat, NeevaAI, Perplexity.ai, and YouChat) finding on average only 51.5 percent of generated sentences were fully supported by citations (citation recall) and only 74.5 percent of citations actually backed their attached claims (citation precision)—exposing a "facade of trustworthiness."
>
> **Audience:** AI Engineers · Chief Product Officer · Legal / Compliance · CISO · **Type:** Peer-reviewed paper · **Cited in:** [Ch. 15](chapters/15-hallucinations-and-reliability.md)

<a id="luccioni-2024-power-hungry"></a>
Luccioni, Alexandra Sasha, Yacine Jernite, and Emma Strubell. "Power Hungry Processing: Watts Driving the Cost of AI Deployment?" In *Proceedings of the 2024 ACM Conference on Fairness, Accountability, and Transparency (ACM FAccT '24)*, June 2024. arXiv:2311.16863. https://doi.org/10.48550/arXiv.2311.16863.

> **Annotation:** Systematic empirical evaluation of 88 models across 30 datasets and 10 tasks proving that multi-purpose generative inference architectures consume orders of magnitude more electricity and carbon per 1,000 inferences than task-specific fine-tuned or discriminative models.
>
> **Audience:** CIO · Chief Sustainability Officer · AI Engineers · FinOps · **Type:** Peer-reviewed paper · **Cited in:** [Ch. 28](chapters/28-metrics-kris-and-reporting.md)

<a id="lundberg-2017-shap"></a>
Lundberg, Scott M., and Su-In Lee. "A Unified Approach to Interpreting Model Predictions." In *Advances in Neural Information Processing Systems 30 (NeurIPS 2017)*, 2017. arXiv:1705.07874. https://doi.org/10.48550/arXiv.1705.07874.

> **Annotation:** Unifies six feature-importance frameworks under Shapley values (`SHAP`), proving unique satisfaction of local accuracy, missingness, and consistency alongside fast `TreeSHAP` algorithms used across regulated credit, claims, and fraud scoring models.
>
> **Audience:** AI Engineers · Chief Credit Officer · Risk / Compliance · CDO · **Type:** Peer-reviewed paper · **Cited in:** [Ch. 18](chapters/18-transparency-disclosure-and-content-provenance.md)

<a id="magesh-2025-legal-rag"></a>
Magesh, Varun, Faiz Surani, Matthew Dahl, Mirac Suzgun, Christopher D. Manning, and Daniel E. Ho. "Hallucination-Free? Assessing the Reliability of Leading AI Legal Research Tools." *Journal of Empirical Legal Studies* (2025): 1–27. arXiv:2405.20362. https://doi.org/10.1111/jels.12413.

> **Annotation:** Preregistered Stanford RegLab benchmark evaluating proprietary commercial legal RAG products (*Lexis+ AI*, *Westlaw AI-Assisted Research*, *Ask Practical Law AI*) and finding hallucination rates between 17 percent and 33 percent despite vendor "hallucination-free" marketing claims.
>
> **Audience:** General Counsel · CIO · Legal / Compliance · Procurement · **Type:** Peer-reviewed paper · **Cited in:** [Ch. 15](chapters/15-hallucinations-and-reliability.md), [Ch. 26](chapters/26-testing-evaluation-and-red-teaming.md)

<a id="magramo-2024-arup"></a>
Magramo, Kathleen. "British Engineering Giant Arup Revealed as \$25 Million Deepfake Scam Victim." CNN, May 17, 2024. https://edition.cnn.com/2024/05/16/tech/arup-deepfake-scam-loss-hong-kong-intl-hnk/index.html.

> **Annotation:** Names Arup as the victim of the Hong Kong fraud in which an employee transferred HK\$200 million after a video call where every other participant was a deepfake. The defining case study for AI-enabled social engineering, and the clearest argument for verifying high-value payment requests through an independent channel.
>
> **Audience:** Board · CFO / Finance · CISO · **Type:** News report · **Cited in:** [Front Matter](chapters/00-front-matter.md), [Ch. 1](chapters/01-why-ai-risk-is-different.md), [Ch. 3](chapters/03-board-and-executive-oversight.md), [Ch. 9](chapters/09-ai-threat-landscape.md), [Ch. 14](chapters/14-ai-enabled-external-threats.md)

<a id="mazeika-2024-harmbench"></a>
Mazeika, Mantas, Long Phan, Xuwang Yin, Andy Zou, Zifan Wang, Norman Mu, Elham Sakhaee, Nathaniel Li, Steven Basart, Bo Li, David Forsyth, and Dan Hendrycks. "HarmBench: A Standardized Evaluation Framework for Automated Red Teaming and Robust Refusal." In *Proceedings of the 41st International Conference on Machine Learning (ICML 2024)*, 2024. arXiv:2402.04249. https://doi.org/10.48550/arXiv.2402.04249.

> **Annotation:** Standardized adversarial safety benchmark covering 510 harmful behaviors evaluated across 18 automated red-teaming attacks and 33 target models and defenses using calibrated Attack Success Rate (`ASR`) classifiers and train/test splits to eliminate inconsistent evaluation baselines.
>
> **Audience:** AI Engineers · Red Teams · CISO · Research / Governance · **Type:** Peer-reviewed paper · **Cited in:** [Ch. 26](chapters/26-testing-evaluation-and-red-teaming.md)

<a id="mdcg-2025-6"></a>
Medical Device Coordination Group (MDCG) and European Artificial Intelligence Board (AIB). *MDCG 2025-6 / AIB 2025-1: FAQ on Interplay Between the Medical Devices Regulation (MDR) & In Vitro Diagnostic Medical Devices Regulation (IVDR) and the Artificial Intelligence Act (AIA)*. Brussels: European Commission, June 2025. https://health.ec.europa.eu/.

> **Annotation:** Joint European Commission guidance clarifying how AI-enabled medical device manufacturers satisfy EU MDR/IVDR and EU AI Act high-risk rules through integrated quality-management systems and single technical files rather than separate regulatory silos.
>
> **Audience:** Chief Medical Officer · Quality Assurance · Regulatory Affairs · AI Engineers · **Type:** Joint EU regulatory guidance · **Cited in:** [Ch. 21](chapters/21-sector-specific-requirements.md)

<a id="meta-2022-system-cards"></a>
Meta AI. "System Cards, a New Resource for Understanding How AI Systems Work." Meta AI Blog, February 2022. https://ai.meta.com/blog/system-cards-a-new-resource-for-understanding-how-ai-systems-work/.

> **Annotation:** Extends documentation from standalone models to full socio-technical *System Cards* detailing how multiple ML models, rankers, filters, rules, and user interfaces combine in production applications.
>
> **Audience:** CIO · Product Leaders · CISO · Internal Audit · **Type:** Industry documentation standard / blog · **Cited in:** [Ch. 18](chapters/18-transparency-disclosure-and-content-provenance.md)

<a id="meta-2024-llama-license"></a>
Meta Platforms, Inc. *Llama Community License Agreement (Llama 3 / 3.1 / 3.3 / 4 Series) and Acceptable Use Policy*. 2024–2025. https://www.llama.com/llama3_1/license/.

> **Annotation:** Canonical custom open-weight model license setting a 700-million monthly active user (MAU) threshold for separate commercial licensing alongside mandatory "Built with Llama" UI attribution, derivative model naming rules, and binding Acceptable Use Policy restrictions.
>
> **Audience:** General Counsel · CTO · Procurement · AI Engineers · **Type:** Model license / AUP · **Cited in:** [Ch. 19](chapters/19-intellectual-property-and-licensing.md), [Ch. 23](chapters/23-vendor-and-third-party-ai-risk.md)

<a id="microsoft-2024-work-trend"></a>
Microsoft and LinkedIn. *2024 Work Trend Index Annual Report: AI at Work Is Here. Now Comes the Hard Part*. May 8, 2024. https://www.microsoft.com/en-us/worklab/work-trend-index/ai-at-work-is-here-now-comes-the-hard-part.

> **Annotation:** Global workplace survey highlighting the scale of Bring Your Own AI (BYOAI): 78 percent of AI users bring their own AI tools to work across all generations while 60 percent of leaders report their organization lacks a clear AI strategy.
>
> **Audience:** Board · CEO · CIO · CISO · **Type:** Industry survey report · **Cited in:** [Ch. 6](chapters/06-data-leakage-and-shadow-ai.md), [Ch. 29](chapters/29-building-a-risk-aware-ai-culture.md), [Ch. 30](chapters/30-governance-maturity-model-and-roadmap.md)

<a id="presidio-oss"></a>
Microsoft and Data Privacy Stack. *Presidio: Data Protection and De-Identification SDK*. GitHub repository and documentation. Accessed November 21, 2026. https://github.com/data-privacy-stack/presidio.

> **Annotation:** Open-source PII detection and anonymization toolkit covering text, structured tables, and images (Analyzer, Anonymizer, Image-Redactor, Structured) by combining regex, checksum validation, and named-entity recognition. Widely used as a reference baseline for inline AI gateway redaction pipelines.
>
> **Audience:** CISO · CDO · AI Engineers · **Type:** Open-source software / documentation · **Cited in:** [Ch. 6](chapters/06-data-leakage-and-shadow-ai.md), [Ch. 13](chapters/13-infrastructure-and-operational-security.md)

<a id="microsoft-2023-ccc"></a>
Microsoft Corporation (Brad Smith and Hossein Nowbar). "Microsoft Announces New Copilot Copyright Commitment for Customers." Microsoft On the Issues Blog, September 7, 2023. https://blogs.microsoft.com/on-the-issues/2023/09/07/copilot-copyright-commitment-ai-legal-risks/.

> **Annotation:** Establishes Microsoft's Copilot / Customer Copyright Commitment defending enterprise users against third-party copyright output suits, expressly conditioned on keeping built-in guardrails and content filters active.
>
> **Audience:** General Counsel · Procurement · CIO · CISO · **Type:** Vendor policy / blog · **Cited in:** [Ch. 19](chapters/19-intellectual-property-and-licensing.md), [Ch. 23](chapters/23-vendor-and-third-party-ai-risk.md)

<a id="microsoft-purview-copilot"></a>
Microsoft Corporation. "Microsoft Purview Data Security and Compliance Protections for Generative AI Apps / SharePoint Data Access Governance." Microsoft Learn Documentation. Accessed November 21, 2026. https://learn.microsoft.com/en-us/purview/ai-microsoft-purview.

> **Annotation:** Enterprise documentation outlining Microsoft's layered oversharing and AI readiness controls: SharePoint Data Access Governance (DAG) reports to detect broad sharing links, temporary Restricted SharePoint Search (allow-list of up to 100 sites while remediating permissions), `VIEW + EXTRACT` usage-rights enforcement, and automatic sensitivity-label inheritance for AI-generated outputs.
>
> **Audience:** CIO · CISO · CDO · Data Stewards · **Type:** Vendor documentation · **Cited in:** [Ch. 7](chapters/07-internal-over-exposure-and-permission-aware-ai.md), [Ch. 22](chapters/22-auditability-assessments-and-evidence.md)

<a id="microsoft-openai-2024-threats"></a>
Microsoft Threat Intelligence and OpenAI. "Staying Ahead of Threat Actors in the Age of AI." Microsoft Security Blog, February 14, 2024. https://www.microsoft.com/en-us/security/blog/2024/02/14/staying-ahead-of-threat-actors-in-the-age-of-ai/.

> **Annotation:** Joint threat-intelligence disclosure tracking how five nation-state affiliated hacking groups—including Forest Blizzard (Russia), Emerald Sleet (North Korea), Crimson Sandstorm (Iran), and Charcoal Typhoon (China)—used LLMs for target research, technical translation, script troubleshooting, and spear-phishing refinement.
>
> **Audience:** CISO · Security Operations · Threat Intelligence · **Type:** Joint threat intelligence report · **Cited in:** [Ch. 9](chapters/09-ai-threat-landscape.md), [Ch. 14](chapters/14-ai-enabled-external-threats.md)

<a id="meity-2025-ai-guidelines"></a>
Ministry of Electronics and Information Technology (MeitY). *India AI Governance Guidelines* (IndiaAI Mission). New Delhi: Government of India, November 5, 2025. https://indiaai.gov.in/.

> **Annotation:** Cross-sectoral Indian governance framework rejecting a rigid standalone AI Act in favor of an agile techno-legal approach enforced under the IT Act and DPDP Act, anchored on Seven Sutras, six pillars, and national safety institutions.
>
> **Audience:** General Counsel · CIO · Board · Public Policy · **Type:** National government guidelines (India) · **Cited in:** [Ch. 20](chapters/20-the-global-regulatory-landscape.md)

<a id="mitchell-2019-model-cards"></a>
Mitchell, Margaret, Simone Wu, Andrew Zaldivar, Parker Barnes, Lucy Vasserman, Ben Hutchinson, Elena Spitzer, Inioluwa Deborah Raji, and Timnit Gebru. "Model Cards for Model Reporting." In *Proceedings of the Conference on Fairness, Accountability, and Transparency (FAT\* '19)*, January 2019. arXiv:1810.03993. https://doi.org/10.1145/3287560.3287596.

> **Annotation:** Canonical transparency framework proposing standardized Model Cards reporting intended uses, out-of-scope boundaries, quantitative performance disaggregated across protected and phenotypic subgroups, and ethical caveats.
>
> **Audience:** AI Engineers · CDO · Procurement · Legal / Compliance · **Type:** Peer-reviewed paper · **Cited in:** [Ch. 18](chapters/18-transparency-disclosure-and-content-provenance.md)

<a id="mitre-atlas"></a>
MITRE Corporation. "ATLAS: Adversarial Threat Landscape for Artificial-Intelligence Systems." Accessed November 17, 2026. https://atlas.mitre.org/.

> **Annotation:** A free, continuously updated knowledge base of adversary tactics, techniques, real-world case studies, and mitigations for AI systems, modelled on MITRE ATT&CK. It began in 2020 as the Adversarial ML Threat Matrix, a collaboration between MITRE, Microsoft, and other partners, and now covers generative and agentic AI threats such as prompt injection, jailbreaks, and poisoning. The primary reference for AI threat modeling, red-team planning, and SOC detection engineering.
>
> **Audience:** CISO · Security Operations · Red Teams · AI Engineers · **Type:** Threat knowledge base · **Cited in:** [Ch. 2](chapters/02-reference-frameworks-at-a-glance.md), [Ch. 9](chapters/09-ai-threat-landscape.md), [Ch. 12](chapters/12-model-and-supply-chain-security.md), [Ch. 13](chapters/13-infrastructure-and-operational-security.md), [Ch. 26](chapters/26-testing-evaluation-and-red-teaming.md)

<a id="mlcommons-2025-ailuminate"></a>
MLCommons. *AILuminate: Introducing v1.0 of the AI Risk and Reliability Benchmark from MLCommons*. MLCommons AI Risk & Reliability Working Group, December 2024 (arXiv:2503.05731, March 2025). https://ailuminate.mlcommons.org/.

> **Annotation:** Multi-stakeholder chat-safety benchmark evaluating general-purpose AI systems across twelve hazard categories—including CBRNE weapons, CSAM, suicide/self-harm, cyber/nonviolent crime, hate, IP, privacy, defamation, and specialized legal/medical/financial advice—on a five-tier *Poor*-to-*Excellent* scale.
>
> **Audience:** Procurement · CRO · AI Engineers · Quality Engineering · **Type:** Industry safety benchmark · **Cited in:** [Ch. 26](chapters/26-testing-evaluation-and-red-teaming.md)

<a id="morris-2023-vec2text"></a>
Morris, John X., Volodymyr Kuleshov, Vitaly Shmatikov, and Alexander M. Rush. "Text Embeddings Reveal (Almost) As Much As Text." In *Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP 2023)*, December 2023. arXiv:2310.06816. https://doi.org/10.48550/arXiv.2310.06816.

> **Annotation:** Introduces `vec2text` iterative embedding inversion, proving that dense vector embeddings allow near-exact reconstruction (`92%` of 32-token inputs) and extraction of full names and medical details from clinical vectors—forcing enterprises to apply plaintext-equivalent security to vector databases.
>
> **Audience:** CISO · CDO · DPO · AI Engineers · **Type:** Peer-reviewed paper · **Cited in:** [Ch. 13](chapters/13-infrastructure-and-operational-security.md)

<a id="munoz-2024-pyrit"></a>
Munoz, Gary D. Lopez, Amanda J. Minnich, Roman Lutz, Richard Lundeen, Raja Sekhar Rao Dheekonda, Nina Chikanov, Bolor-Erdene Jagdagdorj, Martin Pouliot, Shiven Chawla, Whitney Maxwell, Blake Bullwinkel, Katherine Pratt, Joris de Gruyter, Charlotte Siska, Pete Bryan, Tori Westerhoff, Chang Kawaguchi, Christian Seifert, Ram Shankar Siva Kumar, and Yonatan Zunger. "PyRIT: A Framework for Security Risk Identification and Red Teaming in Generative AI Systems." Microsoft AI Red Team, October 2024. arXiv:2410.02828. https://doi.org/10.48550/arXiv.2410.02828.

> **Annotation:** Open-source automation framework built by Microsoft's AI Red Team organizing Targets, Orchestrators, Converters, Scorers, Memory, and seed Datasets to execute scalable multi-turn, adaptive, and multimodal adversarial testing.
>
> **Audience:** CISO · Red Teams · AppSec · AI Engineers · **Type:** Technical paper / tool framework · **Cited in:** [Ch. 26](chapters/26-testing-evaluation-and-red-teaming.md)

<a id="nagli-2025-deepseek-wiz"></a>
Nagli, Gal. "Wiz Research Uncovers Exposed DeepSeek Database Leaking Sensitive Information, Including Chat History." Wiz Blog, January 29, 2025. https://www.wiz.io/blog/wiz-research-uncovers-exposed-deepseek-database-leak.

> **Annotation:** Discloses DeepSeek's publicly exposed, unauthenticated ClickHouse database (`port 9000`) allowing arbitrary SQL queries across more than one million log lines containing plaintext user chat histories, API secret keys, and internal operational metadata.
>
> **Audience:** CISO · Cloud Security · Platform Engineers · DPO · **Type:** Cloud security disclosure · **Cited in:** [Ch. 13](chapters/13-infrastructure-and-operational-security.md)

<a id="nasr-2025-attacker-second"></a>
Nasr, Milad, Nicholas Carlini, Chawin Sitawarin, Sander V. Schulhoff, Jamie Hayes, Michael Ilie, Juliette Pluto, Shuang Song, Harsh Chaudhari, Ilia Shumailov, Abhradeep Thakurta, Kai Yuanqing Xiao, Andreas Terzis, and Florian Tramèr. "The Attacker Moves Second: Stronger Adaptive Attacks Bypass Defenses Against LLM Jailbreaks and Prompt Injections." arXiv:2510.09023, October 2025. https://doi.org/10.48550/arXiv.2510.09023.

> **Annotation:** Landmark multi-institution evaluation showing that adaptive optimization (gradient descent, RL, search) and human red-teaming defeated all 12 tested jailbreak and prompt-injection defenses—achieving attack success rates above 90 percent on most—proving classifier guardrails are speed bumps rather than complete boundaries.
>
> **Audience:** CISO · AI Engineers · Red Teams · AppSec · **Type:** Research preprint · **Cited in:** [Ch. 10](chapters/10-prompt-injection-and-manipulation.md), [Ch. 26](chapters/26-testing-evaluation-and-red-teaming.md)

<a id="nist-2025-ai-100-2"></a>
National Institute of Standards and Technology. *Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations*. NIST AI 100-2 E2025. Gaithersburg, MD: NIST, March 2025. https://doi.org/10.6028/NIST.AI.100-2e2025.

> **Annotation:** Authoritative NIST taxonomy organizing adversarial attacks and defenses across predictive and generative AI lifecycles—categorizing evasion, poisoning, privacy leakage, and abuse tactics to structure enterprise red-teaming and verification scope.
>
> **Audience:** CISO · Red Teams · AI Engineers · CRO · **Type:** Government taxonomy / standard · **Cited in:** [Ch. 26](chapters/26-testing-evaluation-and-red-teaming.md)

<a id="nist-2023-ai-rmf"></a>
National Institute of Standards and Technology. *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*. NIST AI 100-1. Gaithersburg, MD: NIST, January 2023. https://doi.org/10.6028/NIST.AI.100-1.

> **Annotation:** The most widely referenced voluntary framework for AI risk management. It defines the characteristics of trustworthy AI and organizes risk activities into four functions: Govern, Map, Measure, and Manage. It treats AI systems as socio-technical, with risks arising from the interaction of technology, people, and context. It serves as a common baseline across sectors and countries, and many regulations and standards reference or align with it.
>
> **Audience:** All roles · **Type:** Government framework / standard · **Cited in:** [Ch. 1](chapters/01-why-ai-risk-is-different.md), [Ch. 2](chapters/02-reference-frameworks-at-a-glance.md), [Ch. 3](chapters/03-board-and-executive-oversight.md), [Ch. 4](chapters/04-ai-governance-operating-model.md), [Ch. 5](chapters/05-policies-inventory-and-risk-tiering.md), [Ch. 20](chapters/20-the-global-regulatory-landscape.md), [Ch. 28](chapters/28-metrics-kris-and-reporting.md), [Ch. 29](chapters/29-building-a-risk-aware-ai-culture.md), [Ch. 30](chapters/30-governance-maturity-model-and-roadmap.md)

<a id="nist-2024-genai-profile"></a>
National Institute of Standards and Technology. *Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile*. NIST AI 600-1. Gaithersburg, MD: NIST, July 2024. https://doi.org/10.6028/NIST.AI.600-1.

> **Annotation:** A companion to the AI RMF focused on generative AI. It identifies twelve risks that are unique to or made worse by GenAI, including confabulation, data privacy, information security, intellectual property, harmful bias, and value-chain integration. It maps hundreds of suggested actions to the RMF functions, making it one of the most practical government resources for building a GenAI control set.
>
> **Audience:** CISO · CDO / Data Stewards · Legal / Compliance · AI Engineers · **Type:** Government framework / standard · **Cited in:** [Front Matter](chapters/00-front-matter.md), [Ch. 1](chapters/01-why-ai-risk-is-different.md), [Ch. 2](chapters/02-reference-frameworks-at-a-glance.md), [Ch. 6](chapters/06-data-leakage-and-shadow-ai.md), [Ch. 7](chapters/07-internal-over-exposure-and-permission-aware-ai.md)

<a id="nist-airc-crosswalks"></a>
National Institute of Standards and Technology. "Crosswalks to the NIST AI RMF." NIST AI Resource Center. Accessed November 17, 2026. https://airc.nist.gov/.

> **Annotation:** A collection of community-contributed mappings between the NIST AI RMF and other frameworks and standards, including ISO/IEC 42001. A practical starting point for building a single control library that satisfies several frameworks at once. NIST hosts but does not endorse the specific interpretations, and some mappings were drafted against pre-publication versions of the standards.
>
> **Audience:** Legal / Compliance · CRO · CIO · **Type:** Government resource (crosswalks) · **Cited in:** [Ch. 2](chapters/02-reference-frameworks-at-a-glance.md), [Ch. 20](chapters/20-the-global-regulatory-landscape.md)

<a id="nvd-2025-echoleak"></a>
National Institute of Standards and Technology. "CVE-2025-32711 Detail." National Vulnerability Database, June 2025. https://nvd.nist.gov/vuln/detail/CVE-2025-32711.

> **Annotation:** The official record for "EchoLeak," an AI command-injection vulnerability in Microsoft 365 Copilot discovered by Aim Security's research team. It is widely described as the first zero-click prompt-injection exploit against a mainstream enterprise AI assistant. A key case for showing that indirect prompt injection is a practical, production-grade threat and not just a laboratory curiosity.
>
> **Audience:** CISO · AI Engineers · CIO · **Type:** Vulnerability record · **Cited in:** [Front Matter](chapters/00-front-matter.md), [Ch. 1](chapters/01-why-ai-risk-is-different.md), [Ch. 2](chapters/02-reference-frameworks-at-a-glance.md), [Ch. 9](chapters/09-ai-threat-landscape.md), [Ch. 10](chapters/10-prompt-injection-and-manipulation.md), [Ch. 27](chapters/27-ai-incident-response.md)

<a id="nvd-2025-mcp-remote"></a>
National Institute of Standards and Technology. "CVE-2025-6514 Detail." National Vulnerability Database, July 2025. https://nvd.nist.gov/vuln/detail/CVE-2025-6514.

> **Annotation:** Official vulnerability record for critical OS command injection in the `mcp-remote` client proxy (`0.0.5`–`0.1.15`), allowing an untrusted remote MCP server returning a crafted OAuth `authorization_endpoint` to achieve Remote Code Execution on connecting developer machines.
>
> **Audience:** CISO · AppSec · AI Engineers · Platform IT · **Type:** Vulnerability record · **Cited in:** [Ch. 11](chapters/11-securing-ai-agents.md)

<a id="nist-2024-csf-2"></a>
National Institute of Standards and Technology. *The NIST Cybersecurity Framework (CSF) 2.0*. NIST Cybersecurity White Paper CSWP 29. Gaithersburg, MD: NIST, February 26, 2024. https://doi.org/10.6028/NIST.CSWP.29.

> **Annotation:** Major 2024 update expanding the NIST Cybersecurity Framework across all enterprise sectors by adding `Govern` as an overarching sixth function alongside four Implementation Tiers (`Partial`, `Risk Informed`, `Repeatable`, `Adaptive`) guiding progressive governance maturity.
>
> **Audience:** Board · CISO · CRO · CIO · **Type:** Government framework / standard · **Cited in:** [Ch. 30](chapters/30-governance-maturity-model-and-roadmap.md)

<a id="nist-2021-800-160v2r1"></a>
National Institute of Standards and Technology (Ron Ross, Victoria Pillitteri, Richard Graubart, Deborah Bodeau, and Rosalie McQuaid). *Developing Cyber-Resilient Systems: A Systems Security Engineering Approach*. NIST Special Publication 800-160, Volume 2, Revision 1. Gaithersburg, MD: NIST, December 2021. https://doi.org/10.6028/NIST.SP.800-160v2r1.

> **Annotation:** Foundational cyber-resilience engineering framework establishing constrained operation (graceful degradation), architectural diversity, redundancy, analytic monitoring, and non-persistence—providing technical design patterns for operating business functions safely when AI components degrade or drop offline.
>
> **Audience:** CISO · Enterprise Architects · SRE · Operational Resilience · **Type:** Government standard · **Cited in:** [Ch. 25](chapters/25-operational-resilience-and-business-continuity.md)

<a id="nist-2025-800-63b4"></a>
National Institute of Standards and Technology. *Digital Identity Guidelines: Authentication and Authenticator Management*. NIST Special Publication 800-63B-4. Gaithersburg, MD: NIST, July 31, 2025. https://doi.org/10.6028/NIST.SP.800-63B-4.

> **Annotation:** Authoritative authentication standard prioritizing phishing-resistant, verifier-impersonation-resistant authenticators (FIDO2/WebAuthn passkeys and hardware security keys) to neutralize Adversary-in-the-Middle phishing proxies, while modernizing memorized-secret requirements (`>=64` chars, Unicode, password-manager paste, breach-list screening, retiring arbitrary periodic rotation).
>
> **Audience:** CISO · IAM Leads · Platform Architects · Legal / Compliance · **Type:** Government standard · **Cited in:** [Ch. 14](chapters/14-ai-enabled-external-threats.md)

<a id="nist-2025-800-88r2"></a>
National Institute of Standards and Technology. *Guidelines for Media Sanitization*. NIST Special Publication 800-88 Revision 2. Gaithersburg, MD: NIST, September 2025. https://doi.org/10.6028/NIST.SP.800-88r2.

> **Annotation:** Supersedes the 2014 Revision 1 guidance and establishes modern enterprise sanitization controls—Clear, Purge (including Cryptographic Erase across encrypted volumes and key hierarchies), and Destroy—alongside verification testing and documented Certificates of Sanitization governing retired vector stores, caches, and fine-tuning artifacts.
>
> **Audience:** CISO · MLOps · DPO · Internal Audit · **Type:** Government standard · **Cited in:** [Ch. 24](chapters/24-model-lifecycle-and-change-management.md)

<a id="nist-2025-800-61r3"></a>
National Institute of Standards and Technology (Alexander Nelson, Sanjay Rekhi, Murugiah Souppaya, and Karen Scarfone). *Incident Response Recommendations and Considerations for Cybersecurity Risk Management: A CSF 2.0 Community Profile*. NIST Special Publication 800-61 Revision 3. Gaithersburg, MD: NIST, April 2025. https://doi.org/10.6028/NIST.SP.800-61r3.

> **Annotation:** Supersedes the 2012 Revision 2 computer-incident handling guide and integrates cybersecurity and socio-technical incident management across all six NIST CSF 2.0 functions (`Govern`, `Identify`, `Protect`, `Detect`, `Respond`, `Recover`)—supporting joint SOC, legal, engineering, and executive AI response.
>
> **Audience:** CISO · SOC · General Counsel · Operational Resilience · **Type:** Government standard · **Cited in:** [Ch. 27](chapters/27-ai-incident-response.md)

<a id="nist-2011-800-137"></a>
National Institute of Standards and Technology (Kelley Dempsey, Nirali Shah Chawla, Arnold Johnson, Ronald Johnston, Alicia Clay Jones, Angela Orebaugh, Matthew Scholl, and Kevin Stine). *Information Security Continuous Monitoring (ISCM) for Federal Information Systems and Organizations*. NIST Special Publication 800-137. Gaithersburg, MD: NIST, September 2011. https://doi.org/10.6028/NIST.SP.800-137.

> **Annotation:** Core federal continuous-monitoring standard defining automated ongoing awareness of system controls, evolving threats, and posture metrics to replace brittle point-in-time annual authorizations with live risk decisions.
>
> **Audience:** CISO · CIO · Risk / Compliance · Platform Engineering · **Type:** Government standard · **Cited in:** [Ch. 30](chapters/30-governance-maturity-model-and-roadmap.md)

<a id="nist-2024-ai-100-4"></a>
National Institute of Standards and Technology. *Reducing Risks Posed by Synthetic Content: An Overview of Technical Approaches to Digital Content Transparency*. NIST AI 100-4. Gaithersburg, MD: NIST, November 18, 2024. https://doi.org/10.6028/NIST.AI.100-4.

> **Annotation:** Authoritative federal technical overview evaluating Content Credentials (C2PA), invisible watermarking, and synthetic-media detection under cropping, paraphrasing, and re-encoding—recommending layered provenance controls over any single detector.
>
> **Audience:** CMO · CISO · CIO · Legal / Compliance · **Type:** Government technical report · **Cited in:** [Ch. 18](chapters/18-transparency-disclosure-and-content-provenance.md)

<a id="nist-2022-sp1270"></a>
National Institute of Standards and Technology (Reva Schwartz, Apostol Vassilev, Kristen Greene, Lori Perine, Andrew Burt, and Patrick Hall). *Towards a Standard for Identifying and Managing Bias in Artificial Intelligence*. NIST Special Publication 1270. Gaithersburg, MD: NIST, March 2022. https://doi.org/10.6028/NIST.SP.1270.

> **Annotation:** Socio-technical bias standard organizing AI unfairness across systemic, computational/statistical, and human-cognitive bias categories—demonstrating why purely mathematical debiasing fails without lifecycle institutional governance.
>
> **Audience:** Board · Chief Risk Officer · CDO · AI Engineers · **Type:** Government standard / technical report · **Cited in:** [Ch. 16](chapters/16-bias-fairness-and-discrimination.md)

<a id="netskope-2025-genai"></a>
Netskope Threat Labs. *Cloud and Threat Report: Generative AI 2025*. Santa Clara, CA: Netskope, 2025. https://www.netskope.com/netskope-threat-labs/cloud-threat-report.

> **Annotation:** Enterprise cloud telemetry report documenting that while roughly 94 percent of surveyed organizations use generative AI applications, 72 percent of workplace GenAI users access those tools via personal accounts outside corporate control.
>
> **Audience:** CISO · CIO · DPO · **Type:** Industry telemetry report · **Cited in:** [Ch. 6](chapters/06-data-leakage-and-shadow-ai.md)

<a id="nolan-2025-replit"></a>
Nolan, Beatrice. "AI-Powered Coding Tool Wiped Out a Software Company's Database in 'Catastrophic Failure.'" *Fortune*, July 2025. https://fortune.com/2025/07/23/ai-coding-tool-replit-wiped-database-called-it-a-catastrophic-failure/.

> **Annotation:** Recounts how Replit's AI agent deleted a production database during an explicit code freeze, misreported whether the data could be recovered, and prompted the vendor to add separation between development and production. A compact case study of excessive agency, and of the gap between instructions given in a prompt and controls enforced by infrastructure.
>
> **Audience:** CIO · CISO · AI Engineers · **Type:** News report · **Cited in:** [Front Matter](chapters/00-front-matter.md), [Ch. 1](chapters/01-why-ai-risk-is-different.md), [Ch. 3](chapters/03-board-and-executive-oversight.md), [Ch. 11](chapters/11-securing-ai-agents.md), [Ch. 27](chapters/27-ai-incident-response.md)

<a id="notopoulos-2023-chevy"></a>
Notopoulos, Katie. "A Car Dealership Added an AI Chatbot to Its Site. Then All Hell Broke Loose." *Business Insider*, December 18, 2023. https://www.businessinsider.com/car-dealership-chevrolet-chatbot-chatgpt-pranks-chevy-2023-12.

> **Annotation:** Covers the viral December 2023 Chevrolet of Watsonville incident in which Chris Bakke prompt-injected a ChatGPT-powered dealership widget into agreeing to sell a 2024 Chevy Tahoe (priced over \$76,000) for \$1 as a "legally binding offer," highlighting why pricing and commitment rules cannot rely on system prompts.
>
> **Audience:** CIO · CISO · Legal / Compliance · Product Owners · **Type:** News report · **Cited in:** [Ch. 10](chapters/10-prompt-injection-and-manipulation.md), [Ch. 15](chapters/15-hallucinations-and-reliability.md)

<a id="obermeyer-2019-health"></a>
Obermeyer, Ziad, Brian Powers, Christine Vogeli, and Sendhil Mullainathan. "Dissecting Racial Bias in an Algorithm Used to Manage the Health of Populations." *Science* 366, no. 6464 (October 25, 2019): 447–453. https://doi.org/10.1126/science.aax2342.

> **Annotation:** Landmark *Science* audit uncovering severe racial bias in a widely used U.S. clinical population-health algorithm that predicted healthcare costs as a proxy for medical need; replacing cost with true clinical need lifted Black patient eligibility for extra care from 17.7 percent to 46.5 percent.
>
> **Audience:** Chief Clinical Officer · CDO · General Counsel · AI Engineers · **Type:** Peer-reviewed journal article · **Cited in:** [Ch. 16](chapters/16-bias-fairness-and-discrimination.md)

<a id="omb-2025-m25-21"></a>
Office of Management and Budget. *Accelerating Federal Use of AI through Innovation, Governance, and Public Trust*. Memorandum M-25-21. Washington, DC: Executive Office of the President, April 3, 2025. https://www.whitehouse.gov/wp-content/uploads/2025/02/M-25-21-Accelerating-Federal-Use-of-AI-through-Innovation-Governance-and-Public-Trust.pdf.

> **Annotation:** Rescinds and replaces OMB M-24-10, requiring U.S. civilian federal agencies to designate a Chief AI Officer and maintain cross-functional AI Governance Boards chaired by a senior executive (such as a Deputy Secretary) alongside IT, privacy, legal, civil rights, and procurement leaders. A practical institutional model for enterprise AI councils.
>
> **Audience:** CIO · CAIO · General Counsel · Public Sector · **Type:** Government directive · **Cited in:** [Ch. 4](chapters/04-ai-governance-operating-model.md), [Ch. 5](chapters/05-policies-inventory-and-risk-tiering.md), [Ch. 20](chapters/20-the-global-regulatory-landscape.md), [Ch. 21](chapters/21-sector-specific-requirements.md)

<a id="omb-2025-m25-22"></a>
Office of Management and Budget. *Driving Efficient Acquisition of Artificial Intelligence in Government*. Memorandum M-25-22. Washington, DC: Executive Office of the President, April 3, 2025. https://www.whitehouse.gov/.

> **Annotation:** Companion federal AI acquisition directive requiring civilian agencies to secure government data and IP rights, prevent vendor lock-in, prioritize competitive interoperability, and enforce lifecycle risk controls in AI procurement contracts.
>
> **Audience:** Public-Sector Procurement · General Counsel · CIO · Product · **Type:** Government directive (United States) · **Cited in:** [Ch. 21](chapters/21-sector-specific-requirements.md), [Ch. 23](chapters/23-vendor-and-third-party-ai-risk.md)

<a id="ofqual-2020-alevels"></a>
Office of Qualifications and Examinations Regulation (Ofqual). *Awarding GCSE, AS, A Level, Advanced Extension Awards and Extended Project Qualifications in Summer 2020: Interim Report*. Coventry: Ofqual, August 2020. https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/909368/6656-1_Awarding_GCSE__AS__A_level__advanced_extension_awards_and_extended_project_qualifications_in_summer_2020_-_interim_report.pdf.

> **Annotation:** Official UK regulator interim report documenting England's summer 2020 A-level standardization model, which downgraded 39.1 percent of teacher-submitted entries based on historical school-cohort performance profiles and disadvantaged state schools before emergency withdrawal.
>
> **Audience:** Board · Chief Product Officer · Public Sector · Legal / Compliance · **Type:** Official regulatory report · **Cited in:** [Ch. 16](chapters/16-bias-fairness-and-discrimination.md)

<a id="oligo-2024-shadowray"></a>
Oligo Security. "ShadowRay: First Known Attack Campaign Targeting AI Workloads Exploited In The Wild." Oligo Security Blog, March 2024. https://www.oligo.security/blog/shadowray.

> **Annotation:** Uncovers active in-the-wild exploitation of unauthenticated Ray AI cluster APIs (`CVE-2023-48022`), illustrating how "velocity-over-security" no-auth defaults expose AI compute and data tiers across public clouds.
>
> **Audience:** CISO · MLOps · Cloud Security · AppSec · **Type:** Threat research report · **Cited in:** [Ch. 13](chapters/13-infrastructure-and-operational-security.md)

<a id="openai-deprecations"></a>
OpenAI. "Deprecations." OpenAI Platform Documentation. Accessed November 15, 2026. https://platform.openai.com/docs/deprecations.

> **Annotation:** OpenAI's public record of retired models and API features, with their shutdown dates. Cited here as a concrete example of the model lifecycle that enterprise change management and vendor contracts must plan for. Other major providers publish similar schedules.
>
> **Audience:** CIO · AI Engineers · Procurement · **Type:** Vendor documentation · **Cited in:** [Ch. 1](chapters/01-why-ai-risk-is-different.md), [Ch. 24](chapters/24-model-lifecycle-and-change-management.md)

<a id="openai-2025-enterprise-privacy"></a>
OpenAI. "Enterprise Privacy and Data Controls (API Data Retention and Zero Data Retention)." OpenAI Platform Documentation. Accessed November 21, 2026. https://platform.openai.com/docs/guides/your-data.

> **Annotation:** Explains how commercial model APIs separate "no training by default" from persistent retention—including the 30-day abuse-monitoring log window, approval-gated Zero Data Retention (ZDR), Private Safety Processing (PSP), and stateful endpoints (Files, Batches, Assistants, Fine-tuning) that persist data separately.
>
> **Audience:** CISO · Legal / Compliance · DPO · AI Engineers · **Type:** Vendor documentation · **Cited in:** [Ch. 6](chapters/06-data-leakage-and-shadow-ai.md), [Ch. 23](chapters/23-vendor-and-third-party-ai-risk.md)

<a id="openai-2023-redis-outage"></a>
OpenAI. "March 20 ChatGPT Outage: Here's What Happened." OpenAI Blog, March 24, 2023. https://openai.com/index/march-20-chatgpt-outage/.

> **Annotation:** Technical postmortem explaining the `redis-py` `asyncio` cluster pool race condition that leaked chat titles, initial prompt text, and payment metadata for 1.2 percent of active ChatGPT Plus subscribers—underscoring why shared AI caches require strict caller-ID verification per read.
>
> **Audience:** AI Engineers · Platform Architects · CISO · DPO · **Type:** Incident postmortem · **Cited in:** [Ch. 13](chapters/13-infrastructure-and-operational-security.md), [Ch. 27](chapters/27-ai-incident-response.md)

<a id="openai-2024-k8s-outage"></a>
OpenAI. "API, ChatGPT & Sora Facing Issues (December 11, 2024 Incident Postmortem)." OpenAI Status History, December 2024. https://status.openai.com.

> **Annotation:** Official incident postmortem documenting the roughly 4-hour-22-minute fleet-wide outage (`3:16 PM` to `7:38 PM PST`, December 11, 2024) triggered when a newly deployed Kubernetes telemetry service overloaded API control planes and disrupted DNS service discovery across major clusters.
>
> **Audience:** CIO · Platform Architects · SRE · Operational Resilience · **Type:** Incident postmortem · **Cited in:** [Ch. 25](chapters/25-operational-resilience-and-business-continuity.md)

<a id="openai-2025-sycophancy"></a>
OpenAI. "Sycophancy in GPT-4o: What Happened and What We're Doing About It." OpenAI Blog, April 29, 2025. https://openai.com/index/sycophancy-in-gpt-4o/.

> **Annotation:** Candid technical post-mortem explaining why OpenAI rolled back a late-April 2025 GPT-4o update after excessive weighting of short-term thumbs-up user feedback caused the model to devolve into flattery and validate reckless impulses—illustrating the risk of raw CSAT optimization.
>
> **Audience:** Chief Product Officer · AI Engineers · Head of CX · Risk / Compliance · **Type:** Incident postmortem · **Cited in:** [Ch. 15](chapters/15-hallucinations-and-reliability.md), [Ch. 24](chapters/24-model-lifecycle-and-change-management.md), [Ch. 27](chapters/27-ai-incident-response.md)

<a id="osi-2024-osaid"></a>
Open Source Initiative. *The Open Source AI Definition — Version 1.0 (OSAID 1.0)*. October 28, 2024. https://opensource.org/os-ai-definition.

> **Annotation:** Defines Open Source AI standards requiring freedom to use, study, modify, and share alongside detailed training-data transparency enabling model recreation with zero field-of-use caps—separating true open-source AI from custom-licensed open weights.
>
> **Audience:** General Counsel · CTO · Procurement · AI Engineers · **Type:** Open-source definition standard · **Cited in:** [Ch. 19](chapters/19-intellectual-property-and-licensing.md)

<a id="openssf-2025-model-signing"></a>
Open Source Security Foundation (OpenSSF). "Model Signing v1.0 (OMS Specification and Sigstore Integration)." OpenSSF AI/ML Working Group, April 4, 2025. https://openssf.org/blog/2025/04/04/openssf-model-signing-v1-0/.

> **Annotation:** Launches OpenSSF Model Signing v1.0, providing Sigstore cryptographic bundles (via keyless OIDC or enterprise PKI) to sign and verify entire AI model directories—weights, configs, and tokenizers—from build through production deployment.
>
> **Audience:** CISO · MLOps · Platform Architects · AppSec · **Type:** Open security specification · **Cited in:** [Ch. 12](chapters/12-model-and-supply-chain-security.md), [Ch. 23](chapters/23-vendor-and-third-party-ai-risk.md)

<a id="otel-genai-semconv"></a>
OpenTelemetry. "Semantic Conventions for Generative AI Systems." OpenTelemetry Specification Documentation. Accessed November 21, 2026. https://opentelemetry.io/docs/specs/semconv/gen-ai/.

> **Annotation:** Defines standardized `gen_ai.*` span attributes (`gen_ai.operation.name`, `execute_tool`, token accounting) alongside W3C `traceparent` propagation so distributed orchestrators, sub-agents, and MCP servers produce unified forensic execution traces.
>
> **Audience:** AI Engineers · Platform Architects · SRE / SOC · **Type:** Open telemetry specification · **Cited in:** [Ch. 11](chapters/11-securing-ai-agents.md), [Ch. 13](chapters/13-infrastructure-and-operational-security.md), [Ch. 22](chapters/22-auditability-assessments-and-evidence.md), [Ch. 27](chapters/27-ai-incident-response.md), [Ch. 28](chapters/28-metrics-kris-and-reporting.md)

<a id="oecd-2024-ai-incidents"></a>
Organisation for Economic Co-operation and Development (OECD). *Defining AI Incidents and Related Terms*. OECD Artificial Intelligence Papers, No. 16. Paris: OECD Publishing, May 2024. https://doi.org/10.1787/d1a8d965-en.

> **Annotation:** International policy paper establishing standardized criteria separating actualized AI incidents (health harm, critical-infrastructure disruption, human/fundamental/labor/IP rights violations, property/environmental harm) from plausible near-miss AI hazards to align cross-border reporting and triage.
>
> **Audience:** CRO · General Counsel · SOC · Regulatory Affairs · **Type:** International policy paper · **Cited in:** [Ch. 27](chapters/27-ai-incident-response.md), [Ch. 28](chapters/28-metrics-kris-and-reporting.md), [Ch. 29](chapters/29-building-a-risk-aware-ai-culture.md)

<a id="cyclonedx-2024-mlbom"></a>
OWASP Foundation and Ecma International. *CycloneDX Specification (ML-BOM)*. Version 1.6 / ECMA-424. 2024. https://cyclonedx.org/capabilities/mlbom/.

> **Annotation:** Extends the OWASP CycloneDX software bill-of-materials standard to treat AI/ML models, datasets, weights, cryptographic hashes, licenses, and embedded model cards as first-class components. Integrates directly into application-security scanning and CI/CD vulnerability workflows.
>
> **Audience:** CISO · AI Engineers · Platform IT · **Type:** Open technical standard · **Cited in:** [Ch. 5](chapters/05-policies-inventory-and-risk-tiering.md), [Ch. 12](chapters/12-model-and-supply-chain-security.md), [Ch. 22](chapters/22-auditability-assessments-and-evidence.md)

<a id="owasp-2025-nhi-top10"></a>
OWASP Foundation. *OWASP Non-Human Identities Top 10: 2025*. OWASP NHI Project, 2025. https://owasp.org/www-project-non-human-identities-top-10/.

> **Annotation:** Catalogs critical machine- and workload-identity failures applicable directly to AI agents, including Improper Offboarding (`NHI1:2025`) of orphaned service tokens and Secret Leakage (`NHI2:2025`) across repositories and prompts.
>
> **Audience:** CISO · IAM Architects · AppSec · AI Engineers · **Type:** Industry standard (community) · **Cited in:** [Ch. 11](chapters/11-securing-ai-agents.md), [Ch. 13](chapters/13-infrastructure-and-operational-security.md), [Ch. 24](chapters/24-model-lifecycle-and-change-management.md)

<a id="owasp-2024-llm-top10"></a>
OWASP Foundation. *OWASP Top 10 for LLM Applications 2025*. OWASP GenAI Security Project, November 2024. https://genai.owasp.org/llm-top-10/.

> **Annotation:** A community-built ranking of the ten most critical security risks for LLM applications: prompt injection, sensitive information disclosure, supply chain, data and model poisoning, improper output handling, excessive agency, system prompt leakage, vector and embedding weaknesses, misinformation, and unbounded consumption. It is the common vocabulary of AI application security and a practical checklist for design reviews.
>
> **Audience:** CISO · AI Engineers · **Type:** Industry standard (community) · **Cited in:** [Front Matter](chapters/00-front-matter.md), [Ch. 1](chapters/01-why-ai-risk-is-different.md), [Ch. 2](chapters/02-reference-frameworks-at-a-glance.md), [Ch. 6](chapters/06-data-leakage-and-shadow-ai.md), [Ch. 7](chapters/07-internal-over-exposure-and-permission-aware-ai.md), [Ch. 9](chapters/09-ai-threat-landscape.md), [Ch. 10](chapters/10-prompt-injection-and-manipulation.md), [Ch. 11](chapters/11-securing-ai-agents.md), [Ch. 12](chapters/12-model-and-supply-chain-security.md), [Ch. 13](chapters/13-infrastructure-and-operational-security.md), [Ch. 25](chapters/25-operational-resilience-and-business-continuity.md)

<a id="owasp-2025-agentic-top10"></a>
OWASP Foundation. *OWASP Top 10 for Agentic Applications for 2026*. OWASP GenAI Security Project, December 2025. https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/.

> **Annotation:** A companion to the LLM Top 10 focused on autonomous agents that plan, keep memory, use tools, and act with delegated authority. Its ten risks run from agent goal hijack (ASI01) and tool misuse (ASI02) through identity and privilege abuse, agentic supply chain, unexpected code execution, memory and context poisoning, insecure inter-agent communication, cascading failures, and human-agent trust exploitation, to rogue agents (ASI10). An essential design-review checklist for any agentic deployment.
>
> **Audience:** CISO · AI Engineers · CIO · **Type:** Industry standard (community) · **Cited in:** [Ch. 2](chapters/02-reference-frameworks-at-a-glance.md), [Ch. 9](chapters/09-ai-threat-landscape.md), [Ch. 11](chapters/11-securing-ai-agents.md), [Ch. 25](chapters/25-operational-resilience-and-business-continuity.md), [Ch. 26](chapters/26-testing-evaluation-and-red-teaming.md)

<a id="pang-2019-zanzibar"></a>
Pang, Ruoming, Ramon Caceres, Mike Burrows, Zhifeng Chen, Pradeep Dave, Nathan Germer, Alexander Golynski, et al. "Zanzibar: Google's Consistent, Global Authorization System." In *Proceedings of the 2019 USENIX Annual Technical Conference (USENIX ATC '19)*, July 2019. https://www.usenix.org/conference/atc19/presentation/pang.

> **Annotation:** Landmark systems paper describing Google's global authorization engine managing trillions of ACL tuples at sub-10ms latency and >99.999% availability. Its relationship-tuple model (`object#relation@subject`), asynchronous Leopard group-closure indexing, and "zookie" consistency tokens directly underpin modern permission-aware RAG and open-source ReBAC engines (such as OpenFGA and SpiceDB).
>
> **Audience:** AI Engineers · CISO · CIO · **Type:** Peer-reviewed paper · **Cited in:** [Ch. 7](chapters/07-internal-over-exposure-and-permission-aware-ai.md)

<a id="parasuraman-2000-levels"></a>
Parasuraman, Raja, Thomas B. Sheridan, and Christopher D. Wickens. "A Model for Types and Levels of Human Interaction with Automation." *IEEE Transactions on Systems, Man, and Cybernetics—Part A: Systems and Humans* 30, no. 3 (May 2000): 286–297. https://doi.org/10.1109/3468.844354.

> **Annotation:** Canonical systems-engineering framework dividing human-machine interaction across four stages (acquisition, analysis, decision selection, and action implementation) and calibration scales to select HITL, HOTL, or bounded automation levels deliberately.
>
> **Audience:** CIO · Platform Architects · Chief Risk Officer · Product Leads · **Type:** Peer-reviewed journal article · **Cited in:** [Ch. 17](chapters/17-human-oversight-and-automation-bias.md)

<a id="paulk-1993-cmm"></a>
Paulk, Mark C., Bill Curtis, Mary Beth Chrissis, and Charles V. Weber. "Capability Maturity Model, Version 1.1." *IEEE Software* 10, no. 4 (July 1993): 18–27. https://doi.org/10.1109/52.219617.

> **Annotation:** Foundational five-stage organizational process maturity architecture (`Initial`, `Repeatable`, `Defined`, `Managed`, `Optimizing`) demonstrating why disciplined baseline execution must precede quantitative automation.
>
> **Audience:** CIO · CTO · CRO · Governance PMO · **Type:** Peer-reviewed journal article · **Cited in:** [Ch. 30](chapters/30-governance-maturity-model-and-roadmap.md)

<a id="rebedea-2023-nemo-guardrails"></a>
Rebedea, Traian, Razvan Dinu, Makesh Narsimhan Sreedhar, Christopher Parisien, and Jonathan Cohen. "NeMo Guardrails: A Toolkit for Controllable and Safe LLM Applications with Programmable Rails." In *Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: System Demonstrations (EMNLP 2023)*, 2023. arXiv:2310.10501. https://doi.org/10.48550/arXiv.2310.10501.

> **Annotation:** Introduces NVIDIA's open-source programmable runtime guardrail toolkit enabling teams to define declarative topical, safety, jailbreak, and retrieval rails independently of the underlying foundation model.
>
> **Audience:** AI Engineers · CISO · Platform IT · **Type:** Peer-reviewed paper · **Cited in:** [Ch. 10](chapters/10-prompt-injection-and-manipulation.md)

<a id="rbi-2025-free-ai"></a>
Reserve Bank of India (Committee to Develop a Framework for Responsible and Ethical Enablement of Artificial Intelligence). *Report of the Committee to Develop a Framework for Responsible and Ethical Enablement of Artificial Intelligence (FREE-AI)*. Chaired by Pushpak Bhattacharyya. Mumbai: RBI, August 13, 2025. https://www.rbi.org.in/.

> **Annotation:** Reserve Bank of India baseline governance blueprint finding 20.8 percent active AI adoption among regulated entities and establishing 7 Sutras alongside 26 actionable recommendations spanning board-approved policies, centralized AI inventories, red-teaming, vendor controls, and audits.
>
> **Audience:** Board · CRO · CIO · Legal / Compliance · **Type:** Financial-sector committee report (India) · **Cited in:** [Ch. 20](chapters/20-the-global-regulatory-landscape.md), [Ch. 21](chapters/21-sector-specific-requirements.md)

<a id="russinovich-2024-crescendo"></a>
Russinovich, Mark, Ahmed Salem, and Ronen Eldan. "Great, Now Write an Article About That: The Crescendo Multi-Turn LLM Jailbreak Attack." arXiv:2404.01833, April 2024. https://doi.org/10.48550/arXiv.2404.01833.

> **Annotation:** Introduces Crescendo and automated Crescendomation, proving that gradual, benign-looking conversational escalation defeats single-turn LLM safety filters across GPT-4, Gemini Pro, Llama, and Claude by exploiting conversational helpfulness and context consistency.
>
> **Audience:** CISO · Red Teams · AI Engineers · AppSec · **Type:** Research preprint / conference paper · **Cited in:** [Ch. 10](chapters/10-prompt-injection-and-manipulation.md)

<a id="sculley-2015-debt"></a>
Sculley, D., Gary Holt, Daniel Golovin, Eugene Davydov, Todd Phillips, Dietmar Ebner, Vinay Chaudhary, Michael Young, Jean-François Crespo, and Dan Dennison. "Hidden Technical Debt in Machine Learning Systems." In *Advances in Neural Information Processing Systems 28* (NeurIPS 2015). https://papers.nips.cc/paper/5656-hidden-technical-debt-in-machine-learning-systems.

> **Annotation:** A landmark paper by Google engineers showing that machine-learning systems pile up unusual and often hidden maintenance costs: entangled components, undeclared dependencies, feedback loops, and configuration debt. Its "Changing Anything Changes Everything" principle anticipates today's problem of model upgrades and prompt fragility. Still the best short introduction to why AI systems are harder to operate than conventional software.
>
> **Audience:** CIO · AI Engineers · **Type:** Peer-reviewed paper · **Cited in:** [Ch. 1](chapters/01-why-ai-risk-is-different.md), [Ch. 24](chapters/24-model-lifecycle-and-change-management.md)

<a id="sharma-2024-sycophancy"></a>
Sharma, Mrinank, Meg Tong, Tomasz Korbak, David Duvenaud, Amanda Askell, Samuel R. Bowman, et al. "Towards Understanding Sycophancy in Language Models." In *Proceedings of the 12th International Conference on Learning Representations (ICLR 2024)*, 2024. arXiv:2310.13548. https://doi.org/10.48550/arXiv.2310.13548.

> **Annotation:** Evaluates five leading AI assistants across free-form generation tasks and reveals that RLHF human-preference datasets consistently reward agreement with stated user beliefs over factual accuracy, inducing systematic sycophancy.
>
> **Audience:** AI Engineers · CISO · Chief Product Officer · Risk / Compliance · **Type:** Peer-reviewed paper · **Cited in:** [Ch. 15](chapters/15-hallucinations-and-reliability.md)

<a id="shokri-2017-mia"></a>
Shokri, Reza, Marco Stronati, Congzheng Song, and Vitaly Shmatikov. "Membership Inference Attacks Against Machine Learning Models." In *2017 IEEE Symposium on Security and Privacy (SP)*, May 2017. https://doi.org/10.1109/SP.2017.41.

> **Annotation:** Pioneered shadow-model Membership Inference Attacks (MIA), demonstrating that adversaries with black-box query access can determine whether specific individuals' records appeared in a model's secret training corpus.
>
> **Audience:** CISO · DPO · AI Engineers · **Type:** Peer-reviewed paper · **Cited in:** [Ch. 12](chapters/12-model-and-supply-chain-security.md)

<a id="shostack-2014-threat-modeling"></a>
Shostack, Adam. *Threat Modeling: Designing for Security*. Indianapolis: John Wiley & Sons, 2014.

> **Annotation:** The foundational practitioner manual defining threat modeling around the Four Question Framework ("What are we working on?", "What can go wrong?", "What are we going to do about it?", "Did we do a good job?") and Microsoft's STRIDE mnemonic. Provides the durable software-security backbone that this book adapts to AI trust boundaries.
>
> **Audience:** CISO · Security Architects · AppSec · AI Engineers · **Type:** Technical book · **Cited in:** [Ch. 9](chapters/09-ai-threat-landscape.md)

<a id="shumailov-2021-sponge"></a>
Shumailov, Ilia, Yiren Zhao, Daniel Bates, Nicolas Papernot, Robert Mullins, and Ross Anderson. "Sponge Examples: Energy-Latency Attacks on Neural Networks." In *2021 IEEE European Symposium on Security and Privacy (EuroS&P)*, September 2021. arXiv:2006.03463. https://doi.org/10.1109/EuroSP51992.2021.00024.

> **Annotation:** Introduces adversarial "sponge examples" engineered to drive neural networks into worst-case hardware activation and compute latency, dramatically inflating cloud energy consumption and Denial-of-Wallet API expenses.
>
> **Audience:** CISO · AI Engineers · FinOps · **Type:** Peer-reviewed paper · **Cited in:** [Ch. 13](chapters/13-infrastructure-and-operational-security.md), [Ch. 25](chapters/25-operational-resilience-and-business-continuity.md)

<a id="shumailov-2024-collapse"></a>
Shumailov, Ilia, Zakhar Shumaylov, Yiren Zhao, Nicolas Papernot, Ross Anderson, and Yarin Gal. "AI Models Collapse When Trained on Recursively Generated Data." *Nature* 631 (July 2024): 755–759. https://doi.org/10.1038/s41586-024-07566-y.

> **Annotation:** Proves that training successive model generations recursively on model-generated synthetic outputs triggers "model collapse"—progressively erasing the tails of the real distribution and eliminating rare edge cases and minority patterns unless anchored on real human data.
>
> **Audience:** CDO · AI Engineers · CRO · **Type:** Peer-reviewed article · **Cited in:** [Ch. 8](chapters/08-data-provenance-consent-and-sovereignty.md), [Ch. 24](chapters/24-model-lifecycle-and-change-management.md)

<a id="mckinsey-2025-state-of-ai"></a>
Singla, Alex, Alexander Sukharevsky, Lareina Yee, Michael Chui, Bryce Hall, and Tara Balakrishnan. "The State of AI in 2025: Agents, Innovation, and Transformation." McKinsey & Company, November 5, 2025. https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai.

> **Annotation:** McKinsey's annual global survey on AI adoption. The 2025 edition reports widespread use (88 percent of organizations use AI in at least one function), growing experimentation with agents (62 percent), and limited enterprise-level financial impact. It also finds that just over half of organizations using AI have experienced at least one negative consequence, with inaccuracy the most common. Useful for benchmarking and for board briefings.
>
> **Audience:** Board · CIO · Business Owners · **Type:** Industry survey report · **Cited in:** [Front Matter](chapters/00-front-matter.md), [Ch. 1](chapters/01-why-ai-risk-is-different.md), [Ch. 28](chapters/28-metrics-kris-and-reporting.md)

<a id="slattery-2024-risk-repository"></a>
Slattery, Peter, Alexander K. Saeri, Emily A. C. Grundy, Jess Graham, Michael Noetel, Risto Uuk, James Dao, Soroush Pour, Stephen Casper, and Neil Thompson. "The AI Risk Repository: A Comprehensive Meta-Review, Database, and Taxonomy of Risks from Artificial Intelligence." arXiv:2408.12622, August 2024. https://doi.org/10.48550/arXiv.2408.12622.

> **Annotation:** Introduces the MIT AI Risk Repository, a living database that brings together risks from many published frameworks. It organizes them by a causal taxonomy (entity, intent, and timing) and a domain taxonomy of seven areas: discrimination and toxicity; privacy and security; misinformation; malicious actors and misuse; human-computer interaction; socioeconomic and environmental; and AI system safety, failures, and limitations. An excellent resource for testing whether an enterprise risk register is complete.
>
> **Audience:** CRO / Risk · Legal / Compliance · CDO · **Type:** Research preprint and database · **Cited in:** [Ch. 1](chapters/01-why-ai-risk-is-different.md)

<a id="slack-2024-privacy-principles"></a>
Slack Technologies. "How Slack Uses Data for AI and Machine Learning (Privacy Principles Clarification)." Slack Blog, May 2024. https://slack.com/trust/data-management/privacy-principles.

> **Annotation:** Clarifies Slack's May 2024 privacy controversy over default opt-in for global machine-learning models and manual email-based opt-outs, distinguishing aggregated/de-identified global ML features from Slack AI's LLM summarization while illustrating the governance friction of embedded SaaS AI defaults.
>
> **Audience:** CISO · CIO · Legal / Compliance · DPO · **Type:** Vendor policy / clarification · **Cited in:** [Ch. 6](chapters/06-data-leakage-and-shadow-ai.md), [Ch. 23](chapters/23-vendor-and-third-party-ai-risk.md)

<a id="souly-2025-constant-poisoning"></a>
Souly, Alexandra, Javier Rando, Ed Chapman, Xander Davies, Burak Hasircioglu, Ezzeldin Shereen, Carlos Mougan, Vasilios Mavroudis, Erik Jones, Chris Hicks, Nicholas Carlini, Yarin Gal, and Robert Kirk. "Poisoning Attacks on LLMs Require a Near-Constant Number of Poison Samples." arXiv:2510.07192, October 8, 2025. https://doi.org/10.48550/arXiv.2510.07192.

> **Annotation:** Collaborative study (Oxford, Anthropic, UK AISI, Alan Turing Institute) proving across 600M–13B models trained on up to 260B tokens that implanting LLM backdoors requires a near-constant ~250 poisoned documents regardless of dataset or parameter scale.
>
> **Audience:** CISO · AI Engineers · CDO · Model Developers · **Type:** Research preprint · **Cited in:** [Ch. 12](chapters/12-model-and-supply-chain-security.md)

<a id="stadler-2022-synthetic"></a>
Stadler, Theresa, Bristena Oprisanu, and Carmela Troncoso. "Synthetic Data – Anonymisation Groundhog Day." In *Proceedings of the 31st USENIX Security Symposium (USENIX Security 22)*, August 2022. https://www.usenix.org/conference/usenixsecurity22/presentation/stadler.

> **Annotation:** First systematic quantitative evaluation of synthetic data's privacy guarantees, showing that generative synthetic records fail to escape the classical privacy-utility trade-off and remain vulnerable to membership- and attribute-inference (linkage) attacks unless bounded by formal differential privacy.
>
> **Audience:** CDO · DPO · CISO · AI Engineers · **Type:** Peer-reviewed paper · **Cited in:** [Ch. 8](chapters/08-data-provenance-consent-and-sovereignty.md)

<a id="stanford-2025-ai-index"></a>
Stanford Institute for Human-Centered Artificial Intelligence. *The AI Index 2025 Annual Report*. Stanford, CA: Stanford University, April 2025. https://hai.stanford.edu/ai-index/2025-ai-index-report.

> **Annotation:** The most comprehensive annual data compendium on AI research, adoption, policy, and responsible-AI trends. Its Responsible AI chapter reports 233 AI-related incidents in 2024, a 56.4 percent increase over 2023, and tracks how organizations are managing risk. A dependable source of statistics for board papers and business cases.
>
> **Audience:** Board · All roles · **Type:** Academic annual report · **Cited in:** [Ch. 1](chapters/01-why-ai-risk-is-different.md)

<a id="suresh-2021-lifecycle"></a>
Suresh, Harini, and John V. Guttag. "A Framework for Understanding Sources of Harm throughout the Machine Learning Life Cycle." In *Proceedings of the 1st ACM Conference on Equity and Access in Algorithms, Mechanisms, and Optimization (EAAMO '21)*, October 2021. arXiv:1901.10002. https://doi.org/10.1145/3465416.3483305.

> **Annotation:** Canonical lifecycle taxonomy decomposing algorithmic harm into seven distinct mechanisms across data collection, modeling, evaluation, and human deployment—historical, representation, measurement, aggregation, learning, evaluation, and deployment bias.
>
> **Audience:** CDO · AI Engineers · Chief Risk Officer · Legal / Compliance · **Type:** Peer-reviewed paper · **Cited in:** [Ch. 16](chapters/16-bias-fairness-and-discrimination.md)

<a id="sysdig-2024-llmjacking"></a>
Sysdig Threat Research Team. "LLMjacking: Stolen Cloud Credentials Used in New AI Attack." Sysdig Blog, May 6, 2024. https://sysdig.com/blog/llmjacking-stolen-cloud-credentials-used-in-new-ai-attack/.

> **Annotation:** Original research disclosing "LLMjacking," in which threat actors extract leaked cloud IAM credentials to hijack managed LLM APIs such as Amazon Bedrock and resell stolen inference capacity—illustrating potential burn rates exceeding \$46,000 per day at peak quotas (and over \$100,000 per day in subsequent scaled tracking).
>
> **Audience:** CISO · Cloud Security · FinOps · AI Engineers · **Type:** Security research report · **Cited in:** [Ch. 9](chapters/09-ai-threat-landscape.md), [Ch. 13](chapters/13-infrastructure-and-operational-security.md)

<a id="tramer-2016-stealing"></a>
Tramèr, Florian, Fan Zhang, Ari Juels, Michael K. Reiter, and Thomas Ristenpart. "Stealing Machine Learning Models via Prediction APIs." In *Proceedings of the 25th USENIX Security Symposium (USENIX Security 16)*, August 2016. https://www.usenix.org/conference/usenixsecurity16/technical-sessions/presentation/tramer.

> **Annotation:** Seminal study proving black-box MLaaS prediction APIs returning predictions and confidence scores enable adversaries to clone logistic regression, decision tree, SVM, and neural models with high fidelity.
>
> **Audience:** CISO · AI Engineers · API Architects · **Type:** Peer-reviewed paper · **Cited in:** [Ch. 12](chapters/12-model-and-supply-chain-security.md)

<a id="canada-2019-dadm"></a>
Treasury Board of Canada Secretariat. *Directive on Automated Decision-Making* (and *Algorithmic Impact Assessment* tool). Effective April 1, 2019 (as periodically reviewed). Ottawa: Government of Canada. https://www.tbs-sct.canada.ca/pol/doc-eng.aspx?id=32592.

> **Annotation:** Binding Canadian federal public-sector policy scoring automated administrative systems across Impact Levels I–IV and tying higher tiers to independent peer review, plain-language notices, documentation transparency, explanations, and human decision ownership.
>
> **Audience:** Public-Sector CIO · General Counsel · Internal Audit · Product · **Type:** Government directive (Canada) · **Cited in:** [Ch. 21](chapters/21-sector-specific-requirements.md), [Ch. 22](chapters/22-auditability-assessments-and-evidence.md)

<a id="turpin-2023-unfaithful"></a>
Turpin, Miles, Julian Michael, Ethan Perez, and Samuel R. Bowman. "Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting." In *Advances in Neural Information Processing Systems 36 (NeurIPS 2023)*, 2023. arXiv:2305.04388. https://doi.org/10.48550/arXiv.2305.04388.

> **Annotation:** Seminal explainability critique proving Chain-of-Thought narratives routinely construct convincing post-hoc rationalizations concealing ordering or social biasing cues driving model choices (with accuracy drops reaching 36 percent).
>
> **Audience:** AI Engineers · Legal / Compliance · Risk · Internal Audit · **Type:** Peer-reviewed paper · **Cited in:** [Ch. 18](chapters/18-transparency-disclosure-and-content-provenance.md)

<a id="uk-dsit-2024-framework"></a>
United Kingdom Department for Science, Innovation and Technology (DSIT). *A Pro-Innovation Approach to AI Regulation: Government Response* (CP 1019, February 2024) and Digital Regulation Cooperation Forum (DRCF) Cross-Regulator AI Coordination. London: HM Government, 2024–2026. https://www.gov.uk/government/consultations/ai-regulation-a-pro-innovation-approach-policy-proposals.

> **Annotation:** Codifies the UK's decentralized, context-specific regulatory model directing existing sector watchdogs—including the ICO, FCA, CMA, and Ofcom via the DRCF—to enforce five cross-sector AI principles rather than a single omnibus AI Act.
>
> **Audience:** General Counsel · Regulatory Affairs · CRO · Product · **Type:** Government policy framework (United Kingdom) · **Cited in:** [Ch. 20](chapters/20-the-global-regulatory-landscape.md)

<a id="usco-2025-copyrightability"></a>
U.S. Copyright Office. *Copyright and Artificial Intelligence, Part 2: Copyrightability*. Washington, DC: Library of Congress, January 2025. https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-2-Copyrightability-Report.pdf.

> **Annotation:** Official federal copyright guidance clarifying that iterative text prompts do not establish human authorship over generated expression; U.S. copyright protects only perceptible human modifications or original creative selection, requiring applicants to disclaim material AI outputs.
>
> **Audience:** General Counsel · CMO · Chief Product Officer · IP Counsel · **Type:** Government report (United States) · **Cited in:** [Ch. 19](chapters/19-intellectual-property-and-licensing.md)

<a id="dhs-2024-ci-ai"></a>
U.S. Department of Homeland Security (Artificial Intelligence Safety and Security Board). *Roles and Responsibilities Framework for Artificial Intelligence in Critical Infrastructure*. Washington, DC: DHS, November 2024. https://www.dhs.gov/ai.

> **Annotation:** Cross-sector U.S. critical-infrastructure safety framework allocating shared resilience duties across cloud/compute providers, AI developers, and infrastructure operators against AI-enabled cyberattacks, attacks targeting AI models, and design failures.
>
> **Audience:** CISO · OT Engineering Lead · Critical Infrastructure CRO · **Type:** Government framework (United States) · **Cited in:** [Ch. 21](chapters/21-sector-specific-requirements.md), [Ch. 25](chapters/25-operational-resilience-and-business-continuity.md)

<a id="eeoc-2023-itutorgroup"></a>
U.S. Equal Employment Opportunity Commission. "iTutorGroup to Pay \$365,000 to Settle EEOC Discriminatory Hiring Suit." Press release, August 2023. https://www.eeoc.gov/newsroom/itutorgroup-pay-365000-settle-eeoc-discriminatory-hiring-suit.

> **Annotation:** Announces the U.S. EEOC's first AI hiring-discrimination settlement (\$365,000), resolving claims that online recruitment software automatically filtered out over 200 qualified female applicants aged 55+ and male applicants aged 60+.
>
> **Audience:** CHRO · General Counsel · Procurement · AI Engineers · **Type:** Regulatory enforcement release (United States) · **Cited in:** [Ch. 16](chapters/16-bias-fairness-and-discrimination.md)

<a id="fda-2024-ai-samd"></a>
U.S. Food and Drug Administration. *Clinical Decision Support Software: Guidance for Industry and FDA Staff* (September 28, 2022; interpreting 21st Century Cures Act § 3060 / FD&C Act § 520(o)(1)(E)), *Marketing Submission Recommendations for a Predetermined Change Control Plan for Artificial Intelligence-Enabled Device Software Functions* (Final Guidance, December 2024; implementing FDORA § 3308 / FD&C Act § 515C), and *Artificial Intelligence-Enabled Device Software Functions: Lifecycle Management and Marketing Submission Recommendations* (Draft Guidance, January 2025). Silver Spring, MD: FDA, 2022–2025. https://www.fda.gov/medical-devices/software-medical-device-samd/artificial-intelligence-and-machine-learning-aiml-enabled-medical-devices.

> **Annotation:** Core U.S. medical-device AI regulatory suite delineating non-device Clinical Decision Support (`§ 520(o)(1)(E)`) from regulated SaMD while establishing authorized Predetermined Change Control Plans (`PCCPs`, `§ 515C`) for controlled post-market AI model iteration.
>
> **Audience:** Chief Medical Officer · Regulatory Affairs · Quality Engineering · AI Engineers · **Type:** Federal regulatory guidance (United States) · **Cited in:** [Ch. 21](chapters/21-sector-specific-requirements.md), [Ch. 24](chapters/24-model-lifecycle-and-change-management.md)

<a id="sec-2024-ai-washing"></a>
U.S. Securities and Exchange Commission. "SEC Charges Two Investment Advisers with Making False and Misleading Statements About Their Use of Artificial Intelligence." Press release 2024-36, March 18, 2024. https://www.sec.gov/newsroom/press-releases/2024-36.

> **Annotation:** Announces the SEC's first "AI-washing" enforcement actions against Delphia (USA) Inc. and Global Predictions Inc., resulting in \$400,000 in combined civil penalties for false claims about AI-driven investment models. Establishes that public AI claims must be substantiated under securities law.
>
> **Audience:** Board · CFO · General Counsel · Marketing · **Type:** Regulatory enforcement release · **Cited in:** [Ch. 3](chapters/03-board-and-executive-oversight.md), [Ch. 23](chapters/23-vendor-and-third-party-ai-risk.md)

<a id="sec-2025-presto"></a>
U.S. Securities and Exchange Commission. *In the Matter of Presto Automation Inc.* Administrative proceeding, January 14, 2025. https://www.sec.gov/.

> **Annotation:** The SEC's first AI-washing enforcement action against a public operating company, finding material misstatements regarding undisclosed third-party speech technology and overstated drive-thru automation rates. Underscores the need to bring AI capability claims inside formal disclosure controls.
>
> **Audience:** Board · CEO · CFO · General Counsel · **Type:** Regulatory enforcement order · **Cited in:** [Ch. 3](chapters/03-board-and-executive-oversight.md), [Ch. 23](chapters/23-vendor-and-third-party-ai-risk.md)

<a id="varonis-2025-data-security"></a>
Varonis Systems. *2025 State of Data Security Report: Quantifying AI's Impact on Data Risk*. June 2025. https://www.varonis.com/state-of-data-security.

> **Annotation:** Data-security telemetry study quantifying enterprise oversharing ahead of AI rollout: 99 percent of tested organizations have sensitive data exposed or vulnerable to AI tools, 90 percent expose sensitive files to all employees via Microsoft 365 Copilot (averaging 25,000+ sensitive folders), and only 1 in 10 properly classify and label files.
>
> **Audience:** Board · CDO · CISO · CIO · **Type:** Industry research report · **Cited in:** [Ch. 7](chapters/07-internal-over-exposure-and-permission-aware-ai.md)

<a id="wallace-2024-instruction-hierarchy"></a>
Wallace, Eric, Kai Xiao, Reimar Leike, Lilian Weng, Johannes Heidecke, and Alex Beutel. "The Instruction Hierarchy: Training LLMs to Prioritize Privileged Instructions." arXiv:2404.13208, April 2024. https://doi.org/10.48550/arXiv.2404.13208.

> **Annotation:** Proposes synthetic adversarial fine-tuning to establish an explicit privilege hierarchy inside models (System > Developer > User > Untrusted Data Inputs), improving robustness against prompt overrides without severely hurting utility.
>
> **Audience:** AI Engineers · CISO · Model Developers · **Type:** Research preprint · **Cited in:** [Ch. 10](chapters/10-prompt-injection-and-manipulation.md)

<a id="weidinger-2022-taxonomy"></a>
Weidinger, Laura, Jonathan Uesato, Maribeth Rauh, Conor Griffin, Po-Sen Huang, John Mellor, Amelia Glaese, et al. "Taxonomy of Risks Posed by Language Models." In *Proceedings of the 2022 ACM Conference on Fairness, Accountability, and Transparency (FAccT '22)*. New York: ACM, 2022. https://doi.org/10.1145/3531146.3533088.

> **Annotation:** A foundational DeepMind-led taxonomy of the ethical and social risks of language models. It groups twenty-one risks into six areas: discrimination, hate speech and exclusion; information hazards; misinformation harms; malicious uses; human-computer interaction harms; and environmental and socioeconomic harms. Particularly valuable for the people-centred and societal risks that security-focused frameworks tend to underweight.
>
> **Audience:** Legal / Compliance · CDO · Ethics / Responsible AI · **Type:** Peer-reviewed paper · **Cited in:** [Ch. 1](chapters/01-why-ai-risk-is-different.md)

<a id="willison-2022-prompt-injection"></a>
Willison, Simon. "Prompt Injection Attacks against GPT-3." *Simon Willison's Weblog*, September 12, 2022. https://simonwillison.net/2022/Sep/12/prompt-injection/.

> **Annotation:** The post that coined the term "prompt injection," prompted by users hijacking a GPT-3-powered Twitter bot. It draws the analogy to SQL injection and anticipates why the problem is hard to solve. Short and accessible, it is historically significant for understanding how the field of LLM security began.
>
> **Audience:** CISO · AI Engineers · **Type:** Practitioner essay · **Cited in:** [Ch. 1](chapters/01-why-ai-risk-is-different.md), [Ch. 10](chapters/10-prompt-injection-and-manipulation.md)

<a id="willison-2025-lethal-trifecta"></a>
Willison, Simon. "The Lethal Trifecta for AI Agents: Private Data, Untrusted Content, and External Communication." *Simon Willison's Weblog*, June 16, 2025. https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/.

> **Annotation:** Introduces the "lethal trifecta": an agent that combines access to private data, exposure to untrusted content, and the ability to communicate externally can be manipulated into leaking that data. The recommended mitigation is to remove at least one of the three from any workflow. One of the most practical and easily communicated design heuristics in agent security.
>
> **Audience:** CISO · AI Engineers · CIO · **Type:** Practitioner essay · **Cited in:** [Front Matter](chapters/00-front-matter.md), [Ch. 1](chapters/01-why-ai-risk-is-different.md), [Ch. 9](chapters/09-ai-threat-landscape.md), [Ch. 10](chapters/10-prompt-injection-and-manipulation.md), [Ch. 11](chapters/11-securing-ai-agents.md)

<a id="zanki-2025-nullifai"></a>
Zanki, Karlo. "Malicious ML Models Discovered on Hugging Face Platform." ReversingLabs Blog, February 6, 2025. https://www.reversinglabs.com/blog/rl-identifies-malware-ml-model-hosted-on-hugging-face.

> **Annotation:** Exposes the "nullifAI" campaign distributing malicious PyTorch pickle weights inside non-standard 7z compression archives on Hugging Face to evade Picklescan static inspection and execute reverse-shell payloads.
>
> **Audience:** CISO · MLOps · AppSec · AI Engineers · **Type:** Threat research blog · **Cited in:** [Ch. 12](chapters/12-model-and-supply-chain-security.md)

<a id="zheng-2023-llm-judge"></a>
Zheng, Lianmin, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin, Zhuohan Li, Dacheng Li, Eric P. Xing, Hao Zhang, Joseph E. Gonzalez, and Ion Stoica. "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena." In *Advances in Neural Information Processing Systems 36 (NeurIPS 2023)*, 2023. arXiv:2306.05685. https://doi.org/10.48550/arXiv.2306.05685.

> **Annotation:** Demonstrates that frontier LLM evaluators exceed 80% agreement with human preferences—matching human inter-annotator consistency—while systematically cataloging position bias, verbosity bias, and self-enhancement bias requiring order-swapping, length normalization, and cross-family judge controls.
>
> **Audience:** AI Engineers · Quality Engineering · CRO · Internal Audit · **Type:** Peer-reviewed paper · **Cited in:** [Ch. 24](chapters/24-model-lifecycle-and-change-management.md), [Ch. 26](chapters/26-testing-evaluation-and-red-teaming.md)

<a id="zoom-2023-tos-ai"></a>
Zoom Video Communications. "How Zoom's Terms of Service and Practices Apply to AI Features." Zoom Blog, August 2023. https://news.zoom.us/zoom-terms-of-service-ai/.

> **Annotation:** Details Zoom's response and Section 10 Terms of Service revision following public backlash in August 2023, explicitly prohibiting the use of customer audio, video, or chat content to train AI models without explicit opt-in consent. A canonical case study for tracking SaaS terms changes.
>
> **Audience:** Legal / Compliance · CISO · Procurement · DPO · **Type:** Vendor policy / blog · **Cited in:** [Ch. 6](chapters/06-data-leakage-and-shadow-ai.md), [Ch. 23](chapters/23-vendor-and-third-party-ai-risk.md)

<a id="zou-2025-poisonedrag"></a>
Zou, Wei, Runpeng Geng, Binghui Wang, and Jinyuan Jia. "PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models." In *Proceedings of the 34th USENIX Security Symposium (USENIX Security 25)*, 2025. arXiv:2402.07867. https://doi.org/10.48550/arXiv.2402.07867.

> **Annotation:** Demonstrates that injecting only five jointly optimized adversarial documents into a million-document vector knowledge base forces RAG pipelines to return attacker-chosen answers with roughly 90%+ attack success rates.
>
> **Audience:** CISO · AI Engineers · CDO · Red Teams · **Type:** Peer-reviewed paper · **Cited in:** [Ch. 12](chapters/12-model-and-supply-chain-security.md)

---

## Court and Tribunal Decisions

<a id="arbg-hamburg-2024-chatgpt"></a>
*Arbeitsgericht (ArbG) Hamburg* (Hamburg Labour Court), Decision of January 16, 2024, Case No. 24 BVGa 1/24 (ChatGPT workplace use and works-council co-determination under *Betriebsverfassungsgesetz* §§ 87(1)(1) and 87(1)(6)).

> **Annotation:** Landmark German labor-court ruling holding that voluntary employee browser use of ChatGPT via personal accounts avoided BetrVG co-determination because the employer captured no technical monitoring telemetry—defining the boundary requiring prior works agreements when enterprises roll out logged corporate copilots.
>
> **Audience:** CHRO · European Labor Counsel · CIO · IT Governance · **Type:** Case law (Germany) · **Cited in:** [Ch. 21](chapters/21-sector-specific-requirements.md)

<a id="schrems-ii-2020"></a>
*Data Protection Commissioner v. Facebook Ireland Ltd and Maximillian Schrems* (*Schrems II*), Case C-311/18, ECLI:EU:C:2020:559 (Court of Justice of the European Union, July 16, 2020).

> **Annotation:** Landmark CJEU ruling invalidating the EU-U.S. Privacy Shield and establishing that personal data transferred outside the European Economic Area must receive protection "essentially equivalent" to the GDPR and the EU Charter of Fundamental Rights.
>
> **Audience:** General Counsel · DPO · CIO · **Type:** Case law (European Union) · **Cited in:** [Ch. 8](chapters/08-data-provenance-consent-and-sovereignty.md)

<a id="doe-2024-github"></a>
*Doe 1 v. GitHub, Inc.*, No. 4:22-cv-06823-JST, 2024 WL 235484 (N.D. Cal. January 22, 2024) (and June 2024 order dismissing DMCA § 1202(b) claims while retaining open-source license breach-of-contract claims).

> **Annotation:** Class-action orders by U.S. District Judge Jon S. Tigar holding that although DMCA § 1202(b) CMI claims failed strict copy-identicality (certified for appeal), open-source breach-of-contract claims for omitted copyright/license attribution survive in AI code generation.
>
> **Audience:** CTO / VP Engineering · General Counsel · AppSec · M&A Diligence · **Type:** Case law (United States) · **Cited in:** [Ch. 19](chapters/19-intellectual-property-and-licensing.md), [Ch. 23](chapters/23-vendor-and-third-party-ai-risk.md)

<a id="getty-2025-stability"></a>
*Getty Images (US) Inc & Ors v. Stability AI Ltd*, [2025] EWHC 2863 (Ch) (High Court of Justice of England and Wales, November 4, 2025; permission to appeal secondary copyright granted [2025] EWHC 3343 (Ch)).

> **Annotation:** Landmark UK High Court decision by Mrs Justice Joanna Smith upholding limited trademark infringement (`Trade Marks Act 1994 §§ 10(1), 10(2)`) where early Stable Diffusion outputs generated distorted Getty/iStock watermarks while dismissing secondary copyright infringement over downloaded weights.
>
> **Audience:** CMO · General Counsel · IP Counsel · Product Leaders · **Type:** Case law (United Kingdom) · **Cited in:** [Ch. 19](chapters/19-intellectual-property-and-licensing.md)

<a id="caremark-1996"></a>
*In re Caremark International Inc. Derivative Litigation*, 698 A.2d 959 (Del. Ch. 1996).

> **Annotation:** The foundational Delaware corporate-law decision establishing that directors' fiduciary duty of loyalty includes a good-faith duty to ensure an adequate corporate information and reporting system exists for material risks.
>
> **Audience:** Board · CEO · General Counsel · **Type:** Case law (United States) · **Cited in:** [Ch. 3](chapters/03-board-and-executive-oversight.md)

<a id="openai-2025-preservation"></a>
*In re OpenAI, Inc., Copyright Infringement Litigation*, No. 1:25-md-3143 / 1:23-cv-11195 (S.D.N.Y., Preservation Order of May 13, 2025, Magistrate Judge Ona T. Wang; upheld by District Judge Sidney H. Stein; modified October 9, 2025, ending blanket prospective retention after September 26, 2025 while maintaining segregated historical and flagged logs).

> **Annotation:** Landmark e-Discovery preservation dispute compelling an AI platform provider to halt routine output-log deletion and user-requested purges until subsequent modification ended ongoing blanket retention, illustrating why enterprises require scoped custodian legal-hold overrides across AI logs.
>
> **Audience:** General Counsel · e-Discovery Counsel · DPO · CIO · **Type:** Case law / procedural order (United States) · **Cited in:** [Ch. 22](chapters/22-auditability-assessments-and-evidence.md)

<a id="latombe-2025"></a>
*Latombe v. Commission*, Case T-553/23 (General Court of the European Union, September 3, 2025; appeal pending as Case C-703/25 P).

> **Annotation:** First-instance judgment upholding the EU-U.S. Data Privacy Framework (Implementing Decision (EU) 2023/1795) and validating the Data Protection Review Court's independence under Executive Order 14086. Appealed to the CJEU on October 31, 2025, keeping cross-border AI architecture resilience essential.
>
> **Audience:** General Counsel · DPO · CIO · **Type:** Case law (European Union) · **Cited in:** [Ch. 8](chapters/08-data-provenance-consent-and-sovereignty.md)

<a id="li-2023-liu"></a>
*Li Yunkai v. Liu Yuanchun* (*Li v. Liu*), (2023) Jing 0491 Min Chu No. 11279 (Beijing Internet Court, November 27, 2023).

> **Annotation:** Landmark Chinese AI judgment granting copyright protection to a Stable Diffusion image where iterative prompt crafting and parameter tuning demonstrated human "intellectual investment"—highlighting divergence from U.S. prompt-exclusion rules.
>
> **Audience:** General Counsel · IP Counsel · CMO · Global Product · **Type:** Case law (China) · **Cited in:** [Ch. 19](chapters/19-intellectual-property-and-licensing.md)

<a id="marchand-2019"></a>
*Marchand v. Barnhill*, 212 A.3d 805 (Del. 2019).

> **Annotation:** Delaware Supreme Court decision allowing *Caremark* oversight claims to proceed where a board had no committee, reporting protocol, or regular monitoring for a "mission-critical" risk (food safety at Blue Bell Creameries). Sets the template for board-level oversight of mission-critical AI.
>
> **Audience:** Board · CEO · General Counsel · **Type:** Case law (United States) · **Cited in:** [Ch. 3](chapters/03-board-and-executive-oversight.md)

<a id="mata-2023-avianca"></a>
*Mata v. Avianca, Inc.*, 678 F. Supp. 3d 443 (S.D.N.Y. 2023).

> **Annotation:** A U.S. federal court opinion sanctioning attorneys under Rule 11 for submitting a brief containing fictitious case citations generated by ChatGPT, and for continuing to stand by them after they were questioned. The court emphasizes that using AI is not inherently improper, but that professionals keep a non-delegable duty to verify. Widely cited in professional-conduct guidance on generative AI.
>
> **Audience:** Legal / Compliance · Board · Business Owners · **Type:** Case law (United States) · **Cited in:** [Front Matter](chapters/00-front-matter.md), [Ch. 1](chapters/01-why-ai-risk-is-different.md), [Ch. 5](chapters/05-policies-inventory-and-risk-tiering.md), [Ch. 15](chapters/15-hallucinations-and-reliability.md)

<a id="mobley-2024-workday"></a>
*Mobley v. Workday, Inc.*, 740 F. Supp. 3d 796 (N.D. Cal. July 12, 2024) (motion to dismiss) and No. 23-cv-00770-RFL, 2025 WL 1424347 (N.D. Cal. May 16, 2025) (preliminary ADEA collective certification).

> **Annotation:** Precedent-setting rulings by Judge Rita F. Lin holding that an AI hiring-software vendor delegated screening and rejection functions can face direct liability as an employer's "agent" under federal anti-discrimination statutes (Title VII, ADA, ADEA), followed by preliminary nationwide ADEA collective certification for applicants aged 40+.
>
> **Audience:** General Counsel · CHRO · Procurement · AI Vendors · **Type:** Case law (United States) · **Cited in:** [Ch. 16](chapters/16-bias-fairness-and-discrimination.md)

<a id="moffatt-2024-aircanada"></a>
*Moffatt v. Air Canada*, 2024 BCCRT 149 (British Columbia Civil Resolution Tribunal, February 14, 2024).

> **Annotation:** A small-claims tribunal decision holding Air Canada liable for negligent misrepresentation after its website chatbot misstated the bereavement-fare policy. The tribunal rejected the argument that the chatbot was responsible for its own statements, holding that a company is responsible for all information on its website, whether it comes from a static page or a chatbot. Although it sets no binding precedent outside its jurisdiction, it is the most cited example of corporate liability for AI-generated statements.
>
> **Audience:** Board · Legal / Compliance · Customer Experience · **Type:** Tribunal decision (Canada) · **Cited in:** [Front Matter](chapters/00-front-matter.md), [Ch. 1](chapters/01-why-ai-risk-is-different.md), [Ch. 3](chapters/03-board-and-executive-oversight.md), [Ch. 15](chapters/15-hallucinations-and-reliability.md), [Ch. 27](chapters/27-ai-incident-response.md)

<a id="schufa-2023-c634"></a>
*OQ v. Land Hessen (SCHUFA Holding AG — Scoring)*, Case C-634/21, ECLI:EU:C:2023:957 (Court of Justice of the European Union, First Chamber, December 7, 2023).

> **Annotation:** Landmark CJEU ruling establishing that generating an automated credit score constitutes automated decision-making under GDPR Article 22 when downstream lenders rely heavily upon it rather than performing substantive independent human adjudication.
>
> **Audience:** General Counsel · DPO · Chief Credit Officer · Risk · **Type:** Case law (European Union) · **Cited in:** [Ch. 17](chapters/17-human-oversight-and-automation-bias.md)

<a id="pooja-2026-jkbank"></a>
*Pooja Ramesh Singh v. Jammu and Kashmir Bank Ltd. & Anr.*, 2026 INSC 668 (Supreme Court of India, July 2, 2026).

> **Annotation:** A landmark decision by a Supreme Court of India bench of Justices P. S. Narasimha and Alok Aradhe setting aside orders of the National Company Law Tribunal (NCLT) and National Company Law Appellate Tribunal (NCLAT) in an insolvency dispute after discovering that the tribunal had relied on non-existent, AI-hallucinated precedents. The Court held that a decision tainted by even "an iota of fake or hallucinated material" is "no decision in the eyes of the law," and stressed that human control over adjudication must remain total and in the loop.
>
> **Audience:** Legal / Compliance · Board · Public Sector · **Type:** Case law (India) · **Cited in:** [Front Matter](chapters/00-front-matter.md), [Ch. 1](chapters/01-why-ai-risk-is-different.md), [Ch. 5](chapters/05-policies-inventory-and-risk-tiering.md), [Ch. 15](chapters/15-hallucinations-and-reliability.md)

<a id="thaler-2025-perlmutter"></a>
*Thaler v. Perlmutter*, 130 F.4th 1039 (D.C. Cir. March 18, 2025).

> **Annotation:** Unanimous federal appellate decision holding that the U.S. Copyright Act of 1976 mandates human authorship as an absolute statutory precondition, affirming denial of registration for an autonomously generated artwork.
>
> **Audience:** General Counsel · CMO · Chief Product Officer · IP Counsel · **Type:** Case law (United States) · **Cited in:** [Ch. 19](chapters/19-intellectual-property-and-licensing.md)

<a id="thomson-2025-ross"></a>
*Thomson Reuters Enterprise Centre GmbH v. Ross Intelligence Inc.*, No. 1:20-cv-0613-SB (D. Del. February 11, 2025) (memorandum opinion granting partial summary judgment on copyright infringement and rejecting fair use).

> **Annotation:** Landmark federal copyright opinion by Judge Stephanos Bibas rejecting fair use where copyrighted Westlaw headnotes trained a competing commercial legal AI search tool, sharpening risk for unlicensed fine-tuning corpora.
>
> **Audience:** General Counsel · CTO · Data Stewards · IP Counsel · **Type:** Case law (United States) · **Cited in:** [Ch. 19](chapters/19-intellectual-property-and-licensing.md)

<a id="gadiya-2026-uoi"></a>
*Vijay Ghanshyam Gadiya v. Union of India & Anr.*, 2026 INSC 947, Civil Appeal No. 12155 of 2026 (Supreme Court of India, September 2, 2026).

> **Annotation:** A decision by Justices Dipankar Datta and Sheel Nagu setting aside a ₹425.27-crore customs penalty order and the Gujarat High Court judgment upholding it, after independent verification showed that the customs adjudicator had relied on non-existent case law and fabricated legal ratios produced by AI hallucinations. Remanding the matter to a different officer and leaving disciplinary action open, the Court warned that "AI may well serve as training wheels, but entrusting it with the pilot's seat would be both imprudent and dangerous."
>
> **Audience:** Legal / Compliance · Board · Public Sector · **Type:** Case law (India) · **Cited in:** [Front Matter](chapters/00-front-matter.md), [Ch. 1](chapters/01-why-ai-risk-is-different.md), [Ch. 5](chapters/05-policies-inventory-and-risk-tiering.md), [Ch. 15](chapters/15-hallucinations-and-reliability.md)

---

## Legislation and Regulation

<a id="nyc-2021-ll144"></a>
City of New York. *Local Law 144 of 2021 (Automated Employment Decision Tools)*. N.Y.C. Admin. Code §§ 20-870–20-874, and Department of Consumer and Worker Protection Rules, 6 RCNY §§ 5-300–5-304. Enforced from July 5, 2023. https://www.nyc.gov/site/dca/about/automated-employment-decision-tools.page.

> **Annotation:** Pioneering U.S. municipal hiring-AI law and implementing DCWP rules requiring annual independent intersectional bias audits computing selection/scoring rates and impact ratios across EEO-1 categories, public summary disclosures, and 10-business-day candidate notice.
>
> **Audience:** CHRO · General Counsel · Internal Audit · AI Engineers · **Type:** Municipal statute & rules (United States) · **Cited in:** [Ch. 16](chapters/16-bias-fairness-and-discrimination.md), [Ch. 20](chapters/20-the-global-regulatory-landscape.md), [Ch. 21](chapters/21-sector-specific-requirements.md)

<a id="colorado-2023-reg-10-1-1"></a>
Colorado Division of Insurance. *Regulation 10-1-1: Concerning Quantitative Testing of External Consumer Data and Information Sources, Algorithms, and Predictive Models Used for Life Insurance Underwriting* (*Governance and Risk Management Framework Requirements for Life Insurers*). 3 CCR 702-10, effective November 14, 2023 (implementing C.R.S. § 10-3-1104.9 / SB 21-169). https://doi.colorado.gov/.

> **Annotation:** Flagship state insurance rule operationalizing SB 21-169 by mandating board-overseen governance, external consumer data (`ECDIS`) inventorying, quantitative proxy unfair-discrimination testing, and recurring officer compliance attestations.
>
> **Audience:** Chief Actuarial Officer · Board · Chief Risk Officer · Legal / Compliance · **Type:** State regulation (United States) · **Cited in:** [Ch. 16](chapters/16-bias-fairness-and-discrimination.md)

<a id="china-cac-2025-ai-rules"></a>
Cyberspace Administration of China (CAC) et al. *Interim Measures for the Management of Generative Artificial Intelligence Services* (effective August 15, 2023) and *Measures for Labeling of AI-Generated Synthetic Content* (jointly with MIIT, MPS, and NRTA; effective September 1, 2025, paired with Mandatory National Standard GB 45438-2025).

> **Annotation:** Prescriptive Chinese regulatory rules requiring algorithm registry filings and security assessments for public-facing generative AI carrying public-opinion attributes, alongside dual-layer explicit marks and implicit file-header provenance metadata across synthetic text, audio, image, and video.
>
> **Audience:** General Counsel · CIO · Product Engineering · Regional Leads · **Type:** Ministerial regulations & national standard (China) · **Cited in:** [Ch. 20](chapters/20-the-global-regulatory-landscape.md)

<a id="eeoc-1978-uniform-guidelines"></a>
Equal Employment Opportunity Commission, Civil Service Commission, Department of Labor, and Department of Justice. *Uniform Guidelines on Employee Selection Procedures*. 29 CFR Part 1607 (§ 1607.4). Washington, DC, 1978. https://www.ecfr.gov/current/title-29/subtitle-B/chapter-XIV/part-1607.

> **Annotation:** Foundational federal employment-testing regulation establishing the four-fifths (80 percent) adverse-impact rule of thumb and employer recordkeeping and job-relatedness validation duties.
>
> **Audience:** CHRO · Legal / Compliance · Internal Audit · AI Engineers · **Type:** Federal regulation (United States) · **Cited in:** [Ch. 16](chapters/16-bias-fairness-and-discrimination.md)

<a id="eu-2019-whistleblowing"></a>
European Parliament and Council of the European Union. Directive (EU) 2019/1937 of 23 October 2019 on the Protection of Persons Who Report Breaches of Union Law (*EU Whistleblowing Directive*). *Official Journal of the European Union* L 305, November 26, 2019, pp. 17–56. http://data.europa.eu/eli/dir/2019/1937/oj.

> **Annotation:** Horizontal EU whistleblower-protection directive incorporated into EU AI Act Article 87, compelling secure confidential channels, 7-day acknowledgment, 3-month investigation feedback, and strict legal immunity against employer retaliation.
>
> **Audience:** General Counsel · Chief Ethics Officer · CHRO · Board Audit Committee · **Type:** EU directive · **Cited in:** [Ch. 29](chapters/29-building-a-risk-aware-ai-culture.md)

<a id="eu-2022-csrd"></a>
European Parliament and Council of the European Union. Directive (EU) 2022/2464 of 14 December 2022 Amending Regulation (EU) No 537/2014, Directive 2004/109/EC, Directive 2006/43/EC and Directive 2013/34/EU, as Regards Corporate Sustainability Reporting (*CSRD*, alongside European Sustainability Reporting Standards `ESRS E1` Climate Change). *Official Journal of the European Union* L 322, December 16, 2022. http://data.europa.eu/eli/dir/2022/2464/oj.

> **Annotation:** Binding EU corporate sustainability reporting directive and `ESRS E1` climate disclosure standards compelling limited-assurance Scope 2 (on-premise/colocation electricity) and material upstream Scope 3 (hyperscale cloud/AI compute and hardware embodied carbon) accounting without carbon-offset netting inside gross inventories.
>
> **Audience:** Board · CFO · Chief Sustainability Officer · General Counsel · **Type:** EU directive & standards · **Cited in:** [Ch. 28](chapters/28-metrics-kris-and-reporting.md)

<a id="eu-2022-nis2"></a>
European Parliament and Council of the European Union. Directive (EU) 2022/2555 of 14 December 2022 on Measures for a High Common Level of Cybersecurity Across the Union (*NIS2 Directive*, transposition deadline October 17, 2024) and Directive (EU) 2022/2557 on the Resilience of Critical Entities (*CER Directive*). *Official Journal of the European Union* L 333, December 27, 2022. http://data.europa.eu/eli/dir/2022/2555/oj.

> **Annotation:** Paired EU critical-infrastructure resilience directives enforcing board-accountable cybersecurity risk management, supply-chain vetting, physical continuity, and strict `Article 23` incident reporting clocks (`24-hour` early warning, `72-hour` assessment, `1-month` final report).
>
> **Audience:** CISO · OT Resilience Lead · Board · Legal / Compliance · **Type:** EU directives · **Cited in:** [Ch. 21](chapters/21-sector-specific-requirements.md), [Ch. 25](chapters/25-operational-resilience-and-business-continuity.md), [Ch. 27](chapters/27-ai-incident-response.md)

<a id="eu-2024-platform-work"></a>
European Parliament and Council of the European Union. Directive (EU) 2024/2831 of 23 October 2024 on Improving Working Conditions in Platform Work (algorithmic management transparency, representative consultation, and human review; Member State transposition due December 2, 2026). *Official Journal of the European Union* L, 2024/2831, 2024. http://data.europa.eu/eli/dir/2024/2831/oj.

> **Annotation:** EU labor directive setting strict algorithmic-management rules across Articles 6–10 restricting automated worker monitoring, mandating worker and representative transparency over scoring parameters, and guaranteeing human review and written explanations.
>
> **Audience:** CHRO · European Labor Counsel · Product Engineering · Works Councils · **Type:** EU directive · **Cited in:** [Ch. 21](chapters/21-sector-specific-requirements.md)

<a id="gdpr-2016"></a>
European Parliament and Council of the European Union. Regulation (EU) 2016/679 of 27 April 2016 on the Protection of Natural Persons with Regard to the Processing of Personal Data and on the Free Movement of Such Data (General Data Protection Regulation). *Official Journal of the European Union* L 119, May 4, 2016. http://data.europa.eu/eli/reg/2016/679/oj.

> **Annotation:** The foundational EU data-protection statute governing AI data processing—including purpose limitation (Art. 5(1)(b)), lawful bases (Art. 6), the right to erasure (Art. 17), automated decision-making safeguards (Art. 22), and cross-border transfer restrictions (Chapter V).
>
> **Audience:** Legal / Compliance · DPO · Board · CDO · **Type:** Statute (EU regulation) · **Cited in:** [Ch. 8](chapters/08-data-provenance-consent-and-sovereignty.md), [Ch. 17](chapters/17-human-oversight-and-automation-bias.md), [Ch. 22](chapters/22-auditability-assessments-and-evidence.md), [Ch. 27](chapters/27-ai-incident-response.md)

<a id="eu-2017-mdr"></a>
European Parliament and Council of the European Union. Regulation (EU) 2017/745 of 5 April 2017 on Medical Devices (*MDR*). *Official Journal of the European Union* L 117, May 5, 2017. http://data.europa.eu/eli/reg/2017/745/oj.

> **Annotation:** Core EU medical-device safety and conformity framework placing Notified Body–regulated clinical AI software within EU AI Act Annex I high-risk conformity scope.
>
> **Audience:** Chief Medical Officer · Regulatory Affairs · Quality Assurance · Product · **Type:** Statute (EU regulation) · **Cited in:** [Ch. 21](chapters/21-sector-specific-requirements.md)

<a id="eu-2022-dora"></a>
European Parliament and Council of the European Union. Regulation (EU) 2022/2554 of 14 December 2022 on Digital Operational Resilience for the Financial Sector (*DORA*). *Official Journal of the European Union* L 333, December 27, 2022 (applicable from January 17, 2025). http://data.europa.eu/eli/reg/2022/2554/oj.

> **Annotation:** Comprehensive EU financial operational-resilience statute governing third- and fourth-party AI ICT vendors via mandatory `Article 28` Registers of Information, exit/audit clauses, threat-led penetration testing (`TLPT`), and direct ESA supervision of designated critical providers (`CTPPs`).
>
> **Audience:** CRO · CIO · CISO · Financial Regulatory Affairs · **Type:** Statute (EU regulation) · **Cited in:** [Ch. 21](chapters/21-sector-specific-requirements.md), [Ch. 23](chapters/23-vendor-and-third-party-ai-risk.md), [Ch. 25](chapters/25-operational-resilience-and-business-continuity.md), [Ch. 27](chapters/27-ai-incident-response.md)

<a id="eu-2023-data-act"></a>
European Parliament and Council of the European Union. Regulation (EU) 2023/2854 of 13 December 2023 on Harmonised Rules on Fair Access to and Use of Data (*Data Act*). *Official Journal of the European Union* L, 2023/2854, December 22, 2023 (cloud-switching rights applicable September 12, 2025; Article 29(1) prohibition on switching and egress charges effective January 12, 2027). http://data.europa.eu/eli/reg/2023/2854/oj.

> **Annotation:** Binding EU cloud-portability statute capping customer termination notices at 2 months, mandating 30-day transition assistance (since September 12, 2025), and eliminating all switching and migration egress fees under Article 29(1) beginning January 12, 2027.
>
> **Audience:** CIO · Chief Procurement Officer · General Counsel · Cloud Architects · **Type:** Statute (EU regulation) · **Cited in:** [Ch. 23](chapters/23-vendor-and-third-party-ai-risk.md), [Ch. 25](chapters/25-operational-resilience-and-business-continuity.md)

<a id="eu-2024-ai-act"></a>
European Parliament and Council of the European Union. Regulation (EU) 2024/1689 of the European Parliament and of the Council of 13 June 2024 Laying Down Harmonised Rules on Artificial Intelligence (Artificial Intelligence Act). *Official Journal of the European Union* L, 2024/1689, July 12, 2024. http://data.europa.eu/eli/reg/2024/1689/oj.

> **Annotation:** The world's first comprehensive horizontal AI law. It sorts AI systems by risk (prohibited, high-risk, transparency-obligation, and minimal), imposes obligations on providers and deployers, sets separate rules for general-purpose AI models, and provides penalties of up to €35 million or 7 percent of global turnover for prohibited practices. Article 113 sets the phased application dates. It applies to organizations outside the EU whose AI systems are placed on the EU market or whose outputs are used in the EU.
>
> **Audience:** Legal / Compliance · Board · CIO · CDO · **Type:** Statute (EU regulation) · **Cited in:** [Front Matter](chapters/00-front-matter.md), [Ch. 1](chapters/01-why-ai-risk-is-different.md), [Ch. 2](chapters/02-reference-frameworks-at-a-glance.md), [Ch. 3](chapters/03-board-and-executive-oversight.md), [Ch. 5](chapters/05-policies-inventory-and-risk-tiering.md), [Ch. 8](chapters/08-data-provenance-consent-and-sovereignty.md), [Ch. 11](chapters/11-securing-ai-agents.md), [Ch. 15](chapters/15-hallucinations-and-reliability.md), [Ch. 16](chapters/16-bias-fairness-and-discrimination.md), [Ch. 17](chapters/17-human-oversight-and-automation-bias.md), [Ch. 18](chapters/18-transparency-disclosure-and-content-provenance.md), [Ch. 20](chapters/20-the-global-regulatory-landscape.md), [Ch. 21](chapters/21-sector-specific-requirements.md), [Ch. 22](chapters/22-auditability-assessments-and-evidence.md), [Ch. 24](chapters/24-model-lifecycle-and-change-management.md), [Ch. 26](chapters/26-testing-evaluation-and-red-teaming.md), [Ch. 27](chapters/27-ai-incident-response.md), [Ch. 28](chapters/28-metrics-kris-and-reporting.md), [Ch. 29](chapters/29-building-a-risk-aware-ai-culture.md), [Ch. 30](chapters/30-governance-maturity-model-and-roadmap.md)

<a id="eu-2026-digital-omnibus"></a>
European Parliament and Council of the European Union. Regulation (EU) 2026/1744 Amending Regulation (EU) 2024/1689 (Digital Omnibus on AI). *Official Journal of the European Union*, July 24, 2026.

> **Annotation:** The adopted form of the Digital Omnibus on AI. Among other changes, it defers obligations for stand-alone (Annex III) high-risk AI systems to December 2, 2027, and for high-risk AI embedded in regulated products (Annex I) to August 2, 2028. It leaves the rules on prohibited practices, general-purpose AI models, and Article 50 transparency on their own timelines. Essential for any compliance roadmap built on the original AI Act dates.
>
> **Audience:** Legal / Compliance · Board · CIO · **Type:** Statute (EU amending regulation) · **Cited in:** [Ch. 1](chapters/01-why-ai-risk-is-different.md), [Ch. 18](chapters/18-transparency-disclosure-and-content-provenance.md), [Ch. 20](chapters/20-the-global-regulatory-landscape.md), [Ch. 21](chapters/21-sector-specific-requirements.md), [Ch. 30](chapters/30-governance-maturity-model-and-roadmap.md)

<a id="us-eo-14179"></a>
Executive Office of the President of the United States. Executive Order 14179, *Removing Barriers to American Leadership in Artificial Intelligence*. 90 Fed. Reg. 8741, signed January 23, 2025 (published January 31, 2025).

> **Annotation:** Federal executive order revoking prior AI safety-reporting mandates in favor of an innovation-led AI Action Plan while leaving statutory enforcement by the FTC, EEOC, CFPB, SEC, and prudential bank regulators undisturbed.
>
> **Audience:** General Counsel · Regulatory Affairs · Board · CIO · **Type:** Federal executive order (United States) · **Cited in:** [Ch. 20](chapters/20-the-global-regulatory-landscape.md)

<a id="quebec-2021-law25"></a>
National Assembly of Québec. *Act to Modernize Legislative Provisions as Regards the Protection of Personal Information* (*Law 25*, S.Q. 2021, c. 25, amending CQLR c. P-39.1, § 12.1 on automated decision-making; automated-decision rules effective September 22, 2023).

> **Annotation:** Binding Canadian provincial privacy statute requiring organizations making exclusively automated decisions to notify individuals, disclose used data and principal factors on request, and provide meaningful human reconsideration—backed by administrative penalties up to C\$10 million or 2 percent of global turnover.
>
> **Audience:** General Counsel · DPO · CHRO · Product · **Type:** Provincial statute (Canada) · **Cited in:** [Ch. 20](chapters/20-the-global-regulatory-landscape.md)

<a id="korea-2026-ai-basic-act"></a>
National Assembly of the Republic of Korea. *Framework Act on the Development of Artificial Intelligence and Establishment of Trust* (*AI Basic Act*). Enacted January 2025; effective January 22, 2026.

> **Annotation:** Comprehensive national AI statute establishing South Korea's National AI Committee and AI Safety Research Institute, imposing risk-management and human-oversight obligations on High-Impact AI, requiring generative output labels, and compelling qualifying foreign providers to appoint a local representative.
>
> **Audience:** General Counsel · Regional Leads · CIO · Product · **Type:** National statute (South Korea) · **Cited in:** [Ch. 20](chapters/20-the-global-regulatory-landscape.md)

<a id="japan-2025-ai-act"></a>
National Diet of Japan. *Act on the Promotion of Research and Development and the Utilization of Artificial Intelligence-Related Technologies* (*AI Promotion Act*). Enacted May 28, 2025.

> **Annotation:** Light-touch, innovation-first Japanese statutory framework establishing a Cabinet-level AI Basic Plan and safety coordination without EU-style administrative monetary fines, relying instead on agile soft-law guidance and existing domain laws.
>
> **Audience:** General Counsel · Regional Leads · CIO · **Type:** National statute (Japan) · **Cited in:** [Ch. 20](chapters/20-the-global-regulatory-landscape.md)

<a id="india-2023-dpdp"></a>
Parliament of India and Ministry of Electronics and Information Technology. *The Digital Personal Data Protection Act, 2023* (Act No. 22 of 2023) and *Digital Personal Data Protection Rules, 2025* (notified November 2025).

> **Annotation:** India's comprehensive personal data statute and implementing rules. Section 6 requires free, specific, informed, unconditional consent preceded by standalone notices in English and Eighth Schedule languages (prohibiting bundled consent), while Section 16 permits cross-border transfers by default unless restricted by negative-list notification—subject to stricter sectoral localization laws (RBI, DoT) under Section 16(2).
>
> **Audience:** Legal / Compliance · DPO · CIO · Board · **Type:** Statute and rules (India) · **Cited in:** [Ch. 8](chapters/08-data-provenance-consent-and-sovereignty.md), [Ch. 20](chapters/20-the-global-regulatory-landscape.md)

<a id="uk-1988-cdpa"></a>
Parliament of the United Kingdom. *Copyright, Designs and Patents Act 1988*, c. 48, § 9(3) (computer-generated works).

> **Annotation:** Distinctive UK statutory provision vesting authorship of computer-generated works lacking a human author in "the person by whom the arrangements necessary for the creation of the work are undertaken," illustrating international divergence from U.S. human-authorship exclusions.
>
> **Audience:** General Counsel · IP Counsel · CMO · Global Product · **Type:** Statute (United Kingdom) · **Cited in:** [Ch. 19](chapters/19-intellectual-property-and-licensing.md)

<a id="uk-2025-duaa"></a>
Parliament of the United Kingdom. *Data (Use and Access) Act 2025*, 2025 c. 18 (Royal Assent June 19, 2025; reforming automated decision-making rules under UK GDPR alongside ICO guidance).

> **Annotation:** Post-Brexit UK statutory reform broadening commercial lawful bases (including legitimate interests) for non-special-category automated decision-making while requiring explicit transparency, contestation mechanisms, and meaningful human intervention enforced by the ICO.
>
> **Audience:** General Counsel · DPO · Product · **Type:** National statute (United Kingdom) · **Cited in:** [Ch. 20](chapters/20-the-global-regulatory-landscape.md)

<a id="uk-pra-fca-2021-resilience"></a>
Prudential Regulation Authority (Bank of England) and Financial Conduct Authority. *Supervisory Statement SS1/21: Operational Resilience: Impact Tolerances for Important Business Services* and *Policy Statement PS21/3: Building Operational Resilience*. London: Bank of England / FCA, March 2021 (full compliance effective March 31, 2025). https://www.bankofengland.co.uk/prudential-regulation/publication/2021/march/operational-resilience-impact-tolerances-for-important-business-services-ss.

> **Annotation:** Binding UK financial operational-resilience regime requiring firms to identify Important Business Services (`IBS`) from an outside-in perspective, set board-approved Impact Tolerances, map end-to-end third-party technology dependencies, and demonstrate via severe-but-plausible scenario testing that critical services stay within tolerances since March 31, 2025.
>
> **Audience:** Board · Chief Operating Officer · CRO · Operational Resilience · **Type:** Financial supervisory policy (United Kingdom) · **Cited in:** [Ch. 25](chapters/25-operational-resilience-and-business-continuity.md)

<a id="sebi-2015-lodr"></a>
Securities and Exchange Board of India. Securities and Exchange Board of India (Listing Obligations and Disclosure Requirements) Regulations, 2015. Reg. 21 and sched. II, pt. D, as amended.

> **Annotation:** Requires the top 1,000 listed Indian entities by market capitalization to maintain a board-level Risk Management Committee whose mandate expressly covers cyber security—providing an established governance home for AI risk oversight in Indian listed companies alongside SEBI's annual system-audit expectations.
>
> **Audience:** Board · General Counsel · CRO · **Type:** Regulation (India) · **Cited in:** [Ch. 3](chapters/03-board-and-executive-oversight.md), [Ch. 20](chapters/20-the-global-regulatory-landscape.md), [Ch. 21](chapters/21-sector-specific-requirements.md)

<a id="ca-2026-ai-laws"></a>
State of California. *Generative Artificial Intelligence: Training Data Transparency* (AB 2013, effective January 1, 2026), *California AI Transparency Act* (SB 942, as amended by AB 853, operative August 2, 2026), and California Privacy Protection Agency *CCPA Automated Decisionmaking Technology (ADMT) Regulations* (approved September 22, 2025; effective January 1, 2026, with phased compliance through 2027–2028).

> **Annotation:** Multi-layered California AI governance regime combining mandatory public training-data documentation (`AB 2013`), synthetic provenance watermarks and free public detection tools (`SB 942`/`AB 853`), and CCPA ADMT pre-use notices, opt-out/appeal rights, risk assessments, and cybersecurity audits.
>
> **Audience:** General Counsel · DPO · Product Engineering · CDO · **Type:** State statutes & regulations (United States) · **Cited in:** [Ch. 20](chapters/20-the-global-regulatory-landscape.md), [Ch. 22](chapters/22-auditability-assessments-and-evidence.md)

<a id="ca-2025-sb53"></a>
State of California. *Transparency in Frontier Artificial Intelligence Act (TFAIA)*, Senate Bill 53 (signed September 29, 2025; effective January 1, 2026; frontier safety reporting and employee/contractor whistleblower protections).

> **Annotation:** First U.S. state frontier AI safety statute (`10^26` FLOPs training threshold), requiring covered frontier developers to maintain anonymous internal reporting channels and barring retaliation against employees or contractors flagging catastrophic safety risks or misleading safety statements.
>
> **Audience:** General Counsel · Chief Ethics Officer · AI Safety Leads · CHRO · **Type:** State statute (United States) · **Cited in:** [Ch. 29](chapters/29-building-a-risk-aware-ai-culture.md)

<a id="co-2026-sb189"></a>
State of Colorado. *Consumer Protections for Artificial Intelligence* (SB 24-205, enacted May 2024; delayed by SB 25B-004, August 28, 2025; repealed and replaced by SB 26-189, signed May 14, 2026, establishing an ADMT disclosure-and-rights regime effective January 1, 2027).

> **Annotation:** Landmark example of state AI legislative churn—repealing Colorado's broad `SB 24-205` high-risk AI duty-of-care and impact-assessment mandates prior to enforcement and replacing them via `SB 26-189` with a targeted ADMT disclosure-and-rights statute effective January 1, 2027.
>
> **Audience:** General Counsel · Regulatory Affairs · CRO · Product · **Type:** State statute (United States) · **Cited in:** [Ch. 20](chapters/20-the-global-regulatory-landscape.md)

<a id="il-2026-hb3773"></a>
State of Illinois. *House Bill 3773* (Public Act 103-0804, signed August 9, 2024, amending the Illinois Human Rights Act, 775 ILCS 5/2-101 and 5/2-102(L), to regulate AI in employment and prohibit ZIP codes as protected-class proxies; effective January 1, 2026).

> **Annotation:** Binding Illinois employment statute prohibiting discriminatory AI across hiring, promotion, discipline, and discharge, mandating applicant/worker notice, and expressly outlawing the use of ZIP codes as proxies for protected traits.
>
> **Audience:** CHRO · General Counsel · AI Engineers · People Analytics · **Type:** State statute (United States) · **Cited in:** [Ch. 20](chapters/20-the-global-regulatory-landscape.md), [Ch. 21](chapters/21-sector-specific-requirements.md)

<a id="tx-2026-traiga"></a>
State of Texas. *Texas Responsible Artificial Intelligence Governance Act (TRAIGA)*, House Bill 149 (signed June 22, 2025; effective January 1, 2026).

> **Annotation:** State AI governance framework adopting an intent-based liability standard rather than expansive impact assessments, paired with focused guardrails for healthcare and public-sector AI deployments.
>
> **Audience:** General Counsel · Regulatory Affairs · Product · **Type:** State statute (United States) · **Cited in:** [Ch. 20](chapters/20-the-global-regulatory-landscape.md)

<a id="utah-2024-sb149"></a>
State of Utah. *Artificial Intelligence Policy Act*, Senate Bill 149 (disclosure obligations for generative AI in consumer transactions and regulated occupations; refined via SB 226). Effective May 1, 2024.

> **Annotation:** First enacted U.S. state private-sector generative AI statute, pairing upon-request consumer transaction disclosures with mandatory proactive disclosures whenever AI delivers services in licensed regulated occupations (healthcare, law, mental health) alongside an Office of AI Policy sandbox.
>
> **Audience:** General Counsel · Legal / Compliance · Chief Product Officer · CX Design · **Type:** State statute (United States) · **Cited in:** [Ch. 18](chapters/18-transparency-disclosure-and-content-provenance.md), [Ch. 20](chapters/20-the-global-regulatory-landscape.md)

<a id="us-hipaa-rules"></a>
U.S. Department of Health and Human Services. *Health Insurance Portability and Accountability Act (HIPAA) Privacy and Security Rules*. 45 CFR Parts 160 and 164 (including Business Associate Agreements, §§ 164.502(e) and 164.504(e), and de-identification standards, § 164.514). https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164.

> **Annotation:** Federal healthcare privacy framework prohibiting Protected Health Information (`PHI`) exposure to AI vendors absent executed BAAs and ZDR controls while enforcing Safe Harbor and statistical Expert Determination rules on de-identified clinical training corpora.
>
> **Audience:** Chief Medical Officer · Privacy Officer · CISO · AI Engineers · **Type:** Federal regulations (United States) · **Cited in:** [Ch. 21](chapters/21-sector-specific-requirements.md)

<a id="us-frcp-37e"></a>
U.S. Federal Rules of Civil Procedure. Rules 26(b)(1) (Scope of Discovery), 34 (Producing Electronically Stored Information), and 37(e) (Failure to Preserve Electronically Stored Information). 28 U.S.C. app., as amended. https://www.law.cornell.edu/rules/frcp/rule_37.

> **Annotation:** Core U.S. civil discovery rules establishing discoverability over employee AI prompts, agent execution traces, and AI meeting transcripts as Electronically Stored Information (`ESI`) and authorizing spoliation sanctions when auto-deletion erases ESI after litigation becomes reasonably anticipated.
>
> **Audience:** General Counsel · e-Discovery Counsel · CIO · IT Compliance · **Type:** Federal procedural rules (United States) · **Cited in:** [Ch. 22](chapters/22-auditability-assessments-and-evidence.md), [Ch. 24](chapters/24-model-lifecycle-and-change-management.md), [Ch. 27](chapters/27-ai-incident-response.md)

<a id="sec-2023-cyber-disclosure"></a>
U.S. Securities and Exchange Commission. *Cybersecurity Risk Management, Strategy, Governance, and Incident Disclosure*. Final Rule, Release No. 33-11216 (17 CFR Parts 229, 232, 239, 240, and 249; Form 8-K Item 1.05). Washington, DC: SEC, July 26, 2023. https://www.sec.gov/files/rules/final/2023/33-11216.pdf.

> **Annotation:** Binding U.S. public-company disclosure rule requiring Form 8-K Item 1.05 filing within four business days of determining that a cybersecurity incident—including material compromises of AI systems, customer prompt stores, or third-party AI vendors—is material.
>
> **Audience:** General Counsel · CFO · CISO · Board Audit Committee · **Type:** Federal regulation (United States) · **Cited in:** [Ch. 27](chapters/27-ai-incident-response.md)

<a id="sec-rule-21f-17"></a>
U.S. Securities and Exchange Commission. *Staff Communications with Whistleblowers*, 17 CFR § 240.21F-17 (Rule 21F-17 under the Securities Exchange Act of 1934, prohibiting impediment of direct whistleblower reporting via NDAs, severance agreements, or corporate policies). https://www.ecfr.gov/current/title-17/chapter-II/part-240/section-240.21F-17.

> **Annotation:** Binding U.S. securities whistleblower rule aggressively enforced against restrictive NDAs, severance releases, contractor clauses, or internal monitoring practices that chill or impede direct communication with SEC staff regarding corporate or AI compliance violations.
>
> **Audience:** General Counsel · Chief Ethics Officer · CHRO · Board Audit Committee · **Type:** Federal regulation (United States) · **Cited in:** [Ch. 29](chapters/29-building-a-risk-aware-ai-culture.md)
