---
title: "Cash, Drugs, and Guns Why Your Safes Aren't Safe"
speakers: ["Mark Omo James Rowlery"]
conference: "DEF CON"
conference_full: "DEF CON 33"
edition: "33"
year: 2025
source_pdf: "DEF CON 33/Mark Omo James Rowlery - Cash, Drugs, and Guns Why Your Safes Aren't Safe.pdf"
pages: 70
sha256: "bb3811cb30708f76d4febdfbf429dd3a95045e377b261ecad0823b059cf5ced1"
text_chars: 29599
ocr_pages: 1
has_ocr: true
redacted_secrets: 0
ocr_confidence: 83.4
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T07:06:47Z"
---
# Cash, Drugs, and Guns Why Your Safes Aren't Safe

**Speakers:** Mark Omo James Rowlery  
**Conference:** DEF CON 33  
**Source:** `DEF CON 33/Mark Omo James Rowlery - Cash, Drugs, and Guns Why Your Safes Aren't Safe.pdf` (70 pages)


## Slide 1

### Cash, Drugs, and Guns: Why Your Safes Aren't Safe

Abstract: When Liberty Safe was found to have provided safe unlock codes to authorities, it made us wonder; how was it even possible for Liberty to do this? Our talk will cover the vulnerabilities we found and journey into the various families of locks made by SecuRam, the OEM of safe locks used by Liberty Safe and other Safe vendors. Our exploration began with an “analog” lock from Liberty Safe but quickly expanded to SecuRam’s “digital” lock lines, where we found a debug port that allowed access to all firmware and data. Through this, we discovered that codes are stored on the externally accessible keypad, rather than securely inside the safe (as well as other issues). These locks, deployed widely in consumer, and commercial safes at major retail chains exhibit vulnerabilities that enable opening them in seconds with a Raspberry Pi.

We invite you to our session to see us crack UL-certified High-Security Electronic Locks live!

1

© 2025 Mark Omo & James Rowley. All rights reserved.

## Slide 2

## Intro/Story Time

2

© 2025 Mark Omo & James Rowley. All rights reserved.

## Slide 3

###### Who Are We?

###### Mark Omo

Director of Cat Herding

- Leads the an Engineering team

- Expert in hardware and embedded/product security

- Background in regulated device design in the Medical, Industrial, Aerospace, and Consumer market segments

**The views and opinions expressed in this presentation are solely our own and do not necessarily reflect those of our employer or any affiliated organizations.**

###### James Rowley

Senior Security Engineer

- Leads security programs

- Expert in disassembly and embedded security

- Background in regulated device design in the Medical, Industrial, Aerospace, and Consumer market segments

**This work was conducted independently by us.**

- Generally considered to be a nice guy

3

© 2025 Mark Omo & James Rowley. All rights reserved.

## Slide 4

###### Remember this incident?

●During an FBI search on Aug. 30, 2023

●Liberty Safe gave the FBI an access code for a safe

(Liberty Safe has since changed it’s policy)

Sources:

https://www.nytimes.com/2023/09/08/business/liberty-safe-codes.html https://www.locksmithledger.com/safes/news/53071785/liberty-safe-facing-backlash-over-giving-reset-code-to-fbi

4

© 2025 Mark Omo & James Rowley. All rights reserved.

## Slide 5

###### That got us thinking…

How does that even work?

How does the manufacturer even have this code?

5

© 2025 Mark Omo & James Rowley. All rights reserved.

## Slide 6

Turns out Liberty Safe uses **Securam locks Which are UL Certified High Security Safe Locks**

Securam Toplit

Sources: https://www.libertysafe.com/blogs/the-vault/safe-locks-101 https://www.libertysafe.com/pages/securam-options Certificate of Compliance UL-US-2403300-1

6

© 2025 Mark Omo & James Rowley. All rights reserved.

## Slide 7

###### Let's get one.

**Ebay** , the source of all things Bought a **Liberty Safe TopLit** ( _actually made by Securam_ )

7

© 2025 Mark Omo & James Rowley. All rights reserved.

## Slide 8

###### Terminology: **Latch** vs. **Keypad**

Safe
Keypad
Outside Part Latch
Inside part,
holds door
lock closed
Connected
via a cable

8

© 2025 Mark Omo & James Rowley. All rights reserved.

