---
title: "Gotta Phish 'Em All Novel Attack Techniques via Persistent Browser-in-the-Middle"
speakers: ["Giacomo Lenzini"]
conference: "DEF CON"
conference_full: "DEF CON 34"
edition: "34"
year: null
source_pdf: "DEF CON 34/DEF CON 34 - Giacomo Lenzini - Gotta Phish 'Em All Novel Attack Techniques via Persistent Browser-in-the-Middle - v2.pdf"
pages: 64
sha256: "031398127e8bc83fff917ca5c4c4ff8bba917d74c77da7dedaf8507b8ebd942a"
text_chars: 20773
ocr_pages: 10
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T00:20:26Z"
---
# Gotta Phish 'Em All Novel Attack Techniques via Persistent Browser-in-the-Middle

**Speakers:** Giacomo Lenzini  
**Conference:** DEF CON 34  
**Source:** `DEF CON 34/DEF CON 34 - Giacomo Lenzini - Gotta Phish 'Em All Novel Attack Techniques via Persistent Browser-in-the-Middle - v2.pdf` (64 pages)

## Slide 1

###### **Novel Attack Techniques via Persistent Browser-in-the-Middle**

**Giacomo Lenzini**

## Slide 2

##### **$ whoami**

###### **Giacomo Lenzini**

@GiacoLenzo2109

**Offensive Security Specialist @ Italy**

- ➔ Red Team & Adversary Emulation / Simulation

- ➔ Penetration Testing

- ➔ Vulnerability Research

**giacolenzo2109.github.io**

**giacomo-lenzini**

**GiacoLenzo2109**

2

## Slide 3

**1.**

**The State of Phishing Where It Breaks**

## Slide 4

**1.1 The State of Phishing The Adversary's Comfort Zone**

Submit Credentials
Victim

**Fake Login Page** Reverse Proxy / Credential Harvester

Token / Credentials

**Attacker**

4

## Slide 5

#### **Me, sending a standard phishing email and get reported**

5

## Slide 6

###### **1.2 The State of Phishing The Main Critical Limitations**

###### **Limited MFA Bypass**

Fails unless the victim is actively proxied in real time.

###### **Post-Login Visibility**

Zero visibility into the post-authentication session phase.

the

###### **Operator interaction**

No module dispatch, no live social engineering, no guided payload delivery.

6

## Slide 7

# **2.**

**Browser-in-the-Middle The Paradigm Shift**

## Slide 8

**2.1 Browser-in-the-Middle Attack Scheme that defeats MFA**

**Victim Browser**

Original Communication

**Attacker Browser**

Target Server

8

## Slide 9

**2.2 Browser-in-the-Middle Attacker Infrastructure Component Breakdown**

Remote Desktop
Protocol
Web-Based Client
BitM
Server
Protocol Bridge

9

## Slide 10

###### **2.3 Browser-in-the-Middle Victim Browser**

Web-based Client
<div id="screen">
<!-- Attacker Browser -->
</div>

10

## Slide 11

###### **2.3 Browser-in-the-Middle Victim Browser Example**

Victim
Attacker

