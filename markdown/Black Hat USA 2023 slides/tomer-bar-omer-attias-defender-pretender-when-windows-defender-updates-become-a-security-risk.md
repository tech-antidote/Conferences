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
text_chars: 34181
ocr_pages: 38
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:25:29Z"
---
# Defender-Pretender When Windows Defender Updates Become a Security Risk

**Speakers:** Tomer Bar, Omer Attias  
**Conference:** Black Hat USA 2023  
**Source:** `Black Hat USA 2023 slides/Tomer Bar & Omer Attias_Defender-Pretender When Windows Defender Updates Become a Security Risk.pdf` (91 pages)


## Slide 1

LABS

Defender - Pretender When Windows Defender Updates Become a Security Risk

Omer Attias Tomer Bar

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
$:3 SafeBreach'““s
Defender - Pretender
When Windows Defender Updates Become a Security Risk
*
Omer Attias | >
Tomer Bar } ¢@) \N
aa. \ = .on)>
a =.
```

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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
1 mpam-fe.exe Execution
| @ mpamde.exe (8828)
C\Users\POTAT.
. C\Users\petatoh..,
CA\Usere\pctatoh...
a,
-
C:\Program Files (,
C:\Program Files (,
Description: Microsoft Malware Protecti®a Signature Update Stub
Company: Microsoft Corporation
Path: C\Users\POLQIO~1\AppVata\lLocal\ l@gp\CeeCk /10-4//6-491F-2401-Be23] /A2b5eEC\Mpsigstub.ex
Command:  itub 1.1.18500.10 /payload 1,381.2904.0 /program C:\Users\potatohead\ Desktop mpam-fe.exe
User: toystory\potatchead
PID: 8252 Started: = 7/4/2023 7:15:39 AM
Exited: 7/4/2023 7:13:39 AM
```

## Slide 12

