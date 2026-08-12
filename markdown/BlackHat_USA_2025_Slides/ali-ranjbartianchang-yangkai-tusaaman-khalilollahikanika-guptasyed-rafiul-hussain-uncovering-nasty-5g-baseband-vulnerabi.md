---
title: "Uncovering 'NASty' 5G Baseband Vulnerabilities through Dependency-Aware Fuzzing"
speakers: ["Ali Ranjbar", "Tianchang Yang", "Kai Tu", "Saaman Khalilollahi", "Kanika Gupta", "Syed Rafiul Hussain"]
conference: "Black Hat"
conference_full: "Black Hat USA 2025"
edition: "USA"
year: 2025
source_pdf: "BlackHat_USA_2025_Slides/Ali Ranjbar&Tianchang Yang&Kai Tu&Saaman Khalilollahi&Kanika Gupta&Syed Rafiul Hussain_Uncovering 'NASty' 5G Baseband Vulnerabilities through Dependency-Aware Fuzzing.pdf"
pages: 101
sha256: "9107c13a6a13213cfa0924be724c083a99bb692c4754664911b7998010fce110"
text_chars: 37847
ocr_pages: 39
has_ocr: true
redacted_secrets: 0
ocr_confidence: 85.5
ocr_unreliable_blocks: 0
vision_verified_blocks: 3
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T05:05:46Z"
---
# Uncovering 'NASty' 5G Baseband Vulnerabilities through Dependency-Aware Fuzzing

**Speakers:** Ali Ranjbar, Tianchang Yang, Kai Tu, Saaman Khalilollahi, Kanika Gupta, Syed Rafiul Hussain  
**Conference:** Black Hat USA 2025  
**Source:** `BlackHat_USA_2025_Slides/Ali Ranjbar&Tianchang Yang&Kai Tu&Saaman Khalilollahi&Kanika Gupta&Syed Rafiul Hussain_Uncovering 'NASty' 5G Baseband Vulnerabilities through Dependency-Aware Fuzzing.pdf` (101 pages)


## Slide 1

# **Uncovering 'NASty' 5G Baseband Vulnerabilities through Dependency-Aware Fuzzing**

Ali Ranjbar & Tianchang Yang

Kai Tu, Saaman Khalilollahi, Kanika Gupta, Syed Rafiul Hussain

#BHUSA @BlackHatEvents

## Slide 2

### Introduction

###### **Ali Ranjbar**

- Research Assistant, The Pennsylvania State University

- Embedded systems, cellular security, reverse engineering, and fuzzing.

- `aranjbar.me`

#BHUSA @BlackHatEvents

## Slide 3

### Introduction

###### **Tianchang Yang**

- Research Assistant, The Pennsylvania State University

- Mobile network security, resiliency, and robustness: 5G, Open RAN, baseband (fuzzing, program analysis, ML)

- `tianchang-yang.github.io`

#BHUSA @BlackHatEvents

## Slide 4

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 79/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
BRIEFINGS Re
Coffee with Robin in 30 min
© 10.00 a.m. - 11.00 a.m. @ 20°C
```

## Slide 5

### Cellular Network 101

Smartphone (UE)

#BHUSA @BlackHatEvents

## Slide 6

### Cellular Network 101

Smartphone (UE)

Cell tower (Base station)

#BHUSA @BlackHatEvents

## Slide 7

### Cellular Network 101

Smartphone (UE)

Cell tower (Base station)

Core network

#BHUSA @BlackHatEvents

## Slide 8

### Cellular Network 101

Smartphone (UE)

Cell tower (Base station)

Core network

#BHUSA @BlackHatEvents

## Slide 9

### Cellular Network 101

Cell tower
Smartphone (UE)
(Base station)
RRC
NAS

Core network

Data network

SMS/Voice/IP

#BHUSA @BlackHatEvents

## Slide 10

### Non-Access Spectrum (NAS)

- NAS is mostly post-authentication • NAS messages are encrypted and integrity protected – undertested

- • Still results in issues not requiring operator keys to exploit

Smartphone (UE)

Core network

NAS

#BHUSA @BlackHatEvents

## Slide 11

### Baseband Overview

• Memory unsafe language
• Lack exploit protection
Baseband
A A A A A A A A A A

Buffer overflow

https://forums.anandtech.com/threads/samsung-exynos-soc-thread.2620862/

#BHUSA @BlackHatEvents

## Slide 12

### Baseband Overview

• Memory unsafe language
• Lack exploit protection
Baseband
A A A A A A A A A A
Buffer overflow

https://forums.anandtech.com/threads/samsung-exynos-soc-thread.2620862/

#BHUSA @BlackHatEvents

## Slide 13

### Baseband Overview

- Memory unsafe language

- Lack exploit protection

A A A A A A A A A A

Buffer overflow

#BHUSA @BlackHatEvents

https://forums.anandtech.com/threads/samsung-exynos-soc-thread.2620862/

## Slide 14

### Baseband Overview

• Memory unsafe language
• Lack exploit protection
Baseband
A A A A A A A A A A
Buffer overflow
#BHUSA @BlackHatEvents

https://forums.anandtech.com/threads/samsung-exynos-soc-thread.2620862/

## Slide 15

### Baseband exploits in-the-wild

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 85/100 on the text kept, 73/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
BRIEFINGS
Baseband exploits in-the-wild
Project Zero Or... How Network Names became an RCE vector
Over The Air Baseband Exploit:
News and updates from the Project Zero team at Google
Able 48 oon ae Gaining Remote Code
v7} “6 09 GB Execution on 5G Smartphones
Showing posts sorted by relevance for query baseband. Sort by date Show all posts
TL LEAS Marco Grassi (@marcograss)
K> KEEN Xingyu Chen (@@xKira233)
Multiple Internet to Baseband Remote Code Execution ao
Vulnerabilities in Exynos Modems
Posted by Tim Willis, Project Zero
— ASN.1 and Done USArcUe4
a Ye AUGUST 7-8, 2024
| SG AKA Bypass A tale of exploiting ASN.1 parsers in the Overcoming State: Finding Baseband
PDU Session Est Request baseband. Vulnerabilities by Fuzzing Layer-2
PDU Session Est Accept
@amatcama
' Speakers: Dyon Goos & Marius Muench
H i VIGILANT
```

## Slide 16

