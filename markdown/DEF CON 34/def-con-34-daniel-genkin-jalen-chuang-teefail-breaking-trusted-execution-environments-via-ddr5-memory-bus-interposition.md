---
title: "TEE.fail Breaking Trusted Execution Environments via DDR5 Memory Bus Interposition"
speakers: ["Daniel Genkin", "Jalen Chuang"]
conference: "DEF CON"
conference_full: "DEF CON 34"
edition: "34"
year: null
source_pdf: "DEF CON 34/DEF CON 34 - Daniel Genkin, Jalen Chuang - TEE.fail Breaking Trusted Execution Environments via DDR5 Memory Bus Interposition - TEEFail v1.pdf"
pages: 22
sha256: "32adc2f7b42bb4c9842b232af692969eab89d905b6dd8f1bac393ee1552a1327"
text_chars: 7520
ocr_pages: 12
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T00:15:12Z"
---
# TEE.fail Breaking Trusted Execution Environments via DDR5 Memory Bus Interposition

**Speakers:** Daniel Genkin, Jalen Chuang  
**Conference:** DEF CON 34  
**Source:** `DEF CON 34/DEF CON 34 - Daniel Genkin, Jalen Chuang - TEE.fail Breaking Trusted Execution Environments via DDR5 Memory Bus Interposition - TEEFail v1.pdf` (22 pages)


## Slide 1

# TEE.fail: Breaking Trusted Execution Environments via Memory Bus Interposition

**Jalen Chuang Daniel Genkin**

1

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
TEE. fail:
Breaking Trusted Execution Environments
via Memory Bus Interposition
See.
=
bi
- ~~) Georgia Institute
“—” of Technology. W 4 PU RDUE
lL 0
7
Jalen Chuang
=
Oe Daniel Genkin
```

## Slide 2

Bio

**Jalen Chuang**

## **Daniel Genkin**

2

## Slide 3

User Space Enclave Attestation
OS Kernel
VMM
SMM
RAM HW CPU

## Trusted Execution Environments

- Hardware features that enforce data access control and code isolation

- Confidentiality and Integrity of data “guaranteed” by hardware – Even if everything but the CPU is malicious!

- Near native performance

Remote
Client

- Has attestation mechanisms for setting up secure channels with remote clients

- **Trust is entirely based on the attestation key**

- Many versions of this in use today

- Today’s focus: Server TEEs

   - Intel SGX / TDX, latest AMD SEV-SNP

   - Present on many Intel CPUs (since 2016)

3

## Slide 4

## Server SGX and TDX

- SGX has moved from client parts to servers

- TDX was launched (~2023)

   - Just run your VM

   - … but encrypted and totally secure!!!!!

- Much larger encrypted memory

   - From 128MB to 1TB

- Completely different security guarantees

   - Different memory encryption engine

   - CPU still prevents software from reading ciphertext

- TDX security is just as bad, and relies on SGX

4

## Slide 5

## Inside Your Computer…

5

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Inside Your Computer...
intel.
XCON
ye
$a
a9)
So
a2?
apel
$8
a
3
Re
gis
ae
3rd Gen Intel® Xeon®
Scalable Processors
%
```

## Slide 6

How do the pros do it?

6

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
How do the pros do it?
U4970A DDR5 Protocol Debug and Analysis Solution Prices will be shown in your Quote.
Ww KEYSIGHT v | Cancel | Add to Transaction
Y Model Details ¥
6&8 Selected Configurations (26 items) Be
Total: USD 277,565.00
1 B4661A-2FP LPDDR/2/3/4 Listing Decoder, fixed USD 11,234.00 ~«
perpetual license
1 B4661A-3FP DDR/2/3/4 and LPDDR/2/3/4 USD 5,692.00
B4661A-3FP |Validation, fixed perpetual
1 B4661A-4FP DDR3/4, LPDDR2/3/4, and ONFi USD 7,891.00
Analysis, fixed perpetual license
1 B4661A-5FP DDRS5 Analysis and Compliance USD 15,338.00
Validation, fixed perpetual license
1 U4970A-DSC U4970A DDRS5 Bundle (M9502A Chassis -USD 27,868.00
U4164A Logic Analyzer) Bundle DDR5 Bundle (M9502A Chassis U4164A Logic Analyzer)
Adjustment °
Total: USD 277,565.00
```

## Slide 7

## Inside Your Computer…

7

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Inside Your Computer...
intel.
XCON
3rd Gen Intel® Xeon®
Scalable Processors
‘%
```

## Slide 8

## Inside Your Computer…

And don’t do that again!

8

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Inside Your Computer...
And don’t do
that again!
intel.
XCON
3rd Gen Intel® Xeon®
Scalable Processors
\
ress F2 or DEL to run Setup.
Press Fii for Boot Menu.
Detected A ATAPI Devices...
HL-DT-ST DVDRAM GH24NSD1
SATA Port1: ST1O00DM003-1SB10C
Press Fi to Continue
The following Channel memory did not pass CPU memory test
Please remove the memory then plug again.
Channel B
```

## Slide 9

It boots!

CMD pin Clock More Cable (~276 more pins)

9

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
‘Yektronix €SA7404 Communications Signal Analyzer sess B
01 Dec 24 00:12:30
Wwe |
\ oA Kp
More Cable
~2/6 more pins
```

## Slide 10

## MORE CABLE

DDR4 interposer

DDR5 interposer

< $1000 each with secondhand parts

