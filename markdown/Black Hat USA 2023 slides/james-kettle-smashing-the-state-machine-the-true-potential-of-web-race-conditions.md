---
title: "Smashing the State Machine The True Potential of Web Race Conditions"
speakers: ["James Kettle"]
conference: "Black Hat"
conference_full: "Black Hat USA 2023"
edition: "USA"
year: 2023
source_pdf: "Black Hat USA 2023 slides/James Kettle_Smashing the State Machine The True Potential of Web Race Conditions.pdf"
pages: 31
sha256: "90af9cca28a9fb022e9e75fd55a79d6ba7b6d277696c55d5cf672fd764e2b25a"
text_chars: 9557
ocr_pages: 4
has_ocr: true
redacted_secrets: 0
ocr_confidence: 84.6
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T04:09:58Z"
---
# Smashing the State Machine The True Potential of Web Race Conditions

**Speakers:** James Kettle  
**Conference:** Black Hat USA 2023  
**Source:** `Black Hat USA 2023 slides/James Kettle_Smashing the State Machine The True Potential of Web Race Conditions.pdf` (31 pages)


## Slide 1

# Smashing the state machine

_the true potential of web race conditions_ James Kettle

## Slide 2

### Warning / disclaimer

_These slides are intended to supplement the presentation. They are not suitable for stand-alone consumption. You can find the whitepaper and presentation recording here:_ _<u>https://portswigger.net/research/smashing-the-state-machine</u>_

_If it’s not uploaded yet, you can get notified when it’s ready by following me at_ <u>https://twitter.com/albinowax</u>

_- albinowax_

## Slide 3

### The known potential of race conditions

##### What have you seen?

_[transfer/withdraw, redeem voucher, apply discount, review/rate, login]_

Virtually all **limit-overrun:** if (i < limit): i++ do_action()

Exception: _Race conditions on the web_ , by Josip Franjković /confirmemail.php?e=user@gmail.com&c =13475&code=84751

## Slide 4

### Outline

The true potential

• Single-packet attack

• Strategy

Case studies / Demo Future research

Defense / Takeaways / Questions

## Slide 5

### The true potential of race conditions

|POST|/login
302 Found|
|---|---|
|GET|/role
200 OK|
|POST|/role
302 Found|
||**???**|
||X
X|
||**???**|

## Slide 6

### The true potential of race conditions

|POST|/login|302 Found|
|---|---|---|
|GET|/role|200 OK|
|POST|/role|302 Found|

with race conditions, everything is multi-step

## Slide 7

### Making race conditions reliable: Single-packet attack

###### **Single-packet attack**


> Recovered by OCR — confidence 83/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Making race conditions reliable: Single-packet attack
network latency jitter internal latency (— race window
Request 2 2
Single-packet attack
Requests network latency jitter internal latency
..20 more requests 1
```

## Slide 8

### Single-packet attack: under the hood

Last-byte sync

Timeless timing attack

Single-packet attack


> Recovered by OCR — confidence 84/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Single-packet attack: under the hood
Last-byte sync
Timeless timing attack
Single-packet attack
INTRUDER
TCP packet [) §) [ TCP packet a |
TCP packet B® ® [ TCP packet s|
TCP packet
Request 1 headers & data Request 2 headers & data
TCP packet TCPpacket TCP packet
TCP packet
```

## Slide 9

### Single-packet attack: the recipe

disable TCP_NODELAY // make the OS buffer packets

for each request with no body: send the headers withhold an empty data frame

// some servers process a request early if they see $content-length bytes for each request with a body:

send the headers, and the body except the final byte withhold a data frame containing the final byte

wait for 100ms send a ping frame // the OS doesn't buffer the first frame after a delay send the final frames

// reference implementation: https://github.com/portswigger/turbo-intruder

## Slide 10

## benchmark

20 requests ->

###### Melbourne

Dublin

17,208km

**Last-byte sync:** Median spread: 4ms Standard deviation: 3ms **Single-packet attack:** Median spread: 1ms _4 to 10 times more effective_ Standard deviation : 0.3ms _30 seconds vs 2+ hours of attempts_ The single-packet attack makes remote races local

https://github.com/portswigger/turbo-intruder/benchmark.py

## Slide 11

### Methodology

**Predict** potential collisions **Probe** for clues **Prove** the concept

## Slide 12

### Predict potential collisions

Identify stateful objects/systems & map endpoints

- Users, sessions, orders...

Edit vs Append

- Does password reset invalidate previous reset links?

- Will our requests affect the same record?

## Slide 13

### Probe for clues

#### Craft chaotic blend of conflicting requests Benchmark expected behavior

   - Send request blend **in sequence**

- Analyze responses, timing, emails, side-effects…

- Probe for clues

   - Send request blend **in parallel**

   - Look for anomalies

   - No anomalies? Tune timing to tighten execution spread

## Slide 14

### Prove the concept

#### Understand & clean

- Trim superfluous requests

- Tune the timing

- Automate retries

Explore impact

- Think of it as a structural weakness

- Look for chains & variations

- Don't stop at the first exploit

-$5,000

## Slide 15

## Case studies

## Slide 16

### Object-masking via limit-overrun

POST /api/…/invitations HTTP/2

6x {"email":"a@psres.net"}

6x {"email":"b@psres.net"}

6x {"status":"success"} 1x ✉ 1x {"status":"success"} {"message":"The member's 5x email address has already been taken"} 2x ✉

_“User was successfully removed from project”_

## Slide 17

### A multi-endpoint collision

Add to basket during checkout:

###### Gitlab email verification:


> Recovered by OCR — confidence 84/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
fay A multi-endpoint collision
Add to basket during checkout:
basket
Gitlab email verification:
payment basket
pending eee maxcPayment validated | confirmed
email
email . token
pending - eee centirm validated | confirmed
```

## Slide 18

### Multi-endpoint collisions: handling internal latency

###### **Initial probe**

**Client-side delay**

**Server-side delay**

slow fast slow fast slow change confirmfast

## Slide 19

### Multi-endpoint collisions: handling internal latency

\```
POST /-/profile HTTP/2
To: x2@psres.net
Subject: confirmation
user[email]=x2@psres.net…
x2@psres.net, confirm
GET /users/conf?token=vsz… HTTP/2your email address
\```

`POST /-/profile HTTP/2 user[email]=x2@psres.net` **90ms** `GET /users/conf?token=vsz… HTTP/2`

\```
To: x2@psres.net
Subject: confirmation
…
x1@psres.net, confirm
your email address
\```

## Slide 20

demo: single-endpoint collision!

https://gitlab.com/albinowax1


> Recovered by OCR — confidence 89/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
[4]
demo: single-endpoint collision!
https://gitlab.com/albinowax1
```

## Slide 21

### Single-endpoint collision code analysis

self.unconfirmed_email = self.email // from 'email' parameter

...

self.confirmation_token = @raw_confirmation_token = Devise.friendly_token ...

// this spins off a different thread to render & send the email (hint 1) send_devise_notification(:confirmation_instructions,

@raw_confirmation_token,

{ to: unconfirmed_email } )

