---
title: "High Voltage Heist Turning Your EV into my Power Bank"
speakers: ["Fabien Guillebot", "Stepan Konicek"]
conference: "DEF CON"
conference_full: "DEF CON 34"
edition: "34"
year: null
source_pdf: "DEF CON 34/DEF CON 34 - Fabien Guillebot, Stepan Konicek - High Voltage Heist Turning Your EV into my Power Bank - EVintomy Pow.pdf"
pages: 33
sha256: "f312c2e29d5d584ad414189a3d65f551838ed13ab743cf40be700d21179667d6"
text_chars: 14922
ocr_pages: 0
has_ocr: false
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2"
converted_at: "2026-08-12T00:16:03Z"
---
# High Voltage Heist Turning Your EV into my Power Bank

**Speakers:** Fabien Guillebot, Stepan Konicek  
**Conference:** DEF CON 34  
**Source:** `DEF CON 34/DEF CON 34 - Fabien Guillebot, Stepan Konicek - High Voltage Heist Turning Your EV into my Power Bank - EVintomy Pow.pdf` (33 pages)


## Slide 1

###### **DEFCON**

## **34**

#### **HIGH VOLTAGE HEIST**

Turning Your EV into my Power Bank

**Stepan Konicek**

**Fabien Guillebot**

```
High Voltage Heist: Turning Your EV into my Power Bank   ·   DEFCON 34
```

```
01 / 33
```

## Slide 2

##### **Introduction**

**Embedded Systems Security Testing team in Prague, Czech Republic** **`Accenture Security`**

**Stepan Konicek**

###### **Fabien Guillebot**

Embedded Systems Security Engineer

Hardware Security Engineer

Pentesting in embedded & automotive systems

Glitching & hardware design

```
High Voltage Heist: Turning Your EV into my Power Bank   ·   DEFCON 34
```

```
02 / 33
```

## Slide 3

##### **Agenda**

**`01` Charging Communication & In-Vehicle Architecture**

**`02` The Attack Surface**

**`03` The ChargeSploit Project**

**`04` Demo & Q&A**

```
High Voltage Heist: Turning Your EV into my Power Bank   ·   DEFCON 34
```

```
03 / 33
```

## Slide 4

###### **The EV Charging Ecosystem & Attack Surface**

```
High Voltage Heist: Turning Your EV into my Power Bank   ·   DEFCON 34
```

```
04 / 33
```

## Slide 5

```
SECTION  01
```

### **Charging Communication & In-Vehicle Architecture**

From the physical plug to the application layer — and inside the car.

```
High Voltage Heist: Turning Your EV into my Power Bank   ·   DEFCON 34
```

```
05 / 33
```

## Slide 6

```
01 / CHARGING COMMUNICATION
```

###### **The Protocol Stack — ISO/OSI Mapping**

L7 Application
ISO 15118 / DIN 70121
L6 Presentation
V2G application messages (EXI)
L5 Session
L4 Transport TCP  /  TLS
L3 Network IPv6  (link-local)
L2 Data Link HomePlug Green PHY — PLC
L1 Physical CCS  ·  Control Pilot  ·  Proximity Pilot

```
High Voltage Heist: Turning Your EV into my Power Bank   ·   DEFCON 34
```

```
06 / 33
```

## Slide 7

```
01 / CHARGING COMMUNICATION
```

###### **Physical Layer — Connectors**

Type 2 (Mennekes) — AC, EU

CCS2 (Combo 2) — AC + DC, EU

CCS1 (Combo 1) — AC + DC, US

CHAdeMO — DC, Japan

NACS (Tesla / SAE) — AC + DC

```
CCS2 (Combo 2) —pin layout
```

```
High Voltage Heist: Turning Your EV into my Power Bank   ·   DEFCON 34
```

```
07 / 33
```

## Slide 8

```
01 / CHARGING COMMUNICATION
```

###### **Physical Layer — Control & Proximity Pilot**

```
CONTROL PILOT  (CP)
```

```
PROXIMITY PILOT  (PP)
```

PWM signal

Resistor-coded cable rating

Signals charging state Signals max available current PLC carrier in HLC mode

