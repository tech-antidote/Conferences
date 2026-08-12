---
title: "The Yandex Leak How a Russian Search Giant Uses Consumer Data"
speakers: ["Kaileigh McCrea"]
conference: "Black Hat"
conference_full: "Black Hat USA 2023"
edition: "USA"
year: 2023
source_pdf: "Black Hat USA 2023 slides/Kaileigh McCrea_The Yandex Leak How a Russian Search Giant Uses Consumer Data.pdf"
pages: 75
sha256: "f192e8e4cafbfb5a5c69e78952337dc7b7d464f97f81aa32e574bacf27282f23"
text_chars: 41919
ocr_pages: 59
has_ocr: true
redacted_secrets: 0
ocr_confidence: 87.6
ocr_unreliable_blocks: 0
vision_verified_blocks: 4
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T04:13:54Z"
---
# The Yandex Leak How a Russian Search Giant Uses Consumer Data

**Speakers:** Kaileigh McCrea  
**Conference:** Black Hat USA 2023  
**Source:** `Black Hat USA 2023 slides/Kaileigh McCrea_The Yandex Leak How a Russian Search Giant Uses Consumer Data.pdf` (75 pages)


## Slide 1

The Yandex Leak: How a Russian Search Giant Uses Consumer Data

Kaileigh McCrea, Privacy Engineer, Confiant

## Slide 2

#### About Me

##### Kaileigh McCrea

● Privacy Engineer at Confiant (3 yrs) ● Software Engineer (6 years)

● Cybersecurity Nerd

● Recovering Political Science major

● Twitter: @kaileighrose

2

## Slide 3

### What we’re talking about

3


> Recovered by OCR — confidence 92/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
yandex git sources
iby booinieRR- Wednesday January 25, 2023 at 03:48 PM
Repositories only, no data. Size 44,71 G
pied almost completely except for the anti-spam rules
Downloaded by me on 07.
magnet:?
YANDEX SERVICES SOURCE
CODE LEAK
SHORT OVERVIEW OF BREACH CONTENTS
BLEEPINGCOMPUTER
Yandex denies hack, blames source code leak on former employee
Yandex denies hack, blames source code leak on former employee
By Bill Toulas January 26, 2023 09:44 AM 1
```

## Slide 4

# Roadmap

●Background on Yandex Leak ●Dive into code: ○What data Yandex is collecting ○What Yandex is doing with that data ○Who Yandex is sharing that data with ●Conclusions and wrap up ●Q&A

4

## Slide 5

## Yandex 101

5

## Slide 6

#### Yandex 101

6


> Recovered by OCR — confidence 90/100 on the text kept, 65/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Yandex 101
vy Login
Games Images Video Meteum Maps Mail Translate
```

## Slide 7

#### Yandex 101

7


> Recovered by OCR — confidence 95/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Yandex 101
Key Businesses
Search
and Portal
Yandex Search Business
Units
Geo Services
Yandex Browser
Yandex Q
Other
E-commerce,
Mobility and
Delivery
Plus and
Entertainment
Services
Classifieds
Mobility
E-commerce
Other 020
Yandex Plus
Yandex Music
Kinopoisk
Yandex Afisha
Yandex Studio
Auto.ru
Yandex Realty
Yandex Rent
Yandex Travel
Other
Business Units
and Initiatives
Yandex SDG
Yandex Cloud
Yandex Education
Devices and Alice
Other
```

## Slide 8

#### Yandex 101

<u>AppMetrica:</u> “In-depth analytics for product and growth teams”

<u>Audiences: allows you to</u> pull data from several sources to generate your own targeted segments

<u>Crypta: “helps to identify</u> important user characteristics for advertisers”

8

## Slide 9

#### Yandex 101

9


> Recovered by OCR — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Yandex 101
Yandex LLC
Head office in Russia: Moscow
Head office Advertising clients
16, Leo Tolstoy St., Moscow, Russia tel.:+7 495 739-37-77
119021 fax:+7 495 739-23-32
tel.:+7 495 739-70-00 adv@yandex-team.ru
fax: +7 495 739-70-70
Public relations Corporate Secretary
pr@yandex-team.ru secretary@yandex-team.ru
Investor Relations
tel.:+7 495 974-35-38
askIR@yandex-team.ru
Sustainability
sustainability@yandex-team.com
Official Telegram channel for individual investors https://t.me/yndx_forinvestors (in Russian only)
Yandex N.V.
Registered office in Amsterdam
Schiphol Boulevard 165, 1118 BG Schiphol, The
Netherlands
tel.: +31 0 20 206 6970
```

## Slide 10

## Yandex: A Drama

10

## Slide 11

11


> Recovered by OCR — confidence 95/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Russia © This article is more than 3 years old Advertisement
Russian internet giant grants veto
powers to Kremlin-linked body
Yandex agrees to corporate restructuring in move likely to
increase government oversight
Andrew Roth in Moscow
Mon 18 Nov 2019 06.30 ES
@ Arkady
daily oper
zh, the chief executive of Y aid the company would maintain control over its
s. Photograph: Mikhail Metzel,
```

## Slide 12

12


> Recovered by OCR — confidence 94/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
The Observer © This article is more than 1 year old Advertisement
Russia
Warnings raised over Russian tech giant
Yandex’s UK operation
MPs want restrictions placed on the company, known as Russia’s
Google, which also runs the Yango Deli grocery service
Russia-Ukraine war: live news
Shanti Das
Sat 5 Mar 2022 15.02 EST
GA Yango Deli driver on an electric moped delivers to homes in London. The service is expanding
across the city. Photograph: John Sibley/Reuters
```

## Slide 13

13


> Recovered by OCR — confidence 94/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Data-harvesting code in mobile apps sends user
data to “Russia’s Google”
Data from apps on Apple- and Google-powered mobile devices is sent to Russian servers.
User profiles
AppMetrica: Your app’s
CRM
Build complete audience knowledge with
segmentation based on profile data or dive into
individual users with profile cards.
Today
© Addto cart
13
```

## Slide 14

14


> Recovered by OCR — confidence 88/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Article
Russia's war hits Yandex, the ‘Google of Russia’
Sources say the company is seeking a media exit as top exec hit with sanctions over
propaganda charge
TSAKO sh+ Natasha Lomas, Ingrid Lunden 12:20 PM PDT + March 16, 2022
```

## Slide 15

15


> Recovered by OCR — confidence 87/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
| Premium | HOME > TECH
'| bought a plane ticket and left 12 hours later’: Engineers at Yandex,
Russia's Google rival, are fleeing abroad and leaving spouses and
salaries behind
Rosie Bradbury Apr 12,2022, 3:35 AM PDT Q f [<4] ad
```

## Slide 16

16


> Recovered by OCR — confidence 94/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Yandex CEO resigns after being targeted
by EU sanctions
Reuters
June 3, 2022 7:35 AM PDT : Updated a year ago Q Aa < |
The logo of Russian internet group Yandex is pictured at the company's headquarter in Moscow, Russia October 4, 2018. REUTERS/Shamil
Zhumatov
June 3 (Reuters) - Russian internet giant Yandex (YNDX.O) said on Friday that Arkady Volozh had stepped
down as CEO and left the board of directors after the European Union included him on its latest list of
sanctions against Russian entities and individuals.
```

## Slide 17

17


> Recovered by OCR — confidence 91/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Yandex's sale of media assets to VK inc
yandex.ru homepage
=
ludes
Login
AM PDT + August 23, 2022
/ 12:05
ptari
Crunch+
Tect
ups
Star
2
Security
Al
Crypto
Apps
Events
More
```

## Slide 18

18


> Recovered by OCR — confidence 90/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Deals
Yandex parent to review ownership of
Russian tech giant, seek divestment
By Alexander Marrow, Darya Korsunskaya and Polina Devitt
November 25, 2022 7:31 AM PST : Updated 8 months ago q | | Aa | < |
```

## Slide 19

19


> Recovered by OCR — confidence 85/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Europe 30 YEARS 9 4)
Putin, Kudrin touch on future of
Yandex in late-nig ht meeting -sources = NEWS’~ UKRAINEWAR- BUSINESS’ OPINION ARTSANDLIFE PODCASTS
. Moscow Times
INDEPENDENT NEWS FROM RUSSIA
Reuters
Aa
November 25, 2022 4:19 AM PST : Updated 8 months ago W <
Kremlin Ally Kudrin Confirms
“| Move to Tech Giant Yandex
11/2] The logo of Russia
October 4, 2018. REUT!
```

## Slide 20

20


> Recovered by OCR — confidence 93/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ABOUTME CONTACTS NOTACV PROJECTS
YANDEX SERVICES SOURCE
CODE LEAK
SHORT OVERVIEW OF BREACH CONTENTS
Just a few hours ago | found mention on Twitter that proprietary source code of Russian giant
Yandex been leaked on online community called BreachForums. In this post I'll share results of
my friend digging into said archives.
Important details about torrent:
¢ Itjust content of repository without anything else.
All files are dated back to 24 February 2022.
¢ It does not contain git history, mostly just code
¢ No pre-built binaries for most of software with only few exceptions
¢ There are no pre-trained ML models with some exceptions
```

## Slide 21

21


> Recovered by OCR — confidence 79/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
<4 ¢ Support The Moscow 1
The .2, Moscow Times iol
30 YEARS i INDEPENDENT NEWS FROM RUSSIA
= NEWS’ UKRAINEWAR- BUSINESS OPINION ARTSANDLIFE PODCASTS NEWSLETTERS ARCHIVE
Russian Billionaires Line Up to Buy sosreea> stn
Yandex — Reports 1 ama
Russia Says Ukrainian Drone:
Moscow, Crimea
May 4, 2023 600000 2 NO PASSAGE
Russia Blocks Cargo Ship Ov
3 POLITICAL PRISONER
Navalny Ally Jailed 9 Years fc
Y Russia Raises Upper-Age Lir
MONEY DRAIN
```

## Slide 22

22


> Recovered by OCR — confidence 81/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
World Business Markets v Sustainability Legal’ Breakingviews Technology Investigations More v fo MyViwy Q
Technology
Russia's Yandex fined for refusing to
share user information with security
services
(a | [aa] (<)
June 18, 2023 3:20 PM PDT - Updated a month ago
```

