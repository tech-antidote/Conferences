---
title: "AI Assisted Decision Making of Security Review Needs for New Features"
speakers: ["Mrityunjay Gautam", "Pavan Kolachoor"]
conference: "Black Hat"
conference_full: "Black Hat USA 2023"
edition: "USA"
year: 2023
source_pdf: "Black Hat USA 2023 slides/Mrityunjay Gautam & Pavan Kolachoor_AI Assisted Decision Making of Security Review Needs for New Features.pdf"
pages: 45
sha256: "b577a213940fbe2e6691f168d00efb46be3e7fce214410188d26cca903591ba6"
text_chars: 11301
ocr_pages: 8
has_ocr: true
redacted_secrets: 0
ocr_confidence: 83.7
ocr_unreliable_blocks: 0
vision_verified_blocks: 1
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T04:16:23Z"
---
# AI Assisted Decision Making of Security Review Needs for New Features

**Speakers:** Mrityunjay Gautam, Pavan Kolachoor  
**Conference:** Black Hat USA 2023  
**Source:** `Black Hat USA 2023 slides/Mrityunjay Gautam & Pavan Kolachoor_AI Assisted Decision Making of Security Review Needs for New Features.pdf` (45 pages)


## Slide 1

### AI Assisted Decision Making of Security Review Needs

**Mrityunjay Gautam Pavan Kolachoor**

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 91/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
LUISA &
AUGUST 9-10, 20253
BRIEFINGS
Al Assisted Decision Making of Security
Review Needs
Mrityunjay Gautam
Pavan Kolachoor
#BHUSA @BlackHatEvents
```

## Slide 2

# **$ whoami**

Mrityunjay Gautam Sr. Director, Product Security Databricks.

Pavan Kolachoor Sr. Manager, Product Security Databricks.

@xdead10cc

@kolachoor

#BHUSA  @BlackHatEvents

## Slide 3

## Disclaimer

The views expressed in this presentation are strictly those of the speaker(s). Any comments made or views expressed during this presentation are not endorsed by Databricks, and hence would not be a legal liability of Databricks.

#BHUSA  @BlackHatEvents

## Slide 4

##### **Problem Statement**

High Speed of Development in Cloud Env

Low Security vs Developer Ratio (1:100)

100s of Sprint Teams in Agile Dev Process

#BHUSA  @BlackHatEvents

## Slide 5

##### **Problem Statement**

High Speed of
Development in
Cloud Env
Train Developers to
identify Security
Sensitive Features

Low Security vs Developer Ratio (1:100)

(1:100)
Security
Champions in Dev
Teams
100s of Sprint
Teams in Agile
Dev Process

#BHUSA  @BlackHatEvents

## Slide 6

##### **Problem Statement**

High Speed of Development in Cloud Env Train Developers to identify Security Sensitive Features Low Security vs Developer Ratio (1:100) Security Champions in Dev Teams

Low Security vs Developer Ratio (1:100)

Features reported Feature Released for Security Review after SDLC

100s of Sprint Teams in Agile Dev Process

#BHUSA  @BlackHatEvents

## Slide 7

##### **Problem Statement**

High Speed of Development in Cloud Env Train Developers to identify Security Sensitive Features

Low Security vs Developer Ratio (1:100)

Security Champions in Dev Teams

100s of Sprint Teams in Agile Dev Process

Features reported Feature Released for Security Review after SDLC

SECURITY BLINDSPOT

Features NOT reported for Security Review **But Needs Security Review**

Feature Released with SECURITY WEAKNESSES

#BHUSA  @BlackHatEvents

## Slide 8

##### **Security Review Decision Making**

- Is this a good candidate for Automation?

- Additionally needs a base human intelligence and some domain expertise in security and product knowledge

###### **Hypothesis**

- **Can Deep Learning & NLP meet these requirements ?**

#BHUSA  @BlackHatEvents

## Slide 9

##### **“Engineering” English vs “Spoken” English**

- ●Engineering language is unique for any Organization

   - ○Product Names, Code Names, Abbreviations, etc..

#BHUSA  @BlackHatEvents

## Slide 10

##### **“Engineering” English vs “Spoken” English**

●Engineering language is unique for any Organization

○Product Names, Code Names, Abbreviations, etc..

**COW**

###### **Engineering**

**Copy on Write**

###### **Spoken English**

#BHUSA  @BlackHatEvents

## Slide 11

##### **“Engineering” English vs “Spoken” English**

●Engineering language is unique for any Organization

○Product Names, Code Names, Abbreviations, etc..

**COW PoC**

**Engineering**

**Copy on Write Proof of Concept**

**Spoken English**

#BHUSA  @BlackHatEvents

## Slide 12

##### **“Engineering” English vs “Spoken” English**

●Engineering language is unique for any Organization

○Product Names, Code Names, Abbreviations, etc..

**COW**

**PoC**

**Spark**

###### **Engineering**

###### **Copy on Write**

###### **Proof of Concept**

###### **Apache Spark**

###### **Spoken English**

#BHUSA  @BlackHatEvents

## Slide 13

## Machine Learning Basics

#BHUSA  @BlackHatEvents

## Slide 14

Supervised
Learning
Algorithm

##### **Supervised Learning: Classifiers**

**Taxonomy**

**Labelled Input**

#BHUSA  @BlackHatEvents

## Slide 15

##### **Deep Learning: Multi Layer Perceptron**

Input Layer

Output Layer

**Hidden Layers**

#BHUSA  @BlackHatEvents

## Slide 16

Training Data Collection Because no training is possible without the right kind of data…

#BHUSA  @BlackHatEvents

## Slide 17

##### **Engineering Text Sources**

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 77/100 on the text kept, 62/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Engineering Text Sources
PDF :
= Confluence
XJIRA
€@, OneDrive
Kis! 1 Office 365
```

