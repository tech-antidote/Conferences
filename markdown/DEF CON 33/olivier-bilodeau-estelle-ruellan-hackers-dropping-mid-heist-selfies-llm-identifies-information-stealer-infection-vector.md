---
title: "Hackers Dropping Mid-Heist Selfies LLM Identifies Information Stealer Infection Vector and Extracts IoCs"
speakers: ["Olivier Bilodeau Estelle Ruellan"]
conference: "DEF CON"
conference_full: "DEF CON 33"
edition: "33"
year: 2025
source_pdf: "DEF CON 33/Olivier Bilodeau Estelle Ruellan - Hackers Dropping Mid-Heist Selfies LLM Identifies Information Stealer Infection Vector and Extracts IoCs.pdf"
pages: 166
sha256: "451efb5f4d1bb20882562923fce7538455943b4ed54997cc5e6ee875c1f3675c"
text_chars: 67964
ocr_pages: 56
has_ocr: true
redacted_secrets: 0
ocr_confidence: 86.0
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T07:10:57Z"
---
# Hackers Dropping Mid-Heist Selfies LLM Identifies Information Stealer Infection Vector and Extracts IoCs

**Speakers:** Olivier Bilodeau Estelle Ruellan  
**Conference:** DEF CON 33  
**Source:** `DEF CON 33/Olivier Bilodeau Estelle Ruellan - Hackers Dropping Mid-Heist Selfies LLM Identifies Information Stealer Infection Vector and Extracts IoCs.pdf` (166 pages)


## Slide 1

**Hacker Dropping Mid-Heist Selfies** LLM Identifies  Information Stealer Infection Vectors and Extracts IoC

**Olivier Bilodeau,** Principal Cybersecurity Researcher flare.io flare.io **Estelle Ruellan,** Threat Intelligence Researcher

## Slide 2

###### **Who Are We?**

###### **Olivier Bilodeau**

- 15 years cybersecurity industry experience

- Principal Cybersecurity Researcher at Flare

- Former GoSecure, ESET. Founder MontréHack

- • NorthSec’s President

- Serial presenter: DEFCON, BlackHat, SecTor, Botconf, CERT-EU, AtlSecCon

Honorable mentions:

###### **Estelle Ruellan**

- Cyber Threat Intelligence Researcher

- Mathematics and Criminology Background

- Former student athlete

- Loves data science,  shapes and colors

- Baby serial presenter: NorthSec, ShmooCon, Botconf, Hack.lu, eCrime APWG, EUROCRIME

flare.io

2

## Slide 3

###### **Agenda**

1. The Information Stealer Malware Phenomenon

2. Mid-Heist Selfies

3. The LLM Pipeline

4. Prompt Engineering

5. LLM Assessment

6. Discriminating IoCs

7. Inside the Infostealer Playbook

8. Successful Campaigns: 2 Case Studies 9. Strength and Limits 10. Conclusion

flare.io

## Slide 4

###### **Agenda**

1. The Information Stealer Malware Phenomenon

2. Mid-Heist Selfies 3. The LLM Pipeline 4. Prompt Engineering 5. LLM Assessment 6. Discriminating IoCs 7. Inside the Infostealer Playbook

8. Successful Campaigns: 2 Case Studies 9. Strength and Limits 10. Conclusion

flare.io

## Slide 5

###### **What is an Infostealer? The Malware you (may) have never heard of:**

**User downloads cracked software**

Infostealer grabs:
- credentials
- crypto wallets
- browser Data …
Individual logs are
packaged together

**Malware is executed on victim computer**

**Data exfiltrated to C2 infrastructure**

**Log Files are distributed in Telegram Channels**

<u>Administrative rights NOT required! && No Persistence!</u>

flare.io

**5**

## Slide 6

###### **Stealer Log Structure**

78a5g6fdg.zip

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

flare.io

**6**

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

flare.io

**7**

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
cookie
s
uni34r893.zip
Opera_profile_2.txt
flare.io
8 files flare.io

## Slide 9

###### **Agenda**

1. The Information Stealer Malware Phenomenon

2. Mid-Heist Selfies 3. The LLM Pipeline 4. Prompt Engineering 5. LLM Assessment 6. Discriminating IoCs 7. Inside the Infostealer Playbook 8. Successful Campaigns: 2 Case Studies 9. Strength and Limits 10. Conclusion

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

Screen_011e67e8

flare.io

12


> Recovered by OCR — confidence 87/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Mid-Heist selfies
© YouTube w to install mod menu fortnite pe 2022
! IF YOU HAVE TROUBLES
DOWNLOADING/LAUNCHING FILE JUST TURN OFF
YOUR ANTI-VIRUS ITS ABSOLUTELY SAFE !
FORTNITE HACK | UNDETECTED | FORTNITE MOD MENU | DOWNLOAD FREE
o7 Pp A) Share 4 Download
267 views
FOR
12
```

## Slide 13

**Some examples Mid-Heist selfies**

Screen_50efad93
Us

flare.io

14

## Slide 14

**THE NUMBERS**

###### **Mid-Heist selfies**

Infection screenshots contain all the clues and hints needed to solve the mystery of infection

flare.io

15

## Slide 15

**THE NUMBERS**

###### **Mid-Heist selfies**

11 +15M

Malware Families

Screenshots *

## +25%

of all logs

*Including duplicates

flare.io

17

## Slide 16

**THE NUMBERS**

###### **Mid-Heist selfies**

11 +15M +25% Malware Families Screenshots of all logs * *Including duplicates flare.io 18 flare.io

## Slide 17

###### **Agenda**

1. The Information Stealer Malware Phenomenon

2. Mid-Heist Selfies 3. The LLM Pipeline 4. Prompt Engineering 5. LLM Assessment 6. Discriminating IoCs 7. Inside the Infostealer Playbook

8. Successful Campaigns: 2 Case Studies 9. Strength and Limits 10. Conclusion

flare.io

## Slide 18

###### **Overview of the Pipeline**

Screenshot

1st LLM Layer

Formatted Description

2nd LLM Layer

flare.io

20

## Slide 19

###### **Overview of the Pipeline**

2nd LLM Layer

Live IoC

Theme
Dead IoC

[Vector ; Theme] IoC checking

flare.io

21

## Slide 20

Why 2 Layers ? **Overview of the Pipeline**

Screenshot
1st LLM Layer 2nd LLM Layer
Formatted
Description

flare.io

22

## Slide 21

Why 2 Layers ? **Overview of the Pipeline**

“Identify the infection vector”

flare.io

23

## Slide 22

Why 2 Layers ? **Overview of the Pipeline**

“Identify the infection vector”
LLM

flare.io

24

## Slide 23

###### Why 2 Layers ? **Prompt Engineering**

Screen_011e67e8
26

flare.io


> Recovered by OCR — confidence 88/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Prompt Engineering
@PYoulube how to install mod menu fortnite pe
Screen_011e67e8
! IF YOU HAVE TROUBLES
DOWNLOADING/LAUNCHING FILE JUST TURN OFF
YOUR ANTI-VIRUS ITS ABSOLUTELY SAFE !
FORTNITE HACK | UNDETECTED | FORTNITE MOD MENU DOWNLOAD FREE
D MENU | DC
26
```

## Slide 24

WHY 2 LAYERS ? **Overview of the Pipeline**

1. Visually assess the screenshot

flare.io

27

## Slide 25

###### Why 2 Layers ? **Overview of the Pipeline**

Screen_011e67e8
flare.io
29 flare.io


> Recovered by OCR — confidence 86/100 on the text kept, 68/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Overview of the Pipeline
@PYoulube how to install mod menu fortnite pe 2022
Screen_011e67e8
! IF YOU HAVE TROUBLES
DOWNLOADING/LAUNCHING FILE JUST TURN OFF
YOUR ANTI-VIRUS ITS ABSOLUTELY SAFE !
YW.
FORTNITE HACK | UNDETECTED | FORTNITE MOD MENU DOWNLOAD FREE
I 267 views 8 Dec 2022
wnload =+ Save
—] DOWNLOAD LINK
```

## Slide 26

Why 2 Layers ? **Overview of the Pipeline**

1. Visually assess the screenshot

2.  Point out potential infection vectors based on field knowledge

flare.io

30

## Slide 27

**Why 2 Layers ?**

###### **Overview of the Pipeline**

An LLM can’t just ‘figure it out’: we must translate analyst intuition into instructions.

flare.io

31

## Slide 28

###### Why 2 Layers ? **Overview of the Pipeline**

1. Visually assess the screenshot

2. Point out infection vectors

flare.io

32

## Slide 29

###### **Agenda**

1. The Information Stealer Malware Phenomenon

2. Mid-Heist Selfies 3. The LLM Pipeline 4. Prompt Engineering 5. LLM Assessment 6. Discriminating IoCs 7. Inside the Infostealer Playbook

8. Successful Campaigns: 2 Case Studies 9. Strength and Limits 10. Conclusion

flare.io

## Slide 30

###### The first layer **Prompt Engineering**

Visual Assessment

Web Content

File System

Hybrid

flare.io

34

## Slide 31

The first layer **Prompt Engineering**

###### Web Content

Screen_1c086e2

flare.io

35


> Recovered by OCR — confidence 82/100 on the text kept, 66/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Prompt Engineering Wis
MidJourney 64-bit
>
eo
ct
~
000
How do I make a request using MidJourney's Al?
<3 (@ | Screen_1c086e2
35
```

## Slide 32

The first layer **Prompt Engineering**

###### File System

Screen_4af28ad3

flare.io

36


