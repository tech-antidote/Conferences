---
title: "Proxying to Kernel  Streaming vulnerabilities from the Windows Kernel"
speakers: ["An-Jie Yang"]
conference: "Hexacon"
conference_full: "Hexacon 2024"
edition: ""
year: 2024
source_pdf: "Hexacon 2024 Slides/An-Jie Yang_Proxying to Kernel  Streaming vulnerabilities from the Windows Kernel.pdf"
pages: 210
sha256: "c417b8581c2e7f000026218c737e2ae170017092299872854aca4a3f0b9f57f7"
text_chars: 49608
ocr_pages: 58
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T23:20:20Z"
---
# Proxying to Kernel  Streaming vulnerabilities from the Windows Kernel

**Speakers:** An-Jie Yang  
**Conference:** Hexacon 2024  
**Source:** `Hexacon 2024 Slides/An-Jie Yang_Proxying to Kernel  Streaming vulnerabilities from the Windows Kernel.pdf` (210 pages)

## Slide 1

### **Proxying to Kernel : Streaming vulnerabilities from the Windows Kernel**

Angelboy

angelboy@devco.re

HEXACON2024 | 2024.10.05

1

## Slide 2

## **Who am I**

- Angelboy (@scwuaptx)

- Senior Security of DEVCORE

- MSRC 2024 MVR Top 100

- Speaker at

- CODE BLUE, HITCON, HITB GSEC

- • Master of Pwn of Pwn2Own Toronto 2022

2

## Slide 3

## **Looking at historical vulnerabilities is indispensable**

3

## Slide 4

## **Pwn2Own Vancouver 2024**

4

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Pwn2Q0Own Vancouver 2024
Master of Pwn
Target Prize Points
Ubuntu Desktop
Microsoft Windows 11
Apple macOS
DEVCORE
```

## Slide 5

## **In-the-wild**

• Win32k

• GDI (Graphics Device Interface) and UI functions • Windows drawing, font management …

- Complexity of Code

- • It has been a popular target for attackers over the past decade.

5

## Slide 6

## **In-the-wild**

• CLFS

• Common Log File System • Handles log-based transaction processing

- Complexity of Code

- • It has been a popular target for attackers over the past six years.

6

## Slide 7

## **In-the-wild**

• MSKSSRV

- Microsoft Kernel Streaming Service

- • Handles synchronization of multimedia streams

- Very small

7

## Slide 8

## **In-the-wild**

• MSKSSRV

- Microsoft Kernel Streaming Service

- • Handles synchronization of multimedia streams

- Very small

- Last year it became a very popular target, with 2 ITW exploits in just a few month.

8

## Slide 9

## **In-the-wild**

- ~~Win32k~~

~~• CLFS~~

• MSKSSRV

• …

9

## Slide 10

## **Let's take a look at MSKSSRV**

10

## Slide 11

## **MSKSSRV**

• CVE-2023-29360 – logical bug (found by @masthoon) • MmProbeAndLockPages invalid AccessMode • No check if access mode is KernelMode (0)

11

## Slide 12

## **MSKSSRV**

• CVE-2023-29360 – logical bug (found by @masthoon) • MmProbeAndLockPages invalid AccessMode • No check if access mode is KernelMode (0) • Mapping arbitrary kernel memory to user space • Arbitrary memory writing

12

## Slide 13

## **MSKSSRV**

- CVE-2023-36802 – Type Confusion

   - No any check for FileObject->FsContext2

      - Context Object & Stream Object type confusion

13

## Slide 14

## **MSKSSRV**

#### • CVE-2024-30089 (found by chompie)

14

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
MSKSSRV
¢ CVE-2024-30089 (found by chompie)
Security Intelligence
Racing Round and Round: The
Little Bug That Could
DEVCORE
```

## Slide 15

## **But is that the end of it ?**

15

## Slide 16

## **Actually …**

16

## Slide 17

MSKSSRV

ksthunk . sys

ks . sys

portcls . sys

mspclock . sys

HdAud i o . sys

17

## Slide 18

18

## Slide 19

19

## Slide 20

20

## Slide 21

CVE

2024

38054

CVE

2024

30084

CVE

2024

35250

2024

38057

CVE

2024

30090

21

## Slide 22

## **Brief overview of Kernel Streaming**

22

## Slide 23

23

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Night light
e
Accessibility Nearby sharing
op)
8:16 AM
8/13/2024 L
DEVCORE
23
```

## Slide 24

## **What is Kernel Streaming ?** • Microsoft-provided services that support kernel-mode processing of streamed data

- Low Latency

- Efficient Data Processing

- Unified Interface

- High Extensibility

24

## Slide 25

**What is kernel streaming ?** • Microsoft provides 3 multimedia class driver models

- Port class

   - Audio device

- AVStream

   - integrated audio/video streaming

- Stream class

25

## Slide 26

## **How to interact with Device?**

26

## Slide 27

## **Enumerate Device**

27

## Slide 28

**Enumerate KS Device** • You can use SetupDiGetClassDevs with class GUID to emulate device \\?\hdaudio#subfunc_01&ven_8086&dev_2812&nid_0001&subsys _00000000&rev_1000#6&2f1f346a&0&0002&0000001d#{6994ad 04-93ef-11d0-a3cc-00a0c9223196}\ehdmiouttopo

28

## Slide 29

## **Enumerate KS Device**

• KsOpenDefaultDevice • Opens a handle to the first device that is listed in the specified Plug and Play (PnP) category

29

## Slide 30

## **KS Object**

30

## Slide 31

## **KS Object** • After we open these Devices, Kernel Streaming will establish some Kernel Streaming related instance

   - KS Filter

   - KS Pin

   - …

- Encapsulate hardware function

31

## Slide 32

## **KS Filter**

Filter
Data In Data Out
Node Node
0 1
Filter Factory

https://learn.microsoft.com/en-us/windows-hardware/drivers/audio/audio-filters

32

## Slide 33

## **KS Pin**

###### **Source Pin**

Filter
Data In Data Out
Node Node
0 1
Filter Factory
Sink Pin

https://learn.microsoft.com/en-us/windows-hardware/drivers/audio/audio-filters

33

## Slide 34

**KS Property** • A Property represents a capability or control-state setting that belongs to a kernel streaming object

• Client can set or get property to KS Object with GUID

- Device State

- Data format

- Volume Level

34

## Slide 35

## **KS Property**

• Device State is a KS property • Through IOCTL_KS_PROPERTY to get or set it

35

## Slide 36

## **Kernel Streaming Architecture**

36

## Slide 37

## **Kernel Streaming Architecture**

Application
User Mode
Kernel Mode
I/O Manager
mskssrv drmk mspclock …
Audio Filter AVStream
ksthunk.sys
portcls ks
ks.sys
…
HdAudio usbvideo
KS Filter

**Kernel Mode**

37

## Slide 38

## **Kernel Streaming Architecture**

Application
User Mode
Kernel Mode
I/O Manager
mskssrv drmk mspclock …
Audio Filter AVStream
ksthunk.sys
portcls ks
ks.sys
…
HdAudio usbvideo
KS Filter

**Kernel Mode**

38

## Slide 39

## **ksthunk**

- Kernel Streaming WOW Thunk Service Driver

- • Entry point of Kernel Streaming

• For backward compatibility

- If the request process is WoW64

   - Transfer 32-bits to 64-bit request

Wow64

Structure 32

ksthunk.sys
Structure 64

#### **Structure 64**

#### **KS Filter**

39

## Slide 40

## **Kernel Streaming Architecture**

Application
User Mode
Kernel Mode
I/O Manager
mskssrv drmk mspclock …
Audio Filter AVStream
ksthunk.sys
portcls ks
ks.sys
…
HdAudio usbvideo
KS Filter

**Kernel Mode**

40

## Slide 41

## **ks.sys**

• Kernel CSA Library • One of the main components of Kernel Streaming • Provide interface for Kernel Stream

- Property

- Event

- …

41

## Slide 42

## **The work flow of set pin state**

Application
User Mode
IOCTL_KS_PROPERTY
Kernel Mode
I/O Manager
mskssrv drmk mspclock …
Audio Filter AVStream
ksthunk.sys
portcls ks
ks.sys
…
HdAudio usbvideo
KS Filter

**Kernel Mode**

42

## Slide 43

## **The work flow of set pin state**

Application
User Mode
IOCTL_KS_PROPERTY
Kernel Mode
I/O Manager
mskssrv drmk mspclock …
Audio Filter AVStream
ksthunk.sys
portcls ks
ks.sys
…
Convert 32 bit request to 64 bit request
or pass it down directly
HdAudio usbvideo
KS Filter

**Kernel Mode**

43

## Slide 44

## **The work flow of set pin state**

Application
User Mode
IOCTL_KS_PROPERTY
Kernel Mode
I/O Manager
mskssrv drmk mspclock …
Audio Filter AVStream
ksthunk.sys
portcls ks
ks.sys
…
HdAudio usbvideo
KS Filter

**Kernel Mode**

44

## Slide 45

## **The work flow of set pin state**

Application
User Mode
IOCTL_KS_PROPERTY
Kernel Mode
I/O Manager
mskssrv drmk mspclock …
Audio Filter AVStream
ksthunk.sys
portcls ks
ks.sys
…
HdAudio usbvideo
KsPropertyHandler
KS Filter

**Kernel Mode**

45

## Slide 46

## **The work flow of set pin state**

Application
User Mode
IOCTL_KS_PROPERTY
Kernel Mode
I/O Manager
mskssrv drmk mspclock …
Audio Filter AVStream
ksthunk.sys
portcls ks
ks.sys
…
HdAudio usbvideo
KsPropertyHandler
Look for the property set, item and
the handler
KS Filter

46

## Slide 47

## **The work flow of set pin state**

Application
User Mode
IOCTL_KS_PROPERTY
Kernel Mode
I/O Manager
mskssrv drmk mspclock …
Audio Filter AVStream
ksthunk.sys
portcls ks
ks.sys
…
HdAudio usbvideo
KsPropertyHandler
KS Filter
portcls!PinPropertyDeviceState

**Kernel Mode**

47

## Slide 48

## **From attacker's view**

48

## Slide 49

## **From attacker's view**

• **There are many properties for each device**

• **individual implementation**

49

## Slide 50

## **From attacker's view**

• There are many properties for each device

   - individual implementation

- **No vulnerabilities in ks and ksthunk for a long time** • **CVE-2020-16889 (found by @nghiadt1098)**

   - **CVE-2020-17045 (found by @nghiadt1098)**

50

## Slide 51

## **From attacker's view**

• There are many properties for each device

- individual implementation

• No vulnerabilities in ks and ksthunk for a long time

- CVE-2020-16889 (found by @nghiadt1098)

- CVE-2020-17045 (found by @nghiadt1098)

• **Each driver handles part of the content individually, which may lead to inconsistencies.**

51

## Slide 52

## **We found some trivial vulnerabilities in few days …**

52

## Slide 53

## **Vulnerabilities**

- Portcls.sys

   - CVE-2024-38055 (OOB)

   - CVE-2024-38056

- Ksthunk

   - CVE-2024-38054 (OOB)

   - CVE-2024-38057

53

## Slide 54

## **We found some interesting things**

54

## Slide 55

## **Is really safe ?**

55

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Is really safe ?
if ( irp->RequestorMode )
{
}
else
{
v14 = 0xCQ000010;
UserBuffer = (unsigned int *)irp->UserBuffer ;
v19[@] = QLL;
v19[1] = v9;
FileObject = CurrentStackLocation->FileObject;
v21 = FileObject;
v14 = (*(__int64 (__fastcall **)(_QWORD, QWORD, _ int64 *))(Type3InputBuffer + @x38))(
*UserButter,
OLL,
v19);
}
DEVCORE
59
```

