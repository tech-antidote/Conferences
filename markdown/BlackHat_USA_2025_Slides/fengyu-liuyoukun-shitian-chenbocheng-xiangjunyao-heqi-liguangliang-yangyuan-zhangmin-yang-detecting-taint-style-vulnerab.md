---
title: "Detecting Taint-Style Vulnerabilities in Microservice-Structured Web Applications"
speakers: ["Fengyu Liu", "YouKun Shi", "Tian Chen", "Bocheng Xiang", "Junyao He", "Qi Li", "Guangliang Yang", "Yuan Zhang", "Min Yang"]
conference: "Black Hat"
conference_full: "Black Hat USA 2025"
edition: "USA"
year: 2025
source_pdf: "BlackHat_USA_2025_Slides/Fengyu Liu&YouKun Shi&Tian Chen&Bocheng Xiang&Junyao He&Qi Li&Guangliang Yang&Yuan Zhang&Min Yang_Detecting Taint-Style Vulnerabilities in Microservice-Structured Web Applications.pdf"
pages: 43
sha256: "0619eea75f76dbe643453a586f328476ad2258f550ff8bce4fedbd6cc3a9cff4"
text_chars: 11509
ocr_pages: 11
has_ocr: true
redacted_secrets: 0
ocr_confidence: 89.1
ocr_unreliable_blocks: 0
vision_verified_blocks: 1
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T05:10:03Z"
---
# Detecting Taint-Style Vulnerabilities in Microservice-Structured Web Applications

**Speakers:** Fengyu Liu, YouKun Shi, Tian Chen, Bocheng Xiang, Junyao He, Qi Li, Guangliang Yang, Yuan Zhang, Min Yang  
**Conference:** Black Hat USA 2025  
**Source:** `BlackHat_USA_2025_Slides/Fengyu Liu&YouKun Shi&Tian Chen&Bocheng Xiang&Junyao He&Qi Li&Guangliang Yang&Yuan Zhang&Min Yang_Detecting Taint-Style Vulnerabilities in Microservice-Structured Web Applications.pdf` (43 pages)


## Slide 1

Detecting Taint-Style Vulnerabilities in Microservice-Structured Web Applications Speaker: Fengyu Liu (LFY) Contributors:

#BHUSA   @BlackHatEvents

## Slide 2

# Agenda

- Warm-up & Industry Context

- The Attack Surfaces in Microservices

- Real Case Study

- How MScan Works

- Evaluation

- Conclusion & Takeaways

#BHUSA   @BlackHatEvents

## Slide 3

# Modern Apps: From Monolith to Microservices

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 86/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Modern Apps: From Monolith to Microservices
Monolithic architecture
Microservice architecture
Client browser
Client browser
Payment Shopping cort NVEnCONY = Ss _ 41k
Payment Shopping cart Inventory
Single instance
```

## Slide 4

# Modern Apps: From Monolith to Microservices

- Microservices dominate cloud-native architecture

- Decentralized, scalable, dynamic — but complex

- One user request may pass through 10+ services

#BHUSA   @BlackHatEvents

## Slide 5

# Microservices: Gateway

- Central entry that **routes** user requests to internal services based on **routing rules**

• For example, it forwards requests to _Portal_ but blocks access direct to _User_

#BHUSA   @BlackHatEvents

## Slide 6

# Microservices: Inter-service Communication

• Lightweight **network communication** mechanism (e.g., REST, gRPC) that connect services and pass data

#BHUSA   @BlackHatEvents

## Slide 7

# Agenda

- Warm-up & Industry Context

- The Attack Surfaces in Microservices

- Real Case Study

- How MScan Works

- Evaluation

- Conclusion & Takeaways

#BHUSA   @BlackHatEvents

## Slide 8

# Taint-style Vulnerabilities in Microservice App

- Intra-service Vulnerability

- happens within a single microservice

#BHUSA   @BlackHatEvents

## Slide 9

# Taint-style Vulnerabilities in Microservice App

- Inter-service Vulnerability

- involves Inter-service communication

#BHUSA   @BlackHatEvents

## Slide 10

# Agenda

- Warm-up & Industry Context

- The Attack Surfaces in Microservices

- Real Case Study

- How MScan Works

- Evaluation

- Conclusion & Takeaways

#BHUSA   @BlackHatEvents

## Slide 11

# Real Case: Spring Cloud Dataflow

## • A cloud dataflow platform under Spring Projects

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 93/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
BRIEFINGS >
Real Case: Spring Cloud Dataflow
¢ A cloud dataflow platform under Spring Projects
Web
Data Flow
Skipper
Dashboard Server Server
CVE-2024-22263: Arbitrary File Write Vulnerability in
Spring Cloud Data Flow Shell
HIGH | MAY 23, , 2024 | CVE-2024-22263
```

