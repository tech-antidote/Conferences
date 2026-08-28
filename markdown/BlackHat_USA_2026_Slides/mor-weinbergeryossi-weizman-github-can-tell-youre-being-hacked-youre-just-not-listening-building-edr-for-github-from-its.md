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
text_chars: 21783
ocr_pages: 8
has_ocr: true
redacted_secrets: 0
ocr_confidence: 89.7
ocr_unreliable_blocks: 1
vision_verified_pages_changed: 43
vision_verified_pages: 46
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T05:39:11Z"
---
# GitHub Can Tell You're Being Hacked. You're Just Not Listening Building EDR for GitHub from Its Own Event Stream

**Speakers:** Mor Weinberger, Yossi Weizman  
**Conference:** Black Hat USA 2026  
**Source:** `BlackHat_USA_2026_Slides/Mor Weinberger&Yossi Weizman_GitHub Can Tell You're Being Hacked. You're Just Not Listening Building EDR for GitHub from Its Own Event Stream.pdf` (46 pages)


## Slide 1

GitHub Can Tell You're Being Hacked. You're Just Not Listening : Building EDR for GitHub from Its Own Event Stream

## Slide 2

# whoami

**Mor Weinberger**
**Software Architect**
echo

**Yossi Weizman**
**Principal Security Researcher**
Microsoft

## Slide 3

###### Why Now

Cumulative malicious-package advisories

npm (41.7K)

PyPI (11.6K)

_Based on OSV data_

## Slide 4

###### Why Now

**Recent notable incidents**

**Nov 24, 2025 Shai-Hulud 2.0**
Self-replicating npm worm

**Mar 23, 2026 Checkmarx KICS**
GitHub Actions hijacked using stolen CI credentials

**Mar 27, 2026 Telnyx**
Trojanized PyPI release of the official Python SDK

**Apr 22, 2026 Bitwarden CLI**
Malicious npm package pushed via a compromised GitHub Actions workflow

**Apr 30, 2026 PyTorch Lightning**
Backdoored release pushed via a compromised maintainer account

**May 18, 2026 Megalodon**
5k+ GitHub repos backdoored via automated forged-bot commits

**Jul 2026 PolinRider (DPRK)**
100+ malicious packages across npm, Packagist, Go, Chrome

**Mar 19, 2026 Trivy (Aqua)**
CI/CD compromise via GitHub Actions; CVE-2026-33634

**Mar 24, 2026 LiteLLM**
Trojanized release exfiltrating LLM provider API keys

**Mar 31, 2026 Axios (npm)**
70M+ weekly downloads; cross-platform RAT

**Apr 29, 2026 SAP npm packages**
Mini Shai-Hulud worm poisons SAP-related packages for credential harvesting

**May 11, 2026 TanStack**
Abusing GitHub Actions cache to push 84 malicious versions of npm packages

**Jun 1, 2026 Red Hat @redhat-cloud-services**
32 npm packages poisoned via OIDC Trusted Publishing;

**Jul 14, 2026 AsyncAPI**
CI token theft via GitHub Actions

## Slide 5

###### What’s in Our Scope?

Supplier

Consumer

## Slide 6

###### What’s in Our Scope?

Supplier Supplier Consumer

## Slide 7

###### What’s in Our Scope?

###### **In this session, we will focus on GH-related attacks**

## Slide 8

###### Many attacks – same techniques

**Artifact poisoning**
- Mass tag push
- Temporary tag swap
- Malicious release

**OIDC abuse**
- Registry trusted-publish abuse
- Cloud OIDC federation abuse

**Workflow injection & Trigger abuse**
- pull_request_target abuse
- Direct workflow override
- Secrets exfiltration in workflow logs
- Cache poisoning
- Runner’s memory dump

**Identity & commit-metadata forgery**
- Forged maintainer’s identity
- Forged app’s identity
- Forged timestamp and parent commits
- Forged commits tree

**Evidence destruction**
- Delete workflow runs
- Delete forks & branches
- Remove user
- Disable webhooks
- Code & artifact revert
- Base repo commit URL

