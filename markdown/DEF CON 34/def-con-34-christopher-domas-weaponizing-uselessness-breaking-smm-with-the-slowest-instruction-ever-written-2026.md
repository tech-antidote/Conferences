---
title: "Weaponizing Uselessness Breaking SMM with the Slowest Instruction Ever Written"
speakers: ["Christopher Domas"]
conference: "DEF CON"
conference_full: "DEF CON 34"
edition: "34"
year: null
source_pdf: "DEF CON 34/DEF CON 34 - Christopher Domas - Weaponizing Uselessness Breaking SMM with the Slowest Instruction Ever Written - 2026.pdf"
pages: 68
sha256: "1789a79d85e2e866ad7db26955a39188a8e5a5254990f3afc2b307fd28b63215"
text_chars: 11855
ocr_pages: 1
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T00:14:24Z"
---
# Weaponizing Uselessness Breaking SMM with the Slowest Instruction Ever Written

**Speakers:** Christopher Domas  
**Conference:** DEF CON 34  
**Source:** `DEF CON 34/DEF CON 34 - Christopher Domas - Weaponizing Uselessness Breaking SMM with the Slowest Instruction Ever Written - 2026.pdf` (68 pages)


## Slide 1

```
movl $0xfcc68830, %rsi
fxrstor64 (%rsi)
```

```
The world's worst machine instruction
```

```
Weaponizing Uselessness
domas  ·  @xoreaxeaxeax  ·  DEF CON 2026
```

## Slide 2

```
// ACT I
```

```
Let Sleeping Bugs Lie
```

## Slide 3

⊷ `System Management Mode` ⊷ `Invisible to OS + hypervisor` ⊷ `Ring -2 — below kernel` ⊷ `Write access to firmware` ⊷ `Every x86 system, 40 years`

```
SMM 101
```

## Slide 4

⊷ `SMM — yes, again`

⊷ `Every prior attack: broke an implementation` ⊷ `Bad checks, missing validation — patched, forgotten` ⊷ `Let’s break the design`

```
Not another SMM bug
```

## Slide 5

⊷ `Key to SMM design: while SMM runs, nothing else does` ⊷ `SMI → all cores enter SMM together`

- ⊷ `“The rendezvous”`

- ⊷ `No SMM code runs until all checked in`

```
SMM design
```

## Slide 6

⊷ `SMM is hard to attack`

⊷ `~100 SMM TOCTOU CVEs: no one cares`

⊷ `Why? All cores in means none left out to attack`

```
The rendezvous defense
```

## Slide 7

⊷ `The SMM rendezvous has a timeout`

⊷ `Wait 1 second for cores to join SMM, then proceed`

⊷ `Keep one core out past 1 second`

⊷ `Others proceed → some in, some out`

```
The timeout
```

## Slide 8

⊷ `How?`

⊷ `Cores get pulled into SMM on instruction boundaries` ⊷ `SMI sent to core, core finishes instruction, enters SMM` ⊷ `Need: one machine instruction > 1 second` ⊷ `> ~4,000,000,000 cycles` ⊷ `SMM assumption: not possible.`

```
1 second
```

## Slide 9

```
100%
```

```
// LEADERBOARD
nop
```

```
of 4,000,000,000
```

# `nop`

## Slide 10

```
// LEADERBOARD
nop
```

```
0.25 cycles
```

```
0%
```

```
of 4,000,000,000
```

```
100%
```

# `nop`

- `0.25 cycles`

## Slide 11

```
// ACT II
```

```
The Race to the Bottom
```

## Slide 12

```
100%
```

```
// LEADERBOARD
nop
```

- `0.25 cycles`

```
0%
```

```
of 4,000,000,000
```

- ⊷ `rep strings, pause, jmp $ — interruptible`

- ⊷ `SMI checkpoints them mid-loop`

- ⊷ `Need uninterruptible`

```
The obvious picks fail
```

## Slide 13

```
100%
```

