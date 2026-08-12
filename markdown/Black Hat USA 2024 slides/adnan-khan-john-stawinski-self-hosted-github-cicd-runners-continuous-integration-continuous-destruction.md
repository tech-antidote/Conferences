---
title: "Self-Hosted GitHub CICD Runners Continuous Integration, Continuous Destruction"
speakers: ["Adnan Khan", "John Stawinski"]
conference: "Black Hat"
conference_full: "Black Hat USA 2024"
edition: "USA"
year: 2024
source_pdf: "Black Hat USA 2024 slides/Adnan Khan & John Stawinski_Self-Hosted GitHub CICD Runners Continuous Integration, Continuous Destruction.pdf"
pages: 98
sha256: "8c1381fcd289280634e96d806b3746f67d2d15854fc8e7d105e55395f7bc6dfb"
text_chars: 33550
ocr_pages: 16
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:28:50Z"
---
# Self-Hosted GitHub CICD Runners Continuous Integration, Continuous Destruction

**Speakers:** Adnan Khan, John Stawinski  
**Conference:** Black Hat USA 2024  
**Source:** `Black Hat USA 2024 slides/Adnan Khan & John Stawinski_Self-Hosted GitHub CICD Runners Continuous Integration, Continuous Destruction.pdf` (98 pages)


## Slide 1

Self Hosted GitHub Runners

Continuous Integration, Continuous Destruction

Adnan Khan | John Stawinski

#BHUSA @BlackHatEvents

## Slide 2

### First…A Story

Two months ago, someone identified a GitHub Actions misconfiguration in a public repository owned by one of the largest domestic chip manufacturers in the United States - anyone with a GitHub account could have exploited it by creating a pull request. The vulnerability allowed them to obtain Enterprise admin privileges over that company’s GitHub Enterprise Cloud tenant. This provided access to some of that companies most sensitive intellectual property. They had the privileges to make every repository public or even delete their GitHub organizations, which would trigger an immediate loss of over 120,000 repositories. Thankfully, this was not an APT, it was me, and I responsibly disclosed the vulnerability.

-Adnan Khan

## Slide 3

### Disclaimer

- All vulnerabilities mentioned during this talk have been remediated

- The views and opinions expressed in this presentation are solely our own

- The content presented is not endorsed by, nor does it represent the views of our employers

- All materials and ideas shared are independently developed and should not be attributed to our employers

## Slide 4

###### Adnan Khan

- ➔ Security Engineer for Day Job

- ➔ Security Researcher

- ➔ Bug Bounty Hunter

- ➔ Live in Baltimore, Maryland

X: @adnanthekhan Website: adnanthekhan.com

###### John Stawinski

- ➔ Red Team Security Engineer

- ➔ CI/CD Security Researcher

- ➔ Enjoys anything outside, especially activities that lead to injury

- ➔ Former Collegiate  Athlete

➔ Nomadic (for now)

Email: jstan327@gmail.com LinkedIn: www.linkedin.com/in/john-stawinski-72ba87191 Website: johnstawinski.com

Adnan Khan – X: @adnanthekhan Website: adnanthekhan.com

John Stawinski - Email: jstan327@gmail.com Website: johnstawinski.com

#BHUSA @BlackHatEvents

## Slide 5

Insert Adnan pic here

And many more….

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
€) Actions TensorFlow =e Microsoft
an
OPyTorch ©"
AND MANY MORE....
```

## Slide 6

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ame Fortinet
“= = https://www.fortinet.com > resources > cyberglossary
SolarWinds Supply Chain Attack
One of the most notable impacts was the financial fallout from the attack. On average, the
attack cost companies 11% of their annual revenue. The impact was ... Gi t H
| ¢ TECHNICA BIZ& IT TECH SCIENCE POLICY CARS GAMING & CULTURE
DevOps Lifecyle
GitHub besieged by millions of malicious
repositories in ongoing attack
GitHub keeps removing malware-laced repositories, but thousands remain.
- a
on their software supply chains (a three-fold increase from 2021). There’s already evidence this is
happening, with supply chain attacks up 633% and surpassing the number of malware-based attacks
by 40% in 2022.
```

## Slide 7

Ok, but is it really that bad?

## Slide 8

Yes.

## Slide 9

There is a systemic lack of awareness around self-hosted CI/CD agent security in the world’s most advanced technological organizations, exposing them to critical supply chain attacks.

## Slide 10

The tech community is uninformed of these attacks

These attacks are easy

These attacks could shape the course of the world

## Slide 11

### The Progression

August 2022

2022/2023

July 2023

July 2023 - February 2024

Abused a Self-Hosted GitHub Runner on a Red Team Engagement

Developed GitHub Actions Attack Tooling

Lightbulb Moment - Decided to Put Fixing a Typo to the Test Against GitHub Itself

Disclosed GitHub Actions Vulnerabilities in Public Repositories with Bug Bounty Programs Using Self-Hosted Runners

Adnan Khan – X: @adnanthekhan Website: adnanthekhan.com

John Stawinski - Email: jstan327@gmail.com Website: johnstawinski.com

#BHUSA @BlackHatEvents

## Slide 12

###### Github-Hosted Runners

- ➔ Built by GitHub

- ➔ Updated on a weekly cadence

- ➔ As of writing, covers:

   - Linux, Windows, MacOS

   - Multiple architectures

