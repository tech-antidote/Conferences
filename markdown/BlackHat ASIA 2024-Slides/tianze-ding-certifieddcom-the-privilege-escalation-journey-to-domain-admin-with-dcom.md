---
title: "CertifiedDCOM The Privilege Escalation Journey to Domain Admin with DCOM"
speakers: ["Tianze Ding"]
conference: "Black Hat"
conference_full: "Black Hat ASIA 2024"
edition: "ASIA"
year: 2024
source_pdf: "BlackHat ASIA 2024-Slides/Tianze Ding-CertifiedDCOM The Privilege Escalation Journey to Domain Admin with DCOM.pdf"
pages: 51
sha256: "40d7f337621346362bff71cd6fcf4ed948b82328f88989cd82d652dd9ebc2a75"
text_chars: 20669
ocr_pages: 1
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T00:52:02Z"
---
# CertifiedDCOM The Privilege Escalation Journey to Domain Admin with DCOM

**Speakers:** Tianze Ding  
**Conference:** Black Hat ASIA 2024  
**Source:** `BlackHat ASIA 2024-Slides/Tianze Ding-CertifiedDCOM The Privilege Escalation Journey to Domain Admin with DCOM.pdf` (51 pages)


## Slide 1

## CertifiedDCOM The Privilege Escalation Journey to Domain Admin with DCOM

Tianze Ding (@D1iv3) Tencent Security Xuanwu Lab

#BHASIA @BlackHatEvents

## Slide 2

# Whoami

###### **Tianze Ding (@D1iv3)**

- Senior Security Researcher, Tencent Security Xuanwu Lab

- Focusing on Active Directory Security / Cloud Security / Web Security

- 2022 MSRC Most Valuable Researchers

- Black Hat / DEFCON / HITB Speaker

# BHASIA @BlackHatEvents

## Slide 3

# Agenda

- COM/DCOM Basics

- Previous Research

- COM Attack Surface from Local to Remote

- CertifiedDCOM: Privilege Escalation to Domain Admin

- Patches & Mitigations

- Conclusions & Takeaways

# BHASIA @BlackHatEvents

## Slide 4

# What is COM?

- Component Object Model (COM)

- COM is everywhere, OLE, ActiveX, DirectX, Windows Runtime, WMI, etc.

- COM Server

   - DLL/EXE files with one or more COM classes

- COM Object

   - An instance of a COM class which implements one or more interfaces

- COM Interface

   - A set of methods that can be invoked by clients

COM Server
COM Interface
QueryInterface
IUnknown AddRef
Release
Method A
Interface A
Method B
…
COM Object

# BHASIA @BlackHatEvents

## Slide 5

# COM/DCOM

### COM Server

- In-Process Server

Client Process COM Server

   - Runs in the same process of the client

- Out-of-Process Server

   - Runs in a separate process

   - Interact through ALPC

- Remote Server (DCOM)

   - Runs in a remote computer

   - Interact through RPC

Application
COM Object
Code

ALPC/RPC
COM Proxy COM Stub

# BHASIA @BlackHatEvents out-of-process server / remote server

## Slide 6

# Out-of-process COM

Launch and Activation
RPCSS
1. Request COM Object 2. Create new process and
e.g., CoCreateInstance new COM object
3. Register &
4. Activation info
Activation info
Client COM Server
5.Access COM interfaces and methods
through ALPC

**Access**

# BHASIA @BlackHatEvents

## Slide 7

# DCOM

Computer B
Computer A
2. Request COM Object
Port 13
RPCSS RPCSS
1. Request COM Object
3. Launch and Activation
e.g., CoCreateInstance
Dynamic
Client COM Server
Port
4. Access  through RPC

# BHASIA @BlackHatEvents

## Slide 8

# Potato Attacks and Kerberos Relay

Potato attacks and Kerberos Relay abuse COM activation for **LPE**

MS15-076

