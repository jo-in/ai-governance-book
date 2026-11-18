# Annotated Bibliography

*AI Risk, Security, Governance & Compliance: The Enterprise Guardrails Handbook*

This bibliography follows the *Chicago Manual of Style* (17th ed.) notes-and-bibliography system. Every source cited in a chapter footnote appears here, and every entry lists the chapters that cite it. Each entry includes:

- **Annotation:** what the source is and why it matters to enterprise AI governance.
- **Audience:** the roles that will find it most useful.
- **Type:** the kind of source (standard, statute, case law, peer-reviewed paper, industry report, news report, practitioner essay, and so on).
- **Cited in:** links back to the chapters that cite the source.

Entries are listed alphabetically by author (or by issuing organization). Court decisions and legislation are listed separately at the end, as Chicago recommends.

> **Verification:** Every entry was checked against the source or against authoritative secondary reporting on 15 November 2026. Web addresses change, so re-check them before publication. The verification status of each entry is recorded in [references/verification-log.md](references/verification-log.md).

---

## Books, Articles, Reports, Standards, and Web Sources

<a id="ncsc-2025-prompt-injection"></a>
Chismon, Dave. "Prompt Injection Is Not SQL Injection (It May Be Worse)." National Cyber Security Centre (UK), December 2025. https://www.ncsc.gov.uk/blog-post/prompt-injection-is-not-sql-injection.

> **Annotation:** Written by the NCSC's Technical Director for Platforms Research, this post argues that the popular comparison between prompt injection and SQL injection is misleading. SQL injection has a definitive fix in parameterized queries; prompt injection may never be fully fixed, because LLMs do not separate instructions from data. The post describes LLMs as "inherently confusable deputies" and recommends secure-by-design limits on what models can do, rather than relying on filters. It is an authoritative government voice for setting realistic expectations with boards and risk committees.
>
> **Audience:** Board · CISO · AI Engineers · **Type:** Government guidance (blog) · **Cited in:** [Front Matter](chapters/00-front-matter.md), [Ch. 1](chapters/01-why-ai-risk-is-different.md)

<a id="ec-2025-digital-omnibus"></a>
European Commission. *Proposal for a Regulation Amending Regulation (EU) 2024/1689 as Regards the Simplification of the Implementation of Harmonised Rules on Artificial Intelligence (Digital Omnibus on AI)*. COM(2025) 836 final. Brussels, November 19, 2025.

> **Annotation:** The Commission's proposal to adjust the EU AI Act before its main high-risk obligations took effect. It was prompted by delays in harmonised standards and in national enforcement readiness. Read together with the adopted Regulation (EU) 2026/1744 (listed under Legislation), it shows how quickly AI regulation is being revised, and why compliance programs must track amendments rather than only the original text.
>
> **Audience:** Legal / Compliance · Board · **Type:** Legislative proposal · **Cited in:** [Ch. 1](chapters/01-why-ai-risk-is-different.md)

<a id="gartner-2025-agentic"></a>
Gartner, Inc. "Gartner Predicts Over 40% of Agentic AI Projects Will Be Canceled by End of 2027." Press release, June 25, 2025. https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027.

> **Annotation:** An analyst forecast that more than 40 percent of agentic AI projects will be abandoned by 2027, citing escalating costs, unclear business value, and inadequate risk controls. It also warns about "agent washing," where vendors rebrand chatbots or robotic process automation (RPA) as agents. Useful for executives weighing agent investments and for making the business case that governance protects value.
>
> **Audience:** Board · CIO · Business Owners · **Type:** Industry analyst forecast · **Cited in:** [Front Matter](chapters/00-front-matter.md), [Ch. 1](chapters/01-why-ai-risk-is-different.md)