###### To: unconfirmed_email

- // template engine reads the variables back from the database

- confirmation_link = confirmation_url(confirmation_token: @token) #content

- = email_default_heading( @resource.unconfirmed_email) // hint 2 %p= _('Click the link below to confirm your email address.') #cta

- = link_to _('Confirm your email address'), confirmation_link

## Slide 22

### Impact

**Gitlab** Attack #1: Invitation hijack Attack #2: 'Sign in with Gitlab' Patched in 15.7.2 on 4<sup>th</sup> Jan 2023

**Devise** - _"far and away the most popular authentication system for Rails"_ Reported to 4 addresses 200+ days ago. No patch. Easily detected via /users/confirmation Case study highlights:

- Visible locking

- No-hint scenario

- Hidden endpoint

## Slide 23

### Deferred collisions

{"email":"foo@psres.net"} ✉ To: bar@psres.net
20 min
{"email":"bar@psres.net"} ✉ To: bar@psres.net

Timing is irrelevant, so volume is critical Second-order clues are extremely valuable

## Slide 24

## Further research

## Slide 25

### Partial construction attacks

Object creation may contain a race window:

datastore.set(sessionid, 'user', user) datastore.set(sessionid, 'token', rand(32))

Requirement 1: uninitialized value/state doesn't trigger exceptions Requirement 2: Attacker can provide a matching value

[no token parameter] token token= token=null token[]= {"token":null}

https://bugs.chromium.org/p/project-zero/issues/detail?id=2085

## Slide 26

### Data-structures and race-condition defenses

###### Locking

Seen in: PHP native sessions, database transactions

• Masks races in other layers

Batching

Seen in: most major session handlers and ORMs

   - Entire record is read in, cached, and written back afterwards

   - Internally consistent during request lifecycle

- Inconsistent across parallel requests, and background threads

- No defence

Seen in: databases, custom session-handlers

- Not consistent during request lifecycle!

## Slide 27

### What if the session handler has no defence?

**# Bypass code-based password reset** session['reset_username'] = username session['reset_code'] = randomCode() Exploit: Synced reset for $victim and $attacker **# Bypass 2FA** session['user'] = username if 2fa_enabled: session['require2fa'] = true Exploit: Synced login and sensitive page fetch **# Session-swap** session['user'] = username set_auth_cookies_for(session['user']) Exploit: Force session cookie on victim, then sync login

## Slide 28

### Improving the single-packet attack

##### Breaking the 30-request barrier

- Achievable with custom TCP/TLS stack via fake dropped packets

- Simpler/easier strategies may exist

Developing server-side precision

- Micro-delays to counteract TLS decryption time

- Longer delays for staggered attacks

- Generic techniques especially valuable

## Slide 29

### Defense

- Avoid sub-states

- Avoid mixing data sources

- Use datastore consistency features

   - Transactions

   - Atomic operations

   - Uniqueness constraints

- Know your session handler

## Slide 30

### References & further reading

**Whitepaper, slides & academy topic** //portswigger.net/research/smashing-the-state-machine //portswigger.net/web-security/race-conditions

###### **Practice labs**

Limit-overrun Rate-limit bypass Multi-endpoint Single-endpoint Partial construction

**Templates**

**Source code** //github.com/PortSwigger/turbo-intruder

single-packet-attack multi-endpoint email-extraction benchmark

**References & further reading:** benchmark //josipfranjkovic.com/blog/race-conditions-on-web //usenix.org/conference/usenixsecurity20/presentation/van-goethem //aaltodoc.aalto.fi/bitstream/handle/123456789/47110/master_Papli_Kaspar_2020.pdf //googleprojectzero.blogspot.com/2021/01/the-state-of-state-machines.html //soroush.me/downloadable/common-security-issues-in-financially-orientated-web-applications.pdf //portswigger.net/research/how-I-choose-a-security-research-topic

## Slide 31

### Takeaways

ish

The single-packet attack makes race conditions reliable With race conditions, everything is multi-step Predict, probe, prove

@albinowax Email: james.kettle@portswigger.net Paper: https://portswigger.net/research
