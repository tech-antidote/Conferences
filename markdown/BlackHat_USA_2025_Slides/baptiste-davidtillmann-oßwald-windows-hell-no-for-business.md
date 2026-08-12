---
title: "Windows Hell No for Business"
speakers: ["Baptiste David", "Tillmann Oßwald"]
conference: "Black Hat"
conference_full: "Black Hat USA 2025"
edition: "USA"
year: 2025
source_pdf: "BlackHat_USA_2025_Slides/Baptiste David&Tillmann Oßwald_Windows Hell No for Business.pdf"
pages: 151
sha256: "f74051c9a216f98c3e77a8a2591aa1b13f4b5ed1c57686ff0cd3475526872128"
text_chars: 46986
ocr_pages: 27
has_ocr: true
redacted_secrets: 0
ocr_confidence: 85.6
ocr_unreliable_blocks: 4
vision_verified_blocks: 5
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T05:08:59Z"
---
# Windows Hell No for Business

**Speakers:** Baptiste David, Tillmann Oßwald  
**Conference:** Black Hat USA 2025  
**Source:** `BlackHat_USA_2025_Slides/Baptiste David&Tillmann Oßwald_Windows Hell No for Business.pdf` (151 pages)


## Slide 1

## Windows Hell No for Business

Dr Baptiste David    Tillmann Oßwald <u>bdavid@ernw.de tosswald@ernw.de</u>

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 85/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
AUGUST 6-7, 2025
MANDALAY BAY / LAS VEGAS
Windows Hell No for Business
Dr Baptiste David Tillmann Ofwald
bdavid@ernw.de tosswald@ernw.de
```

## Slide 2

#### “Windows Dissected”

- Funded by the German Federal Office for IT Security, carried out by ERNW

- “ _Various in-depth security analyses of security-critical components and functions in Windows…_ ”

- Started in 2024, planned to end in spring 2026

- Various work packages including

   - Windows Hello for Business

   - eXtended Control Flow Guard – state of the art and limitations

   - Code Integrity – caching and  known bypasses

   - Group Policy Objects – processing flow

2025

2

## Slide 3

#### Who am I?

- Tillmann Osswald

- **ERNW Enno Rey Netzwerke GmbH**

   - Security researcher and Windows System Analyst

   - Since 2015

   - "Make the world a safer place"

- Master degree in IT security from the University of Applied Sciences Darmstadt.

- • Reverse engineering Windows components.

2025

3

## Slide 4

#### Who am I?

- Dr David Baptiste

- I am         and I work in

- **ERNW Enno Rey Netzwerke GmbH**

   - Computer security service in Heidelberg, Germany

   - “Make the World a Safer Place!”

- Did many conferences

   - Black Hat USA, DefCon, EICAR, Recon, …

   - And also, one called TROOPERS

- I like good food and good wine

2025

4

## Slide 5

# Windows Hello for Business

As a whole

2025

5

## Slide 6

#### Say Hello to Windows Hello

2025

6


> Recovered by OCR — confidence 84/100 on the text kept, 73/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
® ®
Windows Hello
Thursday, July 30 *
2025 6
```

## Slide 7

#### What is Windows Hello for Business?

- Windows Hello for Business is Microsoft’s passwordless flagship

   - Windows Recall, Passkey, ...

- Build on two key principals

   - Identification    -> Windows Hello …

   - Authentication -> … for Business

2025

7

## Slide 8

#### Windows Hello for Business – Enrollment

2025

8


> Recovered by OCR — confidence 88/100 on the text kept, 62/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
BRIEFINGS = Wa \
ij
Windows Hello for Business — Enrollment
```

## Slide 9

#### Windows Hello for Business – Enrollment

User ID Key

2025

8

## Slide 10

#### Windows Hello for Business – Enrollment

User ID Key
Public Key Private Key

2025

8

## Slide 11

#### Windows Hello for Business – Enrollment

Azure AD Domain
Services
User ID Key
Public Key Private Key

2025

8

## Slide 12

#### Windows Hello for Business – Enrollment

Azure AD Domain Services

User ID Key
Public Key Private Key
Has TPM?
Software TPM storage

2025

8

## Slide 13

#### Windows Hello for Business

2025

9


> Recovered by OCR — confidence 89/100 on the text kept, 70/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
BRIEFINGS = Uf \
Windows Hello for Business
```

## Slide 14

#### Windows Hello for Business

Biometric
Templates
Windows Hello
Gesture

2025

9

## Slide 15

#### Windows Hello for Business

Biometric
Templates
Windows Hello Gesture
Gesture
Gestures

2025

9

## Slide 16

#### Windows Hello for Business

Biometric  Protector Key
Templates
Protector Key
Windows Hello Gesture
Gesture
Protector Key
Protector Key
Gestures

2025

9

## Slide 17

#### Windows Hello for Business

Biometric  Protector Key Authentication Key
Templates
Authentication
Protector Key Key
Windows Hello Gesture
Gesture
Authentication
Protector Key Key
Authentication
Protector Key
Key
Gestures

2025

9

## Slide 18

#### Windows Hello for Business

Biometric  Protector Key Authentication Key
Templates
Authentication
Protector Key Key
Windows Hello Gesture
Gesture
Authentication
Protector Key Key
Authentication
Protector Key
Key
Gestures

2025

9

## Slide 19

#### Windows Hello for Business

Biometric  Protector Key Authentication Key
Templates
Authentication
Protector Key Key
Windows Hello Gesture
Gesture
Authentication
Protector Key Key
Authentication
Protector Key
Key
Gestures

2025

9

## Slide 20

#### Windows Hello for Business

Biometric
Templates
Windows Hello Protector Key
Gesture

2025

9

## Slide 21

#### Windows Hello for Business

Biometric
Templates
Authentication
Windows Hello Protector Key
Key
Gesture

2025

9

## Slide 22

#### Windows Hello for Business

Biometric
Templates
Authentication
Windows Hello User ID Key
Protector Key
Key
Gesture

2025

9

## Slide 23

#### Windows Hello for Business

Biometric
Templates
Authentication
Windows Hello User ID Key
Protector Key
Key
Gesture Azure AD Domain
Services

2025

9

## Slide 24

#### Windows Hello for Business

Biometric
Templates
Authentication
Windows Hello User ID Key
Protector Key
Key
Gesture Azure AD Domain
Services

2025

9

## Slide 25

#### Windows Hello for Business

Biometric
Templates
Authentication
Windows Hello User ID Key
Protector Key
Key
Gesture Azure AD Domain
Services

2025

9

## Slide 26

# Windows Hello for Business

Internals

2025

10

## Slide 27

#### Windows Hello

- Simplified view

2025

11


> Recovered by OCR — confidence 90/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Windows Hello
¢ Simplified view
```

## Slide 28

#### Windows Hello

- Simplified view

2025

11


> Recovered by OCR — confidence 90/100 on the text kept, 73/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Windows Hello
¢ Simplified view
Be
```

## Slide 29

#### Windows Hello

##### • Simplified view

User-Mode

Kernel Mode

USB Driver

Hardware

2025

11

## Slide 30

#### Windows Hello

##### • Simplified view

###### User-Mode

Kernel Mode

Manufacturer
Driver
USB Driver

###### Hardware

2025

11

## Slide 31

#### Windows Hello

##### • Simplified view

###### User-Mode

Kernel Mode
Biometric
Driver
010010011011
Manufacturer
Driver
USB Driver

Hardware

2025

11

## Slide 32

#### Windows Hello

##### • Simplified view

Windows Biometric Service
010010011011
User-Mode
Kernel Mode
Biometric
Driver
Manufacturer
Driver
USB Driver
Hardware

2025

11

## Slide 33

#### Windows Hello

##### • Simplified view

Windows Biometric Service

###### User-Mode

Kernel Mode

Biometric
Driver
Manufacturer
Driver
USB Driver

Hardware

2025

11

## Slide 34

#### Windows Hello

##### • Simplified view

Windows Biometric Service

###### User-Mode

Kernel Mode

Biometric
Driver
Manufacturer
Driver
USB Driver

Hardware

2025

11

## Slide 35

#### Windows Hello

##### • Simplified view

Windows Biometric Service

###### User-Mode

Kernel Mode

Biometric
Driver
Manufacturer
Driver
USB Driver

010010011011

Hardware

2025

11

## Slide 36

#### Windows Hello

##### • Simplified view

Windows Biometric Service

###### User-Mode

Kernel Mode

Biometric
Driver
Manufacturer
Driver
USB Driver USB Driver

Hardware
010010011011

2025

11

## Slide 37

#### Windows Hello

##### • Simplified view

Windows Biometric Service

User-Mode

Kernel Mode

Biometric
Driver
Manufacturer
Driver
USB Driver USB Driver
010010011011

Hardware

2025

11

## Slide 38

#### Windows Hello

##### • Simplified view

Windows Biometric Service

###### User-Mode

