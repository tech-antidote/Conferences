---
title: "An unexpected journey into Microsoft Defender's signature World"
speakers: ["Silvio", "Davide Fontana", "Antonio Villani"]
conference: "REcon"
conference_full: "REcon 2024"
edition: ""
year: 2024
source_pdf: "Recon 2024_Slides/Silvio & Davide Fontana & Antonio Villani_An unexpected journey into Microsoft Defender's signature World.pdf"
pages: 42
sha256: "e271262badd4cfe03f23872f9978d731fead7b00352261983ddec5aad831ff73"
text_chars: 18025
ocr_pages: 3
has_ocr: true
redacted_secrets: 0
ocr_confidence: 85.1
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T06:17:58Z"
---
# An unexpected journey into Microsoft Defender's signature World

**Speakers:** Silvio, Davide Fontana, Antonio Villani  
**Conference:** REcon 2024  
**Source:** `Recon 2024_Slides/Silvio & Davide Fontana & Antonio Villani_An unexpected journey into Microsoft Defender's signature World.pdf` (42 pages)


## Slide 1

https://shorturl.at/bPCzW

https://retooling.io/blog

Welcome to: An unexpected journey into Microsoft Defender's signature World

## Slide 2

# Tools you need: Download in this order

#### 1. ResourceHacker (~3MB)

2. build environment based on msys64 (~350MB)

#### 3. labs

https://shorturl.at/bPCzW

## Slide 3

# Who we are…. "The Italian doctors"  and …

@DrCh40s