Signals max cable current Detects plug present / removed

```
High Voltage Heist: Turning Your EV into my Power Bank   ·   DEFCON 34
```

```
08 / 33
```

## Slide 9

```
01 / CHARGING COMMUNICATION
```

###### **Control Pilot — Signaling States**

CP VOLTAGE STATES PWM DUTY CYCLE
IEC 61851 on the CP wire · 1 kHz
A +12 V Not connected 5 %
High Level Communication (HLC)
B +9 V Connected, not ready
25 %
C +6 V Charging
15 A available
D +3 V Charging (ventilation)
50 %
30 A available
E 0 V Error / no power
90 %
F −12 V EVSE unavailable
65 A available

```
High Voltage Heist: Turning Your EV into my Power Bank   ·   DEFCON 34
```

```
09 / 33
```

## Slide 10

```
01 / CHARGING COMMUNICATION
```

###### **In-Vehicle High-Voltage Architecture**

```
High Voltage Heist: Turning Your EV into my Power Bank   ·   DEFCON 34
```

```
10 / 33
```

## Slide 11

```
01 / CHARGING COMMUNICATION
```

###### **In-Vehicle High-Voltage Architecture**

###### **`EVCC`**

The gateway. Handles ISO 15118/DIN 70121 via PLC (HomePlug Green PHY / Qualcomm QCA700x). Translates external charger requests to internal CAN.

_EV Communication Controller_

###### **`BMS`**

The gatekeeper. Monitors battery health and actuates the contactors based on EVCC instructions.

_Battery Management System_

**`HV CONTACTORS`** The physical relays. Once closed, the raw battery DC voltage is exposed directly to the external pins.

```
THE TRUST FLAW
```

The BMS implicitly trusts the power flow direction and limits negotiated by the EVCC. The OBC (On-Board Charger) is completely bypassed during DC sessions.

```
High Voltage Heist: Turning Your EV into my Power Bank   ·   DEFCON 34
```

```
11 / 33
```

## Slide 12

```
01 / CHARGING COMMUNICATION
```

###### **SLAC — Signal Level Attenuation Characterization**

**`WHY IT EXISTS`** PLC on CP wire causes crosstalk between nearby chargers Lowest attenuation = physical cable connection

Shared AVLN formed for all higher layers

###### **`AVLN`**

AVLN — the private HomePlug network the paired EV + EVSE share. All V2G traffic rides it, encrypted with the NMK.

###### **`EV`**

###### **`PARAM`**

- **`→ CM_SLAC_PARM.REQ`** broadcast · RunID **`← CM_SLAC_PARM.CNF`** RunID · expected sounds **`SOUNDING → CM_START_ATTEN_CHAR.IND`** announces measurement  x3 **`→ CM_MNBC_SOUND.IND`** M-Sounds  x10

###### **`MEASURE`**

- **`← CM_ATTEN_CHAR.IND`** avg attenuation · 58 carrier groups **`→ CM_ATTEN_CHAR.RSP`** EV selects lowest **`MATCH → CM_SLAC_MATCH.REQ ← CM_SLAC_MATCH.CNF`** NMK + NID  ->  join AVLN

###### **`EVSE`**

```
High Voltage Heist: Turning Your EV into my Power Bank   ·   DEFCON 34
```

```
12 / 33
```

## Slide 13

```
01 / CHARGING COMMUNICATION
```

###### **SDP — SECC Discovery Protocol**

EV EVSE
WHAT SDP DOES
REQUEST
Discovers EVSE's IPv6 address and
→ SECC_RequestMessage UDP multicast · FF02::1 · port 15118
TCP port
RESPONSE
SDP request initiated by EV
← SECC_ResponseMessage UDP unicast to EV
SECC IP TCP port transport security
Runs immediately after SLAC
fe80::/10 49152+ TCP TLS | none
NEXT
EV opens TCP (or TLS) to the returned address : port  →  V2G session

_Port is the SECC's dynamic V2G port (49152–65535). 15118 is only the SDP discovery port._

```
High Voltage Heist: Turning Your EV into my Power Bank   ·   DEFCON 34
```

