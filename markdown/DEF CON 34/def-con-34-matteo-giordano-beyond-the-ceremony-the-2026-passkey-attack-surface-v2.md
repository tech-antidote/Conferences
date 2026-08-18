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
vision_verified_pages_changed: 47
vision_verified_pages: 50
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

Google SSO 75.2%, navigator.credentials-only 82.3%, known JS lib 18.6% ↗ <u>Census: Bhardwaj & Sastry, PAM 2026</u>

**3/37**

protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user

## Slide 52

**52**

###### **Microsoft**

\```
mysignins.microsoft.com
\```

\```
POST /api/post/newfido
Content-Type: form-urlencoded
\```

\```
canary=b0f2c1a9 
\```

- `&clientDataJson=eyJ0eXBlIjo `

- `&attestationObject=o2NmbXRkcG `

- `&credentialId=3EHSf9K2mQ  &credentialDeviceType=multiDevice &credentialBackedUp=true &transports=internal,hybrid`

- `&extensions=eyJjcmVkUHJv `

###### **GitHub**

\```
github.com
\```

\```
POST /u2f/trusted_devices
Content-Type: multipart/form-data
\```

\```
------WebKitFormBoundary 
Content-Disposition: form-data;
name="response"
\```

\```
{"id":"3EHSf9K2mQ ",
\```

- `"type":"public-key",`

\```
"response":{
\```

- `"clientDataJSON":"eyJ0 `

- `"attestationObject":"o2N `

\```
},
\```

\```
"clientExtensionResults":{}}
\```

###### **Google**

\```
myaccount.google.com
\```

\```
POST /_/ /batchexecute
Content-Type: form-urlencoded
\```

\```
f.req=[[["GtmsU","[null,null,
null,"eyJ0eXBlIjoi ",
\```

\```
"o2NmbXRkcGFj ",
["internal"],null,1,1]",
null,"generic"]]]
\```

- `&at=AFehe7k9dQ `

- `  idx 3 = clientDataJSON`

- `  idx 4 = attestationObject`

\```
------WebKitFormBoundary --
\```

###### **FLAT FORM FIELDS**

`position:` ~10 flat form params `decode: URL-encoded + Base64URL`

###### **MULTIPART + NESTED JSON**

`position:` spec field names, nested `decode: JSON + Base64URL`

###### **POSITIONAL ARRAYS**

`position:` fields by index in a blob `decode: URL-encoded + Base64URL`

protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user

**4/37**

## Slide 53

### **Decoded fields**

\```
{
\```

- `"clientDataJSON": {`

- `"type": "webauthn.get",`

You want:

- `"challenge": "zYJx-8mHw8wK7vC4qRseSJrDCd01yKIfZk_njXEOoeuQD7CuKUoQ2frvV0NBoJiVZSBgjUYy8vGb-0Lq-BS1wA",`

- `"origin": "https: webauthn.io",`

- `"crossOrigin": false`

- `},`

- `"authenticatorData": {`

- `"rpIdHash": "74A6EA9213C99C2F74B22492B320CF40262A94C1A950A0397F29250B60841EF0",`

- `"flags": {`

- `"userPresent": true,`

- `"userVerified": true,`

- `"backupEligible": false,`

- `"backupState": false,`

- `"attestedCredentialData": false,`

- Traffic detection

   - across vendor wrappers

- Every field decoded: ◆ clientDataJSON

   - authenticatorData

   - signature

   - userHandle

**53**

- `"extensionDataIncluded": false`

- `},`

- `"signCount": 42`

- `},`

- `"signature": "304402207BC3E1F0A2D4C6980B5E3F1A2C4D6E8F0A1B2C3D4E5F60…DDEEFF02",`

- `"userHandle": "6D617474656F2D67696F7264616E6F"`

- `}`

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

**6/37**

protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user

## Slide 55

**55**

**7/37** protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user


> Recovered by OCR — confidence 81/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Passkey Editor
Profiles Guide © About
Profiles
Profile: webauthn.io (Duo py_webauthn)
© Default (SimpleWebAuthn / generic) [not active]
@ webauthn.io (Duo py_webauthn)
3 passkeys-debugger.io (Next.js action) [not active]
© passkeys.io (Hanko) [not active]
© demo.yubico.com {not active]
@ webauthn.lubu.ch [auto-plant] [re-sign]
Add
Copy
Delete
Restore built-ins
Enabled [_] Auto-plant ["] Auto re-sign
id: webauthn.io name: webauthn.io (Duo py_webauthn)
host match: EXACT ~ webauthn.io
default signing alg: EdDSA(-8) ~ plant attestation: None v
Registration
verify URL: CONTAINS v | /registration/verification method: POST
clientDataJSON O path regex _response.response.clientDataJSON © Auto © Raw ©) Base64 () Base64URL [} URL encoded webauthn.create decoded >
attestationObject O path regex response.response.attestationObject O Auto © Raw ©) Base64 () Base64URL [| URL encoded fmt=none - Ed25519 key decoded >
authenticatorData O path regex _response.response.authenticatorData © Auto © Raw ©) Base64 () Base64URL [| URL encoded UP UV AT: signCount 1 decoded >
credentialld O path © regex © Auto © Raw © Base64 ©) Base64URL [] URLencoded decoded >
Authentication
verify URL: CONTAINS v | /authentication/verification method: POST
clientDataJSON O path © regex | response.response.clientDataJSON © Auto © Raw ©) Base64 ©) Base64URL [_) URL encoded webauthn.get decoded >
authenticatorData O path © regex | response.response.authenticatorData © Auto © Raw © Base64 ©) Base64URL [_) URL encoded UP UV - signCount 2 decoded >
signature © path © regex response.response.signature © Auto © Raw ©) Base64 (©) Base64URL [| URL encoded £d25519 - 64B decoded >
userHandle © path © regex | response.response.userHandle © Auto © Raw ©) Base64 () Base64URL [] URL encoded 37B - “webauthnio-asdadsada..." decoded >
credentialld © path © regex | response.rawld © Auto © Raw ©) Base64 () Base64URL [| URL encoded 328 - 893025b4e178... decoded >
Sample bodies
Registration body (paste the reg-verify request body):
{
“defcon34",
{
Authentication body (paste the auth-verify request body):
Check Prettify JSON Save profile all 8 configured field(s) extract cleanly
7/37
protocol / auth - transport - client - RELYING PARTY . sync - user
55
```

