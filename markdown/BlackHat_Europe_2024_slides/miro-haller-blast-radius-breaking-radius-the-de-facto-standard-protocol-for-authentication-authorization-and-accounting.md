---
title: "Blast-RADIUS Breaking RADIUS, the de facto standard protocol for authentication, authorization, and accounting for networked devices"
speakers: ["Miro Haller"]
conference: "Black Hat"
conference_full: "Black Hat Europe 2024"
edition: "Europe"
year: 2024
source_pdf: "BlackHat_Europe_2024_slides/Miro Haller_Blast-RADIUS Breaking RADIUS, the de facto standard protocol for authentication, authorization, and accounting for networked devices.pdf"
pages: 38
sha256: "0ec8765e76dc15cc97b1f2c7eae7f1c767b1ae9b25a69398b814386128ba6b79"
text_chars: 16739
ocr_pages: 0
has_ocr: false
redacted_secrets: 0
ocr_confidence: null
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 1
companion_files: []
extractor: "pymupdf4llm 1.28.2"
converted_at: "2026-08-12T04:58:24Z"
---
# Blast-RADIUS Breaking RADIUS, the de facto standard protocol for authentication, authorization, and accounting for networked devices

**Speakers:** Miro Haller  
**Conference:** Black Hat Europe 2024  
**Source:** `BlackHat_Europe_2024_slides/Miro Haller_Blast-RADIUS Breaking RADIUS, the de facto standard protocol for authentication, authorization, and accounting for networked devices.pdf` (38 pages)


## Slide 1

# Blast-RADIUS

Breaking Enterprise Network Authentication

Sharon Goldberg<sup>1</sup> , **Miro Haller**<sup>2</sup> , Nadia Heninger<sup>2</sup> , Mike Milano<sup>3</sup> , Dan Shumow<sup>4</sup> , Marc Stevens<sup>5</sup> , Adam Suhl<sup>2</sup>

1Cloudflare, 2UC San Diego, 3BastionZero, 4Microsoft Research, 5Centrum Wiskunde & Informatica

Black Hat Europe 2024; December 12, 2024

## Slide 2

## What is RADIUS? Where is it used?

- _RADIUS:_ standard protocol for enterprise network authentication.

- RADIUS is _everywhere_ :

   - _RADIUS is [...] supported by essentially every switch, router, access point, and VPN concentrator product sold in the past twenty-five years._

_(Alan DeKok [4])_

- Used for backbone routers, non-cable ISP, IoT devices, identity providers (Okta, Duo), 802.1X, enterprise WiFi, eduroam...

XKCD from [8]

1/22

Miro Haller

BHEU 2024

## Slide 3

## Blast-RADIUS on a Single Slide

How does RADIUS work?

login Access-Request
user/pw user/pw
access granted! Access-Accept or
user RADIUS client RADIUS server
(router) Access-Reject (auth DB)

- Most RADIUS traffic is sent over UDP.

- _Our protocol vulnerability:_ MITM can change Access-Reject to Access-Accept.

- _Impact:_ authenticate as any user; accelerate RADIUS/UDP deprecation.

- _Mitigation:_ responsible disclosure with over 90 vendors (incl. Cisco, Microsoft, ...).

icons from [6]

2/22

Miro Haller

BHEU 2024

## Slide 4

THE RADIUS PROTOCOL

## Slide 5

## RADIUS Packet Formats

Access-Request = Request Header Request Nonce Attributes
4 bytes 16 random bytes User-Name test
Password Mjg2NzU1z
Access-Accept = Accept Header Response Authenticator Attributes
4 bytes 16 byte “MAC” Reply-Message Welcome test!
Exec-Privilege 4
Access-Reject = Reject Header Response Authenticator Attributes
4 bytes 16 byte “MAC” Reply-Message Access denied

3/22

Miro Haller

BHEU 2024

## Slide 6

## Response Authenticator

Goal : Prevent forgery of packets (e.g., by MITM attacker).
The Response Authenticator from packet
Response Header Response Authenticator Attributes
is computed as
copied from request fixed, pre-configured
Response Header Request Nonce Attributes
MD5 ( Shared Secret ).
copied from response

4/22

Miro Haller

BHEU 2024

## Slide 7

## 90s Cryptography In RADIUS

RADIUS must be broken.

Let’s do it!

Sharon Goldberg

Nadia Heninger

