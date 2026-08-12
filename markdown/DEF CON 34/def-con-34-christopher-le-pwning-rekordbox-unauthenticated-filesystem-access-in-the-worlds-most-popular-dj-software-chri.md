---
title: "Pwning Rekordbox Unauthenticated filesystem access in the world's most popular DJ software"
speakers: ["Christopher Le"]
conference: "DEF CON"
conference_full: "DEF CON 34"
edition: "34"
year: null
source_pdf: "DEF CON 34/DEF CON 34 - Christopher Le - Pwning Rekordbox Unauthenticated filesystem access in the world's most popular DJ software - Chris.pdf"
pages: 44
sha256: "f96d437475016ad8d46bf7e4f100738a3e320125c9746b6fc1991c4ad7f5b94c"
text_chars: 11597
ocr_pages: 35
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T00:15:17Z"
---
# Pwning Rekordbox Unauthenticated filesystem access in the world's most popular DJ software

**Speakers:** Christopher Le  
**Conference:** DEF CON 34  
**Source:** `DEF CON 34/DEF CON 34 - Christopher Le - Pwning Rekordbox Unauthenticated filesystem access in the world's most popular DJ software - Chris.pdf` (44 pages)


## Slide 1

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
DEF CON 34
UNAUTHENTICATED FILESYSTEM ACCESS
PWNING REXORDBOX
Unauthenticated filesystem access in the world's most popular DJ software.
BY TRIODE - CHRIS LE x x x x
FRI AUG 7 2026 3:00 PM PDT 20 MIN
```

## Slide 2

## Slide 3

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
| OPENING
ee
Hl, I'M TRIODE
DJ and engineer. | built Now Playing — the overlay that shows
a DJ's current track live on stream.
TRIODE // PWNING REKORDBOX
```

