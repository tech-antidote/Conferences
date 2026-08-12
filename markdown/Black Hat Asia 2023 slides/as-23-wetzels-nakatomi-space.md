---
title: "Nakatomi Space"
speakers: ["Wetzels"]
conference: "Black Hat"
conference_full: "Black Hat ASIA 2023"
edition: "ASIA"
year: 2023
source_pdf: "Black Hat Asia 2023 slides/AS-23-Wetzels-Nakatomi-Space.pdf"
pages: 41
sha256: "63e6e4610c36eb73a6fcdc8a19e440ddba0e6263c8c40d2b957f13d373665ccc"
text_chars: 21175
ocr_pages: 38
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T23:57:16Z"
---
# Nakatomi Space

**Speakers:** Wetzels  
**Conference:** Black Hat ASIA 2023  
**Source:** `Black Hat Asia 2023 slides/AS-23-Wetzels-Nakatomi-Space.pdf` (41 pages)


## Slide 1

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Automated Cybersecurity Across Your Digital Terrain
NAKATOMI SPACE
Lateral Movement as Level 1
Post-Exploitation in OT
Jos Wetzels
Security Researcher, Forescout
```

## Slide 2

- Security Researcher @ Forescout

   - Focus on OT / IoT, embedded systems in general

- Joined Forescout in 2018 via SecurityMatters

   - OT-focused cybersecurity vendor

- Previously, researcher @ University of Twente (NL)

- Frequent speaker at security conferences, such as Black Hat, DEF CON, CCC, HITB, etc.

## Slide 3

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Level 4/5
Enterprise / "IT"
Internet DMZ
OT Lateral movement
Servers (AV/WSUS/Patch)
Level 3.5 Remote Access / Jumpbox IT/OT
DMZ Historian Perimeter
Central HMIs
Level 3 Servers (App/DB/Eng.)
Historians
Control Center Domain Controllers
Level 2.5
DMZ
Site / Area / Cell Site / Area / Cell
Local HMIs
Level 2 | Ei EWS
Area Supervisory Aelelele) 2 Servers (App/DB)
Gateway
1p) PLCs
[Ci} 2222929 wipe
DO} nested OO (oy
] fieldbus 55550) i Industrial Prior work
Level 1 mle) Wireless
control ney eh ‘Classical’ perimeters at L3.5/L2.5
oo oo us packaged unit ae East-West ‘@)) | D+
sensors Upstream to L2
revel 0 {i tity © Actuators
Field Devices
[peeeee]
Safety [190] sts
EXIIIT
```

## Slide 4

-

-

-

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Nakatomi (Cyber)Space* Architectural elements with
latent potential to enable
> OT has lot of “network crawl space” traversing it in unintended and
— Highly complex systems-of-systems often overlooked ways
> Lot of stuff beyond typical Ethernet networks
— Fieldbus networks (PROFIBUS/NET, CANopen, etc.)
— RF networks (WirelessHART, 9OOMHz, TETRA WAN)
— PTP links to 34 party systems
> Often complete lack of visibility
— Perimeters at this level often unacknowledged
— Little awareness of possibility for maneuver
— No ability to detect activity
* https://bldgblog.com/2010/01/nakatomi-space/
```

## Slide 5

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Deep Lateral Movement Focus
East-West @ LI
Local HMIs “Deep downstream”
Level 2 = EWS
Area Supervisory Aelelel") oA |? Servers (App/DB)
Gateway
J @ Dice Examples
(9) 9
= _\'t RTUS Nested Fieldbus
2299929 IEDs l d t 0 | Wi |
CLIO} wested Oo GD) naustrial Wireless
BEEBE KT dhys IIIT mie inauserial 3rd Party PUs
Level 1 4 | | Sat a) BPCS/SIS links
Control 222999 222999 —_ I
ona oo Ss, rd party CLIO
oa oo us packaged unTt oo
666600
Different Networks
Level 0 Sensors Non-routable (PTP)
Process {= dA © rield povices Non-IP (serial, RF)
2222999
Safety C10} sts
066600
```

## Slide 6

-

-



> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Going through may require L1 RCE
>» Has been demonstrated against many vendors now
> Several LI post-exploitation TTPs have been publicly explored
— Persistence!?3.5
— Privilege escalation?
— Evasion2®
— C27
— Exfiltration®?
— “OT payloads” (impair process control + inhibit response)!4101112
> But no lateral movement at L]
' MITRE SO603, * MITRE S1009,* MITRE S1006
4|INCONTROLLER: New State-Sponsored Cyber Attack Tools Target Multiple ICS - Mandiant
5 Cyber-Security in Building Automation Systems - Forescout
©The Race to Native Code Execution in PLCs—T. Keren et al.
7 Evil bubbles —M. Krotofil et al.
8 Exfiltrating reconnaissance data from air-gapped ICS/SCADA networks - D. Atch et al.
° Greetings from the ‘90s — M. Krotofil et al.
'Ghost in the PLC—A. Abbasi et al.
"A diet of poisoned fruit —J. Wetzels et al. 6
Hey, My Malware Knows Physics! — L. Garcia et al.
```

## Slide 7

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Why bother? Reason #1: Perimeter crossing
| need to move across hardened or unacknowledged perimeters
```

## Slide 8

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
BPCS / SIS architectures
Can be generalized to any distinct but interacting control systems
Integrated Interfaced / “Shared”
ll_o 1
BPCS Sus
```

## Slide 9

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Example: SIS Bypasses
FACEPLATE
(- >)
Bypass sensor,
actuator, SIF BYPASS STATUS }€
BYPASS FB
Needs to be
enabled before > ACTIVATE OUT —
activation (from BPCS) ;
S
Not from BPCS > ENABLE STATUS
> TIMEOUT CNTR —
SW SIGNAL
```

## Slide 10



– –





– –

– –

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Packaged Units (PU)
> Blackbox control systems with specific function
—HVAC, chemical injection, water treatment, gas turbine
—Can range from subsystem to entire plant
> Control/Monitoring interface to PCN/SCADA
—Limited PVs /setpoints exposed
—No direct control over PU internals
> Maintenance often done by 39 party
—E.g. cellular modem
—Indirectly exposes PCN to external connectivity
10
```

## Slide 11

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Example: Fieldbus Couplers. wy
Connect e.g.
PROFIBUS DP ©
External PROFI N ET
site c 1
Master oupter Master
I t Input Output output
npu Area #1 Area #2 utpu
output Output Input I t
utpu Area #1 Area #2 npu
BPCS Packaged unit Often considered
sufficient perimeter due
to limited capabilities
2229299
((y)
O|<— Cz <—— |} ao |
600566 Y oo |
Used to be ‘dumb’
Increasingly ‘smart’
| Coupler vendor remote
maintenace |
Cro Perimeter assumptions
lel lel ey not evaluated for new
attack surface
Mee eee eee ee eee eee eee eee a
```

## Slide 12

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Why bother? Reason #2: Granular control
| want to talk to nested devices in a way not possible through what's
intentionally exposed ©) [Status
OC Valvel
PLC2.Status @) Valve? PLCé
29999000 @) Valvel.Setting
O of
PLC3.Status
PLC3.Fan PLCL SSSEES
PU_PLC.Status 099900
----------- +--+ eee o°o Non-routable [iii
oo|------ ; ' Packaged Unit (PU);
PLC3 PU_PLC
I 1
! ! 999999
i OO]: o,|___={ |
o10 oo “o-
Lol Status 660060006 f
O10 @) Fan OC) Status
Bypass firmware OC ' OC)
. . PU_PLC.Status I Motor
safety limits te !
```

## Slide 13

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Very common in automotive exploitation
RCE on CAN controller / GW to bypass filter > unrestricted CAN access
CAN cmd
filter
3G Multimedia Unit V850 CAN
module Main Processor controller
*C, Miller et al. (2015), “ Tencent Keenlab (2016), Computest (2018)
```

## Slide 14

- 

-

