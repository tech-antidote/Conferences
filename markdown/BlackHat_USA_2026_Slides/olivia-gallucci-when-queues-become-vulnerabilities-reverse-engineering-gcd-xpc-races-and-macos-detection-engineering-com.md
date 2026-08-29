---
title: "When Queues Become Vulnerabilities Reverse Engineering GCD, XPC Races, and macOS Detection Engineering"
speakers: ["Olivia Gallucci"]
conference: "Black Hat"
conference_full: "Black Hat USA 2026"
edition: "USA"
year: 2026
source_pdf: "BlackHat_USA_2026_Slides/Olivia Gallucci_When Queues Become Vulnerabilities Reverse Engineering GCD, XPC Races, and macOS Detection Engineering_Compressed.pdf"
pages: 86
sha256: "525b143eab3c90256caaaf30afb4138c697066c085948e1ab04656533dbcb31d"
text_chars: 24076
ocr_pages: 6
has_ocr: true
redacted_secrets: 0
ocr_confidence: 92.2
ocr_unreliable_blocks: 0
vision_verified_pages_changed: 86
vision_verified_pages: 86
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T05:40:46Z"
---
# When Queues Become Vulnerabilities Reverse Engineering GCD, XPC Races, and macOS Detection Engineering

**Speakers:** Olivia Gallucci  
**Conference:** Black Hat USA 2026  
**Source:** `BlackHat_USA_2026_Slides/Olivia Gallucci_When Queues Become Vulnerabilities Reverse Engineering GCD, XPC Races, and macOS Detection Engineering_Compressed.pdf` (86 pages)


## Slide 1

$ macOS detecting race-conditions

Olivia Gallucci @ Datadog
Black Hat

prev. Apple,  SECUINFRA GmbH,  U.S. Govt.
Aug 2026

## Slide 2

$ whatis vocabulary

## Slide 3

# Processes are runnable entities.

Jonathan Levin

## Slide 4

# Processes are _not_ runnable entities.

Jonathan Levin

## Slide 5

The process itself is technically only a container for one or more threads, and provides the virtual memory image, the descriptors and ports shared by all the threads.

Thus, when one refers to a process as “executing,” the correct terminology is “at least one of the threads of the process pid is executing.”

Jonathan Levin

## Slide 6

**Concurrent**: 2 queues, 1 vending machine

iCode - https://www.youtube.com/watch?v=X9H2M7xMi9E

## Slide 7

**Concurrent**: 2 queues, 1 vending machine

Interleavings

Time ↓

```
T1:  A: read x
     B: x = x + 1
     C: write x

T2:      D: read x
         E: x = x + 1
         F: write x
```

```
One Possible Interleaving
T1:  A     B     C
T2:     D     E     F
```

iCode - https://www.youtube.com/watch?v=X9H2M7xMi9E

## Slide 8

**Concurrent**: 2 queues, 1 vending machine

**Parallel**: 2 queues, 2 vending machines

Interleavings

Time ↓

```
T1:  A: read x
     B: x = x + 1
     C: write x

T2:      D: read x
         E: x = x + 1
         F: write x
```

```
One Possible Interleaving
T1:  A     B     C
T2:     D     E     F
```

iCode - https://www.youtube.com/watch?v=X9H2M7xMi9E

## Slide 9

Concurrency

Parallelism

## Slide 10

$ ssh gcd@apple.com

## Slide 11

# Grand Central Dispatch

Task Queue

Thread Pool

Completed Tasks

iCode - https://www.youtube.com/watch?v=X9H2M7xMi9E
tclementdev - https://tclementdev.com/posts/what_went_wrong_with_the_libdispatch.html

## Slide 12

Dispatch Queue
Task Task Task

Thread → Task → Task → Task
Thread
Thread

Vlog

## Slide 13

Developer   Get Started   Platforms   Technologies   Community   Documentation   Downloads   Support

Documentation                    Language: Swift

< All Technologies

Dispatch

Queues and Tasks
- DispatchQueue
- DispatchWorkItem
- DispatchGroup
- Dispatch Queue
- Dispatch Work Item
- Dispatch Group
- Workloop

Thread Scheduling
- DispatchQoS

System Event Monitoring
- DispatchSource
- Dispatch Source
- DispatchIO
- DispatchData
- DispatchDataIterator
- Dispatch I/O
- Dispatch Data
- DispatchSourceProtocol

Filter

Framework

# Dispatch

Execute code concurrently on multicore hardware by submitting work to dispatch queues managed by the system.

