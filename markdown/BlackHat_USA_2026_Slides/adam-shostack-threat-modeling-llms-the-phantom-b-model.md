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
text_chars: 18235
ocr_pages: 11
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T23:04:45Z"
---
# Threat Modeling LLMs The PHANTOM-B model

**Speakers:** Adam Shostack  
**Conference:** Black Hat USA 2026  
**Source:** `BlackHat_USA_2026_Slides/Adam Shostack_Threat Modeling LLMs The PHANTOM-B model.pdf` (59 pages)

## Slide 1

Threat Modeling LLMs The PHANTOM-B Approach Adam Shostack

**1**

## Slide 2

Threat Modeling LLMs The PHANTOM-B Approach

Blackhat USA August 2026

#### Adam Shostack

**2**

## Slide 3

The Emperor is most displeased with your lack of AI Progress

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
) ie
Ta }
THE EMPEROR IS MOST DISPLEASED WITH YOUR LACK OF Al PROGRESS
```

## Slide 4

### Agenda

- Threat modeling context

- Threat modeling LLMs

- The PHANTOM-B approach

   - Why PHANTOM-B?

   - What is PHANTOM-B?

**4**

## Slide 5

### About

Don’t just understand security. Build it in.

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
SHOSTACK
+ASSOCIATES
Don’t just understand security.
Build it in.
About
Ww
UNIVERSITY of WASHINGTON
es
# threat
modeling
—_—_
```

## Slide 6

Threat modeling context

## Slide 7

### What is threat modeling?

- Using models to help us think about security

- The “measure twice, cut once” of engineering

- Applies to both tech you produce or tech you operate

- Applies to LLMs you train or get from Huggingface

**7**

## Slide 8

How do we threat model?

- Four Question Framework

   - What are we working on?

   - What can go wrong?

   - What are we going to do about it?

   - Did we do a good job?

- Widely adopted: Industry + gov standard

   - Anthropic, Google, Amazon, MITRE, FDA + more

- Threatmodelingmanifesto.org + Shostack.org/whitepapers

**8**

## Slide 9

### Why bother threat modeling LLMs

- “Won’t the LLM threat model?”

- “My skills say only write secure code!”

- “Going fast gets me promoted”

- So why bother threat modeling LLMs?

**9**

## Slide 10

Your executives are really scared

- AI disruption is real

- Maybe we’re in a bubble, maybe not?

- FOMO is rampant

- We have to ship AI stuff!

**10**

## Slide 11

Business works better with threat modeling

- Your developers + leaders don’t understand what can go wrong

- LLMs change your security posture

   - The posture of the code being produced

   - The strengths and weaknesses of the latest models

- Cognitive debt is getting worse

- Change continues to accelerate

- Staying focused on what we’re working on is crucial

**11**

## Slide 12

Threat modeling is the security technique that best survives AI disruptions

**12**

## Slide 13

Threat modeling can drive risk management

**13**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
hreat modeling can drive risk management
peteeeeeneeseeeeeeaeeeeeeeseseeeeeeeesaeeaeuaeesseeseesaasaaaaaeassseseesaesaesaaaaeuaeusesasseesaasaesaauassesssesaesaasaaaaaaaseeseesaesaesaeaaeuacesesseeaeeaaaag  pasaaaaceaceesseseesaesaaeeuessceesaesaasacaaeeaeuesseeseesassaasaaeasaususeseeseesaesaaeasusesseeeeeey,
‘Threat Modeling Risk Management
What can go Easily Nt
wrong? | Addressed? o> > 2 Accept |
Eliminate
Transfer
SHOSTACK 3
+ ASSOCIATES
```

## Slide 14

## LLMs also disrupt threat modeling

**14**

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

**15**

## Slide 16

## Threat modeling LLMs

**17**

## Slide 17

Four scenarios: Using AI in…

- Offense (write me a phishing email/malware/etc)

- Defense (anti-spam, Microsoft defender copilot)

- Software development

- Business (Today’s focus)

Offense Defense Software Business
18

## Slide 18

What are we working on with AI?

- Adding an LLM to our business

   - Chatbots

   - Document processing

   - Search

   - Decision making

- We should ask “what can go wrong?”

**19**

## Slide 19

You are here

Huggingface
Not Here

**20**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
+
NOT HERE
MODEL
DEPLOYMENT
Huggingface
IPs
YOU ARE HERE
Test ;
; : Passes
: est Tests
_ eee eseo@ | ML-onabledh........... e ML-enabled
: System System
Fails Test
SHOSTACK
20
```

