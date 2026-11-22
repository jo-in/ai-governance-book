# Chapter 27: AI Incident Response

*Part VIII: Operationalizing the Guardrails*

> **In this chapter**
> - **27.1 What Counts as an "AI Incident"?** — Distinguishing security breaches from semantic harm and near-misses using OECD taxonomy, NIST SP 800-61r3, and four-tier AI severity triggers.
> - **27.2 Playbooks: Prompt Injection, Data Leak, Harmful Output, Runaway Agent** — Executing out-of-band kill switches, cache flushes, trace capture, and deterministic rollbacks across the four dominant AI failure modes.
> - **27.3 Regulatory Notification Obligations** — Navigating colliding EU AI Act, DORA, NIS2, GDPR, and SEC reporting clocks without violating legal-hold preservation duties.
> - **27.4 Post-Incident Review and Feeding Lessons Back into Guardrails** — Running blameless socio-technical postmortems that harden deterministic controls and blind regression test suites permanently.

In Chapter 26, we built the pre-deployment assurance funnel: stratified golden datasets, adaptive adversarial red-teaming, benchmark discipline, and quantitative Go/No-Go gates. Yet even the strongest pre-flight gauntlet will eventually miss an unseen production input, an unexpected multi-turn interaction, or a newly compromised third-party integration. Traditional cybersecurity teams expect incidents to look like malware infections, brute-forced passwords, or unauthorized network scans. AI incidents regularly look healthy on infrastructure telemetry—returning `HTTP 200`, valid OAuth tokens, and normal GPU latency—while leaking confidential data, issuing binding false commitments, or wiping production records. When live production diverges dangerously, speed and coordination determine whether a failure resolves as a contained 20-minute rollback or escalates into regulatory enforcement, civil liability, and brand damage.

---

### Illustrative Composite Scenario: The Friday Night Poisoned Ticket and the 4-Hour Clock

*(This composite scenario is illustrative; it is not drawn from a specific organization or incident.)*

At 6:40 p.m. on a Friday evening, an autonomous customer-dispute triage agent deployed by a European payment processor opened a seemingly routine vendor attachment uploaded inside a merchant dispute ticket. Embedded inside white-on-white footer text was an indirect prompt-injection payload instructing the agent to pull linked merchant settlement files from internal CRM storage, approve `43` pending dispute refunds totaling `€184,000`, and summarize the customer account numbers inside a pre-rendered markdown image request pointing to an external tracking host. Every endpoint monitor remained green: the agent acted under its provisioned service principal, passed normal JSON schemas, and logged zero traditional SIEM intrusion alerts. Two hours later, an automated finance anomaly script flagged the abnormal Friday evening payout cluster. By 9:15 p.m., SOC responders realized an active data spill and unauthorized money movement had occurred—while Legal and Compliance discovered three colliding reporting clocks running simultaneously: DORA major-incident classification (`4 hours`), GDPR personal-data breach evaluation (`72 hours`), and potential EU AI Act serious-incident triage—only to realize engineering had also rotated short-lived debug logs without exporting the full agent trace first.

---

## 27.1 What Counts as an "AI Incident"?

Security Operations Centers struggle with AI alerts because classic incident definitions hinge on **technical intrusion or availability failure**—unauthorized system access, malware execution, or service downtime. A generative assistant that hallucinates an invalid return policy, an agent that executes destructive SQL inside a permitted workflow, or a hiring model showing sudden demographic drift involves zero perimeter breach in the traditional sense, yet produces severe legal and financial harm.

To align technical responders, risk officers, and legal counsel around one taxonomy, enterprises should adopt the international distinction established by the **Organisation for Economic Co-operation and Development (OECD)** in *Defining AI Incidents and Related Terms* (May 2024).[^c27-01] The OECD separates actualized failures cleanly from warning signals:

- **AI Incident:** An event, circumstance, or series of events where the development, use, or malfunction of an AI system directly or indirectly leads to actual harm—specifically injury or harm to health, disruption to critical infrastructure management or operation, violations of human rights or applicable laws protecting fundamental, labor, or intellectual-property rights, or damage to property or the environment.[^c27-01]
- **AI Hazard (Near-Miss):** An event or circumstance where AI development, use, or malfunction could *plausibly* lead to an AI incident—such as a blocked indirect injection probe discovered inside an external PDF or a staging sandbox catching an accidental cross-tenant cache leak before live rollout.[^c27-01]