```
// LEADERBOARD
nop
0.25 cycles
```

```
0%
```

```
of 4,000,000,000
```

```
add rax, 1
```

## Slide 14

```
100%
```

```
// LEADERBOARD
add rax, 1
```

```
0.25 cycles
```

```
0%
```

```
of 4,000,000,000
```

```
add rax, 1
```

```
0.25 cycles
```

## Slide 15

```
100%
```

```
// LEADERBOARD
add rax, 1
```

```
0.25 cycles
```

```
0%
```

```
of 4,000,000,000
```

```
imul eax, ebx
```

## Slide 16

```
100%
```

```
// LEADERBOARD
imul eax, ebx
3 cycles
```

```
~0%
of 4,000,000,000
```

# `imul eax, ebx`

```
3 cycles
```

## Slide 17

```
// LEADERBOARD
imul eax, ebx
3 cycles
```

```
~0%
of 4,000,000,000
```

```
100%
```

# `idiv ebx`

## Slide 18

```
100%
```

```
// LEADERBOARD
idiv ebx
10 cycles
```

```
~0%
of 4,000,000,000
```

# `idiv ebx`

```
10 cycles
```

## Slide 19

```
// LEADERBOARD
idiv ebx
10 cycles
```

```
~0%
of 4,000,000,000
```

```
100%
```

```
mov eax, [rdi]
```

## Slide 20

```
100%
```

```
// LEADERBOARD
mov eax, [rdi]
11 cycles
```

```
~0%
```

```
of 4,000,000,000
```

```
mov eax, [rdi]
```

```
11 cycles — L1 miss
```

## Slide 21

```
100%
```

```
// LEADERBOARD
mov eax, [rdi]
11 cycles
```

```
~0%
of 4,000,000,000
```

```
sqrtsd xmm0, xmm1
```

## Slide 22

```
100%
```

```
// LEADERBOARD
sqrtsd xmm0, xmm1
```

```
12 cycles
```

```
~0%
of 4,000,000,000
```

```
sqrtsd xmm0, xmm1
```

```
12 cycles
```

## Slide 23

```
// LEADERBOARD
sqrtsd xmm0, xmm1
12 cycles
```

```
~0%
of 4,000,000,000
```

```
100%
```

```
not close.
get creative.
```

## Slide 24

```
100%
```

```
// LEADERBOARD
sqrtsd xmm0, xmm1
12 cycles
```

```
~0%
of 4,000,000,000
```

# `faddl subnorm`

## Slide 25

```
// LEADERBOARD
faddl subnorm
```

```
677 cycles
```

```
0.00001%
```

```
of 4,000,000,000
```

```
100%
```

# `faddl subnorm`

```
677 cycles
```

```
Denormal → x87 microcode assist
```

## Slide 26

```
// LEADERBOARD
faddl subnorm
677 cycles
```

```
0.00001%
```

```
of 4,000,000,000
```

```
100%
```

# `cpuid`

## Slide 27

```
// LEADERBOARD
cpuid
```

```
812 cycles
```

```
0.00002%
```

```
of 4,000,000,000
```

```
100%
```

# `cpuid`

```
812 cycles — pipeline serialize
```

## Slide 28

```
// LEADERBOARD
cpuid
```

```
812 cycles
```

```
0.00002%
```

```
of 4,000,000,000
```

```
100%
```

- ⊷ `Running out of ideas`

- ⊷ `Extend sandsifter`

- ⊷ `Fuzz timing across all of x86`

- ⊷ `Hunt the rare slow instruction`

## Slide 29

```
// LEADERBOARD
cpuid
812 cycles
```

```
0.00002%
```

```
of 4,000,000,000
```

```
100%
```

# `rdseed`

## Slide 30

```
// LEADERBOARD
rdseed
5,579 cycles
```

```
0.0001%
```

```
of 4,000,000,000
```

```
100%
```

# `rdseed`

- `5,579 cycles`

