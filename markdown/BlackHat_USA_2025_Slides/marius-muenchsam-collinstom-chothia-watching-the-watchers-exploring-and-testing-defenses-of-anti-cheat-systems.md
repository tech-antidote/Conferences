---
title: "Watching the Watchers Exploring and Testing Defenses of Anti-Cheat Systems"
speakers: ["Marius Muench", "Sam Collins", "Tom Chothia"]
conference: "Black Hat"
conference_full: "Black Hat USA 2025"
edition: "USA"
year: 2025
source_pdf: "BlackHat_USA_2025_Slides/Marius Muench&Sam Collins&Tom Chothia_Watching the Watchers Exploring and Testing Defenses of Anti-Cheat Systems.pdf"
pages: 89
sha256: "7371de1caa977ea0eea734e0a59b3b207b1d09eb5df9d89bd3be5f991346faff"
text_chars: 31415
ocr_pages: 14
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T22:58:06Z"
---
# Watching the Watchers Exploring and Testing Defenses of Anti-Cheat Systems

**Speakers:** Marius Muench, Sam Collins, Tom Chothia  
**Conference:** Black Hat USA 2025  
**Source:** `BlackHat_USA_2025_Slides/Marius Muench&Sam Collins&Tom Chothia_Watching the Watchers Exploring and Testing Defenses of Anti-Cheat Systems.pdf` (89 pages)


## Slide 1

## Watching the Watchers Exploring and Testing Defenses of Anti-Cheat Systems

Sam Collins, Marius Muench, Tom Chothia

#BHUSA @BlackHatEvents

## Slide 2

###### This talk

This talk is about **anti-cheats as software defenses.**

In this context:

- Cheats & Cheaters act as attackers

- Anti-Cheats & games act as defenders

###### **Do expect …**

- Cool software defenses

- Windows kernel internals

- To learn why a computer is almost never as secure as when playing Fortnite

###### **Do not expect …**

- Comparisons of anti-cheats to spyware

- Bypasses of anti-cheat systems

- Development tips for cheats

#BHUSA @BlackHatEvents

## Slide 3

###### Talk Roadmap

**Part I: Cheats & Anti-Cheats**

- Introduction

- The world of game cheats

- Experiences with investigating anticheats

**Part II: A Treasure Chest of Defenses**

- Mitigating BYOVD

- Windows kernel hardening

- Software diversification

- Detecting rogue hardware

- Hiding memory

**Part III: Insights & Takeaways**

- Impacts of anti-cheats

- • The next battleground

- • Takeaways

#BHUSA @BlackHatEvents

## Slide 4

###### Talk Roadmap

###### **Part I: Cheats & Anti-Cheats**

- Introduction

- The world of game cheats

- Experiences with investigating anticheats

###### **Part II: A Treasure Chest of Defenses**

- Mitigating BYOVD

- Windows kernel hardening

- Software diversification

- Detecting rogue hardware

- Hiding memory

**Part III: Insights & Takeaways**

- Impacts of anti-cheats

- • The next battleground

- • Takeaways

#BHUSA @BlackHatEvents

## Slide 5

###### Who Are We?

##### Sam

- PhD Student @ UoB,

- Man At The End Attacks & Reverse Engineering

- Game Dev but all my games are impossible to beat without cheating

Marius

- Assistant Prof @ UoB

- Baseband hacking, Reverse Engineering, & Low-Level Security

- Hacked the RP2350

Tom

- Professor @ UoB

- Taught game hacking to his students for the last 5 years

- Hacked Apple Pay, Visa, Square, Bank of America, pacemakers, e-passports.

#BHUSA @BlackHatEvents

## Slide 6

###### Setting the Scene

us

Image by Gary Jamroz

The scene - A harsh planet, on which continual combat leads to the evolution of super soldiers/monsters.

#BHUSA @BlackHatEvents

## Slide 7

###### Why Anti-Cheats?

Full-Stack Defence Software, Hardware, Firmware, Networking

Protection vs Mysterious Hands on Privilege: Arcane Tricks Testing: Kernel, Invisible memory Playing Video Hypervisor, and & underhanded Games at Work Beyond windows hooking :P

#BHUSA @BlackHatEvents

## Slide 8

###### Selected Titles

**18.6 Million** (Monthly Players) ~ **$3.1 Billion** (Lifetime Revenue)

**Free**

**~6-8 Million** (Monthly Players)

- ~ **$3.8 Billion**

- (Lifetime Revenue)

**Free**

- **110 Million**

- (Monthly Players) ~ **$26 Billion**

- (Lifetime Revenue)

**Free**

**18 Million** (Monthly Players)

- ~ **$3.4 Billion**

- (Lifetime Revenue)

**Free**

**~24 Million** (Monthly Players)

~ **$6.7 Billion** (Lifetime Revenue)

**Free**

#BHUSA @BlackHatEvents

## Slide 9

###### What Cheats Do

###### ESP

###### Aimbot

###### Extra-Sensory-Perception

- Lets you see things you shouldn’t

- Requires access to the game memory

- Shown in an app or overlay

