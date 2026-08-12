---
title: "VoBERT Unstable Log Sequence Anomaly Detection Introducing Vocabulary-Free BERT"
speakers: ["Eduardo Barbaro", "Yury Zhauniarovich", "Anna Lukina", "Daan Hofman"]
conference: "Black Hat"
conference_full: "Black Hat Europe 2023"
edition: "Europe"
year: 2023
source_pdf: "Black Hat Europe 2023 slides/Eduardo Barbaro, Yury Zhauniarovich, Anna Lukina, Daan Hofman_VoBERT Unstable Log Sequence Anomaly Detection Introducing Vocabulary-Free BERT.pdf"
pages: 43
sha256: "496bbc9d906e4698d3231672399d3868f249f84796f419b25d7767981895ae94"
text_chars: 16115
ocr_pages: 13
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:11:16Z"
---
# VoBERT Unstable Log Sequence Anomaly Detection Introducing Vocabulary-Free BERT

**Speakers:** Eduardo Barbaro, Yury Zhauniarovich, Anna Lukina, Daan Hofman  
**Conference:** Black Hat Europe 2023  
**Source:** `Black Hat Europe 2023 slides/Eduardo Barbaro, Yury Zhauniarovich, Anna Lukina, Daan Hofman_VoBERT Unstable Log Sequence Anomaly Detection Introducing Vocabulary-Free BERT.pdf` (43 pages)


## Slide 1

## **VoBERT: Unstable Log Sequence Anomaly Detection Introducing Vocabulary-Free BERT**

**Dr Eduardo Barbaro** Head of Security Analytics at ING CISO Visiting Researcher Cybersecurity Lab TUDelft

**List of contributors:** Daan Hofman, **_ING_** _&_ **_TUDelft_** Eduardo Barbaro, **_ING_** _&_ **_TUDelft_** Yury Zhauriarovich, _Assistant professor_ **_TUDelft_** Anna Lukina, _Assistant professor_ **_TUDelft_**

## Slide 2

### **Key Take Aways**

Enables learning from **sequential data** Increases robustness: Also works for **unstable** log data Increases **explainability** : provides an element-level score Shows the importance of **evaluating using real-world data**

2

## Slide 3

### **Anomaly Detection?**

The identification of **rare events** or observations which deviate significantly from **most of the data**

Finding **weird** things among **normal** things

3

## Slide 4

### **Log Sequence?**

Any software produces log files

Log analysis is useful for: Finding errors in software behaviour Detect potential cybersecurity threats

Analysts must “manually” identify attacks

4

## Slide 5

### **Log Sequence Anomaly Detection**

