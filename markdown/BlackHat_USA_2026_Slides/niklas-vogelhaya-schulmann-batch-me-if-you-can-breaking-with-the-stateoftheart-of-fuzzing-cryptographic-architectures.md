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

Batch me if you can **Breaking with the State-of-the-Art of Fuzzing Cryptographic Architectures**

**Niklas Vogel** | Haya Schulmann ATHENE @ Goethe University Frankfur **t**

1

## Slide 2

## Agenda: A journey towards RCE in RPKI

2


> Recovered by OCR — confidence 93/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Agenda: A journey towards RCE in RPKI
=
Remote Code Execution
2
```

## Slide 3

## Agenda: A journey towards RCE in RPKI

3


> Recovered by OCR — confidence 91/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Agenda: A journey towards RCE in RPKI
Understanding the
(fuzzing) challenges
@ys4. 3
```

## Slide 4

## Agenda: A journey towards RCE in RPKI

4


> Recovered by OCR — confidence 89/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Agenda: A journey towards RCE in RPKI
fuxzer prototype
Black hat
```

## Slide 5

## Agenda: A journey towards RCE in RPKI

5


> Recovered by OCR — confidence 91/100 on the text kept, 72/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Agenda: A journey towards RCE in RPKI
Making it powerful
-
--
-
5
```

## Slide 6

## Agenda: A journey towards RCE in RPKI

6


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Agenda: A journey towards RCE in RPKI
Remote Code Execution
(and 7 other CVEs)
6
```

## Slide 7

# 1 - Motivation Fuzzing Cryptographic Architectures

7

## Slide 8

## Motivation: Cryptographic Architectures

8


> Recovered by OCR — confidence 95/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Motivation: Cryptographic Architectures
8
```

## Slide 9

## Motivation: Cryptographic Architectures

9


> Recovered by OCR — confidence 96/100 on the text kept, 96/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Motivation: Cryptographic Architectures
9
```

## Slide 10

## Motivation: Cryptographic Architectures

10


> Recovered by OCR — confidence 96/100 on the text kept, 96/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Motivation: Cryptographic Architectures
2026 10
```

## Slide 11

## Motivation: Cryptographic Architectures

11


> Recovered by OCR — confidence 87/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Motivation: Cryptographic Architectures
we we
1
```

## Slide 12

## Motivation: Cryptographic Architectures

12


> Recovered by OCR — confidence 96/100 on the text kept, 96/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Motivation: Cryptographic Architectures
2026 12
```

## Slide 13

## Cryptographic Validators

13


> Recovered by OCR — confidence 94/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Cryptographic Validators
Validator
Relying Party
>
Resolver
2026 13
```

## Slide 14

## Motivation: Cryptographic Architectures

14


> Recovered by OCR — confidence 96/100 on the text kept, 96/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Motivation: Cryptographic Architectures
2026 14
```

## Slide 15

## Motivation: Cryptographic Architectures

15


> Recovered by OCR — confidence 96/100 on the text kept, 96/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Motivation: Cryptographic Architectures
2026 15
```

## Slide 16

RPKI

16


> Recovered by OCR — confidence 84/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
RPKI
RPKI =
Routing Public Key Infrastructure”
254. 16
```

## Slide 17

RPKI

17


> Recovered by OCR — confidence 86/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
RPKI
RPKI=
SERS Public Key Infrastructure*
Resource
‘for routing
254. 17
```

## Slide 18

RPKI

18


> Recovered by OCR — confidence 83/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
RPKI
RPKI=
SERS? Public Key Infra’
Resource
‘for routing
254. 18
```

## Slide 19

## Testing Validators with Fuzzing

fuzzer
Validator

19

## Slide 20

# 2 - Fuzzing Challenge How to deal with cryptography?

20


