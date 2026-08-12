---
title: "Turning your Active Directory into the attacker’s C2 modern Group Policy Objects enumeration and exploitation"
speakers: ["Quentin Roland Wilfried Bécard"]
conference: "DEF CON"
conference_full: "DEF CON 33"
edition: "33"
year: 2025
source_pdf: "DEF CON 33/Quentin Roland Wilfried Bécard - Turning your Active Directory into the attacker’s C2 modern Group Policy Objects enumeration and exploitation.pdf"
pages: 59
sha256: "2399dcd9ef962fb0bbb1f1cb7711ad947b9d293938b66bbf235f2c95dc662d0c"
text_chars: 23850
ocr_pages: 4
has_ocr: true
redacted_secrets: 0
ocr_confidence: 88.4
ocr_unreliable_blocks: 1
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T07:11:42Z"
---
# Turning your Active Directory into the attacker’s C2 modern Group Policy Objects enumeration and exploitation

**Speakers:** Quentin Roland Wilfried Bécard  
**Conference:** DEF CON 33  
**Source:** `DEF CON 33/Quentin Roland Wilfried Bécard - Turning your Active Directory into the attacker’s C2 modern Group Policy Objects enumeration and exploitation.pdf` (59 pages)


## Slide 1

# **Turning your Active Directory into the attacker’s C2**

**Modern Group Policy Objects enumeration and exploitation**

**DEFCON 33 2025/08/10**

## Slide 2

# **<u>Whoami.exe</u>**

**Quentin Roland** Pentester & Red Teamer

**Wilfried Bécard** Red Teamer

**2**

## Slide 3

# **<u>Introduction</u>**

**3**

## Slide 4

# **<u>Introduction</u>**

Group Policy Objects: the (powerful) ugly ducklings of Active Directory exploitation

_"Well yeah, we have an account that can modify a GPO applying to Domain Controllers. But let us check the ADCS first..."_

- _Proceed to exploit an ESC4 and get detected *_

- _Anonymous colleagues, 2025_

**4**

## Slide 5

# **<u>Introduction</u>**

Group Policy Objects: the (powerful) ugly ducklings of Active Directory exploitation

- GPO attack vectors may just be the **`ugly ducklings`** of AD exploitation:

   - Obscure?

   -

Risky?

   - Scarce tooling?

- Which is a shame, since:

   -

   - Well-equipped attackers may not have such concerns

- GPOs exploitation leverages the powerful native C2 capabilities of Active Directory

**5**

## Slide 6

# **<u>Introduction</u>**

##### Table of contents

1. Group Policy Objects implementation 101

2. Leveraging Group Policy Objects for enumeration ( `gpoParser.py` )

3. Abusing Group Policy Objects ACLs ( `GroupPolicyBackdoor.py` )

4. Compromising Group Policy Objects via NTLM relaying ( `GPOddity.py` )

5. Exploiting protected Organizational Units via GPO link poisoning ( `OUned.py` )

**6**

## Slide 7

# **<u>Group Policy Objects implementation 101</u>**

**7**

## Slide 8

**<u>Group Policy Objects implementation 101</u>** Group Policy Objects basics

- A GPO is a collection of configurations applied periodically to AD objects

- It is a core feature in Active Directory for device and identity management

- A GPO can define:

   -

   - **`User`** configurations (applied by user objects)

- **`Computer`** configurations (applied by computer objects)

**8**

## Slide 9

**<u>Group Policy Objects implementation 101</u>** Linking GPOs to Organizational Units

- GPOs are not directly applied to users or computers, but rather to **`Organizational Units`**

- Can also apply to different objects such as **`Sites`** or **`Domains`** but this is less common

- By default, GPOs will be inherited from the parent container

**9**

## Slide 10

**<u>Group Policy Objects implementation 101</u>** Group Policy Container and Group Policy Template

- The implementation of GPOs in Active Directory is a bit peculiar

- GPOs are made up of two components:

- The **`Group Policy Container`** (GPC) - **LDAP object** ■ GPO metadata: name, description, version, etc.

- The **`Group Policy Template`** (GPT) - **SMB share** ■ GPO files: describe the configurations to be applied by clients.

**10**

## Slide 11

