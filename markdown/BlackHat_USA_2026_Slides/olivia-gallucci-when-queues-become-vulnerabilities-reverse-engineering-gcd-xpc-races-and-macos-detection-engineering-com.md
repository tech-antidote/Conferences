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

Olivia Gallucci @ Datadog                                                                                                           prev. Apple,  SECUINFRA GmbH,  U.S. Govt. Black Hat                                                                                                                                                          Aug 2026

Olivia Gallucci - Draft - Approved-Use Only

## Slide 2

$ whatis vocabulary

Olivia Gallucci - Draft - Approved-Use Only

## Slide 3

Jonathan Levin Olivia Gallucci - Draft - Approved-Use Only


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Processes are runnable entities.
Jonathan Levin Olivia Gallucci - Draft - Approved-Use Only
```

## Slide 4

# Processes are _not_ runnable entities.

Olivia Gallucci - Draft - Approved-Use Only

Jonathan Levin

## Slide 5

The process itself is technically only a container for one or more threads, and provides the virtual memory image, the descriptors and ports shared by all the threads. Thus, when one refers to a process as “executing,” the correct terminology is “at least one of the threads of the process pid is executing.”

Olivia Gallucci - Draft - Approved-Use Only

Jonathan Levin

## Slide 6

##### **Concurrent** : 2 queues, 1 vending machine

iCode - https://www.youtube.com/watch?v=X9H2M7xMi9E

Olivia Gallucci - Draft - Approved-Use Only

## Slide 7

**Concurrent** : 2 queues, 1 vending machine

Interleavings

Time ↓

\```
T1:  A: read x
B: x = x +1
C: write x
T2:      D: read x
E: x = x +1
F: write x
\```

\```
One Possible Interleaving
T1:  A     B     C
T2:     D     E     F
\```

iCode - https://www.youtube.com/watch?v=X9H2M7xMi9E

Olivia Gallucci - Draft - Approved-Use Only

## Slide 8

**Concurrent** : 2 queues, 1 vending machine

**Parallel** : 2 queues, 2 vending machines

Interleavings

Time ↓

\```
T1:  A: read x
B: x = x +1
C: write x
\```

\```
T2:      D: read x
E: x = x +1
F: write x
\```

\```
One Possible Interleaving
T1:  A     B     C
T2:     D     E     F
\```

iCode - https://www.youtube.com/watch?v=X9H2M7xMi9E

Olivia Gallucci - Draft - Approved-Use Only

## Slide 9

### Concurrency

Parallelism

Olivia Gallucci - Draft - Approved-Use Only

## Slide 10

$ ssh gcd@apple.com

Olivia Gallucci - Draft - Approved-Use Only

## Slide 11

Olivia Gallucci - Draft - Approved-Use Only

iCode - https://www.youtube.com/watch?v=X9H2M7xMi9E tclementdev - https://tclementdev.com/posts/what_went_wrong_with_the_libdispatch.html

## Slide 12

Thread Task Task Task
Dispatch Queue Thread
Task Task Task
Thread

Olivia Gallucci - Draft - Approved-Use Only

Vlog

## Slide 13

Vlog Olivia Gallucci - Draft - Approved-Use Only


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Developer Get Started Platforms Technologies Community Documentation Support Q
{1 Documentation Language: Swift v
< All Technologies
Dispatch Framework
>] DispatchQueue
©) DispatchWorkitem
>) DispatchGroup
Dispatch Queue
= Dispatch Work Item
Dispatch Group
Workloop
3) DispatchQoS
>) DispatchSource
Dispatch Source
>} DispatchlO
DispatchData
DispatchDatalterator
Dispatch I/O
Dispatch Data
DispatchSourceProtocol
Filter
Dispatch
Execute code concurrently on multicore hardware by submitting work to dispatch queues
managed by the system.
iOS 8.04+ | iPadOS 8.0+ | Mac Catalyst 13.0+ | macOS 10.10+ | tvOS 9.0+ | visionOS 1.0+ | watchOS 2.0+
Overview
Dispatch, also known as Grand Central Dispatch (GCD), contains language features, runtime libraries, and
system enhancements that provide systemic, comprehensive improvements to the support for concurrent code
execution on multicore hardware in macO$S, iOS, watchOS, and tvOS.
The BSD subsystem, Core Foundation, and Cocoa APIs have all been extended to use these enhancements to
help both the system and your application to run faster, more efficiently, and with improved responsiveness.
Consider how difficult it is for a single application to use multiple cores effectively, let alone to do it on different
computers with different numbers of computing cores or in an environment with multiple applications
competing for those cores. GCD, operating at the system level, can better accommodate the needs of all
running applications, matching them to the available system resources in a balanced fashion.
Dispatch Objects and ARC
When you build your app using the Objective-C compiler, all dispatch objects are Objective-C objects. As such,
when automatic reference counting (ARC) is enabled, dispatch objects are retained and released automatically,
just like any other Objective-C object. When ARC is not enabled, use the dispatch retain and dispatch
release functions (or Objective-C semantics) to retain and release your dispatch objects. You cannot use the
Core Foundation retain and release functions.
Gallucci - Draft - Approved-Use Only
```

