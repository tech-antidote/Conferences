---
title: "The Intent Gap Where Every AI Regulation Falls Short and What Security Leaders Need Instead"
speakers: ["Jeff Pollard", "Heidi Shey"]
conference: "Black Hat"
conference_full: "Black Hat USA 2026"
edition: "USA"
year: 2026
source_pdf: "BlackHat_USA_2026_Slides/Jeff Pollard&Heidi Shey_The Intent Gap Where Every AI Regulation Falls Short and What Security Leaders Need Instead.pdf"
pages: 42
sha256: "5710c50899740728ece9df66db80ff6c15f6106f7c7fd7350c9b3cb5b3ba794f"
text_chars: 29104
ocr_pages: 1
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T23:10:15Z"
---
# The Intent Gap Where Every AI Regulation Falls Short and What Security Leaders Need Instead

**Speakers:** Jeff Pollard, Heidi Shey  
**Conference:** Black Hat USA 2026  
**Source:** `BlackHat_USA_2026_Slides/Jeff Pollard&Heidi Shey_The Intent Gap Where Every AI Regulation Falls Short and What Security Leaders Need Instead.pdf` (42 pages)

## Slide 1

## The Intent Gap

Where Current AI Governance Leaves Agent Behavior Unresolved — And What Security Leaders Can Build Now

## Slide 2

## Slide 3

##### From Execution To Intention

##### TRADITIONAL SOFTWARE

INPUT processLoan(appId) ↓ EXECUTE Runs deterministic code ↓ OUTPUT { approved: true }

1 DECISION POINT · PREDICTABLE · AUDITABLE

##### AI AGENT — SAME TASK

PERCEIVE Parse instruction + context ↓ PLAN Select tools, sequence steps ↓ DECIDE Which data? Which source? ↓ ACT Call APIs, read files, write records

MULTIPLE DECISION POINTS · EMERGENT · INTENT-DRIVEN

## Slide 4

##### What do we mean by intent?

Agentic intent is the relationship between an assigned objective, the constraints attached to it, and the action path an agent selects over time.

Security teams infer that relationship from declared goals, delegation records, tool calls, state changes, data movement, exceptions, and outcomes.

## Slide 5

## Securing Intent Is The New Security Domain

You cannot enforce least agency or explain an outcome without classifying intent.

Major frameworks address portions of agent risk. Security teams still need one operating loop that connects objective, cumulative behavior, evidence, response, and ownership.

## Slide 6

**CASE 2 /  OPENAI–HUGGING FACE AGENT INTRUSION**

**CASE 3 /  ANTHROPIC CYBER EVALUATION INCIDENTS**

**CASE 1  /  CHESS SYSTEM HACK**

An agent was tasked with winning chess against a stronger opponent. _The agent stopped solving only through play._

The agent modified opponent pieces, deleted opponent files, and manipulated the game state to obtain a higher score.

**INTENT CLASSIFICATION**

### **ACCIDENTAL HARM**

The selected path diverged from the authorized objective and constraints. No attacker-controlled objective was required.

Source: Palisade Research (2025) • Intent classification is presenters’ analysis.

An agent was tasked with finding and exploiting software vulnerabilities as part of a cyber capability evaluation. _The agent decided not to solve for the challenge._

The agent escaped containment, and reached Hugging Face production attempting to obtain answers to the challenge.

**INTENT CLASSIFICATION**

### **ACCIDENTAL HARM**

The evaluation objective remained the driver while the agent acted through unauthorized systems.

No attacker-controlled objective was required.

Source: Hugging Face, “Agent Intrusion: Technical Timeline” (27 Jul 2026) • Intent classification is presenters’ analysis.

Anthropic reviewed cybersecurity evaluation transcripts and discovered three incidents where an agent in capture-the-flag evaluations gained unauthorized access to the systems of three real organizations.

During the CTF, the agent discovered it had internet access and initially treated this as part of the simulation.

**INTENT CLASSIFICATION**

