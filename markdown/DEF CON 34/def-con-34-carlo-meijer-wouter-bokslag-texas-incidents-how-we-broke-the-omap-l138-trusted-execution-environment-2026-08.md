---
title: "Texas Incidents - How we broke the OMAP-L138 Trusted Execution Environment"
speakers: ["Carlo Meijer", "Wouter Bokslag"]
conference: "DEF CON"
conference_full: "DEF CON 34"
edition: "34"
year: 2026
source_pdf: "DEF CON 34/DEF CON 34 - Carlo Meijer, Wouter Bokslag - Texas Incidents - How we broke the OMAP-L138 Trusted Execution Environment - 2026 08 05 DEF CON.pdf"
pages: 67
sha256: "b060c3eed70c094b4ac1ec338c7eb13c690204060369aa0fb7c126ae54c0b292"
text_chars: 26745
ocr_pages: 4
has_ocr: true
redacted_secrets: 0
ocr_confidence: 79.2
ocr_unreliable_blocks: 1
ocr_timeouts: 0
pages_recovered_from_text_layer: 1
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T06:24:06Z"
---
# Texas Incidents - How we broke the OMAP-L138 Trusted Execution Environment

**Speakers:** Carlo Meijer, Wouter Bokslag  
**Conference:** DEF CON 34  
**Source:** `DEF CON 34/DEF CON 34 - Carlo Meijer, Wouter Bokslag - Texas Incidents - How we broke the OMAP-L138 Trusted Execution Environment - 2026 08 05 DEF CON.pdf` (67 pages)


## Slide 1

###### **August 2026**

Texas Incidents How we broke the OMAP-L138 Trusted Execution Environment

###### By Midnight Blue

hello@midnightblue.nl  //  midnightblue.nl  //  All Right Reserved

## Slide 2

Texas Incidents - Breaking the OMAP-L138

Carlo Meijer, MSc Wouter Bokslag, MSc
Jos Wetzels, MSc

# Midnight Blue

Selected Research

midnightblue.nl

2

August 2026

## Slide 3

# The conundrum

sales@midnightblue.nl  //  midnightblue.nl  //  All Right Reserved

## Slide 4

Texas Incidents - Breaking the OMAP-L138

## What if you somehow need to…

- break a Trusted Execution Environment;

- based on robust AES and RSA crypto primitives,

- implemented on an obscure DSP architecture,

- that has HORRENDOUS features like a 6-stage pipeline combined with executing up to 8 instructions in parallel per clockcycle,

- and for which no public tooling is available?

midnightblue.nl

August 2026

4

## Slide 5

Texas Incidents - Breaking the OMAP-L138

midnightblue.nl

August 2026

5

## Slide 6

Texas Incidents - Breaking the OMAP-L138

## Motorola MTM5400

- Runs on OMAP-L138

- Contains secret TETRA crypto

- We wanna break this thing real bad

midnightblue.nl

6

August 2026

## Slide 7

OMAP-L138 Uses, outline, architecture

sales@midnightblue.nl  //  midnightblue.nl  //  All Right Reserved

## Slide 8

Texas Incidents - Breaking the OMAP-L138

# Global usage

- Extremely popular*

   - PMR radio (TETRA, DMR, …)

   - Satcomms (Inmarsat, Thuraya, …)

   - Military (Thales, Raytheon, General Dynamics combat radios)

   - Aerospace

- _*Not always  in a security critical role_

midnightblue.nl

8

August 2026

## Slide 9

Texas Incidents - Breaking the OMAP-L138

- Non-secure

# Variants

   - No secure boot, no TEE

   - Excellent public documentation

- Basic secure

###### Security offerings

   - Supports secure boot

   - No run-time security features (no TEE)

   - Limited documentation (need US export approval)

- Custom secure

   - Obviously, that’s the variant we’re dealing with…

   - Documentation made of unobtainium

midnightblue.nl

9

August 2026

## Slide 10

Texas Incidents - Breaking the OMAP-L138

###### Two orthogonal privilege separations Running in Secure mode are:

## Privilege separations

- TI Secure Kernel (Secure Supervisor)

   - ROM code _(TI Secure Kernel)_

   - Implements loading of IP protected algorithms

   - − Implements secure boot

- Customer TEE modules (Secure User)

   - Executed through Secure Kernel API call

   - Nonsecure world can’t see loaded code or data

**Privilege / Security Secure Non-secure Supervisor** Secure Kernel and Secure Boot DSP/BIOS or other OS kernels Loader **User** Licensed Algorithms (e.g. WMV, Non-secure Applications or WMA, etc...) other OS kernels

midnightblue.nl

10

August 2026

## Slide 11

Texas Incidents - Breaking the OMAP-L138

# Generic / Basic Secure

- Processor Security guide (SPRUGQ9)

- No mention of Custom Secure

- No runtime functionality described

- Secure boot based on symmetric signatures (Customer Encryption Key, CEK)

- • But: mention of some Custom Secure-only features

   - SK_algoInvoke

   - SK_load

midnightblue.nl

August 2026

11

## Slide 12

Texas Incidents - Breaking the OMAP-L138

# Custom secure

Reading between the lines

- OMAP-L138 Secure UART Boot Host application from SDK

- Allows for booting of signed, (partially) encrypted images over UART

- Teaches implementation details

midnightblue.nl

August 2026

14

## Slide 13

Texas Incidents - Breaking the OMAP-L138

# Custom secure

Reading between the lines

- RSA???

   - Not mentioned anywhere in public docs

