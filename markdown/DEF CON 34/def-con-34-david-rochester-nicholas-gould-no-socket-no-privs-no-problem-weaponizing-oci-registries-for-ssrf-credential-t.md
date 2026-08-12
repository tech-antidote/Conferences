---
title: "No Socket, No Privs, No Problem Weaponizing OCI Registries for SSRF, Credential Theft, and Container E"
speakers: ["David Rochester", "Nicholas Gould"]
conference: "DEF CON"
conference_full: "DEF CON 34"
edition: "34"
year: null
source_pdf: "DEF CON 34/DEF CON 34 - David Rochester, Nicholas Gould - No Socket, No Privs, No Problem Weaponizing OCI Registries for SSRF, Credential Theft, and Container E.pdf"
pages: 32
sha256: "9d12c450ef109f80202d10dcbe4ed78ad481840e6e1a5ff27308110c50984d95"
text_chars: 13387
ocr_pages: 16
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T00:15:54Z"
---
# No Socket, No Privs, No Problem Weaponizing OCI Registries for SSRF, Credential Theft, and Container E

**Speakers:** David Rochester, Nicholas Gould  
**Conference:** DEF CON 34  
**Source:** `DEF CON 34/DEF CON 34 - David Rochester, Nicholas Gould - No Socket, No Privs, No Problem Weaponizing OCI Registries for SSRF, Credential Theft, and Container E.pdf` (32 pages)

## Slide 1

|~/dc34/title
Disclaimer: This research was conducted independently. The views and opinions expressed in this
work are solely those of the authors and do not reflect the views or positions of our employers.|
|---|
|**DEF CON 34**|
|**No Socket, No Privs,**|
|**No Problem.**|
|Weaponizing OCI registries for SSRF, Credential Theft
& Container Escapes
David Rochester (@davidrxchester)  ·  Nicholas Gould (@gouldnicholas)|

## Slide 2

**$ Registries**

### **What even is an OCI Registry?**

- **HTTP API that stores and serves artifacts, most commonly container**

- **images and model files**

- **Like a web server hosting any other content**

- **Available Artifacts described by a manifest**

03 / 25

NO SOCKET, NO PRIVS, NO PROBLEM   //   OCI

## Slide 3

NO SOCKET, NO PRIVS, NO PROBLEM   //   OCI 03 / 25

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
The manifest is the menu
MANIFEST.JSON
BLOBS
{
"config": { "digest": "sha256:9f2a.." }, @ config JSON
TAG "layers": [
- >
registry.io/model: latest { "digest": "sha256:a3ed.." }, @ layer 128 MB
{ "digest": "sha256:71bc.." }
] @ layer 42 MB
}
The manifest just lists digests available on the server.
NO SOCKET, NO PRIVS, NO PROBLEM // OCT
```

## Slide 4

Example to download model blob: curl -sSL https://registry.io/v2/model/blobs/sha256:9f2a3c8d…e41 -o model.gguf

03 / 25

NO SOCKET, NO PRIVS, NO PROBLEM   //   OCI

## Slide 5

#### **Most software implements their own OCI client**

03 / 25

NO SOCKET, NO PRIVS, NO PROBLEM   //   OCI

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Most software implements their own OCI client
°C)°
container ft]
NO SOCKET, NO PRIVS, NO PROBLEM // OCI @3 / 25
```

## Slide 6

# **Ollama**

- Exposes APIs with zero authentication

- Commonly bound to 0.0.0.0 to facilitate access

- Users can

   - pull models

   - push models

   - request inference

03 / 25

NO SOCKET, NO PRIVS, NO PROBLEM   //   OCI

## Slide 7

# **Docker Model Runner**

- Introduced to Docker Desktop in March 2025

- Run models locally and interact with service from containers

- Reachable from any container via model-runner.docker.internal

- Reachable locally on port 12434

03 / 25

NO SOCKET, NO PRIVS, NO PROBLEM   //   OCI

## Slide 8

# **DMR - Pulling a Model**

NO SOCKET, NO PRIVS, NO PROBLEM   //   OCI

