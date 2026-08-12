---
title: "Collide+Power The Evolution of Software-based Power Side-Channels Attacks"
speakers: ["Andreas Kogler"]
conference: "Black Hat"
conference_full: "Black Hat Europe 2023"
edition: "Europe"
year: 2023
source_pdf: "Black Hat Europe 2023 slides/Andreas Kogler_Collide+Power The Evolution of Software-based Power Side-Channels Attacks.pdf"
pages: 141
sha256: "d8efcaf68526c309c9b242e8a2cb6c2167bc06c34cd85c5837db3a90232612c8"
text_chars: 26405
ocr_pages: 1
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:09:41Z"
---
# Collide+Power The Evolution of Software-based Power Side-Channels Attacks

**Speakers:** Andreas Kogler  
**Conference:** Black Hat Europe 2023  
**Source:** `Black Hat Europe 2023 slides/Andreas Kogler_Collide+Power The Evolution of Software-based Power Side-Channels Attacks.pdf` (141 pages)


## Slide 1

# **Collide+Power**

The Evolution of Software-based Power Side-Channels Attacks

**Andreas Kogler Graz University of Technology**

6th December 2023

## Slide 2

**Whoami**

• **Andreas Kogler**

1

� 0xhilbert

� andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 3

### **Whoami**

- **Andreas Kogler**

- • PhD-Candidate - Graz University of Technology

1

� 0xhilbert

� andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 4

### **Whoami**

- **Andreas Kogler**

- PhD-Candidate - Graz University of Technology

   - Software-based power side channels

   - Software-based fault attacks

   - Trusted execution environments

1

� 0xhilbert

� andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 5

### **Whoami**

- **Andreas Kogler**

- PhD-Candidate - Graz University of Technology

   - Software-based power side channels

   - Software-based fault attacks

   - Trusted execution environments

1

� 0xhilbert

� andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 6

**Motivation**

2

� 0xhilbert � andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 7

**Motivation**

#### **Software-based Power Side Channels**

2

� 0xhilbert � andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 8

### **Motivation**

#### **Software-based Power Side Channels**

- **Specific** targets: Algorithms

2

� 0xhilbert

� andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 9

### **Motivation**

#### **Software-based Power Side Channels**

- **Specific** targets: Algorithms

- Leak edge cases

2

� 0xhilbert

� andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 10

### **Motivation**

#### **Software-based Power Side Channels**

- **Specific** targets: Algorithms

- Leak edge cases

- **Limited** to a side channels

2

� 0xhilbert � andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 11

**Motivation**

#### **Software-based Power Side Channels**

#### **Transient Execution Attacks**

- **Specific** targets: Algorithms

- Leak edge cases

- **Limited** to a side channels

2

� 0xhilbert

� andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 12

**Motivation**

#### **Software-based Power Side Channels**

- **Specific** targets: Algorithms

#### **Transient Execution Attacks**

   - **Generic** targets: CPU components

- Leak edge cases

- **Limited** to a side channels

2

� 0xhilbert

� andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 13

**Motivation**

#### **Software-based Power Side Channels**

- **Specific** targets: Algorithms

- Leak edge cases

#### **Transient Execution Attacks**

   - **Generic** targets: CPU components

   - Leak arbitrary data

- **Limited** to a side channels

2

� 0xhilbert

� andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 14

**Motivation**

#### **Software-based Power Side Channels**

- **Specific** targets: Algorithms

- Leak edge cases

- **Limited** to a side channels

#### **Transient Execution Attacks**

- **Generic** targets: CPU components

- Leak arbitrary data

- **Agnostic** to side channels

� 0xhilbert

2

� andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 15

**Motivation**

- **Software-based Power Side ChannelsCollide+PowerTransient Execution Attacks** • **Specific** targets: Algorithms • **Generic** targets: CPU components • Leak edge cases • Leak arbitrary data • **Limited** to a side channels • **Agnostic** to side channels

   - **Limited** to a side channels