**Malicious code injected via fork\off-repo**
- Malicious code stored in fork
- Malicious code stored in a dangling commit
- Malicious code in a temporary branch

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

GIT metadata can be set to any value

```
author     name | email | date
committer  name | email | date

message · tree · parent(s)
```

**The pusher is the authenticated user with GH. This is the field you can trust.**

GitHub resolves the author.email field to its legitimate GitHub (clickable + avatar)

```
$ git config user.name  "web-flow"
$ git config user.email "…@users.noreply.github.com"
$ git commit -m "Add test.txt"
```

**Detection: compare the author's name to the authenticated user**

author = `head_commit.author.username` ← from the commit (forgeable)
pusher = `sender.login` ← authenticated by GitHub (trusted)
flag when **`author ≠ pusher`**

## Slide 11

##### TTPs - examples Cross-org forged-author correlation

Attacks are often automated. Attackers use same forged identities against multiple victims.

Forged identities in the repo which appear in other repos as well – **is a strong indication of compromise.**
**Seen also in: Shai-Hulud, Megalodon**

The reused email is indexed by GitHub - pivot from one repo to the whole campaign:

```
GET /search/commits
    ?q=author-email:x@fake.dev
```

**Detection: Find large-scale forged identities using GH Search API**

For each commit where author ≠ pusher:
GET /search/commits?q=author-email → collect owners
alert if same email spans ≥ x unrelated owners (orgs\users)

## Slide 12

##### TTPs - examples Mass tags push

**Goal:** move many release tags onto one poisoned commit, so every workflow that pins the action by tag `(uses: org/action@vN)` runs the malicious code.

```
$ git tag -f v1 v2 v3 … v46  <poisoned>
$ git push --force origin --tags
```

Tags are movable (mutable) pointers

**Reliable detection must track tag changes via tags API:**

`GET /repos/{owner}/{repo}/git/refs/tags`
→ store SHA per tag
**`old_sha ≠ new_sha`** ⇒ tag moved.

**<u>Many tag changes = potentially mass tag poisoning</u>**

###### **Tag pushes aren’t visible in GitHub Activity:**

No tag events

**They are logged in webhooks, but….**

Events will not be created if more than 5000 branches are pushed at once. Events will not be created for tags when more than three tags are pushed at once.

_https://docs.github.com/en/webhooks/webhook-events-and-payloads#push_

## Slide 13

##### TTPs - examples OIDC abuse

**Old way:** workflow publishes with a stored token (`NPM_TOKEN` in GitHub Secrets)
**OIDC:** workflow with `id-token: write` mints its own short-lived token to authenticate with the cloud / registry.

**→ The workflow IS the identity.**

**The attacker's goal shifts:**
**Steal a secret  →  Get an OIDC-granting workflow to run**

Modify a workflow that grants OIDC, and get it to run:

```
on: push
permissions:
  id-token: write
```

**Detection: track new or modified workflows that mint OIDC tokens**
**Examples:**
**- Direct push to publishing workflow**
**- Token read from risky workflow (e.g. pull_request_request)**

## Slide 14

###### Same trust. Different object

**Package registry**

IMMUTABLE

**Git tags**

v1.2.3 → NEW COMMIT

MOVABLE

**Release assets**

app-v1.2.3.zip (current) ⇄ app-v1.2.3.zip (previous)

SWAPPABLE

**Same version string. Three different trust models.**

## Slide 15

###### Implant into an existing release

**v1.2.3 Release**
app-v1.2.3.zip
12.4 MB

→

**v1.2.3 Release**
app-v1.2.3.zip
12.4 MB

WRITE ACCESS

**INJECTION POINT**
PR · ISSUE · CONTRIBUTOR KEY

**GITHUB ACTIONS**
RUNNER + GITHUB_TOKEN

**STOLEN CREDS**
PAT · ACCOUNT KEY

**DELETE ORIGINAL**
RELEASE ZIP

**UPLOAD MALICIOUS ZIP**
ONTO SAME RELEASE

**COVER TRACKS**

## Slide 16

###### **Tampered Release Artifacts**

###### **What the UI answers**

