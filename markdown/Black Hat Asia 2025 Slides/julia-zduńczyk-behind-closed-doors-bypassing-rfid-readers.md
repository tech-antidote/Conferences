---
title: "Behind Closed Doors - Bypassing RFID Readers"
speakers: ["Julia Zduńczyk"]
conference: "Black Hat"
conference_full: "Black Hat ASIA 2025"
edition: "ASIA"
year: 2025
source_pdf: "Black Hat Asia 2025 Slides/Julia Zduńczyk_Behind Closed Doors - Bypassing RFID Readers.pdf"
pages: 41
sha256: "5377345fe563d89798130438b5c14857a26528cd9d66c026587f995e56417a5f"
text_chars: 9529
ocr_pages: 2
has_ocr: true
redacted_secrets: 0
ocr_confidence: 86.8
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T03:54:35Z"
---
# Behind Closed Doors - Bypassing RFID Readers

**Speakers:** Julia Zduńczyk  
**Conference:** Black Hat ASIA 2025  
**Source:** `Black Hat Asia 2025 Slides/Julia Zduńczyk_Behind Closed Doors - Bypassing RFID Readers.pdf` (41 pages)


## Slide 1

# **Behind Closed Doors Bypassing RFID Readers Julia Zduńczyk**

## Slide 2

###### **$ whoami**

###### **Julia Zduńczyk**

**IT Security Specialist at**

- **Penetration Tester**

- **Red Teamer**

- **Horse archer, diver, caver, rock climber, hiker, gymnast…**

- **tl;dr – I like adrenaline rush :P**

## Slide 3

###### **Disclaimer**

Even though this version of slides contains additional notes that summarize topics discussed during actual live briefing, the original presentation included multiple live demos covering more topics. I encourage you to watch the recording of the session :)

## Slide 4

###### **RFID**

###### **Radio Frequency Identification**

_Source: www.nfcwork.com_

Item tracking

_Source: https://wallester.com_

Contactless payments

_Source: https://dicsan.com_

Access Control

## Slide 5

###### **RFID**

###### **Other interesting use cases**

Coffee filters

Road signs tracking…?

## Slide 6

###### **Card cloning**

###### **Sometimes it works…**

In Red Teaming scenarios we must be quick and efficient. Access card cloning is easy when:

- the system in use is insecure

- employees don’t employ good card handling practices e.g. they leave their cards unattended in places accessible to unauthorized people

## Slide 7

###### **Card cloning**

###### **Sometimes it does not.**

When an access system used in the facility is secure, e.g. employs proper encryption, it is very hard or expensive to clone access cards. In this case it is often not worth it for the attacker to try card cloning and risk being caught in the process.

## Slide 8

###### **Card cloning**

###### **Sometimes it does not.**

And we will not always be so lucky to find cards permanently attached to readers as in this example ;)

## Slide 9

### **How can we bypass RFID access control systems without card cloning?**

## Slide 10

###### **Access control systems**

###### **Autonomous RFID locks**

**Tag UID (via RF)**

Reader is the decision-making unit, storing valid cards in its memory

**Open/Close command (via wires)**

## Slide 11

#### **How this works?**

**Based on the Sebury reader example: New cards can be added using:**

- **Manager Add and Delete cards**


> Recovered by OCR — confidence 95/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Method of Application
(To Add Card User)
How this works?
Read Manager Add Card
(The machine will give two beeps,
and LED turns in orange)
Based on the Sebury reader example:
Read User Card
(Cards can be added continuously)
New cards can be added using:
¢ Manager Add and Delete cards
Read Manager Add Card again
(The machine gives one beep,
and LED turns in white)
```

## Slide 12

##### **How this works?**

###### **New cards can be added using:**

- **Manager Add and Delete cards**

- **“administrator setting”**

\```
SEBURY USER MANUAL
\```

## Slide 13

###### **What can go wrong?**

- Leaving factory default PIN for admin settings

- Logic bypass of the lock operation – a card that would always open a lock (in this case card with UID ‘FFFFFFFF’ cannot be deleted from the system)

- Electromagnetic pulse generator? It can sometimes reset reader’s memory and open the lock (or it may fry the reader – don’t try it at home ;))

- Many other possible problems

## Slide 14

Card credential (via wires)
Controller
Open/Close
command

###### **Access control systems**

###### **Reader + Controller**

Card data
(via RF)

## Slide 15

###### **Communication protocol between the reader and the controller**

Wiegand
Controller


> Recovered by OCR — confidence 79/100 on the text kept, 59/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Communication protocol between
the reader and the controller
TAMPER AC BATT 12-24
rs FAIL FAIL VDC
INT
INS
+
4 @ ONLINE
@ comm
+ @ BATT FAIL
é @ TAMPER
@ins
NO |p
© 10 MODULE
Nc J= TERM IN OUT™ 12.54
. 5 S 9] voc _bIP SWITCH
Controller
Wiegand
HID
multiCLASS
```

## Slide 16

###### **Wiegand**

Wiegand uses two wires for
data transfer. The data is sent
in plaintext.
There is no encryption.
Data 1
Data 0

Controller

## Slide 17

###### **Red Team approach**

**`D e m o t i m e !`** How would we use that knowledge in a real physical Red Team assessment?

## Slide 18

###### **Red Team approach**

• Step 1: learn what type of access system we are working with

## Slide 19

###### **Card used in the example**

Seos Card

