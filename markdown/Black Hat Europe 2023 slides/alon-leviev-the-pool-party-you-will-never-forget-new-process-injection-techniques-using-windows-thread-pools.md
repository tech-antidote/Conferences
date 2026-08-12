---
title: "The Pool Party You Will Never Forget New Process Injection Techniques Using Windows Thread Pools"
speakers: ["Alon Leviev"]
conference: "Black Hat"
conference_full: "Black Hat Europe 2023"
edition: "Europe"
year: 2023
source_pdf: "Black Hat Europe 2023 slides/Alon Leviev_The Pool Party You Will Never Forget New Process Injection Techniques Using Windows Thread Pools.pdf"
pages: 118
sha256: "e664dd1b88e08f1eb849fb171f3da680987176eb5bf135373d4386a6c9b7d08e"
text_chars: 9131
ocr_pages: 33
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:09:59Z"
---
# The Pool Party You Will Never Forget New Process Injection Techniques Using Windows Thread Pools

**Speakers:** Alon Leviev  
**Conference:** Black Hat Europe 2023  
**Source:** `Black Hat Europe 2023 slides/Alon Leviev_The Pool Party You Will Never Forget New Process Injection Techniques Using Windows Thread Pools.pdf` (118 pages)

## Slide 1

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
The Pool Party You
Will Never Forget:
New Process Injection
Techniques Using
Windows Thread Pools
```

## Slide 2

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Alon Leviev
33 SafeBreach
Security Researcher at SafeBreach
21 years old
Self-taught
OS internals, reverse engineering and
vulnerability research
Former BJJ world and european
champion
```

## Slide 3

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Agenda
Process Injection Background
Research Motivation & Questions
Detection Approach
Research Goals
User-mode Thread Pool Deep Dive
Introducing PoolParty
Process Injection Implications
Takeaways
```

## Slide 4

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Process Injection,
Background
```

## Slide 5

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Process Injection Background
Allocate()
Write()
Execute()
Victim Process
&
Attacker Process
```

## Slide 6

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Process Injection Background
VirtualAllocEx()
WriteProcessMemory()
CreateRemoteThread()
Victim Process
&
Attacker Process
oi
```

## Slide 7

## Slide 8

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Motivation
Process injection techniques abuses legitimate
features of the OS
Can an EDR effectively distinguish a legitimate versus
a malicious use of a feature?
Is the current detection approach generic enough?
```

## Slide 9

## Slide 10

## Slide 11

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Detection Approach —
CreateRemotel hread Injection
NtCreateThreadEx (tautacdaeneee)
NtCreateThreadEx(@lnrnaneee)
```

## Slide 12

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Detection Approach — APC Injection
NtQueueApcThread (tite) Ga alger re )
NtQueueApcThread (Reyer) ig ig-ere )
```

## Slide 13

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Detection Approach — Summary
Allocate and write primitives are not detected
Detection is based on execution primitives
Execution primitives gets flag by inspection of
initiator and creator
```

## Slide 14

## Slide 15

▪

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Research Goals
Fully undetectable process
injection techniques
= Applicable against all Windows processes
```

## Slide 16

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
What Ifs
What if the execute primitive is built with write and
allocate primitives?
What if the execution primitive is disguised as a
legitimate action?
```

## Slide 17

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
What Is a Thread Pool?
| wish these
boxes could be
sent in parallel
```

## Slide 18

## Slide 19

## Slide 20

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Why Thread Pool?
All processes have a thread pool by default
Work items and thread pools are represented by
structures
Multiple work item types are supported
```

## Slide 21

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
User-Mode Threa@it™p
Pool Deep Dive
```

## Slide 22

## Slide 23

## Slide 24

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
PoolParty State
No friends in the pool
```

