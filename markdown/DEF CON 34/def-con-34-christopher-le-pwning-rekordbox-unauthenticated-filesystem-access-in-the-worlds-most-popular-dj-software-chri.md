---
title: "Pwning Rekordbox Unauthenticated filesystem access in the world's most popular DJ software"
speakers: ["Christopher Le"]
conference: "DEF CON"
conference_full: "DEF CON 34"
edition: "34"
year: 2026
source_pdf: "DEF CON 34/DEF CON 34 - Christopher Le - Pwning Rekordbox Unauthenticated filesystem access in the world's most popular DJ software - Chris.pdf"
pages: 44
sha256: "f96d437475016ad8d46bf7e4f100738a3e320125c9746b6fc1991c4ad7f5b94c"
text_chars: 9957
ocr_pages: 35
has_ocr: true
redacted_secrets: 0
ocr_confidence: 89.5
ocr_unreliable_blocks: 0
vision_verified_pages_changed: 39
vision_verified_pages: 44
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T06:24:50Z"
---
# Pwning Rekordbox Unauthenticated filesystem access in the world's most popular DJ software

**Speakers:** Christopher Le  
**Conference:** DEF CON 34  
**Source:** `DEF CON 34/DEF CON 34 - Christopher Le - Pwning Rekordbox Unauthenticated filesystem access in the world's most popular DJ software - Chris.pdf` (44 pages)


## Slide 1

DEF CON 34
UNAUTHENTICATED FILESYSTEM ACCESS

# PWNING REKORDBOX

Unauthenticated filesystem access in the world's most popular DJ software.

**BY TRIODE · CHRIS LE**
FRI AUG 7 2026 · 3:00 PM PDT · 20 MIN

## Slide 2

SECTION 01

# OPENING

## Slide 3

OPENING

#### HI, I'M TRIODE

DJ and engineer. I built Now Playing — the overlay that shows a DJ's current track live on stream.

## Slide 4

OPENING

#### NOW PLAYING

It reads the track that's playing and paints it onto the live stream overlay, in real time.

The screenshot shows a stream overlay reading "Rhyme Dust (Dimension Extended Remix" / "MK & Dom Dolla" — the same text highlighted twice, once in a preview box and once live in the corner of the stream. The stream is meowylive's, with on-screen stats: daily subscriber goal 15/20 (75%), july fund <3 $0/$1,000 (0%), follower goal 11767/12000 (98%), latest subbed syfpsy <3, latest follower wooo_o. Title: "drum and bass ... back from rampage/travel and ready 2 party rock !nextshow !support," 312 viewers, 2:10:29 elapsed, tags DJs / drumandbass / dnb / ravebae / DJ / English / PLUR.

## Slide 5


> Recovered by OCR — confidence 91/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

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


