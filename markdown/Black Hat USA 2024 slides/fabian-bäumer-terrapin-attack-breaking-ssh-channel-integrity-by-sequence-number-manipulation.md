---
title: "Terrapin Attack Breaking SSH Channel Integrity by Sequence Number Manipulation"
speakers: ["Fabian Bäumer"]
conference: "Black Hat"
conference_full: "Black Hat USA 2024"
edition: "USA"
year: 2024
source_pdf: "Black Hat USA 2024 slides/Fabian Bäumer_Terrapin Attack Breaking SSH Channel Integrity by Sequence Number Manipulation.pdf"
pages: 31
sha256: "ce0ca22031c21a85435f5076d0962f3f7e43b35b393ba061b20bee0426196380"
text_chars: 9726
ocr_pages: 2
has_ocr: true
companion_files: ["Fabian Bäumer_Terrapin Attack Breaking SSH Channel Integrity by Sequence Number Manipulation_tools.txt"]
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:30:34Z"
---
# Terrapin Attack Breaking SSH Channel Integrity by Sequence Number Manipulation

**Speakers:** Fabian Bäumer  
**Conference:** Black Hat USA 2024  
**Source:** `Black Hat USA 2024 slides/Fabian Bäumer_Terrapin Attack Breaking SSH Channel Integrity by Sequence Number Manipulation.pdf` (31 pages)

## Slide 1

Terrapin Attack: Breaking SSH Channel Integrity by Sequence Number Manipulation

**Fabian Bäumer**

**Ruhr University Bochum**

Marcus Brinkmann Ruhr University Bochum

Jörg Schwenk Ruhr University Bochum

#BHUSA @BlackHatEvents

## Slide 2

##### A Tale Of System Administration

Sysadmin Bob

bob@srv-prod-01
srv-prod-01
SSH
Production
srv-test-01
SSH
Test
mallory@srv-test-01
Network TAP

Trainee Mallory

#BHUSA @BlackHatEvents

## Slide 3

##### Demo

##### - A ‘Normal’ Workday For Bob

#BHUSA @BlackHatEvents

## Slide 4

## In The Next 30 Minutes You Will Learn…

- … how Mallory was able to mess with Bob’s user authentication

- … which other attack variants Mallory can perform

- … the specific requirements for Mallory’s attack to work

- … how Bob can protect himself against Mallory’s attack

###### Beyond that,

- … how adding modern cryptography to older protocols can go wrong

- … how we handled a protocol-level responsible disclosure

#BHUSA @BlackHatEvents

## Slide 5

## Understanding SSH Is Key to Understanding Mallory’s Attack SSH Connection Protocol (RFC 4254)

SSH Authentication Protocol (RFC 4252)

=> Binary Packet Protocol => SSH Key Exchange

SSH Transport Layer Protocol (TLP) (RFC 4253) TCP / IP

#BHUSA @BlackHatEvents

## Slide 6

## Step 1: Exchange of Protocol Version

Bob

Server

```
SSH-2.0-PuTTY-Release-0.80
```

```
SSH-2.0-OpenSSH_9.6p1
```

#BHUSA @BlackHatEvents

## Slide 7

Step 2: Exchange of Supported Algorithms Server Bob `SSH-2.0-PuTTY-Release-0.80 SSH-2.0-OpenSSH_9.6p1`

`KEXINIT:` 𝑛𝑆, 𝑎𝑙𝑔𝑜𝑟𝑖𝑡ℎ𝑚_𝑙𝑖𝑠𝑡𝑠 `KEXINIT:` 𝑛𝐶, 𝑎𝑙𝑔𝑜𝑟𝑖𝑡ℎ𝑚_𝑙𝑖𝑠𝑡𝑠

#BHUSA @BlackHatEvents

## Slide 8

## Step 3: Performing Key Exchange

Server
Bob
Protocol Version Exchange
KEXINIT:  𝑛𝑠, 𝑎𝑙𝑔𝑜𝑟𝑖𝑡ℎ𝑚_𝑙𝑖𝑠𝑡𝑠
KEXINIT:  𝑛𝑐, 𝑎𝑙𝑔𝑜𝑟𝑖𝑡ℎ𝑚_𝑙𝑖𝑠𝑡𝑠
Important:  Computed
over a fixed subset of
message fields
KEXDHINIT:  𝑔 𝑥
KEXDHREPLY:  𝑔 𝑦 , 𝑝𝑘𝑆, 𝑠𝑖𝑔

