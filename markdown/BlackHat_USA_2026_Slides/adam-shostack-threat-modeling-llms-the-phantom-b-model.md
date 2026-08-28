---
title: "Threat Modeling LLMs The PHANTOM-B model"
speakers: ["Adam Shostack"]
conference: "Black Hat"
conference_full: "Black Hat USA 2026"
edition: "USA"
year: 2026
source_pdf: "BlackHat_USA_2026_Slides/Adam Shostack_Threat Modeling LLMs The PHANTOM-B model.pdf"
pages: 59
sha256: "61bb9f93a0218f3f2e7f02d14afcc49ee25ab20aa220df706175080b8e92632f"
text_chars: 17381
ocr_pages: 10
has_ocr: true
redacted_secrets: 0
ocr_confidence: 91.5
ocr_unreliable_blocks: 0
vision_verified_pages_changed: 56
vision_verified_pages: 59
ocr_timeouts: 0
pages_recovered_from_text_layer: 1
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T05:27:08Z"
---
# Threat Modeling LLMs The PHANTOM-B model

**Speakers:** Adam Shostack  
**Conference:** Black Hat USA 2026  
**Source:** `BlackHat_USA_2026_Slides/Adam Shostack_Threat Modeling LLMs The PHANTOM-B model.pdf` (59 pages)


## Slide 1

Threat Modeling LLMs
The PHANTOM-B Approach

Adam Shostack

## Slide 2

Threat Modeling LLMs
The PHANTOM-B Approach

Blackhat USA
August 2026

Adam Shostack

## Slide 3

The Emperor is most displeased with your lack of AI Progress

## Slide 4

### Agenda

- Threat modeling context

- Threat modeling LLMs

- The PHANTOM-B approach

   - Why PHANTOM-B?

   - What is PHANTOM-B?

## Slide 5

### About

Don’t just understand security. Build it in.

## Slide 6

Threat modeling context

## Slide 7

### What is threat modeling?

- Using models to help us think about security

- The “measure twice, cut once” of engineering

- Applies to both tech you produce or tech you operate

- Applies to LLMs you train or get from Huggingface

## Slide 8

### How do we threat model?

- Four Question Framework

   - What are we working on?

   - What can go wrong?

   - What are we going to do about it?

   - Did we do a good job?

- Widely adopted: Industry + gov standard

   - Anthropic, Google, Amazon, MITRE, FDA + more

- Threatmodelingmanifesto.org + Shostack.org/whitepapers

## Slide 9

### Why bother threat modeling LLMs

- “Won’t the LLM threat model?”

- “My skills say only write secure code!”

- “Going fast gets me promoted”

- So why bother threat modeling LLMs?

## Slide 10

### Your executives are really scared

- AI disruption is real

- Maybe we’re in a bubble, maybe not?

- FOMO is rampant

- We have to ship AI stuff!

## Slide 11

### Business works better with threat modeling

- Your developers + leaders don’t understand what can go wrong

- LLMs change your security posture

   - The posture of the code being produced

   - The strengths and weaknesses of the latest models

- Cognitive debt is getting worse

- Change continues to accelerate

- Staying focused on what we’re working on is crucial

## Slide 12

Threat modeling
is the security technique that
best survives AI disruptions

## Slide 13

### Threat modeling can drive risk management

**Threat Modeling**

What can go wrong? → Easily Addressed?

- No → (to Risk Management)
- Yes → Fix it

**Risk Management**

Very bad?

- No → Accept
- Yes → Eliminate / Transfer

## Slide 14

LLMs also disrupt
threat modeling

## Slide 15

### PHANTOM-B origin story (preview)

- AI disrupted threat modeling in two ways

   - Using AI to threat model

   - Threat modeling AI systems

- Clients looking for

   - AI focused training

   - Lower training cost (“Can we make this faster?”)

- Analyzing the state of the art

   - Reviewed and wrote at length about available threat catalogs

## Slide 16

Threat modeling LLMs

## Slide 17

### Four scenarios: Using AI in…

- Offense (write me a phishing email/malware/etc)

- Defense (anti-spam, Microsoft defender copilot)

- Software development