iOS 8.0+ | iPadOS 8.0+ | Mac Catalyst 13.0+ | macOS 10.10+ | tvOS 9.0+ | visionOS 1.0+ | watchOS 2.0+

## Overview

Dispatch, also known as Grand Central Dispatch (GCD), contains language features, runtime libraries, and system enhancements that provide systemic, comprehensive improvements to the support for concurrent code execution on multicore hardware in macOS, iOS, watchOS, and tvOS.

The BSD subsystem, Core Foundation, and Cocoa APIs have all been extended to use these enhancements to help both the system and your application to run faster, more efficiently, and with improved responsiveness. Consider how difficult it is for a single application to use multiple cores effectively, let alone to do it on different computers with different numbers of computing cores or in an environment with multiple applications competing for those cores. GCD, operating at the system level, can better accommodate the needs of all running applications, matching them to the available system resources in a balanced fashion.

## Dispatch Objects and ARC

When you build your app using the Objective-C compiler, all dispatch objects are Objective-C objects. As such, when automatic reference counting (ARC) is enabled, dispatch objects are retained and released automatically, just like any other Objective-C object. When ARC is not enabled, use the `dispatch_retain` and `dispatch_release` functions (or Objective-C semantics) to retain and release your dispatch objects. You cannot use the Core Foundation retain and release functions.

Vlog

## Slide 14

# Quality of Service (QoS)

User Interactive
Utility
Background

iCode- https://www.youtube.com/watch?v=yH0RBTdNi3U

## Slide 15

Unspecified    Default

User Interactive    User Initiated

Utility    Background

iCode- https://www.youtube.com/watch?v=yH0RBTdNi3U

## Slide 16

# Quality of Service (QoS)

- **User Interactive**: Animations or tasks that update the UI immediately.
- **User Initiated**: Tasks required for a seamless user experience, such as loading data for a scrolling table view.
- **Utility**: Long-running tasks where user is aware of progress (e.g., downloads).
- **Background**: Tasks user is unaware of, such as backups or server restoration.
- **Default & Unspecified**: Default falls between User Initiated and Utility. Unspecified indicates missing QoS information and has the lowest priority.

Apple - https://developer.apple.com/documentation/dispatch/dispatchqos
Apple - https://developer.apple.com/documentation/foundation/qualityofservice
Apple - https://developer.apple.com/documentation/dispatch/dispatch_queue_attr_make_with_qos_class
Dr. Howard Oakley - https://eclecticlight.co/2021/05/17/how-m1-macs-feel-faster-than-intel-models-its-about-qos/

## Slide 17

# Public APIs

- Swift/ObjC (Foundation)
  - `QualityOfService` (`userInteractive`, `userInitiated`, `utility`, `background`, plus `default`).
- Swift (Dispatch)
  - `DispatchQoS` / `DispatchQoS.QoSClass` with the same classes
  - System prioritizes higher QoS work when scheduling
- C (libdispatch)
  - queue attributes and global queues take `QOS_CLASS_*` constants (e.g., `QOS_CLASS_USER_INTERACTIVE`, `..._USER_INITIATED`, `..._UTILITY`, `..._BACKGROUND`)

## Slide 18

# Quality of Service (QoS)

- **User Interactive**: Animations or tasks that update the UI immediately.
- **User Initiated**: Tasks required for a seamless user experience, such as loading data for a scrolling table view.
- **Utility**: Long-running tasks where user is aware of progress (e.g., downloads).
- **Background**: Tasks user is unaware of, such as backups or server restoration.
- **Default & Unspecified**: Default falls between User Initiated and Utility. Unspecified indicates missing QoS information and has the lowest priority.

Apple - https://developer.apple.com/documentation/dispatch/dispatchqos
Apple - https://developer.apple.com/documentation/foundation/qualityofservice
Apple - https://developer.apple.com/documentation/dispatch/dispatch_queue_attr_make_with_qos_class
Dr. Howard Oakley - https://eclecticlight.co/2021/05/17/how-m1-macs-feel-faster-than-intel-models-its-about-qos/

## Slide 19

Hackers on the Rocks - https://www.youtube.com/watch?v=9sqoR2qGp0w
Olivia Gallucci - https://oliviagallucci.com/how-to-manipulate-the-execution-flow-of-toctou-attacks/

## Slide 20

Podcast Episode
How Hackers Exploit Milliseconds - TOCTOU Attacks
Hackers On The Rocks
Video • Jul 7, 2025 • 32 min 34 sec

