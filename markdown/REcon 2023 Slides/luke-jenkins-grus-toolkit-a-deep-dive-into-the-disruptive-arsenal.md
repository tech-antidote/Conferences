---
title: "GRU’s toolkit A deep dive into the disruptive arsenal"
speakers: ["Luke Jenkins"]
conference: "REcon"
conference_full: "REcon 2023"
edition: ""
year: 2023
source_pdf: "REcon 2023 Slides/Luke Jenkins_GRU’s toolkit A deep dive into the disruptive arsenal .pdf"
pages: 28
sha256: "d6e474be38ccdaa23e27d715568ac56fe223930c10d60e2ca99884cb55b93512"
text_chars: 11589
ocr_pages: 4
has_ocr: true
redacted_secrets: 0
ocr_confidence: 85.4
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T06:02:03Z"
---
# GRU’s toolkit A deep dive into the disruptive arsenal

**Speakers:** Luke Jenkins  
**Conference:** REcon 2023  
**Source:** `REcon 2023 Slides/Luke Jenkins_GRU’s toolkit A deep dive into the disruptive arsenal .pdf` (28 pages)


## Slide 1

# GRU’s toolkit

A deep dive into the disruptive arsenal

Luke Jenkins

Principal Analyst, Mandiant Intelligence

lukejenx@google.com

©2023 Mandiant

## Slide 2

## Who’s this guy?

- Principal Analyst at Mandiant’s Cyber Espionage team

   - Responsible for tracking nation-stateactors

- Since early 2022 worked on tracking Russian backed cyber activities both within Ukraine and globally

©2023 Mandiant

2

## Slide 3

Attribution is hard; it’s made even harder when multiple teams converge on a single problem.

**©2023 Mandiant** 3


> Recovered by OCR — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Attribution is hard; it’s made even harder when
multiple teams converge ona single problem.
M ©2023 Mandiant
```

## Slide 4

# Disruption tooling

**©2023 Mandiant** 4

## Slide 5

## Disruptive tooling

- Disruptive tooling is the sledgehammer, not the stealthylittle scalpel traditionally used for espionage.

- How Russia uses this sledgehammer:

   - DDOS attacks masquerading as hacktivists

   - Endpoint/Server denial of service

   - Disruption to energy and communications

- The capability is likely developed specifically for a given operation and has a short lifespan.

©2023 Mandiant

5

## Slide 6

## Disruptive tooling

- GRU is currently operating in a high-pressure and high-risk environment

- The GRU limits the risk by:

   - Using a variety of languages

      - C/C++

      - C#/.Net

      - Golang

   - Limiting the lifespan of the tooling

   - Limiting the capability of the tooling

- The actor, however, does recycle components between different operations.

©2023 Mandiant

6

## Slide 7

# Maintaining access

**©2023 Mandiant** 7

## Slide 8

## FREETOW

- FREETOW is a lightweight shellcode loader

   - Used in environments where actor had prolonged access

   - Persisted using a simple schedule task

   - Responsible for loading TOWSTRAP

- A unique feature of FREETOW was an anti-analysis feature that expected an inputted character “z”

   - Note: Deployments of FREETOW occurred months before the invasion, although the symbol had significant value to the RU military at the time of the invasion.

©2023 Mandiant

8

## Slide 9

©2023 Mandiant

9


> Recovered by OCR — confidence 81/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
if ( VirtualALloc )
{
\pBuffer = VirtualAlloc(0i64, pNtHeader->OptionalHeader.SizeOfImage, MEM_COMMIT, PAGE_EXECUTE_READWRITE);
if ( lpBuffer )
{
SizeOfimage = pNtHeader->OptionalHeader.SizeOfImage;
if ( pNtheader->OptionalHeader.SizeOfImage )
{
v19 = \pBuffer - (_QWORD)ImageBaseAddress;// Copy payload
do
<
*((_BYTE *)ImageBaseAddress + v19) = «(_BYTE *)ImageBaseAddress;
ImageBaseAddress = (DWORD *)((char *)ImageBaseAddress + 1);
}
while ( SizeOfImage );
}
}
}
for ( i = (_BYTE «)(\pBuffer + SizeOfUninitializedData + offsetStartPayload);
(unsigned __int64)i <= lpBuffer + offsetStartPayload + SizeOfUninitializedData + dwLenPayload;
++i )
{
}
lpPayload = (void (*)(void))(\pBuffer + offsetStartPayload + optionalHeader->SizeOfUninitializedData) ;
VirtualAlloc(®i64, @x400000i64, MEM_COMMIT, PAGE_EXECUTE_READWRITE);
‘TpPay load); 77 execute payload
*i = -1 - «i; // decode payload
M ©2023 Mandiant
```

## Slide 10

## TOWSTRAP

