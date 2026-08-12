---
title: "Enhancing Modern Threat Intelligence The Pivotal Role of Large Language Models in Extracting Actionable TTP Attack Chains"
speakers: ["Lorin Wu", "Porot Mo", "Jack Tang"]
conference: "Black Hat"
conference_full: "Black Hat ASIA 2025"
edition: "ASIA"
year: 2025
source_pdf: "Black Hat Asia 2025 Slides/Lorin Wu & Porot Mo & Jack Tang_Enhancing Modern Threat Intelligence The Pivotal Role of Large Language Models in Extracting Actionable TTP Attack Chains.pdf"
pages: 37
sha256: "f82fc21d66036da4cafcd0c63d7106f8c295fd9867f51ba950f6de56497d4b4b"
text_chars: 24023
ocr_pages: 0
has_ocr: false
redacted_secrets: 0
ocr_confidence: null
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2"
converted_at: "2026-08-12T03:55:06Z"
---
# Enhancing Modern Threat Intelligence The Pivotal Role of Large Language Models in Extracting Actionable TTP Attack Chains

**Speakers:** Lorin Wu, Porot Mo, Jack Tang  
**Conference:** Black Hat ASIA 2025  
**Source:** `Black Hat Asia 2025 Slides/Lorin Wu & Porot Mo & Jack Tang_Enhancing Modern Threat Intelligence The Pivotal Role of Large Language Models in Extracting Actionable TTP Attack Chains.pdf` (37 pages)


## Slide 1

Enhancing Modern Threat Intelligence The Pivotal Role of Large Language Models in Extracting Actionable TTP Attack Chains

Jack Tang , Lorin Wu, Porot Mo

#BHAS @BlackHatEvents

## Slide 2

## About Us

- Jack Tang

Jack, the team leader, has over 15 years of expertise in the security industry and is presently focusing on the use of MITRE ATT&CK® in security operations and threat intelligence. He is knowledgeable on kernel and virtualization vulnerability research for Android, Mac, and Windows. He ranked Top 16 on the MSRC in 2016 and Top 34 in 2015. In 2016, he was awarded the Microsoft Mitigation Bypass Bounty. Jack has lectured at security conferences such as CanSecWest, Black Hat, HITCon, and PacSec.

###### • Lorin Wu

Building an offensive and defensive knowledge graph for cyber security is what Lorin is currently working on. He spent many y ears working at Trend Micro, where he concentrated on the creation of heuristic patterns and mobile sandbox technologies. During t his period, he identified various international cyber security operations that were reported to INTERPOL and Google Security Team.

- Porot Mo

Porot received a master's degree from the University of Chinese Academy of Sciences after graduating from the University of Science and Technology of China. He is currently devoted to the study of offensive and defensive technologies and has three years of expertise in sandbox development.

#BHAS @BlackHatEvents

## Slide 3

## Agenda

- Background

- Solution Introduction

   - Key Modules & Architecture Overview

- Solution Implementation & Results

   - TTP Extraction Evolution (Three Ages) & KGRAG-Based TTP Extraction

   - KGRAG-Based TTP Attack Chain Enrichment

   - RAG-Based TTP Actionable Conversion

- Takeaways

#BHAS @BlackHatEvents

## Slide 4

## Background

- Understanding TTP: Tactics, Techniques, and Procedures

- The Significance of TTP Extraction and Actionable Conversion

- The Challenges of TTP Extraction and Actionable Conversion

#BHAS @BlackHatEvents

## Slide 5

##### Background - Understanding TTP: Tactics, Techniques, and Procedures

###### Procedure

###### Tactic

- The stage-specific objective of an adversary's actions.

      - The specific implements adversaries take to execute a technique.

      - Example

- Examples

   - Privilege Escalation ( **_TA0004_** )

   - Lateral Movement ( **_TA0008_** )

###### Technique

- The methods adversaries use to achieve their tactical goals.

- Examples

   - Process Injection ( **_T1055_** )

   - Exploitation of Remote Services ( **_T1210_** )

