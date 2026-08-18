---
title: "Batch Me If You Can Breaking With the State‑of‑the‑Art of Fuzzing Cryptographic Architectures"
speakers: ["Niklas Vogel", "Haya Schulmann"]
conference: "Black Hat"
conference_full: "Black Hat USA 2026"
edition: "USA"
year: 2026
source_pdf: "BlackHat_USA_2026_Slides/Niklas Vogel&Haya Schulmann_Batch Me If You Can Breaking With the State‑of‑the‑Art of Fuzzing Cryptographic Architectures.pdf"
pages: 77
sha256: "db7204f0660a798b0899b01eac4030050ff4890b7d4dbd5d1b36d02fb2c5e01d"
text_chars: 8874
ocr_pages: 62
has_ocr: true
redacted_secrets: 0
ocr_confidence: 91.1
ocr_unreliable_blocks: 1
vision_verified_pages_changed: 77
vision_verified_pages: 77
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T05:41:00Z"
---
# Batch Me If You Can Breaking With the State‑of‑the‑Art of Fuzzing Cryptographic Architectures

**Speakers:** Niklas Vogel, Haya Schulmann  
**Conference:** Black Hat USA 2026  
**Source:** `BlackHat_USA_2026_Slides/Niklas Vogel&Haya Schulmann_Batch Me If You Can Breaking With the State‑of‑the‑Art of Fuzzing Cryptographic Architectures.pdf` (77 pages)


## Slide 1

# Batch me if you can

**Breaking with the State-of-the-Art of Fuzzing Cryptographic Architectures**

**Niklas Vogel** | Haya Schulmann  
ATHENE @ Goethe University Frankfurt

## Slide 2

## Agenda: A journey towards RCE in RPKI

- Motivation
- Remote Code Execution

## Slide 3

## Agenda: A journey towards RCE in RPKI

- Understanding the (fuzzing) challenges

## Slide 4

## Agenda: A journey towards RCE in RPKI

- Building a fuzzer prototype

## Slide 5

## Agenda: A journey towards RCE in RPKI

- Making it powerful

## Slide 6

## Agenda: A journey towards RCE in RPKI

- Remote Code Execution (and 7 other CVEs)

## Slide 7

# 1 - Motivation

## Fuzzing Cryptographic Architectures

## Slide 8

## Motivation: Cryptographic Architectures

## Slide 9

## Motivation: Cryptographic Architectures

## Slide 10

## Motivation: Cryptographic Architectures

## Slide 11

## Motivation: Cryptographic Architectures

## Slide 12

## Motivation: Cryptographic Architectures

## Slide 13

## Cryptographic Validators

Validator  
Relying Party  
Resolver

## Slide 14

## Motivation: Cryptographic Architectures

DNS

## Slide 15

## Motivation: Cryptographic Architectures

RPKI

## Slide 16

## RPKI

**RPKI =**

**R**outing **P**ublic **K**ey **I**nfrastructure\*

## Slide 17

## RPKI

**RPKI =**

~~**R**outing~~ **P**ublic **K**ey **I**nfrastructure\*  
**R**esource

\*for routing

## Slide 18

## RPKI

**RPKI =**

~~**R**outing~~ **P**ublic **K**ey **I**nfrastructure\*  
**R**esource

\*for routing

## Slide 19

## Testing Validators with Fuzzing

fuzzer  
Validator

## Slide 20

# 2 - Fuzzing Challenge

## How to deal with cryptography?

## Slide 21

## Fuzzing

Fuzzer → Validator

## Slide 22

## Fuzzing Architecture

Seed file → mutation engine → crashing input → target (no text labels on this build).

## Slide 23

## Fuzzing cryptographic Architectures

Fuzzer → **Failed** ✗ | Validator

## Slide 24

## How to fuzz cryptographic Architectures?

Fuzzer → (a mass of crossed-out inputs, one exploding) | Validator

## Slide 25

## Guessing cryptographic Values

0.000

## Slide 26

## Guessing cryptographic Values

0.000000000000000000000000000000000000000000000…[……]1%

The slide shows ten rows of zeros in total — nine full lines and a tenth that ends in the trailing `[……]1%`; rows 4–9 run behind an overlaid image, so the exact number of zeros cannot be read off the page.

## Slide 27

## Removing Cryptography

Fuzzer → Validator (the signature-checking gear is crossed out)

## Slide 28

