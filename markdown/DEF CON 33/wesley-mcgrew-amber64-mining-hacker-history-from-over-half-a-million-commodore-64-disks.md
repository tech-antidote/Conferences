---
title: "Amber64 Mining Hacker History from Over Half a Million Commodore 64 Disks"
speakers: ["Wesley McGrew"]
conference: "DEF CON"
conference_full: "DEF CON 33"
edition: "33"
year: 2025
source_pdf: "DEF CON 33/Wesley McGrew - Amber64 Mining Hacker History from Over Half a Million Commodore 64 Disks.pdf"
pages: 48
sha256: "48655ce06d010fe09b96d464a152bc2a507b59dff892d73745abe530c613ec19"
text_chars: 18954
ocr_pages: 17
has_ocr: true
redacted_secrets: 0
ocr_confidence: 87.9
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T07:16:38Z"
---
# Amber64 Mining Hacker History from Over Half a Million Commodore 64 Disks

**Speakers:** Wesley McGrew  
**Conference:** DEF CON 33  
**Source:** `DEF CON 33/Wesley McGrew - Amber64 Mining Hacker History from Over Half a Million Commodore 64 Disks.pdf` (48 pages)


## Slide 1

##### `LOAD”AMBER64”,8,1`

\```
SEARCHING FOR AMBER64
LOADING
READY.
RUNAmber64
Mining Hacker History
from Over Half a
Million Commodore 64
Disks
Dr. Wesley McGrew
Senior Cyber Fellow
\```

## Slide 2

# `Agenda`

- Background on 80’s computing and the C64

- The corpus of 653,446 disk images and how they came to be

- Motivations

- Applying modern digital forensics

- Data structures used by the C64 and 1541 disk drive’s Commodore DOS

- Processing the disk images into Elasticsearch for indexed search

- A sample of fun findings

- Future work and conclusions

## Slide 3

# `Computing in the 1980s`

- Hacking/Phreaking

   - Wardialing

   - Boxes/Tones

   - Codes

- BBS

   - Proto-forum/mailing list

   - File trade

   - Cross-platform

   - Motivation for hack/phreak activity

- Software Piracy

   - Cracking protections

   - Distribution

   - Groups

   - Bragging rights

   - Motivation for a lot of other activity (the pornography wasn’t very good yet)

- Demo Scene • “hacking” in the sense of demonstrating low-level systems knowledge

## Slide 4

# `Commodore 64`

- Held the Guiness Book World Record, Highest Selling Single Computer Model. (12.5 to 17 million)

- • Production: August 1982 to April **1994 (!)**

- Keyboard built into the computer

- Composite video, often connected to a television

- Huge library of games, a lot of applications

- First computer for “hackers of a certain age”

- First opportunity to connect via modem to BBS’s, Q-Link, CompuServe

- Most common disk drive: 5.25” Commodore 1541

https://en.wikipedia.org/wiki/Commodore_64#/media/File:Commodore-64-Computer-FL.jpg

## Slide 5

\```
C64      1541
\```

- MOS 6510 at ~1 MHz

- 64K Memory Space

   - Fully-backed by RAM

   - 20KB of ROM

      - KERNAL & BASIC

      - can be switched in and out

- VIC-II for graphics, video signals

- • SID – Digitally controlled analog synth sound

- Serial IEC bus for communications with drives/etc.

- MOS 6502 at ~1 MHz

- Memory

   - 2KB RAM

   - 16KB ROM – Commodore DOS (no relation at all to MSDOS)

- Serial IEC

- ~170KB data per floppy disk

- • Slow – Lots of software and hardware modifications for speeding it up

## Slide 6

\```
Life of a C64 Disk
\```

- Formatted

- Cycle:

   - Downloaded software from BBS, copied from a friend

   - Till the disk fills up

   - Delete some old ones, start the cycle again with fresh warez

   - Disk full of stuff you want to keep? Store it in the floppy box

   - _Rarely label anything accurately_

   - Rinse and repeat

- Other disks might contain data rather than programs

   - Text files

   - BBS sessions (recorded to minimize call times)

- Imaged and archived, distributed on the modern Internet as .d64

## Slide 7

\```
653,446 D64 Images
\```

- The Old School Emulation Center – TOSEC

- C64 Preservation Project

- Internet Archive – Collections and individual downloads

- The Commodore 64 Scene Database (CSDB)

   - Scraped releases

   - Forum threads with large collections

- FTP sites – zimmers, arnold, padua, etc.

- Loadstar Compleat (disk magazine)

   - $15, amazing value: https://rodneylives.itch.io/loadstar

- Other

- Overall, many well-documented games, and an overwhelming number of disks that we have—at best—”surface” level knowledge of the contents

## Slide 8

\```
Classifying
Artifacts
\```

- A floppy disk as a collection of artifacts

   - Apparent

      - Labeled Program  - Printed, on the sticker, on the disk

      - “First” program on the disk

         - Most people are going to **LOAD “*”,8,1**

      - Allocated files ( **LOAD “$”,8** )

         - Mixture of other programs, data files that may or may not be related

   - Hidden

      - Unlabeled disks

      - “Extra” files

      - Deleted files

      - Unallocated/orphaned space

      - Shenanigans

## Slide 9

# `Motivation`

- Lost Media – Games, applications, demos

- Hidden text (such as that documented on The Cutting Room Floor (tcrf.net)

- Comparing versions of software

- Ephemera

   - Communications

   - User-generated files/data

- Hacking history: BBS, phreaking, codes, piracy, cracks, etc.

## Slide 10

# `What we can apply`

- File system forensic analysis (modern, relative to this domain) • Forensic imaging (fortune shines: .d64 format retains most of what we’d want, is essentially a sector-for-sector copy)

   - File system metadata parsing

   - Recovery of deleted files

   - Recovery from free space, allocated-but-not-used space

   - Slack space (between ends of files and ends of sectors, for example)

- Indexed text search

   - Near instantaneous text searching, allowing for easy exploration/analysis

- Modern computing environment

   - Disk space and processing time

## Slide 11

\```
Commodore 1541
Disk Layout &
Data Structures
\```

Diagrams are from Immers, Neufield, _Inside Commodore DOS,_ DATAMOST Inc, 1984 (the book credits technical illustrations to Diane M. Corralejo) This section also known as “Why can’t I just use strings and grep?”

## Slide 12

# `Tracks and Sectors`

.D64 image format is simply a collection of all of these sectors, 256 bytes each, in order.


> Recovered by OCR — confidence 95/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Organization of Tracks and Sectors on a 1541 Formatted Diskette
Track Range of Sector Total Sectors Total Bytes
Numbers Numbers Per Track Per Track
ton, 5376
.D64 image format is simply a collection of all of
these sectors, 256 bytes each, in order.
```

