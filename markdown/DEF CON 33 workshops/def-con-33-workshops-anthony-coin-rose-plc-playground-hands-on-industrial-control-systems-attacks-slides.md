---
title: "PLC Playground_ Hands-On Industrial Control Systems Attacks"
speakers: ["Anthony _Coin_ Rose"]
conference: "DEF CON"
conference_full: "DEF CON 33"
edition: "33"
year: 2025
source_pdf: "DEF CON 33 workshops/DEF CON 33 - Workshops - Anthony _Coin_ Rose - PLC Playground_ Hands-On Industrial Control Systems Attacks - Slides.pptx"
pages: 46
sha256: "45d68ffd0e823dd641590d1f906e9b99ccb0b3983fd257a2682e7a3b76359ee9"
text_chars: 16020
ocr_pages: 0
has_ocr: false
redacted_secrets: 0
ocr_confidence: null
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2"
converted_at: "2026-08-12T06:28:29Z"
---
# PLC Playground_ Hands-On Industrial Control Systems Attacks

**Speakers:** Anthony _Coin_ Rose  
**Conference:** DEF CON 33  
**Source:** `DEF CON 33 workshops/DEF CON 33 - Workshops - Anthony _Coin_ Rose - PLC Playground_ Hands-On Industrial Control Systems Attacks - Slides.pptx` (46 pages)


## Slide 1

**_The AFIT of Today is the Air Force of Tomorrow._**

**PLC Playground: Hands-On Industrial Control Systems Attacks**

This briefing, presentation, or document is for information only. No US Government commitment to sell, loan, lease, co-develop or co-product defense articles or provide defense services is implied or intended

**_Air University: The Intellectual and Leadership Center of the Air Force Aim High ... Fly-Fight-Win_**

## Slide 2

## **Introduction to Cyber-Physical Systems**

**_The AFIT of Today is the Air Force of Tomorrow._**

- Cyber-Physical Systems are integrations of computing, networking, and physical processes.

- Software controls physical components like motors, sensors, valves, and pumps.

- Real-time responsiveness is critical: delays can lead to safety or mission failure

**_Air University: The Intellectual and Leadership Center of the Air Force Aim High ... Fly-Fight-Win_**

2

## Slide 3

## **What are Industrial Control Systems?**

**_The AFIT of Today is the Air Force of Tomorrow._**

- Industrial Control Systems (ICS) are systems that integrate computation, networking, and physical processes to monitor and control industrial operations.Examples: Power grids, water treatment plants, manufacturing assembly lines.

**_Air University: The Intellectual and Leadership Center of the Air Force Aim High ... Fly-Fight-Win_**

## Slide 4

## **Industrial Control Systems**

**_The AFIT of Today is the Air Force of Tomorrow._**

<u>Source: NIST Special Publication 800-82 r2, Guide to Industrial Control Systems (ICS) Security.</u>

**_Air University: The Intellectual and Leadership Center of the Air Force Aim High ... Fly-Fight-Win_**

4

## Slide 5

## **Key Components of ICS**

**_The AFIT of Today is the Air Force of Tomorrow._**

- Sensors: Measure physical parameters (e.g., temperature, pressure).

- Actuators: Respond to control signals (e.g., motors, valves).

- Controllers: Devices like Programmable Logic Controllers (PLCs) or Distributed Control Systems (DCS) that process inputs and adjust processes.

- • Human-Machine Interface (HMI): Enables operators to monitor and interact with the system.

**_Air University: The Intellectual and Leadership Center of the Air Force Aim High ... Fly-Fight-Win_**

5

## Slide 6

## **Why ICS is Important?**

**_The AFIT of Today is the Air Force of Tomorrow._**

- Supports essential services like energy, water, transportation, and manufacturing.

- Plays a vital role in ensuring efficiency, safety, and reliability in industrial operations.

**_Air University: The Intellectual and Leadership Center of the Air Force Aim High ... Fly-Fight-Win_**

6

## Slide 7

## **Common Examples of ICS**

**_The AFIT of Today is the Air Force of Tomorrow._**

- Energy Sector: Supervisory Control and Data Acquisition (SCADA) systems in power plants.

- Transportation: Automated signaling in railway systems.

- Manufacturing: Assembly line automation in car production.

- Utilities: Water distribution and sewage treatment systems.

**_Air University: The Intellectual and Leadership Center of the Air Force Aim High ... Fly-Fight-Win_**

7

## Slide 8

## **Operational Technology**

**_The AFIT of Today is the Air Force of Tomorrow._**

<u>Source: https://commons.wikimedia.org/wiki/File:Transfer_Pump_Station.jpg</u> **_Air University: The Intellectual and Leadership Center of the Air Force Aim High ... Fly-Fight-Win_**

## Slide 9

## **What is CI?**

