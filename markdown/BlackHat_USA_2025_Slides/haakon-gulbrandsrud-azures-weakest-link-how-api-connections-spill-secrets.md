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
text_chars: 27814
ocr_pages: 77
has_ocr: true
redacted_secrets: 0
ocr_confidence: 85.3
ocr_unreliable_blocks: 0
vision_verified_blocks: 1
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T05:13:56Z"
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


> Recovered by OCR — confidence 91/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
‘black hat
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


> Recovered by OCR — confidence 83/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Logic App Designer
Discard (@) Parameters {} Code view Info
2. When a HTTP request
is received
Read a resource
@
t
+ +
@) List keys 3 | Get past time
@A
+
lapse all actions
kpand or collapse all action A ‘ F
o single ck. Create a new issue call some api
Failed to retrieve dyna
```

## Slide 6

###### Logic App Designer

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 84/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Logic App Designer
Discard (@) Parameters {} Code view Info
2. When a HTTP request
is received
Read a resource
+ +
@ List keys | | 8 | Get past time
+
lapse all actions
kpand or collapse all action A ‘ F
o single ck. Create a new issue call some api
Failed to retrieve dyna
```

## Slide 7

###### What do they mean?

#BHUSA   @BlackHatEvents

## Slide 8

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 82/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
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


> Recovered by OCR — confidence 89/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Refresh iO Delete a Feedback
2 Overview “ Essentials
orname : slack
f@ Activity log
yname —: Slack
te time : 6/2/2025 8:17:44 AM
@ Tags
4% Diagnose and solve problems
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


> Recovered by OCR — confidence 80/100 on the text kept, 54/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
iv
"testLinks”:
app-tests/providers/Microsoft.Web,
RuntimeUrl": “https:
```

## Slide 11

#BHUSA   @BlackHatEvents

## Slide 12

##### Azure Resource Management

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 72/100 on the text kept, 62/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
BRIEFINGS ‘4
~ = pt = e52f-d4 —-4347- —-6589250 465e/resourceGroups/ logic =
Azure Resource
Management
```

## Slide 13

##### Subscription

#BHUSA   @BlackHatEvents

## Slide 14

##### Resource Group

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 78/100 on the text kept, 54/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
BRIEFINGS WY
app-tests/providers icrosoft.We cronnections/ siac extens: 3/Proxy
conversations.list HTTP/2
Resource Group
```

## Slide 15

##### API Type

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 75/100 on the text kept, 53/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
BRIEFINGS 4
= —tests x iders icrosofit.We = ections C extensions x
ersations.list HTTP/2
```

## Slide 16

Resource

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 80/100 on the text kept, 43/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
BRIEFINGS YW
app-tests/providers icrosoft.We cronnections/ siac extensions/proxy
conversations.list HTTP/2
Resource
```

## Slide 17

##### Action/Endpoint

#BHUSA   @BlackHatEvents

## Slide 18

#BHUSA   @BlackHatEvents

## Slide 19

#BHUSA   @BlackHatEvents

## Slide 20

#BHUSA   @BlackHatEvents

## Slide 21

#BHUSA   @BlackHatEvents

## Slide 22

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 83/100 on the text kept, 69/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
TP/2 403 Forbidden
©
Ca
Content-Type: application/json
Host: mw {
"code": "AuthorizationFailed",
"
essage":"The client
action ‘Microsoft.Web/1
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


> Recovered by OCR — confidence 83/100 on the text kept, 69/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
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
Power Automate eeroien lanagemen network
connector ID :
operation ID on-peekies RESTful
connection ID PM data gateway API defined 1
in swagger i
Power Apps A |
and policies ; .
Logic Apps
https://learn.microsoft.com/en-us/connectors/connector-architecture
```

## Slide 25

###### API Connection Architecture

https://learn.microsoft.com/en-us/connectors/connector-architecture

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 92/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
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


> Recovered by OCR — confidence 92/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
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


> Recovered by OCR — confidence 89/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
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


> Recovered by OCR — confidence 89/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
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


