---
title: "1.1 Million Cameras, One Wildcard Architectural Surveillance in an IoT Cloud"
speakers: ["Sammy Azdoufal"]
conference: "DEF CON"
conference_full: "DEF CON 34"
edition: "34"
year: 2026
source_pdf: "DEF CON 34/DEF CON 34 - Sammy Azdoufal - 1.1 Million Cameras, One Wildcard Architectural Surveillance in an IoT Cloud - nobody puts baby.pptx"
pages: 54
sha256: "56533fa0c79bb75782212870bfd6ea33407ba7d5632a448e183d1b0f6ab3e01c"
text_chars: 20450
ocr_pages: 54
has_ocr: true
redacted_secrets: 0
ocr_confidence: 89.3
ocr_unreliable_blocks: 0
content_note: "All 54 pages were rendered and read against the source deck by a vision model, and all 54 were rewritten. This deck is a Marp export: every slide is a single flat image with no text layer, so the entire document came from OCR. The ocr_* fields describe the superseded first-pass extraction."
vision_verified_pages_changed: 21
vision_verified_pages: 54
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T06:43:58Z"
---
# 1.1 Million Cameras, One Wildcard Architectural Surveillance in an IoT Cloud

**Speakers:** Sammy Azdoufal  
**Conference:** DEF CON 34  
**Source:** `DEF CON 34/DEF CON 34 - Sammy Azdoufal - 1.1 Million Cameras, One Wildcard Architectural Surveillance in an IoT Cloud - nobody puts baby.pptx` (54 pages)


## Slide 1

### 1.1 Million Cameras, One Wildcard

Architectural Surveillance in an IoT Cloud

DEF CON 34 · Main Stage  
Sammy Azdoufal · @xn0tsa  
Not a bug talk. A receipts talk.

1

## Slide 2

*Full-bleed poster: a world map built out of thousands of surveillance cameras, red beams converging on one glowing asterisk at the centre.*

**ONE WILDCARD**

```text
TARGET:
EVERYWHERE

PROTOCOL:
RTSP / HTTP

AUTH:
*

RESULT:
TOTAL ACCESS
```

```text
> scan.sh --global
> enumerate.py
> exploit.sh
> profit :)
```

```text
CONNECTED CAMERAS
1,100,000+
...AND COUNTING
```

**1.1 MILLION CAMERAS**

2

## Slide 3

DEF CON 34 · Main Stage

**“Most IoT talks end at the CVE.”**

This one starts after the patch.

Sammy Azdoufal · @xn0tsa

3

## Slide 4

DEF CON 34 · Main Stage

*Diagram: three interlocking rings — blue, purple, red — over the words "ONE THESIS".*

1. **TECHNICAL AUDIT** (12 CHAINS) — a numbered chain of links circling a robot with a magnifying glass
2. **DISCLOSURE OPS** (EMAILS · IPO · CONTRACT) — icon labels: IPO, CONTRACT
3. **RESEARCHER LESSONS** (BANK · PRETEXT · BACKDATING · GDPR) — icon labels: BANK, PRETEXT, BACKDATING, GDPR

OBSERVE. MAP. VERIFY.

**ONE THESIS**

**ARCHITECTURAL ACCESS, NOT A BUG LIST**

One thesis · three narratives: Audit · Disclosure ops · Researcher lessons.

Sammy Azdoufal · @xn0tsa

4

## Slide 5

DEF CON 34 · Main Stage

**“The vendor has by-design access to every customer’s camera.”**

Twelve independent chains.  
Patch one — access remains.  
Disclosure behavior is chain thirteen.

Sammy Azdoufal · @xn0tsa

5

## Slide 6

DEF CON 34 · Main Stage

### Three stories. One thesis.

|  | Narrative | What it proves |
| --- | --- | --- |
| 1 | Technical audit | Access is structural (12 chains — talk framing) |
| 2 | Disclosure ops | IR lag, backdating, the contract = evidence |
| 3 | Researcher lessons | Refuse the wrong instrument |

