---
title: "Defender-Pretender When Windows Defender Updates Become a Security Risk"
speakers: ["Tomer Bar", "Omer Attias"]
conference: "Black Hat"
conference_full: "Black Hat USA 2023"
edition: "USA"
year: 2023
source_pdf: "Black Hat USA 2023 slides/Tomer Bar & Omer Attias_Defender-Pretender When Windows Defender Updates Become a Security Risk.pdf"
pages: 91
sha256: "92c433265610c6d6fa5ab3a335d4111bf5fcc26db5cd2adcd71228d917a047ce"
text_chars: 21075
ocr_pages: 26
has_ocr: true
redacted_secrets: 0
ocr_confidence: 83.5
ocr_unreliable_blocks: 4
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T04:23:10Z"
---
# Defender-Pretender When Windows Defender Updates Become a Security Risk

**Speakers:** Tomer Bar, Omer Attias  
**Conference:** Black Hat USA 2023  
**Source:** `Black Hat USA 2023 slides/Tomer Bar & Omer Attias_Defender-Pretender When Windows Defender Updates Become a Security Risk.pdf` (91 pages)


## Slide 1

LABS

Defender - Pretender When Windows Defender Updates Become a Security Risk

Omer Attias Tomer Bar

## Slide 2

# Tomer Bar

###### **VP of Security Research @ SafeBreach**

- **SafeBreach** has been qualified to speak **10** talks at **Black Hat USA**

- 20 years experience in security research

- Main focus in APT and vulnerability research

- Presented at many global security conferences Such as: Black Hat USA 2020, DEFCON 28-30

- 2023 - Qualified to speak 3 talks at Black Hat, DEFCON

LABS

2

## Slide 3

# Omer Attias

###### **Security Researcher @ SafeBreach**

● 6 years of experience in cyber security

● Main focus in low level & vulnerability research

● Technology and science enthusiast

LABS

## Slide 4

##### **Agenda**

● Introduction

● Defender Update Process

● The vulnerability

- Attack vectors

● Takeaways

● Q & A

4

## Slide 5

**Defender - Pretender**

## Slide 6

##### **Motivation - Flame**

● Discovered by Kaspersky in 2012

● State-Sponsored

● 20 MB of code

● One of the most sophisticated Malware ever analyzed

● Signed with a fraudulent Microsoft certificate

● Flame Hijacked Microsoft updates

For lateral movement

## Slide 7

##### **Research Goal and challenges**

Achieve similar capabilities running as an unprivileged user <u>without</u> possessing a forged certificate and without using MITM.

Resulting in turning the original Windows Defender process to our full control.

## Slide 8

Update Process High Level Understanding

## Slide 9

##### **What Windows Defender Pulls?**

**M** icrosoft **P** rotection **A** ntimalware **F** ront **E** nd.


> Recovered by OCR — confidence 87/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
] What Windows Defender Pulls?
Check For Updates
fz} MPAM-FE.exe
== Microsoft
Microsoft Protection Antimalware Front End.
```

## Slide 10

##### **mpam-fe.exe Resources**

Extract Extract Resource CAB Update Payload mpam-fe.exe

mpengine.dll VDM
VDM
VDM
VDM

MpSigStub.exe

## Slide 11

**mpam-fe.exe Execution**


> Recovered by OCR — confidence 78/100 on the text kept, 60/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
1 mpam-fe.exe Execution
C\Users\POTAT.
C:\Program Files (,
C:\Program Files (,
Description: Microsoft Malware Protecti®a Signature Update Stub
Company: Microsoft Corporation
User: toystory\potatchead
PID: 8252 Started: = 7/4/2023 7:15:39 AM
Exited: 7/4/2023 7:13:39 AM
```

## Slide 12

**Database Files & mpengine.dll**


