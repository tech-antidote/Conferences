---
title: "Chained to Hit Discovering New Vectors to Gain Remote and Root Access in SAP Enterprise Software"
speakers: ["Yvan Genuer", "Pablo Artuso"]
conference: "Black Hat"
conference_full: "Black Hat USA 2023"
edition: "USA"
year: 2023
source_pdf: "Black Hat USA 2023 slides/Yvan Genuer & Pablo Artuso_Chained to Hit Discovering New Vectors to Gain Remote and Root Access in SAP Enterprise Software.pdf"
pages: 98
sha256: "78307b2ad41ddde2571333e67115d2b8698538df656c2793494d947b61191b98"
text_chars: 41146
ocr_pages: 37
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:27:51Z"
---
# Chained to Hit Discovering New Vectors to Gain Remote and Root Access in SAP Enterprise Software

**Speakers:** Yvan Genuer, Pablo Artuso  
**Conference:** Black Hat USA 2023  
**Source:** `Black Hat USA 2023 slides/Yvan Genuer & Pablo Artuso_Chained to Hit Discovering New Vectors to Gain Remote and Root Access in SAP Enterprise Software.pdf` (98 pages)


## Slide 1

## Chained to Hit: Discovering New Vectors to Gain Remote and Root Access in SAP Enterprise Software

Pablo Artuso, Yvan Genuer

#BHUSA   @BlackHatEvents

1

## Slide 2

Pablo Artuso

Onapsis

**Yvan Genuer**

- › Lead Security Researcher

   - › Security Researcher

- › 10 years SAP Security experience

   - › 20 years SAP experience

- › Java rookie

   - › 10 years SAP Security

- **›** @lmkalg

- › linkedin.com/in/1ggy

#BHUSA  @BlackHatEvents 2

## Slide 3

87% 77% 100%
of the Global  of the world’s  of F500 Oil & Gas
74% 2000 use SAP transaction revenue

#BHUSA  @BlackHatEvents

3

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 20253
ow ERP SOLUTION MANAGER SANE MUNG SU'SINESS SU ao
SOLUTION MANAGER F /Ij-
=ERP
ERP
ap Pi ml
P IM ERP HCM
fe SCM:
CRM
WM
a |
Be = BUSINESS. IN TELIGENGE: Rp ‘
CLOUD: BUSINESS SUITE s/s Hana LEONARDO cow
of the Global of the world’s of F500 Oil & Gas
2000 use SAP transaction revenue
```

## Slide 4

root or nt/system
CVE-2023-24523
Stage 3  local http request local user access
SSRF RCE Windows Arbitrary file reading SQLi
CVE-2023-36925 CVE-2023-27497 CVE-2023-23857 CVE-2022-41272
P4 service access
Stage 2
Enable arbitrary application
CVE-2023-28761
HTTP service access
Stage 1

#BHUSA   @BlackHatEvents 4

## Slide 5

#BHUSA   @BlackHatEvents 5

## Slide 6

# What just happened ?

#BHUSA  @BlackHatEvents 6

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
USA 20253
What just happened 7?
Chained to hit: Discovering new vectors to
gain remote and root access in SAP
Enterprise Software
Pablo Artuso Yvan Genuer
Onapsis Onapsis
partuso@onapsis.com ygenuer@onapsis.com
1. Abstract
At the core of every business on the planet there will always be a mission critical application system.
Overlooking its security is senseless and at the same time dangerous as it will result in putting your
business at a high risk.
During 2022 multiple months-lasting research projects were kicked off as part of the Onapsis Research
labs. Even though each of them had their own important results, no one was expecting that a combination
of them would end up in finding chains of exploitation which could cause serious damage.
This documentation will begin with the analysis of “P4”, a proprietary protocol based on Remote Method
```

## Slide 7

root or nt/system
CVE-2023-24523

#### **Stage 3**

#BHUSA   @BlackHatEvents

7

## Slide 8

#BHUSA  @BlackHatEvents

8

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
USA 20253
Netweaver JAVA S/4 HANA Netweaver ABAP
/1//7 /1/// /1/1/7
```

## Slide 9

#BHUSA  @BlackHatEvents

9

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
USA 20253
Netweaver JAVA S/4 HANA Netweaver ABAP
```

## Slide 10

Accomplish several life-cycle tasks
OS independent
Part of SAP system

#BHUSA  @BlackHatEvents 10

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
USA 20253
Netweaver JAVA S/4 HANA Netweaver ABAP
SAP Host Ctrl
SILL/
Accomplish several life-cycle tasks
OS independent
Part of SAP system
10
```

## Slide 11

#BHUSA  @BlackHatEvents

11

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 20253
Netweaver JAVA S/4 HANA Netweaver ABAP
[user@saphost ~]# ps
root 42100 1
root 42241 a
sapadm 42110 1
[user@saphost ~]# ss
LISTEN 0 20
ESTAB 0
ESTAB 0
-ef | grep hostctrl
0 Junl13 ? 00:00:16 ./exe/saphostexec -start pf=/usr/sap/hostctrl/exe/host_profile
0 Junl13 ? 00:02:15 /usr/sap/hostctrl/exe/saposcol -l -w60 pf=/usr/sap/hostctrl/exe/host_profile
0 Junl13 ? 00:01:56 /usr/sap/hostctrl/exe/sapstartsrv pf=/usr/sap/hostctrl/exe/host_profile -D
-larntp | grep 421
k:1128 a users: (("sapstartsrv",pid=42110, fd=18) )
saphost:1128 saphost:47510 users: (("sapstartsrv",pid=42110, fd=24) )
saphost:1128 saphost:47514 users: (("sapstartsrv",pid=42110, fd=26) )
11/1/71 /1/// /1/1/7
11
```

## Slide 12

#BHUSA  @BlackHatEvents

