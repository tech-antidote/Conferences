---
title: "Microarchitecture Vulnerabilities Past, Present, and Future"
speakers: ["Anders Fogh", "Daniel Gruss"]
conference: "Black Hat"
conference_full: "Black Hat USA 2024"
edition: "USA"
year: 2024
source_pdf: "Black Hat USA 2024 slides/Anders Fogh & Daniel Gruss_Microarchitecture Vulnerabilities Past, Present, and Future.pdf"
pages: 66
sha256: "38ecfbadb2425e688981a57ee50001755f4901de727036a4b629b45cf0001a8b"
text_chars: 23172
ocr_pages: 16
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:29:17Z"
---
# Microarchitecture Vulnerabilities Past, Present, and Future

**Speakers:** Anders Fogh, Daniel Gruss  
**Conference:** Black Hat USA 2024  
**Source:** `Black Hat USA 2024 slides/Anders Fogh & Daniel Gruss_Microarchitecture Vulnerabilities Past, Present, and Future.pdf` (66 pages)


## Slide 1

Microarchitecture Vulnerabilities

Past, Present and Future

Daniel Gruss (Graz University of Technology) Anders Fogh (Intel Corporation)

## Slide 2

### Introduction

**Daniel Gruss** Graz University of Technology

**Anders Fogh** Intel

Daniel and Anders do not always agree!!

## Slide 3

Past

## Slide 4

#### Past – earliest days

Side Channels always existed

## Slide 5

#### Past – earliest days

Side Channels always existed

First scientific observations in 1943

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Past — earliest days
TEMPEST: A Signal Problem
The story of the discovery
Side Channels always existed of various compromising radiations
from communications and Comsec equipment.
First scientific observations in 1943
impractical. Hydraulic techniques—to replace the
electrical—were tried and abandoned, and experiments
were made with different types of batteries and motor
generators, in attempts to lick the power-line problem.
None was very successful.
During this period, the business of discovering new
TEMPEST threats, or refining techniques and
instrumentation for dececting, recording, and analyzing
these signals, progressed more swiftly than the art of
suppressing them. Perhaps the attack is more exciting than
the defense—something more glamorous about finding a
way to read one of these signals than going through the
drudgery necessary to suppress that whacking great spike
first seen in 1943. At any rate, when they turned over the
next rock, they found the acoustic problem under it.
Phenomenon No. 5.
Acoustics
We found that most acoustic emanations are difficult to
exploit if the microphonic device is outside of the room
containing the source equipment; even a piece of paper
inserted between, say, an offending keyboard and a pick-up
```

## Slide 6

#### Past – earliest days

Side Channels always existed First scientific observations in 1943

Concept of “covert channels” in 1973

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Past — earliest days
Side Channels always existed
First scientific observations in 1943
Concept of “covert channels” in 1973
Operating C. Weissman
Systems Editor
A Note onthe
Confinement Problem
Butler W. Lampson
Xerox Palo Alto Research Center
This note explores the problem of confining a
program during its execution so that it cannot transmit
information to any other program except its caller. A
set of examples attempts to stake out the boundaries of
the problem. Necessary conditions for a solution are
stated and informally justified.
Communications October 1973
of Volume 16
the ACM Number 10
```

## Slide 7

#### Past – earliest days

Side Channels always existed First scientific observations in 1943

Concept of “covert channels” in 1973 1974-1980: Provable secure operating systems with exceptions for side channels

1985: Orange book. Covert channels with low bandwidth not a problem

1996: Paul Kocher’s seminal work on timing attacks

## Slide 8

Past:

#### cryptographic attacks

