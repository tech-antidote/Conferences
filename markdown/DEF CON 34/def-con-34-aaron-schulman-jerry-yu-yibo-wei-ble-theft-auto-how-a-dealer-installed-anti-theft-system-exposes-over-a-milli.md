---
title: "BLE Theft Auto How a Dealer-Installed Anti-Theft System Exposes Over a Million Cars to Theft"
speakers: ["Aaron Schulman", "Jerry Yu", "Yibo Wei"]
conference: "DEF CON"
conference_full: "DEF CON 34"
edition: "34"
year: 2026
source_pdf: "DEF CON 34/DEF CON 34 - Aaron Schulman, Jerry Yu, Yibo Wei - BLE Theft Auto How a Dealer-Installed Anti-Theft System Exposes Over a Million Cars to Theft - BTA.pdf"
pages: 54
sha256: "a9680a675a47c3f534a8767a95008c944926d0253a2f64812e075ca0eeafc1ba"
text_chars: 16927
ocr_pages: 21
has_ocr: true
redacted_secrets: 0
ocr_confidence: 88.3
ocr_unreliable_blocks: 0
vision_verified_pages_changed: 48
vision_verified_pages: 54
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T06:19:21Z"
---
# BLE Theft Auto How a Dealer-Installed Anti-Theft System Exposes Over a Million Cars to Theft

**Speakers:** Aaron Schulman, Jerry Yu, Yibo Wei  
**Conference:** DEF CON 34  
**Source:** `DEF CON 34/DEF CON 34 - Aaron Schulman, Jerry Yu, Yibo Wei - BLE Theft Auto How a Dealer-Installed Anti-Theft System Exposes Over a Million Cars to Theft - BTA.pdf` (54 pages)


## Slide 1

# BLE Theft Auto

UC San Diego

Aaron Schulman

Yibo Wei

Jerry Yu

Nishant Bhaskar

Sumanth Rao

Jefferson Chien

Mohak Vaswani

Christian Dameff

## Slide 2

⚠ If you own one of the ~2 million cars that has ⚠

THIS STICKER on your driverʼs side

or sometimes

KARR SECURITY SYSTEMS

powered by SWDS

PROTECTED BY SWDS

KARR Security System

SCAN AND UPDATE NOW!

Yes, even if itʼs “deactivated ˮ

## Slide 3

# Smartphones are remote controls for vehicles

**Capabilities:**

- Unlock doors

- Immobilizer

- Horn

- Lights

- Remote starter

**Wireless Protocols:**

- Cellular

- Bluetooth

Tesla app

## Slide 4

# Car remote control systems have had vulnerabilities

**Cellular**

- Cellular telematics → CAN

   - Checkoway et al. (2011)

- Cellular head unit → CAN

   - Miller and Valasek (2015)

- Cellular TCU → critical ECUs

   - Keen Security Lab (2018)

**Bluetooth**

- Co-located malicious BLE app → infotainment → CAN

   - Checkoway et al. (2011)

- BLE phone key relay → Body control

   - NCC Group (2022)

   - GoGoByte (2023)

## Slide 5

## One wireless protocol is more sketchy than the other

**Cellular: Long-range attack**

Inherits robust security protocols

- Cellular security is robust

   - SIM card authentication

   - OTA encryption

- Web security is robust

   - Authentication: OAuth2

   - Encryption: HTTPS

- Automatic OTA firmware updates

**Bluetooth: Short-range attack**

YOLO letʼs make custom security

- BLE sec. is not compatible with cars

   - Revoking experience is cumbersome

   - Access sharing is impossible

   - Co-located apps are threats

- Manual user-driven updates

## Slide 6

# OEM BLE control is battle tested.   Aftermarket is…   ???

**OEM System**

Built-in to every vehicle of make/model

- Standardized BLE security protocols (e.g., CCC digital key)

   - Tested by many

**Aftermarket System**

Adding BLE remote control to any car

- Hand-rolled BLE security protocols

- Bypasses OEM security

   - Cut and spliced into wiring

   - 3rd party vendor

   - 3rd party installer

## Slide 7

# That sounded great.

**Real talk:**

Why did we actually study aftermarket BLE security systems?

_Science only follows a straight line in retrospect_ ™

## Slide 8

# ⏱ 2018:  Finding BLE-based skimmers in gas pumps

## Slide 9

## “QT *******ˮ named devices were everywhere in SoCal

- **Seen commonly at gas stations**

- **We thought we hit the skimmer jackpot**

