---
title: "Debug7 Leveraging a Firmware Modification Attack for Remote Debugging of Siemens S7 PLCs"
speakers: ["Eyal Semel", "Ron Semel", "Alon Dankner", "Sara Bitan", "Eli Biham"]
conference: "Black Hat"
conference_full: "Black Hat ASIA 2024"
edition: "ASIA"
year: 2024
source_pdf: "BlackHat ASIA 2024-Slides/Eyal Semel & Ron Semel & Alon Dankner & Sara Bitan & Eli Biham-Debug7 Leveraging a Firmware Modification Attack for Remote Debugging of Siemens S7 PLCs.pdf"
pages: 62
sha256: "d901819750e9352f7eabc33342841317a56601eae523a7cf8e2416578862269a"
text_chars: 21846
ocr_pages: 10
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T00:49:19Z"
---
# Debug7 Leveraging a Firmware Modification Attack for Remote Debugging of Siemens S7 PLCs

**Speakers:** Eyal Semel, Ron Semel, Alon Dankner, Sara Bitan, Eli Biham  
**Conference:** Black Hat ASIA 2024  
**Source:** `BlackHat ASIA 2024-Slides/Eyal Semel & Ron Semel & Alon Dankner & Sara Bitan & Eli Biham-Debug7 Leveraging a Firmware Modification Attack for Remote Debugging of Siemens S7 PLCs.pdf` (62 pages)

## Slide 1

**Debug 7 Leveraging a Firmware Modification Attack for Remote Debugging of Siemens S7 PLCs Ron Semel | Eyal Semel**

Joint work with **Prof. Eli Biham** , **Dr. Sara Bitan** and **Alon Dankner**

Faculty of Computer Science, Technion – Israel Institute of Technology

#BHASIA @BlackHatEvents

## Slide 2

#### **Who Are We?**

##### **Ron Semel**

**Software engineer at Microsoft** Microsoft Defender for Endpoint (MDE) **Security researcher** Computer science faculty, Technion <u>https://www.linkedin.com/in/ronsemel/</u>

##### **Eyal Semel**

**Security researcher** Computer science faculty, Technion <u>https://www.linkedin.com/in/eyalsemel/</u>

# BHASIA @BlackHatEvents

## Slide 3

#### **Talk Topics**

- Introduction and Previous Research

- Runtime Manipulation of Siemens S7 PLCs Firmware

- Implementation of Debug 7 - a Remote Debugger for Siemens S7 PLCs

- Debugger Video Demo

- Conclusions

# BHASIA @BlackHatEvents

## Slide 4

#### **The 4**<sup>**th**</sup> **Industrial Revolution – Industry 4.0**

- Can anyone imagine life without:

Drinking water

Transportation

Food

Amazon

- Our necessities are made accessible via automated industrial control systems.

Wastewater treatment plants purify water.

Complex signaling systems manage traffic.

Food is grown using automatic irrigation systems.

Automated warehouses manage our online purchases # BHASIA @BlackHatEvents

## Slide 5

#### **The 4**<sup>**th**</sup> **Industrial Revolution – Industry 4.0**

- These smart control systems include:

   - Mass integration of IOT devices.

   - Extensive cloud communication.

   - Smart automation

All these cool new features come with risks…

# BHASIA @BlackHatEvents

## Slide 6

#### **Attacks on Critical Infrastructure**

- Cyber attacks on critical infrastructure can be catastrophic!

https://www.technologyreview.com/2019/03/05/103328/cybersecurity-critical-infrastructure-triton-malware/

- We have a great responsibility securing these systems!

# BHASIA @BlackHatEvents

## Slide 7

#### **PLC – Programmable Logic Controller**

PLCs are rugged computers used for industrial automation. • They are the core component of an ICS. They read input data from field devices such as sensors.

- Outputs are triggered based on pre-programmed code.

A bridge between the virtual world and the physical world.

# BHASIA @BlackHatEvents

## Slide 8

#### **Everybody Loves Ice Cream**

# BHASIA @BlackHatEvents

## Slide 9

#### **Industrial Control System Example**

###### **The PLC collects data from the industrial pot:**

- **Temperature**

- **Etc.**

**Based on the sensor input, the PLC commands the tubs:**

- **Start**

- **Stop**

- **Etc.**

**The statuses of the tubs can be viewed in the engineering workstation.**

**The custom control logic can be updated remotely, via the engineering workstation.**

###### Ice Cream Factory

0°
2°
1°

