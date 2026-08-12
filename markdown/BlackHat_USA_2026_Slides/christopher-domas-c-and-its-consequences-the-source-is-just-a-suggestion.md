---
title: "C and Its Consequences The Source Is Just a Suggestion"
speakers: ["Christopher Domas"]
conference: "Black Hat"
conference_full: "Black Hat USA 2026"
edition: "USA"
year: 2026
source_pdf: "BlackHat_USA_2026_Slides/Christopher Domas_C and Its Consequences The Source Is Just a Suggestion.pdf"
pages: 156
sha256: "4301ca6a96fe62effba492b5b1f3643d28fc1fa10d0830250c3bbb762a752d14"
text_chars: 45500
ocr_pages: 0
has_ocr: false
redacted_secrets: 0
ocr_confidence: null
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: ["Christopher Domas_C and Its Consequences The Source Is Just a Suggestion_tools.txt"]
extractor: "pymupdf4llm 1.28.2"
converted_at: "2026-08-12T05:31:02Z"
---
# C and Its Consequences The Source Is Just a Suggestion

**Speakers:** Christopher Domas  
**Conference:** Black Hat USA 2026  
**Source:** `BlackHat_USA_2026_Slides/Christopher Domas_C and Its Consequences The Source Is Just a Suggestion.pdf` (156 pages)


## Slide 1

`C and its Consequences domas / @xoreaxeaxeax / Black Hat 2026` ｛

## Slide 2

\```
find the vulnerability.
\```

## Slide 3

\```
typedef struct {
unsigned int length;
uint8_t data[];
} packet_t;
\```

\```
uint8_t buffer[MAX_SIZE];
\```

\```
/* kernel handler */
int receive(packet_t* pkt /* userspace data */)
{
if (pkt->length > MAX_SIZE) {
return -1;
    }
memcpy(buffer, pkt->data, pkt->length);
return 0;
}
\```

## Slide 4

\```
TOCTOU
\```

## Slide 5

\```
typedef struct {
unsigned int length;
uint8_t data[];
} packet_t;
\```

\```
uint8_t buffer[MAX_SIZE];
\```

\```
/* kernel handler */
int receive(packet_t* pkt /* userspace data */)
{
if (pkt->length > MAX_SIZE) {
return -1;
    }
memcpy(buffer, pkt->data, pkt->length);
return 0;
}
\```

## Slide 6

\```
typedef struct {
unsigned int length;
uint8_t data[];
} packet_t;
uint8_t buffer[MAX_SIZE];
\```

\```
/* kernel handler */
int receive(packet_t* pkt /* userspace data */)
{
if (pkt->length > MAX_SIZE) {
return -1;
    }
memcpy(buffer, pkt->data, pkt->length);
return 0;
}
\```

## Slide 7

\```
typedef struct {
unsigned int length;
uint8_t data[];
} packet_t;
uint8_t buffer[MAX_SIZE];
\```

\```
/* kernel handler */
int receive(packet_t* pkt /* userspace data */)
{
if (pkt->length > MAX_SIZE) {
return -1;
    }
memcpy(buffer, pkt->data, pkt->length);
return 0;
}
\```

## Slide 8

\```
typedef struct {
unsigned int length;
uint8_t data[];
} packet_t;
uint8_t buffer[MAX_SIZE];
\```

\```
/* kernel handler */
int receive(packet_t* pkt /* userspace data */)
{
if (pkt->length > MAX_SIZE) {
return -1;
    }
memcpy(buffer, pkt->data, pkt->length);
return 0;
}
\```

## Slide 9

\```
typedef struct {
unsigned int length;
uint8_t data[];
} packet_t;
uint8_t buffer[MAX_SIZE];
/* kernel handler */
int receive(packet_t* pkt /* userspace data */)
{
if (pkt->length > MAX_SIZE) {
return -1;
    }
memcpy(buffer, pkt->data, pkt->length);
return 0;
}
\```

## Slide 10

\```
let’s fix it.
\```

## Slide 11

\```
let’s fix it.
find the vulnerability.
\```

## Slide 12

\```
typedefstruct {
unsignedint length;
uint8_t data[];
} packet_t;
\```

\```
uint8_t buffer[MAX_SIZE];
\```

\```
/* kernel handler */
intreceive(packet_t* pkt /* userspace data */)
{
\```

\```
/* copy size locally to prevent TOCTOU */
unsignedint local_length = pkt->length;
\```

\```
if (local_length > MAX_SIZE) {
return -1;
    }
memcpy(buffer, pkt->data, local_length);
return0;
}
\```

## Slide 13

\```
typedefstruct {
unsignedint length;
uint8_t data[];
} packet_t;
uint8_t buffer[MAX_SIZE];
\```

\```
/* kernel handler */
intreceive(packet_t* pkt /* userspace data */)
{
/* copy size locally to prevent TOCTOU */
unsignedint local_length = pkt->length;
if (local_length > MAX_SIZE) {
return -1;
    }
memcpy(buffer, pkt->data, local_length);
return0;
}
\```

## Slide 14

\```
typedefstruct {
unsignedint length;
uint8_t data[];
} packet_t;
uint8_t buffer[MAX_SIZE];
\```

\```
/* kernel handler */
intreceive(packet_t* pkt /* userspace data */)
{
/* copy size locally to prevent TOCTOU */
unsignedint local_length = pkt->length;
if (local_length > MAX_SIZE) {
return -1;
    }
memcpy(buffer, pkt->data, local_length);
return0;
}
\```

## Slide 15

\```
typedefstruct {
unsignedint length;
uint8_t data[];
} packet_t;
uint8_t buffer[MAX_SIZE];
\```

\```
/* kernel handler */
intreceive(packet_t* pkt /* userspace data */)
{
/* copy size locally to prevent TOCTOU */
unsignedint local_length = pkt->length;
if (local_length > MAX_SIZE) {
return -1;
    }
memcpy(buffer, pkt->data, local_length);
return0;
}
\```

## Slide 16

\```
typedefstruct {
unsignedint length;
uint8_t data[];
} packet_t;
uint8_t buffer[MAX_SIZE];
\```

\```
/* kernel handler */
intreceive(packet_t* pkt /* userspace data */)
{
/* copy size locally to prevent TOCTOU */
unsignedint local_length = pkt->length;
\```

\```
if (local_length > MAX_SIZE) {
return -1;
    }
memcpy(buffer, pkt->data, local_length);
return0;
}
\```

## Slide 17

\```
typedefstruct {
unsignedint length;
uint8_t data[];
} packet_t;
uint8_t buffer[MAX_SIZE];
\```

\```
/* kernel handler */
intreceive(packet_t* pkt /* userspace data */)
{
\```

\```
/* copy size locally to prevent TOCTOU */
unsignedint local_length = pkt->length;
\```

\```
if (local_length > MAX_SIZE) {
return -1;
    }
memcpy(buffer, pkt->data, local_length);
return0;
}
\```

## Slide 18

\```
no control over local = no attack window
\```

\```
TOCTOU
\```

## Slide 19

\```
no control over local = no attack window
TOCTOU is impossible.
\```

\```
TOCTOU
\```

## Slide 20

## Slide 21

\```
“
\```

\```
... we’ve had compiler writers that say
\```

\```
‘if you read the specs, that’s ok’.
\```

\```
No, it’s not ok.
\```

\```
Because reality trumps any weasel-spec-reading.
”
\```

\```
— Linus Torvalds · lkml · 2019-08-16
\```

## Slide 22

\```
C specifications
\```

## Slide 23

⊷ `C ISO standard – ~700 pages of rules`

- ⊷ `The _` _`abstract machine`_ `_`

   - ⊸ `A theoretical machine`

   - ⊸ `What you’re really programming in C`

- ⊷ `Observable results`

   - ⊸ `Output, file writes, external calls`

   - ⊸ `Everything else is unwitnessed`

- ⊷ `The _` _`as-if`_ `_ rule`

   - ⊸ `Program on real machine must reproduce observable behavior`

   - ⊸ `_` _`as-if`_ `_ it had run on the abstract machine`

   - ⊸ `Nothing else has to match`

\```
C specifications
\```

## Slide 24

⊷ `Compiler follows the _` _`as-if`_ `_ rule`

- ⊸ `Owes only the visible _` _`result`_ `_`

- ⊸ `The _` _`what`_ `_ not the _` _`how`_ `_`

- ⊸ `Doesn’t have to follow` _`_your_`_ `“how”`

- ⊸ `Unobservable can be reordered, merged, deleted`

\```
C specifications
\```

## Slide 25

- ⊷ `But what about our TOCTOU?` ⊷ `We removed the dangerous reload`

- ⊷ `Can the compiler undo this?`

- ⊷ `Reintroduce the dangerous load?`

- ⊷ `Check specification`

- ⊷ `Spec says ... nothing.`

- ⊷ `Loads aren't observable behavior`

