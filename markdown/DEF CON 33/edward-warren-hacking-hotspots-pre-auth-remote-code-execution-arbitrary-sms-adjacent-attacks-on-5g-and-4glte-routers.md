---
title: "Hacking Hotspots Pre-Auth Remote Code Execution, Arbitrary SMS & Adjacent Attacks on 5G and 4GLTE Routers"
speakers: ["Edward Warren"]
conference: "DEF CON"
conference_full: "DEF CON 33"
edition: "33"
year: 2025
source_pdf: "DEF CON 33/Edward Warren - Hacking Hotspots Pre-Auth Remote Code Execution, Arbitrary SMS & Adjacent Attacks on 5G and 4GLTE Routers.pdf"
pages: 33
sha256: "f86478b5408839bb8a6d138b269d9bf54e1f20c98becde841416f4bd8ddc5a1f"
text_chars: 9618
ocr_pages: 16
has_ocr: true
redacted_secrets: 0
ocr_confidence: 85.6
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T06:59:35Z"
---
# Hacking Hotspots Pre-Auth Remote Code Execution, Arbitrary SMS & Adjacent Attacks on 5G and 4GLTE Routers

**Speakers:** Edward Warren  
**Conference:** DEF CON 33  
**Source:** `DEF CON 33/Edward Warren - Hacking Hotspots Pre-Auth Remote Code Execution, Arbitrary SMS & Adjacent Attacks on 5G and 4GLTE Routers.pdf` (33 pages)


## Slide 1

### Project Retrospective Presentation

Duration 00 min

\

Company Name

Month / Year

Project Name


> Recovered by OCR — confidence 75/100 on the text kept, 57/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Pre-AUTH RCE, AFBITraryY SMS & aDJacenryT
ATTACKS ON 5G anD LTE ROUTerS
GITHUB.COM/ACTUATOr By Edward Warren
```

## Slide 2

#### **Agenda**

whoami Related Work Tuoshi 5G & 4G routers Kuwfi 5G & LTE routers Demos <u>Conclusions</u> _Related Tuoshi Kuwfi_ _Demos Conclusions Work Devices Devices_

ACTUATOR.SH

Github.com/Actuator

## Slide 3

ACTUATOR.SH

#### **Whoami**

Sr. Cybersecurity Analyst **F500** Former Information Security Analyst

Previous Talks:

Github.com/Actuator

## Slide 4

## Related Work

DEFCON 27 | “Reverse Engineering 4g Hotspots for Fun Bugs Net Financial Loss” - g richter


> Recovered by OCR — confidence 85/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Related Work
LTE MPIIO - Web Interface Black Box
>» © goform get cmd process
>» © goform set cmd process
For reading data. > Ma i18n a
- /goform/goform_set_cmd process > Th ima
For writing data. Ly index. html
DEFCON 27 | “Reverse Engineering 4g Hotspots for Fun Bugs Net Financial Loss” - g richter
```

## Slide 5

ACTUATOR.SH

## Related Work

https://github.com/TomKing062/CVE-2022-38694_unlock_bootloader/discussions/55


