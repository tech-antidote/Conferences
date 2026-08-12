---
title: "Hyunho Cho-Operation PoisonedApple Tracing Credit Card Information Theft to Payment Fraud"
speakers: ["Gyuyeon Kim"]
conference: "Black Hat"
conference_full: "Black Hat ASIA 2024"
edition: "ASIA"
year: 2024
source_pdf: "BlackHat ASIA 2024-Slides/Gyuyeon Kim _ Hyunho Cho-Operation PoisonedApple Tracing Credit Card Information Theft to Payment Fraud_compressed.pdf"
pages: 51
sha256: "cf7f22865cf90dcbe068a1d412507dee7015dac680632ccb69b0072d1a7087b7"
text_chars: 21931
ocr_pages: 10
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T00:00:22Z"
---
# Hyunho Cho-Operation PoisonedApple Tracing Credit Card Information Theft to Payment Fraud

**Speakers:** Gyuyeon Kim  
**Conference:** Black Hat ASIA 2024  
**Source:** `BlackHat ASIA 2024-Slides/Gyuyeon Kim _ Hyunho Cho-Operation PoisonedApple Tracing Credit Card Information Theft to Payment Fraud_compressed.pdf` (51 pages)


## Slide 1

## Operation PoisonedApple: Tracing Credit Card Information Theft to Payment Fraud **Gyuyeon Kim & Hyunho Cho Financial Security Institute**

#BHASIA   @BlackHatEvents

## Slide 2

### Who are we?

##### **Gyuyeon Kim**

- **Senior researcher at Financial Security Institute**

- **Focusing on incident response in Korean financial companies, digital forensics and cyber threat intelligence**

##### **Hyunho Cho**

- **Principle researcher at Financial Security Institute**

- **Focusing on investigation of security incidents, digital forensics, penetration tests and vulnerabilities analysis**

# BHASIA   @BlackHatEvents

## Slide 3

### Agenda

#### **01. Introduction 02. Operation PoisonedApple**

**03. Attribution**

**04. Conclusion**

# BHASIA   @BlackHatEvents

## Slide 4

Introduction Discovery of the operation

## Slide 5

### Discovery

###### **November 2022**

###### **September 2022**

select payment method select payment method
Payment method Payment method
general payment general payment
Credit card number Credit card number
Expire date Expire date
CVC number CVC number
Resident ID number Resident ID number
Card PIN Card PIN
Amount Amount
check out cancel check out cancel

online store A

###### **online store B**

# BHASIA   @BlackHatEvents

## Slide 6

### Initial Analysis of phishing payment pages

###### **• Returns the phishing payment page’s URI**

###### **Response from legitimate site**

###### **Request to checkout**

POST http:// shop.coleman.co.krstore’s domain /shop/conf/card/kcp/mobile/ order_approval.php?

site_cd=GKI5M&ordr_idxx=1669698692301&good_mny=285000&pay _method=CARD&escw_used=N&good_name=XP%20%C7%ED%BB %E7%20%C5%B8%C7%C1/MDX+&Ret_URL=http://

shop.coleman.co.krstore’s domain /shop/order/card/kcp/mobile/card_return.php HTTP/1.1

HTTP/1.1 200 OK Date: Tue, 29 Nov 2022 05:12:07 GMT Server: Apache X-Powered-By: PHP/5.2.17 Cache-Control: no-store Content-Length: 156 Connection: close Content-Type: text/html

0000,7gYCff9LSlSkgfSvIxjFNQcHyKIPdQ/iE35VBPEo1cQ=, **https:// rsmpay.kcp.co.kr/pay/mobileGW.kcp**

Host: shop.coleman.co.kr store’s domain

