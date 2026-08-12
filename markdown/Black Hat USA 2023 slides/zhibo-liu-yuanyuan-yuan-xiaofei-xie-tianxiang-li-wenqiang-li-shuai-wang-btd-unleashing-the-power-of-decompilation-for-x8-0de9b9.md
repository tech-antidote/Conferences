---
title: "BTD Unleashing the Power of Decompilation for x86 Deep Neural Network Executables"
speakers: ["Zhibo Liu", "Yuanyuan Yuan", "Xiaofei Xie", "Tianxiang Li", "Wenqiang Li", "Shuai Wang"]
conference: "Black Hat"
conference_full: "Black Hat USA 2023"
edition: "USA"
year: 2023
source_pdf: "Black Hat USA 2023 slides/Zhibo Liu & Yuanyuan Yuan & Xiaofei Xie & Tianxiang Li & Wenqiang Li & Shuai Wang_BTD Unleashing the Power of Decompilation for x86 Deep Neural Network Executables.pdf"
pages: 41
sha256: "fd7eb80c8625a835cd760e8228edffa8782282d48cb4254f2a5c3fbc02843f84"
text_chars: 10088
ocr_pages: 3
has_ocr: true
redacted_secrets: 0
ocr_confidence: 89.8
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T04:26:37Z"
---
# BTD Unleashing the Power of Decompilation for x86 Deep Neural Network Executables

**Speakers:** Zhibo Liu, Yuanyuan Yuan, Xiaofei Xie, Tianxiang Li, Wenqiang Li, Shuai Wang  
**Conference:** Black Hat USA 2023  
**Source:** `Black Hat USA 2023 slides/Zhibo Liu & Yuanyuan Yuan & Xiaofei Xie & Tianxiang Li & Wenqiang Li & Shuai Wang_BTD Unleashing the Power of Decompilation for x86 Deep Neural Network Executables.pdf` (41 pages)


## Slide 1

# BTD: Unleashing the Power of Decompilation for x86 Deep Neural Network Executables

Zhibo Liu, Yuanyuan Yuan, Xiaofei Xie, Tianxiang Li, Wenqiang Li, Shuai Wang

#BHUSA   @BlackHatEvents

## Slide 2

# Outline

- Background

- Motivation

- Related Work

- Decompiling DNN executables

- Evaluation

2

#BHUSA  @BlackHatEvents

## Slide 3

# Outline

- Background ◁

- Motivation

- Related Work

- Decompiling DNN executables

- Evaluation

3

#BHUSA  @BlackHatEvents

## Slide 4

# DNN Executable

- What is DNN executable?

   - Output of deep learning compilers.

   - Performing the DNN model inference at runtime.

   - In standalone binary format.

Cat!
DNN  DL Compiler DNN
Model Executable

4

#BHUSA  @BlackHatEvents

## Slide 5

# DNN Executable

- Why we need DNN compilation/executable?

   - To fully leverage low-level hardware primitives for fast model inference.

   - To deploy DNN models on heterogeneous hardware devices.

DNN  DL Compiler DNN
Accelerat
Model Executable or

5

#BHUSA  @BlackHatEvents

## Slide 6

# DL Compiler

- Compile high-level models into binary code.

- Can optimize code utilizing domain-specific hardware features (e.g., Intel SIMD) and abstractions.

- Further squeeze (low-power) hardware performance potential.

6

#BHUSA  @BlackHatEvents

## Slide 7

# DL Compiler

- Compilation process typically involves multiple optimization cycles.

DNN compilation pipeline.

7

#BHUSA  @BlackHatEvents

## Slide 8

# DL Compiler

● Many resources from academia and industry have been devoted to this field.

Support from
industry

#### DL compilers

Academic output OSDI’18

**NNFusion**

arXiv

OSDI’20

8

#BHUSA  @BlackHatEvents

## Slide 9

# Real-World Applications

- Low-power processors suppliers (e.g., NXP, Qualcomm) are incorporating DL compilers into their applications

- Cloud service providers (e.g., Amazon and Google) include DL compilers into their DL services to boost performance

<u>https://aws.amazon.com/sagemaker/neo/</u>

9

#BHUSA  @BlackHatEvents

## Slide 10

# Outline

- Background

- Motivation ◁

- Related Work

- Decompiling DNN executables

- Evaluation

10

#BHUSA  @BlackHatEvents

## Slide 11

# Problem

- Currently, DL compiler community mainly focuses on performance

- Our questions:

   - What is the difference between DNN executables and traditional software?

   - How should we safely use DL compilers?

   - What are the potential security risks of using DL compilers?

11

#BHUSA  @BlackHatEvents

## Slide 12

# Problem

