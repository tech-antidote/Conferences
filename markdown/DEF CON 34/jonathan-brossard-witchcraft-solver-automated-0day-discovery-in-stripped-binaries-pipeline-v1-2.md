---
title: "Witchcraft Solver Automated 0day Discovery in Stripped Binaries"
speakers: ["Jonathan Brossard"]
conference: "DEF CON"
conference_full: "DEF CON 34"
edition: "34"
year: 2026
source_pdf: "DEF CON 34/Jonathan Brossard - Witchcraft Solver Automated 0day Discovery in Stripped Binaries - pipeline v1 (2).pdf"
pages: 57
sha256: "4d43c97044f59c5c2c59e0b55e06ab0eb9a8004357c4eeefbceba4b58d1d25ef"
text_chars: 43107
ocr_pages: 18
has_ocr: true
redacted_secrets: 0
ocr_confidence: 87.5
ocr_unreliable_blocks: 0
duplicate_of: "jonathan-brossard-witchcraft-solver-automated-0day-discovery-in-stripped-binaries-pipeline-v1.md"
content_note: "All 57 pages were rendered and read against the source PDF by a vision model, and 51 were rewritten as a result. The ocr_* fields below describe the superseded first-pass extraction and are kept as provenance, not as a description of this text."
vision_verified_pages_changed: 51
vision_verified_pages: 57
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T06:46:32Z"
---
# Witchcraft Solver Automated 0day Discovery in Stripped Binaries

**Speakers:** Jonathan Brossard  
**Conference:** DEF CON 34  
**Source:** `DEF CON 34/Jonathan Brossard - Witchcraft Solver Automated 0day Discovery in Stripped Binaries - pipeline v1 (2).pdf` (57 pages)


## Slide 1

### **Witchcraft Solver: Automated 0day Discovery in Stripped Binaries**

**DEF CON 34**

_Las Vegas, August 2026_  
_Jonathan Brossard_  
_endrazine@psirt.com_

1

## Slide 2

###### Agenda

Pride  
Avarice  
Envy  
Wrath  
Lust  
Gluttony  
Sloth

2

## Slide 3

### Who Am I ?

Pride

3

## Slide 4

_Full-slide photograph: the speaker standing at a podium in front of a DEF CON step-and-repeat backdrop, overlaid with a red-and-white stencil graphic reading "I AM AN IMMIGRANT" whose words are struck through by red censor bars._

## Slide 5

OPERATIONS // GLOBAL SPEAKING ENGAGEMENTS

21 NODES / 45 EVENTS

_Full-slide dark world map with red proportional-symbol bubbles marking speaking-engagement locations: Hawaii, the western United States (largest bubble), Mexico/Central America, Brazil, a dense cluster over Western and Northern Europe, Italy, India, Southeast Asia, East Asia/Japan, Australia and New Zealand. No individual city labels are printed._

EVENTS PER NODE:  1   4   9

## Slide 6

_Full-slide image of an ornate gold-and-blue bordered ordination certificate:_

**American Marriage Ministries**

Hereby it is certified that upon the recommendation  
of the Church Board we recognize

**Jonathan Brossard**

as a duly ordained minister of  
American Marriage Ministries.  
We grant the full authority to perform all  
duties within the tenets of the Church.

This minister is ordained as of  
February 24th, 2017

in the register of  
American Marriage Ministries.

Minister ID: 659650-396288

_(handwritten signature)_  
Chief Officer and President

6

## Slide 7

##### Automated Libification : the Witchcraft Linker

_Three USENIX badges, top right: ARTIFACT EVALUATED / usenix ASSOCIATION — **AVAILABLE**, **FUNCTIONAL**, **REPRODUCED**._

URL: https://github.com/endrazine/wcc
License: MIT/BSD-2

```text
jonathan@blackbox: ~/woot
Fichier  Édition  Affichage  Rechercher  Terminal  Aide

jonathan@blackbox:~/woot$ file ls
ls: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamicall
y linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=3eca7e
3905b37d48cf0a88b576faa7b95cc3097b, for GNU/Linux 3.2.0, stripped
jonathan@blackbox:~/woot$ wld -libify ./ls
jonathan@blackbox:~/woot$ file ls
ls: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically
 linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=3eca7e3
905b37d48cf0a88b576faa7b95cc3097b, for GNU/Linux 3.2.0, stripped
jonathan@blackbox:~/woot$
```

_In the terminal, `pie executable` and `shared object` are boxed in red; `wld -libify ./ls` is boxed in green._

DOI 10.5281/zenodo.11405214

7

## Slide 8

#### Witchcraft Shell : Procedural Debugging

- Libify ELF executables

- Make ELF executables scriptable

- Call arbitrary functions (procedural debugging)

```text
jonathan@blackbox: ~
Fichier  Édition  Affichage  Rechercher  Terminal  Aide

jonathan@blackbox:~$ wsh /usr/sbin/apache2
ERROR: dlopen() /usr/sbin/apache2: cannot dynamically load
position-independent executable
 ** libifying /usr/sbin/apache2 to //tmp/.wsh-964913/apache
2 (754232 bytes)
 ** loading of libified binary succeeded
> a = ap_get_server_banner()
> print(a)
Apache/2.4.58
>
```

URL: https://github.com/endrazine/wcc
License: MIT/BSD-2

DOI 10.5281/zenodo.13902925

8

## Slide 9

#### Witchcraft Compiler : Unlinking + Relinking

wcc can unlink + relink apache2, nginx, sshd, proftpd.

Unlinking + static unlinking (statification): proven on apache2

https://github.com/endrazine/wcc-test-relinking

