---
title: "Faults in Our Bus Novel Bus Fault Attack to Break Trusted Execution Environments in Embedded Systems"
speakers: ["Nimish Mishra", "Anirban Chakraborty", "Debdeep Mukhopadhyay"]
conference: "Black Hat"
conference_full: "Black Hat ASIA 2024"
edition: "ASIA"
year: 2024
source_pdf: "BlackHat ASIA 2024-Slides/Nimish Mishra & Anirban Chakraborty & Debdeep Mukhopadhyay-Faults in Our Bus Novel Bus Fault Attack to Break Trusted Execution Environments in Embedded Systems.pdf"
pages: 78
sha256: "7203dac53f8a289ea92ccec2b3d6f743e2ac280ebd10769f4851191d82e76a01"
text_chars: 25345
ocr_pages: 12
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T00:50:00Z"
---
# Faults in Our Bus Novel Bus Fault Attack to Break Trusted Execution Environments in Embedded Systems

**Speakers:** Nimish Mishra, Anirban Chakraborty, Debdeep Mukhopadhyay  
**Conference:** Black Hat ASIA 2024  
**Source:** `BlackHat ASIA 2024-Slides/Nimish Mishra & Anirban Chakraborty & Debdeep Mukhopadhyay-Faults in Our Bus Novel Bus Fault Attack to Break Trusted Execution Environments in Embedded Systems.pdf` (78 pages)

## Slide 1

# Faults In Our Bus: Novel Bus Fault Attacks to Break ARM TrustZone

Nimish Mishra, Anirban Chakraborty, Debdeep Mukhopadhyay Indian Institute of Technology Kharagpur, India

#BHASIA @BlackHatEvents

## Slide 2

### Who are we?

Nimish Mishra

Anirban Chakraborty

Debdeep Mukhopadhyay

Indian Institute of Technology Kharagpur India

# BHASIA @BlackHatEvents

## Slide 3

### Outline

1. What are Faults?

2. Traditional Fault Points on Embedded Systems and SoCs

3. A (new) Fault Point on SoCs

4. OP-TEE?

5. End-to-end Attack

   - Load (adversarial) Trusted Application through Faults

   - Redirect communication for other Trusted Applications

   - Decrypt (redirected) communication

6. Impact

# BHASIA @BlackHatEvents

## Slide 4

## What are Faults?

# BHASIA @BlackHatEvents

## Slide 5

###### Input

- Actively perturb data or control-flow of a system and gain information about the secret through faulty system response

Correct Output

Incorrect Output

# BHASIA @BlackHatEvents

## Slide 6

- Fault causes error and error can be exploited to leak secret information

- Fault attack sometimes combined with side channel can lead to stronger attacks

###### Fault Injection

Side Channel Observation

# BHASIA @BlackHatEvents

## Slide 7

Protocols
Cryptographic
Primitives
Arithmetic
RTL: ALU, REGs, MEM
Logic: Gates, Flip-flops
Transistors

#### The Fault Attack Jungle

Fault Attack on Embedded Systems

Fault Exploitation
Fault Injection

I. Verbauwhede, D. Karaklajid, and J.-M. Schmidt, “The Fault Attack Jungle - A Classification Model to Guide You”, FDTC, 2011

# BHASIA @BlackHatEvents

## Slide 8

#### Fault Attack Vectors

Fig: Electromagnetic Fault Injection (EMFI) Probe

- **WHAT:** Strategically modify execution environment of a system

- **HOW:** Through changes in external operational conditions

Fig: Working principle of EMFI Probe

# BHASIA @BlackHatEvents

## Slide 9

#### FI Attack Vectors

- **WHAT:** Strategically modify execution environment of a system

- **HOW:** Through changes in external operational conditions

- **WHY:** Bias software execution to adversarial advantage

Fig: Representative Fault Attack to introduce a bit-flip

# BHASIA @BlackHatEvents

## Slide 10

#### Fault Models

##### Granularity

1. Single bit

2. Multiple bits

3. Byte or Word

# BHASIA @BlackHatEvents

## Slide 11

#### Fault Models

##### Granularity

##### Fault-type

1. Single bit

   1. Stuck-at (zero or one)

