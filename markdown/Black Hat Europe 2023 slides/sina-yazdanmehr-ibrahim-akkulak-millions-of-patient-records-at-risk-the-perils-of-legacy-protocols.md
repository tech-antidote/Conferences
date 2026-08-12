---
title: "Millions of Patient Records at Risk The Perils of Legacy Protocols"
speakers: ["Sina Yazdanmehr", "Ibrahim Akkulak"]
conference: "Black Hat"
conference_full: "Black Hat Europe 2023"
edition: "Europe"
year: 2023
source_pdf: "Black Hat Europe 2023 slides/Sina Yazdanmehr, Ibrahim Akkulak _ Millions of Patient Records at Risk The Perils of Legacy Protocols.pdf"
pages: 35
sha256: "49b4c98343daf727817310424418b44310d1697be904ff6003aa670d4ab14d7d"
text_chars: 19477
ocr_pages: 1
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:13:06Z"
---
# Millions of Patient Records at Risk The Perils of Legacy Protocols

**Speakers:** Sina Yazdanmehr, Ibrahim Akkulak  
**Conference:** Black Hat Europe 2023  
**Source:** `Black Hat Europe 2023 slides/Sina Yazdanmehr, Ibrahim Akkulak _ Millions of Patient Records at Risk The Perils of Legacy Protocols.pdf` (35 pages)

## Slide 1

