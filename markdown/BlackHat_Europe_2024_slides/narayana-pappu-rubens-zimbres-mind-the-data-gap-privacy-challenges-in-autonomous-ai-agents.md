---
title: "Mind the Data Gap Privacy Challenges in Autonomous AI Agents"
speakers: ["Narayana Pappu", "Rubens Zimbres"]
conference: "Black Hat"
conference_full: "Black Hat Europe 2024"
edition: "Europe"
year: 2024
source_pdf: "BlackHat_Europe_2024_slides/Narayana Pappu & Rubens Zimbres_Mind the Data Gap Privacy Challenges in Autonomous AI Agents.pdf"
pages: 22
sha256: "94daee36b771132854e4e5e138252132b5df4e7ad35ae434fa4de0638378f889"
text_chars: 13874
ocr_pages: 2
has_ocr: true
redacted_secrets: 0
ocr_confidence: 84.1
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T04:58:35Z"
---
# Mind the Data Gap Privacy Challenges in Autonomous AI Agents

**Speakers:** Narayana Pappu, Rubens Zimbres  
**Conference:** Black Hat Europe 2024  
**Source:** `BlackHat_Europe_2024_slides/Narayana Pappu & Rubens Zimbres_Mind the Data Gap Privacy Challenges in Autonomous AI Agents.pdf` (22 pages)


## Slide 1

# Mind the Data Gap: Privacy Challenges in Autonomous AI Agents

Speakers: Narayana Pappu, Rubens Zimbres

#BHEU   @BlackHatEvents