- **Then we also saw them at gas stations, parking lots, on highways, etc.**

```text
QT 0008***
QT 0010***
QT 0016***
QT 0029***
QT 0184***
QT 0199***
QT 0201***
QT 0212***
QT 0217***
QT 0220***
```

## Slide 10

# ⏱ 2024:  We try Google.

QT FCCID

fccid.io

https://fccid.io › 2ASRL › 2ASRL-1069

**1069 QT Solutions Bluetooth Sensor User Manual ... - FCC ID**

QT Solutions Bluetooth Sensor User manual details for FCC ID 2ASRL-1069 made by QT Solutions PTY LTD. Document Includes User Manual.

FCC Report

https://fcc.report › company › Qt-Solutions-Pty-L-T-D

**QT Solutions PTY LTD FCC Filings**

Experimental, International, and equipment registration filings filed with the FCC by QT Solutions PTY LTD

fccid.ai

https://fccid.ai › Quantum5x Systems Inc.

**QT-300 Module - FCC Certification**

FCC certification details for QT-300 Module. Product. Frequencies: 525-600 MHz. General Mobile Radio And Broadcast Services equipment

fccid.io

https://fccid.io › 2ASYF

## Slide 11

FCC ID

FCC ID, company, model

Search

FCC ID / 2ASRL / 2ASRL-1069 / User manual

## 1069 QT Solutions Bluetooth Sensor User Manual QT Solutions PTY

FCC ID 2ASRL-1069

User manual

QT Solutions Bluetooth Sensor

by QT Solutions PTY LTD

SWDS

KARR Security Systems

BT SERIES

CUSTOMER USER GUIDE

Congratulations on your purchase of the KARR BT system, designed with convenient, selectable features and a user friendly mobile app to provide you the best in electronic vehicle security.

Read this manual to become familiar with the productʼs functions and features, ensuring that you are able to use the system to your advantage.

CONTENTS   PG

## Slide 12

SETTINGS

These settings can only be changed once you connect the KARR BT app to the vehicle.

**Silent Arm/Lock Disarm/Unlock.** Enabling this setting will turn off normal arm/lock and disarm/unlock honks from the BT system. This does not affect vehicle factory settings. As long as this setting is enabled, the BT system will always be in silent arm/lock and disarm/unlock mode.

In addition, the temporary selection discussed in “KARR BT System Functionsˮ will now only show two icons.

**Disable Door Trigger:** Prevents Door Trigger zone from engaging the BT system.

**Disable Trunk**: Prevents the trunk from engaging the BT system.

**Disable Shock Sensor Triggers:** Prevents impact to the vehicle from engaging the BT system.

**Auto Lock upon Ignition On**: Vehicle doors will lock upon turning “Onˮ the ignition and closing all doors.

**Auto Unlock upon Ignition Off**: Vehicleʼs door locks will unlock immediately upon turning to the “Offˮ position.

ARM MODE

**Active Arm:** Also known as manual arming. Refer to “KARR BT System Functionsˮ on page two, “Active Arming of the BT System,ˮ when using your vehicleʼs keyless entry remote.

**Your system is defaulted to Active Arm.**

**Passive Arm:** The system will arm 30 seconds after all points of entry have been cleared.

If any door or trunk is opened, this will interrupt the arming countdown. Once all the entry points are closed, the countdown will start over for the full 30 seconds

When selecting Passive Arm, an additional option to lock doors automatically upon Passive Arm will become available. The default setting is of; simply press the switch to toggle the feature on or off. Vehicle doors will now lock with the completion of the Passive Arm countdown.

**If you are locked out of your vehicle due to passive arming and your keys and connected phone are in your vehicle, the BT system will disconnect from your phone after approximately 45 seconds to one minute so that you may connect with another device that has the KARR BT app installed to unlock your vehicle.**

SHOCK SENSOR

The Shock Sensor can be adjusted by sliding the button from zero on the left to as high as 15 on the right.

Depending on the size of your vehicle, adjustment selection will vary. Too low a number may not render any response, while too high a number may render an unwanted response.

At the time of installation, your vehicle Shock Sensor has been calibrated and tested. If you wish to make adjustments, this may adversely affect the performance of the Shock Sensor.

We strongly recommend contacting our customer service department if you wish to make changes to your Shock Sensorʼs sensitivity so that a technician may properly perform a new calibration.

BACK   UNIT SETTINGS

5YFBU4EE6DP999998

QT 5958868

BLACK

TOYOTA  COROLLA

Silent Lock and Unlock

Disable Door Trigger

