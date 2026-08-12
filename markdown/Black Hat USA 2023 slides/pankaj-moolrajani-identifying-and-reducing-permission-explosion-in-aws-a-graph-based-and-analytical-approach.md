---
title: "Identifying and Reducing Permission Explosion in AWS A Graph-Based and Analytical Approach"
speakers: ["Pankaj Moolrajani"]
conference: "Black Hat"
conference_full: "Black Hat USA 2023"
edition: "USA"
year: 2023
source_pdf: "Black Hat USA 2023 slides/Pankaj Moolrajani_Identifying and Reducing Permission Explosion in AWS A Graph-Based and Analytical Approach.pdf"
pages: 103
sha256: "331766b8ea411a27f16e17390239c3e0205760afe34997116fb4b154336bf9f9"
text_chars: 12591
ocr_pages: 32
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:23:53Z"
---
# Identifying and Reducing Permission Explosion in AWS A Graph-Based and Analytical Approach

**Speakers:** Pankaj Moolrajani  
**Conference:** Black Hat USA 2023  
**Source:** `Black Hat USA 2023 slides/Pankaj Moolrajani_Identifying and Reducing Permission Explosion in AWS A Graph-Based and Analytical Approach.pdf` (103 pages)


## Slide 1

Identifying & Reducing Permission Explosion in AWS By Pankaj Moolrajani Security Engineering Lead @Motive pmoolrajani@gmail.com @p_moolrajani

## Slide 2

I

Creating Software Indian Food

Walking

## Slide 3

What are we learning today about Permission Explosion?

How to IDENTIFY?

How to FIX?

How to KEEP IT AWAY?

## Slide 4

### Sneak Peak

Nodes:  1465 Nodes:  1152
Edges:  4749 Edges:  1729

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Sneak Peak
production-qa
production-qa
production-platform-
production-platform-admin:
production-embedded
production-safety
production-backend produéjion-backend
```

## Slide 5

Basics

## Slide 6

### What is a Permission?

rds:DeleteDBInstance
Bob Developer rds: fleet-db
(RBAC)

A user’s right to perform an action on a resource eg:  Bob with Developer role is allowed to <u>DeleteDBInstance</u> - <u>rds:fleet-db</u>

## Slide 7

What is Permission Explosion?

User’s having more permissions than they need for their job

## Slide 8

Why does it occur in AWS?

## Slide 9

Reason 1 - Permission Creep

User roles change over time, granting more access while rarely revoking unnecessary permissions.

## Slide 10

### Reason 2 - Temporary Access

Users request new permissions for ad-hoc tasks, and when granted, they become permanent for all users in that role.

## Slide 11

Reason 3 - Easy to Grant Broad Access

Few broad roles with fixed permissions simplify management, but compromise fine-grained control.

## Slide 12

Mathematics of Permission Explosion Gaining Clarity in Chaos

## Slide 13

### Permission Utilization Ratio (PUR)

Represents TRUE utilization ratio of a permission in a role.

## Slide 14

### Permission Utilization Ratio (PUR)

PUR of a permission in a role can be determined by using <u>frequency of use</u> and the <u>number of users</u> who utilize it

## Slide 15

### Permission Utilization Ratio (PUR)

median num days used by users num users used PU = total num days   total num users

## Slide 16

### Under-Utilized Permission Ratio (UPR)

Proportion of the permissions within a role that are rarely or never used

## Slide 17

### Under-Utilized Permission Ratio (UPR)

UPR =

1 - Sum of (PUR’s) Num of Permissions

## Slide 18

Calculate UPR of a Permission in a Role

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Calculate UPR of a Permission in a Role
# Role - piam_subteam_platform_security
# Resource - s3:rnd-bucket
# Action - PutObject
# Permission - s3:rnd-bucket-PutObject
# Input data
median_days_used_by_users = 150
num_users_used = 10
total_num_days = 365
total_num_users = 42
# Calculate Permission Utilization Ratio (PUR)
pur = (median_days_used_by_users * num_users_used) / (total_num_days *
total_num_users)
# Calculate Under Utilized Permission Ratio
upr = 1 - permission_usage_ratio
# Output
print("PUR:", pur)
print("UPR:", upr)
PUR: @.1
UPR: @.9
```

## Slide 19

AWS Setup

## Slide 20