> Recovered by OCR — confidence 90/100 on the text kept, 63/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Action Definitions
‘Slack
Ww
“description”: a team communication tool, that brings together all
e
your team communications in one place, instantly searchable and available wherev
“X-mS-api-annotation": {
```

## Slide 30

#### Action Definitions

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 71/100 on the text kept, 53/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Action Definitions
Swag} 4
' 3
=] > "/{connectionId}/channels.create": {
: > "/{connectionId}/conversations.create": {
of your t srever
> “/{connectionId}/groups.create":
J
‘/{connectionId}/v2/chat.postMessage":
```

## Slide 31

https://learn.microsoft.com/en-us/connectors/connector-architecture #BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 95/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
connector swagger
and policies
https://learn.microsoft.com/en-us/connectors/connector-architecture
```

## Slide 32

https://learn.microsoft.com/en-us/connectors/connector-architecture #BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 95/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
connector swagger
and policies
https://learn.microsoft.com/en-us/connectors/connector-architecture
```

## Slide 33

https://learn.microsoft.com/en-us/connectors/connector-architecture #BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 95/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
connector swagger
and policies
https://learn.microsoft.com/en-us/connectors/connector-architecture
```

## Slide 34

https://learn.microsoft.com/en-us/connectors/connector-architecture #BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 91/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Direct call without additional transformations RESTful API
defined in
swagger
Call proxied for additional
Credential and metadata store
request/response transformations
user token connection
onnection ID token
on-premise
i network
on-premises
connector swagger
and policies
connector webapp ;
```

## Slide 35

https://learn.microsoft.com/en-us/connectors/connector-architecture #BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 87/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
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
Management
connector swagger
and policies
```

## Slide 36

##### Global APIM Host

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 85/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Request
Pretty Raw Hex JSON Web Token
GET /apim/slack/9b973 e753 af049caS4e6e01f1£184c44/conversations.list HTTP/2
Host: logic-apim-—-norwayeast-OOl.azure-api.net
Global APIM Host
```

## Slide 37

##### Connector Type

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 87/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Request
Pretty Raw Hex JSON Web Token
GET /apim/slack/9b973 e753 af049caS4e6e01f1F184c44/conversations.list HTTP/2
Host: logic im—-norwayeast-OOl.azure-api.net
Connector Type
```

## Slide 38

##### Connection ID

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 95/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Request
Pretty Raw Hex JSON Web Token
Connection ID
```

## Slide 39

##### Action endpoint

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 86/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Request
Pretty Raw Hex JSON Web Token
GET /apim/slack/9b973e753 af049caS4e6e01f1F184c44/conversations.list HTTP/2
Host: logic-apim-—-norwayeast-OOl.azure-api.net
Action endpoint
```

## Slide 40

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 85/100 on the text kept, 63/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Response
Pretty Raw Hex =e \n =
1 HTTP/2 403 Forbidden
4 X-Ms-Failure-Cause: apihub-token-exchange
5S X-Ms-Apihub-Obo: false
6 X-Ms-Apihub-Cached-Response: false
7| Date: Wed, 21 May 2025 13:22:14 GMT
{
"status”:403,
"source”
"message":
"Error from token exchange: naan as denied due to missing connection ACL: User = 32
3af049c a94e6e01f1f1 4c44"
```

## Slide 41

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 96/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
This Token Store is live and running build 1.74.18-
release.0+d449227
See Getting stared with Azure Token Store for a quick start
```

## Slide 42

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 86/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
custom-try-parametrized-2 | Access policies *
API Connectior
Add C) Refresh
25 Overview
li Activity log Application
Bp Access control (IAM)
Name Policy Name Action
@ Tags
Api Connection User ApiConnectionUser-8fffba85-5e62-4c4a-9bf7-... Delete
4% Diagnose and solve problems
«,» Resource visualizer
Access policies
```

## Slide 43

But they were, all of them, deceived, for another Connection ACL was made.

#BHUSA   @BlackHatEvents

## Slide 44

###### API Connection Architecture

https://learn.microsoft.com/en-us/connectors/connector-architecture

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 91/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
API Connection Architecture
Azure portal Azure PowerShell Azure CLI REST clients Credential and metadata store
SDKs
} user token
>O4 connection ID
(*) Azure Resource Manager
Data Web App Virtual Service Other
Store Machine Management services
+— Authentication
connector ID <
operation ID
connection ID
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


