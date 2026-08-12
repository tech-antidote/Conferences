---
title: "From Dead Data to Digestion Extracting Windows Fibers for Your Digital Forensics Diet"
speakers: ["Daniel Jary"]
conference: "Black Hat"
conference_full: "Black Hat USA 2023"
edition: "USA"
year: 2023
source_pdf: "Black Hat USA 2023 slides/Daniel Jary_From Dead Data to Digestion Extracting Windows Fibers for Your Digital Forensics Diet.pdf"
pages: 33
sha256: "eb0627cfb800445ba2d60b79817df5558f958499fbc94caa07aaa8c166a1cc6f"
text_chars: 10533
ocr_pages: 3
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:15:07Z"
---
# From Dead Data to Digestion Extracting Windows Fibers for Your Digital Forensics Diet

**Speakers:** Daniel Jary  
**Conference:** Black Hat USA 2023  
**Source:** `Black Hat USA 2023 slides/Daniel Jary_From Dead Data to Digestion Extracting Windows Fibers for Your Digital Forensics Diet.pdf` (33 pages)

## Slide 1

# From Dead Data to Digestion

Extracting Windows Fibers for your digital forensics diet

## Slide 2

# ID

- Daniel Jary (@JanielDary) – Security researcher

- Previously:

   - Senior security researcher @WithSecure/F-Secure.

   - Security research & endpoint agent developer @UKGov.

   - • IR @Mandiant.

- Professional interests:

   - OS  internals.

   - Reverse engineering.

   - Tool & Sensor Dev.

2

## Slide 3

# Agenda

1 What are Fibers? 2 Abusing Fibers 3 Extracting Fibers from memory

4 Weetabix (Proof of concept tool)

3

## Slide 4

# Glossary

- Heap - An area of memory reserved for data that is created for and used by a process.

- Process Environment Block (PEB) – A data structure that represents information about a process in usermode.

- Thread Environment Block (TEB) – A data structure that provides a Thread’s user-mode representation.

- Thread Information Block (TIB) – First field of the TEB, contains FiberData field & stack information about a thread.

4

## Slide 5

# What are Fibers?

- Microsoft Definition – “A fiber is a unit of execution that must be manually scheduled by the application. Fibers run in the context of the threads that schedule them. Each thread can schedule multiple fibers”.

- My definition:

   - Stackful coroutines.

   - Manually scheduled.

   - Usermode only.

   - 1 Fiber/Thread at any  one time.

- Initial use cases:

   - Databases, server-side applications.

- Modern use cases:

   - Browsers. Audio software plugins.

5

## Slide 6

# What are Fibers?

|**Thread**|**Fiber**|
|---|---|
|Mandatory aspect of any process.|Optional aspect of a thread.|
|At least one Thread / process.|One Fiber / Thread at a time.|
|Unit of execution which the operating system
allocates processor time.|Unit of execution that sits within the context of a
thread object.|
|Usermode & Kernel Object representation.|Usermode only.|
|Managed by the Windows system scheduler.|Manually scheduled by the application.|
|Thread->Thread transition:|Fiber->Fiber transition:|
|•
Requires kernel transition.|•
Occurs in usermode.|
|•
Expensive context switch == More CPU cycles.|•
Cheap context switch == Less CPU cycles.|

6

## Slide 7

# Components & Rules

Components:

•
Fiber Objects – including Fiber Data
•
Fiber Local Storage (FLS):
• Index
• Slots
•
Fiber Callback functions

### Basic Rules:

- ✓ A thread must first convert itself into a fiber.

- ✓ All fibers are equal, no “main” fibers.

- ✓ A fiber is free to create/delete another fiber.

- ✓ Only 1 fiber can run per thread at any time.

7

## Slide 8

# The Windows Fiber API

