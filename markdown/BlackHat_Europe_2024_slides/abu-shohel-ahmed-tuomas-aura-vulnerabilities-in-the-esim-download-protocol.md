---
title: "Vulnerabilities in the eSIM download protocol"
speakers: ["Abu Shohel Ahmed", "Tuomas Aura"]
conference: "Black Hat"
conference_full: "Black Hat Europe 2024"
edition: "Europe"
year: 2024
source_pdf: "BlackHat_Europe_2024_slides/Abu Shohel Ahmed & Tuomas Aura_Vulnerabilities in the eSIM download protocol.pdf"
pages: 35
sha256: "e5c2b7478bd38172a1f46a87b716e9d721f11a63e87f41906a9acb3358a65d64"
text_chars: 10381
ocr_pages: 1
has_ocr: true
redacted_secrets: 0
ocr_confidence: 80.5
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T04:53:45Z"
---
# Vulnerabilities in the eSIM download protocol

**Speakers:** Abu Shohel Ahmed, Tuomas Aura  
**Conference:** Black Hat Europe 2024  
**Source:** `BlackHat_Europe_2024_slides/Abu Shohel Ahmed & Tuomas Aura_Vulnerabilities in the eSIM download protocol.pdf` (35 pages)


## Slide 1

### Vulnerabilities in the eSIM download protocol

**Presenters Abu Shohel Ahmed** , Aalto University **Tuomas Aura** , Aalto University Joint work with **Aleksi Peltonen** , CISPA **Mohit Sethi** , Kone and Aalto University

## Slide 2

#### Who are we? our story

Shohel Ahmed, security researcher

Hey, I am working on implementing eSIM download protocol How do I know the protocol is secure ? We could apply formal verification to find out Let’s do it

Aleksi Peltonen

Mohit Sethi

Tuomas Aura, Professor

## Slide 3

#### Talk outline

##### 1. eSIM and the Consumer Remote SIM Provisioning (RSP) protocol

##### 2. Research methodology

##### 3. Discovered vulnerabilities

- ➢ What did we find

- ➢ Why does it matter

- ➢ What can we do about it

## Slide 4

#### From SIM to eSIM

- SIM contains credentials for authenticating a mobile network subscriber

- eSIM replaces removable SIM with downloadable SIM profiles

- Installed into an embedded secure chip (eUICC)

- Managed from phone settings or an app

## Slide 5

#### Consumer eSIM user experience

**Activation code approach Default server approach** • User inputs SM-DP+ server • eUICC or app has a default address  and activation code SM-DP+ server address • Manual entry or QR code • Operator need to know the SM-DP+ address device EID to order profile LPA:1$ sm-dp.example.com $ EID:890490320000010000000 95A9CB26933E7f1C 44883019442 Secret one-time code

## Slide 6

#### Consumer eSIM user experience

Activation code approach Default server approach
•  User inputs SM-DP+ server  •  eUICC or app has a default
address  and activation code SM-DP+ server address
•  Manual entry or QR code •  Operator need to know the
device EID to order profile
LPA:1$sm-dp.example.com$
EID:890490320000010000000
95A9CB26933E7f1C
44883019442
Identifies the device,
privacy sensitive data

## Slide 7

## How does it work under-the-hood?

Mobile
network 1a Web or
User
operator physical shop
visit
MNO
App
1b
2 Backend
UI
API
Phone
eSIM
App
Secure
3a 3b Internal
provisioning  SIM profile (built-in or
chip
server  download user- API
eUICC
authorized)
SM-DP+

## Slide 8

Secure channels
Web PKI
HTTPS or
shop visit
1a
Physical
control
Mutual  1b
2
TLS
3
SM-DP+ address TLS
Profile binding  OID Cryptographic  p roto col EID
GSMA-CI
Manufacturer
(root of trust)

## Slide 9

# Research methodology

How does the eSIM download protocol work? What are the security goals? Does the protocol meet the security goals? ...

## Slide 10

#### Research methodology

1. Protocol description as message sequence chart