- ⊷ `Read once, twice, never — spec's indifferent`

- ⊷ `If the spec is silent – compiler can do anything`

- ⊷ `Only the final result is owed`

\```
C specifications
\```

## Slide 26

⊷ `_` _`invented load`_ `_: extra reads, unrequested` ⊷ `Nothing in C forbids them`

⊷ `Could it _actually_ cause an "impossible" TOCTOU?`

\```
C specifications
\```

## Slide 27

`typedef struct { unsigned int length; uint8_t data[]; } packet_t; uint8_t buffer[MAX_SIZE]; /* kernel handler */ int receive(packet_t* pkt /* userspace data */) { /* copy size locally to prevent TOCTOU */ unsigned int local_length = pkt->length; if (local_length > MAX_SIZE) { return -1; } memcpy(buffer, pkt->data, local_length); return 0; }` pkt->length

## Slide 28

- ⊷ `Local copy would be in register.`

- ⊷ `Replace two register reads with two memory reads.`

- ⊷ `This would make code _slower_.`

- ⊷ `An _optimizing_ compiler would never do this.`

\```
C specifications
\```

## Slide 29

## Slide 30

\```
“
\```

\```
...
\```

\```
if gcc did that, much of the kernel would go down in flames.
”
\```

\```
— Paul E. McKenney · lkml · 2009-04-16
\```

## Slide 31

\```
proof-of-concept
\```

## Slide 32

- ⊷ `Idea seems nonsensical`

- ⊷ `Source: read once, stash it in a register`

- ⊷ `Re-reading memory is slower`

- ⊷ `No reason to ever drop the local copy`

- ⊷ `Compiler would never do this ...`

# `proof-of-concept`

## Slide 33

⊷ _`...unless it runs out of registers`_

⊷ `If every GPR is in use by compiler`

⊷ `Compiler would need to _` _`spill`_ `_ to the stack`

- ⊷ `Spilling costs a store and a load`

- ⊷ `Cheaper to just re-read the original`

⊷ `The invented load is the optimization`

# `proof-of-concept`

## Slide 34

⊷ `Can we make it happen on purpose?` ⊷ `GCC 14.1`

⊷ `Manufacture register pressure` ⊷ `See if load reappears`

# `proof-of-concept`

## Slide 35

\```
; gcc 14 –O0
\```

\```
int x, y, z;
voidf(void) {
    int t = x;
    y = t;
    z = t;
}
\```

\```
moveax, DWORDPTR x[rip]
movDWORDPTR [rbp-4], eax
\```

\```
moveax, DWORDPTR [rbp-4]
movDWORDPTR y[rip], eax
moveax, DWORDPTR [rbp-4]
movDWORDPTR z[rip], eax
\```

## Slide 36

\```
; gcc 14 –O0
\```

\```
int x, y, z;
voidf(void) {
    int t = x;
    y = t;
    z = t;
}
\```

\```
moveax, DWORDPTR x[rip]
movDWORDPTR [rbp-4], eax
moveax, DWORDPTR [rbp-4]
movDWORDPTR y[rip], eax
moveax, DWORDPTR [rbp-4]
movDWORDPTR z[rip], eax
\```

## Slide 37

\```
; gcc 14 –O0
\```

\```
int x, y, z;
\```

\```
voidf(void) {
    int t = x;
    y = t;
    z = t;
}
\```

\```
moveax, DWORDPTR x[rip]
movDWORDPTR [rbp-4], eax
\```

\```
moveax, DWORDPTR [rbp-4]
movDWORDPTR y[rip], eax
moveax, DWORDPTR [rbp-4]
movDWORDPTR z[rip], eax
\```

## Slide 38

\```
int x, y, z;; gcc 14 –O1
voidf(void) {moveax, DWORDPTR x[rip]
    int t = x;
    y = t;movDWORDPTR y[rip], eax
    z = t;
}movDWORDPTR z[rip], eax
\```

## Slide 39

\```
int x, y, z;
voidf(void) {
    int t = x;
    y = t;
    z = t;
}
\```

\```
; gcc 14 –O1
moveax, DWORDPTR x[rip]
movDWORDPTR y[rip], eax
movDWORDPTR z[rip], eax
\```

## Slide 40

\```
int x, y, z;
voidf(void) {
    int t = x;
    y = t;
    z = t;
}
\```

\```
; gcc 14 –O1
moveax, DWORDPTR x[rip]
movDWORDPTR y[rip], eax
movDWORDPTR z[rip], eax
\```

## Slide 41

#### `#define CLOBBER \`

\```
    ""
int x, y, z;
voidf(void) {
int t = x;
asmvolatile("" : : : CLOBBER);
    y = t;
asmvolatile("" : : : CLOBBER);
    z = t;
}
\```

\```
; gcc 14 –O1
\```

\```
moveax, DWORDPTR x[rip]
movDWORDPTR y[rip], eax
movDWORDPTR z[rip], eax
\```

## Slide 42

\```
#defineCLOBBER \
    ""
int x, y, z;
voidf(void) {
int t = x;
asmvolatile("" : : : CLOBBER);
    y = t;
asmvolatile("" : : : CLOBBER);
    z = t;
}
\```

\```
; gcc 14 –O1
moveax, DWORDPTR x[rip]
movDWORDPTR y[rip], eax
movDWORDPTR z[rip], eax
\```

## Slide 43

\```
#defineCLOBBER \
    ""
int x, y, z;
voidf(void) {
int t = x;
asmvolatile("" : : : CLOBBER);
    y = t;
asmvolatile("" : : : CLOBBER);
    z = t;
}
\```

\```
; gcc 14 –O1
moveax, DWORDPTR x[rip]
movDWORDPTR y[rip], eax
movDWORDPTR z[rip], eax
\```

## Slide 44

⊷ `Doesn’t have to be inline asm`

⊷ `Code, variables, calls, etc.`

- ⊷ `Anything using registers will cause pressure`

# `proof-of-concept`

## Slide 45

\```
#defineCLOBBER \
    ""
int x, y, z;
voidf(void) {
int t = x;
asmvolatile("" : : : CLOBBER);
    y = t;
asmvolatile("" : : : CLOBBER);
    z = t;
}
\```

\```
; gcc 14 –O1
moveax, DWORDPTR x[rip]
movDWORDPTR y[rip], eax
movDWORDPTR z[rip], eax
\```

## Slide 46

\```
#defineCLOBBER \
    "rax"
int x, y, z;
voidf(void) {
int t = x;
asmvolatile("" : : : CLOBBER);
    y = t;
asmvolatile("" : : : CLOBBER);
    z = t;
}
\```

\```
; gcc 14 –O1
movedx, DWORDPTR x[rip]
movDWORDPTR y[rip], edx
movDWORDPTR z[rip], edx
\```

## Slide 47

\```
#defineCLOBBER \
    "rax","rdx"
int x, y, z;
voidf(void) {
int t = x;
asmvolatile("" : : : CLOBBER);
    y = t;
asmvolatile("" : : : CLOBBER);
    z = t;
}
\```

\```
; gcc 14 –O1
movecx, DWORDPTR x[rip]
movDWORDPTR y[rip], ecx
movDWORDPTR z[rip], ecx
\```

## Slide 48

#### `#define CLOBBER \`

