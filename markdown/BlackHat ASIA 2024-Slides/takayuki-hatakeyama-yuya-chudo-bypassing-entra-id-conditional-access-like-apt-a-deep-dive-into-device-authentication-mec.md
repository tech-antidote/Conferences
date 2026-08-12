---
title: "Bypassing Entra ID Conditional Access Like APT A Deep Dive Into Device Authentication Mechanisms for Building Your Own PRT Cookie"
speakers: ["Takayuki Hatakeyama", "Yuya Chudo"]
conference: "Black Hat"
conference_full: "Black Hat ASIA 2024"
edition: "ASIA"
year: 2024
source_pdf: "BlackHat ASIA 2024-Slides/Takayuki Hatakeyama & Yuya Chudo-Bypassing Entra ID Conditional Access Like APT A Deep Dive Into Device Authentication Mechanisms for Building Your Own PRT Cookie.pdf"
pages: 67
sha256: "99bb4dc4a24a6026050faaaf2166481cb44cecd81e810173a4fdd494d05fe7eb"
text_chars: 24720
ocr_pages: 12
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T00:51:54Z"
---
# Bypassing Entra ID Conditional Access Like APT A Deep Dive Into Device Authentication Mechanisms for Building Your Own PRT Cookie

**Speakers:** Takayuki Hatakeyama, Yuya Chudo  
**Conference:** Black Hat ASIA 2024  
**Source:** `BlackHat ASIA 2024-Slides/Takayuki Hatakeyama & Yuya Chudo-Bypassing Entra ID Conditional Access Like APT A Deep Dive Into Device Authentication Mechanisms for Building Your Own PRT Cookie.pdf` (67 pages)

## Slide 1

##### Bypassing Entra ID Conditional Access Like APT

**A Deep Dive Into Device Authentication Mechanisms for Building Your Own PRT Cookie**

**Speaker: Yuya Chudo Contributor: Takayuki Hatakeyama**

#BHASIA @BlackHatEvents

## Slide 2

##### Whoami

- Yuya Chudo

- Senior Advisor @ Secureworks Japan K.K

- • Provides red teaming service for enterprises mainly in Japan

# BHASIA @BlackHatEvents

## Slide 3

##### Agenda

- Introduction

- Microsoft Entra ID Device Authentication Mechanism

- Device Authentication Internals and Abuse

- Demo

- Mitigation

- Conclusion

# BHASIA @BlackHatEvents

## Slide 4

# Introduction

# BHASIA @BlackHatEvents

## Slide 5

###### Spear-phished & Compromised Active Directory

###### Attacker (me)

Active Directory

Corporate Device

Dumped credentials with Domain Admin privilege

# BHASIA @BlackHatEvents

## Slide 6

###### Pivoting to the Cloud …

###### Attacker

aadadmin/ qwerty1234

Cracked Password

Microsoft Entra ID

# BHASIA @BlackHatEvents

## Slide 7

