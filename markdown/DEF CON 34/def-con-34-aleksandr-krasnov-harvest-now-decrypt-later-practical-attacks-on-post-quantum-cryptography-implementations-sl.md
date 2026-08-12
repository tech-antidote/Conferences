---
title: "Harvest Now, Decrypt Later Practical Attacks on Post-Quantum Cryptography Implementations"
speakers: ["Aleksandr Krasnov"]
conference: "DEF CON"
conference_full: "DEF CON 34"
edition: "34"
year: null
source_pdf: "DEF CON 34/DEF CON 34 - Aleksandr Krasnov - Harvest Now, Decrypt Later Practical Attacks on Post-Quantum Cryptography Implementations - slides.pdf"
pages: 23
sha256: "c8eacfe97044b6eb7d66ad3b7e88b9106be67f0d921575ed10209716f73ba89c"
text_chars: 12138
ocr_pages: 0
has_ocr: false
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2"
converted_at: "2026-08-12T00:11:22Z"
---
# Harvest Now, Decrypt Later Practical Attacks on Post-Quantum Cryptography Implementations

**Speakers:** Aleksandr Krasnov  
**Conference:** DEF CON 34  
**Source:** `DEF CON 34/DEF CON 34 - Aleksandr Krasnov - Harvest Now, Decrypt Later Practical Attacks on Post-Quantum Cryptography Implementations - slides.pdf` (23 pages)


## Slide 1

## **Harvest Now, Decrypt Later** Practical Attacks on Post-Quantum Cryptography Implementations

Memory corruption, compiler-induced timing leaks, and fault injection in ML-KEM and ML-DSA

**Aleksandr Krasnov**

**DEF CON 34**

## Slide 2

**ROADMAP**

### **What We're Covering**

**I The PQC Panic & the Implementation Gap II The Landscape of PQC Implementations III Attack Vector 1 - Memory Corruption in the Lattice IV Attack Vector 2 - Compiler-Induced Side Channels V Attack Vector 3 - Fault Injection & State Manipulation**

**VI Securing the Migration & Conclusion**

2

## Slide 3

**I - THREAT & MANDATE**

##### **The Threat Model**

Retrospective risk: static data is already compromised Timeline pressure: driving aggressive migration dates Response: rapid PQC deployment without mature auditing

**HARVEST - NOW STORE DECRYPT - LATER** Adversaries intercept and store today's Ciphertext sits in cold storage, A cryptographically-relevant quantum encrypted traffic - TLS sessions, VPNs, undecryptable under classical computer arrives and retroactively archived records. computing for as long as it takes. breaks RSA/ECC-protected data.

3

## Slide 4

**I - THREAT & MANDATE**

##### **The Mandates: NIST Standards & CNSA 2.0**

**NIST Standardization**

**CNSA 2.0 Transition Timeline**

NSA mandate for National Security Systems

**FIPS 203 ML-KEM**

**2025** Software, browsers & firmware signing* - prefer PQC now **ML-KEM** Module-Lattice Key Encapsulation Mechanism - key establishment **2027** Procurement gate: new NSS acquisitions must be CNSA 2.0 compliant **FIPS 204 2030** Network equipment (VPNs, routers) - exclusive PQC use **ML-DSA** Operating systems & custom applications - exclusive use, classical **2033** retired Module-Lattice Digital Signature Algorithm - digital signatures _* signing → excl 2030, browsers/cloud → excl 2033_

4

## Slide 5

###### **I - THREAT & MANDATE**

**The math is sound. The code is not.**

Lattice math - rejection sampling, polynomial arithmetic, NTTs - is all well-proven. Translating it into secure, performant C, Rust, or assembly is incredibly error-prone.

**The rush to deploy PQC is creating a massive window of opportunity for purely classical exploitation - no quantum computer required.**

5

## Slide 6

**II - LANDSCAPE**

##### **The Ecosystem: Who's Shipping PQC Today**

A review of the current state of open-source and vendor PQC implementations.

**OPEN SOURCE**

**liboqs (Open Quantum Safe)**

The reference open-source library underpinning most PQC integrations - widely vendored, widely trusted, widely unaudited.

**HYPERSCALE**

**AWS / Cloudflare Hybrid TLS**

Production hybrid key-exchange (classical + PQC) already live in major cloud edge and CDN infrastructure.

**EMBEDDED**

**Embedded Vendor SDKs**

Chip-vendor PQC SDKs for constrained IoT/automotive targets - smallest install base, least scrutiny.

6

## Slide 7

**II - LANDSCAPE**

##### **The Complexity Problem**

Why lattice-based crypto is so much harder to implement securely than what it replaces.

###### **Complexity Drivers:**

- **NTT: Number Theoretic Transforms for polynomial multiplication**

- **Rejection Sampling: uniform sampling of A from a Keccak/SHAKE-128 stream - variable-iteration, but on public data so timing is not secret-dependent**

7

## Slide 8

**II - LANDSCAPE**

##### **The Underlying Math**

