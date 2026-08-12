---
title: "E-Trojans Ransomware, Tracking, DoS, and Data Leaks on Xiaomi Electric Scooters"
speakers: ["Marco Casagrande", "Daniele Antonioli"]
conference: "Black Hat"
conference_full: "Black Hat USA 2025"
edition: "USA"
year: 2025
source_pdf: "BlackHat_USA_2025_Slides/Marco Casagrande&Daniele Antonioli_E-Trojans Ransomware, Tracking, DoS, and Data Leaks on Xiaomi Electric Scooters_WP.pdf"
pages: 16
sha256: "e169463b67984c886e6d8052df8ed6219d4cb6949b09f2397bed828da5ccfad8"
text_chars: 78205
ocr_pages: 0
has_ocr: false
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2"
converted_at: "2026-08-11T22:57:33Z"
---
# E-Trojans Ransomware, Tracking, DoS, and Data Leaks on Xiaomi Electric Scooters

**Speakers:** Marco Casagrande, Daniele Antonioli  
**Conference:** Black Hat USA 2025  
**Source:** `BlackHat_USA_2025_Slides/Marco Casagrande&Daniele Antonioli_E-Trojans Ransomware, Tracking, DoS, and Data Leaks on Xiaomi Electric Scooters_WP.pdf` (16 pages)


## Slide 1

# **E-Trojans: Ransomware, Tracking, DoS, and Data Leaks on Battery-powered Embedded Systems**

Marco Casagrande _EURECOM_

_marco.casagrande@eurecom.fr_

Riccardo Cestaro

_University of Padova_

_riccardo.cestaro@outlook.it_

Eleonora Losiouk _University of Padova_

_eleonora.losiouk@unipd.it_

Mauro Conti Daniele Antonioli _University of Padova EURECOM mauro.conti@unipd.it daniele.antonioli@eurecom.fr_

## **Abstract**

Battery-powered embedded systems (BESs), such as laptops, smartphones, e-scooters, and drones, have become ubiquitous. Their internals (hardware and firmware) include a battery management system (BMS), a radio interface, and a motor controller. Despite their associated risk, there is little research on BES internal attack surfaces. For example, what can be accomplished by a (remote) attacker with access to a BMS needs to be clarified. This lack of understanding is primarily due to the challenges of analyzing internal attack surfaces, as these components are vendor-specific, proprietary, and undocumented.

To fill this gap, we present the first security and privacy assessment of e-scooters internals. We cover Xiaomi M365 (2016) and ES3 (2023) e-scooters and their interactions with Mi Home (their companion app). We extensively reverseengineer (RE) their internals and uncover four critical design vulnerabilities, including a remote code execution issue with their BMS. Based on our RE findings, we develop E-Trojans, four novel attacks targeting BES internals. The attacks can be conducted remotely (via a malicious app) or in wireless proximity (using a BLE device). They have a critical and widespread real-world impact as they violate the Xiaomi e- scooter ecosystem’s safety, security, availability, and privacy. For instance, one attack allows the extortion of money from a victim via a BMS undervoltage battery ransomware. A second one enables user tracking by fingerprinting the BES internals. With extra RE efforts, the attacks can be ported to other BES featuring similar vulnerabilities.

We implement our attacks and RE findings in E-Trojans, a modular and low-cost toolkit to test BES internals. Our toolkit binary patches BMS firmware by adding malicious capabilities, such as disabling firmware updates, controlling internal buses, and turning off safety thresholds. It also implements our undervoltage battery ransomware in an Android app with a working backend. We successfully test our four attacks on M365 and ES3, empirically confirming their effectiveness and practicality. For example, our undervoltage battery ransomware deteriorates the M365 battery’s auton-

omy by 50% in three hours, and our user tracking generates a persistent fingerprint to track the user over BLE while also leaking sensitive data about the e-scooter. We propose four practical countermeasures to fix our attacks and improve the Xiaomi e-scooter ecosystem security and privacy.

## **1 Introduction**

_Battery-powered embedded systems (BESs)_ are an integral part of our society. They include electric cars, e-scooters, e-bikes, drones, smartphones, and laptops. Electric vehicles alone have a market size of USD 422.8 billion [68]. Meanwhile, e-scooters have a market of USD 37 billion and an estimated annual growth of 10% [52, 53]. These devices carry sensitive data and, if misused, can cause security, privacy, and safety issues. Thus, protecting BES against vulnerabilities and attacks is crucial. For instance, a recent attack on pagers leveraged compromised internal components to detonate explosives concealed within their batteries [17].

Real-world BESs have complex and proprietary internals, including hardware and firmware components. The internal typically consists of a microcontroller, running closed-source firmware, a rechargeable battery, and an electric motor. Moreover, they include a wireless communication interface such as Bluetooth Low Energy (BLE), and internal buses including Universal Asynchronous Receiver-Transmitter (UART) and Inter-Integrated Circuit (I2C). BESs are operated by users and can be controlled using a smart device, e.g., an e-scooter is ridden by the user and controlled via a mobile companion app.

BES internals are an attractive _attack surface_ that received limited attention from the research community. In automotive research, there are papers about the security of externally reachable electric control units (ECUs) [14] and controller area network (CAN) buses [35]. Internal attack surfaces have been explored in works such as [79], implementing authentication and encrypted communication on automotive bus systems.

Another popular class of BES is e-scooters. Most research

1

## Slide 2

on them focused on external attack surfaces, including proprietary protocols over BLE [12] or studying the privacy of e-scooter rental mobile apps [75]. Drone literature highlighted issues in physical layer [39] and communication protocols [9, 56], issues involving, among others, firmware updates and image transfer. Hence, the security of BES internals needs more research (refer to Section 2.1 for an extended motivation).

We fill this gap by presenting the first security and privacy assessment of the internal attack surface of _e-scooters_ . We focus on e-scooters from _Xiaomi_ and _Segway-Ninebot_ [21], two market leaders. Xiaomi has released seven e-scooters in the last seven years: M365, Pro, Pro 2, 1S, Essential, Mi 3 (ES3), and Mi 4. We target the _M365_ and _Mi 3 (ES3)_ models, as they cover two e-scooter generations (2016 – 2024) and are used daily by millions of people [66]. These users include people owning private e-scooters and those using rented Xiaomi e-scooters from services like Bird and Lime [6, 77]. Our analysis also covers _Mi Home_ , the Xiaomi e-scooter companion app available for Android [4] and iOS [5].

We uncover _four design vulnerabilities_ by reverseengineering (RE) the M365 and ES3 internals. The vulnerabilities include unsigned and unencrypted BMS (V1, V2) and unencrypted and unauthenticated UART/I2C communication (V3, V4). Being design flaws, they are effective on _any_ Xiaomi M365 or Mi 3 e-scooters and possibly other Xiaomi e-scooters. We also report novel RE findings, including the e-scooters’ hardware block diagram, firmware protections, and battery management details.

We propose **E-Trojans** , four novel attacks on BES internals, compromising the safety, security, privacy, and availability of the Xiaomi e-scooter ecosystem. The attacks exploit the vulnerabilities we found to achieve malicious goals, including (remote) code execution on the BMS. Among the attacks, we present the first _BES battery ransomware_ . The attack remotely infects the BMS and progressively and irreversibly destroys the e-scooter’s battery via undervoltage until the victim pays a ransom. We also showcase a novel _tracking attack_ that leverages immutable hardware identifiers within the e-scooter’s internals to track its rider.

The E-Trojans attacks are conducted _remotely_ via a malicious app installed on the victim’s phone, or in _wireless range_ of the e-scooter via a BLE device. We note that the attacks can be conducted on any BES device affected by similar vulnerabilities that we found on the Xiaomi e-scooters, like an EV, a drone, a smartphone, or a laptop.

We present E-Trojans, a toolkit implementing our attacks and RE findings with open-source software and cheap hardware. The toolkit contains a binary patcher to transform a stock battery controller firmware into a malicious one. The patcher includes ten capabilities, such as turning off firmware updates and safety-critical voltage protections. Our toolkit targets STM8 chips but can be extended to other ones, including the STM32 [71] family with low engineering effort. We

release the undervoltage battery ransomware proof of concept, including a modified e-scooter firmware, an Android ransom payment app, and a Django/MongoDB backend managing the payment.

We successfully tested the E-Trojans attacks in a realistic but controlled scenario against up-to-date M365 and ES3 e- scooters and report our experimental results. For instance, we were able to degrade the M365 battery’s autonomy by 50% in three hours using the undervoltage battery ransomware PoC and to track a user via unique e-scooter fingerprints broadcasted over BLE.

To fix the presented vulnerabilities and attacks, we propose _four countermeasures (C1–C4)_ . Our fixes add confidentiality and integrity guarantees for the battery controller firmware and protect the internal UART bus against spoofing and DoS. Moreover, they are _backward-compatible_ with the Xiaomi ecosystem, as they reuse cryptographic primitives already supported, and _low-cost_ because they add minimal overhead. We summarize our contributions as follows:

- We present a security and privacy analysis of Xiaomi e-scooters internals. We RE Xiaomi M365 and ES3 e- scooters internals and uncover four critical design vulnerabilities, including unsigned battery controller firmware enabling (remote) exploitation of millions of Xiaomi e-scooters.

- We develop E-Trojans, four novel attacks that can be deployed remotely or in proximity. The attacks include battery ransomware via undervoltage and user tracking via e-scooter internals.

- We release a toolkit implementing our attacks with opensource software and cheap hardware. The toolkit is usable to further RE the proprietary Xiaomi e-scooter ecosystem and to target other BESs.

- We empirically confirm that our four attacks are practical and stealthy by conducting them on M365 and ES3. We propose four effective and legacy-compliant countermeasures to fix the found vulnerabilities and attacks.