-

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
What do vendors & standards say?
> General acceptance of integrated, interfaced and common architectures
> Usual segmentation advice
> Non-routable or serial PTP links are seen as sufficiently segmented
> Little attention to backplane security in multi-zone devices
There is a conduit between the BPCS zone and the SIS zone, presumably to provide
read only data from the SIS to the BPCS. In this case segregation has been achieved by
using a dedicated point-to-point serial connection. Note that the discrete I/O also shown
14
“IEC 61508 intro, “ HSE OG-0086 ed2, “ NERC CIP-005-6, “” NIST SP 800-8212
```

## Slide 15

## Slide 16

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Scenario: Movable Bridge
Bascule Girder
Trunnion Bearing
Rack
Pinion
I
i < Back Wall
= Front Wall —>|] ° ° Pit ack Wall |
le) %
x v
YL i
(a) LEAF OPEN
Lock Bar Trunnion Shaft Rear Break
Lock Bar Actuator ‘\ j a In Deck ;
tT |
| ¥
\
CWT
Lockbar wy = |
Socket Live Load ee Bs
Bearing a
i |} — Bumper
—-¥ =— —_—F—
4 L
Rest Pier > < Channel ple Bascule Pier >|
16
(b) LEAF CLOSED “Bridge Maintenance Reference Manual -— FDOT, structurae.net
```

