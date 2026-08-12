---
title: "A Closer Look at the Gaps in the Grid New Vulnerabilities and Exploits Affecting Solar Power Systems"
speakers: ["Daniel dos Santos", "Francesco La Spina", "Stanislav Dashevskyi"]
conference: "Black Hat"
conference_full: "Black Hat ASIA 2025"
edition: "ASIA"
year: 2025
source_pdf: "Black Hat Asia 2025 Slides/Daniel dos Santos & Francesco La Spina & Stanislav Dashevskyi_A Closer Look at the Gaps in the Grid New Vulnerabilities and Exploits Affecting Solar Power Systems.pdf"
pages: 45
sha256: "01bf829cb3c8ba526603b4db0b6fd3a42a1197183406193060417b3e55c37fcc"
text_chars: 25633
ocr_pages: 7
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:04:03Z"
---
# A Closer Look at the Gaps in the Grid New Vulnerabilities and Exploits Affecting Solar Power Systems

**Speakers:** Daniel dos Santos, Francesco La Spina, Stanislav Dashevskyi  
**Conference:** Black Hat ASIA 2025  
**Source:** `Black Hat Asia 2025 Slides/Daniel dos Santos & Francesco La Spina & Stanislav Dashevskyi_A Closer Look at the Gaps in the Grid New Vulnerabilities and Exploits Affecting Solar Power Systems.pdf` (45 pages)

## Slide 1

A Closer Look at the Gaps in the Grid: New Vulnerabilities and Exploits Affecting Solar Power Systems

<u>Daniel dos Santos, Francesco La Spina, Stanislav Dashevskyi</u> Forescout Technologies

#BHAS @BlackHatEvents

## Slide 2

# **Who we are**

### **Daniel dos Santos**

### **Francesco La Spina**

#BHAS @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
blackhat Who wea re_ A ~
ASIA 2025
—
>
s FFORESCOUT.
atl Li. “oo 4
Daniel dos Santos LJ Francesco La Spina
Vulnerability Research Threat Reports
Focus on vulnerabilities against managed and Manual and automatic analysis of malware
unmanaged devices (IT/loT/lOMT/OT) samples collected via customer telemetry and
200+ vulnerabilities discovered in last 5 years other sources
```

## Slide 3

## Part 1: Motivation and Background

#BHAS @BlackHatEvents

## Slide 4

# **Why analyze solar power systems?**

Image sources: <u>https://en.wikipedia.org/wiki/Growth_of_photovoltaics https://www.ief.org/news/the-remarkable-rise-of-solar-power https://www.iea.org/news/how-solar-energy-could-be-the-largest-source-of-electricity-by-mid-century</u>

#BHAS @BlackHatEvents

## Slide 5

# **Overview of solar power systems**

- Solar PV panels generate DC power, which is converted to AC by **inverters**

- These inverters are **grid-connected** **_and_ cloud-connected IoT devices**

   - Enable remote monitoring and management

   - • Sometimes require an extra dongle / data logger

- Large **attack surface**

   - Inverters (comm dongles) are not supposed to be accessible directly via the internet

   - However, they are managed via the **vendor’s cloud, web apps and mobile apps**

MQTT HTTP
Mobile
app
Manufacturer
Solar  User
Comms cloud
Panels
dongle
Web
Modbus
app
Legend
Inverter Power  Network
Serial
Grid
Electric

- Lots of other components we don’t include in this talk: batteries, EV chargers, etc.

#BHAS @BlackHatEvents

## Slide 6

# **Example 1: Growatt architecture and app**

#BHAS @BlackHatEvents

Image source: <u>https://watts247.com/product/2-x-spf-3000tl-lvm-24p/</u>

## Slide 7

# **Example 2: Sungrow iSolarCloud**

#BHAS @BlackHatEvents

Image source: <u>http://base.isolarcloud.com:8181/docs/a1-0/d3.md</u>

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pisek hat
ASIA 2025
Image source:
sharp001 Gb
&
Real-time Power Today Yield Today Revenue Tree
1.424 220.8 209.7 11.415
MW kWh CNY trees
Installed Powe Total Yield Total Revenue
10.759GWp
44,745.325GWh
385,658.22Billion CNY
Accumulated Equivalent Trees
2.326Billion Trees
Yield Trend Month Yoon Today Plant PR Plant Equivalent Using Hours
ix 50 | Today Yield(kWh P MW. 1 Year Year
1906240466
LS A
€ ) ORA1912020001895335 A1904120009895B25
~ 150 0.9
A190412000989t5 LORA191202000189Fs5
100 0.6
A1906240466 A19091852038525
50
dq@w} Customer... '725062189s ZCB20191122
0
```

