---
title: "Uncovering Supply Chain Attack with Code Genome Framework"
speakers: ["Dhilung Kirat", "Jiyong Jang"]
conference: "Black Hat"
conference_full: "Black Hat USA 2024"
edition: "USA"
year: 2024
source_pdf: "Black Hat USA 2024 slides/Dhilung Kirat & Jiyong Jang_Uncovering Supply Chain Attack with Code Genome Framework_Compressed.pdf"
pages: 30
sha256: "745ccfbce4f0d78897abab385fed409f32e2fcac32c5356a20c00c00aa9dfaf5"
text_chars: 13328
ocr_pages: 4
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T23:58:56Z"
---
# Uncovering Supply Chain Attack with Code Genome Framework

**Speakers:** Dhilung Kirat, Jiyong Jang  
**Conference:** Black Hat USA 2024  
**Source:** `Black Hat USA 2024 slides/Dhilung Kirat & Jiyong Jang_Uncovering Supply Chain Attack with Code Genome Framework_Compressed.pdf` (30 pages)

## Slide 1

# **Uncovering Supply Chain Attack with Code Genome Framework**

Dhilung Kirat, Jiyong Jang, Doug Schales, Ted Habeck, Ian Molloy, JR Rao

**#BHUSA @BlackHatEvents**

## Slide 2

Dhilung Kirat

Jiyong Jang

AI Supply Chain Security Team IBM **Research**

**#BHUSA @BlackHatEvents**

2

## Slide 3

- `$ foo install bar`

- Signed with a certificate.

- Lists dependencies.

- Do you trust it?

**#BHUSA @BlackHatEvents**

3

## Slide 4

_“You can’t trust code that you did not totally create yourself_ .”

_—Ken Thompson_

**#BHUSA @BlackHatEvents**