● Specifically, should we view a DNN executable as a black-box or white-box?

Is it incomprehensible?

Or is it vulnerable?

Which assumption is true?

12

#BHUSA  @BlackHatEvents

## Slide 13

# Challenges

● The traditional software reverse engineering techniques can hardly tackle DNN executables.

13

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 94/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
black hat
Challenges
e The traditional software reverse engineering techniques can hardly tackle DNN
executables.
1
| as
(a) Glow (b) TVM -O0 (c) TVM -O3 (d) NNFusion
Figure 2: Compare CFGs of a Conv operator in VGG16 compiled by different DL compilers. TVM refers to enabling no
optimization as “-O0” while enabling full optimizations as “-O3”. Glow and NNFusion by default apply full optimizations.
13
```

## Slide 14

# Challenges

## ● Complex data flow during DNN inference.

### Decompile with IDA

14

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 84/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
black hat
Challenges
e Complex data flow during DNN inference.
(__m128)*(unsigned int *)(v7 + 4 * v29 + 1024);
_mm_shuffle_ps(v52, v52, @);
= _mm_add_ps(_mm_mul_ps(*(__m128 *)(v8 + 4 * v42), v53), 9);
V = _mm_add_ps(_mm_mul_ps(*(__m128 *)(v8 + 4 * v45), v53), ye
V = _mm_add_ps(_mm_mul_ps(*(__m128 *)(v8 + 4 * v46), v53), se
v162 = _mm_add_ps(_mm_mul_ps(*(__m1 )(v8 + 4 * yi, V53)i5 5
/163 = _mm_add_ps(_mm_mul_ps(*(__m128 *)(v8 + 4 * ), v53), ye
= _mm_add_ps(_mm_mul_ps(*(__m128 *)(v8 + 4 * v49), v53), 6
= _mm_add_ps(_mm_mul_ps(*(__m128 *)(v8 + 4 * ), V53)5 6)5
(__m128)*(unsigned int *)(v7 + 4 * v29 + 1536);
_mm_shuffle_ps(v54, v54, @);
(__m128)*(unsigned int *)(v7 + 4 * v29 + 2048);
_mm_shuffle_ps(v56, v56, @)3
Decompile with IDA
nou
14
```

## Slide 15

# Challenges

- Hardware-aware optimizations during compilation.

   - memory layout optimization  better memory locality & compatible with SIMD

15

#BHUSA  @BlackHatEvents

## Slide 16

# Outline

- Background

- Motivation

- Related Work ◁

- Decompiling DNN executables

- Evaluation

16

#BHUSA  @BlackHatEvents

## Slide 17

# Related

- Attacking DNN models is not new

- Previous works mainly focus on DL frameworks (e.g., PyTorch and TensorFlow): ○ Cache side channel

   - Power side channel

   - Electromagnetic emanations (EM) side channel

   - Bus snooping

……

17

#BHUSA  @BlackHatEvents

## Slide 18

# Threat Model

## ● Physical access

Have
physical
access
Edge Device,
User
Model IoT Device,
…

18

#BHUSA  @BlackHatEvents

## Slide 19

# Threat Model

## ● Remote access

Can run processes on
the same hardware
Provide Inputs via APIs
Results of Model
Cloud Service  User
Model Inference
Provider

19

#BHUSA  @BlackHatEvents

## Slide 20

# Threat Model

## ● Our assumption: binary access

Can read the
DNN
executable
image directly
Downstream
Tasks
Hardware
Model
Devices

20

#BHUSA  @BlackHatEvents

## Slide 21

# Our Work

- We propose BTD (Bin-To-DNN), the first DNN executable decompiler.

x86 DNN Executable

BTD

DNN Model Specification

21

#BHUSA  @BlackHatEvents

## Slide 22

# Outline

- Background

- Motivation

- Related Work

- Decompiling DNN executables ◁

- Evaluation

22

#BHUSA  @BlackHatEvents

## Slide 23

# Observation

- Differences between DNN executables and general software:

   - Complex data flow (millions of floating-point multiplications in DNN exe)  difficult to summarize

   - But only one execution path!

      -  no path explosion

Give us an opportunity to summarize the semantics from low-level binary code (i.e., floating-point arithmetic)

23

#BHUSA  @BlackHatEvents

## Slide 24

# Observation

## ● Moreover

_DL compilers generate distinct low-level code but retain operator high-level semantics, because DNN operators are generally defined in a clean and rigorous manner._

E.g., mathematical definition of Conv:

24

#BHUSA  @BlackHatEvents

## Slide 25

# Idea

- Summarize the invariant operator semantics with trace-based symbolic execution

25

#BHUSA  @BlackHatEvents

