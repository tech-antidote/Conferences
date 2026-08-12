---
title: "Unmasking APTs An Automated Approach for Real-World Threat Attribution"
speakers: ["Aakanksha Saha"]
conference: "Black Hat"
conference_full: "Black Hat Europe 2023"
edition: "Europe"
year: 2023
source_pdf: "Black Hat Europe 2023 slides/Aakanksha Saha_Unmasking APTs An Automated Approach for Real-World Threat Attribution.pdf"
pages: 42
sha256: "8cc141a4b19cac2a25ee40de8a00f5a39618bf6c5214a608ddd883786565081c"
text_chars: 11753
ocr_pages: 12
has_ocr: true
redacted_secrets: 0
ocr_confidence: 85.5
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T03:59:20Z"
---
# Unmasking APTs An Automated Approach for Real-World Threat Attribution

**Speakers:** Aakanksha Saha  
**Conference:** Black Hat Europe 2023  
**Source:** `Black Hat Europe 2023 slides/Aakanksha Saha_Unmasking APTs An Automated Approach for Real-World Threat Attribution.pdf` (42 pages)


## Slide 1

**Unmasking APTs: An Automated Approach for Real-World Threat Attribution**

_Aakanksha Saha, Jorge Blasco, Lorenzo Cavallaro, Martina Lindorfer_

## Slide 2

Researcher at TU Wien Masters from University of Utah Previously: Red Teamer @ MSFT Passionate about ML and security Enjoy Stargazing

2

## Slide 3

# **Roadmap**

Attribution
Insights and
challenges
ADAPT system  Conclusion
design
APT and its
attribution
Evaluation

3

## Slide 4

4

Sophisticated attacks Experienced teams against specific targets of cybercriminals


> Recovered by OCR — confidence 96/100 on the text kept, 96/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Russia-backed hackers target German
legislators: report
Farah Bahgat
03/26/2021
A"Ghostwriter" cyberattack affected seven Bundestag members and 31 state parliamentarians,
according to a Spiegel report. The hackers reportedly launch campaigns that "align" with Russian
interests.
Sophisticated attacks Experienced teams
against specific targets of cybercriminals
```

## Slide 5

## **What is (AP)threat attribution?**

Associate  a cyber-attack to an attacker

Analysts link the activity to a known threat actor/group

5

## Slide 6

## Slide 7

## Slide 8

# **Attribution is challenging!**

8

## Slide 9

## **Campaign variation**

Threat Campaign X

Operated by
Threat Group 1
foobar.evil.com:445

- Threat Campaign Y

- • Incomplete understanding of adversary with vendors tracking groups from varied campaign perspectives [AT&T AlienLabs, 2021]

9

## Slide 10

## **Shared similarity**

Operated by
Threat Group 1
foobar.evil.com:445
Operated by
Threat Group 2
xyzzy.bad.com:676

- Adoption of shared similarities, false flags and collaboration between subgroups results in inconsistent and erroneous attribution [Mandiant, 2023]

10

## Slide 11

## **Heterogeneous files in attack chain**

Threat Campaign X

Operated by

Threat Group 1 foobar.evil.com:445

• Manual analysis of heterogenous files to identify the threat group [Mandiant, 2022]

11

## Slide 12

## **Putting it all together**

### **Threat Campaign X**

Operated by

**Threat Group**

### **Multiple file types**

12

## Slide 13

**Approach ADAPT Attribution of Diverse APT Samples**

**Campaign Attribution**

Identify characteristics of attack + Prioritization of detection and mitigation

**Group Attribution** Identify characteristics of attacker + Aid forensic investigation and indictments

13

## Slide 14

## **ADAPT system design**

14

## Slide 15

### Dataset Collection

### Feature Extraction

### Feature Clustering Transformation

15

## Slide 16

## **APT dataset**

- 6,455 samples

- 22+ file types

- 172 APT groups

16


> Recovered by OCR — confidence 81/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
APT dataset
> | VIRUSTOTAL
* 6,455 samples
* 22+ file types
* 172 APT groups
16
```