If you can recite this table at the end, the talk worked.

Sammy Azdoufal · @xn0tsa

6

## Slide 7

DEF CON 34 · Main Stage

SECTION 1 · 4 MIN · ORIGIN STORY

### How I got here

Light foil → civilian question → Hangzhou.

Sammy Azdoufal · @xn0tsa

7

## Slide 8

DEF CON 34 · Main Stage

### Previously, on MQTT…

Two months earlier: **DJI ROMO** — same MQTT ACL smell, ~7k devices.

$30k. **One-page invoice.** No novel. We move on.

Sammy Azdoufal · @xn0tsa

8

## Slide 9

DEF CON 34 · Main Stage

### Then a colleague asked

Amazon baby monitor.

“Is it safe?”

The box never names the cloud.  
So I bought the same one.

Sammy Azdoufal · @xn0tsa

9

## Slide 10

DEF CON 34 · Main Stage

### Same smell. Different ending.

**DJI** paid like adults. **Meari** sent a Chinese-law service contract for the same neighborhood of money.

This talk is about the second ending.

Sammy Azdoufal · @xn0tsa

10

## Slide 11

DEF CON 34 · Main Stage

SECTION 2 · 3 MIN

### Meet the sticker farm

Sammy Azdoufal · @xn0tsa

11

## Slide 12

DEF CON 34 · Main Stage

### Meari in one breath

Hangzhou ODM. Camera + firmware + cloud + app. Partners slap a logo.

CloudEdge · Arenti · BOIFUN · PetTec · SV3C · Joystek · Luvion · …

IPO background: listed **March 9, 2025** (ChiNext). Share price doubled after listing.  
Not a 2026 disclosure plot point — context.

Sammy Azdoufal · @xn0tsa

12

## Slide 13

DEF CON 34 · Main Stage

*Placeholder card drawn as a classified document: hazard-tape border, corner registration marks.*

Warning triangle, top left: **CLASSIFIED / LEVEL 4 / EYES ONLY**

**REDACTED**

CAMERA ASSEMBLY LINE — FACTORY PHOTO PLACEHOLDER

Bottom-left stamp: `DEF CON` / `//// 4` — bottom-right stamp: `FOUO` / `DO NOT DISTRIBUTE`

Factory / assembly-line photo goes here — where the stickers get born.

Sammy Azdoufal · @xn0tsa

13

## Slide 14

DEF CON 34 · Main Stage

### Brand test

Watch DNS. `*.meari.com.cn` → you’re in.  
The logo on the plastic is cosplay.

Sammy Azdoufal · @xn0tsa

14

## Slide 15

DEF CON 34 · Main Stage

*Split-screen poster: a green “EXPECTATION” panel on the left, a red “REALITY” panel on the right.*

**EXPECTATION**

MY CAMERA IS SECURE AND PRIVATE

- ☑ ENCRYPTED STREAM
- ☑ SECURE CONNECTION
- ☑ YOUR PRIVACY MATTERS

> SAFE. PRIVATE. YOURS.
>
> PEACE OF MIND ACTIVATED.

**REALITY**

ALL ROADS LEAD TO THE SAME FUNNEL

Sign over the loading bay: WELCOME, DEVICES. NO AUTH REQUIRED.

Checklist board:

- ✓ NO PASSWORD?
- ✓ DEFAULT PASSWORD?
- ✓ EXPOSED PORT?
- ✓ MISCONFIGURED?
- ✓ DOESN'T MATTER.
- ✓ WE TAKE ALL.

Funnel swallowing the camera conveyor: **ODM BACKEND**

Sign beside the funnel: ONE FLEET. ONE PIPE. ONE PROFIT. $

> **YOUR CAMERA: THEIR DATA.**
>
> **SCALE IS THE BUSINESS MODEL.**

**You bought a brand. You rented an ODM camera cloud.**

