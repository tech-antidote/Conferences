---
title: "Emit My Keystroke"
speakers: ["Pardomuan"]
conference: "Black Hat"
conference_full: "Black Hat ASIA 2023"
edition: "ASIA"
year: 2023
source_pdf: "Black Hat Asia 2023 slides/AS-23-Pardomuan-Emit-My-Keystroke.pdf"
pages: 41
sha256: "a652a55ff2c81716580e395336f8ed3306961d833b4e9612d67a49cf25ce1903"
text_chars: 19721
ocr_pages: 5
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T23:55:24Z"
---
# Emit My Keystroke

**Speakers:** Pardomuan  
**Conference:** Black Hat ASIA 2023  
**Source:** `Black Hat Asia 2023 slides/AS-23-Pardomuan-Emit-My-Keystroke.pdf` (41 pages)


## Slide 1

## E-Meet (or Emit?) My Keystrokes How Benign Screen-sharing Meetings Could Leak Typing Behaviors

**Chrisando Ryan P. Siahaan**

Security Researcher & Lecturer Specialist in Cybersecurity

#BHASIA @BlackHatEvents

## Slide 2

# About

- Call me **Chrisando Ryan** , **@chrisandoryan** or **Siahaan**

- Lecturer Specialist in Cyber Security, BINUS University, Indonesia

- CEO of Questlabs ID, a security-centered software development agency in Indonesia.

- Driven to a T-shaped culture by extensively studying AI, Computer Vision, and Big Data domains as well, and intertwine them with Cyber Security.

- Black Hat Asia Arsenal speaker, back in 2020 (covid-era L).

- CTF problem setter & judge at various competitions in Indonesia.

- Enjoy bounty hunting, building ventures, and conducting multi-disciplinary projects

#BHASIA @BlackHatEvents

## Slide 3

# Agenda

- Backstage story.

- Others who have tried…

- Our approach.

- The danger behind all these.

- Is there any cure?

- Takeaways.

#BHASIA @BlackHatEvents

## Slide 4

# Backstage Story

###### One ordinary day, you’re in a Zoom meeting with colleagues.

#BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
. ae 7 \ gk Py K <= WE
blackhat Backstage Story Be os
ASIA 20253
One ordinary day, you’re in a Zoom meeting with colleagues.
Unmute tart Video Security —_—Participants
```

## Slide 5

# Backstage Story

###### You guys are doing your stuffs, discussing back and forth.

#BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pisek hat
ASIA 2023
You guys are doing your stuffs, discussing back and forth.
Backstage Story
—~
Chrisando Ryan Pardomuan @Y 4 - OQ xX
ls Harga docx v
jt Draw Design Layout References Mailings Review View Help
Calvi Gow) 2 A A Aare Ap He iS ~ EYEE ALG finn 606 24
Normal No Spacing Heading 1 >ading Replace an -
BIUvax,x Ary 4- Ary [B/E S=1= ay . = — Dictate Editor Reuse
~ a ~ [} Select ¥ Files
Font & Paragraph B Styles 8 Editing Voice Editor Reuse Files ¥
Lalap 5 320 1.600
Serundeng 5 100 500
Total Modal: 63.435
Total Jual: 96.000
Total Untung: 32.565
Total kerlu
1B  f¥ Accessibility: Good to go ‘Di Focus fe - iu + 100%
A Comments | | Editing »
```

## Slide 6

# Backstage Story

Suddenly, while a colleague’s sharing their screen, they stumbled upon a page which forces them **to do a sign-in using password** .

#BHASIA @BlackHatEvents

## Slide 7

# Backstage Story

**Too lazy** to stop the screen-sharing temporarily, they choose to continue typing their password; Thinking that these **black bullet-mask symbol will protect them…**

#BHASIA @BlackHatEvents

## Slide 8

# Backstage Story

###### **All those led to our attempt to test a hypothesis:**

_If we are to live in a world where most meetings will be conducted through online video meetings… Then it might be possible to_ **_leak_** _and_ **_mimic_** _a user's typing behaviour through a_ **_screen-sharing video_** _alone._

#BHASIA @BlackHatEvents

## Slide 9

# Backstage Story: The Basics

So, about **typing behavior.**

- A term coined as **keystroke biometrics,** that is: the process of measuring and analysing an individual's unique typing patterns or rhythms on a computer keyboard.

- Used for?

