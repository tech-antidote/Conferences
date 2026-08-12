---
title: "Open RAN, Open Risk Uncovering Threats and Exposing Vulnerabilities in Next-Gen Cellular RAN"
speakers: ["Tianchang Yang", "Kai Tu", "Syed Md Mukit Rashid", "Ali Ranjbar", "Gang Tan", "Syed Rafiul Hussain"]
conference: "Black Hat"
conference_full: "Black Hat USA 2025"
edition: "USA"
year: 2025
source_pdf: "BlackHat_USA_2025_Slides/Tianchang Yang&Kai Tu&Syed Md Mukit Rashid&Ali Ranjbar&Gang Tan&Syed Rafiul Hussain_Open RAN, Open Risk Uncovering Threats and Exposing Vulnerabilities in Next-Gen Cellular RAN.pdf"
pages: 64
sha256: "4b350d04997e4d25c1819bb0f3290ac9101978d2c99abfac87178ab801a52718"
text_chars: 23802
ocr_pages: 15
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T23:01:55Z"
---
# Open RAN, Open Risk Uncovering Threats and Exposing Vulnerabilities in Next-Gen Cellular RAN

**Speakers:** Tianchang Yang, Kai Tu, Syed Md Mukit Rashid, Ali Ranjbar, Gang Tan, Syed Rafiul Hussain  
**Conference:** Black Hat USA 2025  
**Source:** `BlackHat_USA_2025_Slides/Tianchang Yang&Kai Tu&Syed Md Mukit Rashid&Ali Ranjbar&Gang Tan&Syed Rafiul Hussain_Open RAN, Open Risk Uncovering Threats and Exposing Vulnerabilities in Next-Gen Cellular RAN.pdf` (64 pages)


## Slide 1

# Open RAN, Open Risk: Uncovering Threats and Exposing Vulnerabilities in Next-Gen Cellular RAN

Tianchang Yang, Kai Tu,

Syed Md Mukit Rashid, Ali Ranjbar, Gang Tan, Syed Rafiul Hussain

#BHUSA @BlackHatEvents

## Slide 2

## Introduction

Tianchang Yang

Research Assistant, The Pennsylvania State University Mobile network security, resiliency, and robustness: 5G, Open RAN, baseband

```
tianchang-yang.github.io
```

#BHUSA @BlackHatEvents

## Slide 3

## Introduction

##### Kai Tu

Research Assistant, The Pennsylvania State University Mobile network and Device Security, baseband security, Automatic Vulnerability Discovery

```
hellotkk.github.io
```

#BHUSA @BlackHatEvents

## Slide 4

## Radio Access Network (RAN)

www.anscorporate.com/blog/what-is-a-5g-cell-tower

#BHUSA @BlackHatEvents

## Slide 5

## O-RAN’s Virtualization

the-mobile-network.com/2019/03/taking-the-open-ran-commercial/ the-mobile-network.com/2019/03/open-ran-at-the-tip-ping-point/

#BHUSA @BlackHatEvents

## Slide 6

## Evolution of Mobile RAN

Mainframe of  Specialized
specialized  hardware,
hardware servers, switches
SDN
1960-1970 ~2010
Programs
Simple
running on
programmable
modularized
switches
hardware

Vendor-provided cell equipment

Virtualized, cloudnative RAN on commodity servers

#BHUSA @BlackHatEvents

## Slide 7

## 4G and Before RAN

#BHUSA @BlackHatEvents

## Slide 8

## 4G and Before RAN