# BHASIA @BlackHatEvents

## Slide 10

#### **Previous Research**

Abbasi et al.

Biham et al.

Team82 at Claroty

Colin Finck and Tom Dohrmann

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Q
blackhat Previous Research
ASIA 2024
pidekhat :
A Decade After Stuxnet:
How Siemens S7 is Still an
Attacker’'s Heaven
Colin Finck and Tom Dohrmann
Ali Abbasi, Tobias Scharnowski, Thorsten Holz
Abbasi et al. Team82 at Claroty Colin Finck and Tom Dohrmann
```

## Slide 11

#### **The Siemens ET 200SP PLC Open Controller**

- PLCs are the main target of attacks on critical infrastructure.

   - We focused on the largest PLC vendor – Siemens.

   - More specifically the **Siemens ET 200SP PLC Open Controller** .

   - One of the leading PLCs in the market.

   - It runs on standard hardware - an Intel Atom CPU with 4 cores.

- It includes a software PLC – the **S7-1500 Software Controller** :

   - It’s a software application that simulates the functionality of a hardware PLC.

   - From now on we will call this software PLC – _SWCPU_ .

# BHASIA @BlackHatEvents

## Slide 12

#### **Top Secret**

For years, Siemens kept the firmware of their S7 PLC’s a secret!

They invested a lot of resources in IP protection:

- The S7-1200 PLC self-destructs if a watchdog discovers a core was halted via the JTAG interface.

   - Thomas Weber, Hack In The Box, 2019

   - Ali Abbasi, CS3STHLM, 2020

- The SWCPU is encrypted on the open controller.

   - Soft7, Biham et al., 2022

# BHASIA @BlackHatEvents

## Slide 13

#### **A Revolution in Siemens’ S7 PLC Research**

- For the first time S7 PLC history:

   - We remove from the Siemens’ S7 PLCs from their many layers of obscurity.

   - We expose a powerful remote tool to dynamically analyze their firmware.

   - We can easily expose secrets kept hidden for years.

- As a byproduct, we installed persistent malware on it.

   - Which communicates with a malicious command and control server (C2), to enable convenient communication with the installed implant.

# BHASIA @BlackHatEvents

## Slide 14

#### **The PLC’s Architecture**

Inter OS communication

Communicates with the:

Communicates with the **field devices**

- **Engineering workstation**

• Cloud platform

SWCPU
Bare-metal hypervisor

**The isolation by virtualization,** between the two guest OSs is an important **layer of security.** Even if the Windows OS is compromised, the field devices should remain safe.

Soft7, Eli Biham et al., 2022

# BHASIA @BlackHatEvents

## Slide 15

#### **Boot Process**

VMM 1 st
BIOS
Stage
VMM 2 nd
Stage
GRUB
Windows Embedded
Bootloader
Encrypted SWCPU
Decryptor
SWCPU

Soft7, Eli Biham et al., 2022

# BHASIA @BlackHatEvents

## Slide 16

#### **Previous Research**

- Our research continues where Soft 7 ended.

   - Black Hat USA 22’, Soft7, Biham et al.

- Remember that the hypervisor decrypts the SWCPU and loads it into memory?

   - The Soft7 team, extracted the plaintext SWCPU firmware file.

   - We could finally start studying the SWCPU’s assembly code!

VMM 2 nd Stage
Windows Embedded
Encrypted SWCPU
Decryptor
SWCPU

# BHASIA @BlackHatEvents

## Slide 17

#### **Previous Research**

- Surprisingly, the HV and SWCPU firmware files may be accessed via the Windows OS.

   - _C:\Boot\Siemens\SWCPU\_

- By simply dragging and dropping, we can replace the firmware files.

The OSs aren’t that isolated…

# BHASIA @BlackHatEvents

## Slide 18

#### **Previous Research**

###### **If we zoom in, we will see the:**

- They leveraged this capability to crash debug the HV:

   - Override an instruction in the HV with an “int 3” command.

   - Replace the original HV with the modified version using the “drag and drop” method we showed earlier.

   - Once the “int 3” command executes, a crash dump will be produced (a hidden feature).

**The PLC**

**The crash dump**

- **Registers and stack**

- **The return address on the stack**

# BHASIA @BlackHatEvents

## Slide 19

#### **A Quick Recap**

- Soft7 enabled us to:

   - Study the SWCPU’s assembly code.

   - Modify the hypervisor via the Windows filesystem

   - Crash debug the hypervisor.

- Going forward, we’ll present our contributions!

# BHASIA @BlackHatEvents

## Slide 20

#### **What Will We Show You?**

•

- How a bad actor could:

   - Use remote exploitation to stealthily install persistent malware on the SWCPU.

   - Establish communication between the malware and a remote C2 server.

   - Dynamically inject commands into the SWCPU.

   - Exfiltrate data from the SWCPU.

C2 SWCPU
SWCPU
Bare-metal hypervisor

# BHASIA @BlackHatEvents

## Slide 21

#### **What Will We Show You?**

•

- If you’re a researcher, you will learn how to:

   - Read data from the SWCPU during runtime.

   - Get a better understanding of the code flow.

   - Expedite your research process exponentially.

SWCPU
Bare-metal hypervisor

# BHASIA @BlackHatEvents

## Slide 22

#### **The Heist**

- Our research process was like robbing a bank.

- Let me introduce you to the game “Bank Heist”

   - We’ll be playing this game throughout the talk.

# BHASIA @BlackHatEvents

## Slide 23

#### **Talk Topics**

- Introduction and Previous Research

- Runtime Manipulation of Siemens S7 PLCs Firmware

- Implementation of Debug 7 - a Remote Debugger for Siemens S7 PLCs

- Debugger Video Demo

- Conclusions

# BHASIA @BlackHatEvents

## Slide 24

#### **Level 1 – Gather Intel (Research the firmware)**

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
a
blackhat Level 1 — Gather Intel (Re:
Gnacan
[e SCORE:0 +]
Sr eer Semen rey ey ree Ty ee
‘a a
```

