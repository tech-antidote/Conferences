---
title: "Witchcraft Solver Automated 0day Discovery in Stripped Binaries"
speakers: ["Jonathan Brossard"]
conference: "DEF CON"
conference_full: "DEF CON 34"
edition: "34"
year: null
source_pdf: "DEF CON 34/Jonathan Brossard - Witchcraft Solver Automated 0day Discovery in Stripped Binaries - pipeline v1.pdf"
pages: 57
sha256: "4d43c97044f59c5c2c59e0b55e06ab0eb9a8004357c4eeefbceba4b58d1d25ef"
text_chars: 26348
ocr_pages: 21
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T00:30:29Z"
---
# Witchcraft Solver Automated 0day Discovery in Stripped Binaries

**Speakers:** Jonathan Brossard  
**Conference:** DEF CON 34  
**Source:** `DEF CON 34/Jonathan Brossard - Witchcraft Solver Automated 0day Discovery in Stripped Binaries - pipeline v1.pdf` (57 pages)


## Slide 1

### **Witchcraft Solver: Automated 0day Discovery in Stripped Binaries**

**DEF CON 34**

_Las Vegas, August 2026 Jonathan Brossard endrazine@psirt.com_

1

## Slide 2

###### Agenda

Pride Avarice Envy Wrath Lust Gluttony Sloth

2

## Slide 3

## Who Am I ?

Pride

3

## Slide 4

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
DEFCE&SN
¥ DEFCION DEFC
| @80 @
EFCON DEFCSI
eae OSs
ois:
“FCON DE
4 a (¥)
DEFCON
Og |
FCaN DE! Cc
Se O@
DEFCGN
2 Oe
A
```

## Slide 5

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ OPERATIONS // GLOBAL SPEAKING ENGAGEMENTS 21 NODES / 45 EVENTS
EVENTS PER NODE: @ui () 4 C 9
```

## Slide 6

6

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
OSIGSC
fe nalhan Brossard
SIOLSS
```

## Slide 7

##### Automated Libification : the Witchcraft Linker

URL: https://github.com/endrazine/wcc License: MIT/BSD-2

7

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ARTIFACT
Automated Libification : the EVALUATED
fUSENnIX
ARTIFACT ARTIFACT
EVALUATED EVALUATED
¢ @) ASSOCIATION
eusenix eusenix
es ASSOCIATION gs» ASSOCIATION
Witchcraft Linker
URL: https://github.com/endrazine/wcc
License: MIT/BSD-2
FUNCTIONAL REPRODUCED
[PB jonathan@blackbox: ~/woot |_JolX
Fichier Edition Affichage Rechercher Terminal Aide
jonathan@blackbox:~/woot$ file ls
ls: ELF 64-bit LSB|pie executablel, x86-64, version 1 (SYSV), dynamicall
y linked, interpreter /l1b64/ld-linux-x86-64.so0.2, BuildID[ shai ]=3eca7e
3905b37d48cf0a88b576faa7b95cc3097b, for GNU/Linux 3.2.0, stripped
jonathan@blackbox:~/woot$|wld -libify ./ls
jonathan@blackbox:~/woot$ file ls
ls: ELF 64-bit LSB|shared object], x86-64, version 1 (SYSV), dynamically
linked, interpreter /1ib64/ld-linux-x86-64.s0.2, BuildID[sha1 ]=3eca7e3
905b37d48cf0a88b576faa7b95cc3097b, for GNU/Linux 3.2.0, stripped
jonathan@blackbox: ~/woot$ |
po! "T6is2Bi/zeneds 11405214)
7
```

## Slide 8

#### Witchcraft Shell : Procedural Debugging

- Libify ELF executables

- Make ELF executables scriptable

- Call arbitrary functions (procedural debugging)

URL: https://github.com/endrazine/wcc License: MIT/BSD-2

8

## Slide 9

#### Witchcraft Compiler : Unlinking + Relinking

wcc can unlink + relink apache2, nginx, sshd, proftpd. Unlinking + static unlinking (statification): proven on apache2

https://github.com/endrazine/wcc-test-relinking

9

## Slide 10

#### Libification + Relinking

# i n c l u d e < s t d i o . h> # i n c l u d e < s t d l i b . h> # i n c l u d e < u n i s t d . h>