• Hard or expensive to clone • Real credential is encrypted inside the card

## Slide 20

###### **Red Team approach**

• Step 1: learn what technology we are working with

• Step 2: decide which attack has high chance of success but does not pose a high risk of detection Clone the cards? Attack Wiegand?

## Slide 21

###### **Wiegand Protocol Attack**

Let’s sniff the communication

**BLEkey ESPkey by Mark Baseggio and by Octosavvi Eric Evenchick**

The Tick
by Jakub Kramarz
(with my small contributions ;)

## Slide 22

Controller
We can install the Tick on the
Wiegand wires behind the reader
and intercept the communication.

###### **Access control systems**

###### **Reader + Controller**

We can install the Tick on the Wiegand wires behind the reader and intercept the communication.

## Slide 23

###### **Success**

After the Tick is implanted, we can connect to it via WiFi or Bluetooth and open the door remotely whenever we want – but we can only open the door where the Tick is installed. Now, we want to make a clone of the card to get access to other areas protected by readers. How?

## Slide 24

###### **SEOS cards**

Real credential that is sent later via Wiegand is encrypted inside the card. Even though we have the unencrypted value, to make an exact clone we would still need the key to write data to the forged card. We have to find another way to clone this card.

## Slide 25

###### **Watch carefully**

Let’s see once again which cards the reader supports. Maybe someone left some legacy settings turned on? We can check that by putting different types of cards close to the reader and observing it’s reaction.

## Slide 26

###### **Cards used in the example**

Seos Card

- More secure, way harder to clone

• Real auth data is
encrypted inside the
card

Prox Card

- Insecure

- Unencrypted data sent to the reader

- Easy to clone

## Slide 27

###### **Downgrade attack**

- Prerequisite:

   - ⚬ The system must have legacy credentials enabled (e.g. Prox cards)

- The idea:

   - ⚬ Obtain the decrypted data of the card that is not possible/easy to clone

   - ⚬ Write this data to an old-type, less secure card that will send it to the reader directly in plaintext

## Slide 28

###### **Downgrade attack**

After successful downgrade attack, we obtain a new physical card that can be used on other readers in the facility with legacy credentials enabled. From the perspective of the controller, it will recognize it as a known, valid card, because the data sent over Wiegand will be exactly the same – even though it is a different card type.

## Slide 29

###### **Anti-tamper mechanisms**

The alarm triggers when the reader is taken off the wall, but it must be configured correctly – connected to a system that alerts security guards immediately.

Tamper Sensor

Tamper detection wire label

## Slide 30

###### **Open Supervised Device Protocol**

- successor of Wiegand

- supports AES encryption

- bi-directional

- utilizes the RS485

## Slide 31

###### **Open Supervised Device Protocol**

• <u>supports</u> AES encryption: when secure mode of operation is used

Interesting DEFCON talk: “Badge of Shame” by Dan Petro &  David Vargas

See you in a year (maybe :P) with OSDP support

## Slide 32

### **Cool, but how could we get inside to install the device in a real-life scenario?**

## Slide 33

###### **Maybe try social engineering?**

## Slide 34

###### **Trust me bro I’m an engineer**

Sometimes we may be able to get inside and install the device without rising suspicion with use of some kind of disguise. However, in most cases all you really need is a lot of confidence – if you act as if you belong and know what you are doing, in many places you will be able to get away with a lot – e.g. opening server-room doors with metal hangers (true story ;))

## Slide 35

###### **Reader Denial of Service**

###### **And how to make it useful**

Let’s say we want to install some malicious devices inside the server-room, but we don’t want to get caught while doing it. We can run a DoS attack e.g. with the use of the Tick installed behind the reader to stop the reader from accepting cards thus denying access to the room.

DoS mode – flooding data lines with random bits

## Slide 36

###### **Reader DoS**

###### **And how to make it useful**

We can also use a vulnerability in some unpatched, Bluetooth-enabled HID Readers. With the use of the HID Reader Manager app, we can scan for nearby readers and then “Inspect” or “Locate” them. Using one of these options in a loop allows us to ‘block’ the reader. In case of “Inspect” mode, the reader’s LED will blink, and it won’t accept any cards…

## Slide 37

###### **Reader DoS**

###### **And how to make it useful**

…and in case of “Locate” mode the reader will blink and beep loudly – we could use it as a decoy, making a lot of noise and chaos in one part of the target building while we perform some tests/attacks in other part.

## Slide 38

###### **How to secure access control systems against these attacks?**

• Always place access controllers in secure areas • Use a more advanced solution – OSDP over Wiegand • Configure the protocol correctly (secure mode) • Use proper tamper detection, collect and monitor logs • Keep reader firmware up to date

• Disable legacy credentials

• ...

## Slide 39

**Black Hat Asia Sound Bytes – Key Takeaways** • Physical Access Control Systems are oftentimes insecure • Physical Red Teaming is a service deigned to check for these vulnerabilities that are otherwise often overlooked

• Raise awareness, educate, learn

## Slide 40

###### **Special thanks**

- Sławomir Jasek - https://smartlockpicking.com

- Jakub Kramarz - https://github.com/jkramarz/TheTick

- • Maciej Mionskowski

- My dad :)

- Everyone who puts their time and effort into PACS research

## Slide 41

## **Thank you**

**I AM Julia Zduńczyk**

**FIND ME ON LINKEDIN www.linkedin.com/in/jzdunczyk**

**WEBSITE www.securing.pl**
