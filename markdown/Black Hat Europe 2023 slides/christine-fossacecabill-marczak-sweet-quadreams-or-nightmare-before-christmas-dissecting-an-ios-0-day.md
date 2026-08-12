---
title: "Sweet QuaDreams or Nightmare Before Christmas Dissecting an iOS 0-Day"
speakers: ["Christine Fossaceca", "Bill Marczak"]
conference: "Black Hat"
conference_full: "Black Hat Europe 2023"
edition: "Europe"
year: 2023
source_pdf: "Black Hat Europe 2023 slides/Christine Fossaceca,Bill Marczak_Sweet QuaDreams or Nightmare Before Christmas Dissecting an iOS 0-Day.pdf"
pages: 90
sha256: "ab8d7d71ca2362a2db6f9d14148e94d1e4360808c30ad420e1883483e0733c6f"
text_chars: 18915
ocr_pages: 17
has_ocr: true
redacted_secrets: 0
ocr_confidence: 87.7
ocr_unreliable_blocks: 0
vision_verified_blocks: 2
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T04:02:39Z"
---
# Sweet QuaDreams or Nightmare Before Christmas Dissecting an iOS 0-Day

**Speakers:** Christine Fossaceca, Bill Marczak  
**Conference:** Black Hat Europe 2023  
**Source:** `Black Hat Europe 2023 slides/Christine Fossaceca,Bill Marczak_Sweet QuaDreams or Nightmare Before Christmas Dissecting an iOS 0-Day.pdf` (90 pages)


## Slide 1

# **Sweet QuaDreams or Nightmare before Christmas? Dissecting an iOS 0-Day Attack**

**Bill Marczak,** **_The Citizen Lab_ Christine Fossaceca,** **_Microsoft_**

#BHEU @BlackHatEvents

## Slide 2

### **Notes:**

- We’re talking about an attack from 2021

- • We’re not dropping CVEs on stage!

- • Have shared technical details with Apple

## Slide 3

## **About Christine**

\```
@x71n3
\```


> Recovered by OCR — confidence 81/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
About Christine
ee
/home/christine $ c
tr Th PODCAST
A @x71n3
```

## Slide 4

**About Bill**

## Slide 5

**About Bill**


> Recovered by OCR — confidence 96/100 on the text kept, 96/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
About Bill
HIDE AND SEEK
Tracking NSO Group’s Pegasus Spyware to
Operations in 45 Countries
Running in Circles
Uncovering the Clients of Cyberespionage Firm
Circles
PREDATOR IN THE WIRES
Ahmed Eltantawy Targeted with Predator Spyware
After Announcing Presidential Ambitions
Hooking Candiru
Another Mercenary Spyware Vendor Comes into
Focus
```

## Slide 6

**iPhone Initial Access**

## Slide 7

### **iPhone Initial Access**

CVE-Whatever: Perpetual Safari/WebKit Exploit


> Recovered by OCR — confidence 87/100 on the text kept, 65/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
iPhone Initial Access
eee etisalat = 2:41PM
Messages (6) InfoSMS
sms.webadv.co/
9573305s/
CVE-Whatever: Perpetual
Safari/WebkKit Exploit
```

## Slide 8

### **iPhone Initial Access**

CVE-Whatever: Perpetual Safari/WebKit Exploit

Target: Ahmed Mansoor UAE Human Rights Activist


> Recovered by OCR — confidence 89/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
iPhone Initial Access
eee etisalat = 2:41PM
Messages (6) InfoSMS
sms.webadv.co/
9573305s/
CVE-Whatever: Perpetual Target: Ahmed Mansoor
Safari/WebkKit Exploit UAE Human Rights Activist
```

## Slide 9

**iPhone Initial Access** **<u>with Zero Clicks</u>**

## Slide 10

### **iPhone Initial Access with Zero Clicks**

**CVE-2021-30860: Integer overflow in CoreGraphics**


> Recovered by OCR — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
iPhone Initial Access with Zero Clicks
...NOW, IT TURNS OUT
THIS IS ACTUALLY
TURING-COMPLETE...
)
THIS PHRASE EITHER MEANS
SOMEONE SPENT SIX MONTHS
GETTING A DISHWASHER TO
PLAY MARIO OR YOU'RE UNDER
ATTACK BY A NATION-STATE.
CVE-2021-30860: Integer
overflow in CoreGraphics
```