Disable Trunk Trigger

Disable Shock Sensor Triggers

Auto Lock upon Ignition On

Auto Unlock upon Ignition Off

Arm Mode

Active Arm

Shock Sensor Sensitivity

SAVE SETTINGS

## Slide 13

5YFBU4EE6DP999998

**QT 5958868**

BLACK

TOYOTA  COROLLA

Auto Unlock upon Ignition Off

Arm Mode

Active Arm

Shock Sensor Sensitivity

8

SAVE SETTINGS

Depending on the size of your vehicle, adjustment selection will vary. Too low a number may not render any response, while too high a number may render an unwanted response.

At the time of installation, your vehicle Shock Sensor has been calibrated and tested. If you wish to make adjustments, this may adversely affect the performance of the Shock Sensor.

We strongly recommend contacting our customer service department if you wish to make changes to your Shock Sensorʼs sensitivity so that a technician may properly perform a new calibration.

## Slide 14

### What does KARR Security do for my vehicle?

Your KARR Security system is an advanced anti-theft solution, designed to go beyond your manufacturerʼs alarm. Itʼs like an upgrade for your carʼs security! This gives you extra peace of mind and fewer worries.

## Slide 15

Placeholder demo video

## Slide 16

### How do I get a KARR Security system for my vehicle?

We partner with more than 3,000 car dealerships nationwide. Since we only work with dealerships, give us a call— weʼll connect you with the nearest one.

## Slide 17

# Dealer-Installed aftermarket remote control ecosystem

**Acrisure Protection Group**

Designs and sells the security system

**Dealers (SoCal)**

Install the device on every car they sell for lot security and $$$

**Car Buyers**

Pay for access to the system (0–$1,200) or refuse it

## Slide 18

### How does the KARR system work?

- **AFTERMARKET REMOTE CONTROL MODULE** — talks over Bluetooth to the **AFTERMARKET REMOTE CONTROL APP** on the phone (lock, unlock, and ENGINE START / STOP controls)

- The module is spliced into the **STARTER** wire (cut) and onto the **CAN BUS OR DISCRETE WIRES** that also carry the **IN-VEHICLE SWITCHES & BUTTONS**

- Endpoints wired to the module: **ENGINE**, **LIGHTS**, **HORN**, **DOORS**, **TRUNK**

**Installer**

Splices the system into a carʼs wiring and hides it behind the dash

## Slide 19

# Breaking KARR: The App Reverse Engineered

- Client → Server: `Login (username/pwd)`

- Server → Client: `Session API Token`

- Client → Server: `Get User Vehicles`

- Server → Client: `(User Vehicle, QT name)`

- KARR → Client: `BLE Advertisements`

- Client: _Filter by QT names belonging to user_

- Client → KARR: `READ_MODE`

- KARR → Client: `REQUEST_AUTH`

- Client → KARR: `PROVIDE_AUTH`

- KARR → Client: `AUTH_SUCCESS`

- Client → KARR: `UNLOCK_DOORS`

- KARR → Client: `ACK_OK`

**Server-client authentication** has nothing to do with **client-device authentication**.
**Access control** is only at UI level.

## Slide 20

# Breaking KARR: The App Reverse Engineered

- Client → Server: `Login (username/pwd)`

- Server → Client: `Session API Token`

- Client → Server: `Get User Vehicles`

- Server → Client: `(User Vehicle, QT name)`

- KARR → Client: `BLE Advertisements`

- Client: _Filter by QT names belonging to user_

- Client → KARR: `READ_MODE`

- KARR → Client: `REQUEST_AUTH`

- Client → KARR: `PROVIDE_AUTH`

- KARR → Client: `AUTH_SUCCESS`

- Client → KARR: `UNLOCK_DOORS`

- KARR → Client: `ACK_OK`

## Slide 21

# The KARR Authentication Vulnerability

**REQUEST_AUTH challenge:**

A random byte array.

**PROVIDE_AUTH response:**

1. Device name: “QT xx…xxˮ ✔

2. Device mode enum ✔

3. Challenge bytes ✔

4. Secret key ✔

5. “hashˮ

6. Profit! (AUTH_SUCCESS)

Ensures commands are only accepted by the intended device, but offers **no real security.**

- KARR → “Clientˮ: `BLE Advertisements`

- “Clientˮ → KARR: `READ_MODE`

- KARR → “Clientˮ: `REQUEST_AUTH`

- “Clientˮ → KARR: `PROVIDE_AUTH`

- KARR → “Clientˮ: `AUTH_SUCCESS`