2

Andreas Kogler � 0xhilbert � andreas.kogler@iaik.tugraz.at

## Slide 16

**Can we build a generic software-based power side-channel attack independent of the targeted application?**

## Slide 17

## Slide 18

**Power Leakage - Source**

- **C** omplementary **M** etal **O** xide **S** emiconductor

3

� 0xhilbert

� andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 19

**Power Leakage - Source**

- **C** omplementary **M** etal **O** xide **S** emiconductor

- • Low power consumption

3

� 0xhilbert

� andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 20

**Power Leakage - Source**

- **C** omplementary **M** etal **O** xide **S** emiconductor

- • Low power consumption • Depends on:

3

� 0xhilbert

� andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 21

**Power Leakage - Source**

- **C** omplementary **M** etal **O** xide **S** emiconductor

- Low power consumption

- Depends on:

   - **Instruction** that is executed

3

� 0xhilbert

� andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 22

**Power Leakage - Source**

- **C** omplementary **M** etal **O** xide **S** emiconductor

- Low power consumption

- Depends on:

   - **Instruction** that is executed

   - **Data** that is being processed

3

� 0xhilbert

� andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 23

**Traditional Power Side Channels**

## Slide 24

**Power Side Channel - Setup**

Oscilloscope
Computer
> python measure.py
collecting power traces... DONE
post-processing... DONE
testing key candidates...
Current Probe
+  -
Microprocessor

Credits for theAndreasimageKoglerto: Robert� 0xhilbertPrimas � andreas.kogler@iaik.tugraz.at

4

## Slide 25

**How can we measure the power consumption of a modern CPU?**

**How would we ever do this remotely?**

## Slide 26

## Slide 27

## **PLATYPUS**<sup>1</sup>

> 1Moritz Lipp, Andreas Kogler, David Oswald, Michael Schwarz, Catherine Easdon, Claudio Canella, and Daniel Gruss. PLATYPUS: Software-based Power Side-Channel Attacks on x86. In: S&P. 2021.

## Slide 28

**Running Average Power Limit (RAPL)**

#### Unprivileged power meter

6

� 0xhilbert

� andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 29

**Running Average Power Limit (RAPL)**

Unprivileged power meter

No physical access

6

� 0xhilbert � andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 30

**Running Average Power Limit (RAPL)**

Unprivileged power meter

No physical access

Low refresh rate

6

� 0xhilbert

� andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 31

**External Measurement Equipment vs RAPL**

� 0xhilbert � andreas.kogler@iaik.tugraz.at

7

Andreas Kogler

## Slide 32

**External Measurement Equipment vs RAPL**

� 0xhilbert � andreas.kogler@iaik.tugraz.at

7

Andreas Kogler

## Slide 33

### **External Measurement Equipment vs RAPL**

- **Full** Control

� 0xhilbert � andreas.kogler@iaik.tugraz.at

7

Andreas Kogler

## Slide 34

### **External Measurement Equipment vs RAPL**

- **Full** Control

- **High** timing resolution

� 0xhilbert

� andreas.kogler@iaik.tugraz.at

7

Andreas Kogler

## Slide 35

### **External Measurement Equipment vs RAPL**

- **Full** Control

- **High** timing resolution

- _→_ Multiple samples per instruction

� 0xhilbert

� andreas.kogler@iaik.tugraz.at

7

Andreas Kogler

## Slide 36

### **External Measurement Equipment vs RAPL**

- **Full** Control

   - **No** control, just a register

- **High** timing resolution

- _→_ Multiple samples per instruction

� 0xhilbert

� andreas.kogler@iaik.tugraz.at

7

Andreas Kogler

## Slide 37

### **External Measurement Equipment vs RAPL**

- **Full** Control

   - **No** control, just a register

- **High** timing resolution

   - **Low** timing resolution

- _→_ Multiple samples per instruction

� 0xhilbert