###### Self-Hosted Runners

   - ➔ Managed by end users

   - ➔ Runs the Actions Runner agent

   - ➔ Security is the user’s responsibility ➔ “Path of Least Resistance” is a nonephemeral self-hosted runner.

- ➔ Always Ephemeral

Adnan Khan – X: @adnanthekhan Website: adnanthekhan.com

John Stawinski - Email: jstan327@gmail.com Website: johnstawinski.com

#BHUSA @BlackHatEvents

## Slide 13

Workflow Run Log Analysis

## Slide 14

Public Repository Self-Hosted Runners Scanned ~July 4-8 2024

350
300
250
200
150
100
50
0
0-50 50-250 250-1000 1000-5000
Repository Stars
Repositories with Self-Hosted Runners

###### Non-Ephemeral Ephemeral

Adnan Khan – X: @adnanthekhan Website: adnanthekhan.com

John Stawinski - Email: jstan327@gmail.com Website: johnstawinski.com

#BHUSA @BlackHatEvents

## Slide 15

###### Workflow Run Log Analysis

Every GitHub Actions workflow has a run log. Attackers can:

Learn about the self-hosted runner’s configurations Plan a full attack before any malicious actions

On public repositories, anyone can download the run logs

Adnan Khan – X: @adnanthekhan Website: adnanthekhan.com

John Stawinski - Email: jstan327@gmail.com Website: johnstawinski.com

#BHUSA @BlackHatEvents

## Slide 16

Adnan Khan – X: @adnanthekhan Website: adnanthekhan.com John Stawinski - Email: jstan327@gmail.com Website: johnstawinski.com #BHUSA @BlackHatEvents

## Slide 17

###### Requested Runner Labels

Organization Level vs. Repository Level Runners

Runner Name / Group

Adnan Khan – X: @adnanthekhan Website: adnanthekhan.com

John Stawinski - Email: jstan327@gmail.com Website: johnstawinski.com

#BHUSA @BlackHatEvents

## Slide 18

###### GITHUB_TOKEN Permissions

Ephemeral vs. non-Ephemeral Runner

Runner Architecture

Adnan Khan – X: @adnanthekhan Website: adnanthekhan.com

John Stawinski - Email: jstan327@gmail.com Website: johnstawinski.com

#BHUSA @BlackHatEvents

## Slide 19

Teach Me How to Hack Everyone.

## Slide 20

###### People Tend to Use Default Settings

Becoming a Contributor is Not a Security Boundary

Anyone Can Fix a Typo

## Slide 21

###### What is the “Vulnerability”?

Default workflow approval

Over-permissive GITHUB_TOKEN or Actions Secrets

Non-ephemeral public repo selfhosted runner

By themselves, these are gaps in “best practices”

Together, they could ruin your day

## Slide 22

###### The Three Step Process

Pipeline
1. Become a contributor
Privilege
Escalation
2. Persist on the runner
3. Capture secrets and  Become  Wait for  Build
Implant
move laterally Contributor Runners Builds Tampering
Move  Secrets
Laterally Exfiltration

Adnan Khan – X: @adnanthekhan Website: adnanthekhan.com

John Stawinski - Email: jstan327@gmail.com Website: johnstawinski.com

#BHUSA @BlackHatEvents

## Slide 23

#### Case Studies

Perimeter

## Slide 24

###### Case Study 1

The tech community is uninformed of these attacks which can have critical, widespread impact

## Slide 25

###### Hacking GitHub, Through Actions

Case Study 1: GitHub Actions Runner Images **“The one that started it all”**

## Slide 26

###### How do I become a Contributor?

The typo

Adnan Khan – X: @adnanthekhan Website: adnanthekhan.com

John Stawinski - Email: jstan327@gmail.com Website: johnstawinski.com

#BHUSA @BlackHatEvents

## Slide 27

- Account Created: 07-17-2023

- Pull Request Submitted: 07-18-2023

- Pull Request Merged: 07-20-2023

Adnan Khan – X: @adnanthekhan Website: adnanthekhan.com

John Stawinski - Email: jstan327@gmail.com Website: johnstawinski.com

#BHUSA @BlackHatEvents

## Slide 28

- Account Created: 07-17-2023
- Pull Request Submitted: 07-18-2023
- Pull Request Merged: 07-20-2023

Adnan Khan – X: @adnanthekhan Website: adnanthekhan.com John Stawinski - Email: jstan327@gmail.com Website: johnstawinski.com

#BHUSA @BlackHatEvents

## Slide 29

###### Planning the Attack

Scheduled Nightly Workflows on SelfHosted Runners GITHUB_TOKEN with full write access

Multiple Non-Ephemeral Self Hosted Runners

Nightly Builds Interacted with vCenter, Azure and had secrets to both

Images saved off

## Slide 30

###### The mission - Failure was not an option

One Shot

Capture
GITHUB_TOKEN
Runner Persistence
Scheduled
Workflow
Implantation Cleanup
Time
High Detection Risk
Window Timing Was Critical
GO TIME: Friday, July 21st, 2023

Adnan Khan – X: @adnanthekhan Website: adnanthekhan.com

John Stawinski - Email: jstan327@gmail.com Website: johnstawinski.com

#BHUSA @BlackHatEvents

## Slide 31

###### The payload - Modified “Linter.yml” in Fork

For pull_request trigger, the merge commit is the source of truth!