1996-2015 Mainly side channels on cryptography (threat model!)

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Past:
cryptographic attacks
1996-2015 Mainly side channels on
cryptography (threat model!)
FL IMAGINATION
A CRYPTO NERD'S
HIS LAPTOP'S ENCRYPTED.
LETS BUILD A MILLION-DOLLAR,
ma To CRACK \T-
NO GooD! IT's
ay -BIT ;
eat Ug
1S FOILED! “
1
WHAT \WOULD
ACTUALLY HAPPEN:
HIS LAPTOP'S ENCRYPTED.
DRUG HIM AND HIT HIM WITH
THIS $5 WRENCH UNTIL
HE, t US THE. PASSWORD.
oy IT.
q
```

## Slide 9

Past:

cryptographic attacks 1996-2015 Mainly side channels on cryptography (threat model!) Colin Percival (2005): “Cache Missing for fun and profit”

## Slide 10

Past: Moving beyond crypto

ISCA 2014 + BlackHat US 2015: **Rowhammer**

## Slide 11

Past:

#### Moving beyond crypto

ISCA 2014 + BlackHat US 2015: **Rowhammer**

USENIX Security 2015: **Cache Template Attacks**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Past:
Moving beyond crypto
ISCA 2014 + BlackHat US 2015:
Rowhammer
USENIX Security 2015:
Cache Template Attacks
0x:
/usr/lib/x86_64-linux-gnu/gedit/Libgedit .so
```

## Slide 12

#### Past: Moving beyond crypto

ISCA 2014 + BlackHat US 2015:

**Rowhammer**

USENIX Security 2015: **Cache Template Attacks**

CCS + BlackHat US 2016: **Breaking KASLR**

## Slide 13

#### Past: Moving beyond crypto

ISCA 2014 + BlackHat US 2015: **Rowhammer** USENIX Security 2015: **Cache Template Attacks** CCS + BlackHat US 2016: **Breaking KASLR** 2017: Many academic works on **attacking TEEs with side channels**

USENIX + BlackHat US 2018, S&P 2019:

## Slide 14

Past: Moving beyond crypto

ISCA 2014 + BlackHat US 2015: **Rowhammer**

USENIX Security 2015: **Cache Template Attacks**

CCS + BlackHat US 2016: **Breaking KASLR**

2017: Many academic works on **attacking TEEs with side channels**

USENIX + BlackHat US 2018, S&P 2019: **Spectre & Meltdown**

## Slide 15

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
(a) preface
architectural
time
```

## Slide 16

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
(a) preface (2) trigger instruction
y
SS
architectural transient execution
time
```

## Slide 17

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
(a) preface (2) trigger instruction
(3) transient access to secret
architectural transient execution
time
```

## Slide 18

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
(a) preface (2) trigger instruction
(3) transient access to secret
(4) transmission of secret
y
Ss
(GN
architectural transient execution !
time
```

## Slide 19

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
(a) preface (2) trigger instruction (5) fixup
' —_o.
, tenet ; (3) transient access to secret ' \||
, (4) transmission of secret
L~ = 4 ' — '
architectural transient execution architectural
>
time
```

## Slide 20

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
(a) preface (2) trigger instruction (5) fixup
W
(3) transient access to secret
(4) transmission of secret
J
&
(6) reconstruct
y
Ss
a
architectural transient execution ' architectural
time
>
```

## Slide 21

## Past: Meltdown

1. Window gadget starts executing

2. Mov rbx, [KernelAddress] starts executing

3. Mov rbx, [KernelAddress] Finish execution and deliver data

4. Store in Side Channel (SC): starts execution with data from 3.

5. Store in Side Channel (SC): Data is used to touch the cache allowing the attacker to recover the data

6. Windows Gadget finishes

7. Fault is raised by “Mov rbx, [KernelAddress] “. All registers are cleared but data maintain persistent in the cache.

**<window gadget> mov rbx,[kerneladdress] <recover via SC>**

Out-of-Order unit – out of order execution (track speculation & faults)

## Slide 22

## Meltdown: Details

