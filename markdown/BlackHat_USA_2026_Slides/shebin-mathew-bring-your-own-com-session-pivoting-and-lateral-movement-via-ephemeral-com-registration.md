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
text_chars: 11967
ocr_pages: 17
has_ocr: true
redacted_secrets: 0
ocr_confidence: 88.0
ocr_unreliable_blocks: 2
vision_verified_pages_changed: 19
vision_verified_pages: 31
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T05:43:58Z"
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

**COM Building Blocks**

- COM Server – DLL or EXE implementing one or more COM classes

- COM Class (CLSID) – Unique identifier used to instantiate a COM object

- COM Object – Runtime instance of a COM class

- COM Interface – Collection of methods exposed to clients

**COM Server / DLL or EXE** (diagram)

- **COM Class** `{CLSID}` – Registered in `HKLM\SOFTWARE\Classes\CLSID` · Points to the server · Defines object creation
- **COM Object** – Runtime instance of the COM class · Exposes one or more interfaces
- Base interface **IUnknown** – `QueryInterface()`, `AddRef()`, `Release()`
- Interface A **IClassFactory** – `CreateInstance()`, `LockServer()`
- Interface B **IDispatch** – `GetTypeInfo()`, `Invoke()`
- Interface N **ICustom** – `Method1()`, `Method2()`

4

## Slide 5

#### In-Process COM Server (DLL)

- COM server runs **inside the client process**

- Implemented as a **DLL loaded by the COM runtime**

5

1. **CLIENT** – Calls `CoCreateInstance( CLSID )` to request a COM object
2. **SCM** – Finds CLSID in registry → identifies **InprocServer32** (DLL)
3. **COM RUNTIME** – Loads the DLL into the client process memory
4. **DLL** – COM object is created inside the same process
5. **COM RUNTIME** – Returns a reference to the COM object to the client
6. **CLIENT** – Calls methods directly — no IPC

2026 5

## Slide 6

#### Out of-Process COM Server (EXE)

- COM server runs in a separate process

- Implemented as a standalone EXE registered with SCM

6

1. **CLIENT** – Calls `CoCreateInstance( CLSID )` to request a COM object
2. **SCM** – Finds CLSID in registry → identifies **LocalServer32** (EXE)
3. **COM RUNTIME** – Starts or connects to the COM server process
4. **EXE SERVER — DIFFERENT PROCESS** – COM object is created inside a separate process
5. **COM RUNTIME** – Creates proxy / stub and returns a reference via IPC (RPC)
6. **CLIENT** – Calls methods through IPC — cross-process communication required

2026 6

## Slide 7

#### DCOM - Distributed COM

- DCOM runs COM objects on remote machines over a network.

- It uses RPC proxy/stub so remote calls look like local calls.

7

1. **CLIENT** – Calls `CoCreateInstance( CLSID )` to request a COM object
2. **SCM — LOCAL MACHINE** – Finds CLSID in registry → identifies **remote activation** (DCOM enabled)
3. **DCOM RUNTIME / RPC LAYER** – Establishes network communication to the remote machine hosting the COM server
4. **SERVER MACHINE — EXE SERVER** – COM object is created inside a different machine's process
5. **DCOM PROXY / STUB — RPC OVER NETWORK** – Method calls are marshaled and sent over the network using RPC
6. **CLIENT** – Invokes methods as if local — execution happens on a remote machine

2026 7

## Slide 8

#### COM in the Real World

8

"I need to get the current username and domain, how do i do that ? "

"Simple. i expose exactly through COM interfaces"

2026 8

## Slide 9

#### COM in the Real World

9

Two panels, captioned **COM Registration** and **COM Interfaces**:

Name: `WScript.Network`
CLSID: `{093FF999-1EA0-4079-9525-9614C3504B74}`
Server Type: `InProcServer32`
Server: `C:\Windows\System32\wshom.ocx`
CmdLine: `N/A`
TreatAs: `N/A`
Threading Model: `Apartment`
ProgIDs: `WScript.Network`

