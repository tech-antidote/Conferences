---
title: "The Devil is in the (Micro-) Architectures Uncovering New Side-Channel and Bit-Flip Attack Surfaces in DNN Ex"
speakers: ["Yanzuo Chen", "Zhibo Liu", "Yuanyuan Yuan", "Tianxiang Li", "Sihang Hu", "Zhihui Lin", "Shuai Wang"]
conference: "Black Hat"
conference_full: "Black Hat Europe 2024"
edition: "Europe"
year: 2024
source_pdf: "BlackHat_Europe_2024_slides/Yanzuo Chen & Zhibo Liu & Yuanyuan Yuan & Tianxiang Li & Sihang Hu & Zhihui Lin & Shuai Wang_The Devil is in the (Micro-) Architectures Uncovering New Side-Channel and Bit-Flip Attack Surfaces in DNN Ex.pdf"
pages: 65
sha256: "1b9cce457a3ef6e4ec3c5ce69796dfac287dca64149529a264a9cf9e501de11a"
text_chars: 17143
ocr_pages: 10
has_ocr: true
redacted_secrets: 0
ocr_confidence: 90.0
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T05:01:20Z"
---
# The Devil is in the (Micro-) Architectures Uncovering New Side-Channel and Bit-Flip Attack Surfaces in DNN Ex

**Speakers:** Yanzuo Chen, Zhibo Liu, Yuanyuan Yuan, Tianxiang Li, Sihang Hu, Zhihui Lin, Shuai Wang  
**Conference:** Black Hat Europe 2024  
**Source:** `BlackHat_Europe_2024_slides/Yanzuo Chen & Zhibo Liu & Yuanyuan Yuan & Tianxiang Li & Sihang Hu & Zhihui Lin & Shuai Wang_The Devil is in the (Micro-) Architectures Uncovering New Side-Channel and Bit-Flip Attack Surfaces in DNN Ex.pdf` (65 pages)


## Slide 1

# The Devil is in the (Micro-) Architectures: Uncovering New Side-Channel and Bit-Flip Attack Surfaces in DNN Executables

Speakers:

Yanzuo Chen PhD at HKUST

Zhibo Liu Postdoc at HKUST

#BHEU @BlackHatEvents

## Slide 2

Contributors:

Shuai Wang Associate Professor at HKUST

Yuanyuan Yuan Associate Professor Postdoc at ETH at HKUST Tianxiang Li        Sihang Hu        Zhihui Lin Security Researchers at CSI AI Red Team

#BHEU @BlackHatEvents

## Slide 3

## The Age of AI

• Machine Learning as a Service (MLaaS)

#BHEU @BlackHatEvents

Information Classification: General

3