> Recovered by OCR — confidence 84/100 on the text kept, 61/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Prompt Engineering
File System
Edge
2019
Recycle Bin DuToanéta Théngké Microsoft
& a
Screen_4af28ad3
PowerPoint Chuyen CAD Access
sang Word
Linh Tinh
36
```

## Slide 33

The first layer
Prompt Engineering

File System
The first layer
Prompt Engineering
Screen_23b9d3b8

flare.io

37


> Recovered by OCR — confidence 83/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
37
Prompt Engineering
Please stay online while Office
downloads
File System
@ 33°C Ensoleilé ~ & & DO G4) FRA
13:36
19/01/2023 ac}
```

## Slide 34

The first layer
Prompt Engineering

Hybrid

Screen_29eee3c1

flare.io

38


> Recovered by OCR — confidence 75/100 on the text kept, 57/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
38
The first layer
Prompt Engineering
Hybrid
Qa
© Ten
@es
Bi Documentos #
Bm 25-11-2022
Bm Septiembre 202:
Y @ Dropbox
Ba Espacio familiar
(BB MuvECOM
B& Soporte Tecnico
@ OneDrive - Person
> I Este equipo
Nombre
B win-64.1
Fecha de modificacion
21/11/2022 9:10
21/11/2022 9:09
10/8/2021 7:21
10/8/2021 7:21
Y 7 BE> Este equipo > Descargas > Microsoft Office Crack 2022 > Microsoft Office Crack 2022 v
Tipo Tamafio
Carpeta de archivos
Aplicacion 696320 KB
Extension de la ap. 1.295 KB
Extensi6n de la ap... S71KB
elementos | 1 elemento selecci
@ downoad - MEGA
@ sequridad de Wind..
Screen_29eee3c1
Mostrartodo ) x
```

## Slide 35

###### The first layer **Prompt Engineering**

Scene Description

File Explorer & Installer

URL

Visual Assessment

Browser Tab Identification

Suspicious Elements

flare.io

39

## Slide 36

###### 1<sup>ST</sup> LAYER INPUT PROMPT

**### Main Content:** The first layer Describe the main content visible on the screen, include as much detail as possible. **<u>Prompt Engineering</u>**

**### Files/Programs:**

**Installer:**

Focus on installers or install window, put the name of the file being installed. When there is a name for the installer window, get the name of file/folder or the path.

Focus on file explorer if there is one. Put the names of files and their extensions in this section. If the path of the file explorer reveals **File explorer:** the name of a folder/file, get it. Ignore all desktop programs and icons.Scene Description File Explorer & Installer URL

Seperate filenames by a ",". If there aren’t any file, executable or program put "X".

###### **### URL**

Put all URLs you see. If there aren’t any URLs, put "X". Visual

Assessment **### Browser Tabs Analysis:**

Ignore bookmarks. For each active browser tab in the top row, list in this format:

- **[logo: {logo name}] [text: {visible text}] (meaning/context if apparent)** . If there aren’t any webpage, put "X".

Browser Tab Identification Suspicious Elements

**### Suspicious Elements:**

Highlight any file, executable, program, URL or download link that could contain malware. These could be youtube videos, flare.io blogs, google drive, etc.40 flare.io

## Slide 37

###### **### Main Content:**

The first layer Describe the main content visible on the screen, include as much detail as possible. **Prompt Engineering**

###### 1<sup>ST</sup> LAYER INPUT PROMPT

###### **### Files/Programs:**

###### **Installer:**

Focus on installers or install window, put the name of the file being installed. When there is a name for the installer window, get the name of file/folder or the path.

Focus on file explorer if there is one. Put the names of files and their extensions in this section. If the path of the file explorer reveals **File explorer:** the name of a folder/file, get it. Ignore all desktop programs and icons.Scene Description File Explorer & Installer URL

Seperate filenames by a ",". If there aren’t any file, executable or program put "X".

###### **### URL**

Put all URLs you see. If there aren’t any URLs, put "X". Visual

###### Assessment **### Browser Tabs Analysis:**

Ignore bookmarks. For each active browser tab in the top row, list in this format:

- **[logo: {logo name}] [text: {visible text}] (meaning/context if apparent)** . If there aren’t any webpage, put "X".

Browser Tab Identification

**### Suspicious Elements:**

Suspicious Elements

Highlight any file, executable, program, URL or download link that could contain malware. These could be youtube videos, flare.io blogs, google drive, etc.41 flare.io

## Slide 38

**### Main Content:** The first layer Describe the main content visible on the screen, include as much detail as possible. **Prompt Engineering**

###### 1<sup>ST</sup> LAYER INPUT PROMPT

###### **### Files/Programs:**

**Installer:** Focus on installers or install window, put the name of the file being installed. When there is a name for the installer window, get the name of file/folder or the path.

Focus on file explorer if there is one. Put the names of files and their extensions in this section. If the path of the file explorer reveals **File explorer:** the name of a folder/file, get it. Ignore all desktop programs and icons.Scene Description File Explorer & Installer URL

Seperate filenames by a ",". If there aren’t any file, executable or program put "X".

###### **### URL**

Put all URLs you see. If there aren’t any URLs, put "X". Visual

Assessment **### Browser Tabs Analysis:**

Ignore bookmarks. For each active browser tab in the top row, list in this format:

- **[logo: {logo name}] [text: {visible text}] (meaning/context if apparent)** . If there aren’t any webpage, put "X".

Browser Tab Identification Suspicious Elements

**### Suspicious Elements:**

Highlight any file, executable, program, URL or download link that could contain malware. These could be youtube videos, flare.io blogs, google drive, etc.42 flare.io

## Slide 39

###### **### Main Content:**

The first layer Describe the main content visible on the screen, include as much detail as possible. **Prompt Engineering**

###### 1<sup>ST</sup> LAYER INPUT PROMPT

###### **### Files/Programs:**

**Installer:** Focus on installers or install window, put the name of the file being installed. When there is a name for the installer window, get the name of file/folder or the path.

Focus on file explorer if there is one. Put the names of files and their extensions in this section. If the path of the file explorer reveals **File explorer:** the name of a folder/file, get it. Ignore all desktop programs and icons.Scene Description File Explorer & Installer URL

Seperate filenames by a ",". If there aren’t any file, executable or program put "X".

###### **### URL**

Put all URLs you see. If there aren’t any URLs, put "X". Visual

###### Assessment **### Browser Tabs Analysis:**

Ignore bookmarks. For each active browser tab in the top row, list in this format:

- **[logo: {logo name}] [text: {visible text}] (meaning/context if apparent)** . If there aren’t any webpage, put "X".

Browser Tab Identification

###### **### Suspicious Elements:**

Suspicious Elements

Highlight any file, executable, program, URL or download link that could contain malware. These could be youtube videos, flare.io blogs, google drive, etc.43 flare.io

## Slide 40

###### **### Main Content:**

The first layer Describe the main content visible on the screen, include as much detail as possible. **Prompt Engineering**

###### 1<sup>ST</sup> LAYER INPUT PROMPT

###### **### Files/Programs:**

**Installer:** Focus on installers or install window, put the name of the file being installed. When there is a name for the installer window, get the name of file/folder or the path.

Focus on file explorer if there is one. Put the names of files and their extensions in this section. If the path of the file explorer reveals **File explorer:** the name of a folder/file, get it. Ignore all desktop programs and icons.Scene Description File Explorer & Installer URL

Seperate filenames by a ",". If there aren’t any file, executable or program put "X".

###### **### URL**

Put all URLs you see. If there aren’t any URLs, put "X". Visual

###### Assessment **### Browser Tabs Analysis:**

Ignore bookmarks. For each active browser tab in the top row, list in this format:

- **[logo: {logo name}] [text: {visible text}] (meaning/context if apparent)** . If there aren’t any webpage, put "X".

Browser Tab Identification

**### Suspicious Elements:**

Suspicious Elements

Highlight any file, executable, program, URL or download link that could contain malware. These could be youtube videos, flare.io blogs, google drive, etc.44 flare.io

## Slide 41

The first layer **Prompt Engineering**

Visual Assessment

**Screen_36b3a4c**

flare.io

45


> Recovered by OCR — confidence 73/100 on the text kept, 34/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ESET NODS? ANTIVIRUS CRACK 2023 @ FREE OOWNLOAD @ LICENSE KEY INTORNET SECURITY
@ 100% WORKING
```

## Slide 42

###### **### Main Content:**

The screenshot displays a computer desktop environment with an ESET Security window on the left side, prompting The first layer the user to input a license key. There is a red error message indicating that the entered license key is not correct. On **Prompt Engineering** the right side, there is a YouTube video titled "ESET NOD32 ANTIVIRUS CRACK 2023" which claims to offer a free download of a license key for ESET antivirus software. It includes a description with instructions for installation and cautionary steps such as disabling antivirus and Windows Smart Screen.

**### Files/Programs: Installer:** ESET NOD32 ANTIVIRUS CRACK 2023 **~~File explorer:~~** ~~X~~

Scene Description File Explorer & Installer

URL

###### 1<sup>ST</sup> LAYER OUTPUT

**### URL**

1. https://www.youtube.com/watch?v=HBG5nZQ7ThA

> **###Tabs** Visual

1. {Youtube} : [Download ESET NOD32 ANTIVIRUS CRACK 2023] Assessment

2. {ESET} [License key internet security 100% working]

**### Suspicious Elements:**

- The YouTube video titled "ESETBrowNOD32ser TabANTIVIRUS IdentificatiCRACKon 2023"Suspicious Elementsand the associated download link