- “Clientˮ → KARR: `UNLOCK_DOORS`

- KARR → “Clientˮ: `ACK_OK`

## Slide 22

# Attempted Implementation of User Privileges

Mode Change runs from Higher at the top to Lower Privilege at the bottom:

- **Installer** — Firmware Update, Headlights & Horn

- **Dealer** — _accepted_ ($$$) → **User** — Door/Trunk Lock & Immobilizer

- **Dealer** — _rejected_ → **No Sale** — **Disabled**

X Doubt

## Slide 23

# Attempted Implementation of User Privileges

Mode Change runs from Higher at the top to Lower Privilege at the bottom:

- **Installer** — Firmware Update, Headlights & Horn

- **Dealer** — _accepted_ ($$$) → **User** — Door/Trunk Lock & Immobilizer

- **Dealer** — _rejected_ → **No Sale** — **Disabled** *

_* Still beacons and connectable when the engine is running_

_** Accepts ONE control command:_ **CHANGE_MODE**

## Slide 24

# Demystifying “No Saleˮ Mode

- **Locate KARR vehicle** → **No Sale mode?**

- **No Sale mode?** — NO → **Compromised**

- **No Sale mode?** — YES → **Engine running?**

- **Engine running?** — NO → loop back to **Engine running?** _(Wait till vehicle starts)_

- **Engine running?** — YES → **Change Mode** → **Compromised**

## Slide 25

# Our Super Cool App

Placeholder for demo mayhem mode demo video

← COMMAND

- LOCK

- UNLOCK

- HORN

- LIGHTS

- MAYHEM

## Slide 26

# What can we do?

**Vehicle Entry**

Trivially compromised by unlocking the doors.

**Stranding a car**

Immobilization possible for vehicle ownerʼs without app access.

**Vehicle Theft**

For some vehicles, an attacker can use a locksmithing tool to create a duplicate key to start the engine and drive away.

## Slide 27

# Breaking KARR: How to Target a KARR…Car?

Method #1: Use WiGLE to find where clusters of KARR devices appear.

Method #2: Walk around with a BLE scanner till you find a “QTˮ or “DRˮ device.

Method #3: They do come with a great big sticker.

Method #4: If in Southern California, go outside.

## Slide 28

# Measuring the scale of the vulnerability

Downloaded many KARR devices on <u>Wigle.net</u>

Found KARR MAC addresses are assigned sequentially

Created a new MAC population inference method

```text
xx:xx:xx:xx:xx:01
xx:xx:xx:xx:xx:02
xx:xx:xx:xx:xx:03
xx:xx:xx:xx:xx:04
xx:xx:xx:xx:xx:05
xx:xx:xx:xx:xx:06
xx:xx:xx:xx:xx:07
xx:xx:xx:xx:xx:08
xx:xx:xx:xx:xx:09
xx:xx:xx:xx:xx:0a
xx:xx:xx:xx:xx:0b
xx:xx:xx:xx:xx:0c
xx:xx:xx:xx:xx:0d
xx:xx:xx:xx:xx:0e
xx:xx:xx:xx:xx:0f
```

## Slide 29

### Measuring the Scale of the Vulnerability

- KARR Mac addresses are assigned mostly sequentially

- <u>WiGLE.net</u> has a very good sample of all deployed KARR alarms

The addresses seen on WiGLE, next to the full sequential MAC range with the seen addresses highlighted:

| MAC | In WiGLE sample |
|---|---|
| xx:xx:xx:xx:xx:01 | yes |
| xx:xx:xx:xx:xx:02 | yes |
| xx:xx:xx:xx:xx:03 | no |
| xx:xx:xx:xx:xx:04 | yes |
| xx:xx:xx:xx:xx:05 | no |
| xx:xx:xx:xx:xx:06 | yes |
| xx:xx:xx:xx:xx:07 | yes |
| xx:xx:xx:xx:xx:08 | no |
| xx:xx:xx:xx:xx:09 | yes |
| xx:xx:xx:xx:xx:0a | no |
| xx:xx:xx:xx:xx:0b | yes |
| xx:xx:xx:xx:xx:0c | yes |
| xx:xx:xx:xx:xx:0d | no |
| xx:xx:xx:xx:xx:0e | no |
| xx:xx:xx:xx:xx:0f | yes |

## Slide 30

### Measuring the Scale of the Vulnerability

- KARR Mac addresses are assigned mostly sequentially

- <u>WiGLE.net</u> has a very good sample of all deployed KARR alarms

