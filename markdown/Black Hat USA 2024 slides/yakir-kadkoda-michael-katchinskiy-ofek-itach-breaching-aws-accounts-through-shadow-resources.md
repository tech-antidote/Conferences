---
title: "Breaching AWS Accounts Through Shadow Resources"
speakers: ["Yakir Kadkoda", "Michael Katchinskiy", "Ofek Itach"]
conference: "Black Hat"
conference_full: "Black Hat USA 2024"
edition: "USA"
year: 2024
source_pdf: "Black Hat USA 2024 slides/Yakir Kadkoda & Michael Katchinskiy & Ofek Itach_Breaching AWS Accounts Through Shadow Resources.pdf"
pages: 101
sha256: "8631788edae35599a1d6ce9a7f825b1c7e2caada1accf1facf4b1ccec2d6e25d"
text_chars: 27736
ocr_pages: 35
has_ocr: true
redacted_secrets: 0
ocr_confidence: 87.9
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T04:44:58Z"
---
# Breaching AWS Accounts Through Shadow Resources

**Speakers:** Yakir Kadkoda, Michael Katchinskiy, Ofek Itach  
**Conference:** Black Hat USA 2024  
**Source:** `Black Hat USA 2024 slides/Yakir Kadkoda & Michael Katchinskiy & Ofek Itach_Breaching AWS Accounts Through Shadow Resources.pdf` (101 pages)


## Slide 1

Breaching AWS Accounts Through Shadow Resources

Yakir Kadkoda

Michael Katchinskiy Ofek Itach

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 94/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
AUGUST 7-8, 2024
BRIEFINGS
Breaching AWS Accounts
Through
Shadow Resources
N
Yakir Kadkoda
Michael Katchinskiy
Ofek Itach
```

## Slide 2

##### AWS Account ID

Each AWS account has a unique account ID

12-digit ID

Some treat it as a secret, others don't

#BHUSA @BlackHatEvents

## Slide 3

##### AWS Account ID

Each AWS account has a unique account ID

12-digit ID

Some treat it as a secret, others don't

#BHUSA @BlackHatEvents

## Slide 4

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 91/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
O Plerion Following
3,758 followers
In 2022 AWS unequivocally stated that “Account IDs are not considered
sensitive.” We think they are closer to secrets than most of us would like to
admit, so we're re-opening the debate. Check out the data and attack examples
in this post and let us know if you agree
eC ebrandwine The final answer: AWS account IDs are secrets
@ebrandwine
Account IDs are not secrets. They're discoverable in the ARNs of
resources and in various other places. Our threat model assumes that
they're known; we do not rely on their secrecy.
Nick Frichette @Frichette_n - Jul5 see
4:42 AM - Jan 28, 2022 . .
Also wait, let's talk about this. The technique they blocked was used to
derive an AWS account ID from a bucket name. AWS has vehemently said in
D dabbadoo - 5y 290 the past that account IDs are not secret. But they put in the effort to
Some data points: prevent this? That seems not right.
© run fla id and flaws2.cloud where you find the account ID (and also get “ess keys and
username/p:
jords to IAM users and roles) and have not had negative consequences.
© Anumber of vendors, and AWS, make their account I
iblic for various reasons, and as far as | know, they ? ;
BadDoggie
do not have negative conse
labs/cloudmapper/blob/master/vendor.
aml Not sure if it’s changed, but when | worked at AWS (almost 2 years ago) Account Numbers were definitely
considered sensitive,
| think the only legit reasons why AWS tutorials and others make their account IDs private are’
We were told not to send files containing Account Numbers to anyone - not even the account owners. In the case
« It's somewhat distracting as your ID will be different when you follow the tutorial ;
of account owners it was allowed if the file was encrypted.
* Ifyou make some bad mistakes elsewhere with your account, the account ID is needed to take ad
those mistakes.
Personally, | think the main reason AWS and others hide their account IDs is just that others have done it and their
worried to stop doin
for bothering to hide t
because they don't know why it was done, but as | pointed out, there isn’t a strong case
e IDs.
```