## Slide 17

## **Dataset quality: Filetype**

17


> Recovered by OCR — confidence 84/100 on the text kept, 39/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Filetype
Dataset quality
2,500 4
2,000 ~
17
umouyun
T T
° °
VTfileType
```

## Slide 18

## **Dataset quality: Filetype**

18

## Slide 19

**Dataset quality:  Group label** 2,260 (35.01%) have more than 1 label

19


> Recovered by OCR — confidence 94/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Dataset quality: Group label
2,260 (35.01%) have more than 1 label
Previous
name
ACTINIUM
AMERICIUM
BARIUM
BISMUTH
BOHRIUM
BROMINE
CERIUM
CHROMIUM
COPERNICIUM
CURIUM
New name
Aqua Blizzard
Pink Sandstorm
Brass Typhoon
Canvas Cyclone
Smoke Sandstorm
Ghost Blizzard
Ruby Sleet
Spandex Tempest
Charcoal Typhoon
Sapphire Sleet
Crimson
Sandstorm
Origin/Threat
Russia
Iran
China
Vietnam
Iran
Russia
North Korea
Financially motivated
China
North Korea
Iran
Other names
UNC530, Primitive Bear, Gamaredon
Agrius, Deadwood, BlackShadow,
SharpBoys
APT41
APT32, OceanLotus
Energetic Bear, Crouching Yeti
ControlX
Genie Spider, BlueNoroff
TA456, Tortoise Shell
19
```

## Slide 20

## **Dataset (re)-labeling**

- Standardize aliases

- Consistent naming convention

- Non-unique names and non-APT samples

6,134 samples assigned to 92 groups

_* The standardized group-labeled dataset is available at https://anonymous.4open.science/r/ADAPT-41F7/_

20

## Slide 21

## **Feature extraction**

Static analysis to extract features from heterogeneous files*

21

## Slide 22

## **Feature categories and attribution tasks**

Generic Generic
Specific
Linking
Campaign Attribution Group Attribution

22

## Slide 23

## **Linking attributes**

23


