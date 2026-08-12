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

**ROBLOX INFOSEC**

## Slide 2

**ROBLOX INFOSEC**

#### **Who are we**

**We build the infrastructure that operationalizes and fulfills user privacy rights at scale — safely, completely, and provably.**

**Hao Zhang Engineering Manager, Privacy Infrastructure**

**Yiwen Luo Principal Engineer, Privacy Infrastructure**

## Slide 3

#### **Agenda**

**1**

**Problem Statement**

- **2 Privacy infrastructure: A Redesigned Federated System**

- **3 New Experience: Privacy Workflows in Distributed Systems**

- **4 Security Discussion: Threats, Reliability, and Trade-offs**

**5 Future work & Conclusion**

## Slide 4

# **01 Problem Statement** The challenge that pushed us to rethink everything.


> Recovered by OCR — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
01
Problem
Statement
The challenge that pushed us
to rethink everything.
```

## Slide 5

###### **PRIVACY RIGHTS SOUND SIMPLE**

Delete me.
Give me a copy.
Correct my record.
SIMPLE FOR THE USER
Privacy rights are easy to ask for. They're extremely hard to execute.

## Slide 6

###### **ROBLOX AT SCALE**

= 1 service / datastore

###### = Contains personal data (~20%)

##### **132M**

Daily active users · Q1 2026

600+ 8
services storage
engines
THE HARD WORK IS GROWING FASTER
~1.6x ~3.5X
YoY privacy request
YoY user growth VS. growth SQL NoSQL Object Columnar Key Search Graph In-Memory
Storage Warehouse Value Engine DB Store
8 STORAGE ENGINES ACROSS THE FLEET

**THE WORKLOAD OUTRUNS THE PLATFORM.**

## Slide 7

###### **MICROSERVICE SYSTEM, AND IT KEEPS GROWING**

Microservices at scale have complexity by design.

$

· · ·

## Slide 8

###### **MICROSERVICE SYSTEM, AND IT KEEPS GROWING**

Microservices at scale have complexity by design.

$

· · ·


> Recovered by OCR — confidence 91/100 on the text kept, 64/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
MICROSERVICE SYSTEM, AND IT KEEPS GROWING
Microservices at scale have complexity by design.
Iv
©
©
oo
© oo
©
S
```

## Slide 9

###### **MISS ONE, AND IT'S A BREACH**

A deletion request must be executed everywhere.

$

**X**

**…except one.**

**Miss one = a breach.**

· · ·

## Slide 10

###### **THE MACHINE WE BUILT IS THE ATTACK SURFACE**

###### **WHAT WE BUILT**

REQUEST ORCHESTRATION HANDLER EXPORT
Same machine. Same request.
WHAT WE EXPOSED
REQUEST ORCHESTRATION HANDLER EXPORT

**The same pipeline that protects data can be exploited to abuse it.**

## Slide 11

###### **REGULATORS RAISED THE BAR**

“
“We tried.”
USED TO BE ENOUGH

“
“Prove it.”
IS THE NEW STANDARD

###### **WHAT REGULATORS NOW REQUIRE**

Verifiable Complete Consistent 30-Day Clock Increasing
Evidence Audit Trail Enforcement Scrutiny

**At our scale, you can't produce proof by hand.   Infrastructure is the only way.**

## Slide 12

###### **THE REAL QUESTION**

THE CHALLENGE
Payments Data Lake
600+ Chat User Profile
Friends Email How do you
internal services
coordinate a
Voice Logs
Search Notifications trustworthy privacy
8
Marketplace Reporting guarantee across over
data storage systems
Inventory Safety 600 autonomous
Analytics Experiment services?
~3.5x
Ads Storage
increase in privacy
requests YoY · · · · · ·
Incremental fixes
Legacy Systems Scale  Operational
Reached Their Limits. exploded. burden grew. weren't enough.

## Slide 13

# **02**

**Privacy infrastructure: A Redesigned Federated System** Building the foundation for privacy at scale.

## Slide 14

###### **CENTRALIZE CONTROL FLOW — NOT DATA**

FEDERATED  +  CENTRAL COORDINATION
Service N
COORD
signals
· · ·
Service A Service B Service C Service N
signals out — each owner
acts on its own data
Data stays where it belongs. Autonomy remains.

CENTRALIZED  –  THE NAIVE MODEL
· · ·
Service A Service B Service C Service N
ONE
ENGINE
data in — bottleneck +
single point of failure
☆
Only signals flow.

