---
title: "Modern Anti-Abuse Mechanisms in Competitive Video Games"
speakers: ["Julien Voisin"]
conference: "Black Hat"
conference_full: "Black Hat USA 2024"
edition: "USA"
year: 2024
source_pdf: "Black Hat USA 2024 slides/Julien Voisin_Modern Anti-Abuse Mechanisms in Competitive Video Games.pdf"
pages: 63
sha256: "5c270a083bcd790f300536276a36e26dffc5f5e0a19d637715dccb6c12a35649"
text_chars: 13851
ocr_pages: 8
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:33:33Z"
---
# Modern Anti-Abuse Mechanisms in Competitive Video Games

**Speakers:** Julien Voisin  
**Conference:** Black Hat USA 2024  
**Source:** `Black Hat USA 2024 slides/Julien Voisin_Modern Anti-Abuse Mechanisms in Competitive Video Games.pdf` (63 pages)


## Slide 1

Modern Anti-Abuse Mechanisms in Competitive Video Games

Julien Voisin — dustri.org Julien Voisin — dustri.org

#BHUSA   @BlackHatEvents

## Slide 2

### Agenda

- Cheats & abuses?

- Countermeasures

   - Technical

   - Social

   - Exotic

- Conclusion

#BHUSA  @BlackHatEvents

## Slide 3

#BHUSA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
cu
FPS: 68 IGPU: 13.0 vs PING: 1s
i aS VERSION: 71665793
barbwire
le
24 ra]
3
a <0 12:59 2 i ey
MATCH POINT
[29m]
| ‘¢
valk cam Ds
[17m] kapkan
5
mute jammer
is
kapkan
kapkan VA
canta
mite-jammer
C2 , J
DROP , an
bandit § : =
2F Library Hallway
oF
in ee)
```

## Slide 4

#BHUSA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2024
RICOCHET
ANTI-CHEAT
SS OF woccren
```

## Slide 5

Toxicity? Play Counter Strike or League of Legends for 10 minutes to get vivid examples.

#BHUSA  @BlackHatEvents

## Slide 6

### Cheats, abuses, toxicity, …

Cheats aren’t hunted down because they’re morally questionable: they’re hunted down because they disturb the way the game is meant to be enjoyed.

Toxic and abusive behaviours lead to the very same effects.

Those aren’t purely technical issues: they can't be solved by technical means only.

#BHUSA  @BlackHatEvents

## Slide 7

# Technical countermeasures

Like a EDR, but shadier.

#BHUSA  @BlackHatEvents

## Slide 8

### Integrity-based countermeasures

- Open network connections to know cheat servers, C2-style

#BHUSA  @BlackHatEvents

## Slide 9

### Integrity-based countermeasures

- Open network connections to know cheat servers, C2-style

- Presence of some specific files on the filesystem

#BHUSA  @BlackHatEvents

## Slide 10

### Integrity-based countermeasures

- Open network connections to know cheat servers, C2-style

- Presence of some specific files on the filesystem

- Process names and signatures

#BHUSA  @BlackHatEvents

## Slide 11

### Integrity-based countermeasures

- Open network connections to know cheat servers, C2-style

- Presence of some specific files on the filesystem

- Process names and signatures

- Windows names/titles/icons/…

#BHUSA  @BlackHatEvents

## Slide 12

### Integrity-based countermeasures

- Open network connections to know cheat servers, C2-style

- Presence of some specific files on the filesystem

- Process names and signatures

- Windows names/titles/icons/…

- Loaded modules/dll/…

#BHUSA  @BlackHatEvents

## Slide 13

### Integrity-based countermeasures

- Open network connections to know cheat servers, C2-style

- Presence of some specific files on the filesystem

- Process names and signatures

- Windows names/titles/icons/…

- Loaded modules/dll/…

- Specific hardware

#BHUSA  @BlackHatEvents

## Slide 14

### Integrity-based countermeasures

- Open network connections to know cheat servers, C2-style

- Presence of some specific files on the filesystem

- Process names and signatures

- Windows names/titles/icons/…

- Loaded modules/dll/…

- Specific hardware

- Phone number

#BHUSA  @BlackHatEvents

## Slide 15

### Integrity-based countermeasures

- Open network connections to know cheat servers, C2-style

- Presence of some specific files on the filesystem

- Process names and signatures

- Windows names/titles/icons/…

- Loaded modules/dll/…