11

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2.3 Browser-in-the-Middle
Victim Browser Example
€
ee - Sign in - Google Accounts} xX = +
>
¢
© Not secure | htéps://g009le.defcon lab/ft90bc47/2tid=IPnpR9-3AENCVeyXwiQ37a ~ Vietim
7
G
Sign in —_
Use your Google Account
Forgot email?
Not your computer? Use a Private Window to sign in. Learn more
about using Guest mode
English (United States) ~ Help Privacy Terms
11
```

## Slide 12

###### **2.4 Browser-in-the-Middle Attack Flow**

**1. Phishing Link Delivery**

Attacker Victim
1. https://gooogle.com
BitM Victim
Server Browser

Victim Browser

Attacker Browser

Legitimate Server

12

## Slide 13

###### **2.4 Browser-in-the-Middle Attack Flow**

1. Phishing Link Delivery

**2. Remote Browser Connection:** Instead of loading a fake cloned site, the victim instantly connect to a live, interactive stream of the attacker's remote browser.

###### Victim

Attacker

1. https://gooogle.com
2. https://gooogle.com
BitM Victim
Server Browser

Attacker Browser

Legitimate Server

**13**

## Slide 14

###### **2.4 Browser-in-the-Middle Attack Flow**

1. Phishing Link Delivery

2. Remote Browser Connection: Instead of loading a fake cloned site, the victim instantly connect to a live, interactive stream of the attacker's remote browser.

**3. Direct Target Interaction:** The attacker's remote browser communicates directly with the legitimate target website.

Attacker Victim
1. https://gooogle.com
2. https://gooogle.com
BitM Victim
Server Browser
3. https://google.com
Attacker  Legitimate
Browser Server

**14**

## Slide 15

###### **2.5 Browser-in-the-Middle Breaking the Hardened Web**

**Injections Blocked**

###### **Cookies Locked Down**

**Framing Neutralized**

15

## Slide 16

# **3.**

**Reinventing BitM A Research Journey**

## Slide 17

###### **3.1 Reinventing BitM The BitM Operational Gap**

###### **The Academic Blueprint**

- Remote Browser Stream

- Native MFA Bypass

###### **The Tactical Gap**

###### **The PoC Bottleneck**

- Single Victim

   - Non-Modular

- -

- Lack of stability No Persistence

17

## Slide 18

**3.2 Reinventing BitM The Engineering Problems Nobody Had Solved**

###### **Session Constraints**

- ❌ Logout invalidates victim’s session

###### **Client-side Desync**

- ❌ Static Metadata

- ❌ Isolated Clipboards

###### **Headless Browser Detection**

- ❌ Browser Fingerprints

18

## Slide 19

### **Time to level up…**

**Classic Phishing**

**Browser-in-the-Middle**

**???**

## Slide 20

**4.**

## **Persistent Browser-in-the-Middle Full Session Dominance**

## Slide 21

###### **_Challenges_**

- **The Foothold Challenge:** Transforming a volatile phishing session into a persistent browser-based control channel.

- **Real-Time Realism:** Eliminating interaction latency to flawlessly mirror a legitimate user experience.

- **Infrastructure Scalability**

- **Expanding the Offensive Surface:** Engineering novel attack vectors to automate and control live sessions.

   - **Weaponize Firefox extensions**

   - **Weaponize WebSocket channel**

21

## Slide 22

**4.1 Persistent Browser-in-the-Middle WebRTC Streaming Layer**

###### **High-Performance Transport**

- ✅ WebRTC Engine

- ✅ Low-Bandwidth Resilience

###### **Dynamic Resolution Mapping**

- ✅ On-the-Fly X11 Resizing

- ✅ Pixel-Perfect Canvas

###### **Near-Lossless Quality**

- ✅ Selkies Integration

- ✅ Zero-Delay Feedback

- ✅ Lossless Visual Stream

22

## Slide 23

**4.2 Persistent Browser-in-the-Middle WebRTC Streaming Layer  - Native Cursor Hijacking**

**BitM Selkies**

```
Linux Cursor
(X11/Debian Style)
```

Default Selkies behavior leaks the BitM host OS cursor style (e.g., Linux X11).

**JavaScript Hook**

**`Runtime Hooking`** `Hides base64 cursor` Drops the remote cursor graphics and strips server-side artifacts.

**Victim Browser**

```
Native Alignment
CSS Local Render
```

Client-side CSS maps standard properties (e.g. cursor: pointer) to force local OS rendering.

23

## Slide 24

**4.3 Persistent Browser-in-the-Middle WebRTC Streaming Layer  - Native Cursor Hijacking**

**1. Server-Side Decoupling:** Disabled the legacy server-to-client cursor update.

**2. Dynamic Client-Side Rendering:** Intercepted the victim's cursor state ( _curdata_ ) and dynamically injects the matching CSS cursor type.

24

## Slide 25

**4.4 Persistent Browser-in-the-Middle The WebSocket Control Channel**

**Attacker Server**

###### **Force Download Files**

Push and execute automated, silent file downloads on the target host.

###### **Client-side Sync**

Dynamically synchronizes the attacker’s browser tab title and favicon with the victim’s browser.

###### **Victim Browser**

###### **Real-time JavaScript Injection**

TLS WEBSOCKET (WSS) CHANNEL

Forces execution of arbitrary JavaScript commands directly inside the active victim’s browser and manipulating DOM.

25

## Slide 26

**4.5 Persistent Browser-in-the-Middle The WebSocket Control Channel - Client-side Sync**

**BitM Attacker Browser** `Victim Navigation Interception` Captures victim’s navigation, tab states, and URL changes in real time.

```
WebSocket
```

```
Send title/favicon
```

**Victim Browser** `Real-Time Client Synchronization` Instantly forces matching tab titles and favicons on the client side.

26

## Slide 27

###### **4.6 Persistent Browser-in-the-Middle Absolute Session Control**

###### **The BitM Advantage**

Owning the execution server grants unrestricted, real-time visibility over every interaction.

**Total Interaction Visibility**

###### **Operational Supremacy**

- **Native Keylogging**

   - **Active Session Takeover:** Allows the operator to take the full control over the victim’s session.

- **Victim Session Recording:** Enables real-time screen capture and full session recording.

27

## Slide 28

###### **4.7 Persistent Browser-in-the-Middle The Hardened Kiosk Jail**

###### **The Baseline BitM Strategy**

Forcing the victim into a hardened, single-application sandbox using native browser containment.

###### **The Operational Impact**

###### **The Lockdown**

- **No Address Bar & Navigation**

- - **No Window Controls**

- **Sandbox:** Forces interaction solely with the target application, preventing the victim from exiting the browser.

- **No Browser Menus (** toolbars, settings, and context menus)

- **Maximized Realism:** the session seamlessly mimics a native desktop.

28

## Slide 29

###### **4.8 Persistent Browser-in-the-Middle The Hardened Firefox Kiosk Jail**

###### **The Advanced P-BitM Strategy**

Moving beyond native Kiosk limitations to forge a surgically tailored, unbreachable browser environment.

###### **Engine Lockdown**

###### **Surgical UI Tailoring**

- **Enterprise Policies:** Disable default Firefox features and block dangerous internal protocols (like **`about:`** and **`file:///`** ).