**_The AFIT of Today is the Air Force of Tomorrow._**

- Chemical

- Commercial Facilities

- Communications

- Crit. Manufacturing

- Dams

- Defense Industrial

- Emergency Services

- Energy

- Financial Services

- Food & Agriculture

- Govt. Facilities

- Healthcare

- Information Tech

- Nuclear

- Transportation

- Water & Wastewater

Public or **_Air University: The Intellectual and Leadership Center of the Air Force_** private? **_Aim High ... Fly-Fight-Win_**

9

## Slide 10

## **Components**

**_The AFIT of Today is the Air Force of Tomorrow._**

- Building Automation – HVAC, access control

- Power – distribution, backup generation, conservation

- Water – treatment and waste

- Security – perimeter defenses, cameras

- Transportation – traffic lights, street lights

- Emergency Services – police, fire, EMS

- Flight Line – lights, communications

- Weapon Systems

- Fueling Systems

**_Air University: The Intellectual and Leadership Center of the Air Force Aim High ... Fly-Fight-Win_**

10

## Slide 11

## **Field Sites**

**_The AFIT of Today is the Air Force of Tomorrow._**

**_Air University: The Intellectual and Leadership Center of the Air Force_** <u>Image: https://www.reeng.com.au/products/control-systems/</u> **_<u>Aim High ... Fly-Fight-Win</u>_**

11

## Slide 12

## **Field Sites**

**_The AFIT of Today is the Air Force of Tomorrow._**

**Digital: 0 – 24  VDC 0 – 110 VAC Analog: 0 – 10 VDC 0 – 20 mA 4 – 20 mA**

**_Air University: The Intellectual and Leadership Center of the Air Force Aim High ... Fly-Fight-Win_**

12

## Slide 13

## **ICS and Internet Connectivity**

**_The AFIT of Today is the Air Force of Tomorrow._**

- Modernization of ICS:

   - Increasing integration of Industrial Control Systems (ICS) with IT networks and the internet.

   - • Adoption of protocols like PROFINET and Ethernet/IP for communication.

**???**

- Unintended Consequences:

   - Direct or indirect internet access introduces significant vulnerabilities.

   - Legacy ICS systems often lack built-in security measures.

**_Air University: The Intellectual and Leadership Center of the Air Force Aim High ... Fly-Fight-Win_**

13

## Slide 14

## **Key Challenges**

**_The AFIT of Today is the Air Force of Tomorrow._**

- Weak or Optional Security

   - Security mechanisms are often not prioritized or are optional in ICS setups.

   - Example: Firewalls or intrusion detection systems are frequently omitted.

- Legacy Systems

   - Many ICS were not designed with internet connectivity in mind.

   - Patching and updating older systems can be difficult without downtime.

- Attack Surface Expansion

   - Direct exposure of ICS devices to the internet increases the risk of:

      - Unauthorized Access via poorly secured remote connections.

      - Cyber Attacks like ransomware or data exfiltration.

**_Air University: The Intellectual and Leadership Center of the Air Force Aim High ... Fly-Fight-Win_**

14

## Slide 15

## **EMCS**

**_The AFIT of Today is the Air Force of Tomorrow._**

**_Air University: The Intellectual and Leadership Center of the Air Force Aim High ... Fly-Fight-Win_**

15

<u>Source: Max Cornelisse</u>

## Slide 16

### **The Challenge of Internet-Exposed Devices**

**_The AFIT of Today is the Air Force of Tomorrow._**

- Internet-facing devices are ICS components that are directly accessible from the internet without adequate security controls.

- A significant number of critical devices (e.g., wastewater, manufacturing) are exposed.

- Many are listed as "Unknown," indicating poor inventory or security practices.

**_Air University: The Intellectual and Leadership Center of the Air Force Aim High ... Fly-Fight-Win_**

16

## Slide 17

## **Internet Facing Devices**

**_The AFIT of Today is the Air Force of Tomorrow._**

**_Air University: The Intellectual and Leadership Center of the Air Force Aim High ... Fly-Fight-Win_**

17

## Slide 18

## **Bridge PLC**

**_The AFIT of Today is the Air Force of Tomorrow._**

**_Air University: The Intellectual and Leadership Center of the Air Force Aim High ... Fly-Fight-Win_**

18

<u>Source: Max Cornelisse</u>

## Slide 19

## **ICS Attack Difficulty**

**_The AFIT of Today is the Air Force of Tomorrow._**

**_Air University: The Intellectual and Leadership Center of the Air Force Aim High ... Fly-Fight-Win_**

19

## Slide 20

## **Targets**

**_The AFIT of Today is the Air Force of Tomorrow._**

**_Air University: The Intellectual and Leadership Center of the Air Force_** <u>Source: NIST Special Publication 800-82 r2, Guide to Industrial Control Systems (ICS) Security.</u> **_Aim High ... Fly-Fight-Win_**