Biometric  Biometric
Driver Driver
Manufacturer  Manufacturer
Driver Driver
USB Driver USB Driver
010010011011

Kernel Mode

Hardware

2025

11

## Slide 39

#### Windows Hello

##### • Simplified view

Windows Biometric Service

###### User-Mode

Biometric  Biometric
Driver Driver
010010011011
Manufacturer  Manufacturer
Driver Driver
USB Driver USB Driver

Kernel Mode

Hardware

2025

11

## Slide 40

#### Windows Hello

##### • Simplified view

Windows Biometric Service
010010011011
User-Mode
Kernel Mode
Biometric  Biometric
Driver Driver
Manufacturer  Manufacturer
Driver Driver
USB Driver USB Driver

Hardware

2025

11

## Slide 41

#### Windows Hello

• Simplified view

Manufacturer
Software
Windows Biometric Service

###### User-Mode

Kernel Mode
Biometric  Biometric
Driver Driver
Manufacturer  Manufacturer
Driver Driver
USB Driver USB Driver

Hardware

2025

11

## Slide 42

#### Windows Hello

Windows Hello Manufacturer  Template
Software Database
• Simplified view
Windows Biometric Service

###### User-Mode

Biometric  Biometric
Driver Driver
Manufacturer  Manufacturer
Driver Driver
USB Driver USB Driver

Kernel Mode

Hardware

2025

11

## Slide 43

#### Windows Hello

• Simplified view

Manufacturer  Template
Software Database
Windows Biometric Service

###### User-Mode

Kernel Mode
Biometric  Biometric
Driver Driver
Manufacturer  Manufacturer
Driver Driver
USB Driver USB Driver

Hardware

2025

11

## Slide 44

#### Windows Hello

Windows Hello Manufacturer  Template
Software Database
WinBio API
• Simplified view
Client
Windows Biometric Service
Application
User-Mode

Kernel Mode
Biometric  Biometric
Driver Driver
Manufacturer  Manufacturer
Driver Driver
USB Driver USB Driver

Hardware

2025

11

## Slide 45

Windows Hello Manufacturer  Template
Software Database
WinBio API
• Simplified view
Client
Windows Biometric Service
Application
User-Mode
Kernel Mode
Biometric  Biometric
Driver Driver
Manufacturer  Manufacturer
Driver Driver
USB Driver USB Driver

Hardware

2025

11

## Slide 46

Windows Hello Manufacturer  Template
Software Database
WinBio API
R
 Simplified view
P
Client
Windows Biometric Service
C Application
User-Mode
Kernel Mode
Biometric  Biometric
Driver Driver
Manufacturer  Manufacturer
Driver Driver
USB Driver USB Driver

#### Windows Hello

• Simplified view

Hardware

2025

11

## Slide 47

#### Windows Hello

• Simplified view

Manufacturer  Template
Software Database
WinBio API
R
P
Client
Windows Biometric Service
C Application

###### User-Mode

Kernel Mode
Biometric  Biometric
Driver Driver
Manufacturer  Manufacturer
Driver Driver
USB Driver USB Driver
Hardware

2025

11

## Slide 48

#### Windows Hello

• Simplified view

Manufacturer  Template
Software Database
WinBio API
R
P
Client
Windows Biometric Service
C Application

User-Mode

Kernel Mode
Biometric  Biometric
Driver Driver
Manufacturer  Manufacturer
Driver Driver
USB Driver USB Driver
Hardware

2025

11

## Slide 49

#### Windows Hello

• Simplified view

Manufacturer  Template
Software Database
WinBio API
R
P
Client
Windows Biometric Service
C Application

User-Mode

Kernel Mode
Biometric  Biometric
Driver Driver
Manufacturer  Manufacturer
Driver Driver
USB Driver USB Driver
Hardware

2025

11

## Slide 50

#### Windows Biometric Service – Initialization

RegisterServiceCtrlHandlerExW

2025

12

## Slide 51

#### Windows Biometric Service – Initialization

RegisterServiceCtrlHandlerExW CDatabaseManager::CDatabase
Manager
CDatabaseManager::InitializeSe
CServer::Initialize CDatabaseManager
rviceDirectory
CDatabaseManager::RegisterAll

2025

12

## Slide 52

#### Windows Biometric Service – Initialization

RegisterServiceCtrlHandlerExW CDatabaseManager::CDatabase
Manager
CDatabaseManager::InitializeSe
CServer::Initialize CDatabaseManager
rviceDirectory
CDatabaseManager::RegisterAll
CHardwareManager::Initialize
CFocusMonitor::Initialize
CDataProtector::TryEnforcePolicy

2025

12

## Slide 53

#### Windows Biometric Service – Initialization

RegisterServiceCtrlHandlerExW CDatabaseManager::CDatabase
Manager
CDatabaseManager::InitializeSe
CServer::Initialize CDatabaseManager
rviceDirectory
CDatabaseManager::RegisterAll
CHardwareManager::Initialize TPM Check
CFocusMonitor::Initialize
Refresh the policy and potentially,
CDataProtector::TryEnforcePolicy removes TPM/registry sensitive content.

2025

12

## Slide 54

#### Windows Biometric Service – Initialization

RegisterServiceCtrlHandlerExW CDatabaseManager::CDatabase
Manager
CDatabaseManager::InitializeSe
CServer::Initialize CDatabaseManager
rviceDirectory
CDatabaseManager::RegisterAll
CHardwareManager::Initialize
CFocusMonitor::Initialize
CDataProtector::TryEnforcePolicy

2025

12

## Slide 55

#### Windows Biometric Service – Initialization

RegisterServiceCtrlHandlerExW CDatabaseManager::CDatabase
Manager
CDatabaseManager::InitializeSe
CServer::Initialize CDatabaseManager
rviceDirectory
CDatabaseManager::RegisterAll
CHardwareManager::Initialize
CFocusMonitor::Initialize
CDataProtector::TryEnforcePolicy
CAccountManager::Instance

2025

12

## Slide 56

#### Windows Biometric Service – Initialization

RegisterServiceCtrlHandlerExW CDatabaseManager::CDatabase
Manager
CDatabaseManager::InitializeSe
CServer::Initialize CDatabaseManager
rviceDirectory
CDatabaseManager::RegisterAll
CHardwareManager::Initialize
CFocusMonitor::Initialize
CDataProtector::TryEnforcePolicy
CFingerprintBsp::Create
CAccountManager::Instance
CFacialFeaturesBsp::Create
Bio Unit Creation
CIrisBsp::Create
CVoiceBsp::Create
CBootstrapBsp::Create

2025

12

## Slide 57

#### Windows Biometric Service – Initialization

RegisterServiceCtrlHandlerExW CDatabaseManager::CDatabase
Manager
CDatabaseManager::InitializeSe
CServer::Initialize CDatabaseManager
rviceDirectory
CDatabaseManager::RegisterAll
CHardwareManager::Initialize
CFocusMonitor::Initialize
CDataProtector::TryEnforcePolicy
CFingerprintBsp::Create
CAccountManager::Instance
CFacialFeaturesBsp::Create
Bio Unit Creation
CIrisBsp::Create
CVoiceBsp::Create
CBootstrapBsp::Create

2025

12

## Slide 58

#### Windows Biometric Service – Initialization

RegisterServiceCtrlHandlerExW CDatabaseManager::CDatabase
Manager
CDatabaseManager::InitializeSe
CServer::Initialize CDatabaseManager
rviceDirectory
CDatabaseManager::RegisterAll
CHardwareManager::Initialize
CFocusMonitor::Initialize
CDataProtector::TryEnforcePolicy
CFingerprintBsp::Create
CAccountManager::Instance
CFacialFeaturesBsp::Create
Bio Unit Creation CServer::Instance
CIrisBsp::Create
CVoiceBsp::Create
CBootstrapBsp::Create

2025

12

## Slide 59

#### Windows Biometric Service – Initialization

RegisterServiceCtrlHandlerExW CDatabaseManager::CDatabase
Manager
CDatabaseManager::InitializeSe
CServer::Initialize CDatabaseManager
rviceDirectory
CDatabaseManager::RegisterAll
CHardwareManager::Initialize
CFocusMonitor::Initialize
CDataProtector::TryEnforcePolicy
CFingerprintBsp::Create
CAccountManager::Instance
CFacialFeaturesBsp::Create
Bio Unit Creation CServer::Instance
CIrisBsp::Create
CRpcDispatcher
CVoiceBsp::Create
CBootstrapBsp::Create

2025

12

## Slide 60

#### Windows Biometric Service – Initialization

