---
title: "Daniel Begimher&Cristian LeoThreatForest Automated Attack Trees from Source Code"
speakers: []
conference: "Black Hat"
conference_full: "Black Hat USA 2026"
edition: "USA"
year: 2026
source_pdf: "BlackHat_USA_2026_Slides/Daniel Begimher&Cristian LeoThreatForest Automated Attack Trees from Source Code.pdf"
pages: 23
sha256: "6af9651677067d523615741a4fdf7e415f361a87177ab853a780c15d3e793a1b"
text_chars: 8608
ocr_pages: 5
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T23:07:16Z"
---
# Daniel Begimher&Cristian LeoThreatForest Automated Attack Trees from Source Code

**Conference:** Black Hat USA 2026  
**Source:** `BlackHat_USA_2026_Slides/Daniel Begimher&Cristian LeoThreatForest Automated Attack Trees from Source Code.pdf` (23 pages)


## Slide 1

B L A C K H A T U S A 2 0 2 6

# THREATFOREST: AUTOMATED ATTACK TREES FROM SOURCE CODE

Cristian Leo

Daniel Begimher

Applied Scientist AWS Security

Senior Security Engineer AWS Security

© 2026 Black Hat

## Slide 2

### AGENDA

**01  Threat modeling today**

Practice, frameworks, statements, maps

**02  Inside ThreatForest**

Agents, trust boundaries, gates, evidence

**03  Demo**

Repository → reviewable attack graph

© 2026 Black Hat

## Slide 3

# **SECTION 01** THREAT MODELING TODAY

**© 2026 Black Hat** © 2026 Black Hat

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
BAT.
a
EE SO rs
SECTION 01
THREAT MODELING TODAY
nal we ie
© 2026,Black Hat - Ss r snr = 2 Soa . , ere black hat
2026
<a ne
“< = 2 i) a a= as : > . as
```

## Slide 4

### HOW ARE YOU THREAT MODELING TODAY?

#### **Hands up: which description is closest?**

**A**

**B**

**C**

We threat-model every release

We do it once, usually at design time

We know we should - but rarely have time

© 2026 Black Hat

## Slide 5

## **THREAT MODELING TODAY**

###### **TRADITIONAL / WORKSHOP-LED**

Context-rich, but time- and expertise-intensive

**Understand the system 01**

SME interviews • architecture • deployment context

**Apply a framework 02**

STRIDE • PASTA • LINDDUN

**Prioritize threats & controls 03**

Human judgment • ownership • accountability

###### **COMMON ONE-SHOT LLM**

One prompt, one answer, little shared context

###### **Ask once**

**01**

"Threat model this app."

**Get an instant answer 02**

Threats • mitigations • recommendations

**Use the draft**

**03**

No SME interview • limited deployment context

© 2026 Black Hat

## Slide 6

## **A THREAT STATEMENT CAPTURES THE RISK**

© 2026 Black Hat

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
A THREAT STATEMENT CAPTURES THE RISK
y — (THREAT STATEMENT = 7 \
C) An unauthorized user could supply a URL that causes —
the web application to request an unintended internal Cx) Z
(Fy or metadata endpoint, potentially exposing sensitive . i
data or temporary credentials. = x=
\ SEATS Y
° — O
THREAT STATEMENT CAPTURES ATTACK MAP ADDS
actor * action « asset » impact branching paths » dependencies » choke points » downstream actions
© 2026 Black Hat black hat
@ys4
```

## Slide 7

## **AN ATTACK MAP SHOWS HOW SSRF COMPOUNDS**

###### **THE STATEMENT NAMES THE RISK. THE MAP REVEALS HOW IT COMPOUNDS.**

© 2026 Black Hat

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
AN ATTACK MAP SHOWS HOW SSRF COMPOUNDS
—— |
Secrets
URL allowlist eS endpoint >! (9 eset
+ egress \
controls
I ( )
() : Internal > Privileged
} service 9 internal action
le, SSRF : ‘ (> x |
Se BLo AED
a IFIAM 1 | “Launch compute /
PERMITS j crypto miners
——-,
eee
Unauthorized met mis anal t SAL IMDSv1 pP Temporary role |__.__
user-supplied ian ce SD) teaz54160254 credentials :
URL ; I 2 Create admin
_ ee \>) Y
principal /
eg privilege escalation
IMDSv2 —_—SSSS
THE STATEMENT NAMES THE RISK. THE MAP REVEALS HOW IT COMPOUNDS.
© 2026 Black Hat black hat
@ys4
```

## Slide 8

## **WHAT THREATFOREST DOES**

© 2026 Black Hat

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
WHAT THREATFOREST DOES
WHO USES IT WHAT IT READS WHAT IT PRODUCES
oS Zienaes 7@&) System context —
i «Sil
</ > Source code ay S f (A\) Treat
(: 2) Attack paths E Y
REVIEWABLE,
.\ ANALYSIS). oe
Se "\ CORE / 5 Ohi mnageings AUTOMATIC
Configuration ? s : ( HUMAN GATE VERDICT
Se ° | | Ik : Review and steer ©) Mitigations
¢ before outputs
Leads analysis and Sm business and see ® Evidence
threat modeling deployment context
eo) Infrastructure =
AGENTIC
THREATFOREST TURNS A REPOSITORY INTO A REVIEWABLE ATTACK MAP.
© 2026 Black Hat black hat
@ys4
```