**Responsible Disclosure** . We followed standard practices for responsible disclosure by contacting Xiaomi and the affected vendors. We notified Xiaomi in November 2023 via their official HackerOne bug bounty program [82]. We uploaded and shared with them video demonstrations, PoCs, and instructions on how to reproduce the attacks. Xiaomi acknowledged our multiple reports, updated its CVSS severity score to Medium (5.8), and closed it as informative in March 2024. We disagreed with Xiaomi’s assessment and, to have our findings addressed, in April 2024 we contacted via email the manufacturers of the BMS chips we targeted: STMicroelectronics (ST) and Texas Instruments (TI). ST responded that our attacks do not raise any security concerns as they are physical. We contest their assessment as we conduct our

2

## Slide 3

attacks in wireless proximity or even remotely. TI did not respond.

**Availability** . We provide our toolkit and attack demos at redacted. For safety reasons, we redacted the code responsible for generating malicious BMS firmware, which took months of RE to develop. We also release a patched BCTRL firmware that blocks BMS firmware updates, preventing our attacks. The private repository will be open-sourced in the future.

**Ethics** . We conducted our experiments ethically: we tested our e-scooters and smartphones in a laboratory, and minimized safety risks during the undervoltage and overvoltage experiments.

## **2 Motivation and Threat Model**

In this section, we motivate our work and present our threat model.

## **2.1 Motivation**

BESs represent a diverse range of devices such as EVs, e- scooters, smartphones, drones, and laptops. They have a complex internal architecture that includes several subsystems, such as radio, motor, and battery management, and components, such as communication buses and battery monitors.

Vulnerabilities and attacks on BES internals have received limited attention from researchers. Prior works explored a rogue firmware update through physical access on a Tesla BMS [34] or discussed theoretical vulnerabilities in MacBook laptop batteries [43]. Compromising these devices can pose severe safety risks to users, such as destroying the battery or triggering fire hazards. It also endangers security by enabling DoS, firmware integrity, and spoofing attacks. Since BESs often collect sensitive data, including user identity and location, vulnerable devices could result in privacy leaks.

This work focuses on e-scooters, a pervasive class of BES. No prior study analyzed their internal attacks surface, while only a few looked at external threats. The researchers in [12] reverse-engineered and compromised the BLE proprietary communication protocols used by Xiaomi e-scooters and Mi Home. E-scooter’s security threats, such as DoS, physical attacks, and firmware vulnerabilities, have been highlighted by [33]. The authors of [10] performed a threat analysis on the Xiaomi M365 and reproduce known attacks on its authentication. Privacy issues have also been found in e-scooters’ apps [75] that shared user identity, location, and phone data with the manufacturer and third parties. Hence, further research is needed on the internal attack surface of an e-scooter, including its BMS and internal buses.

## **2.2 Threat Model**

**System Model** . Our system model follows the block diagram in Figure 1. It includes a user who owns a Xiaomi e-scooter

(BES) and a smartphone running Mi Home for Android or iOS. They paired Mi Home with the e-scooter and locked it with a password. The user runs the latest version of the BTS, DRV, BCTRL firmware, and Mi Home, and charges the e-scooter with the original Xiaomi charger. The Xiaomi ecosystem includes e-scooters owned by a user or rented from a fleet. Our model includes both personal and fleet e-scooters and we focus on their Xiaomi-specific features. We do not study features added by a fleet manager on top of the Xiaomi e-scooter, like a cellular module with a SIM card.

**Attacker Models** . We focus on protocol-level attacks and consider two related attacker models: (i) _proximity-based attacker_ who interacts with the e-scooter wirelessly over BLE (e.g., using a laptop in the BLE range with the e-scooter); and a (ii) _remote attacker_ who can connect to the e-scooter over the Internet through malware installed on a victim’s device (e.g., using a malicious Android app). Attacks at the implementation-level, including side channel and fault injection, are out of scope.

Our proximity-based and remote attacker models correspond to several real-world attack scenarios. For example, the proximity-based attacker can place a (cheap) BLE transmitter in a public location (e.g., a train station or a parking spot) to target e-scooters in transit, or attach it beneath an e-scooter, to attack nearby e-scooters as it moves. Similarly, the remote attacker can install a malicious app on a victim’s smartphone to attack their e-scooter, potentially performing timing attacks, such as triggering errors while the user is riding it.

**Attacker Goals** . The attacker wants to violate the _safety_ , _security_ , _privacy_ , and _availability_ of the e-scooter by exploiting V1, V2, V3, and V4 (i.e., architectural vulnerabilities we found in the internals). For instance, the adversary could try to extort money from the e-scooter’s rider via ransomware or follow their movements via a tracking attack. These two goals are _novel_ in the domain of e-scooters, leading to large-scale and critical impacts as they target the entire Xiaomi e-scooter ecosystem, affecting millions of users and devices.

**Attacker Capabilities** . The attacker’s knowledge covers the known details (Section 3.1) and the uncovered details and vulnerabilities (Sections 3.2 and 3.3). The attacker can reuse findings and tools from prior works [12, 45, 62]. For example, they can authenticate to e-scooters via BLE using the E-Spoofer toolkit [11]. The attacker cannot physically access the victim’s e-scooter, charger, and smartphone.

## **3 Xiaomi E-Scooters RE and Vulnerabilities**

We present prior and new details about Xiaomi e-scooter internals we found via RE. Then, we describe the four vulnerabilities we uncovered.

3

## Slide 4

BMS Board
V1 UART
V2 Batt Charger
BCTRL DRV Board
V3 V4
UART
I2C UART
BLE
Remote
Attacker
BLE
BMON BTS Board
Proximity
Attacker
BES

Figure 1: E-Scooter block diagram and attacker models. The green rectangle shows the e-scooter (BES) internals, such as the BMS, DRV, BTS, and UART communication bus. The blue rectangle (BMS) shows the components of the BMS board, i.e., a BCTRL and a BMON connected via I2C. We consider a proximity-based adversary in the BLE range of the e-scooter and a remote adversary who installed a rogue app on the victim’s smartphone.

## **3.1 Available RE Information**

**E-Scooter Block Diagram** . As shown in Figure 1, a Xiaomi e-scooter is composed of three undocumented and closedsource systems: _Bluetooth Low Energy (BTS)_ , _Driving (DRV)_ , and _Battery Management (BMS)_ . BTS provides low-power and reliable wireless communication, DRV controls the electric motor, and BMS manages the battery. Each system has a dedicated System-On-Chip (SoC) running closed-source firmware. The systems communicate using a proprietary protocol over a Universal Asynchronous Receiver-Transmitter (UART) bus. UART provides a serial, asynchronous, and fullduplex digital communication channel with TX/RX wires.

**Mi Home App** . The user interacts with a Xiaomi e-scooter via the _Mi Home_ application for Android [4] or iOS [5]. The e-scooter and the app communicate over BLE using a custom application-layer protocol studied in [12]. They discover each other using BLE scanning and advertising.

To connect and communicate with the e-scooter, the user logs in with their Xiaomi account on Mi Home and pairs the app and the e-scooter. Then, the paired devices connect whenever they are in the BLE range without requiring user interaction.

Mi Home offers valuable features for controlling the e- scooter. For example, it allows to set a password to lock the e-scooter, perform over-the-air (OTA) firmware updates, and monitor the e-scooter’s battery status.

**E-Scooter Internals** . There is limited information about Xiaomi e-scooters’ internals. In [12], the authors focus on external communications with Mi Home and do not discuss

internal components. Research on the Xiaomi 1S e-scooter reports that Xiaomi encrypts the BTS, DRV, and BMS firmware binaries using TEA with an encryption key that has been leaked. These binaries are also signed with ECDSA [8, 45] and contain a certificate chain with a public key for signature verification.

The BTS collects new firmware from Mi Home. When needed, it decrypts, verifies, and distributes them to the DRV and the BMS via the internal bus. The developers of the ScooterHacking Utility Android app [62, 65] reversed a Xiaomi firmware update protocol to enable flashing a modded DRV firmware on e-scooters running an old BTS version. However, there is no information about _recent_ BTS, DRV, and BMS firmware or internal communication protocols.

## **3.2 New RE Information**

Starting from the details presented in Section 3.1 and known information about the internals of the M365 [58], we RE the Mi 3 (ES3) [59] Xiaomi e-scooter and discuss the parts relevant to our attacks. Next, we summarize our findings.

**E-Scooter Internals** . We disassembled the M365 and ES3 to identify their SoCs and internal connections. As shown in Figure 2, we tore the lower deck of the e-scooter to access the DRV, BMS, and battery pack. We unscrewed the deck, removed the plastic wrapping and the protective polystyrene from the battery, and pulled out the BMS board. As shown in Figure 3, the BMS includes a _battery controller (BCTRL)_ and a _battery monitor (BMON)_ , located on opposite sides of the BMS board. We found that the M365 and ES3 share the same BCTRL and BMON chips.

The BCTRL is an STM8L151K6 chip [70] from ST and supports firmware updates [69]. We identified the VDD, SWIM, GND, and RST pins used for powering, programming, and resetting the BCTRL. We soldered them to an _ST-Link v2_ programmer for firmware extraction and debugging and found _no hardware debug (ST-Link) protection_ on the BCTRL. The BMON is a BQ76930 chip [30] from TI, configurable by the BCTRL. Unlike the BCTRL, the BMON does not support firmware updates or hardware debugging [31].

The BCTRL and BMON communicate using a proprietary protocol over I2C, a synchronous serial digital protocol running on two wires (SDA and SCL). The BCTRL (I2C master) controls the BMON (I2C slave). The I2C protocol lacks encryption and authentication.

**Firmware Signing and Encryption** . We gathered BTS, DRV, and BCTRL firmware binaries from the Mi Home app cache, the Xiaomi backend, and a public repository. We also connected to the BCTRL through the SWIM interface, which is used for programming and debugging, to dump its current firmware. Our firmware collection ranges from the M365 firmware released in 2019 to the most recent firmware for the ES3 released in 2024. We statically analyze them with Ghidra to study their encryption and signature verification.

