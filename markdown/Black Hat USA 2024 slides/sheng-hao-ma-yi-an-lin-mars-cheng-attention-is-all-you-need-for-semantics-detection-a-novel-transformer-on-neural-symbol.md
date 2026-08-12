---
title: "Attention Is All You Need for Semantics Detection A Novel Transformer on Neural-Symbolic Approach"
speakers: ["Sheng-Hao Ma", "Yi-An Lin", "Mars Cheng"]
conference: "Black Hat"
conference_full: "Black Hat USA 2024"
edition: "USA"
year: 2024
source_pdf: "Black Hat USA 2024 slides/Sheng-Hao Ma & Yi-An Lin & Mars Cheng_Attention Is All You Need for Semantics Detection A Novel Transformer on Neural-Symbolic Approach.pdf"
pages: 42
sha256: "e6ab37e9609121cfe18f18daf41f09f7fcefb8f4d0c1db8f30c5c96444f5bdab"
text_chars: 26273
ocr_pages: 5
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:39:00Z"
---
# Attention Is All You Need for Semantics Detection A Novel Transformer on Neural-Symbolic Approach

**Speakers:** Sheng-Hao Ma, Yi-An Lin, Mars Cheng  
**Conference:** Black Hat USA 2024  
**Source:** `Black Hat USA 2024 slides/Sheng-Hao Ma & Yi-An Lin & Mars Cheng_Attention Is All You Need for Semantics Detection A Novel Transformer on Neural-Symbolic Approach.pdf` (42 pages)

## Slide 1

**Attention Is All You Need for Semantics Detection A Novel Transformer on Neural-Symbolic Approach**

Sheng-Hao Ma @aaaddress1

Yi-An Lin

Mars Cheng @marscheng_

#BHUSA @BlackHatEvents

## Slide 2

🇹

## **TXOne Threat Researcher From**

Sheng-Hao Ma Yi-An Lin Mars Cheng Team Lead Threat Researcher Threat Research Manager PSIRT and Threat Research PSIRT and Threat Research PSIRT and Threat Research

TXOne Networks  |  Keep the Operation Running

## Slide 3

## **Outline**

### 01 | **Background and Pain Points**

### 03 | **Use One Transformer to Conquer All You Need for Detection**

- nnYara

- nnShellcode

- nnSymUnpacker

### 02 | **Deep Dive into Our Practical NeuralSymbolic Transformer**

### 04 | **Conclusion and Takeaways**

- CuIDA (Cuda-trained Inference Decompiler Agent)

- API Use-define Walker of CFG

- Symbolic-sensitive Represent Tokenizer

- MS Predefined Integer-Scale Semantics

TXOne Networks  |  Keep the Operation Running

## Slide 4

**Background and Pain Points**

**TXOne Networks  |  Keep the Operation Running**

## Slide 5

## **Let’s get straight to the point : the Dilemma of the Blue Team!**

- In their daily duties, SOC personnel, digital forensics experts, malware analysts, and threat intelligence analysts frequently face challenging scenarios without dynamic execution as shown below

Highly Obfuscated Malware

Windows Shellcode

Commercial Packers e.g. VMProtect, Themida, etc.

TXOne Networks  |  Keep the Operation Running

## Slide 6

## **Practice makes Perfect as a Malware Analyst?**

- Through years of analyzing malware, such as in-the-wild obfuscated ransomware, malware analysts developer professional intuition. It leads us to wonder

   - Can we **predict** the function of the malware **without actually executing** it?

   - Expert opinion: 'predicting' the format of call sequences is possible with surprising accuracy

#### **<u>The Sense Behind Human Expert Analysis</u>**

**(1.) Looks like FILE_FLAG Macro (2.) So it should be File Handle? of CreateFile() at #2 argument** **(3.) INVALID_HANDLE_VALUE? (4.) Maybe GetFileSize() with local buffer v14**

**(2.) So it should be File Handle?**

TXOne Networks  |  Keep the Operation Running

## Slide 7

## **Previous Work**

- In our Black Hat USA 2022 research, we highlighted the power of **building a symbolic engine** to detect obfuscated ransomware, aiming to capture hidden ransomware in large-scale sample datasets, such a VirusTotal.

   - The idea relies on taint analysis and tracking **data flow among unknown API calls**

Scrupulous human work is required, but the re is never enough resources L

TXOne Networks  |  Keep the Operation Running

https://www.blackhat.com/us-22/briefings/schedule/#a-new-trend-for-the-blue-team---using-a-practical-symbolic-engine-to-detect-evasive-forms-of-malwareransomware-26932

## Slide 8

## **Distributional Hypothesis**

• _“Given the following format of an unknown API, please choose the best possible API name based on your experience as a malware expert:”_

𝑈𝑛𝑘𝑛𝑜𝑤𝑛𝐴𝑝𝑖𝑁𝑎𝑚𝑒 𝑆𝑡𝑟, 0𝑥40000000, 0, 0, 1, 0𝑥04000000, 0 𝑈𝑛𝑘𝑛𝑜𝑤𝑛𝐴𝑝𝑖𝑁𝑎𝑚𝑒 𝑆𝑡𝑟, 0𝑥𝐶0000000, 0, 0, 1, 0𝑥00000000, 1

