---
title: "Apple Disk-O Party"
speakers: ["Csaba Fitzl"]
conference: "Black Hat"
conference_full: "Black Hat Europe 2024"
edition: "Europe"
year: 2024
source_pdf: "BlackHat_Europe_2024_slides/Csaba Fitzl_Apple Disk-O Party_Compressed.pdf"
pages: 95
sha256: "026472de21aa09f984bed1ee08221e752948b39107680e34db8c940bb5b1ce47"
text_chars: 20726
ocr_pages: 65
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T00:02:11Z"
---
# Apple Disk-O Party

**Speakers:** Csaba Fitzl  
**Conference:** Black Hat Europe 2024  
**Source:** `BlackHat_Europe_2024_slides/Csaba Fitzl_Apple Disk-O Party_Compressed.pdf` (95 pages)

## Slide 1

# Apple Disk-O Party

**_Csaba Fitzl Twitter: @theevilbit_**

## Slide 2

# whoami

• Principal macOS Security Researcher @Kandji

- author of EXP-312 - macOS Exploitation 🐙) at OffSec

- training (

- ex red/blue teamer

- macOS bug hunter

- husband, father

- 🥾 🏔

- • hiking, trail running

## Slide 3

# agenda

1. disk arbitration service

2. CVE-2023-42838 - Sandbox Escape via diskarbitrationd

3. typical mount call flows

4. CVE-2024-44175 - LPE + Sandbox Escape via diskarbitrationd

5. CVE-2024-40855 - TCC Bypass and Sandbox Escape via diskarbitrationd

6. CVE-2024-27848 - LPE via StorageKit

7. CVE-2024-44210 - LPE and TCC bypass via StorageKit

8. CVE-2024-40783 - bypass TM data protection via APFS

9. LPE via Disk Utility

10. conclusion

## Slide 4

# **disk arbitration service**

## Slide 5

# diskarbitrationd - the basics

### • system wide service, defined in: • /System/Library/LaunchDaemons/com.apple.diskarbitrationd.plist • Mach Service: com.apple.DiskArbitration.diskarbitrationd

- manage disk mounting, unmounting

• calls mount/unmount under the hood

## Slide 6

# diskarbitrationd - why we like it?

- runs as root

- unsandboxed

- ~ full disk access rights

- Mach service accessible from application sandbox

- opensource

## Slide 7

# diskarbitrationd - MIG

- MIG service

• DA framework abstracts the MIG service

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
diskarbitrationd - MIG
@ MIG service
routine _DAServerDiskCopyDescription
routine _DAServerDiskGetOptions
routine _DAServerDiskGetUserUID
e DA framework abstracts the routine _DAServerDiskTsClaimed
0 routine _DAServerDiskSetAdoption
MIG service routine _DAServerDiskSetEncoding
routine _DAServerDiskSetOptions
routine _DAServerSessionCopyCallbackQueue
routine _DAServerSessionCreate
routine _DAServerSessionQueueRequest
routine _DAServerSessionRegisterCallback
routine _DAServermkdir
routine _DAServerrmdir
routine _DAServerSessionSetKeepALive
simpleroutine _DAServerSessionRelease
simpleroutine _DAServerSessionSetAuthorization
simpleroutine _DAServerSessionSetClientPort
simpleroutine _DAServerSessionUnregisterCallback
simpleroutine _DAServerSessionQueueResponse
simpleroutine _DAServerDiskUnclaim
```

## Slide 8

diskarbitrationd - mount call flow

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
diskarbitrationd - mount call flow
DAServerSessionQueueRequest > DAQueueRequest
> DAAuthorize
checks “sandbox
and privilege)
DAMountWithArguments |<—_— DARequestMount ——|  DARequestDispatch
posix_spawnmount,...)
- permissions
DAMountWithArgumentsC ~ (DAR leSystemMountwithAr
allbackStogel med Unetiiiithediiar
```

## Slide 9

# **CVE-2023-42838 - Sandbox Escape**

## Slide 10

Where is the problem?

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Where is the problem?
|
eee  csaby — -zsh — 80x24
Last login: Thu Apr 7 16:08:31 on ttys@@1
csaby@monty ~ % touch /Users/Shared/sandboxescape.txt
‘csaby@monty ~ % mount
/dev/disk4sis1 on / (apfs, sealed, local, read-only, jo
jouWna
devfs on /dev (devfs, local, nobrowse)
/dev/disk4s6 on /System/Volumes/VM (apfs, loc
rowse)
/dev/disk4s2 on /System/Volumes/Preb
/dev/disk4s4 on povidone eae at
/dev/disk2s2 on /System/Vol cal, noexec
nobrowse) EAN
/dev/disk2s1 on
ofs, local, nodev, nosuid, jo
1leG, noatime, nob
journaled, nobrowse)
cay, b Sireuie, nobrowse)
\. noatime,
aled, nobrowse)
aed, nobrowse)
, Nobrowse, protect)
/dev/disk2s3
—
```

## Slide 11

# why is that a problem? • no quarantine extended attribute ==> files not quarantined • files not quarantined ==> no GateKeeper (technically there is) • no GK ==> we can launch anything, included unsandboxed apps • can be used for SB escape

## Slide 12

# CVE-2023-42838 - the issue

• diskarbitrationd doesn't add quarantine flag to the quarantined disk image when mounted

- ioreg does show the property

- da should check the property

## Slide 13

CVE-2023-42838 - what goes on?

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
CVE-2023-42838 - what goes on?
——_ >] DAD iskCreateFromIOMedia |——> LORegistryEntrySearchCFProperty
add quarantine Flag mount option
mount, /dev/disk| ——S>| b AbiskCreateFromBSDName
```

