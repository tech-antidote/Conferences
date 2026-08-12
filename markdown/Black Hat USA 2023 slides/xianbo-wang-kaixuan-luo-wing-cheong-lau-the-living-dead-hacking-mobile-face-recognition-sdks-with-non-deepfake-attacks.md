---
title: "The Living Dead Hacking Mobile Face Recognition SDKs with Non-Deepfake Attacks"
speakers: ["Xianbo Wang", "Kaixuan Luo", "Wing Cheong Lau"]
conference: "Black Hat"
conference_full: "Black Hat USA 2023"
edition: "USA"
year: 2023
source_pdf: "Black Hat USA 2023 slides/Xianbo Wang & Kaixuan Luo & Wing Cheong Lau_The Living Dead Hacking Mobile Face Recognition SDKs with Non-Deepfake Attacks.pdf"
pages: 43
sha256: "0821a15adb6a8c667c843dd5cb354537043c8d003510b1f560cc6c0dc39c52eb"
text_chars: 12133
ocr_pages: 5
has_ocr: true
redacted_secrets: 0
ocr_confidence: 88.1
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T04:23:56Z"
---
# The Living Dead Hacking Mobile Face Recognition SDKs with Non-Deepfake Attacks

**Speakers:** Xianbo Wang, Kaixuan Luo, Wing Cheong Lau  
**Conference:** Black Hat USA 2023  
**Source:** `Black Hat USA 2023 slides/Xianbo Wang & Kaixuan Luo & Wing Cheong Lau_The Living Dead Hacking Mobile Face Recognition SDKs with Non-Deepfake Attacks.pdf` (43 pages)


## Slide 1

### The Living Dead: Hacking Mobile Face Recognition SDKs with Non-Deepfake Attacks

Speaker(s): Wang Xianbo, Kaixuan Luo, Wing Cheong Lau The Chinese University of Hong Kong

#BHUSA @BlackHatEvents

## Slide 2

# About Us

Xianbo Wang PhD Candidate @sanebow

Kaixuan Luo PhD Student

Wing Cheong Lau Professor

#BHUSA @BlackHatEvents

2

## Slide 3

# Outline

**1. Motivation** : facial recognition, liveness detection, third-party SDK

**2. Related work** : presentation attacks, deepfake, others

**3. Typical workflows** : system architecture and protocol flow

**4. What can go wrong?**

**5. Empirical study** : analysis on 18 Android SDKs

**6. Case study** : detail steps of the attack

**7. Conclusions**

#BHUSA @BlackHatEvents

3

## Slide 4

# Motivation **Face Recognition and Interactive Liveness Detection in Mobile Apps** App-level _vs._ system-level (Face ID)

#BHUSA @BlackHatEvents

4

## Slide 5

# Use Cases

Setup a new bank account

Age verification in games

Profile verification in dating apps

#BHUSA @BlackHatEvents

5