4

## Slide 5

Figure 2: Disassembled M365 (left) and ES3 (right). We color-coded the boxes to visualize the DRV (orange), the BMS (blue), and the soldered ST-Link wires (fuchsia).

Figure 3: The BCTRL STM8 SoC (green) and BMON BQ73960 SoC (teal) found on opposite sides of the M365 BMON.

We discover that the BTS, DRV, and BCTRL firmware from M365 are _unencrypted_ and _unsigned_ , regardless of their version. Conversely, in the ES3, the BTS firmware is signed with ECDSA since v1.5.2, the DRV firmware is signed with ECDSA and encrypted with TEA since v0.1.7, and the BCTRL firmware is unprotected.

**Battery** . We got relevant M365 and ES3 battery details by physically inspecting them and reviewing public documentation. As summarized in Table 2, the e-scooters have similar lithium-ion (Li-Ion INR) batteries produced by SegwayNinebot. The batteries have 30 cells configured in 10 series of 3 parallel cells and support the same maximum and minimum voltage thresholds (i.e., 42V at 100% and 36V at 0%) and cell voltage (i.e., between 4.2V and 3.6V). The M365 battery has more capacity than the ES3 one (i.e., 7.80Ah/300Wh vs. 7.65Ah/275Wh).

**BMS** . We RE the e-scooter’s BMS by focusing on the unencrypted BCTRL firmware and the BMON datasheet. The BCTRL and BMON work together to ensure safe battery management. Our analysis focuses on three unsafe conditions that impact battery health and safety: undervoltage, which can lead to short circuits and permanent battery damage; overvoltage, which increases the risk of overheating, fire, and thermal runaway; and voltage imbalance between battery cells, which contributes to both undervoltage and overvoltage, accelerating

**Algorithm 1** BCTRL initialization and main loop logic.

|1:|initBCTRL(serial, fwver, cLBD)|
|---|---|
|2:
3:|initBMON(dUVT, cUVT, dOVT, cOVT)|
|4:|**loop**|
|5:|battcells = readBMON(volt, amp)|
|6:|battlevel = compBattlevel(battcells)|
|7:|**if**battcells.deltaVolt_>_=cLBD**then**|
|8:|sleepMode(True)|
|9:|loadBalancing(True)|
|10:|**end if**|
|11:|**if**battcells.minCellVolt_<_cUVT**then**|
|12:|sleepMode(True)|
|13:|**end if**|
|14:|**if**battcells.maxCellVolt_>_cOVT**then**|
|15:|sleepMode(True)|
|16:|**end if**|
|17:||
|18:|**while**(sleepMode and !readWakeUpFromUART())**do**|
|19:|**if**battcells.deltaVolt_>_=cLBD**then**|
|20:|loadBalancing(True)|
|21:|**end if**|
|22:|**end while**|
|23:|readFromUART()|
|24:|writeToUART()|
|25:|**end loop**|

### battery degradation.

The BMON measures battery parameters, such as voltage and temperature, reports fault conditions to the BCTRL, and stores thresholds that activate hardware protections. The undervoltage threshold can be set between 1580mV and 2750mV, while the overvoltage threshold can be set between 4200mV and 4700mV. We consider them critical and dangerous undervoltage thresholds, (cUVT = 1580mV and dUVT = 2750mV) and critical and dangerous overvoltage thresholds, (cOVT = 4700mV and dOVT = 4200mV).

The BCTRL is responsible for the battery’s health, processing data from the BMON and determining whether safety mechanisms should be triggered. It has write access to the BMON hardware protection registers, allowing it to modify safety thresholds and disable safety mechanisms. The BCTRL also manages load balancing, ensuring voltage is evenly distributed among individual battery cells by defining the critical load balancing delta (cLBD = 800mV), which sets the maximum allowable voltage difference between any two cells. Additionally, the BCTRL handles communication with other e-scooter components, such as BTS and the DRV, and powers them off when the battery enters an unsafe state.

**BCTRL Firmware** . We RE the BCTRL firmware _initialization_ and _main loop_ by decompiling its stripped binary and debugging it with an ST-Link device connected to the SWIM interface. As shown in Algorithm 1, during initialization, the BCTRL 1) loads its configuration parameters, including serial number, firmware version, and load balancing deltas; and

5

## Slide 6

2) configures the BMON over I2C by writing into related registers, including setting the undervoltage and overvoltage thresholds.

Then, the BCTRL firmware enters a main loop where it: 5) reads the battery cells’ voltage and current values from special BMON read-only registers; 6) computes the current battery level (percentage); 7) checks voltage levels against cLBD, 9) enables load balancing if needed, and 11) checks undervoltage against cUVT and 14) overvoltage against cOVT.

If a critical undervoltage, overvoltage, or balancing check fails, the BCTRL sends error messages that power off the BTS and the DRV, 18) enters sleep mode, 20) and performs load balancing. During the main loop, the BCTRL 23) reads from and 24) writes to the UART bus to communicate with the BTS and the DRV.

**UART Bus** . We RE the proprietary UART protocol used by the BCTRL, DRV, and BTS. The BCTRL utilizes a USART1 peripheral mapped to RAM (address 0x5230). A UART packet consists of several fields, including the sender and receiver (e.g., 0x22 corresponds to BCTRL), packet type (e.g., read or write), command to execute, payload, and CRC.

**I2C Bus** . We RE the proprietary I2C protocol used by BCTRL and BMON. The BCTRL can read and write the BMON registers via I2C. For example, we can set dUVT by writing into UV_TRIP or read the voltage of specific battery cells via VC1, . . . , VC10.

**DRV Firmware** . We RE the relevant portions of the DRV firmware. It runs on an STM32F103CxT6 SoC and measures the motor voltage, storing it in a RAM register (offset 0x47). The DRV performs a voltage safety check independent of the BCTRL. If the motor voltage hits cUVT, the DRV raises “Error 24 - Supply Voltage out of range” and powers off the e-scooter after ten seconds.

## **3.3 New Vulnerabilities**

During our RE experiments on the M365 and ES3 e-scooters, we discovered four vulnerabilities:

- **V1: BCTRL firmware is unencrypted** . An attacker can retrieve the (stripped) BCTRL firmware in plaintext (e.g., during a firmware update) and RE it.

- **V2: BCTRL firmware is unsigned** . An attacker can modify the firmware of the BCTRL, including its safety thresholds and how it initializes the BMON, and flash the modified BCTRL on the victim’s e-scooter.

- **V3: UART bus lacks integrity protection, encryption, and authentication** . An attacker with access to the UART bus (e.g., via a malicious BCTRL firmware) can eavesdrop on all UART messages, replay or forge them, and impersonate or MitM the DRV and BTS.

- **V4: UART bus lacks protection against DoS** . An attacker accessing the UART bus can DoS internal (BMS, BTS,

and DRV) and external (Mi Home and battery charger) components.

These issues belong to known vulnerability classes but are novel in the context of e-scooters. They stem from design flaws in Xiaomi proprietary protocols, independent of specific hardware or implementation details. As a result, our four vulnerabilities impact the entire Xiaomi ecosystem, potentially affecting other Xiaomi devices using a similar BCTRL and UART bus.

## **4 E-Trojans Attacks**

We present _E-Trojans_ , four novel attacks on the internals of Xiaomi e-scooters. The attacks, among others, can undervolt the e-scooter battery while asking for a ransom, track the e- scooter using internal fingerprints over BLE, and exfiltrate confidential data. Each attack begins by flashing a malicious BCTRL firmware, which includes custom code that enables the necessary malicious capabilities, such as preventing legitimate BCTRL firmware updates. Since firmware updates require authentication, the attacker can bypass this restriction using, for example, the E-Spoofer toolkit [11].

## **4.1 Undervoltage Battery Ransomware (UBR)**

UBR is a novel _undervoltage ransomware_ that progressively and irreversibly damages the e-scooter’s battery until the victim pays a ransom. The damage is caused by flashing a malicious firmware that keeps the battery cell voltages below 2750mV (i.e., battery level lower than 0%). UBR has five steps, also shown in Algorithm 2:

1. The attacker flashes a malicious BCTRL firmware containing the ransomware that exploits remote and proximity-based techniques presented in [12]. The ransomware remains stealthy, letting the user ride the e- scooter as usual, until the battery is low. Although UBR does not require a specific battery level, batteries closer to 0% are faster to undervolt. Then, the user charges the battery using the stock charger.

2. UBR enters its _initialization_ phase (first five lines of Algorithm 2), where it: (1) disables undervoltage protections by increasing dUVT to 1580mV and bypassing cUVT safety checks; (2) disables load balancing by bypassing the cLBD safety checks; (3) disables battery charging by setting the canCharge flag to False; (4) activates the anti-theft software lock to prevent the e- scooter from becoming inactive and automatically turning off; (5) enforces faster discharging by disabling sleep mode and, optionally, spoofing a UART command that turns on the headlight and taillight.

3. UBR enters its _main loop_ , where it (8) reads the battery cells’ voltages from the BMON, and (9) checks for dead cells. Then, for each of the ten series of cells, it checks

6

## Slide 7

**Algorithm 2** UBR undervoltage ransomware logic.

- 1: disableUndervoltageChecks(cUVT, dUVT)

- 2: disableBalancing(cLBD) 3: disableCharging() _▷_ Sets canCharge to False 4: enableLock() _▷_ Keeps the e-scooter on 5: enableFastDischarge() _▷_ Battery discharges faster 6: 7: **loop** 8: battcells = readBMON(volt, amp) 9: deadcells = checkCellHealth(battcells)

