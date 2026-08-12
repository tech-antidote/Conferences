---
title: "The (Un)Rightful Heir My dMSA Is Your New Domain Admin"
speakers: ["Yuval Gordon"]
conference: "DEF CON"
conference_full: "DEF CON 33"
edition: "33"
year: 2025
source_pdf: "DEF CON 33/Yuval Gordon - The (Un)Rightful Heir My dMSA Is Your New Domain Admin.pdf"
pages: 39
sha256: "8652f9225ac00ec4665a2faf53bb106a2a82dd897b308a8aa92dfd26c9aa702d"
text_chars: 5618
ocr_pages: 7
has_ocr: true
redacted_secrets: 0
ocr_confidence: 88.7
ocr_unreliable_blocks: 1
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T07:17:04Z"
---
# The (Un)Rightful Heir My dMSA Is Your New Domain Admin

**Speakers:** Yuval Gordon  
**Conference:** DEF CON 33  
**Source:** `DEF CON 33/Yuval Gordon - The (Un)Rightful Heir My dMSA Is Your New Domain Admin.pdf` (39 pages)


## Slide 1

# **dMSA Is The (Un)Rightful Heir: My Your New Domain Admin**

###### **Yuval Gordon**

## Slide 2

### **The Great Mystery of MSAs**

• d MSA

• g MSA

## Slide 3

#### **whoami**

##### Yuval Gordon Security Researcher at Akamai

@YuG0rd

## Slide 4

#### **Agenda**

Introduction to service accounts Deep dive to dMSA BadSuccessor

## Slide 5

#### **Service Accounts**

Amusement park – Kerberos Daily ticket - TGT Ride – Service Ride Operator – Service account

Story by Elad Shamir – Kerberos Delegation Attacks

## Slide 6

#### **Service account type comparison**

Service Managed Service Account Account (MSA/gMSA) Password rotation High-complex passwords Kerberos best practices by default Can’t request password via LDAP

## Slide 7

#### **Why g(MSA)s Didn’t Take Over**

NOT FULLY POTENTIAL APP OPERATIONAL SUPPORTED DOWNTIME FRICTION FOR IT TEAMS

## Slide 8

**dMSA** (delegated MSA)

“dMSA’s secret can’t be retrieved or found anywhere other than on the DC”

– Microsoft Documentation

## Slide 9

**Migration Flow**

## Slide 10

#### **dMSA Migration Phases**

- Start

- Wait

- Complete

## Slide 11

#### **Authentication Flow – before migration**

##### SQL_SRV$

SQL Service

AS-REQ: svc_sql

AS-REP: svc_sql

DC

## Slide 12

#### **dMSA Migration - start**

DMSA$

Accounts are linked

svc_sql is granted permissions on DMSA$

svc_sql

## Slide 13

#### **Authentication Flow – during migration**

SQL_SRV$

SQL Service

AS-REQ: svc_sql

AS-REP: svc_sql Additional info: Will be superseded by DMSA$ LDAP UPDATE: Allow SQL_SRV$ access DMSA$

DC

## Slide 14

**Meme – now we wait / Spongebob**

## Slide 15

#### **dMSA Migration - complete**

DMSA$

Configurations

svc_sql

## Slide 16

#### **Authentication Flow – after migration**

##### SQL_SRV$

SQL Service

AS-REQ: svc_sql

KRB-ERR: Superseded by DMSA$ AS-REQ: DMSA$

AS-REP: DMSA$

DC

## Slide 17

**dMSA Migration - privileges**

## Slide 18

#### **Privileges**

KERBEROS
PAC
• svc_sql
• svc_sql group A
• svc_sql group B
• svc_sql group C
• …

KERBEROS
PAC
• DMSA$

## Slide 19

**Post migration**

## Slide 20

#### **Privileges**

KERBEROS
PAC

• DMSA$

• svc_sql

- svc_sql group A

- svc_sql group B

- • svc_sql group C • …

## Slide 21

#### **Migration**

Start-ADServiceAccountMigration migrateADServiceAccount (RootDSE op)

Attribute changes

## Slide 22

**BadSuccessor**

## Slide 23

**Attack Flow – Privilege Escalation** Starting point: attacker has control over dMSA

Simulate dMSA Migration Authenticate as dMSA Domain Admin Privileges granted

Goal: Acquire “Domain Admin” privileges

## Slide 24


> Recovered by OCR — confidence 96/100 on the text kept, 96/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Managed
Service
Account
Container
Literally
Any OU
```

## Slide 25

**Attack Flow – Privilege Escalation** ANY OU Starting point: attacker has control over ~~dMSA~~

Create dMSA in controlled OU Simulate dMSA Migration Authenticate as dMSA Domain Admin Privileges granted

Goal: Acquire “Domain Admin” privileges

## Slide 26

**DEMO**


> Recovered by OCR — confidence 79/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Administrator: Windows PowerShell
PS C:\>
```