- XXXAPT has used **_Mimikatz_** to exploit a **_domain controller_** via the **_ZeroLogon_** exploit (CVE-2020-1472).

MITRE ATT&CK provides a unified language for TTP communication and the usage of offensive-

defensive knowledge

#BHAS @BlackHatEvents

## Slide 6

##### Background - The Significance of TTP Extraction

- Defense Upgrade

   - From passive(Static IOC) to proactive(TTP) defense

- Why Accurate TTP Extraction Matters

   - **Granularity Foundation** : TTPs are the smallest unit of cyberattack behavior decomposition.

   - **Analysis & Defense Dependency** : Effective threat hunting, attribution, detection and mitigation are all based on TTP-level granularity.

      - MITRE ATT&CK Detection Model (Data Source/Data Component/Technique)

      - Other Security Products Detection Model e.g. XDR Rule for TTP sequence/data elements/data sources by providing telemetry data

      -

David J. Bianco，2013，FireEye Pyramid of Pain

Shifting Focus from Indicators of Compromise (IOC) to Adversary Behavior (TTP).

#BHAS @BlackHatEvents

A MITRE ATT&CK detection model, Process Injection(T1055)

## Slide 7

##### Background - The Significance of TTP Actionable Conversion

- Why TTP Actionable Conversion Matters?

   - **TTP Intelligence Operationalization** : Bridging Theory(TTP Context) to Actionable Exercises

      - Enables real-time **detection of code-level** attack behaviors and rapid respond by SOAR playbooks (EDR/SEIM/SOAR…)

One playbook from 360 BAS platform, based on an actionable TTP attack chain

- Brings actionable TTPs into **simulatable** and **executable** attack scenarios, e.g. red-blue drills, pen testing and BAS platforms... Provides verifiable improvement measures for depth-defense systems

#BHAS @BlackHatEvents

## Slide 8

##### Background - The Challenges of TTP Extraction and Actionable Conversion

###### The Challenges of TTP Extraction

- Reports Designed to Be **Human Readable**

- Always Contain **Overly Subjective Descriptions** in Threat Reports

- Always Contain **Overly Abstract Descriptions ,** Mismatch Between Reports and Real Attack Chains: **Ignoring Assets/Environment Context**

###### The Challenges of TTP Actionable Conversion

- Purely Manual, **Extremely Time-consuming**

- Depends on **Personnel Knowledge and Skills**

#BHAS @BlackHatEvents

## Slide 9

## Solution Introduction

- Key Modules

- Architecture Overview

#BHAS @BlackHatEvents

## Slide 10

### Solution Introduction - Key Modules

- Attack Path Generator

   - Analyze threat reports to **extract attack path descriptions** (the sequence of behaviors adversaries take during an attack).

- TTP Chain Generator

   - Converts unstructured attack path descriptions into **structured TTP chains** with standardized fields (TTP: the procedure description, tactics and techniques, vulnerabilities exploited, targeted assets, tools used …) accurately and automatically.

- TTP Chain Enricher

   - **Supplements missing TTPs** in the chain to ensure both completeness and realism of the attack chain (Based on the reasoning engine by structed TTPs ).

- Actionable TTP Chain Generator

   - Translates structured TTP chains into **executable code or automation scripts** for further defense tasks.

#BHAS @BlackHatEvents

## Slide 11

Threat Reports
(APT/Ransom/Miner/Malware…)
Attack Actionable
TTP Chain TTP Chain
Path TTP Chain
Generator Enricher
Generator Generator
LLM LLM LLM LLM
KGRAG KGRAG RAG
① Fine-tuned TTP Extractor
Knowledge
TTP Chain Synthesizer
Graph
TTP Verifier/Rethink Module ①②③
②

Phishing Text Downloaders/Droppers New Modules or msfconsole Commands
(Lures) of Metasploit Framework

#BHAS @BlackHatEvents

## Slide 12

## Solution Implementation & Results

- TTP Extraction Evolution (Three Ages)

   - Bronze Age: Traditional ML/DL (Baseline Accuracy)

   - Silver Age: Pre-trained Model/BERT Fine-tuning (Enhanced Accuracy)

   - LLM Age: LLM Generation (SOTA Accuracy)

