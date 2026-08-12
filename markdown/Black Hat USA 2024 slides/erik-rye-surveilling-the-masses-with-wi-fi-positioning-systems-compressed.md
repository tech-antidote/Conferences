---
title: "Surveilling the Masses with Wi-Fi Positioning Systems"
speakers: ["Erik Rye"]
conference: "Black Hat"
conference_full: "Black Hat USA 2024"
edition: "USA"
year: 2024
source_pdf: "Black Hat USA 2024 slides/Erik Rye_Surveilling the Masses with Wi-Fi Positioning Systems_Compressed.pdf"
pages: 97
sha256: "a1465012877065cdf5a6007bbb1668d42c87db6a2f48ab3d90b70b812e2d2511"
text_chars: 17594
ocr_pages: 5
has_ocr: true
redacted_secrets: 0
ocr_confidence: 90.8
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T04:32:58Z"
---
# Surveilling the Masses with Wi-Fi Positioning Systems

**Speakers:** Erik Rye  
**Conference:** Black Hat USA 2024  
**Source:** `Black Hat USA 2024 slides/Erik Rye_Surveilling the Masses with Wi-Fi Positioning Systems_Compressed.pdf` (97 pages)


## Slide 1

Surveilling the Masses with Wi-Fi Positioning Systems

Erik Rye University of Maryland

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 93/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
| Aa
AUGUST 7-8, 2024
BRIEFINGS
Surveilling the Masses with
Wi-Fi Positioning Systems
Erik Rye
University of Maryland
```

## Slide 2

### vitæ

#### **Erik Rye**

- ‣ rye ( _noun)_ a cereal plant that tolerates poor soils and low temperatures

- 🐢

- ‣ University of Maryland Comp Sci PhD Student 🧑🎓

- ‣ Advised by Dave Levin

- ‣ Research interests

   - 🤫 networks 🛜

   - ‣ Security 🔒 privacy

- ‣ Other interests 🐕

- ‣ Dogs

✍ ‣ Fonts, kerning 👶 about Arch 💻 ‣ Telling infants

#BHUSA  @BlackHatEvents

## Slide 3

Wi-Fi Positioning Systems (WPSes)

How mobile devices use Wi-Fi routers as landmarks

#BHUSA  @BlackHatEvents

## Slide 4

### Wi-Fi Positioning Systems (WPSes)

Operated by mobile OS vendors, others - Apple - Google - Microsoft

- Skyhook - Mozilla Location Service 🪦

Apple’s implementation is uniquely vulnerable to certain attacks

#BHUSA  @BlackHatEvents

## Slide 5

WPS

00:11:22:33:44:55

#BHUSA  @BlackHatEvents

## Slide 6

WPS

00:11:22:33:44:55

Basic Service Set Identifier (BSSID)

#BHUSA  @BlackHatEvents

## Slide 7

WPS

00:11:22:33:44:55

#BHUSA  @BlackHatEvents

## Slide 8

WPS

I hear 00:11:22:33:44:55 I’m at 12.34,56.78

00:11:22:33:44:55

#BHUSA  @BlackHatEvents

## Slide 9

WPS

I hear 00:11:22:33:44:55 I’m at 12.34,56.78

00:11:22:33:44:55

#BHUSA  @BlackHatEvents

## Slide 10

WPS

00:11:22:33:44:55

#BHUSA  @BlackHatEvents

## Slide 11

WPS

00:11:22:33:44:55

#BHUSA  @BlackHatEvents

## Slide 12

WPS

66:77:88:99:aa:bb

44:55:66:77:88:99

22:33:44:55:66:77

#BHUSA  @BlackHatEvents

## Slide 13

WPS

66:77:88:99:aa:bb

44:55:66:77:88:99

22:33:44:55:66:77

#BHUSA  @BlackHatEvents

## Slide 14

WPS

Where is 22:33:44:55:66:77?

66:77:88:99:aa:bb

44:55:66:77:88:99

22:33:44:55:66:77

#BHUSA  @BlackHatEvents

## Slide 15

**WPS** Where is 22:33:44:55:66:77?

66:77:88:99:aa:bb

44:55:66:77:88:99

22:33:44:55:66:77

#BHUSA  @BlackHatEvents

## Slide 16

WPS

66:77:88:99:aa:bb

44:55:66:77:88:99

22:33:44:55:66:77

#BHUSA  @BlackHatEvents

## Slide 17

WPS

22:33:44:55:66:77 is at 12.34,56.67 44:55:66:77:88:99 is at 12.33,56.66 66:77:88:99:aa:bb is at 12.32,56.68

66:77:88:99:aa:bb

44:55:66:77:88:99

22:33:44:55:66:77

#BHUSA  @BlackHatEvents

## Slide 18

WPS

22:33:44:55:66:77 is at 12.34,56.67 44:55:66:77:88:99 is at 12.33,56.66 66:77:88:99:aa:bb is at 12.32,56.68 …

66:77:88:99:aa:bb

44:55:66:77:88:99

22:33:44:55:66:77

#BHUSA  @BlackHatEvents

## Slide 19

WPS

22:33:44:55:66:77 is at 12.34,56.67 44:55:66:77:88:99 is at 12.33,56.66 66:77:88:99:aa:bb is at 12.32,56.68 …

66:77:88:99:aa:bb

44:55:66:77:88:99

22:33:44:55:66:77

#BHUSA  @BlackHatEvents

## Slide 20

WPS

22:33:44:55:66:77 is at 12.34,56.67 44:55:66:77:88:99 is at 12.33,56.66 66:77:88:99:aa:bb is at 12.32,56.68 …

66:77:88:99:aa:bb

44:55:66:77:88:99

22:33:44:55:66:77

#BHUSA  @BlackHatEvents

## Slide 21

WPS

I’m at 12.335,56.665!

22:33:44:55:66:77 is at 12.34,56.67 44:55:66:77:88:99 is at 12.33,56.66 66:77:88:99:aa:bb is at 12.32,56.68 …

66:77:88:99:aa:bb

44:55:66:77:88:99

22:33:44:55:66:77

#BHUSA  @BlackHatEvents

## Slide 22

### Apple’s Wi-Fi Positioning System (WPS)

Where is 22:33:44:55:66:77?
22:33:44:55:66:77 is at 12.34,56.67
WPS
44:55:66:77:88:99 is at 12.33,56.66
66:77:88:99:aa:bb is at 12.32,56.68
…

#BHUSA  @BlackHatEvents

## Slide 23

### Apple’s Wi-Fi Positioning System (WPS)

Where is 22:33:44:55:66:77?
22:33:44:55:66:77 is at 12.34,56.67
WPS
44:55:66:77:88:99 is at 12.33,56.66
66:77:88:99:aa:bb is at 12.32,56.68
…

Returns up to 400 additional unrequested BSSID locations per query

#BHUSA  @BlackHatEvents

## Slide 24

### Apple’s Wi-Fi Positioning System (WPS)

Where is 22:33:44:55:66:77?
22:33:44:55:66:77 is at 12.34,56.67
WPS
44:55:66:77:88:99 is at 12.33,56.66
66:77:88:99:aa:bb is at 12.32,56.68
…

Returns up to 400 additional unrequested BSSID locations per query Tracks the location of _ALL_ APs — (was) no way to opt-out

#BHUSA  @BlackHatEvents

## Slide 25

### Apple’s Wi-Fi Positioning System (WPS)

Where is 22:33:44:55:66:77?
22:33:44:55:66:77 is at 12.34,56.67
WPS
44:55:66:77:88:99 is at 12.33,56.66
66:77:88:99:aa:bb is at 12.32,56.68
…

Returns up to 400 additional unrequested BSSID locations per query Tracks the location of _ALL_ APs — (was) no way to opt-out Exposed via an unauthenticated, publicly-accessible API with no rate limit

#BHUSA  @BlackHatEvents

## Slide 26

### Apple’s Wi-Fi Positioning System (WPS)

Where is 22:33:44:55:66:77?
22:33:44:55:66:77 is at 12.34,56.67
WPS
44:55:66:77:88:99 is at 12.33,56.66
66:77:88:99:aa:bb is at 12.32,56.68
…

Returns up to 400 additional unrequested BSSID locations per query

Tracks the location of _ALL_ APs — (was) no way to opt-out

Exposed via an unauthenticated, publicly-accessible API with no rate limit Permits several attacks by a low-power attacker

#BHUSA  @BlackHatEvents

## Slide 27

Apple’s WPS & Black Hat
BH USA ‘12 BH USA ‘21 BH USA ‘24
Surveilling the Masses
iSniff-GPS
IPvSeeYou Enumerating WPS data
Visualizing BSSIDs heard nearby
Geolocating EUI-64 IPv6 addresses Longitudinal analysis

#BHUSA  @BlackHatEvents

## Slide 28

Querying Apple’s WPS for fun and profit

How much can we learn about the world’s Wi-Fi?

#BHUSA  @BlackHatEvents

## Slide 29

### MAC Address Review

48-bit/6-byte hardware identifiers

MAC address(es) of Wi-Fi APs — Basic Service Set Identifier (BSSID) Upper three bytes IEEE-assigned to manufacturers Organizationally-Unique Identifier (OUI)

20:cc:27:a8:92:01

#BHUSA  @BlackHatEvents

## Slide 30

### MAC Address Review

48-bit/6-byte hardware identifiers

MAC address(es) of Wi-Fi APs — Basic Service Set Identifier (BSSID) Upper three bytes IEEE-assigned to manufacturers Organizationally-Unique Identifier (OUI)

20:cc:27:a8:92:01 Cisco Systems

#BHUSA  @BlackHatEvents

## Slide 31

### Naïve Attack — Random BSSID Guessing

WPS

#BHUSA  @BlackHatEvents

## Slide 32

### Naïve Attack — Random BSSID Guessing

Where is 82:95:50:9a:bc:7d?

WPS

BSSIDs are 48 bits — guess random 48-bit numbers

#BHUSA  @BlackHatEvents

## Slide 33

### Naïve Attack — Random BSSID Guessing

Where is 82:95:50:9a:bc:7d?
¯\_( ツ )_/¯

WPS

BSSIDs are 48 bits — guess random 48-bit numbers

#BHUSA  @BlackHatEvents

## Slide 34

### Naïve Attack — Random BSSID Guessing

WPS

BSSIDs are 48 bits — guess random 48-bit numbers

#BHUSA  @BlackHatEvents

## Slide 35

### Naïve Attack — Random BSSID Guessing

Where is 40:85:2b:fe:9b:2a?

WPS

BSSIDs are 48 bits — guess random 48-bit numbers

#BHUSA  @BlackHatEvents

## Slide 36

### Naïve Attack — Random BSSID Guessing

Where is 40:85:2b:fe:9b:2a?

¯\_( ツ )_/¯

WPS

BSSIDs are 48 bits — guess random 48-bit numbers

#BHUSA  @BlackHatEvents

## Slide 37

### Naïve Attack — Random BSSID Guessing

Where is 40:85:2b:fe:9b:2a?

¯\_( `ツ` )_/¯

WPS

BSSIDs are 48 bits — guess random 48-bit numbers

281,474,976,710,656 possible BSSIDs — unlikely to guess an active BSSID

#BHUSA  @BlackHatEvents

## Slide 38

### Improving the Odds

24 bits in OUI; 2<sup>24</sup> ~ 16M possible OUIs

But only 36k OUIs assigned by IEEE

20:cc:27:a8:92:01

Solution: Guess random BSSIDs from allocated OUIs

<u>>99% reduction in search space</u>

#BHUSA  @BlackHatEvents

## Slide 39

### OUI-Based, Intelligent BSSID Guessing

WPS

#BHUSA  @BlackHatEvents

## Slide 40

### OUI-Based, Intelligent BSSID Guessing

Where is 9c:38:18:29:2d:0f?

WPS

Still many “incorrect” BSSID guesses

#BHUSA  @BlackHatEvents

## Slide 41

OUI-Based, Intelligent BSSID Guessing

Cisco Systems
Where is 9c:38:18:29:2d:0f?
WPS

Still many “incorrect” BSSID guesses

#BHUSA  @BlackHatEvents

## Slide 42

OUI-Based, Intelligent BSSID Guessing

Cisco Systems
Where is 9c:38:18:29:2d:0f?
WPS
¯\_( ツ )_/¯

Still many “incorrect” BSSID guesses

#BHUSA  @BlackHatEvents

## Slide 43

### OUI-Based, Intelligent BSSID Guessing

WPS

Still many “incorrect” BSSID guesses

#BHUSA  @BlackHatEvents

## Slide 44

### OUI-Based, Intelligent BSSID Guessing

Where is 94:83:c4:c8:20:12?

WPS

Still many “incorrect” BSSID guesses

#BHUSA  @BlackHatEvents

## Slide 45

OUI-Based, Intelligent BSSID Guessing

GL-iNet
Where is 94:83:c4:c8:20:12?
WPS

Still many “incorrect” BSSID guesses

#BHUSA  @BlackHatEvents

## Slide 46

### OUI-Based, Intelligent BSSID Guessing

Where is 94:83:c4:c8:20:12?

94:83:c4:c8:20:12 is at 34.56,78.9

GL-iNet

WPS

82:19:84:ac:97:42 is at 34.57,78.89 ae:82:99:bf:92:10 is at 34.56,78.91

Still many “incorrect” BSSID guesses

#BHUSA  @BlackHatEvents

## Slide 47

### OUI-Based, Intelligent BSSID Guessing

Where is 94:83:c4:c8:20:12?

94:83:c4:c8:20:12 is at 34.56,78.9

GL-iNet

WPS

82:19:84:ac:97:42 is at 34.57,78.89 ae:82:99:bf:92:10 is at 34.56,78.91

Still many “incorrect” BSSID guesses But, odds of correctly guessing an active BSSID <u>much higher</u>

#BHUSA  @BlackHatEvents

## Slide 48

### OUI-Based, Intelligent BSSID Guessing

Queried Apple WPS for 2<sup>14</sup> random BSSIDs/OUI

“Extra” up-to-400 BSSIDs provide incredible ROI

- 1 day to ~100M BSSIDs

- 4 days to ~500M BSSIDs

#BHUSA  @BlackHatEvents

## Slide 49

### OUI-Based, Intelligent BSSID Guessing

Queried Apple WPS for 2<sup>14</sup> random BSSIDs/OUI

“Extra” up-to-400 BSSIDs provide incredible ROI

- 1 day to ~100M BSSIDs

4 days to ~500M BSSIDs

#BHUSA  @BlackHatEvents

## Slide 50

### OUI-Based, Intelligent BSSID Guessing

Queried Apple WPS for 2<sup>14</sup> random BSSIDs/OUI

“Extra” up-to-400 BSSIDs provide incredible ROI

- 1 day to ~100M BSSIDs

4 days to ~500M BSSIDs

#BHUSA  @BlackHatEvents

## Slide 51

OUI-Based, Intelligent BSSID Guessing

Queried Apple WPS for 2<sup>14</sup> random BSSIDs/OUI

“Extra” up-to-400 BSSIDs provide incredible ROI

1 day to ~100M BSSIDs

4 days to ~500M BSSIDs

100 BSSIDs per query

#BHUSA  @BlackHatEvents

## Slide 52

### Correctly-Guessed BSSID Geolocations (~500M)

2^
20
15
10
5
0

BSSID density (largely) mirrors that of human population density*

#BHUSA  @BlackHatEvents

## Slide 53

### Correctly-Guessed BSSID Geolocations (~500M)

2^
20
15
Amazon Rainforest
10
5
0

BSSID density (largely) mirrors that of human population density*

#BHUSA  @BlackHatEvents

## Slide 54

### Correctly-Guessed BSSID Geolocations (~500M)

2^
20
15
Amazon Rainforest
10
5
0
Sahara Desert

BSSID density (largely) mirrors that of human population density*

#BHUSA  @BlackHatEvents

## Slide 55

### Correctly-Guessed BSSID Geolocations (~500M)

¯\_( ツ )_/¯
2^
20
15
Amazon Rainforest
10
5
0
Sahara Desert

BSSID density (largely) mirrors that of human population density*

#BHUSA  @BlackHatEvents

## Slide 56

### China-Specific Apple WPS

BSSIDs rarely (but not never) appear in non-China Apple WPS

China-specific WPS API exists, perhaps due to data restrictions

China-specific API is globally-queryable

Credit to JaneCCP/Antonio Cheung (acheong08) for finding China API endpoint

#BHUSA  @BlackHatEvents

## Slide 57

Case Study: Remote-est Wi-Fi on Earth

BSSID geolocations on all 7 continents

Wi-Fi present in extremely austere, remote locations

BSSID geolocations among populations of <100 people

#BHUSA  @BlackHatEvents

## Slide 58

# Targeted Surveillance Attack

### Stalking via Wi-Fi router

#BHUSA  @BlackHatEvents

## Slide 59

WPS

Privacy Threat 1: Targeted Tracking BSSIDs are persistent identifiers

00:11:22:33:44:55

#BHUSA  @BlackHatEvents

## Slide 60

WPS

Privacy Threat 1: Targeted Tracking BSSIDs are persistent identifiers

#BHUSA  @BlackHatEvents

## Slide 61

WPS

Privacy Threat 1: Targeted Tracking BSSIDs are persistent identifiers

#BHUSA  @BlackHatEvents

?

## Slide 62

WPS

Privacy Threat 1: Targeted Tracking BSSIDs are persistent identifiers

#BHUSA  @BlackHatEvents

Where is 00:11:22:33:44:55?

?

## Slide 63

Privacy Threat 1: Targeted Tracking
BSSIDs are persistent identifiers
WPS
Where is
00:11:22:33:44:55
00:11:22:33:44:55?
?

#BHUSA  @BlackHatEvents

## Slide 64

# Mass Surveillance Attacks

What can you learn from all the Wi-Fi?

#BHUSA  @BlackHatEvents

## Slide 65

Privacy Threat 2: Vendor Enumeration

OUI (typically) identifies the device manufacturer

Possible to enumerate all 16M BSSIDs in an OUI in a matter of hours Trivial geolocation of privacy-sensitive devices/manufacturers

20:cc:27:a8:92:01 Cisco Systems

#BHUSA  @BlackHatEvents

## Slide 66

Privacy Threat 2: Vendor Enumeration

OUI (typically) identifies the device manufacturer

Possible to enumerate all 16M BSSIDs in an OUI in a matter of hours Trivial geolocation of privacy-sensitive devices/manufacturers

74:24:9f:a8:92:01 Starlink (TIBRO)

#BHUSA  @BlackHatEvents

## Slide 67

### Case Study: Russia-Ukraine War

#BHUSA  @BlackHatEvents

## Slide 68

### Case Study: Russia-Ukraine War

Hotspots in major cities

#BHUSA  @BlackHatEvents

## Slide 69

Case Study: Russia-Ukraine War

Hotspots in major
cities
Presence along
frontlines

#BHUSA  @BlackHatEvents

## Slide 70

Case Study: Russia-Ukraine War Starlink geolocations in Ukraine 2023-2024

Hotspots in major
cities
Presence along
frontlines
Operation in
Russian-occupied
territory

#BHUSA  @BlackHatEvents

## Slide 71

### Privacy Threat 3: Device Mobility

#BHUSA  @BlackHatEvents

## Slide 72

### Privacy Threat 3: Device Mobility

#BHUSA  @BlackHatEvents

## Slide 73

### Privacy Threat 3: Device Mobility

#BHUSA  @BlackHatEvents

## Slide 74

### Tracking 10M BSSIDs for a Month

Most routers stable for long periods…

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 95/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
CDF of BSSIDs Moving > 1 km
0.00
10 Million BSSID Sample Movers GLiNet Movers (1 month) GL-iNet Movers (6 months)
```