## Slide 23

# Roadmap

●Background on Yandex Leak ●Dive into code: ○What data Yandex is collecting ○What Yandex is doing with that data ○Who Yandex is sharing that data with ●Conclusions and wrap up ●Q&A

23

## Slide 24

## Yandex Codebase

24

## Slide 25

#### Codebase

25


> Recovered by OCR — confidence 80/100 on the text kept, 57/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Codebase
nginx.tar.bz2 noc.tar.bz2 partner.tar.bz2 passport.tar.bz2 pay.tar.bz2 payplatform.tar.b
U
Paysys.tar.bz2 portal.tar.bz2 — privacy_office.tar. products.tar.bz2 robot.tar.bz2 rt-
bz2 research.tar.bz2
723)
```

## Slide 26

## Metrika

26

## Slide 27

#### Metrika

27


> Recovered by OCR — confidence 94/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Metrika
a] AppMetrica Solutions Features Verticals Resources
Supercharge app
metrics with data
insights
with a one-stop solution for analytics and marketing
Yandex Metrica
All-Round Web Analytics
Features
Resources
From traffic trends to mouse movements —
get a comprehensive understanding of your
online audience and drive business growth.
Get started
Try live demo
Pricing
27
```

## Slide 28

#### Example Raw Data Fields that AppMetrica Logs

28


> Recovered by OCR — confidence 78/100 on the text kept, 52/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Example Raw Data Fields that AppMetrica Logs
lytics > appmetrica-location-log-anonymizer > = convert_log.yql analytics > appmetrica-location-log-anonymizer > = convert_log.yql
with truncate “IsRooted* ,
select *KitBuildNumber*,
String: :HexEncode(Digest::Blake2B(*IFA*, seed)) as “IFA, ‘Latitude’,
05 ‘Cells_CountriesCodes*, 138 ‘Longitude’,
07 ‘Cells_LastVisibleTimeOffset*, 140 “OSApiLevel*,
119 “DeviceType*, 152 ‘Wifi_Ssids*,
28
```

## Slide 29

#### Anonymized identifiers

29


> Recovered by OCR — confidence 77/100 on the text kept, 72/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Anonymized identifiers
select
String: :HexEncode(Digest::Blake2B(*ADVID*, seed)) as “ADVID*,
String: :HexEncode(Digest::Blake2B(*IFA*, seed)) as “IFA‘,
String: :HexEncode(Digest::Blake2B(*UUID*, seed)) as “UUID*,
String: :HexEncode(Digest: :Blake2B(*AndroidID*, seed)) as ‘AndroidID*,
29
```

## Slide 30

#### Location Fields

30


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 93/100 on the text kept, 56/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Deobfuscation: LLVM Optimisations

[left panel, orange label]  O-LLVM
Instruction Subsitution (3 loops)

101  else if (iVar1 == 2) {
102    uVar10 = (param1 ^ 0xffffffff) & param1;
103    uVar11 = uVar10 ^ 0xffffffff;
104    uVar10 = (param1 & 0x28b159a6 | (param1 ^ 0xffffffff) & 0xd74ea659) ^
105           [obscured by tooltip] | uVar10 & 0xd74ea659) | (param1 | uVar11) ^ 0xffffffff;
106    uVar1[obscured by tooltip] & 0xad02e611 | uVar10 & 0x52fd19ee;
107    uVar10 = (uVar10 ^ 0x52fd19ee) & 0x2d4bd55a | (uVar10 ^ 0xad02e611) & 0xd2b42aa5;
108    uVar10 = (uVar10 ^ 0x2d4bd55a) & uVar10;
109    uVar11 = (param1 & 0x43df8f | (param1 ^ 0xffffffff) & 0xffbc2070) ^ 0xd2f7f52a |
110           (param1 | 0x2d4bd55a) ^ 0xffffffff;
111    uVar12 = uVar10 ^ 0xffffffff | uVar11;
112    uVar10 = (uVar11 ^ 0xffffffff) & (uVar10 ^ 0xffffffff) | uVar10 & uVar11;
113    uVar11 = uVar10 ^ 0xffffffff;
114    uVar10 = (uVar12 & 0xac3e94d1 | (uVar12 ^ 0xffffffff) & 0x53c16b2e) ^
115           (uVar11 & 0xac3e94d1 | uVar10 & 0x53c16b2e) | (uVar12 | uVar11) ^ 0xffffffff;
116    uVar11 = uVar10 ^ 0x35ec8eeb;
117    uVar10 = uVar10 ^ 0xffffffff | 0x35ec8eeb;
118    uVar12 = uVar11 & 0x35ec8eeb ^ 0xffffffff;
119    uVar10 = (uVar12 & 0x2d5bbaff | uVar11 & 0x10a40400) ^
120           (uVar10 & 0x2d5bbaff | (uVar10 ^ 0xffffffff) & 0xd2a44500) |
121           (uVar12 | uVar10) ^ 0xffffffff;
122    uVar11 = (param1 ^ 0xffffffff) & 0x733e697e | param1 & 0x8cc19681;
123    uVar11 = ((uVar11 ^ 0x8cc19681) & 0xfffffffb | (uVar11 ^ 0x733e697e) & 4) ^ 0xffffffff |
124           0xfffffffb;
125    uVar12 = (param1 ^ 0x55a04b31) & (param1 ^ 0xffffffff);
126    uVar4 = (param1 ^ 0xffffffff | 0x55a04b31) ^ 0xffffffff;
127    uVar12 = uVar12 & uVar4 | uVar12 ^ uVar4;
128    uVar12 = (uVar12 ^ 0xffffffff) & 0xf7e551b4 | uVar12 & 0x81aae4b;
129    uVar4 = (uVar12 ^ 0x5dbae57e) & 0xda9fbf90 | (uVar12 ^ 0xa2451a81) & 0x2560406f;
130    uVar5 = (uVar11 ^ 0x8149b87a) & uVar11;
131    uVar6 = (uVar11 ^ 0x8149b87a) & (uVar11 ^ 0xffffffff);
132    uVar7 = (uVar4 ^ 0xa429f815) & (uVar4 ^ 0x2560406f);
133    uVar12 = (uVar12 ^ 0xdcf35d04) & (uVar12 ^ 0xa2451a81);
134    uVar8 = uVar5 ^ 0xffffffff;
135    uVar9 = uVar6 ^ 0xffffffff;
136    uVar5 = (uVar8 & 0xa7224c94 | uVar5 & 0x58ddb36b) ^ (uVar9 & 0xa7224c94 | uVar6 & 0x58ddb36b) |
137           (uVar8 | uVar9) ^ 0xffffffff;
138    uVar12 = uVar7 & uVar12 | uVar7 ^ uVar12;
139    uVar12 = uVar12 & (uVar5 ^ 0xffffffff) | uVar5 & (uVar12 ^ 0xffffffff);
140    uVar11 = ((uVar11 ^ 0xffffffff) & 0x3c7da929 | uVar11 & 0xc38256d6) ^
141           ((uVar4 ^ 0xda9fbf90) & 0x3c7da929 | (uVar4 ^ 0x2560406f) & 0xc38256d6) |
142           (uVar11 ^ 0xffffffff | uVar4 ^ 0xda9fbf90) ^ 0xffffffff;
143    uVar11 = (uVar11 ^ 0xffffffff) & 0x51a3afbb | uVar11 & 0xae5c5044;
144    uVar4 = uVar11 ^ 0x51a3afbb;
145    uVar5 = uVar12 ^ 0xffffffff;
146    local_10 = (((uVar10 ^ 0xffffffff) & 0xebfaad80 | uVar10 & 0x1405527f) ^ 0xb608d971) *
147           ((uVar5 & 0xf368b83d | uVar12 & 0xc9747c2) ^
148            (uVar4 & 0xf368b83d | (uVar11 ^ 0xae5c5044) & 0xc9747c2) |
149            (uVar5 | uVar4) ^ 0xffffffff);
150  }

[tooltip overlaying lines 105-106]
Unsigned Integer (compiler-specific size)
Length: 4

[right panel, orange label]  LLVM Optimised

20  if (iVar5 == 0) {
21    uVar2 = (((param_2 | 0xbaaad0bf) & 0xc4fa1585 | param_2 & 0x1052a40) ^ param_2 ^ 0x80aa1085) &
22          (param_2 | 0xbaaad0bf | param_2 ^ 0x45552f40);
23    uVar1 = uVar2 & (param_2 ^ 0xbaaad0bf);
24    uVar2 = uVar2 ^ param_2;
25    uVar3 = ((param_2 & 0xfffffffd ^ 0xffffffff) & 0x34f5a7e6 | param_2 & 0xcb0a5819) ^
26          (param_2 & 2 | 0xdb2decf5);
27    uVar4 = ((param_2 & 0xfffffffd ^ 0xffffffff) & 0x48c117 | param_2 & 0xffb73ee8) ^
28          (param_2 & 2 | 0x48c115) | param_2 ^ 0xfffffffd;
29    local_24 = (uVar2 ^ uVar1 ^ 0xbaaad0bf | (uVar2 ^ 0xbaaad0bf) & uVar1) *
30          (uVar3 ^ uVar4 ^ 0x1027b4ee | (uVar3 ^ 0x1027b4ee | uVar4) ^ 0xffffffff);
31  }
32  else if (iVar5 == 1) {
33    local_24 = ((((param_2 | 0xbaaad0bf) & 0x3c966fda | param_2 & 0x41410000) ^ param_2 ^ 0x3882409a
34          ) & (param_2 | 0xbaaad0bf | param_2 ^ 0x45552f40)) * (param_2 + 3);
35  }
36  else if (iVar5 == 2) {
37    uVar2 = (param_2 ^ 0xfffffffb | param_2 ^ 4) & (param_2 ^ 0x7eb64781);
38    local_24 = (uVar2 & (param_2 & 4 | 0x8149b87a) |
39          (param_2 & 4 ^ 0x7eb64785) & (uVar2 ^ 0xffffffff)) * (param_2 ^ 0xbaaad0bf);
40  }
41  else {
42    local_24 = (param_2 + 0xbaaad0bf) * (param_2 & 5);
43  }

