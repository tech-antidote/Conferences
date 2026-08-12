---
title: "Think Inside the Box In-the-Wild Abuse of Windows Sandbox in Targeted Attacks"
speakers: ["Hiroaki Hara"]
conference: "Black Hat"
conference_full: "Black Hat ASIA 2025"
edition: "ASIA"
year: 2025
source_pdf: "Black Hat Asia 2025 Slides/Hiroaki Hara_Think Inside the Box In-the-Wild Abuse of Windows Sandbox in Targeted Attacks.pdf"
pages: 33
sha256: "d8b5a7a3278b40585406d1333596fae2e1f7c2334f1a42632b1fcee486c11540"
text_chars: 13643
ocr_pages: 30
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:05:12Z"
---
# Think Inside the Box In-the-Wild Abuse of Windows Sandbox in Targeted Attacks

**Speakers:** Hiroaki Hara  
**Conference:** Black Hat ASIA 2025  
**Source:** `Black Hat Asia 2025 Slides/Hiroaki Hara_Think Inside the Box In-the-Wild Abuse of Windows Sandbox in Targeted Attacks.pdf` (33 pages)


## Slide 1

#BHAS @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Ne
pifek hat
ASIA 2025
APRIL 3-4, 2025
BRIEFINGS
Think Inside the Box
In-the-Wild Abuse of Windows Sandbox
in Targeted Attacks
Hiroaki Hara | Trend Micro
```

## Slide 2

-

-

-

#BHAS @BlackHatEvents

2

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 2025
whoami
Hiroaki Hara @ Trend Micro
Staff Engineer - Threat Research
* 10 years of experience in threat intelligence, malware analysis, and IR
¢ Presented at Virus Bulletin, Botconf, HITCON, and JSAC
¢ The first time at Black Hat Asia!!!
```

## Slide 3

#BHAS @BlackHatEvents

3

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 2025
Today's Talk
ANTI
SANDBOX
ANTI
EDR/EPP
WITH SANDBOX
```

## Slide 4

## **火車(Kasha)**

#BHAS @BlackHatEvents

4

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 2025
Earth Kasha
‘i (Kasha)
* China-aligned espionage-motivated threat actor targeting East Asia
Origin China-aligned
Motivation Espionage / Information Theft
Active Since at least 2017
Regions Japan and Taiwan (+ India)
Government, Political Organizations,
Industries Research Institute, Think Tanks, and
Researchers
aka MirrorFace by ESET
https://en.wikipedia.org/wiki/Kasha_(folk|
ore)#/media/File:SekienKasha.jpg
```

## Slide 5

2019-
2020-2021
2021-2022

#BHAS @BlackHatEvents

5

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 2025
APT10 Umbrella
* We believe that Earth Kasha is a part of “APT10 Umbrella”
APT10 Umbrella 7% S&S
APT1OM — JollyFrog ©)
“ ‘
r 2019-
2020-2021 operas r% & operate qg™
ve As.
A4A1APT Campaign Earth Tengshe & Earth Kasha y LiberalFace Campaign
relation MirrorFace (©) AkaiRyu Campaign
Gg operate
Ransomware Campaign BRONZE STARLIGHT ©
(LockFile, AtomSilo, Rook, Night Sky, Pandora)
```

## Slide 6

#BHAS @BlackHatEvents

6

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 2025
Campaign History
Spear-Phishing Spear-Phishing Exploitation Spear-Phishing
Target: © eS
Tools: | U\ae Tools: | e)»)a)\\ze) Tools: | e)2)3)\ize) Tools: PUAN Se
Target: © Target: © Target: ©
```

## Slide 7

```
_@_.zip
```

```
ScnCfg32.Exe
```

```
vsodscpl.dll
```

<RANDOM>

hello.xml hello.bin

#BHAS @BlackHatEvents

