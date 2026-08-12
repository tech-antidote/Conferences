---
title: "Leveraging Jamf for Red Teaming in Enterprise Environments"
speakers: ["Lance Cain", "Daniel Mayer"]
conference: "Black Hat"
conference_full: "Black Hat USA 2025"
edition: "USA"
year: 2025
source_pdf: "BlackHat_USA_2025_Slides/Lance Cain&Daniel Mayer_Leveraging Jamf for Red Teaming in Enterprise Environments.pdf"
pages: 55
sha256: "48f86d400f90d297c065a9ee23e72941cfb7232ab55268e575da8703596d8f76"
text_chars: 18610
ocr_pages: 7
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T22:57:24Z"
---
# Leveraging Jamf for Red Teaming in Enterprise Environments

**Speakers:** Lance Cain, Daniel Mayer  
**Conference:** Black Hat USA 2025  
**Source:** `BlackHat_USA_2025_Slides/Lance Cain&Daniel Mayer_Leveraging Jamf for Red Teaming in Enterprise Environments.pdf` (55 pages)


## Slide 1

# Leveraging Jamf for Red Teaming in Enterprise Environments

By

Lance Cain and Daniel Mayer

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
~ Jj ~<a
~ \ ~— nes fe - sf ~
YY \ ig Get sc — <A ~
~~ \ & ,
XS $
: s .
TF x
_—— ( — NX
= “a >a, \ »
= 4
WN \ /
gar
‘black hat
FINGS
AUGUST be 2025
MANDALAY BAY / LAS VEGAS
Leveraging Jamf for Red Teaming in
Enterprise Environments
By
Lance Cain and Daniel Mayer
```

## Slide 2

### Lance and Dan

Lance Cain

##### Daniel Mayer

- Service Architect at SpecterOps Inc.

   - Senior Consultant at SpecterOps Inc.

- macOS Security Researcher

   - Ex-Senior Security Researcher at CrowdStrike

- Red Teaming and Pentest Lead

   - Hobbyist free-to-play game cheat maker

- Jamf Exploitation Enthusiast

- Blogs about it and other topics at mayer.cool

#BHUSA @BlackHatEvents

## Slide 3

### Overview

- Introduction

   - Defensive Recommendations

- MacOS in the Modern Enterprise

   - Local vs. Cloud Deployments

- Jamf Management and Permissions

   - Credits and Kudos

- Pros and Cons of Jamf Abuse

      - Questions

   - Tool References

- Privilege Escalation

   - Accounts

   - Api Integrations

- Code Execution

   - Policies and Scripts

   - Policies

   - Computer Extension Attributes

#BHUSA @BlackHatEvents

## Slide 4

### Introduction – MacOS in Modern Enterprises

- macOS is popular with developers, cloud admins, IT engineers, and users with privileged technical access

#BHUSA @BlackHatEvents

## Slide 5

### Introduction – MacOS in Modern Enterprises

- macOS is popular with developers, cloud admins, IT engineers, and users with privileged technical access

- Often macOS devices are initially setup with a Jamf Pro enrollment and integrated with a cloud provider like Azure, then not monitored as much afterwards

#BHUSA @BlackHatEvents

## Slide 6

### Introduction – MacOS in Modern Enterprises

- macOS is popular with developers, cloud admins, IT engineers, and users with privileged technical access

- Often macOS devices are initially setup with a Jamf Pro enrollment and integrated with a cloud provider like Azure, then not monitored as much afterwards

- Sharing some of the most dangerous attack paths we have discovered in client environments regarding Jamf Pro

#BHUSA @BlackHatEvents

## Slide 7

### Introduction – Jamf Management and Permissions

- Many capabilities across Jamf Pro, Jamf Connect, Jamf Protect, Jamf Account:

   - Mobile Device Management (MDM)

   - Software Licensing

   - Device Compliance Checks

   - Initial Provisioning Setups

   - SSO Integrations

   - Device Hardening and Protection

   - More...

#BHUSA @BlackHatEvents

## Slide 8

### Introduction – Jamf Management and Permissions

- Jamf Pro offers a couple different permission assignment interfaces:

   - CRUD access for JSSObjects

   - Allow action for JSSActions

   - Read and Update for JSSSettings

#BHUSA @BlackHatEvents

## Slide 9

### Introduction – Jamf Management and Permissions

- Jamf Pro offers a couple different permission assignment interfaces:

   - CRUD access for JSSObjects

   - Allow action for JSSActions

   - Read and Update for JSSSettings

- Each permission object commonly has an API endpoint : `o` xxx.jamfcloud.com/JSSObjects/computers

#BHUSA @BlackHatEvents

## Slide 10

### Introduction – Jamf Management and Permissions

- Jamf Pro offers a couple different permission assignment interfaces:

   - CRUD access for JSSObjects

   - Allow action for JSSActions

   - Read and Update for JSSSettings

- Each permission object commonly has an API endpoint : `o` xxx.jamfcloud.com/JSSObjects/computers

- With Jamf credentials we leverage API access to:

   - Escalate Privileges

   - Perform Reconaissance

   - Laterally Move to Managed Devices

#BHUSA @BlackHatEvents

## Slide 11

### Introduction – Expectations vs. Reality What Admins Document

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
BRIEFINGS
Introduction — Expectations vs. Reality
What Admins Document
@ REG ) SITE1 jamfContains JVM2
eee
{ep GROUP_ADMINISTRATORS
jamfAdminTo jamfContains jamfScripts
amfPolicies
jamfCreateAccounts JVM1 I
jamfPolicies
jamfUpdateAccounts jamfContains
SOL.JAMFCLOUD.COM
jamfScripts
AZURE_MANAGEMENT_APP.
UPDATE_TEST
jamfAdminTo
jamfContains
jamfPolicies
jamfScripts
LCAIN
SITE2
jamfContains
JVM3
```

## Slide 12

### Introduction – Expectations vs. Reality What Admins Document What We Have Found

What We Have Found

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
black hat
BRIEFINGS
Introduction — Expectations vs. Reality
What Admins Document
What We Have Found
jamfContains JVM2
ee
{ep GROUP_ADMINISTRATORS
jamfAdminTo jamfContains jamfScripts
amfPolicies
jamfCreateAccounts JVM1 I
A jamfPolicies
jamfUpdateAccounts jamfContains
SOL.JAMFCLOUD.COM
jamfScripts
AZURE_MANAGEMENT_APP.
UPDATE_TEST
jamfAdminTo
jamfContains
jamfPolicies
jamfScripts
LCAIN
SITE2
jamfContains
JVM3
@-
jamfMatchedEmail
jamfAZMatchedEmail
sive
jamfAdminTosite
ENROLL jamfContains
LCAIN
jamfContains
jamfContains jamfContains
jamfContains
mfCon
jamfAdminTo jamfContains
jamfCreateAPIRe'
jamfCreateAccounts
jamfUpdateAPiRoles
jamfContains
ateAPiClients
lamfUpdateAccounts
APITEST
jamfadminTo clients
} jamfUpdateAccounts
jamfContains
REG
jamfUpdateAccounts
jamfUpdateAccounts
G) DMAYER
jamfUpdateaPiClients
@) TEST_APLCLIENT
jamfMemberOf
jamfUpdateAPiClients
jamfUp¢ jamfUpdateAccounts
jamfAssignedUser
Jvm3
jamfContains (=)
jamfPolicies
jamfComputerExtensions
jamfScripts
jamfPolicies DAN_TEST
jomtPoticies jamfPolicies
jamfComputerExtensions
jamfComputerExtensions
jamfCont: jamfPolicies
jamfContains jamfPolicies
jamf jamfComputerExtensions
@) emo /2™!jamfPolicies
jamfPolicies
JvMi
JamfUpdateAPiClients fComputerExtensions
jamfContains
jamfComputerExtensions
jamfContains
jamfComputerExtensions
jamfContains
jamfUpdateAccounts
jamfContains
ROUP_EXTENSION
ROUP_ADMINISTRATORS
jamfMemberof
jamfUpdateAccounts
jamfMemberOf ivan
Jvm2
```

## Slide 13

### Introduction – Pros of Jamf Abuse

- Jamf performs multiple administrative actions that EDRs filter to avoid false positives

#BHUSA @BlackHatEvents

## Slide 14

### Introduction – Pros of Jamf Abuse

- Jamf performs multiple administrative actions that EDRs filter to avoid false positives

- • Jamf offers the option to set up self-signing for software deployments

#BHUSA @BlackHatEvents

## Slide 15

### Introduction – Pros of Jamf Abuse

- Jamf performs multiple administrative actions that EDRs filter to avoid false positives

- Jamf offers the option to set up self-signing for software deployments

- Most organizations aren’t monitoring their Jamf environments for change

#BHUSA @BlackHatEvents

## Slide 16

### Introduction – Cons of Jamf Abuse

- If log forwarding is configured, then defenders have a path to follow

#BHUSA @BlackHatEvents

## Slide 17

### Introduction – Tools Eve and JamfHound

• Eve is an open-source python3 postexploitation toolkit that automates many of the attacks we will be discussing and more

#BHUSA @BlackHatEvents

## Slide 18

### Introduction – Tools Eve and JamfHound

• JamfHound is an open-source python3 solution that integrates with BloodHound to visualize attack paths and audit the security of Jamf environments

#BHUSA @BlackHatEvents

## Slide 19

## Privilege Escalation

#BHUSA @BlackHatEvents

## Slide 20

Privilege Escalation – Accounts Jamf Pro Account Creation and Update Edges

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
BRIEFINGS
Privilege Escalation — Accounts
Jamf Pro Account Creation and Update Edges
UPDATE_TEST
jamfUpdateAccounts
eee
q@p GROUP_ADMINISTRATORS
jamfCreateAccounts
SOL.JAMFCLOUD.COM
```