- KGRAG-Based TTP Extraction

- KGRAG-Based TTP Chain Enrichment

- RAG-Based TTP Actionable Conversion

#BHAS @BlackHatEvents

## Slide 13

##### TTP Extraction Evolution - Bronze Age: Traditional ML/DL (Baseline Accuracy)

nz. v. n. n. wp v. n. p. ws. n.
Ransomware employs RSA algorithm to encrypt computers’ all files.

An example about semantic dependency analysis

###### Traditional Machine Learning

- Data Preprocessing

- Deep-level Sentence Segmentation

- **Semantic Dependency Analysis**

- Synonym Expansion

- **Bag-of-Words (BOW)** Model to Engineer Features

- Train and Predict with Selected Models

###### Deep Learning

- Recurrent Neural Networks (RNN)

- **Long Short-Term Memory** (LSTM)

   - Addresses **gradient vanishing/exploding issues** in long sequences

…write to registry… Token Embedding Layer

LSTM Layer

Full Connect Layer
Registry
Mo
Input Cap
SSH

#BHAS @BlackHatEvents

## Slide 14

##### TTP Extraction Evolution - Bronze Age: Traditional ML/DL (Baseline Accuracy)

2019, NER extraction as the task based on Deep Learning https://i.blackhat.com/USA-19/Thursday/us-19-Soman-Death-To-The-IOC-WhatsNext-In-Threat-Intelligence.pdf

2022, MITER Tram project based on Machine Learning, https://github.com/center-for-threat-informed-defense/tram/

2021, Lorin Wu & Porot Mo at Internet Security Conference2021, **Topic: Leverage AI to Extract TTP Automatically from Unstructured Reports**

Excessive Preprocessing; Feature Engineering Dependency; Weak Generalization

#BHAS @BlackHatEvents

## Slide 15

##### TTP Extraction Evolution - Silver Age: Pre-trained Model/BERT Fine-tuning (Enhanced Accuracy)

- **High-Quality Training Data** Preparation

- Pre-trained Model **Selection Strategy**

   - BERT, a groundbreaking bidirectional transformerbased model released by Google in 2018.

   - Whole Word Masking (WWM) technology, e.g. **BERT with WWM** (English, Google), **BERT-wwm-ext** (Chinese, HIT& iFLYTEK)

- Hyperparameter Auto-Tuning

   - Training Epochs/Max Sequence Length/Learning Rate

- Model Distillation and Lightweight Deployment

After the ransomware enumerates user files, the ransomware starts encrypting those files. bert-base-uncased, English

`通` 过修改注册表启动项，实现持久化。

bert-wwm- ext,C hinese

#BHAS @BlackHatEvents

## Slide 16

##### TTP Extraction Evolution - Silver Age: Pre-trained Model/BERT Fine-tuning (Enhanced Accuracy)

2022, Lorin Wu & Porot Mo at Internet Security Conference2022 **Topic: Research on Extracting TTP Entities from Unstructured Text Using SelfAttention mechanism**

**EU ATT&CK community WorkShop 2022** A proposal on using BERT to classify and extract techniques and tactics, but the specific information is not disclosed...

##### Domain Knowledge Lack; Biased Training Dependency;

2023, Lorin Wu & Porot Mo open-sourced a tool named : Luwak TTP Extractor based on ERNIE (a BERT variant) **https://github.com/Qihoo360/Luwak?tab=readme-ov-file**

#BHAS @BlackHatEvents

## Slide 17

TTP Extraction Evolution - LLM Age: LLM Generation (SOTA Accuracy)

- Generative AI/ Large Language Model

   - Universal Knowledge & Multimodal Capabilities

      - possess **encyclopedic knowledge of human language** , **code** , and **technical concepts** , enabling them to parse and contextualize complex **attack behaviors**

   - Interactive with Prompt Engineering and Adaptive Output

      - directly query LLMs to generate structured TTPs, eliminating reliance on rigid rule-based systems.

#BHAS @BlackHatEvents

## Slide 18

✗