> Recovered by OCR — confidence 93/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
| OPENING
IT HANDS YOUR ENTIRE HARD DRIVE
TO ANYONE ON THE NETWORK.
That's the bug. That's the whole talk.
```

## Slide 7

SECTION 02

# THE SETUP

## Slide 8

## Slide 9

THE SETUP

#### LINK EXPORT MODE

Link the laptop to the CDJs and tracks stream from the laptop. Convenient — but the moment it's on, everything your account can read is exposed to that network.

Photo: a close-up of a CDJ's rear-panel LINK port, beside a partial bilingual regulatory label reading "CD...", "DESIGNE...", "CONÇU F..." (cropped at the edge of the photo).

## Slide 10

THE SETUP

#### ONE FLAT SUBNET

Link Export quietly starts an NFS server — a 1989 Unix protocol — and shares the whole drive, every mounted volume.

Guarded by a credential that's published in the open, in multiple open-source implementations.

A diagram shows a laptop (tagged NFS) and two CDJs all connected to a switch labeled "SWITCH · ONE SUBNET." Below the switch, an arrow points down to a box labeled ATTACKER.

## Slide 11

THE SETUP

#### SINCE REKORDBOX 6

Present since 2020. Still in version 7. Every DJ who's used Link Export, across both versions, is exposed.

A rekordbox screenshot: two decks loaded, "Original Mix" (126.00 Abm) on the left and "Little Lights" by Ben Böhmer (122.99 Am) on the right, waveform and effects panels above, and a track browser below showing the playlist "Dope-ISHT Fambient 2019 (34 Tracks" (sidebar playlists partly visible: "...ent 2020," "...ent 2019," "...ent 2018," "...low"):

| # | Track Title | Artist | Album | Genre | BPM | Time | Key |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 14 | -mix out early | Blockhead | Free Sweatpan | Beats | 92.00 | 03:00 | Ebm |
| 31 | Small Moments | Above & Beyon | Flow State | NO Beats | 94.80 | 03:58 | Fm |
| 7 | Valley of Paradi | Psychemagik | I Feel How this | Beats, Voice | 95.00 | 09:49 | Em |
| 2 | Life's Casino | Sounds From T | Binary | Beats | 97.00 | 07:24 | Dm |
| 32 | Believer - Edit | Above & Beyon | Flow State | NO Beats | 97.03 | 02:15 | Ebm |
| 13 | Arizona Mornin | Kaya Project | Ambient Mixes | NO Beats | 99.00 | 07:16 | F#m |
| 11 | Are You Even | Weval | The Weight | Beats, Voice | 107.00 | 05:11 | Fm |
| 33 | Are You Even | Weval, TRS-80 | The Weight Re | Beats | 107.00 | 04:23 | Cm |
| 10 | Temple of Sorr | M83 | DSVII | Beats -slow | 110.00 | 07:04 | Dbm |
| 9 | Perpetual Moti | Max Cooper | Yearning for th | Beats | 119.00 | 04:58 | Abm |
| 3 | Sakral | Prins Thomas | Ambitions | — | 119.00 | 07:35 | Cm |
| 30 | Kyphi | Digitalis | Seb Taylor: Coll | Beats | 119.89 | 06:43 | F#m |
| 27 | Panoramic Stri | Seb Taylor | Seb Taylor: Coll | NO Beats | 119.94 | 02:06 | Gm |
| 18 | Shores of Easy | Royksopp | Shores of Easy | Beats | 120.00 | 13:59 | A |
| 24 | Little Lights | Ben Böhmer | Breathing | Beats | 122.99 | 05:24 | Am |
| 4 | Moon Scepter | Nathan Micay | Blue Spring | Beats | 125.00 | 05:14 | Am |
| 19 | Under Your Sp | Kyau & Albert | Under Your Sp | Beats, Voice | 126.00 | 03:14 | Abm |
| 17 | Love In The Ti | Oneohtrix Point | KCRW Session | Beats | 128.01 | 04:23 | Em |
| 23 | Vanity | Lisel | Angels on the | Beats, Voice | 130.00 | 02:41 | G |
| 28 | Lovesong - Po | Max Cooper, P | One Hundred B | Beats -slow | 133.00 | 06:26 | E |
| 8 | Chimera | Psychemagik | I Feel How this | Beats | 145.92 | 04:08 | Dm |

(Rating and "Date Added" columns are also visible; every row's Date Added reads "6/22," cropped at the panel edge.)

## Slide 12

THE SETUP

#### IN THE TIME IT TAKES TO ORDER A DRINK

That's how fast you can pull this off.

## Slide 13

SECTION 03

# PROTOCOL INTERNALS

## Slide 14

PROTOCOL INTERNALS

#### BORN IN 1989

When rekordbox enters export mode it stands up three services over RPC — Remote Procedure Call.

Decoration: five columns of small rack-style bars, a few highlighted in orange, above a tag reading "1989."

## Slide 15

PROTOCOL INTERNALS

#### THREE SERVICES

- **01 PORTMAPPER — UDP 50111** — Not the standard 111; AlphaTheta moved it. A directory: 'where's the NFS server?'
- **02 MOUNTD** — 'Mount the C drive.' It hands back a file handle — a session token for that volume.
- **03 NFSv2 — PORT 2049** — The real file access. Present the handle, give a path, get the file back.

## Slide 16

PROTOCOL INTERNALS

#### ONE MAGIC VALUE

All three are guarded by a constant in a Unix auth header — hardcoded into the firmware of every PRO DJ LINK™ model.

Known to the community for years: crate-digger, prolink-connect, alphatheta-connect.

Photo: a teardown of a CDJ unit, its case open to show the internal circuit boards and ribbon cables.

## Slide 17

PROTOCOL INTERNALS

#### THE HANDSHAKE

"Hi, I'm a caller with the well-known constant." rekordbox: "Great, you're a CDJ. Here's your access."

A diagram shows DEVICE sending `0xDEADBEEF` to REKORDBOX, which replies ACCESS GRANTED (with a key icon).

## Slide 18

SECTION 04

# THE BUG: SCOPE, NOT AUTH

## Slide 19

THE BUG

#### IT DOESN'T RESTRICT PATHS

rekordbox never limits what file paths you can read. Every file, every volume the user can reach is readable.

A diagram titled "PATH TRAVERSAL — UNRESTRICTED FILE READ" shows a terminal-style box reading:

```text
read /../././../home/user/.ssh/id_rsa
```

The traversal portion is highlighted and labeled "ATTACKER INPUT: CLIMBING DIRECTORIES." An arrow leads to four file icons (the last marked with a key) labeled "DATA EXFILTRATION: CONFIDENTIAL FILES RETRIEVED" and "SSH PRIVATE KEY STOLEN."

## Slide 20

THE BUG

#### YOU DON'T EVEN HAVE TO BE A CDJ

Just a device on the same subnet that says the magic words. It could be anything — a compromised camera, for example.

A diagram shows a security camera, labeled "NOT A CDJ," broadcasting `0xDEADBEEF`, connected down to a line labeled "ONE SUBNET."

## Slide 21

THE BUG

#### THE CONFUSED DEPUTY

rekordbox runs as you, so it reads every file you own. The NFS server is the deputy holding that power — and the attacker borrows it with a public credential.

A diagram shows ATTACKER (public credential) → NFS SERVER (the deputy) → YOUR DRIVE (runs as you).

## Slide 22

THE BUG

#### AUTH ISN'T BROKEN. SCOPE IS.

Authentication works exactly as designed. The design just assumed only CDJs would ever be on this network.

## Slide 23

THE BUG

#### WHAT IT GETS YOU

Anything you can read, the attacker can read — over the network.

Four icons: SSH KEYS, PASSWORD DB, DOCUMENTS, CLOUD TOKENS.

## Slide 24

THE BUG

#### AND DJS? YOUR IDs.

Your playlists and your private collection of tracks.

Mac, Windows, CDJ/XDJ hardware, iOS & Android — anything that speaks PRO DJ LINK™ runs this.

Photo: a CDJ's touchscreen loaded with "Above The Cloud (Original Mix)," 08:45, 128.0, F#m, its waveform highlighted, next to BEAT LOOP / KEY SHIFT / BEAT JUMP buttons and the jog wheel. Below: PLAYER 0, TRACK 00, REMAIN 00:00.000, TEMPO -00.00% (±16), BPM 100.0 (MASTER), and a HOT CUE pad row.

## Slide 25

SECTION 05

# THE DEMO

## Slide 26

THE DEMO

#### RECORDED DEMO

- **01** rekordbox running normally — Link Export on
- **02** Attacker terminal — 16 seconds to plaintext
- **03** Point it at a CDJ — read the library

RECORDED PRE-TALK · rekordbox 7.x

## Slide 27

THE DEMO

#### WHERE IT STANDS

AlphaTheta has worked closely with me through the whole process. Software is done; firmware is a bigger lift across that many models.

- rekordbox — Win & macOS: FIXED
- rekordbox — iOS & Android: FIXED
- CDJ / XDJ firmware: IN PROGRESS

## Slide 28

SECTION 06

# WHY THE FIX IS WHAT IT IS

## Slide 29

WHY THE FIX

#### THE OBVIOUS FIX

Harden the auth — make the credential strong and secret, something AlphaTheta controls. But I don't think they can.

## Slide 30

WHY THE FIX

#### FROZEN SINCE 2009

The constant is burned into every PRO DJ LINK™ model since the CDJ-2000. AlphaTheta holds ~60% of the market — feels like 100% in the booth.

Diagram: a chip labeled HARDCODED, tagged 2009.

## Slide 31


> Recovered by OCR — confidence 92/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

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

WHY THE FIX

#### THAT KILLS THE PARTY.

So it's off the table.

Photo: a CDJ touchscreen reading "Not Loaded, 00:00, 0.0" with "No enlarged waveform data" and the rekordbox logo. Below: PLAYER 2, TRACK 12, A.HOT CUE, REMAIN 00:00.000, SINGLE, TEMPO -1.65% (±10), and the error `E-8302: CANNOT PLAY TRACK(3000)`, with BEAT JUMP 16 and a HOT CUE pad row (B C D E F) below.

## Slide 33


> Recovered by OCR — confidence 94/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
| WHY THE FIX
20 YEARS OF UNBROKEN
BACKWARDS COMPATIBILITY.
A set prepped today plays on a CDJ-1000 from 2001. That's genuinely hard — and it freezes the handshake in
place.
```