- No way to provide CEK for custom secure chips

   - Programmed by TI at the factory?

midnightblue.nl

August 2026

15

## Slide 14

Texas Incidents - Breaking the OMAP-L138

# Custom secure

###### Reading between the lines

- Signature size in Moto firmware confirms RSA

- • Indeed no (encrypted) CEK present in firmware image or anywhere else in flash

midnightblue.nl

16

August 2026

## Slide 15

Texas Incidents - Breaking the OMAP-L138

###### SK_LOAD

#### Trusted Execution Environment

- Runtime loading of protected algorithms

- • Decrypted code never leaves Secure environment

Non-Secure

Encrypted algorithm code

- Success/Fail, Algorithm ID

Secure (TI ROM)

Decrypt CEK
Algorithm code
Validate  Public
signature Key

midnightblue.nl

18

August 2026

## Slide 16

Texas Incidents - Breaking the OMAP-L138

###### SK_ALGOINVOKE

#### Trusted Execution Environment

###### Non-Secure

Algorithm ID,
Input parameters
Result

Secure (TI ROM)

Invoke
Algorithm
Algorithm
code

- Decrypted code never leaves Secure environment

midnightblue.nl

19

August 2026

## Slide 17

Texas Incidents - Breaking the OMAP-L138

- Digging through TI-SYSBIOS SDK

# sk.h

- Found sk.h

   - Significant Secure Kernel API details

- **`SK_LOAD`** object details

   - .. post-decryption, that is

midnightblue.nl

20

August 2026

## Slide 18

# Let’s get hacking

sales@midnightblue.nl  //  midnightblue.nl  //  All Right Reserved

## Slide 19

Texas Incidents - Breaking the OMAP-L138

### On yesterday’s episode

- Casually exploited format string vuln

   - CodeEx on ARM Application Processor

- Jumped to DSP through misconfigured memory protections

   - Built Linux kernel module with DSP hooking / running framework

- Next step; either:

   - DSP TEE module decryption

   - DSP Secure-mode code execution

midnightblue.nl

22

August 2026

## Slide 20

Texas Incidents - Breaking the OMAP-L138

#### Path forward

SK_LOAD

Secure (TI ROM)

Non-Secure

Encrypted algorithm
Decrypt CEK
code
Algorithm code
Success/Fail, Validate  Public
Algorithm ID signature Key

- We have code execution on the DSP in nonsecure mode

   - Can provide arbitrary (garbage) input to SK_LOAD

- Goal: recover CEK by attacking **`SK_LOAD`** module decryption

- Let’s study the SK_LOAD implementation

   - But we need to find it first

midnightblue.nl

25

August 2026

## Slide 21

Texas Incidents - Breaking the OMAP-L138

# Where’s the code?

- TI ROM code implements boot loader, Secure Kernel (including SK_LOAD)

- Can be read from nonsecure DSP userland

- However, no AES implementation to be found??

- • And, calls into nowhere??

- Conclusion: secret area not readable in nonsecure mode

   - We’re going to have to attack blindly

midnightblue.nl

26

August 2026

## Slide 22

Texas Incidents - Breaking the OMAP-L138

### Inspiration

- Don’t have implementation details − A side channel attack may still be feasible?

- Idea :

   - Modern computers use caches to speed up some memory accesses

   - Introduces timing differences

   - These may leak information on secrets

- DJB 2005*:

   - Build profile of timing characteristics, then observe target system’s characteristics

      - Correlate profile with observation

   - Derive which key fits best

* Cache-timing attacks on AES – Daniel J. Bernstein, 2005

Average AES encryption speed for random plaintexts, with the first input byte set to values 0 .. 256

midnightblue.nl

27

August 2026

## Slide 23

Texas Incidents - Breaking the OMAP-L138

### DSP cache architecture

- L1D, L1C, L2 caches

- L1D data cache: 64-byte lines

- Memory read is..

   - **Fast** if already in cache

   - **Slow** if not in cache

midnightblue.nl

28

August 2026

* TMS320C674x DSP Cache User's Guide (SPRUG82A)

## Slide 24

Texas Incidents - Breaking the OMAP-L138

### DSP cache architecture

- MMIO registers for cache control − Some powerful primitives

- Single-cache-line eviction

   - Can evict data from cache up to 64-bytes granularity

   - This applies to memory inaccessible in nonsecure mode as well

- Cache freeze

   - Cache miss causes no update of the cache, cache hit still results in a speedup

- Idea : partially evict the AES s-box used by SK_LOAD for decryption

   - But we don’t even know its location in memory

midnightblue.nl

29

August 2026

## Slide 25

Texas Incidents - Breaking the OMAP-L138

# Locating the s-box

\```
foreach 64-byte linein secret_rom_area:
evict line from L1D and L2 cache
t_start= time_in_clock_cycles()
\```

\```
SK_LOAD(bogus_module) // will decrypt and then reject mod
num_cycles= time_in_clock_cycles() -t_start
results.append(num_cycles)
\```

midnightblue.nl

30

August 2026

## Slide 26

Texas Incidents - Breaking the OMAP-L138

# Locating the s-box

midnightblue.nl

31

August 2026


> Recovered by OCR — confidence 82/100 on the text kept, 63/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
MIDNIGHT 8tve Texas Incidents - Breaking the OMAP-L138
Locating the s-box
—
2
[=
=
=
e
3
ioc
midnightblue.nl 31 August 2026
```

## Slide 27

# AES deep-ish dive

sales@midnightblue.nl  //  midnightblue.nl  //  All Right Reserved