## Slide 14

how to get a /dev/disk in Sandbox?

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
how to get a /dev/disk in Sandbox?
unmount /dev/diskxsY
using diskarbitrationd
API
\
| /dev/diskxsy |
\ is created ;
\
```

## Slide 15

# CVE-2023-42838 - fix

### • the kernel will add quarantine flag to every mount if the device is quarantined • basically the "IOReg" query went down to kernel and performed on every mount

## Slide 16

**call flows**

## Slide 17

call flow 1.: mount only call

## Slide 18

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
fxn |
xnu checks:
- classic usec
POSIX permissions
- MAC callout
cuns as X
might be sancdboxed runs as the caller
```

## Slide 19

## case study: + mount only + mount over root owned dir with user

## Slide 20

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
OPERATION
env: user
target owner: root
disk owner: root
Va \
mount
SS
```

## Slide 21

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
env: user
IHearget owner: root
disk owner: root
```

## Slide 22

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
7 Y
“
OPERATION
env: user
IHearget owner: coot
disk owner: root
FAIL!!! user has no rights over target
```

## Slide 23

# call flow 2.: mount with diskarbitrationd

## Slide 24

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
=
XY
xu checks:
- classic user
; POSIX permissions
might be sandboxed rung as root + unsandboxed runs as disk owner - MAC £ allout
diskarbitrationedl
CUNS AS X
diskarbitrationd checks:
- if calling user id == cisk owner il
- sandbox _check
```

## Slide 25

## case study: + diskarbitrationd + mount over root owned dir with user

## Slide 26

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
OPERATION
env: user
target owner: root
\< disk owner: root
diskarbitrationedl
Va \
mount
SS
```

## Slide 27

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
diskarbitrationedl |
OPERATION
env: user
target owner: root
disk owner: root
FALL!!! user [= root
```

## Slide 28

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
OPERATION
env: user
target owner: coot
\< disk owner: user
diskarbitrationedl
Va \
mount
SS
fxn |
```

## Slide 29

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
diskarbitrationedl (
OPERATION
eriv: user
target owner: root
disk owner: user
Va \
mount
SS
fxn |
```

## Slide 30

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
diskarbitrationedl
target owner: root
disk owner: user
```

## Slide 31

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
diskarbitrationedl
OPERATION
env: user
target owner: coot
disk owner: user
1
FAIL!!! user [= root
```

## Slide 32

## case study: + diskarbitrationd + attack diskarbitrationd with symlink

## Slide 33

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
fOPERATION
env: user
target: link ->
/tmo/ mnt
target owner: user
\cisk owner: user
diskarbitrationedl
Y N
X
```

## Slide 34

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
diskarbitrationedl
fOPERATION
env: user
target: link ->
Jtmp/s mnt
target owner: user
isk owner: user
```

