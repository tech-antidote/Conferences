---
title: "How much of our Bluetooth firmware reverse engineering work can now be automated with LLMs"
speakers: ["Veronica Kovah", "Xeno Kovah"]
conference: "DEF CON"
conference_full: "DEF CON 34"
edition: "34"
year: null
source_pdf: "DEF CON 34/DEF CON 34 - Veronica Kovah, Xeno Kovah - How much of our Bluetooth firmware reverse engineering work can now be automated with LLMs - rever.pdf"
pages: 171
sha256: "7d47b5d8d0659f6843e1ff2307d12bf8ea984a0d5229d0876ab98d2ecec48623"
text_chars: 71387
ocr_pages: 7
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T00:33:24Z"
---
# How much of our Bluetooth firmware reverse engineering work can now be automated with LLMs

**Speakers:** Veronica Kovah, Xeno Kovah  
**Conference:** DEF CON 34  
**Source:** `DEF CON 34/DEF CON 34 - Veronica Kovah, Xeno Kovah - How much of our Bluetooth firmware reverse engineering work can now be automated with LLMs - rever.pdf` (171 pages)

## Slide 1

### **How much of our Bluetooth firmware reverse engineering work can now be automated with LLMs? (Spoiler: a lot!) Xeno Kovah & Veronica Kovah - Dark Mentor LLC**

## Slide 2

#### **About us**

• Veronica previously worked at NSA as a "Capability Development Specialist" and adjunct instructor. Founded Dark Mentor in 2018

"Capab ~~i~~ l ~~i~~ ty Development Spec ~~i~~ al ~~i~~ st"

