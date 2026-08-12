---
title: "SnowGoat_ Exposing Hidden Security Risks and Leaking Data Like a Threat Actor"
speakers: ["Lior Adar"]
conference: "DEF CON"
conference_full: "DEF CON 33"
edition: "33"
year: 2025
source_pdf: "DEF CON 33 workshops/DEF CON 33 - Workshops - Lior Adar - SnowGoat_ Exposing Hidden Security Risks and Leaking Data Like a Threat Actor - Slides.pptx"
pages: 37
sha256: "82820390b7e0d077a550f1049d927448b204c5381c8e37bea864baa184f4a759"
text_chars: 10672
ocr_pages: 8
has_ocr: true
redacted_secrets: 0
ocr_confidence: 90.7
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T06:33:30Z"
---
# SnowGoat_ Exposing Hidden Security Risks and Leaking Data Like a Threat Actor

**Speakers:** Lior Adar  
**Conference:** DEF CON 33  
**Source:** `DEF CON 33 workshops/DEF CON 33 - Workshops - Lior Adar - SnowGoat_ Exposing Hidden Security Risks and Leaking Data Like a Threat Actor - Slides.pptx` (37 pages)


## Slide 1

**SnowGoat:** Exposing Hidden Security Risks & Leaking Data Like A Threat Actor


> Recovered by OCR — confidence 93/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
# The first Snowflake GOAT #
SnowGoat:
Exposing Hidden Security Risks &
Leaking Data Like A Threat Actor
```

## Slide 2

#### **`$~: whoami` – Lior Adar**

\```
@lior-adar-8902a6129
\```

- + Hacking by day, family & dog walks by night

+ Cloud Security Researcher @ Varonis

- + Ex Palo Alto Networks

- + Living Off The Land Contributor

- + Red Teaming & Research background

**`whoami` – Chen Levy Ben A** **~~roy~~** **<u>`@chenlevyba`</u>** + Cloud Security Research Team Lead @ Varonis

- + Ex Porsche

- + Cat-dad to Vicky the cat

+ Average gamer

## Slide 3

### **Agenda**

###### **Workshop Introduction Snowflake Basics**

**Break**

###### **SnowGoat**

- +Introduction

- +Let the hacking begin!

- +Lessons Learned:

   - + Bypassing Network & Authentication Policies

- +Lessons Learned:

   - + Abusing External Stages for Data Discovery

- +Break

- +Hacking continued

- +Lessons Learned:

   - + Situational Awareness & Abusing Privileged Roles

   - + Masked Data

+Feedback and Q&A

## Slide 4

### **Workshop**

### **Introduction** + **Fully automated environment**

   - + “Plug-and-Play” Terraform script

- + **Prerequisites**

   - + Snowflake account (Free-Tier)

   - + AWS account (Free-Tier)

      - + S3 Provisioned

      - + Free-Tier EC2 Required

   - + Terraform installed

   - + Basic SQL Experience

   - + Run & Gun Spirit!

- + **Includes latest techniques and trends** + **Fun and interactive “CTF”-like attack scenario**

## Slide 5

#### **Snowflake Basics**

- + **What is Snowflake?**

   - + A Modern cloud-based data platform

   - + Supports data warehousing

   - + Scalable to handle large datasets

- + **Key Features** :

   - + Fully cloud-native data warehouse

      - + Structured - Relational DB, Tables, Spreadsheets

      - + Unstructured – JSON (controversial), Images, Text File

   - + Delivered as a SaaS (Software as a Service) solution

   - + Supports Python + standard SQL

   - + Automatically scalable and elastic via Virtual Warehouses

+ Virtually unlimited storage using AWS S3

## Slide 6

**Snowflake Basics**


> Recovered by OCR — confidence 93/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Snowflake Basics
Complete Control Over Your Data
Manage All Your Users Seamlessly
J L Built on SQL Database Technology
A Le Hassle-Free, Fully Managed
Only Pay for What You Actually Use
Real-Time Data Sharing Made Easy
```

## Slide 7

#### **SaaS Security Circles Influence**

**Lack of Visibility into SaaS Usage Zero-Day Stolen Vulnerabilities Credentials IN MY CONTROL Access policy** Be prepared, **Data sharing MFA Regulatory Vendor monitor** and **changes protect** from things **security Data I upload Configuration practice** managed by the **s** cloud service **On/Offboarding Data updatesData breaches** provider, and from **at the** malicious actors **Encryption cloud app Phishing & Social Network Policy Engineering Supply chain attacks Misconfigurations of the cloud provider service**