## Slide 20

## What can go wrong with AI?

**21**

## Slide 21

Lots of sweeping talk about AI
Threat
Catalogs
Laws Frameworks
(EU AI Act) (NIST AI RMF)
(Harms, Risks) (“Risks”)
22

## Slide 22

What are **WE** working on?

Executives
Laws Frameworks
(EU AI Act) (NIST AI RMF)
(Harms, Risks) (“Risks”)
Threat
Engineers
Catalogs 23

## Slide 23

Many AI threat catalogs — Ways to answer “what can go wrong”

- Berryville’s ML + LLM Risk Analyses

- • OWASP Top 10 LLMs

- OWASP AI Exchange

- • MITRE ATLAS

- NIST AIML E2025

- Google SAIF

-

- …

Threat
Catalogs

Structured ways to answer “What can go wrong” More organized than ”We’ll red team it”

## Slide 24

## The PHANTOM-B Approach

**25**

## Slide 25

## Why PHANTOM-B?

**26**

## Slide 26

## The alternatives suck All models are wrong, some models are useful.

**27**

## Slide 27

What goes wrong with TM structures? (Each “for some users”)

- High training cost (learning is hard)

- Hard to use (even after training)

- Not LLM/AI focused

- Duplicative/overlaps other frameworks/security work

- • Raises threats which are irrelevant/can’t fix/won’t fix

- – “Academic”

- Low return on investment

- Require software support

## Slide 28

### PHANTOM-B origin story (1/2)

**29**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
PHANTOM-B origin story (1/2)
aadeline
designing wo: security
Al world
EXPANDED AND REVISED
SECOND EDITION
Adam Shostack
WILEY
Threat Modeling: Designing for Security in an Al cy
World
by Adam Shostack (Author) Format: Paperback
iy) Savings Pre-order Price Guarantee. Terms
A major update to the definitive guide on threat modeling techniques for secure by design
More than just a second edition, Threat Modeling: Designing for Security in an Al World
thoroughly updates and expands on Adam Shostack's classic text and structured approach to
analyzing and designing systems, software, and services for security flaws to address threats
and technologies that didn’t exist when the first edition published. Most notably every reader
will benefit from two new chapters covering using LLMs to threat model and exploring threats
to LLMs, Als, and ML Models themselves. There’s a new deep focus on agile and an expansion
of who's involved in threat modeling, now including non-technical product owners. All
told, half of this edition is completely new or heavily revised.
SHOSTACK 29
+ ASSOCIATES
```

## Slide 29

### PHANTOM-B origin story (2/2)

- Built and iterated over several versions

   - On our own projects

   - With hyperscalers, globally significant banks and others

- Earlier versions didn’t meet our release quality bar

   - TRAPHOME

   - PHANTOMED

**30**

## Slide 30

### PHANTOM-B is inspired by STRIDE

- [Spoofing, Tampering, Repudiate, Info disclose, DoS, Expand Authority]

- Time-tested + durable mnemonic from Kohnfelder + Garg

- STRIDE remains broadly applicable

**31**

## Slide 31

PHANTOM-B identifies: “What can go wrong deploying AI?”

Prompt injection Hallucination

- Free to use (CC-BY)

- Memorable

Anthropomorphization

- 100% threat-focused

Non-explainable

Training issues

Over-reliance

Missing security engineering Bias

- Fits on a wallet card

PHANTOM-B threat modeling framework
> P rompt injection
> H allucination
> A nthropomorphization
> N on-explainability
> T raining issues (including data quality or “poison”)
> O ver-reliance on the LLM
> M issing security engineering
> B iases

**32**

## Slide 32

### Focused on using/calling LLMs

- Under your control (on your GPUs or Amazon Bedrock)

   - “Downloaded from Huggingface”

- An LLM provider offers, such as ChatGPT or Claude

   - Via the API

   - (Not useful for “using chatgpt.com in a browser”)

**33**

## Slide 33

### Prompt injection

- Controlling LLM behavior via input

   - Code/data confusion

- More than just funny stories

   - Bypasses your controls and gets the LLM to violate rules

   - Unlike SQLi, no deterministic, proven defenses exist

**34**

## Slide 34

### Hallucination

- The LLM makes stuff up

- The LLM makes up stuff we don’t like:

   - Bad code

   - False citations

**35**

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

**36**

## Slide 36

Chew up tokens!

**37**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ByteDance and Alibaba to disable humanlike AI
custom agents as new rules loom
With Beijing’s rules on humanlike AI interaction services
taking effect on July 15, Doubao and Qwen move to disable
customised features
arXiv:2604.07729 (cs)
[Submitted on 9 Apr 2026]
Emotion Concepts and their Function ina
Large Language Model
Nicholas Sofroniew, Isaac Kauvar, William Saunders, Runjin Chen, Tom Henighan, Sasha
Hydrie, Craig Citro, Adam Pearce, Julius Tarng, Wes Gurnee, Joshua Batson, Sam Zimmerman,
Kelley Rivoire, Kyle Fish, Chris Olah, Jack Lindsey
SHOSTACK 37
+ ASSOCIATES
```

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