## Slide 17

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Bridge closing sequence - Limit Switches
NEAR ISSUE FULLY REMOVE SET BRAKES
FROM AcceeaTe CLOSED LOCKS REDUCED CLOSED LOWER (REMOVE SORES TO NEXT
PREVIOUS [2 ACCELERATION LIMIT DRIVEN (NOT (CREEP) LIMIT (REVERSE) BRAKE ENABLE SHEET
SHEET PULLED)? SPEED DIRECTION RELEASE COMMAND
RAMP COMMAND COMMAND SIGNAL)
LEAF LIMIT SWITCHES
f>— FULL OPEN
>— NEAR OPEN
[— NEAR CLOSED
FULL CLOSED
XX=FA, NA, FO, OR NO
“Bridge Maintenance Reference Manual - FDOT 17
```

## Slide 18

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
“Bridge Maintenance Reference Manual -— FDOT, FDI Services
Bridge closing sequence - Lock Bar
LEAF(S) FULLY
SEATED PERMISSIVE
! ENABLE
START CLOSING ~~ GENERATOR LOWE! SPAN SPAN LOCKS DRIVE SPAN SPAN LOCKS
SEQUENCE CLOSE ™ mee RUNNING? LEAF(6) LOCKS DRIVE LOCKS DRIVEN?
DRIVE
PUSH AND RELEASE PUSH AND RELEASE
PUSH AND RELEASE,
BYPASS FULLY
SEATED LIMIT é ‘ocks for
SWITCHES
BYPASS SPAN
LOCKS DRIVEN
LIMIT SWITCHES
SELECT
LEAF(S)
SEE Leafs FOR
EXPANDED VIEW.
SOUND
HORN | HORN
1
'
1
1
1
1
1
1
f
1
\
se, a
WIZZ East Leat Lea WY”, -tHt)
¥
18
```

## Slide 19





> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Attack Scenarios
> Scenario 1: Close at full speed, hit bearings
—Without decel. to creep speed
—Lock bar driven before closing
—Bypass leaf/lock limit switches
> Scenario 2 : Close at full speed, trigger E-STOP
—Wait until max velocity
—E-STOP not graceful, CWT inertia
—Bypass creep speed
```

## Slide 20

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Attack Path - Likely can’t do this from SCADA
O Bridge #2
| ' Object PlCc| © | Bridge Systems —— ;
Bri #1 ;
ridge i =» 4 te |
: : | a ,
» ' \gcpu [rtug|zo $ OE |
WAN ; uf ° ° S— |
re |
) ! | 4 Wy
y- “ I
! 4 NS z 1 [| '
Coupler 1
~ : Safety PLC (5) At
I
Aa a BYPASS stop
C) SS ' ' ENABLE
' |mcpu | Sp S|ETHS|I0 9 — ‘@ |
: |i sfETHS] 20 § _ e| a
IN L 1 ecco @ (™) ay t
a 1 =» eooee -—_s =
Lf 1 1
| |
1 [
I
(1) RCE on Coupler (2) Auth Bypass (3) RCE on Object PLC
(4) Move into fieldbus (5) Cross SIS PTP link (6) Enable SIS bypass across backplane
```

## Slide 21

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Coupler » Object PLC RTU module
Cannot talk directly to M340 via Wago 750-852 coupler
Various protocols
Limited Modbus Mapping
NNo TDA (routing) BD
Get RCE on coupler via N-day » Proxy traffic to M340
Hook Modbus handler,
turn into proxy
ond
er
Stager Payload
Wago Coupler FW
Supervisor mode
No mitigations
No tsk separation
RWX memory areas
|
NUCLEUS NET
TCP/IP Stack
i
NUCLEUS
Memory Al loc
Modbus
Handler oO
og
>
Proxy Implant
```

## Slide 22





> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
oid _cdecl Control Task(UNSI
CVE-2021-31886* on Wago 750-852
FSP_CB *control_blocka;
>» Stack bof in Nucleus FTPd "USER" cmd CHAR nu_drive[3)3°//
— Check via strlen() but copy until '\r’ > use fake 0x00 [—_————/e—ailippetiermede
: ; . NU TASK *nointerTothisTask;
- Overwrite FTP_Events linked list after user buff FTP SERVER server;
— Disconnect > trigger unlink > write-4 CHAR commandBuf [8];
CHAR *buffer;
INTSZ DytesReceived,
— RW .bss area suitable for shellcode
— Write shellcode ptr to soan_process_packet func ptr
— New FTP session > overwrite buffer ptr with shellcode ptr
— Write shellcode via subsequent FTP data
—LLC frame to trigger shellcode via span_process_packet
>» Supervisor mode, no task separation » No need for privesc
* NUCLEUS:13, Dissecting the Nucleus TCP/IP stack — Forescout & Medigate Labs 22
```

## Slide 23



- –

-

-

-

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
* As of vO1.09.25 (16)
Wago 750-852 Firmware* soolicavion ayer
>» Wago 750 Firmware ZIP Middleware Layer
_ bif: descriptive text file Protocol Stacks Filesystems
_ ANhex: Intel hex fw Nucleus NET stack K-Bus FAT
Ethernet/IP Modbus (RTU/TCP) Datalight FlashFx
>» 60456550.hex » loaded at base address
Automation securit .
_ Nucleus RTOS on ARM Components components CODESYS v2.3 Runtime
~ No symbols (e.g. Diagnostics, wn Gear. Nucleus C/C++, etc.)
— Use BinDiff / Diaphora / debug strs
RTOS - Nucleus
Tasks Interrupts | Mailboxes
> Create Nucleus Task for stable implant nevice privers a
— Runs in background
> Hook Modbus TCP handler
— Proxy incoming FC Ox5A to M340
— Allow tunneling through coupler
```

## Slide 24



-

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Object PLC: Schneider Electric UMAS
> Proprietary SE Modicon engineering protocol under Modbus FC Ox5A
— Much prior work, well-reversed (up to a point)!444
— Start/Stop PLC, download/upload logic, read/write memory blocks, etc.
> SE ControlExpert Security Features
— Project File Encryption (AES-CBC-256)
— Program/Safety password (weak crypto, client-side)*
— UMAS historically unauth, introduced Application Password?
UMAS
SL
Modbus Header
Function Code
Reservation ID
UMAS Service ID
COx5A) (or status) Message Data
TS TT oT ae
1 Byte 1 Byte 1 Byte N Bytes
| Project Basecamp - Digital Bond
2 The secrets of Schneider Electric's UMAS protocol-—P. Nesterov et al.
3 Going Deeper into Schneider Modicon PAC Security —G. Jian
4 Examining Crypto and Bypassing Authentication in Schneider Electric PLCs (M340 / M580) —N. Miles
24.
```

## Slide 25



> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
CVE-2021-22779: Auth Bypass
> Read secret from mem » Don't need to know pwd...
EnhancedcCyberReserve v1
Read Memory Block:
secret = [ B64(salt) + B64(SHA2(salt+pwd)) ]
Take Reservation: auth=SHA2(snonce + secret + cnonce)
Exchange Client & Server Nonce )
[ nested UMAS ]
Authenticated Request:
[ SHA2(SHA2(hwid+cnonce) + msg + SHA2Chwid+snonce)) ]
| Project Basecamp — Digital Bond, 2 The secrets of Schneider Electric’s UMAS protocol - P. Nesterov et al. Going Deeper into Schneider Modicon PAC Security-G. Jian 25
4 Examining Crypto and Bypassing Authentication in Schneider Electric PLCs (M340 / M580) —N. Miles, ° ModiPwn - G. Kauffman et al. 2
```

## Slide 26



> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
CVE-2022-45789 — Authentication Bypass’
> Patch » PW no longer in mem block, however
Reservation Replay
(2) Legitimate session
Exchange Nonces
Send Auth Hash
Get Reservation ID
Replay auth hash
Don't Exchange Nonces
(non-renewing globals)
Get new Reservation ID
@
<
Sniff auth hash
Authenticated Request Forgery
(a) Legitimate session
Exchange Nonces
— Send Auth Hash
— Get Reservation ID
0 k< | >
Forge auth request
Sniff nonces No per-request freshness
Sniff res ID @ No signature secret
“Affects latest M340 and M580 CPU module FW, see SEVD-2023-010-06
26
```

