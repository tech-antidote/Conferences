---
title: "From square root to root escalating privileges in Azure containers with Python in Excel"
speakers: ["Ron Ben Yizhak"]
conference: "DEF CON"
conference_full: "DEF CON 34"
edition: "34"
year: null
source_pdf: "DEF CON 34/DEF CON 34 - Ron Ben Yizhak - From square root to root escalating privileges in Azure containers with Python in Excel - slash esca.pdf"
pages: 83
sha256: "f6fedeee9f61c437307dae089510a8d876759cdb40af8adf49842c743c94a835"
text_chars: 14931
ocr_pages: 14
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T00:27:52Z"
---
# From square root to root escalating privileges in Azure containers with Python in Excel

**Speakers:** Ron Ben Yizhak  
**Conference:** DEF CON 34  
**Source:** `DEF CON 34/DEF CON 34 - Ron Ben Yizhak - From square root to root escalating privileges in Azure containers with Python in Excel - slash esca.pdf` (83 pages)

## Slide 1

From square root to /root: escalating privileges in Azure containers with Python in Excel

Ron Ben Yizhak, SafeBreach

1

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
( OENE
Se
From square root to /root:
escalating privileges in Azure ceopners
; “a with Py tia in Excel bal A ft
= =.
Ron Ben Yizhak, SafeBreach
```

## Slide 2

#### About Me

- Security Researcher @ SafeBreach

- Published privilege escalation and code injection methods for Windows

- Previous talks

   - DEF CON 30-33

   - DEF CON Singapore

   - TyphoonCon 2026

2

## Slide 3

#### Agenda

- Overview – Python in Excel

- Exploring the Environment

- Automating the Communication

- Privilege Escalation to root

- Finding Undocumented Features

- Bypassing Excel Security Mechanism (CVE-2026-45459)

3

## Slide 4

#### Previous Work

- Shalom Carmel - The Problems of Embedded Python in Excel (Black Hat Asia 2025)

- NetSPI - A First Look at Python in Excel (October 2023)

<u>https://www.youtube.com/watch?v=zQ0Z8aAqVVc https://www.netspi.com/blog/technical-blog/red-teaming/a-first-look-at-python-in-excel/</u>

4

## Slide 5

#### Python in Excel

• Modern solution for processing data and performing analytics

- Supports many libraries

   - Matplotlib

   - NumPy

   - pandas

5

## Slide 6

#### Python in Excel

• Calculations run in Microsoft Cloud

np.arange(0, 10, 2) [0,2,4,6,8]

6

## Slide 7

#### Data Security

Secured containers

non-persistent data

restricted access

7

## Slide 8

#### Exploring the Environment

8

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Exploring the Environment
Python Editor wx
“All Python cells ~~
Sheet! a
AL > o- Bdge 2
1 import subprocess
2 subprocess.check_output("“whoami", shell=True).decode()
jovyan
```

## Slide 9

#### Exploring the Environment

- Code is executed using Jupyter

- Persistent execution state

- Cell-by-cell execution model

- jovyan is unprivileged

9

## Slide 10

#### Environment Variables

- No tokens or API keys found

- Variables indicate there are many things to uncover

   - OfficePy__ComputeResourceKey=[SNIP] OfficePy__CodeExecutionService__LoopbackUrl=https://127.0.0.1:5002

   - Kestrel__Endpoints__HttpsInlineCertFile__Certificate__Path=/mnt/secrets/sslcert OFFICEPY_OUTBOUND_BROKER_HOSTNAME=fs.officepy.microsoftusercontent.com

10

## Slide 11

#### Processes

entrypoint.sh
root
jupyter-notebook
jovyan
python -m ipykernel_launcher
jovyan
dotnet httpproxy.dll http://*:8000/
root
dotnet CodeExecutionService.dll
root

11

## Slide 12

#### Directories

/
drwxr-xr-x    root:root app
drwxr-x--- root:root officepyapp
…

12

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Directories
aan
— 9 drwxrxr-x root:root app
= 7 drwxt-x--- root:root officepyapp
— |...
12
```

## Slide 13

#### Web Services

HTTP Proxy

http://127.0.0.1:8000

###### Code Execution Service

https://127.0.0.1:5002

###### Outbound Broker

https://fs.officepy. microsoftusercontent. com:5050

13

## Slide 14

#### Proxy Server

Jupyter

GET http://8.8.8.8

403

Proxy

14

## Slide 15

#### Proxy Server

Jupyter

GET /

Proxy

timeout

8.8.8.8

15

## Slide 16

#### Code Execution Service

Jupyter

GET /

“Code Execution Service||”

Code Execution Service

16

## Slide 17

#### Outbound Broker

Jupyter

GET /data 401 You need to authenticate to access this resource. Outbound Broker

17

## Slide 18

#### Recap

Outbound Broker

prodp6-p1-frc.officepy. svc.usercontent.microsoft

Container Host

Code Exec Service Proxy Jupyter

18

## Slide 19

19

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
JOVYAN
/OFFICERYAPP,
/MNT/SECRETS
19
```

## Slide 20

#### Python Libraries

/app/officepy/lib/python3.12/site-packages

beautifulsoup
excel
matplotlib
officepyai
pandas

20

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Python Libraries
/app/officepy/lib/python3.12/site-packages
a
beautifulsoup
excel
matplotlib
officepyai
pandas
```

## Slide 21

#### Python Libraries

• Exfiltrating data takes too long

zip -r libs.zip ./site_packages

timeout

21

## Slide 22

#### Automating the Communication

- Excel restricts us

- We need to direct communication

- REST API requests were sniffed

Server

Excel

Fiddler

22

## Slide 23

#### Automating the Communication

```
POST https://service-preview.officepy.svc.usercontent.microsoft
Authorization: Bearer eyJ[SNIP]
```

```
HTTP/1.1 201
{
```

- `"url": "https://prodp6-p1-frc.officepy.svc.usercontent.microsoft", [SNIP]`

```
}
```

23

## Slide 24

#### Automating the Communication

```
POST https://prod...microsoft/api/environments/createenvironmentandruntime
Authorization: Bearer eyJ[SNIP]
```

```
HTTP/1.1 201
{
"runtimeId": UUID,
"id": UUID,
[SNIP]
}
```

24

## Slide 25

#### Automating the Communication

```
POST https://prod...microsoft/api/environments/{ID}/runtimes/{RUNTIME_ID}/batchexecute
Authorization: Bearer eyJ[SNIP]
{
"items": [
{
"id": 2,
"roundId": 1,
"preCode": "",
"code": "1+1",
"timeoutSeconds": 30,
"flags": 6,
"codeOrigin": 1,
"clientTagId": 0
}
],
"roundIndex": 1
```

```
}
```

25

## Slide 26

#### Python Libraries

- officepyai - small library for reading .xlsx files

- excel - large library to manage the execution of the client’s code

26

## Slide 27

#### Python Libraries

• excel library reveals credentials for outbound broker

OfficePy__ComputeResourceId:OfficePy__ComputeResourceKey

base64

U2FmZUJyZWFjaA…

27

## Slide 28

#### Outbound Broker

- Authentication accepted

- Parameters remained unknown

Jupyter

GET /data?url=https://8.8.8.8 Authorization: Basic U2Fm… 400 data-download-host-not-trusted

Outbound Broker

28

## Slide 29

#### File Upload

- The “uploadeddata” class mentions /mnt/data_upload

- Large files inserted into cells are uploaded

29

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
File Upload
¢ The “uploadeddata” class mentions /mnt/data_upload
* Large files inserted into cells are uploaded
A
ma img=x1("A1")
29
```

## Slide 30

#### File Upload

```
POST /api/environments/{ID}/runtimes/{RUNTIME_ID}/data/start?dataId={DATA_ID}&etag={ETAG}
Authorization: Bearer eyJ[SNIP]
```

30

## Slide 31

#### File Upload

```
POST /api/environments/{ID}/runtimes/{RUNTIME_ID}/data/start?dataId={DATA_ID}&etag={ETAG}
Authorization: Bearer eyJ[SNIP]
```

```
POST /api/environments/{ID}/runtimes/{RUNTIME_ID}/data/upload?dataId={DATA_ID}
Authorization: Bearer eyJ[SNIP]
Content-Type: multipart/form-data;
BINARY_DATA
```

31

## Slide 32

#### File Upload

/mnt/data_upload/{RUNTIME_ID}

{DATA_ID}.stat

{DATA_ID}.etag

{DATA_ID}.data

32

## Slide 33

#### File Upload

33

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
OOMON ODA KWND =
File Upload
[rv]
None
Python Editor
1 import subprocess
2 img = xl("A1")
3 print(subprocess.check_output(["1ls", "-R", "/mnt/data_upload"], text=True) )
/mnt/data_upload:
b66af9b1-91c7-4321-b9ca-26ee5e86d94d
/mnt/data_upload/b66af9b1-91c7-4321-b9ca-26ee5e86d94d:
precodedata_28a4bd80317b460889fd05d734b56a3b_0 1.data
precodedata_28a4bd80317b460889fd05d734b56a3b_ 0 1.etag
precodedata_28a4bd80317b460889Fd05d734b56a3b_0 1.stat
33
```

## Slide 34

#### File Upload

/mnt/data_upload/{RUNTIME_ID}

root:root {DATA_ID}.stat

root:root {DATA_ID}.etag

root:root {DATA_ID}.data

34

## Slide 35

Could we manipulate a write operation done as root with a symbolic link?

35

## Slide 36

#### Symbolic Link Exploits

weak user

ln -s /root/pwned /tmp/log.txt

/tmp/log.txt

36

## Slide 37

#### Symbolic Link Exploits

weak user

ln -s /root/pwned /tmp/log.txt

/tmp/log.txt

/root/pwned

37

## Slide 38

#### Symbolic Link Exploits

root

weak user

/tmp/log.txt

/root/pwned

38

## Slide 39

#### Exploiting File Upload

• .data file is recreated before writing, resetting our symlink

- writing to .etag follows symlink!

39

## Slide 40

40

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
-g9OvsSsWd AalHt
‘LavaH DOD
“ap
```

## Slide 41

#### Exploit Chain

1. symlink source

2. payload

.etag

3. symlink destination

4. goal

41

## Slide 42

#### Exploit Limitation

payload length

# A-Z

encoding

42

## Slide 43

#### Finding Symlink Target

- Several files have the “Set User ID” permission

- The file will be executed as root

-
~$  ls  l /usr/bin/chage
- - -
rwsr xr x root  root usr
/ /bin/ chage

43

## Slide 44

#### Exploiting SUID Files

- Payload must be ascii

- We can overwrite file with bash script

- SUID isn’t applied to bash script

#!/bin/bash
whoami

-rws chage

44

## Slide 45

#### Exploiting SUID Files

- Special ELF was compiled

- Payload wasn’t executed as root

push $ 59
rax
pop  %
syscall

-rws chage

45

## Slide 46

### What if we aren’t the ones that will execute our payload?

46

## Slide 47

#### Monitoring Process Creation

- /usr/bin/stat is executed periodically

Code
Execution
Service

procmon.py

47

## Slide 48

48

## Slide 49

#### Privilege Escalation to root

Code
Execution
Service

ln -s

{DATA_ID}.etag

/usr/bin/stat

49

## Slide 50

#### Privilege Escalation to root

Code
Execution
Service

etag=PAYLOAD

/usr/bin/stat

{DATA_ID}.etag

50

## Slide 51

#### Privilege Escalation to root

Code
Execution
Service
PAYLOAD

{DATA_ID}.etag /usr/bin/stat

51

## Slide 52

#### Privilege Escalation to root

payload executed!

Code
Execution
Service

/usr/bin/stat

52

## Slide 53

#### Exfiltrating Data

/mnt/secrets

services binaries

config files

53

## Slide 54

#### Development Artifacts

- Decompiled binaries reveal interesting names

_(x)_

#### _f(x)_

TetOnly_LocalDevComputeResourceId

LicenseBypassTenants

LicenseBypassMsaUsers

SubscriptionId_OfficeProGov

IsTestUser ()

IsGovernmentTenantDeployment ()

54

## Slide 55

#### Configuration File

Identities

Key vaults

deploymentdata.json

Databases

Governmental

55

## Slide 56

56

## Slide 57

#### Worldwide Servers

- Config file reveals hundreds of container hosts

- At the time, 88  were available

- Exploit worked on all of them!

57

## Slide 58

#### Privilege Escalation Demo

58

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Privilege Escalation Demo
EXPLORER - run_container.py M X.
v OFFICEPY
> _pycache
> exploit scripts
OFFicePy
© payloads z :
i get_bearer_token, HOSTNA\
® whoamipy
OfficePy.py create_logger()
= requirements.txt filename = os.path.basename(_ file)
® run_container.py logger = logging. getLogger(filename)
logger. addHandler (logging .StreamHandler())
logger. setLevel (log,
logger
® utils.py
main():
hostnames = HOSTNAMES_LIST
logger = create_logger()
token = get_bearer_token()
hostname in hostnames:
print (hostname)
container cePy(hostname, token, logger)
container.whoami()
input ()
Exc
print (ex)
_name__
main()
> OUTUNE
> TIMELINE
x mains @oAo P } Ron Ben Yizhak (3 days ago) Ln 25,Col1 Spaeegy UTF-8 CRLF {)} Python &3 3.13.9 (Excel)
```

## Slide 59

#### Pulling Container Image

- New environment variable exposed container image

- Can be pulled anonymously

- Gives full access to the filesystem

59

## Slide 60

#### Mapping Container Images

- Servers use various images

- Pilot servers were accessed

mcr.microsoft.com/officepy/codeexecutionjupyter:latest
mcr.microsoft.com/officepy/codeexecutionjupyter2:latest
mcr.microsoft.com/officepy/codeexecutionjupyterext1:latest
mcr.microsoft.com/officepy/codeexecutionjupyterext2:latest
mcr.microsoft.com/officeagent/officeagent :Production-Canary
mcr.microsoft.com/officeagent/officeagent :Production-Pilot
mcr.microsoft.com/officeagent/officeagent:MSIT
…

60

## Slide 61

#### Exploring New Features

entrypoint.sh
root
jupyter-notebook
jovyan
node /app/api/src/app.js
jovyan

httpproxy.dll http://*:8000/ root

dotnet CodeExecutionService.dll

root

61

## Slide 62

#### Exploring New Features

- `' Environment configuration loaded'`

- `' IMAGE_SEARCH_ENABLED: %s', ' ANTHROPIC_API_KEY: %s',`

- `' OPENAI_API_KEY: %s', ' ANTHROPIC_BASE_URL: %s',`

- `' OFFICE_AGENT_MODEL: %s',`

- `' AZURE_OPENAI_ENDPOINT: %s',`

- `' AZURE_OPENAI_DEPLOYMENT_NAME: %s',`

- `' AZURE_OPENAI_API_KEY: %s',`

- `' RELAY_URL: %s',`

- `' OAGENT_AGENTID: %s',`

- `' LD_PRELOAD: %s',`

- `' COPILOT_CLI_PATH: %s',`

- `' OFFICEPY_EXT_BUILD_SPEC: %s',`

- `' OFFICEPY_CODEEXEC_IMAGE_NAME: %s',`

- `' OfficeAgentVersion: %s',`

62

## Slide 63

#### LLM Proxy

external server

container host
Jupyter node
prompt

63

## Slide 64

#### LLM Proxy

external server

container host
Jupyter node
prompt

64

## Slide 65

#### LLM Proxy

@officeagent
excel-agent
outlook-agent
ppt-agent
word-agent
…

@officeagentskills
connector-search
enterprise-fetch
enterprise-search
web-fetch
…

65

## Slide 66

66

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Office Agent — “Taste driven” multi-agent system for
Microsoft 365 Copilot
@ QiZhang §
Sep 29, 2025
September 29, 2025 + 5 min read
Vibe working: Introducing
Agent Mode and Office
Agent in Microsoft
365 Copilot
By Sumit Chauhan, Executive Vice President, Office Product Group, Microsoft
i2 Agent mode
Listen to this post
Powered by Microsoft Copilot i/ /
```