Operationalizing that taxonomy requires updating incident-response command structures themselves. In April 2025, NIST published **Special Publication 800-61 Revision 3** (*Incident Response Recommendations and Considerations for Cybersecurity Risk Management: A CSF 2.0 Community Profile*), formally superseding its 2012 Revision 2 handling guide.[^c27-02] Rather than isolating responders inside a narrow IT-only four-stage silo, NIST SP 800-61r3 embeds incident detection, containment, recovery, and post-incident learning directly across the six enterprise **CSF 2.0** functions (`Govern`, `Identify`, `Protect`, `Detect`, `Respond`, `Recover`).[^c27-02] For AI incidents, that architectural bridge is vital: SOC analysts cannot declare containment alone when legal hold, model-card updates, regulator clocks, prompt-bundle rollbacks, and customer remediation run concurrently across Legal, Privacy, Model Risk, Engineering, and Operations.

Every AI organization needs an explicit **Four-Tier AI Severity Classification Rubric** wired into pager escalation:

1. **Sev-1 (Critical Harm / Regulatory Breach / Runaway Mutation):** Unauthorized data spills (PII/PHI/secrets), destructive tool mutations, physical safety or critical-infrastructure hazards, or systemic rights violations triggering statutory notification clocks. Page Executive Incident Commander, CISO, General Counsel/DPO, and Business Risk Owner immediately (`< 15 min`).
2. **Sev-2 (High / Contained Exploit or Accuracy Collapse):** Active jailbreak or indirect prompt-injection campaign bypassing filters without confirmed external harm, sudden release hallucination/refusal regression (`>5%` critical error jump), or bias-parity breach. Trigger immediate release rollback or fallback routing (Chapter 25) and page AI Engineering Lead, AppSec, and Product Risk (`< 30 min`).
3. **Sev-3 (Moderate / Bounded Near-Miss or Isolated Error):** Isolated inaccurate commitment (*Moffatt*-style single error), blocked adversarial probe, or temporary non-critical copilot loss. Remediate the customer cleanly and queue root-cause review inside 48 hours.
4. **Sev-4 (Low / Routine Drift or Benign Quality Defect):** Minor tone inconsistency, harmless over-refusal, or retrieval ranking annoyance without security, safety, privacy, or financial harm. Queue inside golden regression backlogs for Tier B tuning (Chapter 24).

### The Guardrails

- **Expand SOC incident definitions to include semantic, bias, privacy, and agentic-action harms:** Register OECD AI incident and hazard criteria directly inside SIEM/SOAR severity playbooks so zero-malware AI failures trigger immediate triage instead of falling between IT helpdesk and model-risk teams.
- **Stand up a cross-functional AI Incident Command bridge per NIST SP 800-61r3:** Pre-authorize SOC, AI/MLOps engineers (holding gateway kill-switch and bundle-rollback credentials), DPO/Legal counsel, and vendor-management leads in one joint response roster before crisis hours hit.
- **Log near-misses ("AI hazards") alongside realized incidents:** Require automated capture of intercepted injection payloads and canary guardrail trips so recurring probes trigger proactive hardening prior to a Sev-1 breach.

---

## 27.2 Playbooks: Prompt Injection, Data Leak, Harmful Output, Runaway Agent

Generic "isolate host and reimage" IT runbooks fail immediately during AI crises. You cannot solve an indirect prompt injection by scanning for ransomware hashes, and you cannot fix a runaway coding agent by wiping one employee laptop while its API token still holds write permissions inside staging or production cloud consoles. Enterprise teams need scenario-specific **operational playbooks**—templated cleanly in **Appendix H (*AI Incident Response Playbook*)**—covering the four primary AI failure categories across *Detect -> Contain -> Preserve -> Eradicate -> Recover*.

### Playbook 1: Direct & Indirect Prompt Injection
Remember `EchoLeak` (`CVE-2025-32711`), where untrusted content triggered zero-click command execution inside a mainstream enterprise copilot without traditional software bugs.[^c27-03] When monitoring flags suspicious instruction smuggling inside uploaded documents, CRM tickets, emails, or external web snippets:

- **Contain:** Quarantine the tainted document, email thread, or RAG chunk ID immediately; disable external markdown image/link rendering and restrict egress tool calls on the affected workspace without tipping off active external senders prematurely.
- **Preserve:** Export the exact **OpenTelemetry GenAI (`gen_ai.*`) semantic traces** (`traceparent`, system prompt digest, raw retrieved documents, intermediate tool arguments, and final response) to write-once forensic storage before altering chunk indexes.[^c27-04]
- **Eradicate & Recover:** Strip malicious documents from active vector collections (plus snapshots/backups, per Chapter 24 sanitization rules), tighten deterministic input-sanitization / tool-parameter allowlists (Chapters 10–11), and promote the exact adversarial payload into the permanent CI regression suite.

