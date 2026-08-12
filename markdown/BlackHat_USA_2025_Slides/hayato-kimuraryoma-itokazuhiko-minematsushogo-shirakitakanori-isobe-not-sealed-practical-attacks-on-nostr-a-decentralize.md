---
title: "Not Sealed Practical Attacks on Nostr, a Decentralized Censorship-Resistant Protocol"
speakers: ["Hayato Kimura", "Ryoma Ito", "Kazuhiko Minematsu", "Shogo Shiraki", "Takanori Isobe"]
conference: "Black Hat"
conference_full: "Black Hat USA 2025"
edition: "USA"
year: 2025
source_pdf: "BlackHat_USA_2025_Slides/Hayato Kimura&Ryoma Ito&Kazuhiko Minematsu&Shogo Shiraki&Takanori Isobe_Not Sealed Practical Attacks on Nostr, a Decentralized Censorship-Resistant Protocol.pdf"
pages: 70
sha256: "70e626a820b0d35cd80e8dd1967f0d605f5d93f0d2e71abac7b25d66cd200409"
text_chars: 31401
ocr_pages: 6
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T22:54:39Z"
---
# Not Sealed Practical Attacks on Nostr, a Decentralized Censorship-Resistant Protocol

**Speakers:** Hayato Kimura, Ryoma Ito, Kazuhiko Minematsu, Shogo Shiraki, Takanori Isobe  
**Conference:** Black Hat USA 2025  
**Source:** `BlackHat_USA_2025_Slides/Hayato Kimura&Ryoma Ito&Kazuhiko Minematsu&Shogo Shiraki&Takanori Isobe_Not Sealed Practical Attacks on Nostr, a Decentralized Censorship-Resistant Protocol.pdf` (70 pages)


## Slide 1

Not Sealed: **Practical Attacks on Nostr, a Decentralized Censorship-Resistant Protocol** Keywords: Distributed SNS, signature verification bypass, CBC mode malleability, cache poisoning, plaintext recovery Speakers: Hayato Kimura Contributors: Ryoma Ito, Kazuhiko Minematsu, Shogo Shiraki and Takanori Isobe **(Also, IEEE EuroS&P2025)**

#BHUSA @BlackHatEvents

## Slide 2

### Our Team

### Hayato Kimura

- Researcher at NICT, Japan

   - ( **N** ational **I** nstitute of information and **C** ommunications **T** echnology)

- Ph.D. candidate at The University of Osaka

- Research field: Applied Cryptography & Protocol Security

Ryoma Ito Kazuhiko Minematsu (NICT) (NEC)

Shogo Shiraki (University of Hyogo)

Takanori Isobe (The University of Osaka)

#BHUSA @BlackHatEvents

2

## Slide 3

# The dawn of the Distributed SNS

#BHUSA @BlackHatEvents

