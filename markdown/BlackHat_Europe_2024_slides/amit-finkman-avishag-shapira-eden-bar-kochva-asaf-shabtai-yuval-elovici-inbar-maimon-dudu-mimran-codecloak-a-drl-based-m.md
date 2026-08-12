---
title: "CodeCloak A DRL-Based Method for Mitigating Code Leakage by LLM Code Assistants"
speakers: ["Amit Finkman", "Avishag Shapira", "Eden Bar Kochva", "Asaf Shabtai", "Yuval Elovici", "Inbar Maimon", "Dudu Mimran"]
conference: "Black Hat"
conference_full: "Black Hat Europe 2024"
edition: "Europe"
year: 2024
source_pdf: "BlackHat_Europe_2024_slides/Amit Finkman & Avishag Shapira & Eden Bar Kochva & Asaf Shabtai & Yuval Elovici & Inbar Maimon & Dudu Mimran_CodeCloak A DRL-Based Method for Mitigating Code Leakage by LLM Code Assistants.pdf"
pages: 97
sha256: "dfff59306a2bb24f39ccf7618f943beb2e5b4110c20c3874656a147fa60552cc"
text_chars: 32039
ocr_pages: 42
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T00:53:55Z"
---
# CodeCloak A DRL-Based Method for Mitigating Code Leakage by LLM Code Assistants

**Speakers:** Amit Finkman, Avishag Shapira, Eden Bar Kochva, Asaf Shabtai, Yuval Elovici, Inbar Maimon, Dudu Mimran  
**Conference:** Black Hat Europe 2024  
**Source:** `BlackHat_Europe_2024_slides/Amit Finkman & Avishag Shapira & Eden Bar Kochva & Asaf Shabtai & Yuval Elovici & Inbar Maimon & Dudu Mimran_CodeCloak A DRL-Based Method for Mitigating Code Leakage by LLM Code Assistants.pdf` (97 pages)


## Slide 1

###### CodeCloak: A DRL-Based Method for Mitigating Code Leakage by LLM Code Assistants

**Speaker: Amit Finkman**

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
~_EJRO! 3 | “I
DECEMBER 11-12, 2024 r BP / <S
IEFINGS | Z ——\ ee
cols A DRL-Based Method for-Mitigating Code Leakage
by LLM Code Assistants
Y
Speaker: Amit Finkman
```

## Slide 2

**https://arxiv.org/pdf/2404.09066**

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pisekhat
EUROPE 2024
CODECLOAK: A METHOD FOR MITIGATING CODE
LEAKAGE BY LLM CODE ASSISTANTS
Amit Finkman Noah”, Avishag Shapira’, Eden Bar Kochva’, Inbar Maimon, Dudu Mimran,
Yuval Elovici, Asaf Shabtai
Department of Software and Information Systems Engineering
Ben-Gurion University of The Negev
ABSTRACT
LLM-based code assistants are becoming increasingly popular among developers.
These tools help developers improve their coding efficiency and reduce errors by
providing real-time suggestions based on the developer’s codebase. While bene- e
ficial, the use of these tools can inadvertently expose the developer's proprietary https: //arxiv.org/pdf/2404.09066
code to the code assistant service provider during the development process. In this
work, we propose a method to mitigate the risk of code leakage when using LLM-
based code assistants. CodeCloak is a novel deep reinforcement learning agent
that manipulates the prompts before sending them to the code assistant service.
CodeCloak aims to achieve the following two contradictory goals: (1) minimizing
code leakage, while (11) preserving relevant and useful suggestions for the devel-
oper. Our evaluation, employing StarCoder and Code Llama, LLM-based code as-
sistants models, demonstrates CodeCloak’s effectiveness on a diverse set of code
repositories of varying sizes, as well as its transferability across different models.
We also designed a method for reconstructing the developer’s original codebase
from code segments sent to the code assistant service (i.e., prompts) during the
development process, to thoroughly analyze code leakage risks and evaluate the
effectiveness of CodeCloak under practical development scenarios.
Information Classification: General
```

## Slide 3

#### **About Myself and the Team**

**Amit Finkman**

**Eden Bar-Kochva**

**Avishag Shapira**

**Dudu Mimran**

**Inbar Maimon**

**Prof. Asaf Shabtai**

**Prof. Yuval Elovici**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 4

