---
title: "Hello 1994 Abusing Windows Explorer via Component Object Model in 2023"
speakers: ["Michael Harbison"]
conference: "REcon"
conference_full: "REcon 2023"
edition: ""
year: 2023
source_pdf: "REcon 2023 Slides/Michael Harbison_Hello 1994 Abusing Windows Explorer via Component Object Model in 2023.pdf"
pages: 34
sha256: "17f24d5ddff5895cb42282b105538436108d76679e411edd41c5377dfad83bc4"
text_chars: 14222
ocr_pages: 8
has_ocr: true
redacted_secrets: 0
ocr_confidence: 82.9
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T06:02:32Z"
---
# Hello 1994 Abusing Windows Explorer via Component Object Model in 2023

**Speakers:** Michael Harbison  
**Conference:** REcon 2023  
**Source:** `REcon 2023 Slides/Michael Harbison_Hello 1994 Abusing Windows Explorer via Component Object Model in 2023.pdf` (34 pages)


## Slide 1

**Hello 1994: Abusing Windows Explorer via Component Object Model in 2023**

**Mike Harbison Unit 42, Distinguished Engineer**

**REcon June 2023**

© 2023 Palo Alto Networks, Inc. All rights reserved. Proprietary and confidential information.

© 2023 Palo Alto Networks, Inc. All rights reserved. Proprietary and confidential information.

## Slide 2

## **Whoami /all**

### USER INFORMATION

**Name Occupation**

===============     ===============

**Mike Harbison           6+ years with Palo Alto Networks Unit 42 Threat Intel Team**

USER BACKGROUND

- Computer Forensic Examiner w. DC3/Mandiant

- ● Vulnerability Researcher

- ● Reverse Engineer since SoftICE

© 2023 Palo Alto Networks, Inc. All rights reserved. Proprietary and confidential information.

## Slide 3

## **Agenda**

- PlugX Malware Discovery

- Overview of COM

- USB Infection Technique

- Microsoft's Response

- Q & A

© 2023 Palo Alto Networks, Inc. All rights reserved. Proprietary and confidential information.

## Slide 4

## **What is PlugX?**

- Fully-featured remote access tool (RAT) that targets Windows OS

- First seen in 2008

- Chinese nexus but used by various nation state threat actors

- Historically abuses trusted software to DLL side load an **encrypted** payload in-memory

- Considered one of the oldest, evolving malware families

© 2023 Palo Alto Networks, Inc. All rights reserved. Proprietary and confidential information.

## Slide 5

## **PlugX Infection Method - DLL Sideloading**

© 2023 Palo Alto Networks, Inc. All rights reserved. Proprietary and confidential information.

## Slide 6

## **Journey into the IUnknown: Discovery Timeline**

- **January 2023** - Discovered interesting PlugX malware sample while investigating a Black Basta ransomware case: **x32bridge.dat**

- ● **January 22, 2021** - **x32bridge.dat** first uploaded to VirusTotal from Thailand *****

   - 4 / 60 AV engines identified the sample as malware at that time

- **July 4, 2019** - PE Compilation date and time

- **No prior mention or detection of USB capabilities**

© 2023 Palo Alto Networks, Inc. All rights reserved. Proprietary and confidential information.

## Slide 7

## **USB Infection and Concealment Key Components**

1. Targets <u>all type 2 DRIVE_REMOVABLE devices attached to a</u> host

2. Implementation of Shortcut COM object 3. Implementation of Recycle Bin COM object

4. Use of a Unicode character ( **N** on- **B** reaking **SP** ace) as a directory name

The <u>combination o</u> f the Recycle Bin + the NBSP prevents the Windows OS from accessing the directory

© 2023 Palo Alto Networks, Inc. All rights reserved. Proprietary and confidential information.

## Slide 8

## **What is COM?**

#### **Microsoft Definition** -

"COM is a platform-independent, distributed, object-oriented system for creating binary software components that can interact. COM is the foundation technology for Microsoft's OLE (compound documents) and ActiveX (Internet-enabled components) technologies."

Component Object Model (COM) is a binary interface standard for software components introduced by Microsoft in late **1993 early 1994** !

Programming COM involves the use of COM-aware components. Components are identified by a unique ID 128-bit CLSID, which are globally unique identifiers. The components expose their functionality through one or more interfaces.

© 2023 Palo Alto Networks, Inc. All rights reserved. Proprietary and confidential information.

## Slide 9