Bob

#BHUSA @BlackHatEvents

## Slide 9

# Step 4: Activating the Secure Channel

Server Bob Protocol Version Exchange `KEXINIT:` 𝑛𝑠, 𝑎𝑙𝑔𝑜𝑟𝑖𝑡ℎ𝑚_𝑙𝑖𝑠𝑡𝑠 `KEXINIT:` 𝑛𝑐, 𝑎𝑙𝑔𝑜𝑟𝑖𝑡ℎ𝑚_𝑙𝑖𝑠𝑡𝑠 `KEXDHINIT:` <u>𝑔</u><sup>𝑥</sup> `KEXDHREPLY:` <u>𝑔</u><sup>𝑦</sup> <u>, 𝑝𝑘𝑆, 𝑠𝑖𝑔</u> `NEWKEYS NEWKEYS`

#BHUSA @BlackHatEvents

## Slide 10

## Step 5: Request User Authentication Service

Server
Bob
Protocol Version Exchange
KEXINIT:  𝑛𝑠, 𝑎𝑙𝑔𝑜𝑟𝑖𝑡ℎ𝑚_𝑙𝑖𝑠𝑡𝑠
KEXINIT:  𝑛𝑐, 𝑎𝑙𝑔𝑜𝑟𝑖𝑡ℎ𝑚_𝑙𝑖𝑠𝑡𝑠
KEXDHINIT:  𝑔 𝑥
Replay
KEXDHREPLY:  𝑔 𝑦 , 𝑝𝑘𝑆, 𝑠𝑖𝑔 Attacks?
NEWKEYS
NEWKEYS
EXTINFO
SERVICEREQUEST: ssh-userauth
SERVICEACCEPT: ssh-userauth

#BHUSA @BlackHatEvents

## Slide 11

# SSH Uses Implicit Sequence Numbers

Bob

Server

Snd Rcv 0 0

Snd Rcv 0 0

Sequence numbers are not transmitted

#BHUSA @BlackHatEvents

## Slide 12

# SSH Uses Implicit Sequence Numbers

Bob

Server

Snd Rcv

Snd Rcv

0 1

1 0

#BHUSA @BlackHatEvents

## Slide 13

# SSH Uses Implicit Sequence Numbers

Bob

Server

Snd Rcv

Snd Rcv

1 1

1 1

#BHUSA @BlackHatEvents

## Slide 14

# SSH Uses Implicit Sequence Numbers

Bob

Snd Rcv

1 1

Server Snd Rcv `NEWKEYS NEWKEYS` 1 1

#BHUSA @BlackHatEvents

## Slide 15

# SSH Uses Implicit Sequence Numbers

Server
Bob
Snd Rcv
Snd Rcv
NEWKEYS
NEWKEYS
1 1 1 1
Verified
through a
message
authentication
code (MAC)

Snd Rcv

#BHUSA @BlackHatEvents

## Slide 16

# SSH Uses Implicit Sequence Numbers

Bob Snd Rcv

Server Snd Rcv `NEWKEYS NEWKEYS`

2 1

1 2

#BHUSA @BlackHatEvents

## Slide 17

## Introducing Sequence Numbers to the Flow

|Snd|Rcv
Bob|Protocol Version Exchange|Server
Snd|Rcv|
|---|---|---|---|---|
|0|0|`KEXINIT: `𝑛𝑠,𝑎𝑙𝑔𝑜𝑟𝑖𝑡ℎ𝑚_𝑙𝑖𝑠𝑡𝑠|0|0|
|0|1|`KEXINIT: `𝑛𝑐,𝑎𝑙𝑔𝑜𝑟𝑖𝑡ℎ𝑚_𝑙𝑖𝑠𝑡𝑠|1|0|
|1|1|`KEXDHINIT: `𝑔<sup>𝑥</sup>|1|1|
|2|1|`KEXDHREPLY: `𝑔<sup>𝑦</sup>, 𝑝𝑘𝑆,𝑠𝑖𝑔|1|2|
|2|2|`NEWKEYS`|2|2|
|2|3|`NEWKEYS`|3|2|
|**3**|3|`EXTINFO`|3|**3**|
|**4**|3|`SERVICEREQUEST: ssh-userauth`|3|**4**|
|5|**3**|`SERVICEACCEPT: ssh-userauth`|**3**|5|
|5|4||4|5|

#BHUSA @BlackHatEvents

## Slide 18