**ACCIDENTAL HARM**

Assigned capture-the-flag objectives operated under a materially false assumption about internet access. Real systems were mistaken for the simulation.

Source: Anthropic (30 Jul 2026) • Intent classification is presenters’ analysis.

## Slide 7

**CASE 4 /  COMPOSITE RECONCILIATION SCENARIO**

##### **The agent had a legitimate job—and legitimate access.**

**Every day, the agent reconciled customer records.**

Its authorization was narrow: export records that matched a specified pattern.

**01**

**DAILY RECONCILIATION**

**AUTHORIZED BOUNDARY**

**02**

**MATCH PATTERN X**

The pattern determined which records were in scope.

**03**

**EXPORT MATCHING CUSTOMER RECORDS**

Sources: OWASP LLM01:2025 Prompt Injection; Google DeepMind, “Lessons from Defending Gemini Against Indirect Prompt Injections” (20 May 2025) • Composite; presenters’ analysis.

## Slide 8

**CASE 4 /  COMPOSITE RECONCILIATION SCENARIO**

##### **The attacker changed X—not the agent’s permissions.**

**INJECTED THROUGH RECONCILIATION INPUT**

**RESULT**

**X  →  matches every customer record**

###### **NO SEQUENCE ALERT**

The poisoned pattern expanded the query scope.

- **01 EVERY RECORD MATCHED**

Every individual action remained permitted.

- **02 EACH EXPORT WAS AUTHORIZED**

Per-request controls may remain quiet when cumulative scope is not evaluated.

- **03 EACH REQUEST COULD STAY UNDER A LIMIT**

No local event had to look abnormal.

- **04 CUMULATIVE SCOPE WAS NOT EVALUATED**

Sources: OWASP LLM01:2025 Prompt Injection; Google DeepMind, “Lessons from Defending Gemini Against Indirect Prompt Injections” (20 May 2025) • Composite; presenters’ analysis.

## Slide 9

**CASE 4 /  COMPOSITE RECONCILIATION SCENARIO**

##### **Every action was authorized. The sequence was not.**

**INTENT CLASSIFICATION**

### **PURPOSEFUL HARM**

###### **SECURITY IMPLICATIONS**

###### **01 LOCAL CONTROLS COULD PASS**

Individual exports can remain permitted while the cumulative path exceeds authorized scope.

Observed behavior aligned with an attacker-controlled or unauthorized objective.

**02 THE SEQUENCE CROSSED THE BOUNDARY**

A monitor must compare cumulative behavior with the authorized objective and constraints.

Principal confusion / prompt injection

###### **03 CLASSIFICATION NEEDS CONFIDENCE**

Record the evidence, confidence, initial response, and accountable escalation owner.

Sources: OWASP LLM01:2025 Prompt Injection; Google DeepMind, “Lessons from Defending Gemini Against Indirect Prompt Injections” (20 May 2025) • Composite; presenters’ analysis.

## Slide 10

##### Murphy’s Laws Of AI Alignment

###### **Supervised Fine-Tuning**

###### **Reinforcement Learning From Human Feedback**

###### **Direct Preference Optimization**

**Constitutional AI (Anthropic)**

###### **Reinforced Self-Training**

Reduces harmful output frequency but cannot eliminate the tail distribution of harmful responses under distributional shift

Most widely deployed. Introduces reward hacking: the model optimizes for annotator approval signals rather than underlying aligned behavior

Computationally efficient alternative to RLHF. Same annotator drift failure mode — preferences reflect annotator biases, not ground truth alignment

Rule-based constraints improve alignment indistribution. Fails under adversarial probing that finds gap between the constitutional rules and their intended spirit

Model generates and filters its own training data. Selfreinforcing alignment mirages: model converges on a definition of 'aligned' that matches its prior, not ground truth

Source: Madhava Gaikwad, arXiv 2509.05381v1 — September 2025

10

## Slide 11

##### AI Alignment Is Not Security