Row L1 “front end” All data for
VA[6..13]
AGU Provide all data from ways VA L1 “back
Calculate  end”
Virtual  Select relevant data
Address and return data to
(VA) DTLB OoO
PA
Get Physical Address (PA)
VA (way select)
&
Raise faults
<window gadget>  mov rbx,[kerneladdress] <recover via SC>
Out-of-Order unit – out of order execution (track speculation & faults)
Kernel  address
Faults Data

## Slide 23

## Meltdown: Details

###### 1. OoO Trigger load to AGU

Row L1 “front end” All data for
AGU VA[6..13] Provide all data from ways VA L1 “back
Calculate  end”
Virtual  Select relevant
Address data and return
(VA) DTLB PA data to OoO
Get Physical Address (PA)
VA (way select)
&
Raise faults
<window  <recover via
gadget>  mov rbx,[kerneladdress] SC>
Out-of-Order unit – out of order execution (track speculation & faults)
Kernel  address
Faults Data

## Slide 24

## Meltdown: Details

1. 1.OoO Trigger load to
AGU
2. 2.AGU sends
index to L1 &  Row L1 “front end” All data for
AGU VA[6..13] Provide all data from ways VA L1 “back
VA to DTLB Calculate  end”
Virtual  Select relevant
Address data and return
(VA) DTLB PA data to OoO
Get Physical Address (PA)
VA (way select)
&
Raise faults
<window  <recover via
gadget>  mov rbx,[kerneladdress] SC>
Out-of-Order unit – out of order execution (track speculation & faults)
Kernel  address
Faults Data

## Slide 25

## Meltdown: Details

1. OoO Trigger load to AGU

AGU sends index to
Row L1 “front end” All data for
L1 identifies all  AGU VA[6..13] Provide all data from ways VA L1 “back
Calculate  end”
cache lines for  Virtual  Select relevant
Address data and return
(VA) DTLB PA data to OoO
Get Physical Address (PA)
VA (way select)
&
Raise faults
<window  <recover via
gadget>  mov rbx,[kerneladdress] SC>
Out-of-Order unit – out of order execution (track speculation & faults)
Kernel  address
Faults Data

2. AGU sends index to L1 & VA to DTLB

3. L1 identifies all cache lines for for index

## Slide 26

## Meltdown: Details

1. 1.OoO Trigger load to
AGU
2. 2.AGU sends index to
L1 & VA to DTLB Row L1 “front end” All data for
3. 3.a L1 identifies all  AGU VA[6..13] Provide all data from ways VA L1 “back
cache lines for for  Calculate  end”
index Virtual  Select relevant
Address data and return
4. DTLB sends PA  (VA) DTLB data to OoO
PA
Get Physical Address (PA)
VA (way select)
to L1 and faults  &
Raise faults
to OoO
<window  <recover via
gadget>  mov rbx,[kerneladdress] SC>
Out-of-Order unit – out of order execution (track speculation & faults)
Kernel  address
Faults Data

## Slide 27

## Meltdown: Details

1. OoO Trigger load to AGU

2. AGU sends index to L1 & VA to DTLB

3. L1 identifies all cache lines for for index

4. DTLB sends PA & faults  to L1/OoO

5. L1 send right data to OoO

AGU sends index to
Row L1 “front end” All data for
L1 identifies all cache  AGU VA[6..13] Provide all data from ways VA L1 “back
Calculate  end”
DTLB sends PA &  Virtual  Select relevant
Address data and return
(VA) DTLB PA data to OoO
Get Physical Address (PA)
VA (way select)
L1 send right  &
Raise faults
<window  <recover via
gadget>  mov rbx,[kerneladdress] SC>
Out-of-Order unit – out of order execution (track speculation & faults)
Kernel  address
Faults Data

## Slide 28

## Meltdown: Details

1. OoO Trigger load to AGU

2. AGU sends index to L1 & VA to DTLB

3. L1 identifies all cache lines for for index

4. DTLB sends PA & faults  to L1/OoO

5. L1 send right data to OoO

