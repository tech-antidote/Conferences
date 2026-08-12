---
title: "AutoSpill Zero Effort Credential Stealing from Mobile Password Managers"
speakers: ["Ankit Gangwal", "Shubham Singh", "Abhijeet Srivastava"]
conference: "Black Hat"
conference_full: "Black Hat Europe 2023"
edition: "Europe"
year: 2023
source_pdf: "Black Hat Europe 2023 slides/Ankit Gangwal, Shubham Singh, Abhijeet Srivastava_ AutoSpill Zero Effort Credential Stealing from Mobile Password Managers.pdf"
pages: 66
sha256: "b97ab6ed937f3083bf18197b03d92b9ad9d422d296935edfeb204e9cbe235ecb"
text_chars: 23569
ocr_pages: 21
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:10:08Z"
---
# AutoSpill Zero Effort Credential Stealing from Mobile Password Managers

**Speakers:** Ankit Gangwal, Shubham Singh, Abhijeet Srivastava  
**Conference:** Black Hat Europe 2023  
**Source:** `Black Hat Europe 2023 slides/Ankit Gangwal, Shubham Singh, Abhijeet Srivastava_ AutoSpill Zero Effort Credential Stealing from Mobile Password Managers.pdf` (66 pages)


## Slide 1

AutoSpill Zero Effort Credential Stealing from Mobile Password Managers

Ankit Gangwal, Shubham Singh, Abhijeet Srivastava IIIT Hyderabad, IN

**_Disclaimer_** _: All logos, photos, etc. used in this presentation are the property of their respective copyright owners and are used here for educational purposes only._

#BHEU @BlackHatEvents

## Slide 2

# Introduction

#BHEU @BlackHatEvents

2

## Slide 3

# Introduction

Internet
Information Age

#BHEU @BlackHatEvents