## Slide 11

### **iPhone Initial Access with Zero Clicks**

**CVE-2023-41064: Buffer overflow in ImageIO**

**CVE-2021-30860: Integer overflow in CoreGraphics**

## Slide 12

### **iPhone Initial Access with Zero Clicks**

**CVE-2023-41064: Buffer overflow in ImageIO**

**CVE-2023-41990: Issue in FontParser**

**CVE-2021-30860: Integer overflow in CoreGraphics**

## Slide 13

### **Our Definitions**

**0-day (** **_ze·ro·day):_** an exploited vulnerability for which there is no patch available **0-click (** **_ze·ro·click):_** a remote vulnerability that requires no user interaction (or “clicks”)

## Slide 14

### **Our Definitions**

**0-day (** **_ze·ro·day):_** an <u>exploited vulnerability for</u> which there is no patch available **0-click (** **_ze·ro·click):_** a remote vulnerability that requires no user interaction (or “clicks”)

## Slide 15

### **Our Definitions**

**0-day (** **_ze·ro·day):_** an exploited vulnerability for which there is no patch available **0-click (** **_ze·ro·click):_** a <u>remote vulnerability that</u> requires no user interaction (or “clicks”)

## Slide 16

### **Our Definitions**

**0-day (** **_ze·ro·day):_** an exploited vulnerability for which there is no patch available **0-click (** **_ze·ro·click):_** a <u>remote vulnerability that</u> requires no user interaction (or “clicks”)

## Slide 17

**Apple Sandboxes IMTranscoderAgent with BlastDoor**

## Slide 18

#### **Apple Sandboxes IMTranscoderAgent with BlastDoor**

**Neener neener!**

## Slide 19

### **BlastDoor: A Fork in the Road**

**<u>Attack/Circumvent BlastDoor</u>**

**<u>Find a Different Attack Surface</u>**

## Slide 20

### **BlastDoor: A Fork in the Road**

**<u>Attack/Circumvent BlastDoor</u>**

##### **<u>Find a Different Attack Surface</u>**

## Slide 21

### **BlastDoor: A Fork in the Road**

**<u>Attack/Circumvent BlastDoor</u>**

**<u>Find a Different Attack Surface</u>**

## Slide 22

Discovery of the Attack & Samples

Static & Dynamic Reversing of the Sample

Attribution: Sometimes it's Easy!

A Theory of the Exploit

## Slide 23

Discovery of the Attack & Samples

## Slide 24

**Log Analysis**

## Slide 25

### **Log Analysis**

**Top-down: Analyze a spyware sample, understand what forensic traces it leaves behind, then look for these in the phone's logs.**

## Slide 26

### **Log Analysis**

**Top-down: Analyze a spyware sample, understand what forensic traces it leaves behind, then look for these in the phone's logs.**

**Bottom-up: Look for** **_implausible artifacts_ in the phone's logs, and then try to attribute them.** **_Can detect unknown spyware this way!_**

## Slide 27

### **Examples of "Implausible Artifacts"**

• **Evidence that a non-iOS-update binary ran from:** **`/private/var/db/com.apple.xpc.roleaccountd.staging/`**

• **Evidence that any binary ran from** **`/tmp`**

• **Evidence that a binary consumed mobile data that is "not supposed to" (e.g.,** **`BackupAgent` )**

## Slide 28

### **An implausible artifact ITW...**

**Get yer' phones checked here!!!**

## Slide 29

### **An implausible artifact ITW...**

**Get yer' phones checked here!!!**

**Several phones showed a binary had run:** **`/private/var/db/com.apple.xpc.roleaccountd.staging/subridged` Phones negative for Pegasus!!!**

## Slide 30

### **...meanwhile at Microsoft**

**Microsoft Threat Intelligence is constantly tracking ITW threats**

## Slide 31

