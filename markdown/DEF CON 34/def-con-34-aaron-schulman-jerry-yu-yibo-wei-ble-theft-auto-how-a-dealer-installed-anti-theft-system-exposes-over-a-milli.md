---
title: "BLE Theft Auto How a Dealer-Installed Anti-Theft System Exposes Over a Million Cars to Theft"
speakers: ["Aaron Schulman", "Jerry Yu", "Yibo Wei"]
conference: "DEF CON"
conference_full: "DEF CON 34"
edition: "34"
year: null
source_pdf: "DEF CON 34/DEF CON 34 - Aaron Schulman, Jerry Yu, Yibo Wei - BLE Theft Auto How a Dealer-Installed Anti-Theft System Exposes Over a Million Cars to Theft - BTA.pdf"
pages: 54
sha256: "a9680a675a47c3f534a8767a95008c944926d0253a2f64812e075ca0eeafc1ba"
text_chars: 18059
ocr_pages: 22
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T00:11:29Z"
---
# BLE Theft Auto How a Dealer-Installed Anti-Theft System Exposes Over a Million Cars to Theft

**Speakers:** Aaron Schulman, Jerry Yu, Yibo Wei  
**Conference:** DEF CON 34  
**Source:** `DEF CON 34/DEF CON 34 - Aaron Schulman, Jerry Yu, Yibo Wei - BLE Theft Auto How a Dealer-Installed Anti-Theft System Exposes Over a Million Cars to Theft - BTA.pdf` (54 pages)

## Slide 1

Nishant
Bhaskar
Sumanth
Rao
Jefferson Mohak Christian
Chien Vaswani Dameff

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
UCSan Diego
Aaron Schulman
Nishant
eis ot
«+ Bhaskar
eax re Sumanth
i
y.
Fd
Jefferson Mohak _ Christian
Chien Vaswani Dameff
Jerry Y
```

## Slide 2

If you own one of the 2 million cars that ⚠ has THIS STICKER on your driverʼs side **or sometimes** window

⚠

SCAN AND UPDATE NOW!

Yes, even if itʼs “deactivated ˮ

## Slide 3

# Smartphones are remote controls for vehicles

**Capabilities: Wireless Protocols:**

   - Cellular

   - ● Bluetooth

- Unlock doors

- ● Immobilizer ● Horn

- Lights

- Remote starter

Tesla app

## Slide 4

# Car remote control systems have had vulnerabilities

# **Cellular**

# **Bluetooth**

- Cellular telematics → CAN

   - Checkoway et al. 2011

      - Co-located malicious BLE app → infotainment → CAN

         - Checkoway et al. 2011

- Cellular head unit → CAN

   - Miller and Valasek 2015

- Cellular TCU → critical ECUs

   - BLE phone key relay → Body control

      - NCC Group 2022

      - ○ GoGoByte 2023

- Keen Security Lab 2018

## Slide 5

## One wireless protocol is more sketchy than the other

Cellular: Long-range attack Inherits robust security protocols

**Bluetooth: Short-range attack YOLO letʼs make custom security**

- Cellular security is robust

   - SIM card authentication

   - OTA encryption

- Web security is robust

      - BLE sec. is not compatible with cars

         - Revoking experience is cumbersome

         - Access sharing is impossible

         - ○ Co-located apps are threats

   - Authentication: OAuth2

   - Encryption: HTTPS

- Automatic OTA firmware updates

- Manual user-driven updates

## Slide 6

# OEM BLE control is battle tested.   Aftermarket is…

**Aftermarket System** Adding BLE remote control to any car

#### **OEM System**

Built-in to every vehicle of make/model

   - Hand-rolled BLE security protocols

- Standardized BLE security protocols (e.g., CCC digital key)

   - Bypasses OEM security

- Tested by many

- Cut and spliced into wiring

- ○ 3rd party vendor

- ○ 3rd party installer

???

## Slide 7

That sounded great. Real talk: Why did we actually study aftermarket BLE security systems?

_Science only follows a straight line in retrospect_ ™

## Slide 8

⏱

# 2018  Finding BLE-based skimmers in gas

pumps

## Slide 9

## “ **QT ********* ˮ named devices were everywhere in SoCal

- **Seen commonly at gas stations**

- **We thought we hit the skimmer jackpot**

- **Then we also saw them at gas stations, parking lots, on highways, etc.**

## Slide 10

⏱

# 2024  We try Google.

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ 2024: Wetry Google.
Gogle
QT FCCID
fecid.io
https://fecid.io > 2ASRL > 2ASRL-1069
1069 QT Solutions Bluetooth Sensor User Manual ... - FCC ID
QT Solutions Bluetooth Sensor User manual details for FCC ID 2ASRL-1069 made by QT Solutions
PTY LTD. Document Includes User Manual.
FCC Report
https://fec.report > company » Qt-Solutions-Pty-L-T-D
QT Solutions PTY LTD FCC Filings
Experimental, International, and equipment registration filings filed with the FCC by QT Solutions
PTY LTD
fecid.ai
https://fecid.ai » Quantum5x Systems Inc. ?
QT-300 Module - FCC Certification
FCC certification details for QT-300 Module. Product. Frequencies: 525-600 MHz. General Mobile Radio
And Broadcast Services equipment
fecid.io
httn)e-//fearid in « SDACVE s
```

