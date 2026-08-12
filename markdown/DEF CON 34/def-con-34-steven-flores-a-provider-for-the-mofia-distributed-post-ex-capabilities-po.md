---
title: "A Provider for the MOFia - Distributed Post-Ex Capabilities"
speakers: ["Steven Flores"]
conference: "DEF CON"
conference_full: "DEF CON 34"
edition: "34"
year: null
source_pdf: "DEF CON 34/DEF CON 34 - Steven Flores - A Provider for the MOFia - Distributed Post-Ex Capabilities - Po.pdf"
pages: 36
sha256: "2f9bc31624bfdd74f9e516b59b04dd41ac417c0686c5c8c17340c8ebab003f41"
text_chars: 12647
ocr_pages: 0
has_ocr: false
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2"
converted_at: "2026-08-12T00:28:05Z"
---
# A Provider for the MOFia - Distributed Post-Ex Capabilities

**Speakers:** Steven Flores  
**Conference:** DEF CON 34  
**Source:** `DEF CON 34/DEF CON 34 - Steven Flores - A Provider for the MOFia - Distributed Post-Ex Capabilities - Po.pdf` (36 pages)

## Slide 1

# **A Provider for the MOFia**

Distributed Post-ex Capabilities

## Slide 2

### **About me**

- Senior Offensive Security Engineer at SpecterOps

- Provide consultants with tooling, tradecraft, and help

- Research, capability dev, initial access, payload dev, coffee

- @0xthirteen on Twitter

## Slide 3

O V E R V I E W

01 WMI background

02 Purpose

03 Existing capabilities

> 04 Previous work

05 Mofcomp

> 06 Provider install & WMIO

07 Full WMI implementations

08 Tooling & demo

09 Detection guidance

10 Closing

## Slide 4

W M I B A C K G R O U N D · 1 / 4

### **What is WMI**

- Windows Manag ement Instrumentation is Microsoft's implementation of Web -Based Enterprise based on Common Information Model (CIM)

- Classes, methods, and properties, all part of its schema

- Has its own query lang uag e, WQL

- Remote access through DCO M/RPC (or WSMAN can be selected as a transport)

- Usage starts from a client to a WMI service which loads providers and performs actions on the OS

- Namespaces lay out the hierarchy

- MOF files used to manage WMI schema

- Essentially a standard management system for Windows based systems

## Slide 5

W M I B A C K G R O U N D · 2 / 4 **The CIM model**

The CIM standard creates a model for:

Classes

Methods

Properties

Instances

Qualifiers Associations

Namespaces

- Objects consist of Properties, Methods, Qualifiers. Objects become instances

- ▸ Namespaces organize classes

- Associations define relationships

## Slide 6

W M I B A C K G R O U N D · 3 / 4 **Execution level by HostingModel**

- Providers are hosted inside of WmiPrvse.exe

- HostingModel determines which account, which host process, isolation

- Win32_Process uses NetworkServiceHost

LocalSystemHost System NetworkServiceHost Network Service LocalServiceHost Local Service LocalSystemHostOrSelfHost System SelfHost Qualifier-determined integrity level Decoupled:COM Determined by launch permission LocalSystemHost:Trusted System

## Slide 7

W M I B A C K G R O U N D · 4 / 4 **The WMI architecture**

- This is only a very high-level overview; there are a lot of components in WMI

- Matt Graeber's BlackHat 2015 talk covered a lot of information when little public offensive research existed

https://blackhat.com/docs/us-15/materials/us-15-Graeber-AbusingWindows-Management-Instrumentation-WMI-To-Build-APersistent%20Asynchronous-And-Fileless-Backdoor-wp.pdf

## Slide 8

P U R P O S E

### **What WMI detection assumes**

Most existing WMI detections rest on two primitives:

01

#### **Creating a new process**

Child processes from WMIPrvSE.exe or scrcons.exe

02

#### **Reading / writing registry**

Registry reads and writes in an unusual way

Based on publicly available detection rules and first-hand experience. Not the only detections but generally what has been seen

## Slide 9

E X I S T I N G C A P A B I L I T Y · 1 / 2 **How WMI is used today**

- Canonical example is Win32_Process in CIMv2 the Create method spawns a process

- Second common example: event subscriptions for lateral movement or persistence

Create a filter, consumer, and binding that fire on an intrinsic or extrinsic event

Typically, ActiveScriptEventConsumer or CommandLineEventConsumer

- Implementations exist in plenty of scripts, C2 agents, offensive tooling

## Slide 10

E X I S T I N G C A P A B I L I T Y · 2 / 2

### **Beyond process creation**

- Most research since has looked for alternate execution or persistence via WMI

- A handful of abusable methods discovered over the years like service creation, scheduled tasks, product install, and others and others

- Found a few new methods useful for lateral movement and general post-ex capability

## Slide 11

P R E V I O U S W O R K · 1 / 2

### **MSFT_MTProcess**

- Service Performance DLL hijacking for lateral movement