```
13 / 33
```

## Slide 14

```
01 / CHARGING COMMUNICATION
```

###### **V2G Communication — Standards**

Plug & Charge (PnC) ISO 15118-2 / -20 DIN 70121
vs  ISO 15118-2
V2G messages · EXI · V2GTP ISO 15118-2 / DIN 70121
DIN ISO-2
SDP · IPv6 / TCP / TLS ISO 15118-2
Charging DC only DC+AC
TLS none optional
PLC + SLAC (HomePlug GP) ISO 15118-3
Plug & Charge no yes
Basic signaling — PWM / CP IEC 61851-1 Smart charging no yes
Shared:  SLAC · SDP · IPv6/TCP · V2GTP ·
Connector / plug IEC 62196 · J1772
EXI

```
High Voltage Heist: Turning Your EV into my Power Bank   ·   DEFCON 34
```

```
14 / 33
```

## Slide 15

```
01 / CHARGING COMMUNICATION
```

###### **DC Charging Session — ISO 15118**

**`1`** SupportedAppProtocol **`2`** SessionSetup **`3`** ServiceDiscovery **`4`** Authorization **`5`** ChargeParameterDiscovery

**`6`** CableCheck **`7` PreCharge** **`8`** PowerDelivery (start) **`9` CurrentDemand  (loop)** **`10`** WeldingDetection → SessionStop

```
10
```

```
High Voltage Heist: Turning Your EV into my Power Bank   ·   DEFCON 34
```

```
15 / 33
```

## Slide 16

```
01 / CHARGING COMMUNICATION
```

###### **DC Session — Protocol Negotiation**

```
WHAT IT DOES
```

First V2G message after TCP connect EV lists supported protocols + priority EVSE selects the highest-priority match

```
"supportedAppProtocolReq": {
"AppProtocol": [
{
"ProtocolNamespace":
"urn:din:70121:2012:MsgDef",
"Priority": 1
},
{
"ProtocolNamespace":
"urn:iso:15118:2:2013:MsgDef",
"Priority": 2
}
]
}
```

EV lists DIN 70121 as priority 1 — EVSE selects ISO 15118-2

```
High Voltage Heist: Turning Your EV into my Power Bank   ·   DEFCON 34
```

```
16 / 33
```

## Slide 17

```
01 / CHARGING COMMUNICATION
```

###### **DC Session — Session Setup**

```
WHAT IT DOES
```

EV identifies itself with EVCCID

EVSE assigns a unique 8-byte SessionID All subsequent messages are tagged with it

```
// EV  →  EVSE
"SessionSetupReq": {
"EVCCID": "04E77E74D14D"
}
// EVSE  →  EV
"SessionSetupRes": {
"ResponseCode":
"OK_NewSessionEstablished",
"EVSEID": "DE*CBY*E123456*1",
"SessionID": "94DCC04AF06EF97D"
}
```

EVCCID = EVCC MAC address — physical identity of the car

```
High Voltage Heist: Turning Your EV into my Power Bank   ·   DEFCON 34
```

```
17 / 33
```

## Slide 18

```
01 / CHARGING COMMUNICATION
```

###### **DC Session — Charge Parameter Discovery**

```
WHAT IT DOES
```

EV sends its full battery limits to the EVSE

EVSE responds with charger capabilities

Establishes max current, voltage, and SOC

350A max · 825.6V max · SOC 66% — full battery limits exposed

```
"DC_EVChargeParameter": {
"DC_EVStatus": {
"EVReady": false,
"EVErrorCode": "NO_ERROR",
"EVRESSSOC": 66
},
"EVMaximumCurrentLimit": {
"Value": 3500, "Multiplier": -1,
"Unit": "A"
},
"EVMaximumVoltageLimit": {
"Value": 8256, "Multiplier": -1,
"Unit": "V"
```

```
},
"FullSOC": 100,
"BulkSOC": 80
}
```

```
High Voltage Heist: Turning Your EV into my Power Bank   ·   DEFCON 34
```

```
18 / 33
```

## Slide 19

```
01 / CHARGING COMMUNICATION
```