_As of the writing of this specification, RADIUS/UDP is still widely used, even though it depends on MD5 and "ad hoc" constructions for security. While MD5 has been broken, it is a testament to the design of RADIUS that there have been (as yet) no attacks on RADIUS Authenticator signatures which are stronger than brute-force._

_(“Deprecating Insecure Practices in RADIUS” IETF draft, 2023)_

5/22

Miro Haller

BHEU 2024

## Slide 8

THE BLAST-RADIUS ATTACK

## Slide 9

## Blast-RADIUS: Attack Overview

Goal: Forge Access-Accept without knowing shared secret.
Blast-RADIUS attack: Create MD5 collision s.t. Access-Accept and Access-Reject
produce same Response Authenticator: MD5(Access-Accept) = MD5(Access-Reject).
Accept Reject
login Request compute collision! Request ′
password bogus
Access Granted!
Accept Reject
attacker RADIUS client MITM RADIUS server
(router) (auth DB)
copy Response Authenticator

icons from [6]

6/22

Miro Haller

BHEU 2024

## Slide 10

## MD5 Collision Attack History

1990 1995 2000 2005 2010 2015 2020
MD5weakness[5] FullMD5collisionChosen-prefix[14]RogueTLScollisionCA[11]cert[12] MD5considereddead Blast-RADIUS

- MD5 collision: unstructured strings _G_ 1, _G_ 2 with MD5( _G_ 1) = MD5( _G_ 2).

- Chosen-prefix collision: given prefixes _P_ 1, _P_ 2, produces _G_ 1, _G_ 2 s.t.

MD5( _P_ 1 _||G_ 1) = MD5( _P_ 2 _||G_ 2) _._

7/22

Miro Haller

BHEU 2024

## Slide 11

## MD5 Collision Attack History

1990 1995 2000 2005 2010 2015 2020
MD5weakness[5] FullMD5collisionChosen-prefix[14]RogueTLScollisionCA[11]cert[12] MD5considereddead Blast-RADIUS

- MD5 collision: unstructured strings _G_ 1, _G_ 2 with MD5( _G_ 1) = MD5( _G_ 2).

- Chosen-prefix collision with suffix _S_ : given prefixes _P_ 1, _P_ 2, produces _G_ 1, _G_ 2 s.t.

   - MD5( _P_ 1 _||G_ 1 _||S_ ) = MD5( _P_ 2 _||G_ 2 _||S_ ) _._

8/22

Miro Haller

BHEU 2024

## Slide 12

## Blast-RADIUS: Turning Access-Reject into Access-Accept

Attack: MD5 collision to forge Access-Accept with same Response Authenticator as
Access-Reject (without knowledge of the shared secret).
MD5 chosen-prefix collision MD5( P 1 ||G 1 ||S ) = MD5( P 2 ||G 2 ||S ) applied to RADIUS:
Response Authenticator
Accept Header Request Nonce Accept Attributes Accept Gibberish
= MD5( Secret )
Reject Header Request Nonce Reject Attributes Reject Gibberish
= MD5( Secret )
predicted accept/reject prefixes P 1, P 2 gibberish G 1, G 2 suffix S
(unknown)

9/22

Miro Haller

BHEU 2024

## Slide 13

Challenge 1: Inject Reject Gibberish **Problem:** Server must include Reject Gibberish in Response Authenticator computation for Access-Reject.

Reject Header Request Nonce Reject Gibberish
MD5( Shared Secret )

### **Solution:** The Proxy-State attribute.

_This Attribute is available to be sent by a proxy server to another server when forwarding an Access-Request and_ **_MUST be returned unmodified_** _in the Access-Accept, Access-Reject or Access-Challenge._

_(RFC 2058, emphasis added)_

Access-Request = Request Header Request Nonce Proxy-State
Access-Reject = Reject Header Response Authenticator Proxy-State

10/22

Miro Haller

BHEU 2024

## Slide 14

## Challenge 2: Gibberish Length

**Problem:** Hiding Reject Gibberish in single Proxy-State attribute is too slow. **Solution:** Spread longer gibberish across multiple Proxy-State attributes by modifying collision algorithm to embed Proxy-State header.

Proxy State 1 Proxy State 2
PS1 Header Reject Gibberish = PS1 Header Gibberish PS2 Header Gibberish

( PS1 Header is part of the MD5 prefix not the gibberish.)

11/22

Miro Haller

BHEU 2024

## Slide 15

## Challenge 3: Online Collision Computation

Access-Request = Request Header Request Nonce Attributes
Reject Header Request Nonce Reject Gibberish
MD5( Shared Secret )

