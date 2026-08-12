---
title: "Swipe Left for Identity Theft An Analysis of User Data Privacy Risks on Location-based Dating Apps"
speakers: ["Karel Dhondt", "Victor Le Pochat"]
conference: "Black Hat"
conference_full: "Black Hat USA 2024"
edition: "USA"
year: 2024
source_pdf: "Black Hat USA 2024 slides/Karel Dhondt & Victor Le Pochat_Swipe Left for Identity Theft An Analysis of User Data Privacy Risks on Location-based Dating Apps.pdf"
pages: 36
sha256: "9e899f1a98c1bfae22779e699693f699c644646de6ee6dce3e95eb612f610d70"
text_chars: 13217
ocr_pages: 10
has_ocr: true
redacted_secrets: 0
ocr_confidence: 85.1
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T04:35:06Z"
---
# Swipe Left for Identity Theft An Analysis of User Data Privacy Risks on Location-based Dating Apps

**Speakers:** Karel Dhondt, Victor Le Pochat  
**Conference:** Black Hat USA 2024  
**Source:** `Black Hat USA 2024 slides/Karel Dhondt & Victor Le Pochat_Swipe Left for Identity Theft An Analysis of User Data Privacy Risks on Location-based Dating Apps.pdf` (36 pages)


## Slide 1

**_Swipe Left for Identity Theft_** An Analysis of User Data Privacy Risks on Location-based Dating Apps **Karel Dhondt** , **Victor Le Pochat** , Yana Dimova, Wouter Joosen, Stijn Volckaert

## Slide 2

2


> Recovered by OCR — confidence 93/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
sky news @WCnNBC
Finding love online: More than half of | How singles are meeting up on dating
couples set to meet via the internet
© Wednesday 27 November 2019 03:42, UK
FORTUNE
Activity on dating apps has
surged during the pandemic
BY FORTUNE EDITORS
5:30 PM GMT+1
apps like Tinder, Bumble, Hinge during
coronavirus pandemic
PUBLISHED TUE, MAR 24 2020-12:14 PM EDT | UPDATED TUE, MAR 31 2020-10:42 AM EDT
@CAMERONCOSTANY
Bloomberg
A Record Number of Americans
Used Dating Apps in July
By Akayla Gardner +Follow
3 augustus 2021 om 19:15 CEST
Tinder: More pay for dating app
despite cost-of-living crisis
By Noor Nanji
Business re porter, BBC News
```

## Slide 3

3


> Recovered by OCR — confidence 89/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
BIB @ INDEPENDENT
Dating apps found ‘leaking’ News > World > Middle East
: Egypt police ‘using dating apps’ to
location data find and imprison LGBT+ people
© 19 January 2015
Victims thrown into jail and tortured, claims HRW
Gemma Fox Deputy International Editor * Thursday 01 October 2020 17:05
Dating App Insiders Remain
‘Highly Concerned’ About User *Tinder Swindler’ con artist, subject of
Security, According To A Recent new Netflix documentary, banned from
Survey dating app
TET Cee Tinder has also issued new guidelines to protect users from would-be romance
yahoo/news H By Jennifer Hassan
Updated February 7, 2022 at 12:09 p.m. EST | Published February 6, 2022 at 10:32 a.m. EST
the dark side of dating apps } j
A quick sean of your dating profile could provide a scammer
revealed with exactly what they want. Here's how to keep your
Joanna Morris personal details safe
3 July 2022 - 3-min read
Posted Wedi 4 Jan 2023 at 7:41pm, updated Thu 5 Jan 2023 at 1Z4aam
```

## Slide 4

TINDER BADOO POF MEETME TAGGED
100M 100M 50M 50M 50M
GRINDR TANTAN JAUMO LOVOO HAPPN
50M 50M 50M 50M 10M
BUMBLE HINGE HILY OKCUPID MEETIC
10M 10M 10M 10M 10M

4

## Slide 5

1.438

5

## Slide 6

LBD apps elicit **peculiar privacy behavior**

› Users **willingly** share _highly personal and sensitive_ data (including **exact locations** )

› Users **expect** others to share data

› Users share data with **strangers**

Sufficient (self-)disclosure Maintaining privacy

6

## Slide 7