`WScript.Network` interfaces:

| Name | IID | Methods | VTable Offset |
|---|---|---:|---|
| IDispatch | 00020400-0000-0000-C000-000000000046 | 7 | wshom.ocx+0x38A40 |
| IWshNetwork2 | 24BE5A31-EDFE-11D2-B933-00104B365C9F | 8 | wshom.ocx+0x38A40 |
| IUnknown | 00000000-0000-0000-C000-000000000046 | 3 | wshom.ocx+0x38A40 |

2026 9

## Slide 10

#### COM in the Real World

10


> Recovered by OCR — confidence 90/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
COM in the Real World
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
2026 10
```

## Slide 11

#### COM Object Registration

11

Registry Editor, path `Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Classes\CLSID\{093FF999-1EA0-4079-9525-9614C3504B74}\InProcServer32`, with sibling CLSID keys visible in the tree (`{08FC06E4-C6B5-40BE-97B0-B80F943...}`, `{08fedb70-9d27-4bcf-bbb0-99986ae...}`, `{09017262-fdb4-4ff2-9013-26332c92...}`, `{0907616E-F5E6-48D8-9D61-A91C3D...}`, `{09144FD6-BB29-11DB-96F1-005056...}`, `{093cb270-c282-4c22-b2ea-7d2bf1c3...}`, `{093FF999-1EA0-4079-9525-9614C35...}` expanded) showing its subkeys **Implemented Categories**, **InProcServer32**, **ProgID**, **Programmable**, **TypeLib**.

`InProcServer32` values:

| Name | Type | Data |
|---|---|---|
| (Default) | REG_SZ | `C:\Windows\System32\wshom.ocx` |
| ThreadingModel | REG_SZ | `Apartment` |

2026 11

## Slide 12

#### DomainCheck.exe – main()

12

```cpp
int main()
{
    HRESULT hr = CoInitializeEx(0, COINIT_APARTMENTTHREADED);

    // 1. Resolve ProgID to CLSID
    CLSID clsid;
    hr = CLSIDFromProgID(L"WScript.Network", &clsid);

    // 2. Create COM object and request IWshNetwork2 interface
    IWshNetwork2* pNet = nullptr;
    hr = CoCreateInstance(
        clsid,
        nullptr,
        CLSCTX_INPROC_SERVER,
        IID_IWshNetwork2,
        (void**)&pNet
    );

    // 3. Call methods through COM interface
    BSTR computerName = nullptr;
    BSTR userDomain = nullptr;

    hr = pNet->get_ComputerName(&computerName);
    hr = pNet->get_UserDomain(&userDomain);

    if (SUCCEEDED(hr))
    {
        std::wcout << L"Computer : " << computerName << std::endl;
        std::wcout << L"Domain   : " << userDomain << std::endl;
    }

    SysFreeString(computerName);
    SysFreeString(userDomain);

    pNet->Release();
    CoUninitialize();

    return 0;
}
```

2026 12

## Slide 13

#### DomainCheck.exe – main()

13

```text
[29-03-2026 12:37:53] PS C:\Users\mandi\Documents\tools> .\DomainCheck.exe
Computer : WINAZAD
Domain   : WINAZAD
```

`DomainCheck.exe (8268) Properties` — **Modules** tab:

| Name | Base address | Size | Description |
|---|---|---:|---|
| DomainCheck.exe | 0x7ff6bfc90000 | 9.17 MB | |
| icu.dll | 0x7ffebd690000 | 2.18 MB | ICU Combined Library |
| imm32.dll | 0x7ffed0730000 | 188 kB | Multi-User Windows IMM32 API Client DLL |
| kernel32.dll | 0x7ffecf840000 | 776 kB | Windows NT BASE API Client DLL |
| ntdll.dll | 0x7ffed1010000 | 1.97 MB | NT Layer DLL |
| uxtheme.dll | 0x7ffecc040000 | 632 kB | Microsoft UxTheme Library |
| wshom.ocx | 0x7ffebbbc0000 | 164 kB | Windows Script Host Runtime Library |

Process Monitor trace, process `DomainCheck.exe` (PID 4504):

```text
RegOpenKey     HKCR\WScript.Network\CLSID
RegQueryValue  HKCR\WScript.Network\CLSID\(Default)
RegOpenKey     HKCU\Software\Classes\CLSID\{093FF999-1EA0-4079-9525-9614C3504B74}\InProcServer32
RegQueryValue  HKCR\CLSID\{093FF999-1EA0-4079-9525-9614C3504B74}\InProcServer32\(Default)
Load Image     C:\Windows\System32\wshom.ocx
```

2026 13

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

1. **CLIENT** – Calls `CoCreateInstance( CLSID )` to request a COM object
2. **SCM** – Finds CLSID in registry → retrieves the associated AppID *(unlike normal in-process COM, SCM now checks whether the COM class has an AppID)*
3. **SCM** – Detects `DllSurrogate` registry value under the AppID *(signals that this DLL should not be loaded into the client process)*
4. **SCM** – Launches (or reuses) `dllhost.exe` *(instead of loading the DLL into the client, Windows starts the COM Surrogate process)*
5. **DLLHOST.EXE** – Loads the COM DLL and creates the COM object *(the DLL executes inside dllhost.exe — not inside the client application)*
6. **CLIENT** – Communicates with the COM object through COM / RPC *(behaves like a normal COM object — even though it is running in another process)*

2026 16

## Slide 17

#### Windows Sessions - Isolation Model

- Windows sessions isolate user environments and system services

- Sessions separate security boundaries

- Cross-session communication requires OS-managed IPC

17

**Session 0** (non-interactive, system services): `services.exe` (Service Control Manager), `svchost.exe` (Host Process for Services), **COM / DCOM Infrastructure** (DcomLaunch · svchost (DCOM) · dllhost.exe)

**Session 1+** (interactive, user sessions): **User Desktop** (winsta0\Default), **Applications** (GUI · interactive processes), **User Processes** (explorer.exe · notepad.exe · chrome.exe)

Between them: Desktop/Window Station Isolation, Security Token Isolation and Process & Handle Isolation all block direct access — only COM/DCOM · RPC · Named Pipes, as OS-managed IPC, are allowed to cross the boundary.

## Slide 18

#### Session Monikers

- Session Monikers allow COM objects to be activated in a specific Windows session

- Extends normal COM activation by adding a target session identifier

- Uses existing Windows COM activation infrastructure

\```
Format:
\```

Session Monikers provide a legitimate way to route COM activation into another Windows session.

18

## Slide 19

#### Session Monikers – Activation Flow

19

1. **CLIENT** – `CoGetObject("session:N!new:{CLSID}")`
2. **COM RUNTIME — OLE32.DLL** – Resolves the session moniker and extracts the target CLSID
3. **RPCSS / COM ACTIVATION INFRASTRUCTURE** – Routes the activation request to Session N on the target machine
4. **SESSION N — COM INFRASTRUCTURE** – Receives activation request and resolves the COM server type from registry
5. Either **DLLHOST.EXE** – spawned as COM Surrogate when `DllSurrogate` is configured under AppID — **or OTHER COM SERVER** – launched as a registered EXE or reused in-process server

2026 19

## Slide 20

#### DcomLaunch - The COM Activation Broker

- Runs as **svchost.exe -k DcomLaunch** with SYSTEM privileges

- Machine-level COM registration under HKLM is used for DCOM surrogate activation

- Resolves AppID configuration → DllSurrogate="" triggers COM Surrogate (dllhost.exe) activation

20

## Slide 21

#### Evolution of COM Abuse Techniques

21

| Technique | CLSID | Random per run |
|---|---|---|
| BitlockMove | Existing (hardcoded) | No |
| DCOMRunAs | Existing (operator supplied) | No |
| COMouflage | Custom (static) | No |
| SessionHop | Existing (hardcoded) | No |
| BYOC | Custom (random) | Yes |

2026 21

## Slide 22

#### The Idea - Bring Your Own COM

- Generate a unique CLSID and AppID at runtime

- Create a temporary COM registration in HKLM

- Trigger COM activation through Session Moniker or DCOM

- Windows activates the object through the native surrogate path: svchost.exe (DcomLaunch) → dllhost.exe

- dllhost.exe loads the COM DLL and executes the payload

- Remove the temporary COM registration after activation

**Key Characteristics**

- No Traditional COM Hijacking
- Runtime-generated CLSID Identity
- Ephemeral COM Registration
- Native COM Activation Path

22

## Slide 23

#### Registry Staging - What Gets Written

23

Registry root `HKLM\Software\Classes` branches into:

- Key **CLSID** → CLSID key `{Random CLSID}` →
  - value `AppID` = `{Random AppID}`
  - subkey `InprocServer32` → value `(Default)` = `payload.dll`, value `ThreadingModel` = `Both`
- Key **AppID** → AppID key `{Random AppID}` →
  - value `DllSurrogate` = `""`

Writing `DllSurrogate` under the AppID key triggers DCOM infrastructure COM activation, which spawns the surrogate process `dllhost.exe`, which loads `payload.dll`.

2026 23

## Slide 24

#### COM Activation - Session Pivot

24

1. **Generate GUIDs** – `CLSID = CoCreateGuid()`, `AppID = CoCreateGuid()`; random every run, never seen before
2. **Stage Registry** – `CLSID\{X}\InprocServer32` → `payload.dll`; `AppID\{X}` → `DllSurrogate=""`, `RunAs=Interactive User`
3. **Session Moniker** – `CoGetObject( session:N!new:{CLSID} )`; no `CreateProcess` by caller
4. **DcomLaunch Activation** – svchost (DcomLaunch) receives activation request, starts `dllhost.exe` as COM Surrogate
5. **Payload Executes** – `dllhost.exe` loads `payload.dll`, `DllGetClassObject()`, COM object created; keys deleted after call

USA 2026 24

## Slide 25

#### COM Activation - Lateral Movement

25

1. **Generate GUIDs** – `CLSID = CoCreateGuid()`, `AppID = CoCreateGuid()`; random every run, never seen before
2. **Remote COM Registration** – Remote Registry write to target (HKLM): `CLSID\{X}\InprocServer32` → `payload.dll` (on target); `AppID\{X}` → `DllSurrogate=""`
3. **Remote DCOM Activation** – `CoCreateInstanceEx()`; CLSID, remote server, target host; activation request sent
4. **Target DcomLaunch** – COM activation handled on target; DcomLaunch starts `dllhost.exe` as COM Surrogate
5. **Payload Executes** – `dllhost.exe` loads the COM DLL, `DllGetClassObject()`, COM object created; cleanup — registration removed

2026 25

## Slide 26

### DEMO – Session Pivoting

26


> Recovered by OCR — confidence 78/100 on the text kept, 59/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
DEMO — Session Pivoting
Cy OBS 32.1.2 - Profile: Untitled - Scenes: Untitled
File Edit View Docks Profile SceneCollection Tools Help
Scenes a
© Display Capture oa = = : = :
© Display Capture @ Properties ® Filters Display : 1920x1080 @ 0,0 (Primary Monitor) a
Audio Mixer Scene Transitions = Controls
Global Global
Desktop Audio Y Mic/Aux Fade ’ Start Streaming
Q Duration 300ms Start Ragording
me Studio Mode
x x Settings
Se a © a 0 hidden 6 + Options ~
00:00:00 00:00:00 CPU:11.6% 30.00/ 30.00 FPS
5:27 PM
26
26
```

