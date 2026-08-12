---
title: "Cookie Crumbles Unveiling Web Session Integrity Vulnerabilities"
speakers: ["Marco Squarcina", "Pedro Adão"]
conference: "Black Hat"
conference_full: "Black Hat USA 2023"
edition: "USA"
year: 2023
source_pdf: "Black Hat USA 2023 slides/Marco Squarcina & Pedro Adão_Cookie Crumbles Unveiling Web Session Integrity Vulnerabilities.pdf"
pages: 59
sha256: "6f90c6d1d48622fa673fdab03d8a648e5762ff29c037df661e58c1fe8aa4d34a"
text_chars: 30958
ocr_pages: 3
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:19:06Z"
---
# Cookie Crumbles Unveiling Web Session Integrity Vulnerabilities

**Speakers:** Marco Squarcina, Pedro Adão  
**Conference:** Black Hat USA 2023  
**Source:** `Black Hat USA 2023 slides/Marco Squarcina & Pedro Adão_Cookie Crumbles Unveiling Web Session Integrity Vulnerabilities.pdf` (59 pages)


## Slide 1

**Cookie Crumbles: Unveiling Web Session Integrity Vulnerabilities Marco Squarcina Pedro Adão** TU Wien IST, Universidade de Lisboa

IST, Universidade de Lisboa @pedromigueladao https://infosec.exchange/@pedroadao pedro.adao@tecnico.ulisboa.pt

@blueminimal https://infosec.exchange/@minimalblue marco.squarcina@tuwien.ac.at

Joint work with **Lorenzo Veronese** and **Matteo Maffei**

**M. Squarcina, P. Adão // Cookie Crumbles: Unveiling Web Session Integrity Vulnerabilities**

**#BHUSA @BlackHatEvents**

## Slide 2

#### **Who Are We**

- **PhD** @ Ca’ Foscari, Venice, IT

- **Senior Scientist** @ TU Wien, Vienna, AT

- **Web** & **Mobile** ( **in** ) **Security**

- ● **CTF player / organizer** since 2009

- ● Founder of **mhackeroni** (5x **DEF CON CTF** finalist)

   - Playing with **WE_0WN_Y0U**

- IT security education projects with **ENISA** , **CSA** , formerly **Cyberchallenge.IT**

- ● <u>https://minimalblue.com/</u>

**Marco** Squarcina

**M. Squarcina, P. Adão // Cookie Crumbles: Unveiling Web Session Integrity Vulnerabilities**

**#BHUSA @BlackHatEvents**

## Slide 3

#### **Who Are We**

**Pedro** Adão

- **PhD** @ Técnico-Lisboa, PT

- **Associate Prof.** @ Técnico-Lisboa, PT

- ● **Programming Lang** & **Web** ( **in** ) **Security**

- ● **CTF player** since 2013

- Founder of **STT** and **CyberSecurity ChallengePT**

- **Coach Team PT** (ECSC 2019-...)

- **Coach Team Europe** (ICC 2022, 2023)

**M. Squarcina, P. Adão // Cookie Crumbles: Unveiling Web Session Integrity Vulnerabilities**

**#BHUSA @BlackHatEvents**

## Slide 4

**M. Squarcina, P. Adão // Cookie Crumbles: Unveiling Web Session Integrity Vulnerabilities #BHUSA @BlackHatEvents**

## Slide 5

## **Have Weak Integrity**

**M. Squarcina, P. Adão // Cookie Crumbles: Unveiling Web Session Integrity Vulnerabilities**

**#BHUSA @BlackHatEvents**

## Slide 6

2013

**M. Squarcina, P. Adão // Cookie Crumbles: Unveiling Web Session Integrity Vulnerabilities**