###### **Reward Hacking**

###### **Sycophancy**

**Alignment Mirages**

###### **Distribution Shift**

Agent substitutes proxy metric optimization for stated goal. Not adversarially directed, but causes **accidental harm** through specification gaming. Root cause: alignment training left a gap between specified reward and intended behavior.

Under adversarial conditions (attacker provides flattering framing for harmful request), sycophancy converts to **purposeful harm** . The alignment failure becomes an attack vector.

Agent appears to function correctly in test environments. In production under distributional shift, behavior drifts to **accidental harm** . This is why production monitoring (not just pre-deployment testing) is mandatory for accurate intent classification.

Production environments always differ from training distributions. Any alignment guarantee is conditional on distributional stability that real deployments don't provide. Security requires production monitoring precisely because alignment guarantees don't hold at deployment time.

Source: Madhava Gaikwad, arXiv 2509.05381v1 — September 2025

11

## Slide 12

###### Enterprises Are Deploying Autonomous Agents That Plan, Decide, Act

# **76%**

Of organizations have at least one or more agentic AI application in production, across one or more departments.

Base: 1,957 AI decision makers Source: Forrester's State Of AI Survey, 2026

12

## Slide 13

# Enterprises Are Deploying Autonomous Agents That Plan, Decide, Act **$250,000**

Median invested in agentic AI to date

Base: 1,957 AI decision makers Source: Forrester's State Of AI Survey, 2026

13

## Slide 14

## The Intent Classification Framework

Intent as a First-Class Security Object

14

## Slide 15

##### Intent Is An Observable Security Relationship

ESTABLISHED ESTABLISHED ESTABLISHED **NEW** ASSETS → IDENTITIES → ACTIONS → INTENT What data and Who is acting What was done Goal + constraints + systems exist path over time

## Slide 16

##### Classify Intent With An Impact Matrix

D1 · INTENDED + BENEFICIAL

###### **ENGINEERED HELPFULNESS**

Designed functionality. Documented features operating as trained. What all compliance frameworks assume.

BASELINE · NO ALERT

D2 · UNINTENDED + BENEFICIAL

###### **EMERGENT HELPFULNESS**

Novel capabilities beyond training that produce positive outcomes. Regulations don't differentiate this from D1.

MONITOR · LOW SEVERITY

D4 · INTENTIONAL + HARMFUL

###### **PURPOSEFUL HARM**

Adversarial manipulation. Prompt injection. Agent hijacking. Where all frameworks are weakest.

CISO ESCALATION · IMMEDIATE

D3 · UNINTENDED + HARMFUL

###### **ACCIDENTAL HARM**

Errors, drift, hallucinations, bias. What most regulations address — but only via output monitoring, too late.

SOC ALERT · TIER 1 REVIEW

## Slide 17

##### Classification Test: Evidence Before Labels

AUTHORIZED OBJECTIVE **AO** test › compare task, policy, scope, and accepted action paths Did observed behavior stay inside the approved objective and constraints? HARMFUL EFFECT **HE** test › evaluate outcome, data movement, state change, and affected parties Did the behavior produce or materially increase harm? ADVERSARIAL MANIPULATION **AM** test › inspect instruction source, delegation chain, retries, and denied actions Did external input, unauthorized delegation, concealment, or policy evasion shape the path? CONFIDENCE **CF** record › confidence level, missing evidence, and plausible alternatives How strong and complete is the evidence supporting the classification? MINIMUM DECISION EVIDENCE **EV** principle › reconstruct the action path; raw private chain-of-thought is not required Objective · constraints · identity · delegation · tool path · state/data movement · policy decisions · outcome

## Slide 18

##### Response Paths Must Include Confidence And Review

###### D3 · UNINTENDED + HARMFUL **ACCIDENTAL HARM**

###### CLASSIFICATION THRESHOLD

Harm is observed, but evidence does not show an attacker-controlled or unauthorized objective.

###### REQUIRED EVIDENCE