AWS IAM Roles

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
AWS IAM Roles
production-qa production-safety
production-backend production-embedded production-platform-admin
```

## Slide 21

AWS Resource Types

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
AWS Resource Types
Route 53 Cloud Front
ECS
EC2
s3
Secrets Manager
Backup
```

## Slide 22

Tools

## Slide 23

Tools

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Tools
co @
Python Google Colab SigmaJS
Sqlite Database
```

## Slide 24

Data Schema - Role Permissions DB

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Data Schema - Role Permissions DB roles
name
app_id integer >
apps
as varchar role_permissions
id? integer
resource type_actions name varchar
*
name varchar
is_accessible boolean
resources is_accessed boolean
name varchar resource_types upr float
```

## Slide 25

Sample Graph (ipysigma)

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Sample Graph (ipysigma)
CO S piam-split-roles.ipynb +
File Edit View Insert Runtime Tools Help All changes saved
E\ comment 2% Share &
+ Code + Text Reconnect ~ a
» eBshas:
Q oe graph = get_graph(splitted_rp, "sp jext")
graph
{x} Undirected Graph
79 nodes platform-dba
o 94 edges
info
Node platform-dba
From kwargs:
node_size 18
Attributes:
node_type role
color #FF9900
label platform-dba
87.28271484375
y -3.9546258449554443
Computed metrics:
degree 18
```

## Slide 26

How to IDENTIFY?

## Slide 27

#### Starting Point

Permission Explosion

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Starting Point
production-qa
Permission Explosion
production-platform-admin’
production-embedded
production-backend
```

## Slide 28

Accessible vs Accessed Permissions in a Role

Permissions Unused 50%

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Accessible vs Accessed Permissions in a Role
Permissions Unused
50%
1500
1250
@® Accessible
Accessed
1000
750
500
250
```

## Slide 29

#### Under-Utilized Permission Ratio

Overall UPR 0.93

## Slide 30

#### Permissions Per User

QA Role 786

    production-qa

## Slide 31

How to FIX?

## Slide 32

# FIX Strategy 1

## Slide 33

#### Roles & Permissions

Let’s Simplify

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Roles & Permissions
production-qa
Le t Ss S m p | ify production-platform-admin’
production-embedded
production-backend
```

## Slide 34

Roles & Resource Types

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Roles & Resource Types
Ay
© ) ec2:network-act
a
production-ga
production-embedded
©) sa:bucker
Production-backend
=>,
()) ec2:instance
production-safety
rary
©) cerrepository
```

## Slide 35

#### Roles & Resource Types

Unused Resource Types

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Roles & Resource Types @ ccereworiac
|) ec2:instance
production-embedded
Unused Resource
Types a
© pssibucket
production-backend
) ccr:repository
```

## Slide 36

Data Insight Unused Resource Types = 1

ec2:network-acl
    production-qa ec2:instance
