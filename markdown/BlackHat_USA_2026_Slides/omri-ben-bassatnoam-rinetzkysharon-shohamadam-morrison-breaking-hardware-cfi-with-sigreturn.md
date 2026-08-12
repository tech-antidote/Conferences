---
title: "Breaking Hardware CFI with Sigreturn"
speakers: ["Omri Ben-Bassat", "Noam Rinetzky", "Sharon Shoham", "Adam Morrison"]
conference: "Black Hat"
conference_full: "Black Hat USA 2026"
edition: "USA"
year: 2026
source_pdf: "BlackHat_USA_2026_Slides/Omri Ben-Bassat&Noam Rinetzky&Sharon Shoham&Adam Morrison_Breaking Hardware CFI with Sigreturn.pdf"
pages: 68
sha256: "d99ad79a3965701e0b31055aeef512b5202c11278371427ac69574e177e7798b"
text_chars: 53606
ocr_pages: 19
has_ocr: true
redacted_secrets: 0
ocr_confidence: 82.6
ocr_unreliable_blocks: 0
content_note: "All 68 pages were rendered and read against the source PDF by a vision model; 61 were rewritten and 7 confirmed correct. The ocr_* fields describe the superseded first-pass extraction."
vision_verified_pages_changed: 61
vision_verified_pages: 68
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T05:40:55Z"
---
# Breaking Hardware CFI with Sigreturn

**Speakers:** Omri Ben-Bassat, Noam Rinetzky, Sharon Shoham, Adam Morrison  
**Conference:** Black Hat USA 2026  
**Source:** `BlackHat_USA_2026_Slides/Omri Ben-Bassat&Noam Rinetzky&Sharon Shoham&Adam Morrison_Breaking Hardware CFI with Sigreturn.pdf` (68 pages)


## Slide 1

# Breaking Hardware CFI with Sigreturn

_<u>Omri Ben-Bassat</u> , Prof. Noam Rinetzky, Prof. Sharon Shoham, Prof. Adam Morrison_

_Tel Aviv University_

## Slide 2

### $ whoami

Omri Ben-Bassat
_Vulnerability Researcher & MSc Candidate_

Prof. Noam Rinetzky

Prof. Sharon Shoham Buchbinder

Prof. Adam Morrison

Information Classification: General

## Slide 3

### SROP/BTI

- A novel ARM64 hardware-CFI bypass
- Breaks BTI even with PAC enabled
- Demonstrated on Ubuntu 26.04 and Android 17

Information Classification: General

## Slide 4

### Control Flow Integrity (CFI)

- Modern class of mitigations
- Restricts a program’s execution
- Only intended control-flow paths

Information Classification: General

## Slide 5

### ARM64 _Pointer Authentication Code (PAC)_

- ARM mechanism for authenticating pointers
- Can protect both forward and backward edges
- Linux deploys PAC as backward-edge CFI
- Signs return addresses (`pac-ret`)
- Aims to mitigate ROP

Information Classification: General

## Slide 6

### PACIxSP + AUTIxSP

```text
pwndbg> disas main
Dump of assembler code for function main:
   0x0000000000000828 <+0>:     paciasp
   0x000000000000082c <+4>:     stp     x29, x30, [sp, #-32]!
   0x0000000000000830 <+8>:     mov     x29, sp
   0x0000000000000834 <+12>:    str     w0, [sp, #28]
   0x0000000000000838 <+16>:    str     x1, [sp, #16]
   0x000000000000083c <+20>:    adrp    x0, 0x0
   0x0000000000000840 <+24>:    add     x0, x0, #0x878
   0x0000000000000844 <+28>:    bl      0x6c0 <printf@plt>
   0x0000000000000848 <+32>:    mov     w0, #0x0                    // #0
   0x000000000000084c <+36>:    ldp     x29, x30, [sp], #32
   0x0000000000000850 <+40>:    autiasp
   0x0000000000000854 <+44>:    ret
End of assembler dump.
```

`gcc … -mbranch-protection=pac-ret`

Information Classification: General

## Slide 7

### PACIxSP + AUTIxSP

```text
pwndbg> disas main
Dump of assembler code for function main:
   0x0000000000000828 <+0>:     paciasp  ←
   0x000000000000082c <+4>:     stp     x29, x30, [sp, #-32]!
   0x0000000000000830 <+8>:     mov     x29, sp
   0x0000000000000834 <+12>:    str     w0, [sp, #28]
   0x0000000000000838 <+16>:    str     x1, [sp, #16]
   0x000000000000083c <+20>:    adrp    x0, 0x0
   0x0000000000000840 <+24>:    add     x0, x0, #0x878
   0x0000000000000844 <+28>:    bl      0x6c0 <printf@plt>
   0x0000000000000848 <+32>:    mov     w0, #0x0                    // #0
   0x000000000000084c <+36>:    ldp     x29, x30, [sp], #32
   0x0000000000000850 <+40>:    autiasp  ←
   0x0000000000000854 <+44>:    ret
End of assembler dump.
```

`gcc … -mbranch-protection=pac-ret`

Information Classification: General

## Slide 8

### ARM64 _Branch Target Identification (BTI)_

- Aims to mitigate JOP
- Forward-edge CFI
- Compiler plants _Landing Pads (LP)_
- LPs are the only valid branch targets
- Enforced in HW

Information Classification: General

## Slide 9

### Threat Model

- Target is Linux user mode program
- Latest OS on ARMv8.5-A+
- `-mbranch-protection=standard (bti+pac-ret)`
  `=> No ROP / JOP`
- Memory corruption
- ASLR derandomization

Information Classification: General

## Slide 10

### BTI implementation

`blr xN`

`pstate.btype := 0b11`

_A green arrow runs from `blr xN` to the top of the code box:_

```text
// func A
bti // Landing Pad
...
// JOP gadget1
add x0, x1, x2
br xN
...
ret
```

<https://developer.arm.com/documentation/102433/0200/Jump-oriented-programming>

Information Classification: General

## Slide 11

### BTI implementation

`blr xN`

`pstate.btype := 0b11`

- `bti`
  - `pstate.btype := 0b00`

_A green arrow runs from `blr xN` to the `bti` line of the code box:_

```text
// func A
bti // Landing Pad
...
// JOP gadget1
add x0, x1, x2
br xN
...
ret
```

<https://developer.arm.com/documentation/102433/0200/Jump-oriented-programming>

Information Classification: General

## Slide 12

### BTI implementation

`blr xN`

`pstate.btype := 0b11`

- `bti`
  - `pstate.btype := 0b00`
- `add x0, x1, x2`
  - `pstate.btype != 0 => Branch Target Exception`🔥

_A red arrow runs from `blr xN` to the `add x0, x1, x2` line of the code box:_

```text
// func A
bti // Landing Pad
...
// JOP gadget1
add x0, x1, x2
br xN
...
ret
```

<https://developer.arm.com/documentation/102433/0200/Jump-oriented-programming>

Information Classification: General

## Slide 13

_Meme image (the “two buttons” panel): a sweating man agonising over two red buttons, the left one labelled `br xN` and the right one labelled `btype = 0`._

JUMP ORIENTED PROGRAMING

imgflip.com

JAKE-CLARK.TUMBLR

Information Classification: General

## Slide 14

### No JOP? Just Ask the Kernel!

- `rt_sigreturn`
- POSIX signal-resumption mechanism
  - x0–x30, SP, PC, …
  - PSTATE
- Resumes execution at the restored PC
- No BTI landing-pad validation

Information Classification: General

## Slide 15

### Sigreturn: A BTI Bypass by Design 🔮

**user** | **kernel**

```
// func A
...
// JOP gadget1
add x0, x1, x2
br xN
```

*(red arrow points to `add x0, x1, x2`)*

Information Classification: General

## Slide 16

### Sigreturn: A BTI Bypass by Design 🔮

**user** | **kernel**

**Crafted rt_sigframe**

|  |
| --- |
| … |
| regs[31] |
| sp |
| pc = &gadget1 |
| pstate.btype=0 |

```
// func A
...
// JOP gadget1
add x0, x1, x2
br xN
```

Information Classification: General

## Slide 17

### Sigreturn: A BTI Bypass by Design 🔮

**user** | **kernel**

**Crafted rt_sigframe**

|  |
| --- |
| … |
| regs[31] |
| sp |
| pc = &gadget1 |
| pstate.btype=0 |

```
// func A
...
// JOP gadget1
add x0, x1, x2
br xN
```

*(dashed arrow: `pc = &gadget1` → the gadget1 code)*

