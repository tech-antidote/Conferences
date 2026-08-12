---
title: "Voice Phishing Syndicates Unmasked An In-Depth Investigation and Exposure"
speakers: ["Sojun Ryu", "YeongJae Shin"]
conference: "Black Hat"
conference_full: "Black Hat ASIA 2024"
edition: "ASIA"
year: 2024
source_pdf: "BlackHat ASIA 2024-Slides/Sojun Ryu & YeongJae Shin-Voice Phishing Syndicates Unmasked An In-Depth Investigation and Exposure.pdf"
pages: 77
sha256: "dc7d16bf329ecc68b6701e3c5e25357141d0dc0edf170a4174a61a0196b3b5a3"
text_chars: 22990
ocr_pages: 4
has_ocr: true
redacted_secrets: 0
ocr_confidence: 83.5
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T04:51:38Z"
---
# Voice Phishing Syndicates Unmasked An In-Depth Investigation and Exposure

**Speakers:** Sojun Ryu, YeongJae Shin  
**Conference:** Black Hat ASIA 2024  
**Source:** `BlackHat ASIA 2024-Slides/Sojun Ryu & YeongJae Shin-Voice Phishing Syndicates Unmasked An In-Depth Investigation and Exposure.pdf` (77 pages)


## Slide 1

### Voice Phishing Syndicates Unmasked: An In-Depth Investigation and Exposure **Sojun Ryu(S2W Inc.), Yeongjae Shin(Ex-S2W Inc.)**

#BHASIA @BlackHatEvents

## Slide 2

###### **Index**

**1. Background**

**2. Overview**

**3. Attack infrastructure provided as SaaS**

**4. SecretCalls**

**5. Automation**

#BHASIA @BlackHatEvents

## Slide 3

So-jun Ryu **Lead of Threat Analysis Team, @S2W**

- Tracking major ransomware and APT attack groups and identifying their TTP

- Interested and passionate about reverse engineering, threat intelligence, and incident response

**Career**

- Oct, 2020 ~: Threat Analysis Team, S2W TALON

- Dec, 2013 ~ Oct, 2020: KrCERT/CC, KISA

**Speaker of** {FIRSTCON, FIRSTCTI, Virus Bulletin, ISCR, DCC} **Social**

- **hypen1117@gmail.com**

**@hypen1117**

# BHASIA @BlackHatEvents

## Slide 4

##### Yeong-jae Shin

**Researcher of SRE Squad, at Goorm**

- Observability research and threat analysis on Cloud-native

- • Analysis of threat actors on cloud-delivered infrastructure

- • Compliance

###### **Career**

- Nov, 2023 ~: SRE Squad, at Goorm

- Mar, 2022 ~ Nov, 2023: Threat Analysis Team, S2W TALON

**Speaker of** {SIS, Virus Bulletin}

###### **Social**

- **teaf1001@naver.com**

**<u>Facebook Profile</u>**

**<u>Linkedin Profile</u>**

# BHASIA @BlackHatEvents

## Slide 5

# 1. Background

# BHASIA @BlackHatEvents

## Slide 6

#### 1. Background

- An extension of **"When Voice Phishing met Malicious Android App"** at Black Hat Asia in 2019.

- Voice phishing is **social engineering attack** over the **phone.**

- Discovered in the 2000s, **since** 2006 ~ **Today** in South Korea

- Main goal is to **extort money from the victims**

- With **native South Koreans** now occupying key positions, attack scenarios becoming **sophisticated** .

# BHASIA @BlackHatEvents

## Slide 7

#### 1. Background

**Statistics** for voice phishing victimization (Unit: 100M KRW, (= 75K USD)) Damage Amount Number of Victims

> '19 **6,720**

> '20 **2,353 18,265**

> '21 **1,682 13,213**

> '22 **1,451 12,816**

> '23 **1,965 11,503**

**50,372**

Source: Financial Supervisory Service

# BHASIA @BlackHatEvents

## Slide 8

#### 1. Background

###### **Statistics** for voice phishing victimization (Unit: 100M KRW, (= 75K USD)) Damage per victim

'19

**0.133**

'20

**0.129**

'21

**0.127**

'22

**0.113**

**0.171**

'23 **Fewer victims, but damage per victim has increased**

Source: Financial Supervisory Service

# BHASIA @BlackHatEvents

## Slide 9

#### 1. Background