###### Blocked by Entra ID Conditional Access

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Q
black hat
ASIA 2024
Blocked by Entra ID Conditional Access
B® Microsoft
aadadmin@ ,onmicrosoft.com
You can't get there from here
This application contains sensitive information and
can only be accessed from:
* MSFT domain joined devices. Access from
personal devices is not allowed.
Since you're using Firefox, you need to enable the
Firefox browser setting to allow Windows single
sign-on for Microsoft, work, and school accounts.
You must be on Firefox 91 or above. Alternatively,
you can use Microsoft Edge or Internet Explorer to
access this application.
Sign out and sign in with a different account
More details
```

## Slide 8

###### Conditional Access in Microsoft Entra ID

User/Group

Device

Application

Network

“brings signals together, to make decisions, and enforce organizational policies.”

# BHASIA @BlackHatEvents

## Slide 9

###### Requires Corporate Device for Access

**Device based Conditional Access Policy** Require Microsoft Entra hybrid joined device Marked as compliant

# BHASIA @BlackHatEvents

## Slide 10

### Blocked by Entra ID Conditional Access How Can We Bypass Device-Based Conditional Access Policy?

# BHASIA @BlackHatEvents

## Slide 11

##### Goal

- Bypass device-based Condtional Access policy and gain access as any user with their credentials

# BHASIA @BlackHatEvents

## Slide 12

#### Microsoft Entra ID Device Authentication Mechanism

# BHASIA @BlackHatEvents

## Slide 13

###### Device Registration #1 Device key and Transport key are generated

Device key Transport key
dkpub / dkpriv tkpub / tkpriv

# BHASIA @BlackHatEvents

## Slide 14

###### Device Registration #2 dkpub and tkpub are sent to Microsoft Entra ID

Device (win11pc01)

dkpub, tkpub

Microsoft Entra ID

My device name is “win11pc01” and here are my keys

# BHASIA @BlackHatEvents

## Slide 15

Authentication Flow (Browser SSO) #1 Send logon request signed by Device key (dkpriv)

Device (win11pc01)

Logon request signed by dkpriv

Microsoft Entra ID

Let me validate if the request is signed by the “win11pc01” Device key

# BHASIA @BlackHatEvents

## Slide 16

RSASHA256( base64UrlEncode(header) + "." + base64UrlEncode(payload),

###### Authentication Flow (Browser SSO) #1 Send logon request signed by Device key (dkpriv)

JSON Web Signature by Deice key (dkpriv)

# BHASIA @BlackHatEvents

## Slide 17

Authentication Flow (Browser SSO) #2 Receive PRT (Primary Refresh Token) and session key

Device (win11pc01)

Logon request signed by dkpriv

Session key (encrypted)

PRT

Microsoft Entra ID

Okay you are “win11pc01”. Here are the PRT and session key

# BHASIA @BlackHatEvents

## Slide 18

Authentication Flow (Browser SSO) #2 Receive PRT (Primary Refresh Token) and session key

Can be used for Single Sign On

Can be decrypted by Transport key and used for signing

# BHASIA @BlackHatEvents

## Slide 19

Authentication Flow (Browser SSO) #3 Send PRT Cookie signed by session key

Device (win11pc01)

PRT Cookie signed by session key

Microsoft Entra ID

Let me check if the valid session key bounded to device is used for signing

# BHASIA @BlackHatEvents

## Slide 20

###### Authentication Flow (Browser SSO) #3 Send PRT Cookie signed by session key

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Q
black hat
ASIA 2024
Authentication Flow (Browser SSO)
#3 Send PRT Cookie signed by session key
GET /common/oauth2/v2. 0/author ize?cl ient_id=4765445b-32c6-49b0-83e6-1d93765276ca&redirect_ur i=httpsh3a%2F%2fwww. of fice. coms2f landingv2&
response_type=code+id_token&scope=openid+profi le+httpsh3a,2F%2fwww. of fice. coms2fv2%2f0ff iceHome. Al |&response_mode=form_post&nonce=
638448025768012973 Madr mia ts sbtskdoestaten ———— —
cl ient-request-id=8b041a46-d747-4d6a-8f 12-8bb35036d22a&state=
HLROAIBz-GHxaa9f j7beRK-eWTvznr zncSBRO1AZH3q6m_NoCk j21s41 Ihi i6Ye jy¥66kcU4mN2UJOE_NX7K4_| JWT payload (decoded)
vSI8LRW6-Pb5a46mYTcP2C8fqhhOLUSLvFReV3NgtHvsmaF 6eN jApn9aUmzYuUKtF lketvn1FUu7T jM2wPGzAa
NQdw&x-c | ient-SKU=1D_NET6_0&x-cl ient-ver=7. 2. 0. 0&sso_nonce= “refresh token”
AwABAAEAAAACA0z_BQD0_x0QSvBvX0y1dwKAPO!CnNzEv7P1snZtDgk7 fHe9GOR83c2MwO7W9qVguHeaRiWT-a ATOATmRO7 = ’ rae -
8b041a46-d747-4d6a-8f12-8bb35036d22a HTTP/1. 1 . a .
Host: login. microsofton| ine. com PRT
(snipped) “is_primary’: “true”,
X-Ms-Refreshtokencredential “win_ver’: “10.0. 22621. 3085”
eydhbGci0iJIUZ11Nils]CUrZGZFdmVy1 joyLCAi Y3R41 joi TkEZWXd1d1hqaTBkdkZMR1 JQald3MVR2Z01 jSV “windows_api_version’: “2.0.1”,
“x_client_platform’: “windows”
*]
“request_nonce’: “AwABAAEAAAACAOz_BQD0_x0QSv (snip
PRT Cookie
V14M2MyTXRN1c5cVZndUh! YVupV10tYWFTcXhJUC1HW jYxcnBnWFktOVOz0GdBOSU9. OgSOLtuyfKaTwfDGuUvSPty6 ih2vr Zy3UXVKDUKDv30
```

