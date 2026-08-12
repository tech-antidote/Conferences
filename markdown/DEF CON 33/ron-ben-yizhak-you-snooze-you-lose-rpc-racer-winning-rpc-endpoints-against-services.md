---
title: "You snooze you lose RPC-Racer winning RPC endpoints against services"
speakers: ["Ron Ben Yizhak"]
conference: "DEF CON"
conference_full: "DEF CON 33"
edition: "33"
year: 2025
source_pdf: "DEF CON 33/Ron Ben Yizhak - You snooze you lose RPC-Racer winning RPC endpoints against services.pdf"
pages: 70
sha256: "a7d1541e92348a95d59a93f788353c86fd287dece0cf086752aa4dcbb6e121de"
text_chars: 19028
ocr_pages: 14
has_ocr: true
redacted_secrets: 0
ocr_confidence: 84.9
ocr_unreliable_blocks: 2
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T07:12:46Z"
---
# You snooze you lose RPC-Racer winning RPC endpoints against services

**Speakers:** Ron Ben Yizhak  
**Conference:** DEF CON 33  
**Source:** `DEF CON 33/Ron Ben Yizhak - You snooze you lose RPC-Racer winning RPC endpoints against services.pdf` (70 pages)


## Slide 1

You snooze you lose: RPC-Racer winning RPC endpoints against services

Ron Ben Yizhak Security Researcher, SafeBreach


> Recovered by OCR — confidence 76/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
You snooze you lose: ——
RPC-Racer winning RPC n— | —_
endpoints against services <== __
Ron Ben Yizhak '
Security Researcher, SafeBreach
```

## Slide 2

## About Me

Security Researcher @ SafeBreach

Interested in reverse engineering, exploitation techniques and logical vulnerabilities Enjoys rock climbing and playing piano

2

## Slide 3

## Agenda

1. Intro – RPC fundamentals

2. Poisoning core RPC component

3. Performing recon for vulnerable servers

4. Manipulating built-in services

5. Leveraging machine account NTLM authentication

6. Conclusion

3

## Slide 4

## RPC Fundamentals

▪ Remote Procedure Call

▪ The server exposes functionalities

▪ The client asks the server to execute functions

Method1();
Method2();
Call Method 1
Method3();
…
Client Server

4

## Slide 5

## RPC Fundamentals

RPC interfaces are defined by IDL files

]

\```
uuid(8d864136-6900-4894-aece-66d455b552de),
version(1.0),
\```

[

`interface MyRpcInterface` }

`long SendRpcMessage([in, string] const wchar_t* Message);` {

5

## Slide 6

## RPC Fundamentals

#### Binding Handles components

\```
ncacn_ip_tcp:ronb-vm[8888]
ncalrpc:ronb-vm[MyRpcEndpoint]
ncacn_np:ronb-vm[\\pipe\\MyNamedPipe]
ProtSeqNetworkAddrEndpoint
\```

6

## Slide 7

## RPC Fundamentals

Well-known endpoints vs dynamic endpoints

DCOM Well-Known Endpoint Dynamic Endpoint

7


> Recovered by OCR — confidence 89/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
RPC Fundamentals
Well-known endpoints vs dynamic endpoints
(1 rties
LA
44) Prop
fp
General Statistics Performance Threads Token Modules Memory Environment Handles
Options
Type Name
ALPC Port Connection: \RPC Control\OLE6DF 1C8637045BD 17C 110FOCA98F5 DCOM
ALPC Port Connection: \RPC Control\LSMApi Well-Known Endpoint
ALPC Port Connection: \RPC Control\LRPC-13d920216e 1f4f6d5e Dynamic Endpoint
```

## Slide 8

## RPC Fundamentals

▪ The Endpoint Mapper (EPM)

▪ The server registers UUID to endpoint

RPC Server

`12345678-1234-abcd-ef00-0123456789ab` is at `LRPC-203d2899831a7a2380`

OK

EPM

8

## Slide 9

## RPC Fundamentals

▪ The Endpoint Mapper (EPM)

▪ The client queries UUID to endpoint

Where is `12345678-1234-abcd-ef00-0123456789ab` ? `LRPC-203d2899831a7a2380` EPM

RPC Client

9

## Slide 10

## RPC Fundamentals

- The Endpoint Mapper (EPM)

▪ Implemented in C:\Windows\System32\RpcEpMap.dll ▪ Hosted by RpcSs