Connection: keep-alive User-Agent: Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36 Accept: */* Referer: http:// shop.coleman.co.krstore’s domain /m2/ord/settle.php Accept-Encoding: gzip, deflate Accept-Language: ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7 Cookie: PHPSESSID=9297b661d4caa2100650f5f9c14f6911; godoLog=20221129; shop_authenticate=Y;

###### **Response from compromised site**

HTTP/1.1 200 OK Date: Tue, 29 Nov 2022 05:25:33 GMT Server: Apache X-Powered-By: PHP Cache-Control: no-store Connection: close Content-Type: text/html

###### **phishing payment page’s URI**

0000,t1yoaefNR+59FTMNxfxfuAcHyKIPdQ/iE35VBPEo1cQ=, **/shop/ skin_ori/campingyo/order/card/KCP/mobileGW.php?url=https:// rsmpay.kcp.co.kr/pay/mobileGW.kcp**

# BHASIA   @BlackHatEvents

## Slide 7

### Detection of additional compromised sites

###### **• Developed our own detection program and analyzed over 5,000 domains**

**Collect domains from search engines**

**Analyze over 5,000 domains**

**Discover over 50 compromised sites**

# BHASIA   @BlackHatEvents

## Slide 8

### Overview of Operation PoisonedApple

###### **Step 1 Analysis of Korean online card payment system**

**Step 3 Steal user’s credit card & personal info**

**Step 2 Hack into online stores, insert phishing payment pages**

**Step 4 Monetization via fraudulent payments (3 schemes)**

# BHASIA   @BlackHatEvents

## Slide 9

### Why Notable?

###### **#1. Stole additional authentication information for fraudulent payments in Korea**

**select payment method Payment method** **general payment Credit card number Expire date CVC number**

Resident ID number
Card PIN
Additional
Password
Amount
check out cancel

**additional information required for authentication**

**phishing payment page**

# BHASIA   @BlackHatEvents

## Slide 10

### Why Notable?

###### **#2. Monetized fraudulent payments and handled the entire process themselves**

source of leakage steal credit card typical methods
Sell on the
dark web
illegal
duplication
new methods
fraud
payment

# BHASIA   @BlackHatEvents

## Slide 11

# Operation PoisonedApple

Analyzing the entire process from credit card information theft to fraudulent payment

## Slide 12

### Resource Development

###### **• Utilized server hosting Vultr and Cloudflare’s CDN services to hide the real IP**

# BHASIA   @BlackHatEvents

## Slide 13

### Initial Access to Online Stores

###### **• Employed various methods to initially access**

1. Execute SQL injection to
victim online store
acquire admin credentials
2. Upload a webshell using
platform vulnerabilities
the threat actor upload phishing pages
3. Hack the administrator
panel

# BHASIA   @BlackHatEvents

## Slide 14

### Phishing Toolkits

###### **• Uploaded toolkits containing all necessary phishing-related components**

