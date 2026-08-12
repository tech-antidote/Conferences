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
text_chars: 19880
ocr_pages: 11
has_ocr: true
redacted_secrets: 0
ocr_confidence: 81.4
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T04:49:09Z"
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


> Recovered by OCR — confidence 87/100 on the text kept, 70/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Fault Attack Target
, Userspace
, Kernelspace
tLevel 1
SVC call
[f: utee_*()
and
tee_svc_*()]
Crypto library invocation |SMCI
[f: erypto_*()]
initiation « Innocent CA
[f: TEE_*()]
invoke a function
ee
SMC
SMC interface
Secure monitor call handler v
```

## Slide 46

#### Fault Attack Target

# BHASIA @BlackHatEvents


> Recovered by OCR — confidence 76/100 on the text kept, 54/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Fault Attack Target pee TA
TEE_Result verify_signature(char* ta_binary , uint8_t* signature) { 1 tee_eve Oly initiation Innocent CA ’
some code here F Crypto library invocation SMCI , : G |
: MC interf:
```

## Slide 47

#### Fault Attack Target

External glitch DVFS

Stealing signing key

Rowhammer

# BHASIA @BlackHatEvents


> Recovered by OCR — confidence 76/100 on the text kept, 60/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Fault Attack Target pee TA
¥define TEE_SUCCESS 0x00000000 eaten i i —
TEE_Result verify_signature(char* ta_binary , uint8_t* signature) {
a
<
=
=
Innocent CA
if(/*signature is valid */) f: TEE 1) |
return TEE_ERROR_SECURITY ; ie ' in TA
// load a TA referenced by a CA re! : 'REE | Kernelspace Exception Level 1 !
// abort execution ' Je : '
' SMC interface
some more code here P Libtomerypt ; ' SVC handler
' '
Secure monitor call handler v
aw, (Exception Layer 2)
External glitch DVFS Rowhammer _ Stealing signing key
```

## Slide 48

#### Fault Attack Target

Protected TA Signing key not Not Available Not Available stored on device

# BHASIA @BlackHatEvents

access


> Recovered by OCR — confidence 78/100 on the text kept, 56/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
TEE !' Normal world
TEE_Result verify_signature(char* ta_binary , uint8_t* signature) { ' toe_avo Ol initiation . ; Innocent CA '
// load a TA referenced by a CA inexet 1 , (REE Kernelspace Exception Level 1
if(res != TEE_SUCCESS) : SMC 1],
: SMC interface
/ some more code here Libtomerypt ; ' SVC handler
Protected TA Signing key not
Not Available Not Available ane stored on device
```

## Slide 49

#### Fault Attack Target

**Register Sweeping** : Fault the load to 0x0 through data bus faults

# BHASIA @BlackHatEvents


> Recovered by OCR — confidence 78/100 on the text kept, 52/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Fault Attack Target ‘eesnace 14
if(/*signature is valid */)
TEE_Result verify_signature(char* ta_binary , uint8_t* signature) { ' tee_sve_*()] initiation : Innocent CA '
SMC interface
/ some more code here
/! load a TA referenced by a CA re! 1 | 'REE |Kernelspace Exception Level 1 !
if(res != TEE_SUCCESS) ; svc. ot |
' '
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


> Recovered by OCR — confidence 82/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Combined Adversary = Power SCA + FI
ldr
bl oO acipher_r
cmp wO, #0x0
str wo, 6 | b.eq le® <shdr_verify_signature+Oxle0> // b.none
ldr wO, [Sp, #76] Malicious TA
Stack after execution
of str w0, [sp, #76
Sidé-view of electromagnetic [sp ]
fault injection loop Without fault injection
ldr wO, [Sp, #76] Malicious TA
| : emp w0, #0x0 loaded
Stack after execution
Side-view of electromagnetic of str w0, [sp, #76]
fault injection loop With fault injection
```

## Slide 57

#### Combined Adversary = Power SCA + FI

# BHASIA @BlackHatEvents


> Recovered by OCR — confidence 85/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Combined Adversary = Power SCA + FI
0000 0000 .....
Idr w0, [sp, #76] ; Malicious TA
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


> Recovered by OCR — confidence 80/100 on the text kept, 58/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Decrypt (redirected) communication
(gdb) bt Memory access violation
#8 PQCLEAN DILITHIUM2 CLEAN polyt@_ unpack ( y=Oxbefb43c8,| a=Oxbffffbd8 <error: Cannot access memory at address Oxbffffbd8> by faulting address bus
#1 in PQCLEAN DILITHIUM2 CLEAN unpack sk ( rho@entry=6xbefbOeed ""
#2 in PQCLEAN DILITHIUM2 CLEAN crypto sign siqnature (sia- try=0x107e790 "", c =0x0, | ntry=Oxbefbd426,
=0x107f104 “This is a very random message", engentry=30,
#3 in LPOCLEAN DILITHIUM2 CLEAN crypto sign! (sm=0x107e790 “", =Oxbefbd420, m=0x18950 “This is a very random message", 2n=30,
#4 in main () Leaked secret key
```

## Slide 70

End to End Attack Bird's eye-view

# BHASIA @BlackHatEvents

## Slide 71

#### End to End Attack

# BHASIA @BlackHatEvents


> Recovered by OCR — confidence 84/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
End to End Attack
; ; © Actual behaviour after attack 1: Malicious TA installed
Attack 1: Installing malicious TA
; Attack 2: UUID
jo
Loading TA (2) ca, = we Malicious non-persistent 1. Decrypt
&B | a TA with UUID x 2. Change message
3. Re-encrypt
Inte 4. Re-sign
res = verify_signature(); invoking TA with
if ( "verification is not successful*/ ) UUID x Attack 3: Breaking
return TEE_ERROR_SECURITY;
open session with TA*
TA signature verification code a i ial
Expected behaviour: abort with 5 ‘
TEE_ERROR_SECURITY Normal world Secure world
SIGSEGV signals through EM faults WY Leaked encryption and signing keys
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


> Recovered by OCR — confidence 84/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Countermeasure
- res = crypto_acipher_rsassa_verify(shdr->algo, &key, shdr->hash_size,
me SHDR_GET_SIG(shdr), shdr->sig_size);
+ FTMN_CALL_FUNC(res, &ftmn, FTMN_INCR®O,
+ crypto_acipher_rsassa verify, shdr-—>algo, &key,
+ shdr->hash_size, SHDR_GET_HASH({shdr), shdr->hash_size,
+ SHDR_GET_SIG(shdr), shdr->sig_size);
+ ftmn_checkpoint(&ftmn, FTMN_INCR®@);
+ goto out;
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


> Recovered by OCR — confidence 85/100 on the text kept, 58/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
a
_ blackhat
Thank You!
#BHASIA @BlackHatEvents
```