**<u>Group Policy Objects implementation 101</u>** Group Policy Container and Group Policy Template

**11**


> Recovered by OCR — confidence 87/100 on the text kept, 84/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Group Policy Objects implementation 101
Group Policy Container and Group Policy Template
GPC (LDAP object)
CN={ 78BAF44B-B8 90-4812-AEB8-C11AC2B29FD2},CN=Policies, CN=System, DC=corp, DC=com
Group Policy Object
78BAF44B-B890-4812-AEB8-C11AC2B29FD2
GPT (SMB share)
\\dc.corp.com\SysVol\corp.com\Policies\ {78BAF44B-B8 90-4812-AEB8-C11AC2B29FD2}
11
```

## Slide 12

**<u>Group Policy Objects implementation 101</u>** LDAP attributes

- Noteworthy LDAP attributes:

   -

- On GPC objects:

   - `gPCFileSysPath` ― the UNC path to the GPT (generally the SYSVOL share)

   -

      - `flags` ― status of user / computer configuration (enabled vs disabled)

   - `gPCMachineExtensionNames` / `gPCUserExtensionNames` ― a list of GUID pairs describing

   - which configuration the GPO defines for machines and users

- On OU objects:

   - `gPLink` ― whether a GPO is linked / enforced or not

   - `gPOptions` ― whether inheritance is enabled or not

**12**

## Slide 13

**<u>Group Policy Objects implementation 101</u>** Group Policy Template

- **Policies defined across several files**

   - `Groups.xml`

   - `Registry.xml`

   - `GptTmpl.inf`

> ■ And many more

\```
# cat corp.com/Policies/{78BAF44B-B890-4812-AEB8-C11AC2B29FD2}/
Machine/Microsoft/Windows NT/SecEdit/GptTmpl.inf
\```

\```
[Unicode]
Unicode=yes
\```

\```
[Version]
signature="$CHICAGO$"
Revision=1
\```

\```
[Group Membership]
*S-1-5-32-544__Memberof =
*S-1-5-32-544__Members = *S-1-5-21-361363594-1987475875-3919384990-1109
\```

\```
# cat corp.com/Policies/{78BAF44B-B890-4812-AEB8-C11AC2B29FD2}/Machine/Preferences/Groups/Groups.xml
<?xml version="1.0" encoding="utf-8"?>
[...]
\```

\```
groupSid="S-1-5-32-555" groupName="Remote Desktop Users (built-in)"><Members><Member name="CORP\jack" action="ADD"
sid="S-1-5-21-361363594-1987475875-3919384990-1252"/></Members></Properties></Group>
</Groups>
\```

**13**

## Slide 14

**<u>Group Policy Objects implementation 101</u>** Organizational Units attributes ― Inheritance

■ With inheritance

- **`$ ldeep ldap -u bob -p password -d corp \ -s 192.168.57.5 object -v 'workstations'`** `[...]`

- **`"gPOptions": 0,`**

- Without inheritance ( **`gPOptions`** == `1` )

   - **`$ ldeep ldap -u bob -p password -d corp \ -s 192.168.57.5 object -v 'workstations'`** `[...]`

   - **`"gPOptions": 1,`**

**14**

## Slide 15

**<u>Group Policy Objects implementation 101</u>** Organizational Units attributes ― Link

■

**GPOs are linked to OUs through the gPLink attribute (list of GPO DNs)**

■ Integer at the end of the **`gPLink`** attribute describes the link status

■ Enforced GPOs will ignore the inheritance status and will always apply to child containers

- **`$ ldeep ldap -u bob -p password -d corp -s 192.168.57.5 object -v 'workstations'`** `[...]`

- `"dn": "OU=WORKSTATIONS,DC=CORP,DC=COM",`

- `"gPLink": "[LDAP://cn=` **`{78BAF44B-B890-4812-AEB8-C11AC2B29FD2}`** `,` `cn=policies,cn=system,DC=CORP,DC=COM;` **`0`** `]`

- `[LDAP://cn` `=` **`{01F34D14-C761-47F9-A0CF-C7A7F57999A5}`** `,cn=policies,cn=system,DC=CORP,DC=COM;` **`1`** `] [LDAP://cn` `=` **`{C91C6B48-2D8B-4830-B0CB-B0B6D2FBB0A5}`** `,cn=policies,cn=system,DC=CORP,DC=COM;` **`2`** `]",`