- TOWSTRAP is a shellcode downloader, invoked by FREETOW

   - The payload is likely a variant of Metasploit’s reverse_tcp module

   - The payload is responsible for downloading the next stage from a given C2 address

- TOWSTRAP uses a custom network protocol, sending no data but receiving:

   - 4 bytes dictating the size of the payload

   - 32 bytes that are then overwritten

   - The remainder of the next stage, encoded by an XOR with 0xC6

- After decoding the payload, the actor reads the buffer in reverse looking for `pop r15` or `call`

©2023 Mandiant 10

## Slide 11

# Disruption

**©2023 Mandiant** 11

## Slide 12

## WHISPERGATE

- First wiper event documented around the invasion of Ukraine (2022)

- Started in January 2022, using a mixture of commercially available droppers to deploy a MBR wiper (PAYWIPE) and a file encryptor/"ransomware" (SHADYLOOK).

- Would be the first of many fake "ransomware" operations

- MSTIC noted deployment was via impacket, a tool we witnessed other GRU threat actors using

- Operation was unique due to the use of commercially available tools and the use of two distinct payloads.

https://purecoder.io/products/Pure-Crypter

©2023 Mandiant

12

## Slide 13

## PAYWIPE

- PAYWIPE is a lightweight MBR wiper

- According to Microsoft, called stage1.exe #opsec

- Deploys disruptive code in the MBR that results in wiping every 199<sup>th</sup> sector on HDD

- Displays the following “ransomware” note

©2023 Mandiant 13

## Slide 14

## SHADYLOOK

- Disruptive file wiper that was loaded in memory by GOOSECHASE

- Again, amazing opsec – called stage2.exe

- Overwrites the first 1MB of given files with 0xCC and renames with random file extension

- Enumerates all mounted hard drives looking for files with a given extension.

- Analysis of the payload also identified another "ransomware" family from April 2021 called WARYLOOK.

©2023 Mandiant

14

## Slide 15

## WARYLOOK

- SHADYLOOK was functionally similar to another malware family WARYLOOK from 2021

- WARYLOOK contains identical functionality to enumerate drives, but:

   - Uses the filename .encrpt3d

   - Encrypts data with AES (although doesn’t store the key)

- WARYLOOK also installs itself persistently on victim devices

- Responsible for showing the "ransom" note as a popup after boot, similar purpose as PAYWIPE

©2023 Mandiant

15

## Slide 16

## Disruptive attacks on the eve of the invasion

- 23<sup>rd</sup> February, the GRU launched a major disruptive attack using payloads like NEARMISS and  PARTYTICKET.

- The disruption attacks were associated with a series of website defacements.

- Defacements were claimed by a group calling themselves FreeCivilian, this alias will return exactly a year later.

©2023 Mandiant

16

## Slide 17

## NEARMISS

- Windows MBR, MFT and file wiper

- Utilises EaseUS for file writes rather than utilising Windows APIs directly, likely to avoid Windows restrictions

- Designed to cause as much damage as possible as quickly as possible

- Contains a configurable shutdown timer

- Overwrites data with random bytes, including Windows Events Logs

- Disables some windows features

   - Volume shadow copies

   - Crash dumps

©2023 Mandiant 17

## Slide 18

## NEARMISS

©2023 Mandiant

18