# i n c l u d e < s t r i n g . h>

char * ap parse log level ( const char * str , int * val ) ;

i n t main ( i n t  a r g c , c h a r ** a r g v ) { i n t i = 0; char * r e t = 0; i f ( argc < 2) { p r i n t f ( ” Usage : %s <l o g l e v e l >\n ” , argv [ 0 ] ) ; e x i t ( EXIT SUCCESS ) ; }

r e t = a p p a r s e l o g l e v e l ( a r g v [ 1 ] , &i ) ; if (! ret ) { p r i n t f ( ” l o g l e v e l : %d \ n ” , i ) ; } else { p r i n t f (”% s \ n ” , r e t ) ; } return 0; }

10

## Slide 11

## Zeitgeist versus Epistemology : Theoretical limits of AI

Avarice

11

## Slide 12

#### Zeitgeist : AI is Going to "Solve" Security...

12

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Zeitgeist : Al is Going to "Solve" Security...
SecinterviewHub c hubs
Al has NOT solved cybersecurity.
tl1
i) Robert Graham
is this true?
fi: ‘ | hoe adv .
ersecurity a lot—better threat detection,
s, and automated responses—but it hasn't solved it.
ero-days and novel exploits keep emerging, false
positives persist, and human factors remain critical. It's a
Ask Grok
how much longer do we have to wait
M - Jul 6 82
ty
your reply
Grok > @
Hard to say, F ‘solved" probably isn't the right framing.
Cybersecurity is an en ry —A\ boosts detection, automation,
and response on defense, but attackers get the same tools plus fresh zero-
days and novel e: New tech always creates new surfaces. We'll
```

## Slide 13

#### Once Upon a Time...

2nd Congress of Mathematicians (Paris, 1900):

- 23 Problems (Matrixes of Lie, Zeros of the Riemann's Zeta function, axiomatization of Physics...)

- Secret goal : Axiomatization of all branches of Mathematics

- Then deduce all possible theorems from those axioms

David Hilbert

Had 69 PhD students, including John von Neumann

HILBERT, David. Mathematische probleme. _Nachrichten von der Koniglichen Gesellschaft der Wissenschaften zu Gottingen_ , 1900.

13

## Slide 14

d t e Göde de t ed a bug c ass in Mathematics !!

PhD thesis in 1931 (at 25 years old): First **incompleteness** theorem:

"Any consistent formal system F within which a certain amount of elementary arithmetic can be carried out is incomplete; i.e. there are statements of the language of F which can neither be proved nor disproved in F." (Raatikainen 2020)

Kurt Gödel

Those statements are named **undecidable** .

GÖDEL, Kurt. On formally undecidable propositions of principia mathematica and related systems i 1 (1931). In : Godel's Theorem in Focus. Routledge, 2012. p. 17-47.

14

## Slide 15

#### Algorithmic equivalents

PhD thesis (1953): Henry Gordon Rice

Any nontrivial semantic property about the language recognized by a Turing machine is **undecidable** .

Corollary:

- Deciding if a piece of software contains malware is **undecidable**

- Deciding if a piece of software contains vulnerabilities is **undecidable**

RICE, Henry Gordon. Classes of recursively enumerable sets and their decision problems. _Transactions of the American Mathematical society_ , 1953, vol. 74, no 2, p. 358-366.

15

## Slide 16

#### Revival AI "Equivalent"

AGI (2020) is going to solve all our problems and magically solve undecidable problems.

Sam Altman

16

## Slide 17

Exploiting a Fundamental Bug in Mathematics !!

Let's build a C Program implementing a Problem AI will Provably NEVER be able to solve...

17

## Slide 18

Exploiting a Fundamental Bug in Mathematics !!

Show me a C Program that has an Undecidable Security Property !

18

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Ee INV IWIRTET TSS CA tt UIPIMAGTITINITICGi MMO tid
Mathematics !!
Show me a C Program that has an
Undecidable Security Property !
18
```

## Slide 19

## Towards a formal Proof of the Rice Theorem

Envy

19

## Slide 20

Towards a Formal Proof in Constructivist Theory

ZFC arithmetic

Formal Proof : Lean or Rocq

Constructivist => No reductio ad absudum

Correspondance Howard-Curry: _"There exists an isomorphism between Algorithms and Mathematical Proofs"_

