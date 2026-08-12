---
title: "Tales of a RCE in a video game"
speakers: ["Thomas Dubier"]
conference: "Hexacon"
conference_full: "Hexacon 2024"
edition: ""
year: 2024
source_pdf: "Hexacon 2024 Slides/Thomas Dubier_Tales of a RCE in a video game_Compressed.pdf"
pages: 66
sha256: "efd926f8f1bfe29c4ee34f235b28d0e5735babdfd407e0c79a54733e91055fcc"
text_chars: 20184
ocr_pages: 5
has_ocr: true
redacted_secrets: 0
ocr_confidence: 86.4
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T05:53:35Z"
---
# Tales of a RCE in a video game

**Speakers:** Thomas Dubier  
**Conference:** Hexacon 2024  
**Source:** `Hexacon 2024 Slides/Thomas Dubier_Tales of a RCE in a video game_Compressed.pdf` (66 pages)


## Slide 1

1

**Tale of an RCE in a video game Neverwinter Nights**

**04/10/2024**

**HEXACON 2024**

## Slide 2

## **<u>Agenda</u>**

2

- Introduction

- Concepts

- Old games old bugs

- Neverwinter Nights

- Attack Surface

- Vulnerabilities

- Exploitation

- Conclusion

**2**

HEXACON 2024

## Slide 3

## **<u>whoami</u>**

 Thomas DUBIER @Tomtombinary  Security researcher @Synacktiv  In the Reverse Engineering team

- Synacktiv

 Offensive security company  Based in France

 ~170 Ninjas

 We are hiring !

3

**3**

HEXACON 2024

## Slide 4

## **<u>Research motivations</u>**

4

- **Why look for vulnerabilities in old video games ?**

   - ~~Bug bounty~~

   - To have fun

   - To recycle my old video game collections

   - Interesting when old games are rereleased

   - There are always bugs, but sometimes complicated to exploit

   - Training

 **Focus on RCE (no cheating technique)**

**4**

HEXACON 2024

## Slide 5

5

# **<u>Concepts</u>**

**5**

HEXACON 2024

## Slide 6

## **What is video game ?**

6

Process Input Update Game Render

**6**

HEXACON 2024

## Slide 7

## **What is game engine ?**

7

Gameplay Foundations (Event Bus, Script Engine …) Physics & Human Interface Rendering Multiplayer Audio Collision Devices (HID) Ressources / Game Assets Core Systems ( Memory Allocation, Math, Asynchronous File I/O, ….) 3rd Party SDK (DirectX, Havok, …) _Source: https://www.gameenginebook.com/ « Game Engine Architecture » by Jason Gregory_

**7**

HEXACON 2024

## Slide 8

## **Where to focus ?**

8

Gameplay Foundations (Event Bus, Script Engine …)
Physics &  Human Interface
Rendering Multiplayer Audio
Collision Devices (HID)
Ressources / Game Assets
Core Systems ( Memory Allocation, Math, Asynchronous File I/O, ….)
3rd Party SDK (DirectX, Havok, …)

**8**

HEXACON 2024

## Slide 9

9

# **<u>Old games old bugs</u>**

**9**

HEXACON 2024

## Slide 10

## **Stack buffer overflow**

10