4

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
“You can't trust code that you did
not totally create yourself.
pian hat
USA 2024
J
—Ken Thompson
#BHUSA @BlackHatEvents
TURING AWARD LECTURE
Reflections on Trusting Trust
To what extent should one trust a statement that a program is free of Trojan
horses? Perhaps it is more important to trust the people who wrote the
software.
KEN THOMPSON
INTRODUCTION
I thank the ACM for this award. I can’t help but feel
that I am receiving this honor for timing and serendip-
ity as much as technical merit. UNIX’ swept into popu-
larity with an industry-wide change from central main-
frames to autonomous minis. I suspect that Daniel Bob-
row [1] would be here instead of me if he could not
afford a PDP-10 and had had to “settle” for a PDP-11.
Moreover, the current state of UNIX is the result of the
labors of a large number of people.
There is an old adage, “Dance with the one that
brought you,” which means that I should talk about
UNIX. I have not worked on mainstream UNIX in many
years, yet I continue to get undeserved credit for the
work of others. Therefore, I am not going to talk about
UNIX, but I want to thank everyone who has contrib-
uted.
That brings me to Dennis Ritchie. Our collaboration
has been a thing of beauty. In the ten years that we
have worked together, I can recall only one case of
miscoordination of work. On that occasion, I discovered
that we both had written the same 20-line assembly
language program. I compared the sources and was as-
tounded to find that they matched character-for-char-
acter. The result of our work together has been far
greater than the work that we each contributed.
Iam a programmer. On my 1040 form, that is what I
put down as my occupation. As a programmer, I write
7 UNIX is a trademark of AT&T Bell Laboratories.
© 1984 0001-0782/84/0800-0761 75¢
August 1984 Volume 27 Number 8
programs. I would like to present to you the cutest
program I ever wrote. I will do this in three stages and
try to bring it together at the end.
STAGE I
In college, before video games, we would amuse our-
selves by posing programming exercises. One of the
favorites was to write the shortest self-reproducing pro-
gram. Since this is an exercise divorced from reality,
the usual vehicle was FORTRAN. Actually, FORTRAN
was the language of choice for the same reason that
three-legged races are popular.
More precisely stated, the problem is to write a
source program that, when compiled and executed, will
produce as output an exact copy of its source. If you
have never done this, I urge you to try it on your own.
The discovery of how to do it is a revelation that far
surpasses any benefit obtained by being told how to do
it. The part about “shortest” was just an incentive to
demonstrate skill and determine a winner.
Figure 1 shows a self-reproducing program in the C?
programming language. (The purist will note that the
program is not precisely a self-reproducing program,
but will produce a self-reproducing program.) This en-
try is much too large to win a prize, but it demonstrates
the technique and has two important properties that I
need to complete my story: 1) This program can be
easily written by another program. 2) This program can
contain an arbitrary amount of excess baggage that will
be reproduced along with the main algorithm. In the
example, even the comment is reproduced.
Communications of the ACM
761
```

## Slide 5

#### **Supply Chain Attacks**

- SolarWinds (2019-2021) est. cost > $100B

   - Malicious code (backdoor) pushed out through updates

- Dependency confusion (Feb 2021)

   - Private vs public packages (npm, PyPi, RubyGems)

- Codecov (Apr 2021)

   - DevOps tool. Vulnerability in CI. Bash uploader modified

- Kaseya (Jul 2021) ransom $70M

   - IT solutions, including VSA (remote monitoring and management software) to deliver REvil ransomware

- Protestware (Mar 2022)

   - Popular NPM package wiped files in Russia and Belarus

###### 3CX (Mar 2023)

- Backdoor implanted into Windows and macOS due to secondary supply chain attack

**#BHUSA @BlackHatEvents**

5

## Slide 6

#### **xz Backdoor**

Thomas Roccia

_https://www.openwall.com/lists/oss-security/2024/03/29/4_

systemd
OpenSSH

**Semantic gap** between compiled code behavior and its metadata

https://securelist.com/xz-backdoor-story-part-1/112354/

#BHUSA @BlackHatEvents

6

## Slide 7

#### **Supply Chain Security: Industry approach to protecting CI/CD pipelines**

Source Compiled  Distributed
Develop Build Release Deploy
code code code
Security Integrity
(vulnerability) (reproducible CI)
Provenance
(list of components)
SBOM
proprietary code
open source
author
Developer User
CISO

**#BHUSA @BlackHatEvents**

7

## Slide 8

### **Supply Chain Security: Open security issues and residual risks**

Where else the code or
How easy to replicate  library deployed?
10yr old dev environment? ( broader dependency
Compromise dev
analysis , e.g., log4j)
(SolarWinds hack, Security of toolchain? (XCodeGhost)
xz backdoor )
Source Compiled  Distributed
Develop Build Release Deploy
code code code
Security Integrity
(vulnerability) (reproducible CI)
Provenance
bug
(list of components)
SBOM
proprietary code
open source
author
Compromised/stolen SLSAv4 requires  How to inspect
Developer User
certificate? revocation? significant human  closed/legacy code ? How to verify the
CISO
(NVIDIA leak) resources completeness/correctness ?
(copyright, DejaVu)

Where else the code or library deployed? ( **broader dependency analysis** , e.g., log4j)

**#BHUSA @BlackHatEvents**

8

## Slide 9

## Code **Genome**

**#BHUSA @BlackHatEvents**

9

## Slide 10

#### **The Semantic Gap**

Metadata Metadata
Unknown
Known
Code Genome
Code Code

##### **Build chain of trust by following code equivalency**

**#BHUSA @BlackHatEvents**

10

## Slide 11

#### **Code Genome Pipeline**

Optimize
Embedding
Disassembly Lift Generalize
fff Extraction
Code Functions IR Canonical IR Genome

**#BHUSA @BlackHatEvents**

11

## Slide 12

#### **Code Genome Pipeline**

f1
Ingredients for
Function Gene
f1
f2
f2 f3
Code
f3

B x B  sub-blocks
Resize FiltersGabor Sub-blockAveraging
Feature
Trojan.Ramnit
Vector
SigMal pipeline

RetDec Optimize SigMal
Canonicalization
LLVM Pass
LLVM IR Canonical IR Genome

Input Module Shadow Module
• O3 optimization
• dependency
extraction
• global vars
• structs
• other functions
• renaming
• sorting
Canonicalization  pipeline

**#BHUSA @BlackHatEvents**

12

## Slide 13

#### **Code Genome Pipeline**

machine-code “raw” IR Code Gene
Lift
Canonicalize
canonical IR Embedding
Compile
source code
Convert
(optional) bitcode
Convert

_Gene can be constructed from closed-source/legacy code where source code is not easily available._

#BHUSA @BlackHatEvents

13

## Slide 14

#### **Code Genome: Semantically meaningful fingerprint**

**Same Gene**

**#BHUSA @BlackHatEvents**

14

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Code Genome: Semantically meaningful fingerprint
Pes int pen at Sears CIS
if (a>100){
l=l+a;
f3(int a){ 2; if (a>501){
int local = a; irr int tmp = tmp = a+tmp;
a = local;
local = 30;
a+ local; x
a + tmp+2;
maj;
l=m=a;
(aarp x") s “
(ap i lse if(a>10)
sturn a;
l
int tmp 30-a; tmp = tmp + a;
[rbp - tmp = tmp +2; a = a + tmp;
d ptr [rbp - Oxia rn ay
dword ptr [rbp - 4], eax
f2(int a){ S ; : x1000edcfe: 8b 45 f , dvord pte [rbp ~
int local=31; oe pop rbp
local +=1;
local = a + lo
return local; \d
ex100000dbs: 89 ov dword ptr [rbp
eovedbe: a eax, dword ptr [rbp
Lunnamed_addr #0 { ex100000dbb: 89 45 fc word ptr [rbp - 41,
o00edda
e0eeeddd: 8 dword ptr [rbp
e000ede0: 45 eax, dword ptr
ox100000de3: add eax, dword ptr
e000edes: 89 45 dword ptr [rbp
ox100000de9: 8 eax, dword ptr
ee0edec: 8 dword ptr [rbp
dword ptr
mien hat #BHUSA @BlackHatEvents
USA 2024 :
```

