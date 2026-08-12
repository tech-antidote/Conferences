---
title: "How We Taught ChatGPT-4 to Break mbedTLS AES With Side-Channel Attacks"
speakers: ["Witold Waligóra"]
conference: "Black Hat"
conference_full: "Black Hat Europe 2023"
edition: "Europe"
year: 2023
source_pdf: "Black Hat Europe 2023 slides/Witold Waligóra_How We Taught ChatGPT-4 to Break mbedTLS AES With Side-Channel Attacks.pdf"
pages: 30
sha256: "e3a0dcc4156eb1d227ea9ea6a597de1e3d29faf4f0f57500d97d03acfbdabe2d"
text_chars: 9609
ocr_pages: 6
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:13:24Z"
---
# How We Taught ChatGPT-4 to Break mbedTLS AES With Side-Channel Attacks

**Speakers:** Witold Waligóra  
**Conference:** Black Hat Europe 2023  
**Source:** `Black Hat Europe 2023 slides/Witold Waligóra_How We Taught ChatGPT-4 to Break mbedTLS AES With Side-Channel Attacks.pdf` (30 pages)

## Slide 1

## How we taught ChatGPT-4 to break Mbed TLS AES with side-channel attacks

Witold Waligóra

#BHEU   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Q
blackhat
a _e o4-7 CloudVA
ExCel LONDON / UK
How we taught ChatGPT-4
to break Mood LS AES
with side-channel attacks
Witold Waligéra
```

## Slide 2

Who am I MyreLabs, 2010, Founder&CEO Reverse engineering Embedded/IoT security Secure coding High-performance computing

CloudVA, 2021, Founder Side-channels as a service Side-channels as a regression test

#BHEU   @BlackHatEvents

## Slide 3

Agenda 1.  Intro 2.  Why? 3.  How? 4.  Strong sides 5.  Problems & workarounds 6.  Demo! 7.  Conclusions

#BHEU   @BlackHatEvents

## Slide 4

Intro: GPT-4 March 2023: Plugins  GPT-4 can interface with RESTful APIs August 2023: Analysis  GPT-4 can run Python code

#BHEU   @BlackHatEvents

## Slide 5

### Intro: side-channels Physical side-effects of computation  Time taken

>  Power drawn

>  EM Emissions

Fault injections  Clock  Power  EM

#BHEU   @BlackHatEvents

## Slide 6

Intro: side-channels Easier than you think  High initial barrier of entry, but  Everyone uses the same crypto  Everyone uses the same hardware

Find a new zero-day

Re-run the pipeline

#BHEU   @BlackHatEvents

## Slide 7

Why: side-channels The sad state of IoT HWSec  Non-secure element chips  Low clocks

>  No countermeasures

>  Deployed in hostile environments

Cost of attack: a laptop + $100 PicoScope “Clever teenager” threat level

Image by SparkFun Electronics, CC BY 2.0

#BHEU   @BlackHatEvents

## Slide 8

STM32F3, mbedTLS AES Decrypt <u>https://youtube.com/watch?v=CCeK_S3ED4A</u>

#BHEU   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
EUROPE 2025
STM32F3, mbedTLS AES Decrypt
https:/‘youtube.com/watch7v=CCeK S3ED4A
PL
WP YouTube Search
[BR F3-AES-Deay... (2) - Jupyte doudvaio/scci: CloudVA Cl CloudVA
@ 6 doudvaio, N jeOdfe a dt
Template Attack trace gathering
Gather N traces for uniform byte distribution, uniform sbox output HW and uniform FT/RT output HW
, 100000)
#BHEU @BlackHatEvents
```

## Slide 9

Why: GPT-4 Exploring the limits GPT-4 can do time-invariant code What else can it do? Low-cost defense Semi-automatic countermeasures Auto-training

1. Generate code 2. Evaluate leakage 3. Learn 4. Repeat

#BHEU   @BlackHatEvents

## Slide 10

### How: Hardware

●PCIe passthrough USB controllers ●PPPS USB hubs

●ChipWhisperers

●ChipShouters

●Oscilloscopes

●Protocol analyzers ●Debuggers

#BHEU   @BlackHatEvents

## Slide 11

### How: Software Standard virtualization stack

●Linux

●QEMU KVM

●Libvirt

●RESTful API

