---
title: "I Have Got to Warn You, It Is a Learning Robot Using Deep Learning Attribution Methods for Fault Injection Attacks"
speakers: ["Karim Abdellatif"]
conference: "Black Hat"
conference_full: "Black Hat ASIA 2025"
edition: "ASIA"
year: 2025
source_pdf: "Black Hat Asia 2025 Slides/Karim Abdellatif_I Have Got to Warn You, It Is a Learning Robot Using Deep Learning Attribution Methods for Fault Injection Attacks.pdf"
pages: 47
sha256: "0446d92737e799d020d835f9b6e5b34c854892db3f09e792765c270004a4a017"
text_chars: 11735
ocr_pages: 3
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:05:48Z"
---
# I Have Got to Warn You, It Is a Learning Robot Using Deep Learning Attribution Methods for Fault Injection Attacks

**Speakers:** Karim Abdellatif  
**Conference:** Black Hat ASIA 2025  
**Source:** `Black Hat Asia 2025 Slides/Karim Abdellatif_I Have Got to Warn You, It Is a Learning Robot Using Deep Learning Attribution Methods for Fault Injection Attacks.pdf` (47 pages)

## Slide 1

I Have Got to Warn You, It Is a Learning Robot: Using Deep Learning Attribution Methods for Fault Injection Attacks

_Karim M. Abdellatif_

## Slide 2

**Whoami**

Hardware Wallet Manufacturer Donjon Ledger’s Security Research Team

2

## Slide 3

## **Hardware attacks**

- **Fault injection** : Perturbing the chip during sensitive operations:

   - Power and clock glitches

   - Electromagnetic fault injection (EMFI)

   - Body biasing injection (BBI)

   - Laser fault injection (LFI)

- **Side-channel** : Investing leakages such as EM, power, or time to perform:

   - Simple power analysis (SPA)

   - Differential power analysis (DPA)

- Profiling attacks

3

## Slide 4

## **Motivation**

- Working on black-box fault injection evaluations takes a lot of time.

- A lot of parameters should brute-forced:

   - Example: BBI or laser fault injection require tuning the following parameters: pulse power, pulse width, **vulnerable timing moments** , and XY point.

- Identifying vulnerable timing moments is one of the big challenges, especially under the case of countermeasures that require injecting multiple faults.

Having reverse engineering tools would be very useful in such evaluations.

(BBI attack<sup>1</sup> )

> 1Donjon, ”Breaking A Recent SoC’s Hardware AES Accelerator Using Body Biasing Injection”, HW.io 2022.

4

## Slide 5

## **Outline**

**Deep Learning in Hardware Security Deep Learning Attribution Methods Practical Challenge: DS28C36 from Analog Devices Applying DL Attribution Methods into Fault Injection**

**Tooling Conclusion**

5

## Slide 6

**DEEP LEARNING IN HARDWARE SECURITY**

## Slide 7

## **DL-based SCAs**

   - DL-based SCAs<sup>2</sup>

      - Several devices for learning and test

      - Better efficiency in case of countermeasures<sup>3</sup>

   - DL-based leakage detection<sup>4</sup>

      - It uses DL attribution methods to detect POIs.

      - Better than classical statistical techniques in case of countermeasures

- 2H. Maghrebi, T. Portigliatti, and E. Prouff. ”Breaking cryptographic implementations using deep

- learning techniques”, SPACE 2016.

- 3E. Cagli, C. Dumas, and E. Prouff ”Convolutional neural networks with data augmentation against

- jitter-based countermeasures: Profiling attacks without pre-processing”, CHES 2017

> 4L. Masure et _al_ , Gradient Visualization for General Characterization in Profiling Attacks, IACR.

7

## Slide 8

## **DL-based SCAs**

Variable key Training set Neural network
Variable plaintext
Label = 0
Label = 1
Training
target
Label = 254
Label = 255
Profiling phase

8

## Slide 9

## **DL-based SCAs**

Unknown key Test traces Trained network
Label = 0 Pr = 0.1
Label = 1 Pr = 0.05
Test
target
Label = 254 Pr = 0.4
Label = 255 Pr = 0.02
Sum(Pr) = 1
Test phase

9

## Slide 10

## **Practical example**

## Running AES-128 (first round) on a 32-bit MCU.

EM setup for STM32U5 - Donjon

EM signal

10

## Slide 11

## **MLP-based example**

- 1 def mlp model ( sample len , r a n g e o u t e r l a y e r ) : 2 model = S e q u e n t i a l () 3 model . add ( Dense (20 , input dim=sample len , a c t i v a t i o n=t f . nn . r e l u ) ) 4 model . add ( Dense (10 , a c t i v a t i o n=t f . nn . r e l u ) ) 5 model . add ( Dense ( r a n g e o u t e r l a y e r , a c t i v a t i o n=t f . nn . softmax ) ) 6 model . compile ( 7 o p t i m i z e r=”adam” , 8 l o s s=” c a t e g o r i c a l c r o s s e n t r o p y ” , 9 m e t r i c s =[” accuracy ” ] ,

- 10 ) 11 r e t u r n model

