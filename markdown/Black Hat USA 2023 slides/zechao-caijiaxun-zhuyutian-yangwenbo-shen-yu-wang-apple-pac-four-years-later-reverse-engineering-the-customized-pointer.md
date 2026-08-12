---
title: "Apple PAC, Four Years Later Reverse Engineering the Customized Pointer Authentication Hardware Implementation on Apple M1"
speakers: ["Zechao Cai", "Jiaxun Zhu", "Yutian Yang", "Wenbo Shen", "Yu Wang"]
conference: "Black Hat"
conference_full: "Black Hat USA 2023"
edition: "USA"
year: 2023
source_pdf: "Black Hat USA 2023 slides/Zechao Cai,Jiaxun Zhu,Yutian Yang,Wenbo Shen ,Yu Wang _Apple PAC, Four Years Later Reverse Engineering the Customized Pointer Authentication Hardware Implementation on Apple M1.pdf"
pages: 129
sha256: "129de127de201cea66623f60a4654b67e3cb8767435a69fbeb87499ff360b261"
text_chars: 39620
ocr_pages: 2
has_ocr: true
redacted_secrets: 0
ocr_confidence: 93.7
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T04:26:14Z"
---
# Apple PAC, Four Years Later Reverse Engineering the Customized Pointer Authentication Hardware Implementation on Apple M1

**Speakers:** Zechao Cai, Jiaxun Zhu, Yutian Yang, Wenbo Shen, Yu Wang  
**Conference:** Black Hat USA 2023  
**Source:** `Black Hat USA 2023 slides/Zechao Cai,Jiaxun Zhu,Yutian Yang,Wenbo Shen ,Yu Wang _Apple PAC, Four Years Later Reverse Engineering the Customized Pointer Authentication Hardware Implementation on Apple M1.pdf` (129 pages)


## Slide 1

Apple PAC, Four Years Later **Apple PAC, Four Years Later** Reverse Engineering the Customized Pointer Authentication Hardware Implementation on Apple Reverse Engineering the Customized Pointer Authentication M1 Hardware Implementation on Apple M1 Speaker(s):

Zechao Cai (@Zech4o)

#BHUSA @BlackHatEvents#BHUSA   @BlackHatEvents

## Slide 2

###### Whoami

###### **- Zechao/Zachary Cai @Zech4o -**

**Master Student at Zhejiang University Focus on**

- **OS Security**

**- Reverse Engineering**

**- Virtualization**

#BHUSA @BlackHatEvents

## Slide 3

###### Contributors

###### **Jiaxun Zhu (@svnswords):**

###### **Yutian Yang:**

- Student at **Zhejiang University**

   - Student at **Zhejiang University**

- Member of **AAA** CTF Team

- • Focus on *OS security and Android Hook

- • Building **M1 macOS** fuzzing framework and unlimited debugger

- Working toward a Ph.D. degree

- • Focus on OS kernel security and static program analysis for bug detection

- Won **ACSAC 22** distinguished paper award

###### **Wenbo Shen:**

- ZJU100 Professor at **Zhejiang University**

- • Focus on operating system security, software supply chain security, and container security

- Won three awards distinguished paper

- ( **NDSS 16** , **AsiaCCS 17** , **ACSAC 22** )

###### **Yu Wang:**

   - Founder of **CyberServal** Co., Ltd.

-

- Focus on kernel architecture, device driver development, rootkit/anti-rootkit solutions to vulnerability hunting and exploitation

- • Spoken at **Black Hat** , **DEF CON** and other conferences

#BHUSA @BlackHatEvents

## Slide 4

###### Talk Roadmap

- **About Pointer Authentication (PAC)**

- **What is PAC and Current State of Apple PAC Research**

- • **How I Reverse Engineer it**

• **Two Main Challenges**

**- Apple-spec Sysreg**

**- PAC Key Protection**

- **Our Findings on Apple PAC Hardware**

• **How does Apple achieve Cross-domain Attack Mitigation**

#BHUSA @BlackHatEvents

## Slide 5

###### Let’s look at a basic memory attack

###### **A Simple Example of Pointer’s Life Cycle**

**3 Used to**

## {

