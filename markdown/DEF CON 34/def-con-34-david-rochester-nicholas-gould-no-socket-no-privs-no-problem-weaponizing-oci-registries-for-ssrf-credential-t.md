---
title: "No Socket, No Privs, No Problem Weaponizing OCI Registries for SSRF, Credential Theft, and Container E"
speakers: ["David Rochester", "Nicholas Gould"]
conference: "DEF CON"
conference_full: "DEF CON 34"
edition: "34"
year: 2026
source_pdf: "DEF CON 34/DEF CON 34 - David Rochester, Nicholas Gould - No Socket, No Privs, No Problem Weaponizing OCI Registries for SSRF, Credential Theft, and Container E.pdf"
pages: 32
sha256: "9d12c450ef109f80202d10dcbe4ed78ad481840e6e1a5ff27308110c50984d95"
text_chars: 11380
ocr_pages: 14
has_ocr: true
redacted_secrets: 0
ocr_confidence: 87.3
ocr_unreliable_blocks: 0
vision_verified_pages_changed: 27
vision_verified_pages: 32
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T06:25:52Z"
---
# No Socket, No Privs, No Problem Weaponizing OCI Registries for SSRF, Credential Theft, and Container E

**Speakers:** David Rochester, Nicholas Gould  
**Conference:** DEF CON 34  
**Source:** `DEF CON 34/DEF CON 34 - David Rochester, Nicholas Gould - No Socket, No Privs, No Problem Weaponizing OCI Registries for SSRF, Credential Theft, and Container E.pdf` (32 pages)


## Slide 1

~/dc34/title

Disclaimer: This research was conducted independently. The views and opinions expressed in this work are solely those of the authors and do not reflect the views or positions of our employers.

**DEF CON 34**

**No Socket, No Privs,**
**No Problem.**

Weaponizing OCI registries for SSRF, Credential Theft
& Container Escapes

David Rochester (@davidrxchester)  ·  Nicholas Gould (@gouldnicholas)

## Slide 2

**$ Registries**

### **What even is an OCI Registry?**

- **HTTP API that stores and serves artifacts, most commonly container images and model files**
- **Like a web server hosting any other content**
- **Available Artifacts described by a manifest**

03 / 25

NO SOCKET, NO PRIVS, NO PROBLEM   //   OCI

## Slide 3

# **The manifest is the menu**

TAG
registry.io/model:latest

MANIFEST.JSON

```
{
  "config": { "digest": "sha256:9f2a…" },
  "layers": [
    { "digest": "sha256:a3ed…" },
    { "digest": "sha256:71bc…" }
  ]
}
```

BLOBS
- config JSON
- layer 128 MB
- layer 42 MB

The manifest just lists **digests available on the server**.

03 / 25

NO SOCKET, NO PRIVS, NO PROBLEM   //   OCI

## Slide 4

# **Communicate over the OCI protocol**

```
GET   /v2/                          # is this a registry?
GET   /v2/<name>/manifests/<ref>    # fetch a manifest
PUT   /v2/<name>/manifests/<ref>    # publish a manifest
GET   /v2/<name>/blobs/<digest>     # download a blob
POST  /v2/<name>/blobs/uploads/     # upload a blob
```

Example to download model blob:
curl -sSL https://registry.io/v2/model/blobs/sha256:9f2a3c8d…e41 -o model.gguf

03 / 25

NO SOCKET, NO PRIVS, NO PROBLEM   //   OCI

## Slide 5

#### **Most software implements their own OCI client**

03 / 25

NO SOCKET, NO PRIVS, NO PROBLEM   //   OCI

## Slide 6

# **Ollama**

- Exposes APIs with zero authentication
- Commonly bound to 0.0.0.0 to facilitate access
- Users can
   - pull models
   - push models
   - request inference

```
POST    /api/generate    # run inference
POST    /api/chat        # chat completions
GET     /api/tags        # list local models
POST    /api/pull        # pull a model from any registry we name
POST    /api/push        # push a model to a registry
DELETE  /api/delete      # delete a model
```

