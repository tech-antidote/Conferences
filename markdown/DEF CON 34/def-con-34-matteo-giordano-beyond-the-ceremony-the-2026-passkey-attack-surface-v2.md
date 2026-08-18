---
title: "Beyond the Ceremony The 2026 Passkey Attack Surface"
speakers: ["Matteo Giordano"]
conference: "DEF CON"
conference_full: "DEF CON 34"
edition: "34"
year: 2026
source_pdf: "DEF CON 34/DEF CON 34 - Matteo Giordano - Beyond the Ceremony The 2026 Passkey Attack Surface - v2.pdf"
pages: 100
sha256: "6e80a68dc4aa61a0e0fa1e3592941484c14766bab04abff73b2e68d265423f66"
text_chars: 45053
ocr_pages: 43
has_ocr: true
redacted_secrets: 0
ocr_confidence: 86.5
ocr_unreliable_blocks: 0
vision_verified_pages_changed: 88
vision_verified_pages: 100
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T06:41:37Z"
---
# Beyond the Ceremony The 2026 Passkey Attack Surface

**Speakers:** Matteo Giordano  
**Conference:** DEF CON 34  
**Source:** `DEF CON 34/DEF CON 34 - Matteo Giordano - Beyond the Ceremony The 2026 Passkey Attack Surface - v2.pdf` (100 pages)


## Slide 1

## Beyond the Ceremony

## **The 2026 Passkey Attack Surface**

Matteo Giordano

## Slide 2

**2**

Hand-drawn diagram. A tall phone-shaped outline labelled **Authenticator**, holding a bracketed key icon labelled **Private**.

## Slide 3

**3**

Hand-drawn diagram. The **Authenticator** phone outline holding the bracketed **Private** key icon, and — separately, at upper left, unconnected — a bracketed key icon labelled **Public**.

## Slide 4

**4**

Hand-drawn diagram. The **Public** key icon is now inside a blue rounded box labelled **RP**, which also shows an ellipsis (`...`) below the key. A plain line, with no arrowhead at either end, runs from the Public key in the RP box down to the right, to the **Private** key inside the **Authenticator** phone outline.

## Slide 5

**5**

Hand-drawn diagram. Same as the previous build, with a tall narrow rounded rectangle labelled **Client** drawn between the **RP** box and the **Authenticator**. The unarrowed line from the RP's **Public** key to the Authenticator's **Private** key passes behind the Client.

## Slide 6

**6**

Hand-drawn diagram. Same as the previous build — **RP** (holding **Public** and an ellipsis), **Client**, **Authenticator** (holding **Private**), joined by the unarrowed line — with a crowd of black human-figure icons added to the right of the Authenticator.

## Slide 7

**7**

Hand-drawn diagram, scaled up from the earlier builds. Three relying parties on the left, three clients in the middle column, two authenticators on the right, plus the crowd of human-figure icons. Dozens of shrunken copies of the whole diagram are tiled across the background.

- **RP** (blue box) — holds **Public** and an ellipsis (`...`)
- **RP2** (purple box) — holds **Public** and an ellipsis (`...`)
- **RP3** (orange box) — holds **Public** `1` and **Public** `2`
- **Client 1**, **Client 2**, **Client n** — three tall narrow rounded rectangles
- **Authenticator 1** — holds a blue **Private** key and a purple **Private** key
- **Authenticator n** — holds an orange **Private** `1` and an orange **Private** `2`

Connectors, all plain lines with no arrowheads at either end:

- Blue: RP's **Public** → **Client 1**, then on from Client 1 labelled **usb** → Authenticator 1's blue **Private**
- Purple: RP2's **Public** → **Client 2**, then on from Client 2 labelled **nfc** → Authenticator 1's purple **Private**
- Orange: RP3 (at **Public** `1`) → **Client 2**, then on from Client 2 labelled **ble** → Authenticator n's **Private** `1`
- Orange: RP3 (at **Public** `2`) → **Client n**, then on from Client n labelled **usb** → Authenticator n's **Private** `2`

## Slide 8

**8**

Same diagram as the previous build. Brand logos are now scattered across the slide, over and around the tiled background copies: a Google-coloured key mark, the 1Password keyhole mark, the Bitwarden shield, the iCloud cloud, and the Microsoft Entra ID diamond. No new text labels.

## Slide 9

**9**

Same diagram and logos as the previous build, with a large blue circular icon — an open padlock with an arrow curving clockwise around it — drawn over the crowd of human-figure icons.

## Slide 10

**10**

Same diagram as the previous build, with large browser and platform logos overlaid: the Google "G" and the Brave lion at top left/centre, the Chrome circle at mid left, the Apple logo at bottom left over the **RP3** box, and the Firefox logo at mid right. No new text labels.

## Slide 11

**11**

### **I'm not here with the scariest bug**

A wide outlined rectangle holds six labelled boxes in a row: **papers**, **CVEs**, **blog posts**, **talks**, **PoCs**, **threads**.

Six separate arrows, one from each of the six boxes, point down and inward into a single box below:

```text
ONE MAP
Let's give them a home
```

## Slide 12

**12**

### **whoami**

```text
matteo@defcon ~ % whoami --verbose
PublicKeyCredential {
  id:          "matteo-giordano",
  rpId:        "anvilsecure.com",
  userHandle:  "AppSec, offensive research, AI security, Italy",
  authData: {
    flags: {
      UserPresence: true,      // I'm here
      UserVerification: true,  // trust me, right?
    },
    signCount: 0               // first DEF CON talk.
  },
  attestation: { fmt: "none" }
}
```

Don't trust an identity just because the ceremony looked clean. So don't trust mine.

To the right of the terminal pane: a headshot photograph of the speaker, and below it an illustrated map of Italy with a location pin and the Colosseum.

## Slide 13

**13**

### **Passkeys already won-ish**

- **2025**

   - over 1B people have activated a passkey

   - ~15B accounts support them

   - <u>↗ FIDO World Passkey Day 2025</u>

- **2026**

   - ~5B in active use

   - 68% of orgs deploying passkeys for workforce auth

   - <u>↗ FIDO State of Passkeys 2026</u>

## Slide 14

**14**

### **But they almost never run alone**

- Only ~30% of orgs use passkeys as the **PRIMARY** method

- ~57% still lean on a **phishable** one

Four-panel webcomic on the right, signed `seebangnow`:

1. A pink figure alone — "I am all alone."
2. A blue capped figure puts an arm round them — "No you are not!"
3. Two blue capped figures flank the pink figure — "You still got us!"
4. Two blue figures hug the pink figure — "We are here for you!" One wears **SMS** on its back, the other **TOTP** on its cap.

## Slide 15

**15**

**"Passkeys Are Not Broken, The Conversation About Them Often Is."**

<u>↗ Nishant Kaushik, FIDO CTO, Sept 2025</u>

## Slide 16

**16**

### **It's everything else**

Hand-drawn diagram. A green box in the centre, captioned **CEREMONIES** above it, holds:

```text
REGISTRATION / AUTHENTICATION

sign > verify > sealed, proven,
        phishing-resistant
```

Seven pink/red boxes are scattered around it, unconnected — no arrows or lines are drawn:

- **enrollment** (above left of centre)
- **client** (top right)
- **PEBKAC** (left)
- **hybrid transport** (right)
- **relying party** (bottom left)
- **recovery** (bottom centre)
- **Cloud sync** (bottom right)

## Slide 17

**17**

### **What else?**

Hand-drawn flowchart of six boxes, connected by five single-headed arrows in a snake: the top row runs left to right, then down the right-hand side, then the bottom row runs right to left.

- **1. AUTHENTICATOR / PROTOCOL** → **2. Hybrid TRANSPORT** → **3. CLIENT**
- **3. CLIENT** → (downwards) **4. RELYING PARTY**
- **4. RELYING PARTY** → **5. CLOUD SYNC** → **6. USER RECOVERY**

- **Six** components, from *metal* to cloud

- Every passkey attack lives somewhere on this map

## Slide 18

### **Ceremonies**

Quick refresh

## Slide 19

**19**

### **Registration**

Hand-drawn sequence diagram with three participants, each named in a highlighted label: **Relying Party SERVER** (left, a bare lifeline), **Client** (centre — a bracket spanning two lifelines, **RP JS APP** and a paired **WEBAUTHN** / **BROWSER** column, with WEBAUTHN drawn in red), and **Authenticator** (right).

Messages, in the order numbered on the page:

- (1) `Auth request` — RP JS APP → Relying Party SERVER
- (2) `challenge, user info, RP info` — Relying Party SERVER → RP JS APP
- (3) `navigator.credentials.create` (written in orange) — RP JS APP → WEBAUTHN / BROWSER
- (4) self-loop on BROWSER, drawn as a hook returning into the bottom of the BROWSER lifeline
- (5) `hash(clientDataJSON), user info, RP info, RP ID` — BROWSER → Authenticator
- (6), (6.1), (6.2) self-loop on Authenticator
- (7) second self-loop on Authenticator
- (8) `attestationObject` — Authenticator → BROWSER
- (9) `attestationObject, clientDataJSON` — WEBAUTHN / BROWSER → RP JS APP
- (9) `attestationObject, clientDataJSON` — RP JS APP → Relying Party SERVER
- (10) self-loop on Relying Party SERVER

The multi-line annotations, as written:

```text
(4) clientDataJSON = {
        challenge,
        RP origin,
        "webauthn.create"
    }
```

```text
(6)   is User near?
(6.1) can User unlock?
(6.2) Creates the key pair
scoped to the RP ID
```

```text
(7) attestationObject = {
    hash(RP ID),
    flags = [
        UserPresence,
        UserVerification,
        Attested cred data,
        Extension data
    ],
    credential ID,
    public Key in CBOR,
    AAGUID,
    initial sig counter,
    extensions
}
```

```text
(10) verify as per [1]
and add credentials to
its storage
```

## Slide 20

**20**

### **Authentication**

Hand-drawn sequence diagram with the same three participants as the registration slide: **Relying Party SERVER** (left), **Client** (centre — **RP JS APP** plus the paired **WEBAUTHN** / **BROWSER** column, WEBAUTHN in red), and **Authenticator** (right).

Messages, in the order numbered on the page:

- (1) `Auth request` — RP JS APP → Relying Party SERVER
- (2) `challenge` — Relying Party SERVER → RP JS APP
- (3) `navigator.credentials.get` (written in orange) — RP JS APP → WEBAUTHN / BROWSER
- (4) self-loop on BROWSER, drawn as a hook returning into the bottom of the BROWSER lifeline
- (5) `hash(clientDataJSON), RP ID` — BROWSER → Authenticator
- (6), (6.1) self-loop on Authenticator
- (7) second self-loop on Authenticator
- (8) `authenticatorData + signature` — Authenticator → BROWSER
- (9) `authenticatorData + signature + clientDataJSON` — WEBAUTHN / BROWSER → RP JS APP
- (9) `authenticatorData + signature + clientDataJSON` — RP JS APP → Relying Party SERVER
- (10) self-loop on Relying Party SERVER

The multi-line annotations, as written:

```text
(4) clientDataJSON = {
        challenge,
        RP origin,
        "webauthn.get"
    }
```

```text
(6)   is User near?
(6.1) can User unlock?
```

```text
(7) authenticatorData = {
    hash(RP ID),
    flags = [
        UserPresence,
        UserVerification,
        Attested cred data,
        Extension data
    ],
    initial sig counter,
    extensions
}

(7.1) Signs the
authenticatorData
concatenated with the hash
of the clientDataJSON
```

```text
(10) verify as per [1]
and add credentials to
its storage
```

## Slide 21

**21**

### **Outer layers**

Hand-drawn diagram. In the centre, a hatched-fill box captioned **Passkey Ceremonies** above it, holding shrunken copies of the registration and authentication sequence diagrams from the previous slides.

- Left, under the heading **BEFORE the ceremony**: a rounded box reading **Registration bootstrap**, with the smaller line `"how'd you prove you, to enroll?"` below it. An arrow runs from this box rightwards into the Passkey Ceremonies box.
- Right, under the heading **AFTER the ceremony**: a rounded box reading **Session binding the cookie it mints**, with the smaller line `"bound to what?"` below it. An arrow runs from this box leftwards into the Passkey Ceremonies box.
- Below: an arrow runs down out of the Passkey Ceremonies box into a rounded box reading **Password-manager handoff**.

## Slide 22

**22**

### **Our map**

The same hand-drawn flowchart as the "What else?" slide, without the bullets: six boxes joined by five single-headed arrows.

- **1. AUTHENTICATOR / PROTOCOL** → **2. Hybrid TRANSPORT** → **3. CLIENT**
- **3. CLIENT** → (downwards) **4. RELYING PARTY**
- **4. RELYING PARTY** → **5. CLOUD SYNC** → **6. USER RECOVERY**

## Slide 23

**23**

### **Two planes**

Two labelled boxes side by side, each with its own bullets below it.

**RESEARCH** (orange box)

- Pick one actor, go deep.

- Mint CVEs / 0days and POCs

**ENGAGEMENT** (blue box)

- A pentester or red-teamer.

- Find out what was actually shipped following a methodology.

## Slide 24

### **The attack surface**

metal to cloud

## Slide 25

### **1. Authenticator and Protocol**

Researcher's turf

## Slide 26

**26**

### **You are here**

The six-box map again, with **1. AUTHENTICATOR / PROTOCOL** filled orange and a red map pin dropped on it.

- **1. AUTHENTICATOR / PROTOCOL** → **2. Hybrid TRANSPORT** → **3. CLIENT**
- **3. CLIENT** → (downwards) **4. RELYING PARTY**
- **4. RELYING PARTY** → **5. CLOUD SYNC** → **6. USER RECOVERY**

Legend below the map: **Research** (orange highlight) and **Engagement** (blue highlight).

**1/5**

**PROTOCOL** /  auth ·  transport ·  client ·  relying party ·  sync ·  user

## Slide 27

**27**

### **WebAuthn + CTAP**

###### **WHO**

- protocol designers and academics

- FIDO Alliance, W3C

###### **WHAT**

- prove the ceremony resists replay, MitM, forgery

- keep its privacy properties, endpoints assumed honest

###### **HOW**

- symbolic model checkers (ProVerif, Tamarin)

- hand-built computational proofs

- grab the specs, and go down the rabbit-holes

Below the WHO / WHAT columns: the four-panel "confused woman doing maths" meme, its panels overlaid with geometry and calculus formulae.

**2/5**

**PROTOCOL** /  auth ·  transport ·  client ·  relying party ·  sync ·  user