## Slide 56

**56**

**8/37**

protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user


> Recovered by OCR — confidence 89/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Profiles Guide About
Profiles
© Default (SimpleWebAuthn / generic) [not active]
@ webauthn.io (Duo py_webauthn)
O passkeys-debugger.io (Next.js action) [not active]
© passkeys.io (Hanko) [not active]
© demo.yubico.com [not active]
@ webauthn.lubu.ch [auto-plant] [re-sign]
Add
Copy
Delete
Restore built-ins
8/37
protocol / auth - transport - client - RELYING PARTY . sync - user
56
```

## Slide 57

**57**

**9/37** protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user


> Recovered by OCR — confidence 84/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
id: webauthn.io name: webauthn.io (Duo py_we
host match: EXACT v
webauthn.io
default signing alg: EdDSA(-8) ~ _ plant attestation: None
9/37
protocol / auth - transport - client - RELYING PARTY . sync - user
57
```

## Slide 58

**58**

**10/37**

protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user


> Recovered by OCR — confidence 77/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Registration
verify URL: CONTAINS v__ /registration/verification method: POST
clientDataJSON © path ©) regex response.response.clientDataJSON }
authenticatorData O path ©) regex response.response.authenticatorData 4
credentialld O path ©) regex }
Authentication
10/37
protocol / auth - transport - client - RELYING PARTY . sync - user
```

## Slide 59

**59**

**11/37**

protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user


> Recovered by OCR — confidence 77/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Authentication
verify URL: CONTAINS v __ /authentication/verification method: POST
clientDataJSON O path ©) regex response.response.clientDataJSON (e)
authenticatorData O path ©) regex response.response.authenticatorData (eo)
signature O path ©) regex response.response.signature (e]
userHandle O path ©) regex response.response.userHandle (e]
credentialld O path ©) regex response.rawld
Sample bodies ra]
protocol / auth - transport - client - RELYING PARTY . sync - user
59
```

## Slide 60

**60**

**12/37**

protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user