3

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
black hat .
mackhat Introduction
: et
48,0,0) (iF (Gog
C8. document, dea,
rk
d}
Agent .A.8,C,.0 + we
. ontext s{0} a ea
Uglied
= snarl his,a) Wee ae
fa-selector’—bua(tns, selector atte
|} pushStack:t
(a,b) {return e.each( th 12,0), ready
oe 1D 16. call (argunent
#. the extend-e.fn.extend-tunct iont
} a) (deilch , falc; if Lent) cont
Guery tf) ceeturn.e}, isReady: |1, readywait
eatenic, \e)),e.fn.triggertie(c) .triggert
«. (eady, L)ielse Af(c.attachevent {6
daderay: Array AsAreay| | function(a) {ret
), de® lainddject: function(a){it('e e typed
mee yect funct (a){for(var.b.in.a)reture
C estace(o,"€)- eeplaeas: <replace(,
Fd anynce false” ,d.10 et (c)) Pea
‘tase vrata) {return.a.repiace(%,
caaactae for tsgens it (ce seplytalgr a
jon(a,b)ivar.c
ib nananeray eturn-1) merge: tunctianl hie Oe ae
os. sates f});return — ——-"
pap, concat.2pply'
{var ina. eng
ech: funct
in a. fas const recta ae
(2,010
a) eety
event Lis
function )4var
```

## Slide 4

# Introduction

### Connect the world

#BHEU @BlackHatEvents

4

## Slide 5

# Introduction

### Become the world

#BHEU @BlackHatEvents

5

## Slide 6

# Introduction

### Connecting to the Internet

Different devices

#BHEU @BlackHatEvents

6

## Slide 7

# Introduction

### Desktop vs. mobile

Desktop Mobile
43% 57%

Worldwide device market share - 2023

#BHEU @BlackHatEvents

Data source: https://gs.statcounter.com/platform-market-share/desktop-mobile-tablet/worldwide/#monthly-202301-202311-bar7

## Slide 8

# Introduction

### Desktop vs. mobile

Desktop Mobile
35% 65%

Worldwide Internet traffic share - Q1 2023

#BHEU @BlackHatEvents

8

Data source: https://www.similarweb.com/platforms/

## Slide 9

Introduction

Mobile devices
65
63
59.54
60
55.78
55
52.4 52.6 52.2
51.12
50 48.33
45
40 38.43
35
2015 2016 2017 2018 2019 2020 2021 2022 2023
Worldwide mobile Internet traffic trend
%

#BHEU @BlackHatEvents

Data source: https://www.statista.com/statistics/277125/share-of-website-traffic-coming-from-mobile-devices/9

## Slide 10

# Introduction

### The big shift - Oh my!

#BHEU @BlackHatEvents

10

## Slide 11

# Introduction

The big shift - Oh my!

#BHEU @BlackHatEvents

11

## Slide 12

# Introduction

The big shift - Oh my!

#BHEU @BlackHatEvents

12

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pif hat
EUROPE 2023
‘BeSB<O
© B aH:
ORPBAOLZ
SG=@O@AQD
©@6e@G4
S &
Bom ge Eavoo
12
```

## Slide 13

# Introduction

The big shift - Oh my!

#BHEU @BlackHatEvents

13

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Cc
Oo
1s)
=)
oO
O
a)
=
EUROPE 2023
The big shift - Oh my!
pif hat
SseG@ gs
¢€e¢g g| 0S ©
Ce 2 i
a) i ¢ & &
© # ( A Ss
®) @Z ‘4 3 oo.
Ow vy BF awn
BOO@OW asd
GP?BSday tego
\
13
```

## Slide 14

# Introduction

### The big shift - Oh my!

#BHEU @BlackHatEvents

14

## Slide 15

# Introduction

The big shift - Oh my!

#BHEU @BlackHatEvents

15

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Qa
blackhat Introduction
= @CBS NEWS
U.S. >
Common passwords like "123456" and
"admin" take less than a second to
crack, research shows
BY CAITLIN O'KANE Po
INNOVATION * CYBERSECURITY
These Are The
World's Most Hacked
Passwords -- Is
Yours On The List?
Kate O'Flaherty Senior Contributor ©
Cybersecurity and privacy journalist
15
‘Password,’ ‘Monkey’ and the Other Terrible
Passwords We Choose
CG Share full article ae WW
This year’s worst passwords, according to one creator of security applications, include
“starwars,” “iloveyou,” “monkey,” “hello,” “freedom,” “qazwsx” and “trustnol.” Damian
Dovarganes/Associated Press
By Niraj Chokshi
Menu +
TECH / GOOGLE / SECURITY
Google is on a mission to stop you from reusing passwords
/ It’s adding its Password Checkup tool to the Security
Checkup dashboard
By Jay Peters, a news editor who writes about technology, video games, and virtual worlds. He’s
submitted several accepted emoji proposals to the Unicode Consortium.
Jun 23, 2020, 5:30 PM GMT+5:30 | [2 0 Comments / 0 New
```

## Slide 16

# Introduction

## PASSWORD MANAGERS

#BHEU @BlackHatEvents

16

## Slide 17

# Introduction

Log in with

#BHEU @BlackHatEvents

