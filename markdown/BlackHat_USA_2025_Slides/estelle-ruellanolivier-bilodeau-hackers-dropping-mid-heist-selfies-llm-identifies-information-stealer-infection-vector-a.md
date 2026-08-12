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
text_chars: 83853
ocr_pages: 61
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T22:54:49Z"
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Mid-Heist selfies
© YouTube
12
! IF YOU HAVE TROUBLES
DOWNLOADING/LAUNCHING FILE JUST TURN OFF
YOUR ANTI-VIRUS ITS ABSOLUTELY SAFE !
FORTNITE HACK | UNDETECTED | FORTNITE MOD MENU | DOWNLOAD FREE
o=. = on
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Prompt Engineering
© YouTube how to install mod menu fortnite pe
link a2: ae
1 IF YOU HAVE TROUBLES
DOWNLOADING/LAUNCHING FILE JUST TURN OFF
YOUR ANTI-VIRUS ITS ABSOLUTELY SAFE !
Le ————E— ee re |
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Overview of the Pipeline
GP Youtube how to install mod menu fortnite pe 2022
TL
load
d
linkdingtie
1 IF YOU HAVE TROUBLES
DOWNLOADING/LAUNCHING FILE JUST TURN OFF
YOUR ANTI-VIRUS ITS ABSOLUTELY SAFE !
a v
FORTNITE HACK | UNDETECTED | FORTNITE MOD MENU DOWNLOAD FREE
FORTNITE O= a
267 views 8 Dec 2022 Zo Tat T ™ A — Z
snl Ct sanianee T_) DOWNLOAD LINK
aT TY HALE I
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Prompt Engineering Web Content
“mA
MidJourney 64-bit
>
or
ct
Ss
~
i~
000
lf
le.
— 0555
A RA EMD dspa2023 F
euP@cmaacecds
13°C an
@ \isceux Bm & Rechercher
32
```

## Slide 32

The first layer

###### **Prompt Engineering**

###### File System

flare.io

33

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Prompt Engineering
Rm @ 5
Zalo
Admin
3
This PC
rs
Network
Recycle Bin
Control
Panel
6c Cée
ie)
ABBYY
FineRead.
Sey
, >|
: >
&
leaner
@
P
a
Project
‘SAP2000 16
Sketchup
2019
Microsoft
Edge
khd
ASS
cPuID
CPU,
Du Toan Eta
Style Builder
2019
A
Théng ke
cét thé.
~$
THLKALY.
©
Microsoft
Edge
H®s
ETABS 18
Foxit PDF
Reader
D
Google
Chrome
LayOut 2019
PDF24
oF
PowerPoint Chuyen CAD
sang Word
UltraViewer
Unikey
a
vic media
player
Word
xa
a
Excel
=>
A
a
Access
Drawing.d.
Drawingi.d.
mhkalsxy.
yidAMev.
File System
This PC
HEP TTT
Documents
Huéng dan dd an tét nghiép ¢
THUYETMINH
OneDriv DuToanéta
Documents Program Fil
Hinh anh
‘Tap pO AN DRIVER
LAM vie
this Pc
B 3D Objects
Bi esttop
2) Documents
Lp
Music
=| Pictures
Hi Vice
de Acer (C)
= luv tras)
# Network
Program Files (x86
Linh Tinh
55)
```

## Slide 33

The first layer

###### **Prompt Engineering**

###### File System

The first layer
Prompt Engineering

flare.io