## Slide 34

WHY THE FIX

#### SHRINK THE SCOPE

Keep accepting the constant. Change 'read the whole filesystem' to 'read only the library folders.' Least privilege.

The deputy's password was never weak — it just held way too much power.

Five boxes in order: SSH, DOCS, LIBRARY, KEYS, CLOUD. All but LIBRARY are marked with an X; LIBRARY alone has a checkmark.

## Slide 35

SECTION 07

# THE DISCLOSURE

## Slide 36

THE DISCLOSURE

#### FOUND IT BY ACCIDENT

Building Now Playing 3, pulling metadata over NFS, I realized I could point at any path I wanted. 'Wait — you shouldn't be able to do that.'

A code editor shows `rekordbox_nfs.py`:

```python
#!/usr/bin/env python3
"""
rekordbox NFS filesystem browser

Demonstrates that rekordbox exposes the entire host filesystem over NFS
with no meaningful authentication. Any device on the local network can
read any file on any mounted drive.

USAGE
-----
    python3 rekordbox_nfs.py <rekordbox-ip>
    python3 rekordbox_nfs.py <rekordbox-ip> --exports
    python3 rekordbox_nfs.py <rekordbox-ip> --ls
    python3 rekordbox_nfs.py <rekordbox-ip> --ls "Users/chris/Music"
    python3 rekordbox_nfs.py <rekordbox-ip> --read "Users/chris/hello.txt"
    python3 rekordbox_nfs.py <rekordbox-ip> --drive D --ls

REKORDBOX SETUP
----------------
1. Open rekordbox on the target machine (macOS or Windows) and in Export mode.
2. Have any Pro DJ Link-compatible device connected to the same network and
   powered on. This is required so the Link Export button appears in Rekordbox.
3. Find the target machine's IP address:
   - macOS: System Settings > Network, or run `ifconfig en0`
   - Windows: Settings > Network, or run `ipconfig`
4. Run this script with that IP address.

HOW IT WORKS
```

