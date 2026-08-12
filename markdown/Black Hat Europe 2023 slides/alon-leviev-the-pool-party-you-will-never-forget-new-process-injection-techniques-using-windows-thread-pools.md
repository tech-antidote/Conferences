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
text_chars: 16845
ocr_pages: 8
has_ocr: true
redacted_secrets: 0
ocr_confidence: 92.7
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 81
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T03:59:53Z"
---
# The Pool Party You Will Never Forget New Process Injection Techniques Using Windows Thread Pools

**Speakers:** Alon Leviev  
**Conference:** Black Hat Europe 2023  
**Source:** `Black Hat Europe 2023 slides/Alon Leviev_The Pool Party You Will Never Forget New Process Injection Techniques Using Windows Thread Pools.pdf` (118 pages)


## Slide 1

The Pool Party You Will Never Forget:New Process Injection Techniques Using Windows Thread Pools

## Slide 2

Alon
Leviev
Security Researcher at
SafeBreach
21 years old
Self
- taughtOS internals, reverse engineering and vulnerability researchFormer BJJ world and
european
champion

## Slide 3

AgendaProcess Injection BackgroundResearch Motivation & QuestionsDetection ApproachResearch Goals
User
-mode Thread Pool Deep DiveIntroducing PoolPartyProcess Injection ImplicationsTakeaways

## Slide 4

## Slide 5

Process Injection Background
Attacker Process
Victim Process
Allocate()
Write()Execute()

## Slide 6

Process Injection Background
Attacker Process
Victim Process
VirtualAllocEx
()
WriteProcessMemory
()
CreateRemoteThread()

## Slide 7

## Slide 8

Motivation
Process injection techniques abuses legitimate features of the OSCan an EDR effectively distinguish a legitimate versus a malicious use of a feature?Is the current detection approach generic enough?

## Slide 9

## Slide 10

Detection Approach
– Spotting Detection Focus
Attacker Process
Victim Process
VirtualAllocEx
()
WriteProcessMemory
()
CreateRemoteThread()
Trusted
Not Trusted
Trusted

## Slide 11

Detection Approach
–
CreateRemoteThread Injection
NtCreateThreadEx(
Current Process
)
NtCreateThreadEx(
Remote Process
)

## Slide 12

NtQueueApcThread
(Local Thread
)
NtQueueApcThread
(Remote Thread
)
Detection Approach
– APC Injection

## Slide 13

Detection Approach
– Summary
Allocate and write primitives are not detectedDetection is based on execution primitivesExecution primitives gets flag by inspection of initiator and creator

## Slide 14

## Slide 15

Research Goals
Fully undetectable process injection techniques
▪Applicable against all Windows processes

## Slide 16

What Ifs
What if the execute primitive is built with write and allocate primitives?What if the execution primitive is disguised as a legitimate action?

## Slide 17


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
What Is a Thread Pool?
| wish these
boxes could be
sent in parallel
```

## Slide 18

## Slide 19

How a Thread Pool Works?
Worker Threads
Work Item
Worker
Work Item
Worker
Work Item
Work Queue

## Slide 20

Why Thread Pool?
All processes have a thread pool by defaultWork items and thread pools are represented by structuresMultiple work item types are supported

## Slide 21

## Slide 22

User
-Mode Thread Pool Architecture
User mode
Kernel mode
Thread Pool
Worker Threads
Task
TppWorkerThread
Task
TppWorkerThread
TP_POOL Task Queue
TP_POOL Timer Queue
Worker Threads Manager
Worker Factory
I/O Completion Queue
I/O
Timer
Task

## Slide 23

Defining Attack Surface
User mode
Kernel mode
Thread Pool
Worker Threads
Task
TppWorkerThread
Task
TppWorkerThread
TP_POOL Task Queue
TP_POOL Timer Queue
Worker Threads Manager
Worker Factory
I/O Completion Queue
I/O
Timer
Task

## Slide 24

## Slide 25

## Slide 26

Worker Factories Introduction
Worker Threads
Worker Factory Object
…
Manage Worker Threads
1Worker
2Worker
3Worker
Who blocks?Who is active?Who is inactive?

## Slide 27

Worker Factories System Calls
NtQueryInformationWorkerFactoryNtSetInformationWorkerFactory
NtCreateWorkerFactoryNtShutdownWorkerFactory
NtWorkerFactoryWorkerReadyNtWaitForWorkViaWorkerFactoryNtReleaseWorkerFactoryWorker
Create
Shutdown
Query
Set
Ready
Wait
Release

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


> Recovered by OCR — confidence 90/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Attacking Worker Factories
[+] target Process ID: 4656
[+] Retrieved handle to the target process: Oxd@
[+] Allocated shellcode memory in the target process: 9@99000003010000
[+] Written shellcode to the target process
[+] Created Worker Factory I/O completion port: Oxcd
[-] NtCreateWorkerFactory failed: The parameter is incorrect.
```