**Database Files & mpengine.dll**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
1 Database Files & mpengine.dll
a exe i et else Files eee Ueteries\ foray DELI exe” |
> ThisPC > Local Disk (C:) >» ProgramData » Microsoft >» Windows Defender > Definition Updates >» {53291405-777E-4779-8D90-A058720A4481}
A
Name Date modified Type Size
. [] mpasbase.vdm 7/4/2023 3:31 AM VDM File 73,628 KB
D mpasdita.vdm 7/4/2023 3:31 AM VDM File 7,714 KB
. D mpavbase.vdm 7/4/2023 3:31 AM VDM File 36,861 KB
. [|] mpavdita.vdm 7/4/2023 3:31 AM VDM File 2,568 KB
»
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
] Digital Signature
a —— Digital Signature Details ? x
] General Advanced
) =, Digital Signature Information
pd This digital signature is OK.
Update Payload
Signer information
a, eo, Name: [Microsoft Windows
E-mail: Not availabl
Delta Delta JNotavalabe
Signing time: |Friday, May 12, 2023 2:06:17 PM
{OF View Certificate
Countersignatures
. \ \ Name of signer: E-mail address: Timestamp
mpengine.dlll
Microsoft Time-S... Not available Friday, May 12, 202...
Base Base
Detail
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
l MpSigStub to MsMpEng
Manual reversing reveals RPC_GUID which belongs to mpsvc.dll
RPC func num:42
-Pdata: Q20000075BSB8DA8
-Pdata: @@0000075BSB8DBe
. data: @8@000075BSB8DB1
. data: @80000075BSB8DB2
.Pdata: @8@0000075B888DB
.rdata: 860000075BSBR8DB4
-Pdata: #800800 75BSB8DB8
-Pdata: @@0000075BSB8DBA
.Pdata: @80080075BSB8DBC
.Pdata: @8@000075BSB8DED
. data: @@@000075BSB8DBE
. data: @8@0000075BSB8DBF
.Pdata: #808800 75BS88DC8
_Pdata: @80000075BSB8DC1
.rdata: 808800 75B8B8DC2
.Pdata: @@eeeee75BSB8DC3
rdata: ABAAABATSRRRRM A
\ db 39h ]
dq offset unk_75BSBA1De
_rpd guid db 6h ; ~
db 8
db 8
tr Ls
(46 @C5O3F532h [ sec 503#532-4438-4c69-83002CEIBGESERS) (2.0) -- C:\Program Files\Windows Defender \mpsvc.dll
dw 443Ah @ -> servertipenabiereature
1- yerMpDisableFeature
cer ACOs = 2- lpQueryStatus
mt — sf 3- ventOpen
db @cch ; i
db @Dih ; Nl 41 -> ServerMpQueryEngineVersion
db @FBh ; ii { 42 -> ServerMpUpdateEngineSignature J
db @DBh ; U
db 38h ; 3 /
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

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
OxA0
OxBO
Oxco
OxDO
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
gics
c102
FEEE
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
ooo1
FFIA
DD30
0600
J1IFA
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
D41aA
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
4BD3
FREE
0500
0030
2a89
ADSE
oso9
2702
siebe:
780F
8701
BFO2
ECc1A
OOFF
g0o1
BOLF
34E6
cog93
767A
2DD8
S425
2FCD
6706
OAOB
0000
0000
0000
0000
0000
5c04
FFO6
OOFF
0003
3CF7
FFFF
0400
85FA
5306
173c
0016
ocoD
280A
SD54
TA1O
8F04
CFO6
pool
8000
ras)
ooo1
0280
6C7A
FEE
0500
oo16
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
OOEA
SF6E5
0300
7BFA
0100
oocF
oool1
SF78
012345978 9ABCDEF
)..-@..
gt6.1..
~$..€..
—-. ee. Fe
E---s "
--\¥¥--
y.-.-.-yy-€..
-vy-€..°°
‘EYO....4e<
A.... JOA’ y¥lz.
yyqu..yyvz.-.yy{u
--¥Y¥Ez..-G.a....
FS€+R..0”,8....1
€.$.6.*&/I.<§...
X8to.-“g......_x
Zlib
Compressed
Defender
Signatures
```

## Slide 37

Signature Structure

## Slide 38

**Signature Structure**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
1 Signature Structure
bitfield SigqnatureHeader {
Type: 3;
Size: 24:
fi
struct Signature {
SignatureHeader header;
ud Datal header. Size};
ti
```

## Slide 39

**Signature Types**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
1 Signature Types
“SIGNATURE_TYPE_RESERVED",
"SIGNATURE_TYPE_VOLATILE_THREAT_INFO",
"“SIGNATURE_TYPE_VOLATILE_THREAT_ID",
"SIGNATURE_TYPE_CKOLDREC",
"SIGNATURE_TYPE_KVIR32",
"SIGNATURE_TYPE_POLYVIR32",
"SIGNATURE_TYPE_NSCRIPT_NORMAL",
"SIGNATURE_TYPE_NSCRIPT_SP",
"SIGNATURE_TYPE_NSCRIPT_BRUTE",
"SIGNATURE_TYPE_NSCRIPT_CURE",
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
“SIGNATURE_TYPE_RPFROUTINE",
"“SIGNATURE_TYPE_NID",
"“SIGNATURE_TYPE_GENSFX",
"SIGNATURE_TYPE_UNPLIB",
"SIGNATURE_TYPE_DEFAULTS",
"SIGNATURE_TYPE_DBVAR",
Ox5C: "SIGNATURE_TYPE_THREAT_BEGIN",
"“SIGNATURE_TYPE_THREAT_END",
"SIGNATURE_TYPE_FILENAME",
"SIGNATURE_TYPE_FILEPATH",
"SIGNATURE_TYPE_FOLDERNAME" ,
"SIGNATURE_TYPE_PEHSTR",
"SIGNATURE_TYPE_LOCALHASH",
"SIGNATURE_TYPE_REGKEY",
1100:
103:
105:
106:
“SIGNATURE_TYPE_HOSTSENTRY",
"SIGNATURE_TYPE_STATIC",
"SIGNATURE_TYPE_LATENT_THREAT",
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
"SIGNATURE_TYPE_FOP",
SIGNATURE_TYPE_KCRCE",
SIGNATURE_TYPE_VFILE",
SIGNATURE_TYPE_SIGFLAGS",
SIGNATURE_TYPE_PEHSTR_EXT2",
: "SIGNATURE_TYPE_PEMAIN LOCATOR",
: "SIGNATURE_TYPE_PESTATIC",
"SIGNATURE_TYPE_UFSP_DISABLE",
“SIGNATURE_TYPE_FOPEX",
"SIGNATURE_TYPE_PEPCODE",
"SIGNATURE_TYPE_IL_PATTERN",
"SIGNATURE_TYPE_ELFHSTR_EXT",
: "SIGNATURE_TYPE_MACHOHSTR_EXT",
: "SIGNATURE_TYPE_DOSHSTR_EXT",
"SIGNATURE_TYPE_MACROHSTR_EXT",
: "SIGNATURE_TYPE_TARGET_SCRIPT_PCODE",
: "SIGNATURE_TYPE_VDLL_IA64",
“SIGNATURE_TYPE_PEBMPAT",
"SIGNATURE_TYPE_AAGGREGATOR" ,
"SIGNATURE_TYPE_SAMPLE_REQUEST_BY_NAME"
2 "SIGNATURE_TYPE_REMOVAL_POLICY_BY_NAME"
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
176:
tee
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
*SIGNATURE_TYPE_TUNNEL_X66",
"SIGNATURE_TYPE_TUNNEL_X64",
"SIGNATURE_TYPE_TUNNEL_IA64",
"SIGNATURE_TYPE_VDLL_ARM",
"“SIGNATURE_TYPE_THREAD_X86",
"SIGNATURE_TYPE_THREAD_X64",
"SIGNATURE_TYPE_THREAD_IA64",
"SIGNATURE_TYPE_FRIENDLYFILE_SHA2S6
"SIGNATURE_TYPE_FRIENDLYFILE_SHAS12
"SIGNATURE_TYPE_SHARED_THREAT",
"SIGNATURE_TYPE_VDM_METADATA",
"SIGNATURE_TYPE_VSTORE",
"SIGNATURE_TYPE_VDLL_SYMINFO",
"SIGNATURE_TYPE_IL2_PATTERN",
"SIGNATURE_TYPE_BM_STATIC",
"SIGNATURE_TYPE_BM_INFO",
"SIGNATURE_TYPE_NDAT",
"SIGNATURE_TYPE_FASTPATH_DATA",
"SIGNATURE_TYPE_FASTPATH_SDN",
"SIGNATURE_TYPE_DATABASE_CERT",
"SIGNATURE_TYPE_SOURCE_INFO",
"SIGNATURE_TYPE_HIDDEN_FILE",
"SIGNATURE_TYPE_COMMON_CODE",
"SIGNATURE_TYPE_VREG",
"SIGNATURE_TYPE_NISBLOB",
"“SIGNATURE_TYPE_VFILEEX",
"SIGNATURE_TYPE_SIGTREE_BM",
"SIGNATURE_TYPE_VBFOP",
"SIGNATURE_TYPE_VDLL_META",
"SIGNATURE_TYPE_TUNNEL_ARM",
"SIGNATURE_TYPE_THREAD_ARM",
"SIGNATURE_TYPE_PCODEVALIDATOR",
"SIGNATURE_TYPE_MSILFOP",
"SIGNATURE_TYPE_KPAT",
"SIGNATURE_TYPE_KPATEX",
"SIGNATURE_TYPE_LUASTANDALONE",
"SIGNATURE_TYPE_DEXHSTR_EXT",
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
“SIGNATURE_TYPE_DEXHSTR_EXT",
"SIGNATURE_TYPE_JAVAHSTR_EXT",
"SIGNATURE_TYPE_MAGICCODE",
"SIGNATURE_TYPE_CLEANSTORE_RULE",
"SIGNATURE_TYPE_VDLL_CHECKSUM",
"SIGNATURE_TYPE_THREAT_UPDATE_STATUS",
"SIGNATURE_TYPE_VDLL_MSIL",
"SIGNATURE_TYPE_ARHSTR_EXT",
"SIGNATURE_TYPE_MSILFOPEX",
"SIGNATURE_TYPE_VBFOPEX",
"SIGNATURE_TYPE_FOP64",
"SIGNATURE_TYPE_FOPEX64",
"SIGNATURE_TYPE_JSINIT",
"SIGNATURE_TYPE_PESTATICEX",
"SIGNATURE_TYPE_KCRCEX",
"SIGNATURE_TYPE_FTRIE_POS",
"SIGNATURE_TYPE_NID64",
"SIGNATURE_TYPE_MACRO_PCODE64",
"SIGNATURE_TYPE_BRUTE",
"SIGNATURE_TYPE_SWFHSTR_EXT",
"SIGNATURE_TYPE_REWSIGS",
"SIGNATURE_TYPE_AUTOITHSTR_EXT",
"SIGNATURE_TYPE_INNOHSTR_EXT",
"SIGNATURE_TYPE_ROOTCERTSTORE",
"SIGNATURE_TYPE_EXPLICITRESOURCE",
"SIGNATURE_TYPE_CMDHSTR_EXT",
"SIGNATURE_TYPE_FASTPATH_TDN",
"SIGNATURE_TYPE_EXPLICITRESOURCEHASH",
"SIGNATURE_TYPE_FASTPATH_SDN_EX",
"SIGNATURE_TYPE_BLOOM_FILTER",
"“SIGNATURE_TYPE_RESEARCH_TAG",
"SIGNATURE_TYPE_ENVELOPE",
"“SIGNATURE_TYPE_REMOVAL_POLICY64",
“SIGNATURE_TYPE_REMOVAL_POLICY64_BY_NAME",
"“SIGNATURE_TYPE_VDLL_META_X64",
"SIGNATURE_TYPE_VDLL_META_ARM",
"SIGNATURE_TYPE_VDLL_META_MSIL",
"SIGNATURE_TYPE_MDBHSTR_EXT",
"SIGNATURE_TYPE_SNIDEX",
"SIGNATURE_TYPE_SNIDEX2",
"SIGNATURE_TYPE_AAGGREGATOREX",
“SIGNATURE_TYPE_PUA_APPMAP",
"SIGNATURE_TYPE_PROPERTY_BAG",
"SIGNATURE_TYPE_DMGHSTR_EXT",
"SIGNATURE_TYPE_DATABASE_CATALOG",
```

## Slide 40

##### **Threat Begin & Threat End**

Begin

**End**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Threat Begin & Threat End
Begin
iA
WA
9C: "STGNATURE_TYPE_THREAT_BEGIN"
Name
5D: "SIGNATURE_TYPE_THREAT_END",
Size Type
OxO1D1 Threat
oxeo22 ThreatBegin
axQ1A7 [ ]
axgage Threatend
End
5C
1E
F421 41
o4 40
30
30
30
30
72
él
65
44
73
2E
63
65
m3)
79
63
6E
1B
20
oD
te
30
g6
8g
#4
fe
?4
6C
2E
6g
61
78
65
a
Fz
6F
6C
ok
25
64
BS
Ec
cE
G4
45
oF
6
6E
6g
che
ck
40
OB
gs
g2
03
24
WE
lAconki, .@  $
le)
OB
Og
2E
65
641
61
che
fo
65
#3
66
65
73
63
BE
AF
23
FA
6B
63
oh
6F
65
OF
che
#4
6F
a
che
25
64
as
Bo
24
Ba
20
83
Ag
20
6g
6F
6E
fe
4
30
6E
641
#3
65
aa
67
8B
a3
6E
6E
di
74
che
69
26
25
30
f2
aa
3F
3D
ac
16
74
BE
Bu
4F
4E
63
#4
41
69
aa
61
64
#3
25
65
53
Ss)
25
EC
Ad
96
co
G41 a3
EB 36
22 61
65
65
2E
69
69
4c
ch
gc 53
6C
69
26
75
5c
68
49
65
él
fd
25
At
6F
4d
#5
AF Chl
plo)
GheeiE
co]
6E
66
OB
65
#2
6c
6g
73
4c
af
30
Bo
Ba
20
6B
By) 50 a4
5c
34
2
61
#4
oh
65
65
41
63
éF
65
61
25
69
45
25
67
63
40
cE
O41
ac
#4
#3
4c
fi)
#3
f2
6c
#3
66
f2
fi)
16
42
BE
16
23
O41
53
16
2F
F4
69
fe
#4
63
65
oh
65
6F
26
a3
56
30
45
7a
64
79
66
65
75
61
72
73
74
4E
a?
EF
29
06
_ fe :
a
Ei. Ne
revi Ge
E, aconti.net/di
Bler... ALifestyl
E.aconti... Alife
Dialer... SecureD
haler... goodthin
x... dialer/stubl
Jexe.  &dialerhas
hwert=4sedialery
Prsion=*u%s%s
Boftware\aLifest
Wle\... ShowEroki
ts TUT Du ahr
PeseCountr ys
ndcode=*u..g
ny’ B
```

## Slide 41

**Evaluation**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
] Evaluation
try:
while True:
Signature.read_one(base_data)
counter += 1
except Exception:
print(f'Total Signatures: {counter}' )
thon .\CountSignatures. py
py : \
Total Signatures: 2643614
```

## Slide 42

**Threat Begin Signature**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
] Threat Begin Signature
sEruce ThreatBegin {
Signaturedeader header;
u32 Id:
yié Unknown;
ui6 Counter;
wié Cakegory;
| ue Name[ Threathamelength ];
Troy T Tey
ui6 Resources| Counter];
ua Seviri by;
us Action;
ué Unknowns[4];
4;
SC HESEESEEE 4S FE EE BE EE Bo OB Ge 8 Oe
F4 21 41 65 6F 6E f4 69 fe Oo OS 46 85 82 24 oo
4 HO 40 45 80 GO O4 8H O21 63 FO OF GO Bo ob 24
30 GO GH Ob BO Go Ob Be Ob Bo Be oe Bo oe oe 6
```

## Slide 43

**Smart modification on Conti Signature**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
] Smart modification on Conti Signature
#include <stdlib.h>
wchar_t* = L"aconti NetService";
“port.aconti.net/dialer";
"ALifestyle.aconti";
"ALifeDialer”;
"SecureDialer";
“goodthinxx" ;
“dialer/stub.exe";
“dialerhashwert=%s&dialerversion=%u%s%s" ;
"Software\\ALifestyle\\";
"ShowErotic";
"*s 2UID=%u&Nr=%s&Country=%s&indcode=%u" ;
t main()
0063
0074
0001
6E6S
6665S
0B41
6S63
6Fr64
722E
«dies @aeie s PO
rt.aconti.net/di
aler...ALifestyl
e.aconti...ALife
Dialer...SecureD
SaLOL sos thin
xx...dialer/stub
-exe..&dialerhas
hwert=tsédialerv
ersion=tutsts...
Software\ALifest
yle\...ShowEroti
c..%%¢s?UID=tuéNr
```

## Slide 44

**Smart modification on Conti Signature**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
1 Modify Conti Threat Name - Update failed
0405 0607 0809 0B OCOD OEO 0123456789A;CDEF
0 4506 0000 0000 0100 OBO0O0 0800
6F6E 7469 000
0000 0000 0000 0000
FA83 7200 0000 0000 0000 00
0 3006 0 6BA2 924F EB36 ODO0O0 0000 00
0 3000 0 59D2 FEOO 0000 0061 0c01 000
Product name: Microsoft Windows Defend: [iggiiiiemamsellisnesedisnRaiethellted lala piediaenieiiae
Package files: M soo pe rai paar’ ae PA sob
0072 0069 0063 0065 0016
Directory: C:\Defs OxAO 7274 636F 6E74 692E 742F
mpasbase.vdm: b96f6f2ceasb43dtdal54dda/ds3b399/U1EbYbU 1d? lat /524dbb/ /db/44us1be
mpasdlta.vdm: 8bc3lebf7357/bdb5a@57924eb826c5fd212d968F561ac6/17cd47ebb6c2aQbb/o
mpavbase.vdm: 66a/af38e/cbcl@taatbbtc22e4e629b66 3ebad0/ddt93ed490dae8c 952776182
mpavdlta.vdm: 8d15055ae3335aadaddf/b/b@6fasS5edc509fd3e63ec8/cfb39a/10134b082cc
MoSioStub exe: fad?b9b847/54e2e8368e8929F ab4Sbes6dbd/26/817/6ee/5814d2al6d23e5c26
ERROR @x8@5@a904) : MpUpdateEngine(C: \Defs)
ERROR @x8@5@a904) : MpUpdateEngine(C: \Defs)
ERROR @x6@59a004): Failed to update signatures from C:\Defs
PRePE- RR
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
|) RMDX & Zlib Headers Tear he ——
u32 Signature;
B u3s2 Timestamp;
s2 40 44 56 16 AE FF 64
G0 80 Ge Oo Oe ao oo oo FBC ae Be oo u32 Unknownd ;
f0 88 88 88 88 Bo oo Be u32 Options;
FF FF FF FF @@ aa oo oo u32 Unknowne ;
u32 Unknowns;
u3s2 Dakadtfset;
Use DecompressedDataSi ze;
26 01 88 88 29 C6 B2 HH 4
o5 EY @3 80 5B @2@ 8o 8h 5
61 05 G8 OO 67 6E FO Ob
#3 G1 860 86 74 G1 GO Ob 76
FE 67 SC 80 6H BS 8D 8H aC
BF O2 G8 8H 96 83 8H 8S AG
Ba 2 ae a
HH 6D OL OO OO mgt... ie
```

## Slide 49

##### **RMDX & Zlib Headers**

**Zlib Data Header**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
| RMDxX & Zlib Headers
S52 40 44539 16 SE 7F 64 FF FF FF FF @2 fo 28 80 PMDX.. od
HO OF FO OC pretties GE EH HO GA 61 56 8b
______ Zlib DataHeader BP EE
struct CDATA_Header {0000000 Jue
ui? CompressedDataLength; cede @ AL,
use CROSZ Freee eee Se
us CompressedData[CompressedDataLength]; |: a Ve pe
94 14 49
45 AG 62 235 AE
```

## Slide 50

**CRC32 Algorithm**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
) CRC32 Algorithm
Algorithm
CRC- 32
CRC-32/B2Z1P2
CRC-32/ JAMCRC
CRC-32/MPEG-2
CRC-32/POSIX
CRC-32/SATA
Result
@xESB9O2BDF
@xB4E SAGAS
@x1A46D4208
@x4B1CSFS?7
@x9B769BC8
Ox4COSBbas
Check
@xCBF43926
@xFC891918
@x340BC6D9
@xO376E6E7
@x765E7688
OxCF72AFES
Poly
Oxe@4C11DB7
Oxe@4C11DB7
Ox84C11DB7
6xB4C11DB7
Ox84C11DB7
8x84C11DB7
Init
@xFFFFFFFF
@xFFFFFFFF
OxFFFFFFFF
OxFFFFFFFF
BxeeeReeee
8x52325032
```

## Slide 51

##### **Trying One More Update Attempt**

VDM File

New
Raw Signatures
VDM File

## Slide 52

**Trying One More Update Attempt**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
] What's The Delta Format?
bitfield SignatureHeader {
Type: 8;
Size: 24
bi
struct Signature {
SignatureHeader header;
u8 Datal header. Size];
```

## Slide 58

##### **BLOB_RECINFO & BLOB**

###### **BLOB_RECINFO**

**BLOB**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
|) BLOB_RECINFO & BLOB
74
61
aa
SF
BE
D?
pg
80
FF
FF
ac
ca
4
4B
i4
4eE
i4
4h)
a6
42
15
ad
FF
a8
ag
oF
FS
ED
D1
EC
FF
p2
as
Fa
a4
Fz
BLOB_RECINFO
18
AL
78
a7
Ag
CE
E?
a1
FF
13
O35
44
13
1A
12
ie
a3
26
aC
FA
ac
BS
Aa
bc
O41
18
be
CF
a6
O41
as
FS
FF
a1
1F
73
11
6
aa
D4 WS
FF 6
[Gc] FF
O3
a3
af 66
sO 2B
6F FQ
bitfield SignatureHeader
Type
Size
=
struck Signature {
SignatureHeader header
uS Dakal header. Size)
Signature blob recinfo @€
Signature blob @¢
```

## Slide 59

**BLOB Structure**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
1 BLOB Structure
struck Blob {
SignatureHeader header;
u32 Unknown:
u32 Unknown:
We Da
D7 oe /
EY
9 42 9F EC) at
30
FF 15
ad
FF FF
ac a8
co ag
HZ
AS
FS FS
ED te
D1 Fe
FF
AA
De
C2
HB
a5
a4
ad
FF
a2
a
AG
AG
BA
69
FF
FF
a4
58
38
24
10
oF
FF
1F
g5
29 10
ab De
FE CF
BO 86
BD it
45 Fa
BA
Dig
3
FF
ag O41
BS iF
Fa 73
a4
fQ 11
cF 8a
FF
BS
oF
oD
OF
6
FF
a3
66
2B
FQ
```

## Slide 60

**Actions**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
1 Actions
struck Blob {
SignatureHeader header;
u32 Unknown:
(us Datal header, Size - 8];
th
DF oe EF Bd 73
AA
De
C2
HB
20
a5
a4
BA
69
24
29
ra
FE
aD
BD
Ds
45
1
Di
cr
G6
BA
BS
Fo
BA
Lig
3
DO 42 9F EC jai at FF
ae FF FF GB ad
FF 15 HZ FF FF 1A
AL HS 15 BE BOD 35
FF FF FS Fa 3 ay Fa
BC 8G ED o4 15 11
co 9 D1 Fe 44 86 AL
FF
50
a3
FA
a9
20
a1
FF
a2
a
AG
AG
FF
FF
a4
58
38
10
oF
FF
1F
g5
BE
BS
Fel
ad
fa)
CF
FF
ad
1F
73
11
a0)
FF
BS
oF
oD
OF
Bb
FF
a3
66
2B
FQ
```

## Slide 61

##### **Reverse ConsumeInputCompress**

MSB Check

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
1 Reverse ConsumelnputCompress
Lal cea |S
MSB Check
```

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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
1 Diffing Base and Merge
oo
BD
3F
a?
oo
a3
41E
Bc
44
a1
E3
67
18
45
2F
61
oo
09 00
31 BS
54 58
OA BE
45 1c
oo 20
FS 77
67 16
20
38
16
87
B6
48
34
oo
a4
6c
D6
5B
as
oo
06
67
3c
84
bg
oo
02
Fg
DD
72
AS
oo
ES)
67
58
2D
70
30
oo
oo
iF
35
33
E3
20
a?
16
Ba
55 OD 26|B6
94
61
oo
oo
OF
D1
FQ
OF
20
1D
16
58
BB
21
SA
oo
16
Eo =
B2
23 Q
48 g
oo 2
oo ..]
33 g
DF <
19 g
38) | 8.
20 0
3B cl.[g
16
90
B? frog
4D i.wadr.4
44 ..q Zz
68 1G
oo R.1
BS Txg
74 31%. . XX
ED g...E.-.8
ic pl
20 - wOZQ
75 9-9
eiltp BA
GY
6M
2.74
vf-7°
,
E
jo1. 82Q
g...E
?R, NSU
70
B2
5B
43
68
98
4
8c
D6
5B
os
68
06
iF
35
33
E3
20
a7
16
68
2D
c4
23
tol)
6F
tol)
E9
67
82
bg
cg
c?
08
61
EE
ce
88
B1
68
77
67
47
S2
68
6c
68
04
cD
thi
6D
Ao
After
Ec
16
18
AE
as
tcl)
03
59
39
SE
8D
tcl)
E3
67
18
AS
2F
61
ao
99
34
54
A
45
ao
F8
67
3B
16
FO
tol)
tol)
Cc?
SE
73
53
20
38
16
87
B6
A8
34
a0
ao
BS
58
B6
ic
20
77
16
16
BC
AA
EG
tol)
B4
67
tol)
55
54
og
ao
02
F9
DD
72
aS
ao
E9
67
58
2D
78
30
ao
07
83
2B
EF
20
co
16
70
B4
73
81
ao
ao
oF
D1
F9
OF
20
1D
16
58
BB
24
SA
ao
ao
07
68
Merge
EG
B2
23
48
ao
ao
33
OF
87
9A
20
7E
16
Ba
Bg
CF
76
ao
tcl)
6F
DE
ED
3F
20
Eg
1.929
gE.-
q~9
R. . N9u#omS;
dg
Data Size:
OxGACEEF LL
Region: @xG@GG00000 - BxBACEEV11 (@ - 1613531729)
(OxACEE711 | 172.93 MiB)
Baka
ize: fy fsFACEic
Region: OxQ@0800008 - BxOAF6CE1C (@ - 183946780)
(QxAF6CELC | 175.43 MiB}
```

## Slide 71

**Eureka - Unknown Numbers**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
] Eureka - Unknown Numbers
struck Blob { struck Blob {
Sionaturedeader header: Signatureheader header;
us2 Unknown ; u3s2 Mergesize;
u32 Unknown; u32 Mergeckca2;
Bader, Size - 6]; Te tata resters size - 6];
+ 1
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
] Can We Fake an Update?
Ce
,¢
```

## Slide 75

##### **We Did It !!!**

Updated to: 1.383.1800

Version Before

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
3 powershell (running as TOYSTORY\weak)
PS C:\Users\weak\work> .
© new » TL Sort v
View »
€ > ¥ 4 BEX Users > weak > work > Defs - ¢
Name Date modified Type Size
Y We Quick access
IEF MpSigstub 1/91/2023 6:17 AM Application 785 KB
I Desktop *
Downloads #
| \Oserss 9
Pictures *
@ Music *
h BB Videos *
BE work
Be work
& OneDrive
This Pc
a DVD Drive (03) CCC
Ge Network
litem | (=
es 3:28AM
o8 fF ® mC = @ rpepas ©
```