*Terminal window "root@d9a2b979f64a: ~/demos/relinking" (menu: Fichier, Edition, Affichage, Rechercher, Terminal, Aide):*

```
root@d9a2b979f64a:~/demos/relinking# gcc small.c -o small

small.c: In function 'do_something':
small.c:24:22: warning: initialization makes pointer from integer without a cast [-Wint-conversion]
   static char *buff = 4;  // Global initialized : @data
                  ^

small.c:36:2: warning: format not a string literal and no format arguments [-Wformat-security]
  fprintf(stderr, buff);   // relocation to fprintf@plt and stderr@bss (imported)
  ^

root@d9a2b979f64a:~/demos/relinking# ./small
Hello User ! from ./small
root@d9a2b979f64a:~/demos/relinking# wcc small -o small_wcc.o -c

root@d9a2b979f64a:~/demos/relinking# gcc small_wcc.o -o small2

root@d9a2b979f64a:~/demos/relinking# ./small2

Hello User ! from ./small2
root@d9a2b979f64a:~/demos/relinking# file small small_wcc.o small2
small:        ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=bb53acdfcd9c80aab686d10d007b298d6952709a, not stripped
small_wcc.o: ELF 64-bit LSB relocatable, x86-64, version 1 (SYSV), not stripped
small2:       ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=56b2f7573138b2e939d72ecdba30bdfc931b1ecd, not stripped
root@d9a2b979f64a:~/demos/relinking# gcc
```

9

## Slide 10

#### Libification + Relinking

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

char * ap_parse_log_level ( const char * str , int * val ) ;

int main ( int argc , char ** argv ) {
   int i = 0;
   char * ret = 0;
   if ( argc < 2 ) {
      printf ( "Usage : %s <loglevel>\n" , argv [ 0 ] ) ;
      exit ( EXIT_SUCCESS ) ;
   }

   ret = ap_parse_log_level ( argv [ 1 ] , &i ) ;
   if ( ! ret ) {
      printf ( "loglevel: %d \n" , i ) ;
   } else {
      printf ( "%s \n" , ret ) ;
   }
   return 0;
}
```

*Terminal window "jonathan@blackbox: /tmp/apache" (menu: Fichier, Edition, Affichage, Rechercher, Terminal, Aide):*

```
jonathan@blackbox:/tmp/apache$ ./demo_relinked
Usage: ./demo_relinked <loglevel>
jonathan@blackbox:/tmp/apache$ ./demo_relinked alert
log level: 1
jonathan@blackbox:/tmp/apache$ ./demo_relinked emerg
log level: 0
jonathan@blackbox:/tmp/apache$ ./demo_relinked info
log level: 6
jonathan@blackbox:/tmp/apache$
```

10

## Slide 11

#### Zeitgeist versus Epistemology : Theoretical limits of AI

Avarice

*PSIRT logo, top right.*

11

## Slide 12

#### Zeitgeist : AI is Going to "Solve" Security...

*Screenshot of an X (Twitter) thread:*

**SecInterviewHub** (verified) @sec_hub93028 - Jul 5

AI has NOT solved cybersecurity.

7 replies - 1 repost - 24 likes - 2.6K views

**Robert Graham** (verified) @robertgraham - Jul 6

@grok is this true?

1 reply - 0 reposts - 4 likes - 1.2K views

**Grok** (verified) @grok - Jul 6

Yes, it's true. AI has advanced cybersecurity a lot-better threat detection, malware analysis, and automated responses-but it hasn't solved it. Attackers use AI too, zero-days and novel exploits keep emerging, false positives persist, and human factors remain critical. It's a

Show more

[ Ask Grok ]

1 reply - 0 reposts - 1 like - 141 views

**@mikko** (verified)
@mikko

@grok how much longer do we have to wait

8:23 AM - Jul 6, 2026 - **82** Views

1 reply - 0 reposts - 2 likes

Post your reply    [ Reply ]

**Grok** (verified) @grok - Jul 6

Hard to say, because "solved" probably isn't the right framing. Cybersecurity is an endless arms race-AI boosts detection, automation, and response on defense, but attackers get the same tools plus fresh zero-days and novel exploits. New tech always creates new surfaces. We'll

Show more

12

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

#### [first line of the title is clipped above the top edge of the slide - illegible] in Mathematics !!

PhD thesis in 1931 (at 25 years old):

First **incompleteness** theorem:

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

#### Exploiting a Fundamental "Bug" in Mathematics !!

Let's build a C Program implementing a Problem AI will **Provably** NEVER be able to solve...

17

## Slide 18

#### Exploiting a Fundamental "Bug" in Mathematics !!

Show me a C Program that has an Undecidable Security Property !

18

## Slide 19

#### Towards a formal Proof of the Rice Theorem

Envy

19

## Slide 20

#### Towards a Formal Proof in Constructivist Theory

ZFC arithmetic

Formal Proof : Lean or Rocq

Constructivist => No reductio ad absudum

Correspondance Howard-Curry:

_"There exists an isomorphism between Algorithms and Mathematical Proofs"_

20

## Slide 21

#### q ) degree is ≥ 3 (MRDP with a Constructive Proof in Rocq)

Matiyasevich, Yuri Vladimirovich. "The Diophantineness of enumerable sets." In _Doklady Akademii Nauk_, vol. 191, no. 2, pp. 279-282. Russian Academy of Sciences, 1970.

Larchey-Wendling, D. and Forster, Y., 2022. Hilbert's Tenth Problem in Coq (Extended Version). _Logical Methods in Computer Science_, _18_.

21

## Slide 22

#### ( p Equations) is Proved Undecidable with a degree ≥ 3

Given c in ℤ, find {x,y,z} in ℤ³ such that:

x³ + y³ + z³ = c

22

## Slide 23

#### A Constructive Proof of Rice's Theorem and the Halting Problem via Hilbert's 10th Problem

*Screenshot of the first page of the paper:*

> **A CONSTRUCTIVE PROOF OF RICE'S THEOREM AND THE HALTING PROBLEM VIA HILBERT'S TENTH PROBLEM**
>
> JONATHAN BROSSARD
>
> *e-mail address*: brossardj@acm.org
>
> ABSTRACT. Rice's theorem states that no non-trivial semantic property of programs is decidable. Classical proofs proceed by reduction from the halting problem, invoking the law of excluded middle (LEM) twice: once through diagonalization, and once through a case split on whether the always-diverging program ⊥ satisfies the property in question. We present a proof that is *constructive relative to the undecidability of Hilbert's Tenth Problem* (MRDP): valid in intuitionistic logic, requiring neither diagonalization nor self-reference, and adding no classical reasoning beyond the MRDP assumption itself.
>
> The key idea is a two-witness construction. Given a non-trivial property P, we attach to each Diophantine polynomial D a pair of programs S⁰_D, S¹_D that behave like the negative and positive witnesses for P when D is solvable, and both diverge identically when it is not. A hypothetical decider for P would therefore decide Diophantine solvability via the difference δ_D = Decide_P(S¹_D) − Decide_P(S⁰_D) — contradicting the MRDP theorem. The argument is structured as two separate implications, never asserting a disjunction about solvability, and never examining P(⊥). The undecidability of the halting problem follows as an immediate corollary: a single application of Rice's theorem to the `Terminates` property.
>
> A formalization in the Rocq proof assistant¹ confirms both results within a step-indexed model of computation, with the undecidability of Hilbert's Tenth Problem as the sole external axiom. Both `Rice_Theorem` and `Halting_Problem` are *closed under the global context*².
>
> **1. INTRODUCTION**
>
> Rice's theorem [Ric53] states that no non-trivial semantic property of programs is decidable. We prove it constructively *relative to MRDP undecidability*: our proof is valid in intuitionistic logic and adds no classical reasoning beyond the undecidability of Hilbert's Tenth Problem. The halting problem [Tur36] is the most famous specific instance: no algorithm decides, for an arbitrary program and input, whether the program halts. Standard textbook proofs of both results invoke the law of excluded middle (LEM) in essential ways. For Rice's theorem, LEM appears in at least two places: through diagonalization, which requires asserting that a hypothetically constructed program either halts or diverges; and through a case split on whether the always-diverging program ⊥ satisfies the property P in question — the so-called P(⊥) split. For the halting problem, LEM enters through self-reference: the diagonal program halts if and only if the hypothetical decider says it does
>
> *Key words and phrases:* Rice's theorem, halting problem, constructive logic, intuitionistic logic, MRDP theorem, Hilbert's tenth problem, Rocq, step-indexed semantics, undecidability, formal verification, diagonalization-free.
>
> Preprint submitted to
> Logical Methods in Computer Science
>
> © CONSTRUCTIVE RICE AND HALTING VIA MRDP
> Creative Commons

Fully constructive Proof
34 Pages Proof in Rocq
Halting Point is a Corollary

Paper: https://arxiv.org/abs/2604.16477

Code: https://github.com/endrazine/rice-constructive

23

## Slide 24

#### A Constructive Proof of Rice's Theorem and the Halting Problem via Hilbert's 10th Problem

*Terminal window `jonathan@blackbox: ~/rice` — menu: Fichier, Édition, Affichage, Rechercher, Terminal, Aide*

```coq
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
  (forall ar p, is_solvable   ar p -> F ar p = 1%Z) /\
  (forall ar p, is_unsolvable ar p -> F ar p = 0%Z).

