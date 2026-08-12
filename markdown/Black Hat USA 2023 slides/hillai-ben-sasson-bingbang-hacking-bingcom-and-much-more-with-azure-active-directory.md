---
title: "BingBang Hacking Bing.com (and much more) with Azure Active Directory"
speakers: ["Hillai Ben-Sasson"]
conference: "Black Hat"
conference_full: "Black Hat USA 2023"
edition: "USA"
year: 2023
source_pdf: "Black Hat USA 2023 slides/Hillai Ben-Sasson_BingBang Hacking Bing.com (and much more) with Azure Active Directory.pdf"
pages: 60
sha256: "bf0009202cb0a7ceee9cbdf7eef4e2bc812bac97745bb04e07fbebbe73bc8719"
text_chars: 19249
ocr_pages: 28
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:17:22Z"
---
# BingBang Hacking Bing.com (and much more) with Azure Active Directory

**Speakers:** Hillai Ben-Sasson  
**Conference:** Black Hat USA 2023  
**Source:** `Black Hat USA 2023 slides/Hillai Ben-Sasson_BingBang Hacking Bing.com (and much more) with Azure Active Directory.pdf` (60 pages)

## Slide 1

Hillai Ben-Sasson @hillai

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
WIZ Research
eee https://www.bing.com/
BE Microsoft Bing
( BingBangl 9% &@ )
Hacking Bing.com (and much more)
with Azure Active Directory
Hillai Ben-Sasson (@@ @hillai
pif hat
USA 2@0es
```

## Slide 2

### **~~whoami~~ az ad signed-in-user show**

- Hillai Ben-Sasson (@hillai)

- Security Researcher at Wiz

- Microsoft Most Valuable Researcher

- Specialize in cloud security research

## Slide 3

## **Cloud vulnerabilities experience**

- **ChaosDB:** Cross-tenant database access in Azure Cosmos DB – Black Hat Europe 2021

- **OMIGOD:** Unauthenticated RCE as root in preinstalled agent – RSA 2022

- **ExtraReplica:** Cross-tenant database access in Azure PostgreSQL – Black Hat USA 2022

- **AttachMe:** Cross-tenant volume access in Oracle Cloud Infrastructure – Blogpost, Sep 2022

- **Hell’s Keychain:** Supply-chain vulnerability in IBM Cloud Databases - Blogpost, Dec 2022

- **BrokenSesame:** Supply-chain vulnerability in Alibaba Cloud Databases - Blogpost, Apr 2023

## Slide 4

## **Agenda**

1. Azure Active Directory 101

2. AAD Flaws

3. Scanning the internet for fun and profit

4. Hacking Bing & Co – Microsoft case study

5. Aftermath and Takeaways

## Slide 5

**Identity 101**

## Slide 6

Identity 102
🔒
Sign me in, my credentials are
User IdP
🔑
Sign-in successful, your token is
User IdP
🔑
My token is
User
App
Signed in!
User
App

## Slide 7

## Slide 8

## Slide 9

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
08 microsoftonline.com
#® Microsoft
Sign in
Email or phone
Can't access your account?
a4 Sign-in options
WIZ
```

## Slide 10

## **OAuth login request**

Client

Server

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
OAuth login request
POST /{MY_TENANT_ID}/oauth2/v2.@/token HTTP/1.1
Host: login.microsoftonline.com
User-Agent: Testos/1.0
Connection: close
Content-Type: application/x—ww-form-urlencoded oY
Content-Length: 107 sS
Server
scope={APP_ID}/.default&client_id={CLIENT_ID}
&client_secret={CLIENT_SECRET}&grant_type=client_credentials
WIZ
```

## Slide 11

Client

Server

## **OAuth token response**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
OAuth token response
"ver": "2.0",
"aud": "c7bb4ab4-a370-4b06-aa53-bf0aeeel5b80",
"iss": "https://login.microsoftonline.com/63d43bfd-1337-43f2-82d4-f67bd1lfcf8ac/v2.0",
"tid": "63d43bfd-1337-43f2-82d4-f67bd1fcf8ac",
"oid": "c028ba59-3b92-1337-9caf-e00007af7c44",
"sub": "c028ba59-3b92-1337-9caf-e00007af7c44", —
"nbf": ; Server
"exp": >
"ato": "RXZlcnloaW5nSXNTdGluZ2FibGU=",
"azp": "al56fa48-408b-4de4-1337-427b6c616e7b",
"azpacr": "1",
"rh": "SGLSbGFpV2FzSGVyZQ==",
"uti": "V2lL6UmMVZZWFyY2hSdwWxleg=="
```

## Slide 12

**AAD Flaws**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
AAD Flaws
Identity provider
App registration
App registration type
Name
Supported account types
| Microsoft
( ° ) Create new app registration
O Pick an existing app registration in this directory
@ Provide the details of an existing app registration
| hillai-testos
(@) Current tenant - Single tenant
@ Any Azure AD directory - Multi-tenant
@ Any Azure AD directory & personal Microsoft accounts
O Personal Microsoft accounts only
```

## Slide 13

**Shared responsibility model**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Shared responsibility model
"2.0",
"c7bb4ab4-a370-4b06-aa53-bf0aeee15b80" ,
"https://login.microsoftonline. com/63d43bfd-1337-43f2-82d4-f67bd1fcf8ac/v2.0",
"63d43bfd-1337-43f2-82d4-f67bd1fcf8ac",
"¢028ba59-3b92-1337-9caf-e00007af7c44",
: "c028ba59-3b92-1337-9caf-e00007af7c44",
: 1362663420,
: 1362663420,
: 1337663420,
"RXZLcn LoaW5nSXNTdGluZ2FibGU=",
: "al56fa48-408b-4de4-1337-427b6c616e7b" ,
"azpacr": "1",
"rh": "SGLSbGFpV2FzSGVyZQ==",
"uti": "V2L6UmVZZWFyY2hSdwWxleg=="
```

## Slide 14

**OAuth login request**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
OAuth login request
POST /{MY_TENANT_ID}/oauth2/v2.@/token HTTP/1.1
Host: login.microsoftonLline.com
User-Agent: Testos/1.0
Connection: close
Content-Type: application/x—www-form—-urlencoded
Content-Length: 107
scope={APP_ID}/.default&c Lient_id={CLIENT_ID}
&client_secret={CLIENT_SECRET}&grant_type=client_credentials
WIZ
```

## Slide 15

**OAuth login request**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
OAuth login request
{MY_TENANT_ID}
WIZ
```

## Slide 16

**OAuth login request**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
OAuth login request
{YOUR_TENANT_ID}
WIZ
```

## Slide 17

```
User    =  Hillai Ben-Sasson
Tenant  =Wiz Research
```

## Slide 18

```
User    =  Hillai Ben-Sasson
Tenant  =Your company here
```

## Slide 19

User

**_`User`_** `= AttackerUser` **_`Tenant`_** `= AttackerCorp` Wiz Research App

### ACCESS DENIED

## Slide 20

User

**_`User`_** `= AttackerUser` **_`Tenant`_** `= Wiz Research` Wiz Research App

### ACCESS GRANTED

## Slide 21

## **AAD Flaws – Recap**

1. Customer misconfigurations

   - The checkbox of doom

2. Insufficient checks

   - When is my tenant not really my tenant?

## Slide 22

Scanning the internet for fun and profit We have a theory Let’s test it out!

## Slide 23

Get Azure App Service domains Throw away non-existent apps Find AAD apps Filter multi-tenant configurations Log in

## Slide 24

Get Azure App Service domains Throw away non-existent apps Find AAD apps Filter multi-tenant configurations

Log in

## Slide 25

Azure App Service

🌐.azurewebsites.net https://

Let’s hunt some subdomains

## Slide 26

## **grep -r “    ” /internet**

- Where do we find domains?

- Passive DNS

   - DNS query data streams

   - Sourced from ISPs, hosting providers and enterprises

## Slide 27

Get Azure App Service domains Throw away non-existent apps Find AAD apps Filter multi-tenant configurations Log in

## Slide 28

Get Azure App Service domains Throw away non-existent apps Find AAD apps Filter multi-tenant configurations Log in

## Slide 29

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
08 microsoftonline.com
#® Microsoft
Sign in
Email or phone
Can't access your account?
a4 Sign-in options
WIZ
```

## Slide 30

Get Azure App Service domains Throw away non-existent apps Find AAD apps Filter multi-tenant configurations Log in

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Get Azure App Service domains
Throw away non-existent apps
Find AAD apps
Filter multi-tenant configurations
Log in
WIZ
```

## Slide 31

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
08 microsoftonline.com
#® Microsoft
Sign in
Email or phone
Can't access your account?
a4 Sign-in options
WIZ
```

## Slide 32

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
<!DOCTYPE html>
"ltr" Lan
>Sign in to your account</ti
http-equiv="Content-Type" content="text/html; charset=UTF-8"
http-equiv="X-UA-Compatible" conten IE=edge"
a name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=: » user-sca">
a http-equiv="Pragma" content="no-cache"
a http-equiv="Expires" content="-1">
rel="preconnect" href="https://aadcdn.msauth.net" crossorigin>
http-equiv="x-dns-prefetch-control" content="on
rel="dns-prefetch" href="//aadcdn.msauth.net">
dns-prefetch" href="//aadcdn.msftauth.net">
PageID" content="ConvergedSignIn"
SiteID" conten
"ReqLC" content:
a name="LocLC" content="en-US"
a name="format-detection" content="telephone=no"
ript>
neta http-equiv="Refresh" content="0; URL=https://login.microsoftonline.com/jsdisabled"
name="robots" content=
type="text/ javascript"
fig={"fShowPersistentCookiesWarning": false, “urlMsaSignUp":"https://login. live. com/oauth20_autho
script
cript type="text/javascript"
!function(){var e=window, r=e.$Debug=e.$Debug| |{}, . $Config| |{};if(!r.appendLog){var n=[],0=0;r.ap
r c=t(i, !e);if(a&Sa.length>0){for(var d=a. length, l=0;l<d;1++){c.push(all] )}}0.apply(r,c)}catch(e)
(var c=u;c<arguments.length;c++){s.push(arguments[c])}t instanceof Array?e(t,i):i(t)},o.reg
=o. removeItems[c] , l=0;1<o.q. Length; l++){if(o.q[1]===d){o.q.splice(1,1) k}}}o.removelte
r.addEventListener?(r.removeEventListener("DOMContentLoaded" ,o, !1),e.removeEventListener( "load",
f.$Config| |f.ServerData| |{}}function r(e,r){var t=f.$Debug;t&&t.appendLo
r r=e.index0f("?"),t=r>-1?r:e. length,n=e. lastIndex0f(".",t);return e.substring(n,n+h.length).toLo
===a.length){ !0}}return!1}function c(){fur 1 t(e){g.getElementsByTagName( "head" )
r=g.createElement("script"),t=g.querySelector("script[nonce]");if(r.type="text/javascript",r.sr
dex0f(t[n])){va [n+1<t.length?n+1:0],i=r.substring(t[n].length);return"https://"!
h(e,t,n,o){if eturn f(e,t,n,o)}r("[$Loader]: "+(w.successMessage| | "Loaded"),0),v(e+
s.readyState?setTimeout( function( ){h(e,o0,i,s)}, :"complete s.readyState&&h(e,o0,i,s
||e.href||"" Add(t, "AddForReload",e. integrity, 1,e.tagName,r)},w.AddIf=function(e,r,t){
jd. failMessage="Reload Failed" ,d.successMessage="Reload Success",d.Load(null, function( ){if(o){thro
u.Load(null, function( ){if(o){throw"Failed to load external resource [' wey"y: (document .locatio
y.fbundle=null,delete y.fbundle,e.Add(y.bundle, "WebWatson_DemandLoaded"),e.Load(r,t),$=!0}}function
e.setRequestHeader( "Content-Type", "application/json; charset=UTF-8"),e.setRequestHeader( "canary"
"msg": "Failed to load external resource [Core Watson files]","url":o[1]||"","In":0,"ad":0, "an":
}fur 1 a(e,r,t,n,o,i,a){var s=v.event;r n i[|(i=l(o| |s,a?a+2:2)),v.$Debug&&v. $Debug. appendLog
freturn r}function d(e){if(!e){return null}try{if(e.stack){return u(e.stack)}if(e.error){if(e.error
var l=d(e);return 1&&(t.push(s(" Error Event Stack - -",01)), -concat(1l)),t}func
if(jQuery?(r.push("jQuery v:"+jQuery(). jquery), jQuery.easing?r.push("jQuery.easing:"+JSON.stringify
1=0; i<b. length; i++){var 5 Uf (a&&" submit "===a. cmdName ){try{if(JSONSGISON. stringify){var
ar t=r.split("."),n=t.length,o=0; &&nul lt == oid O!==e; ){e=e[t[o++]]}return e}function r(r
ion o(t){var n=null;return null= &(s=e(i,"$Config.urls")),null!==s& (n=e(s,t.toLowerCase
cript:
t type="text/javascript">
n(t,e){!function( ){var n=e.getElementsByTagName( "head" )[0] ;n&&n. addEventListener&&(n.addEve
jone
WIZ
```

## Slide 33

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
"isGlobalTenant": true,
WIZ
```

## Slide 34

Get Azure App Service domains Throw away non-existent apps Find AAD apps Filter multi-tenant configurations Log in

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Get Azure App Service domains
Throw away non-existent apps
Find AAD apps
Filter multi-tenant configurations
Log in
WIZ
```

## Slide 35

**grep -r “   ” /internet**

- 5,266 multi-tenant apps

- 1,298 vulnerable apps

- 562 vulnerable organizations

25% of multi-tenant apps were vulnerable

## Slide 36

Who has the best bug bounty program?

## Slide 37

## **Microsoft as a case study**

- How do we narrow down our list?

- We’ll query each application on Azure’s Graph API

## Slide 38

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
"@odata.context": "https://graph.microsoft.com/v1.0/$metadata#servicePrincipals/gentity",
"id": "4f41e6c2-52a5-4a54-b207-3b02dd8b6d95",
"deletedDateTime": null,
"“accountEnabled": true,
“alternativeNames": [],
"appDisplayName": "bingtriviav8",
"appDescription": null,
"appId": "92b2243e-b03e-45cc-bfb6-ccfe9abaf376",
"“applicationTemplateId": null,
“appOwnerOrganizationId": "72f988bf-86f1-41laf-9lab-2d7cd011db47",
"appRoleAssignmentRequired": false,
"createdDateTime": null,
"description": null,
"disabledByMicrosoftStatus": null,
"displayName": "bingtriviav8",
"homepage": "https://bingtrivia.azurewebsites.net",
"LoginUrl": null,
"LogoutUrl": null,
"notes": null,
"notificationEmailAddresses": [],
"preferredSingleSignOnMode": null,
"preferredTokenSigningKeyThumbprint": null,
"replyUrls": [
"https://bingtrivia.azurewebsites.net/.auth/login/aad/callback"
Ip
"servicePrincipalNames": [
"Q2b2243e-b03e-45cc-bfb6-ccfe9abaf376",
“apt: //92b2243e-b03e-45cc-bfb6-ccfe9abaf376"
lp
"servicePrincipalType": "Application",
"signInAudience": "AzureADMultipleOrgs",
```

## Slide 39

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
"appOwnerOrganizationId": "72f988bf-86f1-4laf-9lab-2d7cd011db47",
```

## Slide 40

**Microsoft findings**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Microsoft findings
- om: ys.azurewebsites.net
* col -2.azurewebsites.net
* poli t.microsoft.com
* con : ——_ -1.azurewebsites.net
«bin a.azurewebsites.net
* con ‘5.azurewebsites.net
* om s.azurewebsites.net
* co . . v1-1.azurewebsites.net
* po -microsoft.com
* con -2.azurewebsites.net
* po .microsoft.com
WIZ
* CO ‘ ‘ 1-2.azurewebsites.net
```

## Slide 41

#### **Microsoft findings**

- bingtrivia.azurewebsites.net

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Microsoft findings
*- om: js.azurewebsites.net
* co -2.azurewebsites.net
* poli t.microsoft.com
* con ; -1.azurewebsites.net
¢ bingtrivia.azurewebsites.net
* con ‘3.azurewebsites.net
° m s.azurewebsites.net
* co v1-1.azurewebsites.net
* po -microsoft.com
* con -2.azurewebsites.net
* po -microsoft.com
WIZ
° co 1-2.azurewebsites.net
```

## Slide 42

**Demo time**

## Slide 43

**Bing for Work**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Bing for Work
&@ bing.com
LATEST FROM WIZ Show info from Wiz COD
Popular searches Coming up im Recent files a
me my office Q
Only users with permission will see your files and info. QO
Learn more See more See more
WIZ
```

## Slide 44

Bing for Work
Generate Office 365 access token for hillai@wiz.io
Client Bing
Your token is   🔑
Client Bing
🔑
My token is
Client
Office
365
Client Office
365

## Slide 45

Bing for Work
Generate Office 365 access token for hillai@wiz.io
Attacker Bing
Your token is   🔑
Attacker
Bing
🔑
My token is
Attacker
Office
365
Attacker
Office
365

## Slide 46

**Work for Bing**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Work for Bing
eee
<script>
fetch("https://business.bing.com/api/v3/user/token/Substrate", {credentials: "include"})
.then((res) => res.json()).then( function(data){
console. log( Logged in as ${data.user.displayName} (${data.user.userPrincipalName})~ );
console.log( User ID is ${data.user.id}, Tenant ID is ${data.tenant.id}° );
console. log( Generated Office 365 token:\n${data.token}  );
IP))E
</script>
WIZ
```

## Slide 47

## **But wait, there’s more**

## Slide 48

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Welcome
¥ Best of Microsoft Ne’
research@wizresearch.onmicrosoft.con
EN-US x _EN-US_New_SingleCol_WithUNmessage. v Ora File:
CMS List ID: e.g. AAdfeCr Load content from CMS List ID Clear All
LIVE PREVIEW: _EN-US_New_SingleCol_WithUNmessage_7Card
bare Y msn BEST OF MSN
powered by Microsoft News
02/08/2023 February 8, 2023
EDITOR NAME,
EDITOR NOTES.
STORYI
URL
(URL1] Import Story
TITLE
[HEADLINE] ]
ABSTRACT
[ABSTRACTI] [HEADLINE1]
IMAGEURL.
http://img-s-msn-com.akamaized.net/tenant/amp/en! [ABSTRACT 1]
PROVIDER
(PARTNER 1] ¥ [PARTNER1]
LOGO
https://img-s-msn-com.akamaized.net/tenanvamp/et
TUCAMI INE
WIZ
```

## Slide 49

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ swecger Select detnton
SMARTBEAR
Centralized Notification Service (CNS) API“
/swagger!v1/swagger.json
Servers
[ https://es-cns-ppe.azurewebsites.net v
TeamsMember “a
/api/teamsmember Adding user to CNS Teams Vv
Configuration A
E /api/configuration/maxattachmentsize Gets maximum attachment size in mb per request Vv
/api/configuration/getmaxattachmentsize Gets maximum attachment size in mb per request Vv
E /api/configuration/maxnumberattachments Gets maximum number of attachments per request Vv
/api/configuration/getmaxnumberattachments Gets maximum number of attachments per request Vv
File “A
/api/file Upload a list of attachments to the attachments storage account blob Vv
MicrosoftGraph A
E /api/microsoftgraph/groupid Get group id from the specified group. Vv
Notification A
/api/notification Sends a notification, we restrict number of recipients when a notification is sent. We can only send email up to 250 recipients at a time. For Teams message the limit is 30 recipients.. Vv
Publication A WIZ
```

## Slide 50

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ swagger Select a definition
'SMARTBEAR
Contact Center API Gateway - Profile®
/swagger/v1/swagger.json
Profile Service APIs
AgentGroups Vv
/AgentGroups Get all agent groups.
E /AgentGroups/{surveyId} Get agent group by survey id.
/AgentGroups/Routing Create routing agent group.
/AgentGroups/Reporting Create reporting agent group.
/AgentGroups/Recording Create reporting agent group.
| b)383)39) /AgentGroups/{id} Delete Agent group by Id.
BusinessPrograms Vv
/BusinessPrograms Get all Business programs.
/BusinessPrograms Create a business program.
/BusinessPrograms/ {code} Get business program by code.
/BusinessPrograms/{code} Update business program.
| b)383)-9) /BusinessPrograms/ {code} Delete business program by code.
BusinessSegments Vv
WIZ
```

## Slide 51

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
PoliCheck term data
Caution
Term data contains explicit language that some may find offensive.
All content is Microsoft confidential.
For severity code definitions, see the Severity code ratings
* Indicates mandatory fields
Language: * English — Select Severity: All Severities (5) - Term Name:
-- Select term -- bd
Select Term Class: All Term Classes (6) bd
Search By Textbox/Language
| Gexport Displayed terms to Exc|| (Export All terms to Excell | (ZExport All Terms in Language
Terms Per Page: |50 ~| Total Terms: 2789
Action/
Severity Context Racommandation For More Information
Pe %
© ‘© English 2 Geopolitical REMOVE
&
© ‘© English 2 Geopolitical REMOVE
Leave term
unchanged
©® °
English 2 Accessibility
REMOVE
Leave term
unchanged
English 2 Accessibility
REMOVE
WIZ
```

## Slide 52

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
powerautomate.microsoft.com
LH Microsoft | Power Automate Product ~ Capabilities » Pricing Partners Learn » Support ~» Community v
Product updates
February 2023 update of Power
Automate for desktop
Yiannis Mavridis, Program Manager II, Wednesday, February 22, 2023 o © fin)
We are happy to announce that the February 2023 update of Power Automate for desktop (version 2.29) has been
released! You can download the latest release here. New features and updates have been added, as described below.
Regions have now been introduced in the designer
Two new actions are available in the flow designer, called ‘Region’ and ‘End region’, which help group and organize
sets of actions together for better flow management purposes.
o/ Run subflow Login_to_terminal
o/” Run subflow Terminal_screen_navigation
WIZ
```

## Slide 53

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
©) A Microsoft Flow Blogs
@ Dashboard
> Posts
All Posts
Add New
oO, Media
® Comments
Workflows
Profile
Tools
Collapse menu
“F New View Post
WordPress 6.1.1 is available! Please notify the site administrator.
Howdy, research a2
Screen Options ¥ Help ¥
Allow WP SendGrid Plugin to send you setup guide? Opt-in to our newsletter and we will immediately e-mail you a setup guide along with 20% discount which you can
use to purchase any theme.
Allow Sending Do not allow
Edit Post Add New
February 2023 update of Power Automate for desktop
Permalink: https://powerautomate.microsoft.com/en-us/blog/february-2023-update-of-power-automate-for-desktop/
Qy Add Media Visual Text
We are happy to announce that the February 2023 update of Power Automate for desktop (version
2.29) has been released! You can download the latest release <a
href="https://go.microsoft.com/fwlink/?Linkid=2102613">here</a>. New features and updates
have been added, as described below.
<h2>Regions have now been introduced in the designer</h2>
Two new actions are available in the flow designer, called ‘Region’ and ‘End region’, which
help group and organize sets of actions together for better flow management purposes.
<img class="alignnone wp-image-9718 size-full" src="/wp-content/uploads/2023/02/Region-
nnn nL WAVa Wadaka WoeaW 7
Publish a
Preview Changes
f Status: Published Edit
® Visibility: Public
Update
Categories a
All Categories Most Used
Vv) Product updates
Developers
WIZ
```

## Slide 54

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
OOOO ee eT
Storage Utilization for MSFT ® = ! 7
Cluster Filter: All / 08-CO3C / 09-CO3C / 11-CY2 / 12-CY2/14-CY2/15-CY/17-_ Data Access Time Window: 7d / 30d / 60d /
co 90d
WIZ
```

## Slide 55

## **Aftermath – Microsoft**

- All issues were reported to Microsoft

- Applications were out of scope

- $40,000 bug bounty - for AAD product and guidance improvements

## Slide 56

## **Aftermath – Microsoft**

- Documentation and guidance overhaul

- You can no longer sign in under a different tenant by default

   - There are several exceptions

- New configurations options

   - WEBSITE_AUTH_AAD_ALLOWED_TENANTS

## Slide 57

## **Aftermath – Azure customers**

- Manually check your multi-tenant apps

   - Should they be multi-tenant?

- Review your authorization logic

   - Do not rely on Azure’s built-in checks alone

   - Implement claims-based authorization

## Slide 58

## **For more guidance**

<u>https://wiz.io/blog/azure-active-directory-bing-misconfiguration</u>

<u>https://msrc.microsoft.com/blog/2023/03/guidance-on-potential-misconfigurationof-authorization-of-multi-tenant-applications-that-use-azure-ad/</u>

## Slide 59

## **Takeaways**

- In the cloud, external exposure is more accessible than ever

   - Agility has its downsides

- Each service has its own shared responsibility model

   - Make sure you’re aware of where the line is drawn

- Monitor your environments

   - Always enable logging

   - Track unusual activity

## Slide 60

# **Thank you!**

@hillai

research@wiz.io

wiz.io/blog
