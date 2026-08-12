---
title: "Introduction to Cryptographic Attacks"
speakers: ["Matt Cheung"]
conference: "DEF CON"
conference_full: "DEF CON 33"
edition: "33"
year: 2025
source_pdf: "DEF CON 33 workshops/DEF CON 33 - Workshops - Matt Cheung - Introduction to Cryptographic Attacks - Handout.pdf"
pages: 3
sha256: "8333df89e0f792b7d8fae9ff9ba5a0774f068c173504ecf582c48ba0cee3e36b"
text_chars: 2317
ocr_pages: 0
has_ocr: false
redacted_secrets: 0
ocr_confidence: null
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2"
converted_at: "2026-08-12T06:31:36Z"
---
# Introduction to Cryptographic Attacks

**Speakers:** Matt Cheung  
**Conference:** DEF CON 33  
**Source:** `DEF CON 33 workshops/DEF CON 33 - Workshops - Matt Cheung - Introduction to Cryptographic Attacks - Handout.pdf` (3 pages)


## Slide 1

# Wiener Attack Handout

Matt Cheung

July 24, 2017

First step is to approximate _pqe_<sup>usingcontinuedfractionsofthe</sup> form _a_ 1

with all _ai_ = 1.

## **1 Continued Fraction Expansion**

Continued fraction expansion of a fraction _f_ .

Return _⟨q_ 0 _, q_ 1 _, · · · , qm⟩_ Example: <u>13872719</u><sup>=</sup><sup>_⟨_0</sup><sup>_,_1</sup><sup>_,_1</sup><sup>_,_24</sup><sup>_,_4</sup><sup>_,_1</sup><sup>_,_1</sup><sup>_,_2</sup><sup>_,_2</sup><sup>_⟩_</sup>

## **2 Reconstructing** _f_ **From Expansion**

## **3 Continued Fraction Algorithm**

Let _f_<sup>_′_</sup> be an underestimate of _f_

1

## Slide 2

In this case _f_<sup>_′_</sup> = _pqe_<sup>=</sup> _n_<sup>_<u>e</u>_and</sup><sup>_f_=</sup> _dgk_ Steps of the Algorithm:

- Generate the next quotient ( _qi_<sup>_′_)forthecontinuedfractionex-</sup> pansion of _f_<sup>_′_</sup>

- Construct the following fraction:

- Check if the fraction equals _f_

An important equation _edg_ = _k_ ( _p −_ 1)( _q −_ 1) + _g_ . This allows for guesses for ( _p −_ 1)( _q −_ 1) and _g_ .

Using this guess and<sup>_<u>pq−</u>_</sup><sup><u>(</u></sup><sup>_<u>p−</u>_1</sup> 2<sup><u>)(</u></sup><sup>_<u>q−</u>_1)+1</sup> =<sup>_<u>p</u>_</sup><sup><u>+</u></sup> 2<sup>_<u>q</u>_</sup> Also _<u>p</u>_ <u>+</u> _<u>q p−q</u>_ � 2 �2 _− pq_ = � 2 �2 Through an example we will show how to check do the check step.

_pq_ = 8927 and _e_ = 2621 so _<u>e</u> pq_<sup>=</sup> 8927<sup><u>2621</u></sup>

2

## Slide 3

|Calculated Quantity|How it is Derived|_i_= 0|_i_= 1|_i_= 2|
|---|---|---|---|---|
|_q_<sup>_′_</sup>
_i_
_r_<sup>_′_</sup>
_i_
_n_<sup>_′_</sup>
_i_
_d_<sup>_′_</sup>
_i_|Continued Fraction Expansion
Continued Fraction Expansion
Reconstruction Algorithm|0
2621
8927
0
1|3
1064
2621
1
3|2
493
1064
2
7|
|guess of
_k_
_dg_
guess of _edg_|_⟨q_<sup>_′_</sup>
0<sup>_, q′_</sup>
1<sup>_, · · · , q′_</sup>
_i−_1<sup>_, q′_</sup>
_i_ <sup>+ 1</sup><sup>_⟩_(</sup><sup>_i_ even)</sup>
_⟨q_<sup>_′_</sup>
0<sup>_, q′_</sup>
1<sup>_, · · · , q′_</sup>
_i_<sup>_⟩_(</sup><sup>_i_ odd)</sup>
_e · dg_|1
1
2621|1
3
7863|3
10
26210|
|guess of (_p −_1)(_q −_1)
guess of _g_
|_⌊edg/k⌋_
_edg_mod_k_|2621
0|7863
0|8736
2|
|guess of <sup>_p_+</sup><sup>_q_</sup>
2
guess of
�_p−q_
2
�2
guess of _d_|see above
see above
_dg/g_|3153.5 (quit)|532.5 (quit)|96
289 = 17<sup>2</sup>
5|

3