## Slide 15

###### **FEDERATED OWNERSHIP MODEL**

###### **Privacy Ownership Follows Data Ownership.**

GAME SVC CHAT SVC PAYMENTS SVC + 600 SERVICES
•••
Owns its Owns its Owns its Owns its
privacy logic privacy logic privacy logic privacy logic
Therefore, each service should also own:
How user data How data is How retention Downstream
is deleted exported policies are enforced dependencies are
respected
The central platform does not execute logic directly.
Instead, it delegates execution to service-owned privacy handlers.

**PLATFORM**

## Slide 16

###### **CENTRAL ORCHESTRATION, FEDERATED EXECUTION**

PRIVACY
1 request  →  600+ sub-tasks
REQUEST
ORCHESTRATION LAYER
Temporal workflow engine
Service Service Service Service • • •
handler handler handler handler + 600
• • •
services
Asynchronous Horizontally Scalable Fault-tolerant Fully Traceable
Non-blocking Handles growth Retries, timeouts, End-to-end visibility
by design with ease and recovery built-in and auditability

## Slide 17

###### **PRIVACY STARTS WITH VISIBILITY**

“where does this user’s data live?” is now **one query.**

ID: 89f7a2c1
> catalog.locate(user=260805) CATALOG SNAPSHOT
7 stores found DynamoDB Owner Game Platform
S3 User’s email,
PI fields
IP address, geolocation
Redis
Kafka Storage DynamoDB
Postgres
Retention policy 7 years
Elastic
Glacier Exemptions No
One query. Full context. Discovery before execution —
Every location. Daily, org-wide.
you can’t delete what you can’t find.

## Slide 18

**DISCOVERY, NOT DELETION.**

**We bet on the wrong hard problem. You cannot automate what you cannot discover.**

**Deletion is easy Discovery is hard once you know. and never static.**

**Continuous by design.**

**Better discovery. Stronger guarantees.**

## Slide 19

###### **CLASSIFICATION: ONE DEFINITION, EVERYWHERE**

Discovery says where.
game_svc.user. email PII
Classification says
what it means —
chat_svc.profile. email PII
the same way,
everywhere.
pay_svc.account. email PII
Same field.  Same verdict.  Same way.
ONE TAXONOMY.
Every time.
One Definition of PI.
Uniform  Trustworthy
Consistency Governed & Evolving
Enforcement Automation

## Slide 20

###### **GOVERNANCE AS A PAVED ROAD**

New data appears constantly. Our process keeps coverage near **100%** — and doesn't decay.

new PII store

new service

new field

**COVERAGE THAT STAYS HIGH**

**~100%**

AUTO-DISCOVER

CONFIG PR

ONBOARDED

PII DISCOVERY COVERAGE
100%
75%
50%
25%
0%
JAN FEB MAR APR MAY JUN
Near 100%. No decay.
Governance scales.

**Always Current**

**Self-service by Design**

**Scales With Org Growth**

**Stronger Guarantee**

## Slide 21

**03 New Experience: Privacy Workflows in Distributed Systems** Making privacy seamless for users and systems.