## Slide 25

#### **A Bump in the Road**

- Remember that the Soft7 team was able to modify the HV and run it?

- Similarly, we wanted to run our modified version of the SWCPU, but:

   - The SWCPU on the PLC is encrypted.

   - The Soft7 team didn’t discover the decryption method or key.

   - After modifying the plaintext SWCPU, we couldn’t encrypt it to match the hypervisor’s decryptor.

   - Replacing the original SWCPU with a decrypted one should just make it crash…

SWCPU
SWCPU
Bare-metal hypervisorHypervisor

# BHASIA @BlackHatEvents

## Slide 26

#### **The Hypervisor Vulnerability We Found**

- We started by reversing the code that loads the SWCPU.

   - The hypervisor can load any ELF file as the SWCPU!!

   - Looks like a backdoor…

**This “if” clause enables any ELF file to be loaded**

**This “if” clause loads the encrypted SWCPU file. It begins with the “S3^\x9F” magic string.**

# BHASIA @BlackHatEvents

## Slide 27

#### **The Vulnerability – A Visual Explanation**

**An admin on the Windows OS can replace the SWCPU with a malicious version, using the “drag and drop” method.**

**Upon PLC restart, the hypervisor loads the malicious SWCPU without checking for authenticity.**

Admin

SWCPU

This undermines a significant advantage of virtualization – isolation. Can be done remotely:

• If an attacker gains remote admin access to the Windows OS. Changes withstand a reboot.

SWCPU
Bare-metal hypervisor

Sidenote: we owned our PLC so obviously we had an admin user

# BHASIA @BlackHatEvents

## Slide 28

#### **Level 1 – Gather Intel (Research the firmware)**

# BHASIA @BlackHatEvents

## Slide 29

#### **Exploiting the Vulnerability**

- Now we can modify the SWCPU to our liking!!

   - Should we make it mine bitcoin?

   - Instead, let’s modify it to help us understand its internal logic better.

- To understand the SWPCU better we needed to extract basic runtime info:

   - Registers

   - Stack

- But how can we do it?

SWCPU
SWCPU
Bare-metal hypervisor

# BHASIA @BlackHatEvents

## Slide 30

#### **The Naïve Approach**

- Remember that by injecting an ‘int3’ command into the hypervisor code we can generate a crash dump?

- If we do the same to the SWCPU, will it also generate a crash dump?

   - Thus, we will see the SWCPU’s registers and stack.

FAIL

# BHASIA @BlackHatEvents

## Slide 31

#### **Improving the Naïve Approach**

- The hypervisor launches the SWCPU.

   - During runtime control is shifted back and forth.

- What does an “int 3” command do when it executes in the SWCPU?

   - We thought it generates a crash dump.

int 3
SWCPU
int 3

int 3
Bare-metal hypervisor

   - We discovered that it shifts control back to the hypervisor!!

- Can we leak data from the SWCPU to the hypervisor’s crash dump?