## Slide 18

##### **Data Download Strategy**

|**Data Source**|**Authentication**|**Text Extraction Strategy**|
|---|---|---|
|Jira|PAT Token|JSON Extraction => Linked Tickets|
|Confluence|PAT Token|Requests API => HTML Parsing => HTML Tag Cleanup|
|Google Doc|OAuth2 Token|Use Google Docs APIs => Extract Text|
|Aha!|API Key|Python Aha Package => Extract Feature Content|
|Public Webpages|NONE|Requests API => HTML Parsing => HTML Tag Cleanup|
|Local Files (Pdf,
Docx, Xlsx, etc)|NONE|PDF: Standard Python packages and Text extraction techniques
Office: Unzip and Parse using standard reg-ex|

#BHUSA  @BlackHatEvents

## Slide 19

## First Attempt: Model v1.0

Now that we have the data…

#BHUSA  @BlackHatEvents

## Slide 20

Create a “SET” of
Text Cleanup
words
Remove number
Remove English  Convert all words
and single letter
“stop words” to lower case
words
#BHUSA  @BlackHatEvents

##### **Building the Vocabulary**

Extract Content
from Jira Tickets

## Slide 21

Vectorization of Documents
Array of integers
Document Parsing  Calculate Term
Text Cleanup of size(Vocab)
& Tokenization Frequency
length
Remove number
Remove English  Convert all words
and single letter
“stop words” to lower case
words
#BHUSA  @BlackHatEvents

## Slide 22

##### **Training Pipeline**

**Manually Processed Text Processing Pipeline Security Review Tickets and Vectorization**

**Manually Processed Text Processing Pipeline Security Review Tickets and Vectorization**

Multi Layer
Perceptron
Input: Size (Vocab)
Output: 2

**MODEL v1.0**

#BHUSA  @BlackHatEvents

## Slide 23

##### **Results & Observations**

###### **Notes:**

