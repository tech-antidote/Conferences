---
title: "Protecting Small Organizations in the Era of AI Bots"
speakers: ["Rama Hoetzlein"]
conference: "Black Hat"
conference_full: "Black Hat USA 2025"
edition: "USA"
year: 2025
source_pdf: "BlackHat_USA_2025_Slides/Rama Hoetzlein_Protecting Small Organizations in the Era of AI Bots.pdf"
pages: 72
sha256: "5e1fe04879a113f12908f1472b803fd9c89ce4af6fa2243ba8430c447970206b"
text_chars: 42462
ocr_pages: 19
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T23:00:30Z"
---
# Protecting Small Organizations in the Era of AI Bots

**Speakers:** Rama Hoetzlein  
**Conference:** Black Hat USA 2025  
**Source:** `BlackHat_USA_2025_Slides/Rama Hoetzlein_Protecting Small Organizations in the Era of AI Bots.pdf` (72 pages)

## Slide 1

# Protecting Small Organizations in the Era of AI Bots

Rama Carl Hoetzlein

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
XS ‘
i x
~ ([—
‘black hat
FINGS
AUGUST 6-7, 2025
MANDALAY BAY / LAS VEGAS
Protecting Small Organizations
in the Era of Al Bots
Rama Carl Hoetzlein
```

## Slide 2

“51% of Internet traffic is non-human, with 37% of Internet traffic from bad bots”

2025 Imperva, Bad Bot Report

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

## Slide 3

“51% of Internet traffic is non-human, with 37% of Internet traffic from bad bots”

2025 Imperva, Bad Bot Report

“87% of the malicious bot IPs [in our study] were not listed in popular IP blocklists.”

2021 Xigao Li et al., Good Bot, Bad Bot

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

## Slide 4

### Client

The Community Science Institute is a public, non-profit that promotes scientific literacy, volunteer water quality monitoring and certified lab analysis for central New York.

**RAMA CARL HOETZLEIN PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS** #BHUSA @BlackHatEvents

## Slide 5

### Client

CSI Database: Curated, certified, water quality data for Stream & Lake chemistry, Harmful Algae Blooms and Biomonitoring

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

## Slide 6

### Client

We observed that a single server received over 150,000 page hits over 20 days, corresponding to **7,500 hits / day.**

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

## Slide 7

### Client

We observed that a single server received over 150,000 page hits over 20 days, corresponding to **7,500 hits / day.**

Traffic was so severe that it was degrading server performance for CSI’s known human users and clients.

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

## Slide 8

### Early Investigation

#### IP B-class aggregation and org lookup

Visitor traffic is from the entire world, despite the fact that the CSI Database is entirely data for central New York State

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

## Slide 9

### Background

### What existing tools are available?

1. Throttling is ineffective – modern crawlers _observe_ rate limits. 2. Public blocklists are ineffective – up to 87% not listed

3. GREP is ineffective – difficult to interpret, good for spot checks

4. GoAccess, AWStats – summary statistics hide details

5. OSSEC, CrowdSec – real-time monitoring, do not examine historic/log access patterns

6. AI/ML Detection (Meyer 2008) – requires non-attack baseline

7. Rank Analysis (Zang 2008) – requires good pre-filtering

8. Large Organizations (Yen 2013) – we focus on small organizations

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

## Slide 10

### Recent Approaches & Limitations

AI/ML Detection (Meyer 2008) – requires non-attack baseline Rank Analysis (Zang 2008) – requires good pre-filtering Large Organizations (Yen 2013) – we focus on small organizations

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

## Slide 11

#### GoAccess log analysis

Statistical tools just tell us – yes – you have a lot of traffic, and it varies by day.

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

## Slide 12

### Methods

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

## Slide 13

### Question:

How can we distinguish human access patterns from machines?

we are a knowledge systems, AI and data visualization startup

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

## Slide 14

**RAMA CARL HOETZLEIN PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS** #BHUSA @BlackHatEvents

## Slide 15

**RAMA CARL HOETZLEIN PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS** #BHUSA @BlackHatEvents

## Slide 16

### Does it _sound_ mechanical?

**RAMA CARL HOETZLEIN PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

#BHUSA @BlackHatEvents

## Slide 17

### Investigation

Time

Host IP

_From:_ Jungkee Kim, Web Server Log Visualization, Intl. Journal of Advance Smart Convergence, 2018

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

## Slide 18

### Investigation

Time

Host IP

_From:_ Jungkee Kim, Web Server Log Visualization, Intl. Journal of Advance Smart Convergence, 2018

Time (Days)

Benefits of Visualization:

- Entire log in one snapshot

- Everything is there, no statistical summary

• Easy for humans to see patterns

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

## Slide 19

Time (Days)

**RAMA CARL HOETZLEIN PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

#BHUSA @BlackHatEvents

## Slide 20

Time (Days)

What do you think is human here? **RAMA CARL HOETZLEIN PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

#BHUSA @BlackHatEvents

## Slide 21

Time (Days)

Probably not human **RAMA CARL HOETZLEIN PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
piSek hat
wo ppecemsomaBtatded ath ie! i
o . . . 2 TES See ayegee fee com enmew be 'peeem ees 6 Oe 8 oc , Bh eee cee mmm 8 Lo tpeem ene emcee sre ctes nematic sates ooo
te
.
a a
.
« ¢e
ee eee
.
Pee Seegee
tt
200 emacs same am, “es 0
jooge?
i”
.
3 4
Time (Days)
s)
)
8
Probably not human
14
15
=
pea nine? me on Ne: gatmemene  Ezecesm 3°, sae RLV TS geet et
borer cee THE esas REO Syste me Sh SS PMT Shee eames ae ou ae cue eres came ms cog re eg tat ywee ms os “=” 2. tee
16
#BHUSA @BlackHatEvents
```

## Slide 22

### Methods

We are interested in distinguishing mechanical access patterns regardless of whether they are benign or malicious.

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

## Slide 23

### Methods

Throttling: How fast are you? Block based on frequency of visit. e.g. no more than 20 pages/minute

We found that most traffic was observing rate limits.

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

## Slide 24

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

##### Throttle limited IPs Reduced traffic by only 33%

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

## Slide 25

### Methods

### What are other patterns that humans would follow?

1. Throttling

- How fast are you?

_Human_ <20 page/min

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

## Slide 26

### Methods

### What are other patterns that humans would follow?

_Human_

1. Throttling - How fast are you?

2. Consecutive - How often do you visit?

- <20 page/min <5 days consec.

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

## Slide 27

### Methods

### What are other patterns that humans would follow?

_Human_

1. Throttling - How fast are you?

2. Consecutive - How often do you visit?

3. Daily Range  - How long can you work?

<20 page/min <5 days consec. <6 hours/day

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

## Slide 28

### Methods

### What are other patterns that humans would follow?

_Human_

<20 page/min <5 days consec. <6 hours/day

1. Throttling - How fast are you?

2. Consecutive - How often do you visit?

3. Daily Range  - How long can you work?

4. Daily Hits      - How much do you look at?            <100 hits/day

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

## Slide 29

### Methods

### What are other patterns that humans would follow?

_Human_

<20 page/min <5 days consec. <6 hours/day

1. Throttling - How fast are you?

2. Consecutive - How often do you visit?

3. Daily Range  - How long can you work? 4. Daily Hits      - How much do you look at?            <100 hits/day

Behavioral Science in Human-Computer Interaction

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

## Slide 30

### Methods

**LOGRIP** Let’s use Human Behavioral Metrics to develop a…

Scoring Algorithm:

1. IP Hashing - key-value map of IPs from raw pages

2. Sort page hits by day & time

3. Apply behavioral metrics

4. Score based on a weighted contribution of metrics

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

## Slide 31

### Intermediate Results

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

## Slide 32

#### **Original Traffic**

**RAMA CARL HOETZLEIN PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS** #BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pisek hat
a
"woof 8 8 8 ee ceetm teste com enmece fy epemm erat es oe ee PC a ea 2 Nope cae cape omen eng cates sgt so cevecmemmame gees 8 ete ee 8) et
mane 2° pm ewne 2 = om tees s on me eromenpenrrme o— - ° i 200 pm eo came page
te . - a . re wet cect come
oo le covematne 0, © pemmaceneas we cece oe ew el “lee w* ppromrematttht iatbie’ Sites BEA k we, oF we ebere mm compe
. Aaah err : i
cede 0 cee we mwebe cee ces cece od wee ove oo cee) ote. o Slee coe .
decd 00 00 ego pee o® oP csc %eameccguah snp
© Beta und “Bells Meinate afte
oo, ee
:
aero dn 8 OK eee er Fee
Tr alae oD mete fF oe we 2% © 8 ote co NEWS, or cry Vee mmee ee PRETO SUR AMEQe He BF OOO cote Semele POPE Set Ce UY? Oe ag OF FP eo ath Vera 2 Mle fo Rqetmtetiealfahans sess 6 foe
Original Traffic
PROTECTING SMALL ORGANIZATIONS IN THE ERA OF Al BOTS #BHUSA @BlackHatEvents
RAMA CARL HOETZLEIN
```

## Slide 33

**RAMA CARL HOETZLEIN PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

#BHUSA @BlackHatEvents

#### **Blocked by Consecutive Days /w Daily Range**

## Slide 34

**Blocked by Daily Range with Freq RAMA CARL HOETZLEIN PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bite hat
bathe ov 34
ore .
BRIEFINGS
. .
aoe
. cmany
ee
-
oe 6
«owe
.
eels .
. Joe
-
epee oo
CRS (MOREL S copenre (
© eee e coe
eles
. a
.
Ce ee
28 on
. 8
0 @ ococe comoe
Os 0d cocemce Ce a
oe ote
° Cn
-—s —_
RAMA CARL HOETZLEIN
ss ar. Foun
5
. 4
*.
‘ «
.
eet hee .
. !
je NP fe Tasos -
Ea t= sesnon
ccm Neccn oe OF « ooteCCHC
Lens ouse-ssemte 4 cance adcuceer ces
6050 ea
ee
|
© domme
+e oof
decd coe god
onge 9
+ neg ere ae
y CKOME e | woeleacooide apace: @ C8 ems commen « (o @mer Cot ance
.
Blocked by Daily Range with Freq
PROTECTING SMALL ORGANIZATIONS IN THE ERA OF Al BOTS
"ee .
one .
.
.
croc
Aaiooe @Oe COOK |
#BHUSA
20] cm om oyomme
, °
* © coop
eum chmege oo
@BlackHatEvents
```

## Slide 35

**RAMA CARL HOETZLEIN PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

#BHUSA @BlackHatEvents

#### **Blocked by Daily Maximum**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pisekchat ¥:
BRI EFINGS
ae . tte . . - . oe et dae ttle es - oe . . oak Ton om semece om: eee wn comem ome epeee
. . a - cole scocmage 4, © pame zemeusece! cm oececgom |e a . ee tama |S 0 eee? Cgcew ee ROMs Rie ren he: ce we eb ere lee wonzeee
. .
. .
ee meee com eC cate eee Weg ete wee eI. eee ue He eM awe cae Cua WG came eels ce
og toate ree 0 slagudecen ay PP ee we —k age sepee|g, © snscemence ga eee gas
Com cles oe . gree r eT ea ees oes amr oe . .
Blocked by Daily Maximum
RAMA CARL HOETZLEIN PROTECTING SMALL ORGANIZATIONS IN THE ERA OF Al BOTS #BHUSA @BlackHatEvents
```

## Slide 36

#### **Cumulative Filtered Results**

**RAMA CARL HOETZLEIN PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS** #BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bi§ekchat
BRIEFINGS Ss
.
.
- meso ede cemcee 6 ts spe e cme
.
. .
. —
.
.* See
we
. o
ee, . CO. et Dot a
access ome 4 00
.
’ .
-
. .
4
-“ ¥ . we - ' eos . oe «|e . . . oo. bw eo otek cece ago gee oe? af ese tommmercqumh mum ose 5 | mp eetenfede
° ‘
-_ a
J Fe Ei ee pee & we eee epee neetente wee: Lee eae rene ee ee meee eres a ne meme ges cmt eens pee meme pe Saree
tomes oniags, | o ewene “tote tortonta wit . wm’. 9," , toon a woes. 2 = 3 a.) a ts en nti STE © eecceses: . Secon sete eee 1s
— a coe deems -_ MW ry joe amen oases ool 2 cone coamen aempn comes . = oe _—
Cumulative Filtered Results
RAMA CARL HOETZLEIN PROTECTING SMALL ORGANIZATIONS IN THE ERA OF Al BOTS #BHUSA @BlackHatEvents
```

## Slide 37

#### **Original Traffic**

**RAMA CARL HOETZLEIN PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS** #BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pisek hat
a
"woof 8 8 8 ee ceetm teste com enmece fy epemm erat es oe ee PC a ea 2 Nope cae cape omen eng cates sgt so cevecmemmame gees 8 ete ee 8) et
mane 2° pm ewne 2 = om tees s on me eromenpenrrme o— - ° i 200 pm eo came page
te . - a . re wet cect come
oo le covematne 0, © pemmaceneas we cece oe ew el “lee w* ppromrematttht iatbie’ Sites BEA k we, oF we ebere mm compe
. Aaah err : i
cede 0 cee we mwebe cee ces cece od wee ove oo cee) ote. o Slee coe .
decd 00 00 ego pee o® oP csc %eameccguah snp
© Beta und “Bells Meinate afte
oo, ee
:
aero dn 8 OK eee er Fee
Tr alae oD mete fF oe we 2% © 8 ote co NEWS, or cry Vee mmee ee PRETO SUR AMEQe He BF OOO cote Semele POPE Set Ce UY? Oe ag OF FP eo ath Vera 2 Mle fo Rqetmtetiealfahans sess 6 foe
Original Traffic
PROTECTING SMALL ORGANIZATIONS IN THE ERA OF Al BOTS #BHUSA @BlackHatEvents
RAMA CARL HOETZLEIN
```

## Slide 38

#### **Cumulative Filtered Results**

**RAMA CARL HOETZLEIN PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS** #BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bi§ekchat
BRIEFINGS Ss
.
.
- meso ede cemcee 6 ts spe e cme
.
. .
. —
.
.* See
we
. o
ee, . CO. et Dot a
access ome 4 00
.
’ .
-
. .
4
-“ ¥ . we - ' eos . oe «|e . . . oo. bw eo otek cece ago gee oe? af ese tommmercqumh mum ose 5 | mp eetenfede
° ‘
-_ a
J Fe Ei ee pee & we eee epee neetente wee: Lee eae rene ee ee meee eres a ne meme ges cmt eens pee meme pe Saree
tomes oniags, | o ewene “tote tortonta wit . wm’. 9," , toon a woes. 2 = 3 a.) a ts en nti STE © eecceses: . Secon sete eee 1s
— a coe deems -_ MW ry joe amen oases ool 2 cone coamen aempn comes . = oe _—
Cumulative Filtered Results
RAMA CARL HOETZLEIN PROTECTING SMALL ORGANIZATIONS IN THE ERA OF Al BOTS #BHUSA @BlackHatEvents
```