ecr:repository
s3-bucket

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Data Insight ©) ec2:network-acl
. > .
production-ga > {> ec2:instance
Unused Resource
Types = 1
© ecr:repository
© s3-bucket
```

## Slide 37

Strategy 1: Remove Unused Resource Types
    production-qa
    production-qa
-20%
Permissions: 763 Permissions: 618

## Slide 38

# FIX Strategy 2

## Slide 39

#### Roles & Permissions

Permissions for Resource Types in Use

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Roles & Permissions sencuction-ombecidod
Permissions for
Resource Types in
Use
production-platform-
```

## Slide 40

#### Roles & Permissions

Let’s Simplify

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Roles & Permissions
production-backend
Let’s Simplify
production-platform-
```

## Slide 41

#### Permission Reduction

    production-qa

UPR: 0.46

## Slide 42

#### Permission Reduction

Used vs Unused Permissions

    production-qa

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
lon
Reduct
ission
Perm
19°)
a
¢
aS)
=
3)
5
ae)
(e)
p=
a
Used vs Unused
isSions
Perm
```

## Slide 43

#### Permission Reduction

Unused Permissions Removed

    production-qa

476

## Slide 44

#### Strategy: Remove Unused Permissions

production-qa Permissions: 618

-23%
    production-qa
Permissions: 476

## Slide 45

# FIX Strategy 3

## Slide 46

#### Roles & Permissions

Only Used Permissions

## Slide 47

#### Role & Permissions - Used At Least Once

Let’s Simplify

## Slide 48

#### Permissions Used At Least Once

## Permissions - 476

    production-qa

## Slide 49

DB Table - Role Permissions

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
DB Table - Role Permissions
role resource action |upr | pur |
1 production-qa arn:aws:ecr:us-east-1:933794580186:repository/fleet/k2web BatchDeletelmage 0.89 0.11
2 production-qa arn:aws:ecr:us-east-1:933794580186:repository/fleet/k2web BatchGetimage 0.91 0.09
3 production-qa arn:aws:ecr:us-east-1:933794580186:repository/fleet/k2web CompleteLayerUpload 0.88 0.12
4 production-qa arn:aws:ecr:us-east-1:933794580186:repository/fleet/k2web CreateRepository 09 0.1
5 production-qa —_arn:aws:ecr:us-east-1:933794580186:repository/fleet/k2web DeleteLifecyclePolicy 0.93 0.07
6 __ production-qa arn:aws:ecr:us-east-1:933794580186:repository/fleet/k2web DeletePullThroughCacheRule 0.88 0.12
```

## Slide 50

#### Rarely Used Permissions Removed

UPR > 0.95 Permissions - 286

production-qa

## Slide 51

#### Strategy: Remove Rarely Used Permissions (UPR >0.90)

-40%
    production-qa
    production-qa
Permissions: 476 Permissions: 286

## Slide 52

Pop Quiz

## Slide 53

When a Company Grows, Permissions per User Increases or Decreases?

## Slide 54

# FIX Strategy 4

## Slide 55

#### Production Platform Admin Role

 production-platform-admin

## Slide 56

#### Production Platform Admin Role

Users 29

 production-platform-admin

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Production Platform Admin Role
Adam Mullins
Edwin Garner
Users
29
Craig Lewis
Alejandro Brown
| production-platform-admin
Alexandra Wagner
```

## Slide 57

#### Production Platform Admin Role

Permissions Per User 75

 production-platform-admin

## Slide 58

#### Production Platform Admin Role

Split the Role

platform-dba

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Production Platform Admin Role
platform-dba
Emily Wolfe
platform-iot
Split the Role
Jack Mason
platiorm-sre
Anthony Howard
platform-security
```

## Slide 59

#### Role - Users & Permissions

## Permissions Splitted

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Role - Users & Permissions
Permissions Splitted
platform-dba
a
a
a
4
‘platform-devprod
```

## Slide 60

#### Role - Users & Permissions

Permissions per User 32

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Role - Users & Permissions
Permissions per User
32
platform-dba
a
a
a
4
‘platform-devprod
```

## Slide 61

Strategy: Split the Permissions
-76%
platform-dba
production-platform-admin
Permissions: 75 Permissions: 18

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Strategy: Split the Permissions
+6] platform-d ba
fn
\prod ction-platform-admin
Permissions: 75 Permissions: 18
```

## Slide 62

#### Strategy: Split the Permissions

production-platform-admin

-57%

Permissions Per User: 75

Permissions Per User: 32

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Strategy: Split the Permissions
platform-dba
\production-platform-admin
Platform-devprod
Permissions Per User: 75 Permissions Per User: 32
```

## Slide 63

How to KEEP IT AWAY?

## Slide 64

### Automated Policy Generation

#### Runs Every Week

#### IAM Policy Generator

UPR Threshold > 0.90 UPR Duration = 90d

AWS IAM Role

Role Permissions

## Slide 65

RECAP

## Slide 66

### RECAP

Identifying & Reducing Permission Explosion is a Data Problem Strategies to Fix Permission Explosion:

Reason for Permission Explosion Solution Permission Creep Remove Unused Permissions Temporary Access Remove Rarely Used Permissions Broad Access Roles Create Smaller Team/Subteam Specific Roles

## Slide 67

How to GET STARTED?

## Slide 68

### How to GET STARTED ?

Push IAM Data to Role Permissions Database

Use Workbench Notebook to Identify Permission Explosion Generate New Policies Based on Findings

Automate Policy Generation & Enforcement of Policies

## Slide 69

# PermCutter

<u>h</u> <u>ttps://github.com/PankajMoolrajani/PermCutter</u>

## Slide 70

Q&A

## Slide 71

Thank You

## Slide 72

#### Role - Users & Permissions

75 permissions 29 users Dba 18 Iot 24

## Slide 73

#### Role - Users & Permissions

75 permissions 29 users Dba 18 Iot 24

## Slide 74

#### Role - Users & Permissions

75 permissions 29 users Dba 18 Iot 24

## Slide 75

#### Role - Users & Permissions

75 permissions 29 users Dba 18 Iot 24

## Slide 76

Strategy 3 - Remove Rarely Used Permissions 476 upr dropped to 286

production-qa

## Slide 77

Strategy 3 - Remove Rarely Used Permissions 0.78

production-qa

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
UPR (User Percentage Rate)
Strategy 3 - Remove Rarely Used Permissions
0.78
UPR for Each Role
Role
tion-qa
```

## Slide 78

Permission Reduction

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
production-qa
pproduction-platforr-admin
production-embedded
production-backend)
```

## Slide 79

Permission Reduction

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
production-qa
pproduction-platforr-admin
production-embedded
production-backend)
```