###### **DC Session — Cable Check**

```
WHAT IT DOES
```

EV signals it is ready (EVReady flips to true)

EVSE verifies DC bus insulation integrity

Safety gate that must pass before contactors close

```
// EV  →  EVSE
"CableCheckReq": {
"DC_EVStatus": {
"EVReady": true,
"EVErrorCode": "NO_ERROR",
"EVRESSSOC": 66
}
}
```

```
// EVSE  →  EV
"CableCheckRes": {
"ResponseCode": "OK",
"DC_EVSEStatus": {
"EVSEIsolationStatus": "Valid",
"EVSEStatusCode": "EVSE_Ready"
},
"EVSEProcessing": "Finished"
}
```

```
High Voltage Heist: Turning Your EV into my Power Bank   ·   DEFCON 34
```

```
19 / 33
```

## Slide 20

```
01 / CHARGING COMMUNICATION
```

###### **DC Session — PreCharge**

```
WHAT IT DOES
```

EVSE ramps DC output to match battery voltage EV requests target voltage each iteration Loops until delta is small — then contactors close

450V target, EVSE reports 400V — loops ~11 times before contactors close

```
// EV  →  EVSE  (loops ~11 times)
"PreChargeReq": {
"EVTargetVoltage": {
"Value": 4500, "Multiplier": -1,
"Unit": "V"
},
"EVTargetCurrent": {
"Value": 10, "Multiplier": -1,
"Unit": "A"
}
}
// EVSE  →  EV
"PreChargeRes": {
"ResponseCode": "OK",
"EVSEPresentVoltage": {
"Value": 400, "Multiplier": 0,
"Unit": "V"
}
}
```

```
High Voltage Heist: Turning Your EV into my Power Bank   ·   DEFCON 34
```

```
20 / 33
```

## Slide 21

```
01 / CHARGING COMMUNICATION
```

###### **DC Session — Current Demand**

###### **`WHAT IT DOES`**

Core charging loop — runs continuously EV requests target current each cycle

```
// EV  →  EVSE  (every ~1 s)
"CurrentDemandReq": {
"DC_EVStatus": {
"EVReady": true, "EVRESSSOC": 72
},
"EVTargetCurrent": {
"Value": 1200, "Multiplier": -1
},
"EVTargetVoltage": {
"Value": 4000, "Multiplier": -1
},
"ChargingComplete": false
}
```

EVSE reports live voltage and current

Loop ends when EV sets ChargingComplete

Repeats every ~1 s — attacker can inject fake voltage/current replies

```
// EVSE  →  EV
"CurrentDemandRes": {
"ResponseCode": "OK",
"EVSEPresentVoltage": {
"Value": 4000, "Multiplier": -1
},
"EVSEPresentCurrent": {
"Value": 1200, "Multiplier": -1
},
"EVSECurrentLimitAchieved": false
}
```

```
High Voltage Heist: Turning Your EV into my Power Bank   ·   DEFCON 34
```

```
21 / 33
```

## Slide 22

```
01 / CHARGING COMMUNICATION
```

###### **Putting It Together**

SLAC → SDP → TCP/TLS done — every V2G message then rides this pipeline: encoded down one stack, decoded up the other.

EV  (EVCC) ENCODE DECODE EVSE  (SECC)
JSON message JSON message
V2G app dict V2G app dict
EXI codec EXI codec
compress · Java / py4j compress · Java / py4j
V2GTP V2GTP
+ 8-byte header + 8-byte header
TCP / TLS TCP / TLS
session transport session transport
IPv6 IPv6
link-local fe80::/10 link-local fe80::/10
CP wire
PLC — HPGP PLC — HPGP
Ethernet over CP wire HomePlug Green PHY Ethernet over CP wire

```
High Voltage Heist: Turning Your EV into my Power Bank   ·   DEFCON 34
```

```
22 / 33
```

## Slide 23

```
SECTION  02
```

### **The Attack Surface**

What happens when the vehicle blindly trusts the charger?

```
High Voltage Heist: Turning Your EV into my Power Bank   ·   DEFCON 34
```

```
23 / 33
```

