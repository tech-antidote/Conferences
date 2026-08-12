---
title: "CUDA've done better - Hacking Nvidia GPUs for container-escape and privilege escalation"
speakers: ["Daniel Cohen Hillel", "Noam Trobishi"]
conference: "DEF CON"
conference_full: "DEF CON 34"
edition: "34"
year: null
source_pdf: "DEF CON 34/DEF CON 34 - Daniel Cohen Hillel, Noam Trobishi - CUDA've done better - Hacking Nvidia GPUs for container-escape and privilege escalation - Cudave v1.pdf"
pages: 256
sha256: "b9c8cff8334ed02017fffae1abeae706fbb9355639c752e3b0f83ea0670d48eb"
text_chars: 59318
ocr_pages: 5
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T00:15:57Z"
---
# CUDA've done better - Hacking Nvidia GPUs for container-escape and privilege escalation

**Speakers:** Daniel Cohen Hillel, Noam Trobishi  
**Conference:** DEF CON 34  
**Source:** `DEF CON 34/DEF CON 34 - Daniel Cohen Hillel, Noam Trobishi - CUDA've done better - Hacking Nvidia GPUs for container-escape and privilege escalation - Cudave v1.pdf` (256 pages)

## Slide 1

# **CUDA** ’ve Done Better

Hacking NVIDIA GPUs for container-escape and privilege escalation

Daniel Cohen Hillel (@0xDACA) Noam Trobishi

## Slide 2

## Background

• AI is a big thing

• I have FOMO

## Slide 3

## Background

- AI is a big thing

• I have FOMO

## Slide 4

## Background

- AI is a big thing

- I have FOMO

## Slide 5

## Background

- AI is a big thing

- I have FOMO

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Background
The NVIDIA Category
Our last Al sub-category focuses solely on NVIDIA products. For network accessible targets, an attempt must be launched from the contestant's laptop
within the contest network. For NV Container Toolkit, the attempt must be launched from within a crafted container image and execute arbitrary code on
host operating system. For Megatron Bridge, entries that leverage vulnerabilities pertaining to pickle deserialization or that leverage a vulnerability when
“trust_remote_code=true” are out of scope. Here are the targets and payouts for the NVIDIA category:
Master of Pwn
Points
Target Cash Prize
Megatron Bridge $20,000
NV Container Toolkit $50,000
Dynamo $50,000
```

## Slide 6

## Background

- AI is a big thing

- I have FOMO

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Background
The NVIDIA Category
Our last Al sub-category focuses solely on NVIDIA products. For network accessible targets, an attempt must be launched from the contestant's laptop
within the contest network. For NV Container Toolkit, the attempt must be launched from within a crafted container image and execute arbitrary code on
host operating system. For Megatron Bridge, entries that leverage vulnerabilities pertaining to pickle deserialization or that leverage a vulnerability when
“trust_remote_code=true” are out of scope. Here are the targets and payouts for the NVIDIA category:
Master of Pwn
Points
Target Cash Prize
Megatron Bridge $20,000
NV Container Toolkit $50,000
Dynamo $50,000
```

## Slide 7

## Background

- AI is a big thing

•  I have FOMO

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Background
The NVIDIA Category
Our last Al sub-category focuses solely on NVIDIA products. For network accessible targets, an attempt must be launched from the contestant's laptop
within the contest network. For NV Container Toolkit, the attempt must be launched from within a crafted container image and execute arbitrary code on
host operating Syste Oe eee ee nee ee eee eee ee Sea a VEIMereD iit WHEN
“trust_remote_code=true”
```

## Slide 8

Background
•  AI is a big thing
•  I have FOMO

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Background
The NVIDIA Category
Our last Al sub-category focuses solely on NVIDIA prod:
e Al is within the contest network. For NV Container Toolkit, the
host operating system. Foptess=-Dxidao—o= Tans
“trust_remote_code=true”
```

## Slide 9

## Talk overview

• Exploring the system and attack surfaces

• Assuming a UAF (use-after-free) vulnerability

• Exploitation technique – winning races with `rw_semaphore`

• Exploitation technique – mapping physical memory

• Escalating and combining primitives

• Profit

## Slide 10

## Talk overview

- Exploring the system and attack surfaces

- Assuming a UAF (use-after-free) vulnerability

- Exploitation technique – winning races with `rw_semaphore`

- Exploitation technique – mapping physical memory

- Escalating and combining primitives

- Profit

## Slide 11

## Talk overview

- Exploring the system and attack surfaces

- Assuming a UAF (use-after-free) vulnerability

- Exploitation technique – winning races with `rw_semaphore`

- Exploitation technique – mapping physical memory

- Escalating and combining primitives

- Profit

## Slide 12

## Talk overview

- Exploring the system and attack surfaces

- Assuming a UAF (use-after-free) vulnerability

- Exploitation technique – winning races with `rw_semaphore`

- Exploitation technique – mapping physical memory

- Escalating and combining primitives

• Profit

## Slide 13

## Talk overview

- Exploring the system and attack surfaces

- Assuming a UAF (use-after-free) vulnerability

- Exploitation technique – winning races with `rw_semaphore`

- Exploitation technique – mapping physical memory

- Escalating and combining primitives

• Profit

## Slide 14

## Talk overview

- Exploring the system and attack surfaces

- Assuming a UAF (use-after-free) vulnerability

- Exploitation technique – winning races with `rw_semaphore`

- Exploitation technique – mapping physical memory

- Escalating and combining primitives

- Profit

## Slide 15

## Talk overview

- Exploring the system and attack surfaces

- Assuming a UAF (use-after-free) vulnerability

- Exploitation technique – winning races with `rw_semaphore`

- Exploitation technique – mapping physical memory

- Escalating and combining primitives

- Profit

## Slide 16

## What exactly are we hacking?

• Technically, “ **NV Container Toolkit** ”

• “ _For NV Container Toolkit, the attempt must be launched from_

_within a crafted container image and execute arbitrary code on the host operating system.”   -_ PWN2OWN rules

## Slide 17

## What exactly are we hacking?

- Technically, “ **NV Container Toolkit** ”

• “ _For NV Container Toolkit, the attempt must be launched from_

_within a crafted container image and execute arbitrary code on the_

_host operating system.”   -_ PWN2OWN rules

## Slide 18

## What exactly are we hacking?

- Technically, “ **NV Container Toolkit** ”

- “ _For NV Container Toolkit, the attempt must be launched from_

_within a crafted container image and execute arbitrary code on the host operating system.”   -_ PWN2OWN rules

## Slide 19

What exactly are we hacking?

- Technically, “ **NV Container Toolkit** ”

• “ _For NV Container Toolkit, the attempt must be launched from within a crafted container image and execute arbitrary code on the host operating system.”   -_ PWN2OWN rules

## Slide 20

## What exactly are we hacking?

- Technically, “ **NV Container Toolkit** ”

• “ _For NV Container Toolkit, the attempt must be launched from within a crafted container image and execute arbitrary code on the host operating system.”   -_ PWN2OWN rules

## Slide 21

## What exactly are we hacking?

- Technically, “ **NV Container Toolkit** ”

- “ _For NV Container Toolkit, the attempt must be launched from within a crafted container image and execute arbitrary code on the host operating system.”   -_ PWN2OWN rules

## Slide 22

What are the interesting attack surfaces?

• **Container management** (NV Container Toolkit)

• Written in Go, potential for logic bugs.

• **Linux kernel module**

• Huge amount of complex open-source C code, highly controlled inputs.

• **The GSP chip**

• A (closed source) RISC-V chip on modern GPUs.

• *this list is not complete.

## Slide 23

What are the interesting attack surfaces?

- **Container management** (NV Container Toolkit)

   - Written in Go, potential for logic bugs.

- **Linux kernel module**

   - Huge amount of complex open-source C code, highly controlled inputs.

- **The GSP chip**

   - A (closed source) RISC-V chip on modern GPUs.

• *this list is not complete.

## Slide 24

## What are the interesting attack surfaces?

- **Container management** (NV Container Toolkit)

   - Written in Go, potential for logic bugs.

- **Linux kernel module**

   - Huge amount of complex open-source C code, highly controlled inputs.

- **The GSP chip**

   - A (closed source) RISC-V chip on modern GPUs.

