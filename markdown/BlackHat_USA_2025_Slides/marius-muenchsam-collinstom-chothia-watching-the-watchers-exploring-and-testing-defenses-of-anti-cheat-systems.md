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
text_chars: 28192
ocr_pages: 13
has_ocr: true
redacted_secrets: 0
ocr_confidence: 84.5
ocr_unreliable_blocks: 0
vision_verified_blocks: 3
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T05:17:00Z"
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


> Recovered by OCR — confidence 81/100 on the text kept, 67/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Prior Art
Un veilin g th e #HITB2023AMS https://conference.hitb.org,
underground world of 2024) d Exploiting Online Games
ANTI-CHEATS AMS for
paral sec Bypassing Anti-Cheats &
EUROPE 2m19 Hacking Competitive Games
blackhat
auoust 7s ao Next Level Cheating and
Modern Anti-Abuse Mechanisms in Nicolas Guigo Joel St. John f Pree.
Competitive Video Games
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


> Recovered by OCR — confidence 94/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

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


> Recovered by OCR — confidence 90/100 on the text kept, 65/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
+0x361
© Please confirm x
6
The input file was linked with debug information ix4c
and the symbol filename is:
an you want to look for this file at the specified path
and the Microsoft Symbol Server?
(1 Don't display this message again
The central Riot Anti-Cheat team circa Feb. 18, 2020.
Want to join our gang? Take a look at our careers website (www.riotgames.com/careers) for openings.
```

## Slide 22

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 86/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Your device ran into a problem and needs to resta
We're just collecting some error info, and then you”!
restart.
40% complete
For more information about this issue and possible fixes, vist
if you call # support person give then (His inf
Stop code; SYSTEM THREAD EXCEPTION. NOT WAND«E
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


> Recovered by OCR — confidence 84/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
2 Binary search
Enter binary search string:
String | FF EO 90|
oO Search Up
(Find all occurrences
```

## Slide 37

###### Fishing for Hooks

#BHUSA @BlackHatEvents


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 84/100 on the text kept, 58/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Fishing for Hooks

Address                          Function          Instruction
.data:000000014006F2A3                             db 0FFh ; ÿ
.data:000000014006F2CB                             db 0FFh ; ÿ
seg010:00000001400E3FC9          sub_1400E3FAD     jmp     rax
seg010:00000001400E560B          sub_1400E551D     jmp     rax
seg010:00000001400E89A9          sub_1400E8894     jmp     rax
seg010:00000001400E9D4B          sub_1400E9D32     jmp     rax
seg010:00000001400EDF5B          sub_1400EDF0B     db 2, 2 dup(0), 0FFh, 0
seg010:00000001400F1817          sub_1400F17B5     db 0FFh ; ÿ
seg010:00000001400FA3F6          sub_1400FA39A     jmp     rax
seg010:0000000140102AB3          sub_140102979     jmp     rax
seg010:0000000140111156          sub_1401110B3     jmp     rax
seg010:000000014014A2A7          sub_14014A220     jmp     rax
seg010:000000014014BDD3          sub_14014BD3A     jmp     rax
seg010:0000000140150B87          sub_140150B5A     jmp     rax
seg010:0000000140159785          sub_14015973E     jmp     rax
seg010:0000000140179BF9          sub_140179BDB     jmp     rax
seg010:000000014017C19A          sub_14017C0DA     jmp     rax

(the "db 2, 2 dup(0), 0FFh, 0" row is cut off at the right edge of the screenshot;
 the first two .data rows have an empty Function column)

#BHUSA  @BlackHatEvents
```

## Slide 38

Fishing for Hooks
Target 1
Detour 1
Target 2
Detour 2

#BHUSA @BlackHatEvents


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 73/100 on the text kept, 61/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Fishing for Hooks

[IDA listing — parts of the left-hand label column are hidden behind the pointing-hand graphics]

Target 1 →
140…                     8024AC8D4800000158EC814855h
                                 ; DATA XREF: sub_140116F91+8[obscured]
14…  …mmword             909090E0FF0000000000000000B84850h        ← Detour 1
                                 ; DATA XREF: sub_1400E9D1[obscured]
                                 ; seg010:0000000140E85094↓[obscured]
Target 2 →
140…                     0AC8D4800000150EC8148565508EC8348h
                                 ; DATA XREF: sub_140195A88+8↓r
                                 ; seg010:0000000141197764↓o ...
                     db  24h ; $
                     db  80h ; €
                     db    0
                     db    0
                     db    0
                     db    0
                     db    0
                     db    0
14006F2C0 xmmword    909090E0FF0000000000000000B84850h            ← Detour 2
                                 ; DATA XREF: sub_1401319F[obscured]
                                 ; seg010:0000000141285754↓[obscured]

[left WinDbg pane]
nt!KiPageFault:
fffff800`0f20dd00 50                push    rax
fffff800`0f20dd01 48b8b0d0a62c00f8ffff mov rax,offset vgk+0x5d0b0
fffff800`0f20dd0b ffe0              jmp     rax
fffff800`0f20dd0d 90                nop
fffff800`0f20dd0e 90                nop
fffff800`0f20dd0f 90                nop
fffff800`0f20dd10 c645ab01          mov     byte ptr [rbp-55h],1
fffff800`0f20dd14 488945b0          mov     qword ptr [rbp-50h],rax

[right WinDbg pane]
nt!KiSwInterrupt:
fffff800`0f205050 50                push    rax
fffff800`0f205051 48b83dd1a62c00f8ffff mov rax,offset vgk+0x5d13d
fffff800`0f20505b ffe0              jmp     rax
fffff800`0f20505d 90                nop
fffff800`0f20505e 90                nop
fffff800`0f20505f 90                nop
fffff800`0f205060 90                nop
fffff800`0f205061 90                nop

#BHUSA  @BlackHatEvents
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


> Recovered by OCR — confidence 90/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
\
Direct Memory Access - Game Cheats _
Mouse Fuser
> | HDMI Fuser
OUT
<
IN IN
Player Mouse —
Card
PC Running Game PC Running Cheat
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


> Recovered by OCR — confidence 91/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Detecting DMA Attacks
What
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


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 74/100 on the text kept, 66/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Context Switch Hook

Detour:

[left column]
   push    r15
   mov     rbp,rsp
   sub     rsp,30h
   movzx   eax,byte ptr [vgk+0x7c179 (fffff800`2ca8c179)]
   lea     rbx,[vgk (fffff800`2ca10000)]
   mov     rdi,rcx
00 mov      rax,qword ptr [rbx+rax*8+7C188h]
   xor     rax,qword ptr [vgk+0x7c180 (fffff800`2ca8c180)]
   call    rax
   mov     rax,cr3
   cmp     rax,qword ptr [vgk+0x7c148 (fffff800`2ca8c148)]
   jne     vgk+0x533b1 (fffff800`2ca633b1)  Branch

   movzx   eax,byte ptr [vgk+0x78e31 (fffff800`2ca88e31)]
   mov     rcx,rdi
00 mov      rdx,qword ptr [rbx+rax*8+78E40h]
   xor     rdx,qword ptr [vgk+0x78e38 (fffff800`2ca88e38)]
   call    rdx
   cmp     rax,qword ptr [vgk+0x7c1b8 (fffff800`2ca8c1b8)]
   jne     vgk+0x533b1 (fffff800`2ca633b1)  Branch

   cmp     byte ptr [vgk+0x7c200 (fffff800`2ca8c200)],0
   je      vgk+0x52a61 (fffff800`2ca62a61)  Branch

   cmp     byte ptr [vgk+0x7c201 (fffff800`2ca8c201)],0
   je      vgk+0x533b1 (fffff800`2ca633b1)  Branch

   lea     rcx,[vgk+0x7c2b8 (fffff800`2ca8c2b8)]
   xor     bl,bl
   call    qword ptr [vgk+0x601a8 (fffff800`2ca701a8)]
   mov     r8d,dword ptr [vgk+0x7c1d8 (fffff800`2ca8c1d8)]
   cmp     r8d,200h
   je      vgk+0x52757 (fffff800`2ca62757)  Branch

[right column]
   xor     edx,edx
   test    r8d,r8d
   je      vgk+0x52759 (fffff800`2ca62759)  Branch

   mov     rax,qword ptr [vgk+0x7c1e0 (fffff800`2ca8c1e0)]
   cmp     rdi,qword ptr [rax+rdx*8]
   je      vgk+0x52757 (fffff800`2ca62757)  Branch

   inc     edx
   cmp     edx,r8d
   jb      vgk+0x52741 (fffff800`2ca62741)  Branch

   jmp     vgk+0x52759 (fffff800`2ca62759)  Branch

   mov     bl,1

   lea     rcx,[vgk+0x7c2b8 (fffff800`2ca8c2b8)]
   call    qword ptr [vgk+0x601c0 (fffff800`2ca701c0)]
   test    bl,bl
   je      vgk+0x533b1 (fffff800`2ca633b1)  Branch

...

Custom Handler

#BHUSA  @BlackHatEvents
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

## Slide 80

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 83/100 on the text kept, 43/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Anticheat Strength —«- Cheat Uptime (%)
120-
ry
40-
20-
```

## Slide 81

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 88/100 on the text kept, 41/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Anticheat Strength
—«= Cheat Uptime (%)
Mean Cheat Price ($)
120-
ry
60- 4
40-
20-
```

## Slide 82

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 80/100 on the text kept, 42/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Anticheat Strength —«= Cheat Uptime (%) Mean Cheat Price ($) «=== Avg Monthly Players
120- = 50,000,000
i ha? - 40,000,000
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