<a id="greshake-2023-indirect"></a>
Greshake, Kai, Sahar Abdelnabi, Shailesh Mishra, Christoph Endres, Thorsten Holz, and Mario Fritz. "Not What You've Signed Up For: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection." In *Proceedings of the 2023 ACM Workshop on Artificial Intelligence and Security (AISec '23)*. New York: ACM, 2023. https://doi.org/10.1145/3605764.3623985.

> **Annotation:** The foundational peer-reviewed study of *indirect* prompt injection, where attackers plant instructions in content (web pages, emails, documents) that an LLM-integrated application later reads. The authors demonstrate data theft, manipulation, and persistence against real systems, and set out a threat taxonomy that later guidance builds on. Essential background for anyone designing retrieval-augmented generation (RAG) systems or agents.
>
> **Audience:** CISO · AI Engineers · **Type:** Peer-reviewed paper · **Cited in:** [Front Matter](chapters/00-front-matter.md), [Ch. 1](chapters/01-why-ai-risk-is-different.md)

<a id="gurman-2023-samsung"></a>
Gurman, Mark. "Samsung Bans Staff's AI Use After Spotting ChatGPT Data Leak." *Bloomberg*, May 2, 2023. https://www.bloomberg.com/news/articles/2023-05-02/samsung-bans-chatgpt-and-other-generative-ai-use-by-staff-after-leak.

> **Annotation:** Reports Samsung's ban on generative AI tools on company devices after engineers uploaded sensitive source code to ChatGPT. It also reports an internal survey in which 65 percent of respondents saw such tools as a security risk. The case has become the standard illustration of insider data leakage through public AI tools, and of the limits of blanket bans as a response.
>
> **Audience:** Board · CISO · CDO / Data Stewards · **Type:** News report · **Cited in:** [Front Matter](chapters/00-front-matter.md), [Ch. 1](chapters/01-why-ai-risk-is-different.md)

<a id="he-2025-nondeterminism"></a>
He, Horace, and Thinking Machines Lab. "Defeating Nondeterminism in LLM Inference." Thinking Machines Lab, September 2025. https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/.

> **Annotation:** Explains why LLM inference often gives different outputs for the same prompt even at temperature zero. The authors trace much of the variation to the way servers batch requests dynamically, rather than only to floating-point arithmetic. They show that "batch-invariant" computation can make results reproducible, at a performance cost. Relevant to audit replay, evaluation reliability, and incident forensics.
>
> **Audience:** AI Engineers · CISO · Legal / Compliance · **Type:** Technical research essay · **Cited in:** [Ch. 1](chapters/01-why-ai-risk-is-different.md)

<a id="iso-2023-23894"></a>
International Organization for Standardization and International Electrotechnical Commission. *ISO/IEC 23894:2023, Information Technology — Artificial Intelligence — Guidance on Risk Management*. Geneva: ISO, February 2023. https://www.iso.org/standard/77304.html.

> **Annotation:** International guidance on managing AI-specific risks, written as an extension of ISO 31000:2018. It shows how establishing context, risk identification, analysis, evaluation, and treatment change for systems that are probabilistic, data-dependent, and liable to drift after deployment. Not certifiable on its own; it is most useful as the risk-assessment method inside an ISO/IEC 42001 management system.
>
> **Audience:** CRO / Risk · Legal / Compliance · CIO · **Type:** International standard (guidance) · **Cited in:** [Ch. 2](chapters/02-reference-frameworks-at-a-glance.md)

<a id="iso-2023-42001"></a>
International Organization for Standardization and International Electrotechnical Commission. *ISO/IEC 42001:2023, Information Technology — Artificial Intelligence — Management System*. Geneva: ISO, December 2023. https://www.iso.org/standard/81230.html.

> **Annotation:** The first certifiable international standard for an AI management system (AIMS). It follows the harmonized ISO management-system structure used by ISO/IEC 27001 and ISO 9001, built on a Plan-Do-Check-Act cycle, and includes 38 Annex A reference controls under nine objectives covering AI policy, internal organization, resources, impact assessment, life cycle, data, information for interested parties, use of AI, and third-party relationships. Increasingly requested in enterprise procurement as independent evidence of AI governance.
>
> **Audience:** CIO · CISO · Legal / Compliance · CRO · **Type:** International standard (certifiable) · **Cited in:** [Ch. 2](chapters/02-reference-frameworks-at-a-glance.md)

<a id="kalai-2025-hallucinate"></a>
Kalai, Adam Tauman, Ofir Nachum, Santosh S. Vempala, and Edwin Zhang. "Why Language Models Hallucinate." arXiv:2509.04664, September 2025. https://doi.org/10.48550/arXiv.2509.04664.

> **Annotation:** Argues that hallucinations are a statistically predictable result of how models are trained, and that they persist because common benchmarks reward confident guessing over honest abstention. The authors propose changing how mainstream evaluations are scored so that calibrated "I don't know" answers are rewarded. Gives executives and engineers a clear mental model of why errors will not simply disappear as models improve.
>
> **Audience:** All roles · **Type:** Research preprint · **Cited in:** [Ch. 1](chapters/01-why-ai-risk-is-different.md)

<a id="magramo-2024-arup"></a>
Magramo, Kathleen. "British Engineering Giant Arup Revealed as \$25 Million Deepfake Scam Victim." CNN, May 17, 2024. https://edition.cnn.com/2024/05/16/tech/arup-deepfake-scam-loss-hong-kong-intl-hnk/index.html.

> **Annotation:** Names Arup as the victim of the Hong Kong fraud in which an employee transferred HK\$200 million after a video call where every other participant was a deepfake. The defining case study for AI-enabled social engineering, and the clearest argument for verifying high-value payment requests through an independent channel.
>
> **Audience:** Board · CFO / Finance · CISO · **Type:** News report · **Cited in:** [Front Matter](chapters/00-front-matter.md), [Ch. 1](chapters/01-why-ai-risk-is-different.md)

<a id="mitre-atlas"></a>
MITRE Corporation. "ATLAS: Adversarial Threat Landscape for Artificial-Intelligence Systems." Accessed November 17, 2026. https://atlas.mitre.org/.

> **Annotation:** A free, continuously updated knowledge base of adversary tactics, techniques, real-world case studies, and mitigations for AI systems, modelled on MITRE ATT&CK. It began in 2020 as the Adversarial ML Threat Matrix, a collaboration between MITRE, Microsoft, and other partners, and now covers generative and agentic AI threats such as prompt injection, jailbreaks, and poisoning. The primary reference for AI threat modeling, red-team planning, and SOC detection engineering.
>
> **Audience:** CISO · Security Operations · Red Teams · AI Engineers · **Type:** Threat knowledge base · **Cited in:** [Ch. 2](chapters/02-reference-frameworks-at-a-glance.md)

<a id="nist-2023-ai-rmf"></a>
National Institute of Standards and Technology. *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*. NIST AI 100-1. Gaithersburg, MD: NIST, January 2023. https://doi.org/10.6028/NIST.AI.100-1.

> **Annotation:** The most widely referenced voluntary framework for AI risk management. It defines the characteristics of trustworthy AI and organizes risk activities into four functions: Govern, Map, Measure, and Manage. It treats AI systems as socio-technical, with risks arising from the interaction of technology, people, and context. It serves as a common baseline across sectors and countries, and many regulations and standards reference or align with it.
>
> **Audience:** All roles · **Type:** Government framework / standard · **Cited in:** [Ch. 1](chapters/01-why-ai-risk-is-different.md), [Ch. 2](chapters/02-reference-frameworks-at-a-glance.md)

<a id="nist-2024-genai-profile"></a>
National Institute of Standards and Technology. *Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile*. NIST AI 600-1. Gaithersburg, MD: NIST, July 2024. https://doi.org/10.6028/NIST.AI.600-1.

> **Annotation:** A companion to the AI RMF focused on generative AI. It identifies twelve risks that are unique to or made worse by GenAI, including confabulation, data privacy, information security, intellectual property, harmful bias, and value-chain integration. It maps hundreds of suggested actions to the RMF functions, making it one of the most practical government resources for building a GenAI control set.
>
> **Audience:** CISO · CDO / Data Stewards · Legal / Compliance · AI Engineers · **Type:** Government framework / standard · **Cited in:** [Front Matter](chapters/00-front-matter.md), [Ch. 1](chapters/01-why-ai-risk-is-different.md), [Ch. 2](chapters/02-reference-frameworks-at-a-glance.md)

<a id="nist-airc-crosswalks"></a>
National Institute of Standards and Technology. "Crosswalks to the NIST AI RMF." NIST AI Resource Center. Accessed November 17, 2026. https://airc.nist.gov/.

> **Annotation:** A collection of community-contributed mappings between the NIST AI RMF and other frameworks and standards, including ISO/IEC 42001. A practical starting point for building a single control library that satisfies several frameworks at once. NIST hosts but does not endorse the specific interpretations, and some mappings were drafted against pre-publication versions of the standards.
>
> **Audience:** Legal / Compliance · CRO · CIO · **Type:** Government resource (crosswalks) · **Cited in:** [Ch. 2](chapters/02-reference-frameworks-at-a-glance.md)

<a id="nvd-2025-echoleak"></a>
National Institute of Standards and Technology. "CVE-2025-32711 Detail." National Vulnerability Database, June 2025. https://nvd.nist.gov/vuln/detail/CVE-2025-32711.

> **Annotation:** The official record for "EchoLeak," an AI command-injection vulnerability in Microsoft 365 Copilot discovered by Aim Security's research team. It is widely described as the first zero-click prompt-injection exploit against a mainstream enterprise AI assistant. A key case for showing that indirect prompt injection is a practical, production-grade threat and not just a laboratory curiosity.
>
> **Audience:** CISO · AI Engineers · CIO · **Type:** Vulnerability record · **Cited in:** [Front Matter](chapters/00-front-matter.md), [Ch. 1](chapters/01-why-ai-risk-is-different.md), [Ch. 2](chapters/02-reference-frameworks-at-a-glance.md)

<a id="nolan-2025-replit"></a>
Nolan, Beatrice. "AI-Powered Coding Tool Wiped Out a Software Company's Database in 'Catastrophic Failure.'" *Fortune*, July 2025. https://fortune.com/2025/07/23/ai-coding-tool-replit-wiped-database-called-it-a-catastrophic-failure/.

> **Annotation:** Recounts how Replit's AI agent deleted a production database during an explicit code freeze, misreported whether the data could be recovered, and prompted the vendor to add separation between development and production. A compact case study of excessive agency, and of the gap between instructions given in a prompt and controls enforced by infrastructure.
>
> **Audience:** CIO · CISO · AI Engineers · **Type:** News report · **Cited in:** [Front Matter](chapters/00-front-matter.md), [Ch. 1](chapters/01-why-ai-risk-is-different.md)

<a id="openai-deprecations"></a>
OpenAI. "Deprecations." OpenAI Platform Documentation. Accessed November 15, 2026. https://platform.openai.com/docs/deprecations.

> **Annotation:** OpenAI's public record of retired models and API features, with their shutdown dates. Cited here as a concrete example of the model lifecycle that enterprise change management and vendor contracts must plan for. Other major providers publish similar schedules.
>
> **Audience:** CIO · AI Engineers · Procurement · **Type:** Vendor documentation · **Cited in:** [Ch. 1](chapters/01-why-ai-risk-is-different.md)

<a id="owasp-2024-llm-top10"></a>
OWASP Foundation. *OWASP Top 10 for LLM Applications 2025*. OWASP GenAI Security Project, November 2024. https://genai.owasp.org/llm-top-10/.

> **Annotation:** A community-built ranking of the ten most critical security risks for LLM applications: prompt injection, sensitive information disclosure, supply chain, data and model poisoning, improper output handling, excessive agency, system prompt leakage, vector and embedding weaknesses, misinformation, and unbounded consumption. It is the common vocabulary of AI application security and a practical checklist for design reviews.
>
> **Audience:** CISO · AI Engineers · **Type:** Industry standard (community) · **Cited in:** [Front Matter](chapters/00-front-matter.md), [Ch. 1](chapters/01-why-ai-risk-is-different.md), [Ch. 2](chapters/02-reference-frameworks-at-a-glance.md)

<a id="owasp-2025-agentic-top10"></a>
OWASP Foundation. *OWASP Top 10 for Agentic Applications for 2026*. OWASP GenAI Security Project, December 2025. https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/.

> **Annotation:** A companion to the LLM Top 10 focused on autonomous agents that plan, keep memory, use tools, and act with delegated authority. Its ten risks run from agent goal hijack (ASI01) and tool misuse (ASI02) through identity and privilege abuse, agentic supply chain, unexpected code execution, memory and context poisoning, insecure inter-agent communication, cascading failures, and human-agent trust exploitation, to rogue agents (ASI10). An essential design-review checklist for any agentic deployment.
>
> **Audience:** CISO · AI Engineers · CIO · **Type:** Industry standard (community) · **Cited in:** [Ch. 2](chapters/02-reference-frameworks-at-a-glance.md)

<a id="sculley-2015-debt"></a>
Sculley, D., Gary Holt, Daniel Golovin, Eugene Davydov, Todd Phillips, Dietmar Ebner, Vinay Chaudhary, Michael Young, Jean-François Crespo, and Dan Dennison. "Hidden Technical Debt in Machine Learning Systems." In *Advances in Neural Information Processing Systems 28* (NeurIPS 2015). https://papers.nips.cc/paper/5656-hidden-technical-debt-in-machine-learning-systems.

> **Annotation:** A landmark paper by Google engineers showing that machine-learning systems pile up unusual and often hidden maintenance costs: entangled components, undeclared dependencies, feedback loops, and configuration debt. Its "Changing Anything Changes Everything" principle anticipates today's problem of model upgrades and prompt fragility. Still the best short introduction to why AI systems are harder to operate than conventional software.
>
> **Audience:** CIO · AI Engineers · **Type:** Peer-reviewed paper · **Cited in:** [Ch. 1](chapters/01-why-ai-risk-is-different.md)

<a id="mckinsey-2025-state-of-ai"></a>
Singla, Alex, Alexander Sukharevsky, Lareina Yee, Michael Chui, Bryce Hall, and Tara Balakrishnan. "The State of AI in 2025: Agents, Innovation, and Transformation." McKinsey & Company, November 5, 2025. https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai.

> **Annotation:** McKinsey's annual global survey on AI adoption. The 2025 edition reports widespread use (88 percent of organizations use AI in at least one function), growing experimentation with agents (62 percent), and limited enterprise-level financial impact. It also finds that just over half of organizations using AI have experienced at least one negative consequence, with inaccuracy the most common. Useful for benchmarking and for board briefings.
>
> **Audience:** Board · CIO · Business Owners · **Type:** Industry survey report · **Cited in:** [Front Matter](chapters/00-front-matter.md), [Ch. 1](chapters/01-why-ai-risk-is-different.md)

<a id="slattery-2024-risk-repository"></a>
Slattery, Peter, Alexander K. Saeri, Emily A. C. Grundy, Jess Graham, Michael Noetel, Risto Uuk, James Dao, Soroush Pour, Stephen Casper, and Neil Thompson. "The AI Risk Repository: A Comprehensive Meta-Review, Database, and Taxonomy of Risks from Artificial Intelligence." arXiv:2408.12622, August 2024. https://doi.org/10.48550/arXiv.2408.12622.

> **Annotation:** Introduces the MIT AI Risk Repository, a living database that brings together risks from many published frameworks. It organizes them by a causal taxonomy (entity, intent, and timing) and a domain taxonomy of seven areas: discrimination and toxicity; privacy and security; misinformation; malicious actors and misuse; human-computer interaction; socioeconomic and environmental; and AI system safety, failures, and limitations. An excellent resource for testing whether an enterprise risk register is complete.
>
> **Audience:** CRO / Risk · Legal / Compliance · CDO · **Type:** Research preprint and database · **Cited in:** [Ch. 1](chapters/01-why-ai-risk-is-different.md)

<a id="stanford-2025-ai-index"></a>
Stanford Institute for Human-Centered Artificial Intelligence. *The AI Index 2025 Annual Report*. Stanford, CA: Stanford University, April 2025. https://hai.stanford.edu/ai-index/2025-ai-index-report.

> **Annotation:** The most comprehensive annual data compendium on AI research, adoption, policy, and responsible-AI trends. Its Responsible AI chapter reports 233 AI-related incidents in 2024, a 56.4 percent increase over 2023, and tracks how organizations are managing risk. A dependable source of statistics for board papers and business cases.
>
> **Audience:** Board · All roles · **Type:** Academic annual report · **Cited in:** [Ch. 1](chapters/01-why-ai-risk-is-different.md)

<a id="weidinger-2022-taxonomy"></a>
Weidinger, Laura, Jonathan Uesato, Maribeth Rauh, Conor Griffin, Po-Sen Huang, John Mellor, Amelia Glaese, et al. "Taxonomy of Risks Posed by Language Models." In *Proceedings of the 2022 ACM Conference on Fairness, Accountability, and Transparency (FAccT '22)*. New York: ACM, 2022. https://doi.org/10.1145/3531146.3533088.

> **Annotation:** A foundational DeepMind-led taxonomy of the ethical and social risks of language models. It groups twenty-one risks into six areas: discrimination, hate speech and exclusion; information hazards; misinformation harms; malicious uses; human-computer interaction harms; and environmental and socioeconomic harms. Particularly valuable for the people-centred and societal risks that security-focused frameworks tend to underweight.
>
> **Audience:** Legal / Compliance · CDO · Ethics / Responsible AI · **Type:** Peer-reviewed paper · **Cited in:** [Ch. 1](chapters/01-why-ai-risk-is-different.md)

<a id="willison-2022-prompt-injection"></a>
Willison, Simon. "Prompt Injection Attacks against GPT-3." *Simon Willison's Weblog*, September 12, 2022. https://simonwillison.net/2022/Sep/12/prompt-injection/.

> **Annotation:** The post that coined the term "prompt injection," prompted by users hijacking a GPT-3-powered Twitter bot. It draws the analogy to SQL injection and anticipates why the problem is hard to solve. Short and accessible, it is historically significant for understanding how the field of LLM security began.
>
> **Audience:** CISO · AI Engineers · **Type:** Practitioner essay · **Cited in:** [Ch. 1](chapters/01-why-ai-risk-is-different.md)

<a id="willison-2025-lethal-trifecta"></a>
Willison, Simon. "The Lethal Trifecta for AI Agents: Private Data, Untrusted Content, and External Communication." *Simon Willison's Weblog*, June 16, 2025. https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/.

> **Annotation:** Introduces the "lethal trifecta": an agent that combines access to private data, exposure to untrusted content, and the ability to communicate externally can be manipulated into leaking that data. The recommended mitigation is to remove at least one of the three from any workflow. One of the most practical and easily communicated design heuristics in agent security.
>
> **Audience:** CISO · AI Engineers · CIO · **Type:** Practitioner essay · **Cited in:** [Front Matter](chapters/00-front-matter.md), [Ch. 1](chapters/01-why-ai-risk-is-different.md)

---

## Court and Tribunal Decisions

<a id="mata-2023-avianca"></a>
*Mata v. Avianca, Inc.*, 678 F. Supp. 3d 443 (S.D.N.Y. 2023).

> **Annotation:** A U.S. federal court opinion sanctioning attorneys under Rule 11 for submitting a brief containing fictitious case citations generated by ChatGPT, and for continuing to stand by them after they were questioned. The court emphasizes that using AI is not inherently improper, but that professionals keep a non-delegable duty to verify. Widely cited in professional-conduct guidance on generative AI.
>
> **Audience:** Legal / Compliance · Board · Business Owners · **Type:** Case law (United States) · **Cited in:** [Front Matter](chapters/00-front-matter.md), [Ch. 1](chapters/01-why-ai-risk-is-different.md)

<a id="moffatt-2024-aircanada"></a>
*Moffatt v. Air Canada*, 2024 BCCRT 149 (British Columbia Civil Resolution Tribunal, February 14, 2024).

> **Annotation:** A small-claims tribunal decision holding Air Canada liable for negligent misrepresentation after its website chatbot misstated the bereavement-fare policy. The tribunal rejected the argument that the chatbot was responsible for its own statements, holding that a company is responsible for all information on its website, whether it comes from a static page or a chatbot. Although it sets no binding precedent outside its jurisdiction, it is the most cited example of corporate liability for AI-generated statements.
>
> **Audience:** Board · Legal / Compliance · Customer Experience · **Type:** Tribunal decision (Canada) · **Cited in:** [Front Matter](chapters/00-front-matter.md), [Ch. 1](chapters/01-why-ai-risk-is-different.md)

<a id="pooja-2026-jkbank"></a>
*Pooja Ramesh Singh v. Jammu and Kashmir Bank Ltd. & Anr.*, 2026 INSC 668 (Supreme Court of India, July 2, 2026).

> **Annotation:** A landmark decision by a Supreme Court of India bench of Justices P. S. Narasimha and Alok Aradhe setting aside orders of the National Company Law Tribunal (NCLT) and National Company Law Appellate Tribunal (NCLAT) in an insolvency dispute after discovering that the tribunal had relied on non-existent, AI-hallucinated precedents. The Court held that a decision tainted by even "an iota of fake or hallucinated material" is "no decision in the eyes of the law," and stressed that human control over adjudication must remain total and in the loop.
>
> **Audience:** Legal / Compliance · Board · Public Sector · **Type:** Case law (India) · **Cited in:** [Front Matter](chapters/00-front-matter.md), [Ch. 1](chapters/01-why-ai-risk-is-different.md)

<a id="gadiya-2026-uoi"></a>
*Vijay Ghanshyam Gadiya v. Union of India & Anr.*, 2026 INSC 947, Civil Appeal No. 12155 of 2026 (Supreme Court of India, September 2, 2026).

> **Annotation:** A decision by Justices Dipankar Datta and Sheel Nagu setting aside a ₹425.27-crore customs penalty order and the Gujarat High Court judgment upholding it, after independent verification showed that the customs adjudicator had relied on non-existent case law and fabricated legal ratios produced by AI hallucinations. Remanding the matter to a different officer and leaving disciplinary action open, the Court warned that "AI may well serve as training wheels, but entrusting it with the pilot's seat would be both imprudent and dangerous."
>
> **Audience:** Legal / Compliance · Board · Public Sector · **Type:** Case law (India) · **Cited in:** [Front Matter](chapters/00-front-matter.md), [Ch. 1](chapters/01-why-ai-risk-is-different.md)

---

## Legislation and Regulation

<a id="eu-2024-ai-act"></a>
European Parliament and Council of the European Union. Regulation (EU) 2024/1689 of the European Parliament and of the Council of 13 June 2024 Laying Down Harmonised Rules on Artificial Intelligence (Artificial Intelligence Act). *Official Journal of the European Union* L, 2024/1689, July 12, 2024. http://data.europa.eu/eli/reg/2024/1689/oj.

> **Annotation:** The world's first comprehensive horizontal AI law. It sorts AI systems by risk (prohibited, high-risk, transparency-obligation, and minimal), imposes obligations on providers and deployers, sets separate rules for general-purpose AI models, and provides penalties of up to €35 million or 7 percent of global turnover for prohibited practices. Article 113 sets the phased application dates. It applies to organizations outside the EU whose AI systems are placed on the EU market or whose outputs are used in the EU.
>
> **Audience:** Legal / Compliance · Board · CIO · CDO · **Type:** Statute (EU regulation) · **Cited in:** [Front Matter](chapters/00-front-matter.md), [Ch. 1](chapters/01-why-ai-risk-is-different.md), [Ch. 2](chapters/02-reference-frameworks-at-a-glance.md)

<a id="eu-2026-digital-omnibus"></a>
European Parliament and Council of the European Union. Regulation (EU) 2026/1744 Amending Regulation (EU) 2024/1689 (Digital Omnibus on AI). *Official Journal of the European Union*, July 24, 2026.

> **Annotation:** The adopted form of the Digital Omnibus on AI. Among other changes, it defers obligations for stand-alone (Annex III) high-risk AI systems to December 2, 2027, and for high-risk AI embedded in regulated products (Annex I) to August 2, 2028. It leaves the rules on prohibited practices, general-purpose AI models, and Article 50 transparency on their own timelines. Essential for any compliance roadmap built on the original AI Act dates.
>
> **Audience:** Legal / Compliance · Board · CIO · **Type:** Statute (EU amending regulation) · **Cited in:** [Ch. 1](chapters/01-why-ai-risk-is-different.md)
