---
title: "Deleting Your Domain Preventing Data Leaks at TLD Scale"
speakers: ["Maarten Wullink"]
conference: "Black Hat"
conference_full: "Black Hat Europe 2023"
edition: "Europe"
year: 2023
source_pdf: "Black Hat Europe 2023 slides/Maarten Wullink_Deleting Your Domain Preventing Data Leaks at TLD Scale.pdf"
pages: 51
sha256: "d548f9132a8488c2844676fdf856b285b9a1f74221167c9417a36e4fe7e13866"
text_chars: 9839
ocr_pages: 7
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:12:35Z"
---
# Deleting Your Domain Preventing Data Leaks at TLD Scale

**Speakers:** Maarten Wullink  
**Conference:** Black Hat Europe 2023  
**Source:** `Black Hat Europe 2023 slides/Maarten Wullink_Deleting Your Domain Preventing Data Leaks at TLD Scale.pdf` (51 pages)


## Slide 1

# **Deleting Your Domain? Preventing Data Leaks at TLD Scale**

#BHEU @BlackHatEvents

## Slide 2

## Who Are We?

Maarten Wullink Research engineer SIDN Labs

#### Moritz Müller Research engineer SIDN Labs

## Slide 3

## What to expect?

- Introduction

- Data leaks and email

- LEMMINGS System

- DNS and email

- System functionality

- Results

## Slide 4

## About SIDN

Registry for the **.nl** country code top-level domain (cctld)

- **6.3** million .nl domains

- **61%** uses DNSSEC

- Global Anycast DNS network

## Slide 5

## About SIDN Labs

#### Research arm of SIDN

   - Applied technical research into the safety and stability of the Internet

- Main research themes

      - Domain name security

      - Infrastructucture security

      - Emerging Internet technologies

## Slide 6

## Data leaks and Email

#### Normal situation

Bob
Send mail to
bob@example.nl
Alice
example.nl
Use
mail.example.nl

## Slide 7

## Data leaks and Email

#### Domain ownership change

Bob Mallory
example.nl
mail.example.nl

mail.example.nl

## Slide 8

## Data leaks and Email

After re-registration
Bob Mallory
Send mail to
bob@example.nl
Receive mail to
bob@example.nl
Alice
example.nl
Use
mail.example.nl

## Slide 9

Data leak - Example

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Data leak - Example
Major data breach at Jeugdriagg:
medical records of vulnerable children
leaked
~*~ Daniel Verlaan
Due to an error at Jeugdriagg, the files of children with often serious
psychological problems have been leaked. Despite efforts by Minister Hugo de
Jonge to better secure healthcare institutions, hardly anything seems to have
changed in a year and a half.
Just in
Anderleq
to go to
Greek tr.
ranking 2
Eloise er
with Prid
Barbie is|
director f
dollars
Lost Rot
surgery
```

## Slide 10

Data leak - Example

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Data leak - Example
f | articles ~ Community Career Topics Awards Live Whitepapers More Service
COMPUTABLE To sare fo
Home | Articles | News | Security
Police leak data via expired email domains
January 20, 2017 11:50 | Pim van der Beek 1&3
iy ii =
The police have allowed a number of domain names linked to e-mail ad-
dresses to expire. Third parties can purchase those domains and gain ac-
cess to emails containing information about arrests and event security. An
ethical hacker has demonstrated this on behalf of BNR (Business News
Radio).
That ethical hacker, Wouter Slotboom, warned the police about the security risk
two years ago and is now raising the alarm because the risk still exists. Six
months after his report, Slotboom bought a number of expired police domains.
Information such as arrest warrants and a security plan for a large Christmas
market in Dordrecht still regularly arrives on these email accounts.
```

## Slide 11

## LEMMINGS

De **L** et **E** d do **M** ain **M** a **I** l war **N** in **G S** ystem A system for detecting mail traffic involving deleted domains and alerting registrants

## Slide 12

## LEMMINGS

- Method:

   - Analyse DNS queries for all deleted domains

   - Combine with web crawler and domain abuse data

   - Alert the former registrant, when following is true

      - Indication domain is used for email

      - Domain has not yet exited quarantine period

