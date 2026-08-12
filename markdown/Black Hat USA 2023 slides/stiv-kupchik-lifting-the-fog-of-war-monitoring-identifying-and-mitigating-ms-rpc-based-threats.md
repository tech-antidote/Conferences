---
title: "Lifting the Fog of War - Monitoring, Identifying and Mitigating MS-RPC Based Threats"
speakers: ["Stiv Kupchik"]
conference: "Black Hat"
conference_full: "Black Hat USA 2023"
edition: "USA"
year: 2023
source_pdf: "Black Hat USA 2023 slides/Stiv Kupchik_Lifting the Fog of War - Monitoring, Identifying and Mitigating MS-RPC Based Threats.pdf"
pages: 101
sha256: "818d8fef756361882e1731af0d76314b033fc58e07d5db27c23dfc849275c4ed"
text_chars: 26325
ocr_pages: 6
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:24:33Z"
---
# Lifting the Fog of War - Monitoring, Identifying and Mitigating MS-RPC Based Threats

**Speakers:** Stiv Kupchik  
**Conference:** Black Hat USA 2023  
**Source:** `Black Hat USA 2023 slides/Stiv Kupchik_Lifting the Fog of War - Monitoring, Identifying and Mitigating MS-RPC Based Threats.pdf` (101 pages)

## Slide 1

**Lifting the Fog of War Monitoring, Identifying and Mitigating MS-RPC Based Threats**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
o~ :
pifex hat Cakamai
Lifting the Fog of War
Monitoring, Identifying and Mitigating MS-RPC Based Threats
```

## Slide 2

## **whoami**

#### **Stiv Kupchik**

Security Researcher Akamai

@kupsul

Background in DFIR and Windows internals

## Slide 3

## **Agenda**

❏ MS-RPC introduction and overview

- ❏ ETW introduction and overview

- ❏ Using ETW to detect MS-RPC based attacks

- ❏ Supplementing defense with RPC Filters

## Slide 4

# **#define RPC**

## Slide 5

## **It’s** **everywhere in the network**

## Slide 6

**… and is involved in many parts of the attack matrix**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ment Tels
extern
atic
satan ns Layer Protoce sitration
Through Removable Media
Exfitration
jacking
Network Medium
amain Trust biecavery
Policy Medication
use Alternate
utnentication Material
(Netwark Denial of Service
Protocol Tunnel
Indirect Coron
Modify System image
— = ... and Is Involve
in many parts of
the attack matrix
nfuscated
```

## Slide 7

## **RPC Attacks are Hard to Detect**

- RPC is another layer of encapsulation that you need to peel

   - Deep packet inspection is expensive, usually only connection metadata

## Slide 8

## **RPC Attacks are Hard to Detect**

- RPC is another layer of encapsulation that you need to peel

   - Deep packet inspection is expensive, usually only connection metadata

- Most RPC servers are running under svchost or protected processes

   - Difficult to match traffic to process or RPC server

## Slide 9

## **RPC Attacks are Hard to Detect**

- RPC is another layer of encapsulation that you need to peel

   - Deep packet inspection is expensive, usually only connection metadata

- Most RPC servers are running under svchost or protected processes

   - Difficult to match traffic to process or RPC server

- RPC traffic can occur over ephemeral ports

   - Can’t create FW rules in advance

## Slide 10

## **Not Many (documented) Defense Options**

- RPC Filters in the Windows Firewall

- ETW monitors aimed at researchers

   - <u>RpcMon</u> by CyberArk

   - <u>RpcInvestigator</u> by TrailOfBits

- <u>RPC Firewall</u> by ZeroNetworks

   - requires process injection & hooks

## Slide 11

## **RPC without visibility**

## Slide 12