03 / 25

NO SOCKET, NO PRIVS, NO PROBLEM   //   OCI

## Slide 7

# **Docker Model Runner**

- Introduced to Docker Desktop in March 2025
- Run models locally and interact with service from containers
- Reachable from any container via model-runner.docker.internal
- Reachable locally on port 12434

```
POST    /engines/v1/chat/completions   # inference
POST    /engines/v1/embeddings         # embeddings
GET     /models                        # list models
POST    /models/create                 # pull from any registry
GET     /models/{ns}/{name}            # inspect
DELETE  /models/{ns}/{name}            # delete
```

03 / 25

NO SOCKET, NO PRIVS, NO PROBLEM   //   OCI

## Slide 8

# **DMR - Pulling a Model**

```
~ curl -s -X POST http://localhost:12434/models/create \
-H "Content-Type: application/json" -d '{"from":"ai/smollm2"}'
```

Request | Response | Connection | Timing | Comment

```
HEAD https://registry-1.docker.io/v2/ai/smollm2/manifests/latest HTTP/2.0
accept: application/vnd.docker.distribution.manifest.v2+json,
application/vnd.docker.distribution.manifest.list.v2+json,
application/vnd.oci.image.manifest.v1+json, application/vnd.oci.image.index.v1+json,
*/*
```

```
HTTP/2.0 401
date: Wed, 15 Jul 2026 14:24:10 GMT
content-type: application/json
content-length: 153
docker-distribution-api-version: registry/2.0
www-authenticate: Bearer realm="https://auth.docker.io/token",service="registry.docker.io",scope="repository:ai/smollm2:pull"
docker-ratelimit-source: 2600:6c5e:1340:1::
strict-transport-security: max-age=31536000
```

03 / 25

NO SOCKET, NO PRIVS, NO PROBLEM   //   OCI

## Slide 9

# **DMR - Pulling a Model cont.**

Request | Response | Connection | Timing | Comment

```
POST https://auth.docker.io/token HTTP/2.0
content-type: application/x-www-form-urlencoded;
user-agent: containerd/2.2.3+unknown
content-length: 184
accept-encoding: gzip

URL-encoded

client_id: containerd-client
grant_type: password
password: ████████
scope: repository:ai/smollm2:pull
service: registry.docker.io
username: ████████
```

Request | Response | Connection | Timing | Comment

```
HTTP/2.0 200
date: Wed, 15 Jul 2026 14:24:11 GMT
content-type: application/json
x-trace-id: 4de6a054b671cec098e42d7d4c62a925
x-trace-sampled: false
x-ratelimit-limit: 3000, 3000;w=60
x-ratelimit-remaining: 2999
x-ratelimit-reset: 49
strict-transport-security: max-age=31536000
cf-cache-status: DYNAMIC
set-cookie: __cf_bm=8Xp3snC7CaKAPbtyxfFWQdDuiFqi3d24V5tVm
1.0.1.1-
zIPs73W9rGFauxyOKV_x0SNi3pSbhQwFRvB4YEanm2hZ2ctfltgxqRj
J0G4yks_CiReTSB4S6JLlIw.rtaPXn13DqLmHb8dxT2c; HttpOnly;
Path=/; Domain=auth.docker.io; Expires=Wed, 15 Jul 2026
server: cloudflare
cf-ray: a1b96de5aeb13123-ATL
```

```
JSON
{
  "access_token": "████████",
  "scope": "repository:ai/smollm2:pull",
  "expires_in": 300,
  "issued_at": "2026-07-15T14:24:11.1858982Z"
}
```

03 / 25

NO SOCKET, NO PRIVS, NO PROBLEM   //   OCI

## Slide 10

# **DMR- Pulling a Model cont.**

Request | Response | Connection | Timing | Comment

