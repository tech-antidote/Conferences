---
title: "Dead Pixel Detected - A Security Assessment of Apple's Graphics Subsystem"
speakers: ["Yu Wang", "Weiteng Chen"]
conference: "Black Hat"
conference_full: "Black Hat USA 2025"
edition: "USA"
year: 2025
source_pdf: "BlackHat_USA_2025_Slides/Yu Wang&Weiteng Chen_Dead Pixel Detected - A Security Assessment of Apple's Graphics Subsystem.pdf"
pages: 67
sha256: "d09156ff6909532f2db53e83ef3783744478f1889fc54c327475ed061c1b93f8"
text_chars: 46045
ocr_pages: 7
has_ocr: true
redacted_secrets: 0
ocr_confidence: 82.6
ocr_unreliable_blocks: 3
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T05:27:08Z"
---
# Dead Pixel Detected - A Security Assessment of Apple's Graphics Subsystem

**Speakers:** Yu Wang, Weiteng Chen  
**Conference:** Black Hat USA 2025  
**Source:** `BlackHat_USA_2025_Slides/Yu Wang&Weiteng Chen_Dead Pixel Detected - A Security Assessment of Apple's Graphics Subsystem.pdf` (67 pages)


## Slide 1

- "Dead pixel detected" A Security Assessment of Apple's Graphics Subsystem

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 86/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
pie hat
EFINGS
AUGUST be 2025
MANDALAY BAY / LAS VEGAS
“Dead pixel detected’ -
A Security Assessment of Apple's
Graphics Subsystem
```

## Slide 2

## About us

Yu Wang Co-founder && CEO at Cyberserval <u>keenjoy95@gmail.com</u>

Weiteng Chen Microsoft Research Redmond <u>weitengchencc@gmail.com</u>

#BHUSA @BlackHatEvents

## Slide 3

A Quick Introduction to (Apple) Graphics Subsystem

#BHUSA @BlackHatEvents

## Slide 4

## A quick introduction to GPU

Rather than drafting your own GPU overview, check out how GPU manufacturers describe their products. NVIDIA && Mythbusters: "Mythbusters Demo GPU versus CPU" <u>https://web.archive.org/web/20201007031633/https://www.youtube.com/watch?v=-P28LKWTzrI</u>

#BHUSA @BlackHatEvents

## Slide 5

## The key components

Framebuffer

Command queue and data sharing (The 10-second countdown can be regarded as preparation for data and instructions)

Command submission

Mythbusters Demo GPU versus CPU

#BHUSA @BlackHatEvents

## Slide 6

## Let's start with the simplest form

3D
Browser ...... Gaming
Modeling
Application
Runtime Framework
OpenGL/Vulkan
CUDA/Direct3D/Metal ......
User Mode
Kernel Mode
Talk directly to the kernel mode drivers
DRM/Dxgkrnl/IOGPUFamily
Plug-in Kernel Drivers
Central Processing Unit/Application Processor
Graphics Processing Unit
GPU OS/Hypervisor
Firmware

"Dead pixel detected" - A Security Assessment of Apple's Graphics Subsystem

#BHUSA @BlackHatEvents

## Slide 7

## From command to ring buffer

3D
Browser ...... Gaming
Modeling
Application
Runtime Framework
Vertex Fragment Accelerated Shading
Processing Generation Encryption Language
Primitive Framebuffer Decryption Interpreter
Assembly Operation Compression & LLVM
Wrapper Layer: libDRM, etc.
User Mode
Kernel Mode
ioctl-style Interfaces
DRM/Dxgkrnl/IOGPUFamily Ring Buffer
Construction
Plug-in Kernel Drivers CommandQueue 0
CommandQueue 1
Execution Central Processing Unit/Application Processor
......
Graphics Processing Unit
GPU OS/Hypervisor
CommandQueue N
Firmware

"Dead pixel detected" - A Security Assessment of Apple's Graphics Subsystem

#BHUSA @BlackHatEvents

## Slide 8

## Introducing scheduling and context switching

3D
Browser ...... Gaming
Modeling
Application
Runtime Framework
Vertex Fragment Accelerated Shading
Processing Generation Encryption Language
Primitive Framebuffer Decryption Interpreter
Assembly Operation Compression & LLVM
Wrapper Layer: libDRM, etc.
User Mode
Kernel Mode
ioctl-style Interfaces
DRM/Dxgkrnl/IOGPUFamily Ring Buffer
Construction
Plug-in Kernel Drivers CommandQueue 0
Preemption and GPU Context Switching CommandQueue 1
Scheduler Execution Central Processing Unit/Application Processor
......
Graphics Processing Unit
GPU OS/Hypervisor
CommandQueue N
Firmware

"Dead pixel detected" - A Security Assessment of Apple's Graphics Subsystem

#BHUSA @BlackHatEvents

## Slide 9

## Introducing data channel

mmap-style Interfaces Data Buffer
3D
Browser ...... Gaming
Modeling
Application
Runtime Framework
Vertex Fragment Accelerated Shading
Processing Generation Encryption Language
Primitive Framebuffer Decryption Interpreter
Assembly Operation Compression & LLVM
Wrapper Layer: libDRM, etc.
User Mode
Kernel Mode
ioctl-style Interfaces
DRM/Dxgkrnl/IOGPUFamily Ring Buffer Scratch Buffer
Construction Read/Write Operation
Plug-in Kernel Drivers CommandQueue 0
Preemption and GPU Context Switching CommandQueue 1
Scheduler Execution Central Processing Unit/Application Processor
......
Graphics Processing Unit
GPU OS/Hypervisor
CommandQueue N
Firmware

"Dead pixel detected" - A Security Assessment of Apple's Graphics Subsystem

#BHUSA @BlackHatEvents

## Slide 10

## You can't just bolt on security engineering at the last minute

"Dead pixel detected" - A Security Assessment of Apple's Graphics Subsystem

mmap-style Interfaces Data Buffer Virtual Memory Physical Memory
3D
Browser ...... Gaming
Modeling
Application
Runtime Framework
Vertex Fragment Accelerated Shading
Processing Generation Encryption Language Process
Primitive Framebuffer Decryption Interpreter
Level
Assembly Operation Compression & LLVM
Locally
Wrapper Layer: libDRM, etc.
Accessible User Mode
Kernel Mode
ioctl-style Interfaces
......
DRM/Dxgkrnl/IOGPUFamily Ring Buffer Scratch Buffer MMU AP
Construction Read/Write Operation Kernel
Plug-in Kernel Drivers CommandQueue 0 Page
Preemption and GPU Context Switching CommandQueue 1 AP Kerneland GPU Table Page
Scheduler Execution Central Processing Unit/Application Processor
...... Globally
Accessible Graphics Processing Unit
GPU
GPU OS/Hypervisor
CommandQueue N Page
Firmware ......
SMMU Table
GPU Page Table Switching

#BHUSA @BlackHatEvents

## Slide 11

## These background information are sufficient for today

Mythbusters Demo GPU versus CPU && "Dead pixel detected" - A Security Assessment of Apple's Graphics Subsystem

mmap-style Interfaces Data Buffer Virtual Memory Physical Memory
3D
Browser ...... Gaming
Modeling
Application
Runtime Framework
Vertex Fragment Accelerated Shading
Processing Generation Encryption Language Process
Primitive Framebuffer Decryption Interpreter
Level
Assembly Operation Compression & LLVM
Locally
Wrapper Layer: libDRM, etc.
Accessible User Mode
Kernel Mode
ioctl-style Interfaces
......
DRM/Dxgkrnl/IOGPUFamily Ring Buffer Scratch Buffer MMU AP
Construction Read/Write Operation Kernel
Plug-in Kernel Drivers CommandQueue 0 Page
Preemption and GPU Context Switching CommandQueue 1 AP Kerneland GPU Table Page
Scheduler Execution Central Processing Unit/Application Processor
...... Globally
Accessible Graphics Processing Unit
GPU
GPU OS/Hypervisor
CommandQueue N Page
Firmware ......
SMMU Table
GPU Page Table Switching

#BHUSA @BlackHatEvents

## Slide 12

## Apple GPU subsystem's kernel mode architecture

3D
Browser ...... Gaming
Modeling
Application
Runtime Framework
Vertex Fragment Accelerated Shading
Processing Generation Encryption Language
Primitive Framebuffer Decryption Interpreter
Assembly Operation Compression & LLVM
Wrapper Layer: libDRM, etc.
User Mode
Kernel Mode
IOGraphicsFamily/IOGPUFamily
AppleIntelSKLGraphicsF ramebuffer AGPM
...... AGX AMDSupport AGDCPluginDisplayMetrics
Accelerator ...... AppleGraphicsDeviceControl
Ap pleIntelKBL
AMDFramebuffer ......
A ppleIntelICL
IOMobileFramebuffer/IOMobileGraphicsFamily
IOMobileGraphicsFamily-DCP/DCPDP/AVFamily
Central Processing Unit/Application Processor
RTBuddy
Graphics Processing Unit
GPU OS/Hypervisor RTKit
Firmware RTOS
Display Co-processor (DCP) Firmware

"Dead pixel detected" - A Security Assessment of Apple's Graphics Subsystem

#BHUSA @BlackHatEvents

## Slide 13

# Security Assessment of - Apple's AMD and Intel based GPU

#BHUSA @BlackHatEvents

## Slide 14

## Research background

CVE-2020-27915

ATIController::setupSharedSurface Arbitrary Memory Write Vulnerability <u>https://support.apple.com/en-us/102846</u>

CVE-2022-22631

Out-of-bounds Read and Write Vulnerabilities in AGDCPluginDisplayMetrics Handlers <u>https://support.apple.com/en-us/102882</u>

CVE-2022-22661

AppleIntelMEUserClient::start/AppleIntelMEUserClient::stop, An Out-of-bounds Write Vulnerability caused by Type Confusion <u>https://support.apple.com/en-us/102882</u>

#BHUSA @BlackHatEvents

## Slide 15

## Case study of CVE-2020-27915

\```
Process 1 stopped
\```

\```
* thread #1, stop reason = signal SIGSTOP
\```

\```
frame #0: 0xffffff7fae144193 AMDSupport`ATIController::setupSharedSurface(AGDCMultiLinkConfig_t*,
ScanOutMetaInfo*) + 2339
AMDSupport`ATIController::setupSharedSurface:
\```

\```
->  0xffffff7fae144193 <+2339>: movb%dil, -0x578(%rbp,%rcx)
0xffffff7fae14419b <+2347>: movq-0x48(%rbp), %rcx
0xffffff7fae14419f <+2351>: movslq-0x600(%rbp), %rdx
0xffffff7fae1441a6 <+2358>: imulq$0xa8, %rdx, %rdx
\```

\```
(lldb) register read
\```

\```
General Purpose Registers:
\```

\```
rax= 0x0000000000000000
rbx= 0xffffffa09ca93ab8
\```

\```
rcx= 0xffffffffdeadbeef
rbp= 0xffffffa09ca93860
\```

\```
rsp= 0xffffffa09ca93220
\```

\```
rip = 0xffffff7fae144193  AMDSupport`ATIController::setupSharedSurface(AGDCMultiLinkConfig_t*,
ScanOutMetaInfo*) + 2339
\```

\```
......
\```

#BHUSA @BlackHatEvents

## Slide 16

## Case study of CVE-2022-22631

\```
Process 1 stopped
\```

- `thread #1, stop reason = EXC_BAD_ACCESS (code=2, address=0xd2285184) frame #0: 0xffffff7f9fd44aa9`

