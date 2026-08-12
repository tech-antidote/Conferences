---
title: "FACADE High-Precision Insider Threat Detection Using Contrastive Learning"
speakers: ["Alex Kantchelian", "Ryan Stevens", "Yanis Pavlidis", "Sadegh Momeni", "Casper Neo", "Birkett Huber", "Elie Bursztein"]
conference: "Black Hat"
conference_full: "Black Hat USA 2025"
edition: "USA"
year: 2025
source_pdf: "BlackHat_USA_2025_Slides/Alex Kantchelian&Ryan Stevens&Yanis Pavlidis&Sadegh Momeni&Casper Neo&Birkett Huber&Elie Bursztein_FACADE High-Precision Insider Threat Detection Using Contrastive Learning.pdf"
pages: 43
sha256: "fc1170bbfeeba8a8785b313bd208106a4b5f4c7e7d4f426816c7cea1e29de237"
text_chars: 9643
ocr_pages: 1
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T00:53:14Z"
---
# FACADE High-Precision Insider Threat Detection Using Contrastive Learning

**Speakers:** Alex Kantchelian, Ryan Stevens, Yanis Pavlidis, Sadegh Momeni, Casper Neo, Birkett Huber, Elie Bursztein  
**Conference:** Black Hat USA 2025  
**Source:** `BlackHat_USA_2025_Slides/Alex Kantchelian&Ryan Stevens&Yanis Pavlidis&Sadegh Momeni&Casper Neo&Birkett Huber&Elie Bursztein_FACADE High-Precision Insider Threat Detection Using Contrastive Learning.pdf` (43 pages)

## Slide 1

# **FACADE**

High-Precision Insider Threat Detection Using Contrastive Learning

Alex Kantchelian Elie Bursztein Google Google DeepMind

with **Casper Neo** , **Ryan Stevens** , **Sadegh Momeni** , **Birkett Huber** , **Yanis Pavlidis** and **many** other Googlers

#BHUSA   @BlackHatEvents

## Slide 2

SCAN ME

**Presentation slides: https://elie.net/facade**

**#BHUSA @BlackHatEvents**

## Slide 3

10 billion+ events processed annually to protect Google from insider threats

**#BHUSA @BlackHatEvents**

## Slide 4

### Insider at t acks threat model

Intentional Unwilling Accidental
attack by a rogue  attack by a deceived or  harm by a well
employee coerced employee intentioned employee

**#BHUSA @BlackHatEvents**

## Slide 5

### Example of insider threats

**Intentional**

access of confidential documents without business justification through access permissions abuse

**Unwilling**

access made using an employee account compromised by a malware

**Accidental**

share confidential documents with external party without NDA in good faith

**#BHUSA @BlackHatEvents**

## Slide 6

### Why detecting insider at t acks is hard

|**Very low incidence**|
|---|
|Insider threat incidence events are extremely low volume|
|**Heavily context dependent**|
|Risk depends on user roles and their relations to the resources accessed|
|**Wide attack surface**|
|Insider attackers have broad access to the enterprise infrastructure via
legitimate credentials|

**#BHUSA @BlackHatEvents**

## Slide 7

##### low false alerts

FACADE: A High-Precision Insider Threat Detection Using Deep Contextual Anomaly Detection Deep User and How likely is resource the acces? learning model aware

**#BHUSA @BlackHatEvents**

## Slide 8

Highly accurate anomaly detection? Really?