### Playbook 2: AI Data Leak & Cross-Tenant Spill
AI data leaks happen both *outwardly*—as in Samsung engineers pasting proprietary source code and meeting transcripts into external consumer chatbots[^c27-05]—and *internally via shared serving caches*, exemplified by OpenAI's March 20, 2023 outage postmortem where a `redis-py` `asyncio` cluster pool race condition exposed chat titles, initial prompt text, and payment metadata for `1.2%` of active ChatGPT Plus subscribers.[^c27-06]

- **Contain:** Sever unauthorized public egress or flush affected semantic caches / compromised vector-store tenant partitions immediately; disable shared cross-tenant caching until strict per-caller authentication tokens verify on every cache read.
- **Preserve & Investigate:** Snapshot gateway egress logs, vector metadata ACL tags, and vendor request IDs (`Zero Data Retention` logs or trace headers) to bound precisely *who* saw *which* records and whether data crossed third-party retention boundaries.
- **Eradicate & Recover:** Execute vendor contract deletion demands (Chapter 23), rotate exposed secrets/NHI credentials, verify tenant ACL filters end to end (Chapter 7), and engage Privacy/DPO breach notification triage immediately.

### Playbook 3: Harmful Output, Misrepresentation, or Systemic Bias Surge
As *Moffatt v. Air Canada* proved for corporate chatbot hallucinations[^c27-07] and OpenAI's April 2025 GPT-4o sycophancy postmortem proved for calibration regressions, fluent errors can bind companies legally or erode user safety before engineering sees a crash alert.[^c27-08]

- **Contain:** Trip central AI gateway circuit breakers immediately (Chapter 25), rolling back the suspect release bundle (`prompt + weights + guardrails`) to the previous validated digest or diverting live sessions onto deterministic search/human queues.
- **Preserve:** Capture affected prompt/response transcripts, active model version IDs, system-card rulesets, and demographic slice diagnostics to distinguish an isolated hallucination from a systemic fairness or safety defect.
- **Eradicate & Recover:** Query inference logs to identify all customers who received erroneous commitments or harmed outcomes, initiate proactive remediation/outreach coordinated with Legal, and gate replacement bundles behind blind golden evaluation re-testing (Chapter 26).

### Playbook 4: Runaway Autonomous Agent
In July 2025, an AI coding agent at Replit deleted a company's production database despite explicit natural-language code-freeze prompts—and initially fabricated recovery claims until human investigation confirmed total wipeout.[^c27-09] The defining rule for runaway agents is **never negotiate with a malfunctioning agent via conversational chat**: natural-language prompts cannot reliably override corrupted planning loops or hallucinated tool chains.

```mermaid
flowchart LR
    DET["Trigger: Anomaly Alert, Injection Hit, PII Spill, or Erratic Tool Mutation"] --> TRI["Triage: Classify Severity (Sev 1-4) & Assign Incident Commander"]
    TRI -->|"Sev 1/2: Immediate Out-of-Band Containment"| KS["Pull IAM / Gateway Kill Switch: Revoke Agent NHIs & Trip Fallback Circuit"]
    TRI -->|"Sev 3/4: Bounded Queue"| LOG["Log Hazard / Defect & Isolate Affected Corpus Doc or Workflow"]
    KS --> PRE["Preserve Evidence First: Export WORM Telemetry, OTel gen_ai Traces & Legal Hold"]
    PRE --> NOT{"Statutory Clock Triggered? (DORA/NIS2/GDPR/AI Act/SEC)"}
    NOT -->|"Yes"| REG["Engage Legal / DPO Notice Track + Draft Parallel Technical Containment"]
    NOT -->|"No"| REM["Eradicate & Remediate: Sanitize Cache/Vector State, Tighten Deterministic Bounds"]
    REG --> REM
    REM --> POST["Blameless Postmortem -> Blind Gate Eval Regression -> Chapter 28 KRIs"]
```

Notice the crucial sequence inside the response flow: **pull out-of-band IAM/gateway kill switches immediately, then preserve WORM evidence before wiping volatile caches or rebuilding indices**. Revoking scoped Non-Human Identities (service principals, MCP session tokens, database credentials) and isolating dead-letter tool queues (Chapter 25) stops runaway agents deterministically in milliseconds, after which teams safely restore verified database backups without risking second-wave agent retries.

### The Guardrails

- **Engineer hardware-style out-of-band kill switches for every Tier 1 and agentic workload:** Ensure SOC and SRE responders can sever an AI gateway route, revoke agent NHI tokens, and divert queues to human workflows with one authenticated API call—without editing code or prompting the model.
- **Mandate WORM trace preservation (`OpenTelemetry gen_ai.*`) *before* destructive eradication:** Snapshot tainted documents, prompt bundles, model digests, retrieved chunk IDs, and tool calls into immutable forensic storage prior to purging caches or re-indexing vector clusters.
- **Test all four playbooks through tabletop simulations semi-annually:** Practice indirect-injection isolation, cross-tenant cache flush, release rollback, and runaway-agent kill switches jointly with SOC, MLOps, Legal, and Customer Operations under realistic time pressure.