## Slide 28

Texas Incidents - Breaking the OMAP-L138

# AES structure

- 10 rounds of four basic operations

- Round keys are derived from key

   - Recovering any round key yields the original key

- Our case:

   - Decryption

   - We control ciphertext 𝑐𝑡

   - Round keys 𝑟𝑘10, 𝑟𝑘9, etc are constant

midnightblue.nl

33

August 2026

## Slide 29

Texas Incidents - Breaking the OMAP-L138

### Let’s walk through a decryption

|𝑎0|𝑎1|𝑎2|𝑎3|
|---|---|---|---|
|𝑎4|𝑎5|𝑎6|𝑎7|
|𝑎8|𝑎9|𝑎10|𝑎11|
|𝑎12|𝑎13|𝑎14|𝑎15|

midnightblue.nl

34

August 2026

## Slide 30

Texas Incidents - Breaking the OMAP-L138

𝑎0 𝑎1 𝑎2 𝑎3 𝑎0 ⊕𝑘0 𝑎1 ⊕𝑘1 𝑎2 ⊕𝑘2
𝑎4 𝑎5 𝑎6 𝑎7
𝑎8 𝑎9 𝑎10 𝑎11
𝑎12 𝑎13 𝑎14 𝑎15

𝑏3
𝑏4 𝑏5 𝑏6 𝑏7
𝑏8 𝑏9 𝑏10 𝑏11
𝑏12 𝑏13 𝑏14 𝑏15

AddRoundKey

𝑘0 𝑘1 𝑘2 𝑘3
𝑘4 𝑘5 𝑘6 𝑘7
𝑘8 𝑘9 𝑘10 𝑘11
𝑘12 𝑘13 𝑘14 𝑘15

midnightblue.nl

35

August 2026

## Slide 31

Texas Incidents - Breaking the OMAP-L138

|𝑎0|𝑎1|𝑎2|𝑎3|
|---|---|---|---|
|𝑎4|𝑎5|𝑎6|𝑎7|
|𝑎8|𝑎9|𝑎10|𝑎11|
|𝑎12|𝑎13|𝑎14|𝑎15|

midnightblue.nl

36

August 2026

## Slide 32

Texas Incidents - Breaking the OMAP-L138

0x 1540
𝑎0 𝑎1 𝑎2 𝑎3 0x 4015
0x 722F
00 01 02 03 04 05 06 07 08 09 0a 0b 0c 0d 0e 0f
𝑎4 𝑎5 𝑎6 𝑎7 00 52 09 6a d5 30 36 a5 38 bf 40 a3 9e 81 f3 d7 fb
10 7c e3 39 82 9b 2f ff 87 34 8e 43 44 c4 de e9 cb
20 54 7b 94 32 a6 c2 23 3d ee 4c 95 0b 42 fa c3 4e
𝑎8 𝑎9 𝑎10 𝑎11
30 08 2e a1 66 28 d9 24 b2 76 5b a2 49 6d 8b d1 25
40 72 f8 f6 64 86 68 98 16 d4 a4 5c cc 5d 65 b6 92
𝑎12 𝑎13 𝑎14 𝑎15 50 6c 70 48 50 fd ed b9 da 5e 15 46 57 a7 8d 9d 84
60 90 d8 ab 00 8c bc d3 0a f7 e4 58 05 b8 b3 45 06
70 d0 2c 1e 8f ca 3f 0f 02 c1 af bd 03 01 13 8a 6b
80 3a 91 11 41 4f 67 dc ea 97 f2 cf ce f0 b4 e6 73
𝑏2 𝑏3
90 96 ac 74 22 e7 ad 35 85 e2 f9 37 e8 1c 75 df 6e
a0 47 f1 1a 71 1d 29 c5 89 6f b7 62 0e aa 18 be 1b
b0 fc 56 3e 4b c6 d2 79 20 9a db c0 fe 78 cd 5a f4
𝑏4 𝑏5 𝑏6 𝑏7
c0 1f dd a8 33 88 07 c7 31 b1 12 10 59 27 80 ec 5f
d0 60 51 7f a9 19 b5 4a 0d 2d e5 7a 9f 93 c9 9c ef
𝑏8 𝑏9 𝑏10 𝑏11 e0 a0 e0 3b 4d ae 2a f5 b0 c8 eb bb 3c 83 53 99 61
f0 17 2b 04 7e ba 77 d6 26 e1 69 14 63 55 21 0c 7d
𝑏12 𝑏13 𝑏14 𝑏15
InvSubBytes

midnightblue.nl

37

August 2026

## Slide 33

Texas Incidents - Breaking the OMAP-L138

|𝑎0|𝑎1|𝑎2|𝑎3|𝑏0|𝑏0|
|---|---|---|---|---|---|
|𝑎4|𝑎5|𝑎6|𝑎7|𝑏4|𝑏4|
|𝑎8|𝑎9|𝑎10|𝑎11|𝑏8|𝑏8|
|𝑎12|𝑎13|𝑎14|𝑎15|𝑏12|𝑏12|

|𝑏2|𝑏3|
|---|---|
|𝑏6|𝑏7|
|𝑏10|𝑏11|
|𝑏14|𝑏15|

midnightblue.nl

38

August 2026

## Slide 34