Information Classification: General

## Slide 18

### Sigreturn: A BTI Bypass by Design 🔮

**user** | **kernel**

**Crafted rt_sigframe**

|  |
| --- |
| … |
| regs[31] |
| sp |
| pc = &gadget1 |
| pstate.btype=0 |

*(green arrow: Crafted rt_sigframe →)* **`__kernel_rt_sigreturn`**

```
// func A
...
// JOP gadget1
add x0, x1, x2
br xN
```

*(dashed arrow: `pc = &gadget1` → the gadget1 code)*

Information Classification: General

## Slide 19

### Sigreturn: A BTI Bypass by Design 🔮

**user** | **kernel**

**Crafted rt_sigframe**

|  |
| --- |
| … |
| regs[31] |
| sp |
| pc = &gadget1 |
| pstate.btype=0 |

*(green arrow: Crafted rt_sigframe →)* **`__kernel_rt_sigreturn`**

*(arrow →)* **`rt_sigreturn`** (kernel side)

```
// func A
...
// JOP gadget1
add x0, x1, x2
br xN
```

*(dashed arrow: `pc = &gadget1` → the gadget1 code)*

Information Classification: General

## Slide 20

### Sigreturn: A BTI Bypass by Design 🔮

**user** | **kernel**

**Crafted rt_sigframe**

|  |
| --- |
| … |
| regs[31] |
| sp |
| pc = &gadget1 |
| pstate.btype=0 |

*(green arrow: Crafted rt_sigframe →)* **`__kernel_rt_sigreturn`**

*(arrow →)* **`rt_sigreturn`** (kernel side)

ERET

```
// func A
...
// JOP gadget1
add x0, x1, x2
br xN
```

*(dashed arrow: `pc = &gadget1` → the gadget1 code)*

*(arrow: rt_sigreturn → the gadget1 code, via ERET)*

Information Classification: General

## Slide 21

### Sigreturn: A BTI Bypass by Design 🔮

**user** | **kernel**

**Crafted rt_sigframe**

|  |
| --- |
| … |
| regs[31] |
| sp |
| pc = &gadget1 |
| pstate.btype=0 |

*(green arrow: Crafted rt_sigframe →)* **`__kernel_rt_sigreturn`**

*(arrow →)* **`rt_sigreturn`** (kernel side)

ERET

```
// func A
...
// JOP gadget1
add x0, x1, x2
br xN
```

*(dashed arrow: `pc = &gadget1` → the gadget1 code)*

*(arrow: rt_sigreturn → the gadget1 code, via ERET)*

✅ pc == &gadget1

Information Classification: General

## Slide 22

### Sigreturn: A BTI Bypass by Design 🔮

**user** | **kernel**

**Crafted rt_sigframe**

|  |
| --- |
| … |
| regs[31] |
| sp |
| pc = &gadget1 |
| pstate.btype=0 |

*(green arrow: Crafted rt_sigframe →)* **`__kernel_rt_sigreturn`**

*(arrow →)* **`rt_sigreturn`** (kernel side)

ERET

```
// func A
...
// JOP gadget1
add x0, x1, x2
br xN
```

*(dashed arrow: `pc = &gadget1` → the gadget1 code)*

*(arrow: rt_sigreturn → the gadget1 code, via ERET)*

✅ pc == &gadget1  
✅ pstate.btype == 0

Information Classification: General

## Slide 23

### Sigreturn: A BTI Bypass by Design 🔮

**user** | **kernel**

**Crafted rt_sigframe**

|  |
| --- |
| … |
| regs[31] |
| sp |
| pc = &gadget1 |
| pstate.btype=0 |

*(green arrow: Crafted rt_sigframe →)* **`__kernel_rt_sigreturn`**

*(arrow →)* **`rt_sigreturn`** (kernel side)

ERET

```
// func A
...
// JOP gadget1
add x0, x1, x2
br xN
```

*(dashed arrow: `pc = &gadget1` → the gadget1 code)*

*(arrow: rt_sigreturn → the gadget1 code, via ERET)*

✅ pc == &gadget1  
✅ pstate.btype == 0  
✅ BTI BYPASSED

Information Classification: General

## Slide 24

### From Super Gadget to BTI Bypass

| Year | Milestone |
| --- | --- |
| 2014 | Sigreturn Oriented Programming (SROP) — Bosman & Bos |
| 2016 | CET, PAC |
| 2018 | BTI, ARMv8.5-A |
| 2025 | BTI Support In Ubuntu (25.04) |
| 2026 | *SROP/BTI* |

**NO HW CFI** *(red, marking the 2014–2016 span of the timeline)*

Information Classification: General

## Slide 25

### Bootstrapping SROP/BTI

- `rt_sigreturn` takes sigframe from <u>stack pointer</u>
- `pac-ret` ⇒ No more (exploitable) stack overflows
- BTI ⇒ Can't jump to ROP/JOP stack pivot

|  |
| --- |
| … |
| LR |
| Crafted rt_sigframe |
| … |

Information Classification: General

## Slide 26

### Bootstrapping SROP/BTI

- `rt_sigreturn` takes sigframe from <u>stack pointer</u>
- `pac-ret` ⇒ No more (exploitable) stack overflows
- BTI ⇒ Can't jump to ROP/JOP stack pivot

|  |
| --- |
| … |
| ~~LR~~ → __kernel_rt_sigreturn |
| **SP →** Crafted rt_sigframe |
| … |

Information Classification: General

## Slide 27

### SROP/BTI CFI-Safe Stack Pivots

1. bti

2. sp := xN // xN=&frame_1

3. br xM    // xM=__kernel_rt_sigreturn

Information Classification: General

## Slide 28

### Glibc — CFI Safe Pivot

Distro logos shown: Ubuntu, Fedora, Debian, openSUSE, Gentoo.

Ghidra listing window — title bar: **Listing: libc.so.6 - (16 addresses selected)**

```text
0013ec7f d5              ??       D5h
                    ****************************************************************
                    *                          FUNCTION                            *
                    ****************************************************************
                    undefined setcontext()
undefined         <UNASSIGNED>    <RETURN>
                  setcontext                    XREF[5]:   Entry Point(*),
                                                           FUN_0013edc0:0013edcc(j),
                                                           swapcontext:0014bad8(c),
                                                           00274b28, 0027f570(*)
0013ec80 5f 24 03 d5     bti      c
0013ec84 e9 03 00 aa     mov      x9,x0
0013ec88 40 00 80 d2     mov      x0,#0x2
0013ec8c 21 a1 00 91     add      x1,x9,#0x28
0013ec90 02 00 80 d2     mov      x2,#0x0
0013ec94 03 01 80 d2     mov      x3,#0x8
0013ec98 e8 10 80 d2     mov      x8,#0x87
0013ec9c 01 00 00 d4     svc      0x0
0013eca0 40 00 00 b4     cbz      x0,LAB_0013eca8
0013eca4 1f 91 ff 17     b        FUN_00123120              undefined FUN_00123120()
                    -- Flow Override: CALL_RETURN (CALL_TERMINATOR)

                    LAB_0013eca8                  XREF[1]:   0013eca0(j)
0013eca8 ed 03 1e aa     mov      x13,x30
0013ecac e5 e6 02 94     bl       FUN_001f8840              undefined FUN_001f8840()
0013ecb0 fe 03 0d aa     mov      x30,x13
0013ecb4 e0 03 09 aa     mov      x0,x9
0013ecb8 12 cc 54 a9     ldp      x18,x19,[x0, #0x148]
0013ecbc 14 d4 55 a9     ldp      x20,x21,[x0, #0x158]
0013ecc0 16 dc 56 a9     ldp      x22,x23,[x0, #0x168]
0013ecc4 18 e4 57 a9     ldp      x24,x25,[x0, #0x178]
0013ecc8 1a ec 58 a9     ldp      x26,x27,[x0, #0x188]
0013eccc 1c f4 59 a9     ldp      x28,x29,[x0, #0x198]
0013ecd0 1e d4 40 f9     ldr      x30,[x0, #0x1a8]
0013ecd4 02 d8 40 f9     ldr      x2,[x0, #0x1b0]
0013ecd8 5f 00 00 91     mov      sp,x2
0013ecdc 02 40 07 91     add      x2,x0,#0x1d0
0013ece0 [row cut off at panel edge — illegible]

                    LAB_0013ed90                  XREF[4]:   0013ecf0(j), 0013ed24(j),
                                                             0013ed40(j), 0013ed80(j)
0013ed90 10 dc 40 f9     ldr      x16,[x0, #0x1b8]
0013ed94 02 8c 4c a9     ldp      x2,x3,[x0, #0xc8]
0013ed98 04 94 4d a9     ldp      x4,x5,[x0, #0xd8]
0013ed9c 06 9c 4e a9     ldp      x6,x7,[x0, #0xe8]
0013eda0 00 84 4b a9     ldp      x0,x1,[x0, #0xb8]
0013eda4 00 02 1f d6     br       x16
0013eda8 [row cut off at panel edge — illegible; ends in `b  FUN_00123120`]
```

