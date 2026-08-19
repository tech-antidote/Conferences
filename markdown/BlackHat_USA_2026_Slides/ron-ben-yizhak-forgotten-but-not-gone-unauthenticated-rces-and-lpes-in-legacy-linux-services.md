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
text_chars: 12136
ocr_pages: 17
has_ocr: true
redacted_secrets: 0
ocr_confidence: 89.0
ocr_unreliable_blocks: 0
vision_verified_pages_changed: 63
vision_verified_pages: 69
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T05:42:46Z"
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

## Slide 3

##### ABOUT ME

Security Research Team Lead @ SafeBreach

Published privilege escalation and code injection methods for Windows

Previous talks

- DEF CON 30-33
- DEF CON Singapore
- TyphoonCon 2026

3

## Slide 4

##### Agenda

- Common services in Linux
- Research initiator (CVE-2026-24061)
- Privilege Escalation in GNU TelnedD
- Samba Inner Workings
- Unauthenticated RCE in Samba via SAMR
- Unauthenticated RCE in Samba via Spoolss
- Takeaways

4

## Slide 5

##### When was the last time you checked what your network devices are running?

5

## Slide 6

##### How long ago you updated your printer?

6

## Slide 7

##### Telnet

- Allows accessing the terminal of another machine remotely
- Legacy protocol superseded by SSH
- Still widely used globally

Shodan Report (`telnet`) — Total: 270,235

// GENERAL

| Country | Count |
|---|---|
| China | 194,311 |
| Brazil | 25,148 |
| Canada | 9,679 |
| Argentina | 7,536 |
| United States | 5,263 |

7

## Slide 8

##### Samba

- Open-source implementation of SMB and Active Directory
- Exposes the RPC interface of common services
- Released in 1992

Diagram: a Linux server exposes four common services over RPC — SMB, Netlogon, Event log, Print Spooler.

8

## Slide 9

##### RCE in TelnetD

- Reported by Carlos Cortes Alvarez on January 19th, 2026
- Issued as CVE-2026-24061
- CVSS 9.8
- Stayed undetected since 2015

<u>https://www.safebreach.com/blog/safebreach-labs-root-cause-analysis-and-poc-exploit-for-cve-2026-24061/</u>

9

## Slide 10

##### Root Cause Analysis

### Telnetd allows unauthenticated clients to set its environment variables

Diagram: an unauthenticated client sends `ENVAR=VALUE` to `telnetd`, whose environment becomes:

```text
LANG=en_US.UTF-8
USER=john
...
ENVAR=VALUE
```

10

## Slide 11

##### Root Cause Analysis

### The spawned shell will inherit the new environment variables

Diagram: the client sends `ENVAR=VALUE` to `telnetd`, which spawns `bash`; the spawned shell inherits the environment:

```text
LANG=en_US.UTF-8
USER=john
...
ENVAR=VALUE
```

11

## Slide 12

##### Root Cause Analysis

### Telnetd doesn’t perform the authentication itself

Diagram: `/usr/sbin/telnetd` spawns `/usr/bin/login`, which handles the exchange with the client — `login` asks "Who are you?" and the client replies "user:password".

12

## Slide 13

##### Root Cause Analysis

Telnetd executes login with a format string

In 2015 it was updated

```diff
- PATH_LOGIN " -p -h %h %?u{-f %u}"
+ PATH_LOGIN " -p -h %h %?u{-f %u}{%U}"
```

The added `{%U}` is highlighted.

13

## Slide 14

##### Root Cause Analysis

```text
PATH_LOGIN " -p -h %h %?u{-f %u}{%U}"
```

```text
~$ /usr/bin/login --help

Usage:
 login [-p] [-h <host>] [-H] [[-f] <username>]

Begin a session on the system.

Options:
 -p             do not destroy the environment
 -f             skip a login authentication
 -h <host>      hostname to be used for utmp logging
 -H             suppress hostname in the login prompt
    --help      display this help
 -V, --version  display version
```

