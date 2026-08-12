---
title: "Kill Latest MPU-based Protections in Just One Shot Targeting All Commodity RTOSes"
speakers: ["Yueqi Chen", "Minghao Lin", "Chaoyang Lin", "Jiahe Wang", "Zicheng Wang", "Minghang Shen"]
conference: "Black Hat"
conference_full: "Black Hat USA 2023"
edition: "USA"
year: 2023
source_pdf: "Black Hat USA 2023 slides/Yueqi Chen,Minghao Lin,Chaoyang Lin,Jiahe Wang,Zicheng Wang,Minghang Shen_Kill Latest MPU-based Protections in Just One Shot Targeting All Commodity RTOSes.pdf"
pages: 41
sha256: "0fdd6963ae5b47440b9addb6d1422b296aeda552a9592e2fb8f4a5ebed3fcf12"
text_chars: 13766
ocr_pages: 2
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:26:27Z"
---
# Kill Latest MPU-based Protections in Just One Shot Targeting All Commodity RTOSes

**Speakers:** Yueqi Chen, Minghao Lin, Chaoyang Lin, Jiahe Wang, Zicheng Wang, Minghang Shen  
**Conference:** Black Hat USA 2023  
**Source:** `Black Hat USA 2023 slides/Yueqi Chen,Minghao Lin,Chaoyang Lin,Jiahe Wang,Zicheng Wang,Minghang Shen_Kill Latest MPU-based Protections in Just One Shot Targeting All Commodity RTOSes.pdf` (41 pages)


## Slide 1

### **Kill Latest MPU-based Protections in Just One Shot: Targeting All Commodity RTOSes**

**Speaker: Minghao Lin**

#BHUSA   @BlackHatEvents

## Slide 2

## Who We Are

Minghao Lin, Professional Research Assistant, , University of Colorado Boulder

Yueqi Chen, Assistant Professor,  University of Colorado Boulder

Zicheng Wang, Professional Research Assistant, University of Colorado Boulder

**2**

#BHUSA  @BlackHatEvents

## Slide 3

## Who We Are

Minghang Shen, Independent Security Researcher

Chaoyang Lin, Independent Security Researcher

Jiahe Wang, Independent Security Researcher

**3**

#BHUSA  @BlackHatEvents

## Slide 4

## Real Time Operating Systems Are Everywhere

**4**

#BHUSA  @BlackHatEvents

## Slide 5

## MPU is Commonly Found in RTOSes

**5**

Source: Abbasi, Ali, et al. "Challenges in designing exploit mitigations for deeply embedded systems." _2019 IEEE European Symposium on Security and Privacy (EuroS&P)_ . IEEE, 2019.

#BHUSA  @BlackHatEvents

## Slide 6

## Memory Protection Unit (MPU)

U : Unprivilieged P : Privileged

- Hardware feature commonly found in microcontrollers and processors

- Functionality

   - Manage the access **permissions** and attributes, e.g., R/W of different regions in memory according execution state, i.e., Privileged (P) or Unprivileged (U)

   - Fault occurs when access permission is violated

Flash
RAM
Region A ( P :R-X)
U  Task
Region B ( PU :RWX)
Region C ( U :RX)

**6** #BHUSA  @BlackHatEvents

## Slide 7

## An Exploitation Case

- Over The Air Update

Send malicious updated file
Internet

**Speakers: Omri Ben-Bassat, Tamir Ariel**

Server

IOT devices

**7**

#BHUSA  @BlackHatEvents

## Slide 8

## An Exploitation Case

- Vulnerability Details

1. GetEntireFile() function is used to parse the file sent through Internet

2. FileSize could be very large before malloc, causing integer overflow and thereby a **small allocated memory**

Integer Overflow

3. Followed by Heap overflow caused by memcpy Heap Overflow

**8**

#BHUSA  @BlackHatEvents

## Slide 9

## An Exploitation Case

- Find Function Pointer to Overwrite

- httpGetHandler function is used to handle different types of http requests

- httpRequest is an array of http handler function pointers

- Overwrite function pointer of the arrary to point shellcode

Http handler function pointers

**9**

#BHUSA  @BlackHatEvents

## Slide 10

## An Exploitation Case - Heap Layout

Next
Next
Free
Size Vulnerable object Size Free
Bloc
Block
k
Original Heap Layout
RWX (R: Read W: Write X: Executable)
Allocated Free

**10**