## Slide 8

# **Example 2: Sungrow iSolarCloud App**

#BHAS @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
\
2)
ASIA 2025
blackhat Example 2: SungrowiSolarCloud
»)
02:35 8 Fl 97% 02:41 B S| 95%
MORE < BACK
SETTINGS
System Parameters
Operation Parameters
Firmware Update
Power Regulation Parameters
Modify Password
Protection Parameters
About
Communication Parameters
Home Run Informatior Records
```

## Slide 9

# **Example 2: Sungrow WiNet-S dongle**

- Remember that they should not be accessible?

   - 2,600 with exposed HTTP server on Shodan

   - Thousands more similarly exposed from other manufacturers

   - • **Millions more managed via apps/clouds**

Image source: <u>https://www.vpsolar.com/en/product/sungrow-sg-2-0-2-5-3-0-rs-s-1-mppt/</u> Shodan query: https://www.shodan.io/search?query=http.favicon.hash%3A792201344

#BHAS @BlackHatEvents

## Slide 10

# **Solar power deployments**

- Three types of deployments

   - **Residential** : 5-15 kW, small rooftop

   - **Commercial** : >100 kW, large rooftop

   - **Utility** : >1 MW, solar parks/farms owned by utilities

- Most installations are residential but most power comes from utilities

   - Varies per country, but **usually >90% inverters are residential/commercial, while >50% of power is from utilities**

   - Utility deployments are often different, with large battery systems and less cloud connection

- Commercial deployments are growing and an interesting attack surface

   - Not very different from residential in terms of security but more power

   - Chart: distribution of 1,700 inverters seen on customer networks

Solar inverters by sector
Retail
Technology Entertainment
3%
1% 1%
Healthcare
4%
Government
22%
Services
12%
Financial
15%
Manufacturing
21%
Education
21% #BHAS @BlackHatEvents

## Slide 11

# **Previous vulnerabilities**

#### CVEs by CVSS score

- Cataloged **93 previous vulnerabilities affecting 34 vendors**

   - CVEs since 2012, average of 10/year for the past 3 years

   - 80% high or critical CVSS

   - Most cases affected solar monitoring/cloud products

   - Relatively few issues found directly on the inverters

- Six vulnerabilities **regularly exploited by botnets since 2022**

Product CVEs
CVE-2022-29303
CONTEC  CVE-2022-40881
SolarView CVE-2023-23333
CVE-2023-29919
APsytems  CVE-2023-28343
Altenergy CVE-2024-11305

Low
Medium
1%
19%
Critical
39%
High
41%

Affected components
Firewall
App
2%
6%
Solar monitor
Inverter
38%
15%
Gateway
14%
Cloud
25%

#BHAS @BlackHatEvents

CVE catalog extended data from <u>https://dersec.io/wp-content/uploads/2024/11/DERSec_Solar_Vulnerability_Summary_11-15-24.pdf</u>

## Slide 12

# **Known incidents**

- **Reports of incidents since 2019**

   - **US 2019:** Repeated denial of service on a firewall caused loss of visibility over 500MW PV generation

   - **Romania 2023** : Installer credentials used to disable safety setting on inverter that decreases output during low grid demand

- **Three relevant issues in 2024**

   - **Lithuania** : Pro-Russian hacktivists hijacked inverters in 22 organizations, including 2 hospitals via iSolarCloud management

   - **Japan** : 800 CONTEC monitoring devices hijacked by botnets

   - **US** : Flax Typhoon APT building botnets used to proxy further attacks. Exploited CVEs include two on CONTEC

- **No incidents directly targeting power generation** , but

   - FBI warned in a Private Industry Notification of the risk in July 2024

   - **Is it possible to affect the power grid?**

#BHAS @BlackHatEvents

Image source: <u>https://cyble.com/blog/photovoltaic-plants-pv-facing-risk-of-cyberattack/</u>

## Slide 13

# **Potential impacts on the grid**

- **AC power grid operates at a certain frequency**

- Grid stability depends on real-time **balance between power generation and demand** to keep that frequency (50 or 60Hz)

- Increased/decreased generation or demand without the other side keeping up impacts the frequency

- Too fast and too wild swings in frequency lead to emergency measures, such as load shedding

### • **Several grid disturbances worldwide due to solar power faults**

- Blue Cut Fire (California, 2016) – ~1.2 GW

- Canyon 2 Fire (California, 2017) – ~900 MW

- Odessa Disturbance (Texas, 2021) – ~1.1 GW

- Sri Lanka, 2025 – ~1.2 GW

- A disturbance does not mean a blackout – different grids have different levels of emergency capacity for frequency control

- These were not cyber, but natural phenomena (fire, animals, others) affecting power output or transmission

#BHAS @BlackHatEvents

Image source: <u>https://www.nerc.com/pa/rrm/ea/Documents/1200_MW_Fault_Induced_Solar_Photovoltaic_Resource_Interruption_Final.pdf</u>

## Slide 14

# **Further risk: supply chain considerations**

- Due to this potential impact, there’s now a focus on the origin and security of these devices

- Countries are starting to ban the sale or remote management of devices from certain countries

   - It’s not just about cyberattacks but remote control from foreign manufacturers (Deye case in US, 2024)

- 53% of inverter manufacturers are based in China, 14% in India, 5% in the US, remaining 28% throughout the world

100%
90%
80%
70%
60%
50%
40%
30%
20%
10%
0%

Distribution of solar power system vendors per country (top 5)

Inverters Storage systems Monitoring systems China India US Germany Italy Others

- Somewhat similar for other components

- 9 of 10 largest manufacturers are based in China, 1 in Germany.

Manufacturer data source: https://www.enfsolar.com/ Image sources: <u>https://www.lrt.lt/en/news-in-english/19/2411602/lithuania-passes-law-to-block-chinese-access-to-solar-and-wind-farm-systems</u> and <u>https://www.ft.com/content/534eef36-d9ad-4a03-afa1-f87ab03a9b18</u>

#BHAS @BlackHatEvents

## Slide 15

# **Research methodology**

- **Research questions**

   - Can we find an exploit chain from cloud to inverters that allows to take over a fleet of devices?

   - Are there other relevant vulnerabilities on these ecosystems?

- **Target selection**

   - 6 of top 10 vendors

   - Sungrow: ~740 GW worldwide

   - Growatt: ~300 GW worldwide

   - SMA: ~130 GW worldwide

- **Research strategy**

   - Cloud analysis using demo/test account

   - Mobile/web app analysis

   - Inverter/dongle analysis in one case

|**Vendor**|**Market share**|**Selected for**
**analysis?**|**Summary Results**|
|---|---|---|---|
|**Huawei**|29%|Yes|No issues found in limited
analysis|
|**Sungrow**|23%|Yes|Possible takeover of devices
and data leak|
|**Ginlong Solis**|8%|Yes|No issues found in limited
analysis|
|**Growatt**|6%|Yes|Possible takeover of accounts
and devices and data leak|
|**GoodWe**|5%|Yes|No issues found in limited
analysis|
|**SMA**|3%|Yes|Remote Code Execution on the
cloudplatform|
|**Power Electronics**|3%|No|N/A|
|**SofarSolar**|3%|No|N/A|
|**Sineng**|3%|No|N/A|
|**Aiswei**|3%|No|N/A|
|**Others**|14%|No|N/A|

#BHAS @BlackHatEvents

Market share source: <u>https://www.statista.com/statistics/1003705/global-pv-inverter-market-share-shipments/</u>

## Slide 16

## Part 2: Our Findings

#BHAS @BlackHatEvents

## Slide 17

# **Overview of findings**

46 vulnerabilities in three vendors!

- SMA Solar Technology

- Growatt

- Sungrow

To fully exploitable RCE

**Two exploitable RCEs and account takeover**

#BHAS @BlackHatEvents

## Slide 18

# **Vulnerabilities in SMA**

**SMA Solar Technology** is a German solar energy equipment supplier founded in 1981. It is **the largest Europe-based solar technology company** by revenue

- **RCE** on their cloud portal (sunnyportal.com) through **unrestricted file upload (** CVE-2025-0731 **)** -> unprivileged user

- **We uploaded an aspx file** instead of a plant picture **through a demo account**

- Potential control of an inverter fleet?

#BHAS @BlackHatEvents

## Slide 19

# **Vulnerabilities in Growatt**

**Growatt** is a Chinese manufacturer of PV inverters founded in 2011 and is the global No.1 residential inverter supplier

- We found a lot of **Insecure Direct Object References (IDOR)** in Shine Server!

- 2 x Stored XSS (also through IDORs)

- Missing authentication/broken access control issues led to **data leakage** and **account takeover**

- Potential control of a fleet?

#BHAS @BlackHatEvents

## Slide 20

# **How to take control of inverters?**

- **The first way and more direct** is by taking over accounts because of broken access control issues

- **The second way** is by injecting JavaScript in user profiles through an IDOR and potentially getting credentials and performing arbitrary operations

- In all cases, **we can guess valid usernames by exploiting other exposed APIs** or by obtaining thousands of them from the vendor’s legitimate "customer cases" page

#BHAS @BlackHatEvents

## Slide 21

# **Account takeover**

#BHAS @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
biSekhat Account takeoyer~
ASIA 2025
Activities @ Emulator + okt 9 15:42
proton.me,
Proton Mail needs your permission to enable desktop notifications.
vegkropo
Del Proton Mail i Q Search messages sagitbeetnme OY
342 OA
New message Inbox t
~ lad Hasfile =)
a ROWATT
Upgrade to use Proton Mail with Apple Mail, Outlook or Thunderbird G Upgrade x
=) Drafts
l
7 Sent
Afghanistan
Starred g =
MikeScot
MikeScott
123456
Remember password
MikeScott Mikescott
No messages found qwerty u
Seems like you are all caught up for now asdf g h j k
@ zxevboam
7123 , ©
```