#### **Agenda**

#### **1. Intro**

#### **2. Background 3. Threat Model**

#### **4. Countermeasure 5. Takeaways 6. Future Steps 7. Q&A**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 5

#### **Agenda**

#### **1. Intro 2. Background 3. Threat Model 4. Countermeasure 5. Takeaways 6. Future Steps 7. Q&A**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 6

#### **Today’s AI code Assistants**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 7

#### **Today’s AI code Assistants**

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
blackhat = Today’s Al code Assistants
EUROPE 2024
Al<coder [Raa mcodium’ Ay Magic
ey Judini
4 Cursor ey mutable.ai
sith: BLACKBOX menbme CodePilot.ai Duet Al for Google Cloud
re) a) GitHub Q
bloop. Q> codesquiresi Gp Sonic 4 Sourcegraph
o™ ut j =- 1BM Watson Assistant RS |
a gicoeacy Ey Codiga | (© tabnine
```

## Slide 8

Information Classification: General

#BHEU @BlackHatEvents

## Slide 9

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
def bubble_sort(arr):
for i in range(len(arr)):
for j in range(len(arr) - i - 1):
if arr[j] > arr[j+1]:
arr(j], are[j+1] = arr[j+1], arr[j]
return arr
def merge_sort(arr):
if len(arr) < 2:
return arr
mid = len(arr) // 2
Left_arr = merge_sort(arr[:mid])
right_arr = merge_sort(arr[mid: ])
return merge(left_arr, right_arr)
a
quick_sort(arr):
lif Len(arr) < 2:
return arr
pivot = arr[@]
left_arr = [x for x in arr[1:] if x < pivot]
right_arr = [x for x in arr[i:] if x >= pivot]
return quick_sort(left_arr) + [pivot] + quick_sort(right_arr)
def merge(left_arr, right_arr):
result = []
while Len(left_arr) > 8 and Len(right_arr) > @:
if left_arr[6] < right_arr[e]:
```

## Slide 10

Already typed Developer is coding The suggestion of how to complete the code snippet

Information Classification: General

#BHEU @BlackHatEvents

## Slide 11

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
EUROPE 2024
Prompt ,
<———
Suggestion
Code Assistant
| Service |
```

## Slide 12

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
EUROPE 2024
| Developer |
Prompt ,
<———
IDE
Suggestion
Code Assistant
Service
```

## Slide 13

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
EUROPE 2024
Prompt a —
< —— inputNumber = inputNumber / 2;
. |
Suggestion
Code Assistant
| Service |
```

## Slide 14

#### **Agenda**

#### **1. Intro**

#### **2. Background 3. Threat Model**

#### **4. Countermeasure 5. Takeaways 6. Future Steps 7. Q&A**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 15

#### **Agenda**

#### **1. Intro 2. Background 3. Threat Model 4. Countermeasure 5. Takeaways 6. Future Steps 7. Q&A**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 16

#### **The Problem**

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pisekhat The Problem
EUROPE 2024
+) ; z ;
blackhat Leakage To the Service Providers black hat Attackers
Information Classification: General 1
```

## Slide 17

#### **Leakage To the Service Providers**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 18

#### **Leakage To the Service Providers**

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ARTIFICIAL INTELLIGENCE F 54. > . 3
— = — = +s >
FORTUNE so
Home News Tech Finance Leadership Well Recommends Fortune 500
TECH - APPLE
Apple clamps down on employees using ChatGPT as
more companies fear sensitive data sharing with A.I.
models
BY NICHOLAS GORDON
| ' LCpPULrieuw PiU Suiay, PULSE a BU WIE Hot OL COT police CACC HOU AUUUL SCHSIlive a —
tration by Alex Castye internal information being leaked through AI.
-
```

## Slide 19

#### **Leakage To the Service Providers**

**sent The code is written with the help of these platforms is being to the servers of external companies** **Potential Intellectual Property Violation!**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 20

#### **The Problem**

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pisekhat The Problem
EUROPE 2024
A , A
blackhat Leakage To the Service Providers blackhat Attackers
EUROPE 2024 EUROPE 2024
>. Ss
Information Classification: General 1
```

## Slide 21

#### **Attackers**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 22

#### **Threat Model**

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
blackhat Threat Model
EUROPE 2024
Coding Ach Prompt ek Prompt =3
> — > >
a « <
Suggestions Date Leakage Suggestions Code Assistant
Developer IDE Monitor Service
Reco nst-(4)
ructed
Code
Code Segments
@)
Data Evaluati
Preprocessing Reconstruction valuation |
Source Code |
Information Classification: General
```

## Slide 23

#### **Threat Model**

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
blackhat Threat Model
EUROPE 2024
Coding R= 5 Prompt Prompt =3
————> — > >
a < <
Suggestions Suggestions Code Assistant
Developer IDE Monitor Service
Code Segments
(2) oF Reco nst-(4)
S05 iS ructed
__Code
— ———_
Data Code
Preprocessing Reconstruction Evaluation |
Source Code |
Information Classification: General
```