\```
void __thiscall sub_404160(comm_t *this)
{
  [...]
char buf[0x800]; // [esp+34h] [ebp-800h] BYREF
\```

\```
  [...]
while ( 1 )
  {
    bytes_recv = recvfrom(this->sockfd, ::buf, 0x8000, 0, &from, &fromlen);
if ( bytes_recv == -1 )
break;
if ( bytes_recv <= 0 )
goto LABEL_6;
    qmemcpy(buf, ::buf, bytes_recv);
\```

**10**

HEXACON 2024

## Slide 11

## **Stack buffer overflow**

11

\```
int __thiscall sub_4DC120(_DWORD *this)
{
constchar *SessionName; // eax
int NumberOfPlayer; // [esp-8h] [ebp-9Ch]
int NumberMax; // [esp-4h] [ebp-98h]
char GameName[122]; // [esp+8h] [ebp-8Ch] BYREF
  [...]
  NumberMax = Array_GetNumberMax(v9);
  NumberOfPlayer = Array_GetNumberOfPlayer(v9);
  SessionName = (constchar *)Array_GetSessionName(v9++);
  sprintf(GameName, "%s ( %.1d / %.1d )", SessionName, NumberOfPlayer, NumberMax);
\```

**11**

HEXACON 2024

## Slide 12

12

## **Stack buffer overflow**

int __thiscall sub_4DC120(_DWORD *this)
{
const char *SessionName; // eax
int NumberOfPlayer; // [esp-8h] [ebp-9Ch]
int NumberMax; // [esp-4h] [ebp-98h]
char GameName[122]; // [esp+8h] [ebp-8Ch] BYREF
  [...]
  NumberMax = Array_GetNumberMax(v9);
  NumberOfPlayer = Array_GetNumberOfPlayer(v9);
  SessionName = (const char *)Array_GetSessionName(v9++);
  sprintf(GameName, "%s ( %.1d / %.1d )", SessionName, NumberOfPlayer, NumberMax);

**12**

HEXACON 2024

## Slide 13

## **Stack buffer overflow**

13

int __thiscall sub_4DC120(_DWORD *this)
{
const char *SessionName; // eax
int NumberOfPlayer; // [esp-8h] [ebp-9Ch]
int NumberMax; // [esp-4h] [ebp-98h]
char GameName[122]; // [esp+8h] [ebp-8Ch] BYREF
  [...]
  NumberMax = Array_GetNumberMax(v9);
  NumberOfPlayer = Array_GetNumberOfPlayer(v9);
  SessionName = (const char *)Array_GetSessionName(v9++);
  sprintf(GameName, "%s ( %.1d / %.1d )", SessionName, NumberOfPlayer, NumberMax);

**13**

HEXACON 2024

## Slide 14

**14**

## **Game assets handling**

14

HEXACON 2024


> Recovered by OCR — confidence 79/100 on the text kept, 66/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Game assets handling #SYNACKTIV
=~ Downloading map. 33% copiés
```

## Slide 15

**15**

## **Game assets handling**

15