# What are the **privacy risks** in sharing personal data with **other users** ?

7

## Slide 8

**Social privacy** ( institutional privacy)

Our adversary focuses on collecting _<u>personal</u>_ data about _<u>one or more other users</u>_ of the LBD app user using only _<u>client-side</u>_ interactions as a _<u>regular</u>_

8

## Slide 9

#### Adversary Intentions

9


> Recovered by OCR — confidence 94/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Adversary Intentions
A quick scan of your dating profile could provide a scammer
with exactly what they want. Here's how to keep your
personal details safe
yahoo/news 3 INDEPENDENT
News > World > Middle East
Rape, stalking and blackmail: Egypt police ‘using dating apps’ to
the dark side of dating apps ___ find and imprison LGBT+ people
revealed
```

## Slide 10

# What is the extent of **data exposure & leaks** in **LBD apps** ?

10

## Slide 11

#### Data exposure & leaks

**UI Exposure** readily visible in the _UI_

**_Intended_** _sharing_

11

## Slide 12

#### Data exposure & leaks

**UI Exposure** readily visible in the _UI_

**Traffic leak Exfiltration leak** automatically sent sent after _altering_ in _API_ network traffic traffic or behavior

**_Intended_** _sharing_

**_Inadvertent_** _sharing_

12

## Slide 13

### Private Data Leaks

› Three modes of data exposure & leaks

_UI Exposure:_ readily visible in the UI _Traffic Leak_ : automatically sent in API network traffic _Exfiltration Leak:_ sent after altering traffic or behavior

## Slide 14

##### _Personal data_

_Sensitive data (GDPR art. 9)_

_App usage data_

14


> Recovered by OCR — confidence 96/100 on the text kept, 96/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
First name
Last name
Gender
Age
Date of birth
Education
Employment
Languages spoken
Nationality
Place of residence
Hometown
Relationship status
Marital status
Having children
Having siblings
Email address
Phone number
Other platforms
Photos
Interests
Income
Personal data
Racial or ethnic origin
Political opinions
Religious/philos. beliefs
Health data
Height
Weight
Figure
Fitness
Diet
Eye color
Hair color
Smoking
Alcohol
Recreational drugs
(COVID) vaccination
HIV status
Sexual orientation
Sex life
Other has liked you
Other has disliked you
Popularity score
Number of likes/dislikes
Other was recently active
Last activity time
Account creation time
Relationship type sought
Wanting children
Filters
# profiles per API request
Card stack
Grid
Permanent profile access
See profiles while paused
Sensitive data (GDPR art. 9)
App usage
data
14
```

## Slide 15

APIs leak data for **all** apps **99** leaks in total

15

## Slide 16

### Personal Data Leaks

###### _Tinder_ : leak of **non-binary gender**

16