- 10: log(deadcells) 11: **for** cell **in** battcells **do** 12: **if** cell _<_ cUVT **then** _▷_ 1580mV 13: log(cell, cUVT) 14: **else if** cell _<_ dUVT **then** _▷_ 2750mV 15: log(cell, dUVT) 16: **end if** 17: **end for** 18: **if** notifyUser **then** 19: log(notifyUser) 20: advertiseRansomOverBLE(url) _▷_ Reboot 21: **end if** 22: **end loop**

   - (12) if any cell is below cUVT or (14) below dUVT. Since undervoltage and balancing protections are off, the battery discharges below the undervoltage threshold and deteriorates. When a programmable condition is met (e.g., a cell reaches cUVT), the ransomware (18) reveals itself. The e-scooter (20) reboots and broadcasts the download link to the ransom payment app over BLE. The link appears shortened (e.g., _t.ly/AaBbCc_ ) due to length limitations on the e-scooter BLE name.

4. The victim installs the ransom app and can monitor the degradation of the battery. They stop the attack by transferring money to the attacker’s crypto wallet. Once the app’s backend confirms the payment (made in cryptocurrency, which complicates tracing), it reveals the secret unlock code, unique to that compromised device, to the app’s front end. The app then sends a special BLE packet that contains this unlock code, activating firmware updates on the BCTRL.

5. The ransom app guides the victim through a recovery procedure to restore the stock BCTRL firmware. The app flashes a BCTRL recovery firmware that allows charging even when the battery is critically undervolted. After the e-scooter is sufficiently charged (i.e., voltage is higher than cUVT), the app allows the user to flash the stock BCTRL.

UBR primarily impacts the victim’s safety by causing battery undervoltage and imbalance, which increases the likelihood of malfunctions and short circuits [28]. In the optimal scenario, the attacker undervolts a battery cell as low as 0mV, reducing its longevity [32, 67]. The impact of UBR,

BTS Mal. BCTRL DRV
Read BattId [14 B]
Read DRVId
DRVId [14 B]
Fingerprint [8 B] =
BattId[10:14] || DRVId[10:14]
Read BattLevel [2 B]
Read Mileage
Mileage [14 B]
Track [14 B] = Fingerprint
|| BattLevel || Mileage
EscName = Track
Reboots
Advertises EscName

Figure 4: User Tracking via Internals (UTI). Mal. BCTRL (the attacker) builds an 8-byte e-scooter fingerprint (Fingerprint) from the electric motor serial number. Then, they append other sensitive data like mileage and battery level to the fingerprint, creating a 14-byte tracking message (Track). Finally, they enforce a BLE name change to Track, allowing anyone to track the user and read their private data in real-time.

and battery ransomware attacks in general, is high: it causes irreversible physical damage to the battery, which is the most expensive component of an e-scooter. The same reasoning holds for other battery-powered systems, including electric vehicles. Replacing the battery can cost up to USD 139 [81], while most Xiaomi e-scooters are priced between USD 200 and 450. We highlight that UBR can be deployed _without_ asking for a ransom. This variant is a proximity or remote DoS attack that undervolts and destroys the battery without alerting the user.

## **4.2 User Tracking via Internals (UTI)**

UTI is a new _user tracking_ attack that tracks an e-scooter user and exfiltrates their private data. As shown in Figure 4, UTI creates a reliable user fingerprint and leaks sensitive e-scooter data. The malicious BCTRL firmware retrieves the 14-byte DRV serial number (Read DRVId) by impersonating the BTS and spoofing a read to the DRV. UTI builds a Fingerprint from the last 8 bytes of DRVId representing the year, month, and day of production, the revision, and the unit identifier (i.e., the nth unit produced that day).

UTI optionally retrieves via UART or I2C extra private data from the DRV, BMON, and BTS, like the mileage and battery level (Read BattLevel and Read Mileage). Then, UTI appends the data to the fingerprint and creates a 14-byte tracking message (Track). It sends a command to the BTS

7

## Slide 8

while spoofing the DRV to set the tracking message as the BLE name (EscName = Track). The e-scooter reboots and advertises its new name (Track) over BLE.

The adversary uses Track to identify the user via a proximity-based BLE sniffer or remotely via a malicious app. UTI is stealthy, as the Mi Home UI never shows the e-scooter name. Changing the e-scooter name does not disconnect or unpair the e-scooter from Mi Home, as it only checks the BLE address. Moreover, since the fingerprint persists through factory resets and firmware updates, UTI bypasses privacy defenses like BLE address randomization.

## **4.3 Denial of E-Scooter Services (DES)**

DES is a collection of seven DoS attacks, including an original _denial-of-sleep (DoSL)_ which is typically used in sensor networks [73]. DES impacts the availability of internal components (i.e., BTS, DRV, BCTRL, and BMON), internal buses (i.e., UART and I2C), e-scooter functionalities (i.e., battery charging, error handling, and sleep mode), external components (i.e., Mi Home and the battery charger), or even the entire e-scooter. These attacks are particularly effective as they DoS components from the inside and _cannot_ be fixed by the victim from the outside (e.g., via Mi Home or by rebooting). We summarize the seven DES attacks.

_DES1_ drops all UART and I2C packets destined for the BCTRL by altering the firmware code for internal bus communications. _DES2_ forces a supplier-only mode (SHIP mode) that disables the BMON by issuing a special unauthenticated I2C command. _DES3_ floods the UART bus with dummy packets by altering the firmware code for the UART transmitter function. _DES4_ periodically issues lock or reset commands to the DRV by impersonating the BTS and forging UART packets. As a result, the e-scooter is stuck in a state where the motor is immediately locked whenever the user tries to unlock it or in an infinite loop of power on and off.

_DES5_ disables battery charging by setting the canCharge flag in the BCTRL’s Flash memory to False. _DES6_ exploits the error handling routines by impersonating BTS, DRV, or BMON and raising fake errors that put the e-scooter in an irregular state (e.g., alarm noises, locked motor, unresponsiveness, and forced power off). _DES7_ is a denial-of-sleep attack that keeps the BCTRL in a resource-intensive mode instead of letting it switch to sleep mode by altering the BCTRL main loop (described in Algorithm 1).

## **4.4 Password Leak and Recovery (PLR)**

PLR enables remote and offline brute forcing of the e-scooter password. On the Mi Home app, the user can set a security code to prevent unauthorized access to their e-scooter (e.g., in case of smartphone theft). This (hashed) e-scooter password is stored on the DRV (memory address 0x17, 0x18, and 0x19) and is readable and writeable by other internal components.

PLR spoofs the BTS to retrieve the password’s SHA256 hash from the DRV, sets the e-scooter BLE name equal to the hash, and exfiltrates it via BLE advertising (similar to UTI). However, the 14-byte long e-scooter name is too short to fit the 32-byte SHA256 hash of the password.

To solve this, PLR cycles through three e-scooter names containing parts of the hash, causing a reboot each time the BLE advertisement changes, which is noticeable by the user. The password is brute-forceable, being a numeric sequence of exactly six digits (e.g., 123456), with a search space of 10<sup>6</sup> [41]. Hence, the attacker can use known techniques to recover the password offline, including password lists and rainbow tables.

## **4.5 Mapping Attacks and Vulnerabilities**

Table 3 shows the mapping between the four attacks and four vulnerabilities. The attacks take advantage of unencrypted BCTRL firmware (V1) as they rely on functionalities found via RE (e.g., sending UART messages from the BCTRL). Moreover, they exploit the unsigned BCTRL firmware (V2) to push malicious firmware on the BCTRL. The attacks also abuse the unprotected UART bus (V3) as they utilize arbitrary UART messages without properly encrypting and integrity protecting them and without needing to authenticate on the bus. Finally, DES exploits the lack of DoS protection on the UART bus (V4) to DoS internal and external e-scooter components.

## **5 Implementation**

We present E-Trojans, a toolkit that implements our RE findings and the four attacks described in Section 4. Our toolkit is _extensible_ to BESs from Xiaomi or other vendors employing a similar internal architecture and chips. We also include the attacks’ demos.

## **5.1 BCTRL Firmware Patch and Capabilities**

Our Python3 script (payload-patcher.py) binary patches a BCTRL using STM8 assembly code. During this process, the user can include up to ten new capabilities unavailable in the stock BCTRL firmware in the patch. We devised these capabilities thanks to our extensive RE of the BCTRL firmware. The script writes the STM8 assembly code for unused parts of the firmware and then updates the firmware CRC. The resulting binary can be flashed over BLE on the BCTRL of a M365 or ES3 e-scooter. We developed _ten_ capabilities that now we describe.

**DFU: Disable Firmware Updates** . DFU disables firmware updates on the BCTRL. We introduce a new canFwUpdate flag (address 0x04CB), set to False by default. We rewrite the HandleUART() function (address 0x94C5) to accept or reject firmware update packets (starting with 0x07,

8

## Slide 9

0x08, 0x09, or 0x0A), depending on canFwUpdate. This flag is set to True only when the BCTRL receives our new unlock packet (starting with 0xEE and followed by the correct unlock code). For example, in UBR, the user retrieves the unique unlock code by paying a ransom and utilizes it to enable firmware updates on the BCTRL.

**MUB: Manage UART Bus** . MUB sends arbitrary packets on UART. Due to V3, MUB can craft arbitrary UART messages and impersonate internal components (BTS, DRV, BCTRL, and BMON) by altering the sender field. We rewrite the sendUART() function (address 0xB06C) to send our forged packets, stored from address 0xD3 onward. For example, Password Leak and Recovery uses MUB to spoof the BTS and retrieve the SHA256 hash of the e-scooter password from the DRV.

**MIB: Manage I2C Bus** . MIB sends arbitrary packets on I2C. We rewrite the writeToI2C() function (address 0x90BE) to send our forged packets, whose data is stored in register A and target BMON register in register X. This includes special I2C commands, such as regressing the BMON into SHIP mode (used in DES7).

**DDT: Disable Dangerous Thresholds** . DDT alters the default BMON undervoltage and overvoltage thresholds. At BCTRL boot, DDT initializes the BMON’s UV_TRIP (address 0x923D) and OV_TRIP (address 0x923D) registers to 1580mV and 4700mV, their lowest and highest values, instead of the default ones. DDT enables UBR to reach voltages below the undervoltage threshold (i.e., 2750mV) recommended by Xiaomi, resulting in permanent battery damage and increased safety risks.