Information Classification: General

## Slide 29

### Glibc CFI Safe Pivot

**Left panel — Ghidra disassembly listing.** Title bar: "Listing: libc.so.6 - (16 addresses selected)"

```text
0013ec7f d5                     ??            D5h

                                 ****************************************************
                                 *                    FUNCTION                      *
                                 ****************************************************
                                 undefined setcontext()
undefined                       <UNASSIGNED>  <RETURN>
                                 setcontext                     XREF[5]:   Entry Point(*),
                                                                            FUN_0013edc0:0013edcc(j),
                                                                            swapcontext:0014bad8(c),
                                                                            00274b28, 0027f570(*)
0013ec80 5f 24 03 d5   bti      c                    <- "Landing Pad" callout
0013ec84 e9 03 00 aa   mov      x9,x0
0013ec88 40 00 80 d2   mov      x0,#0x2
0013ec8c 21 a1 00 91   add      x1,x9,#0x28
0013ec90 02 00 80 d2   mov      x2,#0x0
0013ec94 03 01 80 d2   mov      x3,#0x8
0013ec98 e8 10 80 d2   mov      x8,#0x87
0013ec9c 01 00 00 d4   svc      0x0
0013eca0 40 00 00 b4   cbz      x0,LAB_0013eca8
0013eca4 1f 91 ff 17   b        FUN_00123120                   undefined FUN_00123120()
                                 -- Flow Override: CALL_RETURN (CALL_TERMINATOR)

                                 LAB_0013eca8                   XREF[1]:   0013eca0(j)
0013eca8 ed 03 1e aa   mov      x13,x30
0013ecac e5 e6 02 94   bl       FUN_001f8840                   undefined FUN_001f8840()
0013ecb0 fe 03 0d aa   mov      x30,x13
0013ecb4 e0 03 09 aa   mov      x0,x9
0013ecb8 12 cc 54 a9   ldp      x18,x19,[x0, #0x148]
0013ecbc 14 d4 55 a9   ldp      x20,x21,[x0, #0x158]
0013ecc0 16 dc 56 a9   ldp      x22,x23,[x0, #0x168]
0013ecc4 18 e4 57 a9   ldp      x24,x25,[x0, #0x178]
0013ecc8 1a ec 58 a9   ldp      x26,x27,[x0, #0x188]
0013eccc 1c f4 59 a9   ldp      x28,x29,[x0, #0x198]
0013ecd0 1e d4 40 f9   ldr      x30,[x0, #0x1a8]        <- "LR" callout
0013ecd4 02 d8 40 f9   ldr      x2,[x0, #0x1b0]
0013ecd8 5f 00 00 91   mov      sp,x2                   <- "SP" callout
0013ecdc 02 40 07 91   add      x2,x0,#0x1d0
...
                                 LAB_0013ed90                   XREF[4]:   0013ecf0(j), 0013ed24(j),
                                                                            0013ed40(j), 0013ed80(j)
0013ed90 10 dc 40 f9   ldr      x16,[x0, #0x1b8]        <- "PC" callout
0013ed94 02 8c 4c a9   ldp      x2,x3,[x0, #0xc8]
0013ed98 04 94 4d a9   ldp      x4,x5,[x0, #0xd8]
0013ed9c 06 9c 4e a9   ldp      x6,x7,[x0, #0xe8]
0013eda0 00 84 4b a9   ldp      x0,x1,[x0, #0xb8]
0013eda4 00 02 1f d6   br       x16                     <- "PC" callout
[illegible] b   FUN_00123120   (row cut off at the bottom edge of the screenshot)
```

**Right panel:** heading "Glibc" / "CFI Safe Pivot", below which are the logos of Ubuntu, Fedora, Debian, and openSUSE (no accompanying text), and the "black hat USA 2026" logo.

Information Classification: General

## Slide 30

### Caveats

```text
63
64  /*
65   * GDB, libgcc and libunwind rely on being able to identify the sigreturn
66   * instruction sequence to unwind from signal handlers. We cannot, therefore,
67   * use SYM_FUNC_START() here, as it will emit a BTI C instruction and break the
68   * unwinder. Thankfully, this function is only ever called from a RET and so
69   * omitting the landing pad is perfectly fine.
70   */
71  SYM_CODE_START(__kernel_rt_sigreturn)
72  //      PLEASE DO NOT MODIFY
73          mov     x8, #__NR_rt_sigreturn
74  //      PLEASE DO NOT MODIFY
75          svc     #0
76  //      PLEASE DO NOT MODIFY
77  //      .cfi_endproc
78  SYM_CODE_END(__kernel_rt_sigreturn)
79
80  emit_aarch64_feature_1_and
```

Information Classification: General

## Slide 31

### Caveats

*A white call-out box is overlaid on the code, zooming in on (and repeating) part of the comment:*

```text
* instruction sequence to unwind from signal handlers. We cannot, therefore,
* use SYM_FUNC_START() here, as it will emit a BTI C instruction and break the
* unwinder. Thankfully, this function is only ever called from a RET and so
* omitting the landing pad is perfectly fine.
```

**Underlying code listing (same as previous build step):**

```text
63
64  /*
65   * GDB, libgcc and libunwind rely on being able to identify the sigreturn
66   * instruction sequence to unwind from signal handlers. We cannot, therefore,
67   * use SYM_FUNC_START() here, as it will emit a BTI C instruction and break the
68   * unwinder. Thankfully, this function is only ever called from a RET and so
69   * omitting the landing pad is perfectly fine.
70   */
71  SYM_CODE_START(__kernel_rt_sigreturn)
72  //      PLEASE DO NOT MODIFY
73          mov     x8, #__NR_rt_sigreturn
74  //      PLEASE DO NOT MODIFY
75          svc     #0
76  //      PLEASE DO NOT MODIFY
77  //      .cfi_endproc
78  SYM_CODE_END(__kernel_rt_sigreturn)
79
80  emit_aarch64_feature_1_and
```

Information Classification: General

## Slide 32

### Caveats

*The white call-out box still overlays the top of the code (same clipped comment text as before). A second, black call-out box now reads "Most Linux Distros", with a red arrow pointing right at a Kconfig source panel.*

**Kconfig snippet (right panel):** line numbers 2092-2100 are hidden behind the black "Most Linux Distros" box; the code text itself is unobstructed.

```text
2089
2090  config ARM64_BTI_KERNEL
2091          bool "Use Branch Target Identification for kernel"
              default y
              depends on ARM64_BTI
              depends on ARM64_PTR_AUTH_KERNEL
              depends on CC_HAS_BRANCH_PROT_PAC_RET_BTI
              # https://gcc.gnu.org/bugzilla/show_bug.cgi?id=94697
              depends on !CC_IS_GCC || GCC_VERSION >= 100100
              # https://gcc.gnu.org/bugzilla/show_bug.cgi?id=106671
              depends on !CC_IS_GCC
              depends on (!FUNCTION_GRAPH_TRACER || DYNAMIC_FTRACE_WITH_ARGS)
2101          help
2102            Build the kernel with Branch Target Identification annotations
2103            and enable enforcement of this for kernel code. When this option
2104            is enabled and the system supports BTI all kernel code including
2105            modular code must have BTI enabled.
2106
```

**Underlying code listing (partially covered, same as previous slides):**

```text
71  SYM_CODE_START(__kernel_rt_sigreturn)
72  //      PLEASE DO NOT MODIFY
73          mov     x8, #__NR_rt_sigreturn
74  //      PLEASE DO NOT MODIFY
75          svc     #0
76  //      PLEASE DO NOT MODIFY
77  //      .cfi_endproc
78  SYM_CODE_END(__kernel_rt_sigreturn)
79
80  emit_aarch64_feature_1_and
```

Information Classification: General

## Slide 33

### Forward-to-Backward Edge Gadget

*Flow diagram, four boxes connected by arrows:*