`-p` in the format string and its description "do not destroy the environment" are highlighted.

14

## Slide 15

##### Root Cause Analysis

```text
PATH_LOGIN " -p -h %h %?u{-f %u}{%U}"
```

```text
~$ /usr/bin/login --help

Usage:
 login [-p] [-h <host>] [-H] [[-f] <username>]

Begin a session on the system.

Options:
 -p             do not destroy the environment
 -f             skip a login authentication
 -h <host>      hostname to be used for utmp logging
 -H             suppress hostname in the login prompt
    --help      display this help
 -V, --version  display version
```

`-h` in the format string and its description "hostname to be used for utmp logging" are highlighted.

15

## Slide 16

##### Root Cause Analysis

```text
PATH_LOGIN " -p -h %h %?u{-f %u}{%U}"
```

- `%h` = The remote hostname of the connecting client

16

## Slide 17

##### Root Cause Analysis

```text
PATH_LOGIN " -p -h %h %?u{-f %u}{%U}"
```

- `%h` = The remote hostname of the connecting client
- `%?u` = Is the variable “user_name” non-empty?

17

## Slide 18

##### Root Cause Analysis

```text
PATH_LOGIN " -p -h %h %?u{-f %u}{%U}"
```

- `%h` = The remote hostname of the connecting client
- `%?u` = Is the variable “user_name” non-empty?
- `{-f %u}` = True block

18

## Slide 19

##### Root Cause Analysis

```text
PATH_LOGIN " -p -h %h %?u{-f %u}{%U}"
```

- `%h` = The remote hostname of the connecting client
- `%?u` = Is the variable “user_name” non-empty?
- `{-f %u}` = True block
- `{%U}` = False block

19

## Slide 20

##### Root Cause Analysis

- By default, “user_name” is not set
- %U is mapped to $USER
- Command line can be simplified as follows

```text
/usr/bin/login -p -h remote_hostname $USER
```

20

## Slide 21

##### Root Cause Analysis

- The client controls the environment variables of telnetd
- $USER is not sanitized before formatting it!
- Arbitrary parameters can be injected to the command line

Diagram: the client sends `USER=FOOBAR` to `telnetd`, which spawns `/usr/bin/login -p -h %h FOOBAR` — the injected `FOOBAR` becomes a command-line argument.

21

## Slide 22

##### Root Cause Analysis

```text
~$ /usr/bin/login --help

Usage:
 login [-p] [-h <host>] [-H] [[-f] <username>]

Begin a session on the system.

Options:
 -p             do not destroy the environment
 -f             skip a login authentication
 -h <host>      hostname to be used for utmp logging
 -H             suppress hostname in the login prompt
    --help      display this help
 -V, --version  display version
```

`-f` and its description "skip a login authentication" are highlighted.

22

## Slide 23

##### Root Cause Analysis

- The -f parameter can be injected to skip authentication
- Any username can be set

Diagram: the client sends `USER=-f root` to `telnetd`, which spawns `/usr/bin/login -p -h %h -f root` — the injected `-f root` skips authentication and logs in as root.

23

## Slide 24

##### Security Patch

Parameters cannot be set before the username

```diff
- PATH_LOGIN " -p -h %h %?u{-f %u}{%U}"
+ PATH_LOGIN " -p -h %h %?u{-f -- %u}{-- %U}"
```

The added `--` separators are highlighted.

24

## Slide 25

##### Security Patch

Variables are sanitized for shell metachars

Flowchart: each of `remote_hostname`, `user_name` and `$USER` enters a decision — does it contain any of these characters?

