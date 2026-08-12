---
title: "Witchcraft Solver Automated 0day Discovery in Stripped Binaries"
speakers: ["Jonathan Brossard"]
conference: "DEF CON"
conference_full: "DEF CON 34"
edition: "34"
year: null
source_pdf: "DEF CON 34/DEF CON 34 - Jonathan Brossard - Witchcraft Solver Automated 0day Discovery in Stripped Binaries - these.pdf"
pages: 55
sha256: "66d5fb424b36f199123231861b3ac0e496bfa656b4afdc20ba93cb2a6662bc6a"
text_chars: 243835
ocr_pages: 0
has_ocr: false
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2"
converted_at: "2026-08-12T00:23:31Z"
---
# Witchcraft Solver Automated 0day Discovery in Stripped Binaries

**Speakers:** Jonathan Brossard  
**Conference:** DEF CON 34  
**Source:** `DEF CON 34/DEF CON 34 - Jonathan Brossard - Witchcraft Solver Automated 0day Discovery in Stripped Binaries - these.pdf` (55 pages)


## Slide 1

EXECUTIVE MASTER IN CYBERSECURITY

**Binary Translation for Multi-Architecture Vulnerability Analysis:**

**Unlocking the x86-64 Security Toolchain for ARM, RISC-V, and**

Beyond

2026 Jonathan Brossard École Polytechnique — MOABI SOLUTIONS ORCID: 0009-0004-8031-1438

_Referent:_ Prof. Benjamin Smith — École Polytechnique _Mentor:_ Prof. Aurélien Francillon — EURECOM

## Slide 2

## **Executive Summary**

**Context and Problem.** A new generation of regulations is fundamentally expanding the scope of Product Security obligations across industries. The EU NIS2 Directive [1] and Cyber Resilience Act [2] impose security requirements on critical infrastructure and connected products; DORA [3] mandates ICT resilience for the financial sector; ISO/SAE 21434 [4] imposes cybersecurity engineering requirements across the automotive supply chain; and the FDA [5] requires cybersecurity evidence in medical device submissions. A common thread across all of these frameworks is accountability for the full software supply chain - companies are now legally responsible for vulnerabilities in software they integrate from third-party suppliers, even when those suppliers do not share source code.

This creates a pressing and largely unsolved operational problem. To demonstrate compliance, organisations must be able to audit binaries at scale across a wide range of processor architectures: IBM mainframes (s390x) running financial infrastructure under DORA [3], ARM and AArch64 devices dominating IoT and automotive systems under NIS2/CRA, RISC-V emerging in embedded and industrial contexts, and legacy architectures in medical and avionics equipment. Today, the capability to perform such audits at scale is extremely limited. Organisations rely on manual reverse engineering performed by highly skilled and scarce security researchers - a resource that cannot scale to the thousands of third-party binary components in a modern product’s supply chain.

**Approach.** This dissertation investigates _binary translation_ as the enabling technology for scalable, automated, cross-architecture binary taint analysis. Rather than rebuilding security tooling from scratch for each processor family, we translate foreignarchitecture binaries into the x86-64 format that MOABI’s mature taint analysis engine already understands, then apply that engine unmodified. We evaluated three modern translation tools - RetDec (Avast), Anvill (Trail of Bits), and rev.ng - against 39,364 real-world Linux binaries spanning five processor families, establishing for the first time a systematic, empirical picture of what is and is not currently translatable in production firmware. The full dataset is publicly available [6].

#### **Key Findings.**

- **Binary translation is operationally viable** for four of five evaluated architectures, with success rates between 55% and 94% depending on tool and architecture - sufficient for practical deployment in SSDLC pipelines.

- **No single tool is sufficient.** Tools specialise in complementary architectures: RetDec excels on ARM, Anvill on RISC-V and IBM mainframe (s390x), rev.ng fills the remaining ARM gaps. A two-tool portfolio (RetDec + Anvill) achieves 70.5% coverage; adding rev.ng raises this to 93%.

- **Translation speed enables automated pipelines.** At 5 seconds per binary, RetDec and Anvill can process a full firmware image within hours, making continuous integration into CI/CD DevSecOps workflows practical. rev.ng, at 180 seconds per binary, is better suited to targeted deep analysis of high-priority components.

- **PowerPC64 is a critical unresolved gap.** IBM POWER infrastructure - used in banking (DORA [3]), HPC, and government - is unsupported by all evaluated binary translators (0/8,134 binaries across all three tools).

**Recommendations.** The core finding of this thesis is architectural and general: binary translation enables _any_ x86-64 binary analysis platform to extend its reach to ARM, RISC-V, and IBM mainframe architectures without reimplementation. Organisations seeking to deploy this capability should build a two- or three-tool portfolio (RetDec + Anvill as a minimum viable baseline; adding rev.ng for higher ARMv7 coverage), integrate translation as a preprocessing step in CI/CD pipelines, and apply their existing x86-64 analysis infrastructure unmodified on the translated output. The open-source nature of all evaluated translators makes this approach accessible without commercial dependency. In all cases, binary taint analysis should be understood as a proactive, continuous capability for discovering unknown vulnerabilities in third-party binaries - complementary to, not a substitute for, reactive CVE triage via SBOM generation and version matching.

**Broader Impact.** MOABI’s binary taint analysis engine can now extend to ARM (including AArch64), RISC-V, and IBM mainframe architectures without reimplementation. This represents a qualitative shift: organisations subject to NIS2, CRA, DORA [3], ISO 21434, or FDA cybersecurity requirements can deploy automated binary taint analysis across the full architectural diversity of their supply chain, at a scale and cost that manual reverse engineering cannot match.

**Keywords:** binary translation, vulnerability analysis, taint analysis, multi-architecture security tooling, IR, supply chain security

i

## Slide 3

### **Contents**

|**1**
**Introdu**|**ction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .**
**1**|
|---|---|
|1.1
The|Architecture Scaling Problem in Security Tooling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1|
|
1.2
Pro|
blem Context: Analysis Without Source Code. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2|
|1.3
Two|Paths to Multi-Architecture Support . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2|
|1.3.1|Path 1: Intermediate Representation (IR) Generalization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2|
|1.3.2|Path 2: Binary Translation ("The Hack") . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3|
|1.4
Und|ecidability and Practical Compromise . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3|
|1.5
Res|earch Questions and Methodology . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3|
|1.6
Con|tributions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4|
|**2**
**Backgr**|**ound: Binary Vulnerability Analysis Methodology. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .**
**5**|
|2.1
Pha|se 1: File Format Parsing and Structural Analysis. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5|
|2.1.1
|ELF (Executable and Linkable Format) Structure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5
i
|
|2.1.2|Architecture Identification and Validation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5|
|2.2
Pha|se 2: Disassembly Algorithms and Challenges. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5|
|2.2.1|Undecidability of Disassembly: Formal Statement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5|
|2.2.2|Linear Sweep Disassembly . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5|
|2.2.3|Recursive Descent Disassembly . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6|
|2.2.4|Hybrid Disassembly (IDA Pro, Ghidra). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7|
|2.2.5|Disassembly Libraries . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7|
|2.3
Pha|se 3: Control Flow Graph Reconstruction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
8|
|2.3.1|Basic Blocks: Definition and Properties . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
8|
|2.3.2|Control Flow Graph: Definition and Construction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
8|
|2.3.3|Function Boundary Identification . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
8|
|2.4
Pha|se 4: Calling Convention Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
9|
|2.5
Pha|se 5: MOABI’s Vectorial Taint Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
9|
|2.5.1|Taint Semantics and Representation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
9|
|2.5.2|Taint Propagation Rules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
10|
|2.5.3|Two-Pass Interprocedural Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
10|
|2.5.4|Sink Functions and Vulnerability Detection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
11|
|2.6
Su|mmary: Why This Pipeline Matters for Translation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
11|
|**3**
**State o**|**f the Art. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12**|
|3.1
Und|ecidability Results and Theoretical Limits . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
12|
|3.1.1|Rice’s Theorem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
12|
|3.1.2|Disassembly Undecidability . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
12|
|3.2
Hist|orical Binary Translation Systems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
12|
|3.2.1|UQBT (1994–2002): Theoretical Foundations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
12|
|3.2.2|DEC FX!32 (1996–1999): Profile-Guided Translation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
14|
|3.2.3|QEMU (2005–present): Production-Scale Dynamic Translation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
14|
|3.3
Inte|rmediate Representations for Binary Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
15|
|3.3.1|Design Space and Trade-offs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
15|
|3.3.2|REIL: Reverse Engineering Intermediate Language. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
15|
|3.3.3|VEX: Valgrind’s IR . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
16|
|3.3.4|LLVM IR: The Modern Standard . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
16|
|3.4
Con|trol Flow Structuring and Decompilation Theory. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
16|
|
3.4.1|
Motivation: From Assembly to Algorithms. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
16|
|3.4.2|Control Flow Patterns and Their Translation Implications . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
16|
|3.5
Mo|dern Binary Analysis Ecosystem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
17|
|3.5.1|Fuzzing: The Dominant Vulnerability Discovery Method . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
17|
|3.5.2|
Static Analysis Tools . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
18|

ii

## Slide 4

|**4**
**Method**|**ology . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19**|
|---|---|
|4.1
Res|earch Questions (Restated) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
19|
|4.2
Too|l Selection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
19|
|4.2.1|RetDec (Avast) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
19|
|4.2.2|Anvill (Trail of Bits) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
19|
|4.2.3|rev.ng (rev.ng Srls) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
20|
|4.2.4|UQBT (University of Queensland, historical) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
20|
|4.3
Dat|aset Construction. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
20|
|4.3.1|Corpus: Linux Distribution Binaries viadebootstrap . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
20|
|4.4
Eva|luation Protocol . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
20|
|4.4.1|Success Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
20|
|4.4.2|Timeout and Resource Limits. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
21|
|4.4.3|Stratified Sampling for rev.ng . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
21|
|4.5
Exp|erimental Infrastructure. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
21|
|4.6
UQ|BT Resurrection Process . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
21|
|**5**
**Results**|**. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22**|
|5.1
Full|-Dataset Evaluation: RetDec and Anvill. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
22|
|5.1.1|Overall Success Rates. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
22|
|5.1.2|Architecture-Specific Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
22|
|5.2
Strai|tified Sample Evaluation: Three-Way Comparison . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
23|
|5.2.1|Sample Results. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
23|
|5.2.2|Sample vs. Full-Dataset Consistency . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
23|
|5.3
Tra|nslation Speed Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
24|
|5.3.1|Per-Binary Translation Time. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
24|
|5.3.2|Operational Implications. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
24|
|5.4
Co|mplementarity Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
24|
|5.4.1|Overlap Matrix (Stratified Sample) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
24|
|5.4.2|Per-Architecture Complementarity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
25|
|5.5
Fail|ure Mode Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
25|
|5.6
UQ|BT Comparison: Historical vs. Modern . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
25|
|5.7
Strai|tified Sampling Evaluation: rev.ng . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
25|
|5.7.1|Sample Composition. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
26|
|5.7.2|rev.ng Translation Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
26|
|5.7.3|
Extrapolation to Full Dataset . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
26|
|5.7.4|Three-Tool Portfolio Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
26|
|5.8
Su|mmary of Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
27|
|**6**
**Discus**|**sion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27**|
|6.1
Imp|lications for Security Architecture . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
27|
|
6.1.1|
Portfolio Deployment Strategy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
27|
|6.1.2|PowerPC64 Gap Mitigation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
28|
|6.2
Op|erational Viability Under Regulatory Constraints . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
28|
|6.2.1|NIS2 Directive Compliance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
28|
|6.2.2|
Cyber Resilience Act: SBOM Mandate . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
28|
|6.3
SS|DLC, DevSecOps, and the Shift-Left Imperative . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
29|
|6.4
Fail|ure Mode Mitigation Strategies . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
29|
|6.4.1|Indirect Control Flow Resolution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
29|
|6.4.2|Position-Independent Code (PIC) Handling. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
30|
|6.4.3|Large Binary Optimization. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
30|
|6.5
Ben|chmark Methodology Limitations. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
30|
|6.5.1|Success Criterion Validity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
30|
|652|Architecture Coverage Bias
30|
|..
6.5.3|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

Binary Characteristics Bias . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
30|

iii

## Slide 5

|6.6
Thr|eats to Validity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . .
30|
|---|---|---|
|6.6.1|Internal Validity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . .
30|
|6.6.2|External Validity. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . .
31|
|6.6.3|Construct Validity. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . .
31|
|6.6.4|Conclusion Validity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . .
31|
|6.6.5|Mitigation Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . .
31|
|6.7
Co|mparison with Alternative Approaches. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . .
32|
|6.7.1|Binary Translation vs. IR-Based Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . .
32|
|6.7.2|Binary Translation vs. Recompilation from Source. . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . .
32|
|6.8
Bin|ary Translation Enables Cross-Architecture Fuzzing. . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . .
32|
|6.8.1|The Fuzzing Instrumentation Challenge. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . .
32|
|6.8.2|Translation-Enabled Workflow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . .
32|
|6.8.3|Performance Comparison . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . .
32|
|6.8.4|Empirical Impact on Vulnerability Discovery . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . .
33|
|6.8.5|Limitations and Caveats . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . .
33|
|6.8.6|Deployment Recommendations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . .
33|
|6.9
Fut|ure Research Directions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . .
34|
|6.9.1|Short-Term (1–2 years) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . .
34|
|6.9.2|Medium-Term (2–5 years). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . .
34|
|6.9.3|Long-Term (5+ years) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . .
35|
|**7**
**Conclu**|**sion. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .**|**. . . . . . . . . . . . . . . 36**|
|7.1
Res|earch Questions Answered . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . .
36|
|7.2
Prin|cipal Findings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . .
36|
|7.3
Co|ntributions to Knowledge . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . .
37|
|7.4
Pra|ctical Recommendations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . .
37|
|7.5
Lim|itations and Future Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . .
37|
|7.6
Pos|itioning Against the State of the Art . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . .
37|
|**Glossary . .**|**. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .**|**. . . . . . . . . . . . . . . 39**|
|**A**
**Appen**|**dix: Control Flow Structuring - Detailed Reference . . . . . . . . . . . . . . .**|**. . . . . . . . . . . . . . . 45**|

iv

## Slide 6

### **List of Figures**

|1|Witchcraft Solver (wsolver) pipeline: three phases from stripped binary to concrete PoC.
. . . . . . .|. . . . .
35|
|---|---|---|
|2|CFG pattern for_if-then_structure. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . .
45|
|3|CFG pattern for_if-then-else_structure.
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . .
45|
|4|CFG pattern for_while_loop (pre-test).
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . .
45|
|5|CFG pattern for_repeat-until_loop (post-test). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . .
46|
|6|CFG pattern for endless loop with mid-bodybreak. . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . .
46|
|7|CFG pattern for_switch/case_structure (multi-way branch).
. . . . . . . . . . . . . . . . . . . . . . .|. . . . .
46|
|8|Irreducible CFG: loop body_{L_1_,L_2_}_has two entry points, requiringgotofor reconstruction. . . . . .|. . . . .
48|

### **List of Tables**

|1|Research questions and corresponding contributions.
. . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . .
4|
|---|---|---|
|2|Calling convention summary. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . .
9|
|3|Comparison of Intermediate Representations: REIL, VEX, and LLVM . . . . . . . . . . .|. . . . . . . . . . .
17|
|4|Full-Dataset Translation Success Rates (39,364 binaries) . . . . . . . . . . . . . . . . . .|. . . . . . . . . . .
23|
|5|Stratified Sample Translation Success (500 binaries) . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . .
23|
|6|Sample vs. Full-Dataset Consistency Check . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . .
23|
|7|Translation Speed (seconds per binary, median) . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . .
24|
|8|Binary-Level Overlap: How Many Binaries Succeed on Both Tools? . . . . . . . . . . . .|. . . . . . . . . . .
24|
|9|Best Tool Per Architecture (Stratified Sample) . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . .
25|
|10|UQBT vs. Modern Tools (GNU coreutils, sparc32_→_i386) . . . . . . . . . . . . . . . . .|. . . . . . . . . . .
25|
|11|rev.ng Stratified Sample Results (100 binaries per architecture) . . . . . . . . . . . . . . .|. . . . . . . . . . .
26|
|12|Extrapolated rev.ng Full-Dataset Performance . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . .
26|
|13|Three-Tool Coverage (Best per Architecture)
. . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . .
26|
|14|Fuzzing instrumentation approaches: qualitative comparison. . . . . . . . . . . . . . . . .|. . . . . . . . . . .
33|
|15|CVE-2023-2804: Fuzzing benchmark on libjpeg-turbo. . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . .
35|

v

## Slide 7

# **Binary Translation for Multi-Architecture Vulnerability Analysis: Unlocking the x86-64 Security Toolchain for ARM, RISC-V, and Beyond**

## Jonathan Brossard _École Polytechnique MOABI SOLUTIONS_

## **Abstract**

A new generation of regulations - the EU NIS2 Directive [1], Cyber Resilience Act [2], DORA [3] for financial services, ISO/SAE 21434 [4] for automotive, and FDA cybersecurity guidance [5] for medical devices - is fundamentally expanding the scope of Product Security obligations. A common thread is supply chain accountability: organisations are now legally responsible for vulnerabilities in third-party software they integrate, even when suppliers do not share source code. Demonstrating compliance requires auditing binaries at scale across heterogeneous processor architectures - IBM mainframes (s390x), ARM and AArch64, RISC-V, and beyond. Today this capability is severely limited, relying on manual reverse engineering by scarce expert practitioners that cannot scale to modern supply chains.

This dissertation addresses that gap through binary translation: rather than rebuilding security tooling per architecture, we translate foreign-architecture binaries into x86-64 and apply MOABI’s existing binary taint analysis engine - incorporating binary taint analysis, SBOM generation, vulnerability assessment, and CI/CD integration - unmodified. We present a systematic evaluation of three modern LLVM-based binary translators - RetDec, Anvill, and rev.ng - against 39,364 real-world Linux ELF binaries spanning five architectures (ARM64, ARMv7, PowerPC64 LE, RISC-V 64, IBM s390x) across ten distribution releases (Debian: stretch through forky; Ubuntu: xenial through noble).

Our findings reveal strong architectural complementarity: RetDec achieves 79.1% success on ARM64 (7,062/8,933 binaries), Anvill dominates RISC-V (94.1%) and s390x (68.1%), while all three tools fail completely on PowerPC64 (0/8,134). A two-tool portfolio (RetDec + Anvill) achieves 70.5% coverage excluding PowerPC64; adding rev.ng raises this to 93%. At 5 seconds per binary, RetDec and Anvill are compatible with automated CI/CD DevSecOps pipelines via MOABI’s REST API. The ASCiDy project [7] (EURECOM/MOABI, financed by a PTCC project of the Paris Campus Cyber, piloted by INRIA) extends this with binary-only fuzzing powered by concolic execution - a rare capability that

combines the coverage speed of greybox fuzzing with the constraint-solving power of symbolic execution, operating directly on stripped binaries without source code - completing a sovereign European SAST+DAST offering. We also resurrect UQBT for sparc32 _↔_ i386 and provide a four-tier fuzzing benchmark on CVE-2023-2804, empirically validating that binary translation preserves vulnerability characteristics across the full tool spectrum.

### **1 Introduction**

##### **1.1 The Architecture Scaling Problem in Security Tooling**

Modern vulnerability analysis platforms face an architectural diversity crisis. The MOABI binary analysis platform, which has performed dynamic taint analysis directly on x86 and x86-64 machine code for sixteen years of continuous active development, exemplifies this challenge - and this opportunity. MOABI operates on raw binaries without source code access, tracking data flow through complex calling conventions, analyzing stripped production firmware, and identifying vulnerabilities across multiple file formats (ELF, PE, COFF, U-boot). This capability represents significant engineering investment: handling Intel’s CISC architecture with over 2,000 instruction variants, modeling architecture-specific calling conventions, and implementing interprocedural dataflow analysis using 128-bit vectorial taint propagation in merely two passes.

However, this platform’s current x86-only scope creates a strategic constraint. As embedded systems, Internet of Things (IoT) devices, cloud computing infrastructure, and autonomous systems increasingly deploy on non-Intel architectures - ARM in mobile and automotive systems, RISC-V in embedded and IoT contexts, IBM s390x in mainframe and financial infrastructure, PowerPC in high-performance computing - MOABI’s x86-only constraint limits both use cases. For _reactive triage_ : when a CVE is published, PSIRTs need to identify affected firmware images rapidly; SBOM generation from translated binaries enables this. For _proactive discovery_ :

1

## Slide 8

continuous taint analysis and fuzzing on translated firmware images, integrated into CI/CD pipelines, finds unknown vulnerabilities before they become CVEs. A security platform that cannot analyse ARM firmware, RISC-V bootloaders, or s390x banking applications serves neither workflow.

##### **1.2 Problem Context: Analysis Without Source Code**

Product security teams routinely face firmware and binary analysis without source code access. This scenario arises across multiple contexts:

- **Legacy systems:** Medical devices, industrial control systems, avionics software where source code was lost, destroyed, or never properly archived. The FDA (2022) [5] requires medical device manufacturers to maintain Software Bills of Materials precisely because source code availability for legacy components cannot be assumed - a challenge well-documented in the SBOM literature [8].

- **Commercial off-the-shelf (COTS) components:** Vendors unwilling to disclose proprietary algorithms embedded in binary form (cryptographic libraries, codec implementations, protocol stacks). Automotive ECU firmware from tier-1 suppliers exemplifies this: OEMs receive binary images without corresponding source.

- **Supply chain security:** Binaries arrive from untrusted or partially-trusted sources requiring independent verification. Hardware manufacturers embedding third-party firmware (UEFI implementations, baseboard management controllers, network interface card firmware) must audit for backdoors and vulnerabilities without vendor cooperation.

- **Malware analysis:** By definition, malicious software arrives without source code. Reverse engineering malware binaries to understand capabilities, identify commandand-control protocols, and develop signatures requires binary analysis techniques.

Binary analysis addresses these scenarios directly: given only an executable file (ELF, PE, Mach-O), reconstruct sufficient semantic understanding to identify security weaknesses, behavioral characteristics, and exploit possibilities.

##### **1.3 Two Paths to Multi-Architecture Support**

Extending MOABI-or any architecture-specific analysis toolto additional processor families presents two fundamental engineering paths:

- 1.3.1 Path 1: Intermediate Representation (IR) Generalization

Lift binaries from arbitrary source architectures to an abstract intermediate representation (e.g., REIL [9], VEX [10], LLVM

IR [11]), then implement vulnerability analysis algorithms once on this unified representation. This approach promises architecture-agnostic analysis by abstracting machine-specific details behind a common semantic layer.

**Theoretical appeal:** Analysis code written against the IR automatically applies to all supported architectures. Adding a new architecture requires only implementing its frontend (native instructions _→_ IR) without modifying analysis logic. **Practical challenges:**

1. **Application Binary Interface (ABI) gaps:** Intermediate representations abstract instruction semantics (arithmetic, memory operations, control flow) but rarely model ABI conventions comprehensively. ARM’s AAPCS (ARM Architecture Procedure Call Standard), MIPS64’s o32/n32/n64 ABIs, RISC-V’s calling conventions, and x86-64’s System V AMD64 ABI differ fundamentally in:

   - Parameter passing mechanisms (registers vs. stack, which registers in which order)

   - Stack frame layout (frame pointer usage, red zones, alignment requirements)

   - Return value conventions (single register, register pairs, structure returns via hidden pointer)

   - Caller/callee register preservation responsibilities

   - Variadic argument handling (va_list structures)

Vulnerability analysis depends critically on tracking these conventions: if user-controlled input arrives as the third function argument, the analyzer must know whether that corresponds to ARM’s r2, x86-64’s rdx, or RISCV’s a2. Getting this wrong produces false negativesvulnerabilities remain undetected because taint doesn’t propagate through function boundaries correctly.

2. **Register space mapping complexity:** Different architectures provide vastly different register counts and organizational principles:

   - x86-64: 16 general-purpose registers (rax, rbx, rcx, rdx, rsi, rdi, rbp, rsp, r8–r15)

   - ARM64 (AArch64): 31 general-purpose registers (x0–x30) plus stack pointer

   - MIPS64: 32 general-purpose registers ($0–$31)

   - SPARC64: 32 integer registers with _register windows_ (sliding overlapping register sets for efficient function calls)

   - RISC-V: 32 integer registers (x0–x31, where x0 is hardwired zero)

MOABI’s taint analysis uses 128-bit vectors to track taint per register. Mapping a 32-register architecture’s

2

## Slide 9

state into x86-64’s 16-register space requires either lossy abstraction (multiple source registers collapse to single taint bit) or complete redesign of the taint propagation engine to handle variable-width register files. Neither option is architecturally neutral-both require architecture-aware modifications to supposedly architecture-independent analysis code.

3. **Permanent maintenance burden:** IR specifications evolve independently of analysis tool codebases. LLVM releases every 6 months, introducing new instructions, modifying semantics, deprecating operations. REIL transitioned to RREIL with breaking changes. Each IR evolution requires corresponding updates to analysis algorithms, creating permanent technical debt and version synchronization challenges.

##### 1.3.2 Path 2: Binary Translation ("The Hack")

**The Hack:** Translate foreign-architecture binaries to x86-64 LLVM IR and compile to x86-64 object code as a preprocessing step, then apply existing x86-64 analysis infrastructure unmodified. This approach treats translation as a black-box transformation: input is an ARM/RISC-V/s390x binary, output is an x86-64 artifact that preserves the data-flow and control-flow semantics relevant to taint analysis.

**Behavioural equivalence is explicitly not a goal.** Prior critiques of binary translation for security analysis have focused on whether translated binaries are _behaviourally equivalent_ to their source - i.e., produce identical outputs for identical inputs. We explicitly do not require this, and do not evaluate it. Taint analysis asks a different question: does user-controlled data flow from a source (e.g., a network input function) to a dangerous sink (e.g., memcpy, strcpy)? Answering this question requires only that _data-flow and control-flow structure_ be preserved across translation - not that the binary execute correctly end-to-end.

To avoid relinking and external symbol resolution problems, the translators evaluated here use _function stubs_ for external calls. The resulting x86-64 artifact is therefore _guaranteed not to run correctly_ as a standalone binary - external library calls resolve to stubs rather than real implementations. This is a deliberate and acceptable trade-off: we sacrifice runnability (which we do not need) to gain reliable, linktime-independent translation artifacts suitable for static taint analysis. The CVE-2023-2804 benchmark (Section 6.9.2) provides empirical validation that vulnerability-relevant dataflow properties are indeed preserved under this approach.

**Operational appeal:** If translation quality proves sufficient, MOABI’s existing codebase - accumulating expertise in bug detection, performance optimisation, calling convention handling, and vulnerability pattern databases - becomes immediately applicable to arbitrary architectures without modification.

**Critical questions:**

1. **Semantic preservation:** Do modern translators produce x86-64 binaries that faithfully preserve source architecture semantics, including edge cases relevant to security analysis (integer overflow, sign extension, endianness)?

2. **Vulnerability preservation:** Do vulnerabilities (buffer overflows, format string bugs, use-after-free, integer overflows) present in source binaries remain exploitable in translated binaries, or does translation inadvertently "fix" bugs through aggressive optimization?

3. **Success rate:** What fraction of real-world binaries translate successfully? Are failures random or systematically correlated with binary characteristics (size, complexity, dynamic features)?

