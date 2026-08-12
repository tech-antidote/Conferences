---
title: "LLMDYara LLMs-Driven Automated YARA Rules Generation with Explainable File Features and DNAHash"
speakers: ["Xiaochen Wang", "Yiping Liu", "Xiaoman Wang", "Cong Cheng"]
conference: "Black Hat"
conference_full: "Black Hat USA 2025"
edition: "USA"
year: 2025
source_pdf: "BlackHat_USA_2025_Slides/Xiaochen Wang&Yiping Liu&Xiaoman Wang&Cong Cheng_LLMDYara LLMs-Driven Automated YARA Rules Generation with Explainable File Features and DNAHash.pdf"
pages: 27
sha256: "7106807c7f243da907555cbbd51202615997c98d1da8c004d28337e280580dc6"
text_chars: 15896
ocr_pages: 7
has_ocr: true
redacted_secrets: 0
ocr_confidence: 85.9
ocr_unreliable_blocks: 4
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T05:25:57Z"
---
# LLMDYara LLMs-Driven Automated YARA Rules Generation with Explainable File Features and DNAHash

**Speakers:** Xiaochen Wang, Yiping Liu, Xiaoman Wang, Cong Cheng  
**Conference:** Black Hat USA 2025  
**Source:** `BlackHat_USA_2025_Slides/Xiaochen Wang&Yiping Liu&Xiaoman Wang&Cong Cheng_LLMDYara LLMs-Driven Automated YARA Rules Generation with Explainable File Features and DNAHash.pdf` (27 pages)


## Slide 1

LLMDYara: LLMs-Driven Automated YARA Rules Generation with Explainable File Features and DNAHash

Xiaochen Wang, Yiping Liu, Xiaoman Wang, Cong Cheng

#BHUSA @BlackHatEvents

## Slide 2

# Team

##### Xiaochen Wang

Xiaochen is a security engineer with extensive expertise in reverse engineering and malware detection. At Alibaba Cloud, she currently focuses on static malware detection and the design and development of antivirus engine.

Yiping Liu

Yiping is a security engineer with a keen interest in reverse engineering, malware analysis, and related domains. Currently, she is focused on research in reverse engineering and binary malware detection at Alibaba Cloud.

Xiaoman Wang

Xiaoman Wang is a Senior Security Engineer at Alibaba Cloud Security Center. He was a core member of the CTF team "Never Stop Exploiting," Currently, he focuses on advanced malware analysis and building next-generation threat detection systems.

Cong Cheng

Cong Cheng is a Senior Security Engineer at Alibaba Cloud, interested in malware analysis, windows internals, and virtualization security.

## Slide 3

## Rising Malware Threats