Sammy Azdoufal · @xn0tsa

15

## Slide 16

DEF CON 34 · Main Stage

*Poster: a baby monitor wearing a suit and tie sits on a nursery table in front of a server rack.*

**THE BOX SAYS BABY MONITOR**

Sticky note on the table: GOOD NIGHT, SLEEP TIGHT, WE <u>OWN</u> YOUR SITE ♡

Rack label: CLOUD

```text
meari/video/1        QoS 1
meari/audio/1        QoS 0
meari/ptz/1          QoS 1
meari/alert/motion   QoS 1
meari/status         QoS 0
meari/config         QoS 1

meari/#
```

Graffiti on the wall: THERE IS NO PRIVACY ONLY TOPICS — and a skull tagged `</>` over DEF CON

**THE CLOUD SAYS EVERYONE’S MONITOR**

**300+ logos. One SDK. One backend.**

Sammy Azdoufal · @xn0tsa

16

## Slide 17

DEF CON 34 · Main Stage

### 1.1M

devices · 118+ countries ·
registered at audit scale

Sammy Azdoufal · @xn0tsa

17

## Slide 18

DEF CON 34 · Main Stage

SECTION 3 · 15 MIN · EVIDENCE CHAINS

### Twelve chains. One access.

60–90 seconds each. Artifact →
“why this alone is enough.”

Sammy Azdoufal · @xn0tsa

18

## Slide 19

DEF CON 34 · Main Stage

> **How to listen to this section**
>
> Don’t collect CVEs like Pokémon.
>
> Ask once per chain: if this were the *only* finding — does the vendor still have a path to the camera?
>
> Twelve yeses = architecture.

Sammy Azdoufal · @xn0tsa

19

## Slide 20

DEF CON 34 · Main Stage

### Evidence board

**01–06** firehose · secret store · forever JPEGs · XOR costume · CMS · DingTalk SSO
**07–12** OpenAPI WAN-IP · TUTK · PIS bulk · RSA unbind · cloud-video (withdrawn) · static keys

Talk framing = **12 evidence chains**. CVE numbers at the end of this section — not the point of each slide.

Sammy Azdoufal · @xn0tsa

20

## Slide 21

*Full-bleed meme poster: a hoodie-wearing Pepe leans back at a desk in front of a browser window, confetti everywhere, glowing world-map panels on all four sides.*

**DEFAULT CREDENTIALS**

Map panels: NORTH AMERICA ONLINE · EUROPE ONLINE · SOUTH AMERICA ONLINE · ASIA / PACIFIC ONLINE

Browser window — tab: Customer Portal · address bar: `https://totally.secure.login`

```text
PLEASE SIGN IN

Username
admin

Password
public

✔ ACCESS GRANTED

Welcome, admin!
You now have full access to everything. 😎
```

Desk props: trophy “ZERO ALERTS CLUB” · mug “SECURITY? NAH.” · mug “IT WORKS ON MY MACHINE” · neon sign “HACKER OF THE MONTH*” with “* BY DEFAULT” · pizza box “DEPLOY & PRAY”

Sticky note on the laptop: TODO: · FIX LATER · ~~SECURITY~~

**IN PRODUCTION. ON FOUR CONTINENTS.**

21

## Slide 22

DEF CON 34 · Main Stage

### 01 EMQX — the welcome mat

Regional brokers (US-West · EU-Frankfurt · CN-Hangzhou · + Global/HK path).
Dashboards on `:18083`. Default `admin:public`. Auth plugins off.
Wildcard subscribe: yes. Anonymous: yes.

Alone: still a vendor path? **Yes.**

Wildcard topic on an authenticated free account = the firehose.
(Historical finding — don’t “try it from the hotel.”)

`14,204 msgs / 5 min · 2,117 devices · one free account`

Sammy Azdoufal · @xn0tsa

22

## Slide 23

DEF CON 34 · Main Stage

### 02 Apollo — secret vending machine