## Fixing Cryptography

Fuzzer → Validator (the mutated object is patched, and passes ✓)

## Slide 29

# 3 - Building the Prototype

## An RPKI validator Fuzzer

## Slide 30

## Object Parsing and Mutation

Input file → **AST Tree Parser** → **Mutation** → **Encoding**

Encoding output:

```text
10110
10110
01100
```

## Slide 31

## Object Parsing and Mutation

Input file → **AST Tree Parser** → **AST Labeling** → **Mutation** → **Fixing** → **Encoding**

Encoding output:

```text
10110
10110
01100
```

## Slide 32

## Fuzzing Architecture

**Corpus** → **Queue** → **Mutation** → **Harness** → **Target**

- **Target** → **Scoring**, and **Target** → **Oracle**: two independent edges leaving Target. **Oracle** is a terminal node here — nothing leaves it.
- **Scoring** → back into **Queue**.
- Queue, Mutation, Harness, Scoring and Oracle sit inside the dashed fuzzer boundary; Corpus and Target sit outside it.

## Slide 33

# Does this work?

## Slide 34

## Speed of our Fuzzer

Line chart — x-axis **Time (s)** with ticks 0, 200, 400, 600, 800, 1000; y-axis **Objects / s** with ticks 0, 500, 1000, 1500.

- Orange line, flat at 1000 objects/s — annotated **Speed of regular fuzzers**

## Slide 35

## Speed of our Fuzzer

Line chart — x-axis **Time (s)** with ticks 0, 200, 400, 600, 800, 1000; y-axis **Objects / s** with ticks 0, 500, 1000, 1500.

- Orange line, flat at 1000 objects/s (speed of regular fuzzers)
- Blue line, flat just above 0 objects/s — annotated **Speed of prototype fuzzer**

## Slide 36

## Speed of our Fuzzer

Same chart as the previous slide — x-axis **Time (s)** 0–1000, y-axis **Objects / s** 0–1500, orange line flat at 1000 and blue line flat just above 0 — with a photograph of a wrecked box truck dropped over the plot area. No new text labels.

## Slide 37

## The challenge of fuzzing RPKI

Every fuzzing iteration has to walk the whole RPKI publication chain:

**TAL** → **root.cer** → **Notify.xml** → **Snap.xml** → **ca.cer** → **ca.mft** → **ca.crl** → **test.roa**

Everything up to and including `ca.crl` sits inside the dashed boundary; the mutated `test.roa` (red) sits outside it.

## Slide 38

## The challenge of fuzzing RPKI

Same chain as the previous slide — **TAL** → **root.cer** → **Notify.xml** → **Snap.xml** → **ca.cer** → **ca.mft** → **ca.crl** → **test.roa** — with a meme image dropped over the `Notify.xml` / `Snap.xml` end of the top row. No new text labels.

## Slide 39

## Snapshotting Setup

A dashed box holds the whole static repository — **TAL**, **root.cer**, **Notify.xml**, **Snap.xml**, **ca.cer**, **ca.mft**, **ca.crl** — stacked as one bundle.

That bundle is **load**ed into **state**, and **state** ↔ **test.roa** exchange in both directions.

## Slide 40

## Snapshotting doesn't work

The same objects, but now every one of them depends on the others, so no snapshot can be taken:

- **Snap.xml** → **Notify.xml** → **root.cer** → **TAL**
- **Notify.xml** → **Snap.xml**
- **root.cer** → **ca.cer**
- **ca.cer**, **ca.mft**, **ca.crl** and **test.roa** all feed back into each other, and **test.roa** feeds back up into **Snap.xml**

## Slide 41

## Sequential Fuzzing Architecture

**Corpus** → **Queue** → **Mutation** → **Harness** → **Target**

- **Target** → **Scoring**, and **Target** → **Oracle**: two independent edges leaving Target. **Oracle** is a terminal node here — nothing leaves it.
- **Scoring** → back into **Queue**.
- Queue, Mutation, Harness, Scoring and Oracle sit inside the dashed fuzzer boundary; Corpus and Target sit outside it.

## Slide 42

## Sequential Fuzzing Architecture

The same **Corpus → Queue → Mutation → Harness → Target → Oracle → Scoring → Queue** loop, greyed out, with a large red question mark over it and a thinking-face meme alongside. No new text labels.

## Slide 43

# 4 - Making it Powerful

## A new fuzzing Architecture