- (https://cutt.ly/NOD-32) are highly suspicious, as they suggest accessing cracked software, which typically contains malware.

- The46license key entry <u>prompt</u> in the ESET window may indicate that the user is following instructionsflare.iofrom the

- video to illegally activate software.

## Slide 43

The first layer **Prompt Engineering**

INPUT

Web Content

File System

###### Hybrid

Visual Assessment

Formatted Description

Vector Identification

flare.io

47

## Slide 44

The first layer
Prompt Engineering
Web
Content
File
System
Visual
Hybrid
Assessment
48

INPUT

Formatted
Vector
Description
Identification
flare.io
flare.io

## Slide 45

###### **Agenda**

1. The Information Stealer Malware Phenomenon

2. Mid-Heist Selfies 3. The LLM Pipeline 4. Prompt Engineering 5. LLM Assessment 6. Discriminating IoCs

7. Inside the Infostealer Playbook

8. Successful Campaigns: 2 Case Studies 9. Strength and Limits 10. Conclusion

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

Browser Tab Identification

Suspicious Elements

flare.io

50

## Slide 47

###### The first layer **Evaluation - Browser Tab Identification**

30% 32% 36%

Browser Tab Identification

flare.io

51

## Slide 48

###### The first layer **Evaluation - Browser Tab Identification - Case Study**

**Screen_92ce42b**

flare.io

52


> Recovered by OCR — confidence 79/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Evaluation - Browser Tab Identification - Case Study
TradingView
scrit
Experimente potencia adicional, velocidad adicional y
Screen 92ce42b flexibilidad adicional, todo con la misma UX que conoce y ama.
PT | DESCARGAR ¢ DESCARGAR A DESCARGAR
SM Dara ventanas nara mac OS
52 Despejado an Q Buisqueda a @® | La | o =) 5 A@evo 11/12/202,
```

## Slide 49

The first layer **Evaluation - Browser Tab Identification - Case Study**

\```
### Browser Tabs Analysis:
\```

\```
-[logo: TradingView] [text: Aplicación de escritorio TradingView] (A webpage for the desktop
application of TradingView)
\```

\```
-[logo: YouTube] [text: (15) Tradingview para pc mas rápido] (A video related to using
TradingView on PC)
\```

**`- [logo: Google] [text: 1PrimeOptions] (A tab likely related to trading or financial information) - [logo: WhatsApp] [text: (53)] (Notifications for WhatsApp) - [logo: Google] [text: RePelis24 | Ver Pel...] (A site for watching movies or series) - [logo: Google] [text: Creador de logotipo... (Logo creator link)`** flare.io **`- [unknown logo] [text: Olymp Trade — Pla...] (A financial trading platform)`**

flare.io

53

## Slide 50

The first layer **Evaluation - Solution**

Visual Assessment

File Explorer & Installer

Scene Description

URL

Browser Tab Identification

Suspicious Elements

flare.io

54

## Slide 51

The first layer
Evaluation - Solution
Scene Description File Explorer & Installer URL
Visual
Assessment
Browser Tab Identification Suspicious Elements
flare.io
55 flare.io

## Slide 52

###### The first layer **Evaluation - Solution**

Visual Assessment

File Explorer & Installer

Scene Description

URL

Browser Tab Identification

Suspicious Elements

flare.io

56

## Slide 53

The first layer
Evaluation - Solution

Visual
Assessment

Scene Description File Explorer & Installer URL
85%
Suspicious Elements
flare.io
flare.io

57

## Slide 54

The first layer **Evaluation**

Web Content File System

Hybrid

Formatted
Visual
2nd LLM
Description
Assessment
Layer

flare.io

58

## Slide 55

THE 2ND LAYER **THE LLM LAYERS**

Vector identification + formatting

V [Vector ; Theme] V T
T

**V** **`https://mega.nz/folder/GEkRCKaT#f93dJ6myfe3fENhDS4wqxQ;` T** **<u>`KMSAuto++ v1.8.7 for Microsoft product activation`</u>**

flare.io

64

## Slide 56

###### Getting out the trash **Discriminating IoCs**

[Vector ; Theme]

2nd LLM Layer

flare.io

65

## Slide 57

###### Getting out the trash **Discriminating IoCs**

[Vector ; Theme]

2nd LLM Layer

flare.io

66

## Slide 58

Getting out the trash **Discriminating IoCs**

[Vector ; Theme]

2nd LLM Layer

flare.io

67

## Slide 59

###### Getting out the trash **Discriminating IoCs**

[Vector ; Theme]

2nd LLM Layer

flare.io

68

## Slide 60

Getting out the trash
Discriminating IoCs

Discriminating IoCs
Live IoC
[Vector ; Theme] Theme
IoC checking
2nd LLM Layer
Dead IoC

flare.io

69

## Slide 61

###### Getting out the trash **Discriminating IoCs**

2nd LLM Layer

Live IoC
[Vector ; Theme] Theme
IoC checking
Dead IoC

flare.io

70

## Slide 62

###### **Agenda**

1. The Information Stealer Malware Phenomenon 2. Mid-Heist Selfies 3. The LLM Pipeline 4. Prompt Engineering 5. LLM Assessment 6. Discriminating IoCs 7. Inside the Infostealer Playbook 8. Successful Campaigns: 2 Case Studies 9. Strength and Limits 10. Conclusion

flare.io

## Slide 63

###### Getting out the trash **Discriminating IoCs**

IoC checking

File sharing platforms

YouTube Videos Others

flare.io

72

## Slide 64

###### Getting out the trash **Discriminating IoCs**

IoC checking

Dead IoC

flare.io

73


> Recovered by OCR — confidence 95/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
73
Discriminating loCs
This could be due to the following reasons:
e The file has been removed as it violated our Terms of Service
loC checking
Dead loC
```

## Slide 65

###### Getting out the trash **Discriminating IoCs**

IoC checking

Live IoC

flare.io

74


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
74
Discriminating loCs
loC checking
Save to MEGA Download
Setup
Name
Password - 2025.txt
SoftwareDownload+(Password - 202...
Enter decryption key
Live loC
```

## Slide 66

###### Getting out the trash **Discriminating IoCs**

IoC checking

Live IoC

flare.io

75


> Recovered by OCR — confidence 81/100 on the text kept, 73/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
75
Discriminating loCs
loC checking
18 vww.fixerroryt.com/20:
Q
FiveM Fix GTA5 b3905.exe!sub_1407A07C8 (0x43)!
S& THELITE € LY 02, 2024 JMMENTS
How To Downl
```

## Slide 67

###### Getting out the trash **Discriminating IoCs**

###### IoC checking

Dead IoC

flare.io

76


> Recovered by OCR — confidence 93/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Getting out the trash
Discriminating loCs
loC checking
76
Search
Video unavailable
This content isn't available.
x Dead loC
```

## Slide 68

###### Getting out the trash **Discriminating IoCs**

IoC checking

Live IoC

flare.io

77


> Recovered by OCR — confidence 94/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
77
Getting out the trash
Discriminating loCs
Microsoft Office Crack Free Download Full Version 2022
~ 33 vues 31 oct. 2022
Welcome! Leave a LIKE and SUBSCRIBE if you enjoyed this video!
ARCHIVE PASSWORD: 7521
DOWNLOAD LINK (DIRECT LINK): https://bit.ly/3N8nHDp
loC checking
Live loC
```

## Slide 69

###### Getting out the trash **Discriminating IoCs**

IoC checking

Theme

flare.io

78


> Recovered by OCR — confidence 95/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
78
Getting out the trash
Discriminating loCs
loC checking
Microsoft Office Crack Free Download Full Version 2022
33 vues 31 oct. 2022
Welcome! Leave a LIKE and SUBSCRIBE if you enjoyed this video!
ARCHIVE PASSWORD: 7521
Theme
```

## Slide 70

# **DEMO**

flare.io

## Slide 71

86

flare.io


> Recovered by OCR — confidence 78/100 on the text kept, 68/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
(stealerlogs-ioc-feed) obilodeau@sparkle ~/f/r/s/stealerlogs ioc feed (main)> python -m fetch _screens.refactored pipel
ine. fetch analyze --download-screens --open-screens --openai-response --delay 10
```

## Slide 72

flare.io

87

## Slide 73

88 flare.io

## Slide 74

###### **Agenda**

1. The Information Stealer Malware Phenomenon

2. Mid-Heist Selfies 3. The LLM Pipeline 4. Prompt Engineering 5. LLM Assessment

6. Discriminating IoCs

7. Inside the Infostealer Playbook

8. Successful Campaigns: 2 Case Studies 9. Strength and Limits 10. Conclusion

flare.io

## Slide 75

###### **Lure Themes - Cracked Software**

flare.io

## Slide 76

Infostealer Playbook **Lure Themes - Cracked Software**

$$$

Cracked 0$

flare.io

91

## Slide 77

Infostealer Playbook
Lure Themes - Cracked Software
Cracked
150$
0$
flare.io
flare.io

92


> Recovered by OCR — confidence 96/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
92
Infostealer Playbook
Lure Theme
Paying $150
for lifetime access
to a secure,
legitimate license
from a globally
recognized corporation.
```

## Slide 78

Infostealer Playbook **Lure Themes - Cracked Software**

Threat actors prey on users’ willingness to bypass legitimate licensing fees at the cost of their own security

flare.io

93

## Slide 79

Infostealer Playbook **Lure Themes - Cracked Software**

flare.io

94

## Slide 80

Infostealer Playbook **Lure Themes - Cracked Software**

###### MAINSTREAM

flare.io

95

## Slide 81

###### **Infostealer Playbook - Lure Themes**

###### Targeting mainstream products ensures large pool of potential victims

flare.io

96

## Slide 82

###### **Lure Themes - Gaming Cheats & Mods**

flare.io

## Slide 83

Infostealer Playbook **Lure Themes - Gaming Cheats & Mods**

flare.io

98

## Slide 84

Infostealer Playbook **Lure Themes - Gaming Cheats & Mods**

flare.io

99

## Slide 85

Infostealer Playbook **Lure Themes - Gaming Cheats & Mods**

flare.io

100

## Slide 86

Infostealer Playbook **Lure Themes - Gaming Cheats & Mods**

Weapons
Skins

Mods

flare.io

101

## Slide 87

Infostealer Playbook **Lure Themes**

###### If it’s free and shady, you’re likely the victim

flare.io

102

## Slide 88

**Distribution Strategies - YouTube as a Distribution System**

flare.io

## Slide 89

###### Infostealer Playbook **Distribution Strategies - YouTube as a Distribution System**

**BEST FREE FORTNITE CHEAT 2025 |** **SILENT AIM + ESP | UNDETECTED**

**MICROSOFT 2022 CRACK (GENUINE  + 100% FREE)**

flare.io

104

## Slide 90

###### Infostealer Playbook **Distribution Strategies - YouTube as a Distribution System**

**BEST FREE FORTNITE CHEAT 2025 |** **SILENT AIM + ESP | UNDETECTED MICROSOFT 2022 CRACK (GENUINE  + 100% FREE)**

flare.io

105

## Slide 91

Screen_011e67e8

flare.io
flare.io

106


> Recovered by OCR — confidence 78/100 on the text kept, 57/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
how to install mod menu fortnite pe 2022 x & 8
linkdinktheyc kia DOWNLOAD LINK
S ABSOLUTELY SAFE!
FORTNITE HACK | UNDETECTED | FORTNITE MOD MENU | DOWNI@/AD FREE
$5) SS&B fie) 17 ch a Share ~ Download =+ Save
267 views 8 Decqw022
FORTNITE HACKggNDETECTED | FORTNITE MOD MENUAMAVYNLOAD FREE
```

## Slide 92

###### Infostealer Playbook **Distribution Strategies - YouTube as a Distribution System**

It is free It works Disabling antivirus is needed & safe

flare.io

107

## Slide 93

###### Infostealer Playbook **Distribution Strategies - YouTube as a Distribution System**

It is free It works Disabling antivirus is needed & safe

flare.io

108

## Slide 94

###### Infostealer Playbook **Distribution Strategies - YouTube as a Distribution System**

YouTube’s reach and tutorial-driven-content make it the perfect launchpad for infostealer malware

flare.io

109

## Slide 95

###### **Distribution Strategies - Google Ads**

flare.io

## Slide 96

###### Infostealer Playbook **Distribution Strategies - Leveraging Google Ads**

Software S

flare.io

111

## Slide 97

###### Infostealer Playbook **Distribution Strategies - Leveraging Google Ads**

Google Ads give threat actors a fast lane to users’ trust — by placing malicious content where users expect safety: at the top.

flare.io

112

## Slide 98

###### **Agenda**

1. The Information Stealer Malware Phenomenon

2. Mid-Heist Selfies 3. The LLM Pipeline 4. Prompt Engineering 5. LLM Assessment 6. Discriminating IoCs 7. Inside the Infostealer Playbook 8. Successful Campaigns: 2 Case Studies 9. Strength and Limits 10. Conclusion

flare.io

## Slide 99

Infostealer Playbook Successful Campaigns: ~~3~~ 2 Case Studies

flare.io

115


> Recovered by OCR — confidence 90/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Successful Campaigns: 3 2 Case Studies
IoC - https://mega.nz/folder/GErkCTaT#9dGmye
Theme - Microsoft 2022
Ioc - https://mega.nz/folder/GErkKCTaT#9dGmy
Theme - Microsoft 2022 Cracked Free
IoC - https://mega.nz/folder/GErkCTaT#9dGmye
Theme - Yuki Microsoft 2022 DOWNLOAD
```

