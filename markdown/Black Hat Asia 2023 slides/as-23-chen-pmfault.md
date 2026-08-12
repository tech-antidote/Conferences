---
title: "PMFault"
speakers: ["Chen"]
conference: "Black Hat"
conference_full: "Black Hat ASIA 2023"
edition: "ASIA"
year: 2023
source_pdf: "Black Hat Asia 2023 slides/AS-23-Chen-PMFault.pdf"
pages: 21
sha256: "d4c6c5dfc01b7ac68da5dd1238d189a6025f95c78e6dc23d6f9247d62c6dfe12"
text_chars: 7667
ocr_pages: 2
has_ocr: true
redacted_secrets: 0
ocr_confidence: 87.0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T01:55:15Z"
---
# PMFault

**Speakers:** Chen  
**Conference:** Black Hat ASIA 2023  
**Source:** `Black Hat Asia 2023 slides/AS-23-Chen-PMFault.pdf` (21 pages)


## Slide 1

# **PMFault: Voltage Fault Injection on Session Title Server Platforms Through the PMBus**

**Zitai Chen** David Oswald (Z.Chen@pgr.bham.ac.ukSpeaker Name(s)/ (d.f.oswald@bham.ac.uk) zitaichen@outlook.com ) Professor PhD Student

University of Birmingham

#BHASIA @BlackHatEvents

## Slide 2

### Evolution of fault injection on Intel systems

##### Software-based (MSR 0x150)

Ref: Plundervolt [1] GitHub

##### Hardware-based (SVID Bus)

Teensy 4.0
SVID
？
Trigger
Ref: Voltpillager [2] Talk

Supermicro X11SSL-CF

[1] Kit Murdock et al. Plundervolt: Software-based Fault Injection Attacks against Intel SGX [2] Zitai Chen et al. VoltPillager: Hardware-based fault injection attacks against Intel SGX Enclaves using the SVID voltage scaling interface

## Slide 3

### What is PMBus?

36 SCL_P
SDA_P: PMBUS Data
35 SDA_P ？
SCL_P: PMBus Clock
34 ALT_P#
• I2C based
28 ALT#
• Semi-standardized protocol
27 SDIO SVID
• Standard commands
26 SCLK
• + Manufacturer-defined
commands

Ref: MP2965 <u>DataSheet</u> (Supermicro X11SSL-CF server motherboard uses MP2955)

## Slide 4

### Packet structure

Each device is assigned a 7-bit address What is the address for VRM?

From **PMBus Spec** and **MP2965** VRM datasheet

## Slide 5

### Attempt 0: From CPU? What is the VRM address?

~$ sudo modprobe i2c_i801 ~$ sudo i2cdetect 0 0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f [00-20]: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 30:     -- -- -- -- -- -- -- 37 -- -- -- -- -- -- -- -- 40:     -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 50:     50 -- -- -- -- -- -- -- 58 -- -- -- -- -- -- -- 60:     -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 70:     -- -- -- -- -- -- -- --

- -

- 12 devices Which one looks like VRM?

   - Response to common PMBus commands

   - The value returned make sense

~$ sudo i2cdetect 1 0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f 00:          -- -- -- -- -- 08 -- -- -- -- -- -- -- 10: 10 -- -- -- -- -- -- -- -- 19 -- -- -- -- -- -- 20: 20 --30: 30 -- ---- ---- ---- --35 36 ---- -- ---- ---- ---- ---- ---- ---- ---- ---READ_VOUT() < 0.55V 0x20 40: -- -- -- -- 44 -- -- -- -- -- -- -- -- -- -- -- && MFR_ADDR_PMBUS == ADDR 50: -- 51 -- -- -- -- -- -- -- -- -- -- -- -- -- -- 60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 70: -- -- -- -- -- -- -- --

- Next: Change the voltage!

## Slide 6

### Attempt 0: From CPU? Undervolt it!

- With libi2c – library for sending commands on I2C bus -

- 1. PMBus Override Mode > REG_VOUT_OPERATION -

- 2. Target Voltage > REG_VOUT_COMMAND -

- 3. SVID_OVERCLK2_EN (Bit 3) > REG_MFR_VR_CONFIG

**Stall…** 🫠

At least… we know the address of the VRM now.

🤔 CPU crashed or recoverable?

## Slide 7

#### " – Attempt 0.1: Try with EXPENSIVE" equipment Raspberry Pi

Luckily, we can use libi2c on RPi. No changes in code needed.

Send PMBus After setting Bit 3 of SVID_OVERCLK2_EN Voltage changed commands for but stall… undervolting

CPU is running Setting again! registers back

Fault injection on CRT-RSA? Success! ❓ Why 0.1 🥡 -- Requires“Opening the box”

## Slide 8

How to access PMBus?