|Protocol|Name|
|---|---|
|ncacn_ip_tcp|135|
|ncacn_np|\pipe\epmapper|
|ncalrpc|epmapper|

10

## Slide 11

RPC Fundamentals The Endpoint Mapper (EPM)

11


> Recovered by OCR — confidence 88/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
kali@kali: ~
. File Actions Edit View Help
Impacket v0.13.0.dev0 - Copyright Fortra, LLC and its affiliated companies
[*] Retrieving endpoint list from ronb-insider
Protocol: N/A
Provider: N/A
UUID : 51A227AE-825B-41F2-B4A9-1AC9557A1018 v1.@ Ngc Pop Key Service
Bindings:
ncacn_ip_tcp:172.28.134.141[ 49664]
ncalrpc:[samss lpc]
ncalrpc:[SidKey Local End Point]
ncalrpc:[protected_storage]
ncalrpc:[lsasspirpc]
ncalrpc:[lsapolicylookup ]
ncalrpc:[LSA_EAS_ENDPOINT]
ncalrpc:[LSA_IDPEXT_ENDPOINT]
ncalrpc:[lsacap]
ncalrpc:[LSARPC_ENDPOINT]
ncalrpc:[securityevent ]
ncacn_np:\\RONB-INSIDER[\pipe\lLsass ]
ncalrpc:[imsfk]
ncalrpc:[clipsfk]
```

## Slide 12

## RPC Fundamentals

#### The Endpoint Mapper (EPM)

RPC Clients

Poisoned EPM

Rogue RPC Server

12

## Slide 13

Previous RPC Exploits Most exploitation tools target RPC Servers

PetitPotam

13

## Slide 14

# We’ll target RPC clients

14

## Slide 15

## Research Goals

Masquerade as Poison a legitimate RPC the EPM server

Manipulate RPC clients

Achieve local/domain privilege escalation

15

## Slide 16

Register as built-in interface Registration is made by calling `RpcEpRegister`

Benign RPC Server

UUID: `GoodEndpoint`

EPM

16

## Slide 17

Register as built-in interface The rogue server will mimic this behavior

UUID:  EvilEndpoint
OK
Rogue
RPC
Server

EPM

17

## Slide 18

## Register as built-in interface

There is no verification on registering built-in interfaces

18

## Slide 19

## Register Before a legitimate server

If the service is not running, we can register first

Registering first causes clients to connect to us

19

## Slide 20

## EPM Poisoning

Novel manipulation technique

Destabilize the core of MSRPC

Doesn’t require admin privileges

20


> Recovered by OCR — confidence 94/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
EPM Poisoning
Novel manipulation
technique
Destabilize the
core of MSRPC
admin privileges
Attacker
@
Injects fake
endpoint
entry
©
@
Issues
request to
real server
Fake Server
RPC
Request
resolves to
```

## Slide 21

## Finding Delayed Services

Services with manual startup pose a security risk

Their RPC interface won’t be registered on boot

21