**User authentication Fraud detection Forensic analysis**

- But, how?

**Time between keystrokes (called** **_Inter-key Latency_ ) Duration of each keystroke (called** **_Hold Latency_ ) Pressure or force applied to the keys**

#BHASIA @BlackHatEvents

## Slide 10

# Backstage Story: The Basics

###### **The Recipe (Simplified):**

**How short** (or long) **the delay between** each **keypress**

**+**

**How short** (or long) **you hold-press** each **character**

**+**

- **(**) How hard/strong you press** the character keys

**+**

**(**) How many typos/mistakes** you made

**=**

**Authentication/Classification. [i.e., Welcome, Bob!]**

(**): **less-common metrics**

#BHASIA @BlackHatEvents

## Slide 11

# Backstage Story: The Basics

- Although not as widely-accepted as fingerprint, but **keystroke biometrics** are gaining attention.

- Some major players in the **keystroke dynamics** industry.

#BHASIA @BlackHatEvents

## Slide 12

# The Idea, Originally

~~Create a better~~ **~~keystroke dynamics~~** ~~approach as a way to robustly~~ **~~authenticate legitimate users~~**

Create a technique to extract **typing key-delay** out of a screenrecorded video,

…and maybe use them for despicable reasons >:) (we’ll come back for this)

#BHASIA @BlackHatEvents

## Slide 13

# The Idea, Originally

##### We call this technique, **Camstroke** .

#BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pisek hat
ASIA 2023
tin
The Idea, Originally «
We call this technique, Camstroke.
Camstroke | Private
Annotate keystroke from recorded typing video, a utility for video-based
Keystroke Inference Attack
```

## Slide 14

# Others Who Have Tried…

- Silk-tv: Secret information leakage from keystroke timing videos (Balagani, et al., 2020)

   - Studied the **leakage of user secrets** ( _password_ and PIN) from typing activities.

   - Use video footage of a computer/ATM machine screen where password masking characters are displayed when users type their password/PIN.

   - Extract **inter-keystroke** timing information from the video and feed them to Random Forest (RF) classifier to predict the typed password/PIN.

- Cracking Android pattern lock in five attempts (Ye, et al., 2017)

   - Proposed a novel video-based attack to **reconstruct Android lock patterns** .

   - • **Does not require** the video to capture **any content displayed on the screen** , only **fingertip movements.**

- Use TLD ( _tracking—learning—detection)_ algorithm to generate movement trajectory.

#BHASIA @BlackHatEvents

## Slide 15

# Our Approach, Originally

#BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ny
2)
blackhat Our Approach, Originally :
ASIA 2023
Victim
— IK Keylra
Legit
Authentication Keystroke Dynamics
Authentication
Observing victim's screen t
(screen sharing, etc.)
Spoot Authentication
Extract Character Create a synthetic typing
from Screen- ._+————>} sequence from victim's
recorded Video typing pattern
Attacker
ee ee ee
: '412ms '67ms | '
a n fae |
Beeeeese 8 Beeeeee 8 tbeowwne
```

## Slide 16

# Our Approach, Originally

- During this study, we encountered (at least) **four** of the most pain-staking, mind-bending, and brainmelting obstacles:

- **Challenge #1:** How to **detect when a user is typing** from a mere screen-recording video data?

- **Challenge #2:** How to **detect what character** is **typed** by the user **on each millisecond** of the video?

- **Challenge #3:** How to **reconstruct the victim’s typing pattern** (extract each keystroke’s timing/delay information)?

- **Challenge #4:** How to **predict/expose a victim’s password** from **the leaked typing pattern** ?

#BHASIA @BlackHatEvents

## Slide 17

#### Cursor Tracking and Text Detection Alg.

- First things first. From a mere **screen-recording video** , we need to:

   **1. Isolate the segment** of the video **where a typing activity occurs** .

   **2. Extract what character** is being **typed** by the user **on each millisecond** of the video.

**The AHA!** 💡 **Assumption:**

the **most recent typing activity** must be **occurred to the left of a text cursor object** that appears on the screen.

#BHASIA @BlackHatEvents

## Slide 18

#### Cursor Tracking and Text Detection Alg.

**Challenge #1. Isolate the segment of the video where a typing activity occurs.**

- Use **OpenCV** to identify **a moving rectangle-shaped object** (i.e., the **Text Cursor** )

   - Grayscale Conversion & Otsu’s Thresholding

   - Canny Edge Detection & Bitwise XOR