## Slide 25

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
=adClones
Attacking Worker@i™™y
```

## Slide 26

## Slide 27

**Create Shutdown**

**Query Set Ready Wait Release**

## Slide 28

|`NTSTATUS NTAPI`**NtCreateWorkerFactory**`(`
`_Out_ PHANDLE WorkerFactoryHandleReturn,`
`_In_ ACCESS_MASK DesiredAccess,`
`_In_opt_ POBJECT_ATTRIBUTES ObjectAttributes,`
`_In_ HANDLE CompletionPortHandle,`|
|---|
|`_In_ HANDLE WorkerProcessHandle,`
`_In_ PVOID StartRoutine,`|
|`_In_opt_ PVOID StartParameter,`|
|`_In_opt_ ULONG MaxThreadCount,`|
|`_In_opt_ SIZE_T StackReserve,`|
|`_In_opt_ SIZE_T StackCommit`
`);`|

## Slide 29

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Attacking Worker Factories
Cc: \Users\User\Desktop\PooLParty>CreateWorkerFactoryByProcessName.exe explorer.exe
[+] target Process ID: 4656
[+] Retrieved handle to the target process: Oxd@
[+] Allocated shellcode memory in the target process: 9@99000003010000
[+] Written shellcode to the target process
[+] Created Worker Factory I/O completion port: Oxcd
[-] NtCreateWorkerFactory failed: The parameter is incorrect.
```

## Slide 30

```
NTSTATUS NTAPI NtCreateWorkerFactory(..., HANDLE WorkerProcessHandle, ...)
{
[snip]
```

```
KPROCESS * pWorkerProcessObject;
ObpReferenceObjectByHandleWithTag(WorkerProcessHandle, ..., &pWorkerProcessObject);
```

**if** `( KeGetCurrentThread()->ApcState.Process != pWorkerProcessObject) {` **return** `STATUS_INVALID_PARAMETER; }`

```
[snip]
```

```
}
```

## Slide 31

## Slide 32

## Slide 33

`NTSTATUS NTAPI` **NtQueryInformationWorkerFactory** `(`

```
_In_ HANDLE WorkerFactoryHandle,
```

```
_In_ QUERY_WORKERFACTORYINFOCLASS WorkerFactoryInformationClass,
_In_reads_bytes_(WorkerFactoryInformationLength) PVOID WorkerFactoryInformation,
_In_ ULONG WorkerFactoryInformationLength,
_Out_opt_ PULONG ReturnLength
```

```
);
```

## Slide 34

```
typedef enum_QUERY_WORKERFACTORYINFOCLASS
{
WorkerFactoryBasicInformation= 7,
```

```
} QUERY_WORKERFACTORYINFOCLASS, * PQUERY_WORKERFACTORYINFOCLASS;
```

## Slide 35

`typedef struct` **_WORKER_FACTORY_BASIC_INFORMATION** `{ [snip] PVOID StartRoutine; [snip]`

- `} WORKER_FACTORY_BASIC_INFORMATION, * PWORKER_FACTORY_BASIC_INFORMATION;`

## Slide 36

`NTSTATUS NTAPI` **NtSetInformationWorkerFactory** `(`

- `_In_ HANDLE WorkerFactoryHandle,`

- `_In_ SET_WORKERFACTORYINFOCLASS WorkerFactoryInformationClass,`

- `_In_reads_bytes_(WorkerFactoryInformationLength) PVOID WorkerFactoryInformation, _In_ ULONG WorkerFactoryInformationLength,`

```
);
```

## Slide 37

**typedef enum** `_SET_WORKERFACTORYINFOCLASS { WorkerFactoryTimeout = 0, WorkerFactoryRetryTimeout = 1, WorkerFactoryIdleTimeout = 2, WorkerFactoryBindingCount = 3, WorkerFactoryThreadMinimum = 4, WorkerFactoryThreadMaximum = 5, WorkerFactoryPaused = 6, WorkerFactoryAdjustThreadGoal = 8, WorkerFactoryCallbackType = 9, WorkerFactoryStackInformation = 10, WorkerFactoryThreadBasePriority = 11, WorkerFactoryTimeoutWaiters = 12, WorkerFactoryFlags = 13, WorkerFactoryThreadSoftMaximum = 14 } SET_WORKERFACTORYINFOCLASS, * PSET_WORKERFACTORYINFOCLASS;`