> Recovered by OCR — confidence 81/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
1 Database Files & mpengine.dll
> ThisPC > Local Disk (C:) >» ProgramData » Microsoft >» Windows Defender > Definition Updates >» {53291405-777E-4779-8D90-A058720A4481}
A
Name Date modified Type Size
. [] mpasbase.vdm 7/4/2023 3:31 AM VDM File 73,628 KB
D mpasdita.vdm 7/4/2023 3:31 AM VDM File 7,714 KB
. D mpavbase.vdm 7/4/2023 3:31 AM VDM File 36,861 KB
. [|] mpavdita.vdm 7/4/2023 3:31 AM VDM File 2,568 KB
mpengine.dll 7/4/2023 3:31 AM Application exten... 17,978 KB
```

## Slide 13

##### **Base & Delta Files**

MZ
MZ
Delta
Base

## Slide 14

##### **Base & Delta Versions**

MZ
MZ
1.391.3508.0
1.391.0.0
Delta
Base
<major.minor.build.revision>

## Slide 15

##### **Security Intelligence Version**

MZ
1.391.3508.0
Delta


> Recovered by OCR — confidence 92/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
1 Security Intelligence Version
Security intelligence
Microsoft Defender Antivirus uses security intelligend
We try to automatically download the most recent in
your device against the newest threats. You can also
Updates.
Security intelligence version: 1.391.3508.0
Version created on: 7/3/2023 5:47 PM
Last update: 7/4/2023 3:31 AM
1.391.3508.0
```

## Slide 16

##### **Digital Signature**

Update Payload

Delta

Base

mpengine.dll

Delta

Base


