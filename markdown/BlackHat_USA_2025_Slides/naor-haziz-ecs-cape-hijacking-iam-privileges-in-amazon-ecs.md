---
title: "ECS-cape – Hijacking IAM Privileges in Amazon ECS"
speakers: ["Naor Haziz"]
conference: "Black Hat"
conference_full: "Black Hat USA 2025"
edition: "USA"
year: 2025
source_pdf: "BlackHat_USA_2025_Slides/Naor Haziz_ECS-cape – Hijacking IAM Privileges in Amazon ECS.pdf"
pages: 129
sha256: "960f4eb5affd0244ffe12904be015be5f9d3aed254fddf3748d6ab28ebeffd06"
text_chars: 38387
ocr_pages: 42
has_ocr: true
redacted_secrets: 3
companion_files: ["Naor Haziz_ECS-cape – Hijacking IAM Privileges in Amazon ECS_tools.txt"]
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T22:59:07Z"
---
# ECS-cape – Hijacking IAM Privileges in Amazon ECS

**Speakers:** Naor Haziz  
**Conference:** Black Hat USA 2025  
**Source:** `BlackHat_USA_2025_Slides/Naor Haziz_ECS-cape – Hijacking IAM Privileges in Amazon ECS.pdf` (129 pages)


## Slide 1

**Expanding Privileges in the Cloud:**

ECScape

**Exploring Security Boundaries in Amazon ECS**

**#BHUSA @BlackHatEvents**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pigeachat
BRIEFINGS
AUGUST 6-7, 2025
MANDALAY BAY / LAS VEGAS
Expanding
Privileges in
the Cloud:
Exploring Security Boundaries
ECSca pe in Amazon ECS
#BHUSA @BlackHatEvents
```

## Slide 2

###### $whoami

###### **Naor Haziz**

- **Israel**

- **Software Developer**

- **Security Researcher**

- **Sweet Security**

**#BHUSA @BlackHatEvents**

## Slide 3

**#BHUSA @BlackHatEvents**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
—
%
=
'
fy
\
\ #BHUSA @BlackHatEvents
```

## Slide 4

###### Agenda

Technical
01
Background

04 Impact

02 Story Time
05 Demo

03 ECScape
06 Mitigation

**#BHUSA @BlackHatEvents**

## Slide 5

# 33%

Of Developers Using Orchestration Technologies rely on Amazon ECS

CNCF Annual Survey 2021

**#BHUSA @BlackHatEvents**

## Slide 6

#### 01 Technical Background

**#BHUSA @BlackHatEvents**

## Slide 7

###### What is IAM?

Role

Policy

**#BHUSA @BlackHatEvents**

## Slide 8

AmazonS3FullAccess AmazonEC2FullAccess CloudWatchFullAccess

**#BHUSA @BlackHatEvents**

## Slide 9

Assume
Role

**#BHUSA @BlackHatEvents**

## Slide 10

###### What Is Amazon ECS?

**ECS**

**≈**

**K8S**

**#BHUSA @BlackHatEvents**

## Slide 11

###### ECS Cluster

EC2 EC2 EC2

**#BHUSA @BlackHatEvents**

## Slide 12

EC2

###### Instance Role

**#BHUSA @BlackHatEvents**

## Slide 13

EC2

Instance Role

AmazonEC2ContainerServiceforEC2Role

**#BHUSA @BlackHatEvents**

## Slide 14

###### EC2

**#BHUSA @BlackHatEvents**

## Slide 15

EC2

Service

Task

**#BHUSA @BlackHatEvents**

## Slide 16

###### Service

**#BHUSA @BlackHatEvents**

## Slide 17

###### Service

Task

**#BHUSA @BlackHatEvents**

## Slide 18

###### Service

Task

Task Task

**#BHUSA @BlackHatEvents**

## Slide 19

###### Task

**#BHUSA @BlackHatEvents**

## Slide 20

###### Task

Container

Container Container

**#BHUSA @BlackHatEvents**

## Slide 21

Task
Task
Container
Execution
Role
Task Role

**#BHUSA @BlackHatEvents**

## Slide 22

Task Execution Role

Task

**#BHUSA @BlackHatEvents**

## Slide 23

Task

**#BHUSA @BlackHatEvents**

## Slide 24

Task
Container
Task Role

**#BHUSA @BlackHatEvents**

## Slide 25

EC2

Task Task Task
Role 1 Role 2 Role 3

**#BHUSA @BlackHatEvents**

## Slide 26

###### ECS Launch Modes

Fargate

EC2

**#BHUSA @BlackHatEvents**

## Slide 27

###### ECS Launch Modes

EC2

**#BHUSA @BlackHatEvents**

## Slide 28

EC2

ECS Agent

Instance Role

**#BHUSA @BlackHatEvents**

## Slide 29

EC2

ECS Agent

Instance Role

**#BHUSA @BlackHatEvents**

## Slide 30

EC2

ECS Agent

**#BHUSA @BlackHatEvents**

## Slide 31

EC2
ECS Agent

###### Container Instance

**#BHUSA @BlackHatEvents**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
EC2
Container instances (1) into
Q. Filter container instances by property or value
ECS Agent
Container instance v Status ¥
9049855055 14485eba4d18f00bdc28... @ Active
Container Instance
#BHUSA @BlackHatEvents
```

## Slide 32

## 02 Story Time

**#BHUSA @BlackHatEvents**

## Slide 33

Can you
monitor ECS  Sure, let’s try
tasks?

**#BHUSA @BlackHatEvents**

## Slide 34

EC2

ECS Agent

**#BHUSA @BlackHatEvents**

## Slide 35

EC2

**#BHUSA @BlackHatEvents**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
"Labels": {
"COm.amazonaws.ecs.cluster': ‘ecscape",
"com. amazonaws.ecs.container-name": "high-priv",
"com.amazonaws.ecs.task-arn": “arn:aws:ecs:us-east-2:74614708:
"com. amazonaws.ecs.task-definition-family": "high-priv-task",
"com.amazonaws.ecs.task-definition-version": "4",
“org.opencontainers.image.ref.name": "ubuntu",
"org.opencontainers.image.version": "24.04"
#BHUSA @BlackHatEvents
```

## Slide 36

## Except… The Service Name

#BHUSA @BlackHatEvents

## Slide 37

###### Amazon ECS task metadata endpoint