## Slide 35

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
diskarbitrationedl
“4 Y
mount -k
\
fOPERATION
env: user
target: link ->
Jtme/ mnt
target owner: user
\cisk owner: user
fxn |
```

## Slide 36

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
diskarbitrationedl
fOPERATION
env: user
target: link ->
Jtme/ mnt
target owner: user
isk owner: user
FAIL!!! »nu doesn't Follow symlinks, (-k)
```

## Slide 37

## **CVE-2024-44175- Sandbox Escape & LPE (UserFS)**

## Slide 38

# CVE-2024-44175 - theory

- diskarbitrationd supports 2 file systems

   - backed by KEXT

   - backed by UserFS

• symlink check is not done in UserFS 😎

## Slide 39

# CVE-2024-44175 - theory

• user ID / owner / etc is not
passed

• always run as root

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
CVE-2024
@e user ID / owner / etc is not
passed
@
returnValue = [FSKitDiskArbHelper DAMountUserFSVolume: fsType
deviceName:deviceName
mountPoint:mountpoint
volumeName LumeName
nountOptions:mountOptions] 3|
@ always run as root
eco
Subtree: 5
launchd
xpeproxy
fskitd
fskitd
mount_lifs
175 - theory
Event Facts
Metadata  Eventcorrelation2 Process group 2 Initiating process JSON
Event details
Endpoint Security message details
+ Event type: © ES_EVENT_TYPE_NOTIFY_EXEC
Message timestamp: 2024-08-@5T15:24:43.539Z
Initiating user: root (0)
Process execute details
© Start time: 2024-08-05T15:24:43.539Z
User: root (@)
+ Process nami mount_lifs -PID: 1015 -GID: 1010
+ Process path: /sbin/mount_lifs
+ Command line:
/sbin/mount_lifs
rsize=524288,wsiz 5536, readahead=4, dsize=65536, actimeo=10, nodev, noowners, nosuid, noatime, fh=0
1000000300000000000000000000000000000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000 :/ /Users/tree/mnt
Code signing details
+ Code signing type: Platform binary
+ Process signing ID: com.apple.mount_lifs
+ SHA256 Code directory hash: @29a9dc7f13e72b4c26ac8c9c61b94b9b17749ef
+ Certificate chain:
```

## Slide 40

## Slide 41

CVE-2024-44175 exploitation

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
CVE-2024-44175 exploitation
user: root
mountpoint:
link -> not_ok_place
user: root
mount point:
link -> not_ok_place
user. user
/ mounteoint;
link -> ok_place
user. user
mountpoint;
link -> ok_place
```

## Slide 42

weaponization for LPE

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
mount over
/etc/cups >
\
\
drop
‘
“
Some junk
Cups-Files.conf:
Errorlog /etc/sudoers.d/lpe
LogFilePerm ##7
weaponization tor LPE
/etc/sudoers.d/lpe:
_ oS | tstoff ALL=(ALL) NOPASSWD:ALL
ao
create file rN
7 edit
/ |
edit
1) /ete/sudoers.d/lpe
2) cups-Files.conf
/
/
cupsctl ———_=>=>
cups-files.conf:
Errorlog /etc/sudoers.d/lpe
LogFilePerm 700
Some junk
```

## Slide 43

weaponization for SB escape

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
weaponization for SB escape
mount over
~/Library/Preferences
run "/bin/zsh ~/Library/Preferences/lpe.sh"
pe-sh:
shell script to achieve LPE
com.apple. Terminal. plist:
CommandString:
/bin/zsh ~/Library/Preferences/lpe.sh
```

## Slide 44

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ Finder File Edit View Go Window’ Help oO Q S ThuOct3 22:49
DAUserFSSbxLPE
— i DAUserFSSbxLPE.zip
2. Applicati... Desktop
(=) Desktop TD Documents
® Downloads
{} Documents Movies
© Downloads BB Music
fa} n00b ® Pictures
D Public
© iCloud Dri...
Guest
9eOS82s8O08eG 0860: 570 18 at
```

## Slide 45

# CVE-2024-44175 fix • "nofollow" is added to every mount -> no symlinks • fskitd gets the original requestor and executes mount with that user

## Slide 46

## **CVE-2024-40855- Sandbox Escape & TCC Bypass (directory traversal)**

## Slide 47

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
diskarbitrationd
mu checks:
- classic user
crUunS aS X - MAC callout
might be sandboxed
runs as root + unsandboxedl
diskarbitrationd checks:
- if calling user id == disk owner id
- sandbox _check
```