> Recovered by OCR — confidence 72/100 on the text kept, 60/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
{'URL': ['https://sapp-f347f.firebaseio.com'],
Linking attributes
"FilePath_2': ['/res/color/abc_hint_foreground_material_dark aut nomous_system : {
*/res/drawable/abc_seekbar_tick_mark_material.xml', bgp_p refix": 57.90.0. 0/16 ’
*/res/layout/notification_template_custom_big.xml', u a sn" : 24940 ,
*/res/layout/notification_template_icon_group.xml', "desc ription t "HETZNER-AS
*md5': ['@0@ddbb75d10a939b54a7ceea5f12563', count ry_code . DE
‘Ethereum': [], "subdomains": [
‘aSnoniveeekey". [] ssuer_d "C=CN, ST=ZJ, L=HZ, O=Internet Widgits Pty Ltd",
"SSHECprivatekey': [], “issuer_organization": [
"PGPprivatekeyblock': [], "Internet Widgits Pty Ltd"
‘GitHub’: [],
"GenericAPIKey': [],
"GoogleAPIKey': ['AIzaSyDjITMkuXq8V@cUt1PNGydH3uQ3GebImB8'], 23
```

## Slide 24

## **Feature transformation**

- Normalization

- One-hot encoding

   - EXE:ResourceLanguage = DOCX:LanguageCode = “Language”

- String vectorization

- Word embedding

- PDF:Author = XML:Creator = “Author”

24

## Slide 25

## **Feature transformation**

- Normalization

- One-hot encoding

- String vectorization

- Word embedding

25


> Recovered by OCR — confidence 76/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Feature transformation
One-hot encoding
“hash": "4%
"MSVC_2017_linke
“MSVC_2017_rich"
“KeyloggerApi":
"SpecialKeyNames": + A
“DownloadUsingWinHttp": t
"PostHttpForm": true,
“FingerprintHardware": true,
“FingerprintEnvironment": +
"RunShell": true
25
```

## Slide 26

## **Feature transformation**

{‘AdjustTokenPrivilege’, ‘GlobalUnlock’, ‘setupx.dll’}

- Normalization {‘BITMAP’, ‘Qatev’, ‘GlobalUnlock’, ‘GetPrivateProfile’}

- One-hot encoding

   - Count Vectorizer

- String vectorization

- Word embedding

|**Adjust**
**Token**
**Privilege**|**Global**
**Unlock**|**setupx.dll**|**BITMAP**|**Qatev**|**GetPrivate**
**Profile**|
|---|---|---|---|---|---|
|1|1|1|0|0|0|
|0|1|0|1|1|1|

26

## Slide 27

## **Feature transformation**

- Normalization

api-notify3.dropbox.com api-notify5.dropbox.com api-notify.dropbox.com

- One-hot encoding

- String vectorization

- Word embedding

a071309.xsph.ru a070534.xsph.ru a069313.xsph.ru

27

## Slide 28

## **Modeling and clustering**

- Lack of standardized ground truth labels • Multiple group labels for ~35% samples

- No dataset for threat campaigns

Unsupervised Agglomerative Clustering

- **APT Campaign** attribution for executable and document files

- • **APT Group** attribution for all files

28

## Slide 29

## **Evaluation**

Evaluated the performance of ADAPT on a reference dataset from MITRE

29


> Recovered by OCR — confidence 94/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
CAMPAIGNS
Overview ID
2015 Ukraine Electric Power
Attack
c0028
2016 Ukraine Electric Power
Attack
co010
coo11
C0017
C0027
c0025
CostaRicto
Matrices
Name
2015 Ukraine
Electric Power
Attack
2016 Ukraine
Electric Power
Attack
Evaluation
ics Techniques Defenses > CTl v Resources ¥ Benefactors Blog @ Search Q
Campaigns: 24
Description
2015 Ukraine Electric Power Attack was a Sandworm Team campaign during which they used BlackEnergy
(specifically BlackEnergy3) and KillDisk to target and disrupt transmission and distribution substations within
the Ukrainian power grid. This campaign was the first major public attack conducted against the Ukrainian
power grid by Sandworm Team.
2016 Ukraine Electric Power Attack was a Sandworm Team campaign during which they used Industroyer
malware to target and disrupt distribution substations within the Ukrainian power grid. This campaign was the
second major public attack conducted against Ukraine by Sandworm Team.
C0010 was a cyber espionage campaign conducted by UNC3890 that targeted Israeli shipping, government,
aviation, energy, and healthcare organizations. Security researcher assess UNC3890 conducts operations in
support of Iranian interests, and noted several limited technical connections to Iran, including PDB strings and
Farsi language artifacts. C0010 began by at least late 2020, and was still ongoing as of mid-2022.
C0011 was a suspected cyber espionage campaign conducted by Transparent Tribe that targeted students at
universities and colleges in India. Security researchers noted this campaign against students was a significant
shift from Transparent Tribe's historic targeting Indian government, military, and think tank personnel, and
assessed it was still ongoing as of July 2022.
Evaluated the performance of ADAPT on a reference dataset from MITRE
29
```

## Slide 30

## **Evaluation: Quantitative**

Campaign

Precision : 0.91 Recall: 0.90 F1-score: 0.90

Campaign

Group

Precision: 0.98 Recall: 0.97 F1-score: 0.97

Precision: 0.84 Recall: 0.80 F1-score: 0.78

30

## Slide 31

## **Evaluation: Qualitative**

Campaigns

**Groups**

31

July  2020


> Recovered by OCR — confidence 81/100 on the text kept, 73/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Evaluation: Qualitative
ge» | National Cyber
a part of GCHQ
COVID-19 vaccine
development
ES Security Centre . | el
S
gets
July 2020
31
```

## Slide 32

32


> Recovered by OCR — confidence 86/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
JPCERT CC
JPCERT/CC Eyes
Top > List of “Malware” > Malware “WellMess” Targeting Linux and Windows
se) SAE Fw (Shusei Tomonaga) July 6, 2018
Malware “WellMess”
Targeting Linux and
Windows
32
```

## Slide 33

## **ADAPT…**

- Successfully attributes samples belonging to Wellmail and Wellmess campaigns since 2017 to the same entity

- Streamlines and automates the process of extracting and clustering key patterns such as…

33

## Slide 34

34


> Recovered by OCR — confidence 88/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
> Signatures
> Signatures
Suspect
network
TorUsage
Odd Other
network compiler
gc (gc_5_x64_elf)
gc (gc_6_x64_elf)
Odd Other
network compiler
PostHttpForm Al Golang
gc (gc_x64)
>» Check
34
```

## Slide 35

35


> Recovered by OCR — confidence 82/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
» Di crypto (12)
» Wij curve25519 (12)
cswap
freeze
invert
ladderstep
v Dj botlib (45)
BlockSize
Decrypt
Encrypt
v Dj (*KeySizeError) (1)
Error
v Dj KeySizeError (1)
Error
v Dj Send (1)
func1
AES_Decrypt
AES_Encrypt
v Dj vendor/golang_org/x/crypto/curve25519 (12)
cswap
freeze
invert
ladderstep
35
```

## Slide 36

## **What’s next?**

36

## Slide 37

# **ADAPT 2.0**

• Gain invaluable insights from real-world defenders – that's YOU! 🛡

- Explore how YOU, as analysts,  skillfully identify malicious activities and untangle complexities. 🕵

37

## Slide 38

## **Attributing APTs: Expert Insights**

Intrigued?  Learn
more about our
study here !

<u>https://secpriv.wien/adapt/</u>

38

## Slide 39

## **Key Highlights**

- Systematic attribution approach by disassociating campaign attribution and group attribution

- Considering the diverse array of file types in the evolving APT landscape is promising

- Effective knowledge exchange between academia and industry can lead to impactful research outcomes

39

## Slide 40

40


> Recovered by OCR — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
THANK YOU
HELP US
HELP YOU
UNIVERSIDAD
: POLITECNICA
Security DE MADRID
& Privacy
40
```

## Slide 41

## **State-of-the art research**

**BlackHat, 2015** Big game hunting: The peculiarities in nation-state malware research

**TrustBus, 2018 IEEE KDE,  2022** CSKG4APT: A Cybersecurity An Enhanced Cyber Attack Knowledge Graph for Attribution Framework Advanced Persistent Threat Organization Attribution

DeepAPT: Nation-State APT Attribution Using End-toEnd Deep Neural Networks

**ICANN, 2017**

A machine learning-based FinTech cyber threat attribution framework using high-level indicators of compromise **Elsevier, 2019**

41

## Slide 42

## **References**

[1] https://securityaffairs.com/116001/apt/german-parliament-bundestag-russia-hackers.html [2] https://www.mandiant.com/resources/blog/unc2452-merged-into-apt29 [3] https://www.mandiant.com/resources/blog/north-korea-cyber-structure-alignment-2023 [4] <u>https://cybersecurity.att.com/blogs/labs-research/a-global-perspective-of-the-sidewinder-apt</u> [5] https://blog.talosintelligence.com/whats-with-shared-vba-code/

[6] <u>https://machinelearningmastery.com/why-one-hot-encode-data-in-machine-learning/</u> [7] https://scikit-

<u>learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html</u> [8] https://huggingface.co/sentence-transformers [9] <u>https://scikit-</u>

<u>learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html#</u> [10] https://attack.mitre.org/campaigns/

[11] https://www.ncsc.gov.uk/files/Advisory-APT29-targets-COVID-19-vaccine-development.pdf [12] https://blogs.jpcert.or.jp/en/2018/07/malware-wellmes-9b78.html

[13] https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor- <u>naming?view=o365-worldwide</u>

- [14] <u>https://attack.mitre.org/groups/</u>

42