RegisterServiceCtrlHandlerExW CDatabaseManager::CDatabase
Manager
CDatabaseManager::InitializeSe
CServer::Initialize CDatabaseManager
rviceDirectory
CDatabaseManager::RegisterAll
RPC Interface CHardwareManager::Initialize
CRpcDispatcher::Instance CFocusMonitor::Initialize
RpcServerInterfaceGroupActivate
CDataProtector::TryEnforcePolicy
CFingerprintBsp::Create
CAccountManager::Instance
CFacialFeaturesBsp::Create
Bio Unit Creation CServer::Instance
CIrisBsp::Create
CRpcDispatcher
CVoiceBsp::Create
CBootstrapBsp::Create

2025

12

## Slide 61

#### Windows Biometric Service – Initialization

RegisterServiceCtrlHandlerExW CDatabaseManager::CDatabase
Manager
CDatabaseManager::InitializeSe
CServer::Initialize CDatabaseManager
rviceDirectory
CDatabaseManager::RegisterAll
RPC Interface CHardwareManager::Initialize
CRpcDispatcher::Instance CFocusMonitor::Initialize
RpcServerInterfaceGroupActivate CHardwareManager
CDataProtector::TryEnforcePolicy
CFingerprintBsp::Create
CAccountManager::Instance
CFacialFeaturesBsp::Create
Bio Unit Creation CServer::Instance
CIrisBsp::Create
CRpcDispatcher
CVoiceBsp::Create
CBootstrapBsp::Create

2025

12

## Slide 62

#### Windows Biometric Service – Initialization

RegisterServiceCtrlHandlerExW CDatabaseManager::CDatabase
Manager
CDatabaseManager::InitializeSe
CServer::Initialize CDatabaseManager
rviceDirectory
CDatabaseManager::RegisterAll
RPC Interface CHardwareManager::Initialize
CRpcDispatcher::Instance CFocusMonitor::Initialize
RpcServerInterfaceGroupActivate CHardwareManager
CDataProtector::TryEnforcePolicy
CFingerprintBsp::Create
CAccountManager::Instance
CFingerprintBsp::Create
CFacialFeaturesBsp::Create
Bio Unit Creation CServer::Instance
CFingerprintBsp::Create
CIrisBsp::Create
CHardwareManager::CHardwar
eManager
CFingerprintBsp::Create CRpcDispatcher
CVoiceBsp::Create
CFingerprintBsp::Create
CBootstrapBsp::Create

2025

12

## Slide 63

#### Windows Biometric Service – Configuration

2025

13


> Recovered by OCR — confidence 83/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Databases
Parameters
Security
v Service Providers
iv Bootstrap
v Virtual Sensors
v FacialFeatures
vw Fingerprint
vw Iris
vw Voice
v Virtual Sensors
/ Configurations
```

## Slide 64

#### Windows Biometric Service – Configuration

2025

13


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 83/100 on the text kept, 75/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Windows Biometric Service – Configuration

Left panel (registry tree, regedit screenshot):
∨ WbioSrvc
  ∨ Databases
      {51F39552-1075-4199-B513-0C10EA185DB0}
      {A61A7480-6A54-4D36-A0EF-B150B8545827}
      {DC576DA6-D676-4A15-906D-C0CEAF949543}
    Parameters
    Security
  ∨ Service Providers
    ∨ Bootstrap
        Global Configurations
      ∨ Virtual Sensors
        ∨ {0527b250-7514-4321-8b68-41c65f956998}
          ∨ Configurations
              0
    ∨ FacialFeatures
        Global Configurations
        Virtual Sensors
    ∨ Fingerprint
        Global Configurations
        Virtual Sensors
    ∨ Iris
        Global Configurations
        Virtual Sensors
    ∨ Voice
        Global Configurations
      ∨ Virtual Sensors
        ∨ {F25AB4A2-593A-4A89-B9FF-8144BEA81E15}
          ∨ Configurations
              0

Right panel (regedit screenshot):
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\WbioSrvc\Databases\{DC576DA6-D676-4A15-906D-C0CEAF949543}

Left pane (registry tree):
    wbengine
  ∨ WbioSrvc
    ∨ Databases
        {51F39552-1075-4199-B513-0C10EA185DB0}
        {A61A7480-6A54-4D36-A0EF-B150B8545827}
        {DC576DA6-D676-4A15-906D-C0CEAF949543}   (selected)
      Parameters
      Security
    > Service Providers
    > TriggerInfo
      WBDI

Right pane (values):
| Name | Type | Data |
| (Default) | REG_SZ | (value not set) |
| Attributes | REG_DWORD | 0x00000001 (1) |
| AutoCreate | REG_DWORD | 0x00000001 (1) |
| AutoName | REG_DWORD | 0x00000000 (0) |
| BiometricType | REG_DWORD | 0x00000002 (2) |
| ConnectionString | REG_SZ | |
| FilePath | REG_SZ | C:\WINDOWS\SYSTEM32\WINBIODATABASE\DC576DA6-D676-4A15-906D-C0CEAF949543.DAT |
| Format | REG_SZ | 5B3FBA54-792B-40C7-8822-2EFC0A255F78 |
| InitialSize | REG_DWORD | 0x00000020 (32) |

(Red annotation boxes highlight the three Databases GUID subkeys in both trees, and in the
right pane the BiometricType row and the FilePath row.)

2025    13
```

## Slide 65

#### Windows Biometric Service – Configuration

2025

13


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 77/100 on the text kept, 60/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Windows Biometric Service – Configuration

Left panel (registry tree, regedit screenshot):
∨ WbioSrvc
  ∨ Databases
      {51F39552-1075-4199-B513-0C10EA185DB0}
      {A61A7480-6A54-4D36-A0EF-B150B8545827}
      {DC576DA6-D676-4A15-906D-C0CEAF949543}
    Parameters
    Security
  ∨ Service Providers
    ∨ Bootstrap
        Global Configurations
      ∨ Virtual Sensors
        ∨ {0527b250-7514-4321-8b68-41c65f956998}
          ∨ Configurations
              0
    ∨ FacialFeatures
        Global Configurations
        Virtual Sensors
    ∨ Fingerprint
        Global Configurations
        Virtual Sensors
    ∨ Iris
        Global Configurations
        Virtual Sensors
    ∨ Voice
        Global Configurations
      ∨ Virtual Sensors
        ∨ {F25AB4A2-593A-4A89-B9FF-8144BEA81E15}
          ∨ Configurations
              0

Right panel (regedit screenshot):
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\WbioSrvc\Databases\{DC576DA6-D676-4A15-906D-C0CEAF949543}

Left pane (registry tree):
    wbengine
  ∨ WbioSrvc
    ∨ Databases
        {51F39552-1075-4199-B513-0C10EA185DB0}
        {A61A7480-6A54-4D36-A0EF-B150B8545827}
        {DC576DA6-D676-4A15-906D-C0CEAF949543}   (selected)
      Parameters
      Security
    > Service Providers
    > TriggerInfo
      WBDI

Right pane (values):
| Name | Type | Data |
| (Default) | REG_SZ | (value not set) |
| Attributes | REG_DWORD | 0x00000001 (1) |
| AutoCreate | REG_DWORD | 0x00000001 (1) |
| AutoName | REG_DWORD | 0x00000000 (0) |
| BiometricType | REG_DWORD | 0x00000002 (2) |
| ConnectionString | REG_SZ | |
| FilePath | REG_SZ | C:\WINDOWS\SYSTEM32\WINBIODATABASE\DC576DA6-D676-4A15-906D-C0CEAF949543.DAT |
| Format | REG_SZ | 5B3FBA54-792B-40C7-8822-2EFC0A255F78 |
| InitialSize | REG_DWORD | 0x00000020 (32) |

(No annotation marks on this slide.)

2025    13
```

## Slide 66

#### Windows Biometric Service – Configuration

2025

13


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 79/100 on the text kept, 67/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Windows Biometric Service – Configuration

Left panel (registry tree, regedit screenshot):
∨ WbioSrvc
  ∨ Databases
      {51F39552-1075-4199-B513-0C10EA185DB0}
      {A61A7480-6A54-4D36-A0EF-B150B8545827}
      {DC576DA6-D676-4A15-906D-C0CEAF949543}
    Parameters
    Security
  ∨ Service Providers
    ∨ Bootstrap
        Global Configurations
      ∨ Virtual Sensors
        ∨ {0527b250-7514-4321-8b68-41c65f956998}
          ∨ Configurations
              0
    ∨ FacialFeatures
        Global Configurations
        Virtual Sensors
    ∨ Fingerprint
        Global Configurations
        Virtual Sensors
    ∨ Iris
        Global Configurations
        Virtual Sensors
    ∨ Voice
        Global Configurations
      ∨ Virtual Sensors
        ∨ {F25AB4A2-593A-4A89-B9FF-8144BEA81E15}
          ∨ Configurations
              0

Right panel (regedit screenshot):
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\WbioSrvc\Databases\{DC576DA6-D676-4A15-906D-C0CEAF949543}

Left pane (registry tree):
    wbengine
  ∨ WbioSrvc
    ∨ Databases
        {51F39552-1075-4199-B513-0C10EA185DB0}
        {A61A7480-6A54-4D36-A0EF-B150B8545827}
        {DC576DA6-D676-4A15-906D-C0CEAF949543}   (selected)
      Parameters
      Security
    > Service Providers
    > TriggerInfo
      WBDI

Right pane (values):
| Name | Type | Data |
| (Default) | REG_SZ | (value not set) |
| Attributes | REG_DWORD | 0x00000001 (1) |
| AutoCreate | REG_DWORD | 0x00000001 (1) |
| AutoName | REG_DWORD | 0x00000000 (0) |
| BiometricType | REG_DWORD | 0x00000002 (2) |
| ConnectionString | REG_SZ | |
| FilePath | REG_SZ | C:\WINDOWS\SYSTEM32\WINBIODATABASE\DC576DA6-D676-4A15-906D-C0CEAF949543.DAT |
| Format | REG_SZ | 5B3FBA54-792B-40C7-8822-2EFC0A255F78 |
| InitialSize | REG_DWORD | 0x00000020 (32) |

(A red annotation box encloses the whole "Service Providers" subtree in the left panel, and
the modality names Bootstrap, FacialFeatures, Fingerprint, Iris and Voice are underlined in red.)

2025    13
```