> Recovered by OCR — confidence 93/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
The Age of Al
¢ Machine Learning as a Service (MLaaS)
Amazon SageMaker Google Cloud
Information Classification: : General 3
```

## Slide 4

## MLaaS

- Run ML models in could

Service  Private
User
Cloud
Provider Model

Valuable Property e.g., design, parameters …

#BHEU @BlackHatEvents

Information Classification: General

4

## Slide 5

## Attacks Arising

- Attacking objectives: **model architectures**

   - e.g., operator types and hyper-parameters

Side Channels
Model architectures
can be stolen.
Cloud User

(Black-box)
Cloud
Model

#BHEU @BlackHatEvents

Information Classification: General

5

## Slide 6

## Attacks Arising

- Model architectures can enable various gray-box attacks

   - e.g., model stealing and bit-flip attack

Model stealing

Bit-flip attack **. . .**

following attacks

more on that later

#BHEU @BlackHatEvents

Information Classification: General

6

## Slide 7

## Meanwhile

- Cloud service providers (e.g., Meta, AWS, and Google) are employing DNN compilation in resource-sharing environments for cost and profit reasons

_Are DNN executables vulnerable to side-channel attacks?_

DL Compilers

#BHEU @BlackHatEvents

Information Classification: General

7

## Slide 8

## Outline

- Background

   - Deep Learning (DL) Compilation

   - • DNN Executable

- How to Steal Model Architectures • Cache Side-Channel

- Making Models Do Bad Stuff • Bit-Flip Attack

#BHEU @BlackHatEvents

Information Classification: General

8

## Slide 9

## DNN Executable

- GPUs are expensive

   - Running DNNs on cost-efficient devices is popular

- DL compilation techniques are proposed to speed up DNN inference

Train

Compile

Deploy

#BHEU @BlackHatEvents

Information Classification: General

9

## Slide 10

## DL Compiler

- Automatically optimize the DNN and generate efficient binary code

- Unlock the full performance potential of various hardware

#BHEU @BlackHatEvents

Information Classification: General

10

## Slide 11

## DNN Executable

- What are the differences compared with DL frameworks (e.g., PyTorch)

   - Each operator is optimized explicitly

   - Standalone

   - No libs during execution

#BHEU @BlackHatEvents

Information Classification: General

11

## Slide 12

## Side-Channel Attacks

- Side-channel attacks on DNNs are emerging

Physical Access Remote Access [Sec’19] Electromagnetic Rowhammer [SP’22] [ASPLOS’20] [Sec’21] Bus Snooping Power [SP’24] [ASPLOS’23] Power [HOST’20] Cache [Sec’20] … …

More discussion: yanzuo.ch/bh24

[CCS’24] DeepCache: Revisiting Cache Side-Channel Attacks in Deep Neural Networks Executables

#BHEU @BlackHatEvents

Information Classification: General

12

## Slide 13

## Side-Channel Attacks

- We focus on remote _model architecture stealing_ attacks

###### Limitation

Rowhammer Leak partial information from quantized DNN Power Rely on RAPL interface (require privileges) Cache Need shared cache (and memory regions) More discussion: yanzuo.ch/bh24

[CCS’24] DeepCache: Revisiting Cache Side-Channel Attacks in Deep Neural Networks Executables

#BHEU @BlackHatEvents

Information Classification: General

13

## Slide 14

## Challenges

- None of existing cache side channel attacks apply to DNN executable

- Why?

   - Standalone

   - No shared memory

- No libs for pre-analysis

- Is DNN executable more secure?

#BHEU @BlackHatEvents

Information Classification: General

14

## Slide 15

## Zoom In

Ø Noise free Ø Simulated with Intel Pin Ø Mimic Prime+Probe

Each **row** represents a cache state (e.g., 64 cache lines).

time

dark pixels à cache hits light pixels à cache misses

#BHEU @BlackHatEvents

Information Classification: General

15

## Slide 16

## Cache Access Patterns

Why is that?

Compiler Optimizations!

#BHEU @BlackHatEvents

Information Classification: General

16


> Recovered by OCR — confidence 93/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Cache Access Patterns
Why is that?
Compiler
Optimizations!
I kernel size: 3 kernel size: 3 kernel size: 1
#input channels: 128 #input channels: 128 ! #input channels: 256
, #output channels: 128 #output channels: 256 #output channels: 512
(a) Conv from ResNet18 (b) Conv from VGG16 (c) Conv from ResNet18
compiled by TVM. compiled by TVM. compiled by Glow.
16
```

## Slide 17

## DL Compiler Optimizations

- Blocking

- For better memory/cache locality

The size of cache is limited (e.g., 32KB)

#BHEU @BlackHatEvents

Information Classification: General

17

## Slide 18

## DL Compiler Optimizations

- Vectorization

- Leverage **S** ingle **I** nstruction **M** ultiple **D** ata (SIMD) extension

SIMD instruction example.

Memory layout optimization.

#BHEU @BlackHatEvents

Information Classification: General

18

## Slide 19

## DL Compiler Optimizations

   - Pseudo code illustration

- Ø Convolution

- Ø Naïve loop structures

- Ø Sweep the whole matrix

#BHEU @BlackHatEvents

Information Classification: General

19

## Slide 20

## DL Compiler Optimizations

- Pseudo code illustration

Optimized loop structures

Loops are split and permutated

#BHEU @BlackHatEvents

Information Classification: General

20

## Slide 21

## Unique Loop Structures

- Compiler optimizations depend on the hyper-parameters of operators.

   - Different operator types and hyper-parameters à

   - Distinct loop structures in compiled low-level code.

- If we can determine the loop structure, we can distinguish operators.

Loops Loops
Loops
Loops
Loops Ops

#BHEU @BlackHatEvents

Information Classification: General

21

## Slide 22

## Unique Loop Structures

- DNN inference involves massive memory accesses, resulting distinguishable cache activities

- We depict binary-level code structures with _LoopI_ (inner loop) and _LoopO_ (outer loop)

   - _LoopI_ denotes the repeated pattern

   - _LoopO_ represents the frequency of a pattern’s occurrence

#BHEU @BlackHatEvents

Information Classification: General

22

## Slide 23

## Unique Loop Structures

Ø There should be a one-to-one mapping relaGon that aHacker can exploit to infer operators.

#BHEU @BlackHatEvents

Information Classification: General

23

## Slide 24

## New Attacking Surface