#BHUSA  @BlackHatEvents

## Slide 11

## An Exploitation Case - MPU Disables this Exploitation

MPU Disables this Exploitation
MPU
Func Next Func Next Next
YYYYYYYYYYYYYYYYYYYYVulnerable object Size Ptr AddrBlockFree Data Size FuncPtr YYYYYYYYYYYYYYYYYYYYVuln obj Size Ptr AddrBlockFree Data Size BlockFuncFreePtr Data
RWX (R: Read W: Write X: Executable) NX (Non-Executable)
Allocate Free Shellcode

Allocate Free Shellcode

**11**

#BHUSA  @BlackHatEvents

## Slide 12

MPU becomes a
terminator for
exploitation?

**12**

#BHUSA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
USA 20253
MPU becomes a
terminator for
exploitation?
E>. y | ae)
```

## Slide 13

No!

**13**

#BHUSA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
USA 20253
(@81OS)| TIZEN
“OM aT -Thread
A  oarm
Zephyr’ ~~ MBED
```

## Slide 14

You first!

**14**

#BHUSA  @BlackHatEvents

## Slide 15

## Privilege Isolation In FreeRTOS Using MPU

   Background Region | P:RW
General peripherals region MPU Region 4 | PU:RW-XN
MPU Region 5 | PU:R
Unprivileged flash region Trampoline functions, Task
code
MPU Region 3 | PU:RW-XN
Task stack regionprivileged data MPU_0 MPU_1 MPU_2
Task stack
MPU Region 6 | P:R
Privileged flash region
Kernel code
MPU Region 7 | P:RW-XN
Privileged data region
Kernel stack, heap
Predefined regions User-defined regions

**15**

**MPU region definitions of ARM-CM3 FreeRTOS-MPU**

#BHUSA  @BlackHatEvents

## Slide 16

## Memory View Per Task

1. Every Task has their own access permission and execution state

2. When task switching happens, MPU configuration will be changed to the specific task

Task switching U : Unprivilieged P : Privileged

Kernel code  Kernel code
and data and data
Stack for task A Stack for task ( P ) A
Stack for task ( U ) B Stack for task B
Stack for task C Stack for task C
Executing unprivileged task B Executing privileged task A

Not accessible

**16**

#BHUSA  @BlackHatEvents

## Slide 17

- Issue 1 Missing Legitimacy Check During Mode Switch - Overview of Trampoline Function

- In FreeRTOS, kernel functions are wrapped by trampoline functions with “MPU_” prefix, which play the role as a trampoline for switching from user mode to kernel mode

- Non-privileged tasks can call these trampoline functions to request kernel service

Task A Task B
Trampoline
Functions
Kernel services
Unprivileged
Privileged

**17**

#BHUSA  @BlackHatEvents

## Slide 18

- Issue 1 Missing Legitimacy Check During Mode Switch - Implementation of Trampoline Function

1. Check if current execution state is privileged or not

2. If not, it will raise privilege, then call the kernel function. Finally, it will drop privilege

3. If current execution state is privileged, it will directly call kernel function

4. No check for parameters of MPU_vTaskGetInfo

**18**

#BHUSA  @BlackHatEvents

## Slide 19

Issue 1 Missing Legitimacy Check During Mode Switch - Arbitrary Read or Write in vTaskGetInfo

1. Unprivileged task can pass two arbitrary pointers to parameters xTask and pxTaskStatus

2. Then, pxTCB is later assigned as xTask

3. pxTaskStatus and pxTCB is dereferenced → arbitrary read from or write to any pointers

xTask == NULL ? xTask : current TCB

**19**

#BHUSA  @BlackHatEvents

## Slide 20

Issue 1 Missing Legitimacy Check During Mode Switch - Privilege Escalation

- A task is privileged or not depends on the value stored in top of its stack

- When task switching happens, CTROL will be set to the execution state of the next task

- Leverage arbitrary write to modify the execution state value to be privileged

P : Privileged U : Unprivileged CTROL : Control register

Task (P) A

The execution state value (U) stored in the top of  Task B’s stack is assigned to CTROL

Task switching

**Modify execution state value of task C**

Task (U) B

The execution state value (P) The execution state value (U) Task Task stored in the top of  Task C’s stored in the top of  Task C’s switching switching stack is assigned to CTROL stack is assigned to CTROL

Task (U) C

Task (P) C

**20**

#BHUSA  @BlackHatEvents

## Slide 21

