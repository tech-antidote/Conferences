---
title: "Parse Me, Baby, One More Time Bypassing HTML Sanitizer via Parsing Differentials"
speakers: ["David Klein"]
conference: "Black Hat"
conference_full: "Black Hat Europe 2024"
edition: "Europe"
year: 2024
source_pdf: "BlackHat_Europe_2024_slides/David Klein_Parse Me, Baby, One More Time Bypassing HTML Sanitizer via Parsing Differentials.pdf"
pages: 83
sha256: "66af1da21b757b25cdd253d8817f43c825b3b44575420ee724088b1c953ab8f0"
text_chars: 17680
ocr_pages: 4
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:49:11Z"
---
# Parse Me, Baby, One More Time Bypassing HTML Sanitizer via Parsing Differentials

**Speakers:** David Klein  
**Conference:** Black Hat Europe 2024  
**Source:** `BlackHat_Europe_2024_slides/David Klein_Parse Me, Baby, One More Time Bypassing HTML Sanitizer via Parsing Differentials.pdf` (83 pages)

## Slide 1

**Parse Me Baby One More Time: Bypassing HTML Sanitizer via Parsing Differentials**

Speaker: David Klein

#BHEU   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
lack
EWROPE 20 4 Lin
DE BER 11-12, 2024
RIEFINGS
~Parse Me Baby One More Tires:
Bypassing HTML Sanitizer
via Parsing Differentials
Speaker: David Klein
```

## Slide 2

# About Me

PhD Candidate Research interests:

- Web Security

- Privacy

- Application Security

1

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
eon 2024 t M €
m PhD Candidate
m Research interests:
— Web Security
— Privacy
— Application Security
ote
INSTITUTE FOR oy) S $g6|xg% Technische
APPLICATION \ A oY = Universitat
SECURITY CYBER SECURITY IN THE AGE Fi ; Braunschweig
OF LARGE-SCALE ADVERSARIES
```

## Slide 3

# Cross Site Scripting (XSS)

## **Client-Side**

**Server-Side**

```
document.write(location.hash);
```

```
<?php
echo$_GET["name"];
```

2

## Slide 4

# Cross Site Scripting (XSS)

**Client-Side**

**Server-Side**

`document.write` `(location.hash)` `;` User Input

```
<?php
echo$_GET["name"];
```

User Input

2

## Slide 5

# Cross Site Scripting (XSS)

## **Client-Side**

**Server-Side**

```
document.write(location.hash);
```

Reflection

_`<?php`_ `echo` `$_GET["name"];` Reflection

2

## Slide 6

# Cross Site Scripting (XSS)

## **Client-Side**

**Server-Side**

```
document.write(location.hash);
```

```
<?php
echo$_GET["name"];
```

**Such Code Patterns Are Everywhere!**

2

## Slide 7

# Cross Site Scripting (XSS)

## **Client-Side**

**Server-Side**

```
document.write(location.hash);
```

```
<?php
echo$_GET["name"];
```

**Such Code Patterns Are Everywhere!**

2

## Slide 8

Everywhere?

