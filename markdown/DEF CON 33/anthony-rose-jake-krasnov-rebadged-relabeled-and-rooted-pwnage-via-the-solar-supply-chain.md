---
title: "Rebadged, Relabeled, and Rooted Pwnage via the Solar Supply Chain"
speakers: ["Anthony Rose Jake Krasnov"]
conference: "DEF CON"
conference_full: "DEF CON 33"
edition: "33"
year: 2025
source_pdf: "DEF CON 33/Anthony Rose Jake Krasnov - Rebadged, Relabeled, and Rooted Pwnage via the Solar Supply Chain.pdf"
pages: 78
sha256: "a5b0bf6d594220818cc8571213a14a6a9a822357a050006f4f3735ee3084cb16"
text_chars: 35768
ocr_pages: 32
has_ocr: true
redacted_secrets: 0
ocr_confidence: 86.9
ocr_unreliable_blocks: 3
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T06:53:35Z"
---
# Rebadged, Relabeled, and Rooted Pwnage via the Solar Supply Chain

**Speakers:** Anthony Rose Jake Krasnov  
**Conference:** DEF CON 33  
**Source:** `DEF CON 33/Anthony Rose Jake Krasnov - Rebadged, Relabeled, and Rooted Pwnage via the Solar Supply Chain.pdf` (78 pages)


## Slide 1

Rebadged, Relabeled, and Rooted: Pwnage via the Solar Supply Chain

@bcsecurity

1

## Slide 2

## whoami

##### **Jake Krasnov**

Red Team Ops Lead CEO

###### **Expertise**

- Red Team Operations

- Embedded Systems Engineering

- AV/EDR Evasion

- Operational Technologies (this talk)

###### **Education**

- United States Air Force Academy – B.S. Astronautical Eng

- Colorado College – MBA

2

## Slide 3

## whoami

##### **Anthony Rose**

Director, Security Research - BC Security Assistant Professor, Air Force Institute of Technology

###### **Expertise**

- Wireless System Security

- System Engineering Risk Assessments

- IT System Security

- Artificial Intelligence / Machine Learning

###### **Education**

- Arizona State University – B.S. Electrical Engineering

- Air Force Institute of Technology – MSEE

- Air Force Institute of Technology – PhD

3

## Slide 4

## Solar is now Global

- 25 Million homes now have solar

   - Projected to reach 100M by 2030

- Accounted for 10% of global energy production in April

4

## Slide 5

## What is a Microgrid?

- Made up of a system that performs 5 critical functions

   - Energy Generation

   - Energy Storage

   - Energy Management

   - Energy Distribution

   - Grid Isolation

5

## Slide 6

## As Solar explodes so do smart devices

- Smart Inverters

- Smart Batteries

- Remote monitoring

- • Web Applications

6


> Recovered by OCR — confidence 82/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
As Solar explodes so do smart devices
¢ Smart Inverters 7 = -_
¢ Smart Batteries Automation: Sustainable Living
¢ Remote monitoring
¢ Web Applications
```

## Slide 7

## Smart Devices

7


> Recovered by OCR — confidence 89/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Smart Devices
EGy Smart Monitoring Communication Path
Remote Monitoring, Diagnostics & Firmware Updates
Ethernet or Wi-Fi
REMOTE ACCESS
ANYWHERE AT ANY TIME
€G4 Smart Monitoring
REAL-TIME offers the most advanced
inverter management
TS4
ADJUSTMENTS software available.
Using the EG4's :
mountable Wi-Fi device Wireless:
FIRMWARE UPDATES iptional levice), |
—: remotely access and TSA 10154, RS485 Communication Cable
manage your 6000XP unit. - 1S4 to TAP
LIVE & HISTORICAL DATA
INVERTER ELECTRICAL
SOLAR PANELS MPPT BATTERY
NETWORK
MULTIPLE
PROTOCOLS
MONITORING
DASHBOARD
MANAGEMENT
‘APPLICATION
```

## Slide 8

## China in the Lead

- China is the leading manufacturer of solar technology

- Highest installed solar capacity

- Many Western “manufacturers” are simply relabeling products

- EG4 is just rebranded LuxPower

   - Sol-Ark is just rebranded Deye

- This carries over to software as well

8

## Slide 9

## Lots of Vulns

- EG4/LuxPower

   - Serial Number Enumeration

   - PIN Enumeration

      - Power Packet

         - Unauthenticated Dashboard access

   - Account Takeover

   - Unsigned Firmware

- Tigo

   - Hard Coded Credentials

   - Unsigned Firmware

   - Command Injection

   - Insecure Key Generation

9

## Slide 10

## Why this should scare you

- Gateways to our homes

- Pattern of life data

- Physical effects

- • Opaque supply lines

10

## Slide 11

The Global Solar Supply Chain Dumpster Fire

## Slide 12

Supply Chains are a Muddled Mess • Companies claim to make everything in the US, but an investigation reveals this to likely not be true

12

## Slide 13

## Sol-Ark

- Rebadged Deye inverters

   - Does not manufacture them

- Until Mid 2024 all data was sent to China

   - Now at least it goes to an AWS gateway

https://www.trendmicro.com/vinfo/us/security/news/security-technology/distributed-energy-generation-gateway-insecurity

13

## Slide 14

## Sol-Ark (We Will Come Back to This)

14


