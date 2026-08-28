---
title: "Privacy at Scale Roblox's Infrastructure for Honoring User Privacy Rights"
speakers: ["Hao Zhang", "Yiwen Luo", "Minkyong Kim", "Nicole Grinstead"]
conference: "Black Hat"
conference_full: "Black Hat USA 2026"
edition: "USA"
year: 2026
source_pdf: "BlackHat_USA_2026_Slides/Hao Zhang&Yiwen Luo&Minkyong Kim&Nicole Grinstead_Privacy at Scale Roblox's Infrastructure for Honoring User Privacy Rights.pdf"
pages: 46
sha256: "e91d5770808daf95e87a4ce5d7b9b86bfbfc7c257bd0d3319d49e8125842d504"
text_chars: 19094
ocr_pages: 4
has_ocr: true
redacted_secrets: 0
ocr_confidence: 93.6
ocr_unreliable_blocks: 0
vision_verified_pages_changed: 44
vision_verified_pages: 46
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T05:34:17Z"
---
# Privacy at Scale Roblox's Infrastructure for Honoring User Privacy Rights

**Speakers:** Hao Zhang, Yiwen Luo, Minkyong Kim, Nicole Grinstead  
**Conference:** Black Hat USA 2026  
**Source:** `BlackHat_USA_2026_Slides/Hao Zhang&Yiwen Luo&Minkyong Kim&Nicole Grinstead_Privacy at Scale Roblox's Infrastructure for Honoring User Privacy Rights.pdf` (46 pages)


## Slide 1

### **PRIVACY AT SCALE**

Roblox's Infrastructure for **Honoring** User Privacy Rights

## Slide 2

#### **Who are we**

We build the infrastructure that operationalizes and fulfills user privacy rights at scale — safely, completely, and provably.

**Hao Zhang**

Engineering Manager, Privacy Infrastructure

**Yiwen Luo**

Principal Engineer, Privacy Infrastructure

## Slide 3

#### **Agenda**

**1** Problem Statement

**2** Privacy infrastructure: A Redesigned Federated System

**3** New Experience: Privacy Workflows in Distributed Systems

**4** Security Discussion: Threats, Reliability, and Trade-offs

**5** Future work & Conclusion

## Slide 4

# **01**

**Problem Statement**

The challenge that pushed us to rethink everything.

## Slide 5

###### **PRIVACY RIGHTS SOUND SIMPLE**

Delete me.

Give me a copy.

Correct my record.

**SIMPLE FOR THE USER**

**600 SERVICES**

Chat · Payments · Friends · Marketplace · Safety · Analytics · Voice · Games · Backend Services · Storage · Data Lake · ... AND MORE

**Where does this person's data actually live?**

**ONE REQUEST → HUNDREDS OF SYSTEMS**

Privacy rights are easy to ask for.   They're extremely hard to execute.

## Slide 6

###### **ROBLOX AT SCALE**

**132M**

Daily active users · Q1 2026

**600+** services

**8** storage engines

**THE HARD WORK IS GROWING FASTER**

**~1.6x** YoY user growth   vs.   **~3.5X** YoY privacy request growth

= 1 service / datastore     = Contains personal data (~20%)

SQL · NoSQL · Object Storage · Columnar Warehouse · Key Value · Search Engine · Graph DB · In-Memory Store

**8 STORAGE ENGINES ACROSS THE FLEET**

**THE WORKLOAD OUTRUNS THE PLATFORM.**

## Slide 7

###### **MICROSERVICE SYSTEM, AND IT KEEPS GROWING**

Microservices at scale have complexity by design.

## Slide 8

###### **MICROSERVICE SYSTEM, AND IT KEEPS GROWING**

Microservices at scale have complexity by design.

## Slide 9

###### **MISS ONE, AND IT'S A BREACH**

A deletion request must be executed everywhere.

**…except one.**

**Miss one = a breach.**

## Slide 10

###### **THE MACHINE WE BUILT IS THE ATTACK SURFACE**

**WHAT WE BUILT**

REQUEST → ORCHESTRATION → HANDLER → EXPORT

Same machine. Same request.

**WHAT WE EXPOSED**

REQUEST → ORCHESTRATION → HANDLER → EXPORT

