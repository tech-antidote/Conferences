---
title: "Journey to the center of the PSTN How I became a phone company, and why you should too."
speakers: ["Enzo Damato"]
conference: "DEF CON"
conference_full: "DEF CON 33"
edition: "33"
year: 2025
source_pdf: "DEF CON 33/Enzo Damato - Journey to the center of the PSTN How I became a phone company, and why you should too..pdf"
pages: 79
sha256: "38b7ba853692ce1575873b6e564be712bca5e5663f4136b4e7a070c89b8bdb0a"
text_chars: 24209
ocr_pages: 13
has_ocr: true
redacted_secrets: 0
ocr_confidence: 89.6
ocr_unreliable_blocks: 1
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T07:00:06Z"
---
# Journey to the center of the PSTN How I became a phone company, and why you should too.

**Speakers:** Enzo Damato  
**Conference:** DEF CON 33  
**Source:** `DEF CON 33/Enzo Damato - Journey to the center of the PSTN How I became a phone company, and why you should too..pdf` (79 pages)


## Slide 1

How I became a phone company, and how you can too Enzo Damato

1

## Slide 2

2

## Slide 3

3

## Slide 4

4

## Slide 5

## AS25944

5

## Slide 6

- How the phone network works

- How you can become a part of it

- How you can exploit the hell out of it

6

## Slide 7

- Legal advice

- A comprehensive course on voice network design

- A guide to the regulations in your state

- How to hack PBXes

7

## Slide 8

**Publicly Switched Telephone Network** Essentially, any phone that allows you to call another phone using a standard US phone number

8

## Slide 9

- A “real” phone company

   - owns it’s own numbering resources

   - Files it’s own FCC 499

   - Is interconnected with other carriers

9

## Slide 10

10


> Recovered by OCR — confidence 93/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
EXPLODING
THE PHONE
PHIL LAPSLEY
FOREWORD BY STEVE WOZNIAK
“A fascinating book”
i
10
```

## Slide 11

11

## Slide 12

- There was AT&T

   - An amalgam of local companies in each region, tied together by a parent long-distance network

   - Complete control over the US telephone network

- The 1984 breakup created:

   - 9 RBOCs with a monopoly on local calls (State regulation)

   - 1 IXC for LD subject to competition (Federal regulation)

12

## Slide 13

13


> Recovered by OCR — confidence 85/100 on the text kept, 65/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
The collapse of the empire
2006
1984
1004
a” BELLSOUTH
1984
2006
@ Bell Atlantic Mc
2000 2005 7 a
1984
1997 2003
— Northwestern Bell
verizon
1984 Py
Mountain Bell
AUS WEST COMPANY
Pacific Northwest Bell
1991 1991
2000
Qwe es
13
```

## Slide 14

14


> Recovered by OCR — confidence 92/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
at is a Local Call?
Washington
South Dakota
640
Wyoming
654
Colorado
Alabama
476
© Copyright 1999
Nathan Stratton
14
```

## Slide 15

- Calls within a rate center are always local

- Arbitrary local boundaries between rate centers

   - Usually, RC + adjoining RCs

15


> Recovered by OCR — confidence 85/100 on the text kept, 73/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
What is a Local
Call?
* Calls within a rate center are
always local
¢ Arbitrary local boundaries
between rate centers
¢ Usually, RC + adjoining RCs
Pennsylvania 484/610/835 NPA Overlay Rate Center Map \N A N PA,
Legend
(5) 484, 610 and 835 NPA Boundary
(2) Other NPA Boundaries
[| Rate Center Boundaries
272/570 NPA
908 NPA
ALLENTOWN RIEGELSVILLE
FERNDALE
(BUCKS)
BERNVILLE
4
READING
215/267/445 NPA
223/717 NPA
MORGANTOWN,
PHILADELPHIA
‘SUBURBAN.
ZONE 28
PHILADELPHIA ZONE 23
SUBURBAN. YSUBURBAN ZONE 24
SUBURBAN SUBURBAN
PHILADELPHIA
SUBURBAN,
ZONE 11
856 NPA
302 NPA
410/443/667 NPA
tev: 2021-12-08 (© 2016_2020 TomTom. This map is provided for informational purposes only.
15
```

## Slide 16