**Problem:** Computing MD5 prefixes requires Request Nonce . = _⇒_ Must compute collision before RADIUS client times out, _but_ chosen-prefix collisions are slow (e.g., 28h on 215 PS3 [12]).

**Solution:** Reduce collision time from days to _≤_ 5m (on 47 servers) with algorithmic improvements and parallelization.

12/22

Miro Haller

BHEU 2024

## Slide 16

## Challenge 3: Our Optimizations

• Increase
precomputation.
• New GPU
generator mode
for birthday
search.
• Parallelize
forward phase
across machines.

- Tune parameters to trade runtime for success rate.

Execution monitoring during collision optimization.

13/22

Miro Haller

BHEU 2024

## Slide 17

## Blast-RADIUS: Example

As concrete example, putting everything together, we get the following collision.

PoC example packets
Response Authenticator
blastradius.fail/example.py
6034d0ff16e4...30
Header Request Nonce Proxy State 1 Proxy State 2
02 1d 01c0 726164617574...72 21 ec 3d...86 21 c0 f5...9e
= MD5( Shared Secret )
Accept Prefix Accept Gibberish (unknown)
03 1d 01c0 726164617574...72 21 ec 96...86 21 c0 f5...9e
= MD5( Shared Secret )
Reject Prefix Reject Gibberish (unknown)

14/22

Miro Haller

BHEU 2024

## Slide 18

# IMPACT

of the Blast-RADIUS attack

## Slide 19

## Impact Summary

### **Affected modes:**

- PAP, CHAP, MS-CHAP are vulnerable.

- EAP modes likely not vulnerable (see below).

**Affected deployments:** Requires MITM network access

- RADIUS/UDP traffic over open Internet = _⇒_ vulnerable.

   - incl. cloud providers and telecommunication networks.

- RADIUS/UDP traffic over VLAN/IPSEC = _⇒_ lateral movement.

### **Timing:**

- RADIUS client timeouts _≤_ 1m, our PoCs take _≈_ 5m.

- Optimizations feasible: parallelizes well, hardware implementation.

15/22

Miro Haller

BHEU 2024

## Slide 20

## Successful PoCs<sup>*</sup>

Blast-RADIUS allows attacker to authenticate:

- **FreeRADIUS 3.2.3** : “most widely used RADIUS server in the world” [9]

- **Okta** : RADIUS in PAP mode for MFA.

- **Cisco ASA 5505 firewall** using RADIUS to authenticate users for access to serial console, VPN, Telnet, FTP, or HTTPS.

- **PAM** : RADIUS authentication for SSH, sudo.

- = _⇒_ Confirms no Message-Authenticator used, Proxy-State accepted in Access-Accept.

PoC with Cisco ASA 5505 firewall tunneling UDP via TCP to our cluster.

- *With longer timeouts than used in practice.

16/22

Miro Haller

BHEU 2024

## Slide 21

EAP: It’s Complicated.
• TLS in EAP-TLS does not protect RADIUS
packets.
Not to be confused with RADIUS/TLS, which
properly nests RADIUS inside TLS.
RFC 3579 requires that EAP-Message has
Message-Authenticator attribute [1].
Unclear client behavior for Access-Accept
without EAP-Message.
In eduroam and 802.1X, key is negotiated
inside EAP session =⇒would require further
attacks.
Miro Haller
BHEU 2024
17/22

## Slide 22

## EAP: It’s Complicated.

- TLS in EAP-TLS does not protect RADIUS packets.

- Not to be confused with RADIUS/TLS, which properly nests RADIUS inside TLS.

- RFC 3579 requires that EAP-Message has Message-Authenticator attribute [1].

- Unclear client behavior for Access-Accept without EAP-Message.

- In eduroam and 802.1X, key is negotiated inside EAP session = _⇒_ would require further attacks.

18/22

Miro Haller

BHEU 2024

## Slide 23

# MITIGATING

the Blast-RADIUS attack

## Slide 24

## Mitigations

- Massive disclosure with 90+ vendors.

- Challenges: widely used, need backwards compatibility.

### **Short-term:**

- Message-Authenticator attribute uses HMAC-MD5 not vulnerable to MD5 collisions.

- All requests and responses should include and verify Message-Authenticator.

### **Long-term:**

- Encapsulate all RADIUS traffic in (D)TLS tunnel.

Some power plants use RADIUS [13].

- Current IETF draft is being standardized [10].

19/22

Miro Haller

BHEU 2024

## Slide 25

