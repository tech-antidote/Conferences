---
title: "Going the Distance Long-Range Keystroke Injection via Meshtastic"
speakers: ["Benito Sauceda"]
conference: "DEF CON"
conference_full: "DEF CON 34"
edition: "34"
year: null
source_pdf: "DEF CON 34/DEF CON 34 - Benito Sauceda - Going the Distance Long-Range Keystroke Injection via Meshtastic - Distancev1 0.pdf"
pages: 38
sha256: "552dafd43ee1dac781e3423d5651d248e040da581f9f2545f34b217ce534163a"
text_chars: 6757
ocr_pages: 1
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T00:12:53Z"
---
# Going the Distance Long-Range Keystroke Injection via Meshtastic

**Speakers:** Benito Sauceda  
**Conference:** DEF CON 34  
**Source:** `DEF CON 34/DEF CON 34 - Benito Sauceda - Going the Distance Long-Range Keystroke Injection via Meshtastic - Distancev1 0.pdf` (38 pages)

## Slide 1

Going the Distance: Long-Range Keystroke Injection via LoRa Mesh Networks

## Slide 2

# Act 1 - Hook, Problem: Steel Mountain

### Steel Gates

## Slide 3

# Act 1 - Hook, Problem: Steel Mountain

- Steel Gates

- Armed Guards

## Slide 4

# Act 1 - Hook, Problem: Steel Mountain

- Steel Gates

- Armed Guards

- Security Cameras

## Slide 5

# Act 1 - Hook, Problem: Steel Mountain

- Steel Gates

- Armed Guards

- Security Cameras

- - Badge systems

## Slide 6

# Act 1 - Hook, Problem: Steel Mountain

- Steel Gates

   - Armed Guards

   - Security Cameras

   - Badge systems

   - Air gapped

## Slide 7

## Quick :$ whoami

-Benito Sauceda, AKA “Paperclips Vinny”

## Slide 8

## Quick :$ whoami

-Benito Sauceda, AKA “Paperclips Vinny”

- “Average”  guy

## Slide 9

## Quick :$ whoami

-Benito Sauceda, AKA “Paperclips Vinny”

- “Average”  guy - Average “Friends”

## Slide 10

## Quick :$ whoami

-Benito Sauceda, AKA “Paperclips Vinny”

- “Average”  guy

- - Average “Friends”

## Slide 11

## The familiar Villains:

-Rubber Ducky, Bash Bunny, OMG Cable, etc

Limitations:

## Slide 12

## The familiar Villains:

-Rubber Ducky, Bash Bunny, OMG Cable, etc

Limitations:

## Slide 13

## The familiar Villains:

-Rubber Ducky, Bash Bunny, OMG Cable, etc

Limitations:

- Fire-and-forget

## Slide 14

## The familiar Villains:

-Rubber Ducky, Bash Bunny, OMG Cable, etc

Limitations:

- Fire-and-forget - WiFi Ceiling for C2 (or needs access to the internet)

## Slide 15

## A new Challenger Approaches…

- Remotely triggered

## Slide 16

## A new Challenger Approaches…

- Remotely triggered

- Mile scale (or kilometer for non-americans)

## Slide 17

## A new Challenger Approaches…

- Remotely triggered

- Mile scale (or kilometer for non-americans)

- - No traditional network infrastructure needed

## Slide 18

## A new Challenger Approaches…

- Remotely triggered

- Mile scale (or kilometer for non-americans)

- No traditional network infrastructure needed

- Growing ecosystem of LoRa devices to provide camouflage

## Slide 19

## A new Challenger Approaches…

   - Remotely triggered

   - Mile scale (or kilometer for non-americans)

   - No traditional network infrastructure needed

   - Growing ecosystem of LoRa devices to provide camouflage

- Introducing: The Mesh Injection Apparatus ( M.I.A)

- *add something about nodes here

## Slide 20

## Monkey see, Monkey do:

- HacktheBay, 2026

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Monkey see, Monkey do:
- HacktheBay, 2026 a
= : FIC HACKER
```

## Slide 21

## Monkey see, Monkey do:

- HacktheBay, 2026

- Venky Raju’s Loki

## Slide 22

## Monkey see, Monkey do:

- HacktheBay, 2026

- - Venky Raju’s Loki

- <u>blackhillsinfosec.com/offensive-iot-for</u> -red-team-implants-part-1/

## Slide 23

## What makes M.I.A. Different?

-Reverse Engineered from Scratch

-Speaks Meshtastic Protocol Natively

Benefits:

- Lightweight

- Flexibility to add other functionality

- ● AES-256 CTR Encryption

- Unmodified, regular Meshtastic nodes relay our malicious commands

## Slide 24

# Act 2 - The Build

- Architecture overview (attack chain)

Get Access to target

Plug in MIA into a computer within target

Walk away (MIA recognized as a keyboard by computer) Later, using another Meshtastic Radio, connect to it, Wait until people have gone home for the day Try different Payloads until something sticks.

## Slide 25

## What is LoRa?

-Long Range, low power, sub ghz frequency.

- used in:

- smart agriculture (remote sensors),

- ● military asset tracking,

- ground-to-satellite communications

- ● off grid communications

## Slide 26

## What is LoRa?

-Long Range, low power, sub ghz frequency.

- used in:

- smart agriculture (remote sensors),

- ● military asset tracking,

- ground-to-satellite communications

- ● off grid communications

## Slide 27

## Meshtastic Crash Course

### Technical details we care about

-uses a modulation technique called chirping to enable transferring data long distances

-what’s the range? Theoretical 15km+, tradeoff battery vs range -meshtastic has different presets opting for different trade offs between data rates versus range. Example: LongFast (default) bandwidth = 250.0kHz, link budget of 153dB, and has a range of around 5-8km, but a data rate of 1.07 kbps. Vs short turbo, with a bandwidth of 500kHz, and a link budget of 140 dB, the range is more like 1km, but the data rate is 21.88 kbps.

## Slide 28

## Meshtastic’s Protobuf encoding

What is protobuf? Compact data serialization technique invented by google. Works by bytes having a tag field and a value field.

What does the header mean? Meshtastic’s port nums = which app gets the data. Speaks meshtastic protocol natively, meaning that you can control MIA with any stock meshtastic node natively by just sending the node a duckyscript command with a !mia: prefix.

Your C2 controller is a $20 device.

Of course, the operator experience is best if you flash my firmware, but maybe you want to have your cake and eat it too.

## Slide 29

## ACT 3: Debugging war stories

Sounds great, but how did you do it?

C++ radiolib.h - want to be able to speak meshtastic, but not rely on meshtastic firmware

Radio clock settings

## Slide 30

ACT 3: Debugging war stories Sounds great, but how did you do it? C++ radiolib.h - want to be able to speak meshtastic, but not rely on meshtastic firmware Radio clock settings

## Slide 31

## More debugging

What I like to call **the AES factor** :

- Nonce was garbled - mbedtls aes module incremented counter after each byte, works for streaming data, but not packets like meshtastic uses, took a while to find that one

- Broadcast channel uses AES 128, not 256 like private channels. The default key is aq==, but in hex, the padding was off.

## Slide 32

## More debugging

What I like to call **the AES factor** :

● Nonce was garbled - mbedtls aes module incremented counter after each byte, works for streaming data, but not packets like meshtastic uses, took a while to find that one

● Broadcast channel uses AES 128, not 256 like private channels. The default key is aq==, but in hex, the padding was off.

## Slide 33

Snazzy Demo

## Slide 34

## Considerations, Limitations

- Planting required

- Stuxnet

- LoRa is slow, about 1 kbps on Long Fast.

- Range depends on the environment-

- 8km line-of-sight → 500m in dense urban environments.

- Relays

## Slide 35

## Defense (for Blue Teams)

SDR radio scans aimed at this frequency:

- (Varies by region, but in the US, 902 to 928 MHz)

- Detection gap:

-Mesh broadcasting = finding originating device is hard Defense starts at the USB level:

- “Whitelisting” devices - blocks random USB devices from mounting

- most payloads rely on access to command prompt/powershell

## Slide 36

## Now your turn

Build your own!

-visit theMIA.dev to start!

firmware, schematics for the PCB, etc

theMIA.dev

## Slide 37

## Thanks and references!

- Luis Ayala (for convincing me to submit to a conference)

- - Venky Raju (for inspiring me with his talk)

- - Parents

- Go check out Loki!

- - <u>https://github.com/venkyr/meshtastic-firmware-loki</u>

## Slide 38

## Any Questions? Stay Updated!

Contact me:

### **theMIA.dev**

Personal Blog: SaucedaSecurity.com

<u>benitosauceda@proton.me</u>

Virtual Business Card