**RPC with visibility**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
RPC with visibility
svcctl<ROpenSCManager2>
svcctl<RCreateServiceW>
cctl<RCloseServiceHandl
svcctl<ROpenServiceW>
svcctl<RStartServiceW>
l<RQueryServiceStatu
svcctl<RQueryServiceStatus>
svcctl<RCloseServiceHandle>
svcctl<RCloseServiceHandle>
svcctl<ROpenSCManager2>
svcctl<ROpenServiceW>
svcctl<RControlService>
svcctl<RQueryServiceStatus>
cctl<RCloseServiceHandl
vcctl<ROpenServiceW>.
svcectl<RDeleteService>
svcctl<RCloseServiceHandle>
svcctl<RCloseServiceHandle>
```

## Slide 13

# **MS-RPC Overview**

## Slide 14

## **Terminology you’ll soon master**

- Interface

- {M}IDL

- Transport

- Endpoint

- Binding

## Slide 15

## **The RPC Client-Server Model**

Server

Client

## Slide 16

## **The RPC Client-Server Model**

Server
Foo(5, “Hello”)
Client

## Slide 17

## **The RPC Client-Server Model**

[ uuid(12345678-4000-2006-0000-2 0000000001a) ] interface **Test** { void **Foo** ([in] int number, [in] char *message); void **Bar** ([out] int * result); }

Server
Foo(5, “Hello”)
Client

## Slide 18

## **The RPC Client-Server Model**

Server
[
uuid(12345678-4000-2006-0000-2 Test_s.c
0000000001a)
]
interface  Test
{ Test.h
MIDL.exe Foo(5, “Hello”)
void  Foo ([in] int number,
[in] char *message);
void  Bar ([out] int * result);
}
Test_c.c
Client

## Slide 19

## **The RPC Client-Server Model**

Server
[
uuid(12345678-4000-2006-0000-2 Test_s.c
0000000001a)
]
interface  Test
{ Test.h
MIDL.exe Foo(5, “Hello”)
void  Foo ([in] int number,
[in] char *message);
void  Bar ([out] int * result);
}
Test_c.c
Client

## Slide 20

## **Endpoints**

### ● The server registers an _endpoint_ using a certain _transport_

|**Transports**|**Protocol Sequence**|**Endpoints**|
|---|---|---|
|TCP|ncacn_ip_tcp|<port number>|
|Named pipe|ncacn_np|<pipe name>|
|UDP|ncadg_ip_udp|<port number>|
|ALPC|ncalrpc|<ALPC port>|
|HTTP|ncacn_http|<hostname>|
|Hyper-V socket|ncacn_hvsocket|<UUID>|

## Slide 21

## **Well-Known Endpoints**

## **Dynamic Endpoints**

Server
Foo(5, “Hello”)
[TCP port 39776]
Client

## Slide 22

## **Well-Known Endpoints**

## **Dynamic Endpoints**

Server EP Mapper Server
Hi I need
Foo(5, “Hello”) server <UUID>
[TCP port 39776] [TCP port 135]
Client Client

## Slide 23

## **Well-Known Endpoints**

## **Dynamic Endpoints**

Server EP Mapper Server
Ok talk  Hi I need
Foo(5, “Hello”) to TCP  server <UUID>
[TCP port 39776] port  [TCP port 135]
50501
Client Client

## Slide 24

## **Well-Known Endpoints**

## **Dynamic Endpoints**

Server EP Mapper Server
Ok talk  Hi I need
Foo(5, “Hello”) to TCP  server <UUID> Foo(5, “Hello”)
[TCP port 39776] port  [TCP port 135] [TCP port 50501]
50501
Client Client

## Slide 25

## **Binding**

- The representation of a session between a client and a server

   - Practically, a handle

   - Client and server can manipulate binding data using designated functions

   - Used for authentication (among other things)

## Slide 26

**An RPC Call’s Flow**

Client Server
Foo(5, “hello”)

## Slide 27

## **An RPC Call’s Flow**

Client Server
Foo(5, “hello”)
NdrClientCall3()

## Slide 28

## **An RPC Call’s Flow**

Client Server
Foo(5, “hello”)
NdrClientCall3()
●
Marshall parameters
●
Connect to endpoint
● Bind to server
● Authenticate

RPC Runtime ( rpcrt4.dll )

## Slide 29

Client Server
Foo(5, “hello”)
NdrClientCall3()

## **An RPC Call’s Flow**

●
Listen on endpoint
●
Marshall parameters
● Unmarshall
●
Connect to endpoint
parameters
● Bind to server
● Perform access
● Authenticate
checks
RPC Runtime ( rpcrt4.dll )

## Slide 30

Client Server
Foo(5, “hello”) Foo(5, “hello”)
NdrClientCall3()

## **An RPC Call’s Flow**

●
Listen on endpoint
●
Marshall parameters
● Unmarshall
●
Connect to endpoint
parameters
● Bind to server
● Perform access
● Authenticate
checks
RPC Runtime ( rpcrt4.dll )

## Slide 31

## **Zooming In**

<u>IDL:</u>

void Foo([in] int number, [in] char* message);

Client Foo(5, “hello”) NdrClientCall3()

## Slide 32

## **Zooming In**

<u>IDL:</u>

void Foo([in] int number, [in] char* message);

**MIDL.exe**

Client

Foo(5, “hello”)

NdrClientCall3()

<u>Test_c.c:</u> void Foo( handle_t IDL_handle, int number, unsigned char *message) {

NdrClientCall3( (PMIDL_STUBLESS_PROXY_INFO )&Test_ProxyInfo, 0, 0, IDL_handle, number, message); }

## Slide 33

## **Zooming In**

<u>IDL:</u>

void Foo([in] int number, [in] char* message);

**MIDL.exe**

Client Foo(5, “hello”) NdrClientCall3()

<u>Test_c.c:</u> void Foo( handle_t IDL_handle, int number, unsigned char *message) {

NdrClientCall3( (PMIDL_STUBLESS_PROXY_INFO )&Test_ProxyInfo , 0, 0, IDL_handle, number, message); } Opnum

## Slide 34

## **Quick Recap**

- Interface – describes server functionality

[UUID]

- Transport – the communication medium

   - [protocol sequence]

- Endpoint – destination to connect to

[port, pipe name, etc.]

- Binding – represents a client-server session [binding handle]

## Slide 35

**RPC Visibility**

## Slide 36

## **#define ETW**

● Event Tracing for Windows ( <u>ETW)</u> is a built-in tracing and logging mechanism

## Slide 37

## **#define ETW**

- Event Tracing for Windows ( <u>ETW)</u> is a built-in tracing and logging mechanism

- Provider-consumer model

   - Providers define a <u>schema</u> for their events so consumers can parse them

   - Both providers and consumers need to register with the ETW

## Slide 38

## **#define ETW**

- Event Tracing for Windows ( <u>ETW)</u> is a built-in tracing and logging mechanism

- Provider-consumer model

   - Providers define a <u>schema</u> for their events so consumers can parse them

   - Both providers and consumers need to register with the ETW

- UM logic implemented in ntdll, transfers control to kernel

## Slide 39

## **Provider <> Consumer**

Application process EtwEventRegister(DEADBEEF-BAAD-DEAD-BEEF-BAADF00D)

Windows Kernel

## Slide 40

## **Provider <> Consumer**

Application process
RegHandle
Windows Kernel

## Slide 41

## **Provider <> Consumer**

Application process
EventWrite(RegHandle, <event_data>)
Windows Kernel

## Slide 42

Provider <> Consumer
Application process
<event_data>
Windows Kernel

## Slide 43

## **Context is Important**

● Since events need to hop the kernel boundary, it is a waste to send them when no consumers are tracing events

## Slide 44

## **Context is Important**

- Since events need to hop the kernel boundary, it is a waste to send them when no consumers are tracing events

- Providers can define a callback to the kernel, to be notified about the state of the provider

## Slide 45

## **Context is Important**

- Since events need to hop the kernel boundary, it is a waste to send them when no consumers are tracing events

- Providers can define a callback to the kernel, to be notified about the state of the provider

- If there are no consumers, the provider is considered disabled and can skip event writing

## Slide 46

void Penablecallback(

[in] LPCGUID SourceId,

[in] ULONG IsEnabled,

[in] UCHAR Level,

[in] ULONGLONG MatchAnyKeyword,

ULONGLONG MatchAllKeyword,

[in, optional] PEVENT_FILTER_DESCRIPTOR FilterData,

[in, optional] PVOID CallbackContext

)

## Slide 47

## **Provider <> Consumer**

Application process

Provider enabled?

Windows Kernel

## Slide 48

## **Provider <> Consumer**

Application process

Event consumer

EnableTraceEx2(DEADBEEF-BAAD-DEAD-BEEF-BAADF00D)

Windows Kernel

## Slide 49

## **Provider <> Consumer**

Application process Event consumer
EventWrite(RegHandle, <event_data>)
<event_data>

Windows Kernel

## Slide 50

## **RPC ETW Provider**

- <u>Microsoft-Windows-RPC</u><sup>1</sup> {6ad52b32-d609-4be9-ae07-ce8dae937e39}

- Implemented in the runtime _rpcrt4.dll_

   - Since event routing is handled in the kernel, multiple processes can write to the same provider

- 13 different events

   - Event ids 5,7 — Client call start/stop

   - Event ids 6,8 –- Server call start/stop

1 https://github.com/repnz/etw-providers-docs/blob/master/Manifests-Win7-7600/Microsoft-Windows-RPC.xml

## Slide 51

## **Call Start Schema**

<template tid="RpcServerCallStartArgs_V1">

<data name="InterfaceUuid" inType="win:GUID"/>

- <data name="ProcNum" inType="win:UInt32"/>

- <data name="Protocol" inType="win:UInt32"/>

- <data name="NetworkAddress" inType="win:UnicodeString"/>

- <data name="Endpoint" inType="win:UnicodeString"/>

- <data name="Options" inType="win:UnicodeString"/>

- <data name="AuthenticationLevel" inType="win:UInt32"/> <data name="AuthenticationService" inType="win:UInt32"/> <data name="ImpersonationLevel" inType="win:UInt32"/>

</template>

## Slide 52

## **Call Start Schema**

- <template tid="RpcServerCallStartArgs_V1">

- <data name="InterfaceUuid" inType="win:GUID"/>

- <data name="ProcNum" inType="win:UInt32"/>

- <data name="Protocol" inType="win:UInt32"/>

- <data name="NetworkAddress" inType="win:UnicodeString"/>

- <data name="Endpoint" inType="win:UnicodeString"/>

- <data name="Options" inType="win:UnicodeString"/>

- <data name="AuthenticationLevel" inType="win:UInt32"/>

- <data name="AuthenticationService" inType="win:UInt32"/>

- <data name="ImpersonationLevel" inType="win:UInt32"/>

- </template>

## Slide 53

## **Additional Useful Event Headers**

● ActivityId — a UUID that can be used to track event chains (Call start, stop, error)

● ProcessId — the PID of the process that sent the trace event

● Timestamp — the time the trace event was generated

## Slide 54

**Attack Detection?**

## Slide 55

## **Server Trace Events Are Lacking**

if ( (Microsoft_Windows_RPCEnableBits & 2) != 0 ) McTemplateU0jqqzzzqqq_EtwEventWriteTransfer( *(_QWORD *)(*((_QWORD *)this + 38) + 80i64), (__int64)&RpcServerCallStartEvent,      // Event descriptor (__int64)v4 + 84,                       // Interface UUID *((_DWORD *)this + 95),                 // Opnum v25[48],                                // Transfer protocol id 0i64,                                   // Network address *(const wchar_t **)(*(_QWORD *)(*((_QWORD *)this + 38) + 80i64) + 32i64),// Endpoint 0i64,                                   // Options v25[32],                                // Authentication level v25[36],                                // Authentication service 0);                                     // Impersonation level

**_OSF_SCALL::DispatchHelper_**

## Slide 56

## **Server Trace Events Are Lacking**

if ( (Microsoft_Windows_RPCEnableBits & 2) != 0 ) McTemplateU0jqqzzzqqq_EtwEventWriteTransfer( *(_QWORD *)(*((_QWORD *)this + 38) + 80i64), (__int64)&RpcServerCallStartEvent,      // Event descriptor (__int64)v4 + 84,                       // Interface UUID *((_DWORD *)this + 95),                 // Opnum v25[48],                                // Transfer protocol id 0i64,                                   // Network address *(const wchar_t **)(*(_QWORD *)(*((_QWORD *)this + 38) + 80i64) + 32i64),// Endpoint 0i64,                                   // Options v25[32],                                // Authentication level v25[36],                                // Authentication service 0);                                     // Impersonation level

**_OSF_SCALL::DispatchHelper_**

## Slide 57

## **Just Do Client Calls, Dummy…**

● We’re looking for malicious traffic, assume client is in the attacker’s control

● Attackers can:

## Slide 58

## **Just Do Client Calls, Dummy…**

● We’re looking for malicious traffic, assume client is in the attacker’s control

- Attackers can:

   - Tamper with ETW events via hooks/memory manipulation

## Slide 59

## **Just Do Client Calls, Dummy…**

- We’re looking for malicious traffic, assume client is in the attacker’s control

- Attackers can:

   - Tamper with ETW events via hooks/memory manipulation

   - Use their own machine outside of our control + local proxy (no ETW then)

## Slide 60

## **Just Do Client Calls, Dummy…**

- We’re looking for malicious traffic, assume client is in the attacker’s control

- Attackers can:

   - Tamper with ETW events via hooks/memory manipulation

   - Use their own machine outside of our control + local proxy (no ETW then)

   - Generate RPC traffic without the OS (i.e Impacket)

## Slide 61

## **ETW to the Rescue, Again**

ETW FIND ETW

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ETW to the Rescue, Again
lusedthe ETW to FIND the: ETW .
```