11

## Slide 12

**Few traces to attack unknown key**

- 500K traces for profiling

- 1K traces for test

- Labels on Sbox output

12

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Few traces to attack unknown key
8
500K traces for profiling
8
1K traces for test
Labels on Sbox output
Ss
Average rank of K[0]
20 30
Number of traces
12
```

## Slide 13

**DEEP LEARNING ATTRIBUTION METHODS**

## Slide 14

## **Attribution methods**

- Such methods are used to interpret and understand the decisions made by deep neural networks.

- Identify which input features (e.g., pixels in an image) are most influential in the model’s predictions.

**Gradient-Based Methods** , **Activation-Based Methods** , ...

Input challenge (predict 7)

Attribution result

14

## Slide 15

## **Activation-Based Methods: Layer-wise Relevance Propagation (LRP)**

It lies in tracing back the contributions of input nodes to the final prediction.

zjk
Rj = � Rk
k � j zjk

(1)

Illustration of the LRP procedure<sup>5</sup>

where j and k denote neurons in consecutive layers, and _zjk_ = _aj wjk_ is the activation of the neuron j multiplied by the weight between neuron j and neuron k.

> 5S. Bach et al. ’On pixel-wise explanations for non-linear classifier decisions by layer-wise relevance propagation.’ PloS one 10.7 (2015).

15

## Slide 16

**MNIST example**

Input challenge

LRP

16

## Slide 17

**Other methods**

Input challenge

Taylor

LRP

Input

17

## Slide 18

## **Application into side-channel**

Previous work<sup>6</sup> exists in the side-channel domain.

Advantages: detecting leakage points in case of countermeasures (ex: masking and jitter) unlike SNR or T-test.

> 6B. Hettwer et al., ” neural network attribution methods for leakage analysis and symmetric key recovery”, SAC-2019.

18

## Slide 19

**Practical example - AES**

1 Collecting power traces from an AES 2 Profiling on _Sbox[0]_ 3 Reverse-engineering using attribution methods 4 Comparing it with SNR/NICV

Difference between SNR and LRP

19

## Slide 20

## **Another example**

1 Two different values with
jitter

2 T-test fails!

Upper: desynchronized traces, below: T-test

20

## Slide 21

## **Using attribution methods**

- 1 Two different values are randomized. 2 Profiling on the two labels of them 3 Timing is very well detected. 4 Advantages:

   - Decision scalability (one trace)

   - It can defeat countermeasures.

Sample trace and LRP

21

## Slide 22

**PRACTICAL CHALLENGE: DS28C36 FROM ANALOG DEVICES**

## Slide 23

## **Security features**<sup>7</sup>

- ECC-256 computation engine

- FIPS 180 SHA-256 computation engine

- TRNG with NIST SP 800-90B compliant entropy source with function to read out

- 17-Bit one-time settable, non-volatile decrement-only counter with authenticated read

- **8Kbit of EEPROM for user data, keys, and certificates**

- The full data sheet is not available and this required some reverse to find the available commands and their parameters.

7https://www.analog.com/media/en/technical-documentation/data-sheets/DS28C36.pdf

23

## Slide 24

## **EEPROM organization**

Page Description
0 to 15 User pages
16 to 21 Public keys (x and y)
22 to 24 Private keys
25 to 26 Secret pages
27 Counter
28 to 29 Random
30 to 31 RAM buffer

24

## Slide 25

## **Sample preparation**

Decapped chip

8Kbits EEPROM
Logic
RAM

Infrared backside image

25

## Slide 26

**Setup**

- An infrared pulsed laser source and a microscope for focusing

- A Scaffold<sup>8</sup> board

- A Tektronix MSO44 oscilloscope

- DUT: DS28C36

Setup

> 8O. Heriveaux. Scaffold. https://github.com/Ledger-Donjon/scaffold

26

## Slide 27

## **Read page command**

- 1 w r i t e d a t a ( page number , data )

- 2 read page ( page number )

- 3 s a v e p o w e r t r a c e ()

1 2
3
32 peaks
4 identical patterns
2 3

Power consumption in case of unprotected page

27

## Slide 28

## **Unprotected and protected page**

- 1 w r i t e d a t a ( page number , data ) 2 read page ( page number )

- 3 s a v e p o w e r t r a c e ()

- 4 lock page ( page number )

- 5 read page ( page number )

- 6 s a v e p o w e r t r a c e ()

### Protected and unprotected

28

## Slide 29

## **Attack scenario**

## Step 1:

- 1 w r i t e d a t a ( page number , data )

- 2 lock page ( page number )

## Step 2:

- 1 wh il e True : 2 p r e p a r e f a u l t () # s i n g l e p u l s e

- 3 c h i p r e s t a r t () 4 read page ( page number )

- 5 s a v e l o g () 6 move laser ()

Fault injection search window

Power consumption when the page is locked

29

## Slide 30

## **Investigation**

Page configuration (bit or bits) can be:

- Stored in the EEPROM

- Stored in eFuses

- Manipulated in the logic

- Temporarily stored in RAM

8Kbits EEPROM
Logic
RAM

IR image

30

## Slide 31

Results

|Number|Chip response|Note|
|---|---|---|
|0|`2155ffffffffffffffffffffffffffffff`
`ffffffffffffffffffffffffffffffffff`|Locked|
|1|`ffffffffffffffffffffffffffffffffff`
`ffffffffffffffffffffffffffffffffff`|Timeout|
|2|NACK|I2C communication error|
|3|`21aab8289516978a7b25eb1d8a317f6c6a`
`71718b4d47de4754ac32a1d1c5adb7d324`|Public key slot|
|4|`21aa208cfc9a7dc7fcdb5437775fea79aa`
`2c95f5795ed2bfe883082a2ada0585694f`|Needs to be investigated|

31

## Slide 32

**Investigation**

- Correct read page trace for response 3

- In case of response 4, no EEPROM read

- It seems to be a RAM, or RNG content

Difference between response 3 (upper) and response 4 (below)

32

## Slide 33

## **Discussion**

- The chip seems to be protected against single fault attacks? (black box evaluation)

- **Reverse-engineering the Read Page command is the only way to understand clearly.**

- **How can we do that? deep learning?**

33

## Slide 34

**APPLYING DL ATTRIBUTION METHODS INTO FAULT INJECTION**

## Slide 35

## **Application on read page command**

- We will apply the DL attribution methods, which are used in SCAs to detect sensitive operations, into fault injection (FI).

- The main purpose is to detect when sensitive bits are processed.

- More precisely, we will try to locate on the power consumption trace, the manipulation of the page protection bit/bits.

   - The first set is collected when the page is unlocked (50K traces).

   - The second set is collected when the **same page** is locked (50K traces).

35

## Slide 36

## **Methodology**

Training set - Unprotected
Neural network
Label = 0
Training  Attribution
target Training set - Protected   Methods
Vulnerable  moments
Label = 1

36

## Slide 37

**Methodology**

Combining two datasets Performance improvement 0 and 1

Learning phase

37

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Methodology
leakages concatenate((leakages @, leakages 1), axis= -
metadat concatenate((labels 0, labels_1), axis=0) Combining two datasets
x train = normalization((leakages), feature _range=(-1, 1)) Performance improvement
Oand1
odel = model _mlp(x_train.shape
profile engine = Profile(model, leakage model=leakage model)
profile engine.data augmentation(aug mixup)
ngine.train(
x train, Learning phase
metadata=metadata,
guess _range=GUE
epochs=EPOCHS,
batch size=10,
validation split=0
data_augmentation=
```

