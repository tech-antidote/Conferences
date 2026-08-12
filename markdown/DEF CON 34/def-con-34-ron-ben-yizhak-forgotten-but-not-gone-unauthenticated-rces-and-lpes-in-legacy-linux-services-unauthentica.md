---
title: "Forgotten but Not Gone Unauthenticated RCEs and LPEs in Legacy Linux Services"
speakers: ["Ron Ben Yizhak"]
conference: "DEF CON"
conference_full: "DEF CON 34"
edition: "34"
year: 2026
source_pdf: "DEF CON 34/DEF CON 34 - Ron Ben Yizhak - Forgotten but Not Gone Unauthenticated RCEs and LPEs in Legacy Linux Services - Unauthentica.pdf"
pages: 68
sha256: "ea037c2a4d24dbe798b0eee3f1e630027e0dcf9a8e7ca0b94a29d8447dc7238a"
text_chars: 11653
ocr_pages: 13
has_ocr: true
redacted_secrets: 0
ocr_confidence: 88.1
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T06:42:49Z"
---
# Forgotten but Not Gone Unauthenticated RCEs and LPEs in Legacy Linux Services

**Speakers:** Ron Ben Yizhak  
**Conference:** DEF CON 34  
**Source:** `DEF CON 34/DEF CON 34 - Ron Ben Yizhak - Forgotten but Not Gone Unauthenticated RCEs and LPEs in Legacy Linux Services - Unauthentica.pdf` (68 pages)


## Slide 1

### **Forgotten but Not Gone: Unauthenticated RCEs and LPEs in Legacy Linux Services**

###### Ron Ben Yizhak, SafeBreach

1

## Slide 2

#### **About Me**

Security Research Team Lead @ SafeBreach

Published privilege escalation and code injection methods for Windows

Previous talks ▪ DEF CON 30-33 ▪ DEF CON Singapore ▪ TyphoonCon 2026

2

## Slide 3

#### **Agenda**

Common services in Linux Research initiator (CVE-2026-24061) Privilege Escalation in GNU TelnedD Samba Inner Workings

Unauthenticated RCE in Samba via SAMR Unauthenticated RCE in Samba via Spoolss Takeaways

3

## Slide 4

#### **When was the last time you checked what your network devices are running?**

4

## Slide 5

#### **How long ago you updated your printer?**

5

## Slide 6

#### **Telnet**

###### Allows accessing the terminal of another machine remotely

###### Legacy protocol superseded by SSH Still widely used globally

6

## Slide 7

#### **Samba**

###### Open-source implementation of SMB and Active Directory Exposes the RPC interface of common services Released in 1992

7

## Slide 8

#### **RCE in TelnetD**

###### Reported by Carlos Cortes Alvarez on January 19th, 2026 Issued as CVE-2026-24061

CVSS 9.8

###### Stayed undetected since 2015

<u>https://www.safebreach.com/blog/safebreach-labs-root-cause-analysis-and-poc-exploit-for-cve-2026-24061/</u>

8

## Slide 9

#### **Root Cause Analysis**

###### Telnetd allows unauthenticated clients to set its environment variables

9


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Telnetd allows unauthenticated clients to set its
environment variables
1 LANG=en_US.UTF-8
USER=root
ENVAR=VALUE
```

## Slide 10

#### **Root Cause Analysis**

###### The spawned shell will inherit the new environment variables

10


> Recovered by OCR — confidence 95/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
The spawned shell will inherit the new
environment variables
1 LANG=en_US.UTF-8
USER=john
ENVAR=VALUE
10
```

## Slide 11

#### **Root Cause Analysis** Telnetd doesn’t perform the authentication itself

11