## Slide 62

## **TCP ETW**

**event 1017 — TcpAcceptListenerComplete**

<template tid="TcpAccpetListenerRouteLookupFailureArgs"> <data name="LocalAddressLength" inType="win:UInt32"/>

<data name="LocalAddress" inType="win:Binary"  length=”LocalAddressLength”/> <data name="RemoteAddressLength" inType="win:UInt32"/> <data name="RemoteAddress" inType="win:Binary"  length=”RemoteAddressLength”/>

…

</template>

Address binary field := AF, IP, port

https://github.com/repnz/etw-providers-docs/blob/master/Manifests-Win10-17134/Microsoft-Windows-TCPIP.xml

## Slide 63

## **TCP ETW**

**event 1017 — TcpAcceptListenerComplete**

<template tid="TcpAccpetListenerRouteLookupFailureArgs"> <data name="LocalAddressLength" inType="win:UInt32"/>

<data name="LocalAddress" inType="win:Binary"  length=”LocalAddressLength”/> <data name="RemoteAddressLength" inType="win:UInt32"/> <data name="RemoteAddress" inType="win:Binary"  length=”RemoteAddressLength”/>

…

</template>

Address binary field := AF, IP, port

https://github.com/repnz/etw-providers-docs/blob/master/Manifests-Win10-17134/Microsoft-Windows-TCPIP.xml