## Slide 14

Quality of Service (QoS)

User
BackgroundUtility
InteractiveInitiated

iCode- https://www.youtube.com/watch?v=yH0RBTdNi3U

Olivia Gallucci - Draft - Approved-Use Only

## Slide 15

Unspecified Default

User  User
Interactive Initiated

Utility

Background

iCode- https://www.youtube.com/watch?v=yH0RBTdNi3U

Olivia Gallucci - Draft - Approved-Use Only

## Slide 16

Quality of Service (QoS)

##### Unspecified

Default

• **User Interactive** : Animations or tasks that update the UI immediately. • **User Initiated** : Tasks required for a seamless user experience, such as loading data for a scrolling table view. User User • **Utility** : Long-running tasks where user is aware of progress (e.g., downloads). Interactive Initiated • **Background** : Tasks user is unaware of, such as backups or server restoration. • **Default & Unspecified** : Default falls between User Initiated and Utility. Unspecified indicates missing QoS information and has the lowest priority.

Utility Background

Apple - https://developer.apple.com/documentation/dispatch/dispatchqos Apple - https://developer.apple.com/documentation/foundation/qualityofservice Apple - https://developer.apple.com/documentation/dispatch/dispatch_queue_attr_make_with_qos_class Dr. Howard Oakley - https://eclecticlight.co/2021/05/17/how-m1-macs-feel-faster-than-intel-models-its-about-qos/

Olivia Gallucci - Draft - Approved-Use Only

## Slide 17

Public APIs

###### • Swift/ObjC (Foundation)

• `QualityOfService` ( `userInteractive` , `userInitiated` , `utility` , `background` , plus `default` ).

- Swift (Dispatch)

• `DispatchQoS` / `DispatchQoS.QoSClass` with the same classes • System prioritizes higher QoS work when scheduling

• C (libdispatch)

• queue attributes and global queues take `QOS_CLASS_` * constants (e.g., `QOS_CLASS_USER_INTERACTIVE` , `..._USER_INITIATED` , `..._UTILITY` , . `.._BACKGROUND` )

Olivia Gallucci - Draft - Approved-Use Only

## Slide 18

Quality of Service (QoS)

##### Unspecified

Default

• **User Interactive** : Animations or tasks that update the UI immediately. • **User Initiated** : Tasks required for a seamless user experience, such as loading data for a scrolling table view. User User • **Utility** : Long-running tasks where user is aware of progress (e.g., downloads). Interactive Initiated • **Background** : Tasks user is unaware of, such as backups or server restoration. • **Default & Unspecified** : Default falls between User Initiated and Utility. Unspecified indicates missing QoS information and has the lowest priority.

Utility Background

Apple - https://developer.apple.com/documentation/dispatch/dispatchqos Apple - https://developer.apple.com/documentation/foundation/qualityofservice Apple - https://developer.apple.com/documentation/dispatch/dispatch_queue_attr_make_with_qos_class Dr. Howard Oakley - https://eclecticlight.co/2021/05/17/how-m1-macs-feel-faster-than-intel-models-its-about-qos/