Who signed the commit at the first place
Key known to GitHub

###### **What it does not**

Release maturity
Whether assets were swapped

**Verified ≠ trustworthy binary**

## Slide 17

###### Same trust chrome. Different maturity.

**Checksums prove integrity of whatever was uploaded - including malware.**

## Slide 18

###### Report to Github Bug bountry

Although this warning does not explicitly mention releases, it does state that the GITHUB_TOKEN is granted write permissions on the repository, which is all that is required to create, edit, and delete releases.

Based on the feedback you've provided here, I've added the suggestion to add timestamps to release assets to our internal feature request list, and the team is actively working to make these improvements to the GitHub interface:

> I think you should emphasize the creation time and modify the time of the assets on the release page

We greatly appreciate the thoroughness of this report and the improvement suggestions made throughout, so we'd like to offer you a small reward as thanks.

## Slide 19

###### Report → Signal → Detection

**DISCLOSE**

Bug bounty report

**PLATFORM**

Assets 4

| Name | Size | Created (NEW) |
|---|---|---|
| agent-linux-amd64 | 12.4 MB | May 12, 2025 08:14:22 UTC |
| agent-linux-arm64 | 11.8 MB | May 12, 2025 08:45:37 UTC |
| checksums.txt | 1.2 KB | May 12, 2025 08:46:01 UTC |
| release-notes.md | 3.6 KB | May 12, 2025 08:46:15 UTC |

**DETECT**

`release-asset-time-skew`

08:14:22 UTC — 08:45:37 UTC
Δ 31m 15s

**Intended behavior. New metadata. Detectable swap.**

## Slide 20

###### Tampered Release Artifacts

## Slide 21

### The Engine

github.com/supplychain-labs/github-threat-detector

## Slide 22

###### The Engine

**LISTEN**
ingest platform activity

**Webhooks**
live push stream

**GitHub APIs**
events · commits · tags
actions · activities

**Git inspect**
bare clone / objects

## Slide 23

###### The Engine

**LISTEN**
ingest platform activity

**Webhooks**
live push stream

**GitHub APIs**
events · commits · tags
actions · activities

**Git inspect**
bare clone / objects

**REMEMBER**
one activity memory

**PostgreSQL**

**Unified View**

**Context tables**
tags history · commits
workflows · git_repo_checks

## Slide 24

###### The Engine

**LISTEN**
ingest platform activity

**Webhooks**
live push stream

**GitHub APIs**
events · commits · tags
actions · activities

**Git inspect**
bare clone / objects

**REMEMBER**
one activity memory

**PostgreSQL**

**Unified View**

**Context tables**
tags history · commits
workflows · git_repo_checks

**DETECT**
behavioral scoring

**SQL rule runner**

**30+ detection rules**
attack-class families

**Baselines**
who pushes · tag norms

## Slide 25

###### The Engine

**LISTEN**
ingest platform activity

**Webhooks**
live push stream

**GitHub APIs**
events · commits · tags
actions · activities

**Git inspect**
bare clone / objects

**REMEMBER**
one activity memory

**PostgreSQL**

**Unified View**

**Context tables**
tags history · commits
workflows · git_repo_checks

**DETECT**
behavioral scoring

**SQL rule runner**

**30+ detection rules**
attack-class families

**Baselines**
who pushes · tag norms

**ACT**
investigate & respond

**Findings**

**Timeline / IR**
when · who · what else

**UI / CLI**

## Slide 26

###### Architecture

Collect -> Enrich -> Detect -> Act

**INGEST**

**Snapshot Collectors**

**Webhook receiver**

**CLI collect / analyze**

**PostgreSQL**
events · context
findings
system of record

**DETECT**

**SQL detection queries**
30+ behavioral rules

**INVESTIGATE**

**Frontend**
timeline · kill chain
Compound

**CLI report**

## Slide 27

###### Architecture

Collect -> Enrich -> Detect -> Act

**INGEST**

**Snapshot Collectors**

**Webhook receiver**

**CLI collect / analyze**

**ENRICH**

**Author Enrichment**

**PostgreSQL**
events · context
findings
system of record