> Recovered by OCR — confidence 75/100 on the text kept, 65/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
reeeecensseerve Tinder: leak of non-binary gender
Last name °
Age OO OROOO oOo° bio: "Academic research account, please ignore. We only collgq
Date of birth nc eee oan birth date: "1994-91-21708:21:29.4182"
Education fomekene: custom gender: "Gender non-conform"
Employment oo$ gender: -1
Languages spoken ooO-9 is traveling: false
Nationality jobs: [J
Place of residence o-¢-¢-o0o¢¢oo00¢ Mame: "Stijn"
Hometown online now: true
Marital status 0000-0. fone) recently active: true
Having children oooo e0000go00 schools: []
Having siblings > b sexual orientations: [{id: "ques", name: "Nog twijfelend"}]
. show gender on profile: false
one number
ta: tatus: 268
Other platforms ‘e) 2 pmeta: {status i
16
```

## Slide 17

### Sensitive Data Leaks

_All apps_ : **data reciprocity** nearly always fails (hidden attributes)

17


> Recovered by OCR — confidence 75/100 on the text kept, 58/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Sensitive Data L
M
Tom completed more of his profile than you. To reveal more about him,
2) (e) o fe complete at least 60% of your own profile.
Political opinions ---------- oo00o-
Health data
Weight -|-]- --o------ -~-0
Figure -|-190-0O-O0--- —~ 9,4 Name Payload Preview Response Initiator Timing Cookies
Fitness O < oO oO 6295. 1df7e3f3ce0c26. >0: {$gpb: "badoo.bma.ProfileField", id: "location", type: 1, nam
Diet oOl- —— = — FF = OO — BS OO 7009.42b425c9b3e1f.. >1: {$gpb: "badoo.bma.ProfileField", id: “aboutme text", type: 2,
v2: {$gpb: "badoo.bma.ProfileField", id: "relationship", type: 3,
name: nship"
(COVID) vaccination O--0O0-O----- OO - - Hi hidden?eurisacwO87x display value: "186 cm"
i hidden?euri=qJyJerl4x id: “appearance”
Sex life fe) © Eellwsberky :
17
All apps:
data reciprocity nearly always fails (hidden attributes)
```

## Slide 18

### App Usage Data Leaks

_Badoo, Bumble_ : **exfiltration** leaks of activity, filters _All apps_ : **data reciprocity** nearly always fails (hidden profiles)

18

_All except OkCupid_ : fetch **multiple profiles** at once

## Slide 19

### Location Data Leaks

19


> Recovered by OCR — confidence 80/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Location Data Leaks
Tagged
Jaumo
LOVOO
< | Grindr
& | Tantan
& | happn
Exact location —
Distance to other user OO -LO9019IO OOOO - - OO
City of recent location
def get nearby(self, geohash, min_age=None, max_age=None, segMch after profile id=None, search after_distance=None):
url = f"https://grindr.mobi/v8/search?nearbyGeoHash={qgOhash}Sonline=false"
if min_age is not None:
url += "G&ageMinimum=" + str(min_age)
if max_age is not None:
url += "G&ageMaximum=" + str(max_age)
if search after profile id is not None:
url += "“&searchAfterProfileld=" + sf (search after profile id)
if search after distance is not None:
url += "“&searchAfterDistance=" + str(search after distance)
url += "&photoOnly=false&faceOnly=false&notRecent lyChatted=false&profileTags=&fresh=false&f reeFilter=false&insertable=false"
response = self.session.get(url)
assert response.status code == 200
```

## Slide 20

### Trilateration: Exact Distance

2.211
2.184
20
1.438


> Recovered by OCR — confidence 80/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Trilateration: Exact Distance
a
© KU Leuven
fal Lives in Ghent
© 2.211 kilometers away
Karel 27@
1 PhD Researcher at KU Leuven
© KU Leuven
fa Lives in Ghent
Karel 27@
t PhD Researcher at KU Leuven \ “ : g 3 © 2.184 kilometers away
fa Lives in Ghent
© 1.438 kilometers away 20
```

## Slide 21

### Trilateration: Rounded Distance

2,5 km
2,5 km
1,5 km
32
12 21

23


> Recovered by OCR — confidence 79/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Karel 27@
“4 tt PhD Researcher at KU Leuven
™@ KU Leuven
fl Lives in Ghent
© 2 kilometers away
Karel 27@
1 PhD Researcher at KU Leuven
™@ KU Leuven
jG Lives in Ghent
Karel 27@
© PhD Researcher at KU Leuven FF \ wi \ SS ~f}© Bkilometers away
& KU Leuven ‘
fl Lives in Ghent
© 2 kilometers away
```

## Slide 22

### Trilateration: Proximity Oracle

22


> Recovered by OCR — confidence 90/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Trilateration: Proximity Oracle
Up to)2 kilometers jaway
See people slightly further away if | run out
Languages they know
Select languages
ae Apply
22
```

## Slide 23

### Bulk **account creation** accelerates stealthy stalking

› The adversary requires an **account** to browse profiles

→ This may **_expose_** the adversary to

- the platform (/law enforcement) → _anonymous_ - other users → _hidden_

## Slide 24

Bulk **account creation** accelerates stealthy stalking

› The adversary requires an **account** to browse profiles → This may **_expose_** the adversary to

- the platform (/law enforcement) → _anonymous_

- other users → _hidden_

› How **easily** and **stealthily** can adversaries gather data? **Security measures** for account creation _(also friction & forced sharing for legitimate users!)_

## Slide 25

### Security of the **account creation** process

