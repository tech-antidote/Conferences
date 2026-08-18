---
title: "Invisible Threads Remote Building Surveillance Through Encrypted Thread Traffic Analysis"
speakers: ["Bela Genge", "Anca Delia Burduv", "Ioan Padurean"]
conference: "Black Hat"
conference_full: "Black Hat USA 2026"
edition: "USA"
year: 2026
source_pdf: "BlackHat_USA_2026_Slides/Bela Genge&Anca Delia Burduv&Ioan Padurean_Invisible Threads Remote Building Surveillance Through Encrypted Thread Traffic Analysis.pdf"
pages: 81
sha256: "97de04b7e66a82e9da13f04a724e4222bb8f920fcd9af24c3a65e653906b78f9"
text_chars: 24523
ocr_pages: 26
has_ocr: true
redacted_secrets: 0
ocr_confidence: 90.9
ocr_unreliable_blocks: 0
vision_verified_pages_changed: 71
vision_verified_pages: 81
vision_verified_blocks: 1
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T05:29:51Z"
---
# Invisible Threads Remote Building Surveillance Through Encrypted Thread Traffic Analysis

**Speakers:** Bela Genge, Anca Delia Burduv, Ioan Padurean  
**Conference:** Black Hat USA 2026  
**Source:** `BlackHat_USA_2026_Slides/Bela Genge&Anca Delia Burduv&Ioan Padurean_Invisible Threads Remote Building Surveillance Through Encrypted Thread Traffic Analysis.pdf` (81 pages)


## Slide 1

## Invisible Threads: Remote building surveillance through encrypted Thread traffic analysis

Speakers: Béla Genge, Anca Delia Burduv

Contributor: Ioan Pădurean

## Slide 2

##### OUR PREVIOUS RESEARCH ON MATTER IOT

- Brand new standard, adopted by **600+ major industry players** (Google, Apple, Samsung, Amazon, etc.)

- We found several design flaws and vulnerabilities in the Matter IoT standard

- Enabled effective DoS, device identification

- Exploit **required Wi-Fi access**

Title slide of the earlier talk, reproduced at left: black hat EUROPE 2024, DECEMBER 11-12, 2024, BRIEFINGS — "Breaking Matter: Vulnerabilities in the Matter Protocol", Speaker: Béla Genge, Contributor: Ioan Pădurean.

Message-sequence diagram along the bottom: an **Initiator** lifeline on the left, a **Responder** lifeline on the right. One message, labelled **Sigma1** where it arrives at the Responder, is drawn three times as three stacked left-to-right arrows:

Random_I, SessionId_I, destId, EphPubKey_I [, …]

Caption under the arrows: No replay protection. A "GREAT SUCCESS!" meme sits alongside.

2

## Slide 3

##### OUR LATEST BLACK HAT TALK: INFO LEAKS

- We accidentally found that Matter's encrypted traffic **leaks information** about devices

- Attackers can **accurately profile devices** on the network, conduct spying and profiling activities, **user behavior identification**, which can lead to other malicious activities

- Exploit **required Wi-Fi access**

Title slide of the previous talk, reproduced at left: black hat BRIEFINGS, DECEMBER 10-11, 2025, EXCEL LONDON / UNITED KINGDOM — "Ghosts in the Stream: Exposing Lives and Devices Behind Encrypted Doors", Speakers: Kristopher Schlett, Béla Genge, Contributors: Ioan Pădurean, Savio Sciancalepore.

Diagram below. From the label **Encrypted packets** on the left, two arrows fan out to three capture panes, each paired with a photograph of a different lamp. All three panes show the same three rows, with the `Len=` column ringed in pink:

```text
Matter          137 35879 → 5540   Len=75
Matter          130 5540 → 35879   Len=68
Matter           96 35879 → 5540   Len=34
```

Two further arrows leave the panes to the right and converge between the labels **Communication patterns** and **Device + user behavior identification**.

3

## Slide 4

##### NATURAL CURIOSITY: THIS RESEARCH

Protocol-stack diagram at the top, two rows deep, with **Application** layer labelled at the left and Communication / **transport** layer labelled at the right.

- Upper row, left to right: Cluster Library | Bridge | the **matter** logo spanning the middle | Provisioning | Profiles | Mesh
- Lower row, left to right: zigbee | THREAD | Wi-Fi | Bluetooth

Below it, the same packet-size sequence is shown twice. The upper copy sits above a solid white bar:

34, 73, 42, 34, 59, 67, 34, 73, 42, 34, 59, 67

An arrow from the right labels it **Application** layer patterns.

The lower copy is enclosed in a hand-drawn pink box with a key at its right-hand end:

34, 73, 42, 34, 59, 67, 34, 73, 42, 34, 59, 67

An arrow from the right labels it **Transport** layer cryptographic protection.

Two arrows lead down from the boxed sequence into a hooded-attacker icon, beside the question:

Is there protection to **prevent** further **information leakage and exploitation**?

4

## Slide 5

##### INNOCENT BYSTANDERS

Three photographs and no body text: the two speakers standing outdoors, the Bitdefender office tower, and a courtroom still captioned "BYSTANDERS ARE, BY DEFINITION, INNOCENT.".

## Slide 6

##### POSSIBLE EXPLOITATION

The same courtroom still, "BYSTANDERS ARE, BY DEFINITION, INNOCENT.", now overstamped with a red **NOT**.

In the middle, three stacked development boards; a pink arrow runs from the boards down to the photograph of the two speakers, marking the board carried in the backpack. To the right of the boards a hydrant icon sprays towards the Bitdefender tower, under the caption:

Information leakage?

## Slide 7

Three speaker cards, left to right, each with a portrait above the text.

**Béla GENGE** — Senior Security Researcher, Bitdefender

Leading research on Matter IoT security since 2023. He combines industrial innovation with academic exploration, diving deep into reverse-engineering proprietary protocols and making sense of the chaos in computer and IoT network traffic.

**Anca Delia BURDUV** — Junior Security Researcher, Bitdefender

She has a Bachelor's degree in Computer Science. Before joining Bitdefender, she interned on Arm's GNU Compiler Collection team, where she worked on Arm intrinsics.

**Ioan PĂDUREAN** — Security Researcher, Bitdefender

Research on Matter IoT since early 2024. He has a master's degree in Artificial Intelligence and is currently pursuing a PhD in IoT security.

7

## Slide 8

##### OUTLINE

A spider's web with four numbered items placed around it:

1. Buildings, motivation — top
2. Threads, information leaks — right
3. Infrastructure discovery — bottom
4. Exploitability — left

Three **Demo** labels stand in a column between item 4 and the web, gathered by a pink curly brace whose tip points left at **Exploitability**.

Beneath item 4, an illustration of a boy with a laptop cabled to an antenna board, beaming wireless signals and envelope icons at a photograph of an office building.

8

## Slide 9

##### BUILDINGS

> Buildings serve several societal needs – occupancy, primarily as shelter from weather, **security**, living space, **privacy**, to store belongings, and to comfortably live and work.

A Wikipedia globe sits beside the quote. Below it, a sign reading "SAFETY FIRST — Keep Door Closed at All Times."

9

## Slide 10

##### BUILDINGS – THE PROBLEM

10

## Slide 11

### The walls haven't changed. The threats have.

11

## Slide 12

##### WHAT MOTIVATED THIS RESEARCH?

Notice anything interesting?

A photograph of a building entrance: a glass door, a white round sensor on the wall above, and a plaque of opening hours reading

```text
Orar
Luni - Joi    8⁰⁰ - 15⁰⁰
Vineri        8⁰⁰ - 14⁰⁰
    S - D  ÎNCHIS
```

12

## Slide 13

##### WHAT TRIGGERED THE RESEARCH

If we take a closer look

An arrow runs from a product render of a smart lock body and its separate numeric keypad to a photograph of the same keypad mounted beside the glass entrance door.

It just happens we had prior experience with such devices

A second arrow runs from that caption to a photograph of the lock cylinder fitted to a metal door, carrying a red **B** badge and a **matter** logo.

13

## Slide 14

##### WHAT IS THE TECHNOLOGY BEHIND IT?

A screenshot of the product page, with the **THREAD** and **matter** logos overlaid on it. An arrow runs from the THREAD logo down to the "Native Support for Matter over Thread" bullet; another runs from the matter logo down to the word "Matter" in the opening paragraph.

Aqara

**Aqara U200 smart lock EU black with keypad**

Easy installation over existing lock without drilling or modification and wide compatibility
Silent unlock mode, automatic alerts, automatic locking, temporary passwords and hands-free unlocking
Seamless integration with major smart home systems, such as Apple Home and Google Home

Tabs: **Description** | Features | Videos (1)

Upgrade your home to a keyless lifestyle with **the Aqara Smart Lock U200 Kit** , which easily installs over your existing EURO cylinder lock, without the need for drilling. This smart lock supports various access methods such as fingerprint, **NFC** , passcode and more, and integrates with **Apple Home** keys . Compatible with **Matter** , it is managed through the Aqara Home app and is built to last, with a six-month battery life and an IPX5 water resistance rating, making it ideal for both indoor and outdoor use.

- **Apple Home Keys and Multiple Unlock Methods :** The U200 offers a variety of convenient unlock methods, including Apple Home Keys (requires Apple 2-in-1 Matter controller and Border Router), fingerprint, passcode, NFC, and more. You can control the lock using the app via either built-in Bluetooth or Thread for remote access. Additionally, it supports temporary passwords, such as one-time and recurring passwords, for easy sharing with others. The device also allows the use of mechanical keys for emergencies.