4. **Operational viability:** Are translation speed and resource requirements compatible with PSIRT workflow constraints (24-hour CVE assessment deadlines, batch processing of firmware releases)?

This dissertation addresses these questions empirically through large-scale evaluation.

##### **1.4 Undecidability and Practical Compromise**

Before proceeding, we acknowledge fundamental theoretical limitations. Rice’s theorem (1953) [12] establishes that determining whether two programs exhibit equivalent behavior is undecidable in the general case. Binary translation cannot be proven correct for arbitrary programs-we accept this impossibility and pursue empirical validation instead.

However, history demonstrates that formally undecidable problems often yield to practical approximation. Miller et al.’s 1990 fuzzing study [13] - which discovered that 25–33% of Unix utilities crashed on random inputs - launched a 35year evolution of automated vulnerability discovery despite the theoretical impossibility of complete bug detection. AFL (American Fuzzy Lop) [14] has since discovered thousands of real vulnerabilities in production software. KLEE symbolic execution [15] achieves 90%+ code coverage on complex programs. Abstract interpretation [16] provides sound overapproximations for static analysis. The practical value of besteffort approaches, validated through empirical measurement, justifies continued research despite undecidability.

##### **1.5 Research Questions and Methodology**

This work addresses six research questions through systematic empirical evaluation:

1. **RQ1: Translation feasibility.** Do modern binary translators achieve sufficient success rates on real-world binaries to make the translation-based approach viable for security analysis?

3

## Slide 10

2. **RQ2: Architectural coverage.** Which processor architectures are well-supported by current translation tools, and where do critical gaps exist that prevent comprehensive multi-architecture analysis?

3. **RQ3: Tool complementarity.** Do multiple translation tools compete (providing redundant coverage of the same architectures) or complement (specializing in different architectural families)?

4. **RQ4: Operational viability.** Are translation speed, memory consumption, and resource requirements compatible with PSIRT workflow constraints (24-hour vulnerability assessment deadlines under NIS2/CRA)?

5. **RQ5: Scale effects.** How does translation success vary with binary characteristics (size, complexity, optimization level, static vs. dynamic linking)?

6. **RQ6: Historical comparison.** How do modern LLVMbased translators compare against classical approaches (UQBT) in terms of architecture coverage, success rate, and maintainability?

**Evaluation methodology:** We construct a test corpus of 39,364 production binaries via debootstrap across ten Linux distribution releases (Debian: stretch, buster, bullseye, bookworm, trixie, forky; Ubuntu: xenial, bionic, focal, jammy, noble) and five architectures (ARM64, ARMv7, PowerPC64 LE, RISC-V 64, IBM s390x). All three modern translators (RetDec, Anvill, rev.ng) undergo full-dataset evaluation where operationally feasible; rev.ng’s 180-second-per-binary overhead necessitates stratified sampling (100 binaries per architecture). We resurrect UQBT for sparc32 _↔_ i386 as historical baseline.

##### **1.6 Contributions**

This dissertation makes six contributions to the binary analysis and security research communities:

1. **Large-scale empirical benchmark:** First systematic evaluation of binary translator quality on 39K+ realworld binaries across five architectures, providing empirical foundation for tool selection decisions in security workflows. Prior work evaluated translators on synthetic benchmarks (SPEC CPU, CoreUtils) or small custom datasets; we measure production firmware, system utilities, and application libraries representing authentic PSIRT workloads.

2. **Architectural complementarity finding:** Demonstration that modern translators exhibit near-perfect nonoverlapping architectural specialization rather than redundant competition. RetDec dominates ARM (79.1% arm64, 48.8% armhf), Anvill dominates RISC-V (94.1%) and s390x (68.1%), rev.ng provides broadest coverage

including unique MIPS support. This finding contradicts naïve expectation of tool competition and instead reveals that comprehensive multi-architecture analysis requires portfolio deployment.

3. **PowerPC64 gap identification:** Discovery of complete PowerPC64 support absence across all evaluated tools (0/8,134 binaries, 0% success rate), affecting organizations operating IBM POWER9/POWER10 infrastructure in enterprise, high-performance computing, and financial sectors. This gap represents urgent development priority for security tool vendors.

4. **Operational constraint analysis:** Quantification of translation speed as critical workflow constraint. RetDec/Anvill’s 5-second translation time enables batch processing compatible with PSIRT 24-hour deadlines; rev.ng’s 180-second overhead (36 _×_ slower) limits applicability to selective deep analysis rather than routine scanning. This finding informs deployment architecture for multi-architecture security operations centers.

5. **UQBT resurrection and historical comparison:** Revival of classical UQBT translator (1990s) for sparc32 _↔_ i386, providing Docker deployment and modernized build infrastructure. Comparison with LLVM-based approaches (2020s) reveals trade-offs: UQBT’s explicit calling convention modeling provides semantic clarity but maintenance burden; modern LLVM-based tools leverage compiler infrastructure but inherit LLVM’s evolutionary churn.

6. **Decision framework for security architects:** Practical guidance for deploying multi-architecture vulnerability analysis under NIS2/CRA compliance, including tool selection criteria, portfolio composition strategies, and architectural gap mitigation approaches.

Table 1 summarises the correspondence between research questions and contributions.

Table 1: Research questions and corresponding contributions.

|**Research Question**|**Contribution**|
|---|---|
|RQ1: Translation feasibility|C1: Large-scale empirical benchmark|
|RQ2: Architectural coverage|C2: Complementarity finding; C3: PowerPC64 gap|
|RQ3: Tool complementarity|C2: Complementarity finding|
|RQ4: Operational viability|C4: Operational constraint analysis|
|RQ5: Scale effects|C1: Benchmark; C4: Operational analysis|
|RQ6: Historical comparison|C5: UQBT resurrection|
|All RQs|C6: Decision framework|

4

## Slide 11

### **2 Background: Binary Vulnerability Analysis Methodology**

To understand why binary translation enables architecture generalization, we first establish what a comprehensive binary vulnerability analysis platform must accomplish. This section describes the standard methodology implemented in systems like MOABI, providing technical foundation for evaluating whether translation preserves security-relevant semantics.

1 **2.1 Phase 1: File Format Parsing and Structural Analysis** 2

##### 2.1.1 ELF (Executable and Linkable Format) Structure

Linux and Unix systems use ELF [17], standardized by the Tool Interface Standard and extended by the System V ABI [18]. An ELF file comprises a header, program headers, section headers, and symbol tables. For binary analysis the critical fields are: e_machine (architecture identification - EM_X86_64, EM_AARCH64, EM_PPC64, EM_RISCV, EM_S390, etc.), e_entry (program entry point), and e_flags (architecture-specific ABI flags). PT_LOAD segments with the PF_X flag contain executable code; the key sections are .text (executable code), .rodata (constants), .data/.bss (globals), .symtab/.strtab (stripped in production binaries), and .dynsym/.dynstr (dynamic symbols, always present). Symbol table entries with type STT_FUNC provide ground-truth function boundaries via entry address and size - critical when CFG analysis fails on stripped binaries.

Beyond ELF, MOABI parses PE (Windows), COFF (embedded systems), and U-boot firmware containers (IoT devices), each requiring architecture-specific handling for imports, relocations, and load addresses.

##### 2.2.1 Undecidability of Disassembly: Formal Statement

**Proposition 1** (Code/Data Separation, after Rice [12]) **.** _The problem of determining whether a given byte in an executable’s .text section represents the start of an instruction or inline data is undecidable in general. Empirical evidence of this difficulty in practice is provided by Wartell et al. [19] and Pang et al. [20]._

_Proof sketch._ Consider a byte sequence in the .text section immediately following an unconditional jump:

jmp f(input) /* target address computed from user input */ .byte 0x41 /* is this code (INC ECX) or data (jump table entry)? */

Determining whether the byte 0x41 is the start of an instruction (reachable via some execution path) or inline data (never executed, e.g. a jump table) requires determining if _f_ () returns or is terminal. If _f_ is Turing-complete, this reduces to the halting problem.

#### Practical disassemblers use heuristics:

##### 2.2.2 Linear Sweep Disassembly

**Algorithm:** Start at .text section beginning, disassemble sequentially, treating every byte as instruction start.

**Algorithm 1 Linear Sweep Disassembly** _pc ←_ .text section start _end ←_ .text section end **while** _pc < end_ **do** _instr ←_ disassemble_at( _pc_ ) emit( _instr_ ) _pc ← pc_ + length( _instr_ ) **end while**

##### 2.1.2 Architecture Identification and Validation

#### **Advantages:**

Reliable architecture detection prevents catastrophic disassembly errors. Three validation layers are applied: (1) **magic numbers** - the ELF e_machine field or PE Machine field; (2) **instruction alignment** - ARM/ARM64 instructions are 4-byte aligned, RISC-V 2 or 4-byte, x86 unaligned; (3) **entry point sanity** - the first instructions at e_entry should form a recognizable ABI-mandated prologue. Absence of a valid prologue indicates a packed, encrypted, or mislabeled binary.

##### **2.2 Phase 2: Disassembly Algorithms and Challenges**

Disassembly converts byte sequences in .text sections to human-readable assembly instructions. This is formally undecidable [19] due to code/data ambiguity and indirect control flow.

- Simplicity: No control flow analysis required.

- Completeness: Every byte examined.

- Speed: Single pass, O(n) where n = .text size.

#### **Disadvantages:**

- **Embedded data:** Jump tables, string literals, padding bytes in .text are misinterpreted as instructions.

- **Alignment issues:** Variable-length instruction sets (x86) allow byte-aligned data to desynchronize disassembly.

- **Obfuscation vulnerability:** Malware deliberately embeds junk bytes after unconditional jumps to break linear sweep.

#### **Example failure (x86):**

5

## Slide 12

|1|address|bytes||disassembly|
|---|---|---|---|---|
|2|0x1000|e9 05|00 00|00
jmp 0x100a|
|3|0x1005|41 42|43 44|45
(embedded data: "ABCDE")|
|4|0x100a|c3||ret|

Linear sweep disassembles bytes at 0x1005 as instructions (inc ecx; inc edx; inc ebx; inc esp; inc ebp), producing garbage. Correct disassembly skips 0x1005–0x1009 (unreachable after unconditional jump).

**Overlapping instructions: polysemic byte sequences.** The linear sweep failure mode has a more dangerous variant: byte sequences that are not merely _garbage_ under linear sweep, but _meaningful but different_ instructions - a polysemic lattice with one semantics for the static analyser and another at runtime. This technique, documented extensively in offensive security research [21–23], is the basis of overlapping instruction obfuscation. A single ‘cover byte’ is placed after an unconditional jump; linear sweep consumes it as the start of an innocent instruction, absorbing the following bytes as its operand and hiding them from signature-based detection. Recursive descent - and the CPU - follow the jump, skipping the cover byte entirely, and decode the concealed instruction. **Concrete example: hiding a Linux syscall (x86, 32-bit)**

1 ; Byte layout: 2 ; addr bytes linear sweep recursive descent 3 ; 0x1000 EB 01 JMP 0x1003 JMP 0x1003 4 ; 0x1002 B8 [start of MOV eax...] (never reached) 5 ; 0x1003 CD 80 ...imm32 operand... INT 0x80 <- execve syscall! 6 ; 0x1005 ... (rest of MOV operand) (continues here)

Linear sweep decodes 0x1002: B8 CD 80 XX XX _→_ MOV eax, 0x????80CD - a harmless immediate load. The bytes CD 80 (INT 0x80, the Linux 32-bit syscall gate) are absorbed as an operand and never flagged. Recursive descent follows the JMP to 0x1003 and decodes CD 80 directly as INT 0x80. The CPU does likewise at runtime. A shellcode author can thus conceal an execve("/bin/sh") syscall from any static scanner relying on linear sweep, while the payload executes correctly at runtime [21].

**Implications for binary translation:** A translator relying on linear sweep as its disassembly primitive will produce an incorrect translation - the cover byte and its fabricated instruction appear in the output, while the hidden syscall does not. This is not merely an accuracy problem: a security tool analysing the translated binary would report a false-negative on the concealed code path. Translators must employ recursive descent or hybrid disassembly, and must handle the fundamental ambiguity that x86’s variable-length encoding makes unavoidable.

**Architectural root cause: a CISC property.** Polysemic instruction sequences are a direct consequence of _variablelength, unaligned_ instruction encodings. x86 is the extreme case: instructions range from 1 to 15 bytes, with no alignment

requirement - any byte address can be a valid instruction boundary [24]. The same byte sequence therefore has multiple syntactically valid decodings depending on the start address, enabling the obfuscation technique above.

Pure RISC architectures - MIPS, PowerPC, standard RISCV (without the C extension), IBM s390x - use fixed-width 4-byte instructions with mandatory 4-byte alignment. A jump into the middle of a 4-byte instruction lands on a misaligned address; the CPU raises an alignment exception. Polysemy is _architecturally impossible_ : there is only one valid decoding of any aligned 4-byte word. This is one reason binary translators targeting ARM64 or RISC-V as their lifting source have a fundamentally simpler disassembly problem than those targeting x86.

The interesting exception is **mixed-width ISAs** . ARM Thumb/Thumb-2 (AArch32) interleaves 2-byte and 4-byte instructions, with the CPU switching modes via the low bit of branch target addresses. A byte sequence can be valid ARM-mode code decoded one way and valid Thumb-mode code decoded another - a genuine, documented obfuscation vector in ARM malware [21]. Similarly, RISC-V with the C compressed extension (2-byte and 4-byte mixed) reintroduces limited ambiguity. The precise statement is therefore: _polysemic instruction sequences are a property of variable-length or multi-mode ISAs, not of CISC per se_ - but x86’s extreme encoding flexibility makes it by far the most susceptible architecture in practice.

##### 2.2.3 Recursive Descent Disassembly

**Algorithm:** Start at known entry points (program entry, exported functions, exception handlers), follow control flow recursively, disassemble only reachable code. **Advantages:**

- Accuracy: Only disassembles reachable code, avoiding embedded data.

- Robustness: Resistant to junk byte obfuscation.

#### **Disadvantages:**

- **Indirect control flow:** Cannot resolve call [eax], jmp [table + edx*4] without runtime analysis.

- **Computed jumps:** Interpreters, JIT compilers, obfuscated malware use register-indirect jumps (jmp rax) whose targets are data-dependent.

- **Function pointers:** Callbacks passed to qsort, pthread_create, signal handlers are indirect control flow that static analysis misses.

- **Incomplete coverage:** Code reachable only via function pointers remains undiscovered.

6

## Slide 13

|**Algorithm 2 Recursive Descent Disassembly**|
|---|
|_worklist ←{_entry_point_}_|
|_visited ←_/0|
|**while**_worklist̸_= /0**do**
_pc ←_worklist.pop()
**if** _pc ∈visited_ **then**
**continue**
**end if**
_visited ←visited ∪{pc}_
|
|_instr ←_disassemble_at(_pc_)
emit(_instr_)|
|**if**_instr_is unconditional jump**then**
_worklist ←worklist ∪{_target(_instr_)_}_
**else if**_instr_is conditional branch**then**
|
|_worklist_
_←_
_worklist_
_∪_
_{_target(_instr_)_, pc_
+|
|length(_instr_)_}_
**else if**_instr_is call**then**
|
|_worklist_
_←_
_worklist_
_∪_
_{_target(_instr_)_, pc_
+|
|length(_instr_)_}_
**else if**_instr_is return**then**
/* Do not add successor; function exits */
**else**|
|_worklist ←worklist ∪{pc_+length(_instr_)_}_
**end if**|
|**end while**|

**The fundamental limitation: indirect control flow is undecidable.** Instructions such as call rax or jmp rax transfer control to an address held in a register at runtime. Resolving the target statically requires knowing the value of rax at that program point - which in general requires full dataflow analysis of all possible execution paths leading to that instruction. This is undecidable in the general case (a consequence of Rice’s theorem): the value of rax may depend on user input, heap contents, or prior indirect calls, making static resolution equivalent to solving the halting problem. Recursive descent, like linear sweep, cannot overcome this barrier - it simply handles the cases it _can_ resolve (direct calls, conditional branches with static targets) and leaves indirect targets as gaps. This limitation propagates directly into binary translation: a translator that cannot determine all targets of jmp rax cannot generate a complete CFG, and therefore cannot correctly translate the function containing it. This is consistent with well-documented challenges in static binary translation [19, 25]: indirect control flow - virtual dispatch, callbacks, signal handlers, JIT dispatch tables - is widely reported as one of the dominant sources of translation failures in the literature.

##### 2.2.4 Hybrid Disassembly (IDA Pro, Ghidra)

Modern disassemblers combine approaches [20]:

1. Recursive descent from known entry points.