## Slide 44

## Batching Inputs

Inside the dashed box (the fixed part of the repository, built once):

- **TAL**, **root.cer**, **Notify.xml**, **Snap.xml**
- **ca.cer**, **ca.mft**, **ca.crl**

Outside it: a whole stack of mutated **test.roa** objects, batched together.

## Slide 45

## Batched (parallel) Fuzzing

The same loop as the sequential architecture, but every edge now carries several inputs in parallel:

**Corpus** ⇒ **Queue** ⇒ **Mutation** ⇒ **Harness** ⇒ **Target** ⇒ **Scoring** ⇒ back into **Queue**

- **Target** → **Oracle** (single edge).
- Queue, Mutation, Harness, Scoring and Oracle sit inside the dashed fuzzer boundary; Corpus and Target sit outside it.

## Slide 46

## Batched (parallel) Fuzzing

Line/scatter chart — x-axis **Time (s)** with ticks 0, 200, 400, 600, 800, 1000; y-axis **Objects / s** with ticks 0, 500, 1000, 1500.

- Blue scatter band around 1200 objects/s — annotated **Speed of our fuzzer**
- Orange line flat at 1000 objects/s (the regular-fuzzer baseline)

Meme caption over the plot: *I am speed*

## Slide 47

## Batched (parallel) Fuzzing

The same batched loop — **Corpus** ⇒ **Queue** ⇒ **Mutation** ⇒ **Harness** ⇒ **Target** ⇒ **Scoring** ⇒ **Queue**, with **Target** → **Oracle** — and a large red arrow pointing at the **Scoring** box.

## Slide 48

## Fuzzing in batches loses coverage benefit

Line chart — x-axis **Iterations** with ticks 0, 100, 200, 300, 400, 500; y-axis **New Coverage** with ticks 0, 1000, 2000, 3000, 4000.

Legend:

- **No Coverage** (blue triangles)
- **Batch Coverage** (green crosses)

Both series rise almost vertically from 0 and then sit on top of each other just under 3000 for the rest of the run — batching gives no coverage advantage.

## Slide 49

## Coverage-guided Fuzzing

```c
void test(int v1, int v2, char *b, size_t b_len) {
    char buf[32];

    if (v1 == 42) {
        if (v2 = 21){
            memcpy(buf, b, b_len); // overflow
        }
    }
}
```

## Slide 50

## Coverage-guided Fuzzing

Input thrown at the target:

- v1: 42
- v2: 67

```c
void test(int v1, int v2, char *b, size_t b_len) {
    char buf[32];

    if (v1 == 42) {
        if (v2 = 21){
            memcpy(buf, b, b_len); // overflow
        }
    }
}
```

The `if (v2 = 21)` line is marked ✗ — the input gets past the first check but not the second.

## Slide 51

## Coverage-guided Fuzzing

Input thrown at the target:

- v1: 22
- v2: 21

```c
void test(int v1, int v2, char *b, size_t b_len) {
    char buf[32];

    if (v1 == 42) {
        if (v2 = 21){
            memcpy(buf, b, b_len); // overflow
        }
    }
}
```

The `if (v1 == 42)` line is marked ✗ — the input fails at the very first check.

## Slide 52

## Coverage-guided Fuzzing

The same function, instrumented — each boxed comment is a coverage counter:

```c
void test(int v1, int v2, char *b, size_t b_len) {
    // cov_counter_1++

    char buf[32];

    if (v1 == 42) {
        // cov_counter_2++

        if (v2 = 21){
            // cov_counter_3++

            memcpy(buf, b, b_len); // overflow
        }
    }
}
```

| cov_counter_1 | cov_counter_2 | cov_counter_3 |
| --- | --- | --- |
| 0 | 0 | 0 |

## Slide 53

## Coverage-guided Fuzzing

Input thrown at the target:

- v1: 42
- v2: 67

```c
void test(int v1, int v2, char *b, size_t b_len) {
    // cov_counter_1++

    char buf[32];

    if (v1 == 42) {
        // cov_counter_2++

        if (v2 = 21){
            // cov_counter_3++

            memcpy(buf, b, b_len); // overflow
        }
    }
}
```

`cov_counter_1++` and `cov_counter_2++` are ticked ✓; `if (v2 = 21){` is marked ✗.

| cov_counter_1 | cov_counter_2 | cov_counter_3 |
| --- | --- | --- |
| 1 ✓ | 1 ✓ | 0 |