From exploits to frameworks: Baseband research • 2020: BaseSAFE: Baseband SAnitized Fuzzing through Emulation.

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 87/100 on the text kept, 57/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
From exploits to frameworks: Baseband research
¢ 2020: BaseSAFE: Baseband SAnitized Fuzzing through Emulation. €
```

## Slide 17

From exploits to frameworks: Baseband research • 2020: BaseSAFE: Baseband SAnitized Fuzzing through Emulation.

#BHUSA @BlackHatEvents


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 84/100 on the text kept, 79/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
BaseSAFE / examples / errc / src / main.rs

Code | Blame        678 lines (603 loc) - 26.2 KB

592        hook!(0x3b4fc4, msg_recv, "msg_receive_extq");
593        hook!(0x3b5010, pass_func, "msg_receive_intq");
594        hook!(0x00119b68, dhl_trace);
595        hook!(0x00119768, pass_func, "dhl_peer_trace");
596        hook!(0x001fe2f0, errc_evth_dump_reserve_queue);
597        hook!(0x001f3d8c, pass_func, "errc_evth_com_timer_expiry_hdlr");
598        hook!(0x003b28a0, pass_func, "stack_get_active_module_id");
599        hook!(0x003b5478, kal_get_buffer);
600        hook!(0x003b5560, kal_release_buffer);
601        hook!(0x003fa4d4, memcpy);
602        hook!(0x003fb818, memcpy);
603        hook!(0x003fad94, memset);
604        hook!(0x003b7c18, get_int_ctrl_buffer);
605        hook!(0x003b7c92, free_ctrl_buffer_ext);
606        hook!(0x003b4c08, free_int_buff, "free_int_peer_buff");
607        hook!(0x003b4c50, free_int_buff, "free_int_local_para");
608        hook!(0x003b4e5c, msg_send);
609        hook!(0x00219798, errc_spv_get_rrc_state);
610        hook!(0x002185fc, errc_spv_is_errc_gemini_suspended);
611        hook!(0x003fb508, kal_assert_fail_ext);
612        hook!(0x003fb570, kal_assert_fail_ext);
613        hook!(0x003b3fc0, kal_fatal_error_handler_int);
614        hook!(0x003b4e56, destroy_int_ilm);
615        hook!(0x004d17e0, free_ctrl_buffer_ext, "qbm_free_one");
616        hook!(
617            0x001f4368,
618            pass_func,
619            "errc_com_calculate_procedure_delay_start"
620        );
621        hook!(0x001f3994, pass_func, "errc_com_stop_timer");
622        hook!(0x001f3860, pass_func, "errc_com_start_timer");
623        hook!(0x001f4d90, pass_func, "errc_conn_any_get_sec_sts");
624        hook!(0x0021ee74, pass_func, "errc_sys_evth_trace_peer");
625        hook!(0x0022c0b0, pass_func, "errc_cel_evth_trace_peer");
626        hook!(0x003fae40, pass_func);
627        hook!(0x006c4d20, memset, "asnMemSet");
628        hook!(0x001ff0bc, skip_internal_queue_loop);

(faint background text, partially hidden behind the code panel)
...ameworks: Baseband research
...SAnitized Fuzzing through Emulation.
```

## Slide 18

From exploits to frameworks: Baseband research

• 2020: BaseSAFE: Baseband SAnitized Fuzzing through Emulation.

#BHUSA @BlackHatEvents


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 82/100 on the text kept, 78/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
BaseSAFE / examples / errc / src / main.rs

Code | Blame        678 lines (603 loc) - 26.2 KB

592        hook!(0x3b4fc4, msg_recv, "msg_receive_extq");
593        hook!(0x3b5010, pass_func, "msg_receive_intq");
594        hook!(0x00119b68, dhl_trace);
595        hook!(0x00119768, pass_func, "dhl_peer_trace");
596        hook!(0x001fe2f0, errc_evth_dump_reserve_queue);
597        hook!(0x001f3d8c, pass_func, "errc_evth_com_timer_expiry_hdlr");
598        hook!(0x003b28a0, pass_func, "stack_get_active_module_id");
599        hook!(0x003b5478, kal_get_buffer);
600        hook!(0x003b5560, kal_release_buffer);
601        hook!(0x003fa4d4, memcpy);
602        hook!(0x003fb818, memcpy);
603        hook!(0x003fad94, memset);
604        hook!(0x003b7c18, get_int_ctrl_buffer);
605        hook!(0x003b7c92, free_ctrl_buffer_ext);
606        hook!(0x003b4c08, free_int_buff, "free_int_peer_buff");
607        hook!(0x003b4c50, free_int_buff, "free_int_local_para");
608        hook!(0x003b4e5c, msg_send);
609        hook!(0x00219798, errc_spv_get_rrc_state);
610        hook!(0x002185fc, errc_spv_is_errc_gemini_suspended);
611        hook!(0x003fb508, kal_assert_fail_ext);
612        hook!(0x003fb570, kal_assert_fail_ext);
613        hook!(0x003b3fc0, kal_fatal_error_handler_int);
614        hook!(0x003b4e56, destroy_int_ilm);
615        hook!(0x004d17e0, free_ctrl_buffer_ext, "qbm_free_one");
616        hook!(
617            0x001f4368,
618            pass_func,
619            "errc_com_calculate_procedure_delay_start"
620        );
621        hook!(0x001f3994, pass_func, "errc_com_stop_timer");
622        hook!(0x001f3860, pass_func, "errc_com_start_timer");
623        hook!(0x001f4d90, pass_func, "errc_conn_any_get_sec_sts");
624        hook!(0x0021ee74, pass_func, "errc_sys_evth_trace_peer");
625        hook!(0x0022c0b0, pass_func, "errc_cel_evth_trace_peer");
626        hook!(0x003fae40, pass_func);
627        hook!(0x006c4d20, memset, "asnMemSet");
628        hook!(0x001ff0bc, skip_internal_queue_loop);

(magnified panel, right side)
hook!(0x003fa4d4, memcpy);
hook!(0x003fb818, memcpy);
hook!(0x003fad94, memset);
hook!(0x003b7c18, get_int_ctrl_buffer);
hook!(0x003b7c92, free_ctrl_buffer_ext);
hook!(0x003b4c08, free_int_buff, "free_int_peer_buff");
hook!(0x003b4c50, free_int_buff, "free_int_local_para");
hook!(0x003b4e5c, msg_send);
hook!(0x00219798, errc_spv_get_rrc_state);
hook!(0x002185fc, errc_spv_is_errc_gemini_suspended);
hook!(0x003fb508, kal_assert_fail_ext);
hook!(0x003fb570, kal_assert_fail_ext);
hook!(0x003b3fc0, kal_fatal_error_handler_int);
hook!(0x003b4e56, destroy_int_ilm);
hook!(0x004d17e0, free_ctrl_buffer_ext, "qbm_free_one");
hook!(
    0x001f4368,
    pass_func,
    "errc_com_calculate_procedure_delay_start"
);
hook!(0x001f3994, pass_func, "errc_com_stop_timer");
hook!(0x001f3860, pass_func, "errc_com_start_timer");
hook!(0x001f4d90, pass_func, "errc_conn_any_get_sec_sts");
```

## Slide 19

### From exploits to frameworks: Baseband research

- 2020: BaseSAFE: Baseband SAnitized Fuzzing through Emulation.

- 2022: FirmWire: Transparent Dynamic Analysis for Cellular Baseband Firmware.

   - Supports Samsung Galaxy S7 – S10 (4G only!)

   - Requires manual harnessing to overcome complex baseband state.

#BHUSA @BlackHatEvents

## Slide 20

**Input rejected immediately!** From exploits to frameworks: Baseband research

• 2020: BaseSAFE: Baseband SAnitized Fuzzing through Emulation.

• 2022: FirmWire: Transparent Dynamic Analysis for Cellular Baseband Firmware.

• Supports Samsung Galaxy S7 – S10 (No 5G smartphone!)

• Requires manual harnessing to overcome complex baseband state.

#BHUSA @BlackHatEvents

## Slide 21

### Introducing Loris

- The first framework to emulate Samsung’s 5G Shannon Basebands.

• Allows symbolic analysis of basebands using angr.

• Enables automated, state-aware fuzzing of modern 4G and 5G basebands.

#BHUSA @BlackHatEvents

## Slide 22

# **Quick Demo**

#BHUSA @BlackHatEvents

## Slide 23

<u>https://drive.google.com/file/d/1oGHDfGwSLMAEBtcRmbA9bRzWGDfFbK8j/view?usp=sharing</u>


> Recovered by OCR — confidence 63/100 on the text kept, 54/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
root@S5fbf79c8d258:/firmwire# ./firmwire.py --shannon-loader-external_peripherals 1 --raw-asm-logging ./modem_files/CP_G991BXXSCGXF5_CP26834843_MQB82095378_REV@1_user_Low_ship_MULTI_CERT.t
```

