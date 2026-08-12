---
title: "Your Traffic Doesn't Lie Unmasking Supply Chain Attacks via Application Behaviour"
speakers: ["Colin Estep", "Dagmawi Mulugeta"]
conference: "Black Hat"
conference_full: "Black Hat USA 2025"
edition: "USA"
year: 2025
source_pdf: "BlackHat_USA_2025_Slides/Colin Estep&Dagmawi Mulugeta_Your Traffic Doesn't Lie Unmasking Supply Chain Attacks via Application Behaviour.pdf"
pages: 66
sha256: "9f215f1b8f7f2c8c945eed5363ed6f2565e8cc39f1f3b8e242ed93e211f898b3"
text_chars: 14978
ocr_pages: 13
has_ocr: true
redacted_secrets: 0
ocr_confidence: 85.8
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T05:08:07Z"
---
# Your Traffic Doesn't Lie Unmasking Supply Chain Attacks via Application Behaviour

**Speakers:** Colin Estep, Dagmawi Mulugeta  
**Conference:** Black Hat USA 2025  
**Source:** `BlackHat_USA_2025_Slides/Colin Estep&Dagmawi Mulugeta_Your Traffic Doesn't Lie Unmasking Supply Chain Attacks via Application Behaviour.pdf` (66 pages)


## Slide 1

### Your Traffic Doesn't Lie: Unmasking Supply Chain Attacks via Application Behaviour

Colin Estep, Dagmawi Mulugeta Netskope Threat Labs

#BHUSA   @BlackHatEvents

## Slide 2

# Intros

LinkedIn: <u>colinestep</u>

LinkedIn: <u>dmulugeta</u>

#BHUSA   @BlackHatEvents

## Slide 3

# SolarWinds Compromise

- First incident as a vendor

- Provided motivation for this research

#BHUSA   @BlackHatEvents

## Slide 4

## What’s out there today

Modify
SCM Distribution
CI/CD Use
Developer
Artifact
Dependency Process

Source: https://www.technologydecisions.com.au/content/security/article/anatomy-of-a-supply-chain-software-attack-440028396

#BHUSA   @BlackHatEvents

## Slide 5

## What’s out there today

Compromise
SCM Distribution
CI/CD Use
Developer
Artifact
Dependency Process

Source: https://www.technologydecisions.com.au/content/security/article/anatomy-of-a-supply-chain-software-attack-440028396

#BHUSA   @BlackHatEvents

## Slide 6

## What’s out there today

Modify
SCM Distribution
CI/CD Use
Developer
Artifact
Dependency Process

Source: https://www.technologydecisions.com.au/content/security/article/anatomy-of-a-supply-chain-software-attack-440028396

#BHUSA   @BlackHatEvents

## Slide 7

## What’s out there today

Compromise
SCM Distribution
CI/CD Use
Developer
Artifact
Dependency Process

Source: https://www.technologydecisions.com.au/content/security/article/anatomy-of-a-supply-chain-software-attack-440028396

#BHUSA   @BlackHatEvents

## Slide 8

## What’s out there today

Bypass
SCM Distribution
CI/CD Use
Developer
Artifact
Dependency Process

Source: https://www.technologydecisions.com.au/content/security/article/anatomy-of-a-supply-chain-software-attack-440028396

#BHUSA   @BlackHatEvents

## Slide 9

## What’s out there today

Compromise
SCM Distribution
CI/CD Use
Developer
Artifact
Dependency Process

Source: https://www.technologydecisions.com.au/content/security/article/anatomy-of-a-supply-chain-software-attack-440028396

#BHUSA   @BlackHatEvents

## Slide 10

## What’s out there today

Swap
SCM Distribution
CI/CD Use
Developer
Artifact
Dependency Process

Source: https://www.technologydecisions.com.au/content/security/article/anatomy-of-a-supply-chain-software-attack-440028396