- A. FindWindowExW

B. CreateFileW

C. GetDlgItems

D. SendMessageW

Great! 0x40000000 and 0xC0000000 are commonly used in the 2nd argument of CreateFileW()

TXOne Networks  |  Keep the Operation Running

https://en.wikipedia.org/wiki/Distributional_semantics#Distributional_hypothesis

## Slide 9

## **Distributional Hypothesis**

### • _“Given the following format of an unknown API, please choose the best possible API name based on your experience as a malware expert:”_

All of them expect 4 args

A. SendMessageA B. SetTimer C. AdjustWindowRectEx

D. RedrawWindow

𝑈𝑛𝑘𝑛𝑜𝑤𝑛𝐴𝑝𝑖𝑁𝑎𝑚𝑒 𝐼𝑛𝑡, 0, 0, 0𝑥105 𝑈𝑛𝑘𝑛𝑜𝑤𝑛𝐴𝑝𝑖𝑁𝑎𝑚𝑒 𝐼𝑛𝑡, 0, 0, 0𝑥401 𝑈𝑛𝑘𝑛𝑜𝑤𝑛𝐴𝑝𝑖𝑁𝑎𝑚𝑒 𝐼𝑛𝑡, 0, 0, 0𝑥180 𝑈𝑛𝑘𝑛𝑜𝑤𝑛𝐴𝑝𝑖𝑁𝑎𝑚𝑒 𝐼𝑛𝑡, 0, 0, 0𝑥181

WOW, 4 argument? This is too common 😈 and harder to guess for humans.

TXOne Networks  |  Keep the Operation Running

https://en.wikipedia.org/wiki/Distributional_semantics#Distributional_hypothesis

## Slide 10

**Deep Dive into Our Practical Neural-Symbolic Transformer**

**TXOne Networks  |  Keep the Operation Running**

## Slide 11

## **Cuda-trained Inference Decompiler Agent (CuIDA)**

𝐿𝑖𝑘𝑒𝑙𝑖ℎ𝑜𝑜𝑑𝑢𝑠𝑎𝑔𝑒𝑜𝑓𝑅𝑒𝑔𝑂𝑝𝑒𝑛𝐾𝑒𝑦𝐸𝑥
80000002ℎ,
𝑝𝑟𝑜𝑏𝑏𝑦𝑡𝑎𝑖𝑛𝑡𝑎𝑛𝑎𝑙𝑦𝑠𝑖𝑠
𝐴𝑛𝑠𝑖𝑆𝑡𝑟,
, During the evaluation phase, we compare the predicted API arguments
0,
with the input lengths of the decompiled unknown calls.
TCSA Symbolic Engine 1,
(BHUSA’22) &ℎ𝐾𝑒𝑦
𝐴𝑛𝑠𝑖𝑆𝑡𝑟,
Neural Symbolic YARA
0,
Walk over the control flow graph
Extract all the contextual parallel API  𝑅𝐸𝐺_𝑆𝑍,
Neural Shellcode Predictor
sequences  &𝑏𝑢𝑓,
260ℎ
Neural Symbolic Unpacker
CuIDA Architecture 0.012 “OpenProcess”,     4
Function
Argument 0.003 “SendMessage”,    4
Transformer Block
Positions “ RegSetValueEx”,  6
Embedding  Softmax 0 . 9 6
⨁ Masked Multi-Head Attention
Layer Output 0.443 “WinExec”,             2
Tokenized Add & Norm
Symbols …
“WriteFile”,            4 Argument
0.57
Length
N×

TXOne Networks  |  Keep the Operation Running

## Slide 12

## **Recap Cylance Research in NDSS 2018**

- They introduce a static-analysis approach for observing arguments in unknown API calls:

- A simplified symbolic execution engine is used to collect usedefinition chains.

   - Hidden-Markov-Models(HMMs) automate inferential processes on well-known Win32 API schemes, achieving up to 87.6% accuracy.

   - **Limitation and Future Work:**

      - The approach may lose the semantics of original API usage patterns.

      - HMMs lack position-wise semantics, making it challenging to classify Win32 APIs with fewer than 5 arguments, especially when meaningful Microsoft MACRO integers are used. For example:

         - 𝑉𝑖𝑟𝑡𝑢𝑎𝑙𝐴𝑙𝑙𝑜𝑐 0, 114ℎ, 80ℎ, 4

         - S𝑒𝑛𝑑𝑀𝑒𝑠𝑠𝑎𝑔𝑒 0, 200ℎ, 1, 0

TXOne Networks  |  Keep the Operation Running

## Slide 13

## **Position-wise Semantics Encoding**

- **Position – The Order Matters for Semantics!**

   - We also understand that the order of function arguments is crucial for the OS interface, such as the Win32 API, to receive the specific inputs chosen by the program developers.

HANDLE OpenProcess( DWORD dwProcessId, DWORD dwDesiredAccess, BOOL  bInheritHandle ) HANDLE OpenProcess( DWORD dwDesiredAccess, BOOL  bInheritHandle, DWORD dwProcessId )

