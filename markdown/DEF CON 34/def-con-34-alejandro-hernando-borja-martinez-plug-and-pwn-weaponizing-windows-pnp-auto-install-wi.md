---
title: "Plug And Pwn Weaponizing Windows PnP Auto-Install"
speakers: ["Alejandro Hernando", "Borja Martinez"]
conference: "DEF CON"
conference_full: "DEF CON 34"
edition: "34"
year: null
source_pdf: "DEF CON 34/DEF CON 34 - Alejandro Hernando, Borja Martinez - Plug And Pwn Weaponizing Windows PnP Auto-Install - Wi.pdf"
pages: 43
sha256: "5c5fe1701291af05a429574aa75e9e9ad185c78094fe9cc0ac4cb9105665f545"
text_chars: 22201
ocr_pages: 29
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T00:11:42Z"
---
# Plug And Pwn Weaponizing Windows PnP Auto-Install

**Speakers:** Alejandro Hernando, Borja Martinez  
**Conference:** DEF CON 34  
**Source:** `DEF CON 34/DEF CON 34 - Alejandro Hernando, Borja Martinez - Plug And Pwn Weaponizing Windows PnP Auto-Install - Wi.pdf` (43 pages)


## Slide 1

# Plug&Pwn: Weaponizing Windows PnP

Alejandro Hernando @0xedh & Borja Martínez @borjmz

## Slide 2

0xedh@defcon34:~$ whoami

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Oxedh@defcon34:~$ whoami
- Oxedhadefcon34
// Alejandro Hernando / @0xedh
//
//
//
//
//
//
//
//
//
//
Red team and researcher in the Hacking Accenture
Spain team.
I like to break things in my free time
and spend money on gadgets.
Github: @0xedh
Telegram: @edhx0
Twitter: @0xedh
```

## Slide 3

borjmz@defcon34:~$ whoami

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
borjmz@defcon34:~$ whoami
- bor jmzadefcon34
// Borja Martinez / @borjmz
//
// Red team and researcher in the Hacking Accenture
// Spain team.
//
// From time to time I play the occasional CTF
// and was part of the ID-10-T (Retired) team.
//
// Telegram: @borjmz
// Twitter: @Qm9yamFN
// Github: @borjmz
```

## Slide 4

## “Physical” access -> SYSTEM. No clicks.

What you're about to watch, side by side:

**Left - the target** Windows 11, fully updated

**Right - us** Linux + a FaceDancer

No user logged on. Nothing pre-installed. A clean, patched machine.

Our exploit chain: emulate two USB devices, hijack DNS through PIPE, plant a DLL, load it as SYSTEM.

## Slide 5

POC_0 - First exploit chain

## Slide 6

## Why a pile of "minor" bugs ends in SYSTEM

- We chain low-severity bugs, across vendors, into one critical.

- On their own they're minor. Some vendors won't even call them vulnerabilities. Chained the right way, together they hand us arbitrary code execution as SYSTEM.

#### **1 - Sierra Wireless**

#### **2 - Sony FeliCa**

#### **3 - Then …**

EM7340 modem utility NFC reader co-installer SwiService.exe runs as pulls its files over HTTP SYSTEM

Doing it remotely. No hardware.

## Slide 7

