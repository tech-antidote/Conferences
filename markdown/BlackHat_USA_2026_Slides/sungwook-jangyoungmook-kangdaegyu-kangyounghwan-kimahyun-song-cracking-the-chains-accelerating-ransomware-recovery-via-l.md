---
title: "Cracking the Chains Accelerating Ransomware Recovery via LLM-Assisted Engineering and Verification"
speakers: ["SungWook Jang", "YoungMook Kang", "DaeGyu Kang", "Younghwan Kim", "Ahyun Song"]
conference: "Black Hat"
conference_full: "Black Hat USA 2026"
edition: "USA"
year: 2026
source_pdf: "BlackHat_USA_2026_Slides/SungWook Jang&YoungMook Kang&DaeGyu Kang&Younghwan Kim&Ahyun Song_Cracking the Chains Accelerating Ransomware Recovery via LLM-Assisted Engineering and Verification.pdf"
pages: 38
sha256: "74d7d46c05d292fcc8df82c2d1724b200dcd6c0d8bdcc61da84d20b2c670599a"
text_chars: 12847
ocr_pages: 1
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T23:16:10Z"
---
# Cracking the Chains Accelerating Ransomware Recovery via LLM-Assisted Engineering and Verification

**Speakers:** SungWook Jang, YoungMook Kang, DaeGyu Kang, Younghwan Kim, Ahyun Song  
**Conference:** Black Hat USA 2026  
**Source:** `BlackHat_USA_2026_Slides/SungWook Jang&YoungMook Kang&DaeGyu Kang&Younghwan Kim&Ahyun Song_Cracking the Chains Accelerating Ransomware Recovery via LLM-Assisted Engineering and Verification.pdf` (38 pages)


## Slide 1

# CRACKING THE CHAINS

Accelerating Ransomware Recovery via LLM-Assisted Engineering and Verification

SungWook Jang · YoungMook Kang Financial Security Institute (FSI) — CSIRT

1

## Slide 2

## WHO WE ARE

SungWook Jang

Malware Analysis · Incident Response Financial Security Institute — CSIRT

###### YoungMook Kang

Malware Analysis · Incident Response Financial Security Institute — CSIRT

2

## Slide 3

## A GUARANTEE SERVICE GOES DARK

Before any analysis, the public already felt it — the incident hit the news the same day:

PRESS   ·   JULY 14, 2025 Major guarantee insurer’s outage disrupts customers — “suspected ransomware attack” “We are treating this as a suspected ransomware attack and mounting a company-wide response to ensure a swift recovery.”

- The affected insurer, 14 July 2025

Behind the outage: a hands-on ransomware attack — and the response that brought it all back

3

## Slide 4

## HOW WE GOT THE DATA BACK

A tight loop of problem and solution — analyze → find the flaw → build the tool → recover

ATTACK ANALYSIS
malware teardown & actor ID

FLAW DISCOVERY
the fatal crypto mistake

TOOL DEVELOPMENT RECOVERY
LLM-assisted decryptor 100% in 81 hours

4

## Slide 5

# DAY 1 INITIAL RESPONSE

Malware teardown and attribution — under the pressure of a live national outage

5

## Slide 6

## MALWARE TEARDOWN - WHAT enc DOES

#### CORE CAPABILITIES

- Generates the ChaCha20 key & nonce

- --limit — max bytes to encrypt

- --ratio — partial-encryption interval

- --device — raw disk vs file targets

- Skips R3ADM3.txt note & .ENCRT files

Decompiled option parser — argc, --device/--keystore/--ratio/--limit

6

## Slide 7

## WHAT enc TARGETS — AND SKIPS

The --exts option drives three code branches — plus two hard-coded skip rules:

THREE TARGETING MODES

- all — every file, no filter

- disk — raw block device, low-level

- <ext-list> — up to 32 extensions

TWO SKIP RULES

   - R3ADM3.txt — its own ransom note

   - *.ENCRT — already-encrypted files

   - (prevents double-encryption)

- `if ( !strcasecmp(name, "R3ADM3.txt") ) { puts("Skipping R3ADM3.txt file"); return; }`

7

## Slide 8

## ATTRIBUTION: THE GUNRA GROUP

###### The ransom note, the .ENCRT extension and TTPs point to Gunra

IDENTIFIED FROM

