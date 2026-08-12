---
title: "Bad Randomness Protecting Against Cryptography's Perfect Crime"
speakers: ["Tal Be'ery"]
conference: "Black Hat"
conference_full: "Black Hat ASIA 2024"
edition: "ASIA"
year: 2024
source_pdf: "BlackHat ASIA 2024-Slides/Tal Be'ery-Bad Randomness Protecting Against Cryptography's Perfect Crime.pdf"
pages: 53
sha256: "43f33b713e7331dbc5c4cce1ffc9fdaf73f8baaa56c59018202d68da08420374"
text_chars: 17016
ocr_pages: 16
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T00:52:26Z"
---
# Bad Randomness Protecting Against Cryptography's Perfect Crime

**Speakers:** Tal Be'ery  
**Conference:** Black Hat ASIA 2024  
**Source:** `BlackHat ASIA 2024-Slides/Tal Be'ery-Bad Randomness Protecting Against Cryptography's Perfect Crime.pdf` (53 pages)


## Slide 1

**Bad Randomness: Protecting Against Cryptography's Perfect Crime**

Tal Be’ery, CTO & Co-Founder Zengo

#BHASIA @BlackHatEvents

## Slide 2

#### 👋 **Hi, I’m Tal Be’ery**

- Co-Founder, CTO @ ZenGo

- ● 20+ years cyber security

- 9th time BH Speaker

- 1st time BHASIA speaker!

- <u>@talbeerysec</u>

## Slide 3

### **Agenda**

**●The Perfect Crime: Why bad randomness is crypto’s perfect crime?**

**●True Crime(s)**

- **→ Bad private key: Bitcoin, gone in milliseconds**

- **→ Bad Nonce:  Ethereum, gone in milliseconds**

- **→ Bad DH parameters: TLS malware, even more powerful than previously known**

**●Solutions**

**→ Avoiding single point of failure with MPC**

## Slide 4

# **The perfect crime**

Randomness in cryptography

## Slide 5

### **The perfect crime**

- **Lethal**

- **Undetectable**

## Slide 6

######

Randomness in cryptography is like the air we breathe. You can’t do anything without it,

- Prof. Yevgeniy Dodis <u>https://cs.nyu.edu/~dodis/courant-article.pdf</u>

## Slide 7

### **Randomness is vital**

**●Kerckhoffs' principle: the security of a cryptographic system should be based on the secrecy of the cryptographic key ●Keys values should be unguessable → created in random**

**●But also other crypto items, e.g. Nonces, IVs**

**●Randomness is vital → Lack thereof is lethal!**

## Slide 8