## Slide 64

## **SMB ETW**

**event 500 — Smb2ConnectionAcceptStart** <template tid="Smb2ConnectionAcceptStart">

<data name="ConnectionGUID" inType="win:GUID"/> <data name="AddressLength" inType="win:UInt32"/> <data name="Address" inType="win:Binary" length=”AddressLength”/>

</template>

https://github.com/repnz/etw-providers-docs/blob/master/Manifests-Win10-17134/Microsoft-Windows-SMBServer.xml

## Slide 65

## **SMB ETW**

**event 500 — Smb2ConnectionAcceptStart** <template tid="Smb2ConnectionAcceptStart"> <data name="ConnectionGUID" inType="win:GUID"/> <data name="AddressLength" inType="win:UInt32"/>

<data name="Address" inType="win:Binary" length=”AddressLength”/> </template>

https://github.com/repnz/etw-providers-docs/blob/master/Manifests-Win10-17134/Microsoft-Windows-SMBServer.xml

## Slide 66

## **SMB ETW**

**event 500 — Smb2ConnectionAcceptStart**

<template tid="Smb2ConnectionAcceptStart">

<data name="ConnectionGUID" inType="win:GUID"/>

<data name="AddressLength" inType="win:UInt32"/>

<data name="Address"

inType="win:Binary" length=”AddressLength”/> </template>

