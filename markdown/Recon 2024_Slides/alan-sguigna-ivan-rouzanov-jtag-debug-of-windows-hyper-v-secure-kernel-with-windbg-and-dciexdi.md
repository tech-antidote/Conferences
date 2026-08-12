---
title: "JTAG debug of Windows Hyper-V  Secure Kernel with WinDbg and DCIEXDI"
speakers: ["Alan Sguigna", "Ivan Rouzanov"]
conference: "REcon"
conference_full: "REcon 2024"
edition: ""
year: 2024
source_pdf: "Recon 2024_Slides/Alan Sguigna & Ivan Rouzanov_JTAG debug of Windows Hyper-V  Secure Kernel with WinDbg and DCIEXDI.pdf"
pages: 14
sha256: "b7b52f98491f1c1a3e70310e1fd79448a34f5706f7026fd496e6cab32b4bc6a2"
text_chars: 4535
ocr_pages: 2
has_ocr: true
redacted_secrets: 0
ocr_confidence: 90.5
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T06:05:14Z"
---
# JTAG debug of Windows Hyper-V  Secure Kernel with WinDbg and DCIEXDI

**Speakers:** Alan Sguigna, Ivan Rouzanov  
**Conference:** REcon 2024  
**Source:** `Recon 2024_Slides/Alan Sguigna & Ivan Rouzanov_JTAG debug of Windows Hyper-V  Secure Kernel with WinDbg and DCIEXDI.pdf` (14 pages)


## Slide 1

JTAG Debug of Windows Hyper

V / Secure Kernel

with

and EXDI

WinDbg

REcon

2024

Alan Sguigna, Ivan Rouzanov

June 29, 2024

Real Insight from Code to Silicon

## Slide 2

–
Workshop Announcement Soprano A

▪ SourcePoint debuggers connected to live Intel targets! ▪ First come, first served ▪ 3:30pm – 4:30pm: 10 seats ▪ 4:30pm – 5:30pm: 10 seats ▪ Basic knowledge of WinDbg/Hyper-V recommended ▪ Sign-in sheet available after this session ▪ **_Complete systems available to take home_**

2

© 2024, ASSET InterTech, Inc.

## Slide 3

Agenda

▪ SourcePoint JTAG-based debugger ▪ From UEFI to Windows ▪ Combining WinDbg + SourcePoint ▪ OS-aware + JTAG/ Hardware Tracing ▪ Demo configuration ▪ What you’ll see in the demo ▪ Demo ▪ Wrap-Up

3

© 2024, ASSET InterTech, Inc.

## Slide 4

-
SourcePoint: x86 JTAG based debugger

- Collaboration with Intel for 20 years

- Merger with Arium in 2013

- Best-in-class UEFI debugger

- Support for x86: Intel (all CPUs) and AMD (EPYC)

- Source-level symbolic debugger, full run-control (stop, go, singlestep, breakpoints, etc.)

- Supports innovative Trace features on Intel

4

© 2024, ASSET InterTech, Inc.

## Slide 5

-
SourcePoint JTAG based debugger: a little history

**<u>Windows (et al) – circa 2023</u>** EXDI integration with WinDbg Hypervisor BP (VM Launch, Resume, Exit) VMCS Viewer/ Editor

**<u>UEFI – circa 2008</u>** Run-control

Intel Trace Hub Intel Processor Trace Architectural Event Trace (AET) SMM breakpoints (Entry, Exit, Data, I/O) Reset/Init/Power Cycle breakpoints Macro Language XDP and DCI access

**JTAG**

**“Ring -** ∞ **”**

Image courtesy of Pavel Yosifovich, <u>Windows Internals course</u>

5

© 2024, ASSET InterTech, Inc.

## Slide 6

Why combine WinDbg and SourcePoint?

- Recent update to EXDI  (Extended Debug Interface)

- EXDI is an adaptation layer between a software debugger and a debugging target.

- ▪ Extends WinDbg by adding support for hardware-based debuggers (i.e. JTAG-based)

- ▪ WinDbg is the controller; SourcePoint is the worker

- “Debugging the Undebuggable” <u>https://www.andreaallievi.com/blog/debugging-theundebuggable-part-1/</u> **_But on steroids!_**

6

© 2024, ASSET InterTech, Inc.

## Slide 7

Why is this cool? New Capabilities

- No agent on the target!

- Target runs at native speed

- Debugging from reset vector to Windows: UEFI + Windows

- ▪ VM Launch/ Resume/ Exit breakpoints: hvix64 -> hvloader -> securekernel and beyond

- Static and dynamic analysis of the Secure Kernel with symbols

- ▪ VMCS Viewer/Editor

- Intel Processor Trace (Intel PT)

- Disabling Windows mitigations; i.e. Intel PT “conceal bits”

- ▪ Architectural Event Trace (AET)

- Debugging VBS-enabled enclave code

- No NDA

7

© 2024, ASSET InterTech, Inc.

## Slide 8

Hardware Tracing Secret Weapons: Intel PT and AET

## **<u>Intel PT</u>**

- Instruction trace, captured to target system memory

- ▪ Nominal overhead (1% - 3%)

- ▪ Can filter by CR3, CPL, address

- **<u>AET</u>**

- Event trace; supports probe mode (JTAG) only

- ▪ Captured to DCI, MTB, or System Memory

- Not CR3-aware

8

© 2024, ASSET InterTech, Inc.

## Slide 9

AAEON  UP Xtreme i11 (Tiger Lake)

▪ Debugging on a physical target ▪ Supports Intel DCI (no HW probe required) out of the box ▪ All Intel run-control and trace features supported

9

© 2024, ASSET InterTech, Inc.

## Slide 10

–
The Demos what you’ll see

1. Alan: Secure Kernel debug, VBS-enabled enclaves, Intel PT, AET, NTOS <-> SK “dance”, etc. 2. Ivan: practical use of Intel PT + AET

**_SourcePoint WinDbg_**

**DCI (USB) Cable**

**AAEON UP Xtreme i11 Tiger Lake**

10

© 2024, ASSET InterTech, Inc.

## Slide 11

Demo

11

© 2024, ASSET InterTech, Inc.


> Recovered by OCR — confidence 94/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
14
Platform for Software Debug and Trace © 2024, ASSET InterTech, Inc. Platform for Embedded Instruments
```

## Slide 12

Resources

▪ SourcePoint Academy: https://www.asset- <u>intertech.com/resources/academy/sourcepointacademy/</u> ▪ _SourcePoint WinDbg Getting Started Guide_ ▪ _Getting Started Guide for the AAEON UP Xtreme i11_ ▪ _Videos, Online Help, Release Notes, etc._ ▪ Getting a copy: https://www.asset- <u>intertech.com/products/sourcepoint/sourcepointwindbg/</u>

12

© 2024, ASSET InterTech, Inc.

## Slide 13

-
Wrap Up and Contact Information

**_Available Now_** _SourcePoint Home: emailto:ai-info@asset-intertech.com SourcePoint Enterprise:_ _<u>www.asset-intertech.com/contact-us/</u>_

_‘X’ DM @AlanSguigna or LinkedIn InMail_

13

© 2024, ASSET InterTech, Inc.

## Slide 14

# Real Insight from Code to Silicon

© 2024, ASSET InterTech, Inc.,


> Recovered by OCR — confidence 87/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
==
tform for Software Deb and Trace © , Inc., Late feed
Platform for Software Debug and Trace © 2024, ASSET InterTech, Inc. Platform for Embedded Instruments
```