- Business (Today’s focus)

Offense Defense Software Business

## Slide 18

### What are we working on with AI?

- Adding an LLM to our business

   - Chatbots

   - Document processing

   - Search

   - Decision making

- We should ask “what can go wrong?”

## Slide 19

MODEL DEPLOYMENT

NOT HERE

YOU ARE HERE

Trained Model → Huggingface → Integrate model into system → Test ML-enabled System → Passes Tests → ML-enabled System

Test Data (2) → Test ML-enabled System

Test ML-enabled System → Fails Test → Integrate model into system

## Slide 20

What can go wrong with AI?

## Slide 21

### Lots of sweeping talk about AI

Threat Catalogs

Laws (EU AI Act) (Harms, Risks)

Frameworks (NIST AI RMF) (“Risks”)

## Slide 22

### What are **WE** working on?

Executives

Laws (EU AI Act) (Harms, Risks)

Frameworks (NIST AI RMF) (“Risks”)

Engineers

Threat Catalogs

## Slide 23

### Many AI threat catalogs —
Ways to answer “what can go wrong”

- Berryville’s ML + LLM Risk Analyses

- OWASP Top 10 LLMs

- OWASP AI Exchange

- MITRE ATLAS

- NIST AIML E2025

- Google SAIF

- …

Threat Catalogs

Structured ways to answer
“What can go wrong”
More organized than ”We’ll red team it”

## Slide 24

The PHANTOM-B Approach

## Slide 25

Why PHANTOM-B?

## Slide 26

~~The alternatives suck~~
All models are wrong,
some models are useful.

## Slide 27

### What goes wrong with TM structures?
(Each “for some users”)

- High training cost (learning is hard)

- Hard to use (even after training)

- Not LLM/AI focused

- Duplicative/overlaps other frameworks/security work

- Raises threats which are irrelevant/can’t fix/won’t fix

   - “Academic”

- Low return on investment

- Require software support

## Slide 28

### PHANTOM-B origin story (1/2)

threat modeling
designing for security in an AI world
EXPANDED AND REVISED SECOND EDITION
Adam Shostack
WILEY

Threat Modeling: Designing for Security in an AI World
by Adam Shostack (Author) | Format: Paperback

Savings Pre-order Price Guarantee. Terms

A major update to the definitive guide on threat modeling techniques for secure by design

More than just a second edition, *Threat Modeling: Designing for Security in an AI World* thoroughly updates and expands on Adam Shostack’s classic text and structured approach to analyzing and designing systems, software, and services for security flaws to address threats and technologies that didn’t exist when the first edition published. Most notably every reader will benefit from two new chapters covering using LLMs to threat model and exploring threats to LLMs, AIs, and ML Models themselves. There’s a new deep focus on agile and an expansion of who’s involved in threat modeling, now including non-technical product owners. All told, half of this edition is completely new or heavily revised.

## Slide 29

### PHANTOM-B origin story (2/2)

- Built and iterated over several versions

   - On our own projects

   - With hyperscalers, globally significant banks and others

- Earlier versions didn’t meet our release quality bar

   - TRAPHOME

   - PHANTOMED

## Slide 30

### PHANTOM-B is inspired by STRIDE

- [Spoofing, Tampering, Repudiate, Info disclose, DoS, Expand Authority]

- Time-tested + durable mnemonic from Kohnfelder + Garg

- STRIDE remains broadly applicable

STRIDE per Element

| | Spoof | Tamper | Repudiate | Info Disclose | Deny Service | EoP |
|---|---|---|---|---|---|---|
| External Entity | ● | | ● | | | |
| Process | ● | ● | ● | ● | ● | ● |
| Data Store | | ● | ? | ● | ● | |
| Dataflow | | ● | | ● | ● | |

THREATS: What Every Engineer Should Learn From Star Wars

## Slide 31

### PHANTOM-B identifies: “What can go wrong deploying AI?”

**P**rompt injection

**H**allucination

**A**nthropomorphization

**N**on-explainable

**T**raining issues

**O**ver-reliance

**M**issing security engineering

**B**ias

- Free to use (CC-BY)

- Memorable