2. Multiple bits

   2. Bit flip

3. Byte or Word

3. Random

# BHASIA @BlackHatEvents

## Slide 12

#### Fault Models

##### Granularity

##### Fault-type

1. Single bit

   1. Stuck-at (zero or one)

2. Multiple bits

   2. Bit flip

3. Byte or Word

3. Random

##### Attacker Control

1. Precise

2. Loose

3. None

# BHASIA @BlackHatEvents

## Slide 13

#### Fault Models

##### Granularity

##### Fault-type

1. Single bit

   1. Stuck-at (zero or one)

2. Multiple bits

   2. Bit flip

3. Byte or Word

3. Random

##### Attacker Control

##### Duration of the fault

1. Precise

   1. Transient

2. Loose

   2. Permanent

3. None

3. Persistent

# BHASIA @BlackHatEvents

## Slide 14

## Traditional Fault Points

# BHASIA @BlackHatEvents

## Slide 15

# BHASIA @BlackHatEvents

## Slide 16

External interface Dynamic (voltage/clock Frequency and glitch) Voltage Scaling (DVFS)

# BHASIA @BlackHatEvents

## Slide 17

External interface Dynamic (voltage/clock Frequency and glitch) Voltage Scaling (DVFS)

Laser/EM Fault
Rowhammer
injection

# BHASIA @BlackHatEvents

## Slide 18

No external interface Privileged (in SoCs; ex RPi)