- Box (light, top-left): `setcontext(&pivot_ctx)` — an arrow enters from above; an arrow labelled "br x16" leaves to the right, into the next box.
- Box (light, "Magical Gadget" 🔮):
  ```text
  bti
  …  // no side effects
  ret
  ```
  An arrow labelled "ret" leaves to the right into the next box.
- Box (light): `__kernel_rt_sigreturn`
- Box (dark, below the "setcontext" box): `ucontext_t pivot_ctx`
  ```text
  …
  x0 = x1 = 1
  pc = Magical Gadget
  sp = fake_sigframe
  💥 lr = __kernel_rt_sigreturn
  …
  ```
  (the 💥 explosion icon marks the `lr = __kernel_rt_sigreturn` line)

Information Classification: General

## Slide 34

### Forward-to-Backward Edge Gadget

*Same flow diagram as the previous build step:*

- Box (light, top-left): `setcontext(&pivot_ctx)` — an arrow enters from above; an arrow labelled "br x16" leaves to the right, into the next box.
- Box (light, "Magical Gadget" 🔮):
  ```text
  bti
  …  // no side effects
  ret
  ```
  An arrow labelled "ret" leaves to the right into the next box.
- Box (light): `__kernel_rt_sigreturn`
- Box (dark, below the "setcontext" box): `ucontext_t pivot_ctx`
  ```text
  …
  x0 = x1 = 1
  pc = Magical Gadget
  sp = fake_sigframe
  💥 lr = __kernel_rt_sigreturn
  …
  ```

**A disassembly panel is now overlaid at bottom-right, showing what the "Magical Gadget" actually is:**

```text
0043c6e0     int64_t lldiv(int64_t arg1, int64_t arg2)

0043c6e0  5f2403d5   bti      c
0043c6e4  e20300aa   mov      x2, x0
0043c6e8  3f2303d5   paciasp
0043c6ec  fd7bbfa9   stp      fp, lr, [sp, #-0x10]! {__saved_fp} {__saved_lr}
0043c6f0  000cc19a   sdiv     x0, x0, x1
0043c6f4  fd030091   mov      fp, sp {__saved_fp}
0043c6f8  fd7bc1a8   ldp      fp, lr, [sp], #0x10 {__saved_fp} {__saved_lr}
0043c6fc  bf2303d5   autiasp
0043c700  0188019b   msub     x1, x0, x1, x2
0043c704  c0035fd6   ret
```

Information Classification: General

## Slide 35

### Bionic (/ llvm-libunwind) CFI Safe Pivot

Source: Google.

*Right side: photo of a smartphone with a shattered/cracked screen (mountain-range wallpaper visible behind the cracks).*

**Left panel — Ghidra disassembly listing.** Title bar: "Listing: libc.so - (20 addresses selected)"

```text
                                 ****************************************************
                                 *                    FUNCTION                      *
                                 ****************************************************
                                 undefined __libunwind_Registers_arm64_jumpto()
undefined                       <UNASSIGNED>  <RETURN>
                                 __libunwind_Registers_arm64_jumpto   XREF[3]:  __libunwind_shstk_get_jump_targe...
                                                                                 jumpto:001f0910(c), 001ff210(*)
001f4190 df 24 03 d5   bti      jc
001f4194 02 0c 41 a9   ldp      x2,x3,[x0, #0x10]
001f4198 04 14 42 a9   ldp      x4,x5,[x0, #0x20]
001f419c 06 1c 43 a9   ldp      x6,x7,[x0, #0x30]
001f41a0 08 24 44 a9   ldp      x8,x9,[x0, #0x40]
001f41a4 0a 2c 45 a9   ldp      x10,x11,[x0, #0x50]
001f41a8 0c 34 46 a9   ldp      x12,x13,[x0, #0x60]
001f41ac 0e 3c 47 a9   ldp      x14,x15,[x0, #0x70]
001f41b0 12 4c 49 a9   ldp      x18,x19,[x0, #0x90]
001f41b4 14 54 4a a9   ldp      x20,x21,[x0, #0xa0]
001f41b8 16 5c 4b a9   ldp      x22,x23,[x0, #0xb0]
001f41bc 18 64 4c a9   ldp      x24,x25,[x0, #0xc0]
001f41c0 1a 6c 4d a9   ldp      x26,x27,[x0, #0xd0]
001f41c4 1c 74 4e a9   ldp      x28,x29,[x0, #0xe0]
001f41c8 1e 80 40 f9   ldr      x30,[x0, #0x100]
001f41cc 00 04 51 6d   ldp      d0,d1,[x0, #0x110]
001f41d0 02 0c 52 6d   ldp      d2,d3,[x0, #0x120]
001f41d4 04 14 53 6d   ldp      d4,d5,[x0, #0x130]
001f41d8 06 1c 54 6d   ldp      d6,d7,[x0, #0x140]
001f41dc 08 24 55 6d   ldp      d8,d9,[x0, #0x150]
001f41e0 0a 2c 56 6d   ldp      d10,d11,[x0, #0x160]
001f41e4 0c 34 57 6d   ldp      d12,d13,[x0, #0x170]
001f41e8 0e 3c 58 6d   ldp      d14,d15,[x0, #0x180]
001f41ec 10 44 59 6d   ldp      d16,d17,[x0, #0x190]
001f41f0 12 4c 5a 6d   ldp      d18,d19,[x0, #0x1a0]
001f41f4 14 54 5b 6d   ldp      d20,d21,[x0, #0x1b0]
001f41f8 16 5c 5c 6d   ldp      d22,d23,[x0, #0x1c0]
001f41fc 18 64 5d 6d   ldp      d24,d25,[x0, #0x1d0]
001f4200 1a 6c 5e 6d   ldp      d26,d27,[x0, #0x1e0]
001f4204 1c 74 5f 6d   ldp      d28,d29,[x0, #0x1f0]
001f4208 1e 00 41 fd   ldr      d30,[x0, #0x200]
001f420c 1f 04 41 fd   ldr      d31,[x0, #0x208]
001f4210 10 7c 40 f9   ldr      x16,[x0, #0xf8]
001f4214 00 04 40 a9   ldp      x0,x1,[x0]
001f4218 1f 02 00 91   mov      sp,x16
001f421c 30 00 80 d2   mov      x16,#0x1
001f4220 1f 25 03 d5   hint     0x28
001f4224 50 00 00 b5   cbnz     x16,Lnogcs
001f4228 1e 77 0b d5   sys      0x3, 0x7, 0x7, 0x0, x30

                                 Lnogcs                    XREF[1]:  001f4224(j)
001f422c c0 03 5f d6   ret
```

Information Classification: General

## Slide 36

### Bionic (/ llvm-libunwind) CFI Safe Pivot

Source: Google.

*Right side: photo of a smartphone with a shattered/cracked screen (mountain-range wallpaper visible behind the cracks).*

**Left panel — Ghidra disassembly listing** (same listing as the previous slide), with two red-arrow callouts:
- "Landing Pad" points to the `bti jc` instruction at 001f4190.
- "SP" points to both `ldr x16,[x0, #0xf8]` (001f4210) and `mov sp,x16` (001f4218).

