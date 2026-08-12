---
title: "GitHub Can Tell You're Being Hacked. You're Just Not Listening Building EDR for GitHub from Its Own Event Stream"
speakers: ["Mor Weinberger", "Yossi Weizman"]
conference: "Black Hat"
conference_full: "Black Hat USA 2026"
edition: "USA"
year: 2026
source_pdf: "BlackHat_USA_2026_Slides/Mor Weinberger&Yossi Weizman_GitHub Can Tell You're Being Hacked. You're Just Not Listening Building EDR for GitHub from Its Own Event Stream.pdf"
pages: 46
sha256: "8d3e2863bb1854c28632838c18e9dea1a8c6db8ff3c0a096ef97f6998353abc0"
text_chars: 23148
ocr_pages: 9
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T23:13:01Z"
---
# GitHub Can Tell You're Being Hacked. You're Just Not Listening Building EDR for GitHub from Its Own Event Stream

**Speakers:** Mor Weinberger, Yossi Weizman  
**Conference:** Black Hat USA 2026  
**Source:** `BlackHat_USA_2026_Slides/Mor Weinberger&Yossi Weizman_GitHub Can Tell You're Being Hacked. You're Just Not Listening Building EDR for GitHub from Its Own Event Stream.pdf` (46 pages)

## Slide 1

GitHub Can Tell You're Being Hacked. You're Just Not Listening : Building EDR for GitHub from Its Own Event Stream

## Slide 2

# whoami

###### **Mor Weinberger Software Architect**

###### **Yossi Weizman Principal Security Researcher**

2

## Slide 3

###### Why Now

_Based on OSV data_

4

## Slide 4

###### Why Now Recent notable incidents

**Nov 24, 2025 Shai-Hulud 2.0**

Self-replicating npm worm

**Mar 23, 2026 Checkmarx KICS**

GitHub Actions hijacked using stolen CI credentials

**Mar 27, 2026**

###### **Telnyx**

Trojanized PyPI release of the official Python SDK

**Apr 22, 2026**

###### **Bitwarden CLI**

Malicious npm package pushed via a compromised GitHub Actions workflow

**Apr 30, 2026 PyTorch Lightning**

Backdoored release pushed via a compromised maintainer account

**May 18, 2026 Megalodon**

5k+ GitHub repos backdoored via automated forged-bot commits

**Jul 2026 PolinRider (DPRK)**

100+ malicious packages across npm, Packagist, Go, Chrome

###### **Mar 19, 2026 Trivy (Aqua)**

CI/CD compromise via GitHub Actions; CVE2026-33634

###### **Mar 24, 2026 LiteLLM**

Trojanized release exfiltrating LLM provider API keys

###### **Mar 31, 2026 Axios (npm)**

70M+ weekly downloads; crossplatform RAT

###### **Apr 29, 2026 SAP npm packages**

Mini Shai-Hulud worm poisons SAP-related packages for credential harvesting

###### **May 11, 2026 TanStack**

Abusing GitHub Actions cache to push 84 malicious versions of npm packages

**Jun 1, 2026 Jul 14, 2026 Red Hat AsyncAPI @redhat-cloud-** CI token theft via **services** GitHub Actions

CI token theft via GitHub Actions

32 npm packages poisoned via OIDC Trusted Publishing;

## Slide 5

###### What’s in Our Scope?

Supplier

Consumer

15

## Slide 6

###### What’s in Our Scope?

Supplier Supplier Consumer

16

## Slide 7

###### What’s in Our Scope?

###### **In this session, we will focus on GH-related attacks**

17

## Slide 8

###### Many attacks – same techniques

Artifact poisoning

Mass tag push Temporary tag swap Malicious release

###### Identity & commitmetadata forgery

Forged Forged app’s maintainer’s identity identity

Forged  Forged commits
timestamp and  tree
parent commits

###### OIDC abuse

Registry trustedCloud OIDC publish abuse federation abuse