\```
signedint __thiscall WriteMapToDisk(DownloadCtx_T *this)
{
\```

\```
[...]
  DKXSize = v22->DKXSize;
  DKDSize = v22->DKDSize;
  MapNameFromFile = (constchar *)(v22->BufferMap + DKDSize + DKXSize);
  NumberOfBytesWritten = v22->TotalBytesToReceive - DKDSize - DKXSize;
  strncpy(MapName, MapNameFromFile, NumberOfBytesWritten);
\```

HEXACON 2024

## Slide 16

## **Index out of bounds**

16

\```
__int64__fastcall CGamePermission::SetSinglePermission(
       CGamePermission *perms,
int index,
char value)
{
__int64 result; // rax
  result = index;
  perms->m_permissions[index] = value;
return result;
}
\```

**16**

HEXACON 2024

## Slide 17

## **Index out of bounds**

17

\```
__int64__fastcall CGamePermission::SetSinglePermission(
       CGamePermission *perms,
int index,
char value)
{
__int64 result; // rax
  result = index;
  perms->m_permissions[index] = value;
return result;
}
\```

HEXACON 2024

**17**

## Slide 18

## **Hunting table**

_Same bugs_

#### **Windows XP**

_Same bugs_

18

#### Windows 10 (re-released)

_Same bugs_

_Same bugs_

**18**

HEXACON 2024

## Slide 19

## **Hunting table**

19

Game Stack Cookie DEP ASLR
Aliens versus Predator 2 No No No
Diablo I No Yes Partial
Baldur’s Gates Enhanced Edition Yes Yes No
Baldur’s Gates II Enhanced Edition Yes Yes No
Icewind Dale Enhanced Editions Yes Yes No
American Conquest No No No
Cossacks II Yes No No

**19**

HEXACON 2024

## Slide 20

20

# **<u>Neverwinter Nights</u>**

**20**

HEXACON 2024

## Slide 21

## **<u>Neverwinter Nights</u>**

- RPG

- Developped by BioWare (2002)

- Reedited by Beamdog (2018)

- Available on Steam, GOG

- Aurora Engine

21

- Multiplayer LAN and Online

**21**

HEXACON 2024

## Slide 22

## **<u>Informations gathering</u>**

- Linux version has debug symbols

- Modding community

 Xoreos (open-source clone of Aurora Engine)

 https://github.com/Nostritius/nwn-wireshark/

- Few information about multiplayer

22

**22**

HEXACON 2024

## Slide 23

## **<u>Tooling</u>**

###  Existing tools to inspect

 Character file (.BIC)

 Saved Games (.SAV)

 NeverwinterNights Modules (.NWM)

23

**23**

HEXACON 2024

## Slide 24

24

## **Open-source components**

- License file

- Check outaded components

**24**

HEXACON 2024


> Recovered by OCR — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Open-source components
| Options > Open-Source Licences
License file
Check outaded
components
cpptoml
curl
glew
glm
hydrogen
jansson
kiwi
moodycamel
nlohmann_json
nuklear
openmp3
openssl
sdl2
shat
sole
Permission is hereby granted, fi arge, to any person obtaining a copy o
this software and associated do onte Files (the “Software"), to deal in
the Software without re on, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
subject to the wing conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the So
IFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
IMPLIED, INCLUDING BU" T LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITN!
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF
OR IN
```

## Slide 25

## **<u>Mitigations</u>**

####  Stack Cookie

- DEP

- ASLR

- No CFG

25

**25**

HEXACON 2024

## Slide 26

26

# **<u>Attack surface</u>**

**26**

HEXACON 2024

## Slide 27

## **<u>Lobby</u>**

###  ~19 “Non Window Message”

Type Description BNES Game Search Broadcast BNER Game Search (Response) BNCS Game CD Key BNCR Game CD Key (Response) BNVS Password Related BNVR Password Related (Response)

27

**27**

HEXACON 2024

## Slide 28

## **<u>Key</u> Exchange**

28

###  Encrypted Communication

- Use open-source LibHydrogen

   - Based on Curve25519 elliptic curve and Gimli permutation

   - Noise Protocol Framework

- Static keypair derived from CD-Key

**28**

HEXACON 2024

## Slide 29

## **Network stack**

29

>  Divided in 3 layer  Layer 1 : Handle deciphering  Layer 2 : Handle compressed and fragmented data  Layer 3 : Handle game message

**29**

HEXACON 2024

## Slide 30

## **Layer 1**

- UDP Based

- 1 magic byte

- 4 random bytes

30

**30**

HEXACON 2024

## Slide 31

## **Layer 2**

###  3 Frame Types

- DATA

- ACK

 NAK

- Fragmentation

>  Compression

31

**31**

HEXACON 2024