2021 2022 2023
2023  type of voice-phishing 100%
• The rate of  Loan for Repayment 90%
662
has approximately  doubled 80%
70% 991
927
• The rate of
60%
Impersonation of Institutions
50%
692
has approximately  tripled
40%
Messenger Phishing
30%
521 311
Loan for Repayment 20%
611
10%
Impersonation of
213
170
Institutions
0%
x3
x2

Source: Financial Supervisory Service

# BHASIA @BlackHatEvents

## Slide 10

# 2. Overview

# BHASIA @BlackHatEvents

## Slide 11

#### 2. Overview – Group structure

Source: Seoul Eastern District Prosecutor's Office

- **Name: Minjun’s group (Name of Director)**

**Director/ December 2017 ~ December 2021 (5 yrs) Deputy director Probably cooperated 560 victims, 10.8 billion(KRW) IT Recruitment Call center department /Directing SIM-box/ Moving Bank Money Phones funds account Laundering Personal information Money withdrawal Burner bank Malicious account Laundering apps VoIP Current exchange** # BHASIA @BlackHatEvents

- **December 2017 ~ December 2021 (5 yrs)**

- **60 members**

- **560 victims, 10.8 billion(KRW)**

Call centers are in competition

## Slide 12

#### 2. Overview – Group structure

- **Name: Minjun’s group (Name of Director)**

- **December 2017 ~ December 2021 (5 yrs)**

- **60 members**

- **560 victims, 10.8 billion(KRW)**

**Director/ Deputy director**

Source: Seoul Eastern District Prosecutor's Office

Call centers are in competition

**IT Recruitment Call center department /Directing Moving Bank Money funds account Laundering**

# BHASIA @BlackHatEvents

## Slide 13

#### 2. Overview – Group structure

Source: Seoul Eastern District Prosecutor's Office

- **Name: Minjun’s group (Name of Director)**

**Director/ December 2017 ~ December 2021 (5 yrs) Deputy director 560 victims, 10.8 billion(KRW) IT Recruitment Call center department /Directing Moving Bank Money funds account Laundering Money withdrawal Burner bank account Laundering Current exchange**

- **December 2017 ~ December 2021 (5 yrs)**

- **60 members**

- **560 victims, 10.8 billion(KRW)**

Call centers are in competition

# BHASIA @BlackHatEvents

## Slide 14

#### 2. Overview – Group structure

Source: Seoul Eastern District Prosecutor's Office
Name: Minjun’s group (Name of Director)
Director/
December 2017 ~ December 2021 (5 yrs)
Deputy director
Probably cooperated
560 victims, 10.8 billion(KRW)
IT
Recruitment
Call center
department
/Directing
SIM-box/
Moving  Bank  Money
Phones
funds account Laundering
Personal
information
Malicious
apps
VoIP
# BHASIA @BlackHatEvents

- **Name: Minjun’s group (Name of Director)**

- **December 2017 ~ December 2021 (5 yrs)**

- **60 members**

- **560 victims, 10.8 billion(KRW)**

Call centers are in competition

## Slide 15

#### 2. Overview – Phishing theme

- **Impersonation**

   - Impersonation-themed dispatch of case documents

   - Send case documents by registered mail

- **Deception Methods**

   - Account used for criminal activities, investigation required

   - Downloading app for proceeding with investigation procedures

Seoul Central District Prosecutors' Office

Case number & Plaintiff’s name

Attacker’s number

Case documents sent by registered mail but returned

Seoul Central District Prosecutors' Office

# BHASIA @BlackHatEvents

## Slide 16

#### 2. Overview – Phishing theme

- **Loans for repayment** • Emergency livelihood support

   - **<u>Coronavirus-themed Government-backed low-interest refinancing</u>**

- **Deception Methods** • Demanding money to boost credit rating via transactions

   - Downloading loan app for contactless lending

Internet bank name

- The last loan of 2021 for low-income

You've been selected for a special offer.

<u>FCFS</u> Limit: 10M ~ 200M (KRW), Interest: 1.3% ~ 3.0%

**. . .**

Contact number & operating hours for consultation

# BHASIA @BlackHatEvents

## Slide 17

#### 2. Overview – Phishing theme