[teal label]  Original Expression Recovered
[callout badges]  1  2  3  4
```

## Slide 31

#### Wifi Fields Collected By AppMetrica

31


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 95/100 on the text kept, 59/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Deobfuscation: LLVM Opt + SiMBA + GAMBA

[left panel, teal label]  INPUT
if (iVar1 == 0) {
  uVar10 = param1 & 0xc9e645ce | (param1 ^ 0xffffffff) & 0x3619ba31;
  uVar11 = ((uVar10 ^ 0x3619ba31) & 0x5c2ea1f5 | (uVar10 ^ 0xc9e645ce) & 0xa3d15e0a) ^ 0xf1571e9d
           | uVar10 ^ 0x3619ba31;
  uVar12 = ((param1 ^ 0xffffffff) & 0xad79bf68 | param1 & 0x52864097) ^ 0xffffffff |
           param1 ^ 0xffffffff;
  uVar4 = uVar11 | uVar12;
  uVar11 = (uVar12 ^ 0xffffffff) & uVar11 | (uVar11 ^ 0xffffffff) & uVar12;
  uVar12 = uVar11 ^ 0xffffffff;
  uVar11 = (uVar4 & 0xaea378c3 | (uVar4 ^ 0xffffffff) & 0x515c873c) ^
           (uVar12 & 0xaea378c3 | uVar11 & 0x515c873c) | (uVar4 | uVar12) ^ 0xffffffff;
  uVar12 = ((uVar11 ^ 0xffffffff) & 0xcb73214a | uVar11 & 0x348cdeb5) ^ 0xcb73214a | 0x604af11c;
  uVar11 = uVar11 ^ 0xffffffff | 0x9fb50ee3;
  uVar11 = (uVar12 & 0x5835bf98 | (uVar12 ^ 0xffffffff) & 0xa7ca4067) ^
           (uVar11 & 0x5835bf98 | (uVar11 ^ 0xffffffff) & 0xa7ca4067) |
           (uVar12 | uVar11) ^ 0xffffffff;
  uVar11 = (uVar11 ^ 0xffffffff) & 0x88666134 | uVar11 & 0x77999ecb;
  uVar12 = uVar10 ^ 0x3619ba31 | 0xbaaad0bf;
  uVar10 = (uVar10 ^ 0x3619ba31) & 0x565b27a0 | (uVar10 ^ 0xc9e645ce) & 0xa9a4d85f;
  uVar4 = uVar10 ^ 0xecf1f71f;
  uVar12 = (uVar12 & 0xc4fa1585 | (uVar12 ^ 0xffffffff) & 0x3b05ea7a) ^
           (uVar4 & 0xc4fa1585 | (uVar10 ^ 0x130e08e0) & 0x3b05ea7a) |
           (uVar12 | uVar4) ^ 0xffffffff;
  uVar10 = (((uVar12 ^ 0xffffffff) & 0xbe3c86ad | uVar12 & 0x41c37952) ^ 0xbe3c86ad | 0xe6842217)
           ^ 0xffffffff;
  uVar12 = (uVar12 ^ 0x197bdde8) & uVar12;
  uVar10 = uVar10 & uVar12 | uVar10 ^ uVar12;
  uVar10 = (uVar10 ^ 0xffffffff) & 0x9d11e123 | uVar10 & 0x62ee1edc;
  uVar10 = (uVar10 ^ 0x846a3ccb) & 0x61675078 | (uVar10 ^ 0x7b95c334) & 0x9e98af87;
  uVar10 = (uVar10 ^ 0x61675078) & 0xa63617bd | (uVar10 ^ 0x9e98af87) & 0x59c9e842;
  uVar12 = (uVar11 ^ uVar10 ^ 0xa63617bd) & uVar11;
  uVar10 = ((uVar11 ^ 0xffffffff) & 0xbcc6bdd4 | uVar11 & 0x4339422b) ^
           ((uVar10 ^ 0xa63617bd) & 0xbcc6bdd4 | (uVar10 ^ 0x59c9e842) & 0x4339422b);
  uVar11 = uVar12 ^ 0xffffffff;
  uVar4 = uVar10 ^ 0xffffffff;
  uVar5 = (param1 ^ 0xffffffff) & 0xaf91567b | param1 & 0x506ea984;
  uVar6 = uVar5 ^ 0xaf91567b;
  uVar5 = (uVar6 & 0xe30d84a7 | (uVar5 ^ 0x506ea984) & 0x1cf27b58) ^ 0xe30d84a5 |
          (uVar6 | 0xfffffffd) ^ 0xffffffff;
  uVar6 = (((param1 ^ 0xffffffff) & 0x7ce0ffb1 | param1 & 0x831f004e) ^ 0xea109553) & 0x96f06ae2;
  uVar7 = (param1 ^ 0xffffffff | 0x96f06ae2) ^ 0xffffffff;
  uVar8 = uVar6 ^ uVar7;
  uVar6 = (uVar8 ^ 0xffffffff) & 0x690f951d | uVar6 & uVar7 | uVar8 & 0x96f06ae2;
  uVar6 = uVar6 & 0xba8c5c70 | (uVar6 ^ 0xffffffff) & 0x4573a38f;
  uVar6 = (uVar6 ^ 0x4573a38f) & (uVar6 ^ 0xba8c5c72);
  uVar7 = (uVar5 ^ 0xcb0a5819) & uVar5;
  uVar8 = (uVar5 | 0x34f5a7e6) ^ 0xffffffff;
  uVar9 = (uVar6 ^ 0x34f5a7e6) & (uVar6 ^ 0xffffffff);
  uVar2 = (uVar6 ^ 0x34f5a7e6) & uVar6;
  uVar7 = uVar7 & uVar8 | uVar7 ^ uVar8;
  uVar8 = uVar9 ^ 0xffffffff;
  uVar3 = uVar2 ^ 0xffffffff;
  uVar8 = (uVar8 & 0xd3d541ce | uVar9 & 0x2c2abe31) ^ (uVar3 & 0xd3d541ce | uVar2 & 0x2c2abe31) |
          (uVar8 | uVar3) ^ 0xffffffff;
  uVar7 = ((uVar7 ^ 0xffffffff) & 0xefd84b11 | uVar7 & 0x1027b4ee) ^
          ((uVar8 ^ 0xffffffff) & 0xefd84b11 | uVar8 & 0x1027b4ee);
  uVar5 = ((uVar5 ^ 0xffffffff) & 0xffb73ee8 | uVar5 & 0x48c117) ^
          (uVar6 & 0xffb73ee8 | (uVar6 ^ 0xffffffff) & 0x48c117) |
          (uVar5 ^ 0xffffffff | uVar6) ^ 0xffffffff;
  uVar5 = (uVar5 ^ 0xffffffff) & 0xa95ee2be | uVar5 & 0x56a11d41;
  uVar6 = uVar5 ^ 0xa95ee2be;
  uVar8 = uVar7 ^ 0xffffffff;
  local_10 = ((uVar11 & 0x1e98326 | uVar12 & 0xfe167cd9) ^
              (uVar4 & 0x1e98326 | uVar10 & 0xfe167cd9) | (uVar11 | uVar4) ^ 0xffffffff) *
             ((uVar8 & 0xc8a77567 | uVar7 & 0x37588a98) ^
              (uVar6 & 0xc8a77567 | (uVar5 ^ 0x56a11d41) & 0x37588a98) |
              (uVar8 | uVar6) ^ 0xffffffff);
}

[top-right box, teal label]  LLVM Optimised
if (iVar5 == 0) {
  uVar2 = (((param_2 | 0xbaaad0bf) & 0xc4fa1585 | param_2 & 0x1052a40) ^ param_2 ^ 0x80aa1085) &
          (param_2 | 0xbaaad0bf | param_2 ^ 0x45552f40);
  uVar1 = uVar2 & (param_2 ^ 0xbaaad0bf);
  uVar2 = uVar2 ^ param_2;
  uVar3 = ((param_2 & 0xfffffffd ^ 0xffffffff) & 0x34f5a7e6 | param_2 & 0xcb0a5819) ^
          (param_2 & 2 | 0xdb2decf5);
  uVar4 = ((param_2 & 0xfffffffd ^ 0xffffffff) & 0x48c117 | param_2 & 0xffb73ee8) ^
          (param_2 & 2 | 0x48c115) | param_2 ^ 0xfffffffd;
  local_24 = (uVar2 ^ uVar1 ^ 0xbaaad0bf | (uVar2 ^ 0xbaaad0bf) & uVar1) *
             (uVar3 ^ uVar4 ^ 0x1027b4ee | (uVar3 ^ 0x1027b4ee | uVar4) ^ 0xffffffff);
}

[middle box, teal label]  SiMBA
if (uVar2 == 0) {
  uVar2 = (param_2 & 0xa81b62f7 | 0x17000408) ^ param_2 & 0x57e49d08;
  *piVar1 = ((uVar2 ^ 0xadaad4b7) & (param_2 & 0xbaaad0bf ^ 0xffffffff) |
             (uVar2 ^ 0x12000008) & param_2 & 0xbaaad0bf) *
             (param_2 & 0xfffffffd ^ (param_2 & 2 | 0x4fa5c831) ^ 0x4fa5c833);
  return;
}

[bottom box, teal label]  Gamba
if (uVar2 == 0) {
  *piVar1 = ((param_2 & 0x77b39989 | 0x88006252) ^ (param_2 ^ 0xed32f2d0) & (param_2 ^ 0x9a816b59)
            ) * (param_2 | 0xbaaad0bf);
  return;
}
```