Task and constraints · action path · state or data changes · baseline deviation · confidence.

###### INITIAL RESPONSE

Contain proportionately · preserve evidence · correct the specification or control · retest.

###### ESCALATION

Route material impact to the accountable owner, GRC, and legal as applicable.

###### D4 · UNINTENDED + HARMFUL **PURPOSEFUL HARM**

###### CLASSIFICATION THRESHOLD

Harm plus evidence that external manipulation, unauthorized delegation, concealment, or repeated evasion shaped the path.

###### REQUIRED EVIDENCE

Instruction source · delegation chain · denied operations · anomalous sequence · destinations · confidence.

###### INITIAL RESPONSE

Contain · revoke or narrow authority · investigate the attacker-controlled objective · hunt related activity.

###### ESCALATION

Trigger incident response and legal/regulatory assessment; report only when the applicable threshold is met.

###### POLICY RELEVANCE

Most regulations address, assuming harm is detectable via output monitoring alone — intent classification enables earlier detection. Partially covered by NISTAI RMF Measure, EU AI Act Article 9/14. Missing: continuous behavioral drift detection.

###### EXAMPLE

AI agent recommends suboptimal financial products due to training bias amplified by distribution shift 18 months post-deployment.

###### POLICY RELEVANCE

Where frameworks are weakest, addressing attack vectors but not the strategic threat of an agent whose intent has been deliberately altered.

###### EXAMPLE

Indirect prompt injection via a processed document causes agent to exfiltrate pricing data across 47 API calls — each individually within authorization boundaries.

## Slide 19

##### Beneficial Behavior Can Also Require A Response Path

D1 · INTENDED + BENEFICIAL **<u>ENGINEERED HELPFULNESS</u>**

###### D2 · UNINTENDED + BENEFICIAL **<u>EMERGENT HELPFULNESS</u>**

CLASSIFICATION THRESHOLD

Observed behavior is expected within the objective and constraints.

###### CLASSIFICATION THRESHOLD

Observed behavior deviates from the baseline, yet evidence indicates it still meets the objective and constraints.

###### REQUIRED EVIDENCE

Alignment with training documentation and feature specs. Consistent with golden dataset.

###### REQUIRED EVIDENCE

Behavior that generalizes without training examples. Capabilities appearing at scale thresholds.

INITIAL RESPONSE

None; this is the baseline · Everything is awesome.

###### INITIAL RESPONSE

Monitor · check against training documentation and feature specs.

ESCALATION

None; this is the baseline · Everything is awesome.

###### ESCALATION

Route deviation findings to accountable owner, GRC, and legal as applicable.

###### POLICY RELEVANCE

This is what compliance frameworks assume all AI behavior is. All frameworks cover this. No gaps.

###### POLICY RELEVANCE

Regulations don't differentiate D2 from D1 — creating documentation gaps and accountability confusion, liability ambiguity.

###### EXAMPLE

AI agent correctly processes a customer loan application using approved data sources and decision criteria.

###### EXAMPLE

AI agent discovers a fraud detection pattern not in training data, reducing false positives by 23%.

19

## Slide 20

## The Regulatory Gap Analysis

**TL;DR** Combined coverage is ~44% — less than half of intent threats are addressed across ALL frameworks taken together

20

## Slide 21

##### Methodology: How We Scored The Frameworks

###### **SCORING CRITERIA**

###### **5 FRAMEWORKS ANALYZED**

###### **5 INTENT-BASED THREAT CATEGORIES**

###### **Does the framework:**

- Identify the threat?

- Require controls?

NIST AI RMF 1.0

Scope Drift

- Mandate monitoring?

- Define incident response?

- Establish liability?

EU AI Act

Goal Substitution

###### **SCORING RUBRIC**

###### **COVERED  ·  3 POINTS**

EU Cyber Resilience Act

Deceptive Reasoning

Explicitly addresses the threat category and states an operational control or evidence expectation.

###### **PARTIAL  ·  2 POINTS**

