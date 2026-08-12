---
title: "Throw Out the Alphabet Token-Based Markov Chains for Password Cracking"
speakers: ["Jon Gorenflo"]
conference: "DEF CON"
conference_full: "DEF CON 34"
edition: "34"
year: null
source_pdf: "DEF CON 34/DEF CON 34 - Jon Gorenflo - Throw Out the Alphabet Token-Based Markov Chains for Password Cracking - 260727.pdf"
pages: 45
sha256: "42a0e82f970d87a495f196d58ba8c8a6cf86e7430df1a63695353d3d330d033b"
text_chars: 23231
ocr_pages: 0
has_ocr: false
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2"
converted_at: "2026-08-12T00:23:13Z"
---
# Throw Out the Alphabet Token-Based Markov Chains for Password Cracking

**Speakers:** Jon Gorenflo  
**Conference:** DEF CON 34  
**Source:** `DEF CON 34/DEF CON 34 - Jon Gorenflo - Throw Out the Alphabet Token-Based Markov Chains for Password Cracking - 260727.pdf` (45 pages)


## Slide 1

## **THROW OUT THE ALPHABET: TOKEN BASED MARKOV CHAINS FOR PASSWORD CRACKING**

Jon Gorenflo | @flakpaket

## Slide 2

From the first (wrong) attempt to the first real signal

ORIGIN STORY / ITERATION

## Slide 3

### ARTIFICIAL, BUT NOT INTELLIGENT

- Using tokens as a password cracking primitive bounced around in my head for a while before I did anything.

- When I finally did, I half heartedly described the research project to my research assistant and went back to work.

- Claude’s first test?

**Me** : Hey Claude… _Claude did things…._

**Claude** : Tokenizer tokens as a flat dictionary is ineffective for password guessing.

- Surprise! Tokenizer tokens as a flat password list is ineffective. Thanks, Claude. Who could have guessed?

## Slide 4

##### COMBINATOR: EARLY ATTEMPTS

- Once redirected to the intended combinator-style attack, it showed weak but real promise.

   - **Fragments** = LLaMA subword pieces (e.g. the, ing, iam, girl)

   - **Whole-PW** = complete common passwords (e.g. 123456, password)

   - Each vocabulary is combined only with itself, never mixed together

- Enough signal to justify digging deeper.

|**Attack Description**|**Fragments**|**Whole-PW**|**Ratio  F / W**|
|---|---|---|---|
|dict  (-a 0)|11|68|0.16x|
|dict + best64 rules|195|1,890|0.10x|
|**combinator  (-a 1)**|**1,499**|**1,261**|**1.19x**|

## Slide 5

###### RANKED PAIRS AND 3-4 TOKENS COMBOS: NO GAINS

**Use 3 or 4 tokens – 10**<sup>**6**</sup> **budget**

**Ranking pairs first (rank-product)**

- For some reason, Claude thought ordering pairs by probability in a combinator attack was worth my tokens and CPU usage

|**Tokens joined (n)**|**Fragments**
**cracks**|**Whole-PW**
**cracks**|
|---|---|---|
|2|65|194|
|3|2|0|
|4|1|0|

- It was not.

- Said another way, “If we try all possible combinations in a set, but change the order, does it change the final result?

Top n=3:

Tokens:  !!!,  !!", and !"!

-
Whole

PW: 123456123456123456

- No. Of course not. Thanks, Claude.

**Takeaway:** Two token combinator attacks worked, but 3 and 4 token attacks regressed to near zero.

## Slide 6

### CLAUDE’S DIY COMPARISON TOOLS

6000
5,658
5000
4000
3000
2000
1,160
1000
594
493
168 194
56 5 65
0
10^5 10^6 10^7
DIY freq-combinator DIY LLaMA-token combinator DIY OMEN stand-in (char 4-gram)

The homemade char-Markov 4-gram ("DIY OMEN stand-in") beats both token combinators by ~9-11x at 1e7. The result that pointed the project at Markov, not combinator. Counts on the 100K RockYou test set.

## Slide 7

### CRACKEN: FULL IMPLEMENTATION OF THE IDEA

**RockYou (consumer)**

**Enterprise union (policy-compliant)**

Cracken JtR OMEN Hashcat

Cracken JtR OMEN Hashcat

