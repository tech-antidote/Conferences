---
title: "Watch Your Phone Novel USB-Based File Access Attacks Against Mobile Devices"
speakers: ["Florian Draschbacher", "Lukas Maar"]
conference: "Black Hat"
conference_full: "Black Hat ASIA 2025"
edition: "ASIA"
year: 2025
source_pdf: "Black Hat Asia 2025 Slides/Florian Draschbacher & Lukas Maar_Watch Your Phone Novel USB-Based File Access Attacks Against Mobile Devices.pdf"
pages: 36
sha256: "81d3a80819369f49fdeb645c17c610a9830853fb45e20ccd86f76c78e89459b8"
text_chars: 14075
ocr_pages: 2
has_ocr: true
redacted_secrets: 0
ocr_confidence: 93.1
ocr_unreliable_blocks: 0
vision_verified_blocks: 1
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T03:52:37Z"
---
# Watch Your Phone Novel USB-Based File Access Attacks Against Mobile Devices

**Speakers:** Florian Draschbacher, Lukas Maar  
**Conference:** Black Hat ASIA 2025  
**Source:** `Black Hat Asia 2025 Slides/Florian Draschbacher & Lukas Maar_Watch Your Phone Novel USB-Based File Access Attacks Against Mobile Devices.pdf` (36 pages)


## Slide 1

WATCH YOUR PHONE Novel USB-Based File Access Attacks Against Mobile Devices

**Florian Draschbacher & Lukas Maar**

#BHAS @BlackHatEvents