## Slide 28

**28**

### **The protocol holds**

- Computational proofs against forgery and replay

   - <u>↗ Barbosa et al. (CRYPTO 2021)</u>

   - <u>↗ Bindel, Cremers, Zhao (IEEE S&P 2023)</u>

   - Revisited recently as <u>↗ Barbosa et al. (PoPETs 2025)</u>

- Studies on vertical aspects

   - Attestation soundness by <u>↗ Bindel, Gama, Guasch, Ronen, ASIACRYPT 2023</u>

On the right: a film still of a man in a leather jacket in an office, captioned **HACKERMAN**.

**3/5**

**PROTOCOL** /  auth ·  transport ·  client ·  relying party ·  sync ·  user

## Slide 29

**29**

### **CTAP**

Hand-drawn diagram, two participants.

- Left, labelled **Client**: a red-outlined vertical box with **WEBAUTHN** written down it in red, and **BROWSER** written down it in black alongside.
- Right, labelled **Authenticator**: a rounded rectangle holding four bracketed key icons — **Private** (blue), **Private** (purple), **Private** `1` (orange), **Private** `2` (orange).
- Between them, a red dotted horizontal line labelled **CTAP** above it and **USB / NFC / BLE** below it.

**4/5**

**PROTOCOL** /  auth ·  transport ·  client ·  relying party ·  sync ·  user

## Slide 30

**30**

### **CTRAPS**

Three photographs in a row, captioned:

| | |
|---|---|
| CI1 - factory reset | photo of a security key inside a backpack pocket, a hand reaching in |
| AC1 - credential deletion | photo of a laptop screen running Electron Fiddle (see the console log below) |
| CI2 - user tracking | photo of a security key resting on the pocket of a pair of jeans |

The middle photograph shows an Electron Fiddle window (`Electron v25.2.0`, with **Stop** and **Console** buttons; menu bar `Edit  View  Window  Tasks  Show Me  Help`). Console output, every line time-stamped `12:31:53`:

```text
pinUvAuthParam
6d85be494a1ead7d7f2fca9080eb95fb77ab7aff2342396762382bb1df5c4ba8

=> Sent enumerateRPsBegin
---------------
PHASE: enumerateRPs
---------------
rp (userHandle)
{ id: 'webauthn.io' }
rpIDHash
74a6ea9213c99c2f74b22492b320cf40262a94c1a950a0397f29250b60841ef0

Total RPs found: 4.

=> Sent enumerateRPsGetNextRP
---------------
PHASE: enumerateRPs
---------------
rp (userHandle)
{ id: 'example.resident.com' }
rpIDHash
730260d41b3b8b8f9b541b35ae9a1e3daa43c4e8db5e51d66cadb4ccd07abdb7

RPs remaining: 2.

=> Sent enumerateRPsGetNextRP
---------------
PHASE: enumerateRPs
---------------
rp (userHandle)
{ id: 'anon.com' }
rpIDHash
b1ab969c891ab124688300577efd9e51f5a09948c4de982b5335fc8443a2363d

RPs remaining: 1.
```

The `pinUvAuthParam` value runs to the right-hand edge of the photograph, so it may continue beyond what is visible.

Below the console, the editor pane shows `index.html` and `main.js` (selected) under **Editors**, a **Modules** search box with `cbor 8.1.0`, and a **Main Process (main.js)** listing whose first visible line (1673) is clipped by the top of the pane and whose lines run off the right edge of the photograph:

```text
1674      // receive CTAP_INIT_RESP with CID.
1675      console.log("<= Received CTAP_INIT_
1676  CID = [0x00].concat([...data.subarr
1677
1678      console.log("\n=> Sent authenticato
1679      fidokey.write(CID.concat(
1680        [0x90,0x00,0x01,0x0b,0xa2],  // he
1681        [0x00,0x00,0x00,0x00,0x00,0x00,0x0
```

Taskbar entries: `Electron Fiddle`, `Attacks on CTAP2`, `Capturing from usbmon1`.

- <u>CTRAPS paper (Casagrande and Antonioli, EuroS&P 2025)</u> - <u>↗ DEF CON 33 talk</u>

- Toolkit: ↗ <u>github.com/Skiti/CTrAPs</u>

**5/5**

**PROTOCOL** /  auth ·  transport ·  client ·  relying party ·  sync ·  user

## Slide 31

**31**

### **Not all authenticators are equal**

| | **PLATFORM** (TPM, Secure Enclave) | **ROAMING** (key, phone) |
|---|---|---|
| **FIRST-PARTY** | iOS keychain, Windows Hello | Apple / Google phone |
| **THIRD-PARTY** | Microsoft Authenticator | YubiKey, Bitwarden |

**hardware** = secure-element backed

**software** = could fake user-pres / user-verif

**1/3**

protocol / **AUTH** ·  transport ·  client ·  relying party ·  sync ·  user

## Slide 32

**32**

### **Hardware authenticators under attack**

###### **WHAT**

- extract the private key

   - <u>↗ Ninjalab: Titan</u>

- clone the authenticator

   - <u>↗ Ninjalab: EUCLEAK</u>

###### **HOW**

- side-channel (EM/power to ECDSA nonce)

   - <u>↗ EUCLEAK (ePrint)</u>

- fault injection

   - <u>↗ NDSS 2024</u>

- invasive probing (decap, microprobing)

   - <u>↗ Ledger Donjon</u>

- firmware and supply-chain analysis

   - <u>↗ NDSS 2024</u>

**2/3**

protocol / **AUTH** ·  transport ·  client ·  relying party ·  sync ·  user

## Slide 33

**33**

### **Software authenticators' anarchy**

Screenshot of a web page.

**User Verification**

The following list of passkey providers have not implemented User Verification in a spec-compliant manner.

| Provider | Architecture | `uv=required` | `uv=preferred` |
|---|---|---|---|
| 1Password | Extension | ❌ Handles request without performing UV, sets UV true | ❌ Sets UV true without performing UV |
| 1Password | Native | ✅ Performs UV | ✅ UV flag accurate |
| Bitwarden | Extension | ❌ Handles request without performing UV, sets UV true | ❌ Sets UV true without performing UV |
| KeepassXC | Extension | ❌ Handles request without performing UV, sets UV true | ❌ Sets UV true without performing UV |
| Okta Personal | Extension | ❌ Handles request without performing UV, sets UV true | ❌ Sets UV true without performing UV |
| Okta Personal | Native | ✅ Performs UV | ✅ UV flag accurate |
| Proton Pass | Extension | ❌ Handles request without performing UV, sets UV true | ❌ Sets UV true without performing UV |
| Proton Pass | Native | ❌ Handles request without performing UV, sets UV true | ❌ Sets UV true without performing UV |
| Strongbox | Native | ❌ Handles request without performing UV, sets UV true | ❌ Sets UV true without performing UV |

> **Architecture**: `Extension` = web browser extension, `Native` = OS native app using provider APIs

"The following passkey providers have not implemented User Verification in a spec-compliant manner."↗ <u>passkeys.dev, known issues</u>

**3/3**

protocol / **AUTH** ·  transport ·  client ·  relying party ·  sync ·  user

## Slide 34

### **2. Hybrid transport**

Cross-Device Authentication (CDA)
BLE + WebSocket, or BLE-only

## Slide 35

**35**

### **You are here**

The six-box map again. **1. AUTHENTICATOR / PROTOCOL** is filled orange; **2. Hybrid TRANSPORT** is filled half orange (left) and half light blue (right), with the red map pin dropped on it.

- **1. AUTHENTICATOR / PROTOCOL** → **2. Hybrid TRANSPORT** → **3. CLIENT**
- **3. CLIENT** → (downwards) **4. RELYING PARTY**
- **4. RELYING PARTY** → **5. CLOUD SYNC** → **6. USER RECOVERY**

Legend below the map: **Research** (orange highlight) and **Engagement** (blue highlight).

**1/5**

protocol /  auth · **TRANSPORT** ·  client ·  relying party ·  sync ·  user

## Slide 36

**36**

### **Co-location vs intent**

Illustration: a laptop displaying a QR code on the left, a hand holding a phone whose camera app is framing the same QR code on the right.

- **1. Shows a QR Code** — above the laptop
- **2. Scan w/ camera** — arrow from the laptop to the phone, arrowhead at the phone end only
- **3. Reads the QR** — above the phone
- **4. BLE** (with the Bluetooth glyph) / **"we are near!"** — double-headed arrow between laptop and phone, arrowheads at both ends
- **5. Tap + Sign** — below the phone
- **6. Logged in** — below the laptop

**2/5**

protocol /  auth · **TRANSPORT** ·  client ·  relying party ·  sync ·  user

## Slide 37

**37**

Illustration with no title. A large hand-drawn ellipse encloses the whole scene; the label **BLE distance** sits below it.

- Top right, inside the ellipse: a laptop wearing red devil horns, showing a pink screen with a QR code, labelled **Attacker**.
- Centre left, inside the ellipse: a laptop showing a QR code with a hand-held phone in front of it, labelled **Victim**.
- A plain diagonal line, with no arrowhead at either end, runs between them, labelled **AiTM phishing**.
- A double-headed arrow, arrowheads at both ends, runs between the victim's phone and the attacker's laptop, labelled **4. BLE** (with the Bluetooth glyph) / **"we are near!"**.

**3/5**

protocol /  auth · **TRANSPORT** ·  client ·  relying party ·  sync ·  user

## Slide 38

**38**

**PoC**

Screenshot of a desktop, with two hand-drawn callouts on the right — **Attacker's laptop** (a horned laptop icon, arrow pointing left at the upper part of the screenshot) and **Victim's laptop** (a plain laptop icon, arrow pointing left at the lower part).

Left pane, a terminal titled `tmux attach`. Its prompt line carries icon segments (an Apple mark, a home icon and folder icons) before the path, and the right-hand segment reads `20.11.1  14:34:19`:

```text
 / ▸ / ▸ / ▸ / ▸/phishing    main
bun run src/attack/cli.ts                                              0
[14:34:43.083] INFO (#17): Waiting for demonstration that cross-platform attachment is fo
rbidden...
Press enter to continue...
```

Status line:

```text
0 Chrome   1 Apps   2 DB   3 Prisma Studio   4 Attack *   5 zsh -   2025-09-11 14:35
```

Top right, a Chrome window — tabs `New Tab` and `phishing-target.local:3000`, address bar `phishing-target.local:3000`, a `New Chrome available` button. The page reads:

**Target Website**

You aren't logged in yet

`Sign in`   `Sign in with Passkey`

Bottom right, a Safari window at `evil.local`:

**Definitely the target website** 😈

Waiting for QR code...

Demo: *"Phishing for Passkeys"* - M. Kuckuk, ↗ <u>inovex 2025</u>

**4/5**

protocol /  auth · **TRANSPORT** ·  client ·  relying party ·  sync ·  user

## Slide 39

**39**

### **Still open in 2026**

- **HiPass** measured the QR relay: 100% over 300 trials, 65s QR window across 10 major RPs (<u>↗ Kim et al., IEEE Access 2025</u>)

- **FIDO URI intent injection**: fixed in mobile browsers, but a father of the mobile FIDO-URI attack class (<u>CVE-2024-9956</u>, <u>↗ Righi 2025</u>)

- Proximity still stops **remote** attackers: PoisonSeed relayed remotely and failed at BLE (<u>↗ Expel retraction</u>)

- Co-located, it's workable: plant BLE boxes in range, offices/airports/conferences (<u>↗ Kniep 2025</u>)

- **No RP-side tell**: through CTAP 2.3 (Feb 2026), an RP still can't distinguish a relayed hybrid ceremony from a real one (<u>↗ FIDO spec</u>)

**5/5**

protocol /  auth · **TRANSPORT** ·  client ·  relying party ·  sync ·  user

## Slide 40

### **3. Client**

and Client-Side attacks

## Slide 41

**41**

### **You are here**

The six-box map again. **1. AUTHENTICATOR / PROTOCOL** is filled orange; **2. Hybrid TRANSPORT** and **3. CLIENT** are each half orange (left) and half light blue (right); the red map pin is dropped on **3. CLIENT**.

- **1. AUTHENTICATOR / PROTOCOL** → **2. Hybrid TRANSPORT** → **3. CLIENT**
- **3. CLIENT** → (downwards) **4. RELYING PARTY**
- **4. RELYING PARTY** → **5. CLOUD SYNC** → **6. USER RECOVERY**

Legend below the map: **Research** (orange highlight) and **Engagement** (blue highlight).

**1/7**

protocol /  auth ·  transport · **CLIENT** ·  relying party ·  sync ·  user

## Slide 42

**42**

### **Own the front door**

###### **WHO**

- browser vendors (Chrome, Firefox, Safari)

- extension devs (password managers)

- high-assurance RPs (fintech, gov)

###### **WHAT**

- UI transparency + user-consent awareness

- WebAuthn API override (activeTab)

- piggybacking

- risk-based-auth bypass resilience

###### **HOW**

- extension fuzzing (PoC malicious extensions)

- browser instrumentation (hook the API)

Below the HOW column, a two-panel Kermit meme:

> Me: I'm using Passkeys, my login is practically unbreakable now.
>
> Also Me: Installs 'Coupon Master Pro' browser extension that reads and modifies all website data.

**2/7**

protocol /  auth ·  transport · **CLIENT** ·  relying party ·  sync ·  user

## Slide 43

**43**

### **Attacker JavaScript forged a live Gmail passkey**

Screen recording still: Chrome on Windows, tabs `Extensions` and `Google Account`, address bar `myaccount.google.com/?utm_source=sign_in_no_continue`. The **Google Account** page shows the left nav (Home, Personal info, Data & privacy, Security, People & sharing, Payments & subscriptions, About), the greeting **Welcome, User Testing**, the line "Manage your info, privacy, and security to make Google work better for you. Learn more", the cards "Don't get locked out of your Google Account" (button `Add recovery phone`) and "Set a home address for your Google Account" (button `Set home address`), a `Search Google Account` box, the chips `My password` `Devices` `Password Manager` `My Activity` `Email`, and lower cards "Privacy & personalization" and "You have security tips". The Google apps grid is open on the right (Account, Drive, Gmail, YouTube, Gemini, Maps, Search, Calendar, News, Photos, Meet, Translate). The Windows taskbar clock reads `2:48 PM 8/10/2025`, weather `100°F Sunny`.

- <u>↗ attacker.passkey.tool</u>

- <u>↗ Passkey Raider</u>

- ...

- <u>↗ Passkey Editor</u>