Cell
Mobile
Cell
RAN

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ap)
o)
=
LL
Lu
oc
an}
0
&
3
Cg
fe}
ere
JS
o. U Ol>
Z|8|Yl</z lu e/YiIYj<zlz le
w2/O/;/e/s/la Cre |*¥ 1S]
—— ——
Aon”
```

## Slide 9

## Mobile Network’s Transition to 5G

Radio  Distributed
Unit
Unit (DU)
(RU)
Central
Radio
Unit (CU) 5G
Unit
(RU) RAN

#BHUSA @BlackHatEvents

## Slide 10

## Mobile Network’s Transition to 5G

Radio  Distributed
Unit
Unit (DU)
(RU)
Central
Radio
Unit (CU) 5G
Unit
(RU) RAN

#BHUSA @BlackHatEvents

## Slide 11

## Introduction of O-RAN

RAN Intelligent
Controller (RIC)
Non-RT RIC (SMO)
Policy, Configurations, AI/ML
RU
DU
rApps (> 1s)
Near-RT RIC
Control, Optimization
xApps (10 ms – 1s)
CU
RU
5G
RAN #BHUSA @BlackHatEvents

#BHUSA @BlackHatEvents

## Slide 12

## Introduction of O-RAN

RAN Intelligent
Controller (RIC)
Non-RT RIC (SMO)
Policy, Configurations, AI/ML
RU
DU
rApps (> 1s)
Near-RT RIC
Control, Optimization
xApps (10 ms – 1s)
CU
RU
5G
RAN #BHUSA @BlackHatEvents

#BHUSA @BlackHatEvents

## Slide 13

## O-RAN RIC Architecture

Near-RT RIC
xApp 1 xApp 2 . . . xApp N
Internal Messaging System
Conflict Subscription . . .
SDL
Mitigation Management
E2 Termination (E2T)
E2 Interface
RAN
O-CU O-DU O-RU

#BHUSA @BlackHatEvents

## Slide 14

## O-RAN RIC Architecture

Near-RT RIC **Traffic steering, power optimization,** xApp 1 xApp 2 **. . .** xApp N **network slice management …** Internal Messaging System Conflict Subscription **. . .** SDL Mitigation Management E2 Termination (E2T) E2 Interface RAN O-CU O-DU O-RU

#BHUSA @BlackHatEvents

## Slide 15

## O-RAN RIC Architecture

Near-RT RIC xApp 1 xApp 2 **. . .** xApp N Internal Messaging System **Service-** Conflict Subscription **. . . Based** SDL Mitigation Management **Architecture** E2 Termination (E2T) E2 Interface RAN O-CU O-DU O-RU

#BHUSA @BlackHatEvents

## Slide 16

## O-RAN RIC Architecture

Near-RT RIC
xApp 1 xApp 2 . . . xApp N
Internal Messaging System
Conflict RAN Control Message Subscription . . .
SDL
Mitigation Management
E2 Termination (E2T)
Throughput, traffic
E2 Interface
etc…
volume, SNR, RSRP,
RAN
O-CU O-DU O-RU

#BHUSA @BlackHatEvents

## Slide 17

## Evolution of Mobile RAN

Mainframe of  Specialized
specialized  hardware,
hardware servers, switches
SDN
1960-1970 ~2010
Programs
Simple
running on
programmable
modularized
switches
hardware

Vendor-provided cell equipment

Virtualized, cloudnative RAN on commodity servers

#BHUSA @BlackHatEvents

## Slide 18

### **Are O-RAN already in use?**

Major operators still opting for single vendor, small or private operators benefiting first

**Will** **_everyone_ move to O- RAN eventually?**

Maybe not every O-RAN promise... But with AI/ML/LLM booming, cloud-native RAN is inevitable.

#BHUSA @BlackHatEvents

## Slide 19

## Threat Demonstration – Malicious User

Near-RT RIC
. . .
xApp 1 xApp 2 xApp N
Internal Messaging System
Conflict Subscription
SDL . . .
Mitigation Management
E2 Termination (E2T)
E2 Interface
RAN
O-CU O-DU O-RU

#BHUSA @BlackHatEvents

## Slide 20

## O-RAN Vulnerability Sources

##### Malicious User

#BHUSA @BlackHatEvents

## Slide 21

#BHUSA @BlackHatEvents

Attacks on 5G Infrastructure from Users’ Devices www.trendmicro.com/en_us/research/23/i/attacks-on-5g-infrastructure-from-users-devices.html

## Slide 22

#BHUSA @BlackHatEvents

RRC Signaling Storm Detection in O-RAN arxiv.org/abs/2504.15738

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
biSekhat
BRIEFINGS
1V > cs > arXiv:2504.15738
Computer Science > Cryptography and Security
(Submitted on 22 Apr 2025]
RRC Signaling Storm Detection in O-RAN
Dang Kien Nguyen, Rim El Malki, Filippo Rebecchi
The Open Radio Access Network (O-RAN) marks a significant shift in the mobile network industry. By transforming a traditionally vertically integrated architecture into an
open, data-driven one, O-RAN promises to enhance operational flexibility and drive innovation. In this paper, we harness O-RAN's openness to address one critical threat to
5G availability: signaling storms caused by abuse of the Radio Resource Contral (RRC) protocol. Such attacks occur when a flood of RRC messages from one or multiple User
Equipments (UEs) deplete resources at a 5G base station (gNB), leading to service degradation. We provide a reference implementation of an RRC signaling storm attack, using
the OpenAirinterface (OAI) platform to evaluate its impact on a gNB. We supplement the experimental results with a theoretical model to extend the findings for different load
conditions. To mitigate RRC signaling storms, we develop a threshold-based detection technique that relies on RRC layer features to distinguish between malicious activity
and legitimate high network load conditions. Leveraging O-RAN capabilities, our detection method is deployed as an external Application (xApp). Performance evaluation
shows attacks can be detected within 90ms, providing a mitigation window of 60ms before gNB unavailability, with an overhead of 1.2% and 0% CPU and memory
consumption, respectively.
Comments: Accepted to IEEE ISCC 2025
Subjects: Cryptography and Security (cs.CR); Networking and Internet Architecture (cs.NI)
Cite as: arxiv:2504.15738 [es.CR]
(or arXiv:2504.1573 8v1 [es.CR] for this version)
https://doi.org/10.48550/arxiv.2504.15738 e
RRC Signaling Storm Detection in O-RAN
arxiv.org/abs/2504.15738
```