> Recovered by OCR — confidence 92/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
bleak hat
ASIA 2025
APRIL 3-4, 2025
BRIEFINGS
WATCH YOUR PHONE
Novel USB-Based File Access Attacks Against Mobile Devices
Florian Draschbacher & Lukas Maar
#BHAS
```

## Slide 2

About Us We are PhD students at Graz University of Technology’s Institute of Information Security

Florian Draschbacher florian.draschbacher@tugraz.at

Research Areas:

- Mobile Security

- Application Analysis

- Hardware Aspects

Research Areas: Lukas Maar • System Security lukas.maar@tugraz.at

- Kernel Security

- Side-Channel Security

#BHAS @BlackHatEvents

## Slide 3

# Introduction

- Mobile devices store sensitive user data

   - Pictures, Messages, Credentials, …

- USB connectivity is a known attack vector

   - Extract data, compromise device

- **We present novel USB data extraction attacks for two scenarios:**

   - Manipulated Chargers: Attacker needs to bypass user prompts

   - Physical Access: Attacker needs to bypass lock screen

#BHAS @BlackHatEvents

## Slide 4

# History of USB Attacks

### **Manipulated USB Devices**

**Physical Access**

Exploit high-level trust model

Exploit individual low-level flaws

- **Malicious Hosts** JuiceJacking (2011) Mitigated with user prompts

- • **Malicious Peripherals** BadUSB (2014-) JuiceFilming (2016-) Ghosttalk (2022-)

- **Example: Checkm8 (2019)** Code execution through Use-After-Free in USB stack

- • **Commercial forensics tools** Cellebrite UFED (2008-) MSAB XRY (2009-) Magnet GrayKey (2017-)

#BHAS @BlackHatEvents

## Slide 5

# Background: USB on Mobile

Image: Kyu3 / CC BY-SA 4.0 / wikimedia

- Mobile devices use multi-function USB-C ports

- **Power** Charge phone or supply peripherals

• **USB** Data exchange with PC or peripherals • **USB Power Delivery** Negotiation of power and data roles **Still:** A USB port **either** acts as USB host or USB device at a given time

#BHAS @BlackHatEvents

## Slide 6

Background: USB File Access on Mobile User prompts mitigate malicious chargers that extract files (“JuiceJacking”)

1. User connects device to USB Host (computer)

2. MTP interface doesn’t yet show any files

3. User unlocks screen

4. User accepts prompt / changes USB mode

5. Files show through MTP

#BHAS @BlackHatEvents

## Slide 7

Manipulated Charger Attacks Bypassing JuiceJacking Mitigations On State-of-the-Art Mobile Devices

#BHAS @BlackHatEvents

## Slide 8

# Attack Setup

- **Attacker plants malicious phone charger** Reflashed firmware or exchanged electronics

- **Charger attacks any charging mobile device** Data extraction, …

- **Easy to mount in public places** Chargers at airports, museum, hotel rooms, …

#BHAS @BlackHatEvents

## Slide 9

Key Observations on JuiceJacking Mitigations **Goal:** Ensure user consciously enables USB file access

**1. Require Screen Unlock Idea:** Subsequent actions executed by legitimate owner **Observation:** Users routinely unlock screen while charging

**2. Require User Consent Idea:** USB partner cannot establish MTP and inject input at same time **Flaw** : Impossible by USB specification, but possible in practice!

#BHAS @BlackHatEvents

## Slide 10

# Attack: ChoiceJacking via PD & BT HID **Use USB PD to switch USB data roles, hide BT device in charger**

Charger Mobile Dev. BT Input Dev. 1. A%ach to Charger 3. BT MAC visible 2. Inject input to start BT scanning 4. Ini?ate BT input connec?on 5. Inject input to accept Pairing Request YES No 6. USB PD Data Role Swap 7. Start MTP handshake USB Data Access 8. Inject input to accept GRANT CANCEL 9. Retrieve MTP files

#BHAS @BlackHatEvents

## Slide 11

# Attack: ChoiceJacking via AOAP **Android Open Accessory Protocol (AOAP)** Allows USB host to inject input events, even if not in accessory mode

1. Connect Android device to malicious charger

2. Initiate MTP connection to trigger user prompt

3. Inject input events through AOAP to confirm prompt

4. Stealthily access files from device

**Android Patch Pending**

#BHAS @BlackHatEvents

## Slide 12

## Demo: Access Files on Samsung Galaxy A14

#BHAS @BlackHatEvents

## Slide 13

Physical Access Attacks on Android Entirely bypassing lock screen and user consent prompts

#BHAS @BlackHatEvents

## Slide 14

# Attack Setup

- **Assumption** : Physical device access

- **Assumption** : Unlocked once since last reboot

- **Note** : Android Disk Encryption only effective until first unlock after boot

Source: developer.android.com

#BHAS @BlackHatEvents

## Slide 15

Media Transfer Protocol (MTP)
USB Host Mobile Dev.
1. GetObjectHandles
2. List of available file handles
[1, 2, 3, 7, 28, …]
3. GetObjectInfo(7)
4. File Properties
{name = “img_123.jp”, size=276172, …}
5. GetObject(3)
6. File Contents
FFD8FFE2 02404943 435F5052 4F46494C …
#BHAS @BlackHatEvents

## Slide 16

# Android MTP Stack

- **USBManager starts MtpService** When connected to host

- **USBManager maintains enabled USB functions** mCurrentFunctions field

- • **USB prompts set current (= enabled) functions** Eg. By calling `usbMgr.setCurrentFunctions(FUNCTION_MTP)`

- **MtpDatabase is only populated if MTP enabled**

MtpService
MtpDatabase
MtpServer

Userspace
Kernel
FunctionFS

#BHAS @BlackHatEvents

## Slide 17

# Populating MtpDatabase

**MtpService** `if ((UsbManager.getCurrentFunctions() & UsbManager.FUNCTION_MTP) != 0) for (StorageVolume v : volumes.values()) database.addStorage(v);`

**MtpDatabase**

\```
MtpStorageManagermManager;
public void addStorage(StorageVolumestorage) {
MtpStoragemtpStorage= mManager.addMtpStorage(storage);
mServer.addStorage(mtpStorage);
…
\```

`MtpStorageManager` keeps track of file handles

#BHAS @BlackHatEvents

## Slide 18

MtpDatabase Vendor Customizations **MtpDatabase** (customized) `private int getObjectFilePath(int handle, char[] outFilePath, …) {` `if (handle <= 10000000) {`

\```
MtpStorageManager.MtpObjectobj= mManager.getObject(handle);
…  }
\```

\```
Uri objectsUri= MediaStore.Files.getContentUri("external_primary");
String[] arg= new String[]{Integer.toString(handle -10000000)};
Cursor c = resolver.query(objectsUri, PROJECTION, ID_WHERE, arg, …);
String path = c.getString(1);
path.getChars(0, path.length(), outFilePath, 0);
\```

#BHAS @BlackHatEvents

## Slide 19

MtpDatabase Vendor Customizations **MtpDatabase** (customized) `private int getObjectFilePath(int handle, char[] outFilePath, …) { if (handle <= 10000000) {`

\```
MtpStorageManager.MtpObjectobj= mManager.getObject(handle);
…  }
\```

\```
Uri objectsUri= MediaStore.Files.getContentUri("external_primary");
String[] arg= new String[]{Integer.toString(handle -10000000)};
Cursor c = resolver.query(objectsUri, PROJECTION, ID_WHERE, arg, …);
String path = c.getString(1);
path.getChars(0, path.length(), outFilePath, 0);
\```

#BHAS @BlackHatEvents

## Slide 20

MtpDatabase Vendor Customizations • **MtpServer includes sanity checks for most requests**

**MtpServer**

`MtpResponseCode MtpServer::doGetObject() { if (!hasStorage()) return MTP_RESPONSE_INVALID_OBJECT_HANDLE; ... hasStorage()` only returns true if database populated

• **However: No sanity checks in doTruncateObject!**

#BHAS @BlackHatEvents

## Slide 21

## Attack: Erase All Files From Huawei nova 12i

For all **_file handles f_** starting from `10000000:` **1. Start edit through MTP BeginEditObject(f)** Opens file descriptor for `MtpDatabase.getObjectFilePath(f)` **2. Invoke MTP TruncateObject(f, 0)** Calls `ftruncate(0)` on file descriptor

**3. Invoke MTP EndEditObject(f)**

**Result: Effectively erase all user files from device**

**CVE-2024-54096** , Patched

#BHAS @BlackHatEvents

## Slide 22

## Demo: Erase All Files From Huawei nova 12i

#BHAS @BlackHatEvents

## Slide 23

Android USB Stack **Can we enable MTP USB function through UsbManager State Machine?** `protected void setEnabledFunctions(long functions) { setUsbConfig(functions, functions == UsbManager.FUNCTION_NONE); }`

\```
private void setUsbConfig(long config, booleanchargeFuncs) {
mUsbGadgetHal.setCurrentUsbFunctions(config, chargeFuncs);
sendMessageDelayed({.what=MSG_TIMEOUT, .arg1=chargeFuncs}, 3000);
}
\```

\```
public void handleMessage(Message msg) {
if (msg.what== MSG_TIMEOUT && msg.arg1 != 1)
setEnabledFunctions(mScreenUnlockedFunctions);
}
\```

#BHAS @BlackHatEvents

## Slide 24

Android USB Stack **Can we enable MTP USB function through UsbManager State Machine?** `protected void setEnabledFunctions(long functions) { setUsbConfig(functions, functions == UsbManager.FUNCTION_NONE); }`

\```
private void setUsbConfig(long config, booleanchargeFuncs) {
mUsbGadgetHal.setCurrentUsbFunctions(config, chargeFuncs);
sendMessageDelayed({.what=MSG_TIMEOUT, .arg1=chargeFuncs}, 3000);
}
\```

\```
public void handleMessage(Message msg) {
if (msg.what== MSG_TIMEOUT && msg.arg1 != 1)
setEnabledFunctions(mScreenUnlockedFunctions);
}
\```

#BHAS @BlackHatEvents

## Slide 25

Android USB Stack **Can we enable MTP USB function through UsbManager State Machine?** `protected void setEnabledFunctions(long functions) { setUsbConfig(functions, functions == UsbManager.FUNCTION_NONE); }`

\```
private void setUsbConfig(long config, booleanchargeFuncs) {
mUsbGadgetHal.setCurrentUsbFunctions(config, chargeFuncs);
sendMessageDelayed({.what=MSG_TIMEOUT, .arg1=chargeFuncs}, 3000);
}
\```

\```
public void handleMessage(Message msg) {
if (msg.what== MSG_TIMEOUT && msg.arg1 != 1)
setEnabledFunctions(mScreenUnlockedFunctions);
}
\```

#BHAS @BlackHatEvents

## Slide 26

Android USB Stack **Can we enable MTP USB function through UsbManager State Machine?** `protected void setEnabledFunctions(long functions) { setUsbConfig(functions, functions == UsbManager.FUNCTION_NONE); }`

\```
private void setUsbConfig(long config, booleanchargeFuncs) {
mUsbGadgetHal.setCurrentUsbFunctions(config, chargeFuncs);
sendMessageDelayed({.what=MSG_TIMEOUT, .arg1=chargeFuncs}, 3000);
}
\```

\```
public void handleMessage(Message msg) {
if (msg.what== MSG_TIMEOUT && msg.arg1 != 1)
setEnabledFunctions(mScreenUnlockedFunctions);
}
\```

#BHAS @BlackHatEvents

## Slide 27

Invoking setEnabledFunctions via USB `setEnabledFunctions()` **needs calling with** `functions` **other than** `NONE protected void setEnabledFunctions(long functions) { setUsbConfig(functions, functions == UsbManager.FUNCTION_NONE); }`

`private void startAccessoryMode() { ... setEnabledFunctions(UsbManager.FUNCTION_ACCESSORY); mHandler.sendMessageDelayed(MSG_ACC_MODE_ENTER_TIMEOUT, 10000); }` **Idea:** Start accessory mode!

#BHAS @BlackHatEvents

## Slide 28

Android USB Stack **Can we enable MTP USB function through UsbManager State Machine?** `protected void setEnabledFunctions(long functions) { setUsbConfig(functions, functions == UsbManager.FUNCTION_NONE); }`

\```
private void setUsbConfig(long config, booleanchargeFuncs) {
mUsbGadgetHal.setCurrentUsbFunctions(config, chargeFuncs);
sendMessageDelayed({.what=MSG_TIMEOUT, .arg1=chargeFuncs}, 3000);
}
\```

\```
public void handleMessage(Message msg) {
if (msg.what== MSG_TIMEOUT && msg.arg1 != 1)
setEnabledFunctions(mScreenUnlockedFunctions);
}
\```

#BHAS @BlackHatEvents

## Slide 29

# mScreenUnlockedFunctions

- **Can it be set to MTP mode?** This would default to MTP upon timeout

- **Yes:** Developer settings `➔` Default USB config Requires developer settings to be unlocked first

- **Supposed to enable MTP while device unlocked**

#BHAS @BlackHatEvents

## Slide 30

Android USB Stack **Can we enable MTP USB function through UsbManager State Machine?** `protected void setEnabledFunctions(long functions) { setUsbConfig(functions, functions == UsbManager.FUNCTION_NONE); }`

\```
private void setUsbConfig(long config, booleanchargeFuncs) {
mUsbGadgetHal.setCurrentUsbFunctions(config, chargeFuncs);
sendMessageDelayed({.what=MSG_TIMEOUT, .arg1=chargeFuncs}, 3000);
}
\```

\```
public void handleMessage(Message msg) {
if (msg.what== MSG_TIMEOUT && msg.arg1 != 1)
setEnabledFunctions(mScreenUnlockedFunctions);
}
\```

#BHAS @BlackHatEvents

## Slide 31

Android USB Stack **Can we enable MTP USB function through UsbManager State Machine?** `protected void setEnabledFunctions(long functions) { setUsbConfig(functions, functions == UsbManager.FUNCTION_NONE); }`

\```
private void setUsbConfig(long config, booleanchargeFuncs) {
mUsbGadgetHal.setCurrentUsbFunctions(config, chargeFuncs);
sendMessageDelayed({.what=MSG_TIMEOUT, .arg1=chargeFuncs}, 3000);
}
\```

\```
public void handleMessage(Message msg) {
if (msg.what== MSG_TIMEOUT && msg.arg1 != 1)
setEnabledFunctions(mScreenUnlockedFunctions);
}
\```

#BHAS @BlackHatEvents

## Slide 32

# Attack: Retrieve Files from Locked Device **Assumption:** Default USB Configuration is set to MTP / File Transfer

### **1. Send USB control message to enable accessory mode** Switches USB descriptor & awaits re-enumeration

**2. Wait 3 seconds until** `MSG_TIMEOUT` Enables populated MTP interface

### **3. MTP access for 7 seconds until** `MSG_ACC_MODE_ENTER_TIMEOUT` **4. Repeat**

**CVE-2024-43085** , Patched in November 2024 ASB

#BHAS @BlackHatEvents

## Slide 33

# Demo: Read Files from Locked Pixel 8a

#BHAS @BlackHatEvents


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 94/100 on the text kept, 86/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Demo: Read Files from Locked Pixel 8a
[phone screen — Android settings]
6:46
Android version
Android version
15
Android security update
October 5, 2024
Google Play system update
July 1, 2024
Baseband version
g5300o-240704-240912-B-12358532,g5300o-240704-240912-B-12358532
Kernel version
5.15.148-android14-11-g3f4e1ccba8ea-ab12020698
#1 Wed Jun 26 21:05:55 UTC 2024
Build number
AP3A.241005.015
```

## Slide 34

# Mitigations

- **User authentication for USB file access prompts** Slow vendor adoption

- **Lockdown / Restricted Modes (improved lock screen)** Slow vendor adoption, flaws exist

**Recommendations** :

- Install updates!

- Bring your own power bank

- Otherwise: Shut down device while charging

Source: <u>quarkslab.com</u>

#BHAS @BlackHatEvents

## Slide 35

# BlackHat SoundBytes

- **ChoiceJacking: JuiceJacking-style attacks are still possible** Malicious chargers can bypass user prompts to extract files

- **File extraction still possible on locked devices** Flaws exist even in state-of-the-art devices

- **Watch your phone** Don’t hand it to strangers, only use trusted chargers

#BHAS @BlackHatEvents

## Slide 36

BlackHat SoundBytes • **ChoiceJacking: JuiceJacking-style attacks are still possible** Malicious chargers can bypass user prompts to extract files • **File extraction still possible on locked devices** Questions? Flaws exist even in state-of-the-art devices • **Watch your phone** Don’t hand it to strangers, only use trusted chargers

#BHAS @BlackHatEvents
