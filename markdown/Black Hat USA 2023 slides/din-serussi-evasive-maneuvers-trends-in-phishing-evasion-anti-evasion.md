---
title: "Evasive Maneuvers Trends in Phishing Evasion & Anti-Evasion"
speakers: ["Din Serussi"]
conference: "Black Hat"
conference_full: "Black Hat USA 2023"
edition: "USA"
year: 2023
source_pdf: "Black Hat USA 2023 slides/Din Serussi_Evasive Maneuvers Trends in Phishing Evasion & Anti-Evasion.pdf"
pages: 28
sha256: "0326047096a45e70e721b93370645f409601387eaf9d3d0f59adc0d59e57cb2b"
text_chars: 16241
ocr_pages: 16
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:15:49Z"
---
# Evasive Maneuvers Trends in Phishing Evasion & Anti-Evasion

**Speakers:** Din Serussi  
**Conference:** Black Hat USA 2023  
**Source:** `Black Hat USA 2023 slides/Din Serussi_Evasive Maneuvers Trends in Phishing Evasion & Anti-Evasion.pdf` (28 pages)


## Slide 1

### Evasive Maneuvers: Trends in Phishing Evasion & Anti-Evasion

Din Serussi – Perception Point

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pifek hat
USA &
AUGUST 9-10, ©0253
BRIEFINGS
Evasive Maneuvers: Trends in
Phishing Evasion & Anti-Evasion
Din Serussi — Perception Point
#BHUSA @BlackHatEvents
```

## Slide 2

## whoami

- Incident Response Group Manager

- Email Threat Hunter

- Expert In Creating Detections Against Phishing

- Perception Point: Email, File & URL security

#BHUSA @BlackHatEvents

## Slide 3

## Phishing: Then & Now

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
USA 20e53
Phishing: Then & Now
| d | | need you to generate an email for me,
=| Fisher The email is sent from Microsoft and has a place to insert a link.
_ The content should ask the user to reset his password
PW/CC Fisher
@ Fish For Passwords Number of people in room: Subject: Urgent: Password Reset Required
© Fish For Credit Cards 20
From: Microsoft noreply@microsoft.com
What You Will Say
C Phrase 1 © Phrase2 @ Phrase 3 © Custom —_> Contents
Text to Be Sent: Dear [User's Name],
ATTENTION: AOL NEWS +
* kkhhe We are reaching out to you regarding your Microsoft account. Our system has detected
Hi, I'm with the America Online billing department. . . . .
Due to a problem we our experiencing with our potential unauthorized access attempts, and as a security measure, we require you to reset
records, we have lost vital information concerning your : :
your password immediately to safeguard your account.
Start Help! | Cancel To proceed with the password reset process, please click on the following link:
[Insert Reset Password Link]
```

## Slide 4

## Agenda

- 1 Phishing Trends & Evasion Techniques (2022-2023)

   - 2 Post Account Takeover Tactics (Compromised Mailbox)

   - 3 Why Does Phishing Still Work?

- 4 Anti-Phishing Approach

#BHUSA @BlackHatEvents

## Slide 5

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 20253
€@ OneDrive
Password Expiry
fz Outlook
Your password is set to expire on 6/27/2023 12:35:26 p.m.
@mm/perception-point.io
Keep My Password
```

## Slide 6

## Text Obfuscation

**Static text filtering bypass.**

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
USA 20253
Text Obfuscation
Static text filtering bypass.
Password Expiry
Your password is set to expire on 6/27/2023 12:35:26 p.m.
@©mm/perception-point.io
Keeo My Password C:\Users\din.serussi>Ke e pMyP a ssw ord
```

