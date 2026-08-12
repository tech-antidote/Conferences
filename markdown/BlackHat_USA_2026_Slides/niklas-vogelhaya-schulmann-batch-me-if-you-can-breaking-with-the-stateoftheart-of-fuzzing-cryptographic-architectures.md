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
text_chars: 10909
ocr_pages: 66
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T23:14:24Z"
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Agenda: A journey towards RCE in RPKI
. Tog |
\ _ 8 | i
=
Remote Code Execution
black hat
2
2026
```

## Slide 3

## Agenda: A journey towards RCE in RPKI

3

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Agenda: A journey towards RCE in RPKI
Understanding the
(fuzzing) challenges
black hat
@ys4. 3
```

## Slide 4

## Agenda: A journey towards RCE in RPKI

4

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Agenda: A journey towards RCE in RPKI
Building a
fuxzer prototype
Black hat
```

## Slide 5

## Agenda: A journey towards RCE in RPKI

5

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Agenda: A journey towards RCE in RPKI
Making it powerful
o”
-
--
-
=_”-
=r"
--"
7
7
black hat
5
2026
```

## Slide 6

## Agenda: A journey towards RCE in RPKI

6

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Agenda: A journey towards RCE in RPKI
Remote Code Execution
(and 7 other CVEs)
black hat
6
2026
```

## Slide 7

# 1 - Motivation Fuzzing Cryptographic Architectures

7

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
1- Motivation
Fuzzing Cryptographic
Architectures oreP
black hat
@ys4. 7
```

## Slide 8

## Motivation: Cryptographic Architectures

8

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Motivation: Cryptographic Architectures
black hat
8
2026
```

## Slide 9

## Motivation: Cryptographic Architectures

9

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Motivation: Cryptographic Architectures
black hat
9
2026
```

## Slide 10

## Motivation: Cryptographic Architectures

10

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Motivation: Cryptographic Architectures
black hat
2026 10
```

## Slide 11

## Motivation: Cryptographic Architectures

11

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Motivation: Cryptographic Architectures
es eS
we we
black hat
1
2026
```

## Slide 12

## Motivation: Cryptographic Architectures

12

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Motivation: Cryptographic Architectures
black hat
2026 12
```

## Slide 13

## Cryptographic Validators

13

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Cryptographic Validators
ZO
(
—+| 6H |%4
Validator
Relying Party
>
Resolver
black hat
2026 13
```

## Slide 14

## Motivation: Cryptographic Architectures

14

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Motivation: Cryptographic Architectures
black hat
2026 14
```

## Slide 15

## Motivation: Cryptographic Architectures

15

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Motivation: Cryptographic Architectures
black hat
2026 15
```

## Slide 16

RPKI

16

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
RPKI
RPKI =
Routing Public Key Infrastructure”
black hat
254. 16
```

## Slide 17

RPKI

17

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
RPKI
RPKI=
SERS Public Key Infrastructure*
Resource
‘for routing
black hat
254. 17
```

## Slide 18

RPKI

18

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
RPKI
RPKI=
SERS? Public Key Infra’
Resource
‘for routing
black hat
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2 - Fuzzing Challenge
Flow to deal with
cryptography?
black hat
(284. 20
```

## Slide 21

Fuzzing

21

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Fuzzing
Fuzzer Validator
2 G6
black hat
21
2026
```

## Slide 22

## Fuzzing Architecture

22

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Fuzzing Architecture
© £85
black hat
22
2026
```

## Slide 23

## Fuzzing cryptographic Architectures

23

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Fuzzing cryptographic Architectures
Fuzzer Validator
black hat
2026 23
```

## Slide 24

## How to fuzz cryptographic Architectures?

24

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
How to fuzz cryptographic Architectures?
Fuzzer 5 Se ry key, Validator
* ABS
ae
black hat
2026
```

## Slide 25

## Guessing cryptographic Values

25

## Slide 26

## Guessing cryptographic Values

26

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Guessing cryptographic Values
0.000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000
0000000000000000000000000000006¢
0000000000000000000000000000000
0000000000000000000000000000000 ~
0000000000000000000000000000000 ~
O000000000000000000000000000000C, ~
000000000000000000000000000000C HF" ,@
0000000000000000000000000000000000000I.......]1%
black hat
2026
```

## Slide 27

## Removing Cryptography

27

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Removing Cryptography
Fuzzer Validator
black hat
27
2026
```

## Slide 28

## Fixing Cryptography

28

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Fixing Cryptography
Fuzzer Validator
black hat
28
2026
```

## Slide 29

# 3 - Building the Prototype An RPKI validator Fuzzer

29

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
3 - Building the Prototype
An RPKI validator
Fuzzer
A.
a He
-_____—| @
— aaa
Ol ee ee ee
black hat
254. 29
```

## Slide 30

## Object Parsing and Mutation

30

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Object Parsing and Mutation
=) \
AST Tree Parser
Mutation
[>
J
Encoding
10110
—> 10110
01100
black hat
30
2026
```

## Slide 31

## Object Parsing and Mutation

31

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Object Parsing and Mutation
EIN
AST Tree Parser Mutation Encoding
fo 40110
9) —> 10110
01100
AST Labeling
black hat
31
2026
```

## Slide 32

## Fuzzing Architecture

32

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Fuzzing Architecture
black hat
254. 32
```