> Recovered by OCR — confidence 89/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Telnetd doesn't perform the authentication itself
/usr/sbin/telnetd
EF Who are you? < | >
user: password
11
```

## Slide 12

#### **Root Cause Analysis** Telnetd executes login with a format string In 2015 it was updated

\```
- PATH_LOGIN " -p -h %h %?u{-f %u}"
+ PATH_LOGIN " -p -h %h %?u{-f %u}{%U}"
\```

12

## Slide 13

#### **Root Cause Analysis**

\```
PATH_LOGIN " -p -h %h %?u{-f %u}{%U}"
\```

~$ /

--
/bin/login

help

Usage:

-
login [

-
p] [

-
h <host>] [

-
H] [[

f] <username>]

Begin a session on the system.

Options:

p

do not destroy the environment

f             skip a login authentication

h <host>      hostname to be used for

logging

H             suppress hostname in the login prompt

--

help     display this help

--
V,

version  display version

13

## Slide 14

#### **Root Cause Analysis**

\```
PATH_LOGIN " -p-h %h %?u{-f %u}{%U}"
\```

~$ /

--
/bin/login

help

Usage:

-
login [

-
p] [

-
h <host>] [

-
H] [[

f] <username>]

Begin a session on the system.

Options:

p             do not destroy the environment

f             skip a login authentication

h <host>

hostname to be used for

logging

H             suppress hostname in the login prompt

--

help     display this help

--
V,

version  display version

14

## Slide 15

**Root Cause Analysis** `PATH_LOGIN " -p -h %h %?u{-f %u}{%U}"` %h = The remote hostname of the connecting client

15

## Slide 16

#### **Root Cause Analysis**

`PATH_LOGIN " -p -h %h` `%?u` `{-f %u}{%U}"` %h = The remote hostname of the connecting client %?u = Is the variable “ user_name” non-empty?

16

## Slide 17

#### **Root Cause Analysis**

`PATH_LOGIN " -p -h %h %?u{` `-f %u}` `{%U}"` %h = The remote hostname of the connecting client %?u = Is the variable “ user_name” non-empty? {-f %u} = True block

17

## Slide 18

**Root Cause Analysis** `PATH_LOGIN " -p -h %h %?u{-f %u` `}{%U}` `"` %h = The remote hostname of the connecting client %?u = Is the variable “ user_name” non-empty? {-f %u} = True block

{%U} = False block

18

## Slide 19

#### **Root Cause Analysis**

By default, “ user_name” is not set %U is mapped to $USER Command line can be simplified as follows `/usr/bin/login -p -h remote_hostname $USER`

19

## Slide 20

#### **Root Cause Analysis**

###### The client controls the environment variables of telnetd $USER is not sanitized before formatting it! Arbitrary parameters can be injected to the command line

###### **telnetd**

**USER=FOOBAR**

**usr/bin/login -p -h %h FOOBAR**

20

## Slide 21

#### **Root Cause Analysis**

~$ /

--
/bin/login

help

Usage:

-
login [

-
p] [

-
h <host>] [

-
H] [[

f] <username>]

Begin a session on the system.

Options:

p             do not destroy the environment

f             skip a login authentication

h <host>      hostname to be used for

logging

H             suppress hostname in the login prompt

--

help     display this help

--
V,

version  display version

21

## Slide 22

#### **Root Cause Analysis** The -f parameter can be injected to skip authentication Any username can be set

telnetd

**USER -f root**

 usr/bin/login -p -h %h -f root

22

## Slide 23

**Security Patch** Parameters cannot be set before the username `-  PATH_LOGIN " -p -h %h %?u{-f %u}{%U}" +  PATH_LOGIN " -p -h %h %?u{-f -- %u}{-- %U}"`

23

## Slide 24

#### **Security Patch** Variables are sanitized for shell metachars

formatting
allowed
no
contain
remote_hostname
\t\n-
user_name
!”#$&'()*;<=>?[\
$USER
\^`{|}~
yes
Formatting
denied

24

## Slide 25

#### **What else stayed hidden?**

25

## Slide 26

#### **Manipulating Envars in TelnetD**

LD_PRELOAD forces the linker to load a library when the process is initialized

26