- Specific hardware

- Phone number

- TPM

#BHUSA  @BlackHatEvents

## Slide 16

### Integrity-based countermeasures

- Open network connections to know cheat servers, C2-style

- Presence of some specific files on the filesystem

- Process names and signatures

- Windows names/titles/icons/…

- Loaded modules/dll/…

- Specific hardware

- Phone number

- TPM

Inspect **everything** , exfiltrate on suspicion

#BHUSA  @BlackHatEvents

## Slide 17

### Integrity-based countermeasures

- Check return addresses/chain of pointers/memory regions/…

#BHUSA  @BlackHatEvents

## Slide 18

### Integrity-based countermeasures

- Check return addresses/chain of pointers/memory regions/…

- HVCI/VBS/… hypervisors all the way down!

#BHUSA  @BlackHatEvents

## Slide 19

### Integrity-based countermeasures

- Check return addresses/chain of pointers/memory regions/…

- HVCI/VBS/… hypervisors all the way down!

- Kernel-level anti-cheats

#BHUSA  @BlackHatEvents

## Slide 20

### Integrity-based countermeasures

- Check return addresses/chain of pointers/memory regions/…

- HVCI/VBS/… hypervisors all the way down!

- Kernel-level anti-cheats

- TPM and Secure Boot

#BHUSA  @BlackHatEvents

## Slide 21

### Integrity-based countermeasures

- Check return addresses/chain of pointers/memory regions/…

- HVCI/VBS/… hypervisors all the way down!

- Kernel-level anti-cheats

- TPM and Secure Boot

- IOMMU all the things!

#BHUSA  @BlackHatEvents

## Slide 22

### Obfuscation

- Classic things: junk code, bogus CFG, CFG flattening, inline functions, implicit flows, instructions substitution, mixed boolean arithmetics …

#BHUSA  @BlackHatEvents

## Slide 23

### Obfuscation

- Classic things: junk code, bogus CFG, CFG flattening, inline functions, implicit flows, instructions substitution, mixed boolean arithmetics … - Anti debugging/vm/modifications/…

#BHUSA  @BlackHatEvents

## Slide 24

### Obfuscation

- Classic things: junk code, bogus CFG, CFG flattening, inline functions, implicit flows, instructions substitution, mixed boolean arithmetics … - Anti debugging/vm/modifications/…

- Move-value-on-change

#BHUSA  @BlackHatEvents

## Slide 25

### Obfuscation

- Classic things: junk code, bogus CFG, CFG flattening, inline functions, implicit flows, instructions substitution, mixed boolean arithmetics … - Anti debugging/vm/modifications/…

- Move-value-on-change

- Shellcode streaming

#BHUSA  @BlackHatEvents

## Slide 26

### Obfuscation

- Classic things: junk code, bogus CFG, CFG flattening, inline functions, implicit flows, instructions substitution, mixed boolean arithmetics … - Anti debugging/vm/modifications/…

- Move-value-on-change

- Shellcode streaming

- Virtualization

#BHUSA  @BlackHatEvents

## Slide 27

#### Side-note: anti-cheats are software too

- Genshin Impact’s mhyprot2.sys

- razer-based injection

- capcom.sys

- - EACKPF

#BHUSA  @BlackHatEvents

## Slide 28

# Social countermeasures

Human powered mitigations!

#BHUSA  @BlackHatEvents

## Slide 29

### Just send the legal department

DMCA, CFAA and even RICO!

- Bossland GmbH vs. Blizzard Entertainment (2017): ~$8.5M

- - EngineOwning UG vs Activision (2024): ~$14.5M

- Elite Boss Tech vs. Bungie (2022): $13.5M

- Aimjunkies vs. Bungie (2024): $63,000

- LeagueSharp vs. Riot: (2017): $10M

- …

Cheat manufacturing/distribution is illegal in South Korea and China.

#BHUSA  @BlackHatEvents

## Slide 30

### Make it expensive to cheat: hardware