\```
->  0xffffff7f9fd44aa9: movb$0x3, 0x14(%r15)
\```

\```
(lldb) register read
\```

\```
General Purpose Registers:
\```

\```
r15 = 0xffffffb0d2285170
rip = 0xffffff7f9fd44aa9
\```

\```
......
\```

\```
(lldb) memory read 0xffffffb0d2285170+0x14
\```

\```
0xffffffb0d2285184: de ad ca fe41 41 41 41 41 41 41 41 41 41 41 41  ....AAAAAAAAAAAA
(lldb) bt
\```

\```
* thread #1, stop reason = EXC_BAD_ACCESS (code=2, address=0xd2285184)
\```

- `frame #0: 0xffffff7f9fd44aa9`

\```
frame #1: 0xffffff7f9fd52eed
frame #2: 0xffffff7f9fd5386f
frame #3: 0xffffff7f9fd50fff
frame #4: 0xffffff8006e2731b  kernel`is_io_connect_method+ 859
......
\```

#BHUSA @BlackHatEvents

## Slide 17

Case study of CVE-2022-22661

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 73/100 on the text kept, 62/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
black hat \ el |
di -s Oxffffff7fadc128fb
Oxffffff7fadc128fb <+975>: movq) | %rax, @x120(%rbx) This instructi
-> Oxffffff7fadc12902 <+982>: int3
Oxffffff7fadc12903 <+983>: sbbb %al, (%rax,%rax)
Oxffffff7fadc12909 <+989>: cld
Oxffffff7fadc129@c <+992>: addb %al, (%rax)
Oxffffff7fadc1290e <+994>: movq -@x48(%rbp), %rbx
Iv Oxffffff7fadc12912 <+998>: jne Oxffffff7fadc12f32 7 <+2566>
register read
( General Purpose Registers:
VE2707 2-2 2606 | rax = Oxffffff950F816c80 The RAX regist
rbx = Oxffffff9500ea53180 The
Tex = Oxffffff86a99d6690
rdx = 0x0000000000000040
rdi = @x@90@000000000040
rsi = 0x@99@000000000040
rbp = Oxffffffdessdb3bee
rsp = Oxffffffde83db3aae
18 = Oxffffff8043052F78
110 = Oxffffff99db29abbe
113 = Oxffffffdes3db3b8e
114 = @x@0000000000002c7
115 = Oxffffff950F793000
rip = Oxffffff7fadc12902 AppleIntelICLLPGraphicsFramebuffer AppleIntelMEClientController: :doCmdAction(MECommand_t, voidx, voidx, voidx) + 982
rflags = 0x0000000000000202
cs = 0x0e00000000000008
fs = exeeooaeeettffecde
gs = 0x9eee220e0ca50000
memory read Oxffffff950ea53180 Oxffffff950cea53180+0x130 -fx -s8
Oxffffff9500a53280:
ex 26000
Oxffffff950cea532a0: OxFFFFFFISOTE16C88 0x000000000000024a t nds write vulnerabilit
bt
* thread #1, stop reason =
* frame #0: Oxffffff7fadc1 2 AppleIntelICLLPGraphicsFramebuffer AppleIntelMEClientController: :doCmdAction(MECommand_t, void*, void*, void*) + 982
frame #1: Oxffffff801605a160 kernel‘ 10CommandGate: : runAction(this=Oxffffff8b76756dc®, inAction=<unavailable>, arg@=@x@000000000000100, argi=<unavailable>, arg2=<unavailable>, arg3=<unavailable>)(OSObject*, void
frame #2: Oxffffff801609462c kernel* o_connect_method(connection=<unavailable>, selector=<unavailable>, scalar_input=<unavailable>, scalar_inputCnt=<unavailable>, inband_input=<unavailable>, inband_inputCn
db29abb@) at I0UserClient.c 85 [opt]
frame #3: Oxffffff801598eca4 kernel *_Xio_connect_method(InHeadP=<unavailable>, OutHeadP=Oxffffffaes2cfc8e®) at device_server.c: 218 [opt]
frame #4: Oxffffff8015862e98 kernel" ipc_kmsg_send at ipc_kobject.c 3 [opt]
frame : Oxffffff8015862c5c kernel‘ ipc_kmsg_send [inlined] ipc_kobject_server(port=<unavailable>, request=<unavailable>, option=3) at ipc_kob
frame #6: Oxffffff8015862b81 kernel‘ ipc_kmsg_send(kmsg=<unavailable>, option=<unavailable>, send_timeout=@) at ipc_kmsg.c 1:10 [opt]
frame #7: Oxffffff80158798dd kernel *mach_msg_overwrite_trap(args=<unavailable>) at mach_msg.c
frame #9: Oxffffff8015828246 kernel hndl_mach_scall64 + 22
```