2.3%
29.9%
28.5%
21.9%
15.0% 1.1%
13.3%
12.3%
6.7%
5.1% 4.7% 0.3% 0.4%
1.4% 0.1% 0.1%
0.3% 0.6% 0.0% 0.0% 0.0% 0.0% 0.0% 0.0%
10^7 10^8 10^9 10^7 10^8 10^9

- Tool by Shmulik Amar, presented at DeepSec2021

- https://github.com/shmuelamar/cracken

- At 1e9 candidates Cracken overtakes JtR on consumer passwords, 29.9% vs 28.5%, and clears OMEN by 8 points.

## Slide 8

### RESEARCH THAT SHAPED THIS PROJECT

|**Tool**|**Year**|**Granularity**|**Method**|**Notes**|
|---|---|---|---|---|
|Char-Markov research|~2005|Character|Markov|Foundational work|
|PCFG (Weir et al.)|2009|Structure +
strings|Probabilistic grammar|IEEE S&P paper and
DEF CON 17 talk|
|OMEN|2015|Character|Ordered Markov|Widely-used baseline|
|FLA|2016|Character|Neural|Character-level|
|Cracken|2021|Token-aware|Combinator / mask-hybrid|Closest prior art -- not
true token-Markov|
|PassGPT|2023|Character|Neural (LLM)|Character-level
despite being LLM-
based|

## Slide 9

When at first you don’t succeed, do more math.

MOVING TO MARKOV

## Slide 10

### MARKOV FOR DUMMIES

A Markov chain guesses the next symbol from the few symbols just before it.

**u i c k**

**q**

**P(u | q) = 0.97**

Across English text the letter after q is u about 97% of the time. The chain sees only the recent past, never the whole word.

**Bigram (order 1)** Condition on the last 1 character. **P(next | “q”) u 97%     a 2%     i 1%** _Cheap to train, short memory._

**Trigram (order 2)** Condition on the last 2 characters. **P(next | “qu”) a 31%   i 27%   e 25%   o 12%** _Sharper guesses, needs far more data._

**Same math, different alphabet: swap characters for tokens and character transitions like “q → u” become token transitions like “Michael → 99”.**

## Slide 11

## HOW WE TRAIN TOKENOV

**1 Tokenize the password**

**2 Wrap START START … END**

**3 Slide a 3-token window**

**4 Tally every transition**

###### **3-4. One counter per window**

**1. Tokenize the password. DEFCON2026** → **DE | FC | ON | 20 | 26 2. Wrap START START…END START START DE FC ON 20 26 END** Two STARTs: the context is two tokens wide.

**START START DE +1 START DE FC +1 DE FC ON +1 FC ON 20 +1 ON 20 26 +1 20 26 END +1** _Six windows, six counters, from one password._

**One table: previous two tokens, next token, count. Streamed in batches, so nothing else grows.**

## Slide 12

## CASING DECIDES RARITY, NOT LENGTH

|**Password**|**Rarity (bits)**|**Bits / token**|**Segmentation**|
|---|---|---|---|
|hacktheplanet|22.1|7.4|hack | the | planet|
|defcon2026|40.6|10.2|def | con | 20 | 26|
|DEFCON2026|47.7|9.5|DE | FC | ON | 20 | 26|
|DefCon2026|62.2|15.5|Def | Con | 20 | 26|
|HackThePlanet|65.3|21.8|Hack | The | Planet|
|HACKTHEPLANET|68.0|11.3|H | ACK | THE | PL | AN | ET|

**Capitals buy distance** Every capitalized form lands beyond 10⁹, CamelCase worst of all.

**Count is not cost** DEFCON2026 has more tokens than DefCon2026, and 15 fewer bits.

**Lowercase gets cracked** hacktheplanet at 22 bits falls inside a 10⁷ run.

_Scored under gpt2_d12. Rarity = surprisal in bits (−log_ ₂ _p); lower means the model reaches it sooner._

## Slide 13

###### TOKEN-MARKOV WORKS AS A SEGMENTATION PRIMITIVE

Trigram (2-token context) Markov over LLaMA-tokenized RockYou vs the char-Markov baseline. Test: 100K held-out RockYou, MD5.

|**Budget**|**char-Markov 4-gram**|**LLaMA-token 3-gram**|**ratio (LLaMA / char)**|
|---|---|---|---|
|10⁴|18|8|**0.44**|
|10⁵|168|88|**0.52**|
|10⁶|1,160|653|**0.56**|
|10⁷|5,658|3,992|**0.71**|

