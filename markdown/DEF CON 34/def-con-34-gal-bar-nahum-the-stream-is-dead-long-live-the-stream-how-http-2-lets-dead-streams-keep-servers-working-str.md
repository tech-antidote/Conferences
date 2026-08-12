---
title: "The Stream Is Dead, Long Live the Stream How HTTP 2 Lets Dead Streams Keep Servers Working"
speakers: ["Gal Bar Nahum"]
conference: "DEF CON"
conference_full: "DEF CON 34"
edition: "34"
year: null
source_pdf: "DEF CON 34/DEF CON 34 - Gal Bar Nahum - The Stream Is Dead, Long Live the Stream How HTTP 2 Lets Dead Streams Keep Servers Working - Str.pdf"
pages: 85
sha256: "3d4d587e8d015ef516f4cb5464bdcf1db80afec3a0b08fd8b328a7896cd8a9dc"
text_chars: 16499
ocr_pages: 17
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T00:19:44Z"
---
# The Stream Is Dead, Long Live the Stream How HTTP 2 Lets Dead Streams Keep Servers Working

**Speakers:** Gal Bar Nahum  
**Conference:** DEF CON 34  
**Source:** `DEF CON 34/DEF CON 34 - Gal Bar Nahum - The Stream Is Dead, Long Live the Stream How HTTP 2 Lets Dead Streams Keep Servers Working - Str.pdf` (85 pages)


## Slide 1

**The Stream Is Dead, Long Live the Stream! Gal Bar Nahum**

## Slide 2

##### **Whoami**

