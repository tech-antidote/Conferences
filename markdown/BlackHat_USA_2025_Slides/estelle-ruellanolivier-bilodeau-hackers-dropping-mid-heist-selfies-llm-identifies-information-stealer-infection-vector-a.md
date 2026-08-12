---
title: "Hackers Dropping Mid-Heist Selfies LLM Identifies Information Stealer Infection Vector and Extracts IoCs"
speakers: ["Estelle Ruellan", "Olivier Bilodeau"]
conference: "Black Hat"
conference_full: "Black Hat USA 2025"
edition: "USA"
year: 2025
source_pdf: "BlackHat_USA_2025_Slides/Estelle Ruellan&Olivier Bilodeau_Hackers Dropping Mid-Heist Selfies LLM Identifies Information Stealer Infection Vector and Extracts IoCs.pdf"
pages: 167
sha256: "a4c759d64018a2af6ddd4d956a7e9db6d19ec5f9138da88c963826038d7a9a8f"
text_chars: 68960
ocr_pages: 55
has_ocr: true
redacted_secrets: 0
ocr_confidence: 86.2
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T05:12:23Z"
---
# Hackers Dropping Mid-Heist Selfies LLM Identifies Information Stealer Infection Vector and Extracts IoCs

**Speakers:** Estelle Ruellan, Olivier Bilodeau  
**Conference:** Black Hat USA 2025  
**Source:** `BlackHat_USA_2025_Slides/Estelle Ruellan&Olivier Bilodeau_Hackers Dropping Mid-Heist Selfies LLM Identifies Information Stealer Infection Vector and Extracts IoCs.pdf` (167 pages)


## Slide 1

Byline **Hacker Dropping Mid-Heist Selfies** LLM Identifies  Information Stealer Infection Vectors and Extracts IoC

**Estelle Ruellan,** Threat Intelligence Researcher **Olivier Bilodeau,** Principal Cybersecurity Researcher

#BHUSA   @BlackHatEvents

## Slide 2

###### **Who Are We?**

###### **Olivier Bilodeau**

- 15 years cybersecurity industry experience

- Principal Cybersecurity Researcher at Flare

- • Former GoSecure, ESET. Founder MontréHack

- • NorthSec’s President

- Serial presenter: DEFCON, BlackHat, SecTor, Botconf, CERT-EU, AtlSecCon

###### **Estelle Ruellan**

- Cyber Threat Intelligence Researcher

- • Mathematics and Criminology Background

- • Former student athlete

- Loves data science,  shapes and colors

- • Baby serial presenter: NorthSec, ShmooCon, Botconf, Hack.lu, eCrime APWG, EUROCRIME

Honorable mentions:

flare.io

2

## Slide 3

###### **Agenda**

1. The Information Stealer Malware Phenomenon 2. Mid-Heist Selfies 3. The LLM Pipeline 4. Prompt Engineering 5. LLM Assessment 6. Discriminating IoCs 7. Inside the Infostealer Playbook

8. Successful Campaigns: 2 Case Studies 9. Strength and Limits 10. Conclusion

flare.io

## Slide 4

###### **Agenda**

1. The Information Stealer Malware Phenomenon 2. Mid-Heist Selfies 3. The LLM Pipeline 4. Prompt Engineering 5. LLM Assessment 6. Discriminating IoCs 7. Inside the Infostealer Playbook 8. Successful Campaigns: 2 Case Studies 9. Strength and Limits 10. Conclusion

flare.io

## Slide 5

**What is an Infostealer? The Malware you (may) have never heard of:**

User downloads
cracked software
Malware is executed on
victim computer
Infostealer grabs:
- credentials
- crypto wallets
- browser Data …
Data exfiltrated to C2
infrastructure

Infostealer grabs:
- credentials
- crypto wallets
- browser Data …

**Individual logs are packaged together**

**Log Files are distributed in Telegram Channels**

<u>Administrative rights NOT required! && No Persistence!</u>

flare.io

**5**

## Slide 6

###### **Stealer Log Structure**

78a5g6fdg.zip
From: Cr4zy Cl0ud 2025!1
Here is the daily  un347y8erf.zip
update for Jan
27th!
crazy_cloud
_daily.zip
jnh2389dfv.zip
crazy_cloud_daily.zip
jnkdf89345.zip
uni34r893.zip
6

flare.io

## Slide 7

###### **Stealer Log Structure**

78a5g6fdg.zip
From: Cr4zy Cl0ud 2025!1
Here is the daily  un347y8erf.zip
update for Jan
27th!
crazy_cloud
_daily.zip
jnh2389dfv.zip
crazy_cloud_daily.zip
jnkdf89345.zip
uni34r893.zip
7

flare.io

## Slide 8

###### **Stealer Log Structure**

78a5g6fdg.zip
SystemInfo.txt
From: Cr4zy Cl0ud 2025!1
Here is the daily
un347y8erf.zip
update for Jan
Passwords.txt
27th!
crazy_cloud
_daily.zip
jnh2389dfv.zip
Screenshot.jpg
crazy_cloud_daily.zip
jnkdf89345.zip
chrome_profile_1.txt
cookies
uni34r893.zip
Opera_profile_2.txt
8
files flare.io

## Slide 9

**Agenda** 1. The Information Stealer Malware Phenomenon 2. Mid-Heist Selfies 3. The LLM Pipeline 4. Prompt Engineering 5. LLM Assessment 6. Discriminating IoCs 7. Inside the Infostealer Playbook 8. Successful Campaigns: 2 Case Studies 9. Strength and Limits 10. Conclusion

flare.io

## Slide 10

###### **Mid-Heist selfies REALISTIC PICTURE OF BRO BEHIND HIS SCREEN**

flare.io

## Slide 11

###### **Mid-Heist selfies**

flare.io

## Slide 12

**Some examples**

###### **Mid-Heist selfies**

flare.io

12


> Recovered by OCR — confidence 90/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Mid-Heist selfies
12
! IF YOU HAVE TROUBLES
DOWNLOADING/LAUNCHING FILE JUST TURN OFF
YOUR ANTI-VIRUS ITS ABSOLUTELY SAFE !
FORTNITE HACK | UNDETECTED | FORTNITE MOD MENU | DOWNLOAD FREE
```

## Slide 13

**Some examples Mid-Heist selfies**

Us

flare.io

13

## Slide 14

**THE NUMBERS**

###### **Mid-Heist selfies**

Infection screenshots contain all the clues and hints needed to solve the mystery of infection

flare.io

14

## Slide 15

**THE NUMBERS**

###### **Mid-Heist selfies**

11 +15M Malware Families Screenshots*

## +25%

of all logs

*Including duplicates

flare.io

16

## Slide 16

**THE NUMBERS**

###### **Mid-Heist selfies**

11 +15M +25% Malware Families Screenshots* of all logs *Including duplicates

flare.io

17

## Slide 17

**Agenda** 1. The Information Stealer Malware Phenomenon 2. Mid-Heist Selfies 3. The LLM Pipeline 4. Prompt Engineering 5. LLM Assessment 6. Discriminating IoCs 7. Inside the Infostealer Playbook 8. Successful Campaigns: 2 Case Studies 9. Strength and Limits 10. Conclusion

flare.io

## Slide 18

###### **Overview of the Pipeline**

Screenshot

1st LLM Layer Formatted Description

2nd LLM Layer

flare.io

19

## Slide 19

###### **Overview of the Pipeline**

2nd LLM Layer

Live IoC
[Vector ; Theme]  Theme
IoC checking
 Dead IoC

flare.io

20

## Slide 20

Why 2 Layers ?

###### **Overview of the Pipeline**

Screenshot
1st LLM Layer 2nd LLM Layer
Formatted
Description

flare.io

21

## Slide 21

Why 2 Layers ?

###### **Overview of the Pipeline**

“Identify the infection vector”

flare.io

22

## Slide 22

Why 2 Layers ?

###### **Overview of the Pipeline**

“Identify the infection vector”
LLM

flare.io

23

## Slide 23

Why 2 Layers ?

###### **Prompt Engineering**

flare.io

24


> Recovered by OCR — confidence 84/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Prompt Engineering
© YouTube how to install mod menu fortnite pe
1 IF YOU HAVE TROUBLES
DOWNLOADING/LAUNCHING FILE JUST TURN OFF
YOUR ANTI-VIRUS ITS ABSOLUTELY SAFE !
FORTNITE HACK | UNDETECTED | FORTNITE MOD MENU DOWNLOAD FREE
FORT NITE = nn) (ene 4 Download = =+ Save
24
```

## Slide 24

WHY 2 LAYERS ?

###### **Overview of the Pipeline**

1. Visually assess the screenshot

flare.io

25

## Slide 25

Why 2 Layers ?

###### **Overview of the Pipeline**

flare.io

26