## Slide 18

## The latest kernel vulnerabilities

Case #1 - CVE-2025-24273 AppleIntelMEClientController::invalidateContentKey Arbitrary Kernel Memory Write Vulnerability About the security content of macOS Sequoia 15.4 <u>https://support.apple.com/en-us/122373</u> About the security content of macOS Sonoma 14.7.5 <u>https://support.apple.com/en-us/122374</u> Case #2 - OE0964116966483 ****** Kernel Out-of-bounds Access Vulnerability

#BHUSA @BlackHatEvents

## Slide 19

## Case #1 - CVE-2025-24273

\```
Process 1 stopped
\```

\```
* thread #1, stop reason = signal SIGSTOP
frame #0: 0xffffff7faef872d0
\```

\```
AppleIntelICLLPGraphicsFramebuffer`AppleIntelMEClientController::invalidateContentKey(MECLIENT_DATA_T*, int,
bool) + 168
\```

\```
AppleIntelICLLPGraphicsFramebuffer`AppleIntelMEClientController::invalidateContentKey:
\```

\```
->  0xffffff7faef872d0 <+168>: movl$0x0, 0x2568(%rbx,%rcx,4)
0xffffff7faef872db <+179>: shlq$0x4, %rcx
0xffffff7faef872df <+183>: xorl%eax, %eax
0xffffff7faef872e1 <+185>: movq%rax, 0x25b0(%rbx,%rcx)
Target 1: (kernel) stopped.
\```

\```
(lldb) register read
\```

\```
General Purpose Registers:
\```

\```
rbx= 0xffffff90a7570000
rcx= 0x0000000041414141
rip = 0xffffff7faef872d0
\```

\```
AppleIntelICLLPGraphicsFramebuffer`AppleIntelMEClientController::invalidateContentKey(MECLIENT_DATA_T*, int,
bool) + 168
\```

\```
......
\```

#BHUSA @BlackHatEvents

## Slide 20

## Case #2 - OE0964116966483

This vulnerability will not be fixed until this fall and will take approximately one year. In my experience, partially refactoring the module to eliminate these attack surfaces usually takes this long.

Apple Product Security, 06.12.2025

#BHUSA @BlackHatEvents

## Slide 21

Security Assessment of Apple Graphics Accelerator (AGX) GPU

#BHUSA @BlackHatEvents

## Slide 22

## Research background

CVE-2020-3837 iOS/macOS: OOB Timestamp Write in IOAccelCommandQueue2:: processSegmentKernelCommand() <u>https://project-zero.issues.chromium.org/issues/42451084</u> CVE-2021-30735 Exploiting Intel Graphics Kernel Extensions on macOS <u>https://blog.ret2.io/2022/06/29/pwn2own-2021-safari-sandbox-intel-graphics-exploit/</u> CVE-2022-32947 I hacked macOS!!! <u>https://asahilina.net/agx-exploit/</u>

#BHUSA @BlackHatEvents

## Slide 23

## The latest kernel vulnerabilities

Case #3 - CVE-2024-44197 IOGPUDeviceUserClient::s_create_notificationqueue/s_destroy_notificationqueue Notification Queue Out-of-bounds Access Vulnerability About the security content of macOS Sequoia 15.1 <u>https://support.apple.com/en-us/121564</u> Case #4 - CVE-2025-24257 IOGPUResource::newResourceGroup Kernel Out-of-bounds Read and Write Vulnerability About the security content of iOS 18.4 and iPadOS 18.4 <u>https://support.apple.com/en-us/122371</u> About the security content of macOS Sequoia 15.4 <u>https://support.apple.com/en-us/122373</u>

#BHUSA @BlackHatEvents

## Slide 24

## Case #3 - CVE-2024-44197

During reverse engineering, I found that functions like create_notificationqueue accept at least two critical parameters, numEntries and entrySize, but such functions do not strictly check the validity of these parameters.

macOS Ventura 13.5 Beta (22G5027e)

#BHUSA @BlackHatEvents

## Slide 25

## The panic

#### `Process 1 stopped`

\```
* thread #1, stop reason = signal SIGSTOP
\```

\```
frame #0: 0xfffffe0020f779f8 kernel.release.t8122`DebuggerTrapWithState(db_op=DBOP_PANIC,
db_message="panic", db_panic_str="%s %s --exit reason namespace %d subcode 0x%llx description: %.800s",
db_panic_args=0xfffffe84f9cef9e8, db_panic_options=8224, db_panic_data_ptr=0x0000000000000000,
\```

\```
db_proceed_on_sync_failure=1, db_panic_caller=18446741875244973128, db_panic_initiator=0x0000000000000000) at
debug.c:819:2 [opt]
\```

\```
Target 1: (kernel.release.t8122) stopped.
\```

\```
warning: kernel.release.t8122 was compiled with optimization -stepping may behave oddly; variables may not be
available.
\```

\```
(lldb) register read
\```

\```
General Purpose Registers:
\```

\```
x0 = 0x0000000000000003
\```

\```
x1 = 0xfffffe001f91e478  "panic"
\```

\```
lr= 0xfffffe0020f76fcc  kernel.release.t8122`panic_trap_to_debugger + 744 [inlined]
panic_spin_foreverat debug.c:1346:3
\```

\```
kernel.release.t8122`panic_trap_to_debugger + 744 at debug.c:1336:2
\```

\```
pc = 0xfffffe0020f779f8  kernel.release.t8122`DebuggerTrapWithState + 76 at debug.c:819:2
\```

\```
......
\```

#BHUSA @BlackHatEvents

## Slide 26

## Patch for CVE-2024-44197

The patch for the vulnerability is straightforward.

macOS Sequoia 15.1 Beta (24B83)

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 86/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
BRIEFINGS
Patch for CVE-2024-44 197
The patch for the
vulnerability is straightforward.
IOGPUObject *object; //
IOGPUNotificationQueue *queue; //
int vy,
if ( (nu - @x2@01) < @xFFFFE@@@ || (ent - @x29) <= @xFFFFFFD7 )
&dword_@,
&
OS_LOG_TYPE_FAULT
return @xE@@@@2C2LL;
}
else
{
= IOGPUNotificationQueue: :withEntries(*( + 8@),
3
= IOGPUNamespace: :addObject(*(this + 144), ject);
```

## Slide 27

## The confusing security advisory

https://support.apple.com/en-us/121564

History of NULL Pointer Dereferences on macOS <u>https://afine.com/history-of-null-pointer-dereferences-on-macos/</u> Case Study: IOMobileFramebuffer NULL Pointer Dereference <u>https://afine.com/case-study-iomobileframebuffer-null-pointer-dereference/</u>

#BHUSA @BlackHatEvents

## Slide 28

## Response from Apple's product security team

I have also discussed this issue with Apple SRC team, and they have promised to modify the description for CVE-2024-44197/OE098860881902.

Apple Product Security, 04.17.2025

#BHUSA @BlackHatEvents

## Slide 29

## Case #4 - CVE-2025-24257

The advisory this time is clear. It's a kernel memory write vulnerability that affects both iOS and macOS.

Through significant effort, I gradually transformed a seemingly unusable raw panic into a kernel memory write vulnerability to demonstrate its exploitability.

https://support.apple.com/en-us/122371

#BHUSA @BlackHatEvents

## Slide 30

## Initially, I only observed some strange kernel panics

\```
Process 1 stopped
\```

\```
* thread #1, stop reason = signal SIGSTOP
\```

\```
frame #0: 0xfffffe002e0d3648 kernel.release.t8122`DebuggerTrapWithState(db_op=DBOP_PANIC,
db_message="panic", db_panic_str="%s at pc 0x%016llx, lr0x%016llx (saved state: %p%s)\n\t  x0:  0x%016llx x1:
0x%016llx  x2:  0x%016llx  x3:  0x%016llx\n\t  x4:  0x%016llx x5:  0x%016llx  x6:  0x%016llx  x7:
0x%016llx\n\t  x8:  0x%016llx x9:  0x%016llx  x10: 0x%016llx  x11: 0x%016llx\n\t  x12: 0x%016llx x13:
0x%016llx  x14: 0x%016llx  x15: 0x%016llx\n\t  x16: 0x%016llx x17: 0x%016llx  x18: 0x%016llx  x19:
0x%016llx\n\t  x20: 0x%016llx x21: 0x%016llx  x22: 0x%016llx  x23: 0x%016llx\n\t  x24: 0x%016llx x25:
0x%016llx  x26: 0x%016llx  x27: 0x%016llx\n\t  x28: 0x%016llx fp:  0x%016llx  lr:  0x%016llx  sp:
0x%016llx\n\t  pc:  0x%016llx cpsr: 0x%08x         esr: 0x%016llx  far: 0x%016llx\n",
\```

\```
db_panic_args=0xfffffe8f1896f028, db_panic_options=0, db_panic_data_ptr=0x0000000000000000,
\```

\```
db_proceed_on_sync_failure=1, db_panic_caller=18446741875467706024, db_panic_initiator=0x0000000000000000) at
debug.c:834:2 [opt]
\```

\```
Target 0: (kernel.release.t8122) stopped.
\```

\```
warning: kernel.release.t8122 was compiled with optimization -stepping may behave oddly; variables may not be
available.
\```

\```
(lldb) di -p
\```

\```
IOGPUFamily`IOGPUGroupMemory::remove_memory_object:
\```

\```
->  0xfffffe0030693724 <+292>: ldrw11, [x11, w10, uxtw#2]
\```

#BHUSA @BlackHatEvents

## Slide 31

### We need to gradually escalate the problem to achieve arbitrary memory access

\```
(lldb) di -p
\```

\```
IOGPUFamily`IOGPUGroupMemory::removeMemoryFromResourceMap:
\```

\```
->  0xfffffe00193f4f40 <+96>:  ldrx8, [x9, x8]
0xfffffe00193f4f44 <+100>: ldrx1, [x8, #0x28]
0xfffffe00193f4f48 <+104>: mov    x0, x20
0xfffffe00193f4f4c <+108>: mov    x2, x19
\```

\```
(lldb) register read
\```

\```
General Purpose Registers:
\```

\```
x8 = 0x0000000000067020
\```

\```
x9 = 0xfffffe24d47e0040
\```

\```
fp= 0xfffffe3eecb03710
\```

\```
lr= 0xfffffe00193f4f0c
\```

\```
IOGPUFamily`IOGPUGroupMemory::removeMemoryFromResourceMap(IOGPUCountedMap<unsigned long long, IOGPUResource*,
IOGPUResourceCountedMapBucket, IOGPUIOLibAllocatorPolicy>*, bool) + 44
\```

\```
sp= 0xfffffe3eecb036d0
\```

\```
pc = 0xfffffe00193f4f40
\```

\```
IOGPUFamily`IOGPUGroupMemory::removeMemoryFromResourceMap(IOGPUCountedMap<unsigned long long, IOGPUResource*,
IOGPUResourceCountedMapBucket, IOGPUIOLibAllocatorPolicy>*, bool) + 96
\```

\```
......
\```

#BHUSA @BlackHatEvents

## Slide 32

## The vulnerable function does check parameters, but inadequately

macOS Sequoia 15.2 RC2 (24C100)

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 85/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
2)
black hat
BRIEFINGS
The vulnerable function does check parameters, but inadequately
else
&dword_@,
&
05_LOG_TYPE_FAULT,
“hs: newResourceGroup bad initial capacity: %d\n",
“static OSPtr<IOGPUResource> I0GPUResource: :newResourceGroup(IOGPU *, IO0GPUDevice *, uint32_t}",
return @LL;
}
```

## Slide 33

## Half a year later, the patch for CVE-2025-24257 landed

macOS Sequoia 15.2 RC2 (24C100)

macOS Tahoe 26.0 Beta (25A5279m)

#BHUSA @BlackHatEvents

## Slide 34

## Hmmm...

Good, "less than" works, but what happens when greater than?

#BHUSA @BlackHatEvents

## Slide 35

Bypassing the patch on the macOS Tahoe 26.0 Beta (25A5279m)

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 72/100 on the text kept, 70/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Process 1 stopped
* thread #1, stop reason =
frame #0: Oxfffffeee@2eebda9c kernel.release.t8122° DebuggerTrapWithState(db_op=DBOP_PANIC, db_message="panic", db_panic_str="%s at pc @x%@1611x, lr @x%@1611x (saved state: %p%s)\n\t x@: @x%@1611x x1:
@x%O@1611x x2: Ox%O@1611x x3: Ox%@1611x\n\t x4: ©Ox%@1611x x5: @x%@1611x x6: @x%@1611x x7: ©x%@1611x\n\t x8: @x%@1611x x9: @x%@1611x x10: @x%@1611x x11: @x%O@1611x\n\t x12: @x%@1611x x13: @
x%@1611x x14: @x%@1611x x15: @x%@1611x\n\t x16: @x%@1611x x17: @x%@1611x x18: @x%@1611x x19: @x%@1611x\n\t x20: @x%O@1611x x21: Ox%@1611x x22: Ox%@1611x x23: Ox%@1611x\n\t x24: Ox%@1611x x25: @x%e
1611x x26: Ox%@1611x x27: @x%@1611x\n\t x28: @x%@1611x fp: @x%@1611x Ir: Ox%@1611x sp: @x%@1611x\n\t pc: @x%@1611x cpsr: Ox%@8x esr: @x%@1611x far: @x%@1611x\n", db_panic_args=Oxfffffe6
770276f68, db_panic_options=0, db_panic_data_ptr=0x0000000000000000, db_proceed_on_sync_failure=1, db_panic_caller=18446741875482508000, db_panic_initiator=0x0000000000000000) at debug.c:834:2 [opt]
Target 2: (kernel.release.t8122) stopped.
warning: kernel.release.t8122 was compiled with optimization -— stepping may behave oddly; variables may not be available.
[(lldb) register read
General Purpose Registers:
x1 Oxfffffe271aee17be
x3 @x0000000000000000
we © Srossssooeeeennae assing the patch on the macOS Tahoe eta m
x12 @x@000000000001000
x16 @xfffffee@2ea4c170 IOGPUFamily*vtable for IOGPUGroupMemory + 72
x20 Oxfffffe214F5234ce
x21 Oxfffffe3laf9c2300
x23 @x@000000000000001
x24 @x8000000000000000
x25 @x@000000000000058
x27 @x0000000000000000
x28 = 0x0000000000000000
fp = Oxfffffe6770277690
lr = @xfffffeee3154e98c IOGPUFamily ~IOGPUGroupMemory: : removeMemoryFromResourceMap(IOGPUCountedMap<unsigned long long, IOGPUResource*, IOGPUResourceCountedMapBucket, IOGPUIOLibAllocatorPolicy>*, b
sp = Oxfffffe6770277650
pe = @xfffffeee3154e998 IOGPUFamily ~IOGPUGroupMemory: : removeMemoryFromResourceMap(IOGPUCountedMap<unsigned long long, IOGPUResource*, IOGPUResourceCountedMapBucket, IOGPUIOLibAllocatorPolicy>*, b
cpsr = @x60401208
[(1lldb) bt
* thread #1, stop reason =
frame #0: Oxfffffeee@2eebda9c kernel.release.t8122° DebuggerTrapWithState(db_op=DBOP_PANIC, db_message="panic", db_panic_str="%s at pc @x%@1611x, lr @x%@1611x (saved state: %p%s)\n\t x@: ©@x%@1611x x1:
@x%@1611x x2: Ox%O@1611x x3: Ox%@1611x\n\t x4: Ox%@1611x x5: @x%@1611x x6: @x%@1611x x7: @x%@1611x\n\t x8: @x%@1611x x9: @x%@1611x x10: @x%@1611x x11: @x%@1611x\n\t x12: @x%@1611x x13: @
x%O1611x x14: @x%@1611x x15: Ox%O1611x\n\t x16: @x%@1611x x17: Ox%O1611x x18: @x%@1611x x19: Ox%O@1611x\n\t x20: @x%O@1611x x21: O@x%@1611x x22: Ox%O@1611x x23: Ox%O@1611x\n\t x24: Ox%O1611x x25: Ox%e
1611x x26: Ox%@1611x x27: @x%@1611x\n\t x28: @x%@1611x fp: @x%O1611x Ir: @x%O1611x sp: @x%@1611x\n\t pc: @x%O01611x cpsr: @x%@8x esr: @x%@1611x far: @x%@1611x\n", db_panic_args=0xfffffe6
770276f68, db_panic_options=@, db_panic_data_ptr=0x0000000000000000, db_proceed_on_sync_failure=1, db_panic_caller=18446741875482508000, db_panic_initiator=0x09000000000000000) at debug.c:834:2 [opt]
frame #1: Oxfffffeee2eebd@58 kernel.release.t8122° panic_trap_to_debugger(panic_format_str="%s at pc @x%@1611x, lr @x%@1611x (saved state: %p%s)\n\t x@: @x%@1611x x1: ©x%@1611x x2: ©x%@1611x x3:
@x%O1611x\n\t x4: @x%O1611x x5: Ox%@1611x x6: Ox%@1611x x7: Ox%@1611x\n\t x8: Ox%@1611x x9: @x%@1611x x10: @x%@1611x x11: @x%@1611x\n\t %«12: @x%@1611x x13: @x%@1611x x14: @x%@1611x x15: @x
%@1611x\n\t x16: @x%@1611x x17: @x%@1611x x18: @x%@1611x x19: @x%@1611x\n\t x2@: @x%@1611x x21: Ox%@1611x x22: @x%@1611x x23: Ox%O@1611x\n\t x24: @x%O@1611x x25: @x%@1611x x26: @x%O@1611x x27: @x%e1
611x\n\t x28: @x%@1611x fp: @x%@161l1x Ir: ©@x%@1611x sp: Ox%@1611x\n\t pc: @x%O@1611x cpsr: Ox%e8x esr: @x%@1611x far: @x%@1611x\n", panic_args=Oxfffffe6770276F68, reason=0, ctx=0x000000000
0000000, panic_options_mask=0, panic_data_ptr=@x9000000000000000, panic_caller=18446741875482508000, panic_initiator=0x@000000000000000) at debug.c:1394:2 [opt]
frame #2: Oxfffffeee2f7484e4 kernel.release.t8122°panic(str=<unavailable>) at debug.c:1161:2 [opt]
frame #3: Oxfffffeee2F753ae® kernel.release.t8122° panic_with_thread_kernel_state(msg="Kernel data abort.", ss=Oxfffffe6770277300) at sleh.c:935:2 [opt]
frame #4: Oxfffffeee2fela7fO@ kernel.release.t8122°handle_kernel_abort(state=Oxfffffe6770277300, esr=<unavailable>, fault_addr=@, fault_code=<unavailable>, fault_type=1, expected_fault_handler=<unavail
able>) at sleh.c:3485:2 Lopt]
frame #5: Oxfffffeee2fe18f7c kernel.release.t8122°>sleh_synchronous [inlined] handle_abort(state=0xfffffe6770277300, esr=2516582406, fault_addr=0, inspect_abort=<unavailable>, handler=<unavailable>, ex
pected_fault_handler=0xe000e00000000008) at sleh.c:1845:2 [opt]
frame #6: Oxfffffeee2fe1sf6és kernel.release.t8122~>sleh_synchronous(context=0xfffffe6770277300, esr=2516582406, far=0, did_initiate_panic_lockdown=<unavailable>) at sleh.c:1308:3 [opt]
frame #7: Oxfffffee0@2ee678cQ@ kernel.release.t8122°fleh_synchronous + 44
* frame #8: Oxfffffee03154e998 IOGPUFamily ~ IlOGPUGroupMemory: : removeMemoryFromResourceMap(IOGPUCountedMap<unsigned long long, IOGPUResource*x, IOGPUResourceCountedMapBucket, IOGPUIOLibAllocatorPolicy>*, b
frame #9: Oxfffffee0315382d8 IOGPUFamily ~ IOGPUResource::free() + 272
frame #10: OxfffffeG0315333d4 IOGPUFamily ~IOGPUObjec elease() const + 48
```

## Slide 36

# Security Assessment of IOMobileFrameBuffer (IOMFB)

#BHUSA @BlackHatEvents

## Slide 37

## The story behind IOMFB

The statistical data on IOMobileFrameBuffer vulnerabilities indicates that the competition between the offensive and defensive sides once reached a fever pitch. According to publicly available records, a total of sixteen kernel vulnerabilities in IOMobileFrameBuffer have been reported throughout its history. Among these, four were actively exploited by APT groups (CVE-2021-30807, CVE-2021-30883, CVE-202130983, CVE-2022-22587), two were leveraged in iOS jailbreak tools (JailbreakMe 3.0 - CVE-2011-0227, Pangu 9 - CVE-2016-4654), and one was successfully utilized to win a security challenge competition (Tianfu Cup - CVE-2021-30983).

#BHUSA @BlackHatEvents

## Slide 38

The historical landscape of IOMFB kernel vulnerabilities - in the first ten years

2011 - CVE-2011-0227 (Comex, JailbreakMe 3.0)

2012 - N/A 2013 - N/A 2014 - N/A 2015 - CVE-2015-1097 (Barak Gabai), CVE-2015-5843 (Filippo Bigarella) 2016 - CVE-2016-4654 (Tielei Wang - Team Pangu, Pangu 9) 2017 - CVE-2017-13879 (Apple) 2018 - CVE-2018-4335 (Brandon Azad) 2019 - N/A 2020 - N/A

#BHUSA @BlackHatEvents

## Slide 39

## The historical landscape of IOMFB kernel vulnerabilities - in recent years

2021 - CVE-2021-30807 (ITW APT attack / Saar Amar), CVE-2021-30883 (ITW APT attack / Tielei Wang - Team Pangu), CVE-2021-30983 (Tielei Wang - Team Pangu, Tianfu Cup Competition), CVE-2021-30985 (Tielei Wang - Team Pangu), CVE-202130991 (Tielei Wang - Team Pangu), CVE-2021-30996 (Saar Amar)

2022 - CVE-2022-22587 (ITW APT attack / Meysam Firouzi / Siddharth Aeri), CVE2022-26768 (An Anonymous Researcher, Highly likely exploited by an ITW APT attack), CVE-2022-46690 (John Aakerblom), CVE-2022-46697 (John Aakerblom / Antonio Zekic)

2023 - N/A

2024 - Any ideas?

#BHUSA @BlackHatEvents

## Slide 40

## One more thing

However, no new IOMobileFrameBuffer kernel vulnerabilities have been disclosed since 2023.

In addition, it should be noted that by the end of 2024, several vulnerabilities were misclassified as IOMobileFramebuffer. In fact, they are firmware issues of the Display Co-processor. These vulnerabilities were submitted by Ye Zhang from the Baidu Security Labs.

#BHUSA @BlackHatEvents

## Slide 41

## Research background

《 IOMFB 的一些陈芝麻》 Pangu 9 Internals <u>https://www.blackhat.com/docs/us-16/materials/us-16-Wang-Pangu-9-Internals.pdf</u> Selector 0x53 - CVE-2021-30807 WebContent to EL1 LPE - OOBR in AppleCLCD and IOMobileFrameBuffer <u>https://saaramar.github.io/IOMobileFrameBuffer_LPE_POC/</u> Selector 0x4E - CVE-2021-30883 Bindiff and PoC for the IOMFB Vulnerability, iOS 15.0.2 <u>https://saaramar.github.io/IOMFB_integer_overflow_poc/</u>

#BHUSA @BlackHatEvents

## Slide 42

## After the party, most of the attack surfaces have been removed

A form of defense-in-depth

IOMFB meme

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 89/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
© Adam Donenfeld @
This has been moved tothe display coprocessor (DCP) starting from 15,
at least on iPhone 12 (and most probably other ones as well)
e Saar Amar
So, another IOMFB vulnerability was exploited ITW (15.0.2). | bindiffed the
patch and built a POC. And, because it's a great bug, | just finished writing a
short blogpost with the tech details, to share this knowledge :) Check it out!
panic-full-2021-10-11-101451.0...
YOU GET KERNEL ACCESS & YOU GET KERNEL valOxaiaratateratatay, s:80, ptrOxttittes7esBcd70)\n 0:
```