## Slide 21

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
ASIA 2024
Microsoft 365 e) @
A Microsoft 365 €2) C@HASS cet sopor 8
si A THis Microsoft 365 DA—A N-VTF. FATO Microsoft 365 PF VAR PIVATFSECEMTAES. SB TUBES I—F— 341A
= SUMENSOES. 10 SMBBLTASTCON-VEBMLTCK ES). ENTEVPTFUPBRSNVAUBSITIS. 17 PSE SSP OR— FUL? a
S)
E +
a)
Microsoft 365 NAO TE ‘
&p <=
RATS fp —
Gy rr venxss 4d -
DAYD FIVA
GIT © SERURES &3 HARRY 7 Pyyo-K = 9
cy
I °
aN
RMUMEBLIEIYT UY ILS0ECA
MLNRFIAXD heremIsn. KFaAxX> bhery7oO-k
```

## Slide 22

###### Device Authentication Mechanism

- Device key and Transport key are generated and registered

- • Microsoft Entra ID identifies device in tenant by signatures of Device key and  session key

- Session key can be used when decrypted by Transport key By signing a specific user’s logon request and PRT with the keys, we can access to resources as a registered device

# BHASIA @BlackHatEvents

## Slide 23

###### Prior Research

- Device key, Transport key and session key are securely stored in TPM (Trusted Platform Module) if available

- • Exporting a derived key of session key for creating PRT Cookie is discovered by Benjamin Delpy and Dirk-jan Mollema (Patched as CVE2021-33781)

# BHASIA @BlackHatEvents

## Slide 24

###### Research Idea

**If we understand how the TPM stored keys are handled, we can still abuse them for faking device?**

# BHASIA @BlackHatEvents

## Slide 25

#### Device Authentication Internals and Abuse

# BHASIA @BlackHatEvents

## Slide 26

###### How Google Chrome Handles Browser SSO

Chrome

(Windows Accounts Extension)

###### **Abuse for PRT Cookie Theft**

PRT Cookie
BrowserCore.exe
MicrosoftAccount
TokenProvider.dll
GetCookieInfoForUri

- `・` BrowserCore approach

(ROADtoken by Dirk-jan Mollema)

`・` DLL approach

(RequestAADRefreshToken by Lee Christensen)

# BHASIA @BlackHatEvents

## Slide 27

###### Reversing GetCookieInfoForUri

Data is sent to an authentication package in lsass.exe for PRT Cookie retrieval

# BHASIA @BlackHatEvents

## Slide 28

###### Reversing GetCookieInfoForUri

JSON data is sent to lsass.exe and it includes call and payload values

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Q
black hat
ASIA 2024
Reversing GetCookielnfoForUri
JSON data is sent to
| a lsass.exe and it includes call
“payload”: and payload values
“https login. microsofton! ine. com, common/oatuh?, author ize?sso_nonce=AwABA
AEAAAACAOz BODO _?u6/X28k jL4AVzLD jdCSeKH jPdTQe/-V6FYeFrvgAFSFdwU jad] Bwetq0s
bObyokq? 109rgk/D3e9v_ UeZJ0GczAA
“correlationid .
“uaClientId”™: °*
```

## Slide 29

JSON Data is passed to CloudAP and aadcloudap **CloudAP** (Cloud Authentication Provider) Modern authentication provider for Windows sign in **aadcloudap** (Microsoft Entra CloudAP Plugin) Verifies user credentials with Microsoft Entra ID

# BHASIA @BlackHatEvents

## Slide 30

