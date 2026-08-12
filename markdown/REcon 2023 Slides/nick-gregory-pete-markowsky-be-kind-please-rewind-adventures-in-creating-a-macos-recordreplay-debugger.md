---
title: "Be Kind, Please Rewind Adventures in creating a macOS recordreplay debugger"
speakers: ["Nick Gregory", "Pete Markowsky"]
conference: "REcon"
conference_full: "REcon 2023"
edition: ""
year: 2023
source_pdf: "REcon 2023 Slides/Nick Gregory & Pete Markowsky_Be Kind, Please Rewind Adventures in creating a macOS recordreplay debugger.pdf"
pages: 53
sha256: "191901f023247451592c197dfaec12d8b06ba331dfaea79c65a617caf05fda0a"
text_chars: 11394
ocr_pages: 9
has_ocr: true
redacted_secrets: 0
ocr_confidence: 90.3
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T06:03:59Z"
---
# Be Kind, Please Rewind Adventures in creating a macOS recordreplay debugger

**Speakers:** Nick Gregory, Pete Markowsky  
**Conference:** REcon 2023  
**Source:** `REcon 2023 Slides/Nick Gregory & Pete Markowsky_Be Kind, Please Rewind Adventures in creating a macOS recordreplay debugger.pdf` (53 pages)


## Slide 1

Be Kind, Please Rewind Adventures in creating a macOS record/replay debugger

## Slide 2

**LEGAL**


> Recovered by OCR — confidence 96/100 on the text kept, 96/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
LEGAL
WARNING
Federal law provides severe civil and crimi-
nal penalties for the unauthorized re-
production, distribution or exhibition of
copyrighted motion pictures, video tapes
or video discs.
Criminal copyright infringement is investi-
gated by the FBI and may constitute a
felony with a maximum penalty of up to five
years in prison and/or a $250,000 fine.
```

## Slide 3

## Slide 4

# Why?

NSURLSessionDataTask *task = [_session dataTaskWithRequest:request completionHandler:^(NSData *_Nullable data, NSURLResponse *_Nullable response, NSError *_Nullable err) {

… ***stop = YES;**

Thread 2 Crashed::  Dispatch queue: com.apple.NSXPCConnection.user.com.google.santa.metricservice.63335 0   libobjc.A.dylib       objc_msgSend + 29

1   Foundation            -[NSError copyWithZone:] + 107

2   santametricservice    -[SNTMetricHTTPWriter write:toURL:error:] + 1372

- 3   santametricservice    -[SNTMetricService exportForMonitoring:] + 475

## Slide 5

# Record/Replay: Prior Art

- PANDA (2020)

- Whole system!

- ● WinDbg (2017)

- ● RR (2014)

- ● Scribe (2010)

- ● Jockey (2005)

- ● Flashback (2004)

- ReTrace

- QuickRec

- Revirt (1999)

   - Whole system!

## Slide 6

# Record/Replay: Prior Art

- PANDA (2020) ○ Whole system!

- ● WinDbg (2017)

- ● RR (2014)

- ● Scribe (2010)

- ● Jockey (2005)

- ● Flashback (2004)

- ReTrace

- QuickRec

- ● Revirt (1999)

- Whole system!

## Slide 7

Record / Replay Basics & Goals

## Slide 8

## Slide 9

## Slide 10

# Goals for our tool

- Only focusing on user-space programs

- Easy to use and deploy – needs to support a stock MBP with/M1,M2

- No DBI / code instrumentation

- Small investment of effort to maintain

- Fast enough to use on real programs

## Slide 11

# RR’s Requirements for User-Space Replay

**Requirement Does macOS Meet This Out of the Box?** Ability to Record Syscalls Ability to Record Syscalls Outside Libc

Ability to determine if a Syscall is blocking

Ability to Intercept Signals

## Slide 12

# RR’s Requirements for User-Space Replay (Part 2)

**Requirement**

**Does macOS Meet This Out of the Box?**

Ability to pin a process to a single core (cpuset)

Ability to trap non-deterministic instructions

Ability to access reliable and deterministic hardware performance counters

## Slide 13

Recording

## Slide 14

# Recording: It’s not that simple…

- Mach traps

   - Close enough to syscalls, no big deal

- … except for a few traps which don’t have normal hook points

- ● Signals

   - The outside world can “asynchronously” poke the target

- mmap

- Multithreading

- Well-formed programs shouldn’t have issues (data races), but…

- ○ Aside: thanks Apple for not giving us cpuset - no easy way to pin to one core

- ● Commpage

- Similar to vvar (normally accessed via vDSO) on Linux

- ● Non-deterministic instructions – mrs x0, cntvct_el0

## Slide 15

Recording: Syscalls & Traps

## Slide 16

# Recording: Syscalls on macOS

- 3 types – BSD, mach traps, machine dependent

● Need pre- and post-hooks for data gathering


> Recovered by OCR — confidence 88/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Recording: Syscalls on macOS
e 3 types — BSD, mach traps, machine dependent
e Need pre- and post-hooks for data gathering
Record
Syscall
Results
```