## Slide 43

## Is it still possible to find new IOMFB kernel vulnerabilities?

Case #5 - CVE-2024-44199 IOMFB::PBTBlockHandlerGeneric::get_map_buf_descs Kernel Out-of-bounds Access Vulnerability caused by Comparison between Unsigned and Signed Integers About the security content of macOS Sonoma 14.6 <u>https://support.apple.com/en-us/120911</u>

#BHUSA @BlackHatEvents

## Slide 44

## Definitely

CVE-2024-44199 resides in the function

IOMFB::PBTBlockHandlerGeneric::get_map_buf_descs, which consists of merely two lines of code. It's worth mentioning that this vulnerability can be triggered directly in user mode without the need to apply for any entitlement.

macOS Sonoma 14.0 Beta 0 (23A344)

#BHUSA @BlackHatEvents

## Slide 45

## The panic

\```
(lldb) di
\```

\```
IOMobileGraphicsFamily`IOMFB::PBTBlockHandlerGeneric::get_map_buf_descs:
0xfffffe002bb7f770 <+88>:  add    x8, x8, #0x308 ; IOMFB::PBTBlockHandlerGeneric::descs
\```

\```
->  0xfffffe002bb7f774 <+92>:  ldrq0, [x8, x9, lsl#4]
0xfffffe002bb7f778 <+96>:  sturq0, [x29, #-0x10]
0xfffffe002bb7f77c <+100>: ldurx0, [x29, #-0x10]
0xfffffe002bb7f780 <+104>: ldurx1, [x29, #-0x8]
\```

\```
(lldb) register read
\```

\```
General Purpose Registers:
\```

\```
x8 = 0xfffffe0029488308IOMobileGraphicsFamily`IOMFB::PBTBlockHandlerGeneric::descs
\```

\```
x9 = 0x00000000deadcafe
\```

\```
fp= 0xfffffe49a50af5d0
\```

\```
lr= 0xfffffe002bb3fb98  IOMobileGraphicsFamily-
\```

\```
DCP`IOMobileFramebufferAP::map_block_buf(IOMobileFramebufferAP::map_block_buf_args*,
\```

\```
IOMFB_Parameter_Block_Type, unsigned char const*, unsigned long, task*, bool) + 156
\```

\```
sp= 0xfffffe49a50af5a0
\```

\```
pc = 0xfffffe002bb7f774
\```

\```
IOMobileGraphicsFamily`IOMFB::PBTBlockHandlerGeneric::get_map_buf_descs(IOMFB_Parameter_Block_Type) + 92
\```

\```
......
\```

#BHUSA @BlackHatEvents

## Slide 46

## Two different patches - keep it as signed

Another interesting footnote is that I found two different implementations for the CVE-2024-44199 patch.

macOS Sonoma 14.6 Beta (23G5066c)

#BHUSA @BlackHatEvents

## Slide 47

## Two different patches - make it unsigned uniformly

If these were developed by separate teams, I would recommend establishing unified standard across all teams.

macOS Sequoia 15.0 Beta 0 (24A335)

#BHUSA @BlackHatEvents

## Slide 48

## Case #6 - OE098868205995

\```
(lldb) bt
\```

- `thread #1, stop reason = signal SIGSTOP`

\```
......
\```

\```
frame #2: 0xfffffe00291f527c kernel.release.t8122`panic(str=<unavailable>) at debug.c:1113:2 [opt]
frame #3: 0xfffffe00291ffcbc kernel.release.t8122`panic_with_thread_kernel_state(msg="Kernel data abort.",
ss=0xfffffe84e0393400) at sleh.c:901:2 [opt]
frame #4: 0xfffffe0028ab1ebc kernel.release.t8122`handle_kernel_abort(state=0xfffffe84e0393400,
esr=2516582406, fault_addr=0, fault_code=FSC_TRANSLATION_FAULT_L2, fault_type=1,
expected_fault_handler=<unavailable>) at sleh.c:3116:2 [opt]
\```

\```
frame #5: 0xfffffe0028ab0864 kernel.release.t8122`sleh_synchronous [inlined]
handle_abort(state=0xfffffe84e0393400, esr=2516582406, fault_addr=0, inspect_abort=<unavailable>,
handler=<unavailable>, expected_fault_handler=0x0000000000000000) at sleh.c:1743:2 [opt]
\```

\```
frame #6: 0xfffffe0028ab0850 kernel.release.t8122`sleh_synchronous(context=0xfffffe84e0393400,
esr=2516582406, far=0, did_initiate_panic_lockdown=<unavailable>) at sleh.c:1256:3 [opt]
frame #7: 0xfffffe002890b888 kernel.release.t8122`fleh_synchronous + 44
\```

\```
frame #8: 0xfffffe002b040fe0 IOMobileGraphicsFamily-DCP`IOMFB::DCPMemoryDescriptor::prepare(IOMFB::
MemoryDescriptor::Options) + 8
\```

\```
......
\```

#BHUSA @BlackHatEvents

## Slide 49

Security Assessment of - Display Co processor (DCP) Firmware

#BHUSA @BlackHatEvents

## Slide 50

## Asahi Linux and m1n1 project

Reverse Engineering DCP <u>https://asahilinux.org/2021/08/progress-report-august-2021/</u> Asahi Linux: DCP Command Interface Reversing <u>https://www.youtube.com/watch?v=LNKLvwfFFa8</u> Asahi Linux: DCP/AGX ASC Mailbox Reversing <u>https://www.youtube.com/watch?v=V5W23At6b4Y</u>

#BHUSA @BlackHatEvents

## Slide 51

## CVE-2021-30983, ColdIntro and ColdInvite

The Curious Tale of a Fake Carrier.app <u>https://googleprojectzero.blogspot.com/2022/06/curious-case-carrier-app.html</u> Abusing iPhone Co-processors for Privilege Escalation <u>https://objectivebythesea.org/v5/talks/OBTS_v5_iBeer.pdf</u>

The Mystery Behind ColdIntro (CVE-2022-32894) and ColdInvite (CVE-2023-27930) a Co-processor Escape Vulnerability Contents <u>https://resources.jamf.com/documents/technical-papers/Coldintro-Coldinvite-Mystery-v2.0.pdf</u>

#BHUSA @BlackHatEvents

## Slide 52

## Short-term research objectives of DCP

1. Dive deep into the architecture of the DCP subsystem.

2. Hunt for potential attack surfaces in the DCP subsystem.

3. Develop a DCP fuzzer by integrating the insights from 1 and 2.

#BHUSA @BlackHatEvents

## Slide 53

## Case study of APT firmware fuzzing

\```
(lldb) memory read 0xfffffe29a0220000 -c0x7000 --force
0xfffffe29a0220000: 50 41 4e 49 43 20 2d 20 61 70 74 20 66 69 72 6d  PANIC -apt firm
0xfffffe29a0220010: 77 61 72 65 3a 20 61 70 74 2e 63 3a 33 37 30 20  ware: apt.c:370
-
0xfffffe29a0220020: 61 70 74 5f 76 62 69 28 29 20 2d 2d20 20 2d 20  apt_vbi() --
0xfffffe29a0220030: 69 6f 6d 66 62 5f 6d 61 69 6c 62 6f 78 28 39 32  iomfb_mailbox(92
0xfffffe29a0220040: 29 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  )...............
0xfffffe29a0220050: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
0xfffffe29a0220060: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
0xfffffe29a0220070: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
0xfffffe29a0220080: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
0xfffffe29a0220090: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
0xfffffe29a02200a0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
0xfffffe29a02200b0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
0xfffffe29a02200c0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
0xfffffe29a02200d0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
0xfffffe29a02200e0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
0xfffffe29a02200f0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
0xfffffe29a0220100: 61 70 74 20 66 69 72 6d 77 61 72 65 3a 20 61 70  apt firmware: ap
0xfffffe29a0220110: 74 2e 63 3a 33 37 30 20 61 70 74 5f 76 62 69 28  t.c:370 apt_vbi(
0xfffffe29a0220120: 29 20 2d 2d20 0a 52 54 4b 69 74 3a 20 52 54 4b  ) --.RTKit: RTK
0xfffffe29a0220130: 69 74 2d 32 37 35 38 2e 34 30 2e 31 39 2e 72 65  it-2758.40.19.re
\```

#BHUSA @BlackHatEvents

## Slide 54

## Case study of PCC firmware fuzzing

\```
(lldb) memory read 0xfffffe2fffd40000 -c0x7000 --force
0xfffffe2fffd40000: 50 41 4e 49 43 20 2d 20 70 63 63 20 66 69 72 6d  PANIC -pccfirm
0xfffffe2fffd40010: 77 61 72 65 3a 20 61 68 5f 74 68 72 2e 63 3a 32  ware: ah_thr.c:2
0xfffffe2fffd40020: 33 33 20 61 68 5f 62 65 67 69 6e 5f 75 70 64 61  33 ah_begin_upda
0xfffffe2fffd40030: 74 65 28 29 20 2d 2d20 20 2d 20 69 6f 6d 66 62  te() ---iomfb
0xfffffe2fffd40040: 5f 6d 61 69 6c 62 6f 78 28 34 32 29 00 00 00 00  _mailbox(42)....
0xfffffe2fffd40050: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
0xfffffe2fffd40060: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
0xfffffe2fffd40070: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
0xfffffe2fffd40080: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
0xfffffe2fffd40090: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
0xfffffe2fffd400a0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
0xfffffe2fffd400b0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
0xfffffe2fffd400c0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
0xfffffe2fffd400d0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
0xfffffe2fffd400e0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
0xfffffe2fffd400f0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
0xfffffe2fffd40100: 70 63 63 20 66 69 72 6d 77 61 72 65 3a 20 61 68  pccfirmware: ah
0xfffffe2fffd40110: 5f 74 68 72 2e 63 3a 32 33 33 20 61 68 5f 62 65  _thr.c:233 ah_be
0xfffffe2fffd40120: 67 69 6e 5f 75 70 64 61 74 65 28 29 20 2d 2d20  gin_update() –
0xfffffe2fffd40130: 0a 52 54 4b 69 74 3a 20 52 54 4b 69 74 2d 32 34  .RTKit: RTKit-24
0xfffffe2fffd40140: 31 33 2e 34 31 2e 31 2e 72 65 6c 65 61 73 65 20  13.41.1.release
\```

#BHUSA @BlackHatEvents

## Slide 55

## The RTBuddy mechanism

\```
(lldb) bt
\```

- `thread #1, stop reason = signal SIGSTOP`

   - `frame #0: 0xfffffe001fbb63b0 kernel.release.t6000`DebuggerTrapWithState(db_op=DBOP_PANIC,`

\```
db_message="panic", db_panic_str="%s %s%s%s\n%s", db_panic_args=0xfffffe840d8c7df8, db_panic_options=0,
db_panic_data_ptr=0x0000000000000000, db_proceed_on_sync_failure=1, db_panic_caller=18446741875263258400) at
debug.c:714:2 [opt]
\```

\```
frame #1: 0xfffffe001fbb593c kernel.release.t6000`panic_trap_to_debugger(panic_format_str="%s %s%s%s\n%s",
panic_args=0xfffffe840d8c7df8, reason=0, ctx=0x0000000000000000, panic_options_mask=0,
panic_data_ptr=0x0000000000000000, panic_caller=18446741875263258400) at debug.c:1175:2 [opt]
frame #2: 0xfffffe0020333fd4 kernel.release.t6000`panic_with_options(reason=<unavailable>,
ctx=<unavailable>, debugger_options_mask=<unavailable>, str=<unavailable>) at debug.c:1018:2 [opt]
frame #3: 0xfffffe002263bf20 RTBuddy`RTBuddyCrashlogEndpoint::_handleCrashlog(bool) + 1280
frame #4: 0xfffffe002209e5e0 IOSlaveProcessor`IOSlaveEndpoint::checkForWork() + 124
frame #5: 0xfffffe0020242e54 kernel.release.t6000`IOWorkLoop::runEventSources(this=0xfffffe33ceba17b0) at
IOWorkLoop.cpp:403:18 [opt]
\```

\```
frame #6: 0xfffffe00202439dc kernel.release.t6000`IOWorkLoop::threadMain(this=0xfffffe33ceba17b0) at
IOWorkLoop.cpp:434:8 [opt]
\```

\```
frame #7: 0xfffffe001fb70e98 kernel.release.t6000`Call_continuation + 216
\```

#BHUSA @BlackHatEvents

## Slide 56

Case #7 - Video streaming attack surface

#BHUSA @BlackHatEvents

## Slide 57

## dcpav-video-interface-epic daemon

Case #8 - CVE-2025-24111 dcpav-video-interface-epic LinkWithSource Display Co-processor (DCP) Firmware Vulnerability

About the security content of iOS 18.3 and iPadOS 18.3 <u>https://support.apple.com/en-us/122066</u> About the security content of macOS Sequoia 15.3 <u>https://support.apple.com/en-us/122068</u>

#BHUSA @BlackHatEvents

## Slide 58

Case #8 - CVE-2025-24111

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 86/100 on the text kept, 81/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
[(lldb) bt
* thread #1,
* frame #0:
stop reason =
Oxfffffee018617fe8 kernel.release.t8122°DebuggerTrapWithState(db_op=DBOP_PANIC, db_message="panic", db_panic_str="%s %s%s%s\n%s", db_panic_args=0xfffffe8f15497db8, db_panic_options=16384, db
_panic_data_ptr=0x0000000000000000, db_proceed_on_sync_failure=1, db_panic_caller=18446741875144245264, db_panic_initiator="DCP") at debug.c:823:2 [opt]
frame #1:
@xfffffeG0186175c8 kernel.release.t8122° panic_trap_to_debugger(panic_format_str="%s %s%s%s\n%s", panic_args=Oxfffffe8f15497db8, reason=0, ctx=0x0000000000000000, panic_options_mask=16384, pa
nic_data_ptr=0x0000000000000000, panic_caller=18446741875144245264, panic_initiator="DCP") at debug.c:1334:2 [opt]
frame #2:
le>) at debug
frame #3:
frame #4:
frame #5:
frame #6:
frame #7:
[(lldb) memory
Oxfffffee0185cd8a8 kernel.release.t8122°Call_continuation + 200
handleCrashlog(bool) + 1368
checkForWork() + 124
Oxfffffe29a67281c0: 74 61 73 6b 20 73 74 61 63 6b 20 66 72 61 6d 65 task stack frame
```

