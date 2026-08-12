---
title: "From Doxing to Doorstep Exposing Privacy Intrusion Techniques used by Hackers for Extortion"
speakers: ["Jacob Larsen"]
conference: "Black Hat"
conference_full: "Black Hat USA 2024"
edition: "USA"
year: 2024
source_pdf: "Black Hat USA 2024 slides/Jacob Larsen_From Doxing to Doorstep Exposing Privacy Intrusion Techniques used by Hackers for Extortion.pdf"
pages: 77
sha256: "f9557e5a9b3a39afa2b850e71bdf8713ed1f18e9dc52a5b6044fd8bf1b459b10"
text_chars: 30742
ocr_pages: 18
has_ocr: true
redacted_secrets: 0
ocr_confidence: 89.9
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T04:34:00Z"
---
# From Doxing to Doorstep Exposing Privacy Intrusion Techniques used by Hackers for Extortion

**Speakers:** Jacob Larsen  
**Conference:** Black Hat USA 2024  
**Source:** `Black Hat USA 2024 slides/Jacob Larsen_From Doxing to Doorstep Exposing Privacy Intrusion Techniques used by Hackers for Extortion.pdf` (77 pages)


## Slide 1

From Doxing to Doorstep: Exposing Privacy Intrusion Techniques used by Hackers for Extortion

###### Jacob Larsen

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 95/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
AUGUST 7-8, 2024
BRIEFINGS
From Doxing to Doorstep:
Exposing Privacy Intrusion Techniques used by Hackers for Extortion
Jacob Larsen
#BHUSA @BlackHatEvents
```

## Slide 2

### whoami

###### **@larsencyber**

###### **Jacob Larsen**

- Offensive Security Team Lead @ CyberCX

- Threat Researcher

- Researching underground cyber crime groups since 2016

- Based in Perth, Australia

<u>https://larsencyber.com</u>

#BHUSA @BlackHatEvents

## Slide 3

- 9 years ago, I was a doxing victim.

- I had an online account with a rare username which they wanted.

- Ever since then, I have followed the subculture surrounding doxing and those participating.

#BHUSA @BlackHatEvents

## Slide 4

### ViLE: Breaching a DEA Data Portal

- In March 2023, 2 members of a notorious doxing gang “ViLE” were charged for breaching a Drug Enforcement Agency data portal.

- This portal allowed them to search for anyone’s personal information across 16 different federal law enforcement databases.

<u>https://www.justice.gov/usao-edny/pr/two-men-chargedbreaching-federal-law-enforcement-database-and-posing-policeofficers</u>

#BHUSA @BlackHatEvents

## Slide 5

#ViLE

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 76/100 on the text kept, 42/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
View/Edit Request 648889 Select Action fig) Save
Assigned To: =
Birth State: |
Basic
[_) PRIVILEGE
Birth City: #ViLE
"DOG:
*Alien Number:|
iSelect Al
```