**#BHUSA @BlackHatEvents**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Amazon ECS task metadata endpoint
Amazon ECS task metadata endpoint version 4
The Amazon ECS container agent injects an environment variable into each container, referred to as the task metadata endpoint which provides
various task metadata and Docker stats to the container.
#BHUSA @BlackHatEvents
```

## Slide 38

**#BHUSA @BlackHatEvents**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
oot @ip-172-31-10-150:/# curl ${ECS_CONTAINER_METADATA_URI_v4}/task | j3q@
% Total % Received % Xferd Average Speed Time Time Time Current
Dload Upload Total Spent Left Speed
100 1441 100 1441 a o 776k O s-feefe- sere te= seteei-=- 1407k
{
“Cluster”: "ecscape",
“TaskARN": "arn: aws:ecs:us-east=-2:746147082083:task/ecscape/&S3d3cc0592fd49dd959b0330dbbO03ea06",
"Family": "“high-priv-task",
“Revision”: "4",
“DesiredStatus": "RUNNING",
“KnownStatus”: "RUNNING",
“PullStartedaAt": $"2025-07-25T18:06:52.985263658z2",
“PullsStoppedaAt": "2025-07-25T18:06:54.859629521z2",
“AvailabilityZome": "us-east-2a",
“LaunchType":s "EC2",
"Containers": [
{
"“DeckerId": "419c2fc436b47654f8b183b269647d005a7 T2asSch3elaTOs?cbhesatcbhas3 9786",
“Name's "high-priw",
“DockerName":s "ecs-high-priv-task-4-high-priv-fseea2%ebb3c34bsd601",
"Image": "“ubuntu:latest",
“ImagelID": "sha256:65ae7ab£3544bd2d2b6d19b13bticé4752d776bc32cSlofLs74lssbfd4o4dz205a3",_,
"Labels": {
“COM. aAMEZOnaAWS.@cs.cluster"”: "ecscape",
“COM. AMAZOnAaAWS.@cs.container-name": “high-priv",
“COM. aMAZTOnaAWS.@cs.task-arn": "arn:aws:ecs:us-east-2:746147082083:task/ecscape/83d3cc0592£d49dd959b0330dbb03e06"
"com.amazonaws.e@ecs.task-definition-family": "high-priv-task",
‘cOm.amazonaws .ecs.task-definition-version": "4"
}e
"DesiredsStatus": "RUNNING",
“KnownStatus"”: "RUNNING",
"Limits": {
"cpu": 256,
"Memory": 512
}e
“CreatedaAt": "2025-07-25T18:06:54.873113372",
"“StartedaAt": "2025-07-25T18:06:55.3171733532",
“Type”: "HORMAL",
“ContainerARN": "Arn:awsS:ecs:us-east—2:746147082083:container/ecscape/$3d3cc0592£d49dd959b03 30dbbO03ea6 / 48 adS8bf2-210d6-43a0-b431-lcbeSS8£73234",
“Networks”: [
t
“MetworkMode": "host",
“IPv4Addresses": [
“WRCID": "vpec-Oc0e2d3975e553d82",
“ServiceName": "high-priv-service",
“FaultinjectionEnabled": false
```

## Slide 39

**#BHUSA @BlackHatEvents**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
" Ipv4Addresses" : [
Te
"VWPRCID": "vec-Oc0e2d3975e5530d82",
"“ServiceName": “high-priv-service",
"FaultinjectionEnabled": false
```

## Slide 40

###### It all started with a service name

##### Where’s ecs:ListServices ???

**#BHUSA @BlackHatEvents**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
It all started with a service name
AmazonEC?2ContainerServiceforEC2Role
Default policy for the Amazon EC? Role for Amazon EC2 Container Service.
“Logs :PutLogEvents"
]
3
"Resource": "*"
1
#BHUSA @BlackHatEvents
```

## Slide 41

###### Proxy

**#BHUSA @BlackHatEvents**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
GET https://ecs-a-2.us-east-2.amazonaws.com/ws?agentHash=e06fc44a&agentVersion=1.96.0&clusterArn=ecscape&containerInstanceArn=a
ce%t2Fecscape%2F9d49835bb514485eba4d18£00bdc2801&dockerVersion=DockerVersion%3A+25.0.8&protocolVersion=2&sendCredentials=true
+ 101 Switching Protocols [no content] 27ms
Request Response
redentialsMessage", "message":{"taskArn":"arn:aws:ecs:us-east-2: 746147082083: task/ecscape/1lcc74f4ca7764bbf8ea59326fc41b649", "taskc
{"credentialsId":"74ee6c68-£304-49bd-8£51-98cb4£d90320", "roleArn":"arn:aws: iam: : 746147082083: role/ecscape-role", “accessKeyId": "AS
sessionToken" : "IQoJb3JpZ21uX2VjEDgaCXVzLWVhc3QtMiJIMEYCIQCa2exZ 1qT/P6XxYodaPle/7EOWIR5SFtOYXMVJ42/kpHgIhANQwCFewGAP jKOROut 6K/xh6/a
oM8xRmxTByn0pESFZf£4ki3cQsbWbSQwuEREVRT2GI0QCg/xI1p49RnUYmZw+Y¥+j 7Ge8epM1v833ImlHygDBrxi2fnxmxjZSzjaLlsBIsSxXJ9nc+F4KAUNefqEu/SarEZCo
JMCgFJIy9 jLwOTxsc497J4f£ZrLpdeD8R/wCiwffHrG9 ieayL2IJ3LubkFYrA7RWhtNPk7Bw2h4/ptuj5eF7mwr0N3YcIFFqL3zYiWnOVUYWs+E+sG+MgGGex6cDM3iB2i
Mhmp9cV0kgC7/yVbh51IWz2fAFktKS1E26P6UKNZ juq1FtoRW68mUdEm1pZ I xUMyEXckHgEcs61LZPJRb28k11ItUwI/23S8qDZsCbZhaUG7o0J 1lrnXwizm4 9TyB+0QjC68/v.
u68AiKYPx3Zs11265DDmmSq1/MqWUvgQF2GotEa9Hvml 3WTAi vUyfEzeqm+WMGPT j 5cP15ykC72xu4n0h7cXOsmVTGgAQWd1QeLpWYPLD+C20//syjkVyRMe5qeSMLuRD
26T22:27:282"} “roleType”: "TaskApplication", "messaged": 1af20ef2e-f7cb-4d99~ 929e-43£56£5£40e6"}}
```

## Slide 42

###### Proxy

**#BHUSA @BlackHatEvents**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
1on=1.96.0&clusterArn=ecscape&containerInstanceArn=al
sion$3A+25.0.8&protocolVersion=2ésendCredentials=true
task/ecscape/1lcc74f4ca7764bbf8ea59326£c41b649", taskC
am: :746147082083:role/ecscape-role", "accessKeyId": "AS
Te/7BOWIRSFtOYXMVJ42/kpHgIhANQwCFewGAP jKOROut6K/xh6/a
alibi. ab aii . ch. % A
```

## Slide 43

###### Proxy