\```
Davide
\```

- <u>`Silvio Antonio Davide`</u> ❑ Co-founder of Retooling LLC ❑ Co-founder of Retooling LLC ❑ Master’s degree student in Cybersecurity @ University of Sapienza

- ❑ Former Senior Cyber Security Architect @ ❑ Former Senior Cyber Security LEONARDO Spa - Cyber Security ❑ Bachelor’s degee in Information Architect @ LEONARDO Spa - Cyber

- Division Technology @ University of L’Aquila Security Division

- ❑ Senior Security Researcher @ EMC/RSA -> ❑ Passionate about malware analysis and ❑ Cyber Threat Analyst / Reverse @t0nvi

- DELL – Center of Excellence reverse engineering Engineer

- ❑ Malware reverse engineer @ Symantec - ❑ PhD System Security @ University of

- Security Response Roma Tre

- ❑ PhD Network Security @ University of ❑ M.Sc. in Computer Science

- Pisa

- ❑ M.Sc. in Computer Engineering

@davidefont96

\```
silvio@retooling.io
\```

\```
antonio@retooling.io
\```

\```
davidefontana96.df@gmail.com
\```

## Slide 4

# An unexpected journey...

Reverse the
malware
Emulate
Trigger detection
Easy peasy? Not at all..
Evade
Integrating new threats into Retooling Revo

❑ Starting point: `PingPull.exe`

❑ Initial objective: `PingPull.sln`

❑ Where we end up: `Defender.IDB`

_PingPull was written in Visual C++ and provides a threat actor the ability to run commands and access a reverse shell on a compromised host. There are three variants of PingPull that are all functionally the same but use different protocols for communications with their C2: ICMP, HTTP(S) and raw TCP. Palo Alto, Unit42_

## Slide 5

# Microsoft Defender Antivirus Architecture

MsMpEng.exe
3 MpCmdRun.exe
RPC
MpClient.dll MpEngine.dll MpClient.dll
Read
MpRtp.dll MpSvc.dll
VDM Registry
ioctl
usermode
kernelmode
WdFilter.sys WdBoot.sys
2 1 1. ELAM Driver
2. Minifilter Driver
3. PPL

## Slide 6

# Microsoft Defender's signatures files

❑ Located in: `C:\ProgramData\Microsoft\Windows`

\```
Defender\Definition Updates\<RandomGUID>\
\```

❑ Portable Executable:

   - ❑ `mpa{s,v}base.vdm` : Updated one per month, contains antimalware/antispyware signatures

   - ❑ `mpa{s,v}dlta.vdm:` Updated constantly, contains antimalware/antispyware updates to the base vdms.

- ❑ Focus on `mpavbase.vdm` and `mpasbase.vdm`

## Slide 7

# mpavbase.vdm and mpasbase.vdm

❑ Both contains compressed data (signatures) inside their resource section ( `.rsrc` ) ❑ At boostrap, `mpengine` merges the `*base.vdm` files with the `*delta.vdm` files

Magic

##### `LoadModuleHeader`

Offset Checksum?

Compressed data

## Slide 8

# Various types of signatures

\```
switch (a1)
    {
...
\```

\```
case 0x79u:
\```

\```
return"SIGNATURE_TYPE_VDLL_X86";
case 0x6Bu:
\```

\```
return"SIGNATURE_TYPE_WVT_EXCEPTION";
case 0x6Cu:
\```

\```
return"SIGNATURE_TYPE_REVOKED_CERTIFICATE";
case 0x70u:
\```

\```
return"SIGNATURE_TYPE_TRUSTED_PUBLISHER";
case 0x71u:
\```

\```
return"SIGNATURE_TYPE_ASEP_FILEPATH";
case 0x73u:
\```

\```
return"SIGNATURE_TYPE_DELTA_BLOB";
case 0x74u:
\```

\```
return"SIGNATURE_TYPE_DELTA_BLOB_RECINFO";
case 0x75u:
\```

\```
return"SIGNATURE_TYPE_ASEP_FOLDERNAME";
case 0x77u:
\```

\```
return"SIGNATURE_TYPE_PATTMATCH_V2";
case 0x78u:
\```

\```
return"SIGNATURE_TYPE_PEHSTR_EXT";
...
    }
\```

## Slide 9

# Lab0: Extract Windows Defender's signatures files

1. Open the folder `C:\ProgramData\Microsoft\Windows Defender\Definition Updates\<Your_GUID_Here>\`

2. Copy the `mpavbase.vdm` on your working folde

3. Cut the file as described to get only the compressed data. Save as `x.gz`

4. Run this `python3` script from the same folder of `x.gz` :

\```
importzlib
compressed=open('x.gz', 'rb').read()
decompressed=zlib.decompress(compressed, -zlib.MAX_WBITS)
\```

No gz header

Labab

## Slide 10

# Expected output of extracted vdm files

❑ Blobs with some `ASCII` strings referring to threats

- ❑ !Hupigon

- ❑ !Plugx.C

- ❑ …

❑ Variable distance among threat names

## Slide 11

# Microsoft Defender Antivirus Architecture

MsMpEng.exe
3 MpCmdRun.exe
RPC
MpClient.dll MpEngine.dll MpClient.dll
Read
MpRtp.dll MpSvc.dll
VDM Registry
ioctl
usermode
kernelmode
WdFilter.sys WdBoot.sys
2 1 1. ELAM Driver
2. Minifilter Driver
3. PPL

## Slide 12

# Phase1: Signatures Database preload

\```
ksignal
\```

##### `modprobe_init_worker`

It reads the header and retrieve general information s.a. signature versions and numbers `LoadModuleHeader` : loads the database header (the first 16 bytes)

**Signature version 1.401.1166.0**

Once the pre-processing of signature file completes, the defender modules initialization begins…

## Slide 13

1

##### `init_modules`

## Phase 2 Initialization of Defender modules

|3|
|---|
|Loop over all the module in
`g_pUnimodEntries`
And call the module-specific init function
`pfnInit()`|

2

##### `AutoInitModules::Initialize`

## Slide 14

# cksig_init_module

##### `pattsearch_init`

Invokes the  pattsearch_init  function initializes
the data structures that will contain the signatures:
namely  g_HstrSigs  and  g_DynamicHstrSigs
Those symbols are pointers to an hashtable which
contains all the HSTR signatures (elf, pe, macho, …)
The  load_database / load_database_cache  will
DispatchRecords  to the right bucket
hstr_search:  is one of the functions
used to perform a scan.
0x? 0x? It is used for all kind of  hstr  signatures
0x61 0x61 Pehstr records PEHSTR records
0x78 0x78 Pehstrext records PEHSTREXT records
0x85 0x85 Pehstrext2 records PEHSTREXT2 records

- ❑ Invokes the `pattsearch_init` function initializes the data structures that will contain the signatures: namely `g_HstrSigs` and `g_DynamicHstrSigs`

- ❑ Those symbols are pointers to an hashtable which contains all the HSTR signatures (elf, pe, macho, …)

- ❑ The `load_database` / `load_database_cache` will `DispatchRecords` to the right bucket

##### `g_HstrSigs`

## Slide 15

~49K ~46K ~5K

# Numbers and stats: Occurrences


> Recovered by OCR — confidence 78/100 on the text kept, 30/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Occurrences
J
wn
=
>
z
Overall
Occurences
GINS 3dAL 3YNLWNOIS
```

