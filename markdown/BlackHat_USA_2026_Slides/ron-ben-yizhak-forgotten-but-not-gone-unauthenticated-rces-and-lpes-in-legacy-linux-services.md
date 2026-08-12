---
title: "Forgotten but Not Gone Unauthenticated RCEs and LPEs in Legacy Linux Services"
speakers: ["Ron Ben Yizhak"]
conference: "Black Hat"
conference_full: "Black Hat USA 2026"
edition: "USA"
year: 2026
source_pdf: "BlackHat_USA_2026_Slides/Ron Ben Yizhak_Forgotten but Not Gone Unauthenticated RCEs and LPEs in Legacy Linux Services.pdf"
pages: 69
sha256: "0d2092003e689035bd11b0cda800cf116cfc5e546a829d91b0bf75356ad2d872"
text_chars: 10983
ocr_pages: 9
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T23:15:22Z"
---
# Forgotten but Not Gone Unauthenticated RCEs and LPEs in Legacy Linux Services

**Speakers:** Ron Ben Yizhak  
**Conference:** Black Hat USA 2026  
**Source:** `BlackHat_USA_2026_Slides/Ron Ben Yizhak_Forgotten but Not Gone Unauthenticated RCEs and LPEs in Legacy Linux Services.pdf` (69 pages)

## Slide 1

## Slide 2

Forgotten but Not Gone: Unauthenticated RCEs and LPEs in Legacy Linux Services

Ron Ben Yizhak, SafeBreach

2

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Forgotten but Not Gone:
Unauthenticated RCEs
and LPEs in Legacy
MnmuxXx Services <— ;
< oo
=
NYS a\ Bat”
Ron Ben Yizhak, SafeBreach
black hat
©3232. 2
```

## Slide 3

##### ABOUT ME

Security Research Team Lead @ SafeBreach

Published privilege escalation and code injection methods for Windows

Previous talks ▪ DEF CON 30-33 ▪ DEF CON Singapore ▪ TyphoonCon 2026

3

## Slide 4

##### Agenda

Common services in Linux Research initiator (CVE-2026-24061) Privilege Escalation in GNU TelnedD Samba Inner Workings

Unauthenticated RCE in Samba via SAMR Unauthenticated RCE in Samba via Spoolss Takeaways

4

## Slide 5

##### When was the last time you checked what your network devices are running?

5

## Slide 6

##### How long ago you updated your printer?

6

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
* 2003
woon
2004
Boon
FILES
i) | HP LaserJet 4000
```

## Slide 7

##### Telnet

Allows accessing the terminal of another machine remotely Legacy protocol superseded by SSH Still widely used globally