20

## Slide 21

## **Vendor Tools**

**_The AFIT of Today is the Air Force of Tomorrow._**

**_Air University: The Intellectual and Leadership Center of the Air Force Aim High ... Fly-Fight-Win_**

21

## Slide 22

## **Easy Defense**

**_The AFIT of Today is the Air Force of Tomorrow._**

**_Air University: The Intellectual and Leadership Center of the Air Force Aim High ... Fly-Fight-Win_**

22

## Slide 23

## **Build Your Own Tools**

#### **_The AFIT of Today is the Air Force of Tomorrow._**

**_Air University: The Intellectual and Leadership Center of the Air Force Aim High ... Fly-Fight-Win_**

23

## Slide 24

## **Firmware Implants**

**_The AFIT of Today is the Air Force of Tomorrow._**

Deployment

Payloads

Triggers

**_Air University: The Intellectual and Leadership Center of the Air Force Aim High ... Fly-Fight-Win_**

24

## Slide 25

## **Why Firmware Implants**

**_The AFIT of Today is the Air Force of Tomorrow._**

- Full control over device

- Bypass security mechanisms

- Include backdoors

- Self propagation

- Impossible to detect

- Impossible to clean device

- Unless you use physical access

**_Air University: The Intellectual and Leadership Center of the Air Force Aim High ... Fly-Fight-Win_**

25

## Slide 26

## **Hardware**

**_The AFIT of Today is the Air Force of Tomorrow._**

**_Air University: The Intellectual and Leadership Center of the Air Force Aim High ... Fly-Fight-Win_**

26

## Slide 27

## **Defense – NIST Framework**

**_The AFIT of Today is the Air Force of Tomorrow._**

- Identify – Passive monitoring

- Protect – Isolation/segmentation

- Detect – Deep packet inspection

- Respond – Manual operation

- Recover – Bring back automation

**_Air University: The Intellectual and Leadership Center of the Air Force Aim High ... Fly-Fight-Win_**

27

## Slide 28

## **The HILICS Platform**

**_The AFIT of Today is the Air Force of Tomorrow._**

- Hardware-in-the-Loop ICS

- Real ICS equipment is expensive, large, and difficult to scale.

   - Water tanks, compressors, and valves are impractical for classrooms.

   - One physical trainer can’t support 30+ students simultaneously.

- Emulation alone isn’t realistic, real PLC hardware matters

- As far as the PLC knows, it's controlling a real industrial process.

https://github.com/sdunlap-afit/hilics

**_Air University: The Intellectual and Leadership Center of the Air Force Aim High ... Fly-Fight-Win_**

28

## Slide 29

## **HILICS Architecture**

**_The AFIT of Today is the Air Force of Tomorrow._**

**_Air University: The Intellectual and Leadership Center of the Air Force Aim High ... Fly-Fight-Win_**

29

## Slide 30

## **HILICS Architecture**

**_The AFIT of Today is the Air Force of Tomorrow._**

- Raspberry Pi acts as the physical process simulation (e.g., door, tank).

- MicroLogix 1100 is the real PLC you're attacking or defending.

- All traffic (VNC + PLC) is routed via the Pi’s IP using port forwarding.

- Students access their kits remotely using web browser + VPN.

- The setup mimics a NATed industrial environment with remote access.

**_Air University: The Intellectual and Leadership Center of the Air Force Aim High ... Fly-Fight-Win_**

30

## Slide 31

## **Initial Setup Instructions**

**_The AFIT of Today is the Air Force of Tomorrow._**

- Open noVNC in Browser

   - VNC gives you visual access to the Raspberry Pi simulation.

   - All tools run in this environment.

- Access PLC Web Interface

   - Navigate to http://<kit_ip> to confirm PLC is online.

- Configure RSLinx

   - Set up Ethernet/IP driver to talk to the MicroLogix 1100.

- Launch RSLogix 500

   - Upload/download the PLC logic.

   - Go online to observe or modify the ladder logic.

**_Air University: The Intellectual and Leadership Center of the Air Force Aim High ... Fly-Fight-Win_**

31

## Slide 32

**Tool**

**noVNC**

**PLC Web UI RSLinx Classic**

**RSLogix 500 Wireshark**

## **HILICS Toolchain**

**_The AFIT of Today is the Air Force of Tomorrow._**

**Purpose**

Browser-based remote desktop for Raspberry Pi GUI

Verify connectivity and PLC identity Communication driver setup (Ethernet/IP) for RSLogix

Upload/download logic, modify ladder diagram, go online

(Optional) Packet capture to see ICS traffic

**_Air University: The Intellectual and Leadership Center of the Air Force Aim High ... Fly-Fight-Win_**

32