> Recovered by OCR — confidence 87/100 on the text kept, 68/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Overview of the Pipeline
GP Youtube how to install mod menu fortnite pe 2022
load
d
1 IF YOU HAVE TROUBLES
DOWNLOADING/LAUNCHING FILE JUST TURN OFF
YOUR ANTI-VIRUS ITS ABSOLUTELY SAFE !
FORTNITE HACK | UNDETECTED | FORTNITE MOD MENU DOWNLOAD FREE
```

## Slide 26

Why 2 Layers ?

###### **Overview of the Pipeline**

1. Visually assess the screenshot

2.  Point out potential infection vectors based on f i eld knowledge

flare.io

27

## Slide 27

**Why 2 Layers ? Overview of the Pipeline**

An LLM can’t just ‘figure it out’: we must translate intuition into instructions.

flare.io

28

## Slide 28

Why 2 Layers ?

###### **Overview of the Pipeline**

1. Visually assess the screenshot

2. Point out infection vectors

flare.io

29

## Slide 29

**Agenda** 1. The Information Stealer Malware Phenomenon 2. Mid-Heist Selfies 3. The LLM Pipeline 4. Prompt Engineering 5. LLM Assessment 6. Discriminating IoCs 7. Inside the Infostealer Playbook 8. Successful Campaigns: 2 Case Studies 9. Strength and Limits 10. Conclusion

flare.io

## Slide 30

The first layer **Prompt Engineering**

Visual Assessment

Web Content

File System

Hybrid

flare.io

31

## Slide 31

The first layer

###### **Prompt Engineering**

###### Web Content

flare.io

32

## Slide 32

The first layer

###### **Prompt Engineering**

###### File System

flare.io

33


> Recovered by OCR — confidence 84/100 on the text kept, 70/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Prompt Engineering
Zalo
Admin
3
This PC
Network
Recycle Bin
Control
Panel
ABBYY
FineRead.
&
leaner
P
Project
‘SAP2000 16
Sketchup
2019
Microsoft
Edge
khd
Du Toan Eta
Style Builder
2019
cét thé.
~$
©
Microsoft
Edge
ETABS 18
Foxit PDF
Reader
Google
Chrome
LayOut 2019
PDF24
PowerPoint Chuyen CAD
sang Word
UltraViewer
Unikey
vic media
player
Word
a
Excel
A
a
Access
mhkalsxy.
yidAMev.
File System
This PC
HEP TTT
Documents
Huéng dan dd an tét nghiép ¢
Documents Program Fil
Hinh anh
‘Tap pO AN DRIVER
this Pc
B 3D Objects
2) Documents
Music
=| Pictures
Program Files (x86
Linh Tinh
```

## Slide 33

The first layer

###### **Prompt Engineering**

###### File System

The first layer
Prompt Engineering

flare.io

34


> Recovered by OCR — confidence 86/100 on the text kept, 68/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
34
Prompt Engineering
Please stay online while Office
downloads
We'll be done in just a
File System
@ 33°C Ensoleilé ~ G & DO GZ) FRA
13:36
19/01/2023 ac}
```

## Slide 34

The first layer

###### **Prompt Engineering**

###### Hybrid

flare.io

35


> Recovered by OCR — confidence 70/100 on the text kept, 55/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
55)
The first layer
Prompt Engineering
http://
Hybrid
=
€ > Y D MP> Este equipo > Descargas > Microsoft Office Crack 2022 > Microsott Office Crack 2022 v
+ Descargas # Wm cata 21/11/2022 9:10 Carpeta de archivos
BB Documentos #
Bl @fomicvell 21/11/2022 909 Aplicacion 696.320 KB
Bm Manuales
Bu Septiembre 202:
Bm Espacio familiar
Ba HALO
BM Soporte Tecnico
@ OneDrive - Person
> I Este equipo
4.lementos | 1 elemento selecciofjsdo 680MB |
= @
```

## Slide 35

The first layer **Prompt Engineering**

Visual Assessment

File Explorer & Installer

Scene Description

URL

Browser Tab Identification

Suspicious Elements

flare.io

36

## Slide 36

###### **### Main Content:**

The first layer Desc ribe the main content vis ible on the screen, include as much detail as possible. **~~Prompt Engineering~~**

**### Files/Programs:**

**Installer:** Focus on installers or install window, put the name of the file being installed. When there is a name for the installer window, get the name of file/folder or the path.

**File explorer:** Focus on file explorer if there is one. Put the names of files and their extensions in this section. If the path of the file explorer reveals the name of a folder/file, get it. Ignore all desktop programs and icons. Scene Description File Explorer & Installer URL Seperate filenames by a ",". If there aren’t any file, executable or program put "X".

###### **### URL**

Put all URLs you see. If there aren’t any URLs, put "X". Visual

**### Browser Tabs Analysis:** Assessment

Assessment

Ignore bookmarks. For each active browser tab in the top row, list in this format:

- **[logo: {logo name}] [text: {visible text}] (meaning/context if apparent)** . If there aren’t any webpage, put "X".

Browser Tab Identification Suspicious Elements

###### **### Suspicious Elements:**

Highlight any file, executable, program, URL or download link that could contain malware. These could be 37 flare.io youtube videos, blogs, google drive, etc.

## Slide 37

###### **### Main Content:**

The first layer Desc ribe the main content vis ible on the screen, include as much detail as possible. **Prompt Engineering**

###### **### Files/Programs:**

**Installer:** Focus on installers or install window, put the name of the file being installed. When there is a name for the installer window, get the name of file/folder or the path.

**File explorer:** Focus on file explorer if there is one. Put the names of files and their extensions in this section. If the path of the file explorer reveals the name of a folder/file, get it. Ignore all desktop programs and icons. Scene Description File Explorer & Installer URL Seperate filenames by a ",". If there aren’t any file, executable or program put "X".

###### **### URL**

Put all URLs you see. If there aren’t any URLs, put "X". Visual

###### **### Browser Tabs Analysis:** Assessment

Assessment

Ignore bookmarks. For each active browser tab in the top row, list in this format:

- **[logo: {logo name}] [text: {visible text}] (meaning/context if apparent)** . If there aren’t any webpage, put "X".

Browser Tab Identification Suspicious Elements

###### **### Suspicious Elements:**

Highlight any file, executable, program, URL or download link that could contain malware. These could be 38 flare.io youtube videos, blogs, google drive, etc.

## Slide 38

###### **### Main Content:**

The first layer Desc ribe the main content vis ible on the screen, include as much detail as possible. **Prompt Engineering**

**### Files/Programs:**

**Installer:** Focus on installers or install window, put the name of the file being installed. When there is a name for the installer window, get the name of file/folder or the path.

**File explorer:** Focus on file explorer if there is one. Put the names of files and their extensions in this section. If the path of the file explorer reveals the name of a folder/file, get it. Ignore all desktop programs and icons. Scene Description File Explorer & Installer URL Seperate filenames by a ",". If there aren’t any file, executable or program put "X".

###### **### URL**

Put all URLs you see. If there aren’t any URLs, put "X".

Visual

###### **### Browser Tabs Analysis:** Assessment

Assessment

Ignore bookmarks. For each active browser tab in the top row, list in this format:

- **[logo: {logo name}] [text: {visible text}] (meaning/context if apparent)** . If there aren’t any webpage, put "X".

Browser Tab Identification Suspicious Elements

###### **### Suspicious Elements:**

Highlight any file, executable, program, URL or download link that could contain malware. These could be 39 flare.io youtube videos, blogs, google drive, etc.

## Slide 39

###### **### Main Content:**

The first layer Desc ribe the main content vis ible on the screen, include as much detail as possible. **Prompt Engineering**

###### **### Files/Programs:**

**Installer:** Focus on installers or install window, put the name of the file being installed. When there is a name for the installer window, get the name of file/folder or the path.

**File explorer:** Focus on file explorer if there is one. Put the names of files and their extensions in this section. If the path of the file explorer reveals the name of a folder/file, get it. Ignore all desktop programs and icons. Scene Description File Explorer & Installer URL Seperate filenames by a ",". If there aren’t any file, executable or program put "X".

###### **### URL**

Put all URLs you see. If there aren’t any URLs, put "X". Visual

###### **### Browser Tabs Analysis:** Assessment

Assessment

Ignore bookmarks. For each active browser tab in the top row, list in this format:

- **[logo: {logo name}] [text: {visible text}] (meaning/context if apparent)** . If there aren’t any webpage, put "X".

Browser Tab Identification

Suspicious Elements

###### **### Suspicious Elements:**

Highlight any file, executable, program, URL or download link that could contain malware. These could be 40 flare.io youtube videos, blogs, google drive, etc.

## Slide 40

###### **### Main Content:**

The first layer Desc ribe the main content vis ible on the screen, include as much detail as possible. **Prompt Engineering**

**### Files/Programs:**

**Installer:** Focus on installers or install window, put the name of the file being installed. When there is a name for the installer window, get the name of file/folder or the path.

**File explorer:** Focus on file explorer if there is one. Put the names of files and their extensions in this section. If the path of the file explorer reveals the name of a folder/file, get it. Ignore all desktop programs and icons. Scene Description File Explorer & Installer URL Seperate filenames by a ",". If there aren’t any file, executable or program put "X".

###### **### URL**

Put all URLs you see. If there aren’t any URLs, put "X". Visual

###### **### Browser Tabs Analysis:** Assessment

Assessment

Ignore bookmarks. For each active browser tab in the top row, list in this format:

- **[logo: {logo name}] [text: {visible text}] (meaning/context if apparent)** . If there aren’t any webpage, put "X".

Browser Tab Identification Suspicious Elements

###### **### Suspicious Elements:**

Highlight any file, executable, program, URL or download link that could contain malware. These could be 41 flare.io youtube videos, blogs, google drive, etc.

## Slide 41

The first layer **Prompt Engineering**

Visual Assessment

flare.io

42


