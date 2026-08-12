---
title: "Bring Your Own COM - Session Pivoting and Lateral Movement via Ephemeral COM Registration"
speakers: ["Shebin Mathew"]
conference: "Black Hat"
conference_full: "Black Hat USA 2026"
edition: "USA"
year: 2026
source_pdf: "BlackHat_USA_2026_Slides/Shebin Mathew_Bring Your Own COM - Session Pivoting and Lateral Movement via Ephemeral COM Registration.pdf"
pages: 31
sha256: "10a10cc4ba00548f67bf1940a297b9001adf2fdfb68f535842e8a4816e13b01f"
text_chars: 13685
ocr_pages: 17
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T23:15:52Z"
---
# Bring Your Own COM - Session Pivoting and Lateral Movement via Ephemeral COM Registration

**Speakers:** Shebin Mathew  
**Conference:** Black Hat USA 2026  
**Source:** `BlackHat_USA_2026_Slides/Shebin Mathew_Bring Your Own COM - Session Pivoting and Lateral Movement via Ephemeral COM Registration.pdf` (31 pages)

## Slide 1

Bring Your Own COM: Session Pivoting and Lateral Movement via Ephemeral COM Registration

## Slide 2

## About me

- Shebin Mathew

- Senior Consultant Google/Mandiant

- Talks: DEFCON . Black Hat EMEA 971 SEC . COCON . BSIDES

- Published Tools/Blogs

2

## Slide 3

## Agenda

- COM/DCOM Fundamentals

- Why Target COM?

- DLL Surrogate Mechanism

- Session Monikers

- The Technique: Bring Your Own COM

- Demo

- Detection Signals

3

## Slide 4

#### What is COM

- **Component Object Model (COM)** – Microsoft's component framework for software interoperability

- Enables communication between applications, processes, and programming languages

- Forms the foundation of many Windows technologies

- **COM Building Blocks**

- COM Server – DLL or EXE implementing one or more COM classes

- COM Class (CLSID) – Unique identifier used to instantiate a COM object

- COM Object – Runtime instance of a COM class

- COM Interface – Collection of methods exposed to clients

4

## Slide 5

#### In-Process COM Server (DLL)

- COM server runs **inside the client process**

- Implemented as a **DLL loaded by the COM runtime**

5

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
In-Process COM Server (DLL)
COM server runs inside the client process
Implemented as a DLL loaded by the COM runtime
CLIENT
Calls CocreateInstance( CLSID ) to request a COM object
J
Finds CLSID in registry — identifies InprocServer32 (DLL)
COM RUNTIME
Loads the DLL into the client process memory
DLL
COM object is created inside the same process
‘@)
YY
COM RUNTIME
Returns a reference to the COM object to the client
|
CLIENT
Calls methods directly — no IPC
black hat
2026 5
```

## Slide 6

#### Out of-Process COM Server (EXE)

- COM server runs in a separate process

- Implemented as a standalone EXE registered with SCM

6

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Out of-Process COM Server (EXE)
COM server runs in a separate process
Implemented as a standalone EXE registered with SCM
CLIENT
Calls cocreateInstance( CLSID ) to request a COM object
|
Finds CLSID in registry > identifies LocalServer32 (EXE)
COM RUNTIME
Starts or connects to the COM server process
|
EXE SERVER — DIFFERENT PROCESS
COM object is created inside a separate process
|
COM RUNTIME
Creates proxy / stub and returns a reference via IPC (RPC)
CLIENT
Calls methods through IPC — cross-process communication required
black hat
2026 6
```

## Slide 7

#### DCOM - Distributed COM

- DCOM runs COM objects on remote machines over a network.

- It uses RPC proxy/stub so remote calls look like local calls.

7

## Slide 8

#### COM in the Real World

8

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
COM in the Real World
™I need to get the current
username and domain,
how do i do that ?.”
‘simple. i expose exactly
through COM
interfaces”
MC
black hat
2026 8
```

## Slide 9

#### COM in the Real World

9

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
COM in the Real World
Name: WScript.Network
[cisip: {093FF999-1EA0-4079-9525-9614C35(
Server Type: InProcServer32
Server: C:\Windows\System32\wshom.ocx = i ¥ . o- yt
CmdLine: N/A
TreatAs: N/A
Threading Model: Apartment
| ProgIDs: .Network
WScript.Network eee
Methods VTable Offset s
Ay}
¢* !
e |
IWshNetwork2
29
|Unknown 00 ) 3 wshom.ocx+0x38A40
black hat
2026 9
```

## Slide 10

#### COM in the Real World