## Slide 24

# **How did we get here?**

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 86/100 on the text kept, 57/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
BRIEFINGS SEE No
How did we get here?
```

## Slide 25

### In search of 5G NAS task: Task Metadata

- Samsung ShannonOS runs over 100 tasks:

   - Samsung Galaxy S21 contains 120+ tasks.

   - Google Pixel 6 contains 140+ tasks.

\```
0x00: TaskStruct
.....
0x10: Stackbase
.....
\```

\```
0x24: Name Pointer
.....
\```

- The metadata can be found from function that creates `‘mainTask’` .

- A global array stores the TaskStructs for all tasks.

\```
0x2c: Stacksize
0x30: Main Function
0x34: Pre-main Function
.....
\```

\```
0x140: Subtask
.....
\```

\```
0x240: End of structure
\```

#BHUSA @BlackHatEvents

## Slide 26

|MSD_OT|CDMOT|PBM|LteRrm|SNDCP|IMS_CC|
|---|---|---|---|---|---|
|L1HOT|L2HPDCPRXDELIV_OT|DS_PBM|LTE_L1LC|REG_SAP|LBS|
|L2LTXOT|L2LMACTXPROXY_OT|ATI|LteRrc|AS_SAP|SHM|
|L1OT|L2LMACTXENC_OT|MTI|LteRrc_DS|SMS_SAP|UL2CC|
|L2LRXOT|AsyncJob|SMS|LTEL2LRx|CC_SS_SAP|UL2DL|
|L2HTXOT|CLM|CC|LTEL2LTx|SIM_SAP|UL2UL|
|L2HRXOT|Acpm|MM|LTEL2HTx|DBG_SAP|UDATA|
|L3OT|Default|SM|LTEL2HRx|DS_REG_SAP|UBMCTask|
|NASOT|DM|SS|LTEL2MON|DS_AS_SAP|ephyFramework|
|QMOT|DM_TX|L1C|LTE_TLP|DS_SMS_SAP|syncTask|
|PSSOT|BDA|PPP|LTE_MTM|DS_CC_SS_SAP|recMailTask|
|PPPCOT|CIQD|GDA|NR_MTM|DS_SIM_SAP|sendMailTask|
|PPPTOT|CIQD_FE|CDH|LTE_DM|DS_DBG_SAP|BTL|
|PPPROT|Background|VSUP|EDFS|MMC|SecuCh|
|L2HPDCPTX_OT|TpTest|VCG|URRC|MMC_IF|Background1|
|L2LMACTX_OT|TaskReg|VCE|HSPA_CALIBRATION|SR_IF|Background2|
|L2HRLCRX_OT|DBGUNS|SAEL3|LLC|LTE_MMC_GL1|Background3|
|L2HRLCRETX_OT|DBGCMD|DS_SAEL3|GRR|USAT|UDC|
|L2LMACRX_OT|DBGCMD2|PDNMGR|RLC|DS_USAT|SHUB_MSG|
|L2HPDCPRX_OT|InitPacketHandler|SIM|GMAC|LTE_TCPIP|SSH|
|L2HRLCTX_OT|PacketHandler|DS_SIM|GLAPD|LTE_SISO_ASYNC|CPCOP|

## Slide 27

|**MSD_OT**|**CDMOT**|PBM|LteRrm|SNDCP|IMS_CC|
|---|---|---|---|---|---|
|**L1HOT**|**L2HPDCPRXDELIV_OT**|DS_PBM|LTE_L1LC|REG_SAP|LBS|
|**L2LTXOT**|**L2LMACTXPROXY_OT**|ATI|LteRrc|AS_SAP|SHM|
|**L1OT**|**L2LMACTXENC_OT**|MTI|LteRrc_DS|SMS_SAP|UL2CC|
|**L2LRXOT**|**AsyncJob**|SMS|LTEL2LRx|CC_SS_SAP|UL2DL|
|**L2HTXOT**|CLM|CC|LTEL2LTx|SIM_SAP|UL2UL|
|**L2HRXOT**|Acpm|MM|LTEL2HTx|DBG_SAP|UDATA|
|**L3OT**|Default|SM|LTEL2HRx|DS_REG_SAP|UBMCTask|
|**NASOT**|DM|SS|LTEL2MON|DS_AS_SAP|ephyFramework|
|**QMOT**|DM_TX|L1C|LTE_TLP|DS_SMS_SAP|syncTask|
|**PSSOT**|BDA|PPP|LTE_MTM|DS_CC_SS_SAP|recMailTask|
|**PPPCOT**|CIQD|GDA|**NR_MTM**|DS_SIM_SAP|sendMailTask|
|**PPPTOT**|CIQD_FE|CDH|LTE_DM|DS_DBG_SAP|BTL|
|**PPPROT**|Background|VSUP|EDFS|MMC|SecuCh|
|**L2HPDCPTX_OT**|TpTest|VCG|URRC|MMC_IF|**Background1**|
|**L2LMACTX_OT**|TaskReg|VCE|HSPA_CALIBRATION|SR_IF|**Background2**|
|**L2HRLCRX_OT**|DBGUNS|SAEL3|LLC|LTE_MMC_GL1|**Background3**|
|**L2HRLCRETX_OT**|DBGCMD|DS_SAEL3|GRR|USAT|**UDC**|
|**L2LMACRX_OT**|DBGCMD2|PDNMGR|RLC|DS_USAT|SHUB_MSG|
|**L2HPDCPRX_OT**|InitPacketHandler|SIM|GMAC|LTE_TCPIP|SSH|
|**L2HRLCTX_OT**|PacketHandler|DS_SIM|GLAPD|LTE_SISO_ASYNC|CPCOP|

## Slide 28

|**MSD_OT**|**CDMOT**|PBM|LteRrm|SNDCP|IMS_CC|
|---|---|---|---|---|---|
|**L1HOT**|**L2HPDCPRXDELIV_OT**|DS_PBM|LTE_L1LC|REG_SAP|LBS|
|**L2LTXOT**|**L2LMACTXPROXY_OT**|ATI|LteRrc|AS_SAP|SHM|
|**L1OT**|**L2LMACTXENC_OT**|MTI|LteRrc_DS|SMS_SAP|UL2CC|
|**L2LRXOT**|**AsyncJob**|SMS|LTEL2LRx|CC_SS_SAP|UL2DL|
|**L2HTXOT**|CLM|CC|LTEL2LTx|SIM_SAP|UL2UL|
|**L2HRXOT**|Acpm|MM|LTEL2HTx|DBG_SAP|UDATA|
|**L3OT**|Default|SM|LTEL2HRx|DS_REG_SAP|UBMCTask|
|**NASOT**|DM|SS|LTEL2MON|DS_AS_SAP|ephyFramework|
|**QMOT**|DM_TX|L1C|LTE_TLP|DS_SMS_SAP|syncTask|
|**PSSOT**|BDA|PPP|LTE_MTM|DS_CC_SS_SAP|recMailTask|
|**PPPCOT**|CIQD|GDA|**NR_MTM**|DS_SIM_SAP|sendMailTask|
|**PPPTOT**|CIQD_FE|CDH|LTE_DM|DS_DBG_SAP|BTL|
|**PPPROT**|Background|VSUP|EDFS|MMC|SecuCh|
|**L2HPDCPTX_OT**|TpTest|VCG|URRC|MMC_IF|**Background1**|
|**L2LMACTX_OT**|TaskReg|VCE|HSPA_CALIBRATION|SR_IF|**Background2**|
|**L2HRLCRX_OT**|DBGUNS|SAEL3|LLC|LTE_MMC_GL1|**Background3**|
|**L2HRLCRETX_OT**|DBGCMD|DS_SAEL3|GRR|USAT|**UDC**|
|**L2LMACRX_OT**|DBGCMD2|PDNMGR|RLC|DS_USAT|SHUB_MSG|
|**L2HPDCPRX_OT**|InitPacketHandler|SIM|GMAC|LTE_TCPIP|SSH|
|**L2HRLCTX_OT**|PacketHandler|DS_SIM|GLAPD|LTE_SISO_ASYNC|CPCOP|

## Slide 29

|**MSD_OT**|**CDMOT**|PBM|LteRrm|SNDCP|IMS_CC|
|---|---|---|---|---|---|
|**L1HOT**|**L2HPDCPRXDELIV_OT**|DS_PBM|LTE_L1LC|REG_SAP|LBS|
|**L2LTXOT**|**L2LMACTXPROXY_OT**|ATI|LteRrc|AS_SAP|SHM|
|**L1OT**|**L2LMACTXENC_OT**|MTI|LteRrc_DS|SMS_SAP|UL2CC|
|**L2LRXOT**|**AsyncJob**|SMS|LTEL2LRx|CC_SS_SAP|UL2DL|
|**L2HTXOT**|CLM|CC|LTEL2LTx|SIM_SAP|UL2UL|
|**L2HRXOT**|Acpm|MM|LTEL2HTx|DBG_SAP|UDATA|
|**L3OT**|Default|SM|LTEL2HRx|DS_REG_SAP|UBMCTask|
|**NASOT**|DM|SS|LTEL2MON|DS_AS_SAP|ephyFramework|
|**QMOT**|DM_TX|L1C|LTE_TLP|DS_SMS_SAP|syncTask|
|**PSSOT**|BDA|PPP|LTE_MTM|DS_CC_SS_SAP|recMailTask|
|**PPPCOT**|CIQD|GDA|**NR_MTM**|DS_SIM_SAP|sendMailTask|
|**PPPTOT**|CIQD_FE|CDH|LTE_DM|DS_DBG_SAP|BTL|
|**PPPROT**|Background|VSUP|EDFS|MMC|SecuCh|
|**L2HPDCPTX_OT**|TpTest|VCG|URRC|MMC_IF|**Background1**|
|**L2LMACTX_OT**|TaskReg|VCE|HSPA_CALIBRATION|SR_IF|**Background2**|
|**L2HRLCRX_OT**|DBGUNS|SAEL3|LLC|LTE_MMC_GL1|**Background3**|
|**L2HRLCRETX_OT**|DBGCMD|DS_SAEL3|GRR|USAT|**UDC**|
|**L2LMACRX_OT**|DBGCMD2|PDNMGR|RLC|DS_USAT|SHUB_MSG|
|**L2HPDCPRX_OT**|InitPacketHandler|SIM|GMAC|LTE_TCPIP|SSH|
|**L2HRLCTX_OT**|PacketHandler|DS_SIM|GLAPD|LTE_SISO_ASYNC|CPCOP|

## Slide 30

**MSD_OT CDMOT** PBM LteRrm SNDCP IMS_CC **L1HOT L2HPDCPRXDELIV_OT** DS_PBM LTE_L1LC REG_SAP LBS **L2LTXOT L2LMACTXPROXY_OT** ATI LteRrc AS_SAP SHM **L1OT L2LMACTXENC_OT** MTI LteRrc_DS SMS_SAP UL2CC **L2LRXOT AsyncJob** SMS LTEL2LRx CC_SS_SAP UL2DL **L2HTXOT** CLM CC LTEL2LTx SIM_SAP UL2UL **L2HRXOT** Acpm MM LTEL2HTx DBG_SAP UDATA **L3OT** Default SM LTEL2HRx DS_REG_SAP UBMCTask **NASOT** DM <u>SS LTEL2MON</u> DS_AS_SAP ephyFramework **QMOT** DM_TX L1C **NASOT** LTE_TLP DS_SMS_SAP syncTask **PSSOT** BDA ~~PPP LTE_MTM~~ DS_CC_SS_SAP recMailTask **PPPCOT** CIQD GDA **NR_MTM** DS_SIM_SAP sendMailTask **PPPTOT** CIQD_FE CDH LTE_DM DS_DBG_SAP BTL **PPPROT** Background VSUP EDFS MMC SecuCh **L2HPDCPTX_OT** TpTest VCG URRC MMC_IF **Background1 L2LMACTX_OT** TaskReg VCE HSPA_CALIBRATION SR_IF **Background2 L2HRLCRX_OT** DBGUNS SAEL3 LLC LTE_MMC_GL1 **Background3 L2HRLCRETX_OT** DBGCMD DS_SAEL3 GRR USAT **UDC L2LMACRX_OT** DBGCMD2 PDNMGR RLC DS_USAT SHUB_MSG **L2HPDCPRX_OT** InitPacketHandler SIM GMAC LTE_TCPIP SSH **L2HRLCTX_OT** PacketHandler DS_SIM GLAPD LTE_SISO_ASYNC CPCOP

## Slide 31

#### Building an emulator: From Cortex-R to Cortex-A

**Memory layout**

- Cortex-A lacks an MPU; requires extracting MMU tables for memory mappings.

Set TTBR0 co-processor register

\```
ldrr0, =page_table_address
mcr
p15, 0x0, r0, cr2, cr0, 0x0
\```

#BHUSA @BlackHatEvents

## Slide 32

Building an emulator: From Cortex-R to Cortex-A **Memory layout**

- Cortex-A lacks an MPU; requires extracting MMU tables for memory mappings.

\```
r0= virtual address
r1= physical address | perm| attr
str
r1, [page_table_address,r0, lsr#18]
\```

Upper bits of virtual address as offset

#BHUSA @BlackHatEvents

## Slide 33

#### Building an emulator: From Cortex-R to Cortex-A

###### **Memory layout**

- Cortex-A lacks an MPU; requires extracting MMU tables for memory mappings.

\```
r0= virtual address
r1= physical address | perm| attr
str
r1, [page_table_address,r0, lsr#18]
\```

###### Boot Stage Translation

\```
ldrr0, =page_table_address
mcr
p15, 0x0, r0, cr2, cr0, 0x0
\```

\```
00000000 -00100000 rwx
40000000 -58800000 rwx
80000000 -86000000 rw-
87000000 -87100000 rw-
87200000 -87300000 rw-
88100000 -88200000 rw-
8f000000 -9f000000 rw-
\```

#BHUSA @BlackHatEvents

## Slide 34

#### Building an emulator: From Cortex-R to Cortex-A

###### **Memory layout**

- Cortex-A lacks an MPU; requires extracting MMU tables for memory mappings.

\```
r0= virtual address
r1= physical address | perm| attr
str
r1, [page_table_address,r0, lsr#18]
\```

\```
ldrr0, =page_table_address
mcr
p15, 0x0, r0, cr2, cr0, 0x0
\```

\```
00000000 -00100000 r-x
40000000 -40100000 rw-
40100000 –42b00000 r-x
42b00000 -49d00000 rw-
49d00000 -4a700000 r---
4a700000 -4d800000 rw-
50000000 -57e00000 rw-
80000000 -86000000 rw-
87000000 -87100000 rw-
87200000 -87300000 rw-
88000000 -88300000 rw-
8a000000 -8b000000 rw-
8f000000 -9f000000 rw-
c0000000 -e0000000 rw-
e0000000 -e8000000 r---
e8000000 -f0000000 rw-
\```

#BHUSA @BlackHatEvents

## Slide 35

#### Building an emulator: From Cortex-R to Cortex-A **Timers**

- Shannon Timer: Well reverse engineered already

   - ShannonEE (G. Hernandez – hardwear.io 22)

- But new devices use 8 timers instead of 6

- And new interrupt handler is required: Cortex-A15MPCore

- Exynos Multi Core timer (MC timer) is utilized for first time.

#BHUSA @BlackHatEvents

## Slide 36

# **Back at it: The 5G NAS Task**

#BHUSA @BlackHatEvents

## Slide 37

Starting at the main function


> Recovered by OCR — confidence 89/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Starting at the main function
24 dof
25
26
27
28
29
30
31
piVar3 = (int *)param_1[1];
if (cVar1 == '\v') {
iVar2 = (*k(code *k)(xpiVar3 + 0x14))(piVar3);
piVar3 = (int *)param_1[1];
if (iVar2 == 0) {
*(undefined1 *)(piVar3 + 8) = 0;
33
34
35
36
37
38
39
41
42
43
44
45
46
47
param_1[1] = 0;
goto LAB_42bfc5cQ;
}
if ((char)piVar3[8] == '\x@3') {
goto LAB_42bfc5be;
}
*(undefined1 *)(piVar3 + 8) = 1;
}
else {
if (piVar3 != (int *)@x@) {
if ((char)piVar3[8] != '\x@3') goto LAB_42bfc5d6;
goto LAB_42bfc5be;
}
49
50
51
52
53
54
55
56
57
if (param_1[5] == @) {
goto LAB_42bfc604;
}
param_1[1] = *(int *)param_1[9];
FUN_42470974((int)(param_1 + 3),0);
piVar3 = (int *)param_1[1];
if (piVar3 == (int *)@x@) {
58LAB_42bfc604:
59
60
61
62
FUN_423f495c( (int) local_38) ;
return xb;
}
}
63LAB_42bfc5d6:
64
65
66
67
68
*(undefined1 *)(piVar3 + 8) = 1;
*(undefined1 *)(param_1 + 2) = *(undefined1 *)(param_i[1] + @x15);
cVar1 = (+*«(code *x)(*(int *)param_1[1] + 0x10))();
} while( true );
```

