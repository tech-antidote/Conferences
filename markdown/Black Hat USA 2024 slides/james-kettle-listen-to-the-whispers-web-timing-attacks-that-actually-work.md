---
title: "Listen to the Whispers Web Timing Attacks that Actually Work"
speakers: ["James Kettle"]
conference: "Black Hat"
conference_full: "Black Hat USA 2024"
edition: "USA"
year: 2024
source_pdf: "Black Hat USA 2024 slides/James Kettle_Listen to the Whispers Web Timing Attacks that Actually Work.pdf"
pages: 35
sha256: "cbe2ca84288d013929827f8492873aebdc30d316dfc8679636ab26a7f0743c56"
text_chars: 11924
ocr_pages: 10
has_ocr: true
companion_files: ["James Kettle_Listen to the Whispers Web Timing Attacks that Actually Work_tools.txt"]
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:33:09Z"
---
# Listen to the Whispers Web Timing Attacks that Actually Work

**Speakers:** James Kettle  
**Conference:** Black Hat USA 2024  
**Source:** `Black Hat USA 2024 slides/James Kettle_Listen to the Whispers Web Timing Attacks that Actually Work.pdf` (35 pages)

## Slide 1

Listen to the whispers **_web timing attacks that actually work_** James Kettle

**PortSwigger Research**

## Slide 2

### <u>The timing trap</u>

### Does the database contain a password reset token starting with d7e?

(not to scale)

def strcmp(s1, s2): for c1, c2 in zip(s1, s2): if c1 != c2: return False time.sleep(0.01) return True

## Slide 3

<u>The timing divide</u>

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
The timing divide
©
1,300ms
200ms
30ms
Delay
7us
5ns?
Attacks I've used
Is there a bug report containing 'API-KEY: XYZ’
Does requesting a password reset for carlos trigger an email?
Does the website lock on this row?
Does the compressed PostgreSQL database contain a token witrr xuZ
Does the database contain a password reset token starting with d7e?
Attacks I've read about
```

## Slide 4

<u>The timing divide</u>

200μs (0.2ms, 0.0002 seconds)

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Time gap (us)
The timing divide
30,000 + Does the website lock on this row?
20,000 +
10,000 +
1,000_+ 200us (0.2ms, 0.0002 seconds)
7 Does the compressed PostgreSQL database contain a token with ‘xuz’
```

## Slide 5

### <u>Outline</u>

Making timing attacks that work everywhere Listening to whispers:

- Hidden attack-surface

- Server-side injection

• Reverse proxy misconfigurations Defense / Takeaways / Questions

PortSwigger/param-miner

## Slide 6

Making timing attacks that work everywhere

## Slide 7

<u>The equation for timing attack success</u>

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
The equation for timing attack success
SUCCESS =
. Network Network
O Time > latency jitter
signal
noise
Internal
latency
Internal
jitter
```

## Slide 8

<u>Making timing attacks 'local'</u>

Timeless Timing Attacks (2020)

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Making timing attacks ‘local!
Request 1 headers & data Request 2 headers & data
TCP packet |
Timeless Timing Attacks (2020) |
6 Ti + Network Network — Internal Internal
ime latency jitter latency jitter
Delay
Request 1 (uN SN =D
Request 2 SO is Bi
```

## Slide 9

<u>The sticky ordering problem</u>

#####

- Solution #1: resynchronize with dummy parameters on first request • Requires per-target configuration

- • Fails outright on some targets

- • Amplifies internal noise

## Slide 10

<u>Making timing attacks universal: single-packet attack</u>

SPA v1 (2023)