## Slide 11

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
User manual
1069 QT Solutions Bluetooth Sensor User Manual QT
Solutions PTY
FCC ID 2ASRL-1069
User manual
QT Solutions Bluetooth Sensor
by QT
Eswas
BT SERIES
CUSTOMER USER GUIDE
Congratulations on your purchase of the KARR BT system, designs
convenient, selectable features and a user friendly mobile app to prov
you the best in electronic vehicle security
Read this manual
features, ens
Search
```

## Slide 12

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
SETTINGS
These settings can only be changed once you
connect the KARR BT app to the vehicle.
Silent Arm/Lock Disarm/Unlock. Enabling
this setting will tum off normal arm/lock and
disarm/unlock honks from the BT system
This does not affect vehicle factory settings.
As long as this setting is enabled, the BT
system will always be in silent arm/lock
and disarm/unlock mode.
In addition, the temporary selection discussed
in "KARR BT System Functions” will now only a
show two icons.
Disable Door Trigger: Prevents Door Trigger
zone from engaging the BT system.
Disable Trunk: Prevents the trunk from
engaging the BT system.
Disable Shock Sensor Triggers: Prevents impact to the vehicle from engaging the
BT system.
Auto Lock upon Ignition On: Vehicle doors will lock upon turning “On’ the ignition
and closing all doors.
Auto Unlock upon Ignition Off: Vehicle's door locks will unlock immediately upon
turning to the "Off" position.
ARM MODE
Active Arm: Also known as manual arming. Refer to “KARR BT System Functions”
(on page two, “Active Arming of the BT System,” when using your vehicle's keyless
entry remote.
Your system is defaulted to Active Arm.
©
Passive Arm: The system will arm 30 seconds after all points of entry have been
cleared.
If any door or trunk is opened, this will interrupt the arming countdown. Once all
the entry points are closed, the countdown will start over for the full 30 seconds
When selecting Passive Arm, an additional option to lock doors automatically
upon Passive Arm will become available. The default setting is of; simply press
the switch to toggle the feature on or off. Vehicle doors will now lock with the
completion of the Passive Arm countdown
If you are locked out of your vehicle due to passive arming and your keys and
connected phone are in your vehicle, the BT system will disconnect from your
phone after approximately 45 seconds to one minute so that you may connect
with another device that has the KARR BT app installed to unlock your vehicle.
SHOCK SENSOR
The Shock Sensor can be adjusted by sliding the button from zero on the left to
as high as 15 on the right.
Depending on the size of your vehicle, adjustment selection will vary. Too low
a number may not render any response, while too high a number may render an
unwanted response.
At the time of installation, your vehicle Shock Sensor has been calibrated
and tested. If you wish to make adjustments, this may adversely affect the
performance of the Shock Sensor.
We strongly recommend contacting our customer service department if you wish
to make changes to your Shock Sensor's sensitivity so that a technician may
properly perform a new calibration.
```

## Slide 13

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Disable Shock Sensor Trigg
BT system.
‘Auto Lock upon Ignition On
and closing all doors
Auto Unlock upon Ignition ¢
turning to the "Off" position
ARM MODE
Active Arm: Also known as
on page two, “Active Arming
entry remote.
Your system is defaulted to
of entry have been
intdown. Once all
ie full 30 seconds
s automatically
E of; simply pres
Dw lock with the
dd your keys and
bnnect from your
you may connect
Jock your vehicle.
ero on the left to
Depending on the size of your vehicle, adjustment selection will vary. Too low
a number may not render any response, while too high a number may render an
unwanted response.
At the time of installation, your vehicle Shock Sensor has been calibrated
and tested. If you wish to make adjustments, this may adversely affect the
performance of the Shock Sensor
We strongly recommend contacting our customer service department if you wish
to make changes to your Shock Sensors sensitivity so that a technician may
properly perform a new calibration.
```

## Slide 14

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
What does KARR Security do for my vehicle?
Your KARR Security system is an advanced anti-theft solution, designed to go beyond
your manufacturer's alarm. It’s like an upgrade for your car's security! This gives you
extra peace of mind and fewer worries.
```