- 100% threat-focused

- Fits on a wallet card

PHANTOM-B threat modeling framework

> **P**rompt injection
> **H**allucination
> **A**nthropomorphization
> **N**on-explainability
> **T**raining issues (including data quality or “poison”)
> **O**ver-reliance on the LLM
> **M**issing security engineering
> **B**iases

## Slide 32

### Focused on using/calling LLMs

- Under your control (on your GPUs or Amazon Bedrock)

   - “Downloaded from Huggingface”

- An LLM provider offers, such as ChatGPT or Claude

   - Via the API

   - (Not useful for “using chatgpt.com in a browser”)

## Slide 33

### Prompt injection

- Controlling LLM behavior via input

   - Code/data confusion

- More than just funny stories

   - Bypasses your controls and gets the LLM to violate rules

   - Unlike SQLi, no deterministic, proven defenses exist

## Slide 34

### Hallucination

- ~~The LLM makes stuff up~~

- The LLM makes up stuff we don’t like:

   - Bad code

   - False citations

## Slide 35

### Anthropomorphization

- Means treating the LLM as a human

- This is great product design

   - Use of language and “I” are a facade

- LLMs are token generators

   - Not concept models

   - Not thinking beings

- “Don’t do X” for humans and token generators

- No guilt, no learning, no desire to improve

## Slide 36

ByteDance and Alibaba to disable humanlike AI custom agents as new rules loom

With Beijing’s rules on humanlike AI interaction services taking effect on July 15, Doubao and Qwen move to disable customised features

Chew up tokens!

arXiv:2604.07729 (cs)

[Submitted on 9 Apr 2026]

Emotion Concepts and their Function in a Large Language Model

Nicholas Sofroniew, Isaac Kauvar, William Saunders, Runjin Chen, Tom Henighan, Sasha Hydrie, Craig Citro, Adam Pearce, Julius Tarng, Wes Gurnee, Joshua Batson, Sam Zimmerman, Kelley Rivoire, Kyle Fish, Chris Olah, Jack Lindsey

## Slide 37

### Non-explainable

- We can’t tell why we got important results

- Explainability as “why did it actually do that?”

- Not asking “why did you do that?”

   - LLMs produce plausible answers, not accurate ones

- More important as LLM makes decisions

- Explainability for various audiences

   - Data scientists

   - End users (eg, medical LLM explaining — accurately — to patients + doctors)

   - Courts

## Slide 38

### Training issues

- LLMs do better as we give them more data

- So your LLM was probably trained on Stack Exchange, Reddit + Twitter

- Good luck finding that in the model card!

- Data poisoning is “scale invariant” with 250 documents

Souly, et al, Poisoning Attacks on LLMs Require a Near-constant Number of Poison Samples, 8 October 2025, _https://arxiv.org/abs/2510.07192_

## Slide 39

### Over-reliance on the LLM

- We trust the LLM and don’t pay close attention

- LLMs generate a lot of text / code

   - Hard to focus on

   - Often okay

- Hard to remain vigilant

- Your code, your brand 🤷

- Making decisions about hiring, college admissions, arrests… 🤯

## Slide 40

Investigations | Jul 17 2026

Black prisoners are assigned harsher living conditions in Ontario jails—thanks to AI

Ontario jails are using a program that claims it can predict prisoners’ behaviour, disproportionately putting Black prisoners in higher-security facilities

## Slide 41

### Missing security engineering

- We assume you still have software security, this ties to it

- LLMs are software

   - All software has bugs

   - Some bugs are security-relevant

- PHANTOM-B augments STRIDE, kill chains, SDLs

- PHANTOM-B was aggressively de-duped

   - For example, MCP has lots of spoofing and expansion of authority issues

   - Not included in PHANTOM-B because you have other security engineering

## Slide 42

LLMS WRITE AND TEST OUR CODE

YOU HAVE OTHER SECURITY ENGINEERING, RIGHT?

RIGHT?

## Slide 43

### Bias

- Does the LLM treat groups unevenly?

- Does it display the board of directors as white men?

   - How about the janitorial staff?