## Slide 4

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
| OPENING
£ NOW PLAYING
It reads the track that's playing and paints it onto the live
stream overlay, in real time.
latest subbed: syfpsy <3 (25 <3 thank vou so muchi! latest follower: wooo_o
Daily subscriber goal: 15/20 (75%) july fund <3 $0/$1,000 (0%) Follower goal: 1767/1200 (98%)
d Mv OBits:5%off  (f Giftasub v mt $Y Subscribe +
m~
yD
e a meowylive @@ Schedule Videos Clips
drum and bass a/\=@ « @=’\n back from rampage/travel and ready 2 party rock !Inextshow !support 2312 © 21029 fh
DJs dr dnb DJ PLUR
TRIODE // PWNING REKORDBOX DEF CON 34: 04
```

## Slide 5

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
| OPENING
PRO DJ LINK™
The protocol AlphaTheta's CDJs use to talk over a network.
James Elliott and Evan Purkhiser reverse-engineered it for
years — I've been contributing.
TRIODE // PWNING REKORDBOX
DEF CON 34:05
```

## Slide 6

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
| OPENING
©
IT HANDS YOUR ENTIRE HARD DRIVE
TO ANYONE ON THE NETWORK.
That's the bug. That's the whole talk.
```

## Slide 7

## Slide 8

## Slide 9

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
| THE SETUP
fF
CC
DESIGNE
CONGU I
TRIODE // PWNING REKORDB
LINK EXPORT MODE
Link the laptop to the CDJs and tracks stream from the laptop.
Convenient — but the moment it’s on, everything your
account can read is exposed to that network.
```

## Slide 10

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
| THE SETUP
ONEFLATSUBNET
Link Export quietly starts an NFS server — a 1989 Unix protocol —
and shares the whole drive, every mounted volume. é SWITCH - ONE SUBNET +)
AN
(eal
ATTACKER
| Guarded by a credential that's published in the open, in multiple open-source
implementations.
TRIODE // PWNING REKORDBOX DEF CON 34
```

## Slide 11

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
| THE SETUP
Original Mix AS oe 2) { Little Lights
55/0 orm xan
= - = O12. oe a .
an 2 |e TS aS a Aer
E: a a ‘ 2 Ie * ck a :
mo a: 1 ‘2 = Pa, ‘
= = — - - Hues
MTOM HHHAT-OP HALPOWER KICK ¢ fa Trampet D Djembe "
ac - eons
HHL SCTRAGH WawAr-CL HIG KICK 120.00 HEE Homsec2.0 SaxScream TakingOram u
aru sv o- >i Sa aa
W blank lst 1B blank lst blank list SB blank lst
Dope-ISHT Fambient 2019 (34 Tracks sssten Pa
11 # Preview wor Track Title Artist Album Genre c Rating Time Key Date Added
bn 4 aanendtn? -mixoutearly Blockhead Free Sweatpan Beats 92.00 kkk! 03:00 Ebm 6122/2
© bea 31 oo Small Moments Above & Beyon Flow State NO Beats 94.80 AkeKTsr 03:58 Fm 6122/2
nt 2020 & bu 7 © a hain Valley of Paradi Psychemagik | Feel How this Beats, Voice 95.00 kek! 09:49 Em 622/2
matzo) a2 ‘Saamadonannitiaamaia® Life's Casino Sounds From T Binary Beats 97.00 ek: 07:24 Dm 6122/2
> enue 32 EB themes =<) Believer-Edit Above & Beyon Flow State NO Beats 97.03 keK IH 02:15 Ebm 622/2
nt2 & Eu 13 Selim, ‘Arizona Momin Kaya Project Ambient Mixes NO Beats 99,00 ekki 07:16 Fim 6722/2
i mu 11 ‘Are You Even Weval The Weight Beats, Voice 107.00 eieksivs 05:11 Fm 6122/2 A omg F 1 .
S baru 33 ‘Are YouEven Weval, TRS-80 The Weight Re Beats 107.00 seks: 04:23 Cm 6722/2 P t 2020 St ll 7.E y DJ h fe| L k
& be 10 Temple of Sor M83 psvit Beals slow 110.00 see xevrs 07:04 Dbm 6122/2 resent sInce . IHIN version /. Ever whos Use In
> tape 9 5 Perpetual Moti Max Cooper Yearning forth Beats 119.00 eiekekY 04:58 Abm e22i2
S pt 3 2 Sakral Prins Thomas Ambitions 119.00 ie 07:35 Om 6722/2
& bso 30 Kyphi Digitalis ‘Seb Taylor: Coll Beats 119.89 tekekeksy 06:43 Fim 6/22/2 E t b th i j fe|
= 27 Panoramic Sti Seb Taylor Seb Teyor.Coll NO Beals «119.04 eH 0206 Gm saz xport, ACrOSS DON Versions, IS Exposed.
( baru 18 5 Shores of Easy Royksopp Shores of Easy Beats 120.00 ekki 13:59 A 62/2
i ue 24 ‘itt Lights Ben Bohmer Breathing Beats 122.99 tekkeee 05:24 Am 62212
ae ol: Moon Scepter Nathan Micay Blue Spring Beats 125.00 weokeet 05:14 Am 6722/2
"5 Under Your Sp Kyau & Albert Under Your Sp Beats, Voice 126.00 wieeIY: 03:14 Abm 62/2
« Love In The Ti Oneohtrix Point KCRW Session Beats 128.01 eke 04:23 Em 6212
Ec Vanity Lise! Angels on the Beats, Voice 130.00 kkekHY 02:41 G 62212
Lovesong-Po Max Cooper, P One Hundred B Beats-slow 133.00 wieskiiyr 06:26 E 6722/2
Chimera Psychemagik | Feel How this Beats 145.92 okie! 04:08 Dm 61212
TRIODE | PWNING REKORDE DEF N 34
```

## Slide 12

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
| THE SETUP
IN THE TIME IT
TAKES 10 ORDER A
DRINK
That's how fast you can pull this off.
TRIODE // PWNING REKORDBOX DEF N 34:12
```

## Slide 13

## Slide 14

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
| PROTOCOL INTERNALS
@ @ @ @ @
BORN IN 1989 = | |
@ @ @ e
When rekordbox enters export mode it stands up three services ° . . ° .
over RPC — Remote Procedure Call. . . ° . .
@ @ @ @ e
@ @ e e @
@ @ e @ @
@ @ @ @ e
TRIODE // PWNING REKORDBOX DEF CON 34:14
```

## Slide 15

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
| PROTOCOL INTERNALS
THREE SERVICES
01 PORTMAPPER — UDP 50111
XXX
Not the standard 11]; AlphaTheta moved it. A directory: ‘where's the NFS server?’
02 ‘Mount the C drive. It hands back a file handle — a session token for that volume.
03 NFSv2 — PORT 2049
The real file access. Present the handle, give a path, get the file back.
```

## Slide 16

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
| PROTOCOL INTERNALS
ONE IViAGIC VALUE
All three are guarded by a constant in a Unix auth header —
hardcoded into the firmware of every PRO DJ LINK™ model.
| Known to the community for years: crate-digger, prolink-connect,
alphatheta-connect.
TRIODE // PWNING REKORDBOX DEF CON 34: 16
```

## Slide 17

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
| PROTOCOL INTERNALS
THE HANDSHAKE
“Hi, lm a caller with the well-known constant.” rekordbox: “Great,
DEVICE ACCESS GRANTED REKORDBOX youre a CDJ. Here's your access.”
O-r
Vv
"N
TRIODE // PWNING REKORDBOX DEF CON 34:17
```

## Slide 18

## Slide 19

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Botue Buc
PATH TRAVERSAL
IT DOESN'T RESTRICT ae
DATA EXFILTRATION:
CONFIDENTIAL FILES RETRIEVED
PATHS —— arose
read JVM nome/user/.ssh/id_rsa = = a,
rekordbox never limits what file paths you can read. Every file, | J
; | SSH PRIVATE
every volume the user can reach is readable. ATTACKER INPUT: KEY STOLEN
CLIMBING DIRECTORIES
```

## Slide 20

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Botue Buc
YOU DON'T EVEN
=“ HAVE 10 BE A COU
Just a device on the same subnet that says the magic words. It
NOT A CDJ
\ ®) could be anything — a compromised camera, for example.
ONE SUBNET
```

## Slide 21

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Botue Buc
THE CONFUSED
DEPUTY ATTACKER NFS SERVER YOUR DRIVE
PUBLIC CREDENTIAL THE DEPUTY RUNS AS YOU
rekordbox runs as you, so it reads every file you own. The NFS
server is the deputy holding that power — and the attacker
borrows it with a public credential.
TRIODE // PWNING REKORDB DEF < N34:2
```