**15**

## Slide 16

**<u>Group Policy Objects implementation 101</u>** Organizational Units attributes ― Link

|**Integer value**|**Link enabled**|**Enforced**|**Meaning**|
|---|---|---|---|
|**0**|**Yes**|**No**|GPO is linked and**processed**normally|
|**1**|**No**|**No**|GPO is unlinked (disabled),**not processed**|
|**2**|**Yes**|**Yes**|GPO is linked and**enforced**|
|**3**|**No**|**Yes**|GPO is enforced but link is disabled,**not processed**|

**16**

## Slide 17

**<u>Group Policy Objects implementation 101</u>** Group Policies attributes ― Status

■ Status determines which configurations will be applied

■ Enabled (all) ■ Only computer config ■ Only user config ■ Everything disabled

**17**

## Slide 18

**<u>Group Policy Objects implementation 101</u>** Group Policies attributes ― Status

- Status is defined by the value of the **`flags`** attribute

- **`$ ldeep ldap -u bob -p password -d corp -s 192.168.57.5 object -v '{474D47E2-2B77-4E37-9744-A3CF6AB04449}'`** `[...]`

- `"cn": "{78BAF44B-B890-4812-AEB8-C11AC2B29FD2}",`

- `"displayName": "Workstation admins",`

- `"distinguishedName": "CN={78BAF44B-B890-4812-AEB8-C11AC2B29FD2},CN=Policies,CN=System,DC=CORP,DC=COM",` **`"flags": 1,`**

**18**

## Slide 19

**<u>Group Policy Objects implementation 101</u>** Group Policies attributes ― Status

|**Integer value**|**User configuration**|**Computer configuration**|**Meaning**|
|---|---|---|---|
|**0**|**Enabled**|**Enabled**|**Both**user and computer settings are**applied**|
|**1**|**Disabled**|**Enabled**|Only**computer**settings are applied|
|**2**|**Enabled**|**Disabled**|Only**user**settings are applied|
|**3**|**Disabled**|**Disabled**|**Both**settings are**disabled**(GPO has no effect)|

**19**

## Slide 20

**<u>Group Policy Objects implementation 101</u>** Group Policies Application / Refresh interval

- **Default policy refresh**

   - Background update every **90 minutes**

      - Random offset of **0 to 30 minutes**

   -

   - This setting can be changed

-

- **Not all policies processed**

      - Software installation only when a computer starts and when a user logs on

**20**

## Slide 21

# **<u>Group Policy Objects implementation 101</u>**

GPO application overview

**21**