� andreas.kogler@iaik.tugraz.at

7

Andreas Kogler

## Slide 38

### **External Measurement Equipment vs RAPL**

- **Full** Control

   - **No** control, just a register

- **High** timing resolution

   - **Low** timing resolution

- _→_ Multiple samples per instruction

- _→_ Single sample per multiple instructions

� 0xhilbert � andreas.kogler@iaik.tugraz.at

7

Andreas Kogler

## Slide 39

### **Distinguishing Instructions**

• Measure the energy consumption of different instructions
clflush
1,000 mov r64,mem
fscale
rdrand
rdtsc
500
1,020 1,040 1,060 1,080 1,100 1,120 1,140 1,160 1,180 1,200 1,220 1,240 1,260 1,280
Energy [pJ]
Number ofcases

8

Andreas Kogler � 0xhilbert � andreas.kogler@iaik.tugraz.at

## Slide 40

### **Distinguishing Operands**

• Measure the energy consumption of different operands
0x00 0xFF
150 0x0F 0x3F
0x03
100
50
0
0.234 0.236 0.238 0.240 0.242 0.244 0.246 0.248 0.250 0.252
Energy [J]
Density

9

� 0xhilbert � andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 41

### **Breaking KASLR**

10

� 0xhilbert � andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 42

**Breaking KASLR**

10

� 0xhilbert � andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 43

**Breaking KASLR**

10

� 0xhilbert � andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 44

**Breaking KASLR**

10

� 0xhilbert � andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 45

### **Breaking KASLR**

10

� 0xhilbert � andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 46

**Breaking KASLR**

10

� 0xhilbert � andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 47

**Breaking KASLR**

10

� 0xhilbert � andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 48

### **Breaking KASLR**

10

� 0xhilbert � andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 49

**Breaking KASLR**

10

