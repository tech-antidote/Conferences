---
title: "Operation BlackEcho Voice Phishing Using Fake Financial and Vaccine Apps"
speakers: ["Hyeji Heo", "Sungchan Jang", "Byungwoo Hwang", "Jinyong Byun", "Kuyju Kim"]
conference: "Black Hat"
conference_full: "Black Hat ASIA 2025"
edition: "ASIA"
year: 2025
source_pdf: "Black Hat Asia 2025 Slides/Hyeji Heo & Sungchan Jang & Byungwoo Hwang & Jinyong Byun & Kuyju Kim_Operation BlackEcho Voice Phishing Using Fake Financial and Vaccine Apps.pdf"
pages: 81
sha256: "11678a32e7d2c38a1dfffe594873210dc6c0b584ffeec87b235d931586282454"
text_chars: 28281
ocr_pages: 3
has_ocr: true
redacted_secrets: 0
ocr_confidence: 83.7
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T03:54:07Z"
---
# Operation BlackEcho Voice Phishing Using Fake Financial and Vaccine Apps

**Speakers:** Hyeji Heo, Sungchan Jang, Byungwoo Hwang, Jinyong Byun, Kuyju Kim  
**Conference:** Black Hat ASIA 2025  
**Source:** `Black Hat Asia 2025 Slides/Hyeji Heo & Sungchan Jang & Byungwoo Hwang & Jinyong Byun & Kuyju Kim_Operation BlackEcho Voice Phishing Using Fake Financial and Vaccine Apps.pdf` (81 pages)


## Slide 1

# Operation BlackEcho :Voice Phishing using Fake Financial and Vaccine Apps

Speakers : Hyeji Heo, Sungchan Jang Contributors : Kuyju Kim, Jinyong Byun, Byungwoo Hwang

#BHAS   @BlackHatEvents

## Slide 2

## Speakers

사진

###### **Hyeji Heo**

- Security researcher at Financial Security Institute (2017~)

- Master’s degree from Chungnam National University (2015~2016)

- Responsible for analyzing and responding to Android malicious apps

###### **Sungchan Jang**

- Security researcher at Financial Security Institute (2019~)

- Security engineer at NCSOFT (2016~2019)

- Responsible for detecting and responding to phishing sites

2

#BHAS   @BlackHatEvents

## Slide 3

## Contributors

사진

###### **Kuyju Kim**

- Security researcher at Financial Security Institute

- Author of the report “Voice Phishing App Distribution Group Profiling”, published by FSI in 2022.

###### **Jinyong Byun**

- Security researcher at Financial Security Institute

###### **Byungwoo Hwang**

- Security researcher

   - & Malware analyst at Financial Security Institute

3

#BHAS   @BlackHatEvents

## Slide 4

## Outline

**1.** Background

**5.** Voice Phishing Scenario

**2.** Attack Flow

**6.** Countermeasure

**3.** Malicious Apps

**7.** Trend

**4.** Infrastructure

**8.** Conclusion

4

#BHAS   @BlackHatEvents

## Slide 5

# 1. Background

Operation BlackEcho :Voice Phishing using Fake Financial and Vaccine Apps

#BHAS   @BlackHatEvents

## Slide 6

## Understanding Voice Phishing

❖ Voice Phishing (a.k.a. Vishing)

   - ➢ A crime where scammers trick people over the phone to get money or personal information.

- ❖ Voice Phishing in South Korea (last 5 years)

※ **High-value damage cases**

Financial Government theme theme

※ [Reference] Korean National Police Agency

6

#BHAS   @BlackHatEvents

## Slide 7

## Why we did research

###### ❖ Malicious Apps

- ➢ **Malicious apps play a crucial role** in voice phishing attacks on smartphone users.

- ➢ These apps **intercept and block phone calls** , **tamper with call screens and call logs** .

❖ New Type of Malicious Apps

###### **Previous malicious apps**

###### **Current malicious apps**

**Normal apps (example)**

Financial theme app (malicious)

Evolution

(Separate its functions)

Financial theme app (malicious)

Vaccine theme app (malicious)

Imitation

Financial app (normal)

Vaccine app (normal)

7

#BHAS   @BlackHatEvents

## Slide 8

- Introducing Operation BlackEcho

- ❖ The criminal organization uses malicious apps **impersonating       financial** and **vaccine** apps for voice phishing