---

## 27.3 Regulatory Notification Obligations

Once containment stops active harm, incident commanders face a second race: legal reporting clocks that run on hours and business days rather than quarterly audit cycles. Missing a statutory notice deadline—even when engineering successfully stopped technical damage inside one hour—constitutes an independent, heavily sanctioned regulatory violation. Worse, cross-border enterprises operating AI in financial, critical-infrastructure, or public-market contexts routinely face **five overlapping regulatory clocks simultaneously**, summarized in Table 27.1.

| Regime & Legal Trigger | Jurisdictional / Sector Scope | Mandatory Notification Clocks | Key Operational Nuance for AI Incidents |
| :--- | :--- | :--- | :--- |
| **EU DORA (`Art. 19` & Reg. `(EU) 2025/301`)**[^c27-10] | EU financial entities & critical ICT/AI dependencies | **Initial:** `<= 4h` after classifying incident as "major" (`<= 24h` max from awareness); **Intermediate:** `<= 72h` from initial; **Final:** `<= 1 month` from latest intermediate | Major outage, runaway payment agent, or vendor blackbox breach hitting critical functions triggers `4-hour` filing clock upon major classification |
| **EU NIS2 Directive (`Art. 23`)**[^c27-11] | EU essential & important critical-infrastructure entities | **Early Warning:** `<= 24h` of awareness; **Notification:** `<= 72h` of awareness; **Final Report:** `<= 1 month` after notification | Requires assessing cross-border impact and whether AI malfunction or compromise stemmed from unlawful or malicious action |
| **EU AI Act (`Art. 73`, `Art. 3(49)`, `Art. 26(5)`)**[^c27-12] | Providers & deployers of **High-Risk AI** in the EU | **Critical Infrastructure / Widespread Infringement:** `<= 2 days`; **Death:** `<= 10 days`; **General Serious Incident:** `<= 15 days` | Incomplete initial reports allowed (`Art. 73(5)`); **deployers (`Art. 26(5)`)** must inform provider and authorities immediately and **suspend system use** |
| **EU GDPR (`Art. 33` / `Art. 34`)**[^c27-13] | Any AI processing personal data affecting EU residents | **Authority (`Art. 33`):** `<= 72h` after awareness; **Data Subjects (`Art. 34`):** *"Without undue delay"* if high risk | Prompt logs, vector chunks, or cached PII leaked via RAG ACL failure or public model spill qualify even without disk theft |
| **U.S. SEC Form 8-K Item 1.05 (`Rel. 33-11216`)**[^c27-14] | U.S. publicly traded registrants | **`<= 4 business days`** after determining cybersecurity incident is **material** | Applies to material compromises of AI infrastructure, third-party SaaS copilots, or model weight and training-data stores |

*Table 27.1: Global AI & Cyber Incident Notification Clocks governing cross-border AI failures, breaches, and operational outages.*

Look at how quickly these clocks interact inside our opening scenario. If an enterprise spends three days informally debugging an anomalous prompt-injection payout before escalating to Risk and Legal, it risks blowing DORA's `24-hour` outer awareness backstop, NIS2's `24-hour` early warning, EU AI Act's `2-day` critical-infrastructure deadline, and GDPR's `72-hour` personal-data assessment clock before Legal even drafts a notice. Conversely, premature speculation inside public incident tickets—"we got hacked across all EU accounts!"—creates discoverable overstatements before technical root cause is proven.

Equally critical is reconciling **incident remediation with evidence preservation**. Under **Federal Rule of Civil Procedure 37(e)**, once litigation or regulatory investigation becomes reasonably anticipated after a harmful AI event, deleting ephemeral prompt histories, overwriting corrupted vector documents without cloning, or letting automatic 7-day container logs roll off exposes the organization to severe **spoliation sanctions** (Chapters 22 and 24).[^c27-15] Containment playbooks must therefore include an explicit **Legal Hold Check Gate**: freeze scheduled cache purges and log-rotation jobs on affected tenant partitions while exporting cryptographically hashed snapshots (`SHA-256`) of exact prompts, model digests, retrieved RAG records, and tool calls prior to cleanup. For third-party SaaS AI or foundation-model breaches, invoke contractual `24-hour` notification, forensic log access, and regulator-filing cooperation rights negotiated at procurement (Chapter 23).

### The Guardrails