## Slide 24

#### **Threat Model**

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
EUROPE 2024
Developer
Information Classification: General
Threat Model
<= E Prompt ek Prompt =3
al Sal
a < <
Suggestions |Date Leakage Suggestions Code Assistant
IDE Monitor Service
Reco nst-(4)
ructed
Code
Code Segments
Source Code |
Evaluation |
```

## Slide 25

#### **Threat Model**

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
blackhat Threat Model
EUROPE 2024
Coding Ach Prompt ek Prompt =3
> — > >
a « <
Suggestions Date Leakage Suggestions Code Assistant
Developer IDE Monitor Service |
) Reconst-(4 )
ructed
Code
Code Segments
@)
Data
Preprocessing
Source Code |
Evaluation |
Information Classification: General
```

## Slide 26

#### **Threat Model**

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
blackhat Threat Model
EUROPE 2024
Coding Ach Prompt ek Prompt =3
> — > >
a « <
Suggestions Date Leakage Suggestions Code Assistant
Developer IDE Monitor Service
Code Segments
(2) (3) Reconst-(4 )
a.
——
$< —
Data
Preprocessing Re pn
Source Code |
Evaluation |
Information Classification: General
```

## Slide 27

#### **Threat Model**

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
blackhat Threat Model
EUROPE 2024
Coding Ach Prompt ek Prompt =3
> — > >
a « <
Suggestions Date Leakage Suggestions Code Assistant
Developer IDE Monitor Service |
Code Segments
( ) (3) Aen Reconst-(4 )
: il
: Code
a
Data
Preprocessing Reconstruction
Source Code |
Information Classification: General
```

## Slide 28

#### **Threat Model**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 29

#### **Threat Model**

**From this Prompts that was Sent to the Service Provider We Succeed to Recover ~80% of the Source Codes!**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 30

#### **Threat Model**

## **The Solution: CodeCloak**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 31

#### **Agenda**

#### **1. Intro**

#### **2. Background 3. Threat Model**

#### **4. Countermeasure 5. Takeaways 6. Future Steps 7. Q&A**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 32

#### **Agenda**

#### **1. Intro 2. Background 3. Threat Model**

#### **4. Countermeasure 5. Takeaways 6. Future Steps 7. Q&A**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 33

#### **Mitigating Risks in AI-code assistants models**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 34

#### **Mitigating Risks in AI-code assistants models**

#### **1. Protecting Intellectual Property.**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 35

#### **Mitigating Risks in AI-code assistants models**

#### **1. Protecting Intellectual Property. 2. Protect Organizations.**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 36

#### **Mitigating Risks in AI-code assistants models**

#### **1. Protecting Intellectual Property. 2. Protect Organizations.**

#### **3. Strengthen AI code assistants models.**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 37

### **CodeCloak: Goal**

• **Reduce code leakage.** • **Preserve the AI code assistant productivity**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 38

### **CodeCloak: Example**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 39

### **Reinforcement Learning**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 40

### **Reinforcement Learning**

• **States: Where we are now.**

• **Actions: What we can do.** • **Rewards: Feedback for doing it right.**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 41

### **Reinforcement Learning (states)**

• **States: Where we are now.**

• **Actions: What we can do.**

• **Rewards: Feedback for doing it right.**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 42

### **Reinforcement Learning (actions)**

• **States: Where we are now.**

• **Actions: What we can do.**

• **Rewards: Feedback for doing it right.**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 43

### **Reinforcement Learning (rewards)**

• **States: Where we are now.**

• **Actions: What we can do.**

•

**Rewards: Feedback for doing it right.**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 44