- Identifies location of the **Text Cursor** , called **Cursor Bounding Box (CBB) (the red box) Takeaway**

   - The occurrence of CBB **marks the start of the video segment** with typing activities.

#BHASIA @BlackHatEvents

## Slide 19

#### Cursor Tracking and Text Detection Alg.

**Challenge #2. Extract what character typed by the user on each millisecond of the video.**

- We generate another bounding-box, called **Isolation Bounding Box (IBB)** relatively **to the left** of the **Cursor Bounding Box (CBB)** coordinates.

- However, in a single IBB region, there might be more than one character captured L.

- Hence, we need to **know, which one is the most recently-typed character?**

###### Frame #087

Cursor Bounding Box (CBB)

Isolation Bounding Box (IBB)

Fig: IBB with multiple characters captured

#BHASIA @BlackHatEvents

## Slide 20

#### Cursor Tracking and Text Detection Alg.

**Challenge #2. Extract what character typed by the user on each millisecond of the video.**

###### Frame #087

- Use **Connected-Component Labeling (CCL)** to separate multiple characters from the IBB frame.

- Yields the following components:

   - Background Region

   - Tallest Region (aka Text Cursor)

   - Rightmost Character

   - Previous-typed Character

**Takeaway**

The **Rightmost Character** , always located to the left of Tallest Region, indicates the most-recently typed character on the frame.

#BHASIA @BlackHatEvents

## Slide 21

#### Typing Pattern Reconstruction

- **Challenge #3. Reconstruct the victim’s typing pattern (extract each keystroke’s timing/delay information)**

- • From every frame in the video, we extract a character (aka the **Rightmost Character** component) and convert them to digital data with **OCR (Optical Character Recognition).**

- • A single character in a single video frame is called a **KUnit** .

- But we observe that the same character might **appear** in **more than one frame** consecutively.

- • **Why?**

#BHASIA @BlackHatEvents

## Slide 22

#### Typing Pattern Reconstruction

- **Challenge #3. Reconstruct the victim’s typing pattern (extract each keystroke’s timing/delay information)**

- • If the same character appears in more video frames adjacently, we can **assume the longer the key-delay** of that character.

- Hence, we group characters from different frames based on similarity of the character’s coordinates relative to each other. We named it **KeystrokePoint.**

#BHASIA @BlackHatEvents

## Slide 23

#### Typing Pattern Reconstruction

**Challenge #3. Reconstruct the victim’s typing pattern (extract each keystroke’s timing/delay information)**

- On the image, character ‘ **a** ’ is displayed in 3 video frames. Hence, the **key-delay** is **99ms** .

- • **Why?**

- Because every video frame lasts for 33ms (30FPS). Thus, 3 video frames last for **99ms** . **Takeaway**

The higher the number of KUnits (frame) are inside a KeystrokePoint (group), we assume the longer the key-delay of that character.

#BHASIA @BlackHatEvents

## Slide 24

#### Attack in Action

#BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
biaekhat Attack in Action ©
ASIA 20253
a
@2-CS . Default (python) U1
[INFO] Storing KUnit to Last KeystrokePoint with ID: 376c52e3-@e8e-4aed-b42f-ead
ecfabf75Sb
[INFO] Current KUnit coordinates: (537.7887092317341, 704.2, 546.188709231734, 7
13.2)
CINFO] KUnit is a RIGHTMOST candidate; Updating lastseen data.
[INFO] KUnit Shape: 84 9@
[INFO] This KeystrokePoint has coordinates (537 .7887092317341, 704.2, 546.1887
09231734, 713.2)
[INFO] Detected Keystroke: o
Frame: 100
[INFO] White composition in Background @.9337941176470588
XY Ratio (@.07291221127487131, 1.0) (1.065533774809484, 1.0)
26 .50334491338435 363.4966550866157 180.55227454110138 169.4
19 409 ® 350
XY Ratio (@.2706543608548607, 1.0) (1.01818 539596, 1.0
2545889865
Predetermined Sentence Phase
ext to type
@ 83.07152911542451 306.9284708845755 176.5770199573726 173.4
61 451 @ 350
XY Ratio (0.53080 38
135 .23152319919404 254.768
100 498 @ 350
[INFO] There are 3 Keystroke Candidates Final Keystroke Image
C'CANDIDATE', ‘CANDIDATE’, "RIGHTMOST" ]
[INFO] KUnit Image Shape: (350, 390)
[INFO] Frame ID: 100
»)
2980042627.
, 1.0) (1.1321980158994676, 1.0)
47680080598 185.8501427212179 164.14985727878212
PC! smc ust, Sampic_cypc,
‘camstroke': conda' ~NOA ® You. 2 months aco 42n93.Col72 Spaces:4 UTF-8 LF Pvthon
```

## Slide 25

#### Wait. Why the Fuss?

- At this point, **key-delay** between characters can be extracted through a video alone.

- It is **permission-less.** No need to insert/install **keylogger** into the victim’s machine.

- This attack can occur when:

   - A victim makes their screen visible to the attacker (i.e., in a Zoom meeting).

   - The attacker records the victim’s screen, where the victim’s typing activities is visible.

   - The delays between characters is extracted from the obtained video frames.

- Thus, this attack can be conducted remotely, without the victim even realizing.

- If the victim’s account is protected with **keystroke dynamics** authentication, we can **mimic** their typing pattern and **replay them** to bypass the authentication.

#BHASIA @BlackHatEvents

## Slide 26

#### Okay. But is it Working?

Before we go into the more despicable part. **Let’s see how good the algorithm performs.**

#BHASIA @BlackHatEvents

## Slide 27

#### Benchmarking the Attack

- Aspects evaluated:

   - **How similar** the **reconstructed typing pattern** of the victim? (Statistic Similarity)

   - **How effective** the attack against **KeyTrac** authentication (Evasion Rate & EER)

- We tested the attack on 14 victims (with consent), each on different Zoom meetings.

- • The victims were asked to perform these **typing activities** :

|**No**|**Evaluation Group**|**Typed Text**|**Total Samples**|
|---|---|---|---|
|1|Password Phrase|abudhabiacrossthesea||
|2|Greeting Sentence|hi my name is [NAME]|210|
|3|Long Sentence|i want to go and change the world||

#BHASIA @BlackHatEvents

## Slide 28

#### Benchmarking the Attack

###### We asked each victim to perform a typing activity, and record them:

And, to collect actual key-delay data, we use **keylogger** installed on the victim’s device.

#BHASIA @BlackHatEvents

## Slide 29

#### Similarity Test: Password Group

###### **Text typed: abudhabiacrossthesea**

- Tested using Shapiro-wilk Test (Normality Test), Levene’s Test (Variance Test), and Wilcoxon Signedrank Test (Mean Similarity Test).

- Both key-delays are **distributed normally** and have **equal variance** .

- There is **no significant mean differences** between the **reconstructed key-delays** and the **actual keydelays;** the data can be considered similar.

- Process time is **5.61FPS** , or **5.35x longer** than the actual video duration (30FPS).

###### **Comparison of the Reconstructed Keydelay and the Actual Key-delay (averaged).**

#BHASIA @BlackHatEvents

## Slide 30

#### Similarity Test: Greeting Group

**Text typed: hi my name is [NAME]**

- Suffers **lower performance** compared to the **password text group** .

- There is **still no significant mean differences** between the **reconstructed key-delays** and the **actual key-delays;** the data can be considered similar.

- Process time is **6.78FPS** , or **4.43x longer** than the actual video duration (30FPS).

**Comparison of the Reconstructed Key-delay and the Actual Key-delay (NOT averaged).**

#BHASIA @BlackHatEvents

## Slide 31

#### Similarity Test: Longtext Group

###### **Text typed: i want to go and change the world**

- Also suffers **lower performance** compared to the **password text group** .

- There is **still no significant mean differences** between the **reconstructed key-delays** and the **actual key-delays;** the data can be considered similar.

- Process time is **5.91FPS** , or **5.08x longer** than the actual video duration (30FPS).

###### **Comparison of the Reconstructed Keydelay and the Actual Key-delay (averaged).**

#BHASIA @BlackHatEvents

## Slide 32

#### Attack Effectiveness

- KeyTrac is a AaaS (Authentication-as-a-service) platform that’s widely used by global companies around the world.

- KeyTrac supports two modes: **Password-hardening** mode and **Freetext** mode.

- **How do we perform the attack against KeyTrac?**

**Performance Metrics**

- Evasion Rate ( **ER** ): measures **the rate of the attack being undetected** .

- Equal Error Rate ( **EER** ): measures the increase/decrease of performance of **KeyTrac** authentication service.

#BHASIA @BlackHatEvents

## Slide 33

#### Attack Effectiveness: FAR-FRR-ERR

KeyTrac performance in **Password** mode, before ( **left** ) and after ( **right** ) the attack. **EER increased 349.5% post-exploitation, Optimal authentication threshold increased from 13 to 59 High ERR indicates the decreasing accuracy of the biometric system (due to FAR is increasing).**

#BHASIA @BlackHatEvents

## Slide 34

#### Attack Effectiveness: FAR-FRR-ERR

KeyTrac performance in **Freetext** ( **Greeting** + **Longtext** group) mode, before ( **left** ) and after ( **right** ) the attack. **EER increased 2553.5% post-exploitation, Optimal authentication threshold increased from 6 to 57 High ERR indicates the decreasing accuracy of the biometric system (due to FAR is increasing)**

#BHASIA @BlackHatEvents

## Slide 35

#### Attack Effectiveness: Evasion Rate

●
●
●
●

- On **Password mode** with authentication threshold of 60%, 9 out of 14 attempts successfully spoof KeyTrac into allowing the authentication to pass through.

- That means, **Evasion Rates (ER) is 67%,** or almost **2 of 3 attacks is successful.**

- Unfortunately, on **Freetext mode** with authentication threshold of 60%, only 6 out of 14 attempts successfully spoof KeyTrac into allowing the authentication to pass through.

- That means, **Evasion Rates (ER) is 43%.**

**Evasion Rates (ER)** on different authentication thresholds

#BHASIA @BlackHatEvents

## Slide 36

#### What Have We Learned?

###### **The evasion rates (ER) were not able to reach beyond 70%, why?**

- This is mainly affected by the typing speed of the respondent (WPM or word-per-minute).

- The higher the WPM, the lower the number of captured frames.

- Hence, the delay similarity of the reconstructed typing pattern is also decreased.

- High WPM should be compensated with high video frame rates (FPS).

**So, are we done here? Well, not apparently.**

#BHASIA @BlackHatEvents

## Slide 37

#### Another Layer of Curiosity

Our Late-Night Thoughts. **We believe the method is working, but perfection is still far away…**

Amidst the study, we encountered **another WHAT-IF question scratching our curiosity.**

_If we’re able to_ **_track text cursor_** _and_ **_extract typing pattern_** _out of screen-recording video, then what happens if_ **_inside the video_** _occur_ **_a user typing their password_** _?_

#BHASIA @BlackHatEvents

## Slide 38

#### Another Layer of Curiosity

### **We’re able to track them as well.** Our Late-Night Thoughts.

#BHASIA @BlackHatEvents

## Slide 39

#### Limitations

- Typing pattern extraction sensitivity drops when there is a lot of movements, e.g., video playing, heavy screen-scrolling, etc.

- The higher the WPM requires more FPS to maintain high accuracy of the extraction. Most online-meeting platforms only support 30/60FPS video recording.

- Many **keystroke biometrics** authentication also uses **hold-delay** metric. As of now, we’re only able to extract the **inter-key delay** metric.

#BHASIA @BlackHatEvents

## Slide 40

#### Is There Any Cure?

- As in many other behavior-based attacks, there are no better solution than to applies a secure user behavior to prevent the leakage.

- That means, **being mindful** on who’s your audience during screen-sharing meetings.

- And **being eager** enough to stop the screen-sharing whenever we’re about to input something sensitive and confidentials.

- However, we also found some projects interesting to inhibit **typing pattern** extraction, such as:

   - **Kloak** by Vinnie Monaco: introduces random delay to keyboard typing at the device level.

   - Keystroke Dynamics Anonymization System (Migdal, D., & Rosenberger, C., 2019)

#BHASIA @BlackHatEvents

## Slide 41

#### Takeaways

1. Should **keystroke biometrics** adoption growth consistently in the next few years, we expect that more advanced mimicry (side-channel) attack will be demonstrated from unexpected sources of data.

2. By using a screen-recorded video, someone can achieve a statistically staggering similarity in key-delay timings as if they used a keylogger.

3. Relying on videos allows for the elimination of the need for any external hardware or modifications on the victim’s computer (i.e., **keylogger** ).

#BHASIA @BlackHatEvents