```text
\t\n-
!”#$&'()*;<=>?[\
\^`{|}~
```

- no → formatting allowed
- yes → Formatting denied

25

## Slide 26

##### What else stayed hidden?

26

## Slide 27

##### Manipulating Envars in TelnetD

LD_PRELOAD forces the linker to load a library when the process is initialized

```text
~$ LD_PRELOAD=/tmp/injected.so /usr/bin/login
```

Diagram: `login` loads its libraries — `injected.so` (the attacker's, highlighted), `libc.so`, `libcap.so`, `libpam.so`.

27

## Slide 28

##### Manipulating Envars in TelnetD

TelnetD removes malicious envars before executing login

Security fix from 1995!

Flowchart: each variable in `environ` enters a decision — does its name contain any of these?

```text
LD_
_RLD_
LIBPATH=
IFS=
```

- no → keep
- yes → scrub

28

## Slide 29

##### Hijack Execution Flow

Modifying $PATH will launch login from another directory

Diagram: the $PATH search chain is `/tmp` (attacker-prepended) → `/usr/local/bin` → `/usr/local/bin` → `/usr/bin`.

29

## Slide 30

##### Hijack Execution Flow

PATH_LOGIN is compiled as a full path

No other process is launched by telnetd

Diagram: the $PATH search chain (bottom) is `/tmp` (attacker-prepended) → `/usr/local/bin` → `/usr/local/bin` → `/usr/bin`. Above it, a `/usr/local/bin` box has an arrow that skips over the chain and points directly to `/usr/bin`, since `login` is launched by its compiled full path.

30

## Slide 31

##### Envars References

- Digging through the code might reveal unique envars
- Telnetd retrieves only $USER
- Envars set in telnetd will be inherited by login

31

## Slide 32

##### Envars References

- login references $CREDENTIALS_DIRECTORY
- Secure mechanism to supply credentials to services

32

## Slide 33

##### $CREDENTIALS_DIRECTORY

Diagram — two ways to pass a secret to a service:

- Insecure (red ✗): `systemd` passes the secret to the `service` directly as an environment variable, `SECRET=****`.
- Secure (green ✓): `systemd` writes the secret to a file `/run/credentials/my.service/secret` and passes the `service` only `CRED_DIR=/run/credentials/my.service`.

33

## Slide 34

##### $CREDENTIALS_DIRECTORY

unit file:

```text
…
[Service]
ExecStart=/usr/bin/myservice.sh
LoadCredential=secrets_file:/etc/my_creds.txt
…
```

Diagram: the credentials directory `/run/credentials/my.service` contains a file `secrets_file` (contents `****`) with permissions `-r-------- root root`.

34

## Slide 35

##### $CREDENTIALS_DIRECTORY

login uses systemd credentials mechanism

Flowchart — each check must pass to reach the next; if all pass, login skips authentication:

1. Is $CREDENTIALS_DIRECTORY set?
2. is it a directory?
3. does it contain the file login.noauth?
4. is the data “yes”?
5. → skip auth

35

## Slide 36

##### $CREDENTIALS_DIRECTORY

login.noauth is even documented

Documentation screenshot:

> **CREDENTIALS**
>
> login supports configuration via systemd credentials (see https://systemd.io/CREDENTIALS/).
> login reads the following systemd credentials:
>
> **login.noauth (boolean)**
> If set, configures login to skip login authentication, similarly to the -f option.

36

## Slide 37

##### Privilege Escalation in TelnetD

Attack chain (numbered steps in the diagram):

1. write “yes” — the attacker writes `yes` to the file `/tmp/login.noauth`.
2. `USER=root, CRED_DIR=/tmp` — the attacker sends these environment variables to `telnetd`; the `telnetd` window now holds `CRED_DIR=/tmp` and `USER=root`.
3. `usr/bin/login -p -h %h root` — `telnetd` spawns login with these arguments (the login window inherits `CRED_DIR=/tmp`).
4. read — login reads `/tmp/login.noauth`.
5. skip auth and spawn root shell — login skips authentication and spawns a root shell.

37

## Slide 38

##### Demo #1

```text
weak_user@telnet-srv:~$
```

38

## Slide 39

##### Privilege Escalation in TelnetD

- Reported to GNU on February 5th, 2026
- Patch was released on February 15th, 2026
- $CREDENTIALS_DIRECTORY is unset before launching login
- CVE-2026-28372 was issued

39

## Slide 40

##### Disabling The Attack Surface

- Another patch was released on March 6th, 2026
- telnetd no longer accepts any envars
- valid names are set using --accept-env

Illustration: a "Flex Tape" meme — GNU covering a "30 YEARS OF VULNERABILITIES" leak with "--ACCEPT-ENV".

40

## Slide 41

##### Expanding The Search

- login.noauth was documented and not exploited
- No complex memory corruption required
- Could there be more services with logical vulnerabilities?

41

## Slide 42

##### Picking The Next Target

- Samba is a very common service
- Installed widely
- Developed over 30 years

Shodan Report (`product:"Samba"`) — Total: 65,767

// GENERAL

| Country | Count |
|---|---|
| Pakistan | 24,401 |
| Taiwan | 5,093 |
| United States | 4,296 |
| Portugal | 3,276 |
| France | 3,260 |

42

## Slide 43

##### Samba Inner Workings

```text
~$ cat /etc/samba/smb.conf
add group script = /usr/sbin/groupadd %g
add share command = /usr/local/bin/addshare
passwd program = /bin/passwd %u
shutdown script = /usr/local/samba/sbin/shutdown %m %t %r %f
```

43

## Slide 44

##### Samba Inner Workings

```text
~$ cat /etc/samba/smb.conf
add group script = /usr/sbin/groupadd %g
add share command = /usr/local/bin/addshare
passwd program = /bin/passwd %u
shutdown script = /usr/local/samba/sbin/shutdown %m %t %r %f
```

The line `add share command = /usr/local/bin/addshare` is highlighted.

44

## Slide 45

##### Attempting Bash Injection

Call flow: `_spoolss_AddPrinterEx` → `sprintf` → `smbrun`

45

## Slide 46

##### Attempting Bash Injection

```text
addprinter_command “printer_name“ “share_name”...
```

+

```text
printer_name=a“ | touch /tmp/pwned | echo “a
```

=

```text
addprinter_command “a“ | touch /tmp/pwned | echo “a“ “share_name”...
```

46

## Slide 47

##### Samba Sanitization Mechanism

Call flow: `smbrun` → `escape_shell_string` → `execl`

47

## Slide 48

##### Samba Sanitization Mechanism

Non-alphanumeric chars outside of quotes are escaped

```text
addprinter_command “a“ \| touch /tmp/pwned \| echo “a“ “share_name”...
```

48

## Slide 49

Photo: a sign reading "smbrunsecret".

49

## Slide 50

##### smbrunsecret

- Executes a command and sends secret over stdin
- Secret isn’t passed on the command line to avoid leak
- escape_shell_string isn’t called!

Diagram: `smbd` spawns `/bin/sh -c crackcheck` and sends the `secret` to it over stdin through a pipe (not on the command line).

50

## Slide 51

51

## Slide 52

##### Unauthenticated RCE #1

Call flow: `_samr_ValidatePassword` → `check_password_complexity` → `smbrunsecret`

52

## Slide 53

##### Unauthenticated RCE #1

- “check password script” includes %u
- ncacn_ip_tcp is used
- samba-dcerpcd launched independently
- rpc start on demand helpers = no

53

## Slide 54

##### Unauthenticated RCE #1

Attack diagram:

- The attacker calls `SamrValidatePassword` with `UserAccountName=“| touch /tmp/pwned”` (the `| touch /tmp/pwned` is the injected payload) against `samba-dcerpcd`.
- `samba-dcerpcd` executes `/bin/sh -c “crackcheck | touch /tmp/pwned”`.

`/etc/samba/smb.conf`:

```text
[global]
    check password script = crackcheck %u
    rpc start on demand helpers = no