# BHASIA @BlackHatEvents

## Slide 32

#### **A Visual Explanation**

**While running within the SWCPU, shift control back to the HV using an “int 3” command.**

**After the context switch, the registers will remain the same, since it’s a baremetal HV.**

**We found a way to leak SWCPU information to the hypervisor’s crash dump, via the registers.**

**The registers in the hypervisor crash dump will be identical to the SWCPU’s registers.**

**Crash the hypervisor by using another “int 3” command.**

SWCPU
int 3
int 3
Bare-metal hypervisor

# BHASIA @BlackHatEvents

## Slide 33

#### **The Code We Injected**

- What function is called here?!

###### **SWCPU code**

- We injected this code:

      - DEADBEEF is a magic number that tells the HV to crash.

      - “int 3” shifts control back to the hypervisor.

   - After “int 3” is run in the SWCPU, we end up here.

•

We injected this code:

• We injected this code: • Check if %edx == DEADBEEF. • If so, crash the hypervisor using an “int 3”. • We discovered %rax in the crash dump.

SWCPU
Bare-metal hypervisor
Hypervisor code
# BHASIA @BlackHatEvents

## Slide 34

#### **Results**

- This was a breakthrough! We managed to leak SWCPU runtime information

   - This worked only in some parts of the code.

- We decided to find the point of failure:

   - Using binary search, we attempted to crash the SWCPU until we found the point of failure.

SWCPU Code

# BHASIA @BlackHatEvents

## Slide 35

#### **Let’s Improve Even More**

- What is the IDT?

   - A kernel struct, pointed to by the IDTR register.

   - Each entry in the IDT points to a different interrupt handler

   - When “int 3” executes, the handler shifts control back to the hypervisor.

   - If modified, the handler won’t shift control back to the hypervisor.

255
…
IDTR
SWCPU
3
“int 3” handler
2
Bare-metal hypervisor
1
0

# BHASIA @BlackHatEvents

## Slide 36

#### **Let’s Improve Even More**

- We bypassed the issue by using the “ _vmcall_ ” instruction instead of “ _int 3”_ .

   - “ _vmcall_ ” shifts control to the hypervisor without going through the IDT.

###### **Our breakpoint looked like this**

###### **Now it looks like this**

# BHASIA @BlackHatEvents

## Slide 37

#### **Level 1 – Gather Intel (Research the firmware)**

# BHASIA @BlackHatEvents

## Slide 38

#### **A Quick Recap**

- The original SWCPU file can be easily replaced with any ELF file.

   - Using the “drag and drop” method

- By modifying the SWCPU and the hypervisor, we were able to extract runtime information from the SWCPU.

- This expedited the next part of our research!

Our Research
SWCPU
SWCPU
Bare-metal hypervisor

# BHASIA @BlackHatEvents

## Slide 39

#### **So How Did This Help Us**

- The SWCPU’s system call table is obfuscated.

   - Using static analysis, we found it and mapped several functions.

- After locating the “open” system call:

   - We copied the filename to the registers.

- For example:

   - r8-r11 contain “ _/winac_rdnvs/retain_aslog”_ in ASCII.

# BHASIA @BlackHatEvents

## Slide 40

#### **The System Call Table**

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Q
blackhat The System Call Table
ASIA 2024
sub_10
sub_10
kernel close
kernel ioctl
sub_10C189D@
sub_10C18C5@
sub_10
kernel_open
kernel _read
kernel_write
sub_1@C1A326
sub_10C1A330
sub_1@C1A3E@
```

## Slide 41

#### **It Was a Pretty Tough Time**

## **We studied crash dumps for months!!**

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
blackhat_ lt Was
ASIA 20,
SIEMENS SIMATIC RT-Y
a sab cs coo ctoeseNe | be “Sepia pains =e M Seansio2 oieewosi se SIEMENS
oy | Usceontvedscond tome. : 7 q SIEMENS 3.102.092 008F oes = SIEMENS SIMATIC RI
|| soma soo cao Fana:eenm ooo iuonoa22ae00 | 0 i pediscr eater SANT pr woo ee
coc - ; Sauna : eee rteonocceony || i ‘ Saeneee
SIEMENS miei = —— Ent rigs i ona Sa arom) shoe msn
si i ay ti coco aeooaniia =r : a | | moms aac sane norcnnng ase cr a TN
Hen Sieectanstares ae eat t ne sais Erectile sec scree eas) ied coats ie totes cro
a ia ce i ioe zi ae Ae | |apoaocs We irene, ine sseeloenasdai® SIEMENS, ea) 8 ie pc00000778 oc
ied crash dum E
ease
2 ae bap) aioe Bassin: Pea Ul Sitters eee
SWIRL Rnaaelioneess-_ssaesooo0n000 H 00 & 5 [a : =
ea a sam Sore son 3 i ress000 : wu Sen Sree onsh | Eaas}000 st sag
Serena | Boreas | Sac ae Pe  Suiowme ie | ee g ||
eitstonates | Soom IAAL.) ete Se ee
```