## Slide 48

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
diskarbitrationd [nou eon)
ADiskMountWithArqumentsc ommon AServerSessionQueueRequest
realeath FURLCreateFromFileSystemRepresentation
CFURLCreateFromFileSystemRepresentation sandbox_checkby_audit_token
/ - removes ../ - removes WA
- removes .. ; - resolves symlink - resolves symlink
- resolves symlink
ONLY FOR THE TIME OF CHECK!! FINAL RESOLUTION!!
PERSISTENT!!
```

## Slide 49

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
diskarbitrationd [vot]
ADiskMountWithArqunentsCommon AServerSessionQueueRequest
FURLCreat eFromFileSyste:
realoath epresentation
CFURLCreateF bunFileSystemRepresentation sandlbox_checkby_audlit token
- removes ../ - removes ../ - removes ../
- resolves symlink - resolves symlink
- resolves symlink
FINAL RESOLUTION!!
ONLY FOR THE TIME OF
PERSISTEMT!!
THE PATH IS UNCHANGED ==> placing a symlink
will cause it to fail at xnu
```

## Slide 50

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
diskarbitrationd [nou eon)
AServerSessionQueueRequest
FURLCreateFromFileSystemRepresentation
CFURL Qe: eFromFileSystemRepresentation sandbox_checkby_audit_token
- removes ../ - removes ../
- remove - resolves symlink - resolves symlink
- resolv,
PEMSISTENT!!
UNDER CALLER CONTROL ==> ../ will remain till the end
```

## Slide 51

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
OPERATION
target: / erivate/ tme/ cir/../../../Users/erab/ Library/, Ape lication Support / com.apple. TCC
dic -> / erivate/tme/’ 1/2/73
esolved path: NA
```

## Slide 52

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
sandbox_checkby_audit_token
OPERATION
target: / erivate/ tme/ cir/../../../Users/erab/ Library/, Ape lication Support / com.apple. TCC
dic -> / erivate/tme/ 1/2/73
esolved path: / erivate/tme/' 1/2/3/../../../ Users/erab/ Library/, Application Support / com.apple.T cc
```

## Slide 53

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
sanclbox_checkby__audit_token
OPERATION
target: / erivate/tme/ dir/../../../Users/erab/ Library/, Ape lication Support / com.apple.TCC
dic -> / erivate/tme/' 1/2/73
esolvect path: vA erivate/ tmo/ Users/erab/i Libracy/ Application Support / com.apple. TCC
```

## Slide 54

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
OPERATION
target: vA erivate/ ‘tmo/ dic/../../../Users/crab/ Library/ Ape lication Support / com.apple. TCC
dir
esolvedt path: NA
```

## Slide 55

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
OPERATION
target: vA erivate/ tmo/ dic/../../../Users/crab/ Libracy/ Application Support / com.apple.TC C
dir Gnot a symlink)
esolved path: /Users/erab/ Library/, Application Support / com.apple.TC c/
```

## Slide 56

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ Terminal Shell Edit View Window Help k
Q $$ MonJun3 8:14
e@ OD crab — -zsh — 80x24 oO 8 Ci}
crab@see ~ % codesign -dv --entitlements - /Applications/DADirTraverse. appl} =]
‘ (0 AllMessages_— Errors and Faults
Type Time Process Message
63 App Store
s# Automator
Books
8 Calculator
“? Calendar
@ Chess
@ Clock
@ Contacts
DADirTraverse
@ Dictionary
FaceTime
=) Find My
W Font Book
DADirTraverse
Application - 143 KB
Information
A Cranfarem
@
```

## Slide 57

the fix

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
the fix
(Cale > tod))_5( a po)
AServerSessionQueueRequest
FURLC reateFromFileSystemRepresentation
sandlbox_checkby_audit_t oken
- removes ./ - removes ./ - removes J
- resolves symlink - resolves symlink - resolves symlink
PERSISTENT!! ONLY FOR THE TIME OF CHECK! FINAL RESOLUTION!
```

## Slide 58