> Recovered by OCR — confidence 84/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Finding Delayed Services
BB system Informer E
System View Tools Users Help
@ Refresh £63 Options | Q Find handles or DLLs 4# System information | 6 & @ | L)
S ; it h Processes Services Network Disk Firewall Devices
e rv | ce S W | Name PID Display name Type Status Start type ~
R\user]++ (Administrato:
GP) edgeupdatem Microsoft Edge Update Service (edge... Own process Stopped Demand start (delay...
aa a Nn U a | Sta rt U O S e Ei) dmwappushservice Device Management Wireless Applica... Share process Stopped Demand start (delay...
p p GH desve Declared Configuration(DC) service Own process Stopped Demand start (delay..
e e GH) WinkRM Windows Remote Management (WS-... Share process Stopped Demand start (delay...
a S e C U r | t a S k = MSDTC Distributed Transaction Coordinator Own process Stopped Demand start (delay...
Y Ge BITs Background Intelligent Transfer Service Share process Stopped Demand start (delay...
EF) XboxGipSvc Xbox Accessory Management Service Share process Stopped Demand start (trigger)
GE) XbIGameSave Xbox Live Game Save Share process Stopped Demand start (trigger)
e e ) Gi) wuauserv 9116 Windows Update Share process Running Demand start (trigger)
T h e | r R p C | nte rfa ce WoO Nn t GH) WPDBusEnum Portable Device Enumerator Service Share process Stopped Demand start (trigger)
EE) wipasve Local Profile Assistant Service Share process Stopped Demand start (trigger)
e EH) wlidsve 1636 Microsoft Account Sign-in Assistant Share process Running Demand start (trigger)
b e re | ste re d O Nn bo ot Ei) wisve Windows Insider Service Share process Stopped Demand start (trigger)
gs GE] WFDSConMgrSve Wi-Fi Direct Services Connection Man... Share process Stopped Demand start (trigger)
Ei) WerSvc Windows Error Reporting Service Own process Stopped Demand start (trigger)
GE) WEPHOSTSVC Windows Encryption Provider Host Se... Share process Stopped Demand start (trigger)
[i] webthreatdefsvc 6628 Web Threat Defense Service Share process Running Demand start (trigger)
GH) WebClient WebClient Share process Stopped Demand start (trigger)
EE) WhioSrve ndows Biometric Service Share process Stopped Demand start (trigger)
EH) WarpJITSvc Warp JIT Service Own process Stopped Demand start (trigger)
```

## Slide 22

## Finding Delayed Services

The EPM can be queried programmatically

Well-known endpoints need to be extracted from memory

22


> Recovered by OCR — confidence 80/100 on the text kept, 73/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Finding Delayed Services
RpcView
The EPM can File Options View Filter Help
° Interfaces a
be queried
° Pid Uuid Location Procs
p rogra mM mati Ca | ly 1976 2a82bb21-e44f-4791-9aal-dfae788e2f43 C:\Windows\System32\ubpm.dll 4
. 1976 86d35949-83c9-4044-b424-db363231fd0c C:\Windows\System32\schedsvc.dll 20
Well-known end pol nts 1976 3a9ef155-691d-4449-8d05-09ad57031823 C:\Windows\System32\schedsve.dll 7
need to be extracted from 1484 c9ac6db5-82b7-4e55-aeSa-e464ed7b42... C:\Windows\System32\sysntfy.dll 15
memo ry 2064 7ea/Obcf-48af-4f6a-8968-6a440754d5fa C:\Windows\System32\nsisvc.dll 9
©
```

## Slide 23

## RPC-Recon

#### Retrieves all endpoints on logon

##### EPM

RPC-Recon
Dynamic endpoints
Well-known endpoints

RPC Servers

23

## Slide 24

## RPC-Recon

#### Retrieves all endpoints on logon

EPM

RPC-Recon
Dynamic endpoints
Well-known endpoints
Early
RPC Servers
Scan

24

## Slide 25

## RPC-Recon

Scans again after most
services start
Dynamic endpoints
Well-known endpoints
Early Late
Scan Scan

EPM
RPC Servers

25

## Slide 26

## RPC-Recon

#### Comparing the lists reveals vulnerable interfaces

Late Scan

Early Scan

Vulnerable Interfaces

26

## Slide 27

## RPC-Recon Demo

27