7

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 2025
The Campaign in 2024: Infection Chain
Initial Access 1st Stage Backdoor 2™ Stage Backdoor
> download
. .ZIP
OneDrive |
drop
& expand
a= —
-DOCX .ZIP
| EE
ROAMINGMOUSE _@_.zip
| ANELLDR ANEL ana NOOPDOOR
* sideload decrypt install qfj@e8 iy decrypt
@ — — O10 —— (xmMp=; —— ono
.EXE -DLL .BIN <@> _BIN
ScnCfg32.Exe vsodscpl.d1l <RANDOM> hello.xml hello.bin
```

## Slide 8

#BHAS @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bleak hat
ASIA 2025
Basics of
Windows Sandbox
#BHAS @BlackHatEvents
```

## Slide 9

#BHAS @BlackHatEvents

9

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 2025
Windows Sandbox
° Anisolated desktop environment to safely run untrusted
Windows applications using the hypervisor-based cael
virtualization technology
° Key Features
* Battery Included in OS
* No need to install VM software or download VHD
* Disposable
* No design for persistence
* Same and clean environment on every execution
* Light-weight
¢ A few seconds to launch
mo Se BCS ~ @ 8% sis
```

## Slide 10

#BHAS @BlackHatEvents

10

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 2025
-wsb
* XML-formed configuration file for Windows Sandbox
pu>Disable
g>Enable
InMB>5096
1>Enable
False
t>False
)Input>False</VideoIn
t>False<//
C:\Users\user\host_share\</H Fo
C:\Users\WDAGUtilityAccount\sandbox_share\
nly>false
C:\Windows \System32\WindowsPowerShell\v1.@\powershell.exe
10
Key Meaning
vGPU Enable or disable the virtualized GPU
Networking Enable or disable network access within the sandbox
MemoryInMB The amount of memory, in megabytes
ClipboardRedirection
Shares the host clipboard with the sandbox
PrinterRedirection
Shares printers from the host into the sandbox
ProtectedClient
Enable AppContainer isolation
Videolnput
Shares the host's webcam input into the sandbox
AudioInput
Shares the host's microphone input into the
sandbox
MappedFolders
Share folders from the host with read or write
permissions
LogonCommand
A command to execute when Windows Sandbox
starts
```

## Slide 11

#BHAS @BlackHatEvents

11

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pisek hat
ASIA 2025
Windows Security
O Virus & threat protection
Ill
Protection for your device against threats.
a
ie)
© Current threats
fo} nN
Oo
L ilable
oo)
6 Quick scan
fom] Scan options
S Allowed threats
Protection history
&
D
®@ Virus & threat protection settings
on needed
Manage settings
ce Virus & threat protection updates
enc (Cf a)
2025/03/12 '
Security intelligence is up to date
Protection updates
a)
```

## Slide 12

#BHAS @BlackHatEvents

12

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
blackhat } ee. fo
ASIA 2025 if
Defense
oO Evasion
```

## Slide 13

#BHAS @BlackHatEvents

13

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pisek hat
ASIA 2025
Abuse of Virtualization for Defense Evasion
* Not an entirely new idea
* Who Contains the Containers? - Project Zero
* Contain Yourself: Staying Undetected Using the Windows Container Isolation Framework - Deep Instinct
13
```

## Slide 14

#BHAS @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bleak hat
ASIA 2025
A Real-World Abuse
of Windows Sandbox
#BHAS @BlackHatEvents
```

## Slide 15

Windows Sandbox
schtasks default.wsb
.RAR
msiexec.bat msiexec.txt msiexec.exe msiexec.dat
C:\Users\Public\AppData (WinRAR)
C:\ProgramData
.RAR
msiexec.txt msiexec.dat
msiexec.cmd
hello.bin hello.xml

C:\Users\Public\AppData
.RAR
msiexec.bat msiexec.txt msiexec.dat

#BHAS @BlackHatEvents

15

## Slide 16

# ➊

-

#BHAS @BlackHatEvents

16

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 2025
C: \Users\Public\AppData
@ Setup
* Drop components on the host
through the ANEL backdoor channel
1010
ono 3
.BIN RAR
msiexec.bat msiexec.txt msiexec.dat
| |
PEM file password-protected RAR archive
60 01 02 03 04 05 06 O7 O08 O58 OA OB OC OD OF OF Decoded text
21 04 oo oo 6 FRR... eee...
5D 4 44 | £7 Oe |e] GUD
5A Fl ade. PIW'<é*azA(U
30 “Ga0 .NAXAZE;].a4 §
ol c'’°E. 7FA"L-.xX=a
TVqQAAMAAAAEAAAA/ / 8AAL BAAAAAARAAQAAARAAARARAAAARAAAAABRAABAAAAARA
AAAAAAAAAAAAAAAAGAE AAASF ug 4AtAnNI bgBTMehVGhpcyBwcm9ncmFtIGNhbmSv
dCBiZSBydwW4gaW4gRE9TIG1vZGUuDQOK JAAAAAAAAABTZ2CbFwYOyBcGDsgXxBg71
o5r/yBEGDsi jmv31 1QYOyKOa/MgaBg71133zyBUGDsixfQr JBQYOyJd9DckdBg7I
Hn6JyBYGDsixfQvJIQYOyBS5+ncgYBg71 FwYPyK@GDsiZfQvIXgYOyI198ceWwBg71
16
```

## Slide 17

# ➋

#BHAS @BlackHatEvents

17

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 2025
schtasks default.wsb
@ Register Windows Sandbox application as a Scheduled Task with a SYSTEM account
id="Author™
§-1-5-18 /UserId
1>LeastPrivilege</RunLevel
Context="Author"
nd>c: \windows\system3?\windows sandbox .exe
ts>c: \windows\system32\default .wsb
17
```