## Slide 15

Placeholder demo video

## Slide 16

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
How do | get a KARR Security system for my vehicle?
We partner with more than 3,000 car dealerships nationwide. Since we only work with
dealerships, give us a call— we'll connect you with the nearest one.
```

## Slide 17

# Dealer-Installed aftermarket remote control ecosystem

**Acrisure Protection Group** Designs and sells the security system

**Dealers SoCal** Install the device on every car they sell for lot security and $$$

**Car Buyers** Pay for access to the system 0$1,200 or refuse it

## Slide 18

### How does the KARR system work?

**Installer** Splices the system into a carʼs wiring and hides it behind the dash

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
How does the KARR system
work?
AFTERMARKET
REMOTE CONTROL mo
Wi
AFTERMARKET
DULE REMOTE CONTROL APP
CAN BUS OR DISCRETE WIRES
Ss)
(m\ (a)
Oo
ENGINE
START
STOP
—
a i
es
STARTER
ENGINE LIGHTS
T
IN-VEHICLE
SWITCHES &
BUTTONS
_—
\ =
—
- |
HORN DOORS TRUNK
Installer
Splices the system
into a car's
wiring and hides it
behind the dash
```

## Slide 19

# Breaking KARR The App Reverse Engineered

Server Client KARR
Login (username/pwd)
Session API Token
Get User Vehicles
(User Vehicle, QT name)
BLE Advertisements
Filter by QT names belonging to user
READ_MODE
REQUEST_AUTH
Server-client authentication has  PROVIDE_AUTH
nothing to do with client-device  AUTH_SUCCESS
authentication.
UNLOCK_DOORS
Access control is only at UI level.
ACK_OK

## Slide 20

# Breaking KARR The App Reverse Engineered

Server Client KARR
Login (username/pwd)
Session API Token
Get User Vehicles
(User Vehicle, QT name)
BLE Advertisements
Filter by QT names belonging to user
READ_MODE
REQUEST_AUTH
PROVIDE_AUTH
AUTH_SUCCESS
UNLOCK_DOORS
ACK_OK

## Slide 21

# The KARR Authentication Vulnerability

“Clientˮ

##### KARR

KARR **REQUEST_AUTH challenge:** A random byte array. Ensures commands are only accepted by the **PROVIDE_AUTH response:** intended device, but offers **no real security.** 1. Device name: “QT xx…xxˮ ✔ BLE Advertisements 2. Device mode enum ✔ 3. Challenge bytes ✔ READ_MODE 4. Secret key ✔ REQUEST_AUTH 5. “hashˮ PROVIDE_AUTH 6. Profit! (AUTH_SUCCESS) AUTH_SUCCESS UNLOCK_DOORS ACK_OK

## Slide 22

Attempted Implementation of User Privileges

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Attempted Implementation of User Privileges
Higher / installer foe aries
eadlights & Horn
a | eee { eee ee eeeebbbebbeveetuteeeeeeeeeeeeeeeeesstitttttttseeeeeeeeeeeees
[or
© accepted Door/Trunk Lock
@) Dealer ————>_—SCO@U ser
2 $$$ & Immobilizer
a
oO
Disabled
} X) Doubt
rejected
Lower Privilege
```

## Slide 23

# Attempted Implementation of User Privileges

*

- _Still beacons and connectable when the engine is running_

_** Accepts ONE control command:_ **CHANGE_MODE**

## Slide 24

# Demystifying “No Saleˮ Mode

Locate KARR
vehicle
Wait till vehicle starts)
No Sale  YES Engine  NO
mode? running?
NO YES
Compromised Change Mode

## Slide 25

# Our Super Cool App

Placeholder for demo mayhem mode demo video

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
<« COMMAND
Our Super Cool App
Placeholder for demo mayhem mode demo video
```

## Slide 26

# What can we do?

**Vehicle Entry**

Trivially compromised by unlocking the doors.

**Stranding a car**

Immobilization possible for vehicle ownerʼs without app access. **Vehicle Theft**

For some vehicles, an attacker can use a locksmithing tool to create a duplicate key to start the engine and drive away.

## Slide 27

# Breaking KARR How to Target a KARR…Car?

Method #1 Use WiGLE to find where clusters of KARR devices appear.

Method #2 Walk around with a BLE scanner till you find a “QTˮ or “DRˮ device. Method #3 They do come with a great big sticker.