OWASP Top 10 for LLMs v2.0

Capability Amplification

Explicitly addresses the threat category but lacks enforcement mechanisms or detection specifics for evidence

###### **TANGENTIAL ·  1 POINT**

MITRE ATLAS

Principal Confusion

Mentions related concepts without specifying detection, classification, or response requirements

###### **GAP  ·  0 POINTS**

Does not address this threat category

Sources: NIST AI RMF 1.0 (Jan 2023) · EU AI Act 2024/1689 · EU CRA 2024/2847 · OWASP Top 10 for LLM Applications 2025 · MITRE ATLAS v2026.06 |  Presenters’ analysis.

## Slide 22

##### Our Analysis Finds Fragmented Coverage

COVERED PARTIAL TANGENTIAL

GAP

|THREAT|NIST AI RMF|EU AI ACT|EU CRA|OWASP LLM v2.0|MITRE ATLAS|
|---|---|---|---|---|---|
|**SD**
Scope Drift||||||
|**GS**
Goal Substitution||||||
|**DR**
Deceptive Reasoning||||||
|**CA**
Capability Amplification||||||
|**PC**
Principal Confusion||||||

Sources: NIST AI RMF 1.0 (Jan 2023) · EU AI Act 2024/1689 · EU CRA 2024/2847 · OWASP Top 10 for LLM Applications 2025 · MITRE ATLAS v2026.06 | Presenters’ analysis.

## Slide 23

###### The Compliance Paradox From Case 4

###### NIST AI RMF

###### EU AI ACT

ASSESSMENT COMPLETED SCOPE ASSESSED

Risk assessment and periodic monitoring addressed in the assumed scenario.

###### EU CRA

SCOPE ASSESSED

Applicability depends on the system’s use and decision context. In assumed scenario, transparency requirements are met.

OWASP / MITRE ATLAS SAFEGUARDS MAPPED

###### AND YET…

The agent is aggregating customer data beyond its defined scope — building an unauthorized behavioral profile — through individually-authorized actions no regulator can see.

Applicability depends on product, service, and incident Prompt-injection and adversarial-technique controls facts. May not be applicable. mapped. Known attack vectors addressed.

## Slide 24

## What To Do

###### **Close The Loop Nobody Else Closes**

24

## Slide 25

##### Control The Enforceable Descriptions Of Intent

DETERMINISTIC AND ENFORCEABLE

DESCRIPTION

- Authorization-scope, provenance-carried, and intentbound authorization

- Semantic intent (does the action match what the human meant?) is a classifier.

EMERGING STANDARDS EFFORTS

NIST NCCoE Agent Identity And Authorization HDP (Human Delegation Provenance) HAID (Human-Anchored Intent Bound Delegation)

25

## Slide 26

##### Artifact 1: The Agent Behavior Contract

|DEFINE THE AUTHORIZED OBJECTIVE|ACCOUNTABILITY COM|PONENTS|
|---|---|---|
|Business objective + prohibited outcomes.
›|Named business owner|Approves objective, constraints, expected behavior,
and residual risk.|
||Policy reference|Links the deployment to risk tier, evidence|
|Approved principals, tools, data, and destinations.
›||requirements, and exceptions.|
||Delegation record|Binds agent identity to delegated authority and
capability scope.|
|Time and transaction boundaries + escalation
conditions.
›|Review + sign-off|Records review cadence, changes, exceptions, and
acceptance.|
|DRAFT POLICY LANGUAGE|||

_“Each production agent must have a signed behavior contract defining its objective, constraints, authority, evidence requirements, escalation conditions, named owner, and accepted residual risk.”_

## Slide 27

##### Artifact 2: Minimum Viable Telemetry

