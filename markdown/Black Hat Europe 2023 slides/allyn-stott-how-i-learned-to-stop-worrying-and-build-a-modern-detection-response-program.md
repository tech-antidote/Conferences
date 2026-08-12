---
title: "How I Learned to Stop Worrying and Build a Modern Detection & Response Program"
speakers: ["Allyn Stott"]
conference: "Black Hat"
conference_full: "Black Hat Europe 2023"
edition: "Europe"
year: 2023
source_pdf: "Black Hat Europe 2023 slides/Allyn Stott_How I Learned to Stop Worrying and Build a Modern Detection & Response Program.pdf"
pages: 70
sha256: "d161c04decc3ff1ea1c8f54df0829235508712b902c07bfb91a6e67022d9b59f"
text_chars: 11310
ocr_pages: 0
has_ocr: false
redacted_secrets: 0
ocr_confidence: null
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2"
converted_at: "2026-08-12T03:59:26Z"
---
# How I Learned to Stop Worrying and Build a Modern Detection & Response Program

**Speakers:** Allyn Stott  
**Conference:** Black Hat Europe 2023  
**Source:** `Black Hat Europe 2023 slides/Allyn Stott_How I Learned to Stop Worrying and Build a Modern Detection & Response Program.pdf` (70 pages)


## Slide 1

# How I Learned to Stop Worrying and ~~Love~~ Build a Modern Detection & Response Program

## Slide 2

#### Hi I’m Allyn I’m a worrier.

## Slide 3

## Slide 4

## Slide 5

Worrying can be a superpower.

## Slide 6

“...worry illuminates the importance of taking action to prevent an undesirable outcome and keeps the situation at the front of one's mind to ensure that appropriate action is taken.” Sweeny K., Dooley M. D. (2017). The surprising upsides of worry. Social and Personality Psychology Compass, 11, Article e12311

## Slide 7

Red team ➡ Blue team

## Slide 8

##### Detection and Response Programs

Legacy

## Modern

## Slide 9

##### Reactive

### Legacy

Technology-focused Manual-heavy Siloed and disjointed

## Slide 10

##### Proactive

### Modern

Business-focused

Automation prioritized Connected and centralized

## Slide 11

##### Challenges

Alert fatigue

Expensive tools Hiring & retention

Firefighting

## Slide 12

1. Assess the scope and goals

**Organizational Design**

##### A Step-by-Step Approach

2. Assess the strategy

3. Analyze the structure

4. Assess process and people

5. Analyze coordination

6. Design the architecture

Burton et al., 2015

7. Implement the architecture

## Slide 13

#### Assess and analyze Design and develop Implement and overcome Evaluate and report

## Slide 14

Assess and analyze Design and develop Implement and overcome Evaluate and report

## Slide 15

## Slide 16

Stop doing and start learning

## Slide 17

##### Viewpoints

People

Technology

Vision & mission

## Slide 18

### Vision & mission

What is unique? What are the problems? What are people doing?

## Slide 19

##### Viewpoints

People

Technology

Vision & mission

## Slide 20

NICE Cybersecurity Workforce Framework People

## Slide 21

##### NICE Cybersecurity Workforce Framework

**Operations Planner Mission Assessment Crime Investigator Exploit Analyst All-Source Analyst Legal Advisor Collection Manager Language Analyst Integration Planner Security Architect Database** People **Research & Administrator Development Cyber Defense Counter Intel Forensic Analyst Analyst Analyst Infrastructure Support Intel Planner Privacy Compliance Vulnerability Cyber Operator Systems Analyst Administrator Threat Target Enterprise Architect Warning Analyst Network Analyst Incident Responder Knowledge Software Developer Target Developer Systems Analyst Manager**

### People

## Slide 22

All-Source Analyst Exploit Analyst
Threat
Collection Manager
Warning Analyst
Cyber Defense
Cyber Operator
Analyst

Target
Language Analyst
Network Analyst
Integration Planner Target Developer
Vulnerability  Counter Intel
Analyst Analyst

##### Threat Intel Engineer

Cyber Defense
Cyber Operator
Threat Triage Analyst
Analyst
Vulnerability  Counter Intel
Incident Responder Forensic Analyst
Analyst Analyst
Incident Responder
Crime Investigator Legal Advisor Privacy Compliance
Software Developer Systems Analyst Security Architect Enterprise Architect
Infrastructure  Systems  Database  Research &
D&R Engineer Support Administrator Administrator Development
Knowledge
Operations Planner Mission Specialist
Manager

## Slide 23

Forensic Analyst

None

Novice

Intermediate

Expert

## Slide 24

All-Source Analyst Exploit Analyst
Threat
Collection Manager
Warning Analyst
Cyber Defense
Cyber Operator
Analyst