34

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
34
Prompt Engineering
GV idocem zc)
UNIVERSTTE
SAINTTHON
EXOIEXE
NAISONS ISG
Psrermetres
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
55)
The first layer
Prompt Engineering
http://
ooo
Ng
Hybrid
[eis waa las BCA Ame © Light Term fy Lear tos = Arp © Rest @ You! @ VO Odo © se Wit Mice O Suse a Mic fil Soft @ tx O con } =e)
=
Cc | Gl) @ meganz/file/DZxXBB5I¥iNTbuEPAK83I-SBIx11LAxY¥mGJ9IigZZSItjTc3521 } ele shar ao =
BB Mikrotik Bm Groficas MB OLT MB OD00 ©) Testing © Saifo @ ISP- Jira [B Trello 9 Coreo:Rafa §%% Muvecom ¢P Webmail Fastcom [i] Geo. @ Whaticket €$ Drive @ less [i Futbol Libre TV »
@& meca
o: = ay
Bi Microsoft Office Crack 2022
@® Nuevo ~ x Oa GQ @ W WW Ordenar-~ Sver~ s+
€ > Y D  MP> Este equipo > Descargas > Microsoft Office Crack 2022 > Microsott Office Crack 2022 v
ME Desttop + Nombre Fecha de moditicacion Tipo Tamanio
+ Descargas # Wm cata 21/11/2022 9:10 Carpeta de archivos
BB Documentos #
Bl @fomicvell 21/11/2022 909 Aplicacion 696.320 KB
Biimagenes #
Papas B vin-32.1 10/9/2021 7:21 Extension dela ap.. 1295 KB
BB Hallo Rata B win-64.ai1 10/8/2021 7:21 Extensi6n de la ap. S71KB
Bm Manuales
Bu Septiembre 202:
¥ 9 Dropbox
Bm Espacio familiar
Ba HALO
Ba Muvecom
BM Soporte Tecnico
@ OneDrive - Person
> I Este equipo
4.lementos | 1 elemento selecciofjsdo 680MB |
BE Microsoft_Office Cr.rar
= @
QB wrarsapp
BEE Microsoft office cr. @ muvecomer2820. GF Download- MEGA. BP Seguridad de Wind.
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Pe x caressa « = . +
q c O «© pxttenn G we. Ser,nmw#sctd @ «em =
(hme ete ET © whee Nierte Peewee Trey (term Ge - | a -
© foulube eset peel? antivirus license key 2003 > ‘ » oO  ]
Yo ore “we v Lm kL os
ESET NODS2 ANTIVIRUS CRACK 2023 @ FREE OOWNLOAD @ UCENSE KEY INTORNET SECURITY
@ 100% WORKING
“ Eng Civé Cantos Heanque 6 eS ie Dp > Cantihds Le
‘9 038 verestircacers € tet 2573
Ret Lowe OLD omed DESIRE pe Crqueed Fee etew
Carne feerwon Fre
@ OR Ors Lee (OEE LNeKy Fepe weet WCE?
Teen of vps toe he ek to week
cate we bie ptthcew.
0 yas carn Gowedane / etl (Re archee pow need wx
\ (hamahe / emmeve etrta Ties fs coTpitety Ceary
3. tl you cartt gowntnadd ty to cogy fe Bet are Sownined using another browner
2 Ceeette Widows Great Screen, or well os updete the Vinal 0+ package
4 Update HET Mersewert to 4.5 version
How to eet?
1 Phe Schageee
2 Congiete tt eteee
De, cory)
@ wiatice weeeomey
tags (gears)
east FOC 2) antvesteest Pet) athens ioonee bey 20 eect Saxtl) artvires borane Grypseet set rect) kore eeyeeet fet ateina
crwes bepy 209 Soweto! aed busted cent nod) ete usenet soc)? bya ent welt? eyeeet Pierwt warhardvem well) rect
beprodh) ethtus keyeeet soci) etvirus bcense try Bet reenact sacl? etvres cove sive veneer rod) metre XI | set
pedi’ Bcercms 287 | geet rect? boencies rrarso 200 | geet socll? arevres fee Scerecactvaton bey cf cnet socll? tye eset etl?
— Beare fry DEceree cnet port)? fetes M0 Lemet soll? ectvedoenet wcll? eens securty boewes try full wertion beter update
w VW 90T | TPPPT? cnet noe? eetve decane cect nod) etetus | Lees red reeset securty }4 cnet sod? etvews |) telcos
a cnet not Towel eet? 11 y ecthes cent rod? 2020," heeet od? eetyeus PTT 2271. 2002 | eeteteces y rete comes ree /
peenre Of 200 Leset sont? even tester red 0 evien esta ow bo rirtal ard ectvete Cort wl? art eee i fore eet red
evtucedt rod) MTL cect red 0 eviewun Goer bey 8.4 vor lett apiwtics POINTE?) cect eT? eeeras borer bry DID bee
e@eeqgqrFrnmaanenvre ves QC rates 40 oe ©
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
49
Evaluation - Browser Tab Identification - Case Study
- ) 15°C
Despejado
TradingView
‘scritorio
SS
rey
od
eS
Experimente potencia adicional, velocidad adicional y
flexibilidad adicional, todo con la misma UX que conoce y ama.
DESCARGAR oO DESCARGAR DESCARGAR
HH « A
GM Para ventanas | | WR nara mac os na lini
Bm =O Bisqueda BPeaeme acs
A@a Frond ee
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
71
Discriminating loCs
loC checking
Save to MEGA Download
ES “~Password - 2025.txt
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
72
Discriminating loCs
~
2
>
di
loC checking
fA 8 htt ww.fixerroryt.com/202
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Getting out the trash
Discriminating loCs
@) YouTube Search
©
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Getting out the trash
Discriminating loCs
©
it
loC checking
74
Microsoft Office Crack Free Download Full Version 2022
Oem
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Getting out the trash
Discriminating loCs
Microsoft Office Crack Free Download Full Version 2022
Qe
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
=. Jul24 1542 es @ @ A @ + GD & = & G100%
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Infostealer Playbook
Lure Themes - Gaming Cheats & Mods
__ FORTNITE
RE SHIN SIVAPPER!
: f \s: Skin Swapper
| A sure Pires § —Eeaayack gP wrogs
wears
fe - el |
an PES ee |
```

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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Infostealer Playbook
Lure Themes - Gaming Cheats & Mods
FORTNITE
RET TER
SHINECRRLT =
OR ECRREN
```

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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
GP YouTube ©
linkdinitheye de oc DOWNLOAD LINK
inti httes telegrauoh/ FURI NITE-HALR-FREE-DOWANLOAD
BLES
ot, VE PASSW rae shozches
im pa’ fe [ } i| \ ASSVJURK SNO ZONE Pacnins miesust TuRn oFF ‘
S ABSOLUTELY SAFE!
ssl hall y = i bed le
FORTNITE HACK | UNDETECTED | FORTNITE MOD MENU | DOWNIS/AD FREE
$5) SS&B nha 17 op AY Share + Download =+ Save
22
267 views 8 DY
FORTNITE HACRAMPNDETECTED | FORTNITE MOD MENU. | OAD FREE
PF) DOWNLOAD LWkK@aers in ,sricatee
& ARCHIVE PA ORD: shgzchez
Car worrmney fat
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Infostealer Playbook
Distribution Strategies -
Software S Q
fama,
http://
[peeps
[http:// .
(http:/7 ¥
```

## Slide 97

**The Anatomy of a Stealer Log**

flare.io

109

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
4
gle
at — — — s
sans titre - Story Book x midjourney - Recherche Google X +
€¢ > C  & googlecom/search?q= { OM O&0q={O00&aqs=chr.. 9 @ *k* OF &
?q=midj = =midj = 157j0i
@ google.com/search?q=midjourney&rlz=1C1VDKB_frFR1054FR1054&0q=midjurny&aqs=chrome. 1.6915 7j0i M Gmail @@ YouTube ge XS
idj Google {ono xX Sw eDa
midjourney x §&§ g
AS
MAY Ol HO] BAst QE As
Q Tous Images () Vidéos W@ Actualités © Livres i: Plus
x
uvert
Environ 39 800 000 résultats
Sponsorise
Sponsorisé
© ai.mid-journey.org
https://ai.mid-journey.org
an a4et Ss
java ANH
java FEA
Java -cp
Aye Che eo
javazt
java ... parameter
java -jar 23
Aer aS
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
2B - http:/www.ikosmo.co.kr/ +
StHZABES| Of O'TH7H EH - java - ikosmo.co.kr
3H|X|21100%, TERA, PAR, NOt, ABM TRA AS, aXrraa Ae
SLSATSFEA7IS, 100% SH SH, 7IZSE AS 1:17, java.
BAMA HHS SAE AMS|RSUCH et 19M] Oats] ASAeS AVISS So SE Ais B+ ASY
ct
Lolz ol
Midjourney is an independent research lab exploring new mediums of thought and expanding aimee 84) Jclels
the imaginative powers of the human species.
https://www.java.com > ... ¥
= "% Java C}2BE
ava yi gin whee 8
an = = e
mm QO Search iki wu Ouet
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
About Store Gmail Images
Q. midjourney x UO)
midjourney prompts with results
midjourney when blending with two text prompts, what do you
put between them.
midjourney what are some of the best user prefer option set
examples
Q  midjourney ai
midjourney bot
midjourney discord
Q
Q
Q midjourney v5
Q. midjourney api
Q
midjourney free
Q  midjourney v4
Google Search I'm Feeling Lucky
Report ingppropriste predictions
Advertising Business How Search works ‘& Carbon neutral since 2007 Privacy Terms Settings
```

## Slide 104

###### **The Anatomy of a Stealer Log**

flare.io

127

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ Design sans titre - Story Book x .  midjourney - Recherche Google X +
¢>x
Google
|
1c
» *
Ciel couvert
HQ
@
midjourney x<
Q Tous E)Images (G) Vidéos ©) Actualités [Livres i Plus Outils
Environ 39 800 000 résultats (
Sponsorisé Ss p 2) n so ri se
ai_mid-journey.org
hittps://ai + org
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
— : : “1  s 1
@@ google.com/search?q=midjourney&rlz=1C1VDKB_frFR1054FR1054&o0q=midjurny&aqs=chrome. 1.6915 7j0i10i433i51213j0i 101131143315 1212j01101512j5.5553j0j7&iso... | WW & oO 2
£33 $33 Connexion
Y A
;
aut
¥
Me
{2} Plus d'images
Midjourney <
Midjourmey est un laboratoire de recherche
indépendant qui produit un programme d'intelligence
artificielle sous le méme nom et qui permet de créer
des images a partir de descriptions textuelles, suivant
un fonctionnement similaire a celui de DALL-E
d'OpenAl. Wikipédia
Créateur : Midjourney
Premiére version : 2022
HH Q Search Bway L Q a © rt | @ 33 B. | € a Zo ) eS @ papi
```

## Slide 105

The Anatomy of a Stealer Log

It is possible that the computer’s security
systems may FALSELY trigger

flare.io

128

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ Fat
é
© She
Cc
© Mo: | $f Abe | G INS | G FNA | [FJ Tou | [FY Tow | FRY Tou | FF Coc | FR Con | ih Rec! | FF Coc
@ ai.mid-journey.org/?gclid=EAlalQobChMI_NKlsu7C_glVEQSiAx3DcQzSEAAYASAAEgJAwPD_BwE
| FE Dek | GRY Dek | £4 Mo: | FRI tour | EP tour |G) Nev | ey Tire | T tus: | FJ vot | @ A | @ sec | © His: | BH oA x +
“A
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ Fatr | © Sho | © Mo: | $4 abe | G INS | G FNE | FY Tow | FY Tow | [PY Tow | [PY Coc | GRY Con | a) Rec! | FP} Coo | FJ Dek | [AY Del | PA Mo: | [PI tour | FRI tou |G New | ew Tire | T ths | FY vot | @ ai | @ sec: | © His: | FH OA x + “ = x
€ CG @ ai.mid-journey.org/?gclid=EAlalQobChMI_NKisu7C_gIVEQSiAx3DcQz5EAAYASAAEg/AwPD_BwE G & 2 x & Oh & (Metreajour
\\
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ra
4
Gérer Téléchargements
| Fichier | Accueil Partage
+t e« Disque local (C:) » Utilisateurs >» Sherlybulle » Téléchargements
Affichage Outils d'application
ATIPIK.FRAN'x¢ ® = Nom las
ATIPI \ ‘ -
e EI a0 v Aujourd'hui (2)
ATIPIK_Sch
M | d suit Bi Midsetupo§ g
ATIPIK-Plante # 3
MidSetup.ex
PERSO ad
; ier (14) o
Innovative Al-powered program th fein Fi) Kicepoge-Sitisiexe
to generate st Egoistement v6)
|m] —Pngtree—woman archer powerful_6636351.png
Etablissement-vi
&| —Pngtree—target shooting_5927062.png
&| Couverture_reels(8).jpg
e |m] Couverture_reels(7).jpg
(-) MidSetup.exe 3s vs
&] les mots mélés(1).png
a] les mots mélés.png
&) Les valeurs de votre Instituti.png
Bureau
|g] Carrousel Linkedin .jpg
|=] Documents
a) ATIPIK.FAM(4),jpg
=) Images 5
&) ATIPIK.FAM(3).jpg
J) Musique |w) Couverture_reels(6).jpg
B Objets 3D &) Couverture_reels(5),jpg
} Téléchargement:
Bg Vidéos .
«| Couverture_reels(4).jpg
= Disque local (C:) ee ee ee ee mM:
v < >
Plus tot cette semaine (28)
1 291 élément(s) 1 élément sélectionné 4,99 Mo
Why MidJourney?
```

## Slide 108

131 flare.io

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
a
or = la
teeta Meee Chrome,
=~ BA SE 2),
SS a 2 : a
Este Holal/PN mumOceanofgams ReisideloanemmmnViC Tnternet
rece : ine Downton
ray ~
+) ~ j o)
: Flea i F 2
a fst. &
2 Tt 7%
M nO < o2,
ViSEOMN SagrauaiVer
q a
~~ = a F,
> © a
=a Om &
[=
on
. Ne! os
am hid
OitSem=Re.. Nandipha808
Mares and Ceeka...
Chromest..
“Splan 70
bso EBIIMGST One a Ree chr
TKIMeN Marine
3
PDF
I
529072024 1%
UMT_UNIS...
ey
UMT_Uniso...
Disable antivirus and try again
O\mscoreei.dl
Continuar |
updates
Blacklist
12:55
A G tq) POR o3/oa/2024 8)
```

## Slide 109

132 flare.io

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
——— e ———et x
“a fe. >) OY | _ =
A av —F i .
Z ' @ Po Be am kia
a Cds Lt ol :
HerciliOumma he eknd sum GOOO|cmmNENeW folder mmmmsPlan/0) Torrents PsiphionPro sy Novo(a) Splan 70 ) Chromest. UtSem=Re.. Nandipha808
(hicini=
Vasco Ouane) Live At Sohne Documenta. ip cde * Mares and Ceeka...
‘PDE
_
1290720241%
1.6 GHz
UMT_UNIS...
is
UMT_Uniso...
\mscoreei.dl
updates
12:55
ao me Om AP OG Re ~ : Gm) FI EE] POR gsog/2004 FB)
```