## Slide 27

### DEMO – Lateral Movement

27


> Recovered by OCR — confidence 80/100 on the text kept, 60/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
DEMO — Lateral Movement
- Profile: Untitled - Scenes: Untitled
File Edit View Docks Profile SceneCollection Tools Help
main —_— i
© Display Capture @ Properties ® Filters Display : 1920x1080 @ 0,0 (Primary Monitor) +.
Audio Mixer Scene Transitions Controls a
Global Global
2 + Wi: Start Virtual Camera a
x x Settings
+W @av 0 hidden 6 + Options w
Recording saved to 'C:/Users/sheb/Videos/2026-06-28 17-46-39.mp4' 0 ) 00:00 CPU: 12.3% 30.00 / 30.00 FPS
27
```

## Slide 28

# DEMO

- Session pivot - cross-session execution via session moniker

Terminal output of a Cobalt Strike-style BOF (`SurrogateExec.x64.o`):

```text
SurrogateExec.x64.o "z:session" "z:4" "z:C:\Users\Public\SurrogateExec2.0\Finalcitrix3.dll"

Task Success
BOF Size: 9336 Args Size: 72
[*] Mode  : Cross-Session Pivot
[*] CLSID : {B33F0DBE-6007-4F3C-B62D-06F3CFA401E4}
[*] AppID : {A7957CE6-D524-48B6-BD88-04DE79143E8A}
[*] Staging registry keys...
[+] Registry staged
[*] Moniker: session:4!new:B33F0DBE-6007-4F3C-B62D-06F3CFA401E4
[+] Cross-session pivot triggered in session 4
[+] Registry keys removed - execution trace gone