8

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
The Windows Fiber API
Setup, teardown & scheduling Fiber Local Storage Local inspection
ConvertThreadToFiber() FisAlloc() IsThreadAFiber()
ConvertThreadToFiberEx() FisFree() GetCurrentFiber()
ConvertFiberToThread() FisSetValue() GetFiberData()
DeleteFiber() FisGeiValue()
CreateFiber()
CreateFiberEx()
Switch ToFiber()
```

## Slide 9

# How to use Fibers

1. Thread converts itself to a fiber – ConvertThreadToFiber().

2. Create a second fiber– CreateFiber().

3. (Optional) Allocate FLS – FlsAlloc().

4. Switch to the newly created fiber – SwitchToFiber().

5. When finished, convert a fiber back to a thread – ConvertFiberToThread().

9

## Slide 10

# How to abuse fibers

- Executing shellcode in a local process using fibers:

   1. Convert a Thread to a Fiber.

   2. Allocate memory & copy over shellcode.

   3. Create a new fiber, supply the shellcode address.

   4. Schedule the newly created fiber.

- Fiber Local Storage and callback functions:

   1. Convert a Thread to a Fiber.

   2. Allocate FLS index, suppling an evil callback function.

   _3. (Optional) Set a FLS slot value to use as a callback parameter._

   4. Free the FLS index / Delete fiber.

10

## Slide 11

## Why are fibers appealing to attackers?

11

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Why are fibers appealing to attackers?
*
‘ 1
1 Q?
oO 1
v Vv
Simplicity Obscure & niche Immature detection capability
Easy to use API Threat hunters unlikely to be No Driver supplied callbacks
looking for this
No complex syncronization
objects -
How do they determine what
In-built fiber safety is legitimate/malicious?
No remote enumeration functions
No opensource tools
```

## Slide 12

# Extracting Fibers from Memory

### Goals:

1. Remotely Identify Threads using Fibers.

2. Identify how a Fiber is structured & stored.

3. Associate a Fiber with the correct FLS, Callbacks & TID.

### The challenges:

- No remote enumeration functions.

- No opensource tools.

• Extremely limited documentation. No diagrams, no internals. (One short paragraph below in the whole of the current Windows Internals books!).

12

## Slide 13

# KERNELBASE!IsThreadAFiber

(Associated goal 1/3 - Remotely Identify Threads using Fibers )

### Determines whether the current thread is a fiber. No remote option available:

- Third bit from the SameTebFlags is set == Thread is using Fibers.

### Write our own Fiber program, validate using WinDbg.

### How do we remotely enumerate fibers:

1. CreateToolhelp32Snapshot(TH32CS_SNAPTHREAD, 0) to take a snapshot of all thread IDs.

2. OpenThread() + NtQueryInformationThread() to get THREAD_BASIC_INFORMATION->TebBaseAddress.

3. ReadProcessMemory() to collect TebBaseAddress+SameTebFlags offset.

13

## Slide 14

GetFiberData() & GetCurrentFiber() (Associated goal 2/3 - Identify how a Fiber is structured & stored )

- Macros inside winnt.h.

- GetFiberData():

   - Retrieves the fiber data associated with the current fiber.

   - Value inside TEB.NT_TIB.FiberData field.

- GetCurrentFiber():

   - Returns the address of the current fiber.

   - Address of TEB.NT_TIB.FiberData field.

   - Implicitly reveals the first field in a Fiber Object is the FiberData field.

14

## Slide 15

# After step 1

What  do we now have?

- Address of executing fiber object - (&FiberData).

- Executing fiber data - (*FiberData).

The next step?

- Identify the remaining Fiber Object fields.

- Collect dormant fibers.

15

## Slide 16

KERNELBASE!ConvertThreadToFiber (Associated goal 2/3 - Identify how a Fiber is structured & stored )

What does this tell us?

- Fiber Objects are stored in requested heap allocations of 0x530 bytes.

- Several fields from the TEB/TIB are used to populate a Fiber Object.

16

## Slide 17

# Buildin g out the Fiber object

(Associated goal 2/3 - Identify how a Fiber is structured & stored )

- Decompile remaining setup, teardown & scheduling functions.

- Uncover new fields inside Fiber object.

- Test against our own Fiber C++ program.

=

17

## Slide 18

## Scannin g the NT heap for Fiber objects

( Associated goal 2/3 - Identify how a Fiber is structured & stored )

1. Identify process heaps

3. Decode & enumerate heap entries from segments

5. Collect potential Fiber object heap entries

2. Collect NT heaps & heap segments within

4. Add new requestedBytes field

18

## Slide 19

Validatin g hea p Fiber Objects using FLS (Associated goal 3/3 – Associate Fiber with the correct FLS, Callbacks & TID )

- The FlsData field (in a fiber object) is part of a doubly linked list.

- Which can be used to find Dormant fibers.

