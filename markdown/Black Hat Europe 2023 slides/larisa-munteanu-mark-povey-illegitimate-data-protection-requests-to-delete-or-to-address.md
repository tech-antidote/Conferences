---
title: "Illegitimate Data Protection Requests - To Delete or to Address"
speakers: ["Larisa Munteanu", "Mark Povey"]
conference: "Black Hat"
conference_full: "Black Hat Europe 2023"
edition: "Europe"
year: 2023
source_pdf: "Black Hat Europe 2023 slides/Larisa Munteanu, Mark Povey_Illegitimate Data Protection Requests - To Delete or to Address.pdf"
pages: 17
sha256: "a3f2e5a95752ba61398c300a50d1397d68ddd2160a426a8c1b3bb6d29844214d"
text_chars: 6241
ocr_pages: 1
has_ocr: true
redacted_secrets: 0
ocr_confidence: 77.6
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T04:03:04Z"
---
# Illegitimate Data Protection Requests - To Delete or to Address

**Speakers:** Larisa Munteanu, Mark Povey  
**Conference:** Black Hat Europe 2023  
**Source:** `Black Hat Europe 2023 slides/Larisa Munteanu, Mark Povey_Illegitimate Data Protection Requests - To Delete or to Address.pdf` (17 pages)


## Slide 1

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 78/100 on the text kept, 70/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
DECEMBER 4-7
Ex<CEL LONDON vy UK
JSIG
#BHEU @BlackHatEvents
```

## Slide 2

## **Illegitimate Data Protection Requests: To Delete or to Address?**

Delivered by:

Mark Povey: Technical Director and Chief DPO at JS Information Governance Ltd Larisa Munteanu: Data Protection Lawyer/DPO at JS Information Governance Ltd, PhD Researcher at Erasmus School of Law (Erasmus University Rotterdam)

#BHEU @BlackHatEvents

## Slide 3

### Privacy – where is the new oil?

#### Data as the key element

#### Relevance

- European Parliament  (2020) – “while oil is obviously a finite and non-reusable resource, data can be infinite and reused – with account taken of ownership and access rights”

- Evolution in the way individuals (even perpetrators) acknowledge the value of personal data

- Digitalisation and subsequently, cyber-crimes

- Legal requirements imposed on both public and private sector

Source: Is data the new oil? (europa.eu)

#BHEU @BlackHatEvents

Information Classification: General

## Slide 4

International and
Regional
Legal Obligations

National Legal
Obligations

GDPR
References

- Convention 108 GDPR

- • NIS 2 Directive

•
Data Protection Act
2018

- Computer Misuse Act 1990 (UK)

- • BSI Act (Germany)

- • Organic Law 3/2018 (Spain)…

- Art. 5 (1) f) – integrity and confidentiality

- Art. 5 (2) – accountability of the General Data Protection Regulation

#BHEU @BlackHatEvents

Information Classification: General

## Slide 5

Operational  Operational  Operational
Measures Measures Measures
• Friend or FOI? • Access restrictions  • Encryption at rest
– “least privilege”  and in transit
principle • Validate ID
• Incident response  • Prior verifications
and disaster
recovery plans

#BHEU @BlackHatEvents

Information Classification: General

## Slide 6

Organisational  Organisational  Organisational
Measures Measures Measures
• Clear roles and  • Solid framework  • Training and
awareness
responsibilities  supporting data
throughout the  security with
organisation policies and
procedures
• ISO standard?

#BHEU @BlackHatEvents

Information Classification: General

## Slide 7

### Data Protection by Design and by Default – Art. 25 GDPR

#### DP by Design

#### DP by Default

- must take into account risks and severity for “rights and freedoms of natural persons posed by the processing (…) **<u>both at the time of the determination of the means for processing and at the time of the processing itself</u>** ”

- must “implement appropriate technical and organizational measures for ensuring that, **<u>by default</u>** only personal data which are necessary for each specific purpose of the processing are processed”

#BHEU @BlackHatEvents

Information Classification: General

## Slide 8

### BlackHat USA 2019

**James Pavur - “GDPArrrrr: Using Privacy Laws to Steal Identities” (2019)** Apparently valid requests, yet a legal omission Knowledge limitations and operational constraints

Manifestly unfounded/excessive:

_“These reasons relate to malicious intent on the part of the sender but do not discuss the possibility of fraud directly - focusing instead on the abuse of GDPR requests to waste organizational resources”_

Source: https://doi.org/10.48550/arXiv.1912.00731

#BHEU @BlackHatEvents

Information Classification: General

## Slide 9

### Malware attack

- Data Subject Access Requests (DSARs) accompanied by a malware attack – you may get tricked by the name of the file

- The file extension is relevant too – although there are no legal restrictions on the format for such requests, you will definitely not receive it as an executable file

#BHEU @BlackHatEvents

Information Classification: General

## Slide 10

### Malware attack

- The person will try to smoothly insist on you opening the file before the communication chain continues

- As presented before, companies will tend to feel overwhelmed by the context and rush into “proceeding” with the request, out of panic

#BHEU @BlackHatEvents

Information Classification: General

## Slide 11

### Malware attack

- Innovation is one of the premises here, so expect the unexpected

- What about pdfs and docs? It can be a hyperlink, multimedia

- Obfuscated text that can be skipped by inspection techniques (it can even be a hidden pdf within the main pdf)

#BHEU @BlackHatEvents

Information Classification: General

## Slide 12

### Vulnerabilities

1. Shared email for privacy matters

- The Data Protection Officer is the privacy guardian of the organisation

- The Data Protection Officer email should belong to… the Data Protection Officer (Privacy Team?)

- How can access controls prevent data breaches via email?

- Is budget a solid constraint for this?

#BHEU @BlackHatEvents

Information Classification: General

## Slide 13

### Vulnerabilities

2. Lack of/inadequate training

- Why would training matter?

- How can training be more appealing or dynamic?

- Is budget a solid constraint for this?

#BHEU @BlackHatEvents

Information Classification: General

## Slide 14

### Vulnerabilities

3. Policies and procedures that are not supported with corresponding operational measures

- A successful compliance program relies on both theory and practice

- Adequate and appropriate implementation is the key

- How to create a real “human firewall” and protect information assets?

- Is budget a solid constraint for this?

#BHEU @BlackHatEvents

Information Classification: General

## Slide 15

### Solutions in 2023

#### Technology vs Technology

#### Rationale vs Impulse

- What types of software should organisations check? (e.g. antivirus, …….)

- What are the main criteria to be used? (e.g. error rate, price?)

- How significant of a problem is it if your budget is extremely limited or you are a start-up?

- It is wiser to spend money on security and compliance packages instead of fines.

- Reputational damage cannot be restored with money (and this triggers “leadership” awareness).

- • Bigger picture?

#BHEU @BlackHatEvents

Information Classification: General

## Slide 16

Takeaway 1
An apparently valid
data protection
request is not
always legitimate.
Often, they are
used to attack .

Takeaway 2
Training and
company culture
are equally
important to policies
and procedures
when it comes to
cyber-attacks.

Takeaway 3
Technology can be
used against
technology.

#BHEU @BlackHatEvents

Information Classification: General

## Slide 17

# Q&A

#BHEU @BlackHatEvents

Information Classification: General
