---
title: "Ghosts of REvil An Inside Look with the Hacker Behind the Kaseya Ransomware Attack"
speakers: ["Jon DiMaggio John Fokker"]
conference: "DEF CON"
conference_full: "DEF CON 33"
edition: "33"
year: 2025
source_pdf: "DEF CON 33/Jon DiMaggio John Fokker - Ghosts of REvil An Inside Look with the Hacker Behind the Kaseya Ransomware Attack.pdf"
pages: 39
sha256: "a5122a725a7158a7f575a29c45c89635eb2c86d9a0502de95a44a7b6c545c6f9"
text_chars: 10704
ocr_pages: 17
has_ocr: true
redacted_secrets: 0
ocr_confidence: 89.6
ocr_unreliable_blocks: 1
ocr_timeouts: 0
pages_recovered_from_text_layer: 1
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T07:03:18Z"
---
# Ghosts of REvil An Inside Look with the Hacker Behind the Kaseya Ransomware Attack

**Speakers:** Jon DiMaggio John Fokker  
**Conference:** DEF CON 33  
**Source:** `DEF CON 33/Jon DiMaggio John Fokker - Ghosts of REvil An Inside Look with the Hacker Behind the Kaseya Ransomware Attack.pdf` (39 pages)


## Slide 1

**Ghosts of REvil:** An Inside Look with the Hacker Behind the Kaseya Ransomware Attack

## Slide 2

##### **Hosts for Today**

**Jon DiMaggio** Chief Security Strategist, Analyst1

**John Fokker** Head of Threat Intelligence, Trellix

## Slide 3


> Recovered by OCR — confidence 91/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Tweet
New --> Romanian authorities have arrested two
people suspected of deploying REvil ransomware and
netting half a million euros in ransom payments,
Europol says. Part of ongoing US-European
crackdown.
Five affiliates to Sodinokibi/REvil unplugged | Europol
REvil, A Notorious Ransomware Gang,
Was Behind JBS Cyberattack, The FBI
Says
\cker accused of Kaseya ransomware attack
d and extradited to the US
¢ Thread
a BleepingComputer @
7
— Scoop: FBI seized $2.2 million in bitcoin from a wallet
NET owned by ‘Lalartu,' a well-known REvil and GandCrab
e Posts stolen documents on dark web
site called "Happy Blog”
AXIS OF REVIL
FBI seized $2.3M from affiliate of REvil, Gandcrab ransomware gangs
```

## Slide 4

#### **Revil Ransomware-as-a-Service (RaaS) Model**

Payout (requires
accounting)
Job
Interview
Ransomware
Admins and
developers
5 Pax
Victims
Affiliates Victims
+/-40 pax

Ransom

## Slide 5

##### **REVIL Core Operators**

Admin team
(5PAX)
Revil source
Affiliate  Backend
code
management  development
development
(2PAX) (2PAX)
(1PAX)
Orange Suslik
Morgot
Unkn  Not-found

**Alternative Jabber accounts: Orange** : Bitcoin, FunnyCrab **Unkn** :  8800553535, Crab **Suslik** : Eddie Bravo **Morgot** : Rcode, Quake3

## Slide 6

### **REvil Key Success Factors**

- Dedicated comms platform vs. Email negotiations

- Leak site to publish stolen data

- Stable Malware and Decryptors

- Increase of available affiliate spots strict selection

- Outsourcing or partnering with facilitating services (Malware obfuscation, Exploit Kits, Customer service Money laundering etc)

- Good administration of infections.

## Slide 7

**Accounting is Hard, but Affiliate Numbers Help…**

Ransomware
Victim Affiliate
Binary

Trellix developed a custom Config extraction tool, for internal use and LE incident response.

## Slide 8

**File Name**

###### **Description**

# **Ransomware Accounting**

**pk** Public key of the attacker in Base64 **pid** Affiliate number **sub** Sub-account or campaign id **dbg** Debug option Option to encrypt the first 1 megabyte of each target **fast** file or all files **wipe** Option to wipe specific files in the field ‘wfld’ **fld** Folders whitelist **wht fls** File whitelist **ext** List of targeted extensions **wfid** List of targeted folders **prc** List of processes to kill **dmn** List of C2 domains **net** Option to specify the connexion to C2 **nbody** Ransom not in base64 **nname** Strings of malware name **exp** Enable exploit CVE-2018-8453 **img** Wallpaper ransom note in base64

## Slide 9


> Recovered by OCR — confidence 69/100 on the text kept, 35/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
7562 1$0110860470645302bd 18890900 VERSION:
211bta 1dc5 1db0G26ct4a4o0a27da1504 VERSION: 5.04
SUBID: 15
SUBID: 62
SUBID: 62
SUBIO: 363
SUBID: 1438
```

## Slide 10

**But… Stay Humble**