**The LLaMA-token 3-gram gained on the char-Markov 4-gram at each increasing budget level.**

It works…but not well enough. How can we improve the results?

## Slide 14

#### WOULD YIELD IMPROVE GOING 3-GRAM TO 4-GRAM?

4500
3,992
4000
3500
3000
2500
2000
1500
997
1000
500
0
Trigram (3-gram) 4-gram

- Token-Markov reaches 71% of char-Markov at the top budget, and the ratio climbs as budget grows.

- The tokenizer is a viable segmentation primitive; the flat-dict framing was unfair to it.

- Token n-gram order caps at 3: a 4-gram collapses as long contexts run out of observations.

_Historical / early prototype (token_markov_runs.csv, token_markov_4gram_runs.csv)._

## Slide 15

###### WHAT IF WE CREATE A CUSTOM TOKENIZER?

_A custom BPE trained directly on RockYou, run through the identical Markov framework, and retrained at 128K to rule out vocab size. Cracks at a 10⁷ budget._

|**Method**|**Cracks (10⁷)**|**vs LLaMA-token**|
|---|---|---|
|char-Markov 4-gram|5,658|1.42×|
|LLaMA-token 3-gram|3,992|1.00×|
|RockYou-BPE-30K|2,707|0.68×|
|RockYou-BPE-128K|1,833|0.46×|

- The off-the-shelf LLaMA tokenizer beats the password-trained BPE by 47% at 30K, the surprising direction.

- Matched at 128K, LLaMA still wins 2.2×, so the edge is vocab content, not size.

- Password-BPE gets worse from 30K to 128K: 14M passwords spread over 128K tokens starve each Markov context, so it collapses onto memorized sequences.

- LLaMA survives because its trillions of pretraining tokens give every token enough mass to stay useful.

## Slide 16

ALL METHODS RANKED: ORDER BEATS ARCHITECTURE _Crack rate (%) at 10⁷, sorted by same-domain RockYou._

|**Method**|**rockyou**|**000webhost**|**myspace**|**hotmail**|
|---|---|---|---|---|
|JtR --markov|**6.73**|1.73|5.95|16.88|
|char-Markov 4-gram|5.66|3.39|15.34|17.36|
|LLaMA-token 3-gram|3.99|6.45|31.70|**32.52**|
|RockYou-BPE-30K|2.71|7.23|32.39|32.05|
|RockYou-BPE-128K|1.83|**7.88**|**33.98**|31.54|

- Wait…what just happened?

- This was a dramatic improvement without changing anything other than the target

## Slide 17

### THE CROSS-DOMAIN SURPRISE

Token-Markov loses on RockYou, which it was trained on, but wins on all three cross-domain corpora.

35
32.5%
31.7%
30
25
20
17.4%
16.9%
15.3%
15
10
6.7% 6.5%
5.7% 6.0%
4.0%
5 3.4%
1.7%
0
RockYou (holdout) 000webhost MySpace Hotmail
Tokenov (llama token-Markov) JtR (--markov bigram) OMEN stand-in (char 4-gram)

_Historical / early prototype -- llama token-Markov @10^7 (cross_domain_triangulation_runs.csv)._

## Slide 18

### THE PLATEAU PROBLEM

14
12
10
8
6
4
2
0
10^7 10^8 10^9

_Gains die after 10^8 (+0.49 pts, 10^8->10^9): the unsmoothed model gets stuck emitting suffix variants of one stem (gummybears200 / gummybears12345, soledadentra / soledadentino) and walks into a long junk tail (median length 20)._

_Early prototype, pre-smoothing (h7_1e9_runs.csv, llama_markov_enum, RockYou) -- see Kneser-Ney fix, next slide._

## Slide 19

## FROM COUNTS TO PROBABILITIES

**Backoff catches the rest**

###### **Duplicates count**

###### **Kneser-Ney discount**

Training keeps duplicates. If 123456 appears 200,000 times, its transitions gain 200,000.

Every seen count gives up a fixed discount D. What is left, P = max(c ₃ − D, 0) / c ₂ , is the trigram probability.

The held-back mass λ = D × distinct children / c ₂ flows down to the bigram, and from there to the unigram.

**Where CamelCase falls off the table**

DefCon2026 needs (Def, Con) → 20. That trigram never occurred in RockYou, and the bigram backoff had nothing either, so scoring dropped to the add-k unigram floor. Twice.