## Slide 110

133 flare.io

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
“aap ae
WOSre © » te
da ent Tents,
oe Newrolders ptln70 Llorrentees PsiphonPro E Splans70) Ghromest.. OifSem=Re.. eet ev
AG ey ae Document... Mares and Ceeka..
ne
ems | |t is possible that the computer's security
systems may FALSELY trigger
;
200720241 me Sinn) Hercilio UMT_UNIS...
is
ig
ay UMT_Uniso...
(
Dente DX
= ~~
‘ | >
> a 7 if
P y id
Bluestacks imusc isplany70) > vl - o@) Pe G3.01 Somme Lagrimas.d ar
. , n ke
Blacklist updates
Moltieinstave
12:55
“A G fa 0) POR 9308/2024 8
```

## Slide 111

###### **The A** **natomy of a Stealer Lo g**

g

How to disable bitdefender antivirus 2023

flare.io

134

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ae HOW NE GOt OVEF 3 DRLIUN VIEW: A | Se ROCECH Us cUcy nsiavauon anc A | Mey LINUX ROGEChI G.co IN€ secure A | OS (NNedaddningar ae je NOW 00 Gisable OnGerencer anuv: A
iia rl
€ > GZ &@ google.com/search?q=how+to+disable+bitdefender+ antivirus +2023 QEl-crgSU Swved=OahUKEwjtofWSvMD8AhUPjosKHZT2D = i ertal 202 o-. Rek BOR TOS:
@ Schemavisare-Sko.. @ CLIPSTUDIO PAINT... (8 YouTube Panzoid [| skola 4 MP3DownloaderO... [i Blueprint Tracker+.. | rust 5 NiceHash-Largest.. @ https//arma3projec... «a MPGH-MultPlayer... [J] iSpace Mining Pool... Miscreated CVAR H... » | IE Ovriga bokmarken
Google [tow to aisable bitdefender antivirus 2023 m ! © Q &
This video will show you how to temporary disable ww enable
How to Temporarily Disable or Enable Bitdefender TOTAL.
YouTube - Nam Anh Cap - 25 jan. 2022
Saknas: 2623 | Maste innehalla: 2023
https:/www. youtube.com
how to bebe disable bitdefender 2023 - YouTube
qb» GalBitdefender 2023 | 8}. Je) o< Bitdefender qb» ita)
how to temporarily disable bitdefender 2023 ... aia win cu
How to disable bitdefender antivirus 2023
YouTube - MR BNA - For 1 manad sedan
https://clean-my-pc.com
Oversatt den har sidan
How to Disable Bitdefender Windows 10 - Clean my PC
Open the Bitdefender Total Security 2019 on your device. - Navigate to the Protection
Features tab and click on the Settings icon under the Antivirus module
https:/Avww. prajwal.org > ho
Oversatt den har sidan
How to Disable Bitdefender Notifications - Prajwal.org
7 2022 — Launch the Bitdefender antivirus or Total security tool. - Select Settings and
click General tab. - Turn off the Special Offers and Recommended
https://www.safetydetectives.com Oversatt den har sidan
How to Cancel Bitdefender Subscription (& Get a Refund) in ...
Find Bitdefender under your list of products and click Stop automatic subscription renewal. ... |
recommend Norton — it's my favorite antivirus in 2023,
kK KK Rankning: 9/10
nsioner
Relaterade sokningar
Q uninstall bitdefender Q bitdefender alert page
Pe e@Oos @
22:36
2023-01-11
```