> Recovered by OCR — confidence 86/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
2 - Fuzzing Challenge
Flow to deal with
cryptography?
(284. 20
```

## Slide 21

Fuzzing

21


> Recovered by OCR — confidence 93/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Fuzzing
Fuzzer Validator
21
```

## Slide 22

## Fuzzing Architecture

22

## Slide 23

## Fuzzing cryptographic Architectures

23


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Fuzzing cryptographic Architectures
Fuzzer Validator
2026 23
```

## Slide 24

## How to fuzz cryptographic Architectures?

24


> Recovered by OCR — confidence 94/100 on the text kept, 69/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
How to fuzz cryptographic Architectures?
```

## Slide 25

## Guessing cryptographic Values

25

## Slide 26

## Guessing cryptographic Values

26


> Recovered by OCR — confidence 88/100 on the text kept, 58/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Guessing cryptographic Values
0.000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000
0000000000000000000000000000000 ~
```

## Slide 27

## Removing Cryptography

27


> Recovered by OCR — confidence 95/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Removing Cryptography
Fuzzer Validator
27
```

## Slide 28

## Fixing Cryptography

28


> Recovered by OCR — confidence 95/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Fixing Cryptography
Fuzzer Validator
28
```

## Slide 29

# 3 - Building the Prototype An RPKI validator Fuzzer

29


> Recovered by OCR — confidence 90/100 on the text kept, 66/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
3 - Building the Prototype
An RPKI validator
Fuzzer
A.
254. 29
```

## Slide 30

## Object Parsing and Mutation

30


> Recovered by OCR — confidence 92/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Object Parsing and Mutation
AST Tree Parser
Mutation
J
Encoding
10110
—> 10110
01100
30
```

## Slide 31

## Object Parsing and Mutation

31


> Recovered by OCR — confidence 93/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Object Parsing and Mutation
EIN
AST Tree Parser Mutation Encoding
fo 40110
01100
AST Labeling
31
```

## Slide 32

## Fuzzing Architecture

32


> Recovered by OCR — confidence 90/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Fuzzing Architecture
254. 32
```

## Slide 33

# Does this work?

33

## Slide 34

## Speed of our Fuzzer

### **Speed of regular fuzzers**

34


> Recovered by OCR — confidence 93/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Speed of our Fuzzer
1500
Objects /s
Speed of regular fuzzers
Ul
O
/
200
400 600
Time (s)
800
1000
34
```

## Slide 35

## Speed of our Fuzzer

Speed of prototype fuzzer

35


> Recovered by OCR — confidence 87/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Speed of our Fuzzer
1500
~ 1000;
rs Speed of prototype fuzzer
¢) 200 400 600 800 1000
Time (s)
35
```

## Slide 36

## Speed of our Fuzzer

36


> Recovered by OCR — confidence 90/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Speed of our Fuzzer
1500
Objects /s
O
O
©
Ul
200
400 600
Time (s)
800
1000
2026 36
```

## Slide 37

## The challenge of fuzzing RPKI

37


> Recovered by OCR — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
The challenge of fuzzing RPKI
ca.cer ca.mft
=
@
37
```

## Slide 38

## The challenge of fuzzing RPKI

38


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
The challenge of fuzzing RPKI
38
```

## Slide 39

## Snapshotting Setup

39


> Recovered by OCR — confidence 95/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Snapshotting Setup
root.cer
Notify.xml
39
```

## Slide 40

## Snapshotting doesn't work

40


> Recovered by OCR — confidence 94/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Snapshotting doesn't work
Notify.xml
root.cer
2026 40
```

## Slide 41

## Sequential Fuzzing Architecture

41


> Recovered by OCR — confidence 86/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Sequential Fuzzing Architecture
2026 a
```

## Slide 42

## Sequential Fuzzing Architecture

42


> Recovered by OCR — confidence 95/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Sequential Fuzzing Architecture
2026 42
```

## Slide 43

# 4 - Making it Powerful A new fuzzing Architecture

43


> Recovered by OCR — confidence 86/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
4 - Making it Powerful
A new fuzzing
Architecture
254. 43
```

## Slide 44

## Batching Inputs

44

## Slide 45

## Batched (parallel) Fuzzing

45


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Batched (parallel) Fuzzing
2026 45
```

## Slide 46