10

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
MORE CABLE
Interposer
DIMM Slot
WW
12 kQ i
ann >To Logie
| |
I]
0.3 pF
Interposer
Edge Connector
(to Motherboard)
DDR4 interposer DDR8& interposer
< $1000 each with secondhand parts Mm
A BB mt
10
```

## Slide 11

Even more cable

11

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Even more cable
11
ThinkCentre
=: succreE=
Horizontal
```

## Slide 12

## Even more cable

12

## Slide 13

Portable setup

13

## Slide 14

Demo 1 – setup and interposer

## Live demo, backup: demo1.mp4

14

## Slide 15

## The Final Note

address

_(tl;dr: we know our encryption sucks)_

Weak Deterministic Encryption Same input becomes same output

15

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
The Final Note
15
*The final thing to note is that Scalable SGX for data center
use TME which relies on AES-XTS mode for confidentiality. address—
block cipher
encryption
The cryptographic scheme used can only mitigate a class of
HW attacks where the adversary can only see the cipher text
once and not while the system is changing the data.
(tl;dr: we know our encryption sucks)
» eae
a Hd | < eT
Weak Deterministic Encryption
Same input becomes same output
Plaintext
CLUTITIITITIITIT)
y
block cipher
encryption
Key: ——~>
LITT TTT ttt)
Ciphertext
```

## Slide 16

## The Final Note

address

_(tl;dr: we know our encryption sucks)_

Let’s see this on real hardware!

16

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
The Final Note
*The final thing to note is that Scalable SGX for data center block cipher
use TME which relies on AES-XTS mode for confidentiality. address>) “encryption
The cryptographic scheme used can only mitigate a class of Plaintext
HW attacks where the adversary can only see the cipher text OOCLOCLLLeErr)
once and not while the system is changing the data.
(tl;dr: we know our encryption sucks) <7
Keys of Beek phe
Let’s see this on
real hardware! Y
CITI TTT TT)
; Ciphertext
DHARWNEOL
5
5
5.
5
5
5
16
```

## Slide 17

## Demo 2 – deterministic encryption

## Live demo

17

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
emo 2 — deterministic encryption
Live demo
:£ Agilent Logic and Protocol Analyzer (LPA) - [.\Desktop\ddrS emo2alal-[Listing-1] - a x
lie Eat View Setup Tools Markers Bur/Stop Listing Window Help
O68 @aw «TH as AL is VUVn”y =
Chckhere to insert new measurements
Sample Number Time Command ChipIDO-2  ChiplID3  BGroup Bank Row0-3 Row 4-17
Column Data Ecc Plaintext Data
NOP
NOP
NOP
NOP
NOP
NOP
Activate
Read
Activate
NOP
NOP
NOP
NOP
NOP
NOP
NOP
NOP
Activate
Read
Activate
NO:
NOP
NOP
NOP
NOP
NOP
NOP
NOP
Activate
Read
Activate
NOP
NOP
NOP
NOP
WWW WWW W/o WW Www ww
42DA
2906
90CA
DOEO
2AA5
3
3
3
3
3
3
3
3
3
3
3
3
3
CER BCR CRCEL ©) © (BUBB BELLE. .) © BUBB CB BLEED Lc! | ol BRL ELE EEL.)
I Geven Wawomt Guang _J
For Help, press F1 Status. Local
```

## Slide 18

## Boring Math Slide

ECSDA Private Quote Attestation Remote Key Client

```
1. z = Hash(quote)
2. k = random()
3. (x,y) = [k]G
4. r = x mod n
5. s = k-1(z+rdpriv)
6. Output (r,s)
```

**Recovering the nonce k reveals the key** k is processed in 5-bit chunks `k K=` **`k1 k`** `2 2` **`k`** `3 3 ... K` **`n [k`** `n132` **`]G`** `... [k]G`

Observe encrypted values and mount a dictionary attack

Deduce  ki
Attestation
Private key
in about 1.5 min

18

## Slide 19

## Demo 3 – key extraction

## Live demo, backup: demo3.mp4

19

## Slide 20

## Who cares?

Attestation Private key

- We extract SGX/TDX attestation keys

   - First time for TDX

- Attacker can pretend to be running a TEE in a genuine Intel CPU

**SGX**

- Signal uses SGX for password recovery (on Azure)

- Blockchains love “decentralized” TEEs

- Support fancy confidential transactions and smart contracts

- Fully decrypted if even a single node is compromised ☺

- NVIDIA Confidential Compute relies on CPU TEE

Use AI
STL file for
 3d printer

SGX

   - Without linking attestation reports to the specific CPU

- AMD SEV-SNP with latest mitigations similarly affected

20

## Slide 21

## Mitigations

- Out of Scope.

   - Intel: “Such attacks are outside the scope of the boundary of protection offered [by SGX / TDX]”

   - Similar response from AMD

   - Users get to deal with it ☺

- Talked to Intel…

- Weak security for performance reasons

   - Gave up integrity, replay protection and randomized encryption

   - At the benefit 30%-50% improvement in memory bandwith

- CPUs can’t be updated to fix this

   - ETA for hardware countermeasures 2029+

- Software fixes have severe performance implications, good luck…

21

## Slide 22

Thanks!

This: https://tee.fail Us: https://architecture.fail

TDX

22DEFCON 34

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
TDX
Frog put the cookies 5 SCX iis he
said. “Now we wil] not eat any more cookies.”
This: https://tee fail
Us: https://architecture. fail
use side
“But we can’ x,” said Toad.
channels
“That is true,” said Frog.
```