## Slide 27

#### **Microsoft Response**

• Vulnerability severity: Moderate

- Does not meet the bar for immediate servicing

• Will be fixed in the future

## Slide 28

**But wait, there’s more!**

## Slide 29

**But wait, there’s more!**


> Recovered by OCR — confidence 91/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
But wait, there's more!
2.2.14 KERB-DMSA-KEY-PACKAGE
04/23/2024
The KERB-DMSA-KEY-PACKAGE structure contains a list of keys supplied by the KDC to an
authorized client when the client sends KDC-REQ-BODY as per [RFC4120] “ with the ticket granting
service as the sname using service for user as defined in [MS-SFU]
KERB-DMSA-KEY-PACKAGE ::= SEQUENCE {
previous-keys [1] SEQUENCE OF Encryptionkey OPTIONAL,
expiration-interval [2] KerberosTime,
fetch-interval [4] KerberosTime,
```

## Slide 30

#### **But wait, there’s more!**


> Recovered by OCR — confidence 90/100 on the text kept, 90/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
But wait, there's more!
SEQUENCE (4 elem)
[@] (1 elem)
SEQUENCE (3 elem)
SEQUENCE (2 elem)
[@] (1 elem) a
INTEGER 18 CURRENT-KEYS
[1] (1 elem)
OCTET STRING (32 byte) @9FED8B52EQ026B6D1B7D8BC223E5F3B39F1F7E94CE7A7F85E0012969B02D924
SEQUENCE (2 elem)
[@] (1 elem)
INTEGER 17
[1] (1 elem)
OCTET STRING (16 byte) EAF@DFD2A857662145D1F5D@56DF6D9C
SEQUENCE (2 elem)
[@] (1 elem)
INTEGER 23
[1] (1 elem)
OCTET STRING (16 byte) 6B9AC3DDCBC7C83F5917419042FFA2B2
elem
SEQUENCE (1 elem)
SEQUENCE (2 elem)
[@] (1 elem) PREVIOUS-KEYS
INTEGER 23
[1] (1 elem)
OCTET STRING (16 byte) 47BF8039A85@6CD67C524AQ3FF84BA4E
[2] (1 elem)
GeneralizedTime 1601-01-24 16:33:45 UTC
[4] (1 elem)
GeneralizedTime 1601-01-24 16:38:45 UTC
```

## Slide 31

**Aa123456**

## Slide 32


> Recovered by OCR — confidence 89/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
£ Yuval Gordon (J +
- @YuG@rd
Many missed this on #BadSuccessor: it’s also a credential dumper.
| wrote a simple PowerShell script that uses Rubeus to dump Kerberos
keys and NTLM hashes for every principal-krbtgt, users, machines. no
DCSync required, no code execution on DC.
an AndreTR @andreTRwi - May 25 (Yo
Seems quite moderate.
```

## Slide 33

**Detection**

## Slide 34

#### **dMSA Creation**

- Configure SACL


> Recovered by OCR — confidence 91/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
¢ Configure SACL
A directory service object was created.
Subject:
Security ID: AKA-DC 1\weak
Account Name: weak
Account Domain: AKA-DC1
Logon ID: Ox9F7154
Directory Service:
Type: Active Directory Domain Services
Object:
DN: CN=weak_dmsa,OU=temp,DC =aka, DC =test
GUID: CN=weak_dmsa,OU=temp,DC=aka,DC=test
Class: msDS-DelegatedManagedServiceAccount
Operation:
Application Correlation ID: -
```

## Slide 35

#### **dMSA Linkage**

- Configure SACL


> Recovered by OCR — confidence 85/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
USA Linkage
¢ Configure SACL
A directory service object was modified.
Subject:
Security ID: AKA-DC 1\weak
Account Name: weak
Account Domain: AKA-DC1
Logon ID: Ox9F72F8
Directory Service:
Name: aka.test
Type: Active Directory Domain Services
Object:
DN: CN=weak_dmsa,OU=temp, DC =aka,DC =test
Class: msDS-DeleqatedManagedServiceAccount
Attribute:
LDAP Display Name: msDS-ManagedAccountPrecededByLink
Syntax (OID): 25551
Value: CN=Administrator,CN=Users,DC=aka,DC=test
```

## Slide 36

#### **dMSA Credentials**

- Default log

## Slide 37

#### **Microsoft Response: Update**

"We are aware of this report and will be addressing it in an upcoming update"

## Slide 38

#### **Conclusions**

- Update ≠ Security

- Never skip the obvious

- Log & alert on dMSA links

- dMSA is a great new feature!

## Slide 39

## **Thank you!**

@YuG0rd