> Recovered by OCR — confidence 85/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
] Digital Signature
a —— Digital Signature Details ? x
) =, Digital Signature Information
pd This digital signature is OK.
Update Payload
Signer information
E-mail: Not availabl
Delta Delta JNotavalabe
Signing time: |Friday, May 12, 2023 2:06:17 PM
{OF View Certificate
Countersignatures
. \ \ Name of signer: E-mail address: Timestamp
Microsoft Time-S... Not available Friday, May 12, 202...
Base Base
```

## Slide 17

##### **Update Process Summary**

mpam-fe.exe

Update Payload
Delta Delta

MpSigStub.exe mpengine.dll Base Base

## Slide 18

Playing Around With The Files The First Clue That Something Is Fishy

## Slide 19

##### **Pick a Target**

Update Payload
Delta Delta
MpSigStub.exe mpengine.dll
Base Base

mpam-fe.exe

## Slide 20

##### **Trying To Modify MpEngine.dll**

Update Payload
Delta Delta
FAKE Base Base
MpSigStub.exe
mpengine.dll

## Slide 21

##### **Trying To Modify MpEngine.dll**

Update Payload
Execute “Stub”
Delta Delta
FAKE Base Base
MpSigStub.exe
mpengine.dll

Execute “Stub”

## Slide 22

##### **Trying To Modify MpEngine.dll**

Update Payload
Delta Delta
MpSigStub.exe mpengine.dll
Base Base

## Slide 23

##### **Trying To Modify the VDM files**

Update Payload

Execute “Stub”

Delta Delta
mpengine.dll Base Base

MpSigStub.exe

## Slide 24

MZ
1.391.3509.0
Delta

##### **First Clue That Something Is Fishy**

MZ
1.391.3508.0
Delta

## Slide 25

Trying To Modify Random Byte
MZ MZ
Random
Random
byte
byte+1
1.391.3508.0 1.391.3509.0
Delta Delta

##### **Trying To Modify Random Byte**

## Slide 26

##### **Summary**

● We gained basic understanding of the update process ● Investigated each file involved

● We **failed** to modify mpengine.dll

● We **successfully** updated Defender with Using a modified ‘VDM’ file version

● A low privileged user can run an update

● We **failed** to update using random data modification

## Slide 27

MpSigStub to MsMpEng Update With a Low Privilege User

## Slide 28

##### **MpSigStub to MsMpEng**

**MsMpEng.exe** _Microsoft Malware Protection Engine_

**MpSigStub.exe** Malware Protection Signature Update Stub

**???**

Protected Process Light Process (PPL)

Black Box

## Slide 29

##### **MpSigStub to MsMpEng**

Manual reversing reveals RPC_GUID which belongs to mpsvc.dll RPC func num:42


> Recovered by OCR — confidence 84/100 on the text kept, 57/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
l MpSigStub to MsMpEng
Manual reversing reveals RPC_GUID which belongs to mpsvc.dll
RPC func num:42
dq offset unk_75BSBA1De
db 8
db 8
dw 443Ah @ -> servertipenabiereature
1- yerMpDisableFeature
9
42 -> ServerMpUpdateEngineSignature
```

## Slide 30

##### **MpSigStub to MsMpEng**

Unprivileged process
MpSigStub.exe
Malware Protection Signature
Update Stub
MpClient.dll
Defender Client Interface

Privileged process
Msmpeng.exe
Microsoft Malware Protection Engine
Protected Process Light Process
(PPL)
MpSVC.dll
Defender RPC server
MpEngine.dll
Defender Scan Engine

## Slide 31

##### **Execution Flow - mpsvc to mpengine**

**mpsvc::** InitEngineContext

**mpengine::** __rsignal

**mpengine::** StartMpEngine **mpengine::** DispatchSignalHelper

**mpengine::** ksignalupper

**mpengine::** ModProbeInit

**mpengine::** modprobe_init_worker

Called 4 times

**mpengine::** LoadDatabase **mpengine::** ConsumeInputCompressed

## Slide 32

### **VDM File Format**

32

## Slide 33

##### **VDM File Format**

MZ
sections
.rdata
.rsrc
RMDX
COMPRESSED DATA

## Slide 34

##### **VDM File Format**

MZ
RMDX
Defender
Resource
Zlib
Signatures
Compressed
VDM

## Slide 35

**The Signatures Are Not Encrypted!** **_Base file_**

proprietary structure **Threat Name Signature Bytes**


> Recovered by OCR — confidence 82/100 on the text kept, 82/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
1 The Signatures Are Not Encrypted!
proprietary structure
Base file
Signature Bytes
0001 0203 0405 0607 0809 OAOB OCOD OEOF 0123456789ARCDEF
0x00 SC1E 0000 4506 0000 0000 0100 OBOO 0800 \...E...........
0x10 F421 4163 6FE6E 7469 0000 0540 0582 2400
0x20 0400 4045 0000 0400 0103 0000 0000 9OZA ..@E.........-.
0x30 3000 0000 0000 0000 0000 0002 £500 0008 O...............
0x40 3000 ODDA FA83 7200 0000 Sv00 0000 0027 0O..UGfr........
0x50 3006 0B34 6BA2 924F <£B36 ODOO 0000 0045 0..4k¢’0&é6.....
0x60 3000 08C1 59D2 rE00 0000 0061 Oc01 0008
0x70 0008 009 0000 0100 2261 0063 OOGF OOGE /........
0x80 0072 0069 0020 004E 0065 0074 0053 0065
Oxfu 0072 0076 0069 0063 0065 0001 0016 706F
OxAO 7274 2E61 636F 6E74 692E GEG5 742F 6469 J rt.aconti.net/di
OxBO 616C 6572 0100 1141 4Cé6é5 6665 7374 796C Jaler...ALifestyl
OxCO 652E 6163 6F6E 7469 0100 0B41 4Cé6é9 6665 Je.aconti...ALife
OxDO 4469 616C 6572 0100 0C53 6563 7572 6544 | Dialer...SecureD
OxEO 6961 6C65 7201 OOOA 676F 6F64 7468 696E Jialer...goodthin
OxFO 7878 0100 OF64 6961 6C65_ 2225 ioc G2P) xx...dialer/stub
6961 6C65 7268 6173 J] .exe..&dialerhas
2664 6961 6CE65 7276 | hwert=%sé&dialerv
7525 7325 7301 0014 J ersion=%uts%s...
5c41 4Cc69 6665 7374 | Software\ALifest
686F 7745 726F 7469 J yle\...ShowEroti
4944 3D25 7526 4E72 Jc. .%%s?UID=%uéNr
7472 793D 2573 2669 | =%s&Country=ts&i
7500 0067 1600 OO0FO dcode=%u..g...
AFCO BDOO 4200 0000
```

## Slide 36

##### **Delta Decompressed Data**

Zlib Zlib
Compressed Compressed
Delta Base
Defender
Unknown
Signatures


> Recovered by OCR — confidence 90/100 on the text kept, 75/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
] Delta Decompressed Data
0x00
0x10
0x20
0x30
0x40
0x50
0x60
0x70
0x80
0x90
OxBO
OxEO
OxFO
ooo1
7450
2902
67B1
TE24
9601
E70B
0100
FFOB
OOFF
c102
0400
4653
EBO4
2058
0203
0000
0000
3600
0000
0000
0000
SCFF
DD30
0600
FFFF
80B9
2401
3886
0405
1300
4008
6col
8013
B30B
738D
FFO1
OOFF
8002
0300
0120
0300
807A
5206
6F16
0607
0000
0000
0000
0000
0000
2208
0000
FF10
00B7
0400
0500
0030
ADSE
2702
8701
BFO2
OOFF
BOLF
34E6
767A
2DD8
2FCD
6706
OAOB
0000
0000
0000
0000
0000
FFO6
OOFF
0003
3CF7
FFFF
0400
5306
173c
0016
ocoD
280A
8F04
CFO6
pool
8000
0280
6C7A
0500
A708
0085
OEOF
0000
0000
0000
0000
0000
8FOE
OOFF
0002
0300
0100
SF78
gt6.1..
~$..€..
Zlib
Compressed
Defender
Signatures
```