- Ransom note left as issue.net

- R3ADM3.txt marker filename

- Encrypted extension .ENCRT

- RSA-4096 + ChaCha20 scheme

- Hands-on artifacts in /root/crypt

8

## Slide 9

## STAGING GROUND: /root/crypt

One directory dropped on every server — no C2, everything needed for the attack.

Name Size Compre.. Modified Date

###### enc (encryptor) · issue.net (note) · public.pem (RSA-4096) · s (script) · .keystore · .progress

9

## Slide 10

## PLAN VS REALITY: THE SCRIPT 's'

The staged script tells one story — the binary that actually ran tells another THE PLANNED COMMAND (script 's')

BUT THE BINARY REJECTED THOSE OPTIONS

`unknown option --device —` the executed binary was a different build than the one they prepared

10

## Slide 11

# DAY 2 THE FATAL FLAW

Two lines of broken C turned an unbreakable scheme into a 256-try guess

11

## Slide 12

## HYBRID CRYPTO – BUILD FAST

ChaCha20 key + nonce .keystore
RSA-4096 wrap
32 B + 12 B 512 B
The ChaCha20 keystream XORs the disk; the key is sealed with RSA — normally unrecoverable

Decompiled ChaCha20 keystream generation and XOR loop

12

## Slide 13

## THE .keystore — THE KEY, SEALED

Everything needed to decrypt is packed into one 512-byte blob — then sealed with RSA-4096: PLAINTEXT KEY MATERIAL — 52 bytes

ChaCha20 KEY NONCE RATIO LIMIT
32 B 12 B 4 B 4 B
RSA-4096 wrap .keystore
bn_modexp · parse_pem_public_key 512 bytes on disk

Without the attacker's RSA private key it's meaningless — the lock they trusted. But the key inside was already broken.

13

## Slide 14

## FLAW #1: PREDICTABLE SEED

THE FLAW

- Key material comes from C's rand()

- Seeded with time(0) — whole seconds

- Deterministic: seed decides the key

- A PRNG, never a CSPRNG

~14,400

candidate seeds in a 4-hour window

File timestamps pin the attack window — brute-forcing the seed is trivial

14

## Slide 15

## FLAW #2: srand() INSIDE THE LOOP

The key generator re-seeds every iteration — so every byte is identical:

`time()` is per-second; the loop runs in microseconds. Same seed → same `rand()` → the SAME byte.

32-byte key · 12-byte nonce · all from the flawed generator.

15

## Slide 16

## 256-BIT KEY - 8 BITS OF ENTROPY

The 32-byte key collapses to one repeating byte:

A8 A8

A8 A8 A8 A8 A8 A8 A8 A8 A8 A8 A8 A8 A8 A8

Effective keyspace 2^8 = 256 — guessable in 256 tries. PROOF: two identical files → the same hash

16

## Slide 17

INTERMITTENT ENCRYPTION 1 MB ON - 3 MB OFF

ratio=3 encrypts 1 MB then skips 3 MB. Block entropy maps the pattern and the recoverable plaintext.

Entropy tool — encrypted blocks (8.00) vs normal plaintext, revealing the ratio

17

## Slide 18

DAY 3 BUILDING THE DECRYPTOR From proof-of-concept to a production recovery engine — LLM-assisted.

18

## Slide 19

## LLM-ASSISTED ENGINEERING

###### AI compressed days of reverse engineering into hours — under human direction:

ASSIST RE RECOVER LOGIC GENERATE VERIFY
explain Hex-Rays reconstruct the ChaCha20  draft & port the tool:  entropy, magic bytes,
flag the srand bug keystream Python → C known-plaintext

###### Human insight + AI-assisted engineering + robust infrastructure, working in unison

19

## Slide 20

## THE FIRST CRACK: TIMESTAMP KEYS

Before the byte-repeat trick, the very first PoC exploited the predictable seed head-on:

- THE PROOF

- Encrypt two identical files → bitidentical output •  Same seed → same key & nonce → same ciphertext •  The seed is a Unix timestamp (seconds)

- THE METHOD

- Read file modified-times → a candidate window

- Try each second in range as the srand seed

- Validate: UTF-8 decode + entropy skew < 80%

It worked — but timestamps can be altered and wide windows explode the seed count. So we went deeper.