> Recovered by OCR — confidence 89/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Layer 2
m= 3 Frame Types
=» DAIA
=» ACK
=» NAK
= Fragmentation
= Compression
HEXACON 2024
flags details
s
T
+00h
+08h
— extended length
message type
‘compressed by net layer
single recipient
Magic cRC Frameld Frameld Flags
nFrame Length
Frame data
00 00.00 0000 0000 Flags
00 00 Length
Frame data
31
```

## Slide 32

## **Layer 3**

32

###  4 types of messages

 “P” Server to Player

 “p” Player to Server

- “S” Server to SysAdmin

 “s” SysAdmin to Server

**32**

HEXACON 2024

## Slide 33

## **SysAdmin Message**

33

###  Only between Server and the “Administrator”  Textual command “Control.Boot  1”

**33**

HEXACON 2024


> Recovered by OCR — confidence 88/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
SysAdmin Message
= Only between Server and the “Administrator”
= Textual command “Control.Boot 1”
Server Name Server
Difficulty Easy
Levels
Players / Max Players:
B NWServer - Server - 1/4 0:31:48
‘Server AutoSave Interval (minutes)
12> 404
- x
IP Address 192.168.56.104:5121
Module Name M4
Game Type Action =|
Player vs. Player Party bd
Local Characters Allowed
Enforce Legal Characters
ltern Level Restrictions
Only One Party
Player Pause Enabled
Reload When Empty
Player Password:
Ban Name Ban CD DM Password:
Ban IP Boot Serer Admin Password
Save Game Slot Number
[Server Message: Send Message
Server status: Build 8193.36-13 [d?7dd024] Idle, login disabled. Shut down|
33
```

## Slide 34

## **Player/Server messages**

34

###  Game related message

- Update creature appearance

- Start a progress bar

- Add a quest in journal

- Level up



   - …

- ~250 messages types

**34**

HEXACON 2024

## Slide 35

## **Message Parsing**

35

###  CNWMessage helps to decode byte stream

- 21 simple types

   - CNWMessage::ReadBOOL

   - CNWMessage::ReadBYTE

   - CNWMessage::ReadINT

   - CNWMessage::ReadDOUBLE

   - CNWMessage::ReadVOIDPtr

   - CNWMessage::ReadCExoString

   -

- …

**35**

HEXACON 2024

## Slide 36

36

# **<u>Vulnerabilities</u>**

**36**

HEXACON 2024

## Slide 37

37

## **<u>First Bug</u>**

