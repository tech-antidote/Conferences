---
title: "ThreatForest: Automated Attack Trees from Source Code"
speakers: ["Cristian Leo", "Daniel Begimher"]
conference: "Black Hat"
conference_full: "Black Hat USA 2026"
edition: "USA"
year: 2026
source_pdf: "BlackHat_USA_2026_Slides/Daniel Begimher&Cristian LeoThreatForest Automated Attack Trees from Source Code.pdf"
pages: 23
sha256: "6af9651677067d523615741a4fdf7e415f361a87177ab853a780c15d3e793a1b"
text_chars: 7925
ocr_pages: 4
has_ocr: true
redacted_secrets: 0
ocr_confidence: 84.5
ocr_unreliable_blocks: 0
vision_verified_pages_changed: 17
vision_verified_pages: 23
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
content_note: "The source filename omits the separator between the speaker names and the title, gluing 'Leo' to 'ThreatForest'."
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T05:30:45Z"
---
# ThreatForest: Automated Attack Trees from Source Code

**Speakers:** Cristian Leo, Daniel Begimher  
**Conference:** Black Hat USA 2026  
**Source:** `BlackHat_USA_2026_Slides/Daniel Begimher&Cristian LeoThreatForest Automated Attack Trees from Source Code.pdf` (23 pages)

## Slide 1

BLACK HAT USA 2026

# THREATFOREST: AUTOMATED ATTACK TREES FROM SOURCE CODE

**Cristian Leo**

Applied Scientist

AWS Security

**Daniel Begimher**

Senior Security Engineer

AWS Security

## Slide 2

### AGENDA

**01  Threat modeling today**

Practice, frameworks, statements, maps

**02  Inside ThreatForest**

Agents, trust boundaries, gates, evidence

**03  Demo**

Repository → reviewable attack graph

## Slide 3

**SECTION 01**

# THREAT MODELING TODAY

## Slide 4

### HOW ARE YOU THREAT MODELING TODAY?

**Hands up: which description is closest?**

**A** We threat-model every release

**B** We do it once, usually at design time

**C** We know we should - but rarely have time

## Slide 5

## THREAT MODELING TODAY

**TRADITIONAL / WORKSHOP-LED**

Context-rich, but time- and expertise-intensive

**01 Understand the system**

SME interviews • architecture • deployment context

**02 Apply a framework**

STRIDE • PASTA • LINDDUN

**03 Prioritize threats & controls**

Human judgment • ownership • accountability

**COMMON ONE-SHOT LLM**

One prompt, one answer, little shared context

**01 Ask once**

"Threat model this app."

**02 Get an instant answer**

Threats • mitigations • recommendations

**03 Use the draft**

No SME interview • limited deployment context

THE OPPORTUNITY: HUMAN CONTEXT AT MACHINE SPEED

## Slide 6

## A THREAT STATEMENT CAPTURES THE RISK

**THREAT STATEMENT**

An unauthorized user could supply a URL that causes the web application to request an unintended internal or metadata endpoint, potentially exposing sensitive data or temporary credentials.

**THREAT STATEMENT CAPTURES**

actor • action • asset • impact

**ATTACK MAP ADDS**

branching paths • dependencies • choke points • downstream actions

## Slide 7

## AN ATTACK MAP SHOWS HOW SSRF COMPOUNDS

Unauthorized user-supplied URL

**SSRF**

Web app makes server-side request

**URL allowlist + egress controls**

Secrets endpoint → Expose secret

Internal service → Privileged internal action

IMDSv1 169.254.169.254 → Temporary role credentials

**Require IMDSv2**

**IF IAM PERMITS**

Launch compute / crypto miners

Create admin principal / privilege escalation

THE STATEMENT NAMES THE RISK. THE MAP REVEALS HOW IT COMPOUNDS.

## Slide 8

## WHAT THREATFOREST DOES

**WHO USES IT**

Security engineer — Leads analysis and threat modeling

Application owner — Provides business and deployment context

**WHAT IT READS**

Source code

Infrastructure

Configuration

**AGENTIC ANALYSIS CORE**

**HUMAN GATE** — Review and steer before outputs are published

**WHAT IT PRODUCES**

System context

Threats

Attack paths

TTP mappings

Mitigations

Evidence

REVIEWABLE, NOT AN AUTOMATIC VERDICT

THREATFOREST TURNS A REPOSITORY INTO A REVIEWABLE ATTACK MAP.

## Slide 9

**SECTION 02**

# INSIDE THREATFOREST

## Slide 10

## **AUTOMATION NEEDS CONTEXT**

**AUTOMATION CONTRIBUTES**

**01 Continuous analysis**

**02 Repeatable results**

**03 Repository awareness**

###### **HUMANS CONTRIBUTE**

**01 Deployment reality**

**02 Business impact**

**03 Risk appetite**

## Slide 11

## **THE THREATFOREST PIPELINE**

Agents perform the repeatable analysis. Humans authorize contextual decisions.

##### **01 Understand the system**

Agent + deterministic verifier

**03 Formulate threats**

Agent + deterministic verifier