functions in aadcloudap are invoked aadcloudap!GenericCallPackageHelper::GenericCallPackage

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Q
black hat
ASIA 2024
functions in aadcloudap are invoked
aadcloudap!GenericCallPackageHelper::GenericCallPackage
switch ( callnum )
if
case lu:
tatus = GenericCallPackageHelper: :SignPayload(al, a2, payload_a
sta 4, TokenHandle, account_info_a6, al@);
v25 = status;
foto LABEL 49;
v23 = 36;
yv21 = (struct CSec
LODWORD(w28) = sta
goto LABEL 3;
ureString *) DBG_BASENAME("onecoreuap\\ds\\ext\\aad\\aadcloudap\\genericcallpackagehelper. cpp")
3
case 2u:
status =|GenericCallPackageHelper: :CreateSSOCookie(al, a2, payload_a4, TokenHandle, account_info_a6, a9, al@);
v25 = status;
goto LABEL 49;
vi? = _DBG_BASENAME("onecoreuap\\ds\\ext\\aad\\\aadcloudap\\genericcallpackagehelper. cpp");
LODWORD(v22) = 48;
goto LABEL 11;
case 3u:
status = GenericCallPackageHelper: :GetPrtAuthority(al, a2, account_info_a6, a9
V£o = STaTuUs,;
```

## Slide 31

###### What’s happening when browser SSO

Chrome
aadcloudap
PRT Cookie
1 SignPayload
BrowserCore.exe
2 CreateSSOCookie
lsass.exe
MicrosoftAccount 3 GetPrtAuthority
RPC
TokenProvider.dll
GetCookieInfoForUri 4 CheckDeviceKeysHealth
call number,  ・
payload ・
・
LsaCallAuthenticationPackage
15 GenerateBindingClaims
# BHASIA @BlackHatEvents

# BHASIA @BlackHatEvents

## Slide 32

###### Replicating the flow for another PRT Cookie theft

Malware
aadcloudap
1 SignPayload
BrowserCore.exe
2 CreateSSOCookie
lsass.exe
MicrosoftAccount 3 GetPrtAuthority
RPC
TokenProvider.dll
GetCookieInfoForUri 4 CheckDeviceKeysHealth
call number,  ・
payload ・
・
LsaCallAuthenticationPackage
15 GenerateBindingClaims
# BHASIA @BlackHatEvents

Malware BrowserCore.exe

# BHASIA @BlackHatEvents

## Slide 33

###### Replicating the flow for another PRT Cookie theft

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
black hat < '
ASIA 2024
cx.) JYYK JOYTb - powershell Te
PS C:\> Request-PRTCookie
| jeyIJhbGci0iJIUZIINiIsICIrZGZfdmVyIjoyLCAiY3R4IjoiMzUzbO9mKOtmbnpyYUp5U1pUWT LcLOd3aDhqeTV3VFpxin®. eyJyZWZyZXNox
3Rva2Vul joiMC5BVDBBN21SUVpHNmIyME9kUnY2QnBse jk2b2M3cWpodG9CZELzbLY2TVdtSTIUdWhBUFEUQWdBQKFBRUFBQURUZMm9sSaEpwU2
LuZG93cyIsICJyZXF1ZXNOX25vbmNLIjoiQXdBQkKFBRUFBQUFDQU96X9IRRDBFeGFrTDZiU3 LaUXQUSZUtcHBOaVKOVIVyM3LtMLdhZLOHYkZ
FMy lmMGFvVDdxYmJ3U2hiQXdwXzBvVmx0UzLiSkp2aU95dnFoTk9YT j BFODNFMKtVMDRnNQUEIFQ.K7xh3mFCyS_5F—-Ewj XCBwi_suYGdNgQIw
M4YxzLhPzk
```

## Slide 34

###### Replicating the flow for another PRT Cookie theft

**Abuse for PRT Cookie Theft** `・` BrowserCore approach (ROADtoken by Dirk-jan Mollema)

- `・` DLL approach

(RequestAADRefreshToken by Lee Christensen) `・` [ **New!** ] **LsaCallAuthenticationPackage** approach

# BHASIA @BlackHatEvents

## Slide 35

###### Replicating the flow for another PRT Cookie theft

• Retrieved PRT Cookie allows us to gain access as a logged-on user

- To achieve the initial goal, we want to sign user’s logon request by Device key

- “SignPayload” function in aadcloudap looks interesting …

# BHASIA @BlackHatEvents

## Slide 36

###### Reversing aadcloudap!SignPayload

```
__int64 __fastcallGenericCallPackageHelper::SignPayload(
structAadContextFunctions*this,
structPluginState*pluginState_a2,
structCSecureString*payload_a3,
void*hToken_a4,
struct_AP_BLOB *accountInfo_a5,
structCSecureString*outBuffer_a6)
{
...
LODWORD(status_v28) = CheckPackageSidForRequestSign(this, hToken_a4);
...
LODWORD(status_v28) = BuildDeviceAuthAssertion(
this,
pluginState_a2,
payload_a3,
bKdf_v10,
assertion_v29);
```

# BHASIA @BlackHatEvents

## Slide 37

###### Reversing aadcloudap!SignPayload BuildDeviceAuthAssertion

Data sent by LsaCallAuthenticationPackage

```
{
"call": 1,
"payload": “
{
\"username\": \"employee01@************\",
\"password\": \"**********\"
\"request_nonce\": \"AwABAAEAAAACAOz_(snip)xqKRkgAA\",
(snip)
}"
}
```

Base64UrlEncode

Sign by Device key (dkpriv)

`. eyJhbGciOiJSUzI1NiIsICJ0eXAiOiJKV1QiLCA... eyAgICAidXNlcm5hbWUiOiAgImVtcGxve...` header payload

`eyJhbGciOiJSUzI1NiIsICJ0eXAiOiJKV1QiLCA... . eyAgICAidXNlcm5hbWUiOiAgImVtcGxve... . uIMsJz8dQAcT6SaiQpWiJAmgCzdkWy...` header payload signature **Data returned to a caller process**

# BHASIA @BlackHatEvents

## Slide 38

Reversing aadcloudap!SignPayload CheckPackageSidForRequestSign

- Checks if a caller process’s sid is “S-1-15-2-19100918851573563583-1104941280-2418270861-3411158377-28227009362990310272”

   - Without valid SID, BuildDeviceAuthAssertion is not called and SignPayload doesn’t generate Device key signed request

# BHASIA @BlackHatEvents

## Slide 39

Reversing aadcloudap!SignPayload CheckPackageSidForRequestSign

- The SID is for the AppContainer, AAD token broker

- With some tricks, we can impersonate this SID!

# BHASIA @BlackHatEvents

## Slide 40

###### Impersonate AAD token broker for Device key signing

Malware
Signed logon
request
AAD token broker
(S-1-15-2-191…)
Impersonate lsass.exe
RPC
LsaCallAuthenticationPackage
call number,
payload

aadcloudap.dll 1 SignPayload 2 CreateSSOCookie 3 GetPrtAuthority

1 SignPayload
2 CreateSSOCookie
3 GetPrtAuthority
4 CheckDeviceKeysHealth
・
・
・
15 GenerateBindingClaims

15 GenerateBindingClaims

# BHASIA @BlackHatEvents

## Slide 41

###### Send logon request signed by Device key

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 2024
Send logon request signed by Device key
POST /common/oauth2/token HTTP/1. 1
User-Agent: Mozilla/5.0 (Windows NT: Windows NT 10.0: ja-JP)
WindowsPowerShel 1/5. 1. 22621. 2506
Content-Type: app! ication/x-www-form-ur | encoded
Host: login. microsofton| ine. com
Content-Length: 2792
Connection: close
request=
KV1QiLCAi eDVj1 joi TU! JRDhqQONBdHF nOXdJOkFnSVF vVWSWSEwxc TF
SMEJBUXNGQURCNE 1 YWXdFUV1LO1pJbW I aUHIMR1IFCR1JZRGUtV jBNQ!
JSUZIINi Is 1CUO0eXAi0
MT kdaNHk5bORmKOS6QUSCZ2txaGtpk
signed logon request
JyPLSQQsqUIE7nvsiH6P7RYdD | BOsz5GdCPTZeSFsYEQ2C1 2haNJfMXehxmT 8uxR xmdkadgr YSf8pRsJgPh 2ts
xOSSFZWXJGF77B £0Z267 ImJut 0 jQe | RODKBxTe] TCOPNOhO jqOhoopbYDR| UUFCAVLaGLZCNR9y-yag
rWirtSF3BSYAVw19rz08 jQ&grant_type=urnS3AietfS3Aparamss3Aoauths3Agr ant—typeS3A jwt— bearer
HTTP/1.1 200 OK
Cache-Control: no-store, no-cache
Pragma: no-cache
Content-Type: application/json: charset=utf-8
Expires: -1
Strict-Transport-Secur ity: max-age=31536000; includeSubDomains
X-Content-Type-Options: nosniff
P3P: CP=“DSP CUR OTPi IND OTRi ONL FIN”
x-ms-request-id: 6a0e6251-b4f8-41f7-albf-bfb85f916d01
x-ms-ests-server: 2.1. 17396.8 - JPE ProdSlices
{
“token_type™ : “Be
“expires_in”:"12
“ext_expires_in
“expires_on” "1710549553
“refresh_token”
“0. ATOATMROZG6b200dRv6Bp | z96p jt2S | ppDZFreLSgbwdYF6hAPO. AgABAAEAAADnfo | hJpSnRYB1SV j-Hed8AgDs_wUA9P_1839cA6T_OZf90s8
PRT
OThSEUWsKwNoao2Kr_HuGkaSSN-OOCtbU3zpsLOGpkkAMGQWyDP INPZGTNyWcC_gaCLAG00cp | MavOOUAcSdypMW | 9tsE5M4 | TUYCeKLFLOMUOtMu6
LeQUhW-Bu j_xhY1_Jxz6rXpQoGqX i gYqApxow
“Td Loken
Ai Oi JKVIQILCUt
9
pted Session Key |
tCMnAFcbé
```

## Slide 42

###### Abusing aadcloudap for Device key signing

- We can sign arbitrary user’s logon request by Device key stored in TPM, thanks to internal aadcloudap loaded in lsass.exe

- The signed request gives us its user’s PRT & encrypted session key

- • For browser SSO access, we need to decrypt the encrypted session key by Transport key and sign the PRT with it

# BHASIA @BlackHatEvents

## Slide 43

###### Undocumented APIs to interact with session key

- cyrptngc.dll functions are imported in aadcloudap.dll

   - cryptngc.dll provides interface for device-stored cryptographic keys

# BHASIA @BlackHatEvents

## Slide 44

###### RPC Call for Your Needs

###### Caller process

encrypted session key DPAPI protected session key blob

NgcImportSymmetric PopKey

DPAPI protected session key blob & signing input NgcSignWithSymme tricPopKey

Session key signature

Ngc Pop Key Service (lsass.exe)

Decrypt by Transport key Session key blob Session key blob & TPM signing input Sign by session key

# BHASIA @BlackHatEvents

## Slide 45

###### Sign PRT with session key

- Undocumented APIs can import session key and decrypt it

- • Imported session key can be used  for signing

Sign by session key

`. eyJhbGciOiJSUzI1NiIsICJ0eXAiOiJKV1QiLCA... eyAgICAidXNlcm5hbWUiOiAgImVtcGxve...` header payload (PRT Included) `eyJhbGciOiJSUzI1NiIsICJ0eXAiOiJKV1QiLCA... . eyAgICAidXNlcm5hbWUiOiAgImVtcGxve... . uIMsJz8dQAcT6SaiQpWiJAmgCzdkWy...` header payload signature **PRT Cookie**

# BHASIA @BlackHatEvents

## Slide 46

###### Got Our Own PRT Cookie!

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pifeK hat x ——
ASIA 2024
x] JYYE JOY7b - powershell + v
PS C:\> Create-PRTCookie empLoyee01@ com $password
eyJhbGci0iJIUZIINiIsImtkZ192ZXIi0jIsImNOeCI6Lkw1UWZtMnZZR1IFYRTMWCUNOZWVJeE LNdUd2YnoyUj Lwin. ewOKICAgICJUX2NsawWVu
dF9wbGFOZm9ybSI6ICAid2LuZG93cyIsDQogICAgIndpbl92ZXIiOiAgI jEwL jAUMTKWNDEUMZU3MCISDQogICAgInJLZnJLc2hfdG9rZWw4idiAg
QUFFQUFBQUNBT3pfQLFEMF83N2LLbE10d09qe jRONMFiTzUzam9DSOJXZVFVNVRGSG1Ld1VVMHLiz2d4zjRZaWZUcjLIaFRiQK1UNDdYb2LhR2RI
Z3EzaUgyMEMZWkwOeHNVUNDBRWdBOSINCn@. uMisSwV3Mt 9nVOUMK6B209ESHXTMBULKAx8h1s54S7k
```

## Slide 47

###### Overview of the entire flow (Browser SSO)

1.Compromise corporate machine

2. Sign logon request by Device key using aadcloudap

5. Import session key to TPM and decrypt it by Transport key

6. Create PRT Cookie by session key

3. Send signed logon request

4. Receive PRT, encrypted session key

7. Send PRT Cookie from attacker’s machine for browser SSO

# BHASIA @BlackHatEvents

## Slide 48

###### Authentication Flow (App Tokens Requests)

• Session key signed PRT can also give us encrypted app tokens (access token / refresh token)

Device (win11pc01)

JWT containing PRT signed by session key

Microsoft Entra ID

App Tokens (encrypted)

# BHASIA @BlackHatEvents

## Slide 49

###### Decrypt app tokens with session key

- Encrypted app tokens can be decrypted by session key

- There is another undocumented API useful for us

# BHASIA @BlackHatEvents

## Slide 50

###### Decrypt app tokens by session key

**Access Token**

**Refresh Token**

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisdk hat e Sine.
ASIA 2024
Decrypt app tokens by session key
PS C:\> $tokens Acquire-Token empLoyee01@ .com 2 “d urn:ms-drs:enterpriseregistration.wind
ows.net 29d9ed98-a469-4536-ade2-f981bc1d605e $Tru
PS C:\> $tokens.access_token
eyJO0eXA101 IJKV1QILCIhbGci0i JSUZIINiIsIngidCI6ILhSdmtvOFA3ZQTNVYVdTbLU3ZYKO5b LQWTWpoQSIsImtpZCI6I LhSdmtvOFA3QTNVYVdTbLU3YkKO5b LQWTWpoQSJ9. eyJhd
WOi0iJlcm46bXMtZHIZOmVudGVvcHJnc2VvZWdoc3RVYXRob24ud2 LuZG93cv5uZXOiLCIJpc3Mi0iJodHRwezovL3NOcv53awSkb3dzLm5 LdC82NDUWN iRLZSO5Y iZLLTOZZGItowd
© 7HBOOEQVBtQ0aB1lChqxeUJLHKRFITihFpr6F70Nee52daEBMG-ZFQ9Vi8wsIMRHmILeTGLU jLmuj4AW_Mdb9HfrTDiJUXti_o88sMm1fXB1AGOH8ytDd_rEWZRzZZS8E33tdSxXgulD
ORhHEU7Loz—cqhxZADAEU7gfVNun8VgXbMDYEe9r-VJebWYLRFLyCrHCSwj YSENhcnSCq-jZKKV77zkqkisms2B407Q
PS C:\> $tokens.refresh_token
0. ATOA7MROZG6D200dRV6BpLz96pjt2S LppDZFreL5qbwdYF6hAPQ. AGABAAEAAADn Fo LhIpSnRYBISV ]—-Hgd8AgDs_wUA9P8xa3srMpPkKWNMFVLMOsWxSWJJc8OPVCILMULKAG j3bDE
Dre6éGuMtfvSzqPRLmvipjt_IMqDzeZtmC21mPbEjY_2wP_yTXJ_LKHFNq59 LumUeDauSdedIf3niMjBL8B3xYtaT27cFhH4qzEsxBookt_gOxVQG8pf9ow
```

## Slide 51

###### Attack TL;DR #1

- By abusing TPM stored keys, attackers can create PRT Cookie or acquire app tokens for arbitrary users with their credentials. • Administrator privilege is not needed for this attack

- Allows attackers to bypass Conditional Access policy based on device

# BHASIA @BlackHatEvents

## Slide 52

###### Explore more for “Passwordless”

- Found that other undocumented APIs allow us to interact with Windows Hello for Business (WHfB) keys stored in TPM

# BHASIA @BlackHatEvents

## Slide 53

###### Windows Hello for Business

• User key (ukpub/ukpriv) are registered to Microsoft Entra ID and allows user authentication without password

Device

dkpriv signed request containing ukpriv signed data

Microsoft Entra ID

PRT

Session key (encrypted)

# BHASIA @BlackHatEvents

## Slide 54

###### Authenticating with WHfB keys

###### dkpriv signed request

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 2024
Authenticating with WHfB keys
POST /common/oauth2/token HTTP/1. 1
User-Agent: Mozilla/5.0 (Windows NT; Windows NT 10.0: ja-JP) WindowsPowerShel 1/5. 1. 22621. 2506
Content-Type: app! ication/x-www-form-ur | encoded
Host: login. microsofton| ine. com
Content-Length: 3992
Connection: oloee JWT payload (decoded)
request= r
C JSUZIINi Is1CJO0eXAi0i JKVIQILCA TU! JRDhqQONBdH c VF QcmNZROFNRVRLa@E | SaE9YaENKZVh6QU5CZ2 txal {
pubW! aUHIMRIFCR1JZRGUtV jBNQ!VH vbVQ4aXhrQVUrVO bVJ2ZDNNdOhRWURWUVFERXhaT | VOMVB jbWRoYm1sN1! 1 YU} “username” emo!ovee(1 is
| “request_ nonce”
i’
W-o0ogN7VO1IM6
AUBA4MOOULOyOgP ‘
urnk3Aietf%3Aparams%3Aoauthh3Ag
dkpriv signed request
XCSqa6TUozLbaqXV tVT299X
BIXaSMjgrckA xSqAFMwXgm8
rant-type%3A jwt-bearer|
] TyXGMOCKHne | XHNef
7PRIC808NOsLB7Bszdlwev
x yXx-NSOXkPwRJQH7tA03G
68S30
T7ZwFhwOcY
At
AwABAAEAAAACA(
int
swBHYy89
“assertion”
0 IQEZ oa
Mi n6Mn MO"
{
“scope”
“win_ver™
“grant_typ
“client_id”
a” urn
C9n12g0Ka
ShgJhGERnWf_kSHhaDHv
GiNrVO&grant_type=
L
```