Laser/EM Fault Rowhammer injection

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
ASIA 2024
-2\YVZ-
! No external interface ! : Laser/EM Fault
(in SoCs: ex RP?) Privileged | ; Rowhammer injection
```

## Slide 19

No external interface Privileged (in SoCs; ex RPi)

Casings ECC checks (requires invasive depackaging)

# BHASIA @BlackHatEvents

## Slide 20

Are there other **architectural aspects** which can be **used for faults** , for which **no known defences** are deployed yet?

# BHASIA @BlackHatEvents

## Slide 21

## A (new) Fault Point on SoCs

# BHASIA @BlackHatEvents

## Slide 22

No external interface Privileged (in SoCs; ex RPi)

Casings ECC checks (requires invasive depackaging)

# BHASIA @BlackHatEvents

## Slide 23

No external interface Privileged (in SoCs; ex RPi)

System Bus

Casings ECC checks (requires invasive depackaging)

# BHASIA @BlackHatEvents

## Slide 24

- Uncased and exposed

- Involved mainly with **load/store** instructions

- Prior works

   - Simulation of bus faults

   - External voltage glitches

   - on PlayStation consoles to **skip** memory cycles

Fig: Exposed bus connections in RPi3

# BHASIA @BlackHatEvents

## Slide 25

#### FI on System Bus: Attack Principle

**load** dest_reg, [mem_addr]

Fig: Electromagnetic Fault Injection probe positioned over the exposed system bus on a RPi3

# BHASIA @BlackHatEvents

## Slide 26

#### FI on System Bus: Attack Principle

mem_addr mem_addr

**load** dest_reg, [mem_addr]

Fig: Electromagnetic Fault Injection probe positioned over the exposed system bus on a RPi3

# BHASIA @BlackHatEvents

## Slide 27

#### FI on System Bus: Attack Principle

mem_addr mem_addr

mem_addr : data
data data

**load** dest_reg, [mem_addr]

Fig: Electromagnetic Fault Injection probe positioned over the exposed system bus on a RPi3

# BHASIA @BlackHatEvents

## Slide 28

#### FI on System Bus: Attack Principle

mem_addr mem_addr

mem_addr : data
data data
mem_addr : data
faulted data data

**load** dest_reg, [mem_addr]

Fig: Electromagnetic Fault Injection probe positioned over the exposed system bus on a RPi3

# BHASIA @BlackHatEvents

## Slide 29

#### FI on System Bus: Success Rates

**load** dest_reg, [mem_addr]

# BHASIA @BlackHatEvents

## Slide 30

#### FI on System Bus: Success Rates

**load** dest_reg, [mem_addr]

Data Bus Faults

- Result in **incorrect data**

- Success rate breakdown

   - **No fault** : 38%

   - **Fault to 0x0:** 35%

▪ **Other cases** : 27%

# BHASIA @BlackHatEvents

## Slide 31

#### FI on System Bus: Success Rates

load dest_reg, [mem_addr]
Data Bus Faults
• Result in  incorrect data
• Success rate breakdown
▪ No fault : 38%
▪
▪ Fault to 0x0:  35%
▪
▪ Other cases : 27%

Address Bus Faults
• Result in  SEGFAULT
• Success rate breakdown
▪ SEGFAULT : 31%
▪ Other cases : 69%

# BHASIA @BlackHatEvents

## Slide 32

#### FI on System Bus: Success Rates

Data Bus Faults

• Result in  incorrect data
• Success rate breakdown
▪ No fault : 38%
▪ Fault to 0x0:  35%
▪ Other cases : 27%

load dest_reg, [mem_addr]
Address Bus Faults
• Result in  SEGFAULT
Register sweeping
(cleans the value of a  load )
• Success rate breakdown
▪ SEGFAULT : 31%
▪ Other cases : 69%

# BHASIA @BlackHatEvents

## Slide 33

**Implication** : Register sweeping to mount an end-to-end attack on Open Portable Trusted Execution Environment (OP-TEE)

# BHASIA @BlackHatEvents

## Slide 34

## OP-TEE?

# BHASIA @BlackHatEvents

## Slide 35

#### "Trusted" Execution Environment

- **WHAT:** An attempt to **disentangle** critical applications from generic software (including kernel)

- **HOW: (** Hardware backed) isolation of system resources

- **OP-TEE:** Implementation of **GlobalPlatformAPI** specification for ARM TZ

`o` Maintained by the **Trusted Firmware,** with members like Google, ARM, Linaro, NXP, STMicroelectronics

`o` Deployed in commercial platforms like Apertis, iWave, and so on

# BHASIA @BlackHatEvents

## Slide 36

#### "Trusted" Execution Environment

- **Two main divisions**

   1. **TEE or Trusted Execution Environment**

Execution context where all the security critical operations reside. TEE has its own

- a) **secure/encrypted memory storage,**

- b) **secure I/O peripherals,**

- c) **secure context switching**

# BHASIA @BlackHatEvents

## Slide 37

#### "Trusted" Execution Environment

- **Two main divisions**

   1. **TEE or Trusted Execution Environment**

Execution context where all the security critical operations reside. TEE has its own

- a) **secure/encrypted memory storage,**

b) **secure I/O peripherals,**

c) **secure context switching**

2. **REE or Rich Execution Environment**

Execution context where rest of the things run. REE invokes the services of TEE when required.

# BHASIA @BlackHatEvents

## Slide 38

"Trusted" Execution Environment

- **Two main divisions**

   1. **TEE or Trusted Execution Environment**

   2. **REE or Rich Execution Environment**

**Note:** <u>All Trusted Applications (TAs) running in the TEE are checked for integrity, implying no adversary having complete control over REE can execute arbitrary TEE code.</u>

# BHASIA @BlackHatEvents

## Slide 39

"Trusted" Execution Environment

- **Two main divisions**

   1. **TEE or Trusted Execution Environment**

   2. **REE or Rich Execution Environment**

ADVERSARIAL GOAL !

**Note:** <u>All Trusted Applications (TAs) running in the TEE are checked for integrity, implying no adversary having complete control over REE can execute arbitrary TEE code.</u>

# BHASIA @BlackHatEvents

## Slide 40

#### Adversarial Goals

- **Goal 1 :** Entire attack must be **online** (without taking the device offline)

# BHASIA @BlackHatEvents

## Slide 41

#### Adversarial Goals

- **Goal 1 :** Entire attack must be **online** (without taking the device offline)

   - **Challenge 1** : Secure Boot cannot be attacked (requires taking the device offline)

(Our) **Solution** : Attack the loading of Trusted Applications in the TEE

# BHASIA @BlackHatEvents

## Slide 42

#### Adversarial Goals

- **Goal 1 :** Entire attack must be **online** (without taking the device offline)

   - **Challenge 1** : Secure Boot cannot be attacked (requires taking the device offline)

      - (Our) **Solution** : Attack the loading of Trusted Applications in the TEE

   - **Challenge 2 :** Cannot use **code-based** triggers (requires code modifications to the OP-TEE kernel) (Our) **Solution** : Construct a combined adversary (side-channel analysis + fault injection)

# BHASIA @BlackHatEvents

## Slide 43

#### Adversarial Goals

**Goal 2 :** The attack must be non-invasive

# BHASIA @BlackHatEvents

## Slide 44

#### Adversarial Goals

**Goal 2 :** The attack must be non-invasive

- **Challenge 3** : Cannot inject processor faults (requires depackaging). Trivial attacks like instruction skips cannot work (Our) **Solution** : Work with a new fault model (register sweeping) on the system-bus (requires no

- invasive alterations to the target device)

# BHASIA @BlackHatEvents

## Slide 45

#### Fault Attack Target

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Q
black hat
ASIA 2024
Fault Attack Target
, Userspace
1 Exception
i Level 0
'
!'
, Kernelspace
1 Exception
tLevel 1
!
Secure world
SVC call
[f: utee_*()
and
tee_svc_*()]
Crypto library invocation |SMCI
[f: erypto_*()]
Libtomcerypt
Normal world
inne
'
'
'
sare as ,
initiation « Innocent CA
'
'
!
i
[f: TEE_*()]
invoke a function
ee
SMC
SMC interface
Secure monitor call handler v
(Exception Layer 2)
```