**#BHUSA @BlackHatEvents**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bu S
ay)
Highly accurate anomaly detection? Really?
#BHUSA @BlackHatEvents
```

## Slide 9

Red Team attacks ranked in the top 0.01% of suspicious events and many red team attackers in the top-10 most suspicious users during the attack period, with 10+ millions events ranked by FACADE during that timespan.

**#BHUSA @BlackHatEvents**

## Slide 10

### Agenda

FACADE Overview

Featurization of Resources and Users

Scoring Arbitrary Time Periods Finding Insider Attacks with FACADE

**#BHUSA @BlackHatEvents**

## Slide 11

FACADE Overview

**#BHUSA @BlackHatEvents**

## Slide 12

Problem formulation Is it normal for a given user to access a given resource?

**#BHUSA @BlackHatEvents**

## Slide 13

TPU schematics

Normal pattern

Legitimate user Hardware division

Rogue actor Ads Sales

TPU schematics

Abnormal pattern

**#BHUSA @BlackHatEvents**

## Slide 14

### FACADE model architecture

User embedding
TF Anomaly
Model Score
Resource embedding

**#BHUSA @BlackHatEvents**

## Slide 15

?

How do we train such model with little to no insider attack examples?

**#BHUSA @BlackHatEvents**

## Slide 16

TPU schematics User A Hardware division

User A embedding TPU doc embedding

User B embedding AlphaSecret doc embedding

AlphaSecret Model results User B Google DeepMind

**#BHUSA @BlackHatEvents**

## Slide 17

#### Unsupervised Training dataset construction

User A embedding User A embedding AlphaSecret doc embedding TPU doc embedding User B embedding User B embedding AlphaSecret doc embedding TPU doc embedding Abnormal behavior Normal behavior examples examples

**#BHUSA @BlackHatEvents**

## Slide 18

## Featurization of Resources and Users

**#BHUSA @BlackHatEvents**

## Slide 19

## Featurization of Resources

**#BHUSA @BlackHatEvents**

## Slide 20

### Resource Featurization Challenges

**Must handle massive, heterogeneous resources** billions of distinct items document, spreadsheet, video, data table, RPC endpoint, URL, …

**Content-based features are impractical** case-by-case development & maintenance cost computationally expensive at inference time

**Large distribution drift** new resources at inference time _is the norm_ , e.g., documents inherent difficulty in predicting appearance of novel topics in content

**#BHUSA @BlackHatEvents**

## Slide 21

?

How to turn the open space of resources into a dense representation suitable to deep-learning training?

**#BHUSA @BlackHatEvents**

## Slide 22

### Intuition

**If the following held, could treat resource as categorical feature:** the set of resources is mostly constant the set of resources is not too large each resource keeps a stable meaning throughout its existence

**Idea: project resources into a more stable set of opaque identifiers** the set of user ids on a corporate system is a good candidate

**History-based Featurization** Bag-of-words of user ids who have previously accessed it

**#BHUSA @BlackHatEvents**

## Slide 23

### History-based Featurization

Resource Access History
A  creates B  accesses C  accesses D  accesses A  accesses
{ A } { A ,  B } { A ,  B ,  C } { A ,  B ,  C ,  D } { A ,  B ,  C ,  D }
Resource featurizations for given time periods
Handles distribution drift (changing content)

**#BHUSA @BlackHatEvents**

## Slide 24

### Access Event Input Example

{

**id** : "e767…"           # _An unique identifier for this access event_ **occurred_at** : 1710…    # _Timestamp of the event_ **principal** : "A"         # _The id of the user performing the access_ **type** : "doc_access"     # _Resource type (doc, db table, hostname, …)_ **resource_id** : "8bca…"  # _Resource identifier, e.g., document id_ }

**You only need to choose a stable-in-time resource identifier Facade takes care of the rest (history-based featurization)**

**#BHUSA @BlackHatEvents**

## Slide 25

### History Set to Dense Vector

{ A ,  B ,  C ,  D }
sum
dense embeddings matrix
resource embedding
…

**#BHUSA @BlackHatEvents**

## Slide 26

## Featurization of Users

**#BHUSA @BlackHatEvents**

## Slide 27

Two Types of User At t ributes

**Low cardinality, stable attributes** E.g. Job title (receptionist, software engineer, hardware engineer, etc) → Direct categorical featurization

**High cardinality, unstable attributes** E.g. team, projects assigned, meetings attended, PRs reviewed, … Large distribution drift (re-orgs, new projects, employees, etc) → Implicit social network featurization

**#BHUSA @BlackHatEvents**

## Slide 28

### Implicit Social Network Featurization

User  B
User  C
User  D
User  A Project XYZ

- “project” feature for user **A** is bag-of-words { **B** , **C** , **D** }

**Any user is featurized by a set of sets of other user ids** one set per attribute type (team, project, department, etc)

**#BHUSA @BlackHatEvents**

## Slide 29

### User Context Event Input Example

{

**valid_from** : 1700…  # _Start of validity for this context fragment_ **principal** : "A"      # _The id of the user_ this pertains to **name** : "project"     # _User attribute (team, project, meetings, …)_ **value** : "XYZ"        # _Opaque identifier_ } **You only need to choose the user attributes you want to use Facade takes care of the rest (implicit social network featurization)**

**#BHUSA @BlackHatEvents**

## Slide 30

### User features to dense vector

Feature Name Feature Value
job_title software_eng embed
team { A ,  B ,  C } embed model user embedding
project { B ,  C ,  D } embed
#BHUSA @BlackHatEvents

## Slide 31

### Featurization Takeaways

1 2
Universal Robust to
featurization method  distribution drift

3 4
New resources and  Fast and efficient
users w/o retraining

**#BHUSA @BlackHatEvents**

## Slide 32

## Scoring Arbitrary Time Periods

**#BHUSA @BlackHatEvents**

## Slide 33

### Pointwise VS Activity Set Scoring

single access scores
???
activity set score
0.23 0.02 0.14 0.19 0.31

**#BHUSA @BlackHatEvents**

## Slide 34

### A Simple Problem?

**Average of scores** attacker can decrease score by adding benign accesses

**Sum of scores** users with more activity will be more anomalous

**Max score** ignores all but one access

**#BHUSA @BlackHatEvents**

## Slide 35

### Scoring Diversity of Anomalous Activity

Eliminate redundant and repetitive anomalies
Use the resource embeddings for similarity
1.  Cluster similarly-anomalous  accesses together
2.  Sum  together  max  score of each cluster
Prevent attacker from hiding malicious activity
More diversely-anomalous sets score higher

**#BHUSA @BlackHatEvents**

## Slide 36

Example
Overall score is:
cluster 2
0.23 (cluster 1)
cluster 1
+ 0.02 (cluster 2)
resource embedding
+ 0.31 (cluster 3)
space
cluster 3
#BHUSA @BlackHatEvents
0.23 0.02 0.14 0.19 0.31

## Slide 37

## Finding Insider Attacks with FACADE

**#BHUSA @BlackHatEvents**

## Slide 38

### Red Team Insider Threat Scenarios

Hardware Product AI Research
Media Sharing Platform
Attackers seek corporate  Attackers seek next gen  Attackers seek next gen
financial data, individual  device design, timelines, AI: unpublished papers,
creators’ earnings, … pictures, schematics, … code, model weights, …

**#BHUSA @BlackHatEvents**

## Slide 39

### Operational Setup

**15 participants** Full-time employees with interest in cyber security

**High-level playbooks provided** attackers seek to discover and access sensitive information attackers not provided detailed attack plans or target resources **Various levels of attack success per participant**

**#BHUSA @BlackHatEvents**

## Slide 40

### Evaluation results

~180,000+ user accounts

Triaging budget: top 10 users/day

Detects 4 out of 15 attackers

More details in <u>ht</u> t <u>ps://arxiv.org/abs/2412.06700</u>

**#BHUSA @BlackHatEvents**

## Slide 41

### Try it yourself

Reference implementation <u>https://github.com/google/facade</u> Note:  as mentioned Facade is meant to work on large scale data and requires you bring your own modeling. Using it on small datasets won’t work well.

**#BHUSA @BlackHatEvents**

## Slide 42

### Takeaways

Insider threats: low incidence high impact attacks Detection requires contextual analysis

FACADE: high-precision contextual anomaly detection Works for single-access _and_ activity set

Adaptable to many systems and use-cases Open-source model and featurizer code available

**#BHUSA @BlackHatEvents**

## Slide 43

Slides: <u>facade https://elie.net</u> <u>/</u>

Code: <u>https://github.com/google/facade</u>

 SCAN ME

**#BHUSA @BlackHatEvents**