Internet bank name • **Coronavirus-themed** The last loan of 2021 **government loans/funds** • Emergency livelihood for low-income support • **<u>Government-backed</u>** You've been selected **<u>low-interest refinancing</u>** for a special offer. FCFS • **Deception Methods** Limit: 10M ~ 200M (KRW), • Demanding money to boost **Interest: 1.3% ~ 3.0%** credit rating via transactions • Downloading loan app for **INTEREST ON MY LOAN** contactless lending **AT THE TIME: 6.0%**

**. . .**

Contact number & operating hours for consultation

# BHASIA @BlackHatEvents

## Slide 18

#### 2. Overview – Attack scenarios

**Loans for repayment** Smishing / Call

**Impersonation**

Smishing / Call

**Impersonation using APK (Case 1)**

Smishing / Call

**Impersonation using APK (Case 2)**

Smishing / Call

**Scam / Extortion**

# BHASIA @BlackHatEvents

## Slide 19

#### 2. Overview – Attack scenarios

Loans for repayment
Smishing / Call
Introduce a loan
Demand fine / fee

**Scam / Extortion**

# BHASIA @BlackHatEvents

## Slide 20

#### 2. Overview – Attack scenarios

**Impersonation** Smishing / Call Threaten with involvement in a crime Induce to access to **fake site**

Show fake official documents Demand money for investigation / protection

**Scam / Extortion**

# BHASIA @BlackHatEvents

## Slide 21

#### 2. Overview – Attack scenarios

**Impersonation using APK (Case 1)**

Smishing / Call

Disguise as investigator via 2<sup>nd</sup> Call / Messenger

Induce to install an **APK** via IP /  Attachment

Using call forwarding, tricking a victim Demand money for investigation / protection

**Scam / Extortion**

# BHASIA @BlackHatEvents

## Slide 22

#### 2. Overview – Attack scenarios

**Impersonation using APK (Case 2)**

Smishing / Call Threaten with involvement in a crime Induce access to **fake site**

Show fake official documents

Induce to install an **APK** via IP Using call forwarding, tricking a victim Demand money for investigation / protection

**Scam / Extortion**

# BHASIA @BlackHatEvents

## Slide 23

#### 2. Overview – Attack scenarios

Source: Financial Supervisory Service, YTN

###### **1. Introduce as investigator**

OR

**2. Disclose criminal 3. Obtain passbook/ID arrests in your name on site**

**4. Ask if a victim or accomplice**

**5. Request to verify official docs for investigation**

**8. Encourage access to a 7. Mention about the specific IP address embargo**

**6. Request to access a portal site**

# BHASIA @BlackHatEvents

## Slide 24

## 3. Attack infrastructure provided as SaaS

# BHASIA @BlackHatEvents

## Slide 25

#### 3. Infrastructure

###### **Provider (Phishing site/APKs)**

**Voice phishing operator groups**

**Targets**

1. Pay

2. Give control over infra

3. Attack with the site/APK

4. Control infected devices

# BHASIA @BlackHatEvents

## Slide 26

#### 3. Infrastructure

• **Disguised as Supreme Prosecutor’s** 114.44.203.96 spo.go.kr **Office website** • Built completely (Real) (Provider A) identical sites • **3** providers supports this theme • Redirects to fake page for **querying** 114.43.215.82 156.247.15.245 **incidents** (Provider B) (Provider C) • Scenario: Impersonation / Impersonation (Case 2) # BHASIA @BlackHatEvents

# BHASIA @BlackHatEvents

## Slide 27

#### 3. Infrastructure

Provider A

AS 3462

(Supreme) (Seoul)

Official letter, Seizure & Search & Arrest Warrant SecretCalls

111.44.203.96 (Provider A)

# BHASIA @BlackHatEvents

## Slide 28

#### 3. Infrastructure

Provider B AS 3462

(South)

Official letter, Bank Statement, Non ~~-~~ Disclosure Agreement, Arrest Warrant SyncCalls

114.43.215.82 (Provider B)

# BHASIA @BlackHatEvents

## Slide 29

#### 3. Infrastructure

Provider C AS 133199

(Supreme)

Official letter, Arrest Warrant, Bank Statement MalCalls

156.247.15.245 (Provider C)

# BHASIA @BlackHatEvents

## Slide 30

#### 3. Infrastructure

(Provider B)

(Provider A)

Name of Prosecutor’s office with Case number, Target’s name, Severity, Date, Registrant,

Former Official Prosecutor General’s seal

(Provider C)

# BHASIA @BlackHatEvents

## Slide 31

3. Infrastructure (Provider C)