## Step 6: Authenticating the User

|Snd|Rcv
Bob|Protocol Version Exchange|Server
Snd|Rcv|
|---|---|---|---|---|
|0|0
How can|Algorithm Negotiation|0|0|
|1|1
Mallory mess
|KeyExchange|1|1|
|2|2
wit~~h this~~
proto~~col flow?~~|`NEWKEYS`|2|2|
|**3**|3|`EXTINFO`|3|**3**|
|**4**|3|`SERVICEREQUEST: ssh-userauth`|3|**4**|
|5|**3**|`SERVICEACCEPT: ssh-userauth`|**3**|5|
|**5**|4|`USERAUTHREQUEST: bob:secret`|4|**5**|
|6|**4**|`USERAUTHSUCCESS`|**4**|6|
|6|5||5|6|

#BHUSA @BlackHatEvents

## Slide 19

Mallory‘s Ultimate Goal: Inject Forged
Authentication Request
Server
Bob Mallory
Protocol Version Exchange
Snd Rcv
Snd Rcv
0 0 Algorithm Negotiation 0 0
1 1 Key Exchange 1 1
2 2 Injection not  NEWKEYS 2 2
possible
3 3 because EXTINFO 3 3
connection is
4 3 SERVICEREQUEST: ssh-userauth 3 4
encrypted and
5 3 SERVICEACCEPT: ssh-userauth 3 5
authenticated
USERAUTHREQUEST: mallory:password 4 5
USERAUTHSUCCESS 4 6
5 4 USERAUTHREQUEST: bob:secret 5 6

#BHUSA @BlackHatEvents

## Slide 20

#### Mallory Tries To Move The Authentication Request Into Unauthenticated Context…

||B|ob|Server
Mallory||
|---|---|---|---|---|
|Snd|Rcv||Snd
Protocol Version Exchange|Rcv|
|0|0||Algorithm Negotiation
0|0|
||||1
`USERAUTHREQUEST: mallory:password`|1|
|1|1||KeyExchange
1
|2
|
|2|2||`NEWKEYS`
2
~~Rc~~v veri
fai|3
fication
ls|
|**3**|3||`EXTINFO`
3|**4**|
|**4**|3||`SERVICEREQUEST: ssh-userauth`
3|**5**|
|5|**3**||`SERVICEACCEPT: ssh-userauth`
**4**|6|
|**5**|4||`USERAUTHREQUEST: bob:secret`
4|**6**|
|6|**4**||`USERAUTHSUCCESS`
**4**|7|

#BHUSA @BlackHatEvents

## Slide 21

#### … And Drops the First Authenticated Message to Realign Sequence Numbers

Server
Bob Mallory
Protocol Version Exchange
Snd Rcv
Snd Rcv
0 0 Algorithm Negotiation 0 0
USERAUTHREQUEST: mallory:password 1 1
1 1 Key Exchange
2 2 NEWKEYS 2 3
Rc v verification
succee ds again
3 3 EXTINFO
4 3 SERVICEREQUEST: ssh-userauth 3 4
5 3 SERVICEACCEPT: ssh-userauth 4 5
5 4 USERAUTHREQUEST: bob:secret 4 5
6 4 USERAUTHSUCCESS 4 6

#BHUSA @BlackHatEvents

## Slide 22

#### Authentication Succeeds Earlier Than Expected

Server
Bob Mallory
Protocol Version Exchange
Snd Rcv
Snd Rcv
0 0 Algorithm Negotiation 0 0
USERAUTHREQUEST: mallory:password 1 1
1 1 Key Exchange
2 2 NEWKEYS 2 3
3 3 EXTINFO
4 3 SERVICEREQUEST: ssh-userauth 3 4
5 3 SERVICEACCEPT: ssh-userauth 4 5
USERAUTHSUCCESS 4 5
5 5 USERAUTHREQUEST: bob:secret 5 5

#BHUSA @BlackHatEvents

## Slide 23

Mallory’s Attack Can Succeed by Delaying
Authentication Success
Server
Bob Mallory
Protocol Version Exchange
Snd Rcv
Snd Rcv
0 0 Algorithm Negotiation 0 0
USERAUTHREQUEST: mallory:password 1 1
1 1 Key Exchange
2 2 NEWKEYS 2 3
3 3 EXTINFO
4 3 SERVICEREQUEST: ssh-userauth 3 4
5 3 SERVICEACCEPT: ssh-userauth 4 5
USERAUTHSUCCESS 4 5
5 5 USERAUTHREQUEST: bob:secret 5 5