12

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
USA 20253
Netweaver JAVA S/4 HANA Netweaver ABAP
[user@saphost ~]# ps -ef | grep hostctrl ./exe/saphostexec -start pf=/usr/:
root 42100 Q@ Junl13 ? 00 5G
root 42241 0 Junl3 ? OTOP ¢
sapadm 42110 0 Junl3 ? 0
[user@saphost ~]# ss -larntp | grep 421
LISTEN 6) D sce a BP |
5 host_profil
/usr/sap/hostctrl/exe/saposcol -1 jpeeceemipexeyneee preeale
/usr/sap/hostctrl/exe/sapstartsrv |Gtmt/exe/mostiprotite =p
Tr TSeTrs=(\ Sapstartsrv",pid=42110, fd=18) )
ESTAB 0) f sapnost: 1128 Sapnos ts: 47510 sers:{({"sapstartsrv" , pid=42110, fd=24) )
ESTAB 0 saphost:1128 saphost:47514 users: (("sapstartsrv",pid=42110, fd=26) )
12
```

## Slide 13

#BHUSA  @BlackHatEvents

13

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 20253
Netweaver JAVA S/4 HANA Netweaver ABAP
Q | A
mel
[user@saphos’
_ A> p hostctrl
I oot 42 1G :00:16 ./exe/saphostexec -start pf=/usr/sap/hostctrl/exe/host_ profile
? 90:02:15 /usr/sap/hostct -l -w60 pf=/usr/sap/hostctrl/exe/host_profile
gelene id 22& 90:01:56 /usr/sap/hostctrl/exe/sapstartsrv pf=/usr/sap/hostctrit/exe/host_profile -D
grep 421
ESTAB 0) f saphost: 1128 Sapnos i: 47510 sers:
({"sapstartsrv" ,pid=42110, fd=24) )
ESTAB 0) saphost:1128 saphost:47514 isers:
("sapstartsrv",pid=42110, fd=26) )
ea nae A> 1 ae ee Jsers: (("sapstartsrv",pid=42110, fd=18) )
f
(
13
```

## Slide 14

#BHUSA  @BlackHatEvents

14

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
USA 20253
Netweaver JAVA
[user@saphost ~]# ps
root 42100 1
root 42241 1
sapadm 42110 dh
[user@saphost ~]# ss
LISTEN
ESTAB
ESTAB
-ef | grep hostctrl
Q@ Junl13 ?
0
0 Junl13 ? 00
0
0 jJunl3 ?
-larntp | grep 421
[TUuse rGSapnost
0 20
0 0
0 0
~|# SS
) BOO 6
1:02:15 /usr/sap/hostctrl/exe/saposcol -|
-Laflityp |
S/4 HANA
A
nl
./exe/saphostexec
QGréep 421
-1128
saphost:1128
saphost:1128
-start pf=/usr/sap/hostctrl/exe/host_profile
-w60 pf=/usr/sap/hostctrl/exe/host_profile
90:01:56 /usr/sap/hostctrl/exe/sapstartsrv pf=/usr/sap/hostctrit/exe/host_profile -D
artsrv",pid=42110, 8)
)
artsrv",pid=42110, fa =.
)
artsrv"
,pid=42110, fd=26)
14
```

## Slide 15

#BHUSA  @BlackHatEvents

15

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 20253
[user@saphost exe]# ./saphostctrl
Usage: saphostctrl [generic option]... -function <Webmethod> [argument]...
Saphostctrl -help [<Webmethod>]
Supported Webmethods:
ConfigureOutsideDiscovery
Configure the Outside [iscovery Job which runs periodically
These Options control the Outside Discovery Job.
If frequency is not provided, it will run every 12 hours.
If execution options are not provided the default will be used
-enable
[-frequency <X> Run frequency in minutes]
[-jobtimeout <X> Wait X seconds for the Outside
```

## Slide 16

#BHUSA  @BlackHatEvents

16

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 20253
[user@saphost exe]# ./saphostctrl -prot tcp -function ConfigureOutsideDiscovery \
-enable \
-sldhost 127.0.0.1 -sldport 1234 \
-sldusername BBBBB -sldpassword CCCC
OR a aK a a KK ak aK ok ak ak ok ok ak ak ok ak ak ok ak ak ok ok ak ak ok ak ok ok ak ok ok akc of
KK aK a a a ok kak kak kak ak ak ok ak ok ak ok ak ak ok ak ok ak ak ak ok
ComputerSystem , string , Enabled
ExecutionFrequencyMinutes , uint64 , 720
ee eee ee eee SSS SSS SSS SSS SSS SSS SSS SSS SSS SSS SSS SSeS SSeS!
CreationClassName , string , OutsideDiscoveryDestinations
127.0.0.1 1234 , string , /usr/sap/hostctrl/exe/config.d/slddest_127.0.0.1 1234.cfg
```

## Slide 17

#BHUSA  @BlackHatEvents

17

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 20253
tcpdump -i lo -A -vv port 1128 or port 1129
17
```

## Slide 18

#BHUSA  @BlackHatEvents

18

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 20253
tcpdump -i lo -A -vv port 1128 or port 1129
localhost.55011 > localhost.saphostctrl: Flags [P.], cksum 0x02b6 (inco
P55100 ecr 1627955100], length 1165
h.q.Q.
Ho localhost:1128
User-Agent: gSOAP/2.7
Content-Type: text/xml; charset=utf-8
Content-Length: 1000
Connection: keep-alive
SOAPAction: ""
<?xml version="1.0" encoding="UTF-8"?>
KSOAP-ENV: Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelo
"http: //www.w3.org/2001/XMLSchema-instance" xmlns d="http://www.w3.org/
MS" xmlns:SAPHostControl="urn:SAPHostControl" xmln APLandscapeService="
ns:SAPOscol="urn:SAPOscol" xmlns:SAPDSR="urn:SAPDSR">
<SOAP- ENV: Body>
KSAPHostControl:ConfigureOutsideDiscovery>
Kconfiguration>
<flags></flags>
<status>0D-CFG-ENABLED</status>
<f requency>720</f requency>
<destinations>
<item>
<name>127.
<host>127
<port>123
<usernam BBBB</username>
<password>CCC password>
<useSSL>false</useSSL>
<properties></properties>
</item>
</destinations>
<arguments></arguments>
K/configuration></SAPHostControl:ConfigureOutsideDiscovery></SOAP-ENV: Bod
```

## Slide 19

No authentication

New parameters in game

#BHUSA  @BlackHatEvents

19

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
piseikhat Na
USA 20253
localhost.
psstooecr a) A...a...POST / HTTP/1.1
Host: localhost:1128
Ucepmoere| User-Agent: gSOAP/2./7
pee) Content-Type: text/xml; charset=utf-8 No authentication
Content-Le
Connection) Content-Length: 1000
SOAPAction ;
Connection: keep-alive
<?xml vers
SoApPseNV:en| SOAPAction: ""
"http://www.
S" xmlns:SAPHostControl="urn:SAPHostControl" xmlns:SAPLandscapeService="
s:SAPOscol= < c : 1 c=
poke ae <destinations>
SAPHostCont <item>
configurati
<flags></ <name>127.0.0.1 1234</name>
<status>0 —
<frequenc <host>127.0.0.1</host>
<destinat
<item> <port>1234</port> .
cho <username>BBBBB</username> New parameters IN game
<po
ae <password>CCCC</password>
a. <useSSL>false</useSSL>
Pia <properties></properties>
</item
</destina < : >
<argument / it em
/configurat- ae! ta tae
```

## Slide 20

#BHUSA   @BlackHatEvents

20

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
[03:31]yvan@saphost: ~
——2,
#BHUSA @BlackHatEvents 20
```

## Slide 21

|**Patch**|**Description**|**CVSS**|**CVE**|
|---|---|---|---|
|3285757|Privilege Escalation vulnerability in SAP Host Agent (Start Service)|8.8|CVE-2023-24523|
|3275727|Memory Corruption vulnerability in SAPOSCOL|7.2|CVE-2023-27498|

#BHUSA  @BlackHatEvents

21

## Slide 22

root or nt/system
CVE-2023-24523
Stage 3  local http request local user access

#BHUSA   @BlackHatEvents

22

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Stage 3
‘ i
ges wae
A
* root or nt/system, ®
CVE-2023-24523
local http request
local user access
#BHUSA @BlackHatEvents 29
```