```
GET https://registry-1.docker.io/v2/ai/smollm2/manifests/sha256:354bf30d0aa3af413d2aa5ae4f23c66d78980072d1e07a5b0d776e9606a2f0b9 HTTP/2.0
user-agent: Docker-Desktop/4.74.0 (Mac; arm64)
accept: application/vnd.oci.image.manifest.v1+json, */*
accept-encoding: zstd;q=1.0, gzip;q=0.8, deflate;q=0.5
authorization: Bearer
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsIng1YyI6WyJNSUlFRmpDQ0F2NmdBd0lCQWdJVU9yTFd5UVpx
MmFuZXd6WnhYN1JLbHQ3bDVUTXdEUVlKS29aSWh2Y05BUUVMQlFBd2dZWXhDekFKQmdOVkJBWVRBbFZUVJN
d0VRWURWUVFJRXdwRFlXeHBabTl5Ym1saE1SSXdFQVlEVlFRSEV3bFFZV3h2SUVGc2RHOHhGVEFUQmdOVkJB
b1RFRV…

No content
```

Request | Response | Connection | Timing | Comment

```
HTTP/2.0 200
date: Wed, 15 Jul 2026 14:24:11 GMT
content-type: application/vnd.oci.image.manifest.v1+json
content-length: 551
docker-content-digest: sha256:354bf30d0aa3af413d2aa5ae4f23c66d78980072d1e07a5b0d776e9606a2f0b9
docker-distribution-api-version: registry/2.0
etag: "sha256:354bf30d0aa3af413d2aa5ae4f23c66d78980072d1e07a5b0d776e9606a2f0b9"
docker-ratelimit-source: davidrochester1
x-ratelimit-limit: 200;w=3600
ratelimit-limit: 200;w=3600
x-ratelimit-remaining: 198;w=3600
ratelimit-remaining: 198;w=3600
strict-transport-security: max-age=31536000
```

```
JSON
{
    "schemaVersion": 2,
    "mediaType": "application/vnd.oci.image.manifest.v1+json",
    "config": {
        "mediaType": "application/vnd.docker.ai.model.config.v0.1+json",
        "size": 375,
        "digest": "sha256:32aaa72e00e9a79d38786abd1e37388e7f01181a0f1bdf23efff6433c12f8…
```

03 / 25

NO SOCKET, NO PRIVS, NO PROBLEM   //   OCI

## Slide 11

# **DMR - Pulling a Model cont.**

```
HTTP/2.0 401
date: Wed, 15 Jul 2026 14:24:10 GMT
content-type: application/json
content-length: 153
docker-distribution-api-version: registry/2.0
www-authenticate: Bearer realm="https://auth.docker.io/token",service="registry.docker.io",scope="repository:ai/smollm2:pull"
docker-ratelimit-source: 2600:6c5e:1340:1::
strict-transport-security: max-age=31536000
```

03 / 25

NO SOCKET, NO PRIVS, NO PROBLEM   //   OCI

## Slide 12

# **Abusing the Auth Flow**

registry.attacker.io
our malicious registry

Docker Model Runner
on the HOST
any container can trigger it

Internal service
127.0.0.1 · 169.254.169.254

1  GET /v2/ — model pull begins
2  401 realm = http://127.0.0.1:9200
3  GET the realm → SSRF from the host
4  response { "token", data }
5  retry — we read the response

full response body reflected
+ Docker Hub creds forwarded

— = attacker-controlled

03 / 25

NO SOCKET, NO PRIVS, NO PROBLEM   //   OCI

## Slide 13

# **DMR - SSRF Demo**

davidrochester@Mac:~/DEFCON34/docker-ssrf-poc

```
docker-ssrf-poc
```

davidrochester@Mac:~/DEFCON34/docker-ssrf-poc

```
docker-ssrf-poc
```

docker exec -it victim sh

```
docker-ssrf-poc docker exec -it victim sh
~ $
```

03 / 25

NO SOCKET, NO PRIVS, NO PROBLEM   //   OCI

## Slide 14

# **Hunting SSRF in Ollama**

- Ollama validates realm before sending tokens cross-origin

```go
// Validate that the realm host matches the original request host to prevent sending tokens cross-origin.
if redirectURL.Host != originalHost {
    return "", fmt.Errorf("realm host %q does not match original host %q", redirectURL.Host, originalHost)
}
```