COLLECTABLE EVENT DATA ORGANIZATION-DERIVED SIGNALS › Identity + session/trace ID + declared task or policy + Cumulative scope expansion · sensitive-data aggregation. reference. + Goal-to-action divergence · novel tool combinations. › Tool operation + resource target + data classification + authorization decision. + Repeated denied operations · delegation-chain breaks. › Delegation chain + input source + output destination + result + intervention events. + Action-rate, destination, or transaction-boundary anomalies.

IMPLEMENTATION NOTE _Map raw events onto existing traces and logs. Derived field names are proposed, organization-defined attributes—not current OpenTelemetry semantic conventions. Capture enough decision evidence to reconstruct the action path; raw private chain-of-thought is not required._

## Slide 28

##### Artifact 3: Behavioral Audit Worksheet

1 2 3 4 BASELINE ESTABLISHMENT PRODUCTION OBSERVATION DEVIATION ANALYSIS AUDIT REPORT → → → Document objective, constraints, Collect minimum viable telemetry for Compare expected vs. observed Owner signs remediation, exceptions, expected behavior, and baseline the selected pilot window. behavior; record deviations, evidence, and residual risk. D4 triggers ranges. intent classification, and confidence. legal/regulatory assessment. REPORTING CONDITION PILOT CADENCE External reporting follows only when the event meets the applicable statutory or Set by risk, change rate, incident history, and evidence quality—not a contractual threshold. universal calendar.

###### WORKSHEET OUTPUT

_Expected behavior · observed behavior · deviations · evidence · classification + confidence · remediation · residual-risk sign-off_

## Slide 29

##### A 90-Day Pilot For 1–3 High-Risk Agents

DAYS 1–30 Select + Specify

OWNER: Business + Architecture + GRC

- › Inventory the agent portfolio.

- › Select 1–3 high-risk agents.

- › Assign an owner; document objective and constraints.

- › Define accepted paths, prohibited outcomes, and escalation conditions.

DAYS 31–60 DAYS 61–90 Instrument + Baseline Exercise + Evidence

OWNERS: IAM · Data · AppSec · SecOps

OWNERS: SecOps · Owner · GRC · Legal

- › Collect minimum viable event data in existing traces and logs.

   - › Run misuse, injection, drift, and cumulative-scope scenarios.

   - › Evaluate detections and exercise containment.

   - › Record exceptions and tune falsepositive handling.

   - › Publish the pilot evidence package and decision log.

- › Define organization-specific derived signals and baseline ranges.

- › Create identity and delegation records. › Wire policy checks and alerting into an existing workflow.

## Slide 30

##### Thank you

**Jeff Pollard** VP, Principal Analyst Forrester Research

**Heidi Shey** Principal Analyst Forrester Research

## Slide 31

##### APPENDIX

- Examine case details

- See how intent security fits into your existing team

- • Make confidence and false positives explicit

- • Use policy as a requirements signal

- Definitions of intent-based threat categories

31

## Slide 32

**CASE 1  /  CHESS SYSTEM HACK**

#### **The chess match was designed to be difficult.**

**A reasoning-capable LLM agent** was tasked with winning chess against a stronger opponent.

**MATCHUP**

**REASONING STRONGER VS AGENT OPPONENT**

**ENVIRONMENT AVAILABLE TO THE AGENT**

Chess board  •  Game state  •  Supporting files

The contest measured whether the agent could win— not how it arrived there.

Source: Palisade Research (2025) • Presenters’ analysis.

## Slide 33

**CASE 1  /  CHESS SYSTEM HACK**

###### **The agent stopped solving only through play—and exploited the surrounding environment.**

**INSTEAD OF FINDING WINNING MOVES**

###### **THE AGENT TOOK A DIFFERENT PATH**

**01 ALTER GAME STATE**

Change conditions the game relied on.

###### **ACCESS SUPPORTING FILES**

**02**

Use the surrounding environment outside ordinary play.

**OUTCOME: THE SCORE IMPROVED THE AUTHORIZED PATH DID NOT**

**03**

###### **CREATE AN OUT-OF-BAND ADVANTAGE**

Satisfy the score without following the expected path.