## Slide 38

• You see these a lot of times: • It’s easy. They’re function calls at some addresses.


> Recovered by OCR — confidence 85/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
¢ You see these a lot of times:
e It’s easy. They’re function calls at
some addresses.
FUN_42430370( (int) local_38) ;
FUN_42470974((int)(param_1 + 3),@);
```

## Slide 39

### What About This?

#BHUSA @BlackHatEvents

## Slide 40

### What About This?

##### `this`

#BHUSA @BlackHatEvents

## Slide 41

### What About This?

##### `this->-vtable`

#BHUSA @BlackHatEvents

## Slide 42

### What About This?

##### `this->-vtable[4]`

#BHUSA @BlackHatEvents

## Slide 43

### We Can Improve It:

#BHUSA @BlackHatEvents

## Slide 44

### And Even Something Better

#BHUSA @BlackHatEvents

## Slide 45

### Harnessing The NAS task

• Searching for message names revealed some

#BHUSA @BlackHatEvents


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 80/100 on the text kept, 77/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
black hat BRIEFINGS

Harnessing The NAS task

- Searching for message names revealed some

s_[N_:MM,%d]_!!FAKE-TESTHARNESS!!_S_407442c2    XREF[1]:     42d70860(*)
    ds              "[N :MM,%d] !!FAKE-TESTHARNESS!! SEND : MM_RRC_DATA_IND (SEUCURITY COMMAND)"

s_[N_:MM,%d]_!!FAKE-TESTHARNESS!!_S_4074430d    XREF[1]:     42d7087c(*)
    ds              "[N :MM,%d] !!FAKE-TESTHARNESS!! SEND : MM_RRC_DATA_IND (AUTHENTICATION REQUEST)"

s_[N_:MM,%d]_!!FAKE-TESTHARNESS!!_S_4074435d    XREF[1]:     42d70898(*)
    ds              "[N :MM,%d] !!FAKE-TESTHARNESS!! SEND : MM_RRC_DATA_IND (REGISTRATION ACCEPT)"

#BHUSA  @BlackHatEvents
```

