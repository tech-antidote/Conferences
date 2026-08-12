---
title: "So Long, and Thanks for All the Phish"
speakers: ["Harrison Sand Erlend Leiknes"]
conference: "DEF CON"
conference_full: "DEF CON 33"
edition: "33"
year: 2025
source_pdf: "DEF CON 33/Harrison Sand Erlend Leiknes - So Long, and Thanks for All the Phish.pdf"
pages: 88
sha256: "8e6ada6b62f1866dd206c5af4d0595ccd927a2b1ba50770e423aefba6f2519b0"
text_chars: 41802
ocr_pages: 69
has_ocr: true
redacted_secrets: 0
ocr_confidence: 86.9
ocr_unreliable_blocks: 3
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T07:02:51Z"
---
# So Long, and Thanks for All the Phish

**Speakers:** Harrison Sand Erlend Leiknes  
**Conference:** DEF CON 33  
**Source:** `DEF CON 33/Harrison Sand Erlend Leiknes - So Long, and Thanks for All the Phish.pdf` (88 pages)


## Slide 1


> Recovered by OCR — confidence 95/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
So Long, and Thanks for All
the Phish
The rise and fall of Darcula
Erlend Leiknes
Harrison Sand
```

## Slide 2


> Recovered by OCR — confidence 96/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Who are we?
Harrison & Erlend
Offensive security consultants
Work at mnemonic, a Norwegian
cybersecurity company
```

## Slide 3


> Recovered by OCR — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Where it started
= Erlend received an iMessage in December
2023
= The message was impersonating Posten, the
Norwegian postal service
= We got curious...
Posten:paakken ankom lageret, men
kunne ikke leveres pa grunn av
ufullstendig adresseinformasjon.
Vennligst bekreft adressen din i
lenken.
https://postens2no.shop/NO/
(Vennligst svar Y, avslutt deretter
tekstmeldingen og apne den igjen for
a aktivere lenken, eller kopier lenken
Og apne den i Safari-
nettleseren).Teamet @nsker deg en
fantastisk dag!
```

## Slide 4

## Slide 5


> Recovered by OCR — confidence 86/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Settings
Tools > Proxy Manage global settings
Enable disabled form fields
User Project z=
Remove input field length limits
Remove JavaScript form validation
Easy Remove all JavaScript
Remove <object> tags
Convert HTTPS links to HTTP
Intruder
Repeater
Remove secure flag from cookies
Sequencer
Burp's browser
> Project (0) HTTP match and replace rules - Project setting
Sessions
> Use these settings to automatically replace parts of HTTP requests and responses passing through the Proxy
> Network Only apply to in-scope items
we Useduitenace Add Enabled — Item Match Replace Comment
Inspector and message editor Edit Requestheader “User-Agent.*$ User-Agent: Mozilla/4.0 (com.. |-- Emulate IE
Hotkeys = Request header “User-Agent.*$ User-Agent: Mozilla/5.0 (iPho.. E Emulate iOS
ar Request header “User-Agent.*$ User-Agent: Mozilla/5.0 (Linux Emulate Android
> Suite Request header “If-None-Match.*$
Request header “Referer.*$
Request header “Accept-Encoding.*$
Display
Extensions
Configuration library
@) WebSocket match and replace rules Project setting
£9} Use these settings to automatically replace parts of WebSocket messages passing through the Proxy.
Only apply to in-scope items
Add Enabled Direction Replace Type Comment
Edit
Remove
Up
```

## Slide 6

## Slide 7


> Recovered by OCR — confidence 85/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
~ | @ Posten: Post- og fraktt x | +
€ G ://post.lol/NO/
Fraktstatus
Ditt pakkesporingsnummer: 330224219
Varsling om leveringsfell
¢ Pakken din ble ikke levert pa grunn av uklar leveringsadresse
¢ Pakken din har blitt returnert til vart oppfyllelsessenter
¢ Vennligst oppdater adressen din, sa sender vi igjen pa 9/2/2024
Fortsette
Sok etter Om oss Nyttig For bedrifter
Apningstider Om Posten Bring Falske SMS og e-post
Pakkebokser Jobb i Posten Priser
```

## Slide 8


> Recovered by OCR — confidence 95/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Deobfuscating the communication
```

## Slide 9