Demo: SquareX, *"Passkeys Pwned"* - DEF CON 33 2025 (<u>↗ sqrx.com/passkeys-pwned</u>)

**3/7**

protocol /  auth ·  transport · **CLIENT** ·  relying party ·  sync ·  user

## Slide 44

**44**

### **Signed Assertion Hijacking**

Two sequence diagrams side by side, each with the participants **Authenticator**, **Client/Browser**, **Server**, **Database** (named in boxes at both top and bottom).

**Left diagram** — a red rectangle encloses the steps "Generate session ID", "Store challenge + session data" and "Challenge + Set-Cookie: sessionID", and a green tick sits inside that rectangle:

- `GET /login/passkey (username)` — Client/Browser → Server (solid)
- `Generate challenge` — Server self-loop
- `Generate session ID` — Server self-loop
- `Store challenge + session data` — Server → Database (solid)
- `Challenge + Set-Cookie: sessionID` — Server → Client/Browser (dashed)
- `navigator.credentials.get() - forward challenge` — Client/Browser → Authenticator (solid)
- `User verification` — Authenticator self-loop
- `Signing challenge` — Authenticator self-loop
- `Signed assertion` — Authenticator → Client/Browser (dashed)
- `POST /login/verify (assertion) + Cookie: sessionID` — Client/Browser → Server (solid)
- `Get public key + challenge + session` — Server → Database (solid)
- `Public key + original challenge + session` — Database → Server (dashed)
- `Verify signature + challenge + session` — Server self-loop
- `Generate session ID` — Server self-loop
- `Store session data` — Server → Database (solid)
- `HTTP 200 + Set-Cookie: sessionId` — Server → Client/Browser (dashed)

**Right diagram** — the red rectangle encloses "Generate challenge", "Store challenge" and "Challenge"; a red skull-and-crossbones tile sits to the right of the rectangle, outside it:

- `GET /login/passkey (username)` — Client/Browser → Server (solid)
- `Generate challenge` — Server self-loop
- `Store challenge` — Server → Database (solid)
- `Challenge` — Server → Client/Browser (dashed)
- `navigator.credentials.get() - forward challenge` — Client/Browser → Authenticator (solid)
- `User verification` — Authenticator self-loop
- `Signing challenge` — Authenticator self-loop
- `Signed assertion` — Authenticator → Client/Browser (dashed)
- `POST /login/verify (assertion)` — Client/Browser → Server (solid)
- `Get public key + challenge` — Server → Database (solid)
- `Public key + original challenge` — Database → Server (dashed)
- `Verify signature + challenge` — Server self-loop
- `Generate session ID` — Server self-loop
- `Store session data` — Server → Database (solid)
- `HTTP 200 + Set-Cookie: sessionId` — Server → Client/Browser (dashed)

<u>↗ Marek Toth, "DOM-based Extension Clickjacking", DEF CON 33 2025</u>

**4/7**

protocol /  auth ·  transport · **CLIENT** ·  relying party ·  sync ·  user

## Slide 45

**45**

### **DOM-based Extension Clickjacking**

1. The attacker **finds XSS** on a server **where passkeys are used**

2. **Inject** JS **malware**

   1. **Redirect signed assertion** to attacker's controller server

**5/7**

protocol /  auth ·  transport · **CLIENT** ·  relying party ·  sync ·  user

## Slide 46

**46**

### **DOM-based Extension Clickjacking**

- **Hide passkey dialog** UI injected by password manager (**uses DOM-based extension clickjacking technique**)

Screenshot: a cookie-consent dialog drawn on top of a semi-transparent passkey dialog.

The opaque, blue-bordered dialog in front:

**Privacy & Transparency**

We and our partners use cookies to Store and/or access information on a device. We and our partners use data for Personalised ads and content, ad and content measurement, audience insights and product development. An example of data being processed may be a unique identifier stored in a cookie. Some of our partners may process your data as a part of their legitimate business interest without asking for consent. To view the purposes they believe they have legitimate interest for, or to object to this data processing use the vendor list link below. The consent submitted will only be used for data processing originating from this website. If you would like to change your settings or withdraw consent at any time, the link to do so is in our privacy policy accessible from our home page.

Buttons: `Accept` (highlighted) and `Decline`.

The faded dialog behind it:

**Passkey sign-in**

Choose a saved passkey to sign-in to testpasskeys.com

**testpasskeys.com** — victim@victim.com

Close this window in order to use a security key or another passkey.

The `Accept` button of the front dialog falls exactly over the `testpasskeys.com` / `victim@victim.com` entry of the passkey dialog.

**6/7**

protocol /  auth ·  transport · **CLIENT** ·  relying party ·  sync ·  user

## Slide 47

**47**

### **DOM-based Extension Clickjacking**

4. The **victim** visits the URL with XSS vulnerability and **clicks once**

5. The attacker obtains the signed challenge

6. The **attacker sends the signed assertion** from their server **to the auth server**

**7/7**

protocol /  auth ·  transport · **CLIENT** ·  relying party ·  sync ·  user

## Slide 48

### **4. Relying party**

## Slide 49

**49**

### **You are here**

The six-box map again. **1. AUTHENTICATOR / PROTOCOL** is filled orange; **2. Hybrid TRANSPORT** and **3. CLIENT** are each half orange (left) and half light blue (right); **4. RELYING PARTY** is filled light blue throughout, with the red map pin dropped on it.

- **1. AUTHENTICATOR / PROTOCOL** → **2. Hybrid TRANSPORT** → **3. CLIENT**
- **3. CLIENT** → (downwards) **4. RELYING PARTY**
- **4. RELYING PARTY** → **5. CLOUD SYNC** → **6. USER RECOVERY**

Legend below the map: **Research** (orange highlight) and **Engagement** (blue highlight).

**1/37**

protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user

## Slide 50

**50**

### **On a high level**

- Trigger the ceremonies and analyze.

- Tampering, tampering, tampering

   - Fuzzing

   - Monkey tests, checklists

   - More nuanced assumptions

- <u>↗ Jannett et al., "State of Passkeys," 2026</u>

   - Actively tested 103 RPs

   - 103 vulnerable to at least one server-side attack.

   - 18 critical, 53 high.

On the right, the registration sequence diagram from earlier in the deck, greyed out, with a lit cartoon bomb drawn over the middle of it. The **Relying Party SERVER** and **Client** labels are highlighted in orange; the Client column shows **RP JS APP**, **WEBAUTHN** (red) and **BROWSER**. The faded message labels still readable are `(1) Auth request`, `(2) challenge, user info, RP info`, `(3) navigator.credentials.create`, `(9) attestationObject, clientDataJSON`, and `(10) verify as per [1] and add credentials to its storage`.

**2/37**

protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user

## Slide 51

**51**

### **Decoding problem**

Flowchart. A **Ceremony** box on the left fans out with six arrows, one to each of six boxes:

- **Vendor A:** base64url(CBOR(...))
- **Vendor B:** protobuf blob
- **Vendor C:** double-wrapped JSON + base64
- **Vendor D:** long body form-POST
- **Vendor E:** RPC batchexecute + positional arrays
- **...**

Six further arrows, one from each of those boxes, converge on a single **decode** box. One arrow leaves **decode** to a rounded blue box:

```text
decoded fields:
fmt,
authData
flags,
signCount,
...
```

Google SSO 75.2%, navigator.credentials-only 82.3%, known JS lib 18.6% <u>↗ Census: Bhardwaj & Sastry, PAM 2026</u>

**3/37**

protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user

## Slide 52

**52**

Three request panes side by side, each with a summary card below it.

###### **Microsoft**

`mysignins.microsoft.com`

```text
POST /api/post/newfido
Content-Type: form-urlencoded

canary=b0f2c1a9...
&clientDataJson=eyJ0eXBlIjo..
&attestationObject=o2NmbXRkcG..
&credentialId=3EHSf9K2mQ..
&credentialDeviceType=multiDevice
&credentialBackedUp=true
&transports=internal,hybrid
&extensions=eyJjcmVkUHJv..
```

**FLAT FORM FIELDS**

`position:` ~10 flat form params
`decode:` URL-encoded + Base64URL

###### **GitHub**

`github.com`

```text
POST /u2f/trusted_devices
Content-Type: multipart/form-data

------WebKitFormBoundary...
Content-Disposition: form-data;
  name="response"
{"id":"3EHSf9K2mQ..",
 "type":"public-key",
 "response":{
   "clientDataJSON":"eyJ0..
   "attestationObject":"o2N..
 },
 "clientExtensionResults":{}}
------WebKitFormBoundary...--
```

**MULTIPART + NESTED JSON**

`position:` spec field names, nested
`decode:` JSON + Base64URL

###### **Google**

`myaccount.google.com`

```text
POST /_/.../batchexecute
Content-Type: form-urlencoded

f.req=[[["GtmsU","[null,null,
  null,"eyJ0eXBlIjoi..",
  "o2NmbXRkcGFj..",
  ["internal"],null,1,1]",
  null,"generic"]]]
&at=AFehe7k9dQ..

// idx 3 = clientDataJSON
// idx 4 = attestationObject
```

**POSITIONAL ARRAYS**

`position:` fields by index in a blob
`decode:` URL-encoded + Base64URL

**4/37**

protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user

## Slide 53

**53**

### **Decoded fields**

```json
{
  "clientDataJSON": {
    "type": "webauthn.get",
    "challenge": "zYJx-8mHw8wK7vC4qRseSJrDCd01yKIfZk_njXEOoeuQD7CuKUoQ2frvV0NBoJiVZSBgjUYy8vGb-0Lq-BS1wA",
    "origin": "https://webauthn.io",
    "crossOrigin": false
  },
  "authenticatorData": {
    "rpIdHash": "74A6EA9213C99C2F74B22492B320CF40262A94C1A950A0397F29250B60841EF0",
    "flags": {
      "userPresent": true,
      "userVerified": true,
      "backupEligible": false,
      "backupState": false,
      "attestedCredentialData": false,
      "extensionDataIncluded": false
    },
    "signCount": 42
  },
  "signature": "304402207BC3E1F0A2D4C6980B5E3F1A2C4D6E8F0A1B2C3D4E5F60…DDEEFF02",
  "userHandle": "6D617474656F2D67696F7264616E6F"
}
```

You want:

- Traffic detection

   - across vendor wrappers

- Every field decoded:

   - clientDataJSON

   - authenticatorData

   - signature

   - userHandle

**5/37**

protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user

## Slide 54

**54**

### **Passkey Editor**

You have:

- Ceremony traffic detection

   - Registration/Authentication/Option

   - Fits every vendor

- Fields decoding:

   - clientDataJSON

   - attestationObject

   - authData

   - COSE key

   - ...

Screenshot of a Burp Suite request, with a **Passkey Editor** tab added.

Selected proxy row: `5160  https://webauthn.io  POST  /registration/verification  ✓  ✓  200`

**Original request** ⌄

Tabs: `Pretty` `Raw` `Hex` **Passkey Editor** (selected).   ☑ Wrap

```json
{
  "clientDataJSON": {
    "type": "webauthn.create",
    "challenge":
"zYJx-8mHw8wK7vC4qRseSJrDCd01yKIfZk_njXEOoeuQD7CuKUoQ2frvV0NBoJiVZSBgjUYy8vGb-0Lq-BS1wA",
    "origin": "https://webauthn.io",
    "crossOrigin": false
  },
  "attestationObject": {
   "attestationStatement": {
     "format": "none"
   },
   "authenticatorData": {
     "rpIdHash": "74A6EA9213C99C2F74B22492B320CF40262A94C1A950A0397F29250B60841EF0",
     "extensions": {},
     "signCount": 1,
     "flags": {
       "userPresent": true,
       "userVerified": true,
       "backupEligible": false,
       "backupState": false,
       "attestedCredentialData": true,
       "extensionDataIncluded": false
     },
     "attestedCredentialData": {
       "aaguid": "01020304-0506-0708-0102-030405060708",
       "coseKey": {
         "keyType": "OKP",
         "algorithm": "EdDSA",
         "curve": "Ed25519",
         "x": "4E7DB02BDD2B21364502D0177930029CEBB39BC8F8BC42CB8997EAB7CDDFEB2D"
       },
       "credentialId": "744D5E363DA57801D203145B4736F9D4653ED2104CE3C4E6C6941C75ED7E0A7F"
     }
   }
  },
  "fmt": "none"
 }
}
```

**6/37**

protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user

## Slide 55

**55**

Screenshot of the **Passkey Editor** tool, full window.

Tabs: **Profiles** (selected) · Guide · About

Left pane, **Profiles**:

- ☐ Default (SimpleWebAuthn / generic)  [not active]
- ☑ webauthn.io (Duo py_webauthn)   *(selected row, highlighted blue)*
- ☐ passkeys-debugger.io (Next.js action)  [not active]
- ☐ passkeys.io (Hanko)  [not active]
- ☐ demo.yubico.com  [not active]
- ☑ webauthn.lubu.ch  [auto-plant]  [re-sign]   *(orange)*

Buttons below the list: **Add** · **Copy** · **Delete** · **Restore built-ins**

Right pane, **Profile: webauthn.io (Duo py_webauthn)**:

☑ Enabled  ☐ Auto-plant  ☐ Auto re-sign

| Field | Value |
|---|---|
| id: | `webauthn.io` |
| name: | `webauthn.io (Duo py_webauthn)` |
| host match: | `EXACT` ⌄ / `webauthn.io` |
| default signing alg: | `EdDSA (-8)` ⌄ |
| plant attestation: | `None` ⌄ |

**Registration**

verify URL: `CONTAINS` ⌄ | `/registration/verification`   method: `POST`

| field | path/regex | value | encoding | decoded |
|---|---|---|---|---|
| clientDataJSON | ⦿ path ○ regex | `response.response.clientDataJSON` | ⦿ Auto ○ Raw ○ Base64 ○ Base64URL ☐ URL encoded | webauthn.create  `decoded ›` |
| attestationObject | ⦿ path ○ regex | `response.response.attestationObject` | ⦿ Auto ○ Raw ○ Base64 ○ Base64URL ☐ URL encoded | fmt=none · Ed25519 key  `decoded ›` |
| authenticatorData | ⦿ path ○ regex | `response.response.authenticatorData` | ⦿ Auto ○ Raw ○ Base64 ○ Base64URL ☐ URL encoded | UP UV AT · signCount 1  `decoded ›` |
| credentialId | ⦿ path ○ regex | *(empty)* | ⦿ Auto ○ Raw ○ Base64 ○ Base64URL ☐ URL encoded | `decoded ›` |