## Mitigations: Status Update (December 12)

- Alan DeKok: many equipment vendors have upgraded [2].

- Some misunderstandings about Message-Authenticator placement.

   - Juniper devices fail if Message-Authenticator is not the first attribute [3].

   - Cisco ISE Auth Server puts Message-Authenticator at arbitrary location [7].

Source of confusion is the **Message-Authenticator hiding attack** :

Reject Gibberish
Reject Header Response Authenticator PS 1 PS 2 Message-Authenticator
Accept Gibberish
Accept Header Response Authenticator PS 1 PS 2 PS Header Message-Authenticator
parsed as Proxy State

20/22

Miro Haller

BHEU 2024

## Slide 26

Mitigations: Status Update (December 12)

- Alan DeKok: many equipment vendors have upgraded [2].

- Some misunderstandings about Message-Authenticator placement.

   - Juniper devices fail if Message-Authenticator is not the first attribute [3].

   - Cisco ISE Auth Server puts Message-Authenticator at arbitrary location [7].

- Where should the Message-Authenticator go?

   - For _sending:_ put it as the first attribute to avoid previous hiding attack.

   - For _receiving:_ do not mandate order, for backwards compatibility.

      - = _⇒_ Deployments that always require Message-Authenticator are _not vulnerable_ .

      - = _⇒_ Other deployments _may remain vulnerable_ , depending on attribute placement.

21/22

Miro Haller

BHEU 2024

## Slide 27

## Blast-RADIUS Attack

**Attack summary:** MD5 collision attack on RADIUS authentication by MITM adversary.

\```
https://blastradius.fail
\```

**RADIUS/UDP Considered Harmful** Sharon Goldberg, Miro Haller, Nadia Heninger, Mike Milano, Dan Shumow, Marc Stevens, and Adam Suhl. USENIX Security, August 2024.

XKCD from [8]

22/22

Miro Haller

BHEU 2024

## Slide 28

BONUS MATERIAL

## Slide 29

## End-to-End Example Attack (1/4)

### Access-Request

Access-Request = 01 1d 0047 726164617574...72 010674...3a `code ID length Request Nonce` attributes Access-Accept = 02 1d 0027 a268dc70e8a2...1d 120f57...04 `code ID length Response Authenticator` attributes Access-Reject = 03 1d 0024 357bf27e8c0a...e5 121041...2e `code ID length Response Authenticator` attributes

1/9

Miro Haller

BHEU 2024

## Slide 30

## End-to-End Example Attack (2/4)

1. Attacker triggers Access-Request.

2. MITM attacker observes Access-Request. 01 1d 0047 726164617574...72 010674...3a `Request Nonce`

PoC example packets `blastradius.fail/example.py`

3. MITM attacker predicts the following prefixes

Accept Prefix = 02 1d 01c0 726164617574...72 21 ec
Reject Prefix = 03 1d 01c0 726164617574...72 21 ec
PS (1/2)

to compute the MD5 chosen-prefix collision gibberish.

Accept Gibberish = 3d...86 21 c0 f5...9e (428 bytes)
Reject Gibberish = 96...86 21 c0 f5...9e (428 bytes)

PS (2/2) Proxy State (PS) BHEU 2024

2/9

Miro Haller

## Slide 31

## End-to-End Example Attack (3/4)

4. MITM sends Access-Request with appended `Reject Gibberish` to server.

01 1d 0047 726164617574...72 010674...3a 21 ec 96...86 21 c0 f5...9e
Reject Gibberish

5. MITM intercepts Access-Reject, learning the Response Authenticator.

03 1d 01c0 6034d0ff16e4...30 21 ec 96...86 21 c0 f5...9e

\```
ResponseAuthenticator
\```

6. MITM puts Response Authenticator in Access-Accept packet with appended `Accept Gibberish` .

02 1d 01c0 6034d0ff16e4...30 21 ec 3d...86 21 c0 f5...9e `Accept Gibberish`

3/9

Miro Haller

BHEU 2024

## Slide 32

## End-to-End Example Attack (4/4)

7. Access-Accept and Access-Reject produce the same Response Authenticator, and hence pass the RADIUS client authentication check.

Response Authenticator
6034d0ff16e4...30
02 1d 01c0 726164617574...72 21 ec 3d...86 21 c0 f5...9e
= MD5( Shared Secret )
Accept Prefix Accept Gibberish (unknown)
03 1d 01c0 726164617574...72 21 ec 96...86 21 c0 f5...9e
= MD5( Shared Secret )
Reject Prefix Reject Gibberish (unknown)

4/9

Miro Haller

BHEU 2024

## Slide 33

## Attack Extensions

- Adversary can add arbitrary attributes in prefix for Access-Accept.

AcceptPrefix = 02 1d 01c0 726164617574...72 1a0b000007db1d04 21 ec Attribute: `Exec-Privilege 04`

- Proxy-State attributes are _not_ the only way to inject the `RejectGibberish` .

   - Any reflected user input could work, e.g. the User-Name or Vendor-Specific attributes.

      - In Access-Request: `User-Name: 0PZjN-_ayr83S-nc6q...Mt85`

      - In Access-Reject: `Reply-Message: Login for 0PZjN-_ayr83S-nc6q...Mt85 failed!`

   - The client does not need to support or parse these attributes.

5/9

Miro Haller

BHEU 2024

## Slide 34

REFERENCES

## Slide 35

## References I

[1] Pat R. Calhoun and Dr. Bernard D. Aboba. _RADIUS (Remote Authentication Dial In User Service) Support For Extensible Authentication Protocol (EAP)_ . RFC 3579. Sept. 2003. DOI: `10.17487/RFC3579` . URL: `https://www.rfc-editor.org/info/rfc3579` .