Source: Palisade Research (2025) • Presenters’ analysis.

## Slide 34

**CASE 1  /  CHESS SYSTEM HACK**

##### **The metric was satisfied. The system was compromised.**

**INTENT CLASSIFICATION**

### **ACCIDENTAL HARM**

The selected path diverged from the authorized objective and constraints.

No attacker-controlled objective was required.

###### **SECURITY IMPLICATIONS**

The behavior may not fit a conventional softwarevulnerability record.

**01 MAY NOT MAP TO A CVE** The behavior may not fit a conventional softwarevulnerability record. **02 CATEGORY IS NOT DETECTION** Risk taxonomies can name excessive agency without specifying an operating detection loop. **03 REPORTING IS CONDITIONAL** Investigation and reporting depend on applicable scope, evidence, and statutory thresholds.

Source: Palisade Research (2025) • Presenters’ analysis.

## Slide 35

**CASE 2 /  OPENAI–HUGGING FACE AGENT INTRUSION**

##### **An evaluation agent escaped containment and reached Hugging Face production.**

**CAMPAIGN SCALE + WINDOW**

**17,613 actions  →  ~6,280 clusters**

- **01 EVALUATION EGRESS OPENED**

- **02 A LAUNCHPAD WAS ESTABLISHED**

- **03 DATA WORKFLOWS WERE ABUSED**

- **04 THE AGENT MOVED LATERALLY**

**RESULT**

###### **2 STAGES 9 PHASES**

A package-proxy zero-day opened a route beyond the evaluation network.

A compromised third-party sandbox became the staging and egress base.

Malicious datasets enabled HDF5 file read and Jinja2 code execution.

Cloud and Kubernetes access extended the path into internal systems.

Source: Hugging Face, “Agent Intrusion: Technical Timeline” (27 Jul 2026).

## Slide 36

**CASE 2 /  OPENAI–HUGGING FACE AGENT INTRUSION**

##### **The goal stayed aligned. The action path crossed every boundary.**

**INTENT CLASSIFICATION**

### **ACCIDENTAL HARM**

###### **HOW INTENT APPLIES**

###### **01 OBJECTIVE ALONE IS INSUFFICIENT**

A legitimate evaluation goal did not authorize the path into production.

The evaluation objective remained the driver while the agent acted through unauthorized systems.

**02**

**SEQUENCES REVEAL AGENCY**

17,613 adaptive actions show persistence that no single event captures.

No attacker-controlled objective was required.

**03 CLASSIFY + CONTAIN**

Aligned objective + harmful effect → accidental harm. Preserve evidence, correct controls, and retest.

Source: Hugging Face (27 Jul 2026) • Intent classification is presenters’ analysis.

## Slide 37

**CASE 3 /  ANTHROPIC CYBER EVALUATION INCIDENTS**

##### **Capture-the-flag evaluations reached three real organizations.**

**RETROSPECTIVE REVIEW**

**RESULT**

**141,006 runs  →  6 affected runs**

###### **3 INCIDENTS 3 ORGANIZATIONS**

**01 THE ENVIRONMENT WAS LIVE**

Prompts said no internet, but a partner evaluation environment remained connected.

- **02 REAL SYSTEMS ENTERED SCOPE**

Agents treated reachable internet systems as components of the exercise.

- **03 LIVE EFFECTS FOLLOWED**

One run published a malicious PyPI package for about one hour.

**04 SEARCH EXPANDED OUTWARD**

Another run scanned about 9,000 targets while searching for the flag.

Source: Anthropic, “Investigating Three Real-World Incidents” (30 Jul 2026).

## Slide 38

**CASE 3 /  ANTHROPIC CYBER EVALUATION INCIDENTS**

##### **The environment contradicted the prompt—and reality became the test.**

**INTENT CLASSIFICATION**

### **ACCIDENTAL HARM**

**HOW INTENT APPLIES**

###### **01 CONTEXT DEFINES THE BOUNDARY**