###### Evidence destruction

Delete workflow Delete forks & runs branches Remove user Disable webhooks Code & artifact Base repo revert commit URL

Workflow injection & Trigger abuse

pull_request_target Direct abuse workflow override Secrets exfiltration Cache in workflow logs poisoning Runner’s memory dump

###### Malicious code injected via fork\off-repo

Malicious code Malicious code stored in fork stored in a dangling commit Malicious code in a temporary branch

19

## Slide 9

###### Many attacks – same techniques

Mass tag push Trivy tj-actions codfish
Temporary tag swap reviewdog
Forged maintainer’s identity Trivy tj-actions megalodon TanStack RedHat
Forged app’s identity tj-actions TanStack
Forged timestamp & parent commits Trivy PolinRider
Forged commits tree Trivy
Off-branch commit tj-actions reviewdog TanStack RedHat
Malicious code in a temporary branch Bitwarden
pull_request_target abuse TanStack AsyncAPI
Direct workflow override megalodon Bitwarden RedHat
Secrets exfiltration in workflow logs tj-actions reviewdog
Cache poisoning TanStack
Runner’s memory dump Trivy reviewdog tj-actions TanStack
Delete workflow runs Bitwarden
Delete forks & branches reviewdog Bitwarden TanStack
Remove user reviewdog
Disable webhooks reviewdog
Code & artifact revert reviewdog TanStack
Base repo commit URL TanStack
Registry trusted-publish abuse TanStack Bitwarden RedHat AsyncAPI
Trivy tj-actions reviewdog megalodon Bitwarden TanStack RedHat PolinRider codfish
AsyncAPI

## Slide 10

##### TTPs - examples GIT metadata forgery

###### GIT metadata can be set to any value

```
author     name | email | date
committer  name | email | date
```

```
message · tree · parent(s)
```

**The pusher is the authenticated user with GH. This is the field you can trust.**

###### GitHub resolves the author.email field to its legitimate GitHub (clickable + avatar)

- `$ git config user.name  "web-flow"`

- `$ git config user.email "…@users.noreply.github.com"`

- `$ git commit -m "Add test.txt"`

**Detection: compare the author's name to the authenticated user**

author = `head_commit.author.username` ← from the commit (forgeable) pusher = `sender.login` ← authenticated by GitHub (trusted) flag when **`author ≠ pusher`**

21

## Slide 11

TTPs - examples Cross-org forged-author correlation

Attacks are often automated. Attackers use same forged identities against multiple victims.

Forged identities in the repo which appear in other repos as well – **is a strong indication of compromise. Seen also in: Shai-Hulud, Megalodon**

The reused email is indexed by GitHub - pivot from one repo to the whole campaign: `GET /search/commits ?q=author-email:` **`x@fake.dev`**

**Detection: Find large-scale forged identities using GH Search API** For each commit where author ≠ pusher: GET /search/commits?q=author-email → collect owners alert if same email spans ≥ x unrelated owners (orgs\users)

## Slide 12

TTPs - examples Mass tags push

**Goal:** move many release tags onto one poisoned commit, so every workflow that pins the action by tag `(uses: org/action@vN)` runs the malicious code.

```
$ git tag -f v1 v2 v3 … v46  <poisoned>
```

```
$ git push --force origin --tags
```

Tags are movable (mutable) pointers

**Reliable detection must track tag changes via tags API:**

`GET /repos/{owner}/{repo}/git/refs/tags` →  store SHA per tag **`old_sha ≠ new_sha`** ⇒ tag moved.

**<u>Many tag changes = potentially mass tag poisoning</u>**

###### **Tag pushes aren’t visible in GitHub Activity:**

**They are logged in webhooks, but….**

_https://docs.github.com/en/webhooks/webhook-events-and-payloads#push_

## Slide 13

##### TTPs - examples OIDC abuse