**Used to Register Register Function Pointer: Function call. Pointer 1 2 Pointer Data Pointer: Memory Access. Store Load** { STR [x2], X1 ; The value in X1 register is **1** a pointer, which is stored into memory **Memory Pointer** LOAD X3, [x2] ; The pointer is then loaded **2** out from memory

BL X3; Function call **3** or LOAD X4, [X3]; Memory Access

#BHUSA @BlackHatEvents

## Slide 6

###### Let’s look at a basic memory attack **A Simple Example of Memory Corruption Attack**

Used to
Register Register Function Pointer: Function call.
Pointer A Pointer A
Data Pointer: Memory Access.
Store Load {
Memory
Pointer A
Attacker with Memory Write Primitive

#BHUSA @BlackHatEvents

## Slide 7

###### Let’s look at a basic memory attack **A Simple Example of Memory Corruption Attack**

Used to
Register Register Function Pointer: Function call.
Pointer A Pointer B
Data Pointer: Memory Access.
Hijack
Store Load {
Memory
Pointer B
Modify
Attacker with Memory Write Primitive

#BHUSA @BlackHatEvents

## Slide 8

###### **How Apple mitigates this Attack**

#BHUSA @BlackHatEvents

## Slide 9

###### What is Pointer Authentication (PAC) **Basic Usage of Pointer Authentication**

pacia x1, x5 autia x1, x5
pac instruction aut instruction
Register Register Register Register
Pointer A PAC Pointer A PAC Pointer A Pointer A
Store Load
Pointer Authentication Code
Memory
PAC Pointer A

#BHUSA @BlackHatEvents

## Slide 10

###### What is Pointer Authentication (PAC) **Basic Usage of Pointer Authentication**

pacia x1, x5
pac instruction
Register
Pointer A
Pointer Authentication Code

x1, x5

**autia**

Register Register
Pointer A PAC Pointer B
Store Load
Memory
PAC Pointer B
Modify Pointer

Register
ERR Pointer B
Error Code

aut instruction

Register
PAC Pointer A
Store

**Attacker with Memory Write Primitive**

#BHUSA @BlackHatEvents

## Slide 11

###### What is Pointer Authentication (PAC) **Basic Usage of Pointer Authentication**

pacia x1, x5
pac instruction
Register
Pointer A
Pointer Authentication Code

x1, x5

**autia**

pac instruction Register Register aut instruction
PAC Pointer A PAC Pointer B
Store Load
Memory
PAC Pointer B
Modify Pointer and PAC
Invalid PAC, Since Attacker
Attacker with Memory Write Primitive
don’t know the PAC Key

Register
ERR Pointer B
Error Code

#BHUSA @BlackHatEvents

## Slide 12

###### What is Pointer Authentication (PAC)

###### **ARMv8.3 Specification**

Five **128-bit** PAC Keys (Each Key is made up by **two 64-bit** System registers)

#BHUSA @BlackHatEvents

## Slide 13

###### What is Pointer Authentication (PAC)

###### **ARMv8.3 Specification**

Five **128-bit** PAC Keys (Each Key is made up by **two 64-bit** System registers) - APIA/IB/DA/DB for Pointer Signing (I: instruction; D: Data) - APGA for Signature Generation (G: General)

#BHUSA @BlackHatEvents

## Slide 14

###### What is Pointer Authentication (PAC)

###### **ARMv8.3 Specification**

Five **128-bit** PAC Keys (Each Key is made up by **two 64-bit** System registers) - APIA/IB/DA/DB for Pointer Signing (I: instruction; D: Data) - APGA for Signature Generation (G: General)

pacxx x1,  x2 Modifier Pointer
PAC Key Selection Pointer
P PAC PAC Pointer
APIA ComputePAC AddPAC
Signed Pointer
APIB
Key
APDA
APDB
#BHUSA

#BHUSA @BlackHatEvents

## Slide 15

###### What is Pointer Authentication (PAC)

**- Only one set of PAC Keys for Exception Level 0/1/2**

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 94/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
What is Pointer Authentication (PAC)
ARMv8.3 Specification
Five 128-bit PAC Keys (Each Key is made up by two 64-bit Sysreg)
- APIA/IB/DA/DB for Pointer Signing (I: instruction; D: Data)
- APGA for Signature Generation (G: General)
- Only one set of PAC Keys for Exception Level 0/1/2
Zechao Cai - @Zech4o #BHUSA @BlackHatEvents
```

## Slide 16

###### What is Pointer Authentication (PAC)

**One Control Register - SCTLR_EL1**

**Per-Key Switches**

**- EnIA/EnIB/EnDA/EnDB bits to enabled/disable pac instruction**

#BHUSA @BlackHatEvents

## Slide 17

###### **Apple PAC**

**Since A12 (iPhone XS, 2018)**

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 94/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Apple PAC
Since A12 (iPhone XS, 2018)
Zechao Cai - @Zech4o
Feature
Kernel
Integrity
Protection
Fast
Permission
Restrictions
System
Coprocessor
Integrity
Protection
Pointer
Authentication
Codes
Page
Protection
Layer
A13, S5
A14, A15, S6,
S7
M1 Family
See Note below.
#BHUSA @BlackHatEvents
```

## Slide 18

###### Current Research State of Apple PAC **Most of Research works focus on Software/PAC Bypass**

**Software (Kernel)**

**Examining Pointer Authentication on the iPhone XS - Brandon Azad (Google Project Zero) Attacking iPhone XS Max (Black Hat USA 2019) - Tielei Wang and Hao Xu (Team Pangu) 2PAC 2Furious: Envisioning an iOS compromise in 2019 - Macro Grassi and Liang Chen KEEN Security Lab**

**2019**

#BHUSA @BlackHatEvents

## Slide 19

###### Current Research State of Apple PAC **Most of Research works focus on Software/PAC Bypass**

Software
(Kernel)

**iOS Kernel PAC, One Year Later (Black Hat USA 2021) - Brandon Azad (Google Project Zero)**

… - Brandon Azad (Google Project Zero)
2019 2020

#BHUSA @BlackHatEvents

## Slide 20

###### Current Research State of Apple PAC **Most of Research works focus on Software/PAC Bypass**

Fugu14 (PAC Bypass)
– Linus Henze
Software
Everything has Changed in iOS 14, but
(Kernel)
Jailbreak is Eternal (Black Hat USA 2021)
… … - Zuozhi Fan (Ant Security Lab)
2019 2020 2021

#BHUSA @BlackHatEvents

## Slide 21

###### Current Research State of Apple PAC **Most of Research works focus on Software/PAC Bypass**

Software
(Kernel)
Fugu15 (PAC Bypass)
… … … – Linus Henze
2019 2020 2021 2022

#BHUSA @BlackHatEvents

## Slide 22

###### Current Research State of Apple PAC

**Brandon Azad found that Apple customized the PAC hardware. . But the implementation behind the “Dark Magic” remains unknown**

… … … …
2019 2020 2021 2022
Now
“Dark Magic”
-
Discovered by Brandon Azad Four Years
Hardware
However, the reason is unknown

#BHUSA @BlackHatEvents

## Slide 23

###### Recap of “Dark Magic”

###### **Cross-domain Attack**

Pointer Substitution Attack across different domains *ARM PAC does not provide hardware isolation

Attacker’s Domain PAC A  Pointer A
Equal
Victim’s Domain PAC A  Pointer A

Fig. Signing Pointers with same inputs (Key Type, Key Value, Pointer, Modifier) in different domains

#BHUSA @BlackHatEvents

## Slide 24

###### Recap of “Dark Magic”

###### **Cross-domain Attack**

Pointer Substitution Attack across different domains *ARM PAC does not provide hardware isolation

Attacker’s Domain PAC B  Pointer B
Replace
Victim’s Domain PAC A  Pointer A

Fig. Hijack the Control/Data flow in victim’s domain by replacing the pointer without being detected

#BHUSA @BlackHatEvents

## Slide 25

###### Recap of “Dark Magic”

###### **Cross-domain Attack**

Pointer Substitution Attack across different domains *ARM PAC does not provide hardware isolation

Attacker’s Domain PAC B  Pointer B
Replace
Victim’s Domain PAC B  Pointer B
Can also pass the authentication

Fig. Hijack the Control/Data flow in victim’s domain by replacing the pointer without being detected

#BHUSA @BlackHatEvents

## Slide 26

###### Recap of “Dark Magic”

**e.g. Cross-EL Attack** Attacker tries to generates a signed kernel pointer in user space

pacia x1,  x2
User space PAC A  Pointer A
P
Equal
pacia x1,  x2
Kernel space P PAC A  Pointer A
APIA
ARM PAC
#BHUSA

#BHUSA @BlackHatEvents

## Slide 27

###### Recap of “Dark Magic”

###### **e.g. Cross-EL Attack** Attacker tries to generates a signed kernel pointer in user space

pacia x1,  x2
User space PAC B  Pointer B
P
Replace
pacia x1,  x2
Kernel space P PAC A  Pointer A
APIA
ARM PAC
#BHUSA

#BHUSA @BlackHatEvents

## Slide 28

###### Recap of “Dark Magic”

###### **e.g. Cross-EL Attack** Attacker tries to generates a signed kernel pointer in user space

pacia x1,  x2
User space PAC B  Pointer B
P
Replace
pacia x1,  x2
Kernel space P PAC B  Pointer B
APIA
ARM PAC
#BHUSA

#BHUSA @BlackHatEvents

## Slide 29

###### Recap of “Dark Magic”

###### **e.g. Cross-EL Attack**

Attacker tries to generates a signed kernel pointer in user space Existing works mitigate cross-EL Attack by

- Maintaining different key values

- Disabling user space PAC

**User space**

**Kernel space**

PAC A  Pointer A
Equal
PAC A  Pointer A

#BHUSA @BlackHatEvents

## Slide 30

###### Recap of “Dark Magic”

###### **1. Cross-EL Attack Mitigation on Apple Silicon** There is **<u>no key switching operation</u>** in the XNU kernel

pacia x1,  x2
User space PAC A  Pointer A
P
Equal
pacia x1,  x2
Kernel space P PAC A  Pointer A
APIA
ARM PAC
#BHUSA

#BHUSA @BlackHatEvents

## Slide 31

###### Recap of “Dark Magic”

###### **1. Cross-EL Attack Mitigation on Apple Silicon** There is **<u>no key switching operation</u>** in the XNU kernel

pacia x1,  x2
User space PAC X  Pointer A
P
Different
pacia x1,  x2
Kernel space P PAC A  Pointer A
APIA
Apple PAC
#BHUSA

#BHUSA @BlackHatEvents

## Slide 32

###### Recap of “Dark Magic”

###### **2. Cross-Key Attack Mitigation on Apple Silicon** Set up **<u>different key using the same values</u>**

pacia x1,  x2
APIB PAC A  Pointer A
P
set to 0
msr  inst APIB
pacia x1,  x2
APIA
PAC A  Pointer A
P
set to 0
msr  inst APIA
ARM PAC

#BHUSA @BlackHatEvents

## Slide 33

###### Recap of “Dark Magic”

###### **2. Cross-Key Attack Mitigation on Apple Silicon** Set up **<u>different key using the same values</u>**

pacia x1,  x2
APIB PAC X  Pointer A
P
set to 0
msr  inst APIB
pacia x1,  x2
APIA
PAC A  Pointer A
P
set to 0
msr  inst APIA
Apple PAC

#BHUSA @BlackHatEvents

## Slide 34

###### Recap of “Dark Magic”

###### **3. Cross-Boot Attack Mitigation on Apple Silicon** Set up **<u>the key with the static value after each CPU boot</u>**

pacia x1,  x2
CPU Boot 1 P PAC A  Pointer A
set to 0
msr  inst APIA
pacia x1,  x2
CPU Boot 2 P PAC A  Pointer A
set to 0
msr  inst APIA
ARM PAC

#BHUSA @BlackHatEvents

## Slide 35

###### Recap of “Dark Magic”

###### **3. Cross-Boot Attack Mitigation on Apple Silicon** Set up **<u>the key with the static value after each CPU boot</u>**

pacia x1,  x2
CPU Boot 1 P PAC X  Pointer A
set to 0
msr  inst APIA
pacia x1,  x2
CPU Boot 2 P PAC A  Pointer A
set to 0
msr  inst APIA
Apple PAC

#BHUSA @BlackHatEvents

## Slide 36

###### Recap of “Dark Magic”

###### **4. Cross-VM Attack Mitigation on Apple Silicon (Apple M1)** Set up **<u>the keys with the same key values in VM and Host</u>**

pacia x1,  x2
Virtual Machine
PAC A  Pointer A
P
(EL1)
set to 0
msr  inst APIA
pacia x1,  x2
Host OS
PAC A  Pointer A
P
(EL2)
set to 0
msr  inst APIA
ARM PAC

#BHUSA @BlackHatEvents

## Slide 37

###### Recap of “Dark Magic”

###### **4. Cross-VM Attack Mitigation on Apple Silicon (Apple M1)** Set up **<u>the keys with the same key values in VM and Host</u>**

pacia x1,  x2
Virtual Machine
PAC A  Pointer A
P
(EL1)
set to 0
msr  inst APIA
pacia x1,  x2
Host OS
PAC A  Pointer A
P
(EL2)
set to 0
msr  inst APIA

Apple PAC

#BHUSA @BlackHatEvents

## Slide 38

“Dark Magic” – My Main Research Motivation **Apple implements Cross-domain Attack Mitigation . without software support How does Apple customized the PAC hardware?**

#BHUSA @BlackHatEvents

## Slide 39

###### “Dark Magic” – Our Main Research Motivation

###### **You will know how Apple implements it after this talk.**

#BHUSA @BlackHatEvents

## Slide 40

### **How I Reverse Engineer Apple PAC**

#BHUSA @BlackHatEvents

## Slide 41

#### **Basic idea**

#BHUSA @BlackHatEvents

## Slide 42

#### **Basic idea Change CPU States    and See what happens**

#BHUSA @BlackHatEvents

## Slide 43

**Basic idea Change CPU States    and See what happens**

Set System Register

**Step 1**

#BHUSA @BlackHatEvents

## Slide 44

**Basic idea Change CPU States    and See what happens**

**Set System Register Step 1**

**Run Instructions Step 2**

#BHUSA @BlackHatEvents

## Slide 45

##### **How I Reverse Engineer**

###### **Challenge 1**

- **What are the system registers we want to set?**

- **Apple introduced undocumented system registers**

Set System Register

#BHUSA @BlackHatEvents

## Slide 46

##### **How I Reverse Engineer**

###### **Challenge 1**

- **What are the system registers we want to set?**

- **Apple introduced undocumented system registers**

Set System Register

###### **Challenge 2**

Run Instructions

- **How to read the PAC key**

**- Apple introduce hardware PAC key protection**

#BHUSA @BlackHatEvents

## Slide 47

##### **How I Reverse Engineer**

###### **Task 1**

- **Identify Apple-spec PAC-related undocumented system registers**

**Set System Register**

#BHUSA @BlackHatEvents

## Slide 48

##### **How I Reverse Engineer**

###### **Task 1**

- **Identify Apple-spec PAC-related undocumented system registers**

**Task 2**

Run Instructions

Set System Register

**Bypass Apple-spec hardware PAC key protection**

#BHUSA @BlackHatEvents

## Slide 49

###### Task 1. Apple-spec PAC system register identification

#BHUSA @BlackHatEvents

## Slide 50

Task 1. Apple-spec PAC system register identification **System Register**

Registers for configuring the CPU feature Accessed by ‘msr’ (write) and ‘mrs’ (read) instructions e.g. TTBR1_EL1, Translation Table Base Register 1 (EL1)

**msr** TTBR1_EL1,  X1

#BHUSA @BlackHatEvents

## Slide 51

###### Task 1. Apple-spec PAC system register identification

**TTBR1_EL1 is a register.**

**msr** TTBR1_EL1,  X1

#BHUSA @BlackHatEvents

## Slide 52

Task 1. Apple-spec PAC system register identification

**TTBR1_EL1 is a register.**

**msr** TTBR1_EL1,  X1

#BHUSA @BlackHatEvents

## Slide 53

###### Task 1. Apple-spec PAC system register identification **TTBR1_EL1 is a register. TTBR1_EL1 is a mnemonic for Encoding (3, 0, 2, 0, 1)**

#BHUSA @BlackHatEvents

## Slide 54

###### Task 1. Apple-spec PAC system register identification

**TTBR1_EL1 is a mnemonic for Encoding (3, 0, 2, 0, 1) msr instruction use Encoding (3, 0, 2, 0, 1) to access Register**

**msr** TTBR1_EL1, X1 **Instruction**

use access **TTBR1_EL1 TTBR1 (3, 0, 2, 0, 1) Encoding Register**

#BHUSA @BlackHatEvents

## Slide 55

###### Task 1. Apple-spec PAC system register identification

**TTBR1_EL1 is a mnemonic for Encoding (3, 0, 2, 0, 1) msr instruction use Encoding (3, 0, 2, 0, 1) to access Register ! Encoding and Register are not 1:1 mapping**

**msr** TTBR1_EL1, X1 **Instruction**

use

access
TTBR1_EL1
TTBR1
(3, 0, 2, 0, 1)
Encoding Register

#BHUSA @BlackHatEvents

## Slide 56

###### Task 1. Apple-spec PAC system register identification

**Virtualization Host Extension (VHE)**

- A set of hardware supports for

- running OS on EL1 and EL2 without software modification

- Hardwired on Apple M1

- Includes **System Register Redirection**

#BHUSA @BlackHatEvents

## Slide 57

###### Task 1. Apple-spec PAC system register identification **System Register Redirection**

Instruction use Encoding access Register
TTBR1_EL1 TTBR1 EL1
EL1 msr TTBR1_EL1, X1 (3, 0, 2, 0, 1) Register
EL2

#BHUSA @BlackHatEvents

## Slide 58

###### Task 1. Apple-spec PAC system register identification **System Register Redirection**

Instruction use Encoding access Register
TTBR1_EL1 TTBR1 EL1
EL1 msr TTBR1_EL1, X1 (3, 0, 2, 0, 1) Register
EL2
TTBR1_EL2 TTBR1 EL2
msr TTBR1_EL2, X1 (3, 4, 2, 0, 1) Register

#BHUSA @BlackHatEvents

## Slide 59

###### Task 1. Apple-spec PAC system register identification **System Register Redirection**

Instruction use Encoding access Register
TTBR1_EL1 TTBR1 EL1
EL1 msr TTBR1_EL1, X1 (3, 0, 2, 0, 1) Register
EL2
msr TTBR1_EL1, X1
TTBR1_EL2 TTBR1 EL2
msr TTBR1_EL2, X1 (3, 4, 2, 0, 1) Register
#BHUSA @BlackHatEvents

## Slide 60

###### Task 1. Apple-spec PAC system register identification **System Register Redirection**

Instruction use Encoding access Register
TTBR1_EL1 TTBR1 EL1
EL1 msr TTBR1_EL1, X1 (3, 0, 2, 0, 1) Register
msr  TTBR1_EL12, X1
TTBR1_EL12
(3, 5, 2, 0, 1)
EL2
msr TTBR1_EL1, X1
TTBR1_EL2 TTBR1 EL2
msr TTBR1_EL2, X1 (3, 4, 2, 0, 1) Register
#BHUSA @BlackHatEvents

## Slide 61

###### Task 1. Apple-spec PAC system register identification **System Register Redirection**

- Bank sysreg on Both EL1 and EL2 - Redirect the Access using EL1 encoding on EL2 - Add a EL12 encoding for accessing EL1 register on EL2

* We term **EL12/EL2 encoding** as **alias encodings**

#BHUSA @BlackHatEvents

## Slide 62

###### Task 1. Apple-spec PAC system register identification **Back to Apple-spec Sysreg** Apple introduced a lot of:

**New Encodings**

to access

**New Registers**

to control **New Features**

#BHUSA @BlackHatEvents

## Slide 63

Task 1. Apple-spec PAC system register identification **Back to Apple-spec Sysreg** Apple introduced a lot of:

**New Encodings**

to access

to control **New Registers New Features**

However, Apple doesn’t disclose information about them

**Undisclosed encoding (3, 6, 15, 14, 4) The CRn field of Apple-spec Encoding is 15**

#BHUSA @BlackHatEvents

## Slide 64

###### Task 1. Apple-spec PAC system register identification

Undisclosed encoding (3, 6, 15, 14, 4)

**1. How to identify encoding/register of interest? 2. How to understand these encodings/registers?**

#BHUSA @BlackHatEvents

## Slide 65

###### Task 1. Apple-spec PAC system register identification **1. How to identify encoding/register of interest?**

Existing work. (AsahiLinux)

- https://github.com/AsahiLinux/m1n1/blob/main/tools/apple_regs.json

#BHUSA @BlackHatEvents

## Slide 66

###### Task 1. Apple-spec PAC system register identification **1. How to identify/document encoding/register of interest?** Tip 1. String Data/ Function/ Known Sysreg in Binary

- 1 _; arm64_ropjop_test_ 2 ... 3 mrs X8, #6, c15, c12, #4 _; APSTS_EL1_ 4 ... 5 and W8, W8, #1 6 adrp X24, _#_ktest_temp1@PAGE_ 7 str W8, [X24, _#_ktest_temp1@PAGEOFF]_ 8 adrl X0, aApsts1ull0 _; "apsts & (1ULL << 0)"_ 9 bl _ktest_set_current_expr _; if test fails, ,! panic will happen and the message above will_

- _,! be printed_

- 10 ...

###### XNU kernel open-source code

###### XNU kernel binary

###### The code related to Apple-spec sysreg can only be viewed in Binary

#BHUSA @BlackHatEvents

## Slide 67

###### Task 1. Apple-spec PAC system register identification **1. How to identify/document encoding/register of interest?** Tip 2. Alias encoding (EL12/EL2)

Register
Encoding
Write a Flag
APIAKeyLo EL1
EL1 APIAKeyLo_EL1
Register

#BHUSA @BlackHatEvents

## Slide 68

###### Task 1. Apple-spec PAC system register identification **1. How to identify/document encoding/register of interest?** Tip 2. Alias encoding (EL12/EL2)

Register
Encoding
Write a Flag
APIAKeyLo EL1
EL1 APIAKeyLo_EL1
Register
Value == Flag
Test all Possible
EL2
APIAKeyLo_EL12
Encodings (CRn = 15)

Not Applicable for all cases (e.g., PAC Key EL2 encoding)

#BHUSA @BlackHatEvents

## Slide 69

Task 1. Apple-spec PAC system register identification **1. How to identify/document encoding/register of interest?** Tip 3. Identify more encodings based on Alias encoding

1 ...
2 ; in the same basic block
3 ldr x8, [x20, #0x40a0]
4 msr #6, c15, c14, #4, x8 ; VMDIVLo_EL2
5 ldr x8, [x20, #0x4098]
6 msr #6, c15, c14, #5, x8 ; VMDIVHi_EL2
7 ldr x8, [x20, #0x40a8]
8 msr #6, c15, c14, #7, x8 ; APSTS_EL12
9 ...

There’s no info in Binary for VMDIVLo (3, 6, 15, 14, 4), we mark it as PAC-related based on identified alias encoding and tests

#BHUSA @BlackHatEvents

## Slide 70

Task 1. Apple-spec PAC system register identification

**2. How to understand the usage of these encoding/register?** Tip 1. Manually analysis

Some Sysregs are set up with hard-coded value

#BHUSA @BlackHatEvents

## Slide 71

Task 1. Apple-spec PAC system register identification

**2. How to understand the usage of these encoding/register?** Tip 2. Dynamic analysis – Sniff Sysregs Based on m1n1 hypervisor - https://github.com/AsahiLinux/m1n1/tree/main We implement a hypervisor-based XNU kernel debugger - Active kernel debugging

- Unlimited number of breakpoints

We plan to open-source it this year. (co-work with Jiaxun Zhu @svnswords)

#BHUSA @BlackHatEvents

## Slide 72

Task 1. Apple-spec PAC system register identification

**2. How to understand the usage of these encoding/register?** Tip 3. Run your tests on EL1 first Most Apple-spec feature are deployed on both EL1 and EL2 - Trap into EL2 to observe EL1 things with higher privilege

#BHUSA @BlackHatEvents

## Slide 73

Task 1. Apple-spec PAC system register identification **Almost all easy(general) cases are done However, there are still lots of undocumented encodings - Not used in the XNU kernel We need your help for more tests to document them**

#BHUSA @BlackHatEvents

## Slide 74

###### Task 2. Apple-spec PAC Key Protection Bypassing

#BHUSA @BlackHatEvents

## Slide 75

###### Task 2. Apple-spec PAC Key Protection Bypassing **Two PAC modes on Apple M1**

Enable
ARM PAC Mode Apple PAC Mode
Disable
(CPU Boot) (XNU kernel)

###### **Our Target: Profile the PAC instruction behavior after enabling Apple PAC Mode**

#BHUSA @BlackHatEvents

## Slide 76

###### Task 2. Apple-spec PAC Key Protection Bypassing **Apple-spec PAC Key Protection**

**ARM PAC Mode Success**

use read
APIAKeyLo_EL1
mrs X1, APIAKeyLo_EL1 (3, 0, 2, 0, 1) APIAKeyLo Register
instruction Encoding Register

#BHUSA @BlackHatEvents

## Slide 77

###### Task 2. Apple-spec PAC Key Protection Bypassing **Apple-spec PAC Key Protection**

**Apple PAC Mode Fail (Trigger an exception)**

use read
APIAKeyLo_EL1
mrs X1, APIAKeyLo_EL1 (3, 0, 2, 0, 1) APIAKeyLo Register
instruction Encoding Register

#BHUSA @BlackHatEvents

## Slide 78

Task 2. Apple-spec PAC Key Protection Bypassing **Why we need to bypass PAC Key Protection** The inputs we can control: **- Key Value (set) - Key Selection - Pointer - Modifier** **<u>x</u>** **pacx x1** , **x2 Key Access PAC Generation Process Process** **msr APKEY** Key_EL1, **x1**

**msr** Key_EL1, **x1**

#BHUSA @BlackHatEvents

## Slide 79

Task 2. Apple-spec PAC Key Protection Bypassing **Why we need to bypass PAC Key Protection**

The inputs we can control: The output we can read: **- Key Value (set) - PAC result - Key Selection - Pointer - Modifier**

**<u>x</u>** **pacx x1** , **x2**

**Key Access PAC Generation Process Process PAC** Pointer **APKEY Signed Pointer**

**msr** Key_EL1, **x1**

#BHUSA @BlackHatEvents

## Slide 80

Task 2. Apple-spec PAC Key Protection Bypassing **Why we need to bypass PAC Key Protection**

The inputs we can control: The output we can read: We can’t determine **- Key Value (set) - PAC result** “Dart Magic” is happened **- Key Selection** in which process **- Pointer - Modifier**

**<u>x</u>** **pacx x1** , **x2**

**Key Access PAC Generation Process Process APKEY Black Box**

**PAC** Pointer **Signed Pointer**

**msr** Key_EL1, **x1**

#BHUSA @BlackHatEvents

## Slide 81

###### Task 2. Apple-spec PAC Key Protection Bypassing

**Why we need to bypass PAC Key Protection**

The inputs we can control: The output we can read: **If we can read the key - Key Value (set) - PAC result - APKEY - Key Selection** We **can** determine **- Pointer** “Dart Magic” happened **- Modifier** in which process

We **can** determine “Dart Magic” happened in which process

**x1** , **x2**

**pacxx**

**Key Access PAC Generation Process Process APKEY**

**PAC** Pointer **Signed Pointer**

**msr** Key_EL1, **x1**

#BHUSA @BlackHatEvents

## Slide 82

###### Task 2. Apple-spec PAC Key Protection Bypassing **Apple-spec PAC Key Protection**

- Deployed on both EL1 and EL2 Apple PAC is different on EL1 and EL2

- EL1 Key Protection Bypass

- EL2 Key Protection Bypass

#BHUSA @BlackHatEvents

## Slide 83

###### Task 2. Apple-spec PAC Key Protection Bypassing **EL1 Key Protection Bypass**

Encoding Read Register
APIAKeyLo_EL1 APIAKeyLo EL1
EL1
(3, 0, 2, 0, 1) Register
EL2

#BHUSA @BlackHatEvents

## Slide 84

###### Task 2. Apple-spec PAC Key Protection Bypassing **EL1 Key Protection Bypass**

Encoding Read Register
APIAKeyLo_EL1 APIAKeyLo EL1
EL1
(3, 0, 2, 0, 1) Register
✓
APIAKeyLo_EL12
EL2
(3, 6,  15 , 7, 1)

#BHUSA @BlackHatEvents

## Slide 85

###### Task 2. Apple-spec PAC Key Protection Bypassing **EL2 Key Protection Bypass**

- There is no higher Exception Level (EL3) on Apple M1

**Encoding** APIAKeyLo_EL1 EL2 (3, 0, 2, 0, 1)

Read

Register
APIAKeyLo EL2
Register

#BHUSA @BlackHatEvents

## Slide 86

###### Task 2. Apple-spec PAC Key Protection Bypassing **EL2 Key Protection Bypass**

- There is no higher Exception Level (EL3) on Apple M1

Encoding Read Register
APIAKeyLo_EL1 APIAKeyLo EL2
EL2
(3, 0, 2, 0, 1) Register

**Idea 1: Are there other encodings for accessing the PAC Key?**

#BHUSA @BlackHatEvents

## Slide 87

###### Task 2. Apple-spec PAC Key Protection Bypassing **EL2 Key Protection Bypass**

- There is no higher Exception Level (EL3) on Apple M1 - EL2 PAC Key Encoding is also **Non-Readable**

**EL2**

**Encoding Read** APIAKeyLo_EL1 (3, 0, 2, 0, 1) APIAKeyLo_EL2 (3, 6, 15, 13, 0)

**Register** APIAKeyLo EL2 Register

#BHUSA @BlackHatEvents

## Slide 88

###### Task 2. Apple-spec PAC Key Protection Bypassing **EL2 Key Protection Bypass**

- There is no higher Exception Level (EL3) on Apple M1

Encoding Read Register
APIAKeyLo_EL1 APIAKeyLo EL2
(3, 0, 2, 0, 1) Register
EL2
APIAKeyLo_EL2
(3, 6, 15, 13, 0)

**Idea 2: Side-channel Attack?**

#BHUSA @BlackHatEvents

## Slide 89

# Task 2. Apple-spec PAC Key Protection Bypassing **EL2 Key Protection Bypass A Lot of Tests**

#BHUSA @BlackHatEvents

## Slide 90

###### Task 2. Apple-spec PAC Key Protection Bypassing **Observation 1**

- If Apple PAC mode is disable on EL2

- **Only one set of PAC Keys** are enabled

**EL1**

**EL2**

**Encoding Access** APIAKeyLo_EL1 (3, 0, 2, 0, 1) APIAKeyLo_EL1 (3, 0, 2, 0, 1)

**Register** APIAKeyLo EL1 Register

#BHUSA @BlackHatEvents

## Slide 91

###### Task 2. Apple-spec PAC Key Protection Bypassing **Observation 1**

- The access of EL1 Key encoding **changes after Apple PAC is enabled**

Access Register
Encoding
EL1
APIAKeyLo EL1
Register
APIAKeyLo_EL1
(3, 0, 2, 0, 1)
APIAKeyLo EL2
EL2 Register

#BHUSA @BlackHatEvents

## Slide 92

###### Task 2. Apple-spec PAC Key Protection Bypassing **Observation 2**

- Enabling Apple PAC won’t change the value in EL2 PAC Key Register

**Encoding EL1** APIAKeyLo_EL1 (3, 0, 2, 0, 1) APIAKeyLo_EL2 **EL2** (3, 6, **15** , 13, 1)

**EL1**

Access Register
APIAKeyLo EL1
Register
APIAKeyLo EL2
Register

#BHUSA @BlackHatEvents

## Slide 93

###### Task 2. Apple-spec PAC Key Protection Bypassing **Observation 3**

- **PAC calculation is based on** the key value accessed by **EL1 encoding**

**Instruction**

**pacia** x1, x2

**use**

###### **Encoding**

APIAKeyLo_EL1 (3, 0, 2, 0, 1) APIAKeyHi_EL1 (3, 0, 2, 0, 2)

**Register** APIAKeyLo EL1 **access** Register APIAKeyHi EL1 Register

#BHUSA @BlackHatEvents

## Slide 94

###### Task 2. Apple-spec PAC Key Protection Bypassing

**Why we need to bypass PAC Key Protection**

The inputs we can control: The output we can read: **If we can read the key - Key Value (set) - PAC result - APKEY - Key Selection** We **can** determine **- Pointer** “Dart Magic” happened **- Modifier** in which process

We **can** determine “Dart Magic” happened in which process

**x1** , **x2**

**pacxx**

**msr** Key_EL1, **x1**

**Key Access PAC Generation Process Process PAC** Pointer **APKEY Signed Pointer**

#BHUSA @BlackHatEvents **What we need: Determine the PAC Key value used for PAC Calculation when Apple PAC is enabled**

## Slide 95

###### Task 2. Apple-spec PAC Key Protection Bypassing **EL2 Key Protection Bypass**

**Idea: Preset the PAC Keys before Apple PAC is enabled**

#BHUSA @BlackHatEvents

## Slide 96

###### Task 2. Apple-spec PAC Key Protection Bypassing **EL2 Key Protection Bypass**

**EL1**

use APIAKeyLo_EL1
pacia x1, x2
(3, 0, 2, 0, 1)
EL2
APIAKeyLo_EL2
msr
(3, 6,  15 , 13, 1)

Register
APIAKeyLo EL1
Register
APIAKeyLo EL2
Register ( Value X )

**Step 1. Set up the EL2 PAC Key using EL2 Encoding with Value X**

#BHUSA @BlackHatEvents

## Slide 97

###### Task 2. Apple-spec PAC Key Protection Bypassing **EL2 Key Protection Bypass**

Register
EL1
APIAKeyLo EL1
Register
use APIAKeyLo_EL1
pacia x1, x2
(3, 0, 2, 0, 1)
APIAKeyLo EL2
EL2
Register ( Value X )
APIAKeyLo_EL2
msr
(3, 6,  15 , 13, 1)

**Step 2. Enable the Apple PAC, the pac inst will calculate PAC based on Value X**

#BHUSA @BlackHatEvents

## Slide 98

**Reverse Engineering Change CPU States    and See what happens**

Set System Register
Step 1

Run Instructions
Step 2

#BHUSA @BlackHatEvents

## Slide 99

### **Our Findings**

#BHUSA @BlackHatEvents

## Slide 100

###### Apple’s Customization on PAC Hardware **Finding Overview**

- Register

   - APCTL_EL1 (Apple-spec PAC Control Register)

   - EXTRAKEY_EL1 (128-bit User-Kernel Diversifier)

   - VMDIV_EL2 (128-bit Per-VM Diverisifer)

- Instruction

   - Key Access

   - pac/aut

#BHUSA @BlackHatEvents

## Slide 101

###### Apple’s Customization on PAC Hardware

###### **Key Access**

PC

Instruction (X1 = 0)

msr APIAKey Lo _EL1, X1
msr APIAKeyHi_EL1, X1

( 3  cycle)

Register

APIAKeyLo Register
( 0 )
APIAKeyHi Register

#BHUSA @BlackHatEvents

## Slide 102

###### Apple’s Customization on PAC Hardware

###### **Key Access**

Instruction (X1 = 0)

msr APIAKeyLo_EL1, X1
PC
msr APIAKey Hi _EL1, X1

Register

APIAKeyLo Register
( 0xfb0b271a781b4e27 )
( 34  cycle)
APIAKeyHi Register
( 0xf625c898230bb934 )

#BHUSA @BlackHatEvents

## Slide 103

###### Apple’s Customization on PAC Hardware

###### **Key Access**

Set up the  higher 64 bits of PAC Key  will trigger a  Key Transformation
Instruction (X1 = 0) Register
APIAKeyLo Register
msr APIAKeyLo_EL1, X1
( 0xfb0b271a781b4e27 )
( 34  cycle)
APIAKeyHi Register
PC
msr APIAKey Hi _EL1, X1 ( 0xf625c898230bb934 )

#BHUSA @BlackHatEvents

## Slide 104

###### Apple’s Customization on PAC Hardware **Key Access**

**EL1**

**Instruction (X1 = 0)**

**msr** APIAKeyLo_EL1, X1 **msr** APIAKeyHi_EL1, X1 VMDIV_EL2 ( **0** )

Register

APIAKeyLo Register
(0xfb0b271a781b4e27)
APIAKeyHi Register
(0xf625c898230bb934)

#BHUSA @BlackHatEvents

## Slide 105

###### Apple’s Customization on PAC Hardware **Key Access**

EL1

Instruction (X1 = 0) Register
APIAKeyLo Register
msr APIAKeyLo_EL1, X1 ( 0x7d7b0db350f67ff6 )
APIAKeyHi Register
( 0xf60db0dcb07eb1b1 )
msr APIAKeyHi_EL1, X1
VMDIV_EL2
( 1 )
Set up the VMDIV_EL2 with different value and trigger the EL1 Key Transformation

#BHUSA @BlackHatEvents

## Slide 106

###### Apple’s Customization on PAC Hardware **Key Access**

EL1

Instruction (X1 = 0) Register
APIAKeyLo Register
msr APIAKeyLo_EL1, X1 ( 0x7d7b0db350f67ff6 )
APIAKeyHi Register
( 0xf60db0dcb07eb1b1 )
msr APIAKeyHi_EL1, X1
VMDIV_EL2
( 1 )
VMDIV_EL2  is one of inputs for  EL1 Key Transformation

#BHUSA @BlackHatEvents

## Slide 107

###### Apple’s Customization on PAC Hardware

###### **Key Access**

Register
APIA
KeyLo
Instruction (X1 = 0) ( 0xfb0b271a781b4e27 )
KeyHi
( 0xf625c898230bb934 )
msr KeyLo_EL1, X1
msr KeyHi_EL1, X1 APIB
KeyLo
( 0x7d7b0db350f67ff6 )
VMDIV_EL2
(0) KeyHi
( 0xf60db0dcb07eb1b1 )
#BHUSA @BlackHatEvents

EL1

## Slide 108

###### Apple’s Customization on PAC Hardware **Key Access**

###### **How Apple differentiate Key Transformation for different Key?**

#BHUSA @BlackHatEvents

## Slide 109

###### Apple’s Customization on PAC Hardware **Key Access**

###### I set the VMDIV from 0b000 to 0b111

|**VMKEY**
**VMDIV**|||**Transformati**|**on Result of**|||
|---|---|---|---|---|---|---|
||**IB**|**IA**|**DB**|**DA**|**EX**|**GA**|
|0b000|0x7d7b0db350f67ff6|0xfb0b271a781b4e27|0xe2ee9eaaa4ec5479|0x3e2b1b189fbc10b4|0xb455818159de0818|0x92584a68198c0286|
||0xf60db0dcb07eb1b1|0xf625c898230bb934|0x3cd6dc8228c5488d|0xe97d268ae2681267|0x5809bcf5f3e87070|0xd8b34f463af4b03c|
|0b001|0xfb0b271a781b4e27|0x7d7b0db350f67ff6|0x3e2b1b189fbc10b4|0xe2ee9eaaa4ec5479|0x92584a68198c0286|0xb455818159de0818|
||0xf625c898230bb934|0xf60db0dcb07eb1b1|0xe97d268ae2681267|0x3cd6dc8228c5488d|0xd8b34f463af4b03c|0x5809bcf5f3e87070|
|0b010|0xe2ee9eaaa4ec5479|0x3e2b1b189fbc10b4|0x7d7b0db350f67ff6|0xfb0b271a781b4e27|0x70e4228e70a3f8ff|0x5eaaa2f0e48ef187|
||0x3cd6dc8228c5488d|0xe97d268ae2681267|0xf60db0dcb07eb1b1|0xf625c898230bb934|0x9cc19db7de935d05|0x982cdffcf13dfb43|
|0b011|0x3e2b1b189fbc10b4|0xe2ee9eaaa4ec5479|0xfb0b271a781b4e27|0x7d7b0db350f67ff6|0x5eaaa2f0e48ef187|0x70e4228e70a3f8ff|
||0xe97d268ae2681267|0x3cd6dc8228c5488d|0xf625c898230bb934|0xf60db0dcb07eb1b1|0x982cdffcf13dfb43|0x9cc19db7de935d05|
|0b100|0xb455818159de0818|0x92584a68198c0286|0x70e4228e70a3f8ff|0x5eaaa2f0e48ef187|0x7d7b0db350f67ff6|0xfb0b271a781b4e27|
||0x5809bcf5f3e87070|0xd8b34f463af4b03c|0x9cc19db7de935d05|0x982cdffcf13dfb43|0xf60db0dcb07eb1b1|0xf625c898230bb934|
|0b101|0x92584a68198c0286|0xb455818159de0818|0x5eaaa2f0e48ef187|0x70e4228e70a3f8ff|0xfb0b271a781b4e27|0x7d7b0db350f67ff6|
||0xd8b34f463af4b03c|0x5809bcf5f3e87070|0x982cdffcf13dfb43|0x9cc19db7de935d05|0xf625c898230bb934|0xf60db0dcb07eb1b1|
|0b110|0x70e4228e70a3f8ff|0x5eaaa2f0e48ef187|0xb455818159de0818|0x92584a68198c0286|0xe2ee9eaaa4ec5479|0x3e2b1b189fbc10b4|
||0x9cc19db7de935d05|0x982cdffcf13dfb43|0x5809bcf5f3e87070|0xd8b34f463af4b03c|0x3cd6dc8228c5488d|0xe97d268ae2681267|
|0b111|0x5eaaa2f0e48ef187|0x70e4228e70a3f8ff|0x92584a68198c0286|0xb455818159de0818|0x3e2b1b189fbc10b4|0xe2ee9eaaa4ec5479|
||0x982cdffcf13dfb43|0x9cc19db7de935d05|0xd8b34f463af4b03c|0x5809bcf5f3e87070|0xe97d268ae2681267|0x3cd6dc8228c5488d|

#BHUSA @BlackHatEvents

## Slide 110

###### Apple’s Customization on PAC Hardware

###### **Key Access**

###### I set the VMDIV from 0b000 to 0b111

Transformation Result of
VMKEY
VMDIV IB IA DB DA EX GA
0b000
0b001
0b010
0b011
0b100
0b101
0b110
0b111

#BHUSA @BlackHatEvents

## Slide 111

###### Apple’s Customization on PAC Hardware

###### **Key Access**

###### There are six **per-key salts** for differentiating Key Trans

Transformation Result of
VMKEY
VMDIV IB IA DB DA EX GA
0b000
0b001
0b010
0b011
0b100
0b101
0b110
0b111

||**Per**
|**-key-t**
|**ype S**
|**alt of**
||
|---|---|---|---|---|---|
|**IB**|**IA**|**DB**|**DA**|**EX**|**GA**|
|0|1|2|3|4|5|
|1|0|2|3|4|5|
|2|3|0|1|6|7|
|3|2|1|0|7|6|
|4|5|6|7|0|1|
|5|4|7|6|1|0|
|6|7|4|5|2|3|
|7|6|5|4|3|2|

Only 8 combinations of per-key salt that XOR with VMDIV will produce the same symmetry

#BHUSA @BlackHatEvents

## Slide 112

###### Apple’s Customization on PAC Hardware

###### **Key Access**

**per-key salt VMDIVLO_EL2 is one of the inputs for Key Trans**

Transformation Result of
VMKEY
VMDIV IB IA DB DA EX GA
0b000
0b001
0b010
0b011
0b100
0b101
0b110
0b111

#BHUSA @BlackHatEvents

## Slide 113

###### Apple’s Customization on PAC Hardware

###### **Key Transformation**

Inputs

- APKeyLo Register - Operator of **msr** APKeyHi_EL1, X1 - per-key salt VMDIVLO_EL2 - VMDIVHI_EL2

Output

- 128-bit PAC Key

#BHUSA @BlackHatEvents

## Slide 114

###### Apple’s Customization on PAC Hardware

###### **Key Transformation**

- Also deployed on EL2

- A **per-boot diversifier** for differentiating the Key Trans of different CPU Boots

#BHUSA @BlackHatEvents

## Slide 115

Apple’s Customization on PAC Hardware **PAC/AUT**

- A new 128-bit Key:  EXTRAKEY_EL1 (also Key Trans)
XOR with APKEY  before PAC computation
- Enabled by  APCTL_EL1
bit[1]: Kernel pacxx x1,  x2
bit[4]: User
P PAC Pointer
Signed Pointer
APKEY
Key Value
EXTRAKEY
#BHUSA @BlackHatEvents

#BHUSA @BlackHatEvents

## Slide 116

###### Apple’s Customization on PAC Hardware **PAC/AUT**

- PAC Algorithm is not QARMA

- ( **Modifier Key Value** ) is one of the inputs

x
pacx x1,  x2
Modifier Pointer
APKEY P PAC Pointer
Key Value
Signed Pointer
EXTRAKEY

#BHUSA @BlackHatEvents

## Slide 117

###### Apple’s Customization on PAC Hardware **PAC/AUT**

- A new **Per-EL switch** for PAC computation - APCTL_EL1   bit[3]: Kernel;  bit[2]: User

x
pacx x1,  x2
P ComputerPAC PAC Pointer
Signed Pointer
…
APCTL SCTLR
OR
Per-EL Swtich Per-Key Swtich

#BHUSA @BlackHatEvents

## Slide 118

###### Cross-domain Attack Mitigation

###### **Cross-EL Attack Mitigation XNU Kernel only enable EXTRAKEY on User space**

pacia x1,  x2
User space PAC X  Pointer A
P
pacia x1,  x2
Kernel space P PAC A  Pointer A
APIA EXTRAKEY

#BHUSA @BlackHatEvents

## Slide 119

###### Cross-domain Attack Mitigation

###### **Cross-VM/Boot Attack Mitigation**

pacia x1,  x2
Virtual Machine
PAC X  Pointer A
P
(EL1)
Key Trans
msr  inst APIA
VMDIV …
Host OS
PAC A  Pointer A
P
(EL2)
Key Trans
msr  inst APIA
Per-boot Diversifier

#BHUSA @BlackHatEvents

## Slide 120

###### Cross-domain Attack Mitigation

###### **Cross-Key Attack Mitigation**

pacia x1,  x2
APIA
PAC X  Pointer A
P
Key Trans
msr  inst APIA
APIA Salt …
APIB
PAC A  Pointer A
P
Key Trans
msr  inst APIB
APIB Salt

#BHUSA @BlackHatEvents

## Slide 121

###### Key Management in the XNU Kernel

###### **PAC Key Configuration**

- Global (Static Value): APIA/DA/GA - Per-Process: APIB/DB, EXTRAKEY

Key APIA APDA APGA APIB  APDB EXTRAKEY
Scope Global Global Global Per-Process Per-Process Per-Process

#BHUSA @BlackHatEvents

## Slide 122

###### Key Management in the XNU Kernel

###### **PAC Instruction Scope**

- pacia/da/ga: Global in Kernel, Per-Process in User

||**pacia**|**pacda**|**pacga**|**pacib**|**pacdb**|
|---|---|---|---|---|---|
|User (arm64e)|Per-Process|Per-Process|Per-Process|Per-Process|Per-Process|
|User (Non-arm64e)|-|-|Per-Process|Per-Process|-|
|Kernel|Global|Global|Global|Per-Process|Per-Process|

#BHUSA @BlackHatEvents

## Slide 123

###### Key Management in the XNU Kernel

###### **PAC Instruction Scope**

- pacia/da/ga: Global in Kernel, Per-Process in User - pacib/db: Per-Process

||**pacia**|**pacda**|**pacga**|**pacib**|**pacdb**|
|---|---|---|---|---|---|
|User (arm64e)|Per-Process|Per-Process|Per-Process|Per-Process|Per-Process|
|User (Non-arm64e)|-|-|Per-Process|Per-Process|-|
|Kernel|Global|Global|Global|Per-Process|Per-Process|

#BHUSA @BlackHatEvents

## Slide 124

###### Key Management in the XNU Kernel

###### **PAC Instruction Scope**

- pacia/da/ga: Global in Kernel, Per-Process in User

- pacib/db: Per-Process

- Always Enable Kernel PAC (Per-EL Switch), Disable User PAC (IA/DA/DB) for non-arm64e process by disabling Per-Key switch

||**pacia**|**pacda**|**pacga**|**pacib**|**pacdb**|
|---|---|---|---|---|---|
|User (arm64e)|Per-Process|Per-Process|Per-Process|Per-Process|Per-Process|
|User (Non-arm64e)|-|-|Per-Process|Per-Process|-|
|Kernel|Global|Global|Global|Per-Process|Per-Process|

#BHUSA @BlackHatEvents

## Slide 125

###### Still Unknown

**What’s the algorithm used for Key Transformation? Also, what’s the PAC algorithm? How Apple implements the per-boot diversifier? - Maybe we can look into (RE) iBoot/SEP.**

#BHUSA @BlackHatEvents

## Slide 126

###### Summary

**- Although there are some implementation remain unknown, the Design is clear.**

- **Apple’s PAC design looks simple, but insightful** - **For ARM CPU Vendors and ARM, Apple give a solution to improve PAC**

#BHUSA @BlackHatEvents

## Slide 127

### **One More Thing**

#BHUSA @BlackHatEvents

## Slide 128

- I did a security analysis of kernel PAC protection.

- Got a CVE-2023-32424 for kernel PAC bypass from Apple.

- Check out my USENIX Security ’23 paper

   - Demystifying Pointer Authentication on Apple M1

   - <u>https://www.usenix.org/conference/usenixsecurity23/presentation/cai-zechao</u>

#BHUSA @BlackHatEvents

## Slide 129

###### Contacts

### **Thank you**

Zechao Cai - @Zech4o zech4o@outlook.com

#BHUSA @BlackHatEvents