> Recovered by OCR — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Related Work ACTUATORSH
Tuoshi 5G CPE Router NR500-EA udx710 unlocking help!? #55
( Dadosed ) CE Preservio asked this question in Q&A
ae) Preservio on Feb 5, 2024 edited
Hello, i have recently bought Tuoshi 5G CPE Router NR500-EA from aliexpress. | am very new to android or unlocking
bootloader/customRoms.
The UI is very buggy and has hidden menus that i was able to find via browsers developer mode. One Menu is called debug mode, which has
USB mode and Debugging mode on/off. However when i turn these on i am not sure if it does any thing, adb & fastboot can't connect to it.
SSH is also enabled by default, i cannot login as root or admin and have tried the ui/wifi passwords which do not work. | am able to login as
‘user’ where the host name shows up as ‘udx710". With the user account i can't really do anything as most apps in /bin/ are locked down and
‘user’ doesn't have permissions to use them (simple system apps like Is & pwd).
https://github.com/TomKing062/CVE-2022-38694_unlock_bootloader/discussions/55
```

## Slide 6

## Related Work

medium.com/@sengkyaut

ACTUATOR.SH


> Recovered by OCR — confidence 90/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Related Work
Name Description
024-48442 Incorrect access control in Shenzhen Tuoshi Network Communications Co.,Ltd 5G CPE
Router NR500-EA RGSOOUEAABxCOMSLICv3.2.2543.12.18 allows attackers to access
the SSH protocol without authentication.
VE-2024-48440 Shenzhen Tuoshi Network Communications Co.,Ltd 5G CPE Router NR500-EA
RGSOOQUEAABxCOMSLICVv3.2.2543.12.18 was discovered to contain a command injection
vulnerability via the component at _command.asp.
® medium.com/@sengkyaut
AT command:
Command: | AT+CGMI
Quectel, OK,
```

## Slide 7

Shenzhen Tuoshi Network, Communications Co.,LTD Model: 5G CPE Router NR500-EA Quectel RG500U Series 5G Chip

ACTUATOR.SH

## Slide 8


> Recovered by OCR — confidence 84/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Search Results
The
re are|743)CVE Records that match your search
Name
6 Te tack overflows
nis ac9 v1.0 firmware v15.03.05.19 contains a
1 was discovered to con] cearch Results ote arbitrary code execution.
lad to remote arbitrary code e:
rds that match your search.
vi.11 was discovered to cont {There are 942 CVE Reco
03.06.47 and classifie
ne leads to stack-based
5 RE11S v1.11 was discovered to cont
found in Tenda ACS 15-
A vulnerability was
argument time/timeZo
A vulnerabili
abili i = c
leads to ae eeatid as critical ha manipulation of the
“base uffer fe) may be used.
verflow.} cve 36 Avulnerability has been found in Tenda ACS 15.03.06-
Jgoformyopensched Wit The manipulation of the argum of the fil /
ile /goform/SetD
eV
A vulnerabili i
ility, which i
' as classified a ‘exploit has been disclosed to the public and may be used.
tical has been found in D-Link pir-513 1 and may be used
HTTP Rei
quest Ha i
argument currime leads to buffer overflow. It is possible to initiate
that are no longer supported by the maintainer. ue is so
me unknown fi
uncti
A vulnerabili
ility classified as critical has Sly affects products
A vulnerability was found in UTT HiPER 840G up to 3.1.1-190328- It ha: 2 i.
nent API. The en disclosed to the public
leads to
stack-based b :
sa overflow. I i joform/formP2PLimitConns of the compo
i be used. The ve
A vulnerability classified as criti hus been disclosed to
curTime leads to buffe ical was} cy 5.6733 A vulnerability Wee fou G up to 3.4.1-190328: ¥
r overflow. The a /goform/formconfigor al of the component API. The mani
The exploit has been disclosed to the public and may be used. The veng
found in uTT HiPER 840G up to 3.1.
A vulnerabili
ility classi ao
ty ssified as critical has § > OA vulnerability was
component API. The manipulation of the argument passwdi leads to buy
acted early about this disq
ar 7
gument curTime leads to buffer
A vulner bi r ove public and may be used. The vendor was conti
ability was found in D-Link ‘ 7 Avulnerability was fo D-Link DIR-619
ink DIR- The manipulation of th webpage le
leads to b
uff
‘er overflow. The attack ma may be used. This vulnerability only affects Pr
CV 6 A vulnerability has been found in D-Link DIR-619L 2.06Bi
```

## Slide 9


> Recovered by OCR — confidence 92/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Top 10 CVE ID Count by Vendor
Edimax
1.3%
Embedthis GoAhea...
1.6%
1.6%
Jensen of Scandinavia
8.2% |
D-Link
```