> Recovered by OCR — confidence 91/100 on the text kept, 38/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Authorization: Bearer <Token>
2021-01-
```

## Slide 48

#### Readers GET

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 83/100 on the text kept, 65/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
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


> Recovered by OCR — confidence 92/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
/subscriptions/8e3ce5
Host: management.azure.com
Authorization: Bearer <Token>
```

## Slide 50

#### Not anything else

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 74/100 on the text kept, 55/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
BRIEFINGS | |
/suDsct Content-Length: 411
65892507465e Content-Type: application/json; charset-utf-8 ALE hs
Host: manage
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


> Recovered by OCR — confidence 92/100 on the text kept, 69/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Azure portal Azure PowerShell Azure CLI REST clients
SDKs
(i>) Azure Resource Manager «—» Authentication
Data Web App Virtual Service Other
Store Machine Management services
```

## Slide 55

###### Role Check

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 89/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Azure portal Azure PowerShell Azure CLI REST clients
SDKs
(>) Azure Resource Manager Authentication
| | | | Role Check
Data Web App Virtual Service Other
Store Machine Management Services
```

## Slide 56

Role Check:

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 90/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Azure portal Azure PowerShell Azure CLI REST clients
SDKs
(>) Azure Resource Manager Authentication
| | | | Role Check: 6
Data Web App Virtual Service Other
Store Machine Management Services
```

## Slide 57

Full Control

Role Check:

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 89/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Azure portal Azure PowerShell Azure CLI REST clients
SDKs
(~) Azure Resource Manager <-> Authentication
Full Control Role Check: 6
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


> Recovered by OCR — confidence 84/100 on the text kept, 51/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
/subscriptions/292c3ce5-4288-4413-8dad-5c665019739d/resourceGroups/binsec-privesc
/binsec-prives
2
test group/providers/Microsoft.Web/sites,
api-version=2014-11-01 HTTP/2
Authorization: Bearer <TOKEN>
https://binarysecurity.no/posts/2023/06/function-apps-rce
```

## Slide 60

#### OOPS

https://binarysecurity.no/posts/2023/06/function-apps-rce

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 75/100 on the text kept, 43/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
BRIEFINGS j
200 OK
Content-Length: 592 rivesc
test Content-Type: application/json ken?
U
ct
W
~~
©
“location” : “Norway
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


> Recovered by OCR — confidence 87/100 on the text kept, 56/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Azure SQL Database
Request
Raw Hex \n
1| GET
/subscriptions/ 8e3ce52 £-d45b-43 47-8705-65892507465e/resourceGro
api-version=2018-07-Ol-preview HTTP/2
2 Host: management.azure.com
3 Metadata: true
4 Authorization: Bearer
```

## Slide 64

###### Azure SQL Database

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 87/100 on the text kept, 56/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
O7 Jan 2025 11:18:19 GMT
Azure SQL Database
Request
Raw Hex
GET
nsions/ proxy/datasets/defé
Host: management.azure.cor
Metadata: true
Authorization: Bearer
"@odata.context":
"value": [
{
"@odata.etag":"",
"ItemInternalld":
"cd4799eb-dd7 1-4b06-a571-19e249d3 606d",
t.azure-ap
```

## Slide 65

###### Azure SQL Database

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 86/100 on the text kept, 61/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
1
5 Date: Tue, O7 Jan 2025 11:18:19 GMT
Azure SQL Database *
"@odata.context":
2b554d201/ §metadata#
Request
Pretty Raw Hex ® in =
GET Sdeb3t",
/subscriptions, 29/resourceGroups/
‘providers/Microsoft.Web/connections/sql/extensions/proxy/V2/datasets/wssw
Host: westeurope.management.azure.com
Authorization: Bearer
```

## Slide 66

###### Azure SQL Database

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 81/100 on the text kept, 70/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
BRIEFINGS 26 07 Jan 2025 11:18:19 GMT
Azu re SQL Data base 29 "@odata.context":
"https://dB4b73bél2cf596é0. 16.common. logic-norwayeast.azure-ap
Requ Response
Pretty . Pretty Raw Hex Re ey in = =
c 1 HTTP/1.1 502 Unexpected Exception : System.InvalidOperationException: Unable to A se
1 GE parse dataset. at aaa
/s\ Microsoft.Azure.Connectors.Mashup.Sql.Models.SqlConnectionParameters.UpdateUsingDa
taset(HttpRequestMessage request, String dataset) in iw
C:\__w\1\s\src\Connectors\FirstParty\sql\Connector\Models\SqlConnectionParameters. io
2 Ho: uestMessage request, String dataset) in
= | 2 Cache-Control: no-store, no-cache
ey. 3 Pragma: no-cache ly
4 Content-Length: 1658 B9décB",
5 Content-Type: application/json
6 Expires: -1
7 Strict-Transport-Security: max—age=31536000; includeSubDomains
8 x-ms-datasourceerror: True
9 x-ms-request—id: 36ac 3e249d3606a",
```