> Recovered by OCR — confidence 71/100 on the text kept, 68/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Base64URL | | URL encoded] fmt=n
Base64URL [ | URL encoded]UP U\
Base64URL [_) URLencoded} de
Base64URL | | URL encoded|weba
Base64URL [| URL encoded]UP U)
Base64URL | | URL encoded} Ed25!
—) Base64URL [ | URL encoded]37B -
~) Base64URL [| URL encod: B -
12/37
protocol / auth - transport - client - RELYING PARTY . sync - user
```

## Slide 61

**61**

**13/37**

protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user


> Recovered by OCR — confidence 77/100 on the text kept, 73/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
‘Sample bodies
Registration
verify URL: CONTAINS v __ /registration/verification method: POST
clientDataJSON O path ©) regex | response.response.clientDataJSON O Auto (© Raw ©) Base64 (©) Base64URL [ | URL encoded]webauthn.create decoded >
attestationObject O path © regex | response.response.attestationObject O Auto © Raw ©) Base64 (©) Base64URL [ | URL encoded} fmt=none - Ed25519 key decoded >
authenticatorData O path ©) regex response.response.authenticatorData O Auto © Raw ©) Base64 (©) Base64URL [ | URL encoded} UP UV AT: signCount 1 decoded >
credentialld O path © regex O Auto © Raw © Base64 () Base64URL [) URLencoded| decoded >
Authentication
verify URL: CONTAINS y¥ /authentication/verification method: POST
clientDataJSON O path ©) regex | response.response.clientDataJSON O Auto © Raw ©) Base64 (©) Base64URL [| URL encoded} webauthn.get decoded >
authenticatorData © path © regex response.response.authenticatorData © Auto © Raw ©) Base64 () Base64URL [| URL encoded} UP UV - signCount 2 decoded >
signature O path © regex | response.response.signature O Auto © Raw ©) Base64 (©) Base64URL [| URL encoded} Ed25519 - 64B decoded > (10 }
userHandle O path © regex response.response.userHandle O Auto © Raw (©) Base64 () Base64URL [ | URL encoded} 37B - “webauthnio-asdadsada..." decoded >
O path ©) regex | response.rawld © Auto © Raw ©) Base64 () Base64URL [| URL encoded} 32B - 893025b4e178... decoded >
Registration body (paste the reg-verify request body):
{
“username": "“defcon34",
{
“response": {
“attestationObject": “o2NmbXRkbm9uZWdhdHRTdG1@0GhhdXRoRGFOYViBdKbqkhPJnC90siSSsyDPQCYq LMGpUKAS f yk LC2CEHVBFAAAAAQECAwQFBgc IAQ IDBAUGBwgAIIkwJ bTheLJwnsyC9RTaHJ aNMNxM—Lw5C@CJMa6 LEbTEpA
Authentication body (paste the auth-verify request body):
{
“authenticatorData": "“dKbqkhPJnC90siSSsyDPQCYq LMGpUKAS fyk LC2CEHVAFAAAAAG",
Check Prettify JSON Save profile all 8 configured field(s) extract cleanly
13/37
protocol / auth - transport - client - RELYING PARTY . sync - user
61
```

## Slide 62

**62**

### **Tamper + re-sign**

- Edit any field, re-encode in place

- Any edit breaks the signature

   - re-plant the key

   - re-sign on passthrough

**14/37**

protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user

## Slide 63

**63**

**15/37** protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user


> Recovered by OCR — confidence 90/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Relying Party '
SERVER Client Authenticator
<— forged (1) Auth request (rR) —
(2) challenge, user info, RP info P
— forged >
(5) hash(clientDataJSON) ,
user info,
RP info, RP ID
(6) is User near?
(6.1) can User unlock?
(6.2) Creates the key pair
scoped to the RP ID
(7) attestationObject = {
(8) attestationObject hash(RP ID),
flags = [
UserPresence,
UserVerification,
Attested cred data,
Extension data
(9) attestationObject,
clientDataJSON
“Au
<— forged ——
(10) verify as per [1]
and add credentials to
its storage
1,
LS credential ID,
public Key in CBOR,
AAGUID,
initial sig counter,
extensions
Plant new key
Resign w/ new key
(4) clientDataJSON = {
challenge,
RP origin,
15/37
protocol / auth - transport - client - RELYING PARTY . sync - user
63
```

## Slide 64

**64**

### **Not the first tool**

◆ <u>↗ webauthn-cbor</u> decodes only, no attacks.

- <u>↗ passkey-scanner</u> passive detection.

- ◆ <u>↗ passkey-raider</u> tampers, but by hand. ◆ <u>↗ Burp_FIDO2</u> handles wrappers, rough on production traffic. ◆ <u>↗ Grafneter, Passt</u> -the-Passkey open-sourced at Black Hat this week. ◆ <u>↗ Passkeys.Tools (Jannet)t</u> emulates browser AND authenticator, tampers every field at scale

- **Passkey Editor's lane:** Burp-native, attack dropdown live across Intercept, history, and Repeater, auto re-sign on passthrough, decoding paired with tampering.

**16/37**

protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user

## Slide 65

**65**

### **clientDataJSON**

Raw HTTP request

Passkey Editor

**17/37**

protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user

## Slide 66

**66**

### **challenge**

**18/37** protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user


> Recovered by OCR — confidence 82/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
challenge
Pretty Raw Hex Passkey Editor R Swe
{
"clientDataJSON": {
"challenge": "evil_challenge",
"origin": "https://webauthn. io",
“crossOrigin": false,
“other_keys_can_be_added_here": "do not compare clientDataJSON against a template.
See https://goo.gl/yabPex"
“authenticatorData": {
“rpIdHash": "74A6EA9213C99C2F74B22492B320CF40262A94C1A950A0397F29250B60841EFO",
“extensions”: {},
“signCount": 2,
"flags": {
“userPresent": true,
“userVerifi true,
“backupEligible": false,
“backupState": false,
“attestedCredentialData": false,
“extensionDataIncluded": false
},
“attestedCredentialData": {}
"signature":
18/37
AV protocol / auth - transport - client - RELYING PARTY . sync - user
```

## Slide 67

**67**

### **origin + rpIdHash**

origin

rpIdHash

**19/37**

protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user


> Recovered by OCR — confidence 84/100 on the text kept, 73/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
origin + rpldHash
Pretty Raw Hex Passkey Editor
{
“clientDataJSON": {
“challenge”:
“crossOrigin": false,
“other_keys_can_be_added_here": "do not compare clientDataJSON against a template.
See https://goo.gl/yabPex"
“authenticatorData": {
“rpIdHash": "74AGEA9213C99C2F74B22492B320CF40262A94C1A950A0397F29250B60841EFO",
“signCount": 2,
"flags": {
“userPresent": true,
“userVerified": true,
“backupEligible": false,
“backupState": false,
“attestedCredentialData": false,
“extensionDataIncluded": false
“attestedCredentialData": {}
},
origin
Pretty Raw Hex Passkey Editor
Attacks ~ @ Wrap
{
“clientDataJSON": {
"type": "webauthn.get",
“crossOrigin": false
“authenticatorData": {
"extensions": {},
“signCount": 2,
"flags": {
“userPresent": true,
“userVerified": true,
“backupEligible": false,
“backupState": false,
“attestedCredentialData": false,
“extensionDataIncluded": false
“attestedCredentialData": {}
}
rpldHash
19/37
protocol / auth - transport - client - RELYING PARTY . sync - user
67
```

## Slide 68

**68**

### **Over-scoping the RPid**

**20/37** protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user


> Recovered by OCR — confidence 86/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Over-scoping the RPid
rpld = example.com
(but only app.example.com valid for *.example.com |——>] customerl.example.com —forges>} customer2.example.com
needed)
cross-origin
ACCOUNT
TAKE
OVER
protocol
auth - transport
20/37
client - RELYING PARTY - sync
user
68
```

## Slide 69

**69**

### **Dangling Allowlist Domain**

**21/37** protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user


> Recovered by OCR — confidence 88/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Dangling Allowlist Domain
/well-known/webauthn
allowlist
(a.com, b.com, patner.com)
partner.com LAPSES
attacker buys it @ 10 Slvr | >
attacker origin now
TRUSTED
cross-origin
ACCOUNT
TAKE
OVER
protocol / auth - transport
21/37
client - RELYING PARTY - sync
user
69
```

## Slide 70

**70**

### **attestationObject and authenticatorData**

**22/37**

protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user

## Slide 71

**71**

**23/37**

protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user


> Recovered by OCR — confidence 89/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ATTESTATION OBJECT
AUTHENTICATOR DATA
32 bytes 1 byte 4 bytes (big-endian uint32) variable length variable length if present (CBOR)
RP ID hash FLAGS COUNTER ATTESTED CRED. DATA EXTENSIONS
If Basic or Privacy CA:
If ECDAA:
UV
1
O UP
14
7
AAGUID
L (CREDENTIAL ID
CREDENTIAL PUBLIC KEY
16 bytes
2 bytes LENGTH L
(variable length)
ATTESTATION STATEMENT (in "packed" attestation statement format)
“ecdaaKeyld*: ...
protocol / auth - transport - client - RELYING PARTY - sync -
variable length (COSE_Key)
23/37
user
```

## Slide 72

**72**

**24/37**

protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user


> Recovered by OCR — confidence 80/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ATTESTATION OBJECT
“authData™: ...
i AUTHENTICATOR DATA
i 32 bytes 1 byte 4 bytes (big-endian uint32) variable length variable length if present (CBOR)
RP ID hash FLAGS COUNTER ATTESTED CRED. DATA EXTENSIONS
Po utnentication
' AAGUID L |CREDENTIAL ID | CREDENTIAL PUBLIC KEY
i 16 bytes 2bytes LENGTHL variable length (COSE_Key)
H (variable length)
ATTESTATION STATEMENT (in "packed" attestation statement format)
If Basic or Privacy CA: “alg: ... “sig: ... “xSe"s o.
24/37
protocol / auth - transport - client - RELYING PARTY . sync - user
72
```

## Slide 73

**73**

**25/37**

protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user


> Recovered by OCR — confidence 85/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ATTESTATION OBJECT
i
i AUTHENTICATOR DATA
i 32 bytes 1 byte 4 bytes (big-endian uint32) variable length variable length if present (CBOR)
RP ID hash FLAGS COUNTER ATTESTED CRED. DATA EXTENSIONS
7
AAGUID L_ |CREDENTIAL ID | CREDENTIAL PUBLIC KEY
16 bytes 2 bytes LENGTH L variable length (COSE_Key)
(variable length)
ATTESTATION STATEMENT (in "packed" attestation statement format)
If Basic or Privacy CA: “alg*: ... “sig: ... “xSe":
25/37
protocol / auth - transport - client - RELYING PARTY . sync - user
```

## Slide 74

**74**

### **signature**

**26/37** protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user


> Recovered by OCR — confidence 83/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
signature
Pretty Raw Hex Passkey Editor R Swe
Attacks + Wrap
{
"clientDataJSON": {
“crossOrigin": false
“authenticatorData": {
"extensions": {},
“signCount": 2,
“flags”: {
“userPresent": true,
“userVerified": true,
“backupEligible": false,
“backupState": false,
“attestedCredentialData": false,
“extensionDataIncluded": false
},
“attestedCredentialData": {}
},
"signature":
"585F37FDF8B02D37B69490DF81D684D895 1BB65EA5F39E13F5843E9E67C37A5926F8A09902D9FEGEG831BFAD
}
26/37
protocol / auth - transport - client - RELYING PARTY .
sync - user
74
```

## Slide 75

**75**

### **alg**

**27/37** protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user


> Recovered by OCR — confidence 82/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
alg
Pretty Raw Hex Passkey Editor R Swe
Attacks ~ Wrap
Signing algorithm: RS256 (-257) ~ |Attestation: None v [266 key planted]
{
"clientDataJSON": {
“origin”: "https://webauthn. io",
“crossOrigin": false
},
“attestationObject": {
“attestationStatement": {
“authenticatorData": {
“rpIdHash": "74A6EA9213C99C2F74B22492B320CF40262A94C1A950A0397F29250B60841EFO",
"extensions": {},
“signCount": 1,
"flags": {
“userPresent": true,
“userVerified rue,
“backupEligible": false,
“backupState": false,
“attestedCredentialData": true,
“extensionDataIncluded": false
“attestedCredentialData": {
“aaguid": "01020304-0506-0708-0102-030405060708",
cosekey
4D4729386160C39FC12B660B611765B9C45BC9E9ED548110766221D9C42906A2273CAEF2143010001"
+
},
“fmt":
}
protocol / auth - transport - client - RELYING PARTY . sync - user
27/37
75
```

## Slide 76

**77**

### **credentialId**

**29/37** protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user


> Recovered by OCR — confidence 81/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
credentialld
Pretty Raw Hex Passkey Editor & 5 in
Attacks + Wrap
Signing algorithm: RS256 (-257) - Attestation: None v RS256 key planted
{
"clientDataJSON": {
"type": "webauthn.create",
“crossOrigin": false
},
“attestationObject": {
“attestationStatement": {
},
“authenticatorData": {
"extensions": {},
“signCount": 1,
"flags": {
“userPresent": true,
“userVerified": true,
“backupEligible": false,
“backupState": false,
“attestedCredentialData": true,
“extensionDataIncluded": false
},
“attestedCredentialData": {
“coseKey": {
"keyType": "RSA",
"algorithm": "RS256",
"raw":
“credentialId": "7AF8A5FDCADE7627" |
}
},
“fmt": "none"
29/37
protocol / auth - transport - client - RELYING PARTY . sync -
user
77
```

## Slide 77

**78**

### **signCount**

**30/37** protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user


> Recovered by OCR — confidence 80/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
signCount
Pretty Raw Hex Passkey Editor Q 5s i=
RP evil Auth
Attacks Wrap
“clientDataJSON": {
13 13 “type": "webauthn.get",
“challenge”:
15 “crossOrigin": false
15 “authenticatorData": {
18 1 “rpIdHash": "74A6EA9213C99C2F74B22492B320CF40262A94C1A950A0397F29250B60841EF0",
S "extensions":
“signCount": 13333337,
x "flags": {
“userPresent": true,
“userVerified": true,
“backupState": false,
“attestedCredentialData": false,
“extensionDataIncluded": false
2 O “signature” :
21 }
30/37
AV protocol / auth - transport - client - RELYING PARTY . sync - user
```

## Slide 78


> Recovered by OCR — confidence 80/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
WebAuthn.io
A demo of the WebAuthn specification
hk
Register Authenticate
Advanced Settings
ik {0 Elements Console Application WebAuthnX Sources >> @ 8 2 xX
Enable virtual authenticator environment
7 Authenticator 90e32 @ active Remove
Protocol ctap2
Transport internal
Supports resident keys Yes
Supports large blob No
Supports user verification Yes
Supports hmac-secret No
Supports hmac-secret-me No
Credentials
ID Is Resi... RPID User Handle Signature Cou... Actions
No credentials. Try calling navigator.credentials.create() from your website.
New authenticator
We
Burp Suite Profe 2 21 d to Am Ventures, In:
tor ®@-~ 2
latch and replace ro Proxy settings
decific extensions Search Q @ filteron @ :
Edited Status code Notes Length MIME type Extension Title TS =P Cookies
Jentication/verification 200 Authentication - webauthn.io 418 JSON Y —-54,184,242.104 _sessionid=1fr4kc...
Yentication/options 200 Options - webauthn.io 611 JSON Y __54.184.242.104
t ification 200 Registration - webauthn.io 316 JSON Y_54.184.242.104
| Response GQ== a
& in = Pretty Raw Hex Render = 3
| 2 Alt-Svc: h3=":443"; ma=2592000 |
2zvceuolw 3 Content-Type; application/json
4 Cross-Origin-Opener-Policy: same-origin
5 Date: Fri, 17 Jul 2026 18:25:11 GMT B
Mac OS X 1@_15_7) AppleWebKit/537.36 (KHTML, 6 Referrer-Policy: same-origin
5 7 Server: Caddy Zz
*;v="150", "Google Chrome"; v="150" 8 Server: gunicorn 2.
9 X-Content-Type-Options: nosniff 8
10 X-Frame-Options: DENY
11 Content-Length: 18
12
13 {
YPb8Sn4QxH3", DEM O #1
KE@TXhiSFVGRj J LZG1wbnVMYUg2b2RNaVRSczZJSnZ4aEFNc
3IFFIQZFPGR_LkyChiNXtpCBb1g9vxKfhDEfc", Pla nt
1C2CFHVRFAAAAAOAAAAAAAAAAAAAAAAAAAAAATND 51n7.1Z Re = S | g n
toy
@ Memory: 194.7MB of 8.00GB
```

## Slide 79


> Recovered by OCR — confidence 85/100 on the text kept, 73/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
webauthn.io
WebAuthn.io
A demo of the WebAu
example_username
Register
Advanced Settings
[0 Elements Console Application WebAut
Enable virtual authenticator environment
@ Authenticator b05e4
Protocol ctap2
Transport internal
Supports resident keys Yes
Supports large blob No
Supports user verification Yes
Supports hmac-secret No
Supports hmac-secret-mc No
Credentials
No credentials. Try calling navigator.cre¢
New authenticator
Target Proxy Repeater Extensions
Passkey Editor
Profiles Guide About
Passkey Editor
Burp Suite Professional v2026.6 - 2026-06-21 - licensed to Anvil Ventures, Inc
Profile: webauthn.io
@ Default (SimpleWebAuthn / generic)
@ webauthn.io
Github [not active]
Add
Copy
Delete
Restore built-ins
Event log (15)® All issues
Enabled Auto-plant Auto re-sign
id: webauthn.io name: webauthn.io
default signing alg: EdDSA(-8) - _ plant attestation: None v
Registration
verify URL: CONTAINS v /registration/verification method: POST
clientDataJSON © path regex response.response.clientDataJSON © Auto Raw Base64 Base64URL URLencoded decoded »
attestationObject O path regex response.response.attestationObject © Auto Raw Base64 Base64URL URL er »
authenticatorData O path regex response.response.authenticatorData O Auto Raw Base64 Base64URL URL er >
credentialld O path regex O Auto Raw Base64 Base64URL URL encoded decoded »
Authentication
verify URL: CONTAINS ~ /authentication/verification method: POST
clientDataJSON © path regex response.response.clientDataJSON O Auto Raw Base64 Base64URL URL er »
authenticatorData © path regex _response.response.authenticatorData © Auto Raw Base64 Base64URL URL encoded decoded »
signature O path regex response.response.signature O Auto Raw Base64 Base64URL URL encoded decoded >
userHandle © path regex response.response.userHandle O Auto Raw Base64 Base64URL URL encoded decoded >
credentialld O path regex response.rawid O Auto Raw Base64 Base64URL URL er ,
Sample bodies
Registration body (paste the reg-verify request body):
DEMO #1
Authentication body (paste the auth-verify request body):
AUTO
mode
Check Prettify JSON Save profile
@ Memory: 388.6MB of 8.00GB “iv
```

## Slide 80


> Recovered by OCR — confidence 82/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
< > CG 23 github.com/settings/security
= q) Settings
matteo-giordano-defcon (ma
Your personal account
A Public profile
8 Account
& Appearance
tr Accessibility
Q Notifications
Access
6 Billing and licensing »
& Emails
| © Password and
authentication
& SSH and GPG keys
@ Credentials
Organizations
® Enterprises
(© Moderation v
Code, planning, and automation
& Codespaces
@ Packages
& Copilot v
& Pages
© Saved replies
Security
Target Proxy Repeater Extensions
Passkey Editor
Profiles Guide About
Profiles
Burp Suite Professional v2026.6 - 2026-06-21 - licensed to Anvil Ventures, Inc
Passkey Editor
Profile: Github
@ Default (SimpleWebAuthn / generic)
© webauthn.io [not active]
@ Github
Add
Copy
Sign i Delete
Restore built-ins
Go
Sig
Ap
Sig
Two-fé
your)
Event log (13) All issues
Enabled
id: github
host match; EXACT v _ github.com
Auto-plant Auto re-sign
name: Github
default signing alg: ES256 (-7) Y plant attestation: None v
Registration
verify URL: CONTAINS v /u2f/trusted_devices method: POST
clientDataJSON path © regex "clientDataJSON":"(**}+)" Auto () Raw ©) Base64 © Base64URL URL er »
attestationObject path © regex "attestationObject":"(*"]+)" Auto Raw Base64 © B B4URL URL er >
authenticatorData © path ©) regex O Ato Raw Base64 B: URL URL er »
credentialld path © regex “rawld*:"((*"}+)" Auto Raw Base64 © S4URL URL er »
Authentication
verify URL: CONTAINS y /session method: POST
clientDataJSON path © regex %22clientDataJSON%22%3A%22(%]+)%22 Auto _) Raw Base64 © Base64URL URL er »
authenticatorData path © regex %22authenticatorData%22%3A%22(" %]}+)%22 Auto Raw Base64 © Base64URL URL encoded decoded >
signature path © regex %22signature%22%3A%22(%]+)%22 Auto (©) Raw ©) Base64 © Base64URL || URL er decoded »
userHandle >) path © regex %22userHandle%22%3A%22((0%]+)%22 Auto () Raw ©) Base64 © Base64URL |) URLencoded decoded >
credentialld © path © regex %22rawld%22%3A%22( %]+)%22 Auto Raw Base64 © Base64URL URL er »
Sample bodies
Registration body (paste the reg-verify request body):
Content-Disposition: form-data; name="authenticity_token"
Authentication body (paste the auth-verify request body):
58bal4eclec961f05384142834180a651a2
Check Prettify JSON Save profile
DEMO #2
Attack the
Registration
@ Memory: 350.1MB of 8.00GB “ov
```

## Slide 81


> Recovered by OCR — confidence 85/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Burp Suite Prof ional v2026.6 - 2026-06-21 - licensed to Anvil Ventures, inc
ce © Proxy settings
O Drop ® Open browser (Q) :
Sign in to GitHub
Username or email address
Password oO matteo-giordano-defcon
Passkey - Apple Passwords
[0 Use Passkey from Another Device
a | © Manage Passwords and Passkeys... On
or
&y Continue with passkey G
G Continue with Google
© Continue with Apple Intercept is off
m ies If you tum Intercept on, messages between Burp's browser and your target servers are held here.
New to GitHub? Create an account This enables you to analyze and modify these messages, before you forward them.
Lea mere
DEMO #3
Attack the
Sign in
e Terms Privacy Docs Contact GitHub Support Manage cookies Do not share my personal information @® Memory: 374.7MB of 8.00GB +1
```