**Authentication**

verify URL: `CONTAINS` ⌄ | `/authentication/verification`   method: `POST`

| field | path/regex | value | encoding | decoded |
|---|---|---|---|---|
| clientDataJSON | ⦿ path ○ regex | `response.response.clientDataJSON` | ⦿ Auto ○ Raw ○ Base64 ○ Base64URL ☐ URL encoded | webauthn.get  `decoded ›` |
| authenticatorData | ⦿ path ○ regex | `response.response.authenticatorData` | ⦿ Auto ○ Raw ○ Base64 ○ Base64URL ☐ URL encoded | UP UV · signCount 2  `decoded ›` |
| signature | ⦿ path ○ regex | `response.response.signature` | ⦿ Auto ○ Raw ○ Base64 ○ Base64URL ☐ URL encoded | Ed25519 · 64B  `decoded ›` |
| userHandle | ⦿ path ○ regex | `response.response.userHandle` | ⦿ Auto ○ Raw ○ Base64 ○ Base64URL ☐ URL encoded | 37B · "webauthnio-asdadsada…"  `decoded ›` |
| credentialId | ⦿ path ○ regex | `response.rawId` | ⦿ Auto ○ Raw ○ Base64 ○ Base64URL ☐ URL encoded | 32B · 893025b4e178…  `decoded ›` |

**Sample bodies**

Registration body (paste the reg-verify request body):

```json
{
  "username": "defcon34",
  "response": {
    "id": "iTAltOF4snCezIL1FNoclo0w3Ez4vDkLQIkxrqURt8Q",
    "rawId": "iTAltOF4snCezIL1FNoclo0w3Ez4vDkLQIkxrqURt8Q",
    "response": {
      "attestationObject": "o2NmbXRkbm9uZWdhdHRTdG10oGhhdXRoRGF0YViBdKbqkhPJnC90siSSsyDPQCYqlMGpUKA5fyklC2CEHvBFAAAAAQECAwQFBgcIAQIDBAUGBwgAIIkwJbTheLJwnsyC9RTaHJaNMNxM-Lw5C0CJMa6lEbfEpAEBAycgBiFYIP8CuPmFEqE1eDHTvdI5hBJwS2K3FKP2f-eI3OHLC_2u",
      "clientDataJSON": "eyJ0eXBlIjoid2ViYXV0aG4uY3JlYXRlIiwiY2hhbGxlbmdlIjoiSmV2VTBETm5rUnRCOUlsTnJiR01vYmFMZGFTNmJSeUJha2tta3plVEtyVFNQR2hCQk5YWHBRSDFDU3NDY1N0RkJaTDNDdFFtY0lmMUE0anlrQVlGZHciLCJvcmlnaW4iOiJodHRwczovL3dlYmF1dGhuLmlvIiwiY3Jvc3NPcmlnaW4iOmZhbHNlfQ",
```

Authentication body (paste the auth-verify request body):

```json
{
  "username": "defcon34",
  "response": {
    "id": "iTAltOF4snCezIL1FNoclo0w3Ez4vDkLQIkxrqURt8Q",
    "rawId": "iTAltOF4snCezIL1FNoclo0w3Ez4vDkLQIkxrqURt8Q",
    "response": {
      "authenticatorData": "dKbqkhPJnC90siSSsyDPQCYqlMGpUKA5fyklC2CEHvAFAAAAAg",
      "clientDataJSON": "eyJ0eXBlIjoid2ViYXV0aG4uZ2V0IiwiY2hhbGxlbmdlIjoiZ0RGMTR2aE1iVlkySGVwdV9PS0lPYzdCR3BZSkc4Z3dEd2dfNXpWMlpNOFNKanFNa1dScGN4RnRkdFNXZE5kZ0FJOFpvWC1ydVRCdm1Kc0JXc01kanciLCJvcmlnaW4iOiJodHRwczovL3dlYmF1dGhuLmlvIiwiY3Jvc3NPcmlnaW4iOmZhbHNlfQ",
      "signature": "xMqaOxhmJ_68vH4KiUMougIZ1FGnJeVvvFVkUvJhRwGn9N-jS9Woa99BTY51-V5711UoG5MJ6_0ADJDFF8orDQ",
```

Both textareas are scrolled, so each body is cut off after the line shown.

Buttons: **Check** · **Prettify JSON** · **Save profile**   `all 8 configured field(s) extract cleanly`

**7/37**

protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user

## Slide 56

**56**

Zoom 1 of the Passkey Editor screenshot: the **Profiles** pane, ringed in a blue rectangle with a blue circled marker **1** at its bottom-right corner.

Tabs above: **Profiles** (selected) · Guide · About

**Profiles**

- ☐ Default (SimpleWebAuthn / generic)  [not active]
- ☑ webauthn.io (Duo py_webauthn)   *(selected row, highlighted blue)*
- ☐ passkeys-debugger.io (Next.js action)  [not active]
- ☐ passkeys.io (Hanko)  [not active]
- ☐ demo.yubico.com  [not active]
- ☑ webauthn.lubu.ch  [auto-plant]  [re-sign]   *(orange)*

Buttons: **Add** · **Copy** · **Delete** · **Restore built-ins**

**8/37**

protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user

## Slide 57

**57**

Zoom 2: the profile identity rows, with the **host match** row ringed in a blue rectangle and a blue circled marker **2** at its right-hand end.

| Field | Value |
|---|---|
| id: | `webauthn.io` |
| name: | `webauthn.io (Duo py_we` — clipped by the right edge of the crop |
| host match: | `EXACT` ⌄ / `webauthn.io` |
| default signing alg: | `EdDSA (-8)` ⌄ |
| plant attestation: | `None` — clipped by the right edge of the crop |

**9/37**

protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user

## Slide 58

**58**

Zoom 3: the **Registration** fieldset, ringed in a blue rectangle with a blue circled marker **3** at its bottom-right corner. A row of controls above it and the **Authentication** legend below it are cut by the crop.

**Registration**

verify URL: `CONTAINS` ⌄ | `/registration/verification`   method: `POST`

| field | | path/regex |
|---|---|---|
| clientDataJSON | ⦿ path ○ regex | `response.response.clientDataJSON` |
| attestationObject | ⦿ path ○ regex | `response.response.attestationObject` |
| authenticatorData | ⦿ path ○ regex | `response.response.authenticatorData` |
| credentialId | ⦿ path ○ regex | *(empty)* |

The encoding radio column to the right is cut off by the crop, leaving only the first ⦿ of each row.

**10/37**

protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user

## Slide 59

**59**

Zoom 4: the **Authentication** fieldset, ringed in a blue rectangle with a blue circled marker **4** at its bottom-right corner. The last row of the Registration fieldset above and the **Sample bodies** legend below are cut by the crop.

**Authentication**

verify URL: `CONTAINS` ⌄ | `/authentication/verification`   method: `POST`

| field | | path/regex |
|---|---|---|
| clientDataJSON | ⦿ path ○ regex | `response.response.clientDataJSON` |
| authenticatorData | ⦿ path ○ regex | `response.response.authenticatorData` |
| signature | ⦿ path ○ regex | `response.response.signature` |
| userHandle | ⦿ path ○ regex | `response.response.userHandle` |
| credentialId | ⦿ path ○ regex | `response.rawId` |

The encoding radio column to the right is cut off by the crop, leaving only the first ⦿ of each row.

**11/37**

protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user

## Slide 60

**60**

Zoom 5: the encoding-selector columns of both fieldsets, ringed in one blue rectangle with a blue circled marker **5** at its bottom-right corner. Field names on the left and the decoded summaries on the right are cut by the crop.

Four rows (Registration):

```text
⦿ Auto  ○ Raw  ○ Base64  ○ Base64URL  ☐ URL encoded   weba…
⦿ Auto  ○ Raw  ○ Base64  ○ Base64URL  ☐ URL encoded   fmt=n…
⦿ Auto  ○ Raw  ○ Base64  ○ Base64URL  ☐ URL encoded   UP U…
⦿ Auto  ○ Raw  ○ Base64  ○ Base64URL  ☐ URL encoded   de…
```

Five rows (Authentication):

```text
⦿ Auto  ○ Raw  ○ Base64  ○ Base64URL  ☐ URL encoded   weba…
⦿ Auto  ○ Raw  ○ Base64  ○ Base64URL  ☐ URL encoded   UP U…
⦿ Auto  ○ Raw  ○ Base64  ○ Base64URL  ☐ URL encoded   Ed25…
⦿ Auto  ○ Raw  ○ Base64  ○ Base64URL  ☐ URL encoded   37B ·
⦿ Auto  ○ Raw  ○ Base64  ○ Base64URL  ☐ URL encoded   32B ·
```

**12/37**

protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user

## Slide 61

**61**

Zoom 6 of the Passkey Editor screenshot: the two fieldsets and the **Sample bodies** pane. Blue circled marker **9** sits above the decoded-summary column of the Registration fieldset, **10** to the right of the userHandle summary, **6** at the top-left corner of the Sample bodies box, **7** above the *Prettify JSON* button and **8** above the *Check* button. One blue rectangle rings the two decoded-summary columns; a second rings the whole Sample bodies box.

**Registration**

verify URL: `CONTAINS` ⌄ | `/registration/verification`   method: `POST`

| field | path/regex | value | encoding | decoded |
|---|---|---|---|---|
| clientDataJSON | ⦿ path ○ regex | `response.response.clientDataJSON` | ⦿ Auto ○ Raw ○ Base64 ○ Base64URL ☐ URL encoded | webauthn.create  `decoded ›` |
| attestationObject | ⦿ path ○ regex | `response.response.attestationObject` | ⦿ Auto ○ Raw ○ Base64 ○ Base64URL ☐ URL encoded | fmt=none · Ed25519 key  `decoded ›` |
| authenticatorData | ⦿ path ○ regex | `response.response.authenticatorData` | ⦿ Auto ○ Raw ○ Base64 ○ Base64URL ☐ URL encoded | UP UV AT · signCount 1  `decoded ›` |
| credentialId | ⦿ path ○ regex | *(empty)* | ⦿ Auto ○ Raw ○ Base64 ○ Base64URL ☐ URL encoded | `decoded ›` |

**Authentication**

verify URL: `CONTAINS` ⌄ | `/authentication/verification`   method: `POST`

| field | path/regex | value | encoding | decoded |
|---|---|---|---|---|
| clientDataJSON | ⦿ path ○ regex | `response.response.clientDataJSON` | ⦿ Auto ○ Raw ○ Base64 ○ Base64URL ☐ URL encoded | webauthn.get  `decoded ›` |
| authenticatorData | ⦿ path ○ regex | `response.response.authenticatorData` | ⦿ Auto ○ Raw ○ Base64 ○ Base64URL ☐ URL encoded | UP UV · signCount 2  `decoded ›` |
| signature | ⦿ path ○ regex | `response.response.signature` | ⦿ Auto ○ Raw ○ Base64 ○ Base64URL ☐ URL encoded | Ed25519 · 64B  `decoded ›` |
| userHandle | ⦿ path ○ regex | `response.response.userHandle` | ⦿ Auto ○ Raw ○ Base64 ○ Base64URL ☐ URL encoded | 37B · "webauthnio-asdadsada…"  `decoded ›` |
| credentialId | ⦿ path ○ regex | `response.rawId` | ⦿ Auto ○ Raw ○ Base64 ○ Base64URL ☐ URL encoded | 32B · 893025b4e178…  `decoded ›` |

**Sample bodies**

Registration body (paste the reg-verify request body):

```json
{
  "username": "defcon34",
  "response": {
    "id": "iTAltOF4snCezIL1FNoclo0w3Ez4vDkLQIkxrqURt8Q",
    "rawId": "iTAltOF4snCezIL1FNoclo0w3Ez4vDkLQIkxrqURt8Q",
    "response": {
      "attestationObject": "o2NmbXRkbm9uZWdhdHRTdG10oGhhdXRoRGF0YViBdKbqkhPJnC90siSSsyDPQCYqlMGpUKA5fyklC2CEHvBFAAAAAQECAwQFBgcIAQIDBAUGBwgAIIkwJbTheLJwnsyC9RTaHJaNMNxM-Lw5C0CJMa6lEbfEpAEBAycgBiFYIP8CuPmFEqE1eDHTvdI5hBJwS2K3FKP2f-eI3OHLC_2u",
      "clientDataJSON": "eyJ0eXBlIjoid2ViYXV0aG4uY3JlYXRlIiwiY2hhbGxlbmdlIjoiSmV2VTBETm5rUnRCOUlsTnJiR01vYmFMZGFTNmJSeUJha2tta3plVEtyVFNQR2hCQk5YWHBRSDFDU3NDY1N0RkJaTDNDdFFtY0lmMUE0anlrQVlGZHciLCJvcmlnaW4iOiJodHRwczovL3dlYmF1dGhuLmlvIiwiY3Jvc3NPcmlnaW4iOmZhbHNlfQ",
```

Authentication body (paste the auth-verify request body):

```json
{
  "username": "defcon34",
  "response": {
    "id": "iTAltOF4snCezIL1FNoclo0w3Ez4vDkLQIkxrqURt8Q",
    "rawId": "iTAltOF4snCezIL1FNoclo0w3Ez4vDkLQIkxrqURt8Q",
    "response": {
      "authenticatorData": "dKbqkhPJnC90siSSsyDPQCYqlMGpUKA5fyklC2CEHvAFAAAAAg",
      "clientDataJSON": "eyJ0eXBlIjoid2ViYXV0aG4uZ2V0IiwiY2hhbGxlbmdlIjoiZ0RGMTR2aE1iVlkySGVwdV9PS0lPYzdCR3BZSkc4Z3dEd2dfNXpWMlpNOFNKanFNa1dScGN4RnRkdFNXZE5kZ0FJOFpvWC1ydVRCdm1Kc0JXc01kanciLCJvcmlnaW4iOiJodHRwczovL3dlYmF1dGhuLmlvIiwiY3Jvc3NPcmlnaW4iOmZhbHNlfQ",
      "signature": "xMqaOxhmJ_68vH4KiUMougIZ1FGnJeVvvFVkUvJhRwGn9N-jS9Woa99BTY51-V5711UoG5MJ6_0ADJDFF8orDQ",
```

Each textarea is scrolled, so both bodies are cut off after the line shown.

Buttons: **Check** · **Prettify JSON** · **Save profile**   `all 8 configured field(s) extract cleanly`

**13/37**

protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user

## Slide 62

**62**

### **Tamper + re-sign**

- Edit any field, re-encode in place