> Recovered by OCR — confidence 71/100 on the text kept, 54/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
RPC-Recon Demo
@
Learn about
this picture #: ta - 1 G ThisPC > Local Disk(C) > temp Search temp Q
é
¥
P é ‘ ® New WN Sort = View se CB Details
jome
ll Desktop
3 Documents
PA Pictures
B Music
WW This Pc
ta Network PR!
```

## Slide 28

## Launching Rogue Server

Known interfaces were registered without admin privileges

The server received connections

The clients were services running as “NT AUTHORITY\SYSTEM”!

28

## Slide 29

## Leveraging The Connections

Can `RpcImpersonateClient` be used?

The level received is Identification

WinAPI will fail due to `ERROR_BAD_IMPERSONATION_LEVEL`

29

## Slide 30

## Leveraging The Connections

\```
typedefenum_SECURITY_IMPERSONATION_LEVEL{
SecurityAnonymous,
SecurityIdentification,
SecurityImpersonation,
SecurityDelegation
\```

\```
} SECURITY_IMPERSONATION_LEVEL, * PSECURITY_IMPERSONATION_LEVEL;
\```

30

## Slide 31

## Leveraging The Connections

▪ Maybe we can force an NTLM authentication?

▪ Accessing remote resources requires delegation

RPC  NTLM Authentication
Authentication
Benign Rogue
RPC Client SMB Server
Rogue
RPC Server

31

## Slide 32

32

## Slide 33

## Looking for Credentials

- Can we gain credentials by registering the right interface?

- We can imitate services used for authentication

▪ No connections received due to Security mechanisms

|Service|Interface|Method|
|---|---|---|
|VaultSvc|bb8b98e8-84dd-45e7-9f34-c3fb6155eeed|VltAddItem|
|wlidsvc|cc105610-da03-467e-bc73-5b9e2937458d|WLIDSetAuthData, WLIDCreateIdentity|
|OneSyncSvc|923c9623-db7f-4b34-9e6d-e86580f8ca2a|AccountsMgmtRpcCreateAccount|

33

## Slide 34

## RPC Security Mechanisms

The client can specify the expected privileges of the server

The RPC runtime will verify it before the connection

\```
typedefstruct_RPC_SECURITY_QOS_V4_W{
unsignedlongVersion;
unsignedlongCapabilities;
unsignedlongIdentityTracking;
unsignedlongImpersonationType;
unsignedlongAdditionalSecurityInfoType;
union
\```

\```
{
\```

\```
RPC_HTTP_TRANSPORT_CREDENTIALS_W*HttpCredentials;
} u;
\```

\```
void*Sid;
\```

\```
unsignedintEffectiveOnly;
\```

- `} RPC_SECURITY_QOS_V4_W, *PRPC_SECURITY_QOS_V4_W;`

34

## Slide 35

## RPC Security Mechanisms

wlidcli.dll (CWLIDBinding::Bind)

35


> Recovered by OCR — confidence 83/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
RPC Security Mechanisms
*&sid.Revision = 0x101;
sid.SubAuthority[@] @x12;
SecurityQOS.Version = 5;
SecurityQOS.Capabilities = 1;
memset (&SecurityQOS.IdentityTracking, @, 24);
v3 = RpcStringBindingComposeW(@LL, L"ncalrpc", @LL, OLL, L"Security=impersonation dynamic false", StringBinding);
|| (v3 = RpcBindingSetAuthInfoExW(Binding, @LL, 6u, @xAu, OLL, 0, &SecurityQOS), v4 = v3 <= @, v3) )
wlidcli.dll (CWLIDBinding::Bind)
```

## Slide 36

37

## Slide 37

## Steps Taken

Attack

Impersonating privileged clients Masquerading as authentication service

Defense

Impersonation policy

Security quality of service

38

## Slide 38

## Manipulating File Access

Can we achieve arbitrary write to protected directories?

Looking for file system services led to “Storage Service”

39

## Slide 39

## Manipulating File Access Registering StorSvc interface resulted in several connections:

RPC Client
Rogue RPC Server
(StorageUsage.dll)

Windows Update
AppXDeploymentClient.dll
(wuaueng.dll)

40

## Slide 40

## Manipulating File Access Registering StorSvc interface resulted in several connections:

Windows Update RPC Client
AppXDeploymentClient.dll Rogue RPC Server
(wuaueng.dll) (StorageUsage.dll)
Storage Service
(StorSvc.dll)

41

## Slide 41

## Manipulating File Access

#### Registering StorSvc interface resulted in several connections:

Windows Update RPC Client
AppXDeploymentClient.dll Rogue RPC Server
(wuaueng.dll) (StorageUsage.dll)
Storage Service
(StorSvc.dll)
Delivery Optimization
(DoSvc.dll)

42

## Slide 42

## Manipulating File Access

The clients invoked 3 undocumented methods

\```
longGetStorageInstanceCount([in] shortarg1, [out] long* arg2);
longGetStorageSettings([in] shortarg1, [in] longarg2, [in] shortarg3, [out] long* arg4);
longGetStorageDeviceInfo([in] intarg1, [in] longarg2, [in, out] structStruct_34_t* arg3);
\```

43

## Slide 43

## Manipulating File Access

▪ Examining the client callstack led to `AppXDeploymentClient.dll`

▪ The public symbols contain definitions of the undocumented methods

44

## Slide 44

## Manipulating File Access

\```
typedefstruct_STORAGE_DEVICE_INFO
{
\```

\```
unsignedintSize;
\```

\```
wchar_tPathName[ 260 ];
\```

\```
STORAGE_DEVICE_PROPERTIESDeviceProperties;
STORAGE_PRESENCE_STATEPresenceState;
STORAGE_DISMOUNT_REASONDismountReason;
STORAGE_VOLUME_STATUSVolumeStatus;
\```

\```
STORAGE_FREE_SPACE_STATEFreeSpaceState;
STORAGE_TEMP_CLEANUP_STATETempCleanupState;
GUIDStorageId;
\```

\```
STORAGE_APP_PAIRING_STATUSAppPairingStatus;
unsigned__int64ReservedSize;
\```

\```
wchar_tFriendlyName[ 260 ];
\```

\```
unsignedintBusType;
\```

\```
unsignedintFileSystemType;
unsignedintPersistentVolumeState;
} STORAGE_DEVICE_INFO;
\```

45

## Slide 45

## Manipulating File Access

▪ DoSvc calls `CreateDirectory` with the path returned ▪ This service is running as “NT AUTHORITY\NETWORK SERVICE”

## Slide 46

## Manipulating File Access

47


> Recovered by OCR — confidence 89/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Manipulating File Access
Event Properties
Event &B Process $ Stack
Date: 24/2025 6:16:58.0074231 PM
Thread: 10368
Class: File System
Operation: CreateFile
Result: SUCCESS
Path: \\renb-insider\cS\Windows\ServiceProfiles\NetworkService\Hello DEF CON 33
Duration: 0.0004970
Desired Access: Read Data/List Directory, Synchronize
Disposition: Create
Options: Directory, Synchronous IO Non-Alert, Open Reparse Point
Attributes: N
ShareMode: Read, Write
AllocationSize: 0
OpenResult: Created
```