## Slide 12

# Real Case: Spring Cloud Dataflow

- Entry: Stream Rest Service

- Edge: RestTemplate

- Service: Package Rest Service

- Sink: Files.write

#BHUSA   @BlackHatEvents

## Slide 13

# Agenda

- Warm-up & Industry Context

- The Attack Surfaces in Microservices

- Real Case Study

- How MScan Works

- Evaluation

- Conclusion & Takeaways

#BHUSA   @BlackHatEvents

## Slide 14

# Challenges

- Hidden entry points due to gateway routing rules

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 89/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Challenges
¢ Hidden entry points due to gateway routing rules
// Allow access / Deny access
1 | portal-route: user-route:
2| path: /portal/** path: /user/**
3 service: portal service: user
4| filters: AddHeader=X-Portal filter: SetResponseStatus=403
a
Ne
```

## Slide 15

# Challenges

- Hidden entry points due to gateway routing rules

- Not all methods are user-accessible

- Gateways control access with flexible, unstructured configs

#BHUSA   @BlackHatEvents

## Slide 16

# Challenges

- Cross-service data flow is hard to track

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 89/100 on the text kept, 70/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Challenges
¢ Cross-service data flow is hard to track
RestTemplate 6 RPC
Gateway Portal Service User Service
```

## Slide 17

# Challenges

- Cross-service data flow is hard to track

- Services communicate via many diverse mechanisms (gRPC, Message Queue), making taint tracking non-trivial

#BHUSA   @BlackHatEvents

## Slide 18

# Challenges

- Long call chains break traditional context-sensitive analysis

- Deep call stacks across multi services cause context-sensitive analysis to timeout or run out of memory

#BHUSA   @BlackHatEvents

## Slide 19

# Mscan Overview

## • LLM-based entry identification and distance-guided taint analysis in Mscan

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 85/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Mscan Overview
¢ [LM-based entry identification and distance-guided taint analysis
= +@
Application Code Entry Points SDG
| S | Distance-guided
7 3 Source-to-Sink Paths
Vulnerability
~
in Mscan
Figure 5: The Architecture of MScan.
```

## Slide 20

# Stage I: Entry Point Identification

- LLM-assisted Routing Rule Extraction

- User-accessible Entry Point Identification

#BHUSA   @BlackHatEvents

## Slide 21

# Stage I: Entry Point Identification

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 93/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Stage I: Entry Point Identification
K Shots
Task Description
routes:
or You are a gateway routing rule reader. Read the following routing @) a
rules of a microservice application and list all that forward requests. user ae
system You must follow these rules: filters:
1. You must respond with a JSON list of strings, where each string - AddRequestHeader=X-Request-red
represents a routing path to a microservice. - id: log-route
2. You need to retain the regex content in the rules as-is. predicates:
3. You must not include any other information in your response. - Path=/log/**
4. By default, assume that the rules will forward requests. filters:
- Status=403
GS ["/add/**"]
Actual query assistant
portal-route:
user path: /portal/** LLM Response
service: portal
util-route:
path: /util/** ["/portal/**"]
filter: deny WSS
service: util
```

## Slide 22

# Stage II: Construct Service Dependence Graph

- Identify Communication APIs

- Too many APIs

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 87/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Stage II: Construct Service Dependence Graph
Framework / Lib Type APIs
° Identify Communication APIs RestTemplate.get
RestTemplate Sync RestTemplate.post
RestTemplate.exchange
¢ Too many APIs = Sine “ImplBase.*
*BlockingStub.*
URL.openConnection
JDK Native Syne 5
HttpClient.send
Apache HttpClient Sync HttpClient.execute
HttpUtil.post
@DubboReference
Kafa Asyne KafkaProducer.send
KafkaConsumer.poll
Jedis.set
MQTT Asyne MattClient.publish
MattClient.subscribe
```

## Slide 23

# Stage II: Construct Service Dependence Graph

- Identify Communication APIs

• Use plugin system to handle all

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 83/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Stage II: Construct Service Dependence Graph
Framework / Lib Type APIs
. . . OpenFeign Sync @FeignClient
Identify Communication APIs RestTemplate.get
RestTemplate Sync RestTemplate.post
RestTemplate.exchange
*BlockingStub.*
HttpClient.send
“. Apache HttpClient Syne HttpClient.execute
Hutool-http Sync HttpUtil.get
HttpUtil.post
Dubbo Sync @DubboReference
gRPC Syne
@DubboService
Kafa Asyne KafkaProducer.send
KafkaConsumer.poll
RabbitMQ Async ae en
Channel.basicConsume
Jedis.get
Use plugin system to handle all Real eee Jolie
MattClient.publish
MattClient.subscribe
MQTT Asynec
```

## Slide 24

# Stage II: Construct Service Dependence Graph

- “Tai-e introduces a novel analysis plugin system to easily develop and integrate new analysis (that interacts with pointer analysis) like taint analysis and exception analysis, etc. ”

#BHUSA   @BlackHatEvents

## Slide 25

# Stage II: Construct Service Dependence Graph

- Use plugin system to handle all

- OpenFeign plugin, gRPC plugin, RestTemplate plugin…

#BHUSA   @BlackHatEvents

## Slide 26

# Stage II: Construct Service Dependence Graph

- Resolve Identifier Nodes

- Link Communication Edges

- Connect Inter-service Data Flows

#BHUSA   @BlackHatEvents

## Slide 27

# Stage III: Vulnerability Detection

- Identify Taint Source

- Match Taint Sinks

- Check for Missing Sanitization

- Selective Context-sensitive Taint Tracking via SDG

#BHUSA   @BlackHatEvents

## Slide 28

# Identify Taint Source Sink and Sanitizer

- **Taint source:** Parameters of user-accessible entry points identified from gateway rules

- **Taint sink:** Security-sensitive operations like SQL queries, file writes, SSRF requests, etc.

- **Taint sanitizer:** If tainted data reaches a sink without proper sanitization → report as vulnerability.

#BHUSA   @BlackHatEvents

## Slide 29

# Selective Context-Sensitive Taint Analysis

- What is Context Sensitivity in Taint Analysis?

- Same method, different callsites = different analysis!

- For example, _D()_ is called in **4 different contexts** :

- A→B→C→D, A→C→D, B→C→D, C→D

#BHUSA   @BlackHatEvents

## Slide 30

# Selective Context-Sensitive Taint Analysis

- Why Full Context Sensitivity Fails in Microservices?

- Long call chains often span multiple services due to inter-service data flows and complex interactions

- Full context tracking generates excessive context objects → high memory, slow analysis, even OOM

#BHUSA   @BlackHatEvents

## Slide 31

# Selective Context-Sensitive Taint Analysis

• Goal: Balance Accuracy and Overhead → Precise Yet Scalable Context-sensitive Analysis

• Our Idea: Distance-guided Strategy

#BHUSA   @BlackHatEvents

## Slide 32

# Agenda

- Warm-up & Industry Context

- The Attack Surfaces in Microservices

- Real Case Study

- How MScan Works

- Evaluation

- Conclusions & Takeaways

#BHUSA   @BlackHatEvents

## Slide 33

# Evaluation Setup: Implementation

- Built on top of Tai-e, a state-of-the-art pointer analysis engine

- ~7K lines of Java code, supports 8 types of vulnerabilities

- SQLi, SSRF, XXE, AFW, code/command injection, etc.

#BHUSA   @BlackHatEvents

## Slide 34

# Evaluation Setup: Dataset

- 25 open-source microservice applications, all with 1K+ GitHub stars

- Cover diverse domains: e-commerce, file services, code hosting, etc.

- 5 industrial applications from a world-leading fintech company

- Real-world scale, with complex cross-service logic

#BHUSA   @BlackHatEvents

## Slide 35

# Evaluation Result: Effectiveness

- MScan detected **59** 0-day vulns

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 91/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Evaluation Result: Effectiveness
¢ MScan detected 59 0-day vulns
Vulnerability Type TP FP Prec(%)
Intra-service 27 12 69.23%
Inter-service 32 11 74.42%
Total 59 23 71.95%
```

## Slide 36

# Evaluation Result: Baseline

- MScan detected **59** 0-day vulns

- CodeQL detected **23** vulns, missed **36**

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 91/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Evaluation Result: Baseline
¢ MScan detected 59 0-day vulns
¢ CodeQL detected 23 vulns, missed 36
Baselines TP FP FN Prec(%) Recall(%)
CodeQL 23 35 36 39.66% 38.98%
MScan 59 23 0 71.95% 100.00%
```

## Slide 37

# Ablation Study

• **NoEntryDet** : Disables entry point filtering → uses all entry methods

- **NoSDG** : Removes inter-service communication edges

- **MScan-CS** : Uses full context sensitivity (no distance-guided strategy)

- **MScan-CS-2call** : Uses 2-call bounded context sensitivity (from Tai-

e)

#BHUSA   @BlackHatEvents

## Slide 38

# Ablation Study

#BHUSA   @BlackHatEvents


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 92/100 on the text kept, 86/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
black hat BRIEFINGS

Ablation Study

| Baselines | TP | FP | FN | Prec(%) | Recall(%) |
| --- | --- | --- | --- | --- | --- |
| MScan-NoEntry | 59 | 89 | 0 | 39.86% | 100% |
| MScan-NoSDG | 27 | 12 | 32 | 69.23% | 45.76% |
| MScan-CS | 29 | 11 | 30 | 72.50% | 49.15% |
| MScan-CS-2call | 59 | 251 | 0 | 19.03% | 100.00% |
| MScan | 59 | 23 | 0 | 71.95% | 100.00% |

#BHUSA  @BlackHatEvents
```

## Slide 39

# Case Study: Site Where

- A famous IoT platform

- Vuln: SQL Injection

- Entry: Device Rest Portal

- Edge: gRPC

- Service: Device Event Service

- Sink: InfluxDB.query

#BHUSA   @BlackHatEvents

## Slide 40

# Case Study: Yudao Cloud

- A famous cloud platform

- Vuln: SQL Injection

- Entry: File Rest Portal

- Edge: OpenFeign

- Service: File Rest Service

- Sink: FileUtil.writeBytes

#BHUSA   @BlackHatEvents

## Slide 41

# Case Study: Mogu Blog

- A famous blog system

- Vuln: Server-Side Request Forgery

- Entry: Wechat Rest Portal

- Edge: OpenFeign

- Serive: Picture Rest Service

- Sink: URL.<init>

#BHUSA   @BlackHatEvents

## Slide 42

# Agenda

- Warm-up & Industry Context

- The Attack Surfaces in Microservices

- Real Case Study

- How MScan Works

- Evaluation

- Conclusion & Takeaways

#BHUSA   @BlackHatEvents

## Slide 43

# Conclusion & Takeaways

- Attendees will know the current state and key challenges of detecting taint-style vulnerabilities in microservice apps.

- Attendees will understand how Mscan works and why it detects taint-style vulnerabilities in microservice apps efficiently and precisely.

- Attendees will learn how to optimize taint analysis when adapting it to a cross service system.

#BHUSA   @BlackHatEvents