`server/auth.go`

03 / 25

NO SOCKET, NO PRIVS, NO PROBLEM   //   OCI

## Slide 15

# **Hunting SSRF in Ollama**

Ollama Server
Ollama

1. Ollama requests blob

Malicious OCI Registry
HTTP 307
Temporary Redirect
(Response)

- 307 Redirects

```go
if resp.StatusCode != http.StatusTemporaryRedirect && resp.StatusCode != http.StatusOK {
    return nil, fmt.Errorf("unexpected status code %d", resp.StatusCode)
}
return resp.Location()
```

`server/download.go`

03 / 25

NO SOCKET, NO PRIVS, NO PROBLEM   //   OCI

## Slide 16

HASH VERIFY · THE BYPASS

# **One digest, twice. Verification skipped.**

**01**
**Malicious Manifest**
Two layers · same digest
sha256:a1b2…

**02**
**downloadBlob()**
307 → SSRF body written

**03**
**skipVerify Map**

| digest | skipVerify |
|---|---|
| a1b2… | ~~false~~ → **true** |
| c9d0… | false |

Cache hit overwrites the flag

**04**
**verifyBlob()**
SHA-256
Skipped — flag is true

**05**
**Blob on Disk**
HTTP 200 internal service
Internal response persists

skipVerify[layer.Digest] = **cacheHit**

**LOGIC FLAW**   A cache hit overwrites verification state — the unverified blob stays on disk.

SAME DIGEST, SECOND LAYER   //   HASH VERIFY BYPASS

## Slide 17

~/dc34/credential-theft

**ATTACK CLASS**

**02**

**ATTACK CLASS**

**Credential Theft**

Access Galore

NO SOCKET, NO PRIVS, NO PROBLEM   //   Credential Theft

13 / 25

## Slide 18

# **Ex: (O)llama Whisper**

03 / 25

NO SOCKET, NO PRIVS, NO PROBLEM   //   OCI

## Slide 19

# **Ex: (O)llama Whisper**

- Attacker reads any file on the server (e.g. /etc/shadow, SSH keys)

- No login required: Ollama has no auth by default

- Ollama commonly listens  on 0.0.0.0

- Bug: a file "digest" isn't checked for ../, so the path escapes its folder

- Trigger: three normal API calls with a booby-trapped digest

- In Docker = runs as root → reads the whole filesystem

- Unpatched : works on latest release (0.31.1) and main, disclosed to Ollama multiple times

03 / 25

NO SOCKET, NO PRIVS, NO PROBLEM   //   OCI

## Slide 20

# **Ex: (O)llama Whisper PoC**

```text
─  VICTIM  ─  ollama-victim (Ollama 0.20.2)  ───────────────
== victim box ==   (press Enter to run each command)

root@victim:/# █
```

```text
─  ATTACKER  ─  rogue registry + exploit  ──────────────────
== attacker box ==   (press Enter to run each command)

root@attacker:/exploit#
```

```text
[ollama-de0:docker*                    " VICTIM  ─  ollama-vi" 17:58 04-Jul-26
```

03 / 25

NO SOCKET, NO PRIVS, NO PROBLEM   //   OCI

## Slide 21

# **Ex: (O)llama Whisper Current State**

- Disclosed to Ollama several times ( starting  April 5 2026 )

- received a CVE

- Publicly Exposed Ollama servers:

   - Jan 2026: 175,000 over 130 countries

03 / 25

NO SOCKET, NO PRIVS, NO PROBLEM   //   OCI

## Slide 22

~/dc34/container-escape

**ATTACK CLASS**

**03**

**ATTACK CLASS**

**Container Escape**

Abusing Docker Model Runner’s inference backends

NO SOCKET, NO PRIVS, NO PROBLEM   //   Container Escape

18 / 25

## Slide 23

**DOCKER MODEL RUNNER · macOS**

# **Inference backends**

**llama.cpp**

GGUF · Metal

**vLLM**

Metal backend

**MLX**

mlx-lm · Apple Silicon

