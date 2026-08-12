---
title: "Insider Threats Packing Their Bags With Corporate Data"
speakers: ["Mulugeta"]
conference: "Black Hat"
conference_full: "Black Hat ASIA 2023"
edition: "ASIA"
year: 2023
source_pdf: "Black Hat Asia 2023 slides/AS-23-Mulugeta-Insider-Threats-Packing-Their-Bags-With-Corporate-Data.pdf"
pages: 40
sha256: "95fd2eadd71408b5d81d676e88fb76eb6606e5a9e98a5b55b2ca28097232cb42"
text_chars: 11411
ocr_pages: 7
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T23:55:15Z"
---
# Insider Threats Packing Their Bags With Corporate Data

**Speakers:** Mulugeta  
**Conference:** Black Hat ASIA 2023  
**Source:** `Black Hat Asia 2023 slides/AS-23-Mulugeta-Insider-Threats-Packing-Their-Bags-With-Corporate-Data.pdf` (40 pages)

## Slide 1

# Insider Threats Packing Their Bags With Corporate Data

Dagmawi Mulugeta Colin Estep

1

#BHASIA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pifkhat”
ASIA 20a
MAY 11-12
BRIEFINGS
Insider Threats Packing Their Bags
With Corporate Data
Dagmawi Mulugeta
Colin Estep
1
#BHASIA @BlackHatEvents
```

## Slide 2

Insider Story
        = Uploads to personal Google Drive
Day 75 Day 50 Day 14 Day 0
Internal documents
Customer contacts
Cat Images
Intellectual
Property
Oh, let me grab the
I want to find a new job in the  Resign Depart
details on that project I
next 90 days or so. aced
The best practices
Almost forgot my
And, my kitten’s  here are top shelf
clients’ emails
Hmm, maybe I should  images too as well!
start saving stuff.
2 #BHASIA   @BlackHatEvents

## Slide 3

# Why should you listen to us?

3

#BHASIA   @BlackHatEvents

## Slide 4

## Our Findings

**207 organisations**

**4.7M active users**

**Important data movement starts 50 days prior to exit**

#BHASIA   @BlackHatEvents

4

## Slide 5

## Agenda

- ●The Problem

- ●Overview of our solution

- ●Employee Departures

- ●Data Exfiltration

- ●Takeaways

Information presented in this talk is based on anonymized usage data collected by the Netskope Security Cloud platform relating to a subset of Netskope customers with prior authorization

#BHASIA   @BlackHatEvents

5

## Slide 6

# The Problem

6

#BHASIA   @BlackHatEvents

## Slide 7

## The problem

**A malicious insider who has exfiltrated sensitive corporate data using cloud apps.**

“ **Sensitive Data** ” refers to data that could hurt the organization if it is exposed externally

The scope of an insider for this presentation is:

●Not using a USB drive

●Not printing out documents and walking out of the building with them

●Not taking pictures of a monitor with their phones

#BHASIA   @BlackHatEvents

7

## Slide 8

## Why is this important?

#### **Insiders**

- ●A 2020 Securonix Insider Threat Report found that 60% of Insider Threats involve "Flight Risk" employees

- ●Every organization has “flight risk” employees

#### **Data Exfiltration**

- ●More organizations than ever have Personally Identifiable Information (PII) and other sensitive data

- ●Liability around data breaches are typically on the organization itself

**Every organization should have a strategy to address this threat**

#BHASIA   @BlackHatEvents

8

## Slide 9

## Defining and Extracting Signals

**Volume** : Which users are downloading or uploading more than usual?

**Nature** : What files contain sensitive corporate information?

**Direction** : Are users are saving data to their own personal cloud storage?

#BHASIA   @BlackHatEvents

9

## Slide 10

# Overview of our solution

10

#BHASIA   @BlackHatEvents

## Slide 11

## Elements of our solution

- ●Architecture to monitor cloud traffic

- ●Applying labels to the cloud traffic

- ●What the events look like

- ●Analysis with Anomaly Detection

#BHASIA   @BlackHatEvents

11

## Slide 12

## Architecture

Monitoring Systems
Corporate Device
 Unmanaged Apps
(Endpoint Agent)
Forward Proxy Managed Apps
(SaaS & IaaS)
Anonymization Audit Log Ingestion
Unmanaged Device
Data Lake
Analysis
12 #BHASIA   @BlackHatEvents

#BHASIA   @BlackHatEvents

## Slide 13

### Applying Labels: Application Instances

The domain associated with a cloud application, which indicates who controls that particular application, is an instance. We use some heuristics to label the instances as data comes in for analysis.

|**Application**|**Domain**|**Label**|**Percentage of Traffic**|
|---|---|---|---|
|Google Drive|netskope.com|Business|50%|
|Google Drive|gmail.com|Personal|15%|
|Google Drive|foobar.com|Unknown|35%|

#BHASIA   @BlackHatEvents

13

## Slide 14

## Applying Labels: DLP

We need a way to label the files that contain an organization’s sensitive information.

DLP policies should alert when something contains the following:

- ●Intellectual Property

- ●Secrets

●Data in scope for compliance (PCI-DSS, GDPR, etc.)

We set policies in DLP to tell us when something sensitive has been accessed.

#BHASIA   @BlackHatEvents

14

## Slide 15

## What the events look like

User App App Instance label Activity File Name DLP Violation
dagmawi@gmail.com Google Drive personal upload black_project.docx Secret project
code names

#BHASIA   @BlackHatEvents

15

## Slide 16

## Analyzing the Data

- ●Use Anomaly Detection to find changes in behavior

- ●Focus on data movement with DLP

- ●Correlation between sensitive data movement and anomalous behavior are key

The approach above produces very useful results to find data exfiltration by insiders

#BHASIA   @BlackHatEvents

16

## Slide 17

# Employee Departures

17

#BHASIA   @BlackHatEvents

## Slide 18

## Our Data

Timeline: **July 2022 to April 2023**

**207 organisations**

**4.7M active users**

**58,314** individuals left their employment

#BHASIA   @BlackHatEvents

18

## Slide 19

## Industry breakdown for Departures

#BHASIA   @BlackHatEvents

19

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 2023
Industry breakdown for Departures
Insurance 7
Technology +
Finance
Retail +
Manufacturing | ar
Hospitality |
Media 4
Telecommunications fo
Consulting +
Healthcare (ii!
Business Services |
Food & Beverage }
Automotive
19 others
0.0% 2.0% 4.0% 6.0% 8.0% 10.0% 12.0% 14.0% 16.0%
Percentage
19
```