3

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
#) :
blackhat Everywhere?
TestConference hoterp.con says
Hi there!
Welcome to the Test Conference (TestConference) submissions site.
Submissions
The deadline for registering submissions has passed
```

## Slide 9

# Detecting XSS

## **Client-Side**

Dynamic Taint Tracking! – A taint browser

## **Server-Side**

Less clear

SAST? DAST? Linter?

Project Foxhound

4

## Slide 10

# Sanitization to Prevent XSS

� Simply remove or change dangerous parts from the input

5

## Slide 11

# Sanitization to Prevent XSS

- Simply remove or change dangerous parts from the input – Allow formatting tags to pass through, but remove everything dangerous – E.g., `<img src=x onerror=alert()>` _→_ `<img src=x>`

5

## Slide 12

# Sanitization to Prevent XSS

- Simply remove or change dangerous parts from the input – Allow formatting tags to pass through, but remove everything dangerous – E.g., `<img src=x onerror=alert()>` _→_ `<img src=x>`

- This is called **sanitization**

5

## Slide 13

# Sanitization to Prevent XSS

� Simply remove or change dangerous parts from the input – Allow formatting tags to pass through, but remove everything dangerous – E.g., `<img src=x onerror=alert()>` _→_ `<img src=x>` This is called **sanitization**

**Definition: Sanitizer**

Function taking arbitrary input and returns a safe value The output shall resemble the input **_⇒_** I.e., perserve benign parts

5

## Slide 14

My journey towards this research

Researching people rolling their own sanitizers E.g., trying to filter HTML with regular expressions

```
functionf(v){
returnv.replace(/'/g,"").replace(/\(/g,"")
.replace(/\)/g,"").replace(/alert/g,"");
```

How not to sanitize HTML

6

## Slide 15

# My journey towards this research

Researching people rolling their own sanitizers E.g., trying to filter HTML with regular expressions

```
functionf(v){
returnv.replace(/'/g,"").replace(/\(/g,"")
.replace(/\)/g,"").replace(/alert/g,"");
```

How not to sanitize HTML

My takeaway: Use sanitizers relying on a real HTML parser I.e., most server-side sanitizers

6

## Slide 16

My journey towards this research

Researching people rolling their own sanitizers E.g., trying to filter HTML with regular expressions

```
functionf(v){
returnv.replace(/'/g,"").replace(/\(/g,"")
.replace(/\)/g,"").replace(/alert/g,"");
```

How not to sanitize HTML

My takeaway: Use sanitizers relying on a real HTML parser I.e., most server-side sanitizers But does that really help?

6

## Slide 17

# Sanitization: Workflow

Input

7

## Slide 18

# Sanitization: Workflow

Parse
Input
1
2 4 5
3 6 7

## Sanitizer

7

## Slide 19

# Sanitization: Workflow

Parse Clean
Input 1 1
2 4 5 2 4 5
3 6 7 6 7

## Sanitizer

7

## Slide 20

# Sanitization: Workflow

Serialize
Parse Clean
Input 1 1 Output
2 4 5 2 4 5
3 6 7 6 7
Sanitizer

7

## Slide 21

# Sanitization: Workflow

Serialize
Parse Clean Parse
Input 1 1 Output 1
2 4 5 2 4 5 2 4 5
3 6 7 6 7 6 7
Sanitizer Application

7

## Slide 22

Sanitization: Workflow
Serialize
Parse Clean Parse
Input 1 1 Output 1 Process
2 4 5 2 4 5 2 4 5
3 6 7 6 7 6 7
Sanitizer Application

7

## Slide 23

# HTML Parsing Complexities

## **HTML Code**

```
<div>
<svg>...</svg>
<table>
<div>
<tbody></tbody>
</div>
</table>

<imgsrc=xonerror=f()>
<style>
Te</div>xt
</style>
</br>
</div>
```

Parsed into

DOM Tree
div
svg
div
table
br tbody
img
iframe
br #text

8

## Slide 24

# HTML Parsing Complexities

HTML Code DOM Tree
Parsed into
<div>
div
<svg>...</svg>
<table>
svg
<div>
</<divtbody> ></tbody> Change to SVG parser div
</table> table

<img src=x onerror=f()> br tbody
<style>
Te</div>xt img
</style>
iframe
</br>
</div>
br #text

8

## Slide 25

# HTML Parsing Complexities

HTML Code DOM Tree
Parsed into
<div>
div
<svg>...</svg>
<table>
svg
<div>
<tbody></tbody> div
</div> Repair broken input
</table> table

<img src=x onerror=f()> br tbody
<style>
Te</div>xt img
</style>
iframe
</br>
</div>
br #text

8

## Slide 26

# HTML Parsing Complexities

HTML Code DOM Tree
Parsed into
<div>
div
<svg>...</svg>
<table>
svg
<div>
<tbody></tbody> div
</div>
</table> table

<img src=x onerror=f()> br tbody
<style>
Te</div>xt img
</style> Closes Automatically
iframe
</br>
</div>
br #text
Transformed to Opening Tag

8

## Slide 27

# HTML Parsing Complexities

HTML Code DOM Tree
Parsed into
<div>
div
<svg>...</svg>
<table>
svg
<div>
<tbody></tbody> div
</div>
</table> table

<img src=x onerror=f()> br tbody
<style>
Te</div>xt img
</style>
</br> Script execution capabilitiesiframe
</div>
br #text

8

## Slide 28

# HTML Parsing Complexities

HTML Code DOM Tree
Parsed into
<div>
div
<svg>...</svg>
<table>
svg
<div>
<tbody></tbody> div
</div>
</table> table

<img src=x onerror=f()> br tbody
<style>
Te</div>xt img
</style>
iframe
</br>
</div>
br #text
Different Parsing Mode

8

## Slide 29

Sanitization: Parsing Differential
Parse Clean Serialize Parse
Input 1 1 Output 1 Process
2 4 5 2 4 5 2 4 5
3 3 3 6 7

9

## Slide 30

Sanitization: Parsing Differential
Parse Clean Serialize Parse
Input 1 1 Output 1 Process
2 4 5 2 4 5 Different! 2 4 5
3 3 3 6 7

9

## Slide 31

# Parsing Differential to XSS

Payload: `<select><iframe><script>payload()</script>`

10

## Slide 32

# Parsing Differential to XSS

Payload: `<select><iframe><script>payload()</script>`

**Parsed by Caja**

## **Parsed by Chrome**

#tag
select
#tag
iframe
#text
<script>payload()</script>

#tag
select
#tag
script

10

## Slide 33

Root Cause

11

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
#) :
blackhat Root Cause
4.8.5 The iframe element
Categories:
Flow content.
Phrasing content.
Embedded content.
Interactive content.
Palpable content.
Contexts in which this element can be used:
Where embedded content is expected.
Content model:
Nothing.
11
```

## Slide 34

# Root Cause

#### **The “nothing” content model:**

. . . the element must contain no Text nodes (other than inter-element whitespace) and no element nodes.

12

## Slide 35

# Root Cause

**The “nothing” content model:** . . . the element must contain no Text nodes (other than inter-element whitespace) and no element nodes. However, the parsing specification disagrees: content of `iframe` shall be parsed as text!

12

## Slide 36

# Root Cause

**The “nothing” content model:** . . . the element must contain no Text nodes (other than inter-element whitespace) and no element nodes. However, the parsing specification disagrees: **_⇒_** Inconsistency in the spec! One parsing quirk we identified

12

## Slide 37

# Root Cause

**The “nothing” content model:** . . . the element must contain no Text nodes (other than inter-element whitespace) and no element nodes.

- Re sults in `iframe` element with payload as textual content. However, the parsing specification disagrees: No code execution!

- **_⇒_** Inconsistency in the spec! One parsing quirk we identified

- `div.innerHTML = `<iframe><img src=x onerror=alert(1)>`;`

12

## Slide 38

# Root Cause

**The “nothing” content model:** . . . the element must contain no Text nodes (other than inter-element whitespace) and no element nodes.

However, the parsing specification disagrees: **_⇒_** Inconsistency in the spec! One parsing quirk we identified So the sanitizer is actually correct, but. . .

12

## Slide 39

# Root Cause

**The “nothing” content model:**

. . . the element must contain no Text nodes (other than inter-element whitespace) and no element nodes. However, the parsing specification disagrees: **_⇒_** Inconsistency in the spec! One parsing quirk we identified So the sanitizer is actually correct, but. . . ? Where has the `iframe` gone?

12

## Slide 40

# The Missing `iframe`

Recall the payload: `<select><iframe><script>payload()</script>`

13

## Slide 41

# The Missing `iframe`

Recall the payload: `<select><iframe><script>payload()</script>`

**The** `select` **Element**

**Content model:** _Zero or more_ _`option` ,_ _`optgroup` , and_ _script-supporting elements._

� “script-supporting elements” are `script` and `template` tags

13

## Slide 42

# The Missing `iframe`

Recall the payload: `<select><iframe><script>payload()</script>`

**The** `select` **Element**

**Content model:** _Zero or more_ _`option` ,_ _`optgroup` , and script-supporting elements._

**_⇒_** An `iframe` can’t be a child of `select` ! So Chrome simply drops it

13

## Slide 43

# Who Uses Google Caja?

Google has deprecated Caja 5y+ ago That does not stop others from using it, however

14

## Slide 44

```
MutaGen
```

Goal: Find Parsing Differentials to bypass HTML sanitizers

15

## Slide 45

# `MutaGen`

Goal: Find Parsing Differentials to bypass HTML sanitizers

`MutaGen` **: HTML payload generator**

� Generate HTML that is difficult to parse

15

## Slide 46

# `MutaGen`

Goal: Find Parsing Differentials to bypass HTML sanitizers

`MutaGen` **: HTML payload generator**

- Generate HTML that is difficult to parse **_⇒_** It _mutates_ during parsing

15

## Slide 47

# `MutaGen`

Goal: Find Parsing Differentials to bypass HTML sanitizers

`MutaGen` **: HTML payload generator**

- Generate HTML that is difficult to parse **_⇒_** It _mutates_ during parsing

Important to keep in mind: HTML parsing never fails! **_⇒_** Garbage in, DOM out

15

## Slide 48

# `MutaGen`

### Simplified Payload Generation and Serialization.

**Generation**

**Serialization**

16

## Slide 49

# `MutaGen`

Simplified Payload Generation and Serialization.

Generation Serialization
Payload(Img tag)

16

## Slide 50

# `MutaGen`

Simplified Payload Generation and Serialization.

Generation Serialization
Payload(Img tag)
Close tag
(NoScript, Prepend)

16

## Slide 51

# `MutaGen`

Simplified Payload Generation and Serialization.
Generation Serialization
Payload(Img tag)
Close tag
(NoScript, Prepend)
Enclose tag attr (Div,
Id, Enclosed(Double))

16

## Slide 52

# `MutaGen`

Simplified Payload Generation and Serialization.

Generation
Payload(Img tag)
Close tag
(NoScript, Prepend)
Enclose tag attr (Div,
Id, Enclosed(Double))
Open tag
(NoScript, Prepend)

Serialization

16

## Slide 53

# `MutaGen`

Simplified Payload Generation and Serialization.
Generation Serialization
Payload(Img tag)
Close tag
(NoScript, Prepend)
Enclose tag attr (Div,
Id, Enclosed(Double))
Open tag
(NoScript, Prepend)
⊥

Serialization

16

## Slide 54

# `MutaGen`

Simplified Payload Generation and Serialization.
Generation Serialization
Payload(Img tag) <img src=x onerror=f()>
Close tag
(NoScript, Prepend)
Enclose tag attr (Div,
Id, Enclosed(Double))
Open tag
(NoScript, Prepend)
⊥

16

## Slide 55

# `MutaGen`

Simplified Payload Generation and Serialization.
Generation Serialization
Payload(Img tag) <img src=x onerror=f()>
Close tag </noscript>
(NoScript, Prepend) <img src=x onerror=f()>
Enclose tag attr (Div,
Id, Enclosed(Double))
Open tag
(NoScript, Prepend)
⊥

16

## Slide 56

# `MutaGen`

### Simplified Payload Generation and Serialization.

Generation
Payload(Img tag)
Close tag
(NoScript, Prepend)
Enclose tag attr (Div,
Id, Enclosed(Double))
Open tag
(NoScript, Prepend)
⊥

Serialization
<img src=x onerror=f()>
</noscript>
<img src=x onerror=f()>
<div id="</noscript>
<img src=x onerror=f()>">

16

## Slide 57

# `MutaGen`

### Simplified Payload Generation and Serialization.

Generation
Payload(Img tag)
Close tag
(NoScript, Prepend)
Enclose tag attr (Div,
Id, Enclosed(Double))
Open tag
(NoScript, Prepend)
⊥

Serialization
<img src=x onerror=f()>
</noscript>
<img src=x onerror=f()>
<div id="</noscript>
<img src=x onerror=f()>">
<noscript>
<div id="</noscript>
<img src=x onerror=f()>">

16

## Slide 58

# Parsing Differential in the Wild

**_⇒_** 11 sanitizers across five programming languages. Java, JavaScript, PHP, Ruby, and .NET

17

## Slide 59

# Parsing Differential in the Wild

Name Total Downloads Language Vulns. DOMPurify 399 001 216 **2** google caja 41 305 997 JavaScript † sanitize-html 276 882 692 **0** HtmlSanitizer 19 800 000 **2** .NET HtmlRuleSanitizer 306 100 **2** Typo3 html-sanitizer 1 950 185 PHP **4** rgrove/sanitize 60 928 006 **1** Ruby loofah 396 621 861 **0** AntiSamy **3** No data available Java JSoup **2** Total Over 1 Billion **16**

<u>18</u>

## Slide 60

# Running `MutaGen`

During the first test, after like 10s, I was greeted by: _`PHP Warning: Uninitialized string offset 26 in html5/src/HTML5/Parser/Scanner.php on line 108`_

A target nobody has fuzzed before, i.e., good target!

19

## Slide 61

# Parsing Differential in the Wild

**_⇒_** 11 sanitizers across five programming languages. Java, JavaScript, PHP, Ruby, and .NET

**All** have functional deficiencies

   - Average parsing similarty compared to browsers is below 60%

- Even if secure, sanitizers mangle input by parsing incorrectly

- 16 new bypass vectors across 9 of them

   - And one bypass vector in a sanitizer not directly tested by us

20

## Slide 62

# Parsing Accuracy #2

What parser processes the output? Fragment or Document?

21

## Slide 63

# Parsing Accuracy #2

What parser processes the output? Fragment or Document? I.e., `innerHTML` assignment or `document.write`

21

## Slide 64

# Parsing Accuracy #2

What parser processes the output? Fragment or Document? I.e., `innerHTML` assignment or `document.write` Which browser is the result displayed in?

21

## Slide 65

# Browser Parsing Differentials

Payload:

```
<svg><embed><iframe><desc><imgsrc=xonerror=f()>
```

22

## Slide 66

# Browser Parsing Differentials

Payload:

```
<svg><embed><iframe><desc><imgsrc=xonerror=f()>
```

**Does this execute code?**

22

## Slide 67

# Browser Parsing Differentials

Payload:

```
<svg><embed><iframe><desc><imgsrc=xonerror=f()>
```

22

## Slide 68

# Browser Parsing Differentials

Payload:

- `<svg><embed><iframe><desc><img src=x onerror=f()>`

context
svg
embed
iframe
#text

- (a) Chrome parsing result

22

## Slide 69

# Browser Parsing Differentials

Payload:

```
<svg><embed><iframe><desc><imgsrc=xonerror=f()>
```

context
svg
embed
iframe
#text

- (a) Chrome parsing result

context
svg
embed
iframe
desc
img
(b) Firefox parsing result

- **_⇒_** Perfectly accurate sanitizer is impossible

22

## Slide 70

# DOMPurify to Aid Exploitation

Input: `<svg><style>&lt;img src=x onerror=f()&gt;<keygen>`

23

## Slide 71

# DOMPurify to Aid Exploitation

Input: `<svg><style>&lt;img src=x onerror=f()&gt;<keygen>` Output: `<svg><style><img src=x onerror=f()>`

23

## Slide 72

# DOMPurify to Aid Exploitation

Input: `<svg><style>&lt;img src=x onerror=f()&gt;<keygen>` Output: `<svg><style><img src=x onerror=f()>` **_⇒_** Sanitizers can help to bypass other security measures!

23

## Slide 73

# Common Problems

Handling comments is surprisingly error prone. . .

24

## Slide 74

# Common Problems

Handling comments is surprisingly error prone. . .

- Three sanitizers do not detect _closing bang comments_

24

## Slide 75

# Common Problems

Handling comments is surprisingly error prone. . .

- Three sanitizers do not detect _closing bang comments_

� That is, comments terminated with `--!>`

24

## Slide 76

# Common Problems

Handling comments is surprisingly error prone. . . – Three sanitizers do not detect _closing bang comments_ `noscript` is impossible to get right: four bypasses

24

## Slide 77

# Common Problems

Handling comments is surprisingly error prone. . . – Three sanitizers do not detect _closing bang comments_ `noscript` is impossible to get right: four bypasses – Parsing depends on browser internal state, not exposed to sanitizers

24

## Slide 78

# Common Problems

Handling comments is surprisingly error prone. . . – Three sanitizers do not detect _closing bang comments_ `noscript` is impossible to get right: four bypasses

- Parsing depends on browser internal state, not exposed to sanitizers

- Sanitizing inputs containing `noscript` impossible!

24

## Slide 79

# Common Problems

Handling comments is surprisingly error prone. . . – Three sanitizers do not detect _closing bang comments_ `noscript` is impossible to get right: four bypasses

- Parsing depends on browser internal state, not exposed to sanitizers

Namespace confusion bugs are common

24

## Slide 80

# Common Problems

Handling comments is surprisingly error prone. . .

- Three sanitizers do not detect _closing bang comments_

- `noscript` is impossible to get right: four bypasses

   - Parsing depends on browser internal state, not exposed to sanitizers

Namespace confusion bugs are common

- Not correctly switching between different parsers. Recall the Firefox bug shown earlier!

24

## Slide 81

# Common Problems

Handling comments is surprisingly error prone. . . – Three sanitizers do not detect _closing bang comments_ `noscript` is impossible to get right: four bypasses – Parsing depends on browser internal state, not exposed to sanitizers Namespace confusion bugs are common Some fundamental parsing bugs too!

- Parsing depends on browser internal state, not exposed to sanitizers

24

## Slide 82

# **Thank you!**

**If you want to chat Web Security please get in touch!**

Contact
� david.klein@tu-braunschweig.de
� leinea
� twitter.com/ncd_leen

## Slide 83

# Black Hat Sound Bytes

**Server-Side HTML Sanitization is Insecure, Broken or Both**

**Parse** _→_ **Serialize** _→_ **Parse is always prone to parsing differentials**

**A New Vision of Sanitization is Required to Get us Out of This Mess**

26