- Does the shooting for you

- Requires access to the game memory

- Executed by artificial mouse clicks

#BHUSA @BlackHatEvents

## Slide 10

Prior Art

**And of course a lot of cheat forums :)**

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Prior Art
Un veilin g th e #HITB2023AMS https://conference.hitb.org,
underground world of 2024) d Exploiting Online Games
ANTI-CHEATS AMS for
a : CASH ¥-
blatkhat Son berar #
paral sec Bypassing Anti-Cheats &
EUROPE 2m19 Hacking Competitive Games
DECEMBER , 2019
©xXCEL LONDON, UK
iSECpartners®
()
blackhat
auoust 7s ao Next Level Cheating and
SRIECINGS ‘ but Twentyyye PPOMMORPG Hackibg: Better Graphics,
Leveling Up Mitigations etal “i
Modern Anti-Abuse Mechanisms in Nicolas Guigo Joel St. John f Pree.
Competitive Video Games
Manfred (@_EBFE), 400Ib hacker in training
s<tedacted>@securityevaluators.com
S KEE
Julien Voisin — dustri.org
And of course a lot of cheat forums :)
```

## Slide 11

###### Talk Roadmap

**Part I: Cheats & Anti-Cheats**

- Introduction

- The world of game cheats

- Experiences with investigating anticheats

**Part II: A Treasure Chest of Defenses**

- Mitigating BYOVD

- Windows kernel hardening

- Software diversification

- Detecting rogue hardware

- Hiding memory

**Part III: Insights & Takeaways**

- Impacts of anti-cheats

- • The next battleground

- • Takeaways

#BHUSA @BlackHatEvents

## Slide 12

###### A Huge Market for Game Cheats

We monitored **80 cheat selling sites** over **six months** , and make a market dataset avilable.

In most countries, game cheats are not illegal, but sites have been sued for copyright infringement.

Cheats sold on a **subscription model** , e.g., one month access.

Well run sites, with user reviews and credit card payment.

#BHUSA @BlackHatEvents

## Slide 13

###### A Huge Market for Game Cheats

At any time, roughly **174,000 people** using cheats from these sites

Prices from **$12 to $220** dollars a month.

Based on standard e-market conversion rates top sites making **~$5,000,000 a year** .

You can make more money with a game cheat than from a bug bounty or from malware!

|**Site**|**Avg. mo.**
**Traffic**|**Avg. mo.**
**Cheat**
**Price**|**Min.**
**Price**|**Max.**
**Price**|
|---|---|---|---|---|
|Engine
Owning|509,720|$13.80|$10.89|$19.59|
|Sky
Cheats|197,463|$92.43|$35.00|$130.00|
|Battle Log|194,463|$72.84|$19.90|$145.75|
|Kernaim|189,338|$41.13|$16.50|$60.00|
|Lavi
Cheats|153,429|$71.08|$29.00|$109.00|
|Interwebz
Cheats|144,838|$21.79|$21.79|$21.79|
|Aimware|135,784|$19.16|$17.24|$22.99|
|Ring-1|115,353|$54.00|$29.00|$99.00|
|Phantom
Overlay|87,528|$32.546|$19.96|$43.24|

#BHUSA @BlackHatEvents

## Slide 14

###### Market Observations

###### **Days**

● Cheat Working | — Cheat Not Working | · Cheat not Available#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Market Observations
Battle Log - vader
Battie Log - fury
Battle Log - quantum
Lavi Cheats - Yamatos
Lavi Cheats - Coffee
Lavi Cheats - Grave
Lavi Cheats - Hyperion
Sky Cheats - Division
Sky Cheats - Omega
Sky Cheats - Zero
Sky Cheats - Valkyrie
Sky Cheats - Tenet
Private Cheatz - Hyperion
Private Cheatz - Droid
Private Cheatz - Intel
Lavi Cheats - Sky
Lavi Cheats - Pro
y
VALORDNT
® Cheat Working | — Cheat Not Working
- Cheat not Available
```

## Slide 15

###### User Level Anti-Cheat

Cheat Windows API AntiUser Mode GameCheat Windows Subsystems Cheat Kernel Mode Windows Kernel Drivers Code signed by MS Hardware Abstraction Layer

#BHUSA @BlackHatEvents

## Slide 16

User Level Anti-Cheat

Cheat
Windows API
Anti-
User Mode GameCheat Windows Subsystems
Cheat
Kernel Mode
Anti-
CheatWindows Kernel Drivers
Code signed by MS
Cheat
Hardware Abstraction Layer

#BHUSA @BlackHatEvents

## Slide 17

###### Kernel Level Anti-Cheat

Cheat
Windows API
Anti-
User Mode Game Windows Subsystems
Cheat
Kernel Mode
Anti-
Windows Kernel Drivers
Code signed by MS
Cheat
Hardware Abstraction Layer

#BHUSA @BlackHatEvents

## Slide 18

###### Kernel Level Anti-Cheat

Cheat
Windows API
Anti-
User Mode Game Windows Subsystems
Cheat
Kernel Mode
Anti-
Windows Kernel Drivers
Code signed by MS
Cheat
Hardware Abstraction Layer

