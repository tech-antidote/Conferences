---
title: "Bring Your Own Root Of Trust"
speakers: ["Mickey Shkatov", "Jesse Michael"]
conference: "DEF CON"
conference_full: "DEF CON 34"
edition: "34"
year: 2026
source_pdf: "DEF CON 34/DEF CON 34 - Mickey Shkatov, Jesse Michael - Bring Your Own Root Of Trust - BYOROT V1.pdf"
pages: 25
sha256: "1b669b5ac295ac9fba18ecdbf3f8808e1ded7fc8fe13909784e93213b859be9e"
text_chars: 6024
ocr_pages: 0
has_ocr: false
redacted_secrets: 0
ocr_confidence: null
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2"
converted_at: "2026-08-12T06:39:17Z"
---
# Bring Your Own Root Of Trust

**Speakers:** Mickey Shkatov, Jesse Michael  
**Conference:** DEF CON 34  
**Source:** `DEF CON 34/DEF CON 34 - Mickey Shkatov, Jesse Michael - Bring Your Own Root Of Trust - BYOROT V1.pdf` (25 pages)


## Slide 1

# **`./DC34 FEED_YOUR_COMMUNITY` BYOROT Bring Your Own Root Of Trust**

\```
AUG 06–09 // 2026
\```

\```
L A S V E G A S C O N V E N T I O N C E N T E R
\```

## Slide 2

\```
./DC34 FEED_YOUR_COMMUNITY
\```

/whoami

- Mickey Shkatov - Jesse Michael

\```
AUG 06–09 // 2026
\```

\```
L A S V E G A S C O N V E N T I O N C E N T E R
\```

## Slide 3

\```
./DC34 FEED_YOUR_COMMUNITY
\```

## Background • Roots of trust - concept and history

\```
AUG 06–09 // 2026
\```

\```
L A S V E G A S C O N V E N T I O N C E N T E R
\```

## Slide 4

\```
./DC34 FEED_YOUR_COMMUNITY
\```

Background • Past research – I2C , LPC, Sniffing, etc.

\```
AUG 06–09 // 2026
\```

\```
L A S V E G A S C O N V E N T I O N C E N T E R
\```

## Slide 5

\```
./DC34 FEED_YOUR_COMMUNITY
\```

## Background

• TPM Features

\```
AUG 06–09 // 2026
\```

\```
L A S V E G A S C O N V E N T I O N C E N T E R
\```

## Slide 6

\```
./DC34 FEED_YOUR_COMMUNITY
\```

## Background

### • TPM SPI is fast

\```
AUG 06–09 // 2026
\```

\```
L A S V E G A S C O N V E N T I O N C E N T E R
\```

## Slide 7

\```
./DC34 FEED_YOUR_COMMUNITY
\```

## Background • This is not about bitlocker keys!

\```
AUG 06–09 // 2026
\```

\```
L A S V E G A S C O N V E N T I O N C E N T E R
\```

## Slide 8

\```
./DC34 FEED_YOUR_COMMUNITY
\```

## Background

### • Terminology

- TPM

- SPI

- EROT

\```
AUG 06–09 // 2026
\```

\```
L A S V E G A S C O N V E N T I O N C E N T E R
\```

## Slide 9

\```
./DC34 FEED_YOUR_COMMUNITY
\```

## Background

### • Real example – NVIDIA EROT

\```
AUG 06–09 // 2026
\```

\```
L A S V E G A S C O N V E N T I O N C E N T E R
\```

## Slide 10

\```
./DC34 FEED_YOUR_COMMUNITY
\```

## BYOROT

• Why? • No one has messed with the SPI TPM like this yet, the bus is too damn fast!

\```
AUG 06–09 // 2026
\```

\```
L A S V E G A S C O N V E N T I O N C E N T E R
\```

## Slide 11

\```
./DC34 FEED_YOUR_COMMUNITY
\```

## BYOROT

• Sniffing SPI is not new, but can we make a fake TPM?

\```
AUG 06–09 // 2026
\```

\```
L A S V E G A S C O N V E N T I O N C E N T E R
\```

## Slide 12

\```
./DC34 FEED_YOUR_COMMUNITY
\```

## BYOROT

• Trying to make a fake SPI TPM:

- Can we use wait states to tell the host to wait while we do slow processing?

- • Can we interpose the SPI and and use signature based byte seuqneces?

\```
AUG 06–09 // 2026
\```

\```
L A S V E G A S C O N V E N T I O N C E N T E R
\```

## Slide 13

\```
./DC34 FEED_YOUR_COMMUNITY
\```

## BYOROT

### • Requirements

- We need to know how to code in LITERALY ANYTHING

- Ain’t nobody got time to learn! Let’s use AI!

- Must be done in windows using vscode using HW that is cheap and easily accessible

\```
AUG 06–09 // 2026
\```

\```
L A S V E G A S C O N V E N T I O N C E N T E R
\```

## Slide 14

\```
./DC34 FEED_YOUR_COMMUNITY
\```

## BYOROT

- much faster

   - Started using OpenAI Pro with codex

   - • Ended up using Opus 4.6 for the PoC

   - • Extended capabilities with Opus 4.8.

   - Claude wins

\```
AUG 06–09 // 2026
\```

\```
L A S V E G A S C O N V E N T I O N C E N T E R
\```

## Slide 15

\```
./DC34 FEED_YOUR_COMMUNITY
\```

## BYOROT

### • HW set up guide

- Pick your target PC

- Which logic analyzer to use?

- Jumper wires? Yeah, got to get them short ones!

- • Custom headers and solder, solder, solder!

\```
AUG 06–09 // 2026
\```

\```
L A S V E G A S C O N V E N T I O N C E N T E R
\```

## Slide 16

\```
./DC34 FEED_YOUR_COMMUNITY
\```

## BYOROT

- War stories.

- • Before this final result there were casualties

- • Raspberry Pi Pico

- • Arduinos

   - STM32 boards

   - ESP32

\```
AUG 06–09 // 2026
\```

\```
L A S V E G A S C O N V E N T I O N C E N T E R
\```

## Slide 17

\```
./DC34 FEED_YOUR_COMMUNITY
\```

## BYOROT

- FPGA wins!

- Challenge was number of LUTs

- • Started with an IceBreaker 5K LUTs, was good but not good enough

- • Tang Nano 20K was the winner

   - ~$40 on Amazon (2-day delivery)

   - • Open tool chain

   - Will work with APIO in vscode

\```
AUG 06–09 // 2026
\```

\```
L A S V E G A S C O N V E N T I O N C E N T E R
\```

## Slide 18

\```
./DC34 FEED_YOUR_COMMUNITY
\```

## FPGA coding

- How do you program an FPGA?

- • Verilog / HDL / VHDL

\```
AUG 06–09 // 2026
\```

\```
L A S V E G A S C O N V E N T I O N C E N T E R
\```

## Slide 19

\```
./DC34 FEED_YOUR_COMMUNITY
\```

## BYOROT

- Expanding from $40 FPGA to a $150 FPGA

- • Prices have increased since last we checked and the FPGA we originally used is now $250, but the ECP 85F dev kit is still ~$150 on DigiKey.

- • RAM prices are increasing as we speak!

\```
AUG 06–09 // 2026
\```

\```
L A S V E G A S C O N V E N T I O N C E N T E R
\```

## Slide 20

\```
./DC34 FEED_YOUR_COMMUNITY
\```

## BYOROT

• Use case for a fake TPM?

- Anti cheat – HW spoofing

- Measured boot – Fake the PCRs

- Attestation

- AI Infra compromise – if a fake TPM would cost you even $10K to make but the server costs $500K

\```
AUG 06–09 // 2026
\```

\```
L A S V E G A S C O N V E N T I O N C E N T E R
\```

## Slide 21

\```
./DC34 FEED_YOUR_COMMUNITY
\```

## DEMO

\```
AUG 06–09 // 2026
\```

\```
L A S V E G A S C O N V E N T I O N C E N T E R
\```

## Slide 22

\```
./DC34 FEED_YOUR_COMMUNITY
\```

- What does this mean? • Breaking assumptions of hardware immutability

- • Bitlocker

   - Platform Attestation

   - Anti cheat using the TPM

   - Compliance issues

   - Ease that anyone can do this in.

\```
AUG 06–09 // 2026
\```

\```
L A S V E G A S C O N V E N T I O N C E N T E R
\```

## Slide 23

\```
./DC34 FEED_YOUR_COMMUNITY
\```

## What does this mean?

• TPMs are the tip of the iceberg

• Using AI the bar has been lowered to attack more complex hardware by less skilled attackers.

\```
AUG 06–09 // 2026
\```

\```
L A S V E G A S C O N V E N T I O N C E N T E R
\```

## Slide 24

\```
./DC34 FEED_YOUR_COMMUNITY
\```

## Conclusion

• Sharing all the prompts , data and code used to create this code • If you can vibe code a working PoC of a SPI TPM 2.0 at 14MHz in one week, what else can you make?

- Pitfalls and what to avoid

- • Go forth and hack with fun!

\```
AUG 06–09 // 2026
\```

\```
L A S V E G A S C O N V E N T I O N C E N T E R
\```

## Slide 25

\```
./DC34 FEED_YOUR_COMMUNITY
\```

## Questions?

\```
AUG 06–09 // 2026
\```

\```
L A S V E G A S C O N V E N T I O N C E N T E R
\```