#BHUSA   @BlackHatEvents

## Slide 11

## What’s out there today

SCM Distribution
CI/CD Use
Developer
Compromise
Artifact
Dependency Process

Source: https://www.technologydecisions.com.au/content/security/article/anatomy-of-a-supply-chain-software-attack-440028396

#BHUSA   @BlackHatEvents

## Slide 12

## What’s out there today

###### This is where we want to identify a compromise

Compromise Compromise Compromise
Modify Modify Bypass  Swap
SCM Distribution
CI/CD Use
Developer
Compromise
Artifact
Dependency Process

Source: https://www.technologydecisions.com.au/content/security/article/anatomy-of-a-supply-chain-software-attack-440028396

#BHUSA   @BlackHatEvents

## Slide 13

# Software Deployed

**Box Client** (not browser)

#BHUSA   @BlackHatEvents

## Slide 14

# Software Deployed

xqpt5z.dagmawi.io

**Box Client** (not browser)

#BHUSA   @BlackHatEvents

## Slide 15

# Finding Malicious Traffic

##### **xqpt5z.dagmawi.io is anomalous (99%)**

URL Entropy Application Hosts Path Depth
URL Randomness Not a known host Root path
Odds: 5.47x Odds: 4.06x Odds: 4.06x

1

5 #BHUSA   @BlackHatEvents

## Slide 16

# Finding Malicious Traffic

Monitoring the whole environment?

#BHUSA   @BlackHatEvents

## Slide 17

# Finding Malicious Traffic

#### Profile applications instead

#BHUSA   @BlackHatEvents

## Slide 18

# **Introducing… B** ehavioral **E** valuation of **A** pplication **M** etrics

●Analyzes network traffic

●Models applications

●Detects compromises

1

8 #BHUSA   @BlackHatEvents

## Slide 19

# **Native Application Models Included**

1

9 #BHUSA   @BlackHatEvents

## Slide 20

# The Research

#BHUSA   @BlackHatEvents

## Slide 21

# What data went into BEAM?

Over **2,000** organizations

**4.2 million 56 billion** different devices transactions

**7.5 million 1.5 million** different user agents different applications

Information presented in this talk is based on anonymized usage data collected by the Netskope Security Cloud platform relating to a subset of Netskope customers with prior authorization

#BHUSA   @BlackHatEvents

## Slide 22

# Overview of our approach

Attribution

Modeling

Detection

Identify applications

Build profiles

Identify anomalies

2

2 #BHUSA   @BlackHatEvents

## Slide 23

# Attribution

Network Traffic Input

Mapper

Enriched Events

#BHUSA   @BlackHatEvents

## Slide 24