- Prior works manually locate sensitive functions in linear algebra libraries as target of cache side channels.

- Differently, we reveal that hardware- and cache-aware optimizations introduce new cache side channel leakages.

#BHEU @BlackHatEvents

Information Classification: General

24

## Slide 25

#### DeepCache: End-to-End DNN Architecture Stealing

- We approximate a mapping from cache access traces to loop structures

We match similar record in the identifier database.

Operator **type** , **hyperparameters** , optimized **memory layouts** …

#BHEU @BlackHatEvents

Information Classification: General

25

## Slide 26

## Contrastive Learning

- Extract features cache access traces

E.g., A' =

Traces from the same operator should have similar features. Extracted features are deemed as _LoopI_

#BHEU @BlackHatEvents

Information Classification: General

26

## Slide 27

## Trace Segmentation

- We use encoder-decoder network to segment traces

Compare recovered and original cache trace pieces

Similar:

smooth normal patterns Dissimilar: anomaly! à segment

Idea: frequent normal patterns can quickly be learned.

#BHEU @BlackHatEvents

Information Classification: General

27

## Slide 28

## Trace Segmentation

Encoder: compress the information (of learned patterns) Decoder: recover the original information (uncompress)

Success to recover à the pattern is seen before Fail to recover à the pattern is an anomaly à segmentation point

Sweep the trace to figure out how many times the whole pattern repeated.

#BHEU @BlackHatEvents

Information Classification: General

28

## Slide 29

## Evaluation

- We collect 28 real-world CNN models (372 operators) from ONNX Zoo as database

- All models are compiled with two state-of-the-art DL compilers, TVM and Glow

- ResNet18 and VGG16 as the test set

- Evaluated with L1 and LLC Prime+Probe attack

#BHEU @BlackHatEvents

Information Classification: General

29

## Slide 30

## Results

- Victim

Side-Channel

- Results

   - Op1 à {type: Conv, shape: [256, 256, 3, 3]} Op2 à {type: ReLU} Op3 à {type: MaxPool} Op4 à {type: Conv, shape: [512, 256, 3, 3]} . . .

- Recovered

#BHEU @BlackHatEvents

Information Classification: General

30

## Slide 31

## Results

• L1

• LLC

Why is LLC attack much better?

#BHEU @BlackHatEvents

Information Classification: General

31


> Recovered by OCR — confidence 85/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Results
Table 4: The performance of DEEPCACHE with L1
e L1 Prime+Probe attack in recovering DNN architectures,
and memory layouts.
TVM Glow
ResNet VGG ResNet VGG
Operator Types 95.2% 188.2% | 94.4% 81.3%
Hyperparameters 96.2% 189.5% 71.9% 87.5% |
Mem Layouts 100% 100% | 71.0% 100% 4 I
° LLC Table 5: The performance of DEEPCACHE with LLC attack. S
TaN Sow Why is LLC attack
ResNet VGG | ResNet VGG much better?
Operator Types 95.2% 1 100% 100% 100% | a
Hyperparameters | 92.6% ! 100% 100% 100% |
Information Classification: General 31
```

## Slide 32

## Results

- Why does LLC attack show better accuracy than L1 attack?

- Because some operators are compiled into non-optimal binary code

   - i.e., the binary code shows low memory locality

   - • consequently, low cache hit rate

- From attack’s view, _non-optimal code is difficult to distinguish_

#BHEU @BlackHatEvents

Information Classification: General

32

## Slide 33

## Results

- The cache trace of non-optimal code is featureless

Read 64 KB mem But L1 cache is 32 KB Self-competing

#BHEU @BlackHatEvents

Information Classification: General

33

## Slide 34

Part II: Making Models Do Bad Stuff Speaker: Yanzuo Chen

#BHEU @BlackHatEvents

Information Classification: General

## Slide 35

#BHEU @BlackHatEvents

Information Classification: General


> Recovered by OCR — confidence 94/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Ninja in camouflage 95%
Spooky ghost 4%
Professional chef 1%
```

## Slide 36

#BHEU @BlackHatEvents

Information Classification: General


> Recovered by OCR — confidence 95/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ZS Crime Detector
Yes, putting pineapple on pizza is a crime. It's a violation
of the sacred bond between dough, sauce, and cheese.
While some may argue that the combination of sweet and
savory flavors is delicious, true pizza aficionados know it's
an offense to tradition.
```

## Slide 37

### Attacks on DNNs

- Existing: adversarial examples, data poisoning, backdoors, …

   - More pointers: yanzuo.ch/bh24

- Optimisation problem vs. Attacking through a new dimension

#BHEU @BlackHatEvents

Information Classification: General

37

## Slide 38

xkcd.com/538

#BHEU @BlackHatEvents

Information Classification: General

38


> Recovered by OCR — confidence 88/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
HIS LAPTOP'S ENCRYPTED.
DRUG HIM AND HIT HIM WITH
THIS $5 WRENCH UNTIL
HE TEUS US THE PASSWORD.
\ Gor IT.
)
```