```text
                                 ****************************************************
                                 *                    FUNCTION                      *
                                 ****************************************************
                                 undefined __libunwind_Registers_arm64_jumpto()
undefined                       <UNASSIGNED>  <RETURN>
                                 __libunwind_Registers_arm64_jumpto   XREF[3]:  __libunwind_shstk_get_jump_targe...
                                                                                 jumpto:001f0910(c), 001ff210(*)
001f4190 df 24 03 d5   bti      jc
001f4194 02 0c 41 a9   ldp      x2,x3,[x0, #0x10]
001f4198 04 14 42 a9   ldp      x4,x5,[x0, #0x20]
001f419c 06 1c 43 a9   ldp      x6,x7,[x0, #0x30]
001f41a0 08 24 44 a9   ldp      x8,x9,[x0, #0x40]
001f41a4 0a 2c 45 a9   ldp      x10,x11,[x0, #0x50]
001f41a8 0c 34 46 a9   ldp      x12,x13,[x0, #0x60]
001f41ac 0e 3c 47 a9   ldp      x14,x15,[x0, #0x70]
001f41b0 12 4c 49 a9   ldp      x18,x19,[x0, #0x90]
001f41b4 14 54 4a a9   ldp      x20,x21,[x0, #0xa0]
001f41b8 16 5c 4b a9   ldp      x22,x23,[x0, #0xb0]
001f41bc 18 64 4c a9   ldp      x24,x25,[x0, #0xc0]
001f41c0 1a 6c 4d a9   ldp      x26,x27,[x0, #0xd0]
001f41c4 1c 74 4e a9   ldp      x28,x29,[x0, #0xe0]
001f41c8 1e 80 40 f9   ldr      x30,[x0, #0x100]
001f41cc 00 04 51 6d   ldp      d0,d1,[x0, #0x110]
001f41d0 02 0c 52 6d   ldp      d2,d3,[x0, #0x120]
001f41d4 04 14 53 6d   ldp      d4,d5,[x0, #0x130]
001f41d8 06 1c 54 6d   ldp      d6,d7,[x0, #0x140]
001f41dc 08 24 55 6d   ldp      d8,d9,[x0, #0x150]
001f41e0 0a 2c 56 6d   ldp      d10,d11,[x0, #0x160]
001f41e4 0c 34 57 6d   ldp      d12,d13,[x0, #0x170]
001f41e8 0e 3c 58 6d   ldp      d14,d15,[x0, #0x180]
001f41ec 10 44 59 6d   ldp      d16,d17,[x0, #0x190]
001f41f0 12 4c 5a 6d   ldp      d18,d19,[x0, #0x1a0]
001f41f4 14 54 5b 6d   ldp      d20,d21,[x0, #0x1b0]
001f41f8 16 5c 5c 6d   ldp      d22,d23,[x0, #0x1c0]
001f41fc 18 64 5d 6d   ldp      d24,d25,[x0, #0x1d0]
001f4200 1a 6c 5e 6d   ldp      d26,d27,[x0, #0x1e0]
001f4204 1c 74 5f 6d   ldp      d28,d29,[x0, #0x1f0]
001f4208 1e 00 41 fd   ldr      d30,[x0, #0x200]
001f420c 1f 04 41 fd   ldr      d31,[x0, #0x208]
001f4210 10 7c 40 f9   ldr      x16,[x0, #0xf8]
001f4214 00 04 40 a9   ldp      x0,x1,[x0]
001f4218 1f 02 00 91   mov      sp,x16
001f421c 30 00 80 d2   mov      x16,#0x1
001f4220 1f 25 03 d5   hint     0x28
001f4224 50 00 00 b5   cbnz     x16,Lnogcs
001f4228 1e 77 0b d5   sys      0x3, 0x7, 0x7, 0x0, x30

                                 Lnogcs                    XREF[1]:  001f4224(j)
001f422c c0 03 5f d6   ret
```

Information Classification: General

## Slide 37

### Bionic (/ llvm-libunwind) CFI Safe Pivot

Source: Google.

*Right side: photo of a smartphone with a shattered/cracked screen (mountain-range wallpaper visible behind the cracks).*

**Left panel — Ghidra disassembly listing** (same listing as the previous slides), with four red-arrow callouts:
- "Landing Pad" points to the `bti jc` instruction at 001f4190.
- "LR" points to `ldr x30,[x0, #0x100]` (001f41c8).
- "SP" points to both `ldr x16,[x0, #0xf8]` (001f4210) and `mov sp,x16` (001f4218).
- "Return to __kernel_rt_sigreturn" points to the final `ret` at 001f422c.

```text
                                 ****************************************************
                                 *                    FUNCTION                      *
                                 ****************************************************
                                 undefined __libunwind_Registers_arm64_jumpto()
undefined                       <UNASSIGNED>  <RETURN>
                                 __libunwind_Registers_arm64_jumpto   XREF[3]:  __libunwind_shstk_get_jump_targe...
                                                                                 jumpto:001f0910(c), 001ff210(*)
001f4190 df 24 03 d5   bti      jc
001f4194 02 0c 41 a9   ldp      x2,x3,[x0, #0x10]
001f4198 04 14 42 a9   ldp      x4,x5,[x0, #0x20]
001f419c 06 1c 43 a9   ldp      x6,x7,[x0, #0x30]
001f41a0 08 24 44 a9   ldp      x8,x9,[x0, #0x40]
001f41a4 0a 2c 45 a9   ldp      x10,x11,[x0, #0x50]
001f41a8 0c 34 46 a9   ldp      x12,x13,[x0, #0x60]
001f41ac 0e 3c 47 a9   ldp      x14,x15,[x0, #0x70]
001f41b0 12 4c 49 a9   ldp      x18,x19,[x0, #0x90]
001f41b4 14 54 4a a9   ldp      x20,x21,[x0, #0xa0]
001f41b8 16 5c 4b a9   ldp      x22,x23,[x0, #0xb0]
001f41bc 18 64 4c a9   ldp      x24,x25,[x0, #0xc0]
001f41c0 1a 6c 4d a9   ldp      x26,x27,[x0, #0xd0]
001f41c4 1c 74 4e a9   ldp      x28,x29,[x0, #0xe0]
001f41c8 1e 80 40 f9   ldr      x30,[x0, #0x100]
001f41cc 00 04 51 6d   ldp      d0,d1,[x0, #0x110]
001f41d0 02 0c 52 6d   ldp      d2,d3,[x0, #0x120]
001f41d4 04 14 53 6d   ldp      d4,d5,[x0, #0x130]
001f41d8 06 1c 54 6d   ldp      d6,d7,[x0, #0x140]
001f41dc 08 24 55 6d   ldp      d8,d9,[x0, #0x150]
001f41e0 0a 2c 56 6d   ldp      d10,d11,[x0, #0x160]
001f41e4 0c 34 57 6d   ldp      d12,d13,[x0, #0x170]
001f41e8 0e 3c 58 6d   ldp      d14,d15,[x0, #0x180]
001f41ec 10 44 59 6d   ldp      d16,d17,[x0, #0x190]
001f41f0 12 4c 5a 6d   ldp      d18,d19,[x0, #0x1a0]
001f41f4 14 54 5b 6d   ldp      d20,d21,[x0, #0x1b0]
001f41f8 16 5c 5c 6d   ldp      d22,d23,[x0, #0x1c0]
001f41fc 18 64 5d 6d   ldp      d24,d25,[x0, #0x1d0]
001f4200 1a 6c 5e 6d   ldp      d26,d27,[x0, #0x1e0]
001f4204 1c 74 5f 6d   ldp      d28,d29,[x0, #0x1f0]
001f4208 1e 00 41 fd   ldr      d30,[x0, #0x200]
001f420c 1f 04 41 fd   ldr      d31,[x0, #0x208]
001f4210 10 7c 40 f9   ldr      x16,[x0, #0xf8]
001f4214 00 04 40 a9   ldp      x0,x1,[x0]
001f4218 1f 02 00 91   mov      sp,x16
001f421c 30 00 80 d2   mov      x16,#0x1
001f4220 1f 25 03 d5   hint     0x28
001f4224 50 00 00 b5   cbnz     x16,Lnogcs
001f4228 1e 77 0b d5   sys      0x3, 0x7, 0x7, 0x0, x30

                                 Lnogcs                    XREF[1]:  001f4224(j)
001f422c c0 03 5f d6   ret
```

Information Classification: General

## Slide 38

### Infinite SROP/BTI Chaining

*Diagram: a horizontal chain of four labelled boxes connected by arrows (the final arrow is dashed, indicating the chain continues beyond the slide):*

1. `setcontext` / `(CFI Safe Pivot)`
2. → `__kernel_rt_sigreturn` / `(Step #1)`
3. → `JOP Gadget #1`
4. → `__kernel_rt_sigreturn` / `(Step #2)` ┄▶ *(dashed arrow, continues off-slide)*

Information Classification: General

## Slide 39

### Infinite SROP/BTI Chaining

*Diagram: the same four-box chain at the top —* `setcontext (CFI Safe Pivot)` → `__kernel_rt_sigreturn (Step #1)` → `JOP Gadget #1` → `__kernel_rt_sigreturn (Step #2)` ┄▶

*A table is now shown beneath the first box, with a curved arrow from the table up into the "Step #1" box:*

**`ucontext_t pivot_ctx`**
```text
…
pc = __kernel_rt_sigreturn      (in red)
sp = &frame_1
…
```

Information Classification: General

## Slide 40

### Infinite SROP/BTI Chaining

*Diagram: the same four-box chain at the top —* `setcontext (CFI Safe Pivot)` → `__kernel_rt_sigreturn (Step #1)` → `JOP Gadget #1` → `__kernel_rt_sigreturn (Step #2)` ┄▶

*Three tables are now shown beneath it. A curved arrow runs from the `pivot_ctx` table up into the "Step #1" box; a second curved arrow runs from the `frame_1` table up into the "Gadget 1 (mem-store)" table.*