10

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
COM in the Real World
IWshNetwork2 eo@e@
1 [Guid ("24BE5A31-EDFE-11D2-B933-00104B365C9E") ]
2 interface IWshNetwork2
3 {
4 /* Properties */
5 string ComputerName { get; }
6 string Organization { get; }
7 string Site { get; }
8 string UserDomain { get; }
i) string UserName { get; }
10 string UserProfile { get; }
11
12 /* Methods */
13 void AddPrinterConnection(string, string, Variant, Variant, Variant);
14 void AddWindowsPrinterConnection(string, string, string);
15 IWshCollection EnumNetworkDrives ();
16 IWshCollection EnumPrinterConnections();
17 void MapNetworkDrive (string, string, Variant, Variant, Variant);
18 void RemoveNetworkDrive (string, Variant, Variant);
19 void RemovePrinterConnection(string, Variant, Variant);
20 void SetDefaultPrinter (string) ;
2] }
black hat
2026 10
```

## Slide 11

#### COM Object Registration

11

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
COM Object Registration
Ao
File Edit v Favorites Help
Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Classes\CLSID\{093FF999-1EA0-4079-9525-9614C3504B74}\lnProcServer32
{O8FCO6E4-C6B5-40BE-97B0-B80F943 Name Type Data
{08fedb70-9d27-4bcf-bbb0-99986ae: (Default) REG_SZ C:\Windows\System32\wshom.ocx
{09017262-fdb4-4ff2-9013-26332c92¢ ThreadingModel REG_SZ Apartment
{0907616E-F5E6-48D8-9D61-A91C3D
{0913ACCF-B1AB-4EEE-AOC7-F4D7C1
{09144FD6-BB29-11DB-96F1-005056¢
{093cb270-c282-4c22-b2ea-7d2bf1c3
{093FF999-1EA0-4079-9525-9614C35
Implemented Categories
InProcServer32
ProgID
Programmable
TypeLib
black hat
2026 11
```

## Slide 12

#### DomainCheck.exe – main()