## Slide 17

# Thanks Apple

- Gutted ptrace implementation – no sysemu

- No seccomp-bpf equivalent

## Slide 18

# One Option: dtrace

- dtrace hooks, storage, etc.

- Not enough to capture arbitrary syscall data though ○ No conditionals for example - not possible to switch in “multiplexed” syscalls

- Strictly async

   - How to pause so userland can get what it needs?

   - Luckily there are “destructive” actions

      - signal(STOP)

      - stop() - mach_task_suspend

   - These only take effect _after_ the syscall is processed though…

## Slide 19

One Option: dtrace

## Slide 20

# Seatbelt / Sandbox?

- Seatbelt is wired up into every syscall maybe?

- Trace mode for recording

   - Not a good API, minimal log entries

- No way to not kill on replay

## Slide 21

# Interposing / Dynamic Interposing / Symbol Rebinding

- macOS is a BSD!

   - ABI compatibility is at the libc level not the kernel

   - Can we just hook libsystem_kernel?

- We can interpose on the symbol

   - Could use <u>fishhook</u>

- Doesn’t catch direct syscalls…

## Slide 22

Recording: Dealing with Data Races


> Recovered by OCR — confidence 91/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Recording: Dealing with Data Races
=
```

## Slide 23

## Slide 24

# How Does RR Handle This?

- Only runs one thread to run at a time (non-parallel)

- ● Limits threads to the same core using processor affinity

- ● Schedules threads and records the choice in the log ( **can mixup order on replay to find bugs** )

## Slide 25

# Thread scheduling on macOS not guaranteed

- No cpu_set(3)

- Can we use THREAD_AFFINITY_POLICY?


> Recovered by OCR — confidence 91/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Thread scheduling on macOS not guaranteed
e Nocpu_ set (3)
e Canwe use THREAD AFFINITY POLICY?
* thread_bind:
*
* Force the current thread to execute on the specified processor.
* Takes effect after the next thread _block().
*
* Returns the previous binding. PROCESSOR_NULL means
* not bound.
*
* XXX - DO NOT export this to users - XXX
*/
thread_bind(
{
thread_t self = current_thread();
```

## Slide 26

# P-cores and E-cores

From: https://eclecticlight.co/2022/01/13/scheduling-of-processes-on-m1-series-chips-first-draft/


> Recovered by OCR — confidence 79/100 on the text kept, 55/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
P-cores and E-cores
Scheduling of Threads on M1 series Chips (draft 0.2)
+
Operation
Seong Mt Pro and Max (MIP) chips
M1 P cluster
ancl 4 thread slots 4 thread slots
frequency ~2 GHz MiP PO cluster
How many threads? 2cores i1P Pt cluster
From: https://eclecticlight.co/2022/01/13/scheduling-of-processes-on-m1-series-chips-first-draft/
```

## Slide 27

# Can we shutdown cores?

● In the old OS X internals books there was an example showing how to shutdown cores using processor_exit ● Can we just limit ourselves to a core?

**[** user@watervile **~ ]** $  sudo ./print_processors Password:

Number of processors: 12 CPU: slot 0(master) CPU: slot 1 //snipped. CPU: slot 11 **[** user@waterville **~ ]** $  sudo ./processor_xable processor_exit: (os/kern) service not supported

## Slide 28

Recording: Asynchronous Events

## Slide 29

## Signals & Scheduling

- Need to be able to intercept signals and record register state of where the signal was delivered or program interrupted for scheduling.

- Need to know where you are in the programs execution so you can inject your signals in the right place during replay

- Replay: when using something interrupt driven must account for late firing interrupts

## Slide 30

## Using PMUs from macOS

- RR works on Asahi Linux and uses the PMU can we?

   - Uses the count of retired conditional branches as progress indicator  (0x8c)

   - ○ Can reset for an interrupt when replaying

- macOS does not have an interface for setting PMUs from EL0

[ user@waterville  ~/src/pmu_counters  ]

$  sudo ./counter_test loaded db: a15 (Apple A15) number of fixed counters: 2 number of configurable counters: 8 counters value:

cycles: 41865278 instructions: 91998218 **branches: 21071096 branch-misses: 53779** [ user@waterville  ~/src/pmu_counters  ] $  sudo ./counter_test

loaded db: a15 (Apple A15) number of fixed counters: 2 number of configurable counters: 8 counters value:

cycles: 41946121 instructions: 92093331 **branches: 0 branch-misses: 0**

## Slide 31

panic(cpu 5 caller 0xfffffe0017c66cd8): kperf: timer fired at 2793246644070, but sampling is disabled @kptimer.c:328 Debugger message: panic

## Slide 32


> Recovered by OCR — confidence 93/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Supporting Nondeterministic Execution in Fault-Tolerant Systems*
J. Hamilton Slye
Dept. of Electrical and Computer Engineering
Carnegie Mellon University
ham+@cmu.edu
Abstract
We present a technique to track nondeterminism re-
sulting from asynchronous events and multithreading
in i log-based rollback-recovery protocols, This tech-
E.N. Elnozahy
Department of Computer Science
Carnegie Mellon University
mootaz@cs.cmu.edu
with the end users [11]. Efficient tracking of non-
determinism is thus crucial to supporting interactive
applications [14].
Different flavors of logging have been suggested
with different performance and resilience character-
Decrement Register
Branch to handler if register = 0
```