## Slide 42

#### **Talk Topics**

- Introduction and Previous Research

- Runtime Manipulation of Siemens S7 PLCs Firmware

- Implementation of Debug 7 - a Remote Debugger for Siemens S7 PLCs

- Debugger Video Demo

- Conclusions

# BHASIA @BlackHatEvents

## Slide 43

#### **Implementation of Debug7**

- To build the remote debugger we needed to:

   - Inject debugger commands into the SWCPU.

   - Exfiltrate data from the SWCPU to the debugger.

- Effectively, we needed C2 capabilities.

Debugger command
Remote
SWCPU
Debugger
Debugger response
Bare-metal hypervisor

# BHASIA @BlackHatEvents

## Slide 44

#### **Level 2 – Breach the Vault (Inject Data)**

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
a
blackhat Level 2 — Breach the Vault.
ASIA 2024
(iva: 25)
[e SCORE: 2 +]
Sr eer Semen rey ey ree Ty ee
‘a a
```

## Slide 45

#### **Its OK to be Lazy**

- We are very lazy!!!

   - Developing a C2 server is hard 

- What if we told you that a C2 platform already exists?

   - Its already installed for us on the PLC.

   - It can save us weeks of development time.

   - It also has a nice GUI.

- Let me introduce you to the PLC’s web server.

# BHASIA @BlackHatEvents

## Slide 46

#### **Can we Inject Data via the Web Server?**

- The PLC exposes a web server via the SWCPU.

   - For example, a technician can connect to it via his cell phone during maintenance.

- Can we inject data into the SWCPU via the URL?

SWCPU
SWCPU
Bare-metal hypervisor

# BHASIA @BlackHatEvents

## Slide 47

#### **Can we Inject data via the Web Server?**

**Request a non-existing page from the web server**

**The SWCPU attempts to open the file**

**Hook the “open” syscall**

**If the filename starts with “dbg7” save it to the memory.**

**Otherwise, continue the normal “open” flow**

HTTP Client

###### **SWCPU**

http://localhost:81/ **dbg7_hello**

**Hook Code open_hook: if (filename starts with dbg7) {**

**save filename in memory } else {**

###### **Memory**

“open”

SWCPU

Bare-metal hypervisor

**resume normal “open” flow }**

# BHASIA @BlackHatEvents

## Slide 48

#### **Level 2 – Breach the Vault (Inject Data)**

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
a
blackhat Level 2 — Breach the Vault
ASIA 2024
Level COME leted
[e SCORE: 3¢]
```

## Slide 49

#### **Level 3 – Escape (Exfiltrate Data)**

# BHASIA @BlackHatEvents

## Slide 50

#### **Can We Extract data via the Web Server?**

The read hook  The web
injects the  server now
HTTP Client
saved string into  displays our
the css page data

The SWCPU
attempts to read a
css page from
memory

**Request the home page from the web server**

**Hook the “read” system call**

http://localhost:81/Portal/Intro.mwsl
“read”
SWCPU
Bare-metal hypervisor

SWCPU
Hook Code Memory
read_hook:
dbg7_hello
if (filename == “MiniWeb.css”)
{
return data from memory
}
else
{
resume normal “read” flow
}

# BHASIA @BlackHatEvents

## Slide 51

#### **Results**

- We exfiltrated data using the “MiniWeb.css” file.

   - After refreshing the home page, our data appeared on the web page.

# BHASIA @BlackHatEvents

## Slide 52

