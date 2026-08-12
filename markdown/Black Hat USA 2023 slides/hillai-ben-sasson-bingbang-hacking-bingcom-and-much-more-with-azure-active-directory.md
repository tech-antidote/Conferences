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
text_chars: 16433
ocr_pages: 27
has_ocr: true
redacted_secrets: 0
ocr_confidence: 86.0
ocr_unreliable_blocks: 0
vision_verified_blocks: 3
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T04:10:39Z"
---
# BingBang Hacking Bing.com (and much more) with Azure Active Directory

**Speakers:** Hillai Ben-Sasson  
**Conference:** Black Hat USA 2023  
**Source:** `Black Hat USA 2023 slides/Hillai Ben-Sasson_BingBang Hacking Bing.com (and much more) with Azure Active Directory.pdf` (60 pages)


## Slide 1

Hillai Ben-Sasson @hillai


> Recovered by OCR — confidence 88/100 on the text kept, 67/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
WIZ Research
BE Microsoft Bing
Hacking Bing.com (and much more)
with Azure Active Directory
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


> Recovered by OCR — confidence 89/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
08 microsoftonline.com
Sign in
Email or phone
Can't access your account?
a4 Sign-in options
```

## Slide 10

## **OAuth login request**

Client

Server


> Recovered by OCR — confidence 82/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

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
```

## Slide 11

Client

Server

## **OAuth token response**


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 76/100 on the text kept, 71/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Factory Mode