gotta do the self promo

How to manipulate the execution flow of TOCTOU attacks ([ret]2read)

Hackers on the Rocks - https://www.youtube.com/watch?v=9sqoR2qGp0w
Olivia Gallucci - https://oliviagallucci.com/how-to-manipulate-the-execution-flow-of-toctou-attacks/

## Slide 21

Hackers on the Rocks - https://www.youtube.com/watch?v=9sqoR2qGp0w
Olivia Gallucci - https://oliviagallucci.com/how-to-manipulate-the-execution-flow-of-toctou-attacks/

## Slide 22

$ cd /vulnerabilities

## Slide 23

# Priority Inversion and QoS Mismatches

3-Thread Swimlane: L holds lock, H blocks, M runs

high priority

low priority

https://news.ycombinator.com/item?id=41724168

## Slide 24

# Priority Inversion and QoS Mismatches

3-Thread Swimlane: L holds lock, H blocks, M runs

high priority

medium priority

low priority

https://news.ycombinator.com/item?id=41724168

## Slide 25

# Priority Inversion and QoS Mismatches

3-Thread Swimlane: L holds lock, H blocks, M runs

low priority

high priority

https://news.ycombinator.com/item?id=41724168

## Slide 26

# Priority Inversion and QoS Mismatches

3-Thread Swimlane: L holds lock, H blocks, M runs

Assume priorities: H > M > L. Shared resource protected by mutex R.

```
Time ↓

L (low):    lock(R)    [critical section..............]    unlock(R)
H (high):          tries lock(R) -> BLOCKED ................... runs
M (med):                     runs............... runs.......... (preempts L)
```

- L acquires R.
- H becomes runnable, needs R, blocks on L.
- While H is blocked, M runs (preempts L), so L can’t finish and release R.
- Result: H is indirectly delayed by M (lower priority than H), which is the inversion.

https://news.ycombinator.com/item?id=41724168

## Slide 27

# Does Apple implement priority inheritance anywhere?

Next few slides are a simplification, but gets the point across

## Slide 28

mutex vs unfair

unfair vs spinlock

spinlock vs semaphores

## Slide 29

### `pthread_mutex_t` (blocks/sleeps, scheduler can help)

```
static pthread_mutex_t gMutex = PTHREAD_MUTEX_INITIALIZER;

pthread_mutex_lock(&gMutex);   // contended: thread can sleep
// critical section
pthread_mutex_unlock(&gMutex);
```

### `os_unfair_lock` (Darwin replacement for spin)

```
static os_unfair_lock gLock = OS_UNFAIR_LOCK_INIT;

os_unfair_lock_lock(&gLock);   // contended: waiter parks
// critical section
os_unfair_lock_unlock(&gLock);
```

https://blog.xoria.org/macos-tips-threading/
https://developer.apple.com/documentation/os/os_unfair_lock
https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/pthread_mutex_init.3.html

## Slide 30

mutex vs unfair

unfair vs spinlock

spinlock vs semaphores

## Slide 31

### `pthread_mutex_t` (blocks/sleeps, scheduler can help)

```
static pthread_mutex_t gMutex = PTHREAD_MUTEX_INITIALIZER;

pthread_mutex_lock(&gMutex);   // contended: thread can sleep
// critical section
pthread_mutex_unlock(&gMutex);
```

### `os_unfair_lock` (Darwin replacement for spin)

```
static os_unfair_lock gLock = OS_UNFAIR_LOCK_INIT;

os_unfair_lock_lock(&gLock);   // contended: waiter parks
// critical section
os_unfair_lock_unlock(&gLock);
```

https://blog.xoria.org/macos-tips-threading/
https://developer.apple.com/documentation/os/os_unfair_lock
https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/pthread_mutex_init.3.html

## Slide 32

### `os_unfair_lock` (Darwin replacement for spin)

```
static os_unfair_lock gLock = OS_UNFAIR_LOCK_INIT;

os_unfair_lock_lock(&gLock);   // contended: waiter parks
// critical section
os_unfair_lock_unlock(&gLock);
```

### Plain spinlock (bad under mixed QoS)

```
static atomic_flag gSpin = ATOMIC_FLAG_INIT;

while (atomic_flag_test_and_set_explicit(&gSpin, memory_order_acquire)) {
  /* spins: keeps running, burns CPU */
}
// critical section
atomic_flag_clear_explicit(&gSpin, memory_order_release);
```