7

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Telnet
Allows accessing the terminal
of another machine remotely
Legacy protocol superseded
by SSH
Still widely used globally
Shodan Report iif
// GENERAL
® Countries
China 194 311
Brazil 25,148
Canada
Argentina
United States 5,253
black hat
2026 7
```

## Slide 8

##### Samba

Open-source implementation of SMB and Active Directory Exposes the RPC interface of common services Released in 1992

8

## Slide 9

##### RCE in TelnetD

Reported by Carlos Cortes Alvarez on January 19th, 2026 Issued as CVE-2026-24061

CVSS 9.8

Stayed undetected since 2015

<u>https://www.safebreach.com/blog/safebreach-labs-root-cause-analysis-and-poc-exploit-for-cve-2026-24061/</u>

9

## Slide 10

##### Root Cause Analysis

### Telnetd allows unauthenticated clients to set its environment variables

10

## Slide 11

##### Root Cause Analysis

### The spawned shell will inherit the new environment variables

11

## Slide 12

### Root Cause Analysis Telnetd doesn’t perform the authentication itself

12

## Slide 13

##### Root Cause Analysis

Telnetd executes login with a format string In 2015 it was updated

```
- PATH_LOGIN " -p -h %h %?u{-f %u}"
+ PATH_LOGIN " -p -h %h %?u{-f %u}{%U}"
```

13

## Slide 14

##### Root Cause Analysis

```
PATH_LOGIN " -p -h %h %?u{-f %u}{%U}"
```

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

14

## Slide 15

##### Root Cause Analysis

```
PATH_LOGIN " -p-h %h %?u{-f %u}{%U}"
```

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

15

## Slide 16

##### Root Cause Analysis

`PATH_LOGIN " -p -h %h %?u{-f %u}{%U}"` %h = The remote hostname of the connecting client

16

## Slide 17

##### Root Cause Analysis

`PATH_LOGIN " -p -h %h` `%?u` `{-f %u}{%U}"` %h = The remote hostname of the connecting client %?u = Is the variable “user_name” non-empty?

17

## Slide 18

##### Root Cause Analysis

`PATH_LOGIN " -p -h %h %?u{` `-f %u}` `{%U}"` %h = The remote hostname of the connecting client %?u = Is the variable “user_name” non-empty? {-f %u} = True block

18

## Slide 19

##### Root Cause Analysis

`PATH_LOGIN " -p -h %h %?u{-f %u` `}{%U}` `"` %h = The remote hostname of the connecting client %?u = Is the variable “user_name” non-empty? {-f %u} = True block

{%U} = False block

19

## Slide 20

##### Root Cause Analysis

By default, “user_name” is not set %U is mapped to $USER Command line can be simplified as follows `/usr/bin/login -p -h remote_hostname $USER`

20

## Slide 21

Root Cause Analysis The client controls the environment variables of telnetd $USER is not sanitized before formatting it! Arbitrary parameters can be injected to the command line

21

## Slide 22

##### Root Cause Analysis

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

22

## Slide 23

##### Root Cause Analysis

### The -f parameter can be injected to skip authentication Any username can be set

23

## Slide 24

Security Patch Parameters cannot be set before the username

```
-  PATH_LOGIN " -p -h %h %?u{-f %u}{%U}"
+  PATH_LOGIN " -p -h %h %?u{-f-- %u}{--%U}"
```

24

## Slide 25

### Security Patch Variables are sanitized for shell metachars

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

25

## Slide 26

##### What else stayed hidden?

26

## Slide 27

##### Manipulating Envars in TelnetD

LD_PRELOAD forces the linker to load a library when the process is initialized

27

## Slide 28

### Manipulating Envars in TelnetD TelnetD removes malicious envars before executing login Security fix from 1995!

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

28

## Slide 29

#### Hijack Execution Flow Modifying $PATH will launch login from another directory

/tmp /usr/local/bin /usr/local/bin /usr/bin

29

## Slide 30

##### Hijack Execution Flow

PATH_LOGIN is compiled as a full path No other process is launched by telnetd

/usr/local/bin
/tmp /usr/local/bin /usr/local/bin /usr/bin

30

## Slide 31

##### Envars References

Digging through the code might reveal unique envars Telnetd retrieves only $USER Envars set in telnetd will be inherited by login

31

## Slide 32

##### Envars References

login references $CREDENTIALS_DIRECTORY Secure mechanism to supply credentials to services

32

## Slide 33

##### $CREDENTIALS_DIRECTORY

33

## Slide 34

##### $CREDENTIALS_DIRECTORY

unit file:

…
[Service]
ExecStart=/usr/bin/myservice.sh
=
LoadCredential secrets_file :/etc/my_creds.txt
…

34

## Slide 35

##### $CREDENTIALS_DIRECTORY

#### login uses systemd credentials mechanism

does it
Is is the
is it a  contain  skip
$CREDENTIALS_DIRECTORY data
the file  auth
directory?
set? “yes”?
login.noauth?

35

## Slide 36

##### $CREDENTIALS_DIRECTORY

#### login.noauth is even documented

36

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
SCREDENTIALS_DIRECTORY
login.noauth is even documented
CREDENTIALS
login supports configuration via systemd credentials (see htt
systemd.io/CREDENTIALS/).
aoc ff
ps-//
fa J
login reads the following systemd credentials:
login.noauth (boolean)
If set, configures login to skip login authentication, similarly to the -f option.
black hat
USA
2026 36
```

## Slide 37

##### Privilege Escalation in TelnetD

37

## Slide 38

Demo #1

38

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Demo #1
weak_user@telnet-srv:~$ |
>
I
7 ®@,
e
~e
black hat
2026 38
```

## Slide 39

##### Privilege Escalation in TelnetD

Reported to GNU on February 5th, 2026 Patch was released on February 15th, 2026 $CREDENTIALS_DIRECTORY is unset before launching login CVE-2026-28372 was issued

39

## Slide 40

##### Disabling The Attack Surface

Another patch was released on March 6th, 2026

telnetd no longer accepts any envars valid names are set using --accept-env

40

## Slide 41

##### Expanding The Search

login.noauth was documented and not exploited

No complex memory corruption required Could there be more services with logical vulnerabilities?

41

## Slide 42

##### Picking The Next Target

Samba is a very common service Installed widely Developed over 30 years

42

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Picking The Next Target
Samba is a very common Shodan Report Ea==es
service // GENERAL
Installed widely @® Countries
Developed over 30 years ne nwo 5008
United States 4,296
Portugal 3,276
France 3,260
black hat
USA
2026 42
```