## Slide 82

**84**

### **Even the big players**

- <u>CVE-2026-46419</u> (Yubico java-webauthn-server, the reference RP library): returns success for a credential owned by a different user in 2FA / non-discoverable flows.

- <u>CVE-2025-26788</u> (StrongKey FIDO Server): treats non-discoverable as discoverable and doesn't bind the assertion to the initiating username, so substitute your own credId and sign in as the victim.

- <u>CVE-2024-12225 (Quarkus, CVSS 9.1): leftover default register/login endpoints</u> stay reachable, yielding a login cookie for any username.

- <u>CVE-2025-12150 and CVE-2026-6856 (Keycloak): attestation-policy bypass via</u>

- fmt:none, and an AAGUID-allowlist bypass via packed self-attestation.

**36/37**

protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user

## Slide 83

**85**

### **Checklist + Creativity**

###### **Checklist**

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

###### **Creativity**

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

- duplicate credId rejected

- signCount checked

- fmt:none empty

- AAGUID allowlist

- BE/BS coherent

- Token Binding rejected

**37/37**

protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user

## Slide 84

**5. Cloud sync**

## Slide 85

**87**

### **You are here**

**1/5** protocol /  auth ·  transport ·  client ·  relying party · **SYNC** ·  user


> Recovered by OCR — confidence 91/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
You are here
1. AUTHENTICATOR /
PROTOCOL
———|>|_ 2. Hybrid TRANSPORT
6. USER RECOVERY
5. CLOUD SYNC
Engagement
protocol
3. CLIENT
4. RELYING PARTY
4/5
auth - transport - client - relying party - SYNC - user
87
```

## Slide 86

**88**

### **Types of Passkeys**

**2/5** protocol /  auth ·  transport ·  client ·  relying party · **SYNC** ·  user


> Recovered by OCR — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Types of Passkeys
DEVICE-BOUND
on one device
you hold
SYNCED
SHARED
synced into a
CLOUD ACCOUNT
iCloud Keychain or
Google Password Mgr
EXPORTED
granted to other users
Apple + most 3rd party:
shared vaults
pulled out of the provider
backup/migrate
(FIDO CXF / CXP)
that device
(Secure Enclave /
TPM)
the cloud account
every account it's
shared to
weakest one wins
only the backup
file's own
password, if any
protocol / auth - transport - client - relying party - SYNC - user
Type
Trust
2/5
88
```

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