## Slide 47

## NT AUTHORITY\NETWORK SERVICE

- Fewer capabilities than the local system account

- Authenticates remote resources with the machine account

48

## Slide 48

## Machine Account

- Represented as COMPUTERNAME$

- Used when the computer accesses remote resources

49


> Recovered by OCR — confidence 84/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Machine Account
a Represented as Active Directory Users and Computers
File Action View Help
] U sed wh en th e 5 Active Directory Users and Com|| Name Type Description
v ia test.domain
computer accesses > ) Builtin RONB-INSIDER Properties ? x
_| Computers
re mote resources 2] Domain Controllers Location Managed By Dialin
> [9] ForeignSecurityPrincipal: General Operating System Member Of Delegation LAPS
> |) Managed Service Accour Member of:
> _J Users -
Name Active Directory Domain Services Folder
Domain Computers test.domain/Users
```

## Slide 49

## Machine Account

50


> Recovered by OCR — confidence 84/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Using machine account
passwords during an engagement
Posted on 30th October 2017 by Adam Chester
FEBRUARY 1, 2022
Machine Domain Escalation —Machine- Accounts
Acco U nt s 4 by Administrator. In Domain Escalation. Leave a Comment
> (2 Copy wv
```

## Slide 50

## Forcing Machine Account Authentication

▪ Returning a network share forces an authentication

▪ It can be used for NTLM relay

Rogue SMB Server Network Resource
3. NTLM Authentication 4. NTLM Relay
DoSvc
1. GetStorageDeviceInfo
Rogue RPC
Server
2. \\RogueSmbServer\Share

## Slide 51

## Success!

52

## Slide 52

## Attack Flow

EPM
2. Where is  StorSvc?
1.  StorSvc  is at EvilEndpoint
3. EvilEndpoint
6. Machine Account
4. GetStorageDeviceInfo()
NTLM Authentication
5. \\RogueSmbServer\Share
Rogue SMB
Rogue RPC Delivery
Server
Server Optimization

53

## Slide 53

## RPC-Racer

- New tool to launch rogue RPC interfaces

- Designed to be executed on logon

- Forces authentication of the machine account

- Patch for CVE-2025-49760 was released on July 8th, 2025

54

## Slide 54

### Where can we relay the machine account authentication?

NTLM Authentication Relayed Victim Rogue Authentication SMB Server

55

## Slide 55

## ESC8

- Targets Active Directory Certificate Service (ADCS)

- ADCS web server can enroll certificates

- Certificates can be used for authentication

56

## Slide 56

## ESC8

#### **Step 1:** Requesting a certificate for DC$

1. Machine  2. Relayed
Account NTLM  Authentication
Authentication
3. DC$ certificate
Domain Rogue  ADCS
Controller SMB Server

57

## Slide 57

## ESC8

#### **Step 2:** using the certificate to request TGT

DC$ certificate
DC$ ticket

Rogue SMB Server

Domain
Controller

58

## Slide 58

## ESC8

#### **Step 3:** using the TGT to dump password hashes

DC$ ticket
Secrets Dump

Rogue SMB Server

Domain
Controller

59

## Slide 59

## RPC-Racer Demo

60

## Slide 60

## Implications

Man in the
Middle

Denial of Service

Stealing
Credentials

61

## Slide 61