- **Advanced Software Control :** U200 enhances home access with Silent Unlock Mode, automatic alerts and hands-free unlocking, ensuring security and peace of mind with features such as Activity Log, auto-lock and PIN Code Anti-spy Protection. It offers flexibility with Passage Mode, temporary passwords including offline passwords (One-Time Passwords) and periodic passwords available in the Aqara Home app, along with Do Not Disturb Mode.

- **Native Support for Matter over Thread :** The U200's Matter over Thread support ensures seamless integration with leading smart home systems, such as Apple Home and Google Home, improving user convenience by extending battery life and efficient remote management.

- **Rechargeable Battery and Multiple Power Options :** The U200's advanced engineering includes IPX5 waterproofing, an operating range of -15ºC to 66ºC, and multiple power sources: rechargeable Li-Ion for the lock (up to 6 months), AAA batteries for the keypad, and wired power capability. This ensures durable and reliable performance

(The last line runs off the bottom edge of the screenshot on the slide.)

14

## Slide 15

##### QUESTIONS OF INTEREST

If devices such as the smart door lock are not located on the street, is traffic still accessible from the street?

If so, what can "the (innocent) bystander" infer when analyzing such data leaks?

15

## Slide 16

# THREAD(S)

16

## Slide 17

##### THREAD, THREAD & MATTER

- Thread:

   - Energy-efficient communication-layer for low-power devices

   - Self-healing mesh network

   - IPv6-based protocol for low-power, mesh networks

- Matter: the application-layer protocol

Top right, the same protocol-stack graphic as slide 4 — upper row Cluster Library | Bridge | **matter** | Provisioning | Profiles | Mesh, lower row zigbee | THREAD | Wi-Fi | Bluetooth.

Bottom left, a mesh topology drawn with dotted links. A **Thread Border Router**, drawn as a sphere, sits at the centre. Links: two devices at the far left each connect to a wall-socket icon; the socket connects to the Border Router; a Thread-badged light bulb connects down to the Border Router; the Border Router connects up-right to a blue Wi-Fi router; the Wi-Fi router connects down to a tablet.

Bottom right, the Thread layer stack, top to bottom, with the middle four boxes outlined in pink and the top and bottom boxes in white:

- HTTP, CoAP, MQTT, ...
- DTLS
- UDP
- Distance Vector Routing
- 6LowPAN (IPv6)
- IEEE 802.15.4

17

## Slide 18

##### EXAMPLE THREAD DEVICES

Three columns, each headed by photographs of the device class.

**Border Routers**: Connect a Thread mesh network to external IP networks enabling communication between Thread devices and the outside world.

**Router Eligible End Devices** (REEDs): Can be promoted to routers if the network needs more routing capacity. (usually mains-powered)

**Minimal End Devices** (MEDs):

- Connect to a parent router but do not maintain full routing information, cannot become routers.

**Sleepy End Devices** (SEDs):

- Battery-powered devices that spend most of their time asleep to conserve energy.

- Rely on a parent router for message buffering cannot become routers.

18

## Slide 19

###### WHAT IS THE BIG DEAL ABOUT THREAD?

Thread **progressed a lot** from its first release, it is not only viewed as a standard for smart homes

It is moving towards **commercial smart buildings**

**Energy and industrial applications** are on the horizon

Two press clippings fill the right half of the slide. The first, under the KNX logo:

16. Sep 2024

Thread Becomes Partner of the KNX-IoT Startup Incubator Program

Source: <u>https://www.knx.org/knx-en/newsroom/news/press/20240916-thread-becomes-partner-of-the-knx-iot-startup-incubator-program/</u>

The second, tagged PRESS RELEASES:

Thread Group Certifies IoT Hub for Smart Commercial Buildings and New Components

The WideSky Hub is the first certified and widely available Built on Thread product for commercial buildings, energy and industry applications. WideSky's wireless hub uses Thread to cost-effectively and reliably access valuable data across subsystems, devices and sensors without cables. Thread also ensures scalability and compatibility for the data infrastructure monitoring and controlling solutions of the future.

19

## Slide 20

##### SELF-HEALING ARCHITECTURE

- Scalability of up to 10K Thread devices

- Self-healing automates reconfiguration

Legend, each entry a coloured square:

- Non-Router End device — red outline
- Router eligible node — magenta outline
- Router node — solid magenta
- Border router — solid grey

The graph to the right shows five solid-magenta router nodes joined to each other by cyan links, with red-outline and magenta-outline squares hanging off them. Two grey border-router squares connect on the right, and each links by a dotted line to a pink Wi-Fi router icon, which in turn links by a dotted line down to a phone.

20

## Slide 21

##### CHANNELS AND SIGNAL RANGE

- Thread uses the IEEE 802.15.4 2.4 GHz band from approximately 2405 MHz to 2480 MHz

- Possible channels:

   - 11: 2405 MHz

   - …

   - 25: 2475 MHz

- Signal can range from 15m indoor to **30-50m+ outdoor**

Below, a spectrum graphic: overlapping coloured channel lobes over a double-headed axis. The axis is annotated `2.400 GHz` at the left end and `2483 GHz` at the right end, with the tick labels 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 between them. Caption underneath: Channels 11 to 25.

21

## Slide 22

##### THREAD SECURITY

**One network-wide** symmetric **key**:

- Media Access Layer (MAC) authentication and encryption

- Different levels of security as defined in IEEE 802.15.4

- **Does not change** very often 👎

| LEVEL | SECURITY LEVEL | DESCRIPTION | MIC* SIZE |
|---|---|---|---|
| 0x00 | None | No security (unencrypted) | - |
| 0x01 | MIC-32 | Data authenticity only | 32 bits |
| 0x02 | MIC-64 | Data authenticity only | 64 bits |
| 0x03 | MIC-128 | Data authenticity only | 128 bits |
| 0x04 | ENC | Confidentiality only | - |
| 0x05 | ENC-MIC-32 | Confidentiality + Authenticity | 32 bits |
| 0x06 | ENC-MIC-64 | Confidentiality + Authenticity | 64 bits |
| 0x07 | ENC-MIC-128 | Confidentiality + Authenticity | 128 bits |

_*MIC: Message Integrity Code_

On the right, three thumbs-up icons over the caption **Application security**; below a blue rule, **Thread security** over a large pink question mark.

22

## Slide 23

##### THREAD FRAME ENCRYPTION

- Uses the **AES-CCM** scheme to encrypt frames at the IEEE 802.15.4 (MAC/network) layer

- AES-CCM scheme (more specifically AES-CCM*), as defined by NIST 800-38C

The lower half of the slide is an AES-CCM block diagram on a white ground.

Three inputs sit along the top: **Nonce**, **Additional data** (dash-dot line) and **Payload** (dashed line). Their lines run down into the block sequence below; the Payload also runs right and down the far edge of the figure to the final XOR.

Left half — authentication chain: blocks B₀, B₁, … , B_r. B₀ feeds an AES128 block keyed by K, whose output Y₀ is XORed with B₁ before the next AES128, giving Y₁, and so on to Y_r. Every AES128 box is fed `K →`.

Right half — counter chain: Ctr₀, Ctr₁, … , Ctr_m, each into its own AES128 keyed by K, producing S₀, S₁, … , S_m; the output of one stage is XORed into the next counter, as on the left.

Bottom — three cell-strip bars. Under Y_r, a bar whose leading blue cells are braced *Tlen* and labelled **T**. Under S₀, a bar whose leading blue cells are braced *Tlen*. Under S₁ … S_m, a bar whose leading blue cells are braced *Plen*, the whole bar labelled **S**.

T and the S₀ prefix meet at a XOR that feeds the **MAC** box. The *Plen* prefix and the line returning from Payload meet at a second XOR that feeds the adjacent **ENCP** box.

23

## Slide 24

##### ESSENTIALLY

The same action (e.g., command) will generate the **same request ... response** packet sizes

Two encryption diagrams on the right, one per cartoon user at a light switch.

Top — inputs Key `a327981b3a52...`, Nonce `5c920519f4b2...` and Command *Turn ON* all arrow down into an **AES-CCM** box holding **CTR** and **CBC-MAC**; three arrows leave it into a bar split as **Encrypted payload** | **MAC**.

Bottom — the same bar, **Encrypted payload** | **MAC**, sits above its **AES-CCM** box (again **CTR** and **CBC-MAC**), which is fed from below by Key `b5247c8918aa...`, Nonce `43678cc23b45a8...` and Command *Turn ON*.

24

## Slide 25

###### WHAT ABOUT THE APPLICATION-LAYER?

Five icon-and-label rows down the left, then three thumbs-up icons:

- Mandatory security
- Symmetric session keys
- Fabric-specific certificates
- Key exchange algorithms
- Ephemeral asymmetric keys

The right half carries the **matter** logo above a four-row stack diagram, its rows labelled down the left edge:

- **Ecosystems and Cloud** — a dotted-outline band holding HomeKit, hue PERSONAL WIRELESS LIGHTING, amazon alexa, SmartThings and Google Home
- **Application Layer** — Cluster Library | Bridge | **matter** | Provisioning | Profiles | Mesh
- **Network/Transport Layer** — zigbee | THREAD | Wi-Fi | Bluetooth
- **Radio: Physical/Link Layer (MAC/PHY)** — one grey box reading IEEE 802.15.4 spanning the zigbee and THREAD columns, a second reading IEEE 802.11 under Wi-Fi, a third reading Bluetooth under Bluetooth