Adnan Khan – X: @adnanthekhan Website: adnanthekhan.com

John Stawinski - Email: jstan327@gmail.com Website: johnstawinski.com

#BHUSA @BlackHatEvents

## Slide 32

###### The payload - Modified “Linter.yml” in Fork

Run payload on 3 runners in azure-builds group, 3 in macos-vmware group – 6 total

Adnan Khan – X: @adnanthekhan Website: adnanthekhan.com

John Stawinski - Email: jstan327@gmail.com Website: johnstawinski.com

#BHUSA @BlackHatEvents

## Slide 33

###### The payload - Modified “Linter.yml” in Fork

The modified workflow referenced a “linter” script that pulled down a second stage payload from a gist and ran it.

Adnan Khan – X: @adnanthekhan Website: adnanthekhan.com

John Stawinski - Email: jstan327@gmail.com Website: johnstawinski.com

#BHUSA @BlackHatEvents

## Slide 34

###### The payload - Runner on Runner

Adnan Khan – X: @adnanthekhan Website: adnanthekhan.com

John Stawinski - Email: jstan327@gmail.com Website: johnstawinski.com

#BHUSA @BlackHatEvents

## Slide 35

###### The payload - Runner on Runner

First, decoded a PAT hard-coded in the payload and used it to retrieve a self-hosted runner registration token from GitHub’s API.

Adnan Khan – X: @adnanthekhan Website: adnanthekhan.com

John Stawinski - Email: jstan327@gmail.com Website: johnstawinski.com

#BHUSA @BlackHatEvents

## Slide 36

###### The payload - Runner on Runner

###### Next, downloaded the Actions runner binary from GitHub.

Adnan Khan – X: @adnanthekhan Website: adnanthekhan.com

John Stawinski - Email: jstan327@gmail.com Website: johnstawinski.com

#BHUSA @BlackHatEvents

## Slide 37

###### The payload - Runner on Runner

Finally, configured the self-hosted runner and ran it with RUNNER_TRACKING_ID set to 0. This prevents the parent workflow from reaping orphan processes.

Adnan Khan – X: @adnanthekhan Website: adnanthekhan.com

John Stawinski - Email: jstan327@gmail.com Website: johnstawinski.com

#BHUSA @BlackHatEvents

## Slide 38

# Subsequent Workflow Runs { Implantation Workflow Runs {

Adnan Khan – X: @adnanthekhan Website: adnanthekhan.com

John Stawinski - Email: jstan327@gmail.com Website: johnstawinski.com

#BHUSA @BlackHatEvents

## Slide 39

###### PersistencE on Self-Hosted Runner

Access

Result

GITHUB_TOKEN with actions: write

Delete workflow runs via Github API <u>[T1070]</u>

Un-redacted scripts from future workflows

Access to workflow secrets <u>[T1552]</u>

Internal Network Access

GITHUB_TOKEN with contents: write

Move Laterally to Internal vCenter <u>[T1210]</u> Pipeline Privilege Escalation via Repository Dispatch Event <u>[T1546]</u>

Interact with ongoing builds

Supply Chain Compromise <u>[T1195]</u>

Adnan Khan – X: @adnanthekhan Website: adnanthekhan.com

John Stawinski - Email: jstan327@gmail.com Website: johnstawinski.com

#BHUSA @BlackHatEvents

## Slide 40

Adnan Khan – X: @adnanthekhan Website: adnanthekhan.com John Stawinski - Email: jstan327@gmail.com Website: johnstawinski.com #BHUSA @BlackHatEvents

## Slide 41

##### Webshell

Adnan Khan – X: @adnanthekhan Website: adnanthekhan.com John Stawinski - Email: jstan327@gmail.com Website: johnstawinski.com #BHUSA @BlackHatEvents

## Slide 42

##### Clean Malicious Runs

Adnan Khan – X: @adnanthekhan Website: adnanthekhan.com

John Stawinski - Email: jstan327@gmail.com Website: johnstawinski.com

#BHUSA @BlackHatEvents

## Slide 43

Techniques

###### Webshell and Secrets Exfiltration

Base64 encode and print to workflow log on private C2 repo

Use actions/upload-artifact to exfiltrate larger files Place post-checkout hook in .git/hooks and dump runner’s memory - requires root

## Slide 44

###### Impact - NEtwork Lateral Movement

###### Ability to pivot to private vCenter deployment as administrator

Adnan Khan – X: @adnanthekhan Website: adnanthekhan.com

John Stawinski - Email: jstan327@gmail.com Website: johnstawinski.com

#BHUSA @BlackHatEvents

## Slide 45

###### Impact - Build Tampering

Legitimate
Build Starts

Legitimate Runner Checks out Code

Swap Build Scripts Build Poisoned

Adnan Khan – X: @adnanthekhan Website: adnanthekhan.com

John Stawinski - Email: jstan327@gmail.com Website: johnstawinski.com

#BHUSA @BlackHatEvents

## Slide 46

###### Pipeline Privilege Escalation

Adnan Khan – X: @adnanthekhan Website: adnanthekhan.com

John Stawinski - Email: jstan327@gmail.com Website: johnstawinski.com

#BHUSA @BlackHatEvents

## Slide 47

###### Pipeline Privilege Escalation

Use GITHUB_TOKEN and GitHub API to trigger repository dispatch event with script injection payload