� 0xhilbert � andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 50

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
RI
@hp /tmp/kastr
100000 |
60000
FH gs gs
es ee,
oe one ae
a eee
it tee
aoe5
ee ee
ae ge “A
```

## Slide 51

## Slide 52

## Slide 53

**The end?**

## Slide 54

## **Hertzbleed**<sup>23</sup>

> 2Yingchen Wang, Riccardo Paccagnella, Elizabeth He, Hovav Shacham, Christopher W. Fletcher, and David Kohlbrenner. Hertzbleed: Turning Power Side-Channel Attacks Into Remote Timing Attacks on x86. In: USENIX Security. 2022.

> 3Chen Liu, Abhishek Chakraborty, Nikhil Chawla, and Neer Roggel. Frequency throttling side-channel attack. In: CCS. 2022.

## Slide 55

### **CPU Power Management**

- CPU power management is complex

13

� 0xhilbert � andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 56

### **CPU Power Management**

- CPU power management is complex

- In order to save power, you can . . .

13

� 0xhilbert

� andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 57

### **CPU Power Management**

- CPU power management is complex

- In order to save power, you can . . .

Shut down resources

13

� 0xhilbert � andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 58

### **CPU Power Management**

- CPU power management is complex

- In order to save power, you can . . .

Shut down resources

Reduce voltage

13

� 0xhilbert

� andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 59

### **CPU Power Management**

- CPU power management is complex

- In order to save power, you can . . .

Shut down resources

Reduce voltage

Reduce frequency

13

� 0xhilbert � andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 60

### **CPU Power Management**

- CPU power management is complex

- In order to save power, you can . . .

Shut down resources

Reduce voltage

**Reduce frequency**

13

� 0xhilbert � andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 61

**Hertzbleed Effect**

14

� 0xhilbert � andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 62

**Hertzbleed Effect**

14

� 0xhilbert � andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 63

**Hertzbleed Effect**

- Consumes **more** energy

14

� 0xhilbert � andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 64

**Hertzbleed Effect**

- Consumes **more** energy

- Consumes **less** energy

14

� 0xhilbert

� andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 65

**Hertzbleed Effect**

- Consumes **more** energy

   - Consumes **less** energy

- **Reaches** power limit after some time

14

� 0xhilbert

� andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 66

**Hertzbleed Effect**

- Consumes **more** energy

- **Reaches** power limit after some time

- Consumes **less** energy

- **Never reaches** power limit

14

� 0xhilbert

� andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 67

**Hertzbleed Effect**

- Consumes **more** energy

- **Reaches** power limit after some time

   - Consumes **less** energy

   - **Never reaches** power limit

- Throttling occurs

14

� 0xhilbert

� andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 68

**Hertzbleed Effect**

- Consumes **more** energy

- **Reaches** power limit after some time

- Throttling occurs

- Consumes **less** energy

- **Never reaches** power limit

- No throttling

14

� 0xhilbert

� andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 69

**Hertzbleed Effect**

- Consumes **more** energy

- **Reaches** power limit after some time

- Throttling occurs

   - Consumes **less** energy

   - **Never reaches** power limit

   - No throttling

- _→_ Slowdown

14

� 0xhilbert

� andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 70

**Hertzbleed Effect**

- Consumes **more** energy

- **Reaches** power limit after some time

- Throttling occurs

- _→_ Slowdown

- Consumes **less** energy

- **Never reaches** power limit

- No throttling

- _→_ No slowdown

14

� 0xhilbert

� andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 71

**Hertzbleed Effect - Without Power Limit**

Energy

Time

15

� 0xhilbert � andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 72

**Hertzbleed Effect - With Power Limit**

Energy

Time

16

� 0xhilbert � andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 73

## Slide 74

## **GPU Throttling**<sup>45</sup>

> 4Yingchen Wang, Riccardo Paccagnella, Alan Wandke, Zhao Gang, Grant Garrett-Grossman, Christopher W Fletcher, David Kohlbrenner, and Hovav Shacham. DVFS frequently leaks secrets: Hertzbleed attacks beyond SIKE, cryptography, and CPU-only data. In: S&P. 2023.

> 5Hritvik Taneja, Jason Kim, Jie Jeff Xu, Stephan van Schaik, Daniel Genkin, and Yuval Yarom. Hot Pixels: Frequency, Power, and Temperature Attacks on GPUs and ARM SoCs. In: USENIX Security.

## Slide 75

### **GPU Throttling**

#### • **Integrated** GPUs share power limits with the CPU

17

� 0xhilbert

� andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 76

### **GPU Throttling**

- **Integrated** GPUs share power limits with the CPU _→_ **CPU throttling** indicates high GPU consumption

17

� 0xhilbert � andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 77

### **GPU Throttling**

- **Integrated** GPUs share power limits with the CPU

- _→_ **CPU throttling** indicates high GPU consumption

- • **Dedicated** GPUs have power limits too

17

� 0xhilbert

� andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 78

### **GPU Throttling**

- **Integrated** GPUs share power limits with the CPU _→_ **CPU throttling** indicates high GPU consumption

- **Dedicated** GPUs have power limits too

   - _→_ **Observable** by timing a GPU workload

17

� 0xhilbert

� andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 79

### **Pixel Stealing**

• What secrets are _“inside”_ a GPU?

18

� 0xhilbert

� andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 80

### **Pixel Stealing**

- What secrets are _“inside”_ a GPU?

   - GPU renders windows and screen

18

� 0xhilbert

� andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 81

### **Pixel Stealing**

- What secrets are _“inside”_ a GPU?

   - GPU renders windows and screen

   - _→_ **Privacy** related information

18

� 0xhilbert

� andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 82

**Pixel Stealing**

- What secrets are _“inside”_ a GPU?

   - GPU renders windows and screen

   - _→_ **Privacy** related information

- **Pixel** color represents the information

18

� 0xhilbert � andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 83

**Pixel Stealing**

• **Post-processing** without revealing the pixels

19

� 0xhilbert

� andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 84

**Pixel Stealing**

- **Post-processing** without revealing the pixels

- • Pixel value is the **data operand**

19

� 0xhilbert

� andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 85

**Pixel Stealing**

- **Post-processing** without revealing the pixels

- • Pixel value is the **data operand** • Distinguishable power consumption

19

� 0xhilbert

� andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 86

**Pixel Stealing**

- **Post-processing** without revealing the pixels

- • Pixel value is the **data operand** • Distinguishable power consumption

   - **Bright** pixel _→_ less power

19

� 0xhilbert

� andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 87

**Pixel Stealing**

- **Post-processing** without revealing the pixels

- • Pixel value is the **data operand** • Distinguishable power consumption

   - **Bright** pixel _→_ less power

   - **Dark** pixel _→_ more power

19

� 0xhilbert

� andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 88

### **Pixel Stealing**

- **Post-processing** without revealing the pixels

- Pixel value is the **data operand**

- Distinguishable power consumption

   - **Bright** pixel _→_ less power

   - **Dark** pixel _→_ more power

- _→_ Measure timing and infer pixel value

19

� 0xhilbert � andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 89

**How can we transform power side channels towards a broader scope?**

## Slide 90

## **Collide+Power**<sup>6</sup>

> 6Andreas Kogler, Jonas Juffinger, Lukas Giner, Lukas Gerlach, Martin Schwarzl, Michael Schwarz, Daniel Gruss, and Stefan Mangard. Collide+Power: Leaking Inaccessible Data with Software-based Power Side Channels. In: USENIX Security. 2023.

## Slide 91

### **Collide+Power - Memory Subsystem**

Way1 Way2 Way3 Way4 Way5 Way W Attacker
. . .
Set1 G
. . .
Set2 Victim
... ... ... ... ... ... V
. . .
Set N

20

Andreas Kogler � 0xhilbert � andreas.kogler@iaik.tugraz.at

## Slide 92

### **Collide+Power - Memory Subsystem**

Way1 Way2 Way3 Way4 Way5 Way W Attacker
. . .
Set1 G
. . .
Set2 Victim
... ... ... ... ... ... V
. . .
Set N

20

Andreas Kogler � 0xhilbert � andreas.kogler@iaik.tugraz.at

## Slide 93

### **Collide+Power - Memory Subsystem**

Way1 Way2 Way3 Way4 Way5 Way W Attacker
. . .
Set1 G
. . .
Set2 Victim
... ... ... ... ... ... V
. . .
Set N

20

Andreas Kogler � 0xhilbert � andreas.kogler@iaik.tugraz.at

## Slide 94

**Power Leakage - Model Components**

21

� 0xhilbert � andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 95

**Power Leakage - Model Components**

**Hamming Weight:** hw( _x_ )

21

� 0xhilbert � andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 96

**Power Leakage - Model Components**

**Hamming Weight:** hw( _x_ ) Number of set bits

21

� 0xhilbert � andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 97

**Power Leakage - Model Components**

**Hamming Weight:** hw( _x_ ) Number of set bits hw(112) = 2

21

� 0xhilbert � andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 98

### **Power Leakage - Model Components**

**Hamming Weight:** hw( _x_ ) Number of set bits hw(112) = 2

**Hamming Distance:** hd( _x_ , _y_ )

21

� 0xhilbert � andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 99

### **Power Leakage - Model Components**

**Hamming Weight:** hw( _x_ ) Number of set bits hw(112) = 2

**Hamming Distance:** hd( _x_ , _y_ ) Number of different bits

21

� 0xhilbert � andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 100

### **Power Leakage - Model Components**

**Hamming Weight:** hw( _x_ ) **Hamming Distance:** hd( _x_ , _y_ ) Number of set bits Number of different bits hw(112) = 2 hd(112, 012) = 1

21

� 0xhilbert � andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 101

### **Collide+Power - Memory Subsystem**

Way1 Way2 Way3 Way4 Way5 Way W Attacker
. . .
Set1 G
. . .
Set2 Victim
... ... ... ... ... ... V
. . .
Set N

22

Andreas Kogler � 0xhilbert � andreas.kogler@iaik.tugraz.at

## Slide 102

### **Collide+Power - Memory Subsystem**

Way1 Way2 Way3 Way4 Way5 Way W Attacker
Set1 hd( 1010 0101 ) = 4 . . . G
. . .
Set2 Victim
0101
... hd(... .. . . . . 0101 ) = 0... .. . V
. . .
Set N

22

� 0xhilbert � andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 103

### **Collide+Power - Memory Subsystem**

Way1 Way2 Way3 Way4 Way5 Way W Attacker
Set1 hd( 1010 0101 ) = 4 . . . G
. . .
Set2 Victim
0101
... hd(... .. . . . . 0101 ) = 0... .. . V
. . .
Set N
Buthowdoweexploitthis?

22

� 0xhilbert � andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 104

**Collide+Power - Intuition**

_P_ ( _G_ , _V_ ) _≈ . . ._

23

� 0xhilbert � andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 105

**Collide+Power - Intuition**

_P_ ( _G_ , _V_ ) _≈_ hd( _G_ , _V_ )

23

� 0xhilbert � andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 106

**Collide+Power - Intuition**

_P_ ( _G_ , _V_ ) _≈_ hd( _G_ , _V_ )

23

� 0xhilbert � andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 107

**Collide+Power - Intuition**

_P_ <u>(</u> _G_ , _V_ ) _≈_ hd( _G_ , _V_ ) � <u>� ��</u> model

23

� 0xhilbert � andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 108

**Collide+Power - Intuition**

P ( G ,  V ) ≈ hd( G ,  V )
� � � �
�� ��
model signal

23

� 0xhilbert � andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 109

### **Collide+Power - Example**

_P_ ( _G_ , 01012) _≈_ hd( _G_ , 01012) `0b1000 0b0100 0b0010 0b0001` Guess _G_

24

Andreas Kogler � 0xhilbert � andreas.kogler@iaik.tugraz.at

## Slide 110

### **Collide+Power - Example**

_P_ (10002, 01012) _≈_ hd( **1** 0002, **0** 1012) = 3 `0b1000 0b0100 0b0010 0b0001` Guess _G_

24

Andreas Kogler � 0xhilbert � andreas.kogler@iaik.tugraz.at

## Slide 111

### **Collide+Power - Example**

P (01002, 01012)  ≈ hd(0 1 002, 0 1 012) = 1
0b1000 0b0100 0b0010 0b0001
Guess G
() GP V ,

24

Andreas Kogler � 0xhilbert � andreas.kogler@iaik.tugraz.at

## Slide 112

Collide+Power - Example
P (00102, 01012)  ≈ hd(00 1 02, 01 0 12) = 3
0b1000 0b0100 0b0010 0b0001
Guess G
() GP V ,

24

Andreas Kogler � 0xhilbert � andreas.kogler@iaik.tugraz.at

## Slide 113

Collide+Power - Example
P (00012, 01012)  ≈ hd(000 1 2, 010 1 2) = 1
0b1000 0b0100 0b0010 0b0001
Guess G
() GP V ,

24

Andreas Kogler � 0xhilbert

� andreas.kogler@iaik.tugraz.at

## Slide 114

### **Leakage Analysis - Generalization**

B32 B32 B32
B31 B31 B31
GL VL GL
B0 B0 B0

#### Aligned Leakage

B63 B63
GU VU
B32 B32
B31 B31
GL VL
B0 B0

25

Andreas Kogler � 0xhilbert � andreas.kogler@iaik.tugraz.at

## Slide 115

### **Leakage Analysis - Generalization**

B32
B31
GL
B0

Aligned Leakage Cross Leakage
B63 B63 B63 B63
GU VU GU VU
B32 B32 B32 B32
B31 B31 B31 B31
GL VL GL VL
B0 B0 B0 B0

25

Andreas Kogler � 0xhilbert � andreas.kogler@iaik.tugraz.at

## Slide 116

### **Leakage Analysis - Generalization**

Aligned Leakage Cross Leakage Self Leakage
B63 B63 B63 B63 B63 B63
GU VU GU VU GU VU
B32 B32 B32 B32 B32 B32
B31 B31 B31 B31 B31 B31
GL VL GL VL GL VL
B0 B0 B0 B0 B0 B0

25

Andreas Kogler � 0xhilbert � andreas.kogler@iaik.tugraz.at

## Slide 117

### **Leakage Analysis: Results**

Effectiveness Aligned Leakage Cross Leakage Self Leakage Weights
ρ ˆ SNR A hd( vL ,  gL ) hd( vU ,  gU ) hd( vL ,  gU ) hd( vU ,  gL ) hd( vL ,  vU ) hd( gL ,  gU ) hw( vL ) hw( vU ) hw( gL ) hw( gU )
· 1 · 10 − 3 a 0 in µW a 1 in µW c 0 in µW c 1 in µW s 0 in µW s 1 in µW w 0 in µW w 1 in µW w 2 in µW w 3 in µW
None 0.311 72.004 544.5 4.2 1.1 0.5 0.0 0.0 0.0 0.0 362.6 0.0
L1 0.907 7.873 598.3 278.8 0.0 0.0 0.0 0.0 0.0 0.0 6124.4 2696.9
L1+L2 0.822 5.632 339.3 141.7 106.6 89.4 0.0 0.0 0.0 0.0 3750.7 1435.0
None 0.003 0.000 0.0 0.8 0.0 5.7 0.0 0.0 0.0 0.0 1.7 2.8
L1 0.370 11.365 136.7 133.9 1.9 0.1 0.0 0.0 0.0 0.0 454.1 455.5
L1+L2 0.300 5.294 80.5 86.9 40.9 43.0 0.0 0.0 0.0 0.0 334.0 332.5
None 0.003 0.000 0.0 0.0 0.0 3.1 0.0 0.0 0.0 0.0 7.0 0.0
L1 0.241 3.876 63.3 74.5 4.9 9.6 0.0 0.0 0.0 0.0 204.6 303.2
L1+L2 0.450 6.457 133.7 169.0 84.7 86.2 0.0 0.0 0.0 0.0 347.1 1130.5
Do not start reading this!
Inst. Evict.
Load
Prefetch
Store

26

Andreas Kogler � 0xhilbert � andreas.kogler@iaik.tugraz.at

## Slide 118

**Generic Attacks**

## Slide 119

### **MDS-style Attack**

Victim:
� access( V )
Thread

Internal Caches
. . .
. . .
... ... ... ...
. . .
CorePhysical

27

Andreas Kogler � 0xhilbert � andreas.kogler@iaik.tugraz.at

## Slide 120

### **MDS-style Attack**

Victim:
� access( V )
Thread

Internal Caches
Attacker:
. . .
� prime( G )
. . .
... ... ... ...
. . .
Thread
CorePhysical

27

Andreas Kogler � 0xhilbert � andreas.kogler@iaik.tugraz.at

## Slide 121

### **MDS-style Attack**

Internal Caches
Attacker:
. . .
� prime( G )
. . .
... ... ... ...
Victim:
� access( V ) . . .
Thread
CorePhysical
Thread

27

� 0xhilbert � andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 122

### **MDS-style Attack**

Internal Caches
Attacker:
. . .
� prime( G )
. . .
... ... ... ...
Victim:
� access( V ) . . .
Thread
CorePhysical
Thread

27

� 0xhilbert � andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 123

### **Meltdown-style Attack**

Victim (Kernel):
PHT/RSB( V )

Internal Caches
. . .
. . .
... ... ... ...
. . .
Thread
CorePhysical

28

Andreas Kogler � 0xhilbert � andreas.kogler@iaik.tugraz.at

## Slide 124

### **Meltdown-style Attack**

Victim (Kernel):
PHT/RSB( V )

Internal Caches
Attacker (Userspace):
. . .
prime( G )
. . .
... ... ... ...
. . .
Thread
CorePhysical

28

Andreas Kogler � 0xhilbert � andreas.kogler@iaik.tugraz.at

## Slide 125

### **Meltdown-style Attack**

Internal Caches
Attacker (Userspace):
. . .
prime( G )
. . .
... ... ... ...
Victim (Kernel):
PHT/RSB( V ) . . .
Thread
CorePhysical

28

� 0xhilbert � andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 126

### **Meltdown-style Attack**

Internal Caches
Attacker (Userspace):
. . .
prime( G )
. . .
... ... ... ...
Victim (Kernel):
PHT/RSB( V ) . . .
Thread
CorePhysical

28

� 0xhilbert � andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 127

**This must be slow?**

## Slide 128

**NO!**

## Slide 129

## **It is EXTREMELY slow!**<sup>7</sup>

> 7With the current state-of-the-art.

## Slide 130

**Software-based Power Side Channels**

- **MDS-style:** 4.82 bit _/_ h

29

� 0xhilbert � andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 131

**Software-based Power Side Channels**

- **MDS-style:** 4.82 bit _/_ h

- **Meltdown-style (RSB):** 0.84 bit _/_ h

29

� 0xhilbert � andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 132

**Software-based Power Side Channels**

- **MDS-style:** 4.82 bit _/_ h

   - **MDS-style:**

      - 0.065 to 0.68 bit _/_ h

- **Meltdown-style (RSB):** 0.84 bit _/_ h

29

� 0xhilbert

� andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 133

**Software-based Power Side Channels**

- **MDS-style:** 4.82 bit _/_ h

- **Meltdown-style (RSB):** 0.84 bit _/_ h

- **MDS-style:** 0.065 to 0.68 bit _/_ h

- **Meltdown-style estimate (PHT):** 99.95 days _/_ bit to 2.86 years _/_ bit

29

� 0xhilbert

� andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 134

**DEMO**

## Slide 135

**Mitigations**

## Slide 136

### **Mitigations**

- **Preventing data collisions:**

   - **Redesign** of the complete shared data path

   - **Costly** to deploy

   - **Missed** components re-enable Collide+Power

30

� 0xhilbert

� andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 137

**Mitigations**

- **Preventing observable power consumption:**

   - **Restricting** all direct power interfaces

- **Mitigating** Hertzbleed is challenging

   - Thermal and power management is required

- _→_ **Collide+Power** is slow but unmitigated on modern CPUs!

31

� 0xhilbert � andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 138

### **Black Hat Sound Bytes**

- **Unrestricted** power interfaces are a threat for system security

32

� 0xhilbert

� andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 139

### **Black Hat Sound Bytes**

- **Unrestricted** power interfaces are a threat for system security

- **Indirect interfaces** still expose exploitable information

32

� 0xhilbert

� andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 140

### **Black Hat Sound Bytes**

- **Unrestricted** power interfaces are a threat for system security

- **Indirect interfaces** still expose exploitable information

- **Software-based power side channels** can leak arbitrary data

32

� 0xhilbert

� andreas.kogler@iaik.tugraz.at

Andreas Kogler

## Slide 141

### **Black Hat Sound Bytes**

- **Unrestricted** power interfaces are a threat for system security

- **Indirect interfaces** still expose exploitable information

- **Software-based power side channels** can leak arbitrary data

- **Many more details** in the papers `https://collidepower.com https://hertzbleed.com https://platypusattack.com/`

32

� 0xhilbert � andreas.kogler@iaik.tugraz.at

Andreas Kogler