- Inherited from data pipeline

   - Bias in the data, cleaning, training, tuning processes

   - You can’t remove it, but you can understand it

- Often in the eye of the beholder

- Defined by law. Certain decisions have “protected groups”

## Slide 44

### PHANTOM-B identifies: “What can go wrong deploying AI?”

**P**rompt injection

**H**allucination

**A**nthropomorphization

**N**on-explainable

**T**raining issues

**O**ver-reliance

**M**issing security engineering

**B**ias

## Slide 45

### Using PHANTOM-B

- “What can go wrong”

- Many broader than “the math”

- Product-manager or exec suite

## Slide 46

### PHANTOM-B illustrates why TM matters

- Engineering requires tradeoffs between unsatisfiable constraints

   - Features, reliability, speed, cost, quality … and security

   - Building security in is better than bolting-on controls

- Before you write (or vibe) a line of code, consider what can go wrong

   - Threat modeling lets you do this via the Four Questions

   - PHANTOM-B lets you do this for LLMs

- This gives you the most options for what are we going to do

## Slide 47

### Summary

- Threat modeling enables strategic views of security

- What can go wrong with LLMs requires innovative approaches

- PHANTOM-B balances coverage + accessibility

## Slide 48

### Bonus!

- Today: Book signing – bookstore, Breaker Rooms @ 12:45

- Thursday: AI Threat Modeling Community meetup

   - Noon tomorrow “The Convergence, Business Hall”

## Slide 49

Thank you!

## Slide 50

PHANTOM-B approach to LLM TM

Blackhat USA August 2026

Questions?

adam@shostack.org

Slides: Shostack.org/blog

PHANTOM-B threat modeling framework

> **P**rompt injection
> **H**allucination
> **A**nthropomorphization
> **N**on-explainability
> **T**raining issues (including data quality or “poison”)
> **O**ver-reliance on the LLM
> **M**issing security engineering
> **B**iases

Wallet cards, book signing at Bookstore, 12:45 PM today

Meetup, The Convergence, Noon tomorrow

## Slide 51

Supporting Materials

Shostack + Associates

Don’t just understand security.
Build it in.

## Slide 52

### Free resources

- shostack.org/resources

- shostack.org/blog

- youtube.com/c/Shostack

- Books

- Linkedin Learning

Books free at your library/various subscriptions; Linkedin Learning via work

## Slide 53

### Commercial offerings

- Training

   - From under an hour to multi-day

   - Live instruction or computer-based

   - In-person or distributed

   - Private corporate courses

- Accelerator

   - Culture change, process design

- Assessments + analysis

## Slide 54

info@shostack.org

shostack.org/contact

## Slide 55

backup

## Slide 56

LLM01:2025 Prompt Injection
A Prompt Injection Vulnerability occurs when user prompts alter the...
Read More

LLM02:2025 Sensitive Information Disclosure
Sensitive information can affect both the LLM and its application...
Read More

LLM03:2025 Supply Chain
LLM supply chains are susceptible to various vulnerabilities, which can...
Read More

LLM04:2025 Data and Model Poisoning
Data poisoning occurs when pre-training, fine-tuning, or embedding data is...
Read More

LLM05:2025 Improper Output Handling
Improper Output Handling refers specifically to insufficient validation, sanitization, and...
Read More

LLM06:2025 Excessive Agency
An LLM-based system is often granted a degree of agency...
Read More

LLM07:2025 System Prompt Leakage
The system prompt leakage vulnerability in LLMs refers to the...
Read More

LLM08:2025 Vector and Embedding Weaknesses
Vectors and embeddings vulnerabilities present significant security risks in systems...

LLM09:2025 Misinformation
Misinformation from LLMs poses a core vulnerability for applications relying...
Read More

LLM10:2025 Unbounded Consumption
Unbounded Consumption refers to the process where a Large Language...
Read More

https://genai.owasp.org/llm-top-10/

## Slide 57

LLM01:2025 Prompt Injection
A Prompt Injection Vulnerability occurs when user prompts alter the...
Read More

~~LLM02:2025 Sensitive Information Disclosure~~
Sensitive information can affect both the LLM and its application...
Read More