## Slide 67

###### Jira

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 78/100 on the text kept, 53/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Jira
Request
api-version=2018-07-Ol-preview HTTP/2 \rx \n
2 Host: management.azure.com\z \n
3 Metadata: true \r \n
4 Ahuthorization: Bearer
instance \r \n
```

## Slide 68

###### Jira

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 90/100 on the text kept, 57/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Jira
26 Date: Fri, O3 Jan 2025 10:25:31 GHT
31 "message":
"Unable to parse result body. JSON response expected. Body:
32 "source":
```

## Slide 69

###### Jira

#BHUSA   @BlackHatEvents


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 80/100 on the text kept, 70/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
black hat BRIEFINGS

Jira

Description | Request to Collaborator | Response from Collaborator

Pretty   Raw   Hex

 7  X-Azure-RequestChain: hops=1
 8  x-ms-operation-context:
    (;appId=797f4846-ba00-4fd7-ba43-dac1f8f63013,tenantId=72f13b38-6d4b-417c-be51-4e46f66a37a8,objectId=9bc682d6-391e-475e-855c-c68d6cff9461/germanywestcentral/8a62d178-6449-45b2-a17a-c0ede718d0b3)
 9  x-ms-client-request-id: 9cf2aecf-7a3b-474c-a327-0d25a0ef3990
10  x-ms-arm-request-tracking-id: 0711fedb-50f8-4331-a96d-7ceadb656eb2
11  x-ms-correlation-request-id: 0711fedb-50f8-4331-a96d-7ceadb656eb2
12  x-ms-routing-request-id: GERMANYWESTCENTRAL:20250103T102531Z:0711fedb-50f8-4331-a96d-7ceadb656eb2
13  x-ms-client-location: germanywestcentral
14  x-ms-home-tenant-id: 72f13b38-6d4b-417c-be51-4e46f66a37a8
15  x-ms-arm-service-request-id: 5a852172-195c-4974-a390-588889a444cf
16  x-ms-client-audience: https://management.core.windows.net/
17  x-ms-client-scope:
18  x-ms-client-acr:
19  Content-Type: application/json
20  x-ms-client-app-id-acr: 1
21  Authorization: Basic
    aGFha29uQGJpbnNlYy5jbG9[redacted]
    NabVo1S1NCaX1HbGVNYOF1N[redacted]
22  x-ms-client-issuer: https://sts.windows.net/72f13b38-6d4b-417c-be51-4e46f66a37a8/
23  X-MS-APIM-Callback: https://logic-norwayeast-001.consent.azure-apihub.net
24  x-ms-client-puid:
25  x-ms-client-alt-sec-id:
26  x-ms-client-principal-id:
27  x-ms-client-authorization-source: RoleBased
28  x-ms-client-identity-provider: https://sts.windows.net/72f13b38-6d4b-417c-be51-4e46f66a37a8/
29  x-ms-client-principal-group-membership-source: None
30  x-ms-client-principal-name:
31  x-ms-client-family-name-encoded:
32  x-ms-client-given-name-encoded:
33  x-ms-arm-network-source: PublicNetwork
34  x-ms-activity-vector: IN.01.IN.09
35  X-ARR-LOG-ID: 9cf2aecf-7a3b-474c-a327-0d25a0ef3990
36  CLIENT-IP: 51.116.150.71:13378