**Generation and scoring walk the same table. No inference, just counts and backoff.**

## Slide 20

### KNESER-NEY SMOOTHING

45
41.82%
40
35
30.15%
30
25
20
15 12.48% 12.39% 12.88%
10
6.53%
5
0
10^7 10^8 10^9
Without KN (unsmoothed) With KN

_At 10^9, KN is 3.25x the unsmoothed rate and keeps climbing past 10^8 -- it fixes the plateau. Quality fix, not volume fix: both emit 10^9 candidates. KN pulls length back to realistic (median 20 -> 9); enterprise-compliant share rises 2.49% -> 4.37%._

_Historical / early prototype, same regime as the Plateau Problem slide (h7_1e9_runs.csv, RockYou)._

## Slide 21

SCALING UP: THE MAYA BENCHMARK

Moving to a standardized, larger, more diverse benchmark

## Slide 22

#### MAYA: WE TOOK THE CORPORA, NOT THE FRAMEWORK

###### **What we left**

###### **What MAYA is**

###### **What we took**

- Unified benchmark for generative password guessing

      - The framework itself: model wrappers, scenarios, scoring

   - We reviewed it, read the data, and took the corpora

- Six models, eight leaked corpora, one standard pipeline

   - Clever machinery we would have had to audit line by line

- Nineteen real leaked corpora, already collected and cleaned

   - Not worth the effort when what we needed was the data

- Multiple languages and regions, not just RockYou

###### **We ran our own harness: 100k random holdout per corpus, the full set where it holds fewer than 100k, the same protocol we used on RockYou.**

_Corrias, De Gaspari, Hitaj and Mancini (Sapienza University of Rome). MAYA: Addressing Inconsistencies in Generative Password Guessing through a Unified Benchmark._

## Slide 23

### ENGINEERING CHALLENGES

**Slow CPU performance** Generation ran CPU bound while the GPU sat waiting.

**Memory consumption** Token tables and candidate buffers outgrew the box.

**Resource contention** Training, generation and cracking fought for the same cores.

**Out-of-memory failures** Long runs died hours in and took their progress with them.

**Sorting and priority** Ordering guesses by probability cost more than making them.

**Disk space** Candidate output and checkpoints filled volumes fast.

**Whack-a-mole: every fix spawned the next problem, and every fix was a trade-off.**

## Slide 24

Tokenov vs. Classic Tools

RESULTS, PART 1

## Slide 25

### HEAD-TO-HEAD VS. TRADITIONAL TOOLS

50
45.3%
45
40
35.7%
35
30 27.6%
25.0% 24.7%
25 23.0%
20 18.2%
16.6%
15 13.2%
9.9%
9.1%
10 7.4%
5
2.2% 2.0%
0.6% 0.5% 1.0% 0.8%
0
10^7 10^8 10^9
Tokenov JtR Markov JtR Incremental Hashcat Markov (min6) Classic Markov (min6) OMEN

_Tokenov wins at every budget against all five classical baselines, and the gap widens as the budget grows: 25.0% -> 35.7% -> 45.3% at 10^7/10^8/10^9, vs. JtR Markov 9.1% -> 16.6% -> 27.6% and OMEN 9.9% -> 18.2% -> 24.7%. Mean crack rate, no rules, across all 20 corpora (incl. enterprise_union)._

_Same corpus set, same model class (Kneser-Ney n-gram Markov) -- only the alphabet changes. show_results.py --all -m tokenov_v1,omen_freq,jtr_incremental,jtr_markov,hcmarkov_min6,markov_classic_min6._

## Slide 26

why comparisons get harder from here

The Benchmarking Problem

—

RESULTS, PART 2

## Slide 27

### TRAINING & GENERATION SPEED

|Tool|Training Time|Generation Time (to 10^9)|Status|
|---|---|---|---|
|JtR --markov|—|~42 sec (23.5M/s)|Completed|
|Hashcat markov|—|~57 sec (17.5M/s)|Completed|
|Tokenov (8-thread)|~1.5 min|~5.5 min (3.05M/s)|Completed|
|Tokenov (1-thread)|~1.5 min|~28 min (0.59M/s)|Completed|
|PCFT|—|~11.7 min (1.43M/s)|Completed|
|OMEN|—|~24 min (0.69M/s)|Completed|
|PCFG|—|~1.8 hr (0.16M/s)|Completed|
|FLA|~40 hr (20 epochs, LSTM, RTX 3090)|Completed (out-of-repo redo)|Completed|
|PassGPT|Pretrained checkpoint (not project-
trained)|Plateaued at 332.6M unique; 45.5 hr ETA on 3090|Incomplete — too slow to reach
10^9|