## Slide 39

**Cumulative Filtered Results**

**RAMA CARL HOETZLEIN PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS** #BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pisek hat
BRIEFINGS st
+
. -
° .
. .
° vee ange
.
.* See
“
ee, . CO. et Dot a
access ome 4 00
.
’ .
. .
.
eels { . BY
wees - ——.
” Fs
.
.
2° ‘
-_
ee Sim ne pee wh cee ere ones wee
> ome omens * 5 Beta tand “teks ofedoata whto
— - cone
=. ote
= .
.
Cumulative Filtered Results
RAMA CARL HOETZLEIN PROTECTING SMALL ORGANIZATIONS IN THE ERA OF Al BOTS #BHUSA @BlackHatEvents
```

## Slide 40

**RAMA CARL HOETZLEIN PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS** #BHUSA @BlackHatEvents

## Slide 41

**RAMA CARL HOETZLEIN PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS** #BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bi§ekchat
BRIEFINGS
*.
comes pw cece cco
se sect soe ory
es ~~. a PEBPP ALU 0 eS
ot :
ERS
* - ome ome womee
RAMA CARL HOETZLEIN . IZATIONS IN THE ERA OF Al BOTS #BHUSA @BlackHatEvents
```

## Slide 42

Single IP

### Multiple IPs

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bi§ekchat
BRIEFINGS
se sack cee ory
“tee semen Single IP
ERS
Pele, Multiple IPs
RAMA CARL HOETZLEIN . IIZATIONS IN THE ERA OF Al BOTS #BHUSA @BlackHatEvents
```

## Slide 43

**RAMA CARL HOETZLEIN**

Group of machines within the same Class C subnet requesting multiple pages around the same time.

|**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**|
|---|

#BHUSA @BlackHatEvents

## Slide 44

### Subnet Hashing

Aggregate all page hits across a subnet and _then_ perform scoring metrics.

IP

..
40.77.167.5
40.77.167.4
40.77.167.3
40.77.167.2
40.77.167.1
40.77.167.0
40.77.166.255
40.77.166.254
..

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

## Slide 45

### Subnet Hashing

Aggregate all page hits across a subnet
and  then  perform scoring metrics.
..
40.77.167.5
40.77.167.4
40.77.167.3
IP 40.77.167.2
40.77.167.1
40.77.167.0
40.77.166.255
40.77.166.254
score
..

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

## Slide 46

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

Hierarchical IP Hashing with Metric Scoring

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

## Slide 47

### Final Results

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

## Slide 48

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS** #BHUSA @BlackHatEvents

**RAMA CARL HOETZLEIN**

**Filtered Result – Prior to Subnet Hashing**

## Slide 49

**RAMA CARL HOETZLEIN PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

#BHUSA @BlackHatEvents

#### **Blocking Class C Subnets**

## Slide 50

**RAMA CARL HOETZLEIN PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

#BHUSA @BlackHatEvents

#### **Blocking Class B Subnets**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
X
pif hat
we \
. N
BRIEFINGS LOS . :
- tow chow oe |, te teh we. cower on, ee
-
00 comme eam @ [
. e
: 4
. <
: “
. .
aoa cgiatmm) , geeety |e | vereceles nage vce] 2 we ase corer, ae =e oe °. a tee fee |= ee toy coms |" cowremed, “ * . a] - wrangle 20 0g
Blocking Class B Subnets
RAMA CARL HOETZLEIN PROTECTING SMALL ORGANIZATIONS IN THE ERA OF Al BOTS #BHUSA @BlackHatEvents
```

## Slide 51

#BHUSA @BlackHatEvents

#### **Final Result**

**RAMA CARL HOETZLEIN PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

## Slide 52

**Original Traffic Final Result**

**RAMA CARL HOETZLEIN PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

#BHUSA @BlackHatEvents

## Slide 53

Estimated Load Analysis

Original C Filtering B Filtering Final Server Load

**RAMA CARL HOETZLEIN PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

#BHUSA @BlackHatEvents

## Slide 54

### Results

## 94% reduction in traffic

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

## Slide 55

### Results

## 94% reduction in traffic

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

## Slide 56

**Original Traffic Final Result**

**RAMA CARL HOETZLEIN PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

#BHUSA @BlackHatEvents

## Slide 57

### Protecting Small Organizations

We found that - even when well behaved and observing rate limits - the sheer volume of AI bot requests can overwhelm the servers of small organizations.

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

## Slide 58

### Protecting Small Organizations

Policy

“Our water quality data is available to the public for free. We prefer to have a human-in-theloop, and discourage AI crawlers so that our servers remain responsive to our human users.”

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

## Slide 59

### Protecting Small Organizations

Grants for non-profits and small orgs often depend on viewership statistics for new or renewed funding.

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

## Slide 60

### Protecting Small Organizations

Grants for non-profits and small orgs often depend on viewership statistics for new or renewed funding.

**LOGRIP** provides an upper bound on real human views, with blocked/permitted stats per day, at least better than raw traffic stats.

Date All Blocked Allowed Reduction 7/16/2025 11359 10807 552 95.1% 7/17/2025 13476 12965 512 96.2%

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

## Slide 61

### Conclusions

• Understand the extent of AI crawler & bot activity • Defend small organizations (single machines) from large organizations (many machines in data centers)!

• Be able to specify defense policy

• Know (to the extent possible) the implications of those policies

- Do all of this easily, cheaply and open source

### **LOGRIP**

A simple, lightweight, open source tool for generating blocklists _and_ policy visualizations based on access logs.

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

## Slide 62

### New Tool

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

## Slide 63

### Running LOGRIP

Features:

<u>https://github.com/quantasci/logrip</u>

• Open source

• Cmd line based

**Input:** access log config file (log format, policy)

• Read any log format

**Output:** blocklist B-subnet list C-subnet list full IP list policy visualizations load estimation

**RAMA CARL HOETZLEIN**

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

• Config policy settings

• Fast. 150k log in 10 sec

#BHUSA @BlackHatEvents

## Slide 64

LOGRIP
All Output Products

**RAMA CARL HOETZLEIN PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
black hat
BRIEFINGS
” Observed Traffic Blocking Actions (Policy) : . mated Server Page Hits by IP
fore & After) —
1 /bmi/monitoringregions/4
1 /events/2731
57.141.7.16
1/
57.141.7.17
1/
1 /bmi_events/62
1 /events/2424
1 /events/835
1 /groundwater_queries?page=320
1 /groundwater_queries?page=432
§7.141.7.18
1/
1 /bmi_events/152
1 /events/2286
1 /queries/new?q%S5Bs%5D=date+asc
57.141.7.19
1 /bmi_events/167
1 /events/1100
1 /events/2332
1 /events/2863
1 /queries/new?q%5Bs%5D=analyte_nametdesc
1 /queries/new?q%SBs%5D=event_flowtasc
1 /queries?page=978&q%5Bs%5D=event_flow+asc
: ————— —y e-em rpegnen une irae deere marco ro
. f iden page cunig.¢ unig veapse mace mumsrmintinin’ Metrics by IP wer :  Metri B-Subni
Filtered Traffic 5 196.111.210 to 4 y E letrics by B-Subnet 1 /events/1778
jatsi.2te216 10 8 4&0 fowaautmogonaspe ‘zona oon! 1a! sama ca
| 4.227.36.31 422 1.168 4.658 422 1.168 4.658 /bmi/monitoringlocations/629} “a 14.89167 0.007656 14.89167 0.007656] 1 /events/1912
4.227.36.50 41 0.026 20.51 41 (0.026 20.51 /queries/?page=58ql: 5 . ° ° ° | 1 /groundwater_queries?page=322
|4.227.36.122 1 6 0.003 25 6 0.003 25 /queries/new?q%SBs%SD> o o o of r
5.100.173.71 1129 0008 11129 0.009 fevens/08s ss Lseozre oon 12 estas ous 1 /monitoringtocations/530
5.181.190.248 114.89 0.008 10 14.89 0.008 / er suaaea} 2ereasso) 1074 1 /monitoringlocations/8
° oo
8.48,71.250 Imonitoringsets/7 P ns comin coe .
e.211.42.174 Idns-query?das=pHKBAMABAAM) 35 146 +» ao 1|/monitoringsets/25
°
'17.241.75.55 Jevents/842 2459.4." 1 /queries?page=997&q%5Bs%5D=event_flowtasc
17.241.75.92 Isites/117 27.180.*.* -
417.241.785.108 Jevents/499 suis. 1 /sites/158
137.241.786.110 Jevents/34a pan 57.141.7.21
17.241.75.127 Jevents/1519 haa z
172412199 fevents/1969 or "| ea cree 1/fevents/259
17.241.219.12 Ihab_events/701 lease.» ° 1 /events/2747
37.241.210.24
Jevents/120 42.179.
17.241.219.44 1 /queries/new?q%5Bs%5D=monitoringlocation_name+asc
ee 1 /queries?page=6&q%5Bs%5D=event_flowtasc
137.241.210.114
17.241.219.145 1/sitemap
137.241.219.172
417.241.219.182
17.241.297.19
17.241.227.65
317.241.297.124
317.241.297.154
: 417.241.297.167
17.241.227.296 1
18.97.9.169 178 2.738 Thab_events/92
“ . + 920.49.136.28 1 o ‘{monitoringsets/7_
All Output Products fos ax ne
0] 57-141.7.20
0.00027
8
°
°
°
°
°
Imonitoringlocations/382 ff 44.220.*.»
Thab_events/688 5.20.0."
Thab_events/655
Imonitoringlocations/512
Imonitoringlocations/685
Thab_events/169
fevents/1662
Jevents/3107
Thab_events/667
‘Imonitoringlocations/562
Jevents/2872
Jevents/2572
oo d
16:17667 0.199674 16.17067 0.199874 57,141,722
1561089 0.208102 15.6108 0.206103 - -
4.940833 0.00638 4.940833 0.00636] 1 /bmi/monitoringlocations/382
a) q 1 /events/1301
5 q 1 1 /events/2218
0.000276 1.578948 0.000278, 1.576948 1 /events/2260
1.209722 0.048382 1.20072 0.048389
° | 1 /events/2467
1 /events/37
q
q
4 1 /monitoringlocations/684
q
q
ttle a lel Be le ele os
wt 24.59.56.143 0 Imonitoringlocations/s04 J Ste
] 27.150.86.197 o Iqueries/new2q%5Bs%5D=anall 6s 279 +»
31,13.224.222 0
1 /queries/new?q%5Bs%5D=analyte_nametasc
1 /queries/new?q%5Bs%5D=event_flowtasc
1.903056 0.028651 7 0.026651
° °
RAMA CARL HOETZLEIN #BHUSA @BlackHatEvents
Lenw 524.4.
```

## Slide 65

#### **Filtered Result**

### Limitations

Cannot stop DDoS attacks

- acquire random IPs

Many AI crawlers still present

- well disguised, more random

randomized, infrequent

At this point - Human vs. Machine becomes harder to distinguish

DDoS

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

## Slide 66

### Future Goals

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

## Slide 67

### Future Goals

## • Now in use. Measure post-blocking activity with client.

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

## Slide 68

### Future Goals

• Now in use. Measure post-blocking activity with client.

- Ground truth data for human and non-human activity (both are difficult to replicate!)

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

## Slide 69

### Future Goals

• Now in use. Measure post-blocking activity with client.

• Ground truth data for human and non-human activity (both are difficult to replicate!)

• Study policy parameter sensitivity and/or optimize

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

## Slide 70

<u>https://github.com/quantasci</u> we are a knowledge systems, AI and data visualization startup

### LOGRIP

<u>https://github.com/quantasci/logrip</u> Open source, Apache 2.0 license

arXiv

<u>https://arxiv.org/abs/2508.03130</u>

<u>https://ramakarl.com/</u>

rama karl hoetzlein

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

## Slide 71

### Thank you!

#### Rama Karl Hoetzlein

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

## Slide 72

**RAMA CARL HOETZLEIN PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS** #BHUSA @BlackHatEvents
