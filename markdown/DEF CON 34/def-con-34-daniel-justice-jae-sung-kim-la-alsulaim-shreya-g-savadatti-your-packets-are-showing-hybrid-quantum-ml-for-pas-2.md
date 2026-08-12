---
title: "Your Packets Are Showing Hybrid Quantum ML for Passive OS Fingerprinting"
speakers: ["Daniel Justice", "Jae Sung Kim", "La Alsulaim", "Shreya G Savadatti"]
conference: "DEF CON"
conference_full: "DEF CON 34"
edition: "34"
year: null
source_pdf: "DEF CON 34/DEF CON 34 - Daniel Justice, Jae Sung Kim, La Alsulaim, Shreya G Savadatti - Your Packets Are Showing Hybrid Quantum ML for Passive OS Fingerprinting.pdf"
pages: 19
sha256: "f87212367502a3d01b64af69f64fc45fed8f5ca84ff90501300cb2b7e6b48453"
text_chars: 8565
ocr_pages: 0
has_ocr: false
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2"
converted_at: "2026-08-12T00:15:24Z"
---
# Your Packets Are Showing Hybrid Quantum ML for Passive OS Fingerprinting

**Speakers:** Daniel Justice, Jae Sung Kim, La Alsulaim, Shreya G Savadatti  
**Conference:** DEF CON 34  
**Source:** `DEF CON 34/DEF CON 34 - Daniel Justice, Jae Sung Kim, La Alsulaim, Shreya G Savadatti - Your Packets Are Showing Hybrid Quantum ML for Passive OS Fingerprinting.pdf` (19 pages)

## Slide 1

###### **DEF CON 34**

# **Your Packets Are Showing**

**Hybrid Quantum ML for Passive OS Fingerprinting**

**Jae Sung Kim   ·   La Alsulaim   ·   Shreya G Savadatti   ·   Daniel Justice**

**OsirisML  ·  Virginia Tech  ·  Carnegie Mellon University  ·  University of Pittsburgh**

**01**

## Slide 2

###### **THE QUANTUM CYBERSECURITY CONVERSATION HAS TWO SETTINGS:**

## **Breaking encryption and hardening against quantum.**

**This talk expands it: applying quantum machine learning to security problems beyond cryptography, today**

02

## Slide 3

**WHAT WE BUILT, WHAT WE PROVED**

### **Core thesis**

###### **WHAT**

**A 20-qubit variational quantum classifier (VQC) as a drop-in replacement for OsirisML’s XGBoost classifier.**

###### **HOW**

**Hybrid quantum–classical pipeline on identical nPrint-binarized features and an identical 80/20 train/test split.**

###### **RESULT**

**0.348 weighted F1 vs XGBoost’s 0.361  ·  42.9% accuracy vs 45.85%  —  with 1,228 trainable continuous parameters vs 33,436 leaf values in the XGBoost ensemble.**

**CLAIM**

**Real cybersecurity workloads can be mapped onto quantum compute today.**

**03**

## Slide 4

**THE PROBLEM SPACE**

**Passive OS fingerprinting Identify a remote host’s OS from its network traffic — no probes sent, invisible to the target.**

**TCP/IP stacks leak OS identity:**

**TTL initial values**

**TCP window sizes**

**Options ordering**

**Data-offset bits**

**ipv4_ttl_1 is the single highest-MI feature in the whole capture (MI = 0.63).**

**04**

## Slide 5

###### **WHAT WE COMPARE AGAINST**

### **The classical baseline: OsirisML / XGBoost**

**Raw PCAP**

**network capture**

**nPrint 960 bits / packet (480 IPv4 + 480 TCP)**

**Column removal drop 178 leakage cols → 783 features**

**XGBoost gradient-boosted trees 1,200 trees · 33,436 leaves**

###### **Apples-to-apples benchmark**

**Same 20 features, same split → 45.85% accuracy, 0.361 F1  — not the 0.9751 headline from the full 783-feature configuration.**