> Recovered by OCR — confidence 90/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
GPO application overview
Computer in OU
CN=Servers, DC=corp, DC=com
x
Domain Controller
1. Query gPLink for object OU
> CN=Servers, DC=corp, DC=com
LDAP ay
< > gPLink
1. Get list of GPC DNs > gPOptions
2. Query GPCs linked to OU
5 LDAP > CN={78[...]},CN=policies, CN=system, DC=corp, DC=com
< > gPCFileSysPath
2. Gets GPT location and target configurations | > flags
> gPCMachineExtensionNames
3. For each configuration, query file from GPT
~
SMB id \\dc.corp.com\SysVol\corp.com\Policies\{78[...]
3. Apply GPO configuration
21
```

## Slide 22

# **<u>Leveraging Group Policy objects for enumeration</u>** Stealthy, detailed and targeted Active Directory reconnaissance using gpoParser.py

**22**

## Slide 23

**<u>Leveraging Group Policy objects for enumeration</u>** Offensive perspective

- **GPO enumeration**

   - Reveals valuable insights into the security posture of a system

   -

- Most interesting configurations:

      - Group memberships or additions

   -

   - Privilege assignments

   -

   - Registry modifications

- Scheduled tasks

**23**

## Slide 24

**<u>Leveraging Group Policy objects for enumeration</u>** Group memberships

■ **Group memberships frequently defined through GPOs**

-

   - Information that can prove crucial for lateral movement

- Preferable to noisy wide-range scans (eg `netexec 10.0.0.0/8` )

-

- Gives better understanding of group assignments and targets definition

**24**

## Slide 25

**<u>Leveraging Group Policy objects for enumeration</u>** Group memberships ― Example

- **`$ ldeep ldap -u bob -p password -d corp -s 192.168.57.5 gpo`** **`{008B0634-C0B9-443A-A06A-E2BAD875E27F}: Allow RDP`**

\```
{B2510EC3-8C2D-41DE-A70B-69E8FD8276B2}: Firewall - dev
\```

\```
{01F34D14-C761-47F9-A0CF-C7A7F57999A5}: Intune Auto Enrollment
\```

\```
{C91C6B48-2D8B-4830-B0CB-B0B6D2FBB0A5}: WSUS
\```

\```
{185ABAA4-75CA-4702-9027-877B89057E17}: Citrix access
\```

\```
{570CD979-1B09-4E25-A16E-CC382F65F310}: Admin - Hardening
\```

\```
{474D47E2-2B77-4E37-9744-A3CF6AB04449}: Workstation admins
\```

\```
{6AC1786C-016F-11D2-945F-00C04fB984F9}: Default Domain Controllers Policy
\```

\```
{31B2F340-016D-11D2-945F-00C04FB984F9}: Default Domain Policy
\```

- **`$ cat CORP.COM/Policies/`** **`{008B0634-C0B9-443A-A06A-E2BAD875E27F}`** **`/Machine/Preferences/Groups/Groups.xml`** `<Groups clsid="{3125E937-EB16-4b4c-9934-544FC6D24D26}">`

\```
  <Group clsid="{6D4A79E4-529C-4481-ABD0-F5BD7EA93BA7}"name="Remote Desktop Users (built-in)" image="2"
\```

\```
  changed="2025-06-26 12:18:45" uid="{F2EFF8C4-CC57-4FD8-A06D-2C0490E16277}">
\```

\```
    <Properties action="U" newName="" description="" deleteAllUsers="0" deleteAllGroups="0"
\```

\```
    removeAccounts="0" groupSid="S-1-5-32-555" groupName="Remote Desktop Users (built-in)">
\```

\```
      <Members>
\```

\```
        <Member name="CORP\Domain Users" action="ADD" sid="S-1-5-21-691320112-1392913536-3019603446-513"/>
\```

\```
      </Members>
\```

\```
    </Properties>
\```

\```
  </Group>
\```

\```
</Groups>
\```

**25**

## Slide 26

**<u>Leveraging Group Policy objects for enumeration</u>** Group memberships ― Example

\```
$ ldeep ldap -u bob -p password -d corp -s 192.168.57.5 ou
[...]
OU=WORKSTATIONS,DC=CORP,DC=COM
  [gPLink]:
* Allow RDP
\```

\```
$ ldeep ldap -u bob -p password -d corp -s 192.168.57.5 \
-b 'OU=WORKSTATIONS,DC=CORP,DC=COM' computers
WKS01.CORP.COM
\```

**26**

## Slide 27

**<u>Leveraging Group Policy objects for enumeration</u>** Privilege assignments

■ **Interesting privileges can be assigned through GPO** ■ Relatively uncommon

**27**

## Slide 28

**<u>Leveraging Group Policy objects for enumeration</u>** Privilege assignments ― Real life examples

- **But it happens!**

■

   - **`SeTcbPrivilege`** to any user on machines affected by this GPO

-

Free privilege escalation

- **`$ cat "Policies/{5F400B8A-5F8D-475E-AC3A-5A1C5A7AAF0B}/Machine/microsoft/windows nt/SecEdit/GptTmpl.inf"`** `[Unicode] Unicode=yes`

- `[Version]`

- `signature="$CHICAGO$" Revision=1`

- `[Privilege Rights]` **`SeTcbPrivilege = *S-1-5-32-545`**

**28**

## Slide 29

**<u>Leveraging Group Policy objects for enumeration</u>** Privilege assignments ― Real life examples

- **Connection restrictions can be enforced**

   - Reduces the risk of credential exposure for privileged accounts

   - ■ Mitigates privilege escalation and upholds the tiering model

**29**

## Slide 30

## **<u>Leveraging Group Policy objects for enumeration</u>**

Registry modifications ― Real life examples

###### ■ **Registry modifications**

- Provides valuable insights into system hardening measures

-

   - Legacy name resolution protocols (LLMNR, NBNS, mDNS) often disabled through GPO

- Eases reconnaissance / helps to determine the feasibility of related attacks

\```
# cat /corp.com/policies/{31B2F340-016D-11D2-945F-00C04FB984F9}/MACHINE/Preferences/Registry/Registry.xml
<?xml version="1.0" encoding="utf-8"?>
\```

\```
<RegistrySettings clsid="{A3CCFC41-DFDB-43a5-8D26-0FE8B954DA51}">
\```

\```
  <Registry clsid="{9CD4B2F4-923D-47f5-A062-E897DD1DAD50}" name="EnableMDNS" status="EnableMDNS" image="12"
  changed="2025-06-26 13:03:46" uid="{0BEC7FF0-5903-4167-BFE5-957A59C00DDA}">
    <Properties action="U" displayDecimal="1" default="0"
    hive="HKEY_LOCAL_MACHINE"
\```

\```
key="SYSTEM\CurrentControlSet\Services\Dnscache\Parameters" name="EnableMDNS" type="REG_DWORD" value="00000000"/>
  </Registry>
\```

\```
</RegistrySettings>
\```

**30**

## Slide 31

**<u>Leveraging Group Policy objects for enumeration</u>** Registry modifications ― Real life examples

■ **More information can be gathered**

■ Hardening (LDAP / SMB signature, RunAsPPL, CredGuards) ■ Additional software installation (EDRs)

**31**

## Slide 32

**<u>Leveraging Group Policy objects for enumeration</u>** Enumeration automation with gpoParser.py

- **GPO enumeration can be time-consuming and complex**

   - Check for inheritance

   - Check for enforced links

   - Check for computer / user configuration state (enabled vs disabled)

- **Automation is the key!**

**32**

## Slide 33

## **<u>Leveraging Group Policy objects for enumeration</u>** Enumeration ― BloodHound limitations

**33**


> Recovered by OCR — confidence 85/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Leveraging Group Policy objects for enumeration
Enumeration — BloodHound limitations
si Default Domain Policy
Bi Citrix Servers
=] Allow ROP
DEVELOPERS
1p Policy Objects
.dmin - Hardening
© Allow RDP
Default Domain Policy
J Developers debug
J Firewall - dev
Intune Auto Enrollment
Unassgined GPO
Werkstation admins
WSUS
Allow RDP
Scope Details Settings Delegation
Control Panel Settings:
Local Users and Groups:
Group (Name: Remote Desktop Users (built in))
Remote Desktop Users (built-in) (Order: 1)
PS C:\> gpupdate /force ; net localgroup
Updating policy...
Computer Policy update has completed successfully.
User Policy update has completed successfully.
Alias name
Local Group
Action Update
Properties
Group name Remote Desktop Users bul)
Delete all member users
Delete all member groups
‘Add members
Disabled
Disabled
Common
Stop processing tems on this extension f an enor occurs on this tem
No
MemberOf
DOMAIN USERS@CORP.LOCAL
CanRDP
Remote Desktop Users
WKS01.CORP.LOCAL
33
```

## Slide 34

## **<u>Leveraging Group Policy objects for enumeration</u>**

Enumeration automation with gpoParser.py

- **Introducing** **`gpoParser.py`**

   - Parses all GPO configuration parameters

   -

   - Reveals misconfigurations and privilege relationships

-

      - Supports both online (live AD) and offline (tool-assisted) analysis

   - Enriches BloodHound with useful edges:

         - **`AdminTo`**

         - **`CanRDP`**

         - **`CanPSRemote`**

- https://github.com/synacktiv/gpoParser

**34**

## Slide 35

**<u>Leveraging Group Policy objects for enumeration</u>** Enumeration automation with gpoParser.py

### **`Demonstration`**

**35**

## Slide 36

**<u>Abusing Group Policy Objects ACLs</u>** Turning Active Directory into your personal C2

**36**

## Slide 37

**<u>Abusing Group Policy Objects ACLs</u>** Exploitation context

- Situation in which a controlled account has **`write privileges`** over a GPO

- Not an uncommon situation (T1 accounts, administration mistakes etc.)

- Possibility to:

   - Compromise **`all objects in linked OUs`** (including sub-OUs)

   - But also any user connecting to a machine of an affected OU

**37**

## Slide 38

# **<u>Abusing Group Policy Objects ACLs</u>**

GPO attack vectors

- Leverage **`built-in GPO features`** to deploy malicious configurations:

   - Scheduled tasks

   - Immediate tasks

   - Adding users to local groups

   -

   - Transferring and executing arbitrary files

-

   - Setting registry keys (disabling self-relay protections ?)

-

   - Logon/Logoff scripts

-

   - **And many more**

- Imagination is the only limit when it comes to GPO attack vectors

**38**

## Slide 39

**<u>Abusing Group Policy Objects ACLs</u>** Existing tools and limitations

- Current offensive tooling for GPO ACLs exploitation:

   - `SharpGPOAbuse` (.NET)

   - `pyGPOAbuse` (python, impacket)

   -

      - `GPOwned` (python)

   - `DRSAT` (GPMC GUI)

- Limitations: **stability and exploit safety** , **cleanup and revert capabilities** , GPO creation, links management, item-level targeting, **available actions and options**

**39**

## Slide 40

# **<u>Abusing Group Policy Objects ACLs</u>**

Introducing GroupPolicyBackdoor.py

- Introducing **`GroupPolicyBackdoor.py`** :

   - Python implementation using `ldap3` and `smbprotocol`

   -

   - GPO creation, deletion & backup

-

   - Links management

-

   - Injection of customizable configurations

-

   - Only applies configurations to specific clients with item-level targeting

-

      - GPO cleanup capabilities

   - Reverse performed actions on clients

- https://github.com/synacktiv/GroupPolicyBackdoor

**40**

## Slide 41

**<u>Abusing Group Policy Objects ACLs</u>** Exploitation example and demonstration

- Account compromised with write privileges over a GPO applying to **a jump server used by domain administrators**

- No network access to these jump servers

- GPO exploitation steps:

   - Add a Scheduled Task on the jump server

   - Configure the Scheduled Task to run in the context of a high-privileges user

- Configure the Scheduled Task to add an account to the Domain Admins group

- ■ GPO does not apply directly to a domain admin, but used to **trap the jump server**

**41**

## Slide 42

**<u>Abusing Group Policy Objects ACLs</u>** Exploitation example and demonstration

### **`Demonstration`**

**42**

## Slide 43

**<u>Abusing Group Policy Objects ACLs</u>** More exploitation scenarios

- More exploitation scenarios encountered during missions:

   - **Reach network-isolated workstations** by deploying an implant via GPO file transfer

   - **Enable WinRM and add a firewall exception** through GPO to pivot to a sensitive server

   - **Persist** in the Active Directory environment after detection by poisoning a GPO

- `GroupPolicyBackdoor.py` can be extended for your use cases

**43**

## Slide 44

# **<u>Compromising Group Policy Objects via NTLM</u> relaying** Advanced GPO exploitation part 1

**44**

## Slide 45

**<u>Compromising Group Policy Objects via NTLM relaying</u>** Exploitation context

- Active Directory environment vulnerable to NTLM relaying to the LDAP service

- User with write privileges over an interesting GPO relayed to LDAP

- Context in which it is **`possible to modify the GPC`** (LDAP), but **`no privileges over the GPT`** (SMB)

- No direct control over the GPO configuration files

- Is this exploitable ?

**45**

## Slide 46

**<u>Compromising Group Policy Objects via NTLM relaying</u>** Spoofing the GPT location by manipulating the gPCFileSysPath attribute

- The GPC defines an interesting attribute, `gPCFileSysPath`

- Specifies the location of the GPT as a UNC path

- Points by default to the SYSVOL share of the PDC

- ■ It is possible to specify an **`arbitrary SMB share location`** in this attribute

- Legitimate, intended feature rather than a bug ― but also kind of a gray area

**46**

## Slide 47

**<u>Compromising Group Policy Objects via NTLM relaying</u>** Spoofing the GPT location by manipulating the gPCFileSysPath attribute

- `1 $ smbserver.py -smb2support synacktiv .`

- `2 [...]`

- `3` **`[*] Incoming connection (192.168.123.17,49753)`**

- `4` **`[*] AUTHENTICATE_MESSAGE (CORP\AD01-SRV1$,AD01-SRV1)`**

**47**

## Slide 48

**<u>Compromising Group Policy Objects via NTLM relaying</u>** Attack exclusively relying on GPC modifications and exploitable via NTLM relaying

**48**

## Slide 49

**<u>Compromising Group Policy Objects via NTLM relaying</u>** Attack automation with GPOddity.py

- The `GPOddity.py` tool was created to automate the attack

- https://github.com/synacktiv/GPOddity

- ■ Main implementation challenge: **simulate a working domain-joined SMB server**

- The SMB server needs to properly authenticate clients

- `GPOddity.py` performs **`NETLOGON`** authentication for this purpose

**49**

## Slide 50

**<u>Compromising Group Policy Objects via NTLM relaying</u>** Attack automation with GPOddity.py

### **`Demonstration`**

**50**

## Slide 51

# **<u>Exploiting protected Organizational Units via GPO</u> link poisoning** Advanced GPO exploitation part 2

**51**

## Slide 52

**<u>Exploiting protected Organizational Units via GPO link poisoning</u>** Exploitation context

- The GPOs are linked Organizational Units through the `gPLink` attribute

- `[LDAP://cn={78BAF44B-B890-4812-AEB8-C11AC2B29FD2},cn=policies,cn=system,DC=corp,DC=com;0][...]`

- With write access to an OU object, **Petros Koutroumpis** showed that it is possible to **`add a gPLink item`** corresponding to a malicious GPO

- The OU objects would then apply the injected GPO

**52**

## Slide 53

**<u>Exploiting protected Organizational Units via GPO link poisoning</u>** Comparison with other OUs attack vectors

- Existing OU attack vector relies on **`ACL inheritance`**

- A `GenericAll` ACL is added to the OU security descriptor, and is **inherited**

- Simple and reliable attack, however:

   - Necessitates **WriteDACL** privileges to modify the security descriptor

   - Cannot be used against protected objects ( `adminCount=1` )

- `gPLink` poisoning exploitable with limited privileges and for protected objects

**53**

## Slide 54

#### **<u>Exploiting protected Organizational Units via GPO link poisoning</u>** The gPLink poisoning attack

- `gPLink` attribute modified to **`inject an additional GPO link`** to the OU

- The DN points to the attacker's machine

- `[...][LDAP://cn={78BAF44B-B890-4812-AEB8-C11AC2B29FD2},cn=policies,cn=system,` **`DC=attacker,DC=corp,DC=com`** `;0]`

- The attacker simulates a GPC, indicating that the GPT is also hosted on their machines

- **`OUned`** tool created to automate the attack ■ https://github.com/synacktiv/OUned

- https://github.com/synacktiv/OUned

- ■ **`WriteGPLink`** and **`GenericWrite`** BloodHound edges added on OUs

**54**

## Slide 55

#### **<u>Exploiting protected Organizational Units via GPO link poisoning</u>** The gPLink poisoning attack

**55**


> Recovered by OCR — confidence 91/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Exploiting protected Organizational Units via GPO link poisoning §=SYNACKTIV
The SPLink poisoning attack
DC
(corp.com) Client machines
2. Poisoned gPLink retrieval
<
<
v
1. gPLink poisoning of client
machines' OU
[LDAP://[...],DC=attacker, DC=corp, DC=com; 0]
3. GPC retrieval from
attacker.corp.com
4. GPT retrieval from
attacker.corp.com and
execution of malicious
configurations
attacker.corp.com
```

## Slide 56

**<u>Exploiting protected Organizational Units via GPO link poisoning</u>** Attack demonstration with OUned

### **`Demonstration`**

**56**

## Slide 57

# **<u>Conclusion</u>**

**57**

## Slide 58

# **<u>Conclusion</u>**

- **Risks associated with GPO exploitation may be underestimated today**

- GPOs provide powerful enumeration and exploitation primitives

- Knowledge gaps lead to security blind spots, that should be addressed with:

   - **Better understanding** of GPO inner workings

   - **Better enumeration and exploitation tooling**

- GPOs are fun and there is much more to be done!

**58**

## Slide 59

**https://www.linkedin.com/company/synacktiv https://x.com/synacktiv https://synacktiv.com**