midnightblue.nl
00 01 02 03 04 05 06 07 08 09 0a 0b 0c 0d 0e 0f
00 52 09 6a d5 30 36 a5 38 bf 40 a3 9e 81 f3 d7 fb
10 7c e3 39 82 9b 2f ff 87 34 8e 43 44 c4 de e9 cb
20 54 7b 94 32 a6 c2 23 3d ee 4c 95 0b 42 fa c3 4e
30 08 2e a1 66 28 d9 24 b2 76 5b a2 49 6d 8b d1 25
40 72 f8 f6 64 86 68 98 16 d4 a4 5c cc 5d 65 b6 92
50 6c 70 48 50 fd ed b9 da 5e 15 46 57 a7 8d 9d 84
60 90 d8 ab 00 8c bc d3 0a f7 e4 58 05 b8 b3 45 06
70 d0 2c 1e 8f ca 3f 0f 02 c1 af bd 03 01 13 8a 6b
80 3a 91 11 41 4f 67 dc ea 97 f2 cf ce f0 b4 e6 73
90 96 ac 74 22 e7 ad 35 85 e2 f9 37 e8 1c 75 df 6e
a0 47 f1 1a 71 1d 29 c5 89 6f b7 62 0e aa 18 be 1b
b0 fc 56 3e 4b c6 d2 79 20 9a db c0 fe 78 cd 5a f4
c0 1f dd a8 33 88 07 c7 31 b1 12 10 59 27 80 ec 5f
d0 60 51 7f a9 19 b5 4a 0d 2d e5 7a 9f 93 c9 9c ef
e0 a0 e0 3b 4d ae 2a f5 b0 c8 eb bb 3c 83 53 99 61
f0 17 2b 04 7e ba 77 d6 26 e1 69 14 63 55 21 0c 7d
00 01 02 03 04 05 06 07 08 09 0a 0b 0c 0d 0e 0f
00 52 09 6a d5 30 36 a5 38 bf 40 a3 9e 81 f3 d7 fb
10 7c e3 39 82 9b 2f ff 87 34 8e 43 44 c4 de e9 cb
20 54 7b 94 32 a6 c2 23 3d ee 4c 95 0b 42 fa c3 4e
30 08 2e a1 66 28 d9 24 b2 76 5b a2 49 6d 8b d1 25
40 72 f8 f6 64 86 68 98 16 d4 a4 5c cc 5d 65 b6 92
50 6c 70 48 50 fd ed b9 da 5e 15 46 57 a7 8d 9d 84
60 90 d8 ab 00 8c bc d3 0a f7 e4 58 05 b8 b3 45 06
70 d0 2c 1e 8f ca 3f 0f 02 c1 af bd 03 01 13 8a 6b
80 3a 91 11 41 4f 67 dc ea 97 f2 cf ce f0 b4 e6 73
90 96 ac 74 22 e7 ad 35 85 e2 f9 37 e8 1c 75 df 6e
a0 47 f1 1a 71 1d 29 c5 89 6f b7 62 0e aa 18 be 1b
b0 fc 56 3e 4b c6 d2 79 20 9a db c0 fe 78 cd 5a f4
c0 1f dd a8 33 88 07 c7 31 b1 12 10 59 27 80 ec 5f
d0 60 51 7f a9 19 b5 4a 0d 2d e5 7a 9f 93 c9 9c ef
e0 a0 e0 3b 4d ae 2a f5 b0 c8 eb bb 3c 83 53 99 61
f0 17 2b 04 7e ba 77 d6 26 e1 69 14 63 55 21 0c 7d
August 2026
39
Caches + sbox
lookups
• We found the sbox by
throwing lines out of the
cache
• How about we evict only
first octant of the sbox?
• And then lock the cache
state using cache freeze
• We can count hits to the
evicted first octant!
Texas Incidents - Breaking the OMAP-L138

## Slide 35

Texas Incidents - Breaking the OMAP-L138

# Attack outline

- Having evicted the first octant of sbox from cache (32 entries)…

- Set 𝑐𝑡[0] to 0

- Randomize remainder of 𝑐𝑡

- Get average running time of `SK_LOAD`

- Repeat for other values of 𝑐𝑡[0]

- … plot measurements

midnightblue.nl

40

August 2026

## Slide 36

Texas Incidents - Breaking the OMAP-L138

0 𝑎1 𝑎2 𝑎3 𝑘0 𝑎1 ⊕𝑘1 𝑎2 ⊕𝑘2
𝑎4 𝑎5 𝑎6 𝑎7
𝑎8 𝑎9 𝑎10 𝑎11
𝑎12 𝑎13 𝑎14 𝑎15

𝑏3
𝑏4 𝑏5 𝑏6 𝑏7
𝑏8 𝑏9 𝑏10 𝑏11
𝑏12 𝑏13 𝑏14 𝑏15

𝑘0 𝑘1 𝑘2 𝑘3
Target
𝑘4 𝑘5 𝑘6 𝑘7
𝑘8 𝑘9 𝑘10 𝑘11
𝑘12 𝑘13 𝑘14 𝑘15

midnightblue.nl

August 2026

41

## Slide 37

Texas Incidents - Breaking the OMAP-L138

|𝑘0|𝑎1|𝑎2|𝑎3|
|---|---|---|---|
|𝑎4|𝑎5|𝑎6|𝑎7|
|𝑎8|𝑎9|𝑎10|𝑎11|
|𝑎12|𝑎13|𝑎14|𝑎15|

midnightblue.nl

42

August 2026

## Slide 38

Texas Incidents - Breaking the OMAP-L138