### **...meanwhile at Microsoft**

**Microsoft Threat Intelligence is constantly tracking ITW threats**


> Recovered by OCR — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
...meanwhile at Microsoft
Microsoft Threat Intelligence is constantly tracking ITW threats
Blizzard Sleet Typhoon
Russia North Korea China
Sandstorm Storm Tempest
Iran Groups in development Financially motivated
Tsunami Flood
Private sector offensive actor Influence operations
```

## Slide 32

### **...meanwhile at Microsoft**

**Microsoft Threat Intelligence is constantly tracking ITW threats**

**Microsoft had found a sample with this hard-coded path:** **`/private/var/db/com.apple.xpc.roleaccountd.staging/subridged`**

## Slide 33

**Yo Citizen Lab, we have a sample matching your IOCs...**

Tell us more...

## Slide 34

Discovery of the Attack & Attribution: Sometimes Samples it's Easy!

## Slide 35

**Carmine Tsunami**

## Slide 36

### **Carmine Tsunami**

**Private Sector Offensive Actor (PSOA)**

- **A company that sells hacking tools**

- • **Often exclusively to governments**

## Slide 37

### **Carmine Tsunami**

**Private Sector Offensive Actor (PSOA)**

- **A company that sells hacking tools**

• **Often exclusively to governments**

**In this case, QuaDream!**

## Slide 38

**The Mercenary Spyware Industry**


> Recovered by OCR — confidence 87/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
The Mercenary Spyware Industry
nso GROUP
}
CYBER - INTELLI GENCE - SOLUTIONS
```

## Slide 39

**The Industry in the News**


> Recovered by OCR — confidence 96/100 on the text kept, 96/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
The Industry in the News
Pegasus phone spyware used to target
30 Thai activists, cyber watchdogs say
Pegasus spyware used in ‘jaw-dropping’
phone hacks on El Salvador journalists
Israeli spyware used
‘extensively’ on separatists in
Spain, group says
Mexico: reporters and activists hacked
with NSO spyware despite assurances
More Polish opposition figures found to
have been targeted by Pegasus spyware
```

## Slide 40

**The Industry in the News**


> Recovered by OCR — confidence 96/100 on the text kept, 96/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
The Industry in the News
Dubai ruler hacked ex-wife using NSO
Pegasus spyware, high court judge finds
Sheikh Mohammed used spyware on Princess Haya and five
associates in unlawful abuse of power, judge rules
‘The walls are closing in on me’: the hacking of Princess Haya
Ruling in Princess Haya case raises fresh questions for Cherie
Blair
```

## Slide 41

## Slide 42

Victim Locations
Europe
Central Asia
North America
Southeast Asia
Middle East

## Slide 43

Discovery of the Attack & Samples

Static & Dynamic Reversing of the Sample

Attribution: Sometimes it's Easy!

## Slide 44

## **iOS System Protections**

**Protection Mechanism Bypassed?** ASLR and NX Sandboxing Entitlements Codesigning + AMFI PAC PPL

## Slide 45

## **iOS System Protections**

**Protection Mechanism Bypassed?** ASLR and NX Sandboxing Entitlements Codesigning + AMFI PAC PPL

## Slide 46

## **iOS System Protections**

**Protection Mechanism Bypassed?** ASLR and NX Sandboxing Entitlements Codesigning + AMFI PAC PPL

## Slide 47

## **iOS System Protections**

**Protection Mechanism Bypassed?** ASLR and NX Sandboxing Entitlements Codesigning + AMFI PAC PPL

## Slide 48

## **Sample Capabilities**

• **Device Info**

   - **Wi-Fi**

   - **Airplane Mode**

   - **Carrier Info**

   - **iOS version**

- **Spying**

   - **Records audio**

   - **Takes pictures**

   - **Tracks location**

## Slide 49

## **Sample Capabilities**

• **Exfiltrates and deletes keychain items**

- **Exfiltrates and deletes other files on disk**

- **NO persistence mechanism!**

## Slide 50

## **iOS Secure Boot Chain**

###### **Apple WWDC 2016**