```
Fuzzer's champion
```

## Slide 31

```
// LEADERBOARD
rdseed
5,579 cycles
```

```
0.0001%
```

```
of 4,000,000,000
```

```
100%
```

- ⊷ `Ring 3 exhausted`

- ⊷ `Drop to ring 0`

- ⊷ `Unlock privileged instructions`

### `Going privileged`

## Slide 32

```
// LEADERBOARD
0.0001%
rdseed
of 4,000,000,000
5,579 cycles
```

```
100%
```

# `rdmsr`

## Slide 33

```
// LEADERBOARD
0.0025%
rdmsr
of 4,000,000,000
161,602 cycles
```

```
100%
```

# `rdmsr`

```
161,602 cycles — off-die register
```

## Slide 34

```
// LEADERBOARD
0.0025%
rdmsr
of 4,000,000,000
161,602 cycles
```

```
100%
```

# `wbinvd`

## Slide 35

```
// LEADERBOARD
wbinvd
321,946 cycles
```

```
0.0075%
of 4,000,000,000
```

```
100%
```

# `wbinvd`

```
321,946 cycles — flush all cache
```

## Slide 36

```
// LEADERBOARD
wbinvd
321,946 cycles
```

```
0.0075%
```

```
of 4,000,000,000
```

```
100%
```

- ⊷ `RAM + CPU: too fast`

- ⊷ `I/O is slow`

- ⊷ `Try port I/O`

### `Brick wall`

## Slide 37

```
// LEADERBOARD
0.0075%
wbinvd
of 4,000,000,000
321,946 cycles
```

```
100%
```

```
in dx, eax
```

## Slide 38

```
// LEADERBOARD
in dx, eax
```

```
1,121,988 cycles
```

```
0.025%
```

```
of 4,000,000,000
```

```
100%
```

```
in dx, eax
```

```
1,121,988 cycles — port I/O
```

## Slide 39

```
100%
```

```
// LEADERBOARD
in dx, eax
1,121,988 cycles
```

```
0.025%
```

```
of 4,000,000,000
```

- ⊷ `Port I/O maxes ~1,000,000 cycles` ⊷ `Can't reach full I/O space`

- ⊷ `Try memory-mapped I/O`

## Slide 40

```
100%
```

```
// LEADERBOARD
in dx, eax
```

```
1,121,988 cycles
```

- ⊷ `Map full MMIO space`

- ⊷ `Find the outliers`

```
0.025%
```

```
of 4,000,000,000
```

## Slide 41

```
100%
```

```
// LEADERBOARD
in dx, eax
1,121,988 cycles
```

```
0.025%
of 4,000,000,000
```

```
mov eax, [0xfcc003b0]
```

## Slide 42

```
100%
```

```
// LEADERBOARD
mov eax, [0xfcc003b0]
```

```
15,000,000 cycles
```

```
0.4%
```

```
of 4,000,000,000
```

```
mov eax, [0xfcc003b0]
```

```
15,000,000 cycles
```

## Slide 43

```
100%
```

- `// LEADERBOARD mov eax, [0xfcc003b0]`

```
15,000,000 cycles
```

- `0.4%`

```
of 4,000,000,000
```

- ⊷ `Stuck at 15M`

- ⊷ `We don't own the peripherals`

- ⊷ `Underclock: no effect (cycle-counted)`

- ⊷ `Low-power states: negligible`

- ⊷ `Legal options exhausted`

### `Brick wall`

## Slide 44

```
100%
```

```
// LEADERBOARD
mov eax, [0xfcc003b0]
15,000,000 cycles
```

```
0.4%
```

```
of 4,000,000,000
```

⊷ `MMIO access: 8 / 16 / 32-bit only` ⊷ `Must be 4-byte aligned`

⊷ `...says the spec`

⊷ `Everything else is` _`undefined behavior`_

```
The spec is just a suggestion
```

## Slide 45

```
100%
```