3

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
BRIEFINGS
The dawn of the Distributed SNS
FORBES DIGITAL ASSETS
Jack Dorsey Backs Ocean In Shifting Toward
Decentralized Bitcoin Mining
By Susie Violet Ward, Contributor. © Bitcoin journalist and financial analyst b...  v | Follow Author
Why Nostr Today Feels Like Bitcoin In
2012: An Interview With Vitor Pamplona
May 16, 2025 — 04:56 pm EDT
Written by Frank Corva for Bitcoin Magazine >
Published Dec 01, 2023, 03:56am EST
Jack Dorsey pumps $10M into
. a nonprofit focused on open
Mastodon’s Growth, and Communities Branchin F P
e EME Se SEM ele Threads Surpasses 350M Monthly
Users: A Growth Milestone with
Mixed Monetization Prospects
April 30,2023 / Hilda Bastian / Science Communication
Meet @Fiatjaf, The Myster
Nostr Creator Who Has Lt Qijjpem: eotemeor- suv, 2008
18 Million Users And $5 Milton Saggpeeeeeees
>». anal sces Is distributed SNS, which has grown rapidly after Earon Mask's acquisition of Twitter, sluggish?
From Jack Dorsey
Nathaniel Stone + Wednesday, Apr 30, 2025 6:54 pm ET
Bluesky adds 1m new members as users
flee X after the US election
Social media platform has become a ‘refuge’ from the far-
right activism on X, experts say, after Elon Musk teamed up
with Donald Trump
```

## Slide 4

# Distributed SNS

Self-sovereign Federated
Authentication
by a single service provider
User auth
Signed Post Post
Signing Key (identity)

Service providers are independent User’s identity is managed by user

Service providers are interconnected But identity managed like a **centralized** SNS

#BHUSA @BlackHatEvents

4

## Slide 5

# Distributed SNS

**<u>Self-sovereign</u>**

**<u>Federated</u>** Quite different architecture from traditional centralized SNS / messaging Authentication **Research Questions** by a single service provider

- How to trust public keys?

- • New architecture, new attack surface?User auth

Signed Post Post Signing Key (identity)

Service providers are independent User’s identity is managed by user

Service providers are interconnected But identity managed like a **centralized** SNS

#BHUSA @BlackHatEvents

5

## Slide 6

# What is Nostr?

- **Open, censorship-resistant social-network**

- **1.1 million registration users**

- **No centralized authority, users must manage Public-key-based identities**

- A secp256k1 key pair defines who you are; every post carries a signature

- • **Zero barriers to participation**

   - Anyone can run a relay server or client

   - Covers most of the attractive features of centralized SNS

      - E.g., Post, Profile, Encrypted DMs, Micro payment, Multiple device sign-in

#BHUSA @BlackHatEvents

6

## Slide 7

## Cryptography in Nostr Specs

- NIP = Nostr implementation possibilities

- 56+ specifications

- 1 mandatory protocol & 55+ optional protocols

• 4 key feature protocols

NIP-01: Event Structure & Signing

NIP-04: Encrypted DM

Signed Post ECDH + AES-CBC
+ Signing
Signing Key (identity)

NIP-46: NIP-57: Delegation (multi-device) Micro payment Allow to post Send Token via ECDH + AES-CBC + Signing

#BHUSA @BlackHatEvents 7

## Slide 8

## Our Contributions

- •

- Analyze 56 specs Implement 8 attacks

- • •

- Analyze 9 implementations Breaking confidentiality,

- • Find 7 vulnerabilities on integrity, availability

- 4 key features

- Propose mitigation

- • Two years of persistent disclosure process

First Comprehensive Analysis

Practical Attacks & PoCs

Mitigation

- & Responsible Disclosure

#BHUSA @BlackHatEvents

8

## Slide 9

## Our findings

• • • Breaking integrity on Breaking confidentiality on All items Encrypted DMs (e.g., Profile, Contact List Encrypted DMs…) • Impersonating to another user

Hijacking micro payment (subset of impersonating)

**These are not theoretical flaws—they enable practical exploitation** The required threat model varies Some attacks assume a malicious user; others work under a malicious relay server

#BHUSA @BlackHatEvents

9

## Slide 10

## PoC: Note (Post) forgery (simple)

#BHUSA @BlackHatEvents

10

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisa hat
BRIEFINGS
PoC: Note (Post) forgery (simple)
Basic Forgery Attack on All Events
Target: Note (Post) Forgery
vulnerability : lack of signature verification on client
Timeline ©
Goal: display forged Bob's Note(Post) on Alice(Victim) device.
This server doesn't have a server-side signature verification.
This server is non-malicious legitimate relay server and complies on Nostr spec.
@EQ 0B iphone-1234
Timeline ©
Android:
Alice,Plebstr v@.7.6+56 (Android) Victim's app
Compare with Amethyst v@.80.7 (Android) that
performs signature verification
% echo 'Post from Real Bob account'
iPad: Bob, Plebstr v@.7.6+56 (iPad 0S) Victim's app
Bob's public key:
iPhone12 mini:
| Alice, Plebstr v0.7.6+56 (i0S) Victim's app 10
yi
```

## Slide 11

## PoC: Encrypted DMs forgery & URL recovery

#BHUSA @BlackHatEvents

