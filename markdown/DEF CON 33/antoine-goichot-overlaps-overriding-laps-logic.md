---
title: "OverLAPS Overriding LAPS Logic"
speakers: ["Antoine Goichot"]
conference: "DEF CON"
conference_full: "DEF CON 33"
edition: "33"
year: 2025
source_pdf: "DEF CON 33/Antoine Goichot - OverLAPS Overriding LAPS Logic.pdf"
pages: 46
sha256: "c3951a12c2fbdf30cf237f92ff64623c40d4ecf06a7fc40bc7938ea8807d3302"
text_chars: 19699
ocr_pages: 2
has_ocr: true
redacted_secrets: 0
ocr_confidence: 82.9
ocr_unreliable_blocks: 1
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T06:52:48Z"
---
# OverLAPS Overriding LAPS Logic

**Speakers:** Antoine Goichot  
**Conference:** DEF CON 33  
**Source:** `DEF CON 33/Antoine Goichot - OverLAPS Overriding LAPS Logic.pdf` (46 pages)


## Slide 1

OverLAPS: Overriding LAPS Logic

**Antoine Goichot** DEF CON 33, August 2025

## Slide 2

##### From Dijon (Burgundy, France) to DEF CON

###### **Antoine Goichot**

- Born and raised in Dijon, France – _yep, the mustard one._

- **Pentester (consulting)** @ PwC Luxembourg – 10 years of breaking things

- • CVEs:

   - Cisco AnyConnect for Windows: CVE-2020-3433, CVE-2020-3434, CVE-2020-3435, CVE-2020-27123, CVE-2021-1427

   - Ivanti Secure Access Client for Windows: CVE-2023-38042

- Previous talk:

_Malicious use of Microsoft “Local Administrator Password Solution”_ , Hack.lu, October 2017, with Maxime Clementz

**PwC**

2

## Slide 3

##### **1** Foreword & Vocabulary **2** Introduction: LAPS Overview

- **3** Background & Objectives **4** Scope & Infrastructure **5** Dissecting Windows LAPS **6** Conclusion

## Agenda

**PwC**

OverLAPS: Overriding LAPS Logic   |   Agenda

3

## Slide 4

### Foreword & Vocabulary

**PwC**

OverLAPS: Overriding LAPS Logic   |   Foreword & Vocabulary

4

## Slide 5

##### Microsoft LAPS vs. Windows LAPS

##### **LAPS = Local Administrator Password Solution**

**Microsoft LAPS** (in this talk: Legacy / LAPSv1)

**Windows LAPS** (in this talk: Current / LAPSv2)

- Released in  2015

   - Released in 2023

- AD only

   - AD **or Entra ID**

- On DC: installation & config

   - On DC / Entra: only config

- .msi package installation on managed clients

   - **Native support** on managed clients

- Passwords stored in **clear text** in AD attributes

- Status:

   - **Encrypted password** storage and **history** support in AD _(Can mange DSRM account, but not covered here)_

- **Deprecated** starting with Windows 11 23H2 and later

   - Supported

- For older versions, support ends with the OS’s EoL

**PwC**

OverLAPS: Overriding LAPS Logic   |   Foreword & Vocabulary

5

## Slide 6

Introduction: LAPS Overview

**PwC**

OverLAPS: Overriding LAPS Logic   |   LAPS Overview

6

## Slide 7

##### High level operation

**LAPS (v1 & v2) run the same high-level process during each cycle:**

1. Generate a new local administrator password

2. Store the password in the directory

3. Set the password locally on the device

**On AD, resetting LAPS password = setting expiration time to ‘now’ and wait for a new cycle**

**PwC** OverLAPS: Overriding LAPS Logic   |   LAPS Overview

7

## Slide 8

##### Microsoft LAPS (Legacy / v1)

- Managed device = domain-joined device (with `.msi` installed)

- Client-Side group policy Extension (CSE): Poling cycle = Group Policy refresh cycle

- On managed device: 1 DLL `%ProgramFiles%\LAPS\CSE\AdmPwd.dll`

- Password and expiration time stored in AD (Computer object)