**The same pipeline that protects data can be exploited to abuse it.**

## Slide 11

###### **REGULATORS RAISED THE BAR**

“We tried.”

**USED TO BE ENOUGH**

“Prove it.”

**IS THE NEW STANDARD**

###### **WHAT REGULATORS NOW REQUIRE**

Verifiable Evidence · Complete Audit Trail · Consistent Enforcement · 30-Day Clock · Increasing Scrutiny

**At our scale, you can't produce proof by hand.   Infrastructure is the only way.**

## Slide 12

###### **THE REAL QUESTION**

**THE CHALLENGE**

**600+** internal services

**8** data storage systems

**~3.5x** increase in privacy requests YoY

Payments · Chat · Friends · Voice · Search · Marketplace · Inventory · Analytics · Ads · …

Data Lake · User Profile · Email · Logs · Notifications · Reporting · Safety · Experiment · Storage · …

**How do you coordinate a trustworthy privacy guarantee across over 600 autonomous services?**

**Legacy Systems Reached Their Limits.**   Scale exploded.   Operational burden grew.   Incremental fixes weren't enough.

## Slide 13

# **02**

**Privacy infrastructure:**

**A Redesigned Federated System**

Building the foundation for privacy at scale.

## Slide 14

###### **CENTRALIZE CONTROL FLOW — NOT DATA**

**CENTRALIZED – THE NAIVE MODEL**

Service A · Service B · Service C · … · Service N

ONE ENGINE

data in — bottleneck + single point of failure

**FEDERATED + CENTRAL COORDINATION**

COORD

signals

Service A · Service B · Service C · … · Service N

signals out — each owner acts on its own data

**Only signals flow.**   **Data stays where it belongs.**   **Autonomy remains.**

## Slide 15

###### **FEDERATED OWNERSHIP MODEL**

###### **Privacy Ownership Follows Data Ownership.**

**GAME SVC** — Owns its privacy logic

**CHAT SVC** — Owns its privacy logic

**PAYMENTS SVC** — Owns its privacy logic

**+ 600 SERVICES** — Owns its privacy logic

Therefore, each service should also own:

How user data is deleted · How data is exported · How retention policies are enforced · Downstream dependencies are respected

**PLATFORM**

The central platform does not execute logic directly. Instead, it delegates execution to service-owned privacy handlers.

## Slide 16

###### **CENTRAL ORCHESTRATION, FEDERATED EXECUTION**

**PRIVACY REQUEST** › **1 request → 600+ sub-tasks**

**ORCHESTRATION LAYER**

Temporal workflow engine

Service handler · Service handler · Service handler · Service handler · • • • · + 600 services

**Asynchronous** — Non-blocking by design

**Horizontally Scalable** — Handles growth with ease

**Fault-tolerant** — Retries, timeouts, and recovery built-in

**Fully Traceable** — End-to-end visibility and auditability

## Slide 17

###### **PRIVACY STARTS WITH VISIBILITY**

“where does this user’s data live?” is now **one query.**

`> catalog.locate(user=260805)`

**✓ 7 stores found**

DynamoDB · S3 · Redis · Kafka · Postgres · Elastic · Glacier

**CATALOG SNAPSHOT** · ID: 89f7a2c1

| Field | Value |
|---|---|
| Owner | Game Platform |
| PI fields | User’s email, IP address, geolocation |
| Storage | DynamoDB |
| Retention policy | 7 years |
| Exemptions | No |

**One query. Every location.**   **Full context. Daily, org-wide.**   **Discovery before execution — you can’t delete what you can’t find.**

## Slide 18

###### **DISCOVERY, NOT DELETION.**

**We bet on the wrong hard problem. You cannot automate what you cannot discover.**

Databases · Object Storage · Caches · Search Indexes · Logs · Messaging · Backups · Streams · Analytics · Data Warehouses · Application Data

**Deletion is easy once you know.**   **Discovery is hard and never static.**   **Continuous by design.**   **Better discovery. Stronger guarantees.**

## Slide 19

###### **CLASSIFICATION: ONE DEFINITION, EVERYWHERE**

**Discovery says where.**

**Classification says what it means — the same way, everywhere.**

**ONE TAXONOMY.** One Definition of PI.

game_svc.user.email → PII

chat_svc.profile.email → PII