## Slide 67

#### Office Agent

Can enterprise documents be exfiltrated?

Can malicious documents be generated and shared?

67

## Slide 68

#### Responsible Disclosure

- Reported to Microsoft on February 5th, 2026

   - Privilege escalation

   - Public docker images

   - Risks in AI integration

   - Sensitive config file

- Privilege escalation fixed on March 1st (ver 16.0.19828.43251 )

68

## Slide 69

Can we weaponize a workbook with Python code?

69

## Slide 70

#### Excel 4.0 Macros

- Allow basic calculations

- Stored in worksheet cells

- Executed locally

- Used to deliver malware

70

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Excel 4.0 Macros
* Allow basic calculations A |
¢ Stored in worksheet cells ; ;
* Executed locally 3 3
* Used to deliver malware : :
6 |=SUM(A1:A5) |
CALL function
Description
Calls a procedure in a dynamic link library or code resource. There are
70
```

## Slide 71

#### Security Mechanisms

• Mark of the web

" “
PS C: \ Users \ ronb \ Downloads>  get - content - path . \ workbook.xlsx  - Stream Zone.Identifier
[ ZoneTransfer ]
ZoneId =3
ReferrerUrl =http:// 127.0.0.1:8000 /
HostUrl =http:// 127.0.0.1:8000 /workbook.xlsx

71

## Slide 72

#### Security Mechanisms

##### • Trusted Records

HKCU\Software\Microsoft\Office\16.0\Excel\ Security\Trusted Documents\TrustRecords

72

## Slide 73

#### Security Mechanisms

- Activating =IMAGE requires 2 clicks

73

## Slide 74

#### Security Mechanisms

- Activating =IMAGE requires 2 clicks

74

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Security Mechanisms
° Activating =IMAGE requires 2 clicks
GET /
2026-07-09T11:32:56+03:00
213.8.170.106
OPTIONS /
2026-07-09T11:32:56+03:00
213.8.170.106
request catcher
GET / HTTP/1.1
Host: excel.requestcatcher.com
Accept-Auth: badger ,Wlid1.1,Bearer,Basic,NTLM,Digest,Kerberos
Authorization: Bearer
Connection: Keep-Alive
User-Agent: Mozilla/4.0 (compatible; ms-office; MSOffice 16)
X-Featureversion: 3
X-Ms-Authdomainsupport: True
X-Ms-Cookieuri-Requested: t
X-Ms-Openauthenticationsupport: True
X-Of fice-Major-Version: 16
74
```