> Recovered by OCR — confidence 87/100 on the text kept, 69/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Burp Suite Community Edition v2024.5.3 - Temporary Project
Burp Project Intruder Repeater View Help
Dashboard Target Proxy Intruder Repeater Collaborator Sequencer Decoder Comparer Logger Organizer Extensions Learn
Intercept HTTP history ‘WebSockets history 6} Proxy settings
7 Filter settings: Hiding CSS, image and general binary content
# Host Method URL Para... Edited Status c.... Length MIME t... Extensi... Title IP Cookies Time
192.168.100.... 12:09:01
192.168.100.... 12:09:01
192.168.100.... 12:08:36
192.168.100.... 12:08:36
192.168.100.... 12:08:11
192.168.100.... 12:08:11
192.168.100.... 12:07:46
192.168.100.... 12:07:46
192.168.100.... 12:07:21
192.168.100.... 12:07:21
io/
200 214 text io/
200 229 text io!
200 214 text io/
200 229 text io/
200 214 __ text iol
200 214 text io/
200 229 text io/
200 229 text
200 214 text
200 229 text
200 214 text
8p
Original request v Response
Pretty Raw Hex & \n Pretty Raw Hex Render
POST /socket .io/?7EIO=4&t ransport=poll ing&t=P6YmXx8&sid=CiLT2h5j] 87AXzgd1L AAAI | 1 HTTP/1.1 200 OK
HTTP/1.1 2 Server: nginx/1.18.0 (Ubuntu)
Host: post.Lol 3 Date: Fri, 30 Aug 2024 10:08:36 GMT
Content-Length: 1 Content-Type: text/html
Sec-Ch-Ua: "Not/A)Brand";v="8", "Chromium"; v="126" Content-Length: 2
Accept: */* 5 Connection: keep-alive
Content-Type: text/plain;charset=UTF-8 Access-Control-Allow-Origin: *
Accept -Language: en-US 8 cache-control: no-store
Sec-Ch-Ua-Mobile: ?0 9
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, 9 ok
like Gecko) Chrome/126.0.6478.57 Safari/537.36
Sec-Ch-Ua-Platform: "Linux"
Origin: https://post.lol
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Referer: https://post .lol/NO/
Accept-Encoding: gzip, deflate, br
Priority: u=1, i
Connection: keep-alive
18
Event log (6)® All issues @ Memory: 229.6MB
```

## Slide 10


> Recovered by OCR — confidence 82/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Burp Suite Community Edition v2024.5.3 - Temporary Project
Burp Project Intruder Repeater View Help
Dashboard Target Proxy Intruder Repeater Collaborator Sequencer Decoder Comparer Logger Organizer Extensions Learn
Intercept HTTP history WebSockets history 6} Proxy settings
YY Filter settings: Showing all items
URL Direction Time Listener port WebSocket ID
12:13:57 30 Aug 2024 8080
12:13:57 30 Aug 2024 8080
12:13:32 30 Aug 2024 =. 8080
12:13:32 30 Aug 2024 8080
12:13:07 30 Aug 2024 8080
12:13:07 30 Aug 2024 =. 8080
12:13:07 30 Aug 2024 8080
12:13:07 30 Aug 2024 8080
https://post.lol/socket.io/ > To server
https://post.lol/socket.io/ € To client
https://post.lol/socket.io/ > To server
https://post.lol/socket.io/ € To client
https://post.lol/socket.io/ € To client
https://post.lol/socket.io/ € To client
https://post.lol/socket.io/ © To client
https://post.lol/socket.io/ > To server
https://post.lol/socket.io/ > To server 12:13:07 30 Aug 2024 8080
12:13:07 30 Aug 2024 8080
12:13:07 30 Aug 2024
12:13:07 30 Aug 2024
12:13:07 30 Aug 2024
https://post.lol/socket.io/ > To server
https://post.lol/socket.io/ > To server
https://post.lol/socket.io/ € To client
https://post.lol/socket.io/ > To server
Message
Raw Hex EJ in =
| 425["message",{'"msg":{"type":"824d02e7c f6ec64a44710b06ef8c fale", "data" : "U2ZFsdGVkX19IWH3V+KnWIdPj 2LF/wBhLj 4W/ rYovdJmHineTSuwIx fkSQyLyc rSfTyBEAai8R6yrLQnIcd3Ftj qDoXPyh9j 28
Event log (6)® All issues @ Memory: 232.5MB
=}
```

## Slide 11


> Recovered by OCR — confidence 93/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
What exactly is going on here?
= Developer is trying to obfuscate things
— Challenge accepted!
= “type” and “room” are 16-bytes of hex
— MD5?
= “data” is something that’s been Base64
encoded
— Decoding returned mostly garbage
— Contained the string “Salted”
— Probably encrypted
"msg": {
"type":
"data":
},
"user": [],
"21232£297a57a5a743894a0e4a801fc3"
```

## Slide 12


> Recovered by OCR — confidence 86/100 on the text kept, 73/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
@ Posten: Post- og Fraktt
Page Workspace >>
vO top
3ebd86c04NSQZ.js
DB) e9841a77cr7Qm.css
Navnet Ditt
f
Adresse
Gateadresse eller husnummer
Detaliert Adresse (Valafritt)
Paused in debugger
S Network Performance Memory Application Security Lighthouse Recorder DOM Invader
var 1Y
this['_doRese
function(Q9) {
return th
on() {
1o(@x156) ? Q8
return fi
ret
(QQ, Qb, QV, Qk);
1(QQ, Qb, QV, Qk);
function() {
1L
encrypt
€} Line 1, Column 55102
36ba9a1F4NSQZ.js »
»
Cancel
Coverage: n/a
@ Paused on breakpoint
» Watch
y Breakpoints
C) Pause on uncaught exceptions
© Pause on caught exceptions
¥ Scope
y Local
> Object
Qb: "{\"id
Qk
> Closure (G.<computed>.q.<computed>._createHelper)
> Closure
> Closure
> Closure
> Closure
> Module
> Global
y Call Stack
> encrypt
a30i.deep
Je
we
z
Je
Ks
Promise.then (async)
Us
vr
K
tr
$n
Window
```

## Slide 13


> Recovered by OCR — confidence 79/100 on the text kept, 68/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
D 4cd1ec68cr7Qm.css
[) beb21690cr7Qm.css
encrypt
{} Line 1, Column 55102
ar
‘process’: function(Q9) {
var 1R = 1L;
return this['_append'](Q9),
‘finalize’: function(Q9) {
var 1M = 1L;
Q9 && this [1M(@x1b8)](Q9);
var QQ = this[1M(@x231)]();
return QQ;
*_ENC_XFORM_MODE': @x1,
‘_createHelper': (function() {
function Q9(QQ) {
var lo = a3@b;
return typeof QQ == lo(@x156) ? QB : Q5;
‘fencrypt}' : function(Qb, QV, Qk) { Qb = "{\"id\":1, \"domain\":\"post.1o1\",\"ip\
}
Teturn function(QQ) {
return {
var lp = a3@b;
| return Q9(QV) [1p(@x1c4)](QQ, Qb, QV, Qk);
‘decrypt’: function(Qb, QV, Qk) {
var lx = a3@b;
return Q9(QV) [1x(@x28@)](QQ, Qb, QV, Qk);
}
}
‘_doFinalize': function() {
, Q9 = this[1N(@xlad)](!0x@);
a Cancel |
Coverage: n/a
y Breakpoints
C9) Pause on uncaught exceptio:
( Pause on caught exceptions
var a3@bc=a30b; (funct
vy Local
® this: Object
QV: “sync-data"
undefined
Ip: undefined
» Closure (G.<computed>.q.
» Closure
>» Closure
>» Closure
>» Closure
» Module
> Global
y Call Stack
> encrypt
a30i.deep
Je
we
Je
Ks
Promise.then (async)
Us
ve
K
Lr
$n
Gu
```

## Slide 14


> Recovered by OCR — confidence 73/100 on the text kept, 63/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
* @ Paused on breakpoint
» Watch
~ Breakpoints
(C Pause on uncaught exceptions
() Pause on caught exceptions
Var a3@bc=a30b; (function(b,k){var bw=a3@b,1=b() ;while(!![]){try{var S=-parseInt(bw(@x1a1) )/@x1+-parseInt (bw... 1
¥ Local
» this: Object
QV: "sync-data”"
Qe: "{\"idk":1,\"domain\":\"post.1o1\",\"ipv":4"192.168.108.169\" \"ua\":\"Mozilla/5.@ (iPhone; CPU iPhone OS 5_1 1i
Qk: undefined
Ip: undefined
>» Closure (G.<computed>.q.<computed>._createHelper)
> Closure
» Closure
» Closure
lJ » Closure
» Module
¥ Call Stack
we index-84805380.js:1
```

## Slide 15


> Recovered by OCR — confidence 86/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
decrypt_demo,js - Rabbit tools - Visual Studio Code
File Edit Selection View Go Run Terminal Help
JS decrypt_demo.js > ...
const CryptoJS = require("crypto-js");
5. const key = "sync-data"
a const ciphertext = "U2FsdGVkX19JWH3V+KnWIdPjzlF/wBhLj4W/rYovdJmHineTSuwlxfkSQyLycrSfTyBEAai8R6yrLQnIcd3FtjqDo)
iss const plaintext = CryptoJS.Rabbit.decrypt(ciphertext, key);
box@box:~/Desktop/Rabbit tools$ node decrypt demo.js
{"id":1,"domain":"post.lol","ip":"192.168.100.169","ua":"Mozilla/5.0 (iPhone; CPU iPhone OS 5 1 like Mac OS X) AppleWebKit/534.4
6 (KHTML, like Gecko) Version/5.1 Mobile/9B176 Safari/7534.48.3","data":{},"created at":"2024-08-30T10:07:20.907Z","updated at":
"2024-08-30T10:07:20.907Z"}
box@box:~/Desktop/Rabbit tools$ Jj
@)
```

## Slide 16


> Recovered by OCR — confidence 86/100 on the text kept, 61/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
"msg": {
"type": "824d02e7cf6ec64a44710b06ef8cfale",
"data":
},
"user": [],
"room": [
```

## Slide 17


> Recovered by OCR — confidence 90/100 on the text kept, 63/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
"msg": {
"type": "sync-data",
"data":
},
"user": [],
"room": [
```

## Slide 18


> Recovered by OCR — confidence 89/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
"msg": {
"type": "sync-data",
"data": "{"id":1,"domain":"post.lol", "ip":"192.168.100.169","ua":"Mozilla/5.0 (iPhone; CPU iPhone OS 5 1
like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B176
Safari/7534.48.3","data":{},"created_at":"2024-08-30T10:07:20.9072", "updated_at":"2024-08-30T10:07:20.9072"}
"user": [],
"room": [
```

## Slide 19


> Recovered by OCR — confidence 91/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
"msg": {
"type": "sync-data",
"data": "{"id":1,"domain":"post.lol", "ip":"192.168.100.169","ua":"Mozilla/5.0 (iPhone; CPU iPhone OS 5 1
like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B176
Safari/7534.48.3","data":{},"created_at":"2024-08-30T10:07:20.9072", "updated_at":"2024-08-30T10:07:20.9072"}
"user": [],
"admin"
```

## Slide 20


> Recovered by OCR — confidence 86/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Burp Suite Community Edition v2024.5.3 - Temporary Project = ah
Burp Project Intruder Repeater View Help
Dashboard Target Proxy Intruder Repeater Collaborator Sequencer Decoder Comparer Logger Organizer Extensions Leam &} Settings
Intercept HTTP history WebSockets history &} Proxy settings
Y Filter settings: Showing all items (Q)
# URL Direction Edited Length Notes TLS Time Listener port WebSocket ID
2410 https://post.lol/socket io/ > To server 1 v 16:21:49 30 Aug 2024 8080 31
2409 https://post.lol/socket-.io/ € To client 1 v 16:21:49 30 Aug 2024 8080 31
2408 https://post.lol/socket.io/ > To server 1 A 16:21:24 30 Aug 2024 8080 31
2407 https://post.lol/socket.io/ € To client 1 v 16:21:24 30 Aug 2024 8080 31
2406 https://post.lol/socketio/ To client 47 v 16:21:20 30 Aug 2024 8080 31
2405 https://post.lol/socket.io/ > To server 699 v 16:21:20 30 Aug 2024 8080 31
2404 https://post.lol/socket io/ To client 47 v 16:21:18 30 Aug 2024 8080 31
2403 https://post.lol/socket.io/ ~ To server 699 v 16:21:18 30 Aug 2024 8080 31
2402 https://post.lol/socket io/ © To client 47 v 16:21:17 30 Aug 2024 8080 31
2401 https://post.lol/socket-io/ > To server 699 v 16:21:17 30 Aug 2024 8080 31
2400 https://post.lol/socket.io/ © To client 47 v 16:21:07 30 Aug 2024 8080 31
2399 https://post.lol/socket.io/ ~ To server 699 v 16:21:07 30 Aug 2024 8080 31
2398 https://post.lol/socket.io/ € To client 47 v 16:21:05 30 Aug 2024 8080 31
Hex » | @ Posten: Post-og fraktti;: x | + =
Postadresse
Kjeere bruker, vennligst fyll ut skjemaet noye for a sikre vellykket omlevering.
fore €l(> : Navnet Ditt
Event log (8)® All issues
Adresse
Detaljert Adresse (Valgfritt)
```

## Slide 21


> Recovered by OCR — confidence 79/100 on the text kept, 56/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
"msg": {
"type": "824d02e7cf6ec64a44710b0b6ef8cfale",
"data":
t3Uc/50sePBu2C1N8MXeKI5GqBbpcl Pgu8cntWonbpv/LluzJpEQgjKi2RNMy7Ic73WEYiHRt 92iHeOMVn6YZCDVibYD60P+GT4FNJMibWfy
[
```

## Slide 22


> Recovered by OCR — confidence 90/100 on the text kept, 73/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
"domain": "post.lol",
"ip": "192.168.100.169",
"ua": "Mozilla/5.0 (iPhone; CPU iPhone OS 5 1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko)
Version/5.1 Mobile/9B176 Safari/7534.48.3",
"data": {
"fullName": "John Doe",
"address": "1234 Mai"
}
"updated _at": "Fri Aug 30 2024 16:22:12 GMT+0200 (Central European Summer Time)"
```

## Slide 23


> Recovered by OCR — confidence 90/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Burp = Project
Dashboard
Intercept
‘Y Filter settings: Showing all items
#
1212
1211
1210
1209
1208
1207
1206
1205
Intruder Repeater
Target
HTTP history
URL
https://post.lol/socket.io/
https://post.lol/socket.io/
https://post_lol/socket.io/
https://post.lol/socket.io/
Proxy
WebSockets history
Collaborator
€} Proxy settings
Direction
~ To server
> To server
€ To client
© To client
> To server
€ To client
€ To client
€ To client
Burp Suite Community Edition v2024.5.3 - Temporary Project
Sequencer Decoder Comparer Logger Organizer
Extensions
Learn
Time
15:09:02 30 Aug 2024
15:09:02 30 Aug 2024
15:09:02 30 Aug 2024
15:09:02 30 Aug 2024
15:09:02 30 Aug 2024
15:09:02 30 Aug 2024
15:09:02 30 Aug 2024
15:09:02 30 Aug 2024
Listener port
8080
8080
8080
8080
8080
8080
8080
8080
{} Settings
WebSocket ID
20
20
20
10
20
20
20
20
1204
https://post.lol/socket.io/
> To server
15:09:02 30 Aug 2024
8080
20
1203
1202
1201
4.900,
Message
1 423[ "message" ,{"action":"join","room":""}]
https://post.lol/socket.io/
https://post_lol/socket.io/
https://post.lol/socket.io/
Raw Hex
@ &l< >| | Search
Event log (8) ®
All issues
€ To client
~ To server
€ To client
15:09:02 30 Aug 2024
15:09:02 30 Aug 2024
15:09:02 30 Aug 2024
8080
8080
8080
20
20
20
on.
p 0 highlights
@ Memory: 297.9MB
sp
```

## Slide 24


> Recovered by OCR — confidence 86/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
‘Y Filter settings: Showing all items
# URL Direction Edited Length Notes TLS Time Listen
1212 https://post.lol/socket.io/ > To server 154 v 15:09:02 30 Aug 2024 8080
1211 https://post.lol/socket_io/ + To server 690 v 15:09:02 30 Aug 2024 8080
1210 https://post.lol/socket.io/ € To client 46 v 15:09:02 30 Aug 2024 8080
1209 https://post.lol/socket.io/ € To client 215 v 15:09:02 30 Aug 2024 8080
1208 https://post.lol/socket_io/ > To server 154 v 15:09:02 30 Aug 2024 8080
1207 https://post.lol/socket.io/ € To client 67 v 15:09:02 30 Aug 2024 8080
1206 https://post.lol/socket.io/ © To client 99 v 15:09:02 30 Aug 2024 8080
1205 https://post.lol/socket.io/ € To client 131 v 15:09:02 30 Aug 2024 8080
| 1204 https://post.lol/socket.io/ = To server 42 v 15:09:02 30 Aug 2024 8080
1203 https://post.lol/socket.io/ € To client f v 15:09:02 30 Aug 2024 8080
1202 https://post_lol/socket.io/ > To server 58 v 15:09:02 30 Aug 2024 8080
1201 https://post.lol/socket.io/ € To client 44 v 15:09:02 30 Aug 2024 8080
Message
Pretty Raw Hex
1 423["message",{"action":"join","room":""}]
@ > €/|>)| | Search
Event log (8) All issues
```

## Slide 25

## Slide 26


> Recovered by OCR — confidence 86/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Burp Suite Community Edition v2024.5.3 - Temporary Project
Burp Project Intruder Repeater View Help
Dashboard Target Proxy Intruder Repeater Collaborator Sequencer Decoder Comparer Logger Organizer Extensions Learn
Intercept HTTP history WebSockets history &) Proxy settings
VY Filter settings: Showing all items
# URL Direction Time Listener port WebSocket ID
17:37:36 30 Aug 2... 8080 36
17:37:36 30 Aug 2... 8080 36
17:37:11 30 Aug 2... 8080 36
17:37:11 30 Aug 2... 8080 36
17:37:02 30 Aug 2... 8080 36
17:37:01 30 Aug 2... 8080 36
17:37:00 30 Aug 2... 8080 36
17:36:58 30 Aug 2... 8080 36
17:36:58 30 Aug 2... 8080 36
17:36:46 30 Aug 2... 8080 36
17:36:46 30 Aug 2... 8080 36
17:36:21 30 Aug 2... 8080 36
17:36:21 30 Aug 2... 8080 36
2893 https://post_lol/socket.io/ > To server
2892 https://post.lol/socket.io/ € To client
2891 https://post.lol/socket.io/ > To server
2890 https://post_lol/socket.io/ To client
| 2889 https://post_lol/socket.iof © To client
2888 https://post.lol/socket.io/ € To client
2887 https://post.lol/socket.io/ € To client
2886 https://post.lol/socket.io/ © To client
2885 https://post_lol/socket.io/ > To server
2884 https://post.lol/socket.io/ > To server
2883 https://post.lol/socket.io/ € To client
2882 https://post_lol/socket.io/ > To server
2881 https://post_lol/socket.io/ € To client
Message
Raw Hex
@ & <€) [>| | Search ©) Ohighlights
Event log (8)° = Allissues @ Memory: 314.9MB
```

## Slide 27


> Recovered by OCR — confidence 89/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Telegram Founder Charged With Wide
Range of Crimes in France
el Durov, who was are sted near Paris over the weekend as
part of a broad inves igation into criminal acti ity on the platform,
also barred from leavi ¢ the country
A Jen reported from
(=) i) By Aurelien Breeden and Adam Satariano
a
Pavel Duroy, the Russian-born entre preneur who founded the
online communications tool Telegram, was charged on Wednesday
in France with a wide range of crimes for failing to prevent illicit
activity on the app, and barred from leaving the country
His indictment was a rare move by legal authorities to hold a top
technology executive pet onally liable for the behavior of users on
a major messaging platform, escalating the debate over the role of
tech companies in online speech, Privacy and security and the
limits of their responsibility
Mr. Durov, 39, was detained by French authoriti s on Saturday
after a flight from Azerbaijan. He v s charged on Wednesday W ith
complicity in managin online platform to enable illegal
transactions by an organized group, which could lead to a sentence
of up to 10 years in prison.
He was also charged with complicity in crimes such as enabling the
distribution of child sexual abuse material, drug traffic king and
```

## Slide 28

## Slide 29

## Slide 30

## Slide 31

## Slide 32

## Slide 33

## Slide 34


> Recovered by OCR — confidence 88/100 on the text kept, 88/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
SOS only @ 2:54 pm 9%):
< Accounts
Funds © Balance ©
$2,599,622.94 $2,599,622.94
Transactions Statements Notices
ili View your Spend Summary
Today 25 November 2023
Mobile Phone Banking
Funds Transfer 284949 i lease
Yesterday 24 November 2023
ANZ Internet Banking
Funds Tfer Transfer
253042 To -$30,000.00
012403351154685
Sunday 19 November 2023
ANZ Internet Banking Funds
Tfer Transfer 799854 From $10.00
550576442 ~
```

## Slide 35

## Slide 36

## Slide 37

## Slide 38


> Recovered by OCR — confidence 92/100 on the text kept, 58/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
curl https://deploy.magic-
cat.world/i
chmod +x
install.sh
nstall.sh -o install.sh &&
install.sh && sudo ./
```

## Slide 39

## Slide 40


> Recovered by OCR — confidence 87/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
@ post.lol/li6c7LLyDc/#
Welcome back!
Who are you?
```

## Slide 41

## Slide 42

## Slide 43


> Recovered by OCR — confidence 71/100 on the text kept, 53/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
index.js - mc_code - Visual Studio Code
Go Run Terminal Help
mowiahs _@x2801lef:Oxlcd, Ox5aaae6:0x252, 0x16565a:0x264, 0x1f5114:0x24a, 0x261dd5:0x230, 0x352e71:0x214, Oxlda5bc:0x25c, 0x285c74:0x233,
£5 4S commonjs _0x340e01, 0x28c) ) /( -Oxla6a+-0x26e6+-0x4151*- 0x1) *(parseInt(_Ox2d6d5e(0x26e,a3_Ox1fS5a2d. Oxcf1225,a3_Ox1f5a2d. 0x91056e,0x22c))/
(a3_0x31ca['xlvQfG' ]===undefined) {var _@x25bfa9=function(_0x144010) {const
+0x34a*Oxc) ) - (Ox8c*Ox6+-Oxb77* -0x1+0x5*-Ox2f1) !==0x1862+0x1aa3+-0x3305?String['fromCharCode' ] (0x1554+-0x5*-0x6al+-0x357a& @x4bd21a>>
const 0x52acfa=_0x424b3a[Oxab*0x29+0x1*Oxdb1+0x1*-0x2914], Ox46df16= 0x4688c6+ Ox52acfa, Ox21lee3=_0x1745le[_0x46df16] ;if
\x20*{\x5cw+\x20*', this[ 'DLKUIo' ]=' [\x27|\x22] .+[\x27|\x22] ; ?\x20*}';};_0x44b096['prototype' ] [ 'UENKaY' ]=function(){const
0 0 ‘0 Ln1,Col1 Spaces:4 UTF-8 LF JavaScript
```

## Slide 44


> Recovered by OCR — confidence 85/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
JavaScript Obfuscator Tool
A free and efficient obfuscator for JavaScript (including support of ES2022), Make your code
harder to copy and prevent people from stealing your work. This tool is a Web UI to the
excellent (and open source) javascript-obfuscator@4.e.@ created by Timofey Kachalov.
Releases 218
Copy & Paste JavaScript Code
Upload JavaScript File Output
// Paste your JavaScript code here
function hi() {
eum }
Packages
ao
peau © : : 4 5e 4 Strings Identifiers Other
Sm HE Reset options
Transformations Transformations Transformations
Languages
Options Preset
String Array Identifier Names Generator v Compact
Default
String Array Shuffle
Target
Transform Object Keys
String Array Threshold
Browser
0.75
Numbers To Expressions
```

## Slide 45


> Recovered by OCR — confidence 90/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
README
synchrony
Usage note
```

## Slide 46


> Recovered by OCR — confidence 78/100 on the text kept, 70/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
common.cleaned.js - mc_code - Visual Studio Code
File Edit $s tion View Go Run Terminal Help
veccowe [FO @ JS common.cleaned.js > © app.all('/api/can-active/-action/:key?’) callback
O \ admin app.all('/api/can-active/:action/: async (_@x5e7d85, _Ox3ad4cd) => {
48 curdjs return _@x3ad4cd.send(_0x5620e8) ;
JS index.cleaned,js } catch (_0x5b5b46) {
N JS index.js return _@x3ad4cd.send({
JS index.cleaned.js 314 }
JS index.js } else {
JS utilcleanedjs if (_0x5e7d85.method === 'POST') {
JS utiljs if (_@x5e7d85.hostname !== new URL(env_1.ENV.ACTIVE SERVER) .hostname) {
return _0x3ad4cd.sendStatus (404) ;
JS common.cleaned.js
}
JS envjs ‘check-current',
JS index.cleaned.js ‘apply’,
JS site.cleaned js ].includes(_0x506db5)) {
: : const _0x169332 = {};
SIRE return _0x169332.code = -404, _0x169332.msg = 'SHA{THWiB(ERE!', _Ox3ad4cd.send(_0x169332);
JS_utils.cleaned.js }
4S utils.js const 0x502d7a = { activeKey: 0x3e698a };
const _0x353868 = { where: 0x502d7a };
let _0x441b1f = await _1.prisma.active. findUnique(_0x353868) ;
if (!_0x441bif) {
const _0x562cc8 = {};
return _0x562cc8.code = 404, _@x562cc8.color = 'red', _0x562cc8.msg = ', _Ox3ad4cd.send(_0x562cc8) ;
}
=~ if (_0x441b1f.expire <n Date()) {
Q) return _@x3ad4cd.send({
‘code': 403,
~ > TIMELINE 'msg': '4aufIewkAF ' + new Date(_0x441b1f.expire) .toLocaleString('zh')
```

## Slide 47


> Recovered by OCR — confidence 95/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Lab network
post.lol
Magic Cat
software
auth.magic-
cat.world
```

## Slide 48

## Slide 49


> Recovered by OCR — confidence 87/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Intruder Repeater View Help
Burp = Project
Dashboard
mm +
Target Proxy Intruder Repeater Collaborator
Request
Pretty Raw Hex
POST fapi/admin/list/logger HTTP/1.1
Host: post.lol
Content-Length: 65
Sec-Ch-Ua: "Not/A)Brand"; 7
Accept-Language: en-US
Sec-Ch-Ua-Mobile: 70
"Chromium"; v="126"
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppLeWebKit/537.36 (KHTML, Like Gecko)
Chrome/126.0.6478.57 Safari/537.36
Content-Type: application/json
Accept: application/json, text/plain, */*
Sec-Ch-Ua-Platform: "Linux"
Origin: https://post.lol
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Accept-Encoding: gzip, deflate, br
Priority: u=l, i
"where": {
},
"skip":0,
Done
Event log (2)° All issues
Sequencer
Decoder
Burp Suite Community Edition v2024.5.3 - Temporary Project
Comparer Logger Organizer Extensions Learn
Response
Pretty Raw Hex
HTTP/1.1 200 OK
Server: nginx/1.18.0 (Ubuntu)
pu
sp
8 w
Date: Sat, 31 Aug 2024 12:05:21 GMT
Content-Type: application/json; charset=utf-8
Connection: keep-alive
Vary: Accept-Encoding
Access-Control-Allow-Origin: *
X-Powered-By: Express
ETag: W/"88c-wMUfkCL8RZZKEBs /qg/mNdyBhbk *
Content-Length: 2188
{
"success": true,
{
"type": "not-found",
"info":{
"ip":"192.168.100.169",
"id':4,
"type": "not-fou
“ip":"192. 168.100. 1€
Search
©) Ohighlights
10.0; Win64; x64) AppleWebKit/537.36 (KHTML, Like Gecko) Chrome/126.0.64
NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, Like Gecko) Chrome/126.0.64
2,489 bytes | 46 millis
@ Memory: 206.1MB
```

## Slide 50


> Recovered by OCR — confidence 86/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Burp Suite Community Edition v2024.5.3 - Temporary Project
Burp Project Intruder Repeater View Help
Dashboard Target Proxy Intruder Repeater Collaborator Sequencer Decoder Comparer Logger Organizer Extensions Learn {@} Settings
sp
Request Response
Pretty Raw Hex = Pretty Raw Hex
POST /api/admin/list/logger HTTP/1.1 1 HTTP/1.1 401 Unauthorized
Host: post. Lol 2 Server: nginx/1.18.0 (Ubuntu)
Content-Length: 65 3 Date: Sat, 31 Aug 2024 12:05:35 GMT
Sec-Ch-Ua: "Not/A)Brand"; ", "Chromium"; v="126" Content-Type: application/json; charset=utf-8
Accept-Language: en-US 5 Content-Length: 31
Sec-Ch-Ua-Mobile: 70 6 Connection: keep-alive
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppLeWebKit/537.36 (KHTML, Like Gecko) Access-Control-Allow-Origin: *
Chrome/126.0.6478.57 Safari/537.36 8 X-Powered-By: Express
Accept: application/json, text/plain, */* 0
Sec-Ch-Ua-Platform: "Linux"
Origin: https://post.lol
Sec-Fetch-Site: same-origin "msg": "need Login"
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://post.lol/lI6c7LLyDc/
Accept-Encoding: gzip, deflate, br
Priority: u=1l, i
"where": {
"skip":0,
“orderBy":[
316 bytes | 1,044 millis
Event log (2)° All issues @ Memory: 209.1MB
```