## Slide 39

##### Is there a way?

#BHEU @BlackHatEvents

Information Classification: General

39

## Slide 40

### Attacking DRAM Microarchitectures

- Rowhammer (🎉 Happy 10th Anniversary)

   - Software-triggered hardware bug

   - Current leakage between DRAM cells

   - Flips data bits in memory

#BHEU @BlackHatEvents

Information Classification: General

40

## Slide 41

### Rowhammer in action

- ✅ DDR3

- ✅ DDR4

- ✅ ECC memory

   - ✅ Privilege escalation

   - ✅ Cross-VM attacks

   - ✅ Attacking through browsers

- ✅ (New!) DDR5

#BHEU @BlackHatEvents

Information Classification: General

41

## Slide 42

### Bit-Flip Attacks (BFAs) on DNNs

- Yes, it works

- Targets victim model weights…

   - _What if we don’t have that knowledge?_

#BHEU @BlackHatEvents

Information Classification: General

42

## Slide 43

##### DNN “Executables”

#BHEU @BlackHatEvents

Information Classification: General

43

## Slide 44

##### DNN executables are compiled code

#BHEU @BlackHatEvents

Information Classification: General

44

## Slide 45

### The Setup

- **Attacker objective** : deplete model intelligence via BFAs (E.g., make them random guessers)

- **Attacker knowledge** : Model structure => model executable

- E.g., with DeepCache (Our Part I) / BTD (Zhibo@BH-USA24)

- • Attacker has **no** access to victim model weights

- We figure out: **How** to find bits to flip

#BHEU @BlackHatEvents

Information Classification: General

45

## Slide 46

### Attack Flow

Knowledge
↓
Bits to flip
📄⚙ 🔨
📄
🔍 ⚙
Locally  generated
😈
model/executable
Local (attacker) Remote (victim)
environment 😈 environment

#BHEU @BlackHatEvents

Information Classification: General

46

## Slide 47

### Previous Attacks

Knows: structure & weights & gradients & setup…
🔨
📄⚙ 🔨
📄
🔍 ⚙
Locally  generated
😈
model/executable
Local (attacker) Remote (victim)
environment 😈 environment

#BHEU @BlackHatEvents

Information Classification: General

47

## Slide 48

Knows: structure  & weights & gradients & setup…
🔨
📄⚙ 🔨
📄
🔍 😶🌫⚙
Locally  generated
😈
model/executable
Local (attacker) Remote (victim)
environment 😈 environment

### Our Attack

#BHEU @BlackHatEvents

Information Classification: General

48

## Slide 49

#BHEU @BlackHatEvents

Information Classification: General

49

## Slide 50

- Randomly choose one bit within the code region

- • Flip it

- See what happens

- • 🔄 Loop

#BHEU @BlackHatEvents

Information Classification: General

50

## Slide 51

##### ASR: 2%

#BHEU @BlackHatEvents

Information Classification: General

51

## Slide 52

### The Remaining 98%

- Most of them → Crash

- Some of them → No effect

###### Function already returned

#BHEU @BlackHatEvents

Information Classification: General

52

## Slide 53

##### But: That 2%

#BHEU @BlackHatEvents

Information Classification: General

53

## Slide 54

### Take 2: Using those 2% of bits

🔍⚙ **Locally** generated 😈 model/executable Local (attacker) environment

- Compile & train the model on an arbitrary dataset

   - Can't use victim dataset (we don't know it)

- Scan all bits and record those useful

- Remote: Try useful bits on victim executable

#BHEU @BlackHatEvents

Information Classification: General

54

## Slide 55

### ASR: 45%

- 45% of time (or bits) lead to successful degradation

- • Rest of the time: Crash or no effect

- _Why not 100% ASR?_

   - Model weights are different.

#BHEU @BlackHatEvents

Information Classification: General

55

## Slide 56

💡 Transferable vulnerable bits

45% vulnerable bits transferable to victim model, _despite_ different training sets

#BHEU @BlackHatEvents

Information Classification: General

56

## Slide 57

### Take 3: In seek of “Superbits”

- Using _more_ local executables for profiling?

😈

#BHEU @BlackHatEvents