## Slide 37

Signature Structure

## Slide 38

**Signature Structure**


> Recovered by OCR — confidence 81/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
1 Signature Structure
bitfield SigqnatureHeader {
Type: 3;
Size: 24:
struct Signature {
SignatureHeader header;
ud Datal header. Size};
```

## Slide 39

**Signature Types**


> Recovered by OCR — confidence 84/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
1 Signature Types
"SIGNATURE_TYPE_CKOLDREC",
"SIGNATURE_TYPE_KVIR32",
"SIGNATURE_TYPE_POLYVIR32",
"SIGNATURE_TYPE_NSCRIPT_NORMAL",
"SIGNATURE_TYPE_NSCRIPT_SP",
"SIGNATURE_TYPE_NSCRIPT_BRUTE",
"SIGNATURE_TYPE_TITANFLT",
"SIGNATURE_TYPE_PEFILE_CURE",
"SIGNATURE_TYPE_MAC_CURE",
"SIGNATURE_TYPE_SIGTREE",
"SIGNATURE_TYPE_SIGTREE_EXT",
"SIGNATURE_TYPE_MACRO_PCODE",
"SIGNATURE_TYPE_MACRO_SOURCE",
"SIGNATURE_TYPE_BOOT",
"SIGNATURE_TYPE_CLEANSCRIPT",
"SIGNATURE_TYPE_TARGET_SCRIPT",
"SIGNATURE_TYPE_CKSIMPLEREC",
"SIGNATURE_TYPE_PATTMATCH" ,
"SIGNATURE_TYPE_UNPLIB",
"SIGNATURE_TYPE_DEFAULTS",
"SIGNATURE_TYPE_DBVAR",
Ox5C: "SIGNATURE_TYPE_THREAT_BEGIN",
"SIGNATURE_TYPE_FILENAME",
"SIGNATURE_TYPE_FILEPATH",
"SIGNATURE_TYPE_PEHSTR",
"SIGNATURE_TYPE_LOCALHASH",
1100:
105:
106:
SIGNATURE_TYPE_REMOVAL_POLICY",
SIGNATURE_TYPE_WVT_EXCEPTION",
SIGNATURE_TYPE_REVOKED_CERTIFICATE",
SIGNATURE_TYPE_TRUSTED_PUBLISHER",
: “SIGNATURE_TYPE_ASEP_FILEPATH",
SIGNATURE_TYPE_DELTA_BLOB",
SIGNATURE_TYPE_DELTA_BLOB_RECINFO",
SIGNATURE_TYPE_ASEP_FOLDERNAME",
SIGNATURE_TYPE_PATTMATCH_V2",
SIGNATURE_TYPE_PEHSTR_EXT",
: "SIGNATURE_TYPE_VDLL_X86",
SIGNATURE_TYPE_VERSIONCHECK",
SIGNATURE_TYPE_SAMPLE_REQUEST",
SIGNATURE_TYPE_VDLL_X64",
SIGNATURE_TYPE_SNID",
SIGNATURE_TYPE_KCRCE",
SIGNATURE_TYPE_VFILE",
SIGNATURE_TYPE_SIGFLAGS",
SIGNATURE_TYPE_PEHSTR_EXT2",
: "SIGNATURE_TYPE_PESTATIC",
"SIGNATURE_TYPE_PEPCODE",
"SIGNATURE_TYPE_IL_PATTERN",
: "SIGNATURE_TYPE_MACHOHSTR_EXT",
: "SIGNATURE_TYPE_DOSHSTR_EXT",
: "SIGNATURE_TYPE_TARGET_SCRIPT_PCODE",
: "SIGNATURE_TYPE_VDLL_IA64",
"SIGNATURE_TYPE_AAGGREGATOR" ,
153:
154:
155:
156:
157:
158:
159:
160:
161:
162:
163:
164:
165:
166:
167:
168:
169:
170:
171:
172:
173:
174:
175:
178:
1179:
180:
181:
182:
183:
184:
186:
187:
188:
189:
190:
"SIGNATURE_TYPE_TUNNEL_X64",
"SIGNATURE_TYPE_TUNNEL_IA64",
"SIGNATURE_TYPE_THREAD_X64",
"SIGNATURE_TYPE_THREAD_IA64",
"SIGNATURE_TYPE_VDM_METADATA",
"SIGNATURE_TYPE_VSTORE",
"SIGNATURE_TYPE_VDLL_SYMINFO",
"SIGNATURE_TYPE_IL2_PATTERN",
"SIGNATURE_TYPE_BM_STATIC",
"SIGNATURE_TYPE_NDAT",
"SIGNATURE_TYPE_FASTPATH_DATA",
"SIGNATURE_TYPE_FASTPATH_SDN",
"SIGNATURE_TYPE_DATABASE_CERT",
"SIGNATURE_TYPE_SOURCE_INFO",
"SIGNATURE_TYPE_HIDDEN_FILE",
"SIGNATURE_TYPE_COMMON_CODE",
"SIGNATURE_TYPE_VREG",
"SIGNATURE_TYPE_THREAD_ARM",
"SIGNATURE_TYPE_PCODEVALIDATOR",
"SIGNATURE_TYPE_MSILFOP",
"SIGNATURE_TYPE_KPATEX",
"SIGNATURE_TYPE_LUASTANDALONE",
190:
191:
192:
193:
194:
195:
196:
197:
198:
199:
200:
201:
202:
203:
204:
205:
206:
207:
208:
209:
210:
211:
212:
213:
214:
215:
216:
217:
218:
219:
220:
222:
223:
224:
225:
226:
227:
228:
229:
230:
231:
232:
233:
234:
235:
"SIGNATURE_TYPE_JAVAHSTR_EXT",
"SIGNATURE_TYPE_MAGICCODE",
"SIGNATURE_TYPE_CLEANSTORE_RULE",
"SIGNATURE_TYPE_VDLL_CHECKSUM",
"SIGNATURE_TYPE_THREAT_UPDATE_STATUS",
"SIGNATURE_TYPE_VDLL_MSIL",
"SIGNATURE_TYPE_ARHSTR_EXT",
"SIGNATURE_TYPE_MSILFOPEX",
"SIGNATURE_TYPE_VBFOPEX",
"SIGNATURE_TYPE_FOPEX64",
"SIGNATURE_TYPE_JSINIT",
"SIGNATURE_TYPE_PESTATICEX",
"SIGNATURE_TYPE_KCRCEX",
"SIGNATURE_TYPE_FTRIE_POS",
"SIGNATURE_TYPE_MACRO_PCODE64",
"SIGNATURE_TYPE_BRUTE",
"SIGNATURE_TYPE_INNOHSTR_EXT",
"SIGNATURE_TYPE_ROOTCERTSTORE",
"SIGNATURE_TYPE_EXPLICITRESOURCE",
"SIGNATURE_TYPE_CMDHSTR_EXT",
"SIGNATURE_TYPE_FASTPATH_TDN",
"SIGNATURE_TYPE_EXPLICITRESOURCEHASH",
"SIGNATURE_TYPE_FASTPATH_SDN_EX",
"SIGNATURE_TYPE_BLOOM_FILTER",
"SIGNATURE_TYPE_VDLL_META_MSIL",
"SIGNATURE_TYPE_MDBHSTR_EXT",
"SIGNATURE_TYPE_SNIDEX",
"SIGNATURE_TYPE_SNIDEX2",
"SIGNATURE_TYPE_AAGGREGATOREX",
"SIGNATURE_TYPE_PROPERTY_BAG",
"SIGNATURE_TYPE_DMGHSTR_EXT",
"SIGNATURE_TYPE_DATABASE_CATALOG",
```

## Slide 40

##### **Threat Begin & Threat End**

Begin

**End**

## Slide 41

**Evaluation**


> Recovered by OCR — confidence 85/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
] Evaluation
try:
while True:
Signature.read_one(base_data)
counter += 1
except Exception:
print(f'Total Signatures: {counter}' )
thon .\CountSignatures. py
Total Signatures: 2643614
```

## Slide 42

**Threat Begin Signature**

## Slide 43

**Smart modification on Conti Signature**


> Recovered by OCR — confidence 83/100 on the text kept, 65/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
] Smart modification on Conti Signature
#include <stdlib.h>
wchar_t* = L"aconti NetService";
“port.aconti.net/dialer";
"ALifestyle.aconti";
“dialerhashwert=%s&dialerversion=%u%s%s" ;
"Software\\ALifestyle\\";
"ShowErotic";
t main()
0063
0074
0001
6E6S
6S63
rt.aconti.net/di
aler...ALifestyl
Dialer...SecureD
xx...dialer/stub
-exe..&dialerhas
hwert=tsédialerv
ersion=tutsts...
Software\ALifest
yle\...ShowEroti
```