pay_svc.account.email → PII

**Same field.  Same verdict.  Same way. Every time.**

Consistency · Uniform Enforcement · Trustworthy Automation · Governed & Evolving

## Slide 20

###### **GOVERNANCE AS A PAVED ROAD**

New data appears constantly. Our process keeps coverage near **100%** — and doesn't decay.

new PII store · new service · new field

**AUTO-DISCOVER › CONFIG PR › ONBOARDED**

**COVERAGE THAT STAYS HIGH**

**~100%**

PII DISCOVERY COVERAGE — 100% / 75% / 50% / 25% / 0% · JAN FEB MAR APR MAY JUN

Near 100%. No decay. Governance scales.

**Always Current** · **Self-service by Design** · **Scales With Org Growth** · **Stronger Guarantee**

## Slide 21

# **03**

**New Experience:**

**Privacy Workflows in Distributed Systems**

Making privacy seamless for users and systems.

Request → Process → Fulfill

## Slide 22

###### **A FEDERATED SOLUTION: FOR SCALABILITY**

**METADATA INGESTION (PUBLISH)** → **METADATA CATALOG (MC)** → **AUTO ONBOARDING (PR GENERATION)** → **SERVICE TEAMS (REVIEW & MERGE)** → **SERVICES (WEBHOOK HANDLERS) — FEDERATED**

METADATA CATALOG (MC): Data Ownership · PI Tagging · Service Metadata

SERVICES (WEBHOOK HANDLERS) — FEDERATED: Service A · Service B · Service C · … · Service N (each with RtA, RtBF)

**ORCHESTRATOR**

Workflow Management: Fan-out Requests · Track Execution

Policy & SLA: Enforce SLA

Results Management: Collect Results · Aggregate Status

Execution Status Per Service

**CENTRALIZED AUDIT**

Request Records · Execution Status · Responses & Artifacts · Discrepancies · Compliance Reports

## Slide 23

###### **A FEDERATED SOLUTION: FOR SCALABILITY**

**METADATA INGESTION (PUBLISH)** → **METADATA CATALOG (MC)** → **AUTO ONBOARDING (PR GENERATION)** → **SERVICE TEAMS (REVIEW & MERGE)** → **SERVICES (WEBHOOK HANDLERS) — FEDERATED**

METADATA CATALOG (MC): Data Ownership · PI Tagging · Service Metadata

SERVICES (WEBHOOK HANDLERS) — FEDERATED: Service A · Service B · Service C · … · Service N (each with RtA, RtBF)

## Slide 24

###### **A FEDERATED SOLUTION: FOR SCALABILITY**

**METADATA INGESTION (PUBLISH)** → **METADATA CATALOG (MC)** → **AUTO ONBOARDING (PR GENERATION)** → **SERVICE TEAMS (REVIEW & MERGE)** → **SERVICES (WEBHOOK HANDLERS) — FEDERATED**

METADATA CATALOG (MC): Data Ownership · PI Tagging · Service Metadata

SERVICES (WEBHOOK HANDLERS) — FEDERATED: Service A · Service B · Service C · … · Service N (each with RtA, RtBF)

**ORCHESTRATOR**

Workflow Management: Fan-out Requests · Track Execution

Policy & SLA: Enforce SLA

Results Management: Collect Results · Aggregate Status

Execution Status Per Service

## Slide 25

###### **A FEDERATED SOLUTION: FOR SCALABILITY**

**METADATA INGESTION (PUBLISH)** → **METADATA CATALOG (MC)** → **AUTO ONBOARDING (PR GENERATION)** → **SERVICE TEAMS (REVIEW & MERGE)** → **SERVICES (WEBHOOK HANDLERS) — FEDERATED**

METADATA CATALOG (MC): Data Ownership · PI Tagging · Service Metadata

SERVICES (WEBHOOK HANDLERS) — FEDERATED: Service A · Service B · Service C · … · Service N (each with RtA, RtBF)

**ORCHESTRATOR**

Workflow Management: Fan-out Requests · Track Execution

Policy & SLA: Enforce SLA

Results Management: Collect Results · Aggregate Status

Execution Status Per Service

**CENTRALIZED AUDIT**

Request Records · Execution Status · Responses & Artifacts · Discrepancies · Compliance Reports