## Slide 6

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 93/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Victims are extorted into paying ('
have their information removed uses the threat of revealing
personal information to extort victims
```

## Slide 7

### ViLE: Doxing for Extortion

- ViLE used this access for “doxing”, which is slang for “dropping documents”, also known as dropping information which links someone’s public identity with their online username.

- The intention of doxing is to intimidate victims and make them fearful of “what might happen” when their personal information is uploaded on a website where it won’t be taken down.

- This is why adversaries choose to use websites like **Doxbin** .

#BHUSA @BlackHatEvents

## Slide 8


> Recovered by OCR — confidence 94/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Doxbin Home Add Paste Users Upgrades Hallof Autism TOS
Telegram
Login Register
Official Doxbin Telegram
Mirrors: doxbin.org | doxbin.com | doxbin.net
Search for a paste
Search for... Search
Showing 150 (of 133419 total) pastes
Pinned Pastes
Title Comments Views Created by Added
Development Changelog - 33727 Reiko [Council] Sep 7th, 2023
How to Ensure Your Paste Stays Up - 179812 ‘Operator [Admin] Nov 20th, 2020
Transparency Report
- 138370 Operator [Admin] Jun 20th, 2020
```

## Slide 9

### Doxbin

- Doxbin is a doxing website that offers adversaries, or their users, a place to upload doxes where they won’t be taken down. As per their website it says:

   - “ _if your information goes up, it won’t come down unless it breaks our terms of service_ ”

- A feature Doxbin offers upgraded users is the ability to publish private doxes.

#BHUSA @BlackHatEvents

## Slide 10

##### **Doxbin Account Upgrades**

**1941 – 302 = 1639 “Private” Doxes**


> Recovered by OCR — confidence 86/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Doxbin Account Upgrades
ID Username Comments | Pastes Join date
PERKS 294760 Joana 157 1941 1 year ago
Username preview Anonymous [Rich] ;
Name color sparkling gol d Information
Paste highlight color Gold User ID 294260
More noticeable 4 Joined 1 year ago
.GIF profile picture wd Pastes 302
Instant paste edits / Comments 174
Unlist your own pastes wf Following 0
Private your own pastes a a Followers 73
Password protected pastes v/ Likes Given 2
Username changes 3 Likes Received 309
Purchase with Bitcoin or Monero 1941 -— 302 =
1639 “Private” Doxes
```

## Slide 11

### Doxbin

- This means adversaries can upload a victims dox, and then send them a private link to it on Doxbin.

- Next, the adversary will attempt to extort the victim by threatening to release their personal information publicly and to the Doxbin community.

- • Due to this simple functionality, Doxbin has become the largest doxing community online and amassed 300,000 users and over 165,000 published doxes.

#BHUSA @BlackHatEvents

## Slide 12

###### **Doxbin Admins**

###### **ViLe Members**

brenton kt ego cain
convict
weep

## Slide 13

### Doxbin & ViLE

- Doxbin was founded in 2018 by two actors, called “Kt” and “Brenton”.

- “Kt” is one of 5 members of the doxing gang “ViLE”. The other members are

   - “Ego”, “Cain”, “Weep” and “Convict”.

- “Weep and “Convict” were the members charged by authorities, with the remaining members wanted for their involvement.

- To get better insights into the doxing techniques they used, I personally conducted an interview with “Ego”, a member of ViLE that wasn’t

apprehended.

#BHUSA @BlackHatEvents

## Slide 14

###### **Doxbin Admins**

###### **ViLe Members**

brenton kt ego cain
convict
weep

## Slide 15

## **who is** **_Ego_ ?**

**Started out in XBOX Live ISP Doxing scene. Member of wanted gang “ViLE”. Doxed key LAPSUS$ member “white”. Earns $100k+ from doxing and extortion.** **Schizophrenic and emotionally detached.**

ego

## Slide 16

###### **ego**

**Do you ever use private sources to enrich your data for doxes?**

**Yes, nearly every time. I’ve taught loads of people to do the same.**

- **Private databases,**

- **Text** • **TLO lookups,** • **Social engineering customer service,** • **Insiders at mobile carriers, and** • **Fraudulent Emergency Data Requests to social media companies.**

## Slide 17

### What is an Emergency Data Request?

- A procedure used by law enforcement in emergency situations.

- Information provided by service providers in less than 24 hours.

- • Circumvents the need for a subpoena, due to an immediate threat.

###### **Social Media Platform**

Mobile  Email
Number Address

**Residential Address**

IP Address

**Full Name**

#BHUSA @BlackHatEvents

## Slide 18

**Government or Law Enforcement**

**Social Media Law Enforcement Emergency Data email@usdoj.gov Email Verification Portal Request Platform**

#BHUSA @BlackHatEvents

## Slide 19

### Emergency Data Requests (EDR)

- Before an Emergency Data Request can be submitted, an identity verification process is required.

- For most Law Enforcement panels, this simply requires a Government email address to receive an authorization link, as shown in the previous slide.

- There are also aggregator platforms which offer Government workers a single portal to lodge multiple requests, against a variety of service providers simultaneously, as shown in the next slide.

#BHUSA @BlackHatEvents

## Slide 20

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 74/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
black hat \
Pare O cohaintin coinbase coinbase
NTL Law Enforcement US Law Enforcement
Click to request access
@ MoonPay ¥ official
```

## Slide 21

### Fraudulent Emergency Data Request

- Given the depth of information service providers have on users…

- If a fraudulent Emergency Data Request could be completed, it would be the **fastest** and **most efficient** way for an adversary to obtain **highly accurate** and **sensitive** data on a victim.

- Submitting a fraudulent request, only requires access to compromised Government email address, as this allows the adversary to verify themselves on Law Enforcement panels by receiving the authorization link.

#BHUSA @BlackHatEvents

## Slide 22

### Fraudulent Emergency Data Request

**Hijacked Gov Email**

**Government or Law Enforcement**

**email@usdoj.gov**

**Email Verification**

**Social Media Law Enforcement Emergency Data Portal Request Platform**

#BHUSA @BlackHatEvents

## Slide 23

### Fraudulent Emergency Data Request

- Government emails can be easily purchased on underground forums and Telegram communities, for the cheap price of $70 USD.

- They are typically obtained from information stealer malware logs, hijacked cPanels, and phishing.

- I went undercover and infiltrated invite-only communities where threat actors both sell Government emails and provide the service to submit fraudulent Emergency Data Requests.

#BHUSA @BlackHatEvents

## Slide 24

###### **Government Email Access**

$70 each

Law Enforcement Portals

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 91/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
blackhat
USA 2024 2:
Government Email Access |"
All for $70 each $
Our mails can be used for 70 each
Need a middleman? Try out our Escrow App!
```

## Slide 25

#### email accounts

*****.gov.mz

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 90/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
black hat
Tools
J Current User
gov
Custom Gov Emails
Primary Domain
*Philippines /direct * &
*Pakistan / direct * | Shared IP Address
*Brazil / subdomain* @
Direct domain - 125USD Home Directory
Subdomain - 100USD /nome/
Last Login IP Address
You can use them for phishings, EDR's, leads, |
scams, etc...
```

## Slide 26

### Hijacked US Gov Mails n***l@usdoj.gov

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 93/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Law enforcement
requests
n***|@usdoj.gov
€ C © hitp
Law enforcement
requests
Submitted
Under review
More info needed
Closed
© Reference number
Ref number
Creation date
| have 2x US top tier
@fbi.gov and @usdoj.gov
```

## Slide 27

### Fraudulent Emergency Data Request

- Once a fraudulent Emergency Data Request is completed the adversary will attempt to **compromise the victim’s personal accounts** , to get other sensitive information they can add to the victim’s Dox.

- Historically simply the fear of “what might happen” when a victim’s personal information was released online, was enough for them to meet extortion demands.

#BHUSA @BlackHatEvents

## Slide 28

Email
Email
Address
Account
Mobile
Number
Emergency  IP Address Dox
Data Request
Residential
Address
Full Name #BHUSA

#BHUSA @BlackHatEvents

## Slide 29

### Violence-as-a-Service

- This was because adversaries had no way to intimidate their victims in real life, and it was just seen as a virtual threat.

- However, due to new “Violence-as-a-Service” marketplaces, digital conflicts now manifest physically, with real life consequences.

- In my interview with “Ego”, I asked if Doxbin members pay for their targets to be intimidated physically, and he shared that even some of the members provide these services.

#BHUSA @BlackHatEvents

## Slide 30

**ego**

**Do Doxbin members pay for their targets to be bricked or intimidated physically?**

**Those who have the means often go for it, and some of the members even provide these services.**

**The range of offerings is quite extensive, from bricking, to firing shots at their homes from the outside.**

**These acts are usually driven by the motive to acquire cryptocurrency.**

## Slide 31

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 95/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
“ViLe has
come to get
yah!”
```

## Slide 32

#### **Violence-as-aService**


> Recovered by OCR — confidence 87/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Violence-as-a-
Service
© Harassment 4
Swats (USA & CA + UK + EU) ~-585 308
Constant calling, trolling, messaging (ANY
COUNTRY) ~ 25$
= anyone jumped ( UK + EU + USA) ~
170
Get any house bricked (USA + UK+ EU) ~
Get your target stabbed (UK + USA) ~
12,0008
Get your target kidnapped (UK ) ~
24,500$
A
Comes with video proof for any of these
@e@ MM / Escrow Accepted
@® 24/7 Online
Contact Mme: jijsiattenttianstingiemsiaitaja
```

## Slide 33

###### **ego**

**There’s those who take it a step further, and break into the residence, torturing these individuals with anything from cutting their fingers off to killing them, all to take the crypto currencies they behold. Things get pretty wicked online, much more than people realize.**

## Slide 34


> Recovered by OCR — confidence 95/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
PRESS RELEASE
Man Convicted of Violent Home Invasion
Robberies to Steal Cryptocurrency
yetrator-2 threatened
to cut off Husband’s toes and genitalia, if he didn’t access his
Coinbase account.
```

## Slide 35

### Violence-as-a-Service

- Cutting off someone’s fingers is quite different to throwing a brick through their window, however it is happening, and recent arrests prove this.

- In June 2024, a Florida man was convicted of doxing and extorting victims for their cryptocurrency, just like “Ego” said in the interview.

- He broke into victim’s homes, and took them hostage, even threatening to cut off their fingers and toes.

- This brings to life the doxing and extortion tactics used by gangs like ViLE.

#BHUSA @BlackHatEvents

## Slide 36

### Doxbin & ViLE

- ViLE disbanded within months of “Weep” and “Convict” being charged.

- “Kt” also went into hiding and decided to part ways with Doxbin.

- Doxbin was sold to “Operator” in June 2023, and “Reiko” stepped in as a new system administrator and developer.

- With an interest in wanting to better understanding the legality of Doxbin, I was able to organize an interview with “Reiko” to shed some light.

#BHUSA @BlackHatEvents

## Slide 37

###### **Doxbin Admins**

###### **ViLe Members**

kt
ego cain
reiko operator
convict
weep

#BHUSA @BlackHatEvents

## Slide 38

## **who is** **_Reiko_ ?**

**Started Doxing in 2016 when he was a minor. Involved in SWAT’ing attacks on women. Leader of doxing gang called “Valhalla”. Developer and system administrator of Doxbin.**

reiko

## Slide 39

**Bulletproof hosting is not necessary. Doxbin is not illegal. This is due to Section 230 of the Communications Decency Act**

**How do you ensure operational security with Doxbin infrastructure? Do you rely on bulletproof hosting?**

## Slide 40

### Legality of Doxbin

- In the interview “Reiko” shared that “ _bulletproof hosting is not necessary_ ” because “ _Doxbin is not illegal_ ”.

- However, this didn’t seem to be correct, as Doxbin runs a service called “offshore.cat” which recommends offshore hosting providers.

- The website includes reviews that specifically mention Doxbin’s experiences.

- It’s clear that offshore hosting providers are used by Doxbin operates in a legal gray area.

#BHUSA @BlackHatEvents

## Slide 41


> Recovered by OCR — confidence 90/100 on the text kept, 48/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
The Real Offshore Hosting List
OFFSHORE.CAT
The Real Offshore Hosting List HOSTIN
DOMAINS
VPN
EMAILS CON/WAF
Offshore.CAT is a compiled list of the real & genuine,
we have either used/have had experiencejw"™ ™
Company
Name Website link Description policy*
country Log
Filter Filter Filter Filter Filter
Offshore.CAT is a Doxbin Project.
An extremely lenient domain registrar,
=a has been hosting Doxbin.net for years
```

## Slide 42

### Communications Decency Act

- “Reiko” also shared that the reason Doxbin is not illegal, is because of Section 230 of the Communications Decency Act (CDA).

- The CDA is a US federal law which applies immunity to platforms which host or republish user’s content.

- This means that Doxbin, and other websites which republish user’s content, cannot be held legally liable for what user’s say and do.

- A case example of this, is Gamergate.

#BHUSA @BlackHatEvents

## Slide 43

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 96/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
CDA 230 isa
federal law that
prevents websites,
blogs, and forums
from being held
responsible for
the speech of
their users.
“No provider or user
of an interactive
computer service
shall be treated as the
publisher or speaker
of any information
provided by another
information content
provider.”
```

## Slide 44

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 88/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
q Death to Brianna
£4 spacekatgal You just made a game nobody liked. That's it.
= Nobody wil Ilcare when you die.
4 Death to Brianna
£4 spacekatgal | hope you enjoy your last moments alive on this earth.
= YOu did nothing worthwhile with your life.
```

## Slide 45

### Communications Decency Act

- This was a case from a female game developer Brianna Wu, against Twitter.

- She sued Twitter, as **Twitter users were sharing her dox and death threats** on the platform.

- Twitter won the case, as they **could not be held legally liable** for what user’s uploaded to their platform, under the Communications Decency Act.

- Like this, Doxbin takes the stance, that even though user’s upload victims doxes to their website, which can be used for harassment, they are not

responsible or legally liable.

#BHUSA @BlackHatEvents

## Slide 46

### What other laws relate to Doxing?

**US Interstate Communications Statute, section 875(c).**

- Criminalizes any communication containing a threat to injure a person.

- Threatened party does not need to receive the threat.

#BHUSA @BlackHatEvents

## Slide 47

### What other laws relate to Doxing?

**US Interstate Stalking Statute, section 2261A(2).**

• Prohibits the use of any interactive computer service in a ‘course of conduct’ that places a person in reasonable fear of death, or serious bodily injury, or causes substantial distress to a person.

#BHUSA @BlackHatEvents

## Slide 48

# <u>Terms of Service</u> Content that is not allowed on Doxbin: **Direct** **_threats_ for physical harm**

## Slide 49

### Circumventing Legal Liability

- I shared earlier that Doxbin prides themselves on being a platform where doxes are not taken down, unless it breaks their terms of service.

- Doxbin, aware of the laws discussed, has constructed their terms of service to circumvent legal liability, by **disallowing doxes to include direct threats** for physical harm.

- Whilst direct threats are not allowed, I spoke to a prolific Doxbin member called “Joana”, who shared more insights.

#BHUSA @BlackHatEvents

## Slide 50

**joana**

**Do you believe Doxbin users might leverage a person’s dox for intimidation or threats?**

**Doxbin disallows *direct* threats for acts of violence. There is no doubt that information posted on Doxbin can and has been used to harass the people it pertains to.**

## Slide 51

### Circumventing Legal Liability

- “Joana” mentioned that simply sharing a victims dox could have the intention of intimidation and be used for threats.

- However, if the published dox doesn’t include a threat, it could be seen as technically complying with all US laws.

- This creates an **ambiguous stance** , as there is **nothing remaining** under US law that **prohibits Doxbin from running.**

- Whilst Doxbin will take down a dox if it violates their terms of service, they don’t proactively review any published content to see if it complies.

#BHUSA @BlackHatEvents

## Slide 52


> Recovered by OCR — confidence 88/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Rules:
Content that is not allowed on Doxbin:
- Third party links to underage explicit images
- Pastes that don't meet our information minimum requirements (Example)
- Any personal information specifically about children under the age of 15
- Dox requests
- Spam
- |Ploggers/infected files
- Reposting the same copy/paste dox
- Direct threats of physical harm, terroristic threats and swat threats/requests
If you would like to report a paste for TOS violation, contact us on Telegram #
If a paste does not break our rules, there is nothing we can do. ° # © ee
```

## Slide 53


> Recovered by OCR — confidence 92/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Title Comments Views Created by Added
- 138407 Kt [Admin] Jun 20th, 2020
https://dox.report/ | https://archive.is/BNgzv
Transparency Report
Transparency Report
We abide to a regulation made by us to comply with our current legal rights.
Please read over TOS & FAQ to understand our code of conduct.
Breaking this will result in a paste deletion.
Current Period: May 2020 - May 2024
Legal Enquiries: legal@dox.report
Updated on 18th of July, 2024
+
[September ist, 2023]
Pennsylvania State Police, Pennsylvania, USA
Requested: Paste removal
Verdict: Denied | Information within the paste is considered public.
+
```

## Slide 54

### Circumventing Legal Liability

- Instead Doxbin maintains a **Transparency Report** , which is a public record of all Government agency requests to take down information on the site.

- Since inception, Doxbin has received over 141 Government requests from 27 different countries worldwide.

- However, **only 43%** of these request have resulted in a dox being taken down. This means only **60 out of a possible 165,000** have been removed.

#BHUSA @BlackHatEvents

## Slide 55

### Doxbin Responses Verdict

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 96/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Doxbin Responses Verdict
Pending User data not logged
0.7% 14.9%
Denied
19.9%
No reply
21.1%
Removed
43.4%
```

## Slide 56

### Circumventing Legal Liability

- It’s clear that Doxbin uses the Transparency Report to masquerade as running as legitimate website that complies with Government requests.

- However, they are operating in a legal gray area due to gaps in U.S. policy.

- They’ve carefully constructed their terms of service to exploit these gaps and avoid legal liability.

- Due to these gaps, **policy changes are required** to better protect victims, by persecuting doxing platforms and perpetrators.

#BHUSA @BlackHatEvents

## Slide 57

### Required Policy Reform **<u>Doxing Platforms:</u>**

Hosting of doxing information, should be reasonably accepted to have the intention of malicious dissemination and be disallowed under communications policies.

**<u>Doxing Perpetrators:</u>**

The sharing of personal information without an individual’s permission, should be reasonably accepted to have the intention of causing substantial stress, or a threat to harm and be disallowed under stalking policies.

#BHUSA @BlackHatEvents

## Slide 58

How to help protect yourself from Doxing?

#BHUSA @BlackHatEvents

## Slide 59

###### **US Department of Homeland Security**

1. Turn on privacy settings on social media.

2. Set unique and complex passwords.

3. Use two-factor authentication on all accounts.

4. Limit personal information that you share online, even if temporary.

**Make a habit of searching for yourself online, to see how much of your information is accessible.**

<u>https://www.dhs.gov/publication/resources-individuals-threat-doxing</u>

#BHUSA @BlackHatEvents

## Slide 60

###### **ego**

**What are the common mistakes you see people make that lead them to get doxed?**

- **Identical email addresses across all online accounts, with password re-use.**

- **Using consistent or similar usernames across various platforms.**

- **They choose not to use VPNs.**

- **Sharing complete names and general location on social media platforms.**

- **Post personal pictures of family members, compromising privacy and security.**

## Slide 61

### Recommendations

- Earlier I shared a diagram which shows that an adversary's primary objective after completing a fraudulent Emergency Data Request is to **compromise the victim’s personal accounts** .

- Unfortunately, there isn’t anything that can be done by you to protect yourself from a fraudulent Emergency Data Request, as this requires industry changes which will take time.

- Instead, you can focus on **disrupting the attack chain** which is used to compromise your personal accounts, after the fraudulent request is completed.

#BHUSA @BlackHatEvents

## Slide 62

Email
Email
Address
Account
Mobile
Number
Emergency  IP Address Dox
Data Request
Residential
Address
Full Name

#BHUSA @BlackHatEvents

## Slide 63

### Recommendations

- When the fraudulent Emergency Data Request is completed, the adversary will obtain your email address and mobile number and use this to compromise your account through the **account recovery forgotten password** process.

- They will perform a **sim swap attack** on your mobile number, to port forward it to a sim card they control, so they can **receive a One-Time-Pass** (OTP) code.

- • This OTP allows them to change the password to your account and disable multi-factor authentication, compromising it for them to harvest additional information for the dox.

#BHUSA @BlackHatEvents

## Slide 64

Account Recovery
Email  OTP Sent
Process Initiated
Address

Emergency Data
Request
Mobile
Number

Password Reset  Email Account
Sim Swap
OTP Captured Compromised

#BHUSA @BlackHatEvents

## Slide 65

**To disrupt the attack chain, you need to make sure the adversary can’t receive your OTP code.**

Email
Address

**Account Recovery Process Initiated**

OTP Sent

Emergency Data
Request
Mobile
Number

Password Reset  Email Account
Sim Swap
OTP Captured Compromised

#BHUSA @BlackHatEvents

## Slide 66

### Recommendations

- Remove SMS-based authentication from all your online accounts.

- If a sim swap attack occurs, your mobile number can’t be used to hack you.

- Your MFA must always include an Authenticator-based application, or a physical token.

- Try to never use SMS-based authentication, except in exceptional circumstances where nothing else is offered. However, the mobile number used cannot be linked to your identity in any way.

#BHUSA @BlackHatEvents

## Slide 67

Authenticator App

**Account Recovery Email Process Initiated Address**

**OTP Sent**

Physical Token

**User**

Emergency Data
Request

**Break Glass Mobile (not linked to identity)**

**Mobile Number**

**Sim Swap**

#BHUSA @BlackHatEvents

## Slide 68

### Protecting Residential Address

- Use P.O. boxes and mail forwarding services.

- Blur your home, vehicle and persons on google maps.

#BHUSA @BlackHatEvents

## Slide 69

### Personal Safety

###### **Physical deterrents** :

- CCTV

- Intrusion alarms

- Floodlights

- **Self-defence** :

- Baseball bat

- Licensed firearm

#BHUSA @BlackHatEvents

## Slide 70

**1. Doxing is no longer just a virtual threat; it has evolved into a tool used for real world extortion.**

**2. Limit the personal information you share and make the habit of searching for yourself online.**

**3. Never secure your accounts with SMS-based authentication.**

**4. Blur your home on Google Maps and implement physical deterrents.**

#BHUSA @BlackHatEvents

## Slide 71

**Read full chat transcripts with “** **_Ego” and “Reiko”_**

<u>larsencyber.com</u>

#BHUSA @BlackHatEvents

## Slide 72

### Credit

1. Credit to **Zach Stanford** <u>(@svch0st) for a massive help in the initial</u> research phase, assisting with the preparation of interview questions, and connecting me with relevant industry professionals.

2. Credit to **Shanna Daly** <u>(@fancy_4n6) and</u> **Lidia Giuliano** <u>(@pink_tangent)</u> for their mentorship in the Black Hat Speaker’s Program.

3. Credit to **Chis Rock** <u>(@chrisrockhacker) for providing feedback on my</u> CFP submission.

4. Credit to **Angus Strom** <u>(@0x10F2C_) for providing feedback on my CFP</u> submission.

5. Credit to **Bex Nitret** <u>(@4n6Bexaminer) for inspiring me to complete</u> investigative-style security research.

#BHUSA @BlackHatEvents

## Slide 73

### References

1. Doxbin: https://doxbin.org

2. ViLE: https://vile.sh

3. Doxbin’s Offshore Hosting List: https://offshore.cat/

4. Wired – What is Doxing: https://www.wired.com/2014/03/doxing/

5. DailyDot – Silk Road trial judge may have been doxed and threatened: https://www.dailydot.com/debug/forrest-dox- <u>threatened/</u>

6. Vice – What Happens When a Lawyer Takes on a Hacker: https://www.vice.com/en/article/z4mqxy/what-happens- <u>when-a-lawyer-takes-on-a-hacker</u>

7. KrebsOnSecurity – Two USA Men Charged in 2022 Hacking of DEA Portal: https://krebsonsecurity.com/2023/03/two- <u>us-men-charged-in-2022-hacking-of-dea-portal</u>

8. US Department of Justice – Two Men Charged for Breaching Federal Law Enforcement Database and Posing as Police Officers to Defraud Social Media Companies: https://www.justice.gov/usao-edny/pr/two-men-charged- <u>breaching-federal-law-enforcement-database-and-posing-police-officers</u>

#BHUSA @BlackHatEvents

## Slide 74

### References

9. US Department of Justice – Two Men Plead Guilty to Computer Intrusion and Aggravated Identity Theft for Hacking into Federal Law Enforcement Web Portal: https://www.justice.gov/usao-edny/pr/two-men-plead-guilty-computer- <u>intrusion-and-aggravated-identity-theft-hacking-federal</u>

10. NYDailyNews – Members of ViLe online group charged by Brooklyn feds with using stolen police credentials for doxing scheme: https://www.nydailynews.com/2023/03/14/members-of-vile-online-group-charged-by-brooklyn-feds- <u>with-using-stolen-police-credentials-for-doxxing-scheme</u>

11. Vice – Nobody is Safe in Wild Hacking Spree: https://www.vice.com/en/article/pkae7g/nobody-is-safe-in-wild- <u>hacking-spree-hackers-accessed-federal-law-enforcement-database</u>

12. BBC – LAPSUS$ Oxford teen accused of being multi-millionaire cybercriminal: <u>https://www.bbc.com/news/technology-60864283</u>

13. BBC – LAPSUS$: GTA 6 Hacker Handed Indefinite Hospital Order <u>https://www.bbc.com/news/technology-67663128</u>

14. KrebsOnSecurity – NJ Man Hired Online to Firebomb, Shoot at Homes Gets 13 Years in Prison: <u>https://krebsonsecurity.com/2023/10/nj-man-hired-online-to-firebomb-shoot-at-homes-gets-13-years-in-prison/</u>

15. KrebsOnSecurity – Violence-as-a-Service, Brickings, Firebombings and Shootings for Hire: <u>https://krebsonsecurity.com/2022/09/violence-as-a-service-brickings-firebombings-shootings-for-hire/</u>

#BHUSA @BlackHatEvents

## Slide 75

### References

16. CourtListener - United States vs McGovern-Allen: <u>https://www.courtlistener.com/docket/64945732/united-states-v-mcgovern-allen/</u>

17. YouTube: Ironic – The Dark History of Doxbin: <u>https://www.youtube.com/watch?v=ULxiqLNybUA</u>

18. KrebsOnSecurity – Hackers Gain Power of Subpoena via Fake “Emergency Data Requests”: <u>https://krebsonsecurity.com/2022/03/hackers-gaining-power-of-subpoena-via-fake-emergency-data-requests/</u>

19. US Department of Justice – Man Convicted of Violent Home Invasion Robberies to Steal Cryptocurrency: <u>https://www.justice.gov/opa/pr/man-convicted-violent-home-invasion-robberies-steal-cryptocurrency</u>

20. WIRED – Inside a Violent Gang's Ruthless Crypto-Stealing Home Invasion Spree: <u>https://www.wired.com/story/crypto-home-invasion-crime-ring/</u>

21. CourtListener – United States vs Seemungal: <u>https://www.courtlistener.com/docket/67654880/united-states-v-seemungal/</u>

22. US National Institute of Justice – Ranking Needs for Fighting Digital Abuse: <u>https://nij.ojp.gov/topics/articles/ranking-needs-fighting-digital-abuse-sextortion-swatting-doxing-cyberstalking</u>

#BHUSA @BlackHatEvents

## Slide 76

### References

23. Witwer, A. R., Langton, L., Vermeer, M. J., Banks, D., Woods, D., & Jackson, B. A. (2020). Countering technologyfacilitated abuse: Criminal Justice Strategies for combating nonconsensual pornography, sextortion, doxing, and swatting. RAND.

<u>https://www.ojp.gov/library/publications/countering-technology-facilitated-abuse-criminal-justice-strategies-combating</u>

24. Australian Government eSafety Commissioner – Doxing Tech Trends and Challenges: <u>https://www.esafety.gov.au/industry/tech-trends-and-challenges/doxing</u>

25. US Department of Homeland Security – Resources for Individuals on the Threat of Doxing: <u>https://www.dhs.gov/publication/resources-individuals-threat-doxing</u>

26. Electronic Frontier Foundation – Section 230 Communications Decency Act: <u>https://www.eff.org/issues/cda230</u>

27. HudsonRock – Infostealer Infections Lead to Hacking of Google, TikTok, and Meta Law Enforcement Systems: <u>https://www.infostealers.com/article/infostealer-infections-lead-to-hacking-of-google-tiktok-and-meta-lawenforcement-systems/</u>

28. Michigan Technology Law Review – Online Harassment and Doxing on Social Media: <u>https://mttlr.org/2022/04/online-harassment-and-doxing-on-social-media/</u>

#BHUSA @BlackHatEvents

## Slide 77

### References

29. Batuhan Kukul, Personal Data and Personal Safety: Re-examining the limits of public data in the context of doxing, International Data Privacy Law, Volume 13, Issue 3, August 2023, Pages 182-193: <u>https://doi.org/10.1093/idpl/ipad011</u>

30. Julia M. MacAllister, The Doxing Dilemma: Seeking a Remedy for the Malicious Publication of Personal Information, Fordham Law Review, Article 44, 2017: <u>https://ir.lawnet.fordham.edu/cgi/viewcontent.cgi?article=5411&context=flr</u>

31. Schuster, J., Franz, A., & Benlian, A (2024). What Makes Doxing Good or Bad? Exploring Bystanders’ Appraisal and Responses to the Malicious Disclosure of Personal Information <u>https://scholarspace.manoa.hawaii.edu/server/api/core/bitstreams/5d7c2c85-a253-4b5c-9728-a6c2a614a5d0/content</u>

32. Shan, G., Pu, W., Thatcher, J. B., & Roth, P. (2024). How Doxing on Social Media Leads to Social Stigma and Perceived Dignity. <u>https://scholarspace.manoa.hawaii.edu/server/api/core/bitstreams/3607365d-95e3-4b0a-ae9684045e78e07e/content</u>

#BHUSA @BlackHatEvents