• Xeno previously worked at Apple as the firmware security team lead. In addition to joining Dark Mentor in 2021 he also runs OpenSecurityTraining2 (https://ost2.fyi), a nonprofit that provides freeas-in-beer and free-as-in-freedom security classes online

## Slide 3

#### **And** **_also..._ We're here for our 20th wedding anniversary!!!** • We got married in Vegas while in town for DEFCON 14 in 2006!!!

🎉

## Slide 4

#### **Prior work**

• Veronica - Texas Instruments WL1835MOD & Silicon Labs EFR32xG21 @ BlackHat USA 2020 • "Finding New Bluetooth Low Energy Exploits via Reverse Engineering <u>Multiple Vendors' Firmwares"</u>

• Xeno - Realtek RTL8761B* RE @ Hardwear.io Nov 2025 • "Reverse engineering Realtek RTL8761B* Bluetooth chips, to make better <u>Bluetooth security tools & classes"</u>

## Slide 5

**How much faster could we do prior work now?** • Investigated local LLMs in October 2025 (with highest-end Apple M4 Max) & April 2026 (with highest-end Apple M5 Max)

• Results were _underwhelming!_ • Wanted to re-investigate once frontier models started talking up their exploit capabilities

## Slide 6

**Goal: LLM-driven RE tool To find and rename interesting functions/variables/structures** • LLM should be able to help the analyst answer questions like: • Which code is responsible for sending packet _FOO_ over the air? • Which code is responsible for receiving packet _BAR_ over the air?

   - Which code interfaces between the Host and Controller?

- Non-goal: Model benchmarking/comparison • Initial work done on Opus 4.6 -> 4.7 -> 4.8 and then moved to GPT 5.6 Sol

## Slide 7

**How to connect LLM to existing RE tools? MCP! Model Context Protocol** • MCP (for our purposes) is basically just a mechanism to describe "tools" in a way that the LLM can call them (in practice, it's just a passthrough to an API call, explaining what parameters to pass)

Just needs a "run_inline_script" tool!

<u>Gh</u> ~~<u>i</u>~~ <u>draMCP</u>

<u>pygh</u> ~~<u>i</u>~~ <u>dra</u> ~~-~~ <u>mcp gh</u> ~~<u>i</u>~~ <u>dra</u> ~~-~~ <u>mcp</u>

<u>https://github.com/lauriewired/ghidramcp https://github.com/bethington/ghidra-mcp https://github.com/clearbluejar/pyghidra-mcp</u>

Image from https://malcolmsmusings.org/2023/09/04/the-goldilocks-principle/

## Slide 8

"Rename functions that are responsible for sending Link Layer Control PDUs." Ghidra (headless or GUI) <u>MCP MCP</u> pyghidra library Client Server pyghidra-mcp CLI application

###### Ghidra project

John McIntosh's original blog post about pyghidra-mcp: https://clearbluejar.github.io/posts/pyghidra-mcp-headless-ghidra-mcp-server-for-project-wide-multi-binary-analysis/

## Slide 9

"Rename functions that are responsible for sending Link Layer Control PDUs." Ghidra (headless or GUI) <u>MCP MCP</u> pyghidra library Client Server pyghidra-mcp CLI application {tools/list}

###### Ghidra project

John McIntosh's original blog post about pyghidra-mcp: https://clearbluejar.github.io/posts/pyghidra-mcp-headless-ghidra-mcp-server-for-project-wide-multi-binary-analysis/

## Slide 10

"Rename functions that are responsible for sending Link Layer Control PDUs." Ghidra (headless or GUI) <u>MCP MCP</u> pyghidra library Client Server pyghidra-mcp CLI application

{tools/list}

###### Ghidra project

John McIntosh's original blog post about pyghidra-mcp: https://clearbluejar.github.io/posts/pyghidra-mcp-headless-ghidra-mcp-server-for-project-wide-multi-binary-analysis/

## Slide 11

"Rename functions that are responsible for sending Link Layer Control PDUs."

Ghidra (headless or GUI) pyghidra library pyghidra-mcp CLI application

<u>MCP MCP</u> Client Server

{tools/list} {list_functions, ...}

###### Ghidra project

John McIntosh's original blog post about pyghidra-mcp: https://clearbluejar.github.io/posts/pyghidra-mcp-headless-ghidra-mcp-server-for-project-wide-multi-binary-analysis/

## Slide 12

"Rename functions that are responsible for sending Link Layer Control PDUs." Ghidra (headless or GUI)

<u>MCP MCP</u> pyghidra library Client Server pyghidra-mcp CLI application

{tools/list}

###### Ghidra project

{list_functions, ...}

John McIntosh's original blog post about pyghidra-mcp: https://clearbluejar.github.io/posts/pyghidra-mcp-headless-ghidra-mcp-server-for-project-wide-multi-binary-analysis/

## Slide 13

"Rename functions that are responsible for sending Link Layer Control PDUs." Ghidra (headless or GUI)

<u>MCP MCP</u> pyghidra library Client Server pyghidra-mcp CLI application

{tools/list}

###### Ghidra project

{list_functions, ...} {list_functions}

John McIntosh's original blog post about pyghidra-mcp: https://clearbluejar.github.io/posts/pyghidra-mcp-headless-ghidra-mcp-server-for-project-wide-multi-binary-analysis/

## Slide 14

"Rename functions that are responsible for sending Link Layer Control PDUs." Ghidra (headless or GUI) <u>MCP MCP</u> pyghidra library Client Server pyghidra-mcp CLI application

{tools/list}

###### Ghidra project

{list_functions, ...}

{list_functions}

John McIntosh's original blog post about pyghidra-mcp: https://clearbluejar.github.io/posts/pyghidra-mcp-headless-ghidra-mcp-server-for-project-wide-multi-binary-analysis/

## Slide 15

"Rename functions that are responsible for sending Link Layer Control PDUs." Ghidra (headless or GUI) <u>MCP MCP</u> pyghidra library Client Server pyghidra-mcp CLI application

{tools/list}

###### Ghidra project

{list_functions, ...}

{list_functions} {Func1, Func2, ...}

John McIntosh's original blog post about pyghidra-mcp: https://clearbluejar.github.io/posts/pyghidra-mcp-headless-ghidra-mcp-server-for-project-wide-multi-binary-analysis/

## Slide 16

"Rename functions that are responsible for sending Link Layer Control PDUs." Ghidra (headless or GUI) <u>MCP MCP</u> pyghidra library Client Server pyghidra-mcp CLI application

{tools/list}

###### Ghidra project

{list_functions, ...}

{list_functions}

{Func1, Func2, ...}

John McIntosh's original blog post about pyghidra-mcp: https://clearbluejar.github.io/posts/pyghidra-mcp-headless-ghidra-mcp-server-for-project-wide-multi-binary-analysis/

## Slide 17

#### **YOLOing it Initial prompt which yielded surprisingly good results!**

The code which is being analyzed is for a Realtek USB dongle which has a Bluetooth Controller (in the Bluetooth "Host Controller Interface" sense of the word "Controller", meaning the code which is not on the host). The code therefore must handle Bluetooth HCI, LMP, and LLCP protocols on the Controller, because those are functionality which must exist on the Controller according to the Bluetooth specification.

Download all the decompiled code for all of the functions. For each function create a markdown file which describes roughly what the function does, and whether it could be related to handling of HCI, LMP, or LLCP code. If you find code which looks like it is doing dispatching of HCI commands, LMP opcodes, or LLCP opcodes, then go back and see what other code it references, and update the descriptions in markdown files for whether you think the code may be related to handling those types of over-the-air packets, or HCI commands (coming from the Host) or HCI events (going from the Controller to the Host).

Once you are done downloading all the decompiled code and writing all the markdown files, do a secondary pass where you specifically look for whether you found the HCI, LMP, or LLCP dispatchers. If you did, do another pass over functions that are called by the dispatchers, to determine what types of packets or commands/events they handle.

At the end of the analysis, create a list of proposed functions to rename based on your understanding of their functionality as it pertains to HCI, LMP, or LLCP. Print the list and wait for approval before updating function names in the code based on the list.

## Slide 18

#### **YOLOing it Initial prompt which yielded surprisingly good results!**

The code which is being analyzed is for a Realtek USB dongle which has a Bluetooth Controller (in the Bluetooth "Host Controller Interface" sense of the word "Controller", meaning the code which is not on the host). The code therefore must handle Bluetooth HCI, LMP, and LLCP protocols on the Controller, because those are functionality which must exist on the Controller according to the Bluetooth specification.

Download all the decompiled code for all of the functions. For each function create a markdown file which describes roughly what the function does, and whether it could be related to handling of HCI, LMP, or LLCP code. If you find code which looks like it is doing dispatching of HCI commands, LMP opcodes, or LLCP opcodes, then go back and see what other code it Don't try to read this right now, it's just for demonstration / historical reference references, and update the descriptions in markdown files for whether you think the code may be related to handling those types of over-the-air packets, or HCI commands (coming from the Host) or HCI events (going from the Controller to the Host).

Once you are done downloading all the decompiled code and writing all the markdown files, do a secondary pass where you specifically look for whether you found the HCI, LMP, or LLCP dispatchers. If you did, do another pass over functions that are called by the dispatchers, to determine what types of packets or commands/events they handle.

At the end of the analysis, create a list of proposed functions to rename based on your understanding of their functionality as it pertains to HCI, LMP, or LLCP. Print the list and wait for approval before updating function names in the code based on the list.

## Slide 19

#### **Spec knowledge → Prompts → Skill (1)**

• We created a large text file of all the various prompts we'd want the LLM to do, to find specific information, or to improve the general readability of the final decompiled code • Asked Claude "What's the best way to structure all these queries in this file to ask an LLM to execute them all, some sequentially, and some in parallel?"

- It said to create a Skill

   - And that it has a /skill-creator skill to create skills

      - So we said "Make it so!"

## Slide 20

**Mad skillz! LLM skills were new to us, so maybe they're still new to you...** • Folder in ~/.claude/skills or ~/.codex/skills where the folder name (like "bt-recontroller") is how you invoke the skill with a / prefix (like /bt-re-controller) from within the LLM interface

• SKILL.md at root of the folder describes what to do, when to do it, and how to do it • Can either be explicitly invoked or found by the LLM's when it's trying to do something and the details within the SKILL.md describe the skill as pertinent to the task

- _Our skills are meant to be explicitly invoked_

## Slide 21

"/bt-re-controller <path to Ghidra project>"

Ghidra (headless or GUI)

Ghidra project

~/.claude/skills/bt-re-controller

SKILL.md prompts/P1<name>.md prompts/P2<name>.md ... references/lmp_opcodes.md references/llcp_opcodes.md

<u>MCP MCP</u> pyghidra library Client Server pyghidra-mcp CLI application

... scripts/run.sh

## Slide 22

#### **The skill needs** **_decompilable_ code to start**

• We have not automated the process of getting from raw binaries to code which Ghidra views as valid and for which there are many functions correctly decompiling

- LLMs can help clean up the code to get you to decompilable code, but building that into the skill is out of scope for now • Originally for the Realtek work, Xeno asked Veronica to make a script for him which helped, due to Ghidra not handling MIPS16e assembly well

- • Similar issues occur on other niche architectures like ARC variants

## Slide 23

## Specification-driven "Waypoints" 📍

## Slide 24

**Encoding "Waypoints" A pin** 📍 **in a map obscured by the fog of war** • Waypoints are _specification-driven_ behavior which needs to manifest in code _somewhere_ • Therefore humans should be able to find the code while REing • Therefore humans can encode into LLM code searches • Let's visualize Waypoints in the context of Bluetooth protocol stacks...

## Slide 25

###### BLE & BC Host

Host Controller Interface (HCI)

📍

Parse incoming HCI

OGF 1 OGF 2 OGF 3 OGF 4 OGF 5 OGF 5 OGF 8 OGF 3F

Link Policy Controller & Baseband Cmds Informational Status Testing LE Controller Cmds Vendor-Specific Cmds

Link Control

📍

OCF 0x19

"send_LMP_NAME_RES_packet()" "send_LMP_ACCEPTED_packet()" "send_LMP_NOT_ACCEPTED_packet()" ... Link Layer (LL)

BLE Radio Physical Layer (PHY)

HCI_Remote_Name_Request 📍 "send_LMP_NAME_REQ_packet()" Link Manager Protocol (LMP) 📍 "send_LMP_packet()" BC Radio Physical Layer (PHY)

###### BLE & BC Controller

**Veronica & Xeno Kovah, Dark Mentor LLC, CC-BY_SA**

## Slide 26

###### BLE & BC Host

Host Controller Interface (HCI)📍 Parse incoming HCI 📍 OGF 1 OGF 2 OGF 3 OGF 4 OGF 5 OGF 5 OGF 8 OGF 3F

Link Control

Link Policy Controller & Baseband Cmds Informational Status Testing LE Controller Cmds Vendor-Specific Cmds

📍

OCF 0x19

"send_LMP_NAME_RES_packet()" "send_LMP_ACCEPTED_packet()" "send_LMP_NOT_ACCEPTED_packet()"

... Link Layer (LL)

BLE Radio Physical Layer (PHY)

HCI_Remote_Name_Request 📍 "send_LMP_NAME_REQ_packet()" Link Manager Protocol (LMP) 📍 "send_LMP_packet()" BC Radio Physical Layer (PHY)

###### BLE & BC Controller

**Veronica & Xeno Kovah, Dark Mentor LLC, CC-BY_SA**

## Slide 27

BLE & BC Host Host Controller Interface (HCI)📍 Parse incoming HCI OGF 1 OGF 2 OGF 3 OGF 4 OGF 5 OGF 5 Link Control Link Policy Controller & Baseband Cmds Informational Status Testing

OGF 5 OGF 8 OGF 3F Testing LE Controller Cmds Vendor-Specific Cmds

📍

OCF 0x19 "send_LMP_NAME_RES_packet()" HCI_Remote_Name_Request "send_LMP_ACCEPTED_packet()" 📍 "send_LMP_NOT_ACCEPTED_packet()" "send_LMP_NAME_REQ_packet()" ... Link Layer (LL) Link Manager Protocol (LMP) 📍 "send_LMP_packet()" BLE Radio Physical Layer (PHY) BC Radio Physical Layer (PHY)

"send_LMP_NAME_RES_packet()" "send_LMP_ACCEPTED_packet()" "send_LMP_NOT_ACCEPTED_packet()"

BLE Radio Physical Layer (PHY)

###### BLE & BC Controller

**Veronica & Xeno Kovah, Dark Mentor LLC, CC-BY_SA**

## Slide 28

###### BLE & BC Host

Host Controller Interface (HCI)📍 Parse incoming HCI 📍 OGF 1 OGF 2 OGF 3 OGF 4 OGF 5 OGF 5 OGF 8 OGF 3F Link Control Link Policy Controller & Baseband Cmds Informational Status Testing LE Controller Cmds Vendor-Specific Cmds

📍

OCF 0x19

"send_LMP_NAME_RES_packet()" "send_LMP_ACCEPTED_packet()" "send_LMP_NOT_ACCEPTED_packet()" ... Link Layer (LL)

BLE Radio Physical Layer (PHY)

HCI_Remote_Name_Request 📍 "send_LMP_NAME_REQ_packet()" Link Manager Protocol (LMP) 📍 "send_LMP_packet()" BC Radio Physical Layer (PHY)

###### BLE & BC Controller

**Veronica & Xeno Kovah, Dark Mentor LLC, CC-BY_SA**

## Slide 29

###### BLE & BC Host

Host Controller Interface (HCI)📍 Parse incoming HCI 📍 OGF 1 OGF 2 OGF 3 OGF 4 OGF 5 OGF 5 Link Control Link Policy Controller & Baseband Cmds Informational Status Testing

OGF 5 OGF 8 OGF 3F Testing LE Controller Cmds Vendor-Specific Cmds

Testing

OCF 0x19

"send_LMP_NAME_RES_packet()" "send_LMP_ACCEPTED_packet()" "send_LMP_NOT_ACCEPTED_packet()"

... Link Layer (LL)

BLE Radio Physical Layer (PHY)

HCI_Remote_Name_Request 📍 "send_LMP_NAME_REQ_packet()" Link Manager Protocol (LMP) 📍 "send_LMP_packet()" BC Radio Physical Layer (PHY)

###### BLE & BC Controller

**Veronica & Xeno Kovah, Dark Mentor LLC, CC-BY_SA**

## Slide 30

###### BLE & BC Host

Host Controller Interface (HCI)📍 Parse incoming HCI 📍 OGF 1 OGF 2 OGF 3 OGF 4 OGF 5 OGF 5 OGF 8 OGF 3F Link Control Link Policy Controller & Baseband Cmds Informational Status Testing LE Controller Cmds Vendor-Specific Cmds 📍 OCF 0x19 "send_LMP_NAME_RES_packet()" HCI_Remote_Name_Request "send_LMP_ACCEPTED_packet()" 📍

"send_LMP_NAME_RES_packet()" "send_LMP_ACCEPTED_packet()" "send_LMP_NOT_ACCEPTED_packet()" ... Link Layer (LL)

HCI_Remote_Name_Request 📍 "send_LMP_NAME_REQ_packet()" Link Manager Protocol (LMP) 📍 "send_LMP_packet()" BC Radio Physical Layer (PHY)

BLE Radio Physical Layer (PHY)

BLE & BC Controller

**Veronica & Xeno Kovah, Dark Mentor LLC, CC-BY_SA**

## Slide 31

###### BLE & BC Host

Host Controller Interface (HCI)📍 Parse incoming HCI 📍 OGF 1 OGF 2 OGF 3 OGF 4 OGF 5 OGF 5 OGF 8 OGF 3F Link Control Link Policy Controller & Baseband Cmds Informational Status Testing LE Controller Cmds Vendor-Specific Cmds

📍

OCF 0x19 "send_LMP_NAME_RES_packet()" HCI_Remote_Name_Request "send_LMP_ACCEPTED_packet()" "send_LMP_NOT_ACCEPTED_packet()" "send_LMP_NAME_REQ_packet()" ... Link Layer (LL) Link Manager Protocol (LMP) 📍 "send_LMP_packet()" BLE Radio Physical Layer (PHY) BC Radio Physical Layer (PHY)

###### BLE & BC Controller

**Veronica & Xeno Kovah, Dark Mentor LLC, CC-BY_SA**

## Slide 32

###### BLE & BC Host

Host Controller Interface (HCI)📍 Parse incoming HCI 📍 OGF 1 OGF 2 OGF 3 OGF 4 OGF 5 OGF 5 OGF 8 OGF 3F Link Control Link Policy Controller & Baseband Cmds Informational Status Testing LE Controller Cmds Vendor-Specific Cmds

📍

OCF 0x19 "send_LMP_NAME_RES_packet()" HCI_Remote_Name_Request "send_LMP_ACCEPTED_packet()" 📍 "send_LMP_NOT_ACCEPTED_packet()" "send_LMP_NAME_REQ_packet()" ... Link Layer (LL) Link Manager Protocol (LMP) 📍 "send_LMP_packet()" BLE Radio Physical Layer (PHY) BC Radio Physical Layer (PHY)

BLE & BC Controller

**Veronica & Xeno Kovah, Dark Mentor LLC, CC-BY_SA**

## Slide 33

###### BLE & BC Host

Host Controller Interface (HCI)📍 Parse incoming HCI 📍 OGF 1 OGF 2 OGF 3 OGF 4 OGF 5 OGF 5 OGF 8 OGF 3F Link Control Link Policy Controller & Baseband Cmds Informational Status Testing LE Controller Cmds Vendor-Specific Cmds 📍 OCF 0x19 "send_LMP_NAME_RES_packet()" HCI_Remote_Name_Request "send_LMP_ACCEPTED_packet()" 📍 "send_LMP_NOT_ACCEPTED_packet()" "send_LMP_NAME_REQ_packet()" ... Link Layer (LL) Link Manager Protocol (LMP) "send_LMP_packet()" BLE Radio Physical Layer (PHY) BC Radio Physical Layer (PHY)

BLE & BC Controller

**Veronica & Xeno Kovah, Dark Mentor LLC, CC-BY_SA**

## Slide 34

###### BLE & BC Host

Host Controller Interface (HCI)📍 Parse incoming HCI 📍 OGF 1 OGF 2 OGF 3 OGF 4 OGF 5 OGF 5 OGF 8 OGF 3F Link Control Link Policy Controller & Baseband Cmds Informational Status Testing LE Controller Cmds Vendor-Specific Cmds

📍

"send_LMP_NAME_RES_packet()" "send_LMP_ACCEPTED_packet()" "send_LMP_NOT_ACCEPTED_packet()" ... Link Layer (LL) BLE Radio Physical Layer (PHY)

OCF 0x19 HCI_Remote_Name_Request 📍 "send_LMP_NAME_REQ_packet()" Link Manager Protocol (LMP) 📍 "send_LMP_packet()" BC Radio Physical Layer (PHY)

BLE & BC Controller

**Veronica & Xeno Kovah, Dark Mentor LLC, CC-BY_SA**

## Slide 35

###### BLE & BC Host

Host Controller Interface (HCI)📍 Parse incoming HCI 📍 OGF 1 OGF 2 OGF 3 OGF 4 OGF 5 OGF 5 OGF 8 OGF 3F Link Control Link Policy Controller & Baseband Cmds Informational Status Testing LE Controller Cmds Vendor-Specific Cmds

📍

"send_LMP_NAME_RES_packet()" "send_LMP_ACCEPTED_packet()" "send_LMP_NOT_ACCEPTED_packet()" ... Link Layer (LL) BLE Radio Physical Layer (PHY)

OCF 0x19 HCI_Remote_Name_Request 📍 "send_LMP_NAME_REQ_packet()" Link Manager Protocol (LMP) 📍 "send_LMP_packet()" BC Radio Physical Layer (PHY) BLE & BC Controller

**Veronica & Xeno Kovah, Dark Mentor LLC, CC-BY_SA**

## Slide 36

###### BLE & BC Host

Host Controller Interface (HCI)📍 Parse incoming HCI 📍 OGF 1 OGF 2 OGF 3 OGF 4 OGF 5 OGF 5 Link Control Link Policy Controller & Baseband Cmds Informational Status Testing

OGF 1 OGF 2 OGF 3 OGF 4 OGF 5 OGF 5 OGF 8 OGF 3F Link Control Link Policy Controller & Baseband Cmds Informational Status Testing LE Controller Cmds Vendor-Specific Cmds 📍 OCF 0x19 📍 "send_LMP_NAME_RES_packet()" 📍 HCI_Remote_Name_Request "send_LMP_ACCEPTED_packet()" 📍 📍 "send_LMP_NOT_ACCEPTED_packet()" "send_LMP_NAME_REQ_packet()" ... Link Layer (LL) Link Manager Protocol (LMP) 📍 "send_LMP_packet()" BLE Radio Physical Layer (PHY) BC Radio Physical Layer (PHY)

BLE & BC Controller

**Veronica & Xeno Kovah, Dark Mentor LLC, CC-BY_SA**

## Slide 37

###### BLE & BC Host

Host Controller Interface (HCI)📍 Parse incoming HCI 📍 OGF 1 OGF 2 OGF 3 OGF 4 OGF 5 OGF 5 OGF 8 OGF 3F Link Control Link Policy Controller & Baseband Cmds Informational Status Testing LE Controller Cmds Vendor-Specific Cmds

Testing LE Controller Cmds Vendor-Specific Cmds

📍

OCF 0x19 "send_LMP_NAME_RES_packet()" 📍 HCI_Remote_Name_Request "send_LMP_ACCEPTED_packet()" 📍 📍 "send_LMP_NOT_ACCEPTED_packet()" "send_LMP_NAME_REQ_packet()" ... Link Layer (LL) Link Manager Protocol (LMP) 📍 "send_LMP_packet()" BLE Radio Physical Layer (PHY) BC Radio Physical Layer (PHY) BLE & BC Controller

**Veronica & Xeno Kovah, Dark Mentor LLC, CC-BY_SA**

## Slide 38

###### BLE Host Applications

###### BC Host

Purpose-specific Profiles (e.g. Mesh, OTP, HRP, etc) Purpose-specific Profiles (e.g. SPP, A2DP, BIP, etc) RFCOMM Bluetooth Network Encapsulation Protocol

Bluetooth Network Encapsulation Protocol

Generic Access Profile (GAP) Generic Attribute Profile (GATT)

Attribute Protocol (ATT) Security Manager Protocol (SMP) Logical Link Control and Adaptation Protocol (L2CAP) Host Controller Interface (HCI)

Service Discovery Protocol (SDP)

Link Layer (LL) BLE Radio Physical Layer (PHY)

Link Manager Protocol (LMP) BC Radio Physical Layer (PHY)

###### BLE Controller

BC Controller

**Veronica & Xeno Kovah, Dark Mentor LLC, CC-BY_SA**

## Slide 39

###### BLE Host

###### BC Host

Host Controller Interface (HCI)

Link Layer (LL) BLE Radio Physical Layer (PHY)

Link Manager Protocol (LMP) BC Radio Physical Layer (PHY)

BLE Controller

BC Controller

**Veronica & Xeno Kovah, Dark Mentor LLC, CC-BY_SA**

## Slide 40

###### BLE Host

BC Host

Host Controller Interface (HCI)

Link Layer (LL) BLE Radio Physical Layer (PHY)

Link Manager Protocol (LMP) BC Radio Physical Layer (PHY)

BLE Controller

BC Controller

**Veronica & Xeno Kovah, Dark Mentor LLC, CC-BY_SA**

## Slide 41

###### BLE Host

BC Host

Host Controller Interface (HCI)

Link Layer (LL) BLE Radio Physical Layer (PHY)

Link Manager Protocol (LMP) BC Radio Physical Layer (PHY)

BLE Controller

BC Controller

**Veronica & Xeno Kovah, Dark Mentor LLC, CC-BY_SA**

## Slide 42

###### BLE & BC Host

Host Controller Interface (HCI)

Link Layer (LL) BLE Radio Physical Layer (PHY)

Link Manager Protocol (LMP) BC Radio Physical Layer (PHY)

BLE & BC Controller

**Veronica & Xeno Kovah, Dark Mentor LLC, CC-BY_SA**

## Slide 43

###### BLE & BC Host

Send HCI
commands from
the BT spec!

Host Controller Interface (HCI)

Link Layer (LL)

Link Manager Protocol (LMP)

BLE Radio Physical Layer (PHY)

BC Radio Physical Layer (PHY)

BLE & BC Controller

**Veronica & Xeno Kovah, Dark Mentor LLC, CC-BY_SA**

## Slide 44

###### BLE & BC Host

Send HCI commands from the BT spec! HCI_LE_Set_Random_Address

Host Controller Interface (HCI)

Link Layer (LL)

Link Manager Protocol (LMP)

BLE Radio Physical Layer (PHY)

BC Radio Physical Layer (PHY)

BLE & BC Controller

**Veronica & Xeno Kovah, Dark Mentor LLC, CC-BY_SA**

## Slide 45

###### BLE & BC Host

Send HCI commands from the BT spec!

###### HCI_LE_Set_Random_Address

HCI_Inquiry

Host Controller Interface (HCI)

Link Layer (LL)

Link Manager Protocol (LMP)

BLE Radio Physical Layer (PHY)

BC Radio Physical Layer (PHY)

BLE & BC Controller

**Veronica & Xeno Kovah, Dark Mentor LLC, CC-BY_SA**

## Slide 46

###### Realtek Driver

###### BLE & BC Host

Host Controller Interface (HCI)

Link Layer (LL) BLE Radio Physical Layer (PHY)

Link Manager Protocol (LMP)

BC Radio Physical Layer (PHY)

BLE & BC Controller

**Veronica & Xeno Kovah, Dark Mentor LLC, CC-BY_SA**

## Slide 47

###### Realtek Driver

Vendor-Specific Command (VSC) Group (OGF) = 0x3F (always) Command (OCF) = 0x020 "HCI_VENDOR_DOWNLOAD"

###### BLE & BC Host

Host Controller Interface (HCI)

Link Layer (LL)

BLE Radio Physical Layer (PHY)

BLE & BC Controller

Link Manager Protocol (LMP) BC Radio Physical Layer (PHY)

**Veronica & Xeno Kovah, Dark Mentor LLC, CC-BY_SA**

## Slide 48

###### BLE & BC Host

Host Controller Interface (HCI)

Link Layer (LL)

Link Manager Protocol (LMP)

BLE Radio Physical Layer (PHY)

BC Radio Physical Layer (PHY)

BLE & BC Controller

**Veronica & Xeno Kovah, Dark Mentor LLC, CC-BY_SA**

## Slide 49

###### BLE & BC Host

Host Controller Interface (HCI) Parse incoming HCI

OGF 1 OGF 2 OGF 3 OGF 4 OGF 5 OGF 6 OGF 8 OGF 3F Link Control Link Policy Controller & Baseband Cmds Informational Status Testing LE Controller Cmds Vendor-Specific Cmds Per the spec!

Link Layer (LL)

BLE Radio Physical Layer (PHY)

BLE & BC Controller

Link Manager Protocol (LMP) BC Radio Physical Layer (PHY)

**Veronica & Xeno Kovah, Dark Mentor LLC, CC-BY_SA**

## Slide 50

###### BLE & BC Host

WAYPOINTS !
Host Controller Interface (HCI)
📍
Parse incoming HCI
📍 📍 📍 📍 📍 📍 📍 📍
OGF 1  OGF 2  OGF 3  OGF 4  OGF 5  OGF 6  OGF 8  OGF 3F
Link Control Link Policy Controller & Baseband Cmds Informational Status Testing LE Controller Cmds Vendor-Specific Cmds
Per the spec!

Link Layer (LL) BLE Radio Physical Layer (PHY)

###### BLE & BC Controller

Link Manager Protocol (LMP) BC Radio Physical Layer (PHY)

**Veronica & Xeno Kovah, Dark Mentor LLC, CC-BY_SA**

## Slide 51

###### BLE & BC Host

Host Controller Interface (HCI) Parse incoming HCI

OGF 1 OGF 2 OGF 3 OGF 4 OGF 5 OGF 5 OGF 8 OGF 3F Link Control Link Policy Controller & Baseband Cmds Informational Status Testing LE Controller Cmds Vendor-Specific Cmds

Link Layer (LL)

Link Manager Protocol (LMP)

BLE Radio Physical Layer (PHY)

BC Radio Physical Layer (PHY)

BLE & BC Controller

**Veronica & Xeno Kovah, Dark Mentor LLC, CC-BY_SA**

## Slide 52

###### BLE & BC Host

Host Controller Interface (HCI) Parse incoming HCI

OGF 1  OGF 2  OGF 3  OGF 4  OGF 5  OGF 5  OGF 8  OGF 3F
Link Control Link Policy Controller & Baseband Cmds Informational Status Testing LE Controller Cmds Vendor-Specific Cmds
OCF 0x45
OCF 1 OCF 2 ...
Per the spec!
OCF 1 OCF 3 ... OCF 0x11
Link Layer (LL) Link Manager Protocol (LMP)
BLE Radio Physical Layer (PHY) BC Radio Physical Layer (PHY)
BLE & BC Controller
Veronica & Xeno Kovah, Dark Mentor LLC, CC-BY_SA
HCI_Inquiry  HCI_Inquiry_Cancel
HCI_Hold_Mode  HCI_Sniff_Mode  HCI_Sniff_Subrating
HCI_Remote_OOB_Extended_Data_Request_Reply

**Veronica & Xeno Kovah, Dark Mentor LLC, CC-BY_SA**

## Slide 53

###### BLE & BC Host

WAYPOINTS !
Host Controller Interface (HCI)
Parse incoming HCI
📍
OGF 1  OGF 2  OGF 3  OGF 4  OGF 5  OGF 5  OGF 8  OGF 3F
Link Control Link Policy Controller & Baseband Cmds Informational Status Testing LE Controller Cmds Vendor-Specific Cmds
OCF 0x45
OCF 1 OCF 2 ...
Per the spec!
OCF 1 OCF 3 ... OCF 0x11
Link Layer (LL) Link Manager Protocol (LMP)
BLE Radio Physical Layer (PHY) BC Radio Physical Layer (PHY)
BLE & BC Controller
Veronica & Xeno Kovah, Dark Mentor LLC, CC-BY_SA
HCI_Inquiry  HCI_Inquiry_Cancel
HCI_Hold_Mode  HCI_Sniff_Mode  HCI_Sniff_Subrating
HCI_Remote_OOB_Extended_Data_Request_Reply

**Veronica & Xeno Kovah, Dark Mentor LLC, CC-BY_SA**

## Slide 54

###### BLE & BC Host

Host Controller Interface (HCI) Parse incoming HCI

OGF 1 OGF 2 OGF 3 OGF 4 OGF 5 OGF 5 OGF 8 OGF 3F Link Control Link Policy Controller & Baseband Cmds Informational Status Testing LE Controller Cmds Vendor-Specific Cmds

Link Layer (LL)

Link Manager Protocol (LMP)

BLE Radio Physical Layer (PHY)

BC Radio Physical Layer (PHY)

BLE & BC Controller

**Veronica & Xeno Kovah, Dark Mentor LLC, CC-BY_SA**

## Slide 55

###### BLE & BC Host

Host Controller Interface (HCI) Parse incoming HCI

OGF 1 OGF 2 Link Control Link Policy

Link Policy

OGF 3 OGF 4 OGF 5 OGF 5 Controller & Baseband Cmds Informational Status Testing

OGF 5 OGF 8

OGF 8 OGF 3F LE Controller Cmds Vendor-Specific Cmds

OCF 0x19 HCI_Remote_Name_Request

Link Layer (LL)

BLE Radio Physical Layer (PHY)

Link Manager Protocol (LMP) BC Radio Physical Layer (PHY)

BLE & BC Controller

**Veronica & Xeno Kovah, Dark Mentor LLC, CC-BY_SA**

## Slide 56

###### BLE & BC Host

Host Controller Interface (HCI) Parse incoming HCI

OGF 1 OGF 2 Link Control Link Policy

Link Policy

OGF 3 OGF 4 OGF 5 Controller & Baseband Cmds Informational Status

OGF 5 OGF 8

OGF 8 OGF 3F LE Controller Cmds Vendor-Specific Cmds

Testing

OCF 0x19 HCI_Remote_Name_Request

Link Layer (LL)

BLE Radio Physical Layer (PHY)

"send_LMP_NAME_REQ_packet()" Link Manager Protocol (LMP) BC Radio Physical Layer (PHY)

BLE & BC Controller

**Veronica & Xeno Kovah, Dark Mentor LLC, CC-BY_SA**

## Slide 57

###### BLE & BC Host

Host Controller Interface (HCI) Parse incoming HCI

OGF 1 OGF 2 OGF 3 OGF 4 OGF 5 OGF 5 OGF 8 OGF 3F Link Control Link Policy Controller & Baseband Cmds Informational Status Testing LE Controller Cmds Vendor-Specific Cmds

📍

WAYPOINTS ~~!~~

This, and other relationships like it, help us seed the analysis of other areas of the code Link Layer (LL) BLE Radio Physical Layer (PHY) BLE & BC Controller

OCF 0x19 HCI_Remote_Name_Request 📍 "send_LMP_NAME_REQ_packet()" Link Manager Protocol (LMP) BC Radio Physical Layer (PHY)

**Veronica & Xeno Kovah, Dark Mentor LLC, CC-BY_SA**

## Slide 58

###### BLE & BC Host

Host Controller Interface (HCI) Parse incoming HCI

OGF 1 OGF 2 Link Control Link Policy

Link Policy

OGF 3 OGF 4 OGF 5 Controller & Baseband Cmds Informational Status

OGF 5 OGF 8

OGF 8 OGF 3F LE Controller Cmds Vendor-Specific Cmds

Testing

Link Layer (LL)

BLE Radio Physical Layer (PHY)

OCF 0x19 HCI_Remote_Name_Request 📍 "send_LMP_NAME_REQ_packet()" Link Manager Protocol (LMP) BC Radio Physical Layer (PHY)

BLE & BC Controller

**Veronica & Xeno Kovah, Dark Mentor LLC, CC-BY_SA**

## Slide 59

###### BLE & BC Host

Host Controller Interface (HCI) Parse incoming HCI

OGF 1 OGF 2 OGF 3 OGF 4 OGF 5 OGF 5 OGF 8 OGF 3F Link Control Link Policy Controller & Baseband Cmds Informational Status Testing LE Controller Cmds Vendor-Specific Cmds OCF 0x19 📍 "send_LMP_NAME_RES_packet()" 📍 HCI_Remote_Name_Request "send_LMP_ACCEPTED_packet()" 📍 📍 "send_LMP_NOT_ACCEPTED_packet()" "send_LMP_NAME_REQ_packet()" ... Link Layer (LL) Link Manager Protocol (LMP) 📍 "send_LMP_packet()" BLE Radio Physical Layer (PHY) BC Radio Physical Layer (PHY) BLE & BC Controller

**Veronica & Xeno Kovah, Dark Mentor LLC, CC-BY_SA**

## Slide 60

BLE & BC Host Spec-driven "Waypoints" are super-useful! Host Controller Interface (HCI)📍 Parse incoming HCI 📍

OGF 1 OGF 2 OGF 3 OGF 4 OGF 5 OGF 5 OGF 8 OGF 3F Link Control Link Policy Controller & Baseband Cmds Informational Status Testing LE Controller Cmds Vendor-Specific Cmds

📍

OCF 0x19 "send_LMP_NAME_RES_packet()" 📍 HCI_Remote_Name_Request "send_LMP_ACCEPTED_packet()" 📍 📍 "send_LMP_NOT_ACCEPTED_packet()" "send_LMP_NAME_REQ_packet()" ... Link Layer (LL) Link Manager Protocol (LMP) 📍 "send_LMP_packet()" BLE Radio Physical Layer (PHY) BC Radio Physical Layer (PHY) BLE & BC Controller

**Veronica & Xeno Kovah, Dark Mentor LLC, CC-BY_SA**

## Slide 61

###### BLE & BC Host

Host Controller Interface (HCI) Parse incoming HCI

OGF 1 OGF 2 OGF 3 OGF 4 OGF 5 OGF 5 OGF 8 OGF 3F Link Control Link Policy Controller & Baseband Cmds Informational Status Testing LE Controller Cmds Vendor-Specific Cmds

Link Layer (LL)

Link Manager Protocol (LMP) BC Radio Physical Layer (PHY)

BLE Radio Physical Layer (PHY) BLE & BC Controller [1] https://github.com/darkmentorllc/BT_Security_VSC_DB

**Veronica & Xeno Kovah, Dark Mentor LLC, CC-BY_SA**

## Slide 62

###### BLE & BC Host

WAYPOINT ~~!~~ Host Controller Interface (HCI) Parse incoming HCI 📍 OGF 1 OGF 2 OGF 3 OGF 4 OGF 5 OGF 5 OGF 8 OGF 3F Link Control Link Policy Controller & Baseband Cmds Informational Status Testing LE Controller Cmds Vendor-Specific Cmds VSCs can be a mixture of documented & OCF 0x20 OCF 1 OCF 2 ... ... OCF N undocumented commands Link Layer (LL) Link Manager Protocol (LMP) BLE Radio Physical Layer (PHY) BC Radio Physical Layer (PHY) BLE & BC Controller [1] https://github.com/darkmentorllc/BT_Security_VSC_DB **Veronica & Xeno Kovah, Dark Mentor LLC, CC-BY_SA**

**Veronica & Xeno Kovah, Dark Mentor LLC, CC-BY_SA**

## Slide 63

###### BLE & BC Host

WAYPOINT !
Host Controller Interface (HCI)
Parse incoming HCI
📍
OGF 1  OGF 2  OGF 3  OGF 4  OGF 5  OGF 5  OGF 8  OGF 3F
Link Control Link Policy Controller & Baseband Cmds Informational Status Testing LE Controller Cmds Vendor-Specific Cmds
VSCs can be a mixture of  BT REs should care
documented &
about this  a lot , and
OCF 0x20
OCF 1 OCF 2 ... ... OCF N
undocumented commands
document them!  [1]
Link Layer (LL) Link Manager Protocol (LMP)
BLE Radio Physical Layer (PHY) BC Radio Physical Layer (PHY)
BLE & BC Controller
??? ???
Download_Patch ???

###### [1] https://github.com/darkmentorllc/BT_Security_VSC_DB

**Veronica & Xeno Kovah, Dark Mentor LLC, CC-BY_SA**

## Slide 64

#### **Spec knowledge → Prompts → Skill (2)**

- So what we _actually_ did was...

- We created a large text file of all the various prompts we'd want the LLM to do, to find specific information **_<u>related to Waypoints</u>_** <u>, or to improve the</u> general readability of the final decompiled code

   - And then had Claude turn that into a skill

## Slide 65

#### **Naive skill vs. performance-optimized skill**

• A naive skill would just linearly run prompts 1, 2, 3, 4....N • Optimized skills run some prompts in parallel; but the skill author needs to understand and account for dependencies • E.g. the prompt to search for HCI Commands (OCFs) should be _preceded_ by the prompt to search for HCI Groups (OGFs), not vice versa • E.g. we can run searches for LMP and LL completely in parallel because they don't relate to each other at all (two mutually-incompatible link layers for BLE vs. BC)

## Slide 66

###### **bt-re-controller — prompt dependency DAG (DUAL_MODE)**

 prep/cleanup   HCI   version+coverage   link-layer   structs
P2 P3 P4 P5
rename set mem stubs retype undefined4 fptrs log string inference find memcpy memset
P7 P6
consolidate p phase refresh bulk apply pointer type
H1
rename ogf dispatchers
H2
rename hci command handlers
H5 V1 B5_ADV B7_LMP B7_LL
discover cmd dispatch table extract ota spec version identify ble advertisement identify lmp frequency hopping identify ble channel selection
B1_LL B1_LMP S9_ADV
rename llcp packet functions rename lmp packet functions advertisement structs

## Slide 67

B1_LL B1_LMP S9_ADV
rename llcp packet functions rename lmp packet functions advertisement structs
B2_LL B6 B2_LMP
discover missing llcp handlers identify spec crypto primitives discover missing lmp handlers
H3 H4 B3_LL B3_LMP
type hci command args rename hci event handlers discover missing llcp fptr table discover missing lmp fptr table
S3_HCI V2_HCI B4_SCO V4_LL V3_LMP
structs hci globals crosscheck missing hci identify sco esco handlers crosscheck missing llcp crosscheck missing lmp
S1_HCI S8_SCO S2_LL S5_LL S2_LMP S4_LMP
structs hci cmd evt bodies esco structs structs llcp packet args structs ll globals structs lmp packet args structs lmp globals
S6
recursive arg propagation
S7 D1 D2
per connection arrays rename masked locals find malloc free
F2 E2 E3 E4 F1
rename hardcode return stubs rename struct unknown fields author labels and comments xref cluster naming apply basic data types

## Slide 68

version + coverage

prep / cleanup

HCI

link-layer

structs

P-phase prep
P2–P6 → P7 (non-BT)
H1 → H2
OGF dispatch + handlers
V1
spec down-select
H3 · H4 B1_LMP B1_LL
args · events LMP send/recv LLCP send/recv
B-extras V2_HCI B2_LMP B2_LL
B4 · B5 · B7 HCI coverage closure closure
B3_LMP B3_LL
fptr table fptr table
V3_LMP V4_LL
LMP coverage LLCP coverage
B6
crypto
struct creation (Batch 7)
S1–S5 · S8_SCO · S9_ADV
S6 S7
propagate args per-conn arrays
D1 · D2
masked locals · malloc/free
finishing pass
fields · labels · xrefs · types · F2 stubs (Batch 11, last)

## Slide 69

version + coverage

link-layer

prep / cleanup

HCI

structs

###### P-phase prep Generic non-BT-specifc prep workP2–P6 → P7 (non-BT)

H1 → H2
OGF dispatch + handlers
V1
spec down-select
H3 · H4 B1_LMP B1_LL
args · events LMP send/recv LLCP send/recv
B-extras V2_HCI B2_LMP B2_LL
B4 · B5 · B7 HCI coverage closure closure
B3_LMP B3_LL
fptr table fptr table
V3_LMP V4_LL
LMP coverage LLCP coverage
B6
crypto
struct creation (Batch 7)
S1–S5 · S8_SCO · S9_ADV
S6 S7
propagate args per-conn arrays
D1 · D2
masked locals · malloc/free
finishing pass
fields · labels · xrefs · types · F2 stubs (Batch 11, last)

## Slide 70

version + coverage

link-layer

prep / cleanup

HCI

structs

###### P-phase prep Generic non-BT-specifc prep workP2–P6 → P7 (non-BT)

H1 → H2
OGF dispatch + handlers
HCI-specific searching
V1
spec down-select
H3 · H4 B1_LMP B1_LL
args · events LMP send/recv LLCP send/recv
B-extras V2_HCI B2_LMP B2_LL
B4 · B5 · B7 HCI coverage closure closure
B3_LMP B3_LL
fptr table fptr table
V3_LMP V4_LL
LMP coverage LLCP coverage
B6
crypto
struct creation (Batch 7)
S1–S5 · S8_SCO · S9_ADV
S6 S7
propagate args per-conn arrays
D1 · D2
masked locals · malloc/free
finishing pass
fields · labels · xrefs · types · F2 stubs (Batch 11, last)

## Slide 71

version + coverage

link-layer

prep / cleanup

HCI

structs

###### P-phase prep Generic non-BT-specifc prep workP2–P6 → P7 (non-BT)

###### H1 → H2 OGF dispatch + handlers HCI-specific searching

###### V1 Downselect search targets based on BT spec versionspec down-select

H3 · H4 B1_LMP B1_LL
args · events LMP send/recv LLCP send/recv
B-extras V2_HCI B2_LMP B2_LL
B4 · B5 · B7 HCI coverage closure closure
B3_LMP B3_LL
fptr table fptr table
V3_LMP V4_LL
LMP coverage LLCP coverage
B6
crypto
struct creation (Batch 7)
S1–S5 · S8_SCO · S9_ADV
S6 S7
propagate args per-conn arrays
D1 · D2
masked locals · malloc/free
finishing pass
fields · labels · xrefs · types · F2 stubs (Batch 11, last)

## Slide 72

version + coverage

prep / cleanup

HCI

link-layer

structs

###### P-phase prep Generic non-BT-specifc prep workP2–P6 → P7 (non-BT)

H1 → H2 OGF dispatch + handlers HCI-specific searching

###### V1 Downselect search targets based on BT spec versionspec down-select

B-extras B4 · B5 · B7 Misc other BC/BLE searching

H3 · H4 B1_LMP B1_LL args · events LMP send/recv LLCP send/recv V2_HCI B2_LMP B2_LL HCI coverage closure closure More HCIBC LinkBLE LinkB3_LMP B3_LL specific Layer Layer fptr table fptr table searching searching searching V3_LMP V4_LL LMP coverage LLCP coverage B6 crypto struct creation (Batch 7) S1–S5 · S8_SCO · S9_ADV S6 S7 propagate args per-conn arrays D1 · D2 masked locals · malloc/free finishing pass fields · labels · xrefs · types · F2 stubs (Batch 11, last)

## Slide 73

prep / cleanup

HCI

version + coverage

link-layer

structs

###### P-phase prep Generic non-BT-specifc prep workP2–P6 → P7 (non-BT)

H1 → H2 OGF dispatch + handlers HCI-specific searching V1 Downselect search targets based on BT spec versionspec down-select

B-extras B4 · B5 · B7 Misc other BC/BLE searching

H3 · H4 B1_LMP B1_LL args · events LMP send/recv LLCP send/recv V2_HCI B2_LMP B2_LL HCI coverage closure closure More HCIBC LinkBLE LinkB3_LMP B3_LL specific Layer Layer fptr table fptr table searching searching searching V3_LMP V4_LL LMP coverage LLCP coverage B6 crypto

struct creation (Batch 7) S1–S5 · S8_SCO · S9_ADV BT-specific struct creation

S6

S7

propagate args per-conn arrays

D1 · D2 masked locals · malloc/free finishing pass fields · labels · xrefs · types · F2 stubs (Batch 11, last)

## Slide 74

prep / cleanup

HCI

version + coverage

link-layer

structs

###### P-phase prep Generic non-BT-specifc prep workP2–P6 → P7 (non-BT)

H1 → H2 OGF dispatch + handlers HCI-specific searching V1 Downselect search targets based on BT spec versionspec down-select

H3 · H4 B1_LMP B1_LL args · events LMP send/recv LLCP send/recv B-extras V2_HCI B2_LMP B2_LL B4 · B5 · B7 HCI coverage closure closure Misc other More HCIBC LinkBLE LinkB3_LMP B3_LL BC/BLE specific Layer Layer fptr table fptr table searching searching searching searching V3_LMP V4_LL LMP coverage LLCP coverage B6 crypto

struct creation (Batch 7) S1–S5 · S8_SCO · S9_ADV BT-specific struct creation S6 S7 propagate args per-conn arrays

D1 · D2

masked locals · malloc/free

Misc other final output cleanup (e.g. variable renaming) finishing pass fields · labels · xrefs · types · F2 stubs (Batch 11, last)

## Slide 75

Skill improvement

## Slide 76

Closed-source firmware

Open-source firmware **"Ground Truth" per-PDU names**

|**Binary**|**HCI**
**Commands**|**HCI Events**|**LLCP Send**|**LLCP Receive**|**LMP Send**|**LMP Receive**|
|---|---|---|---|---|---|---|
|**Realtek**
**RTL8761BU**|Xeno named
some
✅|Xeno named
some
✅|Xeno didn't
analyze
❌|Xeno didn't
analyze
❌|Xeno named
most/all?
✅|Xeno named
most/all?
✅|
|**Texas**|Veronica named|
Veronica named|
Veronica didn't|Veronica didn't|Veronica did|Veronica did|
|**Instruments**|some
|some
|analyze
|analyze
|minimal
|minimal
|
|**WL1835MOD**|✅|✅|❌|❌|✅|✅|
|**Silicon Labs**
**EFR32xG21**|Symbols
available
✅|Symbols
available
✅|Symbols
available
✅|Symbols
available
✅|N/A
BLE-Only|N/A
BLE-Only|
|**Zephyr on**
**Nordic**
**nRF52840**|Symbols
available
✅|Symbols
available
✅|Symbols
available
✅|Symbols
available
✅|N/A
BLE-Only|N/A
BLE-Only|
|**EM**|Symbols|Symbols|Symbols, but no|
Symbols, but no|N/A|N/A|
|**icroelectronics**
**EM9304**|
available
✅|available
✅|per-PDU funcs
❌|per-PDU funcs
❌|
BLE-Only|
BLE-Only|

**EM Microelectronics EM9304**

## Slide 77

#### **FYI:** **_shifting evaluation criteria_ over time AI YOLO match → AI** **_similar-string_ match → AI semantic match**

**_<u>all</u>_** original symbols or human renames

###### Final Ghidra file that had our skill run on it

## Slide 78

**FYI:** **_shifting evaluation criteria_ over time AI YOLO match → AI** **_similar-string_ match → AI semantic match** **_<u>all</u>_** original symbols or human **AI YOLO** renames Final **match** Ghidra file that had our skill run on it

## Slide 79

**FYI:** **_shifting evaluation criteria_ over time AI YOLO match → AI** **_similar-string_ match → AI semantic match** **_<u>all</u>_** original symbols or human **AI YOLO** renames Final **match**

Final Ghidra file that had our skill run on it

**_<u>normalized</u>_ symbol names related to categories of interest**

**→**

## Slide 80

**FYI:** **_shifting evaluation criteria_ over time AI YOLO match → AI** **_similar-string_ match → AI semantic match**

###### Final Ghidra file that had our skill run on it

**_<u>normalized</u>_ symbol names related to categories of interest**

## Slide 81

#### **FYI:** **_shifting evaluation criteria_ over time AI YOLO match → AI** **_similar-string_ match → AI semantic match**

###### Final Ghidra file that had our skill run on it

###### **AI** **_similar-string_ match**

**_<u>normalized</u>_ symbol names related to categories of interest**

## Slide 82

#### **FYI:** **_shifting evaluation criteria_ over time AI YOLO match → AI** **_similar-string_ match → AI semantic match**

Final Ghidra file that had our skill run on it

###### **AI** **_similar-string_ match**

**_<u>normalized</u>_ symbol names related to categories of interest**

**_<u>normalized</u>_ symbol names related to categories of → interest that are confirmed** **_<u>reachable</u>_ through control flow**

## Slide 83

**FYI:** **_shifting evaluation criteria_ over time AI YOLO match → AI** **_similar-string_ match → AI semantic match**

###### Final Ghidra file that had our skill run on it

**_<u>normalized</u>_ symbol names related to categories of interest that are confirmed** **_<u>reachable</u>_ through control flow**

## Slide 84

**FYI:** **_shifting evaluation criteria_ over time AI YOLO match → AI** **_similar-string_ match → AI semantic match**

Final Ghidra file that had our skill run on it

###### **AI** **_similar-string_ match**

**_<u>normalized</u>_ symbol names related to categories of interest that are confirmed** **_<u>reachable</u>_ through control flow**

## Slide 85

**FYI:** **_shifting evaluation criteria_ over time AI YOLO match → AI** **_similar-string_ match → AI semantic match**

###### **AI**

Final Ghidra file that had our skill run on it

**_similar-string_ match**

**_<u>normalized</u>_ symbol names related to categories of interest that are confirmed** **_<u>reachable</u>_ through control flow**

**_<u>normalized</u>_ symbol names**

_Unioned_

**Symbol names agreed on by 2 LLMs →**

## Slide 86

**FYI:** **_shifting evaluation criteria_ over time AI YOLO match → AI** **_similar-string_ match → AI semantic match**

###### Final Ghidra file that had our skill run on it

**_<u>normalized</u>_ symbol names**

_Unioned_ **Symbol names agreed on by 2 LLMs**

## Slide 87

**FYI:** **_shifting evaluation criteria_ over time AI YOLO match → AI** **_similar-string_ match → AI semantic match**

Final Ghidra file that had our skill run on it

###### **AI** **_semantic_**

**match**

**_<u>normalized</u>_ symbol names**

_Unioned_ **Symbol names agreed on by 2 LLMs**

## Slide 88

#### **FYI:** **_shifting evaluation criteria_ over time AI YOLO match → AI** **_similar-string_ match → AI semantic match**

Final Ghidra file that had our skill run on it

**_<u>all</u>_** original symbols or human renames

**→**

**_<u>normalized</u>_ symbol names related to categories of interest**

**_<u>normalized</u>_ symbol names related to categories of → interest that are confirmed** **_<u>reachable</u>_ through control flow**

**D3**

**_<u>normalized</u>_ symbol D2 names**

_Unioned_ **Symbol names agreed on by 2 LLMs →**

**D4**

**D1**

**D2**

## Slide 89

/bt-re-controller-improvement-orchestrator

Prepare pyghidra-mcp environment

Realtek Run full /bt-re-controllertmp for binary 1

Eval how well it did vs. D1 ground truth (human-renames)

Get suggested edits to /bt-re-controllertmp for binary 1

Aggregate recommendations (to be non-device-specific) and edit /bt-re-controller-tmp

## Slide 90

/bt-re-controller-improvement-orchestrator

Prepare pyghidra-mcp environment

Realtek Run full /bt-re-controllertmp for binary 1

⭐

Eval how well it did vs. D1 ground truth (human-renames)

Get suggested edits to /bt-re-controllertmp for binary 1

Aggregate recommendations (to be non-device-specific) and edit /bt-re-controller-tmp

## Slide 91

###### /bt-re-controller-improvement-orchestrator

Prepare pyghidra-mcp environment

Realtek

Run full /bt-re-controllertmp for binary 1

⭐

Eval how well it did vs. D1 ground truth (human-renames)

Get suggested edits to /bt-re-controllertmp for binary 1

Silicon Labs

Texas Instruments

Run full /bt-re-controllertmp for binary 2

Run full /bt-re-controllertmp for binary 3

⭐

⭐

Eval how well it did vs. D1 ground truth (human-renames)

Eval how well it did vs. D1 ground truth (found symbols)

Get suggested edits to /bt-re-controllertmp for binary 2

Get suggested edits to /bt-re-controllertmp for binary 3

Aggregate recommendations (to be non-device-specific) and edit /bt-re-controller-tmp

## Slide 92

**_<u>Problem:</u>_ /bt-re-controller-improvementorchestrator wasn't converging... Improvements to prompts that improved one binary hurt another...**

Denominator: D1

## Slide 93

###### **Rewrite for "categorized" core skill & orchestrator Improve the prompts for one category of data recovery at a time**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Rewrite for "categorized" core skill & orchestrator
Improve the prompts for one category of data recovery at a time
bt-re-controller-categorized — prompt wiring (goal-driven slices)
n order « each = one isolate e under jle /goal very ructs > S6 propagate + S10 drive phase pre-provisioned (never
INPUT - pre-provisioned p_phase_done baseline (Baseline.)
- Link H
hci_ctrl_cmd_+ L OGF dispatch cmd handlers data table J arg types J f cmdsevt structs J | HC! global JL Propagate args | data-driven
Controller HCI Events H4 S1 S3 S6 S10
t rlevt_+ evt handlers i HCI global pagate arg } dis
p_send_* packet tni losure {ptr tab pkt args | LL global propagate args data-driven PF
i € . packet fn: osu {ptr tak pkt arc | LL global: opagate args data-driven PF .
mp_send_+ packet fns losui {ptr tat pkt arc | MP globa propagate args data-driven sUPP .
mp_recv_* packet tns josure fptr tat pkt arg { MP globais J propagate args =} | Jata-driven a
P prep (frozen H HCI dispatch/handlers B LMP/LLCP packet S structs / arg typing
```

## Slide 94

## **_Categories_** **for statistical evaluation** BLE & BC Host

Host Controller Interface (HCI) Parse incoming HCI Commands

OGF 1 OGF 2 OGF 3 OGF 4 OGF 5 OGF 5 OGF 8 OGF 3F Link Control Link Policy Controller & Baseband Cmds Informational Status Testing LE Controller Cmds Vendor-Specific Cmds OCF 0x45 OCF 1 OCF 2 ... OCF 1 OCF 3 ... OCF 0x11 ... ... ... ... ... ...

Link Layer (LL) BLE Radio Physical Layer (PHY)

Link Manager Protocol (LMP) BC Radio Physical Layer (PHY)

BLE & BC Controller

**Veronica & Xeno Kovah, Dark Mentor LLC, CC-BY_SA**

## Slide 95

## **_Categories_** **for statistical evaluation** BLE & BC Host

Host Controller Interface (HCI) Parse incoming HCI Commands

OGF 1 OGF 2 OGF 3 OGF 4 OGF 5 OGF 5 OGF 8 OGF 3F Link Control Link Policy Controller & Baseband Cmds Informational Status Testing LE Controller Cmds Vendor-Specific Cmds hc ~~<u>i</u>~~ <u>_ctrl_cmd...</u> OCF 0x45 OCF 1 OCF 2 ... OCF 1 OCF 3 ... OCF 0x11 ... ... ... ... ... ... Link Layer (LL) Link Manager Protocol (LMP) BLE Radio Physical Layer (PHY) BC Radio Physical Layer (PHY) BLE & BC Controller

**Veronica & Xeno Kovah, Dark Mentor LLC, CC-BY_SA**

## Slide 96

## **_Categories_** **for statistical evaluation** BLE & BC Host

Host Controller Interface (HCI) hc ~~<u>i</u>~~ <u>_ctrl_evt...</u> Parse incoming HCI Commands

OGF 1 OGF 2 OGF 3 OGF 4 OGF 5 OGF 5 OGF 8 OGF 3F Link Control Link Policy Controller & Baseband Cmds Informational Status Testing LE Controller Cmds Vendor-Specific Cmds hc ~~<u>i</u>~~ <u>_ctrl_cmd...</u> OCF 0x45 OCF 1 OCF 2 ... OCF 1 OCF 3 ... OCF 0x11 ... ... ... ... ... ... Link Layer (LL) Link Manager Protocol (LMP) BLE Radio Physical Layer (PHY) BC Radio Physical Layer (PHY) BLE & BC Controller

**Veronica & Xeno Kovah, Dark Mentor LLC, CC-BY_SA**

## Slide 97

## **_Categories_** **for statistical evaluation** BLE & BC Host

Host Controller Interface (HCI) hc ~~<u>i</u>~~ <u>_ctrl_evt...</u> Parse incoming HCI Commands

OGF 1 OGF 2 OGF 3 OGF 4 OGF 5 OGF 5 OGF 8 OGF 3F Link Control Link Policy Controller & Baseband Cmds Informational Status Testing LE Controller Cmds Vendor-Specific Cmds hc ~~<u>i</u>~~ <u>_ctrl_cmd...</u> OCF 0x45 OCF 1 OCF 2 ... OCF 1 OCF 3 ... OCF 0x11 ... ... ... ... ... ...

hc ~~<u>i</u>~~ <u>_ctrl_cmd...</u>

llcp_send...Link Layer (LL) BLE Radio Physical Layer (PHY) BLE & BC Controller

Link Manager Protocol (LMP) BC Radio Physical Layer (PHY)

**Veronica & Xeno Kovah, Dark Mentor LLC, CC-BY_SA**

## Slide 98

## **_Categories_** **for statistical evaluation** BLE & BC Host

Host Controller Interface (HCI) hc ~~<u>i</u>~~ <u>_ctrl_evt...</u> Parse incoming HCI Commands

OGF 1 OGF 2 OGF 3 OGF 4 OGF 5 OGF 5 OGF 8 OGF 3F Link Control Link Policy Controller & Baseband Cmds Informational Status Testing LE Controller Cmds Vendor-Specific Cmds hc ~~<u>i</u>~~ <u>_ctrl_cmd...</u> OCF 0x45 OCF 1 OCF 2 ... OCF 1 OCF 3 ... OCF 0x11 ... ... ... ... ... ...

hc ~~<u>i</u>~~ <u>_ctrl_cmd...</u>

llcp_send...Link Layer (LL) llcp_recv... BLE Radio Physical Layer (PHY) BLE & BC Controller

Link Manager Protocol (LMP) BC Radio Physical Layer (PHY)

**Veronica & Xeno Kovah, Dark Mentor LLC, CC-BY_SA**

## Slide 99

## **_Categories_** **for statistical evaluation** BLE & BC Host

Host Controller Interface (HCI) hc ~~<u>i</u>~~ <u>_ctrl_evt...</u> Parse incoming HCI Commands

OGF 1 OGF 2 OGF 3 OGF 4 OGF 5 OGF 5 OGF 8 OGF 3F Link Control Link Policy Controller & Baseband Cmds Informational Status Testing LE Controller Cmds Vendor-Specific Cmds hc ~~<u>i</u>~~ <u>_ctrl_cmd...</u> OCF 0x45 OCF 1 OCF 2 ... OCF 1 OCF 3 ... OCF 0x11 ... ... ... ... ... ...

hc ~~<u>i</u>~~ <u>_ctrl_cmd...</u>

llcp_send...Link Layer (LL) llcp_recv... BLE Radio Physical Layer (PHY)

ecv... lmp_sLink Manager Protocol (LMP)end... BC Radio Physical Layer (PHY) BLE & BC Controller

**Veronica & Xeno Kovah, Dark Mentor LLC, CC-BY_SA**

## Slide 100

## **_Categories_** **for statistical evaluation** BLE & BC Host

Host Controller Interface (HCI) hc ~~<u>i</u>~~ <u>_ctrl_evt...</u> Parse incoming HCI Commands

OGF 1 OGF 2 OGF 3 OGF 4 OGF 5 OGF 5 OGF 8 OGF 3F Link Control Link Policy Controller & Baseband Cmds Informational Status Testing LE Controller Cmds Vendor-Specific Cmds hc ~~<u>i</u>~~ <u>_ctrl_cmd...</u> OCF 0x45 OCF 1 OCF 2 ... OCF 1 OCF 3 ... OCF 0x11 ... ... ... ... ... ...

hc ~~<u>i</u>~~ <u>_ctrl_cmd...</u>

llcp_send...Link Layer (LL) llcp_recv... lmp_sLink Manager Protocol (LMPend... BLE Radio Physical Layer (PHY) BLE & BC Controller

lmp_sLink Manager Protocol (LMPend... lmp_r) ecv... BC Radio Physical Layer (PHY)

**Veronica & Xeno Kovah, Dark Mentor LLC, CC-BY_SA**

## Slide 101

###### Goal for targeted prompt improvement: "Find >= 95% of D3, or get within 2"

|**category**
👉
**binary**
👇|**hci_ctrl_cmd**|**hci_ctrl_evt**|**llcp_send**|**llcp_recv**|**lmp_send**|**lmp_recv**|
|---|---|---|---|---|---|---|
|**Realtek**
**RTL8761BU**|139/139|50/50|No human-
renames|No human-
renames|50/50|92/92|
|**Texas**
**Instruments**
**WL1835MOD**|348/349|27/27|No human-
renames|No human-
renames|1/3|18/18|
|**Silicon Labs**
**EFR32xG21**|24/26|21/23|5/5|9/9|N/A BLE-only|N/A BLE-only|
|**EM**
**Microelectronics**
**EM9304**|84/85|10/10|∅|∅|N/A BLE-only|N/A BLE-only|
|**Zephyr on**
**Nordic nRF52840**|1/1|4/4|31/31|19/19|N/A BLE-only|N/A BLE-only|

Values are "found / ground truth" for Opus 4.8 "Max" effort Intermediate result just to confirm it found almost all the ground truth we had at the time, _don't dwell on it too much ;)_

Denominator: D3

## Slide 102

###### Goal for targeted prompt improvement: "Find >= 95% of D3, or get within 2"

|**category**
👉
**binary**
👇|**hci_ctrl_cmd**|**hci_ctrl_evt**|**llcp_send**|**llcp_recv**|**lmp_send**|**lmp_recv**|
|---|---|---|---|---|---|---|
|**Realtek**
**RTL8761BU**|139/139|50/50|No human-
renames|No human-
renames|50/50|92/92|
|**Texas**
**Instruments**
**WL1835MOD**|348/349|27/27|No human-
renames|No human-
renames|1/3|18/18|
|**Silicon Labs**
**EFR32xG21**|24/26|21/23|5/5|9/9|N/A BLE-only|N/A BLE-only|
|**EM**
**Microelectronics**
**EM9304**|84/85|10/10|∅|∅|N/A BLE-only|N/A BLE-only|
|**Zephyr on**
**Nordic nRF52840**|1/1|4/4|31/31|19/19|N/A BLE-only|N/A BLE-only|

Values are "found / ground truth" for Opus 4.8 "Max" effort Intermediate result just to confirm it found almost all the ground truth we had at the time, _don't dwell on it too much ;)_

Denominator: D3

## Slide 103

###### Goal for targeted prompt improvement: "Find >= 95% of D3, or get within 2"

|**category**
👉
**binary**
👇|**hci_ctrl_cmd**|**hci_ctrl_evt**|**llcp_send**|**llcp_recv**|**lmp_send**|**lmp_recv**|
|---|---|---|---|---|---|---|
|**Realtek**
**RTL8761BU**|139/139|50/50|No human-
renames|No human-
renames|50/50|92/92|
|**Texas**
**Instruments**
**WL1835MOD**|348/349|27/27|No human-
renames|No human-
renames|1/3|18/18|
|**Silicon Labs**
**EFR32xG21**|24/26|21/23|5/5|9/9|N/A BLE-only|N/A BLE-only|
|**EM**
**Microelectronics**
**EM9304**|84/85|10/10|∅
Expe
EM Code doesn
func|∅
cted
't have per-PDU
tions|N/A BLE-only|N/A BLE-only|
|**Zephyr on**
**Nordic nRF52840**|1/1|4/4|31/31|19/19|N/A BLE-only|N/A BLE-only|

Values are "found / ground truth" for Opus 4.8 "Max" effort Intermediate result just to confirm it found almost all the ground truth we had at the time, _don't dwell on it too much ;)_

Denominator: D3

## Slide 104

#### **Two** **_extremely_ painful lessons learned...**

1. If you just let Claude throw together an wrapper around the core bt-re-controller skill ("orchestrator"), it will serialize all the prompts! It doesn't seem to support running the main session with per-binary sub-agents with all of the built-in sub-agents & parallelism that the core bt-re-controlled skill

• Takeaway: didn't have time to design around sub-agent depth limits, just started collecting stats by manually running N instances of bt-re-controller 2. In the first stab at the categorized orchestrator, Claude ended up defaulting to one session querying 5 Ghidra MCP servers, instead of 5 sessions independently queuing their own MCP server. This led to "attention dilution" where the exact same prompt which recovered 144/144 HCI command functions, collapsed to 20/144

- Takeaway: explicitly design for context isolation

## Slide 105

## Evaluating improved skill, background

## Slide 106

Opus
findings

GPT findings

Opus 4.8

GPT 5.6 Sol

## Slide 107

###### original symbols or human renames 0x00004efc BLELINKLAYERCORE_HciResetNotification

###### Opus findings

0x00004efc hci_ctrl_cmd_03_003__HCI_Reset() ...

GPT findings

**Opus 4.8**

**GPT 5.6 Sol**

## Slide 108

Opus
findings

original symbols or human renames
0x00004efc
BLELINKLAYERCORE_HciResetNotification
0x00004efc
hci_ctrl_cmd_03_003__HCI_Reset()
...
GPT findings
GPT 5.6 Sol

**Opus 4.8**

## Slide 109

original symbols or human renames
0x00004efc
BLELINKLAYERCORE_HciResetNotification
0x00004efc
hci_ctrl_cmd_03_003__HCI_Reset()
Opus  ...
findings
GPT findings
Opus 4.8 GPT 5.6 Sol

## Slide 110

original symbols or human renames
Opus decides:
True Positive 👍 0x00004efc
BLELINKLAYERCORE_HciResetNotification
False Positive 👎
0x00004efc
hci_ctrl_cmd_03_003__HCI_Reset()
Opus  ...
findings
GPT findings
Opus 4.8 GPT 5.6 Sol

Opus 4.8

## Slide 111

original symbols or human renames 0x00004efc BLELINKLAYERCORE_HciResetNotification

0x00004efc hci_ctrl_cmd_03_003__HCI_Reset()

...

Opus findings

GPT findings

**GPT 5.6 Sol**

**Opus 4.8**

## Slide 112

original symbols or human renames 0x00004efc BLELINKLAYERCORE_HciResetNotification

0x00004efc hci_ctrl_cmd_03_003__HCI_Reset() ...

Opus findings

GPT findings

**GPT 5.6 Sol**

**Opus 4.8**

## Slide 113

###### original symbols or human renames 0x00004efc BLELINKLAYERCORE_HciResetNotification

0x00004efc hci_ctrl_cmd_03_003__HCI_Reset() ...

Opus findings

**Opus 4.8**

GPT findings

**GPT 5.6 Sol**

## Slide 114

GPT decides: True Positive 👍 False Positive 👎

original symbols or human renames 0x00004efc BLELINKLAYERCORE_HciResetNotification 0x00004efc hci_ctrl_cmd_03_003__HCI_Reset() ...

Opus findings

GPT findings

**Opus 4.8**

**GPT 5.6 Sol**

## Slide 115

###### **When are different names actually the same? Realtek binary example**

###### **Ground truth (e.g. human-rename)**

###### **LLM analysis based on bt-re-controller**

## Slide 116

###### **When are different names actually the same? Realtek binary example**

###### **Ground truth (e.g. human-rename)**

###### **LLM analysis based on bt-re-controller**

## Slide 117

###### **When are different names actually the same? Realtek binary example**

###### **Ground truth (e.g. human-rename)**

###### **LLM analysis based on bt-re-controller**

## Slide 118

###### **When are different names actually the same? Realtek binary example**

###### **Ground truth (e.g. human-rename)**

###### **LLM analysis based on bt-re-controller**

**?**

## Slide 119

#### **"Related Operations" (RelOps) From a BT Spec perspective**

Always let _the specification_ be your guide!

- "Procedures" in Bluetooth are defined as multi-step activities that can involve the Host and/or Controller

- They're often going to be implemented as per-procedure state machines in code

- There are also explicit _separate_ state machines & transitions which aren't called "Procedures" (although we think they probably should have been)

- We'll use RelOps as an umbrella term for all these sort of things where related multi-step operations are going to show up in code

Jiminy Cricket image from https://www.thedisneyclassics.com/blog/jiminy-cricket

## Slide 120

#### **Semantic-match using RelOps Realtek binary: cross layer match**

###### **Ground truth (e.g. human-rename)**

###### **LLM analysis based on bt-re-controller**

# **?**

## Slide 121

#### **Semantic-match using RelOps Realtek binary: cross layer match**

###### **Ground truth (e.g. human-rename)**

###### **LLM analysis based on bt-re-controller**

## Slide 122

Opus
findings

GPT findings

Opus 4.8

GPT 5.6 Sol

## Slide 123

👎
Opus FP
GPT FP
👎
Opus-only
TP 👍
👍 GPT-only
Opus
TP
findings
GPT
findings
Shared TP Shared TP
👍
👍

Opus 4.8

GPT 5.6 Sol

## Slide 124

Opus FP
Opus-only
TP
Opus
findings
Shared TP

GPT FP **GPT-only TP** GPT findings Shared TP

Opus 4.8

GPT 5.6 Sol

## Slide 125

Opus-only
TP
Shared TP

GPT-only
TP
Opus-only
TP
GPT-only
TP
Shared TP Shared TP
GPT 5.6 Sol

Opus 4.8

## Slide 126

*truth.md D2

Opus-only
TP
Shared TP

Unioned
GPT-only
TP
Opus-only
TP
GPT-only
TP
Shared TP Shared TP
GPT 5.6 Sol

Opus 4.8

## Slide 127

100%

*truth.md D2

Unioned

X%
Opus-only
TP
Shared TP

GPT-only
TP
Opus-only
TP
Shared TP

Y%
GPT-only
TP
Shared TP
GPT 5.6 Sol

Opus 4.8

## Slide 128

###### Coloring conventions for next graphs:

100%
X%
Opus-only
Y%
TP
denominator
GPT-only
.md
TP
Shared TP Shared TP
Opus 4.8 D4 GPT 5.6 Sol

Opus 4.8

## Slide 129

###### Coloring conventions for next graphs:

100%
X%
Opus-only
Y%
TP
denominator
GPT-only
.md
TP
Shared TP Shared TP
Opus 4.8 D4 GPT 5.6 Sol

Opus 4.8

## Slide 130

## Final skill evaluation on binaries used for skill creation

## Slide 131

Anthropic Claude Opus 4.8 run with "Max" level of effort ("Ultracode" not available in sub-agents) OpenAI Codex GPT 5.6 Sol run with "Ultra" level of effort Denominator: D4

## Slide 132

N/A due to BLE-only chip

N/A due to BLE-only chip

Anthropic Claude Opus 4.8 run with "Max" level of effort ("Ultracode" not available in sub-agents) OpenAI Codex GPT 5.6 Sol run with "Ultra" level of effort Denominator: D4

## Slide 133

N/A due to BLE-only chip

Anthropic Claude Opus 4.8 run with "Max" level of effort ("Ultracode" not available in sub-agents) OpenAI Codex GPT 5.6 Sol run with "Ultra" level of effort Denominator: D4

## Slide 134

N/A due to BLE-only chip

EM9304 doesn't have per-PDU LLCP sending/receiving functions like a lot of other binaries, but rather single dispatchers with lots of switch cases

Anthropic Claude Opus 4.8 run with "Max" level of effort ("Ultracode" not available in sub-agents) OpenAI Codex GPT 5.6 Sol run with "Ultra" level of effort Denominator: D4

## Slide 135

N/A due to BLE-only chip

EM9304 doesn't have per-PDU LLCP sending/receiving functions like a lot of other binaries, but rather single dispatchers with lots of switch cases

We create "function-equivalent-comments" which mark functionality that handles opcodes and give them a name we the naming conventions we would use to rename functions Anthropic Claude Opus 4.8 run with "Max" level of effort ("Ultracode" not available in sub-agents) OpenAI Codex GPT 5.6 Sol run with "Ultra" level of effort Denominator: D4

## Slide 136

## Final skill evaluation on binaries _<u>not used</u>_ for skill creation

## Slide 137

#### **Testing on un-analyzed firmware 7 binaries not used during targeted prompt improvement**

- Renesas DA1469X (Princess Cruise Medallion [1])

- Broadcom BCM43430A1 (Raspberry Pi Zero W built-in)

- Realtek 8821CE (Dell Laptop built-in)

- Intel Wireless-AC 9260 (AAEON UP<sup>2</sup> add-in wireless card)

- Nordic nRF52832 (Development board)

- STMicroelectronics BlueNRG (Development board)

- Espressif ESP32 (ROMs on official github)

[1] Firmware binary dump from Princess Cruise's "medallions" (onboard access control system) from this research https://github.com/atredispartners/DaBootZone shared privately, without any analysis applied.

## Slide 138

##### **How to evaluate things for which we have no ground truth?**

• The starting point for truth is whatever functions they both found at the same locations with semantically matching names • For the remaining functions, do the "Model grades other model's results" cross-check • Obviously we could extend it to multi-model consensus in the future

## Slide 139

Opus
findings

GPT findings

Opus 4.8

GPT 5.6 Sol

## Slide 140

###### Opus-only findings

###### Shared findings

GPT-only findings

Shared findings

Opus 4.8

GPT 5.6 Sol

## Slide 141

###### Opus-only findings

###### Shared findings

GPT-only findings

Shared findings

Opus 4.8

GPT 5.6 Sol

## Slide 142

Opus-only
findings
GPT-only
findings
Shared
Shared
findings
findings

GPT 5.6 Sol

Opus 4.8

## Slide 143

Opus-only
findings
GPT-only
GPT-only
findings
TP
👍
(Opus FN)
Shared
Shared
findings
findings
Opus 4.8 GPT 5.6 Sol

Opus 4.8

## Slide 144

Opus-only
GPT FP
👎
findings
GPT-only
GPT-only
findings
TP
👍
(Opus FN)
Shared
Shared
findings
findings
Opus 4.8 GPT 5.6 Sol

Opus 4.8

## Slide 145

###### Opus-only findings

###### Shared findings

GPT-only findings

Shared findings

Opus 4.8

GPT 5.6 Sol

## Slide 146

Opus-only
findings
Shared
findings

GPT-only
findings
Shared
findings
GPT 5.6 Sol

Opus 4.8

## Slide 147

Opus-only
Opus-only
findings
TP
👍
GPT-only
(GPT FN) findings
Shared
Shared
findings
findings
Opus 4.8 GPT 5.6 Sol

Opus 4.8

## Slide 148

Opus FP 👎
Opus-only
Opus-only
findings
TP
👍
GPT-only
(GPT FN) findings
Shared
Shared
findings
findings
Opus 4.8 GPT 5.6 Sol

Opus 4.8

## Slide 149

Opus FP 👎
Opus-only
Opus-only  👎 GPT FP
findings
TP
👍
GPT-only
GPT-only
(GPT FN) findings
TP
👍
(Opus FN)
Shared
Shared
findings
findings
Opus 4.8 GPT 5.6 Sol

## Slide 150

Opus FP
Opus-only
Opus-only  GPT FP
findings
TP  GPT-only
GPT-only
(GPT FN) findings
TP
(Opus FN)
Shared
Shared
findings
findings
Opus 4.8 GPT 5.6 Sol

## Slide 151

Opus-only
TP
(GPT FN)
GPT-only
TP
(Opus FN)

Shared findings

Opus 4.8 & GPT 5.6 Sol **_<u>Mutually-agreed-upon truth</u>_**

## Slide 152

🏆→ ←Opus Wins

←      ~ Tie        →

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Broadcom BCM43430A1
Field Count Share
@ Shared 592 85.2%
@ Opus FN 29 4.2%
GPTFN «Opus Wins’ 74 = 10.6%
Opus FP 0 0.0%
GPT FP 0 0.0%
Likely true-positives (first 3) 695
Total function/comment findings 695
Realtek RTL8821CE
Field Count Share
| @ Shared 551 94.7%
Opus FP 0 0.0%
@ GPT FP 4 0.7%
Likely true-positives (first 3) 578
Total function/comment findings 582
```

## Slide 153

🏆→ ←Opus Wins

←GPT Wins🏆→

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Espressif ESP32
aS
Field Count
@ Shared 469
@ Opus FN 27
GPTFN «~Opus Wins’ > 91
@ Opus FP 1
Likely true-positives (first 3)
Total function/comment findings
Intel 9260 ThunderPeak
\
Field Count
@ Shared 43
@ Opus FN «GPT Wins v’- 585
GPT FN 233
@ Opus FP 15
Likely true-positives (first 3)
Total function/comment findings
Share
79.8%
4.6%
15.5%
0.2%
0.0%
587
588
Share
4.8%
64.7%
25.8%
1.7%
3.1%
861
904
```

## Slide 154

←      ~ Tie        →

←GPT Wins🏆→

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Renesas DA1469x
Field Count Share
N @ Shared 153 29.6%
@ Opus FN . 169 32.7%
cptrN*s =~ ‘Tie 151 29.2%
@ Opus FP 11 2.1%
@ GPT FP 33 6.4%
Likely true-positives (first 3) 473
Total function/comment findings 517
Nordic nRF52832
Field Count Share
@ Shared 11 13.8%
@ Opus FN GPT Wins’ 54 675%
GPT FN 15 18.8%
Opus FP 0 0.0%
GPT FP 0 0.0%
Likely true-positives (first 3) 80
Total function/comment findings 80
```

## Slide 155

←      ~ Tie        →

←GPT Wins🏆→

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Renesas DA1469x
Field Count Share
N @ Shared 153 29.6%
@ Opus FN . 169 32.7%
GpTEN* =~ Tle 151 29.2%
@ Opus FP 11 2.1%
@ GPT FP 33 6.4%
Likely true-positives (first 3) 473
Total function/comment findings 517
Nordic nRF52832
Field Count Share
@ Shared 112)013.8%
@ Opus FN GPT Wins’ 54 675%
GPT FN 15 18.8%
Opus FP 0 0.0%
GPT FP 0 0.0%
Likely true-positives (first 3) 80 ee
Total function/comment findings 80
```

## Slide 156

←      ???      →

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
STMicro BlueNRG-1
Field
@ Shared
Opus FN
GPT FN
Opus FP
GPT FP
Likely true-positives (first 3)
Total function/comment findings
Share
100.0%
0.0%
0.0%
0.0%
0.0%
25
25
```

## Slide 157

←      ???      →

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
STMicro BlueNRG-1
Field Count Share
@ Shared 22% 25°)®)0.0%
Opus FN 0 0.0%
GPT FN 0.0%
0
Opus FP 0 0.0%
0
GPT FP 0.0%
Likely true-positives (first 3) 25 ee
Total function/comment findings 25
```

## Slide 158

#### **Should you use Opus 4.8 or GPT 5.6 Sol?**

https://giphy.com/gifs/celebrate-shrugging-both-zbzNUbpFnlw8E

## Slide 159

#### **Should you use Opus 4.8 or GPT 5.6 Sol?**

https://giphy.com/gifs/celebrate-shrugging-both-zbzNUbpFnlw8E

## Slide 160

Wrap-up

## Slide 161

#### **Future work**

###### • Create _vendor-specific_ skills

- Unlike the current skill, which is told to avoid vendor-isms, these versions can be specifically reinforced with information from the same vendor's chips

• Create skills for reversing closed-source _Host-level_ protocols & code (e.g. L2CAP, ATT, SMP, etc protocols in the "Full Stack" code we already have for SiLabs, TI, EMMicro, Espressif, etc)

## Slide 162

#### **Conclusion**

**_•_**<sup>**_<u>Days or weeks of work eliminated!</u>_**</sup>

• FIXME: public git URL TBD <u>https://github.com/darkmentorllc/mad_bt_skillz</u> ?

## Slide 163

#### **Applicability to other domains**

• This is not just about Bluetooth!

• Firmware sits between Software and Hardware

• Firmware often implements specifications

• Think UEFI, NVMe, WiFi, XHCI, etc

• Therefore you should be able to use specification knowledge to find **_Waypoints_** 📍 in other firmware for other technologies as _fundamentallyrequired_ functionality to meet the specification requirements

## Slide 164

**OpenSecurityTraining2** 🎉 **_5th anniversary!_** 🔑 Level 6 Unlocked! 🔓 **https://ost2.fyi**

## Slide 165

**Thanks for listening** P.s. here's a timeline of the last 25 years of BT research! <u>https://darkmentor.com/bt.html</u>

"Documentation is what separates us from the animals!"

<u>https://darkmentor.com https://www.linkedin.com/company/dark-mentor/ https://bsky.app/profile/darkmentor.com https://infosec.exchange/@DarkMentor https://twitter.com/DarkMentorLLC https://github.com/darkmentorllc</u>

<u>https://ost2.fyi https://www.linkedin.com/company/OST2 https://bsky.app/profle/OpenSecTrainingi https://infosec.exchange/@OpenSecurityTraining2 https://twitter.com/OpenSecTraining https://gitlab.com/OpenSecTraining</u>

## Slide 166

Backup

## Slide 167

###### **Misc note: all eval done with internet lookup prohibited**

• When evaluating our skill to show its results, we specifically prohibit it from reaching out to the internet, so that we have more deterministic results

• In ~/.claude/settings.json set "env": {"BTRE_OFFLINE": "1"},

• In ~/.codex/config.toml set [shell_environment_policy.set] BTRE_OFFLINE = "1"

## Slide 168

#### **A word about the V* prompts**

- V1 down-selects from all-possible HCI/LLCP/LMP stuff to search for, to the subset that we might reasonable expect the Controller to implement, based on:

   - Bluetooth Specification version stated as supported by the humans, but also recovered from LMP_VERSION_RES/REQ or LL_VERSION_IND packets

   - HCI "Supported Commands" command (which says which HCI Commands the Controller supports)

   - Supported features for

      - LMP - based on HCI_Read_Local_Supported_Features/HCI_Read_Local_Extended_Features or LMP_FEATURES_REQ/RES

      - LLCP - based on HCI_LE_Read_Local_Supported_Features_Page_0 or LL_FEATURE_RSP/REQ

- It's generally pretty unlikely to down-select correctly on the first pass since it's only searched rigorously for HCI at that point, not LLCP/LMP yet

   - But if we re-run the skill on the same file twice it's much more likely to get it right!

## Slide 169

#### **How long does it take the skill to run? (1) Set 1 (used for skill creation)**

- Claude Desktop

- ChatGPT (neé Codex)

• EM (1654 .c files) - 5h 41m Realtek (2884 .c files) - 6h 19m SiLabs (1689 .c files) - 6h 35m TI (5954 .c files) - 6h 51m Zephyr on Nordic (2211 .c files) - 6h 15m

• EM - 6h 3m Realtek - 8h 26m SiLabs - 5h 28m TI - 6h 31m Zephyr on Nordic - 5h 53m

## Slide 170

#### **How long does it take the skill to run? (2) Set 2 (** **_<u>not</u>_ used for skill creation)**

- Claude Desktop

- ChatGPT (neé Codex)

• Broadcom (5989 .c files) - 7h 48m Espressif (2433 .c files) - 6h 4m Intel (4735 .c files) - 7h 47m Nordic (2250 .c files) - 5h 32m Realtek RTL8821CE ( .c files) - Renesas (2966 .c files) - 7h 10m STMicro (937 .c files) - 5h 19m

• Broadcom - 7h 19m Espressif - 7h 14m Intel - 8h 46m Nordic - 4h 20m Realtek RTL8821CE - Renesas - 5h 7m STMicro - 4h 49m

## Slide 171

**#Life-/Goals** "Preparation: Create a new skill named bt-re-controller-superGPT which starts out as an exact copy of the Codex bt-re-controller skill. Procedure: Make edits to the prompts to improve them until the final prompts recover 100% of the truth-reachable.md. All edits must be confirmed to not cause regressions of the recovery rate on any other binaries. Goal: recover 100% of the ground truth (in the truth-reachable.md file for each binary) as reported when using the bt-re-controller-eval evaluation methodology. Look at existing results in 5xManualCodex to see the starting results which you need to improve to 100%." • GPT 5.6 Sol at "Ultra" level of effort spent 11 hours creating bt-re-controller-superGPT

- How does it perform? Almost always the same or worse!

   - **So the point is you can't just use /goal instead of the orchestrator style we used**