### **Reinforcement Learning (rewards)**

+ 100

• **States: Where we are now.**

• **Actions: What we can do.**

• **Rewards: Feedback for doing it right.**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 45

### **From RL to DRL**

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
EUROPE 2024
Information Classification: General
From RL to DRL~
| Reward r
Action
a
Parameter @
Observation State S
Environment
```

## Slide 46

### **CodeCloak modeling**

States =

Actions =
, , , … ,

Rewards =

Information Classification: General

#BHEU @BlackHatEvents

## Slide 47

### **CodeCloak modeling - states**

###### **State**

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
blackhat CodeCloak modeling
EUROPE 2024
pip install opencv-python pyautogui numpy keyboard
import cv2
import numpy as np
import pyautogui
import keyboard
screen_size = pyautogui.size()
fps = 20
fource = cv2.VideoWriter_fourcc(*"XVID")
output_file = "screen_recording_clcoding.mp4"
out = cv2.VideoWriter(output_file, fourcc, fps,
(screen_size.width, screen_size.height))
print("Recording... Press 'q' to stop.")
while True:
screen = pyautogui.screenshot()
frame = np.array(screen)
frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
out .write(frame)
if keyboard.is_pressed('q'):
print("Recording stopped.")
break
out.release()
print(f"Video saved to {output_file}")
#source code --> clcoding.com
- states
pip install opencv-python pyautogui numpy keyboard
import cv2
import numpy as np
import pyautogui
import keyboard
screen_size = pyautogui.size()
fps = 20
fource = cv2.VideoWriter_fourcc(*"XVID")
fource = cv2.VideoWriter_fourcc(*"XVID")
output_file = "screen_recording clcoding.mp4"
out = cv2.VideoWriter(output_file, fourcc, fps,
(screen_size.width, screen_size.height))
print("Recording... Press 'q' to stop.")
while True:
screen = pyautogui.screenshot()
frame = np.array(screen)
frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
out .write(frame)
Information Classification: General
if keyboard.is_pressed('q'):
print("Recording stopped.")
break
out.release()
print(f"Video saved to {output_file}")
ro
L J
```

## Slide 48

### **CodeCloak modeling - actions**

#### **Examples:**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 49

### **CodeCloak modeling - actions**

**Examples:**

###### ▪ **Detect and replace personally identifiable information (PII)**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 50

### **CodeCloak modeling - actions**

**Examples:**

▪ **Detect and replace personally identifiable information (PII)**

▪ **Change/delete/insert random lines of code**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 51

### **CodeCloak modeling - actions**

**Examples:**

▪ **Detect and replace personally identifiable information (PII)**

▪ **Change/delete/insert random lines of code** ▪ **Delete function bodies and replace with summaries**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 52

### **CodeCloak modeling - actions**

**Examples:**

▪ **Detect and replace personally identifiable information (PII)**

▪ **Change/delete/insert random lines of code** ▪ **Delete function bodies and replace with summaries** ▪ **Rename variables, functions, arguments**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 53

### **CodeCloak modeling - actions**

**Examples:**

▪ **Detect and replace personally identifiable information (PII)**

▪ **Change/delete/insert random lines of code** ▪ **Delete function bodies and replace with summaries** ▪ **Rename variables, functions, arguments**

▪ **Stop manipulations and send the manipulated prompt**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 54

### **CodeCloak modeling - actions**

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
blackhat CodeCloak modeling “actions
EUROPE 2024
fource = cv2.VideoWriter_fourcc(*"XVID")
output_file = "screen_recording clcoding.mp4"
out = cv2.VideoWriter(output_file, fourcc, fps,
(screen_size.width, screen_size.height) )
print("Recording... Press ‘q' to stop.")
while True:
screen = pyautogui.screenshot()
frame = np.array(screen)
cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
out .write(frame)
frame
Information Classification: General
```

## Slide 55

### **CodeCloak modeling - actions**

**Prompt Manipulation: delete lines**

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
blackhat CodeCloak modeling “actions
EUROPE 2024
fource = cv2.VideoWriter_fourcc(*"XVID")
output_file = "screen_recording clcoding.mp4"
out = cv2.VideoWriter(output_file, fourcc, fps,
(screen_size.width, screen_size.height) )
print("Recording... Press ‘q' to stop.")
while True:
screen = pyautogui.screenshot()
frame = np.array(screen)
cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
out .write(frame)
frame
Information Classification: General
```