03 / 25

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
DMR - Pulling a Model
~ curl -s -X POST http://LocaLhost:12434/models/create \
-H "Content-Type: application/json" -d '{"from":"ai/smoLLm2"}
© | Request | Response Connection Timing Comment
HEAD https://registry-1.docker.io/v2/ai/smollm2/manifests/latest HTTP/2.0
accept: application/vnd.docker.distribution.manifest.v2+json,
application/vnd.docker.distribution.manifest. list.v2+json,
application/vnd.oci.image.manifest.v1l+json, application/vnd.oci. image. index.v1+json,
HTTP/2.0 401
date: Wed, 15 Jul 2026 14:24:10 GMT
content-type: application/json
content-length: 153
docker-distribution-api-version: registry/2.0
www-authenticate: Bearer
realm="https://auth.docker. io/token", service="registry.docker.io",scope="repository:
ai/smollm2: pull"
docker-ratelimit-source: 2600: 6c5e:1340:1::
strict-transport-security: max—age=31536000
```

## Slide 9

# **DMR - Pulling a Model cont.**

03 / 25

NO SOCKET, NO PRIVS, NO PROBLEM   //   OCI

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
DMR - Pulling a Model cont.
© Request | Response | Connection Timing Comment
HTTP/2.0 200
date: Wed, 15 Jul 2026 14:24:11 GMT
content-type: application/json
x-trace-id: 4de6a054b671cec098e42d7d4c62a925
x-trace-sampled: false
x-ratelimit-limit: 3000, 3000;w=60
x-ratelimit-remaining: 2999
© | Request | Response Connection Timing Comm
| POST https://auth.docker. io/token HTTP/2.0
| content-type: app Lication/x-—www-form-ur lencoded;
user-agent: containerd/2.2.3+unknown
content-length: 184
x-ratelimit-reset: 49
accept-encoding: gzi
P 9:9 P strict-transport-security: max—age=31536000
URL-encoded cf-cache-status: DYNAMIC
set-cookie: __cf_bm=8Xp3snC7CaKAPbtyxfFWQdDuiFgi3d24V5tVi
1.0.1.1-
client_id: containerd-client
grant_type: password
password: laa
scope: repository:ai/smollm2:pull
service: registry.docker.io
username: as
ZIPs73W9rGFauxyOKV_x@SNi3pSbhQwFRvB4YEanm2hZ2ctf ltgxqRj
J0G4yks_CiReTSB4S6JL Iw. rtaPXn13DqLmHb8dxT2c; HttpOnly;
Patho 7. Nawatnoath denbae das Cowlencchinad 46 Sit Aa
server: cloudflare
cf-ray: alb96de5aeb13123-ATL
JSON
{
"access_token": '
"scope"
Mexpires__ H
“issued_at": "2026-@7-15T14:24:11.18589822"
NO SOCKET, NO PRIVS, NO PROBLEM // OCI @3 / 25
```

## Slide 10

# **DMR- Pulling a Model cont.**

03 / 25