## **USB Infection Stages**

Create directory structure and Windows shortcut. Move **all user files** from root of USB device to 2nd NBSP directory

**1**

- \Root of USB device

- NBSP Directory  #1

- Windows Shortcut

Windows Shortcut links to X32dbg.exe

- \..\NBSP Directory #1

**2**

Applies drive icon to NBSP directory

- NBSP Directory #2

- Windows Shortcut

- Desktop.ini

**3**

- \..\..\NBSP Directory #2

Contains the 128-bit CLSID for Recycle bin COM object. Windows Explorer now sees the hidden recycler.bin folder as a link to the hosts master recycle bin!

- **All user files** from the root of the USB device

- Recycle **<u>r</u>** <u>.bin Directory</u>

- Desktop.ini

**4**

- \..\..\..\Recycle **<u>r</u>** <u>.bin Directory</u> ● Subdirectory + files

- Desktop.ini

© 2023 Palo Alto Networks, Inc. All rights reserved. Proprietary and confidential information.

## Slide 10

## **COM Class Factories**

- Used to create the Windows shortcut file(s)

   - 128-bit CLSID (RIID) of **00021401-0000-0000-C000-000000000046**

   - ○ “Shortcut”

- Used to turn a folder to link to the master Recycle bin

   - 128-bit CLSID (RIID) of **645FF040-5081-101B-9F08-00AA002F954E**

   - “Recycle Bin”

© 2023 Palo Alto Networks, Inc. All rights reserved. Proprietary and confidential information.

## Slide 11

## **COM Class Factories - Shortcut**

- 128-bit CLSID (RIID) of **00021401-0000-0000-C000-000 000000046**

- CLSID_ShellLink (Shortcut) class implements the following interfaces in windows.storage.dll version 10.0 taken from Windows 10 version 21H2

© 2023 Palo Alto Networks, Inc. All rights reserved. Proprietary and confidential information.

## Slide 12

## **COM Class Factories - Recycle Bin**

- 128-bit CLSID (RIID) of **645FF040-5081-101B-9F08-00AA 002F954E**

- CLSID_Recyle Bin class implements the following interfaces in shell32.dll version 10.0 taken from Windows 10 version 21H2

© 2023 Palo Alto Networks, Inc. All rights reserved. Proprietary and confidential information.

## Slide 13

## **Shortcut File Creation**

- The shortcut COM object uses the Windows.Storage namespace

● This class allows for the managing of files, folders, and application settings

- Once the COM shortcut instance is instantiated:

○ Calls the ::SetPath method to set the initial shell link file path ○ Calls the ::SetArguments to set the command arguments ○ Sets the show state of the command shell link object to SW_SHOWMINNOACTIVE

- Sets the ICON file for the new object to shell32.dll number 7

- Finally calling IPersistFile::Save to save the **object** to disk

© 2023 Palo Alto Networks, Inc. All rights reserved. Proprietary and confidential information.

## Slide 14

## **Shortcut File On USB Device**

© 2023 Palo Alto Networks, Inc. All rights reserved. Proprietary and confidential information.