**`ucontext_t pivot_ctx`**
```text
…
pc = __kernel_rt_sigreturn      (in red)
sp = &frame_1
…
```

**`rt_sigframe frame_1`**
```text
…
(blank row)
pc = &gadget_1
sp = &frame_2
pstate = 0
```

***Gadget 1 (mem-store)***
```text
str w2, [x0]
br x16
```

Information Classification: General

## Slide 41

### Infinite SROP/BTI Chaining

*Diagram: the same four-box chain at the top and the same three tables as the previous build step, with two changes highlighted in red:*

- The blank row in the `frame_1` table now reads `x16 = __kernel_rt_sigreturn` (in red).
- The `br x16` line in the "Gadget 1" table is now shown in red.

**`ucontext_t pivot_ctx`**
```text
…
pc = __kernel_rt_sigreturn      (in red)
sp = &frame_1
…
```

**`rt_sigframe frame_1`**
```text
…
x16 = __kernel_rt_sigreturn     (in red)
pc = &gadget_1
sp = &frame_2
pstate = 0
```

***Gadget 1 (mem-store)***
```text
str w2, [x0]
br x16                          (in red)
```

Information Classification: General

## Slide 42

### Infinite SROP/BTI Chaining

*Diagram: same four-box chain at top and the same three tables as the previous slide, plus a fourth table. A curved arrow runs from the `frame_1` table's `sp = &frame_2` row over to the new table.*

**`ucontext_t pivot_ctx`**
```text
…
pc = __kernel_rt_sigreturn      (in red)
sp = &frame_1
…
```

**`rt_sigframe frame_1`**
```text
…
x16 = __kernel_rt_sigreturn     (in red)
pc = &gadget_1
sp = &frame_2
pstate = 0
```

***Gadget 1 (mem-store)***
```text
str w2, [x0]
br x16                          (in red)
```

**`rt_sigframe frame_2`**
```text
…
pc = &gadget_2
sp = &frame_3
pstate = 0
```

Information Classification: General

## Slide 43

### Infinite SROP/BTI Chaining