## Inefficient Manual Operations

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 92/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Rising Malware Threats
2,800,000
2,400,000
2,000,000
1,600,000
1,200,000
800,000
total malware families
400,000
0
— total malware families
WW total malware
i
2023-Q1 2023-Q2 2023-Q3 2023-Q4 2024-Q1 2024-Q2 2024-Q3 2024-Q4 2025-Q1 2025-Q2 2025-Q3
The trend of malware from 2023 to 2025
Inefficient Manual Operations
300,000,000
250,000,000
200,000,000
150,000,000
100,000,000
50,000,000
0
total malware
```

## Slide 4

## Automated YARA Rules Generation

###### NeuroYara

###### YARA

An industry standard regular expression tool designed for malware analysis.

VxSig

Uses a least-common-subsequence (LCS) algorithm to find byte sequences, extracted from functions, that appear to be common to all files in the given sample.

Propose a novel architecture utilizing two learning to rank neural networks to understand the underlying effectiveness and correlations among n- grams extracted for rule construction. This approach provides better flexibility and coverage of possible n-grams while reducing the required storage size from several GBs to only 10MBs.

2013

2014

2019

2020

2024

Use a Naïve Bayes model to score the potential utility of features that can be extracted from a binary, predominately strings.

YarGen

Leverage work in finding frequent larger n- grams, for n(8-1024), to find several candidate byte strings that could become features. Then it extend the SpectralCoClustering algorithm to work when the number of biclusters is not known a priori.

AutoYara

#BHUSA @BlackHatEvents

## Slide 5

## Challenge

1. How to reduce false positives and improve rule quality?

2. How to enhance the interpretability of selected features?

3. How to unlock the potential of LLM on our task?

#BHUSA @BlackHatEvents

## Slide 6

# LLMDYara Method

#BHUSA @BlackHatEvents

## Slide 7

## LLMDYara Method

**Break down the task for Automated YARA Rules Generation**

Step 1. What features need to be extracted?

Feature Extraction

Step 2. How to filter out features with false positives?

Feature Filter

Step 3. How to evaluate the selected features?

Feature Decision by LLM

Step 4. Which features should be selected to generate rules?

Rule Generation

#BHUSA @BlackHatEvents

## Slide 8

## Framework

###### Feature Extraction

Feature Filter

Feature Decision On LLM

Rule Generation

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 75/100 on the text kept, 64/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Framework
Feature Extraction Feature Filter Feature Decision On LLM Rule Generation
Benign Files sllauncher.exe":"filename_with_ext Top Common Strings Security Domain Features "tag": "nlp-date" Top-N Strings vd file-2 xx xX
in Benign Db 3 file-3 x x x \
; : "iat_function" file-6 x x x Cluster
LO BOOL sub_402320()
{ abcefghijk
HKEY phkResult ; ile-
Ld BYTE SubKey[257]; Oo Cluster-1 ») file 3 xx x
n memset (&SubKey[1], @, 0x100u); tag: xor_dynamic_decrypt file-6 * x x
e Similiar return RegOpenkeyExA(HKEY_LOCAL_MACHINE, Finger Hash file-5 XXXXXKX
SubKey, @, OxF@@3Fu, &phkResult) == 0;
tag: shellcode_loader J subset
, 2
Malicious Files => Ao , >) Rule Scoring Mechanism
header | .text | .rdata| .rsrc | overlay | —-> [e) ee. Cluster-n 1 |
e ° tag: add_autorun_reg , 1. opcode feature xM |
H1] }H2]) ... |Hn in Benign Db ~~~ Vector Space —> 7 N 3. string feature x1 |
```

## Slide 9

## Feature Extraction: String Features

String features are widely used features,

**How to define and extract high-quality strings?**

17 types of IOC-related strings

Natural language strings

#BHUSA @BlackHatEvents

## Slide 10

Feature Extraction: Function Features Besides string features, **What other features can be extracted?**

###### decompiled code with line numbers and offsets

If decompile fails, extract asm code

###### Function Call Graph

#BHUSA @BlackHatEvents

## Slide 11

Feature Extraction: File DNAHash Features If string and function-based features are not usable,

#### **what alternative features can be used while controlling false positives?**

1. Self-Modifying Code
2. Control Flow Obfuscation

3. Self-Implemented Packers

string features are encrypted function features decompiled failed or became hard to understand

#BHUSA @BlackHatEvents

## Slide 12

## Feature Filter: string feature filter

There are too many natural language strings,

To reduce false positives in string features,

**Deep filtering of natural language strings**

**Filter based on white samples**

We further classify the strings of type natural_language into more specific subtypes such as compiler, sensitive_api … …

#BHUSA @BlackHatEvents

## Slide 13

Feature Filter: function feature filter If there are so many functions in malware,

**How to decide which functions are more valuable?** System API or third-party library functions

      - Self-built Third-Party Library Function Signature Database

- IDA built-in ability

   - idc.FUNC_LIB

   - idc.AF_FLIRT

   - idc.FUNC_CHUNK

before after

- function name in import functions

#BHUSA @BlackHatEvents

## Slide 14

## Feature Filter: function feature filter

The entrance related functions

Sensitive API or crypto related functions

Use <u>CAPA</u> to identify sensitive functions

Weight the importance with: function size, number of referenced strings and number of reference.

#BHUSA @BlackHatEvents

## Slide 15

## Feature Decision base on LLM

##### String Feature Selection

#### **how to fine-tune the LLM?**

1. invalid output format

2. unexpected string selection

#BHUSA @BlackHatEvents

## Slide 16

## Feature Decision base on LLM **What kind of function opcode sequence is suitable to be part of a YARA rule?**