## Slide 13

# `Sector Layout`

The header block is normally used to help drive identify position and read data block, and isn’t in the D64. Other formats (G64, NIB) contain this, but aren’t processed by Amber64 yet.

## Slide 14

# `Sector Layout`

This “256 Data Bytes” is what we’re most interested in


> Recovered by OCR — confidence 92/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
SECTOR #0 SECTOR #1
SECTOR #2
HEAOER BLOCK | DATA BLOCK I. HEADER BLOCK
OATA BLOCK |
HEADER BLOCK
syne mark
inter-sec gap
This “256 Data Bytes” is what we’re most interested in
256 DATA
DATA BYTES BLOCK
CHECKSUM
$00
BYTE
INTER- | SYNC
SECTOR | MARK
GAP
HEADER
BLOCK
1D
```

## Slide 15

# `Directory Track`

• Track 18 typically contains directory information

• Start at Track 18, Sector 0 (18:0):

Forensic Concepts (Brian Carrier, _File System Forensic Analysis_ ): **Essential Data** – Required to be accurate to parse **Nonessential Data** – Not required to be accurate

Also: space for anomalous usage

## Slide 16

# `Directory Track`

- BAM – Table of sectors and whether they’re “free” or not.

- First example of sector chaining: First two bytes of the sector identify the next track and sector that continues the chain (file/directory/whatever)

   - First answer to “Why can’t I just run strings and grep?”

## Slide 17

# `Directory Entry Blocks`

- Note the directory chaining

- • In practice these sectors/blocks aren’t even contiguous (Interleaved)

   - Optimization for spinning disk

   - • Another reason “Why can’t I just run strings and grep?”

## Slide 18

\```
File Entry Format
\```


> Recovered by OCR — confidence 94/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
*STRUCTURE OF SINGLE DIRECTORY ENTRY
ASCII FILE TYPE
BYTE |CONTENTS DEFINITION
0 128+type |File type OR’ed with $80 to indicate properly closed
file.
TYPES: 0 = DELeted
1 = SEQential
2 = PROGram
3 = USER
4 = RELative
1—2 Track and block of Ist data block.
3—18 File name padded with shifted spaces.
19—20 Relative file only: track and block for first side sector
block.
21 Relative file only: Record size.
22—25 Unused.
26—27 Track and block of replacement file when OPEN@ is
in effect.
Number of blocks in file: low byte, high byte.
$00
$81
$83
$00
$01
$02
$03
$04
$A0
$Al
$A2
$A4
$C0
$C1
$C2
$C3
$C4
Scratched
Deleted
Sequential
Program
User
Relative
Unclosed deleted
Unclosed sequential
Unclosed program
Unclosed user
Unclosed relative
Deleted @ replacement
Sequential @ replacement
Program @ replacement
User @ replacement
Relative @ replacement
Locked deleted
Locked sequential
Locked program
Locked user
Locked relative
DIRECTORY SHOWS
Does not appear
DEL
SEQ
PRG
USR
REL
Same as scratched
*SEQ
*PRG
*USR
Cannot occur
DEL
SEQ
PRG
USR
Cannot occur
DEL <
SEQ <
PRG <
USR <
REL <
```