## Slide 38

## **Methodology**

LRP

38

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Methodology
yate.model wo softmax(model)
estigate.analyzer.LRP(model wo sm LRP
trace = trace _sample.reshape(1, x_test.shape[1])
vis trace = gradient analyzer.analyze(trace) [0]
38
```

## Slide 39

Result

• Two zones
• Protected against Zone 1 Zone 2
single fault attacks

LRP result

39

## Slide 40

## **Successful faults**

• Scanning the chip with
double pulses
• Scanning the logic area
• Successful fault

Vulnerable spot

40

## Slide 41

## **Double fault attack**

- Fixing the laser beam on the correct location

- Success rate close to 99%

Power trace in case of a successful fault

This confirms the efficiency of DL attribution methods.

41

## Slide 42

## **User pages vs other pages**

- The presented attack is applicable on all the user pages.

- It isn’t applicable on permanent-protected pages used for P256 curve private keys.

   - The chip passed a fixed unidentified value for these pages.

42

## Slide 43

**TOOLING**

## Slide 44

**Scadl**

- Latest side-channel attacks using deep learning

- Leakage detection using deep learning attribution methods

Scadl: Open source tool - Donjon

Clone and investigate!

44

## Slide 45

**CONCLUSION**

## Slide 46

## **Conclusion**

- DL attribution methods involved in this work, can be used when performing fault injection attacks in black box context.

- Manufacturers **must** consider such technique for testing countermeasures in addition to leakage detection techniques to detect vulnerable timing moments.

- Using double verification against fault injection attacks is not efficient enough if it is used alone.

- Manufacturers must at minimum combine it with strong hardware and/or software jitter as an additional countermeasure.

46

## Slide 47

# THANK YOU. QUESTIONS?

Karim M. Abdellatif, PhD e-mail: karim.abdellatif@ledger.fr

47