**#BHUSA @BlackHatEvents**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
{"type": "IAMRoleCredentialsMessage", "message": {"taskArn":"arn:aws:ecs:us-east~-2: 746147082083: task/ecscape/lcc74f4
, "roleCredentials":{"credentialsId":"74ee6c68-£304-49bd-8£51-98cb4£d90320","roleArn":"arn:aws:iam: :746147082083:role
0534yhalZ94vK1U£","sessionToken" : "IQoJb3JpZ21uX2VjEDgaCxXVzLWVhc3QtMiJIMEYCIQCa2exZ 1qT/P6XxYodaPIe/7EOWIRSFtOYXMVJ42,
XEqwgMDhAYbmyebRYO+oM8xRmxTByn0pESFZf4ki3cQsbWbSQwuEREVRT2GIQCg/xI1p49RnUYmZwtY+ j 7Ge8epM1v833Im1HygDBrxi2fnxmxjZSzji
sP2wjBGrBUGxKAHwWjqJMCgFJly9 jLwOTxsc497J4£ZrLpdeD8R/wCiwffHrG9 ieayL2IJ3LubkFYrA7RWhtNPk7Bw2h4/ptuj5eF7mwr0N3YcIFFqL:
Otwj ZMnTKCMKquc j 3M£Mhmp9cV0kgC7/yVbh5 1Wz2fAFktKS1E26P6UKNZ juqlFtoRW6 8mUdEm1pZIxUMyEXckHgEcs61LZPJRb28k11tUwI/23S8qDi
AtmYmqg/Mo1D/3mfGXsu6 8AiKYPx3Zs11265DDmmSq1/MqWUvgQF2GotEa9Hvm1 3WTAivUyfEzeqm+WMGPT j 5cP15ykC72xu4n0h7cXOsmVTGgAQWd1(¢
piration":"2025-07-26T22:27:28Z2"},"roleType":"TaskApplication", "messageId":"af20ef2e-f7cb-4d99-929e-43£56£5£40e6"}}
```

## Slide 44

## Can I impersonate the ECS agent?

**#BHUSA @BlackHatEvents**

## Slide 45

You have  Ron, can I
3 days research it?
#BHUSA @BlackHatEvents

#BHUSA @BlackHatEvents

## Slide 46

## 03 ECScape

**#BHUSA @BlackHatEvents**

## Slide 47

**#BHUSA @BlackHatEvents**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
requests 17 Q) Discussions © Actions © Security | Insights
@ amazon-ecs-agent *»'
P master ~ P 136 Branches ) 191 Tags Q Goto file Add file ~ "© Code ~
© singholt Release 1.93.1 v b3258c6-2weeks ago ©) 4,900 Commits
B® github Revert "Run Github action Linux tests on ubuntu-22.04" 4 months ago
BB agent-container Add env with required path for appmesh integration. 3 years ago
B® agent Release 1.93.1 2 weeks ago
amazon-ecs-cni-plugins @ 7b4ec60 Update amazon-ecs-cni-plugins to 7b4ec60 (#4442) 5 months ago
amazon-vpc-cni-plugins @ be52143 Migrate Agent to use vpc-eni plugin for awsvpc mode ins... 2 years ago
BB aws-sdk-go-v2 Codegen aws-sdk-go-v2 clients (#4406) 6 months ago
B® build-infrastructure Update CodeBuild CF stack template to add disabled enc... 10 months ago
BB buildspecs Revert changes adding backup Go installation to pr-buil... 9 months ago
OorO+-8¢088
BB doc readme: Clean up the README a bit 8 years ago
```

## Slide 48

###### Instance Role

AmazonEC2ContainerServiceforEC2Role

**ecs:RegisterContainerInstance ecs:DeregisterContainerInstance ecs:DiscoverPollEndpoint ecs:Poll**

**#BHUSA @BlackHatEvents**

## Slide 49

EC2

ECS Agent
ecs:RegisterContainerInstance
Instance Role

RegisterContainerInstance

**#BHUSA @BlackHatEvents**

## Slide 50

EC2

ECS Agent

Instance Role

**#BHUSA @BlackHatEvents**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ ic
ECS Agent Container instances (1) into
Q Filter container instances by property or value
Container instance v Status ¥
904983555b5 14485ebadd18f00bdcz8... e) Active
Instance Role
#BHUSA @BlackHatEvents
```

## Slide 51

EC2

ECS Agent

Instance Role

**#BHUSA @BlackHatEvents**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ ic
ECS Agent
© © Note
This action is only used by the Amazon ECS agent, and it is not intended for use outside of the
agent.
RegisterContainerInstance
CO Focus mode
Registers an EC2 instance into the specified cluster. This instance becomes available to place containers on.
Instance Role
#BHUSA @BlackHatEvents
```

## Slide 52

EC2

ECS Agent
ecs:DiscoverPollEndpoint
Instance Role

DiscoverPollEndpoint

**#BHUSA @BlackHatEvents**

## Slide 53

Poll Endpoint URL

https://ecs-a-1.us-east-2.amazonaws.com

**#BHUSA @BlackHatEvents**

## Slide 54

EC2
ECS Agent
Instance Role

**#BHUSA @BlackHatEvents**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ ic
ECS Agent
This action is only used by the Amazon ECS agent, and it is not intended for use outside of the
agent.
DiscoverPollEndpoint
O Focus mode
Returns an endpoint for the Amazon ECS agent to poll for updates.
Instance Role
#BHUSA @BlackHatEvents
```

## Slide 55

###### **Agent Version Cluster ARN Container Instance ARN … sendCredentials=true**

ECS Agent

**#BHUSA @BlackHatEvents**

## Slide 56

EC2

ECS Agent
Instance Role

**#BHUSA @BlackHatEvents**

## Slide 57

EC2
ECS Agent
ecs:Poll?
Instance Role

**#BHUSA @BlackHatEvents**

## Slide 58

EC2

ECS Agent
ecs:Poll
Instance Role

**#BHUSA @BlackHatEvents**

## Slide 59

EC2

ECS Agent
Instance Role

**#BHUSA @BlackHatEvents**

## Slide 60

###### ACS – Agent Communication Service

Task
Metadata

Agent-Level  IAM
Directives Credentials

**#BHUSA @BlackHatEvents**

## Slide 61

###### ECS Agent – Authentication Flow

**#BHUSA @BlackHatEvents**

## Slide 62

### Can a Task Impersonate the ECS Agent?

**#BHUSA @BlackHatEvents**

## Slide 63

###### ecs:DiscoverPollEndpoint?

ECScape

**#BHUSA @BlackHatEvents**

## Slide 64

###### Brute Force

Poll Endpoint URL https://ecs-a- <u>.<REGION>.amazonaws.com</u>

**#BHUSA @BlackHatEvents**

## Slide 65

EC2

ECScape

**#BHUSA @BlackHatEvents**

## Slide 66

EC2

ECScape

ecs:Poll?

**#BHUSA @BlackHatEvents**

## Slide 67

###### IMDS – Instance Metadata Service

EC2
ECScape
Region
Instance ID
Private IP address
Instance Role
IMDS

**#BHUSA @BlackHatEvents**

## Slide 68

EC2

ECScape
ecs:DiscoverPollEndpoint
Instance Role

DiscoverPollEndpoint

**#BHUSA @BlackHatEvents**

## Slide 69

**Agent Version Cluster ARN** ??? **Container Instance ARN …** ECScape

**#BHUSA @BlackHatEvents**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
app # curl ${ECS_CONTAINER_METADATA_URI_V4}/task | jq
% Total % Received % Xferd Average Speed Time Time Time Current
Dload Upload Total Spent Left Speed
100 1447 100 1447 °o 0 1054k O m-ienie- -nienre- --:--:-- 1413k
{
“Cluster": “ecscape",
“TaskARN": “arn:aws:ecs:us-—east-—2:746147082083:task/ecscape/3e7 £9ea94c394d0e82c3fc52e091d757",
“Family": “ecscape-task",
“Revision”: "4",
“DesiredStatus": "RUNNING",
“KnownStatus": "RUNNING",
“PullStartedAt": "2025-07-26T19:03:12.9403006842",
“PullStoppedAt": "2025-07-26T19:03:13.0546165922",
“AvailabilityZone": "“us-east-2a",
“LaunchType": "EC2",
“Containers”: [
{
“DockerId": "763dd46728a60a73d3edc763607d7e5£303£9c965004cb78924cd334348791fe",
“Name": “ecscape",
“DockerName": “ecs-ecscape-task-—4-ecscape-d0ebb6978ff7c2d35c00",
“Image": “ghcr.io/naorhaziz/ecscape:latest",
“ImageID": "sha256:3£45e8248b514202c690bd26b997d9bf0dae559al£16£93b464F88159856a25b",
“Labels": {
“com.amazonaws.ecs.cluster": “ecscape",
“com.amazonaws.ecs.container-name": “ecscape",
“com.amazonaws.ecs.task-arn": “arn:aws:ecs:us-east-2:746147082083:task/ecscape/3e7£9ea94c394d0e82c3£c52e091d757",
“com.amazonaws.ecs.task-definition-family": “ecscape-task",
“com.amazonaws .ecs.task-definition-version": "4"
},
“DesiredStatus": "RUNNING",
“KnownStatus": "RUNNING",
“Limits": {
“CcPu": 256,
“Memory": 512
},
“CreatedAt": "2025-07-26T19:03:13.0679180542",
“StartedAt": "2025-07-26T19:03:13.3168676932Z",
“Type": "NORMAL",
“ContainerARN": "“arn:aws:ecs:us-east-2:746147082083:container/ecscape/3e7f£9ea94c394d0e82c3£c52e091d757/98e3280F-53£7-4054-bc0f-F817£43e0f03",
“Networks": [
{
“NetworkMode": "host",
“IPpv4Addresses": [
1
}
1
}
1,
“VPCID": "“vpc-0c0e2d3975e553d82",
“ServiceName": "“ecscape-service",
“FaultInjectionEnabled": false
pee eee event
```

## Slide 70

## Except… Container Instance ARN

#BHUSA @BlackHatEvents

## Slide 71

###### Container Instance ARN?

###### ecs:ListContainerInstances ???

**#BHUSA @BlackHatEvents**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Container Instance ARN?
AmazonEC?2ContainerServiceforEC2Role
Default policy for the Amazon EC? Role for Amazon EC2 Container Service.
ecs:ListContainerlnstances ???
“Logs :PutLogEvents"
],
"Resource": "*"
#BHUSA @BlackHatEvents
```

## Slide 72

EC2
RegisterContainerInstance
ECScape
ecs:RegisterContainerInstance
Instance Role
#BHUSA @BlackHatEvents

## Slide 73

###### Container Instance ARN?

EC2
ECS Agent
BoltDB

**#BHUSA @BlackHatEvents**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Container Instance ARN?
Container
ECSCape
v Volume -1
Volume name info
host-root
Source volume
host-root
Storage configurations
Source path Info
/
Container path
/mnt/host-root
BoltDB
Read only
Read only
#BHUSA @BlackHatEvents
```

## Slide 74

Container Instance ARN?
EC2
ECScape ECS Agent
BoltDB
#BHUSA @BlackHatEvents

## Slide 75

###### Amazon ECS container introspection

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Amazon ECS
fapp # curl -s http://localhost:51678/
{
“Cluster’t '
“ContainerInstanceArn”:
“Version”
+
#BHUSA @BlackHatEvents
```

## Slide 76

EC2

ECScape Container Instance ARN Agent Version and Hash

ECS Agent

**#BHUSA @BlackHatEvents**

## Slide 77

EC2
ECScape
Instance Role

**#BHUSA @BlackHatEvents**

## Slide 78

EC2
ECScape
ecs:Poll?
Instance Role

**#BHUSA @BlackHatEvents**

## Slide 79

EC2

ECScape
ecs:Poll
Instance Role

**#BHUSA @BlackHatEvents**

## Slide 80

EC2
ECScape
Instance Role

**#BHUSA @BlackHatEvents**

## Slide 81

Assume

Role

**#BHUSA @BlackHatEvents**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
(2
"aventVersion": "1.08",
"userIdentity": {
"type": "AWSService",
“invokedBy": "“ecs-tasks.amazonaws.com"
},
"eventTime": "2025-07-28711:54:252",
"eventSource": "sts.amazonaws.com",
"eventName": "AssumeRole",
"awsRegion": “us-east-2",
"sourcelPAddress": “ecs-tasks.amazonaws.com",
"userAgent": "ecs-tasks.amazonaws.com",
"“requestParameters": {
"roleArn": “arntaws! iam! : 746147082083: role/s3-—control-role",
"roleSessionName": "b549fae648d24d4dad76cef1c8d54154"
fy
SaAt+TPNWIDERStCWU4VGSTcPoazrhnUuBbe?r Jpdoxin4alJCKV /c45MzZ6FSMnSSb0Sq4H /r+ss
VEKQA/ ]KBSxACSUY4SNrEnupinTCLh5PEBj]qxAYBMbEI+BwGbiwx6fqpex0h16XuL2Dkt
hOLOwT2YP9HSEDJR1g8n7nuu6377ABajajBf6nKT3ikYSPHwOy7 1AxE/pY/3vSBQO==",
"Expiration": "2025-07-26T18:12:522"
#BHUSA @BlackHatEvents
```

## Slide 82

###### ECScape - Final Flow

**#BHUSA @BlackHatEvents**

## Slide 83

###### ECScape - Final Flow

**#BHUSA @BlackHatEvents**

## Slide 84

###### AWS Documentation

**#BHUSA @BlackHatEvents**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
AWS Documentation
The following are the benefits of using task roles:
¢ Credential Isolation: A container can only retrieve
credentials for the IAM role that is defined in the
task definition to which it belongs; a container never
has access to credentials that are intended for
another container that belongs to another task.
#BHUSA @BlackHatEvents
```

## Slide 85

###### AWS Documentation

**#BHUSA @BlackHatEvents**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
AWS Documentation
@ Note
These permissions aren't acccessible by the
containers in the task. For the IAM permissions
that your application needs to run, see
Amazon ECS task IAM role.
#BHUSA @BlackHatEvents
```

## Slide 86

## 04 Impact

**#BHUSA @BlackHatEvents**

## Slide 87

EC2
Task Task
Low Privilege Role High Privilege Role

**#BHUSA @BlackHatEvents**

## Slide 88

EC2

ECScape
Low Privilege Role

Task
High Privilege Role

**#BHUSA @BlackHatEvents**

## Slide 89

EC2
ECScape
High Privilege Role

**#BHUSA @BlackHatEvents**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Using
my task role
Using
another task’s role
#BHUSA @BlackHatEvents
```

## Slide 90

EC2

ECScape

Task Execution Role
Task

**#BHUSA @BlackHatEvents**

## Slide 91

EC2

ECScape Task Execution Role

**#BHUSA @BlackHatEvents**

## Slide 92

Tenant 1 Tenant 2
EC2
ECScape Task

Task

**#BHUSA @BlackHatEvents**

## Slide 93

Tenant 1 Tenant 2 EC2

ECScape

**#BHUSA @BlackHatEvents**

## Slide 94

ECScape

**#BHUSA @BlackHatEvents**

## Slide 95

###### Impact

Cross-Task IAM Role Hijacking Abuse of Task Execution Role Access to ECS Internals No Misconfiguration Needed - IMDS & Instance Role

**#BHUSA @BlackHatEvents**

## Slide 96

## 05 Demo

Demo

**#BHUSA @BlackHatEvents**

## Slide 97

**#BHUSA @BlackHatEvents**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Last updated
ecscape August 01, 2025 at 14:07 (UTC+3:00) ©) C Update cluster ) C Delete cluster ) Launch ¥
Cluster overview
ARN Status CloudWatch monitoring Registered container instances
IF) arn:aws:ecs:us-east-2:746147082083:cluster/e ©) Active © Default 1
cscape
Services Tasks
Draining Active Pending Running
- 3 - 3
Services Tasks Infrastructure Metrics Scheduled tasks Configuration Tags
Tasks (3) ©) Manage tags Run new task
Filter desired status ————__ Filter launch type
Q Filter tasks by property or value Any desired status v Any launch type v 1 &
7 Task v | Laststatus v | Desiredst... v | Task definition v | Healthsta... v | Created at v Started by v
_ IE) 70e3810c9e2e4134b6bfce0112f98d83 (2) Running (2) Running ecscape-task:7 @ Unknown 4 days ago ecs-svc/09499136327...
IE) b549fae648d24d4dad76cef1c8d54154 © Running © Running s3-control-task:4 @ Unknown 4 days ago ecs-svc/17938369179...
I) d2165e5c93194b82b521ebe7a54bbdfd © Running © Running database-task:4 @ Unknown 4 days ago ecs-svc/92367368739...
#BHUSA @BlackHatEvents
```

## Slide 98

**#BHUSA @BlackHatEvents**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
IF] 70e3810c9e2e4134b6bfce0112F98d83, © Running © Running ecscape-task:/
b549fae648d24d4dad76cef1c8d54154 ©) Running ®) Running 53-control-task:4
IF) d2165e5c93194b82b521ebe7a54bbdfd @) Running @ Running database-task:4
#BHUSA @BlackHatEvents
```

## Slide 99

**#BHUSA @BlackHatEvents**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
a 70e38 10c9e27e4134b6bfce0112f98d83 ©) Running ©) Running ecscape-task:7
Task role Task execution role
ecscape-role [4
ecscape-policy
Policy that denies all actions
"Statement": [
{
"Action': es
"Effect": "Deny",
"Resource’: "**
}
],
"Version": "2012-10-17"
#BHUSA @BlackHatEvents
```