**DCT: Disable Critical Thresholds** . DCT bypasses batteryrelated errors, including undervoltage and overvoltage. We rewrite the BCTRL error handler to replace error checks (address 0xB5A9) with NOPs. For example, we use DCT in DES5 to raise fake errors, such as _Error 23 - Internal BMS not activated_ and _Error 24 - Supply Voltage out of range_ , putting the e-scooter in an abnormal state.

**DLB: Disable Load Balancing** . DLB prevents load balancing of the battery cells. We rewrite the manageLoadBalancing() function (address 0xA81A) to unset (with MOV) the three CELLBAL registers that regulate balancing. As a result, battery cells become more imbalanced over time. DLB enables UBR to create one extremely imbalanced cell that quickly dies, impacting battery longevity.

**DBC: Disable Battery Charging** . DBC disallows battery charging. We rewrite the controlCharge() (address 0x945C) function to read canCharge flag (address 0x42C) as False, even if the charger is connected. For instance, without DBC, DES5 would be unable to DoS the battery charger and prevent the battery from charging.

**FBD: Fast Battery Discharge** . FBD accelerates battery consumption. We rewrite the BCTRL main loop to permanently assign False to the sleepMode variable (address 0x400), forever disabling sleep mode and forcing the BC-

TRL to stay in a more resource-intensive mode. FBD can also turn on the e-scooter’s headlight and taillight to increase battery consumption. UBR uses FBD to accelerate battery depletion and critical undervoltage.

**CBA: Change BLE Advertising** . CBA changes the e- scooter’s BLE advertisements, including its BLE device name. CBA sends an arbitrary e-scooter advertising change packet to the BTS, causing a reboot. This packet comprises a destination field (0x20 to indicate BTS), an operation type field (0x50 to indicate a change in BLE advertising), and a payload containing the new advertisement. In UTI, the attacker tracks the user and exfiltrates their private data by changing the e-scooter’s BLE advertisements with CBA.

**SCV: Spoof Cell Voltage** . SCV spoofs voltage measurements of battery cells. We rewrite the BCTRL main loop to ignore BMON’s voltage measurements and only read the spoofed values we inject in register X. SCV delivers these values to the BTS, displaying them to the user via the Mi Home UI. By faking voltage measurements, SCV allows UBR to hide the real battery voltage of a spoofed cell from users who want to check the battery status via Mi Home.

**Capability Usage** . Table 4 shows how we _combine_ the ten capabilities to perform UBR, UTI, DES, and PLR. We require DFU in all attacks to prevent users from replacing our malicious BCTRL via BLE firmware updates. We integrate MUB and MIB in all attacks (except MIB in PLR), as they allow for controlling the UART and I2C buses. We deploy DDT, DCT, DLB, and SCV in UBR, as they affect the safety of the battery (i.e., undervoltage). We use DBC in UBR and DES5 as, alongside the e-scooter, they also target the battery charger. Similarly, we use FBD in UBR and DES7, as they try to accelerate battery consumption by triggering resource-intensive tasks. For UBR, UTI, and PLR, we rely on CBA to exfiltrate data from the e-scooter. UBR requires all capabilities.

## **5.2 UBR App and Backend**

As part of UBR, we developed an Android app and a Django and MongoDB backend to test our ransomware in a controlled but realistic environment. These components cooperate to generate unique ransomware unlock codes, manage cryptocurrency payments, and handle BCTRL firmware recovery.

**Android App** . We developed _ScooterToolkit_ , an Android app written in Kotlin. This app is given to the ransomware victim so that the ransom can be paid in cryptocurrency and the battery can be rebalanced. It requires Bluetooth, Location, and Internet permissions. The app initiates the BCTRL recovery when the back-end returns the unlock code that enables firmware updates (i.e., the user paid the ransom). Under normal battery conditions, the app flashes the stock BCTRL firmware. If the voltage is lower than 1580mV, a special recovery firmware is flashed instead.

**Django and MongoDB Backend** . Using Django, we developed a RESTful web service that exposes two APIs

9

## Slide 10

to the ransom app through the APIView class. The simulatePayment() API simulates a user payment, setting the payment status to Paid. The unlockFirmware(serial ) API requires the e-scooter’s motor serial as its input and if the ransom has been paid, their unlock code is returned. We also created a model serializer that converts e-scooter objects into JSON to interface with our MongoDB database. This database stores the e-scooter’s motor serial and model, 128bit ransomware unlock codes, and payment status for each compromised device.

## **6 Evaluation**

We evaluated our attacks by using the E-Trojans toolkit (described in Section 5) on Xiaomi M365 and ES3 e-scooters with up-to-date BTS, DRV, and BCTRL firmware.

## **6.1 Setup**

Our payload-patcher.py script offers an interactive shell to craft malicious BCTRL firmware. The user must select one of our four attacks and a supported e-scooter model (i.e., M365, Pro1, Essential, Pro2, and ES3). Then, we connect to the victim’s e-scooter, gain authorized access (i.e., through malicious pairing or session downgrade) and perform a rogue BCTRL firmware update.

We tested proximity-based attacks on a Dell Inspiron 15 3000 running a Linux-based OS, setting up the attacks from the BLE range. We tested remote attacks on a Realme GT (Android 13) and a OnePlus 3 (Android 9), performing the attack setup remotely from the _ScooterToolkit_ Android app installed on the victim’s smartphone.

Regarding UBR, we monitored the voltage and stopped the experiment upon reaching critical undervoltage (for safety reasons) or after ten hours. We tested the feasibility of retrieving the six-digit e-scooter password when deploying PLR. We considered the seven most common six-digit patterns [76] and randomly generated seventy Xiaomi-compliant passwords (ten for each pattern). Then, we implemented a rainbow table [38] and populated it with 3 million randomly generated Xiaomi-compliant passwords, simulating the most basic attacker setup.

## **6.2 Results**

As shown in Table 1, we conducted the four E-Trojans attacks on the M365 and the ES3. Our experimental results represent a _lower bound_ as other e-scooters and BESs might be affected by similar vulnerabilities. For instance, the Xiaomi Pro e-scooter runs BCTRL v1.2.6 (like the M365), and the 1S, Essential, and Pro 2 run BCTRL v1.4.1 (like the ES3) [64]. Next, we provide attack-specific insights.

**UBR** . UBR irreversibly reduced the battery autonomy of the M365 by approximately 50% in three hours and thirty

Table 1: Evaluation results. All four attacks are effective on the M365 and ES3. ✓<sup>_∗_</sup> : UBR with dangerous undervoltage.

|**Attack**|**M365**|**ES3**|**Details**|
|---|---|---|---|
|UBR|✓|✓<sup>_∗_</sup>|Battery autonomy -50% in 3.5h (M365)|
|UTI|✓|✓|Persists factory resets|
|DES|✓|✓|Internal component failure|
|PLR|✓|✓|Leaks common passwords|

minutes. We forced a critical undervoltage state and stopped the experiment when some cells reached 0V (i.e., the most critical undervoltage condition). This group of cells now has limited charging capacity (i.e., 75%) and discharges four times faster than average.

Similarly, we reduced the battery autonomy of the ES3 by around 10% in ten hours, spending six of them depleting the battery to 0% (three hours for the M365). We could not reach a critical undervoltage due to the DRV independently measuring an abnormal voltage and raising _Error 24 - Supply Voltage out of range_ . As such, the ES3 is better protected than the M365 against UBR, even though it still sustained significant damage.

**UTI** . UTI successfully tracks users and exfiltrates their private data over BLE. We sniffed BLE advertisements emitted by e-scooters running our malicious firmware. We could identify each device from their fingerprint (e.g., motor serial number), allowing us to track users across four areas where we deployed BLE sniffers. The sniffers uploaded location data online, allowing for real-time tracking. We could read real-time mileage (e.g., 0x01B1 represents 433km), battery level (e.g., 0x2D represents 45%), and other updated data.

We confirmed that the user is still trackable after a factory reset. We could also extrapolate the user’s movements to some extent. For example, we made the user stop at a random position during a ride between two monitored locations. By leaking the total mileage, last travel time, last travel mileage, and average speed, we could infer where a user stopped and for how long. Similarly, by leaking the battery level, the attacker can infer whether the user stopped at a familiar place (e.g., home or office) to charge the e-scooter.

**DES** . DES made the e-scooter unresponsive and not rideable. DES1 and DES3 cause the DRV to raise _Error 21 - No Communication with BMS_ , halting the motor and powering off the e-scooter after ten seconds. DES2 cuts power from all internal systems, powering off the e-scooter and barring it from powering on again. DES4 prevents battery charging regardless of the battery charger hardware or the e-scooter status (e.g., powered on or off). DES5 induces an endless lock state or reboot cycle, rendering the e-scooter unable to move and forcing it continuously to stay powered on.

DES6 raises _Error 23 - Internal BMS not activated_ which induces a constant beeping noise and _Error 24 - Supply Volt-_

10

## Slide 11

_age out of range_ which powers off the e-scooter. DES7 ignores all sleep cycles even when the e-scooter is off, thus accelerating battery consumption. DES was able to target a variety of internal components and deny them. To restore the e-scooter to its original state, the user needs to flash the original BMON firmware via debug ports without the option of an over-the-air firmware update. This operation is complex, as it requires disassembling the entire battery compartment.

**PLR** . PLR leaked the e-scooter password hash and enabled offline brute forcing. We sniffed three rotating BLE advertisements broadcasted by a compromised e-scooter, each containing a fragment of the hash. Since the e-scooter resets after changing its advertisement, we programmed the malicious firmware to rotate it in rapid succession, tricking the user into thinking a single reboot happened instead of three. We also confirmed that retrieving the e-scooter password from the hash is feasible. Our non-optimized rainbow table cracked the seventy passwords, following the most common six-digit patterns, in less than one second on average.