5

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Log Sequence Anomaly Detection
f ~ ‘a
Username field filled in Username field filled in
N ) ‘ T
‘a ¥ ~ (
Password field filled in Login Succesfull
N J J y
Password field filled in
Login button clicked
\ J y, ¥
Login button clicked
Login Succesfull
oq x
(b) Anomalous Log
(a) Normal Log sequence sequence
```

## Slide 6

### **<u>Unstable Log Sequence Anomaly Detection</u>**

66

6

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Unstable Log Sequence Anomaly Detection
( ’) ( \ )) c
Username field filled in _=> Username field populated I Username field filled in
\ / L ) J \ J
( ¥ > r ¥ \ a
Password field filled in Password field populated Login Succesfull
\ y, a J y, J y,
( ’ ) ( ) f _ .
Login button clicked Login button clicked [ Password field filled in
\ ) \ J J J
a Y ~ la ~ (
i Login button clicked
Login Succesfull Login Succesfull L
\ y,
\ }
QO Y) “
(c) Normal Log sequence (b) Anomalous Log
(a) Normal Log sequence with slightly changed log sequence
messages
```

## Slide 7

**That begs the following question: (and some others too)**

### **How can we identify anomalies in unstable sequential log data?**

**1. Explainability** : what is the influence of each individual log/alert?

**2. Unstable Logs:** how can we deal with log instability?

**3. Real-world vs synthetic data** : how do models perform on real-world security events?

7

## Slide 8

### **Introduction**

2. Log Grouping

8

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Introduction
1. Log Parsing
Vee 1!
i. 081109 205931 13 INFO dfs.DataBlockScanner: ;
| Verification succeeded for blk_4980916519894289 | >
‘ !
Fixed partitioning
2. Log Grouping
```

## Slide 9

### **Step 1: Log Parsing (Cleaning the house)**

Raw log message

LogKey

9

## Slide 10

### **Step 2: Log Grouping (too much data….)**

##### **2. Log Grouping**

Fixed Window

Sliding Window
Session Window

10

## Slide 11

### **Pre-processing Output**

### **Sequence 1**

**Sequence 2**

**Sequence 3**

11

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Sequence 1
Sequence 2
Sequence 3
wee eee ee ew ew ee ewe ee ew ew ew ewe ew ew ew ew ew ew ew ew ew ee ew ew ew ew ew ew ew ew ew ee ew ew ew ee eH
Meee ee ee ee ee eB ee ee ee ee ee ee eB ee ee ee ee ee ee ee ee ee ee ee ee
11
```

## Slide 12

### **How to detect anomalies?**

Rule based? Too noisy (loads of false positives)

Shallow Machine Learning? We lose the temporal (order) information

Deep Learning? Potentially. But where do we start?

12

## Slide 13

## **Background**

**So many words, so little numbers Where do we start?**

## Slide 14

### **How do we go from words to numbers?**

‘The moon, Earth's only natural satellite, has been a subject of fascination and wonder for thousands of years.’

|a|and|been|earth|fascination|for|has|moon|
|---|---|---|---|---|---|---|---|
|1|1|1|1|1|1|1|1|
|natural|of|only|subject|thousands|the|wonder|years|
|1|2|1|1|1|1|1|1|

The English Wikionary has over 700k entries

“Raise for everyone, no termination!”

or

The above can work, but word order has some meaning…

“No raise, termination for everyone!”

14

## Slide 15

### **Tokenization**

|Tokenisation
method|Tokens|Token count|Vocab size|
|---|---|---|---|
|Sentence|‘The moon, Earth's only natural satellite, has been a subject of
fascination and wonder for thousands of years.’|1|# sentences in doc|
|Word|'The', 'moon,', "Earth's", 'only', 'natural', 'satellite,', 'has', 'been',
'a', 'subject', 'of', 'fascination', 'and', 'wonder', 'for', 'thousands',
'of', 'years.'|18|171K (English1)|
|Sub-word|'The', 'moon', ',', 'Earth', "'", 's', 'only', 'natur', 'al', 'satellite', ',',
'has', 'been', 'a', 'subject', 'of', 'fascinat', 'ion', 'and', 'wonder',
'for', 'thousand', 's', 'of', 'year’, ‘s', '.'|27|(varies)|
||'T', 'h', 'e', ' ', 'm', 'o', 'o', 'n', ',', ' ', 'E', 'a', 'r', 't', 'h', "'", 's', ' ', 'o',
'n', 'l', 'y', ' ', 'n', 'a', 't', 'u', 'r', 'a', 'l', ' ', 's', 'a', 't', 'e', 'l', 'l', 'i', 't', 'e',|||
|Character|',', ' ', 'h', 'a', 's', ' ', 'b', 'e', 'e', 'n', ' ', 'a', ' ', 's', 'u', 'b', 'j', 'e', 'c', 't', '
', 'o', 'f', ' ', 'f', 'a', 's', 'c', 'i', 'n', 'a', 't', 'i', 'o', 'n', ' ', 'a', 'n', 'd', ' ', 'w',
'o', 'n', 'd', 'e', 'r', ' ', 'f', 'o', 'r', ' ', 't', 'h', 'o', 'u', 's', 'a', 'n', 'd', 's', ' ',
'o', 'f', ' ', 'y', 'e', 'a', 'r', 's', '.'|110|52 + punctuation (English)|

15

## Slide 16

### **Tokenization**

Tokenization
Tokens  Token count Vocab size
method
‘The moon, Earth's only natural satellite, has been a subject of
Sentence  1  # sentences in doc
fascination and wonder for thousands of years.’
'The', 'moon,', "Earth's", 'only', 'natural', 'satellite,', 'has', 'been', 'a',
Word  'subject', 'of', 'fascination', 'and', 'wonder', 'for', 'thousands', 'of',  18  171K (English1)
'years.'
'The', 'moon', ',', 'Earth', "'", 's', 'only', 'natur', 'al', 'satellite', ',', 'has',
Sub-word  'been', 'a', 'subject', 'of', 'fascinat', 'ion', 'and', 'wonder', 'for',  37  (varies)
'thousand', 's', 'of', 'year’, ‘s', '.'
Pros:
'T', 'h', 'e', ' ', 'm', 'o', 'o', 'n', ',', ' ', 'E', 'a', 'r', 't', 'h', "'", 's', ' ', 'o', 'n',
Intuitive.
'l', 'y', ' ', 'n', 'a', 't', 'u', 'r', 'a', 'l', ' ', 's', 'a', 't', 'e', 'l', 'l', 'i', 't', 'e', ',', ' ',
'h', 'a', 's', ' ', 'b', 'e', 'e', 'n', ' ', 'a', ' ', 's', 'u', 'b', 'j', 'e', 'c', 't', ' ', 'o', 'f',
Character  110  52 + punctuation (English)
' ', 'f', 'a', 's', 'c', 'i', 'n', 'a', 't', 'i', 'o', 'n', ' ', 'a', 'n', 'd', ' ', 'w', 'o', 'n', 'd', Cons:
'e', 'r', ' ', 'f', 'o', 'r', ' ', 't', 'h', 'o', 'u', 's', 'a', 'n', 'd', 's', ' ', 'o', 'f', ' ', 'y', Big vocabularies.
'e', 'a', 'r', 's', '.'
Complications such as handling misspellings.
Other out-of-vocabulary words.

16

## Slide 17

### **Tokenization**

Tokenizatio Tokens Token count Vocab size n method <u>Pros:</u> ‘The moon, Earth's only natural satellite, has been a subject of Sentence Small vocabulary. 1 # sentences in doc fascination and wonder for thousands of years.’ ~~No out-of-vocabulary words.~~ 'The', 'moon,', "Earth's", 'only', 'natural', 'satellite,', 'has', 'been', 'a', Word 'subject', 'of', 'fascination', 'and', 'wonder', 'for', 'thousands', 'of', 18 171K (English1) Cons: 'years.' ~~Loss of context within words.~~ 'The', 'moon', ',', 'Earth', "'", 's', 'only', 'natur', 'al', 'satellite', ',', 'has', Sub-word 'been', 'a', 'subject', 'of', 'fascinat', 'ion', 'and', 'wonder', 'for', Much longer sequences for a given input. 27 (varies) 'thousand', 's', 'of', 'year’, ‘s', '.' 'T', 'h', 'e', ' ', 'm', 'o', 'o', 'n', ',', ' ', 'E', 'a', 'r', 't', 'h', "'", 's', ' ', 'o', 'n', 'l', 'y', ' ', 'n', 'a', 't', 'u', 'r', 'a', 'l', ' ', 's', 'a', 't', 'e', 'l', 'l', 'i', 't', 'e', ',', ' ', 'h', 'a', 's', ' ', 'b', 'e', 'e', 'n', ' ', 'a', ' ', 's', 'u', 'b', 'j', 'e', 'c', 't', ' ', 'o', 'f', Character 110 52 + punctuation (English) ' ', 'f', 'a', 's', 'c', 'i', 'n', 'a', 't', 'i', 'o', 'n', ' ', 'a', 'n', 'd', ' ', 'w', 'o', 'n', 'd', 'e', 'r', ' ', 'f', 'o', 'r', ' ', 't', 'h', 'o', 'u', 's', 'a', 'n', 'd', 's', ' ', 'o', 'f', ' ', 'y', 'e', 'a', 'r', 's', '.'

17

## Slide 18

### **Tokenization**

<u>Compromise</u> Tokenizatio Tokens “Smart” vocabulary built from characters which co-occur frequently. Token count Vocab size n method ~~More robust to novel words. Compromise~~ ‘The moon, Earth's only natural satellite, has been a subject of Sentence “Smart” vocabulary built from characters which co-occur frequently. 1 # sentences in doc fascination and wonder for thousands of years.’ ~~More robust to novel words.~~ 'The', 'moon,', "Earth's", 'only', 'natural', 'satellite,', 'has', 'been', 'a', Word 'subject', 'of', 'fascination', 'and', 'wonder', 'for', 'thousands', 'of', 18 171K (English1) 'years.' 'The', 'moon', ',', 'Earth', "'", 's', 'only', 'natur', 'al', 'satellite', ',', 'has', Sub-word 'been', 'a', 'subject', 'of', 'fascinat', 'ion', 'and', 'wonder', 'for', 27 (varies) 'thousand', 's', 'of', 'year’, ‘s', '.' 'T', 'h', 'e', ' ', 'm', 'o', 'o', 'n', ',', ' ', 'E', 'a', 'r', 't', 'h', "'", 's', ' ', 'o', 'n', 'l', 'y', ' ', 'n', 'a', 't', 'u', 'r', 'a', 'l', ' ', 's', 'a', 't', 'e', 'l', 'l', 'i', 't', 'e', ',', ' ', 'h', 'a', 's', ' ', 'b', 'e', 'e', 'n', ' ', 'a', ' ', 's', 'u', 'b', 'j', 'e', 'c', 't', ' ', 'o', 'f', Character 110 52 + punctuation (English) ' ', 'f', 'a', 's', 'c', 'i', 'n', 'a', 't', 'i', 'o', 'n', ' ', 'a', 'n', 'd', ' ', 'w', 'o', 'n', 'd', 'e', 'r', ' ', 'f', 'o', 'r', ' ', 't', 'h', 'o', 'u', 's', 'a', 'n', 'd', 's', ' ', 'o', 'f', ' ', 'y', 'e', 'a', 'r', 's', '.'

18

## Slide 19

### **Represent words with vectors**

Words with similar meaning tend to occur in similar contexts:

The king waved to the crowd from the balcony. The queen waved to the subjects from the terrace.

The words **king** and **queen** share context here, as do **balcony** and **terrace** .

19

Images source: https://blog.acolyer.org/

## Slide 20

### **Now, pay attention, this is the good stuff**

Transformer
The king waved to the
De koning zwaaide vanaf
large crowd from the
Transformer het balkon naar de grote
balcony and they
Encoder Decoder menigte en zij waren blij.
rejoiced.
High Attention

**The king waved to the large crowd from the balcony and they rejoiced.**

Low Attention

## Slide 21

### **Even the best models need fine-tuning**

Fine-tuning enables the tailoring of LLMs to specific IT challenges, bridging the gap between generalised understanding and specialised solutions.

**Pre-Training**

**Fine-Tuning**

21

## Slide 22

### **BERT models are a great starting point**

Bidirectional Encoder Representations from Transformers

Transformer-based architecture: Just like **GPT** Transforms text based on attention-mechanism

Word embeddings with context: I go to a bar ≠ I raise the bar

22

## Slide 23

### **BERT training: Masked Language Modelling (MLM)**

23

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
BERT training: Masked Language Modelling (MLM)
Model
Output LOG B LOGA
BERT
Input
i Original [Loca [Loc | [Loe c| [Los 0| [Loc |
‘Sequence
23
```

## Slide 24

### **BERT for Anomaly Detection**

Trained only on normal sequences

Predicts **poorly** on anomalous sequences

24

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
BERT for Anomaly Detection
= Trained only on normal sequences prec eenecee cece ee ee ene eee
i Model LOGB LOGA
. ' Output '
= Predicts poorly on anomalous sequences a
BERT
Input
i Original [toca [toss [tose] [tos] [rose |
‘Sequence
24
```

## Slide 25

### **BERT for Anomaly Detection**

We need Embeddings as logs need to be represented in a numerical fashion

25

## Slide 26

### **LogBERT**

FFNN: Single Layer

Anomaly Criteria Correct token is not in top- **_g_** predicted tokens More than **_t_** _%_ of the masked log-keys are wrong

26

## Slide 27

## **Solution**

**How can we solve these problems?**

## Slide 28

### **Explainability: Element-Level Prediction**

Sequence Level Predictions (LogBERT)

Element Level Predictions (VoBERT)

28

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Element-Level Prediction
4 \ \ 6 \ 6 \ >)
LOGA LOG B LOG C LOG D LOGE
e J J \ J J \ y
a i i i i ~
LOGA LOG B LOG B LOG B LOG B
X J Ww J J JW S
—— i a i a i a i a +)
LOGA LOGA LOGA LOGA LOGE
\ J J J J y,
Sequence Level Predictions
(LogBERT)
wee eww wee eee wee
LOG B LOG C LOG D LOGE
FF 7 ————~ * /——_, ‘
LOGB LOG . LOG B ‘Los .
L L a
‘Loe A LOG A LOGA LOGE
Ress ssa sess ee sean naan S
Element Level Predictions
(VoBERT)
28
```

## Slide 29

### **Explainability: Per Element Masking**

Ratio Masking O(1) (LogBERT)

Per Element Masking O(n) (VoBERT)

29

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Per Element Masking
Nn----------- eee Ne eee ee ee ee ee ee ee ee ee ee ee
LoGA| | LocB| (elena!) | Locp| | Loce|! } #Logkeys
Ratio Masking O(1) Per Element Masking
(LogBERT) O(n)
(VoBERT)
29
```

## Slide 30

### **Log-stability: How can we make it more robust?**

By making it Vocabulary-Free:

Model architecture cannot depend on vocabulary Embedding layer works with out-of-vocabulary log-keys

Novel pre-training task based on this key insight: No need to actually reconstruct the whole sequence, **we just need to know how close the model was**

30

## Slide 31

### **Log-stability: Vocabulary-Free MLM**

Architecture requirement: Compare embeddings directly

Embedding layer requirement: Semantic embedding layer

31

## Slide 32

### **Real-world data: meet the security detection framework**

*

*ACCEPTED Roelofs et. al. Finding Harmony in the Noise: Blending Security Alerts for Attack Detection, **39**<sup>**th**</sup> **ACM/SIGAAP Symposium on Applied Computing 2024**

32

## Slide 33

## **Results**

**How did we do?**

## Slide 34

### **Evaluation Log Data**

- 3 most frequently used High Performance Computing (HPC) log datasets Hadoop Distributed File System (HDFS) BlueGene/L Supercomputer System (BGL) Thunderbird (TBird)

#### ING alert dataset

|ING|
|---|

34

## Slide 35

### **Data Instability**

Proxy: Percentage of unseen log-keys in the normal test set

Data redistribution algorithm Reshuffle train-test split Train and test size remain fixed

Normal Anomalous

Train set Test set

35

## Slide 36

### **Increasing Data Instability (BGL Dataset)**

Original split: Normal sequences contain <5% unseen Anomalous sequences contain >80% unseen Few unseen log-keys in total

We increase the unseen percentage to >80%

Original Split

36

## Slide 37

### **Results Public Datasets**

37

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Results Public Datasets
MCC Score
Performance on Sequence Level | TBird
100 +
2074
—e— VoBERT
—e-— LogBERT
—e— Unseen Logkey Heuristic
T T T T
20 40 60 80 100
% of normal sequences containing at least one unseen element
MCC Score
Performance on Sequence Level | BGL
100
| —e— VoBERT
—e— LogBERT
30 | —e— Unseen Logkey Heuristic
\
60 4 \
e.
WS
p ——e, SN
40 4 ‘e.
e.
I ™
20 4 Ss
es
0 T T T T
0 20 40 60 80
% of normal sequences containing at least one unseen element
100
37
```

## Slide 38

### **Results using real-world data**

#### Simple heuristic did not work

- VoBERT had similar performance to LogBERT

- LogBERT performance was stable Why? The average percentage of unseen log-keys in the sequences did not increase

   - We will probably see this effect when using this metric instead

38

## Slide 39

### **Conclusion**

Using a transformer model allows us to **leverage sequential data** (keep the alert order)

Our solution is robust in **unstable log data** environments

**Explainability** : Element-level evaluation performance can provide extra insights, but at a significant computational cost

Use it to further investigate suspicious alerts/logs

- LogBERT’s performance that was not representative of a real-world situation Don’t blindly trust published research It is important to **evaluate on real-world data**

39

## Slide 40

**Visit us at Booth 436**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Visit us at Booth 436
do your thing
```

## Slide 41

# **Data set split**

41

Appendix

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Data set split
f )
Dataset
\ y,
(- Y >
Normal Anomalous
Y MA y,
( ; Y~ >
Train aI Test rest | Dev
Dev
Y A y,
41
```

## Slide 42

# **Future Work: n-gram masking**

42

Appendix

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Future Work: n-gram masking
at
O
@
>
I-
Oo
)
W
= 'y
O
Q@)
@
I-
Oo
)
&
I-
Oo
Q@
m
New www wm mem em em em ee em ee ee eee ee ee ee ee ee ee ee ee ee ee ee ee ee
ee
# log keys
n
-
O
°)
>
_
e)
>)
OO
——
_
)
>)
O
Ld)
——
T_
1)
7)
1s)
LC
TT
fe)
)
Hi
42
```

## Slide 43

# **Data Instability: Case Study**

43

Appendix

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Data Instability: Case Study
Percentage of test sequences containing unseen logkeys | The bank Average percentage of unseen logkeys in a sequence | The bank
100 100
—e— Normal test sequences —e— Normal test sequences
—e— Abnormal test sequences —e— Abnormal test sequences
—e— Total test sequences —e— Total test sequences
80 5 go 4
a
F e
v 605 x 605
o 2
“ ” c
Hi — H
ES ° a 5 40,
& &
eo e
o ———e e o—"——_
. WA ey
° ° ° ~ : : °
o+—# T T T T T fe) r +, — r r t
vy) 1 2 3 4 5 ) 1 2 3 4 5
Data redistribution algorithm iterations Data redistribution algorithm iterations
```