## Slide 32

#### Those fields in Crypta

32


> Recovered by OCR — confidence 90/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Those fields in Crypta
graph > fuzzy > lib > yql > = export_ssid_devid_day_table.yq]
26
27
28
29
30
31
32
33
34
35
36
$list_metrika_log = (
select coalesce(DeviceID, "") as DeviceID,
coalesce(OriginalDevicelD, "") as OriginalDeviceID,
$MakeStringList(Wifi_Ssids) as Wifi_Ssids,
$MakeIntList(Wifi_SignalsStrengths) as Wifi_SignalsStrengths,
$MakeIntList(Wifi_AreConnected) as Wifi_AreConnected
from ‘{source_mmetric_table}*
where DeviceID is not null
32
```

## Slide 33

#### Dev Id and SSID Associated with Yandex UID

33


> Recovered by OCR — confidence 90/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Dev Id and SSID Associated with Yandex UID
graph > fuzzy > lib > yql >
7
8
10
12
13
14
1D
1A
$mobile_all_table = (
export_ssid_yuids.yql
select distinct mmetric_devid, ssid
from concat({sources})
$mmetric_to_devid = (
select mmetric_devid,
coalesce(cast(
devid,
yuid as uint64), @) as yuid
33
```

## Slide 34

Click Event Data Being Matched to Existing Users

34


> Recovered by OCR — confidence 88/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Click Event Data Being Matched to Existing Users
core > programs > clicklogd-mobile > src > C event_indexed_pool.h > ¢g TEventIndexedPool > © Getindex<TMatchCriteria>()
58 private:
59 template <class TMatchCriteria>
60 TIndex<TMatchCriteria>& GetIndex() {
61 if constexpr (std::is_same_v<TMatchCriteria, NMatchCriteria::TAndroidId>) {
63 1} else if constexpr (std::is_same_v<TMatchCriteria, NMatchCriteria::TAndroidIdMd5>) {
64 return AndroidIdMd5_;
65 1} else if constexpr (std::is_same_v<TMatchCriteria, NMatchCriteria::TAndroidIdSha1>) {
66 return AndroidIdSha1_;
67 } else if constexpr (std::is_same_v<TMatchCriteria, NMatchCriteria::TDeviceIdHash>) {
68 return DeviceIdHash ;
69 else if constexpr (std::is_same_v<TMatchCriteria, NMatchCriteria::TFingerprint>) {
else if constexpr (std
return GoogleAid_;
} else if constexpr (std::is_same_v<TMatchCriteria, NMatchCriteria::TGoogleAidMd5>) {
return GoogleAidMd5_;
75 } else if constexpr (std
return GoogleAidSha1_;|
HW else if constexpr (std:
return Ifa_;
} else if constexpr (std::is_same_v<TMatchCriteria, NMatchCriteria::TIfaMd5>) {
return IfaMd5_;
'S_same_v<IMatchcriteria, NMatchCriteria::TGoogleAid>) {
Bones
s_same_v<TMatchCriteria, NMatchCriteria::TIfa>) {
81 } else if constexpr (std::is_same_v<TMatchCriteria, NMatchCriteria::TIfaShal>) {
82 return IfaShal_;
83 } else if constexpr (std::is_same_v<TMatchCriteria, NMatchCriteria::TWindowsAid>) {
84 return WindowsAid_}
85 } else if constexpr (std::is_same_v<TMatchCriteria, NMatchCriteria::TWindowsAidMd5>) {
86 return WindowsAidMd5,
87 } else if constexpr (std s_same_v<TMatchCriteria, NMatchCriteria::TWindowsAidShal>) {
88 return WindowsAidSha1.
89 } else if constexpr (std _same_v<TMatchCriteria, NMatchCriteria::TYmTrackingId>) {
90 return YmTrackingId_;
34
```

## Slide 35

#### Socio-Demographic Attributes for DevID being Updated

35


> Recovered by OCR — confidence 84/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Socio-Demographic Attributes for DevID being Updated
core > programs > socdem-updaterd-mobile > src > G UserldAndinfoParser.cpp > ...
45 {"0_17", AgeIntervalsCrypta: :LessThan18},
6 {"18_24", AgeIntervalsCrypta: :Between18and24},
{"25_34", AgeIntervalsCrypta: : Between25and34},
{"35_44", AgeIntervalsCrypta: :Between35and44},
{"45_54", AgeIntervalsCrypta: :Between45and54},
{"55_99", AgeIntervalsCrypta: :MoreThan55}
55 void UserIdAndInfoParser: :setValue(
56 SexTypesCrypta & value,
const NYT::TNode & exact_socdem_node,
const TString key)
9 ¢{
60 static const std::map<TString, SexTypesCrypta> json_keys_to_sex_types =
6 {
62 {"f", SexTypesCrypta::Female},
63 {"m", SexTypesCrypta: :Male}
65 risetValue(value, exact_socdem_node, key, json_keys_to_sex_types) ;
68 std::string UserIdAndInfoParser::parse(const NYT::TNode & user_record)
1) const TString &{device_id = user_record["appmetrica_devid"] .AsString(); |
] UserInfo user_in?o;
const auto & exact_socdem = user_record["exact_socdem"] ;
setValue(user_info.age, exact_socdem, “age_segment");
setValue(user_info.sex, exact_socdem, "gender");
7 static const auto tail = getConstTail();
std::ostringstream buffer;
buffer <<
81 sipHash64(device_id.data(), device_id.size()) << ‘\t' <
35
```

## Slide 36

36


> Recovered by OCR — confidence 96/100 on the text kept, 68/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Create segments based on
offline and online data
Create Segment
To come in
36
```

## Slide 37

## Crypta

37

## Slide 38

#### Crypta

38


> Recovered by OCR — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Crypta
Yandex COMPANY JOBS FORDEVELOPERS FORADVERTISERS FOR INVESTORS
About History Privacy PressReleases Blog Contact Qo
Technologies /
Crypta
Every day, millions of web users are exposed to banner ads on the pages of Yandex's sites. Advertisers on
Yandex can opt to show their ads only to that part of the viewer audience that is potentially interested in
seeing them, such as people of a certain age or gender. To enable advertisers to target their ads to a specific
audience, Yandex uses its own proprietary behavior analytics technology called Crypta. This technology allows
classification of web users based on their online behavior. Their behaviour just has to differ somehow.
38
```

## Slide 39

#### Example Segments

39


> Recovered by OCR — confidence 90/100 on the text kept, 70/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Example Segments
eee
eee @
test
age_segment_18_20.py
alice_users.py
apartment_room_number.py
apps_users.py
artists.py
auto_interactions.py
avia_travellers.py
bank_cards.py
bought_two_tickets.py
business_travellers.py
compulsory_auto_insurance.py
connection_type.py
console_gamers.py
contest.py
devices_without_google_services.py
digital_viewers.py
direct_clients_by_industry.py
direct_product_users.py
disk_users.py
ecommerce_owners.py
edadeal_offline_purchases_lal.py
expensive_car_customers.py
film_lovers_by_genres.py
gas_stations.py
industry_representatives.py
kbt_customers.py
kfc_visitors.py
kinopoisk_logins.py
kinopoisk_movie_watchers.py
kinopoisk_movie_watchers.py
kz_users.py
laptop_users.py
logged_in_for_plus.py
longterm_interest_mobile_gamers.py
loyal_to_launcher_install.py
macos_users.py
mail_data.py
manufacturer_phone_owners.py
mobile_gamers.py
mobile_operators_users_by_prefix.py
mobile_operators_users.py
multidevice_puid.py
multidevice.py
music_genres_listeners.py
nestle_regions.py
phone_buyers.py
phone_owners.py
phone_with_esim_owners.py
potential_aon_android_users.py
potential_aon_ios_users.py
preinstalled_apps.py
prism.py
proleads.py
realty_interactions.py
recent_passport_accounts.py
score_users_for_telephony.py
searched_for_phone_numbers.py
searched_radisson_on_maps.py
\ CRYPTA
mobile_operators_users_by_prefix.py
mobile_operators_users.py
multidevice_puid.py
multidevice.py
music_genres_listeners.py
nestle_regions.py
phone_buyers.py
phone_owners.py
phone_with_esim_owners.py
potential_aon_android_users.py
potential_aon_ios_users.py
preinstalled_apps.py
prism.py
proleads.py
realty_interactions.py
recent_passport_accounts.py
score_users_for_telephony.py
searched_for_phone_numbers.py
searched_radisson_on_maps.py
seo_specialists.py
smart_gadgets_customers.py
smokers.py
summer_residents.py
travellers.py
video_bloggers.py
want_to_change_the_provider.py
webmaster.py
widgets.py
with_children_by_ages.py
a make
39
```

## Slide 40

#### Example Segments

40


> Recovered by OCR — confidence 91/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Example Segments
v
smart_gadgets_customers.py
smokers.py
travellers.py
video_bloggers.py
want_to_change_the_provider.py
webmaster.py
widgets.py
with_children_by_ages.py
va make
40
```

## Slide 41

#### Travellers

41


> Recovered by OCR — confidence 87/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Travellers
profile > runners > segments > lib > coded_segments > ® travellers.py > ...
82
83 INSERT INTO ‘{output_table}* WITH TRUNCATE
84 SELECT
85 id,
86 id_type,
87 segment_name
88 FROM(
89 SELECT
90 crypta_id AS id,
91 ‘crypta_id' AS id type,
92 CASE
93 WHEN Geo: :RoundRegionById(region, “country").id != Geo::RoundRegionById(CAST(main_region AS Int32), “country").id THEN ‘internati
94 ELSE ‘domestic’
96 MAX(*date*>) AS last_seen,
97 MIN(*date*) AS first_seen,
98 region,
99 week_end_date,
100 FROM $travell_visits
101 GROUP BY region, main_region, crypta_id, week_end_date
103 WHERE
104 last_seen <= week_end_date AND
105 DateTime: : ToDays (DateTime: :MakeTimestamp($parse(last_seen)) —- DateTime: :MakeTimestamp($parse(first_seen))) > @ AND
106 DateTime: : ToDays (DateTime: :MakeTimestamp($parse(week_end_date)) - DateTime: :MakeTimestamp($parse(first_seen))) <= 7
107. GROUP BY id, id_type, segment_name
108 ue
109
118
41
```

## Slide 42

#### Mail Data

42


> Recovered by OCR — confidence 87/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Mail Data
profile > runners > segments > lib > coded_segments > @ mail_data.py > ...
13
14 segment_query = """
15 INSERT INTO ‘{output_table}* WITH TRUNCATE
16 SELECT id, id_type, segment_name
17 FROM *{mail_data_table}*;
18
19 INSERT INTO ‘{sample_table}* WITH TRUNCATE
20 SELECT,
21 yandexuid,
22 segment_name
23 FROM (
24 SELECT matching. yandexuid AS yandexuid, mail_data.segment_name AS segment_name
25 FROM ‘{mail_data_table}* AS mail_data
26 INNER JOIN ‘{indevice_yandexuid_matching}* AS matching
27 USING (id, id_type)
28 )
29 GROUP BY yandexuid, segment_name
30 uae
32
BS class PrepareMailSampleForLalSegments(RegularSegmentBuilder) :
34 keyword = 549
65 name_segment_dict = {
36 ‘aviaticket': 1404,
38 "hotel': 1406,
39 }
42
```

## Slide 43

#### Gas Stations

43


> Recovered by OCR — confidence 93/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Gas Stations
profile > runners > segments > lib > coded_segments > @ gas_stations.py > ...
92
94
95
96
98
100
101
102
103
104
105
106
107
108
109
110
111
class ProcessedDeepVisitLogForGasStations(DayProcessor):
def requires(self):
return deep_visits.org_visits_deep_external_input(self.date)
def process_day(self, inputs, output_path):
organization_categories=config.ORGANIZATION_CATEGORIES,
deep_visits=inputs.table,
matching_idfa=get_matching_table('idfa', ‘crypta_id'),
matching_gaid=get_matching_table('gaid', ‘crypta_id'),
[u'("{}", "{}")'.format(key, value)
for key, value in name_to_variable.iteritems()]
output_table=output_path,
),
transaction=self.transaction,
43
```

## Slide 44

#### Example ML Model Types

44


> Recovered by OCR — confidence 88/100 on the text kept, 72/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Example ML Model Types
eee
legal_entities_model_application.py
legal_entities_model_training.py
its_model_application.py
legal_office_visits_model_training.py
market_model_application.py
market_model_training.py
market_rfm_model_application.py
market_rfm_model_training.py
marriage_model_application.py
marriage_model_training.py
medical_clinic_model_application.py
medical_clinic_model_training.py
mortgage_approval_model_application.py
mortgage_approval_model_training.py
online_cinema_model_application.py
online_cinema_model_training.py
online_payment_model_training.py
online_sales_register_model_application.py
online_sales_register_model_training.py
online_shopping_model_application.py
online_shopping_model_training.py
pharmacy_model_application.py
pharmacy_model_training.py
realty_visit_model_application.py
realty_visit_model_training.py
tv_viewers_model_application.py
tv_viewers_model_training.py
windows_installation_model_application.py
windows_installation_model_training.py
va make.
44
```

## Slide 45

#### Basic example of household details

45


> Recovered by OCR — confidence 88/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Basic example of household details
78
79
graph > metrics > household > & query.sq!
44
45
46
FROM $composition
GROUP BY $size_to_range(size) AS key;
END DEFINE;
DEFINE SUBQUERY $hh size by crypta id($title, $predicat) AS
SELECT
($title || key) AS key,
COUNT(1) AS hh_size_by_crypta_id
FROM $composition
WHERE $predicat(size, socdems)
GROUP BY CAST(Yson::GetLength(Yson::Lookup(data, ‘crypta_ids')) AS String) AS key;
END DEFINE;
DEFINE SUBQUERY $hh_by_socdems($title, $predicat) AS
$hh_socdem = (
SELECT
hhid,
size,
IF((Yson::LookupInt64(info, 'female') @), ‘female’, Null) AS has_female,
IF((Yson::LookupInt64(info, ‘male') != @), ‘male’, Null) AS has_male,
IF((Yson::LookupInt64(info, ‘grand') != @), ‘grand', Null) AS has_old,
IF((Yson::LookupInt64(info, ‘child') != @), ‘child', Null) AS has_child
FROM $composition
WHERE $predicat(size, socdems)
SELECT ($title || groups) AS key, hh_c AS hh_socdem_count
FROM (
SELECT groups, SUM(size) AS hh_c
FROM $hh_socdem
GROUP BY String::JoinFromList(
Listsort(AsList(has female, has mate, has old, has child).
*_') AS groups
) WHERE groups != "";
END DEFINE;
45
```

## Slide 46

AppMetrica being used to pull wifi connection types:

46


> Recovered by OCR — confidence 86/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
AppMetrica being used to pull wifi
connection types:
profile > runners > segments > lib > coded_segments > ® connection_type.py
9 connection_type_query = """
@ INSERT INTO ‘{output_table}” WITH TRUNCATE
SELECT
AS id_type,
5 WHEN types
6€ WHEN types
ELSE '3g_4g'
f END AS segment_name
9 FROM (
® SELECT
id,
ToSet (AGGREGATE_LIST_DISTINCT(segment_name)) AS types
FROM *{input_table}
GROUP BY id
AsSet('3g') THEN ‘3g'
AsSet('4g') THEN ‘4g'
¢ class ConnectionType(RegularSegmentBuilder):
80 name_segment_dict = {
'3g': (557, 17823841),
‘4g': (557, 17823853),
"3g_4g': (557, 17823847),
BE number_of_days = 35
BE def requires(self):
9 return {
self.date,
self.number_of_days,
46
```

## Slide 47

##### AppMetrica data being used to separate users with common SSIDs (wifi networks)

47


> Recovered by OCR — confidence 90/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
AppMetrica data being used to separate users with common
SSIDs (wifi networks)
class ImportSsidMobileMetrikalask(BaseTask):
date = DateParameter()
SSID_THRESHOLD = 20
YUID_THRESHOLD = 20
DAYS_IN_MONTH = 7
def requires(self):
asks must be done to complete this task
task_list = [
ImportSsidMobileMetrikaDayTask(date=self.date, target_date=target_date, ssid_threshold=self.SSID_THRESHOLD)
for target_date in days_range_back(self.date, self.DAYS_IN_ MONTH)
]
return task_list
47
```

## Slide 48

AppMetrica data being used to separate users with common SSIDs (wifi networks)

48


> Recovered by OCR — confidence 90/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
AppMetrica data being used to separate users with common
SSIDs (wifi networks)
def _run(self):
self.yt.create_table_with_schema(
self.destination, self.destination_schema, strict=True, recreate_if_exists=True
)
with self.yt.TempTable() as unexploded, self.yt.TempTable() as not_unique:
self.yql.execute(self.query(unexploded), syntax_version=1)
run_native_reduce(
source=unexploded,
destination=not_unique,
proxy=self.yt.proxy,
transaction=self.yt.transaction_id,
pool=conf.Yt.POOL,
title="Explode yandexuids with common wifi access point",
reduce_by=["ssid"],
)
yuid_pair = [conf.Constants.YUID_LEFT, conf.Constants.YUID_RIGHT]
self.yt.run_sort(not_unique, not_unique, sort_by=yuid_pair)
run_native_reduce(
source=not_unique,
destination=self.destination,
proxy=self.yt.proxy,
transaction=self.yt.transaction_id,
pool=conf.Yt.POOL,
title="Make yandexuids with common wifi access point unique",
reduce_by=yuid_pair,
)
self.yt.run_sort(self.destination, sort_by=yuid_pair)
self.yt.set(self.destination + "/@generate_date", self.date. isoformat())
48
```

## Slide 49

#### Sources

Search Data Wifi

49


> Recovered by OCR — confidence 85/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Sources
graph > fuzzy > lib > ®@ config.py > ¢ GeoPaths
class SourceTypes(object):
EMAIL_SIMILAR = “EMAIL SIMILAR"
GEO_HOMEWORK = "GEO HOMEWORK"
HOUSEHOLD = "HOUSEHOLD"
REQANS_LOG = “REQANS LOG" ——= Search Data
SSID = "SSID" ——\Vifj
49
```

## Slide 50

#### Yandex IDs Associated with Email

50


> Recovered by OCR — confidence 74/100 on the text kept, 65/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Yandex IDs Associated with Email
class EmailPaths(object):
ROOT = ROOT
# Emails
BASE = "{root}/email". format(root=RO0T)
ALL_EMAILS_TABLE = "{base}/all_emails". format (base=BASE)
ALL_EMAIL_LOGINS_PAIRS_TABLE = "{base}/all_email_logins.pairs". format (base=BASE)
ALL_EMAILS GROUPED_BY_LOGIN = "{base}/all_email_logins.groups". format (base=BASE)
ALL_YUID_PAIRS_FROM_SIMILAR_EMAILS = "{base}/all_yuid_pairs_from_similar_emails". format (base=BASE)
ALL_EMAILS_TABLE_SCHEMA = {"emai "string", "yuids": “any"}
ALL_EMAIL_LOGINS_TABLE_SCHEMA = {"login": "string", "email": "string", “yuids": "“any"}
ALL_EMAILS_GROUPED_BY_LOGIN_SCHEMA = {"login": "string", "all_emails": "any", “howmany": "uint64"}
ALL_EMAIL_LOGINS_PAIRS_TABLE_SCHEMA = {
“email_1": "string",
“yuids_1": “any",
“yuids_2": "any",
}
ALL_YUID_PAIRS_FROM_EMAIL_LOGIN_SCHEMA = {
Constants. YUID_LEFT: (“uint64", True),
Constants. YUID_RIGHT: ("uint64", True),
"match": "any",
ALL_YUID_PAIRS_FROM_SIMILAR_EMAILS SCHEMA = {
```

## Slide 51

#### Login Data

Extracting multiple types of identifiers

51


> Recovered by OCR — confidence 91/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Login Data
graph > fuzzy > lib > tasks > sources > visitlog_logins > ® extract.py > ...
return TFilterRareLoginsOptions(Threshold=self.threshold).SerializeToString()
@property
def filter_keys_options(self):
return TFilterKeysOptions(
Keywords=[
“clientid",
“emailhash",
“computerid",
“suserid",
]
).SerializeToString()
Extracting
multiple types
of identifiers
51
```

## Slide 52

#### Passport

52


> Recovered by OCR — confidence 76/100 on the text kept, 70/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Passport
@ passport.yandex.com,
©) confiant-inc/priva... [3 Tracker DBs
punt, y
2t dire
tions and u
Yandex
@ hittps://emplist.co...
@ https:j/vendor-list..
1% Consent String De...
Registration
Technique protect...
52
```

## Slide 53

#### Passport User ID Associated with Phone

53


> Recovered by OCR — confidence 88/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Passport User ID Associated with Phone
graph > data_import > passport > lib > query > = passport.sql
33
34 $out_login_tbl = $soup_output_dir || $edge(IdType::PUID(), IdType::PHONE(), SourceType::PASSPORT_PROFILE(), LogSource: : PASSPORT_PHONE_DUMP( ) ) ;
3 INSERT INTO $out_login_tbl WITH TRUNCATE
SELECT
37 id1,
38 IdType::PUID() AS id1Type,
39 id2,
IdType::PHONE() AS id2Type,
SourceType: : PASSPORT_PROFILE() AS sourceType,
LogSource: : PASSPORT_PHONE_DUMP() AS logSource,
é ListCreate(String) AS dates
44 FROM (
45 SELECT DISTINCT puid, phone
4 FROM $log FLATTEN LIST BY phones AS phone
) WHERE Identifiers: : IsSignificantPhone(phone)
GROUP BY
puid AS id1,
50 phone AS id2
53
```

## Slide 54

54


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 84/100 on the text kept, 76/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Deobfuscation: LLVM Opt + SiMBA + GAMBA

[left panel, orange label]  Polaris
Instruction substitution (loop 3)

12    uVar1 = param1 & 3;                                    [row clipped by panel top edge]
13  if (uVar1 == 0) {
14    uVar1 = ((param1 ^ 0xffffffff) & 0x19495cff | param1 & 0xe6b6a300) ^ 0x5c1c73bf;
15    uVar1 = (uVar1 ^ param1 ^ 0xffffffff) & uVar1;         [line start partly under tooltip]
16    uVar5 = (param1 ^ 0x625558ec) & (param1 ^ 0xffffffff); [line start partly under tooltip]
17    uVar2 = (param1 ^ 0x625558ec) & param1;
18    uVar5 = uVar5 & uVar2 | uVar5 ^ uVar2;
19    uVar5 = (uVar5 ^ 0xffffffff) & 0xd8ff8853 | uVar5 & 0x270077ac;
20    uVar2 = (param1 & 0x1ba026fa | (param1 ^ 0xffffffff) & 0xe45fd905) ^ 0x860a81e9;
21    uVar3 = (param1 ^ 0xffffffff) & 0x625558ec | param1 ^ 0x9daaa713;
22    uVar3 = (uVar3 ^ 0xffffffff) & 0x741226bb | uVar3 & 0x8bedd944;
23    uVar2 = (uVar2 ^ param1) & uVar2 ^ 0xffffffff;
24    uVar2 = (uVar2 ^ ((uVar3 ^ 0x741226bb) & 0x6590700b | (uVar3 ^ 0x8bedd944) & 0x9a6f8ff4) ^
25                     0x6590700b) & uVar2;
26    uVar2 = (uVar2 ^ 0xffffffff) & 0x1eba5d23 | uVar2 & 0xe145a2dc;
27    uVar1 = (uVar2 ^ 0x1eba5d23 | 0x625558ee) ^ 0xffffffff;
28    uVar1 = (((uVar2 ^ 0x1eba5d23) & 0x60b6df70 | (uVar2 ^ 0xe145a2dc) & 0x9f49208f) ^ 0x2e3879e) &
29           0x625558ee;
30    local_c = (((uVar1 ^ 0xffffffff) & 0x7c83e458 | uVar1 & 0x837c1ba7) ^ 0x7c83e458 |
31             ((uVar5 ^ 0xffffffff) & 0x721da317 | uVar5 & 0x8de25ce8) ^ 0x721da317) *
32             (uVar1 & uVar1 | uVar1 ^ uVar1);
33  }
34  else if (uVar1 == 1) {
35    uVar1 = (((param1 ^ 0xffffffff) & 0x5fb8011c | param1 & 0xa047fee3) ^ 0x5fb8011c | 0x8de25ce8) &
36             ((param1 ^ 0x721da317) & param1 ^ 0xffffffff);
37    uVar1 = uVar1 & 0x8de25ce8 | (uVar1 ^ 0xffffffff) & 0x721da317;
38    uVar1 = ((uVar1 ^ 0xffffffff) & 0x53584bcb | uVar1 & 0xaca7b434) ^ 0x53584bcb | 0x45552f40;
39    uVar5 = uVar1 ^ 0xffffffff;
40    local_c = ((uVar5 ^ uVar1) & uVar5) * -(-3 - param1);
41  }
42  else if (uVar1 == 2) {
43    uVar1 = (param1 | 0xfaf8dc98) & ((param1 ^ 0x5072367) & param1 ^ 0xffffffff);
44    uVar1 = ((uVar1 & 0x68b867d3 | (uVar1 ^ 0xffffffff) & 0x9747982c) ^ 0x9240bb4b) & 0xbaaad0bf;
45    uVar5 = ((param1 ^ 0xffffffff) & 0x368db37e | param1 & 0xc9724c81) ^ 0x8c2763c1;
46    uVar5 = (uVar5 ^ param1 ^ 0xffffffff) & uVar5;
47    uVar2 = (param1 ^ 0xffffffff) & 0xfffffffb | param1 & 4;
48    uVar2 = (uVar2 ^ 0xfffffffb) & uVar2;
49    uVar3 = (param1 | 0xb4a770ab) & (param1 ^ 0xffffffff | 0x4b588f54);
50    uVar3 = uVar3 & 0x1c4a08ec | (uVar3 ^ 0xffffffff) & 0xe3b5f713;
51    uVar4 = (uVar2 ^ 0xffffffff | uVar3 ^ 0xa8ed7843) ^ 0xffffffff;
52    uVar1 = (uVar2 ^ 0xffffffff) & (uVar3 ^ 0x571287bc) | uVar2 & (uVar3 ^ 0xa8ed7843);
53    local_c = ((uVar1 ^ 0xffffffff | uVar5 ^ 0xffffffff) &
54             (((uVar1 ^ 0xffffffff) & uVar5 | uVar1 & (uVar5 ^ 0xffffffff)) ^ 0xffffffff) ^
55             0xffffffff) * (uVar4 & uVar1 | uVar4 ^ uVar1);
56  }
57  else {
58    uVar1 = ((param1 ^ 0xffffffff) & 0x769a091f ^ 0x769a091f) &
59             ((param1 ^ 0xffffffff) & param1 ^ 0xffffffff);
60    uVar5 = (uVar1 ^ 0x8bedd944) & uVar1;
61    uVar1 = (uVar1 | 0x741226bb) ^ 0xffffffff;
62    uVar1 = uVar5 & uVar1 | uVar5 ^ uVar1;
63    local_c = -(-0x374a3fe6 - (-0x374a3fe6 - (0x45552f41 - param1))) *
64             ((((uVar1 ^ 0xffffffff) & 0x52a311c3 | uVar1 & 0xad5cee3c) ^ 0x26b1377d) & 5);
65  }
66  return local_c;

[tooltip overlaying the left edge of lines 15-16, itself cut off by the slide edge]
...004d56, OTHER:00004d59]

[right panel, orange label]  LLVM Optimisation  + SiMBA + GAMBA
 9    uVar1 = param_2 & 3;
10    iVar3 = (param_2 ^ 0xbaaad0bf) * (param_2 | 4);          [3]
11    if (uVar1 != 2) {
12      iVar3 = (param_2 + 0xbaaad0bf) * (param_2 & 5);        [4]
13    }
14    iVar2 = (param_2 + 2) * (param_2 | 0xbaaad0bf);          [1]
15    if (uVar1 != 0) {
16      iVar2 = (param_2 & 0xbaaad0bd) * (param_2 + 3);        [2]
17    }
18    if (uVar1 < 2) {
19      iVar3 = iVar2;
20    }
21    return iVar3;

[teal label]  Completely Recovered
```

## Slide 55

#### Crypta - Geo graphs

Using lat/long data associated with “predicted home”, linked to Yandex UID

55


> Recovered by OCR — confidence 85/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Crypta - Geo grap
Using lat/long
data associated
with “predicted
home’, linked to
Yandex UID
graph > fuzzy
lib > tasks > sources > geo > C geo_operations.h
void Do(TTableReader<TNode>* input, TTableWriter<TGeoSquare>* output)
override {
for
input->IsValid( input->Next()) {
t auto& row = input->GetRow();
if (not IsRowValid(row)) {
continue;
t ui64 yandexuid = FromString<ui64>(row|"yandexuid"] .AsString());
auto& homeCoordinates = row|"predicted_home"'];
latitude = homeCoordinates |" latitude"] .AsDouble();
to longitude = homeCoordinates |" longitude") .AsDouble( ) ;
onst
onst auto& square = computeSquare({.Lat = latitude, .Lon = longitude}, State->radius());
for (int beltOffset : {-1, @, 1}
for (int sqoffset : {-1, 0}
if (beltoffset
continue;
ynst ui64 square_idx = ConvertSquareToIdx({.Belt =
TGeoSquare out;
out. set_yandexuid(yandexuid) ;
out.set_lat( latitude) ;
out.set_lon( Longitude) ;
square.Belt + belt0ffset, .Sq =
square.Sq + sq0ffset
54
```

## Slide 56

#### Crypta - Geo graphs

Then using that data to find literal neighbors within a certain radius of that home

56


> Recovered by OCR — confidence 88/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Crypta - Geo graphs
Then using that
data to find
literal neighbors
within a certain
radius of that
home
public:
lib > tasks > sources > geo > C geo_operations.h
TEindNeighbors: public IReducer<TTableReader<TGeoSquare>, TTableWriter<TNeighborsDistance>> {
: State(
TFindNeighbors(const TBuffer& buffer
: State(buffer
d Do(TTableReader<TGeoSquare>* input, TTableWriter<TNeighborsDistance>* output) override
‘onst double radius = State->radius();
TVector<TGeoSquare> candidates;
for (; input->IsValid(); input->Next()) {
const auto& row = input->GetRow();
xrange(candidates.size())) {
for (auto j : xrange(i + 1, candidates.size()
suto& left = candidates.at(i);
const auto& right = candidates.at(j);
if (left.yandexuid() == right. yandexuid()
continue;
distance = computeDistance({.Lat = left.lat(), .Lon = left.lon()}, {.Lat =
distance > radius
inu
‘TNeighborsDistance out;
out. set_distance(distance) ;
output->AddRow(out) ;
```

## Slide 57

#### AppMetrica and Taxi data being used generate segments about households with children:

57


> Recovered by OCR — confidence 86/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
AppMetrica and Taxi data being used generate segments
about households with children:
self.yql.query(
2pp_metrica query. format (
devid_by_app_table=self.input() ['DevidByApp'].table,
app_to_segment_name='\n'.join(app_segment_name_tuples),
transaction=self.transaction,
build_segment(self, inputs, output_path):
with self.yt.TempTable() as taxi_puid_table, \
self.yt.TempTable() as app_metri table:
extract children from taxi
taxi_puid_table,
self.prepare_with_children_by_app(app_metrica_table)
self.yql.query(
with_children_query_template. format (
metrics_table=inputs['ProcessedMetrics'].table,
app_metrica_table=app_metrica_table,
taxi_data_table=taxi_puid_table,
id_to_crypta_id_table=config.VERTICES_NO_MULTI_PROFILE,
crypta_id_to_hhid_table=config.HOUSEHOLD_CRYPTA_ID_TO_HHID,
yandexuid_to_hhid_table=config.HOUSEHOLD_REVERSED_TABLE,
hhid_to_yandexuid_table=config.HOUSEHOLD_ENRICH_TABLE,
output_table=output_path,
57
```

## Slide 58

#### ID mapping associations:

58


> Recovered by OCR — confidence 85/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ID mapping associations:
taxi_data_table=taxi_puid_table,
crypta_id_to_hhid_table=config.HOUSEHOLD_CRYPTA_ID_TO_HHID,
yandexuid_to_hhid_table=config.HOUSEHOLD_REVERSED_TABLE,
hhid_to_yandexuid_table=config.HOUSEHOLD ENRICH TABLE,
output_table=output_path,
58
```

## Slide 59

Profiles integrate biometric data, most likely from smart speakers that use Yandex’s Alice smart assistant

59


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Profiles integrate biometric data, most likely from smart
speakers that use Yandex’s Alice smart assistant
Yandex COMPANY JOBS FOR DEVELOPERS FOR ADVERTISERS FQ
About History Privacy Press Releases Blog Contact
Press Releases / 2022 /
Yandex Launches Smart Devices With Alice in
Uzbekistan
Internet, November 22, 2022. Uzbekistan’s local
Stations with Alice. Upon purchasing a smart s|
pene e P Stations are smart speakers with Alice. A single Yandex Plus subscription allows you to play music, podcasts,
or playlists with personal recommendations on Yandex Station. Alice, the voice assistant on board, can
entertain children with an educational game or compose a fairy tale together. She will tell you about the
weather or remind you to buy groceries. Alice loves talking and will hold a conversation with ease: currently, in
Russian only.
59
```

## Slide 60

#### Possible Children by Voice

60


> Recovered by OCR — confidence 88/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Possib
e Children by Voice
profile > runners > segments > lib > coded_segments > ® children_age_segment_clarification.py > ..
13 clarify_children_yql_template =
14 $possible_children_by_voice = (
15 SELECT ‘uuid’, TableName() AS ‘date’, '@_12' AS segment_name
17 WHERE bio_child > 0.8
18 3
19
20 Spossible children by voice = (
21 SELECT DISTINCT “uuid’, ‘date’, segment_name
22 FROM $possible_children_by_voice
24
25 $possible children by voice = (
26 SELECT “uuid’, segment_name
27 FROM $possible_children_by_voice
28 GROUP BY ‘uuid*, segment_name
29 HAVING COUNT(*) >= 2
30 3
31
32 $sources_new_age = (
33 SELECT matching.cryptaId AS cryptaId,
34 CASE
35 WHEN socdem storage.birth date > ‘{thirteenth birthday}' THEN '@ 12°
36 WHEN ‘{thirteenth_birthday}' >= socdem_storage.birth_date AND
37 socdem_storage.birth_date > '{eighteenth_birthday}' THEN '13_17'
38 ELSE '18_99°
39 END AS segment_name
40 FROM ‘{socdem_storage_table}* AS socdem_storage
41 INNER JOIN ‘{id_to_crypta_id_table}* AS matching
42 ON socdem_storage.id == matching.id AND socdem_storage.id_type == matching. id_type
43 WHERE socdem_storage.birth_date is not Null
44 UNION ALL
45 SELECT matching.cryptaId AS cryptaId, biometry.segment_name AS segment_name
46 FROM $possible_children_by_voice AS biometry
47 INNER JOIN ‘{id_to_crypta_id_table}’ AS matching
48 ON biometry. *uuid* matching. id
60
```

## Slide 61

UI for Infographics Card

61


> Recovered by OCR — confidence 81/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
_UI for Infographics Card
const marriedText = convertMarriedToSingleText(exactDemographics.gender, married);
const incomeText = convertIncomeSegmentToText (exactDemographics. income) ;
const hasChildrenText = convertHasChildrenToText(hasChildren) ;
return (
<div className="BasicInfoGraphics">
<img alt="" className="BasicInfoGraphics—Image" src={images [exactDemographics.gender] }/>
<div “BasicInfoGraphics-Bubble BasicInfoGraphics—Bubble_family">{marriedText}</div>
<div BasicInfoGraphics-Bubble BasicInfoGraphics—Bubble_income">{incomeText}</div>
<div BasicInfoGraphics-Bubble BasicInfoGraphics—Bubble_children">{hasChildrenText}</div>
<div className="BasicInfoGraphics-Interest BasicInfoGraphics-Interest_first">
<div className="BasicInfoGraphics—InterestIcon"
style={{ backgroundImage: ‘url(${interestIcons(6]})> }}/>
</div>
<div className="BasicInfoGraphics-Interest BasicInfoGraphics-Interest_second">
<div className="BasicInfoGraphics-InterestIcon"
style={{ backgroundImage: ‘url(${interestIcons[1]})> }}/>
</div>
<div className="BasicInfoGraphics-Interest BasicInfoGraphics-Interest_third">
<div className="BasicInfoGraphics-InterestIcon"
style={{ backgroundImage: ‘url(${interestIcons[2]})* }}/>
© icons
> apps
~ interests
"@ agro.svg
animals.svg
appliances.svg
beauty.svg
business.svg
clothes.svg
construction.svg
‘mw education.svg
“a electronics.svg
“a family.svg
‘a finance.svg
‘a gifts.svg
Js index.js
job.svg
realty.svg
rest.svg
sport.svg
stationery.svg
telecom.svg
61
transport.svg
```

## Slide 62

#### Search Profile by ID

62


> Recovered by OCR — confidence 84/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Search Profile by ID
web > portal > src > graph > search > JS SearchPanel.js > ...
<div key={"inputs—" + suffix} className="input-group">
14 <div style={{display: showIdInput ? "block" : "none"}}>
<ValueInput
key="id_value"
placeholder="[id value]"
value={parameters ["idValue" + suffix]}
onChange={changeParameter("uid" + suffix)}
return (
experiments.status !== 403 && (
<div className="experiments—bar">
<div className="experiments-select-uid-type">
<RadioButton
value={act iveUid}
view="default"
className="select-sorting"
onChange={(event) => selectUidType(event.target.value) }
{ value: "uid", children: t("by") + " yandexuid" },
{ value: “cryptaId", children: t("by") + " CryptaID" },|
|
62
```

## Slide 63

#### UI - Available App Icons

63


> Recovered by OCR — confidence 83/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
UI - Available App Icons
4S Timedinterests.js
> pages
> components
v icons
fa active.svg
fa disabled.svg
com yandex.lavka
>
>
> comyandex.mobile.drive
> comyandex.music.auto
>
com yandex.music.xiaomi
com yandex.toloka.androidapp
fa disabled.svg
default
ruyandex.androidkeyboard
ruyandex.androidkeyboard.auto
ruyandex.androidkeyboard.tv
ruyandex.blue.market
ruyandex.disk
ruyandex.disk.notificationserviceext
ruyandex.disk.shareext
ruyandex.lavka
ruyandex.mail
ruyandex.mail.notificationserviceextension
ruyandex.market
\ CRYPTA
ru.yandex.mail.notificationserviceextension
ruyandex.market
ruyandex.metro
ruyandex.mobile
ruyandex.mobile.drive
ruyandex.mobile.drive.notification
ruyandex.mobile.keyboard
ruyandex.mobile.KeyboardExtension
ruyandex.mobile.metro
ruyandex.mobile.music
ruyandex.mobile.music.push-extension
ruyandex.mobile.music.widget-extension
ruyandex.mobile.navigator
ruyandex.mobile.NotificationService
ruyandex.mobile.search
ruyandex.mobile.toloka
ruyandex.mobile.translate
ruyandex.mobile.weather-v2
ruyandex.music
ruyandex.music.samsung
ruyandex.searchplugin
ruyandex.taxi
ruyandex.telemost
ruyandex.traffic
ruyandex.translate
ruyandex.uber
ruyandex.uber-kz
ruyandex.weatherplugin
ruyandex yandexnavi
ru.yandex.yandexmaps
ru.yandex.yandexnavi
ru.yandex.ymarket
ru.yandex.ytaxi
Js index.js
~ interests
‘m agro.svg
‘= appliances.svg
63
```

## Slide 64

#### Ids Associated with Social Media Accounts

64


> Recovered by OCR — confidence 81/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Ids Associated with Social Media Accounts
web > portal > src > public-info > sections > GraphSection > 45 GraphSection.js
import React, { useEffect, useMemo, useState } from
import { useSelector } from "“react-redux’
react";
import { getPublicGraph, getPublicGraphLoading } from "../../store/selectors";
import { Graph, GraphSkeleton } from "../../components/Graph/Graph"
import { Section } from “../../components/Section/Section";
import { getServicelcon } from "../../icons/services'
import { getAppIcon } from "../../icons/apps";
import "./GraphSection.scss";
import noData from "./no-data.sva";
const IMAGE_SIZE_XS = 12;
const IMAGE_SIZE_S = 31
const IMAGE_SIZE_M = 56;
const IMAGE_SIZE_L = 80;
const NODE_MAPPING = {
email: {
imageSize: IMAGE_SIZEM,
imageHref: "mail",
yandexuid: {
imageHref: "yandexuid",
idfa: {
imageSize: INAGE_SIZE_L,
imageHref: "ios",
gaid: {
imageSize: IMAGE_SIZE_L,
imageHref: “android”,
oaid: {
imageHref: "android",
imageHref: "key",
imageHref: "key",
instagram_login: {
imageHref: "instagram
{
imageSize: IMAGE_SIZEM,
3 GraphSection >
web > portal > src > public-info > sections > GraphSection > 4s GraphSection.js > @ GraphSection > © useEffe:
instagram_id: {
imageSize: IMAGE_SIZE_M,
imageSize: IMAGE_SIZE_M,
imageHref: "facebook"
ok_id: {
imageHref: "ok"
imageSize: IMAGE_SIZE_M,
imageHref: "vk"
vk_name: {
imageSize: IMAGE_SIZE M,
kp_id: {
imageHref: "kinopoisk'
if (item. idType
return { imageHref: item.icon, imageSize: IMAGE_SIZE_S };
return NODE_MAPPING[item. icon] 77 { imageHref: “default, imageSize: IMAGE_SIZE_XS
function getImage(item) {
const disabled = !item.isActive;
if (item, idType *uuid') {
return getAppIcon(item.imageHref, disabled)
scatch(() => getAppIcon("default", disabled) );
return getServiceIcon(item.imageHref, disabled)
scatch(() => getServiceIcon("default", disabled) )
64
```

## Slide 65

## Matcher

65

## Slide 66

#### Matcher

66


> Recovered by OCR — confidence 87/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Matc
ner
> bin
> bundle
v lib
> config
Y matchers
base_matcher
beeline_matcher
er_telecom_matcher
intentai_matcher
mts_matcher
>
rostelecom_matcher
ya.make
G parser.cpp
C parser.h
66
```

## Slide 67

#### Rostelecom Matcher

67


> Recovered by OCR — confidence 85/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Rostelecom Matcher
ext_fp > matcher > lib > matchers > rostelecom_matcher > G rostelecom_matcher.cpp
22 TConnection [RostelecomMatcher: :MakeConnection(const TFpEvent& event) {
23 return {
24 «Ip = event.GetIp(),
25 «Port = event.GetPort(),
27 «Domain = NMcDomain: :GetMcDomainForRostelecom(event.GetDuid()),
30
31 void TRostelecomMatcher: :AddConnection(const TFpEvent& event) {
32 auto connection = MakeConnection(event);
33
34 Stats. Count->Add("events. incoming. rostelecom. count") ;
35 Request += TStringBuilder() << connection.Ip << ‘\t'
36 << connection.Port << '\t'
37 << connection.Timestamp << '\t'
38 << connection.Domain << ‘\n';
40
42 if (Request. length() ®) {
43 return TMatches();
44 }
45 const auto& requestId = CreateGuidAsString();
46 Log->info("Rostelecom request {} body:\n{}", requestId, Request);
47
48 NNeh::TMessage message(GetApiUrl(), "");
49 Y_ENSURE (NNeh: :NHttp: :MakeFullRequest(message, "", Request, "“text/plain"), "Failed to build request to Rostelecom API");
52 const auto& resp = MakeRequest(Client, message, TDuration::MilliSeconds(Config.GetApiCallTimeoutMs()), “Rostelecom", requestId, Log);
53
54 return ParseResponse(resp->Data) ;
55 }
56
57 TString TRostelecomMatcher::GetApiUrl() const {
58 return “post://" + Config.GetApiUrl();
67
```

## Slide 68

#### Rostelecom Matcher

68


> Recovered by OCR — confidence 88/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Rostelecom Matcher
ext_fp > matcher > lib > matchers > rostelecom_matcher > G rostelecom_matcher.cpp
22
23
24
25
26
27
28
29
TConnection [Rostelecomatcher::MakeConnection(const TFpEvent& event) {
return {
-Ip = event.GetIp(),
«Port = event.GetPort(),
-Timestamp = event.GetUnixtime(),
-Domain = NMcDomain: :GetMcDomainForRostelecom(event.GetDuid()),
68
```

## Slide 69

#### Rostelecom Matcher

69


> Recovered by OCR — confidence 86/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Rostelecom Matcher
41
42
43
44
45
46
47
48
49
58
51
52
55
TMatches TRostelecomMatcher: :GetMatches() {
if (Request. length() == @) {
return TMatches();
}
const auto& requestId = CreateGuidAsString();
Log->info("Rostelecom request {} body:\n{}", requestId, Request);
NNeh::TMessage message(GetApiUrl(), "");
Y_ENSURE (NNeh: :NHttp: :MakeFullRequest(message, "", Request, "text/plain"), "Failed to build request to Rostelecom API")
const auto& resp = MakeRequest(Client, message, TDuration: :MilliSeconds(Config.GetApiCallTimeoutMs()), “Rostelecom", requestId, Log);
return ParseResponse(resp->Data) ;
69
```

## Slide 70

#### Test Result Data

70


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 78/100 on the text kept, 67/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Deobfuscation: SOUPER

[orange label]  Hikari
Bogus Control Flow ( loop 2)

14  if (uVar2 == 0) {
15    if (((((uRam00010ae8 | uRam00010aec) ^ 0x3c2e5570) & 0x97ff2bd7) + 0x64293ba9 < 0xe0465c21) {
16      bVar1 = true;
17    }
18    else {
19      bVar1 = false;
20    }
21    while( true ) {
22      while (bVar1) {
23        bVar1 = false;
24      }
25      if (0x5fd76e94 < ((iRam00010af0 + iRam00010af4 ^ 0x41005e8aU) + 0x63d028ff) * 0x65edfa51)
26      break;
27      bVar1 = true;
28    }
29    if ((iRam00010af8 * iRam00010afc + 0xd9ef92c7U | 0xba1e4315) + 0xce83d3a0 < 0x8bb488b1) {
30      do {
31      } while (((uRam00010c30 ^ uRam00010c34) + 0x6f44ee27 & 0x7ca03c77) * 0x5ed0b58a == -0x29120a04
32              );
33    }
34    do {
35      local_c = (param1 | 0xbaaad0bf) * (param1 ^ 2);
36    } while (((uRam00010b00 / uRam00010b04 | 0xbabf5164) * -0x32ee4c95 & 0x67c7c119) < 0x20a96022);
37    do {
38    } while ((uRam00010b10 / uRam00010b14 + 0xc8de4516) / 0x936b17aa == 0xa9f0a4ac);
39  }

[orange label pointing at the boxed line 15]  Opaque Predicate

[right edge: control-flow-graph overview thumbnail, node text illegible]
```

## Slide 71

# Roadmap

●Background on Yandex Leak ●Dive into code: ○What data Yandex is collecting ○What Yandex is doing with that data ○Who Yandex is sharing that data with ● Conclusions and wrap up

●Q&A

71

## Slide 72

## Conclusion

72

## Slide 73

#### Wrap Up

- ●Yandex has access to a broad international reach of data and it has been evasive about what it can do with that data

●A small amount of data can say a lot when it is matched to entries from a company’s other data sources and analyzed

●Yandex has code to sync some of its data with a Russian-state owned entity

73

## Slide 74

#### Takeaways

●Anonymization is very easily undone when data gets combined with pools from other sources that may contain identifying data

●Pay attention to who runs your SDKs, what data points they collect, and where they send your user data. ●Who gets access to a company’s user data when its assets are sold, the geopolitical climate changes, or a government tightens its control?

74

## Slide 75

## Q&A

Link to Write Up: <u>https://bit.ly/455utBP</u>

75