Breakdown

**POLYNOMIAL RING**

_Rq  =  Zq[X] / (X_<sup>_n_</sup> _+ 1)_

Coefficients live in this ring - n = 256, q = 3329 for ML-KEM.

**CENTERED BINOMIAL SAMPLING**

_ci  =  Σj=1η bj − Σj=1η b′j_

Draws secret / error coefficients from a discrete noise distribution.

**Math is invariant. Compilers and hardware are not.**

**NUMBER THEORETIC TRANSFORM (** **_GENERIC - illustrative_ )**

_âi  =  Σj=0n−1 aj ωij mod q_

Turns slow polynomial multiplication into fast base-case products.

**CENTERED REDUCTION**

_r ≡ a (mod q),   r_ ∈ _(−q/2, q/2]_

Maps reduced coefficients into a signed range for compact encoding.

8

## Slide 9

# **ATTACK VECTOR 1** **~~01~~ Memory Corruption in the Lattice**

The vulnerability class: unchecked length handling at the deserialization boundary

Case study: stack overflow in KEM public-key parsing

9

## Slide 10

**III - ATTACK VECTOR 1**

##### **The Vulnerability Class**

The bugs live at the serialization boundary - where attacker bytes become coefficients - not in the arithmetic kernels.

###### **Buffer Overflows**

###### **Out-of-Bounds Reads**

###### **Signed Integer Overflow**

Unchecked length fields in KEM key/ciphertext deserialization copy attacker bytes past a fixed-size buffer. The 1996-era stack smash - now guarding a post-quantum key.

An off-by-one in **rej_uniform** (uniform matrix sampling from the SHAKE-128 stream) over-reads the XOF buffer, folding adjacent memory into the public matrix Â.

Coefficients that skip range validation violate the invariant reduction routines assume (inputs < q). Downstream arithmetic exceeds the **int16_t** range - signed overflow, which is undefined behavior in C.

10

## Slide 11

**III - ATTACK VECTOR 1**

##### **Case Study: Reading the Vulnerable Code**

A representative stack overflow in KEM public-key deserialization

###### **Where it fails**

Code’s Intent → “Read a length-prefixed pub key and decode it into coefficients”

**#define KYBER_K             3                           // ML-KEM-768 #define KYBER_POLYBYTES     384 #define KYBER_POLYVECBYTES  (KYBER_K * KYBER_POLYBYTES) // 1152 - polyvec itself**