Sierra Wireless “SwiService.exe (1/2)”

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Sierra Wireless “SwiService.exe (1/2)”
r
43 local_b®@ = GetTickCount64();
44 if (param_1[3] == 0) {
45 BVar3 = InitializeSecurityDescriptor(local_90,1) ;
46 if (BVar3 != @) {
47 pwVar9 = (wchar_t *)@xQ;
48
49 BVar3 = SetSecurityDescriptorDacl(local_90,1, (PACL)0x0,@) ;
50 if (BVar3 != @) {
51 local_d@.nLength = 0x18;
52 local_d®.1pSecurityDescriptor = local_90;
// Exposes a named pipe with an Everyone r/w ACL. |
r
pvVarl2 = CreateNamedPipeW(param_2,0x40000003 ,6,Oxff,param_4,0,5000,
&local_d@Q) ;
if (pvVar12 == (HANDLE) OxffffffffffffffTF) {
GetLastError();
pwVar9 = L"Failed to create named pipe [%s]. Err - %d";
lpHandles = (HANDLE *)@x3;
FUN_140087070(6,3,L"Failed to create named pipe [%s]. Err - %d",param_2) ;
}
// Any local user or any domain user can connect and
// call SetDNS function remotely.
```

## Slide 8

Sierra Wireless “SwiService.exe (2/2)”

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Sierra Wireless “SwiService.exe (2/2)”
// The executable is hardcoded to netsh.
// The interface name comes from a system lookup.
89 local_12d@ = local_10b8;
90 local_12d8 = *(undefined4 **)((longlong)pvVar2 + 0x48) ;
91 FUN_140014940(1local_838,0x400,L"interface ipv%d add dns \"%s\" %s", (ulonglong) uVar8) ;
92 FUN_1400027c0( (undefined (*) [16])L"netsh.exe", local_838,0,1);
93 }
94 else {
95 if ((bool)*(char *)(param_1 + 1) != (iVar3 == @)) {
96 uVar8 = uVar9;
97 }
98 FUN_140087070(6,3,L"Error retrieving IPv%d address string", (ulonglong)uVars) ;
99 }
100 GlobalFree(local_12bQ) ;
// The intended effect, point DNS at any IP (under our control).
```

## Slide 9

SONY + SIERRA - Sierra recap

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
SONY + SIERRA - Sierra recap
1 emulate Sierra EM?734@ 1199:Ag88 SIERRA
SwiService.exe (SYSTEM) opens a NULL-DACL pipe \\.\pipe\SwiServicePipe -
Everyone R/W, local or over SMB/4d45
Vv
2 call SetDns (msg type 9) -> hijack DNS SIERRA
service runs netsh ... add dns as SYSTEM -> machine ONS = attacker;
FlushONS (type 8) for instant effect
Vv
3 attacker serves ONS
wuu.sony.,co.jp -> attacker IP; everything else -> 8.8.8.8
```

## Slide 10

Sony Felica “felica_coinst.dll (1/2)”

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Sony Felica “felica_coinst.dll (1/2)”
r
19 /* 0x7334 1 ClassInsatller
20 0x7334 2 ClassInstaller
21 This is not my typo! Sony's own typo in the export table. */
22 local_d8 = Oxfffffffffffffffe;
23 local_28 = DAT_@202a1b8 “ (ulonglong) auStackY_138;
24 local_e8 = (longlong *)FUN_020077b8() ;
25 local_e@ = Q;
26 FUN_02006c90();
27 DAT_0202bfc® = param_2;
28 DAT_0202bfc8 = param_3;
29 if (param_1 == @xle) {
30 /7* Runs the orchestrator as SYSTEM. It downloads config
31 files and writes them to disk.
32 This is where path traversal triggers */
33 puVar4 = (undefined *)ORCHESTRATOR_DOWNLOAD( ) ;
r
142 iVar2 = FUN_02013a90((longlong) &local_548) ;
143 if (iVar2 == 0) {
144 puVar5 = URL_STRING_2(&local_548) ;
145 std: :basic_string<>: :assign(local_220, (basic_string<> *)puVar5,0, OxfffffffffffffTTF) ;
146 if (@xf < local_528) {
147 free((void *)CONCAT71(uStack_53f,1local_54@) ) ;
148 }
```

## Slide 11

Sony Felica “felica_coinst.dll (2/2)”

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Sony Felica “felica_coinst.dll (2/2)”
r
58 LAB_0200dd36:
59 if (1Var5 != -1) {
60 /* Substring after last "/" */
61 pbVar2 = FUN_02014624(param_2,local_40,1Var5 + 1,OxfffffffttfffttTTF) ;
62 /* Filename NO sanitization */
63 std: :basic_string<>: :assign((basic_string<> *)param_1,pbVar2,0,0xfffffftfffttfTTF) ;
64 if (Oxf < local_20) {
65 free(local_38) ;
66 }
67 } |
z
169 std: :basic_string<>::assign((basic_string<> *)&local_4a8,"pUr1",4) ;
170 FUN_02015e10( (longlong) &local_4a8, (longlong)&local_548) ;
171 DOWNLOAD_TO_TEMP(pcVar10,"url_list.txt") ;
172 local_528 = Qxf;
173 local_530 = Q;
174 local_54@ = Q;
_|
r
62 std: :basic_string<>::assign(local_518," at Util: :Download().",@x15);
63 GetTempPathA(0x104,1local_148) ;
64 local_578 = Oxf;
65 local_580 = Q;
66 local_590 = Q;
```

## Slide 12

SONY + SIERRA - Sony recap

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
SONY + SIERRA - Sony recap
4 emulate Sony FeliCa @54C:86C3 SONY
felica_coinst1658.d11 ClassInstaller (DIF @x1e) as SYSTEM pulls url_list /
ins_list / app_info over plaintext HTTP from the spoofed Sony host
Vv
5 path traversal -> arbitrary write to System32 SONY
filename scan stops at / only (no .. / \ filter) -> SYSTEM writes
o\. 4. SWindows\System32\WUC6d, d11
Vv
6 re-emulate Sierra -> load the planted DLL SIERRA
SwiService.exe loads WUC64.d11 from System32
Vv
7 code execution as NT AUTHORITY SYSTEM
D1llMain runs as SYSTEM - pre-login console / reverse shell
```

## Slide 13

## NoPlug & pwn - No hardware required?

**Standard-user RDP -> SYSTEM - no device/no admin/remote**

- You don't have to plug something into the machine.

- RDP USB redirection: forward USB into remote session.

- The client describes the hardware. The server "builds" the device.

## Slide 14

NoPlug & pwn - USB_REDIR umrdp.dll (1/2)

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
NoPlug & pwn - USB_REDIR umrdp.dll (1/2)
68 /* proceed only if fDisableUSBRedir is absent / @ (USB redir NOT disabled) */
69 if (((LVar5 != 0) || (local_84 != 4)) || ((local_88 != 4 || (local_8@[@] == 0)))) {
70 uVar12 = (uint)param_2;
71 bVar3 = FUN_18002f650(pHVar9,uVar12) ;
72 if ((int)CONCAT71(extraout_var,bVar3) != 0) {
73 *(undefined *)(param_1 + @x78) = 0;
74 local_88 = 4;
75 LVar5 = RegQueryValueExW(local_78,L"MaxNumUsbDevices", (LPDWORD) 0x0, &local_84, (LPBYTE)1local_80,
76 &local_88) ;
95 if (((-1 < (int)uVar7) &&
96 (uVar8 = FUN_18002d9ac((uint *)(param_1 + 0x50) ,uVari2,(undefined4 *)local_60),
97 puVar11 = local_5®@, (int)uVar8 != @)) && (puVar11 = puVar10, iVar4 == @)) {
98 7* ADD_DEVICE / announce to PnP */
99 ADD_DEVICE_FUN_18002fb94(param_1,uVar12,iVar4 == Q);
100 }
a
```

## Slide 15

NoPlug & pwn - USB_REDIR termsrv.dll

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
NoPlug & pwn - USB_REDIR termsrv.dll
) /* default = E_INVALIDARG */
10 uVar3 = 0x8Q070057;
11 if ((param_2 != (uint *)@x@) && (param_4 != Q)) {
12 /* compare key to
{93D359D5 -831F -47B4 - 90BE -8383AF8F1BOE}
*/
13 1Var1 = 0x47b4831f93d359d5 - *param_1;
14 if (1Varl == @) {
15 1Varl1 = Oxelb8faf8383be90 - param_1[1];
16 }
a
r
36 /* BIT 11 of WinStation config = fDisablePNPRedir */
37 if (1Varl1 == @) {
38 uVar2 = *(uint *)(param_4 + @x1f00) >> Oxb & 1;
39 }
40 else {
41 uVar2 = *(uint *)(param_4 + @x1f0Q) >> Oxc & 7;
42 }
43 /* write value -> consumer reads *(pt4) */
44 *(uint *)(param_3 + 4) = uVar2;
45 uVar3 = Q;
46 }
47 }
48 return uVar3;
```

## Slide 16

NoPlug & pwn - USB_REDIR umrdp.dll (2/2)

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
NoPlug & pwn - USB_REDIR umrdp.dll (2/2)
13 local_res8 = (short *)0x@;
14 /* cVar1 = ok; DAT_180046210 = {93D359D5-...} PROPERTYKEY */
15 cVarl = WinStationGetConnectionProperty (param_2, &DAT_180046210,&local_res8) ;
16 /* iVar4 = 1;<-- DEFAULT = DISABLED */
17 iVar4 = 1;
18 if ((cVar1 != '\®@') && (*local_res8 == 1)) {
19 /* take the policy value (fDisablePNPRedir) */
20 iVar4 = *(int *)(local_res8 + 4);
21 +}
22 if (local_res8 != (short *)@x®) {
23 WinStationFreePropertyValue() ;
24 «+}
25 if ((((undefined **)PTR_LOOP_180051000 != &PTR_LOOP_180051000) &&
26 ((PTR_LOOP_180051000[@x1c] & 1) != 0)) && (2 < (byte)PTR_LOOP_180051000[0x19])) {
27 uVar2 = FUN_1800daf4();
28 pwVar3 = L"Enabled";
29 if (iVar4 != @) {
30 pwVar3 = L"Disabled";
31 }
32 FUN_180014324(*(undefined8 *) (PTR_LOOP_18005100@ + 0x10) ,@x5Q,&DAT_180049058, uVar2, pwVar3) ;
33. +}
34 /* ALLOW device announce ONLY when value == @ */
35 return iVar4 == Q;
36 }
```

## Slide 17

NoPlug & pwn - USB_REDIR RealSense POC

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
NoPlug & pwn - USB_REDIR RealSense POC
1 Intel RealSense F288 - DLL hijack oem49.inf 8886; 0A66
PnP install (DIF) - co-installer runs as SYSTEM
RealSenseF26@Coinstaller_227975.d11 (WHOL) -> launches Setup.exe [SYSTEM]
v
2 co-installer drops Setup.exe
copies ...\realsensef2a8depth.inf_amd64_*\Setup.exe ->
C:\Intel\RSOCM\Setup. exe
Vv
3 ProcMon - insecure DOLL search order in Setup.exe PROCMON
Setup.exe CreateFile C:\Intel\RSOCMS\CRYPTBASE.d11 NAME NOT FOUND <- we
plant it here
Setup.exe CreateFile C:\Windouws\System32\CRYPTBASE.d11 SUCCESS (normal
fallback)
v
4 code execution as NT AUTHORITY SYSTEM
C:\Intel is writable by normal users, and Setup.exe probes its own dir
first -> our CRYPTBASE.d11 loads, D1l1lMain runs as SYSTEM
Also confirmed hijackable: profapi, IPHLPAPI, WINHTTP, ... (12 candidates)
```

## Slide 18

POC_1 - USB_REDIR LPE

## Slide 19

## Same Path, Third Road

### **Beyond the last POC - PnP becomes the loader**

- The last POC was just one example.

- The real target was the install path Windows PnP fetches & loads hundreds of vulnerable signed packages straight from Windows Update. Fully trusted.

- No CreateService nor admin. The classic precondition evaporates.

- Two roads, same path: USB cable + FaceDancer (physical) and a standard RDP session (remote). We also have a third road.

## Slide 20

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
- PhP as the Loader
Windows PnP install path
"the loader"
' _—™~
Physical USB) (ROP USB redirection] |jpnp_simulate.exe
FaceDancer remote path research path
v
Vendor package/softuare
privileged install path _|
```

## Slide 21

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
= From Features to Primitives
f*
We were not hunting a single vendor bug.
We mapped packages Windows can bind to USB identities.
The real surface starts when vendor code enters the install path.
*f
¥
USB identity
t
Windows package match
y
Yendor codé appears
mo a
—~Y
co-installer
service
executable] jconfig logic
Ss Ss
2
Offensive primitive
```

## Slide 22

From packages to USB identities

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
From packages to USB identities
1 collect packages
WU/CATALOG
Microsoft Catalog + Windows Update -> CABs -> INFs -> Hardware IDs
Vv
# triage vendor code
PE
co-installers, services, standalone EAEs, imports, registry writes, named
pipes, service controls
3 reproduce the identity
USB/PNP
FaceDancer backends: Cynthion + GreatFET; plus pnp_simulate.exe for
controlled Windows-side testing
v
f* no real vendor hardware required
Windows only sees an identity: VID, PID, class,
The rest is the normal PnP path. */
COMMENT
interfaces and descriptors.
```

## Slide 23

pnp_simulate.exe

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pnp_simulate.exe
1 run prp_simulate. exe ADMIN
--Vid KAKA --pid KAKA; builds USB\WVID_XXKHXGPID_XAKK; starts observer via
CM_Register_Notification.
2 SetupDi device creation DEVCON
SetupODiCreateDeviceInfoLlist;
SetupDiCreateDeviceInfoW(ROOT, DICO_GENERATE_ID); set hardware ID.
4
3 DIF_REGISTERDEVICE -> device tree KEY STEP
Device visible to PnP Manager, Device Manager and Windows Update; creates
ROOTS PHPSIMDEVICE.66a88,
```

## Slide 24

pnp_simulate.exe

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pnp_simulate.exe
4 DilnstallDevice -> ODriverStore QUERY
Local driver search only; local INFs; writes setupapi.dev,log.
Vv
5 WU COM API -> catalog search QUERY
IUpdateSearcher: :Search; catalog metadata for discovery; not proof of auto-
install,
Vv
6 --install -> CM_Setup_DevNode(READY) INSTALL
Real install path; same API boundary into kernel. Without --install: query-
only, no system changes.
```

## Slide 25

Catalog Hit != Auto-Install

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Catalog Hit != Auto-Install
WU COM API / IUpdateSearcher — _orscoverv.
> Returns catalog metadata,
> Great for finding candidates,
> Includes automatic, manual, old, and catalog-only
packages,
/* A Windows Update hit is not proof that PnP will auto-
download or install that package. */
Device Installation AUTO-INSTALL PATH
Service / Server-Side
Resolve
> Triggered by CH_Setup_DevNode (READY).
l > Runs through DsmSvce as a privileged install flow,
> Restricted path: far fewer candidates,
> Match -> CAB staging -> drvinst.exe install path.
```

## Slide 26

Phase 1: Device Identity

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
e [ acevancer
Phase 1: Device snutated Use device
¥
Identity Device descriptor
YID / PID / device class
¥v
Configuration
descriptor
i
Control descriptors.
Control the hardware IDs
Windows will resolve.
# f
Interface descriptors
class / subclass / protocol
Windows buildsl*
hardware IDs
USB\VID_XRRRGEPIO_YYYYEMI_22
composite device
INF matching _|
USB\VID_RRKKEPIO_VYYY
```

## Slide 27

Phase 2: USB identity to devnode

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Phase 2: USB identity to devnode
1 real USB path HARDWARE
USB hub reads descriptors from the emulated device.
4
2 PDO KERNEL
Creates a Physical Device Object for the child device.
Vv
3 BusRelations PNP
ToInvalidateDeviceRelations(BusRelations) tells PnP: new child device.
```

## Slide 28

Phase 2: USB identity to devnode

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Phase 2: USB identity to devnode
4 pnp_simulate.exe path USER MODE
No full USB bus emulation. We reproduce the useful part from user-mode,
Vv
5 Hardware IDs SETUPDI
SetupDiSetDeviceRegistryProperty(SPORP_HARDWAREIO).
Vv
6 Register devnode DEVCON
SetupDiCallClassInstaller(DIF_REGISTERDEVICE),
Vv
Y Same research target COMMENT
Both paths give us a devnode with controlled hardware IDs that Windous
tries to resolve.
```

## Slide 29

Phase 3: CM_Setup_DevNode

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Phase 3: CM_Setup_DevNode
1 CH_Setup_DevNode( READY) WINDBG
CM_Setup_DevNode(deviInst, CMH _SETUP_DOEVNODE_READY) enters
cfgmgr32!Local_CM_Setup_DevNode.
2 DeviceloControl(axd7a8dF) KERNEL BOUNDARY
The request crosses into the Configuration Manager / PnP kernel path.
Vv
3 PiCh* handling KERNEL
PiCMFastIoDeviceDispatch -> PiCMHandleIoctl -> PiCMDeviceAction.
Vv
4 PidueveDeviceRequest
The action i8 queued. User-mode returns, but the real PnP work continues
asynchronously,
```

## Slide 30

Phase 4: Device Installation Service

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Phase 4: Device Installation Service
1 PrP worker KERNEL
Queued action picked up by the PnP worker; device IDs and compatibility are
resolved,
2 Device Installation Service SYSTEM
OsmSve runs inside svchost.exe as SYSTEM and handles the privileged install
flow.
3 Package resolution FILTERED
Local DriverStore first. If needed: Server-Side Resolve -> Windows Update
CAB staging.
4 drvinst.exe install path VENDOR CODE
Co-installers, support executables or services enter the privileged
installation path.
```

## Slide 31

POC_2: Internals Demo

## Slide 32

Signed does not mean safe logic

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Signed does not mean safe logic
Cryptographic trust
>
>
SIGNED PACKAGE
Valid catalog / known package.
Windows can resolve and stage it.
PnP can enter the privileged install path.
#* Origin and install trust. Not a vendor
logic audit. */
Yendor logic ATTACK SURFACE
> Co-installers, services, support EXEs.
> Registry values, debug flags, config paths.
> Privileged code accepting controlled state.
> Impact appears when pieces compose.
/* No UAC prompt does not mean no privileged
action. */
```

## Slide 33

Wacom: The Bugdoor

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
050
071
072
073
080
081
082
083
084
085
086
120
121
122
123
124
125
126
127
128
Wacom: The Bugdoor
/* WTabletServiceISD. exe
SHA256 955fb51d0fc2b3ccb192b6ed707771a99d28be2e7c1a7541be7762207325c86F
Signed vendor service. The interesting part is privileged logic,
not memory corruption. */
RegOpenKeyExA (HKLM,
"SYSTEM\\CurrentControlSet\\Services\\WlabletServiceISD\\Service",
edi
/* Registry trigger verified at 0x140036950 -> 0x140036981 */
RegQueryValueExA(hKey, "PowerT", NULL, &type, (BYTE *)&value, &cbData) ;
if (type == REG BINARY & cbData == 4 &
value == 0x346b4c7f) { /* bytes in registry: 7F 4C 6B 34 */
g_PowerT enabled = true; /* sete byte [0x140093be2] */
}
/* Later: execution path controlled by that flag */
if (g_PowerT enabled) { /* checked around 0x14002f18f */
startup. lpDesktop = L"WinSta0\\default"; /* 0x14002f1b2 */
cmdline = L"cmd.exe"; /* 0x14002f226 */
/* Token/session plumbing is present in the binary:
WTSQueryUserToken / OpenProcessToken / DuplicateTokenEx */
CreateProcessAsUserW(token, NULL, cmdline, ...);
```

## Slide 34

Wacom Trigger Conditions

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Wacom Trigger Conditions
1 registry key
Service key: WlabletServiceISD\\Service
Vv
2 trigger value
REG_BINARY with bytes ?F dC 6B 34
3 binary checks
type == 3, chData == 4, compare with @x3d6b4c7f
Vv
4 service context
WlabletServiceISD.exe runs as LocalSystem,
Vv
5 process path
CreateProcessAsUserW -> WinSta@\\default -> cmd.exe
Vv
HKLM
PowerT
VERIFIED
SYSTEM
INTERACTIVE
6 demo boundary
COMMENT
Standalone demo writes HKLM as admin only to isolate Wacom behavior
```

## Slide 35

POC_3: Wacom

## Slide 36

Atheros

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Atheros
i AdminService.exe
/* Found in our pipeline; aligns with public
CVE-2019-10617 */
// AtherosSvc / AdminService.exe
// service context: LocalSystem
C:\ProgramData\Atheros\AtherosServiceConfig. ini
[AthService]
regOpType="3" // write value
regPath="HKEY LOCAL MACHINE\...\Print\Monitors\PocPortMon"
regValue="Driver"
regType="1" // REG SZ
regData="C:\ProgramData\Atheros\PocPortMon.dll"
ControlService(AtherosSvc, 133)
-> GetPrivateProfileStringW("AthService", "reg*", ...)
-> RegCreateKeyExW / RegOpenKeyExW
-> RegSetValueExW(...)
/* user controls the INI; the service provides the
privilege */
/* result: HKLM registry write as SYSTEM */
```

## Slide 37

Atheros INI -> Registry

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Atheros INI -> Registry
[ 1 INI payload
[AthService]
regType = 1 / REG_SZ
t
2 AtherosSvc
ControlService(133)
AdminService.exe as LocalSystem
‘i
3 privileged registry write
HKLH\SYSTEM\CurrentControlSet\Control\Print\Monitors
PocPortMon
Driver = C:\ProgramData\Atheros\PocPortMon.d1l
4 Spooler start a
spoolsyv.exe as SYSTEM le stable REG_S2 path; exact binary write happens from SYSTEM DLL */
enumerates Print Monitors
¥
5 DLL load
PocPortMon.dil
runs inside spoolsyv.exe
¥
6 bridge to Wacom
urite PowerT as REG_BINARY
?F 4C 6B 34
```

## Slide 38

The chain we wanted vs the chain that worked

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
The chain we wanted vs the chain that worked
TOO CLEAN
> Atheros writes PowerT as REG_BINARY.
Direct Wacom chain
> Restart WlabletServiceISD.
> Wacom launches cmd.exe as SYSTEM.
> Problem: AdminService.exe parses binary
data character-bhy-character.
> "?F4C6B34" becomes the wrong byte sequence.
/* Pretty chain. Wrong parser behavior for
this target, */
Working chain STABLE PATH
> Atheros writes a Print Monitor REG_5S2.
> spoolsv.exe loads PocPortMon.d1ll as SYSTEM.
> The OLL writes the exact Wacom PowerT
value,
> RegSetValueExW: ?F 4C 6B 34.
> Restart Wacom -> interactive SYSTEM shell.
/* Registry write -> SYSTEM DLL -> exact
Wacom trigger. */
```

## Slide 39

POC_4: Full Chain From Low Priv

## Slide 40

## Mitigations

- Physically rip out the USB ports

- ● Fill the ports with silicone or cement

- ● Cut the power cable to the user's machine

- Restrict package delivery via Windows Update

- ● Allow-lists by hardware ID / device class

- Block unnecessary USB classes

- Audit vendor services that persist running as SYSTEM

- ● Disable RDP USB redirection in remote environments

## Slide 41

## Conclusions

- A physical USB identity can lead to SYSTEM execution with 0 clicks

- ● In certain environments, a USB identity redirected over RDP can result in privilege escalation

- ● A bug that looks like it requires admin can chain into a full LPE on the latest Windows with a second bug that has been there since 2019

- ● Windows can pull vendor software on our behalf with system permissions just by inserting a USB

- If that software exposes the right primitive, PnP stops being just device installation, It becomes an execution path

## Slide 42

## References

- CVE Program. (s. f.). CVE-2019-10617. https://www.cve.org/CVERecord?id=CVE-2019-10617

- National Institute of Standards and Technology. (s. f.). CVE-2019-10617 detail. National Vulnerability Database. https://nvd.nist.gov/vuln/detail/CVE-2019-10617

- Qualcomm Technologies, Inc. (2019, october). Qualcomm Security Bulletin: October 2019. https://docs.qualcomm.com/product/publicresources/securitybulletin/october-2019-bulletin.html

- Microsoft. (s. f.). Hardware IDs. Microsoft Learn. https://learn.microsoft.com/en-us/windows-hardware/drivers/install/hardware-ids

- Microsoft. (s. f.). SetupDiCreateDeviceInfoA function. Microsoft Learn. https://learn.microsoft.com/en-us/windows/win32/api/setupapi/nf-setupapi-setupdicreatedeviceinfoa

- Microsoft. (s. f.). DIF_REGISTERDEVICE installation request. Microsoft Learn. https://learn.microsoft.com/en-us/windows-hardware/drivers/install/dif-registerdevice

- Microsoft. (s. f.). CM_Setup_DevNode function. Microsoft Learn. https://learn.microsoft.com/en-us/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_setup_devnode

- Microsoft. (s. f.). DiInstallDevice function. Microsoft Learn. https://learn.microsoft.com/en-us/windows/win32/api/newdev/nf-newdev-diinstalldevice

- Microsoft. (s. f.). Driver Store. Microsoft Learn. https://learn.microsoft.com/en-us/windows-hardware/drivers/install/driver-store

- Microsoft. (s. f.). IUpdateSearcher interface. Microsoft Learn. https://learn.microsoft.com/en-us/windows/win32/api/wuapi/nn-wuapi-iupdatesearcher

- Yosifovich, P., Russinovich, M. E., Ionescu, A., & Solomon, D. A. (2017). Windows Internals, Part 1: System architecture, processes, threads, memory management, and more (7th ed.). Microsoft Press.

https://www.microsoftpressstore.com/store/windows-internals-part-1-system-architecture-processes-9780735684188

- Allievi, A., Russinovich, M. E., Ionescu, A., & Solomon, D. A. (2021). Windows Internals, Part 2 (7th ed.). Microsoft Press. https://www.microsoftpressstore.com/store/windows-internals-part-2-9780135462409

- Great Scott Gadgets. (s. f.). FaceDancer [GitHub repository]. GitHub. https://github.com/greatscottgadgets/facedancer

- Great Scott Gadgets. (s. f.). Cynthion. https://greatscottgadgets.com/cynthion/

- Great Scott Gadgets. (s. f.). Cynthion [GitHub repository]. GitHub. https://github.com/greatscottgadgets/cynthion

- Great Scott Gadgets. (s. f.). GreatFET [GitHub repository]. GitHub. https://github.com/greatscottgadgets/greatfet

## Slide 43

Telegram: @edhx0 & @borjmz