## Slide 23

SSRF RCE Windows Arbitrary file reading SQLi
CVE-2023-36925 CVE-2023-27497 CVE-2023-23857 CVE-2022-41272

#### **Stage 2**

#BHUSA   @BlackHatEvents

23

## Slide 24

OS
P4 Protocol
SAP Java NetWeaver
< Solution / Product >
PI/PO
SolMan
EP
LaMa
… #BHUSA  @BlackHatEvents

### P4: Introduction

**Simplified stack of SAP Java-based Solution / Product**

#BHUSA  @BlackHatEvents

24

## Slide 25

### P4: JNDI basics

https://help.sap.com/doc/saphelp_nw73ehp1/7.31.19/en-US/48/2d9ba88aef4bb9e10000000a42189b/content.htm?no_cache=true

#BHUSA  @BlackHatEvents 25

## Slide 26

### P4: JNDI basics

#BHUSA  @BlackHatEvents

26

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
USA 20253
P4: JNDI basics
JNDI
Implementation
$SSsss
26
```

## Slide 27

### P4: Analysis Cycle

List
Services

#BHUSA  @BlackHatEvents

## Slide 28

### P4: Listing services

#BHUSA  @BlackHatEvents 28

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
blackhat Se rae . *
USA 20253
P4: Listing services
public static void Licensing(String host, String port) throws Exception{
Context ctxt = build properties(host, port, auth: false);
Object licen = (Object) ctxt. lookup("Licensing");
if (licen == null){
System.out.println("Lookup failed! Object is null");
com.sap.engine.services. jndi.persistent.exceptions.NameNotFoundException:| Object not found in lookup of Licensing &
at com.sap.engine.services. jndi.implserver.ServerContextImpL. LookupeGServercunrtextinpe. java oss)
at com.sap.engine.services. jndi.implserver.ServerContextRedirectableImpL. Lookup(ServerContextRedirectable
at com.sap.engine.services. jndi.implserver.ServerContextRedirectableImp|lp4 Skel.dispatch(ServerContextRedi
at com.sap.engine.services.rmi_p4.DispatchImpl. runInternal(DispatchImplL. java:483)
```

## Slide 29

### P4: Listing services

<u>https://codewhitesec.blogspot.com/2021/06/about-unsuccessful-quest-for.html</u> (Kai Ullrich)

#BHUSA  @BlackHatEvents

29

## Slide 30

P4: Analysis Cycle
Kai
Server
Ullrich’s
Find Interface  Logs
Script List  Pick
&
Services service
Filter
Implementation grep
Telnet
Results
Static &
Dynamic  Documentation
analysis
JBD
Server
Logs JCC
#BHUSA  @BlackHatEvents

## Slide 31

### P4: Findings

|**Patch**|**Description**|**CVSS**|**CVE**|
|---|---|---|---|
|3305369|Multiple vulnerabilities in SAP Diagnostics Agent|10|CVE-2023-27497|
|3252433|Arbitrary read of OS files+Full DoS in locking service|9.9|CVE-2023-23857|
|3273480|SQL injection (read)+DoS in User Defined Search service|9.9|CVE-2022-41272|
|3267780|SQL injection (read)+DoS in JobBean service|9.4|CVE-2022-41271|
|3268093|RFC arbitrary function execution+JCO password leak in rfcengine service|9.4|CVE-2023-0017|
||Incorrect reference handling leading to arbitrary application startup|8.2|CVE-2023-30744|
|3288096|||CVE-2023-26460|
|3288394
3288480|Multiple information disclosures|5.3|CVE-2023-24526
CVE-2023-27268|
|3287784|||CVE-2023-24527|

#BHUSA  @BlackHatEvents 31

## Slide 32

### P4: Findings

|**Patch**|**Description**|**CVSS**|**CVE**|
|---|---|---|---|
|3305369|Multiple vulnerabilities in SAP Diagnostics Agent|10|CVE-2023-27497|
|**3252433**|**Arbitrary read of OS files+ Full DoS in locking service**|**9.9**|**CVE-2023-23857**|
|3273480|SQL injection (read)+DoS in User Defined Search service|9.9|CVE-2022-41272|
|3267780|SQL injection (read)+DoS in JobBean service|9.4|CVE-2022-41271|
|3268093|RFC arbitrary function execution+JCO password leak in rfcengine service|9.4|CVE-2023-0017|
||Incorrect reference handling leading to arbitrary application startup|8.2|CVE-2023-30744|
|3288096|||CVE-2023-26460|
|3288394
3288480|Multiple information disclosures|5.3|CVE-2023-24526
CVE-2023-27268|
|3287784|||CVE-2023-24527|

#BHUSA  @BlackHatEvents 32

## Slide 33

### P4: Findings

|**Patch**|**Description**|**CVSS**|**CVE**|
|---|---|---|---|
|**3305369**|**Multiple vulnerabilities in SAP Diagnostics Agent**|**10**|**CVE-2023-27497**|
|3252433|Arbitrary read of OS files+Full DoS in locking service|9.9|CVE-2023-23857|
|3273480|SQL injection (read)+DoS in User Defined Search service|9.9|CVE-2022-41272|
|3267780|SQL injection (read)+DoS in JobBean service|9.4|CVE-2022-41271|
|3268093|RFC arbitrary function execution+JCO password leak in rfcengine service|9.4|CVE-2023-0017|
||Incorrect reference handling leading to arbitrary application startup|8.2|CVE-2023-30744|
|3288096|||CVE-2023-26460|
|3288394
3288480|Multiple information disclosures|5.3|CVE-2023-24526
CVE-2023-27268|
|3287784|||CVE-2023-24527|

#BHUSA  @BlackHatEvents 33

## Slide 34

#BHUSA  @BlackHatEvents

34

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
USA 20253
Netweaver JAVA S/4 HANA Netweaver ABAP
SAP Solution
Manager
34
```

## Slide 35

#BHUSA  @BlackHatEvents

35

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
USA 20253
Netweaver JAVA S/4 HANA Netweaver ABAP
SAP Solution
Manager
prftichiat 2
USA 224,
AUGUST 5-6, 2020
BRIEFINGS
An Unauthenticated Journey to Root :
Pwning Your Company's Enterprise
Software Servers
Pablo Artuso - Yvan Genuer
35
```

## Slide 36

#BHUSA  @BlackHatEvents

36

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
USA 20253
Netweaver JAVA S/4 HANA Netweaver ABAP
SAP Solution
SMDAgent SMDAgent SMDAgent Manager
SMDAgent
36
```

## Slide 37

#BHUSA  @BlackHatEvents

37

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
USA 20253
Netweaver JAVA S/4 HANA Netweaver ABAP
SAP Solution
Manager
SMDAgent
SMDAgent SMDAgent
SMDAgent
37
```