Source: <u>https://www.qorvo.com/design-hub/blog/matter-gets-everybody-talking</u>

Two brick-wall icons close the slide, captioned **Interoperability** and **Mandatory security**.

25

## Slide 26

##### MATTER PACKET ENCRYPTION

- Matter uses the **AES-CCM** scheme to encrypt packets at the IEEE 802.15.4 (MAC/network) layer

- AES-CCM scheme, as defined by NIST 800-38C

The same AES-CCM block diagram as slide 23 fills the lower half: **Nonce**, **Additional data** and **Payload** feeding the block sequence B₀, B₁, … , B_r through AES128 stages keyed by K to Y₀, Y₁, … , Y_r; the counter chain Ctr₀, Ctr₁, … , Ctr_m through AES128 to S₀, S₁, … , S_m; and the three cell-strip bars braced *Tlen*, *Tlen* and *Plen*, whose XORs feed the **MAC** and **ENCP** boxes.

26

## Slide 27

A kitten meme, captioned "I don't believe my eyes", is the only content on the slide.

27

## Slide 28

##### WHAT DOES THIS MEAN?

A two-panel meme, each panel a photograph of the same cardboard box:

STEP 1: PACK THE PACKAGE

STEP 2: PUT IT IN AN IDENTICAL PACKAGE

28

## Slide 29

### SO EVERYTHING IS (DOUBLE) ENCRYPTED?

Below it, a Wonka meme captioned "FINALLY, WE CAN REST ASSURED".

29

## Slide 30

# INFRASTRUCTURE DISCOVERY

30

## Slide 31

##### SNIFFING THREAD TRAFFIC

1. Get a Nordic nRF52840 DK development board

2. Download and install Nordic SDK

3. Compile & flash: **Thread sniffer**

4. Add Wireshark plug-in

An nRF5 SDK badge sits under the list. To the right, a photograph of a laptop running Wireshark with two development boards on the desk; the upper board is ringed in pink and labelled **Thread sniffer** by an arrow.

31

## Slide 32

##### WHERE WE STARTED

32

## Slide 33

##### WORK OBJECT: THE FRAME

A layer diagram on the left. A white badge carrying the vertical word **THREAD** sits at the far left; a line from it branches to three of the stacked boxes:

- Applications (pink outline)
- UDP (blue outline)
- IP Routing (blue outline)
- 6LoWPAN (blue outline)

A tall blue-outlined box reading **Security / Commissioning** stands alongside that group, joined by short links to UDP, IP Routing and 6LoWPAN. Two wider pink-outlined boxes sit beneath the group:

- IEEE 802.15.4 MAC
- IEEE 802.15.4 PHY

On the right:

Frames are the individual messages devices exchange over the network

Each frame is made up of protocol headers plus a payload

Below that, a Wireshark packet-detail pane:

```text
> Frame 445: Packet, 87 bytes on wire (696 bits), 87 bytes captured (696 bits) on interface /dev/ttyACM1, id 0
> IEEE 802.15.4 Data, Src: 0x6c00, Dst: 0xac00
> 6LoWPAN, Src: ::79d2:6940:cb50:459d, Dest: fda0:13ed:8be5::be9
> Internet Protocol Version 6, Src: ::79d2:6940:cb50:459d, Dst: fda0:13ed:8be5::be9
> User Datagram Protocol, Src Port: 5540, Dst Port: 60375
> Matter
```

33

## Slide 34

##### (NON-ENCRYPTED) FIELDS OF INTEREST

A Wireshark packet-detail screenshot fills the left half. Pink highlighter rings four regions; the ink covers parts of the lines it crosses, and the pane is clipped at its right edge so several lines run off.

```text
v Frame 97: Packet, 103 bytes on wire (824 bits), 103 bytes captured (824 bits) …
    Section number: 1
  > Interface id: 0 (/dev/ttyACM1)
    Encapsulation type: IEEE 802.15.4 Wireless PAN with FCS not present (127)
    Arrival Time: Jan 15, 2026 14:23:12.734628000 EET
    UTC Arrival Time: Jan 15, 2026 12:23:12.734628000 UTC
    Epoch Arrival Time: 1768479792.734628000
    [Time shift for this packet: 0.000000000 seconds]
    [Time delta from previous captured frame: 28.505000 milliseconds]
    [Time delta from previous displayed frame: 28.505000 milliseconds]
    [Time since reference or first frame: 10.323112000 seconds]
    Frame Number: 97
    Frame Length: 103 bytes (824 bits)
    Capture Length: 103 bytes (824 bits)
    [Frame is marked: False]
    [Frame is ignored: False]
    [Protocols in frame: wpan:data]
    Character encoding: ASCII (0)
v IEEE 802.15.4 Data, Src: 0xac00, Dst: 0x6c00
  > Frame Control Field: 0x9869, Frame Type: Data, Security Enabled, Acknowledge…
    Sequence Number: 96
    Destination PAN: 0x90d5
    Destination: 0x6c00
    Source: 0xac00
  > Auxiliary Security Header
    MIC: 578450da
  > [Expert Info (Warning/Undecoded): No encryption key set - can't decrypt]
v Data (84 bytes)
    Data: 06b1a5434d1ae869a8469ed792039f6dc19b3585192a9b8ebb51517613f0e3467e7e9…
    [Length: 84]
```

The `IEEE 802.15.4 Data, Src: 0xac00, Dst: 0x6c00` row is highlighted yellow. The lines `UTC Arrival Time`, `[Time shift for this packet…]`, `Frame Number: 97` and `Source: 0xac00` are partly obscured by the pink ink; they are recovered above from the magnified callouts and from the surrounding context.

Five magnified callouts stack down the right half, each a crop of one ringed line:

```text
Epoch Arrival Time: 1768479792.734628000

Frame Length: 103 bytes (824 bits)

d: 0x9869, Frame Type: Data, Security Enab

Sequence Number: 96

Destination: 0x6c00
Source: 0xac00
```

Below them, a meme captioned "IS IT GOLD IN HERE?" / "OR IS IT JUST ME?".

34

## Slide 35

##### REMEMBER OUR PRIOR RESEARCH

Top left, the title slide of the earlier talk: black hat BRIEFINGS, DECEMBER 10-11, 2025, EXCEL LONDON / UNITED KINGDOM — "Ghosts in the Stream: Exposing Lives and Devices Behind Encrypted Doors", Speakers: Kristopher Schlett, Béla Genge; Contributors: Ioan Pădurean, Savio Sciancalepore; footer #BHEU @BlackHatEvents.

In our initial attempt we simply used our approaches developed in the previous research

Three capture panes stack across the lower half, each paired with a photograph of a different lamp — a red disc lamp, a red bulb on a stand and a purple caged bulb — and all three carrying identical rows:

```text
Matter          137 35879 →  5540 Len=75
Matter          130  5540 → 35879 Len=68
Matter           96 35879 →  5540 Len=34
```

```text
Matter          137 35879 →  5540 Len=75
Matter          130  5540 → 35879 Len=68
Matter           96 35879 →  5540 Len=34
```

```text
Matter          137 35879 →  5540 Len=75
Matter          130  5540 → 35879 Len=68
Matter           96 35879 →  5540 Len=34
```

35

## Slide 36

##### WE CAN JUST USE OUR PREVIOUS RESEARCH

Two capture panes side by side, joined by a pink arrow pointing left to right and labelled **One – to – one mapping**.

Left pane — Matter view:

```text
Matter           96  5540 → 59065 Len=34
Matter          135  5540 → 59065 Len=73
Matter          104 59065 →  5540 Len=42
Matter           96  5540 → 59065 Len=34
Matter          121 59065 →  5540 Len=59
Matter          129  5540 → 59065 Len=67
Matter           96 59065 →  5540 Len=34
Matter          135  5540 → 59065 Len=73
Matter          104 59065 →  5540 Len=42
Matter           96  5540 → 59065 Len=34
Matter          121 59065 →  5540 Len=59
Matter          129  5540 → 59065 Len=67
Matter           96 59065 →  5540 Len=34
Matter          291  5540 → 59065 Len=229
Matter          104 59065 →  5540 Len=42
Matter           96  5540 → 59065 Len=34
Matter          262  5540 → 59065 Len=200
Matter          104 59065 →  5540 Len=42
Matter           96  5540 → 59065 Len=34
Matter          135  5540 → 59065 Len=73
Matter          104 59065 →  5540 Len=42
Matter           96  5540 → 59065 Len=34
Matter          135  5540 → 59065 Len=73
Matter          104 59065 →  5540 Len=42
```

Right pane — IEEE 802.15.4 view:

```text
IEEE 802.15.4        150 Data, Src: 0xb800, Dst: 0xa800
IEEE 802.15.4         31 Ack
IEEE 802.15.4         60 Data, Src: 0xb800, Dst: 0xa800
IEEE 802.15.4        131 Data, Src: 0xa800, Dst: 0xb800
IEEE 802.15.4         31 Ack
IEEE 802.15.4         31 Ack
IEEE 802.15.4        150 Data, Src: 0xb800, Dst: 0xa800
IEEE 802.15.4         60 Data, Src: 0xb800, Dst: 0xa800
IEEE 802.15.4         48 Data Request
IEEE 802.15.4         31 Ack
IEEE 802.15.4        127 Data, Src: 0xb800, Dst: 0xb804
IEEE 802.15.4        115 Data, Src: 0xb804, Dst: 0xb800
IEEE 802.15.4         31 Ack
IEEE 802.15.4        116 Data, Src: 0xb800, Dst: 0xa800
IEEE 802.15.4         31 Ack
IEEE 802.15.4        131 Data, Src: 0xa800, Dst: 0xa000
IEEE 802.15.4         31 Ack
IEEE 802.15.4         31 Ack
IEEE 802.15.4         31 Ack
IEEE 802.15.4        131 Data, Src: 0xa800, Dst: 0xa400
IEEE 802.15.4         31 Ack
IEEE 802.15.4         31 Ack
```

36

## Slide 37

A cartoon meme, captioned "WELL, AIN'T THAT CUTE?", is the only content on the slide.

37

## Slide 38

##### RESULT: VERY BAD – 37%

Below it, the same cartoon character, now captioned "BUT IT'S WRONG!!!".

38

## Slide 39

##### WHY WAS THIS THE CASE?

- When forwarded through the mesh network, the same frame shows up several times

- The sniffer picks up the same frame several times

- Solution: identify **unique frames** (forwarding detection)

The right half holds a mesh graph: filled purple router squares joined by cyan edges, with magenta-outlined and red-outlined end-device squares hanging off them. Four plain grey squares sit at points around the graph, each labelled

96Bytes

39

## Slide 40

##### HEURISTICS FOR FORWARDING DETECTION

```text
if recv(frame) and send(frame) and delta(recv, send) < Threshold then
    mark_forwarded(frame)
end_if
```

An arrow points from the caption up to `Threshold` in the first line:

Value of `Threshold` determined empirically (~0.8s)

A grouped bar chart fills the lower right, drawn in a hand-sketched style. Legend: cyan — Number of unfiltered frames; pink — Number of frames after forwarding detection. The y-axis is titled Count with ticks 0, 2500, 5000, 7500, 10000, 12500, 15000, 17500, 20000; the x-axis is titled Device, with one cyan/pink pair per device, in this order:

0x5c00 LIGHTAPP, 0xb800 LIGHTAPP, 0x5c07 MOTION_SENSOR, 0xa000 SWITCH, 0x6c00 LIGHTAPP, 0x5c0a DOOR_SENSOR, 0x5c01 THERMOSTAT, 0xb400 LIGHTAPP, 0x9800 LIGHTAPP, 0xb809 MOTION_SENSOR, 0x5c08 MOTION_SENSOR, 0x3400 LIGHTAPP, 0xb80f WEATHER_SENSOR, 0xb807 DOOR_SENSOR, 0xa001 MOTION_SENSOR, 0xb806 DOORLOCK, 0x6c01 DOOR_SENSOR

The bars carry no printed values. A second arrow points from the caption down to the pink bar of the second device:

Eliminate "noise", keep only relevant frames

40

## Slide 41

##### LETS TRY AGAIN

##### RESULT: BETTER – 44%, STILL NOT GOOD

41

## Slide 42

##### WHY WAS THIS THE CASE?

Two hand-sketched bar charts, each with y-axis titled Occurrences and x-axis titled "Observed individual frame length", and every bar carrying its count above it.

Upper-left chart — y ticks 0, 50000, 100000, 150000, 200000:

| Observed individual frame length | Occurrences |
|---|---:|
| 87 | 172351 |
| 88 | 63957 |
| 91 | 20829 |
| 92 | 22 |
| 93 | 20 |
| 94 | 3 |
| 95 | 23474 |
| 101 | 352 |

A hand-drawn pink box encloses the right-hand end of this chart, from just before the 94 tick to the 101 tick.

Lower-right chart — y ticks 0, 25000, 50000, 75000, 100000, 125000:

| Observed individual frame length | Occurrences |
|---|---:|
| 94 | 105228 |
| 95 | 4178 |
| 99 | 12 |
| 100 | 12 |
| 101 | 1 |

A second pink box encloses the 94 and 95 bars.

Between the charts, two captions with pink arrows: **Payload of 42 bytes**, its arrow pointing left at the upper chart, and **Payload of 49 bytes**, its arrow pointing right at the lower chart.

42

## Slide 43

##### FRAME TRANSMISSION: DIFFERENT SIZES

The same **Matter** command can be packaged in **Thread** frames of different sizes

A small box icon labelled **Command** sits at the left; three dotted pink arrows fan out from it to three parcel icons of different sizes, each badged with the Thread logo.

43

## Slide 44

##### WHAT EXACTLY IS HAPPENING?

Nothing at the application layer seems different between commands packaged in larger or smaller frames

A **Command** icon sits at the top centre, above two numbered Wireshark panes. Both panes are clipped at their right edge on the "Message Flags" row.

Pane **1**:

```text
v Matter
  > Message Flags: 0x00, Destination ID Type: Not present
    Session ID: 0xfc77
  > Security Flags: 0x00, Session Type: Unicast Session
    Message Counter: 38695646
    Encrypted Payload (10 bytes)
    Integrity Check: 9ba27d91dd58c27d20f16f87223b702a
```

Pane **2**:

```text
v Matter
  > Message Flags: 0x00, Destination ID Type: Not present
    Session ID: 0xacee
  > Security Flags: 0x00, Session Type: Unicast Session
    Message Counter: 194035104
    Encrypted Payload (10 bytes)
    Integrity Check: 47772b688b88ce0886bb36afc63893b9
```

A dotted pink arrow drops from each pane to a Thread-badged parcel icon; the two parcels are drawn at different sizes.

44

## Slide 45

##### WHY IS THIS HAPPENING?

- Hop limit (decreases after each "hop"):

   - 1, 64, 255: compressed

   - other values: **inline** takes up space

Some nodes add Fragmentation Header (fragment of 1)

Traffic class, flow label, etc.: inline / compressed

Two Wireshark panes on the left, pane **2** overlapping and hiding the bottom rows of pane **1**. Pink ink rings `Fragmentation Header`, the Traffic class line and the Hop limit line in each.

Pane **1**:

```text
v 6LoWPAN, Src: fda0:13ed:8be5::be9, Dest: ::2d14:840c:e1a2:b52c
  > Fragmentation Header
  v IPHC Header
      011. .... = Pattern: IP header compression (0x03)
      ...0 1... .... .... = Traffic class and flow label: ECN and flow label inline (0x1)
      .... .1.. .... .... = Next header: Compressed
      .... ..00 .... .... = Hop limit: Inline (0x0)
      .... .... 1... .... = Context identifier extension: True
      .... .... .0.. .... = Source address compression: Stateless
      .... .... ..00 .... = Source address mode: Inline (0x0000)
      .... .... .... 0... = Multicast address compression: False
      .... .... .... .1.. = Destination address compression: Stateful
      .... .... .... ..01 = Destination address mode: 64-bits inline (0x0001)
    0000 .... = Source context identifier: 0x0
    .... 0001 = Destination context identifier: 0x1
  00.. .... = ECN: 0
```

Pane **2**:

```text
v 6LoWPAN, Src: ::a2c5:f62:1ac0:80f0, Dest: fda0:13ed:8be5::be9
  v IPHC Header
      011. .... = Pattern: IP header compression (0x03)
      ...1 1... .... .... = Traffic class and flow label: Version, traffic class, and flow label compressed (0x3)
      .... .1.. .... .... = Next header: Compressed
      .... ..10 .... .... = Hop limit: 64 (0x2)
      .... .... 1... .... = Context identifier extension: True
      .... .... .1.. .... = Source address compression: Stateful
      .... .... ..01 .... = Source address mode: 64-bits inline (0x0001)
      .... .... .... 0... = Multicast address compression: False
      .... .... .... .0.. = Destination address compression: Stateless
      .... .... .... ..00 = Destination address mode: Inline (0x0000)
    0001 .... = Source context identifier: 0x1
    .... 0000 = Destination context identifier: 0x0
  Source: ::a2c5:f62:1ac0:80f0
  Destination: fda0:13ed:8be5::be9
```

Pane 2's Traffic class row is itself clipped at the right edge, ending in `(0x3`.

45

## Slide 46

##### FRAME SIZE DISTRIBUTION

The same payload transmitted in frames of different length

A hand-sketched heat map fills the left. Its y-axis is titled "Observed individual frame length" with ticks 25, 35, 43, 53, 60, 81, 90, 97, 105, 112, 119; its x-axis is titled "IPv6 payload length" with ticks 34, 70, 81, 107, 145, 187, 261, 714, 1024, 1036, 1217. The colour bar beside it is titled "Occurrences, log scale", running cyan at 10⁰ through violet to pink at 10⁵, with decade ticks 10⁰, 10¹, 10², 10³, 10⁴, 10⁵. Individual cells carry no printed values.

A puzzled cartoon spider holding a ruler sits at the lower right, beside four thread spools labelled 0.5 mm, 1.0 mm, 1.5 mm and 2.0 mm.

46

## Slide 47

##### REALITY IS COMPLEX

Left — a horizontal bar chart. The y-axis is titled "IPv6 payload length", the x-axis "Distinct observed frame lengths" with ticks 0, 2, 4, 6, 8. Each bar carries its value at the tip:

