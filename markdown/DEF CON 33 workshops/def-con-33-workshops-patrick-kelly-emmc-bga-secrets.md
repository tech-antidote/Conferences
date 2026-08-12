---
title: "EMMC BGA Secrets"
speakers: ["Patrick Kelly"]
conference: "DEF CON"
conference_full: "DEF CON 33"
edition: "33"
year: 2025
source_pdf: "DEF CON 33 workshops/DEF CON 33 - Workshops - Patrick Kelly - EMMC BGA Secrets.pdf"
pages: 44
sha256: "6eee98fd61113c9d668a5b4af768a3d1713573c236ca9cc87302b6bf103176f2"
text_chars: 11462
ocr_pages: 1
has_ocr: true
redacted_secrets: 0
ocr_confidence: 89.1
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T06:33:59Z"
---
# EMMC BGA Secrets

**Speakers:** Patrick Kelly  
**Conference:** DEF CON 33  
**Source:** `DEF CON 33 workshops/DEF CON 33 - Workshops - Patrick Kelly - EMMC BGA Secrets.pdf` (44 pages)


## Slide 1

**Google Cloud Security**

## **EMMC No Ball Reball Defcon 33 Workshop**

August 2025

## Slide 2

#### **Contents**

|**EMMC Fundies**|**06**|
|---|---|
|**BGA Removal**|**15**|
|**EMMC Imaging**|**24**|
|**Image Rooting**|**28**|
|**Reballing**|**34**|
|**The No Ball Reball**|**37**|
|**BGA Reattachment**|**39**|
|**Additional Resources**|**43**|

Proprietary & Conf i dential

Google Cloud Security 2

## Slide 3

#### **Presenter Introduction**

##### **Patrick Kiley**

Principal Red Team Consultant at Mandiant/Google, specializing in embedded systems testing. Patrick has over 20 years of information security experience working with both US Govt and private sector employers. Patrick has spoken at DEFCON, BlackHat, Bsides and RSA. Patrick can usually be found in the Car Hacking or Aerospace village where he volunteered for several years. His passion is hardware security and has released research in Avionics, IoT and even bricked his own Tesla while trying to make it faster.

Principal Red Team Consultant

Proprietary & Conf i dential

Google Cloud Security

3

## Slide 4

#### **Class Introduction**

##### **Patrick Kiley**

EMMC is a common flash memory format for more complex embedded devices and the Ball Grid Array (BGA) is a popular format for EMMC modules. BGA modules can be intimidating to hardware hackers since the pins are not exposed and are instead underneath the chip. This workshop will demonstrate and allow you to practice removing EMMC modules from an inexpensive circuit board using flux and a hot air station. The module will contain a Linux operating system and a Raspberry Pi. Workshop participants will learn how to image the removed EMMC. Mount and change the Linux filesystem in order to backdoor the image and gain access, and then learn how to copy the image to a new EMMC. Participants will then learn how to attach the module to a BGA carrier board with hot air.

###### Principal Red Team Consultant

Proprietary & Conf i dential

Google Cloud Security

4

## Slide 5

# **01 EMMC Fundies**

EMMC is a rather close relative of the SD card

Proprietary & Conf i dential

Google Cloud Security

5

## Slide 6

**Flash Types NAND - Higher density, cheaper, bad blocks**

**NOR - Fast read, slow write/erase, random access**

**EMMC - NAND++, managed NAND UFS - Newer mobile devices, faster**

Proprietary & Conf i dential

Google Cloud Security

6

## Slide 7

#### **SDMC and EMMC**

**Easy explanation, EMMC is an SD card with 8 data lines instead of 4 For our purposes, they are identical To communicate with EMMC, you only need 1 data line**

Proprietary & Conf i dential

Google Cloud Security

7

## Slide 8

**EMMC footprints BGA 221**

**BGA 153 (this is us)**

**BGA 254**

**BGA 169 (another common one)**

**Remember - top down, mirror if you are looking at it.**

Proprietary & Conf i dential

Google Cloud Security

8

## Slide 9

#### **SD and EMMC Pin Descriptions**

- **VCC 1.8v and 3.3v**

   - **1.8v controller**

   - **3.3 flash**

- **GND**

- **CMD (command)**

- **CLK (clock)**

- **Data 0-7**

   - **SD uses 0-3**

   - **EMMC doubles, 0-7**

   - **Just need 1 (0 if you think that way)**

Proprietary & Conf i dential

Google Cloud Security

9

## Slide 10

**Deadbugging Connect from removed BGA (or traces) to chip Did this once when I did not have an adapter (Not my image)**

Proprietary & Conf i dential

Google Cloud Security