17

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Qa
blackhat Introduction
Il Fal B 14:43
Cancel
Log in with
& Google
Username or Email
Password
Log in
```

## Slide 18

# Introduction

Log in with

#BHEU @BlackHatEvents

18

## Slide 19

# Background

### Password Managers (PMs)

Store & manage

Choose stronger passwords

Automatically fill (autofill)

User
xxxx

#BHEU @BlackHatEvents

19

## Slide 20

# Background

### PMs are becoming increasingly common Computers as well as mobile devices (e.g., smartphones) [1, 2]

- [1] Sean Oesch, Anuj Gautam, and Scott Ruoti, “The Emperor’s New Autofill Framework: A Security Analysis of Autofill on iOS and Android,” In Annual Computer Security Applications Conference. 996-1010, 2021.

- [2] Sean Oesch and Scott Ruoti, “That was then, this is Now: A Security Evaluation of Password Generation, Storage, and Autofill in Browser-based Password Managers,” In USENIX Security Symposium. 2165-2182, 2020. 20

#BHEU @BlackHatEvents

## Slide 21

# Background

PMs on computers Generally, implemented as browser extension

#BHEU @BlackHatEvents

21

## Slide 22

# Background

PMs on computers Generally, implemented as browser extension Handles everything Storing, rendering, prompting, autofilling

#BHEU @BlackHatEvents

22

## Slide 23

# Background

PMs on computers Generally, implemented as browser extension Handles everything Storing, rendering, prompting, autofilling Autofill ceremony involves only two parties

#BHEU @BlackHatEvents

23

## Slide 24

# Background

PMs on mobile OSes (e.g., Android) System-wide autofill frameworks & sandboxing Autofill ceremony involves at least three parties

#BHEU @BlackHatEvents

24

## Slide 25

# Background

PMs on mobile OSes (e.g., Android) System-wide autofill frameworks & sandboxing Autofill ceremony involves at least three parties

#BHEU @BlackHatEvents

25

## Slide 26

# Background

PMs on mobile OSes (e.g., Android) System-wide autofill frameworks & sandboxing Autofill ceremony involves at least three parties

#BHEU @BlackHatEvents

26

## Slide 27

# Background

PMs on mobile OSes (e.g., Android) System-wide autofill frameworks & sandboxing Autofill ceremony involves at least three parties

#BHEU @BlackHatEvents

27

## Slide 28

# Background

PMs on mobile OSes (e.g., Android) System-wide autofill frameworks & sandboxing Autofill ceremony involves at least three parties

#BHEU @BlackHatEvents

28

## Slide 29

# Background

Mobile OSes have developed WebView controls Act as a minimalistic browser

Empower an app to render web content within itself

Prevents redirection to main browser app

#BHEU @BlackHatEvents

29

## Slide 30

# Background

Mobile OSes have developed WebView controls Act as a minimalistic browser

Empower an app to render web content within itself Prevents redirection to main browser app

#BHEU @BlackHatEvents

30

## Slide 31

# AutoSpill

#BHEU @BlackHatEvents

31

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ok
Y)
O
—
=)
<<
ion
Cc
pifechat
EWIROPE 20
31
```

## Slide 32

# AutoSpill

### PM is invoked to fill fields in an app

#BHEU @BlackHatEvents

32

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2
blackhat AutoSpill
PM is invoked to fill fields in an app
App
MH
PPrrrrerrrrrrr errr ts
euueeeeeeeeeeeeeeeny
Perrrrrr rrr errr ttt
PM)
|
Prompt
fi
Select &
authorise
Fill
!
32
```

## Slide 33

# AutoSpill

### PM is invoked to fill fields in an app

#BHEU @BlackHatEvents

33

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2 |
blackhat AutoSpill
(S
o Prompt
| Select &
_—_——
Q authorise
ro
<x
feXeXe)
; elements
33
```

## Slide 34

# AutoSpill

### PM is invoked to fill fields in a WebView

#BHEU @BlackHatEvents

34

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2
blackhat AutoSpill
PM is invoked to fill fields in a WebView
=
=
=
{2
os a
“2 ®
x= =
= iusername }
<x SU,
: password
PIII.
App
elements |
34
```

## Slide 35

# AutoSpill

### PM is invoked to fill fields in a WebView

#BHEU @BlackHatEvents

35

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pif hat
EUROPE 2023
AutoSpill
PM is invoked to fill fields in a WebView
(S
Ou
=
x
>
| @
° >
2a $
x= =
[ok
Qa
<
_——————
Prompt
H
Select &
authorise
|
Fill
Peres
Perera
errr t
35
```

## Slide 36