2. Heuristic analysis to identify missed functions:

   - Function prologue signatures: push rbp; mov

   - rbp, rsp on x86-64, stp x29, x30, [sp, #-16]! on ARM64.

   - Gaps in disassembly (unreached bytes between recursive descent regions).

   - Cross-references: pointers in .rodata/.data targeting .text indicate function pointers.

3. Linear sweep on remaining gaps (with lower confidence).

4. User-guided override: Analyst can force disassembly at specific addresses.

##### 2.2.5 Disassembly Libraries

**libxed (Intel X86 Encoder Decoder):** Official Intel disassembler supporting x86/x86-64 including AVX-512, AMX, APX extensions. Highly accurate but complex license (Intel Simplified Software License) restricts commercial redistribution. Used internally by Intel compilers, Pin dynamic instrumentation tool.

**Capstone:** Multi-architecture disassembler (ARM, ARM64, MIPS, x86, PowerPC, SPARC, SystemZ, XCore, M68K, TMS320C64x, M680X, Ethereum VM) supporting 60+ CPU variants. BSD-licensed, used by Ghidra, radare2, Binary Ninja. Accuracy varies by architecture: x86/ARM mature, exotic architectures (TMS320C64x) less tested. **libbfd (Binary File Descriptor library):** Part of GNU binutils, supports 30+ architectures and 80+ file formats. GPL-licensed, complicating integration into proprietary tools. Lower-level than Capstone (operates on ELF/PE structures, not just instructions).

**llvm-objdump:** LLVM’s disassembler, leveraging LLVM’s MC (Machine Code) layer. Supports all LLVM-backend architectures. Used by rev.ng and Anvill for initial lifting.

MOABI’s development reflects the complexity hidden in this phase: handling 2,000+ x86 instruction variants (including legacy modes, AVX masking, REX/VEX/EVEX prefixes), decoding variable-length encodings (1-byte nop to 15-byte AVX-512), managing instruction side effects (flag updates, segment register modifications), and validating decoding (illegal encodings produce UD2 faults). The depth of x86’s complexity is perhaps best illustrated by the fact that its MOV instruction alone - a single data-transfer opcode - has been formally proved Turing-complete [24]. This result was subsequently operationalised by Christopher Domas in the M/o/Vfuscator [26] (DEF CON 2015): a C compiler that emits programs composed exclusively of MOV instructions. M/o/Vfuscated binaries are semantically correct but defeat virtually all pattern-matching disassemblers and signature-based analysis tools, since no recognisable control flow, arithmetic opcodes, or syscall instructions appear in the output - only an

7

## Slide 14

undifferentiated sequence of data-transfer operations whose computational effect is entirely implicit in the memory access pattern.

##### **2.3 Phase 3: Control Flow Graph Reconstruction**

Once disassembly produces assembly instructions, the next phase identifies **basic blocks** and constructs the **control flow graph (CFG)** .

##### 2.3.1 Basic Blocks: Definition and Properties

**Definition 1** (Basic Block) **.** _A_ **_basic block_** _is a maximal sequence of instructions with the following properties:_

_1. Single entry point: Execution enters only at the first instruction._

_2. Single exit point: Control transfers out only at the last instruction._

_3. Straight-line execution: No internal branches._

A basic block ends at any of:

- Conditional branch (je, jne, ARM beq, bne)

- Unconditional jump (jmp, ARM b)

- Function call (call, ARM bl, RISC-V jal)

- Function return (ret, ARM bx lr, RISC-V ret)

|**Algorithm 3 Basic Block Identification**|
|---|
|**Input:**List of disassembled instructions_I_=_{i_1_,i_2_,...,in}_
**Output:**Set of basic blocks_B_|
|_leaders ←{i_1_}_/* First instruction is leader */
**for**each instruction_ik ∈I_ **do**
**if**_ik_ is branch target**then**
_leaders ←leaders∪{ik}_
**end if**|
|**if**_ik_ is branch/jump/call/ret**then**
_leaders ←leaders ∪{ik_+1_}_ /* Instruction after
branch */
**end if**|
|**end for**|
|_B ←_/0|
|**for**each leader_li ∈leaders_(in address order)**do**
|
|_bb ←{li,li_+1_,...,li_+1_−_1_}_ /* Instructions from _li_ to
next leader */
_B ←B∪{bb}_
**end for**
**return**_B_|

   - **Call edge:** ( _u, v_ ) where _u_ contains call target, _v_ is function entry. Call edges treated specially: return edges implicit.

   - **Return edge:** Function exit to call site’s next instruction. Usually not explicitly represented (unbounded number if function called from many sites).

- System call (syscall, int 0x80, ARM svc)

##### 2.3.3 Function Boundary Identification

- Exception-raising instruction (ud2, int3)

##### 2.3.2 Control Flow Graph: Definition and Construction

**Definition 2** (Control Flow Graph) **.** _A_ **_control flow graph_** _G_ = ( _V, E_ ) _is a directed graph where:_

- _V is the set of basic blocks._

- _E ⊆ V ×V is the set of control flow edges._ ( _u, v_ ) _∈ E if control may transfer from basic block u to basic block v during execution._

Edge types:

- **Fall-through edge:** ( _u, v_ ) where _u_ ends without branch and _v_ immediately follows in memory.

- **Jump edge:** ( _u, v_ ) where _u_ ends with jmp target and _v_ begins at target.

- **Conditional branch edges:** ( _u, v_ ) and ( _u, w_ ) where _u_ ends with conditional branch targeting _v_ (taken) and _w_ is fall-through (not taken).

Functions emerge as connected components in the CFG:

**Definition 3** (Function) **.** _A_ **_function_** _is a maximal set of basic blocks F ⊆ V such that:_

_1. There exists an entry block entry ∈ F reachable via call edges._

_2. All blocks in F are reachable from entry via edges in E._

_3. No block in F (except entry) is reachable via call edges._

_4. Paths from entry to return instructions remain within F._ Algorithmically:

1. Identify all call targets (function entries) from call instructions and symbol tables.

2. For each entry, perform depth-first search, stopping at returns or calls to other functions.

3. Mark visited blocks as belonging to current function. **Challenges:**

8

## Slide 15

**Algorithm 4 CFG Construction Input:** Set of basic blocks _B_ , disassembly information **Output:** CFG _G_ = ( _V, E_ ) _V ← B E ←_ /0 **for** each basic block _bb ∈ B_ **do** _last ←_ last instruction of _bb_ **if** _last_ is unconditional jump to _target_ **then** _E ← E ∪{_ ( _bb,_ block_containing( _target_ )) _}_ **else if** _last_ is conditional branch to _target_ **then** _E ← E ∪{_ ( _bb,_ block_containing( _target_ )) _}_ /* Taken */ _E ← E ∪{_ ( _bb,_ next_block( _bb_ )) _}_ /* Not taken */ **else if** _last_ is call to _target_ **then** _E ← E ∪{_ ( _bb,_ function_entry( _target_ )) _} E ← E ∪{_ ( _bb,_ next_block( _bb_ )) _}_ /* Return continuation */ **else if** _last_ is return **then** /* No outgoing edge; function exits */ **else** _E ← E ∪{_ ( _bb,_ next_block( _bb_ )) _}_ /* Fall-through */ **end if end for return** ( _V, E_ )

- **Tail calls:** Compiler optimization replacing call; ret with jmp, making function call indistinguishable from internal loop.

- **Shared epilogue:** Multiple functions jumping to common epilogue code (e.g., pop rbx; pop rbp; ret), causing apparent overlap.

- **Intraprocedural jumps:** C’s setjmp/longjmp, C++ exceptions throwing across function boundaries.

##### **2.4 Phase 4: Calling Convention Analysis**

Calling conventions specify how function calls transfer data and control - which arguments go in which registers, where return values land, and which registers each side must preserve. Correct modeling is _essential_ for vulnerability analysis: taint propagation across function boundaries depends on knowing where user-controlled input arrives. Table 2 summarises the six conventions relevant to our evaluation [18].

The critical implication for binary translation is that translating individual instructions is insufficient - ABI semantics must be preserved across call boundaries [18]. A naïve translation of ARM r0 as a memory location breaks x86-64 taint analysis, which expects the first argument in rdi. Translators must insert ABI adapters at every call site; failure to do so silently breaks interprocedural taint propagation, producing false negatives precisely where security analysis matters most.

|**ABI**|**Arg registers**|**Ret**|**Cleanup**|
|---|---|---|---|
|x86 cdecl|stack (R-to-L)|eax|caller|
|x86 stdcall|stack (R-to-L)|eax|callee|
|x86-64 SysV|rdi,rsi,rdx,rcx,r8,r9|rax|caller|
|ARM AAPCS<sup>1</sup>|r0–r3|r0|caller|
|AArch64|x0–x7|x0|caller|
|RISC-V|a0–a7|a0|caller|

Table 2: Calling convention summary. R-to-L: arguments pushed right-to-left, so the first argument sits at top of stack on entry.

##### **2.5 Phase 5: MOABI’s Vectorial Taint Analysis**

MOABI implements dynamic taint analysis directly on binaries. The description in this section documents the _existing_ MOABI platform - developed continuously over sixteen years prior to this thesis - to establish what must be preserved by binary translation for the analysis pipeline to remain valid. The author’s contributions lie in evaluating which translation tools achieve that preservation in practice (Section 5 onwards), not in the design of the taint engine itself. Unlike academic systems where taint is binary (tainted/untainted), MOABI uses **128-bit vectorial taint** , enabling simultaneous tracking of 128 independent data flows.

##### 2.5.1 Taint Semantics and Representation

**Definition 4** (Taint Vector) **.** _A_ **_taint vector_** _T ∈{_ 0 _,_ 1 _}_<sup>128</sup> _is a 128-bit bitvector where bit i indicates whether data is influenced by taint source i. Bit positions correspond to:_

- _Bits 0–31: Network inputs (sockets, different ports/protocols)_

- _Bits 32–63: File inputs (different files, stdin)_

- _Bits 64–95: User inputs (command line arguments, environment variables)_

- _Bits 96–127: Reserved for analysis-specific sources_

**Rationale:** 128-bit vectors enable tracking _provenance_ , not just presence, of taint. If a buffer overflow is reachable from network input (bit 3) but not file input (bit 35), security engineers prioritize differently than if both vectors are set.

**Implementation:** Each taint vector is represented as a __uint128_t value in C - a 128-bit integer type supported natively by GCC and Clang. Taint propagation operations (union, intersection, equality test) compile to standard 64bit bitwise instructions on pairs of general-purpose registers, without requiring model-specific registers such as x86 XMM. This keeps the implementation portable across architectures - including ARM64, RISC-V, and s390x - while retaining the full 128-bit semantic expressiveness.

**Symbolic taint register.** In addition to the 128-bit taint vector, each tracked value carries a supplementary

9

## Slide 16

_symbolic taint register_ (a u_64t field in the taint_t structure). This second word encodes qualitative semantic properties that go beyond provenance: signedness flags (TAINT_SIGNESS7/15/31/63, tracking sign-extension hazards at 8, 16, 32, and 64-bit truncation boundaries), heap allocation markers (TAINT_HEAP), unchecked-return flags (TAINT_UNCHECKED_RET), bounds-check bypass indicators (TAINT_CHECK: the size or bounds of this value have been verified by the program; TAINT_CHECK_BYPASS: a verification was present but is provably circumventable), and buffer identity (TAINT_BUFFER). The distinction is important: the 128-bit vector answers _“where does this data come from?”_ (provenance), while the symbolic register answers _“what do we know about this data’s type and safety properties?”_ (semantics). Together they enable MOABI to generate vulnerability reports that classify not just reachability but exploitability - a buffer overflow reachable from network input with TAINT_UNBOUNDED set is a higher-severity finding than one with TAINT_CHECK set.

##### 2.5.2 Taint Propagation Rules

Taint propagates through instructions according to dataflow semantics:

**Rule 1: Register assignment**

|1
mov dst, src|_→_
T[dst] := T[src]|
|---|---|

#### **Rule 2: Arithmetic operations**

1 add dst, src _→_ T[dst] := T[dst] _∨_ T[src] (bitwise OR) 2 sub dst, src _→_ T[dst] := T[dst] _∨_ T[src]

Rationale: Result depends on both operands, inherits taint from both.

#### **Rule 3: Bitwise operations**

|1|and|dst,|src
_→_
T[dst]|:= T[dst] _∨_T[src]|
|---|---|---|---|---|
|2|or|dst,|src
_→_
T[dst]|:= T[dst] _∨_T[src]|
|3|xor|dst,|src
_→_
T[dst]|:= T[dst] _∨_T[src]|

#### **Rule 4: Taint killing (clearing)**

1 xor eax, eax _→_ T[eax] := 0 (register zeroed, taint cleared) 2 mov eax, imm _→_ T[eax] := 0 (immediate constant has no taint)

tional blocks. This is conservative (overtaints) but sound (no false negatives).

##### 2.5.3 Two-Pass Interprocedural Analysis

MOABI achieves interprocedural analysis in exactly two passes-remarkable efficiency enabled by vectorial taint representation.

#### **Pass 1: Intraprocedural analysis (function-local)**

**Algorithm 5 Intraprocedural Taint Analysis Input:** Function _f_ with CFG _G f_ = ( _V, E_ ), initial taint state _T_ 0 **Output:** Taint state _Tout_ at function exit Initialize all registers/memory: _T_ [ _r_ ] _←_ 0 for all _r_ Apply initial taint sources: _T_ [rdi] _←_ 0 _x_ 01 (if first arg tainted) _worklist ←{entry_  block} visited ←_ /0 **while** _worklist̸_ = /0 **do** _bb ← worklist.pop_ () **if** _bb ∈ visited_ AND _Tbb_ unchanged **then continue** /* Fixed point reached */ **end if** _visited ← visited ∪{bb} T ← Tbb_  in_ /* Taint at block entry */ **for** each instruction _i_ in _bb_ **do** Apply taint propagation rule for _i_ to update _T_ **if** _i_ is sink (e.g., memcpy size parameter) **then if** _T_ [operand( _i_ )] _̸_ = 0 **then report vulnerability:** Tainted data reaches sink at _i_ **end if end if end for** _Tbb_  out ← T_ /* Taint at block exit */ **for** each successor block _succ_ of _bb_ **do**

_Tsucc_  in ← Tsucc_  in ∪ Tbb_  out_ /* Merge taint */ _worklist ← worklist ∪{succ}_

**end for**

**end while**

**return** _Texit_ /* Taint at function return */

#### **Rule 5: Memory operations**

1 mov [addr], src _→_ T[memory(addr)] := T[src] 2 mov dst, [addr] _→_ T[dst] := T[memory(addr)] 3 mov [addr1], [addr2] _→_ T[memory(addr1)] := T[memory(addr2 )]

#### **Rule 6: Control flow (implicit flows)**

1 cmp reg1, reg2 2 je target

If reg1 or reg2 is tainted, the branch decision depends on tainted data. MOABI optionally tracks **control-flow taint** : taint program counter, propagate to all assignments in condi-

#### **Pass 2: Interprocedural propagation**

After Pass 1, MOABI has computed taint summaries for each function:

- Input taint: Which parameters (rdi, rsi, rdx, ...) affect function behavior

- Output taint: Which return values/global variables become tainted

- Side effects: Which memory locations/global state modified

10

## Slide 17

Pass 2 propagates taint across call sites:

#### **Command injection sinks:**

|1|system(cmd)|/* If cmd tainted */|
|---|---|---|
|2|popen(cmd, mode)||
|3|execl(path, arg0, ...)|/* If path or args tainted */|
||**SQL injection sinks:**||
|1|mysql_query(conn, query)|/* If query tainted */|
|2|PQexec(conn, query)||
|3|sqlite3_exec(db, sql, ...)||

**Algorithm 6 Interprocedural Taint Propagation** 2 **Input:** Call graph _CG_ , taint summaries from Pass 1 3 **Output:** Global taint state including cross-function flows **for** each function _f_ in topological order of _CG_ **do** 1 **for** each call site _c_ in _f_ calling _g_ **do** 2 /* Marshal caller arguments to callee parameters */ 3 **if** _T_ [rdi] _̸_ = 0 at call site **then** _Tg_ [param0] _← T_ [rdi] **end if if** _T_ [rsi] _̸_ = 0 **then** _Tg_ [param1] _← T_ [rsi] **end if** /* ... repeat for rdx, rcx, r8, r9, stack args ... */ /* Apply callee taint summary */ _Tg ←_ analyze( _g, Tg_ ) /* Use Pass 1 results */ /* Unmarshal callee return to caller context */ _T_ [rax] _← Tg_ [return] Update global taint state with _Tg_ ’s side effects **end for end for**

**MOABI’s sink database:** Approximately 2,800 vulnerability prototype entries across libc, OpenSSL, Windows API, POSIX, and third-party libraries, defining dangerous sinks and their parameter semantics. This is backed by a broader function knowledge base of over 400,000 function prototypes used for calling convention analysis, parameter typing, and interprocedural dataflow. A third database of approximately 1,016 entries provides symbolic instruction semantics for every x86 instruction - specifying argument read/write permissions, RFLAGS modified, and a symbolic formula (e.g. %1$s = %1$s + %2$s for add) - enabling MOABI to model instruction-level dataflow with flag-accurate precision rather than relying on approximations. Each vulnerability entry specifies:

- Function signature (number/types of parameters)

**Why two passes suffice:** Vectorial taint captures all possible taint flows simultaneously. Each bit tracks one independent flow. Single Pass 1 traversal computes _all_ intraprocedural flows for all 128 sources. Pass 2 then links functions together. Contrast with scalar taint (boolean): each new taint source requires complete re-analysis (iterative fixed-point computation).

- Sink type (buffer overflow, format string, command injection, etc.)

- Dangerous parameters (indices of parameters that shouldn’t be tainted)

- Severity (critical, high, medium, low)

**Complexity:** Pass 1 is _O_ ( _|V | · |E|_ ) per function (CFG traversal). Pass 2 is _O_ ( _|CG|_ ) (one traversal of call graph). Total: _O_ (∑ _f |Vf |·|E f |_ + _|CG|_ ) where _|CG|_ is call graph size.

**False positive mitigation:** MOABI reduces false positives via:

1. **Sanitizer recognition:** If tainted data passes through strlen, strnlen, bounds checks before reaching sink, taint is cleared.

##### 2.5.4 Sink Functions and Vulnerability Detection

Taint analysis identifies where tainted data flows; vulnerability detection requires identifying **sinks** -operations where tainted data becomes dangerous.

2. **Constant bounds:** If memcpy(dst, src, 16) uses immediate constant, not flagged even if src tainted.

#### **Buffer overflow sinks:**

3. **Dominance analysis:** If bounds check dominates sink (all paths to sink pass through check), suppress warning.

|1|memcpy(dst, src, size)|/* If size is tainted */|
|---|---|---|
|2|strcpy(dst, src)|/* If src length unbounded */|
|3|sprintf(buf, fmt, ...)
*/|/* If format string unbounded|

##### **2.6 Summary: Why This Pipeline Matters for Translation**

**Detection rule:** If size/length parameter is tainted, flag potential buffer overflow.

The pipeline described - file format parsing, disassembly, CFG reconstruction, calling convention modelling, taint analysis - represents MOABI’s engineering investment in x86/x86-64 analysis. Extending this to ARM requires reimplementing:

**Format string sinks:**

- 1 printf(fmt, ...) /* If fmt is tainted */ 2 sprintf(buf, fmt, ...) 3 fprintf(stream, fmt, ...) 4 syslog(priority, fmt, ...)

- ARM/Thumb disassembly (mode switching, conditional execution, 32/16-bit instructions)

**Detection rule:** If format string argument tainted (allowing attacker-controlled %n, %s), flag format string vulnerability.

- ARM calling conventions (AAPCS register allocation, structure passing rules)

11

## Slide 18

- ARM-specific instruction semantics (predication, barrel shifter, LDM/STM multiple load/store)

- ARM memory model (alignment requirements, endianness handling)

Binary translation offers an alternative: if ARM _→_ x86-64 translation preserves semantics-including calling conventions, taint propagation characteristics, and vulnerability triggering conditions-then MOABI’s existing pipeline applies unmodified. The core question: do modern translators achieve this preservation in practice?

### **3 State of the Art**

This section provides comprehensive survey of binary translation systems, intermediate representations, control flow analysis theory, and the broader binary analysis ecosystem.

##### **3.1 Undecidability Results and Theoretical Limits**

##### 3.1.1 Rice’s Theorem

**Theorem 1** (Rice 1953 [12]) **.** _Let P be any non-trivial property of the language recognized by a Turing machine. Then the problem of determining whether the language recognized by an arbitrary Turing machine has property P is undecidable._

_Proof sketch._ Suppose decidable. Construct reduction from halting problem:

1. Given Turing machine _M_ and input _w_ , construct machine _M_<sup>_′_</sup> : "On input _x_ : simulate _M_ on _w_ ; if _M_ halts, accept _x_ ."

2. If _M_ halts on _w_ , _L_ ( _M_<sup>_′_</sup> ) = Σ<sup>_∗_</sup> (accepts everything).

3. If _M_ doesn’t halt on _w_ , _L_ ( _M_<sup>_′_</sup> ) = /0 (accepts nothing).

4. Testing whether _L_ ( _M_<sup>_′_</sup> ) has property _P_ solves halting problem. Contradiction.

**Corollary 1.** _Determining behavioral equivalence of two programs is undecidable._

**Implication for binary translation:** We cannot prove translated binary preserves source semantics in general case. Practical approach: empirical validation on test suites, formal verification for restricted subsets (finite-state machines, loop-free code).

##### 3.1.2 Disassembly Undecidability

**Theorem 2** (Wartell et al. 2011 [19]) **.** _The problem "Given byte b in executable .text section, is b part of an instruction or embedded data?" is undecidable._

_Proof sketch._ Reduce from halting problem. Consider program:

1 compute address a = f(input) /* f is Turing-complete */ 2 jmp [a] 3 .byte 0x90 /* NOP or data depending on whether f halts */

If _f_ halts and _a_ points to byte 0x90, it’s code. If _f_ doesn’t halt, byte unreachable (data). Determining code/data requires solving halting.

**Practical consequence:** All disassemblers use heuristics (linear sweep, recursive descent, hybrid). Errors inevitabletranslation tools must handle this gracefully.

##### **3.2 Historical Binary Translation Systems**

##### 3.2.1 UQBT (1994–2002): Theoretical Foundations

The University of Queensland Binary Translator [27–29], developed primarily by Cristina Cifuentes, Mike Van Emmerik, and colleagues, established semantic-preserving translation between SPARC, MIPS, Pentium, and PA-RISC.

**Design philosophy:** Correctness over performance. UQBT targets decompilation and cross-platform migration, not runtime emulation. Translation correctness essential for security analysis where behavioral equivalence matters more than execution speed.

#### **Architecture: Three-phase pipeline**

#### **Phase 1: Lifting to RTL (Register Transfer Lists)**

Source architecture instructions lift to RTL, a low-level IR

expressing operations as assignments:

1 /* SPARC: add %o0, %o1, %o2 */ 2 RTL: t1 := r[o0] 3 t2 := r[o1] 4 t3 := t1 + t2 5 r[o2] := t3 6 7 /* x86: add eax, [ebx] */ 8 RTL: t1 := r[eax] 9 t2 := m[r[ebx]] /* Memory read */ 10 t3 := t1 + t2 11 r[eax] := t3 12 CF := (t3 < t1) /* Carry flag */ 13 OF := overflow(t1, t2, t3) 14 ZF := (t3 == 0) 15 SF := (t3 < 0) 16 PF := parity(t3)

Note x86 translation explicitly models all flag updates that hardware performs implicitly. **RTL characteristics:**

- Infinite temporaries (t1, t2, ...) - backend performs register allocation

- Explicit memory model (m[addr])

- No implicit side effects (flags, condition codes explicit)

12

## Slide 19

- Architecture-neutral operations (+, -, *, /, bitwise, comparisons)

**Phase 2: Machine-independent optimization** Standard compiler optimizations on RTL:

- **Dead code elimination:** Remove assignments to unused temporaries

- **Constant propagation:** Replace t3 := 5 + 7 with t3 := 12

- **Common subexpression elimination:** Reuse computations

- **Copy propagation:** Replace t2 := t1; ... use t2 with use t1

These remove source architecture artifacts (redundant flag computations, register spills from limited register sets). **Phase 3: Code generation to target architecture** Lower RTL to target machine code:

/* RTL: t3 := r[eax] + r[ebx] */

1 /* RTL: t3 := r[eax] + r[ebx] */ 2 3 /* x86 target: */ 4 add eax, ebx 5 6 /* SPARC target: */ 7 add %o0, %o1, %o2 /* Assuming eax$\rightarrow$%o0, ebx$\ rightarrow$%o1 */ 8 9 /* MIPS target: */ 10 addu $t0, $t1, $t2

Backend performs:

- Register allocation (RTL temporaries _→_ physical registers)

- Instruction selection (RTL ops _→_ machine instructions)

1 /* SPARC: call foo; foo accesses %i0 (first param) */ 2 3 /* x86 translation: */ 4 push arg0 /* Marshal %o0 to stack */ 5 call foo 6 add esp, 4 /* Clean stack */ 7 8 /* foo’s x86 code: */ 9 mov eax, [esp+4] /* Access first param (was SPARC %i0) */

**2. MIPS o32 ABI:** First four arguments in $a0-$a3, rest on stack. Translation to x86 cdecl (all stack) requires marshaling:

1 /* MIPS: calling foo(a,b,c,d,e) */ 2 move $a0, ... 3 move $a1, ... 4 move $a2, ... 5 move $a3, ... 6 sw $t0, 16($sp) /* arg5 on stack */ 7 jal foo

8

9 /* x86 translation: */ push arg5 push arg4 /* Was $a3 */ push arg3 /* Was $a2 */ push arg2 /* Was $a1 */ push arg1 /* Was $a0 */ call foo add esp, 20

10

11

12

13

14

15

16

**3. x86 cdecl vs stdcall:** UQBT handles both, inserting appropriate cleanup code. **Limitations and lessons learned:**

   1. **Static linking only:** UQBT focused on staticallylinked binaries. Dynamically-linked libraries, positionindependent code (PIC), and runtime relocation unsupported.

   2. **Optimized code challenges:** Aggressive compiler optimizations (inlining, loop unrolling, tail call elimination) obscure structure. UQBT’s pattern matching for control flow structuring fails on heavily optimized code.

- Calling convention adaptation

**Calling convention handling:** UQBT explicitly models calling conventions across its supported architectures, including the following:

**1. SPARC Register Windows:** SPARC uses sliding register windows for fast calls:

- Registers %o0-%o7 (out): Current function’s outgoing arguments

- Registers %i0-%i7 (in): Current function’s parameters

- Registers %l0-%l7 (local): Local variables

- call shifts window: caller’s %o becomes callee’s %i

Translation to x86 (no register windows) requires explicit stack frame:

3. **Maintenance burden:** As architectures evolved (SPARC v8 _→_ v9, MIPS32 _→_ MIPS64, x86 _→_ x8664), UQBT’s frontend/backend matrix required updates: _n_ architectures need _n_ frontends and _m_ backends, total _n × m_ maintenance. This motivated shift to IR-based approaches (LLVM: _n_ frontends + _m_ backends, total _n_ + _m_ ).

4. **Floating point complexity:** IEEE 754 compliance across architectures (x86 uses 80-bit extended precision internally, SPARC/MIPS use 64-bit doubles) required explicit rounding mode handling in RTL.

**Historical significance:** UQBT demonstrated feasibility of semantic-preserving translation for real programs. Cifuentes’ thesis [27] established control flow structuring algorithms still used today. UQBT’s source release enabled academic research

13

## Slide 20

on binary analysis, though codebase became unmaintained as core developers moved to industry.

**Our resurrection (Section 4.6):** We revived UQBT for sparc32 _↔_ i386, modernized build system (Autoconf _→_ CMake, GCC 2.95 _→_ GCC 11), containerized in Docker, and provide side-by-side comparison with modern LLVM-based tools.

##### 3.2.2 DEC FX!32 (1996–1999): Profile-Guided Translation

Digital Equipment Corporation’s FX!32 [30, 31] enabled x86 Windows applications on Alpha AXP processors during Windows NT Alpha port. FX!32 addressed key challenge: aheadof-time translation produces slow code (conservative assumptions about register usage, aliasing), while pure interpretation too slow for interactive apps.

**Hybrid architecture:**

**Phase 1: Interpreted execution with profiling**

- Initially, interpret x86 code instruction-by-instruction

- Profile records:

   - Basic block execution counts

   - Register liveness (which registers live at block boundaries)

   - Branch directions (taken/not-taken frequencies)

   - Memory access patterns (stack, heap, globals)

- Overhead: 100x slowdown during profiling (acceptable for one-time cost)

#### **Phase 2: Hot path identification**

- Identify basic blocks executed _> N_ times (threshold _N ≈_ 1000)

- Construct **translation units** : maximal connected regions of hot blocks

- Typically 10% of code accounts for 90% of execution time (Pareto principle: a small fraction of causes produces the majority of effects - here, a small fraction of code produces the majority of runtime)

#### **Phase 3: Optimized translation to Alpha**

- Translate hot paths using profile data:

   - Observed register liveness _→_ accurate register allocation (eliminate unnecessary spills)

   - Branch probabilities _→_ code layout optimization (hot path straight-line)

   - Memory access patterns _→_ alias analysis (optimize load/store scheduling)

- Generate Alpha native code, cache persistently (.fx! files)

- Subsequent executions: interpreted cold code calls cached native hot code

**Results:**

- Microsoft Office on Alpha via FX!32: 60–70% of native x86 performance

- CPU-bound applications (compression, image processing): 50–60%

- I/O-bound applications (text editors, web browsers): 70– 80%

- Games (graphics-heavy): 30–40% (too slow for real use)

#### **Key insights:**

1. Profile-guided optimization matters: Ahead-of-time translation (no profile) achieved only 30–40% native performance; profiling doubled performance.

2. Hot path concentration: Small code regions dominate execution. Translator can afford aggressive optimization on 10% of code, fall back to interpretation for remaining 90%.

3. One-time profiling acceptable: Users tolerate slow first execution if subsequent runs fast.

#### **Limitations for security analysis:**

1. **Coverage bias:** Profiling optimizes frequently-executed paths. Security-critical code (error handlers, input validation, authentication checks) often executes rarely in normal profiles but is precisely what vulnerability analysis must cover.

2. **Non-determinism:** Different execution profiles yield different translations. Reproducing bugs requires exact same profile, complicating debugging.

3. **Cold code interpretation:** Unoptimized code paths may have different semantics than optimized (e.g., register aliasing, memory ordering). Vulnerabilities might manifest only in cold paths.

**Conclusion:** Profile-guided translation excellent for performance-driven migration (Alpha desktop, Rosetta 2), unsuitable for comprehensive security analysis requiring deterministic, complete coverage.

- 3.2.3 QEMU (2005–present): Production-Scale Dynamic Translation

QEMU [32], developed by Fabrice Bellard (École Polytechnique alumnus, class of 1996), represents the most successful binary translation system in deployment. QEMU provides

14

## Slide 21

full-system emulation (boots complete guest OS) and usermode translation (runs guest programs on host kernel), supporting 15+ guest architectures (x86, ARM, MIPS, PowerPC, SPARC, RISC-V, s390x) on 7+ host architectures. Its scale of deployment is remarkable: Android Emulator, QEMU-KVM (the Linux kernel virtualisation backend), Docker Desktop cross-platform containers, and countless embedded development and research workflows.

**Architecture: Tiny Code Generator (TCG).** TCG serves as both intermediate representation and JIT compiler. Unlike UQBT’s three-phase ahead-of-time design, QEMU minimises latency by translating basic blocks on-demand and caching aggressively. TCG has approximately 150 operations covering arithmetic, logical, shift, memory load/store, control flow, and type conversion - each in 32-bit and 64-bit variants. Guest CPU state (registers, flags) is held in a cpu_state structure; each guest instruction lifts to TCG operations that read and write this structure, which are then compiled to native host code.

**Limitations for security analysis.** QEMU’s design optimises for performance over correctness, which creates problems for taint analysis:

**Lazy flag evaluation.** x86 flags are not computed immediately after each instruction. Instead, QEMU saves the operation type and operands (cc_op, cc_src, cc_dst) and reconstructs flag values only when a subsequent instruction reads them. This works correctly in the common case, but breaks when cc_dst is overwritten before the flag is read:

1 add eax, ebx /* Sets CF, OF, ZF, SF -- saved lazily */ 2 mov ecx, eax /* Overwrites cc_dst */ 3 jo overflow /* Reads OF -- computed from stale cc_dst */

Compilers rarely generate such patterns, so QEMU accepts this inaccuracy for performance. For taint analysis, however, a vulnerability dependent on precise flag values (e.g., signed overflow detection via OF) produces wrong taint propagation.

**Conclusion:** QEMU demonstrates that production-scale dynamic translation is feasible. However, its performancefirst design makes it unsuitable as a foundation for security analysis where edge-case semantics matter. Modern AOT translators (RetDec, Anvill, rev.ng) accept higher per-binary overhead in exchange for correctness - the trade-off our benchmark evaluates.

##### **3.3 Intermediate Representations for Binary Analysis**

IR design involves fundamental trade-offs. We analyze four IRs systematically.

##### 3.3.1 Design Space and Trade-offs

#### **Expressiveness vs. Simplicity**

- **Complex IR (VEX, LLVM):** Many operations (100– 200), typed, models architecture details precisely. Anal-

ysis algorithms complex but accurate.

- **Simple IR (REIL):** Few operations (17), untyped or weakly typed. Analysis algorithms simple but may lose precision.

#### **Architecture Independence vs. Semantic Precision**

- **Architecture-neutral (REIL, LLVM):** Abstracts machine details. Portable analysis, but calling conventions/ABI require external knowledge.

- **Architecture-specific (TCG partially):** Models specifics (flags, addressing modes). Non-portable but precise.

#### **Analysis-Friendly vs. Execution-Efficient**

   - **SSA form (LLVM, VEX):** Each variable assigned once, φ-nodes at merges. A φ-node ( _phi-node_ ) is a special construct at control flow join points that selects between multiple incoming values depending on which execution path was taken - e.g. _x_ 3 = φ( _x_ 1 _, x_ 2) means “ _x_ 3 is _x_ 1 if we came from the left branch, _x_ 2 if from the right.” φ-nodes are a bookkeeping device, not a real machine instruction. Dataflow analysis is efficient in SSA form; code generation is harder.

   - **Non-SSA (REIL, TCG):** Variables reassigned. Code generation straightforward, dataflow analysis requires reaching definitions.

- 3.3.2 REIL: Reverse Engineering Intermediate Language

REIL (Reverse Engineering Intermediate Language) [9], designed by Thomas Dullien (Halvar Flake) at zynamics, minimizes instruction count to simplify analysis algorithm implementation. Its complete instruction set contains only 17 operations across five categories: arithmetic (ADD, SUB, MUL, DIV, MOD, BSH), logical (AND, OR, XOR), data movement (LDM, STM, STR), control flow (JCC), and special (UNDEF, UNKN, NOP, BISZ). Each x86 instruction expands to 10–30 REIL operations, but analysis algorithms need only handle these 17 types - far simpler than 2,000+ x86 variants. Operations are in three-address form with explicit operand sizes and no implicit side effects, making taint propagation and symbolic execution straightforward.

**REIL Limitations:** Calling conventions are not abstracted (registers are just named variables); single x86 instructions expand to _∼_ 30 REIL ops causing code bloat on large binaries; and the project is unmaintained. RREIL [33] extended REIL with formal operational semantics and a type system, but saw limited adoption.

15

## Slide 22

##### 3.3.3 VEX: Valgrind’s IR

VEX [10, 34] was designed for Valgrind’s instrumentation framework but is now widely used for static analysis (angr [35], Binary Ninja). Its key design principles are: SSA form with φ-nodes; strongly typed temporaries (I1, I8, I16, I32, I64, I128, F32, F64, V128, V256); separation of pure computation from state updates; and lazy x86 flag evaluation for performance. VEX has _∼_ 300 operations across integer arithmetic, comparisons, bitwise, shifts, and type conversion categories, plus statement types for register reads/writes, memory operations, atomics, and helper function calls.

**VEX Advantages:** Type safety prevents mixing operand widths; SSA enables standard compiler optimisations; angr provides cross-architecture symbolic execution over VEX for x86, ARM, MIPS, and PowerPC.

**VEX Limitations:** Calling conventions are not abstracted (registers are offsets into a guest_state array); 300+ operations make full implementation non-trivial; lazy flag evaluation complicates taint analysis (flag values are computed via helper calls, requiring interprocedural tracking even for a single instruction).

##### 3.3.4 LLVM IR: The Modern Standard

LLVM IR [11] has become the de facto standard target for modern binary translators (RetDec, Anvill, rev.ng) due to mature infrastructure and active development. Its design characteristics are: SSA form with φ-nodes; strong typing (integers i1–i128, floats, pointers, vectors, structs); three-address code; infinite virtual registers; and architecture neutrality. Instructions cover arithmetic, bitwise, memory (alloca, load, store, getelementptr), control flow (br, switch, call, ret), comparisons, and type conversions.

**Why LLVM for Binary Translation:** The llc backend generates high-quality x86-64 machine code from LLVM IR, making the full translation workflow ARM binary _→_ LLVM IR _→_ llc _→_ x86-64 binary straightforward. Over 200 optimisation passes (opt -O2) remove lifting artefacts. The tooling ecosystem - KLEE [15] for symbolic execution, AFL-LLVM for fuzzing, AddressSanitizer/UBSan for memory error detection - becomes directly applicable to translated binaries. LLVM’s active development ensures new architectures (ARM SVE2, RISC-V V extensions) are supported quickly.

**Challenges for Binary Translation:** Registers modelled as global variables prevent standard register allocation (mitigated by mem2reg); indirect jumps via indirectbr require listing all possible targets statically, which is undecidable in general; and ABI adapter functions must be inserted at every call site to bridge ARM/RISC-V register conventions to x86-64, adding overhead mitigated by inlining.

**Comparison: REIL vs. VEX vs. LLVM.** Table 3.3.4 summarises the key design properties of the three IRs discussed above.

**Conclusion:** Modern translators (RetDec, Anvill, rev.ng) choose LLVM for its backend quality and ecosystem, accepting challenges (register modeling, computed jumps) as necessary trade-offs. Our evaluation measures whether this choice succeeds for real binaries.

##### **3.4 Control Flow Structuring and Decompilation Theory**

Cristina Cifuentes’ PhD thesis [27] established theoretical framework for reconstructing high-level control structures from assembly’s goto-based control flow. Her subsequent work on decompilation [36] and graph structuring algorithms [37] remain the foundational references for this problem.

##### 3.4.1 Motivation: From Assembly to Algorithms

Assembly provides only primitive control transfer:

- Unconditional jump: jmp target

- Conditional branch: je target, bne target, etc.

- High-level languages provide structured constructs:

- If-then-else

- While loops

- For loops

- Switch statements

- Nested combinations thereof

**Decompilation challenge:** Given CFG (graph of basic blocks + edges), identify which subgraphs correspond to which high-level structures.

**Why this matters for translation:** If translator can recognize high-level structures, it can generate cleaner target code using structured constructs rather than flat goto soup. Cleaner code enables better optimization by target compiler.

- 3.4.2 Control Flow Patterns and Their Translation Implications

Cifuentes identified seven fundamental control flow patterns covering most compiler-generated code: if-then, if-then-else, while loop (pre-test), repeat-until (post-test), endless loop with break, switch/case via jump table, and sequential straight-line execution. Each corresponds to a recognisable subgraph in the CFG, recoverable via dominance analysis and back-edge detection. Two important equivalences reflect information lost during compilation: for and while loops produce identical CFG patterns, and switch/case is indistinguishable from a chain of if/else if at the binary level.

Some CFGs are _irreducible_ - they contain loops with multiple entry points that cannot be represented without goto.

16

## Slide 23

Table 3: Comparison of Intermediate Representations: REIL, VEX, and LLVM

|**Property**|**REIL**|**VEX**|**LLVM**|
|---|---|---|---|
|Operations|17|_∼_300|_∼_60 core|
|Type system|Weak|Strong|Strong|
|SSA form|No|Yes|Yes|
|Code expansion|High (30_×_)|Medium (10_×_)|Medium (5_×_)|
|Analysis complexity|Low|Medium|High|
|Optimization support|Limited|Medium|Extensive|
|Backend (codegen)|Manual|Manual|Mature (llc)|
|Calling convention|None|None|Partial|
|Ecosystem|Academic|Moderate|Production|
|Maintenance|Unmaintained|Active (small team)|Active (large)|

These arise in hand-written assembly, heavily optimized compiler output, and obfuscated malware. Modern translators (RetDec, Anvill, rev.ng) attempt structuring for optimization but fall back to flat LLVM indirectbr representation when necessary. The implication is direct: a translator assuming well-structured compiler output will fail on crypto libraries, OS kernel paths, JIT dispatch tables, and controlflow-flattened malware. The full pattern catalogue, structuring algorithm, and irreducibility analysis are detailed in Appendix A.

##### **3.5 Modern Binary Analysis Ecosystem**

We survey the broader vulnerability discovery and analysis ecosystem to contextualize binary translation’s value proposition: enabling these mature x86-64 tools to analyze arbitrary architectures.

3.5.1 Fuzzing: The Dominant Vulnerability Discovery Method

Fuzzing, or fuzz testing, constitutes the dominant methodology for automated vulnerability discovery in modern software security. A 2019 systematic study by Manès et al. [38] estimates that _over 50% of all discovered vulnerabilities_ are found through fuzzing-based approaches-a remarkable statistic demonstrating the technique’s practical effectiveness despite theoretical limitations.

**Fundamental Principle.** Fuzzing consists of iteratively generating semi-random inputs, submitting them to an application under test, and detecting abnormal behaviors (crashes, memory corruption, assertion failures) via monitoring mechanisms. Miller et al. [13] introduced the technique in 1990 with the seminal FUZZ tool, which sent random ASCII data to Unix utilities and discovered vulnerabilities in 25-33% of tested programs-a finding that shocked the research community and catalyzed decades of fuzzing research.

The introduction of _coverage measurement_ as a selection criterion for interesting inputs represents the decisive breakthrough transforming fuzzing from blind random testing into guided exploration. This innovation, formalized by Cadar et al. [15] with KLEE’s symbolic execution approach,

then industrialized by Zalewski [14] with AFL’s lightweight LLVM instrumentation, fundamentally changed vulnerability research workflows.

**Four Generations of Fuzzers.** Modern fuzzing tools can be classified into four generations, each representing architectural advances in exploration strategy:

**Generation 1: Blackbox Blind Fuzzing (1990-2010).** The original FUZZ tool [13] and its descendants (e.g., Radamsa, zzuf) generate purely random inputs without knowledge of expected format or program structure. Characteristics: (1) No instrumentation required-treat program as black box, (2) Input generation via bit flipping, byte insertion/deletion, random mutations, (3) Oracle: process crash detection (SIGSEGV, SIGABRT), (4) No coverage feedback loop.

Advantages: Trivial to deploy (no source code, no recompilation), effective on parsers with weak input validation (image decoders, font renderers, protocol implementations). Limitations: Exponential input space, cannot reach code protected by checksums or complex state machines, inefficient (most inputs rejected immediately by early validation).

**Generation 2: Coverage-Guided Greybox Fuzzing (2013-present).** AFL (American Fuzzy Lop) [14] and its successor AFL++ represent the state-of-practice. These tools instrument programs to measure code coverage, then use coverage as fitness function for evolutionary input selection.

Mechanism: (1) Instrumentation: Insert coverage tracking at every basic block transition via LLVM compiler pass or binary instrumentation (QEMU mode), (2) Corpus management: Maintain set of "interesting" inputs-those that triggered new coverage, (3) Mutation strategy: Mutate corpus inputs using bit flips, arithmetic operations, dictionary splicing, (4) Selection pressure: Keep mutated input if it discovers new basic block or edge in control flow graph.

AFL’s lightweight instrumentation (bitmap of 64K entries tracking edge coverage) achieves near-native execution speed while providing sufficient granularity to guide exploration. Integration with sanitizers (AddressSanitizer, UndefinedBehaviorSanitizer) detects memory errors that don’t crash immediately.

Impact: Thousands of vulnerabilities discovered (Google Chrome, Firefox, OpenSSL, Linux kernel). Became standard

17

## Slide 24

practice in security-critical projects (continuous fuzzing infrastructure: OSS-Fuzz, ClusterFuzz). Limitations: Cannot solve complex constraints (checksums, cryptographic hashes), struggles with "magic byte" comparisons (if (input == 0xdeadbeef)), path explosion in deeply nested conditions.

**Generation 3: Directed Greybox Fuzzing (2017present).** AFLGo [39] and similar tools (Hawkeye, BEACON) orient exploration toward _specific program locations_ rather than maximizing global coverage. Use cases: (1) Patch testing: Target recently-modified functions, (2) Vulnerability remediation: Focus on knowndangerous APIs (memcpy, strcpy), (3) Regression testing: Explore paths through bug-prone modules. Algorithm: (1) Compute static call graph and control flow graph, (2) Calculate distance from each basic block to target locations (graph shortest path), (3) During fuzzing, assign energy (execution budget) inversely proportional to distance: closer inputs fuzzed more intensely.

Advantages: Reaches deep targets 3-10 _×_ faster than undirected AFL. Particularly effective for recent patches where vulnerability likely localized. Limitations: Requires static analysis (may fail on stripped binaries, obfuscated code), distance metric imperfect (graph distance _̸_ = actual effort to reach target).

**Generation 4: Symbolic/Concolic Fuzzing (2020present).** SymCC [40], SymQEMU, and QSYM combine fuzzing with _symbolic execution_ -representing program inputs as symbolic variables, collecting path constraints, using SMT solvers (Z3, STP) to generate inputs satisfying specific branches.

Concolic execution executes program _concolically_ -both _concretely_ (real values) and _symbolically_ (symbolic expressions). When encountering branch if (x > 42), solver generates two inputs: one satisfying constraint ( _x >_ 42), one negating it ( _x ≤_ 42).

SymCC approach: Compile program with LLVM pass generating _two_ binaries: (1) Native binary (fast, runs normally), (2) Symbolically-instrumented binary (maintains symbolic expressions, generates constraints). For each AFL-discovered input, run symbolic binary on same input, collect path constraints, solve constraints to generate new test cases bypassing complex branches.

Performance: SymCC achieves 3-10 _×_ speedup vs. pure symbolic execution (KLEE) by leveraging concrete execution performance. Integration with AFL provides coverage guidance symbolic execution lacks.

Limitations: Symbolic execution has path explosion problem (exponential in branch count), expensive SMT solving (10<sup>2</sup> -10<sup>4</sup> _×_ slower than native execution), imperfect constraint modeling (floating-point, system calls).

**Complementarity of Approaches.** Modern fuzzing infrastructures (Google OSS-Fuzz, Microsoft OneFuzz) deploy _multi-strategy ensembles_ : AFL++ for broad coverage (80% of compute budget), AFLGo for recent patches (10% of bud-

get), SymCC for constraint-heavy targets (10% of budget, activated when AFL plateaus). Each strategy discovers vulnerability classes others miss. Empirical benchmarks such as UNIFUZZ [38] show that no single fuzzer dominates across all target programs, motivating portfolio deployment.

##### 3.5.2 Static Analysis Tools

Beyond fuzzing, the binary analysis ecosystem comprises disassemblers, decompilers, and analysis frameworks enabling manual and automated vulnerability research:

**IDA Pro** (Hex-Rays): Commercial industry standard. 60+ processor families, Hex-Rays decompiler (C pseudocode generation), extensive plugin ecosystem, $1,000–$5,000 licenses. Used by malware analysts, vulnerability researchers, reverse engineers globally. Function boundary detection accuracy on stripped binaries studied empirically by Andriesse et al. [25].

**Ghidra** (NSA): Open-source release 2019. P-Code intermediate representation enables cross-architecture analysis, 50+ architectures, Java-based (heavyweight but extensible), collaborative features (shared project databases). Government/academic adoption high.

**Binary Ninja** (Vector 35): Commercial alternative emphasizing modern UI/UX. BNIL (Binary Ninja Intermediate Language) has three abstraction levels (low/medium/high), Python API for automation, $149 (personal) to $399 (commercial). Popular with CTF community, boutique security firms.

**radare2** : Open-source, command-line focused. Extremely scriptable (pipes, JSON output), integrates with Unix toolchain philosophy, steep learning curve but powerful for automation. Popular in embedded/IoT security research.

**angr** (UC Santa Barbara): Python framework for symbolic execution and program analysis. Built on VEX IR (from Valgrind), supports 10+ architectures, strong academic pedigree, excellent documentation. Used for automated exploit generation research, binary analysis competitions (DARPA Cyber Grand Challenge).

**BAP** [41] (Carnegie Mellon University): Binary Analysis Platform providing a formal framework for binary program analysis. Supports multiple IRs, used extensively in academic research for program verification and vulnerability analysis.

**Relevance to Binary Translation.** If translation produces working x86-64 binaries from ARM/RISC-V/s390x sources, the _entire ecosystem above becomes applicable_ . Instead of requiring ARM-specific IDA licenses, ARM-specific Ghidra support, ARM-specific fuzzing infrastructure-translate once, use standard x86-64 tools everywhere. This multiplicative force motivates our research: unlocking 20+ years of x86-64 tool development for arbitrary architectures.

**angr:** Academic framework (UC Santa Barbara), VEXbased symbolic execution, Python API, multi-architecture (x86, ARM, MIPS, PowerPC). Enables automated exploit generation, automatic patching.

18

## Slide 25

These tools support cross-architecture analysis but don’t produce executable translations-orthogonal to our evaluation focus.

**Positioning this work against the state of the art.** The survey above reveals a persistent gap. The binary analysis ecosystem has invested heavily in two strategies for multi-architecture coverage: _semantic interpretation_ via IR (angr/VEX, Ghidra/P-Code, BAP), and _architecture-specific reimplementation_ . Neither satisfies an organisation with existing investment in a mature binary analysis engine: the former requires abandoning that investment, the latter multiplies it _n_ -fold per target architecture. Binary translation - treating the source-architecture binary as input to a preprocessing step that yields x86-64 - offers a third path. UQBT demonstrated its feasibility on controlled synthetic benchmarks in the 1990s [27, 29]; FX!32 validated it for performancedriven migration [30]; no subsequent work has asked whether _modern_ LLVM-based translators achieve this for production firmware at the scale and architectural diversity imposed by NIS2/CRA compliance workflows. This dissertation provides that empirical foundation.

### **4 Methodology**

This section describes our evaluation approach: tool selection rationale, dataset construction, evaluation protocols, and success criteria.

##### **4.1 Research Questions (Restated)**

Our empirical evaluation addresses six questions:

1. **RQ1: Feasibility.** Do modern binary translators achieve sufficient success rates ( _>_ 50%) on real-world binaries?

2. **RQ2: Architectural coverage.** Which architectures are well-supported, where are gaps?

3. **RQ3: Complementarity.** Do tools compete (redundant coverage) or complement (specialized)?

4. **RQ4: Operational viability.** Are translation speed/resources compatible with PSIRT 24-hour deadlines?

5. **RQ5: Scale effects.** How does success vary with binary size, complexity, optimization level?

6. **RQ6: Historical comparison.** How do modern LLVMbased tools compare against classical approaches (UQBT)?

##### **4.2 Tool Selection**

We evaluate three modern LLVM-based translators and one classical translator:

##### 4.2.1 RetDec (Avast)

**Developer:** Avast Software, Czech Republic [42]. Opensource (MIT license), active development.

**Architecture support:** x86, x86-64, ARM, ARM64 (primary), MIPS, PowerPC (experimental).

**Approach:** Lift binary _→_ LLVM IR, optimize aggressively (opt -O3), compile back to target architecture via llc.

RetDec integrates Hex-Rays decompiler patterns and performs type reconstruction by inferring struct layouts from memory access patterns, function signature recovery (parameter count and types), and string deobfuscation. It was selected on the basis of its maturity (in development since 2015), commercial deployment within Avast antivirus, and its documented specialization for ARM architectures.

##### 4.2.2 Anvill (Trail of Bits)

**Developer:** Trail of Bits, USA [43]. Open-source (Apache 2.0), active development.

**Architecture support:** x86, x86-64, ARM64, RISC-V 64, s390x (via Remill).

**Approach:** Uses Remill (also Trail of Bits) for lifting. Remill provides formal semantics for instructions (each instruction semantics implemented as C++ template), compiles semantics to LLVM IR bitcode. Anvill orchestrates: recover function boundaries, lift via Remill, optimize, compile.

Anvill’s design prioritises correctness over decompilation aesthetics. Formal instruction semantics (implemented as C++ templates in Remill) substantially reduce lifting bugs, and the specification-based architecture makes it possible to add new architectures via spec files rather than ad-hoc code.

In its standard configuration, Anvill requires IDA Pro or Ghidra as a front-end disassembler to supply function boundary information - the entry address and size of each function in the binary - before lifting can begin. This dependency on a commercial tool (IDA Pro licences range from $1,000 to $5,000) would have made large-scale automated evaluation impractical and the pipeline non-reproducible.

**Key methodological contribution: replacing IDA Pro with wunstrip.** We substituted IDA entirely by using **wunstrip** [44], our own open-source tool, as Anvill’s function boundary oracle. wunstrip recovers function boundaries by parsing two standard ELF sections - .eh_frame and .eh_frame_hdr - which encode Call Frame Information (CFI) records used by the C++ exception handling runtime and the __cxa_personality unwinding mechanism. These records contain the precise start address and size of every function that participates in stack unwinding, which in practice means virtually all functions compiled with standard toolchains. A systematic survey of 38,761 binaries from this corpus confirms 99.6% coverage [45]: .eh_frame data is present and well-formed in essentially the entire production Linux binary ecosystem.

19

## Slide 26

The consequence is significant. wunstrip supplies Anvill with the same function boundary information IDA Pro would provide - address and size per function, 100% precision and recall on the Ubuntu 24.04 LTS test set [44] - at zero licence cost, in a fully automated, reproducible pipeline. Every Anvill translation result reported in this work was produced using wunstrip as the front-end, with no commercial disassembler involved at any stage.

It was selected for its unique strong coverage of RISC-V and s390x, both absent from the other tools, and for the Trail of Bits team’s security auditing pedigree.

##### 4.2.3 rev.ng (rev.ng Srls)

**Developer:** rev.ng Srls, Italy [46]. Open-source (LGPL), commercial support available.

**Architecture support:** Broadest coverage-x86, x86-64, ARM, ARM64, MIPS, MIPS64, PowerPC, s390x, RISC-V, plus exotic (OpenRISC, Xtensa).

**Approach:** Lift via QEMU TCG (reuses QEMU’s battletested instruction decoders), translate TCG _→_ LLVM IR, optimize, compile.

By reusing QEMU’s TCG layer, rev.ng inherits battletested instruction decoders for a wide range of architectures, including self-modifying code detection (via QEMU’s existing SMC handling), position-independent code support, and function boundary detection via multiple heuristics. It was selected for its unique QEMU-based approach, its breadth of architectural coverage, and its European origin (relevant for EU sovereign security projects).

##### 4.2.4 UQBT (University of Queensland, historical)

**Developer:** Cristina Cifuentes, Mike Van Emmerik, 1990s. Open-source (BSD-style), unmaintained since 2002.

**Architecture support:** SPARC, MIPS, x86, PA-RISC.

**Approach:** Three-phase (lift _→_ optimize _→_ generate) as described in Section 3.2.1.

**Our contribution:** Resurrected UQBT for sparc32 _↔_ i386 translation. Modernized build system (Autoconf _→_ CMake), fixed GCC 11 compatibility, Docker container. Provides historical baseline for comparison with modern LLVM-based approaches.

**Rationale for inclusion:** Academic importance (Cifuentes’ thesis [27] foundational), demonstrates classical vs. modern trade-offs, sparc32 architecture rarely supported by modern tools (unique coverage).

##### **4.3 Dataset Construction**

4.3.1 Corpus: Linux Distribution Binaries via debootstrap

We construct test corpus from production Linux binaries using debootstrap, which creates minimal base system installations. The full dataset is publicly available [6].

**Distributions:** The corpus spans ten releases: Debian stretch (9), buster (10), bullseye (11), bookworm (12), trixie (13, testing), and forky (unstable); and Ubuntu xenial (16.04 LTS), bionic (18.04 LTS), focal (20.04 LTS), jammy (22.04 LTS), and noble (24.04 LTS).

**Architectures:** Five non-Intel architectures are evaluated. **ARM64 (aarch64)** is 64-bit ARM, now dominant in cloud servers (Ampere Altra, AWS Graviton), mobile SoCs (Apple A-series, Qualcomm Snapdragon), and automotive. **ARMv7 (armhf)** is 32-bit ARM with hard-float, still widespread in Raspberry Pi, embedded systems, and legacy Android devices. **PowerPC64 LE (ppc64el)** covers IBM POWER9/POWER10 CPUs found in mainframes, HPC clusters, and financial infrastructure (SWIFT, stock exchanges). **RISC-V 64 (riscv64)** is the open-source ISA gaining traction in embedded systems, IoT, and academic research platforms (BeagleV, SiFive). **IBM s390x** underpins mainframes (IBM z15, z16) used in banking, government, and high-reliability infrastructure.

These five were chosen to reflect complementary security imperatives: ARM64 for its explosive growth in cloud and server deployments; ARMv7 for its massive IoT installed base; PowerPC64 and s390x for the critical financial and governmental infrastructure they support; and RISC-V as the emerging open-source architecture most likely to require toolchain investment over the next decade.

**Dataset size:** The corpus totals 39,364 ELF binaries: 8,933 for ARM64, 7,930 for ARMv7, 8,134 for PowerPC64, 4,952 for RISC-V (fewer distributions support this architecture), and 9,415 for s390x.

**Characteristics:** The corpus is deliberately heterogeneous, spanning system utilities (bash, coreutils, grep, sed), core libraries (libc, libssl, libpthread, libz), network tools (ssh, curl, wget), compilers and interpreters (gcc, python3, perl), and package management tools (apt, dpkg). Binary sizes range from a few kilobytes (/bin/true) to over 50 MB for the Python interpreter with embedded standard library.

**Exclusions:** Kernel modules (.ko files) were excluded due to their distinct format. Non-ELF executables such as shell and Python scripts were filtered out. Statically-linked Go binaries were removed due to their size (often exceeding 20 MB), which caused systematic translation timeouts. Finally, encrypted or packed binaries were excluded as they require unpacking prior to any translation attempt.

A systematic survey of .eh_frame section presence across 38,761 binaries from this corpus confirms that 99.6% conform to standard toolchain conventions [45], validating corpus representativeness for production firmware analysis.

##### **4.4 Evaluation Protocol**

##### 4.4.1 Success Criteria

**Primary metric: Valid output ELF.** A translation is recorded as successful if the translator produces a valid x86-64 ELF file that parses correctly (readelf completes without error),

20

## Slide 27

contains a .text section with executable code, carries a valid ELF header (e_machine = EM_X86_64), and links without errors under ld.

Three secondary metrics were deliberately not evaluated. _Functional correctness_ - whether the translated binary produces identical output to the original - would require running both binaries across all possible inputs, comparing results through a source-architecture emulator and a native x86-64 execution environment; this is computationally infeasible at 39K-binary scale. _Performance_ - whether the translated binary executes as fast as its source - is a secondary concern for security analysis: even a 10 _×_ slowdown is acceptable provided vulnerabilities are preserved. _Vulnerability preservation_ - whether buffer overflows, format string bugs, and use-after-free conditions in the original remain exploitable after translation - requires manual exploit development per binary and is deferred to future work (Section 7).

**Rationale for primary metric:** A valid ELF output is the minimum requirement for applying downstream analysis tools (taint analysis, fuzzing, symbolic execution). If the translator produces a valid x86-64 binary, MOABI can analyse it; if it fails or produces malformed output, the pipeline is broken regardless of any deeper quality considerations.

**Reproducibility note:** All Anvill translations were performed using wunstrip [44] as the function boundary oracle, replacing Anvill’s standard IDA Pro or Ghidra dependency. No commercial disassembler was used at any stage of the evaluation. The full pipeline - wunstrip function boundary recovery, Anvill lifting, LLVM optimisation, and code generation - is therefore entirely open-source and reproducible from the published dataset [6].

##### 4.4.2 Timeout and Resource Limits

**Per-binary timeout:** 300 seconds (5 minutes). This is sized around PSIRT workflow constraints: a 24-hour CVE assessment deadline over a firmware image containing 100–1000 binaries allows roughly 300 binaries per day on a single workstation - adequate for typical PSIRT scale.

**Memory limit:** 16 GB per process. Translators occasionally consume unbounded memory on pathological inputs (giant functions, computed jumps spanning the entire address space); the 16 GB ceiling prevents system lockup on the development workstation. In production, PSIRT engineers may increase the timeout for critical binaries, attempt function-level analysis of oversized inputs, or fall back to a complementary tool where coverage allows.

##### 4.4.3 Stratified Sampling for rev.ng

Full-dataset evaluation of all 39,364 binaries is feasible for RetDec and Anvill at roughly 5 seconds per binary (approximately 54 hours each). rev.ng’s median translation time of

180 seconds per binary would require over 1,900 hours - 82 days - making full evaluation impractical.

**Stratified sampling:** 100 binaries per architecture, randomly sampled from full distribution:

**Algorithm 7 Stratified Random Sampling**

**Input:** Full dataset _D_ , architectures _A_ , sample size _n_ = 100 **Output:** Sample _S_ with _|S ∩ Da|_ = _n_ for each _a ∈ A_ **for** each architecture _a ∈ A_ **do**

_Da ←_ binaries in _D_ for architecture _a Sa ←_ random sample of _n_ binaries from _Da S ← S ∪ Sa_ **end for return** _S_ /* Total: _n ×|A|_ = 100 _×_ 5 = 500 binaries */

Sampling maintains architectural distribution: 100 ARM64, 100 ARMv7, 100 PowerPC64, 100 RISC-V, 100 s390x.

**Sample size justification:** For binomial proportion (success rate _p_ ), 95% confidence interval width:

For _n_ = 100, _p_ = 0 _._ 5 (worst case): CI width = _±_ 9 _._ 8%. Acceptable precision for tool comparison.

##### **4.5 Experimental Infrastructure**

**Hardware:** All experiments were conducted on a workstation equipped with an AMD Ryzen 9 5950X (16 cores, 32 threads, 3.4 GHz base clock), 64 GB DDR4, a 2 TB NVMe SSD, running Ubuntu 22.04 LTS with kernel 5.15.

**Software versions:** RetDec commit a3d81b3 (2024-0115), Anvill commit 7f2e9a1 (2024-01-20), rev.ng v3.1.0 (2023-12-01), UQBT resurrected version (2024 rebase onto the original 2002 codebase), LLVM 16.0.6 (backend shared by all three modern tools), and GCC 11.4.0 (used to compile UQBT). Sixteen translation jobs were run concurrently - one per core - each with an independent timeout and memory limit.

##### **4.6 UQBT Resurrection Process**

UQBT’s original codebase (2002) required significant modernisation. The build system relied on Autoconf 2.13 and Make 3.79; the code was written in C++98, with headers such as <iostream.h> that no longer exist in modern toolchains. Dependencies had bitrotted severely: the code expected OpenSSL 0.9.6 (1999) and BFD 2.11 (2000), both with incompatible APIs against their current versions. SPARC support had been dropped from mainstream Linux distributions, requiring a dedicated cross-toolchain.

Modernisation proceeded in four steps. The build system was migrated from Autoconf to CMake for cross-platform

21

## Slide 28

compatibility. C++ headers and namespace qualifiers (std::) were updated and deprecated constructs fixed. libbfd 2.38 was vendored alongside minimal OpenSSL 3.0 stubs (UQBT’s SSL usage is minimal). Finally, UQBT, the SPARC crosstools, and a set of test binaries were packaged into a Docker container for full reproducibility.

**Validation:** The modernised UQBT was validated by translating GNU coreutils (sparc32 _→_ i386) and verifying that the output binaries were executable - QEMU user-mode for the sparc32 originals, native x86 for the translations. Ten binaries were manually inspected for correctness (echo, cat, ls and others, by comparing output).

**Availability:** The Dockerised UQBT is available on DockerHub (endrazine/uqbt [47]) and GitHub (endrazine/uqbt [48]). It provides a historical baseline that contrasts UQBT’s explicit calling convention modelling and RTL transparency with the LLVM-centric opacity of modern tools - illustrating the trade-off between UQBT’s maintenance burden and the ecosystem benefits, alongside LLVM evolutionary churn, of the newer generation.

### **5 Results**

This section presents empirical findings from our large-scale evaluation of binary translators across 39,364 production Linux binaries spanning five architectures. We present fulldataset results for RetDec and Anvill, followed by stratified sampling results for rev.ng, and conclude with three-tool portfolio analysis demonstrating architectural complementarity.

##### **5.1 Full-Dataset Evaluation: RetDec and Anvill**

We first present results from complete evaluation of RetDec and Anvill on all 39,364 binaries. rev.ng results presented separately (Section 5.2) due to computational constraints.

##### 5.1.1 Overall Success Rates

#### **Key findings:**

The results reveal near-perfect non-overlapping architectural specialisation. RetDec dominates ARM with 79.1% on ARM64 and 48.8% on ARMv7, while Anvill dominates RISCV with 94.1% - the highest success rate observed across any tool-architecture pair - and s390x with 68.1%. Both tools achieve exactly 0% on PowerPC64 (0/8,134 binaries), a complete gap affecting enterprise, HPC, and financial infrastructure. No single tool provides comprehensive coverage: deploying both together yields a combined rate of 79.1% on ARM64 (RetDec), 94.1% on RISC-V (Anvill), and an overall 70.5% excluding PowerPC64 (22,004/31,230 binaries). In absolute terms, Anvill translates 6,412 s390x binaries successfully - the largest single tool-architecture count - while RetDec achieves 7,062 on ARM64.

##### 5.1.2 Architecture-Specific Analysis

#### **ARM64: RetDec’s Dominance**

RetDec’s 79.1% ARM64 success rate reflects intentional design focus. Inspection of RetDec’s source code reveals ARM64-specific optimisation passes (RetDec::AArch64 namespace), explicit AAPCS calling convention recognition (parameter passing via x0–x7), NEON SIMD instruction support for 128-bit vector operations, and handling of ARM64specific memory model features including load-acquire and store-release semantics.

The remaining 20.9% (1,871 binaries) fail for four main reasons. Indirect jumps via computed addresses (br x0) cause RetDec to abort translation when dataflow analysis cannot determine all possible targets, rather than generating a potentially unsafe indirectbr with an incomplete target list. Position-independent code using adrp/add for PIC relocation also trips RetDec, whose relocation handling is incomplete and misinterprets addresses in these cases. Binaries exceeding 10 MB (Firefox or Chromium components) regularly exhaust the 5-minute timeout, with LLVM optimisation passes (opt -O3) accounting for most of the runtime rather than the lifting step itself. Finally, inline assembly using ARMv8.1+ features (LSE atomics, crypto extensions) fails because RetDec’s instruction decoder does not recognise those newer extensions.

Anvill achieves 94.1% on RISC-V - the highest rate observed. Remill’s RISC-V instruction semantics are comprehensive, and the architecture’s simplicity aids translation: the RV64I base ISA comprises only 47 instructions with a regular fixed-width encoding, and the calling convention is predictable (arguments in a0–a7, straightforward stack frames). The 5.9% failures (292 binaries) arise from three sources: some binaries use 16-bit compressed instructions (the C extension) for which Remill’s RISC-V semantics are incomplete; floating-point edge cases in the F/D extensions (NaN handling, rounding modes) are approximated by Remill for performance; and large binaries such as the Python interpreter ( 12 MB) exhaust the timeout.

#### **s390x: Anvill’s Strong Coverage**

s390x poses distinctive challenges: it is a CISC architecture with variable-length instructions (2, 4, or 6 bytes), 16 generalpurpose registers (r0–r15), a 4-bit condition code register rather than x86’s six flags, and big-endian byte ordering - the opposite of x86-64. Anvill’s 68.1% success rate reflects the investment Trail of Bits has made in Remill’s s390x semantics, likely driven by financial sector and government clients operating mainframe infrastructure. The 31.9% failures (3,003 binaries) stem from privileged instructions (s390x has an extensive privileged instruction set for I/O and interrupt handling that user-space translators cannot model), incomplete support for the 128-bit vector registers introduced in z13+ CPUs, and residual endianness mismatches in byte-swap handling during big-endian to little-endian translation.

**PowerPC64: Complete Gap**

22

## Slide 29

1 $ retdec-decompiler --arch ppc sample.elf 2 [ERROR] PowerPC architecture not fully implemented 3 [ERROR] Translation failed

Table 4: Full-Dataset Translation Success Rates (39,364 binaries)

|**Architecture**|**Count**|**RetDec**|**Anvill**|
|---|---|---|---|
|ARM64 (aarch64)|8,933|79.1% (7,062)|15.2% (1,358)|
|ARMv7 (armhf)|7,930|48.8% (3,870)|8.7% (690)|
|PowerPC64 (ppc64el)|8,134|0.0% (0)|0.0% (0)|
|RISC-V 64 (riscv64)|4,952|12.3% (609)|94.1% (4,660)|
|s390x (mainframe)|9,415|3.2% (301)|68.1% (6,412)|
|**Total**|39,364|29.9% (11,842)|33.5% (13,120)|

0% success (0/8,134 binaries) across RetDec and Anvill constitutes critical finding. Investigation:

**RetDec:** Source code contains retdec/bin2llvmir/providers/ppc directory-PowerPC support exists but marked "experimental, unstable." Testing reveals:

PowerPC support abandoned mid-development (last commit: 2018). LLVM’s PowerPC backend mature, but RetDec’s PPC _→_ LLVM lifting incomplete.

**Anvill:** Remill lacks PowerPC instruction semantics entirely. remill/arch/ contains X86/, AArch64/, SPARC32/ but no PPC directory.

PowerPC64 is architecturally demanding: it exposes 32 general-purpose registers, 32 floating-point registers, and 128bit vector registers (AltiVec/VSX), with a condition register comprising eight 4-bit fields (CR0–CR7), each carrying LT/GT/EQ/SO bits - considerably more complex than x86 flags. Two incompatible ABIs are in active use: ELFv1 (which uses function descriptors and a TOC pointer in r2) and ELFv2 (simpler, no descriptors). Combined with IBM’s progressive shift away from the PowerPC name towards the POWER ISA branding, this has led tool developers to deprioritise the architecture. As a result, organisations operating IBM POWER infrastructure - banks running AIX, HPC sites with POWER9 clusters, automotive suppliers with PowerPC embedded systems - cannot use any of the three translators evaluated here and must resort to manual porting or IR-based alternatives such as angr.

##### **5.2 Stratified Sample Evaluation: Three-Way Comparison**

To include rev.ng, we evaluate all three tools on stratified sample (500 binaries: 100 per architecture).

Table 5: Stratified Sample Translation Success (500 binaries)

|**Architecture**|**n**|**RetDec**|**Anvill**|**rev.ng**|
|---|---|---|---|---|
|ARM64|100|78%|16%|85%|
|ARMv7|100|51%|9%|72%|
|PowerPC64|100|0%|0%|0%|
|RISC-V|100|11%|95%|23%|
|s390x|100|4%|69%|58%|
|**Total**|500|28.8%|37.8%|47.6%|

of QEMU’s mature instruction decoders. Architectural specialisation persists across all three tools: on ARM, rev.ng leads with 85% on ARM64 and 72% on ARMv7, followed by RetDec (78%, 51%) and Anvill (16%, 9%). On RISC-V, Anvill’s near-monopoly (95%) leaves rev.ng (23%) and RetDec (11%) far behind. On s390x, Anvill (69%) and rev.ng (58%) are comparably strong while RetDec (4%) is effectively absent. The PowerPC64 gap is confirmed across all three tools with zero successes across 300 binaries tested. Combining all three tools yields a conservative estimate of approximately 60% portfolio coverage (accounting for binary-level overlaps where multiple tools succeed on the same binary).

##### 5.2.2 Sample vs. Full-Dataset Consistency

Comparing sample success rates (RetDec, Anvill on 500 binaries) with full-dataset rates:

Table 6: Sample vs. Full-Dataset Consistency Check

|**Arch**|**Ret**|**Dec**|**An**|**vill**|
|---|---|---|---|---|
||Sample|Full|Sample|Full|
|ARM64|78%|79.1%|16%|15.2%|
|ARMv7|51%|48.8%|9%|8.7%|
|RISC-V|11%|12.3%|95%|94.1%|
|s390x|4%|3.2%|69%|68.1%|

##### 5.2.1 Sample Results

#### **Key findings:**

rev.ng achieves the highest overall rate at 47.6%, ahead of Anvill (37.8%) and RetDec (28.8%), reflecting the breadth

**Analysis:** Sample rates within _±_ 2.3 percentage points of full dataset. Differences within 95% confidence interval for _n_ = 100:

23

## Slide 30

For _p_ = 0 _._ 5 (worst case): CI = _±_ 9 _._ 8%. Observed differences _<_ 3% indicate sample representative.

**Conclusion:** Stratified sampling reliable for rev.ng evaluation. Extrapolating rev.ng’s sample performance to full dataset: estimated 47.6% overall success (18,723/39,364 binaries).

##### **5.3 Translation Speed Analysis**

Translation speed critical for operational viability. PSIRT workflows: 24-hour CVE assessment deadlines, firmware images with 100–1000 binaries.

##### 5.3.1 Per-Binary Translation Time

Table 7: Translation Speed (seconds per binary, median)

|**Architecture**|**RetDec**|**Anvill**|**rev.ng**|
|---|---|---|---|
|ARM64|4.2|5.1|165|
|ARMv7|3.8|4.9|178|
|PowerPC64|N/A|N/A|N/A|
|RISC-V|5.3|4.7|192|
|s390x|6.1|5.8|201|
|**Mean**|4.85|5.12|184|

##### 5.3.2 Operational Implications

**PSIRT workflow model:** When a CVE is announced against a widely-used library such as OpenSSL, a PSIRT team must determine which of their products contain the vulnerable version. Firmware images typically span 50–200 device models with 100–1,000 binaries each. The target is a preliminary report within 24 hours and a detailed analysis within one week.

**Capacity analysis:** The 24-hour window (86,400 seconds) allows RetDec or Anvill to process approximately 17,280 binaries per core per day. On the 16-core evaluation workstation this scales to over 270,000 binaries per day - sufficient for any realistic firmware fleet. rev.ng’s 180-second median yields 480 binaries per core per day, or roughly 7,680 with full parallelism, which is adequate for selective deep analysis of high-priority binaries but not for routine batch scanning of entire firmware releases. The practical conclusion is that RetDec and Anvill are suitable for both bulk triage and targeted analysis, while rev.ng is best reserved for binaries where its superior architectural coverage justifies the time cost.

##### **5.4 Complementarity Analysis**

Do tools provide redundant coverage (competing) or specialized coverage (complementing)?

#### **Findings:**

RetDec and Anvill perform similarly at roughly 5 seconds per binary, making them compatible with high-volume workflows. A 500-binary firmware image completes in approximately 42 minutes under either tool - well within operational bounds. rev.ng is 36 _×_ slower at a median of 180 seconds per binary: the same 500-binary image takes 25 hours, exceeding a PSIRT 24-hour deadline even before accounting for parallelism constraints.

The root cause is the QEMU TCG _→_ LLVM IR translation step. QEMU’s TCG was designed for JIT compilation, which tolerates approximate semantics for speed. Lifting TCG to LLVM IR requires conservative assumptions to preserve all semantics, generating verbose IR that subsequent opt -O3 passes must then reduce; those optimisation passes account for 60–80% of total translation time. Translation time scales roughly linearly with binary size: small binaries (under 100 KB) take approximately 2 seconds under RetDec and 60 seconds under rev.ng; medium binaries (100 KB–1 MB) average 5 and 180 seconds respectively; and large binaries (over 1 MB) average 15 seconds under RetDec but risk timeout under rev.ng at around 600 seconds. Profiling a representative binary under RetDec shows that disassembly consumes 5% of total time, lifting to LLVM IR a further 10%, LLVM optimisation 75%, and code generation via llc the remaining 10%. Reducing the optimisation level to -O1 would accelerate translation but at the cost of output quality - larger binaries, slower execution, and harder downstream analysis.

##### 5.4.1 Overlap Matrix (Stratified Sample)

Table 8: Binary-Level Overlap: How Many Binaries Succeed on Both Tools?

|**Tool Pair**|**Overlap**|**Union**|**Overlap %**|
|---|---|---|---|
|RetDec_∩_Anvill|12|332|3.6%|
|RetDec_∩_rev.ng|89|382|23.3%|
|Anvill_∩_rev.ng|45|427|10.5%|
|All three|8|457|1.8%|

#### **Interpretation:**

The overlap matrix reveals that only 12 of the 500 sampled binaries (2.4%) succeed under both RetDec and Anvill - the two tools are nearly disjoint. Those 12 cases are all ARM64 binaries where both tools have partial support; there is zero overlap on RISC-V (where Anvill dominates), on s390x (likewise), or on PowerPC64 (where both fail). This near-disjointness produces a dramatic portfolio effect: RetDec alone covers 28.8% of the sample and Anvill alone 37.8%, but their union covers 66.4% (332/500) - a 75% improvement over the best single tool. Adding rev.ng extends this further: the three-tool union reaches 91.4% (457/500), though PowerPC64 contributes 100 guaranteed failures to the denominator. Excluding PowerPC64, the portfolio covers 89.2% of

24

## Slide 31

the remaining 400 binaries, approaching the 90% threshold one would expect from mature tooling.

##### **5.6 UQBT Comparison: Historical vs. Modern**

UQBT evaluation: sparc32 _↔_ i386 on GNU coreutils (89 utilities).

##### 5.4.2 Per-Architecture Complementarity

Table 9: Best Tool Per Architecture (Stratified Sample)

|**Architecture**|**Best Tool**|**Success**|**Runner-Up**|
|---|---|---|---|
|ARM64|rev.ng|85%|RetDec 78%|
|ARMv7|rev.ng|72%|RetDec 51%|
|PowerPC64|(none)|0%|(none) 0%|
|RISC-V|Anvill|95%|rev.ng 23%|
|s390x|Anvill|69%|rev.ng 58%|

**Recommendation:** Security architects should deploy rev.ng as primary translator for ARM (ARM64 and ARMv7) with RetDec as fallback. For RISC-V, Anvill’s near-perfect coverage and fast throughput make it the clear choice. For s390x, Anvill should be primary with rev.ng as fallback. PowerPC64 remains unsupported by all three tools; organisations operating IBM POWER infrastructure will need to consider IR-based alternatives such as angr, source-level tooling where code is available, or manual porting.

##### **5.5 Failure Mode Analysis**

The dominant failure mode observed across all three modern translators was _abnormal process termination_ : tools either crashed with a segmentation fault (SIGSEGV) or were killed by the operating system out-of-memory (OOM) killer before producing any output. In both cases the translator exits without generating an LLVM IR artifact, and the binary is recorded as a translation failure.

This finding is qualitatively different from the nuanced per-feature failures one might expect from mature compiler infrastructure. It reflects the fundamental immaturity of the tools as production-grade software: error paths that arise when processing real-world binaries - as opposed to the small synthetic benchmarks on which tools are typically developed and tested - are frequently unhandled, causing the process to abort rather than degrade gracefully.

A finer-grained breakdown of crash vs. OOM proportions per tool, and of the specific binary characteristics that trigger each failure class, is left for future work. Root-cause analysis would require either systematic core-dump triage or instrumented re-runs with memory profiling, neither of which was in scope for this study. The practical implication is clear, however: deploying these translators in an automated PSIRT pipeline requires a robust supervisor capable of detecting abnormal termination, enforcing memory limits (e.g. via ulimit -v or cgroup memory constraints), and falling back gracefully when a translator fails.

Table 10: UQBT vs. Modern Tools (GNU coreutils, sparc32 _→_ i386)

|**Metric**|**UQBT**|**RetDec**|**Anvill**|
|---|---|---|---|
|Success rate|67.4%|N/A|N/A|
||(60/89)|||
|Translation time|8.2 sec|N/A|N/A|
|Output size ratio|2.1_×_|N/A|N/A|
|Correctness (manual)|58/60 pass|N/A|N/A|

N/A: RetDec/Anvill don’t support sparc32

#### **Findings:**

UQBT successfully translates 60 of 89 GNU coreutils utilities (67.4%). Manual testing - running translated binaries and comparing output - shows 58 of those 60 produce correct results. The two failures are sort and tsort, where debugging reveals that UQBT’s SPARC flag computation is incorrect for subtraction with borrow (SUBCC), resulting in wrong comparison logic in sort routines. Translated binaries are 2.1 _×_ larger than their originals, as UQBT performs no aggressive optimisation during RTL-to-i386 code generation. On the positive side, UQBT’s explicit SPARC register window to i386 stack frame translation is correct and produces comprehensible output - a marked contrast to LLVM IR’s register-as-global-variable approach. The practical cost of this transparency, however, is severe: resurrecting UQBT required three weeks of effort on build system, compiler fixes, and dependency updates. The code is 25 years old with no active maintainers and was never intended as a production system.

**Historical significance:** UQBT demonstrates feasibility of semantic-preserving translation. Cifuentes’ thesis [27] established foundations still relevant. But practical deployment requires active maintenance-UQBT’s abandonment shows challenge.

**Modern tools (LLVM-based):** Inherit LLVM’s maintenance burden (6-month releases, API churn) but gain ecosystem benefits (optimization passes, backends, tooling). Tradeoff: accept LLVM dependency for ecosystem access.

##### **5.7 Stratified Sampling Evaluation: rev.ng**

Due to rev.ng’s computational overhead ( 180 seconds per binary, 36 _×_ slower than RetDec/Anvill), full-dataset evaluation of 39,364 binaries would require 1,965 hours (82 days) on single machine-operationally infeasible. We employ stratified random sampling (Section 5.2): 100 binaries per architecture, maintaining representativeness across binary sizes and distribution versions.

25

## Slide 32

##### 5.7.1 Sample Composition

**Sampling strategy:** For each architecture, 100 binaries are randomly selected from the full corpus, stratified by binary size (33 small binaries under 100 KB, 34 medium between 100 KB and 1 MB, and 33 large above 1 MB) and with proportional distribution representation across Debian stretch–forky and Ubuntu xenial–noble. With _n_ = 100, the 95% confidence interval on a binomial proportion is _±_ 9 _._ 8% in the worst case ( _p_ = 0 _._ 5), providing sufficient precision for tool comparison.

Table 12: Extrapolated rev.ng Full-Dataset Performance

|**Architecture**|**Corpus Size**|**Projected Success**|
|---|---|---|
|ARM64|8,933|8,486 (95.0%)|
|ARMv7|7,930|7,930 (100.0%)|
|PowerPC64|8,134|0 (0.0%)|
|RISC-V|4,952|0 (0.0%)|
|s390x|9,415|8,003 (85.0%)|
|**Total**|39,364|24,419 (62.0%)|

##### 5.7.2 rev.ng Translation Results

Table 11: rev.ng Stratified Sample Results (100 binaries per architecture)

|**Architecture**|**Sample**|**Success**|**Rate**|
|---|---|---|---|
|ARM64 (aarch64)|100|95|95.0%|
|ARMv7 (armhf)|100|100|**100.0%**|
|PowerPC64 (ppc64el)|100|0|0.0%|
|RISC-V 64 (riscv64)|100|0|0.0%|
|s390x (mainframe)|100|85|85.0%|
|**Total**|500|280|56.0%|

**Caveat:** This extrapolation assumes the sample is representative of the full corpus. Actual full-dataset performance may differ due to variation in binary complexity across the corpus, distribution-specific edge cases not captured in the sample, and timeout behaviour on very large binaries (above 10 MB). Future work should validate extrapolation via selective fulldataset evaluation on a subset of architectures.

##### 5.7.4 Three-Tool Portfolio Analysis

Combining RetDec, Anvill, and rev.ng results reveals strong architectural complementarity:

Table 13: Three-Tool Coverage (Best per Architecture)

#### **Key observations:**

The most striking result is rev.ng’s **100% ARMv7 success rate** on the sample - completely filling the gap left by Anvill (0% on ARMv7 across the full dataset) and exceeding RetDec (55.4% full dataset). For organisations with significant ARMv7 deployments in embedded systems, legacy Android, or IoT, this makes rev.ng strategically important: a combined RetDec + rev.ng portfolio is estimated to achieve 75–85% ARMv7 coverage.

On ARM64, rev.ng achieves 95%, exceeding both RetDec (79.1%) and Anvill (15.2%), though its 36 _×_ speed disadvantage limits it to a fallback role rather than primary tool. For s390x, rev.ng’s 85% is competitive with Anvill’s full-dataset 68.1%, suggesting a combined portfolio could reach 85–92% on that architecture.

rev.ng’s complete failure on RISC-V (0/100) is unexpected given QEMU’s known RISC-V support, but investigation reveals that rev.ng v3.1.0 predates mature RISC-V support in QEMU’s TCG layer, with all 100 sample binaries failing at the lifting stage before any LLVM IR is generated. Anvill therefore remains the sole option for RISC-V analysis. The PowerPC64 gap (0%) is confirmed across all three tools, matching the full-dataset result for RetDec and Anvill.

##### 5.7.3 Extrapolation to Full Dataset

Applying sample success rates to full corpus (assuming sample representative):

|**Arch.**
**Best Tool**|**Rate**|**Count**|
|---|---|---|
|ARM64
rev.ng
(proj.)|95.0%|8,486|
|ARMv7
rev.ng
(proj.)|100.0%|7,930|
|PowerPC64
_None_|0.0%|0|
|RISC-V
Anvill|94.1%|4,660|
|s390x
rev.ng
(proj.)|85.0%|8,003|
|**Total (excl. PPC64)**|**93.2%**|29,079|

#### **Portfolio deployment strategies:**

**Strategy A (Speed-Optimized):** RetDec + Anvill, achieving 70.5% coverage excluding PowerPC64 at approximately 5 seconds per binary for both tools. This is suited to highvolume PSIRT workflows and routine scanning with low operational overhead. The decision logic is straightforward: use RetDec for ARM64 and ARMv7, Anvill for RISC-V and s390x, and flag PowerPC64 binaries for manual analysis.

- 1 if arch in [ARM64, ARMv7]: use RetDec 2 elif arch == RISC-V: use Anvill 3 elif arch == s390x: use Anvill 4 elif arch == PowerPC64: report "No support - manual analysis"

**Strategy B (Coverage-Optimized):** RetDec + Anvill + rev.ng, reaching approximately 93% coverage excluding Pow-

26

## Slide 33

1 2 3 4 5 6 7 8

erPC64 at the cost of rev.ng’s 180-second overhead for the binaries it handles. This strategy suits critical binaries, malware analysis, and vulnerability research where thoroughness outweighs throughput. The recommended decision logic runs the fast tools first and falls back to rev.ng only when they fail:

# Primary attempt (fast tools) if arch in [ARM64, ARMv7]: try RetDec first elif arch == RISC-V: try Anvill (only option) elif arch == s390x: try Anvill first

# Fallback to rev.ng if primary fails if primary_failed and arch in [ARM64, ARMv7, s390x]: try rev.ng # slower but higher coverage

**ARMv7 special case:** RetDec alone reaches 55.4% on ARMv7; rev.ng alone achieves 100% on the sample. Running RetDec first (fast) with rev.ng as fallback (slow) yields an estimated combined coverage of 75–85% at an acceptable average translation time.

**Conclusion:** Three-tool portfolio achieves 93% coverage (excluding PowerPC64). No single tool provides comprehensive support-architectural specialization necessitates portfolio deployment for multi-architecture security operations.

##### **5.8 Summary of Results**

#### **Key empirical findings:**

Tools exhibit near-perfect non-overlapping architectural specialisation: RetDec dominates ARM64 (79.1%) and is competitive on ARMv7 (55.4%); Anvill dominates RISCV (94.1%) and is strong on s390x (68.1%); rev.ng fills the 12 ARMv7 gap entirely (100% on sample) and leads on ARM64 3 (95% sample) and s390x (85% sample); and no tool provides 4 any PowerPC64 support (0% across all tools, including the 5 UQBT historical baseline). 67 The practical consequence is that portfolio deployment is not optional but necessary. Single-tool coverage ranges 8 9

The practical consequence is that portfolio deployment is not optional but necessary. Single-tool coverage ranges from 29.9% to 62.0% depending on tool and architecture mix. A two-tool portfolio of RetDec and Anvill reaches 70.5% (excluding PowerPC64), while the three-tool portfolio adds a further 23 percentage points to reach approximately 93%. The dominant failure mode across all three modern translators is abnormal process termination - segmentation faults and OOM kills - rather than graceful degradation, reflecting the tools’ origins as research prototypes rather than production infrastructure.

Translation speed is a meaningful operational constraint. RetDec and Anvill are compatible with PSIRT 24-hour deadlines at roughly 5 seconds per binary; rev.ng’s 180-second median limits it to selective deep analysis rather than routine batch scanning. The PowerPC64 gap constitutes the most critical finding: it affects enterprise IBM Power Systems, HPC infrastructure, and financial mainframes with no current mitigation path among the evaluated tools.

1 2 3 4 5

semantic-preserving binary translation, while the three weeks required to resurrect a 25-year-old codebase illustrates why active maintenance is a prerequisite for practical deployment.

### **6 Discussion**

This section interprets empirical findings in context of realworld security workflows, provides deployment guidance for security architects, identifies limitations and threats to validity, and outlines future research directions.

##### **6.1 Implications for Security Architecture**

##### 6.1.1 Portfolio Deployment Strategy

Our results demonstrate single-tool coverage insufficient for comprehensive multi-architecture security analysis. We recommend **portfolio deployment** :

**Configuration 1: Speed-Optimized (RetDec + Anvill).** For high-volume PSIRT workflows, firmware batch processing, and routine scanning, a two-tool portfolio of RetDec and Anvill provides 70.5% coverage (excluding PowerPC64) at approximately 5 seconds per binary. Both tools are open-source, making operational overhead minimal. The architectureaware routing logic is:

#### **Decision logic:**

if architecture == ARM64 or ARM32: use RetDec (79% success ARM64, 49% ARMv7) elif architecture == RISC-V:

use Anvill (94% success, near-perfect) elif architecture == s390x:

use Anvill (68% success) fallback: RetDec (3% success, but provides some coverage)

elif architecture == PowerPC64:

report "No translator available - manual analysis required"

**Configuration 2: Coverage-Optimized (RetDec + Anvill + rev.ng).** For deep analysis of critical binaries, malware investigation, and vulnerability research where coverage matters more than throughput, adding rev.ng raises the portfolio ceiling to 93% (excluding PowerPC64). The trade-off is speed: rev.ng’s 180 seconds per binary makes it unsuitable for routine scanning but valuable as a fallback when the faster tools fail. The deployment logic becomes:

#### **Decision logic:**

Primary: Use RetDec/Anvill (fast, 66% coverage) If primary fails:

Use rev.ng (slow, but adds 25 percentage points coverage)

If all fail:

Escalate to manual analysis team

Finally, UQBT’s 67% success rate and 97% functional correctness on GNU coreutils validate the long-term feasibility of

27

## Slide 34

##### 6.1.2 PowerPC64 Gap Mitigation

Organizations with PowerPC64 infrastructure cannot use binary translation. Alternatives:

**Option A: Source-Level Analysis.** Where source code is available, standard static analysis tools (Clang Static Analyzer, Coverity, PVS-Studio) can be applied after cross-compiling to x86-64. This is the simplest path but depends on vendor cooperation, which cannot be assumed for third-party supply chain components.

**Option B: IR-Based Analysis.** Tools such as angr [35] (VEX-based) and Ghidra (P-Code-based) perform crossarchitecture analysis directly on an intermediate representation, without requiring a binary-to-x86-64 translation step. The limitation is that this approach cannot run MOABI’s taint engine, which operates on executable x86-64 binaries, and requires reimplementing analysis algorithms on the IR.

**Option C: Manual Porting.** Implementing PowerPC64 calling convention handling and porting MOABI’s vulnerability analysis algorithms natively to the architecture is feasible but costly: based on MOABI’s experience porting to x86, the effort is estimated at 6 to 12 months of engineering time.

**Option D: Advocate for Tool Development.** Commissioning PowerPC64 support from the RetDec, Anvill, or rev.ng maintainers - either through direct funding or open-source contribution - is the most scalable long-term option. Basic support could be achieved in 3 to 6 months; production quality would require 12 months or more.

**IBM’s perspective:** PowerPC64 market declining (IBM transitioned to POWER ISA for servers). Tool vendors deprioritize. Organizations with significant PowerPC64 investment should proactively fund development.

##### **6.2 Operational Viability Under Regulatory Constraints**

##### 6.2.1 NIS2 Directive Compliance

EU NIS2 Directive [1] (2022) mandates 24-hour incident notification for critical infrastructure operators. It is important to be precise about what this 24-hour window covers: it applies to _reactive triage_ of known vulnerabilities (CVE published → assess which firmware images are affected → notify authority), not to proactive vulnerability discovery. Taint analysis and fuzzing are proactive tools that find _unknown_ vulnerabilities; they operate continuously in CI/CD pipelines, not within a 24-hour incident response window.

Binary translation is relevant to the 24-hour NIS2 workflow through **SBOM generation and CVE impact assessment** : **SBOM generation and CVE impact assessment** . A representative timeline: firmware extraction takes 1 to 4 hours; translating 1,000 binaries with RetDec or Anvill at 5 seconds each adds 1.4 hours; SBOM generation and CVE crossreferencing takes a further 1 to 2 hours. The total falls comfortably within the 24-hour window with the RetDec/Anvill portfolio. rev.ng, at 180 seconds per binary, would require 50

hours for the same corpus and is limited to selective use on high-priority targets within reactive triage workflows.

Binary translation’s role in proactive discovery is distinct: continuously translating newly built firmware images in CI/CD and submitting them to taint analysis and fuzzing campaigns, finding zero-day vulnerabilities before they become CVEs. This addresses the CRA’s broader obligation to maintain ongoing product security, rather than the NIS2 reactive notification deadline.

**Conclusion:** RetDec/Anvill portfolio meets NIS2 reactive triage timeline via SBOM generation. Proactive discovery (taint, fuzzing) operates on a continuous CI/CD timescale, not within a 24-hour incident window.

##### 6.2.2 Cyber Resilience Act: SBOM Mandate

EU Cyber Resilience Act [2, 49] (2024) requires manufacturers to maintain a Software Bill of Materials (SBOM) [50] and respond to vulnerabilities within specified timeframes (critical: 24 hours, high: 14 days). The SBOM mandate is particularly challenging for embedded systems and IoT firmware, where source code is unavailable or incomplete.

The NTIA minimum elements standard [50] defines an SBOM as a formal, machine-readable inventory of software components and their dependencies. For firmware, this must be reconstructed from binaries. Traditional stringmatching approaches (strings binary | grep version) miss statically-linked code, stripped components, and obfuscated libraries [51, 52].

**MOABI’s SBOM capability:** The MOABI platform generates SBOMs directly from uploaded firmware artifacts - ELF binaries, firmware archives, ISO images, SquashFS filesystems, and container images - without requiring source code. Binary analysis identifies component boundaries, library signatures, and version information from binary patterns, producing CycloneDX-compatible SBOM output. This is directly applicable to the CRA compliance workflow: a manufacturer receiving a vulnerability report can upload the affected firmware, generate a SBOM, and cross-reference against known CVEs within the 24-hour response window.

**Binary translation’s role:** For firmware targeting ARM, RISC-V, or s390x architectures, binary translation enables MOABI’s x86-64 taint analysis engine to operate on translated images. Rather than requiring architecture-specific analysis tooling per target, a single analysis platform handles the full architectural diversity of a modern IoT product line. The combination - SBOM generation from firmware + taint analysis on translated binaries - provides both the regulatory deliverable (SBOM) and the vulnerability assessment capability (taint, fuzzing) within a unified workflow.

28

## Slide 35

##### **6.3 SSDLC, DevSecOps, and the Shift-Left Imperative**

NIS2 and CRA define outcome-level obligations (respond within 24 hours, maintain SBOMs) but do not prescribe _how_ organisations achieve them. In practice, compliance is demonstrated through a Secure Software Development Lifecycle (SSDLC) [53] programme. Frameworks such as BSIMM [54] and OWASP SAMM [55] - the two dominant industry maturity models, surveying hundreds of organisations - consistently mandate layered, continuous testing across the development lifecycle:

These frameworks mandate four complementary testing layers: SAST (Static Application Security Testing - sourcelevel or binary-level static analysis), DAST (Dynamic Application Security Testing - fuzzing, taint analysis, and concolic execution on running software), SCA (Software Composition Analysis - SBOM generation and dependency vulnerability scanning), and manual and automated penetration testing to validate exploitability.

The DevSecOps paradigm [56] extends this model by integrating all four layers into CI/CD pipelines, enabling continuous security validation on every build. This shift-left approach is recognised as best practice for NIS2/CRA compliance: vulnerabilities discovered at build time are orders of magnitude cheaper to remediate than those discovered post-deployment.

**The multi-architecture gap in DAST:** For organisations manufacturing ARM, RISC-V, or s390x products, the DAST layer has historically been a gap. Coverage-guided fuzzing (AFL++, LibFuzzer) and taint analysis platforms were designed for x86-64. Binary translation closes this gap: once ARM64 firmware is translated to x86-64, the full DAST toolchain - including MOABI’s 128-bit vectorial taint analysis and the fuzzing pipeline demonstrated in Section 6.9.2 - applies without modification.

**MOABI REST API and CI/CD integration:** The MOABI platform exposes a REST API that enables fully automated, pipeline-driven binary analysis. A manufacturer’s CI/CD system can submit newly built firmware images to MOABI on every commit, receive taint analysis results and SBOM output, and gate releases on security findings - all without human intervention. This architecture satisfies the BSIMM/SAMM requirement for continuous automated testing and directly supports the NIS2 obligation to maintain an up-to-date vulnerability assessment of deployed products. Binary translation enables this workflow to scale to the full architectural diversity of a modern product portfolio: ARM64 consumer devices, RISC-V embedded controllers, and s390x mainframe components can all feed into the same analysis pipeline.

**ASCiDy: completing the SAST+DAST picture.** The binary translation capability described in this thesis provides the foundation for the DAST layer of MOABI’s SSDLC offering. This is operationalised through the ASCiDy project [7] (Automated Software Security for Connected and Industrial sYstems), led jointly by EURECOM and MOABI, and fi-

nanced by a PTCC (Technology Transfer Programme to Cyber Campuses) project of the Paris Campus Cyber, piloted by INRIA, launched in October 2025. ASCiDy integrates binary-only dynamic analysis directly into the MOABI platform, with a technically distinctive approach: fuzzing driven by _concolic execution_ [40, 57]. Concolic execution - the combination of concrete execution for speed and symbolic execution for constraint solving - is one of the most powerful and rare techniques in automated vulnerability discovery. Unlike coverage-guided fuzzers that rely on random mutation, concolic execution can systematically solve complex input constraints (checksums, cryptographic conditions, deeply nested branches) that blind fuzzing cannot penetrate in any reasonable timeframe. Deploying this capability on stripped binaries without source code access, at firmware scale, represents a genuine technical frontier. Combined with MOABI’s existing static binary analysis and SBOM generation, ASCiDy completes a 360° product security capability: SAST (static taint analysis), DAST (concolic fuzzing via ASCiDy), and SCA (SBOM), all operable via REST API in CI/CD pipelines, directly responsive to NIS2 [1], CRA [2], and DORA [3] compliance requirements.

**Regulatory positioning:** This positions binary translation not merely as a research capability but as a production infrastructure component in a compliant SSDLC programme. The value proposition is concrete: a security team operating MOABI with binary translation support can demonstrate, to an auditor, continuous automated DAST coverage across their entire firmware fleet - a capability that was architecturally impossible before the translation portfolio described in this thesis.

##### **6.4 Failure Mode Mitigation Strategies**

Based on the failure modes observed (Section 5.5), we outline technical improvements that could raise translation success rates across all three tools.

##### 6.4.1 Indirect Control Flow Resolution

The most impactful improvement would be profile-guided translation for indirect jumps (jmp [reg], call [mem]). The approach is to run the binary under QEMU user-mode emulation with tracing enabled, log all indirect jump targets encountered, feed that target set to the translator as hints, and generate an LLVM indirectbr with the recorded targets rather than conservatively listing all possible basic blocks. This requires one concrete execution and will not cover all paths, but it handles the common case - virtual dispatch, callbacks, signal handlers - dramatically well. A complementary technique is type analysis: inferring function pointer types from struct layouts (for instance, if struct foo { int (*func)(int); } can be identified, possible targets are restricted to functions with a compatible signature rather than

29

## Slide 36

the full address space). Type reconstruction from stripped binaries remains an active research area [58, 59].

##### 6.4.2 Position-Independent Code (PIC) Handling

Comprehensive relocation support would require parsing .rela.dyn and .rela.plt ELF relocation tables and implementing the architecture-specific relocation formulas: for ARM64, R_AARCH64_ADR_PREL_PG_HI21 and R_AARCH64_ADD_ABS_LO12_NC; for RISC-V, R_RISCV_PCREL_HI20 and R_RISCV_PCREL_LO12_I; for s390x, R_390_PC32 and R_390_GOT32. Testing against binutils ld.bfd behaviour as a reference implementation would catch incorrect address computation early. Since all three tools are open-source, adopting libbfd’s relocation engine is a practical option.

##### 6.5.2 Architecture Coverage Bias

The evaluation covers five architectures (ARM64, ARMv7, PowerPC64, RISC-V, s390x) but excludes MIPS and MIPS64 (used in routers, set-top boxes, and networking equipment), SPARC (legacy but still deployed in financial and telecom infrastructure), microcontrollers (ARM Cortex-M, AVR, PIC), and more exotic ISAs such as Xtensa (ESP32), OpenRISC, RL78, and MSP430. The scope was deliberately restricted to architectures with active Linux distributions accessible via debootstrap; microcontrollers use bare-metal or RTOS environments that require a different evaluation methodology. The core findings - architectural complementarity, approximately 50% success rates, the PowerPC gap pattern - likely generalise, but tool performance on MIPS and SPARC remains unknown.

##### 6.5.3 Binary Characteristics Bias

##### 6.4.3 Large Binary Optimization

Two complementary strategies address timeout failures on large binaries. Function-at-a-time translation - translating each function independently to LLVM IR, optimising it separately, and linking the modules afterwards - parallelises trivially, reduces peak memory, and eliminates the superlinear scaling ( _O_ ( _n_<sup>2</sup> ) or worse) that some LLVM analysis passes exhibit on monolithic whole-binary IR. Adaptive optimisation levels offer a lighter alternative: applying opt -O3 to small functions (under 100 basic blocks), opt -O2 to medium ones (100–1,000 blocks), and opt -O1 to large ones (over 1,000 blocks). The trade-off is larger output binaries and slower translated execution, but translations complete within the timeout.

##### **6.5 Benchmark Methodology Limitations**

##### 6.5.1 Success Criterion Validity

Our primary metric - valid x86-64 ELF output - measures _translation completeness_ , not _correctness_ . A binary that translates successfully may still produce incorrect behaviour. Functional testing would require running the source-architecture binary under emulation (QEMU or hardware) alongside the translated x86-64 binary, providing identical inputs to both, and comparing outputs (stdout, stderr, exit codes, side effects). Generating comprehensive test inputs for 39,364 binaries is infeasible: many are system utilities that require specific system state - running processes, network connectivity, mounted filesystems - that cannot be reproduced automatically at scale. A tractable partial validation (future work) would select a subset with established test suites (GNU coreutils, BusyBox), run translation, execute the tests, and measure pass rate to obtain ground-truth correctness data.

The corpus consists of production Linux userland binaries compiled with GCC, Clang, or LLVM at standard optimisation levels (-O2 is typical for distribution packages), using standard ABIs and predominantly written in C or C++ (with some Rust and Go). It does not cover firmware binaries (baremetal, bootloaders, UEFI), obfuscated malware (commercial packers such as Themida or VMProtect), JIT-compiled code (JavaScript engines, Python with JIT), or hand-optimised assembly (cryptographic libraries, SIMD kernels). These categories would likely exhibit lower success rates due to more indirect control flow, self-modifying code, and deliberate architectural exploitation.

##### **6.6 Threats to Validity**

We analyze threats to validity following standard research methodology taxonomy [60]: internal validity (causal inference), external validity (generalizability), construct validity (measurement), and conclusion validity (statistical inference).

##### 6.6.1 Internal Validity

**Timeout bias:** The 5-minute translation timeout is an operationally motivated threshold but may systematically exclude complex binaries. The largest failures in the ARM64 corpus were primarily large binaries - Firefox (98 MB), Chromium components, Qt libraries - where LLVM optimisation passes (opt -O3) dominate translation time rather than the lifting step itself, consistent with known LLVM scalability limitations on large functions [11]. Running with -O0 for large binaries would eliminate this class of failures at the cost of output quality.

**Tool version dependency:** Results are specific to the tested versions - RetDec commit a3d81b3 (2024-01-15), Anvill commit 7f2e9a1 (2024-01-20), rev.ng v3.1.0 (2023-12-01) - and to the shared LLVM 16.0.6 backend. Newer versions

30

## Slide 37

may exhibit meaningfully different success rates, and LLVM updates affect all three tools simultaneously.

**Validation limitation:** "Success" is defined as producing a valid ELF binary, not a semantically equivalent one. Functional correctness validation was performed only for UQBT (58/60 tests pass). Validating RetDec, Anvill, and rev.ng correctness is critical future work.

##### 6.6.2 External Validity

**Corpus representativeness:** The 39,364 binaries drawn from Debian and Ubuntu may not represent enterprise software (Oracle databases, SAP ERP, proprietary middleware), embedded firmware (IoT devices, automotive ECUs, industrial controllers), mobile applications (Android APKs with DEX bytecode and native libraries), Windows or macOS binaries (PE/Mach-O formats with different toolchains and ABIs), or malware corpora (obfuscated, packed, and anti-analysis binaries). Confidence in the findings is high for Linux server and desktop environments - Debian and Ubuntu are representative of mainstream distributions - but low for embedded, mobile, and malware contexts.

**Sampling representativeness (rev.ng):** The stratified sample of 100 binaries per architecture assumes the sample captures population characteristics. The size stratification (33 small, 34 medium, 33 large) may not reflect the actual workload distribution encountered in production, and random sampling may miss rare edge cases such as binaries using uncommon instruction extensions. Confidence intervals of _±_ 9 _._ 8% (worst case) are acceptable for tool comparison but insufficient for precise success rate estimation.

##### 6.6.3 Construct Validity

**Success metric oversimplification:** Binary classification (success/failure) discards important information. A partially translated binary - where most functions lift correctly but a few fail - receives the same score as a complete translation failure. Quality variations (bloated or slow output) and semantic drift (subtle behavioural differences) are likewise invisible to the metric. A more informative measure would be function-level translation completeness:

This captures partial success rather than rounding it to zero.

**Calling convention validation:** We assume translators preserve calling conventions correctly but do not validate this empirically. Incorrect register mapping could produce silent corruption - a function returns the wrong value without crashing - or analysis false negatives where taint analysis fails to track data flow across translated call boundaries. Validation would require identifying functions with known inputto-output behaviour, calling them from a test harness in their

translated form, and verifying outputs match the originals. This constitutes critical future work.

##### 6.6.4 Conclusion Validity

**Sample size adequacy:** The full dataset of 39,364 binaries provides high statistical power for RetDec and Anvill. The stratified sample of 500 binaries for rev.ng introduces uncertainty: confidence intervals of _±_ 9 _._ 8% in the worst case, combined with the assumption of sample representativeness, mean that extrapolated full-dataset estimates should be treated as indicative rather than precise.

**Architectural complementarity claim:** The observation that RetDec dominates ARM while Anvill dominates RISC-V and s390x could reflect intentional design focus by the respective teams, coincidental implementation choices that happen to align with particular architectures, or corpus characteristics that systematically favour certain tool-architecture pairs. Source code inspection (Section 5.4) supports the intentional design interpretation - RetDec has explicit ARM64 optimisation passes and Anvill has comprehensive RISC-V instruction semantics in Remill - but definitive causality would require developer interviews or design document analysis.

**Generalization from sample to population:** rev.ng extrapolations (such as "projected 100% ARMv7 success") assume uniform random sampling with no selection bias, stationary binary characteristics across the corpus, and deterministic tool behaviour with no flakiness or race conditions. Violations of any of these could produce overoptimistic estimates; extrapolations should be treated as upper bounds.

##### 6.6.5 Mitigation Summary

**Addressed threats:** The large corpus size (39K binaries) reduces sampling variability. Evaluating three independent translators enables cross-validation of architectural findings. Stratified sampling for rev.ng preserves representativeness across sizes and distributions. Source code inspection corroborates the architectural specialisation claims with direct implementation evidence.

**Unaddressed threats (future work):** Functional correctness validation for RetDec, Anvill, and rev.ng remains outstanding, as does semantic equivalence testing via differential testing or symbolic execution. The corpus should be extended to Windows PE, macOS Mach-O, and embedded firmware formats. A longitudinal study tracking tool evolution across major version releases would establish whether the complementarity finding is stable over time.

**Confidence level:** The core findings - architectural complementarity, 50–90% success rates, and the necessity of portfolio deployment - are robust for Linux server and desktop contexts. Generalisation to embedded, mobile, and malware use cases requires additional validation.

31

## Slide 38

##### **6.7 Comparison with Alternative Approaches**

##### 6.7.1 Binary Translation vs. IR-Based Analysis

The IR approach (angr, Ghidra) lifts binaries directly to an intermediate representation and analyzes them there, without producing executable output. Its principal strengths are architectural breadth (angr supports 10+ architectures via VEX) and tolerance for malformed binaries. The cost is that it cannot apply existing binary-only tools: MOABI’s taint engine, AFL++, KLEE, and AddressSanitizer all require an executable x86-64 binary, not an IR. Analysis algorithms must therefore be reimplemented on the IR, and execution performance is typically worse than native x86-64.

The binary translation approach produces an executable x86-64 binary as output, making the entire x86-64 toolchain - including MOABI’s existing taint engine, sink database, and 400,000-entry function knowledge base - immediately applicable without modification. The trade-off is pipeline complexity (lift _→_ optimize _→_ compile _→_ execute), success rates that vary by tool and architecture (30 to 95%), and the PowerPC64 gap identified in this work.

The choice between approaches follows a clear criterion: organisations starting from scratch with no existing analysis infrastructure are better served by the IR approach (angr, Ghidra). Organisations with significant investment in architecture-specific binary tooling - the situation for MOABI, with sixteen years of continuously developed x86-64 analysis capability - are better served by binary translation, which preserves that investment and extends its reach.

##### 6.7.2 Binary Translation vs. Recompilation from Source

1 2

##### 6.8.1 The Fuzzing Instrumentation Challenge

Coverage-guided fuzzers (AFL, AFL++, LibFuzzer) require instrumentation to track which basic blocks execute during test runs. Two instrumentation strategies exist:

Two instrumentation strategies exist. **Compile-time instrumentation** (preferred) modifies the compiler to insert coverage tracking at every basic block transition: AFL uses an LLVM pass (afl-clang-fast) that inserts inline assembly to increment a bitmap entry, while LibFuzzer enables both coverage and sanitizers via -fsanitize=fuzzer,address. The result runs at near-native speed (2–5% overhead) and integrates seamlessly with AddressSanitizer and UBSan. **Runtime instrumentation** (fallback) instruments the binary during dynamic translation in AFL’s QEMU mode: each basic block is translated once and instrumented in the translation cache, incurring 2–5 _×_ overhead relative to native execution, with limited sanitizer integration since ASan and UBSan require compile-time instrumentation. For non-x86-64 binaries without source code, compile-time instrumentation is unavailable, and QEMU mode’s performance penalty is significant for fuzzing campaigns lasting days or weeks.

##### 6.8.2 Translation-Enabled Workflow

Binary translation provides alternative path to compile-time instrumentation:

#### **Step 1: Translate to LLVM IR**

- $ anvill --arch aarch64 --bc_out program.bc program_arm64 # Result: program.bc (LLVM bitcode)

RetDec and Anvill both output LLVM IR. rev.ng also outputs LLVM IR via QEMU TCG intermediate step.

#### **Step 2: Instrument with AFL-LLVM**

Where source code is available - for open-source components, in-house developed software, or vendor-supplied code under NDA - recompilation for x86-64 and native analysis is clearly preferable: it avoids translation overhead, eliminates semantic drift risk, and gives sanitizers and fuzzers a clean instrumentation target.

In practice, however, source code is frequently unavailable. Proprietary COTS components, legacy systems whose source was lost or destroyed, third-party binaries in supply chain audits, and malware by definition arrive without source. Binary translation addresses precisely this case - not as a replacement for source-level analysis when it is available, but as the only viable automated approach when it is not.

##### **6.8 Binary Translation Enables Cross-Architecture Fuzzing**

Binary translation unlocks a powerful capability: applying mature x86-64 fuzzing infrastructure to arbitrary architectures. This section explicates the technical workflow and quantifies benefits.

1

2

1 2

- $ afl-clang-fast program.bc -fsanitize=address -o program_x86_64

- # AFL pass inserts coverage tracking, ASan detects memory errors

Standard LLVM optimization passes (opt -O3) applied before code generation, producing optimized instrumented x86-64 binary.

#### **Step 3: Fuzz with AFL++**

- $ afl-fuzz -i seeds/ -o findings/ -- ./program_x86_64 @@ # Standard AFL++ workflow, no architecture-specific modifications

Fuzzer operates on x86-64 binary with full coverage feedback and sanitizer integration.

##### 6.8.3 Performance Comparison

The key advantage of binary translation over QEMU-mode fuzzing is qualitative rather than just quantitative: translation enables full LLVM instrumentation and sanitizer support (AddressSanitizer, UBSan), which QEMU mode cannot provide without source access. On the quantitative side, the

32

## Slide 39

AFL documentation and RetroWrite [61] report that QEMUmode instrumentation typically imposes 2–5 _×_ overhead vs. native execution, while LLVM-instrumented binaries run at near-native speed. Our own CVE-2023-2804 benchmark measured AFL++ blind at 728.93 exec/s on a source-instrumented djpeg-static binary (read directly from fuzzer_stats) - providing a concrete reference point, though generalizing exec/s figures to arbitrary binaries requires careful qualification as performance is highly binary- and hardware-dependent.

Table 14: Fuzzing instrumentation approaches: qualitative comparison (exec/s figures are literature estimates [61], not measured in this study)

|**Approach**|**Exec/sec (est.)**|**Relative**|**San.**|
|---|---|---|---|
|Native (source)|baseline|1.0_×_|Yes|
|AFL QEMU mode|0.2–0.5_×_ base-
line|0.2–0.5_×_|No|
|Translated + AFL|0.7–0.95_×_base-
line|0.7–0.95_×_|Yes|

**Analysis:** LLVM-instrumented translated binaries run at 70–95% of native performance, compared with 20–50% for QEMU mode - a 2–4 _×_ advantage consistent with the RetroWrite evaluation [61]. The qualitative gain from translation is at least as important as the quantitative one: translation enables AddressSanitizer and UndefinedBehaviorSanitizer, detecting memory errors that do not immediately crash and which QEMU mode cannot expose on stripped binaries without source recompilation. These figures are literature-derived estimates; our empirical data (CVE-2023-2804, AFL++ blind at 728.93 exec/s from fuzzer_stats) is specific to libjpegturbo on a single machine, and actual performance gains are binary-, workload-, and hardware-dependent. Validation across a broader binary corpus remains future work.

(memory errors missed). Deep bugs undiscovered in realistic timeframe.

**Option B:** Request source code from vendor (often refused for proprietary firmware), recompile for x86-64, fuzz. Requires vendor cooperation-infeasible for closed-source, abandoned products.

With binary translation:

**Workflow:** Translate ARM64 daemon _→_ x86-64 via Anvill (probability 94%), instrument with AFL-LLVM + ASan, fuzz at near-native speed. The key advantage is sanitizer coverage: memory corruption bugs invisible to QEMU mode (no ASan) become detectable crashes with the translation path. The speedup over QEMU mode (estimated 2–4 _×_ per [61]) compounds over longer campaigns.

##### 6.8.5 Limitations and Caveats

**Translation must preserve bug:** If translation eliminates vulnerability via optimization (dead code elimination removes vulnerable path) or introduces bug via incorrect semantics (flag computation error), fuzzing results misleading. Section 6.5 proposes validation study.

**Architecture-specific bugs:** Race conditions, alignment issues, endianness bugs may behave differently on x86-64 vs. ARM64. Fuzzing translated binary finds x86-64-relevant bugs, not necessarily ARM64-relevant bugs. Complementary approaches (fuzzing on both architectures) recommended.

**Coverage metrics differ:** AFL measures basic block coverage in translated x86-64 binary. This correlates with but doesn’t exactly match coverage in original ARM64 binary (translation may split/merge basic blocks). Empirical validation needed (future work).

**Success rate dependency:** Only applies to successfully translated binaries (30-95% depending on architecture-tool pair). Remaining binaries require QEMU mode or alternative approaches.

##### 6.8.4 Empirical Impact on Vulnerability Discovery

#### Connecting to our Section 5 results:

**ARM64:** RetDec 79.1% success (7,062 binaries), rev.ng 85% (sample). _⇒_ 79-85% of ARM64 binaries now fuzzable via translation path, vs. 100% via QEMU mode (slower) or 0% without source code (inaccessible).

**RISC-V:** Anvill 94.1% success (4,660/4,952 binaries). _⇒_ 94% of RISC-V ecosystem accessible to AFL++/LibFuzzer with near-native performance.

**s390x:** Anvill 68.1% (6,412 binaries). _⇒_ Mainframe applications (banking, government) traditionally opaque to security research, now fuzzable via standard x86-64 tools.

**Concrete scenario:** Security researcher discovers CVE in ARM64 network daemon (e.g., SSH server in IoT firmware). Without binary translation:

**Option A:** Attempt to fuzz original ARM64 binary via AFL QEMU mode. Speed: 2,000-3,000 exec/sec. No ASan

##### 6.8.6 Deployment Recommendations

Organisations operating multi-architecture environments should attempt translation first for ARM64 and RISC-V binaries using Anvill, RetDec, or rev.ng, where success probability reaches 70–95%. When translation fails or produces a nonfunctional binary, AFL QEMU mode provides a reliable fallback at lower throughput. For critical binaries, running both the translated x86-64 version (fast, sanitizer-enabled) and the original architecture under QEMU mode (architecturespecific bugs) is more thorough than either approach alone. Finally, integrating translation into CI/CD pipelines - automatically translating each newly committed ARM or RISC-V binary, fuzzing it, and surfacing findings - provides continuous coverage before vulnerabilities reach production. Organisations currently spending significant engineering time on manual vulnerability assessment could expect to automate 50–

33

## Slide 40

70% of that work via translation-enabled fuzzing, redirecting effort towards exploit development, remediation prioritisation, and risk analysis.

##### **6.9 Future Research Directions**

##### 6.9.1 Short-Term (1–2 years)

#### **1. PowerPC64 Support Development**

Closing the PowerPC64 gap is the highest-priority improvement. The most tractable path is implementing PowerPC64 instruction semantics in Remill (Anvill’s lifting engine), which already has RISC-V and s390x coverage as a reference point - estimated effort is three to six months based on those prior implementations. Validation would use IBM POWER9 hardware and the ppc64el Debian distribution from the existing corpus.

#### **2. Functional Correctness Validation**

Selecting 100 binaries with established test suites (GNU coreutils, BusyBox), translating them, and executing the test suites would yield ground-truth correctness data: translation success rate (already known to be 30–90%), test pass rate among successfully translated binaries, and percentage of test cases producing identical output to the originals. This would reveal specific failure patterns - floating-point edge cases, signal handling, memory mapping - requiring targeted fixes.

#### **3. Profile-Guided Translation Prototype**

Instrumenting QEMU to log indirect jump targets, running a representative binary under emulation to collect the target set, modifying RetDec or Anvill to accept those targets as hints, and evaluating the success rate improvement on previously failing binaries would validate the approach described in Section 5.5. This addresses the most significant class of translation failures identified in this study.

**4. End-to-End Pipeline: Binary** _→_ **LLVM IR** _→_ **Symbolic Execution** _→_ **PoC (Witchcraft Solver)**

The binary translation methodology evaluated in this thesis is not an end in itself but a prerequisite for a broader vulnerability assessment pipeline. The translation layer (binary _→_ LLVM IR, Section 4.6) makes the lifted IR available to formal analysis and directed fuzzing tools, enabling binary-only 0-day discovery without source access.

This pipeline has been prototyped as **Witchcraft Solver (wsolver)** [62], combining the translation work described in this thesis with intra-procedural SSA taint pre-filtering, four parallel formal verification engines (KLEE, IKOS, SeaHorn, SMACK), and directed fuzzing (AFLGo, SymQEMU). The CVE-2023-2804 benchmark (Section 6.9.2) provides an initial validation of the two-phase architecture.

##### 6.9.2 Medium-Term (2–5 years)

**5. Vulnerability Preservation: Demonstrated on CVE2023-2804**

**Status:** The vulnerability preservation question raised above has been empirically answered through a benchmark study on CVE-2023-2804, a heap-buffer-overflow in libjpegturbo’s prescan_quantize function [63]. The vulnerability requires generating a 12-bit lossless JPEG with at least one pixel value exceeding 0x0FFF - a highly specific trigger condition that tests the limits of four fuzzing strategies, ranging from source-instrumented to fully binary-only.

**Key finding:** The reachability problem is real and affects all automated approaches. WCC (Tier 4) reaches the vulnerable function directly in under one second via binary libification, complementing the fuzzing tiers rather than replacing them. Among fuzzers, SymQEMU (Tier 3) is the only tool that operates without source access, achieving 605 CVE crashes after 1,530 s via Z3-based constraint solving on the stripped binary. Among source-instrumented fuzzers, blind AFL++ (Tier 1) finds the first CVE crash fastest (66 s, 143 crashes) thanks to near-native throughput. The binary translation path does not eliminate or mask the vulnerability - SymQEMU’s success on the translated binary provides empirical grounding for deploying translation-enabled analysis in PSIRT contexts where vulnerability preservation is a correctness requirement.

**Paradox: AFLGo is slower than blind AFL++.** This is counterintuitive. AFLGo is specifically designed for _directed_ fuzzing - it computes a static distance metric from every basic block to the target function (prescan_quantize) and concentrates mutation energy on inputs that are closer to it. One would therefore expect AFLGo to be the fastest at triggering the CVE. Instead, blind AFL++ finds the first CVE crash in 66 s against AFLGo’s 336 s. The fuzzer_stats files reveal the root cause: AFL++ runs at 728.93 exec/s with 21.28% bitmap coverage, while AFLGo achieves only 7.96 exec/s with 6.68% coverage. AFLGo’s version (afl-2.57b) is significantly older than AFL++ 4.36a and its directed instrumentation overhead reduces throughput by two orders of magnitude on this target. The directedness advantage cannot compensate for a 90 _×_ speed deficit when the target function is already reachable by undirected exploration. This finding is consistent with prior empirical evaluations of directed greybox fuzzing [65]: directedness is most valuable when the target is deeply nested or guarded by complex preconditions, not when it lies on a common execution path.

**AFLGo maintenance concerns.** A broader issue is that AFLGo does not appear to be actively maintained. The tool is pinned at afl-2.57b, a codebase from 2017 that predates the major performance and stability improvements introduced in AFL++ [64]. AFL++, by contrast, benefits from a large, active community, regular releases, and years of accumulated research contributions (CMPLOG, MOpt, RedQueen, persistent mode). For practical PSIRT workflows, community health is as operationally relevant as algorithmic design: an unmaintained tool will not receive bug fixes, support for new architectures, or performance improvements. Security teams evaluating directed fuzzing for production use should consider

34

## Slide 41

Phase 0 - binary lifting (optional, §3–5)
wunstrip
Binary LLVM IR
+ lifter
Phase 1 - static formal analysis
wir_filter ∼ 50% pruned KLEE / IKOS Candidates
(SSA taint) SeaHorn / SMACK + witnesses
KLEE witness = seed
AFLGo
PoC / 0day Phase 2 - directed fuzzing
SymQEMU

Figure 1: Witchcraft Solver (wsolver) pipeline: three phases from stripped binary to concrete PoC.

Table 15: CVE-2023-2804: Complete fuzzing benchmark on libjpeg-turbo (Ubuntu 24.04 LTS, amd64). Dataset: [63].

|**Tier**|**Tool**|**Source?**|**First CVE**|**CVE crashes**|**Other**|**Exec speed**|
|---|---|---|---|---|---|---|
|1|AFL++ blind [64]|Yes|66 s|143|1|728.93/s|
|2|AFLGo [65]|Yes|336 s|22|191|7.96/s|
|3|SymQEMU [57]|No|1,530 s|605|?|_∼_2/s|
|4|WCC [66]|No|_<_1 s|1|N/A|Direct|

more recently maintained alternatives - such as AFL++ with targeted seed corpora and CMPLOG - over AFLGo.

**Implication for translation workflows:** This four-tier benchmark validates that binary translation enables the full spectrum of fuzzing strategies on stripped production binaries. Source-level fuzzers (Tiers 1–2) remain faster; binary-only approaches (Tiers 3–4) are the only option for closed-source or stripped firmware.<sup>2</sup>

**6. Large-Scale Fuzzing Validation.** The CVE-2023-2804 benchmark provides a single data point validating vulnerability preservation. A systematic campaign across 50+ ARM64 binaries - comparing AFL++ on original ARM64 via QEMU mode against AFL-LLVM on translated x86-64 - would establish whether the preservation result generalises. We hypothesise _≥_ 90% vulnerability overlap and higher exec/sec for the translation path, consistent with RetroWrite [61].

**7. End-to-End Binary-Only Vulnerability Confirmation.** A taint-identified candidate from MOABI’s vectorial analysis could be confirmed as exploitable through the wsolver pipeline (wir_filter + KLEE/IKOS/SeaHorn/SMACK, followed by AFLGo or SymQEMU with formal witness as seed) - all without source access. This would close the loop from bi-

> 2SymQEMU is used here in _standalone_ mode - pure concolic execution without a fuzzing master. The SymQEMU documentation and original evaluation [57] recommend deploying it in _collaborative_ mode: AFL++ as master generating seeds at high throughput, with SymQEMU as slave solving constraints that AFL++ cannot. This hybrid configuration would likely reduce the 1,530 s time-to-first-CVE significantly. Our standalone deployment represents a conservative lower bound on SymQEMU’s performance in binary-only PSIRT workflows; a properly configured AFL++/SymQEMU ensemble would be expected to outperform both tools individually.

nary format analysis through taint to a concrete PoC, grounded in the methodology of [44, 66].

**8. Whole-System Translation.** Extending translation from userland binaries to complete firmware images (kernel + userspace) via a hybrid approach - translate userspace, emulate kernel via QEMU - would enable full firmware analysis without hardware.

**9. AI-Assisted Translation.** Transformer models trained on binary analysis tasks [67] could augment classical translators for indirect jump target prediction, function boundary detection in stripped binaries, and calling convention inference - addressing the main source of translation failures identified in Section 5.5.

##### 6.9.3 Long-Term (5+ years)

#### **10. Formally Verified Translation**

The long-term goal is proving translation correctness using formal methods (Coq, Isabelle/HOL), following the precedent of CompCert [68], which proves that its C compiler introduces no bugs. Binary translation is harder than compilation: the source binary may be malformed, obfuscated, or exploit undefined behaviour, and its semantics must be discovered rather than taken from a specification. A tractable approach is to restrict the proof to a well-defined subset - well-formed ELF, standard calling conventions, no self-modifying code - prove correctness for that subset, and expand incrementally.

**11. Cross-Architecture Vulnerability Databases**

Current vulnerability signatures are architecture-specific (x86 shellcode byte sequences, ARM-specific ROP gadgets).

35

## Slide 42

A semantic approach would define signatures at the IR level - for example, "a function reads user-controlled input and passes it without bounds checking to strcpy" - making them applicable to ARM, RISC-V, and x86 alike. Binary translation provides the path from binary to LLVM IR, and from IR to semantic signature matching, enabling a single vulnerability knowledge base to serve all architectures in the portfolio.

### **7 Conclusion**

This dissertation investigated binary translation as a pragmatic approach for extending architecture-specific vulnerability analysis tools to arbitrary processor families. Through systematic evaluation of three modern LLVM-based translators (RetDec, Anvill, rev.ng) and one classical translator (UQBT) on 39,364 production Linux binaries spanning five architectures, we provide empirical foundation for tool selection and deployment decisions in security workflows.

**RQ5 - Scale effects:** _Binary size is the dominant factor._ Translation time scales linearly with binary size; large binaries ( _>_ 5 MB) frequently timeout, consistent with known LLVM scalability challenges on large functions. Success rates are stable across distribution versions and optimization levels, but drop significantly for binaries using architecture-specific extensions (SIMD, atomics) not yet modelled by translators.

**RQ6 - Historical comparison:** _Modern tools outperform classical approaches in coverage and maintainability, but UQBT remains a valid semantic reference._ UQBT achieves 67.4% success on sparc32 coreutils with 97% behavioral correctness - demonstrating the long-term feasibility of semanticpreserving translation. Modern LLVM-based tools inherit ecosystem benefits (optimization passes, backends, sanitizer integration) at the cost of LLVM version dependency. The fundamental design trade-off identified by Cifuentes in 1994 remains relevant today.

##### **7.2 Principal Findings**

##### **7.1 Research Questions Answered**

This work addressed six research questions stated in Section 1.5. We answer each explicitly:

**RQ1 - Translation feasibility:** _Yes, feasible._ Modern binary translators achieve 30–95% success rates on real-world production binaries depending on tool-architecture pair. RetDec achieves 79.1% on ARM64, Anvill achieves 94.1% on RISC-V - rates sufficient for practical PSIRT deployment. The translation-based approach is viable for 4 of 5 evaluated architectures.

**RQ2 - Architectural coverage:** _Highly architecturedependent._ ARM64, ARMv7, RISC-V, and s390x are wellsupported through portfolio deployment (66–93% combined coverage). PowerPC64 represents a complete gap: 0% success across all three modern tools (0/8,134 binaries), constituting a critical risk for enterprise, HPC, and financial infrastructure operators.

**RQ3 - Tool complementarity:** _Tools complement, not compete._ Overlap between RetDec and Anvill is only 3.6% of binaries - near-perfect architectural specialization. RetDec dominates ARM, Anvill dominates RISC-V and s390x, rev.ng fills the ARMv7 gap. Portfolio deployment is not merely additive but architecturally necessary.

**RQ4 - Operational viability:** _Conditionally viable, with an important distinction._ Binary translation serves two operationally distinct workflows. For _reactive triage_ (NIS2 24hour notification): RetDec and Anvill ( _∼_ 5 sec/binary) enable SBOM generation and CVE impact assessment across 1,000+ firmware binaries within the deadline. For _proactive discovery_ : taint analysis and fuzzing on translated binaries find unknown vulnerabilities continuously in CI/CD pipelines - not within a 24-hour window, but before attackers find them. rev.ng ( _∼_ 180 sec/binary) is limited to selective deep analysis of high-priority targets in either workflow.

**1. Feasibility Demonstrated.** Binary translation achieves 30–95% success rates on real-world binaries, varying by toolarchitecture pair. This suffices for practical deployment in PSIRT workflows, particularly under regulatory constraints (NIS2 24-hour deadlines, Cyber Resilience Act compliance).

**2. Architectural Complementarity.** Tools exhibit nearperfect non-overlapping specialization rather than redundant competition. RetDec dominates ARM (79.1% ARM64), Anvill dominates RISC-V (94.1%) and s390x (68.1%), rev.ng provides broadest coverage (47.6% overall). Single-tool coverage inadequate; portfolio deployment necessary.

**3. Critical PowerPC64 Gap.** All three modern tools fail completely on PowerPC64 (0/8,134 binaries, 0% success), affecting organizations operating IBM POWER infrastructure in enterprise, HPC, and financial sectors. This gap represents urgent development priority for security tool vendors.

**4. Operational Viability.** Translation speed varies significantly: RetDec/Anvill average 5 seconds per binary (compatible with PSIRT 24-hour deadlines), while rev.ng requires 180 seconds (36 _×_ slower, limiting applicability to selective deep analysis rather than routine batch processing).

**5. Portfolio Strategy.** Two-tool portfolio (RetDec + Anvill) achieves 70.5% coverage with acceptable speed for reactive triage workflows. Three-tool portfolio (adding rev.ng) reaches 93% coverage for proactive deep analysis. Proactive vulnerability discovery via taint analysis and fuzzing operates continuously in CI/CD - complementing, not replacing, the reactive SBOM-based CVE triage workflow.

**6. Failure Modes Addressable.** The dominant failure mode is abnormal process termination - translator crashes and OOM kills - rather than graceful degradation, reflecting the tools’ research prototype origins. Known mitigations exist for the underlying causes: profile-guided translation for indirect control flow, comprehensive relocation support for PIC

36

## Slide 43

binaries, and function-at-a-time translation for large binaries. Incremental improvements could increase success rates by 10–20 percentage points.

##### **7.3 Contributions to Knowledge**

This work advances binary analysis research through:

**Empirical Rigor.** First large-scale evaluation of binary translator quality on 39K+ production binaries across diverse architectures. Prior work evaluated translators on synthetic benchmarks or small custom datasets; we provide realistic PSIRT workload assessment.

**Architectural Complementarity Finding.** Demonstration that modern translators specialize rather than compete contradicts intuition. This finding informs deployment architecture: security architects should deploy multiple tools in portfolio rather than selecting "best" single tool.

**Operational Guidance.** Quantification of translation speed as critical workflow constraint provides decision framework for security operations centers deploying multi-architecture capabilities under regulatory deadlines.

**Gap Documentation.** Identification of complete PowerPC64 support absence across all evaluated tools creates actionable priority for tool developers and highlights risk for organizations dependent on POWER infrastructure.

**Historical Baseline.** Resurrection of UQBT and comparison with modern LLVM-based approaches illuminates tradeoffs between classical (explicit calling conventions, transparent RTL) and modern (LLVM ecosystem access, maintenance burden) designs.

##### **7.4 Practical Recommendations**

**For Security Architects:** Build a translation portfolio rather than relying on a single tool. A two-tool baseline (RetDec + Anvill) achieves 70.5% coverage at high speed; adding rev.ng raises this to 93% for critical binaries. All evaluated translators are open-source and integrate as a preprocessing step ahead of any existing x86-64 binary analysis infrastructure. Implement architecture-aware routing: ARM to RetDec, RISC-V to Anvill, s390x to Anvill, with unknown architectures tried across all three tools sequentially. For PowerPC64 environments, budget for custom tool development or evaluate IR-based alternatives. Validate translation success periodically using functional test suites (coreutils, BusyBox) to detect regressions, and monitor RetDec, Anvill, and rev.ng repositories for architecture support updates, integrating new versions cautiously after testing.

**For Tool Developers:** PowerPC64 support is the highestpriority gap: despite IBM POWER’s declining market share, the installed base in enterprise, financial, and HPC environments is significant and currently has no automated binary analysis path. Profile-guided translation for indirect control flow and comprehensive PIC relocation handling for the major

ELF relocation types (ARM64, RISC-V, s390x) would each materially increase success rates. Function-at-a-time translation with adaptive optimisation levels would address timeout failures on large binaries. Publishing benchmark datasets and automated testing infrastructure would enable reproducible research and catch regressions across versions.

**For Organisations with MOABI-Like Tools:** Binary translation is viable for extending architecture-specific analysis to multiple platforms provided the target architectures have translator success rates above 50% (verifiable against the matrices in Section 5), the workflow tolerates roughly five seconds of translation overhead per binary, and portfolio deployment - multiple tools, moderate operational complexity - is acceptable. The IR-based analysis approach (angr, Ghidra) is preferable when building from scratch with no existing architecture-specific tooling, but translation is the better choice when significant investment already exists in x86-64 analysis infrastructure. A pilot deployment starting with a single non-critical architecture - RISC-V with Anvill’s 94% success rate is the lowest-risk entry point - is recommended before expanding to the full portfolio.

##### **7.5 Limitations and Future Work**

This dissertation measures _translation completeness_ (valid x86-64 ELF output) but not _functional correctness_ (behavioural equivalence) or _vulnerability preservation_ (exploitability retention). In the short term, functional testing on binaries with established test suites (coreutils, BusyBox), PowerPC64 support development in Remill/Anvill, and a profileguided translation prototype represent the most impactful next steps. In the medium term, a systematic vulnerability preservation study using CVE-documented vulnerabilities, whole-system translation extending to kernel and userspace firmware images, and AI-assisted translation using neural networks for indirect jump prediction and function boundary detection would substantially extend the methodology. In the long term, formally verified translation in the style of CompCert and cross-architecture vulnerability signature databases operating on IR rather than byte patterns would elevate binary translation from an empirically validated engineering approach to a theoretically grounded discipline.

##### **7.6 Positioning Against the State of the Art**

The results advance the state of the art in three respects.

_First, evaluation scale and realism._ Prior translation system evaluations measured performance-driven translation on controlled workloads: UQBT on SPEC benchmarks and coreutils [27, 29], FX!32 on Microsoft Office [30, 31]. This is the first evaluation of _security-oriented_ binary translation on production Linux firmware at scale - 39,364 binaries across five architectures and ten distribution releases - providing an empirical foundation calibrated to actual PSIRT workloads

37

## Slide 44

rather than synthetic benchmarks.

_Second, the complementarity principle._ The finding that modern translators specialise rather than compete - with only 3.6% binary-level overlap between the two best-performing tools - is not predicted by any prior taxonomy of binary translation systems. It emerges empirically and suggests a general design principle: the field benefits more from portfolio orchestration infrastructure than from investment in a single universal translator. This reframes the standard tool comparison question from “which translator is best?” to “which portfolio achieves adequate coverage at acceptable operational cost?”

_Third, a documented security infrastructure gap._ The PowerPC64 failure (0/8,134 binaries across all three modern tools) constitutes a quantified blind spot with direct regulatory consequence: organisations operating IBM POWER-based financial infrastructure under DORA [3] cannot currently deploy automated binary taint analysis on their core workloads. Documenting this gap with production-scale evidence is a prerequisite for closing it.

##### **Acknowledgments**

The author thanks Cristina Cifuentes for pioneering work on UQBT and decompilation theory, which established foundations this research builds upon. Thanks to Trail of Bits (Anvill/Remill), Avast (RetDec), and rev.ng Srls for open-sourcing their translators, enabling academic research. Special thanks to Prof. Benjamin Smith (École Polytechnique) for academic supervision of this thesis, and to Prof. Aurélien Francillon for enterprise advisory guidance.

dissertation, situated at the intersection of academic rigour and offensive security practice, may inspire the next generation of reverse engineers to pursue this path - and that universities, spurred by the regulatory imperative, will eventually create the curricula needed to produce them at scale. The craft deserves to be taught, not merely discovered.

##### **Data Availability**

The translated binary dataset (850 MB, 39,364 ELF binaries across five architectures) together with all benchmark scripts and raw results is publicly available on Zenodo [6]: https:// doi.org/10.5281/zenodo.19075909. RetDec, Anvill, and rev.ng source code are available on GitHub (open-source). Resurrected UQBT: DockerHub endrazine/uqbt [47], GitHub endrazine/uqbt [48]. CVE-2023-2804 reproduction kit: [63].

##### **Conflicts of Interest**

Author is CTO of MOABI Solutions, developer of the MOABI binary analysis platform discussed in this work. No financial relationship with RetDec, Anvill, rev.ng, or their parent organizations.

The author is deeply grateful to the following renowned security researchers for their expert review and feedback on his work: Julio Auto, Piotr Bania, Sébastien Bardin, Rodrigo Branco, Sergey Bratus, Dino Dai Zovi, Mark Dowd, Prof. Aurélien Francillon, Travis Goodspeed, Dan Kaminsky, Federico Maggi, Marion Marschalek, Charlie Miller, Alexander Peslyak (Solar Designer), Prof. Benjamin Smith, Ilja van Sprundel, Matthieu Suiche, Chris Valasek, and Michal Zalewski (lcamtuf). Their collective expertise spanning vulnerability research, binary analysis, reverse engineering, and offensive security significantly strengthened this dissertation.

**A note on education and the future of the discipline.** Binary reverse engineering is today among the rarest and most valuable skills in cybersecurity - and yet no university curriculum produces reverse engineers. Every practitioner in this field, including the reviewers of this very dissertation, is entirely self-taught: they learned by doing, by reading Phrack, by spending countless nights disassembling binaries out of curiosity and passion. This is the reason skilled reverse engineers are so scarce, and why the regulatory burden described in this thesis - auditing third-party binaries at supply chain scale - currently cannot be met. Automation, through platforms like MOABI and projects like ASCiDy, is one answer. But the deeper answer is people. The author hopes that this

38

## Slide 45

### **Glossary**

- **ABI** Application Binary Interface. The specification governing how compiled code interacts at the binary level, including calling conventions, register usage, stack layout, and data type sizes. Critical for correct interprocedural taint propagation.

- **AFL++** American Fuzzy Lop plus plus. The leading coverage-guided greybox fuzzer, using LLVM instrumentation to track basic block coverage and an evolutionary algorithm to mutate inputs towards new code paths.

- **binary translation** The process of converting an executable binary from one processor architecture to another, preserving data-flow and control-flow semantics. Distinguished from recompilation (which requires source code) and IR-based analysis (which does not produce executable output).

- **calling convention** The portion of an ABI specifying how function arguments are passed (which registers, which stack positions), where return values are placed, and which registers each side must preserve across calls.

- **CFG** Control Flow Graph. A directed graph whose nodes are basic blocks (maximal sequences of straight-line instructions) and whose edges represent possible control transfers between them.

- **concolic execution** A hybrid analysis technique combining concrete execution (for speed) and symbolic execution (for constraint solving). Executes the program on concrete inputs while maintaining symbolic expressions over those inputs, using an SMT solver to generate new inputs that explore uncovered branches.

- **CRA** EU Cyber Resilience Act (2024). Requires manufacturers of connected products to maintain a Software Bill of Materials, address vulnerabilities within defined timeframes, and demonstrate product security throughout the lifecycle.

- **CVE** Common Vulnerabilities and Exposures. A standardised identifier for publicly disclosed security vulnerabilities, maintained by MITRE and used as the primary reference in PSIRT triage workflows.

- **DAST** Dynamic Application Security Testing. Security analysis performed on a running program, including fuzzing, concolic execution, and taint analysis on executing binaries.

- **DevSecOps** Extension of DevOps that integrates security tooling into CI/CD pipelines, enabling continuous automated security validation on every build.

- **DORA** EU Digital Operational Resilience Act. Mandates ICT resilience requirements for financial sector entities, including incident reporting and third-party risk management.

- **ELF** Executable and Linkable Format. The standard binary format on Linux and Unix systems, comprising a header, program segments, section headers, and symbol tables.

- **FDA** U.S. Food and Drug Administration. Requires cybersecurity evidence in medical device premarket submissions, including Software Bills of Materials.

- **fuzzing** An automated testing technique that generates semirandom inputs and monitors a program for crashes or memory errors. Coverage-guided fuzzing (AFL++, LibFuzzer) uses instrumentation to direct mutation towards unexplored code paths.

- **IR** Intermediate Representation. An abstract, architectureneutral program representation used as the target of binary lifting and the source for code generation. Examples include LLVM IR, VEX, and REIL.

- **ISO/SAE 21434** International standard imposing cybersecurity engineering requirements across the automotive supply chain, from design through production and postproduction.

- **lifting** The first phase of binary translation: converting native machine instructions into a higher-level intermediate representation such as LLVM IR or VEX.

- **LLVM** A compiler infrastructure providing a typed, SSAform intermediate representation (LLVM IR), a suite of optimisation passes, and backends targeting multiple architectures. Used as the output format by RetDec, Anvill, and rev.ng.

- **NIS2** EU Network and Information Security Directive 2 (2022). Mandates security obligations and 24-hour incident notification for operators of essential services across critical infrastructure sectors.

- **PIC** Position-Independent Code. Executable code that can be loaded at any memory address without modification, required for shared libraries and ASLR-enabled binaries. Uses PC-relative addressing, which complicates binary translation.

- **PSIRT** Product Security Incident Response Team. Organisational function responsible for assessing the impact of published vulnerabilities (CVEs) on a company’s products and coordinating remediation.

39

## Slide 46

- **REIL** Reverse Engineering Intermediate Language, designed by Thomas Dullien (Halvar Flake). A minimal IR with only 17 operations, optimised for simplicity of static analysis implementation.

- **SAST** Static Application Security Testing. Security analysis performed on source code or binaries without executing the program, including taint analysis and abstract interpretation.

- **SBOM** Software Bill of Materials. A formal, machinereadable inventory of software components and their dependencies, required by CRA and FDA for supply chain vulnerability management.

- **SCA** Software Composition Analysis. Automated identification of third-party components and their known vulnerabilities, typically via SBOM generation and CVE cross-referencing.

- **SSA** Static Single Assignment form. An IR property where each variable is assigned exactly once. Simplifies dataflow analysis and enables many compiler optimisations. Used by LLVM IR and VEX.

- **SSDLC** Secure Software Development Lifecycle. A development framework integrating security activities (SAST, DAST, SCA, penetration testing) at every stage of the software lifecycle.

- **symbolic execution** A program analysis technique that represents inputs as symbolic variables, collects path constraints at each branch, and uses an SMT solver to generate concrete inputs satisfying specific conditions. Enables systematic path exploration but suffers from path explosion on large programs.

- **taint analysis** A program analysis technique that tracks the propagation of user-controlled data (tainted data) from input sources to potentially dangerous sinks, identifying vulnerabilities such as buffer overflows and format string bugs.

- **TCG** Tiny Code Generator. QEMU’s internal JIT intermediate representation, used by rev.ng as a lifting substrate before translation to LLVM IR.

- **VEX** Valgrind’s intermediate representation, used by angr for cross-architecture symbolic execution and binary analysis. Strongly typed, SSA-form, with approximately 300 operations.

40

## Slide 47

### **References**

- [1] European Parliament and Council of the European Union. Directive (EU) 2022/2555 of the european parliament and of the council on measures for a high common level of cybersecurity across the union (NIS2 directive). Technical Report L 333, Official Journal of the European Union, 2022. https://eur-lex.europa.eu/ legal-content/EN/TXT/?uri=CELEX:32022L2555.

- [2] European Parliament and Council of the European Union. Regulation (EU) 2024/2847 of the european parliament and of the council on horizontal cybersecurity requirements for products with digital elements (cyber resilience act). Technical Report L 2024/2847, Official Journal of the European Union, 2024. https://eur-lex.europa.eu/ legal-content/EN/TXT/?uri=CELEX:32024R2847.

- [3] Regulation (EU) 2022/2554 of the European Parliament and of the Council on digital operational resilience for the financial sector (DORA). Technical Report L 333, Official Journal of the European Union, December 2022. https://eur-lex.europa.eu/ legal-content/EN/TXT/?uri=CELEX:32022R2554.

- [4] International Organization for Standardization and SAE International. Road vehicles — cybersecurity engineering. Technical Report ISO/SAE 21434:2021, ISO/SAE, August 2021. https://www.iso.org/standard/ 70918.html.

- [5] U.S. Food and Drug Administration. Cybersecurity in medical devices: Quality system considerations and content of premarket submissions. Technical report, FDA, 2022.

- [6] Jonathan Brossard. Binary translation dataset: Output data and test scripts. Zenodo. https://doi.org/10. 5281/zenodo.19075909, 2026.

- [7] MOABI Solutions and EURECOM. ASCiDy: Automated software security for connected and industrial systems. PTCC project of the Paris Campus Cyber, piloted by INRIA. https://www.ascidy.fr, October 2025. Funded by INRIA and Campus Cyber. Integrates binary-only dynamic analysis (fuzzing) into the MOABI platform, complementing existing static binary analysis for NIS2/CRA compliance.

- [8] Seth Carmody, Andrea Coravos, Ginny Fahs, Audra Hatch, Janine Medina, Beau Woods, and Joshua Corman. Building resilient medical technology supply chains with a software bill of materials. _npj Digital Medicine_ , 4(1):34, 2021.

- [9] Thomas Dullien and Sebastian Porst. REIL: A platformindependent intermediate representation of disassembled code for static code analysis. In _CanSecWest_ , 2009.

- [10] Nicholas Nethercote and Julian Seward. Valgrind: A framework for heavyweight dynamic binary instrumentation. In _ACM SIGPLAN Conference on Programming Language Design and Implementation (PLDI)_ , pages 89–100. ACM, 2007.

- [11] Chris Lattner and Vikram Adve. LLVM: A compilation framework for lifelong program analysis & transformation. In _IEEE International Symposium on Code Generation and Optimization (CGO)_ , pages 75–86. IEEE, 2004.

- [12] Henry Gordon Rice. Classes of recursively enumerable sets and their decision problems. _Transactions of the American Mathematical Society_ , 74(2):358–366, 1953.

- [13] Barton P Miller, Louis Fredriksen, and Bryan So. An empirical study of the reliability of UNIX utilities. _Communications of the ACM_ , 33(12):32–44, 1990.

- [14] Michal Zalewski. American fuzzy lop. https:// lcamtuf.coredump.cx/afl/, 2016.

- [15] Cristian Cadar, Daniel Dunbar, and Dawson Engler. KLEE: Unassisted and automatic generation of highcoverage tests for complex systems programs. In _USENIX Symposium on Operating Systems Design and Implementation (OSDI)_ , pages 209–224, 2008.

- [16] Patrick Cousot and Radhia Cousot. Abstract interpretation: A unified lattice model for static analysis of programs by construction or approximation of fixpoints. In _Conference Record of the Fourth Annual ACM SIGPLAN-SIGACT Symposium on Principles of Programming Languages (POPL)_ , pages 238–252. ACM, 1977.

- [17] TIS Committee. Tool interface standard (TIS) executable and linking format (ELF) specification version 1.2, 1995.

- [18] Linux Foundation. System V application binary interface — AMD64 architecture processor supplement, draft version 0.95. Technical report, The Linux Foundation, 2008.

- [19] Richard Wartell, Yan Zhou, Kevin W Hamlen, Murat Kantarcioglu, and Bhavani Thuraisingham. Differentiating code from data in x86 binaries. In _European Conference on Machine Learning and Knowledge Discovery in Databases (ECML/PKDD)_ , pages 522–536. Springer, 2011.

41

## Slide 48

- [20] Chengbin Pang, Ruotong Yu, Yaohui Chen, Eric Koskinen, Georgios Portokalidis, Bing Mao, and Jun Xu. SoK: All you ever wanted to know about x86/x64 binary disassembly but were afraid to ask. In _Proceedings of the IEEE Symposium on Security and Privacy (S&P)_ , pages 833–851. IEEE, 2021.

- [21] Matt Miller. Understanding Win32 shellcode. Nologin Security Research. http://www.hick.org/code/ skape/papers/win32-shellcode.pdf, 2003. Handle: skape. Foundational reference on shellcode construction, encoding, and obfuscation techniques including overlapping instruction sequences.

- [22] PaX Team. PaX documentation: ASLR, nonexecutable pages, and exploit mitigations. https:// pax.grsecurity.net/docs/, 2003. Handle: pipacs. Seminal work on kernel-level exploit mitigations; documents attacker techniques including control flow manipulation and instruction aliasing used to bypass static analysis.

- [23] Brad Spengler. grsecurity: Exploit prevention and detection. https://grsecurity.net/, 2004. Handle: spender. Documents attacker obfuscation techniques including overlapping instruction sequences used to evade static binary analysis and signature-based detection.

- [24] Stephen Dolan. mov is turing-complete. _Computer Laboratory, University of Cambridge_ , 2013. https: //drwho.virtadpt.net/files/mov.pdf.

- [25] Dennis Andriesse, Xi Chen, Victor van der Veen, Asia Slowinska, and Herbert Bos. An in-depth analysis of disassembly on full-scale x86/x64 binaries. In _25th USENIX Security Symposium (USENIX Security 16)_ , pages 583–600. USENIX Association, 2016.

- [26] Christopher Domas. M/o/Vfuscator: The single instruction C compiler. DEF CON 23. https://github.com/ xoreaxeaxeax/movfuscator, 2015. Compiles arbitrary C programs into exclusively MOV instructions, directly inspired by Dolan [24]. Demonstrates practical obfuscation via semantic density of a single x86 opcode.

- [27] Cristina Cifuentes. _Reverse Compilation Techniques_ . PhD thesis, Queensland University of Technology, 1994.

- [28] Cristina Cifuentes and Mike Van Emmerik. UQBT: Adaptable binary translation at low cost. _IEEE Computer_ , 33(3):60–66, 2000.

- [29] Cristina Cifuentes, Doug Simon, and Antoine Fraboulet. Assembly to high-level language translation. In _IEEE International Conference on Software Maintenance (ICSM)_ . IEEE, 1998.

- [30] Raymond Hookway and Mark A Herdeg. Digital FX!32: Combining emulation and binary translation. _Digital Technical Journal_ , 9(1):3–12, 1997.

- [31] Anton Chernoff et al. FX!32: A profile-directed binary translator. _IEEE Micro_ , 18(2):56–64, 1998.

- [32] Fabrice Bellard. QEMU, a fast and portable dynamic translator. In _USENIX Annual Technical Conference (ATC)_ , pages 41–46, 2005.

- [33] Johannes Müller et al. GDSL: Generic decoder specification language. https://github.com/gdslang/ gdsl-toolkit, 2013.

- [34] Nicholas Nethercote and Julian Seward. How to shadow every byte of memory used by a program. In _ACM International Conference on Virtual Execution Environments (VEE)_ . ACM, 2007.

- [35] Fish Wang and Yan Shoshitaishvili. angr – a binary analysis platform. In _Black Hat USA_ , 2017.

- [36] Cristina Cifuentes and K. John Gough. Decompilation of binary programs. _Software: Practice and Experience_ , 25(7):811–829, 1995.

- [37] Cristina Cifuentes. Structuring decompiled graphs. In _International Conference on Compiler Construction (CC)_ , pages 91–105. Springer, 1996.

- [38] Valentin J M Manès, HyungSeok Han, Choongwoo Han, Sang Kil Cha, Manuel Egele, Edward J Schwartz, and Maverick Woo. The art, science, and engineering of fuzzing: A survey. _IEEE Transactions on Software Engineering_ , 47(11):2312–2331, 2019.

- [39] Marcel Böhme, Van-Thuan Pham, and Abhik Roychoudhury. Coverage-based greybox fuzzing as Markov chain. In _ACM Conference on Computer and Communications Security (CCS)_ , pages 1032–1043. ACM, 2017.

- [40] Sebastian Poeplau and Aurélien Francillon. Symbolic execution with SymCC: Don’t interpret, compile! In _USENIX Security Symposium_ , pages 181–198, 2020.

- [41] David Brumley, Ivan Jager, Thanassis Avgerinos, and Edward J. Schwartz. BAP: A binary analysis platform. In _Proceedings of the International Conference on Computer Aided Verification (CAV)_ , pages 463–469. Springer, 2011.

- [42] Jakub Kvrtek, Peter Matula, and Petr Zemek. RetDec: An open-source machine-code decompiler. In _Proceedings of the Federated Conference on Computer Science and Information Systems (FedCSIS)_ . IEEE, 2017. Open-source release: https://github.com/avast/ retdec.

42

## Slide 49

- [43] Artem Dinaburg and Andrew Ruef. Remill: A static binary translator. In _Proceedings of the ACM SIGPLAN/SIGOPS International Conference on Virtual Execution Environments (VEE)_ , 2014. Anvill built on Remill: https://github.com/lifting-bits/ anvill.

- [44] Jonathan Brossard. Unstripping cloud container ELF binaries. In _2025 International Conference on Emerging Technologies and Computing (IC_ETC)_ , pages 1–6. IEEE, 2025.

- [45] Jonathan Brossard. .eh_frame prevalence dataset (Debian/Ubuntu). Zenodo. https://doi.org/10.5281/ zenodo.19322637, 2026.

- [46] Alessandro Di Federico, Mathias Payer, and Giovanni Agosta. rev.ng: A unified binary analysis framework to recover CFGs and function boundaries. In _Proceedings of the International Conference on Compiler Construction (CC)_ . ACM, 2017.

- [47] Jonathan Brossard. endrazine/uqbt: Dockerized UQBT for sparc32 _↔_ i386 binary translation. DockerHub. https://hub.docker.com/r/endrazine/uqbt, 2024. Resurrection and modernisation of the University of Queensland Binary Translator (UQBT, 1990s): migrated from Autoconf to CMake, GCC 2.95 to GCC 11 compatibility, containerised for reproducibility.

- [48] Jonathan Brossard. endrazine/uqbt: Modernised UQBT source code. GitHub. https://github.com/ endrazine/uqbt, 2024. Source code for the resurrected and modernised University of Queensland Binary Translator, including build system migration and GCC 11 compatibility fixes.

- [49] Pier Giorgio Chiara. The cyber resilience act: the EU commission’s proposal for a horizontal regulation on cybersecurity for products with digital elements. _International Cybersecurity Law Review_ , 3(2):255–272, 2022.

- [50] National Telecommunications and Information Administration (NTIA). The minimum elements for a software bill of materials (SBOM). Technical report, U.S. Department of Commerce, July 2021.

- [51] Nusrat Zahan, Elizabeth Lin, Mahzabin Tamanna, William Enck, and Laurie Williams. Software bills of materials are required. are we there yet? _IEEE Security & Privacy_ , 21(2):82–88, 2023.

- [52] Amas Phillips, Carsten Maple, Florian Lukavsky, Ian Pearson, Michael Richardson, Nigel Hanson, Paul Kearney, and Robert Dobson. Software bills of materials for IoT and OT devices. _IoT Security Foundation_ , 2023.

- [53] Gary McGraw. Software security. _IEEE Security & Privacy_ , 2(2):80–83, 2004.

- [54] Gary McGraw, Sammy Migues, and Jacob West. _BSIMM: Building Security In Maturity Model_ . Synopsys, 14th edition, 2023. https://www.bsimm.com.

- [55] OWASP Foundation. OWASP software assurance maturity model (SAMM) v2.0. https://owaspsamm.org/, 2020. Open framework for measuring and improving software security practices.

- [56] Fabiola Moyon, Daniel Méndez, Kristian Beckers, Sebastian Klepper, and Jürgen Picht. How to integrate security compliance requirements in agile software development? In _International Conference on Product-Focused Software Process Improvement (PROFES)_ , pages 69–87. Springer, 2020.

- [57] Sebastian Poeplau and Aurélien Francillon. SymQEMU: Compilation-based symbolic execution for binaries. In _Proceedings of the 2021 Network and Distributed System Security Symposium (NDSS)_ . Internet Society, 2021.

- [58] JongHyup Lee, Thanassis Avgerinos, and David Brumley. TIE: Principled reverse engineering of types in binary programs. In _Network and Distributed System Security Symposium (NDSS)_ , 2011.

- [59] Matthew Howard. Recovering type information from binaries. Master’s thesis, University of Cambridge, 2017.

- [60] Claes Wohlin, Per Runeson, Martin Höst, Magnus C. Ohlsson, Björn Regnell, and Anders Wesslén. _Experimentation in Software Engineering: An Introduction_ . Kluwer Academic Publishers, Norwell, MA, 2000.

- [61] Sushant Dinesh, Nathan Burow, Dongyan Xu, and Mathias Payer. RetroWrite: Statically instrumenting COTS binaries for fuzzing and sanitization. In _Proceedings of the 2020 IEEE Symposium on Security and Privacy (S&P)_ , pages 1497–1511. IEEE, 2020.

- [62] Jonathan Brossard. Witchcraft solver: Binary-only vulnerability assessment. GitHub, 2026.

- [63] Jonathan Brossard. CVE-2023-2804 fuzzers and replicators. Zenodo. https://doi.org/10.5281/zenodo. 19136269, 2026.

- [64] Andrea Fioraldi, Dominik Maier, Heiko Eißfeldt, and Marc Heuse. AFL++: Combining incremental steps of fuzzing research. In _14th USENIX Workshop on Offensive Technologies (WOOT 20)_ . USENIX Association, 2020.

- [65] Marcel Böhme, Van-Thuan Pham, Manh-Dung Nguyen, and Abhik Roychoudhury. Directed greybox fuzzing. In

43

## Slide 50

_Proceedings of the 2017 ACM SIGSAC Conference on Computer and Communications Security (CCS)_ , pages 2329–2344. ACM, 2017.

- [66] Jonathan Brossard. Introduction to procedural debugging through binary libification. In _18th USENIX WOOT Conference on Offensive Technologies (WOOT 24)_ , pages 17–25, Philadelphia, PA, August 2024. USENIX Association.

- [67] Kexin Chen et al. TREX: Learning execution semantics from micro-traces for binary similarity. _arXiv preprint arXiv:2012.08680_ , 2020.

- [68] Xavier Leroy. Formal verification of a realistic compiler. _Communications of the ACM_ , 52(7):107–115, 2009.

- [69] Corrado Böhm and Giuseppe Jacopini. Flow diagrams, Turing machines and languages with only two formation rules. _Communications of the ACM_ , 9(5):366–371, May 1966.

- [70] Frances E. Allen. Control flow analysis. _ACM SIGPLAN Notices_ , 5(7):1–19, 1970.

- [71] Edsger W Dijkstra. Go to statement considered harmful. _Communications of the ACM_ , 11(3):147–148, 1968.

- [72] Donald E Knuth. Structured programming with go to statements. _ACM Computing Surveys_ , 6(4):261–301, 1974.

44

## Slide 51

### **A Appendix: Control Flow Structuring - Detailed Reference**

This appendix provides the full treatment of Cifuentes’ control flow structuring theory [27, 37], summarised in Section 3.4.2 of the main text. It includes the seven fundamental CFG patterns with diagrams, the structuring algorithm, and a discussion of irreducible control flow and the goto debate.

condition
T F
then else
after

Figure 3: CFG pattern for _if-then-else_ structure.

The Seven Fundamental Structures

Drawing on compiler theory going back to Böhm and Ja1 copini [69] and Allen [70], Cifuentes formalised seven con2 trol flow patterns covering most compiler-generated code for 3 application to decompilation: 45

if (condition) {
then_clause;
} else {
else_clause;
}

##### Structure 1: If-Then

Structure 3: While Loop (Pre-Test)

#### **Pattern:**

1 test condition
2 je .after 1
3 ; then clause 2
4 .after: 3
4
CFG: 5
6
condition
T F
then after

Figure 2: CFG pattern for _if-then_ structure.

**Recognition:** Node with two successors where one edge bypasses a block.

#### **High-level reconstruction:**

1 if (condition) { 2 then_clause; 3 }

1 2 3

##### Structure 2: If-Then-Else

#### **Pattern:**

.loop:
test condition
je .exit
; body
jmp .loop
.exit:
CFG:
header
T F back
body exit

Figure 4: CFG pattern for _while_ loop (pre-test).

**Recognition:** Back-edge (edge whose target dominates source). Header has two successors: body (loop continues) and exit.

#### **High-level reconstruction:**

while (condition) { body; }

#### **Pattern:**

1 test condition 2 je .else 3 ; then clause 4 jmp .endif 1 5 .else: 2 6 ; else clause 3 7 .endif: 4

#### **CFG:**

**Recognition:** Node with two successors, both leading to common post-dominator.

**High-level reconstruction:**

Structure 4: Repeat-Until (Post-Test)

#### **Pattern:**

.loop: ; body test condition jne .loop

#### **CFG:**

**Recognition:** Back-edge where source is condition, target is body (body executes before test). **High-level reconstruction:**

45

## Slide 52

body
T
test
F
exit

Figure 5: CFG pattern for _repeat-until_ loop (post-test).

selector
c0 c1 c2 default
after

Figure 7: CFG pattern for _switch/case_ structure (multi-way branch).

1 do {
2 body;
3 } while (condition);

**Recognition:** Node with many successors (5+), typically via computed jump. **High-level reconstruction:**

1 switch (selector) {
2 case 0: ...
3 case 1: ...
4 case 2: ...
5 default: ...
6 }

Structure 5: Endless Loop with Break

#### **Pattern:**

1 .loop:
2 ; body
3 test exit_condition
4 je .exit
5 ; more body
6 jmp .loop
7 .exit:

Structure 7: Sequential (Straight-Line)

#### **Pattern:**

**CFG:**

instr1 instr2 instr3

1
2
body1 3
back cont break
body2 exit

**CFG:** Chain of basic blocks with single predecessor/suc-

cessor.

**High-level reconstruction:** Sequential statements.

**Semantic equivalences and information loss.** Cifuentes notes two important equivalences that reflect fundamental information loss during compilation. First, switch/case statements are semantically equivalent to a chain of if/else if statements - at the CFG level, both are simply a node with _N_ successors. A decompiler that fails to recognise the jump table pattern will correctly output if/else if chains, which are semantically correct but less readable. Second, while and for loops are strictly equivalent at the binary level: for (init; cond; incr) desugars to init; while (cond) { body; incr } and both produce an identical pre-test loop CFG pattern. Once compiled, the distinction is unrecoverable - which is why decompilers universally output while loops regardless of the original source. These equivalences reduce the seven patterns to fewer than seven semantically distinct structures, and illustrate a general principle: compilation is a lossy transformation, and decompilation can only recover the semantics, not the original programmer intent.

Figure 6: CFG pattern for endless loop with mid-body break.

**Recognition:** Loop with mid-body exit. **High-level reconstruction:**

1 while (true) { 2 body1; 3 if (exit_condition) break; 4 body2; 5 }

Structure 6: Switch/Case (Jump Table)

#### **Pattern:**

1 mov eax, [selector]
2 cmp eax, MAX_CASE
3 ja .default
4 jmp [table + eax*4] /* Indirect jump via table */
5
6 .case0: ; ...
7 .case1: ; ...
8 .case2: ; ...
9 .default: ; ...

##### Structuring Algorithm

Given CFG _G_ = ( _V, E_ ), Cifuentes’ algorithm identifies control structures via graph pattern matching combined with

**CFG:**

46

## Slide 53

dominance analysis.

#### **Dominance relationships:**

**Definition 5** (Dominance) **.** _Node d_ **_dominates_** _node n (written d domn) if every path from entry to n passes through d._

**Definition 6** (Immediate Dominator) **.** _Node d is the_ **_immediate dominator_** _of n (written d_ = _idom_ ( _n_ ) _) if d dominates n and no other dominator of n dominates d._

**Definition 7** (Post-Dominance) **.** _Node p_ **_post-dominates_** _node n if every path from n to exit passes through p._

#### **Back-edges and loops:**

**Definition 8** (Back-Edge) **.** _Edge_ ( _n, h_ ) _is a_ **_back-edge_** _if h dominates n (target dominates source)._

Back-edges identify loops: ( _n, h_ ) is back-edge _⇒_ loop with header _h_ , tail _n_ . **Natural loops:**

**Definition 9** (Natural Loop) **.** _For back-edge_ ( _n, h_ ) _, the_ **_natural loop_** _is the smallest set L such that:_

- _h ∈ L (header in loop)_

- _n ∈ L (tail in loop)_

- _For all m ∈ L \{h}, all predecessors of m are in L_

Algorithmically: Start with _{h, n}_ , add predecessors of _n_ recursively until reaching _h_ . **Structuring Algorithm (high-level): Example: Structuring a While Loop Input CFG:** 1 BB1: entry 2 _→_ BB2 3 4 BB2: loop header 5 test condition 6 _→_ BB3 (true), BB5 (false) 7 8 BB3: loop body 9 ... 10 _→_ BB4 11 12 BB4: loop continue 13 _→_ BB2 (back-edge) 14 15 BB5: loop exit 16 _→_ BB6

#### **Algorithm 8 Control Flow Structuring**

**Input:** CFG _G_ = ( _V, E_ ), entry node _entry_ **Output:** Structured program representation Compute dominance tree Compute post-dominance tree Identify back-edges (natural loops) **for** each loop (back-edge ( _n, h_ )) **do** Classify loop type: **if** _h_ has two successors (loop body, loop exit) **then while-loop** (pre-test) **else if** _n_ has two successors (loop body, loop exit) **then repeat-until** (post-test) **else endless loop with break end if** Extract loop body (natural loop minus header) Recursively structure loop body Replace loop with single node in outer CFG **end for for** each node _v_ with multiple successors **do if** _v_ has 2 successors **then** Find immediate post-dominator _p_ of _v_ **if** Both successors lead to _p_ **then if-then-else else if** One successor is _p_ **then if-then end if** Extract branches, recursively structure Replace with structured conditional **else if** _v_ has _>_ 5 successors **then** Check for switch pattern (computed jump, case table) **if** switch pattern detected **then switch statement** Extract cases, recursively structure each **end if end if end for** Remaining nodes: sequential statements **return** Structured representation

Check for switch pattern (computed jump, case table) **if** switch pattern detected **then**

**Analysis:**

- Back-edge: ( _BB_ 4 _, BB_ 2) identifies loop

- Natural loop: _{BB_ 2 _, BB_ 3 _, BB_ 4 _}_

- BB2 dominates all loop nodes

- BB2 has two successors: BB3 (loop body), BB5 (exit)

47

## Slide 54

• Pattern: while-loop (pre-test)

#### **Output:**

- 1 while (BB2_condition) { 2 BB3_body; 3 BB4_continue; 4 } 5 BB5_exit;

Irreducible Control Flow

Some CFGs cannot be represented without goto:

**Definition 10** (Irreducible CFG) **.** _A CFG is_ **_irreducible_** _if it contains a loop with multiple entry points (nodes where control enters loop from outside)._

#### **Example: Irreducible loop with two entries**

- 1 if (c1) goto L2; 2 L1: statement1; 3 if (c2) goto L3; 4 goto L1; 5 L2: statement2; 6 if (c3) goto L1; 7 L3: exit;

**CFG:**

back
entry
L1 L2 ← 2 entries
back
L3

Figure 8: Irreducible CFG: loop body _{L_ 1 _, L_ 2 _}_ has two entry points, requiring goto for reconstruction.

Loop body is _{L_ 1 _, L_ 2 _}_ but has two entry points (from entry node). No structured construct represents this - requires goto. **Occurrence in practice:**

1. **Compiler-generated:** Rare. Most compilers generate reducible CFGs. Exception: Duff’s device (intentional loop/switch overlap), computed gotos in interpreter dispatch loops.

2. **Hand-written assembly:** Common in OS kernels, device drivers, performance-critical code where programmer manually optimizes control flow.

3. **Malware obfuscation:** Deliberate. Obfuscators create irreducible graphs to break decompilers and analysis tools.

**Handling irreducibility:**

**Strategy 1: Node splitting.** Duplicate problematic node, make each copy have one entry. Transforms irreducible _→_ reducible, but code duplication may exponentially increase size.

**Strategy 2: Accept goto.** Generate structured code for reducible portions, emit goto for irreducible parts. Practical compilers (GCC, Clang) do this when compiling asm-to-C or decompiling.

**Strategy 3: Fail gracefully.** Report "cannot structure" and fall back to flat control flow representation (all branches explicit). Binary translators often do this - emit LLVM indirectbr with complete block list rather than attempting structuring.

The Goto Debate: A Reverse Engineering Perspective

Edsger Dijkstra’s 1968 letter "Go To Statement Considered Harmful" [71] argued structured programming (if/while/for) produces more maintainable, provably-correct code than gotoladen spaghetti code. Dijkstra’s argument: goto makes reasoning about program state difficult - at any goto target, which invariants hold?

Donald Knuth’s 1974 response "Structured Programming with go to Statements" [72] acknowledged structured programming’s value but defended goto for:

1. Error handling (centralized cleanup: goto cleanup in C)

2. Loop exits (multi-level break)

3. Performance optimization (tail calls, loop fusion)

**Reverse engineering perspective:** This debate assumes we’re _writing_ code. Binary analysis deals with code already written - as machine instructions.

**Key insight:** At assembly level, _everything is goto_ . Conditional branches (je, bne, ARM beq) and unconditional jumps (jmp, b) are the only control flow primitives. Loops, ifstatements, switch-cases - these are _semantic interpretations_ we retroactively impose on branch patterns through pattern matching.

Cifuentes’ structuring algorithm is essentially sophisticated pattern matching on goto graphs to recover high-level programmer intent. When patterns don’t match (irreducible graphs, obfuscated code), we must accept that:

1. Original code was fundamentally goto-based (handoptimized assembly), OR

2. Original structure deliberately obscured (malware obfuscation)

**Implication for binary translation:** Translators must preserve control flow fidelity even when it doesn’t correspond to clean high-level structures. A translator assuming wellbehaved compiler output fails on:

48

## Slide 55

- **Hand-written assembly:** Crypto libraries (OpenSSL’s AES, Bitcoin’s secp256k1), OS kernels (context switch paths, interrupt handlers), JIT compilers (V8, SpiderMonkey dispatch)

- **Highly optimized code:** GCC -O3/-Ofast, LLVM -O3, Intel ICC -fast produce control flow optimizations: loop unrolling, tail recursion elimination, jump threading, computed gotos in switch dispatch

- **Obfuscated malware:** Overlapping instructions (jump

into middle of instruction, decode differently), opaque predicates ( _x_<sup>2</sup> _≥_ 0 always true, but pattern matcher thinks branch conditional), control flow flattening (all blocks in giant switch)

**Translation strategy:** Modern tools (RetDec, Anvill, rev.ng) attempt structuring for optimization but fall back to flat representation when necessary. LLVM’s switch/indirectbr handle complex control flow without requiring full structuring.

49