2. AGU sends index to
L1 & VA to DTLB Row L1 “front end” All data for
3. L1 identifies all cache  AGU VA[6..13] Provide all data from ways VA L1 “back
lines for for index Calculate  end”
4. DTLB sends PA &  Virtual  Select relevant
Address data and return
faults  to L1/OoO (VA) DTLB PA data to OoO
5. L1 send right data to  VA Get Physical Address (PA) (way select)
&
OoO
Raise faults
6. OoO execute
depend
instructions
<window  <recover via
gadget>  mov rbx,[kerneladdress] SC>
Out-of-Order unit – out of order execution (track speculation & faults)
Kernel  address
Faults Data

## Slide 29

## The First Meltdown Mitigations

Row L1 “front end” All data for
VA[6..13]
AGU Provide all data from ways VA L1 “back
Calculate  end”
Virtual  Select relevant data
Address and return data to
(VA) DTLB OoO
PA
Get Physical Address (PA) If Fault return 0
VA (way select)
&
+Faults
Raise faults
<window gadget>  mov rbx,[kerneladdress] <recover via SC>
Out-of-Order unit – out of order execution (track speculation & faults)
Kernel  address
Faults
or 0Data

## Slide 30

## Meltdown defense in depth  (LASS)

AGU
Calculate  Row L1 “front end” All data for
VA[6..13]
Virtual  Provide all data from ways VA L1 “back
Address
end”
(VA)
If CPL=3  Select relevant data
&& and return data to
VA&bit[63] DTLB PA OoO
raise fault Get Physical Address (PA) If Fault return 0
VA (way select)
and stop &  +Faults
Raise faults
<window gadget>  mov rbx,[kerneladdress] <recover via SC>
Out-of-Order unit – out of order execution (track speculation & faults)
KA
Fault Faults
or 0Data

## Slide 31

Spectre and LVI