> Recovered by OCR — confidence 90/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Manipulating Envars in TelnetD
~$ LD_PRELOAD=/tmp/injected.so /usr/bin/login
LD_PRELOAD forces
the linker to load a
library when the
process Is initialized
libc.so
libcap.so
libpam.so
26
```

## Slide 27

#### **Manipulating Envars in TelnetD** TelnetD removes malicious envars before executing login Security fix from 1995!

keep
no
contain
LD_
environ
_RLD_
LIBPATH=
IFS=
yes
scrub

27

## Slide 28

#### **Hijack Execution Flow** Modifying $PATH will launch login from another directory

/tmp /usr/local/bin /usr/local/bin /usr/bin

28

## Slide 29

**Hijack Execution Flow** PATH_LOGIN is compiled as a full path No other process is launched by telnetd

/usr/local/bin

/usr/local/bin /usr/local/bin /usr/bin

/tmp

29

## Slide 30

#### **Envars References**

Digging through the code might reveal unique envars Telnetd retrieves only $USER Envars set in telnetd will be inherited by login

30

## Slide 31

#### **Envars References** login references $CREDENTIALS_DIRECTORY Secure mechanism to supply credentials to services

31

## Slide 32

#### **$CREDENTIALS_DIRECTORY**

32


> Recovered by OCR — confidence 86/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
$CREDENTIALS_DIRECTORY
systemd 2 systemd
service
CRED_DIR=/run/credentials/my.service
\
32
```

## Slide 33

#### **$CREDENTIALS_DIRECTORY**

###### unit file:

…
[Service]
ExecStart=/usr/bin/myservice.sh
=
LoadCredential secrets_file :/etc/my_creds.txt
…

33

## Slide 34

**$CREDENTIALS_DIRECTORY** login uses systemd credentials mechanism

does it
Is is the
is it a  contain  skip
$CREDENTIALS_DIRECTORY data
the file  auth
directory?
set? “yes”?
login.noauth?

34

## Slide 35

#### **<u>$CREDENTIALS_DIRECTORY</u>** login.noauth is even documented

35