Method #4 If in Southern California, go outside.

## Slide 28

Measuring the scale of the vulnerability

Downloaded many KARR devices on <u>Wigle.net</u> Found KARR MAC addresses are assigned sequentially

Created a new MAC population inference method

## Slide 29

### Measuring the Scale of the Vulnerability

- KARR Mac addresses are assigned mostly sequentially

- <u>WiGLE.net</u> has a very good sample of all deployed KARR alarms

## Slide 30

0.31

0.56

0.88

### Measuring the Scale of the Vulnerability

- KARR Mac addresses are assigned mostly sequentially

- <u>WiGLE.net</u> has a very good sample of all deployed KARR alarms

- We measure the “densityˮ of <u>WiGLE.net</u> samples

## Slide 31

### Measuring the Scale of the Vulnerability

- KARR Mac addresses are assigned mostly sequentially

- <u>WiGLE.net</u> has a very good sample of all deployed KARR alarms

- We measure the “densityˮ of <u>WiGLE.net</u> samples

- Result:

   - Total observations: _1.3M_

   - Density: _0.5_

   - Total estimated: _1.3M / 0.5 = 2.6M_

- See details in our paper!

## Slide 32

### Where are KARRs deployed

- We know most of them are sold in SW

- They stay in the used car market forever

- Thank you WiGLE

## Slide 33

# Mitigations from KARR

Jan 21, 2025

Disclosure Day. Productive meeting with Acrisure representatives. Discussed solutions.

Aug 2, 2025

Received initial prototype patched device and app.

Jul 20, 2026 Patch was rolled out to customers.

## Slide 34

# Mitigations from KARR

**Interim fix**

- Removing the universal key from the source code.

- ● Removing the compromised APKs from the web.

**Full patch**

- Firmware update to replace the global key.

- ● Fully disabling devices in _No Sale_ mode.

- _For paying customers with KARR accounts:_

   - Push notification from app to update firmware.

- _For non-paying customers with “inactiveˮ alarms:_

   - Download app, verify with VIN number to get the firmware update, which should fully disable their KARR devices.

## Slide 35

Finding similar systems…

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Finding similar systems...
ROCKLEDGE About Us Products /Support Photos. Install Videos Careers Contact
SECURITIES
Download the Rockledge Mobile App
erred a] Download on the
Pp «€ App Store
‘Over 20 Years of Experience delivering qua
reliable products. Ny
a B> Google Play
Scan QR code to download
INSURANCE
AUTO SECURITY AUDIO & VIDEO
'* Vehicle Theft Protection
‘+ Superior Alarm installations
+ Pre-Loaded Alarms
+ Factory Security Upgrades
+ Reinsurance Products
+ Advanced Bluetooth Technology
* GPS Tracking Products
+ iPhone, iPod & MP3 Integration
+ Rear Back-up Cameras
+ Dent, Ding & Paint Repair
‘+ Wheel & Tire Protection
++ Service Contracts & GAP Insurance
```

## Slide 36

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
» Google Play Games Apps Movies&TV Books Kids. Gift Cards
Rockledge VR
Lightwave Technology
100+
Downloads
Install « Share 8] Add to wishlist
CO This app is available for some of your devices
About this app >
Add this virtual remote to control your Rockledge Vehicle Security System.
Everyone
Learn more
App support v
SS | Carlink BTLR
ve Lightwave Technology
"i
, 3.0%
```