## Slide 22

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Botue Buc
AUTH ISN'T BROKEN.
SCOPE IS.
Authentication works exactly as designed. The design just assumed only CDJs would ever be on this network.
```

## Slide 23

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Botue Buc
WHAT IT GETS YOU
Anything you can read, the attacker can read — over the
network.
TRIODE
/| PWNING REKORDBOX
D
SSH KEYS
DOCUMENTS
CLOUD TOKENS
```

## Slide 24

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Botue Buc
Ka ee ee eT
mins
Bounce [| prov > - inal
| aa =
& = > Above The Cloud (Original Mix) BEAT KEY BEAT
use 08:45 128.0 Fim » Loop SHIFT JUMP
0) 00 ==; 00:0000 -00.00. 100: a
a ao o ,
—— J en a. ae ween co oan MP3/AAC/ WAV,
os | 3 ' 7 7 7 rT F#m AIFF/FLAC/ALAC
VINYL SPEED ADJ
HOT CUE
AND DUS?
YOUR IDs.
Your playlists and your private collection of tracks.
| Mac, Windows, CDJ/XDJ hardware, iOS & Android — anything that speaks PRO
DJ LINK™ runs this.
```

## Slide 25

## Slide 26

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
| THE DEMO
-
RECORDED DEMO
O01 rekordbox running normally — Link Export on
02 Attacker terminal — 16 seconds to plaintext
O03  Pointit at a CDJ — read the library
RECORDED PRE-TALK rekordbox 7.x
TRIODE // PWNING REKORDBOX DEF CON 34: 26
```

## Slide 27

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
| THE DEMO
AlphaTheta has worked closely with me through the whole
process. Software is done; firmware is a bigger lift across that YS See) 22 SS UCI alel cle Vv FIXED
WHERE IT STANDS w2=-wems
many models.
CDJ / XDJ firmware C IN PROGRESS )
TRIODE // PWNING REKORDBOX DEF CON 34: 27
```

## Slide 28

## Slide 29

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
| WHY THE FIX
THE OBVIOUS FIX
Harden the auth — make the credential strong and secret,
something AlphaTheta controls. But | dont think they can.
TRIODE // PWNING REKORDBOX DEF CON 34: 29
```

## Slide 30

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
| WHY THE FIX
AS A)
«2 FROZEN SINCE 2009
The constant is burned into every PRO DJ LINK™ model since the
HARDCODED CDJ-2000. AlphaTheta holds ~60% of the market — feels like
100% in the booth.
abated eta t ata
TRIODE // PWNING REKORDBOX DEF ON 34: 30
```

## Slide 31

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
| WHY THE FIX
INSTALLED FOR A
DECADE
Booths get bolted in and run for years. Demand a new
credential and every older CDJ instantly stops loading.
TRIODE // PWNING REKORDBOX
DEF CON 34: 3
```