12

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
DomainCheck.exe — main()
int main()
{
HRESULT hr = CoInitializeEx(@, COINIT_APARTMENTTHREADED) ;
// 1. Resolve ProgID to CLSID
CLSID clsid;
hr = CLSIDFromProgID(L"WScript.Network", &clsid);
// 2. Create COM object and request IWshNetwork2 interface
IWshNetwork2* pNet = nullptr;
hr = CoCreateInstance(
clsid,
nulliptr,
CLSCTX_INPROC_SERVER,
IID_IWshNetwork2,
(void** )&pNet
// 3. Call methods through COM interface
BSTR computerName = nullptr;
BSTR userDomain = nullptr;
hr = pNet->get_ComputerName(&computerName) ;
hr = pNet->get_UserDomain(&userDomain) ;
if (SUCCEEDED(hr) )
{
std::wcout << L"Computer
std::wcout << L"Domain
<< computerName << std::endl;
<< userDomain << std::endl;
}
SysFreeString(computerName) ;
SysFreeString(userDomain) ;
pNet->Release() >;
CoUninitialize();
return 0;
} black hat
2026 12
```

## Slide 13

#### DomainCheck.exe – main()

13

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
DomainCheck.exe — main()
[29-03-2026 12:37:53] PS C:\Users\mandi\Documents\tools> .\DomainCheck.exe
Computer : WINAZAD
Domain : WINAZAD
HB DomainCheck.exe (8268) Properties
General Statistics Performance Threads Token Modules Memory Environment Handles .NET assemblies .NET performance
Options
Name Base address Size Description
DomainCheck.exe Ox7ff6bfc90000 9.17 MB
icu.dll 0x7ffebd690000 2.18 MB ICU Combined Library
imm32.dll Ox7ffed0730000 188 kB Multi-User Windows IMM32 API Client DLL
kernel32.dll Ox7ffecf840000 776 kB Windows NT BASE API Client DLL
ntdll.dll Ox7ffed1010000 1.97 MB_ NT Layer DLL
uxtheme.dll Ox7ffecc040000 632 kB Microsoft UxTheme Library
wshom.ocx 0x7ffebbbc0000 164kB Windows Script Host Runtime Library
DomainCheck.exe 9 RegOpenKey HKCR\WScript.Network\CLSID
DomainCheck.exe RegQueryValue HKCR\WScript.Network\CLSID\(Default)
DomainCheck.exe 4504 FAS RegOpenkey HKCU\Software\Classes\CLSID\{O93FF999-1EA0-4079-9525-9614C3504B74}\InProcServer32
DomainCheck.exe 4504 ff} RegQueryValue HKCR\CLSID\{093FF999-1EA0-4079-9525-9614C3504B74}\InProcServer32\(Default)
DomainCheck.exe 4504 & Load Image C:\Windows\System32\wshom.ocx
black hat
2026 13
```

## Slide 14

#### Why Target COM?

- Trusted Windows execution framework

- Object activation is a legitimate operating system behaviour

- Multiple activation models

- Registration-driven architecture

- Process abstraction

- Widely adopted across Windows

14

## Slide 15

#### COM Surrogate Mechanism

- Allows an in-process COM DLL to execute as an out-of-process COM server

- Windows hosts the DLL inside **dllhost.exe** (the COM Surrogate process)

- Enabled by associating a CLSID with an AppID that defines **DllSurrogate**

- Provides process isolation while preserving the original COM interface

- Clients continue to use **CoCreateInstance() and** receives the same COM interface pointer

- The COM runtime transparently redirects activation to **dllhost.exe**

15

## Slide 16

#### Activation Flow

16

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Activation Flow
@) CLIENT
Calls cocreateInstance( CLSID ) to request a COM object
J
@) SCM
Finds CLSID in registry — retrieves the associated AppID
G) SscM
Detects DilSurrogate registry value under the AppID
@) SCM
Launches (or reuses) dilhost.exe
G) DLLHOST.EXE
Loads the COM DLL and creates the COM object
G) CLIENT
Communicates with the COM object through COM / RPC
black hat
2026 16
```

## Slide 17

#### Windows Sessions - Isolation Model

- Windows sessions isolate user environments and system services

- Sessions separate security boundaries

- Cross-session communication requires OS-managed IPC

17

## Slide 18

#### Session Monikers

- Session Monikers allow COM objects to be activated in a specific Windows session

- Extends normal COM activation by adding a target session identifier

- Uses existing Windows COM activation infrastructure

```
Format:
```

Session Monikers provide a legitimate way to route COM activation into another Windows session.

18

## Slide 19

#### Session Monikers – Activation Flow

19

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Session Monikers — Activation Flow
(a) CLIENT
CoGetObject("session:N!new:{CLSID}")
(2) COM RUNTIME — OLE32.DLL
Resolves the session moniker and extracts the target CLSID
ff
(3) RPCSS / COM ACTIVATION INFRASTRUCTURE
Routes the activation request to Session N on the target machine
|
(4) SESSION N — COM INFRASTRUCTURE
Receives activation request and resolves the COM server type from registry
G) DLLHOST.EXE OTHER COM SERVER
Spawned as COM Surrogate Launched as a registered EXE or
when DilSurrogate is configured reused in-process server
under AppID
black hat
2026 19
```

## Slide 20

#### DcomLaunch - The COM Activation Broker

- Runs as **svchost.exe -k DcomLaunch** with SYSTEM privileges

- Machine-level COM registration under HKLM is used for DCOM surrogate activation

- Resolves AppID configuration → DllSurrogate="" triggers COM Surrogate (dllhost.exe) activation

20

## Slide 21

#### Evolution of COM Abuse Techniques

21

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Evolution of COM Abuse Techniques
TECHNIQUE CLSID RANDOM PER RUN
BitlockMove Existing (hardcoded) No
DCOMRunAs Existing (operator supplied) INKo)
COMouflage Custom (static) No
SessionHop Existing (hardcoded) No
Custom (random)
black hat
2026 21
```

## Slide 22

#### The Idea - Bring Your Own COM

- Generate a unique CLSID and AppID at runtime

- Create a temporary COM registration in HKLM

- Trigger COM activation through Session Moniker or DCOM

- Windows activates the object through the native surrogate path: svchost.exe (DcomLaunch) → dllhost.exe

- dllhost.exe loads the COM DLL and executes the payload

- Remove the temporary COM registration after activation

- Key Characteristics

22

## Slide 23

#### Registry Staging - What Gets Written

23

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Registry Staging - What Gets Written
KEY
CLSID
CLSID KEY
{Random CLSID}
VALUE SUBKEY
AppID
VALUE
(Default)
HKLM\Software\Classes
AppID
{Random AppID}
InprocServer32
VALUE VALUE
ThreadingModel D1lSurrogate
v
(
DCOM INFRASTRUCTURE
COM Activation
v
(
SURROGATE PROCESS
dilhost.exe
v
LOADED DLL
payload.d1l
black hat
2026 23
```

## Slide 24

#### COM Activation - Session Pivot