the fix

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
the Tix
diskarbitrationd
Z x
! no path \
\ resolution /
is kDADiskMountOptionNoFollow
set?
(cient | a sQueueRequest
yes
resolve path
-o=-_o—_— —-—_=
disallow symlink
sandbox check . and ../ in path
=e ee
```

## Slide 59

# **CVE-2024-27848 - LPE via StorageKit**

## Slide 60

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
runs as X runs as the disk owner
might be sandboxed \
la Y
XY
Ss
lassie us rmissions
MAC calldit
GOs...
g user id == disk owner id
sandbox_check
runs as root + unsancdboxed
storagekite chee
- sandbox _check
```

## Slide 61

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
(OPERATION
env: user
target owner: root
(disk owner: root
\
storagekitd
diskarbitrationd
et)
```

## Slide 62

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
(OPERATION
env: user
target owner: root
disk owner: root
diskarbitrationd
storagekitd
et)
```

## Slide 63

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
\
storagekitd
(OPERATION
env: user
target owner: coot
disk owner: root
diskarbitrationd
et)
```

## Slide 64

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
\
storagekitd
ass
oA
eriv: root <---//I
target owner: root
disk owner: root
Pom |
W
```

## Slide 65

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
(OPERATION
eriv: coot
target owner: coot
disk owner: root Trout)
\
diskarbitrationd
storagekitd
```

## Slide 66

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
eriv: root
> target ower: root
disk owner: root
\
diskarbitrationd
storagekitd
```

## Slide 67

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ = Terminal Shell Edit View Window Help G Me wto) Q $$ Wed Mar 27 14:39
OD fish — -zsh — 112x35, m
Last login: Wed Mar 27 12:36:22 on ttysee2
fish@sonomal ~ %
9HOS82#8OS8e4 BBO0«1790 FC 0 amt
```

## Slide 68

## **CVE-2024-44210 - Bypass CVE-2024-27848 - LPE + TCC bypass via StorageKit**

## Slide 69

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
runs as X runs as the disk owner
might be sandboxed \
la Y
XY
[xn |
xnu checks:
- classic user POSIX permissions
- MAC callout
CUunNS AS caller
Lv
diskarbitrationd
™—~.
runs as root + unsandboxed
diskarbitrationd checks:
- if calling user id == disk owner id
- sandbox _check
storagekitd
storagekite checks:
- sandbox _check
- target dic id == caller id
runs as root + unsandboxed
```

## Slide 70

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
target: Jtmo/ wnt
fe toragekite
1. stat Cuserid) check on target dir
Csome time passes)
2. call diskarbitrationd with target dir
target: /tme/mnt
```

## Slide 71

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
target: /tmp/link ( alternate symlink
Jete/ cups
fe toragekite
1. stat Cuserid) check on /tmo/mnt
Csome time passes)
2. call diskarbitrationd with Jete/cups
target: Jete/ CUPS
```

## Slide 72

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
THE ATT Ac K A Jt mpe/mnt
target: /tmo/ link alternate symlink
NX
~/ Library/, Application Support / com.apple.TC Cc
fe toragekite
1. sandbox _cheek on Jtmo/ mnt
Csome time passes)
2. call diskarbitrationd with
~/ Library/ Application Support / com.apple. TCC
target: ~/ Libracy/ Application Support / com.apple.TC Cc
```

## Slide 73

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
(OPERATION
env: user
/tmp/link owner: ??
(disk owner: root
\
storagekitd
diskarbitrationd
et)
```

## Slide 74

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
(OPERATION
env: user
Jtmp/| link owner: ??
disk owner: root
storagekitd
diskarbitrationd
et)
```

## Slide 75

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
\
storagekitd
(OPERATION
env: user
Jtmp/ mnt owner: user
disk owner: root
A
diskarbitrationd
» OK
et)
```

## Slide 76

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
\
storagekitd
oA
priv: root
Jete/cups owner:
disk owner: root
Pom |
W
```

## Slide 77

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
(OPERATION
priv: coot
/ ete/cups owner: root
disk owner: root
\
diskarbitrationd
storagekitd
```