## Slide 56

## **Is really safe ?**

##### **UserMode(1)**

56

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Is really safe ?
if ( irp->RequestorMode 2 sertede
{
}
else
{
v14 = 0xCQ000010;
UserBuffer = (unsigned int *)irp->UserBuffer;
v19[0] = @LL;
v19[1] = v9;
FileObject = CurrentStackLocation->FileObject;
v21 = FileObject;
v14 = (*(__int64 (__fastcall **)(_QWORD, QWORD, _ int64 *))(Type3InputBuffer + @x38))(
*UserBuffer,
@LL,
v19);
}
DEVCORE
56
```

## Slide 57

## **The Overlooked Bug Class**

57

## Slide 58

**PreviousMode** • A field in the thread object that indicates whether the parameters for a System Service Call originated in user mode or kernel mode.

Application
User Mode
Kernel Mode
kthread->PreviousMode =
NtCreateFile
UserMode
ZwCreateFile
Device Driver Device Driver
kthread->PreviousMode =
KernelMode

58

## Slide 59

## **IRP RequestorMode**

• IRP->RequestorMode

• the execution mode of the original requester of the operation • A copy of the PreviousMode value from the thread object

59

## Slide 60

## **IRP RequestorMode**

60

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
IRP RequestorMode
if ( Irp->RequestorMode )
{
ProbeForRead(CurrentStackLocation->Parameters .DeviceloControl.Type3InputBuffer, InputBufferLength, 1u)
a4 = callback;
outputLength = outlen;
}
MmProbeAndLockPages(Irp->MdlAddress, Irp->RequestorMode, IoWriteAccess);
RequestorMode = Irp->RequestorMode;
v16 = (unsigned __int8)HIBYTE(*(_WORD *)(a2 + 24)) >> 6;
Object = OLL;
v14 = ObReferenceObjectByHandle(v8, v16, (POBJECT_TYPE)IoFileObjectType, RequestorMode, &Object, @LL);
DEVCORE
60
```

## Slide 61

## **But there are some issues in some cases …**

61

## Slide 62

## **A logical bug class** • Windows Kernel Logic Bug Class: Access Mode Mismatch in IO Manager by James Forshaw

User Mode Kernel Mode
Application Device Driver ZwOpenFile NtOpenFile
PreviousMode == UserMode

https://googleprojectzero.blogspot.com/2019/03/windows-kernel-logic-bug-class-access.html

62

## Slide 63

## **A logical bug class** • Windows Kernel Logic Bug Class: Access Mode Mismatch in IO Manager by James Forshaw

User Mode Kernel Mode
Application Device Driver ZwOpenFile NtOpenFile
PreviousMode == UserMode PreviousMode == KernelMode

https://googleprojectzero.blogspot.com/2019/03/windows-kernel-logic-bug-class-access.html

63

## Slide 64

## **A logical bug class** • What happens if kernel call OpenFile and solely relies on RequestorMode for validation ?

User Mode Kernel Mode
No Access Check
Application Device Driver ZwOpenFile NtOpenFile
PreviousMode == UserMode PreviousMode == KernelMode

https://googleprojectzero.blogspot.com/2019/03/windows-kernel-logic-bug-class-access.html

64

## Slide 65

## **A logical bug class** • What happens if kernel call OpenFile and solely relies on RequestorMode for validation ?

- Bypass

   - Security Access Check

   - Memory Access Check

https://googleprojectzero.blogspot.com/2019/03/windows-kernel-logic-bug-class-access.html

65

## Slide 66

## **It focuses on Zw* system service call**

66

## Slide 67

## **Are there other potential causes for this bug class?**

67

## Slide 68

## **Are there other potential causes for this bug class?**

68

## Slide 69

## **The Bug Pattern**

#### • IoBuildDeviceIoControlRequest

69

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
The Bug Pattern
¢ loBuildDeviceloControlRequest
The loBuildDeviceloControlRequest routine allocates and sets up an IRP for a synchronously processed device control
request.
Syntax
C++
__drv_aliasesMem PIRP IoBuildDeviceIoControlRequest(
[in] ULONG IoControlcode,
[in] PDEVICE_OBJECT DeviceObject,
[in, optional] PVOID InputBuffer,
[in] ULONG InputBufferLength,
[out, optional] PVOID OutputBuffer,
[in] ULONG OutputBufferLength,
[in] BOOLEAN InternalDeviceIoControl,
[in, optional] PKEVENT Event,
[out] PIO_STATUS_BLOCK IoStatusBlock
DEVCORE
69
```

## Slide 70

## **The Bug Pattern**

#### • IoBuildDeviceIoControlRequest

70

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
The Bug Pattern
¢ loBuildDeviceloControlRequest
loBuildDeviceloControlRequest returns, the RequestorMode field is always set to KernelMode.
DEVCORE
70
```

## Slide 71

## **The Bug Pattern**

#### • IoBuildDeviceIoControlRequest

Application
User Mode
Kernel Mode
RequestorMode
Nt*
= UserMode
Device Driver Device Driver
IoBuildDeviceIoControlRequest

71

## Slide 72

## **The Bug Pattern**

#### • IoBuildDeviceIoControlRequest

Application
User Mode
RequestorMode
Kernel Mode
= KernelMode
Nt*
IofCallDriver
Device Driver Device Driver
IoBuildDeviceIoControlRequest

72

## Slide 73

## **After quick review of this bug pattern in KS**

73

## Slide 74

74

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
NTSTATUS __stdcall KsSynchronousIoControlDevice(
PFILE OBJECT FileObject,
KPROCESSOR_MODE RequestorMode,
ULONG IoControl,————=~S
PVOID InBuffer,
ULONG InSize,
PVOID OutBuffer,
ULONG OutSize,
PULONG BytesReturned)
KeInitializeEvent(&Event, NotificationEvent, @);
NewIrp = IoBuildDeviceIoControlRequest(
ToControl,
RelatedDeviceObject,
InBuffer,
InSize,
OutBuffer,
OutSize,
e@,
&Event,
&IoStatusBlock) ;
NewIrp->RequestorMode RequestorMode;
Status = IofCallDriver(RelatedDeviceObject, NewIrp);
DEVCORE
74
```

## Slide 75

## **But …**

75

## Slide 76

##### **KernelMode**

###### **CKsPin::GetState**

76

## Slide 77

###### **CKsPin::GetState**

###### **SerializePropertySet**

KernelMode

77

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
CKsPin::GetState
BytesReturned = Q;
v5 = KsSynchronousToControlDevicelin_Worker|, 0, px2F0003u, &InBuffer, @x18u, OutBuffer,
v5 = -1073741306;
SerializePropertySet
{
if ( SerialSize )
v19 = KsSynchronousIoControlDevice(
ne i 1 leObject,
paren rameters .DevicelIoControl.IoControlCode,
PoolWithTag,
InSize,
(v16 + 0x20),
SerialSize,
&BytesReturned) ;
DEVCORE
77
```

## Slide 78

###### **CKsPin::GetState**

###### **UnserializePropertySet**

##### **KernelMode SerializePropertySet**

78

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
UnserializePropertySet
rror2;
KsSynchronousloControlDevice(
el
mrentStackLocation->Parameters .DeviceloControl.IoControlCode,
New_KsProperty_req,
InSize,
OutBuffer,
OutSize,
&BytesReturned) ;
DEVCORE
78
```

## Slide 79

## **Look for the bug pattern in KS**

1. KsSynchronousIoControlDevice 2. Controllable

- InputBuffer

- • OutputBuffer

- 3. IOCTL relies on RequestorMode for security checks

79

## Slide 80

## **Look for the bug pattern in KS**

#### 1. KsSynchronousIoControlDevice 2. Controllable

- InputBuffer

- OutputBuffer

80

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Look for the bug pattern in KS
1. KsSynchronousloControlDevice
2. Controllable
KsSynchronous LloControlDevice(
| nputBuffer CurrentStackLocation->FileObject,
0,
~ OutputBuffer CurrentStackLocation->Parameters.DeviceloControl.IoControlCode,
New KsProperty req,
InSize,
OutBuffer,
OutSize,
&BytesReturned) ;
DEVCORE
80
```

## Slide 81

## **Look for the bug pattern in KS**

#### 1. KsSynchronousIoControlDevice

2. Controllable

- InputBuffer

- • OutputBuffer

- 3. IOCTL relies on RequestorMode for security checks

81

## Slide 82

## **The Vulnerability & Exploitation**

82

## Slide 83

83

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
onmw
on i
aan
aa
ccs
oan
eoe
a6
=
[oS
c=
ects
sce
oo
eat
rug
can
owes
wo meee fe
merses (ee ria xs So Dy (9)
Oewe ay) {Acted rab & oe
Oe: Qastexra das |
```

## Slide 84

## **Unserialize the property set**

• KSPROPERTY_TYPE_UNSERIALIZESET • Interaction with multiple properties with a single call

Property Set
Property 1
Kernel
Application
Property 2
Streming
…
User Mode Kernel Mode

84

## Slide 85

## **UnserializePropertySet**

85

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
UnserializePropertySet
NTSTATUS __fastcall KspPropertyHandler(
PIRP Irp,
unsigned int propertysetscnt,
KSPROPERTY_SET *propertyset,
__int64 (__fastcall *a4)(_QWORD, _QWORD, _QWORD),
int a5,
__int64 NodeAutomationTable,
unsigned int NodeCnt)f{
// check if the UserProvideProperty->Set is in the propertyset
if ( KsProperty_flag == KSPROPERTY_TYPE_UNSERIALIZESET )
return UnserializePropertySet(Irp, sysbuf_, propertyset_);
85
```

## Slide 86

## **UnserializePropertySet**

86

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
UnserializePropertySet
unsigned __int64 _ fastcall UnserializePropertySet(
PIRP irp,
KSIDENTIFIER* UserProvideProperty,
KSPROPERTY_SET* propertyset_)
if
New_KsProperty_req = ExAllocatePoolWithTag(NonPagedPoolNx, InSize, @x7@70534Bu) ;
memmove(New_KsProperty_req, CurrentStackLocation->Parameters.DeviceloControl.Type3InputBuffer, InSize) ;
status = KsSynchronousloControlDevice(
CurrentStackLocation->FileObject,
e,
CurrentStackLocation->Parameters .DeviceloControl.IoControlCode,
New_KsProperty_req,
InSize,
OutBuffer,
OutSize,
&BytesReturned) ;
}
86
```

## Slide 87

## **UnserializePropertySet**

87

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
UnserializePropertySet
unsigned __int64 _ fastcall UnserializePropertySet(
PIRP irp,
KSIDENTIFIER* UserProvideProperty,
KSPROPERTY_SET* propertyset_)
if
New_KsProperty_req = ExAllocatePoolWithTag(NonPagedPoolNx, InSize, @x7@70534Bu) ;
memmove(New_KsProperty_req, CurrentStackLocation->Parameters.DeviceloControl.Type3InputBuffer, InSize) ;
status = KsSynchronousloControlDevice(
CurrentStackLocation->FileObject,
e,
CurrentStackLocation->Parameters .DeviceloControl.IoControlCode,
New_KsProperty_req,
InSize,
OutBuffer,
OutSize,
&BytesReturned) ;
}
87
```

## Slide 88

## **UnserializePropertySet**

KernelMode

88

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
UnserializePropertySet
unsigned __int64 __fastcall UnserializePropertySet(
PIRP irp,
KSIDENTIFIER* UserProvideProperty,
KSPROPERTY_SET* propertyset_)
New_KsProperty_req ExAllocatePoolWithTag(NonPagedPoolNx, InSize, 9x7@7@534Bu) ;
memmove(New_KsProperty_req, CurrentStackLocation->Parameters.DeviceloControl.Type3InputBuffer, InSize) ;
status = KsSynchronousIoControlDevice(
rentStackLocation->FileObject,
2. | KernelMode
eerentStackLocation->Parameters .DeviceloControl.IoControlCode,
New_KsProperty_req,
InSize,
OutBuffer,
OutSize,
&BytesReturned) ;
88
```

## Slide 89

## **UnserializePropertySet**

User Control

89

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
UnserializePropertySet
unsigned __int64 __fastcall UnserializePropertySet(
PIRP irp,
KSIDENTIFIER* UserProvideProperty,
KSPROPERTY_SET* propertyset_)
{
New_KsProperty_req = ExAllocatePoolWithTag(NonPagedPoolNx, InSize, @x7@70534Bu) ;
memmove(New_KsProperty_req, CurrentStackLocation->Parameters.DeviceloControl.Type3InputBuffer, InSize) ;
status = KsSynchronousloControlDevice(
CurrentStackLocation->FileObject,
8,
CurrentStackLocation->Parameters .DeviceloControl.IoControlCode,
New_KsProperty_req,
InSize,
OutBuffer, User Control
OutSize,
&BytesReturned) ;
}
89
```

## Slide 90

## **UnserializePropertySet**

Application
User Mode
IOCTL_KS_PROPERTY
Kernel Mode
I/O Manager
mskssrv drmk mspclock …
Audio Filter AVStream
ksthunk.sys
portcls ks
ks.sys
…
HdAudio usbvideo
KS Filter

**Kernel Mode**

90

## Slide 91

## **UnserializePropertySet**

Application
User Mode
IOCTL_KS_PROPERTY
Kernel Mode
RequestorMode
I/O Manager
= UserMode
mskssrv drmk mspclock …
Audio Filter AVStream
ksthunk.sys
portcls ks
ks.sys
Convert 32-bit to 64-bit
…
HdAudio usbvideo
KS Filter

**Kernel Mode**

91

## Slide 92

## **UnserializePropertySet**

Application
User Mode
IOCTL_KS_PROPERTY
Kernel Mode
I/O Manager
mskssrv drmk mspclock …
Audio Filter AVStream
ksthunk.sys
portcls ks
ks.sys
…
HdAudio usbvideo
KS Filter

**Kernel Mode**

92

## Slide 93

## **UnserializePropertySet**

Application
User Mode
IOCTL_KS_PROPERTY
Kernel Mode
I/O Manager
mskssrv drmk mspclock …
Audio Filter AVStream
ksthunk.sys
portcls ks
ks.sys
…
HdAudio usbvideo
KsPropertyHandler
KS Filter

93

## Slide 94

## **UnserializePropertySet**

Application
User Mode
IOCTL_KS_PROPERTY
Kernel Mode
I/O Manager
mskssrv drmk mspclock …
Audio Filter AVStream
ksthunk.sys
portcls ks
ks.sys
…
HdAudio usbvideo
KsPropertyHandler
If this property set exists,
call UnserializePropertySet
KS Filter

94

## Slide 95

## **UnserializePropertySet**

Application
User Mode
IOCTL_KS_PROPERTY
Kernel Mode
I/O Manager
mskssrv drmk mspclock …
Audio Filter AVStream
ksthunk.sys
portcls ks
ks.sys
…
HdAudio usbvideo
KS Filter KsSynchronousIoControlDevice

95

## Slide 96

## **UnserializePropertySet**

Application
User Mode
IOCTL_KS_PROPERTY
Kernel Mode
RequestorMode
I/O Manager
= KernelMode
mskssrv drmk mspclock …
Audio Filter AVStream
ksthunk.sys
portcls ks
ks.sys
…
HdAudio usbvideo
KS Filter KsSynchronousIoControlDevice

96

## Slide 97

## **We can do arbitrary IOCTL_KS_PROPERTY with KernelMode now**

97

## Slide 98

## **We need to find a target to EoP**

98

## Slide 99

## **UnserializePropertySet**

Application
User Mode
IOCTL_KS_PROPERTY
Kernel Mode
I/O Manager
mskssrv drmk mspclock …
Audio Filter AVStream
ksthunk.sys
portcls ks
ks.sys
…
HdAudio usbvideo
KS Filter
KsSynchronousIoControlDevice

**Kernel Mode**

99

## Slide 100

## **ksthunk!DispatchIoctl**

100

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ksthunk! Dispatchloctl
int64 a3, int *a4)
__int64 _ fastcall CKSThunkDevice: :CheckIrpForStackAdjustmentNative(__int64 al, struct _IRP *irp,
{
if ( *(_OWORD *)&Type3InputBuffer->Set == *(_OWORD *)&KSPROPSETID DrmAudioStream
&& !type3inputbuf.Id
&& (type3inputbuf.Flags & 2) != @ ) // KSPROPERTY_TYPE_SET
if ( irp->RequestorMode )
{
v14 = @xCceeeeele;
}
else
{
UserBuffer = (unsigned int *)irp->UserBuffer;
v14 = (*(__int64 (__fastcall **)(_QWORD, _QWORD, _ int64 *))(Type3InputBuffer + @x38))(// call Type3InputBuffer+0x38
*UserBuffer,
@LL,
v19);
100
```

## Slide 101

## **ksthunk!DispatchIoctl**

101

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ksthunk! Dispatchloctl
__int64 _ fastcall CKSThunkDevice: :CheckIrpForStackAdjustmentNative(__int64 al, struct _IRP *irp, __int64 a3, int *a4)
if
if ( *(_OWORD *)&Type3InputBuffer->Set == *(_OWORD *)&KSPROPSETID DrmAudioStream
&& !type3inputbuf.Id
&& (type3inputbuf.Flags & 2) !=@ ) // KSPROPERTY_TYPE_SET
{
if ( irp->RequestorMode )
{
v14 = 0xC@0ee00e10;
}
else
{
UserBuffer = (unsigned int *)irp->UserBuffer;
v14 = (*(__int64 (__fastcall **)(_QWORD, _QWORD, _ int64 *))(Type3InputBuffer + @x38))(// call Type3InputBuffer+0x38
*UserBuffer,
@LL,
v19);
}
}
101
```

## Slide 102

## **ksthunk!DispatchIoctl**

RequestorMode == KernelMode (0)

102

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ksthunk! Dispatchloctl
__int64 _ fastcall CKSThunkDevice: :CheckIrpForStackAdjustmentNative(__int64 al, struct _IRP *irp, __int64 a3, int *a4)
if
if ( *(_OWORD *)&Type3InputBuffer->Set == *(_OWORD *)&KSPROPSETID DrmAudioStream
&& !type3inputbuf.Id
&& (type3inputbuf.Flags & 2) !=@ ) // KSPROPERTY_TYPE_SET
{
if ( irp->RequestorMode )
{ RequestorMode == KernelMode (0)
v14 = 0xC@0ee00e10;
}
else
{
UserBuffer = (unsigned int *)irp->UserBuffer;
v14 = (*(__int64 (__fastcall **)(_QWORD, _QWORD, _ int64 *))(Type3InputBuffer + @x38))(// call Type3InputBuffer+0x38
*UserBuffer,
@LL,
v19);
}
}
102
```

## Slide 103

## **ksthunk!DispatchIoctl**

103

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ksthunk! Dispatchloctl
__int64 _ fastcall CKSThunkDevice: :CheckIrpForStackAdjustmentNative(__int64 al, struct _IRP *irp, __int64 a3, int *a4)
{
if ( *(_OWORD *)&Type3InputBuffer->Set == *(_OWORD *)&KSPROPSETID DrmAudioStream
&& !type3inputbuf.Id
&& (type3inputbuf.Flags & 2) !=@ ) // KSPROPERTY_TYPE_SET
{
if ( irp->RequestorMode )
{
v14 = 0xC@0ee00e10;
}
else
UserBuffer = (unsigned int *)irp->UserBuffer;
v14 = (*(__int64 (__fastcall **)(_QWORD, _QWORD, _ int64 *))(Type3InputBuffer + @x38))(// call Type3InputBuffer+0x38
*UserBuffer,
@LL,
v19);
}
103
```

## Slide 104

## **ksthunk!DispatchIoctl**

104

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ksthunk! Dispatchloctl
__int64 _ fastcall CKSThunkDevice: :CheckIrpForStackAdjustmentNative(__int64 al, struct _IRP *irp, __int64 a3, int *a4)
{
if ( *(_OWORD *)&Type3InputBuffer->Set == *(_OWORD *)&KSPROPSETID DrmAudioStream
&& !type3inputbuf.Id
&& (type3inputbuf.Flags & 2) !=@ ) // KSPROPERTY_TYPE_SET
v14 = @xCe@ee0e1e;
}
else
{
UserBuffer = (unsigned int *)irp->UserBuffer;
v14 = (*(__int64 (__fastcall **)(_QWORD, _QWORD, _ int64 *))(Type3InputBuffer + @x38))(// call Type3InputBuffer+0x38
*UserBuffer,
@LL,
v19);
104
```

## Slide 105

## **UnserializePropertySet**

Application
User Mode
IOCTL_KS_PROPERTY
Kernel Mode
I/O Manager
mskssrv drmk mspclock …
Audio Filter AVStream
ksthunk.sys
portcls ks
ks.sys
…
HdAudio usbvideo
KS Filter
KsSynchronousIoControlDevice

**Kernel Mode**

105

## Slide 106

## **ksthunk!DispatchIoctl**

106

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
BUGCHECK_
BUGCHECK_P1: c0Q@00005
BUGCHECK_P2: fffff801
BUGCHECK_P3: ffffaa88
BUGCHECK_P4: 0
CONTEXT:
rax=ffFF404040404040
rdx=eeeeeeQgeGeeReRe0
rip=ffFFF8017 3333380
r8=ffffaa88a40deb78
r11=eeeeEe2eEeeeQeeeeeRe
r14=4fac41982f2c8ddd
iopl=0e nv up
cs=@010 ss=0018 ds
ksthunk! guard_dispatc
FfFFF801° 73333380 ffe
=@02b
ksthunk! Dispatchloct!
73333380
a40de100
ffffaa88a40de100 -- (.cxr Oxffffaa88a40de100)
rbx=fFFfFF838a3cef5b20
rsi=ffff838a3cef5dae
rsp=ffffaa88a40deb28
r9=ffffaa88a40dec8e
r1i2=ffffaa88a4edec8e
r15=fffF838a3d45eeae
h_icall_nop:
) jmp
Resetting default scope
rcx=eee0eeeedeadbeed
rdi=eeee9ee9eeeeeee1
rbp=fffF838a3d45e0ae
r10=fffFfF8016aa26e90
r13=ffFF838a3dF23dee
es=@02b fs=0053 gs=002b
rax {ffff4e4e° 40404040}
ef1=00050246
```

## Slide 107

## **We have an arbitrary call with one argument now**

107

## Slide 108

## **Exploitation**

108

## Slide 109

## **Mitigation on Win11**

- kCFG

- kASLR

- SMEP

- …

109

## Slide 110

## **Mitigation on Win11**

- kCFG

- kASLR

   - NtQuerySystemInformation

- SMEP

   - Reuse Kernel Code

- …

110

## Slide 111

## **Bypass kCFG**

• Find a valid function in Windows Kernel • Our goal is turn arbitrary call to arbitrary memory write

111

## Slide 112

## **Bypass kCFG**

• Find a valid function in Windows Kernel

• Our goal is turn arbitrary call to arbitrary memory write • Search *Set* function export from ntoskrnl.exe

112

## Slide 113

## **Bypass kCFG**

113

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Bypass kCFG
Name
 f | ita Sai
fi RtINumberO BitsUlongPtr
fARtI ctiveConsoleld
i Rtl IIBits
fA Rtl IIBitsEx
fi RtiSetBit
Rt
i RtiSetBits
fA RtiSetBitsEx
fi RtlSetConsoleSessionForegroundProcessId
fA Rt
Rt
Rt
ControlSecurityDescriptor
DaclSecurityDescriptor
DynamicTimeZonelInformation
Address
00000001405A7080
00000001403B0490
0000000140758470
000000014024EE60
00000001403B3240
000000014029A5F0
000000014029D810
000000014024D8B0
0000000140355B70
00000001407574E0
0000000140852320
0000000140697010
00000001409BBA60
Ordinal
2441
2442
2505
2506
2507
2508
2509
2510
2511
2512
2513
2514
2515
DEVCORE
113
```

## Slide 114

## **Two hours later …**

114

## Slide 115

## **Bypass kCFG**

115

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Bypass kCFG
void __stdcall Rt1SetA11Bits(PRTL_BITMAP BitMapHeader)
if
unsigned int *Buffer; // r8
unsigned __int64 v2; // rdx
Buffer = BitMapHeader->Buffer;
v2 = (unsigned __int64)(4 * (((BitMapHeader->SizeOfBitMap & @x1F) != 6) + (BitMapHeader->SizeOfBitMap >> 5))) >> 2;
{
memset(Buffer, @xFFu, 8 * (v2 >> 1));
if ( (v2 &1) !=@ )
Buffer[v2 - 1] = -1;
DEVCORE
115
```

## Slide 116

## **Bypass kCFG**

#### • RtlSetAllBits • The RtlSetAllBits routine sets all bits in a given bitmap variable.

116

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Bypass kCFG
e RtlSetAllBits
¢ The RtlSetAllBits routine sets all bits in a given bitmap variable.
struct _RTL_BITMAP
NTSYSAPI VOID Rtl1SetAl11Bits( {
[in| PRTL_BITMAP BitMapHeader
); ULONG SizeOfBitMap;
ULONG* Buffer;
ts
DEVCORE
116
```

## Slide 117

## **We can set all bits in arbitrary memory**

117

## Slide 118

## **Abuse token privilege**

- We can use the primitive to

• Enable all privilege in current process token

###### **Eprocess->Token**

Token

_RTL_BITMAP
SizeOfBitmap

SizeOfBitmap
Buffer

Privileges

118

## Slide 119

## **Abuse token privilege**

- We can use the primitive to

#### • Enable all privilege in current process token

119

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Abuse token privilege
¢ We can use the primitive to
¢ Enable all privilege in current process token
Enabled
Enabled
Enabled
serlmpersonatePrivilege Enabled
Trivilege Enabled
Enabled
Enabled
C.-b)-4
Permissions
DEVCORE
119
```

## Slide 120

## **The Last Step**

• Well-known EoP method with SeDebugPrivilege

• Open process of winlogon.exe • Set thread attribute to PROC_THREAD_ATTRIBUTE_PARENT_PROCESS

• Spawn cmd.exe

120

## Slide 121

121

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Windows 11 23H2 - VMware Workstation
File Edit View VM Tabs Help . » Ooaga Dea
ibrary » Windows 11 23H2 Windows 11 Insider Preview
My Computer
Administrator: CAWind: 032
q Microsoft Windows [Version 10.0.22631.3527]
meee (c) Microsoft Corporation. All rights reserved.
ys
C: \Users\p20\Desktop>whoami
nt authority\system
C:\Users\p20\Desktop>,
121
```

## Slide 122

## **It's like a Proxy to Kernel !**

122

## Slide 123

## **However …**

123

## Slide 124

124

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
File Action Media View Help
»@
Command Prompt - p20_poc. +
Microsoft Windows [Version 10.0.22631.3527]
(c) Microsoft Corporation. All rights reserved.
2 & C:\Use/
fam</Error: 80070103
vl Ul
PRIVIL'
am /1t doesn't have a DRM device !
Press any key to continue...
° ec
Memory allocated at 0000000042420000
+] cur token address: FFFFCQO7BBE7F360
Error: 80070103
It doesn't have a DRM device !
Press any key to continue .
6:04AM <2
e/13/2024 SAE
Status: Running <=. §
124
```

## Slide 125

## **KS Device in Hyper-V**

Application
User Mode
IOCTL_KS_PROPERTY
Kernel Mode
I/O Manager
mskssrv drmk mspclock …
Audio Filter AVStream
ksthunk.sys
portcls ks
ks.sys
…
HdAudio usbvideo
KS Filter
KsSynchronousIoControlDevice

125

## Slide 126

## **KS Device in Hyper-V**

Application
User Mode
IOCTL_KS_PROPERTY
Kernel Mode
I/O Manager
mskssrv …
ksthunk.sys
No DrmAudioStream
property set
ks.sys
…
KS Filter
KsSynchronousIoControlDevice

126

## Slide 127

127

## Slide 128

## **IOCTL_KS_PROPERTY**

• Neither I/O

• Using user input buffer directly • Inputbuffer = Parameters.DeviceIoControl.Type3InputBuffer • Outputbuffer = Irp->UserBuffer

128

## Slide 129

## **KspPropertyHandler**

###### **User input buffer**

129

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
KspPropertyHandler
NTSTATUS __fastcall KspPropertyHandler(
PIRP Irp,
unsigned int propertysetscnt,
KSPROPERTY_SET *propertyset,
df
memmove (SystemBuffer| outlen_padding],
User input|buffer CurrentStackLocation->Parameters .DeviceIoControl.Type3InputBuffer,
InputBufferLength) ;
Guid = *&SystemBuffer outlen padding F
// Check if the Guid is in the property set
if ( KsProperty_flag == KSPROPERTY_TYPE_UNSERIALIZESET )
return UnserializePropertySet(Irp, sysbuf_, propertyset_);
129
```

## Slide 130

## **KspPropertyHandler**

130

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
KspPropertyHandler
NTSTATUS __fastcall KspPropertyHandler(
PIRP Irp,
unsigned int propertysetscnt,
KSPROPERTY_SET *propertyset,
aot!
memmove (SystemBuffer| outlen_padding],
CurrentStackLocation->Parameters .DeviceloControl.Type3InputBuffer,
InputBufferLength) ;
Guid = *&SystemBuffer|[ outlen_padding | ;
// Check if the Guid is in the property set
if ( KsProperty_flag == KSPROPERTY_TYPE_UNSERIALIZESET )
return UnserializePropertySet(Irp, sysbuf_, propertyset_);
130
```

## Slide 131

## **Let's take a look at UnserializePropertySet again**

131

## Slide 132

## **UnserializePropertySet**

###### **Copy User input again !?**

132

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
UnserializePropertySet
unsigned __int64 __fastcall UnserializePropertySet(
PIRP irp,
KSIDENTIFIER* UserProvideProperty,
KSPROPERTY_SET* propertyset_)
{
New_KsProperty_req = ExAllocatePoolWithTag(NonPagedPoolNx, InSize, @x7@70534Bu) ;
memmove(New_KsProperty_req, CurrentStackLocation->Parameters.DeviceloControl.Type3InputBuffer, InSize) ;
status = KsSynchronousloControlDevice( Copy User input again 1?
CurrentStackLocation->FileObject,
Q,
CurrentStackLocation->Parameters .DeviceloControl.IoControlCode,
New_KsProperty_req,
InSize,
OutBuffer,
OutSize,
&BytesReturned) ;
}
132
```

## Slide 133

## **UnserializePropertySet**

Copy User input again !?

133

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
UnserializePropertySet
unsigned __int64 __fastcall UnserializePropertySet(
PIRP irp,
KSIDENTIFIER* UserProvideProperty,
KSPROPERTY_SET* propertyset_)
New_KsProperty_req = ExAllocatePoolWithTag(NonP
InputBuffer, InSize) ;
put again !?
oControl.IoControlCode,
133
```

## Slide 134

## **UnserializePropertySet**

User Input Buffer
KSPROPSETID_Service
User Mode

KSPROPSETID_Service
Application
User Mode
IOCTL_KS_PROPERTY
Kernel Mode
I/O Manager
mskssrv …
ksthunk.sys
ks.sys
…
KS Filter

**Kernel Mode**

134

## Slide 135

## **UnserializePropertySet**

User Input Buffer

KSPROPSETID_Service
Application
User Mode
IOCTL_KS_PROPERTY
Kernel Mode
SystemBuffer
I/O Manager
KSPROPSETID_Service
mskssrv …
ksthunk.sys
ks.sys
…
KsPropertyHandler
If this property set exists,
call UnserializePropertySet
KS Filter

135

## Slide 136

## **UnserializePropertySet**

UnserializePropertySet
User Input Buffer Trigger Race Condition
DrmAudioStream
Application
User Mode
IOCTL_KS_PROPERTY
Kernel Mode
I/O Manager
mskssrv …
ksthunk.sys
ks.sys
…
call UnserializePropertySet
KS Filter

136

## Slide 137

## **UnserializePropertySet**

User Input Buffer
DrmAudioStream
Application
User Mode
IOCTL_KS_PROPERTY
Kernel Mode
New Input Buffer
I/O Manager
DrmAudioStream
mskssrv …
ksthunk.sys
ks.sys
…
call UnserializePropertySet
KS Filter

137

## Slide 138

## **UnserializePropertySet**

User Input Buffer
DrmAudioStream
Application
User Mode
IOCTL_KS_PROPERTY
Kernel Mode
RequestorMode
New Input Buffer
I/O Manager
= KernelMode
DrmAudioStream
mskssrv …
ksthunk.sys
ks.sys
…
KS Filter
KsSynchronousIoControlDevice

138

## Slide 139

139

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
File Action Media View’ Help
»@©O = ayy
GA Command Prompt
Microsoft Windows [Version 10.0.22631.3527]
(c) Microsoft Corporation. ALL rights reserved.
C:\Users\user>|
139
```

## Slide 140

140

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
DQ Zero Day Initiative @thezdi - 34215
Confirmed! The DEVCORE Team used a couple of bugs, including a
somewhat risky TOCTAU race condition, to get their LPE on #Windows 11.
They earn $30,000 and 3 Master of Pwn points. #Pwn2Own
DEVCORE RESEARCH TEAM
TARGETTING
Microsoft Windows 11 in the
PRIZE $ Local Elevation of Privilege category
ane
O
DEVCORE
140
```

## Slide 141

## **Is that the end of it ?**

141

## Slide 142

142

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ONS ore beer Leg = eri er
power.
7
Hilup oe
Chaqger aval ty
Savapink
tHUNe We OW Ale
Sait ee ae
fe riasse lp sy
ue ay) Aacea mak oe Oo
oe: taster dao
Qeo Me e-sosascodgct
SE Tae MAIS Oo
= recdsococSsS
```

## Slide 143

## **KS Event**

143

## Slide 144

## **KS Event** • Event sets are groups of related events for which a listener can request notification.

• Client can register event for

- Device State Change

- Time interval

• ...

144

## Slide 145

## **KS Event**

- Use  IOCTL_KS_ENABLE_EVENT to register

   - EVENT_HANDLE

   - SEMAPHORE_HANDLE

145

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
KS Event
¢ Use IOCTL_KS_ENABLE_EVENT to register typedef struct {
ULONG NotificationType;
» EVENT HANDLE inion 4
struct {
» SEMAPHORE HANDLE “HANDLE Event:
} EventHandle;
struct {
HANDLE Semaphore;
} SemaphoreHandle;
}
} KSEVENTDATA, *PKSEVENTDATA;
DEVCORE
145
```

## Slide 146

## **kstunk!ThunkEnableEventIrp** • Transfer 32-bit IOCTL_KS_ENABLE_EVENT requests to 64-bit requests

146

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
kstunk! ThunkEnableEventirp
¢ Transfer 32-bit IOCTL_KS_ENABLE_EVENT requests to 64-bit requests
__int64 _ fastcall CKSThunkDevice: :DispatchIoct1l(CKernelFilterDevice *al, IRP *irp, unsigned int a3, NTSTATUS *a4)
{
if ( IoIs32bitProcess(irp) && irp->RequestorMode )
{
if ( CurrentStackLocation->Parameters.DeviceIoControl.IoControlCode == IOCTL_KS ENABLE EVENT )
return CKSAutomationThunk: :ThunkEnableEventIrp(v12, a2, v11, a4);
}
else if ( CurrentStackLocation->Parameters.DeviceloControl.IoControlCode == IOCTL_KS_ PROPERTY )
{
//Pass down
return CKSThunkDevice: :CheckIrpForStackAdjustmentNative((__int64)al1, irp, v11, a4);
}
146
```

## Slide 147

## **ThunkEnableEventIrp**

User input

147

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ThunkEnableEventir
__int64 _ fastcall CKSAutomationThunk::ThunkEnableEventIrp(__int64 ioctlcode d, PIRP irp, __int64 a3, int *a4)
if
if ( (v25->Parameters.DeviceloControl.Type3InputBuffer->Flags & @xEFFFFFFF) == KSEVENT_TYPE_ENABLE
|| (v25->Parameters .DeviceIoControl.Type3InputBuffer->Flags & @xEFFFFFFF) == KSEVENT_TYPE_ONESHOT
|| (v25->Parameters .DeviceIoControl.Type3InputBuffer->Flags & @xEFFFFFFF) == KSEVENT_TYPE_ENABLEBUFFERED )
{
// Convert 32-bit requests and pass down directly
}
else if ( (v25->Parameters.DeviceloControl.Type3InputBuffer->Flags & @xEFFFFFFF) == KSEVENT_TYPE_QUERYBUFFER )
{
newinputbuf = (KSEVENT *)ExAllocatePoolWithTag((POOL_TYPE)@x600, (unsigned int)(inputbuflen + 8), ‘bqSK"');
memcpy (newinputbuf, Type3InputBuffer , 0x28) ; User input
el
v18 = KsSynchronousloControlDevice(
v25->FileObject,
e,
IOCTL_KS_ENABLE_EVENT,
newinputbuf ,
inputbuflen + 8,
OutBuffer,
outbuflen,
&BytesReturned) ;
147
```

## Slide 148

## **ThunkEnableEventIrp**

148

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ThunkEnableEventir
__int64 _ fastcall CKSAutomationThunk::ThunkEnableEventIrp(__int64 ioctlcode d, PIRP irp, __int64 a3, int *a4)
if
if ( (v25->Parameters.DeviceloControl.Type3InputBuffer->Flags & @xEFFFFFFF) == KSEVENT_TYPE_ENABLE
|| (v25->Parameters .DeviceIoControl.Type3InputBuffer->Flags & @xEFFFFFFF) == KSEVENT_TYPE_ONESHOT
|| (v25->Parameters .DeviceIoControl.Type3InputBuffer->Flags & @xEFFFFFFF) == KSEVENT_TYPE_ENABLEBUFFERED )
{
// Convert 32-bit requests and pass down directly
}
else if ( (v25->Parameters.DeviceloControl.Type3InputBuffer->Flags & @xEFFFFFFF) == KSEVENT_TYPE_QUERYBUFFER )
{
newinputbuf = (KSEVENT *)ExAllocatePoolWithTag((POOL_TYPE)@x600, (unsigned int)(inputbuflen + 8), ‘bqSK"');
memcpy (newinputbuf , Type3InputBuffer , 0x28) ;
v18 = KsSynchronousloControlDevice(
v25->FileObject,
8,
IOCTL_KS ENABLE EVENT,
newinputbuf ,
inputbuflen + 8,
OutBuffer,
outbuflen,
&BytesReturned) ;
148
```

## Slide 149

## **ThunkEnableEventIrp**

KernelMode

149

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ThunkEnableEventir
__int64 _ fastcall CKSAutomationThunk::ThunkEnableEventIrp(__int64 ioctlcode d, PIRP irp, __int64 a3, int *a4)
if
if ( (v25->Parameters.DeviceloControl.Type3InputBuffer->Flags & @xEFFFFFFF) == KSEVENT_TYPE_ENABLE
|| (v25->Parameters .DeviceIoControl.Type3InputBuffer->Flags & @xEFFFFFFF) == KSEVENT_TYPE_ONESHOT
|| (v25->Parameters .DeviceIoControl.Type3InputBuffer->Flags & @xEFFFFFFF) == KSEVENT_TYPE_ENABLEBUFFERED )
// Convert 32-bit requests and pass down directly
}
else if ( (v25->Parameters.DeviceloControl.Type3InputBuffer->Flags & @xEFFFFFFF) == KSEVENT_TYPE_QUERYBUFFER )
{
newinputbuf = (KSEVENT *)ExAllocatePoolWithTag((POOL_TYPE)@x600, (unsigned int)(inputbuflen + 8), ‘bqSK"');
memcpy (newinputbuf , Type3InputBuffer , 0x28) ;
v18 = KsSynchronousloControlDevice(
v25->FileObject,
KernelMode
eeTL KS ENABLE EVENT,
newinputbuf ,
inputbuflen + 8,
OutBuffer,
outbuflen,
&BytesReturned) ;
149
```

## Slide 150

## **ThunkEnableEventIrp**

Application
User Mode
IOCTL_KS_ENABLE_EVENT
Kernel Mode
I/O Manager
mskssrv drmk mspclock …
Audio Filter AVStream
ksthunk.sys
portcls ks
ks.sys
…
HdAudio usbvideo
KS Filter

**Kernel Mode**

150

## Slide 151

## **ThunkEnableEventIrp**

Application
User Mode
IOCTL_KS_ENABLE_EVENT
Kernel Mode
RequestorMode
I/O Manager
= UserMode
mskssrv drmk mspclock …
Audio Filter AVStream
ksthunk.sys
portcls ks
ks.sys
ThunkEnableEventIrp
…
HdAudio usbvideo
KS Filter

**Kernel Mode**

151

## Slide 152

## **ThunkEnableEventIrp**

###### **Application**

**User Mode**

IOCTL_KS_ENABLE_EVENT

**Kernel Mode**

I/O Manager
RequestorMode
mskssrv drmk mspclock …
= UserMode
Audio Filter AVStream
ksthunk.sys
portcls ks
ks.sys
ThunkEnableEventIrp
…
Convert 32-bit to 64-bit
HdAudio usbvideo
KS Filter

152

## Slide 153

## **ThunkEnableEventIrp**

Application
User Mode
IOCTL_KS_ENABLE_EVENT
Kernel Mode
I/O Manager
RequestorMode
mskssrv drmk mspclock …
= UserMode
Audio Filter AVStream
ksthunk.sys
portcls ks
ks.sys
…
HdAudio usbvideo
KS Filter
KsSynchronousIoControlDevice

**Kernel Mode**

153

## Slide 154

## **ThunkEnableEventIrp**

Application
User Mode
IOCTL_KS_ENABLE_EVENT
Kernel Mode
RequestorMode
I/O Manager
= KernelMode
mskssrv drmk mspclock …
Audio Filter AVStream
ksthunk.sys
portcls ks
ks.sys
…
HdAudio usbvideo
KS Filter
KsSynchronousIoControlDevice

154

## Slide 155

## **We can do arbitrary IOCTL_KS_ENABLE_EVENT with KernelMode now**

155

## Slide 156

## **We need to find a target to EoP**

156

## Slide 157

## **But we didn't find a suitable target in ksthunk**

157

## Slide 158

## **We decide to pass it down to look for target**

158

## Slide 159

## **ThunkEnableEventIrp**

Application
User Mode
IOCTL_KS_ENABLE_EVENT
Kernel Mode
RequestorMode
I/O Manager
= KernelMode
mskssrv drmk mspclock …
Audio Filter AVStream
ksthunk.sys
portcls ks
ks.sys
…
HdAudio usbvideo
KspEnableEvent
KS Filter

159

## Slide 160

## **We found some interesting …**

160

## Slide 161

## **KspEnableEvent**

161

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
KspEnableEvent
__int64 _ fastcall KspEnableEvent(
-)
EventData = ExAllocatePoolWithTag(...);
memcpy(EventData, Irp->UserBuffer,...);
EventEntryEx->EventEntry.NotificationType = EventData->NotificationType;
switch ( EventEntryEx_->EventEntry.NotificationType )
case KSEVENTF_EVENT_HANDLE:
break;
case KSEVENTF_EVENT_OBJECT:
case DPC:
case KSEVENTF_KSWORKITEM:
if (Irp->RequestorMode)
goto error;
}
Eventitem->AddEventHandler(Irp, EventData, PEventEntry) ;
161
```

## Slide 162

## **KS Event**

#### • The output buffer is a KSEVENTDATA structure used to specify a notification method.

- Call from kernel driver

   - EVENT_OBJECT

   - DPC

   - KSWORKITEM

   - …

162

## Slide 163

## **We can provide arbitrary kernel object to it !**

163

## Slide 164

## **But …**

164

## Slide 165

## **ThunkEnableEventIrp**

165

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ThunkEnableEventir
__int64 _ fastcall CKSAutomationThunk::ThunkEnableEventIrp(__int64 ioctlcode d, PIRP irp, __int64 a3, int *a4)
if
if ( (v25->Parameters.DeviceloControl.Type3InputBuffer->Flags & @xEFFFFFFF) == KSEVENT TYPE ENABLE
De
|| (v25->Parameters .DeviceIoControl.Type3InputBuffer->Flags & @xEFFFFFFF) == KSEVENT_TYPE_ONESHOT
|| (v25->Parameters .DeviceIoControl.Type3InputBuffer->Flags & @xEFFFFFFF) == KSEVENT_TYPE_ENABLEBUFFERED )
// Convert 32-bit requests and pass down directly
}
else if ( (v25->Parameters.DeviceloControl.Type3InputBuffer->Flags & @xEFFFFFFF) == KSEVENT_TYPE_QUERYBUFFER )
{
newinputbuf = (KSEVENT *)ExAllocatePoolWithTag((POOL_TYPE)@x600, (unsigned int)(inputbuflen + 8), ‘bqSK"');
memcpy (newinputbuf , Type3InputBuffer , 0x28) ;
v18 = KsSynchronousloControlDevice(
v25->FileObject,
e,
IOCTL_KS_ENABLE_EVENT,
newinputbuf ,
inputbuflen + 8,
OutBuffer,
outbuflen,
&BytesReturned) ;
165
```

## Slide 166

## **ThunkEnableEventIrp**

166

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ThunkEnableEventirp
__int64 _ fastcall CKSAutomationThunk::ThunkEnableEventIrp(__int64 ioctlcode d, PIRP irp, __int64 a3, int *a4)
if
if ( (v25->Parameters.DeviceloControl.Type3InputBuffer->Flags & @xEFFFFFFF) == KSEVENT_TYPE_ENABLE
|| (v25->Parameters .DeviceIoControl.Type3InputBuffer->Flags & @xEFFFFFFF) == KSEVENT_TYPE_ONESHOT
|| (v25->Parameters .DeviceIoControl.Type3InputBuffer->Flags & @xEFFFFFFF) == KSEVENT_TYPE_ENABLEBUFFERED )
// Convert 32-bit requests and pass down directly
}
else if ( (v25->Parameters.DeviceloControl.Type3InputBuffer->Flags & @xEFFFFFFF) == KSEVENT_TYPE_QUERYBUFFER )
|
{
newinputbuf = (KSEVENT *)ExAllocatePoolWithTag((POOL_TYPE)@x600, (unsigned int)(inputbuflen + 8), ‘bqSK"');
memcpy (newinputbuf , Type3InputBuffer , 0x28) ;
v18 = KsSynchronousloControlDevice(
v25->FileObject,
e,
IOCTL_KS_ENABLE_EVENT,
newinputbuf ,
inputbuflen + 8,
OutBuffer,
outbuflen,
&BytesReturned) ;
166
```

## Slide 167

## **Fortunately, there are double fetch everywhere.**

167

## Slide 168

## **ThunkEnableEventIrp**

**Race window**

168

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ThunkEnableEventirp
z)
else if ( (v25->Parameters.DevicelIoControl.Type3InputBuffer->Flags & @xEFFFFFFF) == KSEVENT_TYPE_QUERYBUFFER )
{
eee A
newinputbuf = (KSEVENT *)ExAllocatePoolWithTag((POOL_TYPE)@x60@, (unsigned int)(inputbuflen + 8), ‘baSK'3 Race window
memcpy (newinputbuf , Type3InputBuffer , 6x28) ; v
v18 = KsSynchronousIoControlDevice(
v25->FileObject,
8,
IOCTL_KS_ENABLE_EVENT,
newinputbuf,
inputbuflen + 8,
OutBuffer,
outbuflen,
&BytesReturned) ;
168
```

## Slide 169

## **If we trigger the event, it would call KsGenerateEvent**

169

## Slide 170

## **KsGenerateEvent**

###### **Arbitrary register DPC**

170

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
KsGenerateEvent
NTSTATUS __stdcall KsGenerateEvent(PKSEVENT_ENTRY EventEntry)
{
switch ( EventEntry->NotificationType )
{
case KSEVENTF_DPC:
wee Arbitrary register DPC
if ( !KeInsertQueueDpc(EventEntry->EventData->Dpc.Dpc, EventEntry->EventData, @LL) )
_InterlockedAdd(&EventEntry->EventData->EventObject.Increment, @xFFFFFFFF) ;
case KSEVENTF_KSWORKITEM:
KsIncrementCountedWorker (eventdata->KsWorkItem.KsWorkerObject) ;
170
```

## Slide 171

## **KsGenerateEvent**

171

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
KsGenerateEvent
NTSTATUS __stdcall KsGenerateEvent(PKSEVENT_ENTRY EventEntry)
{
switch ( EventEntry->NotificationType )
{
case KSEVENTF_DPC:
if ( !KeInsertQueueDpc(EventEntry->EventData->Dpc.Dpc, EventEntry->EventData, @LL) )
_InterlockedAdd(&EventEntry->EventData->EventObject.Increment, @xFFFFFFFF) ;
case KSEVENTF_KSWORKITEM:
KsIncrementCountedWorker (eventdata->KsWorkItem.KsWorkerObject) ;
171
```

## Slide 172

## **KsIncrementCountedWorker**

###### **Arbitrary memory increment**

172

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
KsIncrementCountedWorker
ULONG _ stdcall KsIncrementCountedWorker(__int64 Worker)
{
ULONG v1; // ebx
v1 = _InterlockedIncrement( (Worker + @x5C));
if ( vl == 1 ) Arbitrary memory increment
KsQueueWorkItem(Worker, *(Worker + 96));
return v1;
}
172
```

## Slide 173

## **We have arbitrary increment primitive now**

173

## Slide 174

## **Arbitrary increment primitive to EoP**

• There are many well-known method

- Abuse token privilege

- IoRing

- …

174

## Slide 175

## **It seems trivial, but ...**

175

## Slide 176

## **Arbitrary increment primitive to EoP**

#### • Abuse token privilege

• Need to overwrite Privileges.Enable and Privileges.Present • Need to trigger the bug multiple times

• It may take a long time

176

## Slide 177

## **Arbitrary increment primitive to EoP**

• IoRing • Need to overwrite IoRing->RegBuffersCount and IoRing->RegBuffers

• Good Candidate

• Only need to trigger the bug twice

177

## Slide 178

## **KsIncrementCountedWorker**

178

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
KsIncrementCountedWorker
ULONG _ stdcall KsIncrementCountedWorker(__int64 Worker)
{
ULONG v1; // ebx
v1 = _InterlockedIncrement( (Worker + @x5C));
KsQueueWorkItem(Worker, *(Worker + 96));
return v1;
}
178
```

## Slide 179

179

## Slide 180

## **Let's find a new way !**

180

## Slide 181

## **Arbitrary increment primitive to EoP**

• Abuse token privilege

• The goal is to obtain SeDebugPrivilege

• Open process of winlogon.exe

181

## Slide 182

## **Why does having SeDebugPrivilege allow you to open high-privilege process?**

182

## Slide 183

## **PsOpenProcess**

183

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
PsOpenProcess
if ( SeSinglePrivilegeCheck(SeDebugPrivilege, AccessMode ) )
{
if ( (AccessState.RemainingDesiredAccess & MAXIMUM_ALLOWED) != @ )
AccessState.PreviouslyGrantedAccess |= PROCESS ALL ACCESS;
else
AccessState.PreviouslyGrantedAccess |= AccessState.RemainingDesiredAccess;
AccessState.RemainingDesiredAccess = 0;
}
v2@ = ObOpenObjectByPointer (
Process,
HandleAttributes,
&AccessState,
0,
(POBJECT_TYPE)PsProcessType,
AccessMode,
&Handle) ;
DEVCORE
183
```

## Slide 184

## **PsOpenProcess**

184

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
PsOpenProcess
if ( SeSinglePrivilegeCheck|[SeDebugPrivilege,} AccessMode_) )
{
if ( (AccessState.RemainingDesiredAccess & MAXIMUM_ALLOWED) != @ )
AccessState.PreviouslyGrantedAccess |= PROCESS ALL ACCESS;
else
AccessState.PreviouslyGrantedAccess |= AccessState.RemainingDesiredAccess;
AccessState.RemainingDesiredAccess = 0;
}
v2@ = ObOpenObjectByPointer (
Process,
HandleAttributes,
&AccessState,
0,
(POBJECT_TYPE)PsProcessType,
AccessMode,
&Handle) ;
DEVCORE
184
```

## Slide 185

## **PsOpenProcess**

185

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
PsOpenProcess
DEVCORE
bool SepVariableInitialization()
if
SeDebugPrivilege = (LUID)@x14LL ;
v103 = 2LL;
v6@ = (PSID)21;
v61 = (PSID)@x16;
Sid (PSID)@x17;
SeAuditPrivilege = 21LL;
SeSystemEnvironmentPrivilege = (LUID)@x16LL;
SeChangeNotifyPrivilege = @x17LL;
185
```

## Slide 186

## **Make abusing token privilege great again**

Application
User Mode
Kernel Mode
NtOpenProcess
PsOpenProcess
Nt
SeSinglePrivilegeCheck
SeSinglePrivilegeCheck
SeDebugPrivilege
0x14
Token
Privileges
Eprocess->Token

186

## Slide 187

## **Make abusing token privilege great again**

Application
User Mode
Kernel Mode
NtOpenProcess
PsOpenProcess
Nt
SeSinglePrivilegeCheck
SeDebugPrivilege
0x14
Token
Privileges
Eprocess->Token

187

## Slide 188

## **One more interesting …**

188

## Slide 189

## **nt!SeDebugPrivilege**

###### **Writable !!!**

189

## Slide 190

## **Make abusing token privilege great again !**

190

## Slide 191

## **Make abusing token privilege great again**

191

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Make abusing token privilege great again
C:\Users\angelboy>whoami /priv
PRIVILEGES INFORMATION
Privilege Name Description State
SeShutdownPrivilege Shut down the system Disabled
SeChangeNotifyPrivilege Bypass traverse checking Enabled
SeUndockPrivilege Remove computer from docking station Disabled
SeIncreaseWorkingSetPrivilege Increase a process working set Disabled
SeTimeZonePrivilege Change the time zone Disabled
DEVCORE
191
```

## Slide 192

## **Make abusing token privilege great again**

192

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Make abusing token privilege great again
C:\Users\angelboy>whoami /priv
PRIVILEGES INFORMATION
Privilege Name Description State
SeShutdownPrivilege Shut down the system Disabled
SeChangeNotifyPrivilege Bypass traverse checking Enabled
SeUndockPrivilege Remove computer from docking station Disabled
SeIncreaseWorkingSetPrivilege Increase a process working set Disabled
SeTimeZonePrivilege Change the time zone Disabled
DEVCORE
192
```

## Slide 193

## **nt!SeChangeNotifyPrivilege**

193

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
nt! SeChangeNotifyPrivilege
bool SepVariableInitialization()
{
SeDebugPrivilege (LUID)@x14LL;
v103 = 2LL;
v6@ = (PSID)21;
v61 = (PSID)0x16;
Sid = (PSID)@x17;
SeAuditPrivilege = 21LL;
SeSystemEnvironmentPrivilege = (LUID)@x16LL;
SeChangeNotifyPrivilege = @x17LL;
DEVCORE
193
```

## Slide 194

**How about changing the value of nt!SeDebugPrivilege from 0x14 to 0x17 ?**

194

## Slide 195

## **Make abusing token privilege great again**

Application
User Mode
Kernel Mode
NtOpenProcess
PsOpenProcess
Nt
SeSinglePrivilegeCheck
SeSinglePrivilegeCheck
SeDebugPrivilege
0x17
Token
Privileges
Eprocess->Token

195

## Slide 196

## **Make abusing token privilege great again**

Application
User Mode
Kernel Mode
NtOpenProcess
PsOpenProcess
Nt
SeSinglePrivilegeCheck
SeDebugPrivilege
0x17
Token
Privileges
Eprocess->Token

196

## Slide 197

## **Make abusing token privilege great again**

Application
User Mode
Kernel Mode
NtOpenProcess
PsOpenProcess
Nt
SeSinglePrivilegeCheck
SeDebugPrivilege
0x17
Token
Privileges
Eprocess->Token

197

## Slide 198

## **Make abusing token privilege great again**

• We can use arbitrary increment primitive to • Increase nt!SeDebugPrivilege to 0x17

Nt
SeDebugPrivilege
0x17
V1 == 0x14

199

## Slide 199

## **Make abusing token privilege great again**

#### • Not only nt!SeDebugPrivilege, but …

- SeTcbPrivilege = 0x7

- SeTakeOwnershipPrivilege = 0x9

- SeLoadDriverPrivilege = 0xa

- …

200

## Slide 200

201

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Help
Library Home Windows 11 23H2
Computer
FE command Prompt x + ¥
Microsoft Windows [Version 10.0.22631.3527]
(c) Microsoft Corporation. All rights reserved.
C:\Users\p20>
DEVCORE
201
```

## Slide 201

## **Proxying to Kernel again !**

202

## Slide 202

203

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Exploitability
The following table provides an exploitability assessment for this vulnerability at the time of original publication.
Publicly disclosed
No
Exploited
NO
Exploitability assessment
Exploitation Less Likely
» EXPLOTATION
© LESS LIKELY
DEVCORE Ge
203
```

## Slide 203

## **The Next**

204

## Slide 204

## **The Next**

• The Overlook bug class • It may be possible to find more related proxy type bug • IoBuildDeviceIoControlRequest

• IofCallDriver

• ...

• The timing of setting Irp->RequestorMode to KernelMode is very important.

205

## Slide 205

## **The Next**

- The Attack Surface

   - kernel streaming has many components

      - Low-hanging fruit

         - Hdaudio.sys

         - Usbvideo.sys

• …

206

## Slide 206

## **Takeaways**

• Looking at historical vulnerabilities is indispensable • When current exploitation methods no longer work, explore the core mechanics - you may discover new approaches.

207

## Slide 207

## **Is that the end of it ?**

208

## Slide 208

CVE

2024

38125

CVE

2024

38056

CVE

2024

38055

CVE

2024

CVE

2024

38054

CVE

2024

38144

CVE

2024

CVE

2024

38052

CVE

2024

35250

CVE

2024

30090

CVE

2024

38057

38191

30084

209

## Slide 209

## **To Be Continued …**

210

## Slide 210

# **Thanks!**

scwuaptx angelboy@devco.re

211