\```
map pseudocode to
asmdata
loose mode:
wildcard immediate value
loose/normal mode:
wildcard displacement
\```

\```
Tag: xor_dynamic_decrypt
Detail: Performing XOR operations on each byte
using a dynamically generated key
Features: [{ "start": 19, "size": 7, "comment":
"This code segment contains the core logic of
XOR decryption, including dynamic key generation
and XOR operations" }]
\```

#BHUSA @BlackHatEvents

## Slide 17

## Feature Decision base on LLM

Function behavior tagging

#### **how to generate high-quality training data?**

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 91/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Feature Decision base on LLM
Function behavior tagging
how to generate high-quality training data?
capability
mbc objectives
[ ATT&CK Tactic
behavior tag summary
cloud sandbox
function behavior tags
( data generation
=
Lo
behavior tag list (5
of each sample
prompt
rebound_shell
shellcode_loader
tagging rules
steal_leak_xdata
capa sandbox
judge rules
dynamic
(sa mple filter
analysis
cloud sandbox
ae |
N °
static
analysis
1
capa sandbox => 2
capability
namespace
download and write a
file
file-transfer
create reverse shell
create reverse shell
3
q
check for debugger
via API
debugger-detection
capture screenshot via
keybd event
collection/screenshot
function behavior tags =
Yes
<fes target tags? >
=
No
[x drop
feature extraction
feature filter
note: just save functions
those function tags in the
behavior tag list of this
sample.
samples | behavior tag list
sample2 runtime_anti_debug
function tags
No
```

## Slide 18

## Rule Generation

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 81/100 on the text kept, 67/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
file_index fea
type file_index
feature
Welcome to use storm ddos
type
natural_language-blacklisted
natural_language-blacklisted
2b05557d
2b@5557d
4b458bfe,
4b458bfe,
3d38abdd,
3d38abdd,
7c82cfcd,
7c82cfcd,
00000000,
4b458bfe,
4b458bfe,
11c6d9d3,
11c6d9d3,
13677351,
13677351,
WriteProcessMemory
192.168.1.2
Welcome to use storm ddos
WriteProcessMemory
= opcode
+ opcode
iat_function
ip
ip
natural_language-blacklisted
iat_function
064b169d,
3d38abdd,
3d38abdd,
3d38abdd,
1ea207df
1ea207df
7c82cfcd,
7c82cfcd,
7c82cfcd,
5014fec5,
5014fec5,
5014fec5,
£4d72143,
5ace954d,
02858942,
064b1b9d,
264b1b9d,
82770912,
827f0912,
3d38abdd,
3d38abdd,
3d38abdd,
3d38abdd,
7c82cfcd,
7c82cfcd,
7c82cfcd,
5014fec5,
00000000,
00000000,
8270912,
11c6d9d3,
11c6d9d3,
11c6d9d3,
119836c9,
d74e847c,
bce2bd73
78e0066f
+ opcode
pean SOFTWARE\\Microsoft\\Active Setup\\Install natural_language-blacklisted
CreateRemoteThread iat_function
192.168.1. ip
Storm ddos Server natural_language-blacklisted
+ opcode
+ opcode
+ opcode
,- Hierarchical Cluster on DNAHaSh-—ig
opcode features string features
Rule Scoring Mechanism @64b1b9d, 3d38abdd, 7c82cfcd, 5014fec5, £4d72143, 11c6d9d3, *, *
|
\
| 1. opcode feature XM
. |! 2. dna hash feature XN | 1,5 Ha_@,*,Ha_2,...,Ha_6,*,...
ports Double Cluster on file and feature ----- . | 3. string feature x1 2,3.4, *,Hb_1,...,Hb_5,Hb_6,*,...
\
file_Index, string_features | , ! \
1 =
; 1,2,3,4,5, op_1, op_2 1,4,5, ul_1,ul_2 i ie See \ = "CreateFontA" ascii wide
4 2,3,4,5, op_4 ia a : 1 threshold ? VENT_SINK_GetIDsOfNames" ascii wide
5 _- Rule Compress And Generation ___________}_---
Ya of ($p*) and dnahash.match_pos(@, 0x21393263) and dnahash.match_pos(3, @xf6a76223) and dnahash.match_pos(4, @x296ff62e)
subset compression intersection rule merging
strings:
1,2,3,4 er A $p1 = {8B45?77BE7C4400000FBE040299F7FEB86410400080EA3F3011FF45??C38B45?76A0599} // sub_401000,xor_dynamic_decrypt
12,3,
i>! f \ ; $p4 nstall.exe" fullword ascii wide
\ condition:
all of ($px*)
```

## Slide 19

# Results

#BHUSA @BlackHatEvents

## Slide 20

### Rule Generation Result of Recently Active Malware

• Families from VirusShare, VirusSign and malwarebazaar

Total Families: 151 Samples in Train Set: 17,435 Samples in Test Samples: 58,156 Total Samples: 75,591

#BHUSA @BlackHatEvents

## Slide 21

### Rule Generation Result of Recently Active Malware

- False positive info On  2.3 million benign samples

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 90/100 on the text kept, 70/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Rule Generation Result of Recently Active Malware
¢ False positive info On 2.3 million benign samples
yargen Top 10 False Positive Rules
Win32_Delf_NAY
Win32_Spy_CardSpy_NAF
win32_Agent_OAT
Win32_Agent_ADMM
9
ss
Number of False Positives
Ilmdyara Top 10 False Positive Rules
win32_Urelas_AB
win32_Allaple Gen
Unux_Miral_A
9
Number of False Positives
win32_Pacex_Gen
Un Lox)
500000
400000
300000
Total Count
200000
100000
autoyara Top 10 False Positive Rules
64039
158!
Number of False Positives
Total False Positives by Tools
316,014
229,996
15,333
yargen autoyara limdyara
Tool Name
Win32_Agent_NFD
Win32_Delf_NAY
Win32_Agent_NLP
Win32_Spy_CardSpy_NAF
Win32_AutoRun_VB_BWD
Win32_Pacex_Gen
Win32_Agent_OAT
Win32_Flyagent_NGX
Win32_Urelas_AB
Win32_AutoRun_Delf_RO
Win32_VBClone_E
Win32_Agent_ADMM
Win32_Agent_SNX
Win32_Delf_BFX
Win32_TrojanDownloader_ModiL.
Win32_Agent_AAEF
Win32_Filecoder_Trigona_A
Win64_Agent_ABU
Win32_Kryptik_AUY
Win32_TrojanDownloader_Small..
Total
AutoYARA
229996
Yargen
167035
135181
121289
73528
4977
4028
3204
229
2007
1557
516014
Yargen_Gen
167600
150998
279344
121291
73560
5075
4027
3786
6075
2005
2186
820317
```

