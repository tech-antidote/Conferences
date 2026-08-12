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
text_chars: 20251
ocr_pages: 10
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T23:03:44Z"
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
BRIEFINGS
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pie hat
EFINGS
AUGUST be 2025
MANDALAY BAY / LAS VEGAS
LLMDYara Method
#BHUSA @BlackHatEvents
```

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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pis hat
BRIEFINGS
Framework
Feature Extraction Feature Filter Feature Decision On LLM Rule Generation
{ ¢
String Feature setring': * (aAbAc) V(aAbAcAeAEAgAhAi)V
g": "unexpected heap error", * sya ha
g ‘e MP Statistical Features | east apap rant (eAEAgAhAG)V (eAEAQAHAAGAK)V (hAGASAK)
hibcéf jk
"t+password: %s": "natural_lan e" t, nn, ea 94
. . —— " i ; athe sanguage a “stringt: "Sunday", vA file-1 xxxxxxxx
Benign Files sllauncher.exe":"filename_with_ext Top Common Strings Security Domain Features "tag": "nlp-date" Top-N Strings vd file-2 xx xX
in Benign Db 3 file-3 x x x \
i { file-4 x xx xx
Function Feature Lorteame areal (ROCCE ing": "HeapDestroy", / file-5 x xx xx xx Double
; : "iat_function" file-6 x x x Cluster
LO BOOL sub_402320()
{ abcefghijk
HKEY phkResult ; ile-
Ld BYTE SubKey[257]; Oo Cluster-1 ») file 3 xx x
n memset (&SubKey[1], @, 0x100u); tag: xor_dynamic_decrypt file-6 * x x
. /\ strepy(subkey, asystencurrente. 8) Third-Party Library e 3F 30 11 FF 45 77 C3 8B 45 fia xen * x * . *
e Similiar return RegOpenkeyExA(HKEY_LOCAL_MACHINE, Finger Hash file-5 XXXXXKX
SubKey, @, OxF@@3Fu, &phkResult) == 0;
juer —> ‘e-
e q y 3 Cluster-2 ») file-2 xx XX
tag: shellcode_loader J subset
a I ISSN NV C6 45 2? 52 C6 45 ?? 4E C6 -~\We- compression &
, 2
/ ee 8, y push call ... pop ret { 0 Ne S B o\ B . intersection
So Ss ! .
\ \ mergin
A> ae? Capa Sensitive (“ ctuster-3 >) \ \ / , ons
\ @8, hash| | sSDeep Function Rules Coo. LLU OL Va
Suen 8B 0B 8B 73 2? 03 75 2? 8B . s As
\ Ne J (aAbAc)V(eA£AgAhAA) V(hALAJAK)
DMAHash Feature a — eee eeee
Malicious Files => Ao , >) Rule Scoring Mechanism
header | .text | .rdata| .rsrc | overlay | —-> [e) ee. Cluster-n 1 |
e ° tag: add_autorun_reg , 1. opcode feature xM |
Top Conmon DNAHash 8B 4C 24 2? 8D 44 24 27 68 80 | 2. dna hash feature = xw |
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

```
map pseudocode to
asmdata
loose mode:
wildcard immediate value
loose/normal mode:
wildcard displacement
```

```
Tag: xor_dynamic_decrypt
Detail: Performing XOR operations on each byte
using a dynamically generated key
Features: [{ "start": 19, "size": 7, "comment":
"This code segment contains the core logic of
XOR decryption, including dynamic key generation
and XOR operations" }]
```

#BHUSA @BlackHatEvents

## Slide 17

## Feature Decision base on LLM

Function behavior tagging

#### **how to generate high-quality training data?**

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pis hat
BRIEFINGS
Feature Decision base on LLM
Function behavior tagging
how to generate high-quality training data?
capability
mbc objectives
[ ATT&CK Tactic
behavior tag summary
G3 >
cloud sandbox
function behavior tags
( data generation
=
Lo
behavior tag list (5
of each sample
NY Vv ¥v
N75 qwen3-32b
NY
prompt
rebound_shell
shellcode_loader
tagging rules
steal_leak_xdata
xor_dynamic_decrypt
(th
capa sandbox
> < <
judge rules
oe w Ne
dynamic
(sa mple filter
analysis
Cb?
cloud sandbox
CS
ae |
CS
CJ
N °
static
analysis
1
capa sandbox => 2
capability
namespace
download and write a
file
communication/c2/
file-transfer
create reverse shell
create reverse shell
3
q
a
check for debugger
via API
‘anti-analysis/anti-debugging/
debugger-detection
capture screenshot via
keybd event
collection/screenshot
| >
Lo
function behavior tags =
”
Yes
<fes target tags? >
=
No
[x drop
feature extraction
feature filter
v
note: just save functions
those function tags in the
behavior tag list of this
sample.
\
samples | behavior tag list
rebound. shel,
sample1 network_connect_
sample2 runtime_anti_debug
sample3_ | remote_thread_inject
function tags
No
```

## Slide 18

## Rule Generation

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pifeK hat
BRIEFINGS
file_index fea
68 00 01 00
20 00 c3 6a 00
type file_index
+ opcode rl
feature
SYSTEM\\CurrentControlset\\Services\\Lanmans...
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
00000000,
4b458bfe,
4b458bfe,
11c6d9d3,
11c6d9d3,
13677351,
13677351,
WriteProcessMemory
192.168.1.2
192. 168.1.244
Welcome to use storm ddos
WriteProcessMemory
= opcode
+ opcode
iat_function
ip
ip
natural_language-blacklisted
iat_function
@64b1b9d,
064b1b9d,
064b169d,
3d38abdd,
3d38abdd,
3d38abdd,
1ea207dT
1ea207df
1ea207df
7c82cfcd,
7c82cfcd,
7c82cfcd,
5014fec5,
5014fec5,
5014fec5,
£4d72143,
£4d72143,
£4d72143,
11c6d9d3,
11c6d9d3,
11c6d9d3,
#5590595,
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
7c82cfcd,
5014fec5,
5014fec5.
00000000,
00000000,
£4d72143,
£4d72143.
8270912,
82770912,
11c6d9d3,
11¢6d9d3,
11c6d9d3,
11c6d9d3,
119836c9,
bf6édbdas,
d74e84/c,
d74e847c,
bce2bd73
bce2bd7?
78e0066f
78e0066f
http: //www.microsoft.com/PKI/docs/CPS/defat url
+ opcode
pean SOFTWARE\\Microsoft\\Active Setup\\Install natural_language-blacklisted
CreateRemoteThread iat_function
192.168.1. ip
Storm ddos Server natural_language-blacklisted
iexplore. exe filename_with_ext
+ opcode
+ opcode
+ opcode
wuseeaw
,- Hierarchical Cluster on DNAHaSh-—ig
opcode features string features
es go
Rule Scoring Mechanism @64b1b9d, 3d38abdd, 7c82cfcd, 5014fec5, £4d72143, 11c6d9d3, *, *
I
|
!
i file_Index, dna_hash_features !
|
!
\
4 I
! f
i}
| 1. opcode feature XM
. |! 2. dna hash feature XN | 1,5 Ha_@,*,Ha_2,...,Ha_6,*,...
ports Double Cluster on file and feature ----- . | 3. string feature x1 2,3.4, *,Hb_1,...,Hb_5,Hb_6,*,...
\
| i \
1 [ file_Index, opcode_features ‘ j hj '
file_Index, string_features | , ! \
1 =
; 1,2,3,4,5, op_1, op_2 1,4,5, ul_1,ul_2 i ie See \ = "CreateFontA" ascii wide
\ 1,4,5, op_3 ~ a ' a ' V5!kncHaP_E" ascii wide
2,3,4,5. u2_1,u2_2 | ° -
4 2,3,4,5, op_4 ia a : 1 threshold ? VENT_SINK_GetIDsOfNames" ascii wide
\ Z ’ 1 etFileVersionInfoA" ascii wide
N--------p------------- ----- - - - - ee ee ee a [ne een arma) Come ee MSVBVM60.DLL" ascii wide
5 _- Rule Compress And Generation ___________}_---
Ya of ($p*) and dnahash.match_pos(@, 0x21393263) and dnahash.match_pos(3, @xf6a76223) and dnahash.match_pos(4, @x296ff62e)
subset compression intersection rule merging
strings:
1,2,3,4 er A $p1 = {8B45?77BE7C4400000FBE040299F7FEB86410400080EA3F3011FF45??C38B45?76A0599} // sub_401000,xor_dynamic_decrypt
12,3,
— 1,2,3,4,6,7 — eine Bi 77 L -- B2 (A & B1)* (A & B2) $p2 = {8BCA83E103F3AAEB??6A046800100000508B43? 70345? ?50FF55??78B0B8B73? 70375? ?8BD18BF8C1E9@2F3A5} // sub_4590B4, shellcode_loader
Moy / Dar » , ee PY y \ $p3 = {C6457752C645?74EC645?7?45C645??74CC645?733C6457732} // sub_458E9A, shellcode_Loader
i>! f \ ; $p4 nstall.exe" fullword ascii wide
Ay UE 1 \ ! !
SS el Se 7 oN / x Voy + — >A & (B1* B2) $p5 = "MSVCRT_HEAP_SELECT" fullword ascii wide
ae 4 Me -7% Sieve Seas OY
\ condition:
all of ($px*)
```

## Slide 19

# Results

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pie hat
EFINGS
AUGUST be 2025
MANDALAY BAY / LAS VEGAS
#BHUSA @BlackHatEvents
```

## Slide 20

### Rule Generation Result of Recently Active Malware

• Families from VirusShare, VirusSign and malwarebazaar

Total Families: 151 Samples in Train Set: 17,435 Samples in Test Samples: 58,156 Total Samples: 75,591

#BHUSA @BlackHatEvents

## Slide 21

### Rule Generation Result of Recently Active Malware

- False positive info On  2.3 million benign samples

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pis hat
BRIEFINGS
Rule Generation Result of Recently Active Malware
¢ False positive info On 2.3 million benign samples
yargen Top 10 False Positive Rules
win32_Agent.NFD
Win32_Delf_NAY
Win32_Spy_CardSpy_NAF
Win32_AutoRun_VB_8WD
win32_Agent_OAT
win32_Flyagent_NGX
‘Win32_AutoRun_Deif_ RO
Win32_Agent_ADMM
win32_Agent, SNx
win32_Agent_ AAEF 11157
y y
iy Ss
Ss gs
* ©
9
ss
s
e &
ss
Number of False Positives
Ilmdyara Top 10 False Positive Rules
win32_Urelas_AB
\Win32_TtojanDownloader_ModiLoader_8
Win32_TrojanDownloader_Small_ PRL
\win64_Kryptik_FAZ
win32_Allaple Gen
win32_Kryptik HMRV
Unux_Miral_A
‘win32_Spy_CardSpy_NAF
9
s
s
ss s s
Number of False Positives
Win32_Agent_NFD.
win32_Pacex_Gen
win32_Delt_BFX
Win64_Agent_ABU
‘win32_Kryptik_AUY
\Win32_TrojanDropper_Gepys_AA
‘win32_Genkryptik_CYBX
Un Lox)
\Win32_TrojanDropper_Agent_SGF
500000
400000
300000
Total Count
200000
100000
autoyara Top 10 False Positive Rules
64039
158!
° ‘y y Ss S 9 9 y Y
se Fs SF Ss Fs SF
s é gs s ¥ as g
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
v1)
121289
73528
(7)
4977
4028
(1)
3204
229
2007
1557
1)
v7)
516014
Yargen_Gen
167600
150998
279344
121291
73560
)
5075
4027
1)
3786
6075
2005
2186
v)
1)
820317
```

## Slide 22

### Rule Generation Result of Recently Active Malware

• **Rule Details**

Yargen

##### AutoYara

LLMDYara

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pifex hat
BRIEFINGS
Rule Generation Result of Recently Active Malware
Rule Details
eR EHEAWIN32_Oberal_A_LeeR ERK
sig: 8a 06 46 32 45 ?? 50 56 ff 45 ?? 8b 75 ?? 8a 06 46 8b 5d ?? 39 5d 7?
75 2? 8b 55 ?? 89 55 ?? 8b 75 ?? 8a 06
"1A2466363E2F7236296D0CQA1E4353060D54373E074EQQ0AS7347C2D100652080B15244501160E080B151B4FOEQ00D49
"1A2466363E2F7236296D0CQA1E4353060D54373E074EQQ0AS7347C2D100652080B15244501160E080B151B4FOEQ0QD49
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
}
FP est: -@.@ Entropy: 2.5 Found in 317 files
} //This might be a string? Looks like:53D0A53
FP est: -@.@ Entropy: 3.@ Found in 316 files
FP est: -@.@ Entropy: 3.0 Found in 319 files
} //This might be a string? Looks Like:nMutexA
FP est: -@.@ Entropy: 3.@ Found in 317 files
}
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
$op2
$op3 //Input TP Rate:
$op4 /1316/320
$ops strings:
$op6 //Benign FP est: -@.@ Malicious
$op7 $x® = { OC FF 75 08 E8 73 03 00
$op8 //Benign FP est: -@.@ Malicious
$op9 $x1 = { 35 00 33 44 30 41 35 33
$op10 //Benign FP est: -0.@ Malicious
opi $x2 = "206915E4" ascii
$opi2 //Benign FP est: -@.@ Malicious
$op113 $x3 = { GE 4D 75 74 65 78 41 00
$op14 //Benign FP est: -0.0 Malicious
pon $x4 = { 35 97 64 40 00 E8 1A 05
$op16 //Benign FP est: -@.@ Malicious
ae $x5 = { 30 35 00 31 41 32 34 36
Op. //Benign FP est: -@.@ Malicious
Gams $x6 = { 20 40 00 55 8B EC 56 8B
. ae //Benign FP est: -@.@ Malicious
| Sa
$x7 = "9EB3QF16" ascii
condition:
FP est: -@.@ Entropy: 3.0 Found in 317 files
(8 of ($xO,$x1,$x2,$x3,$x4,$x5,$x6,$x7) )
black_samples_cnt = "320
strings: 5
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
"GetModuleFileName, ’*
"GetSystemDirector, ,,
"GetWindowsDirecto ;,
"Process32First" a) /x
"Process32Next" as: /*
"RegCreateKeyA" a /*
"RegOpenKeyExA" a is
"RegSetValueExA" |: /,,
"comment": "Core operation for XOR encryption/decryption"
7)
a5)
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
{8A06463245??75056FF45??78B75? ?78AQ6468B5D? ?395D??75?78B55? 789557?
do
LOBYTE(result) = v10 * *v6;
v9 = result;
v8 = x++v11;
if ( v11 == &a3[a4] )
4
v11 = a3;
v8 = *a3;
}
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pis hat
BRIEFINGS
Rule Generation Result of Malware from AutoYara
¢ False positive info On 2.3 million benign samples
yargen Top 10 False Positive Rules autoyara Top 10 False Positive Rules
a — volar sens
exch .2879 356151
xosn dns er ares olympicdestroyer 354 311477
pong p30 -ponispyware rossi sekur 217651 )
rere 8 sorsvne seozs xpantispywar 183451 @
darkvnc 38624 10
dragonmess 116
darkvne 0 baofa 3265
butt nezchi 7)
olympicdestroyer 4354
suproate baofa 3265
subroate 4296
™ subroate
° 2S ws) ) 2 £ £ ° 2S 2 ws) 2 £ ws) ws)
s s ss s s s s s s SS Ss Ss s potukorp
s sf Ss se se Ss s Sy SF s se Ss S
s 9 s *< s s ¥ s + s s
Number of False Positives Number of False Positives zcash
lImdyara Top 10 False Positive Rules Total False Positives by Tools
— ee plurox
800000 :
subroat
700000 . -
jongiti
600000
dragonmess
+ 500000 ee
3 wininf
8 400000 355,274 bkff
300000
200000
100000
25 355274
°
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pie hat
EFINGS
AUGUST be 2025
MANDALAY BAY / LAS VEGAS
#BHUSA @BlackHatEvents
```