## Slide 9

###### Reverse Engineering TopLit

- **Figuring out how to dump it**

   - **Completely novel exploits** against processors and custom tooling

   - • Hardwear.io talk last year on our novel FW dump exploit on the Renesas 78K0S/Kx1+ processor used in the latch

- **Manual reverse engineering**

   - Including creating a custom disassembler!

   - No Ghidra Support :(

Source: https://hardwear.io/archives/usa-2024/

9

© 2025 Mark Omo & James Rowley. All rights reserved.

## Slide 10

###### Are there super secret backdoor codes?

###### Not really. There’s just two codes:

- **Manager Code**

   - Can change itself or the user code

   - • Can enable/disable user code

   - Can’t be disabled

- **User Code**

\```
staticconststructnvdata __at(0x0E00)k_nv1 ={
.wrong_count =0x00,
.code_manager ={// "111111"
0x31,0x31,0x31,0x31,0x31,0x31
},
.code_user ={// "123456"
0x31,0x32, 0x33,0x34,0x35,0x36
}
.user_mode =UM_ENABLED,// = 0x01
.digital_id =0xFF,
.lock_type =LT_ANALOG_A,// = 0xAA
.digital_mode =0xAA,
.data_valid =0xAA
};// initial value in new lock
\```

   - The one & only code for the lock, from a user’s perspective.

   - User-facing documentation only describes this code.

   - Can’t modify manager code, can change itself but can’t disable itself.

- **There are no other ways to open the lock**

Sources:

SafeLogic Basic Series -MANAGER- Operating Instructions; Doc.No.:BM-EC0601A130919 Analysis of firmware from EL-0601-BM mfg’d in 2018 (S/N 41807201810293003049) (at C-68)

10

© 2025 Mark Omo & James Rowley. All rights reserved.

## Slide 11

###### Who has the manager code?

- Safe vendors or independent locksmiths, such as Liberty Safe, typically set and withhold the manager code.

      - It provides an easy and non-destructive way to get back into a safe if a customer forgets their user code.

      - Of course, this makes one’s security entirely reliant on trusting a third party to actually keep their manager code secure…

- Liberty Safe offers to delete the record of this for any concerned customer.

      - Unsure of other vendors’ policies.

      - It can also be reset by resetting the latch.

      - (You should probably do this.)

- But, **not a technical vulnerability** , just a **management vulnerability** .

   - They recommend this practice in some documents

Sources:

SafeLogic Basic Series -MANAGER- Operating Instructions; Doc.No.:BM-EC0601A130919 “In some instances the Manager Code and associated Operating Instructions are not issued to the End User. In this case, simply remove this insert from the Operating Instruction.” https://www.libertysafe.com/pages/combination-removal Doc no. LS-200817 V1.01 SUPER11

© 2025 Mark Omo & James Rowley. All rights reserved.

## Slide 12

###### TopLit/SafeLogic is… actually fine!

- After reverse engineering its whole firmware, we determined that in the SafeLogic operating mode, **we didn't identify any clear, exploitable security vulnerabilities!**

- Only gap is the use of a non-constant-time compare on the unlock code.

   - We were unable to exploit it even with best in class power analysis

   - Theoretical vulnerability, but in the best case scenario still a very slow method (five-minute time out).

- **But that’s only true** **_in SafeLogic mode,_ i.e., “analog mode”.**

Source:

Analysis of firmware from EL-0601-BM mfg’d in 2018 (S/N 41807201810293003049) Note: this conclusion may not be applicable to other HW/FW versions.

12

© 2025 Mark Omo & James Rowley. All rights reserved.

## Slide 13

###### Analog Vs. Digital

- Securam’s docs describe the **SafeLogic** series as **“analog” locks** .

   - Button presses on the keypad are transmitted as analog voltage levels; the keypad has no smarts at all.

- Actuator firmware definitely has code paths for digital communication

- Turns out Securam has **“digital” locks** - the **ProLogic and ScanLogic series** .

Sources:

https://securamsys.com/collections/lock-bodies ProLogic L01 Operation Instructions V1.02: https://support.securamsys.com/hc/en-us/article_attachments/12750832079131 Analysis of firmware from EL-0601-BM mfg’d in 2018 (S/N 41807201810293003049) (at C-966, C-251)

13

© 2025 Mark Omo & James Rowley. All rights reserved.

## Slide 14

## Reverse Engineering ProLogic

Digging into Securam’s lineup

14

© 2025 Mark Omo & James Rowley. All rights reserved.

## Slide 15

ProLogic looks interesting; let's look into it

**ProLogic L02** is the **most popular model**

- **ProLogic** Lock is the **Digital line** of locks • This is the one we dig into

- • ProLogic Locks are **also UL Certified** High Security Safe Locks

Sources:

https://www.libertysafe.com/products/securam-prologic-lock15

© 2025 Mark Omo & James Rowley. All rights reserved.

## Slide 16

Turns out this was the start of a curse, we are now drowning in locks…

16

© 2025 Mark Omo & James Rowley. All rights reserved.

## Slide 17

###### Some interesting facts…

● The latch has a “reset” button, **but it doesn’t reset the codes** when a ProLogic keypad is used (vs. SafeLogic).

- ProLogic has a “recovery” mode; lets you call the

- factory and get a magic code, **this** **_does_ reset the codes.**

● OEM claims “Encryption” and “Security”

Sources:

ProLogic L01 Operation Instructions V1.02: https://support.securamsys.com/hc/en-us/article_attachments/12750832079131

17

© 2025 Mark Omo & James Rowley. All rights reserved.

## Slide 18

###### What’s in here?

- It’s a **Renesas RL78/G13**

- Turns out this is **in the PS4**

- The **gamer hackers already got this one**

   - Documented attacks to dump memory, get the debug port etc.

   - **The more widely a part is used, the more likely any flaws will be found.**

   - _Many thanks to fail0verflow!_

Sources:

https://fail0verflow.com/blog/2018/ps4-syscon/ Analysis of EC-0601A-C **L01** -100LG hardware mfg’d in **2023** (S/N 43427202310270005042) Analysis of EC-0601A-C **L02** -100LG hardware mfg’d in **2022** (S/N 4320A302210141601040)

18

© 2025 Mark Omo & James Rowley. All rights reserved.

## Slide 19

#### Reverse Engineering the Code

Sources for this section:

Primary firmware analysis of “V6.00211027” firmware from EC-0601A-CL02-100LG mfg’d in 2022 (S/N 4320A302210141601040) Confirmed exploits on “V6.00211027” firmware from EC-0601A-CL01-100LG mfg’d in 2023 (S/N 43427202310270005042)

19

© 2025 Mark Omo & James Rowley. All rights reserved.

## Slide 20

###### First, one must GET the code

- The RL78/G13 has a combined flash programming and debug function accessible on the “TOOL” pin.

- Flash mode doesn’t have any read command, but **debug mode can be used** to upload a little program to RAM that **dumps everything** .

- The hard work of documenting the debug protocol and developing security bypasses was thankfully done by fail0verflow.

- Still, no reference implementation. We’ll need to set all this up and figure out the right **glitching parameters** .

20

© 2025 Mark Omo & James Rowley. All rights reserved.

## Slide 21

###### Easy physical access to debug port

Fortunately, the programming port, which is also the debug port, is very easy to access. **Can even get at it through the battery door!**

Sources: Pictured keypad is a Securam L02 manufactured Sep 26th 2022

21

© 2025 Mark Omo & James Rowley. All rights reserved.

## Slide 22

###### Ready to dump!

- Put crowbar FET in place of core voltage cap

- Established **basic comms with debug port**

- Debug commands **shouldn’t work** because it’s disabled, but can glitch past this.

- Ready to start glitching after entering debug mode…

We built a custom software stack for the Pi Pico to do this work.

###### very special capacitor

22

© 2025 Mark Omo & James Rowley. All rights reserved.

## Slide 23

###### Easier than it looked

- Well, the **debug mode commands immediately work**

   - Guess it _wasn’t_ disabled…

- We still **don’t know the unlock code** , which must be provided to unlock full debug functionality.

   - But we might as well try all 0’s.

- **Unlock code is 0000000000**

Source: Analysis of “V6.00211027” firmware from EC-0601A-CL02-100LG mfg’d in **2022** (S/N 4320A302210141601040)

**No glitches needed.**

23

© 2025 Mark Omo & James Rowley. All rights reserved.

## Slide 24

###### Let’s dig in to the code!

24

© 2025 Mark Omo & James Rowley. All rights reserved.


> Recovered by OCR — confidence 83/100 on the text kept, 64/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
undefined
byte
vint32_t
XREF[4.
=
=
=
* FUNCTION *
undefined __stdcall menu_change_code(byte which)
<RETURN>
menu_change_code
PUSH HL
sysmenu:90007ed5(c),
sysmenu:0000807e(c),
PUSH AX
MOVW HL,SP
CALL !!oled_clear_main
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
80
121
«
Q
sVar5 = (short) ((ushort)bStack_4 << 8) >> 6;
/* This decompilation sucks bt
((uint32_t*) DFLData) [which]
passing the address of that
x*(undefined2 *)(sVar5 + -9x2b5e) = CONCATI1(key.
x*(undefined2 *)(sVar5 + -@x2b5c) = key._2_2_;
key._6.1_ = 1;
key._1_1_ = 0;
sVar5 = (short) ((ushort)bStack_4 << 8) >> 6;
uVar3 = *(undefined2 *)(sVar5 + -0x2b5c);
enc_dec_code((uint32_t *)(((short) ((ushort)bStac
(uint32_t *)&tempCodeHigh,
CONCAT13((char)((ushort)uVar3 >> 8)
if (pstack_4 == 6) {
DFLData.superCodeHigh._6_2_ =
OFLData.superCodeHigh._2_2_ =
else if (bStack_4 == 0x20) {
(undefined2) tempCc
tempCodeHigh._2_2.
```

## Slide 25

Find some interesting things…

25

© 2025 Mark Omo & James Rowley. All rights reserved.

## Slide 26

Where would you store the codes?

Safe

Keypad
Outside Part

Latch
Inside part,
holds door
lock closed
Connected
via a cable

**What do** **y ou think the** **y did?**

26

© 2025 Mark Omo & James Rowley. All rights reserved.

## Slide 27

Yep they put them on the outside

**Super Code** is Right Here **Stored in the Keypad**

Source: Analysis of “V6.00211027” firmware from EC-0601A-CL01-100LG mfg’d in **2023** (S/N 43427202310270005042) Note: this may not be applicable to other HW/FW versions.

27

© 2025 Mark Omo & James Rowley. All rights reserved.

## Slide 28

## What about the encryption?

They said there was encryption…

28

© 2025 Mark Omo & James Rowley. All rights reserved.

## Slide 29

###### What about Encryption?

- The super code **is stored encrypted** • Super Code is kind of like root

- • Encrypted with XXTEA (symmetric cipher) and a 128-bit key

- **How could we possibly decode it?**

**Encryption key** is **stored here** (plus 96 bits of _static key_ )

Source: Analysis of “V6.00211027” firmware from EC-0601A-CL01-100LG mfg’d in **2023** (S/N 43427202310270005042) Note: this may not be applicable to other HW/FW versions.

29

© 2025 Mark Omo & James Rowley. All rights reserved.

## Slide 30

Source:

###### ScanLogic Basic

- **Doesn't even bother with encryption!**

- • Debug port unlocked on this model too!

**999999**

**876543**

Analysis of dataflash from FPC-1808-v5 mfg’d in **2023** (S/N 51825392312220123051)

30

© 2025 Mark Omo & James Rowley. All rights reserved.

## Slide 31

## The Attack

31

© 2025 Mark Omo & James Rowley. All rights reserved.

## Slide 32

We built this custom tool

32

© 2025 Mark Omo & James Rowley. All rights reserved.

## Slide 33

###### It reaches way up in there

33

© 2025 Mark Omo & James Rowley. All rights reserved.

## Slide 34

And connects to the debug port

34

© 2025 Mark Omo & James Rowley. All rights reserved.

## Slide 35

Goes through a **lengthy complex process** : ● Booting the processor in debugging mode ● Injecting a code blob

First:

Reset the processor Boot into debug mode (with debug key 000000000)

Second:

Patch the debug RAM with custom code

● Reading out the memory

Third:

Dump data storage region over debug port

**This takes 0.8s**

35

© 2025 Mark Omo & James Rowley. All rights reserved.

## Slide 36

###### We call this attack **CodeSnatch**

36

© 2025 Mark Omo & James Rowley. All rights reserved.

## Slide 37

##### Demo Time!

37

© 2025 Mark Omo & James Rowley. All rights reserved.

## Slide 38

Ok… but who uses these things?

Note: We have not purchased or tested locks from the following vendors, only identified that they sell the same models of locks we examined and found vulnerable to at least one attack.

Our attacks were tested on locks with manf dates ranging from May 2014 to Mar 2025.

38

© 2025 Mark Omo & James Rowley. All rights reserved.

## Slide 39

###### Safe companies like these

“[Securam] holds about 70% of the high-security smart lock systems market [...] with approximately 3 million customers in North America”

Dec. 2021; EastHouse tour by China National Hardware […] Commercial Assoastion

Sources:Manf and distributor websitesCompanies selling SecuRam L01, L02, E66, OL66 and/or ScanLogic Basic

China National Hardware, Electrical and Chemical Products Commercial Association. (December 30, 2021). Inspection of EastHouse. WeChat official account. (Note 3M includes © 20all 25 Mark Omo & James Row not just vulnerable product s)ley. All rights reserved.

39

## Slide 40

## Ok but who else? Anything Serious?

40

© 2025 Mark Omo & James Rowley. All rights reserved.

## Slide 41

###### Pharmaceutical Safe Manufacturers

Used by some of  the largest
SecuRam commercial safe providers
ProLogic

> Sources: Companies selling SecuRam L01, L02, E66, OL66 and/or ScanLogic Basic https://narcsafe.com/ https://www.cennox.com/what-we-do/traditional-safes/ © 2025 Mark Omo & James Rowley. All rights reserved.

41

© 2025 Mark Omo & James Rowley. All rights reserved.

## Slide 42

###### SecuRam in the wild on Pharmacy Safes

2x Bonus
ProLogic

SecuRam
ProLogic
Sources:
https://easthouse.net/about
https://www.facebook.com/ReevesUsedFixtures/photos

https://www.wsaz.com/content/news/CVS-pharmacies-in-West-Virginia-added-time-delayed-safes-to-all-stores-566054271.html @ 0:31

42

© 2025 Mark Omo & James Rowley. All rights reserved.

## Slide 43

Also used in cash drop safes

Papa Murphy's
T-Mobile
Taco Del MarSubway https://www.auctionfactory.com/archive_item_detail.php?item=103972Sources:

Sources: https://www.auctionfactory.com/archive_item_detail.php?item=103972Sources: https://www.assetauctionsgroup.com/archive_item_detail.php?item=56310

43

© 2025 Mark Omo & James Rowley. All rights reserved.

## Slide 44

###### Mitigations

There are **no Mitigations** for existing users for CodeSnatch that we can identify, **except for SW update**

While going back and forth with SecuRam they sent us a lock with software “V6.00231223” (Presumably Dec 23 2023) that appeared to remove Keypad side code storage.

**But we have not seen this version in the wild** - a lock purchased a month ago (July 2025, made in March 2025) had a non-zero debug key, this does not effectively mitigate this attack. We added this new value to our tool.

Sources:

Securam communication on Apr 27, 2024 Lock FW V6.00241217 (Dec 17th 2024) 44

© 2025 Mark Omo & James Rowley. All rights reserved.

## Slide 45

###### Field Firmware Update

The Keypad and Latch **firmware can be updated in the field** Remember this tool? It could be used to update the firmware in the locks we examined!

An inexpensive service tool could be used to update the firmware.

45

© 2025 Mark Omo & James Rowley. All rights reserved.

## Slide 46

But… Is there an easier way in?

46

© 2025 Mark Omo & James Rowley. All rights reserved.

## Slide 47

###### Lock Recovery

Locks have this **Recovery** feature

“System **Recovery** is used to **delete all the codes** on the ProLogic or ScanLogic and set the Entrypad and its linked lock back to back to a factory default state”

“To Perform a Recovery, the Locksmith must call SECURAM, during business hours to speak with a live customer support representative.”

Sources:

https://support.securamsys.com/hc/en-us/articles/6185820502043-ProLogic-Recovery

47

© 2025 Mark Omo & James Rowley. All rights reserved.

## Slide 48

###### How Does it work?

- You enter the recovery code

   - (999999 by default)

- You are shown a recovery challenge

- You call Securam to get the correct response • (limited to registered Locksmiths)

- Type in the code

- All lock codes are reset

Sources:

https://support.securamsys.com/hc/en-us/articles/6185820502043-ProLogic-Recovery

48

© 2025 Mark Omo & James Rowley. All rights reserved.

## Slide 49

###### I am sure this is implemented securely

Recovery  Recovery Code
Static Data
Challenge Encryption Code
XXTEA-128
Symmetric Cypher
Challenge
Response

**Anyone can recover a lock**

Source:

Analysis of “V6.00211027” firmware from EC-0601A-CL02-100LG mfg’d in **2022** (S/N 4320A302210141601040)

49

© 2025 Mark Omo & James Rowley. All rights reserved.

## Slide 50

Demo “To Perform a Recovery, the Locksmith must call SECURAM [...]”

50

© 2025 Mark Omo & James Rowley. All rights reserved.

## Slide 51

###### Demo (backup)

51

© 2025 Mark Omo & James Rowley. All rights reserved.

## Slide 52

###### What about Recovery/Encryption Code?

"Now, the **encryption key is rarely changed** , at least in the North American market. **No one ever changes this key** . You can change it. But most people leave it as default, and that's fine.

The **recovery code** , those six nines that we saw previously, is **also usually never changed** because there is **no security risk** in leaving as six nines as we saw previously. We have to decrypt that key. So, usually those things don't change."

Source:

However…

**Some** **_printed_ manuals do recommend changing recovery and encryption codes.** _Good!_ We were unable to find this recommendation in any materials published online.

“Webinar ProLogic L02 - Locksmith version with Drill Points”

52

© 2025 Mark Omo & James Rowley. All rights reserved.

## Slide 53

###### ResetHeist Mitigations

We call this attack **ResetHeist**

It require **no tools or hardware**

You can **mitigate** ResetHeist by **changing your Recovery Code and Encryption Code**

Changing the recovery code requires calling Securam

53

© 2025 Mark Omo & James Rowley. All rights reserved.

## Slide 54

###### Confirmed Vulnerable Products

Lock CodeSnatch ResetHeist
EC-0601A-CL01-100LG - mfg’d Oct 2023
L01
S/N 43427202310270005042/FW V6.00211027
EC-0601A-L02-C-II -  mfg’d Mar 2025
S/N 43205392503210684057/FW V6.00241217
EC-0601A-CL02-100LG - mfg’d Sep 2024
S/N 43205392409201444056/FW V6.00231214
EC-0601A-CL02-100LG - mfg’d Oct 2022
L02
S/N 4320A302210141601040/FW V6.00211027
EC-0601A-L02 - mfg’d Oct 2019  (Cennox SR2)
S/N 22306361910251202045/FW V4.13180928
EC-0601A-L02 -  mfg’d May 2014
S/N 19506091405141202050/FW V1.83130707
EC-0601A-E66-O - mfg’d Jul 2021
E66
S/N 33406362107160085055/FW V4.12200930
EC-0601A-OL66 - mfg’d Jun 2021
L66
S/N 23406362106250084052/FW V5.01200811
FPC-1808-v5 (ScanLogic Basic) - mfg’d Dec 2023 (Does not
ScanLogic Basic S/N 51825392312220123051/FW V3.0220617 &  support
V1.20190604 recovery)
EVERY LOCK WE TESTED  was vulnerable to ResetHeist.

54

© 2025 Mark Omo & James Rowley. All rights reserved.

## Slide 55

## Disclosure Timeline

55

© 2025 Mark Omo & James Rowley. All rights reserved.

## Slide 56

###### Disclosure Timeline

Nov. 2024 **April 2024** We reach out again 2025 Aug 2025 **Detailed Technical** “We will refer this matter to DEF CON 33 **disclosure** our counsel [...]" - Securam **15 months after disclosure Almost 2 years of work**

2024

Dec 2023 We Start Research

June 2025 Accepted to DC33 Requested comment again

###### Dec 2024

Sep 2023 Mar 2024 **May 2024** EFF Reaches out on NYT Liberty Safe Informed Securam “We will refer this matter to our our behalf offered to Article about our research counsel for trade libel if you choose include statement and invited the route of public announcement or collaboration disclosure" - Securam

July 2025 First contact from Securam’s counsel

###### **"The attack method you have indicated is not new."**

(-Securam, referring to the Little Black Box and Phoenix Tool)

56

© 2025 Mark Omo & James Rowley. All rights reserved.

## Slide 57

Securam Communications May 2024

- “[...] **we don’t believe it is appropriate [for you] to communicate to our customers of any concern** .  Your disclosure to our customers would interfere with our relationship with the customers.”

- “We object to your sharing or disclosure of your ‘findings’ even at a conference as such **disclosure** as you presented would be misleading and **damaging to SecuRam’s goodwill and reputation** .  We **will refer this matter to our counsel** for trade libel if you choose the route of public announcement or disclosure.”

Source: Securam communication; May 3rd and 21st 2024 Emphasis added

57

© 2025 Mark Omo & James Rowley. All rights reserved.

## Slide 58

###### Mitigation Timeline

Securam did not share plans or timelines for mitigations with us.

58

© 2025 Mark Omo & James Rowley. All rights reserved.

## Slide 59

## Prior Art

59

© 2025 Mark Omo & James Rowley. All rights reserved.

## Slide 60

###### Prior Art; “Locksmith only” tools

###### **Little Black Box** ; tool that can open:

- **SecuRam**

   - Prologic models L01, B01, L02, L22, L62, L66 and L68 before Dec 16th 2016

- **LaGard**

   - LaGard Basic Series, 39E, and 66E up through mid-2018.

   - LG Basic, 33E, SafeGard 3600 & 3650, LgCombo from Jan. 2000 – Jan. 2016

- **Sargent & Greenleaf**

   - Sargent & Greenleaf 6120 locks from Jan. 2000 – Jan. 2016

   - S&G Spartan and Titan until February 2016

   - S&G 6123 Series Locks from 2000 until January 2016.

- **Amsec** locks

   - AMSEC – ESL5 & ESL15 series from 2000 to at least Feb. 2020

- **DormaKaba** locks

   - DormaKaba Auditcon 252 & 552 series until 2019

###### **Phoenix Tool** ; another tool that can open:

- **AMSEC**

   - ESL-10​, ESL-20

- **Sargent & Greenleaf**

   - 6120 ('98 - '13), 6121, 6123 ('98 - '13), Biometric, Titan PivotBolt *, Spartan PivotBolt **, Titan D-Drive *, Spartan D-Drive **

- **Sentry Safe​**

   - SF Series​

- **Lagard** locks

   - Basic/Basic Plus (through 2019), LGBasic (green board), LGBasic II (blue board through 2019), LGCombo, ComboGard 33E, SafeGard 3650, ComboGard Pro 39E, 3801, 3802, 4200, 3040, 3260, 3765, 3740, 2441 Mechanical Redundant, AuditGard 66E, LPAudit, LGAudit, 6441 Mechanical Redundant

**Safe Locks with** **<u>known exploited vulnerabilities</u>**

<u>Would</u> _<u>you</u>_ <u>use software with known vulns?</u>

Sources:

https://1010security.com/catalogsearch/result/?q=little%20Black%20Box https://www.taylortechtools.com/phoenix

Private SecuRam communication

60

© 2025 Mark Omo & James Rowley. All rights reserved.

## Slide 61

###### Prior Art; Others

- In 2016 Somerset recon demonstrated a Bluetooth sniffing attack against the ProLogic B01, resulting in unlock capability

- Separately, they demonstrated a rapid unlock capability against a ECSL-0601A latch unit using a specialized tool

- Deviant Ollam’s talk on locksmith tools (among other things) at PancakeCon 2024: <u>youtube.com/watch?v=mi3WIwq86t8</u>

Sources:

https://www.somersetrecon.com/blog/2016/10/14/electronic-safe-lock-analysis-part-2https://www.youtube.com/watch?v=hOZkViOOiKE

61

© 2025 Mark Omo & James Rowley. All rights reserved.

## Slide 62

## Summary and Takeaways

Our opinions on lock safety

62

© 2025 Mark Omo & James Rowley. All rights reserved.

## Slide 63

###### Does it really matter?

**Is this a legitimate threat** to security?

- **Yes** - organized crime rings could make this tool, or do the reset thing

###### Credit card skimmers

   - They **already make credit card skimmers**

   - • And sell and use **tools to steal cars** via CAN hacking

- So could nation-state threat actors.

- **Quick to open means it’s actually practical**

###### Tool to steal cars via CAN Bus

Sources:

https://apnews.com/general-news-e254277cefa44657a2427ec0aa93999b https://www.designworldonline.com/skim-reaper-detecting-credit-card-skimmers-one-swipe-at-a-time/ https://kentindell.github.io/2023/04/03/can-injection/

63

© 2025 Mark Omo & James Rowley. All rights reserved.

## Slide 64

###### Threat Modeling

The **codes** need to be **inside the safe**

• (Safes are designed to protect the inside)

**Anything else can become a weak point** Safe codes are generally short (6-8 digits, 20-25 bit of security) **hashing is ineffective**

64

© 2025 Mark Omo & James Rowley. All rights reserved.

## Slide 65

###### What Went Wrong?

Where was the biggest failure?

- Securam for it’s design?

- Safe OEMs for not vetting it?

- UL..?

**Almost…**

**Standards** for electronic physical security products **lag significantly behind the state of the art** _You should be able to trust the certification_

65

© 2025 Mark Omo & James Rowley. All rights reserved.

## Slide 66

###### Certified Locks

###### **Little Black Box :**

- **SecuRam**

   - **Prologic models L01, B01, L02, L22, L62, L66 and L68 before Dec 16th 2016**

- **LaGard**

   - **LaGard Basic Series, 39E, and 66E**

   - **LG Basic, 33E, SafeGard 3600 & 3650, LgCombo**

- **Sargent & Greenleaf**

   - **Sargent & Greenleaf 6120 locks**

   - **• S&G Spartan and Titan**

   - **S&G 6123 Series Locks**

- **Amsec locks**

   - **AMSEC – ESL5 & ESL15 series**

- **DormaKaba locks**

   - **DormaKaba Auditcon 252 & 552 series**

###### **Locks that are UL Type 1 certified**

###### **Phoenix Tool :**

- **AMSEC**

   - **ESL-10​, ESL-20**

- **Sargent & Greenleaf**

   - **6120, 6121, 6123, Biometric, Titan PivotBolt, Spartan PivotBolt, Titan D-Drive, Spartan D-Drive**

- **Sentry Safe​**

   - **SF Series​**

- **Lagard locks**

   - **Basic/Basic Plus, LGBasic, LGBasic II, LGCombo, ComboGard 33E, SafeGard 3650, ComboGard Pro 39E, 3801, 3802, 4200, 3040, 3260, 3765, 3740, 2441**

**Mechanical Redundant, AuditGard 66E, LPAudit, LGAudit, 6441 Mechanical Redundant**

Sources:

UL: https://productiq.ulprospector.com/en

66

© 2025 Mark Omo & James Rowley. All rights reserved.

## Slide 67

###### Certification - Looking Forward

###### **Should require:**

- Secure Product Development Framework (SPDF)

- • Threat Modeling/Risk Assessment

- • Detailed flow and functional descriptions

   - Independent white box/black box cybersecurity testing FIPS/Common Criteria type side channel testing

-

-

###### **Following examples from:**

- Medical device field/FDA

   - FDA; Cybersecurity in Medical Devices

   - • IEC 81001-5-1; Health software systems safety, effectiveness and security

- Automotive field/NHTSA

   - NHTSA; Cybersecurity Best Practices for the Safety of Modern Vehicles

- ISO/SAE 21434; Road vehicles — Cybersecurity engineering

67

© 2025 Mark Omo & James Rowley. All rights reserved.

## Slide 68

Bonus; Chinese Government Backdoors There been been a lot of hype in the media about Chinese government mandated backdoors

**We found no evidence of any such feature in any locks we examined** (except for those in the manual)

**Don’t believe the hype Bad Design ≠ Government Backdoors**

68

© 2025 Mark Omo & James Rowley. All rights reserved.

## Slide 69

EFF / Coder’s Rights Project **Big thanks to the EFF’s Coder’s Rights Project for representing us!**

They helped us understand our rights and our exposure, and gain the confidence to disclose this important information.

69

© 2025 Mark Omo & James Rowley. All rights reserved.

## Slide 70

# Questions?

70

© 2025 Mark Omo & James Rowley. All rights reserved.