## Slide 26

###### **NOBODY WANTS A PRIVACY PLATFORM**

###### **The system disappears into three workflows:**

**Engineers** — Build it. Ship it. Stay fast.

- Plug in a SDK / API
- Use standard libraries and templates
- Get guardrails and defaults out of the box
- Focus on features, not compliance
- **Privacy is built-in. No extra work.**

**Privacy teams** — Operate at scale. Reduce risk.

- Central catalog and inventory
- Policy management and taxonomy
- Monitor coverage and risk in real time
- Drive adoption with self-serve
- **One source of truth. Actionable insights.**

**Compliance** — Prove it. Every time.

- End-to-end audit trails
- Policy enforcement evidence
- Reports in minutes, not weeks
- Regulatory ready, always
- **Provable, repeatable, and audit-ready.**

## Slide 27

###### **FOR ENGINEERS: A FEW LINES, NOT A PROJECT**

Integrate privacy in **minutes.** Not quarters.

Tag your PII · Choose erasure · Choose export · Cover the full footprint · Validated by default

**PR #4213** add privacy integration   +5 −0   ✓ Checks passed

service.yaml

```
120   ...
121 + privacy:
122 +   pii: [email, ip_addr, dob]
123 +   erasure: auto key based deletion        # or: custom_api
124 +   export: spark_sql
125 +   includes: [logs, caches, indexes]
126   ...
```

## Slide 28

###### **FOR PRIVACY TEAMS: OPERATE, DON'T COORDINATE**

From chasing tickets to operating the system.    |    Off the critical path. **In control.**

**BEFORE**

ticket · chase service #1

ticket · chase service #2

ticket · chase service #3

ticket · chase service #4

ticket · chase service #5

ticket · chase service #6

**Manual. Fragmented. You are the bottleneck.**

**AFTER**

**PRIVACY CONSOLE** — Export · Filter · Refresh

RtBF › in progress · on track

RtA › in progress · on track

failures › none stuck · healthy

Services 600+ · Workflows Auto-fanout · SLA On track · Reliability Built-in

**Operate the engine.** Durable, observable, and scalable workflows. Generic webhook contract. Any service can join.

## Slide 29

###### **A REQUEST IS A DISTRIBUTED EXECUTION**

One request. Hundreds of services. Five stages. Fully observable.

**1 Validate** — 2-step MFA

**2 Pre-process** — Fraud · Legal · ATO

**3 Orchestrate** — Register workers

**4 Execute** — Delete or export

**5 Respond** — Archive · RtA only

**End-to-end visibility** · **Built for scale** · **Fault-tolerant** · **Privacy by design** · **Measurable**

## Slide 30

###### **WHAT CHANGED**

**FROM UNKNOWN TO PROVABLE: INCOMPLETE DELETION IS NOW DETECTABLE.**

**COVERAGE NEAR 100% AND DOESN'T DECAY**

**AUDIT EXPOSURE** — BEFORE: Periodic (Sampling) → AFTER: Continuous (Evidence). Always ready. Audit anytime.

**FULFILLMENT TIME** — BEFORE: Days (Often > 3 days) → AFTER: Hours (Often < 24 hrs). Faster for users. Lower operational risk.

**ONBOARDING** — BEFORE: Falling Behind (Manual, ticket-driven) → AFTER: Self-Service (Auto-discovered, self-onboarded). Coverage scales with the organization.

**OPERATIONAL RISK** — BEFORE: Unknown Gaps (Hard to find, easy to miss) → AFTER: Known & Actionable (Every gap is visible). Less risk. More control. Provable compliance.

## Slide 31

###### **FOR COMPLIANCE: PROOF, NOT PROMISES**

From anxiety to evidence. Every request leaves an audit-grade, immutable receipt.

**THE OLD WAY**

- Did we actually comply?
- Email teams
- Assemble spreadsheets
- Days or weeks

From “Did we comply?” to **“Here is the proof.”**

**AUDIT RECEIPT** · request #A7F3-2C · **IMMUTABLE**

| Step | Detail | Status |
|---|---|---|
| type | Right to be Forgotten (erasure) | validated |
| 2-step MFA | | validated |
| checkpoint | fraud · legal · risk — passed | passed |
| executed | 600 services · 0 failures | executed |
| verified | complete — no residual PII | verified |
| signed | 2026-03-14T09:22Z · immutable | |