## Slide 33

## Options without PMU or DBI

- We can count the number of syscalls and then single step forward then inject the signal (set a breakpoint and invoke the signal handler)

- Do what scribe(10) does and simply deliver the signal at the next syscall and replay interrupted syscall (special case for signals like SIGSEGV that originate in user space.)

- If we need to go further than say 10,000 instructions we can use an high res clock (e.g. pacman) to trap back to us

## Slide 34

Darling

## Slide 35

## Darling

- “A Translation Layer that lets you run macOS software on Linux”

- Uses a custom loader, interposing of libsystem_kernel, a lot of duct tape code and userland a server to translate macOS syscalls to Linux syscalls

- Can run software like xcode on Linux

## Slide 36

High Level: How Darling Works

## Slide 37

Warpspeed

## Slide 38

# Warpspeed

- Isolate target inside a VM with 1 core

- ● Proxy syscalls

- Both signal slide + SoftPMU to approximate program progression

- ● Manual thread scheduling

## Slide 39

# Hypervisor.framework

- Super light-weight framework

   - Little as possible in the kernel

- Usage:

   - Create a VM

   - Map memory (from hypervisor address space)

   - Create vCPU

   - Set regs

   - Run

   - Trap out to <u>userland</u> on VM exit

   - GOTO 5

   - _That’s it_

## Slide 40

# Warpspeed: VM/Hypervisor

- Use modified darling’s loader (mldr) to map in target program and dyld

- ● Load in shared cache

- “Share” an address space with the guest

- 1:1 map the regions of the loaded target into VM at the same virtual address

- ● Trap out and forward syscalls

- All based on Hyperpom (Rust!)

- Lets us control the execution of the program perfectly

   - Only have one virtual core

   - Manually schedule threads

## Slide 41

Warpspeed: VM/Hypervisor


> Recovered by OCR — confidence 94/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Tracee Warpspeed Kernel
Calls getpid() and traps to Warpspeed
Record Syscall Args / Snapshot if necessary
Setup stack and registers with shared memory
getpid()
Record Syscall result and memory updates
Start Tracee with new register state
Tracee Warpspeed Kernel
```

## Slide 42

## Slide 43

dyld

## Slide 44

# Warpspeed: Unimplemented Features

- LLDB/GDB interface

- Optimizing/compressing log format

- The hypervisor itself is responsible for performing the syscalls

   - What happens on a blocking call?

   - Could deadlock on mutex wait

- Handling blocking syscalls

   - Manually enumerate and perform some non-blocking alternative

   - or…

## Slide 45

## Slide 46

Warpspeed: VM/Hypervisor


> Recovered by OCR — confidence 91/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Trace Warpspeed pthread Kernel
Calls getpid() and traps to Warpspeed
Record Syscall Args / Snapshot if necessary
spawn new pthread for syscall
take syscall mutex
Setup stack and registers with shared memory
{>
getpid()
release syscall mutex
getPid() result
Record Syscall result and memory updates
Start Tracee with new register state
Trace Warpspeed pthread Kernel
```

## Slide 47

Warpspeed: VM/Hypervisor


> Recovered by OCR — confidence 89/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Tracee Warpspeed pthread Kernel
and traps to Warpspeed
Syscall Args / Snapshot if necessary
n new pthread for syscall
take syscall mutex
Setup stack and regi shared memory
release syscall
{t and memory updates
new register state
Tracee Warpspeed pthread Kernet
```

## Slide 48

# Warpspeed: Outstanding Issues

### ● MMIO

### ● Entitlements

## Slide 49

That’s Only Half the Battle

## Slide 50

# Replay

- If you can figure out recording, replay is much simpler

   - Set breakpoints where something happened in recording

   - ○ Mimic side-effects

   - Continue

- SoftPMU needed here in case we end up with an async event in a hot loop

## Slide 51

# Replay: GUI

- UI is core to macOS

- How can we “pass through” events on replay to the OS (to see the app running) while not introducing nondeterminism?

   - _In theory_ it will “just work”

   - No (easy) way to show the UI on replay though

## Slide 52

# Recap

### ● Tool is WIP

- But principles work!

- ● Stay posted for more

## Slide 53

Questions?