## Slide 78

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
(OPERATION
eriv: coot
Jetc/cups owner: root
disk owner: root
<
diskarbitrationd
\
storagekitd
```

## Slide 79

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ Terminal Shell Edit View Window Help Q ®& FriMay 24 6:42
@ OD crab — -zsh — 130x43
crab@see ~ % swW_vers =]
ProductName: macOS
ProductVersion: 14.5
BuildVersion: 23F79
crab@see ~ % ff
iintosh HD
6 2
tartup Snapshot - APFS 62,83 GB
4.5 7:
"i = vocu © Other Volumes Free
10,26 GB 12,45 GB 40,12 GB
Mount Point (Read-Only): 1 | Type: APFS Startup Snapshot
Capacity: 62,83 GB Owners: Disabled
Available: 40,45 GB (329,3 MB purgeable) Connection: Unknown
disk4s1s1
Used: 10,26 GB Device:
Snapshot Name: com.apple.os.update-4F9A570DA7279961C47EEA2... Snapshot UUID: 8E508755-591C-4B27-ACOC-91E8E9BA4D45
```

## Slide 80

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ = Terminal
Shell
Edit
View
Window _ Help
OD crab — -zsh — 128x43
IIdb « sudo lidb « sudo -zsh
crab@see ~ % ./storagekitd-tcc.sh ff
Allow the applications below to access files and folders.
Mount Point (Read-Only):
Capacity:
Available:
Used:
/
62,83 GB
40,21 GB (541,7 MB purgeable)
10,26 GB
Snapshot Name: com.apple.os.update-4F9A570DA7279961C47EEA2...
S=SO® B80-*
-zsh
Type:
Owners:
Connection:
Device:
Snapshot UUID: 8E508755-'
Q  ThuMay 30 12:58
-zsh an
APFS Startup Snapshot
Disabled
Unknown
disk4s1s1
591C-4B27-ACOC-91E8E9BA4D45
```

## Slide 81

the ultimate fix

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
the ultimate Tix
(— diskarbitrationd
-
storegakitd DAQueueRequest
-
-
—_
-
is kDADiskMountOptionWoFollow
‘ set? ----—-~
- =”
‘\
\
es
disallow
symlink and
../f in path
```

## Slide 82

# **CVE-2024-40783 - bypass TM data protection via APFS**

## Slide 83

# Time Machine

• TM backups are protected by TCC

- if allowed - we can access all private data

• also allowed if having "Full Disk Access" permissions

## Slide 84

# APFS disk roles

• APFS defines various disk roles

• TM = Backup

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
APFS disk roles
e APFS defines various disk roles
APFS VOLUME ROLES
APFS Volumes can be tagged with certain role meta-data flags. Supported flags are:
e@ TM — Backup e B- Preboot (boot loader)
e R — Recovery
e V - VM (swap space)
s I - Installer
e T - Backup (Time Machine)
° D - Data
fish@sonomal ~ % diskutil apfs list
+-> Volume disk3s2 9DAQCF6C-F7C7-4506-9436-
° E - Update
Q06B16FBF408 e  X — XART (hardware security)
APFS Volume Disk (Role): disk3s2 (Backup) eH - Hardware
Name: . TM (Case-sensitive) e CC - Sidecar (Time Machine)
Mount Point: /Volumes/TM
Capacity Consumed: 3737165824 B (3.7 GB) 6 Ve BRGREREEES CARE
Sealed: No
FileVault: No (Encrypted at rest)
ee oe
```

## Slide 85

SIP (Sandbox Platform Profile)

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
SIP (Sandbox Platform Profile)
long __cdecl storage_class_map( )
else
{
if ( literal("/lLibrary/preferences/com.apple.timemachine.plist") != 0
) return allow("assign-storage-class 'TimeMachine'");
if ( subpath("/volumes/com.apple.timemachine.localsnapshots") )
return allow("assign-storage-class 'TimeMachine'");
if ( subpath_prefix("/volumes/.timemachine/${any_uuid}") )
return allow("assign-storage-class 'TimeMachine'");
return allow("assign-storage-class 'TimeMachine'");
return allow("assign-storage-class 'TimeMachine'");
```

## Slide 86

Exploit

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
eee
Exploit
fish@sonomal ~ % diskutil apfs changeVolumeRole disk3s2 clear
fish@sonomal ~
Volume TM on d
fish@sonomal ~
Volume TM on d
fish@sonomal ~
total 8
drwxr-xr-x@ 5 root
-rw-r--r--@ 1 root
fish@sonomal ~ % Ls
total 4373688
staff
% diskutil umount disk3s2
isk3s2 unmounted
% diskutil mount disk3s2
isk3s2 mounted
% ls -l /Volumes/TM/
160 Apr 11 15:02 2024-04-11-150432.previous
staff 563 Apr 11 15:04 backup_manifest.plist
-l /Volumes/TM/2024-04-11-150432.previous/Data/Users/fish
-rw------- + 1 root staff
-rw-r--r--@ 1 fish staff
-rwxrwxrwx+ 1 fish admin
drwxr-xr-x@ 2 fish staff
drwx------ @5 fish staff
drwx------ @ 4 fish staff
Lrwx------ + 1 fish staff
fitzl.csaba@gmail.com
drwx------ @5 fish staff
drwx------ @5 fish staff
drwx------ @5 fish staff
drwxr-xr-x@ 4 fish staff
fish@sonomal ~ % ls
total 8
-rw-r--r--@ 1 fish
14739
3959690
38
64
160
128
66
160
160
160
128
Apr
Jun
Mar
Nov
Mar
Apr
Apr
Feb
Apr
Apr
Oct
10
2
5
7
22
11
11
19
11
11
24
17:51 2.txt
2023
14:
18:
15:
14:
14:
ils}3
14:
14:
224
14
55
56
04
48
46
33
54
54
Apple Service Utility Customer.pkg
AppleServiceUtility
Applications
Desktop
Downloads
Google Drive -> /Users/fish/Library/CloudStorage/GoogleDrive-
Movies
Music
Pictures
Public
Lt /Volumes/TM/2024-04-11-150432.previous/Data/Users/fish/Desktop
staff
12 Dec 13 10:26 secret.txt
—
```

## Slide 87

# Fix

### • can no longer change / clear APFS disk roles

## Slide 88

**Disk Utility LPE**

## Slide 89

Disk Utility meets ASR • asr (Apple Software Restore) - can restore (bit copy) one disk to another

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Disk Utility meets ASR
@ asr (Apple Software Restore) - can restore (bit copy) one disk to another
XPC: com.apple.asr
```