> Recovered by OCR — confidence 69/100 on the text kept, 34/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ESET NODS2 ANTIVIRUS CRACK 2023 @ FREE OOWNLOAD @ UCENSE KEY INTORNET SECURITY
@ 100% WORKING
```

## Slide 42

###### **### Main Content:**

The sc reenshot displays a comp uter desktop environment with an ESET Security window on the left side , promp ting The first layer the user to input a license key. There is a red error message indicating that the entered license key is not correct. On **Prompt Engineering** the right side, there is a YouTube video titled "ESET NOD32 ANTIVIRUS CRACK 2023" which claims to offer a free download of a license key for ESET antivirus software. It includes a description with instructions for installation and cautionary steps such as disabling antivirus and Windows Smart Screen.

**### Files/Programs:**

**Installer:** ESET NOD32 ANTIVIRUS CRACK 2023 **File explorer:** X

Scene Description File Explorer & Installer

URL

###### **### URL**

1. https://www.youtube.com/watch?v=HBG5nZQ7ThA

###### **###Tabs** Visual

1. {Youtube} : [Download ESET NOD32 ANTIVIRUS CRACK 2023] Assessment

2. {ESET} [License key internet security 100% working]

###### **### Suspicious Elements:**

- The YouTube video titled "ESET NOD32 ANTIVIRUS CRACK 2023" and the associated download link Browser Tab Identification Suspicious Elements

- (https://cutt.ly/NOD-32) are highly suspicious, as they suggest accessing cracked software, which typically contains malware.

- 43

- - The license key entry prompt in the ESET window may indicate that the user is following instructi ons from the vi flare.io deo to illegally activate software.

## Slide 43

The first layer **Prompt Engineering**

###### INPUT

Web Content

File System

Hybrid

Visual Assessment

Formatted Description

Vector Identification

flare.io

44

## Slide 44

The first layer
Prompt Engineering
INPUT
Web
Content
File
System
Visual  Formatted
Hybrid
Description
Assessment

Visual  Formatted
Vector
Description
Assessment
Identification
flare.io

45

## Slide 45

**Agenda** 1. The Information Stealer Malware Phenomenon 2. Mid-Heist Selfies 3. The LLM Pipeline 4. Prompt Engineering 5. LLM Assessment 6. Discriminating IoCs 7. Inside the Infostealer Playbook 8. Successful Campaigns: 2 Case Studies 9. Strength and Limits 10. Conclusion

flare.io

## Slide 46

The first layer

###### **Evaluation**

Visual Assessment

96%

100%

100%

File Explorer & Installer

Scene Description

URL

85%

Browser Tab Identification INCONSISTENT Suspicious Elements
INCONSISTENT

flare.io

47

## Slide 47

###### The first layer **Evaluation - Browser Tab Identification**

30% 32% Browser Tab Identification 36%

flare.io

48

## Slide 48

###### The first layer **Evaluation - Browser Tab Identification - Case Study**

flare.io

49


> Recovered by OCR — confidence 85/100 on the text kept, 72/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
49
Evaluation - Browser Tab Identification - Case Study
Despejado
TradingView
Experimente potencia adicional, velocidad adicional y
flexibilidad adicional, todo con la misma UX que conoce y ama.
DESCARGAR oO DESCARGAR DESCARGAR
GM Para ventanas | | WR nara mac os na lini
```

## Slide 49

The first layer **Evaluation - Browser Tab Identification - Case Study**

**### Browser Tabs Analysis:**

**- [logo: TradingView] [text: Aplicación de escritorio TradingView] (A webpage for the desktop application of TradingView)**

**- [logo: YouTube] [text: (15) Tradingview para pc mas rápido] (A video related to using TradingView on PC)**

**- [logo: Google] [text: 1PrimeOptions] (A tab likely related to trading or financial information) - [logo: WhatsApp] [text: (53)] (Notifications for WhatsApp) - [logo: Google] [text: RePelis24 | Ver Pel...] (A site for watching movies or series) - [logo: Google] [text: Creador de logotipo... (Logo creator link)**

**- [unknown logo] [text: Olymp Trade — Pla...] (A financial trading platform)**

flare.io

50

## Slide 50

###### The first layer **Evaluation - Solution**

Visual Assessment

Scene Description

File Explorer & Installer

URL

Browser Tab Identification INCONSISTENT
INCONSISTENT

Suspicious Elements

flare.io

51

## Slide 51

The first layer
Evaluation - Solution
Scene Description File Explorer & Installer URL
Visual
Assessment
Browser Tab Identification Suspicious Elements
52
flare.io
INCONSISTENT
INCONSISTENT

## Slide 52

###### The first layer **Evaluation - Solution**

Visual Assessment

Scene Description

File Explorer & Installer

URL

Browser Tab Identification INCONSISTENT
INCONSISTENT

Suspicious Elements

flare.io

53

## Slide 53

###### The first layer **Evaluation - Solution**

Scene Description File Explorer & Installer URL
85%
Visual
Assessment
Suspicious Elements

flare.io

54

## Slide 54

The first layer **Evaluation**

Web Content File System Hybrid

Visual  Formatted
2nd LLM
Description
Assessment
Layer
flare.io

55

## Slide 55

THE 2ND LAYER **THE LLM LAYERS**

**V** [Vector ; Theme] **V T T**

**T** Vector identification + formatting **V https://mega.nz/folder/GEkRCKaT#f93dJ6myfe3fENhDS4wqxQ; T** **<u>KMSAuto++ v1.8.7 for Microsoft product activation</u>**

flare.io

61

## Slide 56

###### Getting out the trash **Discriminating IoCs**

[Vector ; Theme]

2nd LLM Layer

flare.io

62

## Slide 57

###### Getting out the trash **Discriminating IoCs**

[Vector ; Theme]

2nd LLM Layer

flare.io

63

## Slide 58

Getting out the trash **Discriminating IoCs**

[Vector ; Theme] 2nd LLM Layer

flare.io

64

## Slide 59

Getting out the trash **Discriminating IoCs**

[Vector ; Theme]

2nd LLM Layer

flare.io

65

## Slide 60

Getting out the trash
Discriminating IoCs

Discriminating IoCs
Live IoC
[Vector ; Theme]  Theme
IoC checking
2nd LLM Layer
 Dead IoC

flare.io

66

## Slide 61

###### Getting out the trash **Discriminating IoCs**

2nd LLM Layer

Live IoC
[Vector ; Theme]  Theme
IoC checking
 Dead IoC

flare.io

67

## Slide 62

**Agenda** 1. The Information Stealer Malware Phenomenon 2. Mid-Heist Selfies 3. The LLM Pipeline 4. Prompt Engineering 5. LLM Assessment 6. Discriminating IoCs 7. Inside the Infostealer Playbook 8. Successful Campaigns: 2 Case Studies 9. Strength and Limits 10. Conclusion

flare.io

## Slide 63

###### Getting out the trash **Discriminating IoCs**

IoC checking

File sharing platforms

YouTube Videos Others

flare.io

69

## Slide 64

###### Getting out the trash **Discriminating IoCs**

IoC checking

 Dead IoC

flare.io

70

## Slide 65

###### Getting out the trash **Discriminating IoCs**

IoC checking

Live IoC

flare.io

71


> Recovered by OCR — confidence 87/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
71
Discriminating loCs
loC checking
Save to MEGA Download
| | SoftwareDownload+(Password -
Enter decryption key
Live loC
```

## Slide 66

###### Getting out the trash **Discriminating IoCs**

IoC checking

Live IoC

flare.io

72


> Recovered by OCR — confidence 77/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
72
Discriminating loCs
~
2
>
loC checking
Q
@ Home GTA5(FiveM) Fortnite AMD &NVIDIABESTSETTINGS ~ Blood Fx
eM Fix GTAS _b3905.exe!sub_1407A07C8 (0x43
FiveM Fix GTA5 b3905.exe!sub_1407A07C8 (0x43)!
How To Downl
```

## Slide 67

###### Getting out the trash **Discriminating IoCs**

IoC checking

Dead IoC

flare.io

73


> Recovered by OCR — confidence 84/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Getting out the trash
Discriminating loCs
@) YouTube Search
Video unavailable
/ r This content isn't available.
loC checking t
x Dead loC
```

## Slide 68

###### Getting out the trash **Discriminating IoCs**

IoC checking

Live IoC

flare.io

74


> Recovered by OCR — confidence 95/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Getting out the trash
Discriminating loCs
loC checking
74
Microsoft Office Crack Free Download Full Version 2022
33 vues 31 oct. 2022
Welcome! Leave a LIKE and SUBSCRIBE if you enjoyed this video!
ARCHIVE PASSWORD: 7521
DOWNLOAD LINK (DIRECT LINK): https://bit.ly/3N8nHDp
Live loC
```

## Slide 69

###### Getting out the trash **Discriminating IoCs**

IoC checking

Theme

flare.io

75


> Recovered by OCR — confidence 94/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Getting out the trash
Discriminating loCs
Microsoft Office Crack Free Download Full Version 2022
~ 33 vues 31 oct. 2022
Welcome! Leave a LIKE and SUBSCRIBE if you enjoyed this video!
ARCHIVE PASSWORD: 7521
i Theme
loC checking
```

## Slide 70

# **DEMO**

flare.io

## Slide 71

83

flare.io


> Recovered by OCR — confidence 87/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
(stealerlogs-ioc-feed) obilodeau@sparkle ~/f/r/s/stealerlogs ioc feed (main)> python -m fetch _screens.refactored pipel
ine.fetch_analyze --download-screens --open-screens --openai-response --delay 10
```

## Slide 72

flare.io

84

## Slide 73

85 flare.io

## Slide 74

**Agenda** 1. The Information Stealer Malware Phenomenon 2. Mid-Heist Selfies 3. The LLM Pipeline 4. Prompt Engineering 5. LLM Assessment 6. Discriminating IoCs 7. Inside the Infostealer Playbook 8. Successful Campaigns: 2 Case Studies 9. Strength and Limits 10. Conclusion

flare.io

## Slide 75

###### **Lure Themes - Cracked Software**

flare.io

## Slide 76

Infostealer Playbook

###### **Lure Themes - Cracked Software**

$$$

Cracked 0$

flare.io

88

## Slide 77

Infostealer Playbook **Lure Themes - Cracked Software** Cracked 150$ 0$

flare.io

89


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
89
Infostealer Playbook
Lure Themes
Paying $150
for lifetime access
to a secure,
legitimate license
from a globally
recognized corporation.
Free Microsoft_Office_Crack_rar
```

## Slide 78

Infostealer Playbook

###### **Lure Themes - Cracked Software**

Threat actors prey on users’ willingness to bypass legitimate licensing fees at the cost of their own security

flare.io

90

## Slide 79

Infostealer Playbook

###### **Lure Themes - Cracked Software**

flare.io

91

## Slide 80

Infostealer Playbook

###### **Lure Themes - Cracked Software**

###### MAINSTREAM

flare.io

92

## Slide 81

###### **Infostealer Playbook - Lure Themes**

###### Targeting mainstream products ensures large pool of potential victims

flare.io

93

## Slide 82

###### **Lure Themes - Gaming Cheats & Mods**

flare.io

## Slide 83

Infostealer Playbook

###### **Lure Themes - Gaming Cheats & Mods**

flare.io

95

## Slide 84

Infostealer Playbook

###### **Lure Themes - Gaming Cheats & Mods**

flare.io

96

## Slide 85

Infostealer Playbook

###### **Lure Themes - Gaming Cheats & Mods**

flare.io

97

## Slide 86

Infostealer Playbook

###### **Lure Themes - Gaming Cheats & Mods**

Weapons
Skins

Mods

flare.io

98

## Slide 87

Infostealer Playbook

###### **Lure Themes**

###### If it’s free and shady, you’re likely the victim

flare.io

99

## Slide 88

**Distribution Strategies - YouTube as a Distribution System**

flare.io

## Slide 89

###### Infostealer Playbook **Distribution Strategies - YouTube as a Distribution System**

**BEST FREE FORTNITE CHEAT 2025 | SILENT AIM + ESP | UNDETECTED**

**MICROSOFT 2022 CRACK (GENUINE  + 100% FREE)**

flare.io

101

## Slide 90

###### Infostealer Playbook **Distribution Strategies - YouTube as a Distribution System**

**BEST FREE FORTNITE CHEAT 2025 | SILENT AIM + ESP | UNDETECTED**

**MICROSOFT 2022 CRACK (GENUINE  + 100% FREE)**

flare.io

102

## Slide 91

103

flare.io


> Recovered by OCR — confidence 81/100 on the text kept, 59/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
BLES
S ABSOLUTELY SAFE!
FORTNITE HACK | UNDETECTED | FORTNITE MOD MENU | DOWNIS/AD FREE
$5) SS&B nha 17 op AY Share + Download =+ Save
22
267 views 8 DY
FORTNITE HACRAMPNDETECTED | FORTNITE MOD MENU. | OAD FREE
& ARCHIVE PA ORD: shgzchez
(> Instructions
```

## Slide 92

###### Infostealer Playbook **Distribution Strategies - YouTube as a Distribution System**

It is free It works

Disabling antivirus is needed & safe

flare.io

104

## Slide 93

###### Infostealer Playbook **Distribution Strategies - YouTube as a Distribution System**

It is free It works

Disabling antivirus is needed & safe

flare.io

105

## Slide 94

###### Infostealer Playbook **Distribution Strategies - YouTube as a Distribution System**

YouTube’s reach and tutorial-driven-content make it the perfect launchpad for infostealer malware

flare.io

106

## Slide 95

###### **Distribution Strategies - Google Ads**

flare.io

## Slide 96

Infostealer Playbook **Distribution Strategies - Leveraging Google Ads**

Software S

flare.io

108

## Slide 97

**The Anatomy of a Stealer Log**

flare.io

109


> Recovered by OCR — confidence 87/100 on the text kept, 66/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
4
gle
sans titre - Story Book x midjourney - Recherche Google X +
?q=midj = =midj = 157j0i
midjourney x §&§ g
AS
x
Environ 39 800 000 résultats
Sponsorise
Sponsorisé
© ai.mid-journey.org
java ANH
Java -cp
java ... parameter
java -jar 23
Get The Latest Updates - MidJourney
Comprehensive Tutorials on Working with Midjourney. Exclusive Updates and Fi
Subscribe To Our Midjourney Course.
Recherches associées
Bil - https://go.java-gapp.space/ +
Switch to Java - Java Download
Java is a reliable and powerful programming language that provides convenient programn
Java is a platform for creating analytical and consumer with extensive capabilities.
midjourney image — midjourney bot
midjourney ai midjourney #macron
midjourney gratuit midjourney how to use
midjourney discord midjourney prix
Midjourney
https://midjourney.com - Traduire cette page
Midjourney
Midjourney is an independent research lab exploring new mediums of thought and expanding aimee 84) Jclels
the imaginative powers of the human species.
https://www.java.com > ... ¥
```

## Slide 98

###### Infostealer Playbook

###### **Distribution Strategies - Leveraging Google Ads**

Google Ads give threat actors a fast lane to users’ trust — by placing malicious content where users expect safety: at the top.

flare.io

110

## Slide 99

**Agenda** 1. The Information Stealer Malware Phenomenon 2. Mid-Heist Selfies 3. The LLM Pipeline 4. Prompt Engineering 5. LLM Assessment 6. Discriminating IoCs 7. Inside the Infostealer Playbook 8. Successful Campaigns: 2 Case Studies 9. Strength and Limits 10. Conclusion

flare.io

## Slide 100

Infostealer Playbook **Successful Campaigns:** **~~3~~ 2 Case Studies**

flare.io

113


> Recovered by OCR — confidence 89/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Infostealer Playbook
Successful Campaigns: 3 2 Case Studies
IoC - https://mega.nz/folder/GErkKCTaT#9dGmye
Theme - Microsoft 2022
IoC - https://mega.nz/folder/GErkKCTaT#9dGmy
Theme - Microsoft 2022 Cracked Free
IoC - https://mega.nz/folder/GErkCTaT#9dGmye
Theme - Yuki Microsoft 2022 DOWNLOAD
```