## Slide 26

# Workflow

● BTD consists of 3 steps: operator recovery, topology recovery, dimension & parameter recovery.

- BTD is able to recover full model specification (including operators, topologies, dimensions, and parameters) from DNN executable.

26

#BHUSA  @BlackHatEvents

## Slide 27

# Step 1: Operator Recovery

- We train a LSTM model to map assembly functions to DNN operators.

   - Treat x86 opcodes as language tokens.

   - Segment x86 opcodes using Byte Pair Encoding (BPE).

x86  LSTM DNN
assembly  operator  Conv, ReLU,
function type MatMul, …

Conv Conv
ReLU Pool

27

#BHUSA  @BlackHatEvents

## Slide 28

# Step 2: Topology Recovery

- DL compilers compile DNN operators into assembly functions and pass inputs and outputs as memory pointers through function arguments.

- We hook every call site to record the memory address, and chain operators into computation graph.

Conv ReLU Pool Conv …
Conv ReLU Pool Conv …

28

#BHUSA  @BlackHatEvents

## Slide 29

# Step 3: Dimension & Parameter

- We launch trace-based symbolic execution (SE) to infer dimensions and localize parameters for DNN operators ● We filter trace with taint analysis to only keep parts related to operator output.

SE
assembly  symbolic  Human readable
trace constraints operator semantics

29

#BHUSA  @BlackHatEvents

## Slide 30

# Step 3: Dimension & Parameter

- The gap (offset) between inputs implies the dimension information.

(0x29c4-0x29b8) / sizeof(float) = 3 each row has 3 float values.

30

#BHUSA  @BlackHatEvents

## Slide 31

# Step 3: Dimension & Parameter

● Symbolic constraints extracted from vastly different binaries are mostly consistent.

31

#BHUSA  @BlackHatEvents

## Slide 32

# Step 3: Dimension & Parameter

- We infer operator dimensions (e.g., kernel size, #input channels, #output channels, stride) from extracted symbolic constraints.

- Then instrument the DNN executable to dump parameters (e.g., weights, biases) during execution.

- With all extracted information (i.e., types, topology, dimensions, and parameters), we can rebuild a new model showing identical behavior with the original model.

32

#BHUSA  @BlackHatEvents

## Slide 33

# Implementation

- BTD is open available at: <u>https://github.com/monkbai/DNN-decompiler</u>

● BTD passed the artifact evaluation of USENIX Security With Available, Functional, Reproduced badges

33

#BHUSA  @BlackHatEvents

## Slide 34

# Outline

- Background

- Motivation

- Related Work

- Decompiling DNN executables

- Evaluation ◁

34

#BHUSA  @BlackHatEvents

## Slide 35

# Evaluation

- 8 version of 3 state-of-the-art, production level DL compilers

35

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 92/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Evaluation
e 8 version of 3 state-of-the-art, production level DL compilers
Table 1: Compilers evaluated in our study.
Tool Name
Publication
Developer
Version (git commit)
TYM [20]
Amazon
v0.7.0
v0.8.0
Glow [77]
arXiv
Facebook
2020 (07a82bd9fe97dfd)
2021 (97835cec670bd2f)
2022 (793fec7fb0269db)
NNFusion [58]
Microsoft
v0.2
v0.3
35
```

## Slide 36

# Evaluation

- 7 models cover all operators used in the CV models from ONNX Zoo <u>https://github.com/onnx/models</u>

- real-world image classification models trained on ImageNet

36

#BHUSA  @BlackHatEvents

## Slide 37

# Results

## ● Step 1: DNN operator inference

- Errors can be eliminated by post-checking symbolic constraints, e.g., ○ predicted types  Conv+ReLU

   - but no max operation in constraints

   - remove ReLU label and get the correct Conv type

37

#BHUSA  @BlackHatEvents

## Slide 38

# Results

- Step 3: Parameter layout/dimension inference

- BTD fails on two cases because of DL compiler optimizations (details in our paper)

38

#BHUSA  @BlackHatEvents

## Slide 39

# Results

● Overall, BTD is able to extract functional models in most cases.

● Thus, we can enable white-box attacks (e.g., Adversarial Example, Knowledge Stealing) on a black-box, obscure DNN executable!

39

#BHUSA  @BlackHatEvents

## Slide 40

# Example

- We can use DeepInversion (CVPR’20) to attack a ResNet18 executable decompiled with BTD.

Synthesized Images

- The results are the same as attacking the original model

40

#BHUSA  @BlackHatEvents

## Slide 41

# Thanks!

Q&A

● BTD: <u>https://github.com/monkbai/DNN-decompiler</u>

41

#BHUSA  @BlackHatEvents