# AutoSpill

### PM is invoked to fill fields in a WebView Example 1

“Login with Apple/Facebook/Google/etc.” buttons

#BHEU @BlackHatEvents

36

## Slide 37

# AutoSpill

### PM is invoked to fill fields in a WebView Example 2

Logging in OneDrive app, which supports 3rd party authentication

#BHEU @BlackHatEvents

37

## Slide 38

# AutoSpill

PM is invoked to fill fields in a WebView Example 2

Logging in OneDrive app, which supports 3rd party authentication

#BHEU @BlackHatEvents

38

## Slide 39

# AutoSpill

PM is invoked to fill fields in a WebView Example 2

Logging in OneDrive app, which supports 3rd party authentication

#BHEU @BlackHatEvents

39

## Slide 40

# AutoSpill

### Credential leakage from H<sup>W</sup> to HA = AutoSpill

Violation of secure autofill process Responsibility for leakage is stranded between PM and Android

#BHEU @BlackHatEvents

40

## Slide 41

# AutoSpill

### Credential leakage from H<sup>W</sup> to HA = AutoSpill

A real-world credential AutoSpill from Facebook page

#BHEU @BlackHatEvents

41

## Slide 42

# AutoSpill

Biggest benefit (rather risk!) of AutoSpill + Phishing is not required

1. Benign app with input fields

2. Invokes H<sup>W</sup>

3. Code for processing

- + No malicious code in app Reside on official app store

#BHEU @BlackHatEvents

42

## Slide 43

# AutoSpill -Investigation

Created a custom autofill service Information exchanged during autofill ceremony

#BHEU @BlackHatEvents

43

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
€ . oo.
blackhat = AutoSpill - Investigation
Created a custom autofill service
Information exchanged during autofill ceremony
: Autofill
App Android Service
43
```

## Slide 44

# AutoSpill -Investigation

Created a custom autofill service Information exchanged during autofill ceremony _1. Autofill request from Android to autofill service_

#### _AssistStructure_ [3]

[3] AssistStructure, https://developer.android.com/reference/android/app/assist/AssistStructure

#BHEU @BlackHatEvents

44

## Slide 45

# AutoSpill -Investigation

Created a custom autofill service Information exchanged during autofill ceremony _1. Autofill request from Android to autofill service 2. Processing and response from autofill service_

#### _AssistStructure_ [3]

_Datasets_ [4]

[3] AssistStructure, https://developer.android.com/reference/android/app/assist/AssistStructure [4] Datasets, https://developer.android.com/reference/android/service/autofill/Dataset

#BHEU @BlackHatEvents

45

## Slide 46

# AutoSpill -Investigation

_1. Autofill request from Android to autofill service_

46

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pif hat
EUROPE 2023
AutoSpill - Investigation
[ FillRequest |
1. Autofill request from :
FillContext
FocusedID: 1073741826:196608
Android to autofill service :
[ AssistStructure ]
¥
[ WindowNode }
[ 1. RootView }
I
v v
1.1 NativeView
ChildrenCount: 2
AutoFillld: 1073741829
WebDomain: null
1.2 WebView
ChildrenCount: 2
AutoFillld: 1073741826
WebDomain: m.facebook.com
v
v
v
v
1.1.1 Username
1.1.2 Password
AutoFillld: 1073741824
Dimension: 300x100
AutofillType: 1
AutofillHints: null
WebDomain: null
AutofillOptions: null
Htmllnfo: null
ViewID: 2131231192
InputType: 1 (text)
AutoFillld: 1073741825
Dimension: 300x100
AutofillType: 1
AutofillHints: null
WebDomain: null
AutofillOptions: null
Htmllnfo: null
ViewID: 2131231055
InputType: 129 (password)
1.2.1 Username
1.2.2 Password
AutoFillld: 1073741826:196608
Dimension: 300x100
AutofillType: 1
AutofillHints: on
WebDomain: null
AutofillOptions: null
Htmllnfo: [Pair{name email},
Pair{type email},
Pair{label Mobile
number or email address},
Pair{ua-autofill-hints null},
Pair{id m_login_email},
Pair{maxLength 2147483647}]
View ID: -1
InputType: 0
AutoFillld: 1073741826 :196609
Dimension: 300x100
AutofillType: 1
AutofillHints: on
WebDomain: null
AutofillOptions: null
Htmlinfo: [Pair{name pass},
Pair{type password},
Pair{label Password},
Pair{ua-autofill-hints null},
Pair{id m_login_email},
Pair{maxLength 2147483647}]
ViewD: -1
InputType: 0
```