- **Direct CSS Manipulation (userChrome.css):** Create a custom ad-hoc phishing browser.

- **User Preferences (user.js):** Force specific operational settings.

29

## Slide 30

**4.9 Persistent Browser-in-the-Middle Weaponizing Firefox Extensions**

**Server-Side Vantage Point**

Custom Firefox extensions

**Native Core**

Weaponizing standard API layers

###### **Total Traffic Governance**

Act as a proxy

30

## Slide 31

**5. P-BitM**

**The First Operational Framework**

## Slide 32

###### **5.1 P-BitM Core Infrastructure**

32

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
5.1 P-BitM
Core Infrastructure
ss
Attacker
ADMIN DASHBOARD
{e) {e) {e) fe)
fom) am) om fam)
Victim Victim Victim Victim
‘Traetik Proxy
(public)
© CAMPAIGN CONTAINER
ari
PUBLIC API
Tracking AP|_——- WebSocket
HOI—CHi<
2
‘(0
© CAMPAIGN CONTAINER
API
PUBLIC API
WebSooket
& VICTIM CONTAINERS
os ws
Victim, Victim
Container Container
os ws
Victim Victim
Container Container
& VICTIM CONTAINERS
os ws
Victim Victim
Container Container <—~
vs
Victim Victim
Container Container
32
```

## Slide 33

###### **5.2 P-BitM**

###### **Engineering a Scalable BitM Platform**

###### **Victim Containerization**

**On-demand isolation** : One isolated Docker container per target campaign and victim.

target

**Zero crosstalk** : Dedicated isolated browser with its own session state.

**APIs**

**REST:** Campaign orchestration and backend state automation.

**Data Channels:** Private endpoints to manage exfiltrated session state.

###### **WebRTC Streaming Layer**

**Selkies WebRTC:** High-performance real-time transport layer.

**Near-lossless latency:** Near-lossless visual stream for long-running sessions.

33

## Slide 34

**6. Operator Console & Live Session Control Puppeteering Live Targets**

## Slide 35

**6.1 Operator Console & Live Session Control Gophish-style Campaign Management**

**1**

**2**

**3**

**4**

###### **Target & Scheduling**

###### **DNS & SMTP**

###### **Tracking**

###### **Target Domain Binding**

Define user groups, target profiles, and automated launch windows for targeted campaigns.

Handle automated email delivery to initial targets using custom SMTP profiles and dedicated domains.

Continuous monitoring of email delivery, open rates, and malicious link interaction.

The platform spins up a headless browser instance and shares the remote desktop to the victim.

35

## Slide 36

###### **6.2 Operator Console & Live Session Control Admin Dashboard**

###### **Campaign Management**

Streamlines the creation, deployment, and tracking of targeted phishing operations from a centralized interface.

###### **Real-Time Session Control**

Provides live monitoring and direct interaction with active victim browser sessions as they happen.

###### **Modular Extension Engine**

Create custom Firefox extensions and tailored client-side modules to expand operational capabilities.

36

## Slide 37

**Time to show what P-BitM can actually do...**

## Slide 38

**6.3 Operator Console & Live Session Control Admin Dashboard - Campaign Creation + MFA Bypass – DEMO 1**

Attacker Victim

38

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
6.3 Operator Console & Live Session Control
Admin Dashboard - Campaign Creation + MFA Bypass — DEMO 1
foes ~ = wmoeivone
© Opetsee mepesn27 00 AKs/eampsions
Campaigns
No campaigns yet
Google Search Tm Feeling Lucky
38
```

## Slide 39

**6.4 Operator Console & Live Session Control Admin Dashboard - Real-Time Monitoring – DEMO 2**

Attacker Victim

39

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
6.4 Operator Console & Live Session Control
Admin Dashboard - Real-Time Monitoring - DEMO 2
(roe
© Oretsenee nipsin27.0.0.884s}areagrlcO38
1G Toggle Theme
> DEF CON 34
© e@scive DEF CON 34
Victim.defcon34@gmailcom
Live Session
‘racking ink
Q. Search victims
Export
Last Activity
Fy
> @norsecon mas fopogl eteon be Hc0S06ed=ORW OBE ZBAVUAKG
39
```

## Slide 40

## **7. Weaponizing Firefox Extensions**

**Native API Exploitation**

## Slide 41

**7.1 Weaponizing Firefox Extensions The Architecture of Firefox Extensions**

`DOM Access` **Content Scripts Web Page** `Native APIs` **Background Context Network / Storage / Downloads** `browser.webRequest browser.downloads browser.cookies`

41

## Slide 42

**7.2 Weaponizing Firefox Extensions Dynamic Credential Interception & Cookie Harvesting**

`POST /login` **Web Page / Login Form Target Auth Server** `Intercept Request Intercept Response Native APIs` **Creds & Cookie Background Context Exfiltration** `browser.webRequest.onBeforeRequest browser.webRequest.onHeadersReceived`

42

## Slide 43

###### **7.3 Weaponizing Firefox Extensions In-Flight Data Manipulation**

Web Page

Page Loading
Web Page with IBAN
Replace IBAN
Native APIs
Background Context
browser.tabs.executeScript

43

## Slide 44

**7.4 Weaponizing Firefox Extensions Preventing Sandbox Bypasses by Restricting Firefox Shortcuts**

**Web Page** `Keydown event`

```
Shortcut detected
```

**Background Context Prevent Shortcut**

44

## Slide 45

**7.5 Weaponizing Firefox Extensions File Hijacking & Download Interception**

```
Download Button
```

**Standard Download Stream** `Invoice.pdf Native APIs` **Background Context File Exfiltration & Manipulation** `browser.downloads` .onCreated

**Web Page**

45

## Slide 46

###### **7.6 Weaponizing Firefox Extensions File Hijacking & Download Interception – DEMO 3**

Attacker

Victim

46

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
7.6 Weaponizing Firefox Extensions
we barbneee = cr re
SIS ereisean mininzr.001s4a3janosonlecebecyictmaetoet © hetseae in beg don bese AbecredelAZanrsrMNOMA. JO
& Q a1sb3d
me to Drive
F) campaigns « Gage
https:/igoogle defcon.labidéfc:
172.217.23.67 con
Email Templates a)
Landing Pages
@ Live Control
Live Keylog n
SMTP Profiles
4 Modules
© Plugins
IN STARTED
13717:05:50. 458016+
00:00
Campaign: d4fcabéc | Victim: a15b3d2f
#2 Target Lists
[-—— 2026-07-13 17:06 1
ictim.defcon34 [shift] [shift] egmail.com
alt] [ctrl v
Toggle Theme
[-— 2026-0 ny
330584
[-— 2026-07-13 17:06:57 —]
46
```

## Slide 47

**7.7 Weaponizing Firefox Extensions Persistence Logout**

```
POST /logout
```

**Target Auth Server**

**Web Page**

```
Intercept Request
```

**Background Context**

```
Native APIs
```

**Deleting cookies to simulate logging out**

```
browser.webRequest.onBeforeRequest
```

47

## Slide 48

###### **7.8 Weaponizing Firefox Extensions Persistence Logout – DEMO 4**

Attacker

Victim

48

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
7.8 Weaponizing Firefox Extensions
Persistence Logout - DEMO 4
(Toe 2 tutes =
© > © Oretseaee ps7. 0018442 |ampsioneesetse4
2 < > Campaigns > DEF CON34
(© verse song dean abate sed Essa
F2 campaigns & enive DEF CON 34 stop campaign | , Export
“ 3 Created: 13.1ul2026, 19:45 © Duration: 26s
i emaiTenpates G
© Lninor a — Sign in
Use your Google Account
J SMTP Profiles
z ° caro
Victim defeon34@gmail.com
Forgot onal?
4 Modules o
ete cee Vor ts do toon Coe re
© Pus Live Session bout eig Guest mode
Target Lists
cron inte te) © 1 ry Tee
All Targets 2 Q Search victims. allstatus
Toggle Theme
status Vitim Tracking Link Fist Activity Last Activity
(> Logout
\ ict DEECON. Ss,
48
```

## Slide 49

**8. Hook like a BeEF Arbitrary JavaScript Execution via WebSocket Streams**

## Slide 50

###### **8.1 Hooking like a BeEF Old but Gold**

###### **Hardware & Environment Access**

**Persistent WebSocket Channel** Establishes a WebSocket channel allowing the operator to push dynamic, unconstrained JavaScript payloads directly into the victim's browser context in real time.

Abuses built-in HTML5 capabilities and native browser APIs to capture live media streams and harvest host environmental metadata.

50

## Slide 51

###### **8.2 Hooking like a BeEF The ClickFix Technique**

**Dynamic DOM Manipulation** : Overlaying the current page layout to inject highly realistic, context-aware error prompts or fake update alerts.

**Social Engineering Delivery** : Forcing the browser to display urgent operational instructions that prompt the user to execute malicious commands on their host system.

Victim

51

## Slide 52

###### **8.3 Hooking like a BeEF The ClickFix Technique – DEMO 5**

Attacker Victim

52

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
.3 Hooking like a BeEF
oo
Campaigns
Email Templates
Landing Pages
SMTP Prot
Modules
Plugins
Target Lists
Toggle Theme
4 Modu =
Attack Preset Library
CAMPAIGN MODULES
Fake KYC Verification
Credential Harvester
&
Network Scanner
Sane
© nestcun Hs pe een bse
alt] [etrul v
[-—- 2026-07-13 17:06:36
330584
— 2026-07-13
alt] [ctrl] [shift]
— 2026-07-13 17:07:17 —
alt) [ctrl] [shift]
® Cooki let
ClickFix
Execution param
e
52
```

## Slide 53

###### **8.4 Hooking like a BeEF The Fake KYC Bait**

###### **Real-Time Identity Harvesting** :

###### **Victim**

Injecting a rogue, convincing Know Your Customer (KYC) verification overlay to trick the user into allowing access to the webcam and microphone.

###### **Hardware API Hijacking** :

Programmatically invoking and controlling the victim’s webcam and media streaming capabilities directly through the WebSocket channel.

53

## Slide 54

###### **8.5 Hooking like a BeEF The Fake KYC Bait – DEMO 6**

Attacker

Victim

54

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
8.5 Hooking like a BeEF
= < a1sb3d
Campaigns < —
WM victim. defcon34¢gnail com
Email Templates to
Landing Pages
@ Live Control
SMTP Profiles
Modules
Plugins
Target Lists
Toggle Theme
https:/google.defcon lab/d4fes
Live Keylog © .
IN STARTED
13717:05:50. 458016+
Campaign: d4fcabéc | Victim: a15b3d2f
[-—— 2026-07-13 17:06
1
ictim.defcon34 [shift] [shift] egmail.com
alt] [ctrl v
[-— 2026-0
330584
[-— 2026-07-13 17:06:57 —]
yer aS
© vot seae sponge detente
me to Drive
54
```

## Slide 55

###### **8.6 Hooking like a BeEF Inline Injected Login Forms**

###### **Phishing-in-the-Middle** :

###### **Victim**

Injecting completely rogue authentication prompts or fake sessionexpired overlays directly over legitimate web apps.

###### **Credential Harvesting** :

Capturing username, password, and other sensitive contextual information in real time as the user interacts with the page.

55

## Slide 56

###### **8.7 Hooking like a BeEF Inline Injected Login Forms – DEMO 7**

Attacker

Victim

56

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
8.7 Hooking like a BeEF
(Tee 2 runes =
we, < alSb:
F_ Campaigns <
& Email Templates o
® Landing Pages
@ Live Control
J sMtP Profiles
4 Modules
© Plugins
#2 Target Lists
Toggle Theme
https:/google.defcon lab/d4fes
Export
[SESSION STARTED: 2026~07-
13717:05:50. 458016+00:0
Campaign: d4fcabéc | Victim: a15b3d2f
[-— 2026-07-13
shift] @gmail.com
ictim.defcon34
alt] [ctrl v
[-— 2026-07-13 17:06
330584
ance
© mesic hp apo een abet
56
```

## Slide 57

###### **8.8 Hooking like a BeEF Network Scanner- DEMO 8**

Attacker

Victim

57

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
8.8 Hooking like a BeEF
Network Scanner- DEMO 8
(Toe o cuss =
© > © Onetseare ms:27.09.1844a}arosoneaa0eyxnez6265735
campaigns
© Email templates
© Landing Pages
J SMTP Profiles
4 Modules
© Pisins
® Target Lists
© Console Modules
[attack Preset Library
(CAMPAIGN MODULES.
Fake KYC Verification
1G Toggle Theme ‘Sic Engrg tora
Logout
G
Hi Victim
°
Module Outs Data Fils 4, Upload Cooks [et Timetne
eter Sener ume
¢ snc
cconsnanct Sparen
Campaign: cfdd93b8 | Victim: 20265735
| 2026-07-12 19:26:27
1
att [ctr [shift
[— 2026-07-12 19:26:46 —1
ictim.defcon34 [shift] [shift] @ [shift] gmail.com
[2026-07-12 19:27:17 —]
[shift] Super [shift] Secret [shift] Password
— 2026-07-12 19:29:23 —]
fate)
Credential Harvester
resent ansing|
1 Horse stooge dtean abt 38/re-ONN_ be NZBEYUAG
G
Hi Victim
@ vecimactconsuegnatcon =
TD stow posers
57
```

## Slide 58

**9. Blue Teaming P-BitM Mitigating, Detecting, and Breaking BitM Frameworks**

## Slide 59

###### **9.1 Blue Teaming P-BitM Identifying Indicators of Compromise and Behavioral Anomalies**

###### **Anomalous Protocol Behavior**

###### **Geolocation Telemetry**

Flagging unexpected WebRTC session establishments originating from arbitrary web contexts and detecting persistent WebSocket traffic patterns.

session

Analyzing authenticated sessions originating from anomalous IP addresses immediately following a phishing interaction, and alerting on geographically inconsistent access patterns.

###### **Client-Side Content Integrity**

###### **Intentional IoCs**

Monitoring high-frequency JavaScript DOM mutation events indicative of modular injection frameworks, and detecting file hash mismatches resulting from in-transit download modifications.

Enforcing actively hunting for P-BitM's hardcoded infrastructure fingerprint embedded across all responses.

59

## Slide 60

**10. Future Roadmap Evolving the P-BitM Ecosystem**

## Slide 61

**10.1 Future Roadmap Evolving the Persistent Browser-in-the-Middle Ecosystem**

**Password Manager Spoofing**

**Chromium-based Support**

**AI-Driven Phishing Flows**

**Community-Driven Modules**

61

## Slide 62

**Open Source Core Release Empowering the Community with Deployable Frameworks**

## Slide 63

###### **Open Source Core Release**

**Evolving the Persistent Browser-in-the-Middle Ecosystem**

A core version of P-BitM designed to be immediately deployable and community-extensible will be released as open-source after DEF CON 34

**Core Framework**

**Base Modules & Firefox Extension**

**Documentation**

- **`$ git clone https://github.com/P-BitM-Framework/P-BitM`**

63

## Slide 64

## **Thanks DEF CON!**

**Giacomo Lenzini**

_GiacoLenzo2109@proton.me_ giacomo-lenzini