#BHUSA @BlackHatEvents

## Slide 19

###### Talk Roadmap

**Part I: Cheats & Anti-Cheats**

- Introduction

- The world of game cheats

- Experiences with investigating anticheats

**Part II: A Treasure Chest of Defenses**

- Mitigating BYOVD

- Windows kernel hardening

- Software diversification

- Detecting rogue hardware

- Hiding memory

**Part III: Insights & Takeaways**

- Impacts of anti-cheats

- • The next battleground

- • Takeaways

#BHUSA @BlackHatEvents

## Slide 20

###### Cheat Forums – The Good, Bad, and Ugly

Cheat forums are the best and the worst source of information about game hacking and anti-cheats – this talk would not have been possible without this impressive community

Game
Guides
Offsets
Whatever
this is

#BHUSA @BlackHatEvents

## Slide 21

Investigated Anti-Cheats in a Nutshell:
Prodding the Bear

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
BRIEFINGS
2a8660 eeBeeees eeGEe802 BBERGEGee BEeEGeee— : nt! KeBugCheckEx
184b19 eeeeeeeR eeGeEeF4d FFFF9d42° eeeeeeee : nt! KiBugCheckDispatch+0x69
peee9eee ffffcae4’ c7693d4e fffffsee0 eeeeeeee : nt! KiPageFault+0x4738
peeeeee ffffc98e d27a8eee FFffb588° 2cef6e380 : myfault+exi2de
he@fc76 eeeeeeee eeRGeETe FFfff3800 OF407b91 : myfault+ex168e
H7ac3ce ffffc98e di7afbse eeeeeeee eeeeeeee : myfault+Ox17F1
+0x361
© Please confirm x
6
The input file was linked with debug information ix4c
and the symbol filename is:
“https://imgur.com/a/PiWvsBO0"
an you want to look for this file at the specified path
and the Microsoft Symbol Server?
(1 Don't display this message again
The central Riot Anti-Cheat team circa Feb. 18, 2020.
Want to join our gang? Take a look at our careers website (www.riotgames.com/careers) for openings.
```

## Slide 22

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
a .
black hat
MMIrMrminime
Your device ran into a problem and needs to resta
We're just collecting some error info, and then you”!
restart.
40% complete
For more information about this issue and possible fixes, vist
hitps://weew windows.com/stopen
if you call # support person give then (His inf
Stop code; SYSTEM THREAD EXCEPTION. NOT WAND«E
JP
H \
You're laughing - EAG just crashed
my hypervisor and you¥e laughing
ED OUR CODE OF CONDUCT
s been permanently for Cheating. This is a direct breach of Su PPORT
uct, which you can refer to here. We have taken the necessary steps
ositive experience for other players, resulting in a permanent ban,
itely. This ban will prevent you from participating in online content in
Rainbow Six Siege
```

## Slide 23

#BHUSA @BlackHatEvents

## Slide 24

###### Talk Roadmap

###### **Part I: Cheats & Anti-Cheats**

- Introduction

- The world of game cheats

- Experiences with investigating anticheats

###### **Part II: A Treasure Chest of Defenses**

- Mitigating BYOVD

- Windows kernel hardening

- Software diversification

- Detecting rogue hardware

- Hiding memory

**Part III: Insights & Takeaways**

- Impacts of anti-cheats

- • The next battleground

- • Takeaways

#BHUSA @BlackHatEvents

## Slide 25

###### Anti Cheat Defences – The Usual Suspects

###### Any defense you have heard about is probably used:

- Registered Callbacks

   - Hooking API calls

- Signature scanning

   - AI detection methods

- File and memory integrity checks

- Obfuscations and packing

   - Instruction Misalignment

   - TPM usage

   - Stack walking

- Anti Debug

#BHUSA @BlackHatEvents

## Slide 26

###### Talk Roadmap

###### **Part I: Cheats & Anti-Cheats**

- Introduction

- The world of game cheats

- Experiences with investigating anticheats

###### **Part II: A Treasure Chest of Defenses**

   - Mitigating BYOVD

-

- Windows kernel hardening

- Software diversification

- Detecting rogue hardware

- Hiding memory

**Part III: Insights & Takeaways**

- Impacts of anti-cheats

- • The next battleground

- • Takeaways

#BHUSA @BlackHatEvents

## Slide 27

###### Kernel code protection

All code in the kernel should be signed. ≠

Windows checks that all code loaded into the kernel via normal APIs is signed.

#BHUSA @BlackHatEvents

## Slide 28

Bring Your Own Vulnerable Driver (BYOVD)

1. Legitimate drivers contain bugs/vulnerabilities

2. Attackers exploit these

3. Unsigned code can now be loaded into the kernel

In recent years, this became a popular entry vector for malware

#BHUSA @BlackHatEvents

## Slide 29

###### BYOVD – Malware Case Study

Arbitrary Kernel Read/Write found in GIGABYTE Driver `gpcidrv.sys`

Robinhood ransomware attacks use `gpcidrv.sys`

Sophos EDR detects `gpcidrv.sys` and prevents it from loading

Check Point’s SandBlast detects and prevents Robinhood in tests

#BHUSA @BlackHatEvents

## Slide 30

###### BYOVD – Malware Case Study

BattlEye Anti-Cheat blocks `gpcidrv.sys` from loading

Arbitrary Kernel Read/Write found in GIGABYTE Driver `gpcidrv.sys`

Robinhood ransomware attacks use `gpcidrv.sys`

`Gpcidrv.sys` appears on UnknownCheats forum

Sophos EDR detects `gpcidrv.sys` and prevents it from loading

Check Point’s SandBlast detects and prevents Robinhood in tests

#BHUSA @BlackHatEvents

## Slide 31

###### BYOVD – Malware Case Study

Attempted ransomware campaign by Scattered Spider using `iqvsw64e.sys`

Trojan.DownLoader installs crypto mining software via `WinRing0x64`

BlackByte uses `RTCore64.sys` to disable EDR callbacks APT41 deploys `zamguard64.sys` to disable EDR

#BHUSA @BlackHatEvents

## Slide 32

###### BYOVD – Malware Case Study

All four drivers are blocked by multiple anti-cheat solutions

Takeaway: Cheat & anti-cheats move faster than malware & EDRs

Attempted ransomware campaign by Scattered Spider using `iqvsw64e.sys`

Trojan.DownLoader installs crypto mining software via `WinRing0x64`

BlackByte uses `RTCore64.sys` to disable EDR callbacks APT41 deploys `zamguard64.sys` to disable EDR

#BHUSA @BlackHatEvents

## Slide 33

How Anti Cheats stop BYOVD

**Method A Load Time Prevention** Block vulnerable drivers from loading altogether

**Example** - Using object callbacks to intercept handle manipulation behaviour and strip access rights

**Method B Run Time Detection**

Walk through suspect areas and scan for malicious code

**Example** – Scanning through the nonpaged pool space  looking for known behaviour signatures

#BHUSA @BlackHatEvents

## Slide 34

###### Talk Roadmap

###### **Part I: Cheats & Anti-Cheats**

- Introduction

- The world of game cheats

- Experiences with investigating anticheats

###### **Part II: A Treasure Chest of Defenses**

   - Mitigating BYOVD

-

- Windows kernel hardening

- Software diversification

- Detecting rogue hardware

- Hiding memory

**Part III: Insights & Takeaways**

- Impacts of anti-cheats

- • The next battleground

- • Takeaways

#BHUSA @BlackHatEvents

## Slide 35

###### Shortcomings of BYOVD Defenses

###### **Method A Method B Load Time Run Time Prevention Scanning**

**Issue –** Cheat can **Issue –** Slow to run be loaded before and hurts game the game runs performance

   - Both methods rely on signatures to detect

   - known drivers/cheats

- How to **detect unknown attacks** ?

   - Some anti-cheats use _arcane_ measures

**Let's Investigate!**

#BHUSA @BlackHatEvents

## Slide 36

Let’s Investigate
Crash
dump

Crash
dump

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Let's Investigate
2 Binary search
Enter binary search string:
String | FF EO 90|
(Match case
oO Search Up
(Find all occurrences
```

## Slide 37

###### Fishing for Hooks

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Fishing for Hooks
Address
seg010:0000000 1400E560B6
seg0 100000000 1400E8949
seg0 100000000 1400E9D48
seg010:0000000 1400EDF 56
seg010:0000000 1400F 1817
seg010:0000000 1400FA3F6
s€9010:0000000140102AB5
seg010:0000000 140111156
seg0 100000000 140 144247
seg010:0000000140 145DD3
seg010:0000000140 150637
seg010:0000000140159785
seg0 100000000 140 179BF9
seg010:0000000140170 194
Function
sub_1400E3FAD
sub_1400E551D
sub_1400E8894
sub_1400E9D32
sub_1400EDFOB
sub_1400F 1765
sub_1400F A394
sub_ 140102979
sub_140111063
sub_140144220
sub_140148D34
sub_ 140150654
sub_14015973E
sub_140179BDB
sub_14017C0DA
Instruction
jmp
jmp
db 2, 2 dup(0), OFFh, ¢
rax
db OFFh ; ¥
jmp
jmp
jmp
jmp
jmp
jmp
jmp
jmp
jmp
Fax
Tax
rax
Fax
Fax
Tax
rax
fax
fax
```

## Slide 38

Fishing for Hooks
Target 1
Detour 1
Target 2
Detour 2

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Fishing for Hooks
)
Target1, =
enmmword 90
ar (
, “cc, Detour 1
Target 2 5
>
db
db
db
db
db @
db @
db (
L4@@6F2C@ xmmword 9 I
¢
g Detour 2
nt!KiPageFault: nt!KiSwInterrupt:
FFFFF300° eF2eddee 5A push rax FFFFF300° @F285058 5e push rax
FFFFF300° OF20dde1 48b8bedea62ceefSfffF mov rax,offset vgk+ex5debe FFFFF300° 8F205051 48b83dd1a62ceefsffff mov rax,offset vgk+@x5d13d
FFFFF300° @F2eddeb Ffee jmp rax FFFFF800° 8F20505b ffee jmp rax
FFFFF300° @F2Added 98 nop FFFFF3800° 8F20505d 90 nop
FFFFF3800° OF2Addee 90 nop FFFFF800° OF20505e 90 nop
FFFFF300° OF2AddeF 90 nop FFFFF300° BF2E5E5F 90 nop
FFFFF300° OF20dd10 c645abe1 mov byte ptr [rbp-55h],1 FFFFF300° OF205060 90 nop
FFFFF3800° OF20dd14 488945be mov qword ptr [rbp-5@h],rax FFFFF300° OF205061 90 nop
```

## Slide 39

###### A look at the Targets

##### KiPageFault

##### KiSwInterrupt

   - Kernel trap handler for software interrupts

- Windows page fault handler

•

- Handles:

   - Triggered by the OS for deferred kernel work (DPCs)

- Bad read/write access

- Page protection violations

- Executing NX pages

#BHUSA @BlackHatEvents

## Slide 40

###### Page Fault

If interrupt is from Kernel… And Page Fault code is 4 (executing NX page) And IRQL <= 2

Run CustomErrorHandler(RCX = FaultingAddress, RDX = ErrorCode);

…

#BHUSA @BlackHatEvents

## Slide 41

###### Laying the Trap

- Malicious code is often mapped using **MmAllocatePagesForMdl** or **ExAllocatePoolWithTag**

- Both create a safe, non-pagable, area for the code to execute

- On game boot -> page map flags for these target areas is written

- **NX is set for target PPE** , the second level of paging

**Game Boot**

#BHUSA @BlackHatEvents

## Slide 42

Detection Pipeline

Install hook on Page Fault handler

Spray NX on suspect kernel areas

Execution attempt in nonpaged pool

Exception thrown & caught by the custom handler

Defender can analyse & respond

#BHUSA @BlackHatEvents

## Slide 43

###### Blue Screen of Death

- Attempt to replicate a page fault hook…

- We install a simple inline hook which returns to the main fault handler…

**CRITICAL_STRUCTURE_CORRUPTION Windows Kernel Patch Protection Blue Screens our Machine :(**

#BHUSA @BlackHatEvents

## Slide 44

KiSwInterrupt is one such entry point

###### PatchGuard Boot Camp

- PatchGuard protects critical kernel structures and functions

- It **hides by piggybacking** legitimate kernel entry points

- This way it can execute its checks without exposing a dedicated thread

- **KiSwInterrupt** is one such entry point

- III – Triggering a Check E - KiSwInterruptDispatch

#BHUSA @BlackHatEvents

## Slide 45

###### A look at the Targets

##### KiPageFault

##### KiSwInterrupt

   - Kernel trap handler for software interrupts

- Windows page fault handler

•

- Handles:

   - Triggered by the OS for deferred kernel work (DPCs)

- Bad read/write access

- Page protection violations

- Executing NX pages

   - Piggy backed by windows kernel patch protection

- Core function - protected by windows kernel patch protection

#BHUSA @BlackHatEvents

## Slide 46

###### Muting PatchGuard

###### KiSwInterrupt Hook:

Check interrupt came from the kernel Save registers & align stack

Another Function Call

Unclobber registers & stack Check privilege and return to interrupted code

HalPerformEndOfInterrupt Tells interrupt controller that the CPU is finished processing an interrupt

#BHUSA @BlackHatEvents

## Slide 47

###### Other PatchGuard Smashing

- Vanguard disables PatchGuard entry via KiSwInterrupt with an inline hook

- It also mutes currently running PatchGuard contexts -> queuing infinite waits

- And corrupts DPC structures to break PatchGuard’s deferred execution and checks

#BHUSA @BlackHatEvents

## Slide 48

###### Other PatchGuard Smashing

- Vanguard disables PatchGuard entry via KiSwInterrupt with an inline hook

##### Silence, PatchGuard

- It also mutes currently running PatchGuard contexts  queuing infinite waits

- And corrupts DPC structures to break PatchGuard’s deferred execution and checks

Riot Vanguard is talking

#BHUSA @BlackHatEvents

## Slide 49

Defence Recap

Install NX net and Suppress Windows page fault hook Patch Protection

Mapped Code falls straight into the net

#BHUSA @BlackHatEvents

## Slide 50

###### Talk Roadmap

###### **Part I: Cheats & Anti-Cheats**

- Introduction

- The world of game cheats

- Experiences with investigating anticheats

###### **Part II: A Treasure Chest of Defenses**

   - Mitigating BYOVD

-

- Windows kernel hardening

- Software diversification

- Detecting rogue hardware

- Hiding memory

###### **Part III: Insights & Takeaways**

- Impacts of anti-cheats

- • The next battleground

- • Takeaways

#BHUSA @BlackHatEvents

## Slide 51

A long-time issue

Cheats rely on **offsets** and **pointer paths** to know where important values or functions are located

ModuleBase + 0xFA

+ 0x103 + 0x20 - 0x7 Health

#BHUSA @BlackHatEvents

## Slide 52

###### Effect of Updates

When a game gets updated/rebuilt the **pointer paths change** and must be freshly reversed

ModuleBase + 0xFA

+ 0x103 + 0x20

- 0x7 CatPictures

**What if this could be done for everyone all the time?**

#BHUSA @BlackHatEvents

## Slide 53

QB System

The Process
0.exe
0.exe
• Each client initially
gets a base build
0.exe
• First time run -> patch
is delivered
Base Build
0.exe
• Patch repeated at
0.exe
semi-regular intervals
0.exe
0.exe

#BHUSA @BlackHatEvents

## Slide 54

QB System

The Process
3.exe
4.exe
• Each client initially
gets a base build
1.exe
• First time run  patch
is delivered
Base Build
5.exe
• Patch repeated at
2.exe
semi-regular intervals
7.exe
6.exe

#BHUSA @BlackHatEvents

## Slide 55

QB System

The Process
b.exe
c.exe
• Each client initially
gets a base build
d.exe
• First time run  patch
is delivered
Base Build
e.exe
• Patch repeated at
8.exe
semi-regular intervals
9.exe
a.exe

#BHUSA @BlackHatEvents

## Slide 56

###### What Changes

### Offsets

Specific memory offsets are shifted per build

### Encryption

Decryption routines use unique keys and logic per build

### Obfuscation

Code is reshuffled across builds, making static signature scanning unreliable

#BHUSA @BlackHatEvents

## Slide 57

The Effect

**Offsets are now unique to each build leaving two options for cheat developers:**

1. Provide a unique cheat per unique build on the game (time consuming)

2. Develop cheats which signature scan or wrap key functions (time consuming and hard)

+

#BHUSA @BlackHatEvents

## Slide 58

The Effect

**Offsets are now unique to each build leaving two options for cheat developers:**

1. Provide a unique **attack** per unique build on the target (time consuming)

2. Develop **attacks** which signature scan or wrap key functions (time consuming and hard)

+

#BHUSA @BlackHatEvents

## Slide 59

###### Talk Roadmap

###### **Part I: Cheats & Anti-Cheats**

- Introduction

- The world of game cheats

- Experiences with investigating anticheats

###### **Part II: A Treasure Chest of Defenses**

- Mitigating BYOVD

- Windows kernel hardening

- Software diversification

- Detecting rogue hardware

- Hiding memory

###### **Part III: Insights & Takeaways**

- Impacts of anti-cheat

- • The next battleground

- • Takeaways

#BHUSA @BlackHatEvents

## Slide 60

###### Introduction to Memory Access

Applications
Kernel
MMU Memory
IOMMU
PCI Express Bus
Device Device Device Malicious Device

#BHUSA @BlackHatEvents

## Slide 61

Direct Memory Access – Attack Examples

Bypass the lock screen on Windows 10

Connect a USB-C device and dump password (Thunderclap attack) Cloud provider dumping memory of protected machine

Cheat at video games.

#BHUSA @BlackHatEvents

## Slide 62

Direct Memory Access – Game Cheats

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
‘
\
Direct Memory Access - Game Cheats _
Mouse Fuser
> | HDMI Fuser
—/({ ——
OUT
<
IN IN
Player Mouse —
re
Direct-—Memory-Access
Card
PC Running Game PC Running Cheat
pee
```

## Slide 63

###### Detecting DMA Attacks

Anti-cheat scans all PCI devices

By walking the config space, simple checks can be done on serials, vendor IDs, etc.

Known DMA firmware can be flagged Anything that instantly looks like a DMA card is disabled

#BHUSA @BlackHatEvents

## Slide 64

###### Detecting DMA Attacks

DMA cards need to get sneaky

DMA cheats change their firmware to look innocent e.g., a network card.

**Configuration Space** – Vendor IDs, Supported Capabilities, Serials

**Base Address Registers** – Responding to reads/writes correctly (behaviour)

**Interrupts** – Messaged Signal Interrupts behave correctly

#BHUSA @BlackHatEvents

## Slide 65

###### Detecting DMA Attacks

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Detecting DMA Attacks
What
ae kind?
network
card
Intel
Do some
networking
Uhhhbhh,
OxFFFFFFFF?
cy@
```

## Slide 66

###### Talk Roadmap

###### **Part I: Cheats & Anti-Cheats**

- Introduction

- The world of game cheats

- Experiences with investigating anticheats

###### **Part II: A Treasure Chest of Defenses**

- Mitigating BYOVD

- Windows kernel hardening

- Software diversification

- Detecting rogue hardware

- Hiding memory

###### **Part III: Insights & Takeaways**

- Impacts of anti-cheats

- • The next battleground

- • Takeaways

#BHUSA @BlackHatEvents

## Slide 67

###### Protecting Secrets in Memory

- Info stealing malware scans memory for credentials and credit card numbers.

- Easy Anti-Cheat and Vanguard have cool ways making important values in memory significantly harder to find.

- We present Vanguard’s memory protection method

#BHUSA @BlackHatEvents

## Slide 68

###### Process Isolation

- Each Windows process runs in its own **virtual address space**

- This ensures one process cannot directly access another’s memory

- The **CR3 register** holds the base address of the page map ( **PML4** ) for the current process

- Switching process = loading a new CR3  changes the view of memory

MS Paint

Valorant

CR3

#BHUSA @BlackHatEvents

## Slide 69

###### Hooking the Scheduler

- Riot Vanguard **hooks the context switch** post operation

- When the context is changed, vanguard checks the properties of the new context

- Based off the result of these checks, **CR3 is written**

##### HalClearLastBranchRecordStack

#BHUSA @BlackHatEvents

## Slide 70

###### Context Switch Hook

###### Detour:

…

Custom Handler

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Context Switch Hook
Detour:
e
push ris
moy rbp.rsp xor edx,edx
wo cling tr [vgk+0x7c179 (ffFfF800" 2ca8c179) ] fest renered
movzx eax,byte ptr [vgk+0x7c casc - > c
lea rbx. [vgk (F4#F8@0 2ca10000) ] je vgk+0x52759 (fffFf800° 2ca62759) Branch
mov rdi,rcx
@8 mov rax,qword ptr [rbx+rax*8+7C188h] | .
xor rax,qword ptr [vgk+0x7c180 (fffff800° 2ca8c18@) ] part ee me ea CEFR feeorzcancree) 1
call rex cmp rdi,qword ptr [rax+rdx
mov rax,cr3 je vgk+0x52757 (fffff800° 2ca62757) Branch
cmp rax,qword ptr [vgk+@x7c148 (fffff800 2ca8c148) ]
jne vgk+0x533b1 (fffFF800° 2ca633b1) Branch
inc edx
cmp edx,r8d
movzx eax,byte ptr [vgk+0x78e31 (ffffF800° 2ca88e31) ] jb vgk+0x52741 (fffff800°2ca62741) Branch
mov rex,rdi
@@ mov rdx,qword ptr [rbx+rax*8+78E4eh]
xor rdx,qword ptr [vgk+0x78e38 (ffffF3800° 2ca88e38) | jmp vgk+0x52759 (fff Ff8e0°2ca62759) Branch
call rdx
cmp rax,qword ptr [vgk+@x7c1b8 (fffff800° 2ca8c1b8) |
jne vgk+0x533b1 (fffFF800° 2ca633b1) Branch mov bl.1
cmp byte ptr [vgk+0x7c2ee (ffFFF800° 2ca8c20@) ],e _ rex, [vgk#@x7c2b8 (FFFFF80@" 2ca8c2b8) ]
je vgk+0x52a61 (fffFF800° 2ca62a61) Branch 2
call qword ptr [vgk+0x601c0 (fffff800° 2ca7e1c8@) J
test bl,bl
cmp byte ptr [vgk+0x7c201 (fffff880° 2ca8c201) ],e je vgk+0x533b1 (fffff800°2ca633b1) Branch
je vgk+0x533b1 (fffff800° 2ca633b1) Branch
eee
lea rex, [vgk+@x7c2b8 (ffFFf800° 2ca8c2b8) ]
xor bl,bl
call qword ptr [vgk+@x601a8 (fffff800° 2ca7e1a8) | Custom Handler
mov r8d,dword ptr [vgk+@x7c1d8 (fffff800° 2ca8c1d8) ]
cmp r8d,200h
je vgk+0x52757 (fffff800° 2ca62757) Branch
```

## Slide 71

###### Context Switch Hook – Pseudocode

If:

1. The new address space is for Valorant

2. The new thread belongs to the Valorant process

3. The thread belongs to a predefined allowlist

Then:

Jump to custom handler -> switch to secret CR3

#BHUSA @BlackHatEvents

## Slide 72

###### Process Isolation

- A context switch occurs

- Our new process is Valorant, and our **thread is allowlisted**

**CR3**

- **CR3 is shifted** to point to a different PML4/address space

???

MS Paint

Valorant

#BHUSA @BlackHatEvents

## Slide 73

Process Isolation

CR3
??? Valorant
Health Status
IsPaused Velocity
Ammo Weapon

#BHUSA @BlackHatEvents

## Slide 74

Process Isolation

CR3
Valorant 2.0 Valorant
EnemyLocation Health Status
EnemyHealth IsPaused Velocity
WorldState Ammo Weapon

#BHUSA @BlackHatEvents

## Slide 75

Defence Recap

Augment the scheduling system

Redirect trusted Creating an threads to a invisibility cloak different page map for memory!

#BHUSA @BlackHatEvents

## Slide 76

###### Talk Roadmap

###### **Part I: Cheats & Anti-Cheats**

- Introduction

- The world of game cheats

- Experiences with investigating anticheats

###### **Part II: A Treasure Chest of Defenses**

- Mitigating BYOVD

- Windows kernel hardening

- Software diversification

- Detecting rogue hardware

- Hiding memory

###### **Part III: Insights & Takeaways**

- Impacts of anti-cheats

- • The next battleground

- • Takeaways

#BHUSA @BlackHatEvents

## Slide 77

###### Measurable Factors

Anti-Cheat Strength Measured via grey box testing

Cheat Availability Scraped from cheat selling sites

Game

Cheat Price

Cheat Game Price Popularity Scraped from Average players cheat selling sites in a month (PC)

#BHUSA @BlackHatEvents

## Slide 78

###### Market Observations

**Mean Cheat Uptime = 50%**

**Mean Cheat Uptime = 86.2%**

- Cheat Working | — Cheat Not Working | · Cheat not Available

#BHUSA @BlackHatEvents

## Slide 79

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
BRIEFINGS
Anticheat Strength
NS mo Vv © Ro Vv S w \
SC XK SP SF er SF SF ww SF &
6) & < N wv Gy x
~ ° > we (oy s . xf < iN
as < x < © v Ww ro) < Ww
ao tS x < v J &
Ry ¢ “ oo” gt pS e « e
& wW oe ‘SS s
eg oe wv
```

## Slide 80

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
BRIEFINGS
Anticheat Strength —«- Cheat Uptime (%)
120-
100- Denne :
pewne~ eo sis
80- Lf "2 —- “SL a Pas
Za Se ee at
ry
7
60- ie
aS Sa
40-
20-
0 1 1 1 1 t 1 1 1 1 1 1
x .xU Vv Le} S Vv S wu NS
Ss yr ses & & x F  @&
se ‘. RS < & os wv & ev BS
I Sn ST SO DEN A CO SE
ee ¢ “ ow” at © ce < gf
x ye Oo s RS
```

## Slide 81

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
BRIEFINGS
Anticheat Strength
—«= Cheat Uptime (%)
Mean Cheat Price ($)
120-
100- Bet .
o ¢
80- ra i ee ee eo, mm . we
~ a "s —— wn eh = meas Pa
ry
ye 7
60- 4
40-
20-
0 7 7 1 ' 7 1 1 ' 1 1
\ xe Vv © © v S © s
. x ‘s » s <
S S .) RY we x < f) RC S >
So MF KS OK KF OK SK K
xe « oO Ss w & N RNY 5 < wv
we ¢ “ Vg at S) e < ee
x .°) 2 oo s <
mS os &
```

## Slide 82

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
BRIEFINGS
Anticheat Strength —«= Cheat Uptime (%) Mean Cheat Price ($) «=== Avg Monthly Players
120- = 50,000,000
100- ae .
i ha? - 40,000,000
80- 5 er ee ; rs ‘
ix = “a “ee : 30,000,000
60- ii ‘ s .
Be -
= 20,000,000
40 -
20- = 10,000,000
0 1 ' t ' t 1 1 1 1 ' '
x 1x Vv Le} S Vv S wu S
Se KX SF SF KF SF S&S  & @
30 < > Ne) < > o vv n> wv rN
RY <e PO aS ww 5. Ma we <? cs ww
R\ Oy S
x © we S& RS ss °
```