- ●Multiple configurations with different hidden layers ●Individual Model Accuracy = 63% to 71%

###### **Can we try Ensemble Classifier ?**

###### **Model v1.0**

#BHUSA  @BlackHatEvents

## Slide 24

##### **Results & Observations**

**Accuracy: 78%**

###### **VERDICT**

**Not Acceptable for Use without Human Interference**

**Ensemble Model v1.5**

#BHUSA  @BlackHatEvents

## Slide 25

## Deeper into Machine Learning

#BHUSA  @BlackHatEvents

## Slide 26

Unsupervised
Learning
Algorithm

##### **Unsupervised Learning**

**Clusters**

**Unlabelled Input**

#BHUSA  @BlackHatEvents

## Slide 27

##### **Convolutional Neural Network**

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 82/100 on the text kept, 70/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Convolutional Neural Network
Dog
Input image Convolution ReLU layer Pooling layer *, FJ Output
layer # classes
Fully connected
layer
```

## Slide 28

## Final Implementation: Clairvoyant

The one that works…

#BHUSA  @BlackHatEvents

## Slide 29

##### **Sample Use Case: Apache Spark**

**What is Apache Spark™?**

Apache Spark™ is a multi-language engine for executing data engineering, data science, and machine learning on single-node machines or clusters.

#BHUSA  @BlackHatEvents

## Slide 30

##### **Text Cleanup: SparkNLP Pipeline**

Tokenizer

#BHUSA  @BlackHatEvents

## Slide 31

##### **Text Cleanup: SparkNLP Pipeline**

Tokenizer Lemmatizer
{Improved, Improving,
Improve, Improvements}
=> Improve

#BHUSA  @BlackHatEvents

## Slide 32

##### **Text Cleanup: SparkNLP Pipeline**

Tokenizer Lemmatizer
Normalizer
{Improved, Improving,
"résumé," = “resume”
Improve, Improvements}
=> Improve “John” = “john”

#BHUSA  @BlackHatEvents

## Slide 33

Text Cleanup: SparkNLP Pipeline
Stop Words
Tokenizer Lemmatizer
Normalizer
Removal
{Improved, Improving,  Remove irrelevant words
"résumé," = “resume”
Improve, Improvements}
like – “a”, “an”, “the”,
=> Improve “John” = “john”
“of”, “in”

##### **Text Cleanup: SparkNLP Pipeline**

#BHUSA  @BlackHatEvents

## Slide 34

Engineering Language Model Creation
Jira &
Confluence
Unsupervised
Clustering Model
Other
Sources
Spark NLP
Corpus
Pipeline
Word Vectors (300 Dim)
Public Docs Clean Data
Raw Data
● Word Associations
● Word Vector Representation
Google Docs
#BHUSA  @BlackHatEvents

## Slide 35

###### **Sample Word Vectors over Apache Spark**

#BHUSA  @BlackHatEvents


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 71/100 on the text kept, 63/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
AutoSpill - Investigation

1. Autofill request from
Android to autofill service

[diagram, top to bottom]
FillRequest
  |
FillContext
  FocusedID: 1073741826:196608
  |
AssistStructure
  |
WindowNode
  |
1. RootView
  |
  +-- 1.1 NativeView                      +-- 1.2 WebView
      ChildrenCount: 2                        ChildrenCount: 2
      AutoFillId: 1073741829                  AutoFillId: 1073741826
      WebDomain: null                         WebDomain: m.facebook.com

1.1.1 Username                    1.1.2 Password
AutoFillId: 1073741824            AutoFillId: 1073741825
Dimension: 300x100                Dimension: 300x100
AutofillType: 1                   AutofillType: 1
AutofillHints: null               AutofillHints: null
WebDomain: null                   WebDomain: null
AutofillOptions: null             AutofillOptions: null
HtmlInfo: null                    HtmlInfo: null
ViewID: 2131231192                ViewID: 2131231055
InputType: 1 (text)               InputType: 129 (password)

1.2.1 Username                            1.2.2 Password
AutoFillId: 1073741826:196608             AutoFillId: 1073741826:196609
Dimension: 300x100                        Dimension: 300x100
AutofillType: 1                           AutofillType: 1
AutofillHints: on                         AutofillHints: on
WebDomain: null                           WebDomain: null
AutofillOptions: null                     AutofillOptions: null
HtmlInfo: [Pair{name email},              HtmlInfo: [Pair{name pass},
Pair{type email},                         Pair{type password},
Pair{label Mobile                         Pair{label Password},
number or email address},                 Pair{ua-autofill-hints null},
Pair{ua-autofill-hints null},             Pair{id m_login_email},
Pair{id m_login_email},                   Pair{maxLength 2147483647}]
Pair{maxLength 2147483647}]
ViewID: -1                                ViewID: -1
InputType: 0                              InputType: 0
```