\```
    "rax","rdx","rcx"
\```

\```
; gcc 14 –O1
\```

\```
int x, y, z;
voidf(void) {
int t = x;
asmvolatile("" : : : CLOBBER);
    y = t;
asmvolatile("" : : : CLOBBER);
    z = t;
}
\```

\```
movesi, DWORDPTR x[rip]
movDWORDPTR y[rip], esi
movDWORDPTR z[rip], esi
\```

## Slide 49

\```
#defineCLOBBER \
\```

\```
    "rax","rdx","rcx","rbx","rsi", \
    "rdi","rbp","r8","r9","r10",   \
    "r11","r12","r13","r14”
\```

\```
; gcc 14 –O1
\```

\```
int x, y, z;movr15d, DWORDPTR x[rip]
voidf(void) {movDWORDPTR y[rip], r15d
int t = x;
asmvolatile("" : : : CLOBBER);movDWORDPTR z[rip], r15d
    y = t;
asmvolatile("" : : : CLOBBER);
    z = t;
}
\```

## Slide 50

#### `#define CLOBBER \`

\```
    "rax","rdx","rcx","rbx","rsi", \
    "rdi","rbp","r8","r9","r10",   \
    "r11","r12","r13","r14","r15"
\```

\```
int x, y, z;
\```

\```
voidf(void) {
int t = x;
asmvolatile("" : : : CLOBBER);
    y = t;
asmvolatile("" : : : CLOBBER);
    z = t;
}
\```

\```
; gcc 14 –O1
\```

\```
moveax, DWORDPTR x[rip]
movDWORDPTR y[rip], eax
moveax, DWORDPTR x[rip]
movDWORDPTR z[rip], eax
\```

## Slide 51

\```
#defineCLOBBER \
    "rax","rdx","rcx","rbx","rsi", \
    "rdi","rbp","r8","r9","r10",   \
    "r11","r12","r13","r14","r15"
int x, y, z;
voidf(void) {
int t = x;
asmvolatile("" : : : CLOBBER);
    y = t;
asmvolatile("" : : : CLOBBER);
    z = t;
}
\```

\```
; gcc 14 –O1
\```

\```
moveax, DWORD PTR x[rip]
movDWORDPTR y[rip], eax
moveax, DWORD PTR x[rip]
movDWORDPTR z[rip], eax
\```

## Slide 52

- ⊷ `The as-if rule – only visible effects matter`

- ⊷ `Compiler makes pragmatic choice`

   - ⊸ `Eliminate local t, invent second load from x`

   - ⊸ `2 loads vs. 3 loads in –O0 code`

- ⊷ `Confirmed feasible`

   - ⊸ `Optimizing compiler`

   - ⊸ `_can_ skip local value copy`

   - ⊸ `Duplicate memory load _not in the source_`

- ⊷ `Compiler invented loads`

   - ⊸ `Not a vulnerability by itself`

   - ⊸ `Almost always transparent`

   - ⊸ `Unless...`

# `proof-of-concept`

## Slide 53

`typedef struct { unsigned int length; uint8_t data[]; } packet_t; uint8_t buffer[MAX_SIZE]; /* kernel handler */ int receive(packet_t* pkt /* userspace data */) { /* copy size locally to prevent TOCTOU */ unsigned int local_length = pkt->length; if (local_length > MAX_SIZE) { return -1; } memcpy(buffer, pkt->data, local_length); return 0; }` pkt->length

## Slide 54

⊷ `Impossible TOCTOU`

\```
proof-of-concept
\```

## Slide 55

## Slide 56

\```
“
\```

\```
Insane? Probably so.
\```

\```
But there are compiler guys who swear by it.
\```

\```
”
\```

\```
— Paul E. McKenney · lkml · 2008-02-04
\```

## Slide 57

\```
impossible TOCTOU
\```

## Slide 58

⊷ `Mental model of what we’re _` _`supposed`_ `_ to do`

- ⊷ `Copy untrusted value to a local`

- ⊷ `Validate the local — bounds check, etc.`

- ⊷ `Use the local, assuming it can't change`

- ⊷ `Compiler doesn’t care.`

\```
impossible TOCTOU
\```

## Slide 59

- ⊷ `How do we get the compiler to listen?`

- ⊷ `volatile constrains arbitrary reads/writes`

- ⊷ `But unsettling issue...`

- ⊷ `Nothing in the source _` _`asks`_ `_ for it`

- ⊷ `Widely omitted in the TOCTOU defense`

\```
impossible TOCTOU
\```

## Slide 60

- ⊷ `Unexplored in security`

- ⊷ `New TOCTOU class`

- ⊷ `Negates standard TOCTOU-secure reasoning`

- ⊷ `Vulnerability is not in the source`

- ⊷ `Compiler decides, not the code`

- ⊷ `Must compile to find out`

- ⊷ `"Schrödinger's TOCTOU"`

# `schrödinger's TOCTOU`

## Slide 61

## Slide 62

