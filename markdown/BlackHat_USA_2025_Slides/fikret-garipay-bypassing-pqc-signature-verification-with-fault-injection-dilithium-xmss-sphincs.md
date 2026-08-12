---
title: "Bypassing PQC Signature Verification with Fault Injection Dilithium, XMSS, SPHINCS+"
speakers: ["Fikret Garipay"]
conference: "Black Hat"
conference_full: "Black Hat USA 2025"
edition: "USA"
year: 2025
source_pdf: "BlackHat_USA_2025_Slides/Fikret Garipay_Bypassing PQC Signature Verification with Fault Injection Dilithium, XMSS, SPHINCS+.pdf"
pages: 134
sha256: "6ec6810674f2195ea65a090e641f7e36b06244195889c17c898e27151d5e7282"
text_chars: 43496
ocr_pages: 2
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T22:53:56Z"
---
# Bypassing PQC Signature Verification with Fault Injection Dilithium, XMSS, SPHINCS+

**Speakers:** Fikret Garipay  
**Conference:** Black Hat USA 2025  
**Source:** `BlackHat_USA_2025_Slides/Fikret Garipay_Bypassing PQC Signature Verification with Fault Injection Dilithium, XMSS, SPHINCS+.pdf` (134 pages)

## Slide 1

# Bypassing PQC Signature Verification with Fault Injection: Dilithium, XMSS, SPHINCS+