## Slide 22

### Rule Generation Result of Recently Active Malware

• **Rule Details**

Yargen

##### AutoYara

LLMDYara

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 86/100 on the text kept, 84/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Rule Generation Result of Recently Active Malware
Rule Details
"1919490C1D4E73031A4F090C1E2C67696B206B690E868665A09A616E6574206D296530207BFFB96705" ascii
tags:
rule Rule_Win32_Oberal_A_1
{
['xor_dynamic_decrypt']
Ulm_detail: This function implements XOR encryption/decryption operations,
performing byte-by—byte XOR on the data for encryption or decryption. This is
a common method used in dynamic decryption.
meta: feat:
cover_family = "Win32_Obi ¢
family_sample_cnt = "320
Yargen
"Q5044303053D451000520C1D156D551D034F19001A5937104234591D11114D6D656172207365676765" ascii
AutoYara
FP est: -@.@ Entropy: 3.0 Found in 318 files
FP est: -@.@ Entropy: 2.5 Found in 317 files
} //This might be a string? Looks like:53D0A53
FP est: -@.@ Entropy: 3.@ Found in 316 files
FP est: -@.@ Entropy: 3.0 Found in 319 files
} //This might be a string? Looks Like:nMutexA
FP est: -@.@ Entropy: 3.@ Found in 317 files
FP est: -@.@ Entropy: 3.@ Found in 318 files
} //This might be a string? Looks Like:051A246
FP est: -@.@ Entropy: 2.75 Found in 318 files
} //This might be a string? Looks like: @UV
strings:
$s1 = "5345474745694B" ascii /* hex encoded string 'SEGGEiK' */
$s2 =
$s3 =
$s4 =
$s5 = "@5044303053D451" ascii
$s6 = "0520C1D156D551D034F19" ascii
$s7 = "QD4916067C20111C404F1B0E52373B1B4E6465204720E
$s8 = "652080B15244501160EQ80B151B4FQE" ascii
$s9 = "6520472QEE4QAA208D1EBD728QQEB967071A" ascii
$s10 =
$s11 = "1A5937104234591D11114D6D656172207365676765" ascii
$op0 = { 8b7c24088b4c240c03f833d20Fb6040a }
$op1 rule Win32_Oberal_A
$op3 //Input TP Rate:
$op4 /1316/320
$ops strings:
$op6 //Benign FP est: -@.@ Malicious
$op8 //Benign FP est: -@.@ Malicious
$op10 //Benign FP est: -0.@ Malicious
opi $x2 = "206915E4" ascii
$opi2 //Benign FP est: -@.@ Malicious
$op14 //Benign FP est: -0.0 Malicious
$op16 //Benign FP est: -@.@ Malicious
Op. //Benign FP est: -@.@ Malicious
. ae //Benign FP est: -@.@ Malicious
$x7 = "9EB3QF16" ascii
condition:
FP est: -@.@ Entropy: 3.0 Found in 317 files
(8 of ($xO,$x1,$x2,$x3,$x4,$x5,$x6,$x7) )
black_samples_cnt = "320
$p1 =
$p2 =
$p3 =
$p4 =
$p5 =
$p6 =
$p7 =
$p8 =
$p9 =
$p10
$p11 =
$p12 =
$p13 =
$p14 =
$p15 =
"CreateMutexA" asc /,
"CreateToolhelp32S
"GetLastError" asc /*
"GetWindowsDirecto ;,
"Process32First" a) /x
"Process32Next" as: /*
"RegCreateKeyA" a /*
"comment": "Core operation for XOR encryption/decryption"
16
17
18
19
20
21
22
23
* 24
25
func_content:
@x401d10
int a4)
"FindFirstFileA" a ---
@x401d67
@x401d39
@x401d3c
@x401d44
@x401d4d
@x401d52
@x401d58
@x401d5b
8B75??8A06} // xor_dynamic_decrypt
condition:
all of ($px)
*/ _BYTE *__stdcall sub_401D10(_BYTE x*a1, int a2, _BYTE xa3,
*/
*/
*/
*/
*/
*/
*/
*/
*/
*/
*/
"SHGetSpecialFolderPathA" ascii wide
"ShellExecuteA" ascii wide
do
LOBYTE(result) = v10 * *v6;
v9 = result;
v8 = x++v11;
4
v11 = a3;
v10 = v8;
LLMDYara
```

## Slide 23

### Rule Generation Result of Malware from AutoYara

Total Families: 24 Samples in Train Set: 2,162 Samples in Test Samples: 230 Total Samples: 2,392

#BHUSA @BlackHatEvents

## Slide 24

### Rule Generation Result of Malware from AutoYara

- False positive info On  2.3 million benign samples

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 85/100 on the text kept, 65/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Rule Generation Result of Malware from AutoYara
¢ False positive info On 2.3 million benign samples
yargen Top 10 False Positive Rules autoyara Top 10 False Positive Rules
xosn dns er ares olympicdestroyer 354 311477
darkvnc 38624 10
dragonmess 116
olympicdestroyer 4354
suproate baofa 3265
subroate 4296
™ subroate
Number of False Positives Number of False Positives zcash
lImdyara Top 10 False Positive Rules Total False Positives by Tools
— ee plurox
800000 :
subroat
jongiti
600000
dragonmess
+ 500000 ee
3 wininf
8 400000 355,274 bkff
300000
200000
100000
yargen autoyara limdyara
Tool Name
Number of False Positives
```

## Slide 25

# Contact Us

If you have any question:

Xiaochen Wang     wangxiaochen.wxc@alibaba-inc.com

Yiping Liu               liuyiping.lyp@alibaba-inc.com

Alibaba Cloud Malicious File Detection Platform

<u>https://ti.aliyun.com/#/overview</u>

1. Binary / Webshell / Malicious Script Detection

2. Cloud Sandbox

## Slide 26

## Black Hat Sound Bytes

1. Automated Explainable Rule Generation Solution.

2. Binary Program Feature Engineering Experience.

3. Using LLM for Binary Program Analysis.

#BHUSA @BlackHatEvents

## Slide 27

# Q&A

#BHUSA @BlackHatEvents