Local User to SYSTEM **LPE**

Remote attack surface?

Rotten Potato
Juicy Potato
Rogue Potato

Service Account to SYSTEM **LPE**

Remote Potato

Domain User to SYSTEM / Other Local Sessions **LPE**

Kerberos Relay

Local Potato

Local User to SYSTEM **LPE**

The beginning of the story: **CoGetInstanceFromIStorage**

# BHASIA @BlackHatEvents

## Slide 9

# CoGetInstanceFromIStorage

Windows APIs to create COM objects

- CoGetClassObject

- CoCreateInstance(Ex)

- CoCreateInstanceFromApp

- CoGetInstanceFromFile

- **CoGetInstanceFromIStorage**

HRESULT **CoGetInstanceFromIStorage** ( [in, optional] COSERVERINFO *pServerInfo, [in, optional] CLSID *pClsid,

- [in, optional] IUnknown *punkOuter,

- [in] DWORD dwClsCtx,

**[in] IStorage *pstg,**

- [in] DWORD dwCount,

- [in, out] MULTI_QI *pResults

Create a new COM object and **initializes it from a storage object**

- );

The **pstg** parameter is an **interface pointer** to the storage object

# BHASIA @BlackHatEvents

## Slide 10

# COM Marshaling/Unmarshaling

Interface pointers must be marshalled into OBJREF structures in crossing apartment/process/computer communication. **COM Client** GetUnmarshalClass IStorage IMarshal MarshalInterface marshal EvilStroage *pstg OBJREF_CUSTOM **COM Server** unmarshal Create object and get OBJREF_CUSTOM interface pointer

OBJREF_CUSTOM MEOW OBJREF Type IID CLSID cbExtension Data Size Data

# BHASIA @BlackHatEvents

## Slide 11

# COM Marshaling/Unmarshaling

**COM Client**

GetUnmarshalClass PointerMoniker IStorage IMarshal MarshalInterface OBJREF_STANDARD

marshal

EvilStroage *pstg **COM Server**

OBJREF_CUSTOM unmarshal

PointerMoniker::UnmarshalInterface OBJREF_CUSTOM Unmarshal OBJREF_STANDARD

OBJREF_STANDARD MEOW OBJREF Type IID Flags cPublicRefs OXID (Object Explorer ID)

OID IPID

**StringBindings SecurityBindings**

# BHASIA @BlackHatEvents

## Slide 12

# COM Marshaling/Unmarshaling

**StringBinding**

**COM Server**

Unmarshal OBJREF_STANDARD RPCSS ResolveOxid2 Initiate an RPC connection to the address specified in the StringBinding

TowerId NetworkAddress **SecurityBinding** AuthnSvc Reserved Service Principal Name

**SecurityBinding**

# BHASIA @BlackHatEvents

## Slide 13

# CoGetInstanceFromIStorage

Previous research
Attacker’s COM Client • Attacker’s COM client and the victim COM server
CoGetInstanceFromIStorage(…, Clsid, …, EvilStorage, … ) are on the same machine
Launch and Activation • Impersonate / Relay identities of high-privileged
COM Servers for LPE
Unmarshal OBJREF
Impersonate the high-
ResolveOxid2 over RPC privileged user running the
COM server
High-privileged OxidBindings Attacker’s
RPCSS
(StringBindings and SecurityBindings)
COM Server Rogue Server
Relay NTLM / Kerberos
authentication to
A new COM connection to the address in OxidBindings
other services
Both connections require authentication

# BHASIA @BlackHatEvents

## Slide 14

# Remote CoGetInstanceFromIStorage