𝑘0
f a =st!
𝑘0 𝑎1 𝑎2 𝑎3 vg
0x32
00 01 02 03 04 05 06 07 08 09 0a 0b 0c 0d 0e 0f
𝑎4 𝑎5 𝑎6 𝑎7 00  52 09 6a d5 30 36 a5 38 bf 40 a3 9e 81 f3 d7 fb
10  7c e3 39 82 9b 2f ff 87 34 8e 43 44 c4 de e9 cb
20  54 7b 94 32 a6 c2 23 3d ee 4c 95 0b 42 fa c3 4e
𝑎8 𝑎9 𝑎10 𝑎11
30  08 2e a1 66 28 d9 24 b2 76 5b a2 49 6d 8b d1 25
40  72 f8 f6 64 86 68 98 16 d4 a4 5c cc 5d 65 b6 92
𝑎12 𝑎13 𝑎14 𝑎15 50  6c 70 48 50 fd ed b9 da 5e 15 46 57 a7 8d 9d 84
60  90 d8 ab 00 8c bc d3 0a f7 e4 58 05 b8 b3 45 06
70  d0 2c 1e 8f ca 3f 0f 02 c1 af bd 03 01 13 8a 6b
80  3a 91 11 41 4f 67 dc ea 97 f2 cf ce f0 b4 e6 73
avg avg
90  96 ac 74 22 e7 ad 35 85 e2 f9 37 e8 1c 75 df 6e
a0  47 f1 1a 71 1d 29 c5 89 6f b7 62 0e aa 18 be 1b
b0  fc 56 3e 4b c6 d2 79 20 9a db c0 fe 78 cd 5a f4
avg avg avg avg
c0  1f dd a8 33 88 07 c7 31 b1 12 10 59 27 80 ec 5f
d0  60 51 7f a9 19 b5 4a 0d 2d e5 7a 9f 93 c9 9c ef
avg avg avg avg e0  a0 e0 3b 4d ae 2a f5 b0 c8 eb bb 3c 83 53 99 61
f0  17 2b 04 7e ba 77 d6 26 e1 69 14 63 55 21 0c 7d
avg avg avg avg
InvSubBytes

midnightblue.nl

43

August 2026

## Slide 39

Texas Incidents - Breaking the OMAP-L138

- If penalty observed: 𝑐𝑡 0 ⊕𝑟𝑘10 0 < 0x20

- • Above example: 0x20 ≤𝑟𝑘10 0 < 0x40

midnightblue.nl

August 2026

44

## Slide 40

Texas Incidents - Breaking the OMAP-L138

# Success!

- In our example: 0x20 ≤𝑟𝑘10 0 < 0x40

- Effectively 3 bits of 𝑟𝑘10 0

- Can repeat to obtain 48 bits of 𝑟𝑘10 !

45

August 2026

midnightblue.nl

## Slide 41

Texas Incidents - Breaking the OMAP-L138

# Success..?

- Inherently limited

   - Least significant 5 bits of 𝑟𝑘10[0] do not influence which sbox octant is hit

   - Still missing 80 bits

   - Too much for exhaustive search

   - We need to go deeper

midnightblue.nl

46

August 2026

## Slide 42

Texas Incidents - Breaking the OMAP-L138

## Extended attack

- Take attack one round further

   - Observe penalties during round 2 `InverseSubBytes`

- Round 1 `InverseSubBytes` has introduced required diffusion within the state byte

   - Least significant bits of 𝑟𝑘10 byte now influence the most significant bits of the state byte

- Need to account for:

   - Diffusion over four state bytes from `InverseMixCols`

   - Shifting of state bytes

   - Influence of 𝑟𝑘9

midnightblue.nl

August 2026

47

## Slide 43

Texas Incidents - Breaking the OMAP-L138

0 𝑎1 𝑎2 𝑎3 𝑘0 𝑎1 ⊕𝑘1 𝑎2 ⊕𝑘2
𝑋
𝑎4 𝑎5 𝑎6
𝑌
𝑎8 𝑎9 𝑎11
𝑍
𝑎12 𝑎14 𝑎15

𝑏3
𝑏4 𝑏5 𝑏6 𝑋′
𝑏8 𝑏9 𝑌′ 𝑏11
𝑏12 𝑍′ 𝑏14 𝑏15

AddRoundKey

𝑘0 𝑘1 𝑘2 𝑘3
𝑘4 𝑘5 𝑘6 𝑘7
𝑘8 𝑘9 𝑘10 𝑘11
𝑘12 𝑘13 𝑘14 𝑘15

midnightblue.nl

48

August 2026

## Slide 44

Texas Incidents - Breaking the OMAP-L138

|𝑘0|𝑎1|𝑎2|𝑎3|
|---|---|---|---|
|𝑎4|𝑎5|𝑎6|𝑋|
|𝑎8|𝑎9|𝑌|𝑎11|
|𝑎12|𝑍|𝑎14|𝑎15|

midnightblue.nl

49

August 2026

## Slide 45

Texas Incidents - Breaking the OMAP-L138