- MSFT_MTProcess closest alternative to Win32_Process

Create a process creation method

CreateDump dump an arbitrary process, saving a dmp to disk

- Not a new dump technique uses Task Manager with dbg help.dll to call MiniDumpWriteDump

- Let’s you dump remotely with no new tooling but only on Windows Server 2016+

## Slide 12

PRE VI OUS WORK · 2 / 2

### **Installing the class elsewhere**

- MSFT_MTProcess ships by default on Server 2016+  could we install it anywhere?

- Software installs new WMI classes constantly, think SCCM, or OEM software vendors (Dell, Lenovo, MSI)

- Windows ships mofcomp for this purpose

Takes a MOF file, parse it, installs the provider into the WMI database, makes the class and methods callable

## Slide 13

M O F C O M P

### **What mofcomp does**

- 01 Loads mofd.dll to do most of the work

- 02 Parses the MOF  class defs, instances, qualifiers,

   - namespaces, pragmas

- 03 Compiles into the WMIO binary format

- 04 Adds to the WMI database via IWbemServices::PutC lass and PutInstance

MOF class definition · Win32_Process

## Slide 14

C O M P I E C E · 1 / 2

### **Halfway there**

- Mofcomp gets you half the way there the MOF gives the CLSID of the CO M server

- It only registers info in the WMI database  you still must register the provider

- Registry keys must hold the provider DLL and how it will be used

__Win32Provider CLSID > HKCR\CLSID\{…}\InprocServer32 > cimwin32.dll

## Slide 15

C O M P I E C E · 2 / 2

### **The local-execution problem**

- These steps, pieced together for the MSFT_MTProcess research, install the class on any Windows host

- ▸ Problem: mofcomp requires local execution

Quick method was calling Win32_Process to run mofcomp remotely

- Goal: execute the entire chain purely over WMI  read and write through WMI alone

## Slide 16

P R O V I D E R I N S T A L L A T I O N **Replicating mofcomp remotely**

- 01 PutC lass < ClassN ame> register a new class and give it the provider

- 02 PutInstance on __Win32Provider declare the provider and its CLSID

- 03 PutInstance on __MethodProviderRegistration state the provider handles method calls

## Slide 17

MS-WMI O

### **Serializing to WMIO**

- PutClass and PutInstance are easy, the hard part is parsing the MOF and serializing it as WMIO

- ▸ Microsoft's MS-WMIO protocol spec assists building the DCOM requests

- Call PutClass with the binary blob inside an OBJREF_CUSTOM DCOM envelope

- Impacket had a partial implementation only GetObject for object instantiation

## Slide 18

M S - W M I O **Serializing to WMIO**

##### ▸ Each method’s in/out parameters are themselves full class definitions

OBJREF_CUSTOM envelope Signature: 4D 45 4F 57 ("MEOW") Flags: OBJREF_CUSTOM (0x04) IID: IID_IWbemClassObject CLSID: CLSID_WbemClassObject

ENCODING_UNIT

Signature: 78 56 34 12 ObjectEncodingLength

OBJECT_BLOCK ObjectFlags (class or instance)

CLASS_AND_METHODS_PART CLASS_PART ClassName (heap reference) DerivationList (parent class chain) QualifierSet (class-level qualifiers) PropertyLookupTable (sorted by name) NdTable (2-bit null/default flags per property) ValueTable (default values, 0xFF = null) Heap (all strings referenced by offset)

METHODS_PART MethodCount (uint16) MethodDescriptions (name, origin, qualifiers) Input __PARAMETERS (full embedded class) Output __PARAMETERS (full embedded class)

## Slide 19

C O M P L E T E R E G I S T R A T I O N

### **Finishing registration**

- Write the provider DLL to disk and create the registry keys to make it usable

- StdRegProv::CreateKey on HKC R\CLSID\< CLSID > to register the COM server

HKCR\CLSID\{…}\InprocServer32 > usbdeviceprov.dll

## Slide 20

F UL L WMI I MPLE ME NT ATI ON · 1 / 5 **A file-read primitive**

▸ A file-read primitive via /root/Microsoft/Windows/PowerShellv3 GetInstance on a target file reads its bytes

▸ From an old Matt Graeber gist, rarely seen in use but implemented in WMI_Proc_Dump

## Slide 21

F U L L W M I I M P L E M E N T A T I O N · 2 / 5

### **Writing files with DSC**

- Writing files over WMI: Desired State Configuration

Namespace: /Root/Microsoft/Windows/DesiredStateConfiguration

LCM resources under C:\Windows\System32\WindowsPowerShell\v1.0\Modules\PSD esiredStateC onfig uration\D SC Resources

- Two pieces: WMI classes and Local Configuration Manager classes

- WMI methods are native; LCM is PowerShell but it makes new things possible

## Slide 22

F U L L W M I I M P L E M E N T A T I O N · 3 / 5

### **The DSC classes that matter**

- MSFT_DSCLocalConfig urationManag er access to the LCM classes