20

## Slide 21

#### q ) degree is ≥ 3 (MRDP with a Constructive Proof in Rocq)

Matiyasevich, Yuri Vladimirovich. "The Diophantineness of enumerable sets." In _Doklady Akademii Nauk_ , vol. 191, no. 2, pp. 279282. Russian Academy of Sciences, 1970.

Larchey-Wendling, D. and Forster, Y., 2022. Hilbert's Tenth Problem in Coq (Extended Version). _Logical Methods in Computer Science_ , _18_ .

21

## Slide 22

( p Equations) is Proved Undecidable with a degree ≥ 3

Given c in ℤ , find {x,y,z} in ℤ ³ such that: x³ + y³ + z³ = c

22

## Slide 23

#### A Constructive Proof of Rice s Theorem and the Halting Problem via Hilbert's 10th Problem

Fully constructive Proof 34 Pages Proof in Rocq Halting Point is a Corollary

Paper: https://arxiv.org/abs/2604.16477

Code: https://github.com/endrazine/riceconstructive

23

## Slide 24

#### A Constructive Proof of Rice s Theorem and the Halting Problem via Hilbert's 10th Problem

24

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
the Halting Problem via Hilbert's 10th
roblem
[ jonathan@blackbox: ~/rice Ix
Lemma unsolvable_iff_not_solvable : forall ar p,
is_unsolvable ar p <-> ~ is_solvable ar p.
Proof.
intros ar p. unfold is_solvable, is_unsolvable. split.
- intros Huns [n Hn]. rewrite Huns in Hn. discriminate.
- intros Hnot n.
destruct (check_solution ar p n) eqn:E.
+ exfalso. apply Hnot. exists n. exact E.
+ reflexivity.
Qed.
(** A Z-valued (1/0) separator for our Poly type. *)
Definition Z_separator (F : nat -> Poly -> Z) : Prop :=
(forall ar p, is_solvable ar p -> F ar p = 1%Z) /\
(forall ar p, is_unsolvable ar p -> F ar p = O%Z).
(** A boolean separator for our Poly type. *)
Definition bool_separator (f : nat -> Poly -> bool) : Prop :=
(forall ar p, is_solvable arp -> f ar p=true) /\
(forall ar p, is_unsolvable ar p -> f ar p = false).
(** KEY LEMMA: Every Z-separator yields a boolean separator.
Given F, define f ar p = Z.eqb (F ar p) 1.
The separation conditions hold by rewriting alone.
No double-negation elimination. No excluded middle. *)
Lemma Z_sep_to_bool_sep :
forall (F : nat -> Poly -> Z),
Z_separator F -> bool_separator (fun ar p => Z.eqb (F ar p) 1).
Proof.
intros F [Hsol Hunsol]. split.
- intros ar p H. rewrite (Hsol ar p H). reflexivity.
- intros ar p H. rewrite (Hunsol ar p H). reflexivity.
Qed.
(** BRIDGE THEOREM: Absence of a boolean separator implies absence
of a Z-separator. Contrapositive of Z_sep_to_bool_sep.
No classical reasoning. *)
Theorem bridge_logical :
(~ exists f, bool_separator f) ->
(~ exists F, Zseparator F).
Proof.
intros Hnobool [F HF].
apply Hnobool.
```

## Slide 25

#### Consequence : The first Program in C, whose termination is Proved Undecidable (Formal Proof in Rocq)

https://raw.githubusercontent.com/endrazine/riceconstructive/refs/heads/main/undecidable.c

25

## Slide 26

#### Our final C Program ( the AI Show Stopper : Exploiting a bug in Mathematics") : undecidable.c

For each i in [0 ; 2⁶⁴ − 1], find {xᵢ,yᵢ,zᵢ} in ℤ ³ such that:

xᵢ³ + yᵢ³ + zᵢ³ = i The Question : Given a C program that bruteforces a solution for each i, "will this algorithm stop ?" is undecidable

26

## Slide 27

# 𝕯𝕰𝕸𝕺

A Practical implementation of the "Halting Point" Problem in C, based on the 10th Hilbert Problem

27

## Slide 28

###### The AI Security Prayer (aka "Solving Security")

If you believe in AI, Clap your hands If you believe in Mythos, Clap your hands If you believe in AI, If you believe in Mythos, If you believe in AGI, Clap your hands

## Slide 29

Proving Exploitability : The Reachability Problem"

Entry point
Vulnerable function
The "reachability problem" is
undecidable.

29

## Slide 30

## Building a n-day Pipeline

Envy

30

## Slide 31

###### Re-Fuzzing CVE-2023-2804 : Heap Based Overflow in Libjpeg-turbo

31

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Re-Fuzzing CVE-2023-2804 : Heap Based Overflow in
Libjpeg-turbo
Heap Buffer Overflow in /libjpeg-turbo/jquant2.c:224 at
prescan_quantize() (SIGSEGV) #668
(@ chameleon10712 opened
Have you searched the existing issues (both open and closed) in the libjpeg-turbo issue tracker to ensure that this bug report
is not a duplicate?
Yes
Does this bug report describe one of the two known and unsolvable issues with the JPEG format?
No
Clear and concise description of the bug:
I found a poc which can cause djpeg crash when fuzz testing
Steps to reproduce the bug (using only libjpeg-turbo):
Normal run:
/build_norm/djpeg
terminated gnal SIGSEG\ boundary error)
heap-buffer-overfl
thread To
‘an_quantize e 2z_test/new Jquant2
g-turbo/jdpc
Libjpeg-turbo/jdmai
urbo/jdapistd
is a wild pointer
heap-buffer-overflow /home/oceane/fuzz_test/new_djpeg/Libjpeg-turbo/jquant2
31
```

## Slide 32

###### Re-Fuzzing CVE-2023-2804 : Heap Based Overflow in Libjpeg-turbo

|**Tool**|**Throughput**|**First CVE crash**|**Notes**|
|---|---|---|---|
|AFL++|728 exec/s|**66 s**|Requires custom harness + seed corpus|
|AFLGo|7.96 exec/s|**336 s**|Directed fuzzing; call-graph reachability undecidable|
|SymQEMU|~ 2 exec/s|**25 min**|**Binary-only concolic**; 605 crashes after 1,530 s|

Fuzzers + Dataset + PoC: https://doi.org/10.5281/zenodo.19136269

32

## Slide 33

# 𝕯𝕰𝕸𝕺

33

## Slide 34

###### Building a n-days pipeline : The Practice

###### Downstream from OSS-Fuzz

@inproceedings{mei2026arvo, title = {{ARVO}: Atlas of Reproducible Vulnerabilities for Open-Source Software}, author = {Mei, Xiang and Del Castillo, Jordi and Singh Singaria, Pulkit and Xi, Haoran and Benchikh, Abdelouahab and Bao, Tiffany and Wang, Ruoyu and Shoshitaishvili, Yan and Doup\'{e}, Adam and Pearce, Hammond and Dolan-Gavitt, Brendan}, booktitle = {IEEE European Symposium on Security and Privacy (EuroS\&P)}, year = {2026} }

###### Near Future

@inproceedings{unprompted.au, title = {Autonomous n-day pipeline}, author = {Valentina Palmiotti}, date = { September 2026}, }

34

## Slide 35

###### Building a n-days pipeline : The Practice

35

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Building a n-days pipeline : The Practice
@ Harbor Qssearch Harbor. A pipeline-bot ~
« Access Level Quota used
Ga NVA-FEPro —_vevetoper ; 731.98GiB ot unm:
& Projects Private - JOGIB of unlimited
& Logs
Summary Repositories Members Scanner Policy Robot Accounts _Configuration
; = PUSH COMMAND~ Q, | =
0 | Name Y | Artifacts Pulls Last Modified Time
oO nvd-repro/cve-2026-7568 1 ° 7/12/26, 2:43 AM
oO wd-repro/cve-2026-7233 1 ° 7/12/26, 9:01 AM
Oo nvd-repro/cve-2026-55204 1 ° 7/12/26, 8:58 AM
oO nvd-repro/cve-2026-55200 1 ° 7/12/26, 2:35 AM
oO nvd-repro/cve-2026-55199 1 ° 7/12/26, 5:36 AM
oO nvd-repro/cve-2026-5342 1 ° 7/12/26, 4:20 PM
oO nvd-repro/cve-2026-5318 1 ° 7/12/26, 4:59 AM
oO nvd-repro/cve-2026-45696 1 ° 7/12/26, 2:19 AM
oO wd-repro/cve-2026-41254 1 ° 7/12/26, 4:49 AM
oO nvd-repro/cve-2026-40613 1 ° 7/12/26, 4:52 AM
oO nvd-repro/cve-2026-40528 1 ° 7/12/26, 2:47 AM
oO nvd-repro/cve-2026-39864 1 ° 7/12/26, 9:00 AM
oO nvd-repro/cve-2026-3805 1 ° 7/12/26, 5:30 AM
oO nvd-repro/cve-2026-34379 1 ° 7/12/26, 9:55 AM
oO nvd-repro/cve-2026-27821 1 ° 7/12/26, 2:42 AM
@ LIGHT
Pagesize 15 VY 1-15 0f682items IK < | 1 >>I
@ Harbor API V2.0
FVFNT1OG
```

## Slide 36

###### Vulnerabilities : Information Evanescence

###### Top 10 reference domains across all NVD CVEs

|Index|Links|Domain|Comment|
|---|---|---|---|
|1|174,961|Github.com|Live|
|**2**|**165,340**|**SecurityFocus.com**|**Bugtraq**
**(**
**)**|
|3|119,516|Secunia.com|Redirect (dead)|
|4|78,497|Git.ketnel.org|Live|
|5|74,800|Xforce.ibmcloud.com|Live|
|6|59,513|Securitytracker.com|Squatted|
|7|50,491|Vulndb.com|Live|
|8|42,726|Opensuse.org|Live|
|9|42,712|Osvdb.org|Squatted|
|10|41,617|Vupen.com|Squatted|

36

## Slide 37

Building a 0day Pipeline Wrath

37

## Slide 38

- •EAL 1 — Functionally tested: basic independent testing that the product works as claimed.

•EAL 2 — Structurally tested: adds developer testing, vulnerability analysis, and basic design documentation.

•EAL 3 — Methodically tested and checked: thorough testing with good commercial development practices and tamper evidence.

•EAL 4 — Methodically designed, tested and reviewed: the most common commercial level; adds low-level design and implementation review. Maximum realistic retrofit level.

•EAL 5 — Semiformally designed and tested: requires semiformal design specification and covert channel analysis; specialist techniques needed.

•EAL 6 — Semiformally verified design and tested: adds semiformal verification of the implementation; very few products worldwide reach this level.

- •EAL 7 — Formally verified design and tested: full mathematical proof of correctness; reserved for the highest-security environments such as military cryptographic modules

## Slide 39

## Lifting to LLVM

Lust

39

## Slide 40

###### Lifting to LLVM for Binary Translation

40

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Lifting to LLVM for Binary Translation
We Know how to Analyze x86-64 binaries.
Let’s perform a preliminary binary translation from third party architectures to x86-64
a ”
Ne Binary Translation
d
Exempli Gratia:
Cristina Cifuentes (UQBT, 2000)
Translation from m68k to sparc32
40
```

## Slide 41

###### Lifters

41

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Lifters
Lifter Anvill RetDec Rev.ng
First release 2019-2020 2017 (open-sourced by Avast; 2016 (VEE'16 paper;
research from ~2011) company founded 2014)
License Apache 2.0 MIT GPL v2 / commercial
Maintained by Trail of Bits Community (Avast open- rev.ng srl (Italian startup)
sourced: core team disbanded
~2020)
Output IR LLVM IR LLVM IR LLVM IR (via QEMU TCG)
Lifting strategy
Spec-driven (uses Remill: per-
instruction semantics in LLVM
IR)
Pattern-matching + control-flow
structuring; full decompiler
pipeline
QEMU TCG as first-stage lifter;
LLVM IR as second stage
Architectures x86/x64, AArché4, SPARC (via x86, ARM, MIPS, PPC, MIPS64, All QEMU-supported (~30+);
Remill) ARM64 very broad coverage
Primary goal Binary lifting for analysis & Human-readable decompilation Binary lifting; static + dynamic
recompilation toc analysis; commercial reverse
engineering
Notable Part of the Remill/McSema Integrated into Kali, IDA, Ghidra Broadest arch support;
ecosystem; designed for
composability
plugins; most mature
decompiler output
commercial Ul available (rev.ng
Studio)
41
```

## Slide 42

42

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Oblem : Anvill needs a Decompiler to identity functions
Unstripping Cloud Container ELF binaries
Jonathan Brossard
CEDRIC
Conservatoire National des Arts et Métiers
Paris, France
jonathan. brossard@ lecnam.net
Directive NIS2. The binaries used
g they d debug symbols,
making the evaluation of their security posture more comple
This article focuses on automated ways to recover some of this
critical debugging information, a process named unstripping, on
inux x86_64 binaries, such as those presently overwhelmingly
used within containers.
Index Terms—ELF unstripping, Reverse Engineering, Cloud
binaries, NIS2, debugging
1. INTRODUCTION
The recent upgrades to the European legal framework rela
tive to the security of Cloud services mandate that Product Se
ity Incident Response Teams (or PSIRT) offering services
in Europe shall report new vulnerabilities affecting their prod-
uct and services under 24 hours, to their respective national
authorities. In particular, the Directive (UE) 2022/2555 [1]
dubbed NIS2, renders compulsory the evaluation and reporting
of security vulnerabilities under those timelines
The public disclosure of over 40,000 vulnerabilities under
the form of CVEs by the NIST in 2024 [2] ber up
from about 29,000 in 2023), leaves PSIRT teams with the
daunting task of evaluating the exposure of their services to
over 100 new vulnerabilities published every day. Arguably,
the emergence of tools such as Software Bill of Materials
(SBOMs), alleviate some of the PSIRT burden by auto:
the collection of potential vulnerabilities [10] affectin
tainers, based solely on the versions of the binaries used within
such containers. However, recent studies
doubt over the effectiveness and replicability of such SBOMs.
This leaves PSIRT teams with the task of manually verifying
potential vulnerabilities reported via SBOMs monitoring [11]
through extensive debugging. In particular, a given version
of a piece of software may or may not be vulnerable to
ulnerability, and its CVSS [16] score drastically
zed, depending on their exact compilation options [4] [5]
Those hardening properties are currently not reflected in major
SBOM standards [9] (6] [7] [8]
Recent studies [13] indicate that the vast majority of con
tainers [12] readily available today operate primarily under
Linux and the x86_64 architecture, by as much as 97%
The ELF [15] binaries shipped within those containers are
typically production-ready, and in particular have been stripped
of debugging symbols, making debu by PSIRT team
harder
In this article, we aim to provide a means for PSIRT teams
to improve their response time when evaluating their exposure
to a given vulnerability within a C/C++ Linux ELF x86_64
binary by automatically unstripping the target binary, meaning
entirely or partially retrieving their debug information. We
implement several avenues to perform this task in a sing!
application, named wunstrip, published under a permissi
open-source MIT/BSD-2 license, hoping to foster its study and
adoption by the cybersecurity community. To the best of our
knowledge, the latter two techniques leveraging the specifics
of the x86_64 ELF standard [14] are entirely new:
I. STATE OF THE ART
A. Overview of an ELF executable debug symbols
The need to recover debugging information, and primarily
the name and prototype of functions used within binaries
is probably as old as debu; itself [24]. The ELF file
format [15] features several optional structures and sections.
If an executable ELF m e ader, its section
header is optional (19). The main symbol table of the binary is
typically either not emitted by the compiler (if the -s compiler
flag is used with either gcc or clang), or removed after linking
by the strip command. The debugging sections, in dwarf
format [17], can be entirely removed or compiled separately
[18], leaving the production-ready executable without debu
information.
Current versions of the GNU C Compiler [21] and LLVM's
20] toolchains further hide non-exported functions, by
applying the -fvisibility=hidden flag by default (35}, meaning
that their symbols and addresses are not present the final
binary’s symbol tables. Unless the -rdynamic compiler flag is
used (which is not the default), in which case, the function
symbols and their addresses are kept in the dynamic symbol
table of the final binary (in the .dynstr and .dynsym sections
respectively).
As such, a typical executable ELF binary as shipped by
major distributions, such as Redhat or Debian, in a container
image, does not retain its main symbol table, and possesses
no debug symbols, effectively hiding the addresses of fune-
tions within the executable. However, debug symbols may be
downloaded separately [41]
\ttps://github.com/ends
QD eeveatne 1 wunsro 6
code © issues 11 pullrequests 1 Bi Projects © security and quality
@ wunstrip
‘Your main branch isn't protected
Protect this branch from force pushing or delet
merging,
endrazine
include
gitmodule
D Makefile
EADME.md
1B debuglink
Protect this branch
Releases
Packages
Contributors 1
o
```

## Slide 43

43

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
« The Experiment >>: Dataset Construction
Leverage « debootstrap » to download chroots for Debian stretch (9), buster (10), bullseye (11), bookworm
(12), trixie (13, testing), and forky (unstable) and Ubuntu xenial (16.04 LTS), bionic (18.04 LTS), focal (20.04
LTS), jammy (22.04 LTS), and noble (24.04 LTS) :
chroot-bionic-arm64 chroot-forky-arm64 chroot-trixie-arm64
chroot-bionic-armhf chroot-forky-armht chroot-trixie-armhf
chroot-bionic-ppcé4el chroot-forky-ppcé4el chroot-trixie-ppcé4el
chroot-bionic-s390x chroot-forky-riscv64 chroot-trixie-riscv64
chroot-bookworm-arm64 chroot-forky-s390x chroot-trixie-s390x
chroot-bookworm-armhf chroot-jammy-arm64 chroot-xenial-arm64
chroot-bookworm-ppcé4el chroot-jammy-armhf chroot-xenial-armhf
chroot-bookworm-s390x chroot-jammy-ppcé4el chroot-xenial-ppcé4el
chroot-bullseye-arm64 chroot-jammy-riscv64 chroot-xenial-s390x
chroot-bullseye-armhf chroot-jammy-s390x
chroot-focal-arm64 chroot-noble-arm64 a. |
chroot-focal-armhf atyar pelea 39,364 binaries
chroot-focal-ppcé64el chroot-noble-ppcé4el
chroot-focal-riscv64 chroot-noble-riscv64
chroot-focal-s390x chroot-noble-s390x 43
```

## Slide 44

44

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Full Dataset Evaluation : RetDec & Anvil
Architecture Count RetDec Anvill
ARM64 (aarch64) 8,933 79.1% (7,062) 15.2% (1,358)
ARMv7 (armhf) 7,930 48.8% (3,870) 8.7% (690)
PowerPC64 (ppc64el) 8,134 0.0% (0) 0.0% (0)
RISC-V 64 (riscv64) 4,952 12.3% (609) 94.1% (4,660)
s390x (mainframe) 9.415 3.2% (301) 68.1% (6,412)
Total 39,364 829.9% (11,842) 33.5% (13,120)
44
```

## Slide 45

45

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Stratified Evaluation : RetDec, Anvill & Rev.ng
(100 binaries x 5 architectures
Architecture
ARM64
ARMv7
PowerPC64
RISC-V
s390x
Total
n
100
100
100
100
100
500
RetDec
18%
51%
O%
11%
A%
28.8%
Anvill
16%
9%
O%
95%
69%
37.8%
rev.ng
85%
72%
O%
23%
58%
47.6%
45
```

## Slide 46

46

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Per-Architecture Complementarity
Architecture Best Tool Success Runner-Up
ARM64 rev.ng 85% RetDec 78%
ARMv7 rev.ng 72% RetDec 51%
PowerPC64 (none) 0% (none) 0%
RISC-V Anvill 95% ——irev.ng 23%
s390x Anvill 69% —_—rev.ng 58%
```

## Slide 47

## Wsolver : a Full 0day Pipeline

Glutony

47

## Slide 48

48

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Wsolver : Lifting to LVM + Symbolic Execution/Abstract Interpretation
```

## Slide 49

# 𝕯𝕰𝕸𝕺

49

## Slide 50

Performing a Resurrection Sloth

50

## Slide 51

###### Vulnerabilities : Information Evanescence

###### Top 10 reference domains across all NVD CVEs

|Index|Links|Domain|Comment|
|---|---|---|---|
|1|174,961|Github.com|Live|
|**2**|**165,340**|**SecurityFocus.com**|**Bugtraq**
**(**
**)**|
|3|119,516|Secunia.com|Redirect (dead)|
|4|78,497|Git.ketnel.org|Live|
|5|74,800|Xforce.ibmcloud.com|Live|
|6|59,513|Securitytracker.com|Squatted|
|7|50,491|Vulndb.com|Live|
|8|42,726|Opensuse.org|Live|
|9|42,712|Osvdb.org|Squatted|
|10|41,617|Vupen.com|Squatted|

51

## Slide 52

###### Vulnerabilities : Information Evanescence

jonathan@blackbox:~$ whois securityfocus.com

The Registry database contains ONLY .COM, .NET, .EDU domains and Registrars. Domain Name: securityfocus.com Registry Domain ID: 5068534_DOMAIN_COM-VRSN Registrar WHOIS Server: whois.brandsight.com Registrar URL: https://gcd.com Updated Date: 2025-12-30T15:26:27Z Creation Date: 1999-01-30T05:00:00Z Registrar Registration Expiration Date: 2027-01-30T05:00:00Z Registrar: GoDaddy Corporate Domains, LLC Registrar IANA ID: 3786 Registrar Abuse Contact Email: abuse@gcd.com Registrar Abuse Contact Phone: +1.5188315864 Domain Status: clientTransferProhibited https://icann.org/epp#clientTransferProhibited Registrant Organization: Accenture Global Services Limited Registrant State/Province: IE Registrant Country: IE … jonathan@blackbox:~$

52

## Slide 53

###### Rise from the Deads

53

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Rise from the Deads
Excellent 4.6 out of 5 ¥ Trustpilot
The domain name
Get this domain
sec u rityfoc u Ss ~ co Mm Purchase it today for $175,000.00 or make an offer.
It's for sale!
Make an offer
Following
Free transaction assistance
Y Secure payments
Local currency available in the cart at checkout
Safe and secure transactions Quick and easy transfers Hassle-free payments y
The easy, and safe, way to buy domain names
Need help? Call us. 480-651-9741
Whatever type of domain you wish to buy or rent, we guarantee a simple and secure transfer.
Here is how it works —>
```

## Slide 54

###### The Resurrection

54

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
The Resurrection
Domain
securityfocus.com Domain Status: IDLE
Overview DNS Registration Settings Products Activity Log
Contact Info © Domain Privacy: On ©
blic WHOIS directory when Do cy Your perso ote C o is replace our public WHOIS directo
Jonathan Brossard at Domains By Proxy, LLC
Registration Private
DomainsByProxy.com, 100 S. Mill Ave, Suite 1600, Tempe,
Arizona, United States 85281
jonathan.brossard@moabi.com Telephone +1.4806242599
securityfocus.com@domainsbyproxy.com
54
```

## Slide 55

###### The Resurrection

55

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
The Resurrection
¥ ‘Symantec
_>
accenture
l\
BROADCOM.
55
```

## Slide 56

##### **Thanks for** **<u>your attention</u>**

56

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
© Df AAR
Fall 2 OOO -
-* =, uy, =
? | Ti sore ? =
=i ae amnenqneemee) i. Qi
0 eres, an dt {{ gf |
yy Zh OOO in ae
4“ VA +—4 He JN WA )
tru nde Mt AN (1) ¥
tA ry i \o- Ko,
+ 71 T
oh wT] 2 tale
```

## Slide 57

###### Illustrations & Copyrights

Cover Page: Giomodica, Creative Commons Attribution

3.0 Unported license, https://web.archive.org/web/20161011041054/http://www.panoramio.com/photo/5820740

Logo: By Unknown author, CC BY-SA 4.0, https://commons.wikimedia.org/w/index.php?curid=69056451 Sad Gargoyle: WDWParksGal, Creative Commons Attribution 3.0 LicenseCreative Commons Attribution 3.0 License, https://www.deviantart.com/wdwparksgal-stock/art/Gargoyle-Stock-Photo-IMG-1734-640555082

David Hilbert: Unknown Author, Public Domain, https://commons.wikimedia.org/wiki/File:Hilbert.jpg Kurt Godel: Unknown Author, Public Domain, https://commons.wikimedia.org/wiki/File:Young_Kurt_G%C3%B6del_as_a_student_in_1925.jpg Clown: Linnaea Mallette, CC0 Public Domain, https://www.publicdomainpictures.net/en/viewimage.php?image=449753&picture=clown-zombie-face-and-teeth

57