**OUT OF MY CONTROL Manage** my data content, policy, and **configuration** considering compliance and safety

## Slide 8

#### **Snowflake Basics**

###### **ORGANIZATION**

- +The top-most level of hierarchy in Snowflake

- +Contain multiple Snowflake accounts

###### **ACCOUNT**

- + The highest-level container in Snowflake

- + Housing all objects like databases, users, roles, and warehouses

- +Defines the region, cloud provider, and billing

- +Managed by roles like ACCOUNTADMIN and SECURITYADMIN

## Slide 9

#### **Snowflake Basics**

###### **WAREHOUSE**

- +Virtual compute resources

- +Scalable and elastic—can autoresume

- +Used for executing queries and data processing.

- +Each warehouse operates independently

###### **DATABASE**

- +Logical container for storing schemas, tables, views, and other database objects

- +Each account can have multiple databases for better data organization

- +Acts as a boundary for data and object access

## Slide 10

#### **Snowflake Basics**

**TABLE**

- +Core object that stores structured data in rows and columns

- +Supports various types: permanent, transient, and temporary

- +Can handle both traditional (relational) and semi-structured data (e.g., JSON,

**STAGE**

- +Storage area used for data loading/unloading between Snowflake and external systems

- +Can be internal (within Snowflake) or external (e.g., AWS S3, Azure Blob, Google Cloud Storage)

- +Acts as a holding zone for files before they’re loaded into tables

###### **STORED PROCEDURE**

- +Block of code stored in your Snowflake database.

- +Execute multiple SQL statements and logic in a single call.

- +Stored in the database and schema like other database objects.

XML)

## Slide 11

#### **Snowflake Basics**

**USER**

- + Individual or an application

- + Unique identity (user name)

- +Authenticated with credentials and assigned roles

- +Performs actions like querying, managing data, and objects

**ROLES**

      - + Collection of permissions and permitted actions

      - + Can include other roles (inheritance) (!!)

      - + Attached to users

      - + Snowflake’s **role-based access control (RBAC)** model

- + Classic attributes:

   - + Last login

   - + Has MFA

   - + Email address, etc.

## Slide 12

#### **Snowflake Basics** Access Policies

**NETWORK POLICY**

- + Controls **who can connect** to your account

- + Ip address access lists (Allow/Disallow)

- + Enforce **Zero Trust security**

- + Can be applied at the account level or to specific users

**AUTHENTICATION POLICY**

- + Multi-factor-authentication

- + Client access limitation

- + **Password complexity requirement**

- + Can be applied at the **account level** or to specific **users**

## Slide 13

#### **Snowflake Basics**

###### **MASKING POLICY**

- + Controls how sensitive data is **shown to different users** . + Applied to **specific columns**

- + **Dynamically masks or obfuscates** column data based on who queries it.

## Slide 14

Snowflake Hierarchy
Organization
Account
Other
Warehouse Database Role User
 Account
Objects
Database Role Schema
Other
Table View Stage Stored Procedure UDF
 Schema
Objects

## Slide 15

#### **Snowflake Breach**

Overview of the UNC5537 Snowflake Breach

- + **What Happened**

   - + A financially motivated group, UNC5537, targeted Snowflake customer instances (not Snowflake itself)

   - + Attackers used stolen credentials—often harvested by infostealer malware like RedLine, Raccoon Stealer, and Lumma

   - + Over 165 organizations were potentially impacted

- + **Key Findings**

   - + No evidence of breach in Snowflake’s core platform

   - + Most compromised accounts lacked Multi-Factor Authentication (MFA)

   - + Many credentials had been stolen years earlier and were still valid

## Slide 16

#### **Snowflake Breach: Attack Path**

Illustration by Mandiant/Google


> Recovered by OCR — confidence 93/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Snowflake Breach: Attack Path
Infostealer
Malware
Acquired Snowflake Datab:
& External
Infostealer Logs Storage Recon Exfiltration
UNC5537
Login with Stolen
Snowflake Creds
Snowflake
Customer Instance
Personal Devices
Illustration by Mandiant/Google
```

## Slide 17

Questions?

## Slide 18

## **Break**

15 mins.

## Slide 19

**Let the hacking begin!**

## Slide 20

**What went wrong?**

## Slide 21

**Lessons Learned** Attack path


> Recovered by OCR — confidence 92/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Tacti
Role: UNC5537 Campaign
Tact
Role: UNC5537 Campaign UNC5537 Campaign UNC5537 Campaign
```