#BHUSA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
A ys
black hat
USA as a:
Buy Call of Duty®: Modern Warfare® III a
69,99€ Wea to Cart
Buy Call of Duty®: Modern Warfare@ III - Vault Edition
99,99€ ea to Cart
Buy Diablo® IV a
69,99€ ee to Cart
Buy Diablo® IV - Digital Deluxe Edition LC]
89,99€ WE to Cart
Buy Diablo® IV - Ultimate Edition =
99,99€ ee to Cart
```

## Slide 31

### Make it expensive to cheat: DLC

#BHUSA  @BlackHatEvents

## Slide 32

### Make it expensive to cheat: grind

- Lock competitive behind a number of hours played requirement

- - Make player grind useful equipment

#BHUSA  @BlackHatEvents

## Slide 33

### Empower players

- Reporting (positive and negative) with penalized slander

- Penalties for those benefiting from cheating

- Provide mute/ignore features

- Provide profanity filters

- Peer-based reputation

- Streamer mode

- Private lobbies

- Blocking

#BHUSA  @BlackHatEvents

## Slide 34

#### Machine Learning, AI, ~~blockchain, web3!~~

- Record matches, use ML to pre-filter, have humans validate

- Huge dataset: deviation is easy to spot

- Issue challenges when in doubt

- Use AI for voice chat “moderation”

#BHUSA  @BlackHatEvents

## Slide 35

### Bug-bounties and FUD

- Increase the number of eyeballs, incentivise reporting

- Interesting pricing dynamics

- Blog posts, reports and community managers

#BHUSA  @BlackHatEvents

## Slide 36

### Accounts-level countermeasures

- Add just the right amount of friction: MFA via SMS/tokens, OTP, …

- Account-level "cheater" mark, like Steam is doing

- Account-level DLC/cosmetics/achievements/…

Deters occasional cheaters

#BHUSA  @BlackHatEvents

## Slide 37

### No more instabans

- Makes it hard to understand how/when a cheat was detected

- Incentivise and reward positive behaviours

- Allows players to correct their conduct

#BHUSA  @BlackHatEvents

## Slide 38

# Exotic measures

And now, their weird stuff.

#BHUSA  @BlackHatEvents

## Slide 39

### Cheating is fun, let’s make it tedious!

- Quicksand: random input drops/lag/swap, alter movement speed, …

#BHUSA  @BlackHatEvents

## Slide 40

### Cheating is fun, let’s make it tedious!

- Quicksand: random input drops/lag/swap, alter movement speed, …

- Handicaps: damage output reduction, lame loot, items drop, …

#BHUSA  @BlackHatEvents

## Slide 41

### Cheating is fun, let’s make it tedious!

- Quicksand: random input drops/lag/swap, alter movement speed, …

- Handicaps: damage output reduction, lame loot, items drop, …

- Nonsensical error messages: "Unable to shade polygon normals.”

#BHUSA  @BlackHatEvents

## Slide 42

### Cheating is fun, let’s make it tedious!

- Quicksand: random input drops/lag/swap, alter movement speed, …

- Handicaps: damage output reduction, lame loot, items drop, …

- Nonsensical error messages: "Unable to shade polygon normals.”

- Help honest players: cloaking, damages shield, …

#BHUSA  @BlackHatEvents

## Slide 43

### Cheating is fun, let’s make it tedious!

- Quicksand: random input drops/lag/swap, alter movement speed, …

- Handicaps: damage output reduction, lame loot, items drop, …

- Nonsensical error messages: "Unable to shade polygon normals.”

- Help honest players: cloaking, damages shield, …

- Group players by reputation

#BHUSA  @BlackHatEvents

## Slide 44

### Cheating is fun, let’s make it tedious!

- Quicksand: random input drops/lag/swap, alter movement speed, …

- Handicaps: damage output reduction, lame loot, items drop, …

- Nonsensical error messages: "Unable to shade polygon normals.”

- Help honest players: cloaking, damages shield, …

- Group players by reputation

- Crank up gravity x10,000

#BHUSA  @BlackHatEvents

## Slide 45

### Cheating is fun, let’s make it tedious!

- Quicksand: random input drops/lag/swap, alter movement speed, …

- Handicaps: damage output reduction, lame loot, items drop, …

- Nonsensical error messages: "Unable to shade polygon normals.”

- Help honest players: cloaking, damages shield, …

- Group players by reputation

- Crank up gravity x10,000

- Hallucinations

#BHUSA  @BlackHatEvents

## Slide 46

### Cheating is fun, let’s make it tedious!

- Quicksand: random input drops/lag/swap, alter movement speed, …

- Handicaps: damage output reduction, lame loot, items drop, …

- Nonsensical error messages: "Unable to shade polygon normals.”

- Help honest players: cloaking, damages shield, …

- Group players by reputation

- Crank up gravity x10,000

- Hallucinations

- …

Complement proper anti-cheat, it doesn’t replace it.

#BHUSA  @BlackHatEvents

## Slide 47

Good good. But is it working?

It’s complicated

#BHUSA  @BlackHatEvents

## Slide 48

#BHUSA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2024
Rainbow Six Siege bans
== battleye only = battleye + data
12500 +-
10000 —-
7500 —-
5000 —-
2500 —-
ie)
January 2022 July 2022 January 2023 July 2023 January 2024
```