## Slide 33

# Does this work?

33

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Does this work?
black hat
254. 33
```

## Slide 34

## Speed of our Fuzzer

### **Speed of regular fuzzers**

34

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Speed of our Fuzzer
1500
Objects /s
Speed of regular fuzzers
a
oO
oO
oO
Ul
O
i)
/
200
400 600
Time (s)
800
1000
black hat
34
2026
```

## Slide 35

## Speed of our Fuzzer

Speed of prototype fuzzer

35

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Speed of our Fuzzer
1500
YW)
~ 1000;
rs Speed of prototype fuzzer
2S 500) /
QO:
¢) 200 400 600 800 1000
Time (s)
black hat
35
2026
```

## Slide 36

## Speed of our Fuzzer

36

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Speed of our Fuzzer
1500
Objects /s
_
O
O
©
Ul
oO
oO
200
400 600
Time (s)
800
1000
black hat
2026 36
```

## Slide 37

## The challenge of fuzzing RPKI

37

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
The challenge of fuzzing RPKI
ca.cer ca.mft
=
@
black hat
37
2026
```

## Slide 38

## The challenge of fuzzing RPKI

38

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
The challenge of fuzzing RPKI
black hat
38
2026
```

## Slide 39

## Snapshotting Setup

39

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Snapshotting Setup
root.cer
Notify.xml
black hat
39
2026
```

## Slide 40

## Snapshotting doesn't work

40

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Snapshotting doesn't work
Notify.xml
i)
root.cer
black hat
2026 40
```

## Slide 41

## Sequential Fuzzing Architecture

41

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Sequential Fuzzing Architecture
black hat
2026 a
```

## Slide 42

## Sequential Fuzzing Architecture

42

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Sequential Fuzzing Architecture
black hat
2026 42
```

## Slide 43

# 4 - Making it Powerful A new fuzzing Architecture

43

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
4 - Making it Powerful
A new fuzzing
Architecture
black hat
254. 43
```

## Slide 44

## Batching Inputs

44

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Batching Inputs
I
I
l
I
l
I
Lo _
I
I
I
= |
Xx] F 5 |
Tay °
_ 5 |
(e} = Ww |
2
I
ara
EW SS |
5
1%)
_
9 |
e } |
rd
| ios |
: !
5 |
u I
re} I
rv) l
I
I
I
l
I
I
I
oo J
black hat
254. 44
```

## Slide 45

## Batched (parallel) Fuzzing

45

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Batched (parallel) Fuzzing
black hat
2026 45
```

## Slide 46

## Batched (parallel) Fuzzing

### **Speed of our fuzzer**

46

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Batched (parallel) Fuzzing
Speed of our fuzzer
1500
WY)
~ 1000;
WY)
1s)
v
a 500
ol—. | |
0 200 400 600 800
Time (s)
black hat
2026 46
```

## Slide 47

## Batched (parallel) Fuzzing

47

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Batched (parallel) Fuzzing
black hat
2026 47
```

## Slide 48

## Fuzzing in batches loses coverage benefit

48

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Fuzzing in batches loses coverage benefit
Op
=#— NoCoverage ™< Batch Coverage
3000 |
New Coverage
NO
oO
)
oO
1000;
0 100 200 300 A00 500
Iterations
black hat
2026 48
```

## Slide 49

## Coverage-guided Fuzzing