> Recovered by OCR — confidence 95/100 on the text kept, 72/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
iOS Secure Boot Chain
Apple Public Key
Low-Level
Bootloader Kernel
Apple WWDC 2016
```

## Slide 51

## **Examples of iOS “persistence”**

• **Zecops Blog: “NoReboot”. Hook shutdown mechanism to "fake" a reboot** **_(theoretical attack – not ITW)_**

## Slide 52

## **Examples of iOS “persistence”**

• **Zecops Blog: “NoReboot”. Hook shutdown mechanism to "fake" a reboot** **_(theoretical attack – not ITW)_**

- **Re-infect on reboot examples:**

• **Pegasus in 2016: rtbuddyd –-early-boot. Replace** **_rtbuddyd_ w/** **_JSC_ , put JS exploit in file called "** **_--early-boot_ "**

• **Predator in 2021: iOS shortcut automations**

## Slide 53

## **Examples of iOS “persistence”**

• **Zecops Blog: “NoReboot”. Hook shutdown mechanism to "fake" a reboot** **_(theoretical attack – not ITW)_**

• **Re-infect on reboot examples:**

• **Pegasus in 2016: rtbuddyd –-early-boot. Replace** **_rtbuddyd_ w/** **_JSC_ , put JS exploit in file called "** **_--early-boot_ "**

• **Predator in 2021: iOS shortcut automations**

## Slide 54

## **Subverting iCloud 2FA**

- **_/usr/libexec/adid_ (Anisette) process is responsible**

- **This is “hard” to reverse (FairPlay DRM)**

- **So, they treat it like a black box!**

- **Dylib injection to inject code into** **_adid,_ then function hooking to generate codes**

- **How does this work?**

## Slide 55

## **Dylib Injection**

\```
//lib injection code (thanks newosxbook.com)
//grab the task port for the target pid
task_t remoteTask;
task_for_pid(mach_task_self(), pid, &remoteTask);
//allocate memory
mach_vm_allocate( remoteTask, &remoteMem64, MEM_SIZE, VM_FLAGS_ANYWHERE);
//write shellcode into memory
mach_vm_write(remoteTask, remoteMem64, ptr_to_shellcode,len);
//make memory executable
vm_protect(remoteTask, remoteMem64, SIZE, FALSE,VM_PROT_READ|VM_PROT_EXECUTE);
\```

## Slide 56

## **Dylib Injection**

**`//lib injection code (thanks newosxbook.com) //grab the task port for the target pid`** **Find pid of adid** **`task_t remoteTask; task_for_pid(mach_task_self(), pid, &remoteTask); //allocate memory mach_vm_allocate( remoteTask, &remoteMem64, MEM_SIZE, VM_FLAGS_ANYWHERE); //write shellcode into memory mach_vm_write(remoteTask, remoteMem64, ptr_to_shellcode,len); //make memory executable vm_protect(remoteTask, remoteMem64, SIZE, FALSE,VM_PROT_READ|VM_PROT_EXECUTE);`**

## Slide 57

## **Dylib Injection**

**`//lib injection code (thanks newosxbook.com) //grab the task port for the target pid task_t remoteTask; task_for_pid(mach_task_self(), pid, &remoteTask);`** **allocate memory** **`//allocate memory mach_vm_allocate( remoteTask, &remoteMem64, MEM_SIZE, VM_FLAGS_ANYWHERE); //write shellcode into memory mach_vm_write(remoteTask, remoteMem64, ptr_to_shellcode,len); //make memory executable vm_protect(remoteTask, remoteMem64, SIZE, FALSE,VM_PROT_READ|VM_PROT_EXECUTE);`**

## Slide 58

## **Dylib Injection**

\```
//lib injection code (thanks newosxbook.com)
//grab the task port for the target pid
task_t remoteTask;
task_for_pid(mach_task_self(), pid, &remoteTask);
//allocate memory
\```

**`mach_vm_allocate( remoteTask, &remoteMem64, MEM_SIZE, VM_FLAGS_ANYWHERE);`** **write shellcode** **`//write shellcode into memory mach_vm_write(remoteTask, remoteMem64, ptr_to_shellcode,len); //make memory executable vm_protect(remoteTask, remoteMem64, SIZE, FALSE,VM_PROT_READ|VM_PROT_EXECUTE);`**