## Slide 27



– –



– –

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Route to CPU Module RCE
>» Different approaches in prior work
—UMAS: Download logic (0x31) '4, vulnerable messages**
—~TCP/IP stack RCE (M580 but not M340)°
> Want method allows hotpatching on updated PLC
—No logic restarts
—DFIR hostile ( project checksums, invisible in source )
—Using obscure protocol features to evade most IDS
' TALOS-2018-0742 — J. Rittle
2 Applying a Stuxnet Type Attack to a Modicon PLC - F. Dola
3 Going Deeper into Schneider Modicon PAC Security —G. Jian
* ModiPwn - G. Kauffman et al. 27
5 Exploring and Exploiting PLCs with Urgent/I] Vulnerabilities — B. Hadad et al.
```

## Slide 28



> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Background: Modicon Application Binary File (APX)
Area
Index #Sections |Load Addr. |Attributes _— > Block Types
— Data/ Exec / Upload Info / FB Data / Constant / etc.
Section
Index size Attributes
Relocation Table (RT)
Data . .
Entry Size] #Entries
Block|Block|Block Block Block|Block Block 5
RTE Nr Area ~ Section - size Attributes
A . offset
rte nr. | 474 offest - size Attributes
Section
RTE N Area - Section - si attribut
r. offset ize ributes
Index size Attributes
Data v
Block/Block|Block Block Block Block Block €
28
```

## Slide 29

-

-

-

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Unexplored UMAS CSA Requests (0x50)
Init/Read/write/Exec virtual 'page'
a
Directly manipulate
RTE blocks
Subsystem with
proprietary
command set
* Happens ‘live’, no restart required
* Doesn't change project checksum
* Exec mods don't show up in source
29
```

## Slide 30

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
CVE-2022-45788 — Modicon CPU RCE“
Can't write directly
to code blocks
Code Block
But can copy to
code blocks
A
(permission check
set to ‘ignore')
S~
™
write payload to data block
@)
(find cave or expand block)
Data Block
“Affects latest M340, M580, MIE, MC80, Quantum, Premium CPU module FW,
see SEVD-2023-010-05
Get RCE when block
executes as part of logic
@)
@
copy from data block to
code block
(find cave or expand block,
then hijack control flow)
if ( !ignore )
{
if ( rte ptr )
{
if ( (rte_ptr->attr & @x10000) != @ )
{
return @x9191;
}
else
{
blocktype =
rte _ptr->attr & OxF;
```

## Slide 31

-

-

-

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
“As of v3.50
SE BMXP3420302 Firmware* Suds
> SE Firmware LDX = ZIP middleware Layer
Protocol Stacks
wWindNet TCP/IP stack CANopen
> vxWorks_bmx*.bin » UNITYM binary
Filesystems
= Segment base @ Ox20000000 GoAhead webserver X-Bus mss PAT
— FW code start @ Ox20010110
— Runtime base @ Ox28000000 Modbus (RTU/TCP) UMAS Datalight Reliance
— VxWorks 6.4 on ARMV4 (So no XN)
— Manually reconstruct symbol table Components. | Components APX Loader Mirano Runtime
Misc.
(e.g. Diagnostics, vxworks shell, Dinkumware C/C++, etc.)
> Runtime exec blocks via sas_UserCodeExec
— Scancycle timer is in the way
— Hook triggerable func to escape
TC Device Drivers Memory | Timers Mutex Etc.
RTOS - VxWorks 6.4
Tasks Interrupts | Exceptions
v4 = kl_userTimeEn(result);
v5 = sas UserCodeExec(v4);
kl_userTimeDis((int)v5);
```

## Slide 32

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Stager Payload & Implant
|
Bridge Systems
Safety PLC
ote |
Backplane u HcPpU | SP S|ETHS|1I0 9
Modicon X-Bus i) |e e e e
rN A ,
Backplane CANopen windNet
Device Driver! |Device Driver
TCP/IP Stack
f
Vxworks
sockLib
Supervisor mode O O vxworks
No mitigations “ . taskLib
Injected code executed
by scancycle
Code Block
;| Stager Payload
No tsk separation “© O
RWX memory areas Implant <
* BMXP3420302 as of v3.50
Modicon CPU Module Fw
Relocate implant code + Spawn dedicated task
Cleanup manipulated blocks (Canti-DFIR)
```