| IPv6 payload length | Distinct observed frame lengths |
|---|---:|
| 42 | 8 |
| 79 | 7 |
| 89 | 7 |
| 242 | 7 |
| 1023 | 7 |
| 75 | 6 |
| 76 | 6 |
| 1026 | 6 |
| 1039 | 6 |
| 1040 | 6 |
| 1043 | 6 |
| 1031 | 6 |
| 935 | 6 |
| 1044 | 6 |
| 1034 | 6 |
| 1047 | 6 |
| 1036 | 6 |
| 1021 | 6 |
| 1022 | 6 |
| 81 | 5 |

Right — a second heat map. Its y-axis is titled "Frame count after reassembly", with ticks 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 22; its x-axis is titled "IPv6 payload length" with ticks 34, 70, 81, 107, 145, 187, 261, 714, 1024, 1036, 1217. The colour bar is again titled "Occurrences, log scale" with decade ticks 10⁰ to 10⁵. No cell values are printed.

The cartoon spider reappears at the lower left, now tangled in a heap of web.

47

## Slide 48

##### FRAMES CHANGE: HOP LIMIT

**Hop limit** changes

Upper Wireshark pane:

```text
> IEEE 802.15.4 Data, Src: 0x5c01, Dst: 0x5c00
v 6LoWPAN, Src: ::a2c5:f62:1ac0:80f0, Dest: fda0:13ed:8be5::be9
  v IPHC Header
      011. .... = Pattern: IP header compression (0x03)
      ...1 1... .... .... = Traffic class and flow label: Version, traffic class, and flow label compressed (0x3)
      .... .1.. .... .... = Next header: Compressed
      .... ..10 .... .... = Hop limit: 64 (0x2)
      .... .... 1... .... = Context identifier extension: True
      .... .... .1.. .... = Source address compression: Stateful
      .... .... ..01 .... = Source address mode: 64-bits inline (0x0001)
      .... .... .... 0... = Multicast address compression: False
      .... .... .... .0.. = Destination address compression: Stateless
      .... .... .... ..00 = Destination address mode: Inline (0x0000)
    0001 .... = Source context identifier: 0x1
    .... 0000 = Destination context identifier: 0x0
```

Lower Wireshark pane:

```text
> IEEE 802.15.4 Data, Src: 0x5c00, Dst: 0xac00
v 6LoWPAN, Src: ::a2c5:f62:1ac0:80f0, Dest: fda0:13ed:8be5::be9
  v IPHC Header
      011. .... = Pattern: IP header compression (0x03)
      ...1 1... .... .... = Traffic class and flow label: Version, traffic class, and flow label compressed (0x3)
      .... .1.. .... .... = Next header: Compressed
      .... ..00 .... .... = Hop limit: Inline (0x0)
      .... .... 1... .... = Context identifier extension: True
      .... .... .1.. .... = Source address compression: Stateful
      .... .... ..01 .... = Source address mode: 64-bits inline (0x0001)
      .... .... .... 0... = Multicast address compression: False
      .... .... .... .0.. = Destination address compression: Stateless
      .... .... .... ..00 = Destination address mode: Inline (0x0000)
    0001 .... = Source context identifier: 0x1
    .... 0000 = Destination context identifier: 0x0
  Hop limit: 63
```

At the top right, a fragment of the mesh graph: **0x5c01** as an outlined magenta square, **0x5c00** and **0xac00** as filled magenta squares, plus one unlabelled outlined square below 0x5c00. Small grey rectangles sit on the links. A dotted pink arrow labelled **Hop limit** points at the grey rectangle on the 0xac00–0x5c00 link.

48

## Slide 49

##### FRAMES CHANGE: MESH HEADER

**Mesh header** is removed

Upper Wireshark pane:

```text
> IEEE 802.15.4 Data, Src: 0x3400, Dst: 0xa000
v 6LoWPAN, Src: fda0:13ed:8be5::be9, Dest: ::e9c7:64aa:1cf2:b5f5
  v Mesh Header
    v Flags
        10.. .... = Pattern: Mesh (0x02)
        ..1. .... = V: True
        ...1 .... = D: True
        .... 1111 = Hops left: 15
      Deep Hops left (Flags.Hops left == 15): 18
      Originator: 0xac00
      Destination: 0xa000
  > Fragmentation Header
  v IPHC Header
      011. .... = Pattern: IP header compression (0x03)
      ...0 1... .... .... = Traffic class and flow label: ECN and flow label inline (0x1)
      .... .1.. .... .... = Next header: Compressed
      .... ..00 .... .... = Hop limit: Inline (0x0)
      .... .... 1... .... = Context identifier extension: True
      .... .... .0.. .... = Source address compression: Stateless
      .... .... ..00 .... = Source address mode: Inline (0x0000)
      .... .... .... 0... = Multicast address compression: False
      .... .... .... .1.. = Destination address compression: Stateful
      .... .... .... ..01 = Destination address mode: 64-bits inline (0x0001)
```

Lower Wireshark pane:

```text
> IEEE 802.15.4 Data, Src: 0xa000, Dst: 0xa001
v 6LoWPAN, Src: fda0:13ed:8be5::be9, Dest: ::e9c7:64aa:1cf2:b5f5
  v IPHC Header
      011. .... = Pattern: IP header compression (0x03)
      ...0 1... .... .... = Traffic class and flow label: ECN and flow label inline (0x1)
      .... .1.. .... .... = Next header: Compressed
      .... ..00 .... .... = Hop limit: Inline (0x0)
      .... .... 1... .... = Context identifier extension: True
      .... .... .0.. .... = Source address compression: Stateless
      .... .... ..00 .... = Source address mode: Inline (0x0000)
      .... .... .... 0... = Multicast address compression: False
      .... .... .... .1.. = Destination address compression: Stateful
      .... .... .... ..01 = Destination address mode: 64-bits inline (0x0001)
```

Top right, a mesh fragment: **0x3400** and **0xa000** as filled magenta squares, **0xa001** as a red-outlined square, plus two unlabelled filled magenta squares to the left. Grey rectangles sit on two of the links; a dotted pink arrow labelled **Mesh header** points at the one on the 0x3400–0xa000 link, which is drawn with a cyan stripe above the grey.

49

## Slide 50

##### FRAMES CHANGE: FRAGMENTATION HEADER

**Fragmentation header** is removed

Upper Wireshark pane:

```text
> IEEE 802.15.4 Data, Src: 0xac00, Dst: 0x5c00
v 6LoWPAN, Src: fda0:13ed:8be5::be9, Dest: ::a2c5:f62:1ac0:80f0
  v Fragmentation Header
      1100 0... = Pattern: First fragment (0x18)
    Datagram size: 90
    Datagram tag: 0x1a14
  v IPHC Header
      011. .... = Pattern: IP header compression (0x03)
      ...0 1... .... .... = Traffic class and flow label: ECN and flow label inline (0x1)
      .... .1.. .... .... = Next header: Compressed
      .... ..00 .... .... = Hop limit: Inline (0x0)
      .... .... 1... .... = Context identifier extension: True
      .... .... .0.. .... = Source address compression: Stateless
      .... .... ..00 .... = Source address mode: Inline (0x0000)
      .... .... .... 0... = Multicast address compression: False
      .... .... .... .1.. = Destination address compression: Stateful
      .... .... .... ..01 = Destination address mode: 64-bits inline (0x0001)
    0000 .... = Source context identifier: 0x0
    .... 0001 = Destination context identifier: 0x1
  00.. .... = ECN: 0
  ..00 .... = Padding: 0x00
  .... 0100  1110 1000  1101 0001 = Flow label: 0x04e8d1
  Hop limit: 63
```

Lower Wireshark pane:

```text
> IEEE 802.15.4 Data, Src: 0x5c00, Dst: 0x5c01
v 6LoWPAN, Src: fda0:13ed:8be5::be9, Dest: ::a2c5:f62:1ac0:80f0
  v IPHC Header
      011. .... = Pattern: IP header compression (0x03)
      ...0 1... .... .... = Traffic class and flow label: ECN and flow label inline (0x1)
      .... .1.. .... .... = Next header: Compressed
      .... ..00 .... .... = Hop limit: Inline (0x0)
      .... .... 1... .... = Context identifier extension: True
      .... .... .0.. .... = Source address compression: Stateless
      .... .... ..00 .... = Source address mode: Inline (0x0000)
      .... .... .... 0... = Multicast address compression: False
      .... .... .... .1.. = Destination address compression: Stateful
      .... .... .... ..01 = Destination address mode: 64-bits inline (0x0001)
    0000 .... = Source context identifier: 0x0
    .... 0001 = Destination context identifier: 0x1
  00.. .... = ECN: 0
  ..00 .... = Padding: 0x00
  .... 0100  1110 1000  1101 0001 = Flow label: 0x04e8d1
  Hop limit: 62
```

The lower pane overlaps and clips the right edge of the upper one. Top right, the mesh fragment: **0x5c01** as an outlined magenta square, **0x5c00** and **0xac00** as filled magenta squares, plus one unlabelled outlined square below 0x5c00. A dotted pink arrow labelled **Fragmentation header** points at the grey-and-cyan rectangle on the 0xac00–0x5c00 link; a second, plain grey rectangle sits on the 0x5c00–0x5c01 link.

50

## Slide 51

