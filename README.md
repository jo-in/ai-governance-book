# ai-governance-book


### How This Handbook Adds More Value Beyond What Exists

1. **Collapses the "Five-Book Silo Problem" into One Shared Operating Language**
   Today an enterprise trying to govern AI has to buy five separate books—one for engineers, one for AppSec, one for MRM/data scientists, one for executives, and one for lawyers—none of which share a vocabulary or control architecture. Every chapter in this handbook translates the exact same risk simultaneously across **all eight roles** (Board, CEO, CIO, CISO, CDO, General Counsel/DPO, AI Engineers, and Business Owners) via consistent *Why Every Role Cares* tables, *The Guardrails* checklists, diagnostic questions, and role cheat sheets ([31-appendices.md](file:///Users/work/Antigravity/retrieval-v2/book/chapters/31-appendices.md)).

2. **Grounded in the Late-2025/2026 Agentic, Security, and Regulatory Reality**
   Most widely cited AI governance books were written between 2022 and early 2024—before enterprise agentic deployments, `MCP`/`A2A` protocols, and binding enforcement waves arrived. This manuscript integrates **234 verified primary sources** (`467` annotated footnotes in [bibliography.md](file:///Users/work/Antigravity/retrieval-v2/book/bibliography.md)), including:
   - **2025–2026 Security & Incidents:** `EchoLeak` (`CVE-2025-32711`), `mcp-remote` RCE (`CVE-2025-6514`), Replit's production DB wipe, OpenAI's Dec 2024 K8s blackout and Apr 2025 sycophancy rollback, `Nasr et al.` (adaptive attacks defeating 12 static defenses), `CaMeL`, `OWASP Agentic Top 10:2026`, `NIST AI 100-2 E2025`, and `NIST SP 800-61 Rev. 3`.
   - **2025–2026 Law & Standards:** `EU Digital Omnibus 2026/1744` (`Dec 2027` / `Aug 2028` deferrals), `Fed SR 26-2` (`Apr 2026`), `EU DORA` (`4h/24h` clocks), `UK PRA SS1/21` (`Mar 2025`), `EU Data Act` switching rights, California `SB 53` (*TFAIA*), Colorado `SB 26-189`, `ISO/IEC 42005` & `42006`, and `NIST SP 800-88 Rev. 2`.

3. **Covers High-Impact Enterprise Blind Spots Most Competitors Omit**
   Even combined, the five books above leave major enterprise risk surfaces uncovered that this handbook treats end to end:
   - **Permission-Aware RAG & Embedding Privacy:** Enforcing `Zanzibar`/ReBAC document ACLs at retrieval time and defending against `vec2text` embedding inversion (Chapters 7 & 13).
   - **Legal-Hold & e-Discovery Governance:** Reconciling data-minimization purges with `FRCP Rule 37(e)` spoliation sanctions, *In re OpenAI* preservation lessons, and `EU AI Act Art. 18` (`10-year`) vs. `Art. 26(6)` (`6-month`) retention clocks (Chapters 22 & 24).
   - **M&A Algorithmic Disgorgement & Fourth-Party Risk:** Auditing acquired models for `FTC v. Rite Aid` deletion traps, poisoned weights, and hidden sub-processor foundation chains (Chapter 23).
   - **AI FinOps, Zombie Pilots & ESG Compute Energy:** Connecting `OpenTelemetry gen_ai.*` unit economics and `90-day` pilot sunsets (`State of FinOps 2026`, Gartner `>40%` cancellation risk) directly to SLM carbon right-sizing (`Luccioni et al.`), `IEA` `945 TWh` grid demand, `EU CSRD ESRS E1`, and `EU AI Act Annex XI` (Chapter 28).
   - **AI Speak-Up & Whistleblower Compliance:** Addressing `EU AI Act Art. 87` (`Directive 2019/1937`), California `SB 53`, and `SEC Rule 21F-17` NDA/DLP carve-outs alongside psychological safety (Chapter 29).

4. **Turns Theory into Monday-Morning Execution (`Chapter 30` + `Appendices A–J`)**
   Rather than ending with abstract principles, readers get a **Five-Level Maturity Model**, a sequenced **30/60/90-Day Action Plan** ([30-governance-maturity-model-and-roadmap.md](file:///Users/work/Antigravity/retrieval-v2/book/chapters/30-governance-maturity-model-and-roadmap.md)), and **ten copy-ready operational artifacts** in [31-appendices.md](file:///Users/work/Antigravity/retrieval-v2/book/chapters/31-appendices.md) (Role Cheat Sheets, 18-activity RACI, 5-minute Intake/Tiering Form, 24+ question Vendor DDQ, plain-English AUP with whistleblower carve-outs, Go/No-Go Pre-Flight Rubric, 14-domain Regulatory Crosswalk, offline Incident Response Playbook, 55-term Glossary, and curated Further Reading).

5. **Treats Guardrails as Speed Enablers, Not Compliance Theater**
   Instead of preaching blanket bans or heavy manual committees that push `78%` of employees onto shadow `BYOAI`, the entire book builds around **paved roads** (1-click SSO `ZDR` portals, `<48h` Tier 3 fast lanes, `Policy-as-Code` CI/CD blind evals, fail-closed sidecars, and continuous `NIST SP 800-137` assurance)—giving enterprises a concrete architecture to ship AI *faster* with lower risk.
