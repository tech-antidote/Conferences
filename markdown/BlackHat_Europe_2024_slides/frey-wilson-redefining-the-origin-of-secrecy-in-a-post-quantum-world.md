---
title: "Redefining the Origin of Secrecy in a Post-Quantum World"
speakers: ["Frey Wilson"]
conference: "Black Hat"
conference_full: "Black Hat Europe 2024"
edition: "Europe"
year: 2024
source_pdf: "BlackHat_Europe_2024_slides/Frey Wilson_Redefining the Origin of Secrecy in a Post-Quantum World.pdf"
pages: 34
sha256: "54350bcf16857b8c114d18b8a20423cdb05e5c984dfb0609bd1bb76d1381174f"
text_chars: 9392
ocr_pages: 5
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:49:28Z"
---
# Redefining the Origin of Secrecy in a Post-Quantum World

**Speakers:** Frey Wilson  
**Conference:** Black Hat Europe 2024  
**Source:** `BlackHat_Europe_2024_slides/Frey Wilson_Redefining the Origin of Secrecy in a Post-Quantum World.pdf` (34 pages)


## Slide 1

# Redefining the Origin of Secrecy in a Post-Quantum World

Speaker: Dr Frey Wilson, CTO @ Cavero Quantum

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
EWROPE 20 “
eh | Jae mm
‘Redefi ining the Origin of Secrecy
in a Post-Quantum World
Speaker: Dr Frey Wilson, CTO @ Cavero Quantum
Fora Vx =t aay:
```

## Slide 2

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pisckchat
EUROPE 2024
SECURITY "5
CYBERSECURITY NEWS, INSIGRTS & ANALYSIS
Malware & Threats ~ Security Operations ~ Security Architecture ~ Risk Management CISO Strategy » ICS/OT ~ Funding/M&A ~
NETWORK SECURITY
Russian Telco Hijacked Internet Traffic of Major
Networks — Accident or Malicious Action?
A huge BGP hijack by Russian state telecommunications provider Rostelecom diverted the traffic from more than 200 ni
Google, Amazon, Facebook and Cloudflare — to Russian servers on April 1. It may have been accidental, it may not.
The Register’
Apple network traffic takes mysterious detour
through Russia
Land of Putin capable of attacking routes in cyberspace as well as real world
@ Thomas Claburn Wed 27 Jul 2022 18:56 UTC
Apple's internet traffic took an unwelcome detour through Russian networking equipment
for about twelve hours between July 26 and July 27.
In a write-up for MANRS (Mutually Agreed Norms for Routing Security), a public interest
group that looks after internet routing, Internet Society senior internet technology
manager Aftab Siddiqui said that Russia's Rostelecom started announcing routes for part
of Apple's network on Tuesday, a practice referred to as BGP (Border Gateway Protocol)
hijacking.
is Reuters
innovation business security buying gui
Funil sar ncaa
For two hours, a large chunk of European
mobile traffic was rerouted through China
It was China Telecom, again. The same ISP accused last year
of "hijacking the vital internet backbone of western
World Y Business’ Markets’ Sustainability’ Legal’ Breakingviews’ Technology’ _Investigatio
Europe
Russia reroutes internet traffic in
occupied Ukraine to its infrastructure
By Reuters
Ai} Aal |<
May 2, 2022 10:23 PM GMT+1 - Updated 3 years ago
```

## Slide 3

“Best”
Route
Destination
BGP
User Network
Router
Bad
Network
Border Gateway Protocol Hi-Jacking

Information Classification: General

#BHEU @BlackHatEvents

