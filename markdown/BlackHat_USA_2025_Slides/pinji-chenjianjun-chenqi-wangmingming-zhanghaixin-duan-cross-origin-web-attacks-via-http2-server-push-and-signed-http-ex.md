---
title: "Cross-Origin Web Attacks via HTTP2 Server Push and Signed HTTP Exchange"
speakers: ["Pinji Chen", "Jianjun Chen", "Qi Wang", "Mingming Zhang", "Haixin Duan"]
conference: "Black Hat"
conference_full: "Black Hat USA 2025"
edition: "USA"
year: 2025
source_pdf: "BlackHat_USA_2025_Slides/Pinji Chen&Jianjun Chen&Qi Wang&Mingming Zhang&Haixin Duan_Cross-Origin Web Attacks via HTTP2 Server Push and Signed HTTP Exchange.pdf"
pages: 52
sha256: "281a51acd2514dbf15e9323ca797656f5ddb0996c6abad94a5eb307bff43a97f"
text_chars: 18875
ocr_pages: 5
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T22:59:05Z"
---
# Cross-Origin Web Attacks via HTTP2 Server Push and Signed HTTP Exchange

**Speakers:** Pinji Chen, Jianjun Chen, Qi Wang, Mingming Zhang, Haixin Duan  
**Conference:** Black Hat USA 2025  
**Source:** `BlackHat_USA_2025_Slides/Pinji Chen&Jianjun Chen&Qi Wang&Mingming Zhang&Haixin Duan_Cross-Origin Web Attacks via HTTP2 Server Push and Signed HTTP Exchange.pdf` (52 pages)


## Slide 1

## Cross-Origin Web Attacks via HTTP/2 Server Push and Signed HTTP Exchange

Speaker: Pinji Chen

Contributors: Jianjun Chen, Qi Wang, Mingming Zhang, Haixin Duan

#BHUSA   @BlackHatEvents

## Slide 2

### Talk Roadmap

- **What is SOP and What has been changed in today’s “origin” definition?**

- **What novel threats/attacks would this change bring to the Web?**

   - Our work: CrossPUSH and CrossSXG attack

- **Are these attacks practical in the real world?**

   - Some practical attack techniques caused by Web PKI weakness

   - A real-world case we found

#BHUSA   @BlackHatEvents

## Slide 3

#### “URI-based” same-origin policy(SOP)

- **SOP is a cornerstone of web security**

 designed to safeguard user data against cross-origin attacks

- **URI-based origin**

   - triple of { **scheme** , **host** , **port** }

   - e.g. {“https”, “a.com”, “443”}

Web Server

(a.com)

SOP Isolation
Web Server
(b.com)
a.com b.com
GET http://b.com/1.png
HTTP response

Browser

#BHUSA   @BlackHatEvents

## Slide 4

# Do you know other definition of origin

#BHUSA   @BlackHatEvents

## Slide 5

#### “SAN-based” origin

######  **HTTP/2 and HTTP/3 consider any hosts listed in the SAN of the certificate are same origin (RFC9110--HTTP Semantics, RFC9113--HTTP/2, SXG draft)**

Subject Alternative Name (SAN)

- ***.google.com TLS certificate is shared with many hosts**

   - *.android.com, *.youtube.com, admob-cn.com, gkecnapps.cn,

*.widevine.cn, *.ggpht.cn  ...

#BHUSA   @BlackHatEvents

## Slide 6

#### SAN-based origin is more permisssive

 **<u>96% certificates have multiple domains in SAN list. Even 3.2 %</u> contain domains from different organizations**<sup>**[1]**</sup>

**multi-domain shared certificate is general**

[1] Cangialosi F et al. Measurement and analysis of private key sharing in the https ecosystem[C]//Proceedings of the 2016 ACM SIGSAC Conference on Computer and Communications Security. 2016: 628-640.

#BHUSA   @BlackHatEvents

## Slide 7

#### SAN-based origin is more permisssive  **96% certificates have multiple domains in SAN list. Even 3.2 %** **<u>contain domains from different organizations</u>**<sup>**[1]**</sup>

SAN-based Origin
URI-based Origin
https://org1-sub.com
https://org1.com/dir1
https://org 3 .com
https://org1.com/dir2
https://org 4 .com
SAN is more permissive!!!

[1] Cangialosi F et al. Measurement and analysis of private key sharing in the https ecosystem[C]//Proceedings of the 2016 ACM SIGSAC Conference on Computer and Communications Security. 2016: 628-640.