> Recovered by OCR — confidence 92/100 on the text kept, 61/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
But... Stay Humble
The downfal
```

## Slide 11

### **Bragging**

**Lalartu made 300K USD in one weekend**

## Slide 12

“Mo Money Mo Problems”

##### **Even for Cyber Criminals…**

## Slide 13

## Slide 14

**Snitches get stitches… or not?** Lalartu exposed

Aleksander
Sikerin AKA
Lalartu

## Slide 15


> Recovered by OCR — confidence 89/100 on the text kept, 77/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Sub Last
Info aaa Price visit Botreg \
F3018F6AC886AAD2
f
EDEB12EC08725E2E
afew
=us = $6, seconds ago
216.59.
3C5BOED23ECFA541
WaxXxXx $6,500 ~ a minute ago
US 68.
7146E02E22BD6C77
WaxXxXx $6,500 - a minute ago
WaxXxXx $6,500 -- a minute ago
5 t
8D34D09DEC106C2E cx
1.6
Bot Version
== United States 104.6
GEO
Friday, 13 December 18:24 (9
minutes ago)
Registration date
njevsm16
Extension
0
Visits
lalartu (33) / waxXxXx (2231)
User / SubAccount
Windows 10 Enterprise / 64bit
en-US / no
Language / Ru?
A5300 1SS5AEDCE85
| uploaded. the universal decrypto...
support
5007957F86022CBA
meant http://decryptor.top/42B 1...
support
BC913DFFA8A1438E
Say him to find $100 more from hi...
support
42B1CB1EB8B22EBC
Ok, thank you for information.
support
49690BC634A9041A
Thank you.
Data recovery: SLCUT
5F99630E849394F 8
Thank you.
Data recovery: SLCUT
it is your decision. | will pass the ...
Victim
```

## Slide 16

Accounting is a double-edged sword…
The REvil Backend had a complete administration of linking IDs to Affiliates

## Slide 17


> Recovered by OCR — confidence 93/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Private Project
Password *
Trellix
```

## Slide 18

## **Full Circle:** the ID nr 22 included on the indictment


> Recovered by OCR — confidence 84/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Full Circle:
included
on the
indictment
CLERK US DISTRICT COURT
IN THE UNITED STATES DISTRICT COURT "PH GISL OF tx
FOR THE NORTHERN DISTRICT OF TEXAS |
DALLAS DIVISION 2021 AUG 11 PM 2: &|
UNITED STATES OF AMERICA
Vv.
Yaroslav Vasinskyi (01)
a/k/a Profcomserv
a/k/a Rabotnik
a/k/a Rabotnik_ New
a/k/a Yarik45
a/k/a Affiliate 22
3-21CR0366-S
FILED UNDER SEAL
INDICTMENT
Trellix
```

## Slide 19

### **Breaking His Silence**

text


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Breaking His Silence
Person in Custody: VASINSKYI, YAROSLAV Ona & PP
© CorrLinks <info@corrlinks.com> Friday, February 7, 2025 at 16:52
To: © Jon DiMaggio
External Sender - From: ("CorrLinks" <info@corrlinks.com>) Learn More
This message came from outside your organization.
This is a system generated message informing you that the above-named person is a
federal person in custody who seeks to add you to his/her contact List for
exchanging electronic messages. There is no message from the person in custody at
this time.
@ANALYST1 Trellix
```

## Slide 20

### **What We Know About the Attack**


> Recovered by OCR — confidence 89/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
What We Know About the Attack
ete
ey Biden faces ‘moment of reckoning’
\) over sp
REvil ransomware hits 1,000+ companies in MSP
supply-chain attack
By Lawrence Abrams July 2, 2021 03:56 PM
Catalin Cimpanu
ys 2021 Kaseya: More than 1,500 downstream |
ews | businesses impacted by ransomware
| attack
```

## Slide 21

**Attack Roles & Responsibilities**

## Slide 22

**“The Meeting”**


> Recovered by OCR — confidence 91/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
“The Meeting”
QTOX Meeting - 2 Days Before Attack
Unprecedented high-level coordination meeting - "they never
made a chat like that that before"
UNKN "Trump" "O_neday" "1l_zeroday" "Rabotnik"
(Tearn Leader) — (Head of Support) (Coder) (Exploit Provider) (Vasinskyi)
Division of Labor: REvil provides clean manual build
> Vasinskyi prepares attack > "Old friends" execute
Re-encoded the executable into a certificate format to avoid detection
MSP Delivery
(3) Certificate was delivered to the Managed Service Provider through the
compromised Kaseya platform
Endpoint Distribution
(4) Certificate copied from MSP to endpoint devices with random bytes added
to make the file's MD5 hash unique, reducing antivirus detection
Payload Activation
6 Certificate decoded back into executable format on the endpoint device
and ransomware deployed
rs) Evidence Cleanup
Logs and operation history were systematically deaned to remove traces
Final Deletion
(7) Operation was completely deleted from the MSP database to eliminate
forensic evidence
```

## Slide 23

### **The Hand-off**

**“Yes, the REvil team had partners who were associated with (Russian) government authorities** . “

**“I wrote to my "old friends"— here are the instructions, log in here, run the command, or find someone who will run it. I'm not going to do it”**

## Slide 24

### **Attack Motivation**

**Motive:** Disruption, crippling downstream systems, collecting intelligence, and gaining access to critic al infrastructure

## Slide 25

**Visinkyi’s Silence**


> Recovered by OCR — confidence 95/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Visinkyi’s Silence
YOUR HONOR,
| PLEAD GUILTY
TO ALL CHARGES.
\
We are not talking about that, we are not
discussing that.
```