**int unpack_pk(polyvec *pk, const uint8_t *in, size_t in_len) { size_t declared = ((size_t)in[0] << 8) | in[1];   // attacker-controlled const uint8_t *body = in + 2; uint8_t buf[KYBER_POLYVECBYTES];                   // 1152 bytes memcpy(buf, body, declared);                       // <-- THE FLAW polyvec_frombytes(pk, buf); return 0; }**

The Trap → **declared** is attacker-controlled and is never compared to the 1152-byte buffer

Exploit Outcome → An oversized **memcpy** overruns the stack and overwrites the saved return address -RCE before a single coefficient is decoded

**// ML-KEM encodings are FIXED SIZE. // Never trust a wire length. if (in_len < 2 + KYBER_POLYVECBYTES) return -1; if (declared != KYBER_POLYVECBYTES) return -1; memcpy(buf, body, KYBER_POLYVECBYTES); polyvec_frombytes(pk, buf);**

11

## Slide 12

###### **III - ATTACK VECTOR 1**

#### **Remote Code Execution via Key Exchange**

A TLS 1.3 handshake using a vulnerable hybrid PQC key exchange, with a maliciously crafted KEM public-key encoding.

###### **1  CRAFT**

###### **2  SEND**

###### **3  OVERFLOW**

###### **4  EXECUTE**

Craft a key_share whose length prefix breaks the server’s deserialization bounds.

Initiate a TLS 1.3 handshake; deliver the payload as the client's KEM public key.

Server-side decode copies the oversized payload past a fixed buffer - a classic stack overflow.

Hijacked control flow pops a reverse shell - full RCE, crypto bypassed entirely.

12

## Slide 13

## Slide 14

# **ATTACK VECTOR 2** **~~02~~ Compiler-Induced Side Channels**

The constant-time myth: why “constant-time C” isn't constant-time binary

How LLVM/GCC optimize away timing protections in decapsulation

DEMO: remote timing attack for partial key recovery

13

## Slide 15

**IV - ATTACK VECTOR 2**

##### **The Constant-Time Myth**

Writing constant-time C does not guarantee constant-time execution.

**Source**

**Optimizer**

**Source Optimizer Binary** Developer writes source level Clang (v15-18, common **-O** flags) constant-time **poly_frommsg** - a recognizes the bit-test and emits a Decapsulation timing now depends on m` branchless bit-test mapping the secret secret-dependent branch. The source never bits → a plaintext-checking oracle. message m` to a polynomial. changed.

**Where it hits hardest:** ML-KEM decapsulation runs the Fujisaki-Okamoto transform →  decrypt m`, re-encrypt, compare c` vs c, select between the true shared secret and a PRF over rejection secret z. **poly_frommsg** encodes m` on the re-encrypt step, so a leaked branch there exposes m` → a plaintext-checking oracle → chosen-ciphertext key recovery.

Named instance: Clangover, CVE-2024-37880 (Purnal, 2024) - full ML-KEM-512 key in minutes. Distinct root cause from KyberSlash (secret-dependent division timing, CHES 2025)

14

## Slide 16

**IV - ATTACK VECTOR 2**

###### **Remote Timing Attack on ML-KEM Decapsulation**

Measuring microsecond response variations across thousands of crafted ciphertexts against a compiler-optimized target.

**Δ ~2.45 μs**

Mean timing delta between branches

**10,000+**

Crafted ciphertexts per recovery run

**Partial key**

Recovered over local network

15

## Slide 17

# **ATTACK VECTOR 3** **~~03~~ Fault Injection & State Manipulation**

How PQC algorithms react to power glitching and EM fault injection

Why ML-DSA signature state machines are fragile under physical attack

DEMO: key extraction from an embedded Cortex-M4 via glitching

16

## Slide 18

**V - ATTACK VECTOR 3**

##### **The Hardware Threat**

Shifting focus from software to physical attacks on PQC hardware implementations.

###### **Power Glitching**

A precisely timed voltage dip corrupts a single instruction fetch or execution mid-operation.

###### **State-Machine Fragility**

ML-DSA signing is a rejection loop:

sample mask y (ExpandMask) → w = A·y → commitment w₁ = HighBits(w) → challenge c → response z = y + c·s₁ → bound checks last → reject & retry.

###### **EM Fault Injection (EMFI)**

A localized electromagnetic pulse induces bit-flips in registers without physical contact.

**Abort the mask-sampling loop early → degenerate, low-entropy y:** Now z ≈ c·s₁ leaks s₁ directly - without any out-of-bound rejection ever firing.

[ _Loop-Abort Fault Family_ ]

**Fault locus: the mask-expansion loop in ExpandMask (coefficient sampling), so skipped coefficients remain zero. ExpandMask is dominated by the Keccak-f[1600] permutation - the same primitive behind ExpandA, SampleInBall and the commitment hash - but the leak comes from the truncated fill, not from corrupting Keccak's internals**

17

## Slide 19

**V - ATTACK VECTOR 3**

#### **Analyzing a single-trace voltage glitch on ARM Cortex-M4**

**TARGET**

**ARM Cortex-M4**

**TECHNIQUE**

**Voltage glitching**

**TOOLING**

**Low-cost ChipWhisperer**

**TIMING**

**Single-instruction precision**

**RESULT**

**Partial Recovery**

18

## Slide 20

## Slide 21

**VI - SECURING THE MIGRATION**

##### **The Hybrid Imperative**

Combining classical ECC/RSA with PQC is the prudent default for the transition decade.

**Classical (ECC/RSA)**

**Post-Quantum (ML-KEM)**

**Hybrid Channel** Secure unless both break

###### **Hybrid is insurance against cryptographic break of one algorithm - not against the implementation bugs in this talk. It also adds a second parser to attack**

###### **Memory-Corruption RCE**

_No, overflow fires when PQC is_ **Does Hybrid Help?** _half parsed_ **Actual Fix?** _Memory-safe language, input validation, fuzz the parser_

**Timing Key Recovery Does Hybrid Help?** _Yes, session key needs both secrets_ **Actual Fix?** _Constant-time decapsulation_

**Fault signing-key extraction** _No, signing is moving to pure_ **Does Hybrid Help?** _PQC (no classical fallback) Redundant compute,_ **Actual Fix?** _verify-before-release, glitch sensors_

19

## Slide 22

**VI - SECURING THE MIGRATION**

##### **Verification, Tooling & Tool Release**

**Verification & Dynamic Analysis**

Memory Safety: ASan/MSan + coverage-guided fuzzing of the parsers (libFuzzer, AFL++) - fuzz **unpack_pk** / **poly_frombytes** , not the math

Constant-time, measured: dudect, ctgrind (Valgrind + secret-tainting), TIMECOP

**TOOL RELEASE** LatticeScope

###### **Side-channel analysis scripts**

Automated timing-leak detection across compiled PQC binaries.

Constant-time, proven: ct-verif, Binsec/Rel

Verified implementations: Jasmin, Fiat-Crypto, HACL*/Vale - libjade ships formally verified, constant-time ML-KEM

###### **Lattice-targeted fuzzer**

Purpose-built fuzzer for auditing polynomial/NTT-heavy crypto code.

Differential testing: reference vs optimized build, identical inputs

20

## Slide 23

###### **FINAL THOUGHT**

**The rush to quantum safety has created a goldmine for classical exploitation.**

_We must secure the code before we worry about the quantum computer._

**Thank you!**

**DEF CON 34**

**Aleksandr Krasnov**