> Recovered by OCR — confidence 88/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Shortcut File On USB Device
a» RECON2023 Properties x
Can you spot the NBSP???
spec% /q /c (\\RECYCLER BIN\files\x32dbg.exe"
Target location:
Target: spec% /q /c"\\RECYCLER.BIN\files\x32dbg.exe"
```

## Slide 15

## **Significance of the NBSP Directory (0x00A0)**

- Windows Explorer and the command console (cmd.exe) are unable to traverse into the NBSP directory located in the recycler.bin directory

- The whitespace character is preventing the OS from rendering the directory name, making the folder invisible (rather than leaving a nameless folder in Windows Explorer).

- If an NBSP directory wasn’t used in the recycler.bin directory, a user would be able to traverse the path and delete the corresponding file(s).

© 2023 Palo Alto Networks, Inc. All rights reserved. Proprietary and confidential information.

## Slide 16

# **Walk-Through Demo**

© 2023 Palo Alto Networks, Inc. All rights reserved. Proprietary and confidential information.

## Slide 17

## **Pre and Post USB Infection**

© 2023 Palo Alto Networks, Inc. All rights reserved. Proprietary and confidential information.


> Recovered by OCR — confidence 84/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Pre and Post USB Infection
Home Share View Drive Tools
© Pictures # * [] Name ° Date modified Type Size
Montreslibeer Breweries Montreal Beer Breweries 5/1/2023 6:30 PM File folder
| temp Research Documents 5/1/2023 6:30 PM File folder
testfile (=a APT43_Research.pdf 4/20/2023 12:09 PM Microsoft Edge PDF ... 9,087 KB
tools |) calc64se.bin 4/25/2019 11:49 AM BIN File 1KB
_ | My Will-txt 2/5/2019 5:53 AM Text Document 8 KB
This PC __] secretdocs.locked 2/5/2019 5:51 AM LOCKED File 57 KB
8 3D Objects t= What to do in Montreal.pdf 4/24/2023 6:20 PM Microsoft Edge PDF ... 58 KB
Gl Desktop @i Wine Lists.pdf 4/20/2023 2:35 PM Microsoft Edge PDF ... 1,916 KB
“= Documents
& Downloads
d Music
© Pictures
a Non Infected USB Device
== CD Drive (E:) CD-ROM
=» RECON2023 (F:)
== CD Drive (E:) CD-ROM
~~ RECON2023 (F:)
II rights reserved. Proprietary and confidential in' % paloalto
```

## Slide 18

## **Post USB Infection**

© 2023 Palo Alto Networks, Inc. All rights reserved. Proprietary and confidential information.


> Recovered by OCR — confidence 77/100 on the text kept, 68/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Post USB Infection
Hl Desktop # * [] Name Date modified Type Size
Montreal Beer Breweries
temp
testfile
tools
o tense Infected USB Device
> 13D Objects
> Gl Desktop
> © Documents
> & Downloads
> J} Music
> © Pictures
> a Videos
> &. Local Disk (C:)
> = CD Drive (E:) CD-ROM
II rights reserved. Proprietary and confidential in' & paloal
```

## Slide 19

## **Post USB Infection Shortcut**

© 2023 Palo Alto Networks, Inc. All rights reserved. Proprietary and confidential information.


> Recovered by OCR — confidence 91/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Post USB Infection Shortcut
RECON2023 (F:)
“ [1 Name ° Date modified Type Size
Mise RECON2023 5/28/2023 7:57 AM Shortcut 2 KB
a» RECON2023 Properties x
Colors Terminal File Hashes Details
General Shortcut Options Font Layout
RECON2023
Target type: File
Target location:
Target: Spec% /q /c "F:\ \RECYCLER.BIN\files\x32dbg.ex
Proprietary and confidential i
```

## Slide 20

## **Post USB Infection - Hiding in Plain Sight**

### **Can you spot the NBSP?**

© 2023 Palo Alto Networks, Inc. All rights reserved. Proprietary and confidential information.

## Slide 21

## **USB Recycler Bin Folder**

- Not showing directories / files that were created

- Links to host master recycle bin on the root directory and not the USB device

- NBSP visibility makes it hard to detect as it looks like the F drive

© 2023 Palo Alto Networks, Inc. All rights reserved. Proprietary and confidential information.

## Slide 22

## **Windows File Explorer - Not Found**

© 2023 Palo Alto Networks, Inc. All rights reserved. Proprietary and confidential information.


> Recovered by OCR — confidence 81/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Windows File Explorer - Not Found
ay = | Maneee F:\ \ \RECYCLER.BIN
Home Share View Recycle Bin Tools
temp “ (1 Name Date modified Typ
nels \) desktop ini 5/2/2023 11:45 AM Cor
@ This PC File Explorer x
“J 3D Objects
Hl Desktop 6 Windows can't find 'F:\ \ \RECYCLER.BIN\files'. Check the spelling and try again.
* Documents
& Downloads OK
```

## Slide 23

## **USB Device Recycler bin folder**

© 2023 Palo Alto Networks, Inc. All rights reserved. Proprietary and confidential information.


> Recovered by OCR — confidence 82/100 on the text kept, 72/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
USB Device Recycler bin folder
688 WinHex - [Drive F:]
a File Edit Search Position View Tools Specialist Options Window Help
Drive F:
\ \RECYLER.BIN
Name ~ - [ ea. | Size | Created | Modified | Accessed | Attr. | 1st sector |
( TESTDRIVE / / / RECYCLER.BIN / files : Q
x32bridge. x32bridge. x32dbg.exe
dat dil
Default Edit Mode 0100F030 46 30 38 2D 30 30 41 41 30 30 32 46 39 35 34 45 FOS—-OOAA002F954E
rietary and
```