10

## Slide 11

#### **Deadbugging**

Proprietary & Conf i dential

Google Cloud Security

11

## Slide 12

#### **Equipment**

- **Raspberry Pi**

   - **Pi 5 with SD card adapter**

- **SD to EMMC adapter (8GB)**

   - **Has SD card shaped PCB**

   - **Connects to EMMC**

   - **Caps are on power rails only**

- **Future versions**

   - **Combine boards**

   - **Use higher Tg**

   - **Move caps away from work area**

Proprietary & Conf i dential

Google Cloud Security

12

## Slide 13

#### **Lab 1**

- **Assemble EMMC adapter**

- **● Carefully plug in on underside**

- **● Power up**

- **Try to connect**

   - **Should be able to ping only**

Proprietary & Conf i dential

Google Cloud Security

13

## Slide 14

# **02 BGA Removal**

Flux is your friend here

Proprietary & Conf i dential

Google Cloud Security

14

## Slide 15

#### **Flux**

- **Flux is your friend**

   - **Eliminates oxidation**

   - **Promotes heat transfer**

   - **Smells like hacking!**

- **Use a high quality rework flux**

   - **Single 10cc tube lasts long time**

   - **Amtec is personal favorite**

   - **NC-559-V2 or VS-213A-TF**

   - **Be careful about counterfeits**

Proprietary & Conf i dential

Google Cloud Security

15

## Slide 16

#### **Rework Heater**

- **Helpful but not necessary**

   - **Prevents heat shock on dense boards**

Proprietary & Conf i dential

Google Cloud Security

16

## Slide 17

#### **Hot Air - Really HOT air**

- **Quick 861DW clone**

- **Be careful, it’s a soldering iron, but airborne**

- **Use setting 2, 375 temp and 40 airflow**

- **● Do not turn off when done, return to holster and air will go to max and will cool down elements.**

- **Do not point at table, yourself, anyone else or FFS nothing flammable**

Proprietary & Conf i dential

Google Cloud Security

17

## Slide 18

#### **Kapton Tape**

- **Not necessary here**

- **I have some if you want to try it**

Proprietary & Conf i dential

Google Cloud Security

18

## Slide 19

#### **Process**

- **Make a stack using scrap PCBs**

- **Put PCBS on silicon mat**

- **● Apply liberal bead of flux along edge**

- **Flux will wick underneath when heated**

- **● Heat chip with low airflow and 375-400 temp**

- **Do not force or pry**

- **Remove quickly from board and remove heat**

   - **Let hot air cooldown**

Proprietary & Conf i dential

Google Cloud Security

19

## Slide 20

#### **Cartridge based iron**

- **JBC clone FNIRSI and Sugon A9**

   - **Based on JBC CD-1SQF**

   - **C210 and C245 irons**

   - **C245 used in class**

   - **C210 smaller, used for rework**

- **Heater and thermocouple in cartridge**

   - **Adjusts power dynamically to maintain temperature**

   - **More heat transfer, more power**

Proprietary & Conf i dential

Google Cloud Security

20

## Slide 21

#### **Cleanup**

- **Remove excess solder**

   - **From board**

   - **From bga**

- **Use iron and solder braid**

- **Use more flux**

- **Re-alloy if necessary**

- **Goal is a flat set of pads with minimal solder**

Proprietary & Conf i dential

Google Cloud Security

21

## Slide 22

#### **Cleanup Results**

- **Remove excess flux**

- **Use flux remover and swab**

- **● Should have flat pads with minimal solder**

- **Remaining solder can prevent connection and imaging**

- **● If you removed a cap, you can reattach if you want, not mandatory**

Proprietary & Conf i dential

Google Cloud Security

22

## Slide 23

# **03 EMMC Imaging**

Odin of Flash - The AllSocket

Proprietary & Conf i dential

Google Cloud Security 23

## Slide 24

#### **EMMC Imaging**

- **Devices**

   - **Flash reader**

      - **Read only**

   - **Allsocket**

      - **Can mount, make changes**

- **Just a SD to EMMC clamshell**

- **Few passives to stabilize**

   - **connection**

- **Can use to deadbug**

Proprietary & Conf i dential

Google Cloud Security

24

## Slide 25

#### **EMMC Imaging**

- **Ensure EMMC is clean**

- **No raised solder pads**

- **Ensure pin 1 is lined up with arrow**

- **Try 1.8v first, 3.3 next**

- **Connect to VM, see if /dev/sd$ is recognized**

- **Should have 2 partitions look at messages**

   - **Sd? Attached SCSI removable disk**

   - **sd?: sd?1 sd?2**

Proprietary & Conf i dential