**Flow:** setcontext (CFI Safe Pivot) → __kernel_rt_sigreturn (Step #1) → JOP Gadget #1 → __kernel_rt_sigreturn (Step #2) --→ *(continues off-slide)*

*ucontext_t pivot_ctx*
- …
- pc = __kernel_rt_sigreturn  *(red)*
- sp = &frame_1
- …

*rt_sigframe frame_1*
- …
- x16 = __kernel_rt_sigreturn  *(red)*
- pc = &gadget_1
- sp = &frame_2
- pstate = 0

*Gadget 1 (mem-store)*
```
str w2, [x0]
br x16
```
(`br x16` shown in red; arrow from this gadget points to an explosion icon 💥)

*rt_sigframe frame_2*
- …
- pc = &gadget_2
- sp = &frame_3  (arrow to explosion icon 💥)
- pstate = 0

## Slide 44

### PoC #1

<u>https://github.com/betab0t/srop-bti</u>

Information Classification: General

## Slide 45

### Turing Completeness

1. Instruction pointer

2. State propagation

3. Operations (load, store, etc’)

Information Classification: General

## Slide 46

### Instruction Pointer

●Instructions encoded as rt_sigframes

- sp points to next instruction

●TM steps with __kernel_rt_sigreturn

Information Classification: General

## Slide 47

### State Propagation

```
((void (*)(int))target)(*(int *)p);
```

**rt_sigframe frame_1**
- …
- sp = &frame_2
- pc = &gadget_1
- x1 = __kernel_rt_sigreturn
  x19 = src ptr
  x20 = offsetof(rt_sigframe, x[7])
  x21 = &frame_2
- …
- pstate = 0

*Gadget #1 (mem-load-store)*
```
ldr x2, [x19, #0x18] // src
str x2, [x21, x20]   // dst
blr x1 // back to __kernel_rt_sigreturn
```

**rt_sigframe frame_2**
- …
- x7
- …
- sp = &frame_3
- pc = &gadget_2
- pstate = 0

## Slide 48

### State Propagation

```
((void (*)(int))target)(*(int *)p);
```

**rt_sigframe frame_2**
- …
- x1 = &target
  x7 = *p
- …
- sp = &frame_3
- pc = &gadget_2
- pstate = 0

*Gadget #1 (mem-load-store)*
```
ldr x2, [x19, #0x18] // src
str x2, [x21, x20]   // dst
blr x1 // back to __kernel_rt_sigreturn
```

*Gadget #2 (func-call)*
```
mov x0, x7
blr x1 // target
```

## Slide 49

### State Propagation

```
((void (*)(int))target)(*(int *)p);
```
*(a green checkmark ✅ is shown next to this line)*

**rt_sigframe frame_2**
- …
- x1 = &target
  x7 = *p
- …
- sp = &frame_3
- pc = &gadget_2
- pstate = 0

*Gadget #1 (mem-load-store)*
```
ldr x2, [x19, #0x18] // src
str x2, [x21, x20]   // dst
blr x1 // back to __kernel_rt_sigreturn
```

*Gadget #2 (func-call)*
```
mov x0, x7
blr x1 // target
```

## Slide 50

### Operations

●mem-load/store

●Arithmetics

●Goto

○Loops

●Conditional branching

Information Classification: General

## Slide 51

### Arithmetics

1. Load

2. Calculate

3. Store

4. Sigreturn

Information Classification: General

## Slide 52

### Arithmetics

1. Load
2. Calculate
3. Store
4. Sigreturn

**_SROP/BTI Gadget (madd)_**

*ROP Gadget (madd-gadget-1)*
```
madd x0, x10, x8, x9 // x0 = (x10 * x8) + x9
ret // return to gadget #2
```
↓
*JOP Gadget (madd-gadget-2)*
```
str w0, [x21, #0x10]
mov x0, x19
blr x20 // back to __kernel_rt_sigreturn
```

## Slide 53

<u>https://developer.arm.com/documentation/102433/0200/Return-oriented-programming</u>

*(screenshot of the Arm Developer documentation site, cropped at the right edge)*

```text
arm Developer Develop Blogs Community CPU & Hardware Support

Pointer authentication

Armv8.3-A introduces the option of pointer authentication, FEAT_PAC. Pointer authentication can mitigate against ROP attacks.

Pointer authentication takes advantage of the fact that pointers are stored in a 64-bit format, but not all those bits are needed to represent the addr[ess...]
virtual address space layout:
```

## Slide 54

Ubuntu GLIBC 2.43

*(red label)* -fschedule-insns2

A red arrow labeled **pac** points to the `paciasp` line. A red arrow labeled **aut** points to the `autiasp` line.

```
__drand48_iterate:
0043afc0  paciasp
0043afc4  stp     fp, lr, [sp, #-0x10]!  {__saved_fp} {__saved_lr}
0043afc8  mov     fp, sp {__saved_fp}
0043afcc  ldrh    w2, [x1, #0xe]
0043afd0  cbz     w2, 0x43b014

0043b014  mov     x3, #0xe66d
0043b018  mov     w2, #0xb
0043b01c  movk    x3, #0xdeec, lsl #0x10
0043b020  movk    w2, #0x1, lsl #0x10  {0x1000b}
0043b024  movk    x3, #0x5, lsl #0x20  {0x5deece66d}
0043b028  mov     x4, #0xb
0043b02c  str     w2, [x1, #0xc]  {0x1000b}
0043b030  str     x3, [x1, #0x10]  {0x5deece66d}
0043b034  b       0x43afdc

0043afd4  ldr     x3, [x1, #0x10]
0043afd8  ldrh    w4, [x1, #0xc]

0043afdc  ldrh    w2, [x0]
0043afe0  ldrh    w1, [x0, #0x4]
0043afe4  ldp     fp, lr, [sp], #0x10  {__saved_fp} {__saved_lr}
0043afe8  autiasp
0043afec  orr     x1, x2, x1, lsl #0x20
0043aff0  ldrh    w2, [x0, #0x2]
0043aff4  lsl     w2, w2, #0x10
0043aff8  orr     x1, x1, x2
0043affc  madd    x1, x1, x3, x4
0043b000  str     w1, [x0]
0043b004  lsr     x1, x1, #0x20
0043b008  strh    w1, [x0, #0x4]
0043b00c  mov     w0, #0
0043b010  ret
```

## Slide 55

Ubuntu GLIBC 2.43

*(red label)* -fschedule-insns2

A red arrow labeled **pac** points to the `paciasp` line. A red arrow labeled **aut** points to the `autiasp` line. A red box labeled **gadget** outlines the six instructions from `madd` through `ret` at the end of the listing.

```
__drand48_iterate:
0043afc0  paciasp
0043afc4  stp     fp, lr, [sp, #-0x10]!  {__saved_fp} {__saved_lr}
0043afc8  mov     fp, sp {__saved_fp}
0043afcc  ldrh    w2, [x1, #0xe]
0043afd0  cbz     w2, 0x43b014

0043b014  mov     x3, #0xe66d
0043b018  mov     w2, #0xb
0043b01c  movk    x3, #0xdeec, lsl #0x10
0043b020  movk    w2, #0x1, lsl #0x10  {0x1000b}
0043b024  movk    x3, #0x5, lsl #0x20  {0x5deece66d}
0043b028  mov     x4, #0xb
0043b02c  str     w2, [x1, #0xc]  {0x1000b}
0043b030  str     x3, [x1, #0x10]  {0x5deece66d}
0043b034  b       0x43afdc

0043afd4  ldr     x3, [x1, #0x10]
0043afd8  ldrh    w4, [x1, #0xc]

0043afdc  ldrh    w2, [x0]
0043afe0  ldrh    w1, [x0, #0x4]
0043afe4  ldp     fp, lr, [sp], #0x10  {__saved_fp} {__saved_lr}
0043afe8  autiasp
0043afec  orr     x1, x2, x1, lsl #0x20
0043aff0  ldrh    w2, [x0, #0x2]
0043aff4  lsl     w2, w2, #0x10
0043aff8  orr     x1, x1, x2
0043affc  madd    x1, x1, x3, x4
0043b000  str     w1, [x0]
0043b004  lsr     x1, x1, #0x20
0043b008  strh    w1, [x0, #0x4]
0043b00c  mov     w0, #0
0043b010  ret
```

## Slide 56

Ubuntu GLIBC 2.43

*(red labels)* -fschedule-insns2
pac-ret[+leaf]

A red arrow labeled **pac** points to the `paciasp` line. A red arrow labeled **aut** points to the `autiasp` line. A red box labeled **gadget** outlines the six instructions from `madd` through `ret` at the end of the listing.

```
__drand48_iterate:
0043afc0  paciasp
0043afc4  stp     fp, lr, [sp, #-0x10]!  {__saved_fp} {__saved_lr}
0043afc8  mov     fp, sp {__saved_fp}
0043afcc  ldrh    w2, [x1, #0xe]
0043afd0  cbz     w2, 0x43b014

0043b014  mov     x3, #0xe66d
0043b018  mov     w2, #0xb
0043b01c  movk    x3, #0xdeec, lsl #0x10
0043b020  movk    w2, #0x1, lsl #0x10  {0x1000b}
0043b024  movk    x3, #0x5, lsl #0x20  {0x5deece66d}
0043b028  mov     x4, #0xb
0043b02c  str     w2, [x1, #0xc]  {0x1000b}
0043b030  str     x3, [x1, #0x10]  {0x5deece66d}
0043b034  b       0x43afdc

0043afd4  ldr     x3, [x1, #0x10]
0043afd8  ldrh    w4, [x1, #0xc]

0043afdc  ldrh    w2, [x0]
0043afe0  ldrh    w1, [x0, #0x4]
0043afe4  ldp     fp, lr, [sp], #0x10  {__saved_fp} {__saved_lr}
0043afe8  autiasp
0043afec  orr     x1, x2, x1, lsl #0x20
0043aff0  ldrh    w2, [x0, #0x2]
0043aff4  lsl     w2, w2, #0x10
0043aff8  orr     x1, x1, x2
0043affc  madd    x1, x1, x3, x4
0043b000  str     w1, [x0]
0043b004  lsr     x1, x1, #0x20
0043b008  strh    w1, [x0, #0x4]
0043b00c  mov     w0, #0
0043b010  ret
```

## Slide 57

### Conditional Branching

●If x Then sp = cond_true Else sp = cond_false

Information Classification: General

## Slide 58

### Conditional Branching

●If x Then sp = cond_true Else sp = cond_false

● sp =

= cond_true + (ind(x) * sizeof(rt_sigframe))

| rt_sigframe frame_branch |
| --- |
| sp = ? |
| pc = __kernel_rt_sigreturn |
| pstate = 0 |
| rt_sigframe cond_true |
| rt_sigframe cond_false |

Information Classification: General

## Slide 59

### Conditional Branching

●If x Then sp = cond_true Else sp = cond_false

● sp =

= cond_true + (ind(x) * sizeof(rt_sigframe))

| rt_sigframe frame_branch |
| --- |
| sp = ? |
| pc = __kernel_rt_sigreturn |
| pstate = 0 |
| rt_sigframe cond_true |
| rt_sigframe cond_false |

```asm
// ind(x)
ldr w1, [x2]
cmp w1, #0
cset x1, ne
str x1, [sp, #0x10]
// …
blr x0
```

Information Classification: General

## Slide 60

### PoC #2

<u>https://github.com/betab0t/srop-bti</u>

Information Classification: General

## Slide 61

*Screenshot of an email reply from Linus Torvalds, with one paragraph enlarged as a highlighted callout.*

**Linus Torvalds**
To: me, and 2 others, Cc: security@kernel.org, and 3 oth… · Mon, Jan 26 at 8:03 PM

I have forwarded the original email to the arm64 maintainers, also cc'd here.

But:

On Mon, 26 Jan 2026 at 09:37, beta bot <beta_b0t@yahoo.com> wrote:

**Highlighted callout:**

> So this seems to not be a very effective attack vector and is not practically fixable, because signals by \*design\* have to be able to return anywhere.

Quoted reply:

> This would seem to require that you be able to change the signal return stack in a very particular way, so you probably already had pretty complete control of the program you're attacking.
>
> So this seems to not be a very effective attack vector and is not practically fixable, because signals by \*design\* have to be able to return anywhere.
>
> I suspect this can be discussed publicly, and the signal return path has - as you point out - already been discussed in various other contexts, but I think this is just how signals work.
>
> BTI isn't some kind of absolute shield. It's just one layer of security protection among many others.

Information Classification: General

## Slide 62

### OpenBSD

*GitHub screenshot — openbsd / src*

**Code** · Security and quality · Insights

**Commit `7730d1d`**

deraadt committed on May 10, 2016

```text
SROP mitigation.  sendsig() stores a (per-process ^ &sigcontext) cookie
inside the sigcontext.  sigreturn(2) checks syscall entry was from the
exact PC addr in the (per-process ASLR) sigtramp, verifies the cookie,
and clears it to prevent sigcontext reuse.
not yet tested on landisk, sparc, *88k, socppc.
ok kettenis
```

master

40 files changed

Information Classification: General

## Slide 63

### OpenBSD

*GitHub screenshot — openbsd / src (pink arrow highlights the commit date)*

**Code** · Security and quality · Insights

**Commit `7730d1d`**

deraadt committed on May 10, 2016

```text
SROP mitigation.  sendsig() stores a (per-process ^ &sigcontext) cookie
inside the sigcontext.  sigreturn(2) checks syscall entry was from the
exact PC addr in the (per-process ASLR) sigtramp, verifies the cookie,
and clears it to prevent sigcontext reuse.
not yet tested on landisk, sparc, *88k, socppc.
ok kettenis
```

master

40 files changed

Information Classification: General

## Slide 64

### XNU

```c
    if (ts64->pc) {
        uint64_t discriminator = ptrauth_string_discriminator("pc");
        if (!kernel_signed_pc && userland_diversifier != 0) {
            discriminator = ptrauth_blend_discriminator(userland_diversifier,
                ptrauth_string_discriminator("pc"));
        }
        ts64->pc = (uintptr_t)pmap_auth_user_ptr((void*)ts64->pc,
            ptrauth_key_process_independent_code, discriminator,
            thread->machine.jop_pid);
    }
    if (ts64->lr && !(ts64->flags & __DARWIN_ARM_THREAD_STATE64_FLAGS_IB_SIGNED_LR)) {
        uint64_t discriminator = ptrauth_string_discriminator("lr");
        if (!kernel_signed_lr && userland_diversifier != 0) {
            discriminator = ptrauth_blend_discriminator(userland_diversifier,
                ptrauth_string_discriminator("lr"));
        }
        ts64->lr = (uintptr_t)pmap_auth_user_ptr((void*)ts64->lr,
            ptrauth_key_process_independent_code, discriminator,
            thread->machine.jop_pid);
    }
    if (ts64->sp) {
        ts64->sp = (uintptr_t)pmap_auth_user_ptr((void*)ts64->sp,
            ptrauth_key_process_independent_data, ptrauth_string_discriminator("sp"),
            thread->machine.jop_pid);
    }
    if (ts64->fp) {
        ts64->fp = (uintptr_t)pmap_auth_user_ptr((void*)ts64->fp,
            ptrauth_key_process_independent_data, ptrauth_string_discriminator("fp"),
            thread->machine.jop_pid);
    }
```

*GitHub screenshot — apple-oss-distributions / xnu*

**Code** · Security and quality · Insights

**Commit `a5e7219`**

AppleOSSDistributions committed on Oct 6, 2021

```text
xnu-6153.11.26
Imported from xnu-6153.11.26.tar.gz
```

main · xnu-12377.121.6 ⋯ xnu-6153.11.26

3,016 files changed

<u>https://github.com/apple-oss-distributions/xnu/blob/main/osfmk/arm64/status.c#L1060</u>

Information Classification: General

## Slide 65

### XNU

```c
    if (ts64->pc) {
        uint64_t discriminator = ptrauth_string_discriminator("pc");
        if (!kernel_signed_pc && userland_diversifier != 0) {
            discriminator = ptrauth_blend_discriminator(userland_diversifier,
                ptrauth_string_discriminator("pc"));
        }
        ts64->pc = (uintptr_t)pmap_auth_user_ptr((void*)ts64->pc,
            ptrauth_key_process_independent_code, discriminator,
            thread->machine.jop_pid);
    }
    if (ts64->lr && !(ts64->flags & __DARWIN_ARM_THREAD_STATE64_FLAGS_IB_SIGNED_LR)) {
        uint64_t discriminator = ptrauth_string_discriminator("lr");
        if (!kernel_signed_lr && userland_diversifier != 0) {
            discriminator = ptrauth_blend_discriminator(userland_diversifier,
                ptrauth_string_discriminator("lr"));
        }
        ts64->lr = (uintptr_t)pmap_auth_user_ptr((void*)ts64->lr,
            ptrauth_key_process_independent_code, discriminator,
            thread->machine.jop_pid);
    }
    if (ts64->sp) {
        ts64->sp = (uintptr_t)pmap_auth_user_ptr((void*)ts64->sp,
            ptrauth_key_process_independent_data, ptrauth_string_discriminator("sp"),
            thread->machine.jop_pid);
    }
    if (ts64->fp) {
        ts64->fp = (uintptr_t)pmap_auth_user_ptr((void*)ts64->fp,
            ptrauth_key_process_independent_data, ptrauth_string_discriminator("fp"),
            thread->machine.jop_pid);
    }
```

*(pink arrow highlights the commit date)*

*GitHub screenshot — apple-oss-distributions / xnu*

**Code** · Security and quality · Insights

**Commit `a5e7219`**

AppleOSSDistributions committed on Oct 6, 2021

```text
xnu-6153.11.26
Imported from xnu-6153.11.26.tar.gz
```

main · xnu-12377.121.6 ⋯ xnu-6153.11.26

3,016 files changed

<u>https://github.com/apple-oss-distributions/xnu/blob/main/osfmk/arm64/status.c#L1060</u>

Information Classification: General

## Slide 66

### XNU

```c
    if (ts64->pc) {
        uint64_t discriminator = ptrauth_string_discriminator("pc");
        if (!kernel_signed_pc && userland_diversifier != 0) {
            discriminator = ptrauth_blend_discriminator(userland_diversifier,
                ptrauth_string_discriminator("pc"));
        }
        ts64->pc = (uintptr_t)pmap_auth_user_ptr((void*)ts64->pc,
            ptrauth_key_process_independent_code, discriminator,
            thread->machine.jop_pid);
    }
    if (ts64->lr && !(ts64->flags & __DARWIN_ARM_THREAD_STATE64_FLAGS_IB_SIGNED_LR)) {
        uint64_t discriminator = ptrauth_string_discriminator("lr");
        if (!kernel_signed_lr && userland_diversifier != 0) {
            discriminator = ptrauth_blend_discriminator(userland_diversifier,
                ptrauth_string_discriminator("lr"));
        }
        ts64->lr = (uintptr_t)pmap_auth_user_ptr((void*)ts64->lr,
            ptrauth_key_process_independent_code, discriminator,
            thread->machine.jop_pid);
    }
    if (ts64->sp) {
        ts64->sp = (uintptr_t)pmap_auth_user_ptr((void*)ts64->sp,
            ptrauth_key_process_independent_data, ptrauth_string_discriminator("sp"),
            thread->machine.jop_pid);
    }
    if (ts64->fp) {
        ts64->fp = (uintptr_t)pmap_auth_user_ptr((void*)ts64->fp,
            ptrauth_key_process_independent_data, ptrauth_string_discriminator("fp"),
            thread->machine.jop_pid);
    }
```

*(pink box highlights the `ts64->pc = ... pmap_auth_user_ptr(...)` block; pink arrow highlights the commit date)*

*GitHub screenshot — apple-oss-distributions / xnu*

**Code** · Security and quality · Insights

**Commit `a5e7219`**

AppleOSSDistributions committed on Oct 6, 2021

```text
xnu-6153.11.26
Imported from xnu-6153.11.26.tar.gz
```

main · xnu-12377.121.6 ⋯ xnu-6153.11.26

3,016 files changed

<u>https://github.com/apple-oss-distributions/xnu/blob/main/osfmk/arm64/status.c#L1060</u>

Information Classification: General

## Slide 67

### XNU

```c
    if (ts64->pc) {
        uint64_t discriminator = ptrauth_string_discriminator("pc");
        if (!kernel_signed_pc && userland_diversifier != 0) {
            discriminator = ptrauth_blend_discriminator(userland_diversifier,
                ptrauth_string_discriminator("pc"));
        }
        ts64->pc = (uintptr_t)pmap_auth_user_ptr((void*)ts64->pc,
            ptrauth_key_process_independent_code, discriminator,
            thread->machine.jop_pid);
    }
    if (ts64->lr && !(ts64->flags & __DARWIN_ARM_THREAD_STATE64_FLAGS_IB_SIGNED_LR)) {
        uint64_t discriminator = ptrauth_string_discriminator("lr");
        if (!kernel_signed_lr && userland_diversifier != 0) {
            discriminator = ptrauth_blend_discriminator(userland_diversifier,
                ptrauth_string_discriminator("lr"));
        }
        ts64->lr = (uintptr_t)pmap_auth_user_ptr((void*)ts64->lr,
            ptrauth_key_process_independent_code, discriminator,
            thread->machine.jop_pid);
    }
    if (ts64->sp) {
        ts64->sp = (uintptr_t)pmap_auth_user_ptr((void*)ts64->sp,
            ptrauth_key_process_independent_data, ptrauth_string_discriminator("sp"),
            thread->machine.jop_pid);
    }
    if (ts64->fp) {
        ts64->fp = (uintptr_t)pmap_auth_user_ptr((void*)ts64->fp,
            ptrauth_key_process_independent_data, ptrauth_string_discriminator("fp"),
            thread->machine.jop_pid);
    }
```

*(pink box highlights the `ts64->pc = ... pmap_auth_user_ptr(...)` block; pink arrow highlights the commit date)*

*GitHub screenshot — apple-oss-distributions / xnu*

**Code** · Security and quality · Insights

**Commit `a5e7219`**

AppleOSSDistributions committed on Oct 6, 2021

```text
xnu-6153.11.26
Imported from xnu-6153.11.26.tar.gz
```

main · xnu-12377.121.6 ⋯ xnu-6153.11.26

3,016 files changed

**✅ PRACTICALLY FIXABLE**

<u>https://github.com/apple-oss-distributions/xnu/blob/main/osfmk/arm64/status.c#L1060</u>

Information Classification: General

## Slide 68

Omri Ben-Bassat “beta_b0t”
<u>beta_b0t@yahoo.com</u>
<u>https://www.linkedin.com/in/omri-ben-bassat</u>

### Thank You

**← Schedule**

**Breaking Hardware CFI with Sigreturn**
`DEF CON Official Talk` · `Demo`

**Sessions**
Fri, Aug 7 at 17:30 – 18:00 PDT
LVCC - L1 - Exhibit Hall West 3 - 1007 (Main Track 2)

<u>https://hackertracker.app/defcon34/content/66610</u>

Information Classification: General