```
// LEADERBOARD
mov eax, [0xfcc003b0]
15,000,000 cycles
```

```
0.4%
of 4,000,000,000
```

```
mov rax, [0xfcc003b0]
```

## Slide 46

```
100%
```

```
// LEADERBOARD
mov rax, [0xfcc003b0]
30,000,000 cycles
```

```
0.75%
```

```
of 4,000,000,000
```

```
mov rax, [0xfcc003b0]
```

```
30,000,000 cycles
```

```
64-bit — illegal per spec    ·    Works anyway — 2 transactions
```

## Slide 47

```
100%
```

```
// LEADERBOARD
mov rax, [0xfcc003b0]
30,000,000 cycles
```

```
0.75%
```

```
of 4,000,000,000
```

```
mov rax, [0xfcc003b0+1]
```

## Slide 48

```
100%
```

```
// LEADERBOARD
mov rax, [0xfcc003b0+1]
50,000,000 cycles
```

```
1.25%
```

```
of 4,000,000,000
```

```
mov rax, [0xfcc003b0+1]
```

```
50,000,000 cycles
```

```
Unaligned — also illegal    ·    Works — 3 transactions
```

## Slide 49

```
// LEADERBOARD
mov rax, [0xfcc003b0+1]
50,000,000 cycles
```

- `1.25%`

```
of 4,000,000,000
```

```
100%
```

- ⊷ `16-byte nop from MMIO — can't build it`

- ⊷ `Page-table walk via MMIO — can't build PTEs`

- ⊷ `Both fail`

- ⊷ `Register width is the only lever`

- ⊷ `But we’re out of GPRs`

### `Some bad ideas`

## Slide 50

```
100%
```

```
// LEADERBOARD
mov rax, [0xfcc003b0+1]
```

```
50,000,000 cycles
```

- `1.25%`

```
of 4,000,000,000
```

- ⊷ `GPRs stop at 8 bytes`

- ⊷ `SIMD regs: built for speed`

- ⊷ `Repurpose for slowness`

```
Repurpose SIMD
```

## Slide 51

```
100%
```

```
// LEADERBOARD
mov rax, [0xfcc003b0+1]
50,000,000 cycles
```

```
1.25%
```

```
of 4,000,000,000
```

```
vmovdqu xmm, [0xfcc003b1]
```

## Slide 52

```
100%
```

```
// LEADERBOARD
vmovdqu xmm, [0xfcc003b1]
```

```
100,000,000 cycles
```

```
2.5%
```

```
of 4,000,000,000
```

```
vmovdqu xmm, [0xfcc003b1]
```

```
100,000,000 cycles
```

```
16 bytes
```

## Slide 53

```
100%
```

```
// LEADERBOARD
vmovdqu xmm, [0xfcc003b1]
```

```
2.5%
```

```
100,000,000 cycles
```

```
of 4,000,000,000
```

```
vmovdqu ymm, [0xfcc003b1]
```

## Slide 54

```
100%
```

```
// LEADERBOARD
vmovdqu ymm, [0xfcc003b1]
```

```
200,000,000 cycles
```

```
5%
```

```
of 4,000,000,000
```

```
vmovdqu ymm, [0xfcc003b1]
```

```
200,000,000 cycles
```

```
32 bytes
```

## Slide 55

```
100%
```

```
// LEADERBOARD
vmovdqu ymm, [0xfcc003b1]
200,000,000 cycles
```

```
5%
of 4,000,000,000
```

```
vmovdqu32 zmm, [0xfcc003b1]
```

## Slide 56

```
// LEADERBOARD
vmovdqu32 zmm, [0xfcc003b1]
```

```
400,000,000 cycles
```

```
10%
```

```
of 4,000,000,000
```

```
100%
```

```
vmovdqu32 zmm, [0xfcc003b1]
```

```
400,000,000 cycles
```

```
64 bytes
```

## Slide 57