The slide has no title. On the left, the mesh fragment: **0x5c01** as an outlined magenta square, **0x5c00** and **0xac00** as filled magenta squares, and one unlabelled outlined square below 0x5c00. Grey rectangles sit on the links; only the one on the 0x5c00–0x5c01 link is labelled, **125B** — the rest are blank.

On the right, a meme captioned "DUDE, WHERE IS MY FRAME?".

51

## Slide 52

##### FRAMES CHANGE: SUDDEN FRAGMENTATION

**Fragmentation** down the forwarding path

Upper-left Wireshark pane (its Traffic class row runs off the right edge):

```text
> IEEE 802.15.4 Data, Src: 0x5c01, Dst: 0x5c00
v 6LoWPAN, Src: ::a2c5:f62:1ac0:80f0, Dest: fda0:13ed:8be5::be9
  v IPHC Header
      011. .... = Pattern: IP header compression (0x03)
      ...1 1... .... .... = Traffic class and flow label: Version, traffic
      .... .1.. .... .... = Next header: Compressed
      .... ..10 .... .... = Hop limit: 64 (0x2)
      .... .... 1... .... = Context identifier extension: True
      .... .... .1.. .... = Source address compression: Stateful
      .... .... ..01 .... = Source address mode: 64-bits inline (0x0001)
      .... .... .... 0... = Multicast address compression: False
      .... .... .... .0.. = Destination address compression: Stateless
      .... .... .... ..00 = Destination address mode: Inline (0x0000)
```

Middle Wireshark pane (also clipped on the Traffic class row):

```text
> IEEE 802.15.4 Data, Src: 0x5c00, Dst: 0xac00
v 6LoWPAN, Src: ::a2c5:f62:1ac0:80f0, Dest: fda0:13ed:8be5::be9
  v Fragmentation Header
      1100 0... = Pattern: First fragment (0x18)
    Datagram size: 120
    Datagram tag: 0xb824
  v IPHC Header
      011. .... = Pattern: IP header compression (0x03)
      ...1 1... .... .... = Traffic class and flow label: Version, traffic
      .... .1.. .... .... = Next header: Compressed
      .... ..00 .... .... = Hop limit: Inline (0x0)
      .... .... 1... .... = Context identifier extension: True
      .... .... .1.. .... = Source address compression: Stateful
      .... .... ..01 .... = Source address mode: 64-bits inline (0x0001)
      .... .... .... 0... = Multicast address compression: False
      .... .... .... .0.. = Destination address compression: Stateless
      .... .... .... ..00 = Destination address mode: Inline (0x0000)
```

Lower-right Wireshark pane:

```text
> IEEE 802.15.4 Data, Src: 0x5c00, Dst: 0xac00
v 6LoWPAN
  v Fragmentation Header
      1110 0... = Pattern: Fragment (0x1c)
    Datagram size: 120
    Datagram tag: 0xb824
    Datagram offset: 112
  > [2 Message fragments (120 bytes): #271481(112), #271483(8)]
```

The mesh fragment at the top right carries **125B** on the 0x5c00–0x5c01 link, and **122B** and **32B** on the 0xac00–0x5c00 link. Two dotted pink arrows labelled **Actual fragmentation** point at 122B and 32B.

52

## Slide 53

##### FRAGMENTATION DOES NOT ADD UP

The mesh fragment from the previous slide: **0x5c01** as an outlined magenta square, **0x5c00** and **0xac00** as filled magenta squares, one unlabelled outlined square below 0x5c00; **125B** on the 0x5c00–0x5c01 link, **122B** and **32B** on the 0xac00–0x5c00 link, with two dotted pink arrows labelled **Actual fragmentation** pointing at 122B and 32B.

To the right:

122 + 32 = 125 ?

Below it, a stock photo of three puzzled lab-coated scientists.

53

## Slide 54

The slide has no title. A South Park meme, captioned "I HAVE MANY PROBLEMS", is its only content.

54

## Slide 55

##### COMPLEX PROBLEM REQUIRES (COMPLEX) SOLUTION

Machine learning to the rescue: **Random forests**

The left half is a mesh graph — filled magenta squares for routers, magenta-outlined and red-outlined squares for end devices, joined by cyan links, with blank grey rectangles scattered along them. A tall column of blank cyan cells to its right is gathered by a pink curly brace, and a pink arrow leads from the brace to a photograph of a pine forest, over which the same blank cyan rectangles are scattered.

55

## Slide 56

##### DEVICE CLASSIFICATION – MODEL TRAINING

- Much better, accuracy increases **above 95%**

Left — a line chart with error bars. The y-axis is titled "Average accuracy" with ticks 0.0, 0.2, 0.4, 0.6, 0.8, 1.0; the x-axis is titled "Training window size (hours)" with ticks 1, 2, 3, 5, 8, 10. The legend is headed "Input frame count" and lists 5 frames, 7 frames, 9 frames, 11 frames. The four series lie on top of one another, so only one curve is visible; no point values are printed.

Right — a heat map of the same experiment, y-axis "Training window size (hours)", x-axis "Input frame count", with a colour bar titled "Average accuracy" ticked 0.91, 0.92, 0.93, 0.94, 0.95. Every cell carries its value:

| Training window size (hours) | 5 | 7 | 9 | 11 |
|---|---|---|---|---|
| 1 | 0.901 | 0.902 | 0.904 | 0.905 |
| 2 | 0.906 | 0.908 | 0.908 | 0.909 |
| 3 | 0.906 | 0.906 | 0.907 | 0.908 |
| 5 | 0.910 | 0.910 | 0.910 | 0.910 |
| 8 | 0.952 | 0.952 | 0.952 | 0.952 |
| 10 | 0.953 | 0.953 | 0.953 | 0.953 |

56

## Slide 57

##### DEVICE CLASSIFICATION – HOW LONG TO WAIT

- The more time we sniff, the more frames we acquire

- It's more a question of having **the "right" frames**

Left — a line chart with error bars, y-axis titled "Average frame count" with ticks 20000, 40000, 60000, 80000, x-axis titled "Training window size (hours)". The visible tick labels are 1, 2, 3 and 5; the right-hand end of the axis is covered by the second chart. Each point carries its value, left to right: 9261, 18532, 26812, 44999, 70793, 88470.

Right — a scatter plot overlapping the first, y-axis titled "Accuracy" with ticks 0.0, 0.2, 0.4, 0.6, 0.8, 1.0, x-axis titled "Frame count" with ticks 20000, 40000, 60000, 80000. Legend headed "Input frame count": 5 frames, 7 frames, 9 frames, 11 frames. Most points sit just under 1.0; four outliers sit near 0.75. No point values are printed.

57

## Slide 58

##### YAP: YET ANOTHER PROBLEM

We are seeing more devices than we know we have in the lab

A step chart fills the slide. The y-axis is titled "Number of observed RLOCs" with ticks 0, 10, 20, 30, 40; the x-axis is titled "Time since capture start (hours)" with ticks 0, 20, 40, 60, 80. Each step is marked with a pink star and annotated with the RLOC that appeared.

The annotations over the first two hours are printed on top of each other and most cannot be resolved even at high magnification. The labels that do read, low to high, are `0xb80f`, `0xb800`, `0x6c00`, `0xac00`, `0xb807`, `0x9800`, `0x5c08`, `0xb700`, `0x0800`, `0x0b02` and `0xb401`. Further along the curve, where the labels are spaced out: `0xa002`; then an overlapping pair, of which only the trailing `0008` and the leading `0xb` are legible; then `0xa003`, `0xe9d4`, `0x5c82`, `0x7c0f`, `0xfc00`, `0xb405`, `0xb403` and `0xb407`, with at least one further label in the `0xb4..` group unreadable under the others.

A Simpsons meme sits inside the plot area, captioned "HOUSTON, WE HAVE A PROBLEM.".

58

## Slide 59

59

## Slide 60

##### DEVICE COUNT IS CONSTANT

When a new device **shows up**, another one **disappears**

The chart behind that line has a legend with two entries: a pink star for "Becomes active" and a cyan cross for "Becomes inactive". Its y-axis is titled "Number of active RLOCs (30-minute window)" with ticks 0, 5, 10, 15, 20, 25, 30; its x-axis is titled "Time since capture start (hours)" with ticks 0, 20, 40, 60, 80, 100. The trace rises to about 16 in the first hour and thereafter oscillates in bursts between 16 and roughly 25–29.

60

## Slide 61

##### ROUTING LOCATOR 16: RLOC16

- 16-bit address assigned to every Thread device that identifies its location in the current Thread topology

- It is sent **non-encrypted**

- Router vs **Child**

- Router ID: upper 6 bits

- **Child ID**: lower 10 bits

_RLOC16 = (Router ID_ ≪ _10) + Child ID_

A 16-cell bit strip runs below, numbered left to right 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0. Cells 15–10 are shaded grey and braced **Router ID**; cells 9–0 are white and braced **Child ID**.

On the right, a mesh graph of filled magenta squares (routers) linked in cyan, with magenta-outlined and red-outlined squares hanging off them. Three nodes are labelled: **0x5c00** on a filled router square, **0x5c01** and **0x5c02** on two red-outlined end devices attached to it.

61

## Slide 62

##### RLOC16 MAY CHANGE

- Depending on the device, network state, RLOC16 may change

- Some devices do not change their RLOC16 for weeks, others change it more frequently

- Solution: **fingerprinting**