## Slide 54

## Coverage-guided Fuzzing

Input thrown at the target:

- v1: 42
- v2: 21

```c
void test(int v1, int v2, char *b, size_t b_len) {
    // cov_counter_1++

    char buf[32];

    if (v1 == 42) {
        // cov_counter_2++

        if (v2 = 21){
            // cov_counter_3++

            memcpy(buf, b, b_len); // overflow
        }
    }
}
```

All three counters are ticked ✓ and execution reaches the `memcpy` line.

| cov_counter_1 | cov_counter_2 | cov_counter_3 |
| --- | --- | --- |
| 1 ✓ | 1 ✓ | 1 ✓ |

## Slide 55

## Coverage vs. Batches

A whole batch of inputs is thrown at the validator at once, and only one aggregate result comes back — which input caused what is unknown (a large red **?** sits on the return path).

## Slide 56

## Coverage vs. Batches

The batch comes back as one coverage matrix:

```text
42   0   10   11
23   0    1   23
 5   3    0    0
 0  32   69    0
 3   0   44    1
```

## Slide 57

## Coverage vs. Batches

Same coverage matrix coming back from the batch, with a puzzled-face meme and a red **?** where the thrower was:

```text
42   0   10   11
23   0    1   23
 5   3    0    0
 0  32   69    0
 3   0   44    1
```

## Slide 58

## Idea: Coverage Progression

Step chart — x-axis **Time (ms)** with ticks 0, 20, 40, 60, 80, 100; y-axis **Coverage** with ticks 10, 11, 12, 13, 14, 15.

- Coverage sits at 11 until t = 40 ms, steps up to 13 — annotated **New Coverage**
- Holds at 13 until t = 70 ms, steps up to 14 — annotated **New Coverage**
- Holds at 14 to the end of the run

## Slide 59

## Idea: Coverage Progression

Same step chart as the previous slide — x-axis **Time (ms)** 0–100, y-axis **Coverage** 10–15, stepping 11 → 13 at t = 40 ms and 13 → 14 at t = 70 ms, both steps annotated **New Coverage** — with a meme image dropped over the bottom-right of the plot.

## Slide 60

## Idea: Coverage Progression

```c
for(int i = 0; i < b_len; i++){
    Object obj = objects[i];
    process_obj(obj);
    // ...
}

void process_obj(Object obj){
    // cov_counter_f++

    obj.validate();
    // ...
}
```

**We can use this!** — the arrow points at `// cov_counter_f++`.

Chart alongside — x-axis **Time (ms)** with ticks 0, 20, 40, 60, 80, 100; y-axis **Calls to procces_obj()** with ticks 0, 10, 20, 30. The step curve sits at 0 until about t = 22 ms, climbs steadily to 30 by about t = 80 ms and stays flat.

## Slide 61

## Use functions as timing side-channel

Two stacked charts sharing the same x-axis, **Time (ms)** with ticks 0, 20, 40, 60, 80, 100:

- Top — y-axis **Coverage** with ticks 10, 11, 12, 13, 14, 15. Magenta step line: 11 until t = 40 ms, 13 until t = 70 ms, 14 thereafter.
- Bottom — y-axis **Calls to procces_obj()** with ticks 0, 10, 20, 30. Orange step curve: 0 until about t = 22 ms, climbing to 30 by about t = 80 ms, flat thereafter.

## Slide 62

## Use functions as timing side-channel

The same two stacked charts — **Coverage** (10–15) over **Time (ms)** on top, **Calls to procces_obj()** (0–30) over **Time (ms)** below.

An arrow drops from the coverage step at t = 40 ms onto the call-count curve, and reads across to about 10 calls on the y-axis: **New Coverage**.

## Slide 63

## Mapping requires speed

Chart — x-axis carries only the bare ticks 0, 20, 40, 60, 80, 100 with no axis title on the page; y-axis is titled **Calls to procces_obj()** with ticks 0, 10, 20, 30.

The orange step curve sits at 0 until about t = 22 ms, then climbs one step at a time to 30 by about t = 80 ms and stays flat. The annotation on the rising part reads **every 100 us**.

## Slide 64

## Mapping requires speed

The same chart — x-axis ticks 0–100 with no axis title on the page, y-axis titled **Calls to procces_obj()** 0–30, orange step curve rising from 0 at about t = 22 — with a cartoon dropped over its right-hand half.