## Slide 26

**The Russian Connection**

## Slide 27

### **Working for Russian Intelligence**

**"Before REvil... I had gotten to know people with ties to government authorities. During my work with the ransomware group, those connections deepened."**

**“I got requests from intelligence agencies (usually before elections), though I only realized this after the job was done.”**

## Slide 28

**The Job You Can't Quit**


> Recovered by OCR — confidence 84/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
The Job You Can't Quit
| seemed to be getting back on my
, feet. The school year was about to
= ® start, and | had no intention of
' —- - returning to REvil, after all. | still had
the money | hadn't spent.
```

## Slide 29

### **Detained and Questioned in Ukraine**


> Recovered by OCR — confidence 95/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Detained and Questioned in Ukraine
ONE OF THEM SHOWED ME
A SCREENSHOT ON A PHONE,
SCREENSHOTS | HAD ONCE SENT
IN TELEGRAM TO “MY OLD
FRIENDS.” | KNEW IMMEDIATLY
WHERE THIS WAS COMING FROM,
```

## Slide 30


> Recovered by OCR — confidence 95/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
WE’LL FIX YOUR PROBLEM.
REMEMBER THE STUNTS YOU
PULLED WITH REVIL? YOU
NEED TO DO THEM AGAIN.
WHAT IF
| SAY, NO?!
LISTEN. YOU’VE GOT TWO
KIDNEYS. YOU ONLY NEED ONE.
YOUR GIRLFRIEND HAS TWO TOO,
BY THE WAY, AND THEY’RE WORT
SOMETHING. THINK OF YOUR PAR-
ENTS. YOUR LOVED ONES. WHY
GO SO FAR AND PICK WRONG
OPTION WHEN THE RIGHT
ONE IS RIGHT IN
```

## Slide 31

### **Warning Email**

- 2 days before the attack


> Recovered by OCR — confidence 81/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Warning Email
tbi@fbi.gov
STyJeq Warning: Upcoming Attac
I'm contacting you in order to..,
```

## Slide 32

**WHY DIDN’T HE TALK**

## Slide 33

**Arrest & Extradition**


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
rrest & Extradition
“Family friend...”
```

## Slide 34

### **The Trophy & The Ghost**

Vasinskyi’s arrest and conviction was a big win for the DoJ But there is still more work to do Are they even looking for REvil leadership? Appears not.

## Slide 35

**HAVE YOU SEEN THIS MAN?!**


> Recovered by OCR — confidence 95/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
HAVE YOU SEEN THIS MAN?!
MISSING
UNKWN
Last Seen: July 7, 2021
just days before the REvil ransomware empire
he commanded abruptly vanished from the
internet following the Kaseya supply-chain
attack.
UNKWN was only ever online during
specific time zones, either UTC-6 or
UTC+8. (If it’s -6, it’s likely Latin
America; if +8, it could be Russia or
Asia.) He also frequently took long-
haul flights of about 6-8 hours.
After his disappearance, a theory
emerged. Trying to figure out what
happened, such as flight dates,
approximate departure and arrival
times, | gathered information over
the course of several months to try to
match it with a real identity.
-Vasinskyi
Trellix
```

## Slide 36

**The Vanishing Act**


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
The Vanishing Act
Before the attack,
UNKN recommenided
he contact KOPIbTO.
For the right price,
KOPIbTO could make
someone disappear.
New identity.
New documents.
A clean exit.
Trellix
```

## Slide 37

### **Why Disappear?**

**UNKN didn’t just disappear; HE HAD TO. The $70 million ransom demand, posted publicly by REvil after the Kaseya attack, may have gone too far. Based on everything Vasinskyi told me, it clashed with the deeper purpose of the operation. This wasn’t supposed to be about extortion. It was about disruption: crippling downstream systems, collecting intelligence, and gaining access to critical infrastructure. Putting a price tag on that risked undermining all of it.**

**People like this shouldn't get to disappear into the dark without consequence.**

## Slide 38

###### **The Silence After the Storm – What Comes Next**

**Revil should not be forgotten. Criminals don’t disappear, they evolve Law enforcement momentum changed priorities:** Initial global push didn’t evolve into lasting pressure.

**Ransomware is evolving underground** : Smaller, splintered crews now operate quietly, drawing from the same playbook.

**Without consequences, the model persists** : REvil’s legacy lives on—not as a name, but as a method.

**The real story didn’t end—it just stopped being told** .

## Slide 39

**Q&A - Let's Talk About It**