## Slide 16

Slicing on specific threats


> Recovered by OCR — confidence 83/100 on the text kept, 14/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
J
U
=
Keylogger
Emotet
Meterpreter
```

## Slide 17

General structure of signatures


> Recovered by OCR — confidence 95/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
General structure of signatures
SUB-RULE 1
SUB-RULE 2
```

## Slide 18

# BEGIN 2 END

`SIGNATURE_TYPE_THREAT_BEGIN` and `SIGNATURE_TYPE_THREAT_END` have custom data inside them

❑ One of them is the 4 bytes rule id (e.g. `0x8002be5f` )

\```
createrecid
\```

`typedef struct _STRUCT_` COMMON `_SIGNATURE_TYPE { UINT8 ui8SignatureType; // defines the type of the signature UINT8 ui8SizeLow; // low byte size of the signature UINT16 ui16SizeHigh; // high byte size of the signature BYTE pbRuleContent[]; // content of the rule };`

## Slide 19

# SIGNATURE_TYPE_THREAT_BEGIN

- ❑ Defines the start of a threat with the relative

\```
typedefstruct_STRUCT_SIG_TYPE_THREAT_BEGIN {
UINT8ui8SignatureType;
UINT8ui8SizeLow;
UINT16ui16SizeHigh;
UINT32ui32SignatureId;
BYTEunknownBytes1[6];
UINT8ui8SizeThreatName;
BYTEunknownBytes2[2];
CHARlpszThreatName[ui8SizeThreatName];
BYTEunknownBytes3[9];
} STRUCT_SIG_TYPE_THREAT_BEGIN,
* PSTRUCT_SIG_TYPE_THREAT_BEGIN;
\```

detection name e.g. `!Plugx.C`

- ❑ Code identifier: `0x5C`

- ❑ Contains different signatures inside, used to detect the threat

## Slide 20

# SIGNATURE_TYPE_THREAT_END

❑ Defines the end of a threat

❑ Code identifier: `0x5D`

❑ `pbRuleContent` value is the same as the corresponding ui32SignatureId used in the SIGNATURE_TYPE_THREAT_BEGIN

\```
typedefstruct_STRUCT_SIG_TYPE_THREAT_END
 {
\```

\```
UINT8  ui8SignatureType;
UINT8  ui8SizeLow;
UINT16 ui16SizeHigh;
BYTE   pbRuleContent[];
} STRUCT_SIG_TYPE_THREAT_END,
* PSTRUCT_SIG_TYPE_THREAT_END;
\```

## Slide 21

## `SIGNATURE_TYPE_PEHSTR` vs `SIGNATURE_TYPE_PEHSTR_EXT`

❑ `SIGNATURE_TYPE_PEHSTR` is used to perform string matching against Portable Executable

typedef struct _STRUCT_COMMON_SIGNATURE_TYPE { UINT8  ui8SignatureType; UINT8  ui8SizeLow; UINT16 ui16SizeHigh; BYTE   pbRuleContent[]; } STRUCT_COMMON_SIGNATURE_TYPE, *PSTRUCT_COMMON_SIGNATURE_TYPE;

❑ Code identifier: `0x61`

❑ `SIGNATURE_TYPE_PEHSTR_EXT` is used to perform byte-matching against Portable Executable ❑ Code identifier: `0x78`

## Slide 22

# PEHSTR and PEHSTR_EXT common header

\```
typedefstruct_STRUCT_PEHSTR_HEADER {
\```

- ❑ `ui8TresholdRequiredLow:` the threshold required to obtain a detection from Windows Defender (low part)

- ❑ `ui8TresholdRequiredHigh:` the threshold required to obtain a detection from Windows Defender (high part)

- ❑ `ui8SubRulesNumberLow:` the number of sub-rules that are found inside this particular signature, to identify the threat (low part).

- ❑ `ui8SubRulesNumberHigh:` the number of sub-rules that are found inside this particular signature, to identify the threat. (high part)

- ❑ `pbRuleData[]:` contains all the sub-rules, which are used to perform byte-matching detection.

\```
UINT16 ui16Unknown;
UINT8ui8TresholdRequiredLow;
UINT8ui8TresholdRequiredHigh;
UINT8ui8SubRulesNumberLow;
UINT8ui8SubRulesNumberHigh;
BYTEbEmpty;
BYTEpbRuleData[];
} STRUCT_PEHSTR_HEADER, * PSTRUCT_PEHSTR_HEADER;
\```

❑ Both types of signatures share the same structures

❑ The main difference resides in a slightly different format of the sub-rules structure

\```
SIGNATURE_TYPE_PEHSTR_EXT
\```

- ❑ `SIGNATURE_TYPE_PEHSTR` is used to detect “readable string”

- ❑ `SIGNATURE_TYPE_PEHSTR_EXT` can be used to detect opcodes and has different extra features

## Slide 23

# PEHSTR and PEHSTR_EXT sub-rule structure

- ❑ `ui8SubRuleWeightLow` : represents the weight that the sub-rule has in the detection process (low part).

- ❑ `ui8SubRuleWeightHigh` : represents the weight that the sub-rule has in the detection process (high part).

- ❑ `ui8SubRuleSize` : specify the size of the byte string to match against a given PE.

- ❑ `ui8CodeUnknown` : unknown field.

\```
typedefstruct_STRUCT_RULE_PEHSTR_EXT {
UINT8 ui8SubRuleWeightLow;
UINT8 ui8SubRuleWeightHigh;
UINT8 ui8SubRuleSize;
UINT8 ui8CodeUnknown;  //_EXT only
BYTEpbSubRuleBytesToMatch[];
} STRUCT_RULE_PEHSTR_EXT,
*PSTRUCT_RULE_PEHSTR_EXT;
\```

- ❑ `pbSubRuleBytesToMatch[]:` the bytes that must be found to obtain a detection.

##### Example with three sub-rules

## Slide 24

# Lab1: `SIGNATURE_TYPE_PEHSTR`

❑ Open your extracted `mpavbase.vdm` with a hex editor and find all the `SIGNATURE_TYPE_PEHSTR (0x61)` belonging to threat `!Darby.A`

- ❑ Highlight all the fields of each signature (HINT: make a screenshot of the

relevant bytes in the hexdump and use mspaint to highlight)

- ❑ Identify the sub-rules

- ❑ Identify the threshold

- ❑ Identify the weight of each sub-rule

Labab

## Slide 25

# `Solution SIGNATURE_TYPE_PEHSTR` : real example

- ❑ The example in figure shows a

`SIGNATURE_TYPE_PEHSTR` from threat `!Darby.A`

- ❑ `_STRUCT_PEHSTR_HEADER` :

   - ❑ `ui16Counter1` : highlighted in cyan.

   - ❑ `ui16TresholdRequired` : highlighted in

purple.

   - ❑ `ui16SubRulesNumber` : highlighted in brown.

- ❑ `_STRUCT_RULE_PEHSTR` :

   - ❑ `ui16SubRuleWeight` : highlighted in green.

   - ❑ `ui8UnknownCode` : highlighted in orange.

   - ❑ `ui8SubRuleSize` : highlighted in yellow.

   - ❑ `pbSubRuleBytesToMatch[]` : hihlighted in red

## Slide 26

# `SIGNATURE_TYPE_PEHSTR` : matching a !Darby.A signature

❑ The signature has a `ui16TresholdRequired` e qual to `0x33`

\```
Sample hexdump
\```

   - ❑ To obtain a detection the threshold must be reached

- ❑ In the example the following sub-rules are involved:

   - ❑ Sub-rule 1: weight `0x0A` .

   - ❑ Sub-rule 2: weight `0x0A` .

   - ❑ Sub-rule 3: weight `0x0A` .

   - ❑ Sub-rule 4: weight `0x0A` .

   - ❑ Sub-rule 5: weight `0x0A` .

❑ Sub-rule 6: weight `0x01` .

- `∑ = 0x33`

## Slide 27

# Fast way to check …

Scan your stuffs with `MpCmdRun.exe` utility provided by Windows Defender itself

\```
PS C:\Program Files\Windows Defender> .\MpCmdRun.exe
–Scan –ScanType3 –File <filepath> -
DisableRemediation–Trace –Level 0x10
\```

## Slide 28

# Lab2: Remove Darby signature

- ❑ Add a folder to the Defenders exclusions

\```
PS> Add-MpPreference -ExclusionPath 'C:\YOUR_PATH_HERE'
\```

- ❑ Copy the Darby zip into the excluded folder and uncompress it (pwd:infected)

- ❑ Open the binary with an hex editor

- ❑ Identify which bytes trigger the signature and modify them to evade the detection

   - ❑ What is the minimum number of bytes that you have to modify to avoid the dection?

- ❑ How the total weight is affected when the same sub-rule appear more than once?

   - ❑ Suppose that the string `S_1` with  weight `W_1` appears twice in the binary. Does the binary get a weight of `2*W_1` ?

Labab

## Slide 29

# Give some power to EXT

❑ Multiple patterns are present inside subrules in `SIGNATURE_TYPE_PEHSTR_EXT`

- ❑ It can be used to detect opcodes and more

- ❑ Used to match specific sequences of bytes

- ❑ Wildcard identified:

   - ❑ `90 01 XX`

   - ❑ `90 02 XX`

   - ❑ `90 03 XX YY`

   - ❑ `90 04 XX YY`

   - ❑ `90 05 XX YY`

- ❑ Wildcard still unknown:

   - ❑ `90 06 -> 90 20`

## Slide 30

# Patterns: `90 01 XX`

Pattern `90 01 XX:`

❑ Used in sub-rules in `SIGNATURE_TYPE_PEHSTR_EXT`

- ❑ Match a sequence of bytes that has a specific length defined by `XX` ,

❑ The sequence must appear just after the XX byte

- ❑ An example is highlighted in blue

\```
PlugxA-Sub-Rule3-Example{
strings:
\```

\```
$sub_rule_3_hex = {
\```

\```
45 78 69 74 C7 85 ?? FF FFFF54 68
72 65 66 C7 85 ?? 04 FF FFFF61 64
\```

\```
}
condition:
$sub_rule_3_hex
\```

\```
}
\```

## Slide 31

# Patterns: `90 01 XX`

Pattern `90 01 XX` detection:

- ❑ Using `MpCmdRun.exe`

- ❑ The bytes placed in place of the pattern `90 01 01` are (Highlighted in blue):

   - ❑ `0x00`

   - ❑ `0x04`

- ❑ In red sub-rule 2

- ❑ In green sub-rule 3

- ❑ Expected detection: `Plugx.A`

## Slide 32

# Patterns: `90 02 XX`

#### Pattern `90 02 XX:`

❑ Used as a placeholder to match up to

   - `XX` bytes in a specific position

- ❑ Example of pattern highlighted in cyan

\```
rule PlugxA-Sub-Rule2-Example {
strings:
\```

\```
$sub_rule_2_hex = {75 61 6C 41 C7 [0-16] 6C 6C6F 63 }
condition:
\```

- `$sub_rule_2_hex`

\```
}
\```

## Slide 33

# Patterns: `90 02 XX`

❑ The bytes in place of the pattern `90 02 10` and are highlighted in violet

❑ The entire sub-rule 2 is

### highlighted in red

## Slide 34

# Patterns: `90 03 XX YY`

Pattern `90 03 XX YY` :

❑ `XX` : the length of the first sequence (Sequence_A) of bytes following the pattern in pink

❑ `YY` : the length of the second sequence (Sequence_B) of bytes following the pattern in grape

❑ In the matching sample either Sequence_A or <u>Sequence_B</u> may appear

\```
rule BankerYB_Sub_Rule1_Example{
\```

\```
strings:
\```

\```
$sub_rule_1_hex = { 50 6f 6c 69 63 69 65 73 5c 45 78 70 6c 6f 72 65 72 5c 52 75 6e 22 20 2f 76 20 22
(43 49 50 41|56 49 50 41) 22 20 2f 64 20 43 3a 5c 55 6e 6e69 73 74 74 61 6c 6c2e
65 78 65 20 2f 74 20 22 52 45 47 5f 53 5a 22 20 2f 66 00 90 00
}
condition:       $sub_rule_1_hex
\```

\```
}
\```

## Slide 35

# Patterns: `90 04 XX YY`

❑ `XX` : the length of the expected bytes

\```
rule Pattern-90-04-example {
\```

\```
strings:
\```

❑ `YY` : the length of the regex-like pattern in the figure highlighted in violet

\```
$example1_90_04 =
\```

\```
{ 68 74 74 70 3a 2f 2f61 72 70 2e 31 38 31 38[30-39] [30-
39]2e 63 6e 2f 61 72 70 2e 68 74 6d 90 00 }
\```

❑ The bytes following `90 04 XX YY` describes the pattern itself, in a regex-like fashion:

###### `$example2_90_04 =`

\```
{ 5c 48 61 70 70 79[30-39] [30-39] 68 79 74 2e 65 78 65 90
00 }
\```

❑ In this example the bytes are `30 2d 39` ,

\```
condition:
\```

highlighted in blue which is `0-9`

\```
$ example1_90_04 and $ example2_90_04
\```

\```
}
\```

##### example1

example2

## Slide 36

# Patterns: `90 04 XX YY`

❑ The bytes replacing the pattern `90 04 02 03` `30 2D 39` `(example1)` are:

   - ❑ `0x30`

   - ❑ `0x39`

   - ❑ Highlighted in cyan

- ❑ In red the bytes matching the sub-rule

example1

## Slide 37

# Patterns: `90 05 XX YY`

❑ `XX` : the max length of the expected bytes

❑ `YY` : the length of the regex-like pattern in the figure highlighted in grape

- ❑ Differently from pattern 04, this pattrns is case insensitive

- ❑ The bytes following `90 05 XX YY` describes the pattern itself, in a regex-like format

\```
rule Pattern-90-05-example{
strings:
$example_90_05 =
"http://[a-zA-Z]{0,64}\\.com/dfrg32\\.exe“
condition:
$example_90_05
}
\```

## Slide 38

# Lab3: Match the detection

- ❑ Open `msys64` folder and run `msys64.exe`

- ❑ Change the current folder to the root of the lab using the following command `cd /c/<your_path>/lab3_stration/Exercise`

- ❑ Analyze the Stration.CC PEHSTR signature

   - ❑ Understand weights and wildcards

- ❑ Modify the provided `StrationCC.c` file in such a way that once it is compiled, matches the Stration.CC detection

- ❑ To compile use the `build.sh` script

Labab

## Slide 39

# Solution: Patterns: `90 05 XX YY`

❑ The bytes replacing the pattern `90 05 40 03 61 2D 7A` in sub-rule 2 are highlighted in blue

- ❑ In red fixed bytes of sub-rule 2

❑ Expected detection: `Stration.CC`

## Slide 40

# Final lab

❑ <u>GOAL: implement a working example that triggers the Defender signature</u> `Backdoor:Win64/Havoc.A!MTB`

1. Open the extracted signature database and find the signature

   - ❑ Understand the type of signature

   - ❑ Understand what the signature bytes represents

2. Decompile the provided sample in `lab4_havoc\Exercise\sample.zip` (it is a real MALWARE, so handle with care. PWD: infected) ❑ Identify and analyze the function that triggers the detection

3. Modify the `lab4_havoc\Exercise\havoc_emu_asm.S` to include the same implementation present within the provided sample for the `XorAlgorithm`

4. To compile use the `build.sh` script

Labab

## Slide 41

https://retooling.io/blog

_That’s All Folks_ `silvio@retooling.io antonio@retooling.io`

## Slide 42

# Reference

❑ https://www.safebreach.com/blog/defender-pretender-when-windowsdefender-updates-become-a-security-risk/

❑ https://gist.githubusercontent.com/mattifestation/3af5a472e11b7e135273e71cb5f ed866/raw/15be4f2ae75b2d62465cf9faef72a2f61147a393/ExpandDefenderSig.p s1

❑ https://learn.microsoft.com/en-us/defender-endpoint/command-linearguments-microsoft-defender-antivirus