**Safety Concerns** . Our evaluation confirmed that a malicious BCTRL can turn off hardware protections in the BCTRL, e.g., load balancing, and in the BMON, e.g., voltage thresholds.

The risk of fires and thermal runaway due to undervoltage is realistic. For example, UBR undervolted the M365’s battery below 100mV (below cUVT = 1580mV), placing it in a harmful deep discharge state that increases the likelihood of short circuits and fires. This dangerous condition is also difficult for users to detect, as the BCTRL can spoof battery parameters to conceal the damage.

Battery overheating via overvoltage requires an additional assumption, i.e., a compromised or malfunctioning charger. We confirmed the feasibility of overvoltage using a programmable power supply in a safe environment. We raised the battery voltage to 4900mV (above cOVT = 4700mV), and terminated the experiment to avoid safety risks.

## **7 Countermeasures**

We propose four _practical_ and _backward-compatible_ countermeasures, each addressing one of the four vulnerabilities described in Section 3.3 (i.e., C1 addresses V1, and so on). To fix UBR, UTI, and PLR, Xiaomi must implement C1, C2, and C3. To fix all DES variants, Xiaomi should also add C4.

Our countermeasures introduce negligible overhead, as they leverage lightweight cryptography (TEA [78], SCP03 [50]) designed for embedded systems, while providing valuable security guarantees, including encryption and authentication, and DoS protection. They do not contribute to vendor lock-in for batteries, as third-party batteries remain compatible with the stock BMS.

**C1: Encrypt the BCTRL firmware with TEA** . Xiaomi should encrypt the BCTRL firmware to protect its confidentiality at rest (e.g., in Mi Home) and in transit (e.g., during a

firmware update over BLE). We recommend reusing the TEA block cipher already used to encrypt the DRV firmware.

**C2: Sign and verify the BCTRL firmware with ECDSA** . Xiaomi should digitally sign and verify the BCTRL firmware to prevent rogue BCTRL firmware updates. We recommend reusing ECDSA, which is FIPS-compliant [48] and already employed to sign/verify the DRV and BTS firmware.

**C3: Protect the UART bus with SCP03** . Xiaomi should protect the confidentiality, integrity, and authenticity of the UART bus. We suggest using standard secure embedded bus protocols such as _Secure Channel Protocol 03 (SCP03)_ [50]. SCP03 provides confidentiality, integrity, authenticity, and replay protection using a lightweight scheme based on preshared symmetric keys, authenticated encryption, and AES.

**C4: Protect the UART bus with rate limiting** . Xiaomi should protect the UART bus against DoS attacks or at least mitigate them. We recommend implementing an efficient rate-limiting mechanism for UART, such as the leaky bucket algorithm, where excess packets are discarded if the incoming packet rate exceeds the outgoing rate. Combining C4 with C2 enhances DoS protection, as C4 discards messages failing the integrity checks.

## **8 Related Work**

**E-Scooters’ Security and Privacy** . Research on e-scooters has studied their proprietary protocols and rental ecosystems, but no work has focused on their _internals_ . A recent contribution [12] analyzed the Xiaomi e-scooter ecosystem, identifying issues in the proprietary BLE protocols used by the e-scooter and Mi Home. The researchers identified vulnerabilities [1] in the Bird e-scooter sharing platform and discovered MitM attacks [46] on the rental e-scooters of the Lime company. Other studies focused on the privacy of user-related data in e-scooter rental Android apps [75] and the safety risks of riding e-scooters [40].

**E-Scooters Hacking and Modding** . In 2019, Zimperium revealed flaws in the M365 locking system that could halt a running e-scooter [83]. The same year, the hacker Lanrat found that M365 does not enforce authentication over BLE [23]. ScooterHacking [63], the largest e-scooter modding community, released tools [61, 62] to interact with Xiaomi e-scooters and perform firmware updates [7]. Modding tools, such as [60], focus on increasing the e-scooter’s performance by, for example, increasing the motor’s speed value stored in the DRV’s Flash memory. In contrast, we focus on the BCTRL firmware and develop custom patches for it. Our patches incorporate a substantial amount of binary instructions, including conditional jumps and new UART packets, that implement _new_ capabilities previously unavailable on a Xiaomi e-scooter.

**Attacks on Battery** . The likelihood of battery overheating, thermal runaway, overcharging, and mechanical damage

11

## Slide 12

in electric vehicles have been investigated in [20, 36]. Researchers have proposed a battery drain attack while the ignition is turned off [15], an electromagnetic interference attack [72], and a physical access rogue firmware update to a Tesla BMS [34]. Theoretical vulnerabilities in MacBook laptop batteries, capable of overheating or turning off the machine, have been discussed in [43]. The E-Trojans attacks are _orthogonal_ as they target the battery and BMS of an e-scooter.

**Attacks on Embedded Firmware** . Several studies have focused on malicious embedded firmware, but we are the _first_ to introduce a battery ransomware leveraging a malicious BMS firmware. Researchers attacked embedded firmware on programmable control logic (PCL) [24], object trackers [54], printers [19], mice [42], OS management systems [29], mobile bootloaders [51], network equipment [18], botnets [2] and recently industrial wrenches [49].

**Attacks on BES** . Security research on BESs has identified vulnerabilities across various domains. Automotive researchers exploited the insecure CAN bus by compromising an Electronic Control Unit (ECU) [35]. Similar works have exposed wireless charging stations and EV infrastructure to attacks such as MitM, DoS, and privacy leakage [3,37,47,55,80]. Studies on drones have revealed issues in firmware updates, mobile apps, and wireless traffic [9, 22, 39, 56]. Several IoT devices, such as fitness trackers [13, 16, 27], vacuum robots [25, 26, 74], crypto wallets [44], and smart doorbells [57], have been found vulnerable to a broad range of attacks, including spoofing, eavesdropping, MitM, privacy, and physical attacks. Compared to prior attacks on BESs, we introduce several _novel_ aspects, including the RE of e-scooters’ internal attack surface (an area previously unexplored in the literature), the development of new proximity and remote attacks (e.g., undervoltage battery ransomware and user tracking), and the evaluation of voltage protections in the Xiaomi BMS, along with their safety implications.

## **9 Conclusion**

We present the first evaluation of Xiaomi e-scooters’ internals and their attack surface. Although we focus on M365 and ES3, two popular e-scooters, our research is generalizable to any BES with a comparable system model. We RE the internal systems and communication channels, uncovering four critical flaws affecting the e-scooter’s BCTRL and UART bus. We exploit these vulnerabilities by developing four novel attacks we name E-Trojans. Our attacks violate the safety (UBR), privacy (UTI), availability (DES), and security (PLR) of the Xiaomi e-scooter ecosystem. For example, we deploy the first ransomware for an e-scooter that permanently damages the battery via undervoltage. Our attacks are conducted in BLE proximity or remotely via a malicious Android application.

We develop E-Trojans, a toolkit that implements our attacks by leveraging our RE findings (e.g., disable safety thresholds). We successfully carried out the attacks on actual devices,

proving their practicality. For instance, UBR irreversibly reduced the M365 battery autonomy by 50% in three hours and the ES3 battery autonomy by 10% in ten hours. We fix attacks and their root causes with four backward-compatible countermeasures.

## **Acknowledgments**

Work funded by the European Union under grant agreement no. 101070008 (ORSHIN project). Views and opinions expressed are however those of the author(s) only and do not necessarily reflect those of the European Union. Neither the European Union nor the granting authority can be held responsible for them. Moreover, it has been partially supported by the French National Research Agency under the France 2030 label (NF-HiSec ANR-22-PEFT-0009) and the Apricot/ENCOPIA ANR MESRI-BMBF project (ANR-20-CYAL-0001).

## **References**

- [1] App Analyst. App Analysis: Bird. https://theappan alyst.com/bird.html/, 2019.

- [2] Manos Antonakakis, Tim April, Michael Bailey, Matt Bernhard, Elie Bursztein, Jaime Cochran, Zakir Durumeric, J Alex Halderman, Luca Invernizzi, Michalis Kallitsis, et al. Understanding the mirai botnet. In _26th USENIX security symposium (USENIX Security 17)_ , pages 1093–1110, 2017.

- [3] Richard Baker and Ivan Martinovic. Losing the car keys: Wireless PHY-Layer insecurity in EV charging. In _28th USENIX Security Symposium (USENIX Security 19)_ , pages 407–424, 2019.

- [4] Ltd Beijing Xiaomi Mobile Software Co. Mi Home (Android). https://play.google.com/store/apps /details?id=com.xiaomi.smarthome, 2024.

- [5] Ltd Beijing Xiaomi Mobile Software Co. Mi Home (iOS). https://apps.apple.com/us/app/mi-hom e-xiaomi-smart-home/id957323480, 2024.

- [6] Brian Benchoff. Security Engineering: Inside the Scooter Startups. https://hackaday.com/2019/ 02/12/security-engineering-inside-the-sco oter-startups/, 2019.

- [7] BotoX. Xiaomi M365 Firmware Patcher. https://gi thub.com/BotoX/xiaomi-m365-firmware-patch er, 2022.

- [8] BotoX. Xiaomi M365 Firmware Patcher (GitHub). ht tps://github.com/BotoX/xiaomi-m365-firmwar e-patcher/blob/master/xiaotea/xiaotea.py, 2024.

12

## Slide 13

- [9] Pedro Cabrera. Parrot Drones Hijacking. https://ww w.rsaconference.com/Library/presentation/U SA/2018/parrot-drones-hijacking, 2018.

- [10] Louis Cameron Booth and Matay Mayrany. Iot penetration testing: Hacking an electric scooter, 2019.

- [11] Marco Casagrande. E-Spoofer (GitHub). https://gi thub.com/Skiti/ESpoofer, 2024.