- Password protected by ACL only (stored in clear text):

   - Only authorized users can read the password

   - Everyone can read expiration time

Computer account in AD
...
Admin password
Support staff
Pwd Expiration Time
...
Active Directory
  Managed machine
GPO Framework
...
SceCli.dll
AdmPwd.dll

_Source: LAPS_Datasheet.docx_ _<u>(https://www.microsoft.com/en-us/download/details.aspx?id=46899)</u>_

**PwC**

OverLAPS: Overriding LAPS Logic   |   LAPS Overview

8

## Slide 9

##### Windows LAPS (Current / v2)

- Managed device = domain-joined device OR Entra-joined device

- Not a CSE , but does respond to Group Policy change notifications and to `Invoke-LapsPolicyProcessing` PS cmdlet

- Hard-coded polling cycle: once per hour

- On managed device: 3 main DLLs (native support) `%windir%\System32\laps.dll` – Core logic `%windir%\System32\lapscsp.dll` – CSP logic `%windir%\System32\WindowsPowerShell\v1.0\Modules\ LAPS\lapspsh.dll` – PowerShell cmdlet logic

- AD: password protected both by **encryption** & **ACL**

- Entra: password “further encrypted” at rest & ACL

_Source:_ _<u>https://learn.microsoft.com/en-us/windows-server/identity/laps/lapsconcepts-overview</u>_

- Password tampering protection on local system

**PwC** OverLAPS: Overriding LAPS Logic   |   LAPS Overview

9

## Slide 10

### Background & Objectives

**PwC**

OverLAPS: Overriding LAPS Logic   |   Background & Objectives

10

## Slide 11

##### Background

- LAPS (v1 & v2) have been widely analyzed, with **many tools and articles available**

- However, most attacks focus on abusing accounts authorized to read passwords

- “Client-side” remain **largely unexplored** in public tooling and research

- **This observation is not new.** We studied the clientside of Microsoft LAPS (v1) back in 2017

- TL;DR: LAPS v1 is based on an open-source project, AdmPwd, and is backward compatible

**PwC**

OverLAPS: Overriding LAPS Logic   |   Background & Objectives

11

## Slide 12

##### Eight Years Later…

###### **Several protections and major changes have been introduced:**

- No longer based on open-source code

- Support for Entra ID alongside Active Directory

- Passwords stored with encryption

- Password tampering protection mechanisms

**In this context, we would like to explore the following** **<u>questions:</u>**

Can the LAPS password be **captured** every time it changes or resets?

Is it possible to **desynchronize** the local password from the one stored “server-side”? Can a password **change** be triggered on demand?

**PwC**

OverLAPS: Overriding LAPS Logic   |   Background & Objectives

12

## Slide 13

### Scope & Infrastructure

**PwC**

OverLAPS: Overriding LAPS Logic   |   Scope & Infrastructure

13

## Slide 14

##### Scope & Labs

###### **Scope**

- Focus exclusively on Windows LAPS (v2) _– Microsoft LAPS (v1) being deprecated anyway_

- Encryption enabled: Legacy compatibility not studied

- Cryptography details are out of scope _– see XPN’s blog post in references for more_

###### **Minimalist Labs infrastructure**

In both infra:

- Client = Windows 11, 24H2, 64-bit system

- LAPS is used to manage the built-in local admin account

- **LSA Protection (RunAsPPL) is disabled**

**PwC**

OverLAPS: Overriding LAPS Logic   |   Scope & Infrastructure

14

## Slide 15

### Dissecting Windows LAPS

**PwC**

OverLAPS: Overriding LAPS Logic   |   Dissecting Windows LAPS

15

## Slide 16

##### Exploring laps.dll

As mentioned, 3 main DLLs on clients:

- `laps.dll` – Core logic

- `lapscsp.dll` – CSP logic

- `lapspsh.dll` – PowerShell cmdlet logic

D i scla i mer:
I am not a Reverse Eng i neer
It was easier in 2017 with AdmPwd source code
way

**Luckily, Windows debugger symbols (.pdb) make it easier to understand the logic and function names**

**PwC**

OverLAPS: Overriding LAPS Logic   |   Dissecting Windows LAPS

16

## Slide 17

##### Under the hood of LAPS

_For reference, studied version: 10.0.26100.4202, signed (June 2025) SHA-1:_ _`2332A88D495808A5465A22494B93FB49A8F67A02`_

AD only Entra ID only

**PwC** OverLAPS: Overriding LAPS Logic   |   Dissecting Windows LAPS

17

## Slide 18

Frida is an open-source toolkit that lets you inject custom scripts into running processes for realtime analysis and manipulation <u>(https://frida.re/)</u>

**PwC** OverLAPS: Overriding LAPS Logic   |   Dissecting Windows LAPS

18

## Slide 19

##### `samsrv.dll!SamISetPasswordForeignUser2`

**Exported function – SAM Server DLL**

\```
SamISetPasswordForeignUser2(0,0x200,&local_18,&local_28,0,0,0);
\```

**Username Password (args[2]) (args[3])**

**Password!**

**PwC**

OverLAPS: Overriding LAPS Logic   |   Dissecting Windows LAPS

19

## Slide 20

\```
samsrv.dll!SamISetPasswordForeignUser2
\```

1_SamISetPasswordForeignUser2_get_password.mp4 00:01:07

**PwC**

OverLAPS: Overriding LAPS Logic   |   Dissecting Windows LAPS

20

## Slide 21

\```
laps.dll!AccountManager::ResetLocalAdminAccountPassword
\```

**With Frida, we can also trace internal functions,** we just need the function's offset and to find interesting parameters. `ResetLocalAdminAccountPassword(AccountManager *this, LocalAdminAccount *param_1,` **`longlong param_2`** `, undefined8 param_3)`

**Offset**

**PwC**

OverLAPS: Overriding LAPS Logic   |   Dissecting Windows LAPS

21

## Slide 22

###### `laps.dll!AccountManager::ResetLocalAdminAccountPassword`

**PwC**

OverLAPS: Overriding LAPS Logic   |   Dissecting Windows LAPS

22

## Slide 23

###### **Status of objective**

Can the LAPS password be captured? AD: ✓

Entra ID: ✓

**PwC**

OverLAPS: Overriding LAPS Logic   |   Dissecting Windows LAPS

23

## Slide 24

##### LAPS desync: two options

###### **#1: Modify the local password**

- The password on the directory will be **random** & we **maintain control over the actual** local admin password

- **#2: Modify the directory password**

- Limited impact when used alone: the actual local admin password remains random and unknown.

**PwC**

OverLAPS: Overriding LAPS Logic   |   Dissecting Windows LAPS

24

## Slide 25

##### LAPS desync

OverLAPS: Overriding LAPS Logic   |   Dissecting Windows LAPS

**PwC**

25


> Recovered by OCR — confidence 91/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
LAPS desync
5671 ms
5671 ms
5671 ms
Local Administrator Password Solution
Account name Current LAPS password expiration:
Administrator Wednesday, 30 July 2025 13:10
Security ID
Set new LAPS password expiration:
S-1-5-21-2970840996-3213091915-706289186-500 Wednesday, July 30,2025 1:10 pm
Local administrator password alice
KOS
Last password rotation LAPS local admin account password:
6/30/2025, 3:44:29 PM Yeah.Random123|
Next password rotation :
Copy password Hide password
7/7/2025, 3:44:29 PM
PwC OverLAPS: Overriding LAPS Logic | Dissecting Windows LAPS
LAPS local admin account name:
Administrator
LAPS local admin account password:
iy Expire now
25
```

## Slide 26

###### **Status of objective**

Is it possible to desync. LAPS password? AD: ✓

Entra ID: ✓

**PwC**

OverLAPS: Overriding LAPS Logic   |   Dissecting Windows LAPS

26

## Slide 27

##### Forcing a LAPS password rotation

YES, OF COURSE
IT’S EXPIRED.

**PwC**

OverLAPS: Overriding LAPS Logic   |   Dissecting Windows LAPS

27

## Slide 28

`laps.dll!LapsCore::CheckADPasswordUpdateFactors` (AD) & `laps.dll!LapsCore::CheckAzurePasswordUpdateFactors` (Entra)

###### **We hook the functions** **`CheckADPasswordUpdateFactors` (AD) &** **`CheckAzurePasswordUpdateFactors` (Entra) before they return, and modify a parameter.**

**PwC**

OverLAPS: Overriding LAPS Logic   |   Dissecting Windows LAPS

28

## Slide 29

`laps.dll!LapsCore::CheckADPasswordUpdateFactors` (AD)

2_CheckADPasswordUpdateFactors_reset_password.mp4  00:00:42

**PwC**

OverLAPS: Overriding LAPS Logic   |   Dissecting Windows LAPS

29

## Slide 30

##### Forcing a LAPS password rotation – Entra ID

_Source:_ _<u>https://learn.microsoft.com/en-us/windows-server/identity/laps/lapsconcepts-overview#background-policy-processing-cycle</u>_

**PwC** OverLAPS: Overriding LAPS Logic   |   Dissecting Windows LAPS

30

## Slide 31

##### Forcing a LAPS password rotation – Entra ID

**What if we change the** **`AzurePasswordExpiryTime` key? It can’t be that simple, right? Right?**

_Note: additional registry values related to post-authentication actions can be found under this key._

OverLAPS: Overriding LAPS Logic   |   Dissecting Windows LAPS

**PwC**

31

## Slide 32

\```
HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\LAPS\State
\```

3_Registry_Entra_reset_password.mp4

00:01:01

**PwC**

OverLAPS: Overriding LAPS Logic   |   Dissecting Windows LAPS

32

## Slide 33

Schrödinger’s LAPS password

**PwC** OverLAPS: Overriding LAPS Logic   |   Dissecting Windows LAPS

33


> Recovered by OCR — confidence 75/100 on the text kept, 71/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
@ E
microsoft.com, "
File Action View Help
Microsoft Intune admin center ot #9 28
» “ \ wy - 4 . > Operational Number of events: 164 ‘Actions
Home > Devices | Overview > Windows | Windows devices > LAPS | @@al administrator password ' saa a
. Level Date and Time Source Event ID Task Catego! perati..
: @ Information 13/07/2025 16:14:38 LAPS 10004 None 5 Op.
~ Account name ) @ information 13/07/2025 16:14:38 LAPS 10016 None ¥ Cre.
O Search ] ©) Refresh 2 Got fe Ad > @ Information 13/07/2025 16:14:38 LAPS 10052 None Im.
@© Overview @ Learn more about Local Security ID > )) Information 13/07/2025 16:14:38 LAPS 10022 None Cle..
\ Manage $-1-5-21-2970840996-3213091915-706289186-500 > @ Information 13/07/2025 16:14:38 LAPS 10003 None Y Fit.
Local administrat Local administrator password : Information 06/07/2025 06:11:02 LAPS 10004 None (2) Pro.
+ Properties Oca BcirminIsITAIOF PASS. P > ) Information 08/07/2025 06:11:02 LAPS 10016 None ~
\”_ Monitor Show local administrator pé |
> Fin..
Last password rotation > Event 10016, LAPS x fay sav.
6/30/2025, 4:19:05 PM >
Next password rotation
View >
7/7/2025, 4:19:05 PM > | The managed account password does not need to be updated at this time.
A. This password has expired ; See httns://qo.microsoft.com/fwlink/2linkid=2220550 for more information.
>
; Source: LAPS Logged: 13/07/2025 16:14:38
5 Event ID: 10016 Task Category: None
: Level: Information Keywords:
User: SYSTEM Computer, —_LAPS-W11
Operations Recipe @ BS Input
BB Registry Editor a
1f7637e05cfe600 File Edit View Favorites Help
Fork - Ol 41dbe9c9efoeg62f Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\LAPS\State
fork Hints Name Type Data
Split delimiter > “SIME ab|(Default) REG_SZ (value not set)
Fork mec 31 = 2 Tr Raw Bytes © LF > = Installers jii)AzurePasswordExpiryTime REG_QWORD 0x1f7637e05cfe600 (141691306200000000) _|
2 $i1]DSRMMode REG_DWORD 0x00000000 (0)
Public K Merge delimiter ir ra remet Sett #1) LastAccountRidUpdated REG_DWORD 0x000001f4 (500)
ublic Key \n Output a O ES} hot LanguageCo | 9; LastPasswordUpdateTime REG_QWORD 0x1 dbe9c9ef0e962f (133957667445970479)
Confi
Key Sat 1 January 2050 13:37:00 UTC a
O Ignore errors Mon 30 June 2025 14:19:04 UTC SP tach cornan
Argon2
ENG 16:44
PwC OverLAPS: Overriding LAPS Logic | Dissecting Windows LAPS
```

## Slide 34

###### **Status of objective**

Can we force a password change? AD: ✓

Entra ID: ✓

**PwC**

OverLAPS: Overriding LAPS Logic   |   Dissecting Windows LAPS

34

## Slide 35

Frida is great, but what if we can’t use it?

**PwC**

OverLAPS: Overriding LAPS Logic   |   Dissecting Windows LAPS

35

## Slide 36

##### Microsoft Detours

Detours is a Microsoft-developed open-source library used to intercept and modify Win32 API calls in Windows applications (https://github.com/microsoft/Detours)

The approach is quite straightforward:

Diagrams redrawn based on: <u>https://github.com/microsoft/detours/wiki/OverviewInterception</u>

**1. Define a function** with the same signature as the target function (e.g., which **captures the LAPS password** ) that will be called before **calling the original** function.

**2. Attach the hook** when the DLL is loaded, and detach it upon unloading.

**PwC**

OverLAPS: Overriding LAPS Logic   |   Dissecting Windows LAPS

36

## Slide 37

##### Hijacking LAPS via Microsoft Detours

4_Detours.mp4  00:00:45

**PwC**

OverLAPS: Overriding LAPS Logic   |   Dissecting Windows LAPS

37

## Slide 38

### Conclusion

**PwC**

OverLAPS: Overriding LAPS Logic   |   Conclusion

38

## Slide 39

Can we hook other functions for similar results? Yes.

And probably a bunch more too.

#### Would you like some passwords?

**PwC**

OverLAPS: Overriding LAPS Logic   |   Conclusion

39

## Slide 40

_Safe from Oops, not from Ops: intentional & careful tampering only, please!_

_Source:_ _<u>https://learn.microsoft.com/en-us/windows-server/identity/laps/laps-concepts-overview</u>_

OverLAPS: Overriding LAPS Logic   |   Conclusion

**PwC**

40

## Slide 41

Overriding LAPS Logic: Mission Accomplished? Still a Lot to Explore _Foundations laid, paths wide open_

- ✓ Capture the LAPS password during resets or changes

- ✓ Desynchronize the local password from what’s stored in the directory

- ✓ Force password changes on demand

**Going further**

- **“Messing” with LSASS remains the real challenge (RunAsPPL, EDR, etc.)**

- •This talk and the PoCs aimed to highlight the under-studied client-side logic of LAPS – and will hopefully spark some ideas!

**PwC**

OverLAPS: Overriding LAPS Logic   |   Conclusion

41

## Slide 42

Some unsolicited advice _I’m a Consultant, after all_

###### **Red Teamers – Be creative!**

- Think beyond the PoCs: try retrieving the password via the network, or explore other scenarios

- Numerous functions can be hooked or abused

- Offsets and internal logic may change with updates

###### **Blue Teamers**

- Monitor for unexpected LAPS password resets. If LAPS isn’t actively used, resets should align with the configured rotation period

- Watch for and limit privilege escalations – our scenarios assume post-compromise. Stopping the initial access prevents it

- Ensure technical controls like RunAsPPL, EDR, etc., are properly deployed and active

**PwC**

OverLAPS: Overriding LAPS Logic   |   Conclusion

42

## Slide 43

# Thank you!

**www.pwc.lu**

**<u>https://www.linkedin.com/in/antoinegoichot/</u>**

**PoCs & Scripts (retrieving PDB and offsets):** **<u>https://github.com/goichot/OverLAPS</u>**

© 2025 PricewaterhouseCoopers Tax and Avisory, Société coopérative. All rights reserved. In this document, “PwC” or “PwC Luxembourg” refers to PricewaterhouseCoopers  Tax and Avisory, Société coopérative which is a member firm of PricewaterhouseCoopers International Limited, each member firm of which is a separate legal entity. PwC IL cannot be held liable in any way for the acts or omissions of its member firms.

**PwC**

## Slide 44

##### Food for thought and personal to-do list (aka maybe useless ideas)

Ideas to bypass LSA Protection and load a custom DLL:

- Bring Your Own Vulnerable Driver (BYOVD)

- Bring Your Own Vulnerable DLL (itman’s PPLrevenant)

- Leveraging COM (James Forshaw, Slowerzs’ PPLSystem & T3nb3w’s ComDotNetExploit)

- Malicious Security Support Provider (SSP)

- Verifier DLL

- etc.

**PwC**

OverLAPS: Overriding LAPS Logic   |   References

44

## Slide 45

##### References (1/2)

Microsoft documentation on Windows LAPS:

- What is Windows LAPS? – <u>https://learn.microsoft.com/en-us/windows-server/identity/laps/laps-overview</u>

- Key concepts in Windows LAPS – <u>https://learn.microsoft.com/en-us/windows-server/identity/laps/laps-concepts-overview</u>

Existing attacks and tools:

- HackTricks page on LAPS – <u>https://book.hacktricks.wiki/windows-hardening/active-directory-methodology/laps.html</u>

- Karl Fosaaen (kfosaaen)’s post, _Running LAPS Around Cleartext Passwords_ – <u>https://www.netspi.com/blog/technical-blog/network-penetration-testing/runninglaps-around-cleartext-passwords/</u>

- Karl Fosaaen (kfosaaen) “Get-LAPSPasswords” PowerShell script – <u>https://github.com/kfosaaen/Get-LAPSPasswords</u>

- Leo Loobeek (leoloobeek) “LAPSToolkit” PowerShell script – https://github.com/leoloobeek/LAPSToolkit

- Adam Chester (XPN)’s post, _LAPS 2.0 Internals_ – <u>https://blog.xpnsec.com/lapsv2-internals/</u>

- BloodHound "ReadLAPSPassword" page – <u>https://bloodhound.specterops.io/resources/edges/read-laps-password</u>

- NetExec LAPS module – https://github.com/Pennyw0rth/NetExec/blob/main/nxc/modules/laps.py

**PwC**

OverLAPS: Overriding LAPS Logic   |   References

45

## Slide 46

##### References (2/2)

###### Tools & Frameworks:

- Frida – Ole André Vadla Ravnås – https://frida.re/

- Ghidra – NSA – <u>https://ghidra-sre.org/</u>

- Detours by Microsoft – https://github.com/microsoft/Detours

###### Earlier work & Reference materials:

- Maxime Clementz and Antoine Goichot, _Malicious use of “Local Administrator Password Solution”_ , Hack.lu, October 2017 – <u>http://archive.hack.lu/2017/HackLU_2017_Malicious_use_LAPS_Clementz_Goichot.pdf | https://www.youtube.com/watch?v=opSctm4L8kE</u>

- Microsoft security advisory: Local Administrator Password Solution (LAPS) now available: May 1, 2015 – <u>https://support.microsoft.com/en-us/topic/microsoftsecurity-advisory-local-administrator-password-solution-laps-now-available-may-1-2015-404369c3-ea1e-80ff-1e14-5caafb832f53</u>

- LAPS Operations Guide, LAPS Technical Specification – https://www.microsoft.com/download/details.aspx?id=46899

- Local admin password management solution MSDN Code Gallery page (archive from September 2017) – <u>https://web.archive.org/web/20170929223316/https://code.msdn.microsoft.com/Solution-for-management-of-ae44e789</u>

- Jiri Formacek (jformacek) from GreyCorbel, "AdmPwd" solution (release 5.2.0) – https://github.com/GreyCorbel/admpwd/releases/tag/v5.2.0

**PwC**

OverLAPS: Overriding LAPS Logic   |   References

46