## Slide 13

## Privacy Considerations

- Not capturing or analysing actual mail content

- No trackers in mail alert to registrants

- Removing PII data after process is completed

- Published privacy policy

## Slide 14

Domain Life Cycle
Cancel-Delete
Where is LEMMINGS?
Delete
Active
Register
Quarantine
Free
40 days
Exit
Day 1 - 30

## Slide 15

### DNS and Email

#### Delivering mail for bob@example.nl

Mail server

## Slide 16

### DNS and Email

MX? Mail server DNS Resolver

## Slide 17

### DNS and Email

MX?
Mail server DNS Resolver
MX?

. (root)

## Slide 18

### DNS and Email

. (root)
Operated by SIDN
MX?
MX?
nl.
Mail server DNS Resolver
Capture

## Slide 19

### DNS and Email

. (root)
Operated by SIDN
MX?
nl.
Mail server DNS Resolver
Capture
example.nl.
MX?

## Slide 20

### DNS and Email

. (root)
Operated by SIDN
Answer
nl.
Mail server DNS Resolver
Capture
SMTP
example.nl.
mail.example.nl.
Answer

## Slide 21

## Challenges

- Analysing large volume of DNS data

- Filtering noise (marketing, spam mail)

- Explaining the security risk to registrants

## Slide 22

## Challenges

- Try not to make the alert look like a spam message

- Registrant contact email address is not reachable

   - Privacy proxy

   - In-zone email address

## Slide 23

## Data Sources

- DNS queries for 6.3 million .nl domains

   - ~4 billion daily

   - ~180 million email related

## Slide 24

## Data Sources

- Web crawler data

   - 6.3 million .nl domains

   - Attributes

      - Web content-type

      - Detected email addresses

- Abuse feeds (Spamhaus, APWG)

- Sinkhole (botnet C&C domains)

## Slide 25

## Data Sources

#### Domain registration database

Registrations (light blue) and deletes (dark blue)

https://stats.sidnlabs.nl

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Data Sources
Domain registration database
Registrations and deletes O®
1998 2000 2002 2004 2006 2008 2010 2012 2014 2016 2018 2020 2022
Registrations (light blue) and deletes (dark blue)
https://stats.sidnlabs.nl
```

## Slide 26

## Data Platform

528 CPU cores 1408G memory 500TB storage

https://entrada.sidnlabs.nl

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Data Platform
“Y Chestaap
Parquet
spark:
528 CPUcores
https: //entrada.sidnlabs.nl 1408G memory
500TB storage
```

## Slide 27

## Workflow

Generate Collect  Analyse  Send  Anonymise
filters domains data alerts data

## Slide 28

## Filters

- Use of multiple filters for removing noise

   - Spam, marketing related

- Based on attributes such as

   - IP address

   - ASN

   - Web content-type

## Slide 29

## Filters

#### Filter types

- Static

   - Manually maintained

- Dynamic

   - Automatically generated

## Slide 30

## Static Filters

Static and manually maintained lists

- **AS Number** : e.g. mail marketing company networks

- **Country** : High volume SPAM countries

- **IP Address:** e.g. other researchers

## Slide 31

## Dynamic Filters

Automatically generated each day

- **High Nxdomain** : DNS resolvers showing a high ratio of NXDOMAIN

- **Newly Seen** : IP addresses of resolvers that have not been seen before

- **Suspicious**

   - Open resolvers

   - Sinkhole clients

   - Abuse feeds (Spamhaus, APWG)

## Slide 32

## Alert Rules

#### Distinct risk categories

Based on 10-day average of daily DNS queries (after filtering)

- Low: <= 5

- Medium: > 5 en <= 10

- High  > 10

## Slide 33

## Alert Rules

Special conditions

- Is keyword or business activity match?

   - then risk is high

- Is email address found by web crawler?

   - then risk at least medium

## Slide 34

## Alert Message

- Designed in collaboration with registrars and registrants

- Sent on day 30 of 40 day quarantine period

- Registrant has 10 days to take action

## Slide 35

## Alert Message