> Recovered by OCR — confidence 95/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Sol-Ark (We Will Come Back to This
SolarPowerSimo
n
VP of Sol Ark
Marketing
Nov 18, 2024
S; 3
Fort Worth
Good day everyone, my name is Simon McLean and | work as VP of Marketing at Sol-Ark. | have the following response to the reports which came up
over the week-end.
Sol-Ark has learned of the situation caused by the unauthorized sales of Deye-branded inverters within Puerto Rico and the USA. Though Sol-Ark has no
control over Deye’s actions, we recognize that the messaging conveyed through the Deye-branded inverter's screen suggests Sol-Ark can provide
warranty or service for these cases, which we cannot. Though we are not responsible for Deye-branded inverters or any inverters that are not branded and
sold by Sol-Ark or through an authorized Sol-Ark distributor or reseller, Sol-Ark has determined to offer a possible solution to those consumer
households that have purchased Deye-branded inverters.
Sol-Ark’s mission, as a veteran-owned company created 12 years ago, is to enable the most reliable, innovative, and affordable energy storage solutions
to power families and businesses. Because of this mission and the direct effect that Deye’s actions may have on individual families, for the period from
November 15, 2024 through December 31, 2024, Sol-Ark will permit each consumer household that has installed a Deye-branded inverter and has had
that inverter’s functions disabled by Deye, to purchase a new Sol-Ark inverter of equivalent performance at a substantially discounted price. If you
purchase a Sol-Ark inverter under this limited program, Sol-Ark will pay to have the Sol-Ark unit shipped to your address in Puerto Rico. Sol-Ark will not
make this offer available to any person after December 31,2024. The offer is limited to consumer households and is not being made available to
commercial entities or for installation at commercial facilities (only residential locations). Sol-Ark will not be responsible, and will not pay, for any costs
related to installation of the Sol-Ark inverter, removal of any Deye inverter or for any damage that may have been caused by the Deye inverter or Deye's
actions.
To take advantage of this offer, the homeowner should take a photo of the serial number and model number of their Deye inverter and then contact
Adriana Navarro of Sol-Ark at +1 (214) 919-1632 to initiate the process during normal business hours between 8 AM and 5 PM Eastern Standard Time
Monday through Friday. Sol-Ark will retain the full right and discretion to make final determinations regarding the availability of this program and the
terms under which it operates.
*@ & T-Rex, sunshine_eggo, baipin and 8 others
```

## Slide 15

## Homegrid

- HomeGrid is a subsidiary of Lithion, which represents itself as a US based battery manufacturer

- Application is hosted by Zruipower, a Chinese based battery backup manufacturer

   - State they are Lithion’s OEM partner

15

## Slide 16

## The Problem isn’t just hardware

- Hardware reuse is a fact of life

   - Very little electronics are manufactured outside the us

   - Often, the best case is assembly in the US

- Software is seeing lots of reuse across organizations

   - Solarman was used by many

   - E-Linter was also popular for web enabled monitoring services

   - A ton of “American” software has Chinese debugging comments

16

## Slide 17

## Lux Power VS EG4 Monitoring Solutions

#### • LuxPower

#### • EG4

17


> Recovered by OCR — confidence 89/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Lux Power VS EG4 Monitoring Solutions
° LuxPower ° EG4
E94 Monitor Center
Monitor Center,
Forget password?
Sign in Register
```

## Slide 18

Cautionary Tale

## Slide 19

## Waking Up to Chaos

- In November, a number of users reported that their inverters were bricked with a message saying to contact:

   - Sol-Ark in the US

   - Sunsynk in the US

- Initially reported as Sol-Ark branded inverters being bricked

19

## Slide 20

## The Picture Coming into Focus

- Turns out it was Deye inverters that were bricked

   - Deye claimed they were illegally sold

   - Sol-Ark and Sunsynk have exclusivity agreements for selling Deye products

- Users that had their devices offline were safe

- Automated firmware updates represent a real risk

   - This is our speculation on how they bricked the inverters

20

## Slide 21

## Restricted Distribution

21


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Restricted Distribution
1 It is strictly prohibited to distribute our energy storage inverter products to the United
Kingdom, Ireland, Spain, Pakistan, Afghanistan, South Africa, Lebanon, the Philippines,
Vietnam, Guam, Yemen, Sri Lanka and other regions, as well as other enterprises or
individuals in China, including direct sales, one or more resales, borrowing, and giving away,
including sending to lithium battery factories for testing and debugging. 2
’ The US version of low-pressure fracture phase energy storage inverter can only be exported to South
America and Central America. It is strictly prohibited to flow to other regions including the United
States, Canada, Puerto Rico, Mexico, etc. in any way, including direct sales, one or more
resales, borrowing, and giving away. 3
```

## Slide 22

## Sol-Ark Sort of Responds

22


> Recovered by OCR — confidence 95/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Sola
Sol-Ark Sort of Responds
rPowerSimo
n
VP of Sol Ark
Marketing
Nov 18, 2024
S; 3
Fort Worth
Good day everyone, my name is Simon McLean and | work as VP of Marketing at Sol-Ark. | have the following response to the reports which came up
over the week-end.
Sol-Ark has learned of the situation caused by the unauthorized sales of Deye-branded inverters within Puerto Rico and the USA. Though Sol-Ark has no
control over Deye’s actions, we recognize that the messaging conveyed through the Deye-branded inverter's screen suggests Sol-Ark can provide
warranty or service for these cases, which we cannot. Though we are not responsible for Deye-branded inverters or any inverters that are not branded and
sold by Sol-Ark or through an authorized Sol-Ark distributor or reseller, Sol-Ark has determined to offer a possible solution to those consumer
households that have purchased Deye-branded inverters.
Sol-Ark’s mission, as a veteran-owned company created 12 years ago, is to enable the most reliable, innovative, and affordable energy storage solutions
to power families and businesses. Because of this mission and the direct effect that Deye’s actions may have on individual families, for the period from
November 15, 2024 through December 31, 2024, Sol-Ark will permit each consumer household that has installed a Deye-branded inverter and has had
that inverter’s functions disabled by Deye, to purchase a new Sol-Ark inverter of equivalent performance at a substantially discounted price. If you
purchase a Sol-Ark inverter under this limited program, Sol-Ark will pay to have the Sol-Ark unit shipped to your address in Puerto Rico. Sol-Ark will not
make this offer available to any person after December 31,2024. The offer is limited to consumer households and is not being made available to
commercial entities or for installation at commercial facilities (only residential locations). Sol-Ark will not be responsible, and will not pay, for any costs
related to installation of the Sol-Ark inverter, removal of any Deye inverter or for any damage that may have been caused by the Deye inverter or Deye's
actions.
To take advantage of this offer, the homeowner should take a photo of the serial number and model number of their Deye inverter and then contact
Adriana Navarro of Sol-Ark at +1 (214) 919-1632 to initiate the process during normal business hours between 8 AM and 5 PM Eastern Standard Time
Monday through Friday. Sol-Ark will retain the full right and discretion to make final determinations regarding the availability of this program and the
terms under which it operates.
*@ & T-Rex, sunshine_eggo, baipin and 8 others
```

## Slide 23

No “Hacking” Needed

## Slide 24

## Packet Power

#### • **Shodan Search:** http.html:pawpow

June 17, 2025

24


> Recovered by OCR — confidence 89/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
¢ Shodan Search: http.html:pawpow
Access Granted: Want to get more out of your existing Shodan account? Check out:
) Loading...
= Thailand, Bangkok
3 a
Thailand
United States
Ireland
United Kingdom TLSv1.2, TLSv1.3
1B roland, Dublin
Communication Authority of BB s
Enet Telecommunications Networks
,
angular.element(function() {
.then(function(response) {
// Expose as a global for debugging purposes and use outside of angular
var _emxChannels = _.get(response, ‘data') || {};
window._emxChannels = _emxChannels;
-always(function() {
angular.bootstrap(document, ['eg4']);
```

## Slide 25

## Packet Power

25


> Recovered by OCR — confidence 82/100 on the text kept, 65/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
System OK
System OK
ea) Readings: 5DC0000000007D79
Power A Current A = Status
@ Monitoring Data
Power Nodes Ye w \ ® Monitoring Data
Channel © Data Processing
Monitoring Nodes
os Energy A 22879325 WI 00:00 2025-02-19 08:43:23
@ Data Destinations
Networking Circuit Type 999 10:19 2025-02-19 08:33:03 Tse D
ee Mesh Join Time 2025-02-17 4 04:52 2025-02-19 08:38:30 License
Logs Mesh Leave Cou 226 1 04:52 2025-02-19 08:38:30
‘Watchdog Mesh Time 1.4 18:04:10 00:00 2025-02-19 08:43:24 Logs
Enors Most Recent Rep 2025-02-19 0 00:00 2025-02-19 08:43:24 Watchdog
Reboot Node Age 0:00:00 e000 2025-42-1908:3.24
Reset Count o1 01:55 2025-02-19 08:41:27 Errors
Reset identifier 2118 01:55 (2025-02-19 08:41:27 Reboot
System Update ®
Update this gateway and/or its library of monitoring node firmware. After you upload the firmware file, the
gateway will automatically detect its content and take the appropriate action. If a system upgrade is initiated, it
may take up to 30 minutes to complete.
Please do not power cycle the device during the upgrade process.
Select an Update File
File: { Choose File | No file chosen
```

## Slide 26

## Packet Power

26


> Recovered by OCR — confidence 89/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
PACKETEG
&
Status
Monitoring Data
Data Sources
Data Processing
Data Destinations
System
System OK
General
System firmware: 3.3.3
Radio firmware: 27.12-E1AF334
GUID: A9E4-0000-0000-0251
Radio zone: EC.1 (20145C1A)
System time: 2025-06-17117:49:55Z
Up-time: 08:55:01
Run 08:51:57
Hostname: PacketPower-A9E4-0000-0000-0251
IP address: 192.168.4228
MAC address: 38:42:69:63:19:02
Stats
‘+ Memory: 84% used (84.1MB free)
* OS storage: 56.48% used (539.5 MB free)
+ Persistent storage: 1.12% used (104.3 MB free)
+ Inbound ethernet data: 29.1 MB
‘+ Outbound ethernet data: 52.6 MB
Licensed Features
* Wireless Mesh
Peer Gateways
Modbus Server
SNMP Server
Virtual Panels
EtherNet/IP
BACnet
MQDD
MATT Transmitter
Debug
Data Sources
Wireless Mesh
View:
device
Peer Gateways
Configure peer g
Data Processing
Virtual Panels
Configure and monitor Virtual Panels
MQDD
Configure MQDD
Data Destinations
EMX Monit:
Configure EM
Data Feed
monitoring data feed
EMX Support Feed
Configure EMX support feed
Modbus
View data exposed via Modbus/ICP
SNMP
View data exposed via SNMP
BACnet
Configure BACnet
EtherNet/IP
Configure EtherNet/IP
MTConnect
Configure MTConnect
MQTTTx
Configure MQTTIX
-ommunicating to this gateway
Status
® Monitoring Data
Data Sources
Data Processing
Data Destinations
® System
Packet Power, LLC © 2015-2025
System Status
General
System firmware:
Radio firmware: N/A
GUID: 6DE4-0100-0000-008D
System time: 2025-02-19714:55:41Z
Up-time: 16 d 06:29:44
Hostname: PacketPower-6DE4-0100-0000-
IP address: 192.168.8.54
MAC address: 98:89:24:2f:d1:b8
Stats
+ Memory: 87% used (69.5MB free)
+ OS storage: 44.28% used (728.9 MB free)
+ Persistent storage: 0.64% used (104.8 MB
free)
+ Inbound ethernet data: 3.3 GB
+ Outbound ethernet data: 1.3 GB
Licensed Features
+ EMX
```

## Slide 27

## Packet Power

27


> Recovered by OCR — confidence 69/100 on the text kept, 67/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Search x Raden
® Monitoring Data
Power Nodes Node F/W Type Product Age Timestamp Source vIP Readings
Env. Nodes
Monitoring Nodes 0710-0000-0000-7301 14.22 Environmental £306 00:00 2025-02-19 11:14:12 Wireless Mesh 192.168.40.111 @
All Node Readings 2200-0000-0001-FAF1 37.10 AC Power PSTIA 00:01 2025-02-19 11:14:11 Wireless Mesh 192.168.40.117 @
2D10-0000-0000-BASC 14.22 Environmental 306 00:01 2025-02-19 11:14:11 Wireless Mesh 192.168.40.114 ®
6A10-0000-0000-72FE 14.22 Environmental £306 00:00 2025-02-19 11:14:12 Wireless Mesh 192.168.40.113 ®
8400-0000-0001-FAES 37.10 AC Power PSTIA 00:00 2025-02-19 11:14:12 Wireless Mesh 192.168.40.121 ®
9410-0000-0000-BASE 14.22 Environmental £306 00:00 2025-02-19 11:14:13 Wireless Mesh 192.168.40.115 ®
CHEER 9B00-0000-0001-FAF3 37.10 AC Power PSTIA 00:02 2025-02-19 11:14:10 Wireless Mesh 192.168.40.118 ®
1D810-0000-0000-7300 14.22 Environmental £306 00:00 2025-02-19 11:14:12 Wireless Mesh 192.168.40.112 @
DC10-0000-0000-B106 32.14 Environmental E300 01:15 2025-02-19 11:12:57 Wireless Mesh 192.168.40.109 ®
£900-0000-0001-FAC3 37.10 AC Power PSTIA 00:01 2025-02-19 11:14:11 Wireless Mesh 192.168.40.120 ®
F700-0000-0001-FBB3 37.10 AC Power PSTIA 00:01 2025-02-19 11:14:11 Wireless Mesh 192.168.40.116 ()
FA00-0000-0001-FAC4 37.10 AC Power PSTIA 00:00 2025-02-19 11:14:13 Wireless Mesh 192.168.40.119 C1)
« << Page 1 off > » FITY 1140814
```

## Slide 28

## Packet Power

28


> Recovered by OCR — confidence 87/100 on the text kept, 81/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
PAG KET EG systemox — System Dashboard CTS vx cwecs © 2025-06-17 13:58:11
Status Module Watchdog
Current
Monitoring Data
Last Reported: 2025-06-17117:58:17.541Z
Data Sources Current Status: Watchdog master:1.1.44:141¢e38+, uptime: 32604s, load: 0.76, 74 resets, most recent: (rebooted by emxDataFeed @ 420943), watching: emx(ACTIVE@32594), modbus(idle@0), snmp(idle@0), peerpoller(idle@0),
madd{idie@0)
Data Processing
History
Data Destinations
System
Dashboard
iene EMX Data Feed EMX Support Feed EMX Syslog
Networking Disabled 846 added to 664536 readings pushed local no messages connected a few seconds ago, 1001 events,
1437 values
Authentication
Security
Radio Zone EtherNet/IP Server Hardware Clock Hub MQDD
C master:1.1.44:141ee38+, disabled Device does not support a battery-backed Disabled (not licensed) edmadd master:1.1.44:141ee38+, disabled
em Update hardware clock
MQTTtx MTConnect Server Modbus server Modbus to MQTT
Errors edmatttx master:1.1.44:141ee38+, 0 readings, edmtc master:1.1.44:141ee38+, 0 readings, 0 listening on port 502 Disabled (not licensed)
a 0 readings/sec readings/sec
Reboot
Factory Reset
Packet Power, LIC €
Module Watchdog NTP Client Network P5 Radio
```

## Slide 29

## Packet Power

- Security is the customer’s responsibility, we are not responsible

29


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
e Security is the customer’s responsibility, we are not responsible
pavie64 2025-06-11 (3 weeks, 4 days ago)
fe Thanks for the information. To be clear the devices that were identified in the
report are NOT supposed to be placed on the publicly accessible networks and
the ones you have identified have been placed on such networks due to user
misconfiguration (basic failure to set access credentials and/or removal of
default credentials). We are contacting the owners of the affected devices but
are not in the position to force them to act if they choose not to. We assume
that whatever is intended to be published would not include their specific IP
addresses. What exactly is intended to be published?
Thanks! Paul | ren |
® 2 replies +
```

## Slide 30

## Packet Power

30


> Recovered by OCR — confidence 90/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
aaa) Authentication
1B Status
Configure the authentication method required to access this device.
@ Monitoring Data
Basic Configuration
Power Nodes
‘Authentication Type:
Monitoring Nodes
None
® Data Sources
© Data Processing
Data Destinations
@ System
Dashboard
Preferences
Networking
Security
Radio Zone
Node Firmware Update
tem Update
Liver
Reboot
Authentication
Configure your desired method of authenticating user access to the Gateway. Multiple options
exist including "None" and "Local Account". To set up local users for access see Adding
Authentication
Authentication
Basic Configuration
Authentication Type:
None v
Save
```

## Slide 31

## Packet Power

31


> Recovered by OCR — confidence 92/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Anthony
Reporter
2025-06-17 (2 weeks, 5 days ago)
We do have customers who require us to allow protection to be removed
(obviously for use on isolated networks). We have no (technical) ability to
prevent them from subsequently placing such devices on public networks. We
strongly recommend that they do not do that, but we have no means of strict
technical (or legal) enforcement. FWIW, almost all devices identified are related
to one particularly irresponsible customer whom we are actively trying to
convince to reconfigure their devices. Thanks! Fest |
® 2 replies v
2025-06-17 (2 weeks, 5 days ago) oe
Here are a few | just pulled.
Thailand (Communication Authority of Thailand) http:/
Ireland (Enet Telecommunications Networks Limited) http:/ EY
Thailand (Provincial waterworks authority) http://
Miami (Cogent Communications) http:/ a /
```

## Slide 32

## Packet Power

32


> Recovered by OCR — confidence 95/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
pavie64 2025-06-11 (3 weeks, 4 days ago)
de We are still not in a position enforce that all the time since some customers
explicitly require us to provide "open" access on locked down (air-gapped)
networks, making fool-proof defaults impossible. Obviously putting these
devices on a public network is a major issue, but short of refusing our
customer's demands we are not in the position to change it. All current devices
are shipped with credentials enabled.
Thanks, Paul Fert |
```

## Slide 33

## Packet Power

33


> Recovered by OCR — confidence 86/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
@ SET IP ADDRESS
totus Configure Reboot shutdown] Setting IP Address Setting Netmask Setting Gateway
. . , * With DHCP turned off, enter the
Documentation / Wireless Gateways / Gateway Configuration IP address, netmask and gateway T
: 7 7 © A temporary IP address can be [DHCP IP Netmask Gateway JOHCP IP Netmask Gateway || DHCP IP Netmask Gateway || DHCP IP Netmask Gateway |
Adding Authentication assigned and modified once you x I
have access to the Gateway. Configure Configure Configure
|. Netmask Gateway IP Netmask Gateway IP Netmask Gateway
The E4 platform supports authentication with a locally stored username and Modifying and Saving Values
password.
> value / status
To enable Authentication
@ ACCESS GATEWAY CONSOLE
System OK
1. Enter the IP address of the E4 device on a browser to access the Gateway
Console: IP ADDRESS
2. Click on the System tab on the console
3. Click on the Authentication tab under the System directory J © Data Processing «From the left hand menu
4. Enter the admin username and password you wish to use to access the E4 < Networning:tab
SWITCH ‘© System
Device in the fields provided. Dashboard
* Access the Gateway Console by entering the Gateway's
IP address onto a web browser. NETWORKING TAR
5. Click on the Save button and the E4 device will warn you that it will need a
Make sure the Gateway and browser are connected to an
accessible switch or router.
restart to enable authentication.
6. Once it finishes rebooting you will be presented with the Login screen to,
access your device.
```

## Slide 34

## Packet Power

34

## Slide 35

## Packet Power

35


> Recovered by OCR — confidence 96/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
pavie64 2025-06-25 (1 week, 4 days ago)
Most of the “potential vulnerabilities” described are related to the scenario
of a user placing any unsecured, control-capable device on a public
network (which all manufacturers of such devices generally advise against
but ultimately have no way of preventing). We strongly believe in
aggressive dissemination of best practices and will be even more vigilant
about it going forward, but we are not in a position to ultimately enforce it
and we do not want generic consequences of violating those practices
(which are true of any product) to be misrepresented as “product flaws”
specific to our product. Actually one of the customers you have identified
has confirmed a far broader network misconfiguration which exposed not
only our device but a number of other, far more critical systems (thank
```

## Slide 36

## Packet Power

#### “no means of strict technical enforcement”

36


> Recovered by OCR — confidence 91/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
“no means of strict technical enforcement”
= PACKET
~ POWER
Login
Credentials
Username @
Forgot your credentials?
```

## Slide 37

OSINT is Fun

## Slide 38

## EG4 – Not a Great Start

38


> Recovered by OCR — confidence 95/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
EG4 — Not a Great Start
EGy ELECTRONICS
4. The configuration parameters used by the dongle when connecting and communicating over
the Wi-Fi network are described below:
4
~
Connected
This is the dongle’s IP address of the when it is acting as the access point to
other Wi-Fi devices (i.e. phones, tablets, etc). This is also the gateway address
attached devices use when communicating to the dongle via Wi-Fi. The dongle
IP address 10.10.10.1/24 is pre-set at the factory and will always be the same.
This is the DHCP IP address the dongle received from the home Wi-Fi network.
The gateway listed here is the IP address of the home Wi-Fi router. If the user
knows the home Wi-Fi router password, the gateway address can be used to
connect to the router if network parameters need to be changed. If the STA State
area does not populate with an IP address, the dongle is not properly connecting
to the home Wi-Fi router (network).
This area displays encryption information for the dongle’s Wi-Fi network,
including the SSID of the dongle, if encryption mode is enabled or disabled, the
encryption password, and a button to restart the dongle. Enabling encryption
mode provides a level of security when connecting a device directly to the
dongle. By default, any device can connect to the dongle without requiring a
password (no security).
The SSID of the home Wi-Fi network, password, and connection state.
The protocol and address used to communicate with the EG4 monitoring server
over the internet.
Protocol and port used for internal communication between dongle and inverter.
```

## Slide 39

## Finding strings for Shodan Scans

39


> Recovered by OCR — confidence 82/100 on the text kept, 62/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Finding strings for Shodan Scans
A 72
A 73
4
v
unne!
@
>
8
3
Frome 130: 91 bytes on wire (728 bits), 91 bytes captured (728 bits)
Internet Protocol Version 4, Src: 192.168.100.38, Dst: 3.101.7.137
Transmission Control Protocol, Sre Port: 56152, Dst Port: 8081, Seq: 401, Ack: 1, Len: 25
[2 Reassenbled TCP Segnents (425 bytes): #127(400), #130(25)]
Hypertext Transfer Protocol
Host: us-luxpowertek.com:8081\r\n
Accept: */*\r\n
Content-Type: application/x-www-form-urlencoded\r\n
Connection: keep-alive\r\n
Content-Length: 25\r\n
‘Accept-Encoding: gzip, deflate\r\n
Form item: “recoréId”
key: recordtd
Value: 120
Y Form item: "startIndex
key: startIndex
value: 2
b/mainta
fo HTTP/
“Type: a
Hon: ke
Cookie
‘anage/we
xponerte
Content
Connec
ep-alive
```

## Slide 40

## EG4

40


> Recovered by OCR — confidence 84/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Explore Downloads Pricing @ http.html:eg4
i Historical Trend 0 V
Product Spotlight: We've Launched a new API for Fast Vulnerability Lookups. Check out
ShineMonitor
China, Shenzhen
ow
Seg
China
United States
India
Romania
© Loading...
Hong Kong G SSL Certificate
= United States, Miami
BAS 3
```

## Slide 41

## Finding Devices On the Web

41

## Slide 42

## OSINT of Solar Devices

42

## Slide 43

## OSINT of Solar Devices

43


> Recovered by OCR — confidence 85/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
OSINT of Solar Devices
Home AboutUs + Courses Provincial Colleges News and Events »
User Name
Password
```

## Slide 44

## OSINT of Solar Devices

44


> Recovered by OCR — confidence 82/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
OSINT of Solar Devices
Sri Lanka Institute of Tourism & Arabic Eood
sritanka Hotel Management
Institute... 43 (279)
Hotel management school - &
Montyon Overview Reviews About
Hampton
Inn Rome Directions Save Nearby Send to Share
phone
x
Graduate
Q No: 78 Galle Rd, Colombo, Sri Lanka
Located in: Sirimavo Bandaranaike Memorial
Building
Closed - Opens 8:30AMTue v
PP : Imagery ©2025 Airbus, CNES/ Airbus, Maxar Technologies, Map data ©2025 100 ft
```

## Slide 45

## Pinning down the Buildings

45


> Recovered by OCR — confidence 81/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
inning down the Buildings
Z pates @
Lebanan Chef
Arabic Food
(=) Union Bank of ColomBg}
Tourist Police Station (3)
©) cheers
Restaurant @)
Infinit Luxury Travel
Emproro City Site
Sri Lanka Sri Lanka Institute ° Recently viewed
Convention oe of Tourism & Hotel, © The Sri Lank
Recently viewed Institute of Director
Royal Saudifembassys Ramani Fe
Recentlyviewed) Salons at
Sri Lanka,Toutism |
Cinnamon
Grand Colomb<
4.7 te (19097)
S-star hotel
Japanese Language ©)
Education Association
Seylan Bank PLC
- Millennium
seylan tower 1 @,
```

## Slide 46

## Matching Devices on the Building

46

## Slide 47

## Finding Additional Device Types

47


> Recovered by OCR — confidence 87/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Finding Additional Device Types
EGy ELECTRONICS HOME v OUR PRODUCTS ~v RESOURCES ~ EMP HARDENED DISTRIBUTORS BLOG EVENTS ~ ABOUT v CONTACT v Q
EG4° 24K HYBRID SOLAR EG4° 12K HYBRID SOLAR EG4° 12K MINI-SPLIT
MINI-SPLIT 24000BTU MINI-SPLIT 12000BTU 12000BTU AIR
AC/DC AIR CONDITIONER/ AC/DC AIR CONDITIONER/ CONDITIONER/ HEAT PUMP
HEAT PUMP HEAT PUMP
LEARN MORE
```

## Slide 48

## EG4 OSINT

48


> Recovered by OCR — confidence 84/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
EG4 OSINT
Lebanan Chef
Arabic Food
The Emperor
7 Recently viewed
(en) Union Bank of Colombo
Tourist Police Station (3)
(y} Cheers
PORT VIEW
RESTAURANT |...
(e) Emproro City Site
wW Recently viewed
Sri Lanka
The Grand Lawn)
Cinnamon Grand
Stafford
Eaundro Plus - ~ International School
‘The,Geylon Hotel School
Graduates Association
Sasakawa Hall @)
Japanese Language ©
Education Association
```

## Slide 49

## Solar Panels on the Building

49

## Slide 50

# Who Needs Encryption and Signing

## Slide 51

## Clear Text ModBus and Serial Numbers

51


> Recovered by OCR — confidence 86/100 on the text kept, 76/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Clear Text ModBus and Serial Numbers
. 284646
. 298853
54 8000 ~ 34928
251 8000 — 34928
54 34928 .— 8000
54 34928 . 8000
54 8000 . 34928
ii 27 100.351414
29 126.869666
3.101.7.137
192.168.100.1
192.168.100.40
Accurate ECN: Not set
Congestion Window Reduced: Not
ECN-Echo: Not set
Urgent: Not set
Acknowledgment: Set
Push: Set
Reset: Not set
Syn: Not set
see vse Fin: Not set
Window: 5629
[Calculated window size: 5629]
[Window size scaling factor: -1 (unknown)]
Checksum: @xae76 [unverified]
[Checksum Status: Unverified]
Urgent Pointer:
[Timestamps]
[SEQ/ACK analysis]
TCP payload (291 bytes)
>» Data (291 bytes)
Data [..
@ G Data (data.data), 291 bytes
54 34928 — 8000
73 Bt — 4346
Seq=1 Ack=33 Win=5712 Len=0
[ACK] Seq=34 Ac
[PSH, ACK] Seq=875 Ack=1 Win= 3029 Len=19
43400110
670201
Packets: 2086 - Displayed: 1371 (65.7%)
```

## Slide 52

## Triggering the firmware download

52


> Recovered by OCR — confidence 68/100 on the text kept, 26/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Triggering the firmware download
File Edit Rules Tooke View Help
Transformer | Headers | Textiew |[Sytarvew | inageVien | Hewiew | Viebvew | Auth | Caching | Cookies | Raw | J50N | 2M
```

## Slide 53

## Why this matters

- Can send the inverter unauthenticated Modbus commands

- Serial numbers have high value for registration and configuration

- We can easily obtain firmware for analysis

- Alternatively, we can corrupt the firmware

- There were no indicators of firmware signing

   - Common across all solar manufacturers

53

## Slide 54

Insecure Monitoring Systems

## Slide 55

## EG4 and LuxPower S/N Enumeration

- Monitoring solution uses same code base

   - When the issues were reported patches were pushed simultaneously

- Allows the serial number to be guessed

   - Even if it has already been registered

- Also asks you to enter the PIN without registration

55

## Slide 56

## Just Ask Nicely and You Shall Receive

Confirms the S/N is
valid but
registered
Confirms the PIN
is valid
Confirms the S/N
is valid
Don’t need PIN to
validate SN

56

## Slide 57

## Serial Number to PIN matching

57


> Recovered by OCR — confidence 83/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Serial Number to PIN matching
Name Value
Name Value
Transformer | Headers | TextView || SyntaxView | ImageView | HexView | WebView | Auth | Caching | Cookies | Raw JSON | XML
```

## Slide 58

## Who needs a username?

#### • The forgot password will let you trigger a password reset with just the S/N

This PIN is from the dongle recovery guide

- Verify codes are not rate limited and they are only **6 digits**

58

## Slide 59

## Or just “Social Engineer”

59


> Recovered by OCR — confidence 92/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Or just “Social Engineer”
Turks & Caicos Islands
There needs to be some kind of summoning circle art made for those guys in this forum haha.
Sep 6, 2024
16
€cy) Ihave lined up a potentially good deal for 2 6000XP to add to my system and I'm wondering how to go about registering a used system with EG4. Can they blow away the
account originally tied to it? Do | need to buy a new wifi dongle for it? Does anyone have any experience with this?
EG4TechSolution
steam You will not need another dongle. We can assist you with this process. You will need to provide the inverter's serial number, and we can unlink the dongle
Online Support for to the account it's currently registered to.
Sulphur Springs, TX
@ You will not need another dongle. We can assist you with this pr You will need to provide the inverter's serial number, and w in unlink the dongle to the account it's
currently registered to.
jutstanding thank you! Will mark as solved
Sep 6, 2024
```

## Slide 60

Why One Vuln When Many Will Do

## Slide 61

## Tigo Cloud Connect Advance

- Device used for collecting data from solar microgrids

- Support integration with most major inverter manufacturers

- Enables rapid shutdown safety compliance

   - Sends a keep alive signal to the Tigo TS4-S and TS4-Os.

   - Loss of signal triggers these to drop the voltage output to zero

61

## Slide 62

## Default Creds and Robust DIY community

- The Tigo CCA has a dedicated community of DIY solar people who want access to the device

   - Use it for custom monitoring tools

   - Have found default creds

   - <u>https://www.photovoltaikforum.com</u>

- Default creds have been the same for several years

- Username: Tigo  Password: $olar

62

## Slide 63

## Tigo Firmware Changes

- By default, only an HTTP service is running on the CCA

- However, in earlier software versions you only had to browse to _/cgi-bin/shell_ to start the service

63

## Slide 64

## Tigo Firmware Changes

- Can’t simply browse anymore

   - Of note, the CCA only forces firmware updates when first installing the device

   - Ours shipped with 3.6, the current version is 4.0

- New versions still allow you to enumerate the version with just default creds

64

## Slide 65

## Tigo – One API, Lots of Problems

- Exposed maintenance API at /cgi-bin/mobile_api

- Has a lot of functions

 Most require a Session Id in addition to the default creds to access  DEVICE_INFO and DEVICE_PING do not

65

## Slide 66

### Covert Backdoor and Vulnerability in One

- DEVICE_PING

   - Accepts a user input for the ping interval

   - Doesn’t appear to actually ever perform any ping functions

- Only function appears to be starting the SSH service as a backdoor

66

## Slide 67

## Covert Backdoor and Vulnerability in One

- Hardcoded hash value comparison

   - If the correct value was entered kills existing ssh daemon and restarts ssh services

67

## Slide 68

- Command Injection Inside the Backdoor

- • When the user provided input is hashed to conduct the “magic word” comparison, it can be escaped

- Results in

printf ‘<user input>’ | sha256sum

68

## Slide 69

## Command Injection

- We can escape the printf with a simple _‘;_

- Arbitrary remote code execution! Inside a covert backdoor!

69

## Slide 70

## Crafting Our Own Keys

#### • DEVICE_INFO

- Provides information about the system such as the current OS, uptime, and S/N

- Accessible with just the default creds

- Generates the mobile session key that’s used as the SID when called

70

## Slide 71

## Who needs a secure key?

- rand() will always return the same value after seeding

- Overwrites the existing key when DEVICE_INFO is called  Devices are explicitly configured to Pacific time

71

## Slide 72

## Who needs a secure key?

- The rand value has another value added to it

- We need to know what it is in order to produce the mobile key

- • But, don’t worry, **it’s hardcoded**

72

## Slide 73

## Producing the Key Independently

73


> Recovered by OCR — confidence 84/100 on the text kept, 75/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Producing the Key Independently
~/Desktop |
Yr r Tigo:\$olar \
"Accept: application/json, text/pl
http: //192.168.68.63/cgi-bin/mobile_api \
1752432845
{ "code": @, "serial": "04C05BA1A910", "software": "4.0.1-ct", "uts"
451205666,
atus": 1}, { "id": 4, "name" “Modules Communication" "status": 2 yf tid*:
{ "id": 7, "name | 4.0.1-ct” “status” 0}, "id 8, "name"
}, { "id": 10, "name": "Cellular up" 11,
-[~/Desktop |
./session_test 1752432840
Timestamp: 301488
Random number: 451205666
Input value: 451364926
Formatted input: 451364926
"Last Dat
5, "name":
"sysconfig_ts"
"Discovery",
a Sync: a long time ago"
el: 4.1.15-
2.0.4",
null, “sysid":
"status":
"status"
"name":
"name": "S/N: 04CQ5BA1A910",
"name": "Cellular detected",
~/Desktop |
ba sr Tigo:\$olar \
deflate’ \
"Accept: appl on/json, text/pla
http: //192.168.68.63/cgi-bin/mobile_api
{ "code": "eth": { "dev": "etho", "dhcp": true, "ip": "192.168.1
8:5D:FF" ssid": "ATTr5WaMI2" : true, "ip": "192.168.68.6
2",
"subnet":
"subnet"
0
"255.255.255.0
52.0",
"gateway"
gateway":
"192.168.
192.168.68.
1.
1",
"quality_fraction":
"signal_level":
70/70",
"mac": "0
"Cloud Connection",
2
"st
```

## Slide 74

## Remember that Keep Alive signal?

- Reboot kills the signal

   - Will trigger the rapid shutdown procedure

- Can access all those sensitive APIs now

74

## Slide 75

## Quick Easter Egg

75


> Recovered by OCR — confidence 83/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Quick Easter Egg
-[~/Desktop |
ss h root@192.168.68.63
root@192.168.68.63's password:
~ # grep -rEi ‘defcon' /mnt/ffs/
```

## Slide 76

## What Next?

- The solar industry is growing faster than its security implementation

   - Need strong partnerships

- Embedded system security is falling behind

- We need supply chain clarity

   - Sourcing aspects of products is a fact of life, but we should know what they are

   - The code is a disaster

76

## Slide 77

## In the Meantime, What Can You Do?

- Never expose solar control systems directly to the internet (Apparently wasn’t obvious enough)

   - Always put them through a router or behind a firewall

   - Disable automatic updates (Can’t trust the vendors)

- Take special consideration of remote monitoring solutions

- Home assistant can help set up local monitoring solutions

- Demand more from manufacturers

77

## Slide 78

# Questions?

78