## Slide 56

### **CodeCloak modeling - actions**

**Prompt Manipulation: delete lines**

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
blackhat CodeCloak modeling ‘actions
EUROPE 2024
s _ . ‘tt =—s
TUUPrCO = CVe. VIUCUNT ILS Treurece|, AViv 7
au
output_file = "screen_recording_clcoding.mp4
Otters ttteertttestortprt tite —_forrees tes;
print("Recording... Press ‘q' to stop.")
while True:
screen = pyautogui.screenshot()
frame = np.array(screen)
< ; s —_-P =.
Trame ="CV2.CVcCULU (ir ame, CVeeCULUN mMubeDuUN,
out .write(frame)
Information Classification: General
```

## Slide 57

### **CodeCloak modeling - actions**

**Prompt Manipulation: delete lines**

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
blackhat CodeCloak modeling - actions
EUROPE 2024
output file =
( )
while True:
screen = pyautogui.screenshot()
frame = np.array(screen)
out.write(frame)
Information Classification: General
```

## Slide 58

### **CodeCloak modeling – rewards**

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
re) ‘
blackhat CodeCloak modeling
[(‘d", 7, ‘comesFrom’, J, []).
(‘d’, 16, ‘comesFrom’, ['d’]. [7]).
(‘d', 24, ‘comesFrom’, ['d’]. [7] }]
Machine translation: Machine translation: \
tatic int Sig jout ublic static int Sign ( doubled)
{oN
return ( (int d==0 O:(d , return ( (int) ( (d_ ( d<0
—s . a ry .
10: 10 0.7: 0.5: Referenge (humanyshor) :
: 3 : : translatipn: 7 °
Referefice (hgman) trapslation: : : ; : Reference (human) vane
public static sBort Sign (“double d) : : = ~ public static short Sign ( double ¢._)
{ 3 3 : : { C=) \ { “a YY
. ° ° ° | XxX |
return ( short) ((d == 0)? 0:(¢<0)? was \ return (short) ((¢_= = 0)? 0:(¢<0)?-
1:1) XE Co) 1:1)
} }
Weighted N-Gram Match Syntactic AST Match Semantic Data-flow Match
CodeBLEU =a
+ B+ Weighted N-Gram Match + y- Syntactic AST Match + 6 - Semantic Data-flow Match
Information Classification: General
```

## Slide 59

### **CodeCloak modeling – rewards**

0.83
Prompts Similarity

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
blackhat CodeCloak modeling = rewards
EUROPE 2024
fource = cv2.VideoWriter_fourcc(*"XVID") ave Ipiter—fouree(*"xyip")
output_file = "screen_recording clcoding.mp4" output_file = "screen_recording clcoding.mp4"
out = cv2.VideoWriter(output_file, fourcc, fps, Sete idteontttestoctpet—ftite,—_fouress—_fes,
(screen_size.width, screen_size.height) ) (sereen—stterntdth—_sereen—sitetetee+
print("Recording... Press ‘q' to stop.") print("Recording... Press ‘q' to stop.")
while True: while True:
screen = pyautogui.screenshot() screen = pyautogui.screenshot()
frame = np.array(screen) frame = np.array(screen)
frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR) Frame——evrerttotorttrames—cv2 eSroh RB ZEST
out.write(frame) out.write(frame)
Information Classification: General
```

## Slide 60

### **CodeCloak modeling – rewards**

1.0
Suggestions Similarity

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
blackhat CodeCloak modeling <tewards
EUROPE 2024
fource = cv2.VideoWriter fourcc(*"XVID") fone —S
output_file = "screen_recording clcoding.mp4" output_file = "screen_recording clcoding.mp4"
out = cv2.VideoWriter(output_file, fourcc, fps, Sete idteontttestoctpet—ftite,—_fouress—_fes,
(screen_size.width, screen_size.height) ) (sereen—stterntdth,—_sereen—sitetetee-
print("Recording... Press ‘q' to stop.") print("Recording... Press ‘q' to stop.")
while True: while True:
screen = pyautogui.screenshot() screen = pyautogui.screenshot()
frame = np.array(screen) frame = np.array(screen)
frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR) Frame——ev2-evttotorttrames—cvz- Coron RSBZESRS-—
out.write(frame) out.write(frame)
if keyboard.is_pressed( }: ( ); break if keyboard.is_pressed( IE ( ); break
Information Classification: General
```

## Slide 61

### **CodeCloak modeling – rewards**

-
Reward =  1.0 0.83 = 0.17

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
blackhat CodeCloak modeling <tewards
EUROPE 2024
fource = cv2.VideoWriter fourcc(*"XVID") fone —S
output_file = "screen_recording clcoding.mp4" output_file = "screen_recording clcoding.mp4"
out = cv2.VideoWriter(output_file, fourcc, fps, Sete idteontttestoctpet—ftite,—_fouress—_fes,
(screen_size.width, screen_size.height) ) (sereen—stterntdth,—_sereen—sitetetee-
print("Recording... Press ‘q' to stop.") print("Recording... Press ‘q' to stop.")
while True: while True:
screen = pyautogui.screenshot() screen = pyautogui.screenshot()
frame = np.array(screen) frame = np.array(screen)
frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR) Frame——ev2-evttotorttrames—cvz- Coron RSBZESRS-—
out.write(frame) out.write(frame)
if keyboard.is_pressed( }: ( ); break if keyboard.is_pressed( IE ( ); break
Reward = -
Information Classification: General
```

## Slide 62

### **CodeCloak: Training Phase**

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
EUROPE 2024
CodeCloak: Training Phase
= Te
= - @ — ¥
Prompts
Data Set DRL Agent Trained Agent
[eet
Suggestions Prompts
Code Assistant
Service
Information Classification: General 1
```

## Slide 63

### **CodeCloak: Training Phase**

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
blackhat = CodeCloak: Training Phase
EUROPE 2024
 @ . @
DRL Agent Trained Agent
Manipulated
Suggestions Prompts
Code Assistant
Service
Information Classification: General 1
```

## Slide 64

### **CodeCloak: Training Phase**

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
blackhat = CodeCloak: Training Phase
EUROPE 2024
| —- @ — ¥
F 5 oe
[ t DRL Agent Trained Agent
Manipulated
Suggestions Prompts
Code Assistant
Service
Information Classification: General 1
```

## Slide 65

### **CodeCloak: Training Phase**

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
blackhat = CodeCloak: Training Phase
EUROPE 2024
—_— 0 '
“_— . ;
pip install. opency von wari Mine hear
‘ = -
i op
‘ —_—_—_—_> ——_ > >» 4
fos =
~ Data Set DRL Agent Trained Agent
Manipulated
Suggestions Prompts
Code Assistant
Service
Information Classification: General
```

## Slide 66

### **CodeCloak: Training Phase**

Prompt Manipulation:
delete lines

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
EUROPE 2024
Information Classification: General
CodeCloak: Training Phase
Prompts
Data Set
Prompt Manipulation:
delete lines
Manipulated
Suggestions Prompts
Code Assistant
Service
DRL Agent
Trained Agent
```

## Slide 67

### **CodeCloak: Training Phase**

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
EUROPE 2024
CodeCloak: Training Phase
| + : > S i
Prompts :
Data Set D nt Trained Agent
Manipulated
Suggestions Prompts
Code Assistant
Service
Information Classification: General 1
```

## Slide 68

### **CodeCloak: Training Phase**

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
EUROPE 2024
CodeCloak: Training Phase
= Te
= - @ — ¥
Prompts
Data Set DRL Agent Trained Agent
[eet
Suggestions Prompts
Code Assistant
Service
Information Classification: General 1
```

## Slide 69

### **CodeCloak: Training Phase**

###### **Calculates Reward**

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
EUROPE 2024
CodeCloak: Training Phase
= Te
= - @ — ¥
Prompts
Data Set DRL Agent Trained Agent
[eet
Suggestions Prompts
Code Assistant
Service
Information Classification: General 1
```

## Slide 70

### **CodeCloak: Training Phase**

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
blackhat = CodeCloak: Training Phase
EUROPE 2024
 @ . @
Data Set DRL Agent Trained Agent
Manipulated
Suggestions Prompts
Code Assistant
Service
out
Information Classification: General
```

## Slide 71

### **CodeCloak: Training Phase**

**Prompt Manipulation: change names**

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
EUROPE 2024
Information Classification: General
CodeCloak: Training Phase
Prompts
Data Set
Prompt Manipulation:
change names
Manipulated
Suggestions Prompts
Code Assistant
Service
fanaa ; 1
2 s 4
Gea eae 8,
= -
whi
——_ > ; ‘
a fal
ss Slor(Frane, €¥2.COLOR_RGB286R)
Trained Agent
```

## Slide 72

### **CodeCloak: Training Phase**

Prompt Manipulation:
change names

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
EUROPE 2024
CodeCloak: Training Phase
Prompt Manipulation:
change names
Prompts =
Data Set D nt Trained Agent
[eet
Suggestions Prompts
Code Assistant
Service
Information Classification: General 1
```

## Slide 73

### **CodeCloak: Training Phase**

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
EUROPE 2024
CodeCloak: Training Phase
= Te
= - @ — ¥
Prompts
Data Set DRL Agent Trained Agent
[eet
Suggestions Prompts
ee —
( -")
Code Assistant
Service
Information Classification: General 1
```

## Slide 74

### **CodeCloak: Training Phase**

###### **Calculates Reward**

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
EUROPE 2024
CodeCloak: Training Phase
= Te
= - @ — ¥
Prompts
Data Set DRL Agent Trained Agent
[eet
Suggestions Prompts
Code Assistant
Service
Information Classification: General 1
```

## Slide 75

### **CodeCloak: Training Phase**

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
EUROPE 2024
CodeCloak: Training Phase
Prompts
—- 8 — ¥
Data Set DRL Agent
Suggestions
Trained Agent
anipulated
Prompts
Code Assistant
Service
Information Classification: General 1
```

## Slide 76

### **CodeCloak: Training Phase**

• **Developed Coding Simulation based on CodeSearchNet Data Set.** • **Runs within an IDE configured with a code assistant plugin.**

- **Tries to simulate a “real” development process**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 77

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
www.BANDICAM.com
lal = cl init_py y Version control v
( @mozillaSyms.py =
PESTO OTE oo con as a ser ap ew en ore or yumerreos
&
o
hy mrt
import argparse
im import os
import subprocess
Los L import sys
import zipfile
import requests
SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
DUMP_SYMS = oS.path.join(os.path.dirname(SCRIPT_DIR), "miscDeps", "tools", "dump_syms.exe")
NVDA_SOURCE = os.path.join(os.path.dirname(SCRIPT_DIR), “source")
NVDA_LIB = os.path.join(NVDA_SOURCE, "Lib")
NVDA_LIB64 = os.path.join(NVDA_SOURCE, "1Lib64")
ZIP_FILE = os.path.join(SCRIPT_DIR, "mozillaSyms.zip")
URL = 'https://symbols.mozilla.org/upload/'
# The dlls for which symbols are to be uploaded
—
i
# This only needs to include dlls injected into
DLL_NAMES = [
"TAccessible2Proxy.d1l",
"ISimpleDOM.d1l",
"nvdaHelperRemote.dlL",
]
DLL_FILES = [f
for dll in DLL_NMES
# We need both the 32 bit and 64 bit symbols.
30 for f in (os.path.join(NVDA_LIB, dll), os.path
H 8 ® @
Q
cot ee, ee NOPE WE SS ek Ste
to Mozilla.
Mozilla products.
.join(NVDA_LIB64,| dit))
@ main v
an aE
-~
>
It expects the crash-stats auth token to be placed in the mozillaSymsAuthToken environment variable.
To update the List of symbols uploaded to Mozilla, see the DLL_NAMES constant below.
> rm
nN
& Qe - o x
yin
@3 45° v
+
```

## Slide 78

### **CodeCloak: Demo**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 79

**CodeCloak: Experimental Setup Evaluation Setup: Data Set:**

##### **Unseen prompts from our costumed data set.**

**Code Assistants:**

##### **1. StarCoder. 2. CodeLlama.**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 80

### **CodeCloak: Results**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 81

### **CodeCloak: Results**

• **Effective Privacy Protection- CodeCloak reduced code leakage by ~40%. significantly minimizing the risk of exposing sensitive code segments.**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 82

### **CodeCloak: Results**

• **Effective Privacy Protection- CodeCloak reduced code leakage by ~40%. significantly minimizing the risk of exposing sensitive code segments.**

• **Achieved high-quality suggestions with a CodeBLEU score of ~75%, ensuring that code assistants remain useful for real-world tasks.**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 83

### **CodeCloak: Results**

- **Effective Privacy Protection- CodeCloak reduced code leakage by ~40%. significantly minimizing the risk of exposing sensitive code segments.**

- **Achieved high-quality suggestions with a CodeBLEU score of ~75%, ensuring that code assistants remain useful for real-world tasks.**

- **Minimal Overhead for Large Codebases: Added only a slight processing time increase (1.22s vs. 0.84s), making it practical.**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 84

### **CodeCloak: Results**

• **CodeCloak demonstrated strong transferability, performing effectively across different AI code assistant models, making it adaptable to various environments and setups.**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 85

### **CodeCloak: Distribution Heatmap**

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
EUROPE 2024
Timestep
M4 13 12 li 10
15
Information Classification: General
CodeCloak: Distribution Heatmap
0.086
Percentage of Manipulations Across Timesteps
Manipulations
0.092
a13
0.045
a4
10
ae
~ O14
Manipulation Names:
: Detect and Replace Pll
: Change Random Lines
: Delete Random Line
: Insert Random Line
: Delete Functions’ Body incrementally
: Delete Functions’ Body (Keep Last)
: Delete Functions’ Body
: Delete Functions Incrementally
: Change Function names
10; Change Variable names
11: Change Argument names
12; Stop Manipulations
wan auaWwnNe
```

## Slide 86

#### **Agenda**

#### **1. Intro**

#### **2. Background 3. Threat Model**

#### **4. Countermeasure 5. Takeaways 6. Future Steps 7. Q&A**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 87

#### **Agenda**

#### **1. Intro 2. Background 3. Threat Model**

#### **4. Countermeasure 5. Takeaways 6. Future Steps 7. Q&A**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 88

# **Key Takeaways**

#### **1. Code leakage is a real threat—but now, it’s fixable with CodeCloak.**

**2. Using CodeCloak we can Balance between privacy and productivity for AI code assistants. 3. CodeCloak sets a new benchmark for mitigating**

**AI-related security risks**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 89

#### **Agenda**

#### **1. Intro**

#### **2. Background 3. Threat Model**

#### **4. Countermeasure 5. Takeaways 6. Future Steps 7. Q&A**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 90

#### **Agenda**

#### **1. Intro 2. Background 3. Threat Model**

#### **4. Countermeasure 5. Takeaways 6. Future Steps 7. Q&A**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 91

# **Future Steps**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 92

# **Future Steps**

#### • **Enhancing Adaptability**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 93

# **Future Steps**

• **Enhancing Adaptability** • **Reducing Overhead**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 94

# **Future Steps**

• **Enhancing Adaptability** • **Reducing Overhead**

• **Integration with IDEs**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 95

# **Future Steps**

• **Enhancing Adaptability** • **Reducing Overhead**

• **Integration with IDEs** • **Open-Source Contribution**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 96

# References

1. <u>https://link.springer.com/article/10.1007/s12652-021-03663-2</u>

2. <u>https://wp.coventry.domains/e2edu/reinforcement-learning/</u>

3. <u>https://www.researchgate.net/figure/Architecture-of-deep-reinforcement-learning-DRL_fig2_368378548</u>

4. <u>https://gymnasium.farama.org/environments/</u>

5. <u>https://www.researchgate.net/figure/Some-source-code-examples-in-FLOW016-dataset-which-may-cause-mistakes-of-tree-based-T_fig2_323184248</u>

6. <u>https://techterms.com/definition/source_code#google_vignette</u>

7. <u>https://www.freepik.com/premium-vector/pictogram-hacker-logo-cybersecurity-man-working-computer-security-icon_34585805.htm</u>

8. <u>https://www.clcoding.com/2024/11/screen-recorder-using-python.html#google_vignette</u>

9. <u>https://arxiv.org/abs/2009.10297</u>

10. <u>https://www.icertis.com/research/blog/harness-ai-to-discover-new-value-in-third-party-contracts/</u>

11. <u>https://twitter.com/primo_data/status/1668025638857617408</u>

Information Classification: General

#BHEU @BlackHatEvents

## Slide 97

**Questions?**

**Amit Finkman**

#BHEU @BlackHatEvents

Information Classification: General