## Slide 59

## **Dylib Injection**

\```
//lib injection code (thanks newosxbook.com)
//grab the task port for the target pid
task_t remoteTask;
task_for_pid(mach_task_self(), pid, &remoteTask);
//allocate memory
\```

**`mach_vm_allocate( remoteTask, &remoteMem64, MEM_SIZE, VM_FLAGS_ANYWHERE); //write shellcode into memory mach_vm_write(remoteTask, remoteMem64, ptr_to_shellcode,len);`** **make executable** **`//make memory executable vm_protect(remoteTask, remoteMem64, SIZE, FALSE,VM_PROT_READ|VM_PROT_EXECUTE);`**

## Slide 60

## **Dylib Injection**

\```
//lib injection code continued
//shellcode contains dlopen pointer callback
uint64_t addrOfDlopen = (uint64_t) dlopen;
//dylib is on disk
*path_to_dylib = “/path/to/mydylib”
\```

\```
//when remote thread executes
\```

\```
callBackFunction(*addrOfDlopen, *path_to_dylib)
\```

## Slide 61

## **Dylib Injection**

**Shellcode sets up a stack frame for a call to DLOPEN**

\```
//lib injection code continued
//shellcode contains dlopen pointer callback
uint64_t addrOfDlopen = (uint64_t) dlopen;
//dylib is on disk
*path_to_dylib = “/path/to/mydylib”
\```

\```
//when remote thread executes
\```

\```
callBackFunction(*addrOfDlopen, *path_to_dylib)
\```

## Slide 62

## **Dylib Injection**

**`//lib injection code continued //shellcode contains dlopen pointer callback uint64_t addrOfDlopen = (uint64_t) dlopen; //dylib is on disk` Target binary loads dylib in its own** **`*path_to_dylib = “/path/to/mydylib”` context, arbitrary code execution achieved**