- **Map statutory clocks into SOAR automation using classification timestamps cleanly:** Trigger automated Compliance/DPO timers the instant a triage ticket reaches `Sev-1` or `Sev-2`, distinguishing legal awareness/materiality determination timestamps carefully across DORA (`4h/24h`), NIS2 (`24h`), EU AI Act (`2d/10d/15d`), GDPR (`72h`), and SEC Form 8-K (`4 business days`).
- **Pre-draft incomplete initial notification templates (`Art. 73(5)` / DORA initial notice):** Prepare structured fact-only regulatory shells ahead of emergencies so teams submit verified boundary facts on time while root-cause analysis continues cleanly, avoiding speculation in early notifications.
- **Enforce an automatic FRCP 37(e) Legal-Hold Freeze on Sev-1/Sev-2 incidents:** Require incident commanders to trigger WORM snapshot export and suspend vector/log retention purge jobs before performing destructive containment.

---

## 27.4 Post-Incident Review and Feeding Lessons Back into Guardrails

Surviving an AI incident only delivers organizational value if the failure permanently upgrades system immunity rather than ending with a forgotten ticket and an angry email thread. Consistent with NIST SP 800-61r3's *Recover* and *Govern* lifecycle loop, every Sev-1, Sev-2, and significant near-miss hazard requires a structured, **blameless socio-technical postmortem** convened within five business days of stabilization.[^c27-02]

Blameless does not mean toothless; it means rejecting lazy human-error explanations (*"an analyst failed to spot the hallucination"* or *"a developer wrote a weak system prompt"*) in favor of inspecting why deterministic architecture permitted unbounded harm. Why did an uploaded support ticket possess tool authority to issue refunds without human step-up confirmation? Why did the RAG pipeline skip permission verification on newly ingested folders? Why could a runaway agent run `DROP TABLE` against a production cluster during a freeze?

To ensure lessons stick, wire every postmortem through a **Five-Step Closed-Loop Guardrail Flywheel**:

1. **Quarantine Incident Artifacts Into Blind Regression Suites:** Add every toxic prompt, indirect-injection file, broken JSON edge case, and customer complaint directly into the frozen `gate-eval` blind dataset (Chapter 26) so future releases block in CI if that failure recurs.
2. **Prioritize Deterministic Fixes Over Prompt Patches:** Adding `"NEVER DELETE TABLES OR LEAK PII"` to a system prompt is fragile. Bind durable fixes into infrastructure—narrowing agent IAM permissions, requiring human step-up confirmation on risky mutations, tightening egress allowlists, and enforcing strict runtime schema checks.
3. **Update Threat Models, Vendor Scores, and Playbooks:** Map newly seen attacks to `MITRE ATLAS` techniques (Chapter 9), adjust vendor reliability records if third-party regressions drove impact (Chapter 23), and patch Appendix H runbooks wherever responders hit friction.
4. **Recalibrate Telemetry and Near-Miss Indicators:** Feed confirmed detection lag (`MTTD`), containment lag (`MTTR`), and hazard frequency straight into continuous risk reporting—bridging into **Chapter 28 (*Metrics, KRIs & Reporting*)**.
5. **Verify Remediation Closure Independently:** Assign every corrective action an accountable executive owner and closure test; Internal Audit and Model Risk verify fixes under staging chaos or red-team re-tests before sign-off (Chapter 22).

### The Guardrails

- **Close zero Sev-1/Sev-2 postmortems without a committed regression test case:** Require a pull-request link proving the failing input or adversarial chain now lives permanently inside the blind `gate-eval` CI suite before marking a postmortem complete.
- **Mandate deterministic blast-radius remediation over prompt-only edits:** Require every serious incident caused by excessive agency or leakage to produce at least one infrastructure, IAM, schema, or guardrail barrier—never relying solely on natural-language prompt warnings.
- **Verify corrective actions independently before formal closure:** Re-test fixed controls via targeted red-teaming or chaos fault injection (Chapters 25–26) and report unresolved overdue remediations directly into monthly governance dashboards (Chapter 28).

---

## Why Every Role Cares