## Slide 67

#### Windows Biometric Service – Configuration

2025

13


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 77/100 on the text kept, 60/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Windows Biometric Service – Configuration

Left panel (registry tree, regedit screenshot):
∨ WbioSrvc
  ∨ Databases
      {51F39552-1075-4199-B513-0C10EA185DB0}
      {A61A7480-6A54-4D36-A0EF-B150B8545827}
      {DC576DA6-D676-4A15-906D-C0CEAF949543}
    Parameters
    Security
  ∨ Service Providers
    ∨ Bootstrap
        Global Configurations
      ∨ Virtual Sensors
        ∨ {0527b250-7514-4321-8b68-41c65f956998}
          ∨ Configurations
              0
    ∨ FacialFeatures
        Global Configurations
        Virtual Sensors
    ∨ Fingerprint
        Global Configurations
        Virtual Sensors
    ∨ Iris
        Global Configurations
        Virtual Sensors
    ∨ Voice
        Global Configurations
      ∨ Virtual Sensors
        ∨ {F25AB4A2-593A-4A89-B9FF-8144BEA81E15}
          ∨ Configurations
              0

Right panel (regedit screenshot):
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\WbioSrvc\Databases\{DC576DA6-D676-4A15-906D-C0CEAF949543}

Left pane (registry tree):
    wbengine
  ∨ WbioSrvc
    ∨ Databases
        {51F39552-1075-4199-B513-0C10EA185DB0}
        {A61A7480-6A54-4D36-A0EF-B150B8545827}
        {DC576DA6-D676-4A15-906D-C0CEAF949543}   (selected)
      Parameters
      Security
    > Service Providers
    > TriggerInfo
      WBDI

Right pane (values):
| Name | Type | Data |
| (Default) | REG_SZ | (value not set) |
| Attributes | REG_DWORD | 0x00000001 (1) |
| AutoCreate | REG_DWORD | 0x00000001 (1) |
| AutoName | REG_DWORD | 0x00000000 (0) |
| BiometricType | REG_DWORD | 0x00000002 (2) |
| ConnectionString | REG_SZ | |
| FilePath | REG_SZ | C:\WINDOWS\SYSTEM32\WINBIODATABASE\DC576DA6-D676-4A15-906D-C0CEAF949543.DAT |
| Format | REG_SZ | 5B3FBA54-792B-40C7-8822-2EFC0A255F78 |
| InitialSize | REG_DWORD | 0x00000020 (32) |

(Red annotation: one box around the Bootstrap subtree (Global Configurations, Virtual Sensors,
{0527b250-7514-4321-8b68-41c65f956998}, Configurations, 0), a second box around the
FacialFeatures subtree (Global Configurations, Virtual Sensors), and a hand-drawn arrow/loop
running from the FacialFeatures box up to the Bootstrap box.)

2025    13
```

## Slide 68

#### Windows Biometric Service – Configuration

2025

13


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 77/100 on the text kept, 60/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Windows Biometric Service – Configuration

Left panel (registry tree, regedit screenshot):
∨ WbioSrvc
  ∨ Databases
      {51F39552-1075-4199-B513-0C10EA185DB0}
      {A61A7480-6A54-4D36-A0EF-B150B8545827}
      {DC576DA6-D676-4A15-906D-C0CEAF949543}
    Parameters
    Security
  ∨ Service Providers
    ∨ Bootstrap
        Global Configurations
      ∨ Virtual Sensors
        ∨ {0527b250-7514-4321-8b68-41c65f956998}
          ∨ Configurations
              0
    ∨ FacialFeatures
        Global Configurations
        Virtual Sensors
    ∨ Fingerprint
        Global Configurations
        Virtual Sensors
    ∨ Iris
        Global Configurations
        Virtual Sensors
    ∨ Voice
        Global Configurations
      ∨ Virtual Sensors
        ∨ {F25AB4A2-593A-4A89-B9FF-8144BEA81E15}
          ∨ Configurations
              0

Right panel (regedit screenshot):
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\WbioSrvc\Databases\{DC576DA6-D676-4A15-906D-C0CEAF949543}

Left pane (registry tree):
    wbengine
  ∨ WbioSrvc
    ∨ Databases
        {51F39552-1075-4199-B513-0C10EA185DB0}
        {A61A7480-6A54-4D36-A0EF-B150B8545827}
        {DC576DA6-D676-4A15-906D-C0CEAF949543}   (selected)
      Parameters
      Security
    > Service Providers
    > TriggerInfo
      WBDI

Right pane (values):
| Name | Type | Data |
| (Default) | REG_SZ | (value not set) |
| Attributes | REG_DWORD | 0x00000001 (1) |
| AutoCreate | REG_DWORD | 0x00000001 (1) |
| AutoName | REG_DWORD | 0x00000000 (0) |
| BiometricType | REG_DWORD | 0x00000002 (2) |
| ConnectionString | REG_SZ | |
| FilePath | REG_SZ | C:\WINDOWS\SYSTEM32\WINBIODATABASE\DC576DA6-D676-4A15-906D-C0CEAF949543.DAT |
| Format | REG_SZ | 5B3FBA54-792B-40C7-8822-2EFC0A255F78 |
| InitialSize | REG_DWORD | 0x00000020 (32) |

(No annotation marks on this slide.)

2025    13
```

## Slide 69

#### Windows Biometric Service – Configuration

2025

13


> Recovered by OCR — confidence 71/100 on the text kept, 63/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
blsgisncs, Windows Biometric Serviee — Configy
v Databases wbengine A || Name Type Data
{DC576DA6-D676-4415-906D-COCEAF949543} =) esTeDAs D676-4A15-906D-COCEAFS49543} REG_DWORD 0x00000002 (2)
Parameters Security ab] ConnectionString REG_SZ
Security Service Providers 28) FilePath REG SZ C:AWINDOWS\SYSTEM32\WINBIODATABASE\DCS76DA6-D676-4A15-906D-COCEAF949543,DAT
vw Service Providers WeDI #8) InitialSize REG_DWORD 000000020 (32)
Bootstrap
Virtual 5
hua) 2eneere Parameters “|| Name Type Data
{0527b250-7514-4321-8b68-41 65956998) | Security
= Conf; i 5 p 4 ab| (Default) REG_SZ (value not set)
: onrigurations Y Tose a ers #3) Capabilities REG_DWORD 0x00000080 (128)
i 0 ¥ ootstrap ab) DeviceDescription REG_SZ Windows Hello Face Virtual Software Device
v FacialFeatures Global Configurations ie '
i ¥ Virtual Sensor Manufacturer REG_SZ Microsoft Corporation
Global Configurations B i
Virtual § q {0527b250-7514-4321-8b68-41c65¢956998} } ~ ModelName REG_SZ Windows Hello Face Virtual Sensor
i ua ensors Vv Configurations >| SerialNumber REG SZ 000000000
v Fingerprint 0 io] SubType REG_DWORD 0x00000000 (0)
Global Configurations v ) FacialFeatures #8) Version REG_QWORD 0x200000001000000 (144115188092633088)
vw Iris
vw Voice
2025 13
```

## Slide 70

#### Windows Biometric Service – Configuration

2025

13


> Recovered by OCR — confidence 86/100 on the text kept, 78/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
v Databases
Parameters
Security
v Service Providers
oy Bootstrap
: 0
vw FacialFeatures
vw Fingerprint
vw Iris
vw Voice
2025
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\WbioSrvc\Databases\{DC576DA6-D676-4A15-906D-COCEAF949543}
Windows Biometric Serviee — Config
wbengine Al] Name
{51F39552-1075-4199-B513-0C10EA185DB0}
{A6
{DC576DA6-D676-4A15-906D-COCEAF949543}
Parameters
Security ab] Connectionstring
Service Providers ab) FilePath
Tiggerinfo ab) Format
Type
REG_SZ
REG_DWORD
REG_DWORD
REG_DWORD
REG_DWORD
REG_SZ
REG_SZ
REG_SZ
REG_DWORD
Data
(value not set)
000000001 (1)
000000001 (1)
000000000 (0)
000000002 (2)
0x00000020 (32)
v
v
Parameters
Security
Service Providers
Bootstrap
v Virtual Sensors
0
FacialFeatures
a
Name
ab| (Default)
iro] Capabilities
ab) DeviceDescription
ab) Manufacturer
ab| ModelName
ab) SerialNumber
iis] SubType
Type
REG_SZ
REG_DWORD
REG_SZ
REG_SZ
REG_SZ
REG_SZ
REG_DWORD
REG_QWORD
Data
(value not set)
0x00000080 (128)
Windows Hello Face Virtual Software Device
Microsoft Corporation
Windows Hello Face Virtual Sensor
000000000
0x00000000 (0)
0x200000001000000 (144115188092633088)
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\WbioSrvc\Service Providers\Bootstrap\Virtual Sensors\{0527b250-7514-4321-8b68-41 c65f956998}\ Configurations\0
v
v
Bootstrap
v Virtual Sensors
0
FacialFeatures
A
Name Type Data
ab} (Default) REG_SZ (value not set)
ab) Databaseld REG_SZ DC576DA6-D676-4A15-906D-COCEAF949543
ab) EngineAdapterBinary REG_SZ FaceBootstrapAdapter.dll
ab| SensorAdapterBinary REG_SZ FaceBootstrapAdapter.dll
iro] SensorMode REG_DWORD 0x00000001 (1)
ab) StorageAdapterBinary REG_SZ FaceBootstrapAdapter.dll
iro] SystemSensor
REG_DWORD
0x00000001 (1)
13
```