## Slide 80

##### **Friendly Files**

##### 30,000 friendly hashes

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
|) Friendly Files
30,000 friendly hashes
*"SIGNATURE_TYPE_VDLL_ARM",
"SIGNATURE_TYPE_THREAD_X86",
"SIGNATURE_TYPE_THREAD_X64",
# A p oF
“SIGNATURE_TYP
“SIGNATURE _TYP
_SHA256"
SHAS12"
AREL
"SIGNATURE_TYPE_VDM_METADATA",
"SIGNATURE_TYPE_VSTORE",
"SIGNATURE_TYPE_VOLL_SYMINFO",
"“SIGNATURE_TYPE_IL2_PATTERN",
"SIGNATURE_TYPE_BM_STATIC",
"SIGNATURE TYPE_BM_INFO",
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
0209cfEc2d£2d39dfa9106fa00 Fb6d221dbd450dc6161cc2a7138c46a293add7
0209£490cb£e60c61b651023e1d£9327e5350cd0a8be126907cdbaa6b564ceeb
020a4cbaebdb1lbbbdfdf141cfbb16£165457535b5a4612f fdbb33bc647 43bbe3
020b7b54£1704c10dcSac9b91b£037486£7b88cc21ce55b7 66a8 9ee505a5cde7
020c4b29£3771bac47 6b4ed836c07 61 fdda30adfaf5d59dbd1£667193cd77d9b
020cefa6c036894f912c69eef981lefef7d3£fb6a89000efac4888ddd00c255a8
020dc950741800877ab9ddb69e566897ed3077c4bc181cf£607cdd4 9db£23419d
020e5eb54040628846c4bfd816b71d8c0694b2b6c94883001la2da3dcfc251346
02102b£3d33£117a295093e4af7 2baelb6abbe35e3e4255b65ef24Ff1108c017d
02106197££396ba5c03d528bc6e245d0de25c745237ab37bc5d6a9a913c57e52
0210bd8d5d5a63e1b8 fa97 Sabaf2e33486f8bc6c8c23d6el f5c7£2b9460b023b
02110£602638980ea83de49£575bcaa4e94508043664676c8090£0a7e230C277
021129a2a3446af44a296c2a50£d5023db6el 6b489719992bc7c7ce078cebde2
02119a7d8 4b692650607cd256a52d02de8016e972c22d8 6£6703c4ee240c142d
910 (0212a89972e6e11d056323£cf7 664a226dd2 6bce575eaa02c0b17dc5d4dc2cb3
ao
O12
hls)
0213705992cd08a07c57690ce28e6c7ee930d6a7 6ddc45d841d£4326b04fbcc3
02141b072b5ebe37 £18be2a3658610£353£d3c63b9214472b4fc65588b464c80
02142531a7ae99a5509c79e1c639e34d052 fb39e77e0c9dbae65c8FF6lef7e19
```

## Slide 81

##### **Friendly Files: First Generic Bypass**

What will happen if we will replace existing friendly file hash with mimikatz hash?

Friendly Mimikatz :)

## Slide 82

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
BE Administrator: Windows Powers
PS C:\Users\woody\work>
yw
a
x
BB work
© new ~ WN sony Ea
€ > v B®  BB> ThisPC > Local Disk (C:) > Users >» woody > work » ¢
BE Documents # Name % Date modified Type Sie
Brictures ¢ — BDe 6/22/2023 330 AM File folder
@ Music Gi wa-pretender 6/20/2023 2:42 AM Application 6,601 KB
B Videos
> @ OneDrive
> MB thispc
DVD Drive (0) C.
> Ge Network
2items |
Search work
Windows Security
e
ob OD
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
ACOH cme
6/22/2023
```