(** A boolean separator for our Poly type. *)
Definition bool_separator (f : nat -> Poly -> bool) : Prop :=
  (forall ar p, is_solvable   ar p -> f ar p = true)  /\
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
    of a Z-separator.  Contrapositive of Z_sep_to_bool_sep.
    No classical reasoning. *)
Theorem bridge_logical :
  (~ exists f, bool_separator f) ->
  (~ exists F, Z_separator    F).
Proof.
  intros Hnobool [F HF].
  apply Hnobool.
:
```

24

## Slide 25

#### Consequence : The first Program in C, whose termination is Proved Undecidable (Formal Proof in Rocq)

*Terminal window `jonathan@blackbox: ~/rice` — menu: Fichier, Édition, Affichage, Rechercher, Terminal, Aide*

```text
jonathan@blackbox:~/rice$ make docker-rocq 2>&1|tail -n 8
Closed under the global context
Closed under the global context

=======================================================
  Rocq: proof verified inside Docker container.
  Rocq version: The Coq Proof Assistant, version 8.20.0
  Axiom: H10C_SAT_undec (coq-library-undecidability)
=======================================================
jonathan@blackbox:~/rice$
```

*Screenshot of the source file `undecidable.c`:*

```c
/*
 * undecidable.c — a program whose termination is provably undecidable
 *
 * This file contains two things:
 *
 *   1. A generic Diophantine search engine (find_sol) that directly mirrors
 *      the Rocq function of the same name in rice.v.
 *
 *   2. Two concrete instantiations:
 *
 *      Program 1 ("decidable"):
 *        Searches for x^2 - y^2 - z^2 = 1.
 *        The equation is solvable (x=1, y=0, z=0); this program terminates.
 *
 *      Program 2 ("undecidable"):
 *        For each k = 0, 1, 2, ... with k not congruent to 4 or 5 (mod 9),
 *        searches for integer x, y, z such that x^3 + y^3 + z^3 = k.
 *        Advances to k+1 as soon as a solution for k is found.
 *        This program terminates if and only if every integer not congruent
 *        to 4 or 5 (mod 9) is a sum of three integer cubes — an open
 *        conjecture in number theory.  Whether it terminates is therefore
 *        an open problem in mathematics, permanently (not just until some
 *        single value like 114 is resolved).
 *
 * FORMAL CLAIM (proved in rice.v / Theorem Rice_Theorem):
 *
 *   No static analyzer can correctly determine, for all programs of the
 *   form below, whether they terminate. Any analyzer that could do so
 *   would decide the solvability of arbitrary Diophantine equations —
 *   which is impossible by the MRDP theorem (Hilbert's Tenth Problem).
 *
 *   Formal proof: rice.v (Rocq/Coq 8.20)
 *   MRDP mechanization: https://github.com/uds-psl/coq-library-undecidability
 *
```

https://raw.githubusercontent.com/endrazine/rice-constructive/refs/heads/main/undecidable.c

25

## Slide 26

#### Our final C Program ( "the AI Show Stopper : Exploiting a bug in Mathematics") : undecidable.c

For each i in [0 ; 2⁶⁴ − 1], find {xᵢ,yᵢ,zᵢ} in ℤ³ such that:

xᵢ³ + yᵢ³ + zᵢ³ = i

The Question : Given a C program that bruteforces a solution for each i, "will this algorithm stop ?" is undecidable

26

## Slide 27

# 𝕯𝕰𝕸𝕺

A Practical implementation of the "Halting Point" Problem in C, based on the 10th Hilbert Problem

27

## Slide 28

###### The AI Security Prayer (aka "Solving Security")

If you believe in AI,
Clap your hands 👏 👏

If you believe in Mythos,
Clap your hands 👏 👏

If you believe in AI,
If you believe in Mythos,
If you believe in AGI,
Clap your hands 👏 👏

## Slide 29

#### Proving Exploitability : The "Reachability Problem"

*Large call-graph rendering of a stripped binary: hundreds of tiny function nodes joined by call edges; one node at the top is highlighted in green and one node in the middle right is highlighted in red.*

Entry point

Vulnerable function

The "reachability problem" is undecidable.

29

## Slide 30

### Building a n-day Pipeline

Envy

30

## Slide 31

###### Re-Fuzzing CVE-2023-2804 : Heap Based Overflow in Libjpeg-turbo

*Screenshot of the libjpeg-turbo GitHub issue tracker:*

**Heap Buffer Overflow in /libjpeg-turbo/jquant2.c:224 at prescan_quantize() (SIGSEGV)** #668

`Closed`

chameleon10712 opened on Mar 25, 2023

**Have you searched the existing issues (both open and closed) in the libjpeg-turbo issue tracker to ensure that this bug report is not a duplicate?**

Yes

**Does this bug report describe one of the [two known and unsolvable issues with the JPEG format]?**

No

**Clear and concise description of the bug:**

I found a poc which can cause djpeg crash when fuzz testing.

> AddressSanitizer report it a heap buffer overflow in /libjpeg-turbo/jquant2.c:224 at prescan_quantize()

**Steps to reproduce the bug (using *only* libjpeg-turbo):**

Normal run:

```
$ ../build_norm/djpeg -colors 10 -rgb565 ./poc1min.jpg
fish: “../build_norm/djpeg -colors 10…” terminated by signal SIGSEGV (Address boundary error)
```

Asan report:

```
$ ../build_asan_g/djpeg -colors 10 -rgb565 ./poc1min.jpg
=================================================================
==2390006==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x62900000939a at pc 0x7f0438ef479b bp 0x7ffeb86ef390
READ of size 2 at 0x62900000939a thread T0
    #0 0x7f0438ef479a in prescan_quantize /home/oceane/fuzz_test/new_djpeg/libjpeg-turbo/jquant2.c:224
    #1 0x7f0438eda642 in post_process_prepass /home/oceane/fuzz_test/new_djpeg/libjpeg-turbo/jdpostct.c:192
    #2 0x7f0438eca918 in process_data_context_main /home/oceane/fuzz_test/new_djpeg/libjpeg-turbo/jdmainct.c:381
    #3 0x7f0438e074a4 in output_pass_setup /home/oceane/fuzz_test/new_djpeg/libjpeg-turbo/jdapistd.c:139
    #4 0x560835de2f8f in main /home/oceane/fuzz_test/new_djpeg/libjpeg-turbo/djpeg.c:708
    #5 0x7f0438baa0b2 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x240b2)
    #6 0x560835de4b3d in _start (/home/oceane/fuzz_test/new_djpeg/libjpeg-turbo/build_asan_g/djpeg+0x8b3d)

Address 0x62900000939a is a wild pointer.
SUMMARY: AddressSanitizer: heap-buffer-overflow /home/oceane/fuzz_test/new_djpeg/libjpeg-turbo/jquant2.c:224 in prescan_q
Shadow bytes around the buggy address:
```

31

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

### DEMO

*Right half of the slide: black-and-white photograph of a stone gargoyle statue crouching at the foot of a column.*

33

## Slide 34

###### Building a n-days pipeline : The Practice

*Left: screenshot of the first page of the ARVO paper.*

```
ARVO: Atlas of Reproducible Vulnerabilities for Open-Source Software

Xiang Mei*, Jordi Del Castillo†, Pulkit Singh Singaria*, Haoran Xi†
Abdelouahab Benchikh*, Tiffany Bao*, Ruoyu Wang*, Yan Shoshitaishvili*
Adam Doupé*, Hammond Pearce‡, Brendan Dolan-Gavitt§
*Arizona State University, †New York University, ‡University of New South Wales, §XBOW
*{n132, psingari, tbao, fishw, yans, doupe}@asu.edu, am.benchikh@esi-sba.dz
†{jordi.d, hx759}@nyu.edu,  ‡hammond.pearce@unsw.edu.au,  §moyix@xbow.com
```

*(the remainder of the screenshot is the paper's Abstract and section "1. Introduction" in small two-column print)*

###### Downstream from OSS-Fuzz

```bibtex
@inproceedings{mei2026arvo,
title = {{ARVO}: Atlas of Reproducible Vulnerabilities for Open-Source Software},
author = {Mei, Xiang and Del Castillo, Jordi and Singh Singaria, Pulkit and Xi, Haoran and Benchikh, Abdelouahab and Bao, Tiffany and Wang, Ruoyu and Shoshitaishvili, Yan and Doup\'{e}, Adam and Pearce, Hammond and Dolan-Gavitt, Brendan},
booktitle = {IEEE European Symposium on Security and Privacy (EuroS\&P)},
year = {2026}
}
```

###### Near Future

```bibtex
@inproceedings{unprompted.au,
title = {Autonomous n-day pipeline},
author = {Valentina Palmiotti},
date = { September 2026},
}
```

34

## Slide 35

###### Building a n-days pipeline : The Practice

*Screenshot of a Harbor registry web UI:*

```
Harbor        Search Harbor...                                    pipeline-bot
```

Projects / Logs

**nvd-repro** | *Developer*

Access Level: Private &nbsp;&nbsp; Quota used: 731.98GiB of unlimited &nbsp;&nbsp; EVENT LOG

Summary | Repositories | Members | Scanner | Policy | Robot Accounts | Configuration

DELETE &nbsp;&nbsp; PUSH COMMAND

|Name|Artifacts|Pulls|Last Modified Time|
|---|---|---|---|
|nvd-repro/cve-2026-7568|1|0|7/12/26, 2:43 AM|
|nvd-repro/cve-2026-7233|1|0|7/12/26, 9:01 AM|
|nvd-repro/cve-2026-55204|1|0|7/12/26, 8:58 AM|
|nvd-repro/cve-2026-55200|1|0|7/12/26, 2:35 AM|
|nvd-repro/cve-2026-55199|1|0|7/12/26, 5:36 AM|
|nvd-repro/cve-2026-5342|1|0|7/12/26, 4:20 PM|
|nvd-repro/cve-2026-5318|1|0|7/12/26, 4:59 AM|
|nvd-repro/cve-2026-45696|1|0|7/12/26, 2:19 AM|
|nvd-repro/cve-2026-41254|1|0|7/12/26, 4:49 AM|
|nvd-repro/cve-2026-40613|1|0|7/12/26, 4:52 AM|
|nvd-repro/cve-2026-40528|1|0|7/12/26, 2:47 AM|
|nvd-repro/cve-2026-39864|1|0|7/12/26, 9:00 AM|
|nvd-repro/cve-2026-3805|1|0|7/12/26, 5:30 AM|
|nvd-repro/cve-2026-34379|1|0|7/12/26, 9:55 AM|
|nvd-repro/cve-2026-27821|1|0|7/12/26, 2:42 AM|

Page size 15 &nbsp;&nbsp; 1 - 15 of 682 items &nbsp;&nbsp; |< &nbsp; < &nbsp; 1 / 46 &nbsp; > &nbsp; >|

LIGHT

Harbor API V2.0

35

## Slide 36

###### Vulnerabilities : Information Evanescence

###### Top 10 reference domains across all NVD CVEs

|Index|Links|Domain|Comment|
|---|---|---|---|
|1|174,961|Github.com|Live|
|**2**|**165,340**|**SecurityFocus.com**|**Bugtraq (⭐⭐⭐⭐⭐)**|
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

### Building a 0day Pipeline

Wrath

37

## Slide 38

**Common Criteria — Evaluation Assurance Levels**

| Level | Descriptor |
| --- | --- |
| 1 | Functionally tested |
| 2 | Structurally tested |
| 3 | Methodically tested |
| 4 | Methodically designed |
| 5 | Semiformally designed |
| 6 | Semiformally verified |
| 7 | Formally verified |

Chart columns: EAL 1, EAL 2, EAL 3, EAL 4, EAL 5, EAL 6, EAL 7

| Technique | EAL span |
| --- | --- |
| Linters / SAST (cppcheck, Semgrep) | 1–3 |
| Commercial SAST (Coverity, Fortify) | 2–4 |
| Sound SAST (Astrée, Polyspace) | 3–5 |
| Fuzzing | 1–3 |
| Taint analysis | 2–4 |
| Symbolic / concolic execution ← (red arrow) | 3–5 |
| LLM code review (general) | 1–2 |
| LLM/agentic pentest (general) | 1–3 |
| Mythos / Glasswing | 1–4 |
| Formal proof | 5–7 |

- EAL 1 — Functionally tested: basic independent testing that the product works as claimed.
- EAL 2 — Structurally tested: adds developer testing, vulnerability analysis, and basic design documentation.
- EAL 3 — Methodically tested and checked: thorough testing with good commercial development practices and tamper evidence.
- EAL 4 — Methodically designed, tested and reviewed: the most common commercial level; adds low-level design and implementation review. Maximum realistic retrofit level.
- EAL 5 — Semiformally designed and tested: requires semiformal design specification and covert channel analysis; specialist techniques needed.
- EAL 6 — Semiformally verified design and tested: adds semiformal verification of the implementation; very few products worldwide reach this level.
- EAL 7 — Formally verified design and tested: full mathematical proof of correctness; reserved for the highest-security environments such as military cryptographic modules

## Slide 39

### Lifting to LLVM

Lust

39

## Slide 40

### Lifting to LLVM for Binary Translation

We Know how to Analyze x86-64 binaries.
Let’s perform a preliminary binary translation from third party architectures to x86-64

*Diagram — green box labelled* **Binary Translation**:

```
Aarch64  --Lifting-->  (LLVM) IR  --Compilation-->  x86-64  --Existing MOABI Analyzer-->  MOABI
```

Exempli Gratia :
Cristina Cifuentes (UQBT, 2000)
Translation from m68k to sparc32

40

## Slide 41

### Lifters

| Lifter | Anvill | RetDec | Rev.ng |
| --- | --- | --- | --- |
| First release | 2019–2020 | 2017 (open-sourced by Avast; research from ~2011) | 2016 (VEE'16 paper; company founded 2014) |
| License | Apache 2.0 | MIT | GPL v2 / commercial |
| Maintained by | Trail of Bits | Community (Avast open-sourced; core team disbanded ~2020) | rev.ng srl (Italian startup) |
| Output IR | LLVM IR | LLVM IR | LLVM IR (via QEMU TCG) |
| Lifting strategy | Spec-driven (uses Remill; per-instruction semantics in LLVM IR) | Pattern-matching + control-flow structuring; full decompiler pipeline | QEMU TCG as first-stage lifter; LLVM IR as second stage |
| Architectures | x86/x64, AArch64, SPARC (via Remill) | x86, ARM, MIPS, PPC, MIPS64, ARM64 | All QEMU-supported (~30+); very broad coverage |
| Primary goal | Binary lifting for analysis & recompilation | Human-readable decompilation to C | Binary lifting; static + dynamic analysis; commercial reverse engineering |
| Notable | Part of the Remill/McSema ecosystem; designed for composability | Integrated into Kali, IDA, Ghidra plugins; most mature decompiler output | Broadest arch support; commercial UI available (rev.ng Studio) |

41

## Slide 42

### Problem : Anvill needs a Decompiler to identify functions

*Screenshot — first page of the article:*

**Unstripping Cloud Container ELF binaries**

Jonathan Brossard
CEDRIC/Isid
Conservatoire National des Arts et Métiers
Paris, France
jonathan.brossard@lecnam.net

*Abstract*—Evaluating the security of containers, as part of the supply chain of Cloud services, has become compulsory with the European Directive NIS2. The binaries used within containers are typically stripped, meaning they do not possess debug symbols, making the evaluation of their security posture more complex. This article focuses on automated ways to recover some of this critical debugging information, a process named unstripping, on Linux x86_64 binaries, such as those presently overwhelmingly used within containers.

*Index Terms*—ELF unstripping, Reverse Engineering, Cloud binaries, NIS2, debugging

I. INTRODUCTION

The recent upgrades to the European legal framework relative to the security of Cloud services mandate that Product Security Incident Response Teams (or PSIRT) offering services in Europe shall report new vulnerabilities affecting their product and services under 24 hours, to their respective national authorities. In particular, the Directive (UE) 2022/2555 [1], dubbed NIS2, renders compulsory the evaluation and reporting of security vulnerabilities under those timelines.

The public disclosure of over 40,000 vulnerabilities under the form of CVEs by the NIST in 2024 [2] (a number up from about 29,000 in 2023), leaves PSIRT teams with the daunting task of evaluating the exposure of their services to over 100 new vulnerabilities published every day. Arguably, the emergence of tools such as Software Bill of Materials (SBOMs), alleviate some of the PSIRT burden by automating the collection of potential vulnerabilities [10] affecting containers, based solely on the versions of the binaries used within such containers. However, recent studies [3] cast a significant doubt over the effectiveness and replicability of such SBOMs. This leaves PSIRT teams with the task of manually verifying potential vulnerabilities reported via SBOMs monitoring [11] through extensive debugging. In particular, a given version of a piece of software may or may not be vulnerable to a given vulnerability, and its CVSS [16] score drastically changed, depending on their exact compilation options [4] [5]. Those hardening properties are currently not reflected in major SBOM standards [9] [6] [7] [8].

Recent studies [13] indicate that the vast majority of containers [12] readily available today operate primarily under Linux and the x86_64 architecture, by as much as 97%. The ELF [15] binaries shipped within those containers are typically production-ready, and in particular have been stripped of debugging symbols, making debugging by PSIRT teams harder.

In this article, we aim to provide a means for PSIRT teams to improve their response time when evaluating their exposure to a given vulnerability within a C/C++ Linux ELF x86_64 binary by automatically unstripping the target binary, meaning entirely or partially retrieving their debug information. We implement several avenues to perform this task in a single application, named *wunstrip*, published under a permissive open-source MIT/BSD-2 license, hoping to foster its study and adoption by the cybersecurity community. To the best of our knowledge, the latter two techniques leveraging the specifics of the x86_64 ELF standard [14] are entirely new.

II. STATE OF THE ART

A. Overview of an ELF executable debug symbols

The need to recover debugging information, and primarily the name and prototype of functions used within binaries is probably as old as debugging itself [24]. The ELF file format [15] features several optional structures and sections. If an executable ELF must have a segment header, its section header is optional [19]. The main symbol table of the binary is typically either not emitted by the compiler (if the -s compiler flag is used with either gcc or clang), or removed after linking by the *strip* command. The debugging sections, in dwarf format [17], can be entirely removed or compiled separately [18], leaving the production-ready executable without debug information.

Current versions of the GNU C Compiler [21] and LLVM's clang [20] toolchains further hide non-exported functions, by applying the *-fvisibility=hidden* flag by default [35], meaning that their symbols and addresses are not present in the final binary's symbol tables. Unless the *-rdynamic* compiler flag is used (which is not the default), in which case, the function symbols and their addresses are kept in the dynamic symbol table of the final binary (in the *.dynstr* and *.dynsym* sections respectively).

As such, a typical executable ELF binary as shipped by major distributions, such as Redhat or Debian, in a container image, does not retain its main symbol table, and possesses no debug symbols, effectively hiding the addresses of functions within the executable. However, debug symbols may be downloaded separately [41].

*Screenshot — GitHub repository page:*

```
https://github.com/endrazine/wunstrip

endrazine / wunstrip (private)                       Type / to search
<> Code   Issues   Pull requests 1   Actions   Projects   Security and quality   Insights   Settings

wunstrip  [Private]                        Watch 0    Fork 0    Star 0

Your main branch isn't protected                     Dismiss   [Protect this branch]
Protect this branch from force pushing or deletion, or require status checks before
merging. View documentation.

main    2 Branches   0 Tags        Go to file  [T]     Add file    <> Code

endrazine  Updated README.md with build instructions.   075a2f3 · 8 months ago    4 Commits
  LIEF @ f4d6835     Added v0.15.1 of LIEF.                      8 months ago
  include            Initial commit of wunstrip.                 8 months ago
  test               Initial commit of wunstrip.                 8 months ago
  .gitmodules        Add libLIEF submodule at version 0.15.1     8 months ago
  Makefile           Updated README.md with build instructions.  8 months ago
  README.md          Updated README.md with build instructions.  8 months ago
  debuglink.c        Initial commit of wunstrip.                 8 months ago
  eh_frame.c         Initial commit of wunstrip.                 8 months ago
  md5.c              Initial commit of wunstrip.                 8 months ago

About
No description, website, or topics provided.
  Readme
  Activity
  0 stars
  0 watching
  0 forks

Releases
No releases published
Create a new release

Packages
No packages published
Publish your first package

Contributors 1
  endrazine Jonathan Brossard
```

42

## Slide 43

### « The Experiment » : Dataset Construction

Leverage « debootstrap » to download chroots for Debian stretch (9), buster (10), bullseye (11), bookworm (12), trixie (13, testing), and forky (unstable) and Ubuntu xenial (16.04 LTS), bionic (18.04 LTS), focal (20.04 LTS), jammy (22.04 LTS), and noble (24.04 LTS) :

```
chroot-bionic-arm64       chroot-forky-arm64     chroot-trixie-arm64
chroot-bionic-armhf       chroot-forky-armhf     chroot-trixie-armhf
chroot-bionic-ppc64el     chroot-forky-ppc64el   chroot-trixie-ppc64el
chroot-bionic-s390x       chroot-forky-riscv64   chroot-trixie-riscv64
chroot-bookworm-arm64     chroot-forky-s390x     chroot-trixie-s390x
chroot-bookworm-armhf     chroot-jammy-arm64     chroot-xenial-arm64
chroot-bookworm-ppc64el   chroot-jammy-armhf     chroot-xenial-armhf
chroot-bookworm-s390x     chroot-jammy-ppc64el   chroot-xenial-ppc64el
chroot-bullseye-arm64     chroot-jammy-riscv64   chroot-xenial-s390x
chroot-bullseye-armhf     chroot-jammy-s390x
chroot-focal-arm64        chroot-noble-arm64
chroot-focal-armhf        chroot-noble-armhf
chroot-focal-ppc64el      chroot-noble-ppc64el
chroot-focal-riscv64      chroot-noble-riscv64
chroot-focal-s390x        chroot-noble-s390x
```

**39,364 binaries**

DOI 10.5281/zenodo.19075909

43

## Slide 44

### Full Dataset Evaluation : RetDec & Anvill

| Architecture | Count | RetDec | Anvill |
| --- | --- | --- | --- |
| ARM64 (aarch64) | 8,933 | 79.1% (7,062) | 15.2% (1,358) |
| ARMv7 (armhf) | 7,930 | 48.8% (3,870) | 8.7% (690) |
| PowerPC64 (ppc64el) | 8,134 | 0.0% (0) | 0.0% (0) |
| RISC-V 64 (riscv64) | 4,952 | 12.3% (609) | 94.1% (4,660) |
| s390x (mainframe) | 9,415 | 3.2% (301) | 68.1% (6,412) |
| **Total** | **39,364** | **29.9% (11,842)** | **33.5% (13,120)** |

44

## Slide 45

### Stratified Evaluation : RetDec, Anvill & Rev.ng
(100 binaries x 5 architectures)

| Architecture | n | RetDec | Anvill | rev.ng |
| --- | --- | --- | --- | --- |
| ARM64 | 100 | 78% | 16% | 85% |
| ARMv7 | 100 | 51% | 9% | 72% |
| PowerPC64 | 100 | 0% | 0% | 0% |
| RISC-V | 100 | 11% | 95% | 23% |
| s390x | 100 | 4% | 69% | 58% |
| **Total** | **500** | **28.8%** | **37.8%** | **47.6%** |

45

## Slide 46

### Per-Architecture Complementarity

| Architecture | Best Tool | Success | Runner-Up |
| --- | --- | --- | --- |
| ARM64 | rev.ng | 85% | RetDec 78% |
| ARMv7 | rev.ng | 72% | RetDec 51% |
| PowerPC64 | (none) | 0% | (none) 0% |
| RISC-V | Anvill | 95% | rev.ng 23% |
| s390x | Anvill | 69% | rev.ng 58% |

46

## Slide 47

### Wsolver : a Full 0day Pipeline

Glutony

47

## Slide 48

### Wsolver : Lifting to LLVM + Symbolic Execution/Abstract Interpretation

```text
Binary
   |  Lifting
   v
LLVM Bytecode
   |
   v
Symbolic Execution & Abstract Interpretation

KLEE
IKOS
SMACK
SeaHorse
   |
   v
LLM Triage (DeepSeek, Mistral)
   |
   v
0days
```

48

## Slide 49

# 𝕯𝕰𝕸𝕺

49

## Slide 50

### Performing a Resurrection

Sloth

50

## Slide 51

###### Vulnerabilities : Information Evanescence

Top 10 reference domains across all NVD CVEs

|Index|Links|Domain|Comment|
|---|---|---|---|
|1|174,961|Github.com|Live|
|**2**|**165,340**|**SecurityFocus.com**|**Bugtraq (⭐⭐⭐⭐⭐)**|
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

```
jonathan@blackbox:~$ whois securityfocus.com
…
The Registry database contains ONLY .COM, .NET, .EDU domains and
Registrars.
Domain Name: securityfocus.com
Registry Domain ID: 5068534_DOMAIN_COM-VRSN
Registrar WHOIS Server: whois.brandsight.com
Registrar URL: https://gcd.com
Updated Date: 2025-12-30T15:26:27Z
Creation Date: 1999-01-30T05:00:00Z
Registrar Registration Expiration Date: 2027-01-30T05:00:00Z
Registrar: GoDaddy Corporate Domains, LLC
Registrar IANA ID: 3786
Registrar Abuse Contact Email: abuse@gcd.com
Registrar Abuse Contact Phone: +1.5188315864
Domain Status: clientTransferProhibited https://icann.org/epp#clientTransferProhibited
Registrant Organization: Accenture Global Services Limited
Registrant State/Province: IE
Registrant Country: IE
…
jonathan@blackbox:~$
```

52

## Slide 53

###### Rise from the Deads

*Screenshot of the GoDaddy domain-sale page for securityfocus.com:*

GoDaddy — Excellent 4.6 out of 5 ★ Trustpilot

The domain name

**securityfocus.com**

It's for sale!

**Get this domain**

Purchase it today for $175,000.00 or make an offer.

- (●) Buy now — USD 175,000.00
- (○) Make an offer

[ Following ]

- ✓ Free transaction assistance
- ✓ Secure payments
- ✓ Local currency available in the cart at checkout ⓘ

VISA | Mastercard | AMERICAN EXPRESS | PayPal | Alipay

Safe and secure transactions — Quick and easy transfers — Hassle-free payments

**The easy, and safe, way to buy domain names**

Whatever type of domain you wish to buy or rent, we guarantee a simple and secure transfer.

**Here is how it works** →

Need help? Call us. 480-651-9741

53

## Slide 54

###### The Resurrection

*Screenshot of the GoDaddy domain management page for securityfocus.com:*

**Domain**  [ Connect Domain ]

securityfocus.com — Domain Status: IDLE

Overview | DNS | **Registration Settings** | Products | Activity Log

**Contact Info** ⓘ  [ Edit ]

Your contact info won't show in our public WHOIS directory when Domain Privacy is on.

- Name: Jonathan Brossard
- Address: *[blacked out]*
- Telephone: *[blacked out]*
- Email: jonathan.brossard@moabi.com

**Domain Privacy: On** ⓘ  [ Change ]

Your personal contact info is replaced in our public WHOIS directory with details from our partner, Domains by Proxy®.

- Organization: Domains By Proxy, LLC
- Name: Registration Private
- Address: DomainsByProxy.com, 100 S. Mill Ave, Suite 1600, Tempe, Arizona, United States 85281
- Telephone: +1.4806242599
- Email: securityfocus.com@domainsbyproxy.com

54

## Slide 55

###### The Resurrection

*Diagram of four boxes: the Symantec logo, with an arrow pointing right to the BROADCOM logo; from BROADCOM a diagonal arrow points down-left to the accenture logo; from accenture an arrow points right to a photo of the speaker's face superimposed on a black devil silhouette with horns and a tail.*

55

## Slide 56

##### **Thanks for your attention**

*PSIRT logo (black circle, top right).*

56

## Slide 57

###### Illustrations & Copyrights

Cover Page: Giomodica,  Creative Commons Attribution
3.0 Unported license, https://web.archive.org/web/20161011041054/http://www.panoramio.com/photo/5820740

Logo: By Unknown author, CC BY-SA 4.0, https://commons.wikimedia.org/w/index.php?curid=69056451

Sad Gargoyle: WDWParksGal, Creative Commons Attribution 3.0 LicenseCreative Commons Attribution 3.0 License, https://www.deviantart.com/wdwparksgal-stock/art/Gargoyle-Stock-Photo-IMG-1734-640555082

David Hilbert: Unknown Author, Public Domain, https://commons.wikimedia.org/wiki/File:Hilbert.jpg

Kurt Godel: Unknown Author, Public Domain,
https://commons.wikimedia.org/wiki/File:Young_Kurt_G%C3%B6del_as_a_student_in_1925.jpg

Clown: Linnaea Mallette, CC0 Public Domain, https://www.publicdomainpictures.net/en/view-image.php?image=449753&picture=clown-zombie-face-and-teeth

57