𝑘0
𝑘0 𝑎0 𝑎2 𝑎3 slow=
0x15
00 01 02 03 04 05 06 07 08 09 0a 0b 0c 0d 0e 0f
𝑋
𝑎5 𝑎6 𝑎7 00  52 09 6a d5 30 36 a5 38 bf 40 a3 9e 81 f3 d7 fb
10  7c e3 39 82 9b 2f ff 87 34 8e 43 44 c4 de e9 cb
20  54 7b 94 32 a6 c2 23 3d ee 4c 95 0b 42 fa c3 4e
𝑌
𝑎9 𝑎10 𝑎11
30  08 2e a1 66 28 d9 24 b2 76 5b a2 49 6d 8b d1 25
40  72 f8 f6 64 86 68 98 16 d4 a4 5c cc 5d 65 b6 92
𝑍 𝑎13 𝑎14 𝑎15 50  6c 70 48 50 fd ed b9 da 5e 15 46 57 a7 8d 9d 84
60  90 d8 ab 00 8c bc d3 0a f7 e4 58 05 b8 b3 45 06
70  d0 2c 1e 8f ca 3f 0f 02 c1 af bd 03 01 13 8a 6b
80  3a 91 11 41 4f 67 dc ea 97 f2 cf ce f0 b4 e6 73
avg avg avg
90  96 ac 74 22 e7 ad 35 85 e2 f9 37 e8 1c 75 df 6e
a0  47 f1 1a 71 1d 29 c5 89 6f b7 62 0e aa 18 be 1b
b0  fc 56 3e 4b c6 d2 79 20 9a db c0 fe 78 cd 5a f4
fast
avg avg avg
c0  1f dd a8 33 88 07 c7 31 b1 12 10 59 27 80 ec 5f
d0  60 51 7f a9 19 b5 4a 0d 2d e5 7a 9f 93 c9 9c ef
fast
avg avg avg e0  a0 e0 3b 4d ae 2a f5 b0 c8 eb bb 3c 83 53 99 61
f0  17 2b 04 7e ba 77 d6 26 e1 69 14 63 55 21 0c 7d
slow
avg avg avg
InvSubBytes

midnightblue.nl

50

August 2026

## Slide 46

Texas Incidents - Breaking the OMAP-L138

W 𝑎1 𝑎2 𝑎3 𝑊′ 𝑎1 ⊕𝑘1 𝑎2 ⊕𝑘2
𝑋 𝑋
𝑎5 𝑎6
𝑌 𝑌
𝑎9 𝑎11
𝑍 𝑍
𝑎14 𝑎15

𝑏3
𝑋′ 𝑏5 𝑏6 𝑋′
𝑌′ 𝑏9 𝑌′ 𝑏11
𝑍′ 𝑍′ 𝑏14 𝑏15

𝑟𝑘09 𝑟𝑘19 𝑟𝑘29 𝑟𝑘39
𝑟𝑘49 𝑟𝑘59 𝑟𝑘69 𝑟𝑘79
𝑟𝑘89 𝑟𝑘99 𝑟𝑘109 𝑟𝑘119
𝑟𝑘129 𝑟𝑘139 𝑟𝑘149 𝑟𝑘159

midnightblue.nl

August 2026

51

## Slide 47

Texas Incidents - Breaking the OMAP-L138

𝑊 𝑎1 𝑎2 𝑎3 𝑊′ 𝑏0 𝑏2 𝑏3
𝑋 𝑎5 𝑎6 𝑎7 𝑋′ 𝑏4 𝑏6 𝑏7
𝑌 𝑌′
𝑎9 𝑎10 𝑎11 𝑏8 𝑏10 𝑏11
𝑍 𝑍′
𝑎13 𝑎14 𝑎15 𝑏12 𝑏14 𝑏15

midnightblue.nl

52

August 2026

## Slide 48

Texas Incidents - Breaking the OMAP-L138

|𝑊|𝑎1|𝑎2|𝑎3|
|---|---|---|---|
|𝑋|𝑎5|𝑎6|𝑎7|
|𝑌|𝑎9|𝑎10|𝑎11|
|𝑍|𝑎13|𝑎14|𝑎15|

midnightblue.nl

53

August 2026

## Slide 49

Texas Incidents - Breaking the OMAP-L138

𝑊 𝑎0 𝑎2 𝑎3 0x7dfast
00 01 02 03 04 05 06 07 08 09 0a 0b 0c 0d 0e 0f
𝑋
𝑎5 𝑎6 𝑎7 00 52 09 6a d5 30 36 a5 38 bf 40 a3 9e 81 f3 d7 fb
10 7c e3 39 82 9b 2f ff 87 34 8e 43 44 c4 de e9 cb
20 54 7b 94 32 a6 c2 23 3d ee 4c 95 0b 42 fa c3 4e
𝑌
𝑎10 𝑎9 𝑎11
30 08 2e a1 66 28 d9 24 b2 76 5b a2 49 6d 8b d1 25
40 72 f8 f6 64 86 68 98 16 d4 a4 5c cc 5d 65 b6 92
𝑎15 𝑎13 𝑎14 𝑍 50 6c 70 48 50 fd ed b9 da 5e 15 46 57 a7 8d 9d 84
60 90 d8 ab 00 8c bc d3 0a f7 e4 58 05 b8 b3 45 06
70 d0 2c 1e 8f ca 3f 0f 02 c1 af bd 03 01 13 8a 6b
80 3a 91 11 41 4f 67 dc ea 97 f2 cf ce f0 b4 e6 73
avg avg avg
90 96 ac 74 22 e7 ad 35 85 e2 f9 37 e8 1c 75 df 6e
a0 47 f1 1a 71 1d 29 c5 89 6f b7 62 0e aa 18 be 1b
b0 fc 56 3e 4b c6 d2 79 20 9a db c0 fe 78 cd 5a f4
fast
avg avg avg
c0 1f dd a8 33 88 07 c7 31 b1 12 10 59 27 80 ec 5f
d0 60 51 7f a9 19 b5 4a 0d 2d e5 7a 9f 93 c9 9c ef
slow
avg avg avg e0 a0 e0 3b 4d ae 2a f5 b0 c8 eb bb 3c 83 53 99 61
f0 17 2b 04 7e ba 77 d6 26 e1 69 14 63 55 21 0c 7d
fast
avg avg avg
InvSubBytes

