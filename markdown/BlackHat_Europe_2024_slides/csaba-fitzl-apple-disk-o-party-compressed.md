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
text_chars: 16979
ocr_pages: 62
has_ocr: true
redacted_secrets: 0
ocr_confidence: 82.0
ocr_unreliable_blocks: 0
vision_verified_blocks: 1
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T04:57:27Z"
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


> Recovered by OCR — confidence 88/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

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


> Recovered by OCR — confidence 77/100 on the text kept, 61/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
diskarbitrationd - mount call flow
DAServerSessionQueueRequest > DAQueueRequest
> DAAuthorize
checks “sandbox
and privilege)
- permissions
```

## Slide 9

# **CVE-2023-42838 - Sandbox Escape**

## Slide 10

Where is the problem?


> Recovered by OCR — confidence 86/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Where is the problem?
eee csaby — -zsh — 80x24
Last login: Thu Apr 7 16:08:31 on ttys@@1
csaby@monty ~ % touch /Users/Shared/sandboxescape.txt
‘csaby@monty ~ % mount
/dev/disk4sis1 on / (apfs, sealed, local, read-only, jo
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
aled, nobrowse)
, Nobrowse, protect)
/dev/disk2s3
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


> Recovered by OCR — confidence 90/100 on the text kept, 63/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
CVE-2023-42838 - what goes on?
add quarantine Flag mount option
```

## Slide 14

how to get a /dev/disk in Sandbox?


> Recovered by OCR — confidence 85/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
how to get a /dev/disk in Sandbox?
unmount /dev/diskxsY
using diskarbitrationd
API
\
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


> Recovered by OCR — confidence 83/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
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


> Recovered by OCR — confidence 87/100 on the text kept, 57/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
OPERATION
env: user
disk owner: root
mount
```

## Slide 21


> Recovered by OCR — confidence 86/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
env: user
disk owner: root
```

## Slide 22


> Recovered by OCR — confidence 85/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
OPERATION
env: user
IHearget owner: coot
disk owner: root
FAIL!!! user has no rights over target
```

## Slide 23

# call flow 2.: mount with diskarbitrationd

## Slide 24


> Recovered by OCR — confidence 80/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
=
xu checks:
- classic user
; POSIX permissions
might be sandboxed rung as root + unsandboxed runs as disk owner - MAC £ allout
CUNS AS X
diskarbitrationd checks:
- if calling user id == cisk owner il
```

## Slide 25

## case study: + diskarbitrationd + mount over root owned dir with user

## Slide 26


> Recovered by OCR — confidence 85/100 on the text kept, 69/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
OPERATION
env: user
target owner: root
\< disk owner: root
mount
```

## Slide 27


> Recovered by OCR — confidence 75/100 on the text kept, 72/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
OPERATION
env: user
target owner: root
disk owner: root
FALL!!! user [= root
```

## Slide 28


> Recovered by OCR — confidence 80/100 on the text kept, 62/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
OPERATION
env: user
target owner: coot
\< disk owner: user
mount
```

## Slide 29


> Recovered by OCR — confidence 85/100 on the text kept, 64/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
OPERATION
eriv: user
target owner: root
disk owner: user
mount
```

## Slide 30


> Recovered by OCR — confidence 81/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
target owner: root
disk owner: user
```

## Slide 31


> Recovered by OCR — confidence 75/100 on the text kept, 72/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
OPERATION
env: user
target owner: coot
disk owner: user
FAIL!!! user [= root
```

## Slide 32

## case study: + diskarbitrationd + attack diskarbitrationd with symlink

## Slide 33


> Recovered by OCR — confidence 79/100 on the text kept, 70/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
fOPERATION
env: user
target: link ->
/tmo/ mnt
target owner: user
\cisk owner: user
```

## Slide 34


> Recovered by OCR — confidence 88/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
fOPERATION
env: user
target: link ->
target owner: user
isk owner: user
```

## Slide 35