**It’s important to represent the order in API syntax.**

Argument Inputs = [ embedding(DWORD <u>1 ) , embedding(BOOL 2</u> ), embedding (DWORD <u>3</u> ) ]

TXOne Networks  |  Keep the Operation Running

kazemnejad.com/blog/transformer_architecture_positional_encoding

## Slide 14

## **Scaled Dot-Product Attention**

𝑄𝐾<sup>(</sup> 𝑦= 𝑠𝑜𝑓𝑡𝑚𝑎𝑥( )V 𝑑)

- By projecting argument value distribution into a 3D QKV (Query, Key, Value) database, we can encode this order and predict API names using Softmax.

𝐼𝑛𝑝𝑢𝑡𝑇𝑜𝑘𝑒𝑛 𝑂𝑢𝑡𝑝𝑢𝑡
⋯
ℎ!! ℎ!"
𝑥1, 𝑥2, 𝑥3, 𝑥4 × ⋮ ⋱ ⋮ × 𝑄𝐾𝑉#$$%"$&'" =      [ o1, o2, o3, o4 ]
⋯
ℎ!" ℎ""
𝐸𝑚𝑏𝑒𝑑𝑑𝑖𝑛𝑔𝑊𝑒𝑖𝑔ℎ𝑡𝑀𝑎𝑡𝑟𝑖𝑥
⋯
1 0 0 0
ℎ(𝑥1 + 𝑥2 + ⋯𝑥𝑛)
⋯
0.5 0.5 0 0
ℎ(𝑥1 + 𝑥2 + 𝑥3 + 𝑥4)
⋯
ℎ(𝑥1 + 𝑥2 + 𝑥3) 0.33 0.33 0.33 0
ℎ(𝑥1 + 𝑥2) W#$$%"$&'" ∈𝑅 (×( =
⋮ ⋮ ⋱ ⋱ ⋮
ℎ(𝑥1)
1 1 1
⋯ ⋯
𝐴𝑃𝐼𝐹𝑢𝑛𝑐 𝑥1, 𝑥2, 𝑥3, 𝑥4, … 𝑥" 𝑇 𝑇 𝑇

TXOne Networks  |  Keep the Operation Running

## Slide 15

## **Our Attention-based API Semantics Model**

The sequence of human expert analysis

𝑆𝑒𝑞𝑢𝑒𝑛𝑐𝑒4%#56&7% = 𝑓1 𝑥1, 𝑥2, … 𝑥𝑛 → 𝑓2 𝑥1, 𝑥2, … 𝑥𝑛 → 𝑓3 𝑥1, 𝑥2, … 𝑥𝑛 → …