- And associate dormant fibers with a thread ID.

19

## Slide 20

# After step 2

What  do we now have?

- A complete Fiber object structure.

- All Fiber objects (both dormant & running) associated with a thread.

The next step?

- Identify the number of FLS indexes in use.

- Identify the FLS slots used by each Fiber.

20

## Slide 21

Extractin g FLS Slot values - NTDLL!RtlFlsGetValue (Associated goal 3/3 – Associate Fiber with the correct FLS, Callbacks & TID )

- The maximum FLS index is 4079.

- FLS slot values can be determined using the FiberData field.

21

## Slide 22

# After step 3

What  do we have?

- Fiber object fields.

- Dormant fiber objects.

- Associated TIDs.

- FLS.

The next step?

- Identify the correct callbacks.

22

## Slide 23

# FLS Callbacks

(Associated goal 3/3 – Associate Fiber with the correct FLS, Callbacks & TID )

- Pointer to FLS callback table exists in the RtlFlsContext member of the linked List.

- Callback table indexes == FLS slot indexes.

23

## Slide 24

# After step 4 – Raw telemetry achieved!

### What  do we have?

- Fiber object fields

- Dormant fiber objects

- Associated TIDs

- FLS

- FLS Callbacks

### Goals :

1. Remotely Identify Threads using Fibers.

2. Identify how  a Fiber is structured & stored.

3. Associate a Fiber with the correct FLS, Callbacks & TID.

24

## Slide 25

## Enrichment of Fiber telemetry for detection purposes

Goals Achieved to generate raw telemetry:

- ✓ Remotely Identify Threads using Fibers.

- ✓ Identify how a Fiber is structured & stored.

- ✓ Associate a Fiber with the correct FLS, Callbacks & TID.

25

## Slide 26

# Weetabix - POC tool

- Written in C++.

- Automates the enumeration of Fibers from currently running threads.

- Applies a set of enrichments to:

   - Fiber Objects

   - FLS

   - Fiber Callback telemetry.

- Outputs data into NDJSON file.

- https://github.com/JanielDary/weetabix

26

## Slide 27

# Detection example – CS Artefact Kit

- June 2022 – Cobalt strike implements thread stack spoofing using Fibers.

- Unorthodox implementation:

   - Single fiber use!

   1. Unbacked FiberData.

   2. No FLS data.

   3. No FLS callbacks.

27

## Slide 28

## Detection example 2 – Callback manipulation

RWX Memory protection

28

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Detection example 2 - Callback manipulation
“fiber_callbacks": [
if
“callback”: 4991471925827290437,
ov “callbackMemProt”™: @,
FisAlloc() — evil callback “callbackMemState”: 4896,
“callbackMemType": 16777216,
_ _— i _ _ @) linen Besser": "C: \\Users\\Dan\\Downloads\\a.d11",
“callbackSymbol"; “",
FESEUETES “callbackUnbackedMem": false,
“index": 6
Delete! hs {
Petes) “callback”: 5@63812098665367116, RWX Memory
@)callbackMemProt” : 64,4 .
“callbackMemState”: 4096, protection
“callbackMemType”: 131072,
“callbackModBaseName": "",
“callbackSymbol": “",
“callbackUnbackedMem": true,
“index": 7
‘ConvertThreadToFiben()
28
```

## Slide 29

# Can we go further?

29

## Slide 30

# Key takeaways

- Threat actors can utilize/target obscure operating system concepts circumvent traditional telemetry, helping them evade blue team functions.

- No telemetry == No detections. So, building purpose-built telemetry is vital to EDR product development!

- Building new telemetry often requires deep understanding, but this can lead to high value low-volume & therefore lowcost solutions especially when deployed over enterprise scale environments.

30

## Slide 31

# Resources

- https://www.geoffchappell.com/

- https://doxygen.reactos.org/

- https://github.com/wine-mirror/wine

- https://devblogs.microsoft.com/oldnewthing/20191011-00/?p=102989

- https://www.open-std.org/JTC1/SC22/WG21/docs/papers/2018/p1364r0.pdf

- William Burgess (@joehowwolf) – “What exactly are Fibers Dan?”

31

## Slide 32

# Thankyou!

**@JanielDary**

**https://github.com/JanielDary/weetabix**

32

## Slide 33

# Questions?

33