## Slide 75

### Tracking 10M BSSIDs for a Month

Only 6,002 move >1km

Most routers stable for long periods…

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 92/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Q
a ~I
CDF of BSSIDs Moving > 1 km
Only 6,002 move >1km
10 Million BSSID Sample Movers GLiNet Movers (1 month) - GL-iNet Movers (6 months)
```

## Slide 76

Tracking 10M BSSIDs for a Month

Small movements

Only 6,002 move >1km

Most routers stable for long periods…

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 88/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Q
=
A 0.75
>
Small movements S
=
faa)
‘= 0.25
LL
Q
O
60
Only 6,002 move >1km
10 Million BSSID Sample Movers GLiNet Movers (1 month) - GL-iNet Movers (6 months)
```

## Slide 77

Tracking 10M BSSIDs for a Month

Small movements
Travel routers

Only 6,002 move >1km

…but some move significant distances

#BHUSA  @BlackHatEvents

## Slide 78

Case Study: Russia-Ukraine War Longitudinal data allows tracking movement into and out of regions

Device locations _before entering Ukraine_

#BHUSA  @BlackHatEvents

## Slide 79

Case Study: Russia-Ukraine War Longitudinal data allows tracking movement into and out of regions

Device locations
before entering
Ukraine
Pre-deployment
sites?