Luna Razzaghipour - https://blog.xoria.org/macos-tips-threading/
https://developer.apple.com/documentation/os/os_unfair_lock
https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/pthread_mutex_init.3.html

## Slide 33

mutex vs unfair

unfair vs spinlock

spinlock vs semaphores

## Slide 34

mutex vs unfair

unfair vs spinlock

spinlock vs semaphores

## Slide 35

# With QoS inheritance (`pthread_mutex` / `os_unfair_lock`)

Lock tracks ownership; kernel can temporarily boost the owner to resolve inversion

```
time →
High QoS (Q=UI) :  lock() ── BLOCKED ─────────────────────── RUN (after unlock)
Low  QoS (Q=BG) :  RUN ── holds lock ──(BOOST to UI)─ RUN ── unlock()
CPU scheduling  :         runs boosted BG owner so it can release sooner
```

```
typedef NSObject<OS_dispatch_semaphore> * dispatch_semaphore_t;
```

* “With QoS inheritance (pthread_mutex / os_unfair_lock)” is really “with **potential** QoS inheritance.” Apple’s wording is deliberately hedged (“may use to attempt”).

## Slide 36

# With QoS inheritance (`pthread_mutex` / `os_unfair_lock`)

Lock tracks ownership; kernel can temporarily boost the owner to resolve inversion

```
time →
High QoS (Q=UI) :  lock() ── BLOCKED ─────────────────────── RUN (after unlock)
Low  QoS (Q=BG) :  RUN ── holds lock ──(BOOST to UI)─ RUN ── unlock()
CPU scheduling  :         runs boosted BG owner so it can release sooner
```

# Without QoS inheritance (semaphore / rwlock / custom)

Waiter can’t donate QoS/priority to the owner, so the high-QoS thread stalls

```
time →
High QoS (Q=UI) :   wait() ── BLOCKED ───────────────────────────────────
Low  QoS (Q=BG) :   READY ───────────(not boosted)────────── RUN ── signal()
CPU scheduling  :   keeps running other work; BG owner may not run promptly
```

* “With QoS inheritance (pthread_mutex / os_unfair_lock)” is really “with **potential** QoS inheritance.” Apple’s wording is deliberately hedged (“may use to attempt”).

## Slide 37

mutex vs unfair

unfair vs spinlock

spinlock vs semaphores

## Slide 38

./detection

## Slide 39

This slide carries no title or text of its own.

## Slide 40

# Edit Scheme… > Run > Diagnostics > Runtime API Checking and check “Thread Performance Checker”

GRDB - https://github.com/groue/GRDB.swift/issues/1234

## Slide 41

Thread running at `QOS_CLASS_USER_INTERACTIVE` waiting on a lower QoS thread running at `QOS_CLASS_DEFAULT`. Investigate ways to avoid priority inversions.

GRDB - https://github.com/groue/GRDB.swift/issues/1234

## Slide 42

Thread running at `QOS_CLASS_USER_INTERACTIVE` waiting on a lower QoS thread running at `QOS_CLASS_DEFAULT`. Investigate ways to avoid priority inversions.

GRDB - https://github.com/groue/GRDB.swift/issues/1234
Luna Razzaghipour - https://blog.xoria.org/macos-tips-threading/

## Slide 43

./dispatch-sync-deadlocks

## Slide 44

dispatch_sync

circular wait scanning

## Slide 45

# understanding `dispatch_sync` & deadlocks

## synchronous execution (normal case)

Caller Queue (Main Thread)
Target Queue (Background Thread)

dispatch_sync

Task Block

Caller blocks & waits

Task Complete, Unblock Caller

## deadlock scenario (problem case)

Caller Queue (Main Thread)

dispatch_sync

Queue is BLOCKED by the call

Task CANNOT start

Zeeshan Khan - https://izeeshan.wordpress.com/tag/multithreading/
Apple - https://developer.apple.com/documentation/dispatch/dispatchqueue/sync

## Slide 46

dispatch_sync

circular wait

scanning

Main Dispatch Queue

## Slide 47

# understanding `dispatch_sync` deadlocks

## the main queue pitfall

safe: targeting a _different_ queue (e.g., background)

Main Queue (Serial)
Background Queue (Concurrent)

dispatch_sync

Task Block

Task Complete, Unblock Main

deadlock: targeting the _main_ queue from the main thread

```
dispatch_sync(dispatch_get_main_queue(), ...)
```

Task Block

Main Queue (Serial)

## Slide 48

# circular wait

## setup & trigger

main thread (serial queue)

1. main thread queues tasks to background threads