The repository had another workflow with a valuable secret that ran on a GitHub-hosted runner but used the repository dispatch trigger. If we have a GITHUB_TOKEN with contents: write, then we can trigger it.

Adnan Khan – X: @adnanthekhan Website: adnanthekhan.com

John Stawinski - Email: jstan327@gmail.com Website: johnstawinski.com

#BHUSA @BlackHatEvents

## Slide 48

###### Pipeline Privilege Escalation

Use payload to dump runner’s memory and steal the PRAPPROVAL_SECRET, which is a PAT belonging to a GitHub employee.

Workflow used input from dispatch in a run step by context expression… Since we control the payload, this allows script injection.

Adnan Khan – X: @adnanthekhan Website: adnanthekhan.com

John Stawinski - Email: jstan327@gmail.com Website: johnstawinski.com

#BHUSA @BlackHatEvents

## Slide 49

###### Pipeline Privilege Escalation

Use token to approve and merge attacker fork pull requests into main.

It’s possible to dump the runner’s memory and steal the secret – which is a PAT belonging to a GitHub employee.

Adnan Khan – X: @adnanthekhan Website: adnanthekhan.com

John Stawinski - Email: jstan327@gmail.com Website: johnstawinski.com

#BHUSA @BlackHatEvents

## Slide 50

Main

###### Impact - Supply Chain Compromise

Malicious Changes Self-Approve + Merge

Modify code in Rapid release main cadence

Hack Everyone

Adnan Khan – X: @adnanthekhan Website: adnanthekhan.com

John Stawinski - Email: jstan327@gmail.com Website: johnstawinski.com

#BHUSA @BlackHatEvents

## Slide 51

###### Attack Path Summary

Become Implant Contributor Runners

Capture Secrets from Runs

Pivot to
Mac Cloud
vCenter

Capture Employee Token

Modify Source Code

Tamper with Builds

Adnan Khan – X: @adnanthekhan Website: adnanthekhan.com

John Stawinski - Email: jstan327@gmail.com Website: johnstawinski.com

#BHUSA @BlackHatEvents

## Slide 52

###### Case Study 2

These attack are easy.

## Slide 53

Breaching Microsoft’s

###### Case Study

2

Perimeter

Adnan Khan – X: @adnanthekhan Website: adnanthekhan.com

John Stawinski - Email: jstan327@gmail.com Website: johnstawinski.com

#BHUSA @BlackHatEvents

## Slide 54

Social Engineering Web Application Vulnerability

Fix a Typo

Breaching Microsoft’s

Perimeter

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Social Eyisineerin ° ° ;
Pr 9 Breaching §§ Microsoft's
pr va
Perimeter
DeepSpeed
Web A tion Vulnerability
```

## Slide 55

##### A Trend in AI/ML…

Many public GitHub repositories that use selfhosted runners for compute requirements Engineers working on AI projects have high pressure to move very fast Result: Developers take shortcuts at the expense of security

Adnan Khan – X: @adnanthekhan Website: adnanthekhan.com

John Stawinski - Email: jstan327@gmail.com Website: johnstawinski.com

#BHUSA @BlackHatEvents

## Slide 56

- ➔ Open-source deep-learning optimization library

- ➔ 33,000 stars on GitHub

Adnan Khan – X: @adnanthekhan Website: adnanthekhan.com

John Stawinski - Email: jstan327@gmail.com Website: johnstawinski.com

#BHUSA @BlackHatEvents

## Slide 57

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
DeepSpeed / .github / workflows / amd-mi200.yml (9
3) loadams and root Add required paths to trigger AMD tests on PRs (#5406) agp vy
Blame 86 lines (74 loc) - 2.96 KB: @
name: amd-—mi200
on:
workf low_dispatch:
pull_request:
paths:
- ',github/workf lows/amd—mi200.ymL'
- 'requirements/xx'
schedule:
- cron: "@ @ * * x"
concurrency:
group: ${{ github.workflow }}-${{ github.ref }}
cancel-in-progress: true
permissions:
contents: read
issues: write
jobs:
amd-tests:
# The type of runner that the job will run on
runs-on: [self-hosted, amd, mi20Q]
```