- We measure the “densityˮ of <u>WiGLE.net</u> samples

Three sampled MAC ranges at increasing density (highlighted = address present in the sample):

| MAC | 0.31 | 0.56 | 0.88 |
|---|---|---|---|
| xx:xx:xx:xx:xx:01 | yes | yes | yes |
| xx:xx:xx:xx:xx:02 | no | yes | yes |
| xx:xx:xx:xx:xx:03 | no | no | yes |
| xx:xx:xx:xx:xx:04 | no | yes | yes |
| xx:xx:xx:xx:xx:05 | no | no | no |
| xx:xx:xx:xx:xx:06 | yes | yes | yes |
| xx:xx:xx:xx:xx:07 | yes | yes | yes |
| xx:xx:xx:xx:xx:08 | no | no | yes |
| xx:xx:xx:xx:xx:09 | yes | yes | yes |
| xx:xx:xx:xx:xx:0a | no | no | yes |
| xx:xx:xx:xx:xx:0b | no | yes | yes |
| xx:xx:xx:xx:xx:0c | no | yes | yes |
| xx:xx:xx:xx:xx:0d | no | no | yes |
| xx:xx:xx:xx:xx:0e | no | no | no |
| xx:xx:xx:xx:xx:0f | yes | yes | yes |

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

Map legend: 1K, 10K, 100K, 1M

## Slide 33

# Mitigations from KARR

Jan 21, 2025

Disclosure Day.
Productive meeting with Acrisure representatives. Discussed solutions.

Aug 2, 2025

Received initial prototype patched device and app.

18 MONTHS LATER…

Jul 20, 2026

Patch was rolled out to customers.

## Slide 34

# Mitigations from KARR

**Interim fix**

- Removing the universal key from the source code.

- Removing the compromised APKs from the web.

**Full patch**

- Firmware update to replace the global key.

- Fully disabling devices in _No Sale_ mode.

- _For paying customers with KARR accounts:_

   - Push notification from app to update firmware.

- _For non-paying customers with “inactiveˮ alarms:_

   - Download app, verify with VIN number to get the firmware update, which should fully disable their KARR devices.

## Slide 35

# Finding similar systems…

ROCKLEDGE SECURITIES

About Us   Products / Support   Photos   Install Videos   Careers   Contact

## Vehicle Protection and Security Systems

Over 20 Years of Experience delivering quality, convenient and reliable products.

Download the Rockledge Mobile App

Download on the App Store

GET IT ON Google Play

Scan QR code to download

**AUTO SECURITY**

- Superior Alarm Installations

- Pre-Loaded Alarms

- Factory Security Upgrades

- Reinsurance Products

**AUDIO & VIDEO**

- Advanced Bluetooth Technology

- GPS Tracking Products

- iPhone, iPod & MP3 Integration

- Rear Back-up Cameras

**INSURANCE**

- Vehicle Theft Protection

- Dent, Ding & Paint Repair

- Wheel & Tire Protection

- Service Contracts & GAP Insurance

## Slide 36

Google Play

Games   Apps   Movies & TV   Books   Kids   Gift Cards

## Rockledge VR

Lightwave Technology

100+ Downloads

Install   Share   Add to wishlist

This app is available for some of your devices

About this app →

Add this virtual remote to control your Rockledge Vehicle Security System.

Updated on

Everyone

Learn more

App support

Carlink BTLR

Lightwave Technology

3.0 ★

## Slide 37

Google Play

Games   Apps   Movies & TV   Books   Kids   Gift Cards

## Carlink BTLR

Lightwave Technology

3.0 ★ — 47 reviews

10K+ Downloads

Install on more devices   Share

This app is available for some of your devices

Whatʼs new

Thank you for using Carlink!
This update includes various bugfixes.

Everyone

Learn more

App support

More apps to try →

Google Gemini — Google LLC — 4.6 ★

Uber - Request a ride — Uber Technologies, Inc. — 4.7 ★

## Slide 38

```text
Carlink BTLR_4.2.8_APKPure.apk
  Inputs
  Source code
    android.support.v4
    androidx
    app.com.lightwave.connected
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
```

## Slide 39

```text
Carlink BTLR_4.2.8_APKPure.apk
  Inputs
  Source code
    android.support.v4
    androidx
    app.com.lightwave.connected
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
```

`DirectedProtocol` is highlighted.

DIRECTED.voxx

ABOUT US   BRANDS   SUPPORT   CONTACT US   WHERE TO BUY

Security.

## DS4 — The first fusion of four technologies