## Slide 19

# `File Formats`

### PRG

#### Note how a sector chain ends

Slack! Often from the 1541 RAM buffers


> Recovered by OCR — confidence 91/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Pp RG SECTOR THE FIRST 252 BYTES
LINK OF YOUR PROGRAM
THE WEXT 254 BYTES
OF YOUR PROGRAM
Note how a sector
. LAST THE FINAL BYTES
Slack! Often from the
1541 RAM buffers
```

## Slide 20

# `File Formats`

SEQ


> Recovered by OCR — confidence 95/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
SEQ
THE FINAL OATA BYTES IN
YOUR SEQUENTIAL FILE
```

## Slide 21

# `File Formats`

- REL

   - More complicated and rare. Unsupported on some non-Commodore disk drives.

   - Two sets of content

      - A SEQuential file with fixed-length records

      - A “side sector” file with pointers to sectors of the sequential file to allow for fast access to specific records

   - File entry (in the directory) contains info on location of side sectors and record length

   - Amber64 can parse this in the most naïve way possible and it’s fine for indexing purposes

- USR – Program-defined, but still should have valid sector linking

## Slide 22

## `Other misc. weirdness we must handle`

(650,000+ disk images means you’ll see every possible thing that folk would do intentionally or unintentionally to a disk)

- 40-track disks

- Invalid tracks/sector pointers (maybe someone just put normal data there)

   - Sector chains that merge into each other

   - GEOS disks & filetypes

   - Unexpected values in data structures with otherwise very predictable values

   - **TEXT ENCODING**

- Sector chain loops

## Slide 23

# `On Text Encoding`