## Slide 22

#### **Lessons Learned**

Bypassing Network & Authentication Policies

**NETWORK POLICY**

**BEST PRACTICES**

- + Over permissive Network Policy

   - + Including public addresses

- + Allow connections from trusted networks only

   - + Even when using Private-Links

- + Require MFA on all Snowflake local users

**AUTHENTICATION POLICY**

      - + SSO users will have MFA enforced on SSO side

- + Misconfigured Authentication Policy

   - + No MFA required

- + SnowSQL access only

## Slide 23

**Almost there!**

## Slide 24

**What went wrong?**

## Slide 25

#### **Lessons Learned** Attack path


> Recovered by OCR — confidence 92/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Tacti
Facing an error of Found a valid range because of Access via SNOWSQL
Network Policy of IPs (AWS/Azure) client (CLI) only
Authentication Policy
Role: UNC5537 Campaign
—> Login —
Tacti
Role: UNC5537 Campaign UNC5537 Campaign UNC5537 Campaign
```

## Slide 26

#### **Lessons Learned**

##### Abusing External Stages For Data Recovery

###### **CLASSIFIED DATA**

- + Clear-text passwords and credentials are exposed

###### **PASSWORD REUSE**

- + The user’s password is the same, and unchanged

###### **BEST PRACTICES**

- + Always encrypt passwords and credentials before storing

- + Monitor classified data stored at your cloud providers premises

- + Healthy password management:

   - + Rotate passwords, especially after an exposed backup such as this one

   - + Use different passwords for different services

   - + Usage of complex and long passwords

   - + MFA (!!)

## Slide 27

#### **Lessons Learned** Anomalous Context Switching

###### **CONTEXT SWITCHING**

- + User has logged in as two different user accounts

###### **BEST PRACTICES**

- + Monitor login events and correlate:

   - + Impossible travel (different IPs)

   - + Multiple user-context from the same source

- + Monitor enumeration techniques:

   - + Anomalous amount of configuration reads

   - + Reads from first-time sources

## Slide 28

**Break** 15 mins.


> Recovered by OCR — confidence 91/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Break
15 mins.
REST, YOUMUST.
```

## Slide 29

**Hacking Continued!**

## Slide 30

**What went wrong?**

## Slide 31

#### **Lessons Learned** Attack path


> Recovered by OCR — confidence 92/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Role:
Check Roles &
Privileges
Role:
Login _>
Enumration _
UNC5537 Campaign
Facing an error of
Network Policy
UNC5537 Campaign
Found USAGE
privilege on STAGE
UNC5537 Campaign
Found a valid range
of IPs (AWS/Azure)
Found sensitive data
in STAGE
Sensitive data
Facing an error
because of
Authentication Policy
GET command failed
since its an external
STAGE
IC5537 Campaign
—
Access via SNOWSQL
client (CLI) only
```

## Slide 32

#### **Lessons Learned**

##### Situational Awareness & Abusing Privileged Roles

###### **ENUMERATION**

###### **BEST PRACTICES**

+ Enumeration:

- + Roles

- + Privileges

- + Data

- + Monitor enumeration techniques:

   - + Anomalous amount of configuration reads

   - + Reads from first-time sources

- + Correct identity management

   - + Never (!) assign direct permissions to users

###### **PASSWORD RESET**

- + User is a direct “OWNER” of another privileged

- + Anomalous password reset

   - + Use “USERADMIN” role for user management actions

- + Only “functional” roles should nest other roles

- + Monitor anomalous user management activities

## Slide 33

#### **Lessons Learned**

##### Masked Data

###### **MASKING POLICY**

- + Unmasking data to everyone is an aggressive activity!

###### **BEST PRACTICES**

- + Use masking policies!!

- + Monitor masking policies and masked data:

   - + Unset masking policy to an entire column – exposing the data to whomever has privileges

   - + Anomalous changed and updates to masking policies

## Slide 34

**Summary**

## Slide 35

**Feedback and Q&A**

## Slide 36

**To Be Continued..**


> Recovered by OCR — confidence 79/100 on the text kept, 60/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
# The first Snowflake GOAT # s
é
```

## Slide 37

# **Thank you**

**Lior Adar** ladar@varonis.com **Chen Levy Ben Aroy** clevybenaroy@varonis.c om