## Slide 38

## Slide 39

## Slide 40

## Slide 41

## Slide 42

## Slide 43

## Slide 44

## Slide 45

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
PoolParty State
First friend in the pool
```

## Slide 46

## Slide 47

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Why Thread Pool?
Goal Focus of analysis Assumptions
Insert work How work items  Accessto the
itemstoatarget areinserted worker factory
process thread pools of the thread
pool
```

## Slide 48

## Slide 49

## Slide 50

## Slide 51

## Slide 52

typedef struct **_TP_WORK** { **_TPP_CLEANUP_GROUP_MEMBER** CleanupGroupMember; **TP_TASK** Task; **TPP_WORK_STATE** WorkState; **INT32** __PADDING__[1]; } **TP_WORK,** * **PTP_WORK;**

## Slide 53

## Slide 54

```
NTSTATUS NTAPI TpPostTask(TP_TASK* TpTask, TP_POOL* TpPool, int CallbackPriority, …)
{
[snip]
```

```
TPP_QUEUE* TaskQueue= &TpPool->TaskQueue[CallbackPriority];
InsertTailList(&TaskQueue->Queue, &TpTask->ListEntry);
```

- `[snip]`

- `}`

## Slide 55

## Slide 56

## Slide 57

## Slide 58

## Slide 59

## Slide 60

## Slide 61

## Slide 62

## Slide 63

## Slide 64

## Slide 65

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
PoolParty State
Second friend in the pool
```

## Slide 66

## Slide 67

## Slide 68

**Create Open Query Set**

**Remove**

## Slide 69

typedef struct **_TP_IO** { **_TPP_CLEANUP_GROUP_MEMBER** CleanupGroupMember; **TP_DIRECT** Direct; **HANDLE** File; **INT32** PendingIrpCount; **INT32** __PADDING__[1]; } **TP_WORK,** * **PTP_WORK;**

## Slide 70

## Slide 71

```
NTSTATUS NTAPI TpBindFileToDirect(HANDLE hFile, TP_DIRECT* TpDirect, TP_POOL* TpPool)
{
[snip]
FILE_COMPLETION_INFORMATION FileCompletionInfo{ 0 };
FileCompletionInfo.Key= TpDirect;
FileCompletionInfo.Port= TpPool->CompletionPort;
```

```
NtSetInformationFile(
hFile,
&IoStatusBlock,
&FileCompletionInfo,
sizeof(FILE_COMPLETION_INFORMATION),
FileCompletionInformation);
```

```
[snip]
```

```
}
```

## Slide 72

## Slide 73

## Slide 74

## Slide 75

## Slide 76

## Slide 77

## Slide 78

## Slide 79

## Slide 80

## Slide 81

## Slide 82

## Slide 83

## Slide 84

▪ ▪ ▪ ▪

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Attacking Thread Pools - lO, ALPC, JOB. ...
Any TP_DIRECT notification queued to I/O completion queue gets
executed
Notifications can be queued by object operation completion
= File objects (TP_IO)
= ALPC port objects (TP_ALPC)
= Job objects (TP_JOB)
= Waitable objects — (TP_WAIT)
Notifications can be queued directly by NtSetloCompletion system
Call
```