## Slide 59

## From AP user mode to DCP firmware

It's worth mentioning that this vulnerability can be directly triggered from user mode without requiring any entitlement. Furthermore, many key registers within the DCP firmware are controllable.

Case #8 - CVE-2025-24111

#BHUSA @BlackHatEvents

## Slide 60

# Conclusions and Takeaways

#BHUSA @BlackHatEvents

## Slide 61

## Recalling the previously mentioned kernel architecture

3D
Browser ...... Gaming
Modeling
Application
Runtime Framework
Vertex Fragment Accelerated Shading
Processing Generation Encryption Language
Primitive Framebuffer Decryption Interpreter
Assembly Operation Compression & LLVM
Wrapper Layer: libDRM, etc.
User Mode
Kernel Mode
IOGraphicsFamily/IOGPUFamily
AppleIntelSKLGraphicsF ramebuffer AGPM
...... AGX AMDSupport AGDCPluginDisplayMetrics
Accelerator ...... AppleGraphicsDeviceControl
Ap pleIntelKBL
AMDFramebuffer ......
A ppleIntelICL
IOMobileFramebuffer/IOMobileGraphicsFamily
IOMobileGraphicsFamily-DCP/DCPDP/AVFamily
Central Processing Unit/Application Processor
RTBuddy
Graphics Processing Unit
GPU OS/Hypervisor RTKit
Firmware RTOS
Display Co-processor (DCP) Firmware