## Slide 101

Infostealer Playbook **Successful Campaigns:** **~~3~~ 2 Case Studies**

MidJ0urney Blitz Java 6.3% 5.3%

flare.io

115

## Slide 102

MidJ0urney Blitz Java

## Slide 103

**The Anatomy of a Stealer Log**

flare.io

126


> Recovered by OCR — confidence 90/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
About Store Gmail Images
midjourney prompts with results
midjourney when blending with two text prompts, what do you
put between them.
midjourney what are some of the best user prefer option set
examples
midjourney bot
midjourney discord
Q
Q
Q midjourney v5
Q. midjourney api
Q
midjourney free
Google Search I'm Feeling Lucky
Report ingppropriste predictions
Advertising Business How Search works ‘& Carbon neutral since 2007 Privacy Terms Settings
```

## Slide 104

###### **The Anatomy of a Stealer Log**

flare.io

127


> Recovered by OCR — confidence 85/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
@ Design sans titre - Story Book x . midjourney - Recherche Google X +
¢>x
Google
» *
Ciel couvert
midjourney x<
Q Tous E)Images (G) Vidéos ©) Actualités [Livres i Plus Outils
Environ 39 800 000 résultats (
ai_mid-journey.org
Get The o& Updates - MidJourney
U&rials on Working with Midjourney. Exclusive Updates and Features
Recherches associées
midjourney image midjourney bot
midjoumey ai midjourney #macron
midjourney gratuit | midjourney how to use
midjourney discord midjourney prix
Midjourney
https://midjourney.com - Traduire cette page
Midjourney
Midjourney is an independent research lab exploring new mediums of thought and expanding
the imaginative powers of the human species
£33 $33 Connexion
{2} Plus d'images
Midjourney <
Midjourmey est un laboratoire de recherche
indépendant qui produit un programme d'intelligence
artificielle sous le méme nom et qui permet de créer
des images a partir de descriptions textuelles, suivant
un fonctionnement similaire a celui de DALL-E
Créateur : Midjourney
Premiére version : 2022
```

## Slide 105

The Anatomy of a Stealer Log

It is possible that the computer’s security
systems may FALSELY trigger

flare.io

128


> Recovered by OCR — confidence 83/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
@ Fat
é
© She
Cc
© Mo: | $f Abe | G INS | G FNA | [FJ Tou | [FY Tow | FRY Tou | FF Coc | FR Con | ih Rec! | FF Coc
MidJourney 64-bit
0$/month
Unleash Your Creativity with MidJourney's Al-powered Images!
Download for Windows ¥
How do | make a request using MidJourney's Al?
What stock images can | find on MidJourney
How can | use MidJourney's images?
It is possible that the computer’s security
systems may FALSELY trigger
FAQ.
```

## Slide 106

The Anatomy of a Stealer Log

It is possible that the computer’s security systems may FALSELY trigger

flare.io

129


> Recovered by OCR — confidence 86/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ney 64-bit
month
MidJourney's Al-powered Images!
|for Windows ¥
It is possible that the computer’s security
systems may FALSELY trigger
How can | use MidJourney's images?
```

## Slide 107

130 flare.io


> Recovered by OCR — confidence 77/100 on the text kept, 65/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
4
Gérer Téléchargements
| Fichier | Accueil Partage
+t e« Disque local (C:) » Utilisateurs >» Sherlybulle » Téléchargements
Affichage Outils d'application
ATIPIK_Sch
ATIPIK-Plante # 3
MidSetup.ex
PERSO ad
; ier (14) o
Innovative Al-powered program th fein Fi) Kicepoge-Sitisiexe
to generate st Egoistement v6)
|m] —Pngtree—woman archer powerful_6636351.png
&| —Pngtree—target shooting_5927062.png
&] les mots mélés(1).png
a] les mots mélés.png
&) Les valeurs de votre Instituti.png
|g] Carrousel Linkedin .jpg
|=] Documents
=) Images 5
B Objets 3D &) Couverture_reels(5),jpg
} Téléchargement:
Plus tot cette semaine (28)
1 291 élément(s) 1 élément sélectionné 4,99 Mo
Why MidJourney?
```

## Slide 108

131 flare.io


> Recovered by OCR — confidence 85/100 on the text kept, 43/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
a
q a
Mares and Ceeka...
“Splan 70
PDF
UMT_UNIS...
UMT_Uniso...
Disable antivirus and try again
Continuar |
updates
Blacklist
12:55
```

## Slide 109

132 flare.io


> Recovered by OCR — confidence 91/100 on the text kept, 38/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
1.6 GHz
UMT_UNIS...
UMT_Uniso...
updates
12:55
```

## Slide 110

133 flare.io


> Recovered by OCR — confidence 81/100 on the text kept, 44/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ems | |t is possible that the computer's security
systems may FALSELY trigger
(
Dente DX
Blacklist updates
12:55
```

## Slide 111

###### **The A** **natomy of a Stealer Lo g**

g

How to disable bitdefender antivirus 2023

flare.io

134