## Slide 18

#BHAS @BlackHatEvents

18

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 2025
Why SYSTEM?
* Since Windows Sandbox is basically a desktop application, you can hide a UI by launching sandbox with a
different user’s context
BRA =H: C\Windows\system32\cmd.exe
; < >.
BEM joe c contin wsb <LogonCommand>
Conf i guration>
Vepu>D sab | e</VGpu> <Command>cmd /c whoami > C:¥share¥whoami. txt</Command>
q Network ing>Disab|e</Networking>
MappedFolders: / \
ea MappedFo| der \ Lo onCommand 7,
sss idee HostFol der >C:¥share</HostFolder> 8
Sancho erysincborfolder 7 KK /Conf iguration>
MappedFo | der
c whoami > C:¥share¥whoami. txt</Command>
tem32¥W indowsSandbox. exe C:¥config.wsb” /sc onstart /ru SYSTEM /f
been created
C:¥>schtasks /run /tn “demo
SUCCESS: Attempted to run the scheduled task “demo”
c:¥ C:¥>schtasks /create /tn “demo “C:¥Wi stem32¥WindowsSandbox. exe C:¥config.wsb /sc onstart /ru|SYSTEM /f
oi
€ 4: G © »> ThisPC > Local Disk(C:)) > share Search share Q
® New NL Sort = View ote B Details
Narr
|
18
```

## Slide 19

# ➌

#BHAS @BlackHatEvents

19

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 2025
Windows Sandbox
configure
—>
default.wsb
© Configure the Sandbox settings
1. Enable a network from the guest (for C&C Communication)
2. Map folders with read-write permission
* Host: C:\Users
* Guest: C:\Users\WDAGUtilityAccount\Host
3. Run a batch file within the Guest
Users \WDAGUtIilityAccount\Host\Public\AppData\msiexec. batt / Command
19
```

## Slide 20

# ➍

-

-

-

#BHAS @BlackHatEvents

20

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pisek hat
ASIA 2025
ae % il extract
F .RAR mars
-BIN .EXE
msiexec.bat msiexec.txt msiexec.exe msiexec .dat
(WinRAR)
@ Execute an installer script (msiexec.bat)
* Decode PEM file (msiexec.txt) by using certutil and save as “msiexec.exe” which turns out to be WinRAR
command-line tool
¢ Extract payload components compressed within password-protected RAR archive
¢ Execute launcher script to install payloads (msiexec.cmd)
msiexec.bat
20
```

## Slide 21

# ➎

-

-

#BHAS @BlackHatEvents

21

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 2025
Windows Sandbox
msiexec. cmd hello.xml hello.bin
@ NOOPDOOR Installation
* Rename and move components
¢ Register the loader of NOOPDOOR (hello.xml) as scheduled task
msiexec.cmd
/create /tn Hello , ‘ iy am suilc Cr \Wi : vents xml") /sc minute /mo 5 /st 68:05 /ru System /f
run /tn Hello
21
```

## Slide 22

#BHAS @BlackHatEvents

22

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 2025
Wrap Up
° Executed Windows Sandbox with SYSTEM account to hide a UI
* Granted a read-write permission from the sandbox to the host machine
° Utilized a password-protected archive containing payload components and expanded them
only within a sandbox
od
Executed a payload only within a sandbox
without being affected by EPP/EDR on the host
22
```

## Slide 23

#BHAS @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bleak hat
ASIA 2025
Detection
Engineering
#BHAS @BlackHatEvents
```

## Slide 24

#BHAS @BlackHatEvents

24

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 2025
Existing Research
* Hack The Sandbox: Unveiling the Truth Behind Disappearing Artifacts - ITOCHU Cyber & Intelligence
* TTPs and Detections for Windows Sandbox Abuse - Japan National Police Agency
24
```

## Slide 25

-

-

-

-

-

-

-

-

#BHAS @BlackHatEvents

25

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pisek hat
ASIA 2025
Basic Components
RPC RPC 2° launch oe
— — Xe)) ©
WindowsSandbox.exe Container Service Manager Hyper-V Host Compute Service Virtual Machine Worker Process
(CmService.dll) (vmcompute.exe) (vmwp.exe)
¢ Entry point of Windows ¢ Setup the base layer * Create a container based on * Control Guess Sandbox
Sandbox * Analyze configuration the parsed configuration * Load Guest components
* Read “.wsb” file * Run and orchestrate worker
process
25
```

## Slide 26