## Slide 100

Infostealer Playbook Successful Campaigns: ~~3~~ 2 Case Studies

MidJ0urney Blitz Java 6.3% 5.3%

flare.io

117

## Slide 101

MidJ0urney Blitz Java


> Recovered by OCR — confidence 78/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
J, MidJ@urney
2 Blitz Java
```

## Slide 102

**The Anatomy of a Stealer Log**

flare.io

**Screen_0b3c24da** 128


> Recovered by OCR — confidence 84/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
About Store Gmail images
midjourney prompts with results
midjourney when blending with two text prompts, what do you
put between them.
midjourney what are some of the best user prefer option set
examples
Q. midjourney ai
Q. midjourney bot
midjourney discord
midjourney v5
Q. midjourney api
Google Search I'm Feeling Lucky
Advertising Business How Search works ‘& Carbon neutral since 2007 Privacy Terms Settings
```

## Slide 103

**The Anatomy of a Stealer Log**

**Screen_0a4ffca2**

flare.io

129


> Recovered by OCR — confidence 85/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
©@ Design sans titre - Story Book x . midjourney - Recherche Google +X +
¢>x
Google
@
midjourney x
Q Tous E)images (©) Vidéos’ ® Actualités fF) Livres : Plus Outils
Environ 39 800 000 résultats (
ai.mid-journey.org
https://ai.migjourney.org 3
Get The € Updates - MidJourney
U®rials on Working with Midjourney. Exclusive Updates and Features
Recherches associées
midjourney image = midjourney bot
midjourney ai midjourney #macron
midjourney gratuit | midjourney how to use
midjourney discord midjourney prix
Midjourney
https://midjourney.com - Traduire cette page
Midjourney
"fidjourney is an independent research lab exploring new mediums of thought and expanding
Screen_Oa4ffca2 4¢ imaginative powers of the human species
v
A
Ciel couvert
Midjourney
Midjourney est un laboratoire de recherche
indépendant qui produit un programme diintelligence
artificielle sous le méme nom et qui permet de créer
des images a partir de descriptions textuelles, suivant
un fonctionnement similaire a celui de DALL-E
d'OpenAl. Wikipédia
Créateur : Midjourney
Premiére version : 2022
ENG
FR
10:42 PM
4/19/2023
```

## Slide 104

The Anatomy of a Stealer Log

It is possible that the computer’s security systems may FALSELY trigger

**Screen_1c086e2**

flare.io

130


> Recovered by OCR — confidence 89/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
MidJourney 64-bit
0$/month
Unleash Your Creativity with MidJourney's Al-powered Images
Download for Windows ¥
It is possible that the computer’s
security systems may FALSELY trigger
FAQ.
How do! make a request using MidJourney's Al? +
What stock images can | find on MidJourney Ra
How can | use MidJourney’s images?
Screen_1c086e2
```

## Slide 105

The Anatomy of a Stealer Log

It is possible that the computer’s security systems may FALSELY trigger

**Screen_1c086e2**

flare.io

131


> Recovered by OCR — confidence 74/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
@ Fate | @ Sho | © Mo: | % Abe | G INS | G ENE | FF Tou | FFI Tou | FF tou | [PY Coc | §fy Con | ah Rec | [FI Coc | [I Deh | RY Deh | FY Mo | [79 tow: | [79 tou | @ Ne:
/month
ney 64-bit
It is possible that the computer’s
security systems may FALSELY trigger
How can | use MidJourney’s images?
Screen_1c086e2
```

## Slide 106

132

Screen_2d6e7a1f

flare.io


> Recovered by OCR — confidence 78/100 on the text kept, 67/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
+ $ « Disque local (C:) > Utilisateurs » Sherlybulle » Téléchargements
Affichage Outils d'application
ATIPIK_FRAN! #
° Aujourd’hui (2)
ATIPIK_Schoo #
7 MidSetup(1).
=) —Pngtree—woman archer powerful_6636351.png
to generate st
&| —Pngtree—target shooting_5927062.png
&) Couverture_reels(8).jpg
8) les mots mélés(1).png
&) les mots mélés.png
fl Bureau 8) Les valeurs de votre Instituti.png
&) Carrousel LinkedIn .jpg
Documents
&| ATIPIK.FAM(4).jpg
=! Images
&) ATIPIK.FAM(3).jpg
d Musique
&) Couverture_reels(6).jpg
B Objets 3D &) Couverture_reels(5),jpg
Téléchargement:
Plus tét cette semaine (28)
1 élément(s) 1 élément sélectionné 4,99 Mo = =
Screen_2d6e7a1f W hy M idJou rney?
```

## Slide 107

Screen_6c0eb349

133

flare.io


> Recovered by OCR — confidence 89/100 on the text kept, 35/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
PDF
Mares and Ceeka...
Continuar |
Screen_6c0eb349
12:55 =]
03/08/2024 8)
```

## Slide 108

**Screen_6c0eb349**

134

flare.io


> Recovered by OCR — confidence 81/100 on the text kept, 38/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
PDE
—
1.6 GHz
UMT_UNIS...
is
Screen_6c0eb349
12:55
```

## Slide 109

Screen_6c0eb349

135

flare.io


> Recovered by OCR — confidence 78/100 on the text kept, 50/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
eis | |t is possible that the computer's security
systems may FALSELY trigger
a UMT_Uniso...
(
12:55
```

## Slide 110

###### **The A** **natomy of a Stealer Lo g**

g

How to disable bitdefender antivirus 2023

**Screen_6cf1bf72**

136

flare.io


> Recovered by OCR — confidence 90/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
This video will show you how to temporary disable \ enable
How to Temporarily Disable or Enable Bitdefender TOTAL
YouTube - Nam Anh Cap - 25 jan
innehalla: 2023
ppt How to disable bitdefender antivirus 2023
how to temporarily disable bitdefender 2023 - YouTube
how to temporarily disable bitdefender 2023 ... Gta)_suin ce
YouTube - MR For 1 manad sedar
https://clean-my-pc.com » how-tc Oversatt den har sidan
How to Disable Bitdefender Windows 10 - Clean my PC
Open the Bitdefender Total Security 2019 on your device. - Navigate to the Protection
Features tab and click on the Settings icon under the Antivirus module.
hittps:/Avwww prajwal.org » how-tc Oversatt den har sidan
How to Disable Bitdefender Notifications - Prajwal.org
17 dec. 2022 — Launch the Bitdefender antivirus or Total security tool. - Select Settings and
click General tab. - Turn off the Special Offers and Recommended
https:/Avww.safetydetectives.com Oversatt den har sidan
How to Cancel Bitdefender Subscription (& Get a Refund) in ...
Find Bitdefender under your list of products and click Stop automatic subscription renewal. ... |
recommend Norton — it's my favorite antivirus in 2023
*& kkk Rankning: 9/10 - 13 recensioner
lerade sokningar
Q uninstall bitdefender Q bitdefender alert page
22:36
```

## Slide 111

**Screen_6ddb217b**

137

flare.io


> Recovered by OCR — confidence 90/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Windows Security - o
°5 Virus & threat protection settings
View and update Virus & threat protection settings for Microsoft Have a question?
lone Defender Antivirus. Get help
| ie) Virus & threat protection
This setting is managed by your administrator. Help improve Windows Security
. . Gi feedback
Real-time protection ive us feedbaci
Locates and stops malware from installing or running on your device. You
can turn off this setting for a short time before it turns back on
() Firewall & network protection
6 App & browser control
automatically. Change your privacy settings
B Device security . View and change privacy settings
ey) of for your Windows 10 device.
@ Device performance & health o Privacy settings
Privacy dashboard
sth Family options cy
Cloud-delivered Wotection Privacy Statement
Provides increased and faster protection with access to the latest
protection data in the cloud. Works best with Automatic sample
submission turned on.
Automatic sample submission
Send sample files to Microsoft to help protect you and others from
potential threats. We'll prompt you if the file we need is likely to contain
personal information.
A Automatic sample submission is off. Your device may be —Dismiss
vulnerable.
Submit a sample manually
Tamper Protection
Prevents others from tampering with important security features.
Scree n_6ddb21 7b A\ Tamper protection is off. Your device may be vulnerable, Dismiss
```

## Slide 112

**Screen_6ddb217b**

138

flare.io


> Recovered by OCR — confidence 90/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Windows Security
€
2 Home
| © Virus & threat protection
R Account protection
()) Firewall & network protection
FE) sApp & browser contro!
B Device security
@ Device performance & health
Family options
Screen_6ddb217b
=P Type here to search
% Virus & threat protection settings
View and update Virus & threat protection settings for Microsoft
Defender Antivirus.
This setting is managed by your administrator.
Real-time protection
ps malware from installing or running on your device.
can tum atting for a short time before it turns back on
automatically.
ess to the latest
Provides increased and faster protection with ac
protection data in the cloud. Works bes'
with Automatic sample
submission turned on.
Automatic sample submission
ample file
to Microsoft to help protect you and others fron
| threats, We'll prompt you if the file we need is likely to contain
sonal information.
A Automatic sample submission is off. Your device may be Dismiss
vulnerable.
Submit a sample manually
Tamper Protection
Prever
thers from tampering with important security features.
A, Tamper protection is off. Your device may be vulnerable, Dismiss
& on
Have a question?
Help improve Windows Security
Give us feedback
Change your privacy settings
View and change privacy settings
for your Windows 10 device.
Privacy setting
Privacy dashboard
Privacy Statement
04:13 PM
```

## Slide 113

###### **The** **Anatomy of a Stealer Lo g**

ai.midj0urney or virus

**Screen_6af6791f**

flare.io

139


> Recovered by OCR — confidence 86/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
@ Tips for Waiters.
x oO French Terms Related toF & BS: xX Perfect software for all your visu: X e@ ai.midjOurney.or fake? - Google’ x +
M Gmail
Google
@ Reddit - Dive intoa... GF Discord [J Amazon.de: Low Pri... (@ ChatGPT | Websites [M Tools [J OnePiece | Shopping [| Games Godot
virus fake
Is Midjourney v
What is the most realistic Al art generator? v
Is Midjourney a real Al?
IL Movies & Shows Football
ai.midjOurney or virus
Why is Midjourney no longer free? v
Feedback
Washington Post
https:/Awww.washingtonpost.com > 2023/03/30 > midj
Midjourney is making fake images go mainstream
30 Mar 2023 — The Al image generator Midjourney has quickly become one of the internet's
most eye-catching tools, creating realistic-looking fake visuals ...
2) Decrypt
https://decrypt.co » midjourney-free-ai-image-generati
Midjourney Kills Free Al Image Generator Access After ...
30 Mar 2023 —A “deep fake” is realisticiooking media created by Al by altering images, videos,
or audio to show real people doing or saying things they ...
Vox
https:/Awww.vox.com > technology > ai-image-dalle-o.
unbelievably realistic fake images could take over the ...
Screen_6af6 y g
iar 2023 — Al image generators like DALL-E and Midjourney are getting better and better
at fooling us.
```

## Slide 114

###### **The** **Anatomy of a Stealer Lo g**

ai.midj0urney or virus

**Screen_6af6791f**

140

flare.io
flare.io


> Recovered by OCR — confidence 83/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
@ Tips for Waiters. x Bl French Terms Related toF & BS: xX Perfect software for all your visu: X (3) ai.midjOurney.or fake? - Google > xX + -
@ YouTube M Gmail @ Reddit -Diveintoa.. GF Discord [EJ Amazonde:Low Pri... @@ ChatGPT ff) Websites | Tools [§ OnePiece [| Shopping | Games [ Godot Movies&Shows [ Football ff) Cooking
Google 1. ai.midjQurey.or virus | x|s © Qa £33
virus fake
Is Midjourney v
What is the most realistic Al art generator? v
Is Midjourney a real Al?
Why is Midjourney no longer free?
Washington Post
https:/Awww.washingtonpost.com » 2023/03/30 > midj,
Midjourney is making fake images go mainstream
30 Mar 2023 — The Al image generator Midjourney has quickly become one of the internet's
most eye-catching tools, creating realistic-looking fake visuals ...
2) Decrypt
https://decrypt.co » midjourney-free-ai-image-generati
Midjourney Kills Free Al Image Generator Access After ...
30 Mar 3 —A “deep fake” is realisticiooking media created by Al by altering images, videos,
or audio to show real people doing or saying things they ...
Vox
https:/Avww.vox.com > technology > ai-image-dalle-o
unbelievably realistic fake images could take over the ...
Screen_6af67 y g
ar 2023 — Al image generators like DALL-E and Midjourney are getting better and better
at fooling us.
a PDataDivai
```

## Slide 115

Use Cases

###### **Midj0urney Campaign**

flare.io

141

## Slide 116

MidJ0urney Blitz Java

## Slide 117

Screen_6c0eb349

143

flare.io

## Slide 118

Screen_6f8bc7d4

144

flare.io


> Recovered by OCR — confidence 85/100 on the text kept, 68/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Battle.net
Add Extract To Test » Find Wizard Info
{88 Java_Clientzip - ZIP archive, unpacked size 168 195 366 bytes
Name Size Packed Type Mod
Java Setup.exe 10202752 9641210 Mpxnoxexne 9.221
Screen_6f8bc7d4
11:18
13:19 = ee
```

## Slide 119

**Screen_2b98cef2**

**Screen_6f8bc7d4**

flare.io

145


> Recovered by OCR — confidence 87/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Tl 64-bit Java for Windows X
a java.com/
World of
Warcraft
EPIC
Sjava Télécharger Developer Resources Aide
Ressources d'aide
de Java 8?
épanner Java le Java
A compter du 16 avril 2019.
est sensiblement différent
utilisations a titre gratuit,
H'autres utilisations peuvent
ces Oracle Java. Veuillez lire
it. Une FAQ est disponible ici.
@ E
Test Dele Info «Sean Camment
ZIP archive, unpacked avec un abonnement a Java
Packed
fa Setup.exe
‘Télécharger Java
En téléchargeant Java, vous reconnaissez avoir lu et accepté les conditions du
Contrat de licence Oracle Technology Network License pour Oracle Java SE
Screen_2b98cef2
@ Ala fin de installation de Java, si vous utilisez Web Start, vous devrez peut-étre redémarrer le navigateur (fermer
toutes les fenétres du navigateur et les rouvrir).
Total 1 folder and 10 202 752 bytes in 1 file
Screen_6f8bc7d4
12.2.2023 r.
Recherche
ao Ge
11:18
12/02/2023
1334
12/02/2023
```

## Slide 120

Screen_0ab45c2f

Screen_6f8bc7d4

flare.io

146


> Recovered by OCR — confidence 82/100 on the text kept, 68/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Who spends money like @ octrol fait g NOWICH @ Download Java for Wind Tl 64-bit Java for Windows X
Recherche
Bove sew de Java 8?
YB Imagens
Bm Copturas de |
le Java
compter du 16 avril 2019.
est sensiblement différent
utilisations a titre gratuit,
H'autres utilisations peuvent
ces Oracle Java. Veuillez lire
jit. Une FAQ est disponible ici.
HH Ambiente de #
L Transteréncia #
BE Documentos #
imagens #
avec un abonnement a Java
B® Son Heung Min
Bm The Sims 4
mcc
‘Télécharger Java
Scree n_0a b45c2f En téléchargeant Java, vous reconnaissez avoir lu et accepté les conditions du
1 Contrat de licence Oracle Technology Network License pour Oracle Java SE
# Disco Local (C-
2itens | 1 item selecionado 9,72 MB |
allation de Java, si vous utilisez Web Start, vous devrez peut-étre redémarrer le navigateur (fermer
Q Recherche ao Ge eae
12/02/2023
1 folder and 10 202
```

## Slide 121

Screen_0ab45c2f
Screen_0b87df3b
Screen_6f8bc7d4
flare.io
147 flare.io


> Recovered by OCR — confidence 83/100 on the text kept, 64/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Hl 64-bit Java for Wind
AY \ 3 java.com
® Novo } 10} TL Ordenar
Recherche
Hoje
de Java 8?
le Java
compter du 16 avril 2019.
est sensiblement différent
utilisations a titre gratuit,
H'autres utilisations peuvent
ces Oracle Java. Veuillez lire
it. Une FAQ est disponible ici.
im Son Heung Min
Bm The Sims 4
Documents
= Pictures
New folder
=f fj BS Selected 10 202 752 bytes in 1 file Total 1 folder and 10 202 752 bytes in 1 file
Screen_6f8bc7d4
12.2.2023 r.
```

## Slide 122

Screen_0ab45c2f
Screen_6ab49cefd
Screen_0b87df3b
Screen_6f8bc7d4
flare.io
148 flare.io


> Recovered by OCR — confidence 81/100 on the text kept, 55/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
A Base Nome
MB Java Setuy
Mm Copturas de
Hl Ambiente de #
+ Transferéncia #
BE Documentos #
BB Trabaihos Ba #
B videos *
Bm The Sims 4
«= Selected 10 202 752 bytes in 1 file
Screen_6f8bc7d4
a java.com/
11/02
[64-bit Java for Windows =X
de Java 8?
le Java
compter du 16 avril 2019.
est sensiblement différent
utilisations a titre gratuit,
H'autres utilisations peuvent
12.2.2023 r.
ces Oracle Java. Veuillez lire
it. Une FAQ est disponible ici.
Recherche
12/02/2023
```

## Slide 123

**Screen_7da6278b**

flare.io

149


> Recovered by OCR — confidence 94/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Download Help
Help Resources Download Java for Windows
Version 8 Update 361 (filesize: 40.11 MB)
Release date: January 17, 202
Important Oracle Java License Information
The Oracle Java License changed for releases starting April 16, 2019.
. 7 The T Network A ent fi E is substantially different
from prior Oracle Java licenses. This license permits certain uses, such as personal use and
development use, at no cost -- but other uses authorized under prior Oracle Java licenses may no
longer be available. Please review the terms carefully before downloading and using this
product. An FAQ is available t
Commercial license and support is available with a low cost Java SE Subscription.
F
Download Java
wnloading Java you acknowledge that you have read and accepted the
Screen_7da6278b terms of the
t, you may need to restart your browser (close
```

## Slide 124

###### **Screen_7da6278b**

###### **Screen_7af924bc**

flare.io

150


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Download Help
Help Resources Download Java for Windows
S java Download Developer Resources Help
Help Resources Download Java for Windows
Version 8 Update 361 (filesize: 62.11 MB) Why is Java 8 recommended?
Release date: January 17, 2023
Offline Installation
Trouble downloading?Try the
Important Oracle Java License Information
The Oracle Java License changed for releases starting April 16, 2019.
The Oracle Technology Network License Agreement for Oracle Java SE is substantially different
from prior Oracle Java licenses. This license permits certain uses, such as personal use and
development use, at no cost -- but other uses authorized under prior Oracle Java licenses may no
longer be available. Please review the terms carefully before downloading and using this
product. An FAQ is available here.
Windows 64-bit Users
Do you use both 32-bit and 64-bit
browsers?
Offline Installation Commercial license and support is available with a low cost Java SE Subscription.
Trouble downloading?Try the
offline installer
Screen_7da6278b
By downloading Java you acknowledge that you have read and accepted the
Screen_7af924bc terms of the Oracle Technology Network Agreement for Oracle
brov
{__ When your Java installation completes, if you are using webstart, you may need to restart your browser (close all
browser windows and re-open).
```

## Slide 125

Screen_8a4db042

151

flare.io


> Recovered by OCR — confidence 89/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Download Java for Windows
Version 8 U)
Release dag
= Java Download Developer Resources Help
—
Help Resources Download Java for Windows
What is Java? Version 8 Update 361 (filesize: 62.11 MB) Why is Java 8 recommended?
@ javacom
Information
's starting April 16, 2019.
nent for Oracle Java SE is substantially different
mits certain uses, such as personal use and
. . . thorized under prior Oracle Java licenses may no
Ressources d'aide
Java 64 bits pour Windows fully before downloading and using this
Version 8 Update 361 (taille de fichier : 62.11 MB) Intérét de l'utilisation de Java 8?
Date de publication : 17 janvier 2023
Télécharger Developer Resources Aide
alow cost Java SE Subscription.
Dépanner Ja Informations importantes sur la licence Oracle Java
Aide su . La licence Oracle Java a été modifiée pour les versions publiées 4 compter du 16 avril 2019. el
Le contrat de licence O Technology Network pour Or: a SE est sensiblement différent
des précédentes licences Oracle Java. Cette licence autorise certaines utilisations a titre gratuit,
telles qu'une utilisation personnelle ou pour le développement, mais d'autres utilisations peuvent
ne plus étre disponibles, bien qu’autorisées sous les précédentes licences Oracle Java. Veuillez lire
attentivement les conditions avant de télécharger et d'utiliser ce produit. Une FAQ est disponible ici.
that you have read and accepted the
k License Agreement for Oracle Java SE
Le support et la licence commerciale sont disponibles 8 moindre cout avec un abonnement a Java
SE. webstart, you may need to restart your browser (close all
Télécharger
Contrat de licence chnology Ne!
@_ Ale finde installation de Java, si vous utilisez Web Start, vous devrez peut-étre redémarrer le navigateur (fermer
O Taper ic
```

## Slide 126

Screen_8a4db042
flare.io
152 flare.io

## Slide 127

**Screen_8a102ecd**

flare.io

153


> Recovered by OCR — confidence 88/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
€ CG & google.com/s
[2] TempM - temp mail... {§ Online Phone Num... Your account has b... © Request money fro... @ Receive FreeSMSO... @ SMSPanel t TempMail P Persona §% NEW MIC E MAICRO
Google java x £ DQ &
27 All DB Videos © Ima ? More Tools
s(0
This search may be releva cent activity: F hk AS Java >
java jdk download java Computer software
Ad - https://go java-gapp.space/ ~ Java is a set of computer software and specifications
developed by James Gosling at Sun Microsystems.
which was later acquired by the Oracle Corporation.
that provides a system for developing application
software and deploying it in a cross-platform
computing environment. Wikipedia
App - Java Download
Java - a programming language for creating powerful applications and websites. Java - a
platform that allows you to expand the functionality of your system.
Java - Specifically applications Programming languages: Java. C, C++. Assembly
Programming language and computing platform. Get for desktop applications. language
Initial release date: January 23, 1996
Developer: Oracle, Sun Microsystems, James
Java |_Oracle
Get Java for desktop applications. Download Java - What is Java? Uninstall help. Happy Java
User. Are you a software developer looking for JDK downloads? People also search for
»en Group St
Download Java for Windows
Download or update your existing Java Runtime Environment
“anual download Minecraft Unix WinRAR Minecraft
Screen_8a102ecd v2 manual cownload page. Get the latest version of the Java Bedrock servers
Install Java on Windows More about Java >
This article applies to: Platform(s): Windows 10, Windows &
https://www,java.com How do | install Java
```

## Slide 128

###### **Screen_8a102ecd**

154

flare.io **Screen_0ab87d24**


> Recovered by OCR — confidence 86/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
(S} burp suite pr X
@ Burp Suite z lepit yuysS X 4 Professiona @ burp suite p
€ CG & google.com/searc
iM} TempM - temp mail...
Google
Online Phone Num... Your account has b.. © Request money fro...
java x § Qa
2° All DB Videos [EJ images News ? More Tools
This search may be relevant to recent activity: Search t Fe ack
java jdk download
Ad - https://go java-gapp.space/ ~
App - Java Download
Java - a programming language for creating powerful applications and websites. Java - a
platform that allows you to expand the functionality of your system.
Ad - https://oracle.58226.click) ~
Java - Specifically applications
Programming language and computing platform. Get for desktop applications
Java |_Oracle
Get Java for desktop applications. Download Java - What is Java? Uninstall help. Happy Java
User. Are you a software developer looking for JDK downloads?
Download Java for Windows
Download or update your existing Java Runtime Environment
“anual download
Screen 8a1 02ecd va manual download page. Get the latest version of the Java
https://www.java.com
Install Java on Windows
This article applies to: Platform(s): Windows 10, Windows 3
How do | install Java
java S44 java... parameter
Java -cp java -jar 2&
Bil - https://go.java-gapp.space/ +
Switch to Java - Java Download
Java is a reliable and powerful programming language that provides convenient programming.
Java is a platform for creating analytical and consumer with extensive capabilities.
Bi - http:/www.ikosmo.co.kr/ +
Screen_0ab87d24
```

## Slide 129

**Screen_8a102ecd**

155

flare.io **Screen_0ab87d24**


> Recovered by OCR — confidence 88/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
(S} burp suite pr X
€ Cc
iM} TempM - temp mail...
Google
Screen_8a102ecd
https://www.java.com
@ Burp Suite z
@ google.com,
Online Phone Num... Your account has b... © Request money fro... @ Receive
java x '£@Qa
About 1,930,0 onds)
This search may be relevant to recent activity:
java jdk download
Ad - https://go java-gapp.space/ ~
App - Java Download
Java - a programming language for creating powerful applications and websites. Java - a
platform that allows you to expand the functionality of your system.
Ad - https://oracle.58226.click) ~
Java - Specifically applications
Programming language and computing platform. Get for desktop applications
Java |_Oracle
Get Java for desktop applications. Download Java - What is Java? Uninstall help. Happy Java
User. Are you a software developer looking for JDK downloads?
Download Java for Windows
Download or update your existing Java Runtime Environment
“anual download
va manual download page. Get the latest version of the Java
Install Java on Windows
This article applies to: Platform(s): Windows 10, Windows 3
How do | install Java
Google H44 x +
Google {ono x
AS
“io
java... parameter
java -jar 4! 3
Java -cp
il - https://go.java-gapp.space/ +
Switch to Java - Java Download
Java is a reliable and powerful programming language that provides convenient programming.
Java is a platform for creating analytical and consumer with extensive capabilities.
|
2
S
AS 1417 BOs, java.
Screen_0ab87d24
```

## Slide 130

###### **Screen_8a102ecd**

156

flare.io **Screen_0ab87d24**


> Recovered by OCR — confidence 88/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
(S} burp suite pr X @ Burp Suite ;
4 Professiona
€ Cf google.com/search?q=java&b 821 &bih=833&ei=BwrpY4PXG6KikdUP
iM} TempM - temp mail... Online Phone Num...
@ burp suite p
Your account has b... © Request money fro... @ Receive
This search may be relevant to recent activity:
java jdk download
Ad - https://go java-gapp.space/ ~
App - Java Download
Java - a programming language for creating powerful applications and websites. Java - a
platform that allows you to expand the functionality of your system.
Ad - https://oracle.58226.click) ~
Java - Specifically applications
Programming language and computing platform. Get for desktop applications
Java |_Oracle
Get Java for desktop applications. Download Java - What is Java? Uninstall help. Happy Java
User. Are you a software developer looking for JDK downloads?
Download Java for Windows
Download or update your existing Java Runtime Environment
“anual download
Screen 8a1 02ecd va manual download page. Get the latest version of the Java
Install Java on Windows
This article applies to: Platform(s): Windows 10, Windows 3
How do | install Java
https://www.java.com
G i220 -Google 44 x +
Go gle {ono XxX wena
“+ https://go.java-gapp.space/
Java -c java -jar 34
il - https://go.java-gapp.space/ + aie
Switch to Java - Java Download
Java is a reliable and powerful programming language that provides convenient programming.
Java is a platform for creating analytical and consumer with extensive capabilities.
Screen_0ab87d24
```

## Slide 131

**Screen_8a102ecd**

157

flare.io **Screen_0ab87d24**


> Recovered by OCR — confidence 88/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
(S} burp suite pr X @ Burp Suite ;
4 Professiona
€ Cf google.com/search?q=java&b 821 &bih=833&ei=BwrpY4PXG6KikdUP
iM} TempM - temp mail... Online Phone Num...
@ burp suite p
Your account has b... © Request money fro... @ Receive
This search may be relevant to recent activity:
java jdk download
Ad - https://go java-gapp.space/ ~
App - Java Download
Java - a programming language for creating powerful applications and websites. Java - a
platform that allows you to expand the functionality of your system.
Ad - https://oracle.58226.click) ~
Java - Specifically applications
Programming language and computing platform. Get for desktop applications
Java |_Oracle
Get Java for desktop applications. Download Java - What is Java? Uninstall help. Happy Java
User. Are you a software developer looking for JDK downloads?
Download Java for Windows
Download or update your existing Java Runtime Environment
“anual download
Screen 8a1 02ecd va manual download page. Get the latest version of the Java
Install Java on Windows
This article applies to: Platform(s): Windows 10, Windows 3
How do | install Java
https://www.java.com
G i220 -Google 44 x +
Go gle {ono XxX wena
“+ https://go.java-gapp.space/
Java -c java -jar 34
il - https://go.java-gapp.space/ + aie
Switch to Java - Java Download
Java is a reliable and powerful programming language that provides convenient programming.
Java is a platform for creating analytical and consumer with extensive capabilities.
1 Screen_0ab87d24
```

## Slide 132

**Screen_7af924bc**

flare.io

158


> Recovered by OCR — confidence 94/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
> Java” Download Developer Resources Help
Help Resources Download Java for Windows
Version 8 Update 361 (filesize: 62.11 MB) Why is Java 8 recommended?
Release date: January 17, 2023
What is Java?
Remove older versions
Disable Java
Error messages
Troubleshoot Java Important Oracle Java License Information
Onnentieg The Oracle Java License changed for releases starting April 16, 2019.
5 zs The Oracle Technology Network License Agreement for Oracle Java SE is substantially different
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
terms of the Oracle Technology Network License Agreement for Oracle Java SE
Screen_7af924bc
a When your Java installation completes, if you are using webstart, you may need to restart your browser (close all
browser windows and re-open).
```

## Slide 133

**Screen_7da6278b**

flare.io

159


> Recovered by OCR — confidence 96/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
& Download Help
Help Resources
Offline Installation
Screen_7da6278b
Download Java for Windows
Version 8 Update 361 (filesize: 40.11 MB)
Release date: January 17, 2023
Important Oracle Java License Information
The Oracle Java License changed for releases starting April 16, 2019.
The Oracle Technology Network License Agreement for Oracle Java SE is substantially different
from prior Oracle Java licenses. This license permits certain uses, such as personal use and
development use, at no cost -- but other uses authorized under prior Oracle Java licenses may no
longer be available. Please review the terms carefully before downloading and using this
product. An FAQ is available here
Commercial license and support is available with a low cost Java SE Subscription.
Download Java
By downloading Java you acknowledge that you have read and accepted the
terms of the Oracle Technology Network License Agreement for Oracle Java SE
When your Java installation completes, if you are using webstart, you may need to restart your browser (close all
browser windows and re-open).
```

## Slide 134

###### **Screen_7da6278b**

flare.io
flare.io

160


> Recovered by OCR — confidence 91/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
gojava-gapp.space
& Download Help
Help Resources Download Java for Windows
Version 8 Update 361 (filesize: 40.11 MB)
Release date: January 17, 2023
Important Oracle Java Lic
The Oracle Java License changed for
. . The Oracle Tech gy Network Licer
Offline Installation
from prior Oracle Java licenses. This lice
Trouble downloading?Try the development use, at no cost -- but other
longer be available. Please review the ter
product. An FAQ is available here
Commercial license and support is availal]
By downloading Java you ack
terms of the Oracle Tect
Screen_7da6278b
Oo When your Java installation completes, if you a
browser windows and re-open).
```

## Slide 135

Legit

Screen_7af924bc

###### Malicious

flare.io

**Screen_7da6278b**

161


> Recovered by OCR — confidence 92/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Shave Download Developer Resources Help
Help Resources
Windows 64-bit Users
Do you use both 32-bit and 64-bit
browsers?
Offline Installation
Trouble downloading?Try the
offline installer
a
Screen_7af924bc
{Spore Download Help
Help Resources
Malicious
Screen_7da6278b
Download Java for Windows
Version 8 Update 3
Release date: January 17, ZU.
1 MB) |Why is Java 8 recommended?
filesize: 62.11 MB
product. An FAQ is available here.
Commercial license and support is available with a low cost Java SE Subscription
By downloading Java you acknowledge that you have read and accepted the
terms of the Oracle Technology Network License Agreement for Oracle Java SE
Download Java for Windows
Version 8 Update 36) (fi
filesize: 40.11 MB
product. An FAQ is available
Commercial license and support is available with a low cost Java SE Subscription.
Download Java
By downloading Java you acknowledge and accepted the
terms of the
```

## Slide 136

Screen_8a102ecd

flare.io

162


> Recovered by OCR — confidence 86/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
€ CG & google.com/s ? : rpY4PXx dUPu g KEv a Y ( yy Qe
[2] TempM - temp mail... {§ Online Phone Num... Your account has b... © Request money fro... @ Receive FreeSMSO... @ SMSPanel t TempMail P Persona §% NEW MIC E MAICRO
Go gle java x
®
&
27 All DB Videos © Ima ? More Tools
s(0
This search may be releva cent activity: F hk AS Java >
java jdk download java Computer software
Ad - https: igo gg Mol space! ~ Java is a set of computer software and specifications
developed by James Gosling at Sun Microsystems.
which was later acquired by the Oracle Corporation.
that provides a system for developing application
software and deploying it in a cross-platform
computing environment. Wikipedia
ating powerful applications and websites. Java - a
inctionality of your system.
Java - Specifically applications Programming languages: Java. C, C++. Assembly
Programming language and computing platform. Get for desktop applications. language
Initial release date: January 23, 1996
Developer: Oracle, Sun Microsystems, James
Java | Oracle
Get Java for desktop applications. Download Java - What is Java? Uninstall help. Happy Java
User. Are you a software developer looking for JDK downloads? People also search for
»en Group St
Download Java for Windows
Download or update your existing Java Runtime Environment
“anual download Minecraft Unix WinRAR Minecraft
Screen_8a102ecd v2 manual cownload page. Get the latest version of the Java Bedrock servers
Install Java on Windows More about Java >
This article applies to: Platform(s): Windows 10, Windows &
https://www,java.com How do | install Java .
```

## Slide 137

**Screen_7da6278b**

flare.io

163


> Recovered by OCR — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Download Help
Help Resources Download Java for Windows
Version 8 Update 361 (filesize: 40.11 MB)
Release date: January 17, 2023
Important Oracle Java License Information
The Oracle Java License changed for releases starting April 16, 2019.
. , The Ora Tect gy Network Licer Agreement f acle Java SE is substantially different
Offline Installation
from prior Oracle Java licenses. This license permits certain uses, such as personal use and
development use, at no cost -- but other uses authorized under prior Oracle Java licenses may no
longer be available. Please review the terms carefully before downloading and using this
product. An FAQ is available her
Trouble downloading?Try the
Commercial license and support is available with a low cost Java SE Subscription.
By downloading Java you acknowledge that you h:
terms of the e Techn: Net A
Screen_7da6278b
(When your Java installation completes, if you are using webstart, you may need to restart your browser (close al
browser windows J re-open).
```

## Slide 138

Screen_5efa5fe31

flare.io

164


> Recovered by OCR — confidence 73/100 on the text kept, 59/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
@ Java Client x +
/\ | Java_Client
al Base Nome
~~ @ Barbara - Pessaz
Java Setup=
> [EB Capturas de!
fi Ambiente de #
sb Transferéncia #
164
```

## Slide 139

Screen_0ab4567ef

flare.io

165


> Recovered by OCR — confidence 76/100 on the text kept, 62/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
& Java Client x +
€ > »v MB> Transferéncias > Java_Client
‘ @ Barbara - Pessoz
BB Ambiente de #
sb Transferéncia #
BE Documentos #
@ Masica »
Bi Son Heung Min
Bm The Sims 4
creen_0ab4567ef
2itens | 1 item selecionado 9,72 MB |
165
```

## Slide 140

Screen_0f983eefa

flare.io

166


> Recovered by OCR — confidence 87/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
W (on) @ i try installing java butitde X | +
9a
| w.google.com,
" Google i try installing java but it doesn't work Xx Oa
|
| Q All =) Imag 8 @ Ne jore
s (0.63 seconds)
(a) Temporarily turn off firewall or antivirus clients
Active firewall or antivirus software may prevent Java from installing properly. Remember to
turn your firewall or antivirus software back on when you have successfully completed the
Java install.
https://java.com > d
j 2 Troubleshooting tips for running Java
oad > help » troub
@ About featured snippets -
People also ask
How do | force Java to install?
Screen_0f983eefa
Ai Home Name
166
```

## Slide 141

## 19h

flare.io

167

## Slide 142

###### Use Cases **Blitz Java Campaign**

flare.io

168

## Slide 143

Use Cases **Successful Campaigns**

flare.io

171

## Slide 144

Use Cases **Successful Campaigns**

Threat actors rely on simple psychological tactics—because they still work.

flare.io

172

## Slide 145

###### **Agenda**

1. The Information Stealer Malware Phenomenon

2. Mid-Heist Selfies 3. The LLM Pipeline 4. Prompt Engineering 5. LLM Assessment 6. Discriminating IoCs 7. Inside the Infostealer Playbook

8. Successful Campaigns: 2 Case Studies 9. Strength and Limits 10. Conclusion

flare.io

## Slide 146

Discussion **Strength and Limits**

The screenshots embody both our greatest strength and our primary limitation

flare.io

174

## Slide 147

###### Discussion **Strength and Limits**

flare.io

175

## Slide 148

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

## Slide 149

###### Discussion **Strength and Limits**

flare.io

177

## Slide 150

Discussion **Strength and Limits**

TRADITIONAL MALWARE
LLM
ANALYSIS
Works w/o Code Signatures
Robust against Code Changes*
Cross Family Friendly
Works w/o Screenshot

flare.io

178

## Slide 151

Discussion **Strength and Limits**

Existence

flare.io

179

## Slide 152

Discussion **Strength and Limits**

Existence

Quality

flare.io

180

## Slide 153

Discussion **Strength and Limits**

###### Existence

Quality

flare.io

181

## Slide 154

Discussion **Strength and Limits**

TRADITIONAL MALWARE
LLM
ANALYSIS
Works w/o Code Signatures
Robust against Code Changes*
Cross Family Friendly
Works w/o Screenshot

flare.io

182

## Slide 155

Discussion **Cost and Speed**

5-10s 0.003$

processing per image

Cost for 100k images: 300$

flare.io

183

## Slide 156

###### **Agenda**

1. The Information Stealer Malware Phenomenon

2. Mid-Heist Selfies 3. The LLM Pipeline 4. Prompt Engineering 5. LLM Assessment 6. Discriminating IoCs 7. Inside the Infostealer Playbook

8. Successful Campaigns: 2 Case Studies 9. Strength and Limits 10. Conclusion

flare.io

## Slide 157

Discussion **Conclusion**

+120M Stealer Logs

flare.io

185

## Slide 158

Discussion **Conclusion**

flare.io

186

## Slide 159

Discussion

###### **Conclusion**

1st LLM Layer Formatted Description

2nd LLM Layer

flare.io

187

## Slide 160

Discussion **Conclusion**

#### 1. Identify IoCs at scale 1. Track campaigns

flare.io

188

## Slide 161

**Conclusion**

###### **Sound Bytes**

**(aka Takeaways)**

• AWARENESS: Saw evidence rarely seen in public: actual stealer log victim desktop screenshots: a previously hard to analyze story-telling artifact

- They provide valuable intelligence for Indicators of Compromise (IoCs), tracking malware activity and understanding broader campaign patterns

- To use LLMs to analyze cybersecurity artifacts **translate**

- 189 **analyst intuition into instructions**

flare.io

189

## Slide 162

What’s next ?
Conclusion - What’s next ?
Software.txt
Processes.txt
Screenshot.jpg
Chrome_HIstory.txt
stealer_log.zip
History
Brave_HIstory.txt
flare.io
System.txt
flare.io

190

## Slide 163

What’s next ?
Conclusion - What’s next ?
Software.txt
Processes.txt
Screenshot.jpg
Chrome_HIstory.txt
stealer_log.zip
History
Brave_HIstory.txt
flare.io
System.txt flare.io

191

## Slide 164

What’s next ? **Conclusion - What’s next ?**

Software.txt

History

Screenshot.jpg

Processes.txt

System.tx t

flare.io

192

## Slide 165

###### Discussion **One More Thing**

flare.io
flare.io

193


> Recovered by OCR — confidence 90/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
One More Thing ™
193
LLM-Based Identification of Infostealer Infectio
Vectors from Screenshots:
Estelle Ruellan
Flare Systems
Montreal, Ca
Abstract—Infostealers exfilirate credentials, session cookies,
and sensitive data from infected systems. With over 29 million
stealer logs reported in 2024, manual analysis and mitigation at
scale are virtually unfexsible/unpractical. While mast research
focuses on proactive malware detection, significant gap remains
leveraging reactive analysis of stealer logs and their asso-
ciated artifacts. Specifically, infection artifacts such as screen:
shots, image captured at the point of compromise, are largely
overlooked by the current literature. This paper introduces
approach leveraging Large Language Models (LLMs),
more specifically gptto-mini, to analyze infection screenshots to
extract potential Indicators of Compromise (oCs), map infection
vectors, and track campaigns. Focusing on the Aurora infostealer,
nstrate how LLMs can process screenshots to identify
m vectors, such as malicious URLs, installer files, and
exploited software themes. Our method extracted 337 actionable
URLs and 246 relevant files from 1000 screenshots, revealing
key malware distribution methods and social engineering tactics.
By correlating extracted filenames, URLs, and infection themes,
we identified three distinct malware campaigns, demonstrating
the potential of LLM-driven analysis for uncovering infection
workflows und enhancing threat intelligence. By shifting malware
based detection methods to a reac
this research presents a scalable method for identifying
vectors and enabling early intervention.
Index Terms—LLM, infostealer, malware
I. INTRODUCTION
Infostealers are a type of malware that infect
computer, and steal all credentials, session cook
ersonal data out of a browser, in addition to other s
information from the host. As such, infostealer mal
sents 2 major threat to corporate and personal ide
In 2024, Flare reported over 29 million (29,003,537) st
logs on cybercrime forums and channels. The
containing hundreds of credentials and
manual analysis impractical
ug and mitigating
stealer mal e have
abilities. A notable
on of a screenshe f
which enal
victim’s device. These screenshots are typically ca
shortly after the point of infection, with the pr
on the offset selected by
Aurora
dataset has amassed over 60 million stealer b
turing infections across millions of devices (see
Table 1). In particular, more than a quarter of these lo;
approximately 165 million entries, include a "Screenshot
In other terms, over 25% of stealer lo, isual
‘cord of the crime scene nt of infection, pro
amprehensive clues and ev cal to understan
ection tial to de
diate insights that can reveal context and subtleties ofter
missed or overlooked in textual logs
What may seem like a ¢ perspective of
the attacker—an intrusive snaq the victim's screen—has
be an unexpected gold mine for the cyber threat
smmunity. Initially, these may have
a simple purpose for threat actors: to gauge the
iveness of their infection tactics mine which
become increasingly numerous
has become a po
tealer camp se screenshots offer unfil
imo the vic ment at the mm
They can reveal umation such
i by the victim when the infection occur
taller of a software, provid
to the infection
se untapped "crime scene es represent a valuable
for further a s estigation. They off
that helps analysts identify and un
s responsible for compromising mil
jons of Far from being a mere bypro
of the attack screenshots now represent a key source
of intelligen ind bette
PREVIOUS WORK
olution of malware ar
tion methodolog
of memory analysi (6). [7]
Signature-based remains a fundamental appre
where binary patterns ted from malicious files
le fingerprints. While at for known the
pethod relies on matching suspici
```

## Slide 166

##### Questions?

### Estelle Ruellan

● Email: estelle.ruellan@flare.io

● Social: linkedin.com/in/estelle-ruellan

### Olivier Bilodeau

● Email: olivier.bilodeau@flare.io

First to ask a question will get a NorthSec 2025 hardware badge!

- Other Hat: https://nsec.io

● Social: @obilodeau.bsky.social

flare.io

194