> Recovered by OCR — confidence 84/100 on the text kept, 68/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
mount -k
fOPERATION
env: user
target: link ->
target owner: user
\cisk owner: user
```

## Slide 36


> Recovered by OCR — confidence 82/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
fOPERATION
env: user
target: link ->
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


> Recovered by OCR — confidence 86/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
CVE-2024
@e user ID / owner / etc is not
passed
returnValue = [FSKitDiskArbHelper DAMountUserFSVolume: fsType
mountPoint:mountpoint
volumeName LumeName
@ always run as root
Subtree: 5
launchd
xpeproxy
fskitd
fskitd
mount_lifs
175 - theory
Event Facts
Event details
Endpoint Security message details
+ Event type: © ES_EVENT_TYPE_NOTIFY_EXEC
Message timestamp: 2024-08-@5T15:24:43.539Z
Initiating user: root (0)
Process execute details
User: root (@)
+ Process nami mount_lifs -PID: 1015 -GID: 1010
+ Process path: /sbin/mount_lifs
+ Command line:
/sbin/mount_lifs
rsize=524288,wsiz 5536, readahead=4, dsize=65536, actimeo=10, nodev, noowners, nosuid, noatime, fh=0
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


> Recovered by OCR — confidence 87/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
CVE-2024-44175 exploitation
user: root
mountpoint:
link -> not_ok_place
user: root
link -> not_ok_place
user. user
link -> ok_place
user. user
link -> ok_place
```

## Slide 42

weaponization for LPE


> Recovered by OCR — confidence 78/100 on the text kept, 56/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
mount over
/etc/cups >
\
drop
Errorlog /etc/sudoers.d/lpe
weaponization tor LPE
create file rN
7 edit
edit
1) /ete/sudoers.d/lpe
2) cups-Files.conf
/
/
LogFilePerm 700
```

## Slide 43

weaponization for SB escape


> Recovered by OCR — confidence 90/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
weaponization for SB escape
mount over
~/Library/Preferences
run "/bin/zsh ~/Library/Preferences/lpe.sh"
shell script to achieve LPE
CommandString:
/bin/zsh ~/Library/Preferences/lpe.sh
```

## Slide 44


> Recovered by OCR — confidence 75/100 on the text kept, 65/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
@ Finder File Edit View Go Window’ Help oO Q S ThuOct3 22:49
DAUserFSSbxLPE
— i DAUserFSSbxLPE.zip
2. Applicati... Desktop
® Downloads
{} Documents Movies
© Downloads BB Music
© iCloud Dri...
Guest
```

## Slide 45

# CVE-2024-44175 fix • "nofollow" is added to every mount -> no symlinks • fskitd gets the original requestor and executes mount with that user

## Slide 46

## **CVE-2024-40855- Sandbox Escape & TCC Bypass (directory traversal)**

## Slide 47


> Recovered by OCR — confidence 82/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
mu checks:
- classic user
crUunS aS X - MAC callout
might be sandboxed
runs as root + unsandboxedl
diskarbitrationd checks:
- if calling user id == disk owner id
```

## Slide 48


> Recovered by OCR — confidence 79/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
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


> Recovered by OCR — confidence 89/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ADiskMountWithArqunentsCommon AServerSessionQueueRequest
FURLCreat eFromFileSyste:
realoath epresentation
- removes ../ - removes ../ - removes ../
- resolves symlink - resolves symlink
- resolves symlink
FINAL RESOLUTION!!
ONLY FOR THE TIME OF
THE PATH IS UNCHANGED ==> placing a symlink
will cause it to fail at xnu
```

## Slide 50


> Recovered by OCR — confidence 86/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
AServerSessionQueueRequest
FURLCreateFromFileSystemRepresentation
CFURL Qe: eFromFileSystemRepresentation sandbox_checkby_audit_token
- removes ../ - removes ../
- remove - resolves symlink - resolves symlink
- resolv,
UNDER CALLER CONTROL ==> ../ will remain till the end
```

## Slide 51


> Recovered by OCR — confidence 76/100 on the text kept, 63/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
OPERATION
dic -> / erivate/tme/’ 1/2/73
esolved path: NA
```

## Slide 52


> Recovered by OCR — confidence 68/100 on the text kept, 58/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
OPERATION
dic -> / erivate/tme/ 1/2/73
```

## Slide 53

## Slide 54


> Recovered by OCR — confidence 81/100 on the text kept, 60/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
OPERATION
dir
esolvedt path: NA
```

## Slide 55


> Recovered by OCR — confidence 67/100 on the text kept, 67/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
OPERATION
target: vA erivate/ tmo/ dic/../../../Users/crab/ Libracy/ Application Support / com.apple.TC C
dir Gnot a symlink)
esolved path: /Users/erab/ Library/, Application Support / com.apple.TC c/
```

## Slide 56