## Slide 71

#### Windows Biometric Service – Configuration

2025

13


> Recovered by OCR — confidence 87/100 on the text kept, 78/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
v Databases
Parameters
Security
v Service Providers
oy Bootstrap
vw FacialFeatures
vw Fingerprint
vw Iris
vw Voice
2025
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\WbioSrvc\Databases\{DC576DA6-D676-4A15-906D-COCEAF949543}
Windows Biomewric Serviee — Conf
wbengine
¥ | | Databases
Name
Parameters
Security ab] Connectionstring
Service Providers ab) FilePath
Tiggerinfo ab) Format
Type
REG_SZ
REG_DWORD
REG_DWORD
REG_DWORD
REG_DWORD
REG_SZ
REG_SZ
REG_SZ
REG_DWORD
Data
(value not set)
000000001 (1)
000000001 (1)
000000000 (0)
000000002 (2)
0x00000020 (32)
v
v
Parameters
Security
Service Providers
Bootstrap
v Virtual Sensors
0
FacialFeatures
a
Name
ab| (Default)
iro] Capabilities
ab) DeviceDescription
ab) Manufacturer
ab| ModelName
ab) SerialNumber
iis] SubType
Type
REG_SZ
REG_DWORD
REG_SZ
REG_SZ
REG_SZ
REG_SZ
REG_DWORD
REG_QWORD
Data
(value not set)
0x00000080 (128)
Windows Hello Face Virtual Software Device
Microsoft Corporation
Windows Hello Face Virtual Sensor
000000000
0x00000000 (0)
0x200000001000000 (144115188092633088)
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\WbioSrvc\Service Providers\Bootstrap\Virtual Sensors\{0527b250-7514-4321-8b68-41 c65f956998}\ Configurations\0
v
v
Bootstrap
v Virtual Sensors
0
FacialFeatures
A
Name
ab} (Default)
ab) EngineAdapterBinary
ab| SensorAdapterBinary
iro] SensorMode
ab) StorageAdapterBinary
iro] SystemSensor
Type
REG_SZ
REG_SZ
REG_SZ
REG_SZ
REG_DWORD
REG_SZ
REG_DWORD
Data
(value not set)
DC576DA6-D676-4A15-906D-COCEAF949543
FaceBootstrapAdapter.dll
FaceBootstrapAdapter.dll
0x00000001 (1)
FaceBootstrapAdapter.dll
0x00000001 (1)
13
```

## Slide 72

#### Biometric Unit

Windows Biometric Service

2025

14


> Recovered by OCR — confidence 95/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Biometric Unit
Windows Biometric
Service
```

## Slide 73

#### Biometric Unit

Sensor Engine Storage
Pipeline Pipeline Pipeline
Windows Biometric
Service

2025

14

## Slide 74

#### Biometric Unit

Sensor Engine Storage
Pipeline Pipeline Pipeline
Windows Biometric
Service

2025

14

## Slide 75

#### Biometric Unit

Sensor Engine Storage
Pipeline Pipeline Pipeline
Windows Biometric
Service

2025

14

## Slide 76

#### Biometric Unit

Sensor Engine Storage
Pipeline Pipeline Pipeline
Windows Biometric
Service

2025

14

## Slide 77

#### Biometric Unit

Biometric Unit
Sensor Engine Storage
Pipeline Pipeline Pipeline
Windows Biometric
Service

2025

14

## Slide 78

#### Biometric Unit

Sensor Engine Storage
Pipeline Pipeline Pipeline
Windows Biometric
Service

2025

14

## Slide 79

#### Biometric Unit

Sensor Engine Storage Framework
Pipeline Pipeline Pipeline Pipeline
Windows Biometric
Service
undocumented

2025

14

## Slide 80

#### Biometric Unit

Sensor Engine Storage Framework
Pipeline Pipeline Pipeline Pipeline
Windows Biometric
Service
undocumented

2025

14

## Slide 81

#### Enhanced Sign-in Security (ESS)

LogonUI / CredUI
WinBio API

2025

15


> Recovered by OCR — confidence 82/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Enhanced Sign-in Security (ESS)
<5 Logonul / CredUI
C WinBio API +)
```

## Slide 82

#### Enhanced Sign-in Security (ESS)

LogonUI / CredUI
WinBio API

2025

15

## Slide 83

#### Enhanced Sign-in Security (ESS)

LogonUI / CredUI
WinBio API
Windows Biometric Service

2025

15

## Slide 84

#### Enhanced Sign-in Security (ESS)

LogonUI / CredUI
WinBio API
Windows Biometric Service
User-Mode
Kernel-Mode
Biometric Driver
TPM Biometric Device

2025

15

## Slide 85

#### Enhanced Sign-in Security (ESS)

LogonUI / CredUI
WinBio API
Windows Biometric Service
User-Mode
Kernel-Mode
Biometric Driver
Hypervisor
TPM Biometric Device

2025

15

## Slide 86

#### Enhanced Sign-in Security (ESS)

LogonUI / CredUI
WinBio API
Windows Biometric Service
User-Mode
Kernel-Mode
Biometric Driver
VTL-0 VTL-1
Hypervisor
TPM Biometric Device
Hypervisor boundary

2025

15

## Slide 87

#### Enhanced Sign-in Security (ESS)

LogonUI / CredUI
WinBio API
Windows Biometric Service
User-Mode
Kernel-Mode
Biometric Driver Secure Driver
VTL-0 VTL-1
Hypervisor
TPM Biometric Device
Hypervisor boundary

2025

15

## Slide 88

#### Enhanced Sign-in Security (ESS)

LogonUI / CredUI
WinBio API
Isolated Windows Biometric
Windows Biometric Service
Service
BioIso.exe
User-Mode
Kernel-Mode
Biometric Driver Secure Driver
VTL-0 VTL-1
Hypervisor
TPM Biometric Device
Hypervisor boundary

2025

15

## Slide 89

#### Enhanced Sign-in Security (ESS)

LogonUI / CredUI Biometric Unit
Storage Engine Sensor
WinBio API
Isolated Windows Biometric
Windows Biometric Service
Service
BioIso.exe
User-Mode
Kernel-Mode
Biometric Driver Secure Driver
VTL-0 VTL-1
Hypervisor
TPM Biometric Device
15
Hypervisor boundary

2025

15

## Slide 90

#### Enhanced Sign-in Security (ESS)

LogonUI / CredUI Biometric Unit
Biometric
Template
Database Storage Engine Sensor
WinBio API
Isolated Windows Biometric
Windows Biometric Service
Service
BioIso.exe
User-Mode
Kernel-Mode
Biometric Driver Secure Driver
VTL-0 VTL-1
Hypervisor
TPM Biometric Device
Hypervisor boundary

2025

15

## Slide 91

#### Enhanced Sign-in Security (ESS)

LogonUI / CredUI Biometric Unit
Biometric
Template
Database Storage Engine Sensor
WinBio API
Isolated Windows Biometric
Windows Biometric Service
Service
BioIso.exe
User-Mode
Kernel-Mode
Biometric Driver Secure Driver
VTL-0 VTL-1
Hypervisor
TPM Biometric Device
Hypervisor boundary

2025

15

## Slide 92

#### Enhanced Sign-in Security (ESS)

LogonUI / CredUI Biometric Unit
Biometric
Template
Database Storage Engine Sensor
WinBio API
Isolated Windows Biometric
Windows Biometric Service
Service
BioIso.exe
User-Mode
Kernel-Mode
Biometric Driver Secure Driver
VTL-0 VTL-1
Hypervisor
TPM Biometric Device
Hypervisor boundary

2025

15

## Slide 93

#### Enhanced Sign-in Security (ESS)

LogonUI / CredUI Biometric Unit
Biometric
Template
Database Storage Engine Sensor
WinBio API
Isolated Windows Biometric
Identity Providers Windows Biometric Service
Service
BioIso.exe
User-Mode
Kernel-Mode
Biometric Driver Secure Driver
VTL-0 VTL-1
Hypervisor
TPM Biometric Device
2025
Hypervisor boundary

15

## Slide 94

#### Enhanced Sign-in Security (ESS)

LogonUI / CredUI Biometric Unit
Biometric
Template
Database Storage Engine Sensor
WinBio API
Isolated Windows Biometric
Identity Providers Windows Biometric Service
Service
BioIso.exe
User-Mode
Kernel-Mode
Biometric Driver Secure Driver
VTL-0 VTL-1
Hypervisor
TPM Biometric Device
2025 15
Hypervisor boundary

15

## Slide 95

#### Enhanced Sign-in Security (ESS)

2025

16


> Recovered by OCR — confidence 90/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Enhanced Sign-in Security (ESS)
General Driver Details Events
q PC camera
Property
Capabilities v
Value
000004A4
CM_DEVCAP_REMOVABLE
CM_DEVCAP_SILENTINSTALL
CM_DEVCAP_SURPRISEREMOVALOK
| CM_DEVCAP_SECUREDEVICE }
Cancel
```

