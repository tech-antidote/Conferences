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
text_chars: 13038
ocr_pages: 9
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:20:58Z"
---
# AI Assisted Decision Making of Security Review Needs for New Features

**Speakers:** Mrityunjay Gautam, Pavan Kolachoor  
**Conference:** Black Hat USA 2023  
**Source:** `Black Hat USA 2023 slides/Mrityunjay Gautam & Pavan Kolachoor_AI Assisted Decision Making of Security Review Needs for New Features.pdf` (45 pages)


## Slide 1

### AI Assisted Decision Making of Security Review Needs

**Mrityunjay Gautam Pavan Kolachoor**

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pifek hat
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Output Layer
J
UA
S554 ]
RP SEPDY |
BRR
oe)
NY
KY
OC
My
Noh)
\
\
ERR,
AAW
Deep Learning: Multi Layer Perceptron
ro
®
>
©
—!
—_
>
a.
<
m
fu
0
(u
<
Ul
4)
&
3
Cg
O
Yi \
OOOQOO0O ©
NWA
Hidden Layers
```

## Slide 16

Training Data Collection Because no training is possible without the right kind of data…

#BHUSA  @BlackHatEvents

## Slide 17

##### **Engineering Text Sources**

#BHUSA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
USA 20253
Engineering Text Sources
PDF :
= Confluence
XJIRA
€@, OneDrive
Kis! 1 Office 365
=a & B
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 20253
Convolutional Neural Network
Dog
= ee ee Not dog
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 20253
Sample Word Vectors over Apache Spark
AY L L W " >>> db_wv["dataframe"]
>>> for elem in db_wv.most_similar("dataframe" ): mernap({0.9310919", 050785744, 0.278117, -3.5078952 , -1. 3010696,
— = 0255014 , -0.4637812 , -0.28312248, 0.97335374, 2.3100562 ,
s .731182 , -1.844407 , 0©.8353111 , -0.63139266, ©.00630491,
p run 1 ( elem) 364567, -0.59393615, 1.6423836 , -0.8014536 , 1.4345028 ,
643103 , 0.22679166, 1.4599513 , 0.7172914 , 2.044413 ,
7967019 , 0.94810575, 0©.4200268 , 2.9429126 , -@.8506799 ,
° 74401563, -1.5902468 , -0.23007932, -0.32131946, 0.462017 ,
333657, -0.62744874, 0©.09188309, 0.987241 , 0.1586956 ,
d ¥ ! 48161167, -0.708081 , 0.6901429 , -0.88133466, -1.6377207 ,
ata ranes ’ 0) ° 6118282675743103) 0239885 , 0.3850151 , -1.6293939 99386686, .39724597,
8518817 , .15128905, 0.5563997 3667917 , -1.8927845 ,
d ' 411923, -1.7477007 , -0.8300083 19485356, 1.8997799 ,
ataset > 0) Ps 55197674036026) -06248 , -1.3756353 , -1.1744969 0502687 , 0.3466141 ,
. 76184255, -0.03475898, 3.770701 -32482 .2160301 ,
l ! 6) 078 29189300 3 Fs 9291667 , 0.12784757, 1.1212947 .7264751 . 18605056,
co umn 3 e 55 5 .1273634 , 0.04766518, -1.0251166 , -1.9720559 1214161 ,
83759 ,_--1.1744149 , -0.06331337, -2.3759587 .47384828,
d ' 6) 50923 341 5 1 268005 .74272263, -2.2255695 , -1.2124482 , -1.9246694 600604 ,
pan a r) ° .3197237 , -4.0106916 , -0.6822084 , -2.104292 .23427726,
0888906 , 2.0269437 , 3.858152 , -0.7961048 40143135,
panda_dataframe', 0.5089078545570374) "441909 | -0,79080054, 018853069 , 03444723 | 0.62482643,
,
-4761695 , -0.61990714, -5315938 , -294078 -14454891,
pandas’, 0.5045510530471802) “pasdsze | 2.2908278 | 206970937 | 0.7407337 | 14873685 ,
- 7496026 1.3792899 -4161917 , + 7929713 -8746275 ,
sparkdataframe', 0.4986857771873474) “Geaces2 | 2.0959942 , 1.1508056 , 4.208189 | -1-1084874 ,
2
. 73587084, -1.0648205 -9000793 , + 2424848 -08619205,
Z
index_multiindex', 0.498322993516922) “aaesb46 | 0.62364346, 0150121385, 05659973 | 0.239006%3,
- 7856058 , -3.2071939 , -759164 , -8611768 - 17939295,
python', 0.49831458926200867) "17962093, 113623391 , -0.9124389 | 17653879 | 09030031 ,
-2861032 , -1.105925 , -6695298 , -5895758 -436935 ,
ta ble ' 0 49779176712036133 .2793896 , -2.7052615 , -0.41566476, -0.2550927 .9705007 ,
3 ° .4212031 , 1.4761783 , 0.830782 , -1.174425 .44477263,
-8022616 , -0.21900089, -6940251 , -0655376 -0880742 ,
(
(
(
(
(
(
(
(
(
(
```

## Slide 36

##### **Visualizing the Word Vectors in TWO Dimensions**

#BHUSA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 20253
Visualizing the Word Vectors in TWO Dimensions
Udf
i Python_Udf
e Python_Udfs
. Scalar
. Panda_Udf
~ Panda_Udf
e Pandas_Udf .
. Type_Hint
. Python_Pys
ivesparksubmittests
Dataframe Pythonic
° e'y @ Doctests
@ Pandas Namedtuple o Mypy
e A Paskcontexttests e yarrow
e Pyspark_Panda
@ Cloudpickle  Pandasonspark
@ Panda e Sphinx
eFython_Docs Koalas
* Pyspark\e Pelately
Spark
e
e ol
@ Sparkr . Link_Spark
Rdd
@
A Createdataframe
@ [opandas
- Panda_ Bd tase |
Dataframes
Panda
uy Dataframe
> Sparkdatafrarrre
Astype
= Df_Df Surat RAER Gea spar
. Python
. Df
Dataset
e Groupby Function Format °
- Input
. Sal A Data
e Japle Delta
Link_Spark
- 7 Column ¢ Parquet
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 20253
Confusion Matrix
precision
required 0.98
notrequired 0.98
accuracy
macro avg
weighted avg
recall
0.97
©.99
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 20253
Confusion Matrix
SSSSSSSSSssSsessssssseses=sa== | _ 1s 35ms/step
precision
required 0.98
notrequired 0.98
accuracy
macro avg
weighted avg
recall
©.97
©.99
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pisek hat
USA &
Questions?
#BHUSA @BlackHatEvents
```