Target
Language Analyst
Network Analyst
Integration Planner Target Developer
Vulnerability  Counter Intel
Analyst Analyst

##### Threat Intel Engineer

Cyber Defense
Cyber Operator
Threat Triage Analyst
Analyst
Vulnerability  Counter Intel
Incident Responder Forensic Analyst
Analyst Analyst
Incident Responder
Crime Investigator Legal Advisor Privacy Compliance
Software Developer Systems Analyst Security Architect Enterprise Architect
Infrastructure  Systems  Database  Research &
D&R Engineer Support Administrator Administrator Development
Knowledge
Operations Planner Mission Specialist
Manager

## Slide 25

##### Viewpoints

People

Technology

Vision & mission

## Slide 26

Technology

## Slide 27

### Technical capabilities

###### not product categories

## Slide 28

Assess and analyze Design and develop Implement and overcome Evaluate and report

## Slide 29

## Slide 30

##### Design and develop

Process view

Architecture view

## Slide 31

What processes do we need?

## Slide 32

Threat  Evidence  Evidence
Modeling Collection Preservation
Process View
Intel  Intel  Intel  Forensic
Deception
Collection Analysis Dissemination Analysis
Incident  Threat  Detection  Incident
Reporting Hunting Engineering Response
Metrics
Continuous  Event  Event
Event Triage
Collection
Improvement Monitoring Analysis
Metrics
Micro-Purple  Observability
Reporting
Testing Engineering

## Slide 33

##### Process View

**Red Team / Pentesting Corporate Security**

###### **Detection & Response**

Security Awareness

Production Security

## Slide 34

##### Design and develop

Process view

Architecture view

## Slide 35

What capabilities do we need?

## Slide 36

##### MITRE ATT&CK

### Capability frameworks

MITRE D3FEND

Tines.io SOC Automation Matrix Snowflake's Detection series

## Slide 37

##### Maturity Model

Observability

Proactive Threat
Detection

Rapid Response

## Slide 38

### Observability

Entity & Activity Coverage Searchability

Contextualization

##### Enrichment Sourcing

## Slide 39

### Proactive Threat Detection

##### Intelligence Sourcing

Coverage & Gaps Efficacy, Effectiveness, & Efficiency

Accuracy

## Slide 40

### Rapid Response

##### Scenario Coverage

Organizational Coverage Speed, Accuracy, & Completeness

## Slide 41

Threat  Evidence  Evidence
Modeling Collection Preservation
Process View
Intel  Intel  Intel  Forensic
Deception
Collection Analysis Dissemination Analysis
Incident  Threat  Detection  Incident
Reporting Hunting Engineering Response
Metrics
Continuous  Event  Event
Event Triage
Collection
Improvement Monitoring Analysis
Metrics
Micro-Purple  Observability
Reporting
Testing Engineering

## Slide 42

Threat
Modeling
Process View
Intel  Intel  Intel
Collection Analysis Dissemination
Threat Actor  Intrusion Set  Raw Intel
Early Warning
Profiling Analysis Collection
Brand &  Account
Collection &  Intel Driven
Reputation  Takeover
Dissemination Detection
Monitoring Prevention

## Slide 43

Threat  Evidence  Evidence
Modeling Collection Preservation
Process View
Intel  Intel  Intel  Forensic
Deception
Collection Analysis Dissemination Analysis
Incident  Threat  Detection  Incident
Reporting Hunting Engineering Response
Metrics
Continuous  Event  Event
Event Triage
Collection
Improvement Monitoring Analysis
Metrics
Micro-Purple  Observability
Reporting
Testing Engineering

## Slide 44

Response  Incident
Orchestration Escalation

IP/DNS  Signature-
based Blocking
Blacklisting

Event  Event
Workflow  Analysis
Automate Automate

##### Process View

**Forensic Acquire**

Identity
Blocking

Case
Management

Event Monitoring

Evidence  Evidence
Collection Preservation

Forensic Analysis

Incident
Response

Event Analysis

Event Triage

Asset
Management

## Slide 45

Threat  Evidence  Evidence
Modeling Collection Preservation
Process View
Intel  Intel  Intel  Forensic
Deception
Collection Analysis Dissemination Analysis
Incident  Threat  Detection  Incident
Reporting Hunting Engineering Response
Metrics
Continuous  Event  Event
Event Triage
Collection
Improvement Monitoring Analysis
Metrics
Micro-Purple  Observability
Reporting
Testing Engineering

## Slide 46

Process View
Log
Log Collection
Normalization
Deception
Log  Data / Traffic
Enrichment Aggregate
Incident  Threat  Detection  Event  Historical
Reporting Hunting Engineering Correlation Context
Threat
Search
Behavior
Metrics
Continuous  Optimize
Analytics
Collection
Improvement
Malware  MPT
Analytics Automation
Metrics
Micro-Purple  Observability
Reporting
Testing Engineering