> Recovered by OCR — confidence 95/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
$CREDENTIALS_DIRECTORY
login.noauth is even documented
CREDENTIALS
login supports configuration via systemd credentials (see https://systemd.io/CREDENTIALS/).
login reads the following systemd credentials:
login.noauth (boolean)
If set, configures login to skip login authentication, similarly to the -f option.
35
```

## Slide 36

#### **Privilege Escalation in TelnetD**

tmp root

          tmp

36


> Recovered by OCR — confidence 86/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Privilege Escalation in TelnetD
(2) USER=root, CRED_DIR=/tmp
/tmp/login.noauth
CRED_DIR=/tmp
USER=root
% (3) usr/bin/login -p -h %h root
36
```

## Slide 37

#### **Demo #1**

37

## Slide 38

#### **Privilege Escalation in TelnetD** Reported to GNU on February 5th, 2026 Patch was released on February 15th, 2026 $CREDENTIALS_DIRECTORY is unset before launching login CVE-2026-28372 was issued

38

## Slide 39

#### **Disabling The Attack Surface**

Another patch was released on March 6th, 2026

telnetd no longer accepts any envars

valid names are set using --accept-env

39

## Slide 40

**Expanding The Search** login.noauth was documented and not exploited No complex memory corruption required Could there be more services with logical vulnerabilities?

40

## Slide 41

#### **Picking The Next Target**

###### Samba is a very common service Installed widely Developed over 30 years

41


> Recovered by OCR — confidence 91/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Picking The Next Target
Samba is a very
common service
Installed widely
Developed over 30 years
Shodan Report
// GENERAL
See Total: 65,767
product: "Samba
@® Countries
24,401
5,093
United States 4,296
Portugal 3.276
France 3,260
41
```

## Slide 42

#### **Samba Inner Workings**

~$ cat / etc /samba/ smb.conf
add group script = / usr / sbin / groupadd  %g
add share command = / usr /local/bin/ addshare
passwd program = /bin/passwd %u
shutdown script = / usr /local/samba/ sbin /shutdown %m %t %r %f

42

## Slide 43

#### **Samba Inner Workings**

~$ cat / etc /samba/ smb.conf
add group script = / usr / sbin / groupadd  %g
add share command = / usr /local/bin/ addshare
passwd program = /bin/passwd %u
shutdown script = / usr /local/samba/ sbin /shutdown %m %t %r %f

43

## Slide 44

#### **Attempting Bash Injection**

_spoolss_AddPrinterEx
sprintf
smbrun

44

## Slide 45

#### **Attempting Bash Injection**

\```
addprinter_command “printer_name“ “share_name”...
\```

\```
printer_name=a“ | touch /tmp/pwned | echo “a
\```

\```
addprinter_command “a“ | touch /tmp/pwned | echo
“a“ “share_name”...
\```

45

## Slide 46

#### **Samba Sanitization Mechanism**

smbrun
escape_shell_string
execl

46

## Slide 47

**Samba Sanitization Mechanism** Non-alphanumeric chars outside of quotes are escaped

\```
addprinter_command “a“ \| touch /tmp/pwned \| echo
“a“ “share_name”...
\```

47

## Slide 48

48

## Slide 49

#### **smbrunsecret**

###### Executes a command and sends secret over stdin Secret isn’t passed on the command line to avoid leak escape_shell_string isn’t called!

49

## Slide 50

50

## Slide 51

#### **Unauthenticated RCE #1**

_samr_ValidatePassword
check_password_complexity
smbrunsecret

51

## Slide 52

**Unauthenticated RCE #1** “check password script” includes %u ncacn_ip_tcp is used samba-dcerpcd launched independently rpc start on demand helpers = no

52

## Slide 53

#### **Unauthenticated RCE #1**

53


> Recovered by OCR — confidence 90/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Unauthenticated RCE #1
~ SamrValidatePassword
UserAccountName=
</> i
[global]
check password script = crackcheck Mm
rpc start on demand helpers = no
```

## Slide 54

#### **Demo #2**

54


> Recovered by OCR — confidence 91/100 on the text kept, 60/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Demo #2
Cimpacket) C:\Users\ronb>
54
```

## Slide 55

55

## Slide 56

#### **Unauthenticated RCE #2**

\```
_spoolss_EndDocPrinter
print_job_end
generic_job_submit
print_run_command
smbrun_no_sanitize
\```

56

## Slide 57

#### **Samba as Print Server**

57

## Slide 58

#### **Unauthenticated RCE #2**

Printer share configured

“printing” config isn’t IPRINT or CUPS “print command” includes %J

58

## Slide 59

#### **Unauthenticated RCE #2**

59


> Recovered by OCR — confidence 83/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Unauthenticated RCE #2
pDocName=
"I touch /tmp/ pwned
/bin/sh -c “echo Printing [@Ouehmpypuned
[global]
printing = BSD
print command = echo Printing Bm >> /tmp/print.log
[Printer]
path = /var/tmp/
printable = yes
59
```

## Slide 60

60

## Slide 61

#### **Demo #3**

61


> Recovered by OCR — confidence 77/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Demo #3
C(impacket) C:\Users\ronb>
P| user@samba-srv: ~
user@samba-srv:~$
61
```

## Slide 62

#### **Disclosure**

Reported to Samba on March 15th, 2026 Patch was released on May 26th, 2026 CVE-2026-4408: RCE via SAMR CVE-2026-4480: RCE via Spoolss Rated CVSS 10.0 by Samba Affected all versions over 25 years!

62

## Slide 63

#### **Security Patch**

Formatting engine was refactored Admins are warned to use envars instead of format strings _ samr_ValidatePassword is restricted to DCs

63

## Slide 64

#### **Takeaways**

Issuing patches is not enough Designs and RFCs should be updated Legacy services don’t follow modern security principles

64

## Slide 65

#### **Takeaways**

The latest risks aren’t necessarily the greatest Legacy protocols are still being used in enterprise networks

65

## Slide 66

#### **Takeaways**

## secure

66

## Slide 67

#### **Conclusion**

##### 3 vulnerabilities revealed

Patch led to systemic change Services can stay vulnerable for decades Some network devices don’t describe what’s installed

67

## Slide 68

# **Thank you!**

@RonB_Y www.linkedin.com/in/ron-by

https://github.com/SafeBreach-Labs/ForgottenButNotGone

68


> Recovered by OCR — confidence 77/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Thank you!
@RonB_Y
‘in www.linkedin.com/in/ron-by
sss SafeBreach
https://github.com/SafeBreach-Labs/ForgottenButNotGone
```
