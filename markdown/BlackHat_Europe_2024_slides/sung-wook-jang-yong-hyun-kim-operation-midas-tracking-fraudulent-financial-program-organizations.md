---
title: "Operation MIDAS - Tracking Fraudulent Financial Program Organizations"
speakers: ["Sung-Wook Jang", "Yong-Hyun Kim"]
conference: "Black Hat"
conference_full: "Black Hat Europe 2024"
edition: "Europe"
year: 2024
source_pdf: "BlackHat_Europe_2024_slides/Sung-Wook Jang & Yong-Hyun Kim_Operation MIDAS - Tracking Fraudulent Financial Program Organizations.pdf"
pages: 44
sha256: "afe18fd2352e2be8c12e4cf3e26ce4b5b8b9bbf29b805bfdd50bac06bdc461a1"
text_chars: 18465
ocr_pages: 2
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:52:25Z"
---
# Operation MIDAS - Tracking Fraudulent Financial Program Organizations

**Speakers:** Sung-Wook Jang, Yong-Hyun Kim  
**Conference:** Black Hat Europe 2024  
**Source:** `BlackHat_Europe_2024_slides/Sung-Wook Jang & Yong-Hyun Kim_Operation MIDAS - Tracking Fraudulent Financial Program Organizations.pdf` (44 pages)

## Slide 1

### **Operation MIDAS Tracking Fraudulent Financial Program Organizations**

**Financial Security Institute Sung-Wook Jang Yong-Hyun Kim (@copy_and_paster)**

Information Classification: General

**#BHEU   @BlackHatEvents #BHEU  @BlackHatEvents**

## Slide 2

###### **About us**

- ➔ **Sung-Wook, Jang :** Senior, Financial Security Institute(FSI)

   - 6 years of CTI, DFIR, Malware analysis

- ➔ **Yong-Hyun, Kim :** Principal, Financial Security Institute(FSI)

   - 8 years of SOC & CTI & DFIR, 4 years of DAST SW Developer

   - Past presentations

      - FS-ISAC 2023 APAC : Building CTI Service from 2B NIDS events over 8 years

      - ISCR 2019(KNPA) - Fight Against Cybercrime : GANDCRAB Threat Groups

**#BHEU  @BlackHatEvents**

Information Classification: General

## Slide 3

###### **Background**

- ➔ **Fake Trading System Scam**

   - A Cybercrime that impersonates an investment professional to trick and defraud people into using a fake trading system*

      - HTS(Home Trading System), MTS(Mobile Trading System)

   - In Korea, there are many cases that impersonates existing financial companies

- ➔ **Terms in this presentation**

   - Supplier : An organization that develops and distributes fake HTS

   - Affiliate : An organization that uses fake HTS to commit fraud (there are several groups)

   - 3rd party service : Legitimate & Not Legitimate Services

      - (e.g, Youtube, Money Launderers, Messenger Service, …)

Supplier

📊

…

**Affiliate,#1 Affiliate,#n**

📞

✉

📺

💸

**Victims**

**#BHEU  @BlackHatEvents**

Information Classification: General

## Slide 4

###### **Initial Findings(1/2)**