#BHUSA  @BlackHatEvents

## Slide 80

Case Study: Russia-Ukraine War Longitudinal data allows tracking movement into and out of regions

Device locations
before entering
Ukraine
Pre-deployment
sites?
NGOs? Foreign
legion?

#BHUSA  @BlackHatEvents

## Slide 81

Case Study: Gaza War Tracking outages and destruction over time

75% decrease in Gaza BSSIDs over 4 weeks

25% decrease in Tel Aviv BSSID control group over same period

#BHUSA  @BlackHatEvents

## Slide 82

# Disclosure and Remediation

What can we do about this?

#BHUSA  @BlackHatEvents

## Slide 83

### Disclosure

Disclosed Dec 2023

Can now opt-out of
Apple’s WPS

Disclosed Mar 2024

Recommend
randomizing BSSIDs

#BHUSA  @BlackHatEvents

## Slide 84

### Apple Remediation

Apple modified privacy page in March 2024 indicating users can opt-out of WPS

SSID: Erik-WiFi

Append _nomap to SSID to opt-out

What Apple should do:

- Prevent excessive queries

- Require authentication

74:09:bc:a0:5e:b8

- Limit number of “extra” BSSIDs

#BHUSA  @BlackHatEvents

## Slide 85

### Apple Remediation

Apple modified privacy page in March 2024 indicating users can opt-out of WPS