- Commodore PETSCII isn’t exactly ASCII.

   - Two separate “fonts” that can be switched out, “shifted” and “unshifted”

      - This is system state, not stored with the text

      - Given a stream of bytes it’s difficult to tell programmatically which font it’s meant to be rendered in—a lot of times the case in our parsing will be off

   - Uppercase ASCII text lines up with “unshifted” PETSCII uppercase or “shifted” PETSCII lower case.

   - Lowercase ASCII text lines up with “shifted” PETSCII uppercase.

https://en.wikipedia.org/wiki/PETSCII#/media/File:C64_Petscii_Charts.png

## Slide 24

# `On Text Encoding`

- In video memory, “Screen codes” are used instead of PETSCII or ASCII.

- More ranges for what we’d like to index as printable text

- Separate ranges for plain and reverse-color

- Amber64 has to normalize all of the PETSCII and Screen Codes to ASCII.

## Slide 25

# `Amber64`

- amber64.py contains code for processing all of the previously described data structures in a disk (and more)

- Creates JSON data suitable for Elasticsearch indexing and searching

   - Can also create a bit nicer of a nested structure with little modification

## Slide 26

# `Amber64 Output`

- Image name

- SHA256

- Disk Name/ID/Type

- Files

   - Chains

      - Contents of files

      - Directory chains

      - Chains not associated with files

         - Allocated space

         - Free space

- Strings from

- Slack space from end of chains

- Naïve “strings” across image

- SHA256 hashes for everything

## Slide 27

# `Using Amber64`

- Set up Elasticsearch, the local dev quick start is fine

   - https://www.elastic.co/docs/deploy-manage/deploy/self-managed/localdevelopment-installation-quickstart

- Ingesting .D64

   - Set up a directory of .d64 files

   - Change es_url and api_key in initialize.py and ingest.py to match up with your instance

   - ./initialize.py to set up the index

   - ./ingest.py <dir of d64s>

   - To do it faster, split up your input directories and run multiple instances of ingest.py

   - Processed d64s are moved to store/

- Query it with your favorite Elasticsearch frontend

## Slide 28

# `Using Amber64`

- DirMaster – Excellent tool for interactively exploring a D64 image

- Emulation

   - Make a working copy of the disk image you’re about to load (many games and applications make changes to their own disk)

   - VICE - https://vice-emu.sourceforge.io/

- Real Hardware

   - Be comfortable with through-hole desoldering/soldering

   - Modern replacements of proprietary chips are available

   - Keyboard will likely need a complete teardown, cleaning of carbon stems, lube

   - Ultimate 1541-II: Cartridge-based emulation of the disk drive, modem, and a lot more. Network accessible.

## Slide 29

\```
CRAZY FINDINGS TIME!
 CRAZY FINDINGS TIME!
  CRAZY FINDINGS TIME!
   CRAZY FINDINGS TIME!
    CRAZY FINDINGS TIME!
     CRAZY FINDINGS TIME!
      CRAZY FINDINGS TIME!
\```

DISCLAIMER: Any phone numbers are likely owned now owned by completely different, non-80s hacking scene people that have NO IDEA what you’re going on about

## Slide 30

# `Lost Games`

- Assisted researcher Charlotte Cortois

   - PhD Candidate, Université de Montréal

   - History of pornographic video games, among other very interesting work

   - https://miramar.itch.io/

- Text-based “Sex Quiz” games for parties

   - Found a pirated-but-not-obfuscated copy of “Ladies’” version, suitable for study/editing

   - Found references to the lost “Men’s” version

- In the process, found “Asteroid Miner”, not previously identified in current game collections

Compute Gazette, July 1983, P229

## Slide 31

\```
Codes and Cards
\```


> Recovered by OCR — confidence 90/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
C J
On
I know that regular codez dont work
when trying to call boards overseas!
Lemme in on how to call a board in
europe!! [T know that i have to use a
Pbx but how do i use one without
getting fucked up by feds?!?!%?
hacked off this
latah...
ao DESIGN and Shit and i have a box
37 to card
as Shit to! i just need someone to make
45 the call..
EE) The biggest problem i see is, when i
Card they always ask me for a number to
reach them at, but i give them either a
¥ busy number or a number that always
rings! They never send the shit!
Help me!!! -:3
Lone Wolf
```