## Slide 55

###### Combining all together with WHfB

- Interacting with all the secret keys, we can authenticate to Entra ID with WHfB keys and create PRT Cookie without password

# BHASIA @BlackHatEvents

## Slide 56

- Combining all together with WHfB

- • Access token received by WHfB has deviceid and mfa claims

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Q
black hat
ASIA 2024
Combining all together with WHfB
¢ Access token received by WHfB has deviceid and mfa claims
fx) JYYK JOYTb - powershell x ap
PS C:\> $token = Acquire-Token empLoyee01@ : rue urn:ms-drs:enterpriseregistra
tion.windows.net 29d9ed98-a469-U536—ade2-F981bc1d605e
PS C:\> $token.access_token
ips Es seme tn a ce tet al Al Aa cl ald techn eater Re beh LLL ed age
bLOwTWpoQSJ9. eyJIhdwOi0iJlcmU6bXMtZHIzOmVudGVycHJpc2VyZWdpc3RyyX P
WS38Ka7LBoil8mkIkkm2XloetgMnbVcENkj Lb7—duRI4PsxEbR-T9DCtUmYt_roGGhXK4PpQNDL99Q3Yq jGY pBMF7q-kknBSM31JSMrBZn1yE01Q2dDKOWSu
o0s02fMuCBAXRy j4URIRTKLhHTbNHLo2QLdC7LFE_NSa_rsMZyrjK1OVS5V jRdCL j2zXUS3alqTrfBYwOExTmSw
```

## Slide 57

###### Attack TL;DR #2

- Attackers can create PRT Cookie or acquire app tokens through WHfB keys without password

- • Allows attackers to bypass Conditional Access policy based on device and MFA

- Needs to compromise other WHfB configured device for switching accounts

# BHASIA @BlackHatEvents

## Slide 58

#### Demo

# BHASIA @BlackHatEvents

## Slide 59

###### BAADTokenBroker

• PowerShell-based script for leveraging TPM stored keys to bypass Microsoft Entra ID Conditional Access

**Commands Description Request-PRTCookie** Request PRT Cookie of logged on user directly talking to lsass **Create-PRTCookie** Create PRT Cookie of any user with their credentials or WHfB keys Acquire access tokens and refresh tokens of any user with their **Acquire-Token** credentials or WHfB keys <u>https://github.com/secureworks/BAADTokenBroker</u>

# BHASIA @BlackHatEvents

## Slide 60

#### Mitigation

# BHASIA @BlackHatEvents

## Slide 61

###### Prevention

- Microsoft has responded this attack as an expected behavior

- • Strongly recommends to require MFA for all users with Conditional Access, not only require corporate device

   - This helps to make it harder for attackers to move laterally

   - between accounts with just passwords

# BHASIA @BlackHatEvents

## Slide 62

###### Detection

- Monitor suspicious RPC activity and cryptngc function calls

- • Investigate Entra ID sign-in logs of multiple accounts from the same device

```
SigninLogs
```

- `| where DeviceDetail.deviceId == “<suspicious_deviceid>“`

- `| where ResultType == 0`

- `| where AppId == “29d9ed98-a469-4536-ade2-f981bc1d605e” // Broker AppId`