## Slide 32

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Methodology
p-Arch Buffer
[|
Leakage =
Injection S
= PHT BranchScope [79], Bluethunder [131]| Spectre-PHT [174]
S 5 BTB SBPA [8], BranchShadow [182] Spectre-BTB [174]
8 a RSB Hyper-Channel [46] Spectre-RSB [177, 200]
Gy 24 STL — Spectre-STL [128]
é NULL EchoLoad [49] LVLNULL [311]
i L1D Meltdown [193], Foreshadow [310] | LVI-L1D [311]
= FPU LazyFP [291] LVLFPU [311]
39 SB Store-to-Leak [270], Fallout [48] LVI-SB [311]
a LFB/LP ZombieLoad [276], RIDL [267] LVLLFB/LP [311]
```

## Slide 33

**Present**

## Slide 34

#### Present: Trends

**Attack type Activity level (Point) Mitigation Notable** Crypto side channels Guidance & DOIT Data dependent features for ↘ example  data dependent prefetchers Transient execution ↘ Hardware + Software Predictive store forwarding vulnerabilities +on/off switches Workarounds Stale data vulnerabilities ↘ Microcode Patches or Not any recent attacks SW Mitigation (if possible) Logical bugs ↗ Microcode Patches Reptar, CacheWarp (if possible) Physical properties Hertzbleed, Collide+Power ↗ Exploitation methods Spectre & Power ↗

## Slide 35

Logic Issues

## Slide 36

Reptar - What’s supposed to happen REPNZ is a prefix that will repeat an operation until the Z-flag becomes zero.

MOVSB will copy a single byte from DS:[RSI] to ES:[RDI] and increment both registers and decrement RCX & update flags. REPNZ MOVSB is thus a simple memcpy.

The REX-prefix (REX.PF) changes the meaning of how explicit operands of an instruction are interpreted. MOVSB doesn’t have any explicit operands.

If you use the REX-prefix with REPNZ MOVSB the CPU should ignore the prefix entirely

## Slide 37

### Reptar - The bug

When the REX-prefix is parsed instead of ignored a single bit is overwritten.

This cause an invalid input to be used to generate uOps.

Under certain conditions this leads to a machine check. Careful analysis found that a condition could potentially lead to privilege escalation. A microcode change that mitigates the issue has been made public.

## Slide 38

### Cachewarp

Confidential VM (encrypted but basically no data integrity)

**invd** instruction can invalidate a single cache line

Attack in three steps:

1. let confidential VM modify a target cache line

2. use **invd** to drop the modification

3. confidential VM continues  with an outdated value

## Slide 39

### Zenbleed

Register names are just for the user, CPU uses register file

XMM Register Merge Optimization: merge registers (e.g. zero registers)

also: for zero just set a zero-bit

Zenbleed:

1. misspeculation

2. **vzeroupper** → set zero-bit

3. merge → storage in register file released

4. victim stores data in this register

5. unroll misspeculation

6. architectural access to a victim data

## Slide 40

Exploitation Techniques

## Slide 41

#### Exploitation techniques - example

GhostRace: Exploiting and Mitigating Speculative Race Conditions - Hany Ragab et. al.

Spectre v1. variant that speculatively bypasses synchronization primitives.

Existing methods of mitigating Spectre v1 remain effective.

Quote from the papers abstract:

- “ _There’s is security, and then there’s just being ridiculous_ ”  - Linus Torvalds, on Speculative Race Conditions

## Slide 42

# Physical Domain in Software

## Slide 43

Software-based Power Analysis

before 2020: mainly fingerprinting

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Software-based
Power Analysis 6 letters
before 2020: mainly fingerprinting
7 letters
——Test Run 1
— = Test Run 3
1 1
1 1
1 f] | -->-Test Run 2
1 !
1 !
Nea Rea 4
4 ‘ L
Power[Watt]
Time[100 milliseconds]
```

## Slide 44

#### Software-based Power Analysis

before 2020: mainly fingerprinting

2020: Platypus full recovery of cryptographic keys

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Software-based
Power Analysis
before 2020: mainly fingerprinting
2020: Platypus
full recovery of cryptographic keys
ete teow ell we meme ocmammmntian? oA was sonsers cometneum ilonttentedn®? Sie eumee amathd “Po favba
peseutined
1,010) |
z wore oon wt o cemermmane
22 LOO PEAT TMA TT ETM AP ATT TT TA AMAT ATE TT TTT
95
e Oat PO RAE tS Rk OE he fe cars ote ce eF Malae Me MM PROBS iy gp? OOOUMOR LS
1,000 foe « -
© eee Te “ee Cec cou f | !
0 50 100 150 200 250 300 350 400 450 500
Key Bit
Fig. 13: Core voltage per measured instruction for each key bit offset in the fixed window length implementation of mbed
TLS inside an SGX enclave on the Xeon E3-1275 v5. The blue marks represent | bits, while the red marks represent 0 bits.
Using a threshold (dashed line), they can easily be distinguished.
```

## Slide 45

#### Software-based Power Analysis

before 2020: mainly fingerprinting

2020: Platypus full recovery of cryptographic keys

2023: Hertzbleed DVFS makes timing a proxy for energy consumption → remote attacks

## Slide 46

#### Software-based Power Analysis

before 2020: mainly fingerprinting

2020: Platypus full recovery of cryptographic keys

2023: Hertzbleed DVFS makes timing a proxy for energy consumption → remote attacks

2023: Collide+Power Generic Attacks (not just crypto)

## Slide 47

#### Software-based Fault Attacks

since 2015: Rowhammer still not solved!

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Software-based
Fault Attacks
since 2015: Rowhammer
still not solved!
ZENHAMMER: Rowhammer Attacks on AMD Zen-based Platforms
Patrick Jattke’ | Max Wipflit Flavien Solt Michele Marazzi_ Matej Bolcskei_ Kaveh Razavi
ETH Zurich
Table 10. Analysis of the bit flip exploitability found during the sweep over 256 MiB on AMD Zen 2, Zen 3, and Intel Coffee Lake. For each
attack, we indicate the number of exploitable bit flips (#Ex.) and average time to find an exploitable bit flip (Time). We mark DIMMs with a
single exploitable bit flip by (*). We omit DIMMs without any exploitable bit flips.
PTE [36] RSA-2048 [34] sudo [11]
DIMM Zen 2 Zen 3 Coffee Lake Zen2 Zen 3 Coffee Lake Zen 2 Zen 3 Coffee Lake
#Ex. Time #Ex. Time #Ex. Time #Ex. Time #Ex. Time #Ex. Time  #Ex.T. #Ex. Time #Ex. Time
So 76m 4s 7 2m55s 34m 15s 17 2m47s_ 37 46s 14 Im 36s -- 4 3m 13s 1 *23m 49s
Si 90 9s 1474 2s 846 2s 6 2m 2s 27 30s 21 26s -- 1 *6m 50s 1 *Im 20s
iy} 641 21s 5326 Is 126 lls 30 2ml6s 170 6s 6 Im 59s -- 12 Iml7s’) - -
83 142 9s 61 32s - - 7 2m2!1s - - - - -- - - - -
S4 220 28s 323m 52s 2658 Is 712m 29s 1*23m 52s 53 26s -- = - 4 5m 16s
Ss 102 6s 625 2s 330 As 6 Iml4s 28 33s Il lm 5s -- 2 5m 58s 3 2m 34s
ooo = =< =— A ———e = — 4 -e - a4 Ss 2
```