TTP Extraction Evolution - LLM Age: LLM Generation (SOTA Accuracy)

✓

- Outdated Training Data

   - Training data often **outdated at a specific point** , however TTPs are always updated, MITRE ATT&CK are always updated…

- Hallucinations (Unreliable Generations)

   - LLMs may **generate fictional or misleading TTPs** , due to model’s architecture rather than factual evidence, e.g. unrelated TTPs or invent a nonexistent techniques.

DLL Search Order
TA0004 Privilege Escalation T1574.001
Hijacking
TA0004 Privilege Escalation T1055 Process Injection
Mutual
TA0005 Defense Evasion T1480.002
Exclusion

+++++

✓

duplicated

✗

✓

#BHAS @BlackHatEvents

## Slide 19

✗

TTP Extraction Evolution - LLM Age: LLM Generation (SOTA Accuracy)

- RAG (Retrieval-Augmented Generation): Bridging Knowledge Gaps and Mitigating Hallucinations

✓

✓

- External knowledge to keep Staying Up-to-Date

- Contextual accuracy to keep Mitigating Hallucinations

DLL Search Order
TA0004 Privilege Escalation T1574.001
Hijacking
TA0004 Privilege Escalation T1055 Process Injection
Mutual
TA0005 Defense Evasion T1480.002
Exclusion
+++++

+++++

duplicated

✗

✓

#BHAS @BlackHatEvents

## Slide 20

## Solution Implementation & Results

- TTP Extraction Evolution (Three Ages)

   - Bronze Age: Traditional ML/DL (Baseline Accuracy)

   - Silver Age: Pre-trained Model/BERT Fine-tuning (Enhanced Accuracy)

   - • LLM Age: LLM Generation (SOTA Accuracy)

- KGRAG-Based TTP Extraction

- KGRAG-Based TTP Chain Enrichment

- RAG-Based TTP Actionable Conversion

#BHAS @BlackHatEvents

## Slide 21

##### Solution Implementation - KGRAG-Based TTP Extraction

###### **Task ①**

- Use Fine-tuned BERT Model to Infer the TTPs (Promote Silver Age as Baseline)

   - Prepare the training set **with security analysts sense**

   - Finetune the model for TTP extraction **downstream labelling** task

   - Infer the result to get tactics and techniques as **candidates**

###### **Task**

###### **②**

TTP Chain
Generator
LLM
KGRAG
① Fine-tuned TTP Extractor
Knowledge
Graph
② TTP Verifier/Rethink Module

- Retrieve Similar TTPs from Vector Database and Use LL M to Extract and Rethink the Result

   - Embed and store existing TTPs from knowledge graph to vector database with **designed metadata schema**

   - Retrieve Top 10 TTP examples for **few shooting**

   - Prompt engineering with candidates and few shooting examples **for LLM reference**

#BHAS @BlackHatEvents

## Slide 22

##### Solution Implementation - KGRAG-Based TTP Extraction

Distinguish primary and secondary tactics and  TTP Chain
Generator
LLM
techniques, and extract them based on actual attack
KGRAG
Task ①
① Fine-tuned TTP Extractor
Knowledge
Primary TAID Tactic TID Technique Finetune
Graph
True TA0005 Defense Evasion T1562.001 Disable or Modify Tools ② TTP Verifier/Rethink Module
False TA0005 Defense Evasion T1112 Modify Registry
Extract tactics and techniques involved in attacks
from multiple perspectives such as command lines,
tools, and code snippets
Primary TAID Tactic TID Technique

- Distinguish primary and secondary tactics and techniques, and extract them based on actual attack scenarios

- Extract tactics and techniques involved in attacks from multiple perspectives such as command lines, tools, and code snippets

|Primary|TAID|Tactic|TID|Technique|
|---|---|---|---|---|
|True|TA0005|Defense Evasion|T1218.011|Rundll32|

#BHAS @BlackHatEvents

## Slide 23

##### Solution Implementation - KGRAG-Based TTP Extraction