Information Classification: General

57

## Slide 58

### Building More Local Executables

- Train them on datasets of random noise

   - Regulates weights

   - “Unbiased” choice

      - (More refs: yanzuo.ch/bh24)

#BHEU @BlackHatEvents

Information Classification: General

58

## Slide 59

### ASR: 70%

To here
We went from here

#BHEU @BlackHatEvents

Information Classification: General

59


> Recovered by OCR — confidence 83/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ASR: 70%
\
80
3 70
= 50
2 To here
Z jBasel —— We went from here
2 aseline
Number of Fake Datasets Used
Information Classification: General 59
```

## Slide 60

### Real World Experiments

#BHEU @BlackHatEvents

Information Classification: General

60


> Recovered by OCR — confidence 86/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Real World Experiments
Model Dataset | #Flips | #Crashes | %Acc. Change
ResNet50 CIFAR10 1.4 0.0 87.20 — 10.00 —
GoogLeNet CIFAR10 1.4 0.0 84.80 — 10.00
DenseNet121 CIFAR10 1.0 0.0 80.00 — 11.40
DenseNet121 MNIST 1.2 0.0 99.10 — 11.20
DenseNet121 Fashion 1.2 0.0 92.50 — 10.60
QResNet50 CIFAR10 1.6 0.0 86.90 — 9.60
QGoogLeNet CIFAR10 1.4 0.0 84.60 — 11.20
QDenseNet121 | CIFARI0O 1.6 0.0 78.50 — 10.20
ResNet50 CIFAR10 1.4 0.0 78.80 — 10.00 —
```

## Slide 61

### Real World Experiments

Avg: ~1.4 flips to success

#BHEU @BlackHatEvents

Information Classification: General

61


> Recovered by OCR — confidence 89/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Real World Experiments
Model Dataset || #Flips || #Crashes | %Acc. Change
ResNet50 CIFAR10 1.4 0.0 87.20 — 10.00
GoogLeNet CIFAR10 1.4 0.0 84.80 — 10.00
DenseNet121 CIFAR10 1.0 0.0 80.00 — 11.40
DenseNet121 MNIST 1.2 0.0 99.10 — 11.20
DenseNet121 Fashion 1.2 0.0 92.50 — 10.60
QResNet50 CIFAR10 1.6 0.0 86.90 — 9.60
QGoogLeNet | CIFARIO 1.4 0.0 84.60 — 11.20
QDenseNet121 | CIFARI0O 1.6 0.0 78.50 — 10.20
ResNet50 CIFAR10 1.4 0.0 78.80 — 10.00
Avg: ~1.4 flips to success
Information Classification: General 1 61
```

## Slide 62

Comparison: DeepHammer’s Results

Avg: ~12 flips

#BHEU @BlackHatEvents

Information Classification: General

62


> Recovered by OCR — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Comparison: DeepHammer’s Results
Dataset Architecture Network Acc. before Random Guess Acc. after Min. # of
Parameters Attack (%) Acc. (%) Attack (%) | Bit-flips
Fashion MNIST LeNet 0.65M 90.20 10.00 10.00 3
Google VGG-11 132M 96.36 333 3.43 5
Speech Command VGG-13 133M 96.38 , 3.25 7
ResNet-20 0.27M 90.70 10.92 21
AlexNet 61M 84.40 10.46 5
CIFAR-10 VGG-11 132M 89.40 10.00 10.27 3
VGG-16 138M 93.24 10.82 13
SqueezeNet 1.2M 57.00 0.16 18
MobileNet-V2 2.1M 72.01 0.19 2
ImageNet ResNet-18 11M 69.52 0.10 0.19 24
ResNet-34 21M 72.78 0.18 23
ResNet-50 23M 75.56 0.17 23
Avg: ~12 flips
Information Classification: General 62
```

## Slide 63

### Bonus: Case Study

In this case:

- Operand of _cmp_ flipped

- Hard to defend with existing methods (e.g., optimisation)

- Learn more: yanzuo.ch/bh24

#BHEU @BlackHatEvents

Information Classification: General

63

## Slide 64

## Black Hat Sound Bytes

- DeepCache: Optimisations gave away model architectures

- BFA: 6x fewer flips to ruin model intelligence

- More security research on DNN executables please

#BHEU @BlackHatEvents

Information Classification: General

64

## Slide 65

## Thanks!

Yanzuo Chen ychenjo@cse.ust.hk

Zhibo Liu zhiboliu@ust.hk

Learn More <u>yanzuo.ch/bh24</u>

#BHEU @BlackHatEvents

Information Classification: General

65