## Slide 46

#### Fault Attack Target

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Q
black hat
ASIA 2024
Secure world
Fault Attack Target pee TA
Normal world
'
!
1 Exception 8 '
tLevel 0 . '
define TEE_SUCCESS 0x00000000 ‘ ts utee *0) i ar
#define TEE_ERROR_SECURITY 0xFFFFOO0F : ae - '
1 * wane ee :
TEE_Result verify_signature(char* ta_binary , uint8_t* signature) { 1 tee_eve Oly initiation Innocent CA ’
if(/*signature is valid */) ' f: TEE 1) ' °
return TEE_SUCCESS; pe thea ner ptr belt cy bet er function ;
return TEE_ERROR_SECURITY ; i TEE t) ) in TA
} , Kernelspace t:| “kt witb OOO SH OO Re G eee OS
1 Exception a) JRE Free eS ee
I) Youd va TAL ré¥erended by: a-0A inexet 1 : 1REE Kernelspace Exception Level 1
void load_TA(...) { ° ‘ , $
some code here F Crypto library invocation SMCI , : G |
TEE_Result res = verify_signature(...) ; [f: erypto_*()] ; a iP
if(res != TEE_SUCCESS) t SMC ¢ \
// abort execution ' : ' i (
: MC interf:
POTS CINGTONGOHE. Here Libtomerypt ; ' SVC handler ic
1 '
'
Secure monitor call handler
(Exception Layer 2)
```

## Slide 47

#### Fault Attack Target

External glitch DVFS

Stealing signing key

Rowhammer

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Q
black hat
ASIA 2024
Secure world
Fault Attack Target pee TA
1 Exception
Normal world
i Level 0
1 Exception Level 0
!
!
'
;
!
z SVC call '
¥define TEE_SUCCESS 0x00000000 eaten i i —
#define TEE_ERROR_SECURITY 0xFFFFOO0F ana No —
'
\ ;
'
'
'
'
TEE_Result verify_signature(char* ta_binary , uint8_t* signature) {
g
a
<
°o
=
=
==
2
i—4
ity
=
3
»
Innocent CA
if(/*signature is valid */) f: TEE 1) |
return TEE_SUCCESS; Pie Nechot pierre rire series || Meee percae
return TEE_ERROR_SECURITY ; ie ' in TA
} , Kernelspace ' eendecsecescusesaseese
1 Exception a) JRE Free eS ee
// load a TA referenced by a CA re! : 'REE | Kernelspace Exception Level 1 !
, SS red ae F Crypto library invocation |SMCI ; | ! e
TEE_Result res = verify_signature(...) ; [f: erypto_*()] ' : a iP
if(res != TEE_SUCCESS) t SMC a '
// abort execution ' Je : '
' SMC interface
some more code here P Libtomerypt ; ' SVC handler
' '
'
Secure monitor call handler v
aw, (Exception Layer 2)
External glitch DVFS Rowhammer _ Stealing signing key
```

## Slide 48

#### Fault Attack Target

Protected TA Signing key not Not Available Not Available stored on device

# BHASIA @BlackHatEvents

access

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Q
black hat
ASIA 2024
Secure world
TEE !' Normal world
au ac arge i Userspace TA will §| Goenka eke aeeu
1 Exception : ' | | REE Userspace '
i Level 0 m ' 1 Exception Level 0 é
z SVC call '
define TEE_SUCCESS 0x00000000 ' tutes *() i 1 —
#define TEE_ERROR_SECURITY 0xFFFFOOOF d Tena Owl! os
1 * sare as :
TEE_Result verify_signature(char* ta_binary , uint8_t* signature) { ' toe_avo Ol initiation . ; Innocent CA '
if(/* signature is valid */) ' \(f TEE “Oy ' |
return TEE_SUCCESS; ei ti aco ne apn hetioct ta pee ee || epee tren
return TEE_ERROR_SECURITY ; ie t) ) in TA
} , Kernelspace t:| “kt witb OOO SH OO Re G eee OS
Exception SVCH Dp = || Fenciinca os Lassi ais ied ale DS rrr
// load a TA referenced by a CA inexet 1 , (REE Kernelspace Exception Level 1
‘ pcs red ae F Crypto library invocation |SMCI ; | ! e '
TEE_Result res = verify_signature(...) ; [f: erypto_*()] ' : a PD
if(res != TEE_SUCCESS) : SMC 1],
// abort execution ' ¢ 1 . '
: SMC interface
/ some more code here Libtomerypt ; ' SVC handler
} i p| Sere eee cedewooeocecce
Pabesebeeausieewae cee at SMC
Secure monitor call handler
(Exception Layer 2)
4
EVR ]
Protected TA Signing key not
Not Available Not Available ane stored on device
```

## Slide 49

#### Fault Attack Target

**Register Sweeping** : Fault the load to 0x0 through data bus faults

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Q
black hat
ASIA 2024
Secure world
Fault Attack Target ‘eesnace 14
Normal world
(f: TEE_*()]
if(/*signature is valid */)
!
1 Exception ps . {REE Userspace '
eo tee, i Level 0 f™ — ' \Exception Level 0 :
. SVC call ' ;
TEE_SUCCESS 0x00000000 Pil aig — .
09.61.” TEE ERROR SECURFY OxFFFFOOOF ain es —| '
TEE_Result verify_signature(char* ta_binary , uint8_t* signature) { ' tee_sve_*()] initiation : Innocent CA '
'
'
'
SMC interface
/ some more code here
Libtomcerypt
BLE eee ee ee ee ea weet Ae, I
return TEE_SUCCESS; Pie Nthak pie arte iat besiege a ee eee
return TEE_ERROR_SECURITY ; i TEE ' in TA
} , Kernelspace ' bb nh e.6 & 66666 6 64H HOEE
/! load a TA referenced by a CA re! 1 | 'REE |Kernelspace Exception Level 1 !
, ee : : Sa / ae F Crypto library invocation |SMCI ; | ! e '
TEE_Result res = verify_signature(...) ; [f: erypto_*()] ' “ a iP
if(res != TEE_SUCCESS) ; svc. ot |
// abort execution ' ¢ 1 '
' '
'
Secure monitor call handler
(Exception Layer 2)
Register Sweeping: Fault the load to 0x0 through data bus
faults
```