## Slide 5

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 96/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
they are not considered secret,
```

## Slide 6

<u>https://rhinosecuritylabs.com/aws/assume-worst-aws-assume-role-enumeration/ https://blog.plerion.com/aws-account-ids-are-secrets/</u>

#BHUSA @BlackHatEvents

## Slide 7

#BHUSA @BlackHatEvents

## Slide 8

aws sts get-caller-identity

**Yakir Kadkoa** Security Lead Security Researcher YakirKad

**Michael Katchinskiy** Formerly                   Security Senior Security Researcher mike_katch

**Ofek Itach** Security Senior Security Researcher ofekitach

#BHUSA @BlackHatEvents

## Slide 9

Agenda

Demonstrate
Introduce Showcase several
open-source tool
“Shadow Resources” AWS vulnerabilities
" TrailShark "
Introduce
Mitigation and
"BucketMonopoly" Recommendations

#BHUSA @BlackHatEvents

## Slide 10

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 91/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Console Home into
Services Q
CloudFormation > Stacks > Create stack
Step 1
Create stack
Create stack
Step 2
Specify stack details Specify template
or YAML file that d
Info
A template is a
Configure stack options
Template source
Review and create © Amazon $3 URL
Upload a template file
—N Choose file
[ sam_templateyaml
```

## Slide 11

##### Shadow Resource

AWS resources generated **automatically** or **semiautomatically**

Most of the time, **spawned without user intervention**

Might go **unnoticed** by the account owner

#BHUSA @BlackHatEvents

## Slide 12

##### S3 Buckets as Shadow Resources

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 93/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
S3 Buckets as Shadow Resources
Specify template info
A template is a JSON or YAML file that describes your stack
Template source
Amazon $3 URL © Upload a template file
Upload a template file
fA Choose file
sam_template.yaml
AML formatte
```

## Slide 13

##### Bucket Uniqueness

S3 bucket names must be **globally unique** across all AWS accounts

If you create 'cool-bucket-1', **no one else can claim that bucket name**

#BHUSA @BlackHatEvents

## Slide 14

## AWS CloudFormation Vulnerability

## Slide 15

##### What is AWS CloudFormation?

Create or use an existing  Save locally or in S3  Use AWS CloudFormation to create a
1 2 3
template bucket stack based on your template

<u>https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-overview.html</u>

#BHUSA @BlackHatEvents

## Slide 16

AWS User AWS CloudFormation

1 Upload a template file
CreateUploadBucket
2
3 BucketName If the Bucket Does Not Exists:
Create Bucket
4 PutObject
Return Bucket Name
template_file.yaml
5 …
6 CreateStack

#BHUSA @BlackHatEvents

## Slide 17

##### CloudFormation Bucket Name

cf-templates-a3gjv31ap90h-us-east-1
Prefix Hash Region

#BHUSA @BlackHatEvents

## Slide 18

AWS Account
AWS CloudFormation AWS S3 Bucket
Bucket name:  cf-templates-a3gjv31ap90h-us-east-1
us-east-1

#BHUSA @BlackHatEvents

## Slide 19

AWS Account AWS Account
AWS CloudFormation AWS S3 Bucket AWS CloudFormation AWS S3 Bucket
Bucket name:  cf-templates-a3gjv31ap90h-us-east-1 Bucket name:  cf-templates-a3gjv31ap90h-eu-west-2
us-east-1 eu-west-2

#BHUSA @BlackHatEvents

## Slide 20

AWS Account AWS Account
AWS CloudFormation AWS S3 Bucket AWS CloudFormation AWS S3 Bucket
cf-templates-a3gjv31ap90h-{Region}
Bucket name:  cf-templates-a3gjv31ap90h-us-east-1 Bucket name:  cf-templates-a3gjv31ap90h-eu-west-2
us-east-1 eu-west-2
#BHUSA @BlackHatEvents

## Slide 21

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
black hat
WHAT IF ...?
The CloudFormation
Bucket Already Exists
```

## Slide 22

**<u>https://onecloudplease.com/blog/s3-bucket-namesquatting</u>**

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 83/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
# One Cloud Please Blog Projects Absit Contoct
S3 Bucket Namesquatting - Abusing predictable S3
bucket names
31 July 2019
```

## Slide 23

AWS Account - Victim
AWS CloudFormation AWS S3 Bucket
Bucket name:  cf-templates-a3gjv31ap90h-us-east-1
us-east-1
AWS Account -Victim AWS Account - Attacker
AWS CloudFormation AWS S3 Bucket
Bucket name:  cf-templates-a3gjv31ap90h-eu-west-2 Bucket name:  cf-templates-a3gjv31ap90h-eu-west-2
eu-west-2 eu-west-2
#BHUSA @BlackHatEvents

## Slide 24

#BHUSA @BlackHatEvents

## Slide 25

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 95/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
black hat
WHAT IF ...?
The Attacker Opens the
Bucket for Public Access
```

## Slide 26

AWS Account -Victim AWS Account - Attacker
AWS CloudFormation AWS S3 Bucket
Bucket name:  cf-templates-a3gjv31ap90h-eu-west-2 Bucket name:  cf-templates-a3gjv31ap90h-eu-west-2
eu-west-2 eu-west-2