```

`%u` in the config is replaced by the attacker-controlled `UserAccountName`.

54

## Slide 55

##### Demo #2

Attacker (Windows cmd):

```text
(impacket) C:\Users\ronb>
```

Victim (`user@samba-srv`):

```text
user@samba-srv:~$
```

55

## Slide 56

Photo: a crate labeled "smbrun_no_sanitize".

56

## Slide 57

##### Unauthenticated RCE #2

Call flow: `_spoolss_EndDocPrinter` → `print_job_end` → `generic_job_submit` → `print_run_command` → `smbrun_no_sanitize`

57

## Slide 58

##### Samba as Print Server

Diagram: the attacker sends a document to `spoolss`, which passes it to `Samba`. Samba dispatches to one of three print backends — `generic`, `iprint`, or `cups` — each of which sends the job to the printer.

58

## Slide 59

##### Unauthenticated RCE #2

- Printer share configured
- “printing” config isn’t IPRINT or CUPS
- “print command” includes %J

59

## Slide 60

##### Unauthenticated RCE #2

Attack diagram:

- The attacker calls `RpcEndDocPrinter` with `pDocName=“| touch /tmp/pwned”` (the `| touch /tmp/pwned` is the injected payload) to `smbd`.
- `smbd` executes `/bin/sh -c “echo Printing | touch /tmp/pwned >> /tmp/print.log”`.

`/etc/samba/smb.conf`:

```text
[global]
    printing = BSD
    print command = echo Printing %J >> /tmp/print.log