## Slide 50

#### Fault Attack Target

FAULT INJECTION TARGET!

**Register Sweeping** : Fault the load to 0x0 through data bus faults

# BHASIA @BlackHatEvents

## Slide 51

#### Fault Attack Results

- **No Effect** ( denoted by a "dot" ) : No effect of the injected fault

- **Partial Success** : Injected fault changes the value of the load, but not to 0x0. Or causes SEGFAULT

- **Success** : Faults value of the load to 0x0.

# BHASIA @BlackHatEvents

## Slide 52

## End to End Attack

Load (adversarial) Trusted Applications through Faults Redirect communication for other Trusted Applications Decrypt (redirected) communication

# BHASIA @BlackHatEvents

## Slide 53

End to End Attack Load (adversarial) Trusted Applications through Faults

# BHASIA @BlackHatEvents

## Slide 54

#### Combined Adversary = Power SCA + FI

Power side-channel to inform fault injection in a **non-invasive** way (no recompilation of OP-TEE necessary)

# BHASIA @BlackHatEvents

## Slide 55

#### Combined Adversary = Power SCA + FI

Power side-channel to inform fault injection in a **non-invasive** way (no recompilation of OP-TEE necessary)

Actual Fault Injection on signature verification

# BHASIA @BlackHatEvents