#BHUSA @BlackHatEvents

## Slide 27

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 94/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Block public access (bucket settings)
Block all public access
©on
> Individual Block Public Access settings for this bi
Block all public access
A Off
> Individual Block Public Access settings for this bucket
```

## Slide 28

AWS Account -Victim AWS Account - Attacker
AWS CloudFormation AWS S3 Bucket
Bucket name:  cf-templates-a3gjv31ap90h-eu-west-2 Bucket name:  cf-templates-a3gjv31ap90h-eu-west-2
eu-west-2 eu-west-2
#BHUSA @BlackHatEvents

## Slide 29

<u>https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic-cross-account.html</u>

#BHUSA @BlackHatEvents

## Slide 30

## Information Disclosure

AWS Account -Victim AWS Account - Attacker
AWS CloudFormation AWS S3 Bucket
Bucket name:  cf-templates-a3gjv31ap90h-eu-west-2 Bucket name:  cf-templates-a3gjv31ap90h-eu-west-2
eu-west-2 eu-west-2
#BHUSA @BlackHatEvents

## Slide 31

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 95/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
black hat
WHAT IF ...?
The Attacker Modifies
the Template Files?
```

## Slide 32

###### Resource Injection in CloudFormation Templates

<u>https://rhinosecuritylabs.com/aws/cloud-malware-cloudformation-injection/ https://github.com/RhinoSecurityLabs/pacu/wiki/Module-Details#cfn__resource_injection</u>

#BHUSA @BlackHatEvents

## Slide 33

##### CloudFormation: Full Attack Scenario

AWS Account -Victim AWS Account - Attacker
AWS CloudFormation AWS S3 Bucket
2
1 Create Stack Upload Victim Template
7 Submit Stack
User 8 Get Modified Template
Lambda triggered by
3
4 Get Victim Template PutBucketNotification
6 Put Modified Template
9 Create the injected resource
Admin role 5
Resource Injection
eu-west-2 eu-west-2

#BHUSA @BlackHatEvents

## Slide 34

CloudFormation: Full Attack Scenario
AWS Account -Victim AWS Account - Attacker
AWS CloudFormation AWS S3 Bucket
2
1 Create Stack Upload Victim Template
7 Submit Stack
User 8 Get Modified Template
Lambda triggered by
3
4 Get Victim Template PutBucketNotification
6 Put Modified Template
9 Create the injected resource
Admin role 5
Resource Injection
eu-west-2 eu-west-2
#BHUSA @BlackHatEvents

## Slide 35

##### CloudFormation: Important Points

Initiator needs IAM role management permissions to create admin role

Attackers can still modify resources based on the template file

Wait for new stack deployment in a new region

#BHUSA @BlackHatEvents

## Slide 36

PoC

#BHUSA @BlackHatEvents

## Slide 37

##### The Elephant in the Room

#BHUSA @BlackHatEvents

## Slide 38

##### CloudFormation S3 Bucket Hash

**[a-z0-9]{12}** cf-templates-a3gjv31ap90h-us-east-1 Prefix Hash Region

**4,738,381,338,321,616,896**

#BHUSA @BlackHatEvents

## Slide 39

#BHUSA @BlackHatEvents

## Slide 40