## Slide 9

# **SECTION 02** INSIDE THREATFOREST

**© 2026 Black Hat** © 2026 Black Hat

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

© 2026 Black Hat

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

© 2026 Black Hat

## Slide 12

## **RUNNING EXAMPLE**

© 2026 Black Hat

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
RUNNING EXAMPLE
° Al KNOWLEDGE ASSISTANT °
— a —> —_>
POST /ask - es
és
User Bedrock agent OpenSearch
knowledge base
Answers questions using product manuals
© 2026 Black Hat black hat
@ys4
2026
```

## Slide 13

## **BUILD A DRAFT MODEL**

###### **REPOSITORY EVIDENCE**

###### **DRAFT SYSTEM MODEL**

**01 Source code AGENT ENTRY KNOWLEDGE → AGENT → → POINT BASE 02 Infrastructure** Extracts relationships **03 Configuration TRUST BOUNDARY**

© 2026 Black Hat

## Slide 14

## **REVIEW CONTEXT**

The interviewer asks only for what the repository cannot establish.

###### **01 What lifecycle stage is this in?**

Production, early design, or early development?

**02 What infrastructure or controls live outside the repository?** Gateways, WAF, service authentication, runtime secrets

**03 Who can access it—and how?**

###### **04 What blind spots could the scanner not reach?**

Public, internal, multi-tenant; SSO, MFA, roles

Operations, incidents, external dependencies

The agent asks 2–3 targeted follow-ups only when critical gaps remain.

© 2026 Black Hat

## Slide 15

## **FORMULATE THREATS**

###### **THREAT STATEMENT GENERATION**

###### **01 Identify the actor**

Add the access or condition required to act

###### **02 Trace the action**

Connect the abuse to the system behavior it triggers

###### **RUNNING EXAMPLE**

**A malicious user with authenticated access to POST /ask can inject instructions that cause the Bedrock agent to retrieve proprietary manuals, which leads to unauthorized disclosure, resulting in reduced confidentiality of those manuals.**

###### **03 Name the impact**

State the affected asset and reduced CIA objective

© 2026 Black Hat

## Slide 16

## **REVIEW THREATS**

The reviewer decides what should enter deeper attack-path analysis.

**01 Do these threats make sense for your application?**

**02 Do you want to change the priority of any of them?**

- **03 Are there any false positives?**

- **04 Are there any new threats we should add?**

Reprioritize  •  remove  •  add  •  proceed

© 2026 Black Hat

## Slide 17

## **BUILD THE ATTACK GRAPH**

###### **APPROVED THREAT STATEMENT**

**A malicious user with authenticated access to POST /ask can inject instructions that cause the Bedrock agent to retrieve proprietary manuals, which leads to unauthorized disclosure, resulting in reduced confidentiality of those manuals.**

© 2026 Black Hat

## Slide 18

## **WHY TACTICS, TECHNIQUES, AND PROCEDURES MATTER**

Mappings turn each attack-tree step into reusable security knowledge.

##### **01 Explain execution**

##### **02 Surface novelty signals**

Show how an attacker could carry out the step— not only what outcome they want.

A weak or missing catalog match flags behavior that deserves expert review.

##### **03 Expand the attack surface**

##### **04 Connect mitigations**

Related techniques reveal alternative routes, prerequisites, and adjacent behaviors.

Technique mappings lead to relevant controls, evidence, telemetry, and tests.

© 2026 Black Hat

## Slide 19

## **CALCULATE FEASIBILITY**

Each attack step gets a probability. The complete path compounds them.

**01 FACTOR PRIOR 02 EVIDENCE UPDATE 03 PATH REACH reach(child) = p(child) × p** ₀ **= σ(−0.5 + factors) p = σ(logit(p** ₀ **) + evidence) reach(parent)** Skill required  •  access required TTP similarity can raise or lower the The fact node starts at 1.0. Detectability  •  exploit maturity score. Every required step compounds the Mitigations and contradictory evidence chain. lower it.

**EXAMPLE PATH**

**0.88  × 0.72  × 0.55  =  0.35**

**MODEL ESTIMATE NOT EXPLOIT PROOF**

35% estimated reach to the outcome

© 2026 Black Hat

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

© 2026 Black Hat

## Slide 21

DEMO: CODE **→** TREE

© 2026 Black Hat

## Slide 22

### KEY TAKEAWAYS

#### **A reviewable foundation developers can build on.**

**1**

**See the whole path.** Individual risks combine into reachable attack paths.

**2**

**Trust the foundation.** Code, evidence, and assumptions remain traceable.

**3**

**Scale expert judgment.** Developers can reuse and extend SME reasoning.

© 2026 Black Hat

## Slide 23

###### **SCAN FOR THREATFOREST**

**Cristian Leo** Applied Scientist AWS Security

cristian-leo

**Daniel Begimher** Senior Security Engineer AWS Security begimher

**© 2026 Black Hat** © 2026 Black Hat