## Slide 32

\```
Codes and Cards
\```


> Recovered by OCR — confidence 89/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Speaker : OFF Codes to:PRIWTER
Phreak Elite
By: Fred Phreaker and The Phantom
Yersion T by: Talon
=>Uiew Hacked Codes
Start Hacking Codes
Help With Program
Toggle Printer/Disk
ar Games Dialer
BBS List
Toggle Speaker
Credits
Version 7 made 8/789
```

## Slide 33

\```
Codes and Cards
\```


> Recovered by OCR — confidence 91/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Description of Commands
Dialup Mumber The number of the long-
distance company that you will use.
Start Code Hhen hacking SEQ, this
number is the first code that will be
tried. When hacking RAN, the length of
this number determines the length of
the random code.
End Code Used in conjunction
With above, this Will be the last code
that will be tried.
Test Number A number that will
ALWAYS give a 126868 baud carrier when it
answers. The number given WILL work.
Commas Before The number of two-second
“pauses’ that should exist between
dialing the Dialup WNMumber and the
code/Test Number.
Hit CRETURN]
```

## Slide 34

\```
Phone Phreaking
\```


> Recovered by OCR — confidence 86/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Stack Box
Breaker Box
Echo Box
Cracker Box
Cheese Box
x Box
Brass Box
Henu Terminal Mode
ibble-Copy Disk > Disk Menu
Do NOT Blue-Box In ESS Areas!
Yersion 6.6 Written 681-1i1T-87
D Box Mode
ack Box Mode
Mode
arl Box Mode
¢
¢
¢
¢
¢
¢
¢
¢
¢
nter Your hoice
```

## Slide 35

\```
Wiring up your SID
chip and modem
\```


> Recovered by OCR — confidence 86/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Ingredients
i tput cable
ering Iron & Solder
an being that knows what
ronics Componants looks like
2?
3)
4)
6)
Press any key
```

## Slide 36

\```
Wiring up your SID
chip and modem
\```


> Recovered by OCR — confidence 90/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
First, open your 16586 modem. Second,
you mMUSt Connect the 3 inch wire to
a resistor. Here are some steps to
find that resistor.
Find the crystal in the moden.
Above this crystal their is a diode.
Directly to the left of the diode
is a metal wire. Directly to the
left of this mM@tal wire is a Chip.
It is small in size, COmMPared to the
rest of the chips in the modem.
On the lower left edge of the chip,
is a resistor. This resistor is
Directly above a big capasitor.
Solder the 3 inch wire on the right
@edge of the resistor.
Press any key
```

## Slide 37

\```
Wiring up your SID
chip and modem
\```


> Recovered by OCR — confidence 91/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Hext drill a hole in the side of
your MOdeMm, large enough for the
Switch to fit in it. nstert the
Switch in the hole. This will be the
on-off switch for touch tone dialing.
Solder the other end of the 53 inch
wire to the switch.
Cl] to continue
if you have a monitor
Pp
res
s CM]
```

## Slide 38

\```
Wiring up your SID
chip and modem
\```


> Recovered by OCR — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Since you have a monitor you need
another 3 inch wire and you can take
our RCA cable back to the store.
ttatch the other end of the 5 inch
wire to the center of the audio output
jack on your monitor. Your tones are
now connected. To turn them on just
turn on the switch! Please note, this
is connected directly to the sid chip
in your computer, thus making it so
when the switch is on, any sound made
by your computer will go to both, the
modem AND your monitor.
Press any key
```

## Slide 39