A timeline chart fills the lower half: one horizontal lane per device, y-axis titled Device, x-axis titled "Time since capture start (hours)" with ticks 0, 20, 40, 60, 80, 100. Each device's lane is annotated with the RLOC16 it held, and a coloured star marks each change. Product thumbnails sit beside the device names.

| Device | RLOC16s held, in order |
|---|---|
| tado radiator | 0x5c01 → 0xb406 |
| nordic nrf | 0x5c0b → 0xb400 |
| nanoleaf light bulb 624 | 0x3400 |
| nanoleaf light bulb 224 | 0x9800 |
| eve weather | 0xb80f → 0xb403 |
| eve motion 629 | 0xb809 → 0xb404 |
| eve motion 626 | 0x5c07 → 0xb405 |
| eve energy | 0xa000 |
| eve door and window 95 | 0x5c0a → 0xa001 |
| eve door and window 94 | 0xb807 |
| cono lamp | 0x6c00 |
| aqara smart lock | 0xb806 |
| aqara motion 61 | 0xa001 → 0xb401 → 0xa002 → 0xb402 → 0xa003 → 0xb407 |
| aqara bulb 508 | 0x5c00 |
| aqara bulb 204 | 0xb800 |

The nordic nrf changes about two hours in; the aqara motion 61 changes four times inside the first forty hours and once more near hour 97; the remaining changes all fall around hour 93.

62

## Slide 63

##### DEVICE FINGERPRINTING

- Trained model

- The number of frames used as input does not have a major impact

- However, we seem to peak out in terms of accuracy at **~11 frames**

Left — a line chart with error bars. The y-axis is titled "Average accuracy" with ticks 0.0, 0.2, 0.4, 0.6, 0.8, 1.0; the x-axis is titled "Training window size (hours)" with ticks 1, 2, 3, 5, 8, 10. Legend headed "Input frame count": 5 frames, 7 frames, 9 frames, 11 frames. The four curves lie almost on top of one another just below 0.8, rising slightly to the right. No point values are printed.

Right — the matching heat map, y-axis "Training window size (hours)", x-axis "Input frame count", colour bar titled "Average accuracy" with ticks 0.79, 0.80, 0.81, 0.82, 0.83:

| Training window size (hours) | 5 | 7 | 9 | 11 |
|---|---|---|---|---|
| 1 | 0.786 | 0.789 | 0.790 | 0.792 |
| 2 | 0.794 | 0.797 | 0.799 | 0.800 |
| 3 | 0.795 | 0.799 | 0.800 | 0.801 |
| 5 | 0.800 | 0.805 | 0.806 | 0.806 |
| 8 | 0.825 | 0.830 | 0.831 | 0.831 |
| 10 | 0.826 | 0.831 | 0.832 | 0.832 |

63

## Slide 64

# PRACTICAL EXPLOITATION

64

## Slide 65

##### END-APPROACH

A row of six chevrons, left to right:

1. Thread frame sniffing
2. Frame forwarding detection
3. Frame variance elimination
4. Frame defragment
5. Device classification
6. Device fingerprinting

The first and last are cyan; the four between them shade from white through grey. A pink fingerprint icon sits below the row.

65

## Slide 66

##### TARGET BUILDING: OFFICES

Thread network in a partner building from Târgu Mureș, Romania!

We **asked and got permission** to analyze one of the office's Thread setup!

A relief map of Romania with a red pin sits at the left. The photograph on the right shows the office block; a thick pink arrow labelled **Thread network** points into it, and a second pink arrow points from the building back down to an illustration of a boy with a laptop wired to an antenna board, radiating wireless waves and envelope icons.

66

## Slide 67

##### BUILDING SURVEILLANCE SCENARIOS

**1** — a cutaway illustration of an office floor, with a photograph of one of the speakers standing in a lift lobby holding a laptop dropped into the middle of it.

Inside the building, sniff other's offices

- Signal strength can be very good
- More frames, more details

**2** — an illustration of an office tower ringed by cloud, camera, bulb and meter icons, with a photograph of the two speakers standing outside on the grass laid over it.

Outside the building, sniff whatever is leaking out

- Signal strength can vary, often significantly
- More time needed to capture (relevant) frames

67

## Slide 68

##### INTEGRATED APPLICATION

Real-time Thread frame capture & analysis

Off-line Thread frame analysis

Integrates ML model for device identification

Automated Thread channel scan & detection

Dotted pink lines connect those four captions to the centre: a photograph of an nRF development board and a binary-file icon feed in from the left, a neural-network graphic sits at the right, and a channel-spectrum graphic sits below. The **python** logo tops the centre screenshot.

The screenshot is headed **Thread Network Topology · 573s elapsed** and draws fourteen nodes, each a coloured disc carrying its RLOC16 with role and class badges:

| RLOC16 | Badges |
|---|---|
| 0xa00c | DOOR_SENSOR |
| 0xa00e | DOORLOCK |
| 0xa008 | MOTION_SENSOR |
| 0xa000 | ROUTER, LIGHTAPP |
| 0xa800 | BORDER ROUTER |
| 0xa00a | MOTION_SENSOR |
| 0xb804 | THERMOSTAT |
| 0xb800 | ROUTER, LIGHTAPP |
| 0x6c00 | LIGHTAPP |
| 0xb806 | MOTION_SENSOR |
| 0xb807 | WEATHER_SENSOR |
| 0xec00 | LIGHTAPP |
| 0xa400 | LIGHTAPP |
| 0x3400 | LIGHTAPP |

Edges are labelled `rate · RSSI`. Those that read clear of overlaps are 1.1 · -44dBm, 0.5 · -50dBm, 0.4 · -56dBm, 3.0 · -49dBm, 1.4 · -54dBm, 0.3 · -50dBm, 8.8 · -41dBm, 9.0 · -54dBm, 1.0 · -44dBm, 4.3 · -52dBm, 3.4 · -52dBm, 5.6 · -59dBm, 0.2 · -55dBm, 0.1 · -41dBm, 0.8 · -49dBm, 0.3 · -54dBm and 0.1 · -57dBm; several others are printed over one another.

Three stacked panels run down the right of the screenshot: **Mean RSSI** (dBm, ticks -51.0, -52.5, -54.0), **Active Nodes** (nodes, ticks 0, 5, 10, 15) and **Frames / second** (frames/s, ticks 0, 30, 60, 90).

Its footer reads:

| Nodes seen | Active nodes | Active edges | Frames total | RSSI min/avg/max |
|---|---|---|---|---|
| 14 | 14 | 26 | 1832 | -66 / -50 / -35 dBm |

The RSSI figure sits over a red-to-green colour bar scaled -95 · -62 · -30.

The spectrum graphic below the screenshot repeats the one from slide 21 — lobes over a double-headed axis annotated `2.400 GHz` and `2483 GHz`, tick labels 11 to 27 — with a bracket under channels 11–25 captioned:

2.4 GHz15M Band

Channels 11 to 25

68

## Slide 69

##### THREAD CHANNEL DISCOVERY

```text
(venv) [bgenge@bgenge-l BHUSA]$ sudo python dynamic_network_topology.py
Starting capture on /dev/ttyACM0 - auto-scanning channels for Thread traffic…
[capture] No channel specified - scanning for Thread traffic…
[scan] ─────────────────────────────────────────────
[scan]  802.15.4 channel scan
[scan]  Range  : Ch 11-26  (16 channels)
[scan]  Dwell  : 2.0 s/channel
[scan]  Est.   : ~32 s total
[scan] ─────────────────────────────────────────────
[scan]  Ch 11 [ 1/16]   38 frame(s)  ███████████████ ◄ best so far
[scan]  Ch 12 [ 2/16]    1 frame(s)  █
[scan]  Ch 13 [ 3/16]    0 frame(s)  ·  (no traffic)
[scan]  Ch 14 [ 4/16]    0 frame(s)  ·  (no traffic)
[scan]  Ch 15 [ 5/16]    1 frame(s)  █
[scan]  Ch 16 [ 6/16]    0 frame(s)  ·  (no traffic)
[scan]  Ch 17 [ 7/16]    0 frame(s)  ·  (no traffic)
[scan]  Ch 18 [ 8/16]    0 frame(s)  ·  (no traffic)
[scan]  Ch 19 [ 9/16]    0 frame(s)  ·  (no traffic)
[scan]  Ch 20 [10/16]    0 frame(s)  ·  (no traffic)
[scan]  Ch 21 [11/16]    0 frame(s)  ·  (no traffic)
[scan]  Ch 22 [12/16]    0 frame(s)  ·  (no traffic)
[scan]  Ch 23 [13/16]    0 frame(s)  ·  (no traffic)
[scan]  Ch 24 [14/16]    0 frame(s)  ·  (no traffic)
[scan]  Ch 25 [15/16]    2 frame(s)  █
[scan]  Ch 26 [16/16]    0 frame(s)  ·  (no traffic)
```

The bars after each frame count are drawn as solid white blocks whose width scales with the count; they are transcribed above with block characters.

69

## Slide 70

##### INSIDE THE BUILDING, OUTSIDE OF OFFICE

A photograph of one of the speakers standing in a lift lobby with a laptop, and beside it the tool's three panels — **Mean RSSI**, **Active Nodes** (nodes, ticks 0, 5, 10, 15) and **Frames / second** (frames/s, ticks 0, 20, 40, 60). The Active Nodes trace climbs in steps from about 2 to 15; the Mean RSSI panel's own axis labels are hidden behind the photograph.