```
// LEADERBOARD
vmovdqu32 zmm, [0xfcc003b1]
400,000,000 cycles
```

```
10%
of 4,000,000,000
```

```
100%
```

- ⊷ `There are no larger registers in x86` ⊷ `What about... multiple registers?`

- ⊷ `Load the entire floating point register state`

```
Brick wall
```

## Slide 58

```
// LEADERBOARD
vmovdqu32 zmm, [0xfcc003b1]
400,000,000 cycles
```

```
10%
of 4,000,000,000
```

```
100%
```

```
mov rsi, 0xfcc68830
fxrstor64 (%rsi)
```

## Slide 59

```
// LEADERBOARD
fxrstor64 (%rsi)
3,200,000,000 cycles
```

```
80%
of 4,000,000,000
```

```
100%
```

```
mov rsi, 0xfcc68830
fxrstor64 (%rsi)
```

- `3,200,000,000 cycles Loads 512 bytes of state`

## Slide 60

```
// LEADERBOARD
fxrstor64 (%rsi)
3,200,000,000 cycles
```

```
80%
```

```
of 4,000,000,000
```

```
100%
```

- ⊷ `Largest memory access in the ISA`

- ⊷ `Can't go wider`

- ⊷ `Maybe we can go _` _`slower`_ `_`

⊷ `Bus-lock contention?`

### `Brick wall`

## Slide 61

```
100%
```

```
// LEADERBOARD
fxrstor64 (%rsi)
3,200,000,000 cycles
```

```
80%
of 4,000,000,000
```

```
cores 1–15    mov rsi, 0xfcc68830
              mov r9d, 1
              lock xadd rsi, r9d
core 0        fxrstor64 (%rsi)
```

- `↑ bus-lock contention compounds across cores`

```
// THE FINISH LINE
The finish line
```

## Slide 62

```
// LEADERBOARD
fxrstor64 + bus-lock
```

```
198,002,498,236 cycles
```

```
4,950%
```

```
of 4,000,000,000
```

```
100%
```

```
cores 1–15    mov rsi, 0xfcc68830
              mov r9d, 1
              lock xadd rsi, r9d
core 0        fxrstor64 (%rsi)
```

```
↑ bus-lock contention compounds across cores
```

```
198,002,498,236 cycles   =   61 seconds
```

```
// THE FINISH LINE
```

### `The finish line`

## Slide 63

```
// ACT III
```

## `Weaponizing Uselessness`

## Slide 64

⊷ `Slow instruction outside SMM`

⊷ `Other cores hit the 1s rendezvous timeout`

⊷ `They proceed — some in, some out`

⊷ `Execute normal-mode code at same time as SMM`

## `The break`

## Slide 65

```
// DEMO
```

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
// DEMO
smiiiiiiiiiiiiiiii -— Live SMM rendezvous monitor
SMIs received (leader): 1
cpud [
cpul [
cpu2 [
cpu3 [
PRPRPPR
~<¢ee
spread: 0 @ IN LOCKSTEP
```

## Slide 66

⊷ `40-year design requirement: broken`

⊷ `~100 SMM TOCTOUs now software-reachable`

⊷ `Cloud: SMM pre-empts hypervisor → breaks confidential compute` ⊷ `Client: SMM write-protects firmware → persistence`

⊷ `New primitive — attack surface unmapped`

⊷ `Scope: any x86, billions of systems`

```
Impact
```

## Slide 67

⊷ `Remove timeout → stuck core hangs platform` ⊷ `Keep timeout → this attack works`

⊷ `Raise timeout → kills many-core server perf`

⊷ `No clean path`

## `Defense?`

## Slide 68

```
fxrstor64 (%rsi)
No longer useless
```

```
github.com/xoreaxeaxeax/smiiiiiiiiiiiiiiii
```

```
github.com/xoreaxeaxeax/asm-hall-of-shame
```

```
Weaponizing Uselessness   ·   domas   ·   @xoreaxeaxeax
```