> Recovered by OCR — confidence 78/100 on the text kept, 73/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
@ Terminal Shell Edit View Window Help k
Q $$ MonJun3 8:14
e@ OD crab — -zsh — 80x24 oO 8 Ci}
crab@see ~ % codesign -dv --entitlements - /Applications/DADirTraverse. appl} =]
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
FaceTime
=) Find My
W Font Book
DADirTraverse
Application - 143 KB
Information
@
```

## Slide 57

the fix


> Recovered by OCR — confidence 78/100 on the text kept, 72/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
the fix
AServerSessionQueueRequest
FURLC reateFromFileSystemRepresentation
sandlbox_checkby_audit_t oken
- removes ./ - removes ./ - removes J
- resolves symlink - resolves symlink - resolves symlink
PERSISTENT!! ONLY FOR THE TIME OF CHECK! FINAL RESOLUTION!
```

## Slide 58

the fix


> Recovered by OCR — confidence 81/100 on the text kept, 59/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
the Tix
diskarbitrationd
! no path \
\ resolution /
set?
yes
resolve path
disallow symlink
sandbox check . and ../ in path
```

## Slide 59

# **CVE-2024-27848 - LPE via StorageKit**

## Slide 60


> Recovered by OCR — confidence 86/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
runs as X runs as the disk owner
might be sandboxed \
lassie us rmissions
g user id == disk owner id
runs as root + unsancdboxed
storagekite chee
```

## Slide 61


> Recovered by OCR — confidence 82/100 on the text kept, 73/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
(OPERATION
env: user
target owner: root
(disk owner: root
\
diskarbitrationd
```

## Slide 62


> Recovered by OCR — confidence 88/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
env: user
target owner: root
disk owner: root
diskarbitrationd
```

## Slide 63


> Recovered by OCR — confidence 82/100 on the text kept, 70/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
\
env: user
target owner: coot
disk owner: root
diskarbitrationd
```

## Slide 64


> Recovered by OCR — confidence 86/100 on the text kept, 63/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
\
ass
target owner: root
disk owner: root
```

## Slide 65


> Recovered by OCR — confidence 83/100 on the text kept, 66/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
eriv: coot
target owner: coot
\
diskarbitrationd
```

## Slide 66


> Recovered by OCR — confidence 75/100 on the text kept, 66/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
> target ower: root
disk owner: root
\
diskarbitrationd
```

## Slide 67


> Recovered by OCR — confidence 71/100 on the text kept, 63/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
@ = Terminal Shell Edit View Window Help G Me wto) Q $$ Wed Mar 27 14:39
OD fish — -zsh — 112x35, m
Last login: Wed Mar 27 12:36:22 on ttysee2
fish@sonomal ~ %
```

## Slide 68

## **CVE-2024-44210 - Bypass CVE-2024-27848 - LPE + TCC bypass via StorageKit**

## Slide 69


> Recovered by OCR — confidence 84/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
runs as X runs as the disk owner
might be sandboxed \
xnu checks:
- classic user POSIX permissions
- MAC callout
CUunNS AS caller
diskarbitrationd
runs as root + unsandboxed
diskarbitrationd checks:
- if calling user id == disk owner id
- sandbox _check
storagekite checks:
- sandbox _check
- target dic id == caller id
runs as root + unsandboxed
```

## Slide 70


> Recovered by OCR — confidence 89/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
1. stat Cuserid) check on target dir
Csome time passes)
2. call diskarbitrationd with target dir
target: /tme/mnt
```

## Slide 71


> Recovered by OCR — confidence 79/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
target: /tmp/link ( alternate symlink
Jete/ cups
1. stat Cuserid) check on /tmo/mnt
Csome time passes)
2. call diskarbitrationd with Jete/cups
target: Jete/ CUPS
```

## Slide 72


> Recovered by OCR — confidence 73/100 on the text kept, 65/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
THE ATT Ac K A Jt mpe/mnt
target: /tmo/ link alternate symlink
~/ Library/, Application Support / com.apple.TC Cc
1. sandbox _cheek on Jtmo/ mnt
Csome time passes)
2. call diskarbitrationd with
```

## Slide 73


> Recovered by OCR — confidence 79/100 on the text kept, 70/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
(OPERATION
env: user
/tmp/link owner: ??
(disk owner: root
\
diskarbitrationd
```

## Slide 74