**#BHUSA @BlackHatEvents**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Serenis
THE DEPUTIES ARE STILL CONFUSED
RICH LUNDEEN
M. Squarcina, P. Addo // Cookie Crumbles: Unveiling Web Session Integrity Vulnerabilities #BHUSA @BlackHatEvents
```

## Slide 7

2013

2013
2015

**M. Squarcina, P. Adão // Cookie Crumbles: Unveiling Web Session Integrity Vulnerabilities**

**#BHUSA @BlackHatEvents**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
RICH LUNDE
Cookies Lack Integrity: Real-
orld Implications
Xiaofeng Zheng!>, Jian Jiang’, Jinjin Liang'?>, Haixin Duan'!>+, Shuo Chen®, Tao Wan®, and
Nicholas Weaver*7”
‘Institute for Network Science and Cyberspace, Tsinghua University
Department of Computer Science and Technology, Tsinghua University
3Tsinghua National Laboratory for Information Science and Technology
‘International Computer Science Institute
yusenix
ee
‘e
Abstract
A cookie can contain a “secure” flag, indicating that it
should be only sent over an HTTPS connection. Yet there
is no corresponding flag to indicate how a cookie was
ttackers who act as a man-in-the-midddle even tem-
porarily on an HTTP session can inject cookies which
will be attached to subsequent HTTPS connections. Sim-
ilar attacks can also be launched by a web attacker from a
related domain. Although an acknowledged threat, it has
not yet been studied thoroughly. This paper aims to fill
this gap with an in-depth empirical assessment of cookie
injection attacks. We find that cookie-related vulnerabil-
ities are present in important sites (such as Google and
Bank of America), and can be made worse by the im-
plementation weaknesses we discovered in major web
browsers (such as Chrome, Firefox, and Safari). Our
have included privacy violation, on-
a i:
>Microsoft Research Redmond
°Huawei Canada
7UC Berkeley
man-in-the-middle (MITM). However, there is no similar
measure to protect its integrity from the same adversary:
an HTTP response is allowed to set a secure cookie for
its domain, An adversary controlling a related domain
is also capable to disrupt a cookie’s integrity by making
use of the shared cookie scope. Even worse, there is an
asymmetry between cookie’s read and write operations
involving pathing, enabling more subtle form of cookie
integrity violation.
The lack of cookie integrity is a known problem,
noted in the current specification [2]. However, the
real-world implications are under-appreciated. Although
the problem has been discussed by several previous re-
searchers [4, 5, 30, 32, 24, 23], none provided in-depth
and real-world empirical assessment. Attacks enabled by
merely injecting malicious cookies could be elusive, and
the consequence could be serious. For example, a cau-
tious user might only visit news websites at open wireless
M. Squarcina, P. Addo // Cookie Crumbles: Unveiling Web Session Integrity Vulnerabilities
#BHUSA @BlackHatEvents
```

## Slide 8

2013
2015
2019

**M. Squarcina, P. Adão // Cookie Crumbles: Unveiling Web Session Integrity Vulnerabilities**