**event 8 — Smb2RequestCreate_V2**

<template tid="Smb2RequestCreate_V2">

…

<data name="Filename" inType="win:UnicodeString"/>

…

<data name="ConnectionGUID" inType="win:GUID"/>

<data name="TreeConnectGUID" inType="win:GUID"/>

</template>

https://github.com/repnz/etw-providers-docs/blob/master/Manifests-Win10-17134/Microsoft-Windows-SMBServer.xml

## Slide 67

## **SMB ETW**

**event 500 — Smb2ConnectionAcceptStart**

<template tid="Smb2ConnectionAcceptStart">

<data name="ConnectionGUID" inType="win:GUID"/>

<data name="AddressLength" inType="win:UInt32"/>

<data name="Address"

inType="win:Binary" length=”AddressLength”/> </template>

**event 8 — Smb2RequestCreate_V2**

<template tid="Smb2RequestCreate_V2">

…

<data name="Filename" inType="win:UnicodeString"/>

…

<data name="ConnectionGUID" inType="win:GUID"/>

<data name="TreeConnectGUID"

inType="win:GUID"/> </template>

https://github.com/repnz/etw-providers-docs/blob/master/Manifests-Win10-17134/Microsoft-Windows-SMBServer.xml

## Slide 68

## **SMB ETW**