**05**

## Slide 6

**SAME SLOT IN THE PIPELINE, DIFFERENT ENGINE**

### **Drop-in quantum replacement**

SHARED, UNCHANGED
Raw PCAP nPrint Preprocess Feature select
XGBoost Hybrid QML
classical tree ensemble 20-qubit VQC + classical head
OUT IN

**No changes to capture, preprocessing, labels, or inference-time integration.**

**06**

## Slide 7

**ARCHITECTURE**

### **The quantum circuit: 20-qubit VQC**

**Angle encoding Entanglement 4 variational layers Measurement RY(xᵢ·π) — 20 gates 19-CNOT linear chain RY+RZ per qubit + CNOT Pauli-Z → 20 values in [−1,+1]**

**275 gates per sample  ·  20 encoding + 19 CNOT + 4×59 variational   ·   160 trainable rotation angles**

**09**

## Slide 8

###### **HOW A HEADER FIELD BECOMES QUBITS**

### **Loading a packet into quantum state**

**We never hand the circuit the number 128. We hand it the number’s binary digits — one qubit each.**

###### **1 · One field → bits → qubits**

###### **2 · Two qubits → one of four neighborhoods**

###### **3 · The full 20-wire map**

**Three header fields, twenty qubits, no single qubit knows a whole field.**

**07**

## Slide 9

###### **WHAT ACTUALLY CROSSES THE QUANTUM BOUNDARY**

### **One real packet through the circuit**

**IN: 20 header bits, straight off the wire**

**QUANTUM CIRCUIT 0 1 1 0 1 0 0 0 0 1 160 trainable knobs 0 1 1 0 1 0 0 0 0 0 entangled, reads bit COMBINATIONS, not single bits**

**real macOS packet · CIC-IDS 2017**

**q0 · ipv4_ttl_0 = 0 Trees split one bit at a time. Entanglement reads joint patterns q1 · ipv4_ttl_1 = 1 q9 · tcp_opt_34 = 1**

**Bit → qubit. No floats, no normalization.**

**The TTL story, now visible coming out of the circuit Qubit 0 carries ipv4_ttl_0 — Linux 64 vs Windows 128. Its output flips sign between classes: macOS −0.81, Windows +0.77. Same circuit, same knobs; the OS is written in the measurement.**

**OUT: 20 floats in [−1, +1]**

**a learned fingerprint of the whole packet**

**08**

## Slide 10

###### **QUANTUM CIRCUIT + CLASSICAL HEAD**

### **Hybrid architecture: full model**

**20 binary features Quantum circuit (160 angles)**

**Integration PennyLane’s qml.qnn.TorchLayer wraps the circuit as an nn.Module; a single Adam optimizer trains quantum angles and classical weights jointly.**

**20 Pauli-Z measurements**

**Classical head Linear 20→32 → ReLU → 32→12 12-class softmax**

**Quantum circuit 160 rotation angles Classical head 1,068 weights + biases**

**1,228 trainable parameters**

**Total**

**10**

## Slide 11

**HOW THE CLASSIFICATION ACTUALLY HAPPENS**

### **From 20 numbers to one OS**

**20 quantum measurements**

**the fingerprint from the quantum circuit**

**32 hidden units**

**13 fired  ·  19 stayed silent each unit checks the whole fingerprint**

**12 class scores**

**scores split by OS family**

**macOS p = 0.999**

✓

**correct**

**real macOS packet · CIC-IDS 2017 row 1434617 · values measured, not illustrative**

**11**

## Slide 12

**SAME 20 FEATURES, SAME 80/20 SPLIT, SAME DATASET**

### **Results: head-to-head**

|**Configuration**|**Accuracy**|**Weighted F1**|**Trainable**
**params**|
|---|---|---|---|
|**Hybrid QML (epoch 13)**|**42.9%**|**0.348**|**1,228**|
|**XGBoost — same 20 features**|**45.85%**|**0.361**|**33,436 leaves**|
|**XGBoost — own top-20 features**|**49.33%**|**0.396**|**49,589 leaves**|