- [2] Alan DeKok. _Personal Communication_ .

- [3] Alan DeKok. _[radext] BlastRADIUS problems_ . `https://mailarchive.ietf.org/arch/msg/radext/7c9-35Xh6IoCTJ4_xydvpczGPU/` . 2024.

- [4] Alan DeKok. _RADIUS and MD5 Collision Attacks_ . `https: //networkradius.com/assets/pdf/radius_and_md5_collisions.pdf` . 2024.

6/9

Miro Haller

BHEU 2024

## Slide 36

## References II

[5] Bert den Boer and Antoon Bosselaers. “Collisions for the Compression Function of MD5”. In: _EUROCRYPT’93_ . Ed. by Tor Helleseth. Vol. 765. LNCS. Springer, Heidelberg, Germany, May 1994, pp. 293–304. DOI: `10.1007/3-540-48285-7_26` .

- [6] _Icons from_ _`https: // www. flaticon. com`_ . visited on Dec 4, 2024.

[7] _[ISE Message-Authenticator Attribute order_ . `https://community.cisco.com/t5/network-access-control/isemessage-authenticator-attribute-order/td-p/5205188` . 2024.

- [8] Randall Munroe. _Dependency (Comic #2347)_ . `https://www.xkcd.com/2347/` . 2020.

[9] The FreeRADIUS Server Project and Contributors. _FreeRADIUS_ . `https://freeradius.org/` .

7/9

Miro Haller

BHEU 2024

## Slide 37

## References III

[10] Jan-Frederik Rieckers and Stefan Winter. _(Datagram) Transport Layer Security ((D)TLS Encryption for RADIUS_ . Internet-Draft draft-ietf-radext-radiusdtls-bis-02. Work in Progress. Internet Engineering Task Force, July 2024. 38 pp. URL: `https://datatracker.ietf.org/doc/draftietf-radext-radiusdtls-bis/02/` .

[11] Marc Stevens, Arjen K. Lenstra, and Benne de Weger. “Chosen-Prefix Collisions for MD5 and Colliding X.509 Certificates for Different Identities”. In: _EUROCRYPT_ . Vol. 4515. Lecture Notes in Computer Science. Springer, 2007, pp. 1–22.

[12] Marc Stevens et al. “Short Chosen-Prefix Collisions for MD5 and the Creation of a Rogue CA Certificate”. In: _CRYPTO_ . Vol. 5677. Lecture Notes in Computer Science. Springer, 2009, pp. 55–69.

8/9

Miro Haller

BHEU 2024

## Slide 38

## References IV

[13] Henrik Thejl, Nagaraja K S, and Karl-Georg Aspacher. “A method for user management and a power plant control system thereof for a power plant system”. Pat. 2765466. Siemens Gamesa Renewable Energy A/S. Jan. 24, 2014. URL: `https://data.epo.org/publication-server/rest/v1.0/publicationdates/20190904/patents/EP2765466NWB1/document.pdf` .

[14] Xiaoyun Wang and Hongbo Yu. “How to Break MD5 and Other Hash Functions”. In: _EUROCRYPT_ . Vol. 3494. Lecture Notes in Computer Science. Springer, 2005, pp. 19–35.

9/9

Miro Haller

BHEU 2024