## Slide 23

## Threat Demonstration – Supply Chain Risks

Near-RT RIC
. . .
xApp 1 xApp 2 xApp N
Internal Messaging System
Conflict Subscription
SDL . . .
Mitigation Management
E2 Termination (E2T)
E2 Interface
RAN
O-CU O-DU O-RU

#BHUSA @BlackHatEvents

## Slide 24

## O-RAN Vulnerability Sources

Malicious User Supply Chain Risk

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
BRIEFINGS
O-RAN Vulnerability Sources
y-2)
.S
&
&
.
(Che
Malicious User Supply Chain Risk
```

## Slide 25

#BHUSA @BlackHatEvents

Securing Telecom Supply Chains: Mitigating Risks in the Telecom Ecosystem www.p1sec.com/blog/securing-telecom-supply-chains-mitigating-risks-in-the-telecom-ecosystem

## Slide 26

## Threat Demonstration – Heterogeneous RAN

Near-RT RIC
. . .
xApp 1 xApp 2 xApp N
Internal Messaging System
Conflict Subscription
SDL . . .
Mitigation Management
E2 Termination (E2T)
E2 Interface
RAN
O-CU O-DU O-RU

#BHUSA @BlackHatEvents

## Slide 27

## O-RAN Vulnerability Sources

Malicious User

Supply Chain Risk

Heterogeneity of RAN Nodes

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
€Q
black hat
BRIEFINGS
O-RAN Vulnerability Sources
v-2)
.S
&
&
.
(Che
Malicious User Supply Chain Risk
Heterogeneity of
RAN Nodes
```

## Slide 28

## O-RAN Vulnerability Sources

Malicious User

Heterogeneity of Supply Chain Risk RAN Nodes

O-RAN Study on Security for Near Real Time RIC and xApps www.o-ran.org/specifications

#BHUSA @BlackHatEvents

## Slide 29

## Threat Demonstration – Cloud Tenants

Near-RT RIC
. . .
xApp 1 xApp 2 xApp N
Internal Messaging System
Conflict Subscription
SDL . . .
Mitigation Management
E2 Termination (E2T)
E2 Interface
RAN
O-CU O-DU O-RU

#BHUSA @BlackHatEvents

## Slide 30

## Threat Demonstration – Cloud Tenants

Near-RT RIC
. . .
xApp 1 xApp 2 xApp N
Internal Messaging System
Conflict Subscription
SDL . . .
Mitigation Management
E2 Termination (E2T)
E2 Interface
RAN
O-CU O-DU O-RU

#BHUSA @BlackHatEvents

## Slide 31

## O-RAN Vulnerability Sources

Malicious User

Supply Chain Risk

Heterogeneity of

RAN Nodes

Cloud Tenants

#BHUSA @BlackHatEvents

## Slide 32

## O-RAN Vulnerability Sources

### Malicious User

### Heterogeneity of RAN Nodes

#BHUSA @BlackHatEvents

## Slide 33

• Identified **19 flaws** in RIC components and xApps that can lead to DoS of the RIC, and **7 flaws** in CU components that can lead to DoS of the whole cell.

- **22 CVEs** have been assigned to track all 26 issues.

   - CVE-2023-52724, -52725, -52726, -52727, -52728

   - CVE-2024-25377, -29420, -34043, 34044, -34045, -34046, -34047, -34048,

-34049, -34050, -57330, -57331, -57332, -57333, 57334

- CVE-2025-45420, -45421

#BHUSA @BlackHatEvents

## Slide 34

###### Assertion Failures

###### Memory Issue

###### Runtime Panic

###### Logical Error

- CVE-2024-57330 (OAI DU)

- CVE-2024-57331 (OAI CU)

- CVE-2024-57332 (OAI CU)

- CVE-2024-57333 (OAI CU)

- CVE-2025-45421 (OAI CU)

- CVE-2024-57334 (OAI CU)

- CVE-2025-45420 (OAI CU)

- CVE-2024-34043 (ORAN-SC Dependency)

- CVE-2024-34044 (ORAN-SC E2T)

- CVE-2024-25377 (ORAN-SC xApp)

- CVE-2024-34047 (ORAN-SC E2Manager)

- CVE-2024-34048 (ORAN-SC E2Manager)

- CVE-2025-30077 (SD-RAN Dependency)

- CVE-2023-52727 (SD-RAN Dependency)

- CVE-2023-52728 (SD-RAN Dependency)

      - CVE-2023-52726 (SD-RAN xApp)

      - CVE-2023-52725 (SD-RAN xApp)

   - CVE-2024-29420 (ORAN-SC xApp)

- CU/DU

- • RIC Platforming/Dependency

- • RIC xApp

- CVE-2024-34049 (SD-RAN xApp)

- CVE-2024-34050 (SD-RAN xApp)

- CVE-2023-52724 (SD-RAN xApp)

#BHUSA @BlackHatEvents

## Slide 35

- Assertion Failures Memory Issue Runtime Panic

- • CVE-2024-57330 • CVE-2024-57334 • CVE-2024-34047 (O(OAI DU) (OAI CU) RAN-SC E2Manager)

- • CVE-2024-57331 • CVE-2025-45420 • CVE-2024-34048 (O(OAI CU) (OAI CU) RAN-SC E2Manager)

Logical Error

• CVE-2023-52726 (SD-RAN xApp) • CVE-2023-52725 (SD-RAN xApp)

- CVE-2024-57332 • CVE-2024-34043 (O• CVE-2025-30077 (OAI CU) RAN-SC Dependency) (SD-RAN Dependency)

- • CVE-2024-57333 • CVE-2024-34044 (O• CVE-2023-52727 (OAI CU) RAN-SC E2T) (SD-RAN Dependency)

- • CVE-2025-45421 • CVE-2024-25377 (O• CVE-2023-52728 (OAI CU) RAN-SC xApp) (SD-RAN Dependency)

code • CU/DU • RIC Platforming/Dependency • RIC xApp

- CVE-2024-29420 (ORAN-SC xApp)

- CVE-2024-34049 **_Dependency management:_**

- (SD-RAN xApp)

- • CVE-2024-34050 **In-house:** buggy, undertested (SD-RAN xApp)

- • CVE-2023-52724 **Third-party:** security, backdoor (SD-RAN xApp)

#BHUSA @BlackHatEvents

## Slide 36

Assertion Failures Memory Issue Runtime Panic Logical Error • CVE-2024-57330 • CVE-2024-57334 • CVE-2024-34047 (O• CVE-2023-52726 (OAI DU) (OAI CU) RAN-SC E2Manager) (SD-RAN xApp) • CVE-2024-57331 • CVE-2025-45420 • CVE-2024-34048 (O• CVE-2023-52725 (OAI CU) (OAI CU) RAN-SC E2Manager) (SD-RAN xApp) • CVE-2024-57332 • CVE-2024-34043 (O• CVE-2025-30077 (OAI CU) RAN-SC Dependency) (SD-RAN Dependency) • CVE-2024-57333 • CVE-2024-34044 (O• CVE-2023-52727 (OAI CU) RAN-SC E2T) (SD-RAN Dependency) • CVE-2025-45421 • CVE-2024-25377 (O• CVE-2023-52728 (OAI CU) RAN-SC xApp) (SD-RAN Dependency) • CVE-2024-29420 (ORAN-SC xApp) • CVE-2024-34049 • CU/DU (SD-RAN xApp) • RIC Platforming/Dependency • CVE-2024-34050 (SD-RAN xApp) • RIC xApp • CVE-2023-52724 (SD-RAN xApp)Vulnerable Cgo call

#BHUSA @BlackHatEvents

## Slide 37

## Are Commercial O-RAN Systems Safe?

- Closed-source API testing

- Zero-trust design

- 4 implementation-level issue

- Long requests, unexpected formats (json when string expected)

- **Openness & virtualization creates opportunity, but also vulnerability**

#BHUSA @BlackHatEvents

## Slide 38

## Limitations of Existing Testing Approaches

#### • Existing tools (AFLNET, BooFuzz, Restler, Frizzer) test **one program** at a time

Near-RT RIC
. . .
xApp 1 xApp 2 xApp N
Internal Messaging System
Conflict . . .
Subscription
SDL
Mitigation Management
E2 Termination (E2T)

#BHUSA @BlackHatEvents

## Slide 39

## Limitations of Existing Testing Approaches

- Existing tools (AFLNET, BooFuzz, Restler, Frizzer) test **one program** at a time

- Requires details about the **expected message, dependencies, protocols, …**

- • **Internal details vary across different implementations**

xApp 1
Message Format?
Protocol?
Reception Point? Test Input
Fuzzer

#BHUSA @BlackHatEvents

## Slide 40

## Limitations of Existing Testing Approaches

• Existing tools (AFLNET, BooFuzz, Restler, Frizzer) test **one program** at a time

- Requires details about the **expected message, dependencies, protocols, …**

- **Internal details vary across different implementations**

xApp 2
Message Format? Subscription
Protocol?
Management
Reception Point? Test Input
Message Format?
Protocol?
Fuzzer
Reception Point? Test Input
Fuzzer
RIC2’s
xApp 1
E2T
Message Format?
Protocol?
Reception Point? Test Input
Test Input
Fuzzer
Fuzzer

E2T
Message Format?
Protocol?
Reception Point?
Test Input
Fuzzer

xApp 1 Message Format? Protocol? Reception Point? Test Input Fuzzer

**…**

#BHUSA @BlackHatEvents

## Slide 41

## Our Approach: End-to-End Testing

- Send test inputs only through public interface.

- Automatic test generation for the **standardized protocol**

- **Scalable** to all implementations

- All found bugs are exploitable from a misbehaving RAN

Near-RT RIC
. . .
xApp  1 xApp 2 xApp N
Internal Mess aging System
Conflict Subscription
SDL . . .
Mitigation Management
E2 Termination (E2T)
E2 interface

Test Input

#BHUSA @BlackHatEvents

## Slide 42

## Problem Formulation

Near-RT RIC
Target xApp
. . .
xApp  1 xApp 2 xApp N
Internal Mess aging System
Internal Routing
Conflict Subscription
SDL . . .
Mitigation Management
E2 Termination (E2T)
E2T
E2 interface
Test
Test
Input
Input

#BHUSA @BlackHatEvents

## Slide 43

## Challenge 1: Generating Targeted and Meaningful Test Inputs

Target xApp
Internal Routing
E2T

Test Input

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
A~\ i, aaeiy y/ : : > < by aa
bi§ekhat a, Sa f f-. J :
BRIEFINGS U, \ y |
Challenge 1: Generating Targeted and Meaningful Test Inputs
var requestID int32
for _, v := range request.GetProtocolles() { Target xApp
if v.Id == int32(v2.ProtocolleIDRicrequestID) {
requestID = v.GetValue().GetRicrequestId().GetRicRequestorId()
break
} Internal Routing
}
streamID := stream. ID(requestID)
stream, ok := c.streams.Get(streamID)
if !ok {
return errors.NewNotFound("stream %s not found", streamID)
}
```

## Slide 44

## Challenge 1: Generating Targeted and Meaningful Test Inputs

- **Challenge:** generate inputs that can **reach the target** components (avoid under-constraint) while **maintain variability** for effective testing (avoid over-constraint).

Target xApp
Internal Routing
E2T

Test Input

#BHUSA @BlackHatEvents

## Slide 45

## Solution 1: Layered Testing Approach

- **Layered approach:**

   - First test the component connected with E2: E2T

   - Gradually move to deeper components

   - At each component, find appropriate constraints so the test inputs can reach the next component.

Target xApp

**Dynamic Tracing**

Internal Routing

**Dynamic Tracing**

E2T

- **Challenge:** How can we find these **layerdependencies** between components?

- • **Solution: Dynamic tracing**

**Dynamic Tracing**

Test Input

#BHUSA @BlackHatEvents

## Slide 46

## Challenge 2: Enumerate Appropriate Constraints

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
QQ
black hat iS = <q Yy
BRIEFINGS — g YK 8 VA
Challenge 2: Enumerate Appropriate Constraints
Dependency (9) Benign (9)
Analysis RANs A
Pp .
Source (Preprocessing) Instrumented
Code Code ) RIC Deployment |Operation Trace
= Instrumentor | af at a Analyzer
( e} { e}[ e}
ntry/Exit Points Component
| Initial Corpus ependency
v
```

## Slide 47

## Scalability Challenges in Static Analysis

Target xApp
Exit
Static
Intern al Routing
Analysis
Entry
Exit
Static
Analysis E2T
Entry
Test
Input

#BHUSA @BlackHatEvents

## Slide 48

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
blackhat
BRIEFINGS
GitHub v
B® Goi XML
Files
onosproject/onos-e2t
master
ignore files/dirs comma separated
Lines Blanks
330 661435 94163
Protocol Buffers | Markdown H YAML
Shell H Dockerfile HM Makefile = Plain Text
Comments
76801
Lines of Code
490471
#BHUSA @BlackHatEvents
```

## Slide 49

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
biSekhat
BRIEFINGS
Onos—e2t % grep -Er -—-exclude-dir={test,api} \
'A\s*func\st+(\( [*\) ]*\)\sx*) ? [a-zA-Z_] [a-zA-Z0-9_]*\sx*\(' \
-/ | we -l
```

## Slide 50

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
biSekhat
BRIEFINGS
onos-—e2t % grep —Er |--exclude-dir={test,api}| \
'A\ sxfunc\st(\( [*\) ]*\)\sx*) ? [a-zA-Z_] [a
./ | we -l
6152
```

## Slide 51

# Challenge & Solution 3: Efficient Static Analysis

##### **Solution:**

- Program Dependency Graph (PDG)-based view of control dependencies to find critical conditions

- Backward dataflow analysis to generate constraints on the input message

- **Selectively analyze** functions validating inputs, ignoring generic functions (e.g., network operations, data retrieval)

#BHUSA @BlackHatEvents

## Slide 52

## How to Discern Generic/Validating Functions?

• Name?

• LLM?

• Control Flow?

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
biSekhat N a y y 2
,
BRIEFINGS app Xa y | J
How to Discern Generic/Validating Functions? .
we ween en ++ eee een = ee 2 ee eee en ee ee eee ee eee ere
AssociateRanToE2THandlerImpl(data models.RanE2tMap) error {
DisassociateRanToE2THandlerImpl(data models.RanE2tMap) error {
DeleteE2tHandleHandlerImpl(data *models.E2tDeleteData) error {
DumpDebugData() (models.Debuginfo, error) {
e N ] httpGetXApps(xmurl string) (*[]rtmgr.XApp, error) {
ai } 1e e httpGetE2TList(e2murl string) (*[]rtmgr.E2tIdentity, error) {
PopulateE2TMap(e2tDataList *[]rtmgr.E2tIdentity, e2ts map[string] rtmgr.E2TInstance,
retrieveStartupData(xmurl string, nbiif string, fileName string, configfile string,
(r *HttpRestful) Initialize(xmurl string, nbiif string, fileName string, configfile|
e [ LM2 (r *HttpRestful) Terminate() error {
e addSubscription(subs *rtmgr.SubscriptionList, xappSubData *models.XappSubscriptionD|
delSubscription(subs *rtmgr.SubscriptionList, xappSubData *models.XappSubscriptionD|
updateSubscription(data *xrtmgr.XappList) {
PopulateSubscription(sub_list xfmodel.SubscriptionList) {
e@ ontro F OW Adddelrmrroute(routelist models.Routelist, rtflag bool) error {
e checkrepeatedroute(data string) bool {
NewHttpGetter() +*HttpGetter {
fetchAlLUApps(xmurl string) (*[]rtmgr.XApp, error) {
(g *HttpGetter) Initialize(xmurl string, nbiif string, fileName string, configfile
(g *HttpGetter) Terminate() error {
LaunchRest(nbiif string) {
NewFile() xFile {
(f *File) ReadAll(file string) (*rtmgr.RicComponents, error) {
(f *File) WriteAll(file string, rcs *rtmgr.RicComponents) error {
(f *File) WriteXApps(file string, xApps *[]rtmgr.XApp) error {
(f *File) WriteNewE2TInstance(file string, E2TInst *rtmgr.E2TInstance, meiddata str|
(f *File) WriteAssRANToE2TInstance(file string, rane2tmap models.RanE2tMap) error {
(f *File) WriteDisAssRANFromE2TInstance(file string, disassranmap models.RanE2tMap)
(f *File) WriteDeleteE2TInstance(file string, E2TInst xmodels.E2tDeleteData) error
GetSd1(sdlName string) (Engine, error) {
(params *RMRParams) String() string {
NewRmrPush() *RmrPush {
(c *RmrPush) Initialize(ip string) error {
(c *RmrPush) Terminate() error {
(c *RmrPush) AddEndpoint(ep xrtmgr.Endpoint) error {
(c *RmrPush) DeleteEndpoint(ep *rtmgr.Endpoint) error {
(c *RmrPush) UpdateEndpoints(rcs *rtmgr.RicComponents) {
(c *RmrPush) DistributeAll(policies *[]string) error {
(c *RmrPush) send_sync(ep *rtmgr.Endpoint, policies *[]string, call_id int) {
(c *RmrPush) send_data(ep *rtmgr.Endpoint, policies *[]string, call_id int) bool {
(c *RmrPush) CheckEndpoint(payload string) (ep *rtmgr.Endpoint) {
(c *RmrPush) CreateEndpoint(rmrsrc string) (ep *string, whid int) {
(c uRmrPiich) DictrihiuteToabni(nnliciec «f[letring. en ctringn. whid int) error Jf
```

## Slide 53

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
295 func CreateNewE2tHandleHandlerImpl(data *models.E2tData) error { & w httprestful.go pkg/nbi 3
329
330 return errors.New("Error while adding new E2T " + *data.E2TAddre: func Selita ise eee
331 err := validateE2TAddressRANLis!
332} err := validateE2TAddressRANLis'
es VY httprestful_test.go pkg/nbi 2
334 func ValidateE2TAddressRANListData(assRanE2tData models.RanE2tMap) e : -
335 err := validateE2TAddressRANLisi
336 xapp.Logger.Debug("Invoked.validateE2TAddressRANListData : %v", i err = validateE2TAddressRANList
337
338 for _, element := range assRanE2tData {
339 if *element.E2TAddress == "" {
client.go /usr/local/go/src/net/http - References (5) x
478 // To make a request with custom headers, use [NewRequest] and [Cliq © httpgetter.go pkg/nbi 1
479 // myClient.Get(xmurl)
480 // To make a request with a specified context.Context, use [NewReque .
481 // and Client.Do. ¥ Hite 2 pkg/nbi 2
482 func (c *Client) Get (url string) (resp *Response, err error) { myClient.Get(xmurl)
483 req, err := NewRequest("GET", url, nil) a myClient.Get(e2murl)
484 if err != nil { Y client.go /usr/local/go/src/net...(2
485 return nil, err faultCl '
486 } DefaultClient.Get (url)
487 return c.Do(req) Client) Get(url string) (resp *Resp
488 }
Aaa
```

## Slide 54

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
VY httpgetter.go pkg/nbi
myClient.Get(xmurl)
Y httprestful.go pkg/nbi
myClient.Get(xmurl)
myClient.Get(e2murl)
Y client.go /usr/local/go/src/net...\ 2
DefaultClient.Get (url)
Client) Get(url string) (resp *Resy
```

## Slide 55

## Architecture

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
BRIEFINGS
Architecture
Static
Analysis
Constraints
```

## Slide 56

## Architecture

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
biSekhat
BRIEFINGS
Architecture
epen ency (®) Benign () J Runtime Analysis
Analysis RIC :
Pp ' RANs Deploymen (Testing)
Source (Preprocessing) Instrumented sa ea Ge
Code RIC Deployment Operation Trace a ee .
a | ey) cy) C- Monitor
a) | | Analyzer I | : |
a |
Component E2T Crashing
dency Inputs &
es, Passa) 2222 snes eas of Oe i Crash
Static Path Message Generated Input Test (¢ )) Input i Logs
Analysis Constraints Mutator Test Input Scheduler Input Sender »
en 1 }
. ( \ 1 J
Testing Input ASN.1 Message Fitness Feedback L. Code Coverage ; dy
Generation if Definition Score Collector Feedback \
ee ee ee ee a ee !
```

## Slide 57

## RAN Vulnerability Demo

Near-RT RIC
. . .
xApp 1 xApp 2 xApp N
Internal Messaging System
Conflict Subscription
Mitigation Management SDL . . .
E2 Termination (E2T)
E2 Interface
RAN
O-CU O-DU O-RU

#BHUSA @BlackHatEvents

## Slide 58

Demo: Malicious UE crashing the whole RAN/cell

#BHUSA @BlackHatEvents

## Slide 59

## RIC Vulnerability Demo

Near-RT RIC
. . .
xApp 1 xApp 2 xApp N
Internal Messaging System
Conflict Subscription
Mitigation Management SDL . . .
E2 Termination (E2T)
E2 Interface
RAN
O-CU O-DU O-RU

#BHUSA @BlackHatEvents

## Slide 60

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ifiv + jo) o
Foot@tianchang-Ubuntu: /home/tianchang#
Tilix: Default
root@tianchang-Ubuntu: /home/tianchang/Desktop/proj/daikon/osc/sim-e
Ht
Tianchang Yang
Benign RAN
root@tianchang-Ubuntu: /home/tianchang/Desktop/proj/daikon/osc/sim-e2-interface/e2sinm
Attacking RAN
```

## Slide 61

## Final Thoughts

• O-RAN introduces expanded **attack surfaces** and more likely for a bug to cascade into **system-wide disruption** • Read the specs. Dive into the code. Contribute.

#BHUSA @BlackHatEvents

## Slide 62

## Final Thoughts

• O-RAN introduces expanded **attack surfaces** and more likely for a bug to cascade into **system-wide disruption**

• Read the specs. Dive into the code. Contribute.

O-RAN Software Community Releases “L”: Boosting Integration, AI/ML, and Open Source Collaboration o-ran-sc.org/blog/2025/07/24/o-ran-software-community-releases-l-boosting-integration-ai-ml-and-open-source-collaboration/ #BHUSA @BlackHatEvents

## Slide 63

## Final Thoughts

• O-RAN introduces expanded **attack surfaces** and more likely for a bug to cascade into **system-wide disruption** • Read the specs. Dive into the code. Contribute. • Think broader: side channel, privacy leaks, flooding, …

#BHUSA @BlackHatEvents

## Slide 64

## Thank You!

Tianchang Yang tzy5088@psu.edu tianchang-yang.github.io Kai Tu kjt5562@psu.edu hellotkk.github.io

Syed Md Mukit Rashid, Ali Ranjbar, Gang Tan, Syed Rafiul Hussain

Paper

Code

#BHUSA @BlackHatEvents