## Slide 32

# **04**

**Security Discussion:**

**Threats, Reliability, and Trade-offs**

Securing the system while balancing scale and risk.

## Slide 33

###### **ONE REQUEST. FOUR HOPS.**

the machine we built — from the defender's side

**1 REQUEST › 2 ORCHESTRATION › 3 SERVICE HANDLER › 4 EXPORT ARTIFACT**

**Built for protection. Designed for trust.**

## Slide 34

###### **ONE REQUEST. FOUR HOPS.**

the machine we built — from the defender's side

**1 REQUEST › 2 ORCHESTRATION › 3 SERVICE HANDLER › 4 EXPORT ARTIFACT**

**Built for protection. Designed for trust.**

**Same machine. Different intent.**

**ATTACKER VIEW — FOUR SURFACES.**

**1 REQUEST** — Spoof or replay requests.

**2 ORCHESTRATION** — Forge or replay workflow signals to trigger erasure.

**3 SERVICE HANDLER** — Abuse delete/export APIs as a privileged oracle.

**4 EXPORT ARTIFACT** — Harvest RtA archive — a gift-wrapped dossier.

**Every hop is a target. Every target is an opportunity.**

## Slide 35

###### **FOUR WAYS TO WEAPONIZE THE MACHINE**

**Same machine. Different intent. Same mission: protect users and their data.**

**1 WEAPONIZED DELETION**

Attacker hijacks an account → File “delete me” → Erases across 600 services

Hijack an account → “delete me” erases them across 600 services.

**✓ BLOCKED** — ATO signals + step-up MFA

## Slide 36

###### **FOUR WAYS TO WEAPONIZE THE MACHINE**

**Same machine. Different intent. Same mission: protect users and their data.**

**1 WEAPONIZED DELETION**

Attacker hijacks an account → File “delete me” → Erases across 600 services

Hijack an account → “delete me” erases them across 600 services.

**✓ BLOCKED** — ATO signals + step-up MFA

**2 EVIDENCE DESTRUCTION**

Abuse the platform (fraud, harassment, etc.) → Self-delete via RtBF → Fraud trail vanishes

Abuse, then self-delete → the fraud trail vanishes.

**✓ BLOCKED** — Open-investigation holds

## Slide 37

###### **FOUR WAYS TO WEAPONIZE THE MACHINE**

**Same machine. Different intent. Same mission: protect users and their data.**

**1 WEAPONIZED DELETION**

Attacker hijacks an account → File “delete me” → Erases across 600 services

Hijack an account → “delete me” erases them across 600 services.

**✓ BLOCKED** — ATO signals + step-up MFA

**2 EVIDENCE DESTRUCTION**

Abuse the platform (fraud, harassment, etc.) → Self-delete via RtBF → Fraud trail vanishes

Abuse, then self-delete → the fraud trail vanishes.

**✓ BLOCKED** — Open-investigation holds

**3 DATA EXFILTRATION**

Stolen session (high-value account) → Fire “give me a copy” (RtA) → Full PII dossier

A stolen session fires “give me a copy” → a full PII dossier.

**✓ BLOCKED** — Auth + risk checks + scoped buckets + audit

## Slide 38

###### **FOUR WAYS TO WEAPONIZE THE MACHINE**

**Same machine. Different intent. Same mission: protect users and their data.**

**1 WEAPONIZED DELETION**

Attacker hijacks an account → File “delete me” → Erases across 600 services

Hijack an account → “delete me” erases them across 600 services.

**✓ BLOCKED** — ATO signals + step-up MFA

**2 EVIDENCE DESTRUCTION**

Abuse the platform (fraud, harassment, etc.) → Self-delete via RtBF → Fraud trail vanishes

Abuse, then self-delete → the fraud trail vanishes.

**✓ BLOCKED** — Open-investigation holds

**3 DATA EXFILTRATION**

Stolen session (high-value account) → Fire “give me a copy” (RtA) → Full PII dossier

A stolen session fires “give me a copy” → a full PII dossier.

**✓ BLOCKED** — Auth + risk checks + scoped buckets + audit