## Slide 46

### Harnessing The NAS task

• Searching for message names revealed some

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 81/100 on the text kept, 73/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
BRIEFINGS
Harnessing The NAS task
¢ Searching for message names revealed some
ds “(IN :MM,%d] !!FAKE-TESTHARNESS!! SEND : MM_RRC_DATA_IND (SEUCURITY COMMAND)"
ds “(IN :MM,%sd] !!FAKE-TESTHARNESS!! SEND : MM_RRC_DATA_IND (AUTHENTICATION REQUEST)"
s_[N_:MM,%sd]_!!FAKE-TESTHARNESS!! S 4074435d = XREF [1]: 42d70898(*)
ds “(N :MM,%d] !!FAKE-TESTHARNESS!! SEND : MM_RRC_DATA_IND (REGISTRATION ACCEPT)"
```

## Slide 47

### Bypassing Security Checks in NAS

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 82/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
BRIEFINGS Se
Bypassing Security Checks in NAS
[cn_Nrmm.cpp] - [N :MM,@] | =============================s====s=ssssssssssssSs=5====== |
[cn_NrmmExtHd1LrRRC.cpp] - [N :MM,@] MM_RRC_DATA_IND_Handler
[cn_MmLogUtility.cpp] - [D :MM,@] SET_CTX [ USER_ACTIVITY ] : [@x@] -> [@x1]
[cn_NrmmExtHd1LrRRC.cpp] - [N :MM,@] MM_RRC_DATA_IND_Handler: dataLength: 611(Dump Max. 600)
[cn_MmLogUtility.cpp] - [D :MM,@] SET_CTX [ DL_SEC_HDR_TYPE ] : [@x@] -> [0x0]
[cn_CommonUtil.cpp] - [D :CM,@] RegistryAccessor :: Read [ NV : !NRMM.FAKE_TEST_ENABLE ]
: [cn_MmFakeTestUtil.hpp] - [N :MM,@] FakeTestAssist() : !!FAKE-TESTHARNESS!! IsFakeTestHarness : @
[cn_NrmmAirMessage.cpp] - [A :MM,@] %!EM message [DL NAS transport] with Plain message type can not be accepted
[cn_NrmmAirMessage.cpp] - [MMIQ@,CP] %!EM message [DL NAS transport] with Plain message type can not be accepted
[cn_NrmmExtHd1LrRRC.cpp] - [A :MM,@1..¥%LEM [Error] Nas Message Protection check failed
[cn_NrmmExtHd1rRRC.cpp] - [MMI0,CP3°%!2M [Error] Nas Message Protection check failed
[cn_Nrmm.cpp] - [N :MM,@] Nryim: :NrmmPostProcessMsg()
(@x41d2203d) @b110: [cn_Nrmat {tActinContext . cpp] - [D :MM,@] Add PostAction Functions
[cn_NrmmTimerCtrl.cpp] -{ \
:MM>@j” |- NRMM RUNNING TIMERS -|
[cn_NrmmEventScheduler.cpp] - [D :MM,@] |- NRMM PENDING QUEUE -|
```

## Slide 48

### Bypassing Security Checks in NAS

- Most of NAS messages are exchanged after security context establishment.

   - So, they’re encrypted and integrity protected.

- Option 1: Handling encryption and integrity during fuzz testing and program ⟶ hard, not scalable