Olivia Gallucci - Draft - Approved-Use Only

## Slide 19

Olivia Gallucci - Draft - Approved-Use Only

Hackers on the Rocks - https://www.youtube.com/watch?v=9sqoR2qGp0w Olivia Gallucci - https://oliviagallucci.com/how-to-manipulate-the-execution-flow-of-toctou-attacks/

## Slide 20

##### gotta do the self promo

How to manipulate the execution flow of TOCTOU attacks ([ret]2read)

Hackers on the Rocks - https://www.youtube.com/watch?v=9sqoR2qGp0w Olivia Gallucci - https://oliviagallucci.com/how-to-manipulate-the-execution-flow-of-toctou-attacks/

Olivia Gallucci - Draft - Approved-Use Only

## Slide 21

Hackers on the Rocks - https://www.youtube.com/watch?v=9sqoR2qGp0w Olivia Gallucci - https://oliviagallucci.com/how-to-manipulate-the-execution-flow-of-toctou-attacks/

Olivia Gallucci - Draft - Approved-Use Only

## Slide 22

$ cd /vulnerabilities

Olivia Gallucci - Draft - Approved-Use Only

## Slide 23

Priority Inversion and QoS Mismatches

3-Thread Swimlane: L holds lock, H blocks, M runs

high priority

low priority

https://news.ycombinator.com/item?id=41724168

Olivia Gallucci - Draft - Approved-Use Only

## Slide 24

Priority Inversion and QoS Mismatches

### 3-Thread Swimlane: L holds lock, H blocks, M runs

high priority

medium priority

Olivia Gallucci - Draft - Approved-Use Only low priority

https://news.ycombinator.com/item?id=41724168

## Slide 25

Priority Inversion and QoS Mismatches

3-Thread Swimlane: L holds lock, H blocks, M runs

low priority

high priority

https://news.ycombinator.com/item?id=41724168

Olivia Gallucci - Draft - Approved-Use Only

## Slide 26

Priority Inversion and QoS Mismatches

3-Thread Swimlane: L holds lock, H blocks, M runs Assume priorities: H > M > L. Shared resource protected by mutex R. `Time ↓ L (low): lock(R) [critical section...............] unlock(R) H (high): tries lock(R) -> BLOCKED ....................... runs M (med): runs.................. runs.......... (preempts L)`

- L acquires R.

- H becomes runnable, needs R, blocks on L.

• While H is blocked, M runs (preempts L), so L can’t finish and release R. • Result: H is indirectly delayed by M (lower priority than H), which is the inversion.

https://news.ycombinator.com/item?id=41724168

Olivia Gallucci - Draft - Approved-Use Only

## Slide 27

# Does Apple implement priority inheritance anywhere?

Next few slides are a simplification, but gets the point across

Olivia Gallucci - Draft - Approved-Use Only

## Slide 28

mutex vs unfair

## unfair vs spinlock spinlock vs semaphores

Olivia Gallucci - Draft - Approved-Use Only

## Slide 29

##### `pthread_mutex_t` (blocks/sleeps, scheduler can help)