**05 Build attack maps**

Agent + deterministic verifier

##### **02 Review context**

Human gate

**04 Review threats**

Human gate

##### **06 Recommend controls**

Agent + deterministic verifier

## Slide 12

## RUNNING EXAMPLE

**AI KNOWLEDGE ASSISTANT**

User → POST /ask → Bedrock agent → OpenSearch knowledge base

Answers questions using product manuals

## Slide 13

## BUILD A DRAFT MODEL

**REPOSITORY EVIDENCE**

01 Source code

02 Infrastructure

03 Configuration

**AGENT**

Extracts relationships

**DRAFT SYSTEM MODEL**

ENTRY POINT → AGENT → KNOWLEDGE BASE

TRUST BOUNDARY

## Slide 14

## REVIEW CONTEXT

The interviewer asks only for what the repository cannot establish.

**01 What lifecycle stage is this in?**

Production, early design, or early development?

**02 What infrastructure or controls live outside the repository?**

Gateways, WAF, service authentication, runtime secrets

**03 Who can access it—and how?**

Public, internal, multi-tenant; SSO, MFA, roles

**04 What blind spots could the scanner not reach?**

Operations, incidents, external dependencies

The agent asks 2–3 targeted follow-ups only when critical gaps remain.

## Slide 15

## FORMULATE THREATS

**THREAT STATEMENT GENERATION**

**01 Identify the actor**

Add the access or condition required to act

**02 Trace the action**

Connect the abuse to the system behavior it triggers

**03 Name the impact**

State the affected asset and reduced CIA objective

**RUNNING EXAMPLE**

A malicious user with authenticated access to POST /ask can inject instructions that cause the Bedrock agent to retrieve proprietary manuals, which leads to unauthorized disclosure, resulting in reduced confidentiality of those manuals.

## Slide 16

## **REVIEW THREATS**

The reviewer decides what should enter deeper attack-path analysis.

**01 Do these threats make sense for your application?**

**02 Do you want to change the priority of any of them?**

- **03 Are there any false positives?**

- **04 Are there any new threats we should add?**

Reprioritize  •  remove  •  add  •  proceed

## Slide 17

## BUILD THE ATTACK GRAPH

**APPROVED THREAT STATEMENT**

A malicious user with authenticated access to POST /ask can inject instructions that cause the Bedrock agent to retrieve proprietary manuals, which leads to unauthorized disclosure, resulting in reduced confidentiality of those manuals.

**1. CONDITIONS**

Untrusted input reaches agent

**EVIDENCE** — User message can reach the agent

**2. ACTIONS**

Manipulate prompt → Retrieve manual content

**3. BRANCH**

Return content in response

OR → Trigger chained request

**ASSUMPTION** — Downstream service will process request

**4. OUTCOME**

Protected content exposed

## Slide 18

## WHY TACTICS, TECHNIQUES, AND PROCEDURES MATTER

Mappings turn each attack-tree step into reusable security knowledge.

**01 Explain execution**

Show how an attacker could carry out the step—not only what outcome they want.

**02 Surface novelty signals**

A weak or missing catalog match flags behavior that deserves expert review.

**03 Expand the attack surface**

Related techniques reveal alternative routes, prerequisites, and adjacent behaviors.

**04 Connect mitigations**

Technique mappings lead to relevant controls, evidence, telemetry, and tests.

## Slide 19

## CALCULATE FEASIBILITY

Each attack step gets a probability. The complete path compounds them.

**01 FACTOR PRIOR**

p₀ = σ(−0.5 + factors)

Skill required • access required
Detectability • exploit maturity

**02 EVIDENCE UPDATE**

p = σ(logit(p₀) + evidence)

TTP similarity can raise or lower the score.
Mitigations and contradictory evidence lower it.

**03 PATH REACH**

reach(child) = p(child) × reach(parent)

The fact node starts at 1.0.
Every required step compounds the chain.

**EXAMPLE PATH**

0.88 × 0.72 × 0.55 = 0.35

35% estimated reach to the outcome

**MODEL ESTIMATE NOT EXPLOIT PROOF**

## Slide 20

## **GENERATE MITIGATIONS**

###### **CANDIDATE CONTROLS**

- **01 Isolate untrusted input**

- **02 Limit retrieval scope**

**03 Filter sensitive output**

###### **RANK IN CONTEXT**

**01 Path impact**

**02 Evidence confidence**

**03 Implementation cost**

## Slide 21

# DEMO: CODE → TREE

## Slide 22

### KEY TAKEAWAYS

#### **A reviewable foundation developers can build on.**

**1**

**See the whole path.** Individual risks combine into reachable attack paths.

**2**

**Trust the foundation.** Code, evidence, and assumptions remain traceable.

**3**

**Scale expert judgment.** Developers can reuse and extend SME reasoning.

## Slide 23

# Thank you

**SCAN FOR THREATFOREST**

THREATFOREST

**Cristian Leo**

Applied Scientist

AWS Security

cristian-leo

**Daniel Begimher**

Senior Security Engineer

AWS Security

begimher