## Slide 112

135 flare.io

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Windows Security
ee
fm Home
| sy} Virus & threat protection
QR Account protection
(Firewall & network protection
App & browser control
Device security
Device performance & health
>» @ OD
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
.
)
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
&)D of
n» QO9OSseCs*
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
O43 PM
AED A NG pr rrop4
B
```

## Slide 113

136 flare.io

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

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
© of
Submit a sample manually
Tamper Protection
Prevents others from tampering with important security features.
A Tamper protection is off. Your device may be vulnerable, Dismiss
@ of
Ber Settings
= 04:13 PM
AED A NG pr rrop4
§
P& Type here to search n © 9 =
```

## Slide 114

###### **The** **Anatomy of a Stealer Lo g**

ai.midj0urney or virus

flare.io

137

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

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
O :
https:/Awww.vox.com > technology > al-image-dalle-o.
How unbelievably realistic fake images could take over the ...
30 Mar 2023 — Al image generators like DALL-E and Midjourney are getting better and better
at fooling us.
ma PDataDivel
@ Reddit - Dive into a... G Discord (EJ Amazon.de: Low Pri... (@ ChatGPT [| Websites Tools [| One Piece
2. ai.midjOurmey.or virus | a 6 © Qa
virus fake
Is Midjourney v
What is the most realistic Al art generator? v
v
Feedback
BB Shopping
BB Games [ Godot
a
BB Movies &Shows [Football
ai.midjOurney or virus
x @ # O
IB Cooking
3
o
```

## Slide 115

###### **The** **Anatomy of a Stealer Lo g**

ai.midj0urney or virus

flare.io

138

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ Tips for Waiters. x Hi French Terms Related toF & BSi X Perfect software for all your visu: X (GS) ai.midjOurney.or fake? - Google © X +
eS
Cc @ google.com/search?q=ai.midjOurney.or+fake%3F&oq=ai.midjOurney.or+fake%3F&aqs=chrome..69i57.10221j0j7&sourceid=chrome&ie=UTF-8
@ YouTube M Gmail @ Reddit -Diveintoa.. Gp Discord [EJ Amazone: Low Pri... (@ ChatGPT Websites | Tools [M OnePiece | Shopping [| Games [ Godot
Google [_ai.migjQumey.or virus] x |-& @w a
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
@ *
https:/Awww.vox.com > technology > al-image-dalle-o.
How unbelievably realistic fake images could take over the ...
30 Mar 2023 — Al image generators like DALL-E and Midjourney are getting better and better
at fooling us.
ma PDataDivel
a
BB Movies &Shows [Football
w
# Oo
BB Cooking
3
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
eg
Battle.net
World of
Warcraft
EPIC
i
Epic Games
Launcher
Fall Guys
Ip
dy
i
League of
Legends
_ 11:18
@ 7° Gielcouvet ~ G&D) FA on, FA
as
«3 = 2 Taper ici pour rechercher @ r*%, Bi
a
```

## Slide 119

142 flare.io

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
eg
Battle.net
Pil =
o/ oY
World of
Warcraft
- x
EPIC j =
Ya 8
E }
Pole
Add ExtractTo Test w Delete Find = Wiza Info. | VinieSran Comment
‘Sf Java_Clientzip - ZIP archive, unpacked size 168 195 366 byt
Name Size Packed Type
Manxa c @avinose
jre Manka c daiinose
Java Setup.exe 10202752 9641210 Mpwnoxenne
Total 1 folder and 10 202 752 bytes in 1 file
im = £ Topcene
13:19
a 11:18
5°C Cloudy ADA ax NG .,, O @ 7c Cielcouwet ~ G & 14) FRA
12/02/2023 Bi
```

## Slide 120

143 flare.io

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
HB Who spends money like th MB Jactroll fait gooter des fro X BON CREEUN SANDWICH | x @ Download Java for Window {M|64-bit Java for Windows y
> www javacom/f 2£OOr>rO BSA eE
tid cm Netfinx (® Prime Video
Battle.net es é
=Java _—‘ Télécharger Developer Resources Aide 2. Recherche
Wi y
World of ° Ressources d'aide
Warcraft
® Qu que Java? de Java 8?
FPIC Enlever les ancienne
a Désactiver Java
En Messages d'erreur
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
Mana c gavinose
fa Setup.exe 20. 9641210 Mpnnoxerne
Télécharger Java
En téléchargeant Java, vous reconnaissez avoir lu et accepté les conditions du
Contrat de licence Oracle Technology Network License pour Oracle Java SE
@ Ala finde rinstallation de Java, si vous utilisez Web Start, vous devrez peut-étre redémarrer le navigateur (fermer
toutes les fenétres du navigateur et les rouvrir).
ie 8 os Aa hits pour Wind
xc e 1334
Ensolilé Qrecheche A S e-~ & A 9 B® seo2s2023
Total 1 folder and 10 202 752 bytes in 1 file
eligsctiela.. ddligseilels.. dell
°C Cloudy ADR axes 9 @ rc cel tA GO oy) era 1 oe
Ste Chey et Mis 1222023 r. te couve’ ad 12/02/2023 “YA
```

## Slide 121

144 flare.io

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
. Who spends money like th X MBB Jactroll fait godter des fron X MBBON CREE UN SANDWICH? X @ Download Java for Windov {I 64-bit Java for Windows
\ ies
AY \ \ @ 8 qeeee die 2OO>ro Be a
Bm Java Client x) +
® Novo ~ ae oO ® e@ wW TN Ordenar~ = = Ver ~ a -
2 Recherche
€ > Y | M> Transferéncias > Java_Client » CG
A Base Nome
Y @ Barbara - Peso: | (Hole de Java 8?
je Java 8?
Java Set
Bt Documentos BH ova seu
YB Imagens Be
Bm Capturas de!
i le Java
BBB ambiente de # compter du 16 avril 2019.
ab Transferencia # est sensiblement différent
Mbcarrarc utilisations a titre gratuit,
H'autres utilisations peuvent
Ges fe ces Oracle Java. Veuillez lire
Bm Trabalhos Ba # it. Une FAQ est disponible ici.
@Misica #
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
Qroue Mm @ Of A & FP W sys; @ ‘es dunavigateur et les rouvrir).
» FAQ relative a lava Ad hits nour Windows
oc 1334
Ensoleilé A 9 B® seo2s2023
Qrecrecre MO A C e+ a
Total 1 folder and 10 202 752 bytes in 1 file
elipschilele. Gelipscrilele. cellpscrilele.
: _ 11:18
@ 1C Cielcouvet ~ & & 4) FRA 12/02/2023 be
```

## Slide 122

145 flare.io

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ON CREE UN SANDWIC
Fy \ ‘ : javacom/r
Java Client
Y Ordenar
Ya Barb:
Bi Java Setup
Bm Documentos
YB Imagens
Bm Capturas de |
BE Ambiente de #
L Transferencia #
B Documentos #
B imagen
Bm Trabalhos Ba #
@ Masica *
B videos *
Application To
Home Shave View Manage
SIDSY > Downloads > Java.Clent
n Heung Min = Deterioein
YH Quick access
Bim The Sims desktop
$ Downloads
Dave Seupee
Documents
= Pictures
New flder
[i uscarmesiosy
= INSTALLATION
Disco Local (C:
Zitens | 1 item selecionado 9,72
cy
EnoBrowner 10-1
Q Procurar t
INSTALLATION
ipets
ROO
R20I¢aDSpacelogs
ro020
pont
tmp
today
Widget. CER
® Networ
== Selected 10 202 752 bytes in 1 file Total 1 folder and 10 202 752 bytes in 1 file
Hovaite files Mllasessentt
Givomie —Nipistisisneney.. eles =
aligns leis. aelligscrilels. sell sisilele.
SiO Topcene
SC Cloudy
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
a vel couvert Ft NY) TA
12.2.2023 r. 12/02/2023
```

## Slide 123

146 flare.io

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
\ HB Who spends money like th X  MBJactoll fait godter des fro X BON CREE UN SANDWIC @ Download Java for Windor {BML 64-bit ava for Windows 7
Fy > wwnejavacom/tr 2£OOr>rO BSA eE
Bm Java Client x +
® Novo ~ oe oO @ Ww N Ordenar» = = Ver ~ a
2 Recherche
€ > > | M> Transferéncias > Java Client » CG
A Base me Data de
Y @ Barbara - Pesso: | | Hole de Java 8?
je Java 8?
Java Setu 1/02re
Bm Documentos 8 p
Ym imagens Be Bie x +
Bm Capturas de | © new» 1 Sortieen anzeigen (B Aleextrahieren +++
€ > ¥ 1 [tw tots oocaper(G) > Usse > Rope! > Downloads > fomlClet > fe > . 0 le Java
BBB ambiente de # (Som Name we ey pe eS ee ee la compter du 16 avril 2019.
a Transferencia # @ Raphael—Perssnlic Mi bin Dateiordner 08 est sensiblement différent
Biv Dateiordner utilisations a titre gratuit,
BE Documentos #
Im Desktop ~  BcopyricHt Datei H'autres utilisations peuvent
=
ee 4 Downloads LICENSE Datei ces Oracle Java. Veuillez lire
Bm Trabalhos Ba # os BB rcapme os it. Une FAQ est disponible ici.
@ musica #
Eviacos  #
Bm Son Heung Min
Bm The Sims 4
acc
BB Clothes
v MB Este PC
© Disco Local (C:
( gy
2itens | 1 item selecionado 9,72 MB | a
Bi dokumente  #
re ats
oe vg Bi Tanopamucensereanwe Textdokument
— vp BU THROPARTLICENSEREADMEIA,.Tetdokument
@ Welcome Microsoft Edge HTML Do
ie Bildschirnfotos ss
ME DieserPc
= USBDISK (0)
Ge Netowerk
9 Elemente |
—
Fortite
Raphael -
Chrome
Filmore 12
Selected 10 202 752 bytes in 1 file
Mlicisessentt
Salligseilele. Geligbisilele.. Hell gseilele.
P Topcene
eepop2en2e08 OBB B LY im U
oc Cloudy SGaaa503 oe a wlelcouvert OB NY T™  yg3 A
```

## Slide 124

flare.io

147

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Download Help
Help Resources
Offline Installation
Trouble downloading?Try the
Download Java for Windows
17]
Whe
brov
>
Java"
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
Windows 64-bit Users id . u
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Download Java for Windows
4
=Java Download Developer Resources Help
Help Resources Download Java for Windows
Wits? Version 8 Update 361 (filesize: 62.11 MB) Why is Java 8 recommended?
Ct javacom,
[Bh Geercices et évatuati... [JJ Webformation ECF... G3 Am
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
‘Télécharger.
En téléchargeant Java, vous reconnaissez avoir lu et accepté les conditions du
Contrat de licence Technology Network License pour O
@_ Als finde l'installation de Java, si vous utilisez Web Start, vous devrez peut-étre redémarrer le navigateur (fermer
forge-1.193-44.1.1..jar JavaSetupsu361 (1).2x0 JavaSetup8u361.exe review OptiFine 1..jar OptiFine 1.192 HD..jar
Be i mm '7ASetupau361 (ewe g_JavaSetup By PvewOptiFine 1. jar gy OptiFine 1.192. HO
Bh 222 ciertzip BB optrine 1192 HOW jar : ores
9 = = G e@e@6
```

## Slide 127

150
flare.io

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
‘go.java-gapp.space,
S Java Download Help
```

## Slide 128

flare.io

151

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
© burp suite pr X @ Burp Suite z I 4 Professional, X @ burp suite pr xX | 9 VIP4StatsUss x i'M TempM - ter X (S} java- Google X +
oo CG &@ google.com/s ? a&ibiw=18 APX dUPu KEw Vil n2B3( & Q > om ® CI (A) Paused )
iM} TempM - temp mail... & Online Phone N ~ Your account has b... © Request money fro... @ Receive FreeSMSO.. @ SMSPanel t TempMail P Persona — NEW MIC 7 MAICRO Sm dlac
(oo
®
fe)
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
hitpsiwwwjavacom Gosling
Java |_Oracle
Get Java for desktop applications. Download Java - What is Java? Uninstall help. Happy Java
People also search for
NL
»en Group St
Manual download Minecraft. Unix WinRAR Minecraft
Java manual dowmload page. Get the latest version of the Java Bedrock servers
User. Are you a software developer looking for JDK downloads?
Download Java for Windows
Download or update your existing Java Runtime Environment
Install Java on Windows More about Java >
This article applies to: Platform(s): Windows 10, Windows 3
https://www,java.com How do | install Java .
p . 5 OS ir tke ak: 4
```

## Slide 129

152 flare.io

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
© burp suite pr X
S Cc
iM} TempM - temp mail...
Google
https://www.java.com
4 Professiona @ burp suite p
@ Burp Suitez. X
@ google.com/s ’q=java
Online Phone Num... Your account has b... © Request money fro... @ Receive
x
(oo
@ News : More Tools
This search may be relevant to recent activity:
java jdk download
Ad - hitps://go java-gapp.space/ ~
App - Java Download
Java - a programming language for creating powerful applications and websites. Java - a
platform that allows you to expand the functionality of your system.
Ad - https://oracle.58226.click) ~
Java - Specifically applications
Programming language and computing platform. Get for desktop applications
hittps:/Awwwjava.com
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
¢>7¢ 9 ek
q= | O10 &aqs=chr...
@ google.com/search?q= {| ONO&
™M Gmail @@ YouTube BF X/£
Google {ono
AS
MAPAO! HLO] MOS DE 7/5
am Ast HS x
java 2.0H 4
java FEM
Java -cp
Ate} Chee
javaet
java ... parameter
java -jar 2&
Kru 2S
o
#il + https://go.java-gapp.space/
Switch to Java - Java Download
Java is a reliable and powerful programming language that provides convenient programming.
Java is a platform for creating analytical and consumer with extensive capabilities.
Ba - http:/www.ikosmo.co.kr/ +
StSZADES| Oj Ol A7HES - java - ikosmo.co.kr
= 4|2]21100%, ITFaMS, PAA SA7, AS TRAS AS, 44 UHS
A|S, 100% SH Se, 7IBZSE YS
McCoo
ae el
AM TF
SL SSiT94
\
1A SOA! java.
AOA! HHS! SBE ALIS ASUCH St 194] Oto] ASAE SLASS Soy
rl o¢
APSAL Sells BARR
https://www.java.com > we
Java Cl2ec
i)
os
```

## Slide 130

flare.io

153

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
© burp suite p
S C
'M| TempM - temp mail...
Google
https://www.java.com
x @ Burp Suite z
@ google.com/s
& Online Phone Num... Your account has b... © Request money fro... @ Receive
QO All GD) Videos [EJ Images (i) News : More
About 1,930,000,000 r
(0.42 seconds)
This search may be relevant to recent activity:
java jdk download
Ad - https://go.java-gapp.space/ ~
App - Java Download
Java - a programming language for creating powerful applications and websites. Java - a
platform that allows you to expand the functionality of your system.
Ad - https://oracle.58226.click) ~
Java - Specifically applications
Programming language and computing platform. Get for desktop applications
hittps:/Awwwjava.com
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
¢>7¢
™M Gmail @@ YouTube BF X/£
{ono D8
Google
AS
AHAFA1O] PHBFOY Ost Of
+s
o
A javaét
1 java ... parameter
java -jar 4! 6
Trap aS
Java -cp
Ate} Che ec
Bil - https://go.java-gapp.space/ +
Switch to Java - Java Download
Java is a reliable and powerful programming language that provides convenient programming.
Java is a platform for creating analytical and consumer with extensive capabilities.
3a - http:/www.ikosmo.co.kr/ +
StS=ADES| Oj Ol A7HES - java - ikosmo.co.kr
2AIKE ASAE KI XO} TRY Sa 2 4AtArayo Sac
=S4/%|21100%, TFRs, + I, ABel rus,
e ENS, 1:14) 40H
al AI CLYOA a
SLSSTSSEA7|S, 100% SH FE, 7|RF
java.
tin
iin}
ac]
nn
Me
+>
30
>
ie
AYA! HOHSE SAE ALA S|ASUCH Bt 19M] Olsto] AAKAE ALMSS SH SE
0
b&
te
QAl sells
https:/www.java.com >... ¥
Java Cl2ec
@ google.com/search?q= { OM O&oq={OUOBaqs=chr.. 9 @ ke OF &
```

## Slide 131

flare.io

154

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
© burp suite pr X @ Burp Suite ra $ G 1020 - Google df x +
< (SS  google.com/sea q=java& = 1821 &bih=833 &ei=BwrpY4PXG6KikdU Pue2e6Ac&ivecqi a mtr @ google.com/search?q= { OMO&0q={ONO&aqs=chr... 9 @*ke OF 2
iM] TempM - temp mail... & Online Phone Num... Your account has b... ic enn SMe | Gmail €§) YouTube gf AZ
Google {ono x m@toaa
AS
ABP OL JEStOy BIO SE OE 71S
. *» https://go.java-gapp.space/
ot
This search may be relevant to recent activity:
java jdk download
java + ti java ... parameter
Ad - https:/igo java-gapp.space/ ~ Java -cp java -jar ae
App - Java Download Xo CHSC Ape} BS
Java - a programming language for creating powerful applications and websites. Java - a
platform that allows you to expand the functionality of your system. j
Bil - https://go.java-gapp.space/ +
Ad - hitps:/oracle.58226.click! ~ Ss itch J J D | d
Java - Specifically applications witch to Java - Java Downloa
Programming language and computing platform. Get for desktop applications Java is a reliable and powerful programming language that provides convenient programming.
Java is a platform for creating analytical and consumer with extensive capabilities.
hittps:/Awwwjava.com
Java |_Oracle
Get Java for desktop applications. Download Java - What is Java? Uninstall help. Happy Java
3a - http:/www.ikosmo.co.kr/ +
User. Are you a software developer looking for JDK downloads? SIS ADE OF ol XH 7H St] - java - ikosmo.co.kr
S44] 21100%, ITFUS, PAA AA7t, AS TRASAS, AAs AcMAsg. a
Download Java for Windows
Download or update your existing Java Runtime Environment SLSSTSSEA7|F, 100% SH FE, BSE WS 117 AOHA, java.
Manual download
Java manual dovmload page. Get the latest version of the Java SAWOHA HOS SAE A QS] ASUCH St 19M] O/4to] ASAE AMISS SH SE Sas St USy
ct
Install Java on Windows ALOLOLS JA] 101 015
This article applies to: Platform(s): Windows 10, Windows 8 APSAL HMMS Al ANAS
How do | install Java
https:/www.java.com >... ¥
Java Cl2ec
```

## Slide 132

flare.io

155

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
© burp suite p
S C
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
Ad - https://oracle.58226.click) ~
Java - Specifically applications
Programming language and computing platform. Get for desktop applications
hittps:/Awwwjava.com
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
G 1°70 - Google 44 x + . ~ =
€<€ 7 C @ google.com/search?q= { OM O&o0q= | OM OBaqs=chr.. 9 Be Of
™M Gmail @@ YouTube BF X/£
Google {ono x mgs ®
AS
AHAFAYO! 7HSIO] BO St OE 71 =
=} s Pt
“t https://go.java-gapp.space/
java + ti java ... parameter
Java -cp java -jar 2
Ato} CHP ec teas
Bil - https://go.java-gapp.space/ + ais
Switch to Java - Java Download
Java is a reliable and powerful programming language that provides convenient programming.
Java is a platform for creating analytical and consumer with extensive capabilities.
3a - http:/www.ikosmo.co.kr/ +
StS=ADES| Oj Ol A7HES - java - ikosmo.co.kr
S47] 21100%, ITFRMS, PAA HA, ASP TRASUS, 4AHAas aclayad. a
SLSATSFEAIS, 100% SH FH, BSH YS 117A AOA, java.
AOA] PHS SAE ALS ASUCH Ct 194] Otol ASAE ALAUISS SH SE Aas B+ WS
mo
APSAL Seles PEAR
¥
https:/Awww.java.com > ...
Java Cl2ec
```

