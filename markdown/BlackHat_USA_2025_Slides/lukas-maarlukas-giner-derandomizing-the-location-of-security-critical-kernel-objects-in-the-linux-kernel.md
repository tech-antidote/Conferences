---
title: "Derandomizing the Location of Security-Critical Kernel Objects in the Linux Kernel"
speakers: ["Lukas Maar", "Lukas Giner"]
conference: "Black Hat"
conference_full: "Black Hat USA 2025"
edition: "USA"
year: 2025
source_pdf: "BlackHat_USA_2025_Slides/Lukas Maar&Lukas Giner_Derandomizing the Location of Security-Critical Kernel Objects in the Linux Kernel.pdf"
pages: 165
sha256: "4ab0e085c312cffef9ab82a866dee239b280b97d406ad0564d0dbd5495c78c59"
text_chars: 55885
ocr_pages: 0
has_ocr: false
redacted_secrets: 0
ocr_confidence: null
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2"
converted_at: "2026-08-12T05:16:48Z"
---
# Derandomizing the Location of Security-Critical Kernel Objects in the Linux Kernel

**Speakers:** Lukas Maar, Lukas Giner  
**Conference:** Black Hat USA 2025  
**Source:** `BlackHat_USA_2025_Slides/Lukas Maar&Lukas Giner_Derandomizing the Location of Security-Critical Kernel Objects in the Linux Kernel.pdf` (165 pages)


## Slide 1

S C I E N C E P A S S I O N T E C H N O L O G Y

**Derandomizing the Location of Security-Critical Kernel Objects in the Linux Kernel**

**Lukas Maar Lukas Giner** August 6-7, 2025 Briefings

Daniel Gruss

Stefan Mangard

isec.tugraz.at

## Slide 2

## **About**

### TLB-based location disclosure attacks

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

1

## Slide 3

## **About**

TLB-based location disclosure attacks **Timing side channel:** TLB Evict+Reload

Lukas Maar

Lukas Giner