# BHASIA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Phishing Toolkits
¢ Uploaded toolkits containing all necessary phishing-related components
< www ob = OO ® wey OT Q
PHP PHP PHP: HP’ Hi H >H PHF PHP PHP
be_ok.php be.php be1.php bc2.php checkCardBin.ph checkRedirectAp error.php hanacard_ok.php hanacard.php hanacard1_step1.
p prvJson.php php
PHE PHP Hi PH PH PHP HF PHP PHP
hanacard1.php hanacard2.php huaka.php huaka1.php index.php kb_ok.php kb_step1.php kb.php kb1.php le_ok.php
PHP PHP 4 PHI 1 PHP PH PHF PHP PHF
le.php le1.php mobileGW.php nh_ok.php nh_step1.php nh.php nh1.php payerror.php phone.php phonecc.php
PHP PHP PHP HI PHP. F PHP PHP
phonekb.php shanxing_ok.php shanxing_step1.p shanxing_step2.p shanxing.php shanxing1_step1. shanxing1.php test.php top.php xandai_ok.php
hp hp php
PHP PHP. PHP. PHP PHP PHP PHP.
xandai_step1.php xandai.php xandai1.php xinghan_ok.php xinghan_step1.ph xinghan.php xinghan1.php
p
```

## Slide 15

### Webshell for Persistence

###### **• Persistently accessed and executed commands on the victim system via a webshell**

# BHASIA   @BlackHatEvents

## Slide 16

### How Phishing payment pages work

victim

enter info

transmit data

transmit data

phishing  phishing
payment page related pages
collect   collect
personal info account info

**threat actor’s server**

store’s  store’s
database web server

# BHASIA   @BlackHatEvents

## Slide 17

### Manipulation of the legitimate payment page

###### **• Manipulated the legitimate payment page to redirect users to the phishing page**

legitimate payment
gateway’s page
store’s domain
store’s domain

phishing
payment page

# BHASIA   @BlackHatEvents

## Slide 18

### Manipulation of the legitimate payment page

Polo Shirt (White) 30 $
select shipping method
select payment method
Shipping Payment method
Agree to terms and conditions
general payment
payment amount
Simple payment Standard payment
Credit card number
amount
Shipping  Expire date
fee 1% cashback on points
CVC number
total
Interest-free for 2-3 months
payment method
Resident ID number
payment Interest-free for 2-3 months
Card PIN
credit card bank transfer samsung BC shinhan
mobile virtual account lotte hana nonghyup
Additional
Password
woori citi more
Purchase confirmation
Amount
terms
proceed cancel
check out cancel

###### **inserted the phishing payment page**

# BHASIA   @BlackHatEvents

## Slide 19

### Collecting additional information

###### **• Extracted users' personal information(Name, ID, PW, IP, etc) using session variables**

# BHASIA   @BlackHatEvents

## Slide 20

### Data exfiltration

###### **• Transmitted and stored all collected information on the threat actor's server**

|**Card number**|**Expiration Date**|**CVC**|**Resident ID**
**number**|**Card PIN**|**Addtional**
**password**|**Address**|
|---|---|---|---|---|---|---|
|**Name**|**Mobile Number**|**Online store**
**login ID**|**Online store**
**login PW**|**User’s IP**|**Browser Details**|**Referer**|

**Stolen information item**

# BHASIA   @BlackHatEvents

## Slide 21

### Detection Evasion: Masquerading

###### **• Phishing page's filename and path masquerading as the legitimate one**

###### **phishing payment page's filename**

###### **phishing payment page’s storage path**

# BHASIA   @BlackHatEvents

## Slide 22

### Detection Evasion: Time-Based Evasion

Check current date and time

Display only on weekends and weeknights
If no cookie, display the phishing payment page
Set cookie after displaying the phishing payment page

# BHASIA   @BlackHatEvents

## Slide 23

### Evolution of the phishing interface

Standard payment
Lotte Card
Simple payment Simple payment
Standard payment
App card payment usage location
Amount
Credit Card Credit card number
CVC number
Credit card number PIN number payment
Expire date
Standard payment
CVC number
Card PIN
Standard payment
Resident ID number
Credit card number
Additional
Password Expire Date
Amount
CVC number Card PIN
Check out

**impersonating simple payment and major credit card companies**

# BHASIA   @BlackHatEvents

## Slide 24

“The threat actor’s **monetization tactics** were nothing short of ingenious.”

# BHASIA   @BlackHatEvents

## Slide 25

### Three ways to Monetize

###### **Case #1**

**Refund after fraudulent payment on the secondhand trading platform**

###### **Case #2**

**Sale of the item and fraudulent payment on the open marketplace**

###### **Case #3**

**Exploit of the Apple Store's ‘Someone else Pick-up’ policy**

# BHASIA   @BlackHatEvents

## Slide 26

### Case #1

###### **• Requested for cash refund after payment for an item on second-hand trading platforms**

**As an apology for canceling the purchase, keep the $20 and refund me the remaining $180.**

**stolen card the threat actor info from phishing page**

**second-hand trading platfrom**

**buyer**

# BHASIA   @BlackHatEvents

## Slide 27

### Case #2

###### **• After the sale of the item, fraudulent payments were made on the open marketplace**

stolen card info
the threat actor
from phishing page
second-hand  open
marketplace
trading platfrom
buyer

# BHASIA   @BlackHatEvents

## Slide 28

### Case #3

###### **• Chatted with the threat actor**

Is it available?

Items for Sale
Newest
First

$ 220
Apple watch SE

16 Feburary 2023

# BHASIA   @BlackHatEvents

## Slide 29

### Case #3

###### **• Exploited of the Apple Store's ‘Someone else Pick-up’ policy**

**the threat actor**

**stolen card info from phishing page**

**second-hand trading platfrom**

**online Apple offline Apple Store Store**

**buyer**

# BHASIA   @BlackHatEvents

## Slide 30

### Case #3

**The threat actor filled the buyer’s info into the recipient’s details field.**

# BHASIA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Case #3
Now fill out your pickup information.
Bring the following for pickup:
* The person picking up the order should bring a valid
government-issued photo ID and the order number.
* Your contact will get an email and a text when the order is
ready for pickup.
Who will pick up your order?
Someone else
will pick it up
I'll pick it up
View Apple Pickup Policy >
For best service, please arrive during your reserved time or
you may experience a delay picking up your order. Your order
will be held for 7 days.
First Name
Last Name
Email Address
Phone Number
The threat actor filled the buyer’s info
into the recipient’s details field.
(_) Send pickup notifications via text message to the phone
number above.
What's your contact information?
We'll email you a receipt and order updates.
| Email Address Y 7 .
The phone number you enter can’t be changed after you
| Phone Number ee
place your order, so please make sure it's correct.
```