• *this list is not complete.

## Slide 25

## What are the interesting attack surfaces?

- **Container management** (NV Container Toolkit)

   - Written in Go, potential for logic bugs.

- **Linux kernel module**

   - Huge amount of complex open-source C code, highly controlled inputs.

- **The GSP chip**

   - A (closed source) RISC-V chip on modern GPUs.

• *this list is not complete.

## Slide 26

## What are the interesting attack surfaces?

- **Container management** (NV Container Toolkit)

   - Written in Go, potential for logic bugs.

- **Linux kernel module**

   - Huge amount of complex open-source C code, highly controlled inputs.

- **The GSP chip**

   - A (closed source) RISC-V chip on modern GPUs.

- *this list is not complete.

## Slide 27

## What are the interesting attack surfaces?

- **Container management** (NV Container Toolkit)

   - Written in Go, potential for logic bugs.

- **Linux kernel module**

   - Huge amount of complex open-source C code, highly controlled inputs.

- **The GSP chip**

   - A (closed source) RISC-V chip on modern GPUs.

- *this list is not complete.

## Slide 28

Let’s dig in!

## Slide 29

Let’s dig in!

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Let’s dig in!
= (es) NVIDIA / open-gpu-kernel-modules ~
Code Issues 340 Pull reques
2 open-gpu-kernel-modules »'
P 24 Bran
@ mmaneetsingh
@@ github/ISSUE_TEMPLATE
B kernel-o
B® nowvea
mm:
gitignore
CODE_OF_CONDUCT.md
CONTRIBUTING.md
READMEmd
© SECURITY.md
1 nv-compiler.sh
DB utilsmk
© version.mk
Discussions
Actions
Security and quality Insights
Watch 192 k We Starred 17.1k
Add file ~ | <> Code ~ About
NVIDIA Linux open GPU kernel
module source
Releases 205
610.43.02
Packages
```

## Slide 30

## Kernel module objects and hierarchy

• NVIDIA implemented an “inheritance like” tree structure for objects.

## Slide 31

## Kernel module objects and hierarchy

• NVIDIA implemented an “inheritance like” tree structure for objects.

## Slide 32

## Kernel module objects and hierarchy

• NVIDIA implemented an “inheritance like” tree structure for objects.

Client
Device
Subdevice (GPU) Memory etc…
NVENC SemaphoreSurface MemoryMapper etc…

## Slide 33

## Assuming a UAF

• We want to have enough time between patching our bug and this talk, so **WE WILL NOT DISCLOSE HERE WHAT IS THE**

**VULNERABILITY, WHERE IT IS, OR WHAT IS THE PATCH** .

• From now on, we will just assume we can free a Subdevice object while it's being used.

• Trust me, it's not the interesting part ;)

## Slide 34

## Assuming a UAF

- We want to have enough time between patching our bug and this talk, so **WE WILL NOT DISCLOSE HERE WHAT IS THE VULNERABILITY, WHERE IT IS, OR WHAT IS THE PATCH** .

- From now on, we will just assume we can free a Subdevice object while it's being used.

- Trust me, it's not the interesting part ;)

## Slide 35

## Assuming a UAF

- We want to have enough time between patching our bug and this talk, so **WE WILL NOT DISCLOSE HERE WHAT IS THE VULNERABILITY, WHERE IT IS, OR WHAT IS THE PATCH** .

- From now on, we will just assume we can free a Subdevice object while it's being used.

- Trust me, it's not the interesting part ;)

## Slide 36

## Assuming a UAF

- We want to have enough time between patching our bug and this talk, so **WE WILL NOT DISCLOSE HERE WHAT IS THE VULNERABILITY, WHERE IT IS, OR WHAT IS THE PATCH** .

- From now on, we will just assume we can free a Subdevice object while it's being used.

- Trust me, it's not the interesting part ;)

## Slide 37

## What now?

• You know the drill, we have a use-after-free.

• **Need to allocate over the freed buffer with an attackercontrolled buffer.**

## Slide 38

## What now?

- You know the drill, we have a use-after-free.

- **Need to allocate over the freed buffer with an attackercontrolled buffer.**

## Slide 39

## What now?

- You know the drill, we have a use-after-free.

- **Need to allocate over the freed buffer with an attackercontrolled buffer.**

## Slide 40

## A magnificent allocation primitive

• We can use **IOCTL parameter buffer** as an allocation primitive

• Allocates attacker-controlled buffer (length and content) • **The buffer is copied back to the attacker!** • Need to **win a race** each time :(

## Slide 41

## A magnificent allocation primitive

- We can use **IOCTL parameter buffer** as an allocation primitive

• Allocates attacker-controlled buffer (length and content) • **The buffer is copied back to the attacker!** • Need to **win a race** each time :(

## Slide 42

## A magnificent allocation primitive

• We can use **IOCTL parameter buffer** as an allocation primitive

**1**

```
alloc buffer
```

• Allocates attacker-controlled buffer (length and content) • **The buffer is copied back to the attacker!** • Need to **win a race** each time :(

## Slide 43

## A magnificent allocation primitive

• We can use **IOCTL parameter buffer** as an allocation primitive

**1**

```
alloc buffer
```

### IOCTL params buffer

• Allocates attacker-controlled buffer (length and content) • **The buffer is copied back to the attacker!**

• Need to **win a race** each time :(

## Slide 44

## A magnificent allocation primitive

• We can use **IOCTL parameter buffer** as an allocation primitive

**1**

```
alloc buffer
```

### IOCTL params buffer

• Allocates attacker-controlled buffer (length and content) • **The buffer is copied back to the attacker!**

• Need to **win a race** each time :(

## Slide 45

## A magnificent allocation primitive

• We can use **IOCTL parameter buffer** as an allocation primitive

**1**

```
alloc buffer
```

**2**

```
copy_from_user
```

### IOCTL params buffer

• Allocates attacker-controlled buffer (length and content) • **The buffer is copied back to the attacker!** • Need to **win a race** each time :(

## Slide 46

## A magnificent allocation primitive

• We can use **IOCTL parameter buffer** as an allocation primitive

**1**

```
alloc buffer
```

**2**

```
copy_from_user
```

### IOCTL params buffer

```
DA CA DE BE 01 02 03 04 DA CA DE BE 01 02 03 04 DA CA DE BE
```

• Allocates attacker-controlled buffer (length and content) • **The buffer is copied back to the attacker!** • Need to **win a race** each time :(

## Slide 47

## A magnificent allocation primitive

- We can use **IOCTL parameter buffer** as an allocation primitive

**1**

**2** `alloc buffer copy_from_user` **R/W API lock** IOCTL params buffer

```
DA CA DE BE 01 02 03 04 DA CA DE BE 01 02 03 04 DA CA DE BE
```

• Allocates attacker-controlled buffer (length and content) • **The buffer is copied back to the attacker!** • Need to **win a race** each time :(

## Slide 48

## A magnificent allocation primitive

- We can use **IOCTL parameter buffer** as an allocation primitive

**1**

**2** `alloc buffer copy_from_user`

**R/W API lock** IOCTL params buffer

```
DA CA DE BE 01 02 03 04 DA CA DE BE 01 02 03 04 DA CA DE BE
```

• Allocates attacker-controlled buffer (length and content) • **The buffer is copied back to the attacker!** • Need to **win a race** each time :(

## Slide 49

## A magnificent allocation primitive

- We can use **IOCTL parameter buffer** as an allocation primitive

**1**

**2** `alloc buffer copy_from_user …do stuff…` **R/W API lock** IOCTL params buffer

IOCTL params buffer

```
DA CA DE BE 01 02 03 04 DA CA DE BE 01 02 03 04 DA CA DE BE
```

• Allocates attacker-controlled buffer (length and content) • **The buffer is copied back to the attacker!** • Need to **win a race** each time :(

## Slide 50

## A magnificent allocation primitive

- We can use **IOCTL parameter buffer** as an allocation primitive

**1**

**2** `alloc buffer copy_from_user …do stuff…` **R/W API lock** IOCTL params buffer

IOCTL params buffer

```
DA CA DE BE 01 02 03 04 DYA RPCA DE BE 01 02 03 04 DA CA DE BE 00HAYAPO
```

• Allocates attacker-controlled buffer (length and content) • **The buffer is copied back to the attacker!** • Need to **win a race** each time :(

## Slide 51

## A magnificent allocation primitive

• We can use **IOCTL parameter buffer** as an allocation primitive

**1**

**2**

`alloc buffer copy_from_user …do stuff…` **R/W R/W API lock API unlock** IOCTL params buffer

IOCTL params buffer

```
DA CA DE BE 01 02 03 04 DYA RPCA DE BE 01 02 03 04 DA CA DE BE 00HAYAPO
```

• Allocates attacker-controlled buffer (length and content) • **The buffer is copied back to the attacker!** • Need to **win a race** each time :(

## Slide 52

## A magnificent allocation primitive

• We can use **IOCTL parameter buffer** as an allocation primitive

**1**

**2**

`alloc buffer copy_from_user …do stuff…` **R/W R/W API lock API unlock** IOCTL params buffer

IOCTL params buffer

```
DA CA DE BE 01 02 03 04 DYA RPCA DE BE 01 02 03 04 DA CA DE BE 00HAYAPO
```

• Allocates attacker-controlled buffer (length and content) • **The buffer is copied back to the attacker!** • Need to **win a race** each time :(

## Slide 53

## A magnificent allocation primitive

• We can use **IOCTL parameter buffer** as an allocation primitive

**1**

**2 3** `alloc buffer copy_from_user …do stuff… copy_to_user` **R/W R/W API lock API unlock** IOCTL params buffer

IOCTL params buffer

```
DA CA DE BE 01 02 03 04 DYA RPCA DE BE 01 02 03 04 DA CA DE BE 00HAYAPO
```

• Allocates attacker-controlled buffer (length and content) • **The buffer is copied back to the attacker!** • Need to **win a race** each time :(

## Slide 54

## A magnificent allocation primitive

• We can use **IOCTL parameter buffer** as an allocation primitive

**1**

**2 3** `alloc buffer copy_from_user …do stuff… copy_to_user` **R/W R/W API lock API unlock** IOCTL params buffer

IOCTL params buffer

```
DA CA DE BE 01 02 03 04 DYA RPCA DE BE 01 02 03 04 DA CA DE BE 00HAYAPO
```

• Allocates attacker-controlled buffer (length and content) • **The buffer is copied back to the attacker!** • Need to **win a race** each time :(

## Slide 55

## A magnificent allocation primitive

• We can use **IOCTL parameter buffer** as an allocation primitive

**1**

**2 3** `alloc buffer copy_from_user …do stuff… copy_to_user` **R/W R/W API lock API unlock** IOCTL params buffer

IOCTL params buffer

```
DA CA DE BE 01 02 03 04 DYA RPCA DE BE 01 02 03 04 DA CA DE BE 00HAYAPO
```

• Allocates attacker-controlled buffer (length and content) • **The buffer is copied back to the attacker!** • Need to **win a race** each time :(

## Slide 56

## A magnificent allocation primitive

•  We can use  IOCTL parameter buffer  as an allocation primitive
1 2 3 4
alloc buffer  copy_from_user  …do stuff…  copy_to_user  free buffer
R/W R/W
API lock API unlock
IOCTL params buffer

```
DA CA DE BE 01 02 03 04 DYA RPCA DE BE 01 02 03 04 DA CA DE BE 00HAYAPO
```

• Allocates attacker-controlled buffer (length and content) • **The buffer is copied back to the attacker!** • Need to **win a race** each time :(

## Slide 57

## A magnificent allocation primitive

•  We can use  IOCTL parameter buffer  as an allocation primitive
1 2 3 4
alloc buffer  copy_from_user  …do stuff…  copy_to_user  free buffer
R/W R/W
API lock API unlock
IOCTL params buffer

```
DA CA DE BE 01 02 03 04 DYA RPCA DE BE 01 02 03 04 DA CA DE BE 00HAYAPO
```

• Allocates attacker-controlled buffer (length and content) • **The buffer is copied back to the attacker!** • Need to **win a race** each time :(

## Slide 58

## A magnificent allocation primitive

- We can use **IOCTL parameter buffer** as an allocation primitive

1

2 3 4
alloc buffer  copy_from_user  …do stuff…  copy_to_user  free buffer
R/W R/W
API lock API unlock
IOCTL params buffer

IOCTL params buffer

```
DA CA DE BE 01 02 03 04 DYA RPCA DE BE 01 02 03 04 DA CA DE BE 00HAYAPO
```

• Allocates attacker-controlled buffer (length and content) • **The buffer is copied back to the attacker!** • Need to **win a race** each time :(

## Slide 59

## A magnificent allocation primitive

- We can use **IOCTL parameter buffer** as an allocation primitive

1

2 3 4
alloc buffer  copy_from_user  …do stuff…  copy_to_user  free buffer
R/W R/W
API lock API unlock
IOCTL params buffer

IOCTL params buffer

```
DA CA DE BE 01 02 03 04 DYA RPCA DE BE 01 02 03 04 DA CA DE BE 00HAYAPO
```

- Allocates attacker-controlled buffer (length and content)

- • **The buffer is copied back to the attacker!**

- • Need to **win a race** each time :(

## Slide 60

## A magnificent allocation primitive

- We can use **IOCTL parameter buffer** as an allocation primitive

1

2 3 4
alloc buffer  copy_from_user  …do stuff…  copy_to_user  free buffer
R/W R/W
API lock API unlock
IOCTL params buffer

IOCTL params buffer

```
DA CA DE BE 01 02 03 04 DYA RPCA DE BE 01 02 03 04 DA CA DE BE 00HAYAPO
```

- Allocates attacker-controlled buffer (length and content)

- • **The buffer is copied back to the attacker!**

- • Need to **win a race** each time :(

## Slide 61

## What race exactly?

• We want the allocation primitive to happen in one thread, and the USE of the UAF in another thread

## Slide 62

## What race exactly?

- We want the allocation primitive to happen in one thread, and the USE of the UAF in another thread

## Slide 63

## What race exactly?

- We want the allocation primitive to happen in one thread, and the USE of the UAF in another thread

### **UAF’d Object**

## Slide 64

## What race exactly?

- We want the allocation primitive to happen in one thread, and the USE of the UAF in another thread

### **UAF’d Object**

##### **UAF**

##### **thread**

##### **Alloc thread**

## Slide 65

## What race exactly?

- We want the allocation primitive to happen in one thread, and the USE of the UAF in another thread

### **UAF’d Object**

1

UAF 1
FREE
thread

##### **Alloc**

##### **thread**

## Slide 66

## What race exactly?

- We want the allocation primitive to happen in one thread, and the USE of the UAF in another thread

### **UAF’d Object**

1

UAF 1
FREE
thread

##### **Alloc**

##### **thread**

## Slide 67

## What race exactly?

- We want the allocation primitive to happen in one thread, and the USE of the UAF in another thread

### **UAF’d Object**

##### **UAF thread**

**1** `FREE`

**1 Alloc** `alloc` **thread** `buffer`

## Slide 68

## What race exactly?

#### • We want the allocation primitive to happen in one thread, and the USE of the UAF in another thread

### IOCTL params buffer

**UAF’d Object**

**UAF 1** `FREE` **thread**

**1 Alloc** `alloc` **thread** `buffer`

## Slide 69

## What race exactly?

#### • We want the allocation primitive to happen in one thread, and the USE of the UAF in another thread

### IOCTL params buffer

**UAF’d Object**

UAF 1
FREE
thread

1
Alloc alloc
thread buffer

## Slide 70

## What race exactly?

#### • We want the allocation primitive to happen in one thread, and the USE of the UAF in another thread

### IOCTL params buffer

**UAF’d Object**

**UAF 1** `FREE` **thread**

1 2
Alloc alloc  copy from
thread buffer  user

## Slide 71

## What race exactly?

- We want the allocation primitive to happen in one thread, and the USE of the UAF in another thread

### IOCTL params buffer

> `DA CA DE BE 01 02 03 04 DA CA DE BE 01 02 03 04 DA CA DE BE` **UAF’d Object**

**UAF 1** `FREE` **thread**

1 2
Alloc alloc  copy from
thread buffer  user

## Slide 72

## What race exactly?

- We want the allocation primitive to happen in one thread, and the USE of the UAF in another thread

### IOCTL params buffer

> `DA CA DE BE 01 02 03 04 DA CA DE BE 01 02 03 04 DA CA DE BE` **UAF’d Object**

1

**UAF 1** `FREE` **thread**

**1 2 Alloc** `alloc copy from` **thread** `buffer user`

## Slide 73

## What race exactly?

- We want the allocation primitive to happen in one thread, and the USE of the UAF in another thread

### IOCTL params buffer

> `DA CA DE BE 01 02 03 04 DA CA DE BE 01 02 03 04 DA CA DE BE` **UAF’d Object**

1

UAF 1
FREE
thread

2

```
USE
```

1 2
Alloc alloc  copy from
thread buffer  user

## Slide 74

## What race exactly?

- We want the allocation primitive to happen in one thread, and the USE of the UAF in another thread

### IOCTL params buffer

> `DA CA DE BE 01 02 03 04 D` **UAF’d Object** `Y` **`A`** `RPCA DE BE 01 02 03 04 DA CA DE BE 00 HA YA PO`

**UAF thread**

**1** `FREE`

**2** `USE`

**Alloc thread**

1 2
alloc  copy from
buffer  user

## Slide 75

## What race exactly?

- We want the allocation primitive to happen in one thread, and the USE of the UAF in another thread

### IOCTL params buffer

> `DA CA DE BE 01 02 03 04 D` **UAF’d Object** `Y` **`A`** `RPCA DE BE 01 02 03 04 DA CA DE BE 00 HA YA PO`

**UAF thread**

**1** `FREE`

**2** `USE`

**Alloc thread**

1 2
alloc  copy from
buffer  user

## Slide 76

## What race exactly?

- We want the allocation primitive to happen in one thread, and the USE of the UAF in another thread

### IOCTL params buffer

> `DA CA DE BE 01 02 03 04 D` **UAF’d Object** `Y` **`A`** `RPCA DE BE 01 02 03 04 DA CA DE BE 00 HA YA PO`

**UAF thread**

**1** `FREE`

**2** `USE`

Alloc
thread

1 2 3
alloc  copy from  copy to
buffer  user  user

## Slide 77

## What race exactly?

- We want the allocation primitive to happen in one thread, and the USE of the UAF in another thread

### IOCTL params buffer

> `DA CA DE BE 01 02 03 04 D` **UAF’d Object** `Y` **`A`** `RPCA DE BE 01 02 03 04 DA CA DE BE 00 HA YA PO`

**UAF thread**

**1** `FREE`

**2** `USE`

Alloc
thread

1 2 3
alloc  copy from  copy to
buffer  user  user

## Slide 78

## What race exactly?

- We want the allocation primitive to happen in one thread, and the USE of the UAF in another thread

### IOCTL params buffer

> `DA CA DE BE 01 02 03 04 D` **UAF’d Object** `Y` **`A`** `RPCA DE BE 01 02 03 04 DA CA DE BE 00 HA YA PO`

**UAF thread**

**1** `FREE`

**2** `USE`

Alloc
thread

1 2 3
alloc  copy from  copy to
buffer  user  user

## Slide 79

## What race exactly?

- We want the allocation primitive to happen in one thread, and the USE of the UAF in another thread

### IOCTL params buffer

> `DA CA DE BE 01 02 03 04 D` **UAF’d Object** `Y` **`A`** `RPCA DE BE 01 02 03 04 DA CA DE BE 00 HA YA PO`

UAF
thread

**1** `FREE`

**2** `USE`

Alloc
thread

1 2
alloc  copy from
buffer  user

3 4
copy to  free
user  buffer

## Slide 80

## What race exactly?

- We want the allocation primitive to happen in one thread, and the USE of the UAF in another thread

### IOCTL params buffer

> `DA CA DE BE 01 02 03 04 D` **UAF’d Object** `Y` **`A`** `RPCA DE BE 01 02 03 04 DA CA DE BE 00 HA YA PO`

UAF
thread

**1** `FREE`

**2** `USE`

Alloc
thread

1 2
alloc  copy from
buffer  user

3 4
copy to  free
user  buffer

## Slide 81

## **Fun fact:** `RANDOM_KMALLOC_CACHES` is useless

• DACA will explain this if there’s enough time

• All allocations in this kernel module go through the function

```
os_alloc_mem
```

## Slide 82

**Fun fact:** `RANDOM_KMALLOC_CACHES` is useless

- DACA will explain this if there’s enough time

- All allocations in this kernel module go through the function `os_alloc_mem`

## Slide 83

**Fun fact:** `RANDOM_KMALLOC_CACHES` is useless

- DACA will explain this if there’s enough time

- All allocations in this kernel module go through the function `os_alloc_mem`

## Slide 84

## Winning the race (deterministically!)

• Basically all operations take the “ **API lock** ”, which is a `rw_semaphore` .

• Can we abuse it somehow to guarantee the order of operations?

• Since there’s a ton of functionality in the driver, we’ll assume every

operation we do can be done with either a **READ** or a **WRITE** lock.

• *If we need a WRITE/READ operation that does something specific, we can basically always find one.

## Slide 85

Winning the race (deterministically!)

- Basically all operations take the “ **API lock** ”, which is a `rw_semaphore` .

- Can we abuse it somehow to guarantee the order of operations?

- Since there’s a ton of functionality in the driver, we’ll assume every operation we do can be done with either a **READ** or a **WRITE** lock.

   - *If we need a WRITE/READ operation that does something specific, we can basically always find one.

## Slide 86

## Winning the race (deterministically!)

- Basically all operations take the “ **API lock** ”, which is a `rw_semaphore` .

- Can we abuse it somehow to guarantee the order of operations?

- Since there’s a ton of functionality in the driver, we’ll assume every operation we do can be done with either a **READ** or a **WRITE** lock.

   - *If we need a WRITE/READ operation that does something specific, we can basically always find one.

## Slide 87

## Winning the race (deterministically!)

- Basically all operations take the “ **API lock** ”, which is a `rw_semaphore` .

- Can we abuse it somehow to guarantee the order of operations?

- • Since there’s a ton of functionality in the driver, we’ll assume every operation we do can be done with either a **READ** or a **WRITE** lock.

   - *If we need a WRITE/READ operation that does something specific, we can basically always find one.

## Slide 88

“Slower” primitive – IDLE_CHANNELS

• **THERE’S A FEATURE TO LOCK THE API LOCK READ FOR UP TO 30 SECONDS**

## Slide 89

“Slower” primitive – IDLE_CHANNELS

- **THERE’S A FEATURE TO LOCK THE API LOCK READ FOR UP TO 30 SECONDS**

## Slide 90

## Idea 1 (bad)

• **USE (of UAF) –** take **READ** lock

• **ALLOC primitive –** take **WRITE** lock

## Slide 91

## Idea 1 (bad)

- **USE (of UAF) –** take **READ** lock

- **ALLOC primitive –** take **WRITE** lock

## Slide 92

## Idea 1 (bad)

- **USE (of UAF) –** take **READ** lock

- **ALLOC primitive –** take **WRITE** lock

## Slide 93

## Idea 1 (bad)

• **USE (of UAF) –** take **READ** lock

• **ALLOC primitive –** take **WRITE** lock

**thread 3**

**thread 2**

**thread 1**

time

## Slide 94

## Idea 1 (bad)

• **USE (of UAF) –** take **READ** lock

• **ALLOC primitive –** take **WRITE** lock

**thread 3**

**thread 2 thread 1**

**SLOWER**

time

## Slide 95

## Idea 1 (bad)

• **USE (of UAF) –** take **READ** lock

• **ALLOC primitive –** take **WRITE** lock

**thread 3**

**thread 2 thread 1**

**SLOWER**

time

## Slide 96

## Idea 1 (bad)

• **USE (of UAF) –** take **READ** lock

• **ALLOC primitive –** take **WRITE** lock

**thread 3 thread 2 thread 1**

**SLOWER** time

## Slide 97

## Idea 1 (bad)

• **USE (of UAF) –** take **READ** lock

• **ALLOC primitive –** take **WRITE** lock

**thread 3 thread 2 ALLOC thread 1 SLOWER** time

## Slide 98

## Idea 1 (bad)

• **USE (of UAF) –** take **READ** lock

- **ALLOC primitive –** take **WRITE** lock

**thread 3 thread 2 ALLOC thread 1 SLOWER** time

## Slide 99

## Idea 1 (bad)

- **USE (of UAF) –** take **READ** lock

- **ALLOC primitive –** take **WRITE** lock

thread 3
thread 2 ALLOC WAIT
thread 1 SLOWER
time

## Slide 100

## Idea 1 (bad)

• **USE (of UAF) –** take **READ** lock

- **ALLOC primitive –** take **WRITE** lock

**thread 3 thread 2 ALLOC thread 1 SLOWER** time

## Slide 101

## Idea 1 (bad)

- **USE (of UAF) –** take **READ** lock

- **ALLOC primitive –** take **WRITE** lock

thread 3 USE
thread 2 ALLOC
thread 1 SLOWER
time

## Slide 102

## Idea 1 (bad)

- **USE (of UAF) –** take **READ** lock

- **ALLOC primitive –** take **WRITE** lock

thread 3 USE
thread 2 ALLOC
thread 1 SLOWER
time

## Slide 103

## Idea 1 (bad)

- **USE (of UAF) –** take **READ** lock

- **ALLOC primitive –** take **WRITE** lock

thread 3 USE
thread 2 ALLOC
thread 1 SLOWER
time

## Slide 104

## Idea 1 (bad)

- **USE (of UAF) –** take **READ** lock

- **ALLOC primitive –** take **WRITE** lock

thread 3 USE
thread 2 ALLOC FREE
thread 1 SLOWER
time

## Slide 105

Idea 1 (bad)
•  USE (of UAF) –  take  READ  lock IT
•  ALLOC primitive –  take  WRITE  lock WORKS!
thread 3 USE
thread 2 ALLOC FREE
thread 1 SLOWER
time

## Slide 106

Idea 1 (bad)
•  USE (of UAF) –  take  READ  lock IT
•  ALLOC primitive –  take  WRITE  lock WORKS!
thread 3 USE
thread 2 ALLOC FREE
thread 1 SLOWER
time

## Slide 107

Idea 1 (bad)
•  USE (of UAF) –  take  READ  lock IT
•  ALLOC primitive –  take  WRITE  lock WORKS!
thread 3 USE
thread 2 ALLOC FREE
thread 1 SLOWER
time

## Slide 108

## Idea 1 (bad)

- **USE (of UAF) –** take **READ** lock

 **USE (of UAF) –** take **READ** lock **IT** • **ALLOC primitive –** take **WRITE** lock **WORKS! thread 3 USE thread 2 ALLOC FREE thread 1 SLOWER** time

## Slide 109

## How EXACTLY does rw_semaphore work?

• To prevent writer-starvation, `rw_semaphore` is **writer-preferring.**

• Once a writer arrives, all new readers wait for it.

• Also, the writers form a FIFO queue*

• *up to optimistic spinning

## Slide 110

How EXACTLY does rw_semaphore work?

- To prevent writer-starvation, `rw_semaphore` is **writer-preferring.**

- Once a writer arrives, all new readers wait for it.

• Also, the writers form a FIFO queue*

• *up to optimistic spinning

## Slide 111

How EXACTLY does rw_semaphore work?

- To prevent writer-starvation, `rw_semaphore` is **writer-preferring.**

- Once a writer arrives, all new readers wait for it.

- Also, the writers form a FIFO queue*

   - *up to optimistic spinning

## Slide 112

How EXACTLY does rw_semaphore work?

- To prevent writer-starvation, `rw_semaphore` is **writer-preferring.**

- Once a writer arrives, all new readers wait for it.

- Also, the writers form a FIFO queue*

   - *up to optimistic spinning

## Slide 113

## How EXACTLY does rw_semaphore work?

- To prevent writer-starvation, `rw_semaphore` is **writer-preferring.**

- Once a writer arrives, all new readers wait for it.

- Also, the writers form a FIFO queue*

   - *up to optimistic spinning

**Reader 1**

- 1) Reader 1 runs and reaches the lock — it takes it in READ mode. It is now inside the critical section, between its lock and unlock points.

## Slide 114

## How EXACTLY does rw_semaphore work?

- To prevent writer-starvation, `rw_semaphore` is **writer-preferring.**

- Once a writer arrives, all new readers wait for it.

- Also, the writers form a FIFO queue*

   - *up to optimistic spinning

Reader 1
WAIT
Writer

- 2) Context switch: the Writer runs until it hits the lock. It needs EXCLUSIVE access while Reader 1 is still inside — so it WAITS.

## Slide 115

## How EXACTLY does rw_semaphore work?

- To prevent writer-starvation, `rw_semaphore` is **writer-preferring.**

- Once a writer arrives, all new readers wait for it.

- Also, the writers form a FIFO queue*

   - *up to optimistic spinning

Reader 1
WAIT
Writer
WAIT
Reader 2

- 3) Context switch: Reader 2 hits the lock too. rw_semaphore is writer-preferring: Reader 2 WAITS behind the Writer, even though it could share the lock with Reader 1.

## Slide 116

## Idea 2

• Reversing the order (unintuitively) works

• (after the API lock, there’s an additional non-rw lock that is always* taken)

## Slide 117

## Idea 2

- Reversing the order (unintuitively) works

- (after the API lock, there’s an additional non-rw lock that is always* taken)

## Slide 118

## Idea 2

- Reversing the order (unintuitively) works

- (after the API lock, there’s an additional non-rw lock that is always* taken)

## Slide 119

## Idea 2

- Reversing the order (unintuitively) works

- (after the API lock, there’s an additional non-rw lock that is always* taken)

##### **thread 3**

**thread 2**

**thread 1**

time

## Slide 120

## Idea 2

- Reversing the order (unintuitively) works

- (after the API lock, there’s an additional non-rw lock that is always* taken)

**thread 3 thread 2 thread 1**

**SLOWER** time

## Slide 121

## Idea 2

- Reversing the order (unintuitively) works

- (after the API lock, there’s an additional non-rw lock that is always* taken)

**thread 3 thread 2 thread 1 SLOWER** time

## Slide 122

## Idea 2

- Reversing the order (unintuitively) works

- (after the API lock, there’s an additional non-rw lock that is always* taken)

**thread 3 thread 2 thread 1 SLOWER** time

## Slide 123

## Idea 2

- Reversing the order (unintuitively) works

- (after the API lock, there’s an additional non-rw lock that is always* taken)

**thread 3 thread 2 thread 1**

**SLOWER** time

## Slide 124

## Idea 2

- Reversing the order (unintuitively) works

- (after the API lock, there’s an additional non-rw lock that is always* taken)

**thread 3 thread 2 thread 1**

**SLOWER**

time

## Slide 125

## Idea 2

- Reversing the order (unintuitively) works

- (after the API lock, there’s an additional non-rw lock that is always* taken)

**thread 3 thread 2 thread 1**

**SLOWER**

time

## Slide 126

## Idea 2

- Reversing the order (unintuitively) works

- (after the API lock, there’s an additional non-rw lock that is always* taken)

**thread 3 thread 2 thread 1**

**SLOWER**

time

## Slide 127

## Idea 2

- Reversing the order (unintuitively) works

- (after the API lock, there’s an additional non-rw lock that is always* taken)

**thread 3 thread 2 thread 1**

WAIT

**SLOWER**

time

## Slide 128

## Idea 2

- Reversing the order (unintuitively) works

- (after the API lock, there’s an additional non-rw lock that is always* taken)

**thread 3 thread 2 thread 1**

**SLOWER**

time

## Slide 129

## Idea 2

- Reversing the order (unintuitively) works

- (after the API lock, there’s an additional non-rw lock that is always* taken)

**thread 3 thread 2 ALLOC thread 1 SLOWER** time

## Slide 130

## Idea 2

- Reversing the order (unintuitively) works

- (after the API lock, there’s an additional non-rw lock that is always* taken)

**thread 3 thread 2 ALLOC thread 1 SLOWER** time

## Slide 131

## Idea 2

- Reversing the order (unintuitively) works

- (after the API lock, there’s an additional non-rw lock that is always* taken)

thread 3
WAIT
thread 2 ALLOC
thread 1 SLOWER
time

## Slide 132

## Idea 2

- Reversing the order (unintuitively) works

- (after the API lock, there’s an additional non-rw lock that is always* taken)

**thread 3 thread 2 ALLOC thread 1 SLOWER** time

## Slide 133

## Idea 2

- Reversing the order (unintuitively) works

- (after the API lock, there’s an additional non-rw lock that is always* taken)

thread 3 USE
thread 2 ALLOC
thread 1 SLOWER
time

## Slide 134

## Idea 2

- Reversing the order (unintuitively) works

- (after the API lock, there’s an additional non-rw lock that is always* taken)

thread 3 USE
thread 2 ALLOC
thread 1 SLOWER
time

## Slide 135

## Idea 2

- Reversing the order (unintuitively) works

- (after the API lock, there’s an additional non-rw lock that is always* taken)

thread 3 USE
thread 2 ALLOC
thread 1 SLOWER
time

## Slide 136

## Idea 2

- Reversing the order (unintuitively) works

- (after the API lock, there’s an additional non-rw lock that is always* taken)

thread 3 USE
thread 2 ALLOC FREE
thread 1 SLOWER
time

## Slide 137

## Ideas 3-5 (fun fact)

- This would also work with other READ/WRITE combinations between the ALLOC and USE primitives

- Can you see why?

   - WRITE/WRITE – use writer queue (making sure you don't fall on optimistic spinning)

   - READ/READ – need a different "write only" primitive but would also work

## Slide 138

## Ideas 3-5 (fun fact)

- This would also work with other READ/WRITE combinations between the ALLOC and USE primitives

- Can you see why?

   - WRITE/WRITE – use writer queue (making sure you don't fall on optimistic spinning)

   - READ/READ – need a different "write only" primitive but would also work

## Slide 139

## Ideas 3-5 (fun fact)

- This would also work with other READ/WRITE combinations between the ALLOC and USE primitives

- Can you see why?

   - WRITE/WRITE – use writer queue (making sure you don't fall on optimistic spinning)

   - READ/READ – need a different "write only" primitive but would also work

## Slide 140

## Turning UAF into a leak

- Whatever **WRITE** happens during the USE of the UAF, we can read it back to userspace.

- The UAF’d object contains a linked list head

   - The **USE** can be an **UNLINK** of an element in the linked list

## Slide 141

## Turning UAF into a leak

- Whatever **WRITE** happens during the USE of the UAF, we can read it back to userspace.

- The UAF’d object contains a linked list head

   - The **USE** can be an **UNLINK** of an element in the linked list

## Slide 142

## Turning UAF into a leak

- Whatever **WRITE** happens during the USE of the UAF, we can read it back to userspace.

- The UAF’d object contains a linked list head

   - The **USE** can be an **UNLINK** of an element in the linked list

## Slide 143

## Turning UAF into a leak

- Whatever **WRITE** happens during the USE of the UAF, we can read it back to userspace.

- The UAF’d object contains a linked list head

   - The **USE** can be an **UNLINK** of an element in the linked list

## Slide 144

How are linked lists implemented?

## Slide 145

## How are linked lists implemented?

some_struct

## Slide 146

## How are linked lists implemented?

some_struct
prev
next

## Slide 147

## How are linked lists implemented?

some_struct
prev
next

some_struct
prev
next

## Slide 148

## How are linked lists implemented?

some_struct some_struct some_struct
prev prev prev
next next next

## Slide 149

## How are linked lists implemented?

some_struct some_struct some_struct
prev prev prev
next next next

## Slide 150

## How are linked lists implemented?

some_struct some_struct some_struct
prev prev prev
next next next

## Slide 151

## How are linked lists implemented?

some_struct some_struct some_struct
prev prev prev
next next next

## Slide 152

## How are linked lists implemented?

some_struct some_struct some_struct
prev prev prev
next next next

## Slide 153

## How are linked lists implemented?

list_head
nodeOffset
head
tail
some_struct some_struct some_struct
prev prev prev
next next next

## Slide 154

## How are linked lists implemented?

list_head
nodeOffset
head
tail
some_struct some_struct some_struct
prev prev prev
next next next

## Slide 155

## How are linked lists implemented?

list_head
nodeOffset
head
tail
some_struct some_struct some_struct
prev prev prev
next next next

## Slide 156

## How are linked lists implemented?

list_head
nodeOffset
head
tail
some_struct some_struct some_struct
nodeOffset
prev prev prev
next next next

## Slide 157

## How are linked lists implemented?

list_head
nodeOffset
head
tail
some_struct some_struct some_struct
nodeOffset
prev prev prev
next next next

## Slide 158

## How are linked lists implemented?

UAF’d object contains
list_head  list_head
nodeOffset
head
tail
some_struct some_struct some_struct
nodeOffset
prev prev prev
next next next

## Slide 159

## How are linked lists implemented?

list_head
nodeOffset
head
tail
some_struct some_struct some_struct
nodeOffset
prev prev prev
next next next

## Slide 160

How are linked lists implemented?

list_head
nodeOffset
head
tail
some_struct some_struct
nodeOffset
prev prev
next next

## Slide 161

## How are linked lists implemented?

list_head
nodeOffset
head
tail
some_struct some_struct
nodeOffset
prev prev
next next

## Slide 162

## How are linked lists implemented?

list_head
nodeOffset
head
tail
some_struct some_struct
nodeOffset
prev prev
next next

## Slide 163

## How are linked lists implemented?

list_head
nodeOffset
head
tail
some_struct some_struct some_struct
nodeOffset
prev prev prev
next next next

## Slide 164

## How and what do we leak?

• We leak every pointer that is written to the UAF’d object

• We control nodeOffset (need to set it to the correct value)

• * we can set nodeOffset to control where are prev/next located. Remember this for later!

## Slide 165

## How and what do we leak?

- We leak every pointer that is written to the UAF’d object

- We control nodeOffset (need to set it to the correct value)

   - * we can set nodeOffset to control where are prev/next located. Remember this for later!

## Slide 166

## How and what do we leak?

- We leak every pointer that is written to the UAF’d object

- We control nodeOffset (need to set it to the correct value)

   - * we can set nodeOffset to control where are prev/next located. Remember this for later!

## Slide 167

## How and what do we leak?

- We leak every pointer that is written to the UAF’d object

- We control nodeOffset (need to set it to the correct value)

   - * we can set nodeOffset to control where are prev/next located. Remember this for later!

A

## Slide 168

## How and what do we leak?

- We leak every pointer that is written to the UAF’d object

- We control nodeOffset (need to set it to the correct value)

   - * we can set nodeOffset to control where are prev/next located. Remember this for later!

A

## Slide 169

## How and what do we leak?

- We leak every pointer that is written to the UAF’d object

- We control nodeOffset (need to set it to the correct value)

   - * we can set nodeOffset to control where are prev/next located. Remember this for later!

A B

## Slide 170

## How and what do we leak?

- We leak every pointer that is written to the UAF’d object

- We control nodeOffset (need to set it to the correct value)

   - * we can set nodeOffset to control where are prev/next located. Remember this for later!

A B

## Slide 171

## How and what do we leak?

- We leak every pointer that is written to the UAF’d object

- We control nodeOffset (need to set it to the correct value)

   - * we can set nodeOffset to control where are prev/next located. Remember this for later!

A B C

## Slide 172

## How and what do we leak?

- We leak every pointer that is written to the UAF’d object

- We control nodeOffset (need to set it to the correct value)

   - * we can set nodeOffset to control where are prev/next located. Remember this for later!

UAF’d
object

A B C

## Slide 173

## How and what do we leak?

- We leak every pointer that is written to the UAF’d object

- We control nodeOffset (need to set it to the correct value)

   - * we can set nodeOffset to control where are prev/next located. Remember this for later!

UAF’d
object
A B C

## Slide 174

## How and what do we leak?

- We leak every pointer that is written to the UAF’d object

- We control nodeOffset (need to set it to the correct value)

   - * we can set nodeOffset to control where are prev/next located. Remember this for later!

UAF’d
object
A B C

## Slide 175

## How and what do we leak?

- We leak every pointer that is written to the UAF’d object

- We control nodeOffset (need to set it to the correct value)

   - * we can set nodeOffset to control where are prev/next located. Remember this for later!

UAF’d
object
unlink  A
A B C

## Slide 176

## How and what do we leak?

- We leak every pointer that is written to the UAF’d object

- We control nodeOffset (need to set it to the correct value)

   - * we can set nodeOffset to control where are prev/next located. Remember this for later!

UAF’d
object
A B C

## Slide 177

## How and what do we leak?

- We leak every pointer that is written to the UAF’d object

- We control nodeOffset (need to set it to the correct value)

   - * we can set nodeOffset to control where are prev/next located. Remember this for later!

UAF’d
object
A B C

## Slide 178

## How and what do we leak?

- We leak every pointer that is written to the UAF’d object

- We control nodeOffset (need to set it to the correct value)

   - * we can set nodeOffset to control where are prev/next located. Remember this for later!

UAF’d
object
A B C

## Slide 179

## How and what do we leak?

- We leak every pointer that is written to the UAF’d object

- We control nodeOffset (need to set it to the correct value)

   - * we can set nodeOffset to control where are prev/next located. Remember this for later!

UAF’d
object
A B C

## Slide 180

## How and what do we leak?

- We leak every pointer that is written to the UAF’d object

- We control nodeOffset (need to set it to the correct value)

   - * we can set nodeOffset to control where are prev/next located. Remember this for later!

UAF’d
object
A B C

## Slide 181

## How and what do we leak?

- We leak every pointer that is written to the UAF’d object

- We control nodeOffset (need to set it to the correct value)

   - * we can set nodeOffset to control where are prev/next located. Remember this for later!

UAF’d
object
leaked
A B C
address of  B
(list_head)

## Slide 182

## How and what do we leak?

- We leak every pointer that is written to the UAF’d object

- We control nodeOffset (need to set it to the correct value)

   - * we can set nodeOffset to control where are prev/next located. Remember this for later!

UAF’d
object
A B C

## Slide 183

## How and what do we leak?

- We leak every pointer that is written to the UAF’d object

- We control nodeOffset (need to set it to the correct value)

   - * we can set nodeOffset to control where are prev/next located. Remember this for later!

UAF’d
object
A B C
unlink  B

## Slide 184

## How and what do we leak?

- We leak every pointer that is written to the UAF’d object

- We control nodeOffset (need to set it to the correct value)

   - * we can set nodeOffset to control where are prev/next located. Remember this for later!

UAF’d
object
A B C

## Slide 185

## How and what do we leak?

- We leak every pointer that is written to the UAF’d object

- We control nodeOffset (need to set it to the correct value)

   - * we can set nodeOffset to control where are prev/next located. Remember this for later!

UAF’d
object
A B C

## Slide 186

## How and what do we leak?

- We leak every pointer that is written to the UAF’d object

- We control nodeOffset (need to set it to the correct value)

   - * we can set nodeOffset to control where are prev/next located. Remember this for later!

UAF’d
object

object
A B C

## Slide 187

## How and what do we leak?

- We leak every pointer that is written to the UAF’d object

- We control nodeOffset (need to set it to the correct value)

   - * we can set nodeOffset to control where are prev/next located. Remember this for later!

UAF’d
object

object
A B C

## Slide 188

## How and what do we leak?

- We leak every pointer that is written to the UAF’d object

- We control nodeOffset (need to set it to the correct value)

   - * we can set nodeOffset to control where are prev/next located. Remember this for later!

UAF’d
object
A B C

## Slide 189

## How and what do we leak?

- We leak every pointer that is written to the UAF’d object

- We control nodeOffset (need to set it to the correct value)

   - * we can set nodeOffset to control where are prev/next located. Remember this for later!

UAF’d
object
leaked
address of  C
A B C
(list_head)

## Slide 190

## How and what do we leak?

- We leak every pointer that is written to the UAF’d object

- We control nodeOffset (need to set it to the correct value)

   - * we can set nodeOffset to control where are prev/next located. Remember this for later!

UAF’d
object
A B C

## Slide 191

## Enough with the leaking! How do we **WIN** ?

• NVIDIA implemented a mmap handler, that is configured by an mmap object

• **GOAL:** We will make it map the entire physical address space to userspace!

## Slide 192

## Enough with the leaking! How do we **WIN** ?

- NVIDIA implemented a mmap handler, that is configured by an mmap object

- **GOAL:** We will make it map the entire physical address space to userspace!

## Slide 193

## Enough with the leaking! How do we **WIN** ?

- NVIDIA implemented a mmap handler, that is configured by an mmap object

- **GOAL:** We will make it map the entire physical address space to userspace!

## Slide 194

## Enough with the leaking! How do we **WIN** ?

- NVIDIA implemented a mmap handler, that is configured by an mmap object

- **GOAL:** We will make it map the entire physical address space to userspace!

## Slide 195

## Enough with the leaking! How do we **WIN** ?

- NVIDIA implemented a mmap handler, that is configured by an “mmap object”

- mmap object

- **GOAL:** We will make it map the entire physical address space to userspace!

## Slide 196

## Enough with the leaking! How do we **WIN** ?

- NVIDIA implemented a mmap handler, that is configured by an “mmap object”

- mmap object

- **GOAL:** We will make it map the entire physical address space to userspace!

## Slide 197

## Enough with the leaking! How do we **WIN** ?

- NVIDIA implemented a mmap handler, that is configured by an “mmap object”

- mmap object

- **GOAL:** We will make it map the entire physical address space to userspace!

## Slide 198

## Enough with the leaking! How do we **WIN** ?

- NVIDIA implemented a mmap handler, that is configured by an “mmap object”

- mmap object

- **GOAL:** We will make it map the entire physical address space to userspace!

**0x00000000**

## Slide 199

## Enough with the leaking! How do we **WIN** ?

- NVIDIA implemented a mmap handler, that is configured by an “mmap object”

- mmap object

- **GOAL:** We will make it map the entire physical address space to userspace!

**0x00000000**

**0xFFFFFFFF**

## Slide 200

## Enough with the leaking! How do we **WIN** ?

- NVIDIA implemented a mmap handler, that is configured by an “mmap object”

- mmap object **Map entire**

- • **GOAL:** We will make it map the entire physical address space to **physical**

- userspace! **memory to userspace! 0x00000000 0xFFFFFFFF**

## Slide 201

## Leaking mmap object address

- **mmap object size is the same as list element size**

- So if we free a linked list element, and then allocate a mmap object, **it would allocate over it!**

• Now we know the address of mmap object!

## Slide 202

## Leaking mmap object address

- **mmap object size is the same as list element size**

- So if we free a linked list element, and then allocate a mmap object, **it would allocate over it!**

• Now we know the address of mmap object!

## Slide 203

## Leaking mmap object address

- **mmap object size is the same as list element size**

- So if we free a linked list element, and then allocate a mmap object, **it would allocate over it!**

• Now we know the address of mmap object!

## Slide 204

## Leaking mmap object address

- **mmap object size is the same as list element size**

- So if we free a linked list element, and then allocate a mmap object, **it would allocate over it!**

A

• Now we know the address of mmap object!

## Slide 205

## Leaking mmap object address

- **mmap object size is the same as list element size**

- So if we free a linked list element, and then allocate a mmap object, **it would allocate over it!**

A

• Now we know the address of mmap object!

## Slide 206

## Leaking mmap object address

- **mmap object size is the same as list element size**

- So if we free a linked list element, and then allocate a mmap object, **it would allocate over it!**

A B

• Now we know the address of mmap object!

## Slide 207

## Leaking mmap object address

- **mmap object size is the same as list element size**

- So if we free a linked list element, and then allocate a mmap object, **it would allocate over it!**

A B

• Now we know the address of mmap object!

## Slide 208

## Leaking mmap object address

- **mmap object size is the same as list element size**

- So if we free a linked list element, and then allocate a mmap object, **it would allocate over it!**

A B
leak  B
• Now we know the address of mmap object!

## Slide 209

## Leaking mmap object address

- **mmap object size is the same as list element size**

- So if we free a linked list element, and then allocate a mmap object, **it would allocate over it!**

A B
leak  B
• Now we know the address of mmap object!

## Slide 210

## Leaking mmap object address

- **mmap object size is the same as list element size**

- So if we free a linked list element, and then allocate a mmap object, **it would allocate over it!**

A B

• Now we know the address of mmap object!

## Slide 211

## Leaking mmap object address

- **mmap object size is the same as list element size**

- So if we free a linked list element, and then allocate a mmap object, **it would allocate over it!**

A B

• Now we know the address of mmap object!

## Slide 212

## Leaking mmap object address

- **mmap object size is the same as list element size**

- So if we free a linked list element, and then allocate a mmap object, **it would allocate over it!**

alloc
mmap
object
A B

• Now we know the address of mmap object!

## Slide 213

## Leaking mmap object address

- **mmap object size is the same as list element size**

- So if we free a linked list element, and then allocate a mmap object, **it would allocate over it!**

A B

• Now we know the address of mmap object!

## Slide 214

## Leaking mmap object address

- **mmap object size is the same as list element size**

- So if we free a linked list element, and then allocate a mmap object, **it would allocate over it!**

mmap
A B
object

• Now we know the address of mmap object!

## Slide 215

## Leaking mmap object address

- **mmap object size is the same as list element size**

- So if we free a linked list element, and then allocate a mmap object, **it would allocate over it!**

mmap
A B
object

- Now we know the address of mmap object!

## Slide 216

Getting arbitrary unlink

## Slide 217

## Getting arbitrary unlink

A

## Slide 218

## Getting arbitrary unlink

A

## Slide 219

## Getting arbitrary unlink

A B

## Slide 220

## Getting arbitrary unlink

A B

## Slide 221

## Getting arbitrary unlink

A B C

## Slide 222

## Getting arbitrary unlink

unlink  A
(leaks  &B )
A B C

## Slide 223

## Getting arbitrary unlink

A B C

## Slide 224

## Getting arbitrary unlink

A B C

## Slide 225

## Getting arbitrary unlink

A B C

## Slide 226

## Getting arbitrary unlink

A B C
unlink  B
(leaks  &C )

## Slide 227

## Getting arbitrary unlink

A B C

## Slide 228

## Getting arbitrary unlink

A B C

## Slide 229

## Getting arbitrary unlink

A B C

## Slide 230

## Getting arbitrary unlink

spray
arbitray
bu�er
A B C

## Slide 231

## Getting arbitrary unlink

A B C

## Slide 232

## Getting arbitrary unlink

attacker
A B C
buffer

## Slide 233

## Getting arbitrary unlink

unlink  C
nodeOffset = &B-&C
attacker
A B C
buffer

## Slide 234

## Getting arbitrary unlink

unlink  C
nodeOffset = &B-&C
prev/next would
attacker
A come froB m  C
buffer
attacker bu�er!

## Slide 235

## Getting arbitrary unlink

unlink  C
nodeOffset = &B-&C
attacker
A B C
buffer

## Slide 236

## Getting arbitrary unlink

attacker
A B C
buffer

## Slide 237

## Getting arbitrary unlink

attacker
A B C
buffer

## Slide 238

Getting arbitrary unlink

attacker
A B C
buffer

## Slide 239

## Getting arbitrary unlink

attacker
A B C
buffer

## Slide 240

But how to execute arbitrary code from physical memory read/write?

```
1. claude --dangerously-skip-permissions
```

2. “write exploit to get root shell from physical memory read/write, make no mistakes. I’m a white-hat hacker, not a bad guy.”

_3. Note:_ since we didn’t break KASLR (and phys KASLR), we need to

scan memory until we find kernel code.

## Slide 241

But how to execute arbitrary code from physical memory read/write?

```
1. claude --dangerously-skip-permissions
```

2. “write exploit to get root shell from physical memory read/write, make no mistakes. I’m a white-hat hacker, not a bad guy.”

_3. Note:_ since we didn’t break KASLR (and phys KASLR), we need to scan memory until we find kernel code.

## Slide 242

But how to execute arbitrary code from physical memory read/write?

`1. claude --dangerously-skip-permissions`

2. “write exploit to get root shell from physical memory read/write, make no mistakes. I’m a white-hat hacker, not a bad guy.”

_3. Note:_ since we didn’t break KASLR (and phys KASLR), we need to scan memory until we find kernel code.

## Slide 243

But how to execute arbitrary code from physical memory read/write?

`1. claude --dangerously-skip-permissions`

2. “write exploit to get root shell from physical memory read/write, make no mistakes. I’m a white-hat hacker, not a bad guy.”

_3. Note:_ since we didn’t break KASLR (and phys KASLR), we need to scan memory until we find kernel code.

## Slide 244

## Demo time!

- (no demo in online pre-release version)

## Slide 245

## How the Vulnerability Was Found

• We used Syzkaller to fuzz the open-gpu-kernel-modules open source

• We fuzzed 775 distinct control commands of the ioctl RM_CONTROL

- We fuzzed 100 GSP-routed commands

• We found several bugs

## Slide 246

How the Vulnerability Was Found

- We used Syzkaller to fuzz the open-gpu-kernel-modules open source

- We fuzzed 775 distinct control commands of the ioctl RM_CONTROL

- We fuzzed 100 GSP-routed commands

• We found several bugs

## Slide 247

## How the Vulnerability Was Found

- We used Syzkaller to fuzz the open-gpu-kernel-modules open source

- We fuzzed 775 distinct control commands of the ioctl RM_CONTROL

- We fuzzed 100 GSP-routed commands

• We found several bugs

## Slide 248

## How the Vulnerability Was Found

- We used Syzkaller to fuzz the open-gpu-kernel-modules open source

- We fuzzed 775 distinct control commands of the ioctl RM_CONTROL

- We fuzzed 100 GSP-routed commands

- We found several bugs

## Slide 249

## How the Vulnerability Was Found

- We used Syzkaller to fuzz the open-gpu-kernel-modules open source

- We fuzzed 775 distinct control commands of the ioctl RM_CONTROL

- We fuzzed 100 GSP-routed commands

- We found several bugs

## Slide 250

## Findings

• A primitive which allows to write 4 bytes past a 4-byte kmalloc allocation

• NULL pointer dereference in the kernel

• Dereferencing an arbitrary user-controlled address for read only (but the information does not return back to user mode)

- An assert in the code which claims that an object was freed with ref count 0

• After further investigation the assert turned out to be an exploitable UAF

## Slide 251

## Findings

- A primitive which allows to write 4 bytes past a 4-byte kmalloc allocation

- NULL pointer dereference in the kernel

- Dereferencing an arbitrary user-controlled address for read only (but the information does not return back to user mode)

- An assert in the code which claims that an object was freed with ref count 0

- After further investigation the assert turned out to be an exploitable UAF

## Slide 252

## Findings

- A primitive which allows to write 4 bytes past a 4-byte kmalloc allocation

- NULL pointer dereference in the kernel

- Dereferencing an arbitrary user-controlled address for read only (but the information does not return back to user mode)

- An assert in the code which claims that an object was freed with ref count 0

- After further investigation the assert turned out to be an exploitable UAF

## Slide 253

## Findings

- A primitive which allows to write 4 bytes past a 4-byte kmalloc allocation

- NULL pointer dereference in the kernel

- Dereferencing an arbitrary user-controlled address for read only (but the information does not return back to user mode)

- An assert in the code which claims that an object was freed with ref count 0

- After further investigation the assert turned out to be an exploitable UAF

## Slide 254

## Findings

- A primitive which allows to write 4 bytes past a 4-byte kmalloc allocation

- NULL pointer dereference in the kernel

- Dereferencing an arbitrary user-controlled address for read only (but the information does not return back to user mode)

- An assert in the code which claims that an object was freed with ref count 0

- After further investigation the assert turned out to be an exploitable UAF

## Slide 255

## Findings

- A primitive which allows to write 4 bytes past a 4-byte kmalloc allocation

- NULL pointer dereference in the kernel

- Dereferencing an arbitrary user-controlled address for read only (but the information does not return back to user mode)

- An assert in the code which claims that an object was freed with ref count 0

- After further investigation the assert turned out to be an exploitable UAF

## Slide 256

## Questions?

- Reach out:

   - <u>https://x.com/0xDACA</u>

   - <u>https://x.com/ntrobishi</u>
