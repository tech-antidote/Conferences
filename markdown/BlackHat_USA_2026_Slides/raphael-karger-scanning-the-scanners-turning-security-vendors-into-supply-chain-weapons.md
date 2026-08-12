---
title: "Scanning the Scanners Turning Security Vendors Into Supply Chain Weapons"
speakers: ["Raphael Karger"]
conference: "Black Hat"
conference_full: "Black Hat USA 2026"
edition: "USA"
year: 2026
source_pdf: "BlackHat_USA_2026_Slides/Raphael Karger_Scanning the Scanners Turning Security Vendors Into Supply Chain Weapons.pdf"
pages: 56
sha256: "92fa2b94909529268090befb67505f252ddde483348ad363a9ee57e1cca26c96"
text_chars: 22420
ocr_pages: 2
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T23:15:02Z"
---
# Scanning the Scanners Turning Security Vendors Into Supply Chain Weapons

**Speakers:** Raphael Karger  
**Conference:** Black Hat USA 2026  
**Source:** `BlackHat_USA_2026_Slides/Raphael Karger_Scanning the Scanners Turning Security Vendors Into Supply Chain Weapons.pdf` (56 pages)


## Slide 1

### SCANNING THE SCANNERS

Turning security vendors into supply-chain weapons

Co-founder & CTO @ ZeroPath Raphael Karger

1

## Slide 2

##### Whoami

**Raphael Karger Co-founder & CTO @ ZeroPath** Prior life: Security Engineer @ Google

2

## Slide 3

##### Agenda

**1 Detection**

   - The incident in our scanner and how the research started

- **2 Why Scanners**

   - Why hosted scanners are high-value targets

- **Related**

- **3 Incidents**

   - Vendor-to-customer incidents and the repository-to-vendor path

- **4 Mechanism** Execution and file-read primitives

- **5 Findings**

   - 20 platforms and 5 confirmed boundary failures

- **6 Defenses** Vendor defenses and buyer questions

3

## Slide 4

##### What We Mean by a Scanner

•Hosted code security product accepts a repository or source archive

•Offering one or more of the following:

- SAST

- SCA/SBOM

- Secrets

- IaC

•Focus: **untrusted repository processing** and **what the workers can access**

4

## Slide 5

# **Detection**

5

## Slide 6

##### Initial Alert

###### **LATE DECEMBER 2025**

- Hostile-looking repository submitted through free-tier signup

- Scan failed and triggered an alert

- We treated it as a real incident

6

## Slide 7

##### What We Found

What survived, and what did not

**NO LONGER AVAILABLE**

- Full repository was no longer retained

- Worker terminated shortly afterward

- Only partial worker artifacts remained

###### **PERSISTED TELEMETRY**

- Scan metadata, DNS, and request telemetry remained available

- package.json and packagelock.json were recovered

- Evidence was enough to reconstruct the test path

7

## Slide 8

##### Scanner Probes

###### The recovered files contained several independent probes, not one generic payload package.json

###### **WHAT IT TESTED**

- npm lifecycle execution

- Dependency URL handling

- Manifest parsing

###### package-lock.json

###### **WHAT IT TESTED**

- Lockfile parsing

- Dependency resolution

- Lockfile-specific processing

8

## Slide 9

##### Successful Callback

The only successful callback came from the secret-validation path

- A third-party secret detector attempted online validation

- The **honeytoken** label identified the probe

- The attacker did not cross our worker boundary

**OBSERVED HOSTNAME** honeytoken-a7095a5f. zeropath-ai-staging. d56f72pnmn0ff16jemkg3t9zjeurfme5x. [redacted]

**PROVED  A backend validation path processed the supplied value** DID NOT PROVE  Execution, file access, or compromise of the worker

9

## Slide 10

##### What This Tells Us

- Systematic probing of how we process repositories

   - Symlinks

   - Malicious supply-chain artifacts

   - Honeytokens