Caption on the cartoon: *unsafe{ }*

## Slide 65

## Accurate mapping

Bar chart — y-axis **Tests** with ticks 0, 200, 400, 600, 800, 1000; three categories on the x-axis: **correct**, **imprecise**, **wrong**. Three bars (red, blue, green) per category.

- **correct** — all three bars at or just under 1000
- **imprecise** — a small red bar and a smaller green bar, both just above 0; no blue bar
- **wrong** — a single small red bar just above 0

No per-bar values are printed on the slide.

## Slide 66

## CAT Fuzzing Architecture

The dotted boundary labelled **CAT** 🐈 encloses Corpus, Template Agnostic DER Parser, Labeling, Snapshot RPKI Repo, Fuzzing Queue, Batch Mutation, Signing and Nesting, Scoring and Oracle. **RPKI Validator**, its **Coverage** tag and **Findings Reports** are drawn outside that boundary, to the right of it.

- **Corpus** → **Template Agnostic DER Parser** → **Labeling**
- **Labeling** ⇢ **Fuzzing Queue** (dashed)
- **Snapshot RPKI Repo** ⇢ **Signing and Nesting** (dashed)
- **Fuzzing Queue** → **Batch Mutation** → **Signing and Nesting** → **RPKI Validator**
- **RPKI Validator** carries a **Coverage** tag; **Coverage** → **Scoring** → back into **Fuzzing Queue**
- **RPKI Validator** ⇢ **Oracle** (dashed)
- **Oracle** ⇢ **Findings Reports** (dashed, arrowhead at the Findings Reports end only)

## Slide 67

# 5 - Findings

## Vulnerabilities and CVEs

## Slide 68

# But first...

## The RPKI threat model

## Slide 69

## RPKI requires availability

The RPKI repository and the router exchange traffic in both directions — if the repository is unavailable, the router has nothing to validate against.

## Slide 70

## RPKI is easy to attack globally

One server talks to four separate RPKI repositories, each over its own bidirectional link — a single attacker reaches all of them.

## Slide 71

# 5 - Vulnerabilities in RPKI

## 5 implementations, 21 vulnerabilities, 8 CVEs

## Slide 72

## Vulnerabilities in RPKI

| Type | Amount | Severity | CVEs | Implementations |
| --- | --- | --- | --- | --- |
| **Remote Code Execution** | 1 | 9.8 (critical) | CVE-2024-45237 | Fort Validator |
| **Cache Poisoning** | 1 | - | - | OctoRPKI |
| **Denial of Service** | 19 | 7.5 (high) | CVE-2025-0638, CVE-2024-45238, CVE-2024-45235, CVE-2024-45236, CVE-2024-45239, CVE-2024-45234, CVE-2024-56375 | Routinator, rpki-client, Fort Validator, Prover, OctoRPKI |

## Slide 73

## Remote Code Execution

```c
unsigned char data[2];

if (ku->length == 0) {
    return pr_val_err("%s bit string has no enabled bits.",
        ext_ku()->name);
}

memset(data, 0, sizeof(data));
memcpy(data, ku->data, ku->length);
```

- **2 byte buffer** — points at `unsigned char data[2];`
- **memcpy with attacker controlled length** — points at `memcpy(data, ku->data, ku->length);`

More on this in

<https://dl.acm.org/doi/abs/10.1145/3658644.3691387>

## Slide 74

## Remote Code Execution

Attacker → poisoned RPKI repository → router (which is blown up despite its shield).

The announcement carried over the link reads **AS666: 1.1.1.0/24**.

## Slide 75

## Cache Poisoning

Attacker poisons the RPKI repository, which then feeds the router:

**- AS13335: 1.1.1.0/24**

- ✓ SubjectName: Cloudflare CA / Key: 0x349853
- ✗ SubjectName: Cloudflare CA / Key: 0xf32856e

## Slide 76

## Exploiting DoS

Attacker → explosive object → RPKI repository (destroyed) ↔ router (destroyed).

The object that does it: **ManifestEntries: [0 elements]**

## Slide 77

## Key Takeaways

- Fuzzing in batches is efficient in complex cryptographic infrastructures

- Coverage counters serve as side-channel to map coverage in batches

- Routing security relies on the security of RPKI, which is fragile

**Read Paper!** — QR code

**Contact Me!** — QR code