"Dead pixel detected" - A Security Assessment of Apple's Graphics Subsystem

#BHUSA @BlackHatEvents

## Slide 62

## There remains room for improvement

3D
Browser ...... Gaming
Modeling
Application
Runtime Framework
Vertex Fragment Accelerated Shading
Processing Generation Encryption Language
Primitive Framebuffer Decryption Interpreter
Assembly Operation Compression & LLVM
Wrapper Layer: libDRM, etc.
User Mode
CVE-2024-40854
Kernel Mode
IOGraphicsFamily/IOGPUFamily ......
AppleIntelSKLGraphicsF ramebuffer AGPM
CVE-2025-24273 ...... AGX AMDSupport AGDCPluginDisplayMetrics
OE0964116966483 Accelerator ...... AppleGraphicsDeviceControl
Ap pleIntelKBL CVE-2020-27914
CVE-2022-22661 AMDFramebuffer ...... CVE-2022-22631
A ppleIntelI C VEL -2025-24257 CVE-2020-27936
......
CVE-2022-46706
CVE-2019-8807 IOMobileFramebuffer/IOMobileGraphicsFamilyCVE-2024-44197 CVE-2020-27915 CVE-2024-44197
......
CVE - 2021 - 30678
CVE-2018-4418 IOMobileGraphicsFamily-DCP/DCPDP/AVFamily OE098868205995
......
CVE-2018-4396 ...... Central Processing Unit/Application Processor
RTBuddy
CVE-2018-4350
Graphics Processing Unit
CVE-2017-13883
GPU OS/Hypervisor RTKit
CVE-2017-7163
Firmware RTOS CVE-2025-24111
CVE-2017-7155
OE09704917815
"Dead pixel detected" -......
A Security Assessment of Apple's Display Co-processor (DCP) Firmware ......
Graphics Subsystem