> Recovered by OCR — confidence 95/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
03
New Experience:
Privacy Workflows
in Distributed Systems
Making privacy seamless
for users and systems.
```

## Slide 22

###### **A FEDERATED SOLUTION: FOR SCALABILITY**

METADATA METADATA CATALOG (MC) AUTO ONBOARDING SERVICE TEAMS SERVICES (WEBHOOK HANDLERS) — FEDERATED
INGESTION (PUBLISH) (PR GENERATION) (REVIEW & MERGE) Service A Service B Service C Service N
Data Ownership
PI Tagging ...
Service Metadata RtA RtBF RtA RtBF RtA RtBF RtA RtBF
ORCHESTRATOR
Workflow Management Policy & SLA Results Management Execution Status
Per Service
Fan-out Track Enforce Collect Aggregate
Requests Execution SLA Results Status
CENTRALIZED AUDIT
Request Execution Responses  Compliance
Discrepancies
Records Status & Artifacts Reports

## Slide 23

###### **A FEDERATED SOLUTION: FOR SCALABILITY**

METADATA METADATA CATALOG (MC) AUTO ONBOARDING SERVICE TEAMS SERVICES (WEBHOOK HANDLERS) — FEDERATED
INGESTION (PUBLISH) (PR GENERATION) (REVIEW & MERGE) Service A Service B Service C Service N
Data Ownership
PI Tagging ...
Service Metadata RtA RtBF RtA RtBF RtA RtBF RtA RtBF

## Slide 24

###### **A FEDERATED SOLUTION: FOR SCALABILITY**

METADATA METADATA CATALOG (MC) AUTO ONBOARDING SERVICE TEAMS SERVICES (WEBHOOK HANDLERS) — FEDERATED
INGESTION (PUBLISH) (PR GENERATION) (REVIEW & MERGE) Service A Service B Service C Service N
Data Ownership
PI Tagging ...
Service Metadata RtA RtBF RtA RtBF RtA RtBF RtA RtBF
ORCHESTRATOR
Workflow Management Policy & SLA Results Management Execution Status
Per Service
Fan-out Track Enforce Collect Aggregate
Requests Execution SLA Results Status

## Slide 25

###### **A FEDERATED SOLUTION: FOR SCALABILITY**

METADATA METADATA CATALOG (MC) AUTO ONBOARDING SERVICE TEAMS SERVICES (WEBHOOK HANDLERS) — FEDERATED
INGESTION (PUBLISH) (PR GENERATION) (REVIEW & MERGE) Service A Service B Service C Service N
Data Ownership
PI Tagging ...
Service Metadata RtA RtBF RtA RtBF RtA RtBF RtA RtBF
ORCHESTRATOR
Workflow Management Policy & SLA Results Management Execution Status
Per Service
Fan-out Track Enforce Collect Aggregate
Requests Execution SLA Results Status
CENTRALIZED AUDIT
Request Execution Responses  Compliance
Discrepancies
Records Status & Artifacts Reports

## Slide 26

###### **NOBODY WANTS A PRIVACY PLATFORM**

###### **The system disappears into three workflows:**

Engineers Privacy teams Compliance
Build it. Ship it. Stay fast. Operate at scale. Reduce risk. Prove it. Every time.
Plug in a SDK / API Central catalog and inventory End-to-end audit trails
Use standard libraries Policy management Policy enforcement evidence
and templates and taxonomy
Get guardrails and defaults Monitor coverage and risk Reports in minutes,
out of the box in real time not weeks
Focus on features, Drive adoption Regulatory ready,
not compliance with self-serve always
Privacy is built-in. One source of truth. Provable, repeatable,
No extra work. Actionable insights. and audit-ready.

## Slide 27

###### **FOR ENGINEERS: A FEW LINES, NOT A PROJECT**

###### Integrate privacy in **minutes.** Not quarters.

+5  −0
PR #4213 add privacy integration Checks passed
service.yaml
120 ...
121 + privacy:
122 +   pii: [email, ip_addr, dob]
123 +   erasure: auto key based deletion        # or: custom _ api
124 +   export: spark_sql
125 +   includes: [logs, caches, indexes]
126 ...

Tag your PII

Choose erasure

Choose export 122
123
124
Cover the full footprint
125
126
Validated by default

## Slide 28

###### **FOR PRIVACY TEAMS: OPERATE, DON'T COORDINATE**

From chasing tickets to operating the system.    |    Off the critical path. **In control.**

BEFORE AFTER
PRIVACY CONSOLE
ticket · chase service #1
Export Filter Refresh
ticket · chase service #2 RtBF › in progress on track
ticket · chase service #3
RtA › in progress on track
ticket · chase service #4
failures › none stuck healthy
ticket · chase service #5
Services Workflows SLA Reliability
600+ Auto-fanout On track Built-in
ticket · chase service #6
Manual.  Fragmented. You are the  Operate the engine.  Durable, observable, and scalable workflows.
bottleneck.
Generic webhook contract. Any service can join.

## Slide 29

###### **A REQUEST IS A DISTRIBUTED EXECUTION**

One request. Hundreds of services. Five stages. Fully observable.

**1**

###### **Validate**

**2**

**Pre-process**

**3**

**Orchestrate**

**4**

**Execute**

**5** **Respond**

**2-step MFA Fraud · Legal · ATO Register workers**

**Delete or export**

**Archive · RtA only**

**End-to-end visibility**

**Built for scale**

**Fault-tolerant**

**Privacy by design**

**Measurable**

## Slide 30

###### **WHAT CHANGED**

**FROM UNKNOWN TO PROVABLE: INCOMPLETE DELETION IS NOW DETECTABLE.**

COVERAGE NEAR
100%
AND DOESN'T DECAY

AUDIT EXPOSURE FULFILLMENT TIME ONBOARDING OPERATIONAL RISK
BEFORE AFTER BEFORE AFTER BEFORE AFTER BEFORE AFTER
Periodic Continuous Days Hours Falling Behind Self-Service Unknown Gaps Known &
Actionable
Sampling Evidence Often > 3 days Often < 24 hrs Manual, Auto-discovered, Hard to find, Every gap
ticket-driven self-onboarded easy to miss is visible
Always ready. Audit anytime. Faster for users. Coverage scales with Less risk. More control.
Lower operational risk. the organization. Provable compliance.

## Slide 31

###### **FOR COMPLIANCE: PROOF, NOT PROMISES**

From anxiety to evidence. Every request leaves an audit-grade, immutable receipt.

|**THE OLD WAY**|**AUDIT RECE**|**IPT**·   request #A7F3-2C|**IMMUTABLE**|
|---|---|---|---|
|**Did we actually comply?**||||
||**type**|Right to be Forgotten (erasure)|**validated**|
|**Email teams**|**2-step MFA**||**validated**|
|**Assemble spreadsheets**|**checkpoint**|fraud · legal · risk — passed|**passed**|
|**Days or weeks**|**executed**|600 services · 0 failures|**executed**|
||**verified**|complete — no residual PII|**verified**|
|From “Did we comply?”||||
|to**“Here is the proof.”**|**signed**|2026-03-14T09:22Z · immutable||

## Slide 32

**04 Security Discussion: Threats, Reliability, and Trade-offs**

Securing the system while balancing scale and risk.


> Recovered by OCR — confidence 96/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
04
Security Discussion:
Threats, Reliability,
and Trade-offs
Securing the system while
balancing scale and risk.
```