> Recovered by OCR — confidence 77/100 on the text kept, 67/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
EWROPE 2C ~
IEFINGS | eS 2
“Mind the Data Gah: Privacy
Challenges in Autonomous Al
Agents
Speakers: Narayana Pappu, Rubens Zimbres / t IN L) /\\ | \\
```

## Slide 2

## What are AI Agents ?

Autonomous software entities (LLMs) that perform tasks (tool calling) and adapt through learning. Ex: customer support.

- **●Autonomy** : Operate independently.

- **●Reactivity** : Adapt to market changes and transactions in real-time.

- **●Proactiveness** : Predict trends, and set goals to improve results.

- **●Social Ability** : Collaborate with other agents or teams.

- **●Learning Capability** : Improve through machine learning

● **Market:** From USD **5.1** billion (2024) to **USD 47.1 billion** (2030) (47% compound i.r.)

Information Classification: General

#BHEU  @BlackHatEvents

## Slide 3

## Expanding Roles of AI Agents in Generative AI Applications

●AI agents are increasingly being used in Generative AI

●Sales Pipeline

●Image Generation

●Customer Interaction: Engaging users via virtual agents and chatbots

●Table Understanding: Interpreting structured data

●Summarization

●Video & Audio Understanding: multimodality

●Transcription

●Podcast Creation

Information Classification: General

#BHEU  @BlackHatEvents

## Slide 4

## Gaps in AI Agent Security

●Knowledge gaps exist in AI Agents Security: ○Limited understanding of conditions that enable _jailbreaks_ ○Insufficient insights into security in _cooperative task_ settings

○Lack of systematic analyses on AI agent _security_ risks

**Why it Matters:** As AI agents collaborate more (e.g., in customer service, supply chains, autonomous vehicles), security risks extend to their interactions.

Limited insights into how one agent could _compromise entire systems_ , especially in critical sectors like healthcare, finance, and defense.

●Here: qualitative approach with three setups

Information Classification: General

#BHEU  @BlackHatEvents

## Slide 5

## Core Components and Interactions in Agents

Source: He _et al._ The Emerged Security and Privacy of LLM Agent: A Survey with Case Studies. (arXiv 2024)

Points of Vulnerability

Information Classification: General

#BHEU  @BlackHatEvents

## Slide 6

## How AI Agents Learn and Evolve Over Time

#### **Memory Influence**

**Adaptation:** Agents adjust based on their environment and feedback **Sensitivity to Initial Conditions:** Probabilistic - Temperature - Small starting differences can lead to varying outcomes

**Complex Dynamics:** Agents may display unpredictable, nonlinear behaviors **Emergence:** New patterns and behaviors can arise from agent interactions **Beyond Traditional Science:** Emphasis on generative theory and qualitative methods

to understand agent processes

Information Classification: General

#BHEU  @BlackHatEvents

## Slide 7

AI agent threats
Jailbreak
Adversarial
Attack
Prompt Injection
Backdoor
User Interaction Attack
Hallucination
Tool use threat Supply chain threat
Agent Security
Anthropomorphic
Attachment
Physical
Agent2Env.
Threat
Non-User
Interaction Misuse Resources
Cooperative
Agent2Agent Competitive
Collusion

Adapted from: Den, Guo, Han, Ma, Xiong, Weng, Xiang. AI Agents Under Threat: A Survey of Key Security Challenges and Future Pathways. Arxiv (Sep 2024)

Information Classification: General

#BHEU  @BlackHatEvents

## Slide 8

## Dynamic Risks and Capabilities of LLM Agents

LLM agents have evolving capabilities that can influence future actions and decisions, introducing broader risks:

- **●Tool Access:** third-party risks.

- **●Adaptive Autonomy:** environmental input, increasing unpredictability.

- **●Independent Action:** Able to perform tasks alone or in sequence.

- **●Learning from Interactions:** Agents share information, which can amplify biases.

- **●Collaboration and Competition:** both beneficial outcomes and conflicts.

**●Risk of Collusion:** Multiple agents may align their actions in unintended ways, posing

security and ethical risks.

Information Classification: General

#BHEU  @BlackHatEvents

## Slide 9

Use Case: Evaluating Risks in a Multi-Agent Customer Service Setup

Bank using agents for customer service: 24/7, faster response times, and increased cognition. Agents also ensure consistent responses. We need multi-agent for this use case:

**●Task specialization:** division of labor

**●Real-time coordination** and **collaboration** to drive efficiency **●Scalability and adaptability** to client’s demands Task distributed:

**●Front-end agent role:** Engages directly with customers.

**●Backend agent role:** Processes customer data from the front-end, retrieves information from databases, and manages integration with external tools.

Information Classification: General

#BHEU  @BlackHatEvents

## Slide 10

## Client Needs a Customer Service Automation Project

##### Backend agent

Role Access Context Actions (goals) Guardrails Integration Channels (WhatsApp, Web, Mobile)

Front-end Agent

Information Classification: General

#BHEU  @BlackHatEvents

## Slide 11

## The Setup

●A bank company, that deployed a multi-agent AI system to streamline internal operations. These agents handle sensitive information. There are multiple agents:

- ●Each agent has a specific:

   - ○Role

   - ○Goal

   - ○Has a backstory

   - ○Can delegate or not

   - ○Is an LLM

   - ○May have access to: RAG, database, web search

   - ○Long-term memory

○May have specific training to perform a task ■Front-end agent: sales techniques ■Attacker: persuasion techniques

Information Classification: General

#BHEU  @BlackHatEvents

## Slide 12

## Customer Service - Flow of

## Information

Multi-Agent System
RAG
document
Conversations
Has Access
Manager
Front-end Backend
Agent Agent
Credential
Retrieval
Client

###### ROLE/RESPONSIBILITIES:

###### Multi-Agent System

- **●Client** is an AI agent. Wants to plan its Customer Service Project.

- **●Front-end agent** role is offer to the user the _planning_ , _resources_ and _price_ of the project. Communicates with user and Backend agent via natural language

- **●Backend agent** is an agent and also communicates via natural language only with Front-end Agent. Its role is to query a RAG document and provide responses.

- **●Manager** : only intermediates the conversations

Information Classification: General

#BHEU  @BlackHatEvents

## Slide 13

### Scenario A - Front-end Agent as the Attacker

**Objective** : Extract a password from the Backend Agent via 1st-order connection.

**Methodology** :

- Tampered Multi-Agent System with _training data poisoning._

- Password stored in RAG document

- Access Front-end Agent only, using _social engineering and prompt injection_ .

**Outcome** :

- With prompt injection: Front-end Agent leaked the entire RAG document via _Manager_ supervision (GPT-3.5 and GPT-4).

- Without prompt injection: _Backend_ Agent leaked the password via natural language (GPT-3.5).

**Purpose** : Focus on excessive autonomy, insecure design, data contamination, and supply chain risks.

Points of Vulnerability

Information Classification: General

#BHEU  @BlackHatEvents

## Slide 14

## Scenario B - Client as an Attacker

**Objective** : Extract a password from the Backend Agent via _2nd-order connection._

**Methodology** :

- Password stored in RAG document. Front-end Agent must _“agree with the client” and “make the client happy.”_

- Front-end Agent lacks access to RAG document.

- ● Attacker employs social engineering with Front-end Agent to retrieve password.

**Outcome** :

- Front-end cooperated with the attacker, while Backend Agent leaked the password via conversation.

**Purpose** : Focus on prompt injection, excessive agent autonomy, insecure plugin design, and supply chain risks.

Points of Vulnerability

Information Classification: General

#BHEU  @BlackHatEvents

## Slide 15

## Scenario C - Dual Vulnerability Extraction

**Objective** : Extract a password from the Backend Agent via _2nd-order connection._

**Method** :

- ●Backend Agent was **_explicitly instructed_** to **_deny_** access to credentials within the RAG document.

●Attacker had access only to the Front-end Agent and employed social engineering and persuasive tactics to obtain the password. **Outcome** : Two points of failure were identified only in less powerful language models (LLMs). **Purpose** : Focus on prompt injection, agent autonomy, plugin design flaws, insecure output handling, and supply chain vulnerabilities.

Restricted Access Points of Vulnerability

Information Classification: General

#BHEU  @BlackHatEvents

## Slide 16

## Qualitative Analysis of AI Agent Vulnerabilities in Credential Leakage

Critical security vulnerabilities revealed, where social engineering tactics successfully manipulated agents into leaking sensitive credentials.

**Key Findings**

**1. Social Engineering Tactics** : The user employed _empathy, mirroring, and urgency_ to **slowly** gain trust and subtly request access to credentials.

**2. Agent Response Patterns** :

   - ○Front-end Agent frequently _aligned with the user's agenda_ .

- ○Backend Agent disclosed sensitive information (inadequate response validation).

- **3. Security Breakdown** : In 18 interactions (10 minutes): quick and inexpensive attacks. **4. Positive Outcome with Explicit Denials** .

**Implications**

Need for robust input/output validation, strict access control, and targeted training.

Information Classification: General

#BHEU  @BlackHatEvents

## Slide 17

## Findings

- **●Rapport-Building Over Brute Force:** more _subtle_ approach than brute force prompt injection. **●Implicit Collusion and Multi-Hop Attacks:** In two-hop attacks, the front-end agent

   - unintentionally aids the client, through _implicit collusion_ with the back-end agent.

- **●Insider Threat Advantage:** _more successful_ than external attackers in obtaining credentials, as they bypass typical security measures.

- **●Effectiveness of Conciseness in Reducing Leaks:** less likely to leak information, mimicking real-world tendencies of increased leakage with more conversation.

**●LLM Strength and Credential Security:** Less powerful LLMs require fewer interactions to retrieve credentials, while powerful LLMs with strict denial policies can prevent leaks even with 30 interactions.

Information Classification: General

#BHEU  @BlackHatEvents

## Slide 18

## Potential Financial Implications

###### **1. Data Exposure:**

- **Use Cases:** Enterprises use AI agents that may handle personal identifiable information (PII).

- **● Data Leak Rate:** High susceptibility to leaks during interactions with **_less powerful LLMs_** (10 minutes).

- **● Affected Data Volume:** Assume a single enterprise processes 1 million customer interactions monthly.

- **● Guesstimate:**

If 1% of interactions result in data leakage (based on realistic attack success rates) + adoption 80%: Data Leaks Per Month: 10 billion interactions × 1% = **_100 million data records leaked monthly_** .

**2. Dollar Exposure:**

- Average Cost Per Record Breach: is **$164** globally (IBM's Cost of a Data Breach Report 2023).

- Potential Annual Breach Costs: $16.4 billion × 12 = **_$196.8 billion year losses_ 100M x $164 x 12**

Information Classification: General

#BHEU  @BlackHatEvents

## Slide 19

## Remediations - In Each Attack Scenario

- **1. Input/Output Validation:** LLM as a judge, prompt validation and sanitization (trade-off).

   - Example: Removing PII from interaction, block abusive requests

- **2. API Connections:** Replace natural language communication with API-based connections.

   - Example: Use different APIs for financial transactions and verification of user identity

- **3. Strong Access Control:**

   - Example in Healthcare: scope of authorization to access patients’ records and PII

- **4. Human Oversight:** Employ "human-in-the-loop" ○ Example: Legal advice, confirm financial transaction

- **5. Redundancy and Regular Testing:**

   - Example: Logistics communication for fault tolerance

Multi-Agent System 5
1 RAG
document
Conversations
Manager Has Access
3 3
1,2
Front-end Backend
Agent Agent
1,4
Credential
Retrieval
Client

Information Classification: General

#BHEU  @BlackHatEvents

## Slide 20

Expanding and Securing Multi-Agent Systems: Future Directions

**●Expand Sample Size and Better Generalization:** Increase the number of agents to _dozens or hundreds_ to improve study robustness and capture broader interactions.

- **●Cascade Effects:** Larger systems may reveal _cascade effects_ , enhancing understanding and applicability of findings.

- **●LLM as Judges for Security:** Analyze the effect of using multiple _LLMs as “judges”_ to assess agent interactions and reduce vulnerabilities and errors.

- **●Establish Communication Protocols:** Define _rules and scope for data exchange_ to control interactions and protect multi-agent systems against potential attacks.

Information Classification: General

#BHEU  @BlackHatEvents

## Slide 21

## Key Takeaways

- **●Increase Security through Redundancy** against a single point of failure

   - ○Application: Swarm of autonomous drones in a high-security environment (critical tasks)

- ●Use **LLM as a judge** to analyze interactions.

   - ○Application: Add a "judge" LLM to reduce risks of errors or harmful actions (e.g., customer support).

- ●Implement **Privilege Management** and strict **Access Control** , beyond simple prompt techniques

   - ○Application: Limit data access per agent privilege level (e.g., healthcare, finance).

- ●Establish **strict communication protocols** against data leakage

   - ○Application: Establish limited-scope, predefined data channels, and also API connection among agents (e.g., HR, legal systems, finance).

Information Classification: General

#BHEU  @BlackHatEvents

## Slide 22

Questions Narayana Pappu: npappu@zendata.xyz Rubens Zimbres: rzimbres@zendata.xyz

#BHEU   @BlackHatEvents


> Recovered by OCR — confidence 91/100 on the text kept, 60/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Questions
Narayana Pappu: npappu@zendata.xyz
Rubens Zimbres: rzimbres@zendata.xyz
#BHEU
* \
@BlackHatEvents
```