DIRECTEDʼs new DS4 technology makes our solutions simple, efficient and easier to execute.

EXPERIENCE DS4

**Retailers:** When you become an Authorized DIRECTED Dealer, we become your business partner. Become a Dealer!

## Slide 40

```text
Carlink BTLR_4.2.8_APKPure.apk
  Inputs
  Source code
    android.support.v4
    androidx
    app.com.lightwave.connected
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
```

`FortinProtocol` is highlighted.

FRANÇAIS   MY ACCOUNT   REGISTER

FORTIN

PRODUCTS   SOLUTIONS   RESOURCES   SUPPORT   WHERE TO BUY

QUICK VEHICLE FINDER: Make / Year / Model / Trim

## REMOTE START. SECURITY. CONNECTIVITY AND TRACKING.

Opt for EVO products and get everything you need with a single brand to connect, remote control, secure and track your vehicles.

LEARN MORE

EVO START

…ine Started Successfully

This website uses cookies to ensure you get the best user experience. By continuing to browse our site, you are agreeing to our use of cookies.   Learn More   Continue

## Slide 41

```text
Carlink BTLR_4.2.8_APKPure.apk
  Inputs
  Source code
    android.support.v4
    androidx
    app.com.lightwave.connected
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
```

`AdsTelematicsOmegaProtocol` is highlighted.

Established 1970 — OMEGA — RESEARCH & DEVELOPMENT TECHNOLOGIES, INC. — LEGENDARY VEHICLE SECURITY

My account   Log in   Cart (0)

Search Products & Guides   All

SECURITY & CONVENIENCE   PRODUCTS   ACCESSORIES   SUPPORT   ABOUT US   CONTACT US

Linkr MOBILE, with callouts:

- Selectable Vehicle Image

- Displays Remaining Engine Run Time

- Run Time Extender

- Locked/Unlocked Status

- Ondemand Locate

NEW LINKR-LT

_First Year Of Service_ **INCLUDED!**

(2nd year $39.95)

ANDROID APP ON Google play   Available on the App Store

_OMEGA_ delivers an unmatched _legacy of vehicle security, remote start, & convenience_ products.

Since 1971, Omega thrives on a tradition of unsurpassed quality & value with legendary vehicle security & remote start brands such as Excalibur & K-9. Weʼre continuing that tradition with more lifestyle innovations year after year!

**LINKR-MBT**

Smartphone Control

**Control | Share | Program**

- Uses Bluetooth to control your car from virtually anywhere!

## Slide 42

## Pairing a CarLink BTLR

9:41

CAR·LINK™

12.5

00:00

66°F

Doors unlocked

## Slide 43

## Pairing a CarLink BTLR

1. Add a system

My car

Add a system

## Slide 44

## Pairing a CarLink BTLR

1. Add a system

2. Scan QR Code

System Setup

By scanning ….

QR Code

OR

Antenna near me

## Slide 45

## Pairing a CarLink BTLR

1. Add a system

2. Scan QR Code

3. Set ignition on & Unlock doors

System Setup

SET IGNITION TO ON

MY IGNITION IS ON

## Slide 46

## Pairing a CarLink BTLR

1. Add a system

2. Scan QR Code

3. Set ignition on & Unlock doors

4. Paired!

CAR·LINK™

12.5

00:00

77°F

Doors unlocked

## Slide 47

QR Code

**Barcode content**

`BLX2200-IVU-F4-5E-AB-B1-EE-B5`

`BLX2200-IVU-` is the **Prefix**; `F4-5E-AB-B1-EE-B5` is the **MAC address**.

**Information on barcode**

Format: QR Code

Error correction level: Low (~7%)

## Slide 48

# CarLink Disclosure

Jan 21, 2025 Disclosure Day.

…?

## Slide 49

**32K estimated total units**

Map legend: 10, 100, 1K, 10K

## Slide 50

Final Takeaways

## Slide 51

# BLEʼs Default Security Lacks Access Control

**These systems need fine-grained, server-managed permissions.**

**Vendors built their own application-layer security.**

**They got it wrong.**

## Slide 52

Aftermarket Remote Control Is an Overlooked Attack Surface

**These systems bypass OEM security to control locks, alarms, immobilizers, and ignition.**

**One vulnerable product can affect many unrelated vehicle models.**

## Slide 53

# Fixing the Fleet Is Hard

**Owners may not know the system is installed.**

**OEMs cannot fix devices they did not build.**

**Check your car. Tell your friends.**

## Slide 54

Questions?