11

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pifeachat
BRIEFINGS
(ven
4 % less ./log/dnsmasq.log
py
> Relay Server
cho “This i
is mu.test
B% python3 -m http.server
ving HTTP on :: port 8000 (http://[::]:8000/)
```

## Slide 12

PoC: Hijacking micro payment ← Profile forgery (cache) & DMs forgery

#BHUSA @BlackHatEvents

12

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisa hat
BRIEFINGS
PoC: Hijacking micro payment <— Profile forgery (cache) & DMs forgery
Preliminaries:
Title: 1. Bob sets his correct Bitcoin lightling address
PoC of money transfer fraud. in his profile.
It consists of Encrypted DM forgery |2. Attacker's address is different from Bob's one.
and breaking Profile integrity 3. Alice, Bob can send and receive messages via DM.
through the signature bypass
Malicious QR for NIP-46
s It contains the Victim2's public key
CL emmiaas | "alicious Relay Server and URL of attacker's web socket server.
Manipulate Bob's profile
+3 Ome » 7 100% and replace Bob's Bitcoin Lighting address with the attacker's 4
jone.
Lightning Address
Nostr Connect Playground
Nostr ID b889ff5b1513b641e2a139/661a661364979c5beee9 184218f0ef42ab558e9d4
Status @ Disconnected
n859587387$10618251981c7448aB4a08ed805803204d6d" f
13cef0f9264cteaadds
Connect with Nostr
nostrconnect;//24f235e8aif16defb85c
1 catch_event_from_connect — -bash — 55%6
:catch_event_from_connect$ I
tAttacker's wallet tVictim2(Bob) tVictim1(Alice)
and Victom2's wallet .
on iPad on iPhone
Damus v1.5 Damus v1.5
12
```

## Slide 13

<u>Why does it happen?</u> Cryptographic protocol design flaw + Implementation flaw

• <u>on Breaking integrity</u> All items

   - <u>on</u> •

   - <u>Breaking confidentiality Hijacking</u> micro payment Encrypted DMs (subset of impersonating)

- Impersonating to another user

- Lack of key separation

- • Signature verification • Receiver-side preview

- Bypass generation

• Verification Bypass

#BHUSA @BlackHatEvents 13

## Slide 14

<u>Why does it happen?</u> Cryptographic protocol design flaw + Implementation flaw

Step by step attack tracing Breaking… Plaintext integrity (simple / cache poisoning) Ciphertext integrity Ciphertext confidentiality

Remark: mandatory signing specification (simplified) NIP-01: Event Structure & Signing Signed Post Signing Key (identity)

#BHUSA @BlackHatEvents

14

## Slide 15

Breaking… Plaintext integrity (simple)

Remark: mandatory signing specification (details depending on specification)

Relay Server
Signing with  Verifying Event with
Alice’s private key Alice’s public key
Data Data
Data
Accept Event or Reject it
Event Signed Event
Signed Event
Alice Profile Bob

#BHUSA @BlackHatEvents 15

## Slide 16

Breaking… Plaintext integrity (simple)

### Details depending on many **actual** implementations

Relay Server
Signing with  Verifying Event with
Alice’s private key Alice’s public key
Data Data
Data Always Accept Event  or Reject it
Event Signed Event
Signed Event
Alice Profile Bob

#BHUSA @BlackHatEvents 16

## Slide 17

Breaking…
Event Type Details depending on Data  many  actual  implementations
Plaintext integrity
(simple)Profile Name, Bio,
BTC address
Encrypted DM Encrypted Msg
Post Plaintext Msg
Relay Serve r
etc… Signing with  Verifying Event with
Alice’s private key Alice’s public key
Data Data
Data Always Accept Event  or Reject it
Event Signed Event
Signed Event
Alice Profile Bob

#BHUSA @BlackHatEvents 17

## Slide 18

##### Breaking… Plaintext integrity (simple)

### Details depending on many **actual** implementations

There is no Verify(Sig) call in the event handling!

#BHUSA @BlackHatEvents 18

## Slide 19

##### Breaking… Plaintext integrity (simple)

### Case : Alice publishes her Profile & Bob subscribes it

•
Alice’s display name
•
Alice’s bio

•
Alice’s bio
•
Alice’s Bitcoin(sat) address etc…
Relay Server
Signing with  Verifying Event with
Alice’s private key Alice’s public key
Always Accept Event  or Reject it
Profile Profile
Profile
Event Signed Event
Signed Event
Alice Profile Bob

#BHUSA @BlackHatEvents 19

## Slide 20

Breaking… Plaintext integrity (simple)

### Profile Forgery on Plebstr, FreeFrom Attacker also can publish Alice’s Profile

•
Alice’s display name
•
Alice’s modified bio
•
Attacker’s Bitcoin(sat) address
Relay Server
Verifying Event with
Copy Alice’s Event and modified it
Alice’s public key
Always Accept Event  or Reject it
Profile Profile Profile
Signed Event
Attacker Bob
Profile

#BHUSA @BlackHatEvents 20

## Slide 21

Breaking… Plaintext integrity (cache poisoning)

<u>On the Profile validation</u> of Damus (v1.5(8) & v1.6 (29) ) Attack on a popular Nostr client

Relay Server
Signing with
Alice’s private key
Profile Profile
Event
Signed Event
Alice Profile

Verifying Event with
Alice’s public key
Accept Event or Reject it
Profile
Signed Event
Bob

#BHUSA @BlackHatEvents 21

## Slide 22

Breaking… Plaintext integrity (cache poisoning)

<u>On the Profile validation</u> of Damus (v1.5(8) & v1.6 (29) ) Attack on a popular Nostr client

Sig verification in place

Relay Server Signing with Alice’s private key Profile Profile Event Signed Event

Alice Profile

Verifying Event with
Alice’s public key
Accept Event or Reject it
Profile
Signed Event
Bob

#BHUSA @BlackHatEvents 22

## Slide 23

Breaking… Plaintext integrity (cache poisoning)

<u>On the Profile validation</u> of Damus (v1.5(8) & v1.6 (29) )

### **Let‘s see stack trace**

Sig verification in place

validate_event

Secp256k1. Schnorr.Verify

#BHUSA @BlackHatEvents 23

## Slide 24

Breaking… Plaintext integrity (cache poisoning)

<u>On the Profile validation</u> of Damus (v1.5(8) & v1.6 (29) )

### **Let‘s see stack trace**

EventCache & reference …?

guard_valid_event

?

validate_event

Secp256k1. Schnorr.Verify

#BHUSA @BlackHatEvents 24

## Slide 25

##### Breaking… Plaintext integrity (cache poisoning)

<u>On the Profile validation</u> of Damus (v1.5(8) & v1.6 (29) ) **Let‘s see stack trace**

EventCache.is_event_valid(ev.id) Check past signature verification result

- Return **true** if the event is found and the past verification **succeeded**

- • Return **false** otherwise.

guard_valid_event

?

validate_event

Secp256k1. Schnorr.Verify

#BHUSA @BlackHatEvents 25

## Slide 26

Breaking…  On the Profile validation of Damus (v1.5(8) & v1.6 (29) )
Plaintext integrity
Let‘s see stack trace
(cache poisoning)
If past validation
guard_valid_event
validate_event
nothing
Secp256k1.
is_event_validate(ev.id)
Schnorr.Verify
get_cache_data(ev.id).
succeeded
validated
Return as
validation succeeded

<u>On the Profile validation</u> of Damus (v1.5(8) & v1.6 (29) )

#BHUSA @BlackHatEvents 26

## Slide 27

Breaking… Plaintext integrity (cache poisoning)

<u>On the Profile validation</u> of Damus (v1.5(8) & v1.6 (29) )

**Let‘s see stack trace**

If past validation How can we control this decision point? validate_event

guard_valid_event

nothing

Secp256k1. is_event_validate(ev.id) Schnorr.Verify get_cache_data(ev.id). **succeeded** validated Return as validation succeeded

#BHUSA @BlackHatEvents 27

## Slide 28

Breaking… Plaintext integrity (cache poisoning)

<u>On the Profile validation</u> of Damus (v1.5(8) & v1.6 (29) ) **Let‘s see stack trace**

If past validation
guard_valid_event How can we control this decision point?
validate_event
nothing
Secp256k1.
is_event_validate(ev.id)
Attacker can control this Event IDSchnorr.Verify
get_cache_data(ev.id).
succeeded
validated
Return as
validation succeeded

#BHUSA @BlackHatEvents 28

## Slide 29

Breaking…  On the Profile validation of Damus (v1.5(8) & v1.6 (29) )
Plaintext integrity
(cache poisoning) When Bob received an Alice’s Event (id==  0x…ac)
If past validation
guard_valid_event
validate_event
nothing
Save result
Secp256k1.
is_event_validate(0x…ac)
Schnorr.Verify to cache
get_cache_data(0x…ac).
succeeded
validated
Return as
validation succeeded

#BHUSA @BlackHatEvents

29

## Slide 30

Breaking…  On the Profile validation of Damus (v1.5(8) & v1.6 (29) )
Plaintext integrity
(cache poisoning) Attacker sends a fake event with an ID (  0x…ac  ) to Bob
If past validation
guard_valid_event
validate_event
nothing
Save result
Secp256k1.
is_event_validate(0x…ac)
Schnorr.Verify to cache
get_cache_data(0x…ac).
succeeded
validated
Return as
validation succeeded

#BHUSA @BlackHatEvents 30

## Slide 31

Breaking… Plaintext integrity (cache poisoning)

<u>On the Profile validation</u> of Damus (v1.5(8) & v1.6 (29) ) **How to derivate Event ID on Nostr** Event ID : ev.id = SHA-256(“0”||{ev.data}) The event ID is a deterministic value derived from ev.data Root cause: Refer to the cache using the ID without recalculating it

Mitigation

The ID should be recalculated if {ev.data} is modified.

#BHUSA @BlackHatEvents

31

## Slide 32

> Breaking… <u>On the Profile validation</u> of Damus (v1.5(8) & v1.6 (29) ) Plaintext integrity

> (cache poisoning) **Mitigation: Event ID validation** Original: No ID validation

### Patched: Ensure ID validation

#BHUSA @BlackHatEvents 32

## Slide 33

##### Breaking… Plaintext integrity

Validation

### <u>Takeaway : Plaintext Integrity</u>

Cache

Developer should do integrated security test !

#BHUSA @BlackHatEvents

33

## Slide 34

##### Breaking… Plaintext integrity

### <u>Takeaway : Plaintext Integrity</u>

Authentication Bypass

Developer should do integrated security test !

#BHUSA @BlackHatEvents 34

## Slide 35

##### Breaking…

### <u>Takeaway : Plaintext Integrity (2)</u> Plaintext integrity

- In centralized settings, cryptographic flaws often remain “potential risks”

- • In self-sovereign decentralized systems like Nostr, they become immediately exploitable

   - Nostr does not have centralized authority

   - Nostr does not provide user authentication by default

Signing Key User auth User auth
Verifying Key
Sign Post Subscribe
Verify
Post Subscribe
Nostr
Centralized SNS

#BHUSA @BlackHatEvents 35

## Slide 36

Step by step attack tracing Breaking… Plaintext integrity (simple / cache poisoning)

### Remark: Encrypted Direct Messages specification (simplified)

NIP-04: Encrypted DM

Ciphertext integrity Ciphertext confidentiality

ECDH + AES-CBC
+ Signing

#BHUSA @BlackHatEvents 36

## Slide 37

Encrypted DM Spec

Alice’s Public key (Verifying key)

Alice’s Private key (Signing key)

Bob’s Public key (Verifying key) Bob’s Private key (Signing key)

Relay servers

#BHUSA @BlackHatEvents

37

## Slide 38

Encrypted DM Spec

ECDH over secp256k1

Bob’s Public key (Verifying key) Bob’s Private key (Signing key) Alice’s Public key (Verifying key) Shared Encryption Key

Alice’s Public key (Verifying key)

Alice’s Private key (Signing key) Bob’s Public key (Verifying key) Shared Encryption Key

Relay servers

#BHUSA @BlackHatEvents

38

## Slide 39

Encrypted DM Spec
ECDH over secp256k1
Alice’s Public key
(Verifying key)
Alice’s Private key
(Signing key)
Bob’s Public key
(Verifying key)
Encrypt-then-sign
Shared Key (AES-CBC&Schnorr sign)
Msg E Sign
Relay servers

Bob’s Public key
(Verifying key)
Bob’s Private key
(Signing key)
Alice’s Public key
(Verifying key)
Shared Key
Verify D Msg
#BHUSA @BlackHatEvents

39

## Slide 40

## Encrypted DM Forgery

### Attacker’s Goal : Change decrypted Msg to attacker’s  Msgadv e.g., "Send me BTC"

“Hi”

“Send me BTC”

### ECDH + AES-CBC

+ Signing

#BHUSA @BlackHatEvents

40

## Slide 41

## Encrypted DM Forgery

Assumption1: Signature verification is skipped **<u>on the implementation</u>** (explained earlier)

Alice’s Private key
(Signing key)
Shared Key

Shared Key
“Hi” E Sign

Encrypt ~~-then-sign~~ (AES-CB ~~C&Schnorr sign)~~

Relay servers

Alice’s Public key
(Verifying key)
Shared Key
D “Hi”
#BHUSA @BlackHatEvents

**41**

## Slide 42

Encrypted DM Forgery Assumption2: Threat model

- Attacker is a user of Nostr

- Attacker cannot read/write to “Shared Key”

- Attacker can **freely fetch ciphertext** from relay relays Nostr does not include user authentication on servers by default Simplified encryption specs (AES-CBC)

Shared Key

E

“Hi”

& Threat model

R/W ciphertext

Relay servers

Shared Key
D “Hi”
#BHUSA @BlackHatEvents

**42**

## Slide 43

Encrypted DM Forgery Problem : Verification bypass is not enough to achieve practical forgery on DMs Reason  : CBC Allows Bit Flipping – But decryption result blinds for the attacker (simplified) Bit flipping on Message Encryption

1 block CBC-mode encryption
X ← iv ⨁ “Hi” || pad
X
Ek C, iv
Shared Key (k)
Shared Key
“Hi” E
Relay servers

Shared Key

D Msgdec

#BHUSA @BlackHatEvents

43

## Slide 44

## Encrypted DM Forgery

Problem : Verification bypass is not enough to achieve practical forgery on DMs Reason  : CBC Allows Bit Flipping – But decryption result blinds for the attacker (simplified) Bit flipping on Message Encryption

1 block CBC-mode encryption
X ← iv ⨁ “Hi” || pad
iv’ ← iv ⨁ Flip
X
Ek C, iv
Shared Key (k)
“Hi” E
Relay servers

1 block CBC-mode decryption
C Dk X ⨁ iv’
Msgdec = ?? (unknown)
Shared Key
D
Msgdec

#BHUSA @BlackHatEvents 44

## Slide 45

What does the attacker need to control the decryption result? To craft a forged ciphertext, the attacker needs a reference point: → a known plaintext/ciphertext (Cref, Msgref) pair with the same shared key (k)

Cf. Encryption: X ← iv ⨁ Msg || pad, C ← Ek (X), send iv & C

Random bit-flipping forgery
iv’
C Dk X
X ⨁ iv ⨁ Flip
iv ⨁ “Hi” || pad  ⨁ iv ⨁ Flip

Msgdec = ?? (unknown)

Practical forgery using a known (Cref, Msgref) pair

ivref’
Dk
Cref Xref
Xref ⨁ ivref ⨁ Msgref || pad ⨁“Plz…BTC”
ivref ⨁ Msgref||pad ⨁ ivref⨁ Msgi || pad⨁“Plz…BTC”
Msgdec = “Plz give me BTC”

#BHUSA @BlackHatEvents 45

## Slide 46

Move from Bit Flipping Forgery to Controlled Practical Forgery

#### Random bit-flipping forgery

- No decryption knowledge

- Can’t control decrypted message

- Just makes noise

Practical forgery using a known (Cref, Msgref) pair

- Known plaintext/ciphertext block

- XOR trick enables precision

- Delivers chosen message to victim

#BHUSA @BlackHatEvents

46

## Slide 47

Move from Bit Flipping Forgery to Controlled Practical Forgery

#### Random bit-flipping forgery

- No decryption knowledge

- Can’t control decrypted message Problem:

- • Just makes noise How can we get it ?

Practical forgery using a known (Cref, Msgref) pair

- <u>Known plaintext/ciphertext block</u>

- XOR trick enables precision

- Delivers chosen message to victim

#BHUSA @BlackHatEvents

47

## Slide 48

Encrypted DM Forgery via Cross Protocol Attack Solution : Breaking the Barrier via “Cross Protocol” Attack **Observation:** Delegation (NIP-46) uses same keying & encryption algorithms as DMs (NIP-04) NIP-46 encrypts **<u>known metadata</u>** using the **_<u>same shared key</u>_** as DMs (NIP-04) NIP-04: NIP-46: Encrypted DM Delegation (multi-device) Allow to post Send Token via ECDH + AES-CBC ECDH + AES-CBC + Signing + Signing

#BHUSA @BlackHatEvents

48

## Slide 49

Encrypted DM Forgery via Cross Protocol Attack Solution : Breaking the Barrier via “Cross Protocol” Attack **Observation:** Delegation (NIP-46) uses same keying & encryption algorithms as DMs (NIP-04) NIP-46 encrypts **<u>known metadata</u>** using the **_<u>same shared key</u>_** as DMs (NIP-04) → makes known plaintext → makes known ciphertext

NIP-04: NIP-46: Encrypted DM Delegation (multi-device)

ECDH + AES-CBC + Signing

Allow to post

Send Token via ECDH + AES-CBC + Signing

#BHUSA @BlackHatEvents

49

## Slide 50

### Encrypted DM Forgery via Cross Protocol Attack

### Normal Delegation initial sequence

- ECDH with the public key obtained from the QR

- 𝑨𝒑𝒑

- • Sends encrypted known metadata to 𝑈𝑅𝐿!"#$% from the QR

PubKey App
𝑨𝒑𝒑
𝑈𝑅𝐿!"#$%

Trigger : Alice scans QR.
1. kapp ← ECDH( PubKey App , PrivKeyAlice)
2. Transmit encrypted known Metadata
Delegation QR
Alice C’ = AES-CBC(meta,  kapp )
for NIP-46

#BHUSA @BlackHatEvents

50

## Slide 51

### Encrypted DM Forgery via Cross Protocol Attack

**Strategy:** The attacker starts a NIP-46 session with the victim (as a fake delegation app) The attack puts PubKeyBob to the QR **Result:**

PubKeyBob
())$*+",
𝑈𝑅𝐿!"#$%

The victim sends back encrypted known metadata

0. Attacker obtains PubKeyBob from Relay
Trigger : Alice scans QR.
DMs 1. k ← ECDH( PubKeyBob, PrivKeyAlice)
Relay
2. Transmit encrypted known Metadata
Normal DMs session
Fake Delegation QR
Bob Alice C’ = AES-CBC(meta, k)
C = AES-CBC(Msg, k) for NIP-46

#BHUSA @BlackHatEvents 51

## Slide 52

### <u>Takeaway : Ciphertext Integrity</u>

- **Should use Authenticated Encryption (AE)**

   - E.g., AES-GCM, ChaCha20-Poly1305

   - Don’t use malleable encryption without MAC

- **Should separate key between sub-protocols**

   - Similar issues also occurred in Threema[PST23], Matrix[ACDJ23]

[PST23] Paterson, Scarlata and Truong, “Three Lessons From Threema: Analysis of a Secure Messenger”, USENIX Security’23 [ACDJ23] _Albrecht_ , _Celi, Dowling_ and _Jones_ , “Practically-exploitable Cryptographic Vulnerabilities in Matrix”, IEEE S&P’23 (Also, Black Hat Europe’22)

#BHUSA @BlackHatEvents

52

## Slide 53

Step by step attack tracing Breaking… Plaintext integrity (simple / cache poisoning) Ciphertext integrity Ciphertext confidentiality

### Remark: Encrypted Direct Messages specification (simplified)

NIP-04: Encrypted DM

ECDH + AES-CBC
+ Signing

#BHUSA @BlackHatEvents 53

## Slide 54

### Link Preview in Messaging

- Automatically retrieves and displays elements from the webpage E.g., The webpage’s title, part of its content, and images

- Someone must retrieve the page content (a sender, a receiver or a server) Client-side generation

https://example.net/

example.net

Server-side generation

https://example.net/
*Non E2EE msg

#BHUSA @BlackHatEvents

54

## Slide 55

### Link Preview generation in **Encrypted** Messaging

### Best practice

- Generate preview **ONLY** on the sender-side

- Bad practice

- Generate preview on the receiver-side

- Known privacy issues (IP leakage): https://mysk.blog/2020/10/25/link-previews/ Is there any chance we can use it?

Many Nostr Clients

- Generate preview on the both sender-side and <u>receiver-side</u>

#BHUSA @BlackHatEvents 55

## Slide 56

### Thinking about plaintext recovery in the real-world **Encrypted** Messaging

- Hard to break cryptographic primitive standard

- • But what if the recipient _helps_ the attacker reveal an encrypted msg? • How to win ? → Distinguishes & leaks decryption errors

   - Padding Oracle Attacks often appear in toy environments like CTFs

Q. Can we reproduce such an oracle in real-world systems?

#BHUSA @BlackHatEvents

56

## Slide 57

### Q. Can we reproduce such an oracle in real-world systems?

- Yes, we can! Receiver-side Link Preview generation helps us

- • We finally find 3 attacks to break encrypted message confidentiality

#BHUSA @BlackHatEvents

57

## Slide 58

### URL recovery attack

Attacker’s goal: disclose the authentication token in the URL E.g., shared URL of cloud storage, web conference tools

Attacker wants to know

𝑀 : 𝑀= 𝐸! https://{unknown domain}/{unknown part}

Authentication token

#BHUSA @BlackHatEvents

58

## Slide 59

### URL recovery attack Disclose domain part

- Attacker can obtain domain part of URL via DNS or TLS SNI field

- Just by opening the message, DNS queries and TLS ClientHello packets are sent due to the automatic execution of link previews.

The attacker learned that the domain part is “example.net”

#BHUSA @BlackHatEvents

59

## Slide 60

### URL recovery attack Disclose authentication token

- Force the authentication token to be sent to the attacker's server

- • Generate a modified ciphertext Ek(M′) where the domain is changed to a malicious one

- • When the victim receives Ek(M′), the token is sent to the malicious URL via Link Preview 𝑀 : 𝑀=

- 𝐸! https://example.net/{unknown part} Encrypted DM forgery

𝐸! 𝑀′ : 𝑀′ = https://mu.test/net/{unknown part} 1Block (16Byte)

#BHUSA @BlackHatEvents

60

## Slide 61

### URL recovery attack Disclose authentication token

#BHUSA @BlackHatEvents

61

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
BRIEFINGS
URL recovery attack
Disclose authentication token
1-2. Modify the domain name portion to mu.test without knowing k
1block (16 byte)
—_—"—_
Ex(M):M = net/{unknown part}
| cec forgery
E,(M'): M' = net/{unknown part}
KM) , _ . par) 3-1. Decrypt E,(M’) > M’
— =
i 1-1. Obtain E,(M) au
fees | 2-2. Receive E,(M')
q /) 2-1. Send E;,(M’) on
Active adversary Relay Server
Bob
4. Get access.log
au 3-2. Generate link preview
t t I
ras .
t?q
ee
meme \. access.log:
mu.test | 200630010900 - - [DD/MM/YYYY:mm:::] GET mu.test/net/secret?q=shared-url-token
61
```

## Slide 62

### Link Preview Oracle Attack

##### Attack overview

Attacker recover an encrypted message **before the encrypted URL.** It works like a padding oracle attack.

**Step1.** Modify the encrypted via a CBC malleability, producing a **partially attacker-controlled URL**

Scheme + known domain
Unknown (attacker can get them by DNS or TLS SNI packet)
𝑀 : 𝑀=
𝐸+ ? ? ? h t …
t p s : / / e x a m p l e . n e t
CBC Forgery
Truncated
𝐸+ 𝑀′ : 𝑀 - = ? ? ? t t p : / / m . t e s t /
Attackerʼs URL without ʻhʼ 1 Block = 16 Byte

#BHUSA @BlackHatEvents 62

## Slide 63

### Link Preview Oracle Attack

**Step2.** Seek an IV′ such that the 3rd byte of M′ becomes **“h”.** When “h” appears, the client fires a link preview, allowing the attacker to detect ‘h’ ← IV’[3](0xBE) ⨁𝐸./0 𝑀<sup>-</sup> 3

0xBE
𝐼𝑉′ =
𝐸+ 𝑀′ 𝐸!"# ⨁ m.test
𝑀 - = ? ? h t t p : / / m . t e s t /
M[3] =  0xBE ⨁ ‘h’ ⨁ iv[3](original)

#BHUSA @BlackHatEvents 63

## Slide 64

### Link Preview Oracle Attack

##### **Step3.** Repeat **Step 2** for the second and first bytes

0xA4
0xEF
0xBE
𝐼𝑉′ =
𝐸+ 𝑀′ 𝐸!"# ⨁ m.test
𝑀 - = h t t p : / / m . t e s t / a a
M[3] = 0xBE ⨁ ‘h’ ⨁ iv[3](original)
M[2] = 0xEF ⨁ ‘h’ ⨁ iv[2](original)
M[1] = 0xA4 ⨁ ‘h’ ⨁ iv[1](original)

*Index starts with 1

#BHUSA @BlackHatEvents 64

## Slide 65

### <u>Takeaway : Ciphertext Confidentiality</u>

- **Remark: SHOULD use Authenticated Encryption (AE)**

   - E.g., AES-GCM, ChaCha20-Poly1305

   - Don’t use malleable encryption without MAC

- **SHOULD generate preview ONLY on the sender-side**

#BHUSA @BlackHatEvents

65

## Slide 66

### <u>3 Takeaways : Whole of this presentation</u>

### 1. Decentralized Architecture’s Untapped Risks and Rewards

• Removing a central authentication server in Nostr brings new freedoms but also introduces subtle security pitfalls

- Multi-layered security are lost, and cryptographic weaknesses are immediately upgraded to practical attacks.

#BHUSA @BlackHatEvents

66

## Slide 67

### <u>3 Takeaways : Whole of this presentation</u>

### 2. Hands-On Attacks & Immediate Mitigation

We guided our footsteps, and you learn how to destroy integrity & confidentiality Identify the root cause and understand mitigation

   - Lack of key separation

- Signature verification • Receiver-side preview

- Bypass generation

- Verification Bypass

#BHUSA @BlackHatEvents

67

## Slide 68

### <u>3 Takeaways : Whole of this presentation</u>

### 3. Blueprint for Future-Ready Decentralized Systems

Nostr

Items Nostr Signing is mandatory. Signature But there is no concrete specs for verifying. No specs Link Preview (Mostly receiver-side generation) No specs Public Key Authenticity (NIP-05 Badge is available, but an authenticity is out of scope)

Blueprint

Signing & verifying are mandatory Sender-side generation • Out-of-band authentication • Key Transparency

#BHUSA @BlackHatEvents 68

## Slide 69

### <u>Summary</u>

- First cryptographic deep-dive into Nostr, a distributed SNS.

- • Find practical attacks caused by

cryptographic & implementation flaw.

- Client is the trust anchor.

- Mandatory signature checks, key-separation, and AEAD.

- • Responsible disclosure, and patches

#BHUSA @BlackHatEvents

69

## Slide 70

### <u>Our Paper</u>

https://crypto-sec-n.github.io/

#BHUSA @BlackHatEvents 70

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bi
Oo nat
BRIEFINGS
Our Paper
Hayato Kimura
NICT / The University of Osaka
Osaka, Japan
hytkimura@ protonmail.com
Shogo Shiraki
University of Hyogo
Hyogo, Japan
4w3tag185mpja@ gmail.com
Abstract—Distributed social networking services (SNSs) re-
cently received significant attention as an alternative to
traditional, centralized SNSs, which have inherent limitations
on user privacy and freedom. We provide the first in-depth
security analysis of Nostr, an open-source, distributed SNS
protocol developed in 2019 with more than 1.1 million
registered users. We investigate the specification of Nostr
and the client implementations and present a number of
practical attacks allowing forgeries on various objects, such
as encrypted direct messages (DMs), by a malicious user or a
malicious server. Even more, we show a confidentiality attack
against encrypted DMs by a malicious user exploiting a flaw
in the link preview mechanism and the CBC malleability.
Our attacks are due to cryptographic flaws in the protocol
specification and client implementation, some of which in
combination elevate the forgery attack to a violation of
confidentiality. We verify the practicality of our attacks
via Proof-of-Concept implementations and discuss how to
mitigate them.
Index Terms—Nostr, plaintext recovery attack, forgery attack,
key replace attack, Cache-based Forgery Attack, CBC-mode
2025 10th IEEE European Symposium on Security and Privacy (EuroS&P)
Not in The Prophecies: Practical Attacks on Nostr
Ryoma Ito
Tokyo, Japan
itorym@ nict.go.jp
Kazuhiko Minematsu
NEC
Kanagawa, Japan
k-minematsu@nec.com
NICT
Takanori Isobe
The University of Osaka
Osaka, Japan
takanori.isobe@ist.osaka-u.ac.jp
is considered to be a user of Nostr'. Since the protocol
is fully open-source, a number of client implementations
exist. On iOS, Damus ['] is currently the most major Nostr
client application. It was released in 2023 on the App Store
and garnered widespread attention. It is estimated to have
160,000 Damus users as of May 30, 2023 [5]. Additionally,
among Android users, a popular client application is
Amethyst [0], which has been downloaded by over 100,000
users. Other well-known popular client applications include
Iris ['], FreeFrom [+], and Plebstr ["] (See Appendix B for
details). Moreover, Nostr is applied to building not only
a distributed SNS environment but also an e-commerce
environment, and its further development is expected in
the future.
The designers of Nostr aimed to design their protocol
to be simple and censorship-resistant. The latter is achieved
by connecting the client nodes to the relay servers that do
not possess users’ secrets. The protocol is specified in a
series of documents called NIPs (Nostr Implementation
Possibilities), which are available on GitHub. Following
these NIPs, a number of implementations exist for both
clients and relay servers. Nostr introduced several security
features, such as message signing and encrypted direct
izes (DMs) between use
https://crypto-sec-n.github.io/
70
```