**38**

## Slide 38

### Training issues

- LLMs do better as we give them more data

- So your LLM was probably trained on Stack Exchange, Reddit + Twitter

- Good luck finding that in the model card!

- Data poisoning is “scale invariant” with 250 documents

Souly, et al, Poisoning Attacks on LLMs Require a Near-constant Number of Poison Samples, 8 October 2025, _https://arxiv.org/abs/2510.07192_

**39**

## Slide 39

### Over-reliance on the LLM

- We trust the LLM and don’t pay close attention

- LLMs generate a lot of text / code

   - Hard to focus on

   - Often okay

- Hard to remain vigilant

🤷

- Your code, your brand

🤯

- Making decisions about hiring, college admissions, arrests…

**40**

## Slide 40

**41**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Investigations | Jul 17 2026
Black prisoners are assigned
harsher living conditions in
Ontario jails—thanks to Al
Ontario jails are using a program that claims it can predict
prisoners’ behaviour, disproportionately putting Black
prisoners in higher-security facilities
SHOSTACK
+ ASSOCIATES
41
```

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

**42**

## Slide 42

**43**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
LEMS WRITE YOU HAVE OTHER
AND TEST OUR CODE ‘seeunrry ENGINEERING, RIGHT?
FRIGHT?
43
```

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

**44**

## Slide 44

PHANTOM-B identifies: “What can go wrong deploying AI?” Prompt injection Hallucination Anthropomorphization Non-explainable Training issues Over-reliance Missing security engineering Bias

**45**

## Slide 45

### Using PHANTOM-B

- “What can go wrong”

- Many broader than “the math”

- Product-manager or exec suite

**46**

## Slide 46

### PHANTOM-B illustrates why TM matters

- Engineering requires tradeoffs between unsatisfiable constraints

   - Features, reliability, speed, cost, quality ... and security

   - Building security in is better than bolting-on controls

- Before you write (or vibe) a line of code, consider what can go wrong

   - Threat modeling lets you do this via the Four Questions

   - PHANTOM-B lets you do this for LLMs

- This gives you the most options for what are we going to do

**47**

## Slide 47

### Summary

- Threat modeling enables strategic views of security