## Slide 51


> Recovered by OCR — confidence 85/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Burp Suite Community Edition v2024.5.3 - Temporary Project
Burp Project Intruder Repeater View Help
Dashboard Target Proxy Intruder Repeater Collaborator Sequencer Decoder Comparer Logger Organizer Extensions Learn {@} Settings
sp
Request Response
Pretty Raw Hex = Pretty Raw Hex \n
TP/1.1 HTTP/1.1 200 OK
Host: 127.0.0.1 2 Server: nginx/1.18.0 (Ubuntu)
Content-Length: 6! Date: Sat, 31 Aug 2024 12:06:11 GMT
Sec-Ch-Ua: "Not/A)Br : » "Chromium"; v="126" 4 Content-Type: application/json; charset=utf-8
Accept-Language: en-U: 5 Connection: keep-alive
Sec-Ch-Ua-Mobile: 70 6 Vary: Accept-Encoding
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, Like Gecko) 7 Access-Control-Allow-Origin: *
Chrome/126.0.6478.57 Safari/537.36 3 X-Powered-By: Express
Content-Type: application/json 9 ETag: W/"88c -wMUfkCL8RZZKEBs/qg/mNdyBhbk "
Accept: application/json, text/plain, */* 0 Content-Length: 2188
Sec-Ch-Ua-Platform: "Linux"
Origin: https://post.lol 2\{
Sec-Fetch-Mode: cors "data": [
Sec-Fetch-Dest: empty {
Referer: http://localhost:5174/ "“id":5,
Accept-Encoding: gzip, deflate, br "type": "not-found",
s NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, Like Gecko) Chrome/126.0.64
78.57 Safari/
},
"id's
“Label":" i
10.0; Win64; x64) AppleWebKit/537.36 (KHTML, Like Gecko) Chrome/126.0.64
Done 2,489 bytes | 52 millis
Event log (2)° All issues @ Memory: 209.1MB
```

## Slide 52


> Recovered by OCR — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Darcula’s infrastructure
« All centralized infrastructure is behind
Cloudflare
— Backdoor won't work
= We know the license server is a gold mine
— Database of all activations
— Includes IPs
— Maybe more?
= Netcraft blogged about Darcula in March 2024
— Simultaneous takedown of Darcula’s magic-cat.net
domain
— Back up and running within hours
# License server
auth.magic-cat.world
# Installation files
deploy.magic-cat.world
# Docker registry (Harbor)
registry.magic-cat.world
# Phishing kit server
pages.magic-cat.world
```

## Slide 53

## Slide 54


> Recovered by OCR — confidence 79/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
4% SHODAN Explore Downloads Pricing @ “Not Found" “nginx/1.18.0" “Access-Control-Allow-Origin: *" “Content-Len
Account
vi View Report &% Download Results lt Historical Trend {0 ViewonMap Q Advanced Search
Partner Spotlight: Looking for a Splunk alternative to store all the Shodan data? Check out Gravwell
188.126.71.226 2
eer ae © SSL Certificate HITP/1.1 404 Not Found
a an Issued By: Server: nginx/1-18.@ (Ubuntu)
| Common Name Date: Sat, 31 Aug 2624 12:57:17 GMT
R10 Content-Type: text/plain; charset-utf-8
Content-Length: 9
Lees Bncijat Connection: keep-alive
‘Sweden, Falkenborg
X-Powered-By: Express
Issued To cess-Control-Allow-Origin: *
United States Common Name: ETag: W/"9-0gXLIngzMqISxaGSizx3Fawtl yg"
spark paylio.se
China ‘Supported SSL Versions:
Germany TLSv1.2, TLsv1.3
Netherlands
Singapore 185.15.199.204 [7
© SSL Certificate HITP/1.1 484 Not Found
Issued By Server: nginx/1.18.@ (Ubuntu)
| Organization Date: Sat, 31 Aug 2024 12:33:07 GHT
CloudFlare, Ine. Content-Type: text/plain; charset=utf-8
Connection: keep-alive
More...
| Common Nam
CloudFlare Or Vary: Origin
Access-Control-Allow-Origin: *
| Organization
CloudFlare, Ine.
Supported SSL Versions.
176.58.99.117 (7
P ORGANIZATIONS 17 ip linodeuserconte @ SSL Certificate HITP/1.1. 404 Not Found
Amazon Technologies Inc. in Dote: Sat, 31 Aug 2024 12:20:59 Gir
Aliyun Computing Co.LTD ; Es Content-Type: text/plain; charset-utf-8
Content-Length: 9
DigitalOcean, LLC SE United Kingdom, London Let's Encrypt ‘onnection: keep-alive
Google LLC Issued To Vary: Origin
| Common Name: Access-Control-Allow-Credentials: true
Amazon Data Se apiforest-deviuk Content-Secur....
More... Supported SSL Versions:
```

## Slide 55


> Recovered by OCR — confidence 82/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
SHODAN Explore Downloads Pricing
442.171.242.231
// TAGS: // LAST SEEN: 2024-08-29
® General Information s& Open Ports
Country United States | 22 | | 0 |
City Los Angeles
Organization MULTACOM CORPORATION
SSH-2.0-OpenSSH_8.9p1 Ubuntu-3ubuntud.10
ASN AS35916 Key type: ecdsa-sha2-nistp256
Operating System Linux Fingerprint: Se:9a:51:5e:36:a3:33:4e:7d:78:53:c@:0a:98:bd:38
Kex Algorithms:
curve25519-sha256
ecdh-sha2-nistp256
ecdh-sha2-nistp384
ecdh-sha2-nistp521
sntrup761x25519-sha512@openssh.com
diffie-hellman-group-exchange-sha256
diffie-hellman-group16-sha512
diffie-hellman-group18-sha512
diffie-hellman-group14-sha256
Server Host Key Algorithms:
rsa-sha2-512
rsa-sha2-256
ecdsa-sha2-nistp256
ssh-ed25519
```

## Slide 56


> Recovered by OCR — confidence 76/100 on the text kept, 70/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
800.618.4628
IN HOSTING PERFORMANCE : ==:==
24 x 7 NOC & Technical Support — Cost-Effective Solutions — isa i bs ~ =>
Feature Packed Plans — Reseller Options ft = =
=
==
LEARN MORE >
```

## Slide 57

## Slide 58


> Recovered by OCR — confidence 83/100 on the text kept, 67/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
File Edit Encoding
Search View Language Settings
Tools
bc02757a-dbeb-43
bbd9-a4cabdleé3a2
e5a1-481b-9740- feelale196c7
-08d7-4450-a5f8 6
faabaabb-0fe7-43ab-8357 4ea815b68
bfaafa00-3£0a-430 7d4-eb74d6eb0e7e
1
2
2
2
2
3
d-9
2 875-£14b467
£5176403-4£d2-4809-afa2-71c5a087b280
b2e-c343-4£55-8430-41bfa2e5e274
2023-10-30T11:12:38.553000+0000 2024
10-30T12
OTOO
//t.me/kaolalaqu 2023-11-06T(¢
2023
2023
2023-11-13T0 0
2023-11-13T00
2023-11-13T00
2023-11-29T
2023-11-13T
2023-11-24T00
2023-12
00:00.0002
00
0T12:40:
00.0002
0T13:13
2023-10-30T13:14:
00.0002
430000+0000 2023-11-30T07:28:37.702000+0000 142.
2023-10-3
48.9970
2023-10 1
3:02:40.12701
2023-10-30T1
2023- 3
2023-10-30T1
2023-10-.
0000 202
0000 202
2023-10-30
1
2023-10-30T1
ak
2023-10-30T15
2023-10-. 30T12:
=05-16T06:43:11.685000+0000 142.
39:04.859000+0000 2023-10-30T12:45:11.184000+0000
+0000
-430000+0
27T05:55
862000+0
00 38.60.134.32
(0 2023-11-30T07 45.77.167.230
21.137000+0000 2023-12-03T17:25
+0000 2023-10-30T13:
+0000 2023-11-01707 00
0
-257000+0000 2023-11-17T11:49:
+0000 2024-01-
0 2023-11-15T09:23:
07.484000+0000 208.
353.
2023-10-30T1
OT15:
30T1 0 0 7
2023-10-31T04:
2023-
2023-10
2023-10-31T0O
2023-10-31T
2023-10-.
2023-10-31
1T
2023-10-31T07:
1:34:54.2 0
4.276000
52.288
+0000
0040000 2023-12
-351000+0000 2023-10-31
+0000 2023-10
890000+000"
2023-12-14T09:22:42.645000+0000
2023-10
45.76.1
30T12:3
3.238
4:27.684000+0000 -6
2023-10-30T12:45:11.
2023-10-31T14:49:06.224000+0000
98.137.77
9000+0000 45.
2023-11-08T05:40:
3.673000+0000 66.103.207.164
+0000 §
2023-11-04T10 41.
2023-11-28T12:12:41.0
65.232.
3.198
208.167.
66.103
8.127.
43.
146.81
137.77
218
43
82
153.23 .1
74.130
49.51.186.2
192.161.
00+0000 192.161.161.136
54.6.
43.130
00
165.123
242
44,24
s/0O 108.61. 147.
245
2023-10-30T13:37:
2023-11-01T11:53:41.8
2023-10-30T13:3
2023-10-30T18:09:1
2023-10
43
2023-11-18T1
2023
2023-10-31T11:
2023-11-21T08:
2023 -31T11:
2023-11-11T14:
2023-11-12T10:
2023-10-31T14:
Normal text file
“7 lines : 5,436
7.128000+0
183000+000
18.080000+0000 4
10
000+0000 10
0000
Unix (LF)
UTF-8
```

## Slide 59


> Recovered by OCR — confidence 95/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Good time to inform the police
= Compiled a 24-page report and shared with
— Norwegian National Cybercrime Centre (NC3)
— The National Authority for Investigation and
Prosecution of Economic and Environmental Crime
— Europol
— FBI
= Held meetings with Europol in The Hague,
twice
```

## Slide 60


> Recovered by OCR — confidence 81/100 on the text kept, 61/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
"type": "not-found",
"info": {
"ip": "47.242.121.133",
"ua": "Mozilla/5.0 (iPad; PU OS 17.2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko)
CriOS/120.0.6099.119 Mobile/15E148 Safari/604.1",
"host": "auth.magic-cat.net",
"domain": "auth.magic-cat.net/MdhQXmRj7M/assets/index-ec2973c0.js",
```

## Slide 61


> Recovered by OCR — confidence 82/100 on the text kept, 59/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Shelter Town Island
Siu Pai
Chau
// LAST SEEN: 2024-08-31
® General Information 2 Open Ports
Cloud Provider Alibaba Cloud
Country Hong Kong
City Hong Kong 8 | 2024-08-31TO1:32:03.623375
Organization Alibaba Cloud LLC OpenSSH 8291 Ubuntu-4ubuntu0.1
SSH-2.0-OpenSSH_8.2p1 Ubuntu-4ubuntud.1
ISP Alibaba (US) Technology Co., Ltd. Key type: ssh-rsa
ASN AS45102 eVF8Pr3nYLbWO01d25#Mha7 1q6HOY709YAnfBcISsozrRR@drYAT7tDHEzVdsest7kSMsObTx5GU
Operating System Ubuntu EJGNb+s1Lwg8RIfIBsusa5u+59mwP1SxiS7yatagMbyOVvHyWJ /OXIxWZF 2HCp9cu+3hq8RGNdGi
agf8kDuYV/8=
Kex Algorithms:
curve25519-sha256
curve25519-sha256@libssh.org
ecdh-sha2-nistp256
ecdh-sha2-nistp384
ecdh-sha2-nistp521
diffie-hellman-group-exchange-sha256
```

## Slide 62


> Recovered by OCR — confidence 92/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Record type
legsec.net
Search ...
47.242.121.133
Answer
47.242.121.133
First seen
2022-12-2
2022-08-25 20:42
2022-06-27 08:10
Showing:
History
47.242.121.133
11 seconds ago
```

## Slide 63


> Recovered by OCR — confidence 89/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
History
if-she.com x
10 seconds ago
hk.if-she.com x
15 seconds ago
47.242.121.133 x
3 minutes ago
Search
if-she.com
Record type Query Answer First seen Last seen \
if-she.com 15.197.192.55 2024-03-08 2 2024-04-10 22:56
ifshe.com 91.195.240.94 2021-03-09 1 2022-08-26 06:14
cname if-she.com trizau.github.io 2021-07-13 22:45 2022-05-17 01:38
cname i e00go.github.io 2020-07-14 09:55 2021-05-14 23:42
if-she.com 8.210.88.222 -07-14 10:59 2020-07-14 10:59
if-shi 47.240.54.146 3-22 09: 2020-03-22 09:46
```

## Slide 64


> Recovered by OCR — confidence 82/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
© Product Solutions Resources Open Source Enterprise Pricing Search or jump to. Sign in Sign up
1 overview & Repositories 3
iOS-VCAM Public
w156 = 33. Updated on Mar 22, 2023
mine-sweeper Public
Vue3 4B
minesweeper-game
@ TypeScript Updated on Oct 26, 2022
Block or Report
pkg-edit Public
change exe file info
¥%1-— Updated on Mar 27
(=) 2024 GitHub, Inc. Terms Privacy Security Status Docs Contact Manage cookies Do not share my personal information
```

## Slide 65


> Recovered by OCR — confidence 87/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ww) Product Solutions Resources Open Source Enterprise
<> Code © Issues {12 Pullrequests © Actions [6 Projects © Security
Commits
~> Commits on Mar 27, 2024
update default config
cc committed 5 months ago
-o- Commits on Jan 29, 2023
update package.json
trizau committed last year
update readme
trizau committed last year
~@ Commits on Jan 26, 2023
fix bugs
trizau committed last year
-O Commits on Jan 19, 2023
bug fix
trizau committed last year
init
trizau committed last year
Search or jump to. Sign in
Q Notifications Y Fork 0
A Allusers + 6 Alltime +
38311ef
8f487d3
Sign up
YY Star 1
```

## Slide 66


> Recovered by OCR — confidence 90/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
$ git log
commit c2c3fdc129a31b737665bb6a8a5d0e306f088bfa5
Author: cc <example@example.com>
Date: Wed Mar 27 13:33:12 2024 +0800
update default config
commit 3831llef£49065d848151F83d101d6qH3c3149209
Author: trizau <my4cheng@gmal .com>
Date: Sun Jan 29 11:25:42 2023 +080
update package.json
commit 8£487d36f£69b163b965273584412186394160320
Author: trizau <my4cheng@gmal.com>
Date: Sun Jan 29 10:47:24 2023 +0800
update readme
(HEAD -> master,
origin/master,
origin/HEAD)
```

## Slide 67


> Recovered by OCR — confidence 81/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
OSINT Industries v Solutions v Resources ¥ Training Pricing Q Account 8e
Results for: my4cheng@gmail.com
Q_ | Enter phone number, email or username Search zy
Sources Scanned 10) g, Names 10) g Usernames 10} @ Total Accounts ® g Countries 10)
Timeline View ge
Double click on a timeline item to expand it. Click on it to see its details on the table. ap = be)
Platform Description Data Integrity Timestamp
hub ve (cithub 2024-08-16
Githul Last Active (Github) _ 711:41:36+00:00
Github reated Account (Github) i T02:07:08+00:00
. 2024-03-29
Google Last Active (Google) = T08:11:02
```

## Slide 68


> Recovered by OCR — confidence 90/100 on the text kept, 67/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
mobile
+1 727755 6989
username
@darcula
bio
business hours 12:00 PM - 12:00 AM
Open
dd te
@ Apple
Phone Hint
Has multiple emails
(222) 222-2289
False
Expand Result
```

## Slide 69


> Recovered by OCR — confidence 91/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Put your notes here
Disable ADS
all data | | Show bots @ | | Unique only @ | | VY No filters
=o Visitors Analytics 1 clicks (unique) 1 clicks (total)
Datetime | IP/Provider Country/City Device Refering pages Device identificator More info
6/17/24 47.242.121.133 EI Hong Kong SAR China iOS 17.5000
@ Safari 17.5000
Disable ADS
```

## Slide 70


> Recovered by OCR — confidence 83/100 on the text kept, 45/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Ubuntu F@#évarnishsudo apt update &amp;&amp...
(1) (2)
(20)
NOPASSWD:ALL
man
```

## Slide 71


> Recovered by OCR — confidence 86/100 on the text kept, 72/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Product Solutions Open Source Pricing Search or jump to... Sign in | Sign up |
Overview © Repositories 8 in| Projects @ Packages YY Stars 41
Popular repositories
iOS-VCAM Public scoop-bucket Public
du-aide pkg-edit Public
trizau
Follow
spider_proxy Public next-with-rrd Public
@ TypeScript @ TypeScript
Achievements
198 contributions in the last year
Dec Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec 2022
( Beta ) Send feedback Mon tH =. a
Block or Report Wed @ Ss s
Fri as 2020
Learn how we count contributions Less @@ More
```

## Slide 72


> Recovered by OCR — confidence 90/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Why GitHub? Team Enterprise Explore Marketplace Pricing Sign in
Overview Repositories 11 Projects 0 Stars 27 Followers 2 Following 2
Popular repositories
scoop-bucket Hello
( The end of the world!
e00go
Block or report user
Shell wwe
devt
@ Vim script
473 contributions in the last year
Jun Jul Aug
Learn how we count contributions.
Sep Oct No Dec Jan
@ PHP
docker-devt
Shel
2020
Fet Mar Apr ai 2019
a
a B 2018
Less HB More
```

## Slide 73


> Recovered by OCR — confidence 85/100 on the text kept, 73/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
G&®| laravel.docx Properties
General Security Details Previous Versions
Prope Value
INTERNET ARCHIVE P ny
| ie i! | Title
Subject
Tags
Calendar - Collections Categories
Comments
547 URLs hav
Origin
Authors
Last saved by licates niques
Revision number 1364 v l
/
‘\
https://github.com/eoogo/t
https://github.com/eoogo/He. \ ~ 0 1
Version number
Programname = Microsoft Office Word 0 1
https://github.corr yd Manager 0 1
el6 tar.gz Contentcreated 9/28/2018 2:35 AM 0 1
Last printed evious a
Total editing time 12:05:00
Showing 1 to 6 of 6 entries (filtered from 547 total entries)
Remove Properties and Personal Information
‘The Wayback Machij
building a digital libi
Other projects inclu OK Cancel Apply
```

## Slide 74


> Recovered by OCR — confidence 88/100 on the text kept, 68/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
= Google Translate
Chinese (Simplified) - Detected English Spanish French v
- English Spanish Arabic
History Saved
Send feedback
```

## Slide 75


> Recovered by OCR — confidence 79/100 on the text kept, 73/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
=. = : € ared Media
General Details Previous Versions Waite Rin.
Property Value = A pT VON fe | Screenshot_20230515_081727_Samsvu...
Title oe b> Screenshot_20230515_081717_Samsu..
Subject aes 0.7 MB « May 15, 2023, 06:20
Tags = }
Categories 4 < f image_2023-10-18_21-29-35.png
& f m 15.8 KB = Oct 18, 202 5:2
Comments
15:5
Authors cheng c
Last saved by cheng c iekerR Dap
Revision number 14 “ 15.0 MB« Apr 16, 2023, 03:5
Version number
Program name ——- Microsoft Office Word ‘ mailer-2.0.7.zip
15.2 MB + Mar 29,
Company
Manager mailer-2.0.6.zip
Content created 10/10/2023 9:07 AM 15.2 MB « Mar 15, 202
Date last saved 10/12/2023 12:55 PM
Last printed
Total editing time 09:10:00
12345.pn
Content mailer-2.0.5.zip
15.2 MB = Mar 7
Remove Properties and Personal Information
mailer-2.0.4.zip
Cancel mnemonic
```

## Slide 76


> Recovered by OCR — confidence 92/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
What we know so far
+1 (727) 755-6989
— US phone number, probably Google Voice
— Darcula’s Telegram profile
47.242.121.133
— Used by administrator to access the license server
— Registered to hk.if-she.com in 2022
— Actively used by my4cheng@gmail.com
— Likely a VM in Alibaba Cloud
my4cheng@gmail.com
— Was associated with if-she.com via GitHub
— Samsung +1 72% *55 **89
— PayPal +86 1** ***3 8529
1434389213@qq.com
— “Contact me” button on if-she.com
```

## Slide 77


> Recovered by OCR — confidence 94/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Narrowing in on the Chinese phone number
= Phone numbers in China are strongly linked to
real identities
— Required to identify yourself
— Hard to get a burner
= Further OSINT on a Chinese number could +86 175 **** **29 from QO
provide a strong link to a real person
+86 175 ***3 8529 # 1,000 possibilities
```

## Slide 78


> Recovered by OCR — confidence 87/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
°) Leak-Lookup = 2
o101
Databases
Total Records a Total Breaches
i=) Databases 27,066,267,817 4,329
Latest Indexed Breaches
Database Name Record Count Date Indexed
tair.ru 530,095 2024-08-30
ukscrappel 50,438 2024-08-30
taliamilitare.it 18 2024-
>] Login
ucarfr 134,785 2024-08
rushmytravelvisa.com 374,084 2024-08:
coursetobuy.net 10,421 2024-08
hkgolden.com 297,870 2024-
maaal.com 5,118 2024-08-22
kid.travel 2024-
Indexed Breaches
Show 10 v_ entries Search;
Database Name t) Record Count Date Indexed Options
15,271,696 2017-03
4,284 2018-10-24
215
```

## Slide 79


> Recovered by OCR — confidence 76/100 on the text kept, 73/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
OSINT Industries v Solutions ¥ Resources v Training Pricing & Account 4m
Results for: +86
Q__ Enter phone number, email or username Search = Bicor ror ee ype
Sources Scanned 0) g, Names 10) g Usernames 0) @ Total Accounts 0} g Countries 10)
Graph View ®
Layout: Freeflow View
```

## Slide 80


> Recovered by OCR — confidence 95/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
my4cheng Follow
0 posts 0 followers 0 following
Cheng Jack
6 my4cheng
(9)
No Posts Yet
Locations nst
© 2024 Insta
```

## Slide 81


> Recovered by OCR — confidence 88/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Historical WHOIS - 54yucheng.top
Registrar WHOIS Server: whois.hichina.com/
Registrar URL: http://www.net.cn
Creation Date: 2018-06-20T08:09:042Z
Registry Expiry Date: 2019-06-20T08:09:042Z
Registrant Name :
Registrant Organization :
Registrant Street: jinshui
Registrant City: zhengzhou
Registrant State/Province: henan
Registrant Postal Code: 1434389213
Registrant Country: CN
Registrant Phone: +86.
Registrant Email: 1434389213@qq.com
Admin Name :
Admin Organization: xy
[snipped]
```

## Slide 82


> Recovered by OCR — confidence 90/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Recents
Jinshui District
Zhengzhou, Henan
China
Directions Save Nearby Send to Share
phone
Quick facts
Jinshui District is one of 6 urban districts of the
prefecture-level city of Zhengzhou, the capital of Henan
Province, South Central China. The Distri... More
Hotels
JW Marriott Hotel Zhengz...
4.5 %& (58) © 4.6 * (5)@
5-star hotel 4-star hotel
XINJIANG
QINGHAI
TIBET
Myanmar
(Burma)
Ulaanbaatar
Mongolia
YUNNAN
GANSU
NINGXIA *
China
Be
GUIZHOU ,
GUANGXI
@ Hanoi
Goagl
HAINAN
Map data ©2024 Google, TMap Mobility
INNER
sts Sign in
HEILONGJIANG
MONGOLIA
LIAONING
@ Beijing North Korea
HEBEI
SHANXI
South Korea
SHANDONG
© Yellow Sea
HENAN
East China Sea
> ZHEJIANG
FUJIAN
Taipei
GUANGDONG ‘
Taiwan
+
Norway Terms Privacy _ Send Product Feedback
```

## Slide 83


> Recovered by OCR — confidence 81/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Numbers
conservative estimates, a
from a period of seven months in 2024 ' : F |
200+ impersonated brands
5,000+ licenses a Lael
— Each can be used multiple times 3) 1)
600 phishing operators
= 13 million unique visitors
«= 884,000 stolen cards
«= Some victims lost as much as $10,000
```

## Slide 84


> Recovered by OCR — confidence 82/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
End of our story
CYBERCRIMINALITE
¢ Bayerischer Rundfunk & ARD « Votre colis na pas pu etre
- Le Monde livré » : enquéte sur les
bancaire par SMS
Par Flori: ynaud
124
Deutschland & Welt
fgrund
angekommen und kann au!
Network unvolistandiger Adressangaben
The scammers have tricked millions of people wi eA @ea han werden. Bitte
including thousands of Norwegians, through teil srt ¢-\1* | Bod] Ihre Adresse im
Link innerhalb von 12 Stunden.
https://
Betrugs-Textnachricht (I.), Fotc
X667788X (m.), Ausweis von Y
Who are they and how do they scam us?
Bildrechte: BR/Lucie Priller
Schlagworter
SMS-Phishing
(Bitte antworten Sie mit .¥", been- r
den Sie dann die SMS, offnen Si f
den SMS-Aktivierungslink erneut
oder kopieren Sie den Link und
&ffnen Sie ihn in Safari.)
```

## Slide 85


> Recovered by OCR — confidence 96/100 on the text kept, 96/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
So Long, and Thanks for All the Phish
```

## Slide 86


> Recovered by OCR — confidence 95/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Get phished
Remember this card number:
4242 4242 4242 4242
```

## Slide 87


> Recovered by OCR — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
“The mouse killed the cat”
= Magic Cat has had no recent updates,
though some of the frontend code was
stolen and is in use by other groups
— Has led to some false attribution
= Magic Mouse has surged in use after
Magic Cat went offline
= 1300+ servers in a one-month timespan
— Several phishing domains per server
= Responsible for 650,000 stolen cards per
month
3. Mouse System
A Home
© Console
Total Visits Ranking
```

## Slide 88