#BHUSA   @BlackHatEvents

## Slide 8

What novel threat would this more perimissive origin bring to the Web?

#BHUSA   @BlackHatEvents

## Slide 9

# CrossPUSH and CrossSXG attack

#BHUSA   @BlackHatEvents

## Slide 10

#### Server Push and SXG

HTTP/2 Server Push Signed HTTP Exchange (SXG)
Browser Server Browser 3rd Party Server
verify
verify OK, decode
req html req resource
html
resource’s SXG
resource’s SXG
server push css

######  **Two server delivery mechanism designed to improve web performance**

#BHUSA   @BlackHatEvents

## Slide 11

#### Common characteristics and implication

- **Insight-1: They both comply with the the SAN-based origin (RFC9113--HTTP/2, SXG draft)**

- **Insight-2: They can both indicate (spoof) their origins in shared certfiicate through server response (by “:authority” pseudo header and “request-url” signature header)**

#BHUSA   @BlackHatEvents

## Slide 12

#### Common characteristics and implication

- **Insight-1: They both comply with the the SAN-based origin (RFC9113--HTTP/2, SXG draft)**

- **Insight-2: They can both indicate (spoof) their origins in shared certfiicate through server response (by “:authority” pseudo header and “request-url” signature header)**

**Attackers can push/provide assets to other origins in SAN list, even the origin is hold by other organizations**

#BHUSA   @BlackHatEvents

## Slide 13

#### CrossPUSH and CrossSXG attack

Browser

attacker.com

victim.com

#BHUSA   @BlackHatEvents

## Slide 14

#### CrossPUSH and CrossSXG attack

Browser

attacker.com

victim.com

SAN: **attacker.com** victim.com victim2.com victim3.com

① acquire a certificate shared with victim’s websites

#BHUSA   @BlackHatEvents

## Slide 15

#### CrossPUSH and CrossSXG attack

Browser

attacker.com
② lure users to visit attacker.com

SAN: **attacker.com** victim.com victim2.com victim3.com

① acquire a certificate
shared with victim’s
websites
victim.com

#BHUSA   @BlackHatEvents

## Slide 16

#### CrossPUSH and CrossSXG attack

attacker.com
Browser
② lure users to visit attacker.com
③ server push or SXG indicates
script’s origin as victim.com

victim.com

SAN:
attacker.com
victim.com
victim2.com
victim3.com
① acquire a certificate
shared with victim’s
websites
...

#BHUSA   @BlackHatEvents

## Slide 17

#### CrossPUSH and CrossSXG attack

attacker.com
Browser
victim.com
④ browser accepts malicious cross-
origin script as same-origin and
executes it when requesting
victim.com
② lure users to visit attacker.com
③ server push or SXG indicates
script’s origin as victim.com

SAN: **attacker.com** victim.com victim2.com victim3.com ① acquire a certificate shared with victim’s websites

#BHUSA   @BlackHatEvents

## Slide 18

#### CrossPUSH and CrossSXG attack

SAN:
attacker.com
attacker.com victim.com
victim2.com
victim3.com
Browser
① acquire a certificate
shared with victim’s
websites
victim.com
Security implication
 Enabling  off-path attackers  to launch practical  web attacks  with  shared certificate .
④ browser accepts malicious cross-
origin script as same-origin and
executes it when requesting
victim.com
② lure users to visit attacker.com
③ server push or SXG indicates
script’s origin as victim.com  ...

 Exploitations: Cross-Site Scripting (XSS), Cookie Manipulation, HSTS Bypass...

#BHUSA   @BlackHatEvents

## Slide 19

Various exploitation——leverageing HTTP body  **Exploit-1** ： **Universal XSS**

Header

------------------------------Content-Type: text/html Content-Length: 128

Body

<html> <body> Welcome, Alice! <script> alert("XSS!"); </script> </body> </html>

#BHUSA   @BlackHatEvents

## Slide 20

###### Various exploitation——leverageing HTTP body

 **Exploit-1** ： **Universal XSS**

**We control whole HTTP response**



Header

Body

Content-Type: text/html Content-Length: 128

<html> <body>

Welcome, Alice! <script> alert("XSS!"); </script> </body> </html>

 **Universal:** whether the target website has vulnerabilities, is offline, or no longer exists, our attack still works

 **Robust:** security policies like Content Security Policy (CSP) cannot prevent such attack

#BHUSA   @BlackHatEvents

## Slide 21