## Slide 32

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
| WHY THE FIX
THAT KILLS THE
+ moco et PARTY.
So it's off the table.
HOT CUE
B c D — i J
TRIODE // PWNING REKORDBOX DEF CON 34
```

## Slide 33

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
| WHY THE FIX
20 YEARS OF UNBROKEN
BACKWARDS COMPATIBILITY.
A set prepped today plays on a CDJ-1000 from 2001. That's genuinely hard — and it freezes the handshake in
place.
©)
```

## Slide 34

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
| WHY THE FIX
a -€ a . = 4 = ry j- oo
SHRINK THE SCOPE ..
Keep accepting the constant. Change ‘read the whole SSH DOCS LIBRARY KEYS | CLOUD
filesystem’ to ‘read only the library folders. Least privilege. —_ eT
| The deputy’s password was never weak — it just held way too much power.
TRIODE // PWNING REKORDBOX DEF CON 34: 34
```

## Slide 35

## Slide 36

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
| THE DISCLOSURE
COOINMVMYARWNE
B
S
11
12
13
14
ls)
16
Building Now Playing 8, pulling metadata over NFS, | realized | 20
could point at any path | wanted. ‘Wait — you shouldn't be 23
able to do that. *
TRIODE // PWNING REKORDB
#!/usr/bin/env python3
rekordbox NFS filesystem browser
Demonstrates that rekordbox exposes the entire host filesystem over NFS
with no meaningful authentication. Any device on the local network can
read any file on any mounted drive.
USAGE
python3 rekordbox_nfs.py <rekordbox—ip>
python3 rekordbox_nfs.py <rekordbox—ip> --exports
python3 rekordbox_nfs.py <rekordbox—ip> —-\s
python3 rekordbox_nfs.py <rekordbox—ip> —-ls "Users/chris/Music"
python3 rekordbox_nfs.py <rekordbox—ip> --read "Users/chris/hello. txt"
python3 rekordbox_nfs.py <rekordbox-ip> --drive D --ls
REKORDBOX SETUP
1. Open rekordbox on the target machine (macOS or Windows) and in Export mode.
2. Have any Pro DJ Link-compatible device connected to the same network and
powered on. This is required so the Link Export button appears in Rekordbox.
3. Find the target machine's IP address:
- macO0S: System Settings > Network, or run ‘ifconfig end
- Windows: Settings > Network, or run ‘ipconfig*
4. Run this script with that IP address.
HOW IT WORKS
DEF CON 34
36
```

## Slide 37

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
| THE DISCLOSURE
MY FIRST WORRY (osteo)
WAS US (+ prolink-connect )
+ alphatheta-connect )
A small community builds genuinely cool things on
reverse-engineered PRO DJ LINK™.| worried a report might make ;
+. Now Playing
AlphaTheta lock NFS down and shut us out.
```

## Slide 38

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
| THE DISCLOSURE
| ASKED JAMES
ELLIOTT
Author of crate-digger, the canonical open-source
implementation. We landed in the same place: the flaw is real,
and protecting our own access wasn't reason enough to sit
on it.
TRIODE // PWNING REKORDBOX DEF CON 34: 38
```

## Slide 39

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
| THE DISCLOSURE
A WARM INTRO
Within 48 hours | was talking to Koushi Kashiwada, who leads
rekordbox product planning. Responsive, friendly, professional
the whole way.
JAMES ELLIOTT ALPHATHETA
IJ No bug bounty — but a DJM-V10 would be nice. (Mostly joking.)
TRIODE // PWNING REKORDBOX DEF CON 34: 39
```

## Slide 40

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
| THE DISCLOSURE
] 2
) 7
G) 12
16 17
21 22
13
18
23
14
19
24
10
15
20
25
TRIODE // PWNING REKORDBOX
90 DAYS — JUNE 1
They asked for more time to fix the rest of the lineup, and |
extended it. Transparent and collaborative throughout.
DEF CON 34
40
```

## Slide 41

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
| THE DISCLOSURE
IN THE (WIEANTIME
Worried DJ? Don't bring your laptop on stage 10 minutes
before your set. Bring a USB stick like a professional.
TRIODE // PWNING REKORDBOX
DEF CON 34: 41
```

## Slide 42

## Slide 43

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Bclose
THAT'S THE BUG
NFS, a hardcoded magic number, and a scope nobody ever
locked down. Sitting there for 20 years.
TRIODE // PWNING REKORDBOX DEF N 4 1
```

## Slide 44

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
THANK YOU
Catch anyone's laptop open while I'm on tonight? I'm cutting the music.
TONIGHT — LIVE AS TRIODE (+)
SAHARA STAGE
+ OFFICIAL DEF CON PARTY xXxxKxKXKX
@TRIODE
```