Port 8080. No auth.
**614** prod keys across 11 microservices: DB roots, Redis, MQTT globals, DingTalk, RSA unbind, OAuth…

Config server ≠ junk drawer. Apparently nobody told them.

Sammy Azdoufal · @xn0tsa

23

## Slide 24

DEF CON 34 · Main Stage

### 03–04 Pictures or it didn’t happen

**03** Shared OSS · no isolation · no expiry · URL on MQTT
**04** Baby/indoor `.jpgx3` = XOR first 1KB · SN in the same message

Calling XOR “encryption” is a lifestyle brand.

Sammy Azdoufal · @xn0tsa

24

## Slide 25

DEF CON 34 · Main Stage

*Placeholder frame styled as a classified document.*

Top-left stamp: DEF ☠ CON 31 · LAS VEGAS, NV · AUG 8-11, 2024

Top-right corner marks:

```text
// CLASSIFICATION
LEVEL: RED

// HANDLE VIA
NEED-TO-KNOW
```

**REDACTED**

BABY MONITOR ALERT FRAME — PLACEHOLDER

Bottom-left box: // INFORMATION IS POWER PROTECT IT (over a barcode)

Bottom-right: a faint hex dump [illegible], then STAY CURIOUS STAY SAFE beside a wireframe globe

**Real alert still goes here — faces / IDs redacted. Swap file when ready.**

Sammy Azdoufal · @xn0tsa

25

## Slide 26

DEF CON 34 · Main Stage

> **Encryption as a lifestyle brand.**
>
> SN in the clear. XOR on the
> first kilobyte. Fashion.

Sammy Azdoufal · @xn0tsa

26

## Slide 27

DEF CON 34 · Main Stage

*Placeholder contact sheet styled as a classified document: four empty frames, each carrying a red REDACTED stamp.*

Top-left header block:

```text
CLASSIFICATION: CONFIDENTIAL
HANDLING: RESTRICTED
DISSEMINATION: LIMITED
```

Top-right header block:

```text
DOC ID: A16-9X7
REV: 1.0
DATE: 2024-05-20
```

**AUDIT STILLS — COMING**

REDACTED · REDACTED · REDACTED · REDACTED

baby · doorbell · indoor · factory

Bottom-left box: PROPERTY OF AUDIT TEAM DO NOT DISTRIBUTE

Bottom-right: FOR AUTHORIZED PERSONNEL ONLY

**Montage slot: baby · doorbell · indoor · factory line.**

Sammy Azdoufal · @xn0tsa

27

## Slide 28

DEF CON 34 · Main Stage

### 05–06 Humans in the loop (the scary kind)

**05** CMS operator routes: live / playback / snapshot / cloud video…
**06** DingTalk creds in Apollo · **678** employees · SSO path into the console

Corporate chat as a door into the operator camera desk.

Sammy Azdoufal · @xn0tsa

28

## Slide 29

DEF CON 34 · Main Stage

> **SSO into the camera desk.**
>
> 678 employees. QR scan.
> Wrong blast radius.

Sammy Azdoufal · @xn0tsa

29

## Slide 30

DEF CON 34 · Main Stage

### 07–08 Serial → network path

**07** Hardcoded OpenAPI HMAC in every APK → **device status / WAN IP by serial**
**08** Universal TUTK authcode → direct P2P (cloud optional) — structural only

Alone: still a vendor path? **Yes.** Not a hotel CTF handout.

Sammy Azdoufal · @xn0tsa

30

## Slide 31

DEF CON 34 · Main Stage

### 09–12 Industrialize it

**09** PIS bulk P2P list — **1.16M US P2P rows (+98k Hangzhou)**
**10** RSA unbind private key (from Apollo)

**11** Cloud-video `/detail` — **withdrawn after re-test** (methodology lesson only)
**12** Static keys across every brand — rotate = break 1.1M devices

Alone: still a vendor path? **Yes** (11 kept as “how re-tests lie”).