20

## Slide 21

## ONE TOOL - EVERY CASE

The PoCs became one hardened decryptor — flexible enough for every scenario:

WHAT WE ENGINEERED

- Merged timestamp & fixed-byte PoCs

- Auto-search the key — or specify it

- Partial-encryption ratio & size limit

- Simulate without overwriting the disk

Decryptor CLI — --timestamp · --fixed-byte · --ratio · --limit · --dry-run · --threads

21

## Slide 22

## REBUILDING THE KEYSTREAM

###### The flaw hands us the key — regenerate the exact keystream and XOR it away:

RECOVER KEY
256 tries

REGEN NONCE BUILD KEYSTREAM
same collapse ChaCha20 per block

XOR → PLAINTEXT
cipher ⊕ stream

The malware's read → ChaCha20 → overwrite → skip loop, reversed.

22

## Slide 23

## REVERSING INTERMITTENT ENCRYPTION

Partial encryption isn't only a speed trick — it dictates exactly how the decryptor must run:

1 MB 1 MB 1 MB
3 MB plaintext — skipped 3 MB plaintext — skipped
ENC ENC ENC

##### THE GOTCHAS

- Each 1 MB block = its own ChaCha20 counter (start = 1) — not one continuous stream

- Decrypt the encrypted MBs; copy the plaintext MBs untouched

- XOR a plaintext block by mistake → you corrupt it, so ratio & limit must be exact

   - 1 MB decrypt → 3 MB copy, block by block — the entropy map has to be perfect.

23

## Slide 24

## WHEN ONE KEY WASN'T ENOUGH

Servers sharing one storage volume ran at once

- a single file was encrypted 2–3 times: `.ENCRT.ENCRT.ENCRT`

65,536

double-key combos (256²) 16,777,216

triple-key combos (256³)

Each layer needs its own key — so we peel them one at a time

24

## Slide 25

## PEELING THE LAYERS

Brute-forcing millions of keys across GB-sized files sounds hopeless — until you cheat:

###### KNOWN-PLAINTEXT TARGET

- THE 8-BYTE TRICK

- Sample just 8 bytes at a fixed offset

- Match against a known Oracle header

- ORCLDISKRECO / ORCLDISKDATA signature

- One matching key peels one layer  repeat

###### DOUBLE-KEY EXTRACTION

- 8 bytes instead of a whole GB → double keys in seconds, triple in ~20 minutes

25

## Slide 26

## IS THIS THE RIGHT KEY?

Testing 256 candidate bytes is trivial — knowing which one worked is the hard part. Each sample must pass:

THE VALIDATION PIPELINE

- Entropy gate — sample entropy < 7.5

- Magic bytes — PNG / PDF / ZIP / Oracle

- ASCII ratio — human-readable text %

- Byte diversity — null ratio & unique count

WHY IT MATTERS

- Wrong key → still high-entropy noise

- XOR on plaintext would corrupt it

- So the ratio & limit must match too

- Score > threshold = the real key

- UTF-8 decode — no decode error

256 tries, auto-confirmed — no human eyeballing gigabytes of hex.

26

## Slide 27

## ENGINEERING A 320× SPEEDUP

###### A SIMD / AVX-optimized C engine — 100 GB that took 16 h in Python now decrypts in 147 s

Time to decrypt 100 GB (log scale, lower = faster). AVX2-optimized C vs pure Python

27

## Slide 28

## WHY C WON — THE QUARTERROUND

ChaCha20's core is a 32-bit rotation, run hundreds of millions of times — that's where Python dies:

##### THE 32-BIT ROTATION

```
(x << n) | (x >> (32 -n))
```

- C: fixed 32-bit int → one ROL CPU instruction •  Python: bigint → manual overflow + typing overhead

THROUGHPUT — C VS PYTHON

- Optimized C: 355–366 MiB/s (1 core)

- SIMD AVX2: up to 2.19 GB/s

- PyCryptodome: 70–85% of C •  Pure Python: 1–5% of C (GIL blocks threads)

Port the verified logic to C + SIMD → 100 GB from 16 h to 147 s.

28

## Slide 29

## PROOF: THE DATA CAME BACK

###### ENCRYPTED — random bytes

###### RECOVERED — ORCLDISK signature