## Slide 48

Software-based Fault Attacks

since 2015: Rowhammer still not solved!

2017: CLKScrew

overclock and attack Arm TrustZone

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Software-based
Fault Attacks
since 2015: Rowhammer
still not solved!
2017: CLKScrew
overclock and attack Arm TrustZone
Correct
Trustzone Normal
_
secret AES
i ae Rrinertox
é
key decryption
Faulty
Trustzone Normal
ee
3h
+p
secret AES
key decryption
0.7
> 0.6
$05
oO
£04
20.3
E 0.2
i)
20.1
0.0
a
123 45 67 8
# of faulted AES rounds
Normalized frequency
ia Sete
i i
Differential Sot
Fault Analysis [1 key
Hp |S fault
>/S faulty
“! plaintext
2
a
2
uu
a
BR
2
w
o
N
oO
e
1 3 5 7 9 11 13 15
# of faulted bytes within one round
```

## Slide 49

#### Software-based Fault Attacks

since 2015: Rowhammer still not solved!

2017: CLKSkrew overclock and attack Arm TrustZone

2020: Plundervolt (VoltJockey, V0ltpwn, VoltPillager) undervolt and attack Intel SGX

## Slide 50

Mitigation efforts

## Slide 51

#### Limitations of mitigations

Physical hardware cannot be changed in the field

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Limitations of
mitigations
Physical hardware cannot be
changed in the field
r M HERETO PATCH THE
| CIRCUITRY! IN'YOUR PROCESSOR
```

## Slide 52

#### Limitations of mitigations

Physical hardware cannot be changed in the field

## Slide 53

#### Limitations of mitigations

Physical hardware cannot be changed in the field

Vendors build in “Survivability features” Microcode is the most common used tool for mitigations.

Other firmware is also used

Instructions

Microcode / Firmware

Hardware

## Slide 54

#### Limitations of mitigations

Physical hardware cannot be changed in the field Vendors build in “Survivability features” Microcode is the most common used tool for mitigations.

Other firmware is also used

“Chicken bits” to disable / change behavior

## Slide 55

#### Limitations of mitigations

Physical hardware cannot be changed in the field

Vendors build in “Survivability features” Microcode is the most common used tool for mitigations.

Other firmware is also used

“Chicken bits” to disable / change behavior Some issues are best mitigated in software

## Slide 56

#### Limitations of mitigations

Physical hardware cannot be changed in the field Vendors build in “Survivability features”

Microcode is the most common used tool for mitigations.

Other firmware is also used

Mitigations are **not always possible/reasonable** and almost always **difficult** and **time-consuming** to engineer

“Chicken bits” to disable / change behavior Some issues are best mitigated in software

## Slide 57

### Prevention Pre-silicon

Prevention starts before the product exist: pre-silicon Pre-silicon is slow and cumbersome as the chips are emulated or simulated. This makes security validation & research significantly different from software validation

● Gives great ROI
● There is formal and informal reviews on
Architecture reviews
01 arch
● Taint tracking has proven useful for
some issues
02 Taint tracking ● Techniques such as  CellFT used in
production
● Security properties to standard
validation
Validation
03 ● FInds bugs during development
● Formal works well with hardware IP
● Formal definition of security properties
Formal validation
04 can be done, but not easy
● Bug analysis should lead to lessons
Defense in depth &
learned
05 hardening

## Slide 58

### Post-silicon

Prevention in silicon happens before product ship from A0 to shipping systems. Some issues are best found in post-silicon. Post-silicon issues are particularly difficult. Learning from issues on last generation hardware is critically important.

● Manual research is effective
● Enabled by expertise, documentation,
Manual research
01 access to devs, debug, etc.
● Early silicon helps prevent escapes
● Variant analysis on every issue
● Occasionally finds issues, but lots of
Variant analysis
02 learning for systematic efforts
● Especially useful on early silicon
● Regression issues
Validation
03 ● Issues not easily found in pre-si
● Problematic: Large state space, slow
with good feedback
04 Fuzzing ● There are exceptions

## Slide 59

Future

## Slide 60

#### Future of uArch  security is future of uArch

Silicon performance is the main underlying driver for growth in compute ecosystem

Performance comes from 3 sources

- New process technology

- uArch improvements

- Adaptation to changed workloads

uArch improvements & Changed workloads will lead to new security challenges

## Slide 61

#### uArch security future

###### Offense

New kinds of prediction & data dependent behaviors (memory latency!). Memory is order of magnitude slower than compute. Some examples:

- New kinds of caches and bigger caches

- Work load specific prefetchers

- Different kinds of value prediction

- Cache & memory compression

- ● Growth in reorder buffer sizes

- New exploitation techniques

##### Defense

- Increased maturity

   - Better tooling

   - More defense in depth

- New microarchitecture security features

- More configurability of security

   - Ex.PSF switch on AMD

- Improved support for software influence

   - Ex. Local configuration switches

## Slide 62

### New kinds of compute

more heterogeneous - but all have uArch:

- GPU (new use cases)

   - Remote accessible

   - Increased complexity and new work loads

   - ○ Example: “LeftoverLocals” by Trails of Bits

- Neural Processing Units

   - New model of compute

   - New threats: Integrity of models

   - Attack vector against system

- AI training accelerators in the cloud

   - Soon: shared resources + multi tenant

- More generally: More kinds of compute, more accelerators

## Slide 63

#### Defensive side of things

Huge gap between academia and industry: Academia

- provable Rowhammer mitigations available

- provable secure cache available

###### Industry

- probabilistic Rowhammer mitigations

- secure caches not adopted (but non-inclusive LLCs)

## Slide 64

### uArch in uArch

Embedded processors everywhere -- already with speculation: Speculation vs confidentiality?

- Threat models rarely contain arbitrary execution

   - → constrains attackers

- Embedded processors often provide low-level access → new and different kinds of assets

## Slide 65

### Take Aways

Side channels are **here to stay**

- Side channels **can be managed**

more aspects of microarchitecture and different kinds of issues

- Hard work for both offensive research and defense

- Defense is maturing

Microarchitecture is a **growth area** , so is microarchitecture security Microarchitecture matters, so does microarchitecture security

## Slide 66

Microarchitecture Vulnerabilities

Past, Present and Future

Daniel Gruss (Graz University of Technology) Anders Fogh (Intel Corporation)