typedef struct _COSERVERINFO { HRESULT CoGetInstanceFromIStorage( DWORD dwReserved1; [in, optional] COSERVERINFO *pServerInfo, LPWSTR pwszName; **Remote Computer Name** [in, optional] CLSID *pClsid, COAUTHINFO *pAuthInfo; **Remote Auth Info** [in, optional] IUnknown *punkOuter, DWORD dwReserved2; [in] DWORD dwClsCtx, } COSERVERINFO; [in] IStorage *pstg, [in] DWORD dwCount, typedef enum tagCLSCTX { … [in, out] MULTI_QI *pResults CLSCTX_REMOTE_SERVER **Remote Activation** ); … }

CoGetInstanceFromIStorage also supports **remote COM activation**

Can we use CoGetInstanceFromIStorage to coerce **a remote computer** connect to us over RPC/DCOM and exploit it for a NTLM/Kerberos Relay attack ?

# BHASIA @BlackHatEvents

## Slide 15

# Remote CoGetInstanceFromIStorage

- Suppose an attacker has **Domain User / Domain Computer** privileges

- Use CoGetInstanceFromIStorage to activate a COM object on a remote domain computer

###### **Access is Denied**

# BHASIA @BlackHatEvents

## Slide 16

# COM Security

**COM Launch / Activation / Access**

COM Client

System-wide ACL

Process-wide ACL

###### **System-wide Launch and Activation Limits**

- Defined in HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Ole

COM Server

By default, only users in specify high-privileged local groups are allowed

to perform Remote Launch and Remote Activation

# BHASIA @BlackHatEvents

## Slide 17

# Remote Attack Surface?

Low-privileged accounts (e.g., Domain Users, Domain Computers) are not allowed to activate any COM object on a remote computer in Windows default COM security configuration

Where is the remote attack surface ?

# BHASIA @BlackHatEvents

## Slide 18

# Remote Attack Surface in Active Directory

###### **Windows**

- Windows default COM Security configuration

- Preinstalled COM classes in Windows

###### **Active Directory**

- Widely used services in Active Directory

- COM classes introduced by these services

- Special COM security configuration introduced by these services

- 1

- 8

# BHASIA @BlackHatEvents

## Slide 19

# Special COM Security Configuration

RDS (Remote Desktop Service)

• Widely used by enterprise virtual application/desktop solutions, e.g., Citrix, VMware Horizon

RDS Remote Access Servers, RDS Endpoint Servers and RDS Management Servers have Remote Launch and Remote Activation privileges.

In the RDS default configuration, no low-privilege domain accounts in these groups.

# BHASIA @BlackHatEvents

## Slide 20

# Special COM Security Configuration SCCM (System Center Configuration Manager)

SMS Admins group has Remote Launch and Remote Activation privileges. By default, each administrative user in a hierarchy and the site server computer account are members of the SMS Admins group. No low-privilege domain accounts in the SMS Admins group.

# BHASIA @BlackHatEvents

## Slide 21

# Special COM Security Configuration

AD CS (Active Directory Certificate Service)

Certificate Service DCOM Access group has Remote Activation privilege

The Authenticated Users group is in the Certificate Service DCOM Access group

By default , **any domain account can pass the system-wide ACL check** and are allowed to activate COM objects remotely on ADCS

# BHASIA @BlackHatEvents

## Slide 22

# Special COM Security Configuration

AD CS (Active Directory Certificate Service)

Certificate Signing Request (CSR) Protocol

- **MS-WCCE (DCOM)**

- MS-ICPR (MS-RPC)

- HTTP

https://posts.specterops.io/certified-pre-owned-d95910965cd2

The special configuration is for MS-WCCE to allow any domain account to send a CSR to AD CS with DCOM

# BHASIA @BlackHatEvents

## Slide 23

# Find Exploitable COM Classes on ADCS

Process-wide Security

- Process-wide ACL

- Identity

- Authentication Level

- Impersonation Level

- Registry

   - Defined in

HKEY_CLASSES_ROOT\AppID\{AppID_GUID}\

- CoInitializeSecurity API

- COM server can call it explicitly to override the configuration in the registry

# BHASIA @BlackHatEvents