### **Bad randomness is undetectable**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Bad randomness is undetectable
TOUR OF ACCOUNTING |: age
r “Te NINE NINE #1 You THAT'S THE
OVER HERE Fe NINE NINE al cime PROBLEM
WE HAVE OUR 3 NINE NINE 1 THAT'S WITH RAN-
RANDOM NUMBER [8 3} RANDOM? = DOMNESS :
GENERATOR. é YOU CAN
E 3 ( NEVER BE
be 5
3 $
```

## Slide 9

### **Bad randomness is undetectable**

**●There are no random numbers, only numbers created by a random process**

**●In most cases, you cannot inspect a number and decide if it is random or not**

**●In most cases, the values of these random numbers are not stored as they are too secret → not available for a statistical forensic analysis**

## Slide 10

### **Crypto’s perfect crime**

**Bad randomness is crypto’s perfect crime**

**●Lethal**

**●Undetectable**

## Slide 11

**True crime, true detective**

Bad Randomness in the wild

## Slide 12

### **True detective**

Season 1: Bitcoin’s dark forest

## Slide 13

### **From random to Bitcoin address: step 1**

**●Generate a random 128 bit number**

**●Add 1 bit of checksum for each 32 bit (33 is divisible by 11)**

## Slide 14

**From random to Bitcoin address: step 2**

**●Assign for each 11 bit group a word from BIP-39 to get the seed phrase**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
From random to Bitcoin address: step 2
@ Assign for each 11 bit group a word from BIP-39 to get the seed
phrase
101011011101100011001001001011100100101100100101011000101110000100
| | | |
1390 1586 604 1202 689 900
punch shock entire north file identify
Mnemonic Sentence J
```

## Slide 15

### **From random to Bitcoin address: step 3**

● **Key Derivation Function: PBKDF2: 2048 HMAC-SHA512** ● **Adding performance “penalty” to make bruteforce harder**

## Slide 16

### **From random to Bitcoin address: step 4**

##### ● **Derive addresses**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
From random to Bitcoin address: step 4
@ Derive addresses
BIP 32 - Hierarchical Deterministic Wallets
Master Master Wallets / wallet Addresses
Seed Node Accounts Chains
ta Te) eee (£8
a @8) ~ ~m/0/0/0 | m/0/0/1 = m/0/0/k
gt y m/0/0
a Internal te t te) ..-
m/0 crore.) -m/0/1/0_, m/0/A/1 - m/0/Lk
CKD{en, 0)
Entropy cxomio (08
128 bits crom._- (8 m/1/0
HMAC-SHASI2 (@ 7 t bd
“(28 m/1 env}, 2) 7
Re 8) v cli sie .
s m CKDIm, i) 7 e
.
.
External
cxotov. 0) te
ee m/i/0
vi intemal te te tT) ... &
mi CKO -mii/l0_, mii = mii/lk
Depth = 0 Depth = 1 Depth = 2 Depth = 3
Child Key Derivation Function ~ CKD(x,n) = HMAC-SHA512(x< chain » X purxey [| 9)
```

## Slide 17

### **Randomness in crypto addresses**

**●Getting an address might be a complex process ●But it all starts with a random number**

**●If this number is guessable, all funds are gone!**

## Slide 18

### **Bad randomness can cost Billions**

<u>https://www.washingtonpost.com/technology/2023/11/14/bitcoin-wallet-passcode-flaw/</u>

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Bad randomness can cost Billions
If you created a bitcoin wallet before 2016,
your money may be at risk
A company that helps recover cryptocurrency discovered a software flaw putting as much as $1 billion at risk from
hackers. Now it’s going public in hopes people will move their money before they get robbed.
>)
ey By Joseph Menn
Updated November 14, 2023 at 1:30 p.m. EST — Published November 14, 2023 at 6:00 a.m. EST
httos://www.washingtonpost.com/technology/2023/11/14/bitcoin-wallet-passcode-flaw/
```

## Slide 19

**POC!**

## Slide 20

**Step 1: bad randomness Bitcoin Key**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
tep 1: bad randomness Bitcoin Key
&@ iancoleman.io/bip39/#entropy-notes
Warning _ Entropy is an advanced feature. Your mnemonic may be insecure if this feature is used incorrectly. Read more
Entropy —_ 0000000000000000000000000000000000000000000000000000000000000001 Valid entropy values inckice
Binary [0-1]
Time To Crack —_less than a second - Event Count 64 © tarot
Repeats like "aaa" are > Base 6 [0-5]
easy to guess + 129434014
Entropy Type hexadecimal Avg Bits PerEvent 4.00 © Dice [1-6]
+ 62535634
Raw Entropy Words 24 Total Bits 256
Base 10 [0-9]
Filtered Entropy 00000000000000000000000000000000000000000000000000000000000 + 90834528
00001
@ Hex [0-9A-F]
Raw Binary 00000000000 00000000000 00000000000 00000000000 00000000000 * 4187a8bfd9
(00000000000 00000000000 00000000000 00000000000 00000000000
0000000000 00000000000 00000000000 00000000000 00000000000 Card [A2-9TJQK][CDHS]
00000000000 00000000000 00000000000 00000000000 00000000000 * ahqs9dte
(00000000000 00000000000 00000000000 001
ary Checksum 11101100
Word indexes 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 492
Mnemonic Length Use Raw Entropy (3 words per 32 bits) y
PBKDF2 rounds 2048 (compatibility) ¥
Show entropy details
Hide all private info
Auto compute
"PX(HME) Frangais Italiano tR0 Cestina Portugués
B Espahol PX
Mnemonic Language English
BIP39 Mnemonic abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon
abandon abandon abandon abandon abandon abandon abandon abandon diesel
```

## Slide 21

**Step 2: Address is pristine**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Step 2: Address is pristine
€ C (« mempool.space/address/bc1q4jgysxym8yvp6khka878njuh8dem4!7mneyefz
@® *7 4#+ &@ &@ @
AddFe tercsjaysymayvpskteas7e
Total received 0.00000000
Total sent 0.00000000
Balance 0.00000000
```

## Slide 22

**Step 3: Send money.. It’s gone!**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Step 3: Send money.. It’s gone!
Address be1q4jgysxym8yvp6khka878njuh8dem4I7mneyefz &
Total received 0.00026468
Total sent 0.00026468
Balance 0.00000000 $0.00
2 of 2 transactions
d6a41b5c34b9e75f50c18a9750d6eb1724e471da4c9c86019d9057802ce88809
bc1q4j gysxym8yvp6khka878n... 7mneyefz 0.00026468
- 13,234 $5.00
844276d225a1fd1c7ad9987aa4957edd6998f2864e75dflaf8fadf1f8862ab94
38t4esnJ2muzTZg1wRPnS6qfTxrJ9uTGRn 0.00092039
- 4,284 sat $1.62
2023-11-30 21:51
belqf Lnp7@wn@t3rt546vkz0c... 9kxyw63z 0.0001323487¢ ©
413 confirmations — -0.00026468 8 1c
2023-11-30 21:51
bc1q4j gysxym8yvp6khka878n... 7mneyefz 0.00026468
38t4esnJ2muzTZg1wRPnS6qfTxrJ9UTGRA 0.00061287 ©
413 confirmations — +0.00026468 BTC
```

## Slide 23

### **Conclusions**

**●Bad randomness attackers are real**

**●Bots are lurking for transactions to bad randomness addresses and taking them away in real time**

- **●Further reading**

   - **→** **<u>https://zengo.com/how-keys-are-made/</u>**

   - **→** **<u>https://zengo.com/bitcoin-is-a-dark-forest-too/</u>**

## Slide 24

### **True detective**

Season 2: Ethereum’s dark forest

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
True detective
Season 2: Ethereum’s dark forest
COLIN VINCE! CHEL TAYLOR
FARRELL VAUGHN ‘\- McADAMS KITSCH
TRUE DETEGTIVE 5
&
6/219PMHB® |
```

## Slide 25

### **ECDSA nonce**

**●ECDSA signatures are used in many security related protocols**

**→ Authentication**

**→ Cryptocurrency**

**●require a nonce that should be secret → let’s make it random**

**●However if nonce is somewhat predictable..**

**●** **<u>LadderLeak: Breaking ECDSA with Less than One Bit of Nonce Leakage</u> (BH EU 2020)**

## Slide 26

### **Nonce reuse dark forest in the wild**

**<u>https://twitter.com/bertcmiller/status/1475844939816833032</u>**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Nonce reuse dark forest in the wild
fag @bertcmiller + & @
@bertcmiller
Last week a monster in Ethereum's dark forest revealed themselves to
me.
This blog post tells the story of that encounter:
bertcmiller.com/2021/12/28/gli...
5:03 PM : Dec 28, 2021
https://twitter.com/bertcmiller/status/1475844939816833032
```

## Slide 27

### **True detective**

Season 3: The TLS malware

## Slide 28

### **The Reductor Malware**

**●Identified by Kaspersky in 2019**

**→** **<u>https://securelist.com/compfun-successor-reductor/93633/</u>**

- **→ Attributed to Turla APT group**

**●Malware:**

- **→ patches the PRNG**

- **→ injects CA TLS Certs**

## Slide 29

### **The TLS Handshake**

<u>https://blog.cloudflare.com/keyless-ssl-the-nitty-gritty-technical-details</u>

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
The TLS Handshake
SSL Handshake (RSA) Without Keyless SSL
Handshake
Visitor CloudFlare
Visitor sends hello, client random, and cipher suites supported
Server sends server random and public key certificate
(also sent is a session ID for session resumption)
Visitor encrypts premaster secret with public key
CloudFlare decrypts the premaster
secret with the private key
Now the visitor can request content from CloudFiare,
Bt (also sent is a session ticket for session resumption)
i }
H H Both the visitor and CloudFare create session keys from
t Or session key H the clent random, server random, and premaster secret.
t H
t '
ht
echnical-details
```

## Slide 30

**Patching the PRNG: The Code POV**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Patching the PRNG: The Code POV
PRNG functions
“nss3.dll” PK11_GenerateRandom() Call original PRNG function and generate initial XOR key from its
result. Change PRNG result: set seventh byte to 1, then save
0x45F2837D, hwid and cert hashes. Encrypt the result and return
it instead of the original PRN. It will affect calls to
ssl3_SendClientHello() -> ssl3_GetNewRandom(ss-
>ssl3.hs.client_random);
“advapi32.dll” CryptGenRandom() Spoof these system PRNG function results in similar way with
some minor changes;
“perypt.dll” BCryptGenRandom()
“chrome.adll” PRNG function Find PRNG function by its binary code template and patch it like
all the aforementioned.
```

## Slide 31

**Patching the PRNG: The network POV**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Patching the PRNG: The network POV
Serge aoe
Handshake Protocol: Client Hello
Handshake Type: Client Hello (1)
Length: 126
Version: TLS 1.2 (0x0303)
Random: 64d34a0100000000000000000000000000000000000000000000000000000000
GMT Unix Time: Aug 9, 2023 11:10:41.000000000 IDT
Random Bytes: 00000000000000000000000000000000000000000000000000000000
```

## Slide 32

### **Cyber paleontology**

- **●Reductor malware:**

   - **→ patches the PRNG**

   - **→ injects CA TLS Certs**

- **●Reductor malware must be working with a server MITM**

<u>https://www.kaspersky.com/blog/cyberpaleontology-managed-protection/24118/</u>

## Slide 33

### **The Reductor MITM: Active MITM**

www.cnn.com

https://www.cnn.com Client random: random

ISP

https://www.cnn.com Client random: **marked**

## Slide 34

### **Some observations**

- **●Monsters (Bad randomness attackers) are real!**

**●Although attackers can use their malware, they prefer to fiddle with network traffic**

- **●Why?**

   - **→ Does not really matter**

   - **→ More stealthy**

## Slide 35

### **The TLS Handshake with EDH**

<u>https://blog.cloudflare.com/keyless-ssl-the-nitty-gritty-technical-details</u>

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
The TLS Handshake with EDH
SSL Handshake (Diffie-Hellman) Without Keyless SSL
Handshake
E>
Visitor CloudFlare
[BR server random
Server sends server random and public key certificate
(also sent isa session ID for session resumption)
Public key certificate The key signs for client
random, server random,
and public key certificate
i
Server sends the server DH parameter anda signature t
Hi
t
Visitor sends the client DH parameter
i
Both the visitor and CloudFiare derive identical t
remaster secrets from the server OH parameter ' Premaster secret
‘and client DH parameter. t
t
Both the visitor and CloudFiare derive identical ‘ 4
session keys ors the caer rancom server random
apd premier secret. The shor ca request content 1 Orrm session key '
ae Bagphr nh ne ' |
Gaotenisaseisontcetorsesonrenmpien) «= sw eee eeeeeeeeeeee!
ty-gritt
https://blog.cloudflare.com/keyless-ssl-th echnical-details
```

## Slide 36

### **Ephemeral Diffie Hellman (EDH)**

- **●EDH provides Perfect Forward Secrecy to TLS ●Provided the DH private parameter (“secret color”) remains secret…**

- **●But DH parameter is also created with the, now patched, PRNG!**

**●** 😱 **Reductor attackers could probably passively** 😱 **eavesdrop!**

## Slide 37

### **The Reductor MITM: passive eavesdropper!**

https://www.cnn.com Client random: random

ISP

www.cnn.com I can see!

https://www.cnn.com Client random: **marked**

## Slide 38

**DEMO!**

## Slide 39

### **Demo recipe**

**1. Use our modified TLS client** **<u>github.com/ZenGo-X/tls_client_handshake_pure_python to patch</u> a. Client Random**

   - **b. DH parameter**

**2. Connect with our modified client via TLS to a well known website**

**3. Record the encrypted traffic of this connection using Wireshark PCAP**

**4. Use our tool** **<u>https://github.com/ZenGo-X/TLS-masterkey-recovery</u> key to compute the masterkey using**

   - **a. inputs**

      - **i. Server parameters in plaintext, as obtained from PCAP**

         **1. Server random**

         **2. Server DH public key**

      - **ii. The predetermined Client parameters**

         **1. Client Random (as obtained from PCAP)**

         **2. Client DH private key**

   - **b. Save the masterkey output in the** **<u>standard</u> SSLKEYLOGFILE format**

**5. Feed this masterkey file to Wireshark to successfully decrypt the traffic 6. WIN!**

## Slide 40

**Demo!**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
emo!
«
Q
QuickTime Payer File Edit View Window Help
°
zoom Bw © ES em
‘Thu 28 Mar 9:43,
```

## Slide 41

### **Some (additional) observations**

**●Bad randomness is so undetectable that we are not even sure what the attackers have done**

**●Attackers are even more stealthy now**

**→ Passiveness is the ultimate stealth mode**

**●PFS is not always better than no PFS**

## Slide 42

**Solving bad randomness**

## Slide 43

**Bad solution: Human generated randomness**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Bad solution: Human generated randomness
UNCOMMON
~28 BITS OF ENTROPY
(Non-GisBeRGH) — , ORDER THE Os WAS A ZERO?
BASE WORD UNKNOWN, 5 ; .
“8 oa fs AND THERE WAS
= 3 DANS AT SOME SYMBOL...
Tr@ub4dor &4 1000 GUEssES/sec
TA SEAS cecum Aten
CAPS? —COMMON NUMERAL Heh 1s FASTER, BUT NO a sna
SUBSTITUTIONS ae eee
DIFFICULTY To GUESS: | | DIFFICULTY TO REMEMBER:
(YOU CAN AOD A FEW MORE BTS To PUNCTUATION
peer oat ee EASY HARD
WAS IT TROMBONE? NO,
TROUGADOR. AND ONE OF
correct horse battery staple
FOUR RANDOM
COMMON woRDS
~4U4 BITS OF ENTROPY
2 = 550 YEARS AT
1000 GUESSES/sEC
DIFFICULTY To GUESS:
HARD
DIFFICULTY TO REMEMBER:
YOU'VE ALREADY
MEMORIZEO IT
THROUGH 20 YEARS OF EFFORT, WE'VE SUCCESSFULLY TRAINED
EVERYONE TO USE PASSWORDS THAT ARE HARD FOR HUMANS
To REMEMBER, BUT EASY FoR COMPUTERS To GUESS.
```

## Slide 44

### **Human generated randomness in the wild**

**●AKA “brain” wallets**

**●Entropy is generated from a passphrase ●DEF CON 23 (2012) - Ryan Castellucci - Cracking CryptoCurrency Brainwallets**

**→** **<u>https://www.youtube.com/watch?v=foil0hzl4Pg</u>**

- **Found 733 BTC in 2012 → ~$50M in 2024**

**● “Down the Rabbit-Hole”: held about 85 BTC in July 2012**

## Slide 45

######

Humans are not a good source of entropy

Bitcoin Wiki https://en.bitcoin.it/wiki/Brainwallet

## Slide 46

### **Removing the need of randomness**

**●Reusing existing good randomness → Deterministic Nonce (RFC6979) ■HMAC-SHA256(private_key, message)**

**→ NAXOS trick (draft-irtf-cfrg-randomness-improvements-** **<u>10.html)</u>**

**■Mix server long term key with entropy**

**●See also James P. Hughes, Whitfield Diffie: “The Challenges of IoT, TLS, and Random Number Generators in the Real World” →** **<u>https://queue.acm.org/detail.cfm?id=3546933</u>**

## Slide 47

### **Protecting the PRNG itself**

**● Treat PRNG as the most critical part of the system → E.g. PRNG protection in hardware ●Helpful, yet limited → The PRNG is still single point of failure ●What if we could have it distributed? → We can do it with Multi-Party Computation ■** **<u>https://drand.love/</u>**

## Slide 48

### **Multi-Party computation (MPC) for ECDSA**

**●Key generation is distributed**

**→ Bad randomness of a single party still create a random key**

**●Signing is distributed**

**→ Bad randomness of a single party still create a random nonce**

**●Our implementation**

- **→** **<u>https://github.com/ZenGo-X/gotham-city</u>**

- **→** **<u>Blogs</u>**

## Slide 49

## **MPC wallets**

- **No Single Point of Failure!**

- **Key generation is distributed → Resilient against malware key theft**

- **→ Resilient against bad randomness**

- **Signing is distributed → Resilient against malware key theft**

- **→ Resilient against bad randomness**

- **Blockchain is unaware → Signature looks the same**

## Slide 50

## **Seed Phrase vs. MPC**

Seed Phrase

## Slide 51

**Outro**

## Slide 52

### **Takeaways**

- **Bad randomness is indeed crypto’s perfect crime**

- **●Exploited in the wild**

   - **→ APT for TLS**

   - **→ Bitcoin dark forest attackers → Ethereum dark forest attackers**

- **●Solutions:**

   - **→ Protect PRNG**

   - **→ Remove unnecessary randomness requirements**

   - **→ Use MPC to avoid Single Point of Failure**

## Slide 53

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
724
zengo
@ Bitcoin
: a
1.3983 BTC
$23,092.21
Q Ethereum
10.8673 ETH
12,991.08
```