\```
static pthread_mutex_t gMutex = PTHREAD_MUTEX_INITIALIZER;
pthread_mutex_lock(&gMutex);   // contended: thread can sleep
// critical section
pthread_mutex_unlock(&gMutex);
\```

##### `os_unfair_lock` (Darwin replacement for spin)

\```
static os_unfair_lock gLock = OS_UNFAIR_LOCK_INIT;
os_unfair_lock_lock(&gLock);   // contended: waiter parks
// critical section
os_unfair_lock_unlock(&gLock);
\```

<u>https://blog.xoria.org/macos-tips-threading/ https://developer.apple.com/documentation/os/os_unfair_lock https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/pthread_mutex_init.3.html</u>

Olivia Gallucci - Draft - Approved-Use Only

## Slide 30

## mutex vs unfair unfair vs spinlock spinlock vs semaphores

Olivia Gallucci - Draft - Approved-Use Only

## Slide 31

##### `pthread_mutex_t` (blocks/sleeps, scheduler can help)

\```
static pthread_mutex_t gMutex = PTHREAD_MUTEX_INITIALIZER;
pthread_mutex_lock(&gMutex);   // contended: thread can sleep
// critical section
pthread_mutex_unlock(&gMutex);
\```

##### `os_unfair_lock` (Darwin replacement for spin)

\```
static os_unfair_lock gLock = OS_UNFAIR_LOCK_INIT;
os_unfair_lock_lock(&gLock);   // contended: waiter parks
// critical section
os_unfair_lock_unlock(&gLock);
\```

<u>https://blog.xoria.org/macos-tips-threading/ https://developer.apple.com/documentation/os/os_unfair_lock https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/pthread_mutex_init.3.html</u>

Olivia Gallucci - Draft - Approved-Use Only

## Slide 32

##### `os_unfair_lock` (Darwin replacement for spin)

`static os_unfair_lock gLock = OS_UNFAIR_LOCK_INIT; os_unfair_lock_lock(&gLock);   // contended: waiter parks // critical section os_unfair_lock_unlock(&gLock);` Plain spinlock (bad under mixed QoS) `static atomic_flag gSpin = ATOMIC_FLAG_INIT; while (atomic_flag_test_and_set_explicit(&gSpin, memory_order_acquire)) { /* spins: keeps running, burns CPU */ } // critical section atomic_flag_clear_explicit(&gSpin, memory_order_release);`

Luna Razzaghipour - https://blog.xoria.org/macos-tips-threading/ <u>https://developer.apple.com/documentation/os/os_unfair_lock https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/pthread_mutex_init.3.html</u>

Olivia Gallucci - Draft - Approved-Use Only

## Slide 33

## mutex vs unfair unfair vs spinlock spinlock vs semaphores

Olivia Gallucci - Draft - Approved-Use Only

## Slide 34

## mutex vs unfair unfair vs spinlock

spinlock vs semaphores

Olivia Gallucci - Draft - Approved-Use Only

## Slide 35