## Slide 75

#### Bypassing Trusted Records

- “Enable Content” isn’t shown for Python code

75

## Slide 76

#### Bypassing Trusted Records

• “Enable Content” isn’t shown for Python code

RichValue({'type': 'WebImage', 'address': 'https://malicious.com/image.png'})

"result": {“type": "WebImage", "address": "https://malicious.com/image.png"}

76

## Slide 77

#### Bypass Demo #1

77

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Bypass Demo
Gm Excel
ir Good morning
Home
Pag New blank workbook
B
New
. Favorites Shared with Me 2 Search
Ls You haven't opened any workbooks recently. Click Open to browse for a workbook.
pen
More workbooks —>
DS
Account
Options
10:58
Vv
```

## Slide 78

#### Bypass Network Isolation

- Data can be fetched by client and uploaded to container

server.com
1
"result": {“type": "WebImage",
"address": "https://server.com/fetch_data"}
2 GET /fetch_data
3
OfficePy

78

## Slide 79

#### Bypass Demo #2

79

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Bypass Demo
Gm Excel
ft Good morning
Home
gy bh pa New blank workbook
Recent) Favorites Shared with Me PP Search
e You haven't opened any workbooks recently. Click Open to browse for a workbook.
pen
More workbooks —>
a
Account
Options
11:06
A OY ENG FED ® is oss026
```

## Slide 80

#### Responsible Disclosure

- Disclosed to Microsoft on March 23th, 2026

- Patched on June 9th

- CVE-2026-45459 was issued

80

## Slide 81

#### Takeaways

Least privilege principle

“Least data” principle

81

## Slide 82

#### Conclusion

- Complex environment unveiled

- 88 containers rooted

- Security mechanism bypassed

- Tools released for further research

82

## Slide 83

## Thank You!

@RonB_Y www.linkedin.com/in/ron-by

https://github.com/SafeBreach-Labs/FromSquareRootToSlashRoot

83