**Millions of Patient Records at Risk** The Perils of Legacy Protocols Sina Yazdanmehr <sina@aplite.de>

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
aplite
Tailor-made IT Security
Millions of Patient Records at Risk
The Perils of Legacy Protocols
Sina Yazdanmehr <sina@aplite.de>
```

## Slide 2

## **For more than 30 years, DICOM, standard protocol in medical imaging, has been a lifesaver**

2

## Slide 3

**DICOM has become a known source of sensitive data leakage**

2019  1 Millions of Australians’ sensitive medical images, data left openly accessible
2021  2 45 million unique DICOM files stored on over 2,140 servers in 67 countries
2023 How about now?

1. <u>https://itnews.com.au/news/millions-of-australians-sensitive-medical-images-data-left-openly-accessible-531248</u> 2. <u>https://cybelangel.com/stop-medical-device-leaks/</u>

3

## Slide 4

**2023 Update: the leakage is increasing globally**

### **Over 59M patients’ personal and medical records are accessible on the internet**

4

## Slide 5

## **Health sector is embracing new technologies like Cloud while still using legacy protocols**

### The industry is moving towards cloudification

Medical Institution
Modality DICOM viewer
Internet
Cloud-based storage
•
Many medical institutions now use the
Cloud
•
The Cloud-based servers are often publicly
accessible due to lack of knowledge or
misconfiguration

5

## Slide 6

## **This shift forces small business to align their workflows with the new trends**

### The industry is moving towards cloudification

### Small businesses try to adopt the new trend

Medical Institution
Modality DICOM viewer
Internet
Cloud-based storage

Medical Institution
Modality Storage
Internet
DICOM viewer

- Many medical institutions now use the Cloud

- The Cloud-based servers are often publicly accessible due to lack of knowledge or misconfiguration

- Many small medical facilities, like imaging centers, often use on-premises solutions within their networks

- They lack expertise or resources for complex network setups

6

## Slide 7

## **3,806 DICOM servers on the internet – over 73% hosted on the Cloud or exposed via DSL**

The industry is moving towards cloudification
Medical Institution
Modality DICOM viewer
1,196
1,601
Internet
Cloud-based storage
1,009
•
Many medical institutions now use the
DSL Other Cloud
Cloud
•
The Cloud-based servers are often publicly
accessible due to lack of knowledge or
misconfiguration

Small businesses try to adopt the new trend
Medical Institution
Modality Storage
Internet
DICOM viewer

- Many small medical facilities, like imaging centers, often use on-premises solutions within their networks

- They lack expertise or resources for complex network setups

7

## Slide 8

## **We scanned the whole internet for more than six months assessing the exposure**

### 1. Examined the protocol

### 2. Scan

### 3. Enumeration

### 4. Analyze

- Examined DICOM protocol to uncover all possible attacks

- Scanned the whole internet regularly

- • From different locations and networks

- Tested data retrieving methods on the discovered servers

- Removed false positive results

- Removed unrelated results, e.g., honeypots, vet servers, etc.

8

## Slide 9

## **We scanned the whole internet for more than six months assessing the exposure**

### 1. Examined the protocol

### 2. Scan

### 3. Enumeration

### 4. Analyze

- Examined DICOM protocol to uncover all possible attacks

- Scanned the whole internet regularly

- From different locations and networks

- Tested data retrieving methods on the discovered servers

- Removed false positive results

- Removed unrelated results, e.g., honeypots, vet servers, etc.

### **Personal Identifiable (PII)**

### **Protected health (PHI)**

# **16.1 M**

# **43.5 M**

Information like:

- Full name

- Date of birth

- Address

- Telephone number

- Gender

   - Information like:

   - Result of examination

   - Place, date, and time of examination

   - Referring physician

   - Used modality

- In some cases, Social Security Number (SSN)

The permanence of this data amplifies the danger of leakage

9

## Slide 10

## **We scanned the whole internet for more than six months assessing the exposure**

### 1. Examined the protocol

### 2. Scan

### 3. Enumeration

### 4. Analyze

- Examined DICOM protocol to uncover all possible attacks

- Scanned the whole internet regularly

- • From different locations and networks

- Tested data retrieving methods on the discovered servers

- Removed false positive results

- Removed unrelated results, e.g., honeypots, vet servers, etc.

### **Personal Identifiable (PII)**

### **Protected health (PHI)**

43.5 M
Information like:

# **16.1 M**

- Information like: • Full name

   - Result of examination

- Date of birth

   - Place, date, and time of examination

- Address

   - Referring physician

   - • Used modality

- Telephone number

- Gender

- In some cases, Social Security Number (SSN)

The permanence of this data amplifies the danger of leakage

Top 5 countries out of 111 with the most exposure

USA 18.2 M
India 9.6 M
South Africa 7.3 M
Iran 2.9 M
Brazil 2.6 M

Many servers hosted in the USA store data from other countries

10

## Slide 11

## **Agenda**

1| 2| 3|
Introduction  DICOM: Deep dive  Countermeasures
and results of  and attack scenarios and takeaways
the internet-
wide research

11

## Slide 12

## **PACS streamlines management and transmission of medical images**

Picture Archiving and Communication System (PACS) is a medical image system that saves, finds, and shares medical images
and reports
Hospital Information System
HL7 interface
PACS
Modality Workstation
Medical staff
App logic
Modality
Patients
DICOM viewer DICOM interface Storage Database HTTP interface

Modality = Medical imaging device

DICOM

HTTP

HL7

12

## Slide 13

## **DICOM data model is composed of four main Information Entities**

Each Information Entity (IE) represents certain data

### Image

- Individual medical images or data files

- Elements like acquisition and position attributes, image type, instance number, samples per pixel, etc.

13

## Slide 14

## **DICOM data model is composed of four main Information Entities**

Each Information Entity (IE) represents certain data

Image

Series

- Individual medical images or data files

- Elements like acquisition and position attributes, image type, instance number, samples per pixel, etc.

- Group of related images, e.g., a set of MRI scans

- Elements like series’ UID, modality type, series number, etc.

14

## Slide 15

## **DICOM data model is composed of four main Information Entities**

Each Information Entity (IE) represents certain data

### Image

Series

Study

- Individual medical images or data files

- Elements like acquisition and position attributes, image type, instance number, samples per pixel, etc.

- Group of related images, e.g., a set of MRI scans

- Elements like series’ UID, modality type, series number, etc.

- Specific medical examination

- Elements like study ID, date, time, referring physician, study UID, etc.

15

## Slide 16

## **DICOM data model is composed of four main Information Entities**

Each Information Entity (IE) represents certain data

   - Individual medical images or data files

- Image  Individual medical images or data files • Elements like acquisition and position attributes, image type, instance number, samples per pixel, etc.

- Series • Group of related images, e.g., a set of MRI scans • Elements like series’ UID, modality type, series number, etc.

- •

- Study Specific medical examination • Elements like study ID, date, time, referring physician, study UID, etc.

- Patient • An individual patient

   - Elements like acquisition and position attributes, image type, instance number, samples per pixel, etc.

   - Elements like series’ UID, modality type, series number, etc.

   - Elements like study ID, date, time, referring physician, study UID, etc.

   - An individual patient

   - Patient’s information in elements like:

- Identification: full name, patient ID, etc.

- Demographics: age, gender, birthdate, etc.

16

## Slide 17

## **DICOM data model is composed of four main Information Entities**

- Each Information Entity (IE) represents certain data

- Image • Individual medical images or data files • Elements like acquisition and position attributes, image type, instance number, samples per pixel, etc.

- Series • Group of related images, e.g., a set of MRI scans • Elements like series’ UID, modality type, series number, etc.

- •

- Study Specific medical examination • Elements like study ID, date, time, referring physician, study UID, etc.

- Patient • An individual patient

   - An individual patient

   - • Patient’s information in elements like: • Identification: full name, patient ID, etc.

   - • Demographics: age, gender, birthdate, etc.

|Elements are|structured by four attributes||
|---|---|---|
|Attribute|Description|Example|
|Tag|Uniquely defines the element.|(0010,0010)|
|VR|Defines the data type in a 2-char code.|PN (Person Name)|
|Length|Length of the value.|9 bytes|
|Value Field|Actual value|Doe^John|

17

## Slide 18

## **DICOM network protocol is composed of three key steps with different service elements**

Client Server
1 Establish a new association Server may authorize the request based on
client’s Application Entity Title (AET) and/or
IP address
2 Exchange DIMSE messages
Only if server accepts the association
request
3 Release/abort the association

Association Control Service Element (ACSE)

DICOM Message Service Element (DIMSE)

18

## Slide 19

## **DICOM network protocol is composed of three key steps with different service elements**

|**Client**|**Ser**|**ver**|
|---|---|---|
|**1**

Es
|tablish a new association
|Server may authorize the request based on
client’s Application Entity Title (AET) and/or
IP address|
|**2**
**3**
Ex
Re|change DIMSE messages
lease/abort the association|Only if server accepts the association
request|
|**Type**|**Service**|**Security risk**|
|Query and
retrieve|**C-FIND.**Searches for objects
**C-GET.**Fetches objects completely|**Data leakage.**An attacker can use these services
to access patient’s personal and medical data.|
||**C-MOVE.**Moves objects to a server||
|Store|**C-STORE.**Stores objects on server|**Data tampering.**An attacker can tamper existing
series using this service.|

All services are highly prone to Implementation vulnerabilities due to DICOM’s complexity

Association Control Service Element (ACSE)

DICOM Message Service Element (DIMSE)

19

## Slide 20

## **Less than 1% of DICOM servers on the internet use effective authorization**

### Most of DICOM products do not support association- level authorization

- Only AET authorization

- • These servers use the product default AET or a common one

- **758** • Vendors publish default AETs in the DICOM conformance statement, section 4.4.1.1

- **128** Example of section 4.4.1.1

- **2,920** • Unguessable AET and/or IP-based

- **Weak authorization Strong authorization No authorization** authorization

   - Unguessable AET and/or IP-based authorization

20

## Slide 21

**Attackers can use C-FIND, C-GET, and C-MOVE to access patients’ data**

Attacker Server
C-FIND-RQ
C-FIND-RSP
C-GET-RQ
C-STORE-RQ
Target server
C-MOVE-RQ
C-MVOE-RSP
C-STORE-RQ
Many online resources* provide detailed explanation of
these services

*Roni Zaharia –  https://dicomiseasy.blogspot.com/2012/01/dicom-queryretrieve-part-i.html

21

## Slide 22

## **Attackers can use C-FIND, C-GET, and C-MOVE to access patients’ data**

30% of the servers on the internet expose query/retrieve services
Attacker Server A hacker just needs
to find them on the
C-FIND-RQ
internet
C-FIND-RSP
1,159
C-GET-RQ
C-STORE-RQ
Target server
2,647
C-MOVE-RQ
C-MVOE-RSP
C-STORE-RQ
Expose query/retrieve services
Many online resources* provide detailed explanation of
Expose only storage services
these services

*Roni Zaharia –  https://dicomiseasy.blogspot.com/2012/01/dicom-queryretrieve-part-i.html

22

## Slide 23

## **Attackers can tamper existing series using C-STORE**

Modality

**1** Image 1 Image 2

Server

|patientID|studyUID|seriesUID|instanceUID|**number**|•
Modality transfers the
**1**|
|---|---|---|---|---|---|
|P1234|1.3.12.2….|1.3.12.2….|1.3.12.2….|1|images to the SOP|
|P1234|1.3.12.2….|1.3.12.2….|1.3.12.2….|2||

23

## Slide 24

## **Attackers can tamper existing series using C-STORE**

Modality Server
1
Image 1 Image 2
patientID studyUID seriesUID instanceUID number • 1 Modality transfers the
images to the SOP
P1234 1.3.12.2…. 1.3.12.2…. 1.3.12.2…. 1
P1234 1.3.12.2…. 1.3.12.2…. 1.3.12.2…. 2
Attack
Attacker
2 • 2 Retrieve the existing
series

24

## Slide 25

## **Attackers can tamper existing series using C-STORE**

Modality **1** Image 1 Image 2

Server

||patientID|studyUID|seriesUID|instanceUID|**number**|•
Modality transfers the

**1**|
|---|---|---|---|---|---|---|
||P1234
P1234|1.3.12.2….
1.3.12.2….|1.3.12.2….
1.3.12.2….|1.3.12.2….
1.3.12.2….|1
2|images to the SOP
Ak|
|**Image 1.5**||||||•
Retrieve the existing
series
•
Craft new images using
retrieved study and
series information, and
ttac
**2**
**3**|
||patientID|studyUID|seriesUID|instanceUID|**number**|transmit the crafted|
||P1234|1.3.12.2….|1.3.12.2….|1.3.12.2….|1|images using C-STORE|
||P1234
**P1234**|1.3.12.2….
**1.3.12.2….**|1.3.12.2….
**1.3.12.2….**|1.3.12.2….
**1.3.12.2….**|2
**1.5**||

Attacker
2
3

25

## Slide 26

## **Attackers can tamper existing series using C-STORE**

Modality **1** Image 1 Image 2

Server

-Demo-

||patientID|studyUID|seriesUID|instanceUID|**number**|•
Modality transfers the
**1**|
|---|---|---|---|---|---|---|
||P1234|1.3.12.2….|1.3.12.2….|1.3.12.2….|1|images to the SOP|
|Attacker
**2**|P1234|1.3.12.2….|1.3.12.2….|1.3.12.2….|2|•
Retrieve the existing
series
Attack
**2**|
|**Image 1.5**
**3**||||||•
Craft new images using
retrieved study and
series information, and
**3**|
||patientID|studyUID|seriesUID|instanceUID|**number**|transmit the crafted|
||P1234|1.3.12.2….|1.3.12.2….|1.3.12.2….|1|images using C-STORE|
|Medical staff
**4**|**P1234**|**1.3.12.2….**|**1.3.12.2….**|**1.3.12.2….**|**1.5**|•
Legit SCUs will receive
**4**|
||P1234|1.3.12.2….|1.3.12.2….|1.3.12.2….|2|the altered series|
|Image 1
Image 2
**Image 1.5**|||||||

**Attackers can exploit this issue to destroy a series, or introduce false signs of illness**

26

## Slide 27

## **Database injection is one of the most common DICOM’s implementation vulnerabilities**

C-FIND-RQ
(0010,0020) LO 16 1234 ’+and+1=1--
Server
Attacker -Illustrative-
SELECT * FROM tbl_patients
WHERE id LIKE ‘1234 ’+and+1=1-- %’;
SQL Injection vulnerability in  PatientID  exploited by C-FIND

27

## Slide 28

## **Agenda**

1| 2| 3|
Introduction  DICOM: Deep dive  Countermeasures
and results of  and attack scenarios and takeaways
the internet-
wide research

28

## Slide 29

## **Standard organization – effective governance is essential to address these issues at their core**

### **1. Separate versions**

### **2. Enforcement**

### **3. Audit**

- Enable authorization by default in the new version

- Release the new version with mandatory implementation of access control

- Establish a deprecation date (e.g., 2026) to give vendors sufficient time for adopting the change

- • Cease certification of products with the old version after the deadline

- Communicate this change with other relevant organization, such as ISO

- Ensure that checking DICOM security measures is incorporated into their audit checklist

29

## Slide 30

## **Medical institution – DICOM must not be publicly accessible on the internet**

### **Priority 1**

### Exposure

- Prevent public internet access

- Secure the connection between internal network and remotely hosted DICOM server using a secure channel (e.g., IPSec)

- Regularly scan TCP port 104, 11112, and 4242 for exposed assets to detect potential DICOM exposures

30

## Slide 31

## **Medical institution – DICOM must not be publicly accessible on the internet**

### **Priority 1**

- Exposure

- Prevent public internet access

- Secure the connection between internal network and remotely hosted DICOM server using a secure channel (e.g., IPSec)

- Regularly scan TCP port 104, 11112, and 4242 for exposed assets to detect potential DICOM exposures

### **Priority 2**

### Segmentation

- Create a dedicated DICOM segment, isolated from other segments

- • Restrict access to this segment via DICOM protocol to only modalities

- Restrict user access to this segment exclusively through DICOMweb*

- Deploy a WAF for TLS and protect DICOMweb from attacks like database injection

* Use a DICOMweb proxy if the DICOM server does not support it

31

## Slide 32

## **Medical institution – DICOM must not be publicly accessible on the internet**

-

- **Priority 1** Prevent public internet access • Secure the connection between internal network and remotely hosted DICOM server using a secure

- Exposure channel (e.g., IPSec)

   - Regularly scan TCP port 104, 11112, and 4242 for exposed assets to detect potential DICOM exposures

### **Priority 2**

### Segmentation

   - Create a dedicated DICOM segment, isolated from other segments

   - Restrict access to this segment via DICOM protocol to only modalities

   - Restrict user access to this segment exclusively through DICOMweb*

   - Deploy a WAF for TLS and protect DICOMweb from attacks like database injection

-

- **Priority 3** Authorize only modalities’ IP addresses

- If applicable, implement AET authorization with random AETs

- Access control • Integrate DICOMweb with IAM

* Use a DICOMweb proxy if the DICOM server does not support it

32

## Slide 33

## **Medical institution – DICOM must not be publicly accessible on the internet**

-

- **Priority 1** Prevent public internet access • Secure the connection between internal network and remotely hosted DICOM server using a secure

- Exposure channel (e.g., IPSec)

   - Regularly scan TCP port 104, 11112, and 4242 for exposed assets to detect potential DICOM exposures

### **Priority 2** Segmentation

- Create a dedicated DICOM segment, isolated from other segments

- Restrict access to this segment via DICOM protocol to only modalities

- Restrict user access to this segment exclusively through DICOMweb*

- Deploy a WAF for TLS and protect DICOMweb from attacks like database injection

|**Priority 3**|
|---|

- Access control

   - Authorize only modalities’ IP addresses

   - If applicable, implement AET authorization with random AETs

   - • Integrate DICOMweb with IAM

- Remote user access

- Do not enable remote user access if DICOMweb is not integrated with IAM

- • Permit remote access through a firewall:

   - Implement rate limiting

   - Apply regional source IP whitelisting

* Use a DICOMweb proxy if the DICOM server does not support it

33

## Slide 34

## **Vendors and country CERTs – implement security measures, and monitor the exposure**

-

- Vendor Implement AET authorization and _extended negotiation of user identity_ • Disallow new images for an existing series after a set time, e.g., 1 hour from the last submission.

- • Perform regular security tests, and mitigate the uncovered vulnerabilities:

   - Perform fuzzing test. It effectively detects insecure input handlers in a complex DICOM system

   - • Conduct penetration test and code review for more in-depth security.

- Country • Scan the country’s IP ranges regularly to identify DICOM servers CERTs • Identify the IP’s owner, and help them harden their DICOM setup

34

## Slide 35

**Takeaways**

Continued use of legacy protocols, like DICOM, poses ongoing and
1
significant security risks

Millions of patients’ records face internet exposure and unauthorized
2
tampering

Effective governance is essential to address these issues at their core **3**

**Questions?**

## **Thank you!**

Aplite GmbH | Tailor-made IT Security Web: www.aplite.de Email: hi@aplite.de

35