𝑅𝑒𝑎𝑑𝐹𝑖𝑙𝑒 ℎ𝐹𝑖𝑙𝑒, 𝑠𝑧𝐵𝑢𝑓, 𝐿𝑒𝑛, 0, 0 𝐺𝑒𝑡𝐹𝑖𝑙𝑒𝑆𝑖𝑧𝑒 ℎ𝐹𝑖𝑙𝑒, &𝐿𝑒𝑛 hFile = 𝐶𝑟𝑒𝑎𝑡𝑒𝐹𝑖𝑙𝑒𝐴 𝑝𝑎𝑡ℎ, G𝐸𝑁𝐸𝑅𝐼𝐶+,-., 0, 𝑂𝑃𝐸𝑁,/01(023, 0, 0

TXOne Networks  |  Keep the Operation Running

## Slide 16

## **Our Attention-based API Semantics Model**

𝑆𝑒𝑞𝑢𝑒𝑛𝑐𝑒4%#56&7% = 𝑓1 𝑥1, 𝑥2, … 𝑥𝑛 → 𝑓2 𝑥1, 𝑥2, … 𝑥𝑛 → 𝑓3 𝑥1, 𝑥2, … 𝑥𝑛 → …

𝐴𝑡𝑡𝑒𝑛𝑡𝑖𝑜𝑛 𝑝𝑎𝑡ℎ, G𝐸𝑁𝐸𝑅𝐼𝐶+,-., 0, 𝑂𝑃𝐸𝑁,/01(023, 0, 0 = Embedding(CreateFileA)

𝑇𝑎𝑖𝑛𝑡𝐴𝑛𝑎𝑙𝑦𝑠𝑖𝑠& 𝐸𝑚𝑏𝑒𝑑𝑑𝑖𝑛𝑔

𝐴𝑡𝑡𝑒𝑛𝑡𝑖𝑜𝑛 𝐸𝑚𝑏𝑒𝑑𝑑𝑖𝑛𝑔 𝑝𝑎𝑡ℎ, 𝐺𝐸𝑁𝐸𝑅𝐼𝐶+,-., 0, 𝑂𝑃𝐸𝑁,/01(023, 0, 0 , &𝐿𝑒𝑛 = Embedding(GetFileSize)

𝑇𝑎𝑖𝑛𝑡𝐴𝑛𝑎𝑙𝑦𝑠𝑖𝑠& 𝐸𝑚𝑏𝑒𝑑𝑑𝑖𝑛𝑔 𝑇𝑎𝑖𝑛𝑡𝐴𝑛𝑎𝑙𝑦𝑠𝑖𝑠

𝐴𝑡𝑡𝑒𝑛𝑡𝑖𝑜𝑛 𝐸𝑚𝑏𝑒𝑑𝑑𝑖𝑛𝑔 𝑝𝑎𝑡ℎ, 𝐺𝐸𝑁𝐸𝑅𝐼𝐶+,-., 0, 𝑂𝑃𝐸𝑁,/01(023, 0, 0 , 𝑠𝑧𝐵𝑢𝑓, 𝐿𝑒𝑛, 0, 0 = Embedding(ReadFile)

TXOne Networks  |  Keep the Operation Running

## Slide 17

**Use One Transformer to Conquer All You Need for Detection**

**TXOne Networks  |  Keep the Operation Running**

## Slide 18

## **Use-Define Chain Extractor**

extract the use-define chains based on x86 calling convention of decompiled calls

𝑏𝑢𝑓𝑓𝑒𝑟= 𝑑𝑤𝑜𝑟 𝑑_412714 ( 𝑣4, 40000000ℎ, 4, 0, 2, 4000100ℎ,  0 )

- **Use-define extractor for stripped binaries:**

   - **Argument counting by calling convention:**

      - 32bit – push, push, push, push …

      - 64bit – rcx, rdx, r8, r9, push, push …

      - Determine unknown API argument count from decompiled results.

   - **Taint analysis to track API relationships:**

      1. Record argument values from decompiled API calls.

      2. The engine provides a magic number as return values instead of simulating API behaviors.

      3. Track these magic numbers when used as arguments in other APIs.

TXOne Networks  |  Keep the Operation Running

## Slide 19

## **Tokenizer: Representation of Unlimited Integers in Limited Scale**

?
𝐼𝑡𝑠𝑒𝑒𝑚𝑠𝑙𝑖𝑘𝑒𝑚𝑒𝑎𝑛𝑖𝑛𝑔𝑓𝑢𝑙𝐼𝑛𝑡𝑒𝑔𝑒𝑟𝑠
𝑈𝑛𝑘𝑛𝑜𝑤𝑛𝐹𝑢𝑛𝑐 𝐷7𝐹70𝐶ℎ, 𝐶00000ℎ, 200ℎ
𝑀𝑒𝑚𝑜𝑟𝑦𝑃𝑎𝑔𝑒
𝑅𝑒𝑎𝑑
𝐸𝑥𝑒𝑐𝑢𝑡𝑎𝑏𝑙𝑒?
𝑊𝑟𝑖𝑡𝑎𝑏𝑙𝑒?
PTR_ASM_CODE
In-Mem Data Type
STR_UNICODE STR_ANSI LOCAL_BUFF DATA_EXPR

TXOne Networks  |  Keep the Operation Running

## Slide 20

## **Represent but Keep Semantics on Integer Scale**

𝑆𝑒𝑚𝑎𝑛𝑡𝑖𝑐𝑠𝑜𝑛𝐼𝑛𝑡𝑒𝑔𝑒𝑟𝑆𝑐𝑎𝑙𝑒

𝑍𝑒𝑟𝑜 𝐼𝑁𝑇_𝑀𝐴𝑋 0 … 260 MS Predefined NTSTATUS scale = sqrt( NumberSize ) Meaningful Small Integers 40000000h, 80000000h, HEX _scale by Developers or C0000000h 𝑈𝑛𝑘𝑛𝑜𝑤𝑛𝐹𝑢𝑛𝑐 𝐷7𝐹70𝐶ℎ, 𝐶00000ℎ, 200ℎ 𝑀𝑒𝑚𝑜𝑟𝑦𝑃𝑎𝑔𝑒

- **Challenge of extracting semantics on integer scale**

• Bitwise similar, but distant in meaning  – 80000000h (GENERIC_READ) but 80000001h (HKEY_CURRENT_USER)

- Close in meaning, but distant bitwise    – STATUS_STACK_OVERFLOW(C00000FDh) but STATUS_TIMEOUT (102h)

TXOne Networks  |  Keep the Operation Running

## Slide 21

## **Out-of-Box Pre-Trained Model for Community**

- **Training phase**

   - Selected APT ~3.3k binaries

      - APT Groups listed by MITRE

      - ~770k sequences of Win32 API usages

   - Train with CUDA ~ 26 hours

   - K-Fold (k=10) accuracy ~94.13%

𝐿𝑖𝑘𝑒𝑙𝑖ℎ𝑜𝑜𝑑𝑢𝑠𝑎𝑔𝑒 80000002ℎ,
𝑜𝑓𝑅𝑒𝑔𝑂𝑝𝑒𝑛𝐾𝑒𝑦𝐸𝑥 𝐴𝑛𝑠𝑖𝑆𝑡𝑟, Function
0, , Argument
walk over the  1, Positions
TCSA  control flow graph &ℎ𝐾𝑒𝑦 Transformer
Embedding
Symbolic Engine 𝐴𝑛𝑠𝑖𝑆𝑡𝑟, Block
Extract all the contextual
(BHUSA’22) 0,
Tokenized
parallel API sequences
𝑅𝐸𝐺_𝑆𝑍,
Symbols
&𝑏𝑢𝑓,
260ℎ

TXOne Networks  |  Keep the Operation Running

## Slide 22

## **Case Study: Downloader with Persistence**

0c5214891c50dc1ece818770472806d36eae890b73d9b53d6c0fb8b7e0640ce7

101bd4513c9e5fc5a47d08748c19dc56edb810802fd8202b1d0e6efbb7cc1123

1d42069673fd4b1b2953c185f8e9d1331e56385cd91186cbb396df7978d88f76

Detect InternetOpenA() due to (0, 1, 0, 0, 0) because of  “1” flagged as INTERNET_OPEN_TYPE_DIRECT

CreateFile found because of that magic number 80000000h detect as GENERIC_READ

Success detect RegCreateKeyEx() due to that 80000002h auto-flagged as HKEY_CURRENT_USER

TXOne Networks  |  Keep the Operation Running

## Slide 23

## **Interpretable AI: How AI makes the Inference from Use-Define chains?**

Captum, the platform of Meta research <u>Using Captum to Explain Generative Language Models (Dec 9, 2023)</u>

Essential constraint of predefined API usage

Position #1 Unicode string buffer Position #2 NULL (API reserved value)

TXOne Networks  |  Keep the Operation Running

## Slide 24

**Use Case 1 Using the Attention-Transformer to catch a hacker’s tail in the real world: NeuralYara: Large-scale hunting for missing threats.**

TXOne Networks  |  Keep the Operation Running

## Slide 25

## **Large-scale Hunting for Missing Threats**

### **nnYARA: Neural Network-based YARA detection**

- Recover the API names for pattern matching with YARA rules

- Large-scale threat hunting on VirusTotal ~1200+ binaries

   - Search for the challenging binaries with incomplete detection coverage: size:5MB- type:peexe positives:30- tag:obfuscated

   - fs:2024-03-01T00:00:00+ fs:2024-03-30T00:00:00-

### **Key malware features found:**

1. Anti-sandbox & anti-emulation

2. Leveraging hybrid .NET (fusion of MSIL + x86)

TXOne Networks  |  Keep the Operation Running

## Slide 26

## **Hunting the Missing Threat on Large-Scale VirusTotal Samples**

   - **Successful detection of hidden behaviors**

      - In March, we captured about 400 obfuscated samples daily from VirusTotal.

         - About 90% were duplicates; So, only around 40 unique samples per day remained

- This resulted in collecting in total of around 1,200 new samples in March. **~1200 samples from VT flagged as obfuscated**

- **nnYARA Scan Extra 18 Behaviors are sensitive for AV/EDR:** 1. Windows Token Abuse and EoP 2. Mutex-Private Profile 3. Windows Hooks Profile 4. Mutex Str Internet APIs 5. Hook String of Win32 Internet APIs 6. Overlay Windows Private Profile 7. Disable Antivirus **<u>400+</u> 810 samples** … **samples**

- **YARA Scan 78 Behaviors are none-sensitive for AV/EDR:** 1. Mutex-Access 2. Windows Hooks 3. CRC / MD5 / Sha1 Hash

4. Win32 HTTP API, TCP, Wininet Library and APIs

5. Keylogger 6. Delphi / Borland Components

7. Digital Signature Detection

8. Anti-Debugger 9. WMI Usage 10.RSA & AES 11.Privilege 12.Screenshot 13.SHE 14.OLE 15.Packers …

TXOne Networks  |  Keep the Operation Running

## Slide 27

## **SHGetSpecialFolderPathW**

• 708ffc84d58e60101960b4af6cefb7c02d7a1ff625ae1b13c29907c71cfa5cfc

Detect SHGetSpecialFolderPathW due to

7 = CSIDL_STARTUP & 16 = CSIDL_DESKTOPDIRECTORY

TXOne Networks  |  Keep the Operation Running

## Slide 28

## **VC.Net (Hybrid CIL & C++) – Process Hollowing @ 426188h**

TXOne Networks  |  Keep the Operation Running

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
VC.Net (Hybrid CIL & C++) — Process Hollowing @ 426188h
”
© 2/74 security vendors and no sandboxes flagged this file as malicious QO Follow C Reanalyze 4 Download v
74
3f9359fb5287f62b17f20c85e5096c5328b7a8f4f7b02e1b221765a67f2a35ef Size Last Modification Date
QTTabBar.exe 4.04 MB 22 hours ago
—EEEEEEEE
Community peexe checks-bios assembly idle Calls-wmi checks-usb-bus runtime-modules direct-cpu-clock-access detect-debug-environment obfuscated long
Score
sub_45174C(v6, @x3BB52990) ;
sub_42EB9E(&sInfo, 8, 68);
sInfo.cb = 68;
memset (&prociInfo, @, sizeof(prociInfo));
if ( MEMORY[@x3BB9E10C](a1, a2, 0, @, 1, @x80Q00@0, O, O, &sInfo, &procInfo) )// CreateProcess detect
{
v4 = sub_428DC3(procInfo.hProcess) ; BD Windows PowerShell
MEMORY [ @x3BB9E110](procInfo.hProcess, a3); 22:26:17 [WARNING] [FOUND] (4261a7) - GetEnvironmentVa
v5 = MEMORY[0x3BB9E120]; 22:26:17 [WARNING] [FOUND] (4261c6) - SendMessageA, Ge
if ( prociInfo.hProcess ) 22:26:17 [WARNING] [FOUND] (MMBMBM) - CreateProcessA,
MEMORY [ @x3BB9E120 |(procInfo.hProcess) ; 22:26:17 [WARNING] [FOUND] (455d7) - WriteFile
if ( procInfo.hThread ) 22:26:17 [WARNING] [FOUND] (45527) - CallWindowProcw,
v5(prociInfo.hThread) ;
txOne
TXOne Networks | Keep the Operation Running == ) networks
```

## Slide 29

**Use Case 2 Using the Attention-Transformer to catch a hacker’s tail in the real world: Infer the purpose of a Windows Shellcode without execution**

TXOne Networks  |  Keep the Operation Running

## Slide 30

## **Behavior Inference for Unexecuted Shellcode**

- **Shellcode is usually designed as simple as possible, due to payload size constraints**

- **Shellcode data Use-define collector for inference**

   - We developed a simple shellcode “runner” using the TCSA symbolic engine, which walks through each code block of the shellcode. Simultaneously, it collects the use-define chain to infer the unknown API names used by the shellcode

|Parse export table
to get InternetConnectA address
Prepare the argument values
on the stack for InternetConnectA()|
|---|

Commercial pentest sample CobaltStrike beacon on VirusTotal

TXOne Networks  |  Keep the Operation Running

2569cc660d2ae0102aa74c98d78bb9409ded24101a0eeec15af29d59917265f3

## Slide 31

## **Cobaltstrike HTTP Stager (in-the-wild)**

- A wild sample first seen on 21 May 2023

   - Contained a Cobaltstrike beacon

   - Included a **broken** DLL-based Shellcode runner

      - Compiled with debug symbols and non-functional

   - The shellcode wasn’t encrypted or encoded

      - Detectable by our engine J

Our transformer goes deeper inside the payload wh ich seems like a shellcode

TXOne Networks  |  Keep the Operation Running

## Slide 32

**Demo**

TXOne Networks  |  Keep the Operation Running

## Slide 33

**Use Case 3 Using the Attention-Transformer to demystify the myths of commercial packers: Dissect the behavior of VMProtect without unpacking**

TXOne Networks  |  Keep the Operation Running

## Slide 34

## **Detection Problem of Modern Commercial Packers**

- Novel commercial packers pose a significant challenge for modern AV/EDR systems

   - To extract the original code you may need to: 1. Dump the process 2. Find the OEP (Original Entry Point) through reversing

   - 3. Rebuild the import table

   - Commercial packers often implement techniques to thwart 2. and 3. steps

- However, our AI engine can identify unknown API information even when commercial packers are used

Execute Packed Files as Process

“MZ” PE Headers

.text (Original Code)

.idata (Import Addr Table) .vmp (Packer Code)

Router Functions Pivot to APIs

Kernel32.dll execute the original behavior

TXOne Networks  |  Keep the Operation Running

## Slide 35

## **More Investigation on VMProtect Itself…**

TXOne Networks  |  Keep the Operation Running

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
uf nN
SD
13
14
16
17
More Investigation on VMProtect Itself...
int sub_54D83F()
{
int v@; // eax
v@ = MEMORY[@x771EB770](@xFC@@00, @, @, @x140);
return @;
dword_55FF18 = 16;
dword_55FF@C = v0;
MEMORY[@x10] = MEMORY[@x771DBFD@](@xFC@0@@, 8, @x41C4);
if ( !MEMORY[@x1@] )
return 0;
iF ( IMEMORY[Oxc] )
12
uly
25
25
26
26
26
26
26
26
26
26
26
A Choose segment to jump
‘Start
00531000
00532000
00533000
00534000
[ MEMORY[@xC] = MEMORY[@x75D481B0](@, @x100000, 0x2000, 4);)// S4d8b6 ...
005D7000
005D727C
005D8000
VirtualAlloc()?
‘End
00532000
00533000
00534000
00507000
00sD727¢
00508000
005FC000
R
= =F
x
‘Align
para
para
para
para
para
para
para
[INFO] [+] scan for Oc61cba7ead9c67c5d0838aa76cee95e_dump.exe
[CRITICAL] [!] total found 1219 unknown win32 pointer!
RegCreateKeyA
[WARNING]
[WARNING]
[WARNING]
[WARNING]
[WARNING]
[WARNING]
[WARNING]
[WARNING]
[WARNING]
[WARNING]
{ BD Windows PowerShell
MEMORY [ @x75D45FEQ](@xFC@@00, @, MEMORY[@x10]);
return 0; 16:22:
} 16:22:
MEMORY[8] = -1; 16:22:
MEMORY[@] = @; ee
MEMORY[4] = @; te).
dword_55FF@8 = 1; 16:22:
*MEMORY[@x10] = -1; 16:22:
return Q; 16:22:
16:22:
16:22:
16:22:
16:22:
16:22:
26
[WARNING]
[FOUND]
[FOUND]
[FOUND]
[FOUND]
[FOUND]
[FOUND]
[FOUND]
[FOUND]
[FOUND]
[FOUND]
[FOUND]
(531b79) -
(5uf3f2) -
(5uf37d) -
(551089) -
(551607) -
(5516f0) -
(54158) -
(54f162) -
(54uf065) -
(5ud8b6) -
(54d943) -
CreateFileW, GetTempFileNamewW
MulDiv
GetFileAttributesExA
GetEnvironmentVariableA, MulDiv
public
public
public
public
public
public
public
|Class
CODE
DATA
DATA
CODE
DATA
DATA
CODE
Oo
Ps C:\Users\aaaddressl1\Desktop> py ida-oracle\scan.py .\@c61lcba7ead9c67c5d0838aa76cee95e_dump.exe
[INFO] [!] assert that's an income file to scan.
GetTokenInformation, RegOpenKeyExW, MultiByteToWideChar
CopyFileA, CopyFileW
GetEnvironmentVariableA, lstrcpynA, MulDiv
GetModuleFileNameA, GetModuleFileNameW, GetShortPathNameA
VirtualALloc, VirtualFree, VirtualFreeEx
Xx
```

## Slide 36

## **More Investigation on VMProtect Itself…**

**GetCurrentProcess() equal to HANDLE(-1)**

TXOne Networks  |  Keep the Operation Running

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
More Investigation on VMProtect Itself...
bool __usercall sub_53C27@@<al>(LPVOID src_addr@<esi>, LPVOID dest_addr)
{
char opJump; // [esp+4h] [ebp-8h] BYREF
int v4; // [esp+5h] [ebp-7h]
// Integer Range Check
if ( (dest_addr + 0x80000000i64 - src_addr - 5) >> 32 )
return @;
// x86 Jump Opcode (\xE9)
opJump = @xE9;
v4 = dest_addr - src_addr - 5;
// (53c2b4) - Possible WriteProcessMemory
return WriteProcessMemory_@(QxFFFFFFFF, src_addr, &opJump, Su, 9);
}
| bool __usercall sub_53C27@@<al>(int src_addr@<esi>, int dest_addr)
2f
3 __int64 offset; // kr@@_8
4 char opJump; // [esp+4h] [ebp-8h] BYREF = w:
= Wind PowerShell
5 int v5; // [esp+5h] [ebp-7h] Po Windows Fowersne!
6 18:00:21 [WARNING] [FOUND] (531385) - CreatePen, EnableScrollBar, MonitorFromPoint
/ offset = dest_addr - src_addr - 5 + 0x89@00000i64; 18:00:21 [WARNING] [FOUND] (542216) - memcpy, GetClassNameW, UstrcpynA
8 if ( HIDWORD(offset) ) 18:00:22 [WARNING] [FOUND] (BRM) - ReadFile, WriteFile; WriteProcessMemory |
18:00:22 [WARNING] [FOUND] (53c718) - WritePrivateProfilkSectionW, PtInRect, GetEnvirol
- a 95 Opcode (\xE9 18:00:22 [WARNING] [FOUND] (53f21la) - GetFullPathNameW, AppendMenuA, SendMessageA
- // x ump Opcode (\xE9) 18:00:22 [WARNING] [FOUND] (53f248) - GetFullPathNameW, BendMessageA, InternetCrackUrl
11 opjJump = @xE9; 18:00:22 [WARNING] [FOUND] (542267) - AdjustTokenPrivilepes, ShellExecuteA, FindFirstF:
12 v5 = dest_addr - src_addr - 5;
ne // (53c2b4) - Possible WriteProcessMemory
14 return MEMORY[@x75D62580](offset,| -1, |src_addr, &opJump, 5, @) !- 0; € [Na ae Ea a
15 } oossiand ovsszand ; x ‘ para
A 532000 533000 . ra
GetCurrentProcess() equal to HANDLE(-1) 00533000 00534000 R Ww i sore
TXOne Networks | Keep the Operation Running 3] + 00534000 005D7000 R . X L para
005D7000 005D727C R W L para
```

## Slide 37

## **Themida**

- We also confirmed that this works well with Themida-packed files too

Function Thunk

||redirect by the|
|---|---|
||commercial packers|
|TXOne Networks  |  Keep the Operation Runni|ng|

execute the original behavior

## Slide 38

TXOne Networks  |  Keep the Operation Running

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
(|. IDA - 680000.0c61cba7ead9c67c5d0838aa76cee95e.exe C:\Users\aaaddress 1\Desktop\CulDA\lib\process_13584\680000.0c61cba7ead9c67...
File Edit _— Search View Pensget Lumina SipRETS Windows Help
WB Library function MJ Regular function _ Instruction [J Data (§ Unexplored J External symbol J Lumina function
Ie IDA View-A @ Hex View-1 8 = EN Structures = Enums = SB Imports BA Exports
__int128 v10; // [esp+21Ch] [ebp-14h] BYREF
sub. _681D78(v9, @, 528);
AE a @, v9, 260); 2 Refresh ions | @& Find handles or DLLs 2* System informatio
(“ADVAPI", "RegCreateKeyExw") ; = =
i(ve); Services k Disk Firewall
]("ADVAPI", "RegSetValueExw");
RY [Ox ](v2);
me 2147483647, base Grote NLC hosot NAW indows \\Cunrentvens ton \\RUnG , ®, @, @, 131103, @, &v8, @)
L"H4A0", ®, 1, My 2S ogee + 2); gi
RY[@ "KERNEL32" "CreateProcessW");
v3
vs = M @x76 90] ("WS2_32", “WSASocket"); CPU usage: Physical memory: 12.4 GB (39.08%) _ Free memory
v6 = [ 58} (v5);
while r 1 Ly
MEMORY [x
250](514, &unk_68339@) ;
dword_683520 eG: 1, 6, @, @, @);
word_68356C =
word_68356E =
dword 683570
[FOUND] (69d772) - VirtualFree, memcpy, MulDiv
7:07:55 [FOUND] (69d7cd) - VirtualFree, memset, memcpy
1:07:55 [FOUND] (69a345) - AdjustWindowRectEx, DefMDIChildProcW, WritePrivateProfileStringA
1:07:55 [FOUND] (6a3807) - PtInRect, IntersectRect, UnionRect
1:07:55 [FOUND] (6a3b92) - VirtualQuery, GetClassNameA, FillRect
1:07:55 [FOUND] (69a3dc) - FileTimeToDosDateTime, IntersectRect, MulDiv
1:07:55 [FOUND] (6a2060) - WideCharToMultiByte, ExtTextOutA
1:07:55 [FOUND] (6a0596) - GetTokenInfprmation, CallWindowProcW, RegOpenKeyExwW
1:07:55 [FOUND] (6a0528) - CallWindowProcW, GetTokenInformation, CallWindowProcA
1:07:55 [FOUND] (6a2154) - CreateFileA, CreateFileW
1:07:55 [FOUND] (6a1b26) - CreateFileA, CreateFilewW
1:07:55 [FOUND] (6a1b49) - WriteConsoleW, WriteConsoleA, WriteFile
1:07:55 [FOUND] (6alaf3) - WriteConsoleW, ReadFile, WriteFile
1:07:55 [FOUND] (69fea6) - FillRect, GetScrollInfo, GetPixel
1:07:55 [FOUND] (69fele) - WideCharToMultiByte, DeviceIoControl
1:07:55 [FOUND] (69fe4f) - WriteFile, ReadFile, WriteProcessMemory
107:55 [FOUND] (69fd55) - WriteFile, ReadFile, WriteProcessMemory
1:07:55 [FOUND] (69fc75) - WriteFile, ReadFile, WriteProcessMemory
1:07:55 [FOUND] (69fa65) - FormatMessageW, SetWindowPos
4444);
("192.168.1.19");
MEMORY [ x7 2] (dword_683520, &word_68356C, 16, @, @, @, 2);
dword 683568 dword_683520;
dword_683564 = dword_683520;
dword_68356@ = dword_683520;
qword_68352C = 0164;
qword_683534 = 0164;
qword_68353C = 0164;
qword_683544 = 0164;
qword_68354C = 0164;
qword_683558 = 0164;
dword_683528 = 68;
dword_683554 = 256;
vi@ = xmmword_6821F0;
MEMORY f 8] (3600000) ;
le
}
000004FA sub 681000:26 (6810FA)
idle (Down Disk: 29GB)
we Jf
```

## Slide 39

**Conclusion and Takeaways**

**TXOne Networks  |  Keep the Operation Running**

## Slide 40

## **Constraint and Limitation of Practical Symbolic Engine**

- Difficulties of Taint Analysis with Multi-Threads / OLLVM-FLA

   - Prevent classic path explosion

   - The halting problem with OLLVM (FLA/CFF)

   - Multithread or cross-threading issue

- Boundary Coverage Issue of Uncovering All Functions in Stripped Binaries

   - “SoK: All You Ever Wanted to Know About x86/x64 Binary Disassembly”

   - State-of-the-art community disassemblers like Angr, Radare2, Ghidra uncover only about 80% of binary functions

- Even commercial or nationally supported disassemblers that use heuristic pattern-matching such as Binary Ninja, IDA Pro, BAP, achieve only about 95 ~ 98% coverage

TXOne Networks  |  Keep the Operation Running

## Slide 41

## **Takeaways**

- We have open-source our tool on GitHub to empower the Blue Team community

• https://github.com/TXOne-Networks/CuIDA

- Takeaways

   - Learn strategies for using machine learning on symbolic execution for practical malware analysis, even against advanced code obfuscation techniques, including well-known commercial solutions

   - Understand the limitations of existing auto-sandbox or pure AI-based malware detection systems, particularly when analyzing VC.Net samples (hybrid of C++ and MSIL)

TXOne Networks  |  Keep the Operation Running

## Slide 42

# **Thank you for your attention**

Keep the operation running!

TXOne Networks  |  Keep the Operation Running