With QoS inheritance ( pthread_mutex  /  os_unfair_lock

Lock tracks ownership; kernel can temporarily boost the owner to resolve inversion

\```
time →
High QoS (Q=UI) :  lock() ── BLOCKED ─────────────────────── RUN (after unlock)
Low  QoS (Q=BG) :  RUN ── holds lock ──(BOOST to UI)─ RUN ── unlock()
CPU scheduling  :         runs boosted BG owner so it can release sooner
\```

\```
typedef NSObject<OS_dispatch_semaphore> * dispatch_semaphore_t;
\```

* “With QoS inheritance (pthread_mutex / os_unfair_lock)” is really “with **potential** QoS inheritance.” Apple’s wording is deliberately hedged (“may use to attempt”).

Olivia Gallucci - Draft - Approved-Use Only

## Slide 36

With QoS inheritance ( pthread_mutex  /  os_unfair_lock

Lock tracks ownership; kernel can temporarily boost the owner to resolve inversion `time → High QoS (Q=UI) :  lock() ── BLOCKED ─────────────────────── RUN (after unlock) Low  QoS (Q=BG) :  RUN ── holds lock ──(BOOST to UI)─ RUN ── unlock() CPU scheduling  :         runs boosted BG owner so it can release sooner`

Without QoS inheritance (semaphore / rwlock / custom)

Waiter can’t donate QoS/priority to the owner, so the high-QoS thread stalls `time → High QoS (Q=UI) :   wait() ── BLOCKED ─────────────────────────────────── Low  QoS (Q=BG) :   READY ───────────(not boosted)────────── RUN ── signal() CPU scheduling  :   keeps running other work; BG owner may not run promptly`

* “With QoS inheritance (pthread_mutex / os_unfair_lock)” is really “with **potential** QoS inheritance.” Apple’s wording is deliberately hedged (“may use to attempt”).

Olivia Gallucci - Draft - Approved-Use Only

## Slide 37

## mutex vs unfair unfair vs spinlock

spinlock vs semaphores

Olivia Gallucci - Draft - Approved-Use Only

## Slide 38

./detection

Olivia Gallucci - Draft - Approved-Use Only

## Slide 39

Olivia Gallucci - Draft - Approved-Use Only

## Slide 40

# Edit Scheme… > Run > Diagnostics > Runtime API Checking and check “Thread Performance Checker”

GRDB - https://github.com/groue/GRDB.swift/issues/1234

Olivia Gallucci - Draft - Approved-Use Only

## Slide 41

Thread running at `QOS_CLASS_USER_INTERACTIVE` waiting on a lower QoS thread running at `QOS_CLASS_DEFAULT` . Investigate ways to avoid priority inversions.

GRDB - https://github.com/groue/GRDB.swift/issues/1234

Olivia Gallucci - Draft - Approved-Use Only

## Slide 42

Thread running at `QOS_CLASS_USER_INTERACTIVE` waiting on a lower QoS thread running at `QOS_CLASS_DEFAULT` . Investigate ways to avoid priority inversions.

GRDB - https://github.com/groue/GRDB.swift/issues/1234 Luna Razzaghipour - https://blog.xoria.org/macos-tips-threading/

Olivia Gallucci - Draft - Approved-Use Only

## Slide 43

./dispatch-sync-deadlocks

Olivia Gallucci - Draft - Approved-Use Only

## Slide 44

dispatch_sync

## circular wait scanning

Olivia Gallucci - Draft - Approved-Use Only

## Slide 45

understanding  dispatch_sync  & deadlocks

##### synchronous execution (normal case)

##### deadlock scenario (problem case)

⏱

Caller Queue
Target Queue
(Main Thread)
(Background Thread)
dispatch_sync
Task
Caller blocks &
Block
waits
Task Complete,
Unblock Caller

Caller Queue (Main Thread)

dispatch_sync
Task
Queue is
CANNOT
🔒
BLOCKED
start
by the call

Zeeshan Khan - https://izeeshan.wordpress.com/tag/multithreading/ Apple - https://developer.apple.com/documentation/dispatch/dispatchqueue/sync

Olivia Gallucci - Draft - Approved-Use Only

## Slide 46

## dispatch_sync circular wait scanning

Main Dispatch Queue

Olivia Gallucci - Draft - Approved-Use Only

## Slide 47

understanding  dispatch_sync  deadlocks

### the main queue pitfall

safe: targeting a _different_ queue (e.g., background)

deadlock: targeting the _main_ queue from the main thread

Main Queue (Serial)

Background Queue (Concurrent)

dispatch_sync
Task
Block
Task Complete,
Unblock Main

\```
dispatch_sync(dispatch_get_main_queue(), ...)
\```

Task
Block
🔒

Main Queue (Serial)

Olivia Gallucci - Draft - Approved-Use Only

## Slide 48

circular wait

##### deadlock (circular wait)

##### setup & trigger

main thread  system API /
main thread  dispatch_sync()
(serial queue) global queue
(serial queue)
3. main thread makes synchronous call, waiting for a
1. main thread queues tasks
    worker thread
    to background threads
main thread
waits for 🔒 waits for
deadlock
…
background
background worker threads
worker threads
(concurrent queue)
dispatch_sync(main_queu e) dispatch_sync(main_queu e) dispatch_sync(main_queu e)

###### 2. background threads block, waiting for main thread

4. circular wait: main thread waits for workers, workers wait for main thread. app freezes.

https://blog.stevex.net/2012/09/avoid-dispatch_sync/

Olivia Gallucci - Draft - Approved-Use Only

## Slide 49

## dispatch_sync circular wait

scanning

Olivia Gallucci - Draft - Approved-Use Only

## Slide 50

deadlock scenario

### `dispatch_sync` on serial queue

callback execution
service handler  no
dispatch_sync
continue
(serial listener queue) call? (different queue)
execution
yes , targeting
same queue
deadlock
(waiting for self)
!
guaranteed to deadlock service

Olivia Gallucci - Draft - Approved-Use Only

## Slide 51

$ brew uninstall resource-starvation

Olivia Gallucci - Draft - Approved-Use Only

## Slide 52

Resource Starvation & GCD

### thread pool saturation

Task Task
Task Task
Task Task
DISPATCH_ASYNC
(huge volume / blocking)
worker thread pool
saturated
concurrent queue tasks

##### • misusing GCD can lead to resource starvation • GCD uses a thread pool for concurrent tasks • saturating the pool staves other tasks of CPU/threads

Olivia Gallucci - Draft - Approved-Use Only

## Slide 53

Olivia Gallucci - Draft - Approved-Use Only

iCode - https://www.youtube.com/watch?v=X9H2M7xMi9E tclementdev - https://tclementdev.com/posts/what_went_wrong_with_the_libdispatch.html

## Slide 54

dispatch queue  thread pool starving task / component
worker thread
worker thread worker thread
many tasks queued  all threads busy (blocking) starved of resources
Task
Task
Task
Task
Task
Task

Olivia Gallucci - Draft - Approved-Use Only

Y Combinator -  ıhttps://news.ycombinator.com/item?id=41724168

## Slide 55

Olivia Gallucci - Draft - Approved-Use Only

## Slide 56

historical context

##### abandoned API (macOS 10.7)

🧵🧵🧵🧵🧵🧵
Task
🧵🧵🧵🧵🧵🧵
security transforms:
new queue/thread per task
caused severe thread proliferation
rewrite (iOS 12)
Task 1
Task 2
🧵
Task 3 single-threaded
daemons
improved performance, unconstrained
concurrency can backfire.

Olivia Gallucci - Draft - Approved-Use Only

## Slide 57

# CVE-2018-4331

Olivia Gallucci - Draft - Approved-Use Only

## Slide 58

$ com.apple.GSSCred

Olivia Gallucci - Draft - Approved-Use Only

## Slide 59

reverse-dns identifiers

### com.apple.GSSCred

Top-level domain
.com
Company / Owner
apple.
Specific process
GSSCred
Organizational hierarchy
Reverse-DNS naming style

Olivia Gallucci - Draft - Approved-Use Only

## Slide 60

serialization failure

### XPC connection omission

##### intended (serial execution)

serial dispatch queue
XPC  (event handling) message handler
connection (sequential)
event A event B event C
message handler
actual (concurrent execution - the omission)
(concurrent)
default concurrent queue
XPC  message handler
connection (concurrent)
event A event B event C
message handler
missing target
queue setting (concurrent)
violated serialization assumptions

Brandon Azad - https://bazad.github.io/

Olivia Gallucci - Draft - Approved-Use Only

## Slide 61

# That brings us to _today_

Olivia Gallucci - Draft - Approved-Use Only

## Slide 62

auditing

privileged XPC services • Concurrency risks: unmanaged XPC paths, omitted queues, and cross-queue blocking

- State vulnerabilities: unsynchronized mutable state across handlers • Behavioral anomalies: XPC messaging bursts

• Yikes indicators: crashes, daemon restarts, or anomalous “x” (e.g.,) GSSCred activity

Olivia Gallucci - Draft - Approved-Use Only

## Slide 63

$ sandboxing

Olivia Gallucci - Draft - Approved-Use Only

## Slide 64

Olivia Gallucci - Draft - Approved-Use Only

Apple - https://support.apple.com/en-us/103457 Apple - https://developer.apple.com/documentation/xpc Max Keasley - https://labs.withsecure.com/publications/exploiting-the-aws-client-vpn-on-macos-for-local-privilege-escal

## Slide 65

$ brew uninstall threats

Olivia Gallucci - Draft - Approved-Use Only

## Slide 66

detection patterns

### static code review signals

Olivia Gallucci - Draft - Approved-Use Only

## Slide 67

detection patterns

### static code review signals

• XPC connection queueing: Ensure `xpc_connection_set_target_queue()` is always called for accepted connections

• Serial vs concurrent patterns: Detect improper assumptions about serial executionc in concurrent environments

• Synchronous calls: Flag `dispatch_sync` use and require justification in code review

• Shared mutable state without synchronization: Identify globals accessed without locks or serial queue funnels

Olivia Gallucci - Draft - Approved-Use Only

## Slide 68

$ ./telemetry-signals

Olivia Gallucci - Draft - Approved-Use Only

## Slide 69

Crash patterns

## Thread churn spikes Queue backlogs

Olivia Gallucci - Draft - Approved-Use Only

## Slide 70

Olivia Gallucci - Draft - Approved-Use Only

## Slide 71

## Crash patterns Thread churn spikes Queue backlogs

Olivia Gallucci - Draft - Approved-Use Only

## Slide 72

Olivia Gallucci - Draft - Approved-Use Only

## Slide 73

## Crash patterns Thread churn spikes

Queue backlogs

Olivia Gallucci - Draft - Approved-Use Only

## Slide 74

Olivia Gallucci - Draft - Approved-Use Only

## Slide 75

$ cd /behavior

Olivia Gallucci - Draft - Approved-Use Only

## Slide 76

##### Elevated Synchronization

##### Behavior

Rate Limiting

##### Expected Parallelism

Baseline

##### Drain Time

Olivia Gallucci - Draft - Approved-Use Only

## Slide 77

Static Review

## Telemetry Behavioral Detections

Olivia Gallucci - Draft - Approved-Use Only

## Slide 78

## Static Review Telemetry Behavioral Detections

Olivia Gallucci - Draft - Approved-Use Only

## Slide 79

## Static Review Telemetry

Behavioral Detections

Olivia Gallucci - Draft - Approved-Use Only

## Slide 80

$ ./conclusion.sh

Olivia Gallucci - Draft - Approved-Use Only

## Slide 81

Conclusion

• How GCD works and common concurrency hazards • Priority inversion and deadlock pitfalls with synchronous queue usage • The exploit against com.apple.GSSCred showing how a queue misconfiguration can lead to code execution in privileged services • Detection strategies: code review patterns, telemetry signals, and architectural patterns

Olivia Gallucci - Draft - Approved-Use Only

## Slide 82

$ touch future.txt

Olivia Gallucci - Draft - Approved-Use Only

## Slide 83

#### https://oliviagallucci.com/newsletter/

Olivia Gallucci - Draft - Approved-Use Only


> Recovered by OCR — confidence 91/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
® Subscribe to [ret]2read:
Interested in mac i als, re : i ring, or
open-source tools for exploring obscw
newsletter on Apple security research, sh g what I'm
reading, and how I'm appl it to my work
If that sounds cool, consider subscribing. @&
```

## Slide 84

$ echo
   "thanks"

#### https://oliviagallucci.com/newsletter/

Olivia Gallucci - Draft - Approved-Use Only


> Recovered by OCR — confidence 89/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Interested in macOS internals. reverse enginecring, or
h open-source tools for exploring obscure systems?
(= C @) Starting in September 2025, I'll be publishing a monthly
newsletter on Apple security research, sharing what I'm
| | Jj I reading, and how I'm applying it to my work.
f a Nn Ss It that sounds cool, consider subscribing. @4
```

## Slide 85

$ echo
   "questions?"

#### https://oliviagallucci.com/newsletter/

Olivia Gallucci - Draft - Approved-Use Only


> Recovered by OCR — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
$ echo
"questions?"
Interested in macOS internals, reverse cnginecring, or
open-source tools for exploring obscure systems?
newsletter on Apple securi earch, sharing what I'm
reading, and how I'm applying it to my work.
If that sounds cool, consider subscribing.
```

## Slide 86

$ shutdown

#### https://oliviagallucci.com/newsletter/

Olivia Gallucci - Draft - Approved-Use Only


> Recovered by OCR — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
$ shutdown
Interested in macOS internals, reverse cnginecring, or
open-source tools for exploring obscure systems?
newsletter on Apple security re:
reading, and how I'm applying it to my work.
If that sounds cool, consider subscribing.
```