- Designed to explain the risk and suggest actions, e.g.

   - Informing contacts

   - Restoring the domain

- Multiple alert modes

   - To registrant

   - To registrar, who then forwards the alert

   - Registrar opt-out, no alerts are sent

## Slide 36

Alert Message - Example

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Alert Message - Example
Belangrijke informatie over je opgeheven domeinnaam
Belangrijke informatie over je
opgeheven domeinnaam
mariethereseheijnen.nl
Er is mogelijk nog mailverkeer naar de domeinnaam
An English version of this e-mail can be found at www.sidn.nl
Dit is een bericht van SIDN, wij beheren het .nl-domein en ook de
domeinnaam mariethereseheijnen.nl. Je hebt deze domeinnaam opgezegd op
2023-05-06. Met het opheffen van mariethereseheijnen.nl vervallen ook alle
daaraan gekoppelde e-mailadressen. We sturen je dit bericht, omdat er
waarschijnlijk nog gemaild wordt naar een of meerdere e-mailadressen die
gekoppeld waren aan de opgeheven domeinnaam. Hier schuilt een risico in. We
vertellen je er graag meer over.
```

## Slide 37

## Anonymisation

PII information is deleted after a domain exits the 40-day quarantine period

- Registrant

   - Identifier

   - Name

   - Email address

## Slide 38

## 2 Pilots

Do registrants understand the warning?

## Slide 39

## 2 Pilots

Registrars worried about an increase in support calls

## Slide 40

## Alerts sent

After running LEMMINGS for 10-month period

- **587.778** deleted domains analysed

- Filtering removed 75% of mail related DNS queries

   - The average daily number of queries for

   - a domain dropped from **4.7 to 1.2**

- **54.410** alerts have been sent to registrants

## Slide 41

## Alerts sent

**54.410** alerts have been sent ( **9.2%** of deleted domains)

**Risk category Alerts Percentage** Low 44.701 82.15% Medium 8.080 14.85% High <u>4.639</u> 8.53%

## Slide 42

## Measuring the Effect

- Not possible to directly measure the number of prevented data leaks

- Using a proxy:

   - Cancel-delete request as a proxy for prevented data leaks

   - Registrant survey

## Slide 43

## Cancel-delete Proxy

- Cancel-delete as proxy for prevented data leaks

- Cancel-delete baseline for the 12-month period before using LEMMINGS

   - **0.13%** of **627.285** deleted domains received cancel-delete

## Slide 44

## Cancel-delete Proxy

LEMMINGS cancel-delete ratio vs. baseline ( **0.13%** )

|**Risk category**|**Cancel-delete**|**Percentage**|**Increase**|
|---|---|---|---|
|Low|237|0.53%|3.8x|
|Medium|38|0.84%|6.0x|
|High|50|1.08%|7.7x|

## Slide 45

## Do we alert the correct domains?

Domains receiving an alert are re-registered more quickly

## Slide 46

## Do we alert the correct domains?

Alerted and re-registered domains have a new mail server more quickly

## Slide 47

Registrant Survey

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Registrant Survey
"The mail was useful"
| don't know &@ Strongly disagree S& Disagree Neutral ®§ Agree & Strongly agree
0 10 20 30 40 50 60 70 80 90 100
Share of participants (%)
```

## Slide 48

Registrant Survey

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Registrant Survey
"The mail helped to prevent problems like the leakage of information"
| don't know @ Strongly disagree S& Disagree Neutral 98 Agree ™& Strongly agree
0 10 20 30 AO 50 60 70
Share of participants (%)
```

## Slide 49

## Future Work

- Analyse the impact of DNS Qname Minimisation

- • Improve DNS filters

## Slide 50

## Black Hat Sound Bytes

Key takeaways

- Data leaks due to deleted domains are a real thing

- • Difficult to directly measure the effect of LEMMINGS

- Explaining the problem to registrants is challenging

- • Low number of registrant and registrar questions

- • Positive response from Dutch Internet community

## Slide 51

SIDN.nl

@SIDN Questions? SIDN

www.sidnlabs.nl | stats.sidnlabs.nl