\```
//when remote thread executes
callBackFunction(*addrOfDlopen, *path_to_dylib)
\```

## Slide 63

## **Subverting iCloud 2FA**

- **Codes are TOTP (i.e., solely determined by secret key material & wall-clock time)**

- • **Hooks** **_gettimeofday_ to "fool"** **_adid_ about the current time**

- **Can generate 2FA codes valid for arbitrary future times!!!**

• **Plug & chug a ton of times into the injected** **_adid ..._ profit!!**

## Slide 64

**Complex Predicate Language**

## Slide 65

## **Complex Predicate Language**

- **VPN Connected (T/F)**

- • **Proxy (T/F)**

- • **Third-party Jailbreak (T/F)**

- • **Device Attached (T/F)**

- • **Battery Charging (T/F)**

- • **Screen Locked (T/F)**

- • **Battery Percentage (int)**

- • **Battery Temp. Range (float)**

- • **CPU Utilization (float)**

- • **Located in Country (list)**

## Slide 66

## **Complex Predicate Language**

   - **Connectivity (Mobile Data/WiFi)**

- **VPN Connected (T/F)**

- • **Proxy (T/F)**

- • **Third-party Jailbreak (T/F)**

- • **Device Attached (T/F)**

- • **Battery Charging (T/F)**

- • **Screen Locked (T/F)**

- • **Battery Percentage (int)**

- • **Battery Temp. Range (float)**

- • **CPU Utilization (float)**

- • **Located in Country (list)**

- **Data Uploaded in Duration Exceeds Threshold**

- **Traveled to New Country**

- **Location within radius of coordinates**

- **Threatening process**

- **AND/OR/NOT/PIPE**

## Slide 67

### **Cleanup C&C Command...**

• **Step 1: Open Calendar.sqlitedb**

- **Step 2: Run queries, where %s is supplied by C&C:**

\```
DELETE FROM CalendarItemChanges WHERE record IN (SELECT
owner_id FROM ParticipantChanges WHERE email = "%s");
DELETE FROM ParticipantChanges WHERE email = "%s";
DELETE FROM Identity WHERE ROWID IN (SELECT DISTINCT
identity_id FROM Participant WHERE email = "%s");
\```

• **Step 3: Vacuum the DB**

## Slide 68

## Slide 69

Discovery of the Attack & Samples

Static & Dynamic Reversing of the Sample

Attribution: Sometimes it's Easy!

A Theory of the Exploit

## Slide 70


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 74/100 on the text kept, 58/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
The bottleneck of traditional TLV-format fuzzing
Classic Fuzzing

[left Wireshark packet — Frame 817]
Frame 817: 29 bytes on wire (232 bits), 29 bytes captured (232 bits) on interface bluetooth0, id 0
Bluetooth
Bluetooth HCI H4
Bluetooth HCI ACL Packet
Bluetooth L2CAP Protocol
    Length: 20
    CID: L2CAP Signaling Channel (0x0001)
    Command: Configure Request
        Command Code: Configure Request (0x04)
        Command Identifier: 0x01
        Command Length: 16
        Destination CID: Dynamically Allocated Channel (0x0045)
        0000 0000 0000 000. = Reserved: 0x0000
        .... .... .... ...0 = Continuation Flag: False
        Option: MTU
            Type: Maximum Transmission Unit (0x01)
            Length: 2
            MTU: 0
        Option: MTU
            Type: Maximum Transmission Unit (0x01)
            Length: 2
            MTU: 0
        Option: MTU
            Type: Maximum Transmission Unit (0x01)
            Length: 2
            MTU: 0

[middle Wireshark packet — Frame 2500]
Frame 2500: 45 bytes on wire (360 bits), 45 bytes captured (360 bits) on interface bluetooth0, id 0
Bluetooth
Bluetooth HCI H4
Bluetooth HCI ACL Packet
Bluetooth L2CAP Protocol
    Length: 36
    CID: L2CAP Signaling Channel (0x0001)
    Command: Command Reject
    Command: Unknown command
        Command Code: Unknown (0x00)
        Command Identifier: 0x00
        Command Length: 0
        Unknown Command Code
            [Expert Info (Warning/Protocol): Unknown Command Code]

[hex dump]
02 02 00 1b 01 17 01 5d  00 03 2f 05 23 01 01 41   .......] ../.#.A
41 41 41 41 41 41 41 41  41 41 41 41 41 41 41 41   AAAAAAAA AAAAAAAA
(remaining rows all 41 41 ... = AAAAAAAA AAAAAAAA)

[right graphic] cartoon of a confused person at a monitor reading "USELESS FUZZ"
Documents
A/V Remote Control Profile 1.6.2
Bluetooth
SPECIFICATIONS AND DOCUMENTS
Core Specification 5.4
```

## Slide 71

**Event added >6 months after it ended – backdated!**