- Any edit breaks the signature

   - re-plant the key

   - re-sign on passthrough

Screenshot of Burp Suite Proxy, right of the bullets.

Tabs: **Intercept** (selected, orange dot) · HTTP history · WebSockets history · Match and replace | ⚙ Proxy settings

Buttons: **Intercept on** · **→ Forward** ⌄ · **Drop** ⌄ · `Request to https://we…` ✎ · **⊕ Open browser** · ⓘ

| Time | Type | Direction | Method | URL | Status code | Length |
|---|---|---|---|---|---|---|
| 13:28:50 6 Jul 2026 | HTTP | → Request | POST | `https://webauthn.io/authentication/verification` | | |

**Request** — tabs `Pretty` `Raw` `Hex` **Passkey Editor** (selected)

`Attacks ⌄`   ☑ Wrap

Flags: ☑ UP  ☑ UV  ☐ BE  ☐ BS

```json
{
  "clientDataJSON": {
    "type": "webauthn.get",
    "challenge": "lXi6duZCUvut6pxxch4hKFEuyLMuK7tQH5QfsSs7pts941y_MRf6l-_JI73_yiFB2jJ7CKW-jtsZMmGUpyw5og",
    "origin": "https://evil.webauthn.io",
    "crossOrigin": false
  },
  "authenticatorData": {
    "rpIdHash": "22EA1500B25722FD46E8A8653E37107E07805890FCD719A92A9EF5CAD9693AFF",
    "extensions": {},
    "signCount": 2,
    "flags": {
      "userPresent": true,
      "userVerified": true,
      "backupEligible": false,
      "backupState": false,
      "attestedCredentialData": false,
      "extensionDataIncluded": false
    },
    "attestedCredentialData": {}
  },
  "signature":
"26C90A162BA1528B08AAAEDEFF454A8A3ACAE7041FAD616A9A52CDAF536D0FC3D6B4BFC5799D3AF4079876C667FD7A1A71EBF4660F3C8D8E84DB270885E3C90F"
}
```

`"https://evil.webauthn.io"`, the `rpIdHash` and the `signature` value are highlighted yellow.

Below the pane, in green:

```text
re-signed (EdDSA)
  • rpId = <edited>
  • origin = https://evil.webauthn.io
```

Buttons: **Re-sign with our key** · **Clear edits** · **Apply edits + re-sign**

**14/37**

protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user

## Slide 63

**63**

Hand-drawn WebAuthn registration ceremony with an attacker column inserted. Four participants, left to right: **Relying Party SERVER** (a bare vertical line), a red-outlined box lettered vertically **M I T M**, **Client** (a bracket spanning three vertical lanes lettered **RP JS APP**, **WEBAUTHN**, **BROWSER**) and **Authenticator** (a single vertical lane).

Arrows, top to bottom:

- A red arrow labelled **forged**, MITM → SERVER (arrowhead at the SERVER end only).
- `(1) Auth request` — RP JS APP → MITM (arrowhead at the MITM end).
- One black arrow SERVER → MITM (arrowhead at the MITM end), labelled above and below:
  - `(2) challenge, user info, RP info`
  - `(3) navigator.credentials.create`
- A red arrow labelled **forged**, MITM → RP JS APP (arrowhead at the RP JS APP end only).
- `(5) hash(clientDataJSON), user info, RP info, RP ID` — BROWSER → Authenticator (arrowhead at the Authenticator end).
- A self-loop on Authenticator, labelled `(6)   is User near?` / `(6.1) can User unlock?` / `(6.2) Creates the key pair scoped to the RP ID`.
- A second self-loop on Authenticator, labelled with the `(7) attestationObject` block below.
- `(8) attestationObject` — Authenticator → BROWSER (arrowhead at the BROWSER end).
- `(9) attestationObject, clientDataJSON` — RP JS APP → MITM (arrowhead at the MITM end).
- A red arrow labelled **forged**, MITM → SERVER (arrowhead at the SERVER end only).
- A self-loop on SERVER, labelled `(10) verify as per [1] and add credentials to its storage`.
- A thick arrow entering the bottom of the BROWSER lane from below, labelled with the `(4) clientDataJSON` block.

Side blocks:

```text
(7) attestationObject = {
    hash(RP ID),
    flags = [
        UserPresence,
        UserVerification,
        Attested cred data,
        Extension data
    ],
    credential ID,
    public Key in CBOR,
    AAGUID,
    initial sig counter,
    extensions
}
```

```text
(4) clientDataJSON = {
        challenge,
        RP origin,
        "webauthn.create"
    }
```

A starburst callout below the MITM box, in red:

**Plant new key**
**Resign w/ new key**

**15/37**

protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user

## Slide 64

**64**

### **Not the first tool**

- ◆ <u>↗ webauthn-cbor</u> — decodes only, no attacks.

- ◆ <u>↗ passkey-scanner</u> — passive detection.

- ◆ <u>↗ passkey-raider</u> — tampers, but by hand.

- ◆ <u>↗ Burp_FIDO2</u> — handles wrappers, rough on production traffic.

- ◆ <u>↗ Grafnetter, Pass-the-Passkey</u> — open-sourced at Black Hat this week.

- ◆ <u>↗ Passkeys.Tools (Jannett)</u> — emulates browser AND authenticator, tampers every field at scale

- ◆ **Passkey Editor's lane:** Burp-native, attack dropdown live across Intercept, history, and Repeater, auto re-sign on passthrough, decoding paired with tampering.

**16/37**

protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user

## Slide 65

**65**

### **clientDataJSON**

Two screenshots side by side.

Left, captioned **Raw HTTP request**:

```http
POST /authentication/verification HTTP/2
Host: webauthn.io
Cookie: sessionid=cicj8qb34pnwr50xeyuvyt5pgi690q43
Content-Length: 865
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36
Content-Type: application/json
Origin: https://webauthn.io
Referer: https://webauthn.io/

{
  "username":"defcon34_demo",
  "response":{
    "id":"XYMXeBZ1HTwo15ssOIhVTw3K-Cgy_mclKKaE4Jilvq4",
    "rawId":"XYMXeBZ1HTwo15ssOIhVTw3K-Cgy_mclKKaE4Jilvq4",
    "response":{
      "authenticatorData":
      "dKbqkhPJnC90siSSsyDPQCYqlMGpUKA5fyklC2CEHvAFAAAAAg",
      "clientDataJSON":
      "eyJ0eXBlIjoid2ViYXV0aG4uZ2V0IiwiY2hhbGxlbmdlIjoiZ19jN0VzdEVPWnBSaDIwS
DRLUEFTZzJiUTd0M3dJQU9OSVNhSWFsNVV3SnVsWUxueUlwQmlPY3k5Z1NITlBzZENhajR
lNFd6dVJRUzBNZ05VLXRSbUEiLCJvcmlnaW4iOiJodHRwczovL3dlYmF1dGhuLmlvIiwiY
3Jvc3NPcmlnaW4iOmZhbHNlLCJvdGhlcl9rZXlzX2Nhbl9iZV9hZGRlZF9oZXJlIjoiZG8
gbm90IGNvbXBhcmUgY2xpZW50RGF0YUpTT04gYWdhaW5zdCBhIHRlbXBsYXRlLiBTZWUga
HR0cHM6Ly9nb28uZ2wveWFiUGV4In0",
      "signature":
      "IBTQLAKniU6-XLMn1P8_FVAVaRbsmKD5SMoB5kqrAXuYGr03urUvo7e37g6EW_6hLJ7co
STQ04jMYIO5RrsvCw",
      "userHandle":"d2ViYXV0aG5pby1kZWZjb24zNF9kZW1v"
    },
    "type":"public-key",
    "clientExtensionResults":{
    },
    "authenticatorAttachment":"platform"
  }
}
```

A blue rectangle rings the six wrapped lines of the `clientDataJSON` value.

Right, captioned **Passkey Editor**:

Tabs `Pretty` `Raw` `Hex` **Passkey Editor** (selected); four icon buttons at the right of the tab bar.

`Attacks ⌄`   ☑ Wrap

Flags: ☑ UP  ☑ UV  ☐ BE  ☐ BS

```json
{
  "clientDataJSON": {
    "type": "webauthn.get",
    "challenge":
"g_c7EstEOZpRh20H4KPASg2bQ7t3wIAONISaIal5UwJulYLnyIpBiOcy9gSHNPsdCaj4e4WzuRQS0MgNU-tRmA",
    "origin": "https://webauthn.io",
    "crossOrigin": false,
    "other_keys_can_be_added_here": "do not compare clientDataJSON against a template.
See https://goo.gl/yabPex"
  },
  "authenticatorData": {
    "rpIdHash": "74A6EA9213C99C2F74B22492B320CF40262A94C1A950A0397F29250B60841EF0",
    "extensions": {},
    "signCount": 2,
    "flags": {
      "userPresent": true,
      "userVerified": true,
      "backupEligible": false,
      "backupState": false,
      "attestedCredentialData": false,
      "extensionDataIncluded": false
    },
    "attestedCredentialData": {}
  },
  "signature":
"2014D02C02A7894EBE5CB327D4FF3F1550156916EC98A0F948CA01E64AAB017B981ABD37BAB52FA3B7B7EE0E
845BFEA12C9EDCA124D0D388CC6083B946BB2F0B"
}
```

A blue rectangle rings the whole `clientDataJSON` object.

**17/37**

protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user

## Slide 66

**66**

### **challenge**

Screenshot of the Passkey Editor tab of a Burp request.

Tabs `Pretty` `Raw` `Hex` **Passkey Editor** (selected); four icon buttons at the right of the tab bar.

`Attacks ⌄`   ☑ Wrap

Flags: ☑ UP  ☑ UV  ☐ BE  ☐ BS

```json
{
  "clientDataJSON": {
    "type": "webauthn.get",
    "challenge": "evil_challenge",
    "origin": "https://webauthn.io",
    "crossOrigin": false,
    "other_keys_can_be_added_here": "do not compare clientDataJSON against a template.
See https://goo.gl/yabPex"
  },
  "authenticatorData": {
    "rpIdHash": "74A6EA9213C99C2F74B22492B320CF40262A94C1A950A0397F29250B60841EF0",
    "extensions": {},
    "signCount": 2,
    "flags": {
      "userPresent": true,
      "userVerified": true,
      "backupEligible": false,
      "backupState": false,
      "attestedCredentialData": false,
      "extensionDataIncluded": false
    },
    "attestedCredentialData": {}
  },
  "signature":
"4C0944C43B98FD85B7131C127173B4FE2C6F095C876106BBB1EAC6DC326AF3F7B5B0D4F4867C56BCFE70BBDC
0DB6A00A41BEFD50BF868D4A60018656FF0ECF0F"
}
```

`"evil_challenge"` and the `signature` value are highlighted yellow.

**18/37**

protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user

## Slide 67

**67**

### **origin + rpIdHash**

Two Passkey Editor panes side by side.

Left, captioned **origin** — tabs `Pretty` `Raw` `Hex` **Passkey Editor** (selected); `Attacks ⌄`  ☑ Wrap; Flags: ☑ UP  ☑ UV  ☐ BE  ☐ BS

```json
{
  "clientDataJSON": {
    "type": "webauthn.get",
    "challenge":
"g_c7EstEOZpRh20H4KPASg2bQ7t3wIAONISaIal5UwJulYLnyIpBiOcy9gSHNPsdCaj4e4WzuRQS0MgNU-tRmA",
    "origin": "https://evil.defcon34.xyz",
    "crossOrigin": false,
    "other_keys_can_be_added_here": "do not compare clientDataJSON against a template.
See https://goo.gl/yabPex"
  },
  "authenticatorData": {
    "rpIdHash": "74A6EA9213C99C2F74B22492B320CF40262A94C1A950A0397F29250B60841EF0",
    "extensions": {},
    "signCount": 2,
    "flags": {
      "userPresent": true,
      "userVerified": true,
      "backupEligible": false,
      "backupState": false,
      "attestedCredentialData": false,
      "extensionDataIncluded": false
    },
    "attestedCredentialData": {}
  },
  "signature":
"1AF21C1F86B8C216576A09A4575E89BB97A875E4D2A3C4AA2FB4FD20DB6E10DE43938FC12AF1A0FD83DCC704
E5401D7E3F3542C19472822BEA251454E6C0960A"
}
```

`"https://evil.defcon34.xyz"` and the `signature` value are highlighted yellow.

Right, captioned **rpIdHash** — same tab bar and controls.

```json
{
  "clientDataJSON": {
    "type": "webauthn.get",
    "challenge":
"SnFcY_gy4PO--D3ueYA6PrxBH56EuW_3BcEjBahjtm9tQq8Yk8JNAeDfxN47a4wgp3yNfwPcEySw8axZXhMiqA",
    "origin": "https://webauthn.io",
    "crossOrigin": false
  },
  "authenticatorData": {
    "rpIdHash": "00A6EA9213C99C2F74B22492B320CF40262A94C1A950A0397F29250B60841EF0",
    "extensions": {},
    "signCount": 2,
    "flags": {
      "userPresent": true,
      "userVerified": true,
      "backupEligible": false,
      "backupState": false,
      "attestedCredentialData": false,
      "extensionDataIncluded": false
    },
    "attestedCredentialData": {}
  },
  "signature":
"396EBFCC02B229F152413D4F2EBC30AE7815E4EBA939EAB38A2871F52F962153A81E207D9FFB38181B1EE208
60736655A547320DC10732961492BA548E8F4C0C"
}
```

The `rpIdHash` and `signature` values are highlighted yellow.

**19/37**

protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user

## Slide 68

**68**

### **Over-scoping the RPid**

Flowchart. Four boxes in a row, all enclosed in one large rectangle, joined left to right by arrows (arrowhead at the right-hand end of each):

- `rpId = example.com`  /  `(but only app.example.com needed)`
- → `valid for *.example.com`
- → `customer1.example.com`
- —forges→ `customer2.example.com`

One curved arrow leaves the bottom-right of `customer2.example.com`, runs down and to the left, and ends (arrowhead) at a box **outside** the large rectangle:

```text
cross-origin
ACCOUNT
TAKE
OVER
```

**20/37**

protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user

## Slide 69

**69**

### **Dangling Allowlist Domain**

Flowchart. Four boxes in a row, all enclosed in one large rectangle, joined left to right by arrows (arrowhead at the right-hand end of each):

- `/.well-known/webauthn`  `allowlist`  /  `(a.com, b.com, patner.com)`
- → `partner.com LAPSES`
- → `attacker buys it @ 10 $/yr`
- → `attacker origin now TRUSTED`