## Slide 96

###### • Adapter Capture & Update

ClearContext
CBiometricUnit::FlushPipeline
(Sensor)
ClearContext
(Engine)
StartCapture
ClearContext
(Storage)
CBiometricUnit::WaitForNotification If # loop
Cancel Error Wait reason? Timeout CBiometricUnit::SuspendAndWaitForPlatformResume
Normal
FinishCapture
In case of error before
QueryCalibrationData PushDataToEngine AcceptSampleData
AcceptCalibrationData CPresenceMonitorLocal::Update
CBiometricUnit::OpenHmacSession CPresenceMonitorLocal::GetChanges
Cache & Lists Management
Objects & Resources release

2025

17

## Slide 97

###### • Adapter Capture & Update

ClearContext
CBiometricUnit::FlushPipeline
(Sensor)
ClearContext
(Engine)
StartCapture
ClearContext
(Storage)
CBiometricUnit::WaitForNotification If # loop
Cancel Error Wait reason? Timeout CBiometricUnit::SuspendAndWaitForPlatformResume
Normal
FinishCapture
In case of error before
QueryCalibrationData PushDataToEngine AcceptSampleData
AcceptCalibrationData CPresenceMonitorLocal::Update
CBiometricUnit::OpenHmacSession CPresenceMonitorLocal::GetChanges
Cache & Lists Management
Objects & Resources release

2025

17

## Slide 98

•
Adapter Capture & Update
ClearContext
CBiometricUnit::FlushPipeline
(Sensor)
ClearContext
(Engine)
StartCapture
ClearContext
(Storage)
CBiometricUnit::WaitForNotification If # loop
Cancel Error Wait reason? Timeout CBiometricUnit::SuspendAndWaitForPlatformResume
Normal
FinishCapture
In case of error before
QueryCalibrationData PushDataToEngine AcceptSampleData
AcceptCalibrationData CPresenceMonitorLocal::Update
CBiometricUnit::OpenHmacSession CPresenceMonitorLocal::GetChanges
Cache & Lists Management
2025 Objects & Resources release

17

## Slide 99

###### • Adapter Capture & Update

ClearContext
CBiometricUnit::FlushPipeline
(Sensor)
ClearContext
(Engine)
StartCapture
ClearContext
(Storage)
CBiometricUnit::WaitForNotification If # loop
Cancel Error Wait reason? Timeout CBiometricUnit::SuspendAndWaitForPlatformResume
Normal
FinishCapture
In case of error before
QueryCalibrationData PushDataToEngine AcceptSampleData
AcceptCalibrationData CPresenceMonitorLocal::Update
CBiometricUnit::OpenHmacSession CPresenceMonitorLocal::GetChanges
Cache & Lists Management
Objects & Resources release

2025

17

## Slide 100

###### • Adapter Capture & Update

ClearContext
CBiometricUnit::FlushPipeline
(Sensor)
ClearContext
(Engine)
StartCapture
ClearContext
(Storage)
CBiometricUnit::WaitForNotification If # loop
Cancel Error Wait reason? Timeout CBiometricUnit::SuspendAndWaitForPlatformResume
Normal
FinishCapture
In case of error before
QueryCalibrationData PushDataToEngine AcceptSampleData
AcceptCalibrationData CPresenceMonitorLocal::Update
CBiometricUnit::OpenHmacSession CPresenceMonitorLocal::GetChanges
Cache & Lists Management
Objects & Resources release

2025

17

## Slide 101

###### • Adapter Capture & Update

ClearContext
CBiometricUnit::FlushPipeline
(Sensor)
ClearContext
(Engine)
StartCapture
ClearContext
(Storage)
CBiometricUnit::WaitForNotification If # loop
Cancel Error Wait reason? Timeout CBiometricUnit::SuspendAndWaitForPlatformResume
Normal
FinishCapture
In case of error before
QueryCalibrationData PushDataToEngine AcceptSampleData
AcceptCalibrationData CPresenceMonitorLocal::Update
CBiometricUnit::OpenHmacSession CPresenceMonitorLocal::GetChanges
Cache & Lists Management
Objects & Resources release

2025

17

## Slide 102

###### • Adapter Capture & Update

ClearContext
CBiometricUnit::FlushPipeline
(Sensor)
ClearContext
(Engine)
StartCapture
ClearContext
(Storage)
CBiometricUnit::WaitForNotification If # loop
Cancel Error Wait reason? Timeout CBiometricUnit::SuspendAndWaitForPlatformResume
Normal
FinishCapture
In case of error before
QueryCalibrationData PushDataToEngine AcceptSampleData
AcceptCalibrationData CPresenceMonitorLocal::Update
CBiometricUnit::OpenHmacSession CPresenceMonitorLocal::GetChanges
Cache & Lists Management
Objects & Resources release

2025

17

## Slide 103

###### • Adapter Capture & Update

ClearContext
CBiometricUnit::FlushPipeline
(Sensor)
ClearContext
(Engine)
StartCapture
ClearContext
(Storage)
CBiometricUnit::WaitForNotification If # loop
Cancel Error Wait reason? Timeout CBiometricUnit::SuspendAndWaitForPlatformResume
Normal
FinishCapture
In case of error before
QueryCalibrationData PushDataToEngine AcceptSampleData
AcceptCalibrationData CPresenceMonitorLocal::Update
CBiometricUnit::OpenHmacSession CPresenceMonitorLocal::GetChanges
This is where the
identification happens.
Cache & Lists Management
Objects & Resources release

2025

17

## Slide 104

###### • Adapter Capture & Update

ClearContext
CBiometricUnit::FlushPipeline
(Sensor)
ClearContext
(Engine)
StartCapture
ClearContext
(Storage)
CBiometricUnit::WaitForNotification If # loop
Cancel Error Wait reason? Timeout CBiometricUnit::SuspendAndWaitForPlatformResume
Normal
FinishCapture
In case of error before
QueryCalibrationData PushDataToEngine AcceptSampleData
AcceptCalibrationData CPresenceMonitorLocal::Update
CBiometricUnit::OpenHmacSession CPresenceMonitorLocal::GetChanges
Cache & Lists Management
Objects & Resources release

2025

17

## Slide 105

###### • Adapter Capture & Update

ClearContext
CBiometricUnit::FlushPipeline
(Sensor)
ClearContext
(Engine)
StartCapture
ClearContext
(Storage)
CBiometricUnit::WaitForNotification If # loop
Cancel Error Wait reason? Timeout CBiometricUnit::SuspendAndWaitForPlatformResume
Normal
FinishCapture
In case of error before
QueryCalibrationData PushDataToEngine AcceptSampleData
AcceptCalibrationData CPresenceMonitorLocal::Update
CBiometricUnit::OpenHmacSession CPresenceMonitorLocal::GetChanges
Cache & Lists Management
Objects & Resources release

2025

17

## Slide 106

###### • Adapter Capture & Update