**event 500 — Smb2ConnectionAcceptStart**

<template tid="Smb2ConnectionAcceptStart">

**event 8 — Smb2RequestCreate_V2**

<template tid="Smb2RequestCreate_V2">

<data name="ConnectionGUID" inType="win:GUID"/>

<data name="AddressLength" inType="win:UInt32"/>

<data name="Address"

inType="win:Binary" length=”AddressLength”/> </template>

…

<data name="Filename" inType="win:UnicodeString"/>

…

<data name="ConnectionGUID" inType="win:GUID"/>

<data name="TreeConnectGUID" inType="win:GUID"/> </template>

https://github.com/repnz/etw-providers-docs/blob/master/Manifests-Win10-17134/Microsoft-Windows-SMBServer.xml

## Slide 69

## **SMB ETW**

**event 500 — Smb2ConnectionAcceptStart**

<template tid="Smb2ConnectionAcceptStart"> <data name="ConnectionGUID" inType="win:GUID"/> <data name="AddressLength" inType="win:UInt32"/>

<data name="Address" inType="win:Binary" length=”AddressLength”/> </template>

**event 8 — Smb2RequestCreate_V2**

<template tid="Smb2RequestCreate_V2">

…

<data name="Filename" inType="win:UnicodeString"/> …

<data name="ConnectionGUID" inType="win:GUID"/> <data name="TreeConnectGUID" inType="win:GUID"/> </template>

https://github.com/repnz/etw-providers-docs/blob/master/Manifests-Win10-17134/Microsoft-Windows-SMBServer.xml

## Slide 70

## **Matching Flows**

##### **RPC Request Processing**

Windows Kernel **SMB Provider**

UM Process ETW Consumer

## Slide 71

## **Matching Flows**

##### **RPC Request Processing**

UM Process ETW Consumer

<IP> : <Connection GUID>

## Slide 72

## **Matching Flows**

**RPC Request Processing**

Windows Kernel **SMB Provider**

<Connection GUID> <Pipe>

UM Process <IP> : <Connection GUID> ETW Consumer

## Slide 73

## **Matching Flows**

##### **RPC Request Processing**

UM Process ETW Consumer

<IP> : <Connection GUID> <Connection GUID> : <Pipe>

## Slide 74

## **Matching Flows**

##### **RPC Request Processing**

UM Process
RPC Provider
UM Process <IP> : <Connection GUID>
ETW Consumer <Connection GUID> : <Pipe>
<Pipe><Opnum>
<Interface>

## Slide 75

## **Matching Flows**

##### **RPC Request Processing**

UM Process ETW Consumer

<IP> : <Connection GUID> <Connection GUID> : <Pipe> <Pipe> : <Interface, Opnum>

## Slide 76

## **Matching Flows**

Machine <IP> connected over <Pipe> to request operation <Opnum> of the interface <Interface>

## Slide 77

## **RPC Visibility**

- Python script<sup>1</sup> with pywintrace

- Subscribe to the SMB, TCP and RPC providers

- Send results to Neo4J for easy visualization and querying

   - Could be extended to use other databases

1 <u>https://github.com/akamai/akamai-security-research/rpc_visibility</u>

## Slide 78

**Attack Detection**

## Slide 79