**DETECT**

**SQL detection queries**
30+ behavioral rules

**INVESTIGATE**

**Frontend**
timeline · kill chain
Compound

**CLI report**

## Slide 28

###### **GitHub Telemetry**

**Webhooks**
live push stream

- Real-time
- Rich telemetry
- Harder setup
- Can be disabled
- Missed events are gone

## Slide 29

###### **GitHub Telemetry**

**Webhooks**
live push stream

- Real-time
- Rich telemetry
- Harder setup
- Can be disabled
- Missed events are gone

**GitHub API**
snapshot baseline

- Snapshot & compare over time
- Can't be removed as a channel
- API object can be removed
- Less verbose than webhooks
- Rate limited

## Slide 30

###### **GitHub Telemetry**

**Webhooks**
live push stream

- Real-time
- Rich telemetry
- Harder setup
- Can be disabled
- Missed events are gone

**GitHub API**
snapshot baseline

- Snapshot & compare over time
- Can't be removed as a channel
- API object can be removed
- Less verbose than webhooks
- Rate limited

**Git Inspect**
tag provenance

- Read objects, not just events
- Great for Enrichment
- Harder to stand up
- Not real-time
- Heavier than API / webhooks

## Slide 31

###### Detections

|**TTP family**|**Example of detections**|
|---|---|
|Artifact poisoning|Mass tag force-push burst · Flip-flop tag · Many tags → same commit · Many tags → same parent|
|Identity & commit-metadata forgery|Author ≠ pusher · Committer ≠ pusher · Cross-owner forged author · Unresolvable author email · Tag parent in the future · Unverified commits|
|Malicious code via fork / off-repo|Tag from non-existing branch (dangling commit)|
|Workflow injection & trigger abuse|pull_request_target pwn-request · Direct workflow push to default · Secret base64 exfil in logs|
|Evidence destruction|Workflow-run deleted|
|OIDC abuse|OIDC risky workflow run · Direct OIDC workflow push to default branch|

**Overall**: 22 rules + 12 beta rules

https://github.com/supplychain-labs/github-threat-detector/tree/main/analyzers/detection_queries

## Slide 32

###### Detections

**severity**
**MITRE ATT&CK tactic**
**Detection Logic**

```
-- id: oidc-risky-workflow-run
-- severity: high
-- description: OIDC-minting workflow '{workflow_path}' ran on untrusted trigger '{trigger}' (head_repo {head_repo}) in {repo_name}
-- tactic: Credential Access
-- actor: actor_login
-- event_id: {run_id}:{workflow_path}
-- evidence: workflow_path, trigger, head_branch, head_repo, run_started_at
-- repo_column: repo_name
--
-- Logic (workflow_runs x workflow_files):
--   A workflow run whose file (in workflow_files) requests id-token: write,
--   where the run fired on an untrusted, privileged-context trigger
--   (pull_request_target, workflow_run, issue_comment, PR review events) OR
--   the run's code came from a fork (head_repository differs from
--   repository). Such a run can mint an OIDC token from attacker-influenced
--   input executing in the base repo's context.
--
SELECT
    r.repo_name,
    r.id                              AS run_id,
    r.workflow_path,
    r.event                           AS trigger,
    r.head_branch,
    r.payload->'head_repository'->>'full_name'    AS head_repo,
    r.actor_login,
    r.run_started_at
FROM workflow_runs r
JOIN workflow_files f
  ON f.repo_name = r.repo_name
 AND f.path       = r.workflow_path
WHERE f.content ILIKE '%%id-token: write%%'
  AND (
        r.event IN ('pull_request_target', 'workflow_run',
                    'issue_comment', 'pull_request_review', 'pull_request_review_comment')
    OR (r.payload->'head_repository'->>'full_name')
       IS DISTINCT FROM (r.payload->'repository'->>'full_name')
    )
```

## Slide 33

###### Compound Rules

**DETECTION A**
Push of many tags to the same commit
LOW

+

**DETECTION B**
Tag points to off-branch commit
MEDIUM

→

**COMPOUND RULE**
Mass tag poisoning to an unreachable commit
HIGH