\```
Wiring up your SID
chip and modem
\```


> Recovered by OCR — confidence 92/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Hext, strip the end of the RCA
Cable that hooks up to a stereo and
connect the EIR wire to the other
end of the switch. Your tones are now
connected! How, to turn on the tones
just turn on the switch! Please note
these tones come from the sid chip in
your computer, so by turning on the
SwWitch and Playing something out of
your computer you can hear it through
your mMOdem too:
Press any key
```

## Slide 40

\```
Getting Busted
\```


> Recovered by OCR — confidence 69/100 on the text kept, 56/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
news ANDO RUMORS:
-BGLACKHEARC/CHC WAS BUScCCO FOR HACKING
YOU WHO WERE On HAVE co RE-APPLY
If YOU HAYN "Cc ALREADY DONE 5o.
-CORROSION OF CONMFORMIcyY 15 BACK UP
961-365-8667.
¥
```

## Slide 41

\```
Getting Busted
\```


> Recovered by OCR — confidence 68/100 on the text kept, 56/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Getting Busted
NEHS AND RUNOURS HE WHIZARO: WHO HAD SEEN A REAL ASS
THESE NEMS AND RUHOURS HERE COHFILLED IOLE, SUT HAY INSPIRE ME 10 SAR
: GOT BUSTED FOR HACKING BeeeoT) Cand NUMsens 10 A UNDER cover
OF ALL ELITe BOARDS Because He lie Cree OF A SCARED AND HELPLESS
STABBED IN THE BACH ¢ Tre FORM THAT GO HIS COMPUTER
PeRSOD 2. DELETE HIN OFF NAGGED WHEN HE Gol SUSTED ALONG
Tit HIS LAME BOARD!!!
= OF HAS HLS BORKD
BACK UP AT . LT'S THE
FLLE HEADQUARTERS! CALL LITE
```

## Slide 42

\```
Applying to
traffic in warez
\```


> Recovered by OCR — confidence 83/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
"position": 1509,
"string": " 300\nLogon at 11:06 PM\nMessage from highlander (413-538-5864) \ Tues. ,
3/28 11:08 PM\n\n\nHello, yes I do realize that I am\n300 baud, however I am ordering
my\ 2400 buad this weekend, At the moment\ because of my baud rate, I am unable\nto
keep up with transfers. However\nupon receipt of my 2400 and the \nsoon to be rental of
a P.C Pursuit\naccount, I can assure you that I\nwill be able to keep up with the\»
transfers. \nThank You, \»The Immortal Highlander\nLogoff at 11:12 PM\nConnect time"
"position": 1991,
"string": " minutes. \n\n"
```

## Slide 43

\```
A Very Obscure Ad
for 2600 Magazine
\```

## Slide 44

A 1987 interview with Cheshire Catalyst (Editor of TAP Newsletter, HOPE conference, etc.) in “UpTime”, a disk magazine.

## Slide 45

Text files I haven’t seen on modern archives

## Slide 46

# `Conclusions`

- Amber64 allows us to query a very large set of vintage floppy disk images comprehensively and quickly, through:

   - …understanding the details of 1541 disk layout and file system data structures

   - …normalizing potential text of interest into ASCII

   - …creating a JSON data structure representing the structure of data on a disk and indexable text

- …leveraging an easy-to-use engine for indexed search (Elasticsearch)

- • Enables research for others with interesting questions about this era of computing

## Slide 47

# `Conclusions`

- Future work

   - Identifying topics of interest (contact me, I’m happy to run queries on your old handles, BBS, etc.)

   - More comprehensive research, extraction, documentation

   - Other formats (1571, 1581, PRG, Cartridge, Tape)

   - Other platforms (Amiga, PC, etc.)

## Slide 48

# `Contact`

Dr. Wesley McGrew Senior Cyber Fellow MartinFed w.mcgrew@martinfed.com

X: @McGrewSecurity Personal Site: http://mcgrewsecurity.com