• TTP Chain
Distinguish primary and secondary tactics and
Generator
LLM
techniques, and extract them based on actual attack
scenarios
KGRAG
Task ①
① Fine-tuned TTP Extractor
Knowledge
Primary TAID Tactic TID Technique Finetune
Graph
True TA0005 Defense Evasion T1562.001 Disable or Modify Tools ② TTP Verifier/Rethink Module
False TA0005 Defense Evasion T1112 Modify Registry
•
Extract tactics and techniques involved in attacks
from multiple perspectives such as command lines,  Vector Search
Embedding
tools, and code snippets
The CoughingDown threat group uses the tsvipsrv.dll
injector and the ntusers0.dat payload to execute ……
The CoughingDown threat group uses the commands
Vector Store
`net.exe stop sessionenv` and `net.exe start sessi…..
Task ② The CoughingDown threat group uses dllloader1x64.dll to create the mutex mstoolFtip32W and collect ……
Primary TAID Tactic TID Technique
True TA0005 Defense Evasion T1218.011 Rundll32 …

#BHAS @BlackHatEvents

## Slide 24

#### Solution Results - TTP Extraction Results

|Metric|Bronze Age:
Custom ML Model|Silver Age:
Finetuned BERT|LLM Age:
DeepSeek R1|KGRAG:
Finetuned BERT +
DeepSeek V3|
|---|---|---|---|---|
|**Precision**|0.515|0.626|0.608|0.942|
|**Recall**|0.428|0.593|0.741|0.772|
|**F1**|0.467|0.609|0.668|0.849|

- The test data comes from **100** threat analysis reports, with **2,579 TTPs** .

- • Bronze Age: Custom ML Model uses logistic regression, supports Chinese and English, outperformed MITRE TRAM and other models at the time, tested in May 2021.

- • Silver Age: Finetuned BERT open-sourced as Luwak TTP Extractor, based on the ERNIE model, supports Chinese and English, achieved the best performance among known models at the time, tested in January 2023.

- LLM DeepSeek R1: currently the most capable open-source model in overall performance (on par with OpenAI-o1), featuring outstanding reasoning capabilities, which we tested in its full version during March 2025.

-

- KGRAG: Finetuned BERT + DeepSeek V3: our proposed solution, tested in March 2025 alongside DeepSeek R1.

#BHAS @BlackHatEvents

## Slide 25

## Solution Implementation & Results

- TTP Extraction Evolution (Three Ages)

   - Bronze Age: Traditional ML/DL (Baseline Accuracy)

   - Silver Age: Pre-trained Model/BERT Fine-tuning (Enhanced Accuracy)

   - • LLM Age: LLM Generation (SOTA Accuracy)

- KGRAG-Based TTP Extraction

- KGRAG-Based TTP Chain Enrichment

- RAG-Based TTP Actionable Conversion

#BHAS @BlackHatEvents

## Slide 26

##### Solution Implementation - KGRAG-Based TTP Chain Enrichment

TTP Chain
Enricher
LLM
KGRAG
①②③
Knowledge
TTP Chain Synthesizer
Graph

###### **Task ①**

- Use report metadata to get possible TTPs from knowledge graph

   - LLM analyzes current report to extract meta: adversary/operation period/target regions/target vectors/…

   - Historic TTPs by same adversary/ TTPs for same vectors…

###### **②**

###### **Task**

- Use LLM identifies gaps in current TTP chain

   - Initial Access (Describe how the adversary entered? current supports phishing, exploits …)

   - Privilege Escalation (Describe how the adversary gained higher privileges? )

   - Lateral Movement (were there steps missing in network traversal?)

   - ...

###### **Task ③**

   - Reason the most appropriate TTP according to the situation of the previous/next TTP in current chain.

      - Appropriate tactics and techniques change after privilege gained (e.g. none -> user -> admin -> system/root…)

      - Appropriate assets change in attack path (e.g. weblogic -> server - >database -> pc ->domain controller … )

- Popular TTPs as candidates

#BHAS @BlackHatEvents

## Slide 27

##### Solution Implementation - KGRAG-Based TTP Chain Enrichment

TTP Chain
Enricher
LLM
KGRAG
①②③
Knowledge
TTP Chain Synthesizer
Graph

###### **Solution ②**

- LLM + KG (ToG, Think-on-Graph)

   - Starting from the specified entity, then explores step by step based on its relationship by asking LLM to choose the right one

   - Get an entity and repeat the first step

   - Physical explosion and super time consuming

   - Evaluation: **Bad**

###### **Solution ③**

- LLM + KG (Lightweight Domain Language + Reasoner Tool)

###### **Solution ①**

- LLM + KG (KBQA via LLM-generated SPARQL query)

   - Prompt engineering with database schema

   - One-time navigating based on lightweight domain language

- Generate not necessarily correct query statements and only explicit relationships at one-time, execute by program

   - Develop AI tools as reasoner engine (Based on Apache Jena)

   - Evaluation: **Good**

- Evaluation: **Bad**

#BHAS @BlackHatEvents

## Slide 28

## Solution Implementation & Results

- TTP Extraction Evolution (Three Ages)

   - Bronze Age: Traditional ML/DL (Baseline Accuracy)

   - Silver Age: Pre-trained Model/BERT Fine-tuning (Enhanced Accuracy)

   - • LLM Age: LLM Generation (SOTA Accuracy)

- KGRAG-Based TTP Extraction

- KGRAG-Based TTP Chain Enrichment

- RAG-Based TTP Actionable Conversion

#BHAS @BlackHatEvents

## Slide 29

##### Solution Implementation - RAG-Based TTP Actionable Conversion

Procedure Type
Actionable
Prompt TTP Chain
Engineering
Generator
LLM
Execution
Related
Prompt
Engineering
Phishing Stage 1/Lures Keywords For RAG
Related Related Searching MSF Module
Yes No
Prompt Prompt Prompt Prompt
Engineering Engineering Engineering Engineering
Re-rank Searched Create A New
MSF Modules MSF Module
Prompt Engineering: Module
Definition as RAG

Phishing Text

Downloaders/Droppers
(Lures)

New Modules or msfconsole Commands
of Metasploit Framework

#BHAS @BlackHatEvents

## Slide 30

#### Solution Results - TTP Actionable Conversion Results

|Metric|Phishing Text|Dropper/Lures|Metasploit Module
Execution
Commands|Metasploit New
Module Generation|
|---|---|---|---|---|
|**Accurate**|0.936|0.744|0.812|0.713|
|**Executable**|/|0.915|0.941|0.794|

- The test data comes from **30** threat analysis reports, extracted and enriched **771 TTPs** .

- Accuracy refers to the consistency between the generated content/code logic and the TTP. Accuracy is primarily evaluated using a LLM evaluation framework with the DeepSeek R1 model.

- Execution indicates whether the code can run successfully. Due to the use of code-specific models, the execution rate of generated code is generally high.

#BHAS @BlackHatEvents

## Slide 31

##### Phishing Text Generation Sample

###### **Report Chunk**

① Extract
Structured TTP

- { "uid": "51f22a12-db1d-4390-824f-3f44693e38ac",

- "procedure": "The DarkHotel sent emails to multiple hotels in the Macau area

- under the name of \\\"Macao Special Administrative Region Government Tourism Bureau\\\" to trick hotel staff into downloading and opening malicious Excel attachments.", "techniques": [ **② Convert** "TA0001//T1566.001//Initial Access//Spearphishing Attachment"

- ], "artifacts": [ "x_mail_language360: English",

- "x_mail_content360: Dear Sir/Madam,\nPlease open the attached file with

- enable content and specify whether the people were staying at the hotel or not?\n\nYours faithfully,\nInspection Division - MGTO"

]
}

**LLM Task: Phishing Text Generation** #BHAS @BlackHatEvents

## Slide 32

##### Downloader/Dropped as a Lure Generation Sample

**Report Chunk**

**① Extract**

**Python: Lure file generation script**

###### **Structured TTP**

{ "uid": "51f22a12-db1d-4390-824f-3f44693e38ac",

"procedure": "The bait lnk file used by the attacker runs mshta.exe through cmd.exe with argument: https[:]//www.googlesheetpage.org/bSQphSxgStENEhz5Y+PZCpjr/NBSWGWjjhkJi/PvaqE=, to load and execute the remote jscript script.",

**② Convert**

"techniques": [ "TA0005//T1027.012// 防御逃逸 //LNK Icon Smuggling",

"TA0005//T1218.005// 防御逃逸 // 利用 windows mshta 执行 "

], "artifacts": [] }

**LLM Task: Lure file generation**

#BHAS @BlackHatEvents

## Slide 33

##### Metasploit Msfconsole Commands Generation Sample

###### **Report Chunk**

**Structured TTP**

**① Extract**

**LLM Task: Keywords for searching MSF modules**

{

"uid": "2c1c7570-40cd-4082-a0db-b8a7851d454d",

"procedure": "CoughingDown exploits the ProxyLogon vulnerability (CVE-2021-26855) to upload a malicious Webshell on the Exchange server and gain control of the server by executing commands.", "techniques": [

**3 MSF modules searched**

"TA0001//QT1190.021//Initial Access//SSRF",

"TA0001//T1190//Initial Access//Exploit Public-Facing Application"

],

"artifacts": ["x_vul360:CVE-2021-26855", "x_targetservice360:microsoft:exchange_server"],

###### **Re-ranking**

"configuration": {

"permission_required": "None", "permission_obtained":"Command"

- }

}

Choose module id: 3

**LLM Task: Re-ranking for searched MSF modules**

#BHAS @BlackHatEvents

## Slide 34

##### Metasploit Msfconsole Commands Generation Sample

###### **Report Text**

**① Extract Structured TTP**

{ "uid": "2c1c7570-40cd-4082-a0db-b8a7851d454d", "procedure": "CoughingDown exploits the ProxyLogon vulnerability (CVE-2021-26855) to upload a malicious Webshell on the Exchange server and gain control of the server by executing commands.", "techniques": [ "TA0001//QT1190.021//Initial Access//SSRF", "TA0001//T1190//Initial Access//Exploit Public-Facing Application" ], "artifacts": ["x_vul360:CVE-2021-26855", "x_targetservice360:microsoft:exchange_server"], "configuration": { "permission_required": "None", "permission_obtained":"Command" } }

**② Convert**

**LLM Task: msfconsle commands generation**

**Shell: commands**

#BHAS @BlackHatEvents

## Slide 35

##### Metasploit New Module Generation Sample

###### **Report Text**

**Ruby: New MSF module generation result**

**① Extract**

###### **Structured TTP**

{ “uid”: “4cbe0473-8290-4342-9b7d-bc2d88c082ce”,

“procedure”: “CoughingDown uses the rar.exe command to compress and archive files of the specified type on the victim host. The specific command is:`rar.exe a -v100M idata001.rar -ta\”20240101000000\“ -r -x\”*.mp3\“ -x\”*.dll\“ -x\”*.exe\“ -x\”*.zip\“ -x\”*.mxf\“ -x\”*.rar\“ \”\\\\<<ip in the network>>\\\\c$\\\\Users\\\\<<user name>>\\\\Documents\“  \”\\\\<<ip in the network>>\\\\c$\\\\Users\\\\<<user **② Convert** name>>\\\\Desktop\“`”, “techniques”: [ “TA0009//T1074.001//Collection//Local Data Staging" ], "artifacts": [ "x_malware360:EAGERBEE" ] }

**Task: New MSF module generation**

#BHAS @BlackHatEvents

## Slide 36

## Takeaways

- Provide a **practical pipeline** to automatically convert human-readable threat reports into actionable TTP attack chains to support the **practical application of TTP intelligence** .

- Propose a paradigm **that combines lightweight BERT model predictions with KGRAG** to ensure high-precision TTP extraction **using up-to-date data and avoiding hallucinations** .

- Propose a method **that leverages KG reasoning to systematically enrich TTP attack chains** by linking possible TTPs.

- Propose a method **based on the RAG that converts structured TTP into actionable intelligence in diverse formats** .

#BHAS @BlackHatEvents

## Slide 37

# Thank You

#BHAS @BlackHatEvents