Sammy Azdoufal · @xn0tsa

31

## Slide 32

DEF CON 34 · Main Stage

> **Twelve yeses.**
>
> That’s architecture. Not a
> CVE zoo.

Sammy Azdoufal · @xn0tsa

32

## Slide 33

DEF CON 34 · Main Stage

### The five that got numbers

CVE-2026-**33356** · **33357** · **33359** · **33361** · **33362**

runZero (Tod Beardsley) · CISA coordinated.

Five CVE IDs in the public writeup. Twelve chains = talk/audit framing (not a numbered board in the disclosure). Cloud-video withdrawn from CVE set; CN sig bypass too — Q&A if you care.

Sammy Azdoufal · @xn0tsa

33

## Slide 34

DEF CON 34 · Main Stage

### The map is not vibes

~826k devices by WAN IP.

When the architecture is the exploit,
the heatmap is the CVSS.

*Right half of the slide: a dark world heat-map of device density — one huge magenta bloom over Europe, further hotspots across West Africa, the Middle East, southern Africa, Madagascar, South America and the Asia/Pacific edge. Clipped basemap labels show through: “AFRIKA / أفريقيا” and “AMÉRICA DEL SUR”.*

Sammy Azdoufal · @xn0tsa

34

## Slide 35

DEF CON 34 · Main Stage

### Live bit / tape bit

1. **Tape:** 30s sanitized MQTT wildcard (PII redacted) — historical audit window
2. **Live:** EMQX dashboards **firewalled** 👏 (port block — `admin:public` never rotated)
3. **Residual (audit IR):** Apollo MQTT creds still worked on **3/4** brokers after dashboards went dark
4. **Apollo HTTP** 401 only as of **talk prep** — separate from the 5-day story

They patched the welcome mat. Kept the firehose keys.

Sammy Azdoufal · @xn0tsa

35

## Slide 36

DEF CON 34 · Main Stage

> **IR lag is a finding.**
>
> HK dashboards ~24h. US/EU
> ~5 days later. Apollo
> stayed open the whole
> assessment.

Sammy Azdoufal · @xn0tsa

36

## Slide 37

DEF CON 34 · Main Stage

SECTION 4 · 10 MIN · THE FUN PART (FOR LAWYERS)

### Disclosure ops

Emails as exhibits. Popcorn
optional.

Sammy Azdoufal · @xn0tsa

37

## Slide 38

DEF CON 34 · Main Stage

### Greatest hits playlist

| Beat | Line |
| --- | --- |
| Mar 2 | HK locks `:18083` in 24h — US/EU wait **5 days** |
| Mar 12 | “obsolete products” + $15k if I **delete the internet** |
| Mar 12–13 | I delete posts anyway (users > clout) · tone shift “unlawful” |
| Mar 15 | $30k offer + “technical partnership” article pitch + GDPR vibes |
| Apr 4 (Day 24) | Advisories published, **stamped Mar 2** (Wayback: lol no) |
| Apr 16→25 | PRC service contract → I refuse → one-page VDRA |
| May 11 | Full public disclosure |

Sammy Azdoufal · @xn0tsa

38

## Slide 39

*Full-bleed illustration: a hacker’s desk — a vendor “product discontinuation” email window on the left, a shopping cart heaped with the same cameras on the right.*

**VENDOR EMAIL**

Poster on the wall, top left: **DEF CON** (skull and crossbones).

Small monitor, left: `ALL YOUR BASE ARE BELONG TO LEGACY`

Email window:

> **IMPORTANT:** Product Discontinuation Notice
>
> Dear Valued Partner,
>
> Please be advised that the following products are now considered **obsolete** and will no longer be supported.
>
> We recommend migrating to our current generation solutions.
>
> Thank you for your understanding.
>
> Sincerely,
> Product Lifecycle Management Team
>
> ⚠ These products are end-of-life.
> No further updates or security fixes will be provided.

