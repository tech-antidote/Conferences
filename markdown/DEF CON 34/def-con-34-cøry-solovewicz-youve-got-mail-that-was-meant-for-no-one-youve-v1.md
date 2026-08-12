---
title: "You've Got Mail (That Was Meant For No One)"
speakers: ["Cøry Solovewicz"]
conference: "DEF CON"
conference_full: "DEF CON 34"
edition: "34"
year: null
source_pdf: "DEF CON 34/DEF CON 34 - Cøry Solovewicz - You've Got Mail (That Was Meant For No One) - You've v1.pdf"
pages: 28
sha256: "c0180ea8736ca6d7c406d7e3ebec73b0afd0fb0eb7c1d0a08fcaf8cdfd8fcacb"
text_chars: 5494
ocr_pages: 1
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T00:14:48Z"
---
# You've Got Mail (That Was Meant For No One)

**Speakers:** Cøry Solovewicz  
**Conference:** DEF CON 34  
**Source:** `DEF CON 34/DEF CON 34 - Cøry Solovewicz - You've Got Mail (That Was Meant For No One) - You've v1.pdf` (28 pages)

## Slide 1

**You've Got Mail (That Was Meant For No One)**

**Cøry Søløvewicz (aka interpünkt)**

## Slide 2

###### 2010 - The Beginning

Started thinking about data privacy

Used Gmail "+ addressing" to track retailers

Email address: <u>sasquatch@gmail.com</u>

Examples:

- sasquatch+shopping@gmail.com

- sasquatch+newsletter@gmail.com

## Slide 3

###### 2015 - Enter Catch-All Email

Registered domain: <u>notgettingmy.info</u>

Set up a catch-all email (wildcard)

Great for tracking and filtering

Bonus: Made phone reps say "notgettingmy.info" out loud 😄

Any address at the domain lands in one inbox

## Slide 4

###### What Is a Catch-All Email?

Receives all mail sent to a domain, regardless of the prefix

bigfoot@example.com

sasquatch@example.com

yeti@example.com

All land in catch.all@example.com

## Slide 5

###### 2020 - The Perfect Domain

Found noreply.us available

Registered it on Feb 29, 2020

Bonus experiment: Leap day registration (Spoiler: no free year)

Initially forgot about it

## Slide 6

###### The Trickling Begins

Started receiving odd emails:

Pizza order with PII

Job application confirmations

Dental Job search emails

All meant for someone else

## Slide 7

##### Then It Got Serious

Received sensitive emails from a city government

Appeared to come from a misconfigured fax machine

Default reply-to set to @noreply.us

## Slide 8

Realization I had created an accidental honeypot

## Slide 9

# **<u>placeholder squatting</u>**

_noun_ /ˈpleɪs·hoʊl·dər ˈskwɒt·ɪŋ/ _computing · security_ 1. registering or claiming an identifier that exists only as a placeholder or convention, before its legitimate use, to intercept traffic, data, or trust.

## Slide 10

###### Decided to monitor the inbox more closely

Began documenting the types of emails and creating filters to help organize.

## Slide 11

###### What I Received

Password resets

- School Platform Account Emails

Logistics Bills

- Internal tickets

Service orders

Test Platform Credentials

## Slide 12

##### By the Numbers @noreply.us

37,166

#### 2,329

Days Total emails received Feb 29, 2020 to July 16, 2026

#### 16.52

Unsolicited emails per day

## Slide 13

Expanding the Experiment Registered other "noreply" domains:

<u>noreply.tv noreply.property</u>

## Slide 14

Nothing compared to <u>noreply.us</u>

## Slide 15

https://research.domaintools.com/ statistics/tld-counts/

**source: https://research.domaintools.com/statistics/tld-counts/  (07/20/2026)**

## Slide 16

December 2024 - acquired <u>noreply.net</u>

## Slide 17

https://research.domaintools.com/ statistics/tld-counts/

**source: https://research.domaintools.com/statistics/tld-counts/  (07/20/2026)**

## Slide 18

.us - 1,800,248 domains .net - 12,316,283 domains

**source: https://research.domaintools.com/statistics/tld-counts/  (07/20/2026)**

## Slide 19

708.76 emails per day @noreply.net

## Slide 20

## Stats

###### **noreply.us**

###### **noreply.net**

###### **.us vs .net**

Total number of emails: 37,166 Total number of emails: 397,613 Total number of emails: **10.7x** Average emails per day: 13.97 Average emails per day: 708.76 Average emails per day: **50.7x** Emails in last 1 day: 5 Emails in last 1 day: 352 Emails in last 1 day: **70.4x** Emails in last 7 days: 152 Emails in last 7 days: 2534 Emails in last 7 days: **16.7x** Emails in last 30 days: 281 Emails in last 30 days: 10,889 Emails in last 30 days: **38.8x** Emails with attachments: 4,497 Emails with attachments: 27,941 Emails with attachments: **6.2x**

## Slide 21

placeholder_squatting_probe.py How it works 1. Generate candidate placeholder domains 2. Resolve each domain's real mailserver (MX, falling back to A/AAAA) 3. Probe over SMTP, send nothing. HELO → MAIL FROM:<> → RCPT TO, then hang up (never DATA) 4. Confirm catch-all, send a second RCPT TO to a guaranteed-fake address. 250 response means it takes mail for anyone

5. Record every result in SQLite RDAP, source-IP reputation, response category, catch-all verdict

## Slide 22

#### placeholder_squatting_probe.py

•<sup>noreply</sup>

•<sup>deleted</sup>

•<sup>deletedaccount</sup>

•<sup>deleteduser</sup>

•<sup>deleteuser</sup>

•<sup>example</sup>

- <sup>localhost</sup>

- <sup>noemail</sup>

- <sup>company</sup>

•<sup>removeduser</sup>

•<sup>removeuser</sup> •<sup>donotreply</sup>

## Slide 23

placeholder_squatting_probe.py 232 distinct prefixes (SLDs) Domains probed: 2,303 Confirmed catch-all: 207 (9.0% of all probed)

## Slide 24

### Total Domains Monitored

•<sup><u>noreply.us</u></sup> •<sup>noreply.fyi</sup> •<sup><u>noreply.net</u></sup> •<sup>noreply.tv</sup> •<sup>noreply.nz</sup> •<sup>noreply.property</sup> •<sup>noreply.legal</sup> •<sup>noreply.ws</sup> •<sup>removeuser.com</sup> •<sup>noreply.pw</sup> •<sup>deleteduser.net</sup> •<sup>noreply.onl</sup> •<sup>removeduser.com</sup> •<sup>no-reply.uk</sup>

- <sup>noreply.tel</sup>

- <sup>noreply.zip</sup>

- <sup>noreply.mov</sup>

- •<sup>noreply.fans</sup>

- <sup>noreply.page</sup>

- <sup>noreply.name</sup>

- •<sup>noreply.cymru</sup>

## Slide 25

###### Reflections

1 2 3
People assume "noreply"  Devs/testers use fake  Placeholder values can
means safe and unused domains that get reused in  become liabilities
prod

## Slide 26

###### Call to Action

1

Don't assume a domain is unmonitored

3 Periodically audit email systems for default addresses

2 Use reserved or internal domains for test data

4 And please... don't send faxes to strangers

## Slide 27

Final Thought "Just because it says noreply does not mean no one is reading."

## Slide 28

Thanks! Do you have any questions? contact@cory.so interpunkt.01 🎉 https://503.party 🎉 https://github.com/corysolovewicz/defcon34