## Slide 33

###### **ONE REQUEST. FOUR HOPS.**

the machine we built — from the defender's side

1 2 3 4
› › ›
REQUEST ORCHESTRATION SERVICE EXPORT
HANDLER ARTIFACT

Built for protection.
Designed for trust.

## Slide 34

###### **ONE REQUEST. FOUR HOPS.**

the machine we built — from the defender's side

**1 REQUEST**

**ATTACKER VIEW FOUR SURFACES.**

**2 3 4 › › ›** **ORCHESTRATION SERVICE EXPORT HANDLER ARTIFACT** **Same machine. Different intent. 1 2 3 4 › › › REQUEST ORCHESTRATION SERVICE EXPORT HANDLER ARTIFACT** Spoof or replay Forge or replay workflow Abuse delete/export APIs Harvest RtA archive — requests. signals to trigger erasure. as a privileged oracle. a gift-wrapped dossier.

**Same machine. Different intent.**

**Built for protection. Designed for trust.**

**Every hop is a target. Every target is an opportunity.**

## Slide 35

###### **FOUR WAYS TO WEAPONIZE THE MACHINE**

**Same machine. Different intent. Same mission: protect users and their data.**

**1 WEAPONIZED DELETION**

File “delete me”

Attacker hijacks File “delete me” Erases across an account 600 services

Hijack an account → “delete me” erases them across 600 services. ✓ ATO signals + **BLOCKED** step-up MFA

## Slide 36

###### **FOUR WAYS TO WEAPONIZE THE MACHINE**

**Same machine. Different intent. Same mission: protect users and their data.**

**1 WEAPONIZED DELETION**

File “delete me”

Attacker hijacks an account

Erases across 600 services

**2 EVIDENCE DESTRUCTION** Abuse the platform Self-delete via Fraud trail (fraud, harassment, etc.) RtBF vanishes

Hijack an account → “delete me” erases them across 600 services.

Abuse, then self-delete → the fraud trail vanishes.

✓ ATO signals + **BLOCKED** step-up MFA

✓ Open-investigation **BLOCKED** holds

## Slide 37

###### **FOUR WAYS TO WEAPONIZE THE MACHINE**

**Same machine. Different intent. Same mission: protect users and their data.**

**1 WEAPONIZED DELETION**

File “delete me”

Attacker hijacks an account

Erases across 600 services

**2 EVIDENCE DESTRUCTION** Abuse the platform Self-delete via Fraud trail (fraud, harassment, etc.) RtBF vanishes

Hijack an account → “delete me” erases them across 600 services.