## Slide 58

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
DeepSpeed / .github / workflows / amd-mi200.yml (2
© loadams and root Add required paths to trigger AMD tests on PRs (#5406) gp vy
Blame 86 lines (74 loc) + 2.96 KB: @
name: amd-mi200
on:
workf low_dispatch:
pull_request:
paths:
- ',github/workf lows/amd—mi200. yml'
- 'requirements/xx'
runs-on: [self-hosted, amd, mi20Q]
wo On DOU HW DN
schedule:
PR
S
- cron: "0 0 * * x"
PR
NB
concurrency:
group: ${{ github.workflow }}-${{ github.ref }}
cancel-in-progress: true
PPP PR
ou fh Ww
permissions:
contents: read
R
~~
issues: write
NPR
oS ©
jobs:
amd-tests:
N Nat
N BP
# The type of runner that the job will run on
N
Ww
runs-on: [self-hosted, amd, mi20Q]
```

## Slide 59

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
fix typo in SECURITY.md #4019
sd a PR to fix this typo in SECURITY.md
\ Next >
fix typo in SECURITY.md
jstan327 committed
2 ae SECURITY.md (4b
com/create-report).
Instead, please report them to the Microsoft Security Respo
sible, encrypt yo Security Response Center PGP Key
yre@nicrosoft.c ). If possible, encrypt your message with our PGP key; please download it from the [Microsoft Security Response Center PGP Key page
logging in, send email to [secure@microsoft.com] (m
ttps://www. microsoft. com/en-us/msrc/pgp-key-msrc).
your original message. A
```

## Slide 60

###### Creating our Malicious WOrkflow

1. Create Deepspeed Fork

2. Add malicious workflow

3. Submit PR

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
CREATING OUR MALICIOUS WORKFLOW
name: nv—-h100
oH 1]. Create Deepspeed Fork
pull_request
janis 2. Add molicious workflow
unit-tests:
runs-on: [self-hosted, nvidia, h10@] 3. Submit PR
steps:
. = ©) microsoft / DeepSpeed
- uses: actions/checkout@v3
<)fode © Issues 786 $1] Pullrequests 146 Q) Discussions ©) Actions [fF Projects © Security [~ Insights
— name: unit-tests
€ nv-h100
ti —on- et .
continue-on-error: true 7) Workflow testing #76
run: |
() Summary
unit-tests
succeeded 9 minutes ago in 8s
whoami
Jobs
Bud | @ unit-tests > @ Setupjob
is Run details v @ unit-tests
```

## Slide 61

Creating our Malicious WOrkflow

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
CREATING OUR MALICIOUS WORKFLOW
runs-on: [self-hosted, nvidia, h100]
C¢) microsoft / DeepSpeed
<> Code ©) Issues. 786 {1} Pullrequests 146 1) Discussions ©) Actions [F Projects © Security | Insights
€ nv-h100
@ Workflow testing #76
() Summary .
unit-tests
succeeded 9 minutes ago in 8s
Jobs
it-test
| © unit-tests > @ Setup job
Run details v @ unit-tests
```

## Slide 62

###### Hello REDMOND

Adnan Khan – X: @adnanthekhan Website: adnanthekhan.com John Stawinski - Email: jstan327@gmail.com Website: johnstawinski.com #BHUSA @BlackHatEvents

## Slide 63

Opens the door to Active Directory lateral movement and privilege escalation - Red Teaming 101

## Slide 64

###### Case Study 2 - Microsoft Deepspeed

Lateral
Active  Movement
Become  Implant
Directory  with
Contributor Runner
Foothold Developer
Privileges
These attack are easy.

Adnan Khan – X: @adnanthekhan Website: adnanthekhan.com

John Stawinski - Email: jstan327@gmail.com Website: johnstawinski.com

#BHUSA @BlackHatEvents

## Slide 65

##### Gato-x DEMO

###### Available at: https://github.com/adnanekhan/Gato-X

Adnan Khan – X: @adnanthekhan Website: adnanthekhan.com

John Stawinski - Email: jstan327@gmail.com Website: johnstawinski.com

#BHUSA @BlackHatEvents

## Slide 66

None have Seen what you are about to see…

## Slide 67

Case Study 3 These attacks could shape the course of the world

## Slide 68

###### Case Study 3

###### INSIDE

## Slide 69

Adnan Khan – X: @adnanthekhan Website: adnanthekhan.com John Stawinski - Email: jstan327@gmail.com Website: johnstawinski.com #BHUSA @BlackHatEvents

## Slide 70

##### Look No Typo

Adnan Khan – X: @adnanthekhan Website: adnanthekhan.com

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisekhat
USA 2024
LOOK NO TyPé
ai-containers / .github / workflows / test-runner-ci.yaml
Code
Adnan Khan - X: eadnanthekhan Website: adnanthekhan.com
11
12
13
14
15
16
17
18
19
20
21
7272
23
24
25
26
39
40
41
42
43
Blame 153 lines (152 loc) - 5.75 KB- @
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either ¢€
# See the License for the specific language governing pe
# limitations under the License.
name: Test Runner CI
on:
merge_group: null
pull_request_target:
types: [opened, edited, reopened, synchronize]
branches: [main]
paths:
- ‘test-runner/**'
permissions: read-all
concurrency:
group: ${{ github.workflow }}-${{ github.event.pull_re
cancel-in-progress: true
- uses: actions/checkout@a5ac7e51b41094c92402da3b2437690538@afc29 # v4.1.6
if: ${{ github.event_name == ‘pull request_target' }}
with:
fetch-depth: @
ref: "“refs/pull/${{ github.event.number }}/merge”
#BHUSA
@BlackHatEvents
```

## Slide 71

##### Look No Typo

Pull_request_target workflows have access to secrets

Merge commit contains arbitrary code from fork

Adnan Khan – X: @adnanthekhan Website: adnanthekhan.com

#BHUSA @BlackHatEvents

## Slide 72

##### Show ME THE SECRETS

Adnan Khan – X: @adnanthekhan Website: adnanthekhan.com

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
“rt Snow ME THE SECRETS
65 - name: Install requirements : : .
ai-containers / tox.ini
66 run: python -m pip install -U pip tox-gh-actions
67 - name: Tox Code Blame 61 lines (54 loc) - 1.05 KB
68 run: python -m tox 7
69 env: 8 [testenv]
) d =
70 CACHE_REGISTRY: ${{ secrets.CACHE REGISTRY }} “pe
= iim 10 -r test-runner/dev-requirements .txt
71 FORCE_COLOR: 1 _-_
72 GITHUB_ TOKEN: ${{ secrets.ACTION TOKEN }} 12 python -m coverage run -p -m pytest test-runner/tests/utest.py
73 PERF_REPO: ${{ secrets.PERF_REPO }} 13 pythonpath = tests
14 passenv = DOCKER_*
74 REGISTRY: ${{ secrets.REGISTRY }} -
75 REPO: ${{ secrets.REPO }}
76 - uses: actions/upload-artifact@65462800fd760344b1a7b4382951275a@abb4808 # v4.3.3
77 with:
78 name: covdata-${{ matrix.python }}
79 path: ${{ github-.workspace }}/.coverage*
Adnan Khan - X: eadnanthekhan Website: adnanthekhan.com #BHUSA @BlackHatEvents
```

## Slide 73

##### Show ME THE SECRETS

Adnan Khan – X: @adnanthekhan Website: adnanthekhan.com

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
“rt Swow ME THE SECRETS
65 - name: Install requirements : : .
ai-containers / tox.ini
66 run: python -m pip install -U pip tox-gh-actions
67 - name: Tox Code Blame 61 lines (54 loc) - 1.05 KB
68 run: python -m tox 7
69 env: 8 [testenv]
deps =
70 CACHE_REGISTRY: ${{ secrets.CACHE REGISTRY }} “pe
= iis 10 -r test-runner/dev-requirements .txt
71 FORCE COLOR: 1
— oo commands =
72 GITHUB_TOKEN: ${{ secrets .ACTION_TOKEN ia 12 python -m coverage run -p -m pytest test-runner/tests/utest.py
73 PERF_REPO: ${{ secrets.PERF_REPO }} 1s pythonpath = tests
14 = DOCKER_*
74 REGISTRY: ${{ secrets.REGISTRY }} pee -
75 REPO: ${{ secrets.REPO }}
76 - uses: actions/upload-artifact@65462800fd760344b1a7b4382951275a@abb4808 # v4.3.3
77 with:
78 name: covdata-${{ matrix.python }}
79 path: ${{ github-.workspace }}/.coverage*
Adnan Khan - X: eadnanthekhan Website: adnanthekhan.com #BHUSA @BlackHatEvents
```

## Slide 74

##### Show ME THE SECRETS

Workflow ran tox after checking out untrusted code

Modify tox.ini or unit tests to run arbitrary code

The ‘ACTION_TOKEN’ was a GitHub Personal Access Token

Adnan Khan – X: @adnanthekhan Website: adnanthekhan.com

#BHUSA @BlackHatEvents

## Slide 75

##### AI/ML Strikes Again

Over-scoped Classic Personal Access Token (PAT) with “all boxes checked” as Actions secret Non-ephemeral runner attached to public repository Changes to workflows allowing forks access to secrets without security reviews

Adnan Khan – X: @adnanthekhan Website: adnanthekhan.com

#BHUSA @BlackHatEvents

## Slide 76

##### A Pull Request can do what?

Ability to Approve PR
Workflows
Persistence on Non- Egress from Allow- Search for Internal
Create Pull  Ephem Runner Listed IP Misconfig
ACTION_TOKEN
Request
Access To Private
Organizations
Gato-X
Enumeration from
Intel Self-Hosted
Runner

Adnan Khan – X: @adnanthekhan Website: adnanthekhan.com

#BHUSA @BlackHatEvents

## Slide 77

Not great, but it’s one employee, and the runner is in the DMZ

###### Except…

Adnan Khan – X: @adnanthekhan Website: adnanthekhan.com

#BHUSA @BlackHatEvents

## Slide 78

###### All Employees Could Become Admin

Adnan Khan – X: @adnanthekhan Website: adnanthekhan.com

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisekhat
USA 2024
ALL EMPLOYEES COULD BECOME ADMIN
name: inventory
guid: 185092a3-Qcd0-445b-8b3e—-8ef542227489
owners
topics
— infrastructure
description: Repository to manage all the inventories for intel-innersource
permissions
admin
= Support Team
write
— ALL BB Employees
= Inventory Write
= Inventory Write Generic Accoun
read
- Read CW
allow-merge-—commit
aLllow-squash-merge
allow-rebase-merge
delete-branch-on-merge
Adnan Khan - X: eadnanthekhan Website: adnanthekhan.com
ts
— name
uses
with
github-token
Add
"Earget":| “branch”
"source_type": "Repository",
"source" : a aL i
"enforcement": "active",
"condieions |: ¢
"ref_name": {
"exclude": [
"refs/heads/gh-readonly—queue/**/*"
iF
None lude!:) |)
"SALL"
J
5
,
Support Team
actions/github-script@v3
script
${{ secrets .CONF_GITHUB_TOKEN_00A }}
await github.teams.addOrUpdateRepoPermissionsInOrg({
#BHUSA @BlackHatEvents
```

## Slide 79

All employees had write access

Rulesets prevented modifying all branches

…but branches matching a specific pattern were excluded.

Adnan Khan – X: @adnanthekhan Website: adnanthekhan.com

#BHUSA @BlackHatEvents

## Slide 80

One of the secrets used by the repository seemed very interesting.

Adnan Khan – X: @adnanthekhan Website: adnanthekhan.com

#BHUSA @BlackHatEvents

## Slide 81

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
29
30
31
32
33
34
Run
> Run source venv2/bin/activate && gato-x e -t intel-restricted -sr -oJ intel_rest.json
The authenticated user is: github-1source
[+]
[+]
[+]
[!]
[+]
[+]
The GitHub Classic PAT has the following scopes: admin:enterprise, admin:org, admin:org_ hook, delete repo, project, read:audit_log, repo, user, workflow, write:discussion
Enumerating the intel-restricted organization!
The user is an organization owner!
The token also has the admin:org scope. This token has extensive access to the GitHub organization!
The organization has 30 org-level self-hosted runners!
Name: promark.PROMARKSRV@2, OS: Windows Status: online
The runner has the following labels: self-hosted, X64, Windows, promark, promarksrv@2!
Name: promark.PROMARKSRV@1, OS: Windows Status: online
The runner has the following labels: self-hosted, X64, Windows, promark, promarksrv@1!
Name: pmem_debug_tool.host-202, OS: Windows Status: online
The runner has the following labels: self-hosted, X64, Windows, pmem_debug tool, SPR, HOST202, CI!
Name: pmem_debug_ tool.host-20@, OS: Windows Status: online
The runner has the following labels: self-hosted, X64, Windows, pmem_debug tool, UT, ASD, HOST200, CI, INBANDLINUXSPR_HOST!
Name: sfip.sw.windows-01-001, OS: Windows Status: online
The runner has the following labels: self-hosted, X64, Windows, sfip.sw, sfip-sw, CSESW!
Name: sfip.sw.windows-01-002, OS: Windows Status: online
The runner has the following labels: self-hosted, X64, Windows, sfip.sw, sfip-sw, CSESWI!
Name: sfip.sw.windows-01-003, OS: Windows Status: online
The runner has the following labels: self-hosted, X64, Windows, sfip.sw, sfip-sw, CSESW!
Name: sfip.sw.windows-@1-004, OS: Windows Status: online
The runner has the following labels: self-hosted, X64, Windows, sfip.sw, sfip-sw, CSESW!
Name: sfip.sw.windows-01-005, OS: Windows Status: online
The runner has the following labels: self-hosted, X64, Windows, sfip.sw, sfip-sw, CSESW!
Name: hlp-sw.hlp-sw-27-a-runner2-001, OS: Linux Status: online
The runner has the following labels: self-hosted, Linux, X64, hlp-sw, pako-cloud-prod-3!
Name: hlp-sw.hlp-sw-27-a-runner2-002, OS: Linux Status: online
The runner has the following lahel«: self-hosted. Linux. X64. hin-sw. nako-cloud-nrod-3!
```

## Slide 82

Turns out, it was a PAT belonging to an Enterprise Admin bot account and had org-owner permissions to all organizations.

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
> Run source venv2/bin/activate && gato-x e -t intel-restricted -sr -oJ intel rest.json
[+] The authenticated user is: github-1source
[+] The GitHub Classic PAT has the following scopes: admin:enterprise, admin:org, admin:org hook, delete repo,
[+] Enumerating the intel-restricted organization!
[!] The user is an organization owner!
[+] The token also has the admin:org scope. This token has extensive access to the GitHub organization!
Turns out, it was a PAT belonging to
an Enterprise Admin bot account and
had org-owner permissions to alll
organizations.
```

## Slide 83

##### Unprecedented Access

16321
NDA
Some repos
Admin to ALL repos in ALL repos in repos in
included highly
intel-restricted
restricted IP

Admin to ALL repos in ALL repos in repos in
intel-restricted

Ability to make all repos  Ability to Delete
public Organization Entirely

Adnan Khan – X: @adnanthekhan Website: adnanthekhan.com

#BHUSA @BlackHatEvents

## Slide 84

##### Unprecedented Access

16321

Admin to ALL repos in
intel-restricted

Adnan Khan – X: @adnanthekhan Website: adnanthekhan.com

#BHUSA @BlackHatEvents

## Slide 85

##### Unprecedented Access

NDA
Some repos included highly restricted IP

Adnan Khan – X: @adnanthekhan Website: adnanthekhan.com

#BHUSA @BlackHatEvents

## Slide 86

##### Unprecedented Access

Ability to make all repos public

Adnan Khan – X: @adnanthekhan Website: adnanthekhan.com

#BHUSA @BlackHatEvents

## Slide 87

##### Unprecedented Access

Ability to Delete Organization
Entirely

Adnan Khan – X: @adnanthekhan Website: adnanthekhan.com

#BHUSA @BlackHatEvents

## Slide 88

##### Unprecedented Access

Adnan Khan – X: @adnanthekhan Website: adnanthekhan.com

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
waret ~— UNPRECEDENTED ACCESS
447 35
448 {
449 “id": 472953435,
450 “node_id": “R_kgDOHDCyWw”" ,
451 “name": ™ core-royal”,
452 “full_name": “intel-restricted/ -core-royal",
453 “private”: true,
454 “owner: {
455 “login": “intel-restricted”,
456 “id": 71398875,
457 “node_id": “MDEyOk9yZ2FuaXphdGlvbjcxMzk40Dc1",
458 “avatar_url": “https://avatars.githubusercontent.com/u a
459 “gravatar_id": "",
460 "url": “https://api.github.cor
461 “html_url": “https: //github.c
462 “followers_url": “https://api.
463 “following url": “https://api.
464 “gists url": “https://api.gitt
465 “starred_url": “https://api.g:
466 “subscriptions url": “https:/,
467 “organizations_url": “https:/,
468 “repos_url”: “https://api.gitl
469 “events_url": “https://api.gii
470 “received events url": “https
471 “type”: “Organization”,
472 “site_admin": false
473 1
474 “html_url": “https://github.com/intel-restricted a
475 “description”: “Royal Core Intellectual Property ">
476 “fork": false,
Adnan Khan - X: eadnanthekhan Website: adnanthekhan.com #BHUSA @BlackHatEvents
```

## Slide 89

##### PATs & CI/CD attack Surface

32%

Active PATs with 10 or more scopes checked

79% Percentage of active PATs with no expiration date.

## 0

Audit log events generated when enumerating PAT access

Metrics based on June 14th point in time from Two Intel orgs

Adnan Khan – X: @adnanthekhan Website: adnanthekhan.com

#BHUSA @BlackHatEvents

## Slide 90

###### Aftermath

20+
Reports
Lots of Bug Bounties
Submitted
Earned

Adnan Khan – X: @adnanthekhan Website: adnanthekhan.com

John Stawinski - Email: jstan327@gmail.com Website: johnstawinski.com

#BHUSA @BlackHatEvents

## Slide 91

Defense - How Can You Protect Your Organization From Risk?

Adnan Khan – X: @adnanthekhan Website: adnanthekhan.com

John Stawinski - Email: jstan327@gmail.com Website: johnstawinski.com

#BHUSA @BlackHatEvents

## Slide 92

###### Protecting Against Self Hosted Runner Attacks

Enable Workflow Approval Requirements

Use Least Privilege Principle for Workflow Secrets

Limit GITHUB_TOKEN Permissions

Use Managed Ephemeral Runners Whenever Possible

EDR

Use Deployment Environments for Production Secrets

Do Not Share Runners Between Public and Private Repos

Do Not Mix CI and CD

Monitor Self-Hosted Runners

## Slide 93

###### The Real Problem - Protecting Against CI/CD Attacks

Public Repo
Runners
Pwn Standard  Social
Request PR Trigger Engineering
Internal
Runner
Takeover
Runners

Public Repo
Runners

###### GitHub PAT Hygiene

Adnan Khan – X: @adnanthekhan Website: adnanthekhan.com

John Stawinski - Email: jstan327@gmail.com Website: johnstawinski.com

#BHUSA @BlackHatEvents

## Slide 94

###### Black Hat Sound Bytes

1. Continuous Integration, Continuous Destruction is Systemic 2. Public GitHub Repositories are In the Crosshairs

3. Ignorance is Breach

Adnan Khan – X: @adnanthekhan Website: adnanthekhan.com

John Stawinski - Email: jstan327@gmail.com Website: johnstawinski.com

#BHUSA @BlackHatEvents

## Slide 95

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
{Lr
Sse
Abusing Celf-Hocted GitHub Runners at
Seale oe
ADNAN KHAN | JOHN STAWINSKI a
DEF CON 32 - LAS VEGAS Laer
```

## Slide 96

##### Thank You

```
X: @adnanthekhan
```

```
Email:
me@adnanthekhan.com
Web:
https://adnanthekhan.com
```

```
Email:
jstan327@gmail.com
Web:
https://johnstawinski.com
```

## Slide 97

##### References

- ●Leaking Secret from GitHub Actions

   - <u>https://karimrahal.com/2023/01/05/github-actions-leaking-secrets/</u>

- ●GitHub Security Lab – Preventing Pwn Requests

- <u>https://securitylab.github.com/research/github-actions-preventing-pwn-requests/</u>

- ●Marcus Young Self-Hosted Runners at Facebook

   - <u>https://marcyoung.us/post/zuckerpunch/</u>

- ●GitHub Actions Runner Images

   - <u>https://github.com/actions/runner-images</u>

- ●Adnan Khan - One Supply Chain Attack to Rule Them All

- <u>https://adnanthekhan.com/2023/12/20/one-supply-chain-attack-to-rule-them-all/</u>

- ●John Stawinski – Fixing Typos and Breaching Microsoft’s Perimeter

   - <u>https://johnstawinski.com/2024/04/15/fixing-typos-and-breaching-microsoftsperimeter/</u>

Adnan Khan – X: @adnanthekhan Website: adnanthekhan.com

John Stawinski - Email: jstan327@gmail.com Website: johnstawinski.com

#BHUSA @BlackHatEvents

## Slide 98

##### References Pt. 2

- ●GitHub REST API Documentation

   - <u>https://docs.github.com/en/rest?apiVersion=2022-11-28</u>

- ●GitHub Rulesets Documentation

   - <u>https://docs.github.com/en/repositories/configuring-branches-and-merges-in-yourrepository/managing-rulesets/about-rulesets</u>

- ●GitHub Customer Story For Intel

   - <u>https://github.com/customer-stories/intel</u>

- ●Praetorian – Self-Hosted Runners are Backdoors

   - <u>https://praetorian.com/blog/self-hosted-github-runners-are-backdoors/</u>

Adnan Khan – X: @adnanthekhan Website: adnanthekhan.com

John Stawinski - Email: jstan327@gmail.com Website: johnstawinski.com

#BHUSA @BlackHatEvents