## Takeaways

The destination address of every protocol should be verified by the source

RPC Verify RPC
Client Identity Server
RPC Request
RPC Response

62

## Slide 62

## Takeaways

Any stage where untrusted code can be executed should be considered unsafe Services should be launched as early as possible

63

## Slide 63

## CVE-2025-49760

StorageUsage.dll was patched

Security QOS applied to Binding handle

64


> Recovered by OCR — confidence 81/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
__int64 _ fastcall StorageSvcInit(RPC_BINDING_HANDLE *Binding)
{
// [COLLAPSED LOCAL DECLARATIONS. PRESS NUMPAD "+" TO EXPAND]
*&pIdentifierAuthority.Value[4] = @x50ee;
CVE-2025-49760 ea
*pTdentifierAuthority.Value = @;
returnValue = @;
pSid = @LL;
Sto fa ge U Sage d | | wil::details::FeatureImpl<__WilFeatureTraits_Feature_3064785210>::__ private_IsEnabled(& wil: :Fea
{
Was patched if ( !AllocateAndInitializeSid(&pIdentifierAuthority, lu, @xl2u, @, @, @, @, @, @, @, &pSid) )
{
sosssuussessesssnsnssesssesssnasesessensnnuuseseesssnnnsesessestsnuseseessssnuuasessessnnnnssseeenssnnuesseeesnsnnuaceseeesnnnnsesesensnsnueeceeesesnneeceeeeetense LastError = GetLastError();
returnValue = LastError;
Security QOS applied to goto LABEL_5;
}
Bindin ha ndle tmpSecQOS.Version = 5;
g *(&tmpSecQOS .AdditionalSecurityInfoType + 1) = Q;
tmpSecQOS.Sid = pSid;
tmpSecQOS.Capabilities = 17;
tmpSecQOS.u.HttpCredentials = @LL;
```

## Slide 64

## Detection

#### Validate registrations to the EPM

No
Allow
Is UUID
RpcEpRegister
known?
Monitored
Block
process
Yes

65

## Slide 65

## Detection

#### Monitor ETW

(Delivery Optimization)

(RPC-Racer)
(Storage Service)
(GetStorageDeviceInfo)

66


> Recovered by OCR — confidence 90/100 on the text kept, 86/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Detection
Monitor ETW
Event 5, RPC (Microsoft-Windows-RPC)
General Details
fe} Friendly View O XML View
[ ProcessID]
[ ThreadID]
Channel
Computer
Security
- EventData
ProcNum 4
9816 (Delivery Optimization)
6676
RONB-INSIDER
Event 6, RPC (Microsoft-Windows-RPC)
General Details
O Friendly View O XML View
[ ThreadID}
Channel
Computer
Security
- EventData
InterfaceUuid (44d1520b-6133-41f0-8a66-d37305ecc357}
ProcNum
14100 (RPC-Racer)
13212
RONB-INSIDER
Protocol 3
NetworkAddress NULL
LRPC-4f19b232ab44a076a2
Endpoint
4 (GetStorageDevicelnfo)
Protocol 3
NetworkAddress NULL
LRPC-4f19b232ab44a076a2
(Storage Service)
```

## Slide 66

## Further Research

#### Force DoSvc to use poisoned config files

C:\Windows\ServiceProfiles\NetworkService\AppData\Local\Microsoft\Windows\DeliveryOptimization\State\keyValueLKG.dat

67

## Slide 67

## Further Research

#### Force DoSvc to use poisoned config files

C:\Windows\ServiceProfiles\NetworkService\AppData\Local\Microsoft\Windows\DeliveryOptimization\State\dosvcState.dat

68

## Slide 68

## Further Research

Find additional RPC servers with RPC-Recon

Security Center is vulnerable

69


> Recovered by OCR — confidence 95/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Further Research
Find additional RPC servers with
RPC-Recon
Security Center is vulnerable
O
Ud
Security at a glance
See what's happening with the security and health of your device
and take any actions needed.
Virus & threat protection
No action needed
Account protection
No action needed
Firewall & network protection
No action needed
App & browser control
No action needed
```

## Slide 69

## Conclusion

New attack discovered – EPM Poisoning RPC-Recon is released to map targets

Methods to analyze clients were shown

RPC-Racer is released to force NTLM authentication

70

## Slide 70

## Thank you

@RonB_Y

www.linkedin.com/in/ron-by

github.com/SafeBreach-Labs/RPC-Racer

71