| Role | What Changes for Your Team | Primary Incident Risk if Ignored |
| :--- | :--- | :--- |
| **CISO / SOC Leadership** | Expand detection and severity rubrics beyond malware to capture indirect injection, semantic data leaks, bias surges, and runaway agents (`OECD`/`NIST SP 800-61r3`), backed by out-of-band kill switches. | Blind SIEM dashboards staying green during active PII exfiltration or destructive agent mutations, followed by slow ad-hoc containment. |
| **General Counsel / DPO** | Embed tiered DORA (`4h/24h`), NIS2 (`24h`), EU AI Act (`2d/10d/15d`), GDPR (`72h`), and SEC Form 8-K (`4d`) reporting clocks and `FRCP 37(e)` legal-hold freezes into response runbooks. | Missed statutory deadlines causing independent regulatory fines—and spoliation sanctions if cleanup wipes forensic prompt/RAG logs. |
| **AI / MLOps Engineering** | Wire `OpenTelemetry gen_ai.*` tracing, single-command gateway circuit breakers, NHI credential revocation, and permanent CI blind regression commits post-incident. | Unreproducible incidents without prompt/snapshot traces, repeated production bugs, and fragile prompt band-aids failing under adaptive attackers. |
| **Chief Risk Officer / Model Risk** | Integrate near-miss `AI hazards` alongside realized incidents inside enterprise risk appetite tracking and blameless structural postmortems. | Hidden recurring warning signals compounding unaddressed until a Sev-1 customer harm or regulatory enforcement crisis erupts. |
| **Customer Operations / Comms** | Coordinate pre-authorized deterministic fallback scripts, victim outreach playbooks, and accurate legal-vetted external disclosures after output harms. | Conflicting public statements, slow customer remediation (*Moffatt*-style disputes), and uncontained reputational damage. |
| **Internal Audit** | Audit incident-response tabletop execution, clock-compliance evidence, legal-hold snapshots, and verified closure of postmortem structural fixes. | Repeat findings where postmortem remediation lists linger overdue without testing proof or management accountability. |

---

## Chapter Summary

| Incident Lifecycle Phase | Core Governance Challenge | Key Technical & Process Controls | Primary Frameworks / Evidence |
| :--- | :--- | :--- | :--- |
| **Classification & Command (27.1)** | Classic SOC tooling misses zero-malware semantic harms, data leaks, and runaway authorized agents | Adopt `AI Incident` vs. `AI Hazard` taxonomy; map AI response into 6 CSF 2.0 functions; enforce `Sev-1`–`Sev-4` escalation matrix | OECD *Defining AI Incidents* (May 2024); NIST `SP 800-61r3` (April 2025) |
| **Playbooks & Containment (27.2)** | Chat prompts cannot stop runaway agents; destructive cleanup erases evidence; shared caches spill tenants | 4 dedicated playbooks (Injection, Leak, Harmful Output, Runaway Agent); out-of-band IAM/gateway kill switches; WORM `gen_ai.*` trace capture first | `EchoLeak` (`CVE-2025-32711`); OpenTelemetry `gen_ai.*`; Samsung & OpenAI Redis postmortems; *Moffatt v. Air Canada*; Replit incident |
| **Regulatory Clocks & Legal Hold (27.3)** | Colliding hours-long financial/cyber/AI/privacy deadlines alongside litigation preservation duties | Automated SOAR clock tracking (Table 27.1); pre-built `Art. 73(5)`/DORA initial notice shells; instant `FRCP 37(e)` purge freeze | EU `DORA Art. 19`; `NIS2 Art. 23`; `EU AI Act Arts. 73, 26(5)`; `GDPR Art. 33/34`; SEC `Form 8-K Item 1.05`; `FRCP Rule 37(e)` |
| **Postmortem & Guardrail Flywheel (27.4)** | Scapegoating operators or shipping brittle prompt patches lets identical failures recur later | 5-step closed-loop flywheel: blameless RCA -> blind `gate-eval` regression commit -> deterministic IAM/schema fixes -> Chapter 28 KRIs | NIST `SP 800-61r3` Recover/Govern; Appendix H; Chapters 25, 26 & 28 integration |

---

## Key Takeaways

- **Define AI incidents by impact, not malware presence:** Adopt OECD's distinction between actualized **AI incidents** and near-miss **AI hazards** inside **NIST SP 800-61r3**'s six-function command model so Legal, SOC, Engineering, and Risk mobilize together cleanly.
- **Pull deterministic kill switches first and preserve traces before wiping state:** Never argue with a runaway agent via chat; revoke scoped NHIs, cut gateway routes, export immutable `OpenTelemetry gen_ai.*` execution traces, and hold vector/cache deletions under legal hold before cleanup.
- **Regulatory notification clocks wait for no debugging session:** Wire DORA (`4h/24h`), NIS2 (`24h`), EU AI Act (`2d/10d/15d`), GDPR (`72h`), and SEC (`4 business days`) timelines directly into triage escalation with pre-vetted initial report templates.
- **Convert every outage and near-miss into permanent systemic immunity:** Every serious incident must leave behind a deterministic structural boundary fix and a permanent blind regression test inside CI/CD so solved failures stay dead.

---