#### **Level 3 – Escape (Exfiltrate Data)**

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
a
blackhat Level 3 — Escape (Exfiltrate
ASIA 2024
Level Completed
[+ SCORE: 3 ¢]
4
```

## Slide 53

#### **Boss – Build the Debugger**

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
a
blackhat Boss — Build the Debugger
ASIA 2024
(eve: 39)
[e SCORE: 4 +]
eee Se ye eee Pre ey eee =A
carr fpnsesaafianeasp irc terns finns tif tor end haar ens lca kaze tase
```

## Slide 54

#### **How to Modify the SWCPU Firmware File**

- We needed to add code to the SWCPU without interrupting its normal flow.

###### **The SWCPU firmware file**

Our added section
Loads as RWE

**Loads as RWE**

- We added a whole new section to the decrypted SWCPU file.

Malicious Section

# BHASIA @BlackHatEvents

## Slide 55

#### **The Debugger Architecture**

.hooks (our added section)
The debug cmd HTTP Client
Command Parser Memory
http://localhost:81/ dbg7_R_ Portal/Intro.mwsl 190C2B8D
Prefix Type Params TEST_STRING
SWCPU
Bare-metal hypervisor
Breakpoint  Write  Read
Handler Handler Handler

# BHASIA @BlackHatEvents

## Slide 56

#### **A Video Demonstration of Debug7**

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
blackhat A Video Demonstration of Debug7
@ http://localhost:81/Portal/Int P~ GS) Sintro @ newtab a
SIEMENS mall simatic-controller service&support
English |
ENTERP
SIMATIC
$7-1500 Software Controller
CPU 1505SP
& Skip Intro
peveemmm Network (> Performance Memory Emulation Garu Bl
= i |G) 5 & Y~ Content type Find (Ctrl+F)
Name / Result Initiator 7 & - Headers Body Parameters Cookies Timings
Path Protocol Method Description Content type Received Time Type LS e
Response body — Request body
Intro.mwsl HTTP GET 200 text/html 352.84ms document in
http://localhost:81/Portal/ OK This resource has no response payload data
MiniWeb.css HTTP GET 200 text/css 11.76 KB 170.22 ms fink
http:/localhost:81/CSS/ OK
S7Web.css HTTP GET 200 text/css 32.67 KB 255.13 ms link |
http://localhost:81/CSS, OK
Siemens _Firmenmarke.gif HTTP GET 200 image/gif 667B 149.21 ms_— image
http://localhost:81/Im: OK
CPU1505SP.jpg HTTP GET 200 image/jpeg 128.35 KB 121s image
http://localhost:81/cpu/intro/ OK
intro_enter_arrow.gif HTTP GET 200 image/gif 850B 328.73 ms image
http://localhost:81/Im: OK
< >
174.27 KB transferred 2.47 s taken (DOMContentLoaded: 828 ms, load: 2.06 s)
0 errors 6 requests
```

## Slide 57

#### **Boss – Build the Debugger**

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
a
blackhat Boss — Build the Debugger
ASIA 2024
(eve: 39)
[e SCORE: 4 +]
—>
eee Se ye eee Pre ey eee =A
fpr eases ntcndf terns fone ttf reread bec tf anna Lassa zea ae
```

## Slide 58

#### **Mitigations**

- Common security mitigations:

   - ASLR

   - .text section should not be writeable.

- The hypervisor should be an iron wall between guest OSs.

   - Siemens gave us an elegant backdoor to modify the SWCPU via the Windows OS.

   - This feature must be removed!

- Secure boot chain!!!

   - This is the only way to really protect the PLC from firmware modification attacks.

# BHASIA @BlackHatEvents

## Slide 59

#### **Research Impact**

Our novel debugger is the only known method to dynamically analyze the SWCPU.

- Researchers can now thoroughly research the SWCPU firmware.

- The code is shared between all of Siemens’ Simatic S7 product line. • All the Siemens’ S7 PLCs are now much more vulnerable.

# BHASIA @BlackHatEvents

## Slide 60

#### **Security Impact**

We showed you how a **persistent** trojan horse could be developed for one of the leading PLCs in the market:

- The malware is persistent and can withstand a reboot.

- It can’t be easily detected.

- We know for a fact that bad actors are looking for these capabilities, for example the Triton attack.

- The longer the industry fails to properly secure PLCs, the greater the risk.

   - Patching the existing PLCs in the wild is almost impossible.

# BHASIA @BlackHatEvents

## Slide 61

# **How Safe Do You Really Feel?!**

### **Demand Secure Products**

# BHASIA @BlackHatEvents

## Slide 62

#### **Contact**

Please feel free to contact us for any questions: <u>thesemelbros@gmail.com</u>

<u>sarab@cycloak.com</u>

<u>dankner@cs.technion.ac.il</u>

<u>biham@cs.technion.ac.il</u>

# BHASIA @BlackHatEvents