## Slide 21

### Privilege Escalation – Accounts

- JSSObject Permission ‘Create Accounts’ – Allows creating new local Jamf accounts

- JSSObject Permission ‘Update Accounts’ – Allows updating any existing local Jamf accounts

#BHUSA @BlackHatEvents

## Slide 22

### Privilege Escalation – Accounts

- Permissions are scoped to the entire tenant when given to an account or API client

#BHUSA @BlackHatEvents

## Slide 23

### Privilege Escalation – Accounts

- Permissions are scoped to the entire tenant when given to an account or API client

- Create or Update Account permissions are linked with the Jamf Pro Create or Update Group permissions

#BHUSA @BlackHatEvents

## Slide 24

### Privilege Escalation – API Integrations JamfHound Create and Update API Clients and Roles Edges

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
BRIEFINGS
Privilege Escalation — API Integrations
JamfHound Create and Update API Clients and Roles Edges
DEMO
jamfUpdateAPIClients
GROUP_ADMINISTRATORS
jamfUpdateAPIRoles
jamfCreateAPIRoles
jamfCreateAP!Clients
SOL.JAMFCLOUD.COM
```

## Slide 25

### Privilege Escalation – API Integrations

- JSSObject Permission ‘Create API Integrations’ – Allows creating new API clients and retrieving new passwords

- JSSObject Permission ‘Update API Integrations’ – Allows updating any existing clients

- JSSObject Permission ‘Create API Roles’ – Allows creating API client permission sets

- JSSObject Permission ‘Update API Roles’ – Allows updating existing permission sets

#BHUSA @BlackHatEvents

## Slide 26

### Privilege Escalation – API Integrations

- JSSObject Permission ‘Create API Integrations’ – Allows creating new API clients and retrieving new passwords

- JSSObject Permission ‘Update API Integrations’ – Allows updating any existing clients

- JSSObject Permission ‘Create API Roles’ – Allows creating API client permission sets

- JSSObject Permission ‘Update API Roles’ – Allows updating existing permission sets

- **Control of an API Client + Control of API Role Assignments = Jamf Pro Admin**

#BHUSA @BlackHatEvents

## Slide 27

## Code Execution

#BHUSA @BlackHatEvents

## Slide 28

### Code Execution – Recon

- Computer objects contain any information you could ever want about a particular host

   - Real-world information about the user

   - All installed software

   - Hardware information such as storage info

   - All running services

   - What Jamf policies and groups effect it

   - User accounts

   - Much more

#BHUSA @BlackHatEvents

## Slide 29

### Code Execution – Recon

- Computer objects contain any information you could ever want about a particular host

   - Real-world information about the user

   - All installed software

   - Hardware information such as storage info

   - All running services

   - What Jamf policies and groups effect it

   - User accounts

   - Much more

#BHUSA @BlackHatEvents

## Slide 30

### Code Execution – Recon

- Computer objects contain any information you could ever want about a particular host

   - Real-world information about the user

   - All installed software

   - Hardware information such as storage info

   - All running services

   - What Jamf policies and groups effect it

   - User accounts

   - Much more

#BHUSA @BlackHatEvents

## Slide 31

### Code Execution – Recon

- Computer objects contain any information you could ever want about a particular host

   - Real-world information about the user

   - All installed software

   - Hardware information such as storage info

   - All running services

   - What Jamf policies and groups effect it

   - User accounts

   - Much more

#BHUSA @BlackHatEvents

## Slide 32

### Code Execution – Recon

- JSSObject Permission ‘Computers Read’ – Allows reading computer objects

#BHUSA @BlackHatEvents

## Slide 33

### Code Execution – Policies and Scripts JamfHound Policies and Scripts Edges

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
BRIEFINGS
Code Execution —- Policies and Scripts
JamfHound Policies and Scripts Edges
jamfScripts jamfPolicies
AZURE_MANAGEMENT_APP
jamfScripts jamfScripts
jamfPolicies jamfPolicies
JVM3
JVM2
```