One curved arrow leaves the bottom-right of `attacker origin now TRUSTED`, runs down and to the left, and ends (arrowhead) at a box **outside** the large rectangle:

```text
cross-origin
ACCOUNT
TAKE
OVER
```

**21/37**

protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user

## Slide 70

**70**

### **attestationObject and authenticatorData**

Screenshot of the Passkey Editor tab of a Burp request.

Tabs `Pretty` `Raw` `Hex` **Passkey Editor** (selected); four icon buttons at the right of the tab bar.

`Attacks ⌄`   ☑ Wrap

Flags: ☑ UP  ☑ UV  ☐ BE  ☐ BS

```json
{
  "clientDataJSON": {
    "type": "webauthn.get",
    "challenge":
"SnFcY_gy4PO--D3ueYA6PrxBH56EuW_3BcEjBahjtm9tQq8Yk8JNAeDfxN47a4wgp3yNfwPcEySw8axZXhMiqA",
    "origin": "https://webauthn.io",
    "crossOrigin": false
  },
  "authenticatorData": {
    "rpIdHash": "74A6EA9213C99C2F74B22492B320CF40262A94C1A950A0397F29250B60841EF0",
    "extensions": {},
    "signCount": 2,
    "flags": {
      "userPresent": true,
      "userVerified": true,
      "backupEligible": false,
      "backupState": false,
      "attestedCredentialData": false,
      "extensionDataIncluded": false
    },
    "attestedCredentialData": {}
  },
  "signature":
"E32944FFA58C9630C398D1D5E11AD5E6F732C9281A10703DA1DB28F988F4332C7773A6BC5C3B81733AE170CD
330B135D24B4D28B37C3C34E4836FC1FF6761507"
}
```

A blue rectangle rings the `"authenticatorData"` object, from its opening line down to and including `"attestedCredentialData": {}`. The `signature` below it is outside the rectangle.

**22/37**

protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user

## Slide 71

**71**

Byte-layout figure, on a white card filling the slide.

**ATTESTATION OBJECT** — one row of three cells:

| “fmt“: “packed“ | “attStmt“: ... | “authData“: ... |
|---|---|---|

Braces run from the `“authData“` cell down to **AUTHENTICATOR DATA** — one row of five cells, each captioned above:

| 32 bytes | 1 byte | 4 bytes (big-endian uint32) | variable length | variable length if present (CBOR) |
|---|---|---|---|---|
| RP ID hash | FLAGS | COUNTER | ATTESTED CRED. DATA | EXTENSIONS |

The EXTENSIONS cell ends in a ragged (torn-edge) mark.

A brace from **FLAGS** expands to a bit map, numbered `7` at the left end and `0` at the right end:

| ED | AT | 0 | 0 | 0 | UV | 0 | UP |
|---|---|---|---|---|---|---|---|

A brace from **ATTESTED CRED. DATA** expands to:

| AAGUID | L | CREDENTIAL ID | CREDENTIAL PUBLIC KEY |
|---|---|---|---|
| 16 bytes | 2 bytes | LENGTH L (variable length) | variable length (COSE_Key) |

A dashed line from the `“attStmt“` cell runs down the left of the figure to **ATTESTATION STATEMENT**  (in "packed" attestation statement format):

| | | | |
|---|---|---|---|
| If Basic or Privacy CA: | “alg“: ... | “sig“: ... | “x5c“: ... |
| If ECDAA: | “alg“: ... | “sig“: ... | “ecdaaKeyId“: ... |

**23/37**

protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user

## Slide 72

**72**

The same byte-layout figure as the previous slide, with a red rounded rectangle drawn round the **AUTHENTICATOR DATA** portion and the word **Authentication** written in red inside it.

**ATTESTATION OBJECT** — one row of three cells:

| “fmt“: “packed“ | “attStmt“: ... | “authData“: ... |
|---|---|---|

**AUTHENTICATOR DATA** — one row of five cells, each captioned above:

| 32 bytes | 1 byte | 4 bytes (big-endian uint32) | variable length | variable length if present (CBOR) |
|---|---|---|---|---|
| RP ID hash | FLAGS | COUNTER | ATTESTED CRED. DATA | EXTENSIONS |

A brace from **FLAGS** expands to a bit map, numbered `7` at the left end and `0` at the right end:

| ED | AT | 0 | 0 | 0 | UV | 0 | UP |
|---|---|---|---|---|---|---|---|

A brace from **ATTESTED CRED. DATA** expands to:

| AAGUID | L | CREDENTIAL ID | CREDENTIAL PUBLIC KEY |
|---|---|---|---|
| 16 bytes | 2 bytes | LENGTH L (variable length) | variable length (COSE_Key) |

The red rectangle encloses the AUTHENTICATOR DATA heading, the five-cell row, the flags bit map and the attested-credential-data row. The ATTESTATION OBJECT row above it and the ATTESTATION STATEMENT block below it are **outside** the rectangle.

**ATTESTATION STATEMENT**  (in "packed" attestation statement format):

| | | | |
|---|---|---|---|
| If Basic or Privacy CA: | “alg“: ... | “sig“: ... | “x5c“: ... |
| If ECDAA: | “alg“: ... | “sig“: ... | “ecdaaKeyId“: ... |

**24/37**

protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user

## Slide 73

**73**

The same byte-layout figure again, now with two boxes drawn on it: a blue rounded rectangle enclosing the **whole** figure, labelled **Registration** in blue (the word sits just below the ATTESTATION OBJECT row), and inside it the red rounded rectangle from the previous slide round the AUTHENTICATOR DATA portion, labelled **Authentication** in red.

**ATTESTATION OBJECT** — one row of three cells:

| “fmt“: “packed“ | “attStmt“: ... | “authData“: ... |
|---|---|---|

**AUTHENTICATOR DATA** — one row of five cells, each captioned above:

| 32 bytes | 1 byte | 4 bytes (big-endian uint32) | variable length | variable length if present (CBOR) |
|---|---|---|---|---|
| RP ID hash | FLAGS | COUNTER | ATTESTED CRED. DATA | EXTENSIONS |

A brace from **FLAGS** expands to a bit map, numbered `7` at the left end and `0` at the right end:

| ED | AT | 0 | 0 | 0 | UV | 0 | UP |
|---|---|---|---|---|---|---|---|

A brace from **ATTESTED CRED. DATA** expands to:

| AAGUID | L | CREDENTIAL ID | CREDENTIAL PUBLIC KEY |
|---|---|---|---|
| 16 bytes | 2 bytes | LENGTH L (variable length) | variable length (COSE_Key) |

**ATTESTATION STATEMENT**  (in "packed" attestation statement format):

| | | | |
|---|---|---|---|
| If Basic or Privacy CA: | “alg“: ... | “sig“: ... | “x5c“: ... |
| If ECDAA: | “alg“: ... | “sig“: ... | “ecdaaKeyId“: ... |

The blue rectangle contains everything: the ATTESTATION OBJECT row, the AUTHENTICATOR DATA block and the ATTESTATION STATEMENT block. The red rectangle contains only the AUTHENTICATOR DATA heading, its five-cell row, the flags bit map and the attested-credential-data row.

**25/37**

protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user

## Slide 74

**74**

### **signature**

Screenshot of the Passkey Editor tab of a Burp request.

Tabs `Pretty` `Raw` `Hex` **Passkey Editor** (selected); four icon buttons at the right of the tab bar.

`Attacks ⌄`   ☑ Wrap

Flags: ☑ UP  ☑ UV  ☐ BE  ☐ BS

```json
{
  "clientDataJSON": {
    "type": "webauthn.get",
    "challenge":
"SnFcY_gy4PO--D3ueYA6PrxBH56EuW_3BcEjBahjtm9tQq8Yk8JNAeDfxN47a4wgp3yNfwPcEySw8axZXhMiqA",
    "origin": "https://webauthn.io",
    "crossOrigin": false
  },
  "authenticatorData": {
    "rpIdHash": "74A6EA9213C99C2F74B22492B320CF40262A94C1A950A0397F29250B60841EF0",
    "extensions": {},
    "signCount": 2,
    "flags": {
      "userPresent": true,
      "userVerified": true,
      "backupEligible": false,
      "backupState": false,
      "attestedCredentialData": false,
      "extensionDataIncluded": false
    },
    "attestedCredentialData": {}
  },
  "signature":
"585F37FDF8B02D37B69490DF81D684D8951BB65EA5F39E13F5843E9E67C37A5926F8A09902D9FE6E6831BFAD
951C6145F5BA365188E64E3C348DA3285EE6EE04"
}
```

The `signature` value is highlighted yellow.

**26/37**

protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user

## Slide 75

**75**

### **alg**

Screenshot of the Passkey Editor tab of a Burp request.

Tabs `Pretty` `Raw` `Hex` **Passkey Editor** (selected); four icon buttons at the right of the tab bar.

`Attacks ⌄`   ☑ Wrap

Signing algorithm: `RS256 (-257)` ⌄   Attestation: `None` ⌄   **RS256 key planted** *(green)*

Flags: ☑ UP  ☑ UV  ☐ BE  ☐ BS

```json
{
  "clientDataJSON": {
    "type": "webauthn.create",
    "challenge": "jdrVAViggN5wTpX3MX6QtnmQJgNoCVxWWlCFIes-6F9ThLq_LFAKw4co1BQ3n_XquOmbcA9fsfU_7qGHQVga2w",
    "origin": "https://webauthn.io",
    "crossOrigin": false
  },
  "attestationObject": {
    "attestationStatement": {
      "format": "none"
    },
    "authenticatorData": {
      "rpIdHash": "74A6EA9213C99C2F74B22492B320CF40262A94C1A950A0397F29250B60841EF0",
      "extensions": {},
      "signCount": 1,
      "flags": {
        "userPresent": true,
        "userVerified": true,
        "backupEligible": false,
        "backupState": false,
        "attestedCredentialData": true,
        "extensionDataIncluded": false
      },
      "attestedCredentialData": {
        "aaguid": "01020304-0506-0708-0102-030405060708",
        "coseKey": {
          "keyType": "RSA",
          "algorithm": "RS256",
          "raw":
"A401030339010020590100B104054256CE44CECCC357B8A1444DB2A1698C8D37AC992B52ED79B331AF43BED77844651D3959EC15CFE38F6552F
234AFEDFC5D7AF5F79E067136BFC335C6272FC2FF8A8EA58849E9DF31EA2D27C9F0908D47DDD7FDDD781FD2F8CB51ED0BC8058994522A4C13A41
331B85C037DDBAAED47775A401488E6D5E3823466724D22C6F6BAF274F7B6A8C8EB9660ECCD0BB14530818CE850A553A87A877A2B1C3A88695D7
A0A319FD6AB26113D7F59CFEEFD2D6725FA9BD3BD2D5CFB0568E70F31FCDFEBCA7FCDD1C2EAF4B46C44FD1D7A8269080D9A4A1DB3FAE649E1073
4D4729386160C39FC12B660B611765B9C45BC9E9ED548110766221D9C42906A2273CAEF2143010001"
        },
        "credentialId": "755A521FCEF1ABC93EA6C0DDC6B54FAB4CDED7E102DCB4F09B416C29180AA3CD"
      }
    }
  },
  "fmt": "none"
}
```

Blue rectangles ring `Signing algorithm: RS256 (-257)`, the `RS256 key planted` label, and the `coseKey` block (its `keyType`, `algorithm` and `raw` lines). `"RSA"`, `"RS256"` and the whole `raw` value are highlighted yellow.

**27/37**

protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user

## Slide 76

**77**

### **credentialId**

Screenshot of the Passkey Editor tab of a Burp request.

Tabs `Pretty` `Raw` `Hex` **Passkey Editor** (selected); four icon buttons at the right of the tab bar.

`Attacks ⌄`   ☑ Wrap

Signing algorithm: `RS256 (-257)` ⌄   Attestation: `None` ⌄   **RS256 key planted** *(green)*

Flags: ☑ UP  ☑ UV  ☐ BE  ☐ BS

```json
{
  "clientDataJSON": {
    "type": "webauthn.create",
    "challenge": "jdrVAViggN5wTpX3MX6QtnmQJgNoCVxWWlCFIes-6F9ThLq_LFAKw4co1BQ3n_XquOmbcA9fsfU_7qGHQVga2w",
    "origin": "https://webauthn.io",
    "crossOrigin": false
  },
  "attestationObject": {
    "attestationStatement": {
      "format": "none"
    },
    "authenticatorData": {
      "rpIdHash": "74A6EA9213C99C2F74B22492B320CF40262A94C1A950A0397F29250B60841EF0",
      "extensions": {},
      "signCount": 1,
      "flags": {
        "userPresent": true,
        "userVerified": true,
        "backupEligible": false,
        "backupState": false,
        "attestedCredentialData": true,
        "extensionDataIncluded": false
      },
      "attestedCredentialData": {
        "aaguid": "01020304-0506-0708-0102-030405060708",
        "coseKey": {
          "keyType": "RSA",
          "algorithm": "RS256",
          "raw":
"A4010303390100205901009EEAC616434B9A4603B286B10089427B1CA3A4C7C8F599A1909A07D4C08E7FB038E0244894450F5129EFE6E00BA54
70862E87DA611255CA0064CB6BAAC891E336FEC6C9D4A04A04F770DBBF7E5831C078B8710B3434F4C5DEA9ACF42F853C81BE1E215FF9ECA1FBA8
2F730163778E2F6AF5F65D66A20C2CEC58EF6B4E399B2A7CA7856C8F6E6E838C06F8884C5E66966D75CBE6DA49035AE2BA3FC7A88D5F6A93557E
1E23E0B13B3C8C0E47CE9A4D9791E0181456177ED790100A7D77723A00A56ECE30FB58A8483B20B1F2230A0A4577DEE35797844C6E0FF3BBDE61
C0E27C0F5373EEA0278F2D72147B3D510C22DF8369E0EBFF9E617511934D1DC76BBB3F32143010001"
        },
        "credentialId": "7AF8A5FDCADE7627"
      }
    }
  },
  "fmt": "none"
}
```

`"RSA"`, `"RS256"`, the whole `raw` value and `"7AF8A5FDCADE7627"` are highlighted yellow; a blue rectangle rings only the `"credentialId"` line.

**29/37**

protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user

## Slide 77

**78**

### **signCount**

Left, hand-written in three coloured columns, each heading marker-highlighted — **RP** (blue), **Evil** (red), **Auth** (green):