- ➔ **Monitoring social media threat information**

   - A tweet found about fake HTS threat information on Twitter(@r3dbU7z, '22.10)

   - a lot of screenshot files were being exposed from a specific port

      - not only were victims being exposed, but also screenshots of the criminals!

* https://x.com/r3dbU7z/status/1579235837833011201 Information Classification: General

#BHEU  @BlackHatEvents

## Slide 5

###### **Initial Findings(2/2)**

본부장 = General Manager
모의서버 = Demonstration Server
➔ Victims? or Criminals?
◆ Title bar on Trading SW
●
'General Manager' keyword
Don't chat while
● Multiple Execution of HTS leading. please be
'concentrated'!
◆ Scam messages in chat room #wait
#sell
●
sent from current computer
◆ Suspicious Management SW #sell
#wait
#buy
Scam messages
(156 audience)

* https://www.youtube.com/watch?v=Zhnf9CNVb-A

**#BHEU  @BlackHatEvents**

Information Classification: General

## Slide 6

1. Leaked screenshots by directory

#### **OPSEC Failures**

   - indexing

2. Lack of device isolation

3. Insecure software development

   - process

**#BHEU  @BlackHatEvents**

Information Classification: General

## Slide 7

###### **#1 : Leaked screenshots by directory indexing**

- ➔ **Leaked Screenshots by directory listing, including developer's screenshot** ◆ Most of them were screenshots of the victim, but a few were of the supplier.

● /YYYYMMDD/{USER_NUMBER}/{USER_NUMBER}-YYYYMMDD-{RANDOM}.jpg

Server management using mRemoteNG (Supplier's screenshot) **#BHEU  @BlackHatEvents**

Directory Listing page

Information Classification: General

## Slide 8

###### **#2 : Lack of device isolation(1/2)**

- ➔ **No separation between crime / personal device**

   - Not only the victims' screens were recorded, but also the criminals' screens

You'll need to verify your identity to sign up. Identity verification Process **(HMAC-SHA Hashed value using SSN with Password)** wEi9oYSuekQGxT9MV4rKHG4CO+Zrp+onhLIIuembI8jx/0PLF5Ne3oM BxvUFlN4UmsgjeNErZfmpCVUFHsv8nq==...

**#BHEU  @BlackHatEvents**

Information Classification: General

## Slide 9

###### **#2 : Lack of device isolation(2/2)**

- ➔ **No separation between crime / personal device**

   - Not only the victims' screens were recorded, but also the criminals' screens

Location exposure in food delivery ordering

Identified car license plate, face of affiliate members by wallpaper

**#BHEU  @BlackHatEvents**

Information Classification: General

## Slide 10

###### **#3 : Insecure software development process(1/2)**

- ➔ **Insecure software development and testing**

Screenshot of Supplier uploaded during development

RDP/RDBMS credentials

**#BHEU  @BlackHatEvents**

Information Classification: General

## Slide 11

1. Screenshot Collection & Triage

#### **Tracking Criminals**

2. Deep-dive analysis of screenshots

3. Correlation analysis of

infrastructure

Information Classification: General

**#BHEU  @BlackHatEvents**

## Slide 12

###### **Collection & Triage of Screenshots(1/2)**

- ➔ **Collection of Screenshots**

   - Automatically collect screenshots from fake HTS servers

      - Collect each server as a separate process & single thread to minimizing server load

   - Analytics identified 170+ fake HTS servers, collected 24/7 for nearly 2 months

      - Collected 12 TB of screenshots(Total 2.7million files, 200GB per day)

multiple
single  single
threads
thread thread
Server … Server Server … Server
#1 #170 #1 #170

Example of unsafe collection

Example of safe collection

**#BHEU  @BlackHatEvents**

Information Classification: General

## Slide 13

###### **Collection & Triage of Screenshots(2/2)**

- ➔ **Triage for 12TB of screenshot files**

   - High-profile screenshot triage using template matching script

      - Development Tools(VSCode, Jetbrains IDE, …), VPN(ExpressVPN…), Mirroid

   - Skip analyzing victim screenshots with user numbering patterns

      - 0 & n < 0 : Supplier(Boss / Fake HTS Developer / Helpdesk, …) / Affiliates

      - n > 1000 : Victims

Information Classification: General

Template Matching

**#BHEU  @BlackHatEvents**

## Slide 14

###### **Deep-dive analysis of screenshots(1/2)**

- ➔ **Development environment of Supplier(Developer)**

   - Typically, Supplier test their new feature using a publicly accessible testing server

   - We have identified valuable information, including the supplier’s identity,

      - development environment, and infrastructure through their screenshots

it's a test program. do not deposit funds into account!!! telegram @htsbest

Testing & Preview Server of Supplier

Development environment of Supplier (C#, Jetbrains IDEs, ChatGPT, NordVPN, …) **#BHEU  @BlackHatEvents**

Information Classification: General

## Slide 15

###### **Deep-dive analysis of screenshots(2/2)**

###### ➔ **Technical stacks of suppliers**

**#BHEU  @BlackHatEvents**

Information Classification: General

## Slide 16

###### **Correlation analysis of infrastructure**

- ➔ **Find another Fake HTS Server using Intelligence Services**

   - Use Censys Search to search for hosts with the same Software + same port criteria Installer Deployment Port

services.software.product=`FileZilla Server` and (services.port:4000 and services.port:2127 and services.port:80 and services.port:89) TradingView Chart Automatic Update Port MTS Web Page Installer Deployment Port Port

Automatic Update Port MTS Web Page Installer Deployment Port

- Track & Analyze Passive DNS History using Virustotal

   - useful for tracking server reuse, rebranding and grouping same affiliate

'Turtleship' Affiliate Group

'Union' Affiliate Group

#BHEU  @BlackHatEvents

Information Classification: General

## Slide 17

###### **Correlation analysis of infrastructure**

- ➔ **Tracking known(and newly registered) domains and IP address of backend** ◆ Fake HTS are constantly being created, renamed, and shut down (dormant)

   - We have monitored activation of Fake HTS domain, Screenshots, Icons, Backend IP

   - Sometimes, Supplier forgot to apply Cloudflare CDN and leaks real IP address

Information Classification: General

**#BHEU  @BlackHatEvents**

## Slide 18

###### **Correlation analysis of infrastructure**

- ➔ **Business License Number from Codesign Certificate**

   - License number can be identified from the code sign certificate

   - Use code sign certificates issued in the name of an auto parts company,

###### architecture firm, or IT parts vendor

**#BHEU  @BlackHatEvents**

Information Classification: General

## Slide 19

###### **Correlation analysis of infrastructure**

- ➔ **Lack of applying Domain Privacy Protection Service**

   - Some domains are not protected by domain privacy protection services

   - It was useful in identifying potential helpers(or supplier) for this campaign

d-brg[.]com smilemts[.]com smileasset[.]top benest[.]top Registrant Name: Jong*** Kim Registrant Organization: **j***** motors** Registrant Street: ***-5-*** 13, *******-ro ***beon-gil, ***-gu, Incheon Registrant City: ***-gu Registrant State/Province: Incheon Registrant Postal Code: 22*** Registrant Country: KR Registrant Phone: +82.1048****13 Registrant Email: **htsman@protonmail.com**

**#BHEU  @BlackHatEvents**

Information Classification: General

## Slide 20

1. Fake HTS Scam Process Overview

##### **Analyze fraud schemes**

2. Schemes of Supplier

3. Schemes of Affiliate

**#BHEU  @BlackHatEvents**

Information Classification: General

## Slide 21

###### **Process overview**

Deploy*
Server%Deploy%&% Market*Price*
Troubleshooting
Supplier( Data
Group
(1'Group) Tech$Support Boss$of$ Programmer
(Helpdesk) Supplier Fake$HTS/MTS Market$Price$
Ad'
Consignment Backend$Srv. Collection$Srv.
Pay'fee'to'rent'
Broker
Fake'HTS'Program
(up'to'3'groups'
estimated) Issue'&'Technical'support,'
providing'operational'informations Broker
Advertise
Laundering*&*Acquisition*of*defrauded*funds Using'a'fake'HTS/MTS
(Information'Leakages)
Affiliate( Operating'HTS/MTS
Boss$of$Affiliate Obtain'market'
Groups price'information'
(up'to'20'groups' using'API
estimated)
Youtube'broadcasting
…
Monetary*
Management Operator$#1 Operator$#n Partner
(Victim$baiter)
3rd(Party( Watch*&*Join
Services Mule$Account$/$ Instigates'to'investment(Leading)
API$Server$of$
Virtual$Account
Legitimate$
Lure'using'SMS/Phone'call'
brokerage$
Victims
firms
Deposit(money(into(Affiliate's(Account((Monetary(Damage)
Information Classification: General Victim #BHEU  @BlackHatEvents

Information Classification: General

## Slide 22

###### **[Supplier] Building Infrastructure(1/2)**

- ➔ **Uses Co-location Server in South Korea & Japan**

   - To collect market price information with low-latency, they uses nearest datacenter

   - After the KNPA arrests some affiliate, supplier moved their servers to japan('2023.5) (2023-05) KNPA arrests an affiliate group

Jan. 2023 2023-01-22

* https://www.yna.co.kr/view/AKR20230503039451060 2023-05-03 2023-05-06

Arrest of a worker who operated a leading room with fake HTS... Damage estimated at 300 billion won*

* 200 million dollars May. 2023-05-29 2023-05-30 2023.

🇰🇷 1.255.42.79 AS9318(SK Broadband Co Ltd)

🇺🇸 172.65.221.109 🇯🇵 89.187.160.194 🇯🇵 101.102.222.78 AS13335(CLOUDFLARENET) AS60068(Datacamp Limited) AS17676(SoftBank Corp.) (Cloudflare CDN)

Passive DNS History of Fake HTS Domain 'unionmts[.]com'

**#BHEU  @BlackHatEvents**

Information Classification: General

## Slide 23

###### **[Supplier] Building Infrastructure(2/2)**

###### ➔ **Advertise their fake hts softwares using internet forums and websites**

Foreign Futures HTS Headquarters Direct HTS Leasing and
Development
Foreign Futures HTS, MTS Leasing
Contact Telegram @htsman
1. Directly under the HTS
development team of a securities
company
2. Fast and bug-free system utilizing
the latest development tools
[...snip…]

**#BHEU  @BlackHatEvents**

Information Classification: General

## Slide 24

###### **[Affiliates] Lure victims using 3rd party platform(1/3)**

- ➔ **Management scam team to operate fake trading system campaign**

   - Pay a fee to obtain the fake hts usage rights : 7,500,000 KRW($5,300) / Month

money  Fake HTS  Virtual  Blog(advertisement) fee Meal
laundering  Rental fee Account  DB(phone number list) fee allowance
fee ($5,300/M) fee SMS(Text message) fee ($2,600/M)

Ledger of affiliate from screenshot

**#BHEU  @BlackHatEvents**

Information Classification: General

## Slide 25

###### **[Affiliates] Lure victims using 3rd party platform(2/3)**

➔ **Lure victims to use fake HTS through text messages, calls and YouTube** ◆ **(Spam Call & Text)** Purchase a list of phone numbers list(DB) and send random calls or text message

DB(Phone number list) and advertising using phone calls

[Advertisement Script] Hello, we are 'EZ securities'! I'd like to put in some stock informations and some short-term stuff. Would you like to take a look at it?

Record the call recipient's reaction 'ㅂㅈ' = missed

**#BHEU  @BlackHatEvents**

Information Classification: General

## Slide 26

###### **[Affiliates] Lure victims using 3rd party platform(3/3)**

- ➔ **Lure victims to use fake HTS through text messages, calls and YouTube** ◆ **(Youtube)** Some affiliates take over ownership of Youtube accounts with a large number of subscribers and utilize them for advertising purposes

**<u>Download link for Fake HTS Program</u>**

Gaps in YouTube video uploads and changes in topic

YouTube Broadcast to Lure Investors

**#BHEU  @BlackHatEvents**

Information Classification: General

## Slide 27

###### **[Affiliates] Theft of money from victims(1/2)**

- ➔ **Leading through one-man-show deception to avoid suspicion**

   - To multiple execution, Affiliate uses a various methods

      - (Patch based) V5 Multiloader

      - (Sandbox / Virtual Machines) Sandboxie, VMware workstation, …

multiple execution using 'VMware Workstation'

multiple execution using 'V5 Multiloader'

**#BHEU  @BlackHatEvents**

Information Classification: General

## Slide 28

###### **[Affiliates] Theft of money from victims(2/2)**

- ➔ **Two methods to money theft tricks**

   - Basically, affiliates do sending the wrong signals to victims, leading to losses

   - Ban the victim for reasons that don't make sense to them

   - Needless to say, the money deposited by the victim is not returned and <u>becomes the property of the affiliate</u>

OK! Confirmed
OK
Check please
Buy, Buy wait

Send'wrong'signals(order'hints)'to'victims

Surveillance'of'users'and'banning'with'unconvincing'excuses

**#BHEU  @BlackHatEvents**

Information Classification: General

## Slide 29

#### **Fake HTS Program Analysis**

1. Identify threats

2. Program analysis

3. Malicious behavior analysis

**#BHEU  @BlackHatEvents**

Information Classification: General

## Slide 30

###### **Identify threats**

- ➔ **Lots of screenshot data, including developers and infrastructure operators**

**#BHEU  @BlackHatEvents**

Information Classification: General

## Slide 31

**Identify threats**

- ➔ **Lots of screenshot data, including developers and infrastructure operators**

**#BHEU  @BlackHatEvents**

Information Classification: General

## Slide 32

###### **Identify threats**

- ➔ **Interesting! What is this program?**

**#BHEU  @BlackHatEvents**

Information Classification: General

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
EUROPE 2024
Identify threats
— Interesting! What is this program? TS.exe
CodeView Info
Offset
Name
& CvSig
Signature
Age
PDB
CodeView Info
Name
CySig
Signature
Age
PDB
Offset
CodeView Info
Name
CvSig
Signature
Age
PDB
Offset
Information Classification: General
PE
Type References
b =m References
d Resources
d{} -
4{
Value J 4, ~ eat
v 02000014
RSDS “yA nfoAttribute @02000003
{9235A2CF-0C49-4473-A15E-B9EBO9D4FC633} >% D ker @0200006D
C:-#DevelopwProjectwhts#2. Obfuscator#x86¥HTS. pdb Py Filer
v
Value 7
RSDS 4
{CBSEF8DA-CO15-4999-B9AF-B43A738E0680} DEE pE
b = Type References
b = References
b Resources
4. Obfuscator#x86¥HTS.pdb
C:'¥Develop#Project#]MidasHTSY
b{} -
Value
4{}
RSDS d* oattribute @02000003
(A7AB130E-ABCD-4DF0-ADE4-CC80D4528282} rte i pee
C:¥Develop#Project#hts#2. Obfuscator#x864MANAGER.pdb
S @020001
@02000126
@02000127
@02000128
102000072
@02000129
2.
A
```

## Slide 33

###### **Program analysis**

###### ➔ **Interesting! What is this program?**

Read

**#BHEU  @BlackHatEvents**

Information Classification: General

## Slide 34

###### **Program analysis**

###### ➔ **Correlating programs and screenshots**

**#BHEU  @BlackHatEvents**

Information Classification: General

## Slide 35

###### **Malicious behavior analysis**

- ➔ **They think they're making an investment**

Information Classification: General

**#BHEU  @BlackHatEvents**

## Slide 36

###### **Malicious behavior analysis**

- ➔ **There is someone watching over this**

###### **Sending captured screens to customers is absolutely prohibited!!!**

**#BHEU  @BlackHatEvents**

Information Classification: General

## Slide 37

###### **Malicious behavior analysis**

###### ➔ **There is someone watching over this**

**#BHEU  @BlackHatEvents**

Information Classification: General

## Slide 38

###### **Malicious behavior analysis**

- ➔ **There is someone watching over this**

**#BHEU  @BlackHatEvents**

Information Classification: General

## Slide 39

###### **Malicious behavior analysis**

- ➔ **Eventually they run away**

**#BHEU  @BlackHatEvents**

Information Classification: General

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bifekhat Malicious behavior analysis
EUROPE 2024
— Eventually they run away
2023.04. 2023.06.
case "AONE_295732": case "AONE 295732":
return GClass43. GEnum5.const_51; return GClass35.GEnum4.const_46;
>
case GClass43.GEnum5.const 51: ase GClass35.GEnum4.const 46:
return Thttp://154.83.21.79:4423/"; return |"http://@.0.0.0:4423/">
Check your current connection location or Network status (VPN, etc.)
Information Classification: General
```

## Slide 40

#### **Response**

###### 1. Response for Financial Companies

Information Classification: General

**#BHEU  @BlackHatEvents**

## Slide 41

###### **Response for Financial Companies**

- ➔ **Create detailed analysis and detection rules**

   - OSINT and programmatic analysis identified approximately 125 identical fake HTS

   - Writing detection rules

      - YARA : Livehunt from virustotal

      - Snort : Apply to Financial Security SOC('23.3)

**#BHEU  @BlackHatEvents**

Information Classification: General

## Slide 42

## Conclusion

#BHEU @BlackHatEvents

## Slide 43

###### **Black Hat Europe Sound Bytes**

- ➔ **Large undiscovered cybercrime clusters**

   - Potential losses could reach hundreds of billions due to fake trading platforms, hidden fees, long operations, and large member bases.

   - Many victims often viewing their losses as personal investment failures rather than the result of targeted fraud.

- ➔ **Contextual Literacy and Continuous Monitoring in OSINT**

   - Threat assessment demands understanding your country’s laws, culture, and context.

- ➔ **Criminals are also actively utilizing GenAI like ChatGPT**

   - GenAI is very effective at unit-level function development

   - How do we adapt to counter this new wave of malware?

Antiforensic script by ChatGPT **#BHEU  @BlackHatEvents**

Information Classification: General

## Slide 44

**Report Download**

# **Thank you**

**Financial Security Institute Sung-Wook Jang Yong-Hyun Kim (@copy_and_paster, yhkim@fsec.or.kr)**

Information Classification: General

**#BHEU   @BlackHatEvents #BHEU  @BlackHatEvents**