## Slide 30

\```
NTSTATUS NTAPI NtCreateWorkerFactory(..., HANDLE WorkerProcessHandle, ...)
{
[snip]
\```

\```
KPROCESS * pWorkerProcessObject;
ObpReferenceObjectByHandleWithTag(WorkerProcessHandle, ..., &pWorkerProcessObject);
\```

**if** `( KeGetCurrentThread()->ApcState.Process != pWorkerProcessObject) {` **return** `STATUS_INVALID_PARAMETER; }`

\```
[snip]
\```

\```
}
\```

## Slide 31

Attacking Worker Factories
Attacker Process
Victim Process
DuplicateHandle
( )
Duplicate Worker Factory handle
Worker Factory

## Slide 32

Attacking Worker Factories
Worker Factory Object
…
Start Routine
0 xcafebabe
WriteProcessMemory
( 0 xcafebabe
)
Execute

## Slide 33

`NTSTATUS NTAPI` **NtQueryInformationWorkerFactory** `(`

\```
_In_ HANDLE WorkerFactoryHandle,
\```

\```
_In_ QUERY_WORKERFACTORYINFOCLASS WorkerFactoryInformationClass,
_In_reads_bytes_(WorkerFactoryInformationLength) PVOID WorkerFactoryInformation,
_In_ ULONG WorkerFactoryInformationLength,
_Out_opt_ PULONG ReturnLength
\```

\```
);
\```

## Slide 34

\```
typedef enum_QUERY_WORKERFACTORYINFOCLASS
{
WorkerFactoryBasicInformation= 7,
\```

\```
} QUERY_WORKERFACTORYINFOCLASS, * PQUERY_WORKERFACTORYINFOCLASS;
\```

## Slide 35

`typedef struct` **_WORKER_FACTORY_BASIC_INFORMATION** `{ [snip] PVOID StartRoutine; [snip]`

- `} WORKER_FACTORY_BASIC_INFORMATION, * PWORKER_FACTORY_BASIC_INFORMATION;`

## Slide 36

`NTSTATUS NTAPI` **NtSetInformationWorkerFactory** `(`

- `_In_ HANDLE WorkerFactoryHandle,`

- `_In_ SET_WORKERFACTORYINFOCLASS WorkerFactoryInformationClass,`

- `_In_reads_bytes_(WorkerFactoryInformationLength) PVOID WorkerFactoryInformation, _In_ ULONG WorkerFactoryInformationLength,`

\```
);
\```

## Slide 37

**typedef enum** `_SET_WORKERFACTORYINFOCLASS { WorkerFactoryTimeout = 0, WorkerFactoryRetryTimeout = 1, WorkerFactoryIdleTimeout = 2, WorkerFactoryBindingCount = 3, WorkerFactoryThreadMinimum = 4, WorkerFactoryThreadMaximum = 5, WorkerFactoryPaused = 6, WorkerFactoryAdjustThreadGoal = 8, WorkerFactoryCallbackType = 9, WorkerFactoryStackInformation = 10, WorkerFactoryThreadBasePriority = 11, WorkerFactoryTimeoutWaiters = 12, WorkerFactoryFlags = 13, WorkerFactoryThreadSoftMaximum = 14 } SET_WORKERFACTORYINFOCLASS, * PSET_WORKERFACTORYINFOCLASS;`

## Slide 38

Attacking Worker Factories
Worker Threads
Worker Factory Object
…
Minimum Threads
2
NtSetInformationWorkerFactory
(Running Threads Num +
1 )
Execute
1Worker
2Worker

## Slide 39

Attacking Worker Factories
Worker Threads
Worker Factory Object
…
Minimum Threads
3
Create new worker thread
1Worker
2Worker
3Worker

## Slide 40

Attacking Worker Factories
Attacker Process
Victim Process
NtQueryInformationProcess
( )
Get handle table
Start Routine

## Slide 41

Attacking Worker Factories
Attacker Process
Victim Process
DuplicateHandle()
Duplicate Worker Factory handle
Start Routine

## Slide 42

Attacking Worker Factories
Attacker Process
Victim Process
NtQueryInformationWorkerFactory( )
Get Worker Factory info
Start Routine

## Slide 43

Attacking Worker Factories
Attacker Process
Victim Process
WriteProcessMemory( )
Start Routine
Write shellcode to start routine

## Slide 44

Attacking Worker Factories
Attacker Process
Victim Process
NtSetWorkerFactoryInformation( )
Start Routine
Increase worker factory minimum threads

## Slide 45

## Slide 46

## Slide 47

Why Thread Pool?
GoalInsert work items to a target process
Focus of analysisHow work items are insertedthread pool
s
Assumptions
Access
to the
worker factory of the thread pool

## Slide 48

Attacking Thread Pools
- Work Item Types
TP_IO
TP_WAIT
TP_JOB
TP_ALPC
Regular Work Items
Asynchronous Work Items
TP_TIMER
Timer Work Items
TP_WORK

## Slide 49

Attacking Thread Pools
- Queue Types
Regular work items are queued here
TP_POOL Task Queue
Asynchronous work items are queued here
I/O Completion Queue
Timer work items are queued here
TP_POOL Timer Queue

## Slide 50

User
-Mode Thread Pool
- Helper Structures
Work Item Structure
…
Cleanup Group Structure
…
Helper Structure
…
Helper Callback
…
Helper Structure
…
Cleanup Group Structure
…
Work Item Callback
…
Queue Helper Structure
Helper Executes Callback

## Slide 51

Attacking Thread Pools
TP_IO
TP_WAIT
TP_JOB
TP_ALPC
Regular Work Items
Asynchronous Work Items
TP_TIMER
TP_WORK
Timer Work Items

## Slide 52

typedef struct **_TP_WORK** { **_TPP_CLEANUP_GROUP_MEMBER** CleanupGroupMember; **TP_TASK** Task; **TPP_WORK_STATE** WorkState; **INT32** __PADDING__[1]; } **TP_WORK,** * **PTP_WORK;**

## Slide 53

Attacking Thread Pools
- TP_WORK
SubmitThreadpoolWork
TpPostWork
kernel
32
ntdll
TppWorkPost
TpPostTask

## Slide 54

\```
NTSTATUS NTAPI TpPostTask(TP_TASK* TpTask, TP_POOL* TpPool, int CallbackPriority, …)
{
[snip]
\```

\```
TPP_QUEUE* TaskQueue= &TpPool->TaskQueue[CallbackPriority];
InsertTailList(&TaskQueue->Queue, &TpTask->ListEntry);
\```

- `[snip]`

- `}`

## Slide 55

Attacking Thread Pools
- TP_WORK
Task Queue
Flink
Head
Tail
TP_TASK
1
Blink
Flink
TP_TASK
2
Blink
Flink
TP_TASK
3
Blink
TpPostTask( )
Execute
Flink
TP_TASK
Blink

## Slide 56

Task Queue
Attacking Thread Pools
- TP_WORK
Flink
Queue task
Head
Tail
TP_TASK
1
Blink
Flink
TP_TASK
2
Blink
Flink
TP_TASK
3
Blink
Flink
TP_TASK
4
Blink

## Slide 57

Attacking Thread Pools
– TP_WORK
Attacker Process
Victim Process
NtQueryInformationProcess( )
Get handle table
TP_POOL Task Queue

## Slide 58

Attacking Thread Pools
– TP_WORK
Attacker Process
Victim Process
DuplicateHandle()
Duplicate Worker Factory handle
TP_POOL Task Queue

## Slide 59

Attacking Thread Pools
– TP_WORK
Attacker Process
Victim Process
NtQueryInformationWorkerFactory( )
Get Worker Factory info
TP_POOL Task Queue

## Slide 60

Attacking Thread Pools
– TP_WORK
Attacker Process
Victim Process
ReadProcessMemory( )
Read TP_POOL
TP_POOL Task Queue

## Slide 61

Attacking Thread Pools
– TP_WORK
Attacker Process
Victim Process
CreateThreadpoolWork( )
TP_WORK
TP_POOL Task Queue

## Slide 62

Attacking Thread Pools
– TP_WORK
Attacker Process
Victim Process
VirtualAllocEx( )
TP_WORK
Allocate TP_WORK memory
TP_WORK
TP_POOL Task Queue

## Slide 63

Attacking Thread Pools
– TP_WORK
Attacker Process
Victim Process
WriteProcessMemory( )
TP_WORK
Write TP_WORK memory
TP_POOL Task Queue

## Slide 64

Attacking Thread Pools
– TP_WORK
Attacker Process
TP_POOL Task Queue
Victim Process
WriteProcessMemory( )
TP_WORK
Insert TP_WORK to TP_POOL task queue

## Slide 65


> Recovered by OCR — confidence 96/100 on the text kept, 96/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Second friend in the pool
```

## Slide 66

Attacking Thread Pools
TP_IO
TP_WAIT
TP_JOB
TP_ALPC
Regular Work Items
Asynchronous Work Items
TP_TIMER
TP_WORK
Timer Work Items

## Slide 67

I/O Completion Ports Introduction
I/O Operation
…
Completion Queue
…
Queue Notification
Completion Notification
I/O Completion Queue
…
Completion Notification
Completed

## Slide 68

I/O Completion Queues System Calls
NtOpenIoCompletion
NtQueryIoCompletionNtQueryIoCompletionExNtSetIoCompletionNtSetIoCompletionEx
Open
Query
Set
NtCreateIoCompletion
Create
NtRemoveIoCompletionNtRemoveIoCompletionEx
Remove

## Slide 69

typedef struct **_TP_IO** { **_TPP_CLEANUP_GROUP_MEMBER** CleanupGroupMember; **TP_DIRECT** Direct; **HANDLE** File; **INT32** PendingIrpCount; **INT32** __PADDING__[1]; } **TP_WORK,** * **PTP_WORK;**

## Slide 70

Attacking Thread Pools
- TP_IO
CreateThreadpoolIo
TpAllocIoComplet
io n
TpBindFileToDirect
kernel
32
ntdll

## Slide 71

\```
NTSTATUS NTAPI TpBindFileToDirect(HANDLE hFile, TP_DIRECT* TpDirect, TP_POOL* TpPool)
{
[snip]
FILE_COMPLETION_INFORMATION FileCompletionInfo{ 0 };
FileCompletionInfo.Key= TpDirect;
FileCompletionInfo.Port= TpPool->CompletionPort;
\```

\```
NtSetInformationFile(
hFile,
&IoStatusBlock,
&FileCompletionInfo,
sizeof(FILE_COMPLETION_INFORMATION),
FileCompletionInformation);
\```

\```
[snip]
\```

\```
}
\```

## Slide 72

Attacking Thread Pools
- TP_IO
File Object
…
Completion Queue
NULLCompletion Key
NULL
I/O Completion Queue
…
TpBindFileToDirect( )
Execute

## Slide 73

Attacking Thread Pools
- TP_IO
File Object
…
Completion Queue
TpPool
- > CompletionPortCompletion Key
TpIo
- >Direct
I/O Completion Queue
…

## Slide 74

Attacking Thread Pools
- TP_IO
File Object
…
Completion Queue
TpPool
- > CompletionPortCompletion Key
TpIo
- >Direct
I/O Completion Queue
…
WriteFile( )
Execute

## Slide 75

Attacking Thread Pools
- TP_IO
File Object
…
Completion Queue
TpPool
- > CompletionPort
Completion Notification
TpIo
- >Direct
Queue Notification
Completion Key
TpIo
- >Direct
I/O Completion Queue
…

## Slide 76

Attacking Thread Pools
- TP_IO
Attacker Process
Victim Process
NtQueryInformationProcess()
I/O Completion
Queue
Get handle table

## Slide 77

Attacking Thread Pools
- TP_IO
Attacker Process
Victim Process
I/O Completion
Queue
DuplicateHandle()
Duplicate I/O Completion queue handle

## Slide 78

Attacking Thread Pools
- TP_IO
Attacker Process
Victim Process
I/O Completion
Queue
File
CreateFile( )

## Slide 79

Attacking Thread Pools
- TP_IO
Attacker Process
TP_IO
File
Victim Process
CreateThreadpoo
l I o ( )
I/O Completion
Queue

## Slide 80

Attacking Thread Pools
- TP_IO
Attacker Process
TP_IO
File
Victim Process
VirtualAllocEx( )
I/O Completion
Queue
TP_IO
Allocate TP_IO memory

## Slide 81

Attacking Thread Pools
- TP_IO
Attacker Process
File
Victim Process
WriteProcessMemory( )
Write TP_IO memory
TP_IO
I/O Completion
Queue

## Slide 82

Attacking Thread Pools
- TP_IO
Attacker Process
TP_IO
File
Victim Process
NtSetInformationFile
( )
I/O Completion
Queue
Associate TP_IO with target I/O completion queue

## Slide 83

Attacking Thread Pools
- TP_IO
Attacker Process
File
Victim Process
WriteFile( )
TP_IO
I/O Completion
Queue
Queue notification to I/O completion queue

## Slide 84

Any TP_DIRECT notification queued to I/O completion queue gets executedNotifications can be queued by object operation completion
▪File objects (TP_IO)
▪ALPC port objects (TP_ALPC)
▪Job objects (TP_JOB)
▪Waitable objects
– (TP_WAIT)
Notifications can be queued directly by
NtSetIoCompleti
o n system
call
Attacking Thread Pools
- IO, ALPC, JOB,
…

## Slide 85


> Recovered by OCR — confidence 96/100 on the text kept, 96/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Five new friends in the pool
```

## Slide 86

Attacking Thread Pools
TP_IO
TP_WAIT
TP_JOB
TP_ALPC
Regular Work Items
Asynchronous Work Items
TP_TIMER
TP_WORK
Timer Work Items

## Slide 87

`PTP_TIMER NTAPI` **CreateThreadpoolTimer** `( _In_     PTP_TIMER_CALLBACK TimerCallback, _In_Opt  PVOID TimerContext, _In_Opt  PTP_CALLBACK_ENVIRON TpCallbackEnviron ); void NTAPI` **SetThreadpoolTimer** `( _In_     PTP_TIMER_CALLBACK TimerCallback, _In_Opt  PFILETIME DueTime, _In_     DWORD Period, _In_     DWORD WindowLength );`

## Slide 88

Attacking Thread Pools
– TP_TIMER
Timer Work Item
…
Queue Link
…
Timer Queue
…
Queue
…
Timer Handle
…
SetThreadpoolTimer( )
Execute

## Slide 89

Attacking Thread Pools
– TP_TIMER
Timer Work Item
…
Queue Link
…
Timer Queue
…
Queue
…
Timer Handle
…
Set Queue Timer

## Slide 90

Attacking Thread Pools
– TP_TIMER
Timer Work Item
…
Queue Link
…
Timer Queue
…
Queue
…
Timer Handle
…
Execute Dequeuing Function
Timer Is Expired

## Slide 91

typedef struct  _TP_TIMER
{
[snip]
TPP_PH_LINKS  WindowEndLinks;
TPP_PH_LINKS  WindowStartLinks;
[snip]
}  TP_TIMER,  *  PTP_TIMER ;

## Slide 92

\```
NTSTATUSNTAPITppEnqueueTimer(TPP_TIMER_QUEUE*TimerQueue,TP_TIMER*TpTimer)
{
[snip]
TppPHInsert(&TimerQueue->WindowStart,&TpTimer->WindowStartLinks);
TppPHInsert(&TimerQueue->WindowEnd,&TpTimer->WindowEndLinks);
[snip]
}
\```

## Slide 93

Attacking Thread Pools
– TP_TIMER
Timer Queue
…
Window Start
NULLWindow End
NULL
Timer Work Item
…
Window Start Links
…
Window End Links
…
TppEnqueueTimer( )
Execute

## Slide 94

Attacking Thread Pools
– TP_TIMER
Timer Queue
…
Window Start
Timer
->WindowStartLinksWindow End
Timer
->WindowEndLinks
Timer Work Item
…
Window Start Links
…
Window End Links
…

## Slide 95

Attacking Thread Pools
– TP_TIMER
Attacker Process
Victim Process
NtQueryInformationProcess( )
Get handle table
TP_POOL Timer Queue

## Slide 96

Attacking Thread Pools
– TP_TIMER
Attacker Process
Victim Process
DuplicateHandle( )
Duplicate Worker Factory handle
TP_POOL Timer Queue

## Slide 97

Attacking Thread Pools
– TP_TIMER
Attacker Process
Victim Process
NtQueryInformationWorkerFactory( )
Get Worker Factory info
TP_POOL Timer Queue

## Slide 98

Attacking Thread Pools
– TP_TIMER
Attacker Process
Victim Process
ReadProcessMemory( )
Read TP_POOL
TP_POOL Timer Queue

## Slide 99

Attacking Thread Pools
– TP_TIMER
Attacker Process
Victim Process
CreateThreadpoolTimer( )
TP_TIMER
TP_POOL Timer Queue

## Slide 100

Attacking Thread Pools
– TP_TIMER
Attacker Process
Victim Process
VirtualAllocEx( )
TP_POOL Timer Queue
Allocate TP_TIMER memory
TP_TIMER
TP_TIMER

## Slide 101

Attacking Thread Pools
– TP_TIMER
Attacker Process
Victim Process
WriteProcessMemory( )
TP_TIMER
Write TP_TIMER memory
TP_POOL Timer Queue

## Slide 102

Attacking Thread Pools
– TP_TIMER
Attacker Process
Victim Process
WriteProcessMemory( )
TP_TIMER
Insert TP_TIMER to TP_POOL timer queue
TP_POOL Timer Queue

## Slide 103

Attacking Thread Pools
– TP_TIMER
Attacker Process
Victim Process
DuplicateHandle( )
TP_TIMER
Duplicate queue timer handle
TP_POOL Timer Queue

## Slide 104

Attacking Thread Pools
– TP_TIMER
Attacker Process
Victim Process
NtSetTimer
2 ( )
TP_TIMER
Set queue timer to expire
TP_POOL Timer Queue

## Slide 105


> Recovered by OCR — confidence 96/100 on the text kept, 96/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
One new friend in the pool
```

## Slide 106

## Slide 107

Introducing PoolParty
– Supported Variants
1 Worker Factory Start Routine Overwrite
2 TP_WORK Insertion
3 TP_WAIT Insertion
4 TP_IO Insertion
5 TP_ALPC Insertion
6 TP_JOB Insertion
7 TP_DIRECT Insertion
8 TP_TIMER Insertion

## Slide 108

Palo Alto CortexSentinelOne
EDR
CrowdStrike FalconMicrosoft Defender for EndpointCybereason EDR
Introducing
PoolParty
– Affected Products

## Slide 109

Introducing PoolParty
- GitHub Repository
https://github.com/SafeBreach
-Labs/PoolParty

## Slide 110


> Recovered by OCR — confidence 87/100 on the text kept, 40/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Introducing PoolParty - Demo
Window Manager
Untied
View
```

## Slide 111

## Slide 112

## Slide 113

## Slide 114


> Recovered by OCR — confidence 92/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Process Injection Implications —
Evasive Credential Dumping
```

## Slide 115


> Recovered by OCR — confidence 92/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Process Injection Implications —
Controlled Folder Access Bypass
```

## Slide 116

## Slide 117

Takeaways
We need a generic detection approach for process injectionsThe impact of process injections is larger than we thoughtEnhance your focus on detecting anomalies rather than placing complete trust in processes based solely on their identity

## Slide 118

Q & A
@_
0 xDekuhttps://il.linkedin.com/in/alonlevievalon.leviev@safebreach.com
https://github.com/SafeBreach
-Labs/PoolParty