dispatch_sync(main_queue)   dispatch_sync(main_queue)   dispatch_sync(main_queue)

background worker threads (concurrent queue)

…

2. background threads block, waiting for main thread

## deadlock (circular wait)

main thread (serial queue) — dispatch_sync() → system API / global queue

3. main thread makes synchronous call, waiting for a worker thread

main thread
waits for   deadlock   waits for
background worker threads

4. circular wait: main thread waits for workers, workers wait for main thread. app freezes.

https://blog.stevex.net/2012/09/avoid-dispatch_sync/

## Slide 49

dispatch_sync

circular wait

scanning

## Slide 50

# deadlock scenario

## `dispatch_sync` on serial queue

service handler (serial listener queue)

callback execution

dispatch_sync call?

no (different queue) → continue execution

**yes**, targeting **same** queue → **deadlock** (waiting for self)

guaranteed to deadlock service

## Slide 51

$ brew uninstall resource-starvation

## Slide 52

# Resource Starvation & GCD

## thread pool saturation

DISPATCH_ASYNC (huge volume / blocking)

Task Task
Task Task
Task Task

concurrent queue tasks

worker thread pool saturated

- misusing GCD can lead to resource starvation
- GCD uses a thread pool for concurrent tasks
- saturating the pool staves other tasks of CPU/threads

## Slide 53

# Grand Central Dispatch

Task Queue

Thread Pool

Completed Tasks

iCode - https://www.youtube.com/watch?v=X9H2M7xMi9E
tclementdev - https://tclementdev.com/posts/what_went_wrong_with_the_libdispatch.html

## Slide 54

dispatch queue

Task Task Task
Task Task
Task

many tasks queued

thread pool

worker thread
worker thread   worker thread

all threads busy (blocking)

starving task / component

starved of resources

Y Combinator - ıhttps://news.ycombinator.com/item?id=41724168

## Slide 55

This slide carries no title or text of its own.

## Slide 56

# historical context

## abandoned API (macOS 10.7)

Task

security transforms: new queue/thread per task

caused severe thread proliferation

## rewrite (iOS 12)

Task 1
Task 2
Task 3

single-threaded daemons

improved performance, unconstrained concurrency can backfire.

## Slide 57

# CVE-2018-4331

## Slide 58

$ com.apple.GSSCred

## Slide 59

# reverse-dns identifiers

## com.apple.GSSCred

Top-level domain
.com

Company / Owner
apple.

Specific process
GSSCred

Organizational hierarchy

Reverse-DNS naming style

## Slide 60

# serialization failure

## XPC connection omission

### intended (serial execution)

XPC connection

serial dispatch queue (event handling)
event A   event B   event C

message handler (sequential)

### actual (concurrent execution - the omission)

XPC connection

missing target queue setting

default concurrent queue
event A   event B   event C

message handler (concurrent)
message handler (concurrent)
message handler (concurrent)

violated serialization assumptions

Brandon Azad - https://bazad.github.io/

## Slide 61

# That brings us to _today_

## Slide 62

# auditing

## privileged XPC services

- **Concurrency risks:** unmanaged XPC paths, omitted queues, and cross-queue blocking
- **State vulnerabilities:** unsynchronized mutable state across handlers
- **Behavioral anomalies:** XPC messaging bursts
- **Yikes indicators:** crashes, daemon restarts, or anomalous “x” (e.g.,) GSSCred activity

## Slide 63

$ sandboxing

## Slide 64

Developer   Get Started   Platforms   Technologies   Community   Documentation   Downloads   Support

Documentation                    Language: Objective-C

< All Technologies

XPC

Essentials
- XPC updates

Interprocess communication
- Creating XPC services
- xpc_listener_t
- xpc_session_t

Tasks
- XPC activities

Events
- XPC events

Additional types
- XPC objects
- launchd
- Utilities
- XPC connections

Reference
- Macros

Protocols
- OS_xpc_peer_requirement

Filter

Framework

# XPC

Access a low-level interprocess communication mechanism.

iOS 17.4+ | iPadOS 17.4+ | Mac Catalyst 13.0+ | macOS 10.10+

## Overview

XPC provides a lightweight mechanism for basic interprocess communication. It allows you to create lightweight helper tools, called _XPC services_, that perform work on behalf of your app. The `launchd` system daemon manages these services, launching them on demand, shutting them down when idle, and restarting them if they crash. Benefits of XPC services include:

- Centralize work from multiple processes or mediate access to a shared resource.
- Delegate work so it continues beyond a client’s life cycle.
- Privilege isolation to narrow the scope of access for different functionality.