- Option 2: Leveraging other vulnerabilities: CVE-2023-50804 ⟶ patched

- Option 3: !!FAKE-TESTHARNESS!!

#BHUSA @BlackHatEvents

## Slide 49

### Bypassing Security Checks in NAS

- Most of NAS messages are exchanged after security context establishment.

   - So, they’re encrypted and integrity protected.

- Option 1: Handling encryption and integrity during fuzz testing and program ⟶ hard, not scalable

- Option 2: Leveraging other vulnerabilities: CVE-2023-50804 ⟶ p atched

- Option 3: !!FAKE-TESTHARNESS!!

#BHUSA @BlackHatEvents

## Slide 50

# **How did we really test it?**

#BHUSA @BlackHatEvents

## Slide 51

### Why Is Testing NAS Task Difficult?

Message-processing Loop Why was the input rejected?

OTA message Failed Checks

#BHUSA @BlackHatEvents

## Slide 52

### Why Testing NAS Task is Difficult?

Message-processing Loop

States

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 80/100 on the text kept, 66/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
BRIEFINGS
Why Testing NAS Task ts Difficult?
[@.@3014][AFL_SAEL] @x4b50030b pal_MsgSendTo(SAEL3 (25)) - PALMsg(2)<@x3c7b, LTERRC (10) -> SAEL3 (19), 12 bytes>
SAEL3_MSG_LOG -----------------------------
SAEMM_PROC_NULL
SAEMM_WAIT_CELL_IN_NO_CELL States
[@.03713][SAEL3] @x429f7ba9 0b10:
[@.03937][SAEL3] @x429d946f Qb10:
[@.03976][SAEL3] @x429d946f Qb10:
[@.04006][SAEL3] @x42a4e1a3 0b10:
[@.04027][SAEL3] @x42a4e201 0b10:
[@.04036][SAEL3] @x429d946f Qb10:
[@.04061][SAEL3] @x429d94bd Qb10:
[SAECOMM_Utility.c] - -----------------------------
[SAECOMM_Utility.c] - -----------------------------
[SAEMM_ProcedureManagement.c] - || AS :
[SAECOMM_Utility.c] - ---------------------------—>
SAEQM_INST_STATE
[@.@4215][SAEL3] @x42a1fdid @b1: [SAEMM_Main.c] - Warn>++Not Allowed
[@.@4235][SAEL3] @x42a@9ec5 @b@: [SAEL3_Task.c] - Alert>External Message Handler Error - (@x3c7b)
#BHUSA
@BlackHatEvents
```

## Slide 53

### How states were handled so far

#BHUSA @BlackHatEvents

https://www.blackhat.com/us-24/briefings/schedule/#overcoming-state-finding-baseband-vulnerabilities-by-fuzzing-layer-2-40707

## Slide 54

### States in old-G vs 5G

4G States

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 86/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
BRIEFINGS Sel
States in old-G vs 5G
4G States
9 currStack = SAECOMM_Utility__CurrentStack(Sael3_CurrStack);
10, if (SAEMM_Context[currStack].state_proc_curr != SAEMM_PROC_NULL) {
2byte SAERC_GetStateErcProc(void)
3
4{
5 int iVarl;
6
8) return SAECOMM_Context_1_ARRAY_424e55d0[iVar1].ErcProc;
9}
```

## Slide 55

### States in old-G vs 5G

5G States

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 85/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
bisa hat VR
States in old-G vs 5G
5G States
int GetMmState_Wrapper(NrmmFacade x*facade,undefined4 param_2,uint param_3,uint param_4)
{
int iVar1;
return iVar1;
}
```

## Slide 56

### States in old-G vs 5G

5G States

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 85/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
States in old-G vs 5G
5G States
2int FUN_4230cd52(NrmmContextUtility *param_1,undefined4 param_2,uint param_3,uint param_4)
3
4{
6 GetMmStateFuncT *UNRECOVERED_JUMPTABLE;
7
8 UNRECOVERED_JUMPTABLE = param_1-—>mmGeneralContext—>vtable—>GetMmState;
9 /* WARNING: Could not recover jumptable at @x423@cd58. Too many branches */
10 /* WARNING: Treating indirect jump as call */
11, iVar1 = (*UNRECOVERED_JUMPTABLE) (param_1->mmGeneralContext , UNRECOVERED_JUMPTABLE, param_3,param_4) ;
12) return iVar1;
13}
```

## Slide 57

### States in old-G vs 5G

5G States

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 81/100 on the text kept, 70/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
States in old-G vs 5G
5G States
int __thiscall
cn::mm::MmGeneralContext_MacroClass: :GetMmState
(MmGeneralContext_MacroClass xthis,undefined4 param_1,uint param_2,uint param_3)
uint uVar1;
uVar1 = (this-—>field31_0x28).s1 & param_2 | (this->field31_0x28).s2 & param_3;
if (uVar1 != @) {
uVarl1 = 1;
}
return uVar1;
```

## Slide 58

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 77/100 on the text kept, 69/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
();
{
int err = (NASOT_QID, &msgPtr);
-@2958] [AFL_SAEL] @x4b50@02ef @b1000: [sael3_g991b.c] - FIRE
.@3014] [AFL_SAEL] @x4b5@03@b pal_MsgSendTo(SAEL3 (25)) - PALMsg(2)<@x3c7b, LTERRC (10) -> SAEL3 (19), 12 bytes>
.@3937] [SAEL3] @x429d946f @b10: [SAECOMM_Utility.c] - ----------------------------- SAEL3_MSG_LOG_ -----------------------------
.@3976][SAEL3] @x429d946f @b10: [SAECOMM_Utility.c] - ----------------------------- SAEMM_STATE -----------------------------
- 04006] [SAEL3] @x42a4e1qa3 @b10: [SAEMM_ProcedureManagement.c] - | PROC : SAEMM_PROC_NULL
.@4027] [SAEL3] @x42a4e201 @b10: [SAEMM_ProcedureManagement.c] - | AS : SAEMM_WAIT_CELL_IN_NO_CELL
. 04036] [SAEL3] @x429d946f @b10: [SAECOMM_Utility.c] - ----------------------------- SAEQM_INST_STATE -----------------------------
.@4215] [SAEL3] @x42a1fdid @b1: [SAEMM_Main.c] - Warn>++Not Allowed
.@4235] [SAEL3] @x42a@9ec5 @b@: [SAEL3_Task.c] - Alert>External Message Handler Error - (@x3c7b)
(MmProc != 5GMM_PROC_NULL &&
MmAS == 5GMM_IN_CONNECT)
(msgPtr->payload, msgPtr->plSize);
```

## Slide 59

##### Initialization

Message processing Loop