Google Cloud Security

25

## Slide 26

#### **EMMC Imaging Lab**

- **Try it yourself**

- **If you cannot get a connection, ask for help**

- **● Could have bad connection, try re-alloying, removing solder again**

- **2 options to copy**

- **dd if=/dev/sd(b,c…) of=$filename.img bs=1M**

- **● Or dd if=/dev/sda1 and /dev/sda2 then manually partition target**

Proprietary & Conf i dential

Google Cloud Security

26

## Slide 27

# **04 Image Rooting**

Choose your own backdoor

Proprietary & Conf i dential

Google Cloud Security

27

## Slide 28

#### **Image rooting**

**● If everything fails and you are unable to image**

- **I have a copy of the image on USB**

Proprietary & Conf i dential

Google Cloud Security

28

## Slide 29

#### **Rooting is choose your own method**

- **Simple to elaborate**

   - **Change firewall,**

   - **Add user/ssh key**

   - **Change user password**

   - **Add Cron for reverse connection**

   - **Modify startup script**

Proprietary & Conf i dential

Google Cloud Security

29

## Slide 30

#### **Rooting Lab 1**

- **Again, we are here to help**

- **● Mounting hint**

   - **losetup -P -f**

- **Then may or may not have to manually mount partitions**

Proprietary & Conf i dential

Google Cloud Security

30

## Slide 31

#### **Rooting Lab 2**

- **Again, we are here to help**

- **Mounting hint**

   - **losetup**

Proprietary & Conf i dential

Google Cloud Security

31

## Slide 32

#### **Rooting Lab 3**

- **Modifying hint**

- **chroot makes it much easier**

   - **<u>bit.ly/41aerH9</u>**

- **If you are completely stuck, I have a pre-rooted image you can use to copy over to new emmc**

Proprietary & Conf i dential

Google Cloud Security

32

## Slide 33

# **05 Reballing**

And why it is a waste of time, most of the time

Proprietary & Conf i dential

Google Cloud Security

33

## Slide 34

#### **Reballing process**

- **Purchase appropriate size solder balls**

   - **Sub mm size .25mm for example**

- **Purchase appropriate size stencil**

   - **freeball it if you really want a challenge**

- **Apply thin layer of tacky flux**

- **● Carefully put stencil in position**

- **● Put a ball over each pad**

- **● Remove stencil and reflow (don't use air)**

Proprietary & Conf i dential

Google Cloud Security

34

## Slide 35

### **OR**

Proprietary & Conf i dential

Google Cloud Security

35

## Slide 36

# **06 The no ball reball**

Just replace the EMMC, most of the time its dirt cheap.

Proprietary & Conf i dential

Google Cloud Security

36

## Slide 37

**EMMC replacement cost vs your time Reballing is fine if**

- **The chip is difficult to replace**

- **Your time is not valuable**

- **You are a masochist**

**The cost of the materials, time and effort is usually not worth the cost of buying a new EMMC**

**EMMC have a finite number of read/write cycles**

**Plus if you are resurrecting old hardware, you can replace with a more robust one**

Proprietary & Conf i dential

Google Cloud Security

37

## Slide 38

**07 BGA Reattachment**

The hardest part of the process

Proprietary & Conf i dential

Google Cloud Security

38

## Slide 39

**BGA Reattachment Apply flux to EMMC or board**

**Align pin 1 with markings Can use kapton with loop to make alignment easier**

**Place board on scrap pcb rack and mat Double, triple check before applying heat**

Proprietary & Conf i dential

Google Cloud Security

39

## Slide 40

#### **BGA Reattachment**

**Turn on hot air, setting 2**

**Move air in slow even movement, do not keep in same position Watch carefully, wait for solder to melt and you should see the smallest movement as the chip aligns with pads. Remove heat and do not touch until cool**

Proprietary & Conf i dential

Google Cloud Security

40

## Slide 41

**BGA Reattachment After board has cooled, plug in and see if pi boots Check for connectivity**

**Congratulations!**

Proprietary & Conf i dential

Google Cloud Security

41

## Slide 42

# **08 Additional Resources**

Proprietary & Conf i dential

Google Cloud Security

42

## Slide 43

#### **Resources**

###### **Equipment**

- **JBC - https://www.jbctools.com/**

- **● Flux - https://www.inventecusa.com/**

**Techniques**

- **https://www.youtube.com/@rossmanngroup**

- **● https://www.ipadrehab.com/**

Proprietary & Conf i dential

Google Cloud Security

43

## Slide 44

**Thank you Safe Travels home**


> Recovered by OCR — confidence 89/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Thank you
Safe Travels home 7
Google Cloud
```