- [12] Marco Casagrande, Riccardo Cestaro, Eleonora Losiouk, Mauro Conti, and Daniele Antonioli. E-Spoofer: Attacking and Defending Xiaomi Electric Scooter Ecosystem. In _Proceedings of the 16th ACM Conference on Security and Privacy in Wireless and Mobile Networks_ , WiSec ’23, New York, NY, USA, 2023. Association for Computing Machinery.

- [13] Marco Casagrande, Eleonora Losiouk, Mauro Conti, Mathias Payer, and Daniele Antonioli. Breakmi: Reversing, exploiting and fixing xiaomi fitness tracking ecosystem. _IACR Transactions On Cryptographic Hardware And Embedded Systems_ , 2022(3):330–366, 2022.

- [14] Stephen Checkoway, Damon McCoy, Brian Kantor, Danny Anderson, Hovav Shacham, Stefan Savage, Karl Koscher, Alexei Czeskis, Franziska Roesner, and Tadayoshi Kohno. Comprehensive experimental analyses of automotive attack surfaces. In _20th USENIX security symposium (USENIX Security 11)_ , 2011.

- [15] Kyong-Tak Cho, Yuseung Kim, and Kang G Shin. Who killed my parked car? _arXiv preprint arXiv:1801.07741_ , 2018.

- [16] Jiska Classen, Daniel Wegemer, Paul Patras, Tom Spink, and Matthias Hollick. Anatomy of a Vulnerable Fitness Tracking System: Dissecting the Fitbit Cloud, App, and Firmware. _Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies (IMWUT_

- _’18)_ , 2(1):1–24, 2018.

- [17] CNN. Israel concealed explosives inside batteries of pagers sold to Hezbollah, Lebanese officials say. https: //edition.cnn.com/2024/09/27/middleeast/is rael-pager-attack-hezbollah-lebanon-invs-i ntl/index.html, 2024.

- [18] Andrei Costin, Jonas Zaddach, Aurélien Francillon, and Davide Balzarotti. A large-scale analysis of the security of embedded firmwares. In _23rd USENIX security symposium (USENIX Security 14)_ , pages 95–110, 2014.

- [19] Ang Cui, Michael Costello, and Salvatore Stolfo. When firmware modifications attack: A case study of embedded exploitation. In _NDSS_ , 2013.

- [20] Yan Cui, Jianghong Liu, Xin Han, Shaohua Sun, and Beihua Cong. Full-scale experimental study on suppressing lithium-ion battery pack fires from electric vehicles. _Fire Safety Journal_ , page 103562, 2022.

- [21] Univ Datos. Folding Electric Scooter Market: Current Analysis and Forecast (2023-2030). https://univda tos.com/report/folding-electric-scooter-m arket/, 2022.

- [22] Eddy Deligne. ARDrone Corruption. https://link .springer.com/article/10.1007/s11416-011-0 158-4, 2011.

- [23] Ian D. Foster. Xiaomi M365 Scooter Authentication Bypass. https://lanrat.com/xiaomi-m365/, 2019.

- [24] Luis Garcia, Ferdinand Brasser, Mehmet Hazar Cintuglu, Ahmad-Reza Sadeghi, Osama A Mohammed, and Saman A Zonouz. Hey, My Malware Knows Physics! Attacking PLCs with Physical Model Aware Rootkit. In _NDSS_ , pages 1–15, 2017.

- [25] Dennis Giese. Having fun with IoT: Reverse Engineering and Hacking of Xiaomi IoT Devices. https: //dontvacuum.me/talks/DEFCON26/DEFCON26-Hav ing_fun_with_IoT-Xiaomi.html, 2018.

- [26] Dennis Giese and Braelynn. DEFCON 32 - Reverse engineering and hacking Ecovacs robots. https:// youtu.be/_wUsM0Mlenc?si=ACJj36Xvic03okKj, 2025.

- [27] Rohit Goyal, Nicola Dragoni, and Angelo Spognardi. Mind the Tracker You Wear: A Security Analysis of Wearable Health Trackers. In _Proceedings of the 31st Annual ACM Symposium on Applied Computing (SAC_

- _’16), Pisa, Italy_ , page 131–136, 2016.

- [28] Rui Guo, Minggao Ouyang, Languang Lu, and Xuning Feng. Mechanism of the Entire Overdischarge Process and Overdischarge-induced Internal Short Circuit in Lithium-ion Batteries. _Scientific Reports_ , page 30248, 2016.

- [29] Duha Ibdah, Nada Lachtar, Abdulrahman Abu Elkhail, Anys Bacha, and Hafiz Malik. Dark firmware: a systematic approach to exploring application security risks in the presence of untrusted firmware. In _23rd International Symposium on Research in Attacks, Intrusions and Defenses (RAID 2020)_ , pages 413–426, 2020.

- [30] Texas Instrument. 6 to 10-Series Cell Li-Ion and LiPhosphate Battery Monitor. https://www.ti.com/p roduct/BQ76930, 2022.

- [31] Texas Instrument. BQ769x0 Datasheet. https://www. ti.com/lit/ds/symlink/bq76930.pdf, 2022.

13

## Slide 14

- [32] Texas Instruments. How To Protect 48-V Batteries from Overcurrent and Undervoltage. https://www.ti.com /lit/an/snoaa65/snoaa65.pdf, 2020.

- [33] Gizay Kisa Isik, Theo Tryfonas, and George Oikonomou. E-scooter sharing platforms: Understanding their architecture and cybersecurity threats. In _2023 IEEE 26th International Conference on Intelligent Transportation Systems (ITSC)_ , pages 5909–5916, 2023.

- [34] Patrick Kiley. Reverse Engineering the Tesla Battery Management System to Increase Power Available. ht tps://www.youtube.com/watch?v=UV2zvgyIF0I, 2020.

- [35] Karl Koscher, Alexei Czeskis, Franziska Roesner, Shwetak Patel, Tadayoshi Kohno, Stephen Checkoway, Damon McCoy, Brian Kantor, Danny Anderson, Hovav Shacham, et al. Experimental security analysis of a modern automobile. In _2010 IEEE symposium on security and privacy_ , pages 447–462. IEEE, 2010.

- [36] Binghe Liu, Yikai Jia, Chunhao Yuan, Lubing Wang, Xiang Gao, Sha Yin, and Jun Xu. Safety issues and mechanisms of lithium-ion battery cell upon mechanical abusive loading: A review. _Energy Storage Materials_ , pages 85–112, 2020.

- [37] Jianwei Liu, Xiang Zou, Leqi Zhao, Yusheng Tao, Sideng Hu, Jinsong Han, and Kui Ren. Privacy leakage in wireless charging. _IEEE Transactions on Dependable and Secure Computing_ , 2022.

- [38] Charles Lu and Jialin Ding. Rainbow Table Attack on 6-Digit PINs (GitHub). https://github.com/clu8/ RainbowTable, 2015.

- [39] Aaron Luo. Multidimensional Attack Vectors and Countermeasures. https://media.defcon.org/DEFCON2 4/DEFCON24presentations/DEFCON24-Aaron-Luo

- -Drones-Hijacking-Multi-Dimensional-Attac k-Vectors-And-Countermeasures-UPDATED.pdf, 2016.

- [40] Qingyu Ma, Hong Yang, Alan Mayhue, Yunlong Sun, Zhitong Huang, and Yifang Ma. E-scooter safety: The riding risk analysis based on mobile sensing data. _Accident Analysis and Prevention_ , 2021.

- [41] Philipp Markert, Daniel V Bailey, Maximilian Golla, Markus Dürmuth, and Adam J Aviv. This pin can be easily guessed: Analyzing the security of smartphone unlock pins. In _2020 IEEE Symposium on Security and Privacy (SP)_ , pages 286–303. IEEE, 2020.

- [42] Jacob Maskiewicz, Benjamin Ellis, James Mouradian, and Hovav Shacham. Mouse trap: Exploiting firmware updates in USB peripherals. In _8th USENIX Workshop on Offensive Technologies (WOOT 14)_ , 2014.

- [43] Charlie Miller. Battery firmware hacking. _Black Hat USA_ , pages 3–4, 2011.

- [44] Michael Mouchous and Karim Abdellatif. Hardwear.io USA - The Misuse Of Secure Components In Hardware Wallets. https://www.youtube.com/watch?v=BoOT VeFL30I, 2023.

- [45] Daljeet Nandha. Exploring Xiaomi’s New Firmware Security Measures. https://robocoffee.de/?p=1 93, 2022.

- [46] BBC News. Scooters Hacked To Play Rude Messages To Riders. https://www.bbc.com/news/technolog y-48065432, 2019.

- [47] Tao Ni, Xiaokuan Zhang, Chaoshun Zuo, Jianfeng Li, Zhenyu Yan, Wubing Wang, Weitao Xu, Xiapu Luo, and Qingchuan Zhao. Uncovering User Interactions on Smartphones via Contactless Wireless Charging Side Channels. In _2023 IEEE Symposium on Security and Privacy (SP)_ , pages 3399–3415. IEEE, 2023.

- [48] NIST. FIPS 186-5 – Digital Signature Standard (DSS). https://nvlpubs.nist.gov/nistpubs/FIPS/NIS T.FIPS.186-5.pdf, 2023.

- [49] PCmag. Network-Connected Torque Wrench Used in Factories Is Vulnerable to Ransomware. https://www. pcmag.com/news/network-connected-torque-w rench-used-in-factories-is-vulnerable-to-r ansomware, 2024.

- [50] Global Platform. Secure Channel Protocol 03. https: //globalplatform.org/wp-content/uploads/201 4/07/GPC_2.3_D_SCP03_v1.1.2_PublicRelease. pdf, 2019.

- [51] Nilo Redini, Aravind Machiry, Dipanjan Das, Yanick Fratantonio, Antonio Bianchi, Eric Gustafson, Yan Shoshitaishvili, Christopher Kruegel, and Giovanni Vigna. Bootstomp: on the security of bootloaders in mobile devices. In _26th USENIX Security Symposium (USENIX Security 17)_ , pages 781–798, 2017.