Red rubber stamp across the email: **OBSOLETE PRODUCTS**

Browser window on the right, cart badge **42**:

**Your Cart (42 items)** — stacked camera boxes tagged $199.99 · $149.99 · $89.99 · $249.99 · $179.99 · $159.99, several with **NEW!** starbursts.

Button: **PROCEED TO CHECKOUT**

Phone on the desk mat, bottom left: `DC30` (skull and crossbones). Purple graffiti stickers beside it: [illegible]

**ALSO STILL ON SALE**

39

## Slide 40

DEF CON 34 · Main Stage

> **The products affected are our obsolete products.**
>
> Amazon checkout still
> worked. Amazing
> obsolescence.

Sammy Azdoufal · @xn0tsa

40

## Slide 41

DEF CON 34 · Main Stage

### Backdating speedrun

Published **April 4**. Stamped **March 2**.
Nine days before first contact.

Wayback + DNS history: pages didn’t exist on Mar 2.
Covered **3 of 11** findings reported (not the full CVE set).
Apollo = “a limited amount of configuration information.”

archive.org = offensive security tool.

Sammy Azdoufal · @xn0tsa

41

## Slide 42

*Full-bleed photo-illustration: a desk under a lamp — a paid one-page invoice on the left, a chained-and-padlocked contract on the right.*

**SAME BOUNTY. DIFFERENT VIBES.**

Monitor, left:

```text
» FIND BUG
» WRITE REPORT
» GET PAID
» REPEAT
>_
```

Mug:

```text
REPORT BUGS
GET PAID
>_
```

Sticky note: GOOD BUG / GOOD CITIZEN / GOOD DAY ☑

**INVOICE**

| DESCRIPTION | AMOUNT |
| --- | --- |
| Vulnerability Report | $30,000 |
| TOTAL DUE | **$30,000** ✅ |

**MASTER SERVICES AGREEMENT**

THIS AGREEMENT IS INTENDED TO BE LEGALLY BINDING, COMPREHENSIVE, AND IMPOSSIBLE TO UNDERSTAND.

**PAGE 1 OF 40**

TABLE OF CONTENTS (ABRIDGED)

| Section | Page |
| --- | --- |
| 1. DEFINITIONS | 1 |
| 2. SCOPE | 7 |
| 3. LIMITATION OF EVERYTHING | 11 |
| 4. INDEMNIFICATION | 17 |
| 5. CONFIDENTIALITY | 23 |
| 6. NON-DISCLOSURE | 29 |
| 7. NON-DISPARAGEMENT | 31 |
| 8. GOVERNING LAW (BUT NOT REALLY) | 33 |
| 9. ARBITRATION (WE WIN) | 35 |
| 10. MISCELLANEOUS | 38 |
| 11. SURVIVAL | 40 |
| 12. AND SO ON | ∞ |

BY READING THIS, YOU AGREE TO EVERYTHING, INCLUDING THINGS THAT HAVEN'T HAPPENED YET.

Stamped across the contract: **NO PUBLISH**

Padlocks on the chain: GAG CLAUSE · PERPETUAL NDA · LIQUIDATED DAMAGES · VOID YOUR BOUNTY

Graffiti on the wall: YOUR BUG. OUR RULES. OUR SILENCE. OUR TERMS.

Coaster (skull): DISCLOSE? THINK AGAIN. WE DO.

Book: HOW TO SAY NO (AND LOSE YOUR BOUNTY) — VOLUME 1 OF ∞

Sticky note (skull and crossbones): TL;DR NOPE

42

## Slide 43

DEF CON 34 · Main Stage

### Same $30k neighborhood. Opposite movie.

**DJI:** one-page invoice. Paid.
**Meari:** Personal Service Contract —

- PRC law / Chinese courts
- Refund clause at *their* discretion
- No right to publish
- You eat the tax (incl. China)

That’s not banking. That’s a leash.

Sammy Azdoufal · @xn0tsa