## Slide 43

##### Samba Inner Workings

~$ cat / etc /samba/ smb.conf
add group script = / usr / sbin / groupadd  %g
add share command = / usr /local/bin/ addshare
passwd program = /bin/passwd %u
shutdown script = / usr /local/samba/ sbin /shutdown %m %t %r %f

43

## Slide 44

##### Samba Inner Workings

~$ cat / etc /samba/ smb.conf
add group script = / usr / sbin / groupadd  %g
add share command = / usr /local/bin/ addshare
passwd program = /bin/passwd %u
shutdown script = / usr /local/samba/ sbin /shutdown %m %t %r %f

44

## Slide 45

##### Attempting Bash Injection

_spoolss_AddPrinterEx
sprintf
smbrun

45

## Slide 46

##### Attempting Bash Injection

```
addprinter_command “printer_name“ “share_name”...
```

```
printer_name=a“ | touch /tmp/pwned | echo “a
```

```
addprinter_command “a“ | touch /tmp/pwned | echo
“a“ “share_name”...
```

46

## Slide 47

##### Samba Sanitization Mechanism

smbrun
escape_shell_string
execl

47

## Slide 48

##### Samba Sanitization Mechanism

#### Non-alphanumeric chars outside of quotes are escaped

```
addprinter_command “a“ \| touch /tmp/pwned \| echo
“a“ “share_name”...
```

48

## Slide 49

49

## Slide 50

##### smbrunsecret

Executes a command and sends secret over stdin Secret isn’t passed on the command line to avoid leak escape_shell_string isn’t called!

50

## Slide 51

51

## Slide 52

##### Unauthenticated RCE #1

_samr_ValidatePassword
check_password_complexity
smbrunsecret

52

## Slide 53

##### Unauthenticated RCE #1

“check password script” includes %u ncacn_ip_tcp is used samba-dcerpcd launched independently rpc start on demand helpers = no

53

## Slide 54

##### Unauthenticated RCE #1

54

## Slide 55

Demo #2

55

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Demo #2
Attacker id. x + v | user@samba-srv: ~ x + v Victim
user@samba-srv:~$
C(impacket) C:\Users\ronb>
black hat
USA
2026 55
```

## Slide 56

56

## Slide 57

##### Unauthenticated RCE #2

```
_spoolss_EndDocPrinter
print_job_end
generic_job_submit
print_run_command
smbrun_no_sanitize
```

57

## Slide 58

##### Samba as Print Server

58

## Slide 59

##### Unauthenticated RCE #2

Printer share configured “printing” config isn’t IPRINT or CUPS “print command” includes %J

59

## Slide 60

##### Unauthenticated RCE #2

60

## Slide 61

61

## Slide 62

##### Demo #3

62

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Demo #3
Attacker [ie F) wer@sambe-sr:~ « Victim
user@samba-srv:~$
Cimpacket) C:\Users\ronb>
black hat
USA
2026 62
```

## Slide 63

Disclosure Reported to Samba on March 15th, 2026 Patch was released on May 26th, 2026 CVE-2026-4408: RCE via SAMR CVE-2026-4480: RCE via Spoolss Rated CVSS 10.0 by Samba Affected all versions over 25 years!

63

## Slide 64

##### Security Patch

Formatting engine was refactored Admins are warned to use envars instead of format strings _samr_ValidatePassword is restricted to DCs

64

## Slide 65

##### Takeaways

Issuing patches is not enough Designs and RFCs should be updated Legacy services don’t follow modern security principles

65

## Slide 66

##### Takeaways

The latest risks aren’t necessarily the greatest Legacy protocols are still being used in enterprise networks

66

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Takeaways
7 FNKID ZOEY
a
iP al
The latest risks aren't
necessarily the greatest
Legacy protocols are still 7 vi Bs .
being used in enterprise Tas
networks
PROMPT INJECTIO —
MALICIOUS IDE EXTENTIONS = j
CLOUD-MISCONFIGS USER="F ROOT;
black hat
2026 66
```

## Slide 67

##### Takeaways

## secure

67

## Slide 68

##### Conclusion

3 vulnerabilities revealed Patch led to systemic change Services can stay vulnerable for decades Some network devices don’t describe what’s installed

68

## Slide 69

# Thank you!

@RonB_Y www.linkedin.com/in/ron-by

https://github.com/SafeBreach-Labs/ForgottenButNotGone

69