## Slide 10

ACTUATOR.SH

1. Add section title Slide 00

2. Add section title Slide 00

**≠** session token


> Recovered by OCR — confidence 82/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Content-Length: 118
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/S.0 Windows NT 10.0; Winé4; x6é4) AppleWebKit/537.36
(KHTML, like ¢ ko) Chrome/132.0.0.0 Safari/537.36
ccept: application/json, text/javascript, */*;
ntent-Type: application/json
2.168. 1
ept-Language: ¢« US,en;q=0.9
Well, that’s not guage=EN; a sett ings=}7B%22s idebar-
usernam
a good sign.
```

## Slide 11

Binary: jhttpd

CVE-2025-43989

ACTUATOR.SH


> Recovered by OCR — confidence 84/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
21| iVar2 = cJSON_GetObjectItem(param 2,"ntpserver0");
23 peVar9 = *(char **) (iVar2 + 0x10);
24 peVar3 = (char *)nvram_safe_get ("ntp_server0");
D5 ivar2 = strcmp (pcVar9,pcVar3) ;
30 bVarl = true;
en goto LAB 00430600;
32 }
33} }
34) bvarl = false;
36) ivVar2 = cJSON_GetObjectItem(param 2,"ntpserver1");
38 peVar9 = *(char **) (iVar2 + 0x10);
39 peVar3 = (char *)nvram_safe_get ("ntp_serverl");
40 iVar2 = strcmp (pcVar9,pcVar3) ;
42 nvram_set("ntp_server1",pcVar9);
43 bvarl = true;
44 nvram_modifi
Binary: jhttpd
27 [nvram set("ntp server0",pcVar9);
28 nvram_modified = 1;
nvram modified = 1;
CVE-2025-43989
```

## Slide 12

# DEMO I

ACTUATOR.SH

## Slide 13

ACTUATOR.SH

CVE-2025-43982


> Recovered by OCR — confidence 79/100 on the text kept, 51/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
sh-S.@0# cat /fetc/shadow
cat /fetc/shadow
root :abjNLSDNYTy/6:19898
Sys:*:19898:0:99999:7
sync:*:19898:0:99999:
man:*:19898:0:99999:7
Lp:*:19898:0:99999:7::
uucp:*:19898:0:99999:7
proxy:*:19898:0:99999:
www —-data:«:19898:0:999
sshd: !:19898:0:99999:
radvd:!:19898:0:99999
ntp:!:19898:0:99999:7
user :: 19898:0:99999:7
CVE-2025-43982
abjJNLSDNYTy/6
```

## Slide 14


> Recovered by OCR — confidence 92/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
censys
HTTP 80/TCP
BOOTSTRAP JQUERY
—
Status 200 OK
HTML Title NR Router
HTTP 7547/TCP
Status 401 Unauthorized
SSH 10022/TCP
REMOTE ACCESS
```

## Slide 15

ACTUATOR.SH

## Slide 16

Tuoshi, AKA “DIONLINK” Model: LT15D & LT21B

http://www.tuoshi.net/productview.asp?id=226 http://www.tuoshi.net/productview.asp?id=218 http://amazon.com/s?k=dionlink

LTE/4G

ACTUATOR.SH

## Slide 17

CVE-2024-53931

ACTUATOR.SH


> Recovered by OCR — confidence 91/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ile: UndefinedFunct
n 00426300 jhttpd_dionlink)
,int )
ting > Online Checker
Online Keeper Switch on
Check IP Address 1
Check IP Address 2
ck interval (s )
Offline Time (min) Nether to reboot automatically if offline
CVE-2024-53931
```

## Slide 18

# DEMO II

ACTUATOR.SH

## Slide 19

KUWFI Model: GC111, AC900 & CPF908 4G/ LTE Routers

https://www.amazon.com/stores/page/5C5D20ED-7483-4322-948A-D4642C61DFFE

ACTUATOR.SH

## Slide 20

LTE/4G
CVE-2025-43984
CVE-2025-43985
CVE-2025-43986

###### Model: GC111

Architecture: ARM EABI5 (hard-wired to run on ARMv5‐style cores) No address‐space randomization (fixed load address) Format: ELF 32-bit LSB shared object (non-PIE)

## Slide 21


> Recovered by OCR — confidence 72/100 on the text kept, 49/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Location
Help
String Search [CodeBrowser: Kuwfi:/kthy_topsw_goahead]]
String View
String T
string
—
™ del file fail");
N
size_t svari;
char *__s;
_s = (char *)maificc(svari + 10);
——-—— — — — share process.c"™,0x17,"kthy httpshare-log™,
“kthy httpshare call system: [%s5s] \n"™, se
ny
```

## Slide 22

# DEMO III

ACTUATOR.SH

## Slide 23

###### Model: AC900

LTE/4G

CVE-2024-53945 CVE-2024-53946

SoC (System on Chip): CPU: MT7621+MT7603E+MT7612E Flash: 16MB Flash RAM: 128MB DDR3 RAM

https://kuwfi.com/products/kuwfi-gigabit-wireless-router-4g-lte-wifi-router-dual-band-portable-wifi-modem-hotspot-64-user-with-gigabit-wan-lan-rj11-port

## Slide 24

CVE-2024-53945

ACTUATOR.SH


> Recovered by OCR — confidence 83/100 on the text kept, 63/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Decompile: FUN_004205a4
we setvar (
1 wek
1 wek
1 w
(ct ) wek
it wek
1 €
1 =w
(webserver)
Mozilla
537.36 (K
html, application/j
apng,
linksn : pass=<édialnumber=
CVE-2024-53945
```

## Slide 25

# DEMO IV & V

ACTUATOR.SH

## Slide 26

##### Model: CPF908

LTE/4G

https://fcc.report/FCC-ID/2AX9H-25126/5081635

https://m.media-amazon.com/images/I/61eE90YzOQL._AC_SL1500_.jpg


> Recovered by OCR — confidence 88/100 on the text kept, 48/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Model: CPF908
China Unicom
08.12
LTE/4G
https://fec.report/FCC-ID/2AX9H-25126/5081635
https://m.media-amazon.com/images/|/6leE9OYZOQL._AC_SL1500_.jpg
```

## Slide 27

https://forums.quectel.com/uploads/short-url/avUSxfJeKqWJzAie8wEZCshlXjm.pdf


> Recovered by OCR — confidence 88/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
OU ECTEL 5G Module Series
* Build a Smarter World RG50xQ&RM5xxQ Series AT Commands Manual
8.3. AT+CSCA Service Center Address
8.4. AT+CPMS_ Preferred Message Storage
8.5. AT+CMGD_ Delete Messages
8.6. | AT+CMGL List Messages...
8.7. | AT+CMGR_ Read Messages
8.8. | AT+CMGS Send Messages
8.9. AT+CMMS Send More Messages
8.10. AT+CMGW Write Messages to Memory
8.11. AT+CMSS Send Messages from Storage
https://forums.quectel.com/uploads/short-url/avUSxfJeKqWJzAie8wEZCshlXjm.pdf
```

## Slide 28

# DEMO VI

ACTUATOR.SH

## Slide 29

Chipset: Snapdragon X62

## Slide 30

# DEMO VII

ACTUATOR.SH

## Slide 31

# DEMO  VIII

ACTUATOR.SH

## Slide 32


> Recovered by OCR — confidence 93/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
CONCLUSIONS
CWE-284: Improper Access Control
CWE-200: Information Disclosure
CWE-287: Improper Authentication
CWE-78: Improper Neutralization of Special Elements
used in an OS Command (‘OS Command Injection’)
CWE-352: Cross-Site Request Forgery (CSRF)
```

## Slide 33