State Variables

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 88/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Initialization
Message
processing
Loop
void NasotMa
Task_Msg_t *msgPtr;
in (
) {
} (true);
}
void ExtMsgHandler(Task_Msg_t *msgPtr) {
msg_type = msgPtr->group >> 8 & Oxff;
(MmProc != 5GMM PROC_NULL &&
G
MmAS ==
5GMM_IN_CONNECT)
State Variables
```

## Slide 60

Symbolic Execution Preliminaries MmProc, MmAS is symbolic (can represent any value) msgPtr, msg_type, group, … are all symbolic

MmProc != 5GMM_PROC_NULL MmAS == 5GMM_IN_CONNECT

MmProc != 5GMM_PROC_NULL && MmAS == 5GMM_IN_CONNECT MmProc == 5GMM_PROC_NULL MmAS != 5GMM_IN_CONNECT

#BHUSA @BlackHatEvents

## Slide 61

## The State Explosion Problem

1
2 3
4
5
6 7

- 5 lines of code

- 7 symbolic variables (2 states)

• 4 paths

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 79/100 on the text kept, 66/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
The State Explosion Problem
void ExtMsgHandler(Task_Msg_t *msgPtr) 1if{
2msg_type = msgPtr->group3-> 8 & Oxff;
4MmProc != 5GMM _PROC_NULL &&
5SMmAS == 5GMM_IN_CONNECT)
6 7
e 5 lines of code
```

## Slide 62

## The State Explosion Problem

1
2 3
4
5
6 7
• 5 lines of code
• 7 symbolic variables (2 states)
• 4 paths
#BHUSA @BlackHatEvents

#BHUSA @BlackHatEvents

## Slide 63

## How about we only analyze state variables?

• How do we identify state variable?

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 87/100 on the text kept, 72/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
How about we only analyze state variables?
{ void ExtMsgHandler(Task_Msg_t *msgPtr) {
msg_type = msgPtr->group >> 8 & Oxff;
(MmProc != 5GMM PROC_NULL &&
MmAS 5GMM_IN_CONNECT)
¢ How do we identify state variable?
```

## Slide 64

### Is it enough?

# No

- ~100 state variables

- ~ 4 hours

- ~9k paths

• **_> 1 TB Memory consumed_**

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 89/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
blackhat
BRIEFINGS Set
Is it enough?
Hey Ali. | just saw that the RAM usage on the server is growing
N O really fast and its already 916G. Is it normal?!
e~100 state variables
e~4 hours
e~9k paths
¢> 1 TB Memory consumed
```

## Slide 65

# Is It Enough? No

• x state variables

• < 10 minutes

• Xx Paths

• > 1 TB Memory consumed

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 90/100 on the text kept, 69/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Is It Enough?
No
void (Task_Msg_t *msgPtr) {
msg_type = msgPtr->group >> 8 & Oxff;
(MmProc != 5GMM_PROC_NULL &&
```

## Slide 66

"Stateful Analysis and Fuzzing of Commercial Baseband Firmware" (IEEE S&P 2025).

- State variable identification

- Function pointer

- State variable analysis prioritization

- Use identified state variable conditions

- Grammar-aware test generation

• …

#BHUSA @BlackHatEvents

## Slide 67

### Iterative Symbolic Analysis

• Gradually increase symbolic variables

• Built upon previous results

• Ensures completed symbolic execution in each iteration

#BHUSA @BlackHatEvents

## Slide 68

### Demonstration of Iterative Symbolic Analysis

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 90/100 on the text kept, 67/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
BRIEFINGS
4
~
Demonstration of Iterative Symbolic Analysis
void (Task_Msg_t *msgPtr) {
msg_type = msgPtr->group >> 8 & Oxff;
(MmProc != 5GMM_PROC_NULL &&
MmAS 5GMM_IN_CONNECT)
```

## Slide 69

### Iteration 1

Symbolic variables: {msgPtr} State variables: {MmProc, MmAS}

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 88/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Iteration 1
4 void tM er(Task_Msg_t *msgPtr) {
5 msg_type = msgPtr->group >> 8 & Oxff;
(MmProc != 5GMM_PROC_NULL &&
MmAS 5GMM_IN_CONNECT)
F isg(msgPtr->payload, msgPtr->plSize);
Symbolic variables: {msgPtr}
State variables: {MmProc, MmAS}
```

## Slide 70

### Iteration 1

Symbolic variables: {msgPtr} State variables: {MmProc, MmAS}

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 88/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Iteration 1
4 void tM er(Task_Msg_t *msgPtr) {
5 msg_type = msgPtr->group >> 8 & Oxff;
(MmProc != 5GMM_PROC_NULL &&
MmAS 5GMM_IN_CONNECT)
F isg(msgPtr->payload, msgPtr->plSize);
Symbolic variables: {msgPtr}
State variables: {MmProc, MmAS}
```

## Slide 71

### Iteration 1

Symbolic variables: {msgPtr} State variables: {MmProc, MmAS}

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 84/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
2 See ONN 4 y
Iteration 1
4 void tM er(Task_Msg_t *msgPtr) {
5 msg_type = msgPtr->group >> 8 & Oxff;
(MmProc != 5GMM _PROC_NULL| &&
MmAS 5GMM_IN_CONNECT)
F isg(msgPtr->payload, msgPtr->plSize);
Symbolic variables: {msgPtr}
State variables: {MmProc, MmAS}
```

## Slide 72

### Iteration 2

Symbolic variables: {msgPtr} State variables: {MmProc, MmAS}

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 88/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Iteration 2
4 void tM er(Task_Msg_t *msgPtr) {
5 msg_type = msgPtr->group >> 8 & Oxff;
(MmProc != 5GMM_PROC_NULL &&
MmAS 5GMM_IN_CONNECT)
F isg(msgPtr->payload, msgPtr->plSize);
Symbolic variables: {msgPtr}
State variables: {MmProc, MmAS}
```

## Slide 73

### Iteration 2

Symbolic variables: {msgPtr, **MmProc** } State variables: {MmProc, MmAS}

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 86/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Iteration 2
4 void tM er(Task_Msg_t *msgPtr) {
5 msg_type = msgPtr->group >> 8 & Oxff;
(MmProc != 5GMM_PROC_NULL &&
MmAS 5GMM_IN_CONNECT)
F isg(msgPtr->payload, msgPtr->plSize);
Symbolic variables: {msgPtr, MimProc}
State variables: {MmProc, MmAS}
```

## Slide 74

### Iteration 2

Symbolic variables: {msgPtr, MmProc} State variables: {MmProc, MmAS}

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 88/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Iteration 2
4 void tM er(Task_Msg_t *msgPtr) {
5 msg_type = msgPtr->group >> 8 & Oxff;
(MmProc != 5GMM_PROC_NULL &&
MmAS 5GMM_IN_CONNECT)
F isg(msgPtr->payload, msgPtr->plSize);
Symbolic variables: {msgPtr, MmProc}
State variables: {MmProc, MmAS}
```

## Slide 75

### Iteration 2

Symbolic variables: {msgPtr, MmProc} State variables: {MmProc, MmAS}

**Condition: MmProc != 5GMM_PROC_NULL**

#BHUSA @BlackHatEvents

## Slide 76

### Iteration 2

Symbolic variables: {msgPtr, MmProc} State variables: {MmProc, MmAS}

Condition: MmProc != 5GMM_PROC_NULL

#BHUSA @BlackHatEvents

## Slide 77

### Iteration 3

Symbolic variables: {msgPtr, MmProc, **MmAS** } State variables: {MmProc, MmAS}

Condition: MmProc != 5GMM_PROC_NULL

#BHUSA @BlackHatEvents

## Slide 78

### Iteration 3

Symbolic variables: {msgPtr, MmProc, MmAS} State variables: {MmProc, MmAS}

Condition: MmProc != 5GMM_PROC_NULL

#BHUSA @BlackHatEvents

## Slide 79

### Iteration 3

Symbolic variables: {msgPtr, MmProc, MmAS} State variables: {MmProc, MmAS}

Condition: MmProc != 5GMM_PROC_NULL, **MmAS == 5GMM_IN_CONNECT**

#BHUSA @BlackHatEvents

## Slide 80

### Iteration 3

Symbolic variables: {msgPtr, MmProc, MmAS} State variables: {MmProc, MmAS}

Condition: MmProc != 5GMM_PROC_NULL, MmAS == 5GMM_IN_CONNECT

#BHUSA @BlackHatEvents

## Slide 81

# **Let’s wrap it up!**

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 94/100 on the text kept, 53/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
BRIEFINGS
Let’s wrap it up!
```

## Slide 82

### Loris Architecture

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 88/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
BRIEFINGS ame
Loris Architecture
Firmware
Binary
101001
```

## Slide 83

### Loris Architecture

###### **Emulator**

- Based on FirmWire (NDSS’22)

- Added support for new 5G Exynos baseband.

#BHUSA @BlackHatEvents

## Slide 84

### Loris Architecture

- **Emulator**

- • Based on FirmWire (NDSS’22)

- • Added support for new 5G Exynos baseband.

###### **Iterative symbolic analysis**

- Sate variables detection

- • State variable analysis

- Checkpoint-based path pruning

#BHUSA @BlackHatEvents

## Slide 85

### Loris Architecture

###### **Emulator**

- Based on FirmWire (NDSS’22)

- • Added support for new 5G Exynos baseband.

###### **Iterative symbolic analysis**

- Sate variables detection

- • State variable analysis

- • Checkpoint-based path pruning

###### **Grammar-aware fuzzing**

- No seeds are required

- • Grammar-aware mutations

- • Target task state initialization

#BHUSA @BlackHatEvents

## Slide 86

### Vulnerability Discovery

- Developed a unified harness that accepts any message type with target state from our LibAFL-based fuzzer.

- The harness automatically initializes the target task and delivers the message via baseband APIs.

- We fuzzed 4G NAS (SAEL3) and 5G NAS (NASOT)

   - Samsung Galaxy S21, S20, S10, A41

   - Google Pixel 6

#BHUSA @BlackHatEvents

## Slide 87

### Discovered Seven 0-Days

- We fuzzed 4G NAS (SAEL3) and 5G NAS (NASOT)

   - Samsung Galaxy S21, S20, S10, A41

   - Google Pixel 6

- **Discovered 7 crashes, all of which were previously unknown!**

   - 5G NAS: 1 critical, 2 high, 3 moderate, 1 low

   - 4G NAS: 1 additional heap overflow but unexploitable!

- **5 CVEs:** CVE-2024-52923, CVE-2024-52924, CVE-2025-26784, CVE-2025-26785, and CVE-2025-27891.

#BHUSA @BlackHatEvents

## Slide 88

### OTA Crash Reproduction

- Used a USRP B210 with OpenAirInterface.

- Modified Open5GS as the malicious core network.

- The basebands crashed with each message.

#BHUSA @BlackHatEvents

## Slide 89

#BHUSA @BlackHatEvents

<u>https://drive.google.com/file/d/1LE6pjaaBDgyBLanu6buU56EDTLclpPka/view?usp=sharing</u>


> Recovered by OCR — confidence 90/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Capturing from Loopback: lo - oOo & SM-G991B
File Edit View Go Capture Analyze Statistics Telephony Wireless Tools Help
ip.addr == 127.0.0.5 && ngap +
No. Time Source Destination Protocol Length Info
< About phone Q
Galaxy $215G
Edit
Phone number Unknown
Product name Galaxy S21 5G
Model name SM-G991B/DS
Serial number R3CRAO53Y6J
MEI (slot 1) 350517926819870
354049176819877
MEI (slot 2
Status information
Legal information
Software information
https://drive.google.com/file/d/1LE6pjaaB DgyBLanu6buU56EDTLclpPka/view
* Loopback: lo: <live capture in progress> Packets: 3176 « Displayed: 0 (0.0%) Profile: Default
```

## Slide 90

### Real World Impact

- Discovered 0-days: stack overflow and heap overflow.

- Requirements of turning stack overflow to RCE vector:

   1. RWX stack – eXecute Never bit must be 0

   2. No stack protection – sleepy canaries

- Heap overflow can still lead to RCE; might be limited to small payloads.

   - A better gain: write-what-where primitive

#BHUSA @BlackHatEvents

## Slide 91

### Stack Canaries

stack frame 1

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 93/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
BRIEFINGS
Stack Canaries é
increasing addresses
stack
frame 1
```

## Slide 92

### Stack Canaries

stack
frame 2
stack
frame 1
increasing addresses

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 82/100 on the text kept, 63/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
BRIEFINGS
Stack Canaries é
Y
Y
Y
(av)
stack &
frame 2 ra)
O
stack
frame 1
```

## Slide 93

### Stack Canaries

stack
frame 3
stack
frame 2
stack
frame 1
increasing addresses

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 93/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
BRIEFINGS
Stack Canaries é
stack
frame 3
stack
frame 2
stack
frame 1
increasing addresses
```

## Slide 94

### Stack Canaries

stack
frame 3
…
local
stack
vars
…
frame 2
LR
stack
frame 1
increasing addresses

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 93/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
BRIEFINGS
Stack Canaries é
local
vars
LR
stack
frame 3
stack
frame 2
stack
frame 1
increasing addresses
```

## Slide 95

### Stack Canaries

stack
frame 3
…
local
stack
vars
…
frame 2
LR
stack
frame 1
increasing addresses

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 93/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
BRIEFINGS La
Stack Canaries
local
vars
LR
stack
frame 3
stack
frame 2
stack
frame 1
increasing addresses
```

## Slide 96

### Stack Canaries

stack
frame 3
…
local
42b6ba88    D1E4C0DE
stack
vars
…
frame 2
LR
abort
stack
frame 1
#BHUSA @BlackHatEvents
increasing addresses

## Slide 97

### Stack Canaries

- `42b6ba88    D1E4C0DE` • Hexspeak for “Die for Code” • Changed to a random integer during boot! • Lives in a memory page with write access!! `42b00000 - 49d00000 rw-`

local vars …

stack frame 3 stack frame 2

LR

stack frame 1

#BHUSA @BlackHatEvents

## Slide 98

### From buffer overflow to RCE

- Heap overflow can yield a clean write-what-where primitive.

   - Black Hat USA ’23

- But requires an RWX to obtain RCE.

- Return Oriented Programming (ROP) is the solution!

- Example exploit can set the `NRMM.FAKE_TEST_ENABLE` flag in the NV RAM.

#BHUSA @BlackHatEvents

## Slide 99

### Loris Covers ~200% Code

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 88/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
BRIEFINGS
Loris Covers ~200% Code
8000 16000 24000
Galaxy S10 LTE
4h 8h 12h 16h 20h 24h
Pixel 6 LTE
4h 8h 12h 16h 20h 24h
Galaxy 820 LTE
4h
4h
8h
12h 16h 20h 24h
Pixel 6 5G
8h
/
12h 16h 20h 24h
0 5000 10000 1500020000
?
Galaxy 821 LTE
4h 8h 12h 16h 20h 24h
Galaxy A41 LTE
/
4h 8h 12h 16h 20h 24h
```

## Slide 100

### Parting Thoughts

- The complexity of baseband are increasing due to generation shifts, added functionalities, and new peripherals.

- However, automated systematic analysis using insights gained from understanding these firmware leads to efficient analysis and better results.

- _Complexity_ ≠ _Better Security_

- More research is needed for baseband security (i.e., more protocols).

#BHUSA @BlackHatEvents

## Slide 101

### Thank You & Questions

Code

Paper

- Kai Tu,  Saaman Khalilollahi, Kanika Gupta,  Syed Rafiul Hussain

Ali Ranjbar aranjbar@psu.edu `aranjbar.me`

- Samsung Mobile Security

- Google Android Security

Tianchang Yang tzy5088@psu.edu `tianchang-yang.github.io`

#BHUSA @BlackHatEvents