| RP | Evil | Auth |
|---|---|---|
| 12 | | 12 |
| 13 | | 13 |
| 14 | | 14 |
| 15 | | 15 |
| 18 | 18 | |
| | | ~~16~~ |
| | | ~~17~~ |
| | | ~~18~~ |
| 19 | | 19 |
| 20 | | |
| 21 | | |

The three struck-out values in the Auth column each carry a large hand-drawn ✗ over them, which partly obscures the digits.

Right, a screenshot of the Passkey Editor tab of a Burp request.

Tabs `Pretty` `Raw` `Hex` **Passkey Editor** (selected); four icon buttons at the right of the tab bar.

`Attacks ⌄`   ☑ Wrap

Flags: ☑ UP  ☑ UV  ☐ BE  ☐ BS

```json
{
  "clientDataJSON": {
    "type": "webauthn.get",
    "challenge":
"SnFcY_gy4PO--D3ueYA6PrxBH56EuW_3BcEjBahjtm9tQq8Yk8JNAeDfxN47a4wgp3yNfwPcEySw8axZXhMiqA",
    "origin": "https://webauthn.io",
    "crossOrigin": false
  },
  "authenticatorData": {
    "rpIdHash": "74A6EA9213C99C2F74B22492B320CF40262A94C1A950A0397F29250B60841EF0",
    "extensions": {},
    "signCount": 13333337,
    "flags": {
      "userPresent": true,
      "userVerified": true,
      "backupEligible": false,
      "backupState": false,
      "attestedCredentialData": false,
      "extensionDataIncluded": false
    },
    "attestedCredentialData": {}
  },
  "signature":
"D3EB54B0EF8A3A07F8B20A00197DABC9C75F43C02857503AA4E5CE18DF883E96378CD0E6D6FD5FEB5522135E
77FDA173BDE16AE256986197BDEA26CE22B6AB0F"
}
```

`13333337` and the `signature` value are highlighted yellow.

**30/37**

protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user

## Slide 78

Full-screen demo screenshot (no slide number or footer). Chrome showing **webauthn.io** with DevTools open, overlaid by a Burp Suite window; a light-blue callout box **DEMO #1 / Plant / Re-sign** sits bottom-right.

**Chrome — webauthn.io**

> # WebAuthn.io
> A demo of the WebAuthn specification
>
> `example_username`  *(input placeholder)*
>
> **Register**   **Authenticate**
> **Advanced Settings**

**DevTools — WebAuthn tab** (`⊡` `Elements  Console  Application  WebAuthn ✕  Sources  »`):

☑ Enable virtual authenticator environment

**Authenticator 90e32**  ⦿ Active   **Remove**

| | |
|---|---|
| UUID | `ec3e8453-ec81-4fee-820c-ff2fe9190e32` |
| Protocol | `ctap2` |
| Transport | `internal` |
| Supports resident keys | Yes |
| Supports large blob | No |
| Supports user verification | Yes |
| Supports hmac-secret | No |
| Supports hmac-secret-mc | No |

**Credentials**

| ID | Is Resi... | RPID | User Handle | Signature Cou... | Actions |
|---|---|---|---|---|---|

`No credentials. Try calling navigator.credentials.create() from your website.`

**New authenticator**

**Burp Suite Professional v2026.6 - 2026-06-21 - licensed to Anvil Ventures, Inc** — HTTP history:

| # | ... | Edited | Status code | Notes | Length | MIME type | Extension | Title | TLS | IP | Cookies |
|---|---|---|---|---|---|---|---|---|---|---|---|
| | `/authentication/verification` | | 200 | Authentication - webauthn.io | 418 | JSON | | | ✓ | 54.184.242.104 | sessionid=1fr4kc... |
| | `/authentication/options` | | 200 | Options - webauthn.io | 611 | JSON | | | ✓ | 54.184.242.104 | |
| | `/registration/verification` *(selected)* | | 200 | Registration - webauthn.io | 316 | JSON | | | ✓ | 54.184.242.104 | |

The request pane (left, green text) shows the reg-verify body, its lines clipped at the left edge; readable line-ends include `...Pf6V5rttwzh4",`, `...grtPf6V5rttwzh4",`, `...F0YViBdKbqkhPJnC90siSSsyDPQCYqlMGpUKA5fyklC2CEHv`, `...lnZJZTTvTtXQjRsN8wk2OzTkaq7T3-lea7bcM4epAEBAycgB`, `...9YPb8Sn4QxH3",`, `...wiY2hhbGxlbmdlIjoicVF5ZWhsRURxaWV4VHUwQnY4aV9Kd1`, `...KE0TXhiSFVGRjJlZG1wbnVMYUg2b2RNaVRSczZJSnZ4aEFNc`, `...dGhuLmlvIiwiY3Jvc3NPcmlnaW4iOmZhbHNlfQ",`, `...BIFfJQ2fPGR_LkyChiNXtpCBb1g9vxKfhDEfc",`, `...klC2CEHvBFAAAAAQAAAAAAAAAAAAAAAAAAAAAAINp_51nZJZ`.

**Response** — `Pretty  Raw  Hex  Render`:

```http
HTTP/2 200 OK
Alt-Svc: h3=":443"; ma=2592000
Content-Type: application/json
Cross-Origin-Opener-Policy: same-origin
Date: Fri, 17 Jul 2026 18:25:11 GMT
Referrer-Policy: same-origin
Server: Caddy
Server: gunicorn
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
Content-Length: 18

{
    "verified":true
}
```

`Memory: 194.7MB of 8.00GB`

## Slide 79

Full-screen demo screenshot (no slide number or footer). Chrome showing **webauthn.io** with DevTools open, overlaid by a Burp Suite window whose **Passkey Editor** tab is open; a light-blue callout box **DEMO #1 / AUTO mode** sits bottom-right.

**Chrome — webauthn.io** (`WebAuthn.io` / `A demo of the WebAu...` / `example_username` / **Register** / **Advanced Settings**).

**DevTools — WebAuthn tab**: ☑ Enable virtual authenticator environment; **Authenticator b05e4**; Protocol `ctap2`; Transport `internal`; Supports resident keys Yes; Supports large blob No; Supports user verification Yes; Supports hmac-secret No; Supports hmac-secret-mc No. Credentials: `No credentials. Try calling navigator.cre...`. **New authenticator**.

**Burp** — `Target  Proxy  Repeater  Extensions  Passkey Editor` | Event log (15) · All issues | Burp Suite Professional v2026.6 - 2026-06-21 - licensed to Anvil Ventures, Inc

**Passkey Editor** — Tabs: **Profiles** (selected) · Guide · About

Profiles:
- ☐ Default (SimpleWebAuthn / generic)
- ☑ webauthn.io   *(selected)*
- ☐ Github  [not active]

Buttons: **Add** · **Copy** · **Delete** · **Restore built-ins**

**Profile: webauthn.io** — ☑ Enabled  ☐ Auto-plant  ☐ Auto re-sign
id: `webauthn.io`   name: `webauthn.io`
default signing alg: `EdDSA (-8)` ⌄   plant attestation: `None` ⌄

**Registration** — verify URL: `CONTAINS` ⌄ | `/registration/verification`   method: `POST`

| field | path/regex | value | encoding | |
|---|---|---|---|---|
| clientDataJSON | ⦿ path ○ regex | `response.response.clientDataJSON` | ⦿ Auto ○ Raw ○ Base64 ○ Base64URL ☐ URL encoded | `decoded ›` |
| attestationObject | ⦿ path ○ regex | `response.response.attestationObject` | ⦿ Auto ○ Raw ○ Base64 ○ Base64URL ☐ URL encoded | `›` |
| authenticatorData | ⦿ path ○ regex | `response.response.authenticatorData` | ⦿ Auto ○ Raw ○ Base64 ○ Base64URL ☐ URL encoded | `›` |
| credentialId | ⦿ path ○ regex | *(empty)* | ⦿ Auto ○ Raw ○ Base64 ○ Base64URL ☐ URL encoded | `decoded ›` |

**Authentication** — verify URL: `CONTAINS` ⌄ | `/authentication/verification`   method: `POST`

| field | path/regex | value | encoding | |
|---|---|---|---|---|
| clientDataJSON | ⦿ path ○ regex | `response.response.clientDataJSON` | ⦿ Auto ○ Raw ○ Base64 ○ Base64URL ☐ URL encoded | `›` |
| authenticatorData | ⦿ path ○ regex | `response.response.authenticatorData` | ⦿ Auto ○ Raw ○ Base64 ○ Base64URL ☐ URL encoded | `decoded ›` |
| signature | ⦿ path ○ regex | `response.response.signature` | ⦿ Auto ○ Raw ○ Base64 ○ Base64URL ☐ URL encoded | `decoded ›` |
| userHandle | ⦿ path ○ regex | `response.response.userHandle` | ⦿ Auto ○ Raw ○ Base64 ○ Base64URL ☐ URL encoded | `decoded ›` |
| credentialId | ⦿ path ○ regex | `response.rawId` | ⦿ Auto ○ Raw ○ Base64 ○ Base64URL ☐ URL encoded | `›` |

**Sample bodies** — Registration body (paste the reg-verify request body): *(empty)*. Authentication body (paste the auth-verify request body): *(empty)*.

Buttons: **Check** · **Prettify JSON** · **Save profile**   `Memory: 388.6MB of 8.00GB`

## Slide 80

Full-screen demo screenshot (no slide number or footer). Chrome showing **github.com/settings/security** with the left settings nav, overlaid by a Burp Suite window whose **Passkey Editor** tab shows the **Github** profile; a light-blue callout box **DEMO #2 / Attack the Registration** sits bottom-right.

**Chrome — GitHub Settings** (`github.com/settings/security`): `matteo-giordano-defcon` — Your personal account. Left nav: Public profile, Account, Appearance, Accessibility, Notifications | Access: Billing and licensing, Emails, **Password and authentication** *(selected)*, SSH and GPG keys, Sessions, Credentials, Organizations, Enterprises, Moderation | Code, planning, and automation: Codespaces, Packages, Copilot, Pages, Saved replies | Security.

**Burp** — `Target  Proxy  Repeater  Extensions  Passkey Editor` | Event log (13) · All issues | Burp Suite Professional v2026.6 - 2026-06-21 - licensed to Anvil Ventures, Inc

**Passkey Editor** — Tabs: **Profiles** (selected) · Guide · About

Profiles:
- ☐ Default (SimpleWebAuthn / generic)
- ☐ webauthn.io  [not active]
- ☑ Github   *(selected)*

Buttons: **Add** · **Copy** · **Delete** · **Restore built-ins**

**Profile: Github** — ☑ Enabled  ☐ Auto-plant  ☐ Auto re-sign
id: `github`   name: `Github`
host match: `EXACT` ⌄ | `github.com`
default signing alg: `ES256 (-7)` ⌄   plant attestation: `None` ⌄

**Registration** — verify URL: `CONTAINS` ⌄ | `/u2f/trusted_devices`   method: `POST`

| field | path/regex | value | encoding |
|---|---|---|---|
| clientDataJSON | ○ path ⦿ regex | `"clientDataJSON":"([^"]+)"` | ○ Auto ○ Raw ○ Base64 ⦿ Base64URL ☐ URL encoded |
| attestationObject | ○ path ⦿ regex | `"attestationObject":"([^"]+)"` | ○ Auto ○ Raw ○ Base64 ⦿ Base64URL ☐ URL encoded |
| authenticatorData | ⦿ path ○ regex | *(empty)* | ⦿ Auto ○ Raw ○ Base64 ○ Base64URL ☐ URL encoded |
| credentialId | ○ path ⦿ regex | `"rawId":"([^"]+)"` | ○ Auto ○ Raw ○ Base64 ⦿ Base64URL ☐ URL encoded |

**Authentication** — verify URL: `CONTAINS` ⌄ | `/session`   method: `POST`

| field | path/regex | value | encoding |
|---|---|---|---|
| clientDataJSON | ○ path ⦿ regex | `%22clientDataJSON%22%3A%22([^%]+)%22` | ○ Auto ○ Raw ○ Base64 ⦿ Base64URL ☐ URL encoded |
| authenticatorData | ○ path ⦿ regex | `%22authenticatorData%22%3A%22([^%]+)%22` | ○ Auto ○ Raw ○ Base64 ⦿ Base64URL ☐ URL encoded |
| signature | ○ path ⦿ regex | `%22signature%22%3A%22([^%]+)%22` | ○ Auto ○ Raw ○ Base64 ⦿ Base64URL ☐ URL encoded |
| userHandle | ○ path ⦿ regex | `%22userHandle%22%3A%22([^%]+)%22` | ○ Auto ○ Raw ○ Base64 ⦿ Base64URL ☐ URL encoded |
| credentialId | ○ path ⦿ regex | `%22rawId%22%3A%22([^%]+)%22` | ○ Auto ○ Raw ○ Base64 ⦿ Base64URL ☐ URL encoded |

**Sample bodies**

Registration body (paste the reg-verify request body):

```text
------WebKitFormBoundaryFtlLBlmK8UEZTOzJ
Content-Disposition: form-data; name="authenticity_token"

8JuWqKqopK3oy7v05O1uHdacwz_Xl5yfi15_dE9j4SZnDC7R7vQiBMgCoNTbs8iZSh_-UgjVoha0Qjm09xdDRA
------WebKitFormBoundaryFtlLBlmK8UEZTOzJ
Content-Disposition: form-data; name="response"

{"type":"public-key","id":"Tjhj0zM4Ze3AkJJTB0bktKpJbU8","rawId":"Tjhj0zM4Ze3AkJJTB0bktKpJbU8","authenticatorAttachment":"platform","response":{"clientDataJSON":"eyJ0eXBlIjoid2ViYXV0aG4uY3JlYXRlIiwiY2hhbGxlbmdlIjoiaFk1bWlhMkZpanRGUUhWelFCc0toTVRQcGZ2N2Jmb053QVYxR1hQN0x4WSIsIm9yaWdpbiI6Imh0dHBzOi8vZ2l0aHViLmNvbSIsImNyb3NzT3JpZ2luIjpmYWxzZX0","attestationObject":"o2NmbXRkbm9uZWdhdHRTdG10oGhhdXRoRGF0YViYOusAJGA4HG8ljoOV0wJvVx8NmnZIjc2DdjmxOu0xZWBdAAAAAPv8MAcVTk7MjAtuAgVX170AFE44Y9MzOGXtwJCSU
```

Authentication body (paste the auth-verify request body):