## Slide 24

# **Video Demo**

© 2023 Palo Alto Networks, Inc. All rights reserved. Proprietary and confidential information.

## Slide 25

© 2023 Palo Alto Networks, Inc. All rights reserved. Proprietary and confidential information.


> Recovered by OCR — confidence 77/100 on the text kept, 54/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Montreal Beer 8 secretdocsocked 2/5/2019 5351 AM LOCKED File 5
This PC 2 Music
‘© Pictures
Sitems Bitems
LO Type here to search
2023 Palo Alto Networks, Inc. Alll rights reserved. Proprietary and confidential information. o// paloalt r
```

## Slide 26

# **Vendor Notification**

© 2023 Palo Alto Networks, Inc. All rights reserved. Proprietary and confidential information.

## Slide 27

## **MSRC Submission**

“Hey Microsoft, we are seeing in the wild exploitation of USB devices by the PlugX malware using a novel technique to conceal the payload. Additionally, we are concerned that Windows Defender is not scanning the files.”

- January 4th, 2023

© 2023 Palo Alto Networks, Inc. All rights reserved. Proprietary and confidential information.

## Slide 28

## **MSRC Response**

- “Our developers have looked into possible changes in the OS, but based on designed functionality, there are **no opportunities** to improve on

the design which would help against this particular malware campaign”.

- January 20th, 2023

© 2023 Palo Alto Networks, Inc. All rights reserved. Proprietary and confidential information.

## Slide 29

## **But then…**

- The Windows Defender team added coverage

- While building my slides for this talk, Windows Defender started to hit on the lnk files (shortcut) created by this malware.

- ~ February - March 2023

© 2023 Palo Alto Networks, Inc. All rights reserved. Proprietary and confidential information.

## Slide 30

## **Chitexa VirusTotal Hits**

© 2023 Palo Alto Networks, Inc. All rights reserved. Proprietary and confidential information.


> Recovered by OCR — confidence 84/100 on the text kept, 68/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Chitexa VirusTotal Hits
FILES -6/6
914A6BE2CDBB49836C3A6AB4465BEEQ9 1 83365EE@E9 1 2F52A6E655347 186FA78
6
direct-cpu-clock-access
Detections
11/59
7/60
9/60
10/61
Sort by ~
Size
1.71 KB
1.76 KB
1.73 KB
1.64 KB
1.64 KB
1.64 KB
Filter by ~
First seen
2023-05-04
23:23:22
2023-04-26
10:30:31
2023-03-20
22:40:49
2023-03-18
22:03:58
2023-03-13
02:03:13
2023-02-10
11:50:36
Export ~
Last seen
2023-05-04
23:23:22
2023-04-26
10:30:31
2023-03-20
22:40:49
2023-03-18
22:03:58
2023-03-13
02:03:13
2023-02-10
11:50:36
Tools ~ Help ~
Submitters
q LNK
a LNK
1 ok
1 om
```

## Slide 31

## **Discovery of 2nd USB Variant**

|1.
Same USB infectio
|n technique
|but with additional behaviors
|
|---|---|---|
|a.
Creates a conc|ealed subfol|er named**da5202e5**on the USB|
|device

i|i|i|
|b.
Copies all Micr i
|osoft Office a
|i nd Adobe documents from the host|
|to this director|y||

© 2023 Palo Alto Networks, Inc. All rights reserved. Proprietary and confidential information.

## Slide 32

# **Future Research**

© 2023 Palo Alto Networks, Inc. All rights reserved. Proprietary and confidential information.

## Slide 33

## **Future Research Opportunities**

- Test AV vendors to ensure that they can scan files stored in the NBSP + recycler.bin folder

- Can a Recycle Bin folder exist on non USB devices such as a physical drive

- What other Unicode characters can be abused to conceal folders

- What other Desktop.ini entries can be used to masquerade folders and files

- Little to no research on how the master Recycle Bin folder works. Maybe a chapter in the Windows Internals?

© 2023 Palo Alto Networks, Inc. All rights reserved. Proprietary and confidential information.

## Slide 34

## **Thank you!**

<u>Learning is doing. I’ve re-purposed the techniques outlined in this talk and</u> will make them publicly available. Enjoy, learn, and I welcome any feedback you may have. The POC can be found here:

https://github.com/mjharbison/plugxUSBPOC/tree/master

© 2023 Palo Alto Networks, Inc. All rights reserved. Proprietary and confidential information.