- What can go wrong with LLMs requires innovative approaches

- PHANTOM-B balances coverage + accessibility

**48**

## Slide 48

### Bonus!

- Today: Book signing – bookstore, Breaker Rooms @ 12:45

- Thursday: AI Threat Modeling Community meetup

   - Noon tomorrow “The Convergence, Business Hall”

**49**

## Slide 49

Thank you!

## Slide 50

# PHANTOM-B approach to LLM TM Blackhat USA August 2026 Questions?

adam@shostack.org

Slides: Shostack.org/blog

Wallet cards, book signing at Bookstore, 12:45 PM today

Meetup, The Convergence, Noon tomorrow

## Slide 51

Supporting Materials Shostack + Associates Don’t just understand security. Build it in.

**52**

## Slide 52

### Free resources

- shostack.org/resources

- shostack.org/blog

- youtube.com/c/Shostack

- Books

- Linkedin Learning

Books free at your library/various subscriptions; Linkedin Learning via work

**53**

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

**54**

## Slide 54

## info@shostack.org shostack.org/contact

**55**

## Slide 55

## backup

**56**

## Slide 56

**57**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
{ umor:2025
Prompt
Injection
LLM01:2025
Prompt Injection
A Prompt Injection
Vulnerability occurs when
user prompts alter the...
Read More
[umos: 2025
Excessive
Agency
LLM06:2025
Excessive Agency
An LLM-based system is
often granted a degree of
agency...
Read More
Tuma: 2028 9
Sensitive
Information
Disclosure
LLM02:2025
Sensitive
Information
Disclosure
Sensitive information can
affect both the LLM and its
application...
Read More
[ usor: 2028]
System
Prompt
Leakage
LLM07:2025
System Prompt
Leakage
The system prompt leakage
vulnerability in LLMs refers
to the...
Read More
LLM03:2025 Supply
Chain
LLM supply chains are
susceptible to various
vulnerabilities, which can...
Read More
[uumos: 2025 )
Vector and
Embedding
Weaknesses
LLM08:2025 Vector
and Embedding
Weaknesses
Vectors and embeddings
vulnerabilities present
significant security risks in
systems...
(umo4: 2028)
Data and
Model
Poisoning
LLM04:2025 Data
and Model
Poisoning
Data poisoning occurs when
pre-training, fine-tuning, or
embedding data is...
Read More
Misinformation
LLM09:2025
Misinformation
Misinformation from LLMs
poses a core vulnerability for
applications relying...
Read More
Improper
Output
Handling
LLM05:2025
Improper Output
Handling
Improper Output Handling
refers specifically to
insufficient validation,
sanitization, and...
Read More
(mio: 2025 }
Unbounded
Consumption
LLM10:2025
Unbounded
Consumption
Unbounded Consumption
refers to the process where
a Large Language...
Read More
sdyqy
/01-do}-w}}/610'dsemoleuab//
```

## Slide 57

X

X

# X

# X

# X

**58**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
{ umor:2025
Prompt
Injection
LLM01:2025
Prompt Injection
A Prompt Injection
Vulnerability occurs when
user prompts alter the...
Read More
[umos: 2025
Excessive
Agency
LLM06:2025
Excessive Agency
An LLM-based system is
often granted a degree of
agency...
Read More
Tuma: 2028 9
Sensitive
Information
Disclosure
LLM02:2025
Sensitive
Information
Disclosure
Sensitivinforgmation can
affect bot! LLM and its
applicati
Read More
[ usor: 2028]
System
Prompt
Leakage
LLM07:2025
System Prompt
Leakage
The system pro leakage
vulnerability in efers
to the...
Read More
LLM03:2025 Supply
Chain
LLM supply chains are
suscepypl various
vulneral s, which can...
Read Mre
[uumos: 2025 )
Vector and
Embedding
Weaknesses
LLM08:2025 Vector
and Embedding
Weaknesses
Vectors and embeddings
vulnerabilities present
significant security risks in
systems...
(umo4: 2028)
Data and
Model
Poisoning
LLM04:2025 Data
and Model
Poisoning
Data poisoning occurs when
pre-training, fine-tuning, or
embedding data is...
Read More
Misinformation
LLM09:2025
Misinformation
Misinformation from LLMs
poses a core vulnerability for
applications relying...
Read More
Improper
Output
Handling
LLM05:2025
Improper Output
sanitization, and...
Read More
([uumio:2025 J
Unbounded
Consumption
LLM10:2025
Unbounded
Consumptio
Unbounded Consugpti
refers to the process where
a Large Language...
Read More
sdyqy
/01-do}-w}}/610'dsemoleuab//
```