Spensky, DEF CON 33 (sync-fabric phishing PoC)

- SIM swap, ~19% of passkey account-takeover correlated (↗ <u>Prove)</u>

- Phish the login, drive a real browser as them, walk out with the passkeys (↗ <u>Spensky, DEF CON 33)</u>

- Or go deeper: VaultJacking phishes the vault PIN for the master key, decrypting every synced passkey at once (↗ <u>Brazzell, 2026)</u>

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

### **You are here**

**93**

**1/6** protocol /  auth ·  transport ·  client ·  relying party ·  sync · **USER**


> Recovered by OCR — confidence 93/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
You are here
1. AUTHENTICATOR /
PROTOCOL
6. USER RECOVERY
5. CLOUD SYNC
Engagement
protocol
3. CLIENT
4. RELYING PARTY
4/6
auth - transport - client - relying party - sync - USER
93
```

## Slide 92

### **Weaker ways in**

- SMS

- email links

- security questions

- lost device flows

- helpdesk

- OAuth device-code

**2/6 94** protocol /  auth ·  transport ·  client ·  relying party ·  sync · **USER**

## Slide 93

### **Government says it plainly**

Source: UK NCSC, Traditional and FIDO2 credentials for personal use (2026). ↗ <u>ncsc.gov.uk</u>

**3/6**

**95**

protocol /  auth ·  transport ·  client ·  relying party ·  sync · **USER**

## Slide 94

### **AiTM still works**

- <u>Push Security (2025)</u> named the class: an AiTM kit **rewrites the method-selection page** , so "passkey OR backup code" becomes just "backup code."

- <u>IOActive (2026)</u> weaponized it on Cloudflare Workers: flip the FIDO2 isDefault, or **CSS-hide the passkey** .

**4/6**

**96**

protocol /  auth ·  transport ·  client ·  relying party ·  sync · **USER**

## Slide 95

### **When the attacker is already inside**

- **<u>↗ Dafalla et al. (USENIX Security 2025)f</u>**

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