IntraSTATE InterSTATE
IntraLATA Governed by State PUC Governed by FCC?
Handled by LEC Handled by LEC
(Very rare)
Local calls are an exception:
• Weird arbitrary boundaries
• Always governed by state PUC
• Always handled by LEC
InterLATA Governed by State PUC Governed by FCC
• Always Unmetered*
Handled by IXC Handled by IXC

16

## Slide 17

- The telecom act of 1996:

- Enabled competition for LECs (CLECs)

- Normalized wireless regulation

- Required incumbent LECs (ILECs) to:

   - Interconnect at any technically feasible point on their network

   - Offer services and unbundled network elements (UNEs) for resale

   - At a quality equal to interconnection provided with subsidiaries or affiliates

   - On nondiscriminatory terms expressed in a publicly filed ICA

   - Collectively, 251/252 interconnection

- Later, (2015) a “half-CLEC” certification for VoIP-only carriers

17

## Slide 18

18

## Slide 19

Each color icon is a different company: Red – ILEC Wires: Black wire – TDM Purple wire – IP/SIP

CLEC and Mobile carriers often have one switch that spans LATA boundaries.

ILEC to CLEC call shown

Mobile offices connect
similarly to CLECs Non-Local IXC core
Or, can directly connect
 with an IXC s FGD tandem
IPX interconnection
For roaming and voice
Carriers can subtend
the ILEC tandem
for LD
There is a full mesh
between major IXCs
Connections with ILECs
are ONLY TDM
IPES can, but
are not required to
peer with IXCs
IPES Subtends CLEC
Main connection Unregulated
 for local traffic IP Interconnects
Direct connect to EO
For high-volume
Hypothetical other LATA
19

## Slide 20

###### Long Distance ILEC Call

InterLATA ILEC calls **must** go through IXCs

Mobile offices connect
similarly to CLECs Non-Local IXC core
Or, can directly connect
 with an IXC s FGD tandem
IPX interconnection
For roaming and voice
Carriers can subtend
the ILEC tandem
for LD
There is a full mesh
between major IXCs
Connections with ILECs
are ONLY TDM
IPES can, but
are not required to
peer with IXCs
IPES Subtends CLEC
Main connection Unregulated
 for local traffic IP Interconnects
Direct connect to EO
For high-volume
Hypothetical other LATA
20

## Slide 21

Long Distance CLEC call over private peering.

IP trunks used whenever possible

No regulations on how CLECs handle LD*

Mobile offices connect
similarly to CLECs Non-Local IXC core
Or, can directly connect
 with an IXC s FGD tandem
IPX interconnection
For roaming and voice
Carriers can subtend
the ILEC tandem
for LD
There is a full mesh
between major IXCs
Connections with ILECs
are ONLY TDM
IPES can, but
are not required to
peer with IXCs
IPES Subtends CLEC
Main connection Unregulated
 for local traffic IP Interconnects
Direct connect to EO
For high-volume
Hypothetical other LATA
21

## Slide 22

Call with alternative FGD tandem arrangement and interIXC handoff

###### Bypasses the ILEC tandem

Mobile offices connect
similarly to CLECs Non-Local IXC core
Or, can directly connect
 with an IXC s FGD tandem
IPX interconnection
For roaming and voice
Carriers can subtend
the ILEC tandem
for LD
There is a full mesh
between major IXCs
Connections with ILECs
are ONLY TDM
IPES can, but
are not required to
peer with IXCs
IPES Subtends CLEC
Main connection Unregulated
 for local traffic IP Interconnects
Direct connect to EO
For high-volume
Hypothetical other LATA
22

## Slide 23

- If the two carriers have a private IP interconnect, that is used

- If the call is local, send it over the local interconnection

- If the call is IntraLATA, it can go over the FGD tandem, or the IXC

- If the call is InterLATA, it goes over the IXC

23

## Slide 24

|(979)|855|- 5|555|
|---|---|---|---|
|Area code:
one or multiple|CO code:
basic unit of phone|Thousands-block:
in pooled rate|Line number|
|assigned to a|number routing,|centers CO codes||
|numbering plan
area|originally assigned
to a single end-|are subdivided into
thousands blocks,||
||office, now|replacing CO codes||
||assigned to a LEC|as the unit of||
|||assignment.||