## Slide 83

###### Talk Roadmap

###### **Part I: Cheats & Anti-Cheats**

- Introduction

- The world of game cheats

- Experiences with investigating anticheats

###### **Part II: A Treasure Chest of Defenses**

- Mitigating BYOVD

- Windows kernel hardening

- Software diversification

- Detecting rogue hardware

- Hiding memory

###### **Part III: Insights & Takeaways**

- Impacts of anti-cheats

- The next battleground

- • Takeaways

#BHUSA @BlackHatEvents

## Slide 84

Kernel Hypervisor
Usermode

#BHUSA @BlackHatEvents

## Slide 85

###### Into Hyper-space

#### Cheats

#### Us

Kernel +

###### Hardware

=

Hypervisor Read/Write

#### Anti-Cheats

”if they start requiring virtualization-based security to be on…we will leverage those features that protect Windows for us”

#BHUSA @BlackHatEvents

## Slide 86

###### Talk Roadmap

###### **Part I: Cheats & Anti-Cheats**

- Introduction

- The world of game cheats

- Experiences with investigating anticheats

###### **Part II: A Treasure Chest of Defenses**

- Mitigating BYOVD

- Windows kernel hardening

- Software diversification

- Detecting rogue hardware

- Hiding memory

###### **Part III: Insights & Takeaways**

- Impacts of anti-cheats

- The next battleground

- • Takeaways

#BHUSA @BlackHatEvents

## Slide 87

Cool Defences Deployed by Anti-cheats

Detecting unsigned code in the kernel.

Stopping rouge hardware and DMA attacks.

Practical software diversification

A cloak of invisibility for memory.

#BHUSA @BlackHatEvents

## Slide 88

Takeaways – BlackHat Sound Bytes

Anti-cheats A system is never as implement some safe as when a user of best software is playing Fortnite defences. or Valorant.

If game devs can implement these defences, then so can we!

#BHUSA @BlackHatEvents

## Slide 89

**More information, updates, and code are available at:**

# Questions?

**<u>https://game-research.github.io/</u>**

#BHUSA @BlackHatEvents