# Leveraging User Agent Strings

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 92/100 on the text kept, 72/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Leveraging User Agent Strings
Sec-Ch-Ua-Mobile: 20
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
\User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36
```

## Slide 25

# User Agents → Applications

- LLM Summarization

   - Local Llama model 3.2

   - Google Gemini API

- Python user agent libraries

Chrome 134

#BHUSA   @BlackHatEvents

## Slide 26

# Modeling

Enriched Events

Model Training

Application Models

#BHUSA   @BlackHatEvents

## Slide 27

# Feature Selection

● _unusual DNS query patterns_ (SUNBURST) ● _anomalous repository access_ (3CX) ● _large outbound data transfers_ (MOVEit)

_What else can we add to this list_ ?

#BHUSA   @BlackHatEvents

## Slide 28

# Extracting 185 Features

Examples include:

- Time taken for requests and responses

- Time interval regularity

- Any sequences or notable patterns present

- Typical HTTP methods and status codes

- File types that are being uploaded and downloaded

#BHUSA   @BlackHatEvents

## Slide 29

# Extracting 185 Features

Examples include:

- Time taken for requests and responses

- Time interval regularity

- Any sequences or notable patterns present

- Typical HTTP methods and status codes

• File types that are being uploaded and downloaded

#BHUSA   @BlackHatEvents

## Slide 30

# Extracting 185 Features

#### Examples include:

- Time taken for requests and responses

- Time interval regularity

- Any sequences or notable patterns present

- Typical HTTP methods and status codes

- File types that are being uploaded and downloaded

#BHUSA   @BlackHatEvents

## Slide 31

# Extracting 185 Features

#### Examples include:

- Time taken for requests and responses

- Time interval regularity

- Any sequences or notable patterns present

- Typical HTTP methods and status codes

- File types that are being uploaded and downloaded

#BHUSA   @BlackHatEvents

## Slide 32

# Extracting 185 Features

#### Examples include:

- Time taken for requests and responses

- Time interval regularity

- Any sequences or notable patterns present

- Typical HTTP methods and status codes

- File types that are being uploaded and downloaded

#BHUSA   @BlackHatEvents

## Slide 33

# Trial run with 20 applications

- 5,000 observations / application

- Malware samples

- K-fold cross validation with a

single Random Forest model

#BHUSA   @BlackHatEvents

## Slide 34

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 87/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Box 4)
Chrome -
Cortana -
Edge -
Last Mile Telemetry -
Malware -
Microsoft BITS -
Microsoft Delivery Optimization -
Microsoft Excel -
Microsoft Office -
Microsoft Outlook -
Microsoft Teams —
Microsoft Word -
OneNote -
OneOutlook -
Outlook Web Host -
Postman -
RT HttpStack -
SkyDriveSync -
Slack -
w
=
o
>
w
2
Box -
Chrome -
Cortana -
Slack -
Safari -
Edge -
SkyDriveSync -
Last Mile Telem...
Postman -
OneNote -
RT HttpStack -
OneOutlook -
Malware -
Outlook Web Hos...
Microsoft BITS -
Microsoft Deliv...
rosoft Word -
Microsoft Excel -
Microsoft Offic...
Microsoft Outlo...
soft Teams -
=
Predicted
```

## Slide 35

# Detection

Detector

Explainer

Results

#BHUSA   @BlackHatEvents

## Slide 36

# Supply Chain Compromise Detection

- 56 billion transactions

- 500,000 observations / application

- XGBoost model per application

#BHUSA   @BlackHatEvents

## Slide 37

Results for Box
Box  Not Box  Total
(Predicted) (Predicted)
Box  499,987 13 500,000
(Actual)
Not Box  93 499,907 500,000
(Actual)
3
7
#BHUSA   @BlackHatEvents

## Slide 38

|Results for o|ther popul|ar applicati|ons|
|---|---|---|---|
||**FPR (%)**|**TDR (%)**|**Overall accuracy (%)**|
|**Asana**|0.003|99.988|99.993|
|**Box**|0.003|99.981|99.989|
|**Canva**|0.001|99.306|99.653|
|**Kandji**|0.012|99.965|99.977|
|**OmniFocus**|0.001|99.999|99.999|
|**Slack**|0.062|99.973|99.956|
|**Spotify**|0.046|99.946|99.950|
|**Todoist**|0.377|99.999|99.812|

#BHUSA   @BlackHatEvents

## Slide 39

# Can it detect a threat?

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 88/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
BRIEFINGS WY,
Can it detect a threat?
```

## Slide 40

# Supply Chain Compromise Simulation

**Red Team Member:**

Mohanraj

**Blue Team Members:** Colin and Dagmawi

**Red Team Mission:**

**Blue Team Mission:**

- Compromise a common app

- Use your own C2

   - Model common apps

   - Detect malicious communications

- Keep it secret

#BHUSA   @BlackHatEvents

## Slide 41

Red Team: Attacker Setup

Compromised application:

Command and Control:

#BHUSA   @BlackHatEvents

## Slide 42

# Red Team: Network Trafc fi

Victim Machine

Github Codespaces C2

#BHUSA   @BlackHatEvents

## Slide 43

Red Team: Network Trafc fi

Spotify/125200442 0SX_ARM64/0S X 14.7.1 [arm 2]

Victim Machine

Github Codespaces C2

#BHUSA   @BlackHatEvents

## Slide 44

# Red Team: Victim’s Machine

Spotify client (modified) C2 URL

C2 URL

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 82/100 on the text kept, 69/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
BRIEFINGS St,
Red Team: Victim’s Machine
Spotify client (modified) C2 URL
victim >> ./spotify-client.exe -server="sdper-duper-chains
41 6
victim >> pwd ig
/Users/ /Downloads/hack/simplesheLll
```