SSID: Erik-WiFi_nomap

Append _nomap to SSID to opt-out

What Apple should do:

- Prevent excessive queries

- Require authentication

74:09:bc:a0:5e:b8

- Limit number of “extra” BSSIDs

#BHUSA  @BlackHatEvents

## Slide 86

### BSSID Randomization

Random BSSIDs
prevent device
manufacturer
identification

fa:82:d2:ba:04:2d

#BHUSA  @BlackHatEvents

## Slide 87

### BSSID Randomization

Random BSSIDs
prevent device
manufacturer
identification

fa:82:d2:ba:04:2d

#BHUSA  @BlackHatEvents

## Slide 88

### BSSID Randomization

Random BSSIDs
prevent device
manufacturer
identification

fa:82:d2:ba:04:2d

Random BSSIDs
prevent device
correlation over time
and space

2e:29:ba:95:8d:2f

#BHUSA  @BlackHatEvents

## Slide 89

Remediation Starlink routers began randomizing BSSIDs on all products April 2024

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 85/100 on the text kept, 58/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Starlink routers began randomizing BSSIDs on all products April 2024
& 300,000
jaa)
as,
© 200,000
‘3 100,000
O
0
```

## Slide 90

### Remediation

Initially, no plans to randomize BSSIDs

Reached out in late May 2024 informing us of change of direction

Implemented BSSID randomization in software version v4.6.2+

#BHUSA  @BlackHatEvents

## Slide 91

## Surveilling the Masses with Wi-Fi Positioning Systems

Remotely geolocate >2B BSSIDs over course of 2023

Disclosed to Apple December 2023 — Still a threat today

Longitudinally track BSSID movements

Sample Apple WPS query code github.com/gigaryte/ bssid-geolocator

#BHUSA  @BlackHatEvents

## Slide 92

## Surveilling the Masses with Wi-Fi Positioning Systems

Remotely geolocate >2B BSSIDs over course of 2023 Longitudinally track BSSID movements

Thanks!
Erik Rye
rye@umd.edu

Disclosed to Apple December 2023 — Still a threat today Sample Apple WPS query code github.com/gigaryte/ bssid-geolocator

#BHUSA  @BlackHatEvents

## Slide 93

# Backup Slides

### Frequently Asked Questions

#BHUSA  @BlackHatEvents

## Slide 94

### FAQ — When Does an AP Become a Landmark?

To be a good landmark, AP must be stable. Apple applies some minimum stability threshold

Black box testing — 3-7 days before new BSSID AP appears

Similarly, 3-7 days for a powered-off AP to disappear

Stability threshold a potential tunable parameter by Apple

#BHUSA  @BlackHatEvents

## Slide 95

### FAQ — Mobile Hotspots

Modern Android/iOS use random BSSIDs when in hotspot mode — our best-practice recommendation for mobile APs

Their ephemerality typically precludes them from becoming landmarks — generally only used for several minutes to a few hours

#BHUSA  @BlackHatEvents

## Slide 96

FAQ — Trains, Planes, and Automobiles

Vehicles (typically) don’t become WPS landmarks

Intuition: unstable landmarks useless for positioning

Boats are an exception — boats are often stationary for long periods

#BHUSA  @BlackHatEvents

## Slide 97

### FAQ — Doesn’t WiGLE Do This?

WiGLE is awesome! Several key differences

WPSes use the O(Billions) devices in their ecosystems to do the “wardriving”

WiGLE relies on wardrivers being present in an area and uploading their data to WiGLE

WiGLE captures some additional data the WPS does not — e.g., SSID

#BHUSA  @BlackHatEvents