midnightblue.nl

August 2026

54

## Slide 50

Texas Incidents - Breaking the OMAP-L138

# Score

slowfast
avg avg avg
slowfast
avg avg avg
fastslow
avg avg avg
fast
avg avg avg

- For ct[0] = 0 and other column bytes fixed: 1 penalty

• For ct[0] = 1, we may find 2 penalties • .... Etcetera

midnightblue.nl

August 2026

55

## Slide 51

Texas Incidents - Breaking the OMAP-L138

# Fingerprint

- We build a 256-score ‘fingerprint’

- `ct[0] = 0, ct[0] = 1, ..., ct[0] = 256`

   - `↓`

\```
1001201010003120000001010012010100011201100010001100220000...
\```

- Recovered fingerprint uniquely identifies value of 𝑟𝑘10[0]!

   - _Fingerprint →_ 𝑟𝑘10[0] _mappings precomputed once_

   - _Obtain measurements: fingerprint →_ 𝑟𝑘10[0]

   - _Repeat for all positions to recover full_ 𝑟𝑘10 _,_

   - _Then the base key (the Motorola CEK) follows trivially_

midnightblue.nl

56

August 2026

## Slide 52

Texas Incidents - Breaking the OMAP-L138

# Demo: CVE-2022-25332 **`SK_LOAD`** Cache Timing Side-Channel

midnightblue.nl

August 2026

57

## Slide 53

Texas Incidents - Breaking the OMAP-L138

midnightblue.nl

58

August 2026


> Recovered by OCR — confidence 80/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
user@bluelagoon: /tmp/exploit$ python exploit.py && python connect.py
[*] Opening /dev/ttyUSBO at 9600 baud..
[*] Opening /dev/ttyUSBO at 57600 baud..
{+] Serial port initialized
{+] init ok
Shell | Shell No. 2 | Shell No. 3 | Shet! No. 4 (BABIN IIIs
```

## Slide 54

Texas Incidents - Breaking the OMAP-L138

midnightblue.nl

59

August 2026