###### Various exploitation——leverageing HTTP body

 **Exploit-1** ： **Universal XSS**

**We control whole HTTP response**



Header

Body

Content-Type: text/html Content-Length: 128

<html> <body>

Welcome, Alice! <script> alert("XSS!"); </script> </body> </html>

 **Universal:** whether the target website has vulnerabilities, is offline, or no longer exists, our attack still works

 **Robust:** security policies like Content Security Policy (CSP) cannot prevent such attack

Credit: **@Zedd and @Ehhthing** Blog: https://tttang.com/archive/1703/

#BHUSA   @BlackHatEvents

## Slide 22

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
blackhat > SS > t SOBEL
BRIEFINGS = —. ee, » 4A
Case 1: Universal XSS
```

## Slide 23

###### Various exploitation——leveraging HTTP header

 **Exploit-2** ： **Cookie manipulation**

 **Exploit-3** ： **HSTS bypass**

Header

Content-Type: text/html Content-Length: xxx Set-Cookie: mycookie=Hacked!; domain=victim.com; path=/; expires=Thu, 07 Aug 2025 00:00:00 GMT

Content-Type: text/html Content-Length: xxx Strict-Transport-Security: max-age=0; includeSubdomains

#BHUSA   @BlackHatEvents

## Slide 24

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
black hat y - a 7 ’ OG
BRIEFINGS La — ~— Ve * ’ Low
Case 2: Set Arbitrary Cookie
```

## Slide 25

Various exploitation——leveraging body and header  **Exploit-4** ： **Malicious file download**

Header

Body

Content-Type: text/html Content-Length: xxx Content-Disposition: attachment; filename=`notification`; ---------------------------------------------------binary content of trojan.exe

#BHUSA   @BlackHatEvents