The decrypted disk block reveals the Oracle **`ORCLDISK RECO`** header — a real, mountable database again.

29

## Slide 30

# DAY 4 RECOVERY

Major services back in 81 hours — every DB server restored.

30

## Slide 31

## 100% RESTORED IN 81 HOURS

All DB servers recovered Public services resumed 81 hours after the attack — full restoration days later

31

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
100% RESTORED IN 81 HOURS
All DB servers recovered
Public services resumed 81 hours after the attack — full restoration days later
June 2025 July 14 5, 11:3
+ Initial compromise + Last DB server + Discovery of ransomware «Creation of double and
ransomware infection encryption logic flaws
+ Creation of a large-capacity,
triple encryption and high-speed decryption tool
decryption and tools
O—-e— @—_e— © —_e—_ © _e—_ @—__e—_ © _e—_@ —__e—__ 9 _e—
—e—@—o
July 14, 2025, 23:00 July 16, 2025, 03:30 ily 17, 2025, 10:00 ly 22, 2025
+ First DB server + Completion of initial
+ Completion of decryption + Normalization of the
ransomware infection malicious ransomware
verification of encrypted affected institution's
operation server files external services
+ 100% restoration of
DB servers
code analysis
black hat
2026 31
```

## Slide 32

## THE 26-HOUR PIVOT

Why did a sophisticated crew ship broken crypto? They changed their whole toolkit at the last minute.

2025.07.12  19:15 KST Legacy build

2025.07.13  21:49 KST Unified binary

2025.07.14  00:49 KST Execution

bespoke, per-server toolsets the pivot — 26 h after the legacy build deployed at once — zero QA time A last-minute shift to a single unified routine — zero time for QA — introduced the flaw we exploited

32

## Slide 33

## WHY THE FLAW EXISTED

LEGACY  (SECURE)

- 40+ bespoke per-server binaries

- 40+ unique RSA key pairs

- Stable — high operational overhead

- No shared crypto weakness

26h pivot

UNIFIED  (FLAWED)

- One "one-size-fits-all" binary

- Compiled 26 h before the attack

- Zero QA before deployment

- Shared srand-in-loop flaw

40+ target-specific builds collapsed into one hasty binary — the root of failure.

33

## Slide 34

## IMPLICATIONS FOR DEFENDERS

###### SERVER-INFILTRATION

DOUBLE EXTORTION

   - Exfiltrate before encrypting

- Hands-on, not spray-and-pray

   - Name-and-shame data-leak sites

- Custom scripts per target

- Linux / Oracle DB in the •  Pressure beyond the lockout crosshairs

RESILIENCE

- Harden the attack surface

- Offline, immutable backups •  Regular restore drills

Detection matters — but recovery is engineered before the attack, and proven after it

34

## Slide 35

## GUNRA HASN'T STOPPED

The same group stays active — tracked on their C2 and their data-leak site

GUNRA DATA-LEAK SITE

DOUBLE EXTORTION

- Exfiltrate data before encrypting

- Name-and-shame on a public leak site

- Pay — or the stolen data is published

Next-wave tooling staged on C2: `Sliver RAT (linux) · OpenSSH-Win64` — monitoring continues

35

## Slide 36

## THE FULL PLAYBOOK

Operation Beyond Backups 2025 Ransomware Threat Response Report Financial Security Institute — CERT · Nov 2025

- End-to-end incident-response lifecycle

- Malware teardown & cryptographic audit

- The decryption-engine architecture

- A No-Ransom blueprint for defenders

36

## Slide 37

### REDEFINING RANSOMWARE RESPONSE THROUGH TECHNICAL RIGOR

The Evolutionary Threat

hands-on, double-extortion ransomware is an engineering challenge, not a lock. • The Power of Depth — even "impossible" attacks hide implementation flaws. • Resilience is a Choice — proactive ASM + immutable, tested backups.

The No-Ransom Blueprint human insight + AI-assisted engineering + robust infra, in unison.

37

## Slide 38

# THANK YOU

Financial Security Institute — Code Analysis Team SungWook Jang · YoungMook Kang DaeGyu Kang · Younghwan Kim · Ahyun Song swjang@fsec.or.kr ·  #BHUSA  @BlackHatEvents kangyoungmook@fsec.or.kr kr · #BHUSA  @BlackHatEvents

38