## Slide 45

# Red Team: Attacker’s Console

Victim Interaction

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 88/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
BRIEFINGS Sy ES
Red Team: Attacker’s Console
Victim
/codespaces~c2 >> make run .
Starting the server at :8443 Interaction
enter your command (Spotify/125200442 (43; @; 2)) : whoami
|
enter your command (Mozilla/5.@ (Macintosh; Intel Mac OS X 10_15_7) Ap
pleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.6723.117 Spotify/1.2
-52.442 Safari/537.36) : pwd
/Users/ /Downloads/hack/simpleshell
enter your command (Spotify/125200442 OSX_ARM64/0S X 14.7.1 [arm 2]) :
```

## Slide 46

# **Blue Team:** Defender’s Console

#### Anomaly with 94% confidence

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 79/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
pis hat
Blue Team: Defender’s Console
Anomaly with 94% confidence
Z
11] Potential supply chain compromise found / >»
i=8
Predicted class =(negative_label (94.0%)}
Top 3 predictions = [{'class': 'negative_label', ‘probability’: 94.0}, {‘class': 'Spotify',
FULL predictions path = i i i
```

## Slide 47

# Attacker’s Reaction

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 79/100 on the text kept, 72/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
pis hat
Attacker’s Reaction
2 % Mohanraj_ | Today at 9:19 AM 7
= £ wowwwwwww.. thats right
```

## Slide 48

# How did we detect this?

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 89/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
avg_time_taken_ms
sum_client_bytes
transactions
avg_client_bytes
min_client_bytes
min_time_taken_ms
median_client_bytes
std_time_taken_ms
median_server_bytes
median_time_taken_ms
domain_connect.facebook.net
min_server_bytes D avg_time_taken_ms
range_client_bytes
sum_client_bytes
range_timestamp
range_time_taken_ms +0 transactions
range_time_interval_sec
avg_client_bytes
max_time_taken_ms
83 other features i i
other features min_client_bytes
0.5
```

## Slide 49

# Demo

#BHUSA   @BlackHatEvents

## Slide 50