## Slide 26

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
piseichat NS ff A yg és
BRIEFINGS
```

## Slide 27

### Wait...

### That’s great, but... Are these attacks practical in the real world?

#BHUSA   @BlackHatEvents

## Slide 28

# Techniques to make our attack practical

#BHUSA   @BlackHatEvents

## Slide 29

#### Attack practicality

 **How to acquire attack condition (shared certificate)?**

 **How to extend attack duration?**

 **How to bypass potential countermeasure (certificate revocation)?**

#BHUSA   @BlackHatEvents

## Slide 30

##### How to acquire attack condition (shared certificate)

 **Accidental flaws**

 unsecured file uploads in the “/.well-known” directory

 unprotected “_acme-challenge” DNS records under domain ownership  email provider’s oversight in protecting the domain’s administrative email addresses

#BHUSA   @BlackHatEvents

## Slide 31

##### How to acquire attack condition (shared certificate)

 **Accidental flaws**

 unsecured file uploads in the “/.well-known” directory

 unprotected “_acme-challenge” DNS records under domain ownership  email provider’s oversight in protecting the domain’s administrative email addresses

- **Inherent vulnerabilities —— our focus**

- observation

There is no coercive measure to keep the certificate and domain owner in line!!!

#BHUSA   @BlackHatEvents

## Slide 32

How to acquire attack condition (shared certificate)  **Misalignment between certificate owner and domain owner create attack condition**

 **Method 1: Domain Reselling**

 **Method 2: Domain Takeover**

Attacker can issue a multi-domain certificate and then resell part of the included domains to victims

Attacker can take over dangling domains and issue shared certificates

① buy domains

a.com b.com c.com d.com......

② register shared certificates

③ popularize domains and resell domains to victims

Victims

a.com b.com c.com d.com......

Public VPS IP /

dangling DNS records

CDN
issue shared certificate
via HTTP mode

Attacker Server

#BHUSA   @BlackHatEvents

## Slide 33

##### How to extend attack duration?

######  **Validation reuse extend the attack duration**

attacker takeover victim re-control <u>victim domain</u> victim domain Traditional **T** dangling domain period domain takeover

certificate expiration

expiration
our attack duration time 398  -  T
Our attack  T
without
validation reuse
Certificate Lifetime
( 398 days )

#BHUSA   @BlackHatEvents

## Slide 34

##### How to extend attack duration?

 **Validation reuse extend the attack duration**

attacker takeover  victim re-control
victim domain victim domain
Traditional  T  dangling domain period
domain
takeover
certificate
expiration
our attack duration time 398  -  T
Our attack  T
without
validation reuse
Certificate Lifetime
reissue the  certificate
( 398 days ) certificate expiration
our attack duration time 796  -  T
Our attack  T
with
validation reuse
Domain Validation Reuse  Certificate Lifetime
Period ( 398 days ) ( 398 days ) #BHUSA   @BlackHatEvents

#BHUSA   @BlackHatEvents

## Slide 35

##### How to extend attack duration?

######  **Validation reuse extend the attack duration**

Our attack is still valid for more than two years even after dangling DNS record is removed

attacker takeover  victim re-control  Our attack is still valid for more than two years
victim domain victim domain even after dangling DNS record is removed
Traditional  T  dangling domain period
domain
takeover
certificate
expiration
our attack duration time 398  -  T
Our attack  T
without
validation reuse
Certificate Lifetime
reissue the  certificate
( 398 days ) certificate expiration
our attack duration time 796  -  T
Our attack  T
with
validation reuse
Domain Validation Reuse  Certificate Lifetime
Period ( 398 days ) ( 398 days )

certificate
expiration

#BHUSA   @BlackHatEvents

## Slide 36

#### How to bypass potential countermeasures?

 **Shared certificate makes illegitimate certificate irrevocable**

**Victim countermeasure: check CT logs and revoke illegitimate certificates**

**Our bypass technique: shared certificate include both attacker.com and victim.com**

SAN:
attacker.com
victim.com
victim2.com
victim3.com

- Requirements for revoking a certificate<sup>[2]</sup> :

   - (1)  Pass DOV for all domains    OR

   - (2)  Possess the private key

#BHUSA   @BlackHatEvents

[2] https://letsencrypt.org/docs/revoking/

## Slide 37

#### How to bypass potential countermeasures?

 **Shared certificate makes illegitimate certificate irrevocable**

**Victim countermeasure: check CT logs and revoke illegitimate certificates Our bypass technique: shared certificate include both attacker.com and victim.com**

SAN:
attacker.com
victim.com
victim2.com
victim3.com

- Requirements for revoking a certificate<sup>[2]</sup> :

      - (1)  Pass DOV for all domains    OR

   - (2)  Possess the private key

   - Such shared certificates are irrevocable by victims

#BHUSA   @BlackHatEvents

[2] https://letsencrypt.org/docs/revoking/

## Slide 38

How to bypass potential countermeasures?

 **Shared certificate makes illegitimate certificate irrevocable**

**Victim countermeasure: check CT logs and revoke illegitimate certificates Our bypass technique: shared certificate include both attacker.com and victim.com**

SAN: attacker.com victim.com victim2.com victim3.com

 Requirements for revoking a certificate<sup>[2]</sup> :

- (1)  Pass DOV for all domains    OR

- (2)  Possess the private key

Such shared certificates are irrevocable by victims

We conducted experiment on ZeroSSL to report an illegitimate certificate shared with our domains on official problem reporting platform. No reply.

#BHUSA   @BlackHatEvents

[2] https://letsencrypt.org/docs/revoking/

## Slide 39

#### Large scale evaluation

###### **Client-Side**

###### **Server Side**

Websites  allow
Browser  accepts  Cross-Origin
attackers to acquire a
server push and SXG web attacks
shared certificate

- Client-Side test target:

   - Server-Side test target:

- (1) Top-Used browsers on Statcounter<sup>[3]</sup>

   - (1) Reselling domains in Tranco 1M

- (2) Default browsers on leading mobiles

   - (2) Dangling domains in Tranco 1M

- (3) Celebrated applications on app store

- (3) Existing cert-sharing domains in Tranco 1K

[3] https://gs.statcounter.com/browser-market-share

#BHUSA   @BlackHatEvents

## Slide 40

### Client-side evaluation

 **PSChecker (deployed a month)**

⑤ Support the feature: post success logs

① Users’ daily requests

Users ② Respond iframe link ③ Request ④ Return scripts for measuring of feature iframe server push and SXG support measurement server ⑥ Catch error: post failure logs ⑦ Post request logs

High-Traffic website

Feature measurement

Log server

server

#BHUSA   @BlackHatEvents

## Slide 41

### Client-side evaluation

 **Latest version of 11 top-used browsers and 5 default mobile browsers are vulnerable**

- **OS WebView spread the threat to third-party applications**

#BHUSA   @BlackHatEvents

## Slide 42

### Server-side evaluation

######  **Measure reselling domains**

Use **WHOIS history data** to identify which domain has been resold to others

 **Measure dangling domains**

Utilized the state-of-the-art tool, **HostingChecker**<sup>[4]</sup> , to discover dangling domains

[3] Zhang M, Li X, Liu B, et al. Detecting and measuring security risks of hosting-based dangling domains[J]. Proceedings of the ACM on Measurement and Analysis of Computing Systems, 2023, 7(1): 1-28.

#BHUSA   @BlackHatEvents

## Slide 43

### Server-side evaluation

######  **Measure reselling domains**

Use **WHOIS history data** to identify which domain has been resold to others

- **Measure dangling domains**

Utilized the state-of-the-art tool, **HostingChecker**<sup>[4]</sup> , to discover dangling domains

- **Measure cert-sharing domains**

   1. Scrape all domain names listed in the SAN of certificates from the top 1K websites

   2. Extract subdomains from **HTTP responses, CT logs, and passive DNS databases** .

   3. Check whether these associated domains share certificates with the top 1,000 websites.

[3] Zhang M, Li X, Liu B, et al. Detecting and measuring security risks of hosting-based dangling domains[J]. Proceedings of the ACM on Measurement and Analysis of Computing Systems, 2023, 7(1): 1-28.

#BHUSA   @BlackHatEvents

## Slide 44

### Server-side evaluation

######  **Numerous websites are affected**

**Cert-Sharing Domains**

**Reselling Domains Dangling Domains Scope** Tranco Top 1M Tranco Top 1M and subdomains **Count 11741 4919**

Tranco Top 1K

**829**

**4919**

**ftstatic.com (rank** A subdomain of **3895)** was once **windowsupdate.com Case** resold from an from **Microsoft** is Australian food **Study** dangling, which can company to an be registered by American attacker. advertising agency.

Many Top 1K domains are sharing certificates with domains out of 1M (even from different organizations) , like **baidu.com (rank 107)**

#BHUSA   @BlackHatEvents

## Slide 45

# Talk is cheap, show me your real-world case

#BHUSA   @BlackHatEvents

## Slide 46

### Microsoft case

14.au.www.download.windowsupdate.com

attacker server IP

dangling CNAME

A

au.download.windowsupdate.qtlcdnect.com

qtlcdnect.com **unregistered**

au.download.windowsupdate.qtlcdnect.com configure on DNS qtlcdnect.com **controlled**

**attacker buy and register qtlcdnect.com**

#BHUSA   @BlackHatEvents

## Slide 47

### Microsoft case

Microsoft case
verified
domain ownership
14.au.www.download.windowsupdate.com attacker server IP
dangling CNAME A
au.download.windowsupdate.qtlcdnect.com au.download.windowsupdate.qtlcdnect.com
configure on
DNS
qtlcdnect.com   unregistered qtlcdnect.com   controlled
attacker register

#BHUSA   @BlackHatEvents

## Slide 48

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
BRIEFINGS
Universal XSS
```