## Slide 90

# problem

• Disk Utility doesn't ask for password • allows a GUI user to restore a disk • exploit: restore a DMG which has a SUID binary

## Slide 91

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@e0e
Internal
¥ © Macintosh HD volumes
v & Macintosh HD
Macintosh HD snapshot
Data
Disk Images
&) RAM Disk
& untitled
’ Disk Utility +)
View Volume
Macintosh HD
APFS Volume Group - APFS (Encrypted)
macOS 14.4.1 (23E224)
® Used ® Other Volumes
3,33 TB 8,06 GB
Mount Point (Read-Only): | Type:
Capacity: 8TB Owners:
Available: 4,66 TB Connection:
Used: 3,33 TB Device:
Snapshot Name: com.apple.os.update-39AFBADD5AD7CDABO00800...
APFS Snapshots on “Data”
Name Date Created
com.apple.TimeMachine.2024-03-22-135416.local 22 Mar 2024 at 13:54
com.apple.TimeMachine.2024-03-26-120916.local Yesterday at 12:09
com.apple.TimeMachine.2024-03-26-185015.local Yesterday at 18:50
©v
15 snapshots
Snapshot UUVID:
db
©
First Aid Partition Erase Restore Unmount Info
SHARED BY 5 VOLUMES
Free
4,66 TB
APFS Volume Group
Disabled
Apple Fabric
disk3s1s1
73781D73-D838-442E-919B-4684B6BE232B
Tidemark Size Kind
4,13 TB 24,03 GB Time Machine Snapshot
4,14TB 62,34 GB Time Machine Snapshot
4,14 TB 63,25 GB Time Machine Snapshot
® High tidemark is 4,14 TB
```

## Slide 92

# **conclusion**

## Slide 93

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
GOOD
MOR-NinG
| SUNSHINE‘...
GB
¢>
ZAHACKERS? :
```

## Slide 94

**_Csaba Fitzl Twitter: @theevilbit_**

## Slide 95

# Icons

• flaticon.com

- kliwir art

- Freepik