## Slide 133

flare.io

156

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

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
Windows 64-bit Users . oH oe ‘ : y
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
go.java-gapp.space
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

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
a a
venue tlesize: 62.11
Do you use both 32-bit and 64-bit 7 a
browsers?
FAQ about 64-bit Java for Windows product. An FAQ is available here.
Offline Installation Commercial license and support is available with a low cost Java SE Subscription.
Trouble downloading?Try the
offline installer
Download Java
By downloading Java you acknowledge that you have read and accepted the
terms of the Oracle Technology Network License Agreement for Oracle Java SE
e
Help
Help Resources Download Or for Windows
' Version 8 Update sf (ilesize: 4011B) esi
M a Fi cious ; a portant Oracle ieee
a filesize: 40.11
Trouble downloading? Try the
— product. An FAQ is available h
Commercial license and support is available with a low cost Java SE Subscription.
Download Java
By downloading Java you acknowl t you have read and accepted the
terms of the Network it for
```

## Slide 137

flare.io

160

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
[i] TempM -ter’ x © java-Google x +
FL 74% bY o ( A> Paused }
— MAICRO
@ Burp Suite z 4 Professional, X @ burp suite pr xX | 9 VIP4StatsUss x
© burp suite pr X
S Cc
[2] TempM - temp mail...
@ google.com/s ? a&biw=18 APX dUPu KEw vil - ( &
& Online Phone N Your account has b... © Request money fro... @ Receive FreeSMSO.. @ SMSPanel t TempMail P Persona — NEW MIC em alo
Go gle java x &£§ BDA 83
QA D) Videos @) News : More Tools
https://www.java.com
Oo
This search may be relevant to recent activity:
java jdk download
Ad - hitps://go. gg hh space! ta
ating powerful applications and websites. Java - a
inctionality of your system.
Ad - https://oracle.58226.click/ ~
Java - Specifically applications
Programming language and computing platform. Get for desktop applications.
hittps:/Awwwjava.com
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
Gosiling
People also search for
NL
»en Group St
WinRAR Minecraft
servers
Minecraft Unix
Bedrock
More about Java >
OB“ irr We pik ~
```