\```
“
\```

\```
Compilers that ‘optimize’ things
\```

\```
to touch fields that aren’t touched by the source code
are simply inherently buggy shit.
\```

\```
”
\```

\```
— Linus Torvalds · lkml · 2014-12-04
\```

## Slide 63

\```
semantic drift
\```

## Slide 64

⊷ `PoC: compiler` _`_can_`_ `emit "impossible" TOCTOU`

- ⊷ `But how often, in real code?`

- ⊷ `When do invented loads` _`_really_`_ `happen?`

# `semantic drift`

## Slide 65

⊷ `Source says: copy to a local`

⊷ `Transform is legal – copy disappears`

⊷ `Binary re-reads untrusted memory` ⊷ `Intent ≠ behavior →` _`semantic drift`_

# `semantic drift`

## Slide 66

- ⊷ `Review compiler source to find culprit?`

- ⊷ `Frontend → IR → regalloc → codegen`

- ⊷ `No clear single place responsible`

- ⊷ `Readable source ≠ explainable output`

- ⊷ `Treat compiler as black-box`

- ⊷ `RE compilation pipeline’s _` _`emergent behavior`_ `_`

- ⊷ `Characterize when Schrödinger TOCTOU occurs`

# `semantic drift`

## Slide 67

\```
static RE
\```

## Slide 68

- ⊷ `Manual trial and error`

- ⊷ `Find simple code patterns that emit an invented load`

- ⊷ `A “cat-state”: minimal example of some mechanism triggering invented load`

# `the cat-states`

## Slide 69

\```
externintopaque(int a);
externconstint x;
int y, z, w;
intg(int a) {
    int t = x; // one read of x
    w = t;
    /* a dozen opaque() calls */
    y = t;
    z = t;
return0;
}
\```

\```
; x86-64 gcc -O2
;   (also: icx, icc, clang, msvc)
g:
movedx, DWORD PTR x[rip]
movDWORDPTR w[rip], edx
    …
moveax, DWORD PTR x[rip]
movDWORDPTR y[rip], eax
movDWORDPTR z[rip], eax
    …
\```

\```
cat-state: rematerialization
\```

## Slide 70

\```
; ARM gcc –O2
;   (also: MIPS, –Og, -O1, -O2, -O3)
unsignedintg(unsignedshort *p)f:
{    …
    short t = *p; // one read of *pldrshr2, [r3]
return t < 0 ? 0u : (unsignedshort)t;ldrhr0, [r3]
}cmpr2, #0
it      lt
movltr0, #0
bxlr
\```

\```
cat-state: width-mismatch reload
\```

## Slide 71

\```
typedefstruct {
int  len;
char data[12];
} S;
S dst;
intg(S *p) {
    S u = *p; // one read of *p
if (u.len > 0) {
        dst = u;
return1;
    }
return0;
}
\```

\```
; x86-64 gcc –O2
;   (also aarch64, ppc64, mips64,
;    s390x, -O1/-O2/-O3/-Os)
g:
movedx, DWORD PTR [rdi]
movdquxmm0, XMMWORD PTR [rdi]
testedx, edx
jg.L7
ret
.L7:
movapsXMMWORDPTR dst[rip], xmm0
moveax, 1
ret
\```

\```
cat-state: bulk-vs-scalar overlap
\```

## Slide 72

\```
typedefunion {
float as_float;
; x86-64 gcc –O2
longlong as_int;
;   (also: s390x)
} v_t;
g:
v_t x;
    …
addssxmm0, DWORD PTR [rdi]
longlongg(v_t *p) {
movrax, , QWORD PTR [rdi]
    v_t u = *p; // one read of *p
comissxmm0, xmm1
if (u.as_float + 1.0f > 0.0f)
cmovberax, , rdx
return u.as_int;
ret
return0;
}
\```

\```
addssxmm0, DWORD PTR [rdi]
movrax, , QWORD PTR [rdi]
comissxmm0, xmm1
cmovberax, , rdx
ret
\```

\```
cat-state: cross-class reload
\```

## Slide 73

\```
variant analysis
\```

## Slide 74

\```
typedefstruct {
char target;
char rest[16];
} S;
\```

\```
S dst;
int sink;
\```

\```
voidg(S *p) {
S u;
    memcpy(&u, p, sizeof(u)); // one read of *p
    sink = u.target * 3;
    dst  = u;
}
\```

\```
memcpy
\```

\```
; x86-64 gcc –O2
;   (also: aarch64, -O1/-O2/-O3/-Os)
g:
movsxeax, BYTE PTR [rdi]
movdquxmm0, XMMWORD PTR [rdi]
movrdx, QWORDPTR [rdi+16]
leaeax, [rax+rax*2]
movapsXMMWORDPTR dst[rip], xmm0
movDWORDPTR sink[rip], eax
movQWORDPTR dst[rip+16], rdx
ret
\```

## Slide 75

\```
typedefstruct {
char target;
char rest[16];
} S;
\```

\```
S dst;
int sink;
\```

\```
voidg(volatileS *p) {
S u;
    memcpy(&u, p, sizeof(u)); // one read of *p
    sink = u.target * 3;
    dst  = u;
}
\```

\```
volatile
\```

\```
; x86-64 gcc –O2
;   (also: aarch64, -O1/-O2/-O3/-Os)
g:
movsxeax, BYTE PTR [rdi]
movdquxmm0, XMMWORD PTR [rdi]
movrdx, QWORDPTR [rdi+16]
leaeax, [rax+rax*2]
movapsXMMWORDPTR dst[rip], xmm0
movDWORDPTR sink[rip], eax
movQWORDPTR dst[rip+16], rdx
ret
\```

## Slide 76

\```
// module_1.c
typedefstruct { int  len; char data[12];} S;
S dst;
\```

\```
; x86-64 gcc –O2 –flto
;   (also: aarch64, ppc64, mips64, s390x)
\```

\```
intok (constS *q);
voiduse(const(constconstS *q); *q);
\```

\```
voiduse(const(constconstS *q); *q);g:
movedx, DWORD PTR [rdi]
intg(S *p) {movdquxmm0, XMMWORD PTR [rdi]
S u = *p;// one read of *ptestedx, edx
if (ok(&u))    // other TU – opaquejg.L7
use(&u);   // other TU – opaqueret
return0;.L7:
}movapsXMMWORDPTR dst[rip], xmm0
moveax, 1
// module_2.cret
\```

\```
// module_2.c
intok (constS *q) { return q->len > 0; }
voiduse(constS *q) { dst = *q; }
\```

\```
translation units
\```

## Slide 77

- ⊷ `~50 distinct cat-states`

- ⊷ `Manufactured across`

      - _`_at least_`_ `six independent compiler subsystems`

- ⊷ `Vulnerable vs. not-vulnerable depends on:`

   - ⊸ `compiler×version×architecture×flags`

   - ⊸ `register pressure`

   - ⊸ `structure layout`

   - ⊸ `type width & signedness`

   - ⊸ `float` ⇄ `int unions`

   - ⊸ `byte-order conversions`

   - ⊸ `auto-vectorization`

   - ⊸ `sub-word atomics`

   - ⊸ `CISC memory-operand folds`

# `manual RE results`

## Slide 78

⊷ `Static RE is insufficient`

\```
problem
\```

## Slide 79

\```
dynamic RE
\```

## Slide 80

⊷ `Have initial datapoints, show _` _`can`_ `_ occur`

⊷ `Want to know _` _`everywhere`_ `_`

⊷ `Goal: concretely resolve the boundaries of semantic drift`

⊷ _`Exact`_ `how/when/why a given code shape emits a TOCTOU` ⊸ `compilers? code patterns? flags?`

⊷ `Then defeating should be feasible`

\```
a semantic fuzzer
\```

## Slide 81

\```
typedefstruct {
unsignedint length;
uint8_t data[];
} packet_t;
\```

\```
uint8_t buffer[MAX_SIZE];
\```

\```
/* kernel handler */
intreceive(packet_t* pkt /* userspace data */)
{
\```

\```
/* copy size locally to prevent TOCTOU */
unsignedint local_length = pkt->length;
\```

\```
if (local_length > MAX_SIZE) {
return -1;
    }
memcpy(buffer, pkt->data, local_length);
return0;
}
\```

## Slide 82

### _`cat-state`_

Matrix
Mutation
Runner
Load Detector Flag Minimizer
Engine
compilers ×
arch ×
duplicated loads minimal flag set
program variants flags ×
...
many many more filter filter

# `alpha-lab`

## Slide 83

- ⊷ `systemic mutations of cat-states`

⊷ `struct fields = explore offset dependencies`

- ⊷ `array size = block copy optimizations`

- ⊷ `local variables = impact register pressure` ⊷ `depth of function calls = function inlining`

- ⊷ `generate hundreds of mutations`

# `mutation engine`

## Slide 84

- ⊷ `Local CE instance / 200 GB of compilers`

- ⊷ `Intake code from mutation engine`

- ⊷ `Sweep compiler×version×architecture×flags` ⊸ `Compiler: 5 toolchains: GCC, Clang, ICC, ICX, MSVC` ⊸ `Version: 200+ builds, ~20 years of releases` ⊸ `Arch: x86-64, arm64, arm, RISC-V 32/64, m68k, MSP430` ⊸ `Flags: opt × lto × fp × pic × pie × stack`

- ⊷ `10,000+ compilations for each input`

# `matrix runner`

## Slide 85

- ⊷ `1M+ outputs from matrix runner`

- ⊷ `Identify whether invented load exists`

- ⊷ `Obvious`

   - ⊸ `[r0] followed by [r0]`

- ⊷ `Non-obvious`

   - ⊸ `[edx] vs. [esi]`

   - ⊸ `Loops`

   - ⊸ `Conditionals`

   - ⊸ `Architectures`

# `load detector`

## Slide 86

## ⊷ `Unicorn emulator`

- ⊷ `cat-state specifies C variable “x”`

- ⊷ `Unicorn traces memory accesses`

- ⊷ `Detect multiple reads from “x”`

- ⊷ `Auto-detect invented loads from matrix runner`

- ⊷ `Down-select to only invented load inputs`

# `load detector`

## Slide 87

⊷ `Thousands of outputs from load detector`

- ⊷ `Mostly duplicates`

- ⊷ `Which caused the double-load?`

- ⊷ `What` _`combinations?`_

- ⊷ `~250 optimizer flags, ~10^65 configurations`

- ⊷ `Delta debugging minimization`

- ⊷ `Additive sweep (–O0, –f…)`

- ⊷ `Subtractive sweep (–O3, –fno…)`

# `flag minimizer`

## Slide 88

⊷ `Example:`

⊷ `Start with one cat-state`

⊷ `Feed to the alpha-lab pipeline` ⊷ `Characterize the _` _`boundary conditions`_ `_` ⊷ `Defeat Schrödinger's TOCTOU?`