## Slide 49

#BHUSA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2024
ane Games with a Cheater Weekly
f Games Globally Played with a Scripter (or a Bot)
15% 300 =~ Games
Bans
- 20 «§
¢ 2
2 g
z-) =}
& rm
: :
7 =
8 FA
2 a
a 5% 100 2
Zs
2022-01-01 2022-07-14 2022-01-19 2023-06-08 2023-12-21
```

## Slide 50

#BHUSA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2024
Packman: ie pees ot Type
LoL Anti-Cheat Ser pting Ba Ager ed Weekly
50 ® Manual
= Automatic
40
30
20
idol ss | i a |
2020-10-15 2021-08-05 2022-05-26 2023-03-16 2024-01-04
Weekly Bans (Thousands)
```

## Slide 51

#BHUSA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2024
League of Legends: Bans by System
4000
@ Manual © Hardware ® Vanguard @ Packman
3000
2000
Ss)
8
&
a
2 »
3
3
3
=
1000
```

## Slide 52

#BHUSA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
blackhat ;
USA 2024 ,
WARNINGS TO PENALTIES
100%
RFF
53%
30% WRITTEN CHAT
43% I VOICE CHAT
35%
23% |
TSTWARNING
2ND WARNING SANCTIONS
i]
lu
B
lu
=
—
=
uid
Oo
oe
ud
ao
```

## Slide 53

# Conclusion

This is all interesting, but what’s your point anyway?

#BHUSA  @BlackHatEvents

## Slide 54

### Reflections on the future

- **Feedback and guidance go a long way**

#BHUSA  @BlackHatEvents

## Slide 55

### Reflections on the future

- **Feedback and guidance go a long way**

- Technical means alone aren’t the answer

#BHUSA  @BlackHatEvents

## Slide 56

### Reflections on the future

- **Feedback and guidance go a long way**

- Technical means alone aren’t the answer

- The cat and mouse game will continue

#BHUSA  @BlackHatEvents

## Slide 57

### Reflections on the future

- **Feedback and guidance go a long way**

- Technical means alone aren’t the answer

- The cat and mouse game will continue

- Private cheats will keep working

#BHUSA  @BlackHatEvents

## Slide 58

### Reflections on the future

- **Feedback and guidance go a long way**

- Technical means alone aren’t the answer

- The cat and mouse game will continue

- Private cheats will keep working

- Measuring success is hard

#BHUSA  @BlackHatEvents

## Slide 59

### Reflections on the future

- **Feedback and guidance go a long way**

- Technical means alone aren’t the answer

- The cat and mouse game will continue

- Private cheats will keep working

- Measuring success is hard

- DMA is the current frontier

#BHUSA  @BlackHatEvents

## Slide 60

### Reflections on the future

- **Feedback and guidance go a long way**

- Technical means alone aren’t the answer

- The cat and mouse game will continue

- Private cheats will keep working

- Measuring success is hard

- DMA is the current frontier

- AI will make things worse

#BHUSA  @BlackHatEvents

## Slide 61

### Reflections on the future

- **Feedback and guidance go a long way**

- Technical means alone aren’t the answer

- The cat and mouse game will continue

- Private cheats will keep working

- Measuring success is hard

- DMA is the current frontier

- AI will make things worse

Cheating will always be funnier.

#BHUSA  @BlackHatEvents

## Slide 62

## Questions?

#BHUSA  @BlackHatEvents

## Slide 63

### Sources

- <u>Valorant’s blog, especially the Game Health’s series</u>

- <u>League</u> <u>of L egends’</u> <u>blog</u>

- <u>Rainbow 6: Siege’s blog</u>

- <u>Call of Duty’s blog</u>

- <u>UnKnoWnCheaTs</u>

- <u>The Secret Club</u>

- <u>TorrentFreak</u>

- <u>CheatEngine</u>

#BHUSA  @BlackHatEvents