_Tokenov trains in ~1.5 min (rockyou_train_freq, 32.4M lines) and generates 10^9 in ~5.5 min at 8 threads, CPU-only. Neural baselines need hours-to-days of GPU training. Tokenov is 6-8x slower to generate per-candidate than JtR/Hashcat char-Markov -- the tradeoff the time-boxed comparison resolves next._

## Slide 28

### TOKENOV VS. ROCKYOU + BEST66

**Tokenov 1e9, no rules, vs. RockYou wordlist x best66 rules (~940M candidates): matched budget, all 20 corpora, clean regime. Tokenov wins 20/20: mean 45.3% vs. 39.6% (+5.7 pts).**

35.7%
rockyou 48.1%
mate1 35.7% 44.2%
linkedin 18.9% 27.1%
mailru 19.7% 27.9%
libero 33.1% 41.1%
34.1%
yandex 41.9%
zomato 19.8% 27.6%
000webhost 26.6% 33.4%
41.3%
gmail 48.0%
taobao 11.5% 18.1%
60.6%
ashleymadison 66.6%
66.3%
myspace 71.6%
twitter 34.1% 38.8%
hotmail 55.6% 60.2%
faithwriters 70.1% 73.3%
55.6%
phpbb 58.7%
51.7%
yahoo 54.7%
10. 4%
enterprise_union 12.3%
79 .0%
singles 80.3%
hak5 32.2%32.7%
0 10 20 30 40 50 60 70 80 90
RockYou + best66 (~940M) Tokenov (1e9, no rules)