\```
dynamic RE
\```

## Slide 89

typedef struct {
int  len;
char data[12];
} S;
Matrix
Mutation  Load Flag
Runner
Engine Detector Minimizer
S dst;
compilers ×
arch ×
program  duplicated minimal
flags ×
variants loads flag set
void g(S *p) { ...
    S u = *p;
if (u.len > 0) many many more filter filter
        dst = u;
}

## Slide 90

## `/* safe/vuln changes at size threshold */`

\```
typedefstruct {
int target;
intrest[33];
} S;
S dst;
voidg(S *p) {
Su = *p;
if (u.target > 0) dst = u;
}
\```

\```
typedefstruct {
int target;
intrest[34];
} S;
S dst;
voidg(S *p) {
Su = *p;
if (u.target > 0) dst = u;
}
\```

\```
; SAFE — sizeof(S) == 136(target read once)
\```

\```
g:
movedx, DWORD PTR [rdi]
testedx, edx
jle.L1
movdxmm4, DWORDPTR [rdi+28]
    ...
.L1:
moveax, ecx
ret
\```

\```
; VULN — sizeof(S) == 140(target read twice)
\```

\```
g:
moveax, DWORD PTR [rdi]
movdquxmm7, XMMWORD PTR [rdi]
    ...
testeax, eax
jg.L7
    ...
.L7:
movapsXMMWORDPTR dst[rip], xmm7
    ...
ret
\```

## Slide 91

## `/* safe/vuln changes at field order */`

\```
typedefstruct {
inttarget;
intrest[5];
} S;
S dst;
voidg(S *p) {
S u = *p;
if (u.target > 0) dst = u;
}
\```

\```
typedefstruct {
inthead[5];
inttarget;
} S;
S dst;
voidg(S *p) {
S u = *p;
if (u.target > 0) dst = u;
}
\```

\```
; SAFE — accessed field is first
\```

\```
g:
\```

\```
moveax, DWORD PTR [rdi]
testeax, eax
jle.L1
    ...
movdxmm0, eax
movrdx, QWORDPTR [rdi+16]
    ...
.L1:
ret
\```

\```
; VULN — accessed field is second
\```

\```
g:
moveax, DWORD PTR [rdi+20]
testeax, eax
jle.L1
movrax, QWORD PTR [rdi+16]
movdquxmm0, XMMWORDPTR [rdi]
    ...
.L1:
ret
\```

## Slide 92

## `/* safe/vuln changes on compiler version */`

\```
; RISC-V64, gcc 14.3+ — SAFE (x read once)
\```

\```
structS {
unsigned a : 3;
unsigned b : 29;
};
structS x;
intf(void) {
structSu = x;
return u.a ? u.b : 0;
}
\```

\```
f:
luia5, %hi(x)
lwa5, %lo(x)(a5)
lia0, 0
andia4, a5, 7
beqa4, zero, .L2
srliwa0, a5, 3
.L2:
ret
; RISC-V64, gcc 14.1 / 14.2 — VULN (x read twice)
\```

\```
f:
luia4, %hi(x)
lwa5, %lo(x)(a4)
lia0, 0
andia5, a5, 7
beqa5, zero, .L2
lda0, %lo(x)(a4)
srliwa0, a0, 3
.L2:
ret
\```

## Slide 93

## `/* safe/vuln changes on flags */`

\```
typedefstruct {
int len;
char data[12];
} S;   /* 16 B */
S dst;
\```

\```
intg(S *p) {
Su = *p;
    dst = u;
return u.len;
}
\```

\```
; gcc -O2 -fno-tree-sra (SRA off)
;   SAFE (len read once)
g:
\```

\```
movdquxmm0, XMMWORD PTR [rdi]
movdeax, xmm0
movapsXMMWORDPTR dst[rip], xmm0
ret
\```

\```
; gcc -O2 (SRA on)
;   VULN (len read twice)
g:
\```

\```
movdquxmm0, XMMWORD PTR [rdi]
moveax, DWORD PTR [rdi]
movapsXMMWORDPTR dst[rip], xmm0
ret
\```

## Slide 94

\```
/* safe/vuln changes on architecture tune */
\```

\```
; gcc -O2 -mtune=generic
; → SAFE (target read once)
typedefstruct {g:
int target;movdquxmm0, XMMWORD PTR [rdi]
int rest[19];    ...
} S;movdeax, xmm0
ret
S dst;
intg(S *p) {; gcc -O2 -mtune=znver4
Su = *p;; → VULN (target read twice)
    dst = u;g:
return u.target;movdquxmm4, XMMWORD PTR [rdi]
}moveax, DWORD PTR [rdi]
    ...
ret
\```

## Slide 95

## `/* safe/vuln changes on sizeof ≡ 1 (mod 16) */`

\```
typedefstruct {
char head[16];
char t;
} S;
S dst;
charg(S *p) {
S u = *p;
    dst = u;
return u.t;
}
typedefstruct {
char head[17];
char t;
} S;
S dst;
charg(S *p) {
S u = *p;
    dst = u;
return u.t;
}
\```

\```
; sizeof = 17
; → SAFE (t read once)
g:
\```

\```
; bytes 0..15  (not t)
movdquxmm0, XMMWORDPTR [rdi]
movzxeax, BYTE PTR [rdi+16]
movapsXMMWORDPTR dst[rip], xmm0
movBYTEPTR dst[rip+16], al
ret
\```

\```
; sizeof = 18
;  -> VULN (t read twice)
g:
movdquxmm0, XMMWORDPTR [rdi]
movzxedx, WORD PTR [rdi+16]
movzxeax, BYTE PTR [rdi+17]
movWORDPTR dst[rip+16], dx
ret
\```

## Slide 96

|`Compiler`|`cat-states`|`Architectures`|
|---|---|---|
|`GCC`|• `Rematerialization`
• `Width-mismatch reload`
• `Bulk-vs-scalar overlap`
• `Cross-class reload`
• `CISC mem-op fold`
• `Byte-order reload`|`x86-64 · i386 · ARM · AArch64 ·`
`MIPS · MIPS64 · RV32 · RV64 ·`
`LoongArch64 · PPC64, SPARC ·`
`s390x · m68k · VAX · MSP430 · AVR`
`· HPPA · Xtensa`|
|`Clang`|• `Rematerialization`
• `Bulk-vs-scalar`
• `CISC mem-op fold`|`x86-64 · AArch64 · PPC64 · MIPS64`
`· RV64 · RV32 · 6502`|
|`ICX`|• `Rematerialization`
• `Bulk-vs-scalar`|`x86-64`|
|`ICC`|• `Rematerialization`|`x86-64`|
|`MSVC`|• `Rematerialization`
• `Bulk-vs-scalar`|`x86-64`|

# `TOCTOU by compiler`

## Slide 97

|`Architecture`|`ISA property that invites them`|
|---|---|
|`x86-64`|`register-rich, cheap RIP-relative global reload, split FP/GPR files`|
|`i386`|`single-instruction absolute global reload + register-poor 8-GPR file; bulk copy overlaps a`
`scalar field load`|
|`s390x`|`signed+unsigned 32→64 widening loads lgf/algf; an FP/GPR split, memory-operand ALU, and a `
`byte-reversed load`|
|`ARM (32-bit family)`|`rich narrow-load variants + pipelined loads; ldm bulk copy overlaps a scalar ldr`|
|`AArch64`|`wide ldp/ldr q bulk copy and NEON ld2 de-interleave overlap a scalar field load`
`(3); adrp+ldr addressing and free extend operand-modifiers suppress 1 and 2`|
|`MIPS`|`rich narrow loads, like ARM; word-granular atomics word-load a neighbor on MIPS64`|
|`RISC-V (RV64)`|`lw+ld bitfield reload; wide ld bulk copy vs scalar lw`|
|`LoongArch64`|`wide ldptr.d bulk copy vs scalar ldptr.w field load`|
|`PPC64`|`no unaligned vector load — a realigned wide load reloads each straddling aligned block`|
|`SPARC`|`word-granular atomics only — a sub-word _Atomic RMW word-loads a neighbor via an ld+cas loop`|
|`m68k / MSP430 / VAX`|`single-instruction global addressing; CISC memory-operand ALU add.l x,%d0`|
|`6502`|`memory-operand ALU; the one non-GCC instance`|

# `TOCTOU by architecture`

## Slide 98

⊷ `struct size/shape (17B/byte, 140B/dword)`

⊷ `struct tail, field position (first vs. last)`

⊷ `sizeof ≡ 1 (mod 16)`

⊷ `Direction (4 → 8B = 2 reads, 8 → 4B = 1 read)` ⊷ `Optimization level (-O2 vs. –Os vs. –Og)`

⊷ `Flags (-O2 vs. -ftree-sra vs.`

\```
“-fcode-hoisting+-ftree-ccp+-ftree-forwprop+ -ftree-fre+-ftree-pre+-ftree-vrp”)
\```

⊷ `Compiler version (gcc 14.3 vs 16.1)`

⊷ `ISA extensions (512-bit zmm or RISC-V +zicond)`

⊷ `Host CPU (–mtune)`

## Slide 99

⊷ `vulnerable or safe can depend on which machine compiled the code`

⊸ `e.g. single read on Intel, double on AMD`

- ⊷ `compiler bump can turn safe into vulnerable` ⊸ `e.g. MSVC 19.51, Clang 15; GCC 14.3 / 16.1 the other way`

- ⊷ `safety hangs on details that mean nothing`

⊸ `e.g. one byte of struct size, sizeof mod 16, a trailing char[], field order, even which direction a union widens`

   - ⊸ `each silently flips safe to vulnerable`

- ⊷ `there is no single switch to turn it off`

- ⊷ `spans the whole ecosystem`

- ⊷ `search space is effectively unbounded`

# `alpha-lab conclusions`

## Slide 100

\```
typedefstruct {
unsignedint length;
uint8_t data[];
} packet_t;
\```

\```
uint8_t buffer[MAX_SIZE];
\```

\```
/* kernel handler */
intreceive(packet_t* pkt /* userspace data */)
{
\```

\```
/* copy size locally to prevent TOCTOU */
unsignedint local_length = pkt->length;
\```

\```
if (local_length > MAX_SIZE) {
return -1;
    }
memcpy(buffer, pkt->data, local_length);
return0;
}
\```

## Slide 101

⊷ `alpha-lab conclusion:` _`cannot`_ `predict outcome` ⊷ `No longer: _` _`does_`_ `a compiler do this` ⊷ `Now: _` _`can_`_ `a compiler do this` ⊷ `Schrödinger pattern =` _`_de facto vulnerable_`_

# `alpha-lab conclusions`

## Slide 102

## Slide 103

\```
“
\```

\```
When you have to go read the compiler sources
to figure things like this out,
you know you are too deep.
\```

\```
”
\```

\```
— Linus Torvalds · lkml · 2021-09-13
\```

## Slide 104

\```
attack surface
\```

## Slide 105

- ⊷ `Where should we search?`

- ⊷ `Anywhere data crosses a trust boundary and stays writable by the untrusted side`

# `attack surface`

## Slide 106

- ⊷ `User → kernel`

   - ⊸ `syscall args, copy_from_user snapshots, io_uring shared rings`

- ⊷ `Guest → host VMM`

   - ⊸ `virtio rings, device emulation (AHCI/NVMe descriptors)`

- ⊷ `Malicious host → confidential guest`

   - ⊸ `SEV-SNP, TDX, Arm CCA; shared/bounce buffers`

- ⊷ `Secure world & enclaves`

   - ⊸ `SMM/SMI, TrustZone, SGX/TEE, EL3 monitor`

- ⊷ `Devices & DMA`

   - ⊸ `descriptor rings, MMIO, peripheral-writable buffers`

- ⊷ `Coprocessors over shared DRAM`

   - ⊸ `rpmsg/remoteproc, SCP/PSP, mailboxes, cross-VM shmem`

- ⊷ `Untrusted-format parsers`

   - ⊸ `mmap'd files, fonts/images/archives, on-disk DBs, IPC`

- ⊷ `Network / wire protocols`

   - ⊸ `RDMA, NVMe-oF, MCTP/PLDM/SPDM, NTP`

## Slide 107

⊷ `Search to find Schrödinger pattern (snapshot → validate → use)`

⊷ `... where the C-specification _` _`allows`_ `_ a TOCTOU`

⊷ `Not every case is susceptible to invented-TOCTOU`

⊷ `Certain barriers prevent emitting the second load`

\```
attack surface
\```

## Slide 108

⊷ `Example: volatile`

# `barriers`

## Slide 109

\```
typedefstruct {
unsignedint length;
uint8_t data[];
} packet_t;
uint8_t buffer[MAX_SIZE];
\```

\```
/* kernel handler */
intreceive(packet_t* pkt /* userspace data */)
{
\```

\```
/* copy size locally to prevent TOCTOU */
unsignedint local_length = pkt->length;
if (local_length > MAX_SIZE) {
return -1;
    }
\```

\```
memcpy(buffer, pkt->data, local_length);
return0;
}
\```

## Slide 110

\```
typedefstruct {
unsignedint length;
uint8_t data[];
} packet_t;
uint8_t buffer[MAX_SIZE];
\```

\```
/* kernel handler */
intreceive(packet_t* pkt /* userspace data */)
{
/* copy size locally to prevent TOCTOU */
unsignedint local_length = pkt->length;
if (local_length > MAX_SIZE) {
return -1;
    }
memcpy(buffer, pkt->data, local_length);
return0;
}
\```

## Slide 111

\```
typedefstruct {
unsignedint length;
uint8_t data[];
} packet_t;
uint8_t buffer[MAX_SIZE];
\```

\```
/* kernel handler */
intreceive(packet_t* pkt /* userspace data */)
{
/* copy size locally to prevent TOCTOU */
unsignedint local_length =
        *(volatileunsignedint *)&pkt->length;
if (local_length > MAX_SIZE) {
return -1;
    }
memcpy(buffer, pkt->data, local_length);
return0;
}
\```

## Slide 112

⊷ `volatile — at the exact access site`

- ⊷ `atomic — pins + orders`

- ⊷ `"memory"-clobber barrier`

- ⊷ `opaque copy — asm/.S primitive`

- ⊷ `copy-then-unmap / physical-address-handle`

- ⊷ `read-only mapping`

- ⊷ `per-tenant encryption (TDX/SEV/CCA)`

# `barriers`

## Slide 113

⊷ `This doesn’t scale`

⊷ `Even for _` _`small`_ `_ snippets of code`

⊷ `Outsourced to LLM-driven audit harness`

⊷ `“observer-effect”`

# `observer-effect`

## Slide 114

- ⊷ `Agent picks security-relevant open-source project`

- ⊷ `Syncs state and goals with other agents`

- ⊷ `Pulls source`

- ⊷ `Searches attacker-writable trust boundaries`

- ⊷ `Finds Schrödinger pattern: snapshot → validate → use`

- ⊷ `Evaluates: does C spec` _`_permit_`_ `the invented load?`

- ⊷ `Traces data flow to leaf for barriers`

- ⊷ `Tracks memories, mistakes, progress`

- ⊷ `Ranks impact, adversarial re-review, emit report`

# `observer-effect`

## Slide 115

⊷ `Point at range of security-critical open-source` ⊷ `Run for ~100 hours`

# `observer-effect`

## Slide 116

## Slide 117

\```
“
\```

\```
People love to talk about ‘safe C’,
but compiler people have
\```

\```
actively tried to make C unsafer for decades.
The C standards committee has been complicit.
\```

\```
”
\```

\```
— Linus Torvalds · lkml · 2025-02-21
\```

## Slide 118

\```
impact
\```

## Slide 119

\```
100+ security-critical projects
300+ Schrödinger TOCTOUs
\```

## Slide 120

## `compiler-invented load`

\```
→ compiler-invented consequences
\```

## Slide 121

\```
compiler-invented VM escapes
\```

## Slide 122

\```
uint16_tprdtl = le16_to_cpu(cmd->prdtl);          // 907  [SNAPSHOT] one read of guest header
dma_addr_tprdt_len = (prdtl * sizeof(AHCI_SG));   // 910  use #1: size the PRDT mapping
dma_addr_t real_prdt_len = prdt_len;               // 911
/* ... */
\```

\```
if (!(prdt = dma_memory_map(ad->hba->as, prdt_addr, &prdt_len,   // 929  map prdtl×16 bytes
                            DMA_DIRECTION_TO_DEVICE, MEMTXATTRS_UNSPECIFIED))){ /*...*/ }
\```

\```
if (prdt_len < real_prdt_len) {                    // 936  [CHECK] confirm full region mapped
/* ... */goto out;                            //        (bound tied to prdtl-at-910)
}
if (prdtl > 0) {
\```

\```
AHCI_SG *tbl = (AHCI_SG *)prdt;
\```

\```
for (i = 0; i < prdtl; i++) {                  // 948  [USE] walk bound over the mapping
\```

\```
        tbl_entry_size = prdt_tbl_entry_size(&tbl[i]);     //     reads tbl[i] (mapped guest mem)
/* ... */
    }
\```

\```
qemu_sglist_init(sglist, qbus->parent, (prdtl - off_idx), ad->hba->as);  // 964 [USE] alloc hint
for (i = off_idx + 1; i < prdtl && sglist->size < limit; i++) {          // 970 [USE] walk bound
qemu_sglist_add(sglist, le64_to_cpu(tbl[i].addr), /*...*/);          // 971 OOB entry → DMA
    }
}
\```

}

## Slide 123

\```
compiler-invented root
\```

## Slide 124

\```
rqe = &qp->recvq[qp->rq_get % qp->attrs.rq_size];  // 349  rqe -> userspace-shared
\```

\```
}                                                      //      vmalloc_user recvq slot
if (likely(rqe->flags == SIW_WQE_VALID)) {             // 351
intnum_sge = rqe->num_sge;                        // 352  [SNAPSHOT] one read
\```

\```
if (likely(num_sge <= SIW_MAX_SGE)) {              // 354  [CHECK] num_sge <= 6
int i = 0;
\```

\```
        wqe = rx_wqe(&qp->rx_untagged);                // 357  kernel-private siw_wqe
rx_type(wqe) = SIW_OP_RECEIVE;
\```

\```
        wqe->wr_status = SIW_WR_INPROGRESS;
        wqe->bytes = 0;
        wqe->processed = 0;
\```

\```
        wqe->rqe.id = rqe->id;
\```

\```
        wqe->rqe.num_sge = num_sge;                    // 364
\```

\```
while (i < num_sge) {                          // 366  [USE] bound -> fixed sge[6]/mem[6]
            wqe->rqe.sge[i].laddr = rqe->sge[i].laddr; // 367  compiler may re-derive
            wqe->rqe.sge[i].lkey = rqe->sge[i].lkey;   //      `num_sge` from live rqe
            wqe->rqe.sge[i].length = rqe->sge[i].length;
\```

## Slide 125

\```
compiler-invented platform persistence
\```

## Slide 126

\```
CopyMem (                                       // 199 [SNAPSHOT] copy attacker CommBuffer to stack local
    &TempLockBoxParameterRestore,
\```

\```
    LockBoxParameterRestore,
sizeof (EFI_SMM_LOCK_BOX_PARAMETER_RESTORE));
\```

\```
if (!SmmIsBufferOutsideSmmValid (               // 204 [CHECK] .Buffer/.Length must lie outside SMRAM
      (UINTN)TempLockBoxParameterRestore.Buffer,
      (UINTN)TempLockBoxParameterRestore.Length)) {
DEBUG ((DEBUG_ERROR, "SmmLockBox Restore address in SMRAM or buffer overflow!\n"));
    LockBoxParameterRestore->Header.ReturnStatus = (UINT64)EFI_ACCESS_DENIED;
return;
  }
\```

\```
if ((TempLockBoxParameterRestore.Length == 0) && (TempLockBoxParameterRestore.Buffer == 0)) {
/* ... */
\```

\```
  } else {
\```

\```
    Status = RestoreLockBox (                              // 220 [USE]
      &TempLockBoxParameterRestore.Guid,
\```

- `(VOID *)(UINTN)TempLockBoxParameterRestore.Buffer,   // 222 [USE] dest buffer`

\```
      (UINTN *)&TempLockBoxParameterRestore.Length// 223 [USE] in/out length, writes through
      );
\```

## Slide 127

\```
compiler-invented root-of-trust
\```

## Slide 128

\```
UINT16         cipherSize = 0;  // size of ciphertext
/* ... */
// Retrieve encrypted data size.
if(UINT16_Unmarshal(                           // 949  [SNAPSHOT] one read of live request
    &cipherSize,
    &buffer,
    &bufferSize) != TPM_RC_SUCCESS)
{
return TPM_RC_INSUFFICIENT;
}
\```

\```
if(cipherSize > bufferSize)                    // 954  [CHECK] validate against remaining buffer length
{
\```

\```
return TPM_RC_SIZE;
}
/* ... */
if(session->symmetric.algorithm == TPM_ALG_XOR)
CryptXORObfuscation(session->authHashAlg, &key.b, nonceCaller,
                        &(session->nonceTPM.b),
                        (UINT32)cipherSize,    // 971  [USE] in-place decrypt LENGTH over live buffer
                        buffer);
\```

## Slide 129

\```
compiler-invented enclave breaches
\```

## Slide 130

\```
ms_foo_t* ms = SGX_CAST(ms_foo_t*, pms);   // ms -> UNTRUSTED, host-writable       CodeGen.ml:1671
ms_foo_t  __in_ms;
\```

\```
if (memcpy_s(&__in_ms, sizeof(ms_foo_t), ms, sizeof(ms_foo_t)))
\```

\```
return SGX_ERROR_UNEXPECTED;           // §4.3 stack copy, not a barrier
\```

\```
void*  _tmp_buf = __in_ms.ms_buf;          // [SNAPSHOT] snapshot-once into local  CodeGen.ml:1607
size_t_len_buf = __in_ms.ms_len;          // [SNAPSHOT] host-controlled length    CodeGen.ml:1607/1611
\```

\```
CHECK_UNIQUE_POINTER(_tmp_buf, _len_buf);  // [CHECK] -> if(_tmp_buf &&            CodeGen.ml:2334-2337
//   !sgx_is_outside_enclave(_tmp_buf,_len_buf)) return ...
\```

\```
sgx_lfence();                              // §4.7 CPU-only LFENCE — pins NOTHING  CodeGen.ml:1039
\```

\```
if (_tmp_buf != NULL && _len_buf != 0) {
\```

\```
    _in_buf = (void*)malloc(_len_buf);                       // [USE] alloc size   CodeGen.ml:1304
if (_in_buf == NULL) { status = SGX_ERROR_OUT_OF_MEMORY; goto err; }
\```

\```
if (memcpy_s(_in_buf, _len_buf, _tmp_buf, _len_buf)) {   // [USE] count + cap  CodeGen.ml:1309
        status = SGX_ERROR_UNEXPECTED; goto err; }           //  compiler may re-derive _len_buf
}
\```

foo((void*)_in_buf, __in_ms.ms_len);

\```
foo((void*)_in_buf, __in_ms.ms_len);
\```

## Slide 131

\```
compiler-invented .*
\```

## Slide 132

\```
l1gpa = gfn_to_gaddr(guest_l2e_get_gfn(gw->l2e)) +
guest_l1_table_offset(va) * sizeof(gw->l1e);
if ( !hvmemul_read_cache(v, l1gpa, &gw->l1e, sizeof(gw->l1e)) )
{
\```

\```
gw->l1e = l1p[guest_l1_table_offset(va)];               // 356 [SNAPSHOT] guest PTE (l1p → guest RAM)
hvmemul_write_cache(v, l1gpa, &gw->l1e, sizeof(gw->l1e));
}
\```

\```
gflags = guest_l1e_get_flags(gw->l1e);                      // 360 [CHECK] present/rights (guest_walk.c)
if ( !(gflags & _PAGE_PRESENT) )
\```

\```
goto out;
\```

\```
/* Check for reserved bits. */
\```

\```
if ( guest_l1e_rsvd_bits(v, gw->l1e) )                      // 365 [CHECK] reserved bits (guest_walk.c)
{
\```

\```
    gw->pfec |= PFEC_reserved_bit | PFEC_page_present;
goto out;
}
/* ... */
\```

\```
    guest_walk_to_gfn → guest_l1e_get_gfn(gw->l1e)          // [USE] frame selection (guest_pt.h)
\```

## Slide 133

\```
nodeOffset  = getSyscallArg(4, buffer);                     // 62  [SNAPSHOT] crosses trust boundary
nodeWindow  = getSyscallArg(5, buffer);                     // 63  [SNAPSHOT] crosses trust boundary
/* ... */
\```

\```
if (nodeOffset > nodeSize - 1) {                            // 136 [CHECK] offset within node
/* ... */return EXCEPTION_SYSCALL_ERROR;
}
\```

\```
if (nodeWindow < 1 || nodeWindow > CONFIG_RETYPE_FAN_OUT_LIMIT) {  // 144 [CHECK] window range
/* ... */return EXCEPTION_SYSCALL_ERROR;
}
\```

\```
if (nodeWindow > nodeSize - nodeOffset) {                   // 152 [CHECK] window fits the node
/* ... */return EXCEPTION_SYSCALL_ERROR;
}
\```

\```
destCNode = CTE_PTR(cap_cnode_cap_get_capCNodePtr(nodeCap));
\```

\```
for (i = nodeOffset; i < nodeOffset + nodeWindow; i++) {    // 162 [USE] slot-emptiness loop bound
\```

\```
    status = ensureEmptySlot(destCNode + i);                // 163       (opaque call between iterations)
/* ... */
}
\```

\```
if ((untypedFreeBytes >> objectSize) < nodeWindow) {        // 203 [CHECK] enough memory for window
/* ... */return EXCEPTION_SYSCALL_ERROR;
}
\```

\```
returninvokeUntyped_Retype(slot, reset, (void *)alignedFreeRef, newType, userObjSize,
                            destCNode, nodeOffset, nodeWindow, deviceMemory);  // 229-231 [USE]
\```

## Slide 134

\```
ElfW(Half) ndx = aux->vna_other & 0x7fff;                  // 306  [SNAPSHOT] one read of the mapped ELF
/* In trace mode, dependencies may be missing.  */
if (__glibc_likely (ndx < map->l_nversions))               // 308  [CHECK] gate ndx against table size
  {
    map->l_versions[ndx].hash = aux->vna_hash;             // 310  [USE] ndx as write subscript
    map->l_versions[ndx].hidden = aux->vna_other & 0x8000; // 311  [USE] (re-reads vna_other textually)
    map->l_versions[ndx].name = &strtab[aux->vna_name];    // 312  [USE] writes an attacker pointer
    map->l_versions[ndx].filename = &strtab[ent->vn_file]; // 313  [USE] ndx
  }
\```

## Slide 135

\```
chunk_id = get_be32(table_of_contents);
\```

\```
chunk_offset = get_be64(table_of_contents + 4);          // 121 [SNAPSHOT] one read of the mmap
/* ... terminating-id check ... */
\```

\```
if (chunk_offset % expected_alignment != 0) {            // 127 [CHECK] alignment of snapshot
/* ... error ... */return1;
}
\```

\```
table_of_contents += CHUNK_TOC_ENTRY_SIZE;               // 133 advance the live pointer
\```

\```
next_chunk_offset = get_be64(table_of_contents + 4);     // 134 [SNAPSHOT] next offset
\```

\```
if (next_chunk_offset < chunk_offset ||                  // 136 [CHECK] ordering + in-file bound
\```

\```
    next_chunk_offset > mfile_size - the_hash_algo->rawsz) {
\```

\```
/* ... error ... */return -1;
}
\```

\```
for (i = 0; i < cf->chunks_nr; i++) {                    // 143 dup-id loop = register pressure
if (cf->chunks[i].id == chunk_id) { /* ... */return -1; }
}
\```

\```
cf->chunks[cf->chunks_nr].id = chunk_id;                 // 151
\```

\```
cf->chunks[cf->chunks_nr].start = mfile + chunk_offset;  // 152 [USE] chunk base ptr from offset
cf->chunks[cf->chunks_nr].size = next_chunk_offset - chunk_offset;  // 153 [USE] chunk size
\```

## Slide 136

\```
*
\```

## Slide 137

\```
Everything is vulnerable ...
\```

\```
... and everything is not.
\```

## Slide 138

- ⊷ `Schrödinger's TOCTOU is everywhere`

- ⊷ `Explored a` _`sample, not the boundary`_

- ⊷ `Exploitability is` _`not a property of the source`_ `– emergent property of compiler × version × arch × flags`

- ⊷ `Both safe` _`and`_ `vulnerable until built – then compiler decides`

- ⊷ `One optimizer tweak = TOCTOUs in thousands of deployed projects overnight`

# `impact`

## Slide 139

## Slide 140

\```
“
\```

\```
I would very much prefer a compiler switch
\```

\```
that instructs the compiler to not do bloody stupid things like this
instead of marking every other load/store in the kernel with volatile.
\```

\```
”
\```

\```
— Peter Zijlstra · lkml · 2015-06-17
\```

## Slide 141

\```
solutions
\```

## Slide 142

## ⊷ `Who is the culprit?`

   - ⊸ `Blame the code: should have marked it volatile`

      - ⊶ `Coder: I wrote what I meant - blame the compiler`

   - ⊸ `Blame the compiler: ignored the obvious intent`

      - ⊶ `Compiler: it is legal and it is fast - blame the spec`

   - ⊸ `Blame the spec: too loose to write secure code`

      - ⊶ `Spec: we define effects, not methods - blame the code`

- ⊷ `A closed loop - all three are right`

- ⊷ `Maybe the problem is C itself`

- ⊷ `Treat Schrödinger pattern as de-facto vulnerable`

# `solutions`

## Slide 143

### ⊷ `volatile`

⊸ `silently dropped at the first non-volatile parameter` ⊷ `READ_ONCE(), etc.`

⊸ `opt-in, per-load - requires already knowing every bug` ⊷ `asm volatile("" ::: "memory"), barrier(), etc.` ⊸ `position-dependent, unverified, decays as code moves`

⊷ `Opaque out-of-line call, atomic_read, RO buffers, etc.` ⊸ `pays real performance, still guarantees nothing Short term, this is what we have. All are manual, unchecked, and fail silently`

\```
short-term: code changes
\```

## Slide 144

⊷ `-fno-invented-loads flag`

⊸ `Challenge: pessimizes optimization`

⊷ `Propagating __untrusted qualifier` ⊸ `Challenge: large language and toolchain change`

\```
mid-term: compiler changes
\```

## Slide 145

- ⊷ `Memory-model change`

- ⊷ `C11 prohibited invented` _`_stores`_ `_ to shared mem` ⊷ `Challenge: decade-scale change`

\```
long-term: spec changes
\```

## Slide 146

## Slide 147

\```
“
\```

\```
Now, hoping the compiler generates correct code
 is clearly not ideal and very dangerous indeed.
\```

\```
“
\```

\```
— Peter Zijlstra · lkml · 2020-10-06
\```

## Slide 148

\```
implications
\```

## Slide 149

`typedef struct { unsigned int length; uint8_t data[]; } packet_t; uint8_t buffer[MAX_SIZE]; /* kernel handler */ int receive(packet_t* pkt /* userspace data */) { /* copy size locally to prevent TOCTOU */ unsigned int local_length = pkt->length; if (local_length > MAX_SIZE) { return -1; } memcpy(buffer, pkt->data, local_length); return 0; }` pkt->length

## Slide 150

⊷ `Don’t trust the fix.`

⊷ `Don’t trust the source.`

⊷ `Don’t trust the build.`

# `implications`

## Slide 151

## Slide 152

\```
"
\```

\```
... the definition of 'sane compiler' grows ever looser.
\```

\```
"
\```

\```
— Paul E. McKenney · lkml · 2024-09-30
\```

## Slide 153

\```
try it.
\```

## Slide 154

### `github.com/xoreaxeaxeax/schrodingers-toctou`

- _`; ARM gcc –O2`_

\```
/* compiler explorer */
\```

- _`;   (also: AARCH64/MIPS/MIPS64, -O[gs123])`_

\```
unsignedintg(unsignedshort *p)
{
\```

\```
    shortt = *p;
return (unsignedshort)t - t;
}
\```

\```
g:
ldrhr2, [r0]# load *p, once
ldrshr0, [r0]# load *p, twice
subsr0, r2, r0
bxlr
\```

\```
try it.
\```

## Slide 155

\```
C and its Consequences
\```

\```
github.com/xoreaxeaxeax/schrodingers-toctou
\```

\```
Black Hat 2026   ·   domas   ·   @xoreaxeaxeax
\```

## Slide 156

## Companion resources

### `Christopher Domas_C and Its Consequences The Source Is Just a Suggestion_tools.txt`

```text
https://github.com/xoreaxeaxeax/schrodingers-toctou/
```