## Slide 100

**#BHUSA @BlackHatEvents**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
A b549fae648d24d4dad76cef1c8d54154 ~) Running *) Running 53-control-task:4
Task role Task execution role
53-control-role [7
AmazonS3FullAccess
Provides full access to all buckets via the AWS Management Console.
“Version': "2012-10-17",
"Statement": [
{
"Effect': “ALLow’,
"Action": [
"s3:*",
aT
"$3-object- Lambda: *
iF
“Resource: °*"
#BHUSA @BlackHatEvents
```

## Slide 101

**#BHUSA @BlackHatEvents**

## Slide 102

**#BHUSA @BlackHatEvents**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Q Search [Option+S] A @ {3} United States (Ohio) ¥ editor/naorh@sweet.security ¥
=] Amazon $3 > Buckets > blackhat-las-vegas-2025 @ $) C)
Amazon S3 . blackhat-las-vegas-2025 into
General purpose buckets
Directory buckets < Objects Metadata Properties Permissions Metrics Management >
Table buckets
Vector buckets Preview
Objects (0)
Access Grants —
l Copy $3 URI [] Copy URL ¥ Download Open (2 Delet
Access Points (General Purpose ©) Ly Sopy i * = :
Buckets, FSx file systems =
” ” y ) C Actions ¥ ) C Create folder ) 4 Upload
Access Points (Directory Buckets) ; — ; ; = ;
Objects are the fundamental entities stored in Amazon $3. You can use Amazon S3 inventory [4 to get a list of
Object Lambda Access Points all objects in your bucket. For others to access your objects, you'll need to explicitly grant them permissions.
A
Multi-Region Access Points Learn more [3
CloudShell Feedback Privacy Terms Cookie preferences
© 2025, Amazon Web Services, Inc. or its affiliates.
```

## Slide 103

**#BHUSA @BlackHatEvents**

## Slide 104

**#BHUSA @BlackHatEvents**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
IF d2165e5c93194b82b52 1ebe7a54bbdfd © Running © Running database-task:4
Task execution role
secret-execution-role [4
Task role
"secrets": [
{
"name": “DB_SECRET",
“valueFrom": “arn:aws:secretsmanager:us-east-2: 746147082083 : secret: db-secret-Poluuv'
J,
read-db-password-secret
Policy to read DB_SECRET secret
1- |
27 "Statement": [
Jo {
4~ "Action": [
“secretsmanager :GetSecretVaLlue"
de
"Effect": "Allow",
"Resource": "“arn:aws:secretsmanager:us-east-2: 746147082083: secret: db-secret-Poluuv"
}
],
"Version": "2012-10-17"
#BHUSA @BlackHatEvents
```

## Slide 105

**#BHUSA @BlackHatEvents**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
[Option+s 0) yay @ & United States (Ohio) ¥ editor/naorh@sweet.security ¥
AWS Secrets Manager > Secrets db-secret 0) ‘C)
db-secret
Secret details ©)
Encryption key Secret description
I aws/secretsmanager I) Database secret for demo
Oo
Secret name
1G db-secret
Secret ARN
I) arn:aws:secretsmanager:us-east-2:746147082083:secret:db-secret-Po1uuv
Overview Rotation Versions Replication Tags
Retrieve secret value
Secret value info
CG) CloudShell Feedback © 2025, Amazon Web Services, Inc. or its affiliates Privacy Terms Cookie preferences
```

## Slide 106

**#BHUSA @BlackHatEvents**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
{
1p
“eventVersion": "1.11",
“userIdentity": {
“type": "AssumedRole",
“principalld": “AROA2300U55RQG3KW4K2N: i-0b8a4b70736fc8039",
“arn": “arn:aws:sts::746147082083: assumed-role/ecscape-ecs—instance-role/i-0b8a4b70736f C8039",
“accountId" 746147082083",
“accessKeyld "ASIA[REDACTED:aws-access-key-id]",
“sessionContext": {
“sessionIssuer": {
“type": "Role",
“principalId": "AROA2300U55RQG3KW4K2N",
“arn": “arn:aws: iam: : 746147082083: role/ecscape-ecs-instance-role",
“accountId' "746147082083",
“userName": "ecscape-ecs—instance-role"
}
“attributes: {
“creationDate": "2025-07-28T11:30:08Z",
“mfaAuthenticated": “false”
ty,
“ec2RoleDelivery": "1.0"
+
},
“eventTime": "2025-07-28T11:55:262",
“eventSource": "“ecs.amazonaws.com",
“eventName": “DiscoverPollEndpoint",
“awsRegion": “us-east-2",
“sourceIPAddress": "18.191.77.44",
“userAgent": “aws-sdk-rust/1.3.8 os/linux lang/rust/1.88.0",
“requestParameters": {
“containerInstance": "“arn:aws:ecs:us—east-2: 746147082083: container-instance/ecscape/4b9fbd579af 24baf99cbc4d07806844a",
“cluster": “arn:aws:ecs:us-east-2: 746147082083: cluster/ecscape"
},
“responseElements": null,
“requestID": "lef64c01-b4e3-48e0-9035-4e146924b3a8",
“eventID": “e19a541c-03f1-4034-9b99-—4a482e8d3303",
“readOnly": true,
“eventType": “AwsApiCall",
“managementEvent": true,
“recipientAccountId": "746147082083",
“eventCategory": "Management",
"tlsDetails": {
“tlsVersion": "TLSv1.3",
“cipherSuite": “TLS_AES_128 GCM_SHA256",
“clientProvidedHostHeader": “ecs.us-east-2.amazonaws.com"
}
#BHUSA @BlackHatEvents
```

## Slide 107

**#BHUSA @BlackHatEvents**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
"userIdentity": {
"type": "AssumedRole”,
“principallId’: "AROA2300U55RQG3KW4K2N: 1-O8b8adb7O736TCches9",
"arn: “arniaws:5ts:: 746147082083: assumed-role/ecscape-ecs—instance-role/i-Obéadb/ess6fcees9",
“accountiId": "746147082083",
“accessKeyld": "ASTA2300U55RYW/HCV2N",
"csessionContext": { oO i-Ob8a4b70736fc8039
"sessionlssuer": {
“type": "Role",
“principallId": "AROA2300U55ROG3KW4K2N",
“arn': “arniawS: iam: : #4614 7082083: role/ecscape-ecs—instance-role",
Instance ID
ecscape-ecs-instance-role ino
Summary
Creation date ARN
July 28, 2025, 11:41 (UTC+03:00) [Gj arn:aws:iam::746147082083:role/ecscape-ecs-instance-role
I
“ec2RoleDelivery’: °1.0°
}
1
|
“eaventTime": "2025-07=28711:55: 262",
"aventSource’: “ecs.amaronaws.com",
“eventName’: "DiscoverPollEndpoint”",
#BHUSA @BlackHatEvents
```

## Slide 108

**#BHUSA @BlackHatEvents**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
{
“eventVersion": "1.11",
“userIdentity": {
“type": “AssumedRole",
“principalld": "“AROA2300U55R4HP5MBEPI : b549fae648d24d4dad76cef1c8d54154",
“arn": “arn:aws:sts:: 746147082083: assumed-role/s3-control-role/b549fae648d24d4dad76cef1c8d54154",
“accountId": "746147082083",
“accessKeyId": “ASIA[REDACTED:aws-access-key-id]",
“sessionContext"
“sessionIssuer"
"type": "Role",
“principalId": "AROA2300U55R4HPSMBEPI",
“arn": “arn:aws: iam: : 746147082083: role/s3-control-role",
“accountId": "746147082083",
“userName": "s3-control-role"
},
"attributes": {
“creationDate": "2025-07-28T11:54:252",
“mfaAuthenticated": "false"
}
+
},
“eventTime": "2025-07-28T11:54: 262",
“eventSource": "s3.amazonaws.com",
“eventName" DeleteBucket",
“awsRegion": "us-east-2",
“sourcelPAddress": "18.191.77.44",
“userAgent": "[aws-sdk-rust/1.3.8 os/linux lang/rust/1.88.0]",
“requestParameters": {
“bucketName": “blackhat-las-vegas-2025",
“Host": “blackhat-las-vegas-2025.s3.us-east-2.amazonaws.com"
},
“responseElements": null,
“additionalEventData": {
“SignatureVersion": "SigV4",
"CipherSuite": "TLS_AES_128 GCM_SHA256",
“bytesTransferrediIn": 0,
“AuthenticationMethod": "AuthHeader",
“x-amz-id-2": "“mppBCGXjw9c WMLUhj E6AC4bNTcow+0F3fB/LMwiGXsAV@b5 9a8qCRXKc8tKbRLQZP6 fp rdU6enwO7GY LWYUNXQ==",
“bytesTransferredOut": @
},
“requestID": "WWQ9BO@G4AY6RE2IJQ",
"eventID": "313e534c-Oac5-44f f-a865-8e904f5b2413",
“readOnly": false,
“resources
{
“accountId": "746147082083",
“AWS: :S3::Bucket",
“arn:aws:s3:::blackhat-las-veqas-2025"
#BHUSA @BlackHatEvents
```

## Slide 109

**#BHUSA @BlackHatEvents**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
“userIdentity": {
“typer: “AssumedRole”,
“principallId": “AROA2300USSR4HPSMBEPI : b549fae648d24d4dad/76cef1c8d54154",
“arn: “arniaws:5ts:: 746147082083: assumed—role/s3—control-role/b549taebh4bd27ddd4dadsbcefticaéd54154",
(@) Running @) Running §3-control-task:4
“sessionContext":
"“sessionIssuer": {
"type": "Role",
“principalId": “AROA2300US5R4HPSMBEPI",
“arn: “arniaws: Lam: : 746147082083: role/s3—control-role”",
“accountid": "46147082083",
"userName": "s3=—control-role"
}y
"attributes": {
“creationDate": "2025-07=287T11:54:252",
"mfaAuthenticated": "false"
}
},
"eventTime™: "2625-07-287T11:54: 262",
“eventSource’: “s3.amazonaws.com",
“eventName": “DeleteBucket”",
#BHUSA @BlackHatEvents
```

## Slide 110

**#BHUSA @BlackHatEvents**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
{
“eventVersion": "1.11",
“userIdentity": {
“type": “AssumedRole",
“principalId": "“AROA2300U55R7YDIPAPXQ: d2165e5c93194b82b521ebe7a54bbdfd",
“arn": “arn:aws:sts:: 746147082083: assumed-role/secret-execution-role/d2165e5c93194b82b521ebe7a54bbdfd",
“accountId": "746147082083",
“accessKeyId": "ASIA[REDACTED:aws-access-key-id]",
“sessionContext": {
“sessionIssuer": {
“type": "Role",
“principalId": “AROA2300U55R7YDJPAPXQ",
“arn": “arn:aws: iam: : 746147082083: role/secret-execution-role",
“accountId": "746147082083",
“userName": "secret-execution-role"
}
"attributes": {
“creationDate": "2025-07-28T11:55: 262",
“mfaAuthenticated": "false"
}
}
},
“eventTime": "2025-@7-28T11:55:26Z",
“eventSourc “secretsmanager.amazonaws.com",
“eventName": "GetSecretValue",
“awsRegion": "“us-east-2",
“sourceIPAddress": "18.191.77.44",
“userAgent": “aws-sdk-rust/1.3.8 os/linux lang/rust/1.88.0",
“requestParameters": {
“secretId": “arn:aws:secretsmanager: us—east-2: 746147082083: secret: db-secret-Poluuv"
},
“responseElements": null,
“requestID": "3322cf63-558b-4aba—bd2f-15fcla@fé6dfb",
“eventID": "“f758db74-f9df-4e60-b33e-0109fc7fb202",
“readOnly": true,
“eventType": "“AwsApiCall",
“managementEvent": true,
“recipientAccountId": "746147082083",
“eventCategory": "Management",
"tlsDetails": {
“tlsVersion”: "TLSv1.3",
"cipherSuite": "TLS_AES_128 GCM_SHA256",
“clientProvidedHostHeader": “secretsmanager.us—east-2.amazonaws.com"
}
},
#BHUSA @BlackHatEvents
```

## Slide 111

**#BHUSA @BlackHatEvents**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
r
“useridentity’: +
"type": "“AssumedRole",
“principalld": "AROA2300U55R7YDJPAPXO:d2165e5c93194b82b521ebe/a54bbdfd",
“arn: “arniaws:sts:: 746147082083: assumed-role/secret-execut ion—-role/d?2165e5c93194b82b527 lebefa54bbdtd",
@) Running @) Running database-task:4
"sessionissuer": +
“type": "Role",
“principalId": "AROA2300U55R7YDIPAPXQ",
"arn: “arnitaws: Lam: :/46147082083: role/secret-execution-role”,
“accountid": "746147082083",
"userName": “secret-execution-role"
he
“attributes": {
“creationDate": "2@25-87=287T11:55: 262",
“mfaAuthenticated": "false"
}
hy
“aventTime": "2025-07=-28711:55:262",
“eventSource’: “secretsmanager.amazonaws.com",
“eventName": “GetSecretValue",
#BHUSA @BlackHatEvents
```

## Slide 112

###### ECScape POC GitHub:

**#BHUSA @BlackHatEvents**

## Slide 113

## 06 Mitigation

**#BHUSA @BlackHatEvents**

## Slide 114

###### Disable Tasks IMDS Access

|EC2
|
|---|
|Task|
|Instance Role
IMDS|

**#BHUSA @BlackHatEvents**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Disable Tasks IMDS Access
Block access to Amazon EC2 metadata
When you run your tasks on Amazon EC2 instances, we strongly recommend that you block access to Amazon EC2 metadata to prevent your containers from inheriting the role assigned to those instances. If your applications have to call an
AWS API action, use IAM roles for tasks instead.
To prevent tasks running in bridge mode from accessing Amazon EC2 metadata, run the following command or update the instance’s user data. For more instruction on updating the user data of an instance, see this AWS Support Article 2. For
more information about the task definition bridge mode, see task definition network mode.
sudo yum install -y iptables-services; sudo iptables --insert FORWARD 1 --in-interface docker+ --destination 169.254.169.254/32 --jump DROP
For this change to persist after a reboot, run the following command that's specific for your Amazon Machine Image (AMI):
* Amazon Linux 2
sudo iptables-save | sudo tee /etc/sysconfig/iptables && sudo systemctl --now iptables
* Amazon Linux
sudo service iptables save
For tasks that use awsvpc network mode, set the environment variable ECS_AWSVPC_BLOCK_IMDS to true inthe /etc/ecs/ecs.config file.
‘ou should set the ECS_ENABLE_TASK_IAM_ROLE_NETWORK_HOST variable to false inthe ecs-agent config file to prevent the containers that are running within the host network from accessing the Amazon EC2 metadata.
#BHUSA @BlackHatEvents
```

## Slide 115

###### Task Role

Task
Task Role

#BHUSA @BlackHatEvents

## Slide 116

###### Minimize Task Execution Role Permissions

Task
Task
Execution
Role

**#BHUSA @BlackHatEvents**

## Slide 117

###### **Separate high-privilege and low-privilege workloads**

EC2
Task Task
Low Privilege Role High Privilege Role

**#BHUSA @BlackHatEvents**

## Slide 118

###### **Separate high-privilege and low-privilege workloads**

EC2 EC2
Task Task
Low Privilege Role High Privilege Role

**#BHUSA @BlackHatEvents**

## Slide 119

###### **Isolate Tenants In Multi-Tenant Systems**

Tenant 1 Tenant 2
EC2
Task Task

**#BHUSA @BlackHatEvents**

## Slide 120

###### **Isolate Tenants In Multi-Tenant Systems**

EC2 EC2
Task Task

**#BHUSA @BlackHatEvents**

Tenant 1 Tenant 2

## Slide 121

###### Best Practices

Separate High and Low Privileged Workloads Isolate Tenants in Multi-Tenant Systems Minimize Task / Task Execution Role Permissions

**#BHUSA @BlackHatEvents**

## Slide 122

## 07 Summary

**#BHUSA @BlackHatEvents**

## Slide 123

###### Vendor Response

**#BHUSA @BlackHatEvents**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Vendor Response
AWS Security @
to naorhaziz, rong, noag, orel, me +
ll
After additional review and internal discussion, we are confirming our original determination
that the behavior described in this report does not present a security concern for AWS.
The team is updating the public documentation to more effectively communicate our security
best practices in response to your concerns. | will follow up with the specific language and
resource links as soon as these changes are live. In addition, the team is also considering
long-term defense in-depth changes to the service to increase the security posture for our
customers.
#BHUSA @BlackHatEvents
```

## Slide 124

###### Documentation Change

**#BHUSA @BlackHatEvents**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Documentation Change
The following are the benefits of using task roles:
¢ Credential Isolation: A container can only retrieve
credentials for the IAM role that is defined in the
task definition to which it belongs; a container never
has access to credentials that are intended for
another container that belongs to another task.
The following are the benefits of using task roles:
¢ Credential Isolation: Task credentials are isolated at the EC2 instance level.
While each task receives credentials for its defined IAM role through the ECS
container agent and instance metadata service, tasks running on the same EC2
instance may potentially access credentials belonging to other tasks on that
instance. For workloads requiring stronger isolation, consider using Fargate
which provides task-level isolation.
#BHUSA @BlackHatEvents
```

## Slide 125

###### AWS Acknowledgements

**#BHUSA @BlackHatEvents**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
AWS Acknowledgements
AWS Security @
to naorhaziz, rong, noag, orel, me +
ll
As for formal credit in the ECS documentation, while we're unable to include this in our public
documentation at this time, we continue to work with our docs team on this request.
Regarding recognition of your work, we would be glad to draft a statement of appreciation that you can
include in your presentation and blog post. This would help highlight the positive outcomes of your
research and our collaborative engagement.
#BHUSA @BlackHatEvents
```

## Slide 126

###### AWS Acknowledgements

**#BHUSA @BlackHatEvents**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
AWS Acknowledgements
aWS
wee)
AWS would like to thank Sweet Security and security researcher Naor Haziz,
whose research highlighted the need for more clarity in this blog post
regarding security boundaries between containers and instances. We also
made clarifying changes to ECS documentation as a result of that feedback.
#BHUSA @BlackHatEvents
```

## Slide 127

###### AWS Official Statement

The issues raised by Sweet Security are very important and instructive regarding basic elements of the AWS shared responsibility model [1]. While AWS often provides agents to run on customer-controlled EC2 instances [2] to provide service functionality ( _e.g._ , ECS agent, CloudWatch agent, Systems Manager agent, EMR on EC2 agent, etc.), in all cases these agents run within the customer’s security boundary, and any and all associated AWS roles (and their credentials and permissions) are understood and designed to be fully accessible to customers. The same is true of the open source components [3] running on customer EC2 instances used b y the EKS service. Our threat model also assumes that such roles used by agents may be directly used and potentially abused by customers, and the services are designed to protect themselves from such possible abuse.

In the case of ECS, at the time of the original service launch the only roles/credentials/permissions made automatically available to tasks and containers were those of the underlying instance. Many customers continue to use ECS’s IAM integration in that manner. Later, for customer convenience, a different set of roles (and associated credentials and permissions) was made available at the task level [4] [5] to separate and simplify management of the permissions granted directly to customer code running inside containers in ECS tasks. At that time, we added documentation [6] for iptables-based techniques whereby customers could deny network access to the underlying instance credentials from hosted containers. That configuration remains an option and is not the default behavior. AWS continuously reviews default configurations in our services and as over time a decreasing number customers use instance credentials in ECS/EC2, changes to this default behavior are under consideration. However, even if the default networking behavior was changed, containers were and are never considered a security boundary in AWS [7]. Thus, even such a n etworking change could make it more complicated for containers to access the privileges available to the ECS agent, not make it impossible. Moreover, in EC2-based deployments of ECS, the customer is in full control of both the underlying instance as well as the associated tasks and containers that run inside it. Thus, customers are responsible for guarding against all security issues within a container seeking to access code and data in the underlying instance or other containers hosted on it. In sum, whatever IAM privileges exist in the underlying instance / operating system are assumed to be and are directly or indirectly available to customers, and to the code that they deploy, one way or another.

AWS would like to thank Sweet Security for their interesting and valuable research, which resulted in modifications and clari fications in our documentation and an existing blog post to make more explicit the security boundaries and the implicit threat model of the ECS service (as well as, by implication, analogous scenarios involving AWS-supplied agents running on customer-controlled EC2 instances). Our customers have benefited from this research and collaboration.

- [1] <u>https://aws.amazon.com/compliance/shared-responsibility-model/</u> [2] <u>https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-config.html</u>

- [3] <u>https://docs.aws.amazon.com/eks/latest/userguide/eks-compute.html</u>

- [4] <u>https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html</u>

- [5] https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_execution_IAM_role.html

- [6] <u>https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-metadata-endpoint-v2.html</u>

[7] <u>https://aws.amazon.com/blogs/security/security-considerations-for-running-containers-on-amazon-ecs</u>

**#BHUSA @BlackHatEvents**

## Slide 128

###### Summary

On EC2, tasks and the ECS agent share one trust boundary A task can impersonate the ECS agent Task-level hardening is essential

**#BHUSA @BlackHatEvents**

## Slide 129

## Thanks!

<u>naorhaziz@gmail.com</u> Naor Haziz https://github.com/naorhaziz

**#BHUSA @BlackHatEvents**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
; I’m so glad
each task has
its own IAM role
Then how’s it
getting other task
\ creds on that instance?
Thanks!
-) naorhaziz@gmail.com
‘in Naor Haziz
https://github.com/naorhaziz
#BHUSA @BlackHatEvents
```

## Companion resources

### `Naor Haziz_ECS-cape – Hijacking IAM Privileges in Amazon ECS_tools.txt`

```text
https://github.com/naorhaziz/ecscape
```