## Slide 44

**Smart modification on Conti Signature**


> Recovered by OCR — confidence 92/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
] Smart modification on Conti Signature
Dialer:Win32/Aconti
Alert level: Severe
Status: Active
Date: 5/9/2023 5:01 AM
Category: Dialer
Details: This program dials toll numbers to gain access to adult content.
aconti Affected items:
file: C:\Users\potatohead\Desktop\aconti.exe
```

## Slide 45

**Modify Conti Threat Name – Update failed**


> Recovered by OCR — confidence 84/100 on the text kept, 71/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
1 Modify Conti Threat Name - Update failed
0405 0607 0809 0B OCOD OEO 0123456789A;CDEF
0 4506 0000 0000 0100 OBO0O0 0800
6F6E 7469 000
0000 0000 0000 0000
FA83 7200 0000 0000 0000 00
0 3006 0 6BA2 924F EB36 ODO0O0 0000 00
0 3000 0 59D2 FEOO 0000 0061 0c01 000
0072 0069 0063 0065 0016
Directory: C:\Defs OxAO 7274 636F 6E74 692E 742F
ERROR @x8@5@a904) : MpUpdateEngine(C: \Defs)
ERROR @x8@5@a904) : MpUpdateEngine(C: \Defs)
ERROR @x6@59a004): Failed to update signatures from C:\Defs
```