> Recovered by OCR — confidence 80/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
user@bluelagoon: /tmp/exploit$ python exploit.py && python connect.py
[*] Opening /dev/ttyUSBO at 9600 baud..
[*] Opening /dev/ttyUSBO at 57600 baud..
{+] Serial port initialized
{+] init ok
Shell | Shell No. 2 | Shell No. 3 | Shet! No. 4 (BABIN IIIs
```

## Slide 55

Texas Incidents - Breaking the OMAP-L138

# Not done yet

- We have recovered the CEK

- Header decrypts fine

   - 0xC001BABE magic

- But.. data section header encrypted with different key?

   - ‘session key’ contained in header doesn’t seem to be correct

midnightblue.nl

60

August 2026

## Slide 56

Texas Incidents - Breaking the OMAP-L138

# Rinse and repeat

- It’s just another AES decryption right?

- Repeat same attack, targeting section decryption

- However

   - RSA signature check in the middle

   - Waaay more jitter

   - Needed MANY runs to average out noise

Attack ran for a week…

midnightblue.nl

61

August 2026

## Slide 57

Texas Incidents - Breaking the OMAP-L138

- We have recovered the section key

# Not done yet (again)

- Section header looks good

   - 0x0DEADBEE magic

- Section data has lower entropy

   - 6.6225 out of 8

- … Section data doesn’t look like C6000 instructions…

- Compression? Obfuscation? Hard to tell, we don’t have the code

###### Lamp moment:

- Compare multiple `SK_LOAD` modules

midnightblue.nl

62

August 2026

## Slide 58

Texas Incidents - Breaking the OMAP-L138

- Decrypt the same module taken from different versions of the firmware

# Not done yet (again)

- Inspect them side-by-side

- Interestingly: difference at offset **`x`** ⇒ difference at **`x+16`**

- Turns out: each 16-byte block is XORed with preceding one

   - Unapplying the XOR yields valid C6000 instructions

midnightblue.nl

63

August 2026

## Slide 59

Texas Incidents - Breaking the OMAP-L138

We achieved our goals

Done! But yet..

However, some stuff just didn’t make any sense

_How did we evict 32 bytes from cache if cache lines are 64 bytes?_

_Why is the SK_LOAD module data section 16 bytes larger than indicated in the header?_

Let’s throw in one more day to get some closure

midnightblue.nl

64

August 2026

## Slide 60

# When the walls start crumbling

sales@midnightblue.nl  //  midnightblue.nl  //  All Right Reserved

## Slide 61

Texas Incidents - Breaking the OMAP-L138

|Module Header||Crypt|Sig||
|---|---|---|---|---|
|`uint32`|`loadModMagic`|CEK|**rsaSig**|Module header magic (0xDEADC001, 0xDEADC0FF, 0xC001BABE)|
|`short`|`nSections`|CEK|rsaSig|Number of sections in the module|
|`short`|`modHeaderSize`|CEK|rsaSig|Size of header plus signature|
|`char[16]`|**`sessKey`**|CEK|rsaSig|Used to compute section encryption key|
|`uint32`|`nEntryPoints`|CEK|rsaSig|Number of code entry points in the module body|
|`void *`|`ep`|CEK|rsaSig|Address at which code entry point table resides in body|
|Module Header Signature|||||
|`char[modHeaderSize - 32]`|**`rsaSig`**|CEK|-|RSA signature data; size given in module header|
|Section #1 Header|||||
|`uint32`|`sectHdrMagic`|sessKey*|chksum|Section magic (0x0DEADBEE, 0x0ABEBDEAD)|
|`uint32`|`sectSize`|sessKey*|chksum|Section size|
|`void *`|`sectDest`|sessKey*|chksum|Section loading address in secure RAM|
|`uint32`|`sectAccType`|sessKey*|chksum|Section memory permissions (secure/non-secure access)|
|Section #1 Body|||||
|`char[sectSize]`|`payload`|sessKey*|chksum|(Obfuscated) section body|
|Section #1 Checksum|||||
|`char[16]`|**`chksum`**|sessKey*|-|Section checksum|
|`(further sections)`|||||

midnightblue.nl

66

August 2026

## Slide 62

Texas Incidents - Breaking the OMAP-L138

##### CVE-2022-25333 Flawed **`SK_LOAD`** module authenticity check

- RSA signature only protects header authenticity!

- Section data not cryptographically signed

- We can re-use the signed header, modify section data, re-apply obfuscation/checksum

- Grants code execution in TEE

   - Privilege level (secure user or supervisor) determined by magic in the header

   - `0xc001babe` is for secure supervisor (thanks Motorola)

- Can now dump TI ROM including secret area

   - We have the SK_LOAD implementation now

Can we just always get secure supervisor, even without a correctly signed header?

midnightblue.nl

67

August 2026

## Slide 63

Texas Incidents - Breaking the OMAP-L138

#### Signature check during SK_LOAD

Let’s walk through the header SHA1/RSA check

OS bookkeeping,
Config,
Pointers,
…
sha1_func_ptr
Encrypted sig
hdr(sig size: 256B)Encrypted hdr
Stack Pointer
Local variables,
Return addresses,
…..
DSP Secure RAM
DSP Secure Stack

midnightblue.nl

68

August 2026

## Slide 64

Texas Incidents - Breaking the OMAP-L138

# ROM analysis

midnightblue.nl

69

August 2026


> Recovered by OCR — confidence 74/100 on the text kept, 69/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
MIDNIGHT ®t ve Texas Incidents - Breaking the OMAP-L138
ROM anal
-DSP_L2_ROM:007F8BFO Check decrypted header magic
.DSP_L2_ROM: 007F8BFO ; B13 points to decrypted header
-DSP_L2_ROM:007F8BFO LDW - D2 *+B13, Bi
.DSP_L2_ROM: 007F8BF4 I] MVK 52 (GDEADCGGGR & OFFFFh), B4
.-DSP_L2_ROM: 0O07F8BFC MVK 52 & OFFFFh), B2
-DSP_L2_ROM:007F8CO4 MVK 52 & OFFFFh), BO
.DSP_L2_ROM:007F8C08 MVKH .52 @coo10000h, BO
.DSP_L2_ROM:007F8COC CMPEQ .L2 Bi, B2, B2
-DSP_L2_ROM:007F8C10 MVK -Li 2, Al
-DSP_L2_ROM:007F8C14 [!B2] CMPEQ »L2 B1, B4, B2
-DSP_L2_ROM:007F8C18 | |C!B2] SuB -D1 Al, 1, Al
-DSP_L2_ROM:007F8C1C [C!B2] CMPEQ »L2 B1, BO, B2
-DSP_L2_ROM: 007F8C24 ; No valid magic found, return
-DSP_L2_ROM: 007F8C2C ; Load modHeaderSize field
-DSP_L2_ROM:007F8C30 | |[B2] -D2 *+B13[3], BO
-DSP_L2_ROM:007F8C34
-DSP_L2_ROM:007F8C34 . 32, B2
-DSP_L2_ROM:007F8C36
.DSP_L2_ROM: OO7F8C3C ; We now have Len(signature)
-DSP_L2_ROM: 007F8C3C . n, 1, W, BU, nobr, nosat, 0100000b
.DSP_L2_ROM: 007F8C40 . B1, 2, BO ; Convert bytes to number of dwords
.DSP_L2_ROM: 007F8C44 . B15, BO, B15 ; *-- Decrease stack pointer with len(signature)
midnightblue.nl August 2026
```

## Slide 65

Texas Incidents - Breaking the OMAP-L138

##### CVE-2022-25334 Stack overflow on **`SK_LOAD`** signature length field

OS bookkeeping,
Config,
Pointers,
…
shellcode_addsha1_func_pt ENCR_SIG_DATA r
D E CRYPTEDncrypted sig
hdr(sig sizEncrypt e : d64K hdr)
Stack Pointer
Local variables,
Return addresses,
…..
Secure Kernel RAM
Secure Kernel Stack

midnightblue.nl

70

August 2026

## Slide 66

Texas Incidents - Breaking the OMAP-L138

# Closing thoughts

- We found multiple ROM vulns which bypass secure boot and breaking TEE • In general: Secure Boot and TEE do not provide guarantees

   - Especially if it has to withstand  years of attack

- Please, please:

   - Design with future mitigation in mind

   - Demand transparency from suppliers

   - − Thoroughly assess solutions that matter most

TMS320C674x/OMAP-L1x Processor Security User's Guide (SPRUGQ9)

midnightblue.nl

August 2026

71

## Slide 67

Texas Incidents - Breaking the OMAP-L138

###### Social

## Questions?

###### Web

- midnightblue.nl

Contact

- hello@midnightblue.nl

midnightblue.nl

72

August 2026