Issue 1 Missing Legitimacy Check During Mode Switch - Trampoline Functions DoS Other Tasks

U : Unprivilieged
P : Privileged
Trampoline  Task (U) A
Functions
Task (U) B
DoS
Task (P) C
DoS

TaskControlBlock
pointer
Suspend other tasks

Memory Map

**21**

#BHUSA  @BlackHatEvents

## Slide 22

## MPU Region Overlapping

0x4000

- The two regions have different permissions, the permissions associated with region 2 are applied

- ● For overlapping regions, a fixed priority scheme determines attributes and permissions for memory access to the overlapping region

0x3000

Region 2 P:RW

Region 1 PU: RW

2 > 1

0x0000

**22**

#BHUSA  @BlackHatEvents

## Slide 23

## Issue 2 Mistaken MPU Configuration

MPU Region 0~2 are user-defined MPU regions

1. When creating a child task, the parent task can configure MPU 0-2 regions of child task

Trampoline
functions Task A
Background region
Memory of task C
Overlapping regionMPU region 0~2
Create
Malicious task B Memory of task BSensitive data of
task
task C
Victim task C

2. Unfortunately, the FreeRTOS kernel doesn’t examine if this configuration has conflict with other tasks, resulting in memory overlapping between tasks

3. Adversaries can exploit this mistake to access the memory of victim tasks, stealing or tampering critical data

**23**

#BHUSA  @BlackHatEvents

## Slide 24

## Report to Amazon Team And Got Response

2023-04-06 2023-05-17 2023-07-16
2023-03-17
Provide automatic  Audited the source  Audited the source
Submit the vuln
tool and analysis  code and  code and
report
results with  discovered some  discovered some
Amazon team issues issues again
2023-03-21 2023-05-16 2023-05-27 2023-07-06
2023-07-18
Virtual call to Provide source  Virtual call to  Provide source
Final version of
discuss potential  code of a patched  discuss  code of a patched  FreeRTOS kernel
mitigations FreeRTOS kernel  discovered new  FreeRTOS kernel
for audition issues for audition again

**24**

#BHUSA  @BlackHatEvents

## Slide 25

Amazon Team Mitigations for Fixing These Issues - MPU_xQueueCreateMutex - Limited Trampoline Functions

Unprivileged task

- MPU_xQueueCreateMutexStatic

- MPU_xQueueCreateCountingSemaphore

- MPU_xQueueCreateCountingSemaphoreStatic

- MPU_xQueueGenericCreate

- MPU_xQueueGenericCreateStatic

- MPU_xQueueCreateSet

- MPU_xQueueRemoveFromSet

- MPU_xQueueGenericReset

- MPU_xTaskCreate

- MPU_xTaskCreateStatic

- MPU_vTaskDelete

- MPU_vTaskPrioritySet

- MPU_vTaskSuspendAll

- MPU_xTaskResumeAll

- MPU_xTaskGetHandle

- MPU_xTaskCallApplicationTaskHook

- MPU_vTaskList

- MPU_vTaskGetRunTimeStats

- MPU_xTaskCatchUpTicks

- MPU_xEventGroupCreate

- MPU_xEventGroupCreateStatic

- MPU_vEventGroupDelete

- MPU_xStreamBufferGenericCreate

**25**

#BHUSA  @BlackHatEvents

## Slide 26

Amazon Team Mitigations for Fixing These Issues - Added Function For Checking Access Permissions And Buffer Ranges

Check if the memory is in MPU I want to access region and access permission the memory of the memory is violated by looking up MPU settings

Accessed memory, memory size and access operation read/write

Added Function

**26**

#BHUSA  @BlackHatEvents

## Slide 27

- Amazon Team Mitigations for Fixing These Issues - Replace Object Pointer with Object ID

1. Trampoline functions retrieve objects via ID rather than a raw pointer value

2. Check if the type of object to be retrieved and object ID is valid, if pass check, return an object from the object pool

ID

**27**

#BHUSA  @BlackHatEvents

## Slide 28

Amazon Team Mitigations for Fixing These Issues - Adjust The Location of Context && Privileged Stack for Trampoline Functions

SP: Stack pointer register

1. The task context including execution state value is now stored in TCB which is accessible to privileged code only

2. The trampoline function are now executed on a separate privileged only stack. When a task calls trampoline function, the stack pointer register will change from task stack to privileged only stack.

SP
 Privileged
stack
Task stack

 Privileged