## Slide 24

# Find Exploitable COM Classes on ADCS

Process-wide ACL for Launch / Activation / Access

- Defined in the LaunchPermission and AccessPermission registry values

What kind of exploitable COM do we need?

- COM servers that are already launched

   - Certificate Service DCOM Access group does not have Remote Launch privilege in the ADCS system-wide ACL

- Process-wide ACL allows remote activation by low-privileged domain accounts

# BHASIA @BlackHatEvents

## Slide 25

# Find Exploitable COM Classes on ADCS

Identity

- Defined in the RunAs registry value

- The user identity the COM server runs as

- The Interactive user

- Use the user that is currently logged on to the computer for authentication

The system account

- Use the domain computer account for authentication

- What kind of exploitable COM do we need?

- COM servers with the identity set to any user can perform network authentication except

- Local Service, which use the anonymous user for network authentication

# BHASIA @BlackHatEvents

## Slide 26

# Find Exploitable COM Classes on ADCS

###### Authentication Level

- Defined in the AuthenticationLevel registry value

- The default value is RPC_C_AUTHN_LEVEL_CONNECT, which means no signing and sealing in DCOM connections

Impersonation Level

- The default value is RPC_C_IMP_LEVEL_IDENTIFY, which means the server cannot impersonate the client

What kind of exploitable COM do we need?

Target of Relay Attack Authentication Level Impersonation Level LDAP/LDAPS RPC_C_AUTHN_LEVEL_CONNECT >= RPC_C_IMP_LEVEL_IDENTIFY SMB >= RPC_C_AUTHN_LEVEL_CONNECT RPC_C_IMP_LEVEL_IMPERSONATE ADCS HTTP(S) >= RPC_C_AUTHN_LEVEL_CONNECT RPC_C_IMP_LEVEL_IMPERSONATE ADCS MS-ICPR >= RPC_C_AUTHN_LEVEL_CONNECT RPC_C_IMP_LEVEL_IMPERSONATE

# BHASIA @BlackHatEvents

## Slide 27

# Exploitable COM Classes on ADCS

Exploitable COM classes on ADCS

|Name|CLSID|Identity|Authentication Level|Impersonation Level|
|---|---|---|---|---|
|CertSrv Request|d99e6e74-fc88-11d0-b498-00a0c90312f3|SYSTEM|CONNECT|IDENTIFY|
|CertSrv Admin|d99e6e73-fc88-11d0-b498-00a0c90312f3|SYSTEM|CONNECT|IDENTIFY|
|OCSPRequestD|3ab092c4-de6a-4dc4-be9e-fdacbb05759c|SYSTEM|CONNECT|IDENTIFY|
|OCSPAdminD|6d5ad135-1730-4f19-a4eb-3f78e7c976bb|SYSTEM|CONNECT|IDENTIFY|

CertSrv Request and CertSrv Admin

• installed in ADCS by default for MS-WCCE Use the ADCS$ computer account for network authentication OCSPRequestD and OCSPAdminD

Relay ADCS$’s authentication messages to LDAP(S)

- introduced by the ADCS Online Responder role

# BHASIA @BlackHatEvents

## Slide 28

# NTLM Relay / Remote Kerberos Relay

Attacker

Remote CoGetInstanceFromIStorage

ADCS

An attacker can use CoGetInstanceFromIStorage to activate an exploitable COM object on ADCS remotely

ResolveOxid2 over MS-RPC

OxidBindings

OxidBindings

DCOM with ADCS$’s NTLM / Kerberos authentication messages

SecurityBinding

- AuthnSvc can be set to NTLM / Kerberos

- PrincName can be set to any SPN

# BHASIA @BlackHatEvents

## Slide 29

# NTLM Relay / Remote Kerberos Relay

Attacker

ADCS

Domain Controller

DCOM with ADCS$’s NTLM / Kerberos authentication messages Relaying NTLM / Kerberos to LDAP(S)