## Slide 80

Permission Reduction

Remove Permissions for Unused Resource Types
UPR: 0.46

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Permission Reduction
production-platform-admin
Remove Permissions
production-satety
```

## Slide 81

#### Permission Reduction

### Split Roles

UPR: 0.46

## Slide 82

#### Permission Reduction

Nodes 104

Avg per user 102

## Slide 83

#### Permission Reduction

Nodes 104

Average per user

32

## Slide 84

Permission Reduction

Security - 30 Dba 30 Devprod - 36

UPR: 0.46

## Slide 85

#### Permission Reduction

### Split Roles

UPR: 0.46

## Slide 86

#### Permission Reduction

### Split Roles

UPR: 0.46

## Slide 87

#### Permission Reduction

### Split Roles

UPR: 0.46

## Slide 88

#### Permission Reduction

AWS Setup: Permission Usage by Role

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Permission Reduction
AWS Setup: Pt
Count of Permissions
175
150
1254
100
75
Number of Permissions - Accessible vs. Accessed
lm Accessible
mm Accessed
Roles
```

## Slide 89

#### Permission Reduction

Remove Unused Permissions

## Slide 90

Permission Reduction

Remove Unused Permissions

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Permission Reduction
st-1 :983794580186:db:dispatch-summary-production--DescribeDBInstanceAutomatedBackups
immary-production--DescribeDBSnapshots
Remove
```

## Slide 91

#### Permission Reduction

Remove Unused Permissions

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Permission Reduction
AN ANB LAN BERAStSTHAPAGS HANS BGrabasspeUsy
|
arg tis Sash ¥ 93 HSER TBE ab feet bute Bree luetion
Remove Unused Permissi¢
```

## Slide 92

#### Permission Reduction

Remove Unused Permissions

UPR: 0.0

## Slide 93

#### Permission Reduction

Talk about as the companies go big, the scope decreases and number of resources people need access to decreases. Talk about platform team example.

Split the roles

## Slide 94

#### Permission Reduction

Show the network graph + new UPR

Result

## Slide 95

#### Permission Reduction

Show the network graph + new UPR

Result

## Slide 96

#### Permission Reduction

● How can i do the same thing in my company

Key Takeaways

## Slide 97

#### Permission Reduction

1. Get the data in the schema - github spec. 2. Tools - python + ipysigma to build visualizations. link

How do i do this.

## Slide 98

#### Strategy: Remove Unused Permissions

Overall UPR 0.93 → 0.78

## Slide 99

Permission Reduction Remove Permissions for Unused Resource Types

UPR: 0.46

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Count
Sum of is_ accessible and is accessed for each Role
i
lm is_accessible |
L is accessed |
1000
800
600
400
200
° > > @ <\
& we SS 6
ous > te) ; oe Ko
eo Ra 2 & <
>) < < ~~» Re)
aS © £ & &
oc : os @ < s
Ss oe s {e)
fe) S : oe
$ 3 x
g v
&
$
Role
```

## Slide 100

Strategy 3 - UPR df_isaccess=1 0.85

production-qa

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
UPR (User Percentage Rate)
Strategy 3 - UPR df_isaccess=1
0.85
UPR for Each Role
2°
©
2°
a
ad
&
0.2
0.0 -
Role
```

## Slide 101

Theme

## Slide 102

Why does it occur in AWS?

Root Cause Analysis

350 services x 13.75k Permissions = Decisions

## Slide 103

Why does it occur in AWS?

How did it happen in our company?

50 engineers working on everything     500 engineers working on specific areas.

Roles - platform-admin, fuel, safety, cards - manage their own infra had access to pretty much everything

Then we scaled from 5 to 20 teams - but continued using the same roles as the team level roles gave us the access we needed to do the job.