## Slide 46

The Validation

## Slide 47

##### **Quick Reminder**

**mpengine.dll**

##### **For Each VDM:**

Base
Delta
Base
Delta
LoadDatabase

**_ConsumeInputCompress_**

## Slide 48

**RMDX Header RMDX & Zlib Headers**


> Recovered by OCR — confidence 67/100 on the text kept, 53/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
|) RMDX & Zlib Headers Tear he ——
u32 Signature;
Use DecompressedDataSi ze;
```

## Slide 49

##### **RMDX & Zlib Headers**

**Zlib Data Header**

## Slide 50

**CRC32 Algorithm**


> Recovered by OCR — confidence 83/100 on the text kept, 46/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
) CRC32 Algorithm
Algorithm
CRC- 32
CRC-32/MPEG-2
CRC-32/SATA
Result
Check
@xCBF43926
@xFC891918
Poly
Init
@xFFFFFFFF
@xFFFFFFFF
```

## Slide 51

##### **Trying One More Update Attempt**

VDM File

New
Raw Signatures
VDM File

## Slide 52

**Trying One More Update Attempt**


> Recovered by OCR — confidence 82/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
1 Trying One More Update Attempt
ERROR @x805@a004 : MpUpdateEngine(C:\Defs)
ERROR @x805@a004 : MpUpdateEngine(C:\Defs)
ERROR 6x8@50a004 : Failed to update signatures from C:\Defs
```

## Slide 53

##### **How Do We Modify?**

MZ
Delta
Base
IGNORED

Modified

## Slide 54

##### **Two Pairs Of VDM Files**

mpavdlta mpasdlta
VDM VDM
AntiVirus AntiSpyware
mpavbase mpasbase
VDM VDM

## Slide 55

##### **What The Purpose Of Delta Files?**

**1.391.0.0 1.391.3508.0** Base Delta

**1.391.3508.0** Merged

## Slide 56

The Merge Internals

## Slide 57

##### **What’s The Delta Format?**

Delta


> Recovered by OCR — confidence 87/100 on the text kept, 72/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
] What's The Delta Format?
bitfield SignatureHeader {
Type: 8;
Size: 24
struct Signature {
SignatureHeader header;
```