**4 THE LEGAL-HOLD TRAP**

Account under active investigation → User files “delete me” → Tip them off (or lose evidence)

Delete mid-investigation → destroy evidence, or tip them off.

**✓ BLOCKED** — Legal holds block it silently

## Slide 39

###### **NO SOFT INTERIOR**

**AUTHN / AUTHZ**

Every handler authenticates.

Every orchestration message is signed and scoped.

**IDEMPOTENCY**

Everything retries.

Every action is safe to run twice.

**No double-execution. No partial-state corruption.**

**INTEGRITY**

No over-deletion.

No under-deletion.

**Correct entity. Correct scope.**

## Slide 40

###### **THREE OF FOUR ABUSES STOP AT ONE GATE**

Do the dangerous thinking **ONCE**, at a single preprocessing checkpoint.

REQUEST → **1 VALIDATE** → **CHECKPOINT** (fraud · legal · risk · MFA)

**PROCEED** — Delete or export executes

**HOLD · silent** — Request continues as “in progress”

**THREE ABUSES CONVERGE HERE**

1 Weaponized deletion · 2 Evidence destruction · 4 The legal-hold trap

FRAUD · LEGAL HOLDS · ACCOUNT RISK · MFA / STEP-UP

## Slide 41

###### **EVERY SCALABILITY WIN IS A SECURITY COST**

| SCALABILITY WIN | WHAT WE GAINED | SECURITY COST |
|---|---|---|
| Federated ownership | Horizontal scale, team autonomy, parallel delivery. | Distributed attack surface. |
| Service flexibility | Services choose how to integrate and evolve. | More contracts to validate. |
| Automation speed | High throughput, faster fulfillment. | More to authenticate. |
| Platform scale | Platform grows with users and services. | Larger blast radius. |

## Slide 42

###### **LESSON LEARNED: WHAT WE GOT WRONG FIRST**

**1**

**We orchestrated before we could discover**

Execution is blind without an accurate inventory.

We learned that the hard, embarrassing way.

**2**

**We treated ownership as optional**

If a datastore has no owner, no one is accountable for its privacy posture. Unowned data is where breaches hide.

**3**

**We bolted privacy on downstream**

Privacy can't be a downstream compliance gate. It must live IN the engineering workflow. PR-in-the-repo is why teams actually comply.

###### **TWO MORE WORTH SAYING**

Prefer self-service over central review — queues become bottlenecks. Automation is only as good as your inventory — stale data means errors amplified at scale.

###### **THE BOTTOM LINE**

Good privacy at scale isn't magic. It's inventory, ownership, workflow, and alignment done consistently.

## Slide 43

# **05**

###### **Future work & Conclusion**

Where we're headed and what we've learned.

**Looking Ahead**

**Scaling Impact**

**Continuous Innovation**

**Privacy by Design**

## Slide 44

###### **WHERE THE FRONTIER STILL IS**

###### **Not a roadmap. Open problems. You might be the ones to solve them.**

**STILL HARD — SHADOW DATA**

Systems we don't yet know exist, drifting out of governance.

**STILL HARD — CLASSIFICATION AT SCALE**

Accurate, consistent labeling across genuinely messy storage.

**OPEN — UNIFIED GOVERNANCE**

One control plane across storage, pipelines, analytics — still fragmented today.

**THE ATTACK SURFACE KEEPS GROWING. THE DEFENSE HAS TO KEEP GROWING WITH IT.**

## Slide 45

###### **THE TAKEAWAY**

###### **PRIVACY RIGHTS REQUIRE INFRASTRUCTURE — NOT JUST POLICY.**

That **“Delete me.”** we opened with?   **Now: safe · complete · provable.**

**Can your systems answer these — continuously, by design?**

What data do we have? · Where is it stored? · Who owns it? · How long should it exist?

**A POLICY MAKES A PROMISE.**   **INFRASTRUCTURE KEEPS IT.**

## Slide 46

## **Thank you!**

**PRIVACY AT SCALE**

Roblox's Infrastructure for Honoring User Privacy Rights

**Hao Zhang** — linkedin.com/in/haozhangcs

**Yiwen Luo** — linkedin.com/in/yiwen-luo

Users First · Global Trust · Scalable Impact · Privacy By Design