## Slide 138

flare.io

161

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
go.java-gapp.space.
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
B® Java Client x ar
@Onwr %§ O ( WB 2 W
/\ | Java_Client
€<€ > v 4 MB > Transferéncias { Java_Client V
A Base Nome
Vv @ Barbara - Pessoz .
> [i Documentos 8 Java Se WS
vy Bl Imagens ae
> [i Capturas de!
BH Ambiente de #
wb Transferéncia #
162
```

## Slide 140

flare.io

163

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@& Java Client x a 6
® Novo ~ a (8) @ e W NL Ordenar ~
Ver ~ aoe
€ > vy WF  M> Transferéncias > Java_Client
A Base Nome j
Y @ Barbara - Pesso: | DoHOle /
@ Java Setup “f
Bm Documentos
Ba jre
YB Imagens
Bm Capturas de |
Bl Ambiente de #
wb Transferéncia #
EB Documentos #
Biimagens  #
Bi Trabalhos Ba #
@ Masica *
EE videos *
B® Son Heung Min
Bm The Sims 4
Macc
Bm Clothes
v_ MB Este PC
© Disco Local (C:
2itens | 1 item selecionado 9,72 MB |
Bea
22:55
% ® wo22023 @
+)
>
6
»
Q Procure fy 9
163
```

## Slide 141

164 flare.io

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ (08) @ i try installing java but it ¢ bea) “fF
< (G: 9 & wwwgoogle.com/search
Google i try installing java but it doesn't work xX OQ
Q All () Videos (Images [9] Books News : More Tools
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
ca >vt Bi > Downloads > Java _Clientzip
A Home Name
BB jre
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Strength and Limits
Linz Download Developer Resources Help
Existence
177
```

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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

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
of mem anal ysi:
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