## Slide 83

**Final Attack Vector: DOS** _“!This program cannot be run in DOS Mode”_

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
] Final Attack Vector: DOS “This program cannot be run in DOS Mode”
7and_71 > 71delall pe
« 4 [] > ThisPC > 05(C) > playground > windowDetenderUpdate > (3FIFBFSC-TBEA-4F08-925C-185981E14249) > try update to
tome Date modified pe
HF Quick access
EE mpavaitavdm
I Desitop © 085 2803 (64-bit, windows) - Profile: Untitled - Scenes: Untitled
$ Downloads Fen Ea
2) Documents
= Pictures
n
‘tyupdate to 321.70_and_71
By Videos
windowDefenderUpdate
© Onediive - Personal
tis Pc
B30 Objects
[i Desktop
2) Documents
¥ Downloads
Music
= Pictures
Hy Videos
aS © Display Capture
se £5 (\\ 192.168.2259) (R)
@ Network Scenes
‘items 1 item selected 403 KB
P& Type here to search
Properties  [EJrilters Display
Sources
© Display capture
Audio Mixer
oa
Scene Transit...
Fade
Duration
Controls
Start Streaming
Recording
Start Virtual Camera
Studio Mode
settings
Exit
CPU: 0.3%, 25.00 fps
Search test
e
```

## Slide 84

##### **Final Attack Vector: DOS**

- The demo was recorded on an older version of Defender

- The latetst version implements few additional checks: The "SIGNATURE_TYPE_TRUSTED_PUBLISHER" (112) To make Defender delete benign drivers and OS executables.

## Slide 85

**Future Work - Possible Local Privilege Escalation**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
1 Future Work - Possible Local Privilege Escalation
Name
Lt SIGNATURE_TYPE_LUASTANDALONE_!#_ AutoitExecFile.tet
(aa SIGNATURE_TYPE_LUASTANDALONE_!#_Lua-AttachmentContainerExt.tet
Lt SIGNATURE_TYPE_LUASTANDALONE_!#_Lua-ContextFromSharepoint.tet
Lt SIGNATURE_TYPE_LUASTANDALONE_!*_Lua-ContextFromWebmail.tet
Lt SIGNATURE_TYPE_LUASTANDALONE_!*_Lua-ContextFromWordPress.tet
Lt SIGNATURE_TYPE_LUASTANDALONE_!#_Lua-ContextualDropFileByEmailClient.Includes.GetEmail...
fat SIGNATURE_TYPE_LUASTANDALONE_!#_Lua-ContextualDropFileByEmailClientTag.Includes.Get...
Lay SIGNATURE_TYPE_LUASTANDALONE_!#_Lua-FilelnBasePathAttributes.A.txt
(a SIGNATURE_TYPE_LUASTANDALONE_!#_Lua-FromSkype Transfer.txt
yt SIGNATURE_TYPE_LUASTANDALONE_!*_Lua-InnoSetupClassifier.tet
(a SIGNATURE_TYPE_LUASTANDALONE_!*_Lua-ISOExt.tet
Lt SIGNATURE_TYPE_LUASTANDALONE_!*_Lua-LnkExt.tet
yt SIGNATURE_TYPE_LUASTANDALONE_!#_Lua-NSIS_Installer.txt
ay SIGNATURE_TYPE_LUASTANDALONE_!*_Lua-SuspiciousStringinURL.txt
Ly SIGNATURE_TYPE_LUASTANDALONE_!#_OLEHasJar.ObMp<ttributes.cUVsi6a" Ub. tet
(a SIGNATURE_TYPE_LUASTANDALONE_!#_SuspiciousKEYGENfilename.ObMpaAttributes.cUV4i0, da...
Ly SIGNATURE_TYPE_LUASTANDALONE_!#_ SuspiciousNFOfilename.ObMpAttributes,j.tet
(ay SIGNATURE_TYPE_LUASTANDALONE_!#_Lua-Win32_Prifoulvbs.tet
ay SIGNATURE_TYPE_LUASTANDALONE_!*_Lua-Worm-JS_Bondat.Allnk.txt
fat SIGNATURE_TYPE_LUASTANDALONE_!#000000_First_OfficeFrame.txt
(ay SIGNATURE_TYPE_LUASTANDALONE_!#000010_First_FrarmeNumeralParam.txt
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
] wd-pretender C)
| Ld
OF At
ve
(a) 9:
https://github.com/SafeBreach-Labs/wd-pretender
```

## Slide 90

##### **References**

● https://github.com/commial/experiments/tree/master/windowsdefender/VDM

● https://github.com/sztupy/luadec51/

● https://www.crowdstrike.com/blog/evolution-protected-processespart-1-pass-hash-mitigations-windows-81/

## Slide 91

LABS

## Thank you!

Tomer Bar Omer Attias

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
$33 SafeBreachLABs
Thank you!
Tomer Bar
Omer Attias
```