NO SOCKET, NO PRIVS, NO PROBLEM   //   OCI

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
DMR- Pulling a Model cont.
© | Request | Response Connection Timing Comment
GET https://registry-1.docker. i0/v2/ai/smollm2/manifests/sha256: 354bf30d0aa3af413d2
aadae4f23 e07a5b0d776e9606a2f0b9 HTTP/2.0
user-agent: Docker—-Desktop/4.74.@ (Mac; arm64)
accept: application/vnd.oci.image.manifest.v1+json, */*
accept-encoding: zstd;q=1.0, gzip;q=0.8, deflate; q=0.5
authorization: Bearer
eyJhbGci0iJSUZI1INiIsInR5cCI6IkpXVCIsIng1YyI6WyJNSULFRmpDQ@F2NmdBd LCQWdJIVU9yTFd5UVpx
MmFuZXd6WnhYN1JLbHQ3bDVUTXdEUV LKS29aSWh2Y@5BUUVMQ LF Bd2dZWxXhDekFKQmdOVkJBWVRBbFZUTVIN
d@VRWURWUVFIRXdwRF LXeHBabT L5Ym1saE1SSXdFQV LEV LFRSEV3bFFZV3h2SUVGc2RHOHHGVEFUQmdO0VkIB
KAD EDIT AAKCAIRADATVIoUATC REVIT CCHADMIAICA DANTE TVAILIC H/o el BI AC 14 Vb WIC Em Am ANVIL ID TVDU
No content @ Edit Replace  () View: auto ~
NO SOCKET, NO PRIVS, NO PROBLEM // OCI
© Request | Response} Connection Timing Comment
HTTP/2.0 200
date: Wed, 15 Jul 2026 14:24:11 GMT
content-type: application/vnd.oci. image.manifest.v1+json
content-length: 551
docker-content-
digest: sha256:354bf30d0aa3af413d2aa5ae4f23c66d78980072d1e07a5b0d776e9606a2 Ff 0b9
docker-distribution-api-version: registry/2.0
etag: "sha256:354bf30d0aa3af413d2aa5ae4 f23c66d78980072d1e07a5b0d776e9606a2 f0b9"
docker-ratelimit-source: davidrochester1
x-ratelimit-limit: 200; w=3600
ratelimit-limit: 200 ; w=3600
x-ratelimit-remaining: 198 ; w=3600
ratelimit-remaining: 198 ; w=3600
strict-transport-security: max—age=31536000
JSON B\Copy @Edit M&Replace ( View: auto
4
"schemaVersion": 2,
"mediaType": “application/vnd.oci. image.manifest.v1+json",
"config": {
"mediaType": "“application/vnd.docker.ai.model.config.v@.1+json",
USiZeM ES /O}
"digest": "sha256:32aaa72e00e9a79d38786abd1e37388e7 f01181a0f 1bdf23ef ff6433c12F 89
```

## Slide 11

# **DMR - Pulling a Model cont.**

03 / 25

NO SOCKET, NO PRIVS, NO PROBLEM   //   OCI

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
DMR - Pulling a Model cont.
date: Wed, 15 Jul 2026 14:24:10 GMT
content-type: application/json
content-length: 153
docker-distribution-api-version: registry/2.0
www-authenticate: Bearer
realm="https://auth.docker.io/token", service="registry.docker.io",scope="repository:
ai/smollm2: pull"
docker-ratelimit-source: 2600:6c5e:1340:1::
strict-transport-security: max—age=31536000
NO SOCKET, NO PRIVS, NO PROBLEM // OCI @3 / 25
```

## Slide 12

# **Abusing the Auth Flow**

03 / 25

NO SOCKET, NO PRIVS, NO PROBLEM   //   OCI

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Abusing the Auth Flow
registry.attacker.io Docker Model Runner Internal service
our malicious registry on the HOST 127.0.0.1 - 169.254.169.254
any container can trigger it
1 GET /v2/ — model pull begins
<
2 401 realm = http://127.0.0.1:9200
pe
3 GET the realm + SSRF from the host
a
4 response { "token", data }
<
5 retry — we read the response
G
full response body reflected
+ Docker Hub creds forwarded
——— =attacker-controlled
NO SOCKET, NO PRIVS, NO PROBLEM // OCI 03 / 25
```

## Slide 13

# **DMR - SSRF Demo**

03 / 25

NO SOCKET, NO PRIVS, NO PROBLEM   //   OCI

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
DMR - SSRF Demo
'» docker-ssrf-poc [] )» docker-ssrf-poc []
© @ @ docker exec -it victim sh
‘» docker-ssrf-poc docker exec -it victim sh
~$f
NO SOCKET, NO PRIVS, NO PROBLEM // OCT @3 / 25
```

## Slide 14

# **Hunting SSRF in Ollama**

● Ollama validates realm before sending tokens cross-origin

`server/auth.go`

03 / 25

NO SOCKET, NO PRIVS, NO PROBLEM   //   OCI

## Slide 15

# **Hunting SSRF in Ollama**

● 307 Redirects

`server/download.go`

03 / 25

NO SOCKET, NO PRIVS, NO PROBLEM   //   OCI

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ __Ollama Server © Malicious OCI Registry
Hunting SSRF in Ollama
1. Ollama
requests blob
G Ollama
@ 307 Redirects
if resp.StatusCode != http.StatusTemporaryRedirect && resp.StatusCode != http.StatusOK {
return nil, fmt.Errorf("unexpected status code %d", resp.StatusCode)
i
return resp.Location()
‘server/download.go-
NO SOCKET, NO PRIVS, NO PROBLEM // OCI @3 / 25
```

## Slide 16

NO SOCKET, NO PRIVS, NO PROBLEM   //   OCI 03 / 25

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
HASH VERIFY THE BYPASS
One digest, twice. Verification skipped.
01 02
y
downloadBlob()
307 — SSRF body written
Malicious
sha256:alb2...
4 4 4 : LOGIC
skipVerify[layer.Digest] = cacheHit
03
digest
alb2...
skipVerify Map
Cache hit overwrites the
skipVerify
false true
Lite)
FLAW
stays on disk.
04 05
HTTP 200
internal
SHA;-256 =
service
Blob on Disk
Internal response persists
verifyBlob()
Skipped flag is true
A cache hit overwrites verification state — the unverified blob
SAME DIGEST, SECOND LAYER // HASH VERIFY BYPASS
```

## Slide 17

|~/dc34/credential-theft|
|---|
|**ATTACK CLASS**
**ATTACK CLASS**|
|**~~02~~**
**Credential Theft**|
|Access Galore
NO SOCKET, NO PRIVS, NO PROBLEM   //   Credential Theft
13 / 25|

## Slide 18

# **Ex: (O)llama Whisper**

03 / 25

NO SOCKET, NO PRIVS, NO PROBLEM   //   OCI

## Slide 19

# **Ex: (O)llama Whisper**

- Attacker reads any file on the server (e.g. /etc/shadow, SSH keys) - No login required: Ollama has no auth by default

- Ollama commonly listens  on 0.0.0.0

- Bug: a file "digest" isn't checked for ../, so the path escapes its folder

- Trigger: three normal API calls with a booby-trapped digest

- In Docker = runs as root → reads the whole filesystem

- Unpatched : works on latest release (0.31.1) and main, disclosed to Ollama multiple times

03 / 25

NO SOCKET, NO PRIVS, NO PROBLEM   //   OCI

## Slide 20

# **Ex: (O)llama Whisper PoC**

03 / 25

NO SOCKET, NO PRIVS, NO PROBLEM   //   OCI

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Ex: (O)llama Whisper PoC
— VICTIM - ollama-victim (Ollama 0.20.2)
#0]
&
f ot Lama-de@: docker*
ommand)
ATTACKER - rogue registry + exploit
press E to run each command
rs/exploit#
NO SOCKET, NO PRIVS, NO PROBLEM // OCT
```

## Slide 21

# **Ex: (O)llama Whisper Current State**

- Disclosed to Ollama several times ( starting  April 5 2026 )

- received a CVE

- Publicly Exposed Ollama servers:

   - Jan 2026: 175,000 over 130 countries

03 / 25

NO SOCKET, NO PRIVS, NO PROBLEM   //   OCI

## Slide 22

|~/dc34/contai|ner-escape|
|---|---|
|**ATTACK CLASS**|**ATTACK CLASS**|
|**~~0~~**|**Container Escape**|
|NO SOCKET, NO PRIVS, NO PROBLEM|Abusing Docker Model Runner’s inference backends
//   Container Escape
18 / 25|

## Slide 23

NO SOCKET, NO PRIVS, NO PROBLEM   //   OCI 03 / 25

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
DOCKER MODEL RUNNER +: macOS
Inference backends
Llama. cpp vLLM MLX
GGUF - Metal Metal backend mix-Im - Apple Silicon
native, Metal-accelerated inference — runs as a host process
NO SOCKET, NO PRIVS, NO PROBLEM // OCT @3 / 25
```

## Slide 24

# **MLX-LM**

Apple’s open source library for running LLMs on Apple Silicon

03 / 25

NO SOCKET, NO PRIVS, NO PROBLEM   //   OCI

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
MLX-LM
“config.json gets one extra field:
Apple’s open source library .o
for running LLMs on Apple "model_file": "model.py",
one "architectures": ["LlamaForCausalLM'"],
Silicon @ Open Source "model_type": "Llama",
ML»
APPLE PROJECT
MLX
NO SOCKET, NO PRIVS, NO PROBLEM // OCI @3 / 25
```

## Slide 25

NO SOCKET, NO PRIVS, NO PROBLEM   //   OCI 03 / 25

## Slide 26

# **Docker Model Runner Sandbox**

##### **`pkg/inference/backends/mlx/mlx.go`**

03 / 25

NO SOCKET, NO PRIVS, NO PROBLEM   //   OCI

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Docker Model Runner Sandbox
return backends.RunBackend(ctx, backends.RunnerConfig{
BackendName: *MLX",
Socket: socket,
BinaryPath: m.pythonPath,
SandboxPath: Moher
SandboxConfig: ante
Args: args,
Logger: m. log,
ServerLogWriter: logging.Newriter(m.serverLog),
})
‘pkg/inference/backends/mlx/mlx.go"
NO SOCKET, NO PRIVS, NO PROBLEM // OCT @3 / 25
```

## Slide 27

# **Docker Model Runner Sandbox**

**Its empty**

##### **`pkg/inference/backends/mlx/mlx.go`**

03 / 25

NO SOCKET, NO PRIVS, NO PROBLEM   //   OCI

## Slide 28

# **Ex: Free Willy…errrr Docker PoC**

03 / 25

NO SOCKET, NO PRIVS, NO PROBLEM   //   OCI

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Ex: Free Willy...errrr Docker PoC
root@r00t-x1:~# | root@r00t-x1:~#
root@r00t-x1:~#
NO SOCKET, NO PRIVS, NO PROBLEM // OCT @3 / 25
```

## Slide 29

**But Wait there's more…**

## **Some of the other OCI primitives we’ve discovered**

|▸ SSRF Family: 3XX redirects, 401 auths, etc|
|---|
|▸ Producer-controlled metadata XSS Family:  stored XSS|
|▸ Referrers API / attestation / signature Family: DOS, Injection, bypasses|
|▸ Tar layer extraction Family: LFI , RFI, RCE
▸ Image config / build directive Family: RCE, DOS, RFI, LFI|
|▸ Parser / ACL / mediaType / digest differentials Family: injection, data leak, bypasses|
|▸ Cross-class compositions: above chained|
|**Turns out, OCI can be used to perpetuate almostany traditional attack type, not just SSRF / RFI. You**
**just need to find a way to embed itinto your OCI artifact**
24 / 25|

## Slide 30

~/dc34/registry-attacks

NO SOCKET, NO PRIVS, NO PROBLEM   //   FIN

25 / 25

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@@@ ~/dc34/registry-attacks
container fil
rh Ww
ew
SOCKET, NO PRIVS, NO PROBLEM // FIN
```

## Slide 31

~/dc34/closing **DEF CON 34 No Socket. No Privs. No Problem.**

**$** questions? ▊

**David Rochester** ·   @davidrxchester  · **Nicholas Gould** ·   @gouldnicholas NO SOCKET, NO PRIVS, NO PROBLEM   //   FIN

25 / 25

## Slide 32

- **References:** ● <u>https://www.docker.com/products/docker-desktop/</u>

- ● <u>https://github.com/docker/model-runner/security</u>

- ● <u>https://github.com/ml-explore/mlx-lm</u>

- ● <u>https://github.com/ggml-org/llama.cpp</u>

- ● <u>https://github.com/vllm-project/vllm-metal</u>

- ● <u>https://thehackernews.com/2026/01/researchers-fndi</u> -175000-publicly.html

- ● <u>https://github.com/ollama</u>

- ● <u>https://github.com/containerd/containerd</u>

- ● https://opencontainers.org/

24 / 25