## Slide 36

##### **Visualizing the Word Vectors in TWO Dimensions**

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 87/100 on the text kept, 54/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Visualizing the Word Vectors in TWO Dimensions
Udf
Dataframe Pythonic
e Pyspark_Panda
Spark
e
Rdd
A Createdataframe
Dataframes
Panda
Astype
Dataset
e Groupby Function Format °
e Japle Delta
Link_Spark
Row
```

## Slide 37

Training Deep Learning Classifier
Aha Manual Triage  Threat Model  Word Vectors (300 Dim)
Data Documents
Raw Data Spark NLP Pipeline
Corpus
Security Review
SEC Defects & Linked
Tickets & Linked
Tickets
Tickets
Restrict to first
1000 Words
ONLY
Aha Manual Triage  Support Tickets for
Data Stability
Convolutional Neural
Raw Data Spark NLP Pipeline Network Clairvoyant
Corpus
Input = 300 x 1000
Operations Tickets ML Tickets
Output = 2
#BHUSA  @BlackHatEvents
Positive
Negative

## Slide 38

##### **Confusion Matrix**

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 89/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Confusion Matrix
precision
required 0.98
notrequired 0.98
accuracy
macro avg
weighted avg
recall
0.97
fl-score
0.98
0.99
0.98
0.98
0.98
] - 1s 35ms/step
Support
264
436
100
700
100
```

## Slide 39

##### **Confusion Matrix**

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 89/100 on the text kept, 72/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Confusion Matrix
precision
required 0.98
notrequired 0.98
accuracy
macro avg
weighted avg
recall
fi-score support
264
436
100
700
100
```

## Slide 40

Using the Trained Model for Prediction
Word Vectors (300 Dim)
Text
Confidence
Preprocessing
Threshold Config
Restrict to first
1000 Words
ONLY
ASF Jira
Query for
New Spark
Features
Confidence Score
Key: SPARK-23441
Required: X%
Spark NLP Pipeline Clairvoyant
#BHUSA  @BlackHatEvents
 TEXT EXTRACTION

## Slide 41

#### DEMO

#BHUSA  @BlackHatEvents

## Slide 42

##### **Key Takeaways**

**Time to move to the next stage of automation power by AI**

#BHUSA  @BlackHatEvents

## Slide 43

##### **Key Takeaways**

**Time to move to the next stage of automation power by AI**

**Engineering English is NOT same as Spoken English**

**CNN = “Convolutional Neural Network”**

**OR**

#BHUSA  @BlackHatEvents

## Slide 44

##### **Key Takeaways**

**Time to move to the next stage of automation power by AI**

**Engineering English is NOT same as Spoken English**

**AI can “nitro boost” Security Development Lifecycle and DevSecOps**

**CNN = “Convolutional Neural Network”**

**OR**

#BHUSA  @BlackHatEvents

## Slide 45

# Questions?

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 83/100 on the text kept, 63/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
USA &
Questions?
#BHUSA @BlackHatEvents
```