(The code panel is cut off at the bottom of the slide; "HOW IT WORKS" is the last visible line.)

## Slide 37

THE DISCLOSURE

#### MY FIRST WORRY WAS US

A small community builds genuinely cool things on reverse-engineered PRO DJ LINK™. I worried a report might make AlphaTheta lock NFS down and shut us out.

Four badges: crate-digger, prolink-connect, alphatheta-connect, and Now Playing (highlighted).

## Slide 38

THE DISCLOSURE

#### I ASKED JAMES ELLIOTT

Author of crate-digger, the canonical open-source implementation. We landed in the same place: the flaw is real, and protecting our own access wasn't reason enough to sit on it.

Photo: someone holding lit glow sticks at a night event.

## Slide 39

THE DISCLOSURE

#### A WARM INTRO

Within 48 hours I was talking to Koushi Kashiwada, who leads rekordbox product planning. Responsive, friendly, professional the whole way.

No bug bounty — but a DJM-V10 would be nice. (Mostly joking.)

A diagram shows two figures, JAMES ELLIOTT and ALPHATHETA, connected by an arc.

## Slide 40

THE DISCLOSURE

#### 90 DAYS → JUNE 1

They asked for more time to fix the rest of the lineup, and I extended it. Transparent and collaborative throughout.

A June calendar, with the 1st circled in orange:

| | | | | |
| --- | --- | --- | --- | --- |
| 1 | 2 | 3 | 4 | 5 |
| 6 | 7 | 8 | 9 | 10 |
| 11 | 12 | 13 | 14 | 15 |
| 16 | 17 | 18 | 19 | 20 |
| 21 | 22 | 23 | 24 | 25 |

## Slide 41

THE DISCLOSURE

#### IN THE MEANTIME

Worried DJ? Don't bring your laptop on stage 10 minutes before your set. Bring a USB stick like a professional.

Photo: two DJs performing together at a lit event.

## Slide 42

SECTION 08

# CLOSE

## Slide 43

CLOSE

#### THAT'S THE BUG

NFS, a hardcoded magic number, and a scope nobody ever locked down. Sitting there for 20 years.

Photo: Triode DJing at a rave, the crowd visible under blue lighting, "TRIODE" printed on the back of his shirt.

## Slide 44

# THANK YOU

Catch anyone's laptop open while I'm on tonight? I'm cutting the music.

**TONIGHT — LIVE AS TRIODE**
SAHARA STAGE
+ OFFICIAL DEF CON PARTY

@TRIODE