**Some servers start processing here :(**

SPA v2

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Making timing attacks universal: single-packet attack
TCP packet TCP packet
k
concn, OB 28 | ome
BS 8
Some servers start processing here :(
SPA v2 Bak
... y
TCP packet
| TCP packet |
```

## Slide 11

<u>Enhancing the single-packet attack</u>

disable TCP_NODELAY send a ping frame **>200% accuracy enhancement on nginx** for each request with no body: send the headers withhold an empty data frame for each request with a body: send the headers, and the body except the final byte withhold a data frame containing the final byte wait for 100ms send a ping frame send the final frames

**>200% accuracy enhancement on nginx**

github.com/nxenon/h2spacex Burp Suite Pro/Community 2024.5

## Slide 12

<u>Making timing attacks feasible</u>

## Amplify the signal

- Longest split code path

- Think DoS

GET / HTTP/1.1
X-U: a
{255}
X-U256: a

- -> 256 times easier to detect

## Minimize noise

- Embrace performance features

- Shortest shared code path

Add

`GET / HTTP/1.1 Cookie:` `sid=` `d83a` Remove `DNT: 1`

## Slide 13

# - Hidden attack surface _Guess params_

_does the application support a query parameter called 'exec'?_

## Slide 14

### <u>Discovery overload</u>

|**`Payload`**|**`Response`**|**Respons**|**e time**|
|---|---|---|---|
|`foo: x`|`HTTP/1.1 200 OK`|`50ms`||
|`commonconfig: x`|`HTTP/1.1 200 OK`|`55ms`||
|`commonconfig: {}`|`HTTP/1.1 200 OK`|`50ms`||
|`foo: x`|`--connection closed--`|`30ms`||
|`authorization: x`|`--connection closed--`|`50ms`||
|In cache key|||Cache miss|
|`GET /?`**`id`**`=random`|`HTTP/1.1 200 OK`|`310ms`||
|`GET /?`**`foo`**`=random`|`HTTP/1.1 200 OK`|`22ms`||
|Not in cache key|||Cache hit|

## Slide 15

# The hardest problem: **time analysis is** **_too powerful_**

nowafpls

## Slide 16

### <u>Zooming in: IP address spoofing via HTTP header</u>

Random-header: xyz.example.com 65ms
True-Client-IP: xyz.example.com 70ms
True-Client-IP: xyz.example.com 65ms
375  vulnerable targets
217  with audible DNS caching
206  of which also cause a DNS pingback
(attacker's server)

## Slide 17

### <u>Zooming further</u>

`True-Client-IP: x.psres.net 90ms` `True-Client-IP: 1.1.1.1 170ms` **Time Browser IP Location** 5 minutes ago Chrome on Windows 1.1.1.1 Cloudflare

**->** Timing analysis reveals control flow changes – like exceptions

## Slide 18

# - Server side injection _Detect server-side injection_

## Slide 19

<u>SQLi with a classic payload</u>

**`Payload Response` Response time** `GET /api/alert?mic='` `{} 162ms` `GET /api/alert?mic=''` `{} 170ms` Alternate discovery path: `'||sleep(5)||'`

**->** For sleep-capable bugs, use advanced timing for WAF evasion

**->** What about other injections? JSON, XML, CSV, URL, HTTP, SMTP…

## Slide 20

<u>Blind server-side JSON injection</u>

Invalid JSON speeds the response up by 0.2ms `"error": { key=aa\"bb "message": "Invalid Key: aa\"bb" 24.3ms } "error": { key=a"\bb "message": "Invalid Key: a"\bb" 24.1ms } "error": { key=aaa…a"bbb "message": "Invalid Key: ****bbb" 24.3ms }` …unless the invalid syntax is redacted **->** something is parsing the response server-side!

## Slide 21

<u>Blind server-side parameter pollution</u>

```
/path?objectId=57%23Can't parse parameter180ms
/path?objectId=57%21Can't parse parameter430ms
Hypothesis: /backend?objectId=57#important-param=X
```

You need to know what to expect

**Bug-doppelgangers** _Equivalent but non-blind vulnerabilities useful for developing the understanding required for a successful timing-based exploit_

## Slide 22

Reverse Proxy Misconfigurations Detect scoped-SSRF Find internal targets

_will the front-end proxy to arbitrary subdomains?_

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Reverse Proxy
Misconfigurations
[ JD) Detect scoped-SSRF
Find internal targets
will the front-end proxy to arbitrary subdomains?
```

## Slide 23

<u>SSRF via open reverse proxy</u>

```
GET / HTTP/1.1
Host: xyz.burpcollaborator.net
```

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
SRF via open reverse proxy
Collaborator
server
Firewall
GET / HTTP/1.1
Host:
Vv
Reverse
proxy
xyz.burpcollaborator.net
Public
pi@untimely-demise ~ $ sudo traceroute -T -p 80 94.100.180.7
traceroute to 94.100.180.7 (94.100.180.7), 30 hops max, 60 byte p
bthub.home (192.168.1.254) 1.347 ms 1.403 ms 1.085 ms
31,55.185.188 (31.55.185.188) 12.361 ms 12.382 ms 13.346 ms
195.99.127.116 (195.99.127.116) 12.560 ms core1-hu0-9-0-0.colindale.ukcore.
net (195.99.127.132) 12.687 ms core1-hu0-8-0-S.colindale.ukcore.bt.net (1
127.146) 13.112 ms
195.99.127.60 (195.99.127.60) 17.230 ms core3-hud-8-0-0. faraday.ukcore. btn!
(195.99.127.36) 12.010 ms core3-hu0-14-0-7. faraday.ukcore.bt.net (195.99.127;
) 11.373 ms
core2-Te0-4-0-5.ealing.ukcore.bt.net (62.172.103.191) 13.263 ms core1-Ted-0)
0-2.ealing.ukcore.bt.net (213.121.193.30) 12.663 ms core2-Te0-4-0-6.ealing.ukc
re.bt.net (213.121.193.72)
8 cloud.mail.ru (94.100.180.7) 13.654 ms 14,050 ms
pi@untimely-demise
predator.alien.bt.co.uk
websites
pieuntimely-demise ~ $ sudo traceroute -T -p 443 94.100.180.7
traceroute to 94.100.180.7 (94.100.180.7), 30 hops max, 60 byte packets
1 bthub.home (192.168.1.254) 1.374 ms 1.384 ms 1.408 ms
31,55.185.188 (31.55.185.188) 11.893 ms 11.943 ms 12.629 ms
5 195.99.127.116 (195.99.127.116) 12.295 ms core1-hud-8-0-S.colindale.ukcore
bt.net (195.99.127.146) 12.270 ms core2-hu0-10-0-0.colindale.ukcore.bt.net (1
5.99.127.134) 12.295 ms
6 195.99.127.16 (195.99.127.16) 16.025 ms core4-hud-1-0-0. faraday.ukcore. bt.
net (195.99.127.50) 11.742 ms core3-hu0-14-0-7.faraday.ukcore.bt.net (195.99.1
27.64) 11.837 ms
corei-TeQ-13-0-6.ealing.ukcore.bt.net (213.121.193.24) 17.121 ms core1-Ted
-4-0-3.ealing.ukcore.bt.n 2.103.185) 14.930 ms 14.420 ms
8 host21: 6.ukcore.bt.net (213.121.193.226) 12.745 ms 12.5
12.505 ms
9 213.137.183.17 (213.137.183.17) 14.176 ms 13.318 ms 12.827 ms
10 t2c4-xe-11-1-2-1.uk-lof.eu.bt.net (166.49.164.91) 26.354 ms t2c4-xe-1-1-2-
‘1.uk-lof.eu.bt.net (166.49.164.75) 13.397 ms t2c4-xe-11-1-3-1.uk-lof.eu.bt.net
(166.49.164.95) 19.042 ms
11 xe-11-0-2. frkt-ar2. intl.ip.rostelecom.ru (195.66.225.81) 28.526 ms 45.105
44.806 ms
217.107.67.85 (217.107.67.85) 78.267 ms 77.007 ms
188.254.92.246 (188.254.92.246) 65.405 ms 66.413 ms
4
```

## Slide 24

<u>The scoped-SSRF blind spot</u>

**Scoped SSRF:** SSRF restricted to *.example.com **Caused by:** • Restricted server listener • Internal-only DNS server • Input validation **`Payload in host header Full SSRF Scoped-SSRF`** `abc.example.com 404 Not Found 404 Not Found` `abc.notexample.com 404 Not Found 403 Forbidden`

**->** Scoped-SSRF is invisible to DNS-pingback detection

## Slide 25

Detect scoped-SSRF

<u>Detecting scoped-SSRF</u>

|**`Host header`**|**`Response`**
**Time**|
|---|---|
|`foo.example.com`|`404 Not Found`
`25ms`|
|`foo.random.com`|`403 Forbidden`
`20ms`|
|`abc.example.com`|`404 Not Found`
`25ms`|
|`abc.example.com`|`404 Not Found`
`20ms`|
|Seco|nd response is faster due to DNS caching|
|`aaa…{62}.example.com`|`404 Not Found`
`25ms`|
|`aaa…{63}.example.com`|`404 Not Found`
`20ms`|
||Faster due to invalid DNS label length|

## Slide 26

### <u>Exploiting a scoped SSRF</u>

## Find internal targets

### Subdomain sources:

- 'fdns' DNS database from Rapid7 Project Sonar (58gb!)

- Online services: columbus.elmasy.com & dns.projectdiscovery.io

```
Entry point
mail.example.com
```

```
Host header
mail.example.com
```

```
Result
HTTP/1.1 302 Found
Set-Cookie: sid=abc
X-Cache: miss
```

```
proxy.example.com
```

```
mail.example.com
```

```
HTTP/1.1 302 Found
Set-Cookie: sid=def
```

## Slide 27

<u>Firewall bypass</u>

```
Entry pointHost headerResult
sonarqube.redactedsonarqube.redacted-reset-
app.redacted (proxy)sonarqube.redacted200 OK
```

## Slide 28

<u>Firewall bypass – invisible route variant</u>

```
Entry pointHost headerResult
admin.redacted.govN/ADNS probe fail
www.redacted.govadmin.redacted.gov200 OK
```

## Slide 29

<u>Front-end rule bypass</u>

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Front-end rule bypass
Firewall |
(lo =:
a~S =
eg}, =
og 7 as 5 90) Front end
SX Target
{/
ae
CKD ee =H}=://=
Reverse Publi
UDIIC
proxy websites
Error: Forbidden
Access is forbidden.
```

## Slide 30

<u>Front-end impersonation</u>

```
Service-Gateway-Is-Newrelic-Admin: true
Service-Gateway-Account-Id: 934454
```

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Front-end impersonation
Firewall
OEE f=
& =—-
CHER Front end =
Target
foo |
foo | = f=7 (=
CoD ee = |[=:]]=
Reverse Public
proxy websites
Service-Gateway-Is-Newrelic-Admin: true
Service-Gateway-Account-Id: 934454
```

## Slide 31

CTF https://listentothewhispers.net/

Param Miner Turbo Intruder - > Timing.py

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
CTF
https://listentothewhispers.net/
Ul ———
ete
a e
S eo-o
O
¢
o,e
Param Miner [| |= =z ha——
jee Intruder -> Timing.py
```

## Slide 32

<u>Upcoming tool enhancements</u>

• Enhance param-detection accuracy with single-packet-attack

- Enhance stealth & speed with t-test

- Your requests!

Feature requests here: https://github.com/portswigger/param-miner

## Slide 33

<u>Defense</u>

Assume attackers have full execution flow visibility Always request a PoC… …but patch just in case your security should not rely on noise Break the single-packet attack

- WAF: stagger the packets

- Webserver: throttle to 1 request per 1-5ms per IP

## Slide 34

<u>References & further reading</u>

**Whitepaper, slides & CTF** portswigger.net/research/listen-to-the-whispers

Guess params Detect server-side injection Detect scoped-SSRF Find internal targets

#### **Source code**

github.com/PortSwigger/param-miner github.com/PortSwigger/turbo-intruder Detect scoped-SSRF Find internal targets **References & further reading:** martinschwarzl.at/media/files/compression.pdf usenix.org/conference/usenixsecurity20/presentation/van-goethem portswigger.net/research/the-single-packet-attack-making-remote-race-conditions-local soatok.blog/2021/08/20/lobste-rs-password-reset-vulnerability/ www.ezequiel.tech/p/10k-host-header.html www.youtube.com/watch?v=hWmXEAi9z5w opendata.rapid7.com/sonar.fdns_v2/ portswigger.net/research/cracking-the-lens-targeting-https-hidden-attack-surface

## Slide 35

<u>Takeaways</u>

Web timing attacks answer difficult questions The single-packet attack makes them 'local', universal, and feasible The murmurs are always there… waiting for you to listen

@albinowax

Email: james.kettle@portswigger.net Paper: https://portswigger.net/research

## Companion resources

### `James Kettle_Listen to the Whispers Web Timing Attacks that Actually Work_tools.txt`

```text
https://github.com/PortSwigger/param-miner
```