## Slide 49

### Mitigation

 **For browser vendors**

   - Enforcing consistent authority (IP) in browsers to mitigate CrossPUSH

   - Enforcing single-domain certificates to mitigate CrossSXG

- **For certificate authorities**

   - Facilitating the removal of domains from shared certificates at the request of domain owners listed in the SAN

- **For users**

 Inspecting certificate status in domain registration

#BHUSA   @BlackHatEvents

## Slide 50

### Responsible disclosure

Received Confirmed Fixed
9 vendors 7 vendors 5 vendors
Huawei  Baidu  Microsoft Xunlei 360

Join in our discussion in CA/B NetSec WG!

#BHUSA   @BlackHatEvents

## Slide 51

### Takeaway

**Our Observation:** HTTP/2 and HTTP/3 SAN-based origin is more permissive than browser URI-based origin

**Novel Threat:** CrossPUSH and CrossSXG.

 enable off-path attackers to launch web attacks with shared certificates **Attack Practicality** : Weakness in Web PKI facilitate our attack.

 domain owner                certificate owner (create attack condition)

 domain lifetime              certificate lifetime (extend attack duration)

 control domain               can revoke certificate (bypass countermeasure)

#BHUSA   @BlackHatEvents

## Slide 52

## Thank you ! Q&A

Email:      cpj24@mails.tsinghua.edu.cn Discord:      pinjichen_55767

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
blackhat
BRIEFINGS
AUGUST 6-7, 2025
MANDALAY BAY / LAS VEGAS
Email:
QS <a
NS
=) ww Vii fF i), yy)
Ye Pome fi
Se B ip
SS il
Thank you !
Q&A
cpj24@mails.tsinghua.edu.cn
Discord: __ pinjichen_55/767
```