## Slide 31

Attribution EvilQueen : Uncovered a new Chinese threat actor

## Slide 32

### OPSEC failures (1/3)

###### **• found an email address of the threat actor in the phishing page's source code**

# BHASIA   @BlackHatEvents

## Slide 33

### OPSEC failures (1/3)

- 6a44f0942c2bbc8643016d96602e9e27

- 1ba8b781aa146dec0e3ed43824b249a4

# BHASIA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
OPSEC failures (1/3)
ynwtuukf —.—— > ynwtuukf.net ynwtuukf.net/test.php ——————> ynwtuukf.net/mysql.php
ET
SACS CANE BORA SENSO ByORKAP HyoPHP HuosQr #FeKT
$6 * a my S
z lol: [eRO!
® e586 sane.) meee
# 2eee-|/aeses Rowe ane) ARLME CAR
a Adminer 4.8.1 B79!
now (2e | iteemne Mom me
ita
HOVEMO|~ BA MySQL v
rs ai
ynwtuu.net
APB 7401
itm ik wee
krpay ; sean
am eHOIEIHOIA
\edacom 2
nm
2121 | O8F4e2 S79!
——+ ynwtuukf.cn MW __ pharming malware
ay
Qi
6a44f0942c2bbc8643016d96602e9e27
1ba8b781aa146dec0e3ed43824b249a4
```

## Slide 34

### OPSEC failures (2/3)

accounts dump source: https://www.virustotal.com/gui/file/c25fb3e834316f7c013df5446da1786f4483266f6d56701304af0c41fdfc1577

# BHASIA   @BlackHatEvents

## Slide 35

### OPSEC failures (3/3)

###### **• attempted hacking against Korean websites between 2009 and 2016**

# BHASIA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
OPSEC failures (3/3)
— SHJXE GllO|=S+ (ynwtuukf) mel: 1
A S7 | T}2: =] asp.asa (2.3KB) ASI: 1064
AS: etuetue
= fthsth
= 4 Ky Ad 2 nee *EMMBLAlS MSA SO] GIES ALO] AS OH SS Holl 71H aH SAD
- HAA HHz4(95,97,2000,xp,2003,2007):
S+EREHEESTERRRSTE CHEE * OfeHBOl ARS AyS}A/2 >>
di Sey HANS Ala]
i) php (44byte art
F) 23.jp9 (44byte — pe
©) 23.ip9 (44byte
©) 23. php.ipg (46byte
8 24 tt St Ba9|
C13 (07H) *
4 A
on
=) = aA |
42! : 2010-02-26(01:41)
(2tS31-2S Al) wrtywr<iframe src=http://mp.gemmir.com/upload_file_test/Movie/index. htm 8549 : 2010-02-26(01:41)
width=100 height=0> </iframe>
ig}
ne
bot
i
```

## Slide 36

### Correlation analysis

# BHASIA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Correlation analysis
17fce1...678a
: : en 2
rua WW wh H : nee
ue a  pay.ynwtuukf.net
~ :
a3283e...e7dd ynwtuukf.cn —~@ Cua KX CO. o
“ieaeeenaenarannnannnnensnenonsrararasaranasarasssasnsnsnensnsrarsnanararansnaracsescccsecensnsseeessn® ilQueen 8g pg
oo metamask phishing Sd edeie ae teatadadas a ebtiacemeatelue ieeccae sean ceoadadacnead aia © teeeeee, _ i ff7347...fa28
“ (i) a : codé-sighi
(W WW) 3 : letificaty,
_ : :
a : :
Cy * defi-con.cn wan -com : 1
> : H
LTS : :
QO gee 967c49...9726
; OS (Ge) | : :
? web-cot.com SS |
: china-metamask.tw f 91f830...7892
i 75f0c8...de775
a a
metamask3.cn
103.60.109.137
```

## Slide 37

### Timelines

**Operation “PoisonedApple” targeting Korea and Japan**

Duty-free and Outlet phishing targeting Korea and Japan

Various web hacking targeting Korea and Japan targeting Korean websites 2015 ~ 2017 July 2022 December 2023 2009 ~ 2016 May - July 2023 2021 ~ 2023 Malicious Apps disguised as obituaries Metamask phishing targeting Korea Pharming malware targeting Taiwan and China targeting Korea

# BHASIA   @BlackHatEvents

## Slide 38

### Timelines

Operation “PoisonedApple”
targeting Korea and Japan
Duty-free and Outlet phishing
Various web hacking
targeting Korea and Japan
targeting Korean websites
2015 ~ 2017 July 2022 December 2023
z
2009 ~ 2016 May - July 2023
2021 ~ 2023
Malicious Apps disguised
as obituaries
Metamask phishing
targeting Korea
Pharming malware
targeting Taiwan and China
targeting Korea
# BHASIA   @BlackHatEvents

## Slide 39

### Metamask phishing site and apps

- **created multiple domains for MetaMask phishing**

# BHASIA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Metamask phishing site and apps
Si METAMASK Features ¥ Support
Acrypto wallet &
gateway to
blockchain apps
Start exploring blockchain applications in seconds. Trusted
by over I million users worldwide.
Download now
LEARN MORE
Buy, store, send and swap tokens
Available as a browser extension and as a mobile
app, MetaMask equips you with a key vault, secure
login, token wallet, and token exchange-
everything you need to manage your digital
assets.
About ¥ Build v
¢ created multiple domains for
MetaMask phishing
$228.77
ED Email Address v7 Exactly Matching Sa! ynwtuukf@zohomail.com
Expand Your Search
6
domains
Narrow Your Search
Search
Download Report
Displaying results: 1-60f6 Prev Next
Domain Name Create Date Registrar
china-metamask.tw -- a
cn-metamask.cn 2024-02-20 ss
defi-cot.cn 2023-08-15 oo
metamask2.cn 2022-08-08 DYNADOTCHINA LLC
. metamask3.cn 2022-08-23 DYNADOTCHINA LLC
metamask3.tw = =
```

## Slide 40

### Duty-free shop phishing site

###### **Impersonation of a famous department store in Korea**

# BHASIA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Duty-free shop phishing site
oS C  @ noons.kr fh 10 &©8 2a €. :
HSHuc [222 (sala S0H0%] SUAVBy PUAN BABAE MoAirio
ak Al &
AA BS Suoj4) ABE DS
a
@ xs
Impersonation of afamous_ °
department store in Korea
Apple Of0j@4= 10.2 20214 9M/C} Wi-Fi Apple 2022 OFO}ZH= oo SAICH ALIA BA AISRS 44mm SERA OfOHSt TES QA|CH BHA [HZ
Qa
¥350,0002! ¥650,0002 ¥200,0002) ¥250,0002
‘ef?
@ Sue
```

## Slide 41

### Outlet phishing sites

###### **Impersonation of a famous outlet brand in Korea**

TV Refrigerator Dryer Dishwasher Smartphone Sales TV Refrigerator Dryer Dishwasher Smartphone
name
card companies
expire date
credit card number
cvc
birth date
credit card password
installment months

**Stealing credit card and personal information**

# BHASIA   @BlackHatEvents

## Slide 42

### Malicious Apps disguised as funeral notice

###### **• malicious apps disguised as funeral notice that steal and control smartphone data**

I regret to inform you of
the passing of my father.
 Funeral information:
  https://t.ly/A_CBz

**filename : moblie funeral notice.apk funeral notice**

During a long illness, my father passed away last night. The funeral arrangements will proceed as follows.

view

# BHASIA   @BlackHatEvents

## Slide 43

### Linked with China

# BHASIA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Linked with China
z
RARPAK [pre O ames
a aR seas
RR RitiE EAR BHPLERBES Fee ( Hest) BRR Sawa
TAM ARAB Q | WR: ABicR M2 RF am
BARRiCin Rah AAR }
MARRR 98:1 y | 2G:674| #e:5 gy KGB (27) }
Es 488 #41 °2)3 4 5 6 7/8)9 > 10 1.34 6 /34R FR
2HhED may FA TAM WE BS 7H f# os/aa }
SRBEMEAASOO , TLE. GE ..23 45 6.38 652598 ara
RUESH ENA! Ow 234.5 6..38 sdzbzp1 373 }
HTARNKFREAIR—T , MAMGMNIFIC Oe ..23 45 6.38 dajiefie fa
RRVASA , PURI OM ...2 3 45 6.38 dajiejie at }
RIBS iA wURIT ORY ...2 3-45 6.. 38 anwangosig (373
6AMWEE OM ..23 45 6..38 856 375 }
SBR Ce ATUL A SC SR TERE AK OTR AKA ATMs GB ..2 345 6.38 byzps 573
SRR TUNA © OR ..2 3.45 6.38 xsm Be }
BMAN-LAMBABBRE OH ..23 45 6..38 BARRER bob
SAQWSE OM ...2 345 6..38 856 aa }
BY IN7- MMA OMS ...2 345 6..38 856 nod
M23:25FFHHBI17S23:2545R. GE ..2 345 6..38 856 372 }
3AR, 4AM. KFRE. OM ...23 45 6..38 856
```