[left panel]
public void onReceiveData(IIpcService.IpcMessageEvent ipcMessageEvent) {
    ...
    switch (c) {
        case 0:
            if (msgID == 1001) {
                String string = payloadData.getString(IpcConfig.IPCKey.STRING_MSG);
                if (!TextUtils.isEmpty(string)) {
                    c.b("SecurityCheckService", "onReceive-----> code = " + string);
                    if (this.f1165a.g(string)) {
                        c.b("SecurityCheckService", string + " isSecretKey.");
                        this.f1165a.a(string, getApplicationContext());
                        return;
                    } else if (com.car.devtools.a.c.c.a(string)) {
                        c.b("SecurityCheckService", string + " isFactoryCode.");
                        this.f1165a.b(string, getApplicationContext());
                        return;
                    } else {
                        return;
    ...

public boolean a(String str, String str2) {
    this.b = b.b(str);
    c.b("SecurityCheckPresenter", " verifySecretKey() mCateId:" + this.b);
    int e = e(this.b);
    if (e >= 50) {
        c.b("SecurityCheckPresenter", String.format(MyApplication.a().getString(R.string.text_
        return false;
    }
    return b.c(str2, str);
}

[right panel]
public static boolean c(String str, String str2) {
    if (TextUtils.isEmpty(str2)) {
return false;
    }
    String a2 = a(str, str2);
    com.xiaopeng.lib.b.c.a("FactoryCodeModel", "Current Code " + str2 + "'s mSecretKey is: " + a2);
    return str2.equals(a2);        check input
}

public static String a(String str, String str2) {
    return b(str, b(str2));
}

public static String b(String str, String str2) {
    if (TextUtils.isEmpty(str2)) {
        return "";
    }
    int i = 0;
    try {
        i = Integer.valueOf(str2).intValue();
    }
    catch (Exception e) {
        com.xiaopeng.lib.b.c.e("FactoryCodeModel", e.getMessage());
    }
    return a(str, i);
}

private static String a(String str, int i) {
    char[] charArray = str.toCharArray();
    int i2 = 0;
    for (int i3 = 0; i3 < charArray.length; i3++) {
        i2 = i2 + (charArray[i3] * i3 * 77) + i;
    }
    String format = new DecimalFormat("00000000").format(Math.abs(i2));
    if (format.length() > 8) {
        format = format.substring(0, 9);
    }
return "*#0000*" + i + "*" + format + "#*";
}

The code invokes factory mode authentication
```

## Slide 12

**AAD Flaws**


> Recovered by OCR — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

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


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 81/100 on the text kept, 67/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
TLSRpcRetrieveTermServCert

[Wireshark window: TLSRpcRetrieveTermServCert.pcap]
File  Edit  View  Go  Capture  Analyze  Statistics  Telephony  Wireless  Tools  Help
Apply a display filter ... <Ctrl-/>

No.     Time       Source           Destination      Protocol  Length  Info
14 0.004067   192.168.80.1     192.168.80.128   TCP         54 10207 -> 49674 [ACK] Seq=1 Ack=1 Win=1049600 Len=0
15 0.025550   192.168.80.1     192.168.80.128   DCERPC     166 Bind: call_id: 1, Fragment: Single, 1 context items: 3d267954-eeb7-11d1-b94e-00c04fa3080d V1.0 (32bit NDR), NTLMSSP_NEGOTIATE
16 0.025914   192.168.80.128   192.168.80.1     DCERPC     360 Bind_ack: call_id: 1, Fragment: Single, max_xmit: 4280 max_recv: 4280, 1 results: Acceptance, NTLMSSP_CHALLENGE
17 0.029656   192.168.80.1     192.168.80.128   DCERPC     163 AUTH3: call_id: 1, Fragment: Single, NTLMSSP_AUTH, User: \
18 0.046319   192.168.80.128   192.168.80.1     TCP         54 49674 -> 10207 [ACK] Seq=307 Ack=222 Win=65280 Len=0
19 0.046340   192.168.80.1     192.168.80.128   DCERPC      78 Request: call_id: 2, Fragment: Single, opnum: 1, Ctx: 0 3d267954-eeb7-11d1-b94e-00c04fa3080d V1
20 0.046552   192.168.80.128   192.168.80.1     DCERPC     102 Response: call_id: 2, Fragment: Single, Ctx: 0 3d267954-eeb7-11d1-b94e-00c04fa3080d V1
21 0.047508   192.168.80.1     192.168.80.128   DCERPC     106 Request: call_id: 3, Fragment: Single, opnum: 0, Ctx: 0 3d267954-eeb7-11d1-b94e-00c04fa3080d V1
22 0.047777   192.168.80.128   192.168.80.1     DCERPC      86 Response: call_id: 3, Fragment: Single, Ctx: 0 3d267954-eeb7-11d1-b94e-00c04fa3080d V1
23 0.049946   192.168.80.1     192.168.80.128   DCERPC     262 Request: call_id: 4, Fragment: Single, opnum: 34, Ctx: 0 3d267954-eeb7-11d1-b94e-00c04fa3080d V1
24 0.050221   192.168.80.128   192.168.80.1     DCERPC     110 Response: call_id: 4, Fragment: Single, Ctx: 0 3d267954-eeb7-11d1-b94e-00c04fa3080d V1
25 0.051342   192.168.80.1     192.168.80.128   DCERPC     150 Request: call_id: 5, Fragment: Single, opnum: 35, Ctx: 0 3d267954-eeb7-11d1-b94e-00c04fa3080d V1
26 0.057892   192.168.80.128   192.168.80.1     TCP       1514 49674 -> 10207 [ACK] Seq=443 Ack=602 Win=64768 Len=1460 [TCP segment of a reassembled PDU]
27 0.057924   192.168.80.128   192.168.80.1     TCP       1514 49674 -> 10207 [ACK] Seq=1903 Ack=602 Win=64768 Len=1460 [TCP segment of a reassembled PDU]
28 0.057935   192.168.80.1     192.168.80.128   TCP         54 10207 -> 49674 [ACK] Seq=602 Ack=3363 Win=1049600 Len=0
29 0.057963   192.168.80.128   192.168.80.1     DCERPC    1414 Response: call_id: 5, Fragment: 1st, Ctx: 0 [DCE/RPC 1st fragment, reas: #30]
30 0.058056   192.168.80.128   192.168.80.1     DCERPC     834 Response: call_id: 5, Fragment: Last, Ctx: 0 3d267954-eeb7-11d1-b94e-00c04fa3080d V1
31 0.058070   192.168.80.1     192.168.80.128   TCP         54 10207 -> 49674 [ACK] Seq=602 Ack=5503 Win=1049600 Len=0
32 0.059124   192.168.80.1     192.168.80.128   TCP         54 10207 -> 49674 [FIN, ACK] Seq=602 Ack=5503 Win=1049600 Len=0
33 0.059278   192.168.80.128   192.168.80.1     TCP         54 49674 -> 10207 [ACK] Seq=5503 Ack=603 Win=64768 Len=0

> Frame 29: 1414 bytes on wire (11312 bits), 1414 bytes captured (11312 bits)
> Ethernet II, Src: VMware_48:9a:20 (00:0c:29:48:9a:20), Dst: VMware_c0:00:01 (00:50:56:c0:00:01)
> Internet Protocol Version 4, Src: 192.168.80.128, Dst: 192.168.80.1
> Transmission Control Protocol, Src Port: 49674, Dst Port: 10207, Seq: 3363, Ack: 602, Len: 1360
> [3 Reassembled TCP Segments (4280 bytes): #26(1460), #27(1460), #29(1360)]
> Distributed Computing Environment / Remote Procedure Call (DCE/RPC) Response, Fragment: 1st, FragLen: 4280, Call: 5, Ctx: 0, [Req: #2   [line clipped by pane edge]

0f20  d0 61 ba 18 e3 c7 42 fa   44 5f a4 f6 c9 d5 3f 74   .a....B. D_....?t
0f30  99 38 bf f2 25 3d 4f de   12 da 4e ea 88 e8 68 cf   .8..%=O. ..N...h.
0f40  b6 74 e4 5b 7c f1 30 6b   a0 af 65 e7 2a 68 33 7c   .t.[|.0k ..e.*h3|
0f50  b2 0a a6 99 8c 86 b8 e4   9a 60 57 58 f5 12 50 58   ........ .`WX..PX
0f60  68 a0 a4 41 da 22 23 6a   75 15 75 a7 32 1a 04 00   h..A."#j u.u.2...
0f70  00 30 82 04 16 30 82 03   02 a0 03 02 01 02 02 05   .0...0.. ........
0f80  01 00 00 00 05 30 09 06   05 2b 0e 03 02 1d 05 00   .....0.. .+......
0f90  30 0e 31 0c 30 0a 06 03   55 04 03 13 03 63 63 63   0.1.0... U....ccc
0fa0  30 1e 17 0d 32 34 31 31   31 32 32 32 32 32 31 36   0...2411 12222216
0fb0  5a 17 0d 33 38 30 31 31   39 30 33 31 34 30 37 5a   Z..38011 9031407Z
0fc0  30 81 ac 31 81 a9 30 27   06 03 55 04 03 1e 20 00   0..1..0' ..U... .
0fd0  6e 00 63 00 61 00 63 00   6e 00 5f 00 69 00 70 00   n.c.a.c. n._.i.p.
0fe0  5f 00 74 00 63 00 70 00   3a 00 31 00 39 00 32 30   _.t.c.p. :.1.9.20
0ff0  39 06 03 55 04 07 1e 32   00 6e 00 63 00 61 00 63   9..U...2 .n.c.a.c
1000  00 6e 00 5f 00 69 00 70   00 5f 00 74 00 63 00 70   .n._.i.p ._.t.c.p
1010  00 3a 00 31 00 39 00 32   00 2e 00 31 00 36 00 38   .:.1.9.2 ...1.6.8
1020  00 2e 00 38 00 30 00 2e   00 31 30 43 06 03 55 04   ...8.0.. .10C..U.
1030  05 1e 3c 00 5a 00 57 00   56 00 6c 00 5a 00 57 00   ..<.Z.W. V.l.Z.W.
1040  56 00 6c 00 5a 00 57 00   56 00 6c 00 5a 00 57 00   V.l.Z.W. V.l.Z.W.
1050  56 00 6c 00 5a 00 57 00   56 00 6c 00 5a 00 57 00   V.l.Z.W. V.l.Z.W.
1060  56 00 6c 00 5a 00 57 00   55 00 3d 00 0d 00 0a 30   V.l.Z.W. U.=....0
1070  12 30 0d 06 09 2a 86 48   86 f7 0d 01 01 01 05 00   .0...*.H ........
1080  03 01 00 a3 82 01 f4 30   82 01 f0 30 14 06 09 2b   .......0 ...0...+
1090  06 01 04 01 82 37 12 04   01 01 ff 04 04 01 00 05   .....7.. ........
10a0  00 30 3c 06 09 2b 06 01   04 01 82 37 12 02 01 01   .0<..+.. ...7....
10b0  ff 04 2c 4d 00 69 00 63                             ..,M.i.c

[red annotation with arrow to the highlighted bytes at 0ff0-1030]  192.168.80.10

Frame (1414 bytes)   Reassembled TCP (4280 bytes)
TLSRpcRetrieveTermServCert.pcap        Packets: 47 - Displayed: 47 (100.0%)        Profile: Default
```

## Slide 14

**OAuth login request**


> Recovered by OCR — confidence 83/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

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
```

## Slide 15

**OAuth login request**


> Recovered by OCR — confidence 88/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
OAuth login request
{MY_TENANT_ID}
```

## Slide 16

**OAuth login request**


> Recovered by OCR — confidence 88/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
OAuth login request
{YOUR_TENANT_ID}
```

## Slide 17

\```
User    =  Hillai Ben-Sasson
Tenant  =Wiz Research
\```

## Slide 18

\```
User    =  Hillai Ben-Sasson
Tenant  =Your company here
\```

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


> Recovered by OCR — confidence 89/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
08 microsoftonline.com
Sign in
Email or phone
Can't access your account?
a4 Sign-in options
```

## Slide 30

Get Azure App Service domains Throw away non-existent apps Find AAD apps Filter multi-tenant configurations Log in


> Recovered by OCR — confidence 96/100 on the text kept, 96/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Get Azure App Service domains
Throw away non-existent apps
Find AAD apps
Filter multi-tenant configurations
Log in
```

## Slide 31


> Recovered by OCR — confidence 89/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
08 microsoftonline.com
Sign in
Email or phone
Can't access your account?
a4 Sign-in options
```

## Slide 32


> Recovered by OCR — confidence 78/100 on the text kept, 67/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

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
a name="LocLC" content="en-US"
a name="format-detection" content="telephone=no"
ript>
neta http-equiv="Refresh" content="0; URL=https://login.microsoftonline.com/jsdisabled"
name="robots" content=
script
cript type="text/javascript"
!function(){var e=window, r=e.$Debug=e.$Debug| |{}, . $Config| |{};if(!r.appendLog){var n=[],0=0;r.ap
(var c=u;c<arguments.length;c++){s.push(arguments[c])}t instanceof Array?e(t,i):i(t)},o.reg
r r=e.index0f("?"),t=r>-1?r:e. length,n=e. lastIndex0f(".",t);return e.substring(n,n+h.length).toLo
===a.length){ !0}}return!1}function c(){fur 1 t(e){g.getElementsByTagName( "head" )
h(e,t,n,o){if eturn f(e,t,n,o)}r("[$Loader]: "+(w.successMessage| | "Loaded"),0),v(e+
u.Load(null, function( ){if(o){throw"Failed to load external resource [' wey"y: (document .locatio
y.fbundle=null,delete y.fbundle,e.Add(y.bundle, "WebWatson_DemandLoaded"),e.Load(r,t),$=!0}}function
e.setRequestHeader( "Content-Type", "application/json; charset=UTF-8"),e.setRequestHeader( "canary"
"msg": "Failed to load external resource [Core Watson files]","url":o[1]||"","In":0,"ad":0, "an":
}fur 1 a(e,r,t,n,o,i,a){var s=v.event;r n i[|(i=l(o| |s,a?a+2:2)),v.$Debug&&v. $Debug. appendLog
freturn r}function d(e){if(!e){return null}try{if(e.stack){return u(e.stack)}if(e.error){if(e.error
var l=d(e);return 1&&(t.push(s(" Error Event Stack - -",01)), -concat(1l)),t}func
ion o(t){var n=null;return null= &(s=e(i,"$Config.urls")),null!==s& (n=e(s,t.toLowerCase
cript:
t type="text/javascript">
jone
```

## Slide 33

## Slide 34

Get Azure App Service domains Throw away non-existent apps Find AAD apps Filter multi-tenant configurations Log in


> Recovered by OCR — confidence 96/100 on the text kept, 96/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Get Azure App Service domains
Throw away non-existent apps
Find AAD apps
Filter multi-tenant configurations
Log in
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


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 79/100 on the text kept, 75/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Leak heap address

[Wireshark find bar]
Packet details v   Narrow & Wide v   [ ] Case sensitive   Hex value v   01 88 87 00 02 59        Find    Cancel

No.     Time        Source                   Destination      Protocol  Length  Info
25954 30.108300   192.168.80.128           192.168.80.1     DCERPC     110 Response: call_id: 8611, Fragment: Single, Ctx: 0 3d267954-eeb7-11d1-b94e-00c04fa3080d V1
25955 30.108964   192.168.80.1             192.168.80.128   DCERPC     150 Request: call_id: 8612, Fragment: Single, opnum: 35, Ctx: 0 3d267954-eeb7-11d1-b94e-00c04fa3080d V1
25956 30.111205   192.168.80.128           192.168.80.1     TCP       1514 51836 -> 12644 [ACK] Seq=9105663 Ack=3552662 Win=64768 Len=1460 [TCP segment of a reassembled PDU]
25957 30.111223   192.168.80.128           192.168.80.1     TCP       1514 51836 -> 12644 [ACK] Seq=9107123 Ack=3552662 Win=64768 Len=1460 [TCP segment of a reassembled PDU]
25958 30.111230   192.168.80.1             192.168.80.128   TCP         54 12644 -> 51836 [ACK] Seq=3552662 Ack=9108583 Win=131328 Len=0
25959 30.111235   192.168.80.128           192.168.80.1     DCERPC    1414 Response: call_id: 8612, Fragment: 1st, Ctx: 0 [DCE/RPC 1st fragment, reas: #25960]
25960 30.111401   192.168.80.128           192.168.80.1     DCERPC     834 Response: call_id: 8612, Fragment: Last, Ctx: 0 3d267954-eeb7-11d1-b94e-00c04fa3080d V1
25961 30.111411   192.168.80.1             192.168.80.128   TCP         54 12644 -> 51836 [ACK] Seq=3552662 Ack=9110723 Win=131328 Len=0
25962 30.113115   192.168.80.1             192.168.80.128   DCERPC     262 Request: call_id: 8613, Fragment: Single, opnum: 34, Ctx: 0 3d267954-eeb7-11d1-b94e-00c04fa3080d V1
25963 30.113249   192.168.80.128           192.168.80.1     DCERPC     110 Response: call_id: 8613, Fragment: Single, Ctx: 0 3d267954-eeb7-11d1-b94e-00c04fa3080d V1
25964 30.113941   192.168.80.1             192.168.80.128   DCERPC     150 Request: call_id: 8614, Fragment: Single, opnum: 35, Ctx: 0 3d267954-eeb7-11d1-b94e-00c04fa3080d V1
25965 30.116186   192.168.80.128           192.168.80.1     TCP       1514 51836 -> 12644 [ACK] Seq=9110779 Ack=3552966 Win=64512 Len=1460 [TCP segment of a reassembled PDU]
25966 30.116203   192.168.80.128           192.168.80.1     TCP       1514 51836 -> 12644 [ACK] Seq=9112239 Ack=3552966 Win=64512 Len=1460 [TCP segment of a reassembled PDU]
25967 30.116211   192.168.80.1             192.168.80.128   TCP         54 12644 -> 51836 [ACK] Seq=3552966 Ack=9113699 Win=131328 Len=0
25968 30.116217   192.168.80.128           192.168.80.1     DCERPC    1414 Response: call_id: 8614, Fragment: 1st, Ctx: 0 [DCE/RPC 1st fragment, reas: #25969]
25969 30.116342   192.168.80.128           192.168.80.1     DCERPC     762 Response: call_id: 8614, Fragment: Last, Ctx: 0 3d267954-eeb7-11d1-b94e-00c04fa3080d V1
25970 30.116355   192.168.80.1             192.168.80.128   TCP         54 12644 -> 51836 [ACK] Seq=3552966 Ack=9115767 Win=131328 Len=0
25971 30.834609   192.168.80.1             224.0.0.251      MDNS        85 Standard query 0x0000 PTR _microsoft_mcc._tcp.local, "QM" question
25972 30.834978   fe80::fd2a:a43e:65bf:30e1  ff02::fb       MDNS       105 Standard query 0x0000 PTR _microsoft_mcc._tcp.local, "QM" question

[WinDbg window]
Command - [tcp:server=192.168.80.128,port=12345] Process with service TermServLicensing -...
ModLoad: 00007ff8`11b00000 00007ff8`11b0b000   C:\Windows\System32\rasadhlp.dll   [row clipped by window top edge]
ModLoad: 00007ff8`1c800000 00007ff8`1c8a8000   C:\WINDOWS\System32\clbcatq.dll
ModLoad: 00007ff8`15d10000 00007ff8`15f4e000   C:\Windows\System32\msxml6.dll
ModLoad: 00007ff8`1acb0000 00007ff8`1acbc000   C:\WINDOWS\System32\CRYPTBASE.DLL
ModLoad: 00007ff8`1ad00000 00007ff8`1ad13000   C:\WINDOWS\System32\MSASN1.dll
ModLoad: 00007ff8`0c1c0000 00007ff8`0c1ce000   C:\WINDOWS\system32\tls236.dll
ModLoad: 00007ff8`1ac90000 00007ff8`1acac000   C:\WINDOWS\System32\CRYPTSP.dll
ModLoad: 00007ff8`1a5d0000 00007ff8`1a608000   C:\WINDOWS\system32\rsaenh.dll
ModLoad: 00007ff8`1b590000 00007ff8`1b5b4000   C:\WINDOWS\system32\profapi.dll
ModLoad: 00007ff8`1aab0000 00007ff8`1aadb000   C:\WINDOWS\system32\USERENV.dll
ModLoad: 00007ff8`1ae90000 00007ff8`1aec0000   C:\WINDOWS\System32\ncrypt.dll
ModLoad: 00007ff8`1ae40000 00007ff8`1ae7f000   C:\WINDOWS\System32\NTASN1.dll
ModLoad: 00007ff8`0f930000 00007ff8`0f95a000   c:\windows\system32\SAMLIB.dll
ModLoad: 00007ff8`11f50000 00007ff8`11fc8000   C:\WINDOWS\System32\ES.DLL
ModLoad: 00007ff8`10f60000 00007ff8`11053000   C:\WINDOWS\System32\PROPSYS.dll
ModLoad: 00007ff8`1a980000 00007ff8`1aa0b000   C:\WINDOWS\system32\msv1_0.DLL
ModLoad: 00007ff8`1a960000 00007ff8`1a977000   C:\WINDOWS\system32\NtlmShared.dll
(1f40.1db0): Break instruction exception - code 80000003 (first chance)
ntdll!DbgBreakPoint:
00007ff8`1e363440 cc              int     3
0:014> !heap
        Heap Address      NT/Segment Heap

    0000025987000000          Segment Heap

0:014>

0f00  c3 4e 8e 02 69 ca be fa   e9 d9 ef c9 1d fb b8 e2   .N..i... ........
0f10  49 b9 67 0a 6a 06 20 5b   da 23 76 43 dc 06 5d cb   I.g.j. [ .#vC..].
0f20  d0 61 ba 18 e3 c7 42 fa   44 5f a4 f6 c9 d5 3f 74   .a....B. D_....?t
0f30  99 38 bf f2 25 3d 4f de   12 da 4e ea 88 e8 68 cf   .8..%=O. ..N...h.
0f40  b6 74 e4 5b 7c f1 30 6b   a0 af 65 e7 2a 68 33 7c   .t.[|.0k ..e.*h3|
0f50  b2 0a a6 99 8c 86 b8 e4   9a 60 57 58 f5 12 50 58   ........ .`WX..PX
0f60  68 a0 a4 41 da 22 23 6a   75 15 75 a7 32 d2 03 00   h..A."#j u.u.2...
0f70  00 30 82 03 ce 30 82 02   ba a0 03 02 01 02 02 05   .0...0.. ........
0f80  01 00 00 10 17 30 09 06   05 2b 0e 03 02 1d 05 00   .....0.. .+......
0f90  30 0e 31 0c 30 0a 06 03   55 04 03 13 03 63 63 63   0.1.0... U....ccc
0fa0  30 1e 17 0d [obscured by red annotation]            [obscured]
0fb0  5a 17 0d 33 38 30 31 31   39 30 33 31 34 30 37 5a   Z..38011 9031407Z
0fc0  30 65 31 63 30 0d 06 03   55 04 03 1e 06 01 88 87   0e1c0... U.......
0fd0  00 02 59 30 0d 06 03 55   04 07 1e 06 01 88 87 00   ..Y0...U ........
0fe0  02 59 30 43 06 03 55 04   05 1e 3c 00 5a 00 57 00   .Y0C..U. ..<.Z.W.
0ff0  56 00 6c 00 5a 00 57 00   56 00 6c 00 5a 00 57 00   V.l.Z.W. V.l.Z.W.
1000  56 00 6c 00 5a 00 57 00   56 00 6c 00 5a 00 57 00   V.l.Z.W. V.l.Z.W.
1010  56 00 6c 00 5a 00 57 00   56 00 6c 00 5a 00 57 00   V.l.Z.W. V.l.Z.W.
1020  55 00 3d 00 0d 00 0a 30   12 30 0d 06 09 2a 86 48   U.=....0 .0...*.H
1030  86 f7 0d 01 01 01 05 00   03 01 00 a3 82 01 f4 30   ........ .......0
1040  82 01 f0 30 14 06 09 2b   06 01 04 01 82 37 12 04   ...0...+ .....7..
1050  01 01 ff 04 04 01 00 05   00 30 3c 06 09 2b 06 01   ........ .0<..+..
1060  04 01 82 37 12 02 01 01   ff 04 2c 4d 00 69 00 63   ...7.... ..,M.i.c
1070  00 72 00 6f 00 73 00 6f   00 66 00 74 00 20 00 43   .r.o.s.o .f.t. .C
1080  00 6f 00 72 00 70 00 6f   00 72 00 61 00 74 00 69   .o.r.p.o .r.a.t.i
1090  00 6f 00 6e 00 00 00 30   81 dd 06 09 2b 06 01 04   .o.n...0 ....+...

[red annotation, arrow from the highlighted "01 88 / 87 00" and "02 59" boxes to the WinDbg heap address]
0x025987000188 = 0x025987000000 + 0x188

Frame (1414 bytes)   Reassembled TCP (4280 bytes)
```

## Slide 39


> Recovered by OCR — confidence 70/100 on the text kept, 70/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
"appOwnerOrganizationId": "72f988bf-86f1-4laf-9lab-2d7cd011db47",
```

## Slide 40

**Microsoft findings**


> Recovered by OCR — confidence 79/100 on the text kept, 67/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Microsoft findings
* col -2.azurewebsites.net
* poli t.microsoft.com
«bin a.azurewebsites.net
* con ‘5.azurewebsites.net
* po -microsoft.com
* con -2.azurewebsites.net
* po .microsoft.com
* CO ‘ ‘ 1-2.azurewebsites.net
```

## Slide 41

#### **Microsoft findings**

- bingtrivia.azurewebsites.net


> Recovered by OCR — confidence 80/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Microsoft findings
* co -2.azurewebsites.net
* con ; -1.azurewebsites.net
¢ bingtrivia.azurewebsites.net
° m s.azurewebsites.net
* co v1-1.azurewebsites.net
* po -microsoft.com
* con -2.azurewebsites.net
* po -microsoft.com
° co 1-2.azurewebsites.net
```

## Slide 42

**Demo time**

## Slide 43

**Bing for Work**


> Recovered by OCR — confidence 90/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Bing for Work
LATEST FROM WIZ Show info from Wiz COD
Popular searches Coming up im Recent files a
me my office Q
Only users with permission will see your files and info. QO
Learn more See more See more
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


> Recovered by OCR — confidence 87/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Work for Bing
<script>
fetch("https://business.bing.com/api/v3/user/token/Substrate", {credentials: "include"})
.then((res) => res.json()).then( function(data){
console.log( User ID is ${data.user.id}, Tenant ID is ${data.tenant.id}° );
</script>
```

## Slide 47

## **But wait, there’s more**

## Slide 48


> Recovered by OCR — confidence 87/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

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
ABSTRACT
[ABSTRACTI] [HEADLINE1]
PROVIDER
LOGO
```

## Slide 49


> Recovered by OCR — confidence 91/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
SMARTBEAR
Centralized Notification Service (CNS) API“
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


> Recovered by OCR — confidence 86/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
@ swagger Select a definition
Contact Center API Gateway - Profile®
Profile Service APIs
AgentGroups Vv
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
BusinessSegments Vv
```

## Slide 51


> Recovered by OCR — confidence 88/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

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
© ‘© English 2 Geopolitical REMOVE
© ‘© English 2 Geopolitical REMOVE
Leave term
unchanged
English 2 Accessibility
REMOVE
Leave term
unchanged
English 2 Accessibility
REMOVE
```

## Slide 52


> Recovered by OCR — confidence 90/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

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
```

## Slide 53


> Recovered by OCR — confidence 93/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
@ Dashboard
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
Publish a
Preview Changes
f Status: Published Edit
® Visibility: Public
Update
Categories a
All Categories Most Used
Vv) Product updates
Developers
```

## Slide 54


> Recovered by OCR — confidence 87/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Storage Utilization for MSFT ® = ! 7
Cluster Filter: All / 08-CO3C / 09-CO3C / 11-CY2 / 12-CY2/14-CY2/15-CY/17-_ Data Access Time Window: 7d / 30d / 60d /
co 90d
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