\```
https://lukasmaar.github.io/
\```

1

## Slide 4

## **About**

TLB-based location disclosure attacks **Timing side channel:** TLB Evict+Reload **Leakage Amplification:** Exploits allocator and defense behavior

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

1

## Slide 5

## **About**

TLB-based location disclosure attacks **Timing side channel:** TLB Evict+Reload **Leakage Amplification:** Exploits allocator and defense behavior **Attack:** Reliable kernel exploitation

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

1

## Slide 6

## **About**

TLB-based location disclosure attacks **Timing side channel:** TLB Evict+Reload **Leakage Amplification:** Exploits allocator and defense behavior **Attack:** Reliable kernel exploitation **Demo:**

Shows leakage and exploitation

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

1

## Slide 7

## **Who Are We?**

### **Lukas Maar**

PhD candidate at Graz University of Technology System Security Kernel Security Side-Channel Security Looking for a job (end 2025)

### **Lukas Giner**

PhD Secure Cache Architectures Microarchitectural Attacks GPU Security Looking for a job (now)

Lukas Maar

Lukas Giner

\```
https://lukasmaar.github.io/
\```

2

## Slide 8

**Motivation**

## Slide 9

## **Prior Kernel Exploitation**

## **Kernel Space** Overwrite some

## **User Space**

Overwrite some
other metadata
./exploit
Control-flow
hijacking attack

attack

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

3

## Slide 10

## **Prior Kernel Exploitation**

## **Kernel Space** Overwrite some

## **User Space**

Overwrite some
other metadata
./exploit
Control-flow
hijacking attack

attack

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

3

## Slide 11

## **Prior Kernel Exploitation**

Kernel Space
Overwrite some
metadata

## **User Space**

Overwrite some
other metadata
./exploit
Control-flow
hijacking attack

attack

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

3

## Slide 12

## **Prior Kernel Exploitation**

## **Kernel Space** Overwrite some

## **User Space**

metadata
Read primitive
1 def information_leak():
Overwrite some 2 return kaddr
other metadata

1 def
Overwrite some 2 return
other metadata
./exploit
Control-flow
hijacking attack

attack

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

3

## Slide 13

## **Prior Kernel Exploitation**

## **Kernel Space** Overwrite some

## **User Space**

metadata
Read primitive
1 def information_leak():
Overwrite some 2 return kaddr
other metadata

1 def
Overwrite some 2 return
other metadata
./exploit
Control-flow
hijacking attack

attack

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

3

## Slide 14

## **Prior Kernel Exploitation**

## **Kernel Space** Overwrite some

## **User Space**

metadata
Read primitive
1 def information_leak():
Overwrite some 2 return kaddr
other metadata

1 def
Overwrite some 2 return
other metadata
./exploit
Control-flow
hijacking attack

attack

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

3

## Slide 15

## **Prior Kernel Exploitation**

User Space Kernel Space
Overwrite some Problem!
metadata
Read primitive
1 def information_leak():
Overwrite some 2 return kaddr
other metadata
Trigger kernel event
./exploit
Control-flow Data-oriented
hijacking attack attack
Privilege escalation

## **User Space**

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

3

## Slide 16

## **Prior Kernel Exploitation**

User Space Kernel Space
Overwrite some Problem!
metadata
Read primitive
1 def information_leak():
Overwrite some 2 return kaddr
other metadata
Write primitive
1 def overwrite(data):
2 *kaddr = data
Trigger kernel event
./exploit
Control-flow Data-oriented
hijacking attack attack
Privilege escalation

## **User Space**

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

3

## Slide 17

## **Prior Kernel Exploitation**

User Space Kernel Space
Overwrite some Problem!
metadata
Read primitive
1 def information_leak():
Overwrite some 2 return kaddr
other metadata
Write primitive
1 def overwrite(data):
2 *kaddr = data
Trigger kernel event
./exploit
Control-flow Data-oriented
hijacking attack attack
Privilege escalation

## **User Space**

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

3

## Slide 18

## **Prior Kernel Exploitation**

User Space Kernel Space
Overwrite some Problem!
metadata
Read primitive
1 def information_leak():
Overwrite some 2 return kaddr
other metadata
Write primitive
1 def overwrite(data):
2 *kaddr = data
Trigger kernel event
./exploit
Control-flow Data-oriented
hijacking attack attack
Privilege escalation

## **User Space**

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

3

## Slide 19

## **Prior Kernel Exploitation**

Kernel Space
Overwrite some Problem!
metadata
Read primitive
1 def information_leak():
Overwrite some 2 return kaddr
other metadata
Write primitive
1 def overwrite(data):
2 *kaddr = data
Trigger kernel event
Control-flow Data-oriented
hijacking attack attack
Privilege escalation

## **User Space**

./exploit

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

3

## Slide 20

## **Prior Kernel Exploitation**

User Space Kernel Space
Overwrite some Problem!
metadata
Read primitive
1 def information_leak():
Overwrite some 2 return kaddr
other metadata
Write primitive
1 def overwrite(data):
2 *kaddr = data
Trigger kernel event
./exploit
Control-flow Data-oriented
hijacking attack attack
Privilege escalation

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

3

## Slide 21

## **Prior Kernel Exploitation**

User Space Kernel Space
Overwrite some Problem!
metadata
Read primitive
1 def information_leak():
Overwrite some 2 return kaddr
other metadata
Write primitive
1 def overwrite(data):
2 *kaddr = data
Trigger kernel event
./exploit
Control-flow Data-oriented
hijacking attack attack
Privilege escalation
Lukas Giner https://lukasmaar.github.io/

Lukas Maar Lukas Giner

3

## Slide 22

## **Prior Kernel Exploitation**

User Space Kernel Space
Overwrite some Problem!
metadata
Read primitive
1 def information_leak():
Overwrite some 2 return kaddr
other metadata
Write primitive
1 def overwrite(data):
2 *kaddr = data
Trigger kernel event
./exploit
Control-flow Data-oriented
hijacking attack attack
Privilege escalation
Lukas Giner https://lukasmaar.github.io/

Lukas Maar Lukas Giner

3

## Slide 23

## **Prior Kernel Exploitation**

User Space Kernel Space
Overwrite some Problem!
metadata
Read primitive
1 def information_leak():
Overwrite some 2 return kaddr
other metadata
Write primitive
1 def overwrite(data):
2 *kaddr = data
Trigger kernel event
./exploit
Control-flow Data-oriented
hijacking attack attack
Privilege escalation
Lukas Giner https://lukasmaar.github.io/

Lukas Maar Lukas Giner

3

## Slide 24

## **Prior Kernel Exploitation**

User Space Kernel Space
Overwrite some Problem!
metadata
Read primitive
1 def information_leak():
Overwrite some 2 return kaddr
other metadata
Write primitive
1 def overwrite(data):
2 *kaddr = data
Trigger kernel event
./exploit
Control-flow Data-oriented
hijacking attack attack
Privilege escalation
Lukas Giner https://lukasmaar.github.io/

Lukas Maar Lukas Giner

3

## Slide 25

## **Prior Kernel Exploitation**

User Space Kernel Space
Overwrite some Problem!
metadata
Read primitive
1 def information_leak():
Overwrite some 2 return kaddr
other metadata
Write primitive
1 def overwrite(data):
2 *kaddr = data
Trigger kernel event
./exploit
Control-flow Data-oriented
hijacking attack attack
Privilege escalation
Lukas Giner https://lukasmaar.github.io/

Lukas Maar Lukas Giner

3

## Slide 26

## **Problem**

**How bad is a failed attempt for kernel exploitation?**

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

4

## Slide 27

## **Problem**

**How bad is a failed attempt for kernel exploitation?** Potential immiate system crash Potential system crash later

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

4

## Slide 28

## **Problem**

**How bad is a failed attempt for kernel exploitation?** Potential immiate system crash Potential system crash later **So, worst case a reboot?**

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

4

## Slide 29

## **Problem**

**How bad is a failed attempt for kernel exploitation?** Potential immiate system crash Potential system crash later **So, worst case a reboot? No, potentially triggers forensic investigation!**

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

4

## Slide 30

## **Problem**

**How bad is a failed attempt for kernel exploitation?** Potential immiate system crash Potential system crash later **So, worst case a reboot? No, potentially triggers forensic investigation!** Undermines stealth Potentially burns zero-day vulnerability

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

4

## Slide 31

## **Magic Wand**

Kernel Space
Overwrite some
metadata
C1:  Where to write?

User Space

C1:  Where to write?
C2:  What to write?
./exploit
GOAL:  Reliable!

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

5

## Slide 32

## **Magic Wand**

## **User Space**

## **Kernel Space** Overwrite some

metadata
C1:  Where to write?
C2:  What to write?
./exploit
GOAL:  Reliable!

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

5

## Slide 33

## **Magic Wand**

User Space Kernel Space
Overwrite some
metadata
C1:  Where to write?
Arbitrary r/w primitive
1 def arb_read(addr):
2 return *addr
3
4 def arb_write(addr, val):
5 *addr = val
C2:  What to writ e?
./exploit
Use arbitrary r/w
GOAL:  Reliable!
Privilege escalation

## **User Space**

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

5

## Slide 34

## **Magic Wand**

User Space Kernel Space
Overwrite some
metadata
C1:  Where to write?
Arbitrary r/w primitive
1 def arb_read(addr):
2 return *addr
3
4 def arb_write(addr, val):
5 *addr = val
C2:  What to writ e?
./exploit
Use arbitrary r/w
GOAL:  Reliable!
Privilege escalation

\```
https://lukasmaar.github.io/
\```

Lukas Maar

Lukas Giner

5

## Slide 35

## **Magic Wand**

User Space Kernel Space
Overwrite some
metadata
C1:  Where to write?
Arbitrary r/w primitive
1 def arb_read(addr):
2 return *addr
3
4 def arb_write(addr, val):
5 *addr = val
C2:  What to writ e?
./exploit
Use arbitrary r/w
GOAL:  Reliable!
Privilege escalation

Lukas Giner

Lukas Maar

\```
https://lukasmaar.github.io/
\```

5

## Slide 36

## **Magic Wand**

User Space Kernel Space
Overwrite some
metadata
C1:  Where to write?
Arbitrary r/w primitive
1 def arb_read(addr):
2 return *addr
3
4 def arb_write(addr, val):
5 *addr = val
C2:  What to writ e?
./exploit
Use arbitrary r/w
GOAL:  Reliable!
Privilege escalation

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

5

## Slide 37

## **Magic Wand**

User Space Kernel Space
Overwrite some
metadata
C1:  Where to write?
Arbitrary r/w primitive
1 def arb_read(addr):
2 return *addr
3
4 def arb_write(addr, val):
5 *addr = val
C2:  What to writ e?
./exploit
Use arbitrary r/w
GOAL:  Reliable!
Privilege escalation

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

5

## Slide 38

2 MB-aligned 4 kB-aligned Location of
C1:  Where to write? memory sections ? slab pages ? Object size aligned ? target objects
C2:  What to write? Self reference ? Arbitrary read/write

## Slide 39

**Address Translation**

**C1:** Where to write?

#### **virtual address:**

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

7

## Slide 40

**Address Translation**

**C1:** Where to write?

virtual address:

9 bit 9 bit 9 bit 9 bit 9 bit 12 bit
pgdi p4di pudi pmdi pti offset

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

7

## Slide 41

**C1:** Where to write?

## **Address Translation**

virtual address:

9 bit 9 bit 9 bit 9 bit 9 bit 12 bit
pgdi p4di pudi pmdi pti offset

CR3
...
PGD

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

7

## Slide 42

**C1:** Where to write?

## **Address Translation**

9 bit 9 bit 9 bit 9 bit 9 bit 12 bit
virtual address: pgdi p4di pudi pmdi pti offset
CR3
pgde
...
PGD

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

7

## Slide 43

**C1:** Where to write?

## **Address Translation**

9 bit 9 bit 9 bit 9 bit 9 bit 12 bit
virtual address: pgdi p4di pudi pmdi pti offset
CR3
pgde
... ...
PGD P4D

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

7

## Slide 44

**C1:** Where to write?

## **Address Translation**

9 bit 9 bit 9 bit 9 bit 9 bit 12 bit
virtual address: pgdi p4di pudi pmdi pti offset
CR3
pgde
p4de
... ...
PGD P4D

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

7

## Slide 45

**C1:** Where to write?

## **Address Translation**

9 bit 9 bit 9 bit 9 bit 9 bit 12 bit
virtual address: pgdi p4di pudi pmdi pti offset
CR3
pgde
p4de
... ... ...
PGD P4D PUD

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

7

## Slide 46

**C1:** Where to write?

## **Address Translation**

9 bit 9 bit 9 bit 9 bit 9 bit 12 bit
virtual address: pgdi p4di pudi pmdi pti offset
CR3
pgde pude
p4de
... ... ...
PGD P4D PUD

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

7

## Slide 47

**C1:** Where to write?

## **Address Translation**

9 bit 9 bit 9 bit 9 bit 9 bit 12 bit
virtual address: pgdi p4di pudi pmdi pti offset
CR3
pgde pude
p4de
... ... ... ...
PGD P4D PUD PMD

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

7

## Slide 48

**C1:** Where to write?

## **Address Translation**

9 bit 9 bit 9 bit 9 bit 9 bit 12 bit
virtual address: pgdi p4di pudi pmdi pti offset
CR3
pgde pude
p4de
pmde
... ... ... ...
PGD P4D PUD PMD

Lukas Maar

Lukas Giner

\```
https://lukasmaar.github.io/
\```

7

## Slide 49

**C1:** Where to write?

## **Address Translation**

9 bit 9 bit 9 bit 9 bit 9 bit 12 bit
virtual address: pgdi p4di pudi pmdi pti offset
CR3
pgde pude
p4de
pmde
... ... ... ... ...
PGD P4D PUD PMD PT

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

7

## Slide 50

**C1:** Where to write?

## **Address Translation**

9 bit 9 bit 9 bit 9 bit 9 bit 12 bit
virtual address: pgdi p4di pudi pmdi pti offset
CR3
pte
pgde pude
p4de
pmde
... ... ... ... ...
PGD P4D PUD PMD PT

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

7

## Slide 51

**C1:** Where to write?

## **Address Translation**

9 bit 9 bit 9 bit 9 bit 9 bit 12 bit
virtual address: pgdi p4di pudi pmdi pti offset
CR3
pte
pgde pude
p4de
pmde
... ... ... ... ... ...
PGD P4D PUD PMD PT Page

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

7

## Slide 52

**C1:** Where to write?

## **Address Translation**

9 bit 9 bit 9 bit 9 bit 9 bit 12 bit
virtual address: pgdi p4di pudi pmdi pti offset
CR3
pte
pgde pude
p4de
pmde
... ... ... ... ... ...
PGD P4D PUD PMD PT Page

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

7

## Slide 53

## **Translation-Lookaside Buffer**

## **C1:** Where to write?

Virtual Address
63 27 20 19 12 11 0
Set Index 2 Set Index 1 Offset

Way 1 Way 2 · · · Way 6
Set 1
...
Tag Phys Tag Phys Tag Phys Tag Phys Set n
...
Set 256

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

8

## Slide 54

## **Translation-Lookaside Buffer**

## **C1:** Where to write?

Virtual Address
63 27 20 19 12 11 0
Set Index 2 Set Index 1 Offset
⊕
Way 1 Way 2 · · · Way 6
Set 1
...
Tag Phys Tag Phys Tag Phys Tag Phys Set n
...
Set 256

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

8

## Slide 55

## **Translation-Lookaside Buffer**

## **C1:** Where to write?

Virtual Address
63 27 20 19 12 11 0
Tag Offset
⊕
Way 1 Way 2 · · · Way 6
Set 1
Tag Compare
...
Tag Phys Tag Phys Tag Phys Tag Phys Set n
Way
...
Set 256

Lukas Giner

Lukas Maar

\```
https://lukasmaar.github.io/
\```

8

## Slide 56

## **Translation-Lookaside Buffer**

## **C1:** Where to write?

Virtual Address
63 27 20 19 12 11 0
Tag Offset
⊕
Way 1 Way 2 · · · Way 6
Set 1
Tag Compare
...
Tag Phys Tag Phys Tag Phys Tag Phys Set n
Way
Way Select ...
Hit?
Physical Address Set 256

Lukas Maar

Lukas Giner

\```
https://lukasmaar.github.io/
\```

8

## Slide 57

## **TLB Timing Side Channel**

## **C1:** Where to write?

Is a page in the TLB?

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

9

## Slide 58

## **TLB Timing Side Channel**

## **C1:** Where to write?

Is a page in the TLB? Measure an access:

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

9

## Slide 59

## **TLB Timing Side Channel**

Is a page in the TLB? Measure an access: `start = time();`

## **C1:** Where to write?

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

9

## Slide 60

## **TLB Timing Side Channel**

Is a page in the TLB? Measure an access: `start = time(); access(test_address);`

## **C1:** Where to write?

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

9

## Slide 61

## **TLB Timing Side Channel**

Is a page in the TLB? Measure an access: `start = time(); access(test_address); time = time() - start;`

## **C1:** Where to write?

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

9

## Slide 62

## **TLB Timing Side Channel**

Is a page in the TLB? Measure an access: `start = time(); access(test_address); time = time() - start;` How to measure kernel pages?

## **C1:** Where to write?

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

9

## Slide 63

## **TLB Timing Side Channel**

Is a page in the TLB? Measure an access: `start = time(); access(test_address); time = time() - start;` How to measure kernel pages? `start = time();`

## **C1:** Where to write?

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

9

## Slide 64

## **TLB Timing Side Channel**

Is a page in the TLB? Measure an access: `start = time(); access(test_address); time = time() - start;` How to measure kernel pages? `start = time(); prefetch(kernel_address);`

## **C1:** Where to write?

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

9

## Slide 65

**C1:** Where to write?

## **TLB Timing Side Channel**

Is a page in the TLB? Measure an access: `start = time(); access(test_address); time = time() - start;` How to measure kernel pages? `start = time(); prefetch(kernel_address); time = time() - start;`

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

9

## Slide 66

## **TLB Timing Histogram**

## **C1:** Where to write?

· 10 5 Kaby lake (i7-8650U)
6 Hit Miss Unmapped
4
2
0
20 25 30 35 40 45 50 55 60 65 70 75 80
Samples

Lukas Maar

Lukas Giner

\```
https://lukasmaar.github.io/
\```

10

## Slide 67

## **TLB Timing Histogram**

## **C1:** Where to write?

· 10 5 Kaby lake (i7-8650U)
6 Hit Miss Unmapped
← mapped unmapped →
4
2
0
20 25 30 35 40 45 50 55 60 65 70 75 80
Samples

Lukas Maar

Lukas Giner

\```
https://lukasmaar.github.io/
\```

10

## Slide 68

## **TLB Timing Histogram**

## **C1:** Where to write?

· 10 5 Kaby lake (i7-8650U)
6 Hit Miss Unmapped
← accessed not accessed → ← mapped unmapped →
4
2
0
20 25 30 35 40 45 50 55 60 65 70 75 80
Samples

Lukas Maar

Lukas Giner

\```
https://lukasmaar.github.io/
\```

10

## Slide 69

**TLB Evict+Reload**

## **C1:** Where to write?

### Attacker

TLB

Kernel

Lukas Maar

Lukas Giner

\```
https://lukasmaar.github.io/
\```

11

## Slide 70

**TLB Evict+Reload**

## **C1:** Where to write?

Attacker

TLB

Kernel

Lukas Maar

Lukas Giner

\```
https://lukasmaar.github.io/
\```

11

## Slide 71

## **TLB Evict+Reload**

Attacker

TLB

## **C1:** Where to write?

Kernel

Lukas Maar

Lukas Giner

\```
https://lukasmaar.github.io/
\```

11

## Slide 72

**TLB Evict+Reload**

## **C1:** Where to write?

Attacker

TLB

Kernel

Lukas Maar

Lukas Giner

\```
https://lukasmaar.github.io/
\```

11

## Slide 73

**TLB Evict+Reload**

**C1:** Where to write?

Attacker TLB
kernel access

Kernel

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

11

## Slide 74

**TLB Evict+Reload**

**C1:** Where to write?

Attacker TLB
kernel access

Kernel

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

11

## Slide 75

**TLB Evict+Reload**

## **C1:** Where to write?

Attacker TLB Kernel
fast  prefetch

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

11

## Slide 76

**TLB Evict+Reload**

**C1:** Where to write?

Attacker TLB Kernel
slow  prefetch

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

11

## Slide 77

**TLB Evict+Reload**

**C1:** Where to write?

Attacker TLB Kernel
slow  prefetch

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

11

## Slide 78

## **TLB Evict+Reload**

Attacker

TLB

## **C1:** Where to write?

Kernel

Lukas Maar

Lukas Giner

\```
https://lukasmaar.github.io/
\```

11

## Slide 79

**C1:** Where to write?

## **TLB Memory Mapping Leakage**

Modules
Code code_base
vmemmap vmemmap_base
vmalloc
used by virtual allocator vmalloc_base
DPM
used by
page and slab allocator page_offset_base
ffff888000000000

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

12

## Slide 80

2 MB-aligned 4 kB-aligned Location of
C1:  Where to write? memory sections ? slab pages ? Object size aligned ? target objects
C2:  What to write? Self reference ? Arbitrary read/write

## Slide 81

**C1:** Where to write?

## **Enforcing 4 kB Memory Mappings**

Modules No Mapping
4kB Mapping
Code
2MB Mapping
vmemmap
vmalloc
used by virtual allocator
DPM
used by
page and slab allocator

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

14

## Slide 82

## **Enforcing 4 kB Memory Mappings**

Modules No Mapping
4kB Mapping
Code
2MB Mapping
vmemmap
vmalloc
used by virtual allocator
DPM
used by
page and slab allocator

## **C1:** Where to write?

Use memory allocated with  vmalloc .
E.g., bytecode for eBPF.

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

14

## Slide 83

## **Enforcing 4 kB Memory Mappings**

## **C1:** Where to write?

Modules No Mapping
4kB Mapping Use memory allocated with  vmalloc .
Code
2MB Mapping
E.g., bytecode for eBPF.
vmemmap Use defenses:
vmalloc
used by virtual allocator
DPM
used by
page and slab allocator

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

14

## Slide 84

## **Enforcing 4 kB Memory Mappings**

## **C1:** Where to write?

Modules No Mapping
4kB Mapping Use memory allocated with  vmalloc .
Code
2MB Mapping
E.g., bytecode for eBPF.
vmemmap Use defenses:
vmalloc
CONFIG_VMAP_STACK :
used by virtual allocator
Stack allocated with  vmalloc .
DPM
used by
page and slab allocator

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

14

## Slide 85

## **Enforcing 4 kB Memory Mappings**

Modules No Mapping
4kB Mapping
Code
2MB Mapping
vmemmap
vmalloc
used by virtual allocator
DPM
used by
page and slab allocator

## **C1:** Where to write?

Use memory allocated with `vmalloc` . E.g., bytecode for eBPF. Use defenses: `CONFIG_VMAP_STACK` : Stack allocated with `vmalloc` . `CONFIG_SLAB_VIRTUAL` : Virtualize heap on 4 kB mappings.

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

14

## Slide 86

## **Enforcing 4 kB Memory Mappings**

Modules No Mapping
4kB Mapping
Code
2MB Mapping
vmemmap
vmalloc
used by virtual allocator
DPM
used by
page and slab allocator

## **C1:** Where to write?

Use memory allocated with `vmalloc` . E.g., bytecode for eBPF. Use defenses: `CONFIG_VMAP_STACK` : Stack allocated with `vmalloc` . `CONFIG_SLAB_VIRTUAL` : Virtualize heap on 4 kB mappings. `CONFIG_STRICT_MODULE_RWX` : Split DPM to 4 kB mappings.

14 Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

## Slide 87

**4 kB Access Primitive**

**C1:** Where to write?

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

15

## Slide 88

**4 kB Access Primitive**

**C1:** Where to write?

Syscalls to load 4 kB-aligned kernel address:

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

15

## Slide 89

**4 kB Access Primitive**

**C1:** Where to write?

Syscalls to load 4 kB-aligned kernel address: Kernel stack:

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

15

## Slide 90

**4 kB Access Primitive**

**C1:** Where to write?

Syscalls to load 4 kB-aligned kernel address: Kernel stack: `syscall(-1)`

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

15

## Slide 91

**4 kB Access Primitive**

**C1:** Where to write?

Syscalls to load 4 kB-aligned kernel address: Kernel stack: `syscall(-1) msg_msg` :

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

15

## Slide 92

**4 kB Access Primitive**

**C1:** Where to write?

Syscalls to load 4 kB-aligned kernel address: Kernel stack: `syscall(-1) msg_msg` : `sys_msgrcv`

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

15

## Slide 93

**4 kB Access Primitive**

**C1:** Where to write?

Syscalls to load 4 kB-aligned kernel address: Kernel stack: `syscall(-1) msg_msg` : `sys_msgrcv pipe_buffer` :

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

15

## Slide 94

**4 kB Access Primitive**

**C1:** Where to write?

Syscalls to load 4 kB-aligned kernel address: Kernel stack: `syscall(-1) msg_msg` : `sys_msgrcv pipe_buffer` : `sys_read`

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

15

## Slide 95

**4 kB Access Primitive**

**C1:** Where to write?

Syscalls to load 4 kB-aligned kernel address: Kernel stack: `syscall(-1) msg_msg` : `sys_msgrcv pipe_buffer` : `sys_read` Page tables:

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

15

## Slide 96

**4 kB Access Primitive**

**C1:** Where to write?

Syscalls to load 4 kB-aligned kernel address: Kernel stack: `syscall(-1) msg_msg` : `sys_msgrcv pipe_buffer` : `sys_read` Page tables: `sys_mprotect` ...

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

15

## Slide 97

**4 kB Access Primitive**

**C1:** Where to write?

Syscalls to load 4 kB-aligned kernel address: Kernel stack: `syscall(-1) msg_msg` : `sys_msgrcv pipe_buffer` : `sys_read` Page tables: `sys_mprotect` ...

Multiple addresses are loaded to the TLB ⌢

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

15

## Slide 98

## **Leaking 4 kB-Aligned Address**

## **C1:** Where to write?

DPM
❻
ipc_ns
❺
queue0
❹
queue1
❸ queue32
❷ msg1
msg0
❶
msg32

sys_msgrcv(id, mtext, mtype):
queue = ipc_ns.root_rt[id]
msg = find_msg(queue, mtype)
copy_to_user(mtext, msg.mtext)
mtext = char[]
mtype = 0x41
// ① access TLB pattern [❷ msg0, , ❺, ❻ queue0, ]  ∩ ipc_ns  ∩
sys_msgrcv(0, mtext, mtype) ①
[❷, ❻]  \
② TLB pattern [❷, ❹[❷, ❻] ]  \  \
// access msg1, queue1, ipc_ns
sys_msgrcv ③ TLB pattern [❶ (1, [❶, ❸, mtext,  ❸, ❻, ❻] ] mtype) ②
// access msg32, queue32, ipc_ns
sys_msgrcv(32, mtext, mtype) ③

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

16

## Slide 99

## **Leaking 4 kB-Aligned Address**

## **C1:** Where to write?

DPM
① TLB pattern sys_msgrcv(id, mtext, mtype):
❻ queue = ipc_ns.root_rt[id]
ipc_ns
msg = find_msg(queue, mtype)
❺ copy_to_user(mtext, msg.mtext)
queue0
mtext = char[]
❹ mtype = 0x41
queue1
❸ queue32 // ① access TLB pattern [❷ msg0, , ❺, ❻ queue0, ]  ∩ ipc_ns  ∩
sys_msgrcv(0, mtext, mtype) ①
[❷, ❻]  \
❷ msg1 // ② access TLB pattern [❷ msg1, , ❹[❷, ❻ queue1, ] ]  \ ipc_ns  \
msg0 sys_msgrcv(1, [❶, mtext,  ❸, ❻] mtype) ②
❶ ③ TLB pattern [❶, ❸, ❻]
msg32 // access msg32, queue32, ipc_ns
sys_msgrcv(32, mtext, mtype) ③

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

16

## Slide 100

## **Leaking 4 kB-Aligned Address**

## **C1:** Where to write?

DPM
① TLB pattern sys_msgrcv(id, mtext, mtype):
❻ queue = ipc_ns.root_rt[id]
ipc_ns
msg = find_msg(queue, mtype)
❺ copy_to_user(mtext, msg.mtext)
queue0
mtext = char[]
❹ mtype = 0x41
queue1
❸ queue32 // ① access TLB pattern [❷ msg0, , ❺, ❻ queue0, ]  ∩ ipc_ns  ∩
sys_msgrcv(0, mtext, mtype) ①
[❷, ❻]  \
❷ msg1 // ② access TLB pattern [❷ msg1, , ❹[❷, ❻ queue1, ] ]  \ ipc_ns  \
msg0 sys_msgrcv(1, [❶, mtext,  ❸, ❻] mtype) ②
❶ ③ TLB pattern [❶, ❸, ❻]
msg32 // access msg32, queue32, ipc_ns
sys_msgrcv(32, mtext, mtype) ③

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

16

## Slide 101

## **Leaking 4 kB-Aligned Address**

## **C1:** Where to write?

DPM
① TLB pattern sys_msgrcv(id, mtext, mtype):
❻ queue = ipc_ns.root_rt[id]
ipc_ns
msg = find_msg(queue, mtype)
❺ copy_to_user(mtext, msg.mtext)
queue0
mtext = char[]
❹ mtype = 0x41
queue1
❸ queue32 // ① access TLB pattern [❷ msg0, , ❺, ❻ queue0, ]  ∩ ipc_ns  ∩
sys_msgrcv(0, mtext, mtype) ①
[❷, ❻]  \
❷ msg1 // ② access TLB pattern [❷ msg1, , ❹[❷, ❻ queue1, ] ]  \ ipc_ns  \
msg0 sys_msgrcv(1, [❶, mtext,  ❸, ❻] mtype) ②
❶ ③ TLB pattern [❶, ❸, ❻]
msg32 // access msg32, queue32, ipc_ns
sys_msgrcv(32, mtext, mtype) ③

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

16

## Slide 102

## **Leaking 4 kB-Aligned Address**

## **C1:** Where to write?

DPM
① TLB pattern sys_msgrcv(id, mtext, mtype):
❻ queue = ipc_ns.root_rt[id]
ipc_ns
msg = find_msg(queue, mtype)
❺ copy_to_user(mtext, msg.mtext)
queue0
mtext = char[]
❹ mtype = 0x41
queue1
❸ queue32 // ① access TLB pattern [❷ msg0, , ❺, ❻ queue0, ]  ∩ ipc_ns  ∩
sys_msgrcv(0, mtext, mtype) ①
[❷, ❻]  \
❷ msg1 // ② access TLB pattern [❷ msg1, , ❹[❷, ❻ queue1, ] ]  \ ipc_ns  \
msg0 sys_msgrcv(1, [❶, mtext,  ❸, ❻] mtype) ②
❶ ③ TLB pattern [❶, ❸, ❻]
msg32 // access msg32, queue32, ipc_ns
sys_msgrcv(32, mtext, mtype) ③

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

16

## Slide 103

## **Leaking 4 kB-Aligned Address**

## **C1:** Where to write?

DPM
① TLB pattern sys_msgrcv(id, mtext, mtype):
❻ queue = ipc_ns.root_rt[id]
ipc_ns
msg = find_msg(queue, mtype)
❺ copy_to_user(mtext, msg.mtext)
queue0
mtext = char[]
❹ ② TLB pattern mtype = 0x41
queue1
❸ queue32 // ① access TLB pattern [❷ msg0, , ❺, ❻ queue0, ]  ∩ ipc_ns  ∩
sys_msgrcv(0, mtext, mtype) ①
[❷, ❻]  \
❷ msg1 // ② access TLB pattern [❷ msg1, , ❹[❷, ❻ queue1, ] ]  \ ipc_ns  \
msg0 sys_msgrcv(1, [❶, mtext,  ❸, ❻] mtype) ②
❶ ③ TLB pattern [❶, ❸, ❻]
msg32 // access msg32, queue32, ipc_ns
sys_msgrcv(32, mtext, mtype) ③

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

16

## Slide 104

## **Leaking 4 kB-Aligned Address**

## **C1:** Where to write?

DPM
① TLB pattern sys_msgrcv(id, mtext, mtype):
❻ queue = ipc_ns.root_rt[id]
ipc_ns
msg = find_msg(queue, mtype)
❺ copy_to_user(mtext, msg.mtext)
queue0
mtext = char[]
❹ ② TLB pattern mtype = 0x41
queue1
❸ queue32 // ① access TLB pattern [❷ msg0, , ❺, ❻ queue0, ]  ∩ ipc_ns  ∩
sys_msgrcv(0, mtext, mtype) ①
[❷, ❻]  \
❷ msg1 // ② access TLB pattern [❷ msg1, , ❹[❷, ❻ queue1, ] ]  \ ipc_ns  \
msg0 ③ TLB pattern sys_msgrcv(1, [❶, mtext,  ❸, ❻] mtype) ②
❶ ③ TLB pattern [❶, ❸, ❻]
msg32 // access msg32, queue32, ipc_ns
sys_msgrcv(32, mtext, mtype) ③

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

16

## Slide 105

## **Leaking 4 kB-Aligned Address**

## **C1:** Where to write?

DPM
① TLB pattern sys_msgrcv(id, mtext, mtype):
❻ queue = ipc_ns.root_rt[id]
ipc_ns
msg = find_msg(queue, mtype)
❺ copy_to_user(mtext, msg.mtext)
queue0
mtext = char[]
❹ ② TLB pattern mtype = 0x41
queue1
❸ queue32 // ① access TLB pattern [❷ msg0, , ❺, ❻ queue0, ]  ∩ ipc_ns  ∩
sys_msgrcv(0, mtext, mtype) ①
[❷, ❻]  \
❷ msg1 // ② access TLB pattern [❷ msg1, , ❹[❷, ❻ queue1, ] ]  \ ipc_ns  \
msg0 ③ TLB pattern sys_msgrcv(1, [❶, mtext,  ❸, ❻] mtype) ②
❶ ③ TLB pattern [❶, ❸, ❻]
msg32 // access msg32, queue32, ipc_ns
sys_msgrcv(32, mtext, mtype) ③

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

16

## Slide 106

## **Leaking 4 kB-Aligned Address**

## **C1:** Where to write?

DPM
① TLB pattern sys_msgrcv(id, mtext, mtype):
❻ queue = ipc_ns.root_rt[id]
ipc_ns
msg = find_msg(queue, mtype)
❺ copy_to_user(mtext, msg.mtext)
queue0
mtext = char[]
❹ ② TLB pattern mtype = 0x41
queue1
❸ queue32 // ① access TLB pattern [❷ msg0, , ❺, ❻ queue0, ]  ∩ ipc_ns  ∩
sys_msgrcv(0, mtext, mtype) ①
[❷, ❻]  \
❷ msg1 // ② access TLB pattern [❷ msg1, , ❹[❷, ❻ queue1, ] ]  \ ipc_ns  \
msg0 ③ TLB pattern sys_msgrcv(1, [❶, mtext,  ❸, ❻] mtype) ②
❶ ③ TLB pattern [❶, ❸, ❻]
msg32 // access msg32, queue32, ipc_ns
sys_msgrcv(32, mtext, mtype) ③

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

16

## Slide 107

## **Leaking 4 kB-Aligned Address**

## **C1:** Where to write?

DPM
① TLB pattern sys_msgrcv(id, mtext, mtype):
❻ queue = ipc_ns.root_rt[id]
ipc_ns
msg = find_msg(queue, mtype)
❺ copy_to_user(mtext, msg.mtext)
queue0
mtext = char[]
❹ ② TLB pattern mtype = 0x41
queue1
❸ queue32 // ① access TLB pattern [❷ msg0, , ❺, ❻ queue0, ]  ∩ ipc_ns  ∩
sys_msgrcv(0, mtext, mtype) ①
[❷, ❻]  \
❷ msg1 // ② access TLB pattern [❷ msg1, , ❹[❷, ❻ queue1, ] ]  \ ipc_ns  \
msg0 ③ TLB pattern sys_msgrcv(1, [❶, mtext,  ❸, ❻] mtype) ②
❶ ③ TLB pattern [❶, ❸, ❻]
msg32 // access msg32, queue32, ipc_ns
sys_msgrcv(32, mtext, mtype) ③

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

16

## Slide 108

## **Leaking 4 kB-Aligned Address**

## **C1:** Where to write?

DPM
① TLB pattern sys_msgrcv(id, mtext, mtype):
❻ queue = ipc_ns.root_rt[id]
ipc_ns
msg = find_msg(queue, mtype)
❺ copy_to_user(mtext, msg.mtext)
queue0
mtext = char[]
❹ ② TLB pattern mtype = 0x41
queue1
❸ queue32 // ① access TLB pattern [❷ msg0, , ❺, ❻ queue0, ]  ∩ ipc_ns  ∩
sys_msgrcv(0, mtext, mtype) ①
[❷, ❻]  \
❷ msg1 // ② access TLB pattern [❷ msg1, , ❹[❷, ❻ queue1, ] ]  \ ipc_ns  \
msg0 ③ TLB pattern sys_msgrcv(1, [❶, mtext,  ❸, ❻] mtype) ②
❶ ③ TLB pattern [❶, ❸, ❻]
msg32 // access msg32, queue32, ipc_ns
sys_msgrcv(32, mtext, mtype) ③

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

16

## Slide 109

_2 MB-aligned 4 kB-aligned_ Location of **C1:** Where to write? _memory sections_ ? _slab pages_ ? _Object size aligned_ ? target objects

**C2:** What to write?

> _Self reference_ ? Arbitrary read/write

## Slide 110

**C1:** Where to write?

## **Massaging**

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

18

## Slide 111

**C1:** Where to write?

## **Massaging**

**Ideal page:** Contains only attacker-controlled objects

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

18

## Slide 112

**C1:** Where to write?

## **Massaging**

**Ideal page:** Contains only attacker-controlled objects **How?** Use slab side channel [Maa+24b]

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

18

## Slide 113

**C1:** Where to write?

## **Massaging**

**Ideal page:** Contains only attacker-controlled objects **How?** Use slab side channel [Maa+24b] **Sufficent for reliable kernel exploitation** Known offsets within slab page

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

18

## Slide 114

**Location Disclosure Attacks**

**C1:** Where to write?

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

19

## Slide 115

**C1:** Where to write?

## **Location Disclosure Attacks**

**Evaluated Linux kernel** : v5.15, v6.5, and v6.8

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

19

## Slide 116

## **Location Disclosure Attacks**

## **C1:** Where to write?

**Evaluated Linux kernel** : v5.15, v6.5, and v6.8

**CPUs** :

Intel Kaby, Coffee, Alder, Raptor, and Meteor Lake _evaluated_ AMD and some ARM _affected_

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

19

## Slide 117

**C1:** Where to write?

## **Location Disclosure Attacks**

**Evaluated Linux kernel** : v5.15, v6.5, and v6.8

**CPUs** :

Intel Kaby, Coffee, Alder, Raptor, and Meteor Lake _evaluated_ AMD and some ARM _affected_

**Leaked object locations** :

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

19

## Slide 118

**C1:** Where to write?

## **Location Disclosure Attacks**

**Evaluated Linux kernel** : v5.15, v6.5, and v6.8

**CPUs** :

Intel Kaby, Coffee, Alder, Raptor, and Meteor Lake _evaluated_ AMD and some ARM _affected_

**Leaked object locations** : Kernel stacks

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

19

## Slide 119

**C1:** Where to write?

## **Location Disclosure Attacks**

**Evaluated Linux kernel** : v5.15, v6.5, and v6.8

**CPUs** :

Intel Kaby, Coffee, Alder, Raptor, and Meteor Lake _evaluated_ AMD and some ARM _affected_ **Leaked object locations** :

Kernel stacks Kernel heap:

`msg_msg` , `cred` , `file` , `seq_file` , and `pipe_buffer`

Lukas Maar

Lukas Giner

\```
https://lukasmaar.github.io/
\```

19

## Slide 120

**C1:** Where to write?

## **Location Disclosure Attacks**

### **Evaluated Linux kernel** :

v5.15, v6.5, and v6.8

**CPUs** :

Intel Kaby, Coffee, Alder, Raptor, and Meteor Lake _evaluated_ AMD and some ARM _affected_

**Leaked object locations** :

Kernel stacks Kernel heap:

`msg_msg` , `cred` , `file` , `seq_file` , and `pipe_buffer` Page tables:

PUD, PMD, and PT

Lukas Maar

Lukas Giner

\```
https://lukasmaar.github.io/
\```

19

## Slide 121

2 MB-aligned 4 kB-aligned
C1:  Where to write? memory sections ? slab pages ? Object size aligned ?

> _Self reference_ ?

**C2:** What to write?

Location of target objects

Arbitrary read/write

## Slide 122

# **Side-Channel-Assisted Kernel-Level Attacks**

## Slide 123

**Case Studies**

**C2:** What to write?

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

21

## Slide 124

**Case Studies**

**C2:** What to write?

Lukas Maar

Lukas Giner

\```
https://lukasmaar.github.io/
\```

21

## Slide 125

**Exploit Primitives and Exploit Techniques**

**C2:** What to write?

Start with a solid exploit primitive, e.g.,
unlink primitive or 8-byte slab write , and
end with an arbitrary read/write or an
arbitrary kernel code execution .

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

22

## Slide 126

## **Exploit Primitives and Exploit Techniques**

## **C2:** What to write?

Start with a solid exploit primitive, e.g.,
unlink primitive or 8-byte slab write , and
end with an arbitrary read/write or an
arbitrary kernel code execution .

Lukas Maar

Lukas Giner

\```
https://lukasmaar.github.io/
\```

22

## Slide 127

## **Exploit Primitives and Exploit Techniques**

## **C2:** What to write?

**Start with a solid exploit primitive, e.g.,** **_unlink primitive_ or** **_8-byte slab write_ , and end with an** **_arbitrary read/write_ or an** **_arbitrary kernel code execution_ .**

Lukas Maar

Lukas Giner

\```
https://lukasmaar.github.io/
\```

22

## Slide 128

## **Exploit Primitives and Exploit Techniques**

## **C2:** What to write?

Start with a solid exploit primitive, e.g.,
unlink primitive or 8-byte slab write , and
end with an arbitrary read/write or an
arbitrary kernel code execution .

Lukas Maar

Lukas Giner

\```
https://lukasmaar.github.io/
\```

22

## Slide 129

## **Exploit Primitives and Exploit Techniques**

## **C2:** What to write?

Start with a solid exploit primitive, e.g.,
unlink primitive or 8-byte slab write , and
end with an arbitrary read/write or an
arbitrary kernel code execution .

Lukas Maar

Lukas Giner

\```
https://lukasmaar.github.io/
\```

22

## Slide 130

**C2:** What to write?

## **Unlink Primitive**

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

23

## Slide 131

**C2:** What to write?

## **Unlink Primitive**

### **What is it?**

Misuse unsafe element unlink from a list Two write primitives:

\```
*(next+8)=prev;
*(prev)=next;
\```

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

23

## Slide 132

## **Unlink Primitive**

## **C2:** What to write?

### **What is it?**

Misuse unsafe element unlink from a list Two write primitives:

`*(next + 8) = prev; *(prev) = next;` **Prior work:**

BadBinder [Sto19] Many others [Sec20; San20; Maa+24a]

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

23

## Slide 133

**C2:** What to write?

## **Unlink Primitive**

**What is it?**

Misuse unsafe element unlink from a list Two write primitives:

`*(next + 8) = prev; *(prev) = next;` **Prior work:** BadBinder [Sto19] Many others [Sec20; San20; Maa+24a] **Our goal:**

Arbitrary read/write primitive

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

23

## Slide 134

**C2:** What to write?

## **Unlink Primitive to Controlled Corruption**

##### Unlink operation

1 struct list_head {
2 struct list_head *next;
3 struct list_head *prev;
4 }; binder_thread_1 binder_thread_2 binder_thread_3
5
6 struct binder_thread { wait: wait: wait:
78 ...struct list_head wait; nextprev next prev nextprev
9 ...
10 }; next: bt2.wait next: bt3.wait 0xdeadbeef next: bt4.wait
11 prev: bt0.wait prev: 0xbadc0fe bt1.wait prev: bt2.wait
12 /* Unlinks element e */
13 void list_del(list_head *e) {
14 e->next->prev = e->prev; remove_wait_queue(&binder_thread_2);
15 e->prev->next = e->next; // *(bt3.wait->prev) 0xdeadbeef+8) = 0x = bt1.wait; adc0fe;
16 }
// *(bt1.wait->next) 0xbadc0fe) = 0xdeadbeef; = bt3.wait;
17 void remove_wait_queue(binder_thread *bt) {
18 /* Trigger unlinking */
19 list_del(&bt->wait);
20 }

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

24

## Slide 135

**C2:** What to write?

## **Unlink Primitive to Controlled Corruption**

##### Unlink operation

1 struct list_head {
2 struct list_head *next;
3 struct list_head *prev;
4 }; binder_thread_1 binder_thread_2 binder_thread_3
5
6 struct binder_thread { wait: wait: wait:
78 ...struct list_head wait; nextprev next prev nextprev
9 ...
10 }; next: bt2.wait next: bt3.wait 0xdeadbeef next: bt4.wait
11 prev: bt0.wait prev: 0xbadc0fe bt1.wait prev: bt2.wait
12 /* Unlinks element e */
13 void list_del(list_head *e) {
14 e->next->prev = e->prev; remove_wait_queue(&binder_thread_2);
15 e->prev->next = e->next; // *(bt3.wait->prev) 0xdeadbeef+8) = 0x = bt1.wait; adc0fe;
16 }
// *(bt1.wait->next) 0xbadc0fe) = 0xdeadbeef; = bt3.wait;
17 void remove_wait_queue(binder_thread *bt) {
18 /* Trigger unlinking */
19 list_del(&bt->wait);
20 }

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

24

## Slide 136

**C2:** What to write?

## **Unlink Primitive to Controlled Corruption**

##### Unlink operation

1 struct list_head {
2 struct list_head *next;
3 struct list_head *prev;
4 }; binder_thread_1 binder_thread_2 binder_thread_3
5
6 struct binder_thread { wait: wait: wait:
78 ...struct list_head wait; nextprev next prev nextprev
9 ...
10 }; next: bt2.wait next: bt3.wait 0xdeadbeef next: bt4.wait
11 prev: bt0.wait prev: 0xbadc0fe bt1.wait prev: bt2.wait
12 /* Unlinks element e */
13 void list_del(list_head *e) {
14 e->next->prev = e->prev; remove_wait_queue(&binder_thread_2);
15 e->prev->next = e->next; // *(bt3.wait->prev) 0xdeadbeef+8) = 0x = bt1.wait; adc0fe;
16 }
// *(bt1.wait->next) 0xbadc0fe) = 0xdeadbeef; = bt3.wait;
17 void remove_wait_queue(binder_thread *bt) {
18 /* Trigger unlinking */
19 list_del(&bt->wait);
20 }

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

24

## Slide 137

**C2:** What to write?

## **Unlink Primitive to Controlled Corruption**

##### Unlink operation

1 struct list_head {
2 struct list_head *next;
3 struct list_head *prev;
4 }; binder_thread_1 binder_thread_2 binder_thread_3
5
6 struct binder_thread { wait: wait: wait:
78 ...struct list_head wait; nextprev next prev nextprev
9 ...
10 }; next: bt2.wait next: bt3.wait 0xdeadbeef next: bt4.wait
11 prev: bt0.wait prev: 0xbadc0fe bt1.wait prev: bt2.wait
12 /* Unlinks element e */
13 void list_del(list_head *e) {
14 e->next->prev = e->prev; remove_wait_queue(&binder_thread_2);
15 e->prev->next = e->next; // *(bt3.wait->prev) 0xdeadbeef+8) = 0x = bt1.wait; adc0fe;
16 }
// *(bt1.wait->next) 0xbadc0fe) = 0xdeadbeef; = bt3.wait;
17 void remove_wait_queue(binder_thread *bt) {
18 /* Trigger unlinking */
19 list_del(&bt->wait);
20 }

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

24

## Slide 138

**C2:** What to write?

## **Unlink Primitive to Controlled Corruption**

##### Unlink operation

1 struct list_head {
2 struct list_head *next;
3 struct list_head *prev;
4 }; binder_thread_1 binder_thread_2 binder_thread_3
5
6 struct binder_thread { wait: wait: wait:
78 ...struct list_head wait; nextprev next prev nextprev
9 ...
10 }; next: bt2.wait next: bt3.wait 0xdeadbeef next: bt4.wait
11 prev: bt0.wait prev: 0xbadc0fe bt1.wait prev: bt2.wait
12 /* Unlinks element e */
13 void list_del(list_head *e) {
14 e->next->prev = e->prev; remove_wait_queue(&binder_thread_2);
15 e->prev->next = e->next; // *(bt3.wait->prev) 0xdeadbeef+8) = 0x = bt1.wait; adc0fe;
16 }
// *(bt1.wait->next) 0xbadc0fe) = 0xdeadbeef; = bt3.wait;
17 void remove_wait_queue(binder_thread *bt) {
18 /* Trigger unlinking */
19 list_del(&bt->wait);
20 }

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

24

## Slide 139

**C2:** What to write?

## **Unlink Primitive to Controlled Corruption**

##### Unlink operation

1 struct list_head {
2 struct list_head *next;
3 struct list_head *prev;
4 }; binder_thread_1 binder_thread_2 binder_thread_3
5
6 struct binder_thread { wait: wait: wait:
78 ...struct list_head wait; nextprev next prev nextprev
9 ...
10 }; next: bt2.wait next: bt3.wait 0xdeadbeef next: bt4.wait
11 prev: bt0.wait prev: 0xbadc0fe bt1.wait prev: bt2.wait
12 /* Unlinks element e */
13 void list_del(list_head *e) {
14 e->next->prev = e->prev; remove_wait_queue(&binder_thread_2);
15 e->prev->next = e->next; // *(bt3.wait->prev) 0xdeadbeef+8) = 0x = bt1.wait; adc0fe;
16 }
// *(bt1.wait->next) 0xbadc0fe) = 0xdeadbeef; = bt3.wait;
17 void remove_wait_queue(binder_thread *bt) {
18 /* Trigger unlinking */
19 list_del(&bt->wait);
20 }

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

24

## Slide 140

**C2:** What to write?

## **Unlink Primitive to Controlled Corruption**

##### Unlink operation

1 struct list_head {
2 struct list_head *next;
3 struct list_head *prev;
4 }; binder_thread_1 binder_thread_2 binder_thread_3
5
6 struct binder_thread { wait: wait: wait:
78 ...struct list_head wait; nextprev next prev nextprev
9 ...
10 }; next: bt2.wait next: bt3.wait 0xdeadbeef next: bt4.wait
11 prev: bt0.wait prev: 0xbadc0fe bt1.wait prev: bt2.wait
12 /* Unlinks element e */
13 void list_del(list_head *e) {
14 e->next->prev = e->prev; remove_wait_queue(&binder_thread_2);
15 e->prev->next = e->next; // *(bt3.wait->prev) 0xdeadbeef+8) = 0x = bt1.wait; adc0fe;
16 }
// *(bt1.wait->next) 0xbadc0fe) = 0xdeadbeef; = bt3.wait;
17 void remove_wait_queue(binder_thread *bt) {
18 /* Trigger unlinking */
19 list_del(&bt->wait);
20 }

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

24

## Slide 141

## **Unlink Primitive to Controlled Corruption**

## **C2:** What to write?

##### Unlink operation

1 struct list_head {
2 struct list_head *next;
3 struct list_head *prev;
4 }; binder_thread_1 binder_thread_2 binder_thread_3
5
6 struct binder_thread { wait: wait: wait:
78 ...struct list_head wait; nextprev next prev nextprev
9 ...
10 }; next: bt2.wait next: bt3.wait 0xdeadbeef next: bt4.wait
11 prev: bt0.wait prev: 0xbadc0fe bt1.wait prev: bt2.wait
12 /* Unlinks element e */
13 void list_del(list_head *e) {
14 e->next->prev = e->prev; remove_wait_queue(&binder_thread_2);
15 e->prev->next = e->next; // *( 0xdeadbeef+8) bt3.wait->prev) = 0x = b adc0fe; t1.wait;
16 }
// *(bt1.wait->next) 0xbadc0fe) = 0xdeadbeef; = bt3.wait;
17 void remove_wait_queue(binder_thread *bt) {
18 /* Trigger unlinking */
19 list_del(&bt->wait);
20 }

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

24

## Slide 142

## **Unlink Primitive to Arbitrary Read/Write**

## **C2:** What to write?

Exploit
1
2
3
4
buffered
pipe_buffer2: data 5
len offset 6
page 78
9
buffered 10
pipe_buffer1: data 11
len offset 12
page 13
14
pipe_buffer0: len offset buffereddata 151617
18
page 19
20
21
Slab Page of kmalloc-cg-64

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

25

## Slide 143

## **Unlink Primitive to Arbitrary Read/Write**

## **C2:** What to write?

Exploit

1 // Unlink primitive
2 *(&pipe_buffer0 + 8) = pipe_buffer0
3 *(pipe_buffer0) = &pipe_buffer0
4
buffered
pipe_buffer2: data 5
len offset 6
page 78
9
buffered 10
pipe_buffer1: data 11
len offset 12
page 13
14
Unlink 15
Primitive pipe_buffer0: len offset 1617
18
page 19
20
21
Slab Page of kmalloc-cg-64

25 Lukas Maar

Lukas Giner

\```
https://lukasmaar.github.io/
\```

## Slide 144

## **Unlink Primitive to Arbitrary Read/Write**

## **C2:** What to write?

Exploit
1 // Unlink primitive
2 *(&pipe_buffer0 + 8) = pipe_buffer0
3 *(pipe_buffer0) = &pipe_buffer0
4
buffered
pipe_buffer2: data 5 // Refer target page
len offset 6 write(fd0, data = {
page 78
9
buffered 10
pipe_buffer1: data 11
len offset 12
page 13
14
15 }, 96)
pipe_buffer0: len offset 1617
18
page 19
20
21
Slab Page of kmalloc-cg-64

25 Lukas Maar

Lukas Giner

\```
https://lukasmaar.github.io/
\```

## Slide 145

## **Unlink Primitive to Arbitrary Read/Write**

## **C2:** What to write?

Exploit
1 // Unlink primitive
2 *(&pipe_buffer0 + 8) = pipe_buffer0
3 *(pipe_buffer0) = &pipe_buffer0
4
buffered
pipe_buffer2: data 5 // Refer target page
len offset 6 write(fd0, data = {
7 .pipe_buffer0 = {
page 8 .offset =
9 },
buffered 10 .pipe_buffer1 = {
pipe_buffer1: data 11 .page =
len offset 12 .offset =
page 13 .len =
14 }
15 }, 96)
pipe_buffer0: len offset 1617
18
page 19
20
21
Slab Page of kmalloc-cg-64

Lukas Maar

Lukas Giner

\```
https://lukasmaar.github.io/
\```

25

## Slide 146

## **Unlink Primitive to Arbitrary Read/Write**

## **C2:** What to write?

Exploit
1 // Unlink primitive
2 *(&pipe_buffer0 + 8) = pipe_buffer0
3 *(pipe_buffer0) = &pipe_buffer0
4
buffered
pipe_buffer2: data 5 // Refer target page
len offset 6 write(fd0, data = {
7 .pipe_buffer0 = {
page 8 .offset = 8,
9 },
buffered 10 .pipe_buffer1 = {
pipe_buffer1: data 11 .page =
len offset 12 .offset =
page 13 .len =
14 }
15 }, 96)
pipe_buffer0: len offset 1617
18
page 19
20
21
Slab Page of kmalloc-cg-64

Lukas Maar

Lukas Giner

\```
https://lukasmaar.github.io/
\```

25

## Slide 147

## **Unlink Primitive to Arbitrary Read/Write**

## **C2:** What to write?

Exploit
1 // Unlink primitive
2 *(&pipe_buffer0 + 8) = pipe_buffer0
3 *(pipe_buffer0) = &pipe_buffer0
4
buffered
pipe_buffer2: data 5 // Refer target page
len offset 6 write(fd0, data = {
7 .pipe_buffer0 = {
page 8 .offset = 8,
9 },
10 .pipe_buffer1 = {
pipe_buffer1: 11 .page = &target_page,
len offset 12 .offset = 0,
page target 1314 } .len = PAGE_SIZE,
page 15 }, 96)
pipe_buffer0: len offset 1617
18
page 19
20
21
Slab Page of kmalloc-cg-64

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

25

## Slide 148

## **Unlink Primitive to Arbitrary Read/Write**

## **C2:** What to write?

Exploit
1 // Unlink primitive
2 *(&pipe_buffer0 + 8) = pipe_buffer0
3 *(pipe_buffer0) = &pipe_buffer0
4
buffered
pipe_buffer2: data 5 // Refer target page
len offset 6 write(fd0, data = {
7 .pipe_buffer0 = {
page 8 .offset = 8,
9 },
10 .pipe_buffer1 = {
pipe_buffer1: 11 .page = &target_page,
len offset 12 .offset = 0,
page target 1314 } .len = PAGE_SIZE,
page 15 }, 96)
pipe_buffer0: 16
len offset 17 // Read from target page
18 read(fd1, &data, 8)
page 19
20 // Write to target page
21 write(fd1, data, 8)
Slab Page of kmalloc-cg-64

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

25

## Slide 149

## **Unlink Primitive to Arbitrary Read/Write**

## **C2:** What to write?

Exploit
1 // Unlink primitive
2 *(&pipe_buffer0 + 8) = pipe_buffer0
3 *(pipe_buffer0) = &pipe_buffer0
4
buffered
pipe_buffer2: data 5 // Refer target page
len offset 6 write(fd0, data = {
7 .pipe_buffer0 = {
page 8 .offset = 8,
target 9 },
10 .pipe_buffer1 = {
pipe_buffer1: page 2 11 .page = &target_page,
len offset 12 .offset = 0,
page target 1314 } .len = PAGE_SIZE,
page 15 }, 96)
pipe_buffer0: 16
len offset 17 // Read from target page
18 read(fd1, &data, 8)
page 19
20 // Write to target page
21 write(fd1, data, 8)
Slab Page of kmalloc-cg-64

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

25

## Slide 150

## **Unlink Primitive to Arbitrary Read/Write**

## **C2:** What to write?

Exploit

1 // Unlink primitive
2 *(&pipe_buffer0 + 8) = pipe_buffer0
3 *(pipe_buffer0) = &pipe_buffer0
4
buffered
pipe_buffer2: data 5 // Refer 2048 byte of target page 2
len offset 6
page 78
target 9
pipe_buffer1: page 2 1011
len offset 12
page target 1314
page 15
pipe_buffer0: len offset 1617
18
page 19
20
21
Slab Page of kmalloc-cg-64

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

25

## Slide 151

## **Unlink Primitive to Arbitrary Read/Write**

## **C2:** What to write?

Exploit
1 // Unlink primitive
2 *(&pipe_buffer0 + 8) = pipe_buffer0
3 *(pipe_buffer0) = &pipe_buffer0
4
buffered
pipe_buffer2: data 5 // Refer 2048 byte of target page 2
len offset 6 write(fd0, data = {
7 .pipe_buffer0 = {
page 8 .offset = 8,
target 9 },
10 .pipe_buffer1 = {
pipe_buffer1: page 2 11 .page = &target_page2,
len offset 12 .offset = 2048,
page 13 .len = PAGE_SIZE,
14 }
15 }, 96)
pipe_buffer0: len offset 1617
18
page 19
20
21
Slab Page of kmalloc-cg-64

Lukas Maar

Lukas Giner

\```
https://lukasmaar.github.io/
\```

25

## Slide 152

## **Unlink Primitive to Arbitrary Read/Write**

## **C2:** What to write?

Exploit
1 // Unlink primitive
2 *(&pipe_buffer0 + 8) = pipe_buffer0
3 *(pipe_buffer0) = &pipe_buffer0
4
buffered
pipe_buffer2: data 5 // Refer 2048 byte of target page 2
len offset 6 write(fd0, data = {
7 .pipe_buffer0 = {
page 8 .offset = 8,
target 9 },
10 .pipe_buffer1 = {
pipe_buffer1: page 2 11 .page = &target_page2,
len offset 12 .offset = 2048,
page 13 .len = PAGE_SIZE,
14 }
15 }, 96)
pipe_buffer0: 16
len offset 17 // Read from target page 2
18 read(fd1, &data, 8)
page 19
20 // Write to target page 2
21 write(fd1, data, 8)
Slab Page of kmalloc-cg-64

Lukas Maar

Lukas Giner

\```
https://lukasmaar.github.io/
\```

25

## Slide 153

_2 MB-aligned 4 kB-aligned_ **C1:** Where to write? _memory sections_ ? _slab pages_ ? _Object size aligned_ ?

> _Self reference_ ?

**C2:** What to write?

Location of target objects

Arbitrary read/write

## Slide 154

**Discussion**

## Slide 155

## **Mitigations**

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

27

## Slide 156

## **Mitigations**

Isolate kernel/user address space

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

27

## Slide 157

## **Mitigations**

Isolate kernel/user address space **KPTI** Software-based solution _most kernel memory not mapped while in user mode_

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

27

## Slide 158

## **Mitigations**

Isolate kernel/user address space **KPTI** Software-based solution _most kernel memory not mapped while in user mode_ **Intel LASS** Hardware-based solution Protection before paging _prevents TLB side channel_

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

27

## Slide 159

## **Black Hat Sound Bytes**

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

28

## Slide 160

## **Black Hat Sound Bytes**

**Defense-based Amplification:** Defenses increase security in one dimension but may decrease in another.

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

28

## Slide 161

## **Black Hat Sound Bytes**

**Defense-based Amplification:** Defenses increase security in one dimension but may decrease in another. **Allocator-based Amplification:** Allocator designs can decrease security.

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

28

## Slide 162

## **Black Hat Sound Bytes**

**Defense-based Amplification:** Defenses increase security in one dimension but may decrease in another. **Allocator-based Amplification:** Allocator designs can decrease security. **Reliability:** Side channels can increase reliability of kernel exploitation.

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

28

## Slide 163

## **Acknowledgments**

This research was made possible by generous funding from:

Supported in part by the European Research Council (ERC project FSSec 101076409), the Austrian Research Promotion Agency (FFG) via the SEIZE project (FFG grant number 888087) and the Austrian Science Fund (FWF SFB project SPyCoDe 10.55776/F85). Additional funding was provided by a generous gift from Intel. Any opinions, findings, and conclusions or recommendations expressed in this paper are those of the authors and do not necessarily reflect the views of the funding parties.

Lukas Maar Lukas Giner

\```
https://lukasmaar.github.io/
\```

29

## Slide 164

S C I E N C E P A S S I O N T E C H N O L O G Y

**Derandomizing the Location of Security-Critical Kernel Objects in the Linux Kernel**

**Lukas Maar Lukas Giner** August 6-7, 2025 Briefings

Daniel Gruss

Stefan Mangard

isec.tugraz.at

## Slide 165

## **References I**

[Maa+24a] L. Maar, F. Draschbacher, L. Lamster, and S. Mangard. **Defects-in-Depth: Analyzing the Integration of Effective Defenses against One-Day Exploits in Android Kernels** . USENIX Security. 2024.

- [Maa+24b] L. Maar, S. Gast, M. Unterguggenberger, M. Oberhuber, and S. Mangard. **SLUBStick: Arbitrary Memory Writes through Practical Software Cross-Cache Attacks within the Linux Kernel** . USENIX Security. 2024.

- [San20] E. Sanfelix. **A bug collision tale** . 2020. URL: `https://labs.bluefrostsecurity. de/files/OffensiveCon2020_bug_collision_tale.pdf` .

[Sec20] B. F. Security. **Exploiting CVE-2020-0041 - Part 2: Escalating to root** . 2020. URL: `https://labs.bluefrostsecurity.de/blog/2020/04/08/cve-2020-0041part-2-escalating-to-root/` .

[Sto19] M. Stone. **Bad Binder: Android In-The-Wild Exploit** . 2019. URL: `https://googleprojectzero.blogspot.com/2019/11/bad-binder-androidin-wild-exploit.html` .

\```
https://lukasmaar.github.io/
\```

Lukas Maar Lukas Giner

30