49

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Coverage-guided Fuzzing
void test(int vl, int v2, char *b, size t b len) {
char buf[32];
if (vl == 42) {
if (v2 = 21){
memcpy(buf, b, b len); // overflow
}
black hat
2026 49
```

## Slide 50

## Coverage-guided Fuzzing

50

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Coverage-guided Fuzzing
void test(int vl, int v2, char *b, size t b len) {
char buf[32];
if (vl == 42) {
> if (v2 = 21){
memcpy(buf, b, b len); // overflow
}
black hat
50
2026
```

## Slide 51

## Coverage-guided Fuzzing

51

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Coverage-guided Fuzzing
void test(int vl, int v2, char *b, size t b len) {
char buf[32];
mam if (v1 == 42) { xs
if (v2 = 21)
memcpy(buf, b, b len); // overflow
}
black hat
51
2026
```

## Slide 52

## Coverage-guided Fuzzing

**cov_counter_1 cov_counter_2 cov_counter_3** **0 0** 0

52

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

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
0 0 0
black hat
52
2026
```

## Slide 53

## Coverage-guided Fuzzing

**cov_counter_1 cov_counter_2 cov_counter_3** **1 1** 0

53

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

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
1\f 1Vf 0
black hat
53
2026
```

## Slide 54

## Coverage-guided Fuzzing

**cov_counter_1 cov_counter_2 cov_counter_3** **1 1 1**

54

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

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
1\f 1Vf 1f
black hat
54
2026
```

## Slide 55

## Coverage vs. Batches

55

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Coverage vs. Batches
black hat
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
idea: Coverage Progression
New Coverage
New Coverage J
J
ra)
Ul
a
ms
=
WW
Coverage
—
i)
a
a
_)
io)
20 AO 60 80 100
Time (ms)
0
black hat
58
2026
```

## Slide 59

## Idea: Coverage Progression

New Coverage
New Coverage

59

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
idea: Coverage Progression
New Coverage
New Coverage J
ra)
Ul
S|
=
WW
Coverage
—
i)
—
—
py
is)
©
20
black hat
qeyss 59
```

## Slide 60

## Idea: Coverage Progression

**We can use this!**

60

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
for(int i = 0; i < b len; i+t+){
Object obj = objects[il;
process obj(obj);
// uae
}
void process obj (Object obj){
// cov_counter_ f++
obj .validate();
// ua.
idea: Coverage Progression
_ 30]
S
°,
3 20;
5
a
£10
3
O
0
0 20 40 60 80 100
Time (ms)
We can use this!
black hat
2026 60
```

## Slide 61

## Use functions as timing side-channel

61

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Use functions as timing side-channel
15
Coverage
b b
Ww fs
H
N
| ee
e
a
jo)
(o)
20 40 — 60 80 100
i) W
oO j=)
ra)
oO
Calls to procces_obj()
0 20 40 60 80 100
Time (ms) black hat
ysa 61
2026
```

## Slide 62

## Use functions as timing side-channel

**New Coverage**

62

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Use functions as timing side-channel
15
Coverage
b b
Ww fs
H
N
| ee
e
a
jo)
(o)
20 7 60 80 100
W
j=)
i)
oO
ra)
oO
=)
New Coverage
Calls to procces_obj()
0 20 40 60 80 100
Time (ms) black hat
USA 62
2026
```

## Slide 63

## Mapping requires speed

every 100 us

63

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Mapping requires speed
_ 30;
>
3, every 100 us
WY
3 20. |
U
i
ok
£ 10.
a)
o
O
0
0 20 40 60 80 100
black hat
63
2026
```

## Slide 64

## Mapping requires speed

unsafe{ }

64

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Mapping requires speed
) WW
io) (o)
a
o)
Calls to procces_obj()
black hat
64
2026
```

## Slide 65

Accurate mapping

65

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Accurate mapping
1000;
800}
600
Tests
400,
200
correct imprecise Wigelate|
black hat
2026 65
```

## Slide 66

## CAT Fuzzing Architecture

66

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
CAT Fuzzing Architecture
black hat
@ys4 66
```

## Slide 67

# 5 - Findings Vulnerabilities and CVEs

67

## Slide 68

# But first... The RPKI threat model

68

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
But first...
The RPKI threat model
black hat
68
2026
```

## Slide 69

## RPKI requires availability

69

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
RPKI requires availability
—
<— Heil)
black hat
69
2026
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Remote Code Execution
black hat
254. 74
```

## Slide 75

## Cache Poisoning

75

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Cache Poisoning
LP
- AS13335: 1.1.1.0/24
SubjectName: Cloudflare CA
Key: 0x349853
SubjectName: Cloudflare CA
Key: Oxf32856e
black hat
USA 5
2026
```

## Slide 76

## Exploiting DoS

76

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Exploiting DoS
ManifestEntries: [0 elements]
black hat
76
2026
```

## Slide 77

## Key Takeaways

#### Read Paper!

- Fuzzing in batches is efficient in complex cryptographic infrastructures

- Coverage counters serve as sidechannel to map coverage in batches

#### Contact Me!

- Routing security relies on the security of RPKI, which is fragile

77