(Provider A) (Provider B) Arrest Warrant for Financial Crimes Issued by a Korean Court with Target’s Name & Registration number Fake account number, Detention Center & Period

# BHASIA @BlackHatEvents

## Slide 32

#### 3. Infrastructure

(Provider B)

###### Transaction History Inquiry Form (Provider C)

Account number (Suspended) & Inquiry Period

Inspector, Verifier, Recipient

# BHASIA @BlackHatEvents

## Slide 33

#### 3. Infrastructure

###### (Provider B)

###### Non-Disclosure Agreement

Attorney General, Case Director, Legal Officer, Investigator’s seal

# BHASIA @BlackHatEvents

## Slide 34

#### 3. Infrastructure – Pole-AntiSpy

SecretCalls (Provider A)

MalCalls SyncCalls (Provider C) (Provider B)

# BHASIA @BlackHatEvents

## Slide 35

#### 3. Infrastructure – Provider A

114.44.203.60 (FAKE)

play.google.com (REAL)

# BHASIA @BlackHatEvents

## Slide 36

#### 3. Infrastructure – Provider A

114.44.203.238 (FAKE)

play.google.com (REAL)

# BHASIA @BlackHatEvents


> Recovered by OCR — confidence 83/100 on the text kept, 51/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
bi
on
Infinigru Corporation
sb
Infinigru Corporation
24%
Infinigru Corporation
1.5%
Infinigru Corporation
3.3%
Infinigru Corporation
2.9%
Infinigru Corporation
2022. 6.2
1.5%
Infinigru Corporation
B Google Play Games Apps Movies Books -—_Kids
3.5% 100K+
408 reviews Downloads Rated for 3+ ©
[Add to wishlist
App support *«
© Website
+82234534620
© Support email
phishingeyes@gmail.com
O Privacy Policy
Similar apps >
Updated on
Jan 25, 2024
Tools
47%
V3 Mobile Security Anti-Virus
AhnLab Inc.
46%
```

## Slide 37

# 4. SecretCalls

# BHASIA @BlackHatEvents

## Slide 38

#### 4. SecretCalls

**2019 Average damage per attack**

(Unit: 100M KRW, (= 75K USD)) Source: Board of Audit and Inspection of Korea

1.45

x10

0.13

**Average damage of all attcks**

**Average damage of attacks when APKs used**

# BHASIA @BlackHatEvents

## Slide 39

#### 4. SecretCalls – Common VP Actions

**Data theft (photos, privacy)**

**Surveillance**

**Call redirect**

# BHASIA @BlackHatEvents

## Slide 40

#### 4. SecretCalls – Overview

**Call Forwarding**

**Anti Decompile**

**Encrypted Network Class File Behavior**

**Surveillance**

**Reddit Profile**

**File Structure C&C with FCM**

# BHASIA @BlackHatEvents

## Slide 41

#### 4. SecretCalls – Overview VP groups

|**Num**|**Family**|**Disguised as**|**DEX filename**|**Library(.SO)**
**filename**|**DEX Decryption**
**Method**|**C&C address location**|**C&C Endpoint OR Query**|
|---|---|---|---|---|---|---|---|
|1|**SecretCalls**|Police,
Anti-virus,
Banking|secret-classes[Num].dex
kill-classes[Num].dex
black-classes[Num].dex|libdn_ssl.so
libbbed.so
libset.so|AES-128-ECB|Hardcoded in DEX,
Hardcoded in Lib,
Get from Reddit|- postVal={data}
- a{timestamp}={data}|
|2|**MalCalls**|Banking,
Police,
Anti-virus,
Agency,
E-commerce|obfdex[Num].dex
obk[Num].dex|libbaiduprotec
t_sec_jni.so|AES-256-ECB|Google Drive|- /api/user/ping_server
- /api/user/get_extra_message
-/api/user/get_limit_phone_number|
|3|**SyncCalls**|Police,
Prosecutor's
office|sclasses.dex
yclasses.dex|libdex1.so
libdevaxfo.so|AES-128-ECB|Hardcoded in DEX|- /spy/Sync?imei=
- /spy/SyncConfig?imei=|
|4|**RcCalls**|Banking|classes1.dex|libopenssl.so|AES-128-ECB|Hardcoded in DEX|- {WebSocket}|
|5|**KKvoice**|Banking, Anti-
virus|lpt[Num].obfdex|-|Base64+XOR|Hardcoded in DEX|- /api/[random]/signal/[random]
- {WebSocket}|

# BHASIA @BlackHatEvents

## Slide 42

#### 4. SecretCalls – Anti decompile

1. Compression Method
2. Timestamp

8(Deflate)
07/04/2024

**frCompression: 17185 is not valid, we can fix it to 8(Deflate) frFileDate: Not so far from now**

# BHASIA @BlackHatEvents

## Slide 43

#### 4. SecretCalls – Anti decompile

###### **Fix header manually**

###### **Use open Source mins4416**

# BHASIA @BlackHatEvents


> Recovered by OCR — confidence 91/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
blackhat 4. SecretCalls = Anti decompile
apk_cure
Fixing dirty apk(zip) file header and AndroidManifest.xml in the archive.
Usage
$> python ./apk_cure.py -i source -o destination
Example
$> python ./apk_cure.py -i fsi.apk -o fsi_fixed.apk
Special Thanks
zipfile package! You've got a plan
Fix header manually Use open Source
C) mins4416
```

## Slide 44

#### 4. SecretCalls – File Structure

**1st Stage: Loader**

**2nd Stage: SecretCalls**

# BHASIA @BlackHatEvents


> Recovered by OCR — confidence 88/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
black hag 4. SecretCalls — File Structure .
Is
Resources SecretCal
iS Libraries (Internal)
SecretCalls Loader
(External)
1st Stage: Loader
Encrypted Native Encrypted
Class File Libraries Class File
2nd Stage: SecretCalls
```

## Slide 45

#### 4. SecretCalls – File Structure (1)

**Phishing resources: *. s** **z(zip) (pw: slal18sha)**

**Secretcalls: raw(*.apk)**

**SecretCalls Loader**

*slal18sha: **Korean profanity** (moxxer fxxxer)

# BHASIA @BlackHatEvents

## Slide 46

#### 4. SecretCalls – File Structure (2)

Phishing resources:
raw in assets
SecretCalls: *.sz(zip, separated)
(pw: slal18sha)

**SecretCalls Loader**

*slal18sha: **Korean profanity** (moxxer fxxxer)

# BHASIA @BlackHatEvents

## Slide 47

#### 4. SecretCalls – File Structure (3)

**Phishing resources: raw**

**SecretCalls: raw(*.apk)**

**SecretCalls Loader**

# BHASIA @BlackHatEvents

## Slide 48

#### 4. SecretCalls – Encrypted Class file

• Components of Each apps(Loader/SecretCalls) • Key elements for malicious activity • Decrypted / Loaded on memory in runtime • **Has changed to three different names**

**secretclasses.dex**

**killbalckclasses.dex classes.dex**

# BHASIA @BlackHatEvents

## Slide 49

#### 4. SecretCalls – Encrypted Class file

**kill-classes.dex**

**2021.01**

**2023.04**

**2023.10**

**NOW**

**1**<sup>**st**</sup> **secret-classes.dex**

**Balck-classes.dex 2**<sup>**nd**</sup> **Secret-classes.dex**

# BHASIA @BlackHatEvents

## Slide 50

#### 4. SecretCalls – Encrypted Class file

**Encrypted Decryption key stored in class file** Native Library **1**<sup>**st**</sup> **Secret** AndroidManifest.xml **Kill** Native Library **Balck** AndroidManifest.xml **2**<sup>**nd**</sup> **Secret** Native Library

**Native library(.so) name** libfirebase.so libset.so libbbes.so No use library libdn_ssl.so libbbed.so

# BHASIA @BlackHatEvents

## Slide 51

#### 4. SecretCalls – Encrypted Class file

**Encrypted class file**

**Key to decrypt class file (AES-128/ECB only)**

**key to decrypt extra C&C (AES-128/CBC only)**

**1**<sup>**st**</sup> **Secret**

**Kill**

**Balck**

**2**<sup>**nd**</sup> **Secret**

dbcdcfghijklmaop

xxxxefgaxxdecccc dasdefvvvxxxxyyy

dbcdcfghijklmaop

rb!nBwXv4C%Gr^84(KEY) 1234567812345678(IV)

PY06RguZ68k2as6v(KEY) 1862971933292829(IV)

# BHASIA @BlackHatEvents

## Slide 52

###### 4. SecretCalls – Network Behavior(Protocol)

**Client**

Server

##### **Websocket + HTTP**

# BHASIA @BlackHatEvents

## Slide 53

###### 4. SecretCalls – Network Behavior(Requests)

**App ID(key value) Device’s Information**

# BHASIA @BlackHatEvents


> Recovered by OCR — confidence 72/100 on the text kept, 47/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
pi&knat 4, SecretCalls - Network Behavior(Requests)
_, [ _] App ID(key value)
[ Device’s Information
appid: 11"
h23Rx8bLgTRoJ4QxJzC—bEGARLaDggdRNNGFpIxj 9UIQsYGiMC6c1xj @wsUXXWeTT",
rid: "60884692-0c48-4422-9fdc—ad14d06f2f62-11",
rinfo: "
rno: "+8201054584424",
sys: "Q"
```

## Slide 54

###### 4. SecretCalls – Network Behavior(Requests)

**a[timestamp]=[payload with encryption] (old)postVal=[payload with encryption]**

# BHASIA @BlackHatEvents

## Slide 55

###### 4. SecretCalls – Network Behavior(Requests)

###### **Type**

**behavior**

###### **Endpoint**

**2 Send device status 3 Extort new message ... ...**

**http://{C&C ip}/A3bh3/Vdc5**

**http://{C&C ip}/bC4d/v8N/Sop40**

**...**

**13 Send audio, image files http://{C&C ip}/a/bcF4c/Bdcm/.../vvbg Type 3 => http://{C&C ip}/bC4d/v8N/Sop40**

**[a-zA-Z0-9]{1,5} * 3**

# BHASIA @BlackHatEvents

## Slide 56

###### 4. SecretCalls – Network Behavior(Response)

**Client**

**Server**

**Config for malicious Behavior (e.g. call forwarding)**

# BHASIA @BlackHatEvents

## Slide 57

###### 4. SecretCalls – Network Behavior(Response)

Phone numbers
= to call redirection
Number list
for call blocking
Mode of Juphoon
for surveillance
Image upload server
Server status
Reddit profile
to get extra C&C

# BHASIA @BlackHatEvents

## Slide 58

#### 4. SecretCalls – Call Redirection

**Attacker’s number (** **pno) New Call**

Original Call

**The original call will be canceled, and a new call will be created. It may be difficult to notice**

# BHASIA @BlackHatEvents

## Slide 59

#### 4. SecretCalls – Call Redirection

**KB bank at Sanbon street(name) Real number of KB bank(fno)**

**Fake View**

**User sees a fake screen overlaid on top of the new call screen.**

# BHASIA @BlackHatEvents

## Slide 60

#### 4. SecretCalls – Extra C&C

###### **Username on Reddit**

***1A2B3C*** **_{Encrypted extra C&C address}_** ***4D5E6F* C&C on Reddit profile changes irregularly**

# BHASIA @BlackHatEvents

## Slide 61

#### 4. SecretCalls – FCM

**1. Send token 5. Send results**

**2. Get token from C&C**

**4. Forward command**

**3. Send command using FCM with token**

# BHASIA @BlackHatEvents

## Slide 62

#### 4. SecretCalls - Surveillance

**5. Create Session**

**1. Send ID**

**4. Request API Server**

**2. Get ID from C&C**

**3. Login to Remote app using ID**

# BHASIA @BlackHatEvents

## Slide 63

###### 4. SecretCalls – Custom App for Surveillance

**Login Input Juphoon ID** **Eavesdropping Camera Login (error) Eavesdropping fail! (error) input user ID Check your ID**

# BHASIA @BlackHatEvents

## Slide 64

# 5. Automation

# BHASIA @BlackHatEvents

## Slide 65

#### 5. Automation - Statistics

Collect Loader **64,000** + (including Secretcalls, it **doubles** )

Classified into **15+** target (theme)

# BHASIA @BlackHatEvents

## Slide 66

#### 5. Automation - Statistics

**Others e-commerce, courier services, video player, …** **11,200 Korean Banks** **8,588 33,274 National Police Agency** **11,383 Phishing Eyes**

# BHASIA @BlackHatEvents

## Slide 67

#### 5. Automation - Statistics

Others
e-commerce,
courier services,
video player, …
11,200
Korean
Banks 8,588 33,274 National
Police Agency
11,383
Phishing Eyes

# BHASIA @BlackHatEvents

## Slide 68

#### 5. Automation - Conclusion

**So, we...**

**ANALYZED OVER 99 PERCENT OF APKS AUTOMATICALLY**

# BHASIA @BlackHatEvents

## Slide 69

#### 5. Automation - Conclusion

• **C&C server 130+** • Most are placed in **HK > JP > KR > SG > others**

**South Korea(5+) Japan(50+) India(1) Hong Kong(70+) United States(1) Singapore(5+)**

# BHASIA @BlackHatEvents

## Slide 70

#### 5. Automation - Conclusion

• **malicious phone number 15+** • About 10% of them(2) were **Chinese** ,not Korean

**130, 156: China Unicom**

# BHASIA @BlackHatEvents

## Slide 71

#### Takeaways

- With cases of impersonation of institutions on the rise, it's important to **monitor and block their phishing sites** .

- IoCs alone may not be enough, their attack scenarios need to be **understood and disseminated.**

- • Need to track their infrastructure by extracting key information immediately **through automation**

# BHASIA @BlackHatEvents

## Slide 72

#### Takeaway - IoCs

**Phishing site Provider A Provider B Provider C** 114.44.203.96 114.44.215.128 156.247.15.245 114.41.74.75 114.44.215.163 208.87.202.44 111.253.228.97 114.43.215.82 45.207.51.254 111.253.207.49 114.43.215.197 45.207.51.229 61.223.147.45 114.43.212.118 45.207.54.115 61.223.140.235 114.43.195.191 45.207.54.114

# BHASIA @BlackHatEvents

## Slide 73

#### Takeaway - IoCs

**Provider A - Phishing site Phishing Eyes Supreme Prosecutor Consumer Agency** 114.41.64.218 111.253.216.161 111.253.215.49 111.253.198.50 111.253.220.43 61.223.157.84 111.253.200.198 111.253.246.44 114.41.75.234 111.253.238.95 111.253.247.9 114.41.79.203 61.223.143.191 61.223.129.229 114.41.80.221 61.223.139.252 114.41.76.156 114.47.71.228

# BHASIA @BlackHatEvents

## Slide 74

#### Takeaway - IoCs

**Provider A - SecretCalls Hash Reddit profile C&C** 99dbb222c7096c3bd759bbd49799523e Free-Breakfast-9220 43.202.65.81 0096dbf7aae99f71adaed0a05fd50bb8 WesternMastodon5235 154.19.69.67 d459471e7e64ba61e6592557f8d190e3 No_Double2876 38.181.2.17 305148cfd2598d04ec3afe84271e49f8 Legitimate_Peanut139 27.56.36.70 29d371239a57796983ce1dc639c3e40e CourseComfortable340 103.73.161.210 fd52ae1f3164deb1c9e1439b479c6bb5 Then-Lie-3539 103.97.178.69

# BHASIA @BlackHatEvents

## Slide 75

#### Takeaway - IoCs

**Provider A SecretCalls’ C&C**

27.124.36.74 38.181.2.49 149.104.49.43 38.181.2.83 149.104.49.44 154.19.69.75 149.104.49.46 198.176.60.87 149.104.49.49 103.186.215.103 13.124.202.35 137.220.245.13

137.220.245.14 137.220.245.18 137.220.245.26 137.220.245.37 137.220.245.38 137.220.245.45

# BHASIA @BlackHatEvents

## Slide 76

#### Q&A

**_Contact Sojun:_** _hypen@s2w.inc_ **_Yeongjae:_** _teaf1001@naver.com_

# BHASIA @BlackHatEvents

## Slide 77

Copyright ⓒ 2023, S2W Inc.
Special Thanks to  Young-hyun, Jeong  &

###### Special Thanks to **Young-hyun, Jeong** & Our Presentation Coach **Anant**

**About S2W**

**S2W** is a big data intelligence company specialized in hidden channels and cryptocurrencies.

**S2W** captures massive amount of data from various channels and conducts analysis with the unique AI based multi-domain analytics engine.

**S2W** Offers a threat intelligence solution **S2-XARVIS** , cryptocurrency anti-money laundering solution **S2-EYEZ** , digital fraud detection system **S2-TRUZ** .

**Contact**

For any queries, please contact

**info@s2w.inc**

**www.s2w.inc**

The information contained in this document is proprietary and confidential. If you are not the intended recipient, please note that any use or circulation of this document may be cause for legal action.

# BHASIA @BlackHatEvents