## Slide 34

### Code Execution – Policies and Scripts

- Scripts can be bash, perl, python3, or anything else you can shebang (#!)

- Run as root by default

- We have leveraged this capability extensively to execute malicious scripts on macOS

#BHUSA @BlackHatEvents

## Slide 35

### Code Execution – Policies and Scripts

- Scripts can be bash, perl, python3, or anything else you can shebang (#!)

- Run as root by default

- We have leveraged this capability extensively to execute malicious scripts on macOS

#BHUSA @BlackHatEvents

## Slide 36

### Code Execution – Policies and Scripts

- Scripts can be bash, perl, python3, or anything else you can shebang (#!)

- Run as root by default

- We have leveraged this capability extensively to execute malicious scripts on macOS

#BHUSA @BlackHatEvents

## Slide 37

### Code Execution – Policies and Scripts

- Policies are used to handle configuring macOS devices and a major application.

- These can include scripts executed by different trigger events

- You can configure policies to run pre-defined scripts at regular intervals, once per computer, whenever a computer initially joins a Jamf tenant

- You can specify target computers and even specific users of computers

#BHUSA @BlackHatEvents

## Slide 38

### Code Execution – Policies and Scripts

- Policies are used to handle configuring macOS devices and a major application.

- These can include scripts executed by different trigger events

- You can configure policies to run pre-defined scripts at regular intervals, once per computer, whenever a computer initially joins a Jamf tenant

- You can specify target computers and even specific users of computers

#BHUSA @BlackHatEvents

## Slide 39

### Code Execution – Policies and Scripts

- Policies are used to handle configuring macOS devices and a major application.

- These can include scripts executed by different trigger events

- You can configure policies to run pre-defined scripts at regular intervals, once per computer, whenever a computer initially joins a Jamf tenant

- You can specify target computers and even specific users of computers

#BHUSA @BlackHatEvents

## Slide 40

### Code Execution – Policies and Scripts

- Policies are used to handle configuring macOS devices and a major application.

- These can include scripts executed by different trigger events

- You can configure policies to run pre-defined scripts at regular intervals, once per computer, whenever a computer initially joins a Jamf tenant

- You can specify target computers and even specific users of computers

#BHUSA @BlackHatEvents

## Slide 41

### Code Execution – Policies and Scripts

- JSSObject Permission ‘Create Policies’ – Allows creating new management polices

- JSSObject Permission ‘Update Policies’ – Allows updating existing management policies

- JSSObject Permission ‘Create Scripts’ – Allows creating scripts run by policies

- JSSObject Permission ‘Update Scripts’ – Allows updating scripts run by policies

#BHUSA @BlackHatEvents

## Slide 42

### Code Execution – Policies

- Later discovered policies can be used alone to execute commands on managed macOS devices

- Configured via a separate XML tag

- Avoids uploading scripts

#BHUSA @BlackHatEvents

## Slide 43

### Code Execution – Policies

- Later discovered policies can be used alone to execute commands on managed macOS devices

- Configured via a separate XML tag

- Avoids uploading scripts

#BHUSA @BlackHatEvents

## Slide 44

### Code Execution – Policies

- JSSObject Permission ‘Create Policies’ – Allows creating new management polices

- • JSSObject Permission ‘Update Policies’ – Allows updating existing management policies

#BHUSA @BlackHatEvents

## Slide 45

### Code Execution – Policies

• JSSObject Permission ‘Create Policies’ – Allows creating new management polices • JSSObject Permission ‘Update Policies’ – Allows updating existing management policies

#BHUSA @BlackHatEvents

## Slide 46

#### Code Execution – Computer Extension Attributes JamfHound Computer Extension Edges

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
BRIEFINGS
Code Execution - Computer Extension Attributes
JamfHound Computer Extension Edges
@-
jamfComputerExtensions
@-
jamfComputerExtensions jamfComputerExtension
JVM2
```

## Slide 47

#### Code Execution – Computer Extension Attributes

- Used for populating custom information in the Jamf Pro interface

- Allows supplying scripts to generate data

- Runs whenever ‘jamf recon’ is executed, by default once every 24 hours

- Applied to **all** Jamf controlled macOS devices, filtering must be done in the script

#BHUSA @BlackHatEvents

## Slide 48

#### Code Execution – Computer Extension Attributes

- Used for populating custom information in the Jamf Pro interface

- Allows supplying scripts to generate data

- Runs whenever ‘jamf recon’ is executed, by default once every 24 hours

- Applied to **all** Jamf controlled macOS devices, filtering must be done in the script

#BHUSA @BlackHatEvents

## Slide 49

#### Code Execution – Computer Extension Attributes

- Used for populating custom information in the Jamf Pro interface

- Allows supplying scripts to generate data

- Runs whenever ‘jamf recon’ is executed, by default once every 24 hours

- Applied to **all** Jamf controlled macOS devices, filtering must be done in the script

#BHUSA @BlackHatEvents

## Slide 50

#### Code Execution – Computer Extension Attributes

- JSSObject Permission ‘Create Computer Extension Attributes’ – Allows creating new Computer Extension Attribute objects

- JSSObject Permission ‘Update Computer Extension Attributes’ – Allows updating existing Computer Extension Attributes

#BHUSA @BlackHatEvents

## Slide 51

## Defensive Recommendations

#BHUSA @BlackHatEvents

## Slide 52

## Defensive Recommendations

- JSS access and Tomcat access logs can be used to monitor for API access

- Change Management logs are generated on modifications to Jamf objects, but do not show the delta

- API Credentials can be time-gated to small timespans and created just-in-time

- Firewalls can be configured to allowlist access to API endpoints

##### **Cloud Caveats:**

- If you are a cloud customer, support will engage their internal IR team to investigate logs you do not have access to

   - There is also a paid log forwarding service for JSS access and Change Management logs

- If you are a cloud customer, you can also request allowlisting for API endpoints

#BHUSA @BlackHatEvents

## Slide 53

## Credits and Recognitions

##### • Defensive Recommendations

- Jamf Team Members for collaborating and providing best practice recommendations and answering questions

   - Dino Minutolo

   - Adam Rozmus

   - Chris McMacken

   - Michael Paul

##### • JamfHound

- Craig Wright, JD Crandell, West Shepherd for helping implement the v0.0.1 of JamfHound to demonstrate the POC

- Elad Shamir and the SpecterOps Research Team for helping shape the tool for use with OpenGraph

- Thank you to SpecterOps clients and partners that tested JamfHound enterprise collection via early access

#BHUSA @BlackHatEvents

## Slide 54

## Questions?

- … What's a Jamf?

- Where Are the Links to Eve and JamfHound?

   - Eve - https://github.com/RobotOperator/Eve

   - JamfHound - https://github.com/SpecterOps/JamfHound

#BHUSA @BlackHatEvents

## Slide 55

## Black Hat Sound Bytes

1. Compromised Jamf principals can lead to privilege escalation and undetected code execution in multiple ways – this can be tested with Eve

2. Organizations need to monitor changes across their Jamf tenant to detect compromise – configure local and cloud logging

3. Organizations should regularly audit permissions of their Jamf accounts, groups, and API clients – JamfHound can help

#BHUSA @BlackHatEvents