Abuse, then self-delete → the fraud trail vanishes.

✓ ATO signals + **BLOCKED** step-up MFA

✓ Open-investigation **BLOCKED** holds

**3 DATA EXFILTRATION** Stolen session Fire “give me Full PII (high-value account) a copy” (RtA) dossier A stolen session fires “give me a copy” → a full PII dossier.

Stolen session Fire “give me Full PII (high-value account) a copy” (RtA) dossier A stolen session fires “give me a copy” → a full PII dossier. ✓ Auth + risk checks **BLOCKED** + scoped buckets + audit

## Slide 38

###### **FOUR WAYS TO WEAPONIZE THE MACHINE**

**Same machine. Different intent. Same mission: protect users and their data.**

**1 WEAPONIZED DELETION**

File “delete me”

Attacker hijacks an account

Erases across 600 services

**2 EVIDENCE DESTRUCTION** Abuse the platform Self-delete via Fraud trail (fraud, harassment, etc.) RtBF vanishes

Hijack an account → “delete me” erases them across 600 services.

Abuse, then self-delete → the fraud trail vanishes.

✓ ATO signals + **BLOCKED** step-up MFA

✓ Open-investigation **BLOCKED** holds

**3 DATA EXFILTRATION** Stolen session Fire “give me (high-value account) a copy” (RtA)

Full PII dossier

A stolen session fires “give me a copy” → a full PII dossier.

**4 THE LEGAL-HOLD TRAP** Account under active User files Tip them off investigation “delete me” (or lose evidence) Delete mid-investigation → destroy evidence, or tip them off.

✓ Auth + risk checks **BLOCKED** + scoped buckets + audit

✓ **BLOCKED**

Legal holds block it silently

## Slide 39

###### **NO SOFT INTERIOR**

AUTHN / AUTHZ IDEMPOTENCY INTEGRITY
Every handler
Everything retries. No over-deletion.
authenticates.
Every orchestration  Every action is safe No under-deletion.
message to run twice.
is signed and scoped.
No double-execution. Correct entity.
No partial-state corruption. Correct scope.

## Slide 40

###### **THREE OF FOUR ABUSES STOP AT ONE GATE**

Do the dangerous thinking **ONCE** , at a single preprocessing checkpoint.

PROCEED
Delete or export
executes
1
VALIDATE
HOLD  · silent
REQUEST
CHECKPOINT Request continues
as “in progress”
fraud · legal · risk · MFA
THREE ABUSES CONVERGE HERE FRAUD
LEGAL HOLDS
Weaponized Evidence The legal-hold ACCOUNT RISK
1 2 4
deletion destruction trap
MFA / STEP-UP

## Slide 41

###### **EVERY SCALABILITY WIN IS A SECURITY COST**

SCALABILITY WIN WHAT WE GAINED SECURITY COST
Horizontal scale, team
Federated ownership Distributed attack surface.
autonomy, parallel delivery.
Services choose how
Service flexibility More contracts to validate.
to integrate and evolve.
High throughput,
Automation speed faster fulfillment. More to authenticate.
Platform grows with
Platform scale users and services. Larger blast radius.

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

STILL HARD STILL HARD OPEN
SHADOW DATA CLASSIFICATION AT SCALE UNIFIED GOVERNANCE
Systems we don't yet know Accurate, consistent labeling One control plane across
exist, drifting out of across genuinely messy storage, pipelines, analytics —
governance. storage. still fragmented today.

**THE ATTACK SURFACE KEEPS GROWING. THE DEFENSE HAS TO KEEP GROWING WITH IT.**

## Slide 45

###### **THE TAKEAWAY**

###### **PRIVACY RIGHTS REQUIRE INFRASTRUCTURE — NOT JUST POLICY.**

That **“Delete me.”** we opened with?

**Now: safe · complete · provable.**

**Can your systems answer these — continuously, by design?**

**What data Where is it do we have? stored?**

**Who owns How long should it? it exist?**

**A POLICY MAKES A PROMISE.**

**INFRASTRUCTURE KEEPS IT.**

## Slide 46

Users First
Privacy By Design

Users First
Privacy By Design Global Trust

## **Thank you!**

**PRIVACY AT SCALE** Roblox's Infrastructure for Honoring User Privacy Rights

**Hao Zhang Yiwen Luo** linkedin.com/in/haozhangcs linkedin.com/in/yiwen-luo

Scalable Impact