#BHUSA @BlackHatEvents

## Slide 63

## From the perspective of security engineering

1. New features always mean new attack surfaces. Reckless refactoring can sometimes bring catastrophic consequences to a system.

2. Even in the era of AI and vibe coding, we still need to attach great importance to the programming fundamentals of C/C++, the training related to code quality, the routine use of static and dynamic dev tools, and the regular review of warning messages. 3. The emergency and official patches for CVE-2024-44199 reflect that the engineering team's handling of classic C/C++ issues, such as "comparison between signed and unsigned integer expressions" is somewhat casual. If it is caused by the lack of guidance, the first step should be to formulate these specifications and conduct training.

#BHUSA @BlackHatEvents

## Slide 64

## From the perspective of vulnerability hunting

1. Certain complex kernel functions are repeatedly found to contain vulnerabilities by the security community. I have identified numerous such cases within Apple's Bluetooth, Wi-Fi, and graphics subsystems.

2. In terms of the number of kernel vulnerabilities, the graphics subsystem of the Apple Silicon platform deviates from the theoretical error rate per ten thousand lines of binary code. I believe that security issues in components like the Apple Graphics Accelerator and Display Co-processor are concealed by the complex architecture. Obviously, hiding behind does not mean security.

#BHUSA @BlackHatEvents

## Slide 65

## From the perspective of vulnerability hunting (cont.)

3. Significant knowledge gaps exist across multiple domains including AGX GPU 13/14/15, G/X/C/S-series, DCP firmware, RTKit subsystem, and RTBuddy V1/V2 architectures. The inherent asymmetry of knowledge coupled with capability disparities will further widen the gap in vulnerability research within the security community.

#BHUSA @BlackHatEvents

## Slide 66

## From the perspective of offensive and defensive

1. The competition between the offensive and defensive sides in fields such as IOMobileFrameBuffer once reached a fever pitch.

2. An analysis of IOMobileFrameBuffer/IOMobileGraphicsFamily/AppleCLCD from 2020 to 2022 indicates the lag in vulnerability research is approximately three to six months. 3. The practice of transferring functionalities of kernel extensions such as IOMobileFramebuffer to the Display Co-processor firmware is effective to a certain extent. This mitigation measure restricts access to select high-risk interfaces exposed within WebContent, thereby implicitly introducing the concept of defense-in-depth. But once again, hiding behind does not mean security.

#BHUSA @BlackHatEvents

## Slide 67

Q&A

- "Dead pixel detected" A Security Assessment of Apple's Graphics Subsystem

#BHUSA @BlackHatEvents