#BHUSA @BlackHatEvents

## Slide 24

# What Went Wrong Here?

Server accepted Signature fails to Sqn numbers are user authentication detect message maintained across in unauthenticated injection during different encryption context. handshake. contexts. _Implementation Flaw Specification Flaw Specification Flaw_

#BHUSA @BlackHatEvents

## Slide 25

# Let’s Talk About Attack Variants

Server accepted user authentication in unauthenticated context. _Implementation Flaw_

What if the server
accepts other
messages as well?

Signature fails to Sqn numbers are detect message maintained across injection during different encryption handshake. contexts. _Specification Flaw Specification Flaw_

Message truncation inside the secure channel is a (cryptographically) successful attack in itself. Removing `EXTINFO` can negatively impact user authentication!

#BHUSA @BlackHatEvents

## Slide 26

Caveat: Truncating Encrypted Messages May Hinder Subsequent Message’s Decryption

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2024
Caveat: Truncating Encrypted Messages
May Hinder Subsequent Message’s
Decryption
Authenticated Encryption Mode Enc. State Dec. State Affected Exploitable
CBC (dV,Snd) (UV, Rev)
CTR (ctr, Snd) (ctr, Rev)
CBC UV, Snd) UV, Rev)
CTR (ctr, Snd) (ctr, Rev)
Encrypt-and-MAC
Encrypt-then-MAC
GCM ct l' Invocation ct VInvocation
ChaCha20-Poly 1305 Snd Rcv
\N =*® \N &*&
```

## Slide 27

### But: ChaCha20-Poly1305 And EtM Are Popular

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2024
But: ChaCha20-Poly1305 And EtM Are Popular
AE Mode Preferred Supported
ChaCha20-Poly 1305 8,739k 57.64% 10,247k 67.58%
CTR-EaM 3,964k 26.14%  4,200k 27.70%
GCM 1,219k 8.04% 10,450k 68.92%
CTR-EtM 828k 5.46% 10,685k 70.46%
CBC-EaM 359k =. 2.37% = 1,585k_ =10.46%
CBC-EtM 14k =©0.09% = 2,614k 17.24%
Other 2k =60.01% -
Unknown / No KEXINIT 36k = 0.24% -
Total 15,164k 100%
```

## Slide 28

# How Can Bob Protect Himself?

“Strict KEX”
Countermeasure Our Suggestion
(OpenSSH)
Reset sequence numbers at key installation
Authenticate the entire handshake transcript (hash)
Harden handshake to disallow unexpected messages

“Strict KEX”
Countermeasure Our Suggestion
(OpenSSH)
Reset sequence numbers at key installation
Authenticate the entire handshake transcript (hash)
Harden handshake to disallow unexpected messages

> **30 vendors support “strict kex”**

**~ 11 million servers offer “strict kex”**

#BHUSA @BlackHatEvents

## Slide 29

## We Contacted 31 Vendors During Disclosure

Oct 2023

Initial contact with OpenSSH and AsyncSSH

AsyncSSH published patch to fix implementation bugs Nov Initial contact with 29 additional vendors of SSH implementations 2023

Public Disclosure Dec 2023

Thanks to all involved parties for the smooth responsible disclosure process!

#BHUSA @BlackHatEvents

## Slide 30

# Lessons Learned

**1. Terrapin is a novel cryptographic attack targeting SSH channel integrity**

- Exploitable in practice to downgrade connection‘s security (w/o implementation flaws)

- Enables exploitation of certain implementation flaws as a MitM

**2. Widespread encryption modes are affected**

- ChaCha20-Poly1305

- CTR / CBC ciphers alongside Encrypt-then-MAC

**3. “Strict Kex” as a protocol-level countermeasure**

- Requires support from client and server to take effect

#BHUSA @BlackHatEvents

## Slide 31

# Thanks! Questions?

<u>https://terrapin-attack.com/</u>

```
E-Mail:      fabian.baeumer@rub.de
X (formerlyTwitter):              @TrueSkrillor
Mastodon: @Skrillor@infosec.exchange
```

#BHUSA @BlackHatEvents

## Companion resources

### `Fabian Bäumer_Terrapin Attack Breaking SSH Channel Integrity by Sequence Number Manipulation_tools.txt`

```text
https://github.com/RUB-NDS/Terrapin-Artifacts
```