## Slide 4

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ae ”
re) e ae
black hat _—< <
EUROPE 2024
hashcat (v6.2.1) starting...
CUDA API (CUDA 11.3)
* Device #1: NVIDIA GeForce RTX 2080 Ti, 10137/11264 MB, 68MCU
Hashes: 1 digests; 1 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, Ox09e0effFF mask, 262144 bytes, 5/13 rotates
Optimizers applied:
Optimized-Kernel
Zero-Byte
Precompute-Init
Early-Skip
Not-Iterated
Prepended-Salt
Single-Hash
Single-Salt
Brute-Force
Raw-Hash
*
*
*
*
*
*
*
*
*
*
Watchdog: Temperature abort trigger set to 9@c
Host memory required for this attack: 1100 MB
€983672a03adcC9767b24584338eb378: 00: hashcat
Information Classification: General
```

## Slide 5

~~How do we encrypt our data better?~~ How do we share keys better?

#BHEU @BlackHatEvents

## Slide 6

##### `$~: whoami`

```
> Dr Frey Wilson
```

```
> CTO @ Cavero Quantum
```

- `Quantum-Safe Symmetric Key Distribution`

Ben Varcoe Co-Founder

George Brumpton Researcher

James Trenholme CEO

…Many PhD Students since 2012

Information Classification: General

#BHEU @BlackHatEvents

## Slide 7

##### Random Number Generation

##### Asymmetric Keys

PKI

Signing

##### Authentication

##### Sharing Symmetric Keys

Ciphers

Information Classification: General

#BHEU @BlackHatEvents

## Slide 8

## Roadmap

- Ingredients for Secrecy

- Existing Methods

- Implications of Quantum Computers

- Quantum Resilient Alternatives Method #1

- • Quantum Resilient Alternatives Method #2

- A New Method!

Information Classification: General

#BHEU @BlackHatEvents

## Slide 9

Eve
Bob
Alice

Information Classification: General

#BHEU @BlackHatEvents

## Slide 10

H(A) H(B)
H(A) + H(B)
Distinguishable

>

H(A) H(B)
H(A,B)
Indistinguishable

Information Classification: General

#BHEU @BlackHatEvents

## Slide 11

#### H(A) + H(B) = H(A,B) + I(A:B)

Information Theoretic Approach

Information Classification: General

#BHEU @BlackHatEvents

## Slide 12

### Computational Complexity #BHEU Approach

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
EUROPE 2024
Cin
Cout
>>> x=[0,45,678,43,52,67,923, 74, 32,376]
>>> ave=sum(x)/len(x)
>>> print(x)
[@, 45, 678, 43, 52, 67, 923, 74, 32, 376]
>>> print(ave)
229.0
>>> 1f 45 in x: print(“found")
. else: print(“not found")
Found
Computational Complexity
inormation Clasication Genera Approach
```

## Slide 13

Prime factors of 616081?

1.5kg
2.2kg
0.8kg
10kg

Computational Complexity Approach

Information Classification: General

#BHEU @BlackHatEvents

## Slide 14

Alice

1-Way! E.g. Primes

Private Public

Eve

Public Private

Bob

Information Classification: General

#BHEU @BlackHatEvents