## Slide 22

# **Hijack smart devices and E/V chargers**

- **Growatt app allows users to add and manage other smart devices**

- We could exploit several IDORs to realize potential “Halloween” scenarios:

   - E/V chargers stop charging

   - Thermostats act weird

   - Smart lightbulbs become too smart and swear in Morse code

   -

- …

#BHAS @BlackHatEvents

## Slide 23

# **Vulnerabilities in Sungrow**

**Sungrow** is a Chinese manufacturer of PV inverters founded in 1997 and is recognized as the world's No. 1 on PV inverter shipments

- Again **, many** … **many IDORs**

- Hardcoded credentials for MQTT

- Weak encryption in the mobile app communication

- Unsigned firmware update

- 4x **Buffer overflow** vulnerabilities in the inverter connection Dongle (WiNet-S), **one led to RCE**

- Potential control of a fleet?

#BHAS @BlackHatEvents

## Slide 24

# **How to take control of inverters?**

- Inverter dongles communicate with the cloud via MQTT to receive commands and send telemetry

- A dongle subscribes to topics that contain its serial number (S/N) in the path.

**MQTT topic: cloud/device/cmd/<S/N>/**

Subscribes
Sungrow cloud (MQTT Broker )
Communication
Solar Panel
Solar Panel
dongle
Communication
Power grid
dongle
Modbus
Inverter
Inverter

#BHAS @BlackHatEvents

## Slide 25

# **Exploit chain**

1. Harvest serial numbers via IDORs

2. Use the MQTT hard-coded credentials to publish crafted messages to the dongles

to publish crafted messages to the
dongles
Attacker
3. Via the published messages, exploit an
RCE on the dongles to gain control of
inverters MQTT
Sungrow cloud (MQTT Broker)
Solar Panel Communication
Solar Panel
dongle
Communication
Power grid
dongle
Inverter …
Inverter
#BHAS @BlackHatEvents

## Slide 26

# **Harvesting serial numbers**

- The first step is to get some WiNet device serial numbers

- We have multiple ways to get S/N by exploiting several IDORs

- Example:

   1. With _/v1/powerStationService/getPowerStationInfo_ , we can query a huge list of Power Station IDs (IDs are predictable)

   2. With another IDOR we can get dongle S/N by Power Station IDs:

**API model CVE vulnerable to IDOR CVE-2024-50685** powerStationService **CVE-2024-50693** userService

**CVE-2024-50689** orgService **CVE-2024-50686** commonService **CVE-2024-50687** devService

- _/v1/commonService/getSecondDataAbilitySnInfoByPsId_

#BHAS @BlackHatEvents

## Slide 27

# **Hard-coded credentials**

- The second step is to send crafted messages via MQTT…

- **The WiNet’s module firmware** (the communication dongle) **contains hardcoded MQTT credentials** (CVE-2024-50692) **that allow attackers to send messages to arbitrary dongles** via the corresponding MQTT broker

- It can be chained with another vulnerability to reach arbitrary code execution…

#BHAS @BlackHatEvents

## Slide 28

# **Buffer overflows**

- **We found four buffer overflow vulnerabilities** in the latest version of WiNet firmware.

- **These vulnerabilities are related to parsing incoming MQTT messages** and can be triggered by anyone via the MQTT

- **We decided to exploit a stack overflow in the handler function** for the “settime” command (CVE-2024-50694)

#BHAS @BlackHatEvents

## Slide 29

# **Attack via MQTT**

- We know that the WiNet dongle can receive commands from the cloud through MQTT

- Since the credentials are hard-coded, an attacker can trigger the buffer overflow with any MQTT client

- Attackers can target arbitray dongles, because they know S/Ns

Exploit payload

So far “so good”… what about the exploit?

#BHAS @BlackHatEvents

## Slide 30

# **Tensilica Xtensa Architecture**

- Even if the buffer-overflow is a text-book example…the architecture is not at all

- The WiNet-S dongle runs a modified version of FreeRTOS on an ESP32 SoC (manufactured by Espressif) with **Tensilica Xtensa architecture**

- Unique challenges…very few exploitation techniques are publicly discussed (a few research from Philipp Promeuschel and Carel van Rooyen)

#BHAS @BlackHatEvents

## Slide 31

# **Challenges**

- This architecture uses a ” **sliding register window** ”: there are only 16 logical registers in the CPU

- **The calling convention includes rotating the register window**

- Unlike an x86 architecture, the **return address** the attacker wants to overwrite **is stored in a specific register** , not the stack

- Mechanisms to overcome this limitation include **the overflow exception, which writes registers to the stack** , and the **underflow exception, which restores them**

#BHAS @BlackHatEvents

## Slide 32

# **Windowed registers in a nutshell**

#BHAS @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
pisekhat Windowed registefs.ina nutshell
ASIA 2025
Call stack
amsiae 16 Logical visible registers (out of 64 physical)
Func #0 « *
aO al/a2)|a3|a4/a5|a6/ a7) a8 | a9 ai0jal1al2at3jal4a15
Rotates 8 registers forward
a0\/al|a2\a3|}a4\a5\ a6/a7 a0 al|a2|a3|a4|a5/a6/a7
Preserved registers Registers visible to the Callee function
Func #2 | call8? Overflow Exception >
aO|}ailj|a2 a3\a4\a5/a6\a7 a0 al|a2|a3/a4)|a5| a6 | a7
a”,
| | ¥ ¥ | ¥ ¥ | » Spill registers to a predefined stack area
¥ (Base Save Area)
Rotates back
a0 Function return address | Q@1 | Stack pointer
```

## Slide 33

# **Exploitation Strategy**

- Our only primitive is an out-of-bounds write into the stack, the exploit requires us to overwrite registers stored on the stack, **abusing overflow exceptions**

- The prerequisite is that there is a reachable area on the stack (e.g. the Base Save Area) that has registers stored. **Satisfied because in FreeRTOS a context switch always spills the entire register files into the stack**

- By overwriting the stack with the right amount of bytes **we can overwrite a stored a0 register and return to an arbitrary address**

- **The stack on the ESP32 is non-executable!** Needs to write in IRAM through a **memcpy() gadget**

#BHAS @BlackHatEvents

## Slide 34

# **Reaching the return value**

- **Overwriting the Base Save Area** at the top of the vulnerable function's stack frame **will affect the register values of the vulnerable function's caller's caller** (two functions up the call chain)

- **Control flow must return three times** to trigger the overwritten return address a0

- We must carefully inspect the code leading through these return instructions to **ensure the malicious stack frame will not cause a crash**

Cannot be an invalid address

#BHAS @BlackHatEvents

## Slide 35

# **The stack structure**

- To create our stack frames, **we will need to calculate addresses on the stack** relative to the location of the overflown buffer

- **The stack is dynamically allocated** per RTOS task at startup

- **We found that a specific base address is the most common** for the MQTT task's stack

#BHAS @BlackHatEvents

## Slide 36

# **The final payload**

|“A” is the address of|
|---|
|the overflown buffer|

#BHAS @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
blackhat The final payload’ a fo
ASIA 2025
| Offset From
| Overflown Buffer | Meaning Additional comments
tt packet ~a@ cane
eee | nadget address A’ is the address of
= | : the overflown buffer
parse_mgtt_packet “al A + @xbc '
shellcode “al “A + @x9c”
imaginary al “A + @x106° This value must point to a valid
location, as it may be used to determine
the location of the shellcode's ESA.
location the copy operation.
memcpy gadget al” “A + @x7c”
memcpy gadget a2- target IRAM This is the address where the shellcode
location will be copied.
|
|
|
|
|
|
|
memcpy_gadget “aQ- target IRAM This is the address to return after
|
|
memcpy gadget a3” shellcode
source location This should be the source address for the |
copy. We can use a static address pointing|
to an offset in the MQTT packet where we |
placed the shellcode.
```

## Slide 37

## Part 3: Outlook and Conclusions

#BHAS @BlackHatEvents

## Slide 38

# **Grid destabilization**

- So we can take over a lot of inverters, now what?

   - Impact on grid depends on how much generation capacity can be controlled, how fast can the attack happen and how much the grid has in emergency capacity

- Many other studies have modeled grid impact based on “load-changing attacks”:

   - Increase demand or decrease generation at large scale via botnets

   - • Dvorkin and Garg, 2017; Dabrowski et al., 2017; Soltan et al.; 2018; Goerke et al., 2024; and others.

- Summary for European continental grid (ENTSO-E):

   - 3GW emergency capacity (“reference incident”)

   - **Below 49Hz mandatory load shedding**

   - **Control over 4.5GW needed to drop frequency below 49Hz**

   - That’s around 563,000 inverters (8kW/inverter average)

   - **Current solar capacity is ~270 GW, so need to control less than 2% of inverters** . Market led by Huawei, Sungrow and SMA

Image sources: <u>https://publications.sba-research.org/publications/201712%20-%20ADabrowski%20-%20Grid%20Shock.pdf and https://dl.acm.org/doi/10.1145/3632775.3661943</u>

#BHAS @BlackHatEvents

## Slide 39

# **Other scenarios**

- **Electricity has fluctuating prices based on generation and demand**

   - Remember the Romanian incident in 2023 where safety settings were disabled to continue high output?

- More complex attack scenarios may take advantage of that **for financial gain rather than to impact grid stability**

   - Think cybercriminal vs APT motivations

- A possible scenario is **demanding a ransom** from energy operators based on the threat of changing inverter settings or disabling them at critical times

   - The RCEs on inverters and allow attackers to disconnect them from manufacturer or other central management to keep persistent control

- **“Ransomware on inverters”** has also been discussed academically

#BHAS @BlackHatEvents

Image sources: <u>https://www.ionsolar.com/ion-solar-blog/energy-efficient-home-improvements-to-help-you-save-money and https://ieeexplore.ieee.org/abstract/document/10362822</u>

## Slide 40

# **Incident response**

- The worst-case scenario, where attackers create a “botnet” and disconnect devices from remote management would demand **coordinated incident response**

- There may be no way to stop the attack without **physically disconnecting the inverters**

   - Maybe a C&C server takedown, but that can take a long time and servers can be resilient

- Disconnecting devices **during the day may be harmful**

   - If you don’t know what is infected, disconnecting the “clean” devices will only harm generation capacity further

   - At night, utilities can prepare for the next day, knowing what the impacted generation capacity will be

- **Need for incident response plans** involving utilities, regulators and manufacturers

   - Maybe dedicated APIs that utilities can use to control devices in case of an attack?

#BHAS @BlackHatEvents

## Slide 41

# **Responsible disclosure**

- **Sungrow fixed all issues**

   - Very collaborative during the whole process

   - Calls to better understand the vulnerabilities

   - Asked us to test patches and provide recommendations

   - CISA involved for coordination

- **SMA fixed their issue on time**

   - Single issue on the website/infra, so no need to touch firmware

   - CERT@VDE involved for coordination

- **Growatt also fixed, but much less reactive**

   - Promised fixes by Feb 14, then implemented partially Feb 27 and finally done by March 13

   - They were known to leave other issues unfixed in previous research

   - CISA involved for coordination

- Overall, some vendors in this market seem to be just starting to pay attention to security

   - Similar to OT security a few years ago, but need this needs to go much faster than OT security adoption

#BHAS @BlackHatEvents

Image source: <u>https://www.enisa.europa.eu/topics/vulnerability-disclosure</u>

## Slide 42

# **Recommendations – users**

- **Residential and commercial users**

   - Change default passwords and credentials

   - Use role-based access control

   - Configure the recording of events in a log

   - Update software regularly

   - Backup system information

   - Disable unused features

   - Protect communication connections

- **Commercial and utility installations (in addition)**

   - Include security requirements into procurement considerations

- Conduct a risk assessment when setting up devices

- Ensure network visibility into solar power systems

- Segment these devices into their own sub-networks

- Monitor those network segments

Sources:

<u>https://nvlpubs.nist.gov/nistpubs/ir/2024/NIST.IR.8498.pdf https://pubs.naruc.org/pub/35247A70-0C45-9652-C6D9-99A77C87200F</u>

#BHAS @BlackHatEvents

## Slide 43

# **Recommendations – manufacturers**

- **Keep in mind** : Inverters are part of critical infrastructure!

   - Security requirements should be higher than general use IoT

- **Development**

   - Devices: holistic security architecture including secure boot, binary hardening, anti-exploitation features, permission separation etc

   - Applications: proper authorization checks on web applications, mobile applications and cloud backends

- **Testing**

   - Regular penetration testing on applications and devices

   - Consider bug bounty programs

- **Monitoring**

   - Web Application Firewalls

   - Remember that a WAF does not protect against logical flaws

Image sources: <u>https://nvlpubs.nist.gov/nistpubs/ir/2020/NIST.IR.8259.pdf https://checkmarx.com/glossary/a-secure-sdlc-with-static-source-code-analysis-tools/</u>

#BHAS @BlackHatEvents

## Slide 44

# **Takeaways**

- Solar power is growing massively and so is the attack surface

- Several components have vulnerabilities and they are starting to get targeted by opportunistic attackers

- There is potential for more targeted attacks that impact grid stability or utilities directly

- Risk mitigation depends on actions from users, installers, utilities, regulators and others

- The time to fix these problems is now!

- Read the full report on forescout.com/research

#BHAS @BlackHatEvents

## Slide 45

Thank you! **Questions?** <u>daniel.dossantos@forescout.com francesco.laspina@forescout.com</u>

#BHAS @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
- blsekhat
ASIA 2025
Thank you!
Questions?
daniel.dossantos@forescout.com
francesco.laspina@forescout.com
#BHAS @BlackHatEvents
```