The topology view on the right carries fifteen nodes, each with a product photo alongside:

| RLOC16 | Badges |
|---|---|
| 0xa00a | MOTION_SENSOR |
| 0xa008 | MOTION_SENSOR |
| 0xf400 | LIGHTAPP |
| 0xa400 | SWITCH |
| 0xa000 | ROUTER, LIGHTAPP |
| 0xa00c | DOOR_SENSOR |
| 0xa00e | MOTION_SENSOR |
| 0xec09 | LIGHTAPP |
| 0xec00 | LIGHTAPP |
| 0xa800 | BORDER ROUTER |
| 0xb800 | ROUTER, LIGHTAPP |
| 0x6c00 | LIGHTAPP |
| 0xb807 | LIGHTAPP |
| 0xb804 | THERMOSTAT |
| 0x3400 | LIGHTAPP |

Legible edge labels: 0.0 · -72dBm, 0.0 · -74dBm, 1.5 · -91dBm, 0.7 · -89dBm, 3.6 · -89dBm, 0.3 · -84dBm, 0.4 · -90dBm, 1.7 · -74dBm, 0.8 · -89dBm, 2.6 · -76dBm, 5.2 · -74dBm, 1.9 · -89dBm, 4.5 · -90dBm, 4.0 · -91dBm, 2.2 · -89dBm, 0.5 · -76dBm and 1.4 · -92dBm. Several more are clipped by neighbouring labels.

70

## Slide 71

##### INSIDE THE BUILDING, FLOOR -2

A photograph of the same speaker with his laptop in a basement lobby marked **P**, and the tool's three panels — **Mean RSSI**, **Active Nodes** (nodes, ticks 0, 3, 6, 9) and **Frames / second** (frames/s, ticks 0, 4, 8, 12). The active-node trace sits at about 8 throughout, with one brief step to 9.

The topology view carries twelve nodes:

| RLOC16 | Badges |
|---|---|
| 0xf400 | — |
| 0x3400 | — |
| 0xa400 | LIGHTAPP |
| 0xb804 | THERMOSTAT |
| 0xa00e | MOTION_SENSOR |
| 0xb800 | BORDER ROUTER |
| 0xa800 | ROUTER, LIGHTAPP |
| 0x6c00 | LIGHTAPP |
| 0xa000 | ROUTER, LIGHTAPP |
| 0xa008 | LIGHTAPP |
| 0xa00c | — |
| 0xa00a | — |

Edge labels: 0.8 · -88dBm, 0.1 · -92dBm, 2.1 · -88dBm, 0.0 · -90dBm, 0.2 · -92dBm and 0.3 · -92dBm.

71

## Slide 72

##### OUTSIDE THE BUILDING

Two photographs at the left — the speakers standing on the grass outside, and the office block itself, with a pink arrow running from the first to the second. Below them the tool's panels: **Mean RSSI** (its plot mostly hidden behind the building photo), **Active Nodes** (nodes, ticks 0, 5, 10, 15) and **Frames / second** (frames/s, ticks 0, 10, 20, 30).

The topology view carries fifteen nodes:

| RLOC16 | Badges |
|---|---|
| 0xa005 | MOTION_SENSOR |
| 0xe000 | LIGHTAPP |
| 0xb80c | LIGHTAPP |
| 0xb80b | MOTION_SENSOR |
| 0xa001 | — |
| 0xb807 | DOOR_SENSOR |
| 0xb802 | THERMOSTAT |
| 0xb800 | ROUTER, LIGHTAPP |
| 0xb80d | LIGHTAPP |
| 0x9800 | MOTION_SENSOR |
| 0x6c00 | LIGHTAPP |
| 0x5400 | LIGHTAPP |
| 0x5404 | LIGHTAPP |
| 0xec00 | LIGHTAPP |
| 0xd000 | BORDER ROUTER |

Legible edge labels: 0.0 · -89dBm, 0.0 · -79dBm, 0.1 · -78dBm, 0.3 · -84dBm, 0.0 · -87dBm, 0.2 · -87dBm, 0.1 · -77dBm, 0.3 · -89dBm, 0.0 · -66dBm, 0.2 · -84dBm, 0.1 · -74dBm, 0.1 · -84dBm, 0.2 · -89dBm, 2.2 · -85dBm, 0.0 · -81dBm and 0.0 · -82dBm. Others are printed over one another or hidden behind the product photos.

72

## Slide 73

##### AT A NEARBY FAST FOOD ~30m DISTANCE

A photograph of one of the speakers working on a laptop at an outdoor table, a pink arrow from the caption **Target building** pointing at the glass block behind him.

The tool's panels below: **Mean RSSI** (tick -91.5), **Active Nodes** (nodes, ticks 0, 2, 4, 6 — the trace sits at 6 and dips briefly to 5) and **Frames / second** (frames/s, ticks 0, 5, 10, 15).

The topology view carries seven nodes:

| RLOC16 | Badges |
|---|---|
| 0xa000 | ROUTER, MOTION_SENSOR |
| 0xa00a | — |
| 0xb807 | — |
| 0xa800 | BORDER ROUTER |
| 0xb800 | ROUTER, LIGHTAPP |
| 0x6c00 | LIGHTAPP |
| 0xb804 | MOTION_SENSOR |

Edge labels: 0.0 · -90dBm, 0.0 · -92dBm (twice), 0.9 · -88dBm, 0.1 · -91dBm and 0.2 · -88dBm.

73

## Slide 74

##### OTHER SIDE OF THE BUILDING

Two photographs: the office block, and one of the speakers standing at a side entrance giving a thumbs-down, with a pink arrow running from her back to the building. The tool's panels sit behind them: **Mean RSSI** (tick -88, most of the plot hidden), **Active Nodes** (nodes, ticks 0, 2, 4, 6 — the trace holds at 2 then steps up to 5) and **Frames / second** (frames/s, ticks 0, 4, 8, 12).

The topology view carries five nodes:

| RLOC16 | Badges |
|---|---|
| 0xb807 | — |
| 0xb802 | — |
| (label hidden behind the photograph, ending `0b`) | MOTION_SENSOR |
| 0xb800 | BORDER ROUTER |
| 0xd000 | ROUTER, LIGHTAPP |

Edge labels: 0.2 · -84dBm, 0.2 · -82dBm, 1.5 · -85dBm, 0.1 · -85dBm and 3.8 · -85dBm.

74

## Slide 75

###### REMOTE MONITORING IS POSSIBLE
###### LOCATION, LOCATION, LOCATION

A pink arrow labelled **Thread network** points from the caption into the photograph of the office block; a second pink arrow runs from the building back to an illustration of a boy with a laptop and an antenna board, captioned **The place to be**. A still of Eminem on stage sits in the bottom-left corner.

75

## Slide 76

# DEMO
# THE INNOCENT BYSTANDERS

Two photographs below the title: the two speakers standing outdoors, and the office block.

76

## Slide 77

# KEY TAKEAWAYS
# &
# ACTIONABLE ITEMS

Two cyan icons below the title: an open hand and a clapperboard.

77

## Slide 78

##### TAKEAWAYS

1. An increasing number of devices rely on wireless comms, making them inherently **susceptible to remote attacks**

2. **Insufficient protection** allows traffic capture, analysis, and information leakage. This can have serious privacy implications, leading to building and people profiling

3. **Protocols are** typically **not tested for "information leakage"** and therefore their design is not tailored to minimize information leakage

The numbers are set in pink circles; the cyan open-hand icon repeats at the foot of the slide.

78

## Slide 79

##### ACTIONABLE ITEMS

**Protocol designers:**

1. **Add security (cryptographic) protection** before moving  towards critical applications (e.g., building automation / industry-gradeapplications)

2. **Continue to research** the **security of Thread**, Matter/Thread; these are still new protocols and **likely have undiscovered attack surfaces**. They are also very popular (with steadily growing adoption), hence, vulnerabilities in these protocols may have significant or critical consequences

**Building designers:**

3. Carefully **consider the positioning of critical devices**, since communications can expose them to remote surveillance

A cyan clapperboard sits beside the title; a shield, a microscope and an office-block icon sit at the right of items 1, 2 and 3.

79

## Slide 80

##### ACTIONABLE ITEMS

**Everyone:**

4. Take this research further! Application-layer metadata is now freely available to the security community!

   <u>https://github.com/bitdefender/matter-iot-dataset</u>

   A screenshot of that repository: **matter-iot-dataset** Public — Watch 0 — main | 1 Branch | 0 Tags | Go to file | Add file | Code. Last commit row: ipadurean-bd, "Initial commit", d8bcd26 · last month, 1 Commit. Contents: `dataset` — Initial commit — last month; `README.md` — Initial commit — last month.

5. Create your own IoT virtual playground with realistic devices! We have published a Matter IoT framework!

   <u>https://github.com/bitdefender/matter-ctf</u>

   A screenshot of that repository: **matter-ctf** Public — Edit Pins — Watch 0 — main | 1 Branch | 0 Tags | Go to file | Add file | Code. Last commit row: bgenge-bd, "Add JOBS argument and note regarding target platform", 6c9d280 · 4 months ago, 2 Commits. Contents: `devices-app` — Add JOBS argument and note regarding target platform — 4 months ago; `matter-server` — Initial commit — 5 months ago.

80

## Slide 81

# Thank you! Questions?

<u>bgenge@bitdefender.com, aburduv@bitdefender.com</u>

81