ClearContext
CBiometricUnit::FlushPipeline
(Sensor)
ClearContext
(Engine)
StartCapture
ClearContext
(Storage)
CBiometricUnit::WaitForNotification If # loop
Cancel Error Wait reason? Timeout CBiometricUnit::SuspendAndWaitForPlatformResume
Normal
FinishCapture
In case of error before
QueryCalibrationData PushDataToEngine AcceptSampleData
AcceptCalibrationData CPresenceMonitorLocal::Update
CBiometricUnit::OpenHmacSession CPresenceMonitorLocal::GetChanges
Cache & Lists Management
Objects & Resources release

2025

17

## Slide 107

- Presence Monitor Update Procedure

2025

18


> Recovered by OCR — confidence 86/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
¢ Presence Monitor Update Procedure
```

## Slide 108

• Presence Monitor Update Procedure

Engine IdentifyAll
Storage Adapter  Biometric
Interface Database
IdentifyAll
(Engine)
Engine Matching
Algorithm
Biometric Data
(from PushDataToEngine)

2025

18

## Slide 109

- Presence Monitor Update Procedure

IdentifyAll
(Engine)
WINBIO_PRESENCE
WINBIO_PRESENCE
SID WINBIO_IDENTITY WINBIO_PRESENCE

Engine IdentifyAll
Storage Adapter  Biometric
Interface Database
Engine Matching
Algorithm
Biometric Data
(from PushDataToEngine)

2025

18

## Slide 110

Engine IdentifyAll
•
Presence Monitor Update Procedure
Storage Adapter  Biometric
Interface Database
IdentifyAll
(Engine)
Engine Matching
Algorithm
WINBIO_PRESENCE
WINBIO_PRESENCE
SID WINBIO_IDENTITY WINBIO_PRESENCE
Biometric Data
(from PushDataToEngine)
CPresence::ReportObservation

2025

18

## Slide 111

• Presence Monitor Update Procedure

Engine IdentifyAll

Storage Adapter  Biometric
Interface Database
IdentifyAll
(Engine)
Engine Matching
Algorithm
Biometric Data
(from PushDataToEngine)
CPresence::ReportObservation
Creation CPresence objects
Cache Management Procedure

2025

18

## Slide 112

Authentication procedure Once the identification happened

2025

19

## Slide 113

#### Traditional Auth management

AUTH Procedure
Password
Certificate
Cryptographic procedure Hash
...

2025

20


> Recovered by OCR — confidence 93/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Traditional Auth management
AUTH Procedure
Certificate
Password
Cryptographic procedure
2025 20
```

## Slide 114

#### Traditional Auth management

AUTH Procedure
Password
Certificate
Cryptographic procedure Hash
...

2025

20


> Recovered by OCR — confidence 93/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Traditional Auth management
AUTH Procedure
Certificate
Password
Cryptographic procedure
2025 20
```

## Slide 115

#### Traditional Auth management

AUTH Procedure
Password
Certificate
Cryptographic procedure Hash
...

2025

20


> Recovered by OCR — confidence 93/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Traditional Auth management
AUTH Procedure
Certificate
Password
Cryptographic procedure
2025 20
```

## Slide 116

#### Traditional Auth management

AUTH Procedure
Password
Certificate
Cryptographic procedure Hash
...

2025

20

## Slide 117

#### Traditional Auth management

AUTH Procedure
Password
Certificate
Cryptographic procedure Hash
...

2025

20

## Slide 118

#### Traditional Auth management

AUTH Procedure
Password
Certificate
Cryptographic procedure Hash
...

2025

20

## Slide 119

#### Windows Biometric Auth management

AUTH Procedure in LSASS
Biometrics
Certificate
Biometric
Service TPM Signature
...
Ticket
Passport
2025

21

## Slide 120

#### Windows Biometric Auth management

AUTH Procedure in LSASS
Biometrics
Certificate
Biometric
Service TPM Signature
...
Ticket
Passport
2025

21

## Slide 121

#### Windows Biometric Auth management

AUTH Procedure in LSASS
Biometrics
Certificate
Biometric
Service TPM Signature
...
Ticket
Passport
2025

21

## Slide 122

#### Windows Biometric Auth management

AUTH Procedure in LSASS
Biometrics
Certificate
Biometric
Service TPM Signature
...
Ticket
Passport
2025

21

## Slide 123

#### Windows Biometric Auth management

AUTH Procedure in LSASS
Biometrics
Certificate
Biometric
Service TPM Signature
...
Ticket
Passport
2025

21

## Slide 124

#### Windows Biometric Auth management

AUTH Procedure in LSASS
Biometrics
Certificate
Biometric
Service TPM Signature
...
Ticket
Passport

2025

21

## Slide 125

#### Windows Biometric Auth management

AUTH Procedure in LSASS
Biometrics
Certificate
Biometric
Service TPM Signature
...
Ticket
Passport
2025

21

## Slide 126

#### Windows Biometric Auth management

AUTH Procedure in LSASS
Biometrics
Certificate
Biometric
Service TPM Signature
...
Ticket
Passport

2025

21

## Slide 127

#### Windows Biometric Auth management

AUTH Procedure in LSASS
Biometrics
Certificate
Biometric
Service TPM Signature
...
Ticket
Passport

2025

21

## Slide 128

#### Windows Biometric Auth management

AUTH Procedure in LSASS
Biometrics
Certificate
Biometric
Service Signature
...
Ticket
Passport

2025

21

## Slide 129

# Database Format

Let’s have a look inside

2025

22

## Slide 130

#### Database

- Let’s start with Microsoft’s FAQ.

 …

- And some documentation …

2025

23


> Recovered by OCR — confidence 85/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Database
¢ Let’s start with Microsoft’s FAQ.
¢ And some documentation ... @)
```

## Slide 131

#### Database

- Let’s start with Microsoft’s FAQ.

 …

- And some documentation …

2025

23


> Recovered by OCR — confidence 92/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Database
¢ Let’s start with Microsoft’s FAQ.
¢ And some documentation ... ©)
Who has access on Windows Hello biometrics data?
Since Windows Hello biometrics data is stored in encrypted format, no user, or any process other than Windows Hello
has access to it.
```

## Slide 132

#### Database

- Let’s start with Microsoft’s FAQ. • And some documentation …

2025

23