> Recovered by OCR — confidence 82/100 on the text kept, 73/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
(OPERATION
env: user
Jtmp/| link owner: ??
disk owner: root
diskarbitrationd
```

## Slide 75


> Recovered by OCR — confidence 84/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
\
(OPERATION
env: user
Jtmp/ mnt owner: user
disk owner: root
diskarbitrationd
```

## Slide 76


> Recovered by OCR — confidence 81/100 on the text kept, 57/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
\
Jete/cups owner:
disk owner: root
```

## Slide 77


> Recovered by OCR — confidence 74/100 on the text kept, 67/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
(OPERATION
/ ete/cups owner: root
disk owner: root
\
diskarbitrationd
```

## Slide 78


> Recovered by OCR — confidence 79/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
(OPERATION
eriv: coot
Jetc/cups owner: root
disk owner: root
diskarbitrationd
\
```

## Slide 79


> Recovered by OCR — confidence 83/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
@ Terminal Shell Edit View Window Help Q ®& FriMay 24 6:42
@ OD crab — -zsh — 130x43
crab@see ~ % swW_vers =]
ProductName: macOS
ProductVersion: 14.5
BuildVersion: 23F79
crab@see ~ % ff
6 2
tartup Snapshot - APFS 62,83 GB
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


> Recovered by OCR — confidence 86/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

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
62,83 GB
40,21 GB (541,7 MB purgeable)
10,26 GB
Snapshot Name: com.apple.os.update-4F9A570DA7279961C47EEA2...
-zsh
Type:
Owners:
Connection:
Device:
Snapshot UUID: 8E508755-'
-zsh an
APFS Startup Snapshot
Disabled
Unknown
591C-4B27-ACOC-91E8E9BA4D45
```

## Slide 81

the ultimate fix


> Recovered by OCR — confidence 83/100 on the text kept, 69/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
the ultimate Tix
(— diskarbitrationd
-
storegakitd DAQueueRequest
-
-
-
is kDADiskMountOptionWoFollow
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


> Recovered by OCR — confidence 82/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

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
Q06B16FBF408 e X — XART (hardware security)
APFS Volume Disk (Role): disk3s2 (Backup) eH - Hardware
Name: . TM (Case-sensitive) e CC - Sidecar (Time Machine)
Mount Point: /Volumes/TM
Capacity Consumed: 3737165824 B (3.7 GB) 6 Ve BRGREREEES CARE
Sealed: No
FileVault: No (Encrypted at rest)
```

## Slide 85

SIP (Sandbox Platform Profile)


> Recovered by OCR — confidence 79/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

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


> Recovered by OCR — confidence 91/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
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
14:
14:
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


> Recovered by OCR — confidence 91/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Disk Utility meets ASR
@ asr (Apple Software Restore) - can restore (bit copy) one disk to another
XPC: com.apple.asr
```

## Slide 90

# problem

• Disk Utility doesn't ask for password • allows a GUI user to restore a disk • exploit: restore a DMG which has a SUID binary

## Slide 91


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 90/100 on the text kept, 84/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Internal
  Macintosh HD  volumes
    Macintosh HD
      Macintosh HD  snapshot
      Data
Disk Images
  RAM Disk
  untitled

View   Disk Utility                              Volume  First Aid  Partition  Erase  Restore  Unmount  Info

Macintosh HD
APFS Volume Group • APFS (Encrypted)
macOS 14.4.1 (23E224)                                                        8 TB
                                                                   SHARED BY 5 VOLUMES

Used          Other Volumes         Free
3,33 TB         8,06 GB               4,66 TB

Mount Point (Read-Only):     /            Type:                    APFS Volume Group
Capacity:                  8 TB           Owners:                  Disabled
Available:               4,66 TB          Connection:              Apple Fabric
Used:                    3,33 TB          Device:                  disk3s1s1
Snapshot Name: com.apple.os.update-39AFBADD5AD7CDAB000800...   Snapshot UUID:  73781D73-D838-442E-919B-4684B6BE232B

APFS Snapshots on "Data"

Name                                              Date Created            Tidemark   Size       Kind
com.apple.TimeMachine.2024-03-22-135416.local     22 Mar 2024 at 13:54    4,13 TB    24,03 GB   Time Machine Snapshot
com.apple.TimeMachine.2024-03-26-120916.local     Yesterday at 12:09      4,14 TB    62,34 GB   Time Machine Snapshot
com.apple.TimeMachine.2024-03-26-185015.local     Yesterday at 18:50      4,14 TB    63,25 GB   Time Machine Snapshot

15 snapshots                                                    High tidemark is 4,14 TB
```

## Slide 92

# **conclusion**

## Slide 93

## Slide 94

**_Csaba Fitzl Twitter: @theevilbit_**

## Slide 95

# Icons

• flaticon.com

- kliwir art

- Freepik