**Old way:** workflow publishes with a stored token ( `NPM_TOKEN` in GitHub Secrets) **OIDC:** workflow with `id-token: write` mints its own short-lived token to authenticate with the cloud / registry. **→ The workflow IS the identity.**

**The attacker's goal shifts: Steal a secret  →  Get an OIDC-granting workflow to run**

Modify a workflow that grants OIDC, and get it to run:

```
on: push
permissions:
  id-token: write
```

**Detection: track new or modified workflows that mint OIDC tokens Examples:**

**- Direct push to publishing workflow**

**- Token read from risky workflow (e.g. pull_request_request)**

## Slide 14

##### Same trust. Different object

**Same version string. Three different trust models.**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Same trust. Different object
te |
=" vil.2.3 NEW WO ene
COMMIT app-v1.2.3.zip app-v1.2.3.zip
(current) (previous)
Package registry Git tags
(IMMUTABLE |
Sa at
Release assets
IDARIE |
MAIAT
» VY ArrAve” |
Same version string. Three different trust models.
black hat
2026
```

## Slide 15

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Implant into an existing release
v1.2.3 Release v1.2.3 Release
app-v1.2.3.zip - oo) app-v1.2.3.zip
12.4 MB 12.4 MB
WRITE ACCESS
GITHUB ACTIONS
RUNNER + GITHUB_TOKEN
INJECTION POINT
PR - ISSUE - CONTRIBUTOR KEY
DELETE ORIGINAL UPLOAD MALICIOUS ZIP
RELEASE ZIP ONTO SAME RELEASE
COVER TRACKS
STOLEN CREDS
PAT - ACCOUNT KEY
black hat
2026
```

## Slide 16

###### **Tampered Release Artifacts**

###### **What the UI answers**

Who signed the commit at the first place Key known to GitHub

###### **What it does not**

Release maturity Whether assets were swapped

**Verified ≠trustworthy binary**

## Slide 17

**Same trust chrome. Different maturity.**

###### **Checksums prove integrity of whatever was uploaded - including malware.**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Same trust chrome. Different maturity.
Releases / v1.2.1
‘oworld Public & Pin QWatch 0 ~ —-Y Fork 2 ws
1 2 11 ‘eee B vscan-linux-checksums (16).txt ~
Latest
arr . pe al ae , VIZ atest 05713 fea547eef24079200972115234465d152e08S504Bf8eBfDIGSSGTebb vscan_1.2.11_Linux_end64. zip
eee B vecan-linux-checksums (15).txt ~ Q github-actions released this 11 minutes ago © 1.2.11 © 6e56a63
Releases / v2.01 Besedes2701eTetOctocecdSeeserSbacte25tetO627S2dcee260204a40072¢ vecan_1.2.11 Lint amdet.zip
V1.2.11 ie Changelog
© oithub-actions released this 4 minutes ago © vi2.11 © 6e56a63 © es U; build ymi
* (3@a2ec6 Update build.yml
Changelog + (G88b887) Update build. ym!
+ (G2S8R6R) Update build. ymi * (Jec@d36 Update build.yml
+ (GERREEE) Update build.ymi * (4cafe2a Update build.yml
* |188baa7 Update build. ym
+ (TEERESE) Update build. ym!
* (deate2s Update build. ym!
+ (GRETIR Update build ym!
* Tac7iaf Update build. ym!
vAssets 4
v Assets @ @ vscan-linux-checksums.txt 95 Bytes
@ vacan-linux-checksums.txt 95 Bytes @ vscan_t.2.11_linux_amd64.zip 4 Bytes
@ vecan_1.2.11_Jinux_smd64.2ip 550 KB
Source code (zip)
Source code (zip)
Source code (targz) f) Source code (tar.gz)
ic) (3)
Checksums prove integrity of whatever was uploaded - including malware.
black hat
```

## Slide 18

**Report to Github Bug bountry**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Report to Github Bug bountry
Although this warning does not explicitly mention releases, it does state that the GITHUB_TOKEN is granted write
permissions on the repository, which is all that is required to create, edit, and delete releases.
Based on the
feedback you've provided here, I've added the suggestion to add timestamps to release assets to our internal feature
request list, and the team is actively working to make these improvements to the GitHub interface:
| think you should emphasize the creation time and modify the time of the assets on the release page
We greatly appreciate the thoroughness of this report and the improvement suggestions made throughout, so we'd like
to offer you a small reward as thanks.
black hat
2026
```

## Slide 19

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Report — Signal — Detection
DISCLOSE
Bug bounty report
~
la
PLATFORM
v Assets 4
Name Size
Q agent-linux-amd64 12.4 MB
Q agent-linux-arm64 11.8 MB
 checksums.txt 1.2 KB
B release-notes.md 3.6 KB
Created
May 12, 2025
08:14:22 UTC
May 12, 2025
08:45:37 UTC
May 12, 2025
08:46:01 UTC
May 12, 2025
08:46:15 UTC
~\
rs
DETECT
release-asset-time-skew
08:14:22 08:45:37
UTC UTC
A 31m 15s
Intended behavior. New metadata. Detectable swap.
black hat
2026
```

## Slide 20

**Tampered Release Artifacts**

34

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Tampered Release Artifacts
Compare ~
v1.0.0 Gc compare + ) (A v1.0.0
mo5084-beep re d this 12 minutes ago D v1.0.¢ C mo5084-beep released this 12 minutes ago .0 © 4a22e4c ©
vy Assets 8 v Assets 8
release.pub 693259. 451 Bytes i @ release.pub sha256 . s 12 minutes
SHA256SUMS : _ 2 Byte 12 minutes ago @ SHA256SUMS : ee 12 minutes ago
7)
@
@ tool-darwin-amd64 a Bytes 12 minutes tool-darwin-amd64 S| 2S 12 minu'
@
tool-darwin-amd64.sig sha 256 Bytes 12 minutes ago @ tool-darwin-amd64.sig sha256:71482d7... 12 minutes ag
tool-linux-amd64 s = 22 Byte: ninutes ago @ tool-linux-amd64 31eed41... 2 minutes ago
tool-linux-amd64.sig h Y) es 256 Bytes 12 minutes ago tool-linux-amd64.sig 56: 80 0d... S 2 minutes
Source code (zip) ninutes ag i) Source code (zip) 12 minutes ago
Source cod 13 minutes ago i) Source code (tar.gz) 12 minutes ago
black hat
2026 34
```

## Slide 21

### The Engine

github.com/supplychain-labs/github-threat-detector

## Slide 22

###### The Engine

**LISTEN**

ingest platform activity

**Webhooks**

live push stream

###### **GitHub APIs**

events · commits · tags actions · activities

**Git inspect** bare clone / objects

## Slide 23

###### The Engine

LISTEN REMEMBER
ingest platform activity one activity memory
Webhooks
PostgreSQL
live push stream
GitHub APIs
events · commits · tags Unified View
actions · activities
Context tables
Git inspect
tags history · commits
bare clone / objects
workflows · git_repo_checks

## Slide 24

###### The Engine

LISTEN REMEMBER
ingest platform activity one activity memory
Webhooks
PostgreSQL
live push stream

GitHub APIs
events · commits · tags Unified View
actions · activities
Context tables
Git inspect
tags history · commits
bare clone / objects
workflows · git_repo_checks

DETECT
behavioral scoring
SQL rule runner
30+ detection rules
attack-class families
Baselines
who pushes · tag norms

## Slide 25

###### The Engine

LISTEN REMEMBER DETECT ACT
ingest platform activity one activity memory behavioral scoring investigate & respond
Webhooks
PostgreSQL SQL rule runner Findings
live push stream
GitHub APIs
30+ detection rules Timeline / IR
events · commits · tags Unified View
actions · activities attack-class families when · who · what else
Context tables
Git inspect Baselines
tags history · commits UI / CLI
bare clone / objects
who pushes · tag norms
workflows · git_repo_checks

## Slide 26

###### Architecture

Collect -> Enrich -> Detect -> Act

INGEST
Snapshot Collectors
Webhook receiver
CLI collect / analyze

DETECT
PostgreSQL SQL detection queries
30+ behavioral rules
events · context
findings
system of record
INVESTIGATE
Frontend
timeline · kill chain
Compound
CLI report

## Slide 27

###### Architecture

Collect -> Enrich -> Detect -> Act

DETECT
INGEST
PostgreSQL SQL detection queries
Snapshot Collectors
30+ behavioral rules
events · context
findings
system of record
Webhook receiver
ENRICH INVESTIGATE
CLI collect / analyze
Frontend
Author Enrichment
timeline · kill chain
Compound
CLI report

## Slide 28

###### **GitHub Telemetry**

###### **Webhooks**

live push stream

- Real-time

- Rich telemetry

- Harder setup

- Can be disabled

- Missed events are gone

42

## Slide 29

###### **GitHub Telemetry**

###### **GitHub API**

- **Webhooks GitHub API** live push stream snapshot baseline

- ●  Real-time ●  Snapshot & compare over time ●  Rich telemetry ●  Can't be removed as a channel ●  Harder setup ●  API object can be removed ●  Can be disabled ●  Less verbose than webhooks

   - Snapshot & compare over time

   - Can't be removed as a channel

   - Less verbose than webhooks

- Missed events are gone

- Rate limited

43

## Slide 30

###### **GitHub Telemetry**

Webhooks

- live push stream

- ●  Real-time ●  Rich telemetry ●  Harder setup ●  Can be disabled

- Missed events are gone

GitHub API

snapshot baseline ●  Snapshot & compare over time

- Can't be removed as a channel

- API object can be removed ●  Less verbose than webhooks

- Rate limited

Git Inspect

tag provenance
●  Read objects, not just events
●  Great for Enrichment

- Harder to stand up ●  Not real-time ●  Heavier than API / webhooks

44

## Slide 31

###### Detections

|**TTP family**|**Example of detections**|
|---|---|
|Artifact poisoning|Mass tag force-push burst   ·   Flip-flop tag   ·   Many tags → same commit    ·   Many tags → same parent|
|Identity & commit-metadata forgery|Author ≠ pusher   ·   Committer ≠ pusher   ·   Cross-owner forged author   ·   Unresolvable author email   ·   Tag parent in
the future   ·   Unverified commits|
|Malicious code via fork / off-repo|Tag from non-existing branch  (dangling commit)|
|Workflow injection & trigger abuse|pull_request_target pwn-request   ·   Direct workflow push to default   ·   Secret base64 exfil in logs|
|Evidence destruction|Workflow-run deleted|
|OIDC abuse|OIDC risky workflow run   ·   Direct OIDC workflow push to default branch|
|**Overall**: 22 rules + 12|beta rules|

https://github.com/supplychain-labs/github-threat-detector/tree/main/analyzers/detection_queries

47

## Slide 32

###### Detections

**severity MITRE ATT&CK tactic**

**Detection Logic**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Detections
severity
| path}' ran on untrusted trigger r 4} 1 {_repo}) in {repo_name}
——— MITRE ATT&CK tactic
1 whose file (in v
where the run fired on an untrust
(pull_request_ta workflow_run, issue_comment, PR
the run's
head_repo ry dif
can mint an OIDC token from atta r-influenced
-Pepo_name,
-id AS run_id,
-workflow_path,
«event trigger,
-head_branch,
.payload->"head_repository'->>'full_name' head_repo,
-actor_login,
.run_started_at Detection
FROM workflow_runs r Logic
OIN workflow_files f
ON f.repo_name = r.repo_name
AND f.path = r.workflow_path
WHERE f.content ILIKE '%%id-token: write%%'
AND (
r.event IN (‘pull_request_target', ‘workflow_run',
"issue_comment', ‘pull _request_review', 'pull_request_review_comment')
OR (r.payload->"head_repository'->>'full_name')
TS DISTINCT FROM (r.payload->‘repository*->>"full_name') black hat
```

## Slide 33

###### Compound Rules

COMPOUND RULE
DETECTION A DETECTION B
Mass tag poisoning
Push of many tags to the  Tag points to off-branch
+
to an unreachable commit
same commit commit
LOW MEDIUM HIGH

## Slide 34

#### How did we evaluate it?

52

## Slide 35

###### <u>Simulations</u>

||• Author spoofed
• Re-parent release commits onto today's HEAD
|Aqua Security blog
Microsoft Security Blog|
|---|---|---|
|**CVE-2026-33634**|• Mass tag force-push
•Man tas → same tree / same arent|Wiz blog|
|**`(trivy-actions incident)`**|y g      p
• Impossible lineage (parent newer than child)
• Unsigned / unverified commits on tags||
||• Malicious commit in a fork|GH issue|
|**CVE-2025-30066**|• Force-repoint all tags onto that single commit
|Step Security blog
|
|**`(tj-actions/changed-files incident)`**|• Commit identity spoofed as a bot
• Unsigned commit where baseline was signed
• Tag target on no branch (off-branch / from a fork)|Wiz blog|
|**CVE-2025-30154**
**`(reviewdog incident)`**|• Tag v1 force-repointed to a malicious commit
• Malicious commit off every branch (tag ref only)
• Flip-flop cover-up: v1 reverted back to clean|GH issue
Wiz blog|
|**CVE-2026-45321**
**`(tanstack incident)`**|• pull_request_target “Pwn Request”: untrusted PR ref built
• Cache poisoning across fork
base boundary
• Shared cache key between PR-target and publish
• Anti-forensics: PR closed + fork branch deleted
• OIDC theft on the trusted runner|TanStack
blog
Step Security blog|
|**CVE-2026-42994**|• Existing publish workflow modified on a side branch
• Branch guard removed; trigger change to on: push: tags
• id-token: write: registry token exchange
•Stl tk hd t  l b64|GH issue
Bitwarden
community forum
Step Security blog|
|`(`**`Bitwarden-CLI incident`**`)`|oen oen ecoe o run og (ase)
• Unsigned commit on the publish workflow
• Workflow run fires from a non-default ref (the tag)
• Run + logs deleted afterward (anti-forensics)||
||• Direct push to default branch, no PR (d-PPE)
• Adds a backdoor under .github/workflows/|SafeDep
blog|
|**`Megalodon campaign`**|
• Forged author with unresolvable email (author ≠ pusher)
• Same forged author across many repos/owners in a short window
• Workflow grants id-token: write||

https://github.com/supplychain-labs/github-threat-detector/tree/main/simulations

54

## Slide 36

###### Noise lab: validating detections

DECIDE
CANDIDATE MEASURE
FIELDS IN GH  Keep / demote
Incidents Prevalence
ARCHIVE? Allowlist
Simulations Incident recall
Correlator
ENRICH
GitHub API
git inspect

https://www.gharchive.org/

56

## Slide 37

###### Noise lab: validating detections

DECIDE
CANDIDATE MEASURE
FIELDS IN GH  Keep / demote
Incidents Prevalence
ARCHIVE? Allowlist
Simulations Incident recall
Correlator
ENRICH
GitHub API
git inspect

https://www.gharchive.org/

57

## Slide 38

## Demo

58

## Slide 39

60

## Slide 40

62

## Slide 41

###### Recent Github Hardening & Mitigations

###### **Notable recent changes:**

**Immutable releases (October 2025)**

GitHub permanently locks Release’s tag and assets so they can't be moved, edited, or deleted

**Workflow execution protections (preview) (June 2026)**

Central allowlist of who and which events may trigger workflows, evaluated before the run.

**Safer pull_request_target defaults** `actions/checkout` now refuses to fetch fork PR code in privileged workflows unless you explicitly opt out. **(June 2026)** (default)

**Read-only cache for untrusted triggers** Workflow runs started by non-collaborators get a cache token with read-only permission, limiting the poisoning **(June 2026)** path. (default)

65

## Slide 42

###### Recent Github Hardening & Mitigations

**Safer pull_request_target defaults** `actions/checkout` now refuses to fetch fork PR code in privileged workflows unless you explicitly opt out. **(June 2026)** (opt-out) **Read-only cache for untrusted triggers** Workflow runs started by non-collaborators get a cache token with read-only permission, limiting the poisoning path. **(June 2026)** (opt-out)

###### **Example: TanStack npm supply-chain (May 2026)** **`/simulations/sim-tanstack.sh`**

1 Pwn request

2 Cache poisoning

Attacker opens a fork PR (payload added). That build's actions/cache save writes the pull_request_target builds the untrusted payload under the shared key. Poisoned code on the base repo. cache persists in base scope.

3 Publishing Workflow

Push to main → different workflow with OIDC permissions restores the poisoned cache and publish a malicious package

###### Full simulation script is here:

https://github.com/supplychain-labs/github-threat-detector/blob/main/simulations/sim-tanstack.sh

67

## Slide 43

###### Recent Github Hardening & Mitigations

**Safer pull_request_target defaults** `actions/checkout` now refuses to fetch fork PR code in privileged workflows unless you explicitly opt out. **(June 2026)** (opt-out) **Read-only cache for untrusted triggers** Workflow runs started by non-collaborators get a cache token with read-only permission, limiting the poisoning path. **(June 2026)** (opt-out)

###### **Example: TanStack npm supply-chain (May 2026)** **`/simulations/sim-tanstack.sh`**

1 Pwn request

2 Cache poisoning

**3 Publishing Workflow**

Attacker opens a fork PR (payload added). That build's actions/cache save writes the Push to main → different workflow with pull_request_target builds the untrusted payload under the shared key. Poisoned OIDC permissions restores the poisoned code on the base repo. cache persists in base scope. cache and publish a malicious package

###### Full simulation script is here:

https://github.com/supplychain-labs/github-threat-detector/blob/main/simulations/sim-tanstack.sh

68

## Slide 44

###### Recent Github Hardening & Mitigations

**Safer pull_request_target defaults** `actions/checkout` now refuses to fetch fork PR code in privileged workflows unless you explicitly opt out. **(June 2026)** (opt-out) **Read-only cache for untrusted triggers** Workflow runs started by non-collaborators get a cache token with read-only permission, limiting the poisoning path. **(June 2026)** (opt-out)

**Example: TanStack npm supply-chain (May 2026)** **`/simulations/sim-tanstack.sh`**

1 Pwn request

2 Cache poisoning

Attacker opens a fork PR (payload added). That build's actions/cache save writes the pull_request_target builds the untrusted payload under the shared key. Poisoned code on the base repo. cache persists in base scope.

3 Publishing Workflow

Push to main → different workflow with OIDC permissions restores the poisoned cache and publish a malicious package

Full simulation script is here:

https://github.com/supplychain-labs/github-threat-detector/blob/main/simulations/sim-tanstack.sh

69

## Slide 45

###### Take Aways

- **GitHub repos should be treated as part of the organization’s security perimeter.**

- **Attacks against GitHub repos often share the same TTPs.**

- **Hardening is the first line of defense: built-in features can dramatically reduce the attack surface.**

- **Comprehensive monitoring requires multiple telemetries**

- **Correlating low-fidelity signals can reveal high-confidence activity.**

71

## Slide 46

## **THANK YOU!**

_morwn yossi-weizman_

github.com/supplychain-labs/github-threat-detector

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
BRIEFINGS
black hat
THANK YOU!
IN yossi-weizman in mown
github.com/supplychain-labs/github-threat-detector
black hat
USA
2026
```