## Slide 20

### How many people move data to personal apps?

**85%** of flight risks **did not move data** to their personal apps

**15%** of flight risks **moved data** to their personal apps

#BHASIA   @BlackHatEvents

20

## Slide 21

### When is the data moved to personal apps?

75% of all files uploaded to personal apps were uploaded in the last 50 days

#BHASIA   @BlackHatEvents

21

## Slide 22

## What sort of data gets moved?

Files moved in the last 50 days

#BHASIA   @BlackHatEvents

22

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 20253
What sort of data gets moved?
Executable
Archive
Other
Binary data
1.9 %)
3.2 %)
3.6 %)
5.5 %)
eet
Plain Text (7.9 %)
Document (7.2 %)
Code (8.6 %)
Spreadsheet (11.6 %)
Portable document (21.0 %)
Image (29.5 %)
==
————y Ti}
Files moved in the last 50 days
22
Se Ps
WeTransfer (2.3 %)
Other (2.7 %)
Microsoft OneDrive (11.9 %)
Google Gmail (7.6 %)
Google Drive (75.5 %)
```

## Slide 23

# Data Exfiltration

23

#BHASIA   @BlackHatEvents

## Slide 24

## What kind of data exfiltration?

**A malicious insider who has exfiltrated sensitive corporate data using cloud apps.**

“ **Sensitive Data** ” refers to data that could hurt the organization if it is exposed externally

The scope of an insider for this presentation is:

- ●Not using a USB drive

●Not printing out documents and walking out of the building with them

●Not taking pictures of a monitor with their phones

#BHASIA   @BlackHatEvents

24

## Slide 25

## Finding Data Exfiltration

Volume of the data Anomaly Detection
Data Movement
Nature of the data DLP - Data Labeling
Uploads and Downloads
Direction of the data Instance Labeling

#BHASIA   @BlackHatEvents

25

## Slide 26

## Anomaly Detection

Looking for **spikes in certain activities** :

- ●Different from the user’s own patterns

- ●Different from the rest of the organization

Examples:

- You uploaded 2 TB to Google Drive in one day, which is more than anyone else

- ●You generated 500 DLP alerts on your last day, when you normally generate 10

#BHASIA   @BlackHatEvents

26

## Slide 27

## Detection Categories

||**Heuristic**|**Anomaly Detection**|**Anomaly Detection + DLP**|
|---|---|---|---|
|**Baselines**|**X**|||
|**Instance awareness**|**X**|||
|**Data Loss Prevention**|**X**|**X**||
|**Example**|Alert me if anyone uploads
more than 5 files to Google
Drive|Alert me if someone uploads
more than they usually do to
their personal Google Drive|Alert me if someone uploads
corporate secrets in large
amount to their personal
Google Drive|

#BHASIA   @BlackHatEvents

27

## Slide 28

## Detection efficacy

What is the relative signal strength of each type of detection to find someone who is going to leave?

Data Movement Detection Improvement
Heuristic Baseline
Anomaly Detection* 15.6 x
Anomaly Detection* + DLP 43.0 x

*Monitoring uploads are vital to get these improvements

#BHASIA   @BlackHatEvents

28

## Slide 29

## Exfiltration by departing employees

#### **2% exfiltrated corporate data via cloud apps**

#### **Timeline before departure**

- ●94% of the files exfiltrated in the last 91 days

- ●84% of the files exfiltrated in the last 49 days

- ●74% of the files exfiltrated in the last 28 days

If you monitor the last 30 days of employment, you may get around 75% of the files being mishandled before someone leaves.

In order to catch the 2% of people leaving and doing this, you need proactive analysis

#BHASIA   @BlackHatEvents

29

## Slide 30

## Data Targeted

Policies violated

Apps used

#BHASIA   @BlackHatEvents

30

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 20253
Data Targeted
Intellectual Property
PII
Financial Google Drive (63.0%)
Google Gmail (16.8%)
ma Microsoft OneDrive (16.6%)
Encrypted @—— Microsoft Live Outlook (1.5%)
Category Box (0.6%)
Secrets mm =Yahoo Mail (0.6%)
13 others (1.0%)
Source code
Unknown
0.0% 5.0% 10.0% 15.0% 20.0% 25.0% 30.0% 35.0%
Percentage
Policies violated Apps used
30
```