## Batched (parallel) Fuzzing

### **Speed of our fuzzer**

46


> Recovered by OCR — confidence 91/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Batched (parallel) Fuzzing
Speed of our fuzzer
1500
~ 1000;
a 500
0 200 400 600 800
Time (s)
2026 46
```

## Slide 47

## Batched (parallel) Fuzzing

47


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Batched (parallel) Fuzzing
2026 47
```

## Slide 48

## Fuzzing in batches loses coverage benefit

48


> Recovered by OCR — confidence 88/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Fuzzing in batches loses coverage benefit
=#— NoCoverage ™< Batch Coverage
New Coverage
NO
0 100 200 300 A00 500
Iterations
2026 48
```

## Slide 49

## Coverage-guided Fuzzing

49


> Recovered by OCR — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Coverage-guided Fuzzing
void test(int vl, int v2, char *b, size t b len) {
char buf[32];
if (vl == 42) {
if (v2 = 21){
memcpy(buf, b, b len); // overflow
}
2026 49
```

## Slide 50

## Coverage-guided Fuzzing

50


> Recovered by OCR — confidence 92/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Coverage-guided Fuzzing
void test(int vl, int v2, char *b, size t b len) {
char buf[32];
if (vl == 42) {
> if (v2 = 21){
memcpy(buf, b, b len); // overflow
}
50
```

## Slide 51

## Coverage-guided Fuzzing

51


> Recovered by OCR — confidence 88/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Coverage-guided Fuzzing
void test(int vl, int v2, char *b, size t b len) {
char buf[32];
mam if (v1 == 42) { xs
if (v2 = 21)
memcpy(buf, b, b len); // overflow
}
51
```

## Slide 52

## Coverage-guided Fuzzing

**cov_counter_1 cov_counter_2 cov_counter_3** **0 0** 0

52


> Recovered by OCR — confidence 87/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Coverage-guided Fuzzing
void test(int vl, int v2, char *b, size t b len) {
// cov_counter 1++
char buf[32];
if {vl = 42) {
// cov_counter 2++
if (v2 = 21){
// cov_counter 3++
memcpy(buf, b, b len); // overflow
cov_counter_1 cov_counter_2 cov_counter_3
52
```

## Slide 53

## Coverage-guided Fuzzing

**cov_counter_1 cov_counter_2 cov_counter_3** **1 1** 0

53


> Recovered by OCR — confidence 86/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Coverage-guided Fuzzing
void test(int vl, int v2, char *b, size t b len) {
// cov_counter 1++
char buf[32];
if (vl == 42) {
// cov_counter 2++ SY
if (v2 = 21){
// cov_counter 3++
memcpy(buf, b, b len); // overflow
cov_counter_1 cov_counter_2 cov_counter_3
53
```

## Slide 54

## Coverage-guided Fuzzing

**cov_counter_1 cov_counter_2 cov_counter_3** **1 1 1**

54


> Recovered by OCR — confidence 87/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Coverage-guided Fuzzing
void test(int vl, int v2, char *b, size t b len) {
// cov_counter 1++
char buf[32];
if (vl == 42) {
// cov_counter 2++ SY
if (v2 = 21){
// cov_counter 3++ VA
= memcpy(buf, b, b len); // overflow
cov_counter_1 cov_counter_2 cov_counter_3
54
```

## Slide 55

## Coverage vs. Batches

55


> Recovered by OCR — confidence 96/100 on the text kept, 96/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Coverage vs. Batches
2026 55
```

## Slide 56

## Coverage vs. Batches

42 0 10 11
23 0 1 23
5 3 0 0
0 32 69 0
3 0 44 1

56

## Slide 57

## Coverage vs. Batches

42 0 10 11
23 0 1 23
5 3 0 0
0 32 69 0
3 0 44 1

57

## Slide 58

## Idea: Coverage Progression

New Coverage
New Coverage

58


> Recovered by OCR — confidence 91/100 on the text kept, 72/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
idea: Coverage Progression
New Coverage
New Coverage J
Ul
WW
Coverage
—
Time (ms)
0
58
```

## Slide 59

## Idea: Coverage Progression

New Coverage
New Coverage

59


> Recovered by OCR — confidence 89/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
idea: Coverage Progression
New Coverage
New Coverage J
Ul
WW
Coverage
—
—
—
20
```

## Slide 60

## Idea: Coverage Progression

**We can use this!**

60


> Recovered by OCR — confidence 87/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Object obj = objects[il;
process obj(obj);
}
// cov_counter_ f++
idea: Coverage Progression
_ 30]
5
a
£10
O
0
Time (ms)
We can use this!
2026 60
```

## Slide 61

## Use functions as timing side-channel

61


> Recovered by OCR — confidence 91/100 on the text kept, 68/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Use functions as timing side-channel
15
Coverage
N
i) W
Calls to procces_obj()
Time (ms) black hat
```

## Slide 62

## Use functions as timing side-channel

**New Coverage**

62


> Recovered by OCR — confidence 94/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Use functions as timing side-channel
15
Coverage
N
W
New Coverage
Calls to procces_obj()
Time (ms) black hat
USA 62
```

## Slide 63

## Mapping requires speed

every 100 us

63


> Recovered by OCR — confidence 87/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Mapping requires speed
_ 30;
>
3, every 100 us
U
£ 10.
O
0
63
```

## Slide 64

## Mapping requires speed

unsafe{ }

64


> Recovered by OCR — confidence 92/100 on the text kept, 67/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Mapping requires speed
Calls to procces_obj()
64
```

## Slide 65

Accurate mapping

65


> Recovered by OCR — confidence 83/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Accurate mapping
800}
Tests
400,
200
correct imprecise Wigelate|
2026 65
```

## Slide 66

## CAT Fuzzing Architecture

66


> Recovered by OCR — confidence 87/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
CAT Fuzzing Architecture
@ys4 66
```

## Slide 67

# 5 - Findings Vulnerabilities and CVEs

67

## Slide 68

# But first... The RPKI threat model

68


> Recovered by OCR — confidence 92/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
But first...
The RPKI threat model
68
```

## Slide 69

## RPKI requires availability

69


> Recovered by OCR — confidence 92/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
RPKI requires availability
—
69
```

## Slide 70

RPKI is easy to attack globally

70

## Slide 71

# 5 - Vulnerabilities in RPKI 5 implementations, 21 vulnerabilities, 8 CVEs

71

## Slide 72

Vulnerabilities in RPKI

**Type Amount Severity CVEs Implementations Remote Code Execution** 1 9.8 (critical) CVE-2024-45237 Fort Validator - - **Cache Poisoning** 1 OctoRPKI **Denial of Service** 19 7.5 (high) CVE-2025-0638, CVE-2024-45238, Routinator, rpkiCVE-2024-45235, CVE-2024-45236, client, Fort Validator, CVE-2024-45239, CVE-2024-45234, Prover, OctoRPKI CVE-2024-56375

72

## Slide 73

## Remote Code Execution

2 byte buffer

## **memcpy with attacker controlled length**

**More on this in**

<u>https://dl.acm.org/doi/abs/10.1145/3658644.3691387</u>

73

## Slide 74

## Remote Code Execution

74


> Recovered by OCR — confidence 92/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Remote Code Execution
254. 74
```

## Slide 75

## Cache Poisoning

75


> Recovered by OCR — confidence 92/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Cache Poisoning
- AS13335: 1.1.1.0/24
SubjectName: Cloudflare CA
Key: 0x349853
SubjectName: Cloudflare CA
Key: Oxf32856e
USA 5
```

## Slide 76

## Exploiting DoS

76


> Recovered by OCR — confidence 95/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Exploiting DoS
ManifestEntries: [0 elements]
76
```

## Slide 77

## Key Takeaways

#### Read Paper!

- Fuzzing in batches is efficient in complex cryptographic infrastructures

- Coverage counters serve as sidechannel to map coverage in batches

#### Contact Me!

- Routing security relies on the security of RPKI, which is fragile

77