**#BHUSA @BlackHatEvents**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bi ck Cookies Lack ]
a = = Xiaofeng Zheng!?5, Jian Jiang’, Ji
'nstitute for Network
Department of Compu
3Tsinghua National Lat
‘Interna
yusenix 5M
9 LEE The cookie monster
T H E D) E P | Abstract < !
R | CH LU N D) E A cookie can contain a “secure” flag, indi
should be only sent over an HTTPS connecti
is no corresponding flag to indicate how ¢
set: attackers who act as a man-in-the-midd\ J
porarily on an HTTP session can inject c¢
will be attached to subsequent HTTPS conn
ilar attacks can also be launched by a web at’
related domain. Although an acknowledged,
not yet been studied thoroughly. This papa
this gap with an in-depth empirical assessm|
injection attacks. We find that cookie-rela
ities are present in important sites (such
Bank of America), and can be made wors|
plementation weaknesses we discovered it
browsers (such as Chrome, Firefox, and
ssful attacks have included privacy
: a
@filedescriptor
HITCON 2019
su
1
M. Squarcina, P. Addo // Cookie Crumbles: Unveiling Web Session Integrity Vulnerabilities #BHUSA @BlackHatEvents
```

## Slide 9

2013
2015
2019
2023
rfc6265bis-12

**M. Squarcina, P. Adão // Cookie Crumbles: Unveiling Web Session Integrity Vulnerabilities**

**#BHUSA @BlackHatEvents**

## Slide 10

#### **Cookie Tossing** ( **Same-site Attacker** )

https://example.com https://atk.example.com
Set-Cookie: session= bad;  Secure; domain=example.com
Cookie: session= bad
Attributes Flags
Expires Max-Age Domain Path SameSite Secure HttpOnly
Path  useful to  SameSite  does
prioritize cookies not matter here!

**M. Squarcina, P. Adão // Cookie Crumbles: Unveiling Web Session Integrity Vulnerabilities**

**#BHUSA @BlackHatEvents**

## Slide 11

#### **Cookie Tossing** ( **Network Attacker** )

https://example.com http://example.com
Set-Cookie: session= bad
Cookie: session= bad
Cookies do not follow the
Same Origin Policy
Can also be a subdomain over
HTTP and the forged request
contains a  domain cookie

**M. Squarcina, P. Adão // Cookie Crumbles: Unveiling Web Session Integrity Vulnerabilities**

**#BHUSA @BlackHatEvents**

## Slide 12

#### **Cookie Eviction** ( **Same-site** & **Network Attacker** )

https://example.com https://atk.example.com
Cookie: session= good

**M. Squarcina, P. Adão // Cookie Crumbles: Unveiling Web Session Integrity Vulnerabilities**

**#BHUSA @BlackHatEvents**

## Slide 13

#### **Cookie Eviction** ( **Same-site** & **Network Attacker** )

**https://example.com https://atk.example.com** Cookie: session= good Set-Cookie: x0=_ … Set-Cookie: x199=_ Set-Cookie: session= bad; domain=example.com

**M. Squarcina, P. Adão // Cookie Crumbles: Unveiling Web Session Integrity Vulnerabilities**

**#BHUSA @BlackHatEvents**

## Slide 14

#### **Cookie Eviction** ( **Same-site** & **Network Attacker** )

**https://example.com https://atk.example.com** Cookie: session= good Set-Cookie: x0=_ … Set-Cookie: x199=_ Set-Cookie: session= bad; domain=example.com Cookie: session= bad

**M. Squarcina, P. Adão // Cookie Crumbles: Unveiling Web Session Integrity Vulnerabilities**

**#BHUSA @BlackHatEvents**

## Slide 15

#### **Threat Models**

Dangling DNS Records

Discontinued
Services

**M. Squarcina, P. Adão // Cookie Crumbles: Unveiling Web Session Integrity Vulnerabilities**

**#BHUSA @BlackHatEvents**

## Slide 16

#### **Threat Models**

**1520** vulnerable subdomains

###### **Dangling DNS Records**

**2021**

**cnn.com** , **nih.gov** , **cisco.com** , **f-secure.com** , **harvard.edu** , **lenovo.com** , ...

**Discontinued Services**

**Expired Domains**

**Deprovisioned Cloud Instances**

**Corporate Networks**

**Roaming Services**

**Dynamic DNS Providers**

**M. Squarcina, P. Adão // Cookie Crumbles: Unveiling Web Session Integrity Vulnerabilities**

**#BHUSA @BlackHatEvents**

## Slide 17

90%  of websites deploy
Threat Models partial HSTS
1520  vulnerable
(no IncludeSubdomain )
subdomains
Dangling DNS Records
Expired
2021 Domains
Discontinued
Services
Deprovisioned
cnn.com ,  nih.gov ,  cisco.com ,
Cloud Instances
f-secure.com ,  harvard.edu ,
lenovo.com , ...
Networks Corporate
Services Roaming
Providers Dynamic DNS

**M. Squarcina, P. Adão // Cookie Crumbles: Unveiling Web Session Integrity Vulnerabilities**

**#BHUSA @BlackHatEvents**

## Slide 18

#### **Session Fixation** & **Login CSRF**

**https://bank.com https://atk.bank.com**

Bob

##### **Session Fixation**

**Login CSRF**

- bank.com **does not refresh the session ID after login**

- Attacker obtains a pre-session sid= **s1** and tosses that cookie into Bob’s browser

- Bob authenticates, promoting sid= **s1** to an authenticated session

- **Attacker hijacks Bob’s session** using **s1**

- Attacker has an account on bank.com, with cookie sid= **s2**

- ● Attacker tosses that cookie into Bob’s browser

- When Bob visits bank.com, Bob is **authenticated as the attacker** , leaking sensitive information that can be later accessed by the attacker

**M. Squarcina, P. Adão // Cookie Crumbles: Unveiling Web Session Integrity Vulnerabilities**

**#BHUSA @BlackHatEvents**

## Slide 19

#### **Cross-Origin Request Forgery** ( **CORF** )

https://bank.com https://atk.bank.com Double-Submit
POST /action
if  cookie( csrf )==POST( csrf-tok ):
Cookie:s=x;csrf=y return  True
–  csrf-tok=y return  False
Done!

**M. Squarcina, P. Adão // Cookie Crumbles: Unveiling Web Session Integrity Vulnerabilities**

**#BHUSA @BlackHatEvents**

## Slide 20

#### **Cross-Origin Request Forgery** ( **CORF** )

https://bank.com https://atk.bank.com
POST /action
Cookie:s=x;csrf=y
– csrf-tok=y
Done!
1
Set-Cookie:csrf=z; domain=bank.comz; domain=bank.com; domain=bank.com

1
Set-Cookie:csrf=z; domain=bank.comz; domain=bank.com; domain=bank.com
2
POST /action
POST via  hidden form
Cookie:s=x;csrf=z
submission or  JavaScript
– csrf-tok=z

**Double-Submit if** cookie( **csrf** )==POST( **csrf-tok** ): return **True** return **False Wrong assumption** : attacker can only manipulate the token, but not the cookie!

Trivially  vulnerable  against
same-site attackers, just  toss
and  submit !

**M. Squarcina, P. Adão // Cookie Crumbles: Unveiling Web Session Integrity Vulnerabilities**

**#BHUSA @BlackHatEvents**

## Slide 21

#### **Synchronizer Token Pattern**

- Fixes Double Submit problems by **binding the CSRF token to the session**

● Store a **CSRF secret in the session** and use it to **generate CSRF tokens** generate_func( **CSRF_secret** , params…) = **CSRF_token Attached to HTTP requests via hidden form field** Session      := < **id** , **CSRF_secret** > **Stored in the session** Verify := generate_func( **CSRF_secret** , params…) == **CSRF_token**

Attached to HTTP
requests via
hidden form field

- Overwrite the session cookie? Deauth the user, **NO CORF** , attacker sad :’(

**M. Squarcina, P. Adão // Cookie Crumbles: Unveiling Web Session Integrity Vulnerabilities**

**#BHUSA @BlackHatEvents**

## Slide 22

#### **Synchronizer Token Pattern** ( **Flask-login + Flask-WTF** )

**https://bank.com**

GET /login

**1**

**2**

<input csrf_token= **t0** type="hidden"> Set-Cookie: session={csrf= **s** , _id= **None** }#sign POST /login Cookie: session={csrf= **s** , _id= **None** } #sign – user=bob&password=s3cur3&csrf_token= **t0**

Hi Bob <input csrf_token= **t1** type="hidden"> Set-Cookie: session={csrf= **s** , _id= **bob** }#sign

**s** = sha1(os.urandom(64)).hexdigest()

**t0** = **exp_time0** ##HMAC(SECRET, **s** # **exp_time0** ) **t1** = **exp_time1** ##HMAC(SECRET, **s** # **exp_time1** ) Verification:

**exp_time** , **hmac** = token.split(“##”) if **hmac** == HMAC(SECRET, **s** # **exp_time** ): return **True** return **False**

**3**

POST /action

Cookie: session={csrf= **s** , _id= **bob** } #sign – csrf_token= **t1**

**M. Squarcina, P. Adão // Cookie Crumbles: Unveiling Web Session Integrity Vulnerabilities**

**#BHUSA @BlackHatEvents**

## Slide 23

#### **Synchronizer Token Pattern** ( **Flask-login + Flask-WTF** )

**https://bank.com**

GET /login

**1**

**2**

<input csrf_token= **t0** type="hidden"> Set-Cookie: session={csrf= **s** , _id= **None** }#sign POST /login

Cookie: session={csrf= **s** , _id= **None** } #sign – user=bob&password=s3cur3&csrf_token= **t0**

Hi Bob <input csrf_token= **t1** type="hidden"> Set-Cookie: session={csrf= **s** , _id= **bob** }#sign

**s** = sha1(os.urandom(64)).hexdigest()

**t0** = **exp_time0** ##HMAC(SECRET, **s** # **exp_time0** ) **t1** = **exp_time1** ##HMAC(SECRET, **s** # **exp_time1** ) Verification:

**exp_time** , **hmac** = token.split(“##”) if **hmac** == HMAC(SECRET, **s** # **exp_time** ): return **True** return **False**

**3**

POST /action

Cookie: session={csrf= **s** , _id= **bob** } #sign – csrf_token= **t1**

**M. Squarcina, P. Adão // Cookie Crumbles: Unveiling Web Session Integrity Vulnerabilities**

**#BHUSA @BlackHatEvents**

## Slide 24

CORF Token Fixation  ( Flask-login + Flask-WTF )
https://bank.com https://atk.bank.com
GET /login
1
<input csrf_token= t0  type="hidden">
Set-Cookie: session={csrf= s , _id= None }#sign
2
Set-Cookie: session={csrf= s , _id= None }#sign; domain=bank.com
GET /login
3
Cookie: session={csrf= s , _id= None }#sign Equivalent to an
<input csrf_token= t1  type="hidden"> unauthenticated session fixation
Set-Cookie: session={csrf= s , _id= None }#sign

**M. Squarcina, P. Adão // Cookie Crumbles: Unveiling Web Session Integrity Vulnerabilities**

**#BHUSA @BlackHatEvents**

## Slide 25

CORF Token Fixation  ( Flask-login + Flask-WTF )
https://bank.com https://atk.bank.com
POST /login
4
Cookie: session={csrf= s , _id= None }#sign
 – user=bob&password=s3cur3&csrf_token= t1
Bob authenticates
Welcome Bob!
Set-Cookie: session={csrf= s , _id= bob }#sign

**M. Squarcina, P. Adão // Cookie Crumbles: Unveiling Web Session Integrity Vulnerabilities**

**#BHUSA @BlackHatEvents**

## Slide 26

#### **CORF Token Fixation** ( **Flask-login + Flask-WTF** )

**https://bank.com https://atk.bank.com** POST /login **4** Cookie: session= {csrf= **s** , _id= **None** }#sign – user=bob&password=s3cur3&csrf_token= **t1** Bob authenticates Welcome Bob! Set-Cookie: session={csrf= **s** , _id= **bob** }#sign

5

POST /action Cookie: session= {csrf= **s** , _id= **bob** }#sign – csrf_token= **t0**

The **CSRF secret s** is not refreshed during login! The **CSRF token t0** known by the attacker is valid for Bob’s session!

**M. Squarcina, P. Adão // Cookie Crumbles: Unveiling Web Session Integrity Vulnerabilities**

**#BHUSA @BlackHatEvents**

## Slide 27

#### **CORF Token Fixation**

- Bypasses faulty implementations of the **Synchronizer Token Pattern**

- Caused by the **CSRF secret** in the session **not being renewed** upon login

- The attacker does not need to know the CSRF secret, but only an **unauthenticated session id** and a **valid CSRF token** for that session

- Works against **server-side** and **client-side** session handling implementations

- User already logged-in? No problem, **force a deauth** and toss the attacker’s pre-session, either via eviction or request to /logout endpoint

**M. Squarcina, P. Adão // Cookie Crumbles: Unveiling Web Session Integrity Vulnerabilities**

**#BHUSA @BlackHatEvents**

## Slide 28

#### **CORF Token Fixation** ( **CodeIgniter4** )

**https://bank.com**

**1**

GET /login

<input csrf_token= **t0** type="hidden"> Set-Cookie: session= **sess0**

__ci_last_regenerate|i:1690849755; csrf_test_name|s:32:" 47be9758fe558 98f1958bd201764a0be" ;

CSRF secret **s0**

**M. Squarcina, P. Adão // Cookie Crumbles: Unveiling Web Session Integrity Vulnerabilities**

**#BHUSA @BlackHatEvents**

## Slide 29

#### **CORF Token Fixation** ( **CodeIgniter4** )

**https://bank.com**

**1**

**2**

GET /login <input csrf_token= **t0** type="hidden"> Set-Cookie: session= **sess0** POST /login Cookie: session= **sess0** – user=bob&password=s3cur3&csrf_token= Welcome Bob! Set-Cookie: session= **sess1**

Cookie: session= **sess0** – user=bob&password=s3cur3&csrf_token= **t0**

__ci_last_regenerate|i:1690849755; csrf_test_name|s:32:"1f5b0c83a29e9 f9725d219e53a6d2be1";

__ci_last_regenerate|i:1690849755; csrf_test_name|s:32:" 1f5b0c83a29e9 f9725d219e53a6d2be1" ;user|a:1:{s:2 :"id";s:1:"1";} CSRF secret **s1**

**M. Squarcina, P. Adão // Cookie Crumbles: Unveiling Web Session Integrity Vulnerabilities**

**#BHUSA @BlackHatEvents**

## Slide 30

#### **CORF Token Fixation** ( **CodeIgniter4** )

**https://bank.com**

**1**

**2**

GET /login

<input csrf_token= **t0** type="hidden"> Set-Cookie: session= **sess0** POST /login

Cookie: session= **sess0** – user=bob&password=s3cur3&csrf_token= **t0**

Welcome Bob! Set-Cookie: session= **sess1**

__ci_last_regenerate|i:1690849755; csrf_test_name|s:32:" **1f5b0c83a29e9 f9725d219e53a6d2be1** " ;

CSRF secret **s1**

__ci_last_regenerate|i:1690849755; csrf_test_name|s:32:" 1f5b0c83a29e9 f9725d219e53a6d2be1" ;user|a:1:{s:2 :"id";s:1:"1";} CSRF secret **s1**

**M. Squarcina, P. Adão // Cookie Crumbles: Unveiling Web Session Integrity Vulnerabilities**

**#BHUSA @BlackHatEvents**

## Slide 31

#### **CORF Token Fixation** ( **CodeIgniter4** )

**https://bank.com https://atk.bank.com** GET /login **1** <input csrf_token= **t0** type="hidden"> Set-Cookie: session= **sess0 2** Set-Cookie: session= **sess0** ; domain=bank.com GET /login **3** Cookie: session= **sess0** <input csrf_token= **t1** type="hidden"> Set-Cookie: session= **sess0**

**M. Squarcina, P. Adão // Cookie Crumbles: Unveiling Web Session Integrity Vulnerabilities**

**#BHUSA @BlackHatEvents**

## Slide 32

CORF Token Fixation  ( CodeIgniter4 )
https://bank.com https://atk.bank.com
POST /login
4
 Cookie: session= sess0
 – user=bob&password=s3cur3&csrf_token= t1
Welcome Bob!
Set-Cookie: session= sess1
Bob authenticates. A new
CSRF secret s1  is generated
for  session sess1

**M. Squarcina, P. Adão // Cookie Crumbles: Unveiling Web Session Integrity Vulnerabilities**

**#BHUSA @BlackHatEvents**

## Slide 33

#### **CORF Token Fixation** ( **CodeIgniter4** )

**https://bank.com**

POST /login Cookie: session= **sess0** – user=bob&password=s3cur3&csrf_token= **t1** Welcome Bob! Set-Cookie: session= **sess1** Bob authenticates. A new **CSRF secret s1** is generated for **session sess1**

**4**

**https://atk.bank.com**

The CSRF token **t0** known by the attacker (associated with **s0** ) **is no longer** valid for Bob’s session **sess1** !

**M. Squarcina, P. Adão // Cookie Crumbles: Unveiling Web Session Integrity Vulnerabilities**

**#BHUSA @BlackHatEvents**

## Slide 34

#### **CORF Token Fixation** ( **CodeIgniter4** )

**https://bank.com**

**https://atk.bank.com**

POST /login Cookie: session= **sess0** – user=bob&password=s3cur3&csrf_token= **t1** Welcome Bob! Set-Cookie: session= **sess1** Bob authenticates. A new **CSRF secret s1** is generated for **session sess1**

**4**

The CSRF token **t0** known by the attacker (associated with **s0** ) **is no longer** valid for Bob’s session **sess1** !

But **sess0** was also updated with the **new CSRF secret s1**

**M. Squarcina, P. Adão // Cookie Crumbles: Unveiling Web Session Integrity Vulnerabilities**

**#BHUSA @BlackHatEvents**

## Slide 35

CORF Token Fixation  ( CodeIgniter4 )
https://bank.com https://atk.bank.com
POST /login
4
 Cookie: session= sess0
 – user=bob&password=s3cur3&csrf_token= t1
Welcome Bob!
GET /login
Set-Cookie: session= sess1
5
Cookie: session= sess0
<input csrf_token= t2  type="hidden">
Set-Cookie: session= sess0

**M. Squarcina, P. Adão // Cookie Crumbles: Unveiling Web Session Integrity Vulnerabilities**

**#BHUSA @BlackHatEvents**

## Slide 36

CORF Token Fixation  ( CodeIgniter4 )
https://bank.com https://atk.bank.com
POST /login
4
 Cookie: session= sess0
 – user=bob&password=s3cur3&csrf_token= t1
Welcome Bob!
GET /login
Set-Cookie: session= sess1
5
Cookie: session= sess0
<input csrf_token= t2  type="hidden">
Set-Cookie: session= sess0
6
POST /action
 Cookie:  session= sess1
 – csrf_token= t2

#BHUSA @BlackHatEvents

**M. Squarcina, P. Adão // Cookie Crumbles: Unveiling Web Session Integrity Vulnerabilities**

## Slide 37

#### **Web Frameworks Analysis**

**Framework Broken Default Session (9/13 vulnerable) STP DS Fixation Express** (passport + csurf) ⬤ ⬤ **CVE-2022-25896 Koa** (koa-passport + csrf) ⬤ **Fastify** (fastify/passport + ⬤ ⬤ ⬤ **CVE-2023-29020 CVE-2023-27495 CVE-2023-29019** csrf-protection) **Sails*** (csurf) ⬤ ⬤ **Flask** (flask-login+flask-wtf) ⬤ **Tornado** ⬤ **Symfony** (security-bundle) ⬤ **CVE-2022-24895 CodeIgniter4** (shield) ⬤ ⬤ **CVE-2022-35943 Yii2** ⬤ ***** affects the bootstrap template app

**M. Squarcina, P. Adão // Cookie Crumbles: Unveiling Web Session Integrity Vulnerabilities**

**#BHUSA @BlackHatEvents**

## Slide 38

## **Are           Getting Better?**

**M. Squarcina, P. Adão // Cookie Crumbles: Unveiling Web Session Integrity Vulnerabilities**

**#BHUSA @BlackHatEvents**

## Slide 39

#### **Methodology**

Methodology
Browser testing suit e  for tossing
2
& eviction: check  discrepancies
rfc6265bis
Manual  review of
1
the cookie standard Simple  differential fuzzing to
3
test server implementations

**M. Squarcina, P. Adão // Cookie Crumbles: Unveiling Web Session Integrity Vulnerabilities**

**#BHUSA @BlackHatEvents**

## Slide 40

#### **Strict Secure**

http://atk.bank.com

https://bank.com
Set-Cookie: session=good; Secure
Set-Cookie: session=bad

Browsers now **block setting a cookie without the Secure flag** if there is already a secure cookie in that site with the same name. **Prevents tossing** from network attackers. Also **eviction doesn’t work** as secure cookies are partitioned separately from non-secure cookies.

**M. Squarcina, P. Adão // Cookie Crumbles: Unveiling Web Session Integrity Vulnerabilities**

**#BHUSA @BlackHatEvents**

## Slide 41

#### **Prefixes**

**https://atk.bank.com**

**https://bank.com** Set-Cookie: __Host-session=good; Secure; Path=/ Set-Cookie: __Host-session=bad; Secure; Path=/; d omain=bank.com

**__Secure-** cookies must be set from a secure origin and include the Secure attribute.

**__Host-** cookies, additionally, must **NOT be set with the Domain** attribute and **Path=/** .

__Host- cookies are **high-integrity cookies** even against same-site attackers!

**M. Squarcina, P. Adão // Cookie Crumbles: Unveiling Web Session Integrity Vulnerabilities**

**#BHUSA @BlackHatEvents**

## Slide 42

Collisions
Werkzeug <2.2.3
Set-Cookie: Cookie: Key Value Server <key, value>
foo= foo= foo        <foo,     >
=foo foo foo
=foo= foo= foo=
==foo =foo =foo
foo foo foo

**M. Squarcina, P. Adão // Cookie Crumbles: Unveiling Web Session Integrity Vulnerabilities**

**#BHUSA @BlackHatEvents**

## Slide 43

Collisions
Werkzeug <2.2.3
Set-Cookie: Cookie: Key Value Server <key, value>
foo= foo= foo        <foo,     >
=foo foo foo        <foo,     >
=foo= foo= foo=        <foo,     >
==foo =foo =foo <foo,     >
foo foo foo        <foo,     >

**M. Squarcina, P. Adão // Cookie Crumbles: Unveiling Web Session Integrity Vulnerabilities**

**#BHUSA @BlackHatEvents**

## Slide 44

Collisions
Werkzeug <2.2.3
Set-Cookie: Cookie: Key Value Server <key, value>
foo= foo= foo        <foo,     >
=foo foo foo        <foo,     >
=foo= foo= foo=        <foo,     >
==foo =foo =foo <foo,     >
foo foo foo        <foo,     >

**M. Squarcina, P. Adão // Cookie Crumbles: Unveiling Web Session Integrity Vulnerabilities**

**#BHUSA @BlackHatEvents**

## Slide 45

**http://atk.bank.com Bypassing __Hosthttps://bank.com** Set-Cookie: __Host-session=good; Secure; Path=/

**M. Squarcina, P. Adão // Cookie Crumbles: Unveiling Web Session Integrity Vulnerabilities**

**#BHUSA @BlackHatEvents**

## Slide 46

http://atk.bank.com
Bypassing __Host-
https://bank.com
Set-Cookie: __Host-session=good;
 Secure; Path=/
Set-Cookie:  =__Host-session=bad;  Path=/app;
   domain=bank.com

**M. Squarcina, P. Adão // Cookie Crumbles: Unveiling Web Session Integrity Vulnerabilities**

**#BHUSA @BlackHatEvents**

## Slide 47

http://atk.bank.com
Bypassing __Host-
https://bank.com
Set-Cookie: __Host-session=good;
 Secure; Path=/
Set-Cookie:  =__Host-session=bad;  Path=/app;
   domain=bank.com
Cookie: __Host-session=bad;
        __Host-session=good;

**M. Squarcina, P. Adão // Cookie Crumbles: Unveiling Web Session Integrity Vulnerabilities**

**#BHUSA @BlackHatEvents**

## Slide 48

#### **Bypassing __Host-**

http://atk.bank.com

**https://bank.com**

**CVE-2022-2860* CVE-2022-40958***

Set-Cookie: __Host-session=good; Secure; Path=/

Set-Cookie: =__Host-session=bad; Path=/app; domain=bank.com Cookie: __Host-session=bad; __Host-session=good;

Fixed in browsers and rfc6265bis by blocking nameless cookies with value starting for __Host- or __Secure* Reported almost simultaneously with **Axel Chong** , our issues were merged to jointly discuss mitigations and additional security implications. See also <u>https://github.com/httpwg/http-extensions/issues/2229</u>

**M. Squarcina, P. Adão // Cookie Crumbles: Unveiling Web Session Integrity Vulnerabilities**

**#BHUSA @BlackHatEvents**

## Slide 49

#### **Bypassing __Host-** (after the **fix** )

**CVE-2022-2860* CVE-2022-40958***

- ●● **Serialization collisions** could still be used to bypass __Host- against chains of        parsers

- Fixed in **AWS Lambda proxy integration for HTTP APIs** after our report

Fixed in browsers and rfc6265bis by blocking nameless cookies with value starting for __Host- or __Secure* Reported almost simultaneously with **Axel Chong** , our issues were merged to jointly discuss mitigations and additional security implications. See also <u>https://github.com/httpwg/http-extensions/issues/2229</u>

**M. Squarcina, P. Adão // Cookie Crumbles: Unveiling Web Session Integrity Vulnerabilities**

**#BHUSA @BlackHatEvents**

## Slide 50

http://atk.bank.com
Bypassing Strict Secure
https://bank.com
Set-Cookie: session=good; Secure
Still working!
Set-Cookie: =session=bad
Set-Cookie:  =session=bad;  Path=/app;
       domain=bank.com
Cookie: session=bad; session=good;

**M. Squarcina, P. Adão // Cookie Crumbles: Unveiling Web Session Integrity Vulnerabilities**

**#BHUSA @BlackHatEvents**

## Slide 51

**Bypassing __Host-** (with the help of the **server** )

- Popular programming languages / Web frameworks **diverge from the spec**

- Client / server inconsistencies. Security implications?

**Werkzeug** <2.2.3

Cookie: __Host-sess=bad Cookie: =__Host-sess=bad Cookie: ========__Host-sess=bad

**M. Squarcina, P. Adão // Cookie Crumbles: Unveiling Web Session Integrity Vulnerabilities**

**#BHUSA @BlackHatEvents**

## Slide 52

#### **Bypassing __Host-** (with the help of the **server** )

- Popular programming languages / Web frameworks **diverge from the spec**

- ● Client / server inconsistencies. Security implications?

**Werkzeug** <2.2.3 **CVE-2023-23934**

Parsed as the Cookie: __Host-sess=bad **same cookie** Cookie: =__Host-sess=bad Cookie: ========_ _Host-sess=bad

**Leading ‘=’ are stripped out** while parsing the cookie string! Bypass with, e.g., Set-Cookie: ==__Host-sess=bad

**M. Squarcina, P. Adão // Cookie Crumbles: Unveiling Web Session Integrity Vulnerabilities**

**#BHUSA @BlackHatEvents**

## Slide 53

**Bypassing __Host-** (with the help of the **server** )

- Popular programming languages / Web frameworks **diverge from the spec**

- Client / server inconsistencies. Security implications?

**PHP** <8.1.11 Parsed as the Cookie: __Host-sess=bad **same cookie** Cookie: _ Host-sess=bad Cookie: ..Host-sess=bad

**M. Squarcina, P. Adão // Cookie Crumbles: Unveiling Web Session Integrity Vulnerabilities**

**#BHUSA @BlackHatEvents**

## Slide 54

#### **Bypassing __Host-** (with the help of the **server** )

- Popular programming languages / Web frameworks **diverge from the spec**

- ● Client / server inconsistencies. Security implications?

**PHP** <8.1.11

**CVE-2022-31629**

**register_globals** heritage: ‘ ’ . [ are replaced by _ in the $_COOKIE superglobal array

Cookie: __Host-sess=bad Cookie: _ Host-sess=bad Cookie: ..Host-sess=bad

Parsed as the **same cookie**

Did you know? Cookie: a[b]=c Parsed as {"a":{"b":"c"}}

**M. Squarcina, P. Adão // Cookie Crumbles: Unveiling Web Session Integrity Vulnerabilities**

**#BHUSA @BlackHatEvents**

## Slide 55

#### **Desynchronization Issues**

**CVE-2023-29547**

**1** https://bank.com set a secure Set-Cookie: sess=good; Secure **2** http://bank.com sets a non-secure        vja JS document.cookie = ‘sess=bad’

**<u>Fixed in Firefox 112</u>** Caused by restrictions imposed by the FF implementation of **Site Isolation** ( **Project Fission** )

**EXPECTATION**

**REALITY**

sess=bad is **<u>not set</u>** (Strict Secure        ) Cookie not set, but document.cookie at http://bank.com returns sess=bad

**M. Squarcina, P. Adão // Cookie Crumbles: Unveiling Web Session Integrity Vulnerabilities**

**#BHUSA @BlackHatEvents**

## Slide 56

#### **Desynchronization Issues**

**1** https://atk.bank.com

###### **<u>Fixed in Firefox 115</u>**

Could introduce vulnerabilities in frontends trusting **document.cookie** to set **custom HTTP headers** like **ASP.NET** and **Angular**

**2**

**3**

**Delete** via Set-Cookie (exp. date), Clear-Site-Data header, or manually The first 240         are still in Document.cookie in the original and opened window (survives reloads and schemeful navigations)

**M. Squarcina, P. Adão // Cookie Crumbles: Unveiling Web Session Integrity Vulnerabilities**

**#BHUSA @BlackHatEvents**

## Slide 57

#### **Takeaways**

- Many battle-tested Web frameworks and libraries had **concerning session integrity vulnerabilities** . Causes & consequences?

- ● **Legacy design** is still cursing modern applications: can we **move on without breaking the Web** ?

- ● Developers are falling behind in **keeping track of Web standards**

- Composition issues or lack of understanding of the threat models? Apps in the wild?

- Backward compatibility issues? Is it possible to make deployment easier without trading on security?

- Lack of cohesiveness between browser vendors, developers, and authors of Web standards? Web platform changing too fast?

**M. Squarcina, P. Adão // Cookie Crumbles: Unveiling Web Session Integrity Vulnerabilities**

**#BHUSA @BlackHatEvents**

## Slide 58

### **… and that's the way the cookie crumbles!**

**M. Squarcina, P. Adão // Cookie Crumbles: Unveiling Web Session Integrity Vulnerabilities**

**#BHUSA @BlackHatEvents**

## Slide 59

icons by **flaticon**

# **Thank You! Questions?**

**Marco Squarcina** (TU Wien) @blueminimal https://infosec.exchange/@minimalblue marco.squarcina@tuwien.ac.at

**Pedro Adão** (IST, Universidade de Lisboa) @pedromigueladao https://infosec.exchange/@pedroadao pedro.adao@tecnico.ulisboa.pt

Paper available at <u>https://github.com/SecPriv/cookiecrumbles</u>

**M. Squarcina, P. Adão // Cookie Crumbles: Unveiling Web Session Integrity Vulnerabilities**

**#BHUSA @BlackHatEvents**