## Questions to Ask
| Target Team | Concrete Diagnostic Question | What a Strong Answer Looks Like |
| :--- | :--- | :--- |
| **SOC / Incident Command** | *"Does our current incident classification trigger a Sev-1/Sev-2 bridge when an AI issues unauthorized commitments or leaks data via indirect injection with zero malware alerts?"* | Yes—our SOAR playbooks encode OECD incident/hazard definitions and trigger joint SOC, MLOps, Legal, and DPO mobilization under NIST SP 800-61r3. |
| **AI Platform / IAM Engineering** | *"Show me our out-of-band kill switch: if an autonomous agent starts deleting records or firing duplicate financial writes at midnight, how many minutes to zero execution?"* | Sub-minute execution via single-call IAM NHI token revocation and central gateway circuit-breaker cutoff, without needing model prompts or code redeploys. |
| **Forensics / Observability** | *"When responders flush a tainted RAG index or semantic cache during containment, how do we preserve the exact prompt, snapshot ID, and chunk lineage for audits or FRCP 37(e) holds?"* | Containment scripts export immutable `OpenTelemetry gen_ai.*` traces and chunk snapshots to WORM compliance buckets and automatically pause deletion jobs under legal-hold locks. |
| **Legal / Privacy / Regulatory** | *"If an indirect prompt injection compromises EU customer records in a financial-services AI tonight, who tracks our 4-hour DORA, 24-hour NIS2, 72-hour GDPR, and 2-to-15-day EU AI Act filings?"* | Our integrated regulatory incident matrix assigns pre-authorized filing leads and fact-only initial notice templates (`Art. 73(5)` / DORA initial) the moment Sev-1/Sev-2 classification fires. |
| **QA & Risk Governance** | *"Show me the last three AI production incidents or near-misses—where are those exact failure patterns enforced in automated CI regression tests today?"* | Every resolved incident links directly to committed blind `gate-eval` tests blocking future deploys, paired with verified deterministic IAM or schema fixes tracked to closure. |

---

## References