# **Demo Time**

**RPC Visibility VS PSExec**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
’ | HAVE PSEXEC
Demo Time
RPC Visibility VS PSExec
=e
ny boil PYWINTRAGE neal
```

## Slide 80

## **PSExec**

● Both a general name for attack technique and a sysinternals tool

- Copy service PE to remote machine’s ADMIN$ share

- Tell the SCM (using <u>MS-SCMR)</u> to run a service from the copied binary

○ 0xC — RCreateServiceW

1. SMB cp psexesvc.exe \\VICTIM\ADMIN$\psexesvc.exe 2. RPC, MS-SCMR RCreateServiceW(\\VICTIM, C:\Windows\psexesvc.exe)

## Slide 81

## **DCSync**

- Connect to a DC and pretend to be another DC

   - Request replication of the credential database

- Uses the Directory Replication service ( <u>MS-DRSR )</u>

   - 0x3 — IDL_DRSGetNCChanges

## Slide 82

## **DCSync**

- Connect to a DC and pretend to be another DC

   - Request replication of the credential database

- Uses the Directory Replication service ( <u>MS-DRSR)</u>

   - 0x3 — IDL_DRSGetNCChanges

## Slide 83

## **PetitPotam**

- Tell the EFS service to open a remote file

   - Triggers an SMB connection with authentication that can be relayed

- Uses the <u>MS-EFSR</u> interface

   - 0x0 — EfsRpcOpenFileRaw

   - 0x4 — EfsRpcEncryptFileSrv

## Slide 84

## **Task Scheduler**

- Create a scheduled task remotely

   - MITRE <u>T1053.005</u>

- Uses the Task Scheduler Service Remoting protocol <u>MS-TSCH</u> ○ 0x1 — SchRpcRegisterTask

## Slide 85

## **Remote WMI**

- Use WMI to execute a binary remotely

- Implemented over <u>MS-DCOM</u>

   - Another layer of encapsulation

   - Can’t easily tell which operation was requested

## Slide 86

## **Determining WMI maliciousness**

- Check the opnums in each malicious operation, compared to benign ○ Heuristic based approach, has to be configured for each technique

###### WMIC process get

|WMICprocess call create||Interface Name|Opnums|
|---|---|---|---|
|Interface Name|Opnums|iwbemservices|20|
|iwbemservices|24, 6|iremunknown2|5, 3|
|iremunknown2|5, 3|iwbemlevel1login|6, 3|
|iwbemlevel1login|6, 3|iwbemloginclientid|3|
|iwbemloginclientid|3|iremotescmactivator|4|
|iremotescmactivator|4|iobjectexporter|5|
|iobjectexporter|5|iwbemwcosmartenum
iwbemfetchsmartenum|3
3|

## Slide 87

## **Determining WMI maliciousness**

- Check the opnums in each malicious operation, compared to benign ○ Heuristic based approach, has to be configured for each technique

###### WMIC process get

|WMICprocess call create||Interface Name|Opnums|
|---|---|---|---|
|Interface Name|Opnums|iwbemservices|20|
|iwbemservices|24, 6|iremunknown2|5, 3|
|iremunknown2|5, 3|iwbemlevel1login|6, 3|
|iwbemlevel1login|6, 3|iwbemloginclientid|3|
|iwbemloginclientid|3|iremotescmactivator|4|
|iremotescmactivator|4|iobjectexporter|5|
|iobjectexporter|5|iwbemwcosmartenum
iwbemfetchsmartenum|3
3|

## Slide 88

## **Determining WMI maliciousness**

- Check the opnums in each malicious operation, compared to benign ○ Heuristic based approach, has to be configured for each technique

WMIC process get

WMIC process call create
Interface Name Opnums
Interface Name Opnums
iwbemservices ExecQuery
ExecMethod
iwbemservices iwbemwcosmartenum Next
GetObject
iwbemfetchsmartenum GetSmartEnum

## Slide 89

## **Drawbacks**

- Still only metadata based detection

- Can’t differentiate between “good” and “bad” flows

   - Detection has to be context dependent

   - Will have to be heuristics based analysis

- No blocking, visibility only

- Can’t handle DCOM with certainty

## Slide 90

**Incident Response & Mitigation**

## Slide 91

## **#define RPC Filters**

● Filtering mechanism part of the Windows Firewall

● Exposed through _netsh_ or via WinAPI

● Available since Windows Vista

netsh rpc filter>show filter Listing all RPC Filters. --------------------------------filterKey: ac65a4a0-0ab9-11ee-b826-8038fb83bd95 displayData.name: RPCFilter displayData.description: RPC Filter filterId: 0x2e0773 layerKey: um weight: Type: FWP_EMPTY Value: Empty action.type: block numFilterConditions: 1 filterCondition[0] fieldKey: if_uuid matchType: FWP_MATCH_EQUAL conditionValue: Type: FWP_BYTE_ARRAY16_TYPE Value: 367abb81 35f19844 f09832ad 03100038

## Slide 92

## **Layers? Is it a cake?**

- Filtering can occur at different parts of the RPC connections

- Pre-defined layers tell the FW where to apply the rule

   - FWPM_LAYER_RPC_UM — connection to interface

   - FWPM_LAYER_RPC_EPMAP — connection to the endpoint mapper

   - FWPM_LAYER_RPC_EP_ADD — new endpoint registration

## Slide 93

## **#define RPC Filters**

● Filtering mechanism part of the Windows Firewall ● Exposed through _netsh_ or via WinAPI

● Available since Windows Vista

netsh rpc filter>show filter Listing all RPC Filters. --------------------------------filterKey: ac65a4a0-0ab9-11ee-b826-8038fb83bd95 displayData.name: RPCFilter displayData.description: RPC Filter filterId: 0x2e0773 layerKey: um weight: Type: FWP_EMPTY Value: Empty action.type: block numFilterConditions: 1 filterCondition[0] fieldKey: if_uuid matchType: FWP_MATCH_EQUAL conditionValue: Type: FWP_BYTE_ARRAY16_TYPE Value: 367abb81 35f19844 f09832ad 03100038

## Slide 94

## **Filter fields**

- src & dst IP

- RPC endpoints (port/named pipe)

- RPC interface UUID

- User token

.

. .

###### Full list + notes in our <u>GH</u>

## Slide 95

## **Mitigation strategies**

After understanding what RPC traffic is going on in the network (using ETW), we can:

## Slide 96

## **Mitigation strategies**

After understanding what RPC traffic is going on in the network (using ETW), we can:

- Block unused RPC interfaces that can be used by attackers

   - If no one is using SCMR, why should it be left open?

## Slide 97

## **Mitigation strategies**

After understanding what RPC traffic is going on in the network (using ETW), we can:

- Block unused RPC interfaces that can be used by attackers

   - If no one is using SCMR, why should it be left open?

- Block RPC interfaces once an attack is detected/suspected

   - Emergency anti-lateral movement button

## Slide 98

## **Mitigation strategies**

After understanding what RPC traffic is going on in the network (using ETW), we can:

- Block unused RPC interfaces that can be used by attackers

   - If no one is using SCMR, why should it be left open?

- Block RPC interfaces once an attack is detected/suspected

   - Emergency anti-lateral movement button

- Restrict compromised users using RPC filters

## Slide 99

## **Summary**

- The RPC ETW provider is a treasure trove of information

- Use it to to get the gist of what is going on in the network, and detect potential malicious activity

- Respond to incidents with RPC filters, or use them to mitigate the risk beforehand

## Slide 100

**Thanks for listening Questions?**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Gikamai
Thanks for listening
Questions?
```

## Slide 101

## **References**

- Our <u>repository</u> for all things RPC, including the RPC Visibility script

- RPC tools by other researchers

   - <u>RpcMon</u> by CyberArk

   - <u>RpcInvestigator</u> by TrailOfBits

   - <u>RPC Firewall, requires process injection & hooks</u>

- <u>A Definitive Guide to the RPC filters, by our research team</u>

- Useful readings:

   - Jonathan Johnson of SpecterOps, <u>Utilizing RPC Telemetry</u>

   - Carsten Sandker, <u>Offensive Windows IPC Internals 2: RPC</u>

   - James Forshaw, <u>How to secure a Windows RPC Server, and how not to.</u>