> Text below was recovered by OCR (confidence 88/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
How to access PMBus?
SMBus/I2C Bus
| Ethernet 0
Board
Management
a Controller (BMC) Voltage
Regulator
(VRM)
BMC Flash suites
Chip Devices
```

## Slide 9

### Attempt 1: BMC

- How to run custom code on it or get SHELL?

   - - -

   - 22 (SSH) > gives “ATEN SMASH CLP SystemManagement Shell”

      - `shell sh? [1] ->` not working

   - Firmware reflashing?

      - Web Interface   – 🔒 BMC password, diversified in Supermicro Servers.

      - • `AlUpdate` – 🔥 No password required.

🔐

- Firmware package is “encrypted”

[1] **Exploiting the Supermicro Onboard IPMI Controller,** Available at: https://www.rapid7.com/blog/post/2013/11/15/exploiting-the-supermicro-onboard-ipmi-controller/

## Slide 10

### – BMC Vulnerability

### Firmware Upgrade

🤯

- Write tool to decrypt, modify and repack firmware, based on

   - smcbmc [2] tool and ipmi_firmware_tools [3]

- -

- Reverse engineered the firmware

   - `/SMASH/msh` provides the shell

   - Replace it with shell script with content `/bin/sh`

- -

- Re flash via KCS with `AlUpdate`

Firmware layout is mostly the same as described by Eclypsium![1]

- SSH and successfully get root shell !!! • - PMBus Implement libi2c by hand

[1] **Insecure Firmware Updates in Server Management Systems,** Available at: <u>https://eclypsium.com/2018/09/06/insecure-firmware-updates-in-server-management-systems/</u> [2] <u>https://github.com/c0d3z3r0/smcbmc</u>

[3] <u>https://github.com/devicenull/ipmi_firmware_tools</u>

## Slide 11

### Attack 1: Undervolting

• – Fault injection on SGX WITHOUT physical access Plundervolt revived! 🎉 • - Stability test with CRT RSA fault injection (in SGX):

Not
Exploitable
No fault Other 51%
23% 77%
Exploitable
26%
No fault Not Exploitable Exploitable

**253 tests in 545 mins, on average 9 mins for a useful fault**

## Slide 12

### – Things happen server is broken

🌛 One day at 3:00AM

Why is my undervolting code not working! ( 😴 Dream coding 😴 )

VID_STEP_SEL MFR_VR_CONFIG? VR_CONFIG!!

Reset it to 0x00 try again™!!

## Slide 13

### Attack 2: Overvolting

2.84V!

<u>https://youtu.be/hXuidPexanM?t=88</u>

> Text below was recovered by OCR (confidence 86/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
Attack 2: Overvolting
UL 20M
Freq Probe
Rise Tima ? AVI Invert
Fall Time Volts/Div
+Width Unit
```

## Slide 14

### Attack 2: Overvolting

VID_STEP_SEL MFR_VR_CONFIG (p104 of <u>MP2965 Datasheet)</u>

Bit 8: VID_STEP_SEL 1’b0: 10mV per VID step 1’b1: 5mV per VID step With 10mV per VID step Vcpu can be up to 3V!!! (CPU spec: 1.52V max)

## Slide 15

### We have BMC, maybe use ipmitool?

- `ipmitool i2c`

   - directly interact with I2C buses on the BMC

   - Via KCS: same, not need to login to BMC.

• via Via Ethernet: login required (password can be cleared with `ipmitool` KCS)

No need to reflash the firmware anymore, instead: **`sudo ipmitool`** `user set name` **`sudo ipmitool`** `user set password` **`sudo ipmitool`** `channel setaccess`

\```
ipmitooli2c (Via Ethernet)
\```

## Slide 16

Delayed-Write Fault – Practical Exploitation

### I think this attack is nicer than the VoltPillager NUC

Less messy

## Slide 17

### Tested on

- - -

- Supermicro X11SSL CF Vulnerable

- Supermicro X11SPG-TF and X11SSE-F

   - VRM reachable with default config, undervolting crashed the server

   - Didn’t try overvolting as it was kindly provided by a friend

- Supermicro X12DPi-NT - NOT Vulnerable

- Responsible disclosed to Supermicro, see <u>security advisory</u>

## Slide 18

### Black Hat Sound Bytes

- Think of a server as an embedded system

   - Vulnerability/functionality in one component --> rest of the system

   - • Software + hardware

- SGX security

   - SGX attestation cannot measure BMC firmware

- Improper jumper configuration can cause security issues

   - LPC, SMBus, SPI, I2C, PCIE…

## Slide 19

### PMBusDetect Tool

$ sudo modprobe i2c_i801 $ sudo ./pmbusdetect -d /dev/i2c-1 Device 0x20              READ_TEMPERATURE success: 0019 !!!!!!!!!!! Detected! Device addr: 20 !!!!!!!!!!! Device 0x20              SVID_VENDOR_PRODUCT_ID success, data: 2555 This device is likely to be a MPS VRM # Save the page Device 0x20 : 00         READ_PAGE success Page: 00 Device 0x20 : 00         WRITE_PAGE success Device 0x20 : 00         READ_VOUT success: 00D8 Page: 01 Device 0x20 : 01         WRITE_PAGE success Device 0x20 : 01         READ_VOUT success: 0001 # Restore the page Device 0x20 : 00         WRITE_PAGE success

Currently only tested with ISL68137 and MP2955. Contributions are welcome.

<u>https://github.com/zt-chen/PMFault</u>

## Slide 20

### Acknowledgements

- This research is partially funded by the Engineering and Physical Sciences Research Council (EPSRC) under grants EP/R012598/1, EP/R008000/1, and EP/V000454/1.  The results feed into DsbDtech.

- -

- We would also like to thank Supermicro for providing a X12DPi NT6 server for further investigation of the issue.

## Slide 21

## Thank You!

GitHub Repo

PMFault Website