Install & Execute **Financial Vaccine (1st app) (2nd app)**

**2nd app installation ← Information theft ←**

**→ Voice phishing → Command execution**

- ❖ It also uses apps **impersonating       government agencies** for voice phishing, and creates **smishing** apps.

8

#BHAS   @BlackHatEvents

## Slide 9

# 2. Attack Flow

Operation BlackEcho :Voice Phishing using Fake Financial and Vaccine Apps

#BHAS   @BlackHatEvents

## Slide 10

## Attack Flow

Victim

**Victim’s Smartphone**

###### **SNS, text, calls, etc.**

Infrastructure

**Criminal organization**

**Affordable phone in the victim’s name**

10

**Bank**

#BHAS   @BlackHatEvents

## Slide 11

## ① Malicious App Distribution

**Victim**

2) Applying for a loan consultation

1) Advertising a loan **Criminal** 3) Distributing **organization** a loan app (malicious)

**SNS, text, calls, etc.**

11

#BHAS   @BlackHatEvents

## Slide 12

## ② Attacks

1) Installing
    malicious
Victim
Criminal
    apps 2) Giving
organization
    commands
(remote control,
data theft, etc.)
3) Processing
Infrastructure
    commands
Victim’s  4) Voice phishing
Smartphone

12

#BHAS   @BlackHatEvents

## Slide 13

## ③ Financial fraud

###### **Victim**

**Victim’s Smartphone**

- 1) Transferring /Withdrawing money

2) Swindling money

###### **Criminal organization**

13

**Bank**

#BHAS   @BlackHatEvents

## Slide 14

## ③ Financial fraud

**Victim**

1-2) Making **Victim’s** transactions **Smartphone** (remote control)

2) Swindling money

**Criminal organization** 1-3) Activating phone

**Affordable phone in the victim’s name**

14

**Bank**

1-3) Making transactions

#BHAS   @BlackHatEvents

## Slide 15

## What is next?

5. Voice Phishing
Victim
Criminal
organization
4. Infrastructure
5. Voice Phishing
3. Mal cious Victim’s
Affordable phone
Apps
Smartphone
 in the victim’s name

15

**Bank**

#BHAS   @BlackHatEvents

## Slide 16

# 3. Malicious Apps

Operation BlackEcho :Voice Phishing using Fake Financial and Vaccine Apps

#BHAS   @BlackHatEvents

## Slide 17

## History

❖ Malicious apps are implemented separately based on their functionality.

**December 2021 2022 ~ July 2023 July 2023 ~** Started (estimated) Separated (1st + 2nd) Separated (1st + 2nd_main + 2nd_call) **1st app** (Financial or Government theme, dropper/downloader + data theft)

**2nd app** (Vaccine theme, Voice Phishing + a) **2nd_main app** (Vaccine theme, control + data theft)

**2nd_call app** (Call theme, Voice Phishing)

17

<u>※</u> **<u>These malicious apps copied official apps’ icons.</u>**

#BHAS   @BlackHatEvents

## Slide 18

## 1st app

❖ Installing additional apps & stealing personal information

Name Phone number Social number Job Income Loan amount Address

Main screen Requesting Requesting Installing app Loan application Accessibility permission screen (data theft) permission #BHAS   @BlackHatEvents

18

#BHAS   @BlackHatEvents

## Slide 19

## 1st app - Screen Display

- ❖ The 1st app displays screens disguised as financial companies.

- ❖ And the screen display method has changed in three ways.

   - ① **Local html (~ June 2022)**

② **Layout** ③ **Phishing page (June 2022 ~) (April 2023 ~)**

19

#BHAS   @BlackHatEvents

## Slide 20

## 1st app - Screen Display

- ❖ The 1st app displays screens disguised as financial companies.

- ❖ And the screen display method has changed in three ways.

   - ➢ In the case of Local HTML, the app contains all the files to disguise.

###### **assets/data/web**

###### **assets/data/web/Stw**

###### **interface.html**

20

#BHAS   @BlackHatEvents

## Slide 21

## 1st app - Additional app Installation

- ❖ The 1st app installs 2nd, 2nd_main and 2nd_call apps.

❖ And the app installation method has changed from ‘drop’ to ‘download’.

###### ① **Drop (Before September 2022)**