24

## Slide 25

How can you port a number from one carrier to another?

Answer: Add an overlay layer to the routing!

25

## Slide 26

#### 1. Query a database for each outgoing call 2. Get back an LRN

- a phone number in a CO code owned by the destination carrier

- 3. Route the call based on the LRN!

26

## Slide 27

- An AOCN loads data to BIRRDS (Business Integrated Routing and Rating Database)

   - BIRRDS feeds the LERG

- The LERG maps thousands blocks and CO codes to CLLI codes • Basically, a BIG CSV file

   - Used to MANUALLY build routing entries on switches

   - CLLI codes are manually associated to SS7 point codes or other trunks

27

## Slide 28

- Phone numbers

   - NANPA

- Porting

   - NPAC

- OCNs (company codes)

   - NECA

- CLLI codes, SS7 point codes, LERG, IAC codes

   - Iconectiv

28

## Slide 29

- In almost all cases: calling party pays!

   - Calling customer pays LEC

   - Calling LEC pays IXC

   - Calling IXC pays receiving LEC

- Special cases for billing

   - 800 numbers are toll-free, so receiving party pays

   - 900 and 500 are premium numbers with nonstandard rates

- Local calls are almost always unmetered

   - Or pay per call, not per minute if charged

29

## Slide 30

30

## Slide 31

If the calling party always pays, And most people have unlimited minutes plans, Can I make free money by having people call me?

31

## Slide 32

**YES!** Welcome to access stimulation.

32

## Slide 33

People Call
Me

33


> Recovered by OCR — confidence 90/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Our Master Plan
PHASE 1 PHase 2 PHASES
> People Call Profit
7 Mle
33
```

## Slide 34

Dial-Up calls are 100% inbound Long duration Soooo…

We are an ISP We become a CLEC Almost no costs (no real telephone service) Piles of inbound minutes Profit!!!!!

34

## Slide 35

- Dial-Up calls are • 100% inbound • Long duration

- • Soooo… FCC 2001 ISP-Remand Order: • We are an ISP “Internet traffic is jurisdictionally interstate”

   - We become a CLEC

   - Almost no costs (no real telephone service)

   - • Piles of inbound minutes • Profit!!!!!

35

## Slide 36

FCC rules that calls to “the internet” are interstate?!!??!

What???

36

## Slide 37

People Call
Me

37


> Recovered by OCR — confidence 90/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Our Master Plan
PHASE 1 PHase 2 PHASES
> People Call Profit
7 Mle
37
```

## Slide 38

Just give people free stuff!

38


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Round 2: LD Access stimulation
Just give people free stuff!
@ FreeConferenceCall.com®
24/7 Professional Customer Service —
Home About Us
+ Save Money with
FREE
teleconferencing
+ Save Time
+ Simple To Use
+ Reservationless
+ Immediate Access
+ Dedicated Phone
Number and Access
Code
+ Free Conference
Call Recording,
Playback And
Download Features
+ Free Conference
Call Detail Report
Via Email After
Every Call
TOLL FREE 877.482.5838
Contact Us Services FA Blog
Free Teleconferencing and Conference Call FREE
“If you're paying for conference calls,
you're paying too much!”
Free, reservationless conference calling is our marquee service. This free teleconferencing service is
simple to use, requiring only a name and an email address to receive an instant account.
FreeConferenceCall will provide you with a dedicated dial-in number and an access code for our free
teleconferencing services, which are ready for immediate use. Your free teleconferencing line is
available to you 24/7. There is no need to schedule a meeting or make reservations. Each free
teleconferencing account accommodates 96 callers on an unlimited number of 6 hour conference
calls. Long distance charges may apply, but there are no additional charges from
FreeConferenceCall.com.
FreeConferenceCall accounts also come with FREE conference call recording! So not only is the
recording service free, it's accessible by phone or computer, with no additional charges for
downloading. You can distribute, archive or even send recordings to your listeners via RSS and
Podcast — for FREE. To access the new free teleconference recording features, just visit
FreeConferenceCall.com and register for a recording account. You will receive instant account access
with recording passwords and playback instructions.
Use Our Free Teleconferencing Service For...
« Regional / National Sales Meetings
* New Product Training / Launches
* Multi-Vendor Conferences
« Project Management Team Meetings
* Cross Functional / Divisional Meetings
+ Crisis Response Meetings
* Teaching / Educational Seminars
+ Motivational Seminars
+ School Group / Organization Meetings
« Sports Teams Meetings
Distributing Anonymous Phone Numbers To Your Online Friends
+ Family Reunions
Religious / Bible Study Groups
38
```

## Slide 39

39


> Recovered by OCR — confidence 92/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Round 2: LD Access stimulation
CLLI
907-917 AK 753H ANCHORAGE ANCRAKXCOMD 02/09/2018 Prefix Type: UNKNOWN
Switch Name: N/A
Switch Type: N/A
LATA: Alaska (AT&T Alascom) (832)
Tandem: N/A
Detailed Switch Info
39
```