> Recovered by OCR — confidence 80/100 on the text kept, 64/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
BEGIN: VCALENDAR
PRODID:-//caldav.icloud.com//CALDAVJ 2116B554//EN
BEGIN: VEVENT
DTEND; TZID=Europe/London: 202009 i:
DTSTAMP : 202103
LOCATION: Home Event added >6 months
SUMMARY :Meeting after it ended — backdated!
CREATED: 20210.
ATTENDEE ; CN={; CUTYPE=INDIVIDUAL; PARTSTAT=ACCEPTED; ROLE=CHAIR;
principal/
DESCRIPTION] ]>:x
ATTENDEE<![CDATAL:Notes
```

## Slide 72

**Event added >6 months after it ended – backdated!**

**Closing and opening "CDATA" tags!!!!!!!!!**


> Recovered by OCR — confidence 79/100 on the text kept, 61/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
BEGIN: VCALENDAR
PRODID:-//caldav.icloud.com//CALDAVJ 2116B554//EN
BEGIN: VEVENT
DTEND; TZID=Europe/London: 202009 i:
DTSTAMP : 202103
LOCATION: Home Event added >6 months
SUMMARY :Meeting after it ended — backdated!
CREATED: 20210.
ATTENDEE ; CN={; CUTYPE=INDIVIDUAL; PARTSTAT=ACCEPTED; ROLE=CHAIR;
principal/
ATTENDEE<! [CDATAL | Mtert@S
```

## Slide 73

### **CDATA who???**

\```
<?xml version="1.0" encoding="utf-8"?>
[...]
 <d:calendar-data><![CDATA[
 BEGIN:VCALENDAR
 [...]
 DESCRIPTION]]>:
<lmao>parsed by the phone as XML</lmao>
 ATTENDEE<![CDATA[:Notes
]]></d:calendar-data>
 [...]
\```

## Slide 74

**Hold up, does this really work?**

## Slide 75

### **Hold up, does this really work?**

- **Yes. Parsed by NSXMLParser (libxml2 SAX mode)**

## Slide 76

### **Hold up, does this really work?**

- **Yes. Parsed by NSXMLParser (libxml2 SAX mode)**

- **Hook the SAX callback when an element is found:**

\```
-[CoreDAVXMLElementGenerator
parser:didStartElement:namespaceURI:qualifiedName:attributes:]
\```

## Slide 77

**Phone's iCalendar Parser Only Saw CDATA!** `<?xml version="1.0" encoding="utf-8"?> [...] <d:calendar-data>` `<![CDATA[` `BEGIN:VCALENDAR [...] DESCRIPTION` `]]>` `:x` `<foo>escaped CDATA here!</foo>` `ATTENDE` `E<![CDATA[` `:Notes` `]]>` `</d:calendar-data> [...]`

## Slide 78

**Can We Test Against a Server?**

## Slide 79

**Can We Test Against a Server?**


> Recovered by OCR — confidence 87/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Can We Test Against a Server?
—_ ccs-calendarserver
<> Code ©) Issues 47 3% Pull
The Calendar and Contacts Server.
@ www.calendarserver.org
```

## Slide 80

### **Can We Test Against a Server?**

• **Server rejects** **]]> and** **<![CDATA[ in values (right of the ":") but accepts them in keys (left of the ":")**

## Slide 81

### **Can We Test Against a Server?**

- **Server rejects** **]]> and** **<![CDATA[ in values (right of the ":") but accepts them in keys (left of the ":")**

- **Attacker can "update" to remove any XML escape**

   - `DESCRIPTION]]>: <lmao>XML</lmao>`

   - • `DESCRIPTION]]>: x`

## Slide 82

**Oh yeah, updated once!**


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 77/100 on the text kept, 64/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Disrupting the state machine to discover new Bluetooth vulnerabilities

AVRCP

[flowchart]
Start AVRCP Browsing Setup
SDP Query: Verify Browsing Capability

Protocol Stack Dependencies
  A2DP Audio Streaming
    AVDTP - Audio/Video Distribution Transport Protocol
  AVRCP Control Commands
    AVCTP - Audio/Video Control Transport Protocol
    CMD

Technical Points
  AVDTP (L2CAP-based):
  - Audio transport
  - Codec negotiation
  - Media packetization

  AVCTP (L2CAP-based):
  - Control framing
  - Transaction management
  - Browse multiplexing

Browsing Channel Established

Channel Maintenance
  Monitor AVDTP Channel Health
  Browsing Channel Inactive?
  Yes -> Terminate Browsing Channel
  NO -> Periodic AVCTP Keep-alives

[Wireshark packet list; Source and Destination columns are pixelated: [obscured]]
      Time        Source        Destination     Protocol   Length   Info
242 7.793242   [obscured]   [obscured]   AVRCP   39   Sent Vendor dependent: Status - GetElementAttributes - 0x0000000000000000 (PLA[clipped at pane edge]
243 7.798830   [obscured]   [obscured]   AVRCP   27   Sent Vendor dependent: Status - SetPlayerApplicationSettingValue
246 7.802118   [obscured]   [obscured]   AVRCP   39   Sent Vendor dependent: Status - GetElementAttributes - 0x0000000000000000 (PLA[clipped at pane edge]
247 7.805518   [obscured]   [obscured]   AVRCP   39   Sent Vendor dependent: Status - GetElementAttributes - 0x0000000000000000 (PLA[clipped at pane edge]
249 7.806513   [obscured]   [obscured]   AVRCP   52   Rcvd Vendor dependent: Stable - GetElementAttributes - Title: "Not Provided"
250 7.807872   [obscured]   [obscured]   AVRCP   22   Rcvd Vendor dependent: Accepted - SetPlayerApplicationSettingValue
254 7.816469   [obscured]   [obscured]   AVRCP   52   Rcvd Vendor dependent: Stable - GetElementAttributes - Title: "Not Provided"
256 7.820247   [obscured]   [obscured]   AVRCP   52   Rcvd Vendor dependent: Stable - GetElementAttributes - Title: "Not Provided"

[packet detail pane]
Encapsulation type: Bluetooth H4 with linux header (99)
Arrival Time: Mar 28, 2025 20:56:52.625[obscured]1000 中国标准时间
UTC Arrival Time: Mar 28, 2025 1[obscured]:56:52.625061000 UTC
Epoch Arrival Time: 1743[obscured]66612.625061000
[Time shift for this packet: 0.000000000 seconds]
[Time delta from previous captured frame: 0.003400000 seconds]
[Time delta from previous displayed frame: 0.003400000 seconds]
[Time since reference or first frame: 7.805518000 seconds]
Frame Number: 247
Frame Length: 39 bytes (312 bits)
Capture Length: 39 bytes (312 bits)
[Frame is marked: False]
[Frame is ignored: False]
Point-to-Point Direction: Sent (0)
[Protocols in frame: bluetooth:hci_h4:bthci_acl:btl2cap:btavctp:btavrcp]
> Bluetooth
> Bluetooth HCI H4
> Bluetooth HCI ACL Packet
> Bluetooth L2CAP Protocol
v Bluetooth AVCTP Protocol
     0001 .... = Transaction: 0x1
     .... 00.. = Packet Type: Single (0x0)
     .... ..0. = C/R: Command (0x0)
     .... ...0 = IPID: Profile OK (0x0)
     Profile Identifier: A/V Remote Control (0x110e)

[hex pane]
0000   02 01 00 22 00 1e 00 51   00 10 11 0e 01 48 00 00   ···"···Q ·····H··
0010   19 58 20 00 00 11 00 00   00 00 00 00 00 00 02 00   ·X ····· ········
0020   00 00 01 00 00 00 07                                ·······

> Trigger resource exhaustion by flooding GetPlayStatus commands just before channel timeout

> Exploit timing vulnerability: Overload the protocol stack by spamming short commands at the critical timeout threshold.

> Denial-of-Service (DoS) risk: High-frequency requests near session expiry can crash or degrade system performance.
```

## Slide 83

## Slide 84

**Conclusions**

## Slide 85

### **Conclusions**

**Collaboration and information sharing is important: include civil society too!**

society too!

## Slide 86

### **Conclusions**

**Cloud services as new vector, beyond the classics.**

## Slide 87

### **Conclusions**

##### **Build the wall broader, not just taller in one place.**

## Slide 88

### **Conclusions**

##### **Features like Lockdown Mode are great, but optional.**


> Recovered by OCR — confidence 95/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Conclusions
Features like Lockdown Mode are great, but optional.
9:41
< Back Lockdown Mode
Lockdown Mode
Lockdown Mode is an extreme, optional
protection that should only be used if you
believe you may be personally targeted by a
highly sophisticated cyberattack. Most people
are never targeted by attacks of this nature.
```

## Slide 89

### **Questions?**

### **bill@citizenlab.ca cfossaceca@microsoft.com**


> Recovered by OCR — confidence 86/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Questions?
bill@citizenlab.ca
cfossaceca@microsoft.com
THECITIZENLAB wm Microsoft
```

## Slide 90

# **Black Hat Sound Bytes**

- **Key Takeaway 1: Be careful with software dev; did you introduce a new feature or a new bug?**

- **Key Takeaway 2: Keep your devices up to date!**

- **Key Takeaway 3: Consider additional protections like Defender, Lockdown Mode, etc.**

#BHEU @BlackHatEvents