###### ② **Download (After September 2022)**

(Dropper)
1st app
drops
file name unzip result
-
assets/mobilev3.apk
-
2nd app assets/huhu.apk
assets/apk.zip huhu.apk
assets/apk.zip plus.apk
assets/asdf/apk.zip huhu.apk

(Down-
downloads
loader)
1st app
Distribution server
2nd app

21

#BHAS   @BlackHatEvents

## Slide 22

## 1st app - Personal Information Theft

❖ The 1st app steals personal information by pretending to offer loan applications. **→** Name, Phone number, Social number, Company, Address, ID card, …

…

**Default Value in the loan applications Key Value** Name Hong Gildong Phone number 01052881200 Social number 820526-1234123

22

#BHAS   @BlackHatEvents

## Slide 23

## 2nd app

❖ Processing commands & Voice Phishing

Requesting Requesting Setting a default app Accessibility permission permission

Maintaining Processing a cmd. persistence (get PIN)

23

#BHAS   @BlackHatEvents

## Slide 24

## 2nd app - Command Processing

###### ❖ Command list

streaming control screen record

location

app file Accessibility

record

bluetooth album

voice phishing (enable, update phone numbers, end calls)

contact

sms

call log

24

2nd_main app

2nd_call app

#BHAS   @BlackHatEvents

## Slide 25

## 2nd app - Command Processing

❖ Custom Intent ➢ The 2nd, 2nd_main, 2nd_call apps handle commands through ‘custom intent’. (socket) command, parameter SocketService C2 server send  [custom intent] (HTTP) Send result SMSService (HTTP) Request data send  [custom intent] RestrictedNumbers for voice phishing Service send  [custom intent] CameraStream (RTSP) Streaming Service Streaming server

25

Malicious app

#BHAS   @BlackHatEvents

## Slide 26

## 2nd app - Command Processing

❖ Custom Intent

➢ The 2nd, 2nd_main, 2nd_call apps handle commands through ‘custom intent’. (socket) command, parameter SocketService C2 server send  [custom intent] (HTTP) Send result SMSService Malicious app

**SocketService** Receive commands “send_sms”

26

#BHAS   @BlackHatEvents

## Slide 27

## 2nd app - Command Processing

❖ Custom Intent

➢ The 2nd, 2nd_main, 2nd_call apps handle commands through ‘custom intent’. (socket) command, parameter SocketService C2 server send  [custom intent] (HTTP) Send result SMSService Malicious app

**SocketService** Send [custom intent] “com.dagger.rmc.intents.SEND_SMS”

27

#BHAS   @BlackHatEvents

## Slide 28

## 2nd app - Command Processing

❖ Custom Intent

➢ The 2nd, 2nd_main, 2nd_call apps handle commands through ‘custom intent’. (socket) command, parameter SocketService C2 server send  [custom intent] (HTTP) Send result SMSService Malicious app

**SMSService** Receive and handle [custom inten]) sendMessage()

28

#BHAS   @BlackHatEvents

## Slide 29

## 2nd app - Voice Phishing

❖ Malicious apps(2nd, 2nd_call) intercept or block calls

###### **Forced outgoing calls (‘Gangbal’)**

###### **Forced incoming calls (‘Gangsu’)**

###### **Blocking incoming calls (blacklist)**

‘A’ Bank ARS~
Outgoing Incoming
‘A’ Bank
‘A’ Bank
Victim
Victim ‘A’ Bank Victim ‘A’ Bank ‘A’ Bank
Attacker Attacker Incoming ‘A’ Bank
outgoing Incoming
‘A’ Bank ‘A’ Bank
Attacker Attacker Attacker
Call log Call log Call log
#BHAS   @BlackHatEvents

29

#BHAS   @BlackHatEvents

## Slide 30

2nd app - Voice Phishing ❖ Screens ➢ Malicious apps(2nd, 2nd_call) have their custom screens for voice phishing.

❖ Screens

Ca ll Sear ch Outgoing Incoming Call ended
‘A’ Bank ‘A’ Bank
02-XXXX-XXXX 02-XXXX-XXXX
Name
Phone number
Blocking Add to contact
Cancer Save
CustomDialerActivity DialerSearchActivity ContactActivity CallActivity CallActivity CallActivity
(outgoing call) (incoming call) (call ended) 30
#BHAS   @BlackHatEvents