## Slide 33





– – –

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
CANopen payload 4 ou —
> Talk to M340 CANopen API, use CiA funcs
index |SDOName
can_SWrite SDO(ND, » 1, START_BOOT, Ox1023 OS CMD2
can SWrite SDO(ND, Pee CS meses = OX1024 OS CMD Mode?
eae Ox1025 OS Debugger?
can SWrite SDO(ND, » 1, block[i], Ox1026 OS Prompt?
Ox1F50O
Ox1F51
> RCE via SDO: override firmware (safety) limits
—|n-band code dndl — trigger bootloader via NMT/SDO
—~Memory read/write — hotpatching RCE
—|f auth at all: (Static) 32-bit value written to some SDO
1 CAN-in-Automation (CiA) 302-2, * CAN-in-Automation (CiA) 301, 7 CAN-in-Automation (CiA) 302-3
Download Program?
Program Control?
33
```

## Slide 34

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Object PLC » Safety PLC Ethernet module
Cannot talk directly to GuardLogix CPU module or route CIP
Non-routable PTP link
Only Modbus TCP (AOl)
Explicit protected mode
c Wy oo Wa oO
ERO ES Sot ~ ROR SSS SS wa
Exploit N-day vuln in TCP/IP stack for RCE
on Ethernet Module » hop to rest of SIS Allen-Bradley GuardLogix Safety PLC
1756-EN2T/D Ethernet Module
34
```

## Slide 35

-

-

-

-

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
CVE-2019-12256* on Allen-Bradley 1756-EN2T/D
> Send malformed IP options (URGENT/1]) via VxWorks raw sockets
— Multiple Source Record Route (SRR) opts generate ICMP error response
— Stack buffer overflow (opts copied to response without validation)
srr_opt->ptr = 4;
while ( offset_to_current_route_entry > @ )
{
> Only XN enabled memcpy((char *)srr_opt + (unsigned —_int8)srr_opt->len, current_route |
1 . . current_route_entry -= 4;
— Pick SRRs to align stack overwrite offset_to_current_route_entry -= 4;
srr_opt->len += 4;
— Write-4 ROP + stack fixup » cont. exec }
memcpy((char *)srr_opt + (unsigned __int8)srr_opt->len, icmp param + 12,
— Large unused RWX ‘LOAD’ segment vis = srr_opt->ten + 45
— Chop shellcode into chunks of 4 9 write to RWX seg via ROP chain
> Only slight diffs with Armis exploit* against 1756-EN2TR/C
— ROP chain construction, RWX/gadget/func addrs
> Supervisor Mode, no task separation » No need for privesc
— Spawn VxWorks task for stable implant -
* Exploring & Exploiting PLCs with URGENT/11 - B. Hadadet al.
```

## Slide 36



-

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
* As of v11.01
AB 1756-EN2T/D Firmware* soticaton ayer
Middleware Layer
> Allen-Bradley Firmware ZIP
Protocol Stacks
— .nvs: descriptive text file vxworks
; IPnet TCP/IP stack SNMP
— .plt: binary fw oesyet
a 1Tlesystems
_ der: certificates GoAhead webserver OpenssL POSES aa
Rockwell 1756-EN2x ControlBus . .
Datalight Reliance
. Ethernet/IP stack (via APEX)
> PN-49'7069.pIlt » ELF binary
— Segments pre-loaded Components | components i@gnostics eg conn)
— VxWorks 6.9.3 on ARM Misc.
(e.g. BigDigits, Dinkumware C/c++, etc.)
— Manually reconstruct symbol table
— Implant talks to display & backplane drivers
RTOS - Vxworks 6.9.3
Tasks Interrupts | Exceptions
Device Drivers Memory | Timers Mutex Etc.
symbol <@, aAccessDescript_@, ACCESS DESCHLMPANMPAssomel-y4lna) Malo allele Gels
5 DATA XREF: useS'/¥]_Z7N12bsp_Apexlmpl13StartFirmwareEv
3 usrStandaloneIni .
symbol <@, aAccessDescript_1, ACCESS DESCRL)-2N12bsp_Apeximpl13initBackplaneEb
symbol <0, aAccessDescript 2, ACCESS DESCf4)_ZN12bsp_Apex|mpl9lsFaultedEv
symbol <Q, aAcmAllocateele, ACM_AllocateE]#]_ZN12bsp_Apexlmpl13lsCbaAssertedEv
symbol <0, aAcmAllocatetar, ACM AllocateTéF] 7N12bsp Apeximpl13isCbbAssertedEv (cortex-A9) Spartan (backplane)
```

## Slide 37

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Move across Safety PLC backplane
Use CIP to manipulate SIS
bypass settings not exposed
outside Safety PLC
Also the usual stuff
(eg modify logic)
If we need CPU RCE
and CIP security / RUN
mode is obstacle we
Implant might need CIP parser
vuln.
No routable traffic (eg. CIP)
via PTP link
2 8
SSSR sGssssSa
: es Es
re
Depends on SIS bypass
implementation
Ethernet Module
Firmware
37
```

## Slide 38

-

-

-

-

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
e *SEVD-2023-010-05, SEVD-2023-010-06
Disclosure
> Coordinated disclosure with Schneider Electric
— Issues reported in April and July 2022
— Advisories’ released in January 2023, updated in March 2023
> CVE-2022-45788 (RCE)
— Remediations available for M580 (excluding safety), MIE
— Mitigations for others
> CVE-2022-45789 (auth bypass)
— Currently mitigations only
> We suggested retrofit fix: Secure Remote Password(SPR) + HMAC
— Auth user to PLC with SRP (zero-knowledge, MitM-resistant, discrete-log based)
— Derive HMAC key from shared SRP key K
— Sign messages with HMAC
| 39
```

## Slide 39

|•
•||
|---|---|
|•
•||
|•
•||
|•||
|•||
|•||
|||

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
(some) Mitigation, Detection, and DFIR advice
Attack Step
Wago 750 implant ¢« Alert on UMAS to non-Modicon devices
¢ Monitor Modbus TCP statistics
UMAS Auth Bypass Restrict UMAS flow to EWS (IP ACLs, FW)
(CVE-2022-45789) Look for auth request (SVC Ox38) without none exchange (SVC Ox6E)
UMAS RCE * Alert on UMAS CSA (SVC 0x50)
(CVE-2022-45788) Monitor watchdog errors
¢ Upload PLC project, extract & carve APX, look for malicious ARM
shellcode
1756-EN2T* RCE
(CVE-2019-12256)
1756-EN2T* implant
Monitor IP & assert statistics
Monitor task statistics
Task Statistics STAT
Name Entry Point ID Priority ensues
tJobTask 167208 efc4e8 0 Geatuing i .
texcTask 1269f¢ 3568 Default TL «¢ | >» For full overview,
tErffask 10b9c fOOfF70 10 *
In header errors 4
tLogTask 1e76bc f04110 0 See re ee) rt
Ill aquUQTess errors U
tNeto 1bdc8 fl1e00 50 Forwarded datagrams 0
ae - minints eminent en
* https://www.forescout.com/resources/I1-lateral-movement-report 40
```

## Slide 40





-

-



> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Conclusions
> There's likely a lot of network ‘craw! space’ that’s not on your radar
> If a LI device sits between segments, it needs a perimeter security
profile
> Stop treating certain links (serial, PTP, couplers, non-routable)
as If they’re immune
> Impact of compromise not limited to explicit link capabilities or
1st order connectivity
>» With deep access, things become possible which change
potential impact
4]
```

## Slide 41
