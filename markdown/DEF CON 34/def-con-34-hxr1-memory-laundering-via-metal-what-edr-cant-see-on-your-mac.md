---
title: "Memory Laundering via Metal What EDR Can't See on Your Mac"
speakers: ["Hxr1"]
conference: "DEF CON"
conference_full: "DEF CON 34"
edition: "34"
year: null
source_pdf: "DEF CON 34/DEF CON 34 - Hxr1 - Memory Laundering via Metal What EDR Can't See on Your Mac.pdf"
pages: 17
sha256: "0c06461fef408271fab51d820caced657623b13c9ab637c43f6453fde55e5a3f"
text_chars: 8164
ocr_pages: 0
has_ocr: false
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2"
converted_at: "2026-08-12T00:21:53Z"
---
# Memory Laundering via Metal What EDR Can't See on Your Mac

**Speakers:** Hxr1  
**Conference:** DEF CON 34  
**Source:** `DEF CON 34/DEF CON 34 - Hxr1 - Memory Laundering via Metal What EDR Can't See on Your Mac.pdf` (17 pages)


## Slide 1

# **`DEF CON 34` Memory Laundering via Metal**

What EDR can't see on your Mac

**Hxr1**

```
https://hxr1.ghost.io
```

## Slide 2

```
THE GAP
```

Your Mac has gigabytes of memory **that no security product can scan.**

Not because the tools are bad.

**Because the memory isn't in CPU address space at all.**

## Slide 3

```
AGENDA
```

**Where we're going** Three acts. Keep this map in your head; I'll call out each turn.

```
01
```

**The gap**

Memory your Mac's security can't scan, and the Metal mode behind it.

```
02
```

**The technique**

The GPU trampoline, plus two live demos: hide data, then run code.

**`03` The fix**

What defenders can try, and the platform change only Apple can ship.

## Slide 4

```
THE STAKES
```

**First: what is EDR watching for?** The security agent on every managed Mac earns its keep by inspecting live memory.

```
WHAT IT IS
```

```
WHY IT READS RAM
```

**EDR** = Endpoint Detection & Response: the security agent running on your machine.

```
CrowdStrikeSentinelOneJamf Protect
```

Malware that never touches disk still has to live in memory. Secrets, keys and tokens sit in a process while it runs. So EDR scans process memory for known patterns.

Its job: catch malware and stolen secrets on a **running** host.

The whole talk is one question: what if those bytes never enter memory the EDR can read?

## Slide 5

```
THE THREAT MODEL
```

## **How macOS EDR scans memory**

Every CPU-memory scanner on the platform reduces to the same three Mach calls.

```
CrowdStrike FalconSentinelOneJamf Protectany Endpoint Security client
```

`task_for_pid()` port to the target `// Every macOS EDR memory scanner: task_for_pid(mach_task_self(), pid, &task); mach_vm_region()` walk the `while (mach_vm_region(task, &addr, &size,...)) {` address space `mach_vm_read(task, addr, size, buf, &n); yara_scan(buf, n); } mach_vm_read()` pull bytes, match

**The assumption:** all three read only the CPU address space. True on Intel. **False on Apple Silicon** , where the GPU shares RAM but keeps its own page tables.

## Slide 6

```
GPU 101
```

## **What is Metal?**

Apple's low-level GPU framework, and the only way anything on a Mac talks to the graphics chip.

```
THE FRAMEWORK
```

```
WHAT'S A SHADER
```

A thin layer between your code and the GPU. It replaced OpenGL on macOS in 2014 and is now the **only** GPU API Apple ships.

A small program that runs **on the GPU** , not the CPU. Compiled into a pipeline, then run massively in parallel.

Runs the window server & compositing Video decode, Core Image, Core ML Every game and Final Cut Pro

`Graphics` · vertex + fragment shaders draw pixels `Compute` · kernels crunch general math (ML, imaging)

```
THE OBJECTS WE'LL USE
```

`MTLDevice MTLBuffer MTLCommandQueue MTLBlitCommandEncoder` the GPU handle GPU-accessible memory work you submit a GPU-side copy

The GPU has its own memory. The whole technique hides in one `MTLBuffer` storage mode.

## Slide 7

```
APPLE SILICON
```

**Same RAM, two sets of page tables** The GPU shares one physical memory pool with the CPU but maps it through its own MMU.

`CPU · MACH VM GPU · AGX FIRMWARE PAGE TABLES` Maps malloc, mmap, dylibs, and Shared / Managed buffers. Maps StorageModePrivate buffers, allocated via IOGPUDevice. `mach_vm_region` walks only this. No CPU entry exists to return. `UNIFIED PHYSICAL RAM` one pool, shared by CPU and GPU

The bytes are real and sitting in RAM, but no CPU virtual address points at the private pages, so every CPU memory primitive returns nothing.

## Slide 8

```
METAL · MTLBUFFER
```

## **One storage mode returns nothing at all**

`StorageModePrivate` puts a buffer's bytes outside CPU address space entirely.

|`MODE`|`CPU READS?`|`BACKING STORE`|
|---|---|---|
|`Shared`|`YES`|`unified memory`|
|`Managed`|`YES`|`mirrored, sync`|
|**`StorageModePrivate`**|**`NO`**|`GPU page tables only`|