_The win is universal but not uniform: biggest on rockyou itself (tokenov's home distribution) and on harder/non-English sets; smallest where rockyou+best66 is already near-saturated (hak5, singles, enterprise_union). Runtime caveat: rockyou+best66 finishes in ~9s (static list, GPU rules) vs. tokenov's ~348s (244s generate + 104s attack), ~40x cheaper wall-clock despite cracking less._

## Slide 29

WHY BUDGET-BASED BENCHMARKING IS MISLEADING **Candidate-count budgets (10⁷ / 10⁸ / 10⁹) are clean on paper and blind to how cracking actually runs.**

**Generation is not separable** Some tools bake candidate generation into the cracker. There is no clean place to meter it.

**Rules do the heavy lifting** Some tools are only competitive once rulebased mangling is layered on top.

**Slow tools look strong** PassGPT and FLA score well per candidate but take days to train and days to generate. Impractically slow.

**Not every candidate costs the same** A budget treats all guesses as equal. Generation rate, memory and disk decide how many you actually land in an hour.

**The academic math is correct. The practical application often is not.**

## Slide 30

### SHIFTING TO A TIME-BOXED COMPARISON

25
20.6%
20
14.6%
15 13.8%
10.9%
10
6.4%
5 3.8%
0
JtR --markov Tokenov JtR --incremental hashcat -a3 classic PCFG OMEN

_On a fast hash under a wall-clock cap, raw throughput wins no-rules: JtR --markov and hashcat out-crack Tokenov because they generate 10x-100,000x more candidates per second. PCFG and OMEN -- the two slowest generators (0.16M/s, 0.69M/s) -- land lowest; an hour buys them the fewest candidates. Tokenov + best66 rules: 27.7% -- tops every no-rules result here._

_1 hour (3600s), HIBP 1M SHA-1, no rules unless noted -- full 6-method roster on one sample, one hash, one clock (phase23_hibp_runs.csv)._

## Slide 31

### ENTERPRISE-COMPLIANT CRACKS

**Total Cracked**

**Enterprise-Compliant**

14,159
205,917
146,105
109,418
64,398 4,687 4,338
37,963
896
95
Tokenov JtR PCFG OMEN Hashcat Tokenov JtR PCFG OMEN Hashcat

|Method|Total Cracked|Enterprise-Compliant|Share|
|---|---|---|---|
|**Tokenov (gpt2_d12)**|**146,105**|**14,159**|**9.7%**|
|John the Ripper (jtr_markov L264)|205,917|4,687|2.3%|
|PCFG (classic_cov1)|64,398|4,338|6.7%|
|OMEN (omen_freq)|37,963|896|2.4%|
|Hashcat (markov-classic -a3)|109,418|95|0.1%|

_Quality over quantity: same 1-hour HIBP SHA-1 run as "Shifting to a Time-Boxed Comparison," no rules. Enterprise-compliant = >= 8 characters, 3-of-4 complexity (upper, lower, digit, symbol). Each chart uses its own scale. JtR and Hashcat crack more passwords overall, but the ranking reverses on compliant cracks: Tokenov leads with 3x JtR, 3.3x PCFG, 16x OMEN and ~149x Hashcat._

## Slide 32

### RULES AMPLIFY, QUALITY STILL DECIDES

Passwords Cracked in One Hour Cracks per Trillion (dive)
Tokenov PCFG OMEN
49,704
419,868 407,574 44,954
277,074 274,227 29,840
166,129
146,105
113,623
64,398
37,963
No rules best66 dive Tokenov PCFG OMEN

||Method|No rules|best66|dive|
|---|---|---|---|---|
|**Tokenov**||**146,105 (14.6%)**|**277,074 (27.7%)**|**419,868 (42.0%)**|
|PCFG||64,398 (6.4%)|166,129 (16.6%)|407,574 (40.8%)|
|OMEN||37,963 (3.8%)|113,623 (11.4%)|274,227 (27.4%)|

_Same 1-hour HIBP 1M SHA-1 budget per cell, one rig, nine runs. All dive runs are rule-engine bound in pipe mode at roughly 2.3 to 2.7 GH/s, 8 to 9 trillion candidates per hour. OMEN+dive pushed more candidates than PCFG+dive (9.19T vs 8.20T) and still cracked 133k fewer, so the spread is base candidate quality, not feed rate._

## Slide 33

### DECISION FRAMEWORK

|Hash Speed|Winner|Evidence|
|---|---|---|
|Fast, consumer (MD5 / SHA-1)|Char-Markov / GPU brute|30-min MD5: JtR-markov ties Tokenov. HIBP SHA-1 (1 hr): brute 10.7% > OMEN 5.8% >
Tokenov 4.0%.|
|Fast, enterprise-policy (NTLM /
NetNTLMv2)|Tokenov|NTLM 7.40% vs. OMEN 3.16% (2.3x); brute cracks only 0.05%.|
|Medium (Kerberos RC4)|Tokenov|1.41% vs. OMEN 0.28% (5.0x); brute cracks 0%.|
|Slow (Kerberos AES256 / bcrypt)|Nobody — hash defends|All methods tie near-zero; below statistical resolution.|

_Not just hash speed -- it's hash speed x password policy: on consumer fast hashes, throughput wins; on enterprise-policy fast hashes (NTLM), Tokenov's candidate quality wins even at 35 GH/s, because brute-force and char-Markov barely produce compliant candidates at all._

## Slide 34

### EXPANDING HASH COVERAGE

|Hash Type|Speed|Status|Result (Tokenov vs. OMEN)|
|---|---|---|---|
|MD5 (flat)|Fast|Tested|See head-to-head matrix|
|SHA-1 (HIBP 1M / 9.9M sample)|Fast|Tested|Brute 10.7% > OMEN 5.8% > Tokenov 4.0%
(throughput-won)|
|NTLM|Fast|Tested|7.40% vs. 3.16% (2.3x)|
|NetNTLMv2|Fast / Medium|Tested|7.40% vs. 3.20% (2.3x)|
|Kerberos RC4 (etype 23)|Medium|Tested|1.41% vs. 0.28% (5.0x)|
|Kerberos AES256 (etype 18)|Slow|Tested (underpowered)|0.30% — tie / noise|
|sha512crypt / bcrypt|Slow|Tested (at ceiling)|~0% for all — hash defends|

_Token beats char 2.3-5.0x wherever there's measurable signal on enterprise-policy passwords, across NTLM / NetNTLMv2 / Kerberos RC4. On consumer-policy fast hashes and hash-defended slow algorithms, raw throughput or the hash itself dominates instead._

## Slide 35

tokenov, TACK, and Tangent

MEET THE TOOL

## Slide 36

### SETUP: BOOTSTRAP

- One command handles everything: downloads RockYou (via SecLists), builds the custom "Tokenov B1" -

- tokenizer, trains a frequency weighted model.

- - - -

- Full RockYou equivalent vocabulary (~33 34M tokens/words), frequency weighted for probabilistic ordering. Tool -

- itself ~9MB; resulting model ~250 300MB.

```
$ time tokenov bootstrap
tokenov bootstrap —plan:
...
[04:48:18] [bootstrap] done. Registered model 'tokenov_v1'.
Simple test:  tokenov generate --count 10 --strict
real    1m8.313s
user    6m27.040s
sys     0m3.783s
```

_~1 minute wall-clock (real 1m8s) on a modern machine, 8 threads -- user time exceeds real time because training is multi-core._

## Slide 37

### GENERATION: GENERATE

- -

- Defaults to the best performing configuration out of the box.

- Pipes directly to Hashcat or saves to file.

   - **`$ tokenov generate \`**

      - **`| hashcat -a 0 -m 0 hashes.txt -r best66.rule`**

_Candidates stream straight into Hashcat over a pipe -- no intermediate wordlist file, no disk round trip._

## Slide 38

### SEEDED & WEIGHTED GENERATION

- -

- Feed in OSINT derived wordlists (e.g. via CeWL) as seeds.

- • Tokenov generates candidates by appending/completing around those seed words using learned token transitions.

## Slide 39

### THE ENTERPRISE FLAG (--ENTERPRISE)

14
12.3%
12
10
8
6.3%
6
4
2.3%
2
1.1%
0
10^8 10^9
Tokenov OMEN

_On the Enterprise Union corpus (100% policy-compliant by construction), Tokenov beats OMEN 5.7x / 5.3x at 10^8 / 10^9 (6.3% vs. 1.1%; 12.3% vs. 2.3%). -- enterprise bakes compliance into generation directly; other tools only approximate it with post-hoc rules._

_Enterprise Union: n=83,867, union of test splits of ~17 leak corpora, filtered to length>=8 AND >=3 of 4 character classes, RockYou-training-clean._

## Slide 40

### TACK: TOKEN ANALYSIS AND CRACKING KIT

**TACK is to tokens what PACK is to characters.**

###### **tokdiff**

###### **tokstats**

**--recommend**

Profile one corpus under one tokenizer.

Diff two corpora, or two tokenizers, by lift in log ₂ .

Sweep every tokenizer and rank which fits a crack set.

###### **What tokstats reports**

- Fertility (tokens per password), vocab utilization, single-char and byte fallback rates

- Top token unigrams, bigrams and trigrams

- Token class census, U/L/C/M/D/S/X, and class shapes: Spring2024! becomes CDS

- First and last token class distribution, coverage curve, single-token passwords

**Reports data, not opinions. Deterministic, read-only, one dependency, bring your own tokenizer.**

## Slide 41

#### TANGENT: SEMANTIC OSINT WORDLIST EXPANDER

**A geometric thesaurus for cracking: seeds in, related words and entities out. No model inference.**

**meaning**

**semantic**

wikipedia2vec word and entity vectors, for entity associations.

fastText Common Crawl 2M, for whole-word similarity.

**Blender adds example: tesla, archie griffin -b** Contextual digits and years per term 1974, 1975 **-bb** Boundary-aware case, joins, separators ArchieGriffin, archie_Griffin **-bbb** Per-component substitution leet-ish component swaps

###### **Rules cannot do this: where the case and join fall is data-dependent. Blind leet swaps stay rules' work.**

Real output: tesla → teslamotors, powerwall, nikola. fremont → milpitas, sunnyvale. Python CLI v0.15.0, FAISS-backed, pipes into hashcat, John or tokenov.

## Slide 42

Recap, where to get it, and Q&A

CLOSING

## Slide 43

### RECAP

- **The full arc:**

   - Tokenizer insight

   - Literature gap

   - Trigram discovery

   - -

   - Cross domain generalization

   - -

   - MAYA scale benchmarking

   - The practical benchmarking problem

   - The tool itself

## Slide 44

### WHERE TO GET IT

- —

- Links / repo / contact to be finalized before the talk.

- Jon Gorenflo  |  ATTACKD

- jon@attackd.com

## Slide 45

# **?**

**Jon Gorenflo** |  Founder, CEO

jon@attackd.com

**Questions?**

ATTACKD |  attackd.com