## Slide 24

```
02 / THE ATTACK SURFACE
```

###### **Testing the V2G Attack Surface**

```
STATE MACHINE
```

Force, skip or reorder V2G states — break protocol assumptions.

```
PARAMETER FUZZING
```

Malformed & boundary values in V2G application messages.

```
PHYSICAL DIGITAL TRUST
```

Spoof EVSEPresentVoltage / Current — does the BMS trust V2G over real physical state?

```
High Voltage Heist: Turning Your EV into my Power Bank   ·   DEFCON 34
```

```
24 / 33
```

## Slide 25

```
SECTION  03
```

### **The ChargeSploit Project**

Open-source hardware + software toolkit for EV charging security testing.

```
High Voltage Heist: Turning Your EV into my Power Bank   ·   DEFCON 34
```

```
25 / 33
```

## Slide 26

```
03 / THE CHARGESPLOIT PROJECT
```

###### **ChargeSploit — Overview**

An open-source toolkit for EV charging security testing — hardware + software

```
HARDWARE
```

Custom CCS2 cable Control Pilot generator

```
SOFTWARE
```

ISO 15118 + DIN 70121 support

Test-case handlers with fuzzing modules EV and EVSE side emulation

Dummy load Signal generator

Man-in-the-Middle

TLS support for Plug & Charge testing

```
scan for the repo
github.com/konicst1/ChargeSploit
```

```
High Voltage Heist: Turning Your EV into my Power Bank   ·   DEFCON 34
```

```
26 / 33
```

## Slide 27

```
03 / CHARGESPLOIT —HARDWARE
```

###### **Custom CCS2 Cable**

```
WHAT IT IS
```

CCS2 plug wired straight to our test rig

Breaks out CP, PP and the DC power pins

Lets us sit inline between EV and EVSE

```
High Voltage Heist: Turning Your EV into my Power Bank   ·   DEFCON 34
```

```
27 / 33
```

## Slide 28

```
03 / CHARGESPLOIT —HARDWARE
```

###### **Control Pilot Generator**

```
WHAT IT IS
```

Drives and reads the Control Pilot line

Sets PWM duty cycle, measures CP voltages

Toggles PLC and power on demand

```
High Voltage Heist: Turning Your EV into my Power Bank   ·   DEFCON 34
```

```
28 / 33
```

## Slide 29

```
03 / CHARGESPLOIT —HARDWARE
```

###### **Dummy Load**

```
WHAT IT IS
```

Resistive bulb bank sinks the DC output

Safely dissipates power on the bench

Stands in for a battery accepting charge

```
High Voltage Heist: Turning Your EV into my Power Bank   ·   DEFCON 34
```

```
29 / 33
```

## Slide 30

```
03 / CHARGESPLOIT —HARDWARE
```

###### **Voltage Generator**

```
WHAT IT IS
```

DC source emulating the EVSE physical voltage

Feeds a controlled voltage into the vehicle

```
High Voltage Heist: Turning Your EV into my Power Bank   ·   DEFCON 34
```

```
30 / 33
```

## Slide 31

```
SECTION  04
```

### **Demo**

Unauthorized discharge of a fully locked Tesla Model 3.

```
High Voltage Heist: Turning Your EV into my Power Bank   ·   DEFCON 34
```

```
31 / 33
```

## Slide 32

```
04 / DEMO
```

###### **Physical Consequences**

**`POWER THEFT BATTERY DEGRADATION`** Contactors close without Digital charge state while auth → draining → direct traction-battery cells forced below safe discharge. cutoff.

**`PHYSICAL DoS`** DC bus exposed → intentional short.

```
High Voltage Heist: Turning Your EV into my Power Bank   ·   DEFCON 34
```

```
32 / 33
```

## Slide 33

# **Q&A**

###### **High Voltage Heist: Turning Your EV into my Power Bank**

```
Stepan Konicek  ·  Fabien Guillebot  ·  Accenture Security
```

```
github.com/konicst1/ChargeSploit
```

```
High Voltage Heist: Turning Your EV into my Power Bank   ·   DEFCON 34
```

```
33 / 33
```