RBCD / ShadowCredentails attack

The authentication in this DCOM connection will adhere to the process-wide security configurations of the exploitable COM

The attacker can then relay ADCS$’s authentication messages to LDAP(S) to perform RBCD / ShadowCredentials attack

# BHASIA @BlackHatEvents

## Slide 30

# NTLM Relay / Remote Kerberos Relay

Attacker Remote CoGetInstanceFromIStorage

ADCS

Domain Controller

ResolveOxid2 over MS-RPC

OxidBindings DCOM with ADCS$’s NTLM / Kerberos authentication messages Relaying NTLM / Kerberos to LDAP(S)

RBCD / ShadowCredentails attack

# BHASIA @BlackHatEvents

## Slide 31

# Privilege Escalation to Domain Admin

##### Attack Path #1

- Use S4U2Self/S4U2Proxy to request a domain admin’s ST to access the ADCS

- • RCE on the ADCS with PSEXEC, WMIEXEC, WINRM … to dump the private key

- Escalate to Domain Admin with the Golden Certificate attack

##### Attack Path #2

- Use S4U2Self/S4U2Proxy to request a domain admin’s ST to access the ADCS

- • Use the domain admin‘s ST to request a certificate with MS-WCCE/MS-ICPR/…

- Use the domain admin’s certificate to request a TGT with PKINIT

- Escalate to Domain Admin with the TGT

# BHASIA @BlackHatEvents

## Slide 32

# Demo

<u>https://youtu.be/OHwjeGUSM4w</u>

# BHASIA @BlackHatEvents

## Slide 33

# Patch and Mitigation

**Patch - CVE-2022-37976**

- Released on October 11, 2022

- The patch raised the authentication level to RPC_C_AUTHN_LEVEL_PKT_PRIVACY in the Certificate Service.

**DCOM Authentication Hardening**

- Released on November 8, 2022

- The update automatically raised authentication level for all non-anonymous activation requests from DCOM clients to RPC_C_AUTHN_LEVEL_PKT_INTEGRITY if it's below Packet Integrity.

**Enable Protection for Relay Attacks**

- LDAP Signing and Channel Binding

# BHASIA @BlackHatEvents

## Slide 34

# Can We Relay to Other Services?

- Relaying to ADCS HTTP(S) / SMB / MS-ICPR requires the impersonation level of authentication set to RPC_C_IMP_LEVEL_IMPERSONATE

- No remotely activatable COM class on ADCS satisfies this requirement

Attacker ADCS
Remote CoGetInstanceFromIStorage
ResolveOxid2 over MS-RPC

- Can we relay the authentication in the ResolveOxid2 RPC connection?

# BHASIA @BlackHatEvents

## Slide 35

# Can We Relay to Other Services?

###### rpcss.dll!ResolveClientOXID

The impersonation level of the ResolveOxid2 RPC authentication is RPC_C_IMP_LEVEL_IMPERSONATE **NTLM Relay**

- We can relay ADCS$’s NTLM authentication messages in the ResolveOxid2 RPC to

- another ADCS Server‘s HTTP / MS-ICPR (without IF_ENFORCEENCRYPTICERTREQUEST flag)

- Requires two ADCS server in the domain, because we can’t relay NTLM back to the same machine

# BHASIA @BlackHatEvents

## Slide 36

# Kerberos Relay ?

**SecurityBinding**

###### rpcss.dll!ResolveClientOXID

AuthnSvc Reserved

Service Principal Name

Can we set arbitrary SPN in the forged OBJREF’s SecurityBinding?

The SPN in the ResolveOxid2 RPC authentication is forced to **RPCSS/MachineNameFromStringBinding**

**Kerberos Relay**

- Unable to trigger Kerberos Relay with the SecurityBinding

# BHASIA @BlackHatEvents

## Slide 37