~~LLM03:2025 Supply Chain~~
LLM supply chains are susceptible to various vulnerabilities, which can...
Read More

LLM04:2025 Data and Model Poisoning
Data poisoning occurs when pre-training, fine-tuning, or embedding data is...
Read More

~~LLM05:2025 Improper Output Handling~~
Improper Output Handling refers specifically to insufficient validation, sanitization, and...
Read More

LLM06:2025 Excessive Agency
An LLM-based system is often granted a degree of agency...
Read More

~~LLM07:2025 System Prompt Leakage~~
The system prompt leakage vulnerability in LLMs refers to the...
Read More

LLM08:2025 Vector and Embedding Weaknesses
Vectors and embeddings vulnerabilities present significant security risks in systems...

LLM09:2025 Misinformation
Misinformation from LLMs poses a core vulnerability for applications relying...
Read More

~~LLM10:2025 Unbounded Consumption~~
Unbounded Consumption refers to the process where a Large Language...
Read More

https://genai.owasp.org/llm-top-10/

## Slide 58

### Berryville Institute of Machine Learning

- Think tank of security + ML experts studying machine learning sec https://berryvilleiml.com/

- Taxonomy of threats (2019)

   - Manipulation of input, data, models

   - Extraction of input, data, models

- Architectural Risk Analysis of a generic ML system (2023)

- ARA for LLM (2024)

- Elevation of ML card deck!

- Annotated bibliography

https://agilestationery.com/collections/security/products/elevation-of-machine-learning-security-card-game

## Slide 59

ATLAS Matrix for AI Systems

Subtechniques: Expand All | Collapse All

Filter by Maturity: Feasible — Demonstrated

**Reconnaissance** (8 techniques)
- Active Scanning
- Gather RAG-Indexed Targets
- Gather Victim Identity Information
- Search Application Repositories
- Search Open AI Vulnerability Analysis
- Search Open Technical Databases
- Search Open Websites/Domains
- Search Victim-Owned

**Resource Development** (13 techniques)
- Acquire Infrastructure
- Acquire Public AI Artifacts
- Develop Capabilities
- Establish Accounts
- LLM Prompt Crafting
- Obtain Capabilities
- Poison Training Data
- Publish Hallucinated Entities

**Initial Access** (7 techniques)
- AI Supply Chain Compromise
- Drive-by Compromise
- Evade AI Model
- Exploit Public-Facing Application
- Phishing
- Prompt Infiltration via Public-Facing Application
- Valid Accounts

**AI Model Access** (4 techniques)
- AI Model Inference API Access
- AI-Enabled Product or Service
- Full AI Model Access
- Physical Environment Access

**Execution** (6 techniques)
- AI Agent Clickbait
- AI Agent Tool Invocation
- Command and Scripting Interpreter
- Deploy AI Agent
- LLM Prompt Injection
- User Execution

**Persistence** (9 techniques)
- AI Agent Context Poisoning
- AI Agent Tool Data Poisoning
- AI Agent Tool Poisoning
- LLM Prompt Self-Replication
- Manipulate AI Model
- Modify AI Agent Configuration
- Poison Training Data
- Prompt Infiltration via Public-Facing

**Privilege Escalation** (4 techniques)
- AI Agent Tool Invocation
- Escape to Host
- LLM Jailbreak
- Valid Accounts

**Defense Evasion** (15 techniques)
- AI Supply Chain Reputation Inflation
- AI Supply Chain Rug Pull
- Corrupt AI Model
- Delay Execution of LLM Instructions
- Evade AI Model
- Exploitation for Defense Evasion
- False RAG Entry Injection
- Impersonation

**Credential Access** (6 techniques)
- AI Agent Tool Credential Harvesting
- Credentials from AI Agent Configuration
- Exploitation for Credential Access
- OS Credential Dumping
- RAG Credential Harvesting
- Unsecured Credentials

**Discovery** (9 techniques)
- Cloud Service Discovery
- Discover AI Agent Configuration
- Discover AI Artifacts
- Discover AI Model Family
- Discover AI Model Ontology
- Discover AI Model Outputs
- Discover LLM Hallucinations
- Discover LLM System