## Slide 33

## **What is Ladder Logic?**

**_The AFIT of Today is the Air Force of Tomorrow._**

- Ladder Logic is the only language supported by the MicroLogix 1100.

- Visual, circuit-like programming language designed for reliability and uptime.

- If you come from C++ or Python: it will feel alien.

- If you’ve used AND/OR gates or FPGAs: it’ll feel familiar.

- Main subroutine (LAD 2) runs in an infinite loop — designed to run 24/7.

**_Air University: The Intellectual and Leadership Center of the Air Force Aim High ... Fly-Fight-Win_**

33

## Slide 34

## **Anatomy of a Ladder Program**

**_The AFIT of Today is the Air Force of Tomorrow._**

- Ladders = Subroutines or files (e.g., LAD 2)

- Rungs = Think of them like circuits

- Logic flow: Left → Right, Top → Bottom

- Input logic (left side) controls outputs (right side)

- Logic "flows" across the rung like electricity:

   - Series (AND): All must be true

   - Parallel (OR): One path must be true

**_Air University: The Intellectual and Leadership Center of the Air Force Aim High ... Fly-Fight-Win_**

34

## Slide 35

## **Anatomy of a Ladder Program**

#### **_The AFIT of Today is the Air Force of Tomorrow._**

**_Air University: The Intellectual and Leadership Center of the Air Force Aim High ... Fly-Fight-Win_**

35

## Slide 36

## **Ladders**

**_The AFIT of Today is the Air Force of Tomorrow._**

**_Air University: The Intellectual and Leadership Center of the Air Force Aim High ... Fly-Fight-Win_**

36

## Slide 37

## **Rungs**

#### **_The AFIT of Today is the Air Force of Tomorrow._**

**_Air University: The Intellectual and Leadership Center of the Air Force Aim High ... Fly-Fight-Win_**

37

## Slide 38

## **PLC Variables – Data Files**

**_The AFIT of Today is the Air Force of Tomorrow._**

>  Data stored in typed files:

>  Inputs: I:0/3, Outputs: O:0/2, Binary: B3:1/0, Integer: N7:0

>  Format:

>  I:0/3 → Input file 0, bit 3

>  B3:1/5 → Binary file 3, row 1, bit 5 Type File Access Example Input I Read-only I:0/3 Output O Write-only O:0/2 Binary B3 R/W B3:1/0 Integer N7 R/W N7:0

**_Air University: The Intellectual and Leadership Center of the Air Force Aim High ... Fly-Fight-Win_**

38

## Slide 39

## **PLC Variables – Data Files**

#### **_The AFIT of Today is the Air Force of Tomorrow._**

**_Air University: The Intellectual and Leadership Center of the Air Force Aim High ... Fly-Fight-Win_**

39

## Slide 40

## **Instruction Types and Flow**

**_The AFIT of Today is the Air Force of Tomorrow._**

- Examine If Closed (XIC) – True if input is HIGH (e.g., I:0/3)

- Examine If Open (XIO) – True if input is LOW (inverted logic)

- Output Energize (OTE) – Turns on an output if rung is true

- JSR – Jump to Subroutine (e.g., call LAD 4, 5, or 6)

**_Air University: The Intellectual and Leadership Center of the Air Force Aim High ... Fly-Fight-Win_**

40

## Slide 41

**_The AFIT of Today is the Air Force of Tomorrow._**

# <u>Exercise 1 – Familiarization</u>

**_Air University: The Intellectual and Leadership Center of the Air Force Aim High ... Fly-Fight-Win_**

41

## Slide 42

**_The AFIT of Today is the Air Force of Tomorrow._**

# <u>Exercise 2 – Door Simulation Attacks</u>

**_Air University: The Intellectual and Leadership Center of the Air Force Aim High ... Fly-Fight-Win_**

42

## Slide 43

**_The AFIT of Today is the Air Force of Tomorrow._**

# <u>Exercise 3 – Fluid Tank Simulation Attacks</u>

**_Air University: The Intellectual and Leadership Center of the Air Force Aim High ... Fly-Fight-Win_**

43

## Slide 44

## **Shodan & ICS Exposure**

**_The AFIT of Today is the Air Force of Tomorrow._**

**_Air University: The Intellectual and Leadership Center of the Air Force Aim High ... Fly-Fight-Win_**

44

## Slide 45

**_The AFIT of Today is the Air Force of Tomorrow._**

# <u>Exercise 4 – Custom Exploit Development</u>

**_Air University: The Intellectual and Leadership Center of the Air Force Aim High ... Fly-Fight-Win_**

45

## Slide 46

## **Questions**

**_The AFIT of Today is the Air Force of Tomorrow._**

**_Air University: The Intellectual and Leadership Center of the Air Force Aim High ... Fly-Fight-Win_**

46