## Slide 47

##### Architecture View

###### **Threat Actor Profiling**

###### **Intrusion Set Analysis**

###### **Log Collection**

**Log Response Normalization Orchestration**

**Incident Escalation**

###### **Brand & Reputation Monitoring**

**Account Takeover Prevention**

**Log Enrichment**

**Data Aggregate**

**Forensic Signaturebased Blocking Acquire**

###### **Raw Intel Collection**

**Early Warning Collection Threat Collection & Behavior Dissemination Analytics**

**Event Correlation**

**Search Optimize**

**Historical Context**

**Identity Blocking**

**Event Event Workflow Analysis Automate Automate**

**Malware Detection**

**Asset Management**

**Intel Driven Malware Detection Analytics**

**MPT Automation**

**IP/DNS Case Blacklisting Management**

## Slide 48

Threat Actor  Intrusion Set
Profiling Analysis
Brand &  Account
Reputation  Takeover
Monitoring Prevention
Raw Intel
Early Warning
Collection
Collection &
Dissemination

Architecture View Response  Incident
Orchestration Escalation
Threat
Malware  Forensic  Identity
Behavior
Analytics Acquire Blocking
Analytics
MPT
Signature- IP/DNS
Automation
based Blocking Blacklisting
Event  Event
Workflow  Analysis
Intel Driven  Automate Automate
Detection
Case  Asset
Management Management
Log  Log  Search
Log Collection
Enrichment Normalization Optimize
Data  Event  Historical
Aggregate Correlation Context

## Slide 49

Assess and analyze Design and develop Implement and overcome Evaluate and report

## Slide 50

##### Implement and overcome

Hire and outsource

Build and buy

Overcome operations

## Slide 51

Assess and analyze Design and develop Implement and overcome Evaluate and report

## Slide 52

Modern

##### Evaluate and report

Legacy

## Slide 53

##### Reactive

Event count focused

### Legacy

One-dimensional Lacks business relevance

## Slide 54

##### Proactive

### Modern

Threat focused

Three-dimensional Quantifies business risk

## Slide 55

##### Evaluate and report

Observability

Metrics

Narratives

Roadmap

## Slide 56

What can we detect today? What's our landscape coverage? What's our overall visibility into threats?

## Slide 57

##### Micro-Purple Testing and Continuous Improvement

Threat Intel
Set Scope &  Score  Develop &
MPT Repo Run MPT
Complexity Effectiveness Improve

## Slide 58

##### What can we detect today?

Recon & Resource Dev
Initial Access
Execution
Persistence
PrivEsc
Defense Evasion
Cred Access
Discovery
Lateral Movement
Collection
C2
Exfiltration
Impact
0% 20% 40% 60% 80% 100%
for illustrative purposes only

## Slide 59

##### What's our landscape coverage?

100%
75%
50%
25%
0%
Endpoint Network Cloud SaaS Containers Database Apps Email

for illustrative purposes only

## Slide 60

##### What's our overall visibility into threats?

Validated
23%
Non-validated
31%
54%
Visibility

Gaps
46%

for illustrative purposes only

## Slide 61

##### Evaluate and report

Observability

Metrics

Narratives

Roadmap

## Slide 62

What are the top threats? What risks and impacts are we seeing from incidents? What top preventative controls would reduce risk and impact?

## Slide 63

##### Evaluate and report

Observability

Metrics

Narratives

Roadmap

## Slide 64

In recent incidents: How did the processes perform?

Technologies? People roles?

## Slide 65

##### Evaluate and report

Observability

Metrics

Narratives

Roadmap

## Slide 66

##### What are our priorities?

What is our roadmap to close the gaps?

## Slide 67

##### Micro-Purple Testing and Continuous Improvement

Threat Intel
Set Scope &  Score  Develop &
MPT Repo Run MPT
Complexity Effectiveness Improve

## Slide 68

##### Micro-Purple Testing and Continuous Improvement

Threat Intel
Set Scope &  Score  Develop &
MPT Repo Run MPT
Complexity Effectiveness Improve
Detection
Engineering
Incident
Reporting
Observability
Engineering
Threat  Prioritized
Hunting Backlog
Response
Automation
Metrics
Reporting
Analysis
Automation

## Slide 69

##### Build a Modern Detection & Response Program

###### **Before**

###### **After**

Hiring based on number of detection alerts

→

Data driven resource requests

Threat hunting because it "sounded cool"

→ Processes defined, measured, and proving value

Buying based on "Gartner says you need it"

→ Vision and architecture guides your investments

Telling leadership "yeah we might detect it"

→ Metrics for coverage and performance

## Slide 70

meoward.co allyn.stott@airbnb.com