## Slide 40

Inflated
Free
Rural
Stuff
rates

Very Angry

40

## Slide 41

FCC 2011 USF Transformation Order Revenue share agreement + 3:1 in-out ratio or 100% YOY increase Just give people free stuff! = No Access Revenue for you!

41

## Slide 42

42


> Recovered by OCR — confidence 96/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Round 3: Evading the blockade
This is legal under current
rules because a CEA is in
the call path
Centralized
Equal Access
Provider
Local Exchange
Carrier
Retail Service Interexchange
Provider Carrier Endpoint
Subscriber
Domestic traffic pumping calls
Hacker
Traffic Pumper
42
```

## Slide 43

43


> Recovered by OCR — confidence 96/100 on the text kept, 96/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Round 3: Evading the blockade
43
```

## Slide 44

44


> Recovered by OCR — confidence 74/100 on the text kept, 68/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
_pjsip/pjsip_distributor log_failed_request 5 3 >" failed for "107 3 1821471
pjsip/pjsip_distributor log_failed_request: Reques om '<s failed for "107.17 3 182147155 3 No matching endpoint found
res_pjsip/pjsip_distributor log_failed_request: Reques "107. 6 18 3 thenticate
res_pjsip/pjsip_distributor log_failed_request:
res_pjsip/pjsip_distributor log_failed_request
res_pjsip/pjsip_distributor log_failed_request:
res_pjsip/pjsip distributor log_failed_request GISTER' from '"46 :157.168.10>' failed 2 lid: 23 g endpoint found
res_pjsip/pjsip_distributor log_failed_request: STER' from 6 failed 67.42 dpoint found
res_pjsip/pjsip_distributor log_failed_request: st 'REG 246 ed fo 6 : endpoint found
res_pjsip/pjsip_distributor log_failed_request: Request ‘REG 2 1157.168. e 51: jo matching endpoint found
NOTICE[ 152: res_pjsip/pjsip_distributor log_failed_request REGISTER’ 2 5 5 67.42.251:537: 33 hing
c res_pjsip/pjsip_distributor log_failed_request from '"46 8 failed 1 23442 t found
res_pjsip/pjsip_distributor log_failed_request: Reques from '"46 246 ailed for 67.42 2709 Failed to authenticate
res_pjsip/pjsip_distributor log_failed_reques: E E for 43 hing endpoint found
res_pjsip/pjsip distributor log_failed_request es from 2 E b for 6 2 d to authentic
res_pjsip/pjsip_distributor log_failed_request REG from '"46 61623. for i 115570) - No matching endpoint found
res_pjsip/pjsip_distributor log_failed_request: Request from '"46 246 for 6 : d: 882415570) - Failed to authenticate
res_pjsip/pjsip_distributor log_failed_request: Request fi 461623. 15 failed for 6 2 No matching endpoint found
res_pjsip/pjsip_distributor log_failed_request: S E . for 3
res_pjsip/pjsip_distributor log_failed_request st REGISTER’ from i 1157.168.10> ed for 2 Uli 6 endpoint found
Pjsip/pjsip_distributor log_failed_request: from 6 e 2 2 61) - Failed to authenticate
res_pjsip/pjsip_distributor log_failed_request: G 2461623. 2167.42 : 93 No matching endpoint found
res_pjsip/pjsip_distributor log_failed_request: Reques E ; 5 Failed to authenticate
res_pjsip/pjsip_distributor log failed request: Request ‘REGIS 2 b "10>" failed 6 i jo matching endpoint found
NOTICE[ 1529 res_pjsip/pjsip_distributor log failed_request: Request ‘REGISTER’ from '"46 61023. >' failed 6 lid No matching endpoint found
NOTICE( 1: ]: res_pjsip/pjsip_distributor log_failed_request es STER' from failed 2 Failed to authenticate
NOTICE[ 1529358]: res_pjsip/pjsip distributor log_failed_request: Reque G fi 6 z faile 2 No matching endpoint found
NOTICE[1529358]: res_pjsip/pjsip distributor log_failed_request:
res_pjsip/pjsip_distributor log_failed_request 5 2 2
res_pjsip/pjsip_distributor log_failed_request from 10> 0 6 d: 8824155 matching endpoint. found
res_pjsip/pjsip_distributor log_failed_request GISTER’ from '"46: b failed 2 2 2 Failed to authenticate
res_pjsip/pjsip_distributor log_failed_request: G from '"46 246 failed 2 2 2 No matching endpoint found
res_pjsip/pjsip_distributor 1og_failed_reques: f E E 3) - Failed to authenticate
res_pjsip/pjsip_distributor log_failed_request: E
res_pjsip/pjsip_distributor log_failed_request s <sip: E "10>" failed 67.42.251:
“pjsip/pjsip distributor log_failed_request from 2 b :18>' failed 42.251: lid ning endpoint found
res_pjsip/pjsip_distributor log_failed_request from 61623. 157.16 failed 2 lid: 2: 61) - Failed to authenticate
res_pjsip/pjsip_distributor log_failed_request: Request * from '"46 246 failed 2:167.42.251: d: 293 hing endpoint found
res_pjsip/pjsip_distributor log_failed_request: Request ‘REG 246123. 157 ed fo 6 3 ailed to authenticat
res_pjsip/pjsip_distributor log_failed_request: Reques 2 is 5 e 1421251: jo matching endpoint found
res_pjsip/pjsip_distributor log_failed_request REGISTER’
res_pjsip/pjsip_distributor log_failed_request s STER' from
res_pjsip/pjsip_distributor log_failed_request: from
res_pjsip/pjsip_distributor log_failed_request: G from
res_pjsip/pjsip_distributor log_failed_request:
res_pjsip/pjsip_distributor log_failed_request > 5
res_pjsip/pjsip_distributor log_failed_request est ' om * >" failed 7 578° (c 9 1871860604-145270789) - Failed to nticate
res_pjsip/pjsip_distributor log_failed_request: fi failed 2 No matching endpoint found
res_pjsip/pjsip_distributor log_failed_request: Reques from *<sip:2 failed i 6:62 9 5 60604- Failed to authenticate
res_pjsip/pjsip_distributor log failed request: from 2 failed 2 No matching endpoint found
res_pjsip/pjsip_distributor log_failed_request s from ‘<sip:2 : Failed to te
NOTICE[ 152 res_pjsip/pjsip_distributor log_failed request: Request 'INVITE' from ‘<sip:2 >' failed for c 947505057-1871860604-145270789) - Failed to authenticate
```

## Slide 45

45


> Recovered by OCR — confidence 90/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Hackers rack up £12,000 phone bill
VoIP hackers run up S120 ,000 and providers passed it on to me
p ho ne b ill at Pe rt h bus ine S S Pennine and Focus Group blame each other after hundreds
of premium rate overseas calls were billed to my company
PBX phone system hacking nets crooks $50
million over four years
Dial G for guilty —- one miscreant admits laundering role
N fete) R AZIZ U DDIN HACK ATTACK: Redlands travel agency gets a $117,000 phone bill (UPDATE)
‘onspiracy to Commit Wire Fraud; Conspiracy to Gain Una \ccess to — a=,
Computers; Wire Fraud; Unauthorized Access to Comput: The _
Toronto
= Hacked phone lines rack up bill of more than
$7,000
a
45
```

## Slide 46

46

## Slide 47

- Adds SIP identity header with

   - Cryptographic signature

   - Calling phone number

   - Called number

   - Attestation level

      - A for fully verified caller ids

      - B for verified customer

      - C for gateway attestation

47

## Slide 48

If you have a phone, you may have noticed that you’re still getting robocalls. And caller ids are still being spoofed.

**Why?**

48

## Slide 49

IPES
Spam
CLEC
IPES
Poor Sods
Spamming
Jerk CLEC Cell

49

## Slide 50

IPES
Spam
CLEC
IPES
Poor Sods
Spamming
Jerk CLEC Cell

##### Call arrives with a C attestation, and the spoofed CID is legitimated

50

## Slide 51

- Multiple approaches to this

   - Spammer directly uses TDM

   - Spammer’s carrier uses TDM

   - Spammer forces call over a “legacy” pathway

- Mix + Match multiple shady carriers and shell companies

- Or just could be coincidental

   - Many phone companies are still TDM only

   - Routing can be weird

51

## Slide 52

Standard for TDM SHAKEN exists, but no agreement on implementation

I’m sure that calling party pays has _absolutely no role_ in delays on this front.

52

## Slide 53

Many separate shell companies to evade KYC. Each signed up with multiple

IPES providers with several numbers, rotated regularly

providers

Spamming
Jerk

IPES
PSTN
Poor Sods
Cell

53

## Slide 54

- If you can’t hide it, spread it

- Only front-level provider has to KYC

   - Shell companies to evade detection

- Shell companies connected to small VoIP shops

   - No/bad KYC

   - Low profile at each company

- Change numbers every two weeks

   - Numbers are 0.01/each

   - Let’s get 100/IPES

54

## Slide 55

- Mix + Match all of the above

   - Screws with recordkeeping

   - Evades traceback

- 3+ resellers in the chain

   - Diffuses responsibility

   - No one is regulated, difficult to take enforcement action

55

## Slide 56

- LNP and pooling abuse

   - No pin for wireline ports

   - Just fake LOA!

- SS7 access & phreaking

   - No ANI

   - Changed charge #

- AOCN number block hijacking

- Vulns on 20+ year old switches

Limited only by time and imagination!

56

## Slide 57

57

## Slide 58

#### 1. Get certification

2. Establish interconnection

3. Build a switch

4. Get your numbers

#### 5. Handle taxes

58

## Slide 59

|RBOC (ILEC)|ICO (ILEC)|CLEC|CMRS (Cell)|IPES|
|---|---|---|---|---|
|Bell successor|Non-Bell|Post ‘96 Non-|All wireless|VoIP only|
|entities|independent
incumbents|incumbents|companies|carriers|
|Always||Never|Sometimes|Never|
|required to|Sometimes|required to|required to|required to|
|interconnect
Only allowed|required to
interconnect
(rural|interconnect
Only allowed|interconnect
(only ILECs)|interconnect
Never allowed|
|to send
requests for
ICAs to CMRS|exemptions)
Only allowed
to send|to send
requests for
ICAs to ILECs|Only allowed
to send
requests for
ICAs to ILECs|to send
requests for
ICAs|
|Governed by
state PUCs|requests for
ICAs to CMRS|Governed by
state PUCs|Governed by
FCC|Required to
partner with
CLEC|
|Certification|Governed by|Certification|||
|grandfathered|state PUCs
Certification
grandfathered|by petition to
PUC for CPCN|Certification
attached to
spectrum
licenses|Governed by
FCC
Certification
by petition to
FCC for CPCN|

59

## Slide 60

- Don’t plan to wholesale, and can afford it -> Wireless

   - Technically supposed to only provide wireless service

- Don’t need ICAs -> IPES

   - Nationwide and minimal paperwork, but FCC is slow and expensive

- Want to have maximum power -> CLEC

   - Most paperwork

60

## Slide 61

- File with state public utilities commission, or FCC (if IPES)

- Generally, will need:

   - Balance sheets and income statements

   - Resumes for key executives

   - Descriptions of service area and services to be offered

   - Description of equipment to be deployed, and any construction

- Be prepared to wait 30-90 days

61

## Slide 62

### **READ YOUR STATE’S DOCKET!!!**

62

## Slide 63

- Every application filed is public

   - Read them. Do what works. Don’t do what doesn’t.

- Generally, however:

   - Have a team

   - Don’t have a criminal record or judgements

   - Have some amount of money

   - Read your state’s laws

- Don’t be afraid to call!

- Not as hard as it used to be

63

## Slide 64

- Need two kinds

   - Local (for calls from where your numbers “live”)

   - LD/FGD (for everything else)

- Inbound is hard, outbound is easy

   - Can just use “normal” SIP trunks for outbound

- First step is to pick a LATA and rate center that you’re going to get numbering resources from

64

## Slide 65

- In order for local calls to complete, you’ll need an ICA in the rate center where you’re numbers will live

- For an RBOC, this process is standardized:

   - Send an email

   - Fill in an information request form

   - Sign the draft ICA

- For smaller ILECs, the process is far more variable

   - You might have to supply the ICA

   - Prepare for people to not know what you’re talking about

65

## Slide 66

- Leased facilities & fiber meet point

   - “Entrance facility” from you to ILEC

   - Various trunk types for exchange of traffic between you and ILEC

   - Pricing roulette: InterLATA transport is **devastating**

- Dealing with TDM

   - Cheap T1 media gateways

   - SS7 is a real bear. Avoid if you can

- Interconnect companies

   - Peerless, Intelliquent, Widevoice

   - TDM-IP conversion as a service

   - Convenient but expensive

66

## Slide 67

- Can do LD through an ICA with an RBOC

   - If you like TDM, this is a good option

- Many companies offer it over IP, for free

   - Access homing tandem

   - If you’re doing good volume, intercarrier comp agreement

67

## Slide 68

68


> Recovered by OCR — confidence 88/100 on the text kept, 63/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Switch building 101
Opensips
FreeSWITCH
```

## Slide 69

- IMS

   - Required for LTE

   - “Standard” for consumer voice services, but not deployed

   - Confusing, difficult nightmare

- Custom

   - **Generally** SBC/signaling gateway element and media element

   - Tones of flexibility

   - Larger project

- Commercial switch (metaswitch, ribbon)

   - Very expensive

   - Less customizable

69

## Slide 70

- LEC routing

   - Local & IntraLATA calls over ICA trunks

   - Equal access support?

   - Dealing with TDM and SS7

- Billing!

- HA and failover

   - State standard of 4 nines

   - Multi-site? How?

70

## Slide 71

- NANPA

- You’ll need

   - OCN

   - LD interconnection

   - CLLI code

- 45-60 days

71

## Slide 72

- Once approved by NANPA

   - Need an AOCN to put numbers in BIRRDS

   - Input your numbers into NPAC

- After you’re online, submit Part 4

   - If your numbers are pooled, you’ll also have to submit a “PSTN confirmation”

72

## Slide 73

# You’re Done!!!!

73

## Slide 74

74

## Slide 75

- Monitor your call and SIP logs

   - Set alerts for unexpected usage

   - Lock down international dialing (especially to weird destinations)

   - Huge spikes to third party destinations are not normal

   - DID rotation is not normal

- Know your customer

   - Know the real person behind the company

   - Watch for weird numbering and calling patterns

   - Match customer size to number of minutes and DIDs

   - The ability to supply caller ID should be granted sparingly

75

## Slide 76

- Require ILECs to support IP interconnection

   - At the very least, mandate out of band SHAKEN

- End User SHAKEN

   - Moving the signing to the end-user PBX would fix many issues

   - Proper DNSBLs

- Better enforcement against rogue telcos

   - No proof, but I’d estimate 50% of robocalls come from <10 carriers

   - No licensing for outbound makes them hard to keep down

76

## Slide 77

- 5ESS, DMS100, Ribbon, Genband, Metaswitch

- Crossbar, step-by-step

- Routers, switches, servers, etc

- Mainframe gear

I give unloved gear a new home!

Are you a LEC, IXC, or ASN? I’ll interconnect/peer with anyone!!!

77

## Slide 78

- Livewire Telecom and Dylan Cruz

   - Who knows far more than I ever will about TDM and the “old net”

- Widevoice

   - Nothing but good things to say about their FGD service

- YKC communications

   - I know you didn’t have a choice when I asked for an ICA, but thanks anyway

78

## Slide 79

L: (979) 855 – 5555 M: (845) 248 – 8078 <u>edamato@ricetelecom.net ed56@rice.edu</u>

79