#BHEU   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
EUROPE 2025
How: Software
Standard virtualization stack <—
*Linux \
-QEMU KVM
°Libvirt
*RESTful API
2 a2cac3da84779ddfc3c569e9dcd81lc9efafbb4To running
17. —=—s- ele0e79093110elebe43 F50d03286118726f61e0 running
#BHEU @BlackHatEvents
```

## Slide 12

### How: GPT-4 plugin OpenAPI specification ●When to use your API

●What and how to call

●How to interpret the results ●Codegen instructions ●Usage examples

#BHEU   @BlackHatEvents

## Slide 13

### GPT-4 plugin

#BHEU   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
EUROPE 2025
GPT-4 plugin
/api/v1/vms/{vmid}/gpt/cpa:
post:
operationId: runCPA
summary: |-
Run Correlation Power Analysis -.on previously gathered traces using provided model.
description: |-
Run Correlation Power Analysis :.on previously gathered: traces
(“tfp_uuid’) using provided model.
Perform: simple evaluation of the results.
The analysis is executed: on the virtual machine indicated by “ymid
parameters:
- name: yvmid
in: path
schema:
type: string
required: true
description: |-
The unique id-of the VM.
A -vmid~ can be obtained. from-*vmList*° or “vmCreate operation.
Any VM with type ~gpt°.can-be used.
requestBody: a.
description: CPA model definition and a pointer to target power traces.
required: true
content:
application/json:
schema:
$ref: '#/components/schemas/runCPARequest
#BHEU @BlackHatEvents
```

## Slide 14

How: GPT-4 plugin Details matter “Do not generate 'main' function” “All symbols except 'entrypoint' should be static.” “The file may use one of the provided cryptographic libraries (mbedtls, wolfssl)” “Function `hw(x)` computes hamming weight of x for bytes and integers” Our CPA endpoint specification is 187 LoC <u>https://cloudva.io/.well-known/ai-plugin.json</u>

#BHEU   @BlackHatEvents

## Slide 15

How: GPT-4 plugin Examples matter more than descriptions Token-denser Provide context Show usage, defaults, conventions Annotated examples are awesome!

#BHEU   @BlackHatEvents

## Slide 16

### Strong sides: GPT-4 Boilerplate

   - Knows APIs better than I do

- Writes faster than I can

- Translations

   - English to code

   - Code to code

- Scientific formula to code

- Self-correcting

   - C/C++ build issues

   - Python imports

   - It’s was right about a loose cable once

#BHEU   @BlackHatEvents

## Slide 17

### Problems

●Context size

●Hallucinations

●BLOB handling ●Timeouts

●Arithmetics

●Metrics interpretation