[Printer]
    path = /var/tmp/
    printable = yes
```

`%J` in `print command` is replaced by the attacker-controlled `pDocName`.

60

## Slide 61

Photo: a crate labeled "smbrun_no_sanitize".

61

## Slide 62

##### Demo #3

Attacker (Windows cmd):

```text
(impacket) C:\Users\ronb>
```

Victim (`user@samba-srv`):

```text
user@samba-srv:~$
```

62

## Slide 63

##### Disclosure

- Reported to Samba on March 15th, 2026
- Patch was released on May 26th, 2026
- CVE-2026-4408: RCE via SAMR
- CVE-2026-4480: RCE via Spoolss
- Rated CVSS 10.0 by Samba
- Affected all versions over 25 years!

63

## Slide 64

##### Security Patch

- Formatting engine was refactored
- Admins are warned to use envars instead of format strings
- _samr_ValidatePassword is restricted to DCs

64

## Slide 65

##### Takeaways

- Issuing patches is not enough
- Designs and RFCs should be updated
- Legacy services don’t follow modern security principles

Photo: a stack of printed RFCs beside a vintage IBM terminal — RFC 793 (Transmission Control Protocol, Sept 1981), RFC 768 (User Datagram Protocol, Aug 1980), RFC 854 (Telnet Protocol Specification, May 1983), RFC 821 (Simple Mail Transfer Protocol, Aug 1982), RFC 1034 (Domain Names - Concepts and Facilities, Nov 1987).

65

## Slide 66

##### Takeaways

- The latest risks aren’t necessarily the greatest
- Legacy protocols are still being used in enterprise networks

Illustration: the "Olympic shooters" meme — the heavily-equipped shooter captioned "PROMPT INJECTIONS / MALICIOUS IDE EXTENTIONS / CLOUD MISCONFIGS", the minimal shooter captioned "USER='-F ROOT'".

66

## Slide 67

##### Takeaways

A GitHub "Star 123k" button ≠ secure

67

## Slide 68

##### Conclusion

- 3 vulnerabilities revealed
- Patch led to systemic change
- Services can stay vulnerable for decades
- Some network devices don’t describe what’s installed

68

## Slide 69

# Thank you!

@RonB_Y

www.linkedin.com/in/ron-by

SafeBreach

https://github.com/SafeBreach-Labs/ForgottenButNotGone

69