## Slide 47

# AutoSpill -Investigation

### _1. Autofill request from Android to autofill service_

47

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Q
blackhat = AutoSpill - Investigation
1. Autofill request from
Android to autofill service
v
1.1 NativeView
ChildrenCount: 2
AutoFillld: 1073741829
WebDomain: null
FillRequest
FillContext
FocusedID: 1073741826:196608 mameay,
=.
Y bbb LETT Tree
[ AssistStructure ]
[ WindowNode }
[ 1. RootView
I
v a
1.2 WebView >
ChildrenCount: 2 o*
AutoFillld: 1073741826 o”
WebDomain: m.faceboog Bom
I L,s*
¥ Y ¥ ° Y
1.1.1 Username 1.1.2 Password 1.2.1 Username yw 1.2.2 Password
AutoFillld: 1073741824 AutoFillld: 1073741825 AutoFillld: 1073741826:196608 AutoFillld: 1073741826 :196609
Dimension: 300x100 Dimension: 300x100 Dimension: 300x100 Dimension: 300x100
AutofillType: 1 AutofillType: 1 AutofillType: 1 AutofillType: 1
AutofillHints: null AutofillHints: null AutofillHints: on AutofillHints: on
WebDomain: null WebDomain: null WebDomain: null WebDomain: null
AutofillOptions: null AutofillOptions: null AutofillOptions: null AutofillOptions: null
Htmllnfo: null Htmllnfo: null Htmllnfo: [Pair{name email}, Htmllnfo: [Pair{name pass},
; Pair{type email}, Pair{type password},
View ID: 2131231192 ViewID: 2131231055 Pair{label Mobile Pair{label Password},
. . number or email address}, Pair{ua-autofill-hints null},
InputType: 1 (text) InputType: 129 (password) Pair{ua-autofill-hints null}, Pair{id m_login_email},
Pair{id m_login_email}, Pair{maxLength 2147483647}]
Pair{maxLength 2147483647}]
View ID: -1 ViewlD: -1
InputType: 0 InputType: 0
```

## Slide 48

# AutoSpill -Investigation

### _2. Request processing and response from autofill service_

#BHEU @BlackHatEvents

48

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Q
black hat
EUROPE 2023
Add WebDomain to
DomainCheckList
Ly
Traverse
AssistStructure to find
domain of request
A
Use FocusedID to
identify input field that
triggered the request
LN
Autofill service
receives FillRequest
ene - - - - tee
Request
processing: Pass 1
AutoSpill - Investigation
2. Request processing and response from autofill service
48
```

## Slide 49

# AutoSpill -Investigation

### _2. Request processing and response from autofill service_

#BHEU @BlackHatEvents

49

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
€ . oo.
blackhat = AutoSpill - Investigation
2. Request processing and response from autofill service
Select next view,
whose domain is null
or matches
DomainCheckList
Add WebDomain to
DomainCheckList
Process No more
A selection nodes
Return
Traverse
AssistStructure to find Vv
sorpeni lel tedieet Add AutoFillld of
Traverse next node in If node is .
4 selection input field Wel tee
autofillTargetList
Use FocusedID to
identify input field that
triggered the request
LN
Otherwise
No
Check
WebDomain
of node
Autofill service
: : Traverse children
receives FillRequest
Is null or
matches
ueeeee-- LN _oee eee DomainCheckList
= Start ___
L JL J
Y aa
Request Request
processing: Pass 1 processing: Pass 2
49
```

## Slide 50

# AutoSpill -Investigation

### _2. Request processing and response from autofill service_

#BHEU @BlackHatEvents

50

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pif hat
EUROPE 2023
AutoSpill - Investigation
2. Request processing and response from autofill service
Select next view,
whose domain is null
Traversal complete
Add WebDomain to
DomainCheckList
A
Traverse
AssistStructure to find
domain of request
A
Use FocusedID to
identify input field that
triggered the request
A
or matches
DomainCheckList
No more
nodes
Process
selection
Return
Vv
Traverse next node in
selection
Otherwise
Autofill service
receives FillRequest
Check
WebDomain
of node
Traverse children
Is null or
matches
DomainCheckList
If node is
input field
Add AutoFillld of
this node to
autofillTargetList
No
Y
Use DomainCheckList
to create Dataset(s)
for autofillTargetList
7
Return Dataset(s) to
Android system via
FillResponse
v
Android displays
suggestions to user;
user selects and
authorises
v
Android fills selected
suggestion in fields,
whose AutoFillld is
described in Dataset
se
Neeeeee Start. \_.-- Complete. ____
L J
Y Y Y
Request Request Post-processing,
processing: Pass 1 processing: Pass 2 response
50
```

## Slide 51

# AutoSpill-Investigation

_Report_

#BHEU @BlackHatEvents

51

## Slide 52

# AutoSpill-Investigation

_Report_

- + Always renders NativeView data

   - Even for requests from a WebView

   - Creates confusion for autofill service

#BHEU @BlackHatEvents

52

## Slide 53

# AutoSpill-Investigation

_Report_

- + Always renders NativeView data

   - Even for requests from a WebView

   - Creates confusion for autofill service

- + Parses entire _AssistStructure_

   - No track of parent view’s _WebDomain_

   - Identifies incorrect target input fields

#BHEU @BlackHatEvents

53

## Slide 54

# AutoSpill-Investigation

Report
54

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Qo oa.
blackhat = AutoSpill - Investigation
PASSWORD
MANAGERS
```

## Slide 55

# Results

### PMs considered

|**PM**|**Version**|**PM’s autofill approach**|
|---|---|---|
|Google Smart Lock|13.30.8.26.arm64|OpenYOLO|
|DashLane|6.2221.3-arm64-v8a|OpenYOLO|
|1Password|7.9.4|Autofill Framework|
|LastPass|5.11.0.9519|Autofill Framework|
|Enpass|6.8.2.666|Autofill Framework|
|Keepass2Android|1.09c-r0|Autofill Framework|
|Keeper|16.4.3.1048|Autofill Framework|

### Configurations of devices used

|**Model**|**Type**|**Android version**|**Android security patch**|
|---|---|---|---|
|Poco F1|Smartphone|Android 10|December 2020|
|Samsung Galaxy Tab S6 Lite|Tablet|Android 11|January 2022|
|Samsung Galaxy A52|Smartphone|Android 12|April 2022|

#BHEU @BlackHatEvents

55

## Slide 56

# Results

### Without JavaScript support

Native fields present in HA
2 1 1 1
JavaScript
PM
Both injection
username,  Only  Only  Only
username none
password password
Google Smart Lock ✓ ✓ ✓ ✓
Dashlane ✓ ✓ ✓ ✓
1Password ✗ ✗ P U
LastPass U+P U P U Disabled
Enpass U+P U P U
Keepass2Android U+P U P U
Keeper U+P U P U

✓: No AutoSpill, safe

✗: Autofilling not working at all

U: AutoSpills username P: AutoSpills password <u>U+P: AutoSpills both username and password</u>

#BHEU @BlackHatEvents

56

## Slide 57

# Results

### With JavaScript support

Native fields present in HA
2 1 1 1
JavaScript
PM
Both injection
username,  Only  Only  Only
username none
password password
Google Smart Lock U+P U/P U/P U/P
Dashlane U+P U/P U/P U/P
1Password ✗ ✗ U/P U/P
LastPass U+P U/P U/P U/P Enabled
Enpass U+P U/P U/P U/P
Keepass2Android U+P U/P U/P U/P
Keeper U+P U/P U/P U/P

✗: Autofilling not working at all.

U+P: HA accessed and stole both username and password

U/P: HA accessed both username and password, stole credential of choice.

#BHEU @BlackHatEvents

57

## Slide 58

# Video time!

#BHEU @BlackHatEvents

58

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
af
£
a)
O
oD)
oO
>
—)
EUROPE 202
pif hat
58
```

## Slide 59

# Countermeasures

#BHEU @BlackHatEvents

59

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Q
blackhat Countermeasures
PASSWORD
MANAGERS
I TO ee ee 1
Vv Vv
1 1.1 NativeView 1.2 WebView 1
ChildrenCount: 2 ChildrenCount: 2
' AutoFillld: 1073741829 AutoFillld: 1073741826 '
H WebDomain: null WebDomain: m.facebook.com i
t 1
| | | !
v v v v
1.1.1 Username 1.1.2 Password 1.2.1 Username 1.2.2 Password
AutoFillld: 1073741824 AutoFillld: 1073741825 AutoFillld: 1073741826:196608 AutoFillld: 1073741826 :196609
Dimension: 300x100 Dimension: 300x100 Dimension: 300x100 Dimension: 300x100
59
```

## Slide 60

# Countermeasures

**No excess information!**

_AssistStructure_ data for request-triggering view only

#BHEU @BlackHatEvents

60

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
>)
blackhat Countermeasures
AssistStructure data for request-triggering view only
No excess
information!
PASSWORD
MANAGERS
I (Remi, “rere 1
Vv Vv
1 1.1 NativeView 1.2 WebView 1
ChildrenCount: 2 ChildrenCount: 2
' AutoFillld: 1073741829 AutoFillld: 1073741826 '
H WebDomain: null WebDomain: m.facebook.com i
t 1
| | | !
v v v v
1.1.1 Username 1.1.2 Password 1.2.1 Username 1.2.2 Password
AutoFillld: 1073741824 AutoFillld: 1073741825 AutoFillld: 1073741826:196608 AutoFillld: 1073741826 :196609
Dimension: 300x100 Dimension: 300x100 Dimension: 300x100 Dimension: 300x100
60
```

## Slide 61

# Countermeasures

_AssistStructure_ data for request-triggering view only Non-null WebDomain into HTML elements

**No excess information!**

#BHEU @BlackHatEvents

61

## Slide 62

# Countermeasures

_AssistStructure_ data for request-triggering view only Non-null WebDomain into HTML elements

**No excess information!**

**No excess processing!**

Keep a track of parent view’s WebDomain

#BHEU @BlackHatEvents

62

## Slide 63

# Countermeasures

_AssistStructure_ data for request-triggering view only Non-null WebDomain into HTML elements

**No excess information!**

Keep a track of parent view’s WebDomain

**No excess processing!**

Run-time AutoFillId from _AssistStructure_ to Identify & process request-triggering field Supply values back only for request-triggering view

#BHEU @BlackHatEvents

63

## Slide 64

# Black Hat Sound Bytes

- PMs work under the constraints of Android’s app sandboxing

- Excess information (from Android) and excess processing (by PMs) lead to credential AutoSpill

- Android and PM developers must work together to fix AutoSpill

#BHEU @BlackHatEvents

64

## Slide 65

# Image credits

Evil image by Freepik - Flaticon, www.flaticon.com/free-icons/evil

Markus Spiske, Coding, www.pexels.com/photo/technology-computer-desktop-programming-113850 Worldwide image by Prosymbols Premium - Flaticon, www.flaticon.com/free-icons/worldwide Internet image by Stickers - Flaticon, www.flaticon.com/free-stickers/internet Devices image by Freepik - Flaticon, www.flaticon.com/free-icons/devices Routing image by Iconjam - Flaticon, www.flaticon.com/free-icons/routing Conveyor-belt image by Freepik - Flaticon, www.flaticon.com/free-icons/conveyor-belt Traffic control image by Freepik - Flaticon, www.flaticon.com/free-icons/traffic-control iPhone image by Freepik - Flaticon, www.flaticon.com/free-icons/iphone iPad image by Freepik - Flaticon, www.flaticon.com/free-icons/ipad iMac image by Freepik - Flaticon, www.flaticon.com/free-icons/computer Ecommerce images by Eucalyp - Flaticon, www.flaticon.com/free-icons/ecommerce Login image by bearicons - Flaticon, www.flaticon.com/free-icons/login Filistic, iOS icon pack, www.etsy.com/listing/1343526218/ios-16-app-icon-pack-with-100-aesthetic Checklist image by Freepik - Flaticon, www.flaticon.com/free-icons/checklist Pain image by Smashicons - Flaticon, www.flaticon.com/free-icons/pain Password image by Smashicons - Flaticon, www.flaticon.com/free-icons/password Center focus image by Freepik - Flaticon, www.flaticon.com/free-icons/center-focus Wikimedia Commons, Android, commons.wikimedia.org/wiki/File:Android_robot.svg Database image by Freepik - Flaticon, www.flaticon.com/free-icons/database Selection image by Freepik - Flaticon, www.flaticon.com/free-icons/select Login image by srip - Flaticon, www.flaticon.com/free-icons/login Form image by Freepik - Flaticon, www.flaticon.com/free-icons/form Phone image by juicy_fish - Flaticon, www.flaticon.com/free-icons/cell-phone Desktop image by Vichanon Chaimsuk - Flaticon, www.flaticon.com/free-icons/login Puzzle image by riajulislam - Flaticon, www.flaticon.com/free-icons/puzzle Webpage image by Eucalyp - Flaticon, www.flaticon.com/free-icons/webpage Mobile image by amonrat rungreangfangsai - Flaticon, www.flaticon.com/free-icons/application Playstore image by justicon - Flaticon, www.flaticon.com/free-icons/playstore Sandbox image by juicy_fish - Flaticon, www.flaticon.com/free-icons/sandbox Oil-spill image by nawicon - Flaticon, www.flaticon.com/free-icons/oil-spill Wikimedia Commons, Mad scientist, commons.wikimedia.org/wiki/File:Mad_scientist_transparent_background.svg Investigation image by Dewi Sari - Flaticon, www.flaticon.com/free-icons/investigation Lazy Owl, "The lucifer effect: Why good people turn bad?" www.youtube.com/watch?v=1RwhkZFDYmY Wikimedia Commons, Popcorn, commons.wikimedia.org/wiki/File:Popcorn.svg Thank you image by Freepik - Flaticon, www.flaticon.com/free-icons/thank-you QA image by Freepik - Flaticon, www.flaticon.com/free-icons/qa 65

#BHEU @BlackHatEvents

65

## Slide 66

AutoSpill attack by: **Ankit Gangwal** (gangwal@iiit.ac.in) Shubham Singh Abhijeet Srivastava

#BHEU @BlackHatEvents

66

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pif hat
EUROPE 2023
AutoSpill attack by:
Ankit Gangwal (gangwal@iiit.ac.in)
THANK Shubham Singh
YOU Abhijeet Srivastava
INTERNATIONAL INSTITUTE OF
INFORMATION TECHNOLOGY
HYDERABAD
66
```