› **Requirements** for account setup Email (11/15) _Easy to acquire_ Valid phone number (8/15) _Higher barrier, esp. anonymously_ Real profile data (8/15) _Never verified_

› _Stealth_ : empty profile (Grindr); hidden profile (Hinge) › _Anonymity_ : only email (MeetMe/Tagged)

## Slide 26

### Security of the **account creation** process

› Photo (12/15)

› Face photo (11/15) › Face verification (13/15)

- Only mandatory on Bumble

- • Profile badge = trust

## Slide 27

### **Privacy policies** of LBD apps fall short

- › Legal basis for processing of sensitive data: consent Sensitive data is stated to be optional _(sexual orientation?)_

- › Location sharing options are insufficiently clear

- 12 apps function without location permission

   - Grindr warns about location inference

- › Partially private profile may require paid subscription

- › **Burden to protect data is shifted to users**

- 7 apps warn about sharing data with other users

27

## Slide 28

### _Functionality_ and _privacy_ experience **tension**

**Sufficient (self-)disclosure** Maintaining privacy

› _Users_ **_want_** _data_ : filter on desired traits, search more info, increase trust, improve safety feeling › _Users_ **_provide_** _data:_ more success, protective disclosure; expectation, nudging, defaulting, and pressure to disclose

Sharing data is expected, not concerning, even beneficial

28

## Slide 29

### _Functionality_ and _privacy_ experience **tension**

Sufficient (self-)disclosure **Maintaining privacy** › _Users_ **_care_** _about social privacy_ : limit or falsify disclosure

› _Certain populations are at_ **_higher risk_** _:_ women: stalking/harassment; LGBTQ: outing/prosecution

Online dating is a sensitive context with genuine risks

29

## Slide 30

LBD apps should give users **_control, choice, agency_**

› Avoid nudging users to share data

› Inform users properly about sharing

› Hide profile data by default Make data sharing a conscious decision Only show profile to verified users

› Request location update explicitly Give option to share approximate location

30

## Slide 31

### LBD apps should better **_protect_** user data

- › Fix inadvertent API leaks _(OWASP API Security Top 10)_

- Limit exposure of/by API endpoints

- Enforce proper access control _(least privilege)_

   - <u>Match UI and API: avoid unnecessary extra data in API responses</u>

- › Prevent location inference

- Account for simple _(trilateration)_ and advanced _(stats)_ techniques Implement solutions such as spatial cloaking _(rounding coordinates)_ Consider user needs: does high accuracy matter?

31

## Slide 32

### LBD apps should better **_protect_** user data

- › Prevent mass data gathering _(account creation, stealth)_ <u>Requiring</u> phone number, face verification _(deepfakes)_ Rate limiting, detecting fake requests _(client-side signatures)_ /locations _Just annoying the adversary, and increasing friction for legit users?_

- › Avoid having data in the first place _(data minimization) Tinder_ has fewer sensitive data fields, deploys rounding coordinates

If you do not have data, you cannot leak it

32

## Slide 33

### Responsible disclosure

› 12 out of 15 apps **acknowledged** receipt

- › 9 engaged in substantial **discussion** & deployed **fixes** All location leaks have been fixed

- › _Security vulnerability_ vs. _privacy leak_ Access control bugs, improper filtering, hidden parameters, …

_“As for the data in the API responses, this is not private information”_

33

## Slide 34

### Conclusion

- › LBD apps harbor a **sensitive privacy context** _Users feel compelled to share data, but_ **_social privacy_** _is important_

- › (Intended) data **exposure** varies significantly between apps

- › **Inadvertent leaks/inference** reveal hidden data/locations **_APIs_** _are an important cause of privacy breaches_

- › Privacy policies fall short – Apps put **burden on users** _Need for_ **_technical audits_** _of UI and API, compared with privacy policy_

34

## Slide 35

## Black Hat Sound Bytes

**1. Think beyond** the typical “hacker” **2. API hardening** is crucial

**3. Data minimization** reduces leaks

35

## Slide 36

**_Swipe Left for Identity Theft_** An Analysis of User Data Privacy Risks on Location-based Dating Apps

\```
kareldhondt@outlook.com
victorlepochat@gmail.com
\```

Cybersecurity Research Program Flanders

_Full paper:_