> Recovered by OCR — confidence 91/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Google [tow to aisable bitdefender antivirus 2023 m ! © Q &
This video will show you how to temporary disable ww enable
How to Temporarily Disable or Enable Bitdefender TOTAL.
YouTube - Nam Anh Cap - 25 jan. 2022
Saknas: 2623 | Maste innehalla: 2023
how to bebe disable bitdefender 2023 - YouTube
how to temporarily disable bitdefender 2023 ... aia win cu
How to disable bitdefender antivirus 2023
YouTube - MR BNA - For 1 manad sedan
https://clean-my-pc.com
Oversatt den har sidan
How to Disable Bitdefender Windows 10 - Clean my PC
Open the Bitdefender Total Security 2019 on your device. - Navigate to the Protection
Features tab and click on the Settings icon under the Antivirus module
Oversatt den har sidan
How to Disable Bitdefender Notifications - Prajwal.org
7 2022 — Launch the Bitdefender antivirus or Total security tool. - Select Settings and
click General tab. - Turn off the Special Offers and Recommended
https://www.safetydetectives.com Oversatt den har sidan
How to Cancel Bitdefender Subscription (& Get a Refund) in ...
Find Bitdefender under your list of products and click Stop automatic subscription renewal. ... |
recommend Norton — it's my favorite antivirus in 2023,
nsioner
Q uninstall bitdefender Q bitdefender alert page
22:36
2023-01-11
```

## Slide 112

135 flare.io


> Recovered by OCR — confidence 92/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Windows Security
fm Home
| sy} Virus & threat protection
QR Account protection
(Firewall & network protection
App & browser control
Device security
Device performance & health
Family options
& Settings
ft «= Type here to search
%x Virus & threat protection settings
View and update Virus & threat protection settings for Microsoft
Defender Antivirus.
This setting is managed by your administrator.
Real-time protection
Locates and stops malware from installing or running on your device. You
can turn off this setting for a short time before it turns back on
automatically.
Cloud-delivered Wotection
Provides increased and faster protection with access to the latest
protection data in the cloud. Works best with Automatic sample
submission turned on.
@ of
Automatic sample submission
Send sample files to Microsoft to help protect you and others from
potential threats. We'll prompt you if the file we need is likely to contain
personal information,
A Automatic sample submission is off. Your device may be —— Dismiss
vulnerable.
@ of
Submit a sample manually
Tamper Protection
Prevents others from tampering with important security features.
A Tamper protection is off. Your device may be vulnerable. Dismiss
Have a question?
Get help
Help improve Windows Security
Give us feedback
Change your privacy settings
View and change privacy settings
for your Windows 10 device.
Privacy settings
Privacy dashboard
Privacy Statement
```

## Slide 113

136 flare.io


> Recovered by OCR — confidence 90/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Windows Security -
%x Virus & threat protection settings
View and update Virus & threat protection settings for Microsoft Have a question?
Ge Hone Defender Antivirus. Get help
| sy} Virus & threat protection
This setting is managed by your administrator Help improve Windows Security
QR Account protection
. . Give us feedback
Real-time protection ive us feedbac
Locates and stops malware from installing or running on your device. You
can turn off this setting for a short time before it turns back on
automatically.
(Firewall & network protection
App & browser control Change your privacy settings
Device security - «* View and change privacy settings
) oe for your Windows 10 device.
Device performance & health o Privacy settings
Privacy dashboard
sf Family options
Cloud-delivered Wotection
Privacy Statement
Provides increased and faster protection with access to the latest
protection data in the cloud. Works best with Automatic sample
submission turned on.
@ of
Automatic sample submission
Send sample files to Microsoft to help protect you and others from
potential threats. We'll prompt you if the file we need is likely to contain
personal information
A Automatic sample submission is off. Your device may be Dismiss
vulnerable.
Submit a sample manually
Tamper Protection
Prevents others from tampering with important security features.
A Tamper protection is off. Your device may be vulnerable, Dismiss
@ of
Ber Settings
= 04:13 PM
P& Type here to search n © 9 =
```

## Slide 114

###### **The** **Anatomy of a Stealer Lo g**

ai.midj0urney or virus

flare.io

137


> Recovered by OCR — confidence 87/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
@ Tips for Waiters.
x French Terms Related toF & BSi X Perfect software for all your visu: X (GS) ai.midjOurney.or fake? - Google © X
+
<3 & @ google.com/search?q=ai.midjOurney.or+fake%3F&oq=ai.midjOurney.or+fake%3F&aqs=chrome..69i57.10221j0j7 &sourceid=chrome&ie=UTF-8
@ YouTube ™ Gmail
Google
Is Midjourney a real Al?
Why is Midjourney no longer free?
© Washington Post
https:/Awww.washingtonpost.com » 2023/03/30 > midj
Midjourney is making fake images go mainstream
30 Mar 2023 — The Al image generator Midjourney has quickly become one of the internet's
most eye-catching tools, creating realistic-looking fake visuals ...
Decrypt
https://decrypt.co » midjourney-free-ai-image-generati
Midjourney Kills Free Al Image Generator Access After ...
30 Mar 2023 —A “deep fake’ is realistic-looking media created by Al by altering images, videos,
or audio to show real people doing or saying things they ...
https:/Awww.vox.com > technology > al-image-dalle-o.
How unbelievably realistic fake images could take over the ...
30 Mar 2023 — Al image generators like DALL-E and Midjourney are getting better and better
at fooling us.
@ Reddit - Dive into a... G Discord (EJ Amazon.de: Low Pri... (@ ChatGPT [| Websites Tools [| One Piece
virus fake
Is Midjourney v
What is the most realistic Al art generator? v
v
Feedback
BB Games [ Godot
a
ai.midjOurney or virus
IB Cooking
o
```

## Slide 115

###### **The** **Anatomy of a Stealer Lo g**

ai.midj0urney or virus

flare.io

138