Clients that make use of these services rely on peer-to-peer XPC connections to communicate across process boundaries. There are two sides to each connection. One side, the _listener_ or server, responds to incoming connection requests and performs tasks. The other side, the client, initiates connections to an XPC service by creating a _session_ with a listener. Once a client establishes a connection to the listener, it sends messages and receives replies from the service.

The type of XPC service you build depends on the requirements of the work it performs. The following table summarizes the types of services available and some differences in how they behave:

Service    Process Environment

Apple - https://support.apple.com/en-us/103457
Apple - https://developer.apple.com/documentation/xpc
Max Keasley - https://labs.withsecure.com/publications/exploiting-the-aws-client-vpn-on-macos-for-local-privilege-escal

## Slide 65

$ brew uninstall threats

## Slide 66

# detection patterns

## static code review signals

## Slide 67

# detection patterns

## static code review signals

- **XPC connection queueing**: Ensure `xpc_connection_set_target_queue()` is always called for accepted connections
- **Serial vs concurrent patterns**: Detect improper assumptions about serial executionc in concurrent environments
- **Synchronous calls**: Flag `dispatch_sync` use and require justification in code review
- **Shared mutable state without synchronization**: Identify globals accessed without locks or serial queue funnels

## Slide 68

$ ./telemetry-signals

## Slide 69

Crash patterns

Thread churn spikes

Queue backlogs

## Slide 70

This slide carries no title or text of its own.

## Slide 71

Crash patterns

Thread churn spikes

Queue backlogs

## Slide 72

This slide carries no title or text of its own.

## Slide 73

Crash patterns

Thread churn spikes

Queue backlogs

## Slide 74

This slide carries no title or text of its own.

## Slide 75

$ cd /behavior

## Slide 76

Concept labels arranged around a flag icon: Elevated Synchronization · Behavior · Expected Parallelism · Rate Limiting · Drain Time · Baseline

## Slide 77

Static Review

Telemetry

Behavioral Detections

## Slide 78

Static Review

Telemetry

Behavioral Detections

## Slide 79

Static Review

Telemetry

Behavioral Detections

## Slide 80

$ ./conclusion.sh

## Slide 81

# Conclusion

- How GCD works and common concurrency hazards
- Priority inversion and deadlock pitfalls with synchronous queue usage
- The exploit against com.apple.GSSCred showing how a queue misconfiguration can lead to code execution in privileged services
- Detection strategies: code review patterns, telemetry signals, and architectural patterns

## Slide 82

$ touch future.txt

## Slide 83

👩‍💻 Subscribe to [ret]2read: An OS Internals Newsletter!

Interested in macOS internals, reverse engineering, or open-source tools for exploring obscure systems?

Starting in September 2025, I’ll be publishing a *monthly* newsletter on Apple security research, sharing what I’m reading, and how I’m applying it to my work.

If that sounds cool, consider subscribing. 🍏⛵✨

✓ Subscribed

https://oliviagallucci.com/newsletter/

## Slide 84

$ echo "thanks"

👩‍💻 Subscribe to [ret]2read: An OS Internals Newsletter!

Interested in macOS internals, reverse engineering, or open-source tools for exploring obscure systems?

Starting in September 2025, I’ll be publishing a *monthly* newsletter on Apple security research, sharing what I’m reading, and how I’m applying it to my work.

If that sounds cool, consider subscribing. 🍏⛵✨

✓ Subscribed

https://oliviagallucci.com/newsletter/

## Slide 85

$ echo "questions?"

👩‍💻 Subscribe to [ret]2read: An OS Internals Newsletter!

Interested in macOS internals, reverse engineering, or open-source tools for exploring obscure systems?

Starting in September 2025, I’ll be publishing a *monthly* newsletter on Apple security research, sharing what I’m reading, and how I’m applying it to my work.

If that sounds cool, consider subscribing. 🍏⛵✨

✓ Subscribed

https://oliviagallucci.com/newsletter/

## Slide 86

$ shutdown

👩‍💻 Subscribe to [ret]2read: An OS Internals Newsletter!

Interested in macOS internals, reverse engineering, or open-source tools for exploring obscure systems?

Starting in September 2025, I’ll be publishing a *monthly* newsletter on Apple security research, sharing what I’m reading, and how I’m applying it to my work.

If that sounds cool, consider subscribing. 🍏⛵✨

✓ Subscribed

https://oliviagallucci.com/newsletter/