24

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
COM Activation - Session Pivot
Generate i
SueIe HESS DcomLaunch Payload Executes
GUIDs Registry Moniker Activation
llhost.exe
CLSID = CLSID\{X} CoGetObject( ™
CoCreateGuid() InprocServer32 session:N . ql
AppID = | payload.d1l !new: {CLSID} a vote sesonieen
Receives DllGetClassObject ()
CoCreateGuid() y activation request OM ol created
AppID\ix} = (i‘(<‘iéitéds;:C(‘;SC CY ation request M obj reat
Random D1llSurrogate="" No Starts : 1
= 4 _ after call
every run RunAs= CreateProcess fter
never seen before SUES Sar by caller
black hat
USA
2026 24
```

## Slide 25

#### COM Activation - Lateral Movement

25

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
COM Activation - Lateral Movement
Generate
GUIDs
Remote
COM Registration
Remote DCOM
Activation
Target
DcomLaunch
Payload
Executes
black hat
2026
25
```

## Slide 26

### DEMO – Session Pivoting

26

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
DEMO — Session Pivoting
Cy OBS 32.1.2 - Profile: Untitled - Scenes: Untitled
File Edit View Docks Profile SceneCollection Tools Help
Scenes a
Tle Gt View Docks Frotle Scene Cllemion Tools Held
main —_
FO rnegtaycaprire ea . oe cuaee
OD Dispisy Capture PM rvoperies §— E)iters—ispiay | 1920x1980 8 6.0 {Primary Moniton, -
‘io Winer ‘= Some Transitions = Controls =
phen te kines © Fase - stan Sveaming
oowaton SESE = sunqoare
A +0 i smmucma
oll? ol Suutio age
a a Setings
© Display Capture oa = = : = :
© Display Capture @ Properties ® Filters Display : 1920x1080 @ 0,0 (Primary Monitor) a
Audio Mixer Scene Transitions = Controls
Global Global
Desktop Audio Y Mic/Aux Fade ’ Start Streaming
8 Aa
Q Duration 300ms Start Ragording
MN Mv
4 + Wi: Start Virtual Camera o
rH
me Studio Mode
es: 68
x x Settings
Se a © a 0 hidden 6 + Options ~
00:00:00 00:00:00 CPU:11.6%  30.00/ 30.00 FPS
5:27 PM
26
black hat
26
```

## Slide 27

### DEMO – Lateral Movement

27

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
DEMO — Lateral Movement
- Profile: Untitled - Scenes: Untitled
File Edit View Docks Profile SceneCollection Tools Help
Scenes eS z :
Scene — = ——«<
main —_— i
a
O Poesptay Capture ea
© Disptay Capmure OQ rroperes — E)Miters—iepray : 192941980 8 0.0 (Primary Monitor -
‘io iver © Seaman = Controle .
= Fae - stan streaming
Fi Duraton | 300%m8 gE santrgortng
j +0: Sunvnwatcmes
‘ i ee Studio Mowe
© Display Capture 2a 2 &, : v
© Display Capture @ Properties ® Filters Display : 1920x1080 @ 0,0 (Primary Monitor) +.
Audio Mixer Scene Transitions Controls a
Global Global
Desktop Audio Y Mic/Aux  v Fade ’ Start Streaming
Duration 300 ms — Start SSRI
it ra
2 + Wi: Start Virtual Camera a
r r Studio Mode
x x Settings
+W @av 0 hidden 6 + Options w
Recording saved to 'C:/Users/sheb/Videos/2026-06-28 17-46-39.mp4' 0 ) 00:00 CPU: 12.3% 30.00 / 30.00 FPS
black hat
27
```

## Slide 28

•

# DEMO

- Session pivot - cross-session execution via session moniker

##### Remote lateral movement - DCOM activation across machines

28

## Slide 29

## Detection Signals

29

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Detection Signals
= Ephemeral COM Registration
HKLM\SOFTWARE\Classes\CLSID\
HKLM\SOFTWARE\Classes\AppID\
EID 12 Sysmon
EID 13. Sysmon
COM Surrogate Activation
dllhost.exe
EID 1 Sysmon
4688 Security Log
cup Correlation
(@) COM Activation Telemetry
BEHAVIOR
Session moniker-based COM activation
EXAMPLE
session: <N>!new:{CLSID}
TELEMETRY
ET | Microsoft-Windows-COM-Perf
ET | Microsoft-Windows-RPC
ARTIFACT
COM activation using session moniker syntax
from non-standard processes
(ay: COM Server DLL Loading
\\server\share\payload.d1l
C:\Temp\payload.dll
C:\Users\Public\payload.d11
EID 7 Sysmon
black hat
2026 29
```

## Slide 30

## Q&A

30

## Slide 31

## Thank You

31