```
[privateBuffer contents]
```

```
→ NULL
```

Not restricted. There is **no CPU address to return** , so `mach_vm_region` skips it and ES fires no event.

Metal is the **only** GPU API on macOS since OpenGL was deprecated. It backs everything: window compositing, video decode, Core ML.

## Slide 9

```
THE ATTACK AT A GLANCE
```

## **The attack, end to end**

Six moves: hide a payload in GPU-private memory, wipe every CPU trace, recover it on demand.

##### **`CPU SIDE · SCANNABLE BY EDR`**

##### **`GPU PRIVATE · INVISIBLE TO EDR`**

01 · LOAD 02 · STAGE 03 · BLIT 04 · WIPE 05 · RECOVER 06 · TRAMPOLINE
XOR'd payload lands  Copy the XOR'd bytes  The GPU DMA engine  Erase every CPU  Reverse blit pulls the  Hide then recover on
in CPU RAM from  into a Shared  copies them into a  copy. The data now  bytes back to CPU,  demand, over and
disk. No plaintext ever  MTLBuffer. StorageModePrivate  lives only on the GPU. only when you need  over. The plaintext is
exists in RAM. buffer. them. exposed only for the
instant of use.

**Between WIPE and RECOVER the payload has no CPU address at all, so every memory scanner on the machine returns nothing during that window.**

## Slide 10

```
PRIVILEGE · NONE REQUIRED
```

## **Who can allocate this?**

Anyone. One unprivileged call, hiding in ordinary GPU traffic.

**Any process.** No entitlement. No kext. No root.

App Store apps Sandboxed processes WebKit content processes `newBufferWithLength:options:` the same call Core ML, video decode & every game already make.

#### **You can't block it without breaking the OS.**

## Slide 11

```
WHY IT MATTERS
```

**Not just another evasion trick** Packing and living-off-the-land can still be scanned. This can't.

```
THE CROWDED FIELD
```

```
GPU-PRIVATE IS DIFFERENT
```

- **`1`**<sup>No API to scan it from another process, at all.</sup>

- **`2`**<sup>Unprivileged · even a sandboxed App Store app.</sup>

- **`3`**<sup>Normal traffic · Core ML, video decode, games.</sup>

- **`4`**<sup>An API gap, not a bug · no patch to ship.</sup>

## Slide 12

```
THE LINCHPIN
```

## **Crossing the boundary: the blit** The GPU moves the bytes. The CPU issues the command but never touches them.

✕ `You can't do this`

✓ `The only path: GPU-side DMA`

- A private buffer has no CPU pointer; nothing can

- read or write it.

▸ The GPU's DMA engine performs the copy; the CPU never sees the bytes.

```
blit = [cb blitCommandEncoder ];
[blit
copyFromBuffer :sharedStaging
sourceOffset:
0 toBuffer:privateDest
destinationOffset:
0 size:len];
[blit
endEncoding ];
[cb
commit];  // GPU copies; CPU never sees data
BLIT LATENCYGPU DMA
250–330 ns100s of MB/s
```

## Slide 13

```
DEMO
```

### **Blind-spot proof**

A real EDR-grade scanner, watching the secret vanish and come back.

## Slide 14

```
MACOS 26.5
```

**Timing reality check** The plaintext window is sub-microsecond. No scanner polls near that.

Inbound · materialize to wipe `250–330 ns` A 1 kHz scanner has a **1 ms** window. Recovery · decode to wipe `125–167 ns` **1,000× Total plaintext window** **`< 1 µs`** larger than the exposure it hunts. **Not beatable by “scan faster.”** Encoded staging window (XOR'd) `~1.3 ms` Even a 1 MB payload keeps the inbound window under **10 ms** · still mach_absolute_time · 24 MHz timebase (~41 ns) · reproduced at -O0 and - unreachable by real polling rates. O2.

## Slide 15

```
THE DEFENDER'S MOVE
```

## **Can the defender see it?**

Yes, from outside the process. The trampoline leaves a footprint no real GPU workload has.

- `HOW WE CATCH IT · dyld interposition THE TELL · trampoline vs. real work` The PoC: private buffer, **0 pipelines** **`SUSPICIOUS`**

- • **metal_watch.dylib** - injected with **DYLD_INSERT_LIBRARIES**

- • Swizzles Metal's buffer-allocation calls at load time Real ML app: private + **1 compute** **`AMBIGUOUS`**

- • Logs every buffer: **storage mode, size, caller frame**

- • Runs **outside the target** - needs no cooperation from it The rule: **private memory + zero GPU work** = trampoline shape

**1 of 3 surfaces shipped and working. IOKit telemetry and behavioral analytics are designed, not yet built.**

## Slide 16

```
CLOSING
```

**This isn't a bug. It's how the API is designed to work.**

Defensive tooling assumed a CPU-centric memory model. Apple Silicon broke it, and the fix isn't a patch, it's a rethink.

```
OPTION B · THE RIGHT MOVE
```

Expose a GPU-memory visibility API to entitled defenders.

## Slide 17

**Thank you! Q&A**