## Slide 58

##### **BLOB_RECINFO & BLOB**

###### **BLOB_RECINFO**

**BLOB**

## Slide 59

**BLOB Structure**

## Slide 60

**Actions**

## Slide 61

##### **Reverse ConsumeInputCompress**

MSB Check

## Slide 62

##### **Action Types**

**Copy From Delta**

Copy <size> bytes from the current position of delta file to the **<u>merge</u> file**

##### **Copy From Base**

Copy <size> bytes from <offset> within the base file

to the **<u>merge</u> file**

## Slide 63

##### **Action Header**

_WORD_ 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1

###### Action Type

## Slide 64

##### **CopyFromDelta - Example**

01 00 5C
MSB
<bytes>
<size> = 1
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1

## Slide 65

##### **Action Header -** **CopyFromBase**

WORD
1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1

###### CopyFromBase

## Slide 66

Action Header -  CopyFromBase
WORD
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
<size>
0xffff & 0x7fff 6
(0x8005)
MSB Off

## Slide 67

##### **CopyFromBase - Example**

FF FF 01 00 00 00
Action Header <offset>

(0xffff & 0x7fff) + 0x6 = 0x800 ~~5~~

<size>

## Slide 68

##### **Sum Up**

Actions

Delta

BLOB

## Slide 69

**Merge Algorithm**


> Recovered by OCR — confidence 89/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
1 Merge Algorithm
def merge(actions: list, base: io.BytesI0O):
merge_stream = io.BytesI0()
for action in actions:
if action.type == CopyFromBase:
CopyFromBase: <size><offset>
base.seek(action.offset)
bytes = base.read(action.size)
else:
CopyFromDelta: <size><bytes>
bytes = actions.bytes
merge_stream.write(bytes)
return merge_stream
```

## Slide 70

##### **Diffing Base and Merge**

#### **Base**

#### **After Merge**

## Slide 71

**Eureka - Unknown Numbers**


> Recovered by OCR — confidence 75/100 on the text kept, 58/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
] Eureka - Unknown Numbers
struck Blob { struck Blob {
```

## Slide 72

##### **Validations Recap - Zlib Data Validation**

<CRC>
Zlib
Compressed
VDM
Zlib
<CRC CalculateCRC
Compressed
>

## Slide 73

##### **Validations Recap - Merge Validations**

GetSiz Merged
e
CalculateCRC Merged

<MergedSize>

<MergedCRC>

## Slide 74

**Can We Fake an Update?**

## Slide 75

##### **We Did It !!!**

Updated to: 1.383.1800

Version Before


> Recovered by OCR — confidence 90/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
MpSigStub successfully updated Microsoft Windows Defender (RS1+) using the AM Bases and Delta package.
Original: Updated to:
AS base VDM: 1.383.0.0 1.383.0.0
AV base VDM: 1.383.0.0 1.383.0.0 Updated to: 1.383.1800
AS delta VDM: 1.383.1799.@ 1.383.1800.0
AV delta VDM: 1.383.1799.@ 1.383.1800.0
```

## Slide 76

Attack Vectors (CVE-2023-24934)

## Slide 77

**wd-pretender**

## Slide 78

##### **Delete LaZagane Threats**

Delete LaZagane Threats
Conti
LaZagane
Threats
Mimikatz
Threat #4
Merged

## Slide 79

Delete LaZagne Threats


> Recovered by OCR — confidence 71/100 on the text kept, 61/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
3 powershell (running as TOYSTORY\weak)
PS C:\Users\weak\work> .
View »
Name Date modified Type Size
Y We Quick access
IEF MpSigstub 1/91/2023 6:17 AM Application 785 KB
I Desktop *
Pictures *
h BB Videos *
BE work
litem | (=
es 3:28AM
```

## Slide 80

##### **Friendly Files**

##### 30,000 friendly hashes