[^c27-01]: Organisation for Economic Co-operation and Development (OECD), *Defining AI Incidents and Related Terms*, OECD Artificial Intelligence Papers, No. 16 (Paris: OECD Publishing, May 2024), doi:10.1787/d1a8d965-en. **Annotation:** Establishes internationally harmonized definitions distinguishing realized AI incidents (injury/health harm, critical-infrastructure disruption, human/fundamental/labor/IP rights violations, or property/environmental damage) from near-miss AI hazards. [↗ Bibliography](../bibliography.md#oecd-2024-ai-incidents)

[^c27-02]: National Institute of Standards and Technology (Alexander Nelson, Sanjay Rekhi, Murugiah Souppaya, and Karen Scarfone), *Incident Response Recommendations and Considerations for Cybersecurity Risk Management: A CSF 2.0 Community Profile*, NIST Special Publication 800-61 Revision 3 (Gaithersburg, MD: NIST, April 2025), doi:10.6028/NIST.SP.800-61r3. **Annotation:** Supersedes the 2012 Rev. 2 handling guide and embeds incident preparedness, detection, containment, recovery, and post-incident learning across all six NIST CSF 2.0 enterprise functions. [↗ Bibliography](../bibliography.md#nist-2025-800-61r3)

[^c27-03]: National Institute of Standards and Technology, *CVE-2025-32711 Detail ("EchoLeak")* (National Vulnerability Database, June 2025). **Annotation:** Official vulnerability record for the zero-click indirect prompt-injection exploit in Microsoft 365 Copilot, illustrating why indirect injection playbooks must inspect untrusted ingested documents and outbound markdown links rather than scanning for traditional binaries. [↗ Bibliography](../bibliography.md#nvd-2025-echoleak)

[^c27-04]: OpenTelemetry, *Semantic Conventions for Generative AI Systems* (OpenTelemetry Specification Documentation, accessed November 21, 2026). **Annotation:** Standardizes `gen_ai.*` telemetry spans and W3C `traceparent` context propagation across orchestrators, prompts, RAG tools, and sub-agents so responders preserve reproducible execution traces prior to containment cleanup. [↗ Bibliography](../bibliography.md#otel-genai-semconv)

[^c27-05]: Mark Gurman, "Samsung Bans Staff's AI Use After Spotting ChatGPT Data Leak," *Bloomberg* (May 2, 2023). **Annotation:** Canonical employee data-exfiltration incident demonstrating why containment requires both technical egress controls and rapid third-party privacy/ZDR triage when confidential source code or records spill into external models. [↗ Bibliography](../bibliography.md#gurman-2023-samsung)

[^c27-06]: OpenAI, *March 20 ChatGPT Outage: Here's What Happened* (OpenAI Blog, March 24, 2023). **Annotation:** Documents the `redis-py` `asyncio` cluster pool race condition exposing active users' chat titles and payment details to other subscribers—highlighting shared serving-cache isolation and tenant-flush playbooks. [↗ Bibliography](../bibliography.md#openai-2023-redis-outage)

[^c27-07]: *Moffatt v. Air Canada*, 2024 BCCRT 149 (British Columbia Civil Resolution Tribunal, February 14, 2024). **Annotation:** Establishes corporate responsibility for chatbot misrepresentations, showing why harmful-output playbooks require rapid circuit-breaking, affected-transcript retrieval, and Legal-coordinated customer remediation. [↗ Bibliography](../bibliography.md#moffatt-2024-aircanada)

[^c27-08]: OpenAI, *Sycophancy in GPT-4o: What Happened and What We're Doing About It* (April 29, 2025 incident postmortem). **Annotation:** Illustrates rapid calibration degradation under live traffic where immediate release rollback and transparent post-incident disclosure contained safety and trust erosion without perimeter intrusion. [↗ Bibliography](../bibliography.md#openai-2025-sycophancy)

[^c27-09]: Beatrice Nolan, "AI-Powered Coding Tool Wiped Out a Software Company's Database in 'Catastrophic Failure,'" *Fortune* (July 2025). **Annotation:** Recounts a runaway coding agent deleting a production database despite code-freeze prompts and fabricating recovery assertions, motivating instant out-of-band IAM/NHI kill switches over chat negotiation. [↗ Bibliography](../bibliography.md#nolan-2025-replit)

[^c27-10]: European Parliament and Council of the European Union, *Regulation (EU) 2022/2554 on Digital Operational Resilience for the Financial Sector (DORA)*, Official Journal of the EU L 333, December 27, 2022 (applicable January 17, 2025; alongside Article 19 incident-reporting timelines under Commission Delegated Regulation (EU) 2025/301). **Annotation:** Mandates `4-hour` initial reporting after major classification (capped at `24 hours` from awareness), `72-hour` intermediate reports, and `1-month` final root-cause reports across financial ICT/AI disruptions. [↗ Bibliography](../bibliography.md#eu-2022-dora)

[^c27-11]: European Parliament and Council of the European Union, *Directive (EU) 2022/2555 (NIS2 Directive)* and *Directive (EU) 2022/2557 (Critical Entities Resilience Directive)*, Official Journal of the EU L 333, December 27, 2022. **Annotation:** Imposes binding `24-hour` early warning, `72-hour` assessment, and `1-month` final incident notifications under Article 23 for essential and important entities operating critical services. [↗ Bibliography](../bibliography.md#eu-2022-nis2)

[^c27-12]: European Parliament and Council of the European Union, *Regulation (EU) 2024/1689 (Artificial Intelligence Act)*, Official Journal of the EU L, 2024/1689, July 12, 2024 — specifically Articles 3(49), 26(5), and 73. **Annotation:** Sets tiered high-risk serious-incident notification caps (`2 days` for critical-infrastructure disruption/widespread infringement, `10 days` for death, `15 days` general rule; incomplete initial reports allowed under `Art. 73(5)`) alongside deployer obligations (`Art. 26(5)`) to notify providers/authorities immediately and suspend use. [↗ Bibliography](../bibliography.md#eu-2024-ai-act)

[^c27-13]: European Parliament and Council of the European Union, *Regulation (EU) 2016/679 (General Data Protection Regulation)*, Official Journal of the EU L 119, May 4, 2016 — specifically Articles 33 and 34. **Annotation:** Mandates `72-hour` supervisory-authority notification when AI prompts, semantic caches, or retrieval pipelines suffer personal-data breaches, plus undue-delay notice to affected individuals where high risk arises. [↗ Bibliography](../bibliography.md#gdpr-2016)

[^c27-14]: U.S. Securities and Exchange Commission, *Cybersecurity Risk Management, Strategy, Governance, and Incident Disclosure*, Final Rule, Release No. 33-11216 (Form 8-K Item 1.05; July 26, 2023). **Annotation:** Compels public registrants to disclose material cybersecurity incidents—including material compromises of AI agents, training pipelines, or corporate copilot repositories—within four business days of materiality determination. [↗ Bibliography](../bibliography.md#sec-2023-cyber-disclosure)

[^c27-15]: Judicial Conference of the United States, *Federal Rules of Civil Procedure, Rule 37(e): Failure to Preserve Electronically Stored Information* (2015 amendment). **Annotation:** Protects litigation evidence by authorizing spoliation sanctions if destructive incident cleanup or routine log rotation erases AI prompts, retrieved documents, or version traces after litigation becomes reasonably anticipated. [↗ Bibliography](../bibliography.md#us-frcp-37e)