> Recovered by OCR — confidence 96/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Database
Biometric data storage
The biometric data used to support Windows Hello is stored on the local device only. It doesn’t roam and is never sent
to external devices or servers. This separation helps to stop potential attackers by providing no single collection point
An d some d OC that an attacker could potentially compromise to steal biometric data. Even if an attacker could obtain the biometric data
from a device, it couldn't be converted back into a raw biometric sample recognizable by the biometric sensor.
Each sensor has its own biometric database file where template data is stored (path c:
\WINDOWS \System32\WinBioDatabase ). Each database file has a unique, randomly generated key that is encrypted to the
system. The template data for the sensor is encrypted with the per-database key using AES with CBC chaining mode. The
hash is SHA256,
@ Note
Some fingerprint sensors have the capability to complete matching on the fingerprint sensor module instead of in
the OS. These sensors store biometric data on the fingerprint module instead of in the database file. For more
information, see Windows Hello Enhanced Security Sign-in (ESS).
2025 23
```

## Slide 133

#### What do we know?

- Biometric data is the holy grail of mobile device security.

   - Therefore, we need strong encryption!

- We need something that identifies a user.

   - In Windows this is typically a security identifier (SID).

   - User authentication is the holy grail of domain security.

- The biometric unit uses the templates saved in the database.

   - We need to decrypt the template before we can compare it.

- Where is the key coming from?

   - We do not provide a password or entropy of any kind!

2025

24

## Slide 134

#### Database Format – Overview

struct _LOCK_BOX_PROTECTED_DATA
BYTE
Encrypted[0x400]
struct _LOCK_BOX_FILE_HEADER
struct _LOCK_BOX_RECORD
struct _LOCK_BOX_RECORD
...

2025

25

## Slide 135

#### Database Format – Overview

struct _LOCK_BOX_PROTECTED_DATA
BYTE
Encrypted[0x400]
struct _LOCK_BOX_FILE_HEADER
struct _LOCK_BOX_RECORD
struct _LOCK_BOX_RECORD
...

- The encrypted header

   - Ensures the integrity of the database using a SHA256 hash

   - Contains the AES key for the encrypted templates

2025

25

## Slide 136

#### Database Format – Overview

struct _LOCK_BOX_PROTECTED_DATA
BYTE
Encrypted[0x400]
struct _LOCK_BOX_FILE_HEADER
struct _LOCK_BOX_RECORD
struct _LOCK_BOX_RECORD
...

- The encrypted header

   - Ensures the integrity of the database using a SHA256 hash

   - Contains the AES key for the encrypted templates

- The unencrypted header holds information regarding

   - Version information

   - Number of used records and available records

2025

25

## Slide 137

#### Database Format – Overview

struct _LOCK_BOX_PROTECTED_DATA
•
The encrypted header
•
BYTE •
Encrypted[0x400]
•
struct _LOCK_BOX_FILE_HEADER • Version information
•
struct _LOCK_BOX_RECORD
•
One record per enrolled user
struct _LOCK_BOX_RECORD
•
SID
•
Encrypted template
...

   - Ensures the integrity of the database using a SHA256 hash

   - Contains the AES key for the encrypted templates

- The unencrypted header holds information regarding

   - Version information

   - Number of used records and available records

- One record per enrolled user

2025

25

## Slide 138

#### Database Format

\```
struct_LOCK_BOX_RECORD_HEADER
\```

2025

26

## Slide 139

#### Database Format

struct _LOCK_BOX_RECORD_HEADER
GUID ULONG64 ULONG64 ULONG64 ULONG64 ULONG64
MagicGUID Flags RecordSize LastEntryOffset TemplateBlobSize EncryptedTemplateBlobSize
ULONG64 ULONG64 WINBIO_IDENTITY WINBIO_BIOMETRIC_SUBTYPE BYTE
PayloadBlobSize IndexElementCount Identity SubFactor Alignment[3]

2025

26

## Slide 140

#### Database Format

struct _LOCK_BOX_RECORD_HEADER
GUID ULONG64 ULONG64 ULONG64 ULONG64 ULONG64
MagicGUID Flags RecordSize LastEntryOffset TemplateBlobSize EncryptedTemplateBlobSize
ULONG64 ULONG64 WINBIO_IDENTITY WINBIO_BIOMETRIC_SUBTYPE BYTE
PayloadBlobSize IndexElementCount Identity SubFactor Alignment[3]
struct _LOCK_BOX_RECORD_CONTENT
BYTE         BYTE  BYTE
IndexVector[1]  ... EncryptedTemplate[1]  Template[1]  ...
BYTE
PayloadBlob[1]  ...

2025

26

## Slide 141

#### Database Format

struct _LOCK_BOX_RECORD_HEADER
GUID ULONG64 ULONG64 ULONG64 ULONG64 ULONG64
MagicGUID Flags RecordSize LastEntryOffset TemplateBlobSize EncryptedTemplateBlobSize
ULONG64 ULONG64 WINBIO_IDENTITY WINBIO_BIOMETRIC_SUBTYPE BYTE
PayloadBlobSize IndexElementCount Identity SubFactor Alignment[3]
struct _LOCK_BOX_RECORD_CONTENT
BYTE         BYTE  BYTE
IndexVector[1]  ... EncryptedTemplate[1]  Template[1]  ...
BYTE
PayloadBlob[1]  ...

2025

26

## Slide 142

#### Database Format

For instance: “S-1-5-21-1004336348-1177238915-682003330-5 2”

“S-1-5-21-1004336348-1177238915-682003330-5 2”
struct _LOCK_BOX_RECORD_HEADER
GUID ULONG64 ULONG64 ULONG64 ULONG64 ULONG64
MagicGUID Flags RecordSize LastEntryOffset TemplateBlobSize EncryptedTemplateBlobSize
ULONG64 ULONG64 WINBIO_IDENTITY WINBIO_BIOMETRIC_SUBTYPE BYTE
PayloadBlobSize IndexElementCount Identity SubFactor Alignment[3]
struct _LOCK_BOX_RECORD_CONTENT
BYTE         BYTE  BYTE
IndexVector[1]  ... EncryptedTemplate[1]  Template[1]  ...
BYTE
PayloadBlob[1]  ...

2025

26

## Slide 143

#### Database Security

- There is an encrypted header that ensures

   - The integrity of the database and confidentiality the of biometric data

- How the header’s integrity and confidentiality achieved?

   - We need functionality that does not require an additional key!

   - The header is protected with <u>CryptProtectData/CryptUnprotectData functions.</u>

      - Cipher keys are managed locally by NT-AUTHORITY\SYSTEM.

      - .

      - • Local administrator can get access

Record content check

Safe?

LockBoxLockDatabase

Yes

No

QueryBySubjectCommonUnsafe

Yes Already existing?

No

LockBoxEncryptTemplate

LockBoxCreateRecord

Record structure filled

LockBoxReadFileHeader

LockBoxWriteRecord

LockBoxReadProtectedData

LockBoxComputeFileHash

LockBoxWriteProtectedData

LockBoxUnlockDatabase

End of the procedure

2025

27

## Slide 144

#### Database (In)security

- Local administrators break the security of the database:

   - Decrypt and read the encrypted templates of enrolled users.

   - Change the database and circumvent the integrity controls of the database.

- This means:

   - Exchange SIDs of enrolled users.

   - Decrypt templates.

   - Bring their own biometrics to the system.

      - Authenticate as every enrolled user.

2025

28

## Slide 145

#### Demo – Decrypting the encrypted header

2025

29


> Recovered by OCR — confidence 83/100 on the text kept, 60/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Demo — Decrypting the encrypted header
=sktop\DC576DA6-D676-4415-966D-COCEAF949543 . DAT
calculated Hash:
[INFO] Hashes match proceeding
LockBoxProtectedData {
HeaderkeyDataBlob: dwMaginc: 4D42444B, dwVersion: 1, cbKeySize: 32
Alignment: @
SizeHash: 32
SizeKkey: 16
LockBoxFileHeader {
GuidDatabase: dicaed46-Sb8d-4e7c-8aGe-34bcac166281
Version: 2
DatabaseID: dc5/6da6-d676-4a15-966d-c@ceaf949543
```

## Slide 146

#### Demo Time

2025

30


> Recovered by OCR — confidence 79/100 on the text kept, 52/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
piSekhat Demo Time.
2025
—
=
a
30
```

## Slide 147

Conclusion

2025

31

## Slide 148

#### Conclusion

- Windows Hello for Business is here to stay!

   - Added as security feature to new products like Recall.

- Local administrator to domain user is still a threat.

   - Worst case local admin to domain admin.

- Securing heterogenous clients is a challenge Microsoft faces.

   - ESS mode needs hardware support – new Thinkpads with AMD do not have it.

   - ESS mode needs VBS – sadly not used enough!

   - **If you can use it!**

2025

32

## Slide 149

#### Make the world a safer place

- In any case:

   - Only one user per client!

- Also:

   - Consider only allowing PIN authentication.

   - Monitoring: Only WBS should open or modify the database.

2025

33

## Slide 150

### Questions?

www.ernw.de www.insinuator.net
struct _LOCK_BOX_PROTECTED_DATA
BCRYPT_KEY_DATA_BLOB_HEADER BYTE
bdavid@ernw.de
HeaderKeyDataBlob KeyDataBlob[48]
tosswald@ernw.de UINT32 UINT32 UINT32 BYTE BYTE
Alignment SizeHash SizeSecret Hash[32] Secret[16]
struct _LOCK_BOX_FILE_HEADER
struct _LOCK_BOX_PROTECTED_DATA
GUID ULONG64 WINBIO_UUID WINBIO_BIOMETRIC_TYPE WINBIO_UUID SIZE_T
GuidDatabase Version DatabaseID Factor Format IndexElementCount
BYTE SIZE_T SIZE_T SIZE_T LARGE_INTEGER ULONG64 ULONG64
Encrypted[0x400] TotalRecordCount DeletedRecordCount MaxAvailableRecordCount FirstFreeByte Reserved_01 Reserved_02
struct _LOCK_BOX_RECORD_HEADER
struct _LOCK_BOX_FILE_HEADER
GUID ULONG64 ULONG64 ULONG64 ULONG64 ULONG64
MagicGUID Flags RecordSize LastEntryOffset TemplateBlobSize EncryptedTemplateBlobSize
struct _LOCK_BOX_RECORD struct _LOCK_BOX_RECORD_HEADER
ULONG64 ULONG64 WINBIO_IDENTITY WINBIO_BIOMETRIC_SUBTYPE BYTE
PayloadBlobSize IndexElementCount Identity SubFactor Alignment[3]
struct _LOCK_BOX_RECORD
... struct _LOCK_BOX_RECORD_CONTENT
BCryptDecrypt
BYTE         BYTE
IndexVector[1]  ... EncryptedTemplate[1]  ...
struct _LOCK_BOX_RECORD_CONTENT
BYTE
PayloadBlob[1]  ...

BCryptDecrypt
BYTE
Template[1]

## Slide 151

#### References

• Slide 6: https://thecyberconsultancy.com/hello-auth.html • Slide 7: https://support.microsoft.com/de-de/windows/mit-recall-ihre- <u>schritte-zur%C3%BCckverfolgen-aa03f8a0-a78b-4b3e-b0a1-2eb8ac48701c</u> • Slide 7: https://learn.microsoft.com/en-us/windows/security/identity- <u>protection/passkeys/</u>

• Slide 37: Looking after your teeth – Guernsey Dental Association

• Transition slides: https://www.socwall.com/

2025

35