> Recovered by OCR — confidence 81/100 on the text kept, 72/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Research methodology
1. Protocol description as
message sequence chart
SM-DP+ server (.
Seq, mnold, serverOID
HTTPS tunnel to S with Certs;
[ne]. [serverOID], U, mnold, S
User triggers download
Seq.G
1. GetChallenge |
2. Nu. SKIct
Nu =R
event U0
S = subject of Certs,
‘
event SO
4. Certsa,
Check that the same S returned,
[expected serverOID in Certsa]
5. Certsas Tac.
event S1
8. Sign(I+; SKsp), Certsp
Certsp « Certcr
serverOID from Certs
Zus = ds: Qu 12. E(P;k), MAC(E(P;k);k’),
Sign(Ir, Ns, Nu
7. Certy, Certeum,
]
. | U = subject of Certy
= serverOID from Certs»
k,k! = KDF(Zys, serverOID, U)
event S2
mnold, MAC( mnold; k’),
iccid, MAC(iccid; k’),
Sign(I;, Qs, Qu. serverOID; SKsp)
User checks mnold
User consent
13. E(P;k), MAC(E(P;k);k’),
mnold, MAC( mnold; k’)
iccid, MAC (iccid; k’),
Sign(I;, Qs, Qu. serverOID; SKsp)
14. Sign(I;, Seq, S, serverOID, icci
Zus == du- Qs
k,k’ == KDF(Zys, serverOID, U)
Verify MAC
Decrypt E(P;k), Seq := Seq+1
event U3
SK)
15. Sign(I,, Seq, S, serverOID, iccid; SKy ) Cache Seq
event S3
16. HTTP OK
17. Seq
Delete the notification
```

## Slide 11

#### Research methodology

##### 2. Formal model of the protocol

Participants of the protocols

- `(* ===== MAIN PROCESS ===== *) process`

\```
(** == CA == **)
let PK_CI = pk(SK_CI) in
out(c, PK_CI);
\```

   - `(** == Honest processes == **) !MNO(PK_CI)`

   - `| !SMDP(PK_CI)`

- `| !(new U:Id_t; out(c, U); new LPA2EUICC:channel; LPA(LPA2EUICC,PK_CI,U) |`

- `EUICC(LPA2EUICC,PK_CI,U) )`

   - `(** == Base attacker model == **) | A_ORDER(PK_CI)`

   - `| !A_TLS()`

   - `| (new U:Id_t; out(c, U); event OWNER(AttackerUserId,U); new LPA2EUICC:channel; out(c, LPA2EUICC); A_EUICC(LPA2EUICC,PK_CI,U)`

\```
)
\```

## Slide 12

#### Research methodology

3. Partial compromise scenarios

- Base-case: all participants are honest, network is the adversary

- Partial compromise scenarios

   - Compromised participants

   - Compromised outsiders

   - Compromised channels

## Slide 13

#### Research methodology

4. Test the security goals with model checker

## Slide 14

##### Result

###### Default-server approach

##### summary

- 600 verification targets

- No failures when all

###### design assumptions hold

###### Activation-code approach

41

## Slide 15

##### Result summary

###### Default-server approach

• 600 verification targets

###### Activation-code approach

###### • Found failures in partial compromise scenarios

|42|
|---|

## Slide 16

What did we find

## Slide 17

#### Observation 1: dependence on TLS

SM-DP+ address **TLS** Profile binding OID **Cryptographic** **~~p~~ roto** **~~col~~** EID

- TLS is great. What is the problem?

   - Defense in depth or privacy layer vs critical component

   - Front-end API server or TLS gateway is less secure than we expect from the provisioning server

   - Trust anchor should be GSMA-CI, but vendors prefer web PKI

- Ok, what if TLS fails?

## Slide 18

#### Vulnerability 1: server OID not known

Activation code: LPA:1$sm-dp.example.com$ 95A9CB26933E7f1C$ 1.3.6.1.4.1.31746 Default server EID: 89049032000001000000044883019442

Unique SM-DP+ server identifier

## Slide 19

#### Vulnerability 1: server OID not known

1.3.6.1.4.1.31746

App and eUICC may lack knowledge of the SM-DP+ server OID

- Communicating the OID out-of-band with activation-code is optional

- Input not supported by app user interfaces

- Not specified for the default-server approach

## Slide 20

#### Vulnerability 1: server OID not known

TLS
SM-DP+ address
OID Cryptographic  p roto col EID
SM-DP+ address 1
Any adversary-controlled
OID1
SM-DP+ server

## Slide 21

#### Vulnerability 1: server OID not known

TLS
SM-DP+ address
OID Cryptogr a phic  protocol  EID
SM-DP+ address 1
OID1

Becomes a problem if TLS to the SM-DP+ server is compromised ➔ Adversary who controls any SM-DP+ server in the world can issue fake SIM profiles to any subscriber of any MNO

## Slide 22

#### Vulnerability 2 : EID not known

Activation code: LPA:1$sm-dp.example.com$ 95A9CB26933E7f1C

EID:89049032000001000000044883019442

Profile bound to one-time secret

In the activation code approach, SM-DP+ server usually lacks a-priori knowledge of the EID

## Slide 23

#### Theft of activation codes

Ways activation code can leak:

- 1 TLS from mobile to SM-DP+ path

- 2 User to App path (e.g., sloppy user, insecure app)

- • 3 User to MNO path

- 4 MNO processes

3
4
Activation  code
2
1

## Slide 24

#### Vulnerability 2 : EID not known

Activation code: LPA:1$sm-dp.example.com$ 95A9CB26933E7f1C$1.3.6.1.4.1.31746

- Activation code leaks ➔ adversary can steal the SIM profile

- If adversary has the private key of any eUICC in the world, adversary can also get the profile and the secret key in it

## Slide 25

#### Lessons for protocol design

- Authentication without a-priory knowledge of the identifier

   - Certificate proves the entity class (SM-DP+ or eUICC) but not the individual identity ➔ Attacker can substitute a different one

- Dependence on the TLS tunnel leads to vulnerabilities when combined with other weaknesses

   - Dependency is easy to remove in the default server approach

   - Major redesign required in the activation code approach.

## Slide 26

#### Observation 2: difficulty in verifying user intent

- User goes to the operator (web) shop, receives a QR code, and scans it with the eSIM app

- What is (or should be)communicated between the user and MNO?

- What if the secrecy or integrity is compromised?

User intent

## Slide 27

#### Vulnerability 3: verifying user identity

Often, no reliable method for verifying user identity when subscribing

➔ Identity fraud in ordering      Adversary can steal the victim’s SIM profile

Consequences **similar to SIM swapping**

- May breaks 2FA, enables further fraud

## Slide 28

#### Vulnerability 4: verifying eUICC ownership

• How does MNO verify the eUICC ownership/possession in the Default server approach?

EID:89049032000001000000044883019442
Attacker
MNO

## Slide 29

#### Vulnerability 4: verifying eUICC ownership

User
2. Initiate
download
App

## Slide 30

#### Vulnerability 4: verifying eUICC ownership

3. Download
attacker
selected SIM
Phone
SM-DP+ App eUICC

➔ Victim tricked into using the adversary’s mobile subscription

## Slide 31

#### Potential consequences

Adversary’s SIM profile is in the victim’s phone. So what?

- Leakage of mobile metadata

   - Call and message logs, billing information, roaming history, location services

- Text and call capture with multi-SIM

   - Adversary has a multi-SIM subscription and gets one of the SIM profiles into the victim’s phone ➔ Receives copies of text messages and can answer calls

- Data capture with home routing

   - Spies can use this to divert all mobile data from the device to their country

## Slide 32

Lessons: what the operator should check

1. User identity check: make the order for the correct subscriber

2. Ownership verification: make the order for the correct eUICC (EID)

- Not easy to implement in practice

## Slide 33

#### Notifying GSMA

• We notified GSMA’s eSIM working group • GSMA acknowledges our finding that the RSP protocol is secure between honest entities against network adversary

- For attacks performed with compromised endpoints, (e.g., SM-DP+ server and eUICC), GSMA places importance on eSIM certification process as mitigation control

- For attacks performed by compromising user intent,

- GSMA points these are out of specification scope

## Slide 34

#### Key Takeaways: why should you care

- Protocol designer: Formal verification is an effective way to identify security weakness

- Red teams: Don’t just target products or websites – also target specifications as they affect all products based on them

- Specification body: Telco is not a closed world! Don’t assume everyone in the world is a good guy.

## Slide 35

#### Questions ?

- AS Ahmed, A Peltonen, M Sethi, T Aura. Security Analysis of the Consumer Remote SIM Provisioning Protocol. ACM Transactions on Privacy and Security 27 (3), <u>https://dl.acm.org/doi/pdf/10.1145/3663761</u>

- Model in GitHub: https://github.com/peltona/rsp_model

- Contact

   - <u>abu.ahmed@aalto.fi https://www.linkedin.com/in/shohel</u>

   - <u>tuomas.aura@aalto.fi https://www.linkedin.com/in/tuomas-aura-94749aa4/</u>