> Recovered by OCR — confidence 79/100 on the text kept, 73/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
4
NEARMISS
DWORD dwNumberOfThreads; // esi
struct_physical drive *WipeSectorBlock; // edi
HANDLE hThread; // eax
DWORD i; // edi
void *arrayHThreads[100}; // [esptCh] [ebp-190h] SYREF
dwNumberOfThreads = 0;
WipeSectorBlock = this->WipeSectorBlock;
if ( this->WipeSectorBlock )
do
hThread = CreateThread(0, 0, (LPTHREAD_START yeep tlaghs amir pnvenenreate cd) WipeSectorBlock, 0, 0);// Send a block to wipe to the Wiper function
arrayHThreads[{dwNumberOfThreads} = hThread;/7 Add the thread to the list
if ( hThread )
++dwiumberOfThreads;
WipeSectorBlock = (struct_physical drive *)WipeSectorBlock->next;// Get the next block, then add this
}
while ( WipeSectorSlock I= this->WipeSectorBlock );
WaitForMultipleObjects(dwNumberOfThreads, arraylThreads, 1, OxPFFFFPFF);// Wait for all threads to complete
Closeflandle(arraylThreads[i)}); // Close Handles to all the threads
}
return dwNumberOfThreads != 0;
wnsprintfW(pezDest, 260, L"\\\\.\\EPMNTDRV\\%u", PhysicalDriveNumber);// Open a handle to the Easels driver for that particular PhayicalDrive
‘/ For example, PhysicalDrived would be EPMNTDRV\0
df ( UhEaseUs || bases == (void *j-1 )
lpBuffer = (LPCVOID)1lpThreadParameter->1poOutputRandBuffer;
lpStartRegion = regionsToWipe->lpStartRegion;
if ( _SPAIRG64__(lpStartRegion, dwCurrentLocationWithinBlock) < dwEndOfsector }
do
if { lSetPilePointerEz(hEaseUs, (LARGE_INTEGER)_PAIR64_ (lpStartRegion, dwCurrentLocationWithinBlock), 0, 0) )// Mowe the file pointer to the region to wipe
dwCurrentLocationWithinBlock += nNumberOfBytesToWrite;
va = *(_QWORD *)éregionsToWipe->dwCurrentLocationWithinBlock + *(_QWORD *)éregionsToWipe->dwregionsize;
}
while ( _SPAIRG4_ (lpStartRegion, dwCurrentLocationWithinBlock) < vi );
regionsToWipe = (struct_regions *)regionsToWipe->next;
while ( regionsToWipe 1= lpThreadParameter->regionsToWipe );
if { FlushFileBuffers(hEaseUs) )
18
```

## Slide 19

## PARTYTICKET

- GoLang file encryptor/fake ransomware

- Uses a unique SHA256 hash for each file encryption (ish)

- Crowdstrike noted that the key generation was flawed due to the seeding of the Intn function

- Actor accidently deployed this payload shortly before NEARMISS using NEARMISS command line arguments

- Although variant functions and acts like a ransomware payload, the usage alongside NEARMISS most likely indicates that this is yet another disruptive tool.

©2023 Mandiant 19

## Slide 20

## SKYFALL – Communication disruption

- On the 24<sup>th</sup> February, SKYFALL caused internet service disruptions in Ukraine and Europe

- SKYFALL is designed to impact routers and embedded devices

- Wipes file system and storage device

- Overwrites data with values decrementing from 0xFFFFFFFF

- First disruptive campaign that affected outside of Ukraine, similar to historic GRU disruptive operations like NotPetya

©2023 Mandiant

20

## Slide 21

## CADDYWIPER

- Initially deployed against financial sector prior to targeting government

- Turned into the “go-to” wiper for most of the 2022

- Checks if it’s executing on the domain controller via the DsRoleGetPrimaryDomainInformation

- Starts wiping the c:\Users folder before targeting drives D-Z

- Payload takes ownership of files before wiping

- Same technique was later utilised by JUNKMAIL

©2023 Mandiant

21

## Slide 22

## ARUGEPATCH

- ARGUEPATCH is an in-memory loader, used to execute CADDYWIPER

- Second instance of the GRU using in memory loading in an attempt to extend the lifespan of a tool

- ARGUEPATCH is functionally similar to FREETOW

- Currently 3 major versions of ARGUEPATCH to avoid detection:

- Version 1 (April 2022), deployed as IDA remote debugger. Simply loads CADDYWIPER.

- Version 2 (May 2022), deployed as an ESET tool. Loads CADDYWIPER but contains some code to implement a sleep timer.

- Version 3 (June 2022), deployed as an ESET tool. Loads a custom binary blob that contains the shellcode for the sleep timer and another shellcode for CADDYWIPER.

©2023 Mandiant 22

## Slide 23

## PRESSTEA

AKA: Prestige (Microsoft)

- (actual) Ransomware variant originally discovered by Microsoft

- Targets transportation sectors in Ukraine and Poland

- Payload uses CryptoPP library to load a public key that is used to encrypt each input file

- Deletes back-up catalogs and shadow volume copies

- Second instance during the Ukrainian Invasion of targeting outside of Ukraine by the threat actor

©2023 Mandiant

23

## Slide 24

## TANKTRAP

- GRU’s chosen lateral movement tool

- Rehashed version of SharpGPOAbuse and PowerGPOAbuse

- Used to laterally copy and execute payloads from attack box to entire network

- References SharpGPOAbuse in comments

©2023 Mandiant

24

## Slide 25

# Conclusion

**©2023 Mandiant** 25

## Slide 26

## Conclusion

- Campaign has been littered with low equity, limited use tools

- There was significant delay in replacing tools that were likely burnt at the start of the invasion

- In multiple cases, the GRU attempted to masquerade as “ransomware” actors

- Although some operations were successful, they were littered with operational errors

   - Incorrect wipers

   - Poorly written implants

- The actor attempted to introduce variety, but the wider operation led to cross contamination of operations.

- Regardless of the geopolitical risk, the GRU and wider Russian Intelligence are happy to target outside of Ukraine

©2023 Mandiant

26

## Slide 27

## Acknowledgements

- Mandiant

   - Research Team

   - Incident Response Team

   - Pokemon Master team

   - Intelligence teams

©2023 Mandiant

27

## Slide 28

### lukejenx@google.com

@lukejenx

©2023 Mandiant


> Recovered by OCR — confidence 89/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
now part or Google Cloud
lukejenx@google.com
@lukejenx
```