native, **Metal-accelerated** inference — runs as a host process

03 / 25

NO SOCKET, NO PRIVS, NO PROBLEM   //   OCI

## Slide 24

# **MLX-LM**

Apple’s open source library for running LLMs on Apple Silicon

Open Source

APPLE PROJECT

MLX

````text
`config.json` gets one extra field:

```json
{
  "model_file": "model.py",
  "architectures": ["LlamaForCausalLM"],
  "model_type": "llama",
  ...
}
```
````

03 / 25

NO SOCKET, NO PRIVS, NO PROBLEM   //   OCI

## Slide 25

NO SOCKET, NO PRIVS, NO PROBLEM   //   OCI 03 / 25

## Slide 26

# **Docker Model Runner Sandbox**

```go
return backends.RunBackend(ctx, backends.RunnerConfig{
    BackendName:     "MLX",
    Socket:          socket,
    BinaryPath:      m.pythonPath,
    SandboxPath:     "",
    SandboxConfig:   "",
    Args:            args,
    Logger:          m.log,
    ServerLogWriter: logging.NewWriter(m.serverLog),
})
```

##### **`pkg/inference/backends/mlx/mlx.go`**

03 / 25

NO SOCKET, NO PRIVS, NO PROBLEM   //   OCI

## Slide 27

# **Docker Model Runner Sandbox**

```go
return backends.RunBackend(ctx, backends.RunnerConfig{
    BackendName:     "MLX",
    Socket:          socket,
    BinaryPath:      m.pythonPath,
    SandboxPath:     "",
    SandboxConfig:   "",
    Args:            args,
    Logger:          m.log,
    ServerLogWriter: logging.NewWriter(m.serverLog),
})
```

**Its empty**

##### **`pkg/inference/backends/mlx/mlx.go`**

03 / 25

NO SOCKET, NO PRIVS, NO PROBLEM   //   OCI

## Slide 28

# **Ex: Free Willy…errrr Docker PoC**

```text
root@r00t-x1: ~

root@r00t-x1:~# █          root@r00t-x1:~#

root@r00t-x1:~#
```

03 / 25

NO SOCKET, NO PRIVS, NO PROBLEM   //   OCI

## Slide 29

**But Wait there's more…**

## **Some of the other OCI primitives we’ve discovered**

▸ SSRF Family: 3XX redirects, 401 auths, etc

▸ Producer-controlled metadata XSS Family:  stored XSS

▸ Referrers API / attestation / signature Family: DOS, Injection, bypasses

▸ Tar layer extraction Family: LFI , RFI, RCE

▸ Image config / build directive Family: RCE, DOS, RFI, LFI

▸ Parser / ACL / mediaType / digest differentials Family: injection, data leak, bypasses

▸ Cross-class compositions: above chained

**Turns out, OCI can be used to perpetuate almost any traditional attack type, not just SSRF / RFI. You just need to find a way to embed it into your OCI artifact**

24 / 25

## Slide 30

~/dc34/registry-attacks

NO SOCKET, NO PRIVS, NO PROBLEM   //   FIN

25 / 25

## Slide 31

~/dc34/closing

**DEF CON 34**

**No Socket. No Privs.**

**No Problem.**

**$** questions?▊

**David Rochester** · @davidrxchester · **Nicholas Gould** · @gouldnicholas

NO SOCKET, NO PRIVS, NO PROBLEM   //   FIN

25 / 25

## Slide 32

# **References:**

- ● <u>https://www.docker.com/products/docker-desktop/</u>

- ● <u>https://github.com/docker/model-runner/security</u>

- ● <u>https://github.com/ml-explore/mlx-lm</u>

- ● <u>https://github.com/ggml-org/llama.cpp</u>

- ● <u>https://github.com/vllm-project/vllm-metal</u>

- ● <u>https://thehackernews.com/2026/01/researchers-find-175000-publicly.html</u>

- ● <u>https://github.com/ollama</u>

- ● <u>https://github.com/containerd/containerd</u>

- ● https://opencontainers.org/

24 / 25