## Slide 56

#### Combined Adversary = Power SCA + FI

FAULT INJECTION TARGET!

56

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Q
black hat
ASIA 2024
Combined Adversary = Power SCA + FI
ldr
bl oO acipher_r
cmp wO, #0x0
str wo, 6 | b.eq le® <shdr_verify_signature+Oxle0> // b.none
MOV wO, #Oxf FF FOOT / #-65521
FAULT INJECTION TARGET! i Biois fe
ldr wO, [Sp, #76] Malicious TA
| cmp wo, #0x0 not loaded
Stack after execution
of str w0, [sp, #76
Sidé-view of electromagnetic [sp ]
fault injection loop Without fault injection
Oooo OOt0
ldr wO, [Sp, #76] Malicious TA
| : emp w0, #0x0 loaded
Stack after execution
Side-view of electromagnetic of str w0, [sp, #76]
fault injection loop With fault injection
```

## Slide 57

#### Combined Adversary = Power SCA + FI

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Q
black hat
ASIA 2024
Combined Adversary = Power SCA + FI
0000 0000 .....
Idr w0, [sp, #76] ; Malicious TA
‘ {oF ia ‘a emp wo, #0x0 loaded
Stack after execution
Side-view of electromagnetic of str w0, [sp, #76]
Caciinecnys Hier fault injection loop With fault injection
```

## Slide 58

**Fallout** : **Register sweeping fault attack** loads a **self-signed** , adversarial controlled Trusted Application in the secure world of OP-TEE

# BHASIA @BlackHatEvents

## Slide 59

**Fallout** : **Register sweeping fault attack** loads a **self-signed** , adversarial controlled Trusted Application in the secure world of OP-TEE

# BHASIA @BlackHatEvents

## Slide 60

End to End Attack Redirect communication for other Trusted Applications

# BHASIA @BlackHatEvents

## Slide 61

#### Communication Redirection

Insecure World

Secure World

**U** niversally **U** nique **ID** entifier (UUID) comparison

Secure Trusted Application execution

# BHASIA @BlackHatEvents

## Slide 62

#### Communication Redirection

**Our Findings:** GlobalPlatform API specification (upon which OP-TEE is constructed) **offloads** the responsibility of choosing UUID to **Original Equipment Manufacturer** . It is the responsibility of the OEM to ensure **no two Trusted Applications (TA) share same UUID** .

# BHASIA @BlackHatEvents

## Slide 63

#### Communication Redirection

**Our Findings:** GlobalPlatform API specification (upon which OP-TEE is constructed) **offloads** the responsibility of choosing UUID to **Original Equipment Manufacturer** . It is the responsibility of the OEM to ensure **no two Trusted Applications (TA) share same UUID** .

**UUID confusion:** Behaviour of the system when **UUID are non-unique is undefined** . Our empirical conclusion is that, when UUIDs are shared, a **non-persistent TA is preferred over persistent TA.**

# BHASIA @BlackHatEvents

## Slide 64

#### Communication Redirection

Insecure World

Secure World

**U** niversally **U** nique **ID** entifier (UUID) comparison (with **self-signed TA** loaded after r **egister sweeping** attack)

Secure Trusted Application execution ( **persistent TA** )

Self-signed Trusted Application execution ( **non-persistent TA** with UUID confusion)

# BHASIA @BlackHatEvents

## Slide 65

End to End Attack Decrypt (redirected) communication

# BHASIA @BlackHatEvents

## Slide 66

#### Decrypt (redirected) communication

###### **Third Party extension: SeCReT**

- Symmetric key management

- Blocks SIGTRAP

- Blocks unauthorized read to sensitive data pages

# BHASIA @BlackHatEvents

## Slide 67

#### Decrypt (redirected) communication

**Third Party extension: SeCReT**

- Symmetric key management

- Blocks SIGTRAP

- Blocks unauthorized read to sensitive data pages

# BHASIA @BlackHatEvents

## Slide 68

#### Decrypt (redirected) communication

**Third Party extension: SeCReT**

- Symmetric key management

- Blocks SIGTRAP

- Blocks unauthorized read to sensitive data pages

- Does not block SIGSEGV. Leaks key through coredumps

# BHASIA @BlackHatEvents

## Slide 69

#### Decrypt (redirected) communication

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Q
black hat
ASIA 2024
Decrypt (redirected) communication
(gdb) bt Memory access violation
#8 PQCLEAN DILITHIUM2 CLEAN polyt@_ unpack ( y=Oxbefb43c8,| a=Oxbffffbd8 <error: Cannot access memory at address Oxbffffbd8> by faulting address bus
entry=0x107dal8 "\250\322b\017\241\377/\366\201\025\273M\373\26532'\822\ 342 \007\7\246\376\3510\ 235 \802\257\ 305 OT \n\ 2372429) \202\ob\O24\258- \253\262\346cH\03]
'\234\340N\240\250\313° \036\2010!\307_\340\347\322\376(\241u\361e\037\071\277 - }\O31\240\ 177 . \242] v\177N\267 ! ON\O25\062\261\370F\353\352\ 060U\326\070A\332\340\200\ 267\\
\227\320\331\t2\2413\236\215B\265\\\t\2541\020\ 305\ 335\ 344] \223\350\310\n\681U\023\272G\ 237\035\223\238\t (4Z5\226\225\344\265*\ 326 ( \O30m\ 342\2281\833\221\261q\256\366
\©36\314\0711\363\256\031\023Y\334\306\ 006\264\ 305 ( ]\345\215\350\071\a\377\ 006 ?\370\a\235 (\b1TQ\004\264"...) at 7694
#1 in PQCLEAN DILITHIUM2 CLEAN unpack sk ( rho@entry=6xbefbOeed ""
=OxbefbOfOO “mb2-°E+\241\204dV\211\321\ F\266\340\004Z\ 304\ O35F {\226\371D? ; \O30\266hT\331A2\237\211\267V\ 025 7\262\250\ 032\344\ 377 {npm\274\621\320U\274\3
27\374\V\324\354\032\277  \27271\216\330$"
=Oxbefb0f20 “T\331A2\2 37\211\267v\0257\262\250\032\344\ 377 {nom\274\021\320U\274\327\374\v\ 324\354\032\277 \27271\216\330$'
t € y=Oxbefb43c0, sl=Oxbefb13c8, sl =Oxbefb13cé, =Oxbefb53c8, s2 try=Oxbefb53c6, sk=Oxbefb1728 "", sk try=0xb6f38000 "D/\083") at ; }.c:155
#2 in PQCLEAN DILITHIUM2 CLEAN crypto sign siqnature (sia- try=0x107e790 "", c =0x0, | ntry=Oxbefbd426,
=0x107f104 “This is a very random message", engentry=30,
a /=0x107d6b8 Faraet functior b\b\274=\261\177\003?7\231mb2-“E\ 025 ?\262\250\032\ 344\ 377 {nmm\274\021\320U\274\327\374\v\324\354\ 63
2\277° \27271\216\330$+\241 ___ 26\371D? ; \O30\266hT\331A2\237\211\267v\020\2310\033\067N\233\602\022") at :107
#3 in LPOCLEAN DILITHIUM2 CLEAN crypto sign! (sm=0x107e790 “", =Oxbefbd420, m=0x18950 “This is a very random message", 2n=30,
K=Ox107d0b8 "\a2TL\254\330, \304\245\ 177V\233\351C\200\D\D\ 2 74=\001\ 177 \003? \23 1b 2s *E\0257\262\250\032\344\ 37 7 {nmm\274\021\ 3200 \274\ 327 \374\V\524\ 5504 \030\077 V2
71\216\330$+\241\204dV\211\321\ f\266\340\6042Z\ 304\035F{\226\371D? ; \630\266hT\ 331A2\237\211\267v\626\2310\033\067N\233\002\622") at } :227 1
#4 in main () Leaked secret key
(gdb) §
```

## Slide 70

End to End Attack Bird's eye-view

# BHASIA @BlackHatEvents

## Slide 71

#### End to End Attack

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Q
black hat
ASIA 2024
End to End Attack
; ; © Actual behaviour after attack 1: Malicious TA installed
Attack 1: Installing malicious TA
; Attack 2: UUID
fag poms OY | (einen >
g Gatekeeper @® y 8 | MLaaS TA
jo
Loading TA (2) ca, = we Malicious non-persistent 1. Decrypt
&B | a TA with UUID x 2. Change message
3. Re-encrypt
Inte 4. Re-sign
ity ei Innocent CA eg Path
res = verify_signature(); invoking TA with
if ( "verification is not successful*/ ) UUID x Attack 3: Breaking
return TEE_ERROR_SECURITY;
open session with TA*
TA signature verification code a i ial
Expected behaviour: abort with 5 ‘
TEE_ERROR_SECURITY Normal world Secure world
SIGSEGV signals through EM faults WY Leaked encryption and signing keys
v
encryption and source
authentication to
access MLaaS
```

## Slide 72

## Impact

# BHASIA @BlackHatEvents

## Slide 73

#### Responsible Disclosure

- CVE 2022-47549

- Worked together with Linaro to deploy countermeasure in OP-TEE kernel

● **Website:** <u>https://nimishmishra.wixsite.com/disarmament</u>

# BHASIA @BlackHatEvents

## Slide 74

#### Countermeasure

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Q
black hat
ASIA 2024
Countermeasure
- res = crypto_acipher_rsassa_verify(shdr->algo, &key, shdr->hash_size,
- SHDR_GET_HASH(shdr), shdr->hash_size,
me SHDR_GET_SIG(shdr), shdr->sig_size);
+ FTMN_CALL_FUNC(res, &ftmn, FTMN_INCR®O,
+ crypto_acipher_rsassa verify, shdr-—>algo, &key,
+ shdr->hash_size, SHDR_GET_HASH({shdr), shdr->hash_size,
+ SHDR_GET_SIG(shdr), shdr->sig_size);
+ ftmn_checkpoint(&ftmn, FTMN_INCR®@);
+ goto out;
‘ }
+ err_incr = 1;
+ err:
+ res = TEE_ERROR_SECURITY;
+ FTMN_SET_CHECK_RES_NOT_ZERO(&ftmn, err_incr * FTMN_INCR@, res);
```

## Slide 75

#### Other Implications

- Re-enable Differential Fault Attack (DFA) on T-table implementation of AES (on SoCs)

- Address Bus Faults to leak **all** shares of Masked PQC implementations (like Kyber)

**Observation:** All shares encapsulated within a **single** memory structure

# BHASIA @BlackHatEvents

## Slide 76

#### Takeaways!

- System + Execution Environment, not _just_ the System

- Register sweeping fault model on a (new) architectural aspect – System Bus

   - Implications for other systems?

- Rethinking protocol specifications for embedded systems in light of SCA+FI adversaries

# BHASIA @BlackHatEvents

## Slide 77

##### Research @ Secured Embedded Architecture Laboratory, IIT Kgp

###### **(Some) Research Directions**

- Power/EM **Side-channel evaluation** of FPGAs/micro-controllers/SoCs

- **Fault** Attacks, Fault Analysis, and design of countermeasures

- Evaluation of **Microarchitectural attack** s cenarios on workstations as well as embedded systems

- Others directions…

# BHASIA @BlackHatEvents

## Slide 78

# Thank You!

#BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
a
_ blackhat
X ASIA 2024»
~ PRIL 18-19, 2024 | P ak
/~*X "BRIEFINGS | - - WEBSITE
Thank You!
#BHASIA @BlackHatEvents
```