## Slide 31

## 2nd app - Voice Phishing

###### ❖ ARS files

➢ Malicious apps(2nd, 2nd_call) play files when they intercept victims’ outgoing calls.

###### **ARS files (93)**

|**zip file name**|**unzip result**|
|---|---|
|website.zip|website/ars/*.mp3|
|nackvlaitje.zip|nackvlaitje/ars/*.mp3|
|menu_sound.zip|nackvlaitje/ars/*.mp3|
|123123.zip|nackvlaitje/ars/*.mp3|

###### **Phone numbers (368) - ARS files (93)**

**→** save them to the database (“rings” table)

31

#BHAS   @BlackHatEvents

## Slide 32

## 2nd app - Voice Phishing

- ❖ ARS files

➢ Malicious apps(2nd, 2nd_call) play files when they intercept victims’ outgoing calls.

###### **Phone number classification**

**Category Details** Government agency<sup>Financial, Investigative, Tax, and Other related agencies</sup> (FSC, FSS, SPO, NTS, KODIT, KINFA, KAMCO) 1st financial sector Banks Saving Banks, Insurance companies, Capital firms, Credit 2nd financial sector card companies  and Cooperative federations 3rd financial sector Other lending companies

32

#BHAS   @BlackHatEvents

## Slide 33

## 2nd app - Voice Phishing

- ❖ The victim is mapped with the attacker.

Criminal Organization

- ❖ AndroidManifest.xml in 1st app

   - ➢ app_id : App identifier

   - ➢ app_name : Keyword of financial companies

or government agencies

33

#BHAS   @BlackHatEvents

## Slide 34

## 2nd app - Voice Phishing

###### ❖ Phone numbers

- ➢ The malicious apps(2nd, 2nd_call) send the ‘app_id’ and request phone numbers to the C2 server.

   - ex) Visa card : The attacker pretends to be a Visa card employee.

■ ex) Financial Supervisory Service : The attacker blocks the victim from reporting voice phishing

###### **ex) Intercepting outgoing calls**

###### **ex) intercepting incoming calls**

###### **ex) blocking incoming calls**

Visa card

Visa card

Financial Supervisory Service

→ number : Outgoing call made by the victim

- → number_real : The app actually makes a call to the attacker

- → number : The app displays it to the victim → number_real : Incoming call to the victim

→ number : The app blocks the incoming call

###### **The attacker’s phone number**

34

#BHAS   @BlackHatEvents

## Slide 35

## Common Features

###### ❖ Update statistics

- ➢ Malicious app updates were frequently updated made on weekdays between 8:00 and 9:00 AM

###### **Number of malicious apps updates by day of the week Number of malicious apps updates by time**

35

#BHAS   @BlackHatEvents

## Slide 36

## Common Features

###### ❖ Packer

➢ Packers(DexProtector, AppSealing) are applied to malicious apps to hinder analysis.

- DexProtector (Lical) : Over 50%, applied to the entire period

■ AppSealing (INKA Entworks) : About 10%, applied from 2024.1. to 2024.5.

**AppSealing (10.03%)**

**DexProtector None (51.8%) (38.17%)**

Code example

Statistic

36

#BHAS   @BlackHatEvents

## Slide 37

## Common Features

❖ Keyword

**Huhu / whowho /** 후후

###### **● Code**

###### **● Api**

**Paekjo / dagger**

###### **● Certificate**

###### **● Custom Intent**

37

#BHAS   @BlackHatEvents

## Slide 38

# 4. Infrastructure

Operation BlackEcho :Voice Phishing using Fake Financial and Vaccine Apps

#BHAS   @BlackHatEvents

## Slide 39

Infrastructure
❖ Diagram
HTTP
① Landing page  ② Distribution Server
web browser
HTTP
③ Phishing page
HTTP
HTTP
HTTP
HTTP
④ Discovery server
1st App
HTTP
HTTP ⑤ C2 server
Socket HTTP
RTSP
2nd App
⑥ Streaming server

39

#BHAS   @BlackHatEvents

## Slide 40

## ① Landing page

❖ Role : Tricking victims into download the 1st app

❖ Features : It looks identical to the Google Play(Android’s official app store)

Smal Enterprise and Market Service Policy Fund Policy fund notification

40

Landing page (kmso)

Landing page (somin)

#BHAS   @BlackHatEvents

## Slide 41

## ② Distribution server

❖ Role : Distribution of malicious apps

❖ History : C2 server → File share & Hosting services → Distribution server

|History|Date|Type|File name||
|---|---|---|---|---|
|C2 server|2022.9.|①C2 server|huhu.apk||
|File-sharingservices|2023.1.|②catbox|[a-zA-Z0-9]{6}.apk|2d|
||2.|② gofile|huhu_[version].apk|n_app|
||6.||Security[version].apk||
|File-sharing, hosting services|7.|② gofile|Call.apk, Main.apk||
|(2nd → 2nd_main & 2nd_call)|12.|③dothome|Call.apk, Main.apk|2nd_call
|
||2024.3.|② gofile|Call.apk, Main.apk|&
2ndmain|
|Distribution server|7.|④Distribution server|Call.apk, Main.apk|_|

41

#BHAS   @BlackHatEvents

## Slide 42

## ③ Phishing page server

❖ Role : Personal information theft

❖ Features : Pretending to be a financial companies or government agencies.

‘User Information inquiry’ menu is added

Official homepage

Phishing page

42

#BHAS   @BlackHatEvents

## Slide 43

## ③ Phishing page server

❖ Role : Personal information theft

❖ Features : Pretending to be a financial companies or government agencies.

Phishing page Phishing page (‘My Information Lookup’) (‘My Usage History’)

Phishing page (‘Virtual Account Application’)

43

#BHAS   @BlackHatEvents

## Slide 44

- ④ Discovery, ⑤ C2, ⑥ Streaming server

- ❖ Role :

   - ➢ Discovery server  : Providing addresses of C2 server & Streaming server

   - ➢ C2 server             : Issuing commands, providing voice phishing data, and more.

   - ➢ Streaming server : Streaming camera / mic. / screen

44

#BHAS   @BlackHatEvents

## Slide 45

## Server address

###### ❖ Server address found in plaintext

➢ ① Landing page server, ② Distribution server, ③ Phishing page server

**Attacker Landing page server address** The attacker send it directly to the victim.

You should install the app. http://somin.2024tec.top/app.apk

**Distribution server address** The Landing page or the C2 server provides it.

###### **Phishing page server address**

It is hard-coded in the 1st app.

45

#BHAS   @BlackHatEvents

## Slide 46

## Server address

###### ❖ Server address found in plaintext

➢ Keywords and epoch time are used

**Attacker Landing page server address** → Keyword of the financial company You should install the app. ‘서민금융진흥원’ sounds like somin~ The attacker send it directly to the victim. http:/ /somin.2 024tec.top/app.apk **Distribution server address** The Landing page → epoch time or the C2 server provides it. (2024.7.24. 08:17:11.421 (KST)) **Phishing page server address** It is hard-coded in the 1st app. → Keyword of the financial company ( **I** ndustrial **B** ank of **K** orea)

46

#BHAS   @BlackHatEvents

## Slide 47

## Server address

- ❖ Server address found in encoded-text

➢ ④ Discovery server, ⑤ C2 server, ⑥ Streaming server

**Discovery server address** It is encoded and hard-coded in the apps

**C2, Streaming server** The discovery server provides them

**Decoding algorithm** Base64 + XOR (key : 17)

47

#BHAS   @BlackHatEvents

## Slide 48

## Server address

- ❖ Server address found in encoded-text

➢ Decoding with Base64 & XOR (key : 17)

**Discovery server address** It is encoded and hard-coded in the apps

**C2, Streaming server** The discovery server provides them

**Decoding algorithm** Base64 + XOR (key : 17)

**https://down.sinhan-bank.com/huhu https://down.ok-success.com/huhu**

**(       C2 server      ) https://ghdlwejkg30582.freemall-kr.top (Streaming server) rtsps://213.139.233.131:8322/live (Alternative server) https://www.nh-win.com**

48

#BHAS   @BlackHatEvents

## Slide 49

## Cloudflare

- ❖ The criminal organization uses Cloudflare

   - ➢ They can hide the IP and location of their servers.

   - ➢ Therefore, they can prepare for blocking and continue their malicious behavior.

|**Server**|**Example of server address**|**IP**|**Nation**|**Note**|
|---|---|---|---|---|
|Phishing page|site111.mallmaster[.]top|172.67.168[.]51, 104.21.26[.]2|-|Cloudflare|
|Phishing page|visakor[.]info, visakor[.]asia|8.217.194[.]83|HK|Alibaba US Technology Co., Ltd.|
|Discovery|down.sinhan-bank[.]com|172.67.134[.]184, 104.21.6[.]104|-|Cloudflare|
|Discovery|down.ok-success[.]com|172.67.170[.]125, 104.21.87[.]177|-|Cloudflare|
|C2|jhjdlkjeifhsl989.na333[.]top|172.67.168[.]210, 104.21.38[.]238|-|Cloudflare|
|Streaming|213.139.233[.]131|213.139.233[.]131|JP|Net Innovation LLC|
|Distribution|*.2024tec[.]top|172.67.141.[.]157, 104.21.94[.]238|-|Cloudflare|

49

#BHAS   @BlackHatEvents

## Slide 50

# 5. Voice Phishing Scenario

Operation BlackEcho :Voice Phishing using Fake Financial and Vaccine Apps

#BHAS   @BlackHatEvents

## Slide 51

## Scenario

❖ **Voice Phishing Crime Phases**

① **Access to victim**

- ② **Deceive victim**

- ③ **Temptation to install malicious app**

- ④ **Take control of the victim device**

⑤ **Take the victim's money**

51

※ **Scenario covering all voice-phishing malware, not just Operation BlackEcho**

#BHAS   @BlackHatEvents

## Slide 52

## ① Access to victim

- ❖ Attackers use various means to lure victims, for example, SMS, Facebook, instagram, etc ➢ They usually offer **unusually good terms on loans** or **threaten victims by posing as prosecutors.**

52

#BHAS   @BlackHatEvents

## Slide 53

## ② Deceive victim (1/2)

- ❖ Attacker disguises the process as a legitimate financial loan, and the **victim in need of money follows the attacker's instructions.**

   - ➢ The attacker asks the victim for sensitive documents containing personal information.

53

#BHAS   @BlackHatEvents

## Slide 54

## ② Deceive victim (2/2)

- ❖ Attackers use a variety of methods to disable the victim's cognitive abilities by pressuring the victim's mind.

- **1) Impersonating the social status of prosecutors, financial institutions to pressure victim**

   - In particular, ‘criminal involvement’ and ‘economic disadvantage’ are used to frighten victims.

- **1) Pressuring victims with time pressure and legal penalties**

   - Pressure victim to make a quick decision (ex : withdraw cash) in a short amount of time

- **1) Isolating the victim psychologically**

   - When installing the malicious app, the victim believes they are speaking to the police, financial institutions, etc. The victim is unable to speak to their family.

54

※ **Reference :** "A Study on the Process of Voice Phishing Crime in Korea" by Choi Kwan, Korean Police Studies Review, September 24, 2015

"Analysis of Institutional Impersonation Voice Phishing Scenarios: Focusing on Victims' Psychological Factors" by Lee Yong-soo, Korean Police Studies Review, June 2024#BHAS   @BlackHatEvents

## Slide 55

### ③ Temptation to install malicious app (1/2)

❖ Victim accesses a download page and installs a malicious app to apply for a loan.

➢ **South korea has a very developed mobile banking service** and many financial companies offer mobile apps.

55

#BHAS   @BlackHatEvents

## Slide 56

### ③ Temptation to install malicious app (2/2)

- ❖ If a malicious app is installed on phone, it can **steal phone history, contacts, and other information and control calling's functions.**

➢ **Control examples: block specific calls, manipulate outgoing calls, change contact information**

56

#BHAS   @BlackHatEvents

## Slide 57

### ④ Take control of the victim device (1/2)

❖ Attacker monitors everything about victim, **All calls are routed to the criminal organization.**

57

#BHAS   @BlackHatEvents

## Slide 58

#BHAS   @BlackHatEvents


> Recovered by OCR — confidence 77/100 on the text kept, 53/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
black hat
ASIA 2025
a Phone Number other party's qa
Control
Normal
ontro .
=P Outgoing
Control
<> Call blocking
icon Menu S'sBouacerosenos
```

## Slide 59

### Call Control Type - Forced outgoing calls

‘A’ Bank ARS~
Outgoing
‘A’ Bank
Victim ‘A’ Bank
Attacker
outgoing
‘A’ Bank
Attacker
Call log

① **The victim makes a call to ‘A’ bank.**

② **The malicious app plays an ARS file for ‘A’ bank, ends the outgoing call.**

③ **The malicious app initiates new call to the attacker, and changes the call screen.**

④ **After the victim finishes the call, the malicious app modifies the outgoing call log, from the attacker to**

**‘A’ bank.**

59

#BHAS   @BlackHatEvents

## Slide 60

### Call Control Type - Forced incoming calls

- ① **The attacker makes a call to the victim.**

Incoming
‘A’ Bank
Victim ‘A’ Bank

Attacker
Incoming
‘A’ Bank
Attacker
Call log

② **The malicious app changes the call screen to trick the victim into believing that the call is from ‘A’ bank rather than from the attacker.**

- ③ **After the call ends, the malicious app modifies the incoming  call log, from the attacker to ‘A’ bank.**

60

#BHAS   @BlackHatEvents

## Slide 61

#### Call Control Type - Forced incoming calls blocking

Victim ‘A’ Bank
Incoming ‘A’ Bank
Attacker
Call log

① **‘A’ bank makes a call to the victim.**

② **The malicious app ends the call from ‘A’ bank.**

③ **The malicious app deletes the incoming call log.**

61

#BHAS   @BlackHatEvents

## Slide 62

### ④ Take control of the victim device (2/2)

❖ Attacker monitors everything about victim, **All calls are routed to the criminal organization.**

62

#BHAS   @BlackHatEvents

## Slide 63

## ⑤ Take the victim's money

❖ Finally, attacker sends a **cash collector to collect the victim's money.**

63

#BHAS   @BlackHatEvents


> Recovered by OCR — confidence 82/100 on the text kept, 62/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
black hat
ASIA 2025
(6) Take the victim's money
“* Finally, attacker sends a cash collector to collect the victim's money.
©
Infected inl ? ih Infected phone
Phone List SFA location on
iam Google Maps
Google @ yee
f Control Server— Show Map Menu } 63
```

## Slide 64

# 6. Countermeasure

Operation BlackEcho :Voice Phishing using Fake Financial and Vaccine Apps

#BHAS   @BlackHatEvents

## Slide 65

## Phishing Kill Chain - Introduction

❖ To combat phishing crimes, including voice phishing, **we proactively take down phishing sites and voice phishing app download sites.**

65

#BHAS   @BlackHatEvents

## Slide 66

## Phishing Kill Chain - Detection

##### **Detection method**

- ❖ Phishing detection system

   - ➢ Blacklist IP Monitoring

   - ➢ URL pattern detection

- ❖ Use of external intelligence

   - ➢ Site pattern detection (Using API)

   - ➢ CTI Feed Integration

- ❖ Report from security officer

66

#BHAS   @BlackHatEvents

## Slide 67

## Phishing Kill Chain - Analysis

- ❖ **Collect**

   - ➢ Phishing Site html, Screenshot

   - ➢ Site info (ip, url, asn, country,.. etc)

- ❖ **Analysis**

   - ➢ APK info (Hash, Package name, App name)

   - ➢ App’s Control Server info (URL)

   - ➢ App’s Fake Phone Number (from hardcoding or Control Server communication)

67

#BHAS   @BlackHatEvents

## Slide 68

## Phishing Kill Chain - Response

- ❖ **Share**

   - ➢ Sharing information with financial and security companies through a sharing system called VFISS

      - (VoicePhishing Information Sharing System)

- ❖ **Report**

   - ➢ Report phishing sites to KISA (Korea Internet & Security Agency)

   - ➢ KISA asks South Korean ISPs to block

68

#BHAS   @BlackHatEvents

## Slide 69

## Sharing Info List

- ❖ Financial and security companies use this information to prevent voice phishing.

   - ➢ Malware app: App hash information, control server information, impersonation agency

   - ➢ Phishing Site : IP, URL, Impersonation agency, Screenshot

   - ➢ Therefore, they can prepare for blocking and continue their malicious behavior.

69

#BHAS   @BlackHatEvents

## Slide 70

### Korean Gov., Police, Financial Response

❖ With the rise in the prevalence of voice phishing crimes, **many industries are working to combat the crime.**

**Detecting malicious apps in financial apps**

**Voice Phishing Crime Task Force**

**V.P Integrated Reporting Centre**

#BHAS   @BlackHatEvents

## Slide 71

# 7. Trend

Operation BlackEcho :Voice Phishing using Fake Financial and Vaccine Apps

#BHAS   @BlackHatEvents

## Slide 72

## Trends

- ❖ As the pressure on voice phishing grows, **criminal organizations are moving to other phishing businesses.**

   - ➢ **The “balloon effect” is a situation where solving one problem creates another.**

name
phone
number
social
number name
phone
number
birth

Event (Paris Olympics)

Event (Gas ticket)

**We** **dding Invitation** #BHAS   @BlackHatEvents

72

## Slide 73

## Trends

- ❖ **South Korea has a very high smartphone penetration rate of 98%** , and mobile apps are used to make payments, buy and sell goods, and conduct various financial activities.

➢ Compared to voice phishing, Smishing and second-hand fraud are low-value and require relatively little time and labor.

73

#BHAS   @BlackHatEvents

## Slide 74

National Health Insurance"

## Trends - Smishing(1/2)

❖ While early smishing in South Korea was mostly about impersonating **delivery services and National Health Insurance** , there are now many different themes.

➢ Criminal organizations spread smishing texts to **match holidays or social issues.**

**Holiday pocket money**

###### **Obituary / wedding invitation**

###### **Administrative Fines**

74

#BHAS   @BlackHatEvents

## Slide 75

## Trends - Smishing(2/2)

❖ Recently, smishing in South Korea is basically using **shortened URLs** and creating phishing sites with **modern UIs that are specialized for mobile.**

- ➢ The main purpose of a smishing app is **to spread to the masses.**

(The Smishing app is lighter in function than the VoicePhishing app.)

75

#BHAS   @BlackHatEvents

## Slide 76

## Trends - Second-hand Phishing

- ❖ Korea has a number of active second-hand trading platforms such as “Joonggonara” and “Carrot”.

   - ➢ They trick you into depositing cash by pretending to be a secure payment.

#BHAS   @BlackHatEvents

## Slide 77

# 8. Conclusion

Operation BlackEcho :Voice Phishing using Fake Financial and Vaccine Apps

#BHAS   @BlackHatEvents

## Slide 78

## What can we do?

- ❖ People

- ➢ Install mobile antivirus apps and **don't download apps** from unknown sources

➢ **Be careful about providing personal information,** ID images, and credit information

- ❖ Investigative Agencies, Financial companies

   - ➢ **Share information** related to voice phishing with each other.

   - ➢ Analyze infrastructure related to malicious apps and work to prevent them in advance

   - ➢ Financial firms should operate a system that immediately **alerts or blocks suspicious transactions** on customer

accounts. (FDS).

78

#BHAS   @BlackHatEvents

## Slide 79

## Intelligence Report

- ❖ This report provides details about Operation BlackEcho

   - ➢ Crime Scenario

   - ➢ Malicious App Analysis

   - ➢ Network Analysis

   - ➢ Voice Phishing Analysis

- ❖ Additionally, it includes IoC and various artifacts to identify and respond to Operation BlackEcho.

QR코드

- ➢ IoC (Indicator Of Compromise)

- ➢ Files / SharedPreferences / Database / …

**You can download the report here.**

79

#BHAS   @BlackHatEvents

## Slide 80

## Black Hat Asia Sound Bytes

- ❖ Malicious apps are becoming increasingly sophisticated.

**Security researchers** must enhance their skills to analyze and respond to these apps.

- ❖ **Companies** and **agencies** should identify potential threats and respond accordingly. Collaboration between them can be beneficial.

- ❖ **Financial consumers** should learn how to protect themselves from financial fraud, including voice phishing.

Understanding the attack process and real-life cases can help strengthen their defenses.

80

#BHAS   @BlackHatEvents

## Slide 81

# Thank you

Financial Security Institute Hyeji Heo : heohj@fsec.or.kr Sungchan Jang : bsstudent23@fsec.or.kr

#BHAS   @BlackHatEvents


> Recovered by OCR — confidence 92/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ASIA 2025
Thank you
© Financial Security Institute
Hyeji Heo : heohj@fsec.or.kr
Sungchan Jang : bsstudent23@fsec.or.kr
#BHAS @BlackHatEvents
```