\```
__int64__fastcall CNWCMessage::HandleServerToPlayerLogin(CNWMessage *this, char Minor) {
[...]
int Class[8];       // [rsp+F0h] [rbp-18h] BYREF
char ClassLevel[8]; // [rsp+110h] [rbp+8h] BYREF
[...]
switch(Minor)
{
[…]
case 10:
ClassListSize = CNWMessage::ReadBYTE(this, 8);
_ClasListSize = ClassListSize;
if ( ClassListSize )
{
_ClassLevel = ClassLevel;
_Class = Class;
n = ClassListSize;
do
{
// stack buffer overflow
*_Class = CNWMessage::ReadINT(this, 32);
*_ClassLevel = CNWMessage::ReadBYTE(this, 8);
++_Class;
++_ClassLevel;
--n;
}
while ( n );
}
Experience = CNWMessage::ReadDWORD(this, 32);
[...]
CPanelCharVersionPopup::SetSaveCharacterInfo(v13, _ClassListSize, Class, ClassLevel, Experience);
\```

**37**

HEXACON 2024

## Slide 38

## **<u>First Bug</u>**

>  Classic stack buffer overflow

>  count 0..255

- Inexploitable due to stack cookie …

38

**38**

HEXACON 2024

## Slide 39

## **<u>Second bug</u>**

39

\```
__int64__fastcall CNWCMessage::HandleServerToPlayerCreatureUpdate_Appearance(CNWMessage *this)
{
[…]
unsigned__int16 Buf[18]; // [rsp+216h] [rbp-11Ah] BYREF
[…]
    Count = CNWMessage::ReadBYTE(this, 8);
    _Count = Count;
if ( Count )
    {
      v53 = (int *)Buf;
if ( Count <= 9u )
      {
        CNWCCreatureAppearance::GetPartVariations(
          *((CNWCCreatureAppearance **)CreatureByGameObjectID + 102),
          (unsigned__int8 *)Buf,
;
        n = 0;
while ( 1 )
        {
index = CNWMessage::ReadBYTE(this, 8);
if ( CNWMessage::MessageReadOverflow(this) )
goto LABEL_82;
if ( _bVersionSup_8193_35 )
value = CNWMessage::ReadWORD(this, 16);
else
            value = (unsigned__int8)CNWMessage::ReadBYTE(this, 8);
          ++n;
Buf[index] = value;
if ( _Count == n )
goto LABEL_130;
        }
      }
\```

**39**

HEXACON 2024

## Slide 40

## **<u>Second bug</u>**

40

>  Out of bound write in stack

>  10 word write

>  Enough to rewrite return address

>  Need a leak …

**40**

HEXACON 2024

## Slide 41

## **<u>Find a leak</u>**

41



##### By design server doesn’t need to query information about client …

**41**

HEXACON 2024

## Slide 42

## **<u>Int eger underflow bug</u>**

42

\```
__int64__fastcall CNWCMessage::HandleServerToPlayerMessage(CNWMessage *this, char *Buf, int Len)
{
  […]
  Magic = *Buf;
  Major = Buf[1];
  Minor = Buf[2];
if ( CNWMessage::SetReadMessage(this, Buf + 3, Len - 3, -1, 1)
    && (v8 = g_pAppManager->CClientExoApp->vtable->CClientExoApp::GetNetLayer)(g_pAppManager->CClientExoApp),
        CNetLayer::GetClientConnected(v8))
    && !CNWMessage::MessageReadOverflow(this)
    && Magic == 'P' )
  {
    CNetworkProfiler::AddMessageToProfile((constvoid **)g_cNetworkProfiler, 82, Major, Buf[2], Len);
    CExoString::Format(&a1, "unknown Major (0x%.2X)", Major);
switch ( Major )
    {
case 1u:
        CExoString::operator=(&a1, "ServerStatus");
        active = CNWCMessage::HandleServerToPlayerServerStatus(this, Minor);
goto LABEL_9;
case 2u:
        CExoString::operator=(&a1, "Login");
        active = CNWCMessage::HandleServerToPlayerLogin(this, Minor);
goto LABEL_9;
\```

**42**

HEXACON 2024

## Slide 43

## **<u>Int eger underflow bug</u>**

43

\```
unsignedint__fastcall CNWMessage::SetReadMessage(
        CNWMessage *this,
unsigned__int8 *messageBuf,
unsignedint Length,
int a4,
int a5)
{
unsignedint bytesStreamLength; // ecx
unsignedint res; // eax
  this->messageBuf = messageBuf;
  this->messageLength = Length;
this->curPos = 0;
  [...]
if ( Length )
  {
this->curPos = 4;
    bytesStreamLength = *(_DWORD *)messageBuf - 3;
    res = 0;
this->bitsBufferOffset = bytesStreamLength;
if ( bytesStreamLength < Length )
    {
this->bitsBuffer = &messageBuf[bytesStreamLength];
this->bitsBufferLen = Length - bytesStreamLength;
this->bitsPos = 0;
this->messageLength = bytesStreamLength;
this->nEncodedBits = CNWMessage::ReadBYTE(this, 3);
return 1;
    }
  }
else
  {
  […]
\```

**43**

HEXACON 2024

## Slide 44

## **<u>Int eger underflow bug</u>**

44

\```
unsignedint__fastcall CNWMessage::SetReadMessage(
        CNWMessage *this,
unsigned__int8 *messageBuf,
unsignedint Length,
int a4,
int a5)
{
unsignedint bytesStreamLength; // ecx
unsignedint res; // eax
this->messageBuf = messageBuf;
this->messageLength = Length;
this->curPos = 0;
  [...]
if ( Length )
  {
this->curPos = 4;
bytesStreamLength = *(_DWORD *)messageBuf - 3;
    res = 0;
this->bitsBufferOffset = bytesStreamLength;
if ( bytesStreamLength < Length )
    {
this->bitsBuffer = &messageBuf[bytesStreamLength];
      this->bitsBufferLen = Length - bytesStreamLength;
this->bitsPos = 0;
this->messageLength = bytesStreamLength;
this->nEncodedBits = CNWMessage::ReadBYTE(this, 3);
return 1;
    }
  }
else
  {
  […]
\```

**44**

HEXACON 2024

## Slide 45

## **<u>Transform into OOBR</u>**

45

###  Find a way to have the same memory buffer used between two message

- Frame can contains compressed data

- CNetLayerInternal::UncompressMessage use a temporary buffer

   - Dynamically allocated when uncompressed size is >= 0x20000

   - else _rx_buffer_ member is used

   - _rx_buffer_ is not erased after use

**45**

HEXACON 2024

## Slide 46

## **<u>Transform into OOBR</u>**

46

######  Send first invalid message to initialise buffer

**46**

HEXACON 2024

## Slide 47

## **<u>Transform into OOBR</u>**

47

 Send first invalid message to initialise buffer

 Send second message of 2 bytes

**47**

HEXACON 2024

## Slide 48

## **<u>Transform into OOBR</u>**

48

###  CNWMessage::ReadVOIDPtr

 return a pointer to buffer of arbitrary size  Usage of CNWMessage::ReadVOIDPtr

**48**

HEXACON 2024

## Slide 49

## **<u>Transform into OOBR</u>**

- Upload assets to client

- Write some heap data into a client file

49

- `__int64 __fastcall CNWCMessage::HandleServerToPlayerResman( CNWMessage *this, char minor)`

\```
{
\```

\```
[…]
\```

\```
switch ( minor )
    {
\```

\```
[…]
\```

\```
case 5:
\```

- No way to request file :(

- Give up …

\```
        CNWMessage::ReadCResRef((CResRef *)v34, this, 16);
        CExoString::CExoString(&v29, (const CResRef *)v34);
        v27 = CNWMessage::ReadSHORT(this, 16);
Length = CNWMessage::ReadDWORD(this, 32);
        VOIDPtr = CNWMessage::ReadVOIDPtr(this, Length);
if ( CNWMessage::MessageReadOverflow(this) )
goto LABEL_32;
        CExoString::StripNonAlphaNumeric(&v29, 1, 0, 0);
        v7 = CExoString::CStr(&v29);
        CExoString::CExoString(&v30);
        CExoString::Format(&v30, "TEMPCLIENT:%s", v7);
if ( Length )
\```

\```
        {
          CExoString::CExoString(&v32, "wb");
          CExoFile::CExoFile((CExoFile *)&v31, &v30, v27, &v32);
          [...]
          CExoFile::Write((CExoFile *)&v31, VOIDPtr, 1u, Length);
          CExoFile::~CExoFile((#204 *)&v31);
        }
\```

**49**

HEXACON 2024

## Slide 50

## **<u>Neverwinter Night Script</u>**

- _Weird symbol name RunScriptChunk_

- Virtual Machine stackbased

- Server can execute arbitrary script send from player

 Only in DebugMode …

50

**50**

HEXACON 2024

## Slide 51

## **<u>Portal feature</u>**

51

>  Found when looking NWScript surface

>  Well-documented : https://nwnlexicon.com/index.php/ActivatePortal

**51**

HEXACON 2024

## Slide 52

## **<u>Portal feature</u>**

52

###  CNWCMessage::HandleServerToPlayerPortalActivatePortal

 Major/Minor 2A/01  Work with DebugMode <u>disabled</u>

 bSeamless => Automatic transfert without dialog box

**52**

HEXACON 2024

## Slide 53

## **<u>Portal feature</u>**

53

Player Server A
ActivatePortal

**53**

HEXACON 2024

## Slide 54

## **<u>Portal feature</u>**

54

Player Server A
ActivatePortal
CharacterDownloadGimme

**54**

HEXACON 2024

## Slide 55

## **<u>Portal feature</u>**

55

Player Server A
ActivatePortal
CharacterDownloadGimme
CharacterDownloadReply

**55**

HEXACON 2024

## Slide 56

## **<u>Portal feature</u>**

56

Player Server A Server B
ActivatePortal
CharacterDownloadGimme
CharacterDownloadReply
LoginLocalCharacter

**56**

HEXACON 2024

## Slide 57

57

# **<u>Exploitation</u>**

**57**

HEXACON 2024

## Slide 58

## **<u>Leak</u>**

58

###  Activate Portal

- Use integer underflow bug to trigger OOBR during _SetCharacterFile_

- Second server received leaked heap memory

- Search pattern in memory to find program base

   - `__int64 __fastcall CNWCMessage::HandleServerToPlayerCharacterDownload(CNWMessage *this, char Minor) { [...] if ( Minor == 2 )`

   - `{` **`length = CNWMessage::ReadDWORD(this, 32);`**

   - **`pointer = (unsigned __int8 *)CNWMessage::ReadVOIDPtr(this, length);`**

   - `CClientExoApp::SetCharacterFile(g_pAppManager->CClientExoApp,` **`length`** `,` **`pointer`** `, 0);`

**58**

HEXACON 2024

## Slide 59

## **<u>Pivot</u>**

59

>  OOBW to rewrite return address

>  RBX points to CWNMessage

>  Limited call to existing vtable functions

**59**

HEXACON 2024

## Slide 60

## **<u>Pivot</u>**

60

>  OOBW to rewrite return address

>  RBX points to CWNMessage

>  Limited call to existing vtable functions

**60**

HEXACON 2024

## Slide 61

## **<u>Pivot</u>**

61

>  OOBW to rewrite return address

>  RBX points to CWNMessage

>  Limited call to existing vtable functions

**61**

HEXACON 2024

## Slide 62

## **<u>Pivot</u>**

62

>  Goal : Limited call to arbitrary call

>  Reuse “Steam gadget” (found in previous research)  CCallResult<CSteamInternal,CreateItemResult_t>::Run

>  RCX points to buffer (due to previous gadget)

>  JMP anywhere

**62**

HEXACON 2024

## Slide 63

## **<u>Pivot</u>**

63

>  Goal : Start ROPChain placed in message

>  ROPChain will execute calc.exe

>  COP/JOP Chain

 RAX points to CWNMessage buffer  Move RAX into RSP with 3 gadgets

\```
push rax ; mov rcx, rbx ; call qword ptr [rax + 0x48]
pop rdi ; jmp qword ptr [rax + 0x40]
\```

\```
pop rsp ; and al, 0x50 ; add rsp, 0x58 ; ret
\```

**63**

HEXACON 2024

## Slide 64

## **Demo**

64

**64**

HEXACON 2024


> Recovered by OCR — confidence 83/100 on the text kept, 64/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
VM VirtualBox vax
gy Oracle VM VirtualBox de machines via Server 2 [En fonction] - 01
Fichier hine Fichier Machine Ecran iphériques Aide
L Outils.
Fichier hine Ecran
Server [En fonction] - Oracle VM VirtualBox
G raw Fiques Aide
ry
not defined
-1 poc-leak-in-character-2.js nwmain.e
Ts A world-class dynamic instrumentation toolkit
z
-> Displays the help system
Display information about ‘object’
G xit
Local System (id=local)
Neverwinter
Nights -
Enhanced Edition
P& Tapez ici pour effectuer une recherche
```

## Slide 65

## **<u>Conclusion</u>**

65

###  Modding community provides great ressources for security researchers

>  Devil hides in the details

>  Intel CET will kill exploitation

>  Next …

**65**

HEXACON 2024

## Slide 66

66

**https://www.linkedin.com/company/synacktiv https://twitter.com/synacktiv https://synacktiv.com**

**HEXACON 2024**