## Slide 7

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
USA 20253
Input: | Keep My Password | Identify | Clear
Code points & Annotations
U+@@2@ : SPACE [SP]
U+@@4B : [LATIN CAPITAL LETTER K
U+0435 : |CYRILLIC SMALL LETTER IE
U+FEFF : |ZERO WIDTH NO-BREAK SPACE [ZWNBSP] (alias BYTE ORDER MARK [BOM]) {BOM, ZWNBSP}
U+FEFF : |ZERO WIDTH NO-BREAK SPACE [ZWNBSP] (alias BYTE ORDER MARK [BOM]) {BOM, ZWNBSP}
U+0435 : |CYRILLIC SMALL LETTER IE}
U+FEFF : |ZERO WIDTH NO-BREAK SPACE [ZWNBSP] (alias BYTE ORDER MARK [BOM]) {BOM, ZWNBSP
U+FEFF : |ZERO WIDTH NO-BREAK SPACE [ZWNBSP] (alias BYTE ORDER MARK [BOM]) {BOM, ZWNBSP
U+0070 : [LATIN SMALL LETTER P | |
U+0@2@ : SPACE [SP]
U+@@4D : LATIN CAPITAL LETTER M
U+FEFF : ZERO WIDTH NO-BREAK SPACE [ZWNBSP] (alias BYTE ORDER MARK [BOM]) {BOM, ZWNBSP}
U+@079 : LATIN SMALL LETTER Y
U+@02@ : SPACE [SP]
U+@42@ : CYRILLIC CAPITAL LETTER ER
U+FEFF : ZERO WIDTH NO-BREAK SPACE [ZWNBSP] (alias BYTE ORDER MARK [BOM]) {BOM, ZWNBSP}
U+FEFF : ZERO WIDTH NO-BREAK SPACE [ZWNBSP] (alias BYTE ORDER MARK [BOM]) {BOM, ZWNBSP}
U+@43@ : CYRILLIC SMALL LETTER A
U+FEFF : ZERO WIDTH NO-BREAK SPACE [ZWNBSP] (alias BYTE ORDER MARK [BOM]) {BOM, ZWNBSP}
U+FEFF : ZERO WIDTH NO-BREAK SPACE [ZWNBSP] (alias BYTE ORDER MARK [BOM]) {BOM, ZWNBSP}
U+@073 : LATIN SMALL LETTER S
U+@073 : LATIN SMALL LETTER S
U+FEFF : ZERO WIDTH NO-BREAK SPACE [ZWNBSP] (alias BYTE ORDER MARK [BOM]) {BOM, ZWNBSP}
U+@077 : LATIN SMALL LETTER W
U+FEFF : ZERO WIDTH NO-BREAK SPACE [ZWNBSP] (alias BYTE ORDER MARK [BOM]) {BOM, ZWNBSP}
U+FEFF : ZERO WIDTH NO-BREAK SPACE [ZWNBSP] (alias BYTE ORDER MARK [BOM]) {BOM, ZWNBSP}
U+@@6F : LATIN SMALL LETTER O
U+@0@72 : LATIN SMALL LETTER R
U+FEFF : ZERO WIDTH NO-BREAK SPACE [ZWNBSP] (alias BYTE ORDER MARK [BOM]) {BOM, ZWNBSP}
U+@064 : LATIN SMALL LETTER D
```

## Slide 8

## Browser In The Browser

www.netfliix-login.com
Evading favicon detections.
https://pay.netflix.com/home/login.aspx

#BHUSA @BlackHatEvents

## Slide 9

## Archive In The Browser

**Crawlers bypass.**

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
USA 20253
Archive In The Browser
File Explorer - WinRAR x + vo 8 *
Crawlers bypass.
€ C  @ invoice-december.zip #006
| Google Domains Overview Get started Features Learn shite Invoicezip - WinRAR (evaluation copy)
— a
Extract To Add Test View Scan
C:\Users\Din\Downloads\Invoice.zip
Name Size Type Modified
invoice.pdf 100 KB Document May 1, 2023
B{ Installer.exe 5 MB Executable April 15, 2023
Get up to speed
with .zip
Starting at $15/year
Q. invoice-december zip .
mH invoice.exe A Show a x
```

## Slide 10

## Quishing (QR Phishing)

- 800% increase in 2023

- Moving the threat to the mobile

- Websites look more legitimate

#BHUSA @BlackHatEvents

## Slide 11

## Captchas, Geofence & Redirects

- Automation ToolsUser Agents

- IP BlRem **o** cklistste Debugging Port

- VPNsHeadless Browsing

- Country Allow-listing

- User Interaction

#BHUSA @BlackHatEvents

## Slide 12

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
USA 20e53
PBIP_BLOCK]= array("%66.102.*.*", "*38.100.*.*", "4107.170.%.%", "4149.20.%.%", "438.105.%.%", "474.125.%.%",
"466.150.14.%", "%54.176.%.%", "4184.173.%.%", "%66.249.%.%", "4128.242.%.%", "S72.14.192.%", "4208.65.144.x",
ETA U2Z5 ko Xu NLT Ode 120. tim LL 2O7 26% wm Nl Ae 2O le eo ul, ue 20M VL 2O LAG +, mL) Se LOae <3 4uu, OM 2 5 5cLOOR Ku,
ETD TARO 2 Kee SOOR MOD km cam Odi Lolyts tar LOGO 2 OOS Xa ue OG DDO kar en Ol etl Oly 207k mn 21s DOL OS.
BAGO 65 xoe", “SSO. 7.42e", "S1S1.232 4:4", "AGG. 116uek , "AG2.900 xa, NASD.TSS.4.4", ""62.166.%.4", "985.64.44");
$HOSTS_BLOCK| = array(".tor.","VAULTVPN", "activescan", "alpha2", "amazon", "anti-phishing", "antipishing", "antispam",
"antivirus") "avast", "barracuda", "bitdefender'|,|"cia.gov"|)"cisco","cLlamav", "cLamwin"| "cleandir", "datapacket",
"eset"|,"f-secure",|'fbi.gov"||"fireye'|,"free-av")"fortimail", "fortinet"| "gfihispana",|"kapersky"|,"mailcontrol",
"mailstream", "mallshill", "marimex",|"mcafee", "microsoft.com", "mimecast"}| "monitor", "nod32",|"norton"|,"onlinedc","opendns",
"owned-networks", "phish" ,|"proofpoint"|, "rsa.com" )"sophos"|, "spamfirewall2",|"symantec", "trendmicro"|, "trustwave") ;
if(in_array($HOST, $HOSTS_BLOCK) or in_array($IP, $IP_BLOCK))
{
echo ‘<script Language="javascript">window. Location. replace("about: blank") ;</script>';
break;
```

## Slide 13

## 2 Step Phishing

Embedded href

#### **Over 400 services are being abused.**

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 20253
2 Step Phishing
Over 400 services are being abused.
are not lagged in and changes cannot be
Please regard the below shared Vital | SS @®
Documents Vv
This documents has been scanned for viruses by Norton Antivirus Security
"
J)
Qj aoa) SINS
Information Data: KPF903
Submission Data: TRN0938 a |
Embedded href =
```

## Slide 14

## Microsoft & Google Services Abuse

##### **The allow-listing vulnerability.**

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 20253
Microsoft & Google Services Abuse
The allow-listing vulnerability.
NJ’ WISE Medical Centers, LLC - Mic: X +
@ Microsoft SharePoint x + @ docxx - OneDrive x +
<€ GJ onedrive.live.com & x DE tovgnito : € CG a [customervoice.microsoft.com F Q x SD Dh & meognito (2 € CG @ demosmy.sharepoint.com
OneNote WISE Medical Centers, LLC » @ a Info 1/1 x
IN .
WISE Medical Centers, LLC
2
uesday, June 13, 2023 8:50AM
Signed and secured shared folder with you.
(1) ®SHAREPOINT FILE
You Have received 3 documents for your review.
This message was sent to you to protect sensitive information.
Hello,
VIEW DOCUMENT “ees
Ref: Document
You have just received new shared RFQ files for a proposal bid request via Microsoft
SharePoint. Authenticate and preview files via the SharePoint below;
To view doc sent lick View and Print Online™ |
>ACCESS SHAREPOINT
Thank You! {© 20, ure Microsoft Cloud SharePoint,
u
#BHUSA @BlackHatEvents
```

## Slide 15

## Microsoft & Google Services Abuse

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
USA 20253
Microsoft & Google Services Abuse
BB Admin - Google Slides x + im Mail x +
€ CG @ docs.google.com entation Q-x* §) Qa @ incognito i € C &@ sites.google.com/web-of.. ®& * SJ OF © incognito (3) :
io Microsoft Outlook
HY Microsoft
EMAIL*
MICROSOFT ACCOUNT UPGRADING NOTICE
2 : PASSWORD*
Click Here To Continue
SIGN IN
```

## Slide 16

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 20253
@ PERCEPTION-POINT x +
€ SC @ duhlvnhqu34blq2ni3txli4 prétfbfzpu6frtdu33u7j4-ipfs-cf--ipfs-com.translate.goog/s|
Go gie Translate English - detected —> English v
PERCEPTION Platform Services Partners Resources Company
POINT™
PERCEPTION-POINT
; ; eve nt demo@perception-point.io
LS ta rts “me °
Pp, { Remember me
Al-powered email, web browser, and cloud ap
nlatfarm. ALL threats |iahtnina fast. Zero averhea
x_tr...
Vv =
g® x §] oO e Incognito
Translation
```

## Slide 17

## Encoded HTML Files

##### **200% increase in the usage of malicious html files**

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
USA 20253
Encoded HTML Files
200% increase in the usage of malicious html files
perception-point.io <Microsoft365 Secured> demo@perception-point.io
P ; we
Mailbox Storage Exceeded Monday, July 3, 2023 7:51 a.m. Microsoft
Sign in
O Guide Settings.Html .
4 KB Email, phone, or Skype
demo Can't access your account?
Your Mail Storage is Full Monday, July 3, 2023 7:51 a.m. Back
To continue using perception-point.io free up at least 100.55 MB of
storage. .
QY Sign-in options
```

## Slide 18

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 20253
[2] Guide Settings html £9
1 <script> a
2 PwCAJx1lY = ite ou reeption—-point.io"
document.write Paras "PCEtLSBzYWdmc34vcmJwamN4 42Wdt42RleWS5odmtj]Ym9t4w5sy4mpkaGiwa
4 </script>
[2] Guide Settings html £9 |
1 <script> a
2 PwCAJxX1Y = "demo@perceptic
5 <script srce="https dnis m/ajax/ lil rypto-js/4.1.1/¢c rypto-js
= <script>var key = '4BVcq27bV8COTE
5 key = CryptoJs.enc.Utfs.parse (key);
6 qver decrypted = |CryptoJS .AES.decrypt|(' CGNsMWvSbFpsNw34fnDyYAfcsDmgeL5 oORWChz
7 ,key, {mode: CryptoJS.mode.ECB Ny:
document.write (decrypted.toString (CryptoJS.enc.Ut£8)) ;</script>
9 </script>
(| Guide Settings html 3
1 <script> a
2 PwCAJx1LY = "demo@perception-point.io"
3 function “0x6a66 () {var “0x100e2c=[) \sea\ =e c6E\x73\xG6£E\ZO6\K%74\x2e\x63\x0£"],'
a | 0x6d66=function () {return _Ox1l00e2c;};return 0x6d66();} function _O0x4985(_ 0x36
5 while (!![]){try{var _0x387088=parseInt (_ Ox4e7fcc ( yI/(- +- * +
6 setTimeout ( ()/=>{ _Oxbd67e8 (); he * + + *- )rb}) s}war  Ox2c22de=!
7 let _Oxf873df=await _Ox4caff2 (- + * +- *- )-}}}7_Ox11d791() -}}
8 </script>
```

## Slide 19

## Phone Scams

• Spreading out fake renewals alerts

- Not a generic credit card phishing

- Call centers located in India

• Over 1000 different templates

- **Trying to get control over the endpoint**

#BHUSA @BlackHatEvents

## Slide 20

**http** s://www.b://www.ge **e** stbuy.com/ksquadworld.com

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
USA 20253
httpshavevngbekianadorotid.com
>| =¢
F Bangor
BUY =. Search Best Buy I g Sy Cart
Top Deals Deal of the Day Health & Wellness Credit Cards Gift Cards Gift Ideas More ~ ® Account ~ Recently Viewed ~ Order Status ~ Saved Items ~
Best Buy >» Services
&
Geek Squad’ Services
We're here to
help.
We offer an unmatched level of support, with
Geek Squad Agents ready to help you 24/7
online, on the phone, in store or in your home.
```

## Slide 21

## Social Media Posts

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 20253
Social Media Posts
Meta <support@facebook.com>
Important Notice
demo@perception-point.io |
We want to address a matter of utmost importance that requires your immediate attention. It pertains to a
copyright complaint lodged against your content, which we believe you should be informed about promptly.
As per our well-established guidelines and the provisions outlined in the
Digital Millennium Copyright Act
(DMCA), we have a legal obligation to act upon a valid notice received from a copyright owner. Consequently,
we are compelled to take necessary steps to remove your page, thereby restricting public access to its content.
However, we understand that there may be instances where you feel this action is unjustified and wish to
contest it. If you find yourself in such a situation, we kindly request your cooperation in completing the appeal
form provided aj https://www.facebook.com/109681852182829.
We genuinely appreciate your unwavering attention and cooperation in resolving this matter promptly and
amicably.
Warm regards,
The Meta Team
DMCA Form
@-nvw 1
We regret to inform you that your Account is scheduled for deletion as
it violates our Community Standards regarding Intellectual Property.
If you wish to halt the account deletion process or retrieve any of the
content or information you have contributed, we kindly request you to
submit a report through the following link:
Please note that if no action is taken, Facebook will begin restricting
access to your account within 48 hours. After this time, you will be
unable to access your account or any of the associated content.
To submit a report, please visit: https://meta-business-
appeal15.web.app
Thank you for your cooperation.
Sincerely,
Meta Help Center
```

## Slide 22

*Password Reuse*

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 20253
@ MyPersonal Account Was Restri X
> CA Dangerous | meta-business-appeal15.web.app/?fbclid=IwAR13BPOm5|SeNE5IC2Voac2pOfV07-K70fRUOLQmkk7N 1el5v
Meta | Support Inbox
Meta Business Help Center
Get Support
password
Your page goes against our Community Standards
Our Message
Your page has been scheduled for deletion because one or more the following
- Intellectual Property Infringement
- Community Standards
- Hate Speech
Your Reply
Please be sure to provide the requested information below. Failure to provide this information may delay the processing
of your appeal.
```

## Slide 23

## Account Take Over

Steps:

1. Hacker is generating a phishing email

2. Phishing is sent to the victim’s mailbox

3. The victim opens the phishing email

4. The victim enters the credentials in a fake login window

5. The hackers gets the credentials

6. The hacker logs into the victim’s mailbox

7. Malicious inbox rules are defined

8. Victim’s mailbox is used to deliver malicious payloads

9. Known contacts get the emails and fall for it

10. Recursive phishing

7
2 8
1 3 9
6
4
5

#BHUSA @BlackHatEvents

## Slide 24

## Step 7 – Inbox Rules

Suspicious indicators to look out for:

- Rule names

- Delete actions

- Move actions

- Suspicious text filtering in:

   - A. subjectOrBodyContainsWords

B. fromAddressContainsWords

#BHUSA @BlackHatEvents

## Slide 25

## Why Does Phishing Still Work?

User Using A Static Headless Geofenced User Agent Limited Interaction IP Address Browsing Campaigns Blacklist Resources Evasion System Wise Personal Behavior Based Device Hosts Relying On 3<sup>rd</sup> Bad Context Heuristics Fingerprinting Blacklists Party Services Code Not Static Content No Similarity Lack Of Visual Encrypted Ignoring Sandboxing Filtering Modules Detections Files Iframes URLS Detection Wise Relying On No Anomaly Multilayered Misconfigured No QR\OCR Relying On URL Sender Modules Attacks Allow Lists Capabilities Reputation Reputation Weak Internal Lack Of End Insider Human Password Password Compromised Users Training Threats Errors Reuse Policy User Organization Wise Not Running Not Not Not Running No Web No Email Phishing Configuring Configuring Annual PT Security Filter Security Filter Simulations SPF Records MFA

Organization Wise

#BHUSA @BlackHatEvents

## Slide 26

## A New Approach: In-Browser Security

Dynamic Scanning

Password Reuse

Non Email Threats

Enforce Policies

ATO Investigations

Data Leak Prevention

#BHUSA @BlackHatEvents

## Slide 27

## Key Takeaways

- Set a strong password policy.

- Force 2 factor authentication.

- Configure SPF records against spoofing attempts.

- Conduct phishing trainings to end users at least 2 times a year.

- Run phishing simulations with trendy phishing evasions.

- Run an annual penetration testing and find your weak spots.

- Monitor suspicious inbox activity – logins & rules.

- Deploy an email security solution equipped with anti-evasion algorithms.

- Embrace new and emerging innovative technologies.

#BHUSA @BlackHatEvents

## Slide 28

# **Thank You!**

Contact:din.serussi@perception-point.io Visit our website **:** perception-point.io Twitter: @AttackTrends

#BHUSA @BlackHatEvents