**Gal Bar Nahum Security & AI Researcher @ Tenzai Personal Blog: galbarnahum.com/**

## Slide 3

**Usually, Vulnerabilities…**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
eee src/utils/graphql/withQuery.js — js-project
A EXPLORER BB withQuery,js graphal
4 JS-PROJECT src > utils > graphql > HB withQuery.js > t1INITIAL_QUERY_STATE
@ circleci stefankrajnik, 2 months ago | 4 authors (Pavol Madar and others)
oa import React. from ‘react*
import PropTypes from 'prop-types'
import { bindActionCreators } from 'redux'
te I import { connect } from 'react-redux'
B® public import { createActions, handleActions } from 'redux-actions'
@ scripts import snakeCase from 'lodash.snakecase'
CA src import { request as defaultRequest } from ‘utils/network'
B5 assets const getUpperSnakeCase = key => snakeCase(key).toUpperCase()
BB components
BB locales const defaultMapDataToReducer = (data, payload) => payload
const defaultMapQueryDataToProps = data = data
@ cypress
@ routes
Lata const INITIAL_QUERY_STATE =-{
DB utils stefankrajnik, 2 months ago + Implement shouldClearCache option in with
@ format variables: null,
© graphal isFetching: false,
isFetched: false,
Cl
BB index.js error: null
BB snippets.js
BB withQuery.js
BB historyjs export const createQueriesStore = ({ routeNamespace, query }) => {
B it8n.js const-{
mapDataToReducer = defaultMapDataToReducer,
mapQueryDataToProps = defaultMapQueryDataToProps,
BB lokalisejs request: networkRequest = defaultRequest
BB network.js }-=-query
const actions = createActions({
[getUpperSnakeCase(routeNamespace)]: {
[getUpperSnakeCase(query.name)]: {
reduxPersist.js REQUEST: undefined,
@ localStorage.js
BB onClickOutside,js
i redux.js
red router,js SUCCESS: undefined,
» OUTLINE FAILURE: COANE
Pdevelop ©1810 @0A0 [Live Share ‘© stefankrajnik, 2months ago Ln15,Col14 Spaces:2 UTF-8 LF JavaScriptReact M@
```

## Slide 4

##### **Protocol Level Vulnerabilities**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Protocol Level Vulnerabilities
RFC 9113
HTTP/2
Abstract
This specification describes an optimized expression of the semantics of the Hypertext Transfer Protocol
(HTTP), referred to as HTTP version 2 (HTTP/2). HTTP/2 enables a more efficient use of network resources and
a reduced latency by introducing field compression and allowing multiple concurrent exchanges on the same
connection.
This document obsoletes RFCs 7540 and 8740.9]
Status of This Memo
This is an Internet Standards Track document.
This document is a product of the Internet Engineering Task Force (IETF). It represents the consensus of the
IETF community. It has received public review and has been approved for publication by the Internet
Engineering Steering Group (IESG). Further information on Internet Standards is available in Section 2 of RFC
7841.
Information about the current status of this document, any errata, and how to provide feedback on it may be
obtained at https://www.rfc-editor.org/info/rfc9113.
reserved
(local)
recv ES
half-
closed
(remote)
send R /
recv R
reserved
(remote)
send ES
half-
send R / closed
recv R (local)
closed
send R /
recv R
```

## Slide 5

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
a
ca
mo
a
ly
CLOUDFLARE
®
©
e @ varnisH
r ) CACHE
®
```

## Slide 6

##### **Agenda**

**HTTP/2 1** & Request Concurrency

**2**

**Rapid Reset** & The original explanation

**The Real Problem 3** & a new vulnerability in HTTP/2

**The Design Flaw in HTTP/2 4** & What can we learn from that

## Slide 7

```
[HTTP/2]
```

## Slide 8

```
[HTTP/2]
```

##### **HTTP/2**

**Designed to replace HTTP/1.1**

**Speed & efficiency**

**Almost every major website supports it**

**Request Concurrency**

## Slide 9

```
[HTTP/2]
```

##### **Many Requests, One Connection**

Stream 1 Closed
HTTP/2
connection Request 1 Response 1
Stream 3
Stream 5
Stream 7

## Slide 10

[ HTTP/2 ]

##### **Many Requests, One Connection**

Stream 1
Stream 3
Request 2 Response 2
Stream 5
Request 3 Response 3
Stream 7
Request 4 Response 4

## Slide 11

```
[HTTP/2]
```

##### **Concurrency Limits**

###### **Concurrency is limited by design**

**Max 100 concurrent streams (by default)**

###### **Implemented by a counter**

## Slide 12

[ HTTP/2 ]

##### **Concurrency Limits**

ClosedActive
Stream 1
Active Streams
Request 1 Response 1
Counter: 0 1
Stream 3
Stream 5
Stream 7

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Concurrency Limits
a.
AGA
Stream 1| Siibex oS
Stream aa)
BF request Mit Response 1
Stream 3
( a a od eee thar) a) I Co) eS
POR he tates Un es eee ae )
Stream 5
( TD NE) te oo
Do ee ee )
Stream 7
eee ee ee ee
eee
HTTP/2
Active Streams
Counter: 0
```

## Slide 13

[ HTTP/2 ]

Stopping DoS
Active
Stream X
Active Streams
Request
Counter:  109 890
1 !
Active
Stream X+2
Request
Active
Stream X+4
Request
Stream X+6

## Slide 14

```
[ Rapid Reset ]
```

## Slide 15

```
[ Rapid Reset ]
```

##### **Rapid Reset (2023)**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
[ Rapid Reset |
Rapid Reset (2023)
CVE-2023-44487 Pusiishes B View JSON | @ User Guide
Hov
Collapse all
Required CVE Record Information
CNA: MITRE Corporation met many streams quickly,
Updated: 2025-06-07
Published: 2023-10-10
Description
rces is also displayed.
The HTTP/2 protocol allows a denial of service (server resource consumption) because request cancellation can reset many streams quickly, as
exploited in the wild in August through October 2023.
/C:N/I:N/A:H
Product Status
Learn more
/C:N/I:N/A:H
Information not provided
References} 144 Total
```

## Slide 16

```
[ Rapid Reset ]
```

##### **Rapid Reset (2023)**

Cancel Request ➜ Stream Reset ➜ RST_STREAM

## Slide 17

[  Rapid Reset  ]

##### **Request Cancellation**

Stream 1
Active Streams
Counter: 0 1
ClosedActive
Stream 3
Request 2RST_STREAM
Stream 5
Stream 7

## Slide 18

```
[ Rapid Reset ]
```

##### **Rapid Reset (2023)**

Active Streams Counter ≤ 1

**Stream ID: Stream ID: 9Stream ID: 3Stream ID: 175** 95137 **RST_STREAMRST_STREAM** **GET _** CDAEB

## Slide 19

```
[ Rapid Reset ]
```

##### **The Original Explanation**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
The Original Explanation
Google
[ Rapid
How it works: The novel HTTP/2 ‘Rapid Reset’
DDoS attack
October 10, 2023
Juho Snellman Daniele lamartino
Staff Software Engineer Staff Site Reliability Engineer
A number of Google services and Cloud customers have been targeted with a novel HTTP/2-based
DDoS attack which peaked in August. These attacks were significantly larger than any previously-
Reset |
```

## Slide 20

```
[ Rapid Reset ]
```

**No wait**

**_Google’s blog post about Rapid Reset_**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
[ Rapid Reset |
Standard HTTP/2 attack HTTP/2 Rapid Reset attack
>_> | No wait
Responses
#1-100
Requests
#101-200
Responses Requests and
#101-200 RSTs #1-n
```

## Slide 21

```
[ Rapid Reset ]
```

**The Original Explanation “** **_In a typical HTTP/2 server implementation, the server will still have to do significant amounts of work for canceled requests — allocating new stream data structures, parsing the query…_**

**_— Google’s blog post on Rapid Reset_**

## Slide 22

```
[ Rapid Reset ]
```

## **Rapid Reset, Basically**

**Impact Why? Unbounded Sending Rate RST_STREAMs Work at the Handling canceled server side requests**

## Slide 23

```
[The Real Problem ]
```

### **Unbounded Rate x Canceled Request handling**

## Slide 24

```
[Replicating the work ]
```

## Slide 25

RFC
“Malformed requests
MUST
be treated as errors”

## Slide 26

```
[A New Vulnerability ]
```

### **Quick Win**

Stream ID: 1 9537
GET ADCBE
RESET
Stream ID: 17359
RST _ _STREAM

## Slide 27

```
[ Rapid Reset ]
```

## **Rapid Malformed Requests, Basically**

**Impact**

**Unbounded Rate**

**Why? Sending Malformed Requests**

**Work at the Handling Malformed server side requests**

## Slide 28

##### **Impact Analysis (illustration)**

Rapid Reset

**Rapid “Malformed requests”**

## Slide 29

## Slide 30

```
[ Rapid Reset ]
```

### **What is the difference?**

**Impact**

**Unbounded Rate**

**Work at the server side**

**Rapid Malformed Requests**

**Rapid Reset Sending RST_STREAMs**

**Sending Sending RST_STREAMs Malformed Requests Handling canceled Handling Malformed requests requests**

## Slide 31

```
[The Real Problem ]
```

##### **Cancelled Request Handling**

**Request RST_STREAM Cancellation**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
[| The Real Problem |
Cancelled Request Handling
Cancellation |
def handle_rst_stream(stream, ...):
stream.state = CLOSED
stream.active streams counter -= 1
create_reset_stream_ event(stream)
return
```

## Slide 32

###### `[` **`The Real Problem`** `]`

##### **RST_STREAM Handling**

Reset
Event

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
RST_STREAM Handling
def handle_rst_stream(stream, ...):
stream.state = CLOSED
stream.active_ streams counter -= 1
create_reset_stream_ event(stream)
return
= BS
Event
[| The Real Problem |
```

## Slide 33

```
[The Real Problem ]
```

#### **Web Servers Architecture**

**Manages HTTP/2 connections**

**Web Server HTTP/2 Module Backend**

**Executes application logic**

Works with
HTTP
Messages

## Slide 34

```
[The Real Problem ]
```

#### **Request Handling**

###### **Web Server**

Stream ID: 1
GET A

HTTP/2 Module

Backend
Response A

## Slide 35

```
[The Real Problem ]
```

##### **RST_STREAM Handling**

###### **Web Server**

Stream ID: 1 Stream ID: 1 GET A RST_STREAM

HTTP/2 Module  Backend
Reset
Event Response A

## Slide 36

**!**

```
[The Real Problem ]
```

##### **Phantom Streams**

**1 Closed at the protocol level**

**2**

**The request is still active**

###### **Response is computed**

**1 The Stream is Dead**

**2**

**The Request is Alive**

## Slide 37

```
[The Real Problem ]
```

# **Streams** ≠ **Requests**

## Slide 38

```
[The Real Problem ]
```

### **Streams Concurrency limit** ≠ **Requests Concurrency limit**

## Slide 39

```
[The Real Problem ]
```

### **Rapid Reset = Unlimited Concurrent Requests**

**Stream ID: Stream ID: 9StStream ID: 1ream ID: 735** 95137 **RST_STREAMRST_STREAM** **GET _** CDAEB

## Slide 40

```
[ Rapid Reset ]
```

### **The Real Difference**

**Impact**

**Unbounded Rate**

**Work at the server side**

**Rapid Malformed Requests**

**Rapid Reset Malformed Requests Sending Sending RST_STREAMs Malformed Requests Handling canceled Fu l Request Handling Malformed Handlingrequests requests**

## Slide 41

```
[A New Vulnerability ]
```

## Slide 42

```
[A New Vulnerability ]
```

### **Mitigating Rapid Reset**

**Stream ID: Stream ID: 9Stream ID: 3Stream ID: 175** 95137 **RST_STREAMRST_STREAM** **GET _** CDAEB

RESET

## Slide 43

```
[A New Vulnerability ]
```

## Slide 44

```
[A New Vulnerability ]
```

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
[ A New Vulnerability ]
me_ WAIT A'SECOND = }
ven qa g
‘ITDOESN'T STOPP
wi Katy nse  —<S
```

## Slide 45

```
[A New Vulnerability ]
```

### **Mitigating Rapid Reset**

**Stream ID: Stream ID: 9Stream ID: 3Stream ID: 175** 95137 **RST_STREAMRST_STREAM** **GET _** CDAEB

RESET

## Slide 46

```
[A New Vulnerability ]
```

### **The Twist**

Reset the stream Make the server reset the stream for you

## Slide 47

```
[A New Vulnerability ]
```

### **The Twist**

Stream ID: 1 9537
GET ADCBE
RESET
Stream ID: 17359
RST _ _STREAM

## Slide 48

```
[A New Vulnerability ]
```

##### **Can we force the server to reset streams?**

**RST_STREAM**

**Cancellation Error Condition**

**?**

## Slide 49

```
[A New Vulnerability ]
```

### **MadeYouReset Primitives**

**Ways to cause a** **<u>Stream Error</u> after sending a request**

**6 MadeYouReset primitives**

**Defined by the RFC**

## Slide 50

```
[A New Vulnerability ]
```

### **MadeYouReset Primitive**

**Stream ID: 1Stream ID: 1 WINDOW_UPDATEGET A Increment=0**

**Stream ID: 1 RST** _ **STREAM**

## Slide 51

```
[A New Vulnerability ]
```

### **MadeYouReset**

Active Streams Counter ≤ 1 **Stream ID: 1Stream ID: 153975379 MadeYouReset GET AGET DYouReset CBE Primitive**

**Stream ID: 17359 RST _ STREAM**

## Slide 52

```
[A New Vulnerability ]
```

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
The Hacker News
August 14: @ " -—
nis s auursis
@ New HTTP/2 flaw can crash major servers. C150 Strategy  CS/OT \ Famdimg/MEA \ Cyber A
“MadeYouReset” bypasses Rapid Reset protections—letting attackers flood Apache Tomcat, F5 BIG-IP
& more with thousands of requests, taking sites offline.
Here's how it works >
bility Enables Massive
jas been compared to Rapid Reset.
TRENDING
‘Highest Ever’ Severity Score
Assigned by Microsoft to
ASP.NET Core Vulnerability
F5 Hack: Attack Linked to China,
BIG-IP Flaws Patched,
Governments Issue Alerts
Prosper Data Breach Impacts
17.6 Million Accounts
Cisco Routers Hacked for
Rootkit Deployment
THEHAC JEWS
New HTTP/2 ‘MadeYouReset'’ Vulnerability Enables Large-Scale DoS Attacks
t exploit by HT
High-Severity Vulnerabilities
Patched by Fortinet and Ivanti
```

## Slide 53

General CVE

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Vi N CE Vulnerability Information and Coordination Environment
Case VU#767506: HTTP/2 implementations are vulnerable to "MadeYouReset" DoS attack through HTTP/2 control
@Q Dashboard frames
Vendors Home > Notes >» VU#767506
[VAI 19) ] HTTP/2 implementations are vulnerable to
"MadeYouReset" DoS attack through HTTP/2 control
frames
Akamai Technologies Inc.
Amazon AT
A | Vulnerability Note VU#767506 rm) NX
xX
Original Release Date: 2025-08-13 | Last Revised: 2026-03-17
AMD
&» AMPHP CVE-2025-55163 CVE-2025-9784
General CVE
Apache HTTP Server Project CVE-2025-54500 CVE-2025-5115
CVE-2025-8671
Apache Tomcat CVE-2025-48989 CVE-2025-36047
```

## Slide 54

```
[The Real Problem ]
```

#### **The Real Problem is Phantom Streams**

#### **→ Unbounded Number of Concurrent Requests**

## Slide 55

[ The Real Problem  ]

**How bad can it be? What happens when the server is overloaded?**

Normal Flood Under Load Flood
x100 x100
Request Request
Request Request
Request Request
Computing
Wait
x100
Response Computing
time
Wait
Response Response
Response time
Response x100
x100 Response
Response
Request Response
Request
Request x100
Request
Request
Request

## Slide 56

Unbounded
Memory Growth
Real example – Actix Web
Flood Attacker
Phase
MadeYouReset
Phase

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Real example — Actix Web
Tv
c
je}
oO
o
19)
=
oO
a
n
C4
n
oO
=}
a
oO
[a4
—- MadeYouReset Attacker Req/s Flood Attacker Req/s
— Memory Usage (%) — CPU Usage (%)
Flood Attacker
Phase
adeYouReset
Phase
200 250
Time (seconds)
```

## Slide 57

**Let's make it worse High processing time -> stronger attack Increasing high processing time -> even stronger attack**

**How to make processing time grow in highly concurrent systems?**

**Pick non-concurrent operations…**

## Slide 58

**HTTP/2**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
M6 HTTP/2
®
——<<<<<uU48
eel
== _Mys
_
{AE
{AE
```

## Slide 59

```
[The Real Problem ]
```

#### **The Real Problem is Phantom Streams**

#### **→ Unbounded Number of Concurrent Requests**

## Slide 60

```
[The Design Flaw ]
```

## Slide 61

```
[The Design Flaw ]
```

## **Why so many implementations?**

## Slide 62

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
a
ca
mo
a
ly
CLOUDFLARE
®
©
e @ varnisH
r ) CACHE
®
```

## Slide 63

[ The Design Flaw ]

##### **Before HTTP/2…**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Before HTTP/2...
cocams
Crt —
Ort
coos
The Design Flaw
```

## Slide 64

```
[The Design Flaw ]
```

**Web Server HTTP/1.1 Module HTTP/2 Module Backend**

**The old API remained !**

## Slide 65

[ The Design Flaw ]

### **But HTTP/1.1 does not support request cancellation**

## Slide 66

[ The Design Flaw ]

### **So Existing servers did not support request cancellation**

## Slide 67

```
[The Design Flaw ]
```

### **HTTP/2 entered an existing ecosystem that did not support request cancellation But “allowed” request cancellation**

## Slide 68

So just add
cancellation
support, right?

```
[The Design Flaw ]
```

Right?

## Slide 69

```
[The Design Flaw ]
```

**There is a deeper problem… Real Cancellation is Hard**

## Slide 70

[ The Design Flaw ]

#### **Real End-to-End Cancellation**

###### **Web Server**

Stream ID: 1 Stream ID: 1 GET A RST_STREAM

**HTTP/2 Module**

Cancel A

**Backend**

## Slide 71

```
[The Design Flaw ]
```

**Supporting “End-to-End Cancellation” We must be able to cancel:**

**1 Computations at any point in time**

**2 All computations, everywhere**

## Slide 72

[ The Design Flaw ]

**Stop All Computations Cancellation must propagate everywhere: Legacy code Third party dependencies External services**

**HTTP/2 HTTP/1.1 RST_STREAM** Cancel Cancel Cancel Cancel **?**

## Slide 73

```
[The Design Flaw ]
```

**So end-to-end cancellation is not feasible…**

## Slide 74

[ The Design Flaw ]

**Stopping the work associated with a stream is not feasible**

## Slide 75

```
[The Design Flaw ]
```

### **Phantom Streams are inherent in the design**

## Slide 76

[ The Design Flaw ]

## **Design Flaws in HTTP/2**

**1 Resetting Streams → Phantom Streams Within Concurrency Limits, Rate is 2 Controlled By The Client**

**→ Unlimited Request Concurrency**

## Slide 77

```
[The Design Flaw ]
```

## **Is HTTP/2 Doomed?**

#### **No, it's possible to address Phantom Streams**

## Slide 78

```
[The Design Flaw ]
```

### **Should be part of the RFC**

## Slide 79

```
[The Design Flaw ]
```

## **Is HTTP/2 Doomed?**

#### **How MadeYouReset Should Be Fixed?**

## Slide 80

```
[The Design Flaw ]
```

##### **How can we mitigate MadeYouReset?**

**1 Prevent Phantom Streams**

**2 Limit Phantom Streams abuse**

**Just limit the number of RST_STREAMs from the server**

## Slide 81

[ The Design Flaw ]

##### **How are Phantom Streams Created? Recall Phantom Streams:**

**1 Closed at the protocol level**

**2 The request is still active**

**→   The stream must be CLOSED**

## Slide 82

[ The Design Flaw ]

3 ways to close a stream
1 Response from server
2 Client reset
3 Server reset

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
3 ways to close a stream
®
@) Response from server ¥,¢
half-
closed
(remote)
send PP
reserved
(local)
[| The Design Flaw ]
recv PP
reserved
(remote)
```

## Slide 83

```
[The Design Flaw ]
```

**Phantom Streams will always exist… But they won’t be exploited**

## Slide 84

```
[The Design Flaw ]
```

### **Takeaway**

**Protocols are not implemented on paper It's important to verify they fit the environment they enter**

## Slide 85

```
[Thanks!]
```