## Slide 44

### Linked with China

 Profile

 name  nickname
gender country
language timezone

phone number

# BHASIA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Linked with China
Domain Name: ynwtuukf.net
Registry Domain ID: 1917446201_DOMAIN_NET-VRSN
Registrar WHOIS Server: whois.hichina.com
Registrar URL: http://www.net.cn/
Updated Date: 2015-04-08T07:42:21Z
Creation Date: 2015-04-08T07:42:21Z
Registrar Registration Expiration Date: 2016-04-08T07:42:21Z
Registrar: HICHINA ZHICHENG TECHNOLOGY LTD.
Registrar IANA ID: 420
Registrar Abuse Contact Email: abuse@list.alibaba-inc.com
Registrar Abuse Contact Phone: +86.4006008500
Reseller:
Domain Status: ok http://www.icann.org/epp#0K
Registrant Name: Han Cheng Xiang
Registrant Organization: Han Cheng Xiang
Registrant Street: Shan Dong Zhang Dian Qu,,
Registrant City: Tian Jin Shi
Registrant State/Province: shan dong
Registrant Postal Code: 523645
Registrant Country: CN
Registrant Phone: +86.0213565373
Registrant Phone Ext: 3423
Registrant Fax: +86.0213565373
Registrant Fax Ext: 3423
Registrant Email: ynwtuu@126.com
Registry Admin :
Admin Name: Chang Ping
Profile
AS Be /0/E G0|H10}
ynwtuukf@zohomail.com
nickname
ia)
gender country
RE as RB
language timezone
(GMT 0:00) #844 BR58 tine BTi8) ( Europe/London )
phone number
AAD AAS SE AYR HSH YD eel eric}
(+86) 17050896830
```

## Slide 45

### EvilQueen

###### **Uncovered a new Chinese Threat actor has been active at least since 2009.**

**Objective : Monetization through financial information theft**

**Targets : Korea, Japan, Taiwan**

**Tools : Chinese Webshell, PHP-based phishing pages, Dirty Cow, Adminer, etc. TTPs : Phishing, Fradulent Payments, Malicious android apps, etc.**

|**Resource**
**Development**|**Initial Access**|**Execution**|**Persistence**|**Defense Evasion**|**C&C**|**Exfiltration**|
|---|---|---|---|---|---|---|
|Acquire Infrastructure:
Domains|Exploit Public-Facing
Application|Command and
Scripting Interpreter:
Unix Shell|Server Software
Component: Webshell|Masquerading: Match
Legitimate Name or
Location|Application Layer
Protocol: Web|Automated Exfiltration|
|Acquire Infrastructure:
Virtual Private Server|Phishing||Valid Accounts:
Local Accounts|Indicator Removal:
File Deletion||Exfiltration Over C2
Channel|
|Obtain Capabilities:
Tool and Exploits|External Remote
Services|||Time Based Evasion|||

# BHASIA   @BlackHatEvents

## Slide 46

### Recent Incident

###### **$10,000 was charged on a stolen card at an apple store…**

**A stolen card was used to make a $10,000 payment at an Apple store** , but Apple's refusal to cooperate due to internal regulations has hindered the investigation. Despite Mr. Yoon's efforts to report the incident to both the card company and the police immediately, Apple's lack of cooperation has led to over a month of investigation delays. **Apple's refusal to provide any information, citing internal policy** , has sparked criticism both domestically and in the United States, despite the company's emphasis on privacy protection.

source: https://www.hankyung.com/article/2024020827807

# BHASIA   @BlackHatEvents

## Slide 47

# Conclusion Takeaways

## Slide 48

### Summary of Operation PoisonedApple

**Activity : Theft of credit card and personal data using phishing pages on online stores, fraudulent payment and monetization**

**Victims : Over 50 online stores, Over 8,000 cardholders, and 5 millions of personal information.**

**Geographical scope : Korea, Japan**

**Period of activity : 2 years**

**Revenue : $ 400,000**

**Whitepaper Download QR Code**

# BHASIA   @BlackHatEvents

## Slide 49

### Black Hat Asia Sound Bytes

# BHASIA   @BlackHatEvents

## Slide 50

### Black Hat Asia Sound Bytes

- <sup>**Through analysis starting from small clues, we ultimately discovered phishing pages**</sup> **spreading widely online and identified various attack activities**

   - **Attackers are developing new novel schemes for financial gain, making it very important to continually explore and share new skills and tactics to respond to upcoming greater threats.**

   - **Collaboration among stakeholders played a crucial role in minimizing the attack's impact, highlighting the essentiality of collaborative response for enhancing resilience against incidents.**

# BHASIA   @BlackHatEvents

## Slide 51

# Thank you **gykim@fsec.or.kr**

#BHASIA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ASIA 20
RIL 18-19, 2024
BRIEFINGS
Thank you
gykim@fsec.or.kr
```