## Slide 37

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
P> Google Play Games Apps Movies& TV Books Kids._— Gift Cards
Carlink BTLR
Lightwave Technology
10K+
Install on more devices < Share
£B This app is available for some of your devices
What's new
Thank you for using Carlink!
This update includes various bugfixes
a [€| Everyone
arn more
App support v
More appstotry >
Google Gemini
Google LLC
46%
Uber - Request a ride
Uber uber Technologies, Inc.
47*
```

## Slide 38

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Carlink BTLR_4.2.8_APKPure.apk
Be: Inputs
Source code
android.support.v4
androidx
app.com. lightwave.connected
models
FlavorApp
protocols
AdsTelematicsCompustarProtocol
AdsTelematicsOmegaProtocol
AdsTelematicsPolarStartProtocol
AdsTelematicsVoxxProtocol
AntennaProtocol
CompustarAdsProtocol
DirectedProtocol
FortinProtocol
IdppAdsTelProtocol
IdppProtocol
MidcityEngineeringProtocol
PosseProtocol
StandAloneProtocol
Cc
Cc
Cc
Cc
Cc
Cc
Cc
Cc
Cc
Cc
Cc
Cc
Cc
```

## Slide 39

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Carlink BTLR_4.2.8_APKPure.apk DIRECTED... ABOUTUS’ BRANDS~ SUPPORT’ CONTACT US~
B: Inputs
Source code Security, |
droid. t.v4 ‘
aa wees DS4 — The first fusion
androidx
app.com. lightwave.connected of fourteeh nologies
models DIRECTED's new DS4 technology makes our 54 |
Flavo rApp solutions simple, efficient and easier to execute,
protocols
c, AdsTelematicsCompustarProtocol
AdsTelematicsOmegaProtocol
AdsTelematicsPolarStartProtocol
AdsTelematicsVoxxProtocol
AntennaProtocol
CompustarAdsProtocol
DirectedProtocol
FortinProtocol
IdppAdsTelProtocol
IdppProtocol
MidcityEngineeringProtocol
PosseProtocol
StandAloneProtocol
c
c
c.
c
c
c
c.
c
¢ J
c
c,
c
```

## Slide 40

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Carlink BTLR_4.2.8_APKPure.apk
Be: Inputs
Source code
android.support.v4
androidx
app.com. lightwave.connected
models
FlavorApp
protocols a
c, AdsTelematicsCompustarProtocol . : P
c, AdsTelematicsOmegaProtocol ;
AdsTelematicsPolarStartProtocol
AdsTelematicsVoxxProtocol
AntennaProtocol
CompustarAdsProtocol
DirectedProtocol
FortinProtocol
IdppAdsTelProtocol
IdppProtocol
MidcityEngineeringProtocol
PosseProtocol
StandAloneProtocol
sine Started Successfully
```

## Slide 41

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Carlink BTLR_4.2.8_APKPure.apk
Be: Inputs
Source code
android. support.v4 ee ee Linke
androidx Tngjee Run Time . is
app.com. lightwave. connected e ce =\ i al Bee res
Locked/Unlocked Status ~ . ¥ 7 mn IED!
models Ondonanasesil a (2nd year $39.95)
FlavorApp > i j
- OMEGA delivers an unmatched J y of vehicle security, remote start,
pr otocols & convenience products. .
AdsTelematicsCompustarProtocol
AdsTelematicsOmegaProtocol
AdsTelematicsPolarStartProtocol
AdsTelematicsVoxxProtocol = a
AntennaProtocol zd “elon orca am
CompustarAdsProtocol
DirectedProtocol
FortinProtocol
IdppAdsTelProtocol
IdppProtocol
MidcityEngineeringProtocol
PosseProtocol
StandAloneProtocol
Cc
Cc
Cc
Cc
Cc
Cc
Cc
Cc
Cc
Cc
Cc
Cc
Cc
```

## Slide 42

## Pairing a CarLink BTLR

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
eLINK
CAR
& ill
ink
CarL
Pairing a
BTLR
```

## Slide 43

## Pairing a CarLink BTLR

1. Add a system

## Slide 44

## Pairing a CarLink BTLR

1. Add a system

2. Scan QR Code

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
System Setup
Pairing a CarLink
BTLR
1. Addasystem
2. Scan QR Code
```

## Slide 45

## Pairing a CarLink BTLR

1. Add a system

2. Scan QR Code

3. Set ignition on & Unlock doors

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
System Setup
Pairing a CarLink
BTLR
1. Addasystem
2. Scan QR Code
3. Set ignition on & Unlock doors
```

## Slide 46

## Pairing a CarLink BTLR

1. Add a system

2. Scan QR Code

3. Set ignition on & Unlock doors 4. Paired!

## Slide 47

Prefix MAC address

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ae Barcode content
BLX2200-IVU-F4-5E-AB-B1-EE-B5
Prefix MAC address
©@ Information on barcode
Format: QR Code
Error correction level: Low (~7%)
```

## Slide 48

# CarLink Disclosure

Jan 21, 2025 Disclosure Day.

…?

## Slide 49

**32K estimated total units**

## Slide 50

Final Takeaways

## Slide 51

# BLEʼs Default Security Lacks Access Control

**These systems need fine-grained, server-managed permissions. Vendors built their own application-layer security. They got it wrong.**

## Slide 52

Aftermarket Remote Control Is an Overlooked Attack Surface

**These systems bypass OEM security to control locks, alarms, immobilizers, and ignition.**

**One vulnerable product can affect many unrelated vehicle models.**

## Slide 53

# Fixing the Fleet Is Hard

**Owners may not know the system is installed. OEMs cannot fix devices they did not build. Check your car. Tell your friends.**

## Slide 54

Questions?