> Recovered by OCR — confidence 86/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
@ Tips for Waiters. x Hi French Terms Related toF & BSi X Perfect software for all your visu: X (GS) ai.midjOurney.or fake? - Google © X +
Cc @ google.com/search?q=ai.midjOurney.or+fake%3F&oq=ai.midjOurney.or+fake%3F&aqs=chrome..69i57.10221j0j7&sourceid=chrome&ie=UTF-8
@ YouTube M Gmail @ Reddit -Diveintoa.. Gp Discord [EJ Amazone: Low Pri... (@ ChatGPT Websites | Tools [M OnePiece | Shopping [| Games [ Godot
virus fake
Is Midjourney a
What is the most realistic Al art generator? v
Is Midjourney a real Al?
Why is Midjourney no longer free?
© Washington Post
https:/Awww.washingtonpost.com > 2023/03/30 > midj.
Midjourney is making fake images go mainstream
30 Mar 2023 — The Al image generator Midjourney has quickly become one of the internet's
most eye-catching tools, creating realistic-looking fake visuals ...
(2) Decrypt
https://decrypt.co » midjourney-free-ai-image-generati
Midjourney Kills Free Al Image Generator Access After ...
30 Mar 2023 —A “deep fake’ is realistic-looking media created by Al by altering images, videos,
or audio to show real people doing or saying things they ...
https:/Awww.vox.com > technology > al-image-dalle-o.
How unbelievably realistic fake images could take over the ...
30 Mar 2023 — Al image generators like DALL-E and Midjourney are getting better and better
at fooling us.
a
o
```

## Slide 116

Use Cases

###### **Midj0urney Campaign**

flare.io

139

## Slide 117

### MidJ0urney Blitz Java

## Slide 118

141 flare.io


> Recovered by OCR — confidence 96/100 on the text kept, 63/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Battle.net
World of
Warcraft
EPIC
Epic Games
Launcher
Fall Guys
League of
Legends
```

## Slide 119

142 flare.io


> Recovered by OCR — confidence 83/100 on the text kept, 62/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Battle.net
World of
Warcraft
E }
‘Sf Java_Clientzip - ZIP archive, unpacked size 168 195 366 byt
Name Size Packed Type
jre Manka c daiinose
Java Setup.exe 10202752 9641210 Mpwnoxenne
Total 1 folder and 10 202 752 bytes in 1 file
13:19
12/02/2023 Bi
```

## Slide 120

143 flare.io


> Recovered by OCR — confidence 84/100 on the text kept, 67/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
World of ° Ressources d'aide
Warcraft
® Qu que Java? de Java 8?
FPIC Enlever les ancienne
a Désactiver Java
) Dépanner Java le Java
Aide supplémentaire la compter du 16 avril 2019.
est sensiblement différent
utilisations a titre gratuit,
H'autres utilisations peuvent
AN i Ee ices Oracle Java. Veuillez lire
Find — Wizard an Camment it. Une FAQ est disponible ici.
avec un abonnement a Java
Name e n SE.
Manxa ¢ $2
fa Setup.exe 20. 9641210 Mpnnoxerne
Télécharger Java
En téléchargeant Java, vous reconnaissez avoir lu et accepté les conditions du
Contrat de licence Oracle Technology Network License pour Oracle Java SE
@ Ala finde rinstallation de Java, si vous utilisez Web Start, vous devrez peut-étre redémarrer le navigateur (fermer
toutes les fenétres du navigateur et les rouvrir).
Total 1 folder and 10 202 752 bytes in 1 file
```

## Slide 121

144 flare.io


> Recovered by OCR — confidence 78/100 on the text kept, 67/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
. Who spends money like th X MBB Jactroll fait godter des fron X MBBON CREE UN SANDWICH? X @ Download Java for Windov {I 64-bit Java for Windows
Bm Java Client x) +
2 Recherche
A Base Nome
Y @ Barbara - Peso: | (Hole de Java 8?
je Java 8?
Java Set
i le Java
BBB ambiente de # compter du 16 avril 2019.
ab Transferencia # est sensiblement différent
Mbcarrarc utilisations a titre gratuit,
H'autres utilisations peuvent
Ges fe ces Oracle Java. Veuillez lire
Bm Trabalhos Ba # it. Une FAQ est disponible ici.
avec un abonnement a Java
B videos *
Bim Son Heung Min
Bm The Sims 4
mcc
Ba Clothes Télécharger Java
En téléchargeant Java, vous reconnaissez avoir lu et accepté les conditions du
GQ v MM estepc Contrat de licence Oracle Technology Network License pour Oracle Java SE
Disco Local (C:
Zitens | 1 item selecionado 9,72 MB |
allation de Java, si vous utilisez Web Start, vous devrez peut-étre redémarrer le navigateur (fermer
» FAQ relative a lava Ad hits nour Windows
Total 1 folder and 10 202 752 bytes in 1 file
```

## Slide 122

145 flare.io


> Recovered by OCR — confidence 81/100 on the text kept, 62/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ON CREE UN SANDWIC
BE Ambiente de #
B Documentos #
B imagen
Bm Trabalhos Ba #
B videos *
Home Shave View Manage
SIDSY > Downloads > Java.Clent
Bim The Sims desktop
Documents
New flder
= INSTALLATION
Disco Local (C:
Zitens | 1 item selecionado 9,72
Q Procurar t
INSTALLATION
tmp
today
== Selected 10 202 752 bytes in 1 file Total 1 folder and 10 202 752 bytes in 1 file
HH 64-bit Java for Windows
Recherche
de Java 8?
le Java
{4 compter du 16 avril 2019.
est sensiblement différent
utilisations 4 titre gratuit,
H'autres utilisations peuvent
ices Oracle Java. Veuillez lire
it. Une FAQ est disponible ici.
12.2.2023 r. 12/02/2023
```

## Slide 123

146 flare.io


> Recovered by OCR — confidence 74/100 on the text kept, 54/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Bm Java Client x +
2 Recherche
A Base me Data de
Y @ Barbara - Pesso: | | Hole de Java 8?
je Java 8?
Biv Dateiordner utilisations a titre gratuit,
BE Documentos #
Im Desktop ~ BcopyricHt Datei H'autres utilisations peuvent
=
ee 4 Downloads LICENSE Datei ces Oracle Java. Veuillez lire
Bm Trabalhos Ba # os BB rcapme os it. Une FAQ est disponible ici.
Bm Son Heung Min
Bm The Sims 4
v MB Este PC
© Disco Local (C:
( gy
2itens | 1 item selecionado 9,72 MB | a
@ Welcome Microsoft Edge HTML Do
= USBDISK (0)
—
Chrome
Filmore 12
Selected 10 202 752 bytes in 1 file
```

## Slide 124

flare.io

147


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Line Download Help
Help Resources Download Java for Windows
Version 8 Update 361 (filesize: 40.11 MB)
Release date: January 17, 2023
Important Oracle Java License Information
The Oracle Java License changed for releases starting April 16, 2019.
- F The T Net k Licer A nent fi le Ja E is substantially different
Offline Installation
from prior Oracle Java licenses. This license permits certain uses, such as personal use and
development use, at no cost -- but other uses authorized under prior Oracle Java licenses may no
longer be available. Please review the terms carefully before downloading and using this
product. An FAQ is available t
Trouble downloading?Try the
Commercial license and support is available with a low cost Java SE Subscription.
Download Java
By downloading Java you acknowledge that you have read and accepted the
terms of the Network Ag
(When your Java installation completes, if you ai sing webstart, you may need to restart your browser (close all
browser windows and re-open
```

## Slide 125

flare.io

148


> Recovered by OCR — confidence 93/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Download Help
Help Resources
Offline Installation
Trouble downloading?Try the
Download Java for Windows
Whe
brov
>
Download Developer Resources Help
Help Resources Download Java for Windows
Version 8 Update 361 (filesize: 62.11 MB) Why is Java 8 recommended?
Release date: January 17, 2023
What is Java?
Remove older versions
Disable Java
Error messages
Troubleshoot Java Important Oracle Java License Information
ORE HE The Oracle Java License changed for releases starting April 16, 2019.
" m The Oracle Technology Network License Agreement for Oracle Java SE is substantially different
from prior Oracle Java licenses. This license permits certain uses, such as personal use and
development use, at no cost -- but other uses authorized under prior Oracle Java licenses may no
longer be available. Please review the terms carefully before downloading and using this
product. An FAQ is available here.
Do you use both 32-bit and 64-bit
browsers?
FAQ about 64-bit Java for Windows
Offline Installation Commercial license and support is available with a low cost Java SE Subscription.
Trouble downloading?Try the
offline installer
By downloading Java you acknowledge that you have read and accepted the
terms of the Oracle Technology Network License Agreement for Oracle Jav
When your Java installation completes, if you are using webstart, you may need to restart your browser (close all
browser windows and re-open).
```

## Slide 126

flare.io

149


> Recovered by OCR — confidence 89/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Download Java for Windows
Help Resources Download Java for Windows
Wits? Version 8 Update 361 (filesize: 62.11 MB) Why is Java 8 recommended?
Ct javacom,
é Information
=/Java__—‘ Télécharger Developer Resources Aide s starting April 16, 2019.
ent for Oracle Java SE is substantially different
nits certain uses, such as personal use and
. . . thorized under prior Oracle Java licenses may no
Ressources d'aide
Java 64 bits pour Windows fully before downloading and using this
Version 8 Update 361 (taille de fichier : 62.11 MB) Intérét de l'utilisation de Java 8?
Date de publication : 17 janvier 2023
a low cost Java SE Subscription.
Dépanner Jav. Informations importantes sur la licence Oracle Java
Aide suppl
La licence Oracle Java a été modifiée pour les versions publiées 4 compter du 16 avril 2019.
Le contrat de e Oracle Technology Network pour Oracle Java SE est sensiblement différent jada |
des précédentes licences Oracle Java. Cette licence autorise certaines utilisations a titre gratuit,
telles qu'une utilisation personnelle ou pour le développement, mais d'autres utilisations peuvent e that you have read and accepted the
ne plus étre disponibles, bien qu'autorisées sous les précédentes licences Oracle Java. Veuillez lire k License Agreement for Oracle Java SE
attentivement les conditions avant de télécharger et d'utiliser ce produit. Une FAQ est disponible ici
Le support et la licence commerciale sont disponibles 8 moindre cout avec un abonnement a Java
SE webstart, you may need to restart your browser (close all
En téléchargeant Java, vous reconnaissez avoir lu et accepté les conditions du
Contrat de licence Technology Network License pour O
@_ Als finde l'installation de Java, si vous utilisez Web Start, vous devrez peut-étre redémarrer le navigateur (fermer
```

## Slide 127

150
flare.io

## Slide 128

flare.io

151


> Recovered by OCR — confidence 90/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
iM} TempM - temp mail... & Online Phone N ~ Your account has b... © Request money fro... @ Receive FreeSMSO.. @ SMSPanel t TempMail P Persona — NEW MIC 7 MAICRO Sm dlac
&
Go gle java x
@ News : More Tools
Java
java jdk download ava Computer software
This search may be relevant to recent activity:
Java is a set of computer software and specifications
developed by James Gosling at Sun Microsystems.
which was later acquired by the Oracle Corporation.
that provides a system for developing application
software and deploying it in a cross-platform
computing environment. Wikipedia
Ad - hitps://go java-gapp.space/ ~
App - Java Download
Java - a programming language for creating powerful applications and websites. Java - a
platform that allows you to expand the functionality of your system.
Ad - https://oracle.58226.click/ ~
Java - Specifically applications Programming languages: Java. C, C++. Assembly
Programming language and computing platform. Get for desktop applications. language
Initial release date: January 23, 1996
Developer: Oracle, Sun Microsystems. James
Java |_Oracle
Get Java for desktop applications. Download Java - What is Java? Uninstall help. Happy Java
People also search for
»en Group St
Manual download Minecraft. Unix WinRAR Minecraft
Java manual dowmload page. Get the latest version of the Java Bedrock servers
User. Are you a software developer looking for JDK downloads?
Download Java for Windows
Download or update your existing Java Runtime Environment
Install Java on Windows More about Java >
This article applies to: Platform(s): Windows 10, Windows 3
https://www,java.com How do | install Java .
```

## Slide 129

152 flare.io


> Recovered by OCR — confidence 90/100 on the text kept, 72/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
© burp suite pr X
iM} TempM - temp mail...
Google
https://www.java.com
4 Professiona @ burp suite p
Online Phone Num... Your account has b... © Request money fro... @ Receive
x
@ News : More Tools
This search may be relevant to recent activity:
java jdk download
Ad - hitps://go java-gapp.space/ ~
App - Java Download
Java - a programming language for creating powerful applications and websites. Java - a
platform that allows you to expand the functionality of your system.
Java - Specifically applications
Programming language and computing platform. Get for desktop applications
Java |_Oracle
Get Java for desktop applications. Download Java - What is Java? Uninstall help. Happy Java
User. Are you a software developer looking for JDK downloads?
Download Java for Windows
Download or update your existing Java Runtime Environment
Manual download
Java manual download page. Get the latest version of the Java
Install Java on Windows
This article applies to: Platform(s): Windows 10, Windows 8
How do | install Java
x ts
q= | O10 &aqs=chr...
Google {ono
AS
Java -cp
java ... parameter
java -jar 2&
Switch to Java - Java Download
Java is a reliable and powerful programming language that provides convenient programming.
Java is a platform for creating analytical and consumer with extensive capabilities.
\
```

## Slide 130

flare.io

153


> Recovered by OCR — confidence 89/100 on the text kept, 72/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
© burp suite p
'M| TempM - temp mail...
Google
https://www.java.com
x @ Burp Suite z
@ google.com/s
& Online Phone Num... Your account has b... © Request money fro... @ Receive
About 1,930,000,000 r
(0.42 seconds)
This search may be relevant to recent activity:
java jdk download
Ad - https://go.java-gapp.space/ ~
App - Java Download
Java - a programming language for creating powerful applications and websites. Java - a
platform that allows you to expand the functionality of your system.
Java - Specifically applications
Programming language and computing platform. Get for desktop applications
Java |_Oracle
Get Java for desktop applications. Download Java - What is Java? Uninstall help. Happy Java
User. Are you a software developer looking for JDK downloads?
Download Java for Windows
Download or update your existing Java Runtime Environment
Manual download
Java manual download page. Get the latest version of the Java
Install Java on Windows
This article applies to: Platform(s): Windows 10, Windows 8
How do | install Java
G iozao
Google H4 x +
Google
AS
1 java ... parameter
java -jar 4! 6
Java -cp
Bil - https://go.java-gapp.space/ +
Switch to Java - Java Download
Java is a reliable and powerful programming language that provides convenient programming.
Java is a platform for creating analytical and consumer with extensive capabilities.
3a - http:/www.ikosmo.co.kr/ +
java.
```

## Slide 131

flare.io

154


> Recovered by OCR — confidence 80/100 on the text kept, 72/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
© burp suite pr X @ Burp Suite ra $ G 1020 - Google df x +
iM] TempM - temp mail... & Online Phone Num... Your account has b... ic enn SMe | Gmail €§) YouTube gf AZ
Google {ono x m@toaa
AS
. *» https://go.java-gapp.space/
ot
This search may be relevant to recent activity:
java jdk download
java + ti java ... parameter
Ad - https:/igo java-gapp.space/ ~ Java -cp java -jar ae
Java - a programming language for creating powerful applications and websites. Java - a
platform that allows you to expand the functionality of your system. j
Bil - https://go.java-gapp.space/ +
Java - Specifically applications witch to Java - Java Downloa
Programming language and computing platform. Get for desktop applications Java is a reliable and powerful programming language that provides convenient programming.
Java is a platform for creating analytical and consumer with extensive capabilities.
Java |_Oracle
Get Java for desktop applications. Download Java - What is Java? Uninstall help. Happy Java
3a - http:/www.ikosmo.co.kr/ +
User. Are you a software developer looking for JDK downloads? SIS ADE OF ol XH 7H St] - java - ikosmo.co.kr
Download Java for Windows
Manual download
Java manual dovmload page. Get the latest version of the Java SAWOHA HOS SAE A QS] ASUCH St 19M] O/4to] ASAE AMISS SH SE Sas St USy
Install Java on Windows ALOLOLS JA] 101 015
This article applies to: Platform(s): Windows 10, Windows 8 APSAL HMMS Al ANAS
How do | install Java
```

## Slide 132

flare.io

155


> Recovered by OCR — confidence 90/100 on the text kept, 72/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
© burp suite p
'M| TempM - temp mail...
x @ Burp Suite
@ google.com,
& Online Phone Num... Your account has b... © Request money fro... @ Receive
https://www.java.com
This search may be relevant to recent activity:
java jdk download
Ad - https://go.java-gapp.space/ ~
App - Java Download
Java - a programming language for creating powerful applications and websites. Java - a
platform that allows you to expand the functionality of your system.
Java - Specifically applications
Programming language and computing platform. Get for desktop applications
Java |_Oracle
Get Java for desktop applications. Download Java - What is Java? Uninstall help. Happy Java
User. Are you a software developer looking for JDK downloads?
Download Java for Windows
Download or update your existing Java Runtime Environment
Manual download
Java manual download page. Get the latest version of the Java
Install Java on Windows
This article applies to: Platform(s): Windows 10, Windows 8
How do | install Java
AS
java + ti java ... parameter
Java -cp java -jar 2
Bil - https://go.java-gapp.space/ + ais
Switch to Java - Java Download
Java is a reliable and powerful programming language that provides convenient programming.
Java is a platform for creating analytical and consumer with extensive capabilities.
3a - http:/www.ikosmo.co.kr/ +
https:/Awww.java.com > ...
```

## Slide 133

flare.io

156


> Recovered by OCR — confidence 95/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
& Java Download Developer Resources Help
Help Resources Download Java for Windows
Version 8 Update 361 (filesize: 62.11 MB) Why is Java 8 recommended?
Release date: January 17, 2023
What is Java?
Remove older versions
Disable Java
Error messages
Troubleshoot Java Important Oracle Java License Information
Sine The Oracle Java License changed for releases starting April 16, 2019.
5 Fi The Oracle Technology Network License Agreement for Oracle Java SE is substantially different
from prior Oracle Java licenses. This license permits certain uses, such as personal use and
development use, at no cost -- but other uses authorized under prior Oracle Java licenses may no
longer be available. Please review the terms carefully before downloading and using this
product. An FAQ is available here.
Do you use both 32-bit and 64-bit
browsers?
FAQ about 64-bit Java for Windows
Offline Installation Commercial license and support is available with a low cost Java SE Subscription.
Trouble downloading?Try the
offline installer
Download Java
By downloading Java you acknowledge that you have read and accepted the
terms of the Oracle Technology Network License Agreement for Oracle Java SE
a When your Java installation completes, if you are using webstart, you may need to restart your browser (close all
browser windows and re-open).
```

## Slide 134

flare.io

157


> Recovered by OCR — confidence 95/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
& Java Download Help
Help Resources
Offline Installation
Trouble downloading?Try the
Download Java for Windows
Version 8 Update 361 (filesize: 40.11 MB)
Release date: January 17, 2023
Important Oracle Java License Information
The Oracle Java License changed for releases starting April 16, 2019.
The Oracle Technology Network License Agreement for Oracle Java SE is substantially different
from prior Oracle Java licenses. This license permits certain uses, such as personal use and
development use, at no cost -- but other uses authorized under prior Oracle Java licenses may no
longer be available. Please review the terms carefully before downloading and using this
product. An FAQ is available here.
Commercial license and support is available with a low cost Java SE Subscription.
Download Java
By downloading Java you acknowledge that you have read and accepted the
terms of the Oracle Technology Network License Agreement for Oracle Java SE
QO When your Java installation completes, if you are using webstart, you may need to restart your browser (close all
browser windows and re-open).
```

## Slide 135

158
flare.io


> Recovered by OCR — confidence 92/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
go.java-gapp.space
Help Resources Download Java for Windows
Version 8 Update 361 (filesize: 40.11 MB)
Release date: January 17, 2023
Important Oracle Java Lic
The Oracle Java License changed for r
The Oracle Technology Network License
from prior Oracle Java licenses. This lice
Trouble downloading? Try the development use, at no cost -- but other
f longer be available. Please review the ter
product. An FAQ is available here.
Offline Installation
Commercial license and support is availa
By downloading Java you ack
terms of the Oracle Technolog
QO When your Java installation completes, if you aj
browser windows and re-open).
```

## Slide 136

###### **Legit**

###### **Malicious**

flare.io

159


> Recovered by OCR — confidence 89/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Download Developer Resources Help
Help Resources Download Java for Windows
Version 8 Update 36) (filesize: 62.11 MB)| Why is Java 8 recommended?
Release date: January 17, 2U.
What is Java?
Remove older versions
Disable Java
Error messages
Important Oracle Java Licen
Do you use both 32-bit and 64-bit 7 a
browsers?
FAQ about 64-bit Java for Windows product. An FAQ is available here.
Offline Installation Commercial license and support is available with a low cost Java SE Subscription.
Trouble downloading?Try the
offline installer
Download Java
By downloading Java you acknowledge that you have read and accepted the
terms of the Oracle Technology Network License Agreement for Oracle Java SE
Help
Help Resources Download Or for Windows
M a Fi cious ; a portant Oracle ieee
a filesize: 40.11
— product. An FAQ is available h
Commercial license and support is available with a low cost Java SE Subscription.
Download Java
By downloading Java you acknowl t you have read and accepted the
terms of the Network it for
```

## Slide 137

flare.io

160


> Recovered by OCR — confidence 86/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
[i] TempM -ter’ x © java-Google x +
@ Burp Suite z 4 Professional, X @ burp suite pr xX | 9 VIP4StatsUss x
© burp suite pr X
[2] TempM - temp mail...
@ google.com/s ? a&biw=18 APX dUPu KEw vil - ( &
& Online Phone N Your account has b... © Request money fro... @ Receive FreeSMSO.. @ SMSPanel t TempMail P Persona — NEW MIC em alo
Go gle java x &£§ BDA 83
QA D) Videos @) News : More Tools
https://www.java.com
This search may be relevant to recent activity:
java jdk download
ating powerful applications and websites. Java - a
inctionality of your system.
Ad - https://oracle.58226.click/ ~
Java - Specifically applications
Programming language and computing platform. Get for desktop applications.
Java |_Oracle
Get Java for desktop applications. Download Java - What is Java? Uninstall help. Happy Java
User. Are you a software developer looking for JDK downloads?
Download Java for Windows
Download or update your existing Java Runtime Environment
Manual download
Java manual download page. Get the latest version of the Java
Install Java on Windows
This article applies to: Platform(s): Windows 10, Windows 8
How do | install Java
Java
Java Computer software
Java is a set of computer software and specifications
developed by James Gosling at Sun Microsystems.
which was later acquired by the Oracle Corporation.
that provides a system for developing application
software and deploying it in a cross-platform
computing environment. Wikipedia
Initial release date: January 23, 1996
Programming languages: Java. C, C++. Assembly
language
Developer: Oracle, Sun Microsystems. James
People also search for
»en Group St
WinRAR Minecraft
servers
Minecraft Unix
Bedrock
More about Java >
```

## Slide 138

flare.io

161


> Recovered by OCR — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Download Help
Help Resources Download Java for Windows
Version 8 Update 361 (filesize: 40.11 MB)
Release date: January 17, 2023
Important Oracle Java License Information
The Oracle Java License changed for releases starting April 16, 2019.
F The Oracle Tect gy Network License Agreement for Oracle SE is substantially different
Offline Installation
from prior Oracle Java licenses. This license permits certain uses, such as personal use and
development use, at no cost -- but other uses authorized under prior Oracle Java licenses may no
longer be available. Please review the terms carefully before downloading and using this
product. An FAQ is available here
Trouble downloading? Try the
Commercial license and support is available with a low cost Java SE Subscription
By downloading Java you acknowledge that you hi id accepted the
terms of the Oracle Technology Network ense resent for Oracle Java SE
7) When your Java installation completes, if you are using webstart, you may need to restart your browser (close all
browser windows and re-open).
```

## Slide 139

flare.io

162


> Recovered by OCR — confidence 72/100 on the text kept, 57/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
/\ | Java_Client
A Base Nome
Vv @ Barbara - Pessoz .
> [i Capturas de!
BH Ambiente de #
wb Transferéncia #
162
```

## Slide 140

flare.io

163


> Recovered by OCR — confidence 73/100 on the text kept, 64/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
@& Java Client x a 6
A Base Nome j
@ Java Setup “f
Bm Documentos
Ba jre
YB Imagens
Bm Capturas de |
Bl Ambiente de #
wb Transferéncia #
EB Documentos #
Bi Trabalhos Ba #
@ Masica *
EE videos *
B® Son Heung Min
Bm The Sims 4
v_ MB Este PC
© Disco Local (C:
2itens | 1 item selecionado 9,72 MB |
Bea
22:55
>
»
163
```

## Slide 141

164 flare.io


> Recovered by OCR — confidence 89/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
@ (08) @ i try installing java but it ¢ bea) “fF
Google i try installing java but it doesn't work xX OQ
About 38,800,000 results (0.63 seconds)
Temporarily turn off firewall or antivirus clients
Active firewall or antivirus software may prevent Java from installing properly. Remember to
turn your firewall or antivirus software back on when you have successfully completed the
Java install.
https://java.com > download > help > troubleshoot_java
Troubleshooting tips for running Java
@ About featured snippets - [MH Feedback
People also ask
How do | force Java to install?
A Home Name
164
```

## Slide 142

## 19h

flare.io

165

## Slide 143

Use Cases

###### **Blitz Java Campaign**

flare.io

166

## Slide 144

Use Cases

###### **Successful Campaigns**

flare.io

169

## Slide 145

Use Cases **Successful Campaigns**

Threat actors rely on simple psychological tactics—because they still work.

flare.io

170

## Slide 146

**Agenda** 1. The Information Stealer Malware Phenomenon 2. Mid-Heist Selfies 3. The LLM Pipeline 4. Prompt Engineering 5. LLM Assessment 6. Discriminating IoCs 7. Inside the Infostealer Playbook 8. Successful Campaigns: 2 Case Studies 9. Strength and Limits 10. Conclusion

flare.io

## Slide 147

Discussion **Strength and Limits**

The screenshots embody both our greatest strength and our primary limitation

flare.io

172

## Slide 148

Discussion **Strength and Limits**

flare.io

173

## Slide 149

Discussion **Strength and Limits**

TRADITIONAL MALWARE
LLM
ANALYSIS
Works w/o Code Signatures
Robust against Code Changes*
Cross Family Friendly
Works w/o Screenshot

flare.io

174

## Slide 150

Discussion

###### **Strength and Limits**

flare.io

175

## Slide 151

Discussion **Strength and Limits**

TRADITIONAL MALWARE
LLM
ANALYSIS
Works w/o Code Signatures
Robust against Code Changes*
Cross Family Friendly
Works w/o Screenshot

flare.io

176

## Slide 152

Discussion

###### **Strength and Limits**

Existence

flare.io

177

## Slide 153

Discussion

###### **Strength and Limits**

Existence

Quality

flare.io

178

## Slide 154

Discussion **Strength and Limits**

Existence

Quality

flare.io

179

## Slide 155

Discussion **Strength and Limits**

LLM
Works w/o Code Signatures
Robust against Code Changes*
Cross Family Friendly
Works w/o Screenshot

TRADITIONAL MALWARE
ANALYSIS

flare.io

180

## Slide 156

Discussion **Cost and Speed**

5-10s **0.003** $ processing per image

Cost for 100k images: 300$

flare.io

181

## Slide 157

**Agenda** 1. The Information Stealer Malware Phenomenon 2. Mid-Heist Selfies 3. The LLM Pipeline 4. Prompt Engineering 5. LLM Assessment 6. Discriminating IoCs 7. Inside the Infostealer Playbook 8. Successful Campaigns: 2 Case Studies 9. Strength and Limits 10. Conclusion

flare.io

## Slide 158

Discussion

###### **Conclusion**

+120M Stealer Logs

flare.io

183

## Slide 159

Discussion

###### **Conclusion**

flare.io

184

## Slide 160

Discussion

###### **Conclusion**

1st LLM Layer 2nd LLM Layer Formatted Description

flare.io

185

## Slide 161

Discussion

###### **Conclusion**

1. Identify IoCs at scale

2. Track campaigns

flare.io

186

## Slide 162

**Conclusion**

###### **Sound Bytes**

**(aka Takeaways)**

- AWARENESS: Saw evidence rarely seen in public: actual stealer log victim desktop screenshots: a previously hard to analyze story-telling artifact

- They provide valuable intelligence for Indicators of Compromise (IoCs), tracking malware activity and understanding broader campaign patterns

- To use LLMs to analyze cybersecurity artifacts **translate analyst** **intui tion into instructions** flare.io

flare.io

187

## Slide 163

What’s next ?
Conclusion - What’s next ?
Software.txt
Processes.txt
Screenshot.jpg
Chrome_HIstory.txt
stealer_log.zip
History
Brave _ HIstory.txt
System.txt flare.io

188

## Slide 164

What’s next ?
Conclusion - What’s next ?
Software.txt
Processes.txt
Screenshot.jpg
Chrome_HIstory.txt
stealer_log.zip
History
Brave _ HIstory.txt
System.txt flare.io

189

## Slide 165

What’s next ? **Conclusion - What’s next ?**

Software.txt

Processes.txt

Screenshot.jpg

History

System.txt

flare.io

190

## Slide 166

Discussion

###### **One More Thing ™**

flare.io

191


> Recovered by OCR — confidence 89/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
191
One More Thing ™
LLM-Based Identification of Infostealer Infection
rs from Screenshots: The Case of Aurora
Vect
Estelle Ruellan
Flare Systems
Montreal, Can:
Abstract—Infostealers exfiltrate credentials, session cookies,
and sensitive data from infected systems. With over 29 million
stealer logs reported in 2024, manual analysis and mitigation at
scale are virtually unfeasible/unpractical. While most research
focuses on proactive malware detection, a significant gap remains
leveraging reactive analysis of stealer logs and their asso.
ciated artifacts. Specifically, infection artifacts such as screen-
shots, image captured at the point of compromise, are largely
overlooked by the current literature. This paper introduces a
novel approach leveraging Large Language Models (LLMs),
more specifically gptto-mini, to analyze infection screenshots to
extract potential Indicators of Compromise (ICs), map infection
vectors, and track campaigns. Focusing on the Aurora infostealer,
we demonstrate how LLMs can process screenshots to identify
infection vectors, such as malicious URLs, installer files, and
jed software themes. Our method extracted 337 actionable
246 relevant files from 1000 screenshots, revealing
key malware distribution methods and social engineering tactics
By correlating extracted filenames, URLs, and infectic
we identified three distinct malware campaigns, demonstrating
the potential of LILM-driven analysis for uncovering infection
workflows and enhancing threat intelligence. By shifting malware
analysis from traditional log-based detection methods to a reac
tive, artifact-driven approach that leverages infection screenshots,
this research presents a scalable method for identifying infection
vectors and enabling early intervention.
Index Terms—LLM, infostealer, malware
I. INTRODUCTION
Infostealers are a type of malware th
computer, and ste credentials, session cook
personal data out of a ser, in addition to other s
information from the host. A:
sents a major threat to corporate and pe
In 2024, Flare reported over 29 million (29,003,537) st
gs posted on cybercrime forums and channels. The st
volur contains undreds of crede:
multiple files per entry, renders manual analysis impractical.
overwhelmin, acking and mitigating
campaigns exponentially challenging for hur
cent years, many of infostealer malware have
evolved beyond their data-exfilt abilities. A notable
development is the inclusion of a screenshot ring fun
tionality, which enables threat actors to hot of the
victim’s device. These screenshots
shortly after the point «
typically captured
fection, with the precise timin,
« selected by the attacker
re Systems
jontreal, Canada
set has amassed over 60 million stealer
infections across millions of devices (see
more than a quarter of these |
approximately 165 million entries, include a "Screenshe
In other terms, over 25% of stealer logs contain a visual
cord of the crime scene at the moment of infection, pror
comprehensive clues and evidence critical to under
tion. These screenshots have the potential
diate insights that can reveal context and subtleties ofter
ed or overlooked in textual b
What may s
he attacker—an intrusive snapsh
n like a trivial fi
the victim's screen—has
an unexpe sid mine for the cyber threat
oem itially, these screenshots may have
1 simple purpose for thr s ge the
iven their infection tactics a
raps wer sful. Howev
become increasingly numerous
idition has become a powerful tool
acking infostealer campaigns. These screenshot
nsig’ in the vic environment at the moment
ction. They can reveal critical information such as the
ited by the victim when the infect dF
f a software, providing invaluable context
to the infection
‘crime scene” images represent a valuable
and investigation. They offer a
que visual me at helps at ts identify and unde
the infection vectors responsible for © nising mil
lions of devices worl Far from bein ¢ byproduct
of the attack, screenshots now represent a key source
of intellig analyzing, and better mititgate
infoste
rise to diverse dete
Malware detection ap; categorized
static signature-ba s (dynamic
Signature-based 4 fundamental appre
binary patterns ¢ malicious files s
le fingerprints. While efficient for known th
| method relies on matching suspicious files
```

## Slide 167

##### Questions?

#### Estelle Ruellan

● Email: estelle.ruellan@flare.io ● Social: linkedin.com/in/estelle-ruellan First to ask a question will get a NorthSec 2025 hardware badge!

#### Olivier Bilodeau

- Email: olivier.bilodeau@flare.io

- Other Hat: https://nsec.io

● Social: @obilodeau.bsky.social

flare.io

192