43

## Slide 44

DEF CON 34 · Main Stage

*Photo-illustration: a smiling executive at a podium pulls back a curtain, revealing a burning data centre behind him where a man clutches his head and printed pages labelled "Art.33" and "Art.34" fly through the air.*

Speech bubble:

WE WILL STRICTLY ABIDE BY STANDARDIZED COMPLIANCE PROCEDURES

Backdrop banner:

SECURITY SUMMIT 2024

BUILDING TRUST THROUGH GOVERNANCE

Podium sign: RESILIENCE. TRUST. COMPLIANCE.

Screen in the burning room: SYSTEM FAILURE ⚠

Scattered pages: Art.33 / Art.34

**Art. 33 / 34 asked. Vibes answered.**

Sammy Azdoufal · @xn0tsa

44

## Slide 45

DEF CON 34 · Main Stage

### May 11 energy

Refuse the novel → propose one-page VDRA.
Public ships **5 CVEs + other findings + timeline** — not a numbered 12-chain board.
**Twelve chains** = talk / private audit framing. Publish. runZero · CISA.

The disclosure date was never the negotiation chip.

Sammy Azdoufal · @xn0tsa

45

## Slide 46

DEF CON 34 · Main Stage

SECTION 5 · 8 MIN · STEAL THIS

### Three lessons

Narrative 3. Screenshot fuel.

Sammy Azdoufal · @xn0tsa

46

## Slide 47

DEF CON 34 · Main Stage

### 1. “The bank needs a service contract”

**Test it.**

SAFE under $50k → invoice + purpose declaration.
Not a refundable no-publish PRC novella.

Side-by-side on screen: DJI form vs Meari contract.
Audience does the math.

Sammy Azdoufal · @xn0tsa

47

## Slide 48

DEF CON 34 · Main Stage

### 2. Backdated advisories are a lab method

1. Wayback the URL
2. DNS history
3. Vendor social announce
4. Email headers / first-fix date

If the stamp predates first contact: **say it with charts.**

Sammy Azdoufal · @xn0tsa

48

## Slide 49

DEF CON 34 · Main Stage

### 3. GDPR Art. 33 is a crowbar

EU data exposed + vendor won’t notify?
AEPD / CNIL don’t need your bounty contract.

File the week you publish.
The complaint is part of the research corpus.

Sammy Azdoufal · @xn0tsa

49

## Slide 50

DEF CON 34 · Main Stage

CLOSE · 5 MIN + Q&A

### What to remember walking out

Sammy Azdoufal · @xn0tsa

50

## Slide 51

DEF CON 34 · Main Stage

### Big picture, one more time

**Architectural / by-design access** — twelve independent chains (talk / private audit framing).

1. **Audit** — the chains (not the public CVE count)
2. **Disclosure ops** — evidence too
3. **Researcher lessons** — refuse the leash

Sammy Azdoufal · @xn0tsa

51

## Slide 52

*Full-bleed illustration: a world map built out of surveillance cameras, with red lines converging on a giant glowing asterisk at its centre.*

**ONE WILDCARD**

HUD panel, left:

```text
TARGET:
EVERYWHERE
PROTOCOL:
RTSP / HTTP
AUTH:
*
RESULT:
TOTAL ACCESS
```

Terminal, right:

```text
> scan.sh --global
> enumerate.py
> exploit.sh
> profit :)
```

Counter, lower right:

```text
CONNECTED CAMERAS
1,100,000+
...AND COUNTING
```

**1.1 MILLION CAMERAS**

52

## Slide 53

DEF CON 34 · Main Stage

> “Patch the bug.
> Keep the architecture.
> Call it remediated.”

Don’t clap for that.

Sammy Azdoufal · @xn0tsa

53

## Slide 54

### One wildcard. 1.1M cameras.

Sammy Azdoufal · @xn0tsa

Disclosure repo linked in the talk notes / QR

Questions that don’t create victims tonight

54

