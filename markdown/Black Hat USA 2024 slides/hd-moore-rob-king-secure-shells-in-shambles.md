---
title: "Secure Shells in Shambles"
speakers: ["HD Moore", "Rob King"]
conference: "Black Hat"
conference_full: "Black Hat USA 2024"
edition: "USA"
year: 2024
source_pdf: "Black Hat USA 2024 slides/HD Moore & Rob King_Secure Shells in Shambles.pdf"
pages: 97
sha256: "7d63bb06d0b8a1692297c515acccb3c34bbca06c988908a06683024c34329435"
text_chars: 43296
ocr_pages: 24
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:32:44Z"
---
# Secure Shells in Shambles

**Speakers:** HD Moore, Rob King  
**Conference:** Black Hat USA 2024  
**Source:** `Black Hat USA 2024 slides/HD Moore & Rob King_Secure Shells in Shambles.pdf` (97 pages)


## Slide 1

BLACK HAT BRIEFINGS

# **Secure Shells in Shambles**

HD MOORE     |     ROB KING     |     AUGUST 7, 2024

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
USA 2024
(F
c
CUNZ=ro
NesesAcH
L BLACK HAT BRIEFINGS J
Secure Shells
in Shambles
HDMOORE | ROBKING | AUGUST7,2024
```

## Slide 2

### **Agenda**

###### **This is a talk about the evolution of the Secure Shell (SSH)**

- → An overview of the SSH ecosystem

- → What’s changed & what hasn’t

- → New & interesting attacks

- → OpenSSH fragmentation

- → Introducing **SSHamble**

- → Defending SSH

2

## Slide 3

### **In the beginning was SSH**

###### **Tatu Ylönen created SSH v1 in 1995 as freeware**

→
Continued development as the proprietary SSH.com
→
Björn Grönvall forked Ylönen's free SSH v1.2.12 as OSSH
→
OpenBSD  forked  OSSH into OpenSSH in 1999
1995 1996 1997 1998 1999 2000 2001 2002 2003 2004 2005 2006 2024
SSH
OSSH
OpenSSH
OpenSSH Portable
PKIX-SSH
Dropbear

3

## Slide 4

### **SSH is mostly OpenSSH & Dropbear**

OpenSSH 20,200,340
Dropbear sshd 5,482,314
Linksys WRT45G modified dropbear sshd 46,214
lancom sshd 43,574
Not-OpenSSH/Dropbear are important
SCS sshd 8,215 Firewall, networking, & storage
→ Cisco, NetScreen, Adtran, ComWare, Lancom
HP Integrated Lights-Out mpSSH 7,493
OT/ICS equipment
WeOnlyDo sshd 6,458
→
Siemens, NetPower, Mocana, CradlePoint, Digi
ZyXEL ZyWALL sshd 3,417
Sensitive applications
NetScreen shhd 1,854 → MOVEIT, CrushFTP, GlobalScape,JSCAPE
→
BitVis, GoAnywhere, ConfD
DrayTek Vigor 2820n ADSL router sshd 1,848
→
Gerrit, Forgejo, Gitlab
CoreFTP sshd 1,700

https://www.shodan.io/search/facet?query=shodan.module%3A%22ssh%22&facet=product

4

## Slide 5

### **Other implementations**

###### **Standalone product examples**

###### **SSH library examples**

- → PKIX-SSH — popular in networking equipment, forked from OpenSSH

- → WolfSSH — small implementation popular in embedded systems

- → lsh — an old implementation that predates OpenSSH Portable

- → libssh — open source, bindings for lots of languages

- → Go x/crypto/ssh — a pure Go implementation

- → Apache MINA — a Java implementation

- → Paramiko — SSH in Python

5

## Slide 6

### **SSH is everywhere**

- → Second-most common remote admin service behind HTTP

- → Enabled by default in clouds

- → Part of every major OS

- → Embedded & servers

- → Even mobile!

Mostly SSH

https://exposure.shodan.io/#/US

6

## Slide 7

Clear
Text
Authentication
Channels
Encrypted
Transport

7

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
[ sss cxsent | TCP ) f SSH-TRANS | [ SSH-AUTH | SSH-CONN | [ ssu-senven | ( runz=ro
v —
Verify Kex
cc
Key Exchange ,
SSH2_MSG_SERVICE_REQUEST
SSH2_MSG SERVICE ACCEPT
SSH2_MSG_USERAUTH_REQUEST (user,svc,method, data) <j
Authentication
Verify Auth
CF a
SSH2_MSG_USERAUTH_SUCCESS Channels
Encrypted Create Larval Session
Transport CFE
Send “pty-req”
Allocate PTY
Cc,
Send “env” '
Configure Session
Ca
Open Channel “shell”
Execute Subprocess
Channel Read/Write 1
Channel Close 7
```

## Slide 8

### **SSH provides transport & authentication**

**Version exchange & kex init in the clear**

**Key exchange to negotiate secure transport**

**Authentication using one or more methods**

- → Version: SSH-2.0 OpenSSH-9.8p1 deb13u3

- → Ciphers, MACs, Compressions, Languages, etc

- → Diffie-Hellman & friends pinned with server host key(s)

- → Algorithm picked by kex init agreement

Similar to TLS

- → Passwords, public keys, kerberos, & more

- → PK uses the session ID for proof signing

8

## Slide 9

### **Channels, subsystems, & shells, oh my!**

###### **SSH multiplexes multiple channels (concurrently)**

→ Interactive shells
→ Command execution
→ File transfer (SCP, SFTP)
→
TCP forwarding
→
Unix socket forwarding
→
X11 display forwarding
→
Agent forwarding

SSH connections
$ ls -l bash
Channels
puts “hello!” vim foo.rb
localhost: 4242 localhost: 4242
xclock

9

## Slide 10

### **SSH is the other secure transport**

**An alternative to TLS, but not exactly the same**

**Compliance schemes gloss over SSH**

- → Server key management can be, but usually isn’t CA-based

- → Authentication is a core stage of the protocol

- → Multiplexer & session commands are unique

   - → Vendors point to strong cipher/mac + authentication similar to TLS

   - → SSH specifics are often missing, assume best practices

   - → Key management is the biggest gap

- → SSH  uses the <u>f</u> i <u>rst</u> algorithm sent

- by the client & supported by the server

10

## Slide 11

## **What’s New?**

11

## Slide 12

### **More protocol extensions**

ping Ping & pong server-sig-algs Support for more algorithms publickey-hostbound-v00 Host-bound public keys tun Layer 2 & 3 tunneling hostkeys/hostkeys-prove Host key rotation aes128−gcm,hmac-sha1−etm, … New cipher, kex, & MACs

12

## Slide 13

### **SSHFP: Verify server host keys via DNS**

**DNS record format defined in RFC 4255**

- → Key Algorithm + Hash Type + Fingerprint

   - 4 [ED25519] / 2 [SHA256] / 0A2B3C [SHA256 hash]

**Low adoption as of late 2021***

      - → Enabled for 1 in every 10,000 domains tested

      - → Only 50% use DNSSEC

- → Enforce client-side with -o VerifyHostKeyDNS=yes

- → Enumerate via dig or ssh-keyscan

   - dig -t SSH example.com

   - ssh-keyscan -D example.com

_* See “Neef, S., Wisiol, N. (2022). Oh SSH-it, What’s  My Fingerprint? A Large-Scale Analysis of SSH Host Key Fingerprint Verification Records in the DNS”_

13

## Slide 14

### **MFA for SSH: Interactive OTP**

###### **Traditional SSH MFA is via PAM plugins**

**After Password**

$ **ssh dev@192.168.67.2** (dev@192.168.67.2) Password: (dev@192.168.67.2) Verification code:

**Before Password**

$ **ssh dev@192.168.67.3** https://api-a bc1234.duosecurity.com /frame/portal/v4/enroll?code=012…

- → Uses **challenge-response** or **keyboard-interactive*** mode

- → Google Auth, Duo Security, QQ.com, Qomolo, & more

- **keyboard-interactive** usually just  means **password** ,

- but it is also used for interactive OTP.

14

## Slide 15

### **MFA for SSH: FIDO2 resident keys**

**Use a token-aware SSH agent**

- → https://github.com/FiloSottile/yubikey-agent

- → https://github.com/maxgoedjen/secretive

**Use the new “sk” key types**

- → ssh-keygen -t ed25519-sk -O resident -O verify-required

- → ssh-keygen -K

###### **SSH Server (optional)**

- → PubkeyAuthOptions verify-required

15

## Slide 16

### **Centralized SSH authentication**

**Certificates with short-expiration signed SSH keys**

###### **Projects & products**

- → Authenticate to an IDP, get a signed SSH key

- → Use the signed key like a normal private key

- → The gold standard for managed SSH

- → Opera SSH Key Authority (SKA)

- → HashiCorp Vault SSH Certificate Secret Engine

- → Tectia UKM, Teleport, UserFi, SpanKey, Delinea, & more!

16

## Slide 17

### **Useful pre-authentication banners**

17

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
7
Useful pre-authentication banners
(G runz=ra
6Ue1N SRd$oS JWI qC6UeiNATSSR
ndqgC6 NATBSR w32T2 UcndgC6Ue1NA
xUcnd = UelN $oSlu JWJ cnd 6U
2jWJxU dC TBSRd$ WJx
w32T2jW xUc e1N T8S 272
$o51w32 2jW dqC6Ue1NA Sl
8SR $051w32 xUcndqC6U Rd$
1NA BSRd$oS T2jH = cndq ATS
C6U NATBSR 1u3 JxU Uel
Ucndq UeiNA SRd$oS
jWJxU qC6U-NATESR
2T2jHJ cndqC6U
51w32T WJxUcnd
Processor board ID FHK13@562CK with 118784K/12288K bytes of memory.
Cisco I0S Software, Version 12.4(15)T7, RELEASE SOFTWARE (fc2)
Please Disconnect if you are not an authorized user
2
banner login “Cisco Configuration Assistant. Version: 3.8. Tue Jan 25 17:34:18 GMT 28117
2
banner login “Cisco Configuration Assistant. Version: 3.8. Wed Dec 22 15:58:48 EST 2617
2
banner login “Cisco Configuration Assistant. Version: 3
2
Hed Sep @7 11:37:42 EST 20117
banner login “Cisco Configuration Assistant. Version: 3.2 (3). Fri Aug 31 13:28:10 EDT 22187
2
banner login “Cisco Configuration Assistant. Version: 3,2 (3). Mon Jul @5 01:32:52 EDT 2@21~
2
banner login “Cisco Configuration Assistant. Version: 3.2 (3). Mon Nov 11 16:85:89 EST 2@13*
2
banner login “Cisco Configuration Assistant. Version: 3.2 (3). Sat May 14 18:88:84 ACT 20167
2
banner login “Cisco Configuration Assistant. Version: 3.2 (3). Sun Dec 23 15:46:38 EST 22187
2
banner login “Cisco Configuration Assistant. Version: 3.2 (3). Tue Sep 1@ 10:59:28 ACT 22197
2
banner login “Cisco Configuration Assistant. Version: 3.2 (3). Wed Aug 31 10:17:41 EST 22167
2
banner login “Cisco Configuration Assistant. Version: 3
Fri May @4 12:54:39 EST 20127
banner login “Cisco Configuration Assistant. Version: 3.2. Wed Feb @1 19:27:87 GST 26127
2
Copyright 2823 BlueCat Networks (USA) Inc. and its affiliate--
Server Version 9.5.8-644.GA.bcen
Y
2
MRV OptiSwitch 686 version 1_1_9B
2
MessageWay SFTP Interface Version 6.1
Z
Microsoft Windows [Version 18.8.19845.2965)]
3
Miramar SFTP Gateway
Version 3.5.1
2
NetBSD 7.1.2 (GENERIC. 2818831516112)
Welcome to OpenVMS (TM) VAX Operating System, Version V7.3
Avi Cloud Controller
Avi Networks software, Copyright (C) 2819-2017 by Avi Networks, Inc
All rights reserved.
Version: 21,1,1
Date: 2021-@8-11 17:88:44 UTC
Build 9845
Management : 18.1.1.5/24 uP
Gateway: 18.1.1.1 DOWN
2
EpiSensor Gateway
SKU; NGR-38-3
OS Version; V@2.08
Support: http://episensor .com/helpdesk
2
Policy Manager CLI v6.12(@),
Copyright © 2823, Hewlett Packard Enterprise Development LP.
Software Version : 6.12.8.388732
16.18.2.79
: CLABV
Management IP Address
System Model
22 ILI IIL IIIS LIL ILLIA ILL ISIS I III IA
2
x**HOME FIREWALL LAB TEST xxx
current version 82 at 9:3@am
2
Server Version
Server Build
Serial Number
Network Interface (eth@) MAC
HA/Management Interface (eth1) MAC
Hostname PAG-JBCBN2613-@1H
Type ATNS1@C
Version
Site Name CIREBON
Region West Java
Ring West Java 6
Tower ID JAW-JB-CBN-2613
(8.8)
:(8.8.1.28)
:(5254@@C9SA2E)
:(€52:54:@8:C9:SA:2E)
:(52:54:88:C9:SA:2E)
VRP (R) software, Version 8.21@ (ATN 91@C-G V8aa
```

## Slide 18

### **SSH key types, exchanges, extensions**

18

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
SSH key types, exchanges, extensions (G runz=ro
"publ ickey-hostbound@openssh.com” |
“sntrup761x25519-sha512@openssh.com”,
webauthn-sk-ecdsa-sha2-nistp256@openss
"“ext-info-s",
“ping@openssh.com": "8",
```

## Slide 19

### **OpenSSH’s new PerSourcePenalties**

###### **PerSourcePenalties**

_Controls penalties for various conditions that may represent attacks on sshd(8). If a penalty is_ **“** _enforced against a client then its source address and any others in the same network, as defined by PerSourceNetBlockSize, will be refused connection for a period._

_A penalty doesn't affect concurrent connections in progress, but multiple penalties from the same source from concurrent connections will accumulate up to a maximum. Conversely, penalties are not applied until a minimum threshold time has been accumulated._

_Penalties are enabled by default with the default settings listed below but may disabled using the no keyword. The defaults may be overridden by specifying one or more of the keywords below, separated by whitespace. All keywords accept arguments, e.g. "crash:2m"._ **”**

19

## Slide 20

### **SSH keys as public identities**

→ Public keys used to being mostly private → GitHub & Launchpad changed that

20

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
20
SSH keys as public identities (G runz=ro
> Public keys used to being mostly private
> GitHub & Launchpad changed that
7 ~
Import SSH key
Import SSH identity: from {ub a
from Launchpad SSH keys from GitHub or
GitHub Usernan:: ie
Enter your GitHub username.
[ Done |
[ Cancel ]
\ y
```

## Slide 21

21

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
(G runz=ra
[ ssh whoami.filippo.io | PPS SSS SSS SSS SS SSS ap
_0/ Hello HD Moore!
Did you know that ssh sends all your public keys to any server
it tries to authenticate to?
We matched them to the keys of your GitHub account,
@hdm, which are available via the GraphQL API
and at https://github.com/hdm. keys
-- Filippo (https://filippo.io)
P.S. The source of this server is at
https://github.com/FiloSottile/whoami.filippo.io
```

## Slide 22

### **SFTP as a** **_de facto_ standard for MFT**

###### **Commercial MFT products support SCP/SFTP**

- → Many are based on existing third-party SSH libraries

- → Axway, GlobalScape, CuteFTP, Cerberus, Bitvise

- → SolarWinds, JSCAPE, FileZilla, Kiteworks, WS_FTP

22

## Slide 23

### **Return of the terminal**

###### **Libraries for Go & Rust have created a TUI renaissance**

- → Pretty interfaces delivered right to your screen via SSH

- → Treat SSH almost like TLS with optional authentication

**SSH libraries are used to power source code forges**

- → Go-based GOGS, Gitea, Forgejo, & soft-serve

- → Apache Mina supports Gerrit

- → Azure DevOps Server (VS TFS)

23

## Slide 24

### **$ ssh starwarstel.net**

24

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
24
$ ssh starwarstel.net
Va
aa
=
(G runz=ro
```

## Slide 25

### **$ ssh user@synchronet**

https://www.synchro.net/sbbslist.html

25

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
25
$ ssh user@synchronet (G runz=ro
a a a Distortion
ce | ee | SE
cee | mmm 2
ce | ee
CS a ee es Ee
CS Ea ea 8 8 ee
ae ES 2 > oe
: i 3 cS
: | a
: | om
| I
= f
Ea Lk a Login menu:
=
= Log in
ma. a: | New user
sie Guest account
Retrieve password
Email the sysop
= Page the sysop
= Beaverton, Oregon, USA Disconnect
Sat Jul 13 2024 12:03 am PDT
httos://www.synchro.net/sbbslist.html
```

## Slide 26

### **$ ssh terminal.shop**

26

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
$ ssh terminal.shop 2 runz=ro
(- a
terminal s shop a about f fag c cart $ @
[object Object] segfault
dark mode
404 $22
A sa UY yeet bl | at
from a natural fault in the coffee
cherry that causes it to develop
Iné bean instead two
= llpping 1 US D
TL products +/- qty ccart q quit
Ne SJ
```

## Slide 27

## **Recent Exposures**

27

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
(G runz=ro
Recent Exposures
27
```

## Slide 28

**Terrapin Attack Breaking SSH Channel Integrity by Sequence Number Manipulation Fabian Bäumer** Research Assistant, Ruhr University Bochum

Thursday, August 8   @ 11:20am-12:00pm Islander FG, Level 0

**CVE-2023−48795**

28

## Slide 29

### **XZ Utils backdoor**

**A multi-year campaign started in 2021 and triggered in 2024**

- → “Jia Tan” persona was likely the product of a state actor

- → Nearly-perfect Nobody-But-Us backdoor in SSH

- → Backdoor targeted SSH via systemd patches

- → Limited to Debian/RHEL-based distros

**Caught at the last possible moment by Andres Freund**

- → Noticed that sshd was using more CPU than it should

- → Backdoor made it into rolling releases only

**CVE-2024−3094**

29

## Slide 30

### **RegreSSHion**

###### **Incredible work by the Qualys Threat Research Unit**

- → Regression of a signal re-entrance vulnerability

- → Unauthenticated remote root code execution

- → Tough to exploit due to ASLR & timing

**CVE-2024−6387**

##### **Related issue discovered by Solar Designer**

- → Specific to Red Hat builds of OpenSSH

- → Limited to the non-root privsep user

**CVE-2024−6409**

The patch was hidden in the PerSourcePenalties feature, released a month prior to the disclosure.

30

## Slide 31

### **MOVEit & IPWorks SSH**

###### **Another MOVEit vulnerability, but this time in SSH**

- → watchTowr Labs reversed the MOVEit patch for CVE-2024−3094

- → The attacker’s unauthenticated public key blob is opened as a file

- → File path supports UNC and was used for authentication

- → Root cause was the third-party IPWorks library

- → Threaded a dozen needles to bypass auth

**CVE-2024−5806**

31

## Slide 32

## **What’s the Same?**

32

## Slide 33

### **Unauthenticated information exposure**

**TCP/IP**

**Server Version**

**Kex Init Extensions**

**Server Banner**

**Authentication**

TCP window size & scaling factors can determine the OS & kernel versions.

Protocol version, implementation, & package version.

Ciphers, MACs, key exchange protocols, compression methods, & server-side extensions.

Pre-authentication “banner” can be extensive, especially with network equipment.

Authentication method list, public key testing, failed auth limits, & interactive questions & prompts.

33

## Slide 34

### **A large post-auth attack surface**

###### **Restricted shell environments are difficult to secure**

- → → Multiplexed channels PTY requests

- → Connection forwarding

- → Environment manipulation

- → Subsystems (SFTP, etc)

- → X11 forwarding

- → Client-sent signals

- → Window size changes

- → Break commands

- → Agent auth requests

34

## Slide 35

### **Default exposure to brute force attacks**

**Admins are generally left to figure it out on their own**

**Horrific amount of wasted CPU due to constant attacks**

- → Fail2Ban & PAM lockouts can help, but incomplete

   - → A real impact on embedded device performance

- → PerSourcePenalties will help, but not yet widely deployed

- → Still not as terrible as blockchains or AI

35

## Slide 36

### **Public key authentication is still weird**

**Attacker can verify public keys without the private key**

**Public key auth is flexible, but is easy to get wrong**

- → Servers reply with PK_OK for valid public keys

- → Clients then send the public key + signature

   - → Dynamic PK authentication via AuthorizedKeysCommand

   - → CA user key management & revocations are finicky

- → Leads to information leaks

36

## Slide 37

### **Host key management is error prone**

**Host key duplication is incredibly common**

###### **Host keys are rarely changed due to challenges**

- → Vendors accidentally hard-code firmware & VMs

- → Cloud providers still get this wrong with images

- → VMware hosts often set host key in gold image

- → GitHub exposed their main RSA key in 2023

- → Rotation broke automation & upset users

- → Compare to modern TLS rotations

- → CAs can help, but tricky at scale

37

## Slide 38

### **SSH is still (used as) a transport layer**

**SSH as a generic secure transport layer**

**SFTP & SCP are a popular way to move files**

**Port forwarding & traffic tunneling**

→ git, rsync, systemctl, docker, duplicati, ssh-fs

→ sftp-only shells, tons of commercial tools

→ vendor-appliances & light VPNs

38

## Slide 39

**New Meets Old** (Public Key Authentication)

39

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
(G runz=ro
New Meets Old
(Public Key Authentication)
```

## Slide 40

### **Public key authentication is two-stage**

**An SSH client can confirm if a public key is valid for a given user** → Metasploit support since 2012, but still not widely known

- → The security impact is minimal?

   - /* XXX fake reply & always send PK_OK ? */ /*

   - XXX this allows testing whether a user is allowed

   - to login: if you happen to have a valid pubkey this * message is sent. the message is NEVER sent at all

   - if a user is not allowed to login. is this an

   - issue? -markus

*/

OpenSSH Source (9.8p1)

40

## Slide 41

### **Link a user & key to a specific server**

**Servers**

###### **Public Keys**

**Usernames**

A list of IP addresses or hostnames running SSH.

A list of public keys possibly linked to the target.

A list of usernames likely used by the target.

###### **Scanners**

- → nmap

- → zmap

- → masscan

###### **Databases**

- → Shodan

- → Censys

- → Fofa.info

**BadKeys**

###### **Defaults**

- → root

- → ec2−user

- → ubuntu

###### **Specific**

- → Public key

   - “comments”

- → Common handles

- → Email prefixes

41

## Slide 42

#### **HELLO MY NAME  IS**

Jia Tan

I <3 Open Source!

$ curl https://github.com/JiaT75.keys

###### ssh-rsa

AAAAB3NzaC1yc2EAAAADAQABAAACAQDHVp3Bvg/ALC61dsGehbvoqic49D4SfoiiPURSEec3/phZdAfR1hD6QSNTHLY3QDT b0994ZwOFi05YpUM6/qwBUAbroS64/Mp55qDBlark5v83LcTq7a29VUH3Xvu7sAgdYda16a2KnmU5lhETvBfxuS+tpGin9r aSp+B+z0PIpr9EmEeQgKtgKRQBiMWMtw7jBxm5INk54SmePNDva3f4ml08/Z4JM76dJ7DBQGrLUqZGsRFOZclMb3YOE7DjP GQQ37TzGvKwLaGvRuocA8oW5zp07+uQldP2LIbt0V99eyXrgD7WLc/sdzWeefoNltcgcV/KEg9ivD02qWFDBzAKMcJuLMhq xXIo64KZuVjWRrflgKCk5wZt0XPZ30MFqbBvjhn8zG7bIQJORmn/j6QSyHewu4Rre7uGxAuzee2PPSaSQ51dKgbdn3B3Uuw N8KeIO54W1VYWip+GlG2tXHZAdJOgPPaM72OAqFQBta2MzcHi3/m2HgUNBttYhSUtaeX8myfiRcnC7APhZMOuU9rrHdti2K D6IVArtBiorZbs8iFlzUPmdYVdeFP7EtW6EWgZSLV7rN2r2+CNVJeTrX9zA+mnRjhjq4ffgRUoQikY876kY+1YiEERm7LRB MkKIzM4ZsBk7VQwImSGReyfwEht9tedU5mf5pkrbL8VSMrqQQ==

ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIFiXcmAAjTBp5kM2AUTJdAEB7DHyYuY8am8FIMROD3FG

42

## Slide 43

### **Hunting for Jia Tan across the internet**

**After the XZ backdoor was exposed, we went hunting** → Copied Jia Tan’s SSH public keys from GitHub → Scanned all of IPv4 for SSH with zmap → Created SSHamble to half-auth scan

→ Ran SSHamble on all SSH hits

**We got results!**

43

## Slide 44

44

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
> ‘cpu;— menu;jpreset x
|
up 14:16:84
—) *mem | ; disks, ;io
Total: 15.6 GiB ~~ root v32K 314 GiB -
Used: 1.25 GiB 10% — a
8% Used: 14% saseueee 43.8 GiB
Free: 86% sammmmee 278 GiB
efi 123 MiB -
10% es
Used: 9% a8 *® 11.5 MiB
Free: 91% summmmme 112 MiB
— *net;
11M
}sync pj auto zero <b eth@ mp
download
: ¥ Total:
v9.11 MiB/s (72.9 Mibps)
4 8.71 MiB/s (69.7 Mibps)
420 GiB
411 GiB
Pid:
2815
46
15849
15
86
51
1238
2782
78
17785
17874
1914
626
286
41
1
613
14
26
LI} 4
)19:41:43,
-— “proc; filter,
select J
Program:
sshamble.bin
ksoftirgd/6
btop
rcu_preempt
kworker/5:1-mm_p
ksoftirgqd/7
do-agent
sshd
kswapd@
kworker/u16;1
kworker/u16:@-ev
exim4
sshd
systemd- journal
ksoftirqd/5S
syustemd
unattended-upgr
ksoftirgd/@
ksoftirgqd/2
| alters
Command:
./sshamble.bin scan -
btop
/opt/digitalocean/bin
sshd: root@pts/@
/usr/sbin/exim4 -bd -
sshd: /usr/sbin/sshd
/1ib/systemd/systemd-
/sbin/init
/usr/bin/python3 /usr
i= 2608ms + lm
DO-Regular 2.5 GHz
CPU = TTP amen 95%
Cé 83% C4 86%
C1 83% C5 81%
C2 98% C6 92%
C3 86% C7 85%
|per-core;jreverse;) tree; < cpu lazy >;
User:
root
root
root
root
root
root
do-a
root
root
root
root
Debi
root
root
root
root
root
root
root
LAV: 7.77 7.75 7.73
MemB
601M :
@B
5.8
@B
@B
@B
+ 21M
79M...
@B
|:
GB ....
* 15M
6.9M
14M _
@B —
11M ..
18M
@B ....
@B
```

## Slide 45

### **The** **~~friends~~ shells we found along the way**

**And every single result was a false positive for Jia Tan**

**We found thousands of unauthenticated shells instead**

- → Tons of honeypots & misbehaved servers

   - → Some honeypots, but mostly real bugs

- → Reworked the tools & tried again

   - → This work led to this talk!

- → Still no Jia Tan :(

45

## Slide 46

#### **HELLO MY NAME  IS NOT**

Jia Tan

I swear! We only scan things!

###### **Dear Law Enforcement,**

- → Our scans resulted in Jia’s public key hash & our IP is in everyone’s logs

- → Please don’t arrest us!

46

## Slide 47

### **Speeding up public key testing**

**SSH servers implement MaxAuthTries** → OpenSSH → This is why → Not all servers defaults to 5 & having >4 count pubkey counts keys in your tests as pubkey tests agent breaks failed…

47

## Slide 48

### **Rapid testing with a single connection**

**10% of all public SSH servers do not rate limit key testing** → Dropbear is the most common, but many others

|**GlobalScape EFT**|**Maverick SSHD**|**LANCOM**|**Adtran**|
|---|---|---|---|
|**BitVise WinSSHD**|**GoAnywhere**|**Arris**|**Crestron**|
|**CrushFTPd**|**mod_sftpd**|**Medallia**|**+ Many More!**|

48

## Slide 49

### **Testing millions of public keys fast**

- % **wc -l github-2018.keys** % **nc 192.168.68.2 22** 4,673,197 data/github.keys SSH-2.0-dropbear_2022.83

- % **sshamble scan --checks pubkey-hunt \** **single connection**

**--pubkey-hunt-conn-limit 1000000 --pubkey-hunt-file github-2018.keys \ -u root 192.168.68.2**

192.168.68.2:22 pubkey-hunt is running with 4673197 test keys 192.168.68.2:22 pubkey-hunt completed 4673190/4673197 keys in **7m37s (10544/s)** 192.168.68.2:22 pubkey-hunt accepted hunted half-auth for root with key ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDipNPRHvHknF6WLl7oEPoxxH7k13iKA/14yiWwOwHAUFg+1tl…. dropbear[2921]: Exit before auth from <192.168.68.1:50311>: Exited normally

49

## Slide 50

### **Compare vs OpenSSH MaxAuthLimit=5**

- % **wc -l github-2018.keys** % **nc 192.168.68.2 2222** 4,673,197 data/github.keys SSH-2.0-OpenSSH_9.2p1 Debian-2+deb12u3

- % **sshamble scan --checks pubkey-hunt \** **single connection**

- **--pubkey-hunt-conn-limit 1000000 --pubkey-hunt-file github-2018.keys \**

- **-u root 192.168.68.2 -p 2222**

192.168.68.2:2222 pubkey-hunt is running with 4673197 test keys 192.168.68.2:2222 pubkey-hunt completed 4673190/4673197 keys in **9h50m4s (132/s)** 192.168.68.2:2222 pubkey-hunt accepted hunted half-auth for root with key ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDipNPRHvHknF6WLl7oEPoxxH7k13iKA/14yiWwOwHAUFg+1tl…. sshd[6530]: Connection closed by authenticating user root 192.168.68.1 [preauth]

50

## Slide 51

**New Meets Old** (Authentication Bypass)

51

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
(G runz=ro
New Meets Old
(Authentication Bypass)
```

## Slide 52

### **Secure shell uses a strict state engine**

- → Accepted client message types change as the connection moves through each state

- → OpenSSH & Dropbear remap the table of command handlers on each state change

- → Message IDs are clamped to specific allowed ranges by session state

|SSH2_MSG|_TRANSPORT_MIN|1||
|---|---|---|---|
|SSH2_MSG|_TRANSPORT_MAX|49||
|SSH2_MSG|_USERAUTH_MIN|0||
|SSH2_MSG|_USERAUTH_MAX|79||
|SSH2_MSG|_USERAUTH_PER_METHOD_MIN||60|
|SSH2_MSG|_USERAUTH_PER_METHOD_MAX||79|
|SSH2_MSG|_CONNECTION_MIN|80||
|SSH2_MSG|_CONNECTION_MAX|127||
|SSH2_MSG|_RESERVED_MIN|128||
|SSH2_MSG|_RESERVED_MAX|191||
|SSH2_MSG|_LOCAL_MIN|192||
|SSH2_MSG|_LOCAL_MAX|255||
|SSH2_MSG|_MIN|1||
|SSH2_MSG|_MAX|255||

52

## Slide 53

### **State transitions gone wrong (historic)**

**CVE-2018−10933** A bug in libssh where the server trusted a client-sent USERAUTH_SUCCESS message.

**Metasploit support!**

53

## Slide 54

### **State transitions gone wrong (new)**

What happens if we ask for a session at every possible state transition?

**Free shells!**

54

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
54
State transitions gone wrong (new) (G runz=ro
What happens if we ask for
a session at every possible
state transition?
Free shells!
SSH Client SSH-SERVER
TCP | f SSH-TRANS | [ SSH-AUTH | f SSH-CONN |
Connect
Server Version
Client Version
Verify Versions
eS,
Server Key Init
Client Key Init
Verify Kex
Key Exchange »
SSH2_MSG_SERVICE_REQUEST
SSH2_ MSG SERVICE ACCEPT
SSH2_MSG_USERAUTH_REQUEST (user,svc —— ,data)
—>
SSH2_MSG_USERAUTH_SUCCESS
> Create Larval Session
Ca
Send “pty-req”
Allocate PTY
CaF
Configure Session
Execute Subprocess
Send “env”
Open Channel “shell”
Channel Read/Write
Channel Close
```

## Slide 55

### **State transition vulnerabilities**

|**Product**|**Impact**|**Details**|
|---|---|---|
|Digi TransPort WR Gateways|Remote CLI as
SUPER|Authentication bypass due to uninitialized variable. Updates
available  for WR11, WR21, WR31, WR44R, WR44RR included in
version 8.6.0.4. The Digi International product security team
was great to work with (via Bugcrowd).|
|Realtek ADSL Routers|Remote CLI
access as admin|Authentication bypass via skipping ssh-userauth.
White-labeled by Netis, Neterbit, and many other vendors.
Observed in firmware as recent as 2023.|
|Panasonic Ethernet Switches|Remote CLI
access as admin|Authentication bypass via skipping auth “none” after the
ssh-userauth sequence. Models include PN28080K,
PN28240i, and likely others.|

55

## Slide 56

### **Neterbit NSL-224 authentication bypass**

56

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Neterbit NSL-224 authentication bypass
(G runz=ro
(—
>
ce ss
```

## Slide 57

### **Digi TransPort authentication bypass**

57

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
57
Digi TransPort authentication bypass
(G runz=ro
Va
~
ce ss
```

## Slide 58

### **Post-session authentication is a bad idea**

Various products allow **_none_** authentication & then implement interactive login in the session. Dangerous due to the extensive post-auth attack surface of SSH.

Post-session capabilities
shell exec
pty-req x11−req
env
subsystem
break signal
agent-auth-req window-change

58

## Slide 59

### **Post-session authentication**

59

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
59
Post-session authentication
root@ password:
Copyright (c) 2021 SonicWall, Inc.
Using username ‘root’.
(G runz=ro
X y,
Password: Please login:
Copyright (c) 2882 - 2013 Juniper Networks,
Username: fj
ner
All rights reserved.
```

## Slide 60

### **Ruckus Wireless AP command injection**

**SSH auth** **_none_ drops to an interactive login session** → The password input is passed into a shell without escapes echo -n "$(echo pa55w0rd 1>&2)" | sha256sum **Fixed in firmware versions v5.2.1 (stable) & 6.2.1 (tech)** → Trivial root & still ~900 exposed on the internet → No CVE, no security mention in the release notes → Why did this bug live so long?

60

## Slide 61

### **Ruckus Wireless AP command injection**

61

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
61
Ruckus Wireless AP command injection
(G runz=ro
(—
~
ce ss
```

## Slide 62

### **Signal handling varies by service**

→ OpenSSH restricts signals to relatively safe options → Dropbear allows just about anything, even SEGV → Signal-based attacks seem promising

Login:

sshamble> **signal SEGV**

Aiee, segfault! You should probably report this as a bug to the developer

62

## Slide 63

## **Fun with Forwarding**

63

## Slide 64

SSH connection forwarding
Virtual Connection
“client” “ssh server” “remote”
$ ssh -L
sshd httpd
1234:remote:80
SSH Channel Raw TCP connection

64

## Slide 65

### **Forwarding in restricted shells**

**Inadvertent forwarding in SSH is a common issue**

###### **Post-auth login enables unauthenticated attackers**

- → Network devices, virtual machines, & appliances

- → Can enable other attacks & bypass restrictions

   - → Not super common, but we found some anyways

   - → Requires testing a few destinations to evade ACLs

- → Exposes localhost-bound daemons

65

## Slide 66

### **ION Networks Service Access Point**

66

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
66
ION Networks Service Access Point
(G runz=ro
y
~
ce ss
```

## Slide 67

## **Checkout Git**

67

## Slide 68

### **Git-based code forges support SSH**

- → Services like GitHub, Gitlab, Bitbucket

- → Projects like GOGS, Gitea, Forgejo, Gerrit

- → Libraries like charmbracelet/ssh & Mina

68

## Slide 69

### **Gitlab, Gitea, & Forgejo**

→ Environment control limited to **GIT_PROTOCOL** → Git only parses the **version** parameter → Usually safe, but bugs still exist

● Go < 1.19.3 via <u>CVE-2022−41716</u>

**GIT_PROTOCOL=version=2:** **_\x00PATH_ =C:\Users\gitlab\repositories\rob**

69

## Slide 70

### **GOGS “env” command injection**

**GOGS was the first Go-based git forge**

- → Supports SSH “env”, but gets it terribly wrong

ExecCmd("env", fmt.Sprintf("%s=%s", env.Name, env.Value))

###### **This does nothing, "env" doesn't set the parent env**

- → GOGS supports self-registration & **_env_** often supports **-S**

- → Exploit with env _-SA=B touch /tmp/fun_

- → No patch available, consider alternatives

- Independently discovered by Sonar Source (reported 2 days before us): CVE-2024−39930

70

## Slide 71

### **SSH libraries &** **_env_ : Apache Mina**

###### **Apache Mina is a Java package for SSH clients & servers**

- → Passes "env" variables to caller with no restrictions

- → Callers (like Gerrit) **do** limit the environment

- → JGit & friends don’t spawn subprocesses

71

## Slide 72

### **SSH libraries &** **_env_ : Soft Serve**

###### **Soft Serve is a feature-full Git forge that provides a beautiful CLI**

- → Uses charmbracelet/ssh (a gliderlabs/ssh fork)

- → Accepts all environment variables

- → Soft Serve passes these to Git

- → Combination is a remote shell

**CVE-2024−41956**

72

## Slide 73

### **Remote Code Execution in Soft Serve**

73

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
73
Remote Code Execution in Soft Serve
(G runz=ro
,
~
ce ss
```

## Slide 74

## **OpenSSH Fragmentation**

74

## Slide 75

### **OpenSSH divergence by platform**

|**Name**|**Divergence**|**Notes**|
|---|---|---|
|**Apple macOS**|**Light**|Changes are limited to macOS compatibility, support for the
Keychain, the macOS PKCS helper, & endpoint event logging
support.|
|**Debian/Ubuntu**
**Linux**|**Moderate**|Systemd support & much more (36+ patches)|
|**Red Hat Linux**|**Moderate**|Systemd support & much more (~60 patches)|
|**PKI-X SSH**|**Major**|Forked in 2002 for X509 support, commonly found in
networking gear and FIPS-compliant network appliances.
Generally follows OpenSSH changes, but not exactly.|
|**Microsoft**
**Windows**|**Extreme**|Over 350 files changed. Replaces fork with subprocesses,
removes chroot support & log sanitization. Logs to Windows
Events. Sends telemetry containing SSH-encrypted values.
Password authentication uses Lsa* functions. Still hasn't
fixed Terrapin.  Not affected by regreSSHion.|

75

## Slide 76

### **OpenSSH for Windows**

76

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
76
enSSH for Windows
Recycle Bin a
Oo Fa
BE Windows Powershell x ae ao x
[C}
PS C:\Users\Dev> ssh
OpenSSH_for_Windows_8.6p1, LibreSSL 3.u.3
PS C:\Users\Dev> ssh dev@127.0.0.1 -p 9999
dev@127.0.0.1's password:
9
ge
Task Manager
Processes
Name
@ NVIDIA Container (2)
IF Phone Link (3)
Q Type a name, publisher, or PID to sea...
FB Runnewtask @ Endtask  ] Efficiencymode +++
1% 22% 0% 0%
Status CPU Memory Disk Network
0% «© 550MB = «OMB/s_ Mbps
Suspended @ 0% = 51.6MB OMB/s Mbps
Il ProintelliMouseNotificationService.exe 0% = 11MB MB/s Mbps
IE POP Clipboard Monitor
[ tunZero Explorer
Tl Search @)
Hh Spooler Subsystem App.
© Spotty Widget 2)
Bi shdee
BI chdee
Start (2)
0% = 20MB_—OMB/s_OMbps
0% © 473MB_ = OMB/s_OMbps
0% © 1259MB_ = OMB/s_«OMbps
0% _53MB__OMB/s._0Mbos
© @ Administrator: Windows Pom X +
PS C:\Users\Dev> sshd 9999
debug2: load_server_config: filename __PROGRAMDATA__\\ssh/sshd_config
debug3: w32_fstat ERROR: bad fd: 3
debug2: load_server_config: done config len = 253
dobuatnparse_server_config_depth: config __PROGRAMDATA_.\\ssh/sshd_config len 253
/—
B® windows PowerShell x ae
PS C:\Users\Dev> ssh
OpenSSH_for_Windows_8.6p1, LibreSSL 3.4.3
PS C:\Users\Dev> ssh dev@127.0.0.1 9999
dev@127.0.0.1's password:
Ne
= Oo
XGRAMDATA__\\ssh/sshd_config:79 setting Subsystem sftp sftp-server.exe
ing syntax for 'Match Group administrators’
ersion OpenSSH_for_Windows_8.6, LibreSSL 3.4.3
x Bsswd: Lookup_sid() failed: 1332.
e host key #0: ssh-rsa SHA256: oQV7hyF3E+bw00J0e21S8rFEyLad@VXzzrx00i3P61c
e host key #1: ecdsa~sha2-nistp256 SHA256:ttumLLv2ub+MuJ20FuaYTnXGQvd96NZFNY3eALy jQA
ssh-ed25519 SHA256:rZK@/Hma9UCV8FHj8142zTIQ01Q3SZpzUR4iGqB60Eks.
\Windows\\System32\\OpenSSH\\sshd.exe*
Neate \\ssh/sshd_config:38 setting AuthorizedkeysFile .ssh/authorized_keys
jetting O_NONBLOCK
et_v6only: set socket 3 IPV6_V6ONLY
0 port 9999 on ::.
ling on :: port 9999.
setting O_NONBLOCK
nd to port 9999 on 0.0.0.0.
Server listening on 0.0.0.0 port 9999.
a Ge
443 PM
anjzozs ®
```

## Slide 77

### **OpenSSH for Windows Telemetry**

→ OpenSSH for Windows sends detailed usage data to Microsoft → Client & server versions, kex init parameters, auth methods

void send_ssh_version_telemetry (const char * ssh_version , const char * peer_version , const char * remote_protocol_error ) { TraceLoggingRegister (g_hProvider1 ); TraceLoggingWrite ( g_hProvider1 , "Startup" , TelemetryPrivacyDataTag (PDT_ProductAndServiceUsage ), TraceLoggingKeyword (MICROSOFT_KEYWORD_MEASURES ), TraceLoggingString (ssh_version , "ourVersion" ), TraceLoggingString (remote_protocol_error , "remoteProtocolError" ), TraceLoggingString (peer_version , "peerVersion" ) ); TraceLoggingUnregister (g_hProvider1 ); }

77

## Slide 78

### **compat/timingsafe_bcmp.c**

int timingsafe_bcmp(const void *b1, const void *b2, size_t n) { const unsigned char *p1 = b1, *p2 = b2; int ret = 0; for (; n > 0; n--) { ret |= *p1++ ^ *p2++; } return (ret != 0); } **A solid bit of code from DJM**

**A solid bit of code from DJM** → Timing-safe → Efficient → Secure

78

## Slide 79

### **compat/timingsafe_bcmp.c for Windows**

int timingsafe_bcmp(const void *b1, const void *b2, size_t n) { const unsigned char *p1 = b1, *p2 = b2; int ret = 0; for (; n > 0; n--) { #ifdef WINDOWS if (*p1 == '\r' && *(p1 + 1) == '\n' && *p2 == '\n') p1++; #endif // WINDOWS ret |= *p1++ ^ *p2++; } return (ret != 0); }

79

## Slide 80

### **compat/timingsafe_bcmp.c for Windows**

int timingsafe_bcmp(const void *b1, const void *b2, size_t n) { const unsigned char *p1 = b1, *p2 = b2; int ret = 0; for (; n > 0; n--) { #ifdef WINDOWS if (*p1 == '\r' && *(p1 + 1) == '\n' && *p2 == '\n') p1++; #endif // WINDOWS **Two lines, but so many bugs!** ret |= *p1++ ^ *p2++; → Not timing-safe } return (ret != 0); → 1−byte OOB per \r } → Unequal byte match

80

## Slide 81

### **A critical function within OpenSSH**

- → MAC check on every SSH packet

- → RSA signature verification

- → SSH certificate comparison

- → X11 cookie comparison

- → chachapoly_crypt() MAC

- → SSHFP DNS record checks

- → SSH agent validation

- → WebAuthn SK checks

- → SSH keygen verification

- → … & much more!

###### **One of the most sensitive functions, but what can we do with it?**

- → Attacker has limited influence on the first argument

- → Requires brute force to trigger in the MAC check

- → Not obviously exploitable :(

81

## Slide 82

82

**https://azure.microsoft.com/en-us/products/devops/server**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
82
Comprehensive security and compliance, built in
VY Microsoft invests more than $1 billion annually on cybersecurity \4/ We employ more than 3,500 security experts who are dedicated
research and development. to data security and privacy.
Learn more about security on Azure
https://azure.microsoft.com/en-us/products/devops/server
(G runz=ro
```

## Slide 83

### **Microsoft Security Response Center**

**“**

_Thank you again for submitting this issue to Microsoft. Although your report is valid, currently, MSRC prioritizes vulnerabilities that are assessed as “Important” or “Critical” severities for immediate servicing. After careful investigation, this case does not meet MSRC’s current bar for immediate servicing because currently it appears to be theoretical due to no control over the first argument to the function & would require a brute force style attack to obtain a single byte of data. If you can prove remote reachability or the ability to leak information remotely, then please submit a new report & we are happy to investigate this further!_ **”**

83

## Slide 84

## **Introducing SSHamble**

84

## Slide 85

- → A research tool for SSH implementations

- → Interesting attacks against authentication

- → Post-session authentication attacks → Pre-authentication state transitions

- → Post-session enumeration

- → Easy timing analysis

**https://SSHamble.com**

85

## Slide 86

### **Built-in checks**

|**b**|auth=none|skip=auth|auth=success|
|---|---|---|---|
|**ypass**|method=null|method=empty|skip=pubkey-any|
|**publickey**|pubkey-any
half-auth-limit|pubkey-any-half
pubkey-hunt|user-key
—|
|**assword**|pass-any|pass-empty|pass-null|
|**p**|pass-user|pass-change-empty|pass-change-null|
|**keyboard**|kbd-any
kbd-user|kbd-empty
—|kbd-null
—|
|**gss-api**|gss-any|—|—|
|**userenum**|timing-none|timing-pass|timing-pubkey|
||vuln-tcp-forward|vuln-generic-env|vuln-softserve-env|
|**vulns**|vuln-gogs-env|vuln-ruckus-password-escape|—|

86

## Slide 87

### **Getting started**

Start a network scan

$ sshamble scan -o results.json 192.168.0.0/24

Analyze the results $ sshamble analyze -o output results.json

Specify ports, usernames, passwords, public keys, private keys, and more $ sshamble scan -o results.json 192.168.0.0/24 \

--users root,admin,4DGift,jenkins \ –-password-file copilot.txt \ -p 22,2222 \ --pubkey-hunt-file admin-keys.pub \

Open an interactive shell for sessions $ sshamble scan -o results.json 192.168.0.0/24 \ –-interact first --interact-auto “pty,env LD_DEBUG=all,shell”

87

## Slide 88

### **The interactive shell**

###### **Enter the sshamble shell with `^E`. Commands:**

**exit** - Exit the session (aliases 'quit' or '.') **help** - Show this help text (alias '?') **env** a=1 b=2           - Set the specified environment variables (-w for wait mode) **pty** - Request a pty on the remote session (-w for wait mode) **shell** - Request the default shell on the session **exec** cmd arg1 arg2     - Request non-interactive command on the session **signal** sig1 sig2         - Send one or more signals to the subprocess **tcp** host port         - Make a test connection to a TCP host & port **unix** path              - Make a test connection to a Unix stream socket **break** milliseconds      - Send a 'break' request to the service **req** cmd arg1 arg2     - Send a custom SSH request to the service **sub** subsystem         - Request a specific subsystem **send** string            - Send string to the session **sendb** string            - Send string to the session one byte at a time

sshamble>

88

## Slide 89

### **Happy scanning!**

89

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
89
Happy scanning! (G runz=ro
(— >)
l
XX y,
ce ss
```

## Slide 90

## **Defending SSH**

90

## Slide 91

### **Client recommendations**

**Use public key authentication exclusively**

- → Separate GitHub/Launchpad keys from server administration keys

- → Store your private key on a hardware token

- → Switch to Ed25519 if you haven’t already

- **If you use ssh agent forwarding, restrict destinations**

- → https://www.openssh.com/agent-restrict.html

**Adjust configuration for LTS distro SSH clients**

- → Update ssh_config for OpenSSH 9.8+ Ciphers/MACs/KeyAlgs

91

## Slide 92

### **Server recommendations (general)**

**Centralize SSH hostkey management**

- → Collect server hostkeys & provide clients pre-approved known_hosts

**Use public key authentication exclusively**

- → Limit public key types to Ed25519 & RSA >= 2048

**Limit resource usage by attackers**

- → Enable PerSourcePenalties & set  PerSourceNetBlockSize

- → Consider lowering MaxStartups & MaxAuthTries

- → Disable forwarding (TCP, Unix, Agent, X11) unless required

**Adjust configuration for LTS distro SSH servers**

- → Update sshd_config for OpenSSH 9.8+ Ciphers/MACs/KeyAlgs

## Slide 93

### **Server recommendations (CA)**

###### **Configure a CA for server hostkeys**

- → Create a CA, sign, & distribute hostkeys to each of your servers

- → Set known_hosts for clients: @cert-authority *.domain.tld <CA.pub>

- → CA hostkeys are backwards compatible (fallback to known_hosts)

- →

- **Configure a CA for signing user keys**

- → Sign user public keys with short-term expirations (using your tool of choice)

- → ssh-keygen -s userCA -I user@example.com -n username -V +1h userkey.pub

###### **Consider mandating token-stored private keys**

- → Enforce verification on servers with PubkeyAuthOptions

- → Require PIN with verify-required (vs touch-required)

93

## Slide 94

### **Vendor recommendations**

###### **Build with OpenSSH wherever possible**

- → Leverage OpenSSH 9.8p1+ for tons of great defensive features

- → Integrate with system authentication vs post-session

###### **Ship clean firmware without static credentials**

- → Prior to imaging, purge all host keys, known_hosts, & authorized_keys

- → Disable password authentication (or restrict to serial or console tty)

###### **General hardening**

- → Disable empty password auth & limit which users can authenticate

- → Disable all types of forwarding, set ForceCommand for shells

94

## Slide 95

### **Conclusions**

**1**

**The secure shell is more critical than ever**

**2**

Public key
authentication
is still leaky

3

**4**

OpenSSH Tons of
is still your  issues in the
safest choice periphery

95

## Slide 96

# **Thank you.**

HD MOORE     |     ROB KING     |     AUGUST 7, 2024

runZero.com

research@runZero.com

SSHamble.com

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
biSekhat (| runz=ro
USA 2024
Thank you.
HDMOORE | ROBKING | AUGUST7, 2024
(F
c
rFunZ=ro
ReseARCH PSSM
runZero.com research@runZero.com SSHamble.com
```

## Slide 97

### **References**

- → https://github.com/ssh-mitm/ssh-mitm

- → https://ssh-comparison.quendi.de/comparison/hostkey.html

- → https://words.filippo.io/ssh-whoami-filippo-io/

- → https://github.com/badkeys/badkeys

- → Metasploit: ssh_identify_pubkeys (2012)

- → regreSSHion: https://www.qualys.com/2024/07/01/cve-2024−6387/regresshion.txt

- → Terrapin: https://terrapin-attack.com/

- → https://labs.watchtowr.com/auth-bypass-in-un-limited-scenarios-progress-moveit-transfer-cve-2024−5806/

- → https://boehs.org/node/everything-i-know-about-the-xz-backdoor

- → http://thetarpit.org/2018/shithub-2018−06

- → https://helda.helsinki.fi/server/api/core/bitstreams/471f0ffe-2626−4d12−8725−2147232d849f/content

- → https://github.blog/2023−03−23−we-updated-our-rsa-ssh-host-key/

- → Kannisto, J., Harju, J. (2017). The Time Will Tell on You: Exploring Information Leaks in SSH Public Key Authentication. In: Yan, Z., Molva, R., Mazurczyk, W., Kantola, R. (eds) Network and System Security. NSS 2017. Lecture Notes in Computer Science(), vol 10394. Springer, Cham. https://doi.org/10.1007/978−3−319−64701−2_22

- → West, J.C., Moore, T. (2022). Longitudinal Study of Internet-Facing OpenSSH Update Patterns. In: Hohlfeld, O., Moura, G., Pelsser, C. (eds) Passive and Active Measurement. PAM 2022. Lecture Notes in Computer Science, vol 13210. Springer, Cham. https://doi.org/10.1007/978−3−030−98785−5_30

- → Neef, S. (2022). Source & result datasets for "Oh SSH-it, what's my fingerprint? A Large-Scale Analysis of SSH Host Key Fingerprint Verification Records in the DNS" [Data set]. Zenodo. https://doi.org/10.5281/zenodo.6993096

97