## Slide 85

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
PoolParty State
Five new friends in the pool
```

## Slide 86

## Slide 87

`PTP_TIMER NTAPI` **CreateThreadpoolTimer** `( _In_     PTP_TIMER_CALLBACK TimerCallback, _In_Opt  PVOID TimerContext, _In_Opt  PTP_CALLBACK_ENVIRON TpCallbackEnviron ); void NTAPI` **SetThreadpoolTimer** `( _In_     PTP_TIMER_CALLBACK TimerCallback, _In_Opt  PFILETIME DueTime, _In_     DWORD Period, _In_     DWORD WindowLength );`

## Slide 88

## Slide 89

## Slide 90

## Slide 91

typedef struct  _TP_TIMER
{
[snip]
TPP_PH_LINKS  WindowEndLinks;
TPP_PH_LINKS  WindowStartLinks;
[snip]
}  TP_TIMER,  *  PTP_TIMER ;

## Slide 92

```
NTSTATUSNTAPITppEnqueueTimer(TPP_TIMER_QUEUE*TimerQueue,TP_TIMER*TpTimer)
{
[snip]
TppPHInsert(&TimerQueue->WindowStart,&TpTimer->WindowStartLinks);
TppPHInsert(&TimerQueue->WindowEnd,&TpTimer->WindowEndLinks);
[snip]
}
```

## Slide 93

## Slide 94

## Slide 95

## Slide 96

## Slide 97

## Slide 98

## Slide 99

## Slide 100

## Slide 101

## Slide 102

## Slide 103

## Slide 104

## Slide 105

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
PoolParty State
One new friend in the pool
```

## Slide 106

## Slide 107

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Introducing PoolParty — Supported Variants
Worker Factory Start Routine Overwrite
TP_WORK Insertion
TP_WAIT Insertion
TP_IO Insertion
TP_ALPC Insertion
TP_JOB Insertion
TP_DIRECT Insertion
TP_TIMER Insertion
```

## Slide 108

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Introducing PoolParty — Atfected Products
Palo Alto Cortex @ paloalto’
SentinelOne EDR (ll) Sentinelone
CrowdStrike Falcon \GROWDSTRIKE on a
MicrosoftDefender »
. Microsoft * cate Salary Oo
for Endpoint oe |
CybereasonEDR WD cybereason
ABILITY TO EXECUTE
COMPLETENESS OF VISION - As of October 2022 © Gartner, Ine
Source: Gartner (December 2022)
```

## Slide 109

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Introducing PoolParty - GitHub Repository
https://github.com/SafeBreach-Labs/PoolParty
```

## Slide 110

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Introducing PoolParty - Demo
Retrah_@} Options | th Find handles or DLLs >¢ Syste information X
Frocennen Series Netw Do Lon\Desktop>
ID” er name Desition
Usermode Font Dive Host
sl Security Authority Proce
Chant Server Runtime Process
Winds Legon Appiation
Usermade Font Diver Hest
Window Manager
Ye eplorrece ALON-OESKTOPZAIon Windows Explorer,
Vil emdece [ALON-DESKTOP2\Alen Windows Command Procesor
WB comhoxt exe ALON. OESKTO Console Window Host
Yh emdece [ALON-DESKTOPZ\Alon Windows Command roc
[ALON-DESKTO Console Window Host
‘ALON-DESKTO
Google Crash Handler
Google Crash Handler
1 Googlecrashandlettere
 SecuiyHeathsys2yexe
GD vintoolexe
© onedriveere
[ALON-OESKTO
[ALON-DESKTO Mare
AALON-OESKTOP2Alon —_McrooftOneDive
ace Tole Cre Sev
2) Procenes 157
[CPU Usage 1.90% Physical memany
Untied
View
- Ga
```

## Slide 111

## Slide 112

## Slide 113

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Implications
Process Injection >
```

## Slide 114

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Process Injection Implications —
Evasive Credential Dumping
```

## Slide 115

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Process Injection Implications —
Controlled Folder Access Bypass
BQen02.€BpEaR
```

## Slide 116

## Slide 117

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Takeaways
We need a generic detection approach for
process injections
The impact of process injections is larger than we thought
Enhance your focus on detecting anomalies rather
than placing complete trust in processes based
solely on their identity
```

## Slide 118

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Qa&A
https://github.com/SafeBreach-Labs/PoolParty
@_0OxDeku
bed alon.leviev@safebreach.com
```