## How did we detect the anomaly in the demo?

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 86/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
How did
url_entropy
min_server_bytes
median_time_taken_ms
key_hostname_cnt
chrome_ratio
min_time_taken_ms
avg_path_depth
ua_entropy
avg_domain_length
resp_content_types_application/json B+ u rl entro py
p25_time_taken_ms
robust_cv_time_interval_sec m i n_se rve r_bytes
refered_traffic_pct
min_client_bytes . .
srancactions median_time_taken_ms
p75_client_bytes key_hostname_cnt
avg_client_bytes
131 other features
```

## Slide 51

Logarithmic SHAP Plot Values Each feature affects the odds that we found an anomaly:

●Feature 1: e<sup>0.05</sup> ≈ 1.05 → 1.05x ●Feature 2: e<sup>1.7</sup> ≈ 5.47 → 5.47x

#BHUSA   @BlackHatEvents

## Slide 52

# Finding Malicious Traffic

##### **xqpt5z.dagmawi.io is anomalous (99%)**

URL Entropy Application Hosts Path Depth
URL Randomness Not a known host Root path
Odds: 5.47x Odds: 4.06x Odds: 4.06x

5

2 #BHUSA   @BlackHatEvents

## Slide 53

# Bespoke Models

Network Traffic Input

Unsupervised ML Training

Application Models

#BHUSA   @BlackHatEvents

## Slide 54

# Bespoke modeling

- Any non-browser application

- Trains on traffic captures

- Unsupervised learning

#BHUSA   @BlackHatEvents

## Slide 55

# Training Components

Ensemble Anomaly Detector

Isolation Forest One-Class SVM Anomaly Detector Detection

Weighted Voting Ensemble Prediction

Autoencoder (TensorFlow)

#BHUSA   @BlackHatEvents

## Slide 56

# Capturing Traffic from Notion

Proxyman
Notion Client
(not browser)

#BHUSA   @BlackHatEvents

## Slide 57

# Bespoke Model Training

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 85/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
BRIEFINGS ae
Bespoke Model Training
B® Processing training data: notion_06_10_2025.har
@®. Step 1: Parsing network traffic data...
& Step 2: Enriching events with application intelligence...
@®. Step 3: Discovering applications in traffic...
f Step 4: Training machine learning models...
M Model saved: ./models/custom_models/notion_model.pkl
```

## Slide 58

# Bespoke Model Training

#### Model saved for Notion

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 83/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Bespoke Model Training
—— Model saved for Notion
B Processing training data:] notion_06_10_2025.har
@®. Step 1: Parsing network tlraffic data...
& Step 2: Enriching events with application intelligence...
@®. Step 3: Discovering applications in traffic...
r Step 4: Traini
<M Model saved: ./models/custom_models/notion_model.pk
```

## Slide 59

# Bespoke Model Detection

Notion and VSCode detected

We only have a Notion Model

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 86/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
@ Applications analyzed with custom models (1): .
@ Notion: 7 domains analyzed, all normal behavior detected aA Notion and VSCode detected
Wl DETECTION SUMMARY:
®. Total domains analyzed: 7
@ All domains showed normal behavior: 7
= No supply chain compromises detect
yzed (no model available) (1): We only have a Notion Model
B Applications found but NOT
Bi Visual Studio Code
@ To analyze these applications, train custom models using:
python -m beam —-train -i /path/to/training/data
@. Supply chain compromise detection completed for 1 applications.
@M No critical security issues detected
```

## Slide 60

# Bespoke Model Detection

#### Training data = no anomalies

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 90/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Applications analyzed with custom models (1):
@ Notion: 7 domains analyzed, all normal behavior detected
DETECTION SUMMARY:
®. Total domains analyzed: 7
@ All domains showed normal behavior: 7
Applications found but NOT analyzed (no model available) (1):
SH Visual Studio Code
To analyze these applications, train custom models using:
python -m beam —-train -i /path/to/training/data
Supply chain compromise detection completed for 1 applications.
No critical security issues detected
#BHUSA
—— Training data = no anomalies
@BlackHatEvents
```

## Slide 61

# Next Steps

#BHUSA   @BlackHatEvents

## Slide 62

# Challenges & future improvements

#### 1. High entropy applications

#BHUSA   @BlackHatEvents

## Slide 63

# Challenges & future improvements

#### 1. High entropy applications

2. Additional methods of attribution

#BHUSA   @BlackHatEvents

## Slide 64

# Challenges & future improvements

#### 1. High entropy applications

2. Additional methods of attribution

3. Further support for bespoke models

#BHUSA   @BlackHatEvents

## Slide 65

# **B** ehavioral **E** valuation of **A** pplication **M** etrics

#### Available now:

6

5 #BHUSA   @BlackHatEvents

## Slide 66

# Black Hat Sound Bytes / Takeaways

- Supply chain compromises require more than a single type of solution

- BEAM detects anomalies solely from web traffic

- BEAM can add new models for your applications’ network traffic

#BHUSA   @BlackHatEvents