##### The Hash

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 87/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
master
Blame
dule CloudFormationTool
f bucket.nil?
name = cf_bucket_name(region)
log "Creating CF template bucket #{name}"
awss3(region) .create_bucket ({
acl private",
bucket: name,
}.merge(if region == 'us-east-1' then {} else { create_bucket_configuration: { location_constraint: region } } end))
awss3(region) .delete_public_access_block({bucket: name})
name
bucket [:name]
end
def cf_bucket_name(region, key = nil)
g rat and. key if one wasn't given
key ||= ((@...12).map { [x'a ,*'@'..'9'] [rand(36)] }.join)
“cf-templates—#{key}—#H{ region}"
end
```

## Slide 41

##### The Hash

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 85/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
def cf_bucket_name(region, key = nil)
# generate random key if one wasn't given
key ||= ((@...12).map { [x'a'..'z',*'®'..'9'] [rand(36)] }.join)
end
```

## Slide 42

The Hash
#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 78/100 on the text kept, 64/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
USA 2024 -
def cf_buck
g enerat
key ||= ( ] }.join)
end
```

## Slide 43

##### Hash Discovery in Open-Source

**~1000**

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 81/100 on the text kept, 56/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Filter by 860 files
Code
Repositories
Issues
Pull requests
Discussions
More
Code Search <% Cody About Sourcegraph
i 278 results in 6.75%
Filter results cme
By type
joning artifact_parameters {
4} Code
Paths
‘Symbols
Commits
Diffs
```

## Slide 44

##### Eureka

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 84/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Eureka
v ™S aws-samples/aws-glue-samples - examples/notebooks/hudi2redshift-incremental-load.ipynb
115
116
117
118
119
120
121
"if 'TempDir' in args:\n",
z temp_dir = args['TempDir']\n",
"if not temp_dir:\n",
" temp_dir = f\"s3://aws-glue-assets-{AWS_ACCOUNT_ID}-{REGION}/temporary/\"\n",
"\n",
“jdbc_conf = glueContext.extract_jdbc_conf(connection_name=REDSHIFT_CONNECTION_NAME) \n"
@ Jupyter Notebook -
PB master
```

## Slide 45

Eureka

**glue-assets-{AccoutId}-{Region}**

#BHUSA @BlackHatEvents

## Slide 46

Eureka
glue-assets-{AccoutId}-{Region}

#BHUSA @BlackHatEvents

## Slide 47

##### Exploring Potential Vulnerabilities

Open-Source

Documentation

Crawling Automation

#BHUSA @BlackHatEvents

## Slide 48

##### TrailShark

#BHUSA @BlackHatEvents

## Slide 49

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 87/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Create stack
Create stack
Prerequisite - Prepare template
Prepare template
© Template is ready Use a sz
Specify template .
azon $3 UR © Upload a template Syne from Git
Jpload a template file
Choose file
© 2024, Amazon Web Services, inc. or its affiliates. Privacy Terms
```

## Slide 50

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 83/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Open
[Users/ofekitach/Downloads/cool_recording.pcapng (16 MB)
[Users/ofekitach/Downloads/male.pcapng (52 MB)
Users/ofekitach/Downloads/create_stack_normal.pcapng (13 MB)
[Users/ofekitach/Downloads/traceeshark-f578e4ea-fccc-4ae6-9f77-cSe8ccf3955e. pcapng (6120 Bytes)
[Users/ofekitach/Downloads/traceeshark-99ae9be4-8146-4232-9677-70101034e186.json (8766 KB)
Users/ofekitach/Downloads/glue_recording.pcapng (101 MB)
[Users/ofekitach/Downloads/canvas.pcapng (213 MB)
[Users/ofekitach/Downloads/service_catalog.pcapng (41 MB)
[Users/ofekitach/Downloads/create_stack_with_app.pcapng (5756 KB)
JUsers/ofekitach/Downloads/aws_apprunner.pcapng (27 MB)
Capture
7
Ethernet Adapter (enS): enS
Ethernet Adapter (en6): en6
Thunderbolt 1: ent
Thunderbolt 2: en2
Thunderbolt 3: en3
Thunderbolt Bridge: bridgeO
Subosen 4K Graphic Docking: en7
gifo
© Cisco remote capture: ciscodump
© TrailShark: cloudtrail
© Random packet generator: randpkt
© SSH remote capture: sshdump
© UDP Listener remote capture: udpdump
© Wi-Fi remote capture: wifidump
Learn
User's Guide - Wiki - Questions and Answers - Mailing Lists - SharkFest -
You are running Wireshark 4.2.3 (v4.
-0-ga15d7331476c). You receive automatic updates.
L fy to load or capture
Wireshark Discord
The Wireshark Network Analyzer
~| + Made By Recorder Derivative Event
Donate
No Packets Profile: trailshark-profile
```

## Slide 51

##### TrailShark

<u>https://github.com/Aqua-Nautilus/TrailShark</u>

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 87/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
TrailShark
CreateUploadBucket [permission Grants permission to upload Write
only] templates to Amazon S3
buckets. Used only by the AWS
CloudFormation console and is
not documented|}n the API
reference
DescribeRegions 69 md/Botocore#1. 34.4
PutBucketEncryption eu-south-1 s3.amazonaws.com cloudformat ion. amazonaws. com
```

## Slide 52

##### Digging for Potential Buckets

#BHUSA @BlackHatEvents

## Slide 53

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 81/100 on the text kept, 69/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
serverless-{AWS:: }-{AWS::
eks-emr-cluster-pod-templates-{AWS: :
dstack-{AWS: : }-{AWS: :
s3-analytics-{AWs:: }-{AWS::
aws-glue-segment-dev-{AWS:
spp-code-{AWS
sra-staging-{AWS
aws-glue-studio-transforms-{AWS: :
aws-waf-logs-{AW:
aws-pca-revocation-crl
terraform-state-{AWs: :
sc-terraform-engine-state-{
aws-glue-scripts-{AWS::
terraform-engine-bootstrap-,
aws-accelerator-central-log|
cdk-hnb659fds-assets-{AWs: :
elasticbeanstalk-{AWs: :
aws-cloudtrail-logs-{AWs: :
aws-athena-query-results-{AWS
aws-controltower-Logs-{AWS: :
aws-emr-studio-{AWS: :
```

## Slide 54

Which services are responsible for these buckets?

Are they exploitable?

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 77/100 on the text kept, 72/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
serverless-{AWS:: }-{AWS
eks-emr-cluster-pod-templates-{AWS
dstack-{AWS: : }-{AWS::
s3-analytics-{AWs:: }-{AWS::
macro-template-default-{AWS
spp-code-{AWS: :
codebuild-{AWS Wh h bl
Sea ieetia icn services are responsipie
aws-pca-revocation-crl
terraform-state-{AWs: :
sc-terraform-engine-state-{
aws-glue-scripts-{AWS: :
terraform-engine-bootstrap
aws-glue-jars-{AWS::
aws-accelerator-central-log| . 2
aws-emr-resources-{AWS:: }-{AWS::
aws-glue-assets-{AWS: }-{AWS::
aws-cloudtrail-Logs-{AWS: :
sagemaker-{AWS: : }-{AWS:
aws-athena-query-results-{AWS:
aws-Logs-{AWS }-{AWS
aws-codestar-{AWS: : }-{AWS::
aws-controltower-logs-{AWS: : }-{AWS: :
```

## Slide 55

Glue

Service Catalog

EMR

SageMaker

CodeStar

## Slide 56

##### Pre-Steps for Exploitation

Create predictable S3 bucket in a new region

Create Lambda to inject Allow public access with malicious code via permissive policy _PutBucketNotification_

#BHUSA @BlackHatEvents

## Slide 57

Glue Vulnerability aws-glue-assets-{AWS::AccountId}-{AWS::Region}

## Slide 58

##### What is AWS Glue?

<u>https://aws.amazon.com/glue/</u>

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 87/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
What is AWS Glue?
ul Amazon f
& Amazon S3 Y AWS Glue Studio & Lata ae Des . Amazon Redshift
Choice of interfaces
gy Amazon Data lakes
DynamoDB
Pa Data warehouses
K=y Amazon RDS Open interfaces support
interactive and
job workloads
Create and load data
into data lakes and
(CF rag on data warehouses
Amazon EC2
Databases AWS Glue AWS Glue for AWS Glue for
for Ray Python Shell Apache Spark
Data integration engines
SaaS Choose a preferred serverless, scalable data
processing engine with automatic scaling
and pay-as-you-go pricing
Data sources
```

## Slide 59

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 85/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Welcome to AWS Glue Visual Script Job details Data quality
Get started by setting up your account and users, cq
Getting started
ETL jobs Script (Locked) info
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedoptions
1
2
3
Job run monitoring AWS Glue x AWS Glue > Jobs 4 from pyspark.context import SparkContext
6
7
8
Notebooks
Data Catalog tables from awsglue.job import Job
from awsglue.context import GlueContext
AWS Glue Studio ino
Data connections Getting started ## @params: [JOB_NAME]
Workflows (orchestration) ETL jobs 9 args = getResolvedOptions(sys.argv, ['JOB_NAME'])
Visual ETL 10
> Data Catalog NatabooRs 11 sc = SparkContext() |
_ 12 glueContext = GlueContext(sc)
> Data Integration and ETL Job run monitoring _ Glue 4 13 spark = glueContext.spark_session
14 job = Job(gluecontext)
9 15 job.init(args['JOB_NAME'], args)
>» Legacy pages
Data connections 16 job.commit()
Workflows (orchestration) Visual Script Job details wee eee 7 we eres eee ee
> Data Catalog ¥ Advanced properties
Script filename
script.py
Q s3 /Jaws-glue-assets-123456789123-us-west-2}scripts/ x | View Z% | | Browse $3
```

## Slide 60

Glue: Full Attack Scenario
AWS Account -Victim AWS Account - Attacker
AWS Glue AWS S3 Bucket
2
1 Create job Create Glue Python script
7
Run job 8
User Get Modified Glue Python script
Lambda triggered by
3
4 Get Victim script PutBucketNotification
6 Put Modified script
9 Run the injected Python script
Remote Code Execution
5 Modify Glue Python script
eu-west-2 eu-west-2

#BHUSA @BlackHatEvents

## Slide 61

##### Glue Service Role

<u>https://docs.aws.amazon.com/glue/latest/dg/set-up-iam.html</u>

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 83/100 on the text kept, 56/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Glue Service Role
Basic properties info { {
Name
Untitled job
Description - optional eiere
jons can be up to 2048 characters Lom “BC2:
tribute",
permissionse@® = Q
GENERAL GENERAL / MANAGED POLICIES | AWSGLUESERVICEROLE “cloudwatch:PutMetricbata™
AWSGlueServiceRole
```

## Slide 62

##### Invisible Backdoor

###### What the victim sees

###### What is run

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 87/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Invisible Backdoor
What the victim sees
simple-etl
Visual Script Job details Runs Data quality - updated Schedules Version Control
Script (Locked) into
1 import sys
2 from awsglue.transforms import *
3 from awsglue.utils import getResolvedOptions
4 from pyspark.context import SparkContext
5 from awsglue.context import GlueContext
6
7
8
from awsglue. job import Job
args = getResolvedOptions(sys.argv, ["JOB_NAME"])
9 sc = SparkContext()
10 glueContext = GlueContext(sc)
11 spark = glueContext.spark_session
12 job = Job(glueContext)
13 job.init(args["JO8_NAME"], args)
1S # Script generated for node Amazon S3
16 AmazonS3_node170791870445@ = glueContext.create_dynamic_frame.from_options(
17 format_options={"multiline": False},
18 connection_type="s3",
19 format="json",
20 connection_options={"paths": ["s3://test-glue-bucket-shaa"], “recurse":
21 transformation_ctx="AmazonS3_node1707918704450",
23
What is run
v
Log events
You can use the filter bar below to search for and match terms, phrases, or values in your log events. Learn more about filter patterns (4
Q Fitter event Cleat
> Timestamp Message
No oldegayvents at this moment. fi
6:05:58.151+02:00
No newer events at this moment. Auto retry paused. R
```

## Slide 63

Video

#BHUSA @BlackHatEvents

## Slide 64

EMR Vulnerability aws-emr-studio-{AWS::AccountId}-{AWS::Region}

## Slide 65

##### What is AWS EMR?

<u>https://aws.amazon.com/emr/</u>

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 87/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
What is AWS EMR?
Amazon
SageMaker Studio
ce Amazon EC2
& ©
Amazon EMR
Studio
Gy Amazon EKS ofp
58 Amazon MWAA
AWS Outposts
Amazon EMR a
Easily run and scale Apache siacaste ble Gacy Servertess
Spark, Hive, Presto, and other Self-managed
big dels worlicnds data framework tools
and version Run applications built
using open source Develop, run, visualize, and
frameworks on EC2, EKS, debug data pipelines,
Outposts, or completely analytics, and data science
serverless applications, SQL queries,
and ML workloads using
familiar tools
```

## Slide 66

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 90/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
aws
Amazon EMR x Am
> EMR Studio: Getting Started
Getting started
EMR Studio setup
v EMR on EC2 Set up EMR Studios to help your team c isualize, and debug dat.
ster tem
Notebooks and Git repos
Events
Step 1 (optional) Create a Studio ino
v EMR on EKS AWS Service Catalog Info
Virtual clusters
Setup options info
Create cluster templates using AWS Service Catalog. Studio users:
EMR clusters for a Studio. Then the help panel content will include
v EMR Studio they're used in EMR Studio. © Interactive workloads Batch jobs | | Custom
Galting Started [AWS Service Catalog [7
udios
Workspaces (Notebooks) Studio settings info Edit |
o name
Studio_3
S3 lo 1 for Work
ce storage
We'll create a new bucket and use the location s3:] /aws-emr-studio-1 23456789123-us-east-1/]721 566132875.
Studio acc
Ss your AWS resources
We'll create a new service role named AmazonEMRStudio_ServiceRole_1721566132875.
```

## Slide 67

EMR: Full Attack Scenario
AWS Account -Victim AWS Account - Attacker
AWS EMR AWS S3 Bucket
1 Create a Studio 2 Create Jupyter notebook
7
User 8 Get Modified Jupyter notebook
Lambda triggered by
3
4 Get Victim script PutBucketNotification
6 Put Modified script
9 Redirect the user to the malicious site
5 Modify Jupyter notebook
eu-west-2 eu-west-2

#BHUSA @BlackHatEvents

## Slide 68

EMR: Full Attack Scenario
AWS Account -Victim AWS Account - Attacker
AWS EMR AWS S3 Bucket
1 Create a Studio 2 Create Jupyter notebook
7
User 8 Get Modified Jupyter notebook
Lambda triggered by
3
4 Get Victim script PutBucketNotification
6 Put Modified script
9 Redirect the user to the malicious site
5 Modify Jupyter notebook
eu-west-2 eu-west-2
#BHUSA @BlackHatEvents

## Slide 69

##### EMR: Full Attack Scenario

AWS Account -Victim AWS Account - Attacker
AWS EMR AWS S3 Bucket
1 Create a Studio 2 Create Jupyter notebook
7
User 8 Get Modified Jupyter notebook
Lambda triggered by
3
4 Get Victim script PutBucketNotification
6 Put Modified script
9 Redirect the user to the malicious site
5 Modify Jupyter notebook
eu-west-2 eu-west-2

#BHUSA @BlackHatEvents

## Slide 70

##### EMR: Disclaimer

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 90/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
EMR: Disclaimer
® Failed to create Studio. The AWS Access Key Id you provided does not exist In our records. (Service: AWSEditors; Status Code:
400; Error Code: InvalidRequestException; Request ID: f2feScOc-4e85-454.
Amazon EMR > EM
> Create Studio
Create a Studio w.
Setup options toro
© interactive workloads Batch jobs
Studio settings into
Studio name
'8-De98ab80d069; Proxy: null)
Custom
Reset to default
```

## Slide 71

##### Two Ways to Continue

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 92/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Two Ways to Continue
Service role to let Studio access your AWS resources
We'll create a new service role named AmazonEMRStudio_ServiceRole_1721568479152
We'll create a new bucket and use the location s3://aws-emr-studio-779593258376-us-east-1/1721568479152.
Encrypt Workspace files with your own AWS KMS key
Service role to let Studio access your AWS resources
Create a service role
{ Copy
© Choose an existing service role Version"; "2012-10-17
Service role :
jon det Effect": "Allow
Action”: [
"s3:PutObject’
"s3:DeleteObject”
"Resource": [
"arncaws:s3:::aws-emr-studio:
east-1/""
```

## Slide 72

Video

#BHUSA @BlackHatEvents

## Slide 73

## SageMaker Vulnerability sagemaker-{AWS::Region}-{AWS::AccountId}

## Slide 74

<u>https://aws.amazon.com/sagemaker/</u> #BHUSA @BlackHatEvents


> Recovered by OCR — confidence 83/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Amazon SageMaker
Build, train, and deploy machine learning (ML) models for any use case
with fully managed infrastructure, tools, and workflows
why SageMaker?
SageMaker Canvas
Generate accurate machine learning predictions — no code
required
* Accelerate your a - oe ~
Amazoa = productivity using
generative Al = -- =
with fully manage o a- 2
= productivity using = =
oo —
i Canvas
Canvas configuration
Canvas storage configuration
on $3 artifac
s3://sagemaker-us-west-2-123456789123
```

## Slide 75

##### SageMaker: Full Attack Scenario

AWS Account -Victim AWS Account - Attacker
Data
AWS SageMaker AWS S3 Bucket
Leakage
1 Open Canvas 3 Upload Dataset 4 Get Dataset
Create Dataset/
User 2 6 Get Manipulated Dataset
Upload files 5 Manipulated  Attacker
Dataset
Data Manipulation
eu-west-2 eu-west-2

#BHUSA @BlackHatEvents

## Slide 76

### Service Catalog Vulnerability cf-templates-{Hash}-{AWS::Region}

## Slide 77

##### What is AWS Service Catalog?

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 91/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
What is AWS Service Catalog?
| Version details info
AWS CloudFormation
Vulnerability
```

## Slide 78

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 88/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
AWS Account - Victim AWS Account - Attacker
AWS Service Catalog
©) Upload Vic
tim Template
>
AWS S3 Bucket
Create Portfolio
©) and Products
Users
© (create the injected resource }
Admin role that can be assumed by attacker
Get Modif.
@
©
)
‘ied Tempalte
Get Victim Template © Lambda triggered by
PutBucketNotification
Put Modified Template
© Resource Injection
BackdooredIAMRole:
Type: 'AWS::
Propertie
Version: '2012-10-17
Statement:
- Effect: 'Allow'
Principal:
AWS: ‘arn:aws:iam::<Attacker_ID>:root'
Action: 'sts:AssumeRole'
Policies:
- PolicyName: 'default'
PolicyDocumen
Version: '2012-10-17'
Statement
"ALLow'
```

## Slide 79

## CodeStar Vulnerability aws-codestar-{AWS::Region}-{AWS::AccountId}

## Slide 80

##### CodeStar: Full Attack Scenario

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 86/100 on the text kept, 68/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
black
ha
AWS Codest-
Creat
4 |
Proj
ject
cr
projects
project
Team
User
Q Goto resource
a Feedback
eu-west
```

## Slide 81

### Shadow Resource in Open Source

## Slide 82

#### Case Studies

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 88/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Case Studies
1. cd to the root directory of the project.
ACCOUNT ID-SAWS REGION] --
1. Run “sam deploy --s3-bucket
HEAD_BUCKET=$(aws s3api head-bucket --bucket ${s3_bucket} 2>&1 || true)
uf [ -z "“$HEAD_BUCKET" ]; then
echo “Already exists
else
aws s3api create-bucket --buct ${s3_bucket} --r C ${REGION}
r on LocationConstraint="${REGION}
bucket: ${s3_bucket}
//$1" > /dev/null 2>&1; then
echo “Creating bucket: $1
o “Could not create bucket $1"
exit 1
Fi
ine
```

## Slide 83

Past Services Affected by Shadow Resources

Athena

<u>https://docs.aws.amazon.com/athena/latest/ug/querying.html</u>

#BHUSA @BlackHatEvents

## Slide 84

Bucket Monopoly

## Slide 85

#BHUSA @BlackHatEvents

## Slide 86

#BHUSA @BlackHatEvents

## Slide 87

#BHUSA @BlackHatEvents

## Slide 88

#BHUSA @BlackHatEvents

## Slide 89

#BHUSA @BlackHatEvents

## Slide 90

##### Bucket Monopoly Step-by-Step

**Identifying** Predictable Bucket Name

**Discovering** the Unique Identifier

**Monopolize** Creating Unclaimed Buckets Across All Regions

#BHUSA @BlackHatEvents

## Slide 91

##### Identifying

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 93/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
blackhat
identifying
ring Potential Vulnerabilities
Open-Source Documentation Crawling Automation
```

## Slide 92

##### Discovering the Unique Identifier

**CloudFormation cf-templates-{Hash}-{AWS::Region}**

###### **Glue**

**aws-glue-assets-{AWS::AccountId}-{AWS::Region}**

#BHUSA @BlackHatEvents

## Slide 93

##### Discovering Account IDs

<u>https://www.youtube.com/watch?v=iMYbne-tD20&t=872s&ab_channel=fwd%3Acloudsec https://medium.com/@TalBeerySec/a-short-note-on-aws-key-id-f88cc4317489 https://github.com/righteousgambit/quiet-riot https://github.com/fwdcloudsec/known_aws_accounts</u> #BHUSA @BlackHatEvents

## Slide 94

##### Monopolize

#BHUSA @BlackHatEvents

## Slide 95

##### Disclosure and Timeline

- **16 February 2024:** Reported vulnerabilities in CloudFormation, Glue, EMR, SageMaker, and CodeStar to AWS. AWS acknowledged and began investigating.

- **18 February 2024:** Reported a vulnerability in ServiceCatalog.

- **16 March 2024:** AWS confirmed fixes for CloudFormation and EMR.

- **25 March 2024:** AWS confirmed fixes for Glue and SageMaker. CodeStar addressed as it's planned for deprecation in July 2024.

- **30 April 2024:** Reported CloudFormation fix leaves users vulnerable to DoS.

- **26 June 2024:** AWS confirmed fixes for ServiceCatalog and CloudFormation.

#BHUSA @BlackHatEvents

## Slide 96

##### Summary and Mitigations

Use _‘aws:ResourceAccount’_ Condition

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 92/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Summary and Mitigations
Use ‘aws:ResourceAccount’
Condition
"Condition": {
"StringEquals": {
}
```

## Slide 97

##### Summary and Mitigations

Use  ‘aws:ResourceAccount’  Verify Expected
Bucket Owner
Condition

#BHUSA @BlackHatEvents

## Slide 98

##### Summary and Mitigations

Use  ‘aws:ResourceAccount’  Verify Expected  Naming S3 Buckets with
Condition  Bucket Owner Unpredictable Identifiers
aws-xyz-123456789123-us-east-1
Prefix Account-ID Region

#BHUSA @BlackHatEvents

## Slide 99

##### Summary and Mitigations

Use  ‘aws:ResourceAccount’
Condition

Verify Expected  Naming S3 Buckets with
Bucket Owner Unpredictable Identifiers

aws-xyz-123456789123-us-east-1-1vc8126
Prefix Account-ID Region Random

#BHUSA @BlackHatEvents

## Slide 100

Do you still believe account ID isn’t a secret?

## Slide 101

# Thank you!

@YakirKad @mike_katch @ofekitach

#BHUSA @BlackHatEvents