> Recovered by OCR — confidence 84/100 on the text kept, 60/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
|) Friendly Files
30,000 friendly hashes
"SIGNATURE_TYPE_THREAD_X64",
“SIGNATURE_TYP
_SHA256"
"SIGNATURE_TYPE_VSTORE",
895
896
897
898
899
900
901
902
903
904
905
906
907
908
909
0209a3e590d5cc6c7cb69b012a59e7 Fd29c857e0782Fcd208a90cc9baa283441
020c4b29£3771bac47 6b4ed836c07 61 fdda30adfaf5d59dbd1£667193cd77d9b
02119a7d8 4b692650607cd256a52d02de8016e972c22d8 6£6703c4ee240c142d
02141b072b5ebe37 £18be2a3658610£353£d3c63b9214472b4fc65588b464c80
```

## Slide 81

##### **Friendly Files: First Generic Bypass**

What will happen if we will replace existing friendly file hash with mimikatz hash?

Friendly Mimikatz :)

## Slide 82


> Recovered by OCR — confidence 86/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
BE Administrator: Windows Powers
PS C:\Users\woody\work>
a
x
BB work
BE Documents # Name % Date modified Type Sie
@ Music Gi wa-pretender 6/20/2023 2:42 AM Application 6,601 KB
B Videos
> @ OneDrive
> MB thispc
> Ge Network
2items |
Search work
Windows Security
e
=
Home
Virus & threat protection
Account protection
Firewall & network protection
App & browser control
Device security
Device performance & health
Family options
Protection history
O Virus & threat protection
Protection for your device against threats.
® Current threats
No current threats.
Last scan: Not available
Quick scan
*@ Virus & threat protection settings
No action needed.
Windows Community videos
a t Virus & th
Have a question?
Who's protecting me?
Help improve Windows Security
Change your privacy settings
View and change privacy settings
for your Windows 11 device.
6/22/2023
```

## Slide 83

**Final Attack Vector: DOS** _“!This program cannot be run in DOS Mode”_


> Recovered by OCR — confidence 78/100 on the text kept, 63/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
] Final Attack Vector: DOS “This program cannot be run in DOS Mode”
I Desitop © 085 2803 (64-bit, windows) - Profile: Untitled - Scenes: Untitled
2) Documents
= Pictures
n
© Onediive - Personal
B30 Objects
2) Documents
= Pictures
Hy Videos
@ Network Scenes
‘items 1 item selected 403 KB
P& Type here to search
Sources
© Display capture
Audio Mixer
Fade
Duration
Controls
Start Streaming
Recording
Start Virtual Camera
Studio Mode
Exit
CPU: 0.3%, 25.00 fps
Search test
```

## Slide 84

##### **Final Attack Vector: DOS**

- The demo was recorded on an older version of Defender

- The latetst version implements few additional checks: The "SIGNATURE_TYPE_TRUSTED_PUBLISHER" (112) To make Defender delete benign drivers and OS executables.

## Slide 85

**Future Work - Possible Local Privilege Escalation**


> Recovered by OCR — confidence 90/100 on the text kept, 52/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
1 Future Work - Possible Local Privilege Escalation
Name
```

## Slide 86

##### **Future Work - Possible Local Privilege Escalation**

- Rule: Filename Similar To Windows File.A

- Checks if a file has the Same name of OS Executable but not in The legit path.

- Only 6 extension are Checked, what about “.SCR”

- Only in system32,syswow64

## Slide 87

##### **Takeaways**

● **Trust no one**

● Using **digitally signed files               totally secure**

● **Signature update process** of security controls is a **new possible attack vector**

## Slide 88

##### **Vendor Response**

Microsoft released a fix on April - **CVE-2023-24934** The fix validates the digital signature of all VDM files

**The fixed version is:** Microsoft Malware Protection Platform version **4.18.2303.8**

## Slide 89

##### **wd-pretender**

https://github.com/SafeBreach-Labs/wd-pretender

## Slide 90

##### **References**

● https://github.com/commial/experiments/tree/master/windowsdefender/VDM

● https://github.com/sztupy/luadec51/

● https://www.crowdstrike.com/blog/evolution-protected-processespart-1-pass-hash-mitigations-windows-81/

## Slide 91

LABS

## Thank you!

Tomer Bar Omer Attias