- The attacker understands how code security platforms process repositories

   - Probing to see which backend paths were exercised

   - Other payloads were likely present in the repo that we did not capture

10

## Slide 11

##### Probe Infrastructure

Recovered npm_exec probe (no callback observed)

-bf23fc54 npm_exec .zeropath-ai-staging .d56f72….[OAST host] Probe Type Run ID Target Collector unique test run zeropath-ai-staging OAST correlation and Interactsh host npm script execution

- Interactsh is a service for detecting out-of-band vulnerabilities

- The OAST host returned an Interactsh banner

- Random subdomains resolved through wildcard DNS

- The evidence matched an OAST collection service

11

## Slide 12

#### Why We Expanded the Research **It started as** protecting our own platform

• Build Canaries became an internal regression framework

• The same tests were run against selected hosted scanners • Confirmed issues became minimal reproductions and retests

12

## Slide 13

##### Demo Setup

- Local, deliberately vulnerable scanner

• Exploiting Terragrunt RCE through repository-defined hooks

• Synthetic credentials only

Shows repository submission → backend execution → readable worker data

13

## Slide 14

##### Demo

14

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
:~$ nc -vlp 13377
listening on [any] 13377 ...
Tilix: r@debian: ~
E Y OPERATIONS WORKSPACE
Assessments, findings, policy decisions, and evidence
ASSESSMENT TEMPLATES
Policy pack review
Infrastructure wrapper review
EPOSITORY INTAKE
BLIC GIT URL (HTT
Browse. No file selected.
Standard review
LATEST RESULT
STANDARD
```

## Slide 15

# **Why Scanners**

15

## Slide 16

###### The Assumption: Scanning Is Read-Only

###### **ASSUMPTION**

###### **REALITY**

Scanners may invoke package managers, build tools, metadata commands, plugins, or executable configuration

Scanning is often treated as readmanagers, build tools, metadata only processing of untrusted code commands, plugins, or executable configuration Even without code execution, unsafe path handling can read outside the repository

16

## Slide 17

##### The Trust Chokepoint

###### **UNTRUSTED INPUTS**

- Repositories and archives from many customers

- Sometimes self-service submission

- Security-sensitive and regulated customers

###### **SCANNER PLATFORM**

   - Hosted backend that

   - processes repositories and uses customerscoped integrations

- **WORKER BOUNDARY** Can repository-controlled

- processing reach platform authority?

###### **PLATFORM AUTHORITY AROUND THE WORKER**

- Source access and result publication

- Token brokers, registry access, and cloud identity

- Findings, secrets, internal services, and operational context

17

## Slide 18

Why Worker Exposure Matters The impact depends on what the worker can reach:

**DATA**

###### **AUTHORITY**

- Customer source code

- Unpatched findings and secret findings

   - Source-control and registry credentials

   - Cloud or workload identity

- Repository inventory and scan history

- Status, check, pull-request, or remediation paths

18

## Slide 19

# **Related Incidents**

19

## Slide 20

##### Vendor to Customer

The familiar direction: compromise trusted tooling, then follow its distribution path downstream

**Trivy** Malicious releases and GitHub Actions were published

**Checkmarx Customer-Facing Artifacts** Unauthorized GitHub Malicious code was published to → → repository access was VS Code extensions, GitHub reported after the Trivy Actions workflows, and a Jenkins compromise plugin

This is the classic vendor-to-customer path: trusted security tooling becomes the delivery channel

Public incident: Aqua Security and Checkmarx reports, 2026

20

## Slide 21

##### Code to Vendor

This research tests the reverse path: content the vendor did not write reaches its backend

**HOSTILE CODE**

**SCANNER WORKER** Vendor processes the → content before a result is returned

Attacker controls repository files, configuration, paths, or a published package

**PLATFORM AUTHORITY** Worker may expose credentials, → internal services, or write paths

###### **Same trust concentration, opposite direction**

Public incident: Kudelski Security, CodeRabbit PR → production RCE → GitHub App write access, 2025 Public incident: Anthropic, malicious PyPI package → scanner install → credential theft, 2026

21

## Slide 22

# **Mechanism**

22

## Slide 23

##### Prior Work

• OWASP CICD-SEC-4: Poisoned Pipeline Execution • MITRE ATT&CK T1677: Poisoned Pipeline Execution

- Living off the Pipeline (LOTP)

- …and many others

**Contribution:** not a new primitive. A systematic sweep of an untested product category, and tooling to automate the creation and testing of payloads.

23

## Slide 24

##### Repository Processing Surfaces

###### **PACKAGE AND BUILD METADATA**

**PLUGINS & EXECUTABLE CONFIGURATION**

setup.py metadata commands, gemspec evaluation, and lifecycle scripts external checks, custom rules, and repository-controlled configuration

###### **LANGUAGE & BUILD TOOLING**

repository-controlled build, editor, or language-server configuration

**DEPENDENCY FETCHING**

manifests, lockfiles, registry URLs, and submodules

**PATH HANDLING**

symlinks, archives, absolute paths, traversal, and special files

24

## Slide 25

##### Arbitrary File Read

- No code execution is required

- Scanner reads a repository-controlled path

• Symlinks, archive paths, or unsafe handling can escape the repository

- Worker-local credentials or service configuration can be exposed

25

## Slide 26

##### Build Canaries Pipeline

**Crawl docs:** extract directly named or strongly implied processing surfaces from same-domain vendor documentation. Count only tools with RCE or SSRF potential

**Compare coverage:** match each surface against registered generator IDs, descriptions, triggers, files, and tags

**Review candidates:** missing coverage can generate candidate code, but human review is required before it enters the deterministic Python/Jinja corpus

**Render:** accepted generators produce a fresh repository artifact with a payload ID and unique run ID **Validate:** mount the artifact in Docker, run the declared target tool, and pass only on the matching callback; hosted-vendor testing remains separate

26

## Slide 27

###### Local Validation Uses the Real Target Tool

**Example: npm-preinstall**

- Render package.json with a fresh callback path

- Mount the generated repository at /workspace

- Spawn npm install inside a disposable Docker container

- Observe GET /npm-preinstall-<run-id>

- Pass only when the expected payload ID and run ID arrive before timeout

- Do not count stdout, exit code, or an unrelated request as proof

27

## Slide 28

##### Testing Workflow

Start from vendor documentation

- Capture explicit tool references and strongly implied processing surfaces

- • Keep only surfaces with realistic RCE or blind SSRF potential • Reuse an existing payload, or create and validate one locally • Add validated generators to the payload library

- Probe the hosted scanner

   - Generate a probe-mode repository with unique payload and run IDs

   - • Record which backend paths fire

   - For RCE paths, confirm with a tailored bounded payload

   - • For blind SSRF paths, validate only minimal known-service interactions

28

## Slide 29

##### Example: Checkov External Checks

Documentation signal: product supports Checkov external checks or custom policies

Inference: Checkov may load repository-provided Python modules Build Canaries action: generate a minimal external-check payload when corpus coverage is missing

Docker validation: run the payload against Checkov to confirm the behavior before adding it to the corpus Product test: submit the probe, then use path-specific validation if the path fires

29

## Slide 30

# **Findings**

30

## Slide 31

##### Scope

- 20 self-service hosted scanners were selected for this research (excluding ZeroPath)

• Requiring open signup was the main constraint on the candidate pool • Comparable workflow: hosted code-security or software supply-chain product processing a submitted repository

- Interpretation: this was a selected sample, not a random market survey or prevalence estimate

31

## Slide 32

##### Conduct

• Reachable path: self-service or public access to the tested functionality, with public evidence of real use

- Access limits: no false identities, sales-assisted access, customer impersonation, or social engineering

- Testing stopped immediately when requested

- No lateral movement, persistence, or access to customer data

32

## Slide 33

##### Reporting

- Reports were sent in January 2026

- Each report included recommendations and runnable proof-of-concept material for validation

- When a timely response did not arrive, we used additional public or program-approved contact channels

- Vendor disclosure program rules and stop requests were respected throughout the process

- One vendor awarded its maximum bug bounty payout

- Anonymized uniformly; selective disclosure should not become marketing material

33

## Slide 34

##### How We Validated Worker Impact

- Validation was intentionally minimal: collect only enough evidence to prove worker impact (usually just environment variables)

- When a vendor needed more confirmation, checks stayed narrow, such as limited filesystem enumeration or IMDS reachability

- Testing stopped after reproducible evidence; customer data was not accessed

34

## Slide 35

##### What Counted as a Finding

**1. Path Signal:** a callback, request, tool output, or behavior change only showed that a backend path reacted

**2. Boundary Primitive:** we separately established repository-controlled execution or an out-ofroot file read

**3. Worker Impact:** we also observed sensitive vendor-local material or privileged internal reach from the worker context

**Counted:** both the primitive and meaningful worker impact were required; a callback alone was never enough

35

## Slide 36

##### Cases We Did Not Count

**1. Broken Scan:** one canary caused a scan to fail. We did not isolate the cause or attempt an RCE confirmation

**2. Vendor Request:** the vendor proactively asked us to stop, and we stopped immediately. Dependency fetching suggested a possible RCE-capable path

**3. Proxy Anomaly:** HTTP_PROXY and HTTPS_PROXY routed some exfiltration attempts unexpectedly

**Black-box caveat: a non-trigger could reflect a payload mismatch, required modification, proprietary processing, blocked egress, or real protections**

36

## Slide 37

##### Results

self-service hosted scanner → **20** platforms tested

**confirmed boundary 5 failures**

**4 1 3** cases with backend case with an out-of-root file partial signals execution read

37

## Slide 38

##### Confirmed Cases

**Vendor**

**Attack Vector**

**What Was Exposed**

**Vendor A**

**Vendor B**

Checkov config RCE

Checkov config RCE

Cloud credentials; internal service secrets Cloud credentials; production database credentials and services; internal service secrets

**Vendor C** Ruby gemspec eval

Cloud token; orchestration service-account token; RSA private key (SIGNING_KEY)

**Vendor D** Python setup.py exec

Cloud IAM credentials; GitHub PAT; Docker Hub PAT

**Vendor E** Symlink traversal

Payment processor key

38

## Slide 39

##### Vendor D: Metadata Lookup Code Execution

Observed command: python3.9 -Wi setup.py --name --version

- Main SCA path did **not** trigger

- Auxiliary SBOM collector triggered setup.py

- Loading setup.py runs top-level Python before setup() returns package metadata

###### **Selected PoC lines**

39

## Slide 40

##### Vendor D: HTTPS Attempted, DNS Observed

The payload called urlopen(); the collector saw hostname lookups but no usable HTTP request

- The OAST DNS service received unique queries for every attempt

- Environment variables were hex-encoded and split into 50-character chunks

- The exact vendor-side egress control was not determined

**<chunk number>.<50 hex characters>.<vendor>.<oast domain>**

40

## Slide 41

##### Vendor D: Vendor-Owned Credentials in the Worker

• Cloud IAM credentials were present in the worker; exact permissions

were not enumerated

• GitHub personal access token was present in the same worker

• Docker Hub personal access token was present in the same worker

41

## Slide 42

##### Vendor E: Symlink Traversal

**repo/secrets.txt  →  /proc/self/environ  →  payment processor key in the UI**

- Repository input: a symlink named secrets.txt pointed to /proc/self/environ

- Scanner behavior: the detector followed the link and scanned its own worker environment as file content

- Observed result: a payment processor key matched normal secret rules and appeared in the findings UI

- This counted because repository-controlled file selection caused an out-of-root read of vendor-local data

42

## Slide 43

###### Vendor B: Production Database Credentials

- Source: DATABASE_URL came from Vendor B's worker environment after repository-controlled execution

   - Complete material: the value included scheme, production hostname, database name, username, and password

- Vendor confirmation: the database was live and enabled access to:

   - GitHub OAuth grants (carrying the read and write permissions of the public app)

   - Unpatched findings

   - Secrets

   - SLO/SLA violations

   - Customer information

43

## Slide 44

###### What the Exposed Credentials Could Enable

- **Vendor-confirmed**

   - Production database; the vendor confirmed it backed customer findings, GitHub OAuth grants, and policy state

   - Payment processor key; enabled vendor-side payment API actions

   - GitHub and Docker Hub PATs; confirmed active

   - Two cloud IAM credentials in separate environments; confirmed access within their policy

44

## Slide 45

###### What the Exposed Credentials Could Enable

- **Exposed, scope not enumerated**

   - An RSA private key stored in plaintext as the value of an environment variable named “SIGNING_KEY”

      - If used to sign commits, tags, or releases, an attacker could forge signatures the vendor's downstream checks trust

   - Other cloud IAM credentials; present across the affected environments, permissions not enumerated

45

## Slide 46

###### Patterns Across the Confirmed Cases

- Executable surfaces: setup.py, gemspec evaluation, and Checkov custom checks ran as code during repository processing

- Auxiliary helpers: at Vendor D the SBOM collector triggered while the main SCA path did not

- Worker-local material: the confirmed cases exposed vendor-owned credentials

- Path escape: Vendor E's symlink reached /proc/self/environ with no code execution

46

## Slide 47

# **Defenses**

47

## Slide 48

##### Where the Boundaries Failed

The same five boundaries, scored against what we actually observed

**BOUNDARY WHAT WE OBSERVED**

**EXECUTION**

**FILE ACCESS**

4 of 5: Checkov config at A and B, gemspec at C, setup.py at D 1 of 5: symlink to /proc/self/environ at E

**NETWORK**

**CREDENTIALS LIFETIME & STATE**

Partial where present: DNS out and HTTP blocked at D; proxy routing left one case ambiguous 5 of 5: operational vendor credentials reachable from the analyzer Not testable from outside: no external signal distinguishes a fresh worker from a reused one

Four boundaries we could measure from outside; the fifth is why buyers have to ask

48

## Slide 49

##### What to Enforce

Assume the analyzer can run attacker-controlled behavior; constrain what it can execute, read, reach, and retain **BOUNDARY WHAT SHOULD HAVE BEEN ENFORCED**

**EXECUTION**

Static metadata first; scripts, plugins, and custom rules off by default

**FILE ACCESS**

The repository snapshot is the only readable tree; no symlink, archive, or absolute-path escape

**NETWORK**

Default-deny egress; broker dependency fetches; block metadata, private ranges, internal DNS, and proxies

**CREDENTIALS** No SCM, cloud, registry, database, or publishing tokens in analyzer env, files, or workload identity Fresh sandbox per scan; no writable shared caches; scratch destroyed after the result **LIFETIME & STATE**

The goal is not “containerized”; it is a worker that has nothing durable or privileged to lose

49

## Slide 50

##### Concrete Levers

What to reach for at each boundary

###### **BOUNDARY CONCRETE LEVERS**

**EXECUTION**

no-script tool modes, command allowlists, non-root runner, seccomp, AppArmor

**FILE ACCESS**

**NETWORK**

read-only bind mounts, mount namespace / chroot, openat2, Landlock, AppArmor, safe extractors dependency broker / cache, egress proxy, DNS allowlist, NetworkPolicy / Cilium, nftables

**CREDENTIALS** source fetcher / result publisher split, short-lived scoped tokens, held outside the worker **LIFETIME &** microVM / gVisor / Kata, tmpfs scratch, read-only content-addressed cache, teardown checks **STATE**

Full matrix with every primitive: behind the QR code

50

## Slide 51

##### A Safer Scanner Design

One worker owns the scan end to end. Tool code only ever runs in containers that hold nothing.

###### **PLATFORM**

multi-tenant · durable
job queue
ingestion API
findings DB

**Binds tenant + job** server-side **Re-validates** every submitted result **Workers never** write the DB directly

###### **SCAN WORKER**

- lease job one per job · owns the scan end to end · disposable **1** Leases the job from the platform **2** Clones at the pinned commit, stages a read-only snapshot **3** Spawns a container per tool and feeds it the snapshot **4** Collects output as untrusted data, normalizes it **5** Submits results, then reaps every container

- submit results **Runs no tool code** in its own process **SCM token dropped** before any container starts

lease job

snapshot (read-only) + args findings · hostile input
UNTRUSTED · one ephemeral container per tool, spawned and reaped by the worker
container container container
tool 1 tool 2 tool 3
no credentials · no workload identity · no egress · ro /repo · tmpfs · destroyed after result

clone @ pinned commit

###### **CUSTOMER SCM**

external system **SCM-READ** short-lived, repo-scoped

###### **DEPENDENCY BROKER**

the only egress a container gets: allowlisted package fetches

The worker owns the job. The containers own nothing. Credentials never share a process with tool code.

51

## Slide 52

##### What Buyers Should Ask

Ask for concrete repository lifecycle and worker-boundary details

- Repository lifecycle: What happens from connection or upload through the final result?

- Execution boundary: Which stages or components are shared and which are dedicated?

- Repository-controlled behavior: Which features or integrations can change how a scan runs?

- Adversarial testing: How are scanner changes tested against malformed or hostile repositories?

   - Run Build Canaries against your own vendors and see whether you get callbacks Strong answers describe actual stages, credentials, worker lifetime, and recent design changes

52

## Slide 53

##### Open-Source Releases

###### **BUILD CANARIES**

###### **DVASP**

Generator framework + regression corpus

Damn Vulnerable Application Security Platform

<u>github.com/rek7/build-canaries</u>

<u>github.com/rek7/dvasp</u>

- Test scanner processing paths

- Re-run the same payloads after fixes

- Use deterministic generators and product-specific probes

- Deliberately vulnerable local scanner

- Synthetic credentials and controlled failures

- Practice detection and containment safely

53

## Slide 54

##### Thank you!

###### **Slides, Contact and Tools**

bh2026_qr_v2.png

Takeaways:

- Supply chain risk runs both directions

- Severity lives in the worker, not the bug

- Don't accept “it's containerized”

<u>raphael.karger.is/bh-2026</u>

54

## Slide 55

## Appendix

55

## Slide 56

Full Demo

56

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Full Demo
Mozilla Firefox Ml Tilix: r@debian: ~/ouild.
G
debian: ~/build-canaries v 2700.1
(.venv) $ nc -vlp 13377
listening on [any] 13377
] Assessments, findings, policy decisions, and evidence
ECURITY OPERATIONS WORKSPAC
Dashboard
APPLICATION SECURITY OPERATIONS
AppSec Posture Dashboard
Findings
Assessments
Activity
Documentation
$ sudo docker run --rm -it projectdiscovery/interactsh-client: latest EVIDEN
rver oast.live -v -duc 1
RECENT FINDINGS v WORKSPACE SCOPE
projectdiscovery.io
Infrastr
] Listing 1 payload for 00B Testing ucture
S| £07! 745) v
] d920cbupSbcc73ed92f07btgbmg8745hm.oast. live wrappe
[
{i
0 r
review
genera
teda
finding
MMENDED EVIDEN!
EVENTS
Infrastr
ucture
wrappe
56
black hat
$s)
```