```text
authenticity_token=4BCkIeAvf7Gx74hakELcxN8swjzK5eED_Qa1A8pG7y4dgMCZUA8yxAhnKWyW0GNSCifBpsKKMSPFQc1qwqHEGQ&webauthn_response=%7B%22id%22%3A%22Tjhj0zM4Ze3AkJJTB0bktKpJbU8%22%2C%22rawId%22%3A%22Tjhj0zM4Ze3AkJJTB0bktKpJbU8%22%2C%22authenticatorAttachment%22%3A%22platform%22%2C%22response%22%3A%7B%22clientDataJSON%22%3A%22eyJ0eXBlIjoid2ViYXV0aG4uZ2V0IiwiY2hhbGxlbmdlIjoiWE9FdUxtUVV0TVpEUXZpVnMwb2g0Z09GOS1mdWtRUGtRdnFjMHZVSIsImNyb3NzT3JpZ2luIjpmYWxzZSwib3RoZXJfa2V5c19jYW5fYmVfYWRkZWRfaGVyZSI6ImRvIG5vdCBjb21wYXJlIGNsaWVudERhdGFKU09OIGFnYWluc3hYlBleCJ9%22%2C%22authenticatorData%22%3A%22OusAJGA4HG8ljoOV0wJvVx8NmnZIjc2DdjmxOu0xZWAdAAAAAA%22%2C%22signature%22%3A%22Ze2AiEA5GP6V6PtH5h4Yk-Q0SDZM7dn2PS0kHbUWLKU99eI1f0%22%2C%22userHandle%22%3A%22ERYW-oUGdrnxCkuQkwAM4OcuiP1uZEHlE_i7qdYK4r72%7D%2C%22clientExtensionResults%22%3A%7B%7D%7D&webauthn-conditional=false&javascript-support=true&webauthn-support=supported&return_to=https%3A%2F%2Fgithub.com%2Flogin&allow_signup=&client_id=&integration=&required_field_49d6=&timestamp=1784330483124&t=58ba14ec1ec961f05384142834180a651a2
```

Buttons: **Check** · **Prettify JSON** · **Save profile**   `Memory: 350.1MB of 8.00GB`

## Slide 81

Full-screen demo screenshot (no slide number or footer). Chrome showing the **GitHub sign-in page** with a browser passkey autofill dropdown, overlaid by a Burp Suite window whose Proxy Intercept pane is idle; a light-blue callout box **DEMO #3 / Attack the Sign in** sits bottom-right.

**Chrome — Sign in to GitHub** (`github.com/login`):

> ### Sign in to GitHub
>
> Username or email address
> `[ | ]`   *(empty, focused)*
> Password
>
> **Sign in** *(green button, partly covered)*
>
> — passkey autofill popover —
> ⓖ **matteo-giordano-defcon**  /  Passkey · Apple Passwords
> ▭ Use Passkey from Another Device
> 🔑 Manage Passwords and Passkeys...
>
> or
> **👥 Continue with passkey**
> **G Continue with Google**
> ** Continue with Apple**
>
> New to GitHub? Create an account

Footer: Terms · Privacy · Docs · Contact GitHub Support · Manage cookies · Do not share my personal information

**Burp Suite Professional v2026.6 - 2026-06-21 - licensed to Anvil Ventures, Inc** — Proxy toolbar: `⚙ Proxy settings` · **Drop** ⌄ · **⊕ Open browser** · ⓘ · ⋮

Centre of the Proxy pane:

> **Intercept is off**
> If you turn Intercept on, messages between Burp's browser and your target servers are held here.
> This enables you to analyze and modify these messages, before you forward them.
> **Learn more**   **Open browser**

`Memory: 374.7MB of 8.00GB`

## Slide 82

**84**

### **Even the big players**

- ◆ <u>CVE-2026-46419</u> (Yubico java-webauthn-server, the reference RP library): returns success for a credential owned by a different user in 2FA / non-discoverable flows.

- ◆ <u>CVE-2025-26788</u> (StrongKey FIDO Server): treats non-discoverable as discoverable and doesn't bind the assertion to the initiating username, so substitute your own credId and sign in as the victim.

- ◆ <u>CVE-2024-12225</u> (Quarkus, CVSS 9.1): leftover default register/login endpoints stay reachable, yielding a login cookie for any username.

- ◆ <u>CVE-2025-12150</u> and <u>CVE-2026-6856</u> (Keycloak): attestation-policy bypass via fmt:none, and an AAGUID-allowlist bypass via packed self-attestation.

**36/37**

protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user

## Slide 83

**85**

### **Checklist + Creativity**

Two columns.

**Checklist**

- signature verified
- credId bound to one user
- UV honored
- UP honored
- origin allowlist (exact)
- crossOrigin rejected
- rpIdHash = sha256(rpId)
- challenge fresh + session-bound
- type create vs get
- COSE alg allowlist
- userHandle validated
- credId length 16-1023
- duplicate credId rejected
- signCount checked
- fmt:none empty
- AAGUID allowlist
- BE/BS coherent
- Token Binding rejected

**Creativity**

- rpId over-scoping
- dangling Related-Origin (/.well-known/webauthn)
- clickjacking / framing (register)
- enrollment step-up
- CSRF on register
- admin-API / Entra enrollment
- post-compromise persistence
- recovery downgrade
- mixed-mode fallback (password / TOTP)
- post-ceremony session binding
- credential-management authz
- leftover default endpoints

**37/37**

protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user

## Slide 84

**5. Cloud sync**

## Slide 85

**87**

### **You are here**

Six boxes forming a journey map, joined by arrows.

Top row, left to right:

- **1. AUTHENTICATOR / PROTOCOL** (filled orange)
- → **2. Hybrid TRANSPORT** (left half orange, right half blue)
- → **3. CLIENT** (left half orange, right half blue)

An arrow leaves **3. CLIENT** downward to **4. RELYING PARTY**.

Bottom row, right to left:

- **4. RELYING PARTY** (filled blue)
- → **5. CLOUD SYNC** (thin orange strip on the left, rest blue) — a red map-pin with a user icon sits on its top-left corner, marking "you are here"
- → **6. USER RECOVERY** (white, unfilled)

Every arrow carries a single arrowhead in the direction of travel: `1 → 2 → 3`, `3 ↓ 4`, `4 → 5 → 6` (the bottom row points leftward).

Legend: <span style="orange">**Research**</span> (orange) · <span style="blue">**Engagement**</span> (blue).

**1/5**

protocol /  auth ·  transport ·  client ·  relying party · **SYNC** ·  user

## Slide 86

**88**

### **Types of Passkeys**

A four-column figure. Each column has a header, a **Type** box (top) and, below an arrow, a **Trust** box (bottom). Bracket labels on the right read **Type** (top row) and **Trust** (bottom row).

| | DEVICE-BOUND | SYNCED | SHARED | EXPORTED |
|---|---|---|---|---|
| **Type** | on one device you hold | synced into a CLOUD ACCOUNT — iCloud Keychain or Google Password Mgr | granted to other users — Apple + most 3rd party: shared vaults | pulled out of the provider — backup/migrate (FIDO CXF / CXP) |
| **Trust** | that device (Secure Enclave / TPM) | the cloud account | every account it's shared to — weakest one wins | only the backup file's own password, if any |

The DEVICE-BOUND **Trust** box is outlined in green; the other three **Trust** boxes are outlined in orange. A downward arrow joins each **Type** box to the **Trust** box beneath it.

**2/5**

protocol /  auth ·  transport ·  client ·  relying party · **SYNC** ·  user

## Slide 87

**89**

### **The Cloud options**

- **First-party** (iCloud Keychain, Google)

   - The vendor owns the hardware, OS, and sync servers

   - keys stay inside vendor HSMs and never leave hardware.

- **Third-party** (Bitwarden, LastPass, Dashlane, 1Password)

   - to stay portable, the key decrypts into ordinary app memory

**3/5**

protocol /  auth ·  transport ·  client ·  relying party · **SYNC** ·  user

## Slide 88

**90**

### **The account still falls the old ways**

A screenshot of a DEF CON 33 conference talk: a dark stage slide headed **DEFCON** (skull-and-crossbones logo) showing a terminal pane with a red banner, a small inset photo of the speaker at a lectern (top-right), and the green-and-gold DEF CON **33** key logo (bottom-right). Caption below:

Spensky, DEF CON 33 (sync-fabric phishing PoC)

- SIM swap, ~19% of passkey account-takeover correlated (↗ <u>Prove</u>)

- Phish the login, drive a real browser as them, walk out with the passkeys (↗ <u>Spensky, DEF CON 33</u>)

- Or go deeper: VaultJacking phishes the vault PIN for the master key, decrypting every synced passkey at once (↗ <u>Brazzell, 2026</u>)

**4/5**

protocol /  auth ·  transport ·  client ·  relying party · **SYNC** ·  user

## Slide 89

**91**

### **Decoy passkeys**

- <u>↗ CASPER (Islam et al., USENIX Security 2025)</u>

   - Hides the real passkey among indistinguishable decoys

   - a key stolen from a cloud breach trips a decoy at login

   - <u>so</u> the RP detects the theft.

   - Detection, not prevention.

- <u>↗ Bicakci et al. (2026)</u>

   - Syncs only REAL ciphertext

   - the decryption key stays in the user's hardware token

   - the cloud is never trusted

   - Prevention, not detection

**5/5**

protocol /  auth ·  transport ·  client ·  relying party · **SYNC** ·  user

## Slide 90

**6. User and recovery**

## Slide 91

**93**

### **You are here**

Six boxes forming a journey map, joined by arrows.

Top row, left to right:

- **1. AUTHENTICATOR / PROTOCOL** (filled orange)
- → **2. Hybrid TRANSPORT** (left half orange, right half blue)
- → **3. CLIENT** (left half orange, right half blue)

An arrow leaves **3. CLIENT** downward to **4. RELYING PARTY**.

Bottom row, right to left:

- **4. RELYING PARTY** (filled blue)
- → **5. CLOUD SYNC** (thin orange strip on the left, rest blue)
- → **6. USER RECOVERY** (thin orange strip on the left, rest blue) — a red map-pin with a user icon sits on its top-left corner, marking "you are here"

Every arrow carries a single arrowhead in the direction of travel: `1 → 2 → 3`, `3 ↓ 4`, `4 → 5 → 6` (the bottom row points leftward).

Legend: <span style="orange">**Research**</span> (orange) · <span style="blue">**Engagement**</span> (blue).

**1/6**

protocol /  auth ·  transport ·  client ·  relying party ·  sync · **USER**

## Slide 92

### **Weaker ways in**

- SMS

- email links

- security questions

- lost device flows

- helpdesk

- OAuth device-code

To the right, the four-panel Anakin/Padmé meme. Top-left: Anakin, captioned **PASSKEYS ARE PHISHING-RESISTANT AND HARDWARE-BACKED**. Top-right: Padmé smiling, **SO THERE'S NO WAY IN, RIGHT?**. Bottom-left: Anakin, silent. Bottom-right: Padmé, expression falling, silent.

**2/6**

**94**

protocol /  auth ·  transport ·  client ·  relying party ·  sync · **USER**

## Slide 93

### **Government says it plainly**

Three quoted boxes from the source document (highlight colours preserved as noted):

> **Attacks**
>
> Attackers are seen to <mark>target account recovery</mark> for both tMFA and <mark>FIDO2 protected accounts, as the recovery process can often be weaker</mark> than the authentication to the account. This is particularly common in two cases:

> The vast majority of websites and apps will offer a 'forgot password' functionality. This typically leverages a code or link sent to the email address registered with the user's account, thereby <mark>effectively reducing the security of the service to that of the email account</mark>.

> credentials, revoking those of the legitimate user. These attacks should be prevented <mark>if only passkeys are used, with no weaker password or tMFA options</mark> supported as a 'fallback'.

("target account recovery" and the two orange phrases are highlighted orange; "FIDO2 protected accounts, as the recovery process can often be weaker" is highlighted blue.)

Source: UK NCSC, *Traditional and FIDO2 credentials for personal use* (2026). ↗ <u>ncsc.gov.uk</u>

**3/6**

**95**

protocol /  auth ·  transport ·  client ·  relying party ·  sync · **USER**

## Slide 94

### **AiTM still works**

- <u>Push Security (2025)</u> named the class: an AiTM kit **rewrites the method-selection page**, so "passkey OR backup code" becomes just "backup code."

- <u>IOActive (2026)</u> weaponized it on Cloudflare Workers: flip the FIDO2 isDefault, or **CSS-hide the passkey**.

Below, two mock **Microsoft "Choose a way to sign in"** dialogs with an arrow between them. Left dialog lists three options — **Face, fingerprint, PIN or security key** (ringed in red), *Approve a request on my Microsoft Authenticator app*, *Use my password* — plus a **Back** button. An arrow points to the right dialog, where the passkey option is gone: only *Approve a request on my Microsoft Authenticator app* and *Use my password* remain, above **Back**.

**4/6**

**96**

protocol /  auth ·  transport ·  client ·  relying party ·  sync · **USER**

## Slide 95

### **When the attacker is already inside**

- **<u>↗ Daffalla et al. (USENIX Security 2025)</u>**

   - assume the attacker is **someone in your life**

   - An intimate partner, a family member

- **User** verification, not **owner** verification

   - FIDO2 never binds a passkey to the biometric that enrolled it

**5/6**

protocol /  auth ·  transport ·  client ·  relying party ·  sync · **USER**

**97**

## Slide 96

### **Abuse scenario**

1. Alex **shares** their phone **PIN** with Billy.

2. One bathroom break later:

   - a. Billy **AirDrops** Alex's TikTok passkey to his own iPhone

   - b. **reads** every message.

3. Alex gets suspicious, **resets the password** , **enrolls** a new passkey.

4. It changes nothing.

**6/6**

protocol /  auth ·  transport ·  client ·  relying party ·  sync · **USER**

**98**

## Slide 97

**Close**

## Slide 98

**Passkeys didn't remove the attack surface. They moved it.**

**100**

## Slide 99

### **Questions?**

- Mail: **matteo.giordano@anvilsecure.com**

- LinkedIn: **linkedin.com/in/giordanomatteo/**

- Website: **matteogiordano.im**

- GitHub: **github.com/anvilsecure/passkey-editor**

- Blogposts:

   - **anvilsecure.com/blog/demystifying-passkeys-under-the-hood-the-protocol.html**

   - **anvilsecure.com/blog/demystifying-passkeys-under-the-hood-the-architecture.html**

   - **anvilsecure.com/blog/demystifying-passkeys-under-attack.html**

**101**

## Slide 100

**Beyond the Ceremony.**