## Slide 34

#### How did we evaluate it?

## Slide 35

###### <u>Simulations</u>

| | | |
|---|---|---|
|**CVE-2026-33634**<br>`(trivy-actions incident)`|• Author spoofed<br>• Re-parent release commits onto today's HEAD<br>• Mass tag force-push<br>• Many tags → same tree / same parent<br>• Impossible lineage (parent newer than child)<br>• Unsigned / unverified commits on tags|Aqua Security blog<br>Microsoft Security Blog<br>Wiz blog|
|**CVE-2025-30066**<br>`(tj-actions/changed-files incident)`|• Malicious commit in a fork<br>• Force-repoint all tags onto that single commit<br>• Commit identity spoofed as a bot<br>• Unsigned commit where baseline was signed<br>• Tag target on no branch (off-branch / from a fork)|GH issue<br>Step Security blog<br>Wiz blog|
|**CVE-2025-30154**<br>`(reviewdog incident)`|• Tag v1 force-repointed to a malicious commit<br>• Malicious commit off every branch (tag ref only)<br>• Flip-flop cover-up: v1 reverted back to clean|GH issue<br>Wiz blog|
|**CVE-2026-45321**<br>`(tanstack incident)`|• pull_request_target “Pwn Request”: untrusted PR ref built<br>• Cache poisoning across fork↔base boundary<br>• Shared cache key between PR-target and publish<br>• Anti-forensics: PR closed + fork branch deleted<br>• OIDC theft on the trusted runner|TanStack blog<br>Step Security blog|
|**CVE-2026-42994**<br>`(Bitwarden-CLI incident)`|• Existing publish workflow modified on a side branch<br>• Branch guard removed; trigger change to on: push: tags<br>• id-token: write: registry token exchange<br>• Stolen token echoed to run log (base64)<br>• Unsigned commit on the publish workflow<br>• Workflow run fires from a non-default ref (the tag)<br>• Run + logs deleted afterward (anti-forensics)|GH issue<br>Bitwarden community forum<br>Step Security blog|
|**Megalodon campaign**|• Direct push to default branch, no PR (d-PPE)<br>• Adds a backdoor under .github/workflows/<br>• Forged author with unresolvable email (author ≠ pusher)<br>• Same forged author across many repos/owners in a short window<br>• Workflow grants id-token: write|SafeDep blog|

https://github.com/supplychain-labs/github-threat-detector/tree/main/simulations

## Slide 36

###### Noise lab: validating detections

**CANDIDATE**
Incidents
Simulations

**FIELDS IN GH ARCHIVE?**

**ENRICH**
GitHub API
git inspect

**MEASURE**
Prevalence
Incident recall

**DECIDE**
Keep / demote
Allowlist
Correlator

https://www.gharchive.org/

## Slide 37

###### Noise lab: validating detections

**CANDIDATE**
Incidents
Simulations

**FIELDS IN GH ARCHIVE?**

**ENRICH**
GitHub API
git inspect

**MEASURE**
Prevalence
Incident recall

**DECIDE**
Keep / demote
Allowlist
Correlator

v4 · v4.14.9 · v4.14 → same commit

https://www.gharchive.org/

## Slide 38

## Demo

## Slide 39

```
sim-runner:/tmp# ./demo-trivy.sh
```

## Slide 40

A full-page screenshot; the slide carries no text of its own.

## Slide 41

###### Recent Github Hardening & Mitigations

###### **Notable recent changes:**

**Immutable releases (October 2025)**
GitHub permanently locks Release’s tag and assets so they can't be moved, edited, or deleted

**Workflow execution protections (preview) (June 2026)**
Central allowlist of who and which events may trigger workflows, evaluated before the run.

**Safer pull_request_target defaults (June 2026)**
`actions/checkout` now refuses to fetch fork PR code in privileged workflows unless you explicitly opt out. (default)

**Read-only cache for untrusted triggers (June 2026)**
Workflow runs started by non-collaborators get a cache token with read-only permission, limiting the poisoning path. (default)

## Slide 42

###### Recent Github Hardening & Mitigations