## Slide 15

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
EUROPE 2024
“sy
im!
—— i.
——]
START _ = = —| j — || _ FINISH
= —__]
% iy =
= __~__ Ms il =
= 4 fal
Information Classification: General
```

## Slide 16

<u>AlphaPhoenix</u>

<u>Local copy</u>

How does electricity find the "Path of Least Resistance"? AlphaPhoenix, YouTube

Information Classification: General

#BHEU @BlackHatEvents

## Slide 17

##### **Searching problems:**

Grover’s Search Shor’s Which problems?

Information Classification: General Image attributed to Satoshi Kawase, for IBM/IBM Research/Flickr

#BHEU @BlackHatEvents

## Slide 18

### Find the closest point?

A + 2B
(0,0)

Lattice Based Code Based Multivariate polynomials Based

Information Classification: General

#BHEU @BlackHatEvents

## Slide 19

### ~~Prime Numbers~~ New Problem

Private Public
Alice

Eve

Public Private
Bob

Information Classification: General

#BHEU @BlackHatEvents

## Slide 20

Eve
Bob
Alice
Prepare
0             1            0         1
These are  These are
the  the
directions I  directions I
measured measured
0         1          0        0

Information Classification: General

#BHEU @BlackHatEvents

## Slide 21

Filter For Correllation
1) On the basis choice
2) “information reconciliation” Alice Bob
Alice Bob
0 0
0 0 E E
0 0
0 0
0 1
0 1
O
E
0 0
0 0
0 0
0 0
E => 00 or 11 O O
1 1
1 1 O => 01 or 10
1 0
…
1 0
E O
1 1
1 1

Information Classification: General

#BHEU @BlackHatEvents

## Slide 22

Alice Bob Eve Eve
0 0 0 0x  1? 0?
E
0 0 1 1x  1? 0?
?
0 1 1 1 1.) 3-wayCorrelated datasets
2.) Indistinguishability for Eve
0 0 0 0
0 0 0 O 0x  1? 0?
? Eve’s strategy = Knapsack problem!
1 1 0 0x  0? 1?
1 0 1 1
1 1 1 1

Information Classification: General

#BHEU @BlackHatEvents

## Slide 23

Alice Bob Eve %
0 Y Y 80%*80%= 64%
0 Y N 80%*20%= 16%
R’
80% 20%
0 N Y 20%*80%= 16%
0 1 0 N N 20%*20%= 4%
R R’
80%80%20%20%
0 1 0 1

Information Classification: General

#BHEU @BlackHatEvents

## Slide 24

Eve RA
Bob
Alice
0
R A RA RA B RAB
1
0 0 0 0 0 0
0
1 0 1 1 1 0
0
1 1 0 0 1 1
0
0 0 0 0 0 0
0
0 0 0 0 1 1
1
1 1 0 0 0 0
1
0 1 1 1 1 0
0
1 0 1 1 0 1
0 0 0 0 0 0

Information Classification: General

#BHEU @BlackHatEvents

## Slide 25

#### H(A) + H(B) = H(A,B) + I(A:B)

P(R=0)       = 0.5 P(RAB=0)  = 0.5 P(R,RAB)   = 0.5

… This only applies when length of string, L →∞

H ∝ P

##### I(A:B) = 0

Information Classification: General

#BHEU @BlackHatEvents

## Slide 26

### Random numbers are weird!

H, T, T, T, H, H, H, T, H, T, H, T

6 HEADS, 6 TAILS

P(H)=0.5

H, T, T, H, H, H, H, T, H, T, H, H

7 HEADS, 5 TAILS

P(H)=0.58

Both of these were generated from the same unbiased coin P(H)=0.5

Information Classification: General

#BHEU @BlackHatEvents

## Slide 27

For small samples, all the different possibilities have a real chance of happening!

<u>Local Copy</u>

“You can mix 10 marbles until they sort themselves. Why not 100?” AlphaPhoenix, YouTube

Information Classification: General

#BHEU @BlackHatEvents

## Slide 28

#### **Kolmogorov Complexity**

K(A) < K(B)

A = 0000000000

“10x0”

B = 0110100011

“1x0, 2x1, 1x0, 1x1, 3x0, 2x1”

What if K(A) +K(B) > K(A,B)?

**A B A,B** 0 0 0,0 0 1 0,1 1 1 1,1 1x0, 1x1, 1x0, 1x1 2x0, 2x1 0 0 0,0 0 1 0,1 1 0 1,0 1 1 1,1 0 0 0,0 0 0 0,0

Information Classification: General

#BHEU @BlackHatEvents

## Slide 29

- 1) R, A → RA

   - Eve has RA

- 2)  B → RAB

##### 3) Filter & keep correlation

##### 4) Privacy amplification

R A RA RA B RAB 0 0 0 0 0 0 1 0 1 1 1 0 1 1 0 0 1 1 0 0 0 0 0 0 0 0 0 0 1 1 1 1 0 0 0 0 0 1 1 1 1 0 1 0 1 1 0 1 0 0 0 0 0 0

- Preferential filtering for Bob = Eve retains errors

- Correlation filter has ambiguity

Information Classification: General

#BHEU @BlackHatEvents

## Slide 30

### **Authentication?**

Integrity detectable = Verifiable consistent conversation

Key first, authenticate later = Peer-to-peer mutual authentication

PKI integrable

Information Classification: General

#BHEU @BlackHatEvents

## Slide 31

##### Overhead:

Processing vs Communication (IoT?)

Definable security

Assuming BQP ≠ NP-Complete → Quantum-safe

Information Classification: General

#BHEU @BlackHatEvents

## Slide 32

## Roadmap

- ~~Ingredients for Secrecy~~

- ~~Existing Methods~~

- ~~Implications of Quantum Computers~~

- ~~Quantum Resilient Alternatives Method #1~~

- ~~Quantum Resilient Alternatives Method #2~~

- A New Method!

Information Classification: General

#BHEU @BlackHatEvents

## Slide 33

### **SoundBytes:**

- 1) Secrecy is a matter of perspective

- 2) Random numbers have weird properties

- 3) RKKE – Reciprocal Kolmogorov Key Establishment – a lightweight alternative

Information Classification: General

#BHEU @BlackHatEvents

## Slide 34

# Thank You

**SoundBytes:**

1) Secrecy is a matter of perspective

- 2) Random numbers have weird properties

3) RKKE – Reciprocal Kolmogorov Key Establishment – a lightweight alternative

#BHEU @BlackHatEvents