## Slide 38

#BHUSA  @BlackHatEvents

38

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
USA 20253
Netweaver JAVA S/4 HANA Netweaver ABAP
SMDAgent
SAP Solution
Manager
SMDAgent
a wae
SMDAgent
ay Sa
38
```

## Slide 39

“Hey SMDAgents do this simulation for me”

#BHUSA  @BlackHatEvents

39

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
USA 20253
Netweaver JAVA S/4 HANA
SAP Solution
SMDAgent Manager
(A ie 1D
I I " “Hey SMDAgents do
this simulation for me”
——| P4 SMDAgent
SMDAgent SMDAgent
39
```

## Slide 40

“Sir yes sir !” “Sir yes sir !”

“Sir yes sir !”

“Hey SMDAgents do this simulation for me”

“Sir yes sir !”

#BHUSA  @BlackHatEvents

40

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
USA 20253
Netweaver JAVA S/4 HANA Netweaver ABAP
SAR
SAP Solution
Manager
(Ame 1
“Hey SMDAgents do
this simulation for me”
“Sir yes sir !”
P4
40
```

## Slide 41

#BHUSA  @BlackHatEvents

41

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
USA 20253
@ AVaEPCUMNecLur.jar cs
&  META-INF mi | ft AbapFactoryBean.class | {i AgentDataProviderSimulation. class ©
¥- # com.sap.sup. admin. connector Lnmperec java .ucLe.rrupercics
o api
o & exception
P Pe ahepexcennoaawe spublic final class AgentDataProviderSimulation implements IAbapComponent
& iy AbapFactoryBean.class public static final String KEY = "FM_MAI_SIMULATION_AGENT";
© by» AbapFactoryHome. class
5) package-version. properties
&  impl = public void processFunction(JCO.ParameterList pImport, JCO.ParameterLis
tm sim ae: ._| IMAITestService service;
? ob AgentDataProviderSimulation : .
> @ AgentDataProviderSimulat, | 2: String agentName = pImport.getString("IM_AGENT_ NAME");
PB intrnscapedataPresidersinull if (agentName == null || agentName.trim().equals(""))
|) package-version. properties
& # tool 26 throw new AbapFatalException("Parameter Agent Name cannot be empty
2¢ AgentHandleWrapper agent = SMDManager.getInstance().getSMDAgent (agent
aC if (agent == null)
31 throw new AbapFatalException( "Agent
: try {
7 service = (IMAITestService)SMDManager.getRemoteService(agent,
3¢ } catch (Exception e) {
40 throw new AbapFatalException("Initialization of MAITestService fail
}
a3 String collectorClass = pImport.getString("IM_COLLECTOR_CLASS");
aa Properties contextParams = convertTableToProperties(pImport.getTable(
Map inputParams = convertTableToMap(pImport.getTable("IM_INPUT_PARAMS
Map metricParams = convertTableToMap(pImport.getTable("IM_METRIC_PARA
e try {
+ agentName + "' does not ex
com.
19 MetricData[] metricCollectionData = service. runSimulation(collector
56 JCO.Table results = pExport.getTable("EX_METRIC_DATA");
576 for (int i = 0; i < metricCollectionData.length; i++) {
MetricData metricData = metricCollectionData [i];
results annandRawi 1:
4
```

## Slide 42

#BHUSA  @BlackHatEvents

42

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
USA 20253
@ AVaEPCUMNecLur.jar cs
&  META-INF mi | ft AbapFactoryBean.class | {i AgentDataProviderSimulation. class ©
a hl aL Lnperc java.uciLe.rireuperctics,
o api
o & exception
P Pe ahepexcennoaawe spublic final class AgentDataProviderSimulation implements IAbapComponent
& iy AbapFactoryBean.class public static final String KEY = "FM_MAI_SIMULATION_AGENT";
© by» AbapFactoryHome. class
5) package-version. properties
o & impl = public void processFunction(JCO.ParameterList pImport, JCO.ParameterLis
tm sim IMAITestService service;
P To AgentDataProviderSimulation : .
o & AgentDataProviderSimulat |) 24 String agentName = pImport.getString("IM_AGENT_ NAME") ;
PB intrnscapedataPresidersinull if (agentName == null || agentName.trim().equals(""))
|) package-version. properties
& # tool 26 throw new AbapFatalException("Parameter Agent Name cannot be empty
2¢ AgentHandleWrapper agent = SMDManager.getInstance().getSMDAgent (agent
aC if (agent == null)
31 throw new AbapFatalException( "Agent
: try {
+ agentName + "' does not ex
service = (IMAITestService)SMDManager.getRemoteService(agent, "com.
3¢ } catch (Exception e) {
40 throw new AbapFatalExcepti "Initialization of MAITestService fail
a3 String collectorClass = pImport.getString("IM_COLLECTOR_CLASS");
aa Properties contextParams = Ct getTable(
16 Map metricParams = convertTableToMap (pImport.. getTable("IM_ METRIC_ PARA
7 try {
19 MetricData[] metricCollectionData = service. runSimulation(collector
56 JCO.Table results = pExport.getTable("EX_METRIC_DATA");
576 for (int i = 0; i < metricCollectionData.length; i++) {
MetricData metricData = metricCollectionData [i];
results annandRawi 1:
42
```

## Slide 43

#BHUSA  @BlackHatEvents

43

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
USA 20253
@ AVaEPCUMNecLur.jar cs
o §§ META-INF
¢ & com.sap.sup.admin. connector
o api
o & exception
9 & factory
© fi) AbapFactory.class
& ta» AbapFactoryBean.class
© by» AbapFactoryHome. class
|) package-version. properties
o> 8 impl
? & simu
? tp AgentDataProviderSimulation
o © AgentDataProviderSimulat
© fi IntroscopeDataProviderSimul
|) package-version. properties
© tool
=e try {
e try {
tb AbapFactoryBean. class 2 tip AgentDataProviderSimulation. class °
ampere yava.ucic.rroperctics,
spublic final class AgentDataProviderSimulation implements IAbapComponent
public static final String KEY = "FM_MAI_SIMULATION_AGENT";
public void processFunction(JCO.ParameterList pImport, JCO.ParameterLis
IMAITestService service;
String agentName = pImport.getString("IM_AGENT_ NAME") ;
if (agentName == null || agentName.trim().equals(""))
throw new AbapFatalException("Parameter Agent Name cannot be empty
AgentHandleWrapper agent = SMDManager.getInstance().getSMDAgent (agent
if (agent == null)
throw new AbapFatalException( "Agent
+ agentName + "' does not ex
service = (IMAITestService)SMDManager.getRemoteService(agent, "com.
} catch (Exception e) {
throw new AbapFatalException("Initialization of MAITestService fail
}
String collectorClass = pImport.getString("IM_COLLECTOR_CLASS");
Properties contextParams = convertTableToProperties(pImport.getTable(
Map inputParams = convertTableToMap(pImport. get iapier ah. TNPUT_ PAR
Map metricParams = convertTableToMap (ate
MetricData[] metricCollectionData
JCO.Table results = pExport.getTable
576 for (int i = 0; i < met ricCollectionBetae length; Tr i
MetricData metricData = metricCollectionData [i];
results annandRawi 1:
43
```

## Slide 44

Collectors classes On Agent side

#BHUSA  @BlackHatEvents 44

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
USA 20253
o
8
ie]
ie]
is]
if
ie]
i]
z
_
o
o
o
o
o
o
e
o
o
o
o
o
o
o
o
o
o
o
o
o
o
o
o
o
o
o
o
o
o
o
o
o
o
o
o
o & META-INF
¢  model.collector
bpmmon
hook
http
jxbp
msgmon
saphostctrl
xsa
CollectorHelper.class
EventLogServiceCollector.class
ExtendedSAPControlWSCollector.class
ExtendedSysteminfoCollector.class
FileContentScannerCollector. class
FileServiceCollector. class
FileServiceCollector2. class
HelloWorldCollector. class
JmxGateway.class
JsonWrapperForSccCollector. class
LicenseCollector.class
RFCCollector.class
RFCDataProvider.class
SAPControlWSCollector. class
SAPGenericURLCheckCollector. class
SAPGrmgClassicCollector. class
SAPHTTPResponseCollector.class
SAPHostControlWSCollector. class
SAPJ2EEHttpCollector. class
SAPPingHTTPCollector. class
SAPPingHostCollector.class
SAPPingRfcCollector. class
SccCollector.class
SimpleFileServiceCollector. class
SimpleFileServiceCollector2. class
SimpleHttpCollector. class
fs» Subaccount.class
fxb Tunnel. class
fn» WSMetricCollector. class
<——_—
Collectors classes
On Agent side
44
```

## Slide 45

Collectors classes On Agent side

#BHUSA  @BlackHatEvents 45

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
USA 202
o & META-INF
¢  model.collector
bpmmon
hook
http
ixbp Collectors classes
msgmon .
apbortete < On Agent side
xsa
CollectorHelper.class
EventLogServiceCollector.class
ExtendedSAPControlWSCollector.class
ExtendedSysteminfoCollector.class
FileContentScannerCollector. class
FileServiceCollector. class
FileServiceCollector2. class
HelloWorldCollector. class
fw» JmxGateway.class
fw» JsonWrapperForSccCollector.class
LicenseCollector.class
VEVEVED oF oF oe eB
RFCCollector.class
RFCDataProvider.class
SAPControlWSCollector. class
SAPGenericURLCheckCollector. class
SAPGrmgClassicCollector. class
SAPHTTPResponseCollector.class
SAPPingHTTPCollector. class
SAPPingHostCollector.class
service. runSimulation(collector
SimpleFileServiceCollector2. class
Siipbeetndalled omens ricCollectionData. length; i++) {
SAPHostControlWSCollector. class
i fcCollector. cl .
Seccollectondaes sctionData
Subaccount. class
Tunnel. class metricCollectionData[i];
Speak aber tTableToMap(pImport.getTable("IM METRIC PARA
SimpleFileServiceCollector. class 0 rt. getTab
ton wWSMetricCollector.class _
TPT Tr TT TT TT TT TT TT eT eT eT eT Tee eT ee Tee eee ee ee
45
```

## Slide 46

com.sap.smd.mai.collector.HelloWorldCollector com.sap.smd.mai.collector.SAPPingHostCollector com.sap.smd.mai.collector.SAPGrmgClassicCollector com.sap.smd.mai.collector.SimpleFileServiceCollector com.sap.smd.mai.collector.SimpleFileServiceCollector2 com.sap.smd.mai.collector.SAPPingHTTPCollector com.sap.smd.mai.collector.SccCollector com.sap.smd.mai.collector.SAPControlWSCollector com.sap.smd.mai.collector.LicenseCollector com.sap.smd.mai.collector.FileServiceCollector com.sap.smd.mai.collector.FileContentScanCollector com.sap.smd.mai.collector.EventLogServiceCollector etc.

#BHUSA  @BlackHatEvents

46

## Slide 47

Collectors are executed on the remote Agent. Any vulnerabilities inside collectors will be executed on the remote Agent!

#BHUSA  @BlackHatEvents 47

## Slide 48

com.sap.smd.mai.collector.HelloWorldCollector com.sap.smd.mai.collector.SAPPingHostCollector com.sap.smd.mai.collector.SAPGrmgClassicCollector com.sap.smd.mai.collector.SimpleFileServiceCollector com.sap.smd.mai.collector.SimpleFileServiceCollector2 com.sap.smd.mai.collector.SAPPingHTTPCollector com.sap.smd.mai.collector.SccCollector com.sap.smd.mai.collector.SAPControlWSCollector com.sap.smd.mai.collector.LicenseCollector com.sap.smd.mai.collector.FileServiceCollector com.sap.smd.mai.collector.FileContentScanCollector com.sap.smd.mai.collector.EventLogServiceCollector etc.

#BHUSA  @BlackHatEvents 48

## Slide 49

**Patch** <u>3305369</u>

**Description** <u>Multiple vulnerabilities in SAP Diagnostics Agent</u>

**CVSS CVE** <u>10 CVE-2023-27497</u>

com.sap.smd.mai.collector.HelloWorldCollector com.sap.smd.mai.collector.SAPPingHostCollector com.sap.smd.mai.collector.SAPGrmgClassicCollector com.sap.smd.mai.collector.SimpleFileServiceCollector com.sap.smd.mai.collector.SimpleFileServiceCollector2 com.sap.smd.mai.collector.SAPPingHTTPCollector com.sap.smd.mai.collector.SccCollector com.sap.smd.mai.collector.SAPControlWSCollector com.sap.smd.mai.collector.LicenseCollector com.sap.smd.mai.collector.FileServiceCollector com.sap.smd.mai.collector.FileContentScanCollector **com.sap.smd.mai.collector.EventLogServiceCollector** etc.

#BHUSA  @BlackHatEvents 49

## Slide 50

**Patch Description CVSS CVE** <u>3305369 Multiple vulnerabilities in SAP Diagnostics Agent 10 CVE-2023-27497</u> com.sap.smd.mai.collector.HelloWorldCollector com.sap.smd.mai.collector.SAPPingHostCollector com.sap.smd.mai.collector.SAPGrmgClassicCollector com.sap.smd.mai.collector.SimpleFileServiceCollector com.sap.smd.mai.collector.SimpleFileServiceCollector2 com.sap.smd.mai.collector.SAPPingHTTPCollector com.sap.smd.mai.collector.SccCollector com.sap.smd.mai.collector.SAPControlWSCollector com.sap.smd.mai.collector.LicenseCollector com.sap.smd.mai.collector.FileServiceCollector com.sap.smd.mai.collector.FileContentScanCollector **com.sap.smd.mai.collector.EventLogServiceCollector** etc.

#BHUSA  @BlackHatEvents 50

## Slide 51

**Patch**

**Description**

<u>3348145 Header Injection in SAP Solution Manager (Diagnostic Agent) 3352058 Unauthenticated blind SSRF in SAP Solution Manager (Diagnostics agent)</u>

**CVSS CVE** <u>7.2 CVE-2023-36921 7.2 CVE-2023-36925</u>

com.sap.smd.mai.collector.HelloWorldCollector com.sap.smd.mai.collector.SAPPingHostCollector com.sap.smd.mai.collector.SAPGrmgClassicCollector com.sap.smd.mai.collector.SimpleFileServiceCollector com.sap.smd.mai.collector.SimpleFileServiceCollector2 **com.sap.smd.mai.collector.SAPPingHTTPCollector** com.sap.smd.mai.collector.SccCollector com.sap.smd.mai.collector.SAPControlWSCollector com.sap.smd.mai.collector.LicenseCollector com.sap.smd.mai.collector.FileServiceCollector com.sap.smd.mai.collector.FileContentScanCollector com.sap.smd.mai.collector.EventLogServiceCollector etc.

#BHUSA  @BlackHatEvents 51

## Slide 52

**Patch Description CVSS CVE** <u>3348145 Header Injection in SAP Solution Manager (Diagnostic Agent) 7.2 CVE-2023-36921 3352058 Unauthenticated blind SSRF in SAP Solution Manager (Diagnostics agent) 7.2 CVE-2023-36925</u>

com.sap.smd.mai.collector.HelloWorldCollector com.sap.smd.mai.collector.SAPPingHostCollector com.sap.smd.mai.collector.SAPGrmgClassicCollector com.sap.smd.mai.collector.SimpleFileServiceCollector com.sap.smd.mai.collector.SimpleFileServiceCollector2 **com.sap.smd.mai.collector.SAPPingHTTPCollector** com.sap.smd.mai.collector.SccCollector com.sap.smd.mai.collector.SAPControlWSCollector com.sap.smd.mai.collector.LicenseCollector com.sap.smd.mai.collector.FileServiceCollector com.sap.smd.mai.collector.FileContentScanCollector com.sap.smd.mai.collector.EventLogServiceCollector etc.

#BHUSA  @BlackHatEvents 52

## Slide 53

#BHUSA   @BlackHatEvents 53

## Slide 54

root or nt/system
CVE-2023-24523
Stage 3  local http request local user access
SSRF RCE Windows Arbitrary file reading SQLi
CVE-2023-36925 CVE-2023-27497 CVE-2023-23857 CVE-2022-41272
P4 service access
Stage 2

#BHUSA   @BlackHatEvents

54

## Slide 55

Enable arbitrary application
CVE-2023-28761
HTTP service access
Stage 1

#BHUSA   @BlackHatEvents

55

## Slide 56

### SAP JNDI Injection: JEA

**J** ava **E** ndpoint **A** nalyzer

Connects using credentials Downloads files (SOAP, Servlet, etc) **Config files analysis List of HTTP Endpoints**

###### **SAP Java-based system**

Onapsis/java_endpoint_analyzer

#BHUSA  @BlackHatEvents

5 6

56

## Slide 57

### SAP JNDI Injection: The vulnerable servlet

**Enterprise JEA Portal**

**NavigationServlet** is exposed without authentication

#BHUSA  @BlackHatEvents 57

## Slide 58

### SAP JNDI Injection: The vulnerable servlet

**doGet()** → handleGetSubTreeCall() → getNavigationTree() →… → **redirect** ()

#BHUSA  @BlackHatEvents

58

## Slide 59

### SAP JNDI Injection: The vulnerable servlet

#BHUSA  @BlackHatEvents

59

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
USA 20253
SAP JNDI Injection: The vulnerable servlet
String prefix = getNavURLPrefix(oldURL) ;
String url = getNavInternalName(oldURL) ;
redirector = this.mm_connectorMap.getRedirector (prefix);
while (redirector != null) {
result = redirector.redirect(url, environment) ;
59
```

## Slide 60

### SAP JNDI Injection: Finding the vulnerability

PCD PCDH TBN OBN **Redirectors /** MODELEDCONTENT ROLES GPN **Connectors** COLLABORATIONCONNECTOR

#BHUSA  @BlackHatEvents 60

## Slide 61

### SAP JNDI Injection: Finding the vulnerability

**PCD** PCD PCDH TBN OBN **Redirectors /** MODELEDCONTENT ROLES GPN **Connectors Prefix “pcd://”** COLLABORATIONCONNECTOR

#BHUSA  @BlackHatEvents

61

## Slide 62

### SAP JNDI Injection: Finding the vulnerability doGet() → **handleGetSubTreeCall()** → getNavigationTree() →… → **redirect** ()

#BHUSA  @BlackHatEvents

62

## Slide 63

### SAP JNDI Injection: Finding the vulnerability doGet() → **handleGetSubTreeCall()** → getNavigationTree() →… → **redirect** ()

JNDI lookup with user-controlled input

#BHUSA  @BlackHatEvents 63

## Slide 64

### SAP JNDI Injection: RMI Exploitation

- RMI-JNDI lookups can be used to load **remote clases** through JNDI references.

<u>https://www.blackhat.com/docs/us-16/materials/us-16-Munoz-A-Journey-From-JNDI-LDAP-Manipulation-To-RCE-wp.pdf</u>

#BHUSA  @BlackHatEvents

64

## Slide 65

### SAP JNDI Injection: RMI Exploitation

###### **Attacker**

###### **Attacker controlled server**

1

Enterprise
Portal

**Start an RMI Server hosting a JNDI reference which references to a remote class**

#BHUSA  @BlackHatEvents 65

## Slide 66

### SAP JNDI Injection: RMI Exploitation

###### **Attacker**

Attacker
controlled
server

2
1

Enterprise
Portal

**Executes payload using “pcd://rmi://<ip>:<port>”**

#BHUSA  @BlackHatEvents 66

## Slide 67

### SAP JNDI Injection: RMI Exploitation

Enterprise
Portal
2
1
3
Executes payload using “pcd://rmi://…” which
forces the JNDI lookup

Attacker

Attacker
controlled
server

#BHUSA  @BlackHatEvents 67

## Slide 68

### SAP JNDI Injection: RMI Exploitation

Attacker

Attacker
controlled
server

Enterprise
Portal
2
1
3
4

##### **RMI server returns a reference to remote class**

#BHUSA  @BlackHatEvents 68

## Slide 69

### SAP JNDI Injection: RMI Exploitation

Enterprise
Portal
2
1
3
4

**RMI server returns a reference to remote class**

#BHUSA  @BlackHatEvents 69

## Slide 70

### SAP JNDI Injection: RMI Exploitation

- ~~RMI-JNDI lookups can be used to load~~ **~~remote clases~~** ~~through JNDI references.~~

<u>https://www.blackhat.com/docs/us-16/materials/us-16-Munoz-A-Journey-From-JNDI-LDAP-Manipulation-To-RCE-wp.pdf</u>

- RMI JNDI lookups can be used to load **local classes** through JNDI references.

#BHUSA  @B lackHatEvents

<u>https://www.veracode.com/blog/research/exploiting-jndi-injections-java</u>

70

## Slide 71

### SAP JNDI Injection: RMI Exploitation

Enterprise
Portal
2
1
3
4
RMI server returns a reference to local class

#BHUSA  @BlackHatEvents

71

## Slide 72

### SAP JNDI Injection: Specific gadget

● Conditions to be met:

**○ Class must exist in SAP’s classpath** ○ **…. what else?**

#BHUSA  @BlackHatEvents

72

## Slide 73

### SAP JNDI Injection: Specific gadget

#BHUSA  @BlackHatEvents

73

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
USA 20253
SAP JNDI Injection: Specific gadget
2 private Object _getObjectInstance(Object refInfo, Name name, Context nameCtx,
4 Reference ref = null;
19 Object result = null;
08 if (refInfo instanceof Reference) {
51 ref = (Reference) refinfo;
2 } else if (refInfo instanceof Referenceable) {
ref = ((Referenceable)refInfo) .getReference();
t
ResolverManager mgr = (ResolverManager) ResolverManager.getInstance() ;
ObjectFactory fac = null;
596 if (ref != null) {
51 String f = ref.getFactoryClassName() ;
52 if (f != null) {
e try f
fac = mgr.findObjectFactory(f);
} catch (Exception e) {
NamingException ne = new NamingException("Exception while trying to J
ne.setRootCause(e);
throw ne;
t
72¢ if (fac != null) {
38 if (fac instanceof DirObjectFactory) {
return ((DirObjectFactory) fac) .getObjectInstance(ref, name, nameCtx
t
return fac.getObjectInstance(ref, name, nameCtx, env);
t
13
```

## Slide 74

### SAP JNDI Injection: Specific gadget

#BHUSA  @BlackHatEvents

74

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
USA 20253
SAP JNDI Injection: Specific gadget
String f = ref.getFactoryClassName() ;
fac = mgr.findObjectFactory(f) ;
74
```

## Slide 75

### SAP JNDI Injection: Specific gadget

#BHUSA  @BlackHatEvents 75

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 20253
throws |
String objectFactoryNamep
> public ObjectFactory findObjectFactory
320 IResolver resolver = null;
321 ObjectFactory objectFactory = null;
322 Object resolverClassName = null;
376 Class<?> factoryClass = Class.forName(objectFactoryName, true, Thread.curi
377 ObjectFactory Eee = (ObjectFactory)factoryClass.newInstance();
as. 0g .
3/796 this loo tal naPathIni ocation()) £
75
```

## Slide 76

### SAP JNDI Injection: Specific gadget

● Conditions to be met:

○ Class must exist in SAP’s classpath ○ **Must be a factory ○ Must be casteable to ObjectFactory ○ …. what else?**

#BHUSA  @BlackHatEvents

76

## Slide 77

### SAP JNDI Injection: Specific gadget

#BHUSA  @BlackHatEvents 77

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
We es [ A / 4 PRK. ‘ yo aa j
Q Se << ay
: eee ee. es A
blackhat ok Sia
USA 2023 Se Sig
SAP JNDI Injection: Specific gadget
return fac.getObjectInstance(ref, name, nameCtx, env);
```

## Slide 78

### SAP JNDI Injection: Specific gadget

● Conditions to be met:

○ Class must exist in SAP’s classpath ○ Must be a factory

○ Must be casteable to ObjectFactory **○ Must implement getObjectInstance** ○ **Must do something interesting**

#BHUSA  @BlackHatEvents

78

## Slide 79

### SAP JNDI Injection: Specific gadget **EJBObjectFactory**

#BHUSA  @BlackHatEvents

79

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
USA 20253
SAP JNDI Injection: Specific gadget
EJBObjectFactory
> privat—Obss-++ — =eference, Name argl,
AL. <= 4 String appName = getAppName(rert);
Ob 14 a
= t
rence);
1 ' : —
: - if (appName != null) {
privat rel tT) 4
hop | l - ’ f sARlams ) «
StartApp \appName) ;
179
```

## Slide 80

### SAP JNDI Injection: RMI Exploitation

Enterprise
Portal
2
1
3
4
RMI server returns a ref to the local
EJBObjectFactory

Attacker

Attacker
controlled
server

#BHUSA  @BlackHatEvents 80

## Slide 81

### SAP JNDI Injection: RMI Exploitation

Attacker

Attacker
controlled
server

Enterprise
Portal
2
1
3
5
4
Starting app…

**When resolving the reference, executes the startApp() with the appName provided**

#BHUSA  @BlackHatEvents 81

## Slide 82

### SAP JNDI Injection: RMI Exploitation

Attacker

Attacker
controlled
server

Enterprise
Portal
2
1
3
5
4
App started

##### **Execution crashes but application is now started**

#BHUSA  @BlackHatEvents

82

## Slide 83

### SAP JNDI Injection: Findings

**Patch Description CVSS CVE** 3289994 <u>Missing Authentication check in SAP NetWeaver Enterprise Portal</u> 6.5 CVE-2023-28761

#BHUSA  @BlackHatEvents

83

## Slide 84

### SAP JNDI Injection: Reverseless Exploitation

Attacker

1

Enterprise
Portal
Starting app…

**Launches exploit using EJB resolver and the ref with the appName in the same payload**

#BHUSA  @BlackHatEvents 84

## Slide 85

### SAP JNDI Injection: Reverseless Exploitation

###### **Attacker**

1

Enterprise
Portal

App started

Application started

#BHUSA  @BlackHatEvents

85

## Slide 86

P4 service access
Stage 2
Enable arbitrary application
CVE-2023-28761
HTTP service access
Stage 1

#BHUSA   @BlackHatEvents

86

## Slide 87

### Chaining: SAP Injection + P4 Exploitation

###### **Attacker**

**Enterprise Portal** **P4TunnelingApp**

1 **Launches SAP JNDI exploit and turns on “P4Tunneling” app**

#BHUSA  @BlackHatEvents

87

## Slide 88

### Chaining: SAP Injection + P4 Exploitation

Attacker

Enterprise
Portal
2
P4T
TCP HTTP P4

##### **Sends P4 traffic embedded inside HTTPs request to P4T**

#BHUSA  @BlackHatEvents 88

## Slide 89

root or nt/system
CVE-2023-24523
Stage 3  local http request local user access
SSRF RCE Windows Arbitrary file reading SQLi
CVE-2023-36925 CVE-2023-27497 CVE-2023-23857 CVE-2022-41272
P4 service access
Stage 2
Enable arbitrary application
CVE-2023-28761
HTTP service access
Stage 1

#BHUSA   @BlackHatEvents

89

## Slide 90

root or nt/system
CVE-2023-24523
local http request local user access
SSRF RCE Windows Arbitrary file reading SQLi
CVE-2023-36925 CVE-2023-27497 CVE-2023-23857 CVE-2022-41272
P4 service access
Enable arbitrary application
CVE-2023-28761
HTTP service access

#BHUSA   @BlackHatEvents

90

## Slide 91

root or nt/system
CVE-2023-24523
local http request local user access
SSRF RCE Windows Arbitrary file reading SQLi
CVE-2023-36925 CVE-2023-27497 CVE-2023-23857 CVE-2022-41272
P4 service access
Enable arbitrary application
CVE-2023-28761
HTTP service access

#BHUSA   @BlackHatEvents

91

## Slide 92

root or nt/system
CVE-2023-24523
local http request local user access
SSRF RCE Windows Arbitrary file reading SQLi
CVE-2023-36925 CVE-2023-27497 CVE-2023-23857 CVE-2022-41272
P4 service access
Enable arbitrary application
CVE-2023-28761
HTTP service access

#BHUSA   @BlackHatEvents

92

## Slide 93

# Stay Secure

|**Patch**|**Description**|**CVSS**|**CVE**|
|---|---|---|---|
|3305369|Multiple vulnerabilities in SAP Diagnostics Agent|10|CVE-2023-27497|
|3252433|Arbitrary read of OS files+Full DoS in locking service|9.9|CVE-2023-23857|
|3273480|SQL injection (read)+DoS in User Defined Search service|9.9|CVE-2022-41272|
|3267780|SQL injection (read)+DoS in JobBean service|9.4|CVE-2022-41271|
|3268093|RFC arbitrary function execution+JCO password leak in rfcengine service|9.4|CVE-2023-0017|
|3285757|Privilege Escalation vulnerability in SAP Host Agent (Start Service)|8.8|CVE-2023-24523|
|3317453|Incorrect reference handling leading to arbitrary application startup|8.2|CVE-2023-30744|
|3275727|Memory Corruption vulnerability in SAPOSCOL|7.2|CVE-2023-27498|
|3348145|Header Injection in SAP Solution Manager (Diagnostic Agent)|7.2|CVE-2023-36921|
|3352058|Unauthenticated blind SSRF in SAP Solution Manager (Diagnostics agent)|7.2|CVE-2023-36925|
|3289994|Missing Authentication check in SAP NetWeaver Enterprise Portal|6.5|CVE-2023-28761|
|3288096|||CVE-2023-26460|
|3288394
3288480|Multiple information disclosures|5.3|CVE-2023-24526
CVE-2023-27268|
|3287784|||CVE-2023-24527|

#BHUSA  @BlackHatEvents 93

## Slide 94

# Stay Secure

|**Patch**|**Description**|**CVSS**|**CVE**|
|---|---|---|---|
|3305369|Multiple vulnerabilities in SAP Diagnostics Agent|10|CVE-2023-27497|
|3252433|Arbitrary read of OS files+Full DoS in locking service|9.9|CVE-2023-23857|
|3273480|SQL injection (read)+DoS in User Defined Search service|9.9|CVE-2022-41272|
|3267780|SQL injection (read)+DoS in JobBean service|9.4|CVE-2022-41271|
|3268093|RFC arbitrary function execution+JCO password leak in rfcengine service|9.4|CVE-2023-0017|
|3285757|Privilege Escalation vulnerability in SAP Host Agent (Start Service)|8.8|CVE-2023-24523|
|3317453|Incorrect reference handling leading to arbitrary application startup|8.2|CVE-2023-30744|
|3275727|Memory Corruption vulnerability in SAPOSCOL|7.2|CVE-2023-27498|
|3348145|Header Injection in SAP Solution Manager (Diagnostic Agent)|7.2|CVE-2023-36921|
|3352058|Unauthenticated blind SSRF in SAP Solution Manager (Diagnostics agent)|7.2|CVE-2023-36925|
|3289994|Missing Authentication check in SAP NetWeaver Enterprise Portal|6.5|CVE-2023-28761|
|3288096|||CVE-2023-26460|
|3288394
3288480|Multiple information disclosures|5.3|CVE-2023-24526
CVE-2023-27268|
|3287784|||CVE-2023-24527|
|**3273729**|**Impact of CVE-2022-41271 and CVE-2022-41272**|**na**|**na**|
|**3299806**|**FAQ for SAP Security Note 3252433**|**na**|**na**|

#BHUSA  @BlackHatEvents

94

## Slide 95

Stay Secure
Patch Description CVSS CVE
3305369 Multiple vulnerabilities in SAP Diagnostics Agent 10 CVE-2023-27497
3252433 Arbitrary read of OS files + Full DoS in locking service 9.9 CVE-2023-23857
3273480 SQL injection (read) + DoS in User Defined Search service 9.9 CVE-2022-41272
3267780 SQL injection (read) + DoS in JobBean service 9.4 CVE-2022-41271
3268093 RFC arbitrary function execution + JCO password leak in rfcengine service 9.4 CVE-2023-0017
3285757 Privilege Escalation vulnerability in SAP Host Agent (Start Service) 8.8 CVE-2023-24523
3317453 Incorrect reference handling leading to arbitrary application startup 8.2 CVE-2023-30744
3275727 Memory Corruption vulnerability in SAPOSCOL 7.2 CVE-2023-27498
3348145 Header Injection in SAP Solution Manager (Diagnostic Agent) 7.2 CVE-2023-36921
3352058 Unauthenticated blind SSRF in SAP Solution Manager (Diagnostics agent) 7.2 CVE-2023-36925
3289994 Missing Authentication check in SAP NetWeaver Enterprise Portal 6.5 CVE-2023-28761
 3288096 CVE-2023-26460
3288394 CVE-2023-24526
Multiple information disclosures 5.3
3288480 CVE-2023-27268
3287784 CVE-2023-24527
3273729 Impact of CVE-2022-41271 and CVE-2022-41272 na na
3299806 FAQ for SAP Security Note 3252433 na na
#BHUSA  @BlackHatEvents
95

## Slide 96

# Stay Secure

- › Apply relevant patches…

- › Restrict and monitor P4 access as possible

- › IPS, IDS and Firewall are always encouraged

- › Restrict RMI-like traffic

#BHUSA  @BlackHatEvents

96

## Slide 97

# Conclusions

- › CVSS can be a little obscure.

- › NO need to be an expert in the field to carry out a research project.

- › Proprietary protocol ? Only few information ? Don’t be afraid.

- › Don’t pursue the silver bullet, it could be frustrating.

#BHUSA  @BlackHatEvents

97

## Slide 98

## Thank you !

Pablo Artuso @lmkalg Yvan Genuer linkedin.com/in/1ggy https://www.onapsis.com

#BHUSA   @BlackHatEvents

98

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
plackhat
LISA &
AUGUST 9-10, 20253
BRIEFINGS
Thank you !
Pablo Artuso @Imkalg
Yvan Genuer linkedin.com/in/1ggy
https://www.onapsis.com
‘J ONAPSIS
#BHUSA
@BlackHatEvents
98
```