## Slide 31

# Current Limitations

31

#BHASIA   @BlackHatEvents

## Slide 32

## Current Limitations

●Analysed a finite set of data movement sources

●Scope was insiders that end up leaving the organization, but there are ones that do not

●Unknown traffic (neither personal or business) was primarily excluded from our analysis

#BHASIA   @BlackHatEvents

32

## Slide 33

## Future improvements

●Expanding the set of apps we analyze

●Developing other flight risk signals like uploads of resumes

●Reduction in business activities (saw ~10% reduction on overall business activities)

#BHASIA   @BlackHatEvents

33

## Slide 34

# Takeaways

34

#BHASIA   @BlackHatEvents

## Slide 35

## The problem

#### 2% is not a lot, most users are alright!

#BHASIA   @BlackHatEvents

35

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 2023
The problem
eoee83@8e@ ®@
100% nanan
Users that left
- 2% is not a lot, most users are
1 5? Yn fa alright!
Moved data to personal apps
2% |
Mishandled corporate data
35
```

## Slide 36

## The problem

2% is not a lot, most users are alright

●Incorrect!

~70% of the data targeted was Intellectual Property and PII

#BHASIA   @BlackHatEvents

36

## Slide 37

## Worst case scenario

#BHASIA   @BlackHatEvents

37

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 2023
Worst case scenario
Trade Secret Theft
Investigation Into Theft of Intellectual Property from GE Leads to Two Guilty Pleas
“He thought he was the smartest guy in the room.” That's how FBI Albany Special Agent Vin
Manglavil described Jean Patrice Delia, who pleaded guilty to conspiring to steal trade
secrets from General Electric Compal
that he believed he could download tt
secret—and launch a company to cor
what he was up to. made changes to company source code and exported gigabytes of proprietary
Tesla filed a lawsuit against a former employee this week after it learned he
data to unknown third parties.
“Sernas was traveling on company business, carrying a company laptop that had the GE
trade secret files on it,” Murphy said. The investigation also uncovered evidence that Sernas
and Delia had sent the calculations over email and uploaded them to cloud storage accounts.
37
```

## Slide 38

## Black Hat Sound Bytes

- **2%** of flight risks take sensitive data with them

- **75%** of data is uploaded in the last 50 days, before the typical 14 day notice

- ●Monitoring the **nature, volume,** and **direction** of data moved will allow you to detect these cases

#BHASIA   @BlackHatEvents

38

## Slide 39

## Following up…

Twitter:  Dagmawi ( <u>@dagmulu)</u>

Linkedin: Colin ( <u>colinestep)</u> Dagmawi ( <u>dmulugeta)</u>

Future updates on our <u>Netskope Threat Labs Blog</u>

#BHASIA   @BlackHatEvents

39

## Slide 40

# Thank you! Questions?

40

#BHASIA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
black hat
ASIA | L JR
MAY 11-12
BRIEFINGS
Thank youl
Questions?
40
#BHASIA @BlackHatEvents
```