## Slide 15

#### **Advantages and Challenges**

##### **Advantages**

- Across multiple architectures (x86, ARM, …)

- Across multiple compilers (gcc, clang, …)

- Across multiple optimization levels

- Handling obfuscation

##### **Challenges**

- Disassembly is undecidable

- Function boundary identification

- Loss of architecture specific nuances

- Canonicalization cannot completely recover high-level abstraction

_Genome_

objdump Ghidra retdec

retdec IDA

**#BHUSA @BlackHatEvents**

15

## Slide 16

## Uncovering **Supply Chain Attack**

**#BHUSA @BlackHatEvents**

16

## Slide 17

#### **Demo 1: xz backdoor analysis using Code Genome**

**liblzma.so.5.6.1.github**

Thomas Roccia
Gene Diff

liblzma.so.5.6.1.distro

#BHUSA @BlackHatEvents

17

## Slide 18

#### **Demo 1: xz backdoor analysis using Code Genome**

**#BHUSA @BlackHatEvents**

18

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Demo 1: xz backdoor analysis using Code Genome
localhost
Code Genome
Compare B eer s05209%00
Bp vera sos.20.istro
663500a4dbcb9faaac802eb3c4bSb0dd5c0333df473d7368b0bc53a32/0C363a 7ca35118ebe61d2789be1c84c3e93
Gene similarity: 70 Identical: 191 Similar: 95 Mismatch: 27 Deletions: Additions: 101
liblzma.so.5.6.1.github (663500a4) Functions liblzma.so.5.6.1.distro (4becc50a) Functions Actions
crc32_resolve crc32_resolve
crc64_resolve ‘cre64_resolve
get_literal_price get_literal_price
get_options get_options
hash_append hash_append
Izencoder_prepare Izencoder_prepare
lzma2_bound.part.0 lzma2_bound.part.0
lzma_delta_encoder_init lzma_delta_encoder_init
lzma_index_buffer_decode lzma_index_buffer_decode
lzma_index_memusage lzma_index_memusage
lzma_lz_encoder_init lzma_lz_encoder_init
piSekhat #BHUSA @BlackHatEvents A> 18
USA 2024
```

## Slide 19

#### **xz backdoor Gene Similarity Analysis using GeneDiff**

Gene Similarity

_xz versions_

Local vs distribution builds of same version

**#BHUSA @BlackHatEvents**

19

## Slide 20

#### **xz backdoor Gene Similarity Analysis using GeneDiff**

2024
2007-2009
Earthquake
alpha/beta xz versions
Gene Similarity

###### Incremental version similarity in distribution builds

**#BHUSA @BlackHatEvents**

20

## Slide 21

## Improving **Supply Chain Security**

**#BHUSA @BlackHatEvents**

21

## Slide 22

#### **Trust but Verify SBOM: Metadata vs. Code**

###### `$ sbom generation tools`

##### **Problem**

- Each vendor creates SBOM of their own software including open-source and closed-source components.

- How can we verify its _correctness_ (containing incorrect library mistakenly/maliciously) and _completeness_ (missing library)?

delete dpkg DB

-

- “Unfortunately, some images – such as the <u>official node image on Docker Hub</u> incorrectly report the version of OpenSSL that's used by the Node.js runtime.”

_https://www.chainguard.dev/unchained/mitigating-critical-openssl-vulnerability-with-chainguard_

**#BHUSA @BlackHatEvents**

22

## Slide 23

#### **Knowledge Graph: Gene Granularity**

P
A
A
File
data
Level
F F F
Segment  F
Level
F
f
f
text f
f
f
f
Function  f f f
Level F F f f f
F
F
A F
P
Package (e.g., ) foo.deb
File (e.g.,  /usr/bin/foo )
Archive (e.g., ) data.tar.xz

**#BHUSA @BlackHatEvents**

23

## Slide 24

#### **Knowledge Graph: Gene Granularity**

P
A
A
File
data
Level
F F F
Segment  F
Level
F
f
f
text f
f
f
f
Function  f f f
Level F F f f f
F
F
A F
P
Package (e.g., ) foo.deb
File (e.g.,  /usr/bin/foo )
Archive (e.g., ) data.tar.xz

**#BHUSA @BlackHatEvents**

24

## Slide 25

#### **Demo 2: SBOM generation for an unknown** **`rpm` package**

###### Custom `rpm` package

###### SBOM generated by Code Genome

###### Integrating with other SBOM analysis platforms

**#BHUSA @BlackHatEvents**

25

## Slide 26

#### **Knowledge Graph: Code Genome and Use Cases**

find other
vulnerable code
mozjpeg
CVE-2020-13790
libjpeg-turbo
code classification
Unknown
wget
detect backdoor
Backdoor
Function File Package Container Device
Code Genome KG

#BHUSA @BlackHatEvents

26

## Slide 27

## Open Sourcing **Code Genome**

**#BHUSA @BlackHatEvents**

27

## Slide 28

#### **Status and Roadmap**

###### Open-source tools

###### `–` **`Code Genome Framework`**

###### **code-genome**

https://github.com/code-genome

   - GeneDiff, Basic KG, CLI tools, and GUI

   - Currently supported

      - Binaries: `ELF, PE, Mach-O`

      - Architectures: `x86, x86_64, arm, aarch64, mips, ppc`

   - Optimized canonicalization

- **`Jaudit`**

   - JAR file support

   - JAR version identification

   - CVE annotation

###### Next steps

- Support

   - Packages: `deb, rpm, ipa`

   - Archives: `ar, cpio, tar, bzip2, gzip, zstd, xz, rar, 7zip`

```
git clone https://github.com/code-genome/codegenome.git
cd codegenome
```

```
make start
```

**#BHUSA @BlackHatEvents**

28

## Slide 29

#### **Takeaways**

#### Semantic Gap

Code

Metadata

Inherent sematic gap breaks the transfer of trust from metadata to code

#### Code Genome

Now open-sourced Code Genome Framework can help bridge that gap

#### Supply Chain Security

Detection of XZ-backdoor demonstrates framework’s capability in improving supply chain security

**#BHUSA @BlackHatEvents**

29

## Slide 30

Dhilung Kirat _dkirat@us.ibm.com_ Jiyong Jang _jjang@us.ibm.com_

IBM **Research**

github.com/code-genome

**#BHUSA @BlackHatEvents**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
a a
}
black hat —
USA 2024
Dhilung Kirat & dkirat@us.ibm.com
Jiyong Jang XX jjang@us.!bm.com
IBM Research
github.com/code-genome
#BHUSA @bBlackHatEvents
```