- MSFT_FileDirectoryConfiguration write a file to a remote host (UTF-8 string only)

- MSFT_ScriptResource convert base64 strings to binary

- MSFT_RegistryResource an alternative to StdReg Prov

DSC resources

## Slide 23

F UL L WMI I MPLE ME NT ATI ON · 4 / 5

### **Choosing a write path**

- For a base64 file, call MSFT_ScriptResource; sometimes a second step with MSFT_FileDirectoryConfiguration

- FileDirectoryConfiguration alone works for plain string data; binaries need ScriptResource

- Historically this meant event subscriptions + ActiveScriptEventConsumer to base64-decode via VB/JScript

PowerShell brings script-block logging and suspicious-term risk,  but DSC loading is benign looking

## Slide 24

F U L L W M I I M P L E M E N T A T I O N · 5 / 5 **The write chain**

- 01 MSFT_FileDirectoryC onfig uration writes string data to disk

- 02 MSFT_DSCLocalConfig urationManag er ResourceSet the LCM gets called

- 03 Loads MSFT_ScriptResource, base64-decodes the string back to the original data Could write elsewhere first via MSFT_Reg istryResource, but no real benefit

## Slide 25

C L E A N U P A F T E R U S E **Cleaning up**

- DeleteInstance on __MethodProviderReg istration , __InstanceProviderRegistration, __Win32Provider

- DeleteClass on the registered class name

- StdRegProv::DeleteKey on the registry entries created

- CIM_DataFile::Delete to remove the provider DLL artifact

- O rder does matter on uninstalling, if following the wrong order could be left with artifacts still present in present in WMI

## Slide 26

T O O L I N G · 1 / 5

### **wmiclient**

An SMB-client alternative

- Nothing new introduced onto the target

- Leverages all native WMI classes

- Uses the DSC ScriptResource for execute-assembly

Suspicious PS / SBL, or AMSI comes into play

- Added some AMSI / ETW / SBL tampering because of the PowerShell aspects

## Slide 27

T O O L I N G · 2 / 5

### **doppio**

Provider installation and method-execution tooling

- Historically post-ex meant move laterally, detonate an agent, establish comms, act, exit, move on

- Instead: install providers remotely on the target host

- Perform your post-ex activity directly

- Comms is just calling a WMI method  execution runs over DCOM

- Ships with multiple providers for common post-ex activity

## Slide 28

T OOLI NG · 3 / 5

### **How doppio works**

- Runs as SYSTEM; an optional impersonate flag uses CoImpersonateClient Depends on HostingModel LocalSystemHost executes as SYSTEM

- Per-provider config JSON sets CLSID, upload location, HostingModel, and more

- Builds the provider DLL directly in the CLI (MSVC or MinGW by path/OS)

- Post-ex all happens in wmiprvse run activities on different hosts wherever providers are installed

## Slide 29

T O O L I N G · 4 / 5

### **Provider capabilities**

Execute BOF, assembly, reflective DLL Kerberos (based on Rubeus) Shellcode injection into a remote process Dsregcmd Secrets dump Cookie dumping (CookieMonster)

AAD token (RequestAADRefreshToken)

## Slide 30

T OOLI NG · 5 / 5

### **A method call, end to end**

01 Client calls Win32_USBDevice::SetUsb over DCO M 1 DCOM 02 WMI reads the Win32_USBDevice class definition 03 Reads the provider("USBDeviceProv") qualifier 04 Finds __Win32Provider with Name="USBDeviceProv" 05 Confirms __MethodProviderRegistration exists

- 06 Reads CLSID from the __Win32Provider instance 07 Looks up HKCR\CLSID\{guid}\InProcServer32 08 Loads the DLL into

09 Calls DllGetClassObject > CreateInstance 10 Calls ExecMethodAsync with the method + params

## Slide 31

## **Demo**

**o**

## Slide 32

D E T E C T I O N O P P O R T U N I T I E S · 1 / 3

### **Provider registration events**

- Windows Event ID 63 fires when a provider reg isters with a H osting Model

- LocalSystemHost isn't required  the Hosting Model must match the executing the activity fails

Event 63 · USBDeviceProv registered · LocalSystem

## Slide 33

D E T E C T I O N O P P O R T U N I T I E S · 2 / 3 **Registry & DSC signals**

- WMI registering new COM servers via StdRegProv

- Elastic has good detections around WMI registry writes

- DSC has logging, but little context  log files don't show much much either

- Best bet for any DSC activity is script-block logging

Event 600 · Registry provider started · wmiprvse.exe

## Slide 34

D E T E C T I O N O P P O R T U N I T I E S · 3 / 3

### **DLLs and post-ex**

- Unsig ned DLLs loaded into wmiprvse, or in C:\Windows\system32\wbem

Provider DLLs needn't live in wbem, but it may be uncommon otherwise  doppio installs there by default (configurable)

- General post-ex detections around .NET / BOF execution

- Uncommon processes generating network traffic or local activity

## Slide 35

**Questions?**

## Slide 36

**Thank you**