- [52] Grand View Research. Electric Scooters Market Size, Share & Trends Analysis Report (2024- 2030). https: //www.grandviewresearch.com/industry-analy sis/electric-scooters-market, 2024.

- [53] Grand View Research. Micro-mobility market size, share & trends analysis report by vehicle type (electric kick scooters, electric skateboards, electric bicycles), by battery, by voltage, by region, and segment forecasts, 2021 - 2028. https://www.grandviewresearch. com/industry-analysis/micro-mobility-marke t-report, 2024.

14

## Slide 15

- [54] Thomas Roth, Fabian Freyer, Matthias Hollick, and Jiska Classen. Airtag of the clones: shenanigans with liberated item finders. In _2022 IEEE Security and Privacy Workshops (SPW)_ , pages 301–311. IEEE, 2022.

- [55] Khaled Sarieddine, Mohammad Ali Sayed, Sadegh Torabi, Ribal Attallah, Danial Jafarigiv, Chadi Assi, and Mourad Debbabi. Uncovering covert attacks on ev charging infrastructure: How ocpp backend vulnerabilities could compromise your system. In _Proceedings of the 19th ACM Asia Conference on Computer and Communications Security_ , page 977–989, 2024.

- [56] Moritz Schloegel and Nico Schiller. Unchained Skies: A Deep Dive into Reverse Engineering and Exploitation of Drones. https://cfp.recon.cx/2023/talk/HLH H89/, 2023.

- [57] Daniel Schwendner. Hardwear.io NL - Hacking A Smart Doorbell: An IoT Hacking Guide. http://youtube. com/watch?v=pfp5IaQyIkg, 2023.

- [58] Scootered. Xiaomi M365 Full Specs. https://www. scootered.co.uk/electric-scooter-specs/xia omi-m365-electric-scooter-full-specificati on.html, 2024.

- [59] Scootered. Xiaomi Mi 3 Full Specs. https://www.sc ootered.co.uk/electric-scooter-specs/xiaom i-mi-3-electric-scooter-full-specification .html, 2024.

- [60] ScooterHacking. ScooterHacking Firmware Toolkit. https://mi.cfw.sh/, 2022.

- [61] ScooterHacking. ScooterHacking (GitHub). https: //github.com/orgs/scooterhacking/repositor ies, 2022.

- [62] ScooterHacking. ScooterHacking Utility App. https: //play.google.com/store/apps/details?id=sh .cfw.utility, 2022.

- [63] ScooterHacking. ScooterHacking Website. https: //scooterhacking.org/, 2022.

- [64] ScooterHacking. ScooterHacking Firmware (GitHub). https://github.com/scooterhacking/firmware /, 2023.

- [65] ScooterHacking. ScooterHacking Utility Homepage. https://utility.cfw.sh/, 2023.

- [66] Ma Si. Segway-Ninebot Eyes Bigger Market Share in Country. https://global.chinadaily.com.cn/a /202204/28/WS6269ee14a310fd2b29e59d1f.html, 2022.

- [67] Shashank Sripad, Sekar Kulandaivel, Vikram Pande, Vyas Sekar, and Venkatasubramanian Viswanathan. Vulnerabilities of Electric Vehicle Battery Packs to Cyberattacks on Auxiliary Components. _arXiv preprint arXiv:1711.04822_ , 2017.

- [68] Statista. Battery electric vehicles - worldwide. https: //www.statista.com/outlook/mmo/electric-veh icles/battery-electric-vehicles/worldwide, 2024.

- [69] STMicroelectronics. STM8L151K6 Datasheet. https: //www.st.com/resource/en/datasheet/stm8l15 1r6.pdf, 2018.

- [70] STMicroelectronics. Ultra-low-power 8-bit MCU with 32 Kbytes Flash, 16 MHz CPU, integrated EEPROM. https://www.st.com/en/microcontrollers-mic roprocessors/stm8l151k6.html, 2018.

- [71] STMicroelectronics. Migration of Applications from the STM8L and STM8S Series to the STM32C0 Series Microcontrollers. https://www.st.com/resource/ en/application_note/an5775-migration-of-a pplications-from-the-stm8l-and-stm8s-serie s-to-the-stm32c0-series-microcontrollers-s tmicroelectronics.pdf, 2022.

- [72] Marcell Szakály, Sebastian Köhler, Martin Strohmeier, and Ivan Martinovic. Assault and Battery: Evaluating the Security of Power Conversion Systems Against Electromagnetic Injection Attacks. _arXiv preprint arXiv:2305.06901_ , 2023.

- [73] Jason Uher, Ryan G Mennecke, and Bassam S Farroha. Denial of Sleep Attacks in Bluetooth Low Energy Wireless Sensor Networks. In _MILCOM 20162016 IEEE Military Communications Conference_ , pages 1231–1236. IEEE, 2016.

- [74] Fabian Ullrich, Jiska Classen, Johannes Eger, and Matthias Hollick. Vacuums in ihe cloud: Analyzing security in a hardened iot ecosystem. In _13th USENIX Workshop on Offensive Technologies (WOOT 19)_ , 2019.

- [75] Nisha Vinayaga-Sureshkanth, Raveen Wijewickrama, Anindya Maiti, and Murtuza Jadliwala. An investigative study on the privacy implications of mobile e-scooter rental apps. In _Proceedings of the 15th ACM Conference on Security and Privacy in Wireless and Mobile Networks_ , page 125–139, 2022.

- [76] Ding Wang, Qianchen Gu, Xinyi Huang, and Ping Wang. Understanding human-chosen pins: Characteristics, distribution and security. In _Proceedings of the 2017 ACM on Asia Conference on Computer and Communications Security (ASIA CCS’17)_ . Association for Computing Machinery, 2017.

15

## Slide 16

- [77] Tech We Want. Who Makes Bird and Lime Scooters? https://techwewant.com/this-is-who-makes-b ird-lime-and-jump-scooters-review-b3f6be3 2221e, 2018.

- [78] David J Wheeler and Roger M Needham. TEA, a tiny encryption algorithm. In _Fast Software Encryption: Second International Workshop Leuven, Belgium, December 14–16, 1994 Proceedings 2_ , pages 363–366. Springer, 1995.

- [79] Marko Wolf, André Weimerskirch, and Christof Paar. Security in automotive bus systems. In _Workshop on Embedded Security in Cars_ , pages 1–13. Bochum, 2004.

- [80] Yi Wu, Zhuohang Li, Nicholas Van Nostrand, and Jian Liu. Time to rethink the design of Qi standard? security and privacy vulnerability analysis of Qi wireless charging. In _Annual Computer Security Applications Conference_ , pages 916–929, 2021.

- [81] Xiaomi. Query Estimated Spare Parts Price. https: //www.mi.com/uk/support/spare-parts-price/? name=xiaomi-electric-scooter-4-pro-2nd-gen, 2024.

## **Appendix - Additional Tables**

Table 2: Battery and BMS details. OVT: overvoltage threshold, UVT: undervoltage threshold, LBD: load balancing delta. Prefix "d" means dangerous, and prefix "c" means critical.

||**M365**|**ES3**|
|---|---|---|
|_Battery_|||
|Manuf.|Ninebot|Ninebot|
|Type|Li-Ion 18650|Li-Ion 18650|
|Chem.|10INR19/66-3|10INR19/66-3|
|Cells|30 (10x3)|30 (10x3)|
|Capacity|7.80Ah/300Wh|7.65Ah/275Wh|
|Voltage|42V to 36V|42V to 36V|
|_BMS_|||
|BCTRL|STM8L151K6|STM8L151K6|
|BMON|BQ76930|BQ76930|
|dOVT|4200mV|4200mV|
|cOVT|4700mV|4700mV|
|dUVT|2750mV|2750mV|
|cUVT|1580mV|1580mV|
|cLBD|800mV|800mV|

- [82] Xiaomi. Xiaomi Bug Bounty Program (HackerOne). https://hackerone.com/xiaomi, 2024.

- [83] Rani Idan (Zimperium). Don’t Give Me A Brake – Xiaomi Scooter Hack Enables Dangerous Accelerations And Stops For Unsuspecting Riders. https://blog.z imperium.com/dont-give-me-a-brake-xiaomi-s cooter-hack-enables-dangerous-acceleratio ns-and-stops-for-unsuspecting-riders/, 2019.

Table 3: Mapping between the four attacks and the four vulnerabilities. All attacks exploit V1, V2, and V3. Only the DES attacks exploit V4.

|**Attack**|**V1**|**V2**|**V3**|**V4**|
|---|---|---|---|---|
|Undervoltage Battery Ransomware (UBR)|✓|✓|✓|✗|
|User Tracking via Internals (UTI)|✓|✓|✓|✗|
|Denial of E-Scooter Services (DES)|✓|✓|✓|✓|
|Password Leak and Recovery (PLR)|✓|✓|✓|✗|

Table 4: Mapping between the ten capabilities and the four attacks. All capabilities enable one or more attacks. All ten capabilities are required to deploy UBR.

|**Capability**|**UBR**|**UTI**|**DES**|**PLR**|
|---|---|---|---|---|
|Disable Firmware Updates (DFU)|✓|✓|✓|✓|
|Manage UART Bus (MUB)|✓|✓|✓|✓|
|Manage I2C Bus (MIB)|✓|✓|✓|✗|
|Disable Dangerous Thresh. (DDT)|✓|✗|✗|✗|
|Disable Critical Thresh. (DCT)|✓|✗|✗|✗|
|Disable Load Balancing (DLB)|✓|✗|✗|✗|
|Disable Battery Charging (DBC)|✓|✗|✓|✗|
|Fast Battery Discharge (FBD)|✓|✗|✓|✗|
|Change BLE Advertising (CBA)|✓|✓|✗|✓|
|Spoof Cell Voltage (SCV)|✓|✗|✗|✗|

16