#### **0.013 F1 gap   ·   2.95 accuracy points   ·   27× fewer trainable params**

**12**

## Slide 13

**THE STORY BEHIND THE HEADLINE NUMBER**

### **Where it wins and loses: per-class F1**

**macOS: F1 ≈ 0.86 A distinct TCP/IP stack signature, clean, easy separation.**

**Same-family collapse Windows variants (0.03–0.24) AND Ubuntu variants both confuse within-family (they differ by license or build, not network stack)**

**It’s not a Windows problem, it’s a same-family problem. Distinct stacks separate cleanly; sibling builds don’t.**

**13**

## Slide 14

###### **THE CENTRAL COMPARATIVE FINDING**

### **Parameter efficiency: the information ceiling**

**1,228**

**Hybrid QML trainable continuous parameters**

∼ **27× Fewer than XGBoost’s 33,436 leaf values — counted from the model file**

**28 / 1,024 Leaves XGBoost actually grew per tree — under 3% of the depth-10 budget**

**Both models are sized by the task, not by their budgets.**

**14**

## Slide 15

**WHAT THE TRAINING ARC LOOKED LIKE**

### **Training curve: 13 epochs**

**Collapses aren’t random.**

**They’re reproducible artifacts of inverse-frequency class weighting (15.5 ×) interacting with adjoint-differentiatio n gradient noise.**

**Fix: LR warmup + ReduceLROnPlateau + gradient clipping.**

**15**

## Slide 16

**THE SCALING RESULT**

### **Does it scale? More qubits, more signal**

**The trend is monotonic Weighted F1 climbs 0.12 → 0.19 → 0.28 as qubits go 5 → 10 → 15. More qubits = more input features = a larger Hilbert space — and measurably better classification.**

###### **Read it honestly**

**The sweep (5/10/15) ran balanced with no class weights; the 20-qubit point is the main imbalanced run, shown separately, not as one experiment. Returns diminish and training cost climbs steeply: q15 took 67 GPU-hours.**

**Every sweep point clears the random-chance floor — the circuit is learning, and learning more with scale.**

**16**

## Slide 17

###### **WHAT BOUNDS GENERALIZATION**

### **Limitations**

**1**

##### **Hardware ceiling**

**20-qubit cap from 24 GB VRAM; each qubit doubles the state vector. Noiseless simulator = an upper bound; real NISQ adds decoherence and gate error.**

**2**

##### **Training instability**

**Inverse-frequency weighting + adjoint gradients produce catastrophic collapses. Sequential per-sample circuit evaluation, no gate-level batching.**

**3**

##### **Generalization**

**Binary features use only 2 points on the Bloch sphere per qubit. CIC-IDS 2017 OS mix differs from real enterprise networks.**

**17**

## Slide 18

**WHO BUILT THIS**

### **Team**

JK LA SS DJ
Jae Sung Kim La Alsulaim Shreya G Savadatti Daniel Justice
Independent  Carnegie Mellon  Carnegie Mellon
University of Pittsburgh
Researcher University University

**Direct lineage:  OsirisML was developed by Ekeroth, Neale & Kim at Virginia Tech. This is a quantum extension of our own classical tool.**

**18**

## Slide 19

## **The quantum cybersecurity conversation must expand beyond cryptography.**

- **→ DEF CON–relevant security problems can be mapped onto quantum compute today.**

- **→ We did it for passive OS fingerprinting. The numbers are real. The methodology is reproducible.**

- **→ The path forward: larger circuits, continuous features, real hardware, AND more people trying.**

**Hybrid QML  github.com/JaeSK11/QNNOS**

**CIC-IDS 2017 dataset   ·   PennyLane   · Paper**

**Classical baseline  github.com/OsirisML/OsirisML**

**DEF CON 34**

**19**