[*] a new implant checked-in - Psalms-DC
```

##### Remote lateral movement - DCOM activation across machines

```text
SurrogateExec.x64.o "z:remote" "z:192.168.1.6" "z:\\192.168.1.6\C$\Users\Public\SurrogateExec2.0\Finalcitrix3.dll"

Task Success
BOF Size: 9336 Args Size: 95
[*] Mode  : Remote Lateral Movement
[*] CLSID : {0A281FA9-493E-4A11-8EE6-83D6A270D08C}
[*] AppID : {60A93884-8093-4B8B-8E4A-F14613244348}
[*] Connected to remote registry: 192.168.1.6
[*] Staging registry keys...
[+] Registry staged
[*] Triggering remote DCOM on 192.168.1.6...
[+] Remote lateral movement triggered on 192.168.1.6
[+] Registry keys removed - execution trace gone

[*] a new implant checked-in - Psalms-DC
```

28

## Slide 29

## Detection Signals

29

Four detection panels:

**Ephemeral COM Registration**
- Behavior: custom CLSID/AppID registration
- Example: `HKLM\SOFTWARE\Classes\CLSID\{GUID}`, `HKLM\SOFTWARE\Classes\AppID\{GUID}`
- Telemetry: Sysmon EID 12 (Registry Key Create/Delete), Sysmon EID 13 (Registry Value Set)
- Artifact: COM registration created outside normal software installation workflows

**COM Surrogate Activation**
- Behavior: COM activation through surrogate hosting
- Example: `dllhost.exe /Processid:{GUID}`
- Telemetry: Sysmon EID 1 (Process Creation), Security Log 4688 (Process Creation), command-line GUID analysis (correlation)
- Artifact: dllhost.exe activation associated with COM registrations created by non-installer processes

**COM Activation Telemetry**
- Behavior: session moniker-based COM activation
- Example: `session:<N>!new:{CLSID}`
- Telemetry: ETW Microsoft-Windows-COM-Perf, ETW Microsoft-Windows-RPC
- Artifact: COM activation using session moniker syntax from non-standard processes

**COM Server DLL Loading**
- Behavior: COM server DLL loaded from non-standard locations
- Examples: `\\server\share\payload.dll`, `C:\Temp\payload.dll`, `C:\Users\Public\payload.dll`
- Telemetry: Sysmon EID 7 (Image Load)
- Artifact: dllhost.exe loading DLLs from UNC paths or user-writable locations

2026 29

## Slide 30

## Q&A

30

## Slide 31

## Thank You

31