> Recovered by OCR — confidence 89/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Use Cases
Setup a new bank account Age verification in games Profile verification in
dating apps
Great photo! Now it’s
time to take a selfie ARERR LESH, WRRRAMIRIGAR. (HH Get verified
Prove you’re the person in your
profile by taking a video. If you
match, boom, you’re verified!
To make sure it’s really you, we'll compare
your selfie to the photo on your ID.
Maybe later
Continue
```

## Slide 6

# Hacking Kit Sold in Black Markets

######

ID card / passport photo with high quality headshots **$5 (USD) per set**

Teaching you how to make fake animated video to bypass facial recognition **$300 = tutorial videos + software**

6

Device with special ROM and software **$250**

#BHUSA @BlackHatEvents

## Slide 7

- Reported Criminal Cases

- • In 2019, two young men hacked face recognition system in a local **bank** and created 76 fake accounts.

- • In 2020, a prosecution on criminals exploiting face recognition system in a **government** website to create fake tax invoices since 2018.

#BHUSA @BlackHatEvents

7

## Slide 8

# Related Attacks in Academic Research

###### Presentation attacks

###### Deepfake attacks

###### Exploiting implementation bugs

#BHUSA @BlackHatEvents

8

## Slide 9

# Related Attacks in Academic Research

- **Deepfake against Liveness APIs**

`o` Li, Changjiang, et al. " _Seeing is living? rethinking the security of facial liveness verification in the deepfake era._ " _31st USENIX Security Symposium (USENIX Security 22)_ . 2022.

- **Hardware-based video replacement & FaceID bypass via customized eyeglasses**

`o` Chen, Yu, Bin Ma, and Zhuo Ma. " _Biometric authentication under threat: Liveness detection hacking._ " _Black Hat USA_ (2019).

#BHUSA @BlackHatEvents

9

## Slide 10

# Related Attacks in Academic Research

- **Face Recognition Protocol Analysis**

   - Zhang, Xiaohan, et al. " _Understanding the (In) Security of Cross-side Face Verification Systems in Mobile Apps: A System Perspective._ " 2023 IEEE Symposium on Security and Privacy (SP). IEEE Computer Society, 2023.

   - Parallel independent work

   - Appeared in May 2023, after our submission to Black Hat USA

#BHUSA @BlackHatEvents

10

## Slide 11

# **Provided by SDKs** Workflow

1. Detect and locate face

- à good quality, correctly positioned

2. Liveness Detection

- à Make sure it's real person

3. Face matching

- à Compare captured frame with:

- photo on previously scanned ID card

- OR authority database

#BHUSA @BlackHatEvents

11

## Slide 12

# Liveness Detection

##### Static Liveness Detection _Image-based_

To deny photo **printed** or showed on **screen**

##### Interactive Liveness Detection _Video-based_

More secure, and aims to mitigate image data injection/replay attacks

* Image source: https://www.thalesgroup.com

#BHUSA @BlackHatEvents

12

## Slide 13

# Variants of Video-Based Liveness

##### Motion Based

Flashing

Reciting

Passive

#BHUSA @BlackHatEvents

13


> Recovered by OCR — confidence 95/100 on the text kept, 73/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Variants of Video-Based Liveness
Motion Based Flashing Reciting Passive
x
x
Stay still
Open your mouth
13
```

## Slide 14

# Demo Time !

#BHUSA @BlackHatEvents

14

## Slide 15

# System Architecture

Camera   Mobile Liveness Mobile Face
Image Result
More common in non-end  Stream Detection SDK Comparison SDK
Cloud Face
Camera   Mobile Liveness Cloud Liveness
images Image Comparison Result
Stream Detection SDK Detection Service
Service
Most popular in mobile apps
Cloud Face
Camera   Mobile Face SDK Cloud Liveness
Video Image Comparison Result
Stream (Guidance only)  Detection Service
Service
Threat model: attacker has total control of his mobile device (rooted)
à  Any operation performed on the client cannot be trusted

Pure Local
More common in non-end
user devices
Local-Cloud Mixed
Most popular in mobile apps
Pure Cloud
In some mobile apps

#BHUSA @BlackHatEvents

15

## Slide 16

## Step-by-Step Workflow

- Multi-party communication

- • Many implementation choices

#BHUSA @BlackHatEvents

16


> Recovered by OCR — confidence 81/100 on the text kept, 62/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
>
App's Code
@ init SDK Liveness
with Configs Result
v |
Camera
Bsvcan Mobile Face SDK
User
\ A
3) Liveness
\ Detection
4) Upload Result Data af) Liveness
{a Reference Photo—t+->| @ Face
Comparison
App Server <—Comparison Result Service
¢ Multi-party communication
¢ Many implementation choices
16
ID Photo Matching
2 Authority DB
```

## Slide 17

# Security-Usability Tradeoffs

Pure Local
Local-Cloud
Mixed
Pure Cloud

**Cost** : images (1~3 frames) _vs._ video (100x frames). _poor cellular signal_ **Experience** : [blink, nod, shake] à [nod] _vs._ [ALL over again!] _mad user_

😡

#BHUSA @BlackHatEvents

17

## Slide 18

# Design & Implementation Choices

#BHUSA @BlackHatEvents

18


> Recovered by OCR — confidence 89/100 on the text kept, 59/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Design & Implementation Choices
SDK Core Config Env. : Compare
Logic Generation Checking Sones Bol Face
Java On-device On-device On-device Plaintext App Server
oloo
Native In the Cloud Device & Cloud Hybrid Encrypted Face Cloud
Pure Cloud
18
```

## Slide 19

# Attack Setup

**Attacker owns:** Victim's Photo(s), a device with full control **Goal:**

Spoof Face Recognition, Identify as the victim **How:**

Bypass/Deceive Liveness & Upload victim's photo

#BHUSA @BlackHatEvents

19

## Slide 20

# Sophisticated Protection, but …

Collect and upload mobile sensor data: emulator detection Ineffective when hacker uses a real device

Run secondary static image-based liveness on cloud: detect scanned photo

Ineffective: Attacker has original image file of the victim

#BHUSA @BlackHatEvents

20

## Slide 21

# Pitfalls: Initialization Stage

Actions: [😑, 😮, 😑]
Score threshold  θ = 0.9
😈
Actions: [😑]
θ = 0.1
Next action Next action
Surprise!
😈
Try Actions: [ ] ← random() ← fixed

#BHUSA @BlackHatEvents

21

## Slide 22

# Pitfalls: Result Passing

Level: Easier Than Easy Replace photo returned by liveness 😈 **{R, M'}** result.livenessScore = 0.9; **M M'**

#BHUSA @BlackHatEvents

22

## Slide 23

# Encrypt result, decrypt in cloud

SDK dev: only pro
hackers can reverse my
heavily obfuscated code
🤔
23

#BHUSA @BlackHatEvents

23


> Recovered by OCR — confidence 86/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Encrypt result, decrypt in cloud
Face SDK Mobile App App Server Face Cloud
Liveness|
vimenc J }___{ Menc \__» M >
Enc/Sign enc Dec
Liveness
Compare
23
```

## Slide 24

# Pitfalls: Result Passing

(More) Secure Routine
😎 Script kiddie:
SDK dev: only pro
Let me just replace
hackers can reverse my
the plaintext image
heavily obfuscated code
🤔 Level: EASY
Useless encryption
24 #BHUSA

#BHUSA @BlackHatEvents

## Slide 25

# Pitfalls: Result Passing

Level: Medium Malleability Attack

Failed to bind (R, M) with message authentication or encrypting the whole thing

#BHUSA @BlackHatEvents

25

## Slide 26

# Some Cliché Mistakes

##### Insecure file storage

No UI hijacking protection

Malicious App
Covering
Face authorization

Malicious app can steal your photo! Refer to our previous work : Lower cost for replace attack (no hooking) https://mobitec.ie.cuhk.edu.hk/phyjacking/

#BHUSA @BlackHatEvents

26

## Slide 27

# Empirical Study

_Catastrophic Less secure_

_Good practice_

11 out of 18 _face SDKs_ have insecure design or implementation

#BHUSA @BlackHatEvents

27

## Slide 28

# Measurement Study

Goal: scan market apps to get

- 1) Number of apps embed facial recognition SDKs 2) Identify which SDK they use

Challenge: Many apps are obfuscated / protected by packers

Stable fingerprints:

- 1) Model files (.dat, .tflite)

- 2) SDK Native libraries (.so)

- 3) SDK license files (.txt, .lic)

#BHUSA @BlackHatEvents

28

## Slide 29

# Measurement Study

1) Financial apps are the primary adopters of Face SDKs 2) Most of them include insecure SDKs

#BHUSA @BlackHatEvents

29

## Slide 30

# Case Study

Use banking service (account linking, withdrawal)

Banking
Service
Face Recognition
Service
30

#BHUSA @BlackHatEvents

## Slide 31

# Attacker's Master Plan

##### Recon

##### Target Localization

##### Attack

- Is the app packed?

- • Which face SDK?

- • Collect SDK package

- • Read SDK docs

- Decompile the SDK to locate hooking target

- • Defeat anti-debugging

- • Locate target in app

- Dump and inspect data

- • Process victim's photo to match to format

- • Replace the data

#BHUSA @BlackHatEvents

31

## Slide 32

# Peek into the app

First challenge: Sophisticated commercial packers

###### Some unpacking tools:

- <u>https://github.com/zyq8709/DexHunter</u>

- <u>https://github.com/hluwa/frida-dexdump</u>

Trick: _analyze_ **_history versions_** _of the app_

More about commercial packers:

_Duan, Yue, et al. "Things You May Not Know About Android (Un) Packers: A Systematic Study based on Whole-System Emulation." NDSS. 2018._

_* Disclaimer: analysis and screencaps are not from a single app but a combination of a few real cases for illustration only_ 32

#BHUSA @BlackHatEvents

## Slide 33

# Retrieve SDK and Docs

Q: Why not just decompile apps? A: Many apps are packed, but you can find readable code in SDK

###### When platform says " _enterprise only_ "

###### Other Sources

- GitHub Repositories

Client-side Download Permission Control

- Historical apps without packing

- • Maven Repositories

- SDK docs help reverse engineering

- Protocol diagram

- • List of APIs and options

#BHUSA @BlackHatEvents

## Slide 34

# Analyze the SDK, identify the weak link

Easy-to-tamper threshold value à weaker/invalid liveness detection

There are also a bunch of thresholds like mouth opening gap, head turning angle, etc. Lowering these thresholds can make video forging easier. Or even effectively disable the liveness detection.

#BHUSA @BlackHatEvents

34

## Slide 35

Controllable action sequence. Sometimes even accept empty sequence!

_Interactive_ liveness detection DOWNGRADES to _Static_ liveness detection OR even _No_ liveness detection

Frida hooking

#BHUSA @BlackHatEvents

35

## Slide 36

Provider SDK returns an encrypted result and raw image frames. Apps are supposed to send encrypted result to provider for verification.

A library provided by some tech company that help financial apps to integrate banking service "securely"

#BHUSA @BlackHatEvents

36

## Slide 37

# Who to blame?

Integration library is guilty: Use face SDK in an insecure way

Face service provider is culpable: Leave insecure option to apps Contain design flaws as well

37

#BHUSA @BlackHatEvents

## Slide 38

# Let's do hooking,  but there's anti-xxx

Anti-root Anti-anti-root Magisk + Shamiko <u>https://lsposed.org</u> fridantiroot frida --codeshare dzonerzy/fridantiroot

Anti-debug Anti-anti-debug Modified Frida with characteristics removed _e.g.,_ "re.frida.server" frida early hook _e.g.,_ libc hook to bypass TracerPid detection <u>[Link to a great blog post]</u>

#BHUSA @BlackHatEvents

38

## Slide 39

# Where to hook?

We can enumerate loaded class methods But they are renamed (ProGuard)

Which method is the onComplete() method we saw in SDK code and wanted to hook?

#BHUSA @BlackHatEvents

39

## Slide 40

# Deobfuscate by Signature

By matching arguments and return types, we can find mapping between renamed class/methods/fields with those in the SDK

#BHUSA @BlackHatEvents

40

## Slide 41

# Replace Attack: Data Format To replace result image, you must know exact resolution and image format

Crop victim's image to exact size / orientation

YUV image
(Android Camera)

#BHUSA @BlackHatEvents

41

## Slide 42

# Replace Attack: Data Encryption

This app just does encryption in Java

Others try to hide it in Native library

#BHUSA @BlackHatEvents

42

## Slide 43

#### **Black Hat Sound Bytes**

AI (security) is fancy, but system security still needs attention

You are at risk even if you've been avoid using face recognition in apps Urgent need of industrial standard on secure mobile (app) face recognition systems

@sanebow

More Questions?

#BHUSA @BlackHatEvents