# BHASIA @BlackHatEvents

## Slide 63

#### Conclusion

# BHASIA @BlackHatEvents

## Slide 64

###### Black Hat Asia Sound Bytes

- RPC calls and undocumented APIs allow attackers to interact with keys securely protected by TPM

- TPM stored keys can be abused for bypassing Entra ID Conditional Access once your corporate device is compromised

- • Review your Conditional Access policies to make it harder for attackers to pivot to the cloud and monitor suspicious activities

# BHASIA @BlackHatEvents

## Slide 65

## Q&A @TEMP43487580 @yuya-chudo-2601a596

#BHASIA @BlackHatEvents

## Slide 66

## Thank you

#BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
.
\—
® —
#BHASIA @BlackHatEvents
```

## Slide 67

###### Reference

- <u>https://learn.microsoft.com/en-us/entra/identity/devices/concept-primary-refresh-token</u>

- <u>https://learn.microsoft.com/en-us/windows/security/identity-protection/hello-for-business/how-it-works-authentication</u>

- <u>https://dirkjanm.io/digging-further-into-the-primary-refresh-token/</u>

- <u>https://dirkjanm.io/abusing-azure-ad-sso-with-the-primary-refresh-token/</u>

- <u>https://posts.specterops.io/requesting-azure-ad-request-tokens-on-azure-ad-joined-machines-for-browser-sso2b0409caad30</u>

- <u>https://aadinternals.com/post/deviceidentity/</u>

- <u>https://github.com/gentilkiwi/mimikatz</u>

- <u>https://github.com/dirkjanm/ROADtools</u>

# BHASIA @BlackHatEvents