#BHEU   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
EUROPE 2025
Problems
*Context size
*Hallucinations A 4
‘BLOB handling ==
°Timeouts 7 we
°Arithmetics S&S,
¢Metrics interpretation
```

## Slide 18

Problem: Context size Up to 20 tokens/64-bit element 256 elements = 4K+ tokens April 2023: Unable to produce complete AES S-Box Unable to produce a 200 element random array November 2023: Both problems resolved But still unable to process large pieces of code

#BHEU   @BlackHatEvents

## Slide 19

### Code token size optimization

> ● Process only what you need

> ● Move what you can to separate files and headers

> ● Provide clear naming so model can infer from examples

> ● #define constants away

#BHEU   @BlackHatEvents

## Slide 20

### ID token optimization

Sample Entropy Tok
UUID 550e8400-e29b-41d4-a716- 128 bits 18
446655440000
XKCD1 Tr0ub4dor&3 ~28 bits 8
XKCD2 CorrectHorseBatteryStaple ~44 bits 7
TOK4 HeavyCostWithinLanguage 64 bits? 4

Image by XKCD, CC BY 2.5

#BHEU   @BlackHatEvents

## Slide 21

### Problem: Hallucinations

> ● Calling nonexistent functions

- Importing imaginary modules

- Making up libraries

- Ignoring your instructions

- Mixing up versions

#BHEU   @BlackHatEvents

## Slide 22

### Dealing with hallucinations

- Fail early

- Return meaningful logs

- Provide examples

- Clear and concrete descriptions “is a number” vs “is uint32_t”

- Give in?

#BHEU   @BlackHatEvents

## Slide 23

### Problem: BLOBs

- Can't process large binary data

- Can't store data for later

- Context pollution

- Timeouts

- Serialization

#BHEU   @BlackHatEvents

## Slide 24

### BLOB handling

- Store data on your end

- Even relatively small amounts!

- Only pass IDs around

- Use ID token optmization (yes, we don’t follow our own advice)

- Provide a CRU(D) API Delete needs extra attention

#BHEU   @BlackHatEvents

## Slide 25

### Problem: Timeouts

> ● GPT-4 is not fast

> ● Timing is inconsistent

> ● Plugin calls are just HTTP requests

> ● Subject to request&response timeouts

> ● No sleep/wait-for mechanism It will typically attempt a retry on its own But “Retry-After: [n]“ will be ignored

#BHEU   @BlackHatEvents

## Slide 26

### Fixing timeouts Optimize response times

- Our provisioning takes 0.7s

- VMs respond to ping within 3s

- Are ready to serve GPT endpoints within 10s

- … and that’s not fast enough!

#### Build asynchronous APIs

- Return request ID immediately

- Perform work in the background

- Implement status/progress functions

- Implement wait/sleep on your end

- Return 503 in reasonable time

#BHEU   @BlackHatEvents

## Slide 27

### Live Demo

#BHEU   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
EUROPE 2025
© You
Live Demo
Perform CPA on Mbed TLS AES. Use 50 traces.
REQUEST TO CLOUDVA SIDE-CHANNEL ANALYSIS
"vmid": "873eabai3ceded3271c577efea0faf6b6511£670",
"dutcode": "#include <stdint.h>\n#include <string.h>\n#include
\"mbedtls/aes.h\"\n\nstatic void custom_aes_encrypt(uint8_t *input,
uint8_t *key, uint32_t length) {\n mbedtls_aes_context aes;\n
mbedtls_aes_init(&aes) ;\n mbedtls_aes_setkey_enc(&aes, key, 128);\n
0; i < length; i += 16) {\n mbedtls_aes_crypt_ecb(&aes, MBEDTLS_AES_ENCRYPT,
i, output + i);\n #\n
uint8_t* output, uint8_t* secret,
custom_aes_encrypt(input, output,
}
uint32_t input_len, uint32_t secret_len) {\n
secret, input_len);\n}"
RESPONSE FROM CLOUDVA SIDE-CHANNEL ANALYSIS
"dut_uuid": "40e398e0-9b19-4£70-a3e0-bda528db1i047"
uint8_t *output,
for (uint32_t i =
input +
mbedtls_aes_free(&aes);\n}\n\nvoid entrypoint(uint8_t* input,
Deane ee
0)
REQUEST TO CLOUDVA SIDE-CHANNEL ANALYSIS @
"vmid": "873eabai3ceded3271c577efea0faf6b6511£670",
"tfip_uuid": "d3£82bOf-7ea2-4122-a8e5-6e05f££79bc5",
"model_extra": "from patools.victims.aes_tools import sbox",
"model_hypothesis": "hw(sbox[input[0] “* candidate])",
"model_candidates": "range(256)",
"model_target": "secret[0]"
}
OO
RESPONSE FROM CLOUDVA SIDE-CHANNEL ANALYSIS @
"corr": {
"avg": 0.24634299607714638, ° :
"max": O.4842733144760132, Ss
"min": 0.18558630347251892,
"xeal": 0.4842733144760132
},
"rank": O,
"real_candidate": 176
#BHEU @BlackHatEvents
```

## Slide 28

Conclusions Can GPT-4 do side-channels? Yes Does it solve hard problems? No Is it useful yet? Depends

### Takeaways

How to build a GPT-4 plugin How to work with code Side-channels are easy!

#BHEU   @BlackHatEvents

## Slide 29

# Thank you!

witold.waligora@cloudva.io @WaligoraWitold

linkedin.com/in/witold-waligora

This work has been co-funded by Polish National Centre for Research and Development (NCBR) under project "Evaluation of Side Channel Attack Potential on Embedded Targets (ESCAPE)", proj. sign. PL-TW/VII/5/2020

#BHEU   @BlackHatEvents

## Slide 30

### Extras

#1 [live] Iterative CPA on simple password #2 Fun prompts: "Change leak model to [expr]" Just works "Bisect to find out how many traces it takes" Correct flow, but hits token limits eventually "Extract leak model from publication: [upload]" Biggest problem seems to be loading the paper with its scientific notation intact

#BHEU   @BlackHatEvents