[search box] x-for                                                    5 matches
```

## Slide 70

###### Keyvaults

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 78/100 on the text kept, 68/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Keyvaults
Request
Pretty Raw Hex ® in
/subscriptions/ 8e3ce52 f-d45b-43 47-8705-65892507465e/resourceGroups
2018-07-Ol-previewéprojectkey=TP HTTP/2
2 Host: management.azure.com
```

## Slide 71

###### Keyvaults

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 88/100 on the text kept, 62/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Keyvaults
28 Date: Tue, O7 Jan 2025 14:42:46 GMT
"value": "MySecretValue"
"isEnabled":true,
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


> Recovered by OCR — confidence 92/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
What did they fix?
Request
Pretty Raw Hex JSON Web Token ® » =
GET
HTTP/2
Host: management.azure.com
4 Authorization: Bearer
```

## Slide 75

###### What did they fix?

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 89/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
What did they fix?
"message":
"The API Connection proxy requests are not supported. Only Test Connections
llowed through proxy requests
```

## Slide 76

###### What did they fix?

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 91/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
What did they fix?
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


> Recovered by OCR — confidence 91/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
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
Activityinfo
Acumatica
Download PDF
By: Férdés Andras
ndent Publisher
By: Ford6s Andras
By: Acumatica
By: Adobe Inc
yendent Publisher
By: Troy Taylor, Hitachi
Solutions
By: Africa's Talking
—
By: ahead AG
By: Fordés Andrés
By: Ahmad Najjar, Troy Taylor
By: Richard Wilson
By: Troy Taylor
rip (Independe
By: Taiki Yoshida
1
By: ahead AG
By: Swiftpage ACT!
Adobe Acr
By: Adobe Inc.
By: Adobe Inc.
By: Africa's Talking
By: AgilePoint Inc
Not (Indeper
By: Fordés Andrés
Ref: https://learn.microsoft.com/en-us/connectors/connector-reference/
By: System Administrator
By: Activityinfo
By: Adobe Inc.
By: State Solutions
Africa’s Talking
By: Africa's Talking
By: Agilit-e
By: Larc Al (PTY) Ltd
```

## Slide 78

###### Sensitive Testconnections (?)

<u>https://www.pagerduty.com</u>

#BHUSA   @BlackHatEvents

## Slide 79

###### Sensitive Testconnections (?)

https://mail.google.com

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 90/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
blackhat
Sensitive Testconnections (7?)
Al Foundations
https://mail.google.com
```

## Slide 80

###### Sensitive Testconnections (?)

https://calendar.google.com

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 90/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
blackhat
Sensitive Testconnections (7?)
31
Al Foundations
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

## Slide 84

###### Dynamic Invoke

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 74/100 on the text kept, 44/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
“body”: {
“request”: {
>
65892507465e/resourceGroups/Logic-app-
```

## Slide 85

###### Dynamic Invoke

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 75/100 on the text kept, 51/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Dynamic Invoke
{
“body”: {
“request”: {
“method™ :
6589 /A65e/resourceGroup
```

## Slide 86

###### Dynamic Invoke

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 74/100 on the text kept, 44/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
“body”: {
“request”: {
>
65892507465e/resourceGroups/Logic-app-
```

## Slide 87

###### Dynamic Invoke

#BHUSA   @BlackHatEvents

## Slide 88

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 93/100 on the text kept, 45/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Host: management.azure.com
Authorization: Bearer <Token>
3
```

## Slide 89

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 80/100 on the text kept, 67/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
blackhat HTTP/2 200 OK 9
BRIEFINGS Content-Type: application/json
i
connec CE 10 on / prov ;
Host: management.azure.c EINE
Authorization: Bearer <T "name": "social",
"is channel": true,
"is group": false,
"is im": false,
“request” :{ "is mpim": false,
"method": "set ae "is private”: false,
= Erle "created": 1738674777,
path . / Convers "is archived": false
i rchived": false,
S is general”: false,
=
} "unlinked": 0,
"name normalized": "social"
"is shared": false,
"is org shared": false,
_ shared": false,
context team id": "TOS8BPBEC890",
```

## Slide 90

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 79/100 on the text kept, 53/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Host: management.azure.com
“request”: {
1
J
b44-dc
```

## Slide 91

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 79/100 on the text kept, 57/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
(TP/2 200 OK
Content-Length: 1315
Content-Type: application/json; charset=utf-8
.on=2018-
/sut
connecti
Host: ma "response": {
“statusCode": “OK",
{ {
“name": “SuperSecret",
“isEnabled": true,
} “validityStartTime": null,
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


> Recovered by OCR — confidence 81/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
—
| all endpoint “/path”, Method:
“POST”, Body: “<Data>”
(*) Azure Resource Manager <> Authentication
Role Check: 96
```

## Slide 96

Path and method valid?

Call endpoint “/path”, Method: “POST”, Body: “<Data>”

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 84/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
—
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


> Recovered by OCR — confidence 83/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
—
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


> Recovered by OCR — confidence 82/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
—
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


> Recovered by OCR — confidence 85/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
—
| all endpoint “/path”, Method:
“POST”, Body: “<Data>”
Path and
method <» (>) Azure Resource Manager = <> Authentication
valid?
Path.Join(Host, ConnectionId, InputEndpoint)
and policies
+
|
```

## Slide 100

Path and method valid?

Call endpoint “/path”, Method: “POST”, Body: “<Data>”

Uh oh!

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 83/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
—
| all endpoint “/path”, Method:
“POST”, Body: “<Data>”
Path and
method <> (i) Azure Resource Manager «—> Authentication
valid?
Path.Join(Host, ConnectionId, InputEndpoint)
=
connector swagger
```

## Slide 101

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 83/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
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


> Recovered by OCR — confidence 90/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
myconnector
my nice connector that does a lost of things that we we
1.0
default
thing that comes ba
boolean
call some api
/admin/vfs/c
/path/ {pati
default
path thing
do andnand
MyCustomizer
Mnector that does a lost of things that)
/hei/a call some api
/path/{paths} path thing
/hei do something on localhost
/heisann check this out
> |
```

## Slide 103

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 92/100 on the text kept, 69/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
BRIEFINGS . 4 4
patns:
/path/{path}:
get:
parameters:
- name: path
in: path
required: true
type: string
responses:
description: OK
```

## Slide 104

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 74/100 on the text kept, 52/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
>
BRIEFINGS a 4 ,
IST /subscriptions/
O1- prev 1ew HTIP/2
Bearer <Token>
Authorization:
=
```

## Slide 105

#BHUSA   @BlackHatEvents

Path Traversal


> Recovered by OCR — confidence 77/100 on the text kept, 54/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
>
BRIEFINGS a 4 ,
IST /subscriptions/
O1- prev 1ew HTIP/2
Bearer <Token>
Authorization:
=
Path Traversal
```

## Slide 106

New Path

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 89/100 on the text kept, 42/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
en-
Authorization:
Bearer <Token>
f
path”:
1
J
<ConnectionID>/
```

## Slide 107

#BHUSA   @BlackHatEvents

## Slide 108

##### Runtime URL

#BHUSA   @BlackHatEvents

## Slide 109

##### Traversal

#BHUSA   @BlackHatEvents

## Slide 110

##### Victim’s API Connection

#BHUSA   @BlackHatEvents

## Slide 111

##### Victim’s secret

#BHUSA   @BlackHatEvents

## Slide 112

###### Demo

#BHUSA   @BlackHatEvents

## Slide 113

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 82/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

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
P Search | < w Delete > Move c ) Refresh Open in mobile
Overview “ Essentials
y Resource g : ap nnection Vault URI : https://victomkeyvault.vault.azure.net/
f@ Activity log picconnection
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
Manage keys and secrets used by apps and services
Secrets
Our recommendation is to use a vault per application per environment (Development, Pre-Production
& Certificates and Production). This helps you to not share secrets across environments and also reduces the threat in
case of a breach.
> Settings
> Monitoring
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

## Slide 119

https://learn.microsoft.com/en-us/co nnectors/connector-architecture

###### What did they fix?

#BHUSA   @BlackHatEvents

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


> Recovered by OCR — confidence 95/100 on the text kept, 72/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
AUGUST 6-7, 2025
MANDALAY BAY / LAS VEGAS
Any Questions?
#BHUSA @BlackHatEvents
```