|**Command**|**Action**|
|---|---|
|wsb.exe start|creates and launches a new sandbox|
|wsb.exe list|displays a table that shows the information the running Windows
Sandbox sessions for the current user|
|wsb.exe connect --id <sandbox ID>|starts a remote session within the sandbox|
|wsb.exe exec --id <sandbox ID> --command “cmd.exe" --run-as ExistingLogin|executes a command in the sandbox|
|wsb.exe stop --id <sandbox ID>|stops a running Windows Sandbox session|

#BHAS @BlackHatEvents

26

## Slide 27

#BHAS @BlackHatEvents

27

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 2025
wsb.exe: Another Entrypoint
* “wsb start” command has an argument “-config/-c” for inline configuration
° This feature offers a fully fileless execution and a hidden UI in the current user session
C:\Users\john>wsb start —-config "<Configuration><LogonCommand><Command>cmd .exe</Command></LogonCommand></Configuration>"
Windows Sandbox environment started successfully:
Id: 1cb9e300-cec5-U3fe-8ee9-—c7c25FfOcd37b
27
```

## Slide 28

```
title: Windows Sandbox Execution with SYSTEM Privileges
description: This rule is designed to detect possible Windows
Sandbox abuse by SYSTEM privileged execution which enables the
adversary to hide UI of sandbox.
```

```
logsource:
```

```
category: process_creation
product: windows
service: sysmon
```

```
detection:
selection:
EventID: 1
Image|endswith: 'Windows\System32\WindowsSandbox.exe'
User: 'NT AUTHORITY\SYSTEM'
condition: selection
```

```
falsepositives:
```

```
-Legitimate administrative use
level: high
```

```
title: Execution of wsb.exe with Suspicious Configuration
status: experimental
description: Detects the execution of wsb.exe with --config or -c
parameter containing "<LogonCommand>", which could indicate an attempt
to execute a command inside Windows Sandbox.
```

```
logsource:
```

```
category: process_creation
product: windows
service: sysmon
```

```
detection:
selection:
```

```
EventID: 1
Image|endswith: 'AppData\Local\Microsoft\WindowsApps\wsb.exe'
CommandLine|contains:
```

```
-'--config'
```

```
-'-c'
CommandLine|contains: '<LogonCommand>'
condition: selection
falsepositives:
```

- `Legitimate use of Windows Sandbox with specific LogonCommand`

- `settings level: low`

#BHAS @BlackHatEvents

28

## Slide 29

#BHAS @BlackHatEvents

29

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 2025
Prevention: Group Policy
' Local Group Policy Editor — oO x
File Action View Help
¢9%/2m/8\bm|7
| Windows Game Recon Windows Sandbox
| Windows Hello for Bus
Windows Ink Workspa Select an item to view its description. Setting State
Windows Installer i) Allow audio input in Windows Sandbox Not configured
Windows Logon Optic | Allow clipboard sharing with Windows Sandbox Not configured
| Windows Media Digita i=, Allow mapping folders into Windows Sandbox Not configured
Windows Media Player i=) Allow networking in Windows Sandbox Not configured
Windows Messenger 5) Allow printer sharing with Windows Sandbox Not configured
Windows Mobility Cer i=] Allow vGPU sharing for Windows Sandbox Not configured
Windows PowerShell | Allow video input in Windows Sandbox Not configured
Windows Reliability Ar
Windows Remote Mar
Windows Remote Shel
| ~) Windows Sandbox|
Windows Security
\\ Extended A Standard /
7 setting(s)
29
```

## Slide 30

OS process
Windows 10 vmmem
Windows 11 vmmemSandbox

#BHAS @BlackHatEvents

30

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 2025
Another Detection Chance: Memory
* Process image to manage CPU resource, memory and resources for the Guest Sandbox
os process
Windows 10 vmmem
Windows 11 vmmem Sandbox
* Memory space for the Guest is exposed to the Host
Yara memory scan successfully works
C:\Users\john\Desktop>tasklist | find "vmmemSandbox"
vmmemSandbox 7152 Services © 1,426,804 K
C:\Users\john\Desktop>yara64.exe kiwi_passwords.yar 7152
mimikatz 7152
power_pe_injection 7152
30
```

## Slide 31

#BHAS @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
- blaekhat:
ASIA 2025
Conclusion
#BHAS @BlackHatEvents
```

## Slide 32

#BHAS @BlackHatEvents

32

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 2025
Summary
° Adversaries always “think outside the box”, but a lot of chances to detect them
° What's next?
° Besides Windows, *NIX systems are more container-friendly, which means that they are good
targets
° Developers can be easy targets
* Container abuse has been already reported in the attack against ByBit
* Next: Contagious Interview Campaign?
32
```

## Slide 33

#BHAS @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
- blaekhat:
ASIA 2025
Questions?
#BHAS @BlackHatEvents
```