stack
Calling trampoline
function
SP

Task stack

**28**

#BHUSA  @BlackHatEvents

## Slide 29

# How about Other RTOSes?

**29**

#BHUSA  @BlackHatEvents

## Slide 30

You next!

**30**

#BHUSA  @BlackHatEvents

## Slide 31

## Module Concept in ThreadX

- The smallest unit of memory management is a module which comprises a set of tasks

   - MPU 5, 6, 7 for module data

   - MPU 1, 2, 3, 4 for module code

   - MPU 0 for kernel mode entry

- Similar to FreeRTOS, unprivileged tasks call kernel mode entry to request kernel services

Module N Module 1
Task 1 Task 1
Task 2 Task 2
Task 3 Task 3
Kernel mode entry
Kernel services
Unprivileged
Privileged

**31**

#BHUSA  @BlackHatEvents

## Slide 32

## Trampoline Functions in ThreadX

Unprivileged  Kernel mode entry
ALIGN_TYPE _txm_module_manager_kernel_dispatch(ULONG
task
kernel_request , ALIGN_TYPE param_0, ALIGN_TYPE param_1,
ALIGN_TYPE param_2)
{
switch ( kernel_request )
kernel_request that      {
case TXM_BLOCK_ALLOCATE_CALL:
represents different
_txm_module_manager_tx_block_allocate_dispatc
kernel services and
h(...);
case TXM_BLOCK_POOL_CREATE_CALL:
other parameters to
kernel mode entry _txm_module_manager_tx_block_pool_create_disp
atch(...);
. . .
}

**32**

#BHUSA  @BlackHatEvents

## Slide 33

## Trampoline Functions’ Checks in ThreadX

WTF! I can not pass
Check the location of  arbitrary pointers
pointers any more
Check the type
of pointers

**33**

#BHUSA  @BlackHatEvents

## Slide 34

## Trampoline Functions’ Checks in ThreadX (cont.)

Function definition
Check if the thread_ptr is in kernel space
Check if the thread_ptr is valid
34

#BHUSA  @BlackHatEvents

## Slide 35

## Is Trampoline Function in ThreadX Really Secure?

What about a pointer that
matches type and location, but
is just incorrect?

**35**

#BHUSA  @BlackHatEvents

## Slide 36

## An Illustrative Example

Thread 1
1. Malicious thread 1 pass the
pointer of thread2 handler to  Pass
Thread2_PTR
kernel mode entry.
Kernel mode entry
Fail
Return
2. Check if the PTR is in kernel
space and PTR is the
TX_THREAD* class based on
Success
tx_thread_id
Kernel services
Thread2 is
Delete thread 2
destroyed
3. Matches the type and location
Thread2 is destroyed

**36**

#BHUSA  @BlackHatEvents

## Slide 37

Automatic Approach to Identify Similar Issues - Use CodeQL to Do Code Audition

1. The source is the parameters of trampoline function

2. The sink is assign expression including arithmetic and bitwise operation

3. Add additionalTaint. If A object is taint, field B is also taint after accessing the field B like A.B

**37**

#BHUSA  @BlackHatEvents

## Slide 38

## Results From Automation

- We found 43 trampoline functions causing arbitrary write, 29 trampoline function causing arbitrary read, 23 trampoline function causing other security issues

- We have released our CodeQL script and result of automation in GitHub

● Git link: https://github.com/MinghaoLin200 0/TrampolineFuncAnalyzer4FreeRT OS

**38**

#BHUSA  @BlackHatEvents

## Slide 39

## Key Takeaway: Comparison Among Different RTOSes

RTOS ThreadX MbedOS TIZenRT RT-Thread
Issue
Missing/Incomplete
Check
Mistaken MPU
configuration

**39**

#BHUSA  @BlackHatEvents

## Slide 40

## Future Work

- Continue exploitation

   - Identify different regions with different privileges in MPU_based RTOS firmware ■ Identify the trampoline functions in MPU_based RTOS firmware ■ Gadgets in kernel space are not accessed by user space

- Protection

   - Finer granularity isolation if performance allows ■ MPU Virtualization

**40**

#BHUSA  @BlackHatEvents

## Slide 41

## Thank You !

Twitter: <u>@Y1nKoc</u>

Email: <u>yenkoclike@gmail.com</u>

Personal Page: <u>https://minghaolin2000.github.io/</u>

**41**

#BHUSA  @BlackHatEvents