|**Tower Id**|**RPC Transport**|
|---|---|
|0x04|ncacn_dnet_nsp|
|0x07|ncacn_ip_tcp|
|0x08|ncadg_ip_udp|
|0x09|ncacn_nb_tcp|
|0x0C|ncacn_spx|
|0x0D|ncacn_nb_ipx|
|0x0E|ncadg_ipx|
|0x0F|ncacn_np|
|0x10|ncalrpc|
|0x13|ncacn_nb_nb|
|0x16|ncacn_at_dsp|
|0x17|ncadg_at_ddp|
|0x1A|ncacn_vns_spp|
|0x1D|ncadg_mq|
|0x1F|ncacn_http|
|0x21|# BHASIA @BlackHatEvents
ncacn_hvsocket|

# RPC Protocol Sequence

###### **StringBinding**

TowerId NetworkAddress

RPC sequence type

- identifies the protocol to be used in RPC calls

TCP, UDP, SMB, NetBIOS, HTTP, MQ …

Can these protocols be abused for NTLM/Kerberos Relay?

## Slide 38

# RPC Protocol Sequence

ADCS

Attacker ADCS
Remote CoGetInstanceFromIStorage
RPC
• ncacn_ip_tcp
ResolveOxid2 over MS-RPC
• ncacn_http
OxidBindings
• ncacn_ip_tcp
DCOM Connection
• ncacn_http
• ncacn_np

# BHASIA @BlackHatEvents

## Slide 39

# RPC over HTTP (ncacn_http)

- Support both RPC over HTTP v1 and RPC over HTTP v2

- Use the RPC over HTTP v2 first; if that fails, the client will fall back to the RPC over HTTP v1

###### Authentication messages in the RPC packet

Client

No auth in HTTP layer

Raw RPC Packet

HTTP RPC_CONNET

HTTP/1.1 200 OK

RPC bind

RPC bind_ack

...

Server

**RPC over HTTP v1**

# BHASIA @BlackHatEvents

## Slide 40

# RPC over HTTP (ncacn_http)

**RPC over HTTP v2**

client server clientRPC server
RPC
HTTP RPC_OUT_DATA
HTTP RPC_IN_DATA
No auth in HTTP layer
HTTP/1.1 200 Success HTTP/1.1 200 Success
RPC RTS Packet
RPC RTS Packet
Raw RPC Packet
RPC bind
RPC bind_ack
...
...
RPC over HTTP v2: RPC_IN_DATA
RPC over HTTP v2: RPC_OUT_DATA
Authentication messages in RPC packets

# BHASIA @BlackHatEvents

## Slide 41

# RPC over HTTP (ncacn_http)

**RPC over HTTP (ncacn_http)**

- No authentication in the HTTP layer

- The RPC authentication in **ncacn_http** works the same as it is in **ncacn_ip_tcp**

- RPC

### **NTLM Relay / Kerberos Relay**

- We can perform NTLM Relay / Kerberos Relay with RPC packets in HTTP connections the same as RPC over ncacn_ip_tcp

- RPC over HTTP traffic may bypass some network restrictions or NDR devices

# BHASIA @BlackHatEvents

## Slide 42

# RPC over Named Pipe (ncacn_np)

- The DCOM connection also support RPC over Named Pipe (ncacn_np)

- The ncacn_np uses the identity of RPCSS (NETWORK SERVICE) for network authentication in the SMB layer

- RPC

The ADCS machine account

# BHASIA @BlackHatEvents

## Slide 43

# RPC over Named Pipe (ncacn_np)

The impersonation level of the authentication is <u>SECURITY_IMPERSONATION, which</u> means the client can be impersonated by the server.

- **NTLM Relay** RPC

- RPC

- • We can relay ADCS$’s NTLM authentication messages in the SMB to another ADCS Server‘s HTTP / MS-ICPR (without IF_ENFORCEENCRYPTICERTREQUEST flag)