Fikret Garipay

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
piSek hat
EFINGS
AUGUST be 2025
MANDALAY BAY / LAS VEGAS
Bypassing PQC Signature Verification with
Fault Injection: Dilithium, XMSS, SPHINCS+t
Fikret Garipay
```

## Slide 2

#### Hello!

- Security Engineer at Keysight Device Security Testing

- • Passionate about software exploitation and hardware attacks

- Twitter: @erd0spy

Fikret Garipay

2 #BHUSA @BlackHatEvents

## Slide 3

#### **Agenda**

- Introduction to Post Quantum Cryptography

- Target Implementation

- Voltage Fault Injection in Practice

- Fault Injection Attacks on Dilithium Verification

- Fault Injection Attacks on WOTS+ in XMSS and SPHINCS+

- Fault Injection on Fault Resistance XMSS Library

- Key Takeaways and Conclusions

3 #BHUSA @BlackHatEvents

## Slide 4

## Introduction to Post Quantum Cryptography

4 #BHUSA @BlackHatEvents

## Slide 5

#### **Post-Quantum Crypto Is Getting Real**

- Quantum computers aren’t breaking crypto yet.

- But the shift is underway – **standards** , **vendors** , **firmware** .

- PQC is set to replace RSA, ECC in **secure boot** , **firmware signing** , and more.

- That makes PQC **fresh attack surface** .

5 #BHUSA @BlackHatEvents

## Slide 6

#### **PQC Signatures Are Becoming Global Standards**

|**Algorithm**|**Signature Scheme Type**|**CNSA 2.0 (NSA)**|**Standard**|
|---|---|---|---|
|**Dilithium**|Lattice-based|**Required**for all digital
signatures (general use)|**NIST FIPS 204**
(ML-DSA)|
|**LMS**|Stateful hash-based|**Approved**for
firmware/software signing|ISO/IEC
14888-4:2024|
|**XMSS**|Stateful hash-based|**Approved**for
firmware/software signing|ISO/IEC
14888-4:2024|
|**SPHINCS+**|Stateless hash-based|**Not approved for any use in**
**NSS**|**NIST FIPS 205**
(SLH-DSA)|

6 #BHUSA @BlackHatEvents

## Slide 7

#### **PQC Signatures in Industry**

- Multiple vendors now offer PQC solutions for **Firmware Update** , **Secure Boot** , **Signature Verification**

Source: Fabrication begins for production OpenTitan silicon

7 #BHUSA @BlackHatEvents

## Slide 8

#### **PQC Signatures in Industry**

- Multiple vendors now offer PQC solutions for **Firmware Update** , **Secure Boot** , **Signature Verification**

- **OpenTitan** chip uses **SPHINCS+** for PQC secure boot

Source: Fabrication begins for production OpenTitan silicon

8 #BHUSA @BlackHatEvents

## Slide 9

#### **PQC Signatures in Industry**

- Multiple vendors now offer PQC solutions for **Firmware Update** , **Secure Boot** , **Signature Verification**

- **OpenTitan** chip uses **SPHINCS+** for PQC secure boot

- **Caliptra 2.0** is adding post-quantum secure boot with **Dilithium** and **Kyber**

Source: Fabrication begins for production OpenTitan silicon

9 #BHUSA @BlackHatEvents

## Slide 10

#### **Making the Attacks Real**

- We reviewed dozens of papers

- Focused on **practical attacks** AGAINST PQC signature verification

10 #BHUSA @BlackHatEvents

## Slide 11

#### **Making the Attacks Real**

- We reviewed dozens of papers

- Focused on **practical attacks** AGAINST PQC signature verification

- Public PQC targets aren’t widely deployed yet

- So, we:

Ported public PQC libs to bare-metal firmware

11 #BHUSA @BlackHatEvents

## Slide 12

## **Target Implementation**

12 #BHUSA @BlackHatEvents

## Slide 13

#### **Target Implementation – Libraries**

**Dilithium:** <u>pqm4</u>

- Post-quantum crypto library for the ARM Cortex-M4

- **XMSS:** <u>xmss-reference</u>

**SPHINCS+:** <u>sphincsplus</u>

13 #BHUSA @BlackHatEvents

## Slide 14

#### **Target Implementation – Libraries**

**Dilithium:** <u>pqm4</u>

- Post-quantum crypto library for the ARM Cortex-M4

- **XMSS:** <u>xmss-reference</u>

**SPHINCS+:** <u>sphincsplus</u>

**FI focus:** cryptographic logic only, no generic bypasses like memcmp() skips or forced returns

14 #BHUSA @BlackHatEvents

## Slide 15

**Target Implementation – Firmware STM32F417** , Arm Cortex-M4 core

Running **bare metal firmware** (open source on GitHub)

15 #BHUSA @BlackHatEvents

## Slide 16

**Target Implementation – Firmware STM32F417** , Arm Cortex-M4 core

Running **bare metal firmware** (open source on GitHub)

```
caseCMD_SW_DILITHIUM_VERIFY: {
```

```
uint8_t* signedMessageBuffer= DilithiumState_getScratchPad(&dilithium);
get_bytes(DILITHIUM_SIGNED_MESSAGE_SIZE, signedMessageBuffer);
// Handle the request.
```

```
BEGIN_INTERESTING_STUFF;// []-> Rising Edge Trigger
intresult = DilithiumState_verify(&dilithium, signedMessageBuffer);
END_INTERESTING_STUFF;// []-> Falling Edge Trigger
send_char(result == 0? 0: 1);
```

```
break;
```

```
}
```

16 #BHUSA @BlackHatEvents

## Slide 17

### Voltage Fault Injection on Practice

17 #BHUSA @BlackHatEvents

## Slide 18

#### **Voltage Fault Injection – Concepts**

- Lower the voltage **at the right time** to trigger faults

- Not ‘too soft’ ; Not ‘too hard’

18 #BHUSA @BlackHatEvents

## Slide 19

**Voltage Fault Injection – Effects on Device** Inject fault(s) to disturb the device, then see what happens:

- Nothing

- Device resets, stops working, or dies

19 #BHUSA @BlackHatEvents

## Slide 20

**Voltage Fault Injection – Effects on Device** Inject fault(s) to disturb the device, then see what happens:

- Nothing

- Device resets, stops working, or dies

- A **change** in software decision

- A computational **fault**

20

#BHUSA @BlackHatEvents

## Slide 21

**Voltage Fault Injection – Effects on Device** Inject fault(s) to disturb the device, then see what happens:

- Nothing

- Device resets, stops working, or dies

- A **change** in software decision

- A computational **fault**

May compromise the device!

21 #BHUSA @BlackHatEvents

## Slide 22

#### **Voltage Fault Injection – Setup Overview**

Oscilloscope
FPGA
A
B
Programmable
USB
Power Source
Ext
out
in
Glitch Out
Computer
Target
GPIO
USB USB UART
VCC
USB USB
Reset
GND
Trigger

22 #BHUSA @BlackHatEvents

## Slide 23

#### **Voltage Fault Injection – Real World**

Oscilloscope
PSU
FPGA

23 #BHUSA @BlackHatEvents

## Slide 24

### **Fault Injection Attacks on Dilithium Verification**

24 #BHUSA @BlackHatEvents

## Slide 25

#### **Introduction to Dilithium**

- Lattice-based digital signature scheme, designed to resist quantum attacks.

- Three security levels: Dilithium-2, Dilithium-3, Dilithium-5

- Supports deterministic and randomized signing for flexibility.

- • Optimized using Number Theoretic Transform (NTT) for efficiency.

25 #BHUSA @BlackHatEvents

## Slide 26

#### **Keygen**

1. 𝐀 ← 𝑅𝑞<sup>𝑘×𝑙</sup> 2. 𝐬1, 𝐬2 ← 𝑆𝜂<sup>𝑙</sup> × 𝑆𝜂<sup>𝑘</sup> 3. 𝐭≔𝐀𝐬1 + 𝐬2 4. 𝐭1, 𝐭0 = 𝐏𝐨𝐰𝐞𝐫𝟐𝐑𝐨𝐮𝐧𝐝(𝐭, 𝑑) 5. 𝐫𝐞𝐭𝐮𝐫𝐧(𝑝𝑘= 𝐀, t1 , 𝑠𝑘= 𝐀, 𝐬1, 𝐬2, t0 )

26 #BHUSA @BlackHatEvents

## Slide 27

#### **Keygen**

1. 𝐀 ← 𝑅𝑞<sup>𝑘×𝑙</sup> 2. 𝐬1, 𝐬2 ← 𝑆𝜂<sup>𝑙</sup> × 𝑆𝜂<sup>𝑘</sup>

3. 𝐭≔𝐀𝐬1 + 𝐬2

4. 𝐭1, 𝐭0 = 𝐏𝐨𝐰𝐞𝐫𝟐𝐑𝐨𝐮𝐧𝐝(𝐭, 𝑑)

5. 𝐫𝐞𝐭𝐮𝐫𝐧(𝑝𝑘= 𝐀, t1 , 𝑠𝑘= 𝐀, 𝐬1, 𝐬2, t0 )

- Expand matrix 𝐀 from public seed.

27 #BHUSA @BlackHatEvents

## Slide 28

#### **Keygen**

1. 𝐀 ← 𝑅𝑞<sup>𝑘×𝑙</sup> 2. 𝐬1, 𝐬2 ← 𝑆𝜂<sup>𝑙</sup> × 𝑆𝜂<sup>𝑘</sup>

3. 𝐭≔𝐀𝐬1 + 𝐬2

4. 𝐭1, 𝐭0 = 𝐏𝐨𝐰𝐞𝐫𝟐𝐑𝐨𝐮𝐧𝐝(𝐭, 𝑑)

5. 𝐫𝐞𝐭𝐮𝐫𝐧(𝑝𝑘= 𝐀, t1 , 𝑠𝑘= 𝐀, 𝐬1, 𝐬2, t0 )

- Expand matrix 𝐀 from public seed.

- Sample secret vectors 𝐬1 and 𝐬2

28 #BHUSA @BlackHatEvents

## Slide 29

#### **Keygen**

1. 𝐀 ← 𝑅𝑞<sup>𝑘×𝑙</sup> 2. 𝐬1, 𝐬2 ← 𝑆𝜂<sup>𝑙</sup> × 𝑆𝜂<sup>𝑘</sup> 3. 𝐭≔𝐀𝐬1 + 𝐬2 4. 𝐭1, 𝐭0 = 𝐏𝐨𝐰𝐞𝐫𝟐𝐑𝐨𝐮𝐧𝐝(𝐭, 𝑑)

5. 𝐫𝐞𝐭𝐮𝐫𝐧(𝑝𝑘= 𝐀, t1 , 𝑠𝑘= 𝐀, 𝐬1, 𝐬2, t0 )

- Expand matrix 𝐀 from public seed.

- Sample secret vectors 𝐬1 and 𝐬2

- Compute 𝐭 , then split into 𝐭1 **(public)** and 𝐭0 **(secret)** .

29 #BHUSA @BlackHatEvents

## Slide 30

#### **Keygen**

1. 𝐀 ← 𝑅𝑞<sup>𝑘×𝑙</sup> 2. 𝐬1, 𝐬2 ← 𝑆𝜂<sup>𝑙</sup> × 𝑆𝜂<sup>𝑘</sup>

3. 𝐭≔𝐀𝐬1 + 𝐬2

4. 𝐭1, 𝐭0 = 𝐏𝐨𝐰𝐞𝐫𝟐𝐑𝐨𝐮𝐧𝐝(𝐭, 𝑑)

5. 𝐫𝐞𝐭𝐮𝐫𝐧(𝑝𝑘= 𝐀, t1 , 𝑠𝑘= 𝐀, 𝐬1, 𝐬2, t0 )

- Expand matrix 𝐀 from public seed.

- Sample secret vectors 𝐬1 and 𝐬2

- Compute 𝐭 , then split into 𝐭1 **(public)** and 𝐭0 **(secret)** .

30 #BHUSA @BlackHatEvents

## Slide 31

#### **Sign** ( 𝑴, 𝑠𝑘= 𝐀, 𝐬1, 𝐬2, t0 )

1. (𝐳, ℎ) ≔⊥

2. 𝐰𝐡𝐢𝐥𝐞(𝐳, ℎ) = ⊥𝐝𝐨

3. 𝐲 ← 𝑆𝛾𝑙1

4. 𝐰1 ≔ 𝐇𝐢𝐠𝐡𝐁𝐢𝐭𝐬 𝐀𝐲, 2γ2

5. 𝑐∈𝐵𝜏 ≔H 𝑴∥𝐰1

6. 𝐳≔𝐲+ 𝑐𝐬1

7. 𝐢𝐟rejection conditions met →𝐭 hen z ≔⊥ 8. 𝐞𝐥𝐬𝐞

9. ℎ= 𝐌𝐚𝐤𝐞𝐇𝐢𝐧𝐭(−𝑐t0, 𝐰−𝑐𝐬𝟐 + 𝑐𝐭0)

10. 𝐢𝐟 𝑐𝐭0 ∞ ≥ γ2, 𝐭𝐡𝐞𝐧 𝐳, ℎ= ⊥

11. 𝐫𝐞𝐭𝐮𝐫𝐧σ = (𝒄, 𝐳, ℎ)

31

#BHUSA @BlackHatEvents

## Slide 32

#### **Sign** ( 𝑴, 𝑠𝑘= 𝐀, 𝐬1, 𝐬2, t0 )

1. (𝐳, ℎ) ≔⊥

2. 𝐰𝐡𝐢𝐥𝐞(𝐳, ℎ) = ⊥𝐝𝐨

3. 𝐲 ← 𝑆𝛾𝑙1

4. 𝐰1 ≔ 𝐇𝐢𝐠𝐡𝐁𝐢𝐭𝐬 𝐀𝐲, 2γ2

   - Rejection loop samples y, computes challenge 𝑐 , computes 𝐳 , and verifies constraints.

5. 𝑐∈𝐵𝜏 ≔H 𝑴∥𝐰1

6. 𝐳≔𝐲+ 𝑐𝐬1

7. 𝐢𝐟rejection conditions met →𝐭 hen z ≔⊥

8. 𝐞𝐥𝐬𝐞

9. ℎ= 𝐌𝐚𝐤𝐞𝐇𝐢𝐧𝐭(−𝑐t0, 𝐰−𝑐𝐬𝟐 + 𝑐𝐭0)

10. 𝐢𝐟 𝑐𝐭0 ∞ ≥ γ2, 𝐭𝐡𝐞𝐧 𝐳, ℎ= ⊥

11. 𝐫𝐞𝐭𝐮𝐫𝐧σ = (𝒄, 𝐳, ℎ)

32

#BHUSA @BlackHatEvents

## Slide 33

#### **Sign** ( 𝑴, 𝑠𝑘= 𝐀, 𝐬1, 𝐬2, t0 )

1. (𝐳, ℎ) ≔⊥

2. 𝐰𝐡𝐢𝐥𝐞(𝐳, ℎ) = ⊥𝐝𝐨

   - 𝑙1

3. 𝐲 ← 𝑆𝛾𝑙1

4. 𝐰1 ≔ 𝐇𝐢𝐠𝐡𝐁𝐢𝐭𝐬 𝐀𝐲, 2γ2

5. 𝑐∈𝐵𝜏 ≔H 𝑴∥𝐰1

6. 𝐳≔𝐲+ 𝑐𝐬1

   - Rejection loop samples y, computes challenge 𝑐 , computes 𝐳 , and verifies constraints.

   - Verifier lacks t0 , so hint ℎ helps recover 𝐰1.

7. 𝐢𝐟rejection conditions met →𝐭 hen z ≔⊥

8. 𝐞𝐥𝐬𝐞

9. ℎ= 𝐌𝐚𝐤𝐞𝐇𝐢𝐧𝐭(−𝑐t0, 𝐰−𝑐𝐬𝟐 + 𝑐𝐭0)

10. 𝐢𝐟 𝑐𝐭0 ∞ ≥ γ2, 𝐭𝐡𝐞𝐧 𝐳, ℎ= ⊥

11. 𝐫𝐞𝐭𝐮𝐫𝐧σ = (𝒄, 𝐳, ℎ)

33 #BHUSA @BlackHatEvents

## Slide 34

#### **Sign** ( 𝑴, 𝑠𝑘= 𝐀, 𝐬1, 𝐬2, t0 )

1. (𝐳, ℎ) ≔⊥

2. 𝐰𝐡𝐢𝐥𝐞(𝐳, ℎ) = ⊥𝐝𝐨

   - 𝑙1

3. 𝐲 ← 𝑆𝛾𝑙1

4. 𝐰1 ≔ 𝐇𝐢𝐠𝐡𝐁𝐢𝐭𝐬 𝐀𝐲, 2γ2

5. 𝑐∈𝐵𝜏 ≔H 𝑴∥𝐰1

6. 𝐳≔𝐲+ 𝑐𝐬1

   - Rejection loop samples y, computes challenge 𝑐 , computes 𝐳 , and verifies constraints.

   - Verifier lacks t0 , so hint ℎ helps recover 𝐰1.

7. 𝐢𝐟rejection conditions met →𝐭 hen z ≔⊥

8. 𝐞𝐥𝐬𝐞

9. ℎ= 𝐌𝐚𝐤𝐞𝐇𝐢𝐧𝐭(−𝑐t0, 𝐰−𝑐𝐬𝟐 + 𝑐𝐭0)

10. 𝐢𝐟 𝑐𝐭0 ∞ ≥ γ2, 𝐭𝐡𝐞𝐧 𝐳, ℎ= ⊥

11. 𝐫𝐞𝐭𝐮𝐫𝐧σ = (𝒄, 𝐳, ℎ)

34

#BHUSA @BlackHatEvents

## Slide 35

**Verify** ( 𝑝𝑘= 𝐀, t1 , 𝑀, σ = (𝑐, 𝐳, ℎ) )

1. 𝐰1′ ≔ 𝐔𝐬𝐞𝐇𝐢𝐧𝐭 ℎ, 𝐀𝐳−𝑐𝐭12<sup>𝑑</sup> 2. 𝐢𝐟 𝐳 ∞ < γ1 −𝛽𝐚𝐧𝐝𝑐= 𝐇 𝑀∥𝐰1′ 𝐚𝐧𝐝 ℎ ℎ𝑗=1 ≤ 𝜔 3. 𝐫𝐞𝐭𝐮𝐫𝐧𝐓𝐫𝐮𝐞

4. 𝐞𝐥𝐬𝐞

5. 𝐫𝐞𝐭𝐮𝐫𝐧𝐅𝐚𝐥𝐬𝐞

35 #BHUSA @BlackHatEvents

## Slide 36

#### **Verify** ( 𝑝𝑘= 𝐀, t1 , 𝑀, σ = (𝑐, 𝐳, ℎ) )

1. 𝐰1′ ≔ 𝐔𝐬𝐞𝐇𝐢𝐧𝐭 ℎ, 𝐀𝐳−𝑐𝐭12<sup>𝑑</sup> 2. 𝐢𝐟 𝐳 ∞ < γ1 −𝛽𝐚𝐧𝐝𝑐= 𝐇 𝑀∥𝐰1′ 𝐚𝐧𝐝 ℎ ℎ𝑗=1 ≤ 𝜔 3. 𝐫𝐞𝐭𝐮𝐫𝐧𝐓𝐫𝐮𝐞

4. 𝐞𝐥𝐬𝐞

5. 𝐫𝐞𝐭𝐮𝐫𝐧𝐅𝐚𝐥𝐬𝐞

- Computes high bits of 𝐀𝐳−𝑐𝐭12<sup>𝑑</sup>

36 #BHUSA @BlackHatEvents

## Slide 37

#### **Verify** ( 𝑝𝑘= 𝐀, t1 , 𝑀, σ = (𝑐, 𝐳, ℎ) )

1. 𝐰1′ ≔ 𝐔𝐬𝐞𝐇𝐢𝐧𝐭 ℎ, 𝐀𝐳−𝑐𝐭12<sup>𝑑</sup>

2. 𝐢𝐟 𝐳 ∞ < γ1 −𝛽𝐚𝐧𝐝𝑐= 𝐇 𝑀∥𝐰1′ 𝐚𝐧𝐝 ℎ ℎ𝑗=1 ≤ 𝜔 3. 𝐫𝐞𝐭𝐮𝐫𝐧𝐓𝐫𝐮𝐞

4. 𝐞𝐥𝐬𝐞

5. 𝐫𝐞𝐭𝐮𝐫𝐧𝐅𝐚𝐥𝐬𝐞

- Computes high bits of 𝐀𝐳−𝑐𝐭12<sup>𝑑</sup>

- Correct with hint vector ℎ.

37 #BHUSA @BlackHatEvents

## Slide 38

#### **Verify** ( 𝑝𝑘= 𝐀, t1 , 𝑀, σ = (𝑐, 𝐳, ℎ) )

1. 𝐰1′ ≔ 𝐔𝐬𝐞𝐇𝐢𝐧𝐭 ℎ, 𝐀𝐳−𝑐𝐭12<sup>𝑑</sup>

2. 𝐢𝐟 𝐳 ∞ < γ1 −𝛽𝐚𝐧𝐝𝑐= 𝐇 𝑀∥𝐰1′ 𝐚𝐧𝐝 ℎ ℎ𝑗=1 ≤ 𝜔

3. 𝐫𝐞𝐭𝐮𝐫𝐧𝐓𝐫𝐮𝐞

4. 𝐞𝐥𝐬𝐞

5. 𝐫𝐞𝐭𝐮𝐫𝐧𝐅𝐚𝐥𝐬𝐞

- Computes high bits of 𝐀𝐳−𝑐𝐭12<sup>𝑑</sup>

- Correct with hint vector ℎ.

- Recomputes 𝐰1′ and challenge 𝑐 from message.

38 #BHUSA @BlackHatEvents

## Slide 39

**Verify** ( 𝑝𝑘= 𝐀, t1 , 𝑀, σ = (𝑐, 𝐳, ℎ) )

1. 𝐰1′ ≔ 𝐔𝐬𝐞𝐇𝐢𝐧𝐭 ℎ, 𝐀𝐳−𝑐𝐭12<sup>𝑑</sup> 2. 𝐢𝐟 𝐳 ∞ < γ1 −𝛽𝐚𝐧𝐝𝑐= 𝐇 𝑀∥𝐰1′ 𝐚𝐧𝐝 ℎ ℎ𝑗=1 ≤ 𝜔 3. 𝐫𝐞𝐭𝐮𝐫𝐧𝐓𝐫𝐮𝐞

4. 𝐞𝐥𝐬𝐞

5. 𝐫𝐞𝐭𝐮𝐫𝐧𝐅𝐚𝐥𝐬𝐞

- Computes high bits of 𝐀𝐳−𝑐𝐭12<sup>𝑑</sup>

- Correct with hint vector ℎ.

- Recomputes 𝐰1′ and challenge 𝑐 from message.

39 #BHUSA @BlackHatEvents

## Slide 40

#### **Fault Attack on Dilithium Verification**

• This research builds on _<u>Fault Attacks Sensitivity of Public Parameters in the Dilithium Verification</u>_ (CARDIS 2023).

40 #BHUSA @BlackHatEvents

## Slide 41

- **Fault Attack on Dilithium Verification** • This research builds on _<u>Fault Attacks Sensitivity of Public Parameters in the Dilithium Verification</u>_ (CARDIS 2023).

> ′ ≔𝐔𝐬𝐞𝐇𝐢𝐧𝐭 **Verification Line 1:** 𝐰1 ℎ, 𝐀𝐳−𝑐𝐭12<sup>𝑑</sup>

41 #BHUSA @BlackHatEvents

## Slide 42

- **Fault Attack on Dilithium Verification** Fault Attacks Sensitivity of Public Parameters in the

- • This research builds onDilithium Verification _<u>Fault Attacks Sensitivity of Public Parameters in the Dilithium Verification</u>_ (CARDIS 2023).

> ′ ≔𝐔𝐬𝐞𝐇𝐢𝐧𝐭 **Verification Line 1:** 𝐰1 ℎ, 𝐀𝐳−𝑐𝐭12<sup>𝑑</sup>

- The paper shows how to recover 𝐰𝟏 using only public inputs.

42 #BHUSA @BlackHatEvents

## Slide 43

- **Fault Attack on Dilithium Verification** Fault Attacks Sensitivity of Public Parameters in the

- • This research builds onDilithium Verification _<u>Fault Attacks Sensitivity of Public Parameters in the Dilithium Verification</u>_ (CARDIS 2023).

> ′ ≔𝐔𝐬𝐞𝐇𝐢𝐧𝐭 **Verification Line 1:** 𝐰1 ℎ, 𝐀𝐳−𝑐𝐭12<sup>𝑑</sup>

- The paper shows how to recover 𝐰𝟏 using only public inputs.

- It demonstrates how to constrain 𝒄𝒕𝟏𝟐<sup>𝒅</sup> to minimally affect 𝑨𝒛 ’s high bits.

43 #BHUSA @BlackHatEvents

## Slide 44

- **Fault Attack on Dilithium Verification** Fault Attacks Sensitivity of Public Parameters in the

- • This research builds onDilithium Verification _<u>Fault Attacks Sensitivity of Public Parameters in the Dilithium Verification</u>_ (CARDIS 2023).

> ′ ≔𝐔𝐬𝐞𝐇𝐢𝐧𝐭 **Verification Line 1:** 𝐰1 ℎ, 𝐀𝐳−𝑐𝐭12<sup>𝑑</sup>

- The paper shows how to recover 𝐰𝟏 using only public inputs.

- It demonstrates how to constrain 𝒄𝒕𝟏𝟐<sup>𝒅</sup> to minimally affect 𝑨𝒛 ’s high bits.

- Using this, it presents two signature verification attacks **- exploiting verification with FI.**

44 #BHUSA @BlackHatEvents

## Slide 45

#### **Attacks**

_If either of the following conditions is met during a successful fault injection at verification:_ **Attack 1.**

###### **Attack 2.**

- _A signature generated using only public values_ **_will be accepted as valid_** _._

45 #BHUSA @BlackHatEvents

## Slide 46

#### **Attacks**

_If either of the following conditions is met during a successful fault injection at verification:_ **Attack 1.** 𝑐𝐭12<sup>𝑑</sup> = 0

###### **Attack 2.**

- _A signature generated using only public values_ **_will be accepted as valid_** _._

46 #BHUSA @BlackHatEvents

## Slide 47

#### **Attacks**

_If either of the following conditions is met during a successful fault injection at verification:_ **Attack 1.** 𝑐𝐭12<sup>𝑑</sup> = 0 **Attack 2.** 𝑐𝐭12<sup>𝑑</sup> 𝑐𝐭12<sup>𝑑</sup> , 𝐀𝐳−𝑐𝐭12<sup>𝑑</sup> ∞<sup>≤𝛾2</sup><sup>**and**ℎ= 𝐌𝐚𝐤𝐞𝐇𝐢𝐧𝐭</sup> **Then** , 𝐇𝐢𝐠𝐡𝐁𝐢𝐭𝐬 𝐴𝑧−𝑐𝐭12<sup>𝑑</sup> , 2γ2 = 𝐇𝐢𝐠𝐡𝐁𝐢𝐭𝐬 𝐰, 2γ2

- _A signature generated using only public values_ **_will be accepted as valid_** _._

47 #BHUSA @BlackHatEvents

## Slide 48

##### **Our Signature Generation for Attack 1** ( 𝑴, 𝑝𝑘= 𝐀, t1 )

1. 𝐳≔⊥

2. 𝐰𝐡𝐢𝐥𝐞 𝐳= ⊥𝐝𝐨

- 𝑙

- 3. **z** ←𝑆𝛾1−𝛽

4. ℎ= 0

   - The generated signature will accept by verification if fault forces 𝒄𝐭𝟏𝟐<sup>𝒅</sup> **= 0 at signature verification.**

5. 𝐰1 ≔𝐔𝐬𝐞𝐇𝐢𝐧𝐭 ℎ, 𝐀𝐳, 2γ2

6. 𝑐∈𝐵𝜏 ≔H 𝑴∥𝐰1

7. 𝐫𝐞𝐭𝐮𝐫𝐧σ = (𝒄, 𝐳, ℎ)

48 #BHUSA @BlackHatEvents

## Slide 49

##### **Our Signature Generation for Attack 2** ( 𝑴, 𝑝𝑘= 𝐀, t1 )

**1.** 𝐳, ℎ≔⊥

2. 𝐰𝐡𝐢𝐥𝐞 𝐳, ℎ= ⊥𝐝𝐨

- 𝑙

- 3. **z** ←𝑆𝛾1−𝛽 4. ℎ= 0

   - The generated signature will accept by verification if fault forces 𝒄𝐭𝟏𝟐<sup>𝒅</sup> ∞<sup>**≤**𝜸𝟐</sup><sup>**at**</sup>

   - **signature verification.**

5. 𝐰1 ≔𝐇𝐢𝐠𝐡𝐁𝐢𝐭𝐬 ℎ, 𝐀𝐳, 2γ2

6. 𝑐∈𝐵𝜏 ≔H 𝑴∥𝐰1

7. ℎ= 𝐌𝐚𝐤𝐞𝐇𝐢𝐧𝐭(−𝑐𝐭12<sup>𝑑′</sup> , 𝐀𝐳−𝑐𝐭12<sup>𝑑′</sup> )

8. 𝐢𝐟 ℎ ℎ𝑗=1 > ω, 𝐭𝐡𝐞𝐧 𝐳, ℎ= ⊥

9. 𝐫𝐞𝐭𝐮𝐫𝐧σ = (𝒄, 𝐳, ℎ)

49 #BHUSA @BlackHatEvents

## Slide 50

#### **Where to target?**

> ′ ≔𝐔𝐬𝐞𝐇𝐢𝐧𝐭 𝐰1 ℎ, 𝐀𝐳−𝑐𝐭12<sup>𝑑</sup>

50 #BHUSA @BlackHatEvents

## Slide 51

#### **Where to target?**

> ′ ≔𝐔𝐬𝐞𝐇𝐢𝐧𝐭 𝐰1 ℎ, 𝐀𝐳−𝑐𝐭12<sup>𝑑</sup>

51 #BHUSA @BlackHatEvents

## Slide 52

#### **Where to target?**

**Scenario 1:** Unpacking of Public Key* • **Attack 1** ( 𝑐𝐭12<sup>𝑑</sup> = 0)

> ′ ≔𝐔𝐬𝐞𝐇𝐢𝐧𝐭 𝐰1 ℎ, 𝐀𝐳−𝑐𝐭12<sup>𝑑</sup>

*Depends on implementation and compiler behavior. Requires zero-initialized 𝐭1 coefficients.

52

#BHUSA @BlackHatEvents

## Slide 53

#### **Where to target?**

**Scenario 1:** Unpacking of Public Key*

• **Attack 1** ( 𝑐𝐭12<sup>𝑑</sup> = 0)

**Scenario 2:** Sampling of c • **Attack 1** ( 𝑐𝐭12<sup>𝑑</sup> = 0)

> ′ ≔𝐔𝐬𝐞𝐇𝐢𝐧𝐭 𝐰1 ℎ, 𝐀𝐳−𝑐𝐭12<sup>𝑑</sup>

*Depends on implementation and compiler behavior. Requires zero-initialized 𝐭1 coefficients.

53

#BHUSA @BlackHatEvents

## Slide 54

#### **Where to target?**

**Scenario 1:** Unpacking of Public Key*

- **Attack 1** ( 𝑐𝐭12<sup>𝑑</sup> = 0)

- **Scenario 2:** Sampling of c • **Attack 1** ( 𝑐𝐭12<sup>𝑑</sup> = 0)

> ′ ≔𝐔𝐬𝐞𝐇𝐢𝐧𝐭 𝐰1 ℎ, 𝐀𝐳−𝑐𝐭12<sup>𝑑</sup>

**Scenario 3:** Shift by d • **Attack 2** ( 𝑐𝐭12<sup>𝑑</sup> = 𝑐𝐭12<sup>𝑑</sup> ∞<sup>≤𝛾2)</sup>

*Depends on implementation and compiler behavior. Requires zero-initialized 𝐭1 coefficients.

54

#BHUSA @BlackHatEvents

## Slide 55

#### **Where to target?**

**Scenario 1:** Unpacking of Public Key*

- **Attack 1** ( 𝑐𝐭12<sup>𝑑</sup> = 0)

- **Scenario 2:** Sampling of c • **Attack 1** ( 𝑐𝐭12<sup>𝑑</sup> = 0)

> ′ ≔𝐔𝐬𝐞𝐇𝐢𝐧𝐭 𝐰1 ℎ, 𝐀𝐳−𝑐𝐭12<sup>𝑑</sup>

**Scenario 3:** Shift by d • **Attack 2** ( 𝑐𝐭12<sup>𝑑</sup> = 𝑐𝐭12<sup>𝑑</sup> ∞<sup>≤𝛾2)</sup>

- **Scenario 4:** Subtraction • **Attack 1** ( 𝑐𝐭12<sup>𝑑</sup> = 0)

*Depends on implementation and compiler behavior. Requires zero-initialized 𝐭1 coefficients.

55

#BHUSA @BlackHatEvents

## Slide 56

#### **Where to target?**

**Scenario 1:** Unpacking of Public Key*

- **Attack 1** ( 𝑐𝐭12<sup>𝑑</sup> = 0)

**Scenario 2:** Sampling of c

- **Attack 1** ( 𝑐𝐭12<sup>𝑑</sup> = 0)

> ′ ≔𝐔𝐬𝐞𝐇𝐢𝐧𝐭 𝐰1 ℎ, 𝐀𝐳−𝑐𝐭12<sup>𝑑</sup>

**Scenario 3:** Shift by d

- **Attack 2** ( 𝑐𝐭12<sup>𝑑</sup> = 𝑐𝐭12<sup>𝑑</sup> ∞<sup>≤𝛾2)</sup>

**Scenario 4:** Subtraction

- **Attack 1** ( 𝑐𝐭12<sup>𝑑</sup> = 0)

*Depends on implementation and compiler behavior. Requires zero-initialized 𝐭1 coefficients.

56

#BHUSA @BlackHatEvents

## Slide 57

#### **How to Target?**

Chose the fault injection point

57 #BHUSA @BlackHatEvents

## Slide 58

#### **How to Target?**

Chose the fault injection point

Generate a signature using public key and an **arbitrary message**

58 #BHUSA @BlackHatEvents

## Slide 59

#### **How to Target?**

Chose the fault injection point

Generate a signature using public key and an **arbitrary message**

Inject the fault at the target **during verification**

59 #BHUSA @BlackHatEvents

## Slide 60

### Fault Injection Results

60 #BHUSA @BlackHatEvents

## Slide 61

###### **Scenario 2: Sampling of c**

`1. void poly_challenge(poly *c, const uint8_t seed[SEEDBYTES]) {`

`6. for(i = N-TAU; i < N; ++i) {`

`7. ...`

```
2.unsignedinti, b, pos;
```

`3. ...`

```
4.for(i= 0; i< N; ++i)
```

```
5.c->coeffs[i] = 0;
```

```
8.c->coeffs[i] = c->coeffs[b];
```

```
9.c->coeffs[b] = 1-2*(signs & 1);
```

`10. ...`

```
11.}
```

PQM4: Dilithium verification source code

61

#BHUSA @BlackHatEvents

## Slide 62

###### **Scenario 2: Sampling of c**

`1. void poly_challenge(poly *c, const uint8_t seed[SEEDBYTES]) {`

   `6. for(i = N-TAU; i < N; ++i) {`

   `7. ...`

`2. unsigned int i, b, pos;`

`3. ...`

`4. for(i = 0; i < N; ++i)`

`5. c->coeffs[i] = 0;`

`8. c->coeffs[i] = c->coeffs[b];`

```
9.c->coeffs[b] = 1-2*(signs & 1);
```

`10. ...`

```
11.}
```

PQM4: Dilithium verification source code

62

#BHUSA @BlackHatEvents

## Slide 63

###### **Scenario 2: Sampling of c**

`1. void poly_challenge(poly *c, const uint8_t seed[SEEDBYTES]) {`

###### `6. for(i = N-TAU; i < N; ++i) {`

   `7. ...`

`2. unsigned int i, b, pos; 3. ...`

```
4.for(i= 0; i< N; ++i)
```

```
5.c->coeffs[i] = 0;
```

`8. c->coeffs[i] = c->coeffs[b]; 9. c->coeffs[b] = 1 - 2*(signs & 1);`

`10. ...`

```
11.}
```

PQM4: Dilithium verification source code

63

#BHUSA @BlackHatEvents

## Slide 64

###### **Scenario 2: Sampling of c**

`1. void poly_challenge(poly *c, const uint8_t seed[SEEDBYTES]) {`

```
6.for(i= N-TAU; i< N; ++i) {
```

```
7....
```

`2. unsigned int i, b, pos;`

```
3....
```

```
4.for(i= 0; i< N; ++i)
```

```
5.c->coeffs[i] = 0;
```

```
8.c->coeffs[i] = c->coeffs[b];
9.c->coeffs[b] = 1-2*(signs & 1);
10....
11.}
```

PQM4: Dilithium verification source code

- If the fault is injected in second for loop of the **poly_challenge** function, the **for loop will be skipped.**

- As a result, each coefficient of 𝑐 will be equal to **zero** , **enabling Attack 1** ( 𝑐𝐭12<sup>𝑑</sup> = 0)

64

#BHUSA @BlackHatEvents

## Slide 65

#### **Scenario 2: Sampling of C**

- Green: Normal Execution

- Yellow: Mute/Reset

- Red: Success

Fault Injection Plot of Sampling of C Scenario

65 #BHUSA @BlackHatEvents

## Slide 66

#### **Scenario 3: Shift by d**

```
voidpolyveck_shiftl(polyveck *v) {
unsignedinti;
```

```
for(i = 0; i < K; ++i)
poly_shiftl(&v->vec[i]);
```

```
voidpoly_shiftl(poly *a) {
```

```
...
for(i = 0; i < N; ++i)
a->coeffs[i] <<= D;
```

PQM4: Dilithium verification source code

66 #BHUSA @BlackHatEvents

## Slide 67

#### **Scenario 3: Shift by d**

```
voidpolyveck_shiftl(polyveck *v) {
unsignedinti;
```

```
for(i = 0; i < K; ++i)
poly_shiftl(&v->vec[i]);
```

```
voidpoly_shiftl(poly *a) {
```

```
...
for(i = 0; i < N; ++i)
a->coeffs[i] <<= D;
```

PQM4: Dilithium verification source code

67 #BHUSA @BlackHatEvents

## Slide 68

#### **Scenario 3: Shift by d**

```
voidpolyveck_shiftl(polyveck *v) {
unsignedinti;
for(i = 0; i < K; ++i)
poly_shiftl(&v->vec[i]);
```

```
voidpoly_shiftl(poly *a) {
...
for(i = 0; i < N; ++i)
a->coeffs[i] <<= D;
```

PQM4: Dilithium verification source code

- If the fault is injected at **for loop** of the **polyveck_shiftl** function, the entire **for** loop will be skipped.

- As a result, **each coefficient of** 𝐭1 **will remain unshifted.**

- • 𝑐𝐭12<sup>𝑑</sup> ∞<sup>≤𝛾2, enabling</sup><sup>**Attack 2**with𝑑′= 0</sup>

68 #BHUSA @BlackHatEvents

## Slide 69

#### **Scenario 3: Shift by d**

- Green: Normal Execution

- Yellow: Mute/Reset

- Red: Success

Fault Injection Plot of Shift by d Scenario

69 #BHUSA @BlackHatEvents

## Slide 70

#### **Scenario 4: Subtraction**

```
voidpolyveck_sub(polyveck *w, constpolyveck *u, const
polyveck *v) {
```

```
unsignedinti;
for(i = 0; i < K; ++i){
```

```
send_char(dilithium_counter);
poly_sub(&w->vec[i], &u->vec[i], &v->vec[i]);}
```

```
}
```

PQM4: Dilithium verification source code

70

#BHUSA @BlackHatEvents

## Slide 71

#### **Scenario 4: Subtraction**

```
voidpolyveck_sub(polyveck *w, constpolyveck *u, const
polyveck *v) {
```

```
unsignedinti;
for(i = 0; i < K; ++i) {
send_char(dilithium_counter);
poly_sub(&w->vec[i], &u->vec[i], &v->vec[i]);}
```

```
}
```

PQM4: Dilithium verification source code

71 #BHUSA @BlackHatEvents

## Slide 72

#### **Scenario 4: Subtraction**

```
voidpolyveck_sub(polyveck *w, constpolyveck *u, const
polyveck *v) {
unsignedinti;
for(i = 0; i < K; ++i){
```

```
send_char(dilithium_counter);
poly_sub(&w->vec[i], &u->vec[i], &v->vec[i]);}
```

```
}
```

PQM4: Dilithium verification source code

- If a fault is injected at **for loop** of the **`polyveck_sub`** function, the entire **for** loop will be skipped

- As a result, the subtraction is not performed, so: 𝐀𝐳−𝑐𝐭12<sup>𝑑</sup> = 𝐀𝐳 (Attack 1)

72 #BHUSA @BlackHatEvents

## Slide 73

#### **Scenario 4: Subtraction**

- Green: Normal Execution

- Yellow: Mute/Reset

- Red: Success

Fault Injection Plot of Subtraction Scenario

73 #BHUSA @BlackHatEvents

## Slide 74

#### **Summary of FI on Dilithium**

- Fault Injection on **Dilithium** , can target verification operations like **initialization, challenge generation, shifting,** or **subtraction** .

74 #BHUSA @BlackHatEvents

## Slide 75

#### **Summary of FI on Dilithium**

- Fault Injection on **Dilithium** , can target verification operations like **initialization, challenge generation, shifting,** or **subtraction** .

- **These faults allow bypassing the scheme's logic to accept attackergenerated signatures.**

75 #BHUSA @BlackHatEvents

## Slide 76

#### **Summary of FI on Dilithium**

- Fault Injection on **Dilithium** , can target verification operations like **initialization, challenge generation, shifting,** or **subtraction** .

- **These faults allow bypassing the scheme's logic to accept attackergenerated signatures.**

- The **attack surface and behavior vary significantly across implementations** , making fault resistance hard to generalize.

76 #BHUSA @BlackHatEvents

## Slide 77

### **Bypassing WOTS+ Based Hash Based Signature Verification via Fault Injection**

77 #BHUSA @BlackHatEvents

## Slide 78

#### **Introduction to Hash Based Signatures**

- Hash-based cryptography builds on the cryptographic hash functions.

- Since quantum computers struggle to break secure hash functions, these schemes remain resistant .

- This talk focuses on their fundamental building block: **Winternitz One-Time Signature (WOTS+).**

78

#BHUSA @BlackHatEvents

## Slide 79

#### **Introduction to WOTS**

Message
Chunks Secret Key Public Key
• Winternitz Parameter:
𝐻 𝐻 𝐻
0b10 𝑠𝑘 0 𝑠𝑖𝑔 0
𝑤= 4
• Hash Chain Length: 𝐻 𝐻 𝐻
0b01 𝑠𝑘 1 𝑠𝑖𝑔 1
𝑤−1 = 3 K 𝑝𝑘
𝐻 𝐻 𝐻
0b11 𝑠𝑘 2 𝑠𝑖𝑔 2
• Chunk Bit Size:
𝑙𝑜𝑔2 𝑤= 2 𝐻 𝐻 𝐻
0b00 𝑠𝑘 3 𝑠𝑖𝑔 3

79

#BHUSA @BlackHatEvents

## Slide 80

**Signature Generation: Split message hash into chunks** • 𝑚= [𝑚0, 𝑚1, … , 𝑚𝑙1−1] _(Each_ 𝑚𝑖 _is in_ [0, 𝑤−1] _)_

Message Hash
𝑚0 𝑚1 𝑚2 𝑚3

80 #BHUSA @BlackHatEvents

## Slide 81

**Signature Generation: Signing** • 𝑠𝑖𝑔 𝑖= ℎ𝑎𝑠ℎ_𝑐ℎ𝑎𝑖𝑛(𝑠𝑘 𝑖, 𝑠𝑡𝑒𝑝𝑠= 𝑚 𝑖)

Message
Chunks Secret Key
𝐻 𝐻
0b10 𝑠𝑘 0 𝑠𝑖𝑔 0 𝑠𝑖𝑔 0
𝐻
0b01 𝑠𝑘 1 𝑠𝑖𝑔 1 𝑠𝑖𝑔 1
𝐻 𝐻 𝐻
0b11 𝑠𝑘 2 𝑠𝑖𝑔 2 𝑠𝑖𝑔 2
0b00 𝑠𝑘 3 𝑠𝑖𝑔 3 𝑠𝑖𝑔 3

81 #BHUSA @BlackHatEvents

## Slide 82

#### **Signature Verification:**

• 𝑝𝑘 𝑖== ℎ𝑎𝑠ℎ_𝑐ℎ𝑎𝑖𝑛(𝑠𝑖𝑔 𝑖, 𝑠𝑡𝑒𝑝𝑠= 𝑤−1 −𝑚[𝑖])

Message
Chunks Public Key
𝐻
0b10 𝑠𝑖𝑔 0 𝑠𝑖𝑔 0
𝐻 𝐻
0b01 𝑠𝑖𝑔 1 𝑠𝑖𝑔 1
K 𝑝𝑘
0b11 𝑠𝑖𝑔 2 𝑠𝑖𝑔 2
𝐻 𝐻 𝐻
0b00
𝑠𝑖𝑔 3

82 #BHUSA @BlackHatEvents

## Slide 83

#### **Brute-Force Forgery on WOTS**

- If the attacker brute forces 𝑚<sup>′</sup> ≥𝑚 , **they can forge a valid signature** .

83 #BHUSA @BlackHatEvents

## Slide 84

#### **Brute-Force Forgery on WOTS**

• If the attacker brute forces 𝑚<sup>′</sup> ≥𝑚 , **they can forge a valid signature** .

Message
Chunks
0b10 𝑠𝑖𝑔 0 𝑠𝑖𝑔 0
𝐻
0b01 𝑠𝑖𝑔 1 𝒔𝒊𝒈 𝟏 ′ 𝒔𝒊𝒈 𝟏 ′ 0b10
0b11 𝑠𝑖𝑔 2 𝑠𝑖𝑔 2
0b00
𝑠𝑖𝑔 3 𝑠𝑖𝑔 3

84 #BHUSA @BlackHatEvents

## Slide 85

#### **Brute-Force Forgery on WOTS**

- If the attacker brute forces 𝑚<sup>′</sup> ≥𝑚 , **they can forge a valid signature** .

Message
Chunks Public Key
𝐻
0b10 𝑠𝑖𝑔 0 𝑠𝑖𝑔 0
𝐻
0b10 𝒔𝒊𝒈 𝟏 ′ 𝑠𝑖𝑔 1 𝒔𝒊𝒈 𝟏 ′
K 𝑝𝑘
0b11 𝑠𝑖𝑔 2 𝑠𝑖𝑔 2
𝐻 𝐻 𝐻
0b00
𝑠𝑖𝑔 3

85 #BHUSA @BlackHatEvents

## Slide 86

#### **How WOTS+ Adds a Checksum**

###### **Checksum:**

Secret Key Public Key
𝑙1 𝐻 𝐻 𝐻
0b10 𝑠𝑘 0 𝑠𝑖𝑔 0
𝑐= 𝐶 (𝑤−1 −𝑚𝑖)
𝑚= ෍
𝑖=0
𝐻 𝐻 𝐻
𝑐= 1 + 2 + 0 + 3 0b01 𝑠𝑘 1 𝑠𝑖𝑔 1
𝑐= 6 = 0𝑏0110 𝐻 𝐻 𝐻
0b11 𝑠𝑘 2 𝑠𝑖𝑔 2
K 𝑝𝑘
𝐻 𝐻 𝐻
0b00 𝑠𝑘 3 𝑠𝑖𝑔 3
𝐻 𝐻 𝐻
0b01 𝑠𝑘 4 𝑠𝑖𝑔 4
𝐻 𝐻 𝐻
0b10 𝑠𝑘 5 𝑠𝑖𝑔 5

86

#BHUSA @BlackHatEvents

## Slide 87

#### **How WOTS+ Adds a Checksum**

###### **Checksum:**

Secret Key Public Key
𝑙1 𝐻 𝐻 𝐻
0b10 𝑠𝑘 0 𝑠𝑖𝑔 0
𝑐= 𝐶 (𝑤−1 −𝑚𝑖)
𝑚= ෍
𝑖=0
𝐻 𝐻 𝐻
𝑐= 1 + 2 + 0 + 3 0b01 𝑠𝑘 1 𝑠𝑖𝑔 1
𝑐= 6 = 0𝑏0110 𝐻 𝐻 𝐻
0b11 𝑠𝑘 2 𝑠𝑖𝑔 2
K 𝑝𝑘
𝐻 𝐻 𝐻
0b00 𝑠𝑘 3 𝑠𝑖𝑔 3
𝐻 𝐻 𝐻
0b01 𝑠𝑘 4 𝑠𝑖𝑔 4
𝐻 𝐻 𝐻
0b10 𝑠𝑘 5 𝑠𝑖𝑔 5

87

#BHUSA @BlackHatEvents

## Slide 88

#### **How WOTS+ Adds a Checksum**

###### **Checksum:**

Secret Key Public Key
𝑙1 𝐻 𝐻 𝐻
0b10 𝑠𝑘 0 𝑠𝑖𝑔 0
𝑐= 𝐶 (𝑤−1 −𝑚𝑖)
𝑚= ෍
𝑖=0
𝐻 𝐻 𝐻
𝑐= 1 + 2 + 0 + 3 0b01 𝑠𝑘 1 𝑠𝑖𝑔 1
𝑐= 6 = 0𝑏0110 𝐻 𝐻 𝐻
0b11 𝑠𝑘 2 𝑠𝑖𝑔 2
K 𝑝𝑘
𝐻 𝐻 𝐻
0b00 𝑠𝑘 3 𝑠𝑖𝑔 3
𝐻 𝐻 𝐻
0b01 𝑠𝑘 4 𝑠𝑖𝑔 4
𝐻 𝐻 𝐻
0b10 𝑠𝑘 5 𝑠𝑖𝑔 5

88

#BHUSA @BlackHatEvents

## Slide 89

#### **How WOTS+ Protects Against Forgery**

• 𝑝𝑘 𝑖== ℎ𝑎𝑠ℎ_𝑐ℎ𝑎𝑖𝑛(𝑠𝑖𝑔 𝑖, 𝑠𝑡𝑒𝑝𝑠= 𝑤−1 −𝑚[𝑖])

Message
Chunks Public Key
𝐻
0b10 𝑠𝑖𝑔 0 𝑠𝑖𝑔 0
𝐻 𝐻
0b01 𝑠𝑖𝑔 1 𝑠𝑖𝑔 1
0b11 𝑠𝑖𝑔 2 𝑠𝑖𝑔 2
K 𝑝𝑘
𝐻 𝐻 𝐻
0b00 𝑠𝑖𝑔 3
𝐻 𝐻
0b01 𝑠𝑖𝑔 4 𝑠𝑖𝑔 4
𝐻
0b10
𝑠𝑖𝑔 5 𝑠𝑖𝑔 5

89 #BHUSA @BlackHatEvents

## Slide 90

#### **How WOTS+ Protects Against Forgery**

• 𝑐= 1 + 𝟏 + 0 + 3 = 𝟓

Message
Chunks Public Key
𝐻
0b10 𝑠𝑖𝑔 0 𝑠𝑖𝑔 0
𝐻
0b10 𝒔𝒊𝒈 𝟏 ′ 𝑠𝑖𝑔 1 𝒔𝒊𝒈 𝟏 ′
0b11 𝑠𝑖𝑔 2 𝑠𝑖𝑔 2
K 𝑝𝑘
𝐻 𝐻 𝐻
0b00 𝑠𝑖𝑔 3
𝐻 𝐻
0b01 𝑠𝑖𝑔 4 𝑠𝑖𝑔 4
𝐻
0b10
𝑠𝑖𝑔 5 𝑠𝑖𝑔 5

90 #BHUSA @BlackHatEvents

## Slide 91

#### **How WOTS+ Protects Against Forgery**

• 𝑐= 1 + 𝟏 + 0 + 3 = 𝟓

Message
Chunks Public Key
𝐻
0b10 𝑠𝑖𝑔 0 𝑠𝑖𝑔 0
𝐻
0b10 𝒔𝒊𝒈 𝟏 ′ 𝑠𝑖𝑔 1 𝒔𝒊𝒈 𝟏 ′
0b11 𝑠𝑖𝑔 2 𝑠𝑖𝑔 2
K 𝑝𝑘
𝐻 𝐻 𝐻
0b00 𝑠𝑖𝑔 3
𝐻 𝐻
0b01 𝑠𝑖𝑔 4 𝑠𝑖𝑔 4
𝐻
0b10
𝑠𝑖𝑔 5 𝑠𝑖𝑔 5

91 #BHUSA @BlackHatEvents

## Slide 92

- **Faulting WOTS+ to forge Hash Based Signature** • This research builds on Faulting Winternitz One-Time Signatures to forge LMS, XMSS, <u>or SPHINCS+ signatures</u> (PQCrypto 2023)

92 #BHUSA @BlackHatEvents

## Slide 93

#### **Faulting WOTS+ to forge Hash Based Signature**

- This research builds onor SPHINCS+ signatures <u>Faulting Winternitz One-Time Signatures to forge LMS, XMSS, or SPHINCS+ signatures</u> (PQCrypto 2023)

- The paper demonstrates an attack on the checksum calculation during signature verification using fault injection to alter normal behavior:

𝑠𝑖𝑔_𝑐ℎ𝑒𝑐𝑘𝑠𝑢𝑚 𝑗→ℎ𝑎𝑠ℎ_𝑐ℎ𝑎𝑖𝑛(𝑠𝑡𝑒𝑝𝑠= 𝑤−1 −𝑐<sup>′</sup> 𝑗)

93 #BHUSA @BlackHatEvents

## Slide 94

#### **Faulting WOTS+ to forge Hash Based Signature**

- This research builds onor SPHINCS+ signatures <u>Faulting Winternitz One-Time Signatures to forge LMS, XMSS, or SPHINCS+ signatures</u> (PQCrypto 2023)

- The paper demonstrates an attack on the checksum calculation during signature verification using fault injection to alter normal behavior:

𝑠𝑖𝑔_𝑐ℎ𝑒𝑐𝑘𝑠𝑢𝑚 𝑗→ℎ𝑎𝑠ℎ_𝑐ℎ𝑎𝑖𝑛(𝑠𝑡𝑒𝑝𝑠= 𝑤−1 −𝑐<sup>′</sup> 𝑗)

- **Partial hash chain skip**

- **Full hash chain skip**

94

#BHUSA @BlackHatEvents

## Slide 95

#### **Partial hash chain skip**

• 𝑠𝑖𝑔_𝑐ℎ𝑒𝑐𝑘𝑠𝑢𝑚 𝑗→ℎ𝑎𝑠ℎ_𝑐ℎ𝑎𝑖𝑛 𝑠𝑡𝑒𝑝𝑠= 𝑣<sup>′</sup> 𝑤ℎ𝑒𝑟𝑒𝑣<sup>′</sup> < (𝑤−1 −𝑐<sup>′</sup> 𝑗)

Public Key
𝐻
0b10 𝑠𝑖𝑔 0 𝑠𝑖𝑔 0
𝐻
0b10 𝒔𝒊𝒈 𝟏 ′ 𝑠𝑖𝑔 1 𝒔𝒊𝒈 𝟏 ′
0b11 𝑠𝑖𝑔 2 𝑠𝑖𝑔 2
K 𝑝𝑘
𝐻 𝐻 𝐻
0b00 𝑠𝑖𝑔 3
𝐻 𝐻
0b01 𝑠𝑖𝑔 4 𝑠𝑖𝑔 4 𝑠𝑖𝑔 4
𝐻
0b10
𝑠𝑖𝑔 5 𝑠𝑖𝑔 5

95 #BHUSA @BlackHatEvents

## Slide 96

#### **Full hash chain skip**

• 𝑠𝑖𝑔_𝑐ℎ𝑒𝑐𝑘𝑠𝑢𝑚 𝑗→ℎ𝑎𝑠ℎ_𝑐ℎ𝑎𝑖𝑛(𝑠𝑡𝑒𝑝𝑠= 0)

Public Key
𝐻
0b10 𝑠𝑖𝑔 0 𝑠𝑖𝑔 0
0b11 𝒔𝒊𝒈 𝟏 ′ 𝑠𝑖𝑔 1 𝒔𝒊𝒈 𝟏 ′ 𝒔𝒊𝒈 𝟏 ′
0b11 𝑠𝑖𝑔 2 𝑠𝑖𝑔 2
K 𝑝𝑘
𝐻 𝐻 𝐻
0b00 𝑠𝑖𝑔 3
𝐻 𝐻
0b01 𝑠𝑖𝑔 4 𝑠𝑖𝑔 4 𝑠𝑖𝑔 4 𝑠𝑖𝑔 4
𝐻
0b10
𝑠𝑖𝑔 5 𝑠𝑖𝑔 5

96 #BHUSA @BlackHatEvents

## Slide 97

#### **Full hash chain skip**

• 𝑠𝑖𝑔_𝑐ℎ𝑒𝑐𝑘𝑠𝑢𝑚 𝑗→ℎ𝑎𝑠ℎ_𝑐ℎ𝑎𝑖𝑛(𝑠𝑡𝑒𝑝𝑠= 0)

Public Key
𝐻
0b10 𝑠𝑖𝑔 0 𝑠𝑖𝑔 0
𝐻
0b10 𝒔𝒊𝒈 𝟏 ′ 𝑠𝑖𝑔 1 𝒔𝒊𝒈 𝟏 ′
0b11 𝑠𝑖𝑔 2 𝑠𝑖𝑔 2
K 𝑝𝑘
𝐻 𝐻 𝐻
0b00 𝑠𝑖𝑔 3
𝐻 𝐻
0b11 𝒔𝒊𝒈 𝟒 ′ 𝑠𝑖𝑔 4 𝑠𝑖𝑔 4 𝒔𝒊𝒈 𝟒 ′
𝐻
0b10
𝑠𝑖𝑔 5 𝑠𝑖𝑔 5

97 #BHUSA @BlackHatEvents

## Slide 98

#### **XMSS and SPHINCS+**

- **XMSS (eXtended Merkle Signature Scheme)** is a stateful hash-based signature scheme built on WOTS+ and a Merkle tree. Requires tracking a secret index to avoid key reuse.

98 #BHUSA @BlackHatEvents

## Slide 99

#### **XMSS and SPHINCS+**

- **XMSS (eXtended Merkle Signature Scheme)** is a stateful hash-based signature scheme built on WOTS+ and a Merkle tree. Requires tracking a secret index to avoid key reuse.

- **SPHINCS+** is a stateless hash-based scheme that combines **FORS** and a **hypertree of XMSS instances** .

Eliminates state management and supports flexible trade-offs in size and speed.

99 #BHUSA @BlackHatEvents

## Slide 100

###### **Code Review of the WOTS+ Component in the Reference XMSS Implementation**

```
voidwots_pk_from_sig(constxmss_params*params, unsigned char*pk,
constunsigned char *sig, constunsigned char *msg,
constunsigned char *pub_seed, uint32_taddr[8]) {
```

```
...
```

```
chain_lengths(params, lengths, msg);
```

```
for(i= 0; i< params->wots_len; i++) {
set_chain_addr(addr, i);
gen_chain(params, pk + i*params->n, sig + i*params->n,
lengths[i], params->wots_w-1 -lengths[i], pub_seed0, addr);
}
```

```
}
```

100 #BHUSA @BlackHatEvents

## Slide 101

###### **Code Review of the WOTS+ Component in the Reference XMSS Implementation**

```
voidwots_pk_from_sig(constxmss_params*params, unsigned char*pk,
constunsigned char *sig, constunsigned char *msg,
constunsigned char *pub_seed, uint32_taddr[8]) {
```

```
...
```

1 **`chain_lengths`** `(params, lengths, msg);` **`// [1]-> Attack to checksum calculation`**

```
for(i= 0; i< params->wots_len; i++) {
set_chain_addr(addr, i);
```

```
gen_chain(params, pk + i*params->n, sig + i*params->n,
lengths[i], params->wots_w-1 -lengths[i], pub_seed0, addr);
}
```

```
}
```

101 #BHUSA @BlackHatEvents

## Slide 102

###### **Code Review of the WOTS+ Component in the Reference XMSS Implementation**

```
voidwots_pk_from_sig(constxmss_params*params, unsigned char*pk,
constunsigned char *sig, constunsigned char *msg,
constunsigned char *pub_seed, uint32_taddr[8]) {
```

```
...
```

1 **`chain_lengths`** `(params, lengths, msg);` **`// [1]-> Attack to checksum calculation`**

```
for(i= 0; i< params->wots_len; i++) {
set_chain_addr(addr, i);
```

2 **`gen_chain`** `(params, pk + i*params->n, sig + i*params->n,` **`//[2]->Attack to checksum chunk`** `lengths[i], params->wots_w - 1 - lengths[i], pub_seed0, addr); }`

```
}
```

102

#BHUSA @BlackHatEvents

## Slide 103

**Code Review of the WOTS+ Component in the Reference XMSS Implementation** `static void` **`wots_checksum`** `(...) {`

```
...
/* Compute checksum. */
for (i= 0; i< params->wots_len1; i++) {
csum+= params->wots_w-1 -msg_base_w[i];
}
/* Convert checksum to base_w. */
```

```
csum= csum<< (8 -((params->wots_len2 * params->wots_log_w) % 8));
ull_to_bytes(csum_bytes, sizeof(csum_bytes), csum);
base_w(params, csum_base_w, params->wots_len2, csum_bytes);
}
```

```
static voidchain_lengths(...) {
base_w(params, lengths, params->wots_len1, msg);
wots_checksum(params, lengths + params->wots_len1, lengths);
}
```

103 #BHUSA @BlackHatEvents

## Slide 104

**Code Review of the WOTS+ Component in the Reference XMSS Implementation** `static void` **`wots_checksum`** `(...) {`

```
...
/* Compute checksum. */
for (i= 0; i< params->wots_len1; i++) {
csum+= params->wots_w-1 -msg_base_w[i];
}
/* Convert checksum to base_w. */
```

```
csum= csum<< (8 -((params->wots_len2 * params->wots_log_w) % 8));
ull_to_bytes(csum_bytes, sizeof(csum_bytes), csum);
base_w(params, csum_base_w, params->wots_len2, csum_bytes);
}
```

```
static voidchain_lengths(...) {
base_w(params, lengths, params->wots_len1, msg);
wots_checksum(params, lengths + params->wots_len1, lengths);
```

```
}
```

104 #BHUSA @BlackHatEvents

## Slide 105

###### **Code Review of the WOTS+ Component in the Reference XMSS Implementation** `static void` **`wots_checksum`** `(...) {`

```
...
/* Compute checksum. */
for (i= 0; i< params->wots_len1; i++) {
csum+= params->wots_w-1 -msg_base_w[i];
}
/* Convert checksum to base_w. */
```

```
csum= csum<< (8 -((params->wots_len2 * params->wots_log_w) % 8));
ull_to_bytes(csum_bytes, sizeof(csum_bytes), csum);
base_w(params, csum_base_w, params->wots_len2, csum_bytes);
}
```

```
static voidchain_lengths(...) {
base_w(params, lengths, params->wots_len1, msg);
wots_checksum(params, lengths + params->wots_len1, lengths);
}
```

105 #BHUSA @BlackHatEvents

## Slide 106

**Code Review of the WOTS+ Component in the Reference XMSS Implementation** `static void` **`wots_checksum`** `(...) {`

```
...
/* Compute checksum. */
for (i= 0; i< params->wots_len1; i++) {
csum+= params->wots_w-1 -msg_base_w[i];
}
```

```
/* Convert checksum to base_w. */
```

```
csum= csum<< (8 -((params->wots_len2 * params->wots_log_w) % 8));
ull_to_bytes(csum_bytes, sizeof(csum_bytes), csum);
base_w(params, csum_base_w, params->wots_len2, csum_bytes);
```

```
}
```

```
static voidchain_lengths(...) {
base_w(params, lengths, params->wots_len1, msg);
wots_checksum(params, lengths + params->wots_len1, lengths);
```

```
}
```

106 #BHUSA @BlackHatEvents

## Slide 107

###### **Code Review of the WOTS+ Component in the Reference XMSS Implementation**

`static void` **gen_chain** (...)

{

uint32_t i;

/* Initialize out with the value at position 'start'. */ memcpy(out, in, params->n);

/* Iterate 'steps' calls to the hash function. */ for (i = start; i < (start+steps) && i < params->wots_w; i++) { set_hash_addr(addr, i); thash_f(params, out, out, pub_seed, addr);

}

}

107 #BHUSA @BlackHatEvents

## Slide 108

###### **Code Review of the WOTS+ Component in the Reference XMSS Implementation**

`static void` **gen_chain** (...)

{

uint32_t i;

/* Initialize out with the value at position 'start'. */ memcpy(out, in, params->n);

/* Iterate 'steps' calls to the hash function. */ for (i = start; i < (start+steps) && i < params->wots_w; i++) { set_hash_addr(addr, i); thash_f(params, out, out, pub_seed, addr);

}

}

108 #BHUSA @BlackHatEvents

## Slide 109

###### **Code Review of the WOTS+ Component in the Reference XMSS Implementation**

`static void` **gen_chain** (...)

{

uint32_t i;

- /* Initialize out with the value at position 'start'. */ memcpy(out, in, params->n);

/* Iterate 'steps' calls to the hash function. */ for (i = start; i < (start+steps) && i < params->wots_w; i++) { set_hash_addr(addr, i); thash_f(params, out, out, pub_seed, addr);

}

}

109 #BHUSA @BlackHatEvents

## Slide 110

###### **Code Review of the WOTS+ Component in the Reference XMSS Implementation**

`static void` **gen_chain** (...)

{

uint32_t i;

/* Initialize out with the value at position 'start'. */ memcpy(out, in, params->n);

/* Iterate 'steps' calls to the hash function. */ for (i = start; i < (start+steps) && i < params->wots_w; i++) {

set_hash_addr(addr, i); thash_f(params, out, out, pub_seed, addr);

}

}

110 #BHUSA @BlackHatEvents

## Slide 111

#### **Code Review of the WOTS+ Component in the Reference SPHINCS+ Implementation**

- **SPHINCS+** reuses the same **WOTS+** code as **XMSS** for signature verification.

- As a result, all fault injection **attacks** demonstrated against XMSS also apply directly to SPHINCS+.

111 #BHUSA @BlackHatEvents

## Slide 112

#### **How to Target?**

###### Chose the fault injection point

112 #BHUSA @BlackHatEvents

## Slide 113

#### **How to Target?**

**Brute-force search** for a hash digest 𝒎<sup>′</sup>

Chose the fault injection point

113 #BHUSA @BlackHatEvents

## Slide 114

#### **How to Target?**

**Brute-force** Chose the fault **search** for a injection point hash digest 𝒎<sup>′</sup>

Forge a signature for 𝒎<sup>′</sup>

114 #BHUSA @BlackHatEvents

## Slide 115

#### **How to Target?**

**Brute-force** Chose the fault **search** for a injection point hash digest 𝒎<sup>′</sup>

Forge a
signature for
𝒎 ′

Inject the fault at the target **during verification**

115 #BHUSA @BlackHatEvents

## Slide 116

### **Fault Injection Results of XMSS**

116 #BHUSA @BlackHatEvents

## Slide 117

#### **Fault Injection Results – Skipping Hash Chains**

- Green: Normal Execution

- Yellow: Mute/Reset

- Red: Success

Fault Injection Plot of Sampling of C Scenario

117 #BHUSA @BlackHatEvents

## Slide 118

#### **Summary – XMSS & SPHINCS+**

- We identified multiple fault injection targets in **WOTS+** , which is used in both **XMSS** and **SPHINCS+** .

118 #BHUSA @BlackHatEvents

## Slide 119

#### **Summary – XMSS & SPHINCS+**

- We identified multiple fault injection targets in **WOTS+** , which is used in both **XMSS** and **SPHINCS+** .

- The **checksum calculation** is a broad and critical target. While skipping hash chains is easy, attacking the checksum calculation requires **precise local fault injection** (e.g., laser FI, EMFI).

119 #BHUSA @BlackHatEvents

## Slide 120

#### **Summary – XMSS & SPHINCS+**

- We identified multiple fault injection targets in **WOTS+** , which is used in both **XMSS** and **SPHINCS+** .

- The **checksum calculation** is a broad and critical target. While skipping hash chains is easy, attacking the checksum calculation requires **precise local fault injection** (e.g., laser FI, EMFI).

- Since **SPHINCS+ reuses the same WOTS+ code** , all attack techniques against XMSS verification **apply to SPHINCS+.**

120 #BHUSA @BlackHatEvents

## Slide 121

### **Bonus: Fault Injection on Fault Resistance XMSS Library**

121 #BHUSA @BlackHatEvents

## Slide 122

#### **Introduction**

- Fox Crypto released XMSS v1.0 **before** fault injection attacks on WOTS+ were published.

- The library includes **fault injection resistance** for **verification** , as stated in their documentation and presentations*.

- **Our goal:** Apply the attack on WOTS+

- We implemented Fox Crypto’s XMSS library on our STM32F4 target

- We used the same Voltage Fault Injection Setup from our earlier XMSS research.

Source: Production ready XMSS

122 #BHUSA @BlackHatEvents

## Slide 123

**Vulnerability We Found in Fox Crypto XMSS Implementation** `static void` **`chain`** `(...) {`

```
...
```

```
input_prf->M.ADRS.typed.OTS_Hash_Address.hash_address= start_index; // [1]
assert(start_index+ num_steps< W); // [2]
```

```
native_256_copy(output, input);
```

```
for(uint_fast8_t i= 0; i< num_steps; i++) { // [3]
```

- `...`

```
input_prf->M.ADRS.typed.OTS_Hash_Address.keyAndMask= 1;
xmss_PRF(HASH_ABSTRACTION(hashes) &input_f.M, input_prf);
for(uint_fast8_t j = 0; j < XMSS_VALUE_256_WORDS; j++) {
input_f.M.data[j] ^= output->data[j];
}
```

```
xmss_F(HASH_ABSTRACTION(hashes) output, &input_f);
input_prf->M.ADRS.typed.OTS_Hash_Address.hash_address+= 1; // [4]
```

```
}
```

123 #BHUSA @BlackHatEvents

```
}
```

## Slide 124

**Vulnerability We Found in Fox Crypto XMSS Implementation** `static void` **`chain`** `(...) {`

```
...
```

```
input_prf->M.ADRS.typed.OTS_Hash_Address.hash_address= start_index; // [1]
```

```
assert(start_index+ num_steps< W); // [2]
```

```
native_256_copy(output, input);
```

```
for(uint_fast8_t i= 0; i< num_steps; i++) { // [3]
```

```
...
```

```
input_prf->M.ADRS.typed.OTS_Hash_Address.keyAndMask= 1;
xmss_PRF(HASH_ABSTRACTION(hashes) &input_f.M, input_prf);
for(uint_fast8_t j = 0; j < XMSS_VALUE_256_WORDS; j++) {
input_f.M.data[j] ^= output->data[j];
}
```

```
xmss_F(HASH_ABSTRACTION(hashes) output, &input_f);
input_prf->M.ADRS.typed.OTS_Hash_Address.hash_address+= 1; // [4]
```

```
}
```

124 #BHUSA @BlackHatEvents

```
}
```

## Slide 125

**Vulnerability We Found in Fox Crypto XMSS Implementation** `static void` **`chain`** `(...) {`

```
...
```

```
input_prf->M.ADRS.typed.OTS_Hash_Address.hash_address= start_index; // [1]
assert(start_index+ num_steps< W); // [2]
```

```
native_256_copy(output, input);
```

```
for(uint_fast8_t i= 0; i< num_steps; i++) { // [3]
```

```
...
```

```
input_prf->M.ADRS.typed.OTS_Hash_Address.keyAndMask= 1;
xmss_PRF(HASH_ABSTRACTION(hashes) &input_f.M, input_prf);
for(uint_fast8_t j = 0; j < XMSS_VALUE_256_WORDS; j++) {
input_f.M.data[j] ^= output->data[j];
}
```

```
xmss_F(HASH_ABSTRACTION(hashes) output, &input_f);
input_prf->M.ADRS.typed.OTS_Hash_Address.hash_address+= 1; // [4]
```

```
}
```

125 #BHUSA @BlackHatEvents

```
}
```

## Slide 126

**Vulnerability We Found in Fox Crypto XMSS Implementation** `static void` **`chain`** `(...) {`

```
...
```

```
input_prf->M.ADRS.typed.OTS_Hash_Address.hash_address= start_index; // [1]
assert(start_index+ num_steps< W); // [2]
```

```
native_256_copy(output, input);
```

```
for(uint_fast8_t i= 0; i< num_steps; i++) { // [3]
```

```
...
```

```
input_prf->M.ADRS.typed.OTS_Hash_Address.keyAndMask= 1;
xmss_PRF(HASH_ABSTRACTION(hashes) &input_f.M, input_prf);
for(uint_fast8_t j = 0; j < XMSS_VALUE_256_WORDS; j++) {
input_f.M.data[j] ^= output->data[j];
}
```

```
xmss_F(HASH_ABSTRACTION(hashes) output, &input_f);
input_prf->M.ADRS.typed.OTS_Hash_Address.hash_address+= 1; // [4]
```

```
}
```

126 #BHUSA @BlackHatEvents

```
}
```

## Slide 127

###### **Fault Injection Results of Fox Crypto  XMSS Implementation**

- We used same Voltage Fault Injection Setup

- Green: Normal Behaviour

- Orange and Purple: Hash chain skip is performed, but the library **returns an error** due to the **countermeasure checks.**

- Yellow: Mute/Reset

- Red: Success

Fault Injection Plot of Full Hash Chain Skip

127 #BHUSA @BlackHatEvents

## Slide 128

#### **Vulnerability Disclosure Timeline**

- **Discovery & Validation:**

   - [26.04.2024] – Vulnerability identified and validated internally.

- **Initial Contact with Fox Crypto:**

   - [02.05.2024] – Notified Fox Crypto about the identified vulnerability.

   - [16.05.2024] – We presented the vulnerability and FI results to Fox Crypto.

- **Public Disclosure:**

   - [17.05.2024] – Fox Crypto created a public security issue on GitHub regarding the vulnerability.

- **Fox Crypto Fix Released:**

   - [08.10.2024] – Fox Crypto released version 2.0 of the XMSS library, confirming the fix for the vulnerability.

   - We appreciate Fox Crypto's timely response and transparency in addressing the issue.

128

#BHUSA @BlackHatEvents

## Slide 129

### Key Takeaways and Conclusions

129 #BHUSA @BlackHatEvents

## Slide 130

#### **Key Takeaways and Conclusions**

• Even “quantum-safe” code can be **glitched.** PQC is **not immune** to FI.

130 #BHUSA @BlackHatEvents

## Slide 131

#### **Key Takeaways and Conclusions**

- Even “quantum-safe” code can be **glitched.** PQC is **not immune** to FI.

- **Signature forgery** is possible **without breaking** crypto, just by skipping checks.

131 #BHUSA @BlackHatEvents

## Slide 132

#### **Key Takeaways and Conclusions**

- Even “quantum-safe” code can be **glitched.** PQC is **not immune** to FI.

- **Signature forgery** is possible **without breaking** crypto, just by skipping checks.

- New fault targets continue to emerge. Attackers adapt quickly, so defenses must evolve just as fast.

132 #BHUSA @BlackHatEvents

## Slide 133

#### **Key Takeaways and Conclusions**

- Even “quantum-safe” code can be **glitched.** PQC is **not immune** to FI.

- **Signature forgery** is possible **without breaking** crypto, just by skipping checks.

- New fault targets continue to emerge. Attackers adapt quickly, so defenses must evolve just as fast.

- Implementation security is the **next battleground** for post-quantum crypto.

133 #BHUSA @BlackHatEvents

## Slide 134

# Thank you

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pie hat
EFINGS
AUGUST be 2025
MANDALAY BAY / LAS VEGAS
```