## Slide 58

- Berryville Institute of Machine Learning • Think tank of security + ML experts studying machine learning sec <u>https://berryvilleiml.com/</u>

- Taxonomy of threats (2019)

   - Manipulation of input, data, models

   - Extraction of input, data, models

- Architectural Risk Analysis of a generic ML system (2023)

- ARA for LLM (2024)

- Elevation of ML card deck!

https://agilestationery.com/collections/security/products /elevation-of-machine-learning-security-card-game

- Annotated bibliography

**59**

## Slide 59

**60**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ATLAS Matrix for Al Systems
Reconnaissance®
8 techniques
Resource
Development®
13 techniques
Initial
Access®
7 techniques
Al Model
Access
4 techniques
Execution®
6 techniques
Subtechniques
Expand All
Persistence®
9 techniques
Privilege
Escalation®
4 techniques
Collapse All
Defense
Evasion®
15 techniques
Filler Dy Ivia@lLUrily
Feasible Demons
Credential  Discovery®
Access®
6 techniques 9 techniques
Active
Scanning ®
Gather RAG-Indexed
Targets
Gather Victim
Identity
Information &
Search Application
Repositories
Search Open Al
Vulnerability
Analysis
Search Open
Technical
Databases &
Search Open
Websites/Domains &
Search Victim-
Owned
Acquire
Infrastructure
Acquire Public
Al
Artifacts
Develop
Capabilities &
Establish
Accounts &
LLM Prompt
Crafting
Obtain
Capabilities ®
Poison
Training
Data
Publish
Hallucinated
Entities
Al Supply
Chain
Compromise
Drive-by
Compromise &
Evade Al
Model
Exploit Public-
Facing
Application ®
Phishing & o
Prompt
Infiltration via
Public-Facing
Application
Valid
Accounts &
Al Model
Inference
API
Access
Al-Enabled
Product or
Service
Full Al
Model
Access
Physical
Environment
Access
Al Agent Al Agent Al Agent
Clickbait Context Tool
Poisoning Invocation
Al Agent
Tool Al Agent Tool Escape to
Invocation Data Host &
Poisoning
Command LLM
and Al Agent Tool Jailbreak
Scripting Poisoning
Interpreter & Valid
LLM Prompt A &
Deploy Al Self-Replication counts
Agent
gen Manipulate Al
LLM Model
Prompt ;
Injection Modify Al
Agent
User Configuration
ion &
Execution Poison Training
Data
Prompt
Infiltration via
Public-Facing
Al Supply Chain
Reputation
Inflation
Al Supply Chain
Rug
Pull
Corrupt Al
Model
Delay Execution
of LLM
Instructions
Evade Al
Model
Exploitation for
Defense
Evasion &
False RAG Entry
Injection
Impersonation &
Al Agent Tool Cloud Service
Credential Discovery &
Harvesting
Discover Al
Credentials Agent
from Al Configuration
Agent
Configuration piscover Al
oe Artifacts
Exploitation
for Discover Al
Credential Model
Access & Family
Os Discover Al
Credential Model
Dumping® Ontology
RAG Discover Al
Credential Model
Harvesting Outputs
Unsecured Discover LLM
Hallucinations
Discover LLM |
Cuetam
Credentials &
```