- Requires two ADCS server in the domain

**Kerberos Relay**

- The SPN in the authentication is forced to be **CIFS/MachineNameFromStringBinding**

- Unable to trigger Kerberos Relay

# BHASIA @BlackHatEvents

## Slide 44

# CVE-2022-37976 Patch Analysis

certsrv.exe before patch

certsrv.exe after patch

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pisek hat
ASIA 2024
primary “secondary
aAoaAaAnAaAaATAAaAR
900000014000F 18E *InitializeComSecurity@OVAJXZ
bUBUUUY T46bEF 19S mov edi, eax
668008014068F195 test eax, eax
6686680014868F 197 jz 6x14666F1B4
SSE 2°" Tegt est] == af Cee eee
i
i
:
i
A
Hh
5
t
i
i
i
i
i
i
certsrv.exe before patch certsrv.exe after patch
```

## Slide 45

# CVE-2022-37976 Patch Analysis

MainWndProc

- InitializeComSecurity

- • CoInitializeSecurity

This function is introduced by the patch

Impersonation Level is set to **RPC_C_IMP_LEVEL_IMPERSONATE** Authentication Level is set to RPC_C_AUTHN_LEVEL_PKT_PRIVACY

# BHASIA @BlackHatEvents

## Slide 46

# Kerberos Reflection

The patch for CVE-2022-37976 changed the impersonation level of the Certificate Service (CertSrv Request and CertSrv Admin) to **RPC_C_IMP_LEVEL_IMPERSONATE**

**NTLM Relay**

With the patch, we can relay DCOM to ADCS HTTP / MS-ICPR running on a different machine

###### **Kerberos Reflection**

Kerberos Reflection is not restricted, we can **relay Kerberos back to the same ADCS server**

# BHASIA @BlackHatEvents

## Slide 47

# Kerberos Reflection

Attacker ADCS
Remote CoGetInstanceFromIStorage with the CertSrv Request COM
ResolveOxid2 over MS-RPC
ncacn_ip_tcp
StringBinding : attacker’s machine
or
OxidBindings
SecurityBinding : http/adcs.domain.local
ncacn_http
DCOM with ADCS$’s Kerberos AP-REQ messages
Relaying Kerberos AP-REQ to ADCS HTTP
Request a certificate of ADCS$

# BHASIA @BlackHatEvents

## Slide 48

# Mitigations

#### ADCS HTTP Endpoints

- Follow <u>Microsoft‘s guide to enable EPA (Extended Protection for Authentication) on</u> your ADCS HTTP endpoints

- EPA can protect your ADCS HTTP endpoints from both NTLM Relay and Kerberos Relay

#### MS-ICPR

- Keep the default settings of the MS-ICPR, don't remove the IF_ENFORCEENCRYPTICER

- TREQUEST flag

# BHASIA @BlackHatEvents

## Slide 49

# Black Hat Sounds Bytes

#### CertifiedDCOM

- A remote attack surface of DCOM and AD CS

- Privilege escalation from Domain Users to Domain Admin

- Take Kerberos Relay to the next level, make it a remote attack vector

- Attacks may also work against customized DCOM with misconfigurations

- Mitigations

- Update your AD CS to install the patch for CVE-2022-37976

- Update all your machines to enable DCOM Authentication Hardening

- Enable LDAP Signing and Channel Binding & Enable EPA for ADCS HTTP

- Check your customized system-wide and process-wide COM security configurations

# BHASIA @BlackHatEvents

## Slide 50

# Acknowledgments

Standing on the shoulders of giants !

- James Forshaw (@tiraniddo)

- Andrea Pierini (@decoder_it)

- Antonio Cocomazzi (@splinter_code)

- • @cube0x0

# BHASIA @BlackHatEvents

## Slide 51

# Thank You !

Tianze Ding (@D1iv3) Tencent Security Xuanwu Lab

#BHASIA @BlackHatEvents