**Safer pull_request_target defaults (June 2026)**
`actions/checkout` now refuses to fetch fork PR code in privileged workflows unless you explicitly opt out. (opt-out)

**Read-only cache for untrusted triggers (June 2026)**
Workflow runs started by non-collaborators get a cache token with read-only permission, limiting the poisoning path. (opt-out)

###### **Example: TanStack npm supply-chain (May 2026)**
**`/simulations/sim-tanstack.sh`**

**1 Pwn request**
Attacker opens a fork PR (payload added). pull_request_target builds the untrusted code on the base repo.

**2 Cache poisoning**
That build's actions/cache save writes the payload under the shared key. Poisoned cache persists in base scope.

**3 Publishing Workflow**
Push to main → different workflow with OIDC permissions restores the poisoned cache and publish a malicious package

###### Full simulation script is here:

https://github.com/supplychain-labs/github-threat-detector/blob/main/simulations/sim-tanstack.sh

## Slide 43

###### Recent Github Hardening & Mitigations

**Safer pull_request_target defaults (June 2026)**
`actions/checkout` now refuses to fetch fork PR code in privileged workflows unless you explicitly opt out. (opt-out)

**Read-only cache for untrusted triggers (June 2026)**
Workflow runs started by non-collaborators get a cache token with read-only permission, limiting the poisoning path. (opt-out)

###### **Example: TanStack npm supply-chain (May 2026)**
**`/simulations/sim-tanstack.sh`**

**1 Pwn request**
Attacker opens a fork PR (payload added). pull_request_target builds the untrusted code on the base repo.

**2 Cache poisoning**
That build's actions/cache save writes the payload under the shared key. Poisoned cache persists in base scope.

**3 Publishing Workflow**
Push to main → different workflow with OIDC permissions restores the poisoned cache and publish a malicious package

###### Full simulation script is here:

https://github.com/supplychain-labs/github-threat-detector/blob/main/simulations/sim-tanstack.sh

pr-checks.yml
on: pull_request_target
Status: Failure

build
Refusing to check out fork pull request code from a 'pull_request_target' workflow. This workflow runs with the base repository's GITHUB_TOKEN, secrets, default-branch cache scope, and runner access. Fetching and executing a fork's code in that trusted context commonly leads to "pwn request" vulnerabilities. To opt in, review the risks at https://gh.io/securely-using-pull_request_target and set 'allow-unsafe-pr-checkout: true' on the actions/checkout step.

## Slide 44

###### Recent Github Hardening & Mitigations

**Safer pull_request_target defaults (June 2026)**
`actions/checkout` now refuses to fetch fork PR code in privileged workflows unless you explicitly opt out. (opt-out)

**Read-only cache for untrusted triggers (June 2026)**
Workflow runs started by non-collaborators get a cache token with read-only permission, limiting the poisoning path. (opt-out)

###### **Example: TanStack npm supply-chain (May 2026)**
**`/simulations/sim-tanstack.sh`**

**1 Pwn request**
Attacker opens a fork PR (payload added). pull_request_target builds the untrusted code on the base repo.

**2 Cache poisoning**
That build's actions/cache save writes the payload under the shared key. Poisoned cache persists in base scope.

**3 Publishing Workflow**
Push to main → different workflow with OIDC permissions restores the poisoned cache and publish a malicious package

###### Full simulation script is here:

https://github.com/supplychain-labs/github-threat-detector/blob/main/simulations/sim-tanstack.sh

pr-checks.yml
on: pull_request_target
Status: Success

build
Cache reservation failed: cache write denied: token has no writable scopes

## Slide 45

###### Take Aways

- **GitHub repos should be treated as part of the organization’s security perimeter.**

- **Attacks against GitHub repos often share the same TTPs.**

- **Hardening is the first line of defense: built-in features can dramatically reduce the attack surface.**

- **Comprehensive monitoring requires multiple telemetries**

- **Correlating low-fidelity signals can reveal high-confidence activity.**

## Slide 46

## **THANK YOU!**

_yossi-weizman_   _morwn_

github.com/supplychain-labs/github-threat-detector