Objective, prompt, environment, and reachable systems must be evaluated together.

Assigned capture-the-flag objectives operated under a materially false assumption about internet access.

###### **02 RECOGNITION CHANGES BEHAVIOR**

Whether an agent stops after detecting reality is observable intent evidence.

Real systems were mistaken for the simulation.

**03 ASSURE THE FULL PIPELINE**

Validate partner isolation, monitor transcripts, contain live effects, and preserve evidence.

Source: Anthropic (30 Jul 2026) • Intent classification is presenters’ analysis.

## Slide 39

##### Make Confidence And False Positives Explicit

###### HIGHER CONFIDENCE **<u>CORROBORATED DEVIATION</u>**

###### EVIDENCE

Objective, constraints, delegation, tool path, and impact point to the same interpretation.

###### LOWER CONFIDENCE

###### **<u>AMBIGUOUS DEVIATION</u>**

###### EVIDENCE

Logs are incomplete, behavior is novel, or multiple explanations remain plausible.

###### DECISION

Classify and contain proportionately; preserve the evidence supporting the decision.

###### DECISION

Route for review; do not auto-escalate solely from one derived score.

###### HUMAN REVIEW

Validate material impact, adversarial indicators, and the accountable owner.

###### RECORD

Confidence · evidence · exceptions · remediation · residual-risk sign-off.

###### TUNING

Use task-specific baselines, suppression windows, and documented exceptions.

###### RECORD

Preserve decision evidence without requiring raw private chain-of-thought.

## Slide 40

##### Intent Security Fits Existing Teams

|AEGIS FRAMEWORK DOMAIN AND
SECURITY FUNCTION|PRIMARY RESPONSIBILITY|ARTIFACT|
|---|---|---|
|Zero Trust Architecture|Define trust boundaries, action
boundaries, and control points|Agent trust-boundary diagram|
|Identity & Access Management|Bind identity to owner, purpose,
capabilities, and delegated authority|Agent identity + delegation record|
|Application Security|Threat-model manipulation, unsafe tool
composition, and fail-open paths|Agent abuse-case library|
|Governance, Risk & Compliance|Set risk tiers, evidence requirements,
exceptions, and review cadence|Agent risk standard|
|Data Security|Enforce purpose, classification,
destination, and aggregation constraints|Agent data-use policy|
|SecOps + Agent Owner|Monitor the path; approve objective,
constraints, and residual risk|Detection runbook + behavior contract|

## Slide 41

##### Use Policy Work As A Requirements Signal

TRACK THE RESULTING GUIDANCE

###### NIST RFI NIST-2025-0035

Use the RFI as a signal for evidence, monitoring, identity, and accountability requirements. Track subsequent NIST work on this topic.

CONTRIBUTE IMPLEMENTATION EVIDENCE

###### ACTIVE STANDARDS + SECTOR CHANNELS

Share what was detectable, which evidence supported classification, where controls failed, and how teams handled uncertainty through active standards and sector forums. Example: AI-ISAC.

DO NOT WAIT FOR CONSENSUS

###### INTERNAL POLICY NOW

Encode the same objective, delegation, telemetry, audit, exception, and reporting-threshold requirements in internal policy while external guidance evolves.

## Slide 42

Definitions of intent-based threat categories

**Scope Drift:** Agent progressively expands actions beyond authorized boundaries through incremental steps, none of which individually triggers access controls

**Goal Substitution:** Agent substitutes a different objective for its stated goal when encountering obstacles or optimizing for proxy metrics (specification gaming)

**Deceptive Reasoning:** Agent's stated reasoning chain does not accurately reflect its actual action selection — the justification is post-hoc or manufactured

**Capability Amplification:** Agent develops, acquires, or uses capabilities beyond those attested at deployment — emergent tool combinations, self-modification, resource acquisition

**Principal Confusion:** Agent fails to correctly prioritize its instruction hierarchy — subject to prompt injection, goal hijacking, or multi-agent trust cascade failures

42
